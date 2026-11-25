# 07 - SDK: Python, TypeScript, 그리고 CLI

Anthropic은 Python과 TypeScript용 공식(first-party, 제조사가 직접 제공하는) SDK(Software Development Kit, 프로그램에서 API를 쉽게 호출하도록 돕는 개발 도구 모음)와, 빠른 실험을 위한 CLI(Command Line Interface, 터미널에서 명령어로 조작하는 도구)를 제공합니다. 시험에서는 스트리밍(streaming, 응답을 다 만들기 전에 조금씩 받아 보는 방식) 헬퍼(helper, 자주 쓰는 작업을 간편하게 해 주는 보조 기능), 비동기(async, 응답을 기다리는 동안 다른 작업을 병행하는 방식) 클라이언트(client, API에 요청을 보내는 프로그램 쪽 객체), 그리고 Bedrock / Vertex 하위 클라이언트를 포함해 SDK를 관용적인(idiomatic, 해당 언어·도구에서 권장되는 자연스러운) 방식으로 능숙하게 사용할 수 있기를 기대합니다.

---

## Python SDK

설치:

```
pip install anthropic
```

### 동기 클라이언트

```python
from anthropic import Anthropic

client = Anthropic()  # 환경 변수에서 ANTHROPIC_API_KEY를 읽음
msg = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hi"}],
)
print(msg.content[0].text)
```

### 비동기 클라이언트

```python
from anthropic import AsyncAnthropic
import asyncio

aclient = AsyncAnthropic()

async def main():
    msg = await aclient.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": "Hi"}],
    )
    print(msg.content[0].text)

asyncio.run(main())
```

팬아웃(fan-out, 여러 요청을 동시에 흩뿌려 보내는 방식)에는 비동기를 사용합니다(병렬 요청, 에이전트(agent, 스스로 판단하며 작업을 수행하는 AI 프로그램) 워커(worker, 작업을 나눠 처리하는 실행 단위)).

### 스트리밍 헬퍼

```python
with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Tell me a story"}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
    final = stream.get_final_message()
```

비동기 스트리밍:

```python
async with aclient.messages.stream(...) as stream:
    async for text in stream.text_stream:
        print(text, end="", flush=True)
```

tool_use(도구 사용, 모델이 외부 기능을 호출하는 것) 스트리밍의 경우 `for event in stream:`으로 이벤트(event, 스트림으로 전달되는 개별 신호 단위)를 직접 순회합니다.

### 설정 옵션

```python
client = Anthropic(
    api_key="...",          # 또는 환경 변수
    base_url="...",         # 프록시용
    timeout=30.0,
    max_retries=2,          # SDK 수준 재시도
    default_headers={...},
)
```

### 요청별 옵션

```python
client.with_options(timeout=60.0, max_retries=0).messages.create(...)
```

### 오류 유형

```python
from anthropic import (
    APIError, APIConnectionError, APITimeoutError,
    BadRequestError, AuthenticationError, PermissionDeniedError,
    NotFoundError, RateLimitError, InternalServerError,
)
```

### Bedrock 클라이언트

```python
from anthropic import AnthropicBedrock

client = AnthropicBedrock(
    aws_region="us-east-1",
    # AWS 자격 증명은 환경 변수, 프로필 또는 IAM 역할로 제공
)
msg = client.messages.create(
    model="anthropic.claude-sonnet-4-6-YYYYMMDD-v1:0",
    max_tokens=1024,
    messages=[...],
)
```

### Vertex 클라이언트

```python
from anthropic import AnthropicVertex

client = AnthropicVertex(region="us-east5", project_id="my-gcp-project")
msg = client.messages.create(
    model="claude-sonnet-4-6@YYYYMMDD",
    max_tokens=1024,
    messages=[...],
)
```

Messages 인터페이스(interface, 호출 방법의 형식)는 세 클라이언트 모두에서 동일합니다.

---

## TypeScript SDK

설치:

```
npm install @anthropic-ai/sdk
```

### 기본 사용법

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();  // ANTHROPIC_API_KEY를 읽음

const msg = await client.messages.create({
  model: "claude-sonnet-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hi" }],
});

console.log(msg.content[0]);
```

### 스트리밍

```ts
const stream = client.messages.stream({
  model: "claude-sonnet-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Tell me a story" }],
});

stream.on("text", (delta) => process.stdout.write(delta));

const final = await stream.finalMessage();
```

또는 비동기 반복(async iteration, 데이터가 도착할 때마다 하나씩 꺼내 처리하는 방식):

```ts
for await (const event of stream) {
  if (event.type === "content_block_delta") { ... }
}
```

### 설정

```ts
const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
  baseURL: "...",
  timeout: 30_000,
  maxRetries: 2,
});
```

### 오류 처리

```ts
import { APIError, RateLimitError } from "@anthropic-ai/sdk";

try {
  await client.messages.create({...});
} catch (err) {
  if (err instanceof RateLimitError) { ... }
  else if (err instanceof APIError) { ... }
  else throw err;
}
```

### Bedrock과 Vertex (TS)

```ts
import { AnthropicBedrock } from "@anthropic-ai/bedrock-sdk";
import { AnthropicVertex } from "@anthropic-ai/vertex-sdk";

