# 01 - Claude API 기초

Claude API(API, 프로그램끼리 기능을 주고받기 위한 창구)는 겉으로 보이는 기능은 적지만 깊이가 있습니다. 이 노트에서는 기초가 되는 내용인 인증, 모델, 요청 형식, 그리고 Messages API의 개념적 모델을 다룹니다.

---

## 인증

Anthropic이 직접 제공하는 퍼스트파티(first-party, 제공 회사가 직접 운영하는) API는 API 키(API key, 사용자를 식별하는 비밀 문자열)를 사용합니다.

```
x-api-key: sk-ant-...
anthropic-version: 2023-06-01
```

`anthropic-version` 헤더(header, 요청에 덧붙이는 부가 정보)는 API 계약(API contract, API가 어떻게 동작할지에 대한 약속)을 특정 버전으로 고정합니다. Anthropic은 기존 계약을 깨뜨리지 않으며, 새로운 동작은 새 버전이나 선택적으로 사용하는(opt-in) 베타 헤더를 통해서만 제공됩니다.

베타 기능은 `anthropic-beta` 헤더로 활성화 여부가 제어됩니다. 예를 들면 다음과 같습니다.

```
anthropic-beta: prompt-caching-2024-07-31
```

(구체적인 베타 헤더 문자열은 바뀔 수 있으므로 최신 문서를 확인하십시오.)

Bedrock과 Vertex는 API 키가 아니라 각각 IAM 자격 증명(IAM credentials, AWS의 권한 관리 체계에서 발급하는 인증 정보)과 Google 서비스 계정(service account, 프로그램이 사용하는 Google 계정)을 사용합니다.

---

## 기본 URL

퍼스트파티 API:

```
https://api.anthropic.com
```

Messages 엔드포인트(endpoint, 요청을 보내는 API의 주소)는 `POST /v1/messages`입니다. SDK(SDK, 개발을 쉽게 해 주는 공식 라이브러리 모음)는 기본적으로 이 기본 URL을 사용합니다.

---

## 모델

현재 세대 모델 ID(2026년):

| 모델 | 강점 | 사용 시점 |
|---|---|---|
| claude-opus-4-6 | 가장 깊은 추론 | 어려운 계획 수립, 복잡한 종합 |
| claude-sonnet-4-6 | 균형 잡힌 주력 모델 | 대부분의 앱에서 기본값 |
| claude-haiku-4-5 | 속도, 처리량, 비용 | 분류, 라우팅(routing, 요청을 알맞은 곳으로 나눠 보내기), 서브 에이전트(sub-agent, 주 에이전트가 일을 맡기는 보조 AI) |

모델 ID는 항상 설정(config)에서 매개변수로 지정하고, 소스 코드에 직접 써넣지(hardcode) 마십시오. 새 버전은 정기적으로 출시됩니다.

---

## 요청 형식

유효한 최소 요청:

```json
{
  "model": "claude-sonnet-4-6",
  "max_tokens": 1024,
  "messages": [
    {"role": "user", "content": "Hello"}
  ]
}
```

필수 필드:

- `model`
- `max_tokens` - 응답 길이의 상한이며, thinking과 텍스트를 모두 포함합니다(토큰(token, 모델이 글자를 처리하는 단위) 수 기준)
- `messages` - user / assistant 차례(turn)가 번갈아 이어지는 목록

선택 필드:

- `system` - 최상위 시스템 프롬프트(system prompt, 모델의 역할과 규칙을 정해 주는 지시문). 문자열 또는 콘텐츠 블록 배열
- `temperature` - 0~1
- `top_p`, `top_k` - temperature 대신 쓸 수 있는 샘플링(sampling, 다음에 나올 단어를 확률적으로 고르는 방식) 방법
- `stop_sequences` - 문자열 배열. 이 문자열이 출력되면 응답이 멈춥니다
- `stream` - 불리언(boolean, 참/거짓 값). SSE 스트리밍(streaming, 응답을 조금씩 실시간으로 받는 방식)
- `tools` 및 `tool_choice` - 도구 사용(tool use, Claude가 외부 기능을 호출하는 것) 설정
- `thinking` - 확장 사고(extended thinking, 답하기 전에 단계적으로 깊이 생각하는 기능) 설정
- `metadata` - 악용 추적을 위한 user_id. 여기에 PII(개인 식별 정보)를 넣지 마십시오

---

## 역할(Role)

- `system` - `messages` 안의 역할이 아니라 최상위 필드입니다. 페르소나, 제약 조건, 형식을 설정합니다.
- `user` - 사람의 입력이며, tool_result 블록도 포함합니다.
- `assistant` - Claude의 이전 차례이며, tool_use 블록도 포함합니다.

첫 번째 메시지는 반드시 `user`여야 합니다. 역할은 번갈아 나와야 합니다. 배열의 마지막 메시지가 Claude가 응답할 대상을 결정합니다.

---

## 콘텐츠 블록

각 메시지에는 `content`가 있으며, 이는 문자열(단일 텍스트 블록의 축약형) 또는 타입이 지정된 콘텐츠 블록(content block, 메시지를 구성하는 종류별 조각)의 배열입니다.

