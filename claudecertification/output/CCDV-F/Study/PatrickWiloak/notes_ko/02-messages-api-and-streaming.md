# 02 - Messages API와 스트리밍

Messages API는 Claude의 핵심입니다. 스트리밍(streaming, 응답을 다 만들 때까지 기다리지 않고 조금씩 실시간으로 받는 방식)은 Claude 앱을 빠르게 느껴지도록 만드는 방법입니다. 이 노트에서는 두 가지를 모두 깊이 있게 다룹니다.

---

## Messages 엔드포인트

`POST /v1/messages`

`stream: false`이면 동기(synchronous, 응답이 완성될 때까지 기다렸다가 한 번에 받는) 방식입니다. `stream: true`이면 스트리밍 방식입니다.

Python SDK(SDK, 개발을 쉽게 해 주는 공식 라이브러리 모음)는 두 방식을 모두 제공합니다.

```python
client.messages.create(...)         # 동기 방식, 전체 Message를 반환
client.messages.stream(...)         # 스트리밍 컨텍스트 매니저
```

TypeScript:

```ts
client.messages.create({...});       // Message 또는 스트림을 반환
client.messages.stream({...});       // 스트리밍 헬퍼
```

---

## 대화 상태

대화는 서버에서 무상태(stateless, 서버가 이전 대화 내용을 기억하지 않음)입니다. 모든 요청에는 Claude가 보기를 원하는 전체 메시지 기록이 포함됩니다. 대화를 이어 가려면 다음과 같이 합니다.

1. user 메시지를 추가합니다
2. 전체 기록과 함께 요청을 보냅니다
3. 반환된 assistant 메시지를 추가합니다
4. 반복합니다

즉, 대화가 길어질수록 컨텍스트(context, 모델이 한 번에 참고하는 입력 전체) 비용이 늘어납니다. 긴 대화에는 컴팩션(compaction, 대화 기록을 압축하는 처리)이나 요약을 사용하십시오.

---

## 시스템 프롬프트

`system` 필드는 문자열 또는 콘텐츠 블록(content block, 메시지를 구성하는 종류별 조각) 배열을 받습니다.

```python
client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system="You are a helpful assistant.",
    messages=[{"role": "user", "content": "Hi"}],
)
```

배열 형식을 사용하면 블록마다 `cache_control`(프롬프트 캐싱(prompt caching, 반복되는 입력을 저장해 비용과 시간을 줄이는 기능) 설정)을 지정할 수 있습니다.

```python
system=[
    {"type": "text", "text": "You are a code review assistant.", "cache_control": {"type": "ephemeral"}},
    {"type": "text", "text": project_specific_context},
]
```

---

## 멀티턴 패턴

```python
history = []
while True:
    user = input("> ")
    history.append({"role": "user", "content": user})
    resp = client.messages.create(model="claude-sonnet-4-6", max_tokens=1024, messages=history)
    history.append({"role": "assistant", "content": resp.content})
    print(resp.content[0].text)
```

텍스트만이 아니라 Claude의 content 배열 전체를 항상 추가하십시오. 도구 사용(tool use, Claude가 외부 기능을 호출하는 것), thinking 및 기타 블록은 대화를 이어 가기 위해 유지되어야 합니다.

---

## 스트리밍

스트리밍은 Server-Sent Events(SSE, 서버가 클라이언트로 데이터를 연속해서 밀어 보내는 웹 표준 방식)를 사용합니다. 각 이벤트(event, 서버가 보내는 개별 알림 단위)는 `data:` 줄에 담긴 JSON(JSON, 데이터를 주고받는 텍스트 형식) 객체입니다.

### 이벤트 순서

단순한 텍스트 응답의 경우:

1. `message_start` - content가 비어 있는 초기 Message 객체를 전달합니다
2. `content_block_start` - 콘텐츠 블록 인덱스 0(type text)을 엽니다
3. `content_block_delta`(여러 번) - 각각 새 텍스트를 담은 `text_delta`를 전달합니다
4. `content_block_stop` - 블록 0을 닫습니다
5. `message_delta` - 누적 `usage`와 최종 `stop_reason`을 알립니다
6. `message_stop` - 스트림 종료

tool_use 응답의 경우:

1. `message_start`
2. `content_block_start` - type `tool_use`이며, `id`와 `name`을 포함합니다
3. `content_block_delta`(여러 번) - 도구 인수(arguments, 도구에 넘기는 입력값)를 조금씩 만들어 가는 `input_json_delta`
4. `content_block_stop`
5. `message_delta`(`stop_reason: tool_use` 포함)
6. `message_stop`

thinking 응답의 경우(확장 사고(extended thinking, 답하기 전에 단계적으로 깊이 생각하는 기능) 활성화 시):

- type `thinking`의 `content_block_start`
- 내용을 담은 `thinking_delta`가 포함된 `content_block_delta`
- 검증용 서명(signature, 내용이 변조되지 않았음을 확인하는 값)을 담은 `signature_delta`가 포함된 `content_block_delta`
- `content_block_stop`

그 다음에 일반적인 text/tool_use 블록이 이어집니다.

### Ping

서버는 연결을 유지하기 위해 `ping` 이벤트를 보낼 수 있습니다. 핸들러(handler, 이벤트를 받아 처리하는 코드)에서는 무시하십시오.