const bedrock = new AnthropicBedrock({ awsRegion: "us-east-1" });
const vertex = new AnthropicVertex({ region: "us-east5", projectId: "..." });
```

(패키지 이름은 달라질 수 있으니 최신 문서를 확인하십시오.)

---

## CLI 도구

Python SDK는 기본적으로 한 줄짜리 `anthropic` CLI를 제공하지 않지만, `claude-agent-sdk`와 Claude Code가 CLI 환경을 제공합니다. 즉석 API 테스트에는 `curl`을 사용합니다:

```
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model": "claude-sonnet-4-6", "max_tokens": 256, "messages": [{"role": "user", "content": "Hi"}]}'
```

개발자 워크플로(workflow, 일의 진행 흐름)에는 Claude Code가 공식 CLI 에이전트입니다.

---

## 관용적 패턴

### 클라이언트 재사용

프로세스(process, 실행 중인 프로그램 하나)당 클라이언트를 하나 만들어 재사용합니다. 커넥션 풀링(connection pooling, 서버와의 연결을 재사용해 효율을 높이는 기법), 재시도, 헤더(header, 요청에 붙는 부가 정보)는 여러 호출에 걸쳐 안정적으로 유지됩니다.

### 타입 안전성

두 SDK 모두 완전한 타입 정의(typing, 데이터의 형태를 미리 정해 두어 실수를 줄이는 정보)를 제공합니다. Python에서는 응답 객체가 dataclass와 유사하며, 필드는 속성(attribute)으로 접근합니다. TypeScript에서는 import한 모듈로부터 타입이 자동으로 이어집니다.

### 페이지네이션

일부 엔드포인트(endpoint, API의 개별 호출 주소)(Files 목록, Batches 목록)는 페이지네이션(pagination, 결과를 여러 페이지로 나눠 반환하는 방식)된 결과를 반환합니다. SDK는 이터레이터(iterator, 항목을 하나씩 차례로 꺼내 주는 장치)를 제공합니다:

```python
for f in client.files.list():
    print(f.id)
```

### Webhook 검증

Anthropic 웹훅(webhook, 특정 사건이 발생하면 서버가 자동으로 알려 주는 통지)을 수신한다면(예: 배치 완료 알림), 문서에 따라 서명(signature, 진짜 발신자가 보냈는지 확인하는 값)을 검증하십시오. SDK가 헬퍼를 제공할 수도 있습니다.

### 테스트 더블

테스트에서는 경계 지점에서 클라이언트를 모킹(mocking, 실제 대신 가짜 객체로 대체하는 것)합니다. SDK 내부까지 모킹하는 것은 피하십시오. 스트리밍 동작에는 리플레이 픽스처(replay fixture, 미리 녹화해 둔 응답을 재생하는 테스트용 데이터)를 사용합니다.

---

## SDK 간 선택

| 고려 사항 | Python 선택 | TypeScript 선택 |
|---|---|---|
| 백엔드 서비스 | 흔히 Python | 흔히 Node/TS |
| 프런트엔드 통합 | 드묾 | 예 (서버 측 또는 BFF(Backend For Frontend, 화면 전용 중계 서버)) |
| 데이터 과학 워크플로 | Python | 드묾 |
| 엣지 런타임(edge runtime, 사용자 가까운 곳에서 코드를 실행하는 환경) | 제한적 | 예 (Cloudflare Workers, Vercel) |
| 비동기 편의성 | asyncio | 네이티브 Promise / await |

두 SDK 모두 동일한 Messages 기능 범위를 다룹니다. 생태계(ecosystem, 주변 도구·라이브러리 환경)에 따라 고르십시오.

---

## SDK 버전 관리

SDK는 Anthropic이 기능을 출시할 때마다 기능을 추가합니다. 적당히 최신 상태를 유지하십시오. 오래된 SDK 버전은 새 기능(memory tool, citations, code execution)을 제공하지 않을 수 있습니다. 매니페스트(manifest, 사용하는 패키지와 버전을 적어 두는 파일)에 검증된 마이너 버전을 고정(pin)하고, 업그레이드는 신중하게 계획적으로 하십시오.

---

## 흔한 실수

- 요청마다 새 클라이언트를 생성하는 것(커넥션 풀링이 무력화됨)
- 모든 예외(exception, 프로그램 실행 중 발생한 오류)를 광범위하게 잡는 것
- SDK 내부를 너무 깊이 모킹하는 것
- 소스 코드에 모델 ID를 하드코딩(hardcoding, 값을 코드에 직접 박아 넣는 것)하는 것
- Bedrock 모델 ID와 공식(first-party) 모델 ID를 섞어 쓰는 것
- 스트림을 끝까지 소비하지 않고 방치하는 것

---

## 시험 포인트

- 공식(first-party) / Bedrock / Vertex 각각에 어떤 클라이언트 클래스를 사용하는지
- 스트리밍 헬퍼와 최종 메시지를 조립하는 방법
- 비동기 vs 동기 클라이언트 선택
- 오류 클래스 계층 구조
- 요청별 옵션 재정의
- SDK를 사용한 관용적인 에이전트 루프(agent loop, 모델 호출과 도구 실행을 반복하는 구조) 구성