- `text` - 일반 텍스트
- `image` - base64(base64, 이진 데이터를 문자로 바꾸는 인코딩 방식)로 인코딩된 데이터, URL 또는 file_id
- `document` - base64, URL 또는 file_id로 전달하는 PDF 등의 문서
- `tool_use` - 도구 실행을 요청하는 Claude의 요청(assistant 메시지 안)
- `tool_result` - tool_use에 대한 사용자 측 응답(user 메시지 안)
- `thinking` - Claude의 내부 추론(확장 사고를 사용한 assistant 메시지 안)

한 메시지 안에 여러 타입이 섞이는 것은 일반적입니다. assistant 메시지에는 `thinking` 블록과 `tool_use` 블록이 함께 들어 있는 경우가 많습니다.

---

## 응답 형식

```json
{
  "id": "msg_...",
  "type": "message",
  "role": "assistant",
  "model": "claude-sonnet-4-6",
  "content": [{"type": "text", "text": "Hi there"}],
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 12,
    "output_tokens": 5,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0
  }
}
```

`content` 배열에는 여러 블록이 들어 있을 수 있습니다. 항상 반복문으로 순회하고, 텍스트 블록이 하나뿐이라고 가정하지 마십시오.

---

## 중지 이유(Stop Reasons)

- `end_turn` - 자연스럽게 완료됨
- `max_tokens` - 상한에 도달함. 응답이 불완전할 수 있음
- `stop_sequence` - 설정한 중지 시퀀스에 도달함
- `tool_use` - Claude가 도구 실행을 원함
- `pause_turn` - 긴 응답이 일시 중지됨(드묾. 이어서 진행하면 재개됨)
- `refusal` - 모델이 응답을 거부함

`tool_use`는 오류가 아니라 처리 루프(loop, 반복 처리 흐름)의 한 상태로 다루십시오. `refusal`은 최종 상태로 다루고, 오류인 것처럼 재시도하지 마십시오.

---

## 토큰 계산

요청을 보내기 전에 토큰 계산 엔드포인트를 사용해 요청 크기를 추정하십시오.

```
POST /v1/messages/count_tokens
```

Messages와 동일한 본문을 받아 `input_tokens`를 반환합니다. 컨텍스트(context, 모델이 한 번에 참고하는 입력 전체) 예산 관리와 레이트 리밋(rate limit, 일정 시간당 요청 횟수 제한) 계획에 유용합니다.

---

## Temperature, Top-P, Top-K

- `temperature` 0 = 가장 결정적(deterministic, 같은 입력에 같은 결과가 나오는 성질)임(그래도 실행할 때마다 바이트 단위로 완전히 같지는 않음). 1 = 기본값. 높을수록 = 더 다양함
- `top_p`(누클리어스 샘플링(nucleus sampling, 확률 합이 일정 값에 이를 때까지의 후보만 고르는 방식)) - temperature의 대안
- `top_k` - 각 단계에서 상위 K개 토큰으로 제한

하나만 사용하십시오. 대부분의 프로덕션(production, 실제 서비스 운영 환경) 앱에서는 기본 temperature로 충분합니다. 추출 작업에는 낮게, 창작 작업에는 높게 설정하십시오.

---

## 멱등성(Idempotency)

Messages API는 API 수준에서 기본적으로 멱등성(idempotency, 같은 요청을 여러 번 보내도 결과가 한 번 보낸 것과 같음을 보장하는 성질)을 제공하지 않습니다. 최대 한 번(at-most-once) 실행 보장이 필요하다면 클라이언트 측에서 멱등성을 관리하십시오. 요청의 해시(hash, 데이터를 짧은 고유 값으로 요약한 것)와 응답을 저장해 두고, 재시도 시에는 저장된 응답을 반환하면 됩니다.

---

## 버전 관리 원칙

- `anthropic-version`을 알려진 값으로 고정하십시오
- 모델 ID는 소스 코드가 아니라 설정에서 고정하십시오
- 의존하는 모든 베타 헤더를 문서화하십시오
- 변경 사항을 파악하기 위해 Anthropic 릴리스 노트를 추적하십시오

---

## 다음 단계

- 노트 02: Messages API와 스트리밍 심화
- 노트 03: 도구 사용 수명 주기
- 노트 04: 캐싱과 배치 처리
- 노트 05: 파일, 인용, 멀티모달
- 노트 06: 오류, 레이트 리밋, 재시도
- 노트 07: SDK

이 노트를 이해했다면 Claude를 호출할 수 있습니다. 나머지는 이를 조합하는 일입니다.

---

## 핵심 용어

- **max_tokens** - 응답 길이에 대한 필수 상한이며, thinking과 텍스트를 모두 포함합니다.
- **콘텐츠 블록(Content block)** - 타입이 지정된 메시지의 한 조각: text, image, document, tool_use, tool_result 또는 thinking.
- **stop_reason** - 생성이 끝난 이유를 알려 주는 필드: end_turn, max_tokens, stop_sequence, tool_use, pause_turn, refusal 또는 model_context_window_exceeded.
- **anthropic-version 헤더** - API 계약을 고정하여 기존 동작이 계속 작동하도록 합니다. 새로운 동작은 새 버전이나 선택적으로 사용하는 베타 헤더를 통해 제공됩니다.