### 스트리밍 중 오류

서버가 스트림 도중에 오류를 만나면 `error` 이벤트가 발생합니다. 이를 명시적으로 처리하고, `message_stop`이 항상 도착한다고 가정하지 마십시오.

---

## 스트리밍 헬퍼

Python SDK:

```python
with client.messages.stream(model="claude-sonnet-4-6", max_tokens=1024, messages=[...]) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
    final = stream.get_final_message()
```

이 방식은 SSE 파싱(parsing, 받은 데이터를 해석하는 처리)을 대신 처리해 줍니다. 텍스트 델타(delta, 새로 추가된 부분)만 받게 되며, 마지막에 완성된 Message를 가져올 수 있습니다.

도구 사용의 경우에는 이벤트를 직접 순회하십시오.

```python
with client.messages.stream(...) as stream:
    for event in stream:
        if event.type == "content_block_start" and event.content_block.type == "tool_use":
            ...
```

TypeScript 헬퍼:

```ts
const stream = client.messages.stream({...});
stream.on("text", (delta, snapshot) => process.stdout.write(delta));
const finalMessage = await stream.finalMessage();
```

---

## 백프레셔(Backpressure)

스트리밍 소비자(consumer, 스트림을 받아 읽는 쪽)는 이벤트를 신속하게 읽어야 합니다. 읽기가 지체되면 서버 측 버퍼(buffer, 데이터를 임시로 쌓아 두는 공간)가 결국 연결을 끊을 수 있습니다(이처럼 받는 쪽의 처리 속도가 보내는 쪽에 압력을 주는 현상을 백프레셔라고 합니다). UI 렌더링(rendering, 화면에 그리는 처리)의 경우에는 큐(queue, 순서대로 쌓아 두는 대기열)를 사용해 네트워크 읽기 루프와 렌더링 루프를 분리하십시오.

---

## 재개와 pause_turn

긴 응답에서는 `stop_reason: pause_turn`이 발생할 수 있습니다. 계속하려면 부분적인 assistant 응답을 추가한 메시지를 보내 이어서 생성하도록 요청하십시오. 대부분의 앱에서는 이 상황을 보지 못하지만, 프롬프트가 매우 긴 출력을 생성할 수 있다면 방어적으로 설계하십시오.

---

## 중지 시퀀스(Stop Sequences)

`stop_sequences: ["</answer>"]`를 설정하면 Claude가 해당 문자열을 출력할 때 생성을 멈춥니다. 응답의 `stop_reason`은 `stop_sequence`가 되고, `stop_sequence` 필드에 어떤 문자열이 일치했는지 표시됩니다.

---

## Max Tokens

필수입니다. 출력(텍스트 + thinking)의 상한을 설정합니다. 작업에 따라 선택하십시오.

- 짧은 답변: 256-512
- 중간 길이 답변: 1024-2048
- 장문 생성: 4096+
- 확장 사고 활성화 시: budget_tokens + 화면에 보이는 응답을 위한 여유분

Claude가 `max_tokens`에 도달하면 응답이 잘릴 수 있습니다. 상한을 늘리거나 Claude에게 간결하게 답하도록 지시하십시오.

---

## 실습 예제

```python
from anthropic import Anthropic

client = Anthropic()

with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": "You are a concise assistant.",
            "cache_control": {"type": "ephemeral"},
        }
    ],
    messages=[{"role": "user", "content": "Explain SSE in two sentences."}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
    final = stream.get_final_message()
    print()
    print(f"Tokens: in={final.usage.input_tokens} out={final.usage.output_tokens} cache_read={final.usage.cache_read_input_tokens}")
```

---

## 흔한 실수

- 스트림을 끝까지 소비하는 것을 잊음(리소스 누수(resource leak, 사용한 자원이 해제되지 않고 남는 문제))
- `stop_reason: tool_use`를 오류로 취급함
- 응답에 텍스트 블록이 하나뿐이라고 가정함
- 시스템 프롬프트를 `messages`에 넣음
- 이어서 생성할 때 thinking 블록을 유지하지 않음
- 모델 ID를 하드코딩(hardcoding, 소스 코드에 값을 직접 써넣는 것)함

---

## 시험 대비 포인트

- 이벤트 순서와 종류
- 시스템 프롬프트를 넣는 위치
- 스트리밍과 동기 방식을 언제 사용할지
- 스트리밍 중 `usage`가 어떻게 보고되고 갱신되는지
- tool_use 응답의 수명 주기(lifecycle, 시작부터 끝까지의 흐름)

---

## 핵심 용어

- **Server-Sent Events** - 스트리밍이 사용하는 전송 방식. 각 이벤트는 data: 줄에 담긴 JSON 객체입니다.
- **message_start** - 첫 번째 스트리밍 이벤트로, content가 비어 있는 초기 Message 객체를 전달합니다.
- **무상태 대화(Stateless conversation)** - 서버가 기록을 보관하지 않으므로, 모든 요청에 Claude가 보기를 원하는 전체 메시지 기록을 포함해야 합니다.
- **stop_sequences** - Claude가 출력하면 생성을 멈추게 하는 문자열. stop_reason이 stop_sequence가 됩니다.
