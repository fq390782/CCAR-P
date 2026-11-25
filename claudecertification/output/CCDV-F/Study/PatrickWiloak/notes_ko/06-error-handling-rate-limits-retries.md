# 06 - 에러 처리, 레이트 리밋, 재시도

프로덕션(production, 실제 서비스 운영 환경) Claude 앱의 성패는 에러와 레이트 리밋(rate limit, 일정 시간 동안 보낼 수 있는 요청·토큰 양의 상한)을 어떻게 처리하느냐에 달려 있습니다. 시험에서는 에러를 올바르게 분류할 수 있는지, 그리고 상황을 악화시키지 않는 재시도(retry) 로직을 설계할 수 있는지를 평가합니다.

---

## 에러 코드

| HTTP | 유형 | 원인 | 재시도 가능? |
|---|---|---|---|
| 400 | invalid_request_error | 잘못된 형식의 본문, 스키마(schema, 데이터 구조 규칙) 위반 | 아니요 - 요청을 수정 |
| 401 | authentication_error | 잘못되었거나 누락된 API 키(API key, API 이용 권한을 증명하는 비밀 문자열) | 아니요 - 인증을 수정 |
| 403 | permission_error | 계정 권한 거부 | 아니요 |
| 404 | not_found_error | 잘못된 엔드포인트(endpoint, 요청을 보내는 API 주소) 또는 ID | 아니요 |
| 413 | request_too_large | 본문이 너무 큼 | 아니요 - 크기 축소 |
| 429 | rate_limit_error | RPM(분당 요청 수) 또는 TPM(분당 토큰 수) 상한 도달 | 예 - 백오프(backoff, 실패 후 다시 시도하기까지 기다리는 것) |
| 500 | api_error | 서버 에러 | 예 - 백오프 |
| 529 | overloaded_error | API 과부하 | 예 - 백오프 |

그 밖의 에러 유형으로는 `billing_error`(보통 4xx)와 `timeout_error`가 있습니다.

---

## 에러 응답 형태

```json
{
  "type": "error",
  "error": {
    "type": "rate_limit_error",
    "message": "Rate limit exceeded"
  }
}
```

재시도 로직은 메시지 문자열이 아니라 `error.type`과 HTTP 상태 코드를 기준으로 판단합니다.

---

## 레이트 리밋 헤더

모든 성공 응답과 429 응답에 포함되는 헤더(header, 응답에 붙는 부가 정보):

- `anthropic-ratelimit-requests-limit`
- `anthropic-ratelimit-requests-remaining`
- `anthropic-ratelimit-requests-reset` (RFC 3339 타임스탬프)
- `anthropic-ratelimit-tokens-limit`
- `anthropic-ratelimit-tokens-remaining`
- `anthropic-ratelimit-tokens-reset`
- `anthropic-ratelimit-input-tokens-*`
- `anthropic-ratelimit-output-tokens-*`

429 응답에는 `retry-after`가 있을 수 있습니다(티어 지출 한도(spend cap)로 인한 429에는 없습니다).

이 헤더들을 사용해 선제적 스로틀링(throttling, 요청 속도를 의도적으로 늦추는 것)을 구현합니다. 남은 양(remaining)이 임계값보다 낮으면 차단되기 전에 속도를 줄입니다.

---

## 재시도 패턴

### 지터(jitter, 재시도 대기 시간에 더하는 무작위 값)를 적용한 지수 백오프(exponential backoff, 재시도할 때마다 대기 시간을 2배씩 늘리는 방식)

```python
def with_retry(func, max_attempts=5, base=1.0):
    for attempt in range(max_attempts):
        try:
            return func()
        except RetryableError as e:
            if attempt == max_attempts - 1:
                raise
            delay = e.retry_after or (base * (2 ** attempt))
            delay += random.uniform(0, delay * 0.25)  # 지터
            time.sleep(delay)
```

### 분류

```python
def is_retryable(status, error_type):
    if status in (429, 500, 529):
        return True
    if status >= 500:
        return True
    return False
```

400번대 에러(429 제외)는 재시도하지 않습니다. 재시도하면 호출이 낭비되고 계정 수준의 남용(abuse) 신호를 유발할 수 있습니다.

### Retry-After 준수

서버가 `retry-after`를 제공하면 그 값을 따릅니다. 직접 계산한 백오프 값은 헤더가 없을 때의 대안입니다.

### 재시도 횟수 제한

시도 횟수를 제한합니다(일반적으로 3~5회). 무제한 재시도는 장애를 감추고 지연 시간(latency, 응답까지 걸리는 시간)을 늘립니다.

### 멱등성

Claude API는 Messages에 대해 기본 제공 멱등성 키(idempotency key, 같은 요청이 여러 번 실행돼도 결과가 한 번만 반영되도록 하는 식별자)를 제공하지 않습니다. 멱등성은 클라이언트 측에서 관리합니다. 요청을 해시(hash, 데이터를 고정 길이 값으로 변환한 것)하고, 응답을 저장해 두었다가, 재시도 시 저장된 응답을 반환합니다.

도구 실행의 경우, 에이전트 루프(agent loop, 모델이 도구를 호출하고 결과를 받아 다음 행동을 정하는 반복 과정) 내 재시도가 안전하도록 도구를 멱등적으로 설계합니다.

---

## 서킷 브레이커

N번 연속 실패하면 회로를 엽니다(서킷 브레이커(circuit breaker, 장애가 계속되면 요청을 일시 차단하는 안전장치) 작동):

- 쿨다운(cooldown, 대기 기간) 동안 새 요청 전송을 중단합니다
- 상위 호출자에게 명확한 실패를 알립니다
- 주기적으로 단일 요청을 보내 복구 여부를 확인합니다

Claude나 네트워크 상태가 저하되었을 때 연쇄 장애를 방지합니다.

---

## 타임아웃

요청 타임아웃(timeout, 응답을 기다리는 최대 시간)을 설정합니다. SDK(Software Development Kit, API를 쉽게 쓰도록 제공되는 개발 도구 모음)의 기본 타임아웃은 길기 때문에 워크로드(workload, 시스템이 처리하는 작업)별로 설정합니다:

```python
client = Anthropic(timeout=30.0)  # 또는 요청별: client.with_options(timeout=...)
```

일반적인 타임아웃:

- 대화형 UX: 30~60초
- 배치 / 비동기: 더 길게
- 도구 호출: SDK가 아니라 도구 자체에서 제한

---

## 스트리밍 에러

스트림(stream, 응답을 조금씩 순차적으로 받는 방식)은 도중에 실패할 수 있습니다. SDK는 반복 처리 중에 에러를 예외(exception, 프로그램 실행 중 발생한 오류 신호)로 노출합니다. 다음과 같이 처리합니다:

```python
try:
    with client.messages.stream(...) as stream:
        for text in stream.text_stream:
            ...
except APIError as e:
    log.error("stream failed", error=e)
```

처음부터 다시 시도할지, 이어서 재개할지 결정합니다(대부분의 워크로드는 처음부터 다시 시작합니다).

---

## SDK 예외 계층 구조

Python SDK는 타입이 지정된 예외를 제공합니다:

- `APIError` - 기본 클래스
- `APIConnectionError` - 네트워크 문제
- `APITimeoutError` - 타임아웃
- `APIStatusError` - 2xx가 아닌 응답(하위 클래스로 세분화)
- `BadRequestError`, `AuthenticationError`, `PermissionDeniedError`, `NotFoundError`, `RateLimitError`, `InternalServerError`, `APIResponseValidationError`

관심 있는 특정 클래스만 잡고(catch), 나머지는 상위로 전파되도록 둡니다.

TypeScript SDK에도 대응하는 에러 클래스(`APIError`, `RateLimitError` 등)가 있습니다.

---

## 관측 가능성

요청별로 기록할 항목:

- 요청 ID(응답 헤더로 반환됨)
- 모델
- 입력 토큰(token, 모델이 글자를 처리하는 단위), 출력 토큰, 캐시 읽기/쓰기
- 지연 시간
- 중지 사유(stop reason)
- 도구 호출
- 최종 상태(성공 / 재시도 / 실패)

대시보드로 집계합니다. 다음 경우 알림을 설정합니다:

- 429 비율이 임계값을 초과
- 5xx 비율이 임계값을 초과
- 테일 지연 시간(tail latency, 가장 느린 일부 요청의 응답 시간) 증가
- 요청당 비용 증가

---

## 선제적 스로틀링

`anthropic-ratelimit-tokens-remaining`을 모니터링합니다. 이 값이 안전 마진 아래로 떨어지면 우선순위가 낮은 트래픽을 대기열에 넣거나 버립니다. 429가 쏟아지는 것을 방지합니다.

---

## 실전 예제

```python
import anthropic, time, random

client = anthropic.Anthropic()

def call_with_retry(messages, max_attempts=5):
    for attempt in range(max_attempts):
        try:
            return client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1024,
                messages=messages,
            )
        except anthropic.RateLimitError as e:
            retry_after = e.response.headers.get("retry-after")
            delay = float(retry_after) if retry_after else (2 ** attempt)
            delay += random.uniform(0, delay * 0.25)
            time.sleep(delay)
        except anthropic.InternalServerError:
            time.sleep((2 ** attempt) + random.uniform(0, 1))
        except anthropic.BadRequestError:
            raise  # 재시도하지 않음
    raise RuntimeError("max attempts exceeded")
```

---

## 흔한 실수

- 400 에러를 재시도함
- `retry-after`를 무시함
- 무제한 재시도
- 지터 없음(동시에 재시도가 몰려 thundering herd(대량의 클라이언트가 한꺼번에 몰리는 현상)를 유발)
- `Exception`을 광범위하게 잡아 모두 재시도 가능으로 취급함
- 요청 ID를 기록하지 않고 에러를 숨김
- 서킷 브레이커가 없어 부분 장애 시 예산을 소진함

---

## 시험 출제 포인트

- 어떤 에러 코드가 재시도 가능한가
- `retry-after`의 역할
- 지터를 적용한 지수 백오프
- 레이트 리밋 헤더
- 서킷 브레이커 기본 개념
- 멱등성 전략

---

## 핵심 용어

- **429 rate_limit_error** - 분당 요청 수 또는 분당 토큰 수 상한에 도달한 경우입니다. 백오프와 함께 재시도할 수 있습니다.
- **retry-after header** - 공식 SDK는 재시도 대상 에러에 이 헤더가 있으면 이를 따릅니다. 티어 지출 한도로 인한 429에는 retry-after가 없으며, 이용이 재개될 때까지 계속 실패합니다.
- **Circuit breaker** - N번 연속 실패하면 쿨다운 동안 요청 전송을 중단하고, 가끔 단일 요청으로 복구 여부를 확인합니다.
- **Exponential backoff with jitter** - 재시도 가능한 에러에 대한 재시도 패턴으로, 시도 횟수에 상한을 둡니다.
