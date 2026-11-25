# 04 - 프롬프트 캐싱과 Batch API

Anthropic에서 비용을 줄이는 가장 큰 수단 두 가지입니다. 둘 다 작동 원리를 깊이 이해하는 개발자에게 큰 이점을 줍니다.

---

## 프롬프트 캐싱

프롬프트 캐싱(prompt caching, 반복되는 입력을 서버에 저장해 두고 재사용하는 기능)을 사용하면 Anthropic이 요청의 프리픽스(prefix, 요청의 앞부분)를 서버 측에 저장해 두었다가, 같은 프리픽스를 가진 이후 요청에서 저렴하게 재사용할 수 있습니다.

### 작동 원리

콘텐츠 블록(content block, 메시지를 구성하는 단위 조각)에 `cache_control: {"type": "ephemeral"}`을 표시하면, 그 블록(및 프롬프트에서 그 앞에 있는 모든 내용)이 캐시 브레이크포인트(cache breakpoint, 캐시할 범위의 끝을 나타내는 표시)로 선언됩니다.

```python
system=[
    {
        "type": "text",
        "text": large_static_instructions,
        "cache_control": {"type": "ephemeral"},
    }
]
```

첫 번째 호출: 캐시 쓰기(cache write)입니다. Anthropic이 프리픽스를 저장하고 캐시 쓰기 토큰(token, 모델이 글자를 처리하는 단위)으로 과금합니다.

이후 바이트 단위로 완전히 동일한 프리픽스를 가진 호출: 캐시 읽기(cache read)입니다. 토큰이 캐시에서 제공되며 캐시 읽기 요금이 적용됩니다.

### 요금

기본 입력 요금 대비 대략적인 배율은 다음과 같습니다.

- 캐시 쓰기: 약 1.25배
- 캐시 읽기: 약 0.1배

정확한 수치는 모델마다 다르므로 현재 요금을 확인하십시오.

### TTL

- 기본 ephemeral: 5분
- 연장: 1시간 (지원되는 경우 `cache_control: {"type": "ephemeral", "ttl": "1h"}`)

읽기에 성공하면 TTL(Time To Live, 캐시가 유지되는 유효 시간)이 갱신됩니다.

### 최소 캐시 가능 크기

- 대부분의 모델: 1024 토큰
- Haiku: 2048 토큰

이 기준보다 작으면 캐싱은 효과가 없습니다.

### 브레이크포인트

요청당 최대 4개의 캐시 브레이크포인트를 둘 수 있습니다. 각 브레이크포인트는 캐시 가능한 영역의 끝을 표시하며, 프롬프트의 시작부터 해당 지점까지의 모든 내용이 캐시 키(cache key, 캐시를 찾을 때 쓰는 식별 기준)가 됩니다.

계층 구조 예시입니다.

```python
system=[
    {"type": "text", "text": stable_system_prompt, "cache_control": {"type": "ephemeral"}},
    {"type": "text", "text": product_specific_docs, "cache_control": {"type": "ephemeral"}},
]
```

브레이크포인트가 두 개입니다. 첫 번째 브레이크포인트는 `product_specific_docs`가 달라지더라도 시스템 프롬프트의 캐시가 무효화되지 않도록 보호합니다.

### 캐시 적합성

캐시 효과가 높은 것부터 낮은 것 순서입니다.

1. 시스템 프롬프트(system prompt, 모델의 역할이나 규칙을 미리 지정하는 지시문)
2. 도구 정의 (tools 배열을 통해 캐시)
3. 메시지 안의 변하지 않는 참고 문서
4. 퓨샷 예시(few-shot example, 원하는 답변 형태를 보여주는 몇 개의 예시)
5. 긴 세션에서의 대화 프리픽스

자주 바뀌는 콘텐츠(현재 사용자 메시지, 동적 검색 결과)는 캐시하지 않아야 합니다.

### 사용량 확인

응답의 `usage`는 다음을 보고합니다.

- `input_tokens` - 캐시되지 않은 입력 토큰
- `cache_creation_input_tokens` - 이번 요청에서 캐시에 쓴 토큰
- `cache_read_input_tokens` - 이번 요청에서 캐시로부터 제공된 토큰
- `output_tokens` - 응답 토큰 (thinking 포함)

이 값들을 합산해야 실제 과금 대상 입력 총량이 됩니다.

### 손익분기 계산

쓰기가 1.25배, 읽기가 0.1배라면 다음과 같습니다.

- 캐싱 없음: N회 읽기 비용은 N × 기본 요금
- 캐싱 사용: 1회 쓰기 + N회 읽기 비용은 1.25 + 0.1N

손익분기점은 약 1.4회 읽기입니다. 실무적으로는 TTL 내에 2회 이상 재사용할 내용이라면 무엇이든 캐시하십시오.

### 흔한 실수

- 자주 바뀌는 콘텐츠를 캐시하는 것 (매 요청마다 캐시 미스(cache miss, 캐시에서 찾지 못함)가 발생하고 쓰기 비용이 낭비됨)
- 크기 기준 미만의 콘텐츠를 캐시하는 것 (효과 없음)
- 캐시된 블록이 조금이라도 바뀌면 그 뒤의 모든 내용이 무효화된다는 점을 잊는 것
- 캐시 적중률(cache hit rate, 캐시에서 찾아 재사용한 비율)을 측정하지 않는 것
- 캐시가 모델 버전을 넘어 유지된다고 가정하는 것 (유지되지 않음)

---

## Batch API

Batch API는 작업을 비동기(asynchronous, 요청 후 결과를 기다리지 않고 나중에 받는 방식)로 절반 가격에 실행합니다.

### 사양

- 실시간 대비 50% 할인
- 24시간 이내 SLA(Service Level Agreement, 서비스 제공자가 보장하는 처리 수준) (보통은 훨씬 빠름)
- 배치당 최대 100,000건의 요청
- 배치당 최대 256 MB
- 각 요청은 완전한 Messages API 요청입니다

### 워크플로

1. 배치를 생성합니다.

```python
batch = client.messages.batches.create(
    requests=[
        {
            "custom_id": "request-1",
            "params": {
                "model": "claude-sonnet-4-6",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": "Summarize: ..."}],
            },
        },
        ...
    ]
)
```

2. 상태를 폴링(polling, 일정 간격으로 상태를 반복 확인하는 방식)합니다.

```python
batch = client.messages.batches.retrieve(batch.id)
print(batch.processing_status)  # in_progress | canceling | ended
```

3. 종료되면 결과를 가져옵니다.

```python
for result in client.messages.batches.results(batch.id):
    if result.result.type == "succeeded":
        print(result.custom_id, result.result.message.content)
    elif result.result.type == "errored":
        print(result.custom_id, result.result.error)
```

### 항목별 상태

각 배치 항목은 다음 중 하나의 상태로 끝납니다.

- `succeeded` - 응답을 사용할 수 있음
- `errored` - 항목별 오류 (유효성 검사, 속도 제한 등)
- `expired` - 배치가 만료 시간에 도달함
- `canceled` - 처리 전에 배치가 취소됨

실패는 서로 독립적입니다. 잘못된 항목 하나가 배치 전체를 망치지 않습니다.

### Custom ID

`custom_id`는 여러분의 상관 키(correlation key, 요청과 결과를 서로 연결하기 위한 식별값)입니다. 결과를 여러분의 레코드에 다시 매핑하는 데 사용하십시오.

### 캐싱과 결합하기

배치 요청 안의 캐시된 블록도 배치 항목 간에 프리픽스가 일치하면 캐시 읽기가 적용됩니다. 변하지 않는 시스템 프롬프트를 가진 10만 건 레코드 배치라면, 캐시를 한 번 쓰고 10만 번 읽으므로 막대한 비용을 절감할 수 있습니다.

### 웹훅 vs 폴링

일부 계정에서는 배치 완료 시 웹훅(webhook, 이벤트 발생 시 지정한 주소로 자동 통지하는 방식) 전달을 사용할 수 있습니다. 폴링은 어디서나 동작합니다. 여러분의 인프라에 맞춰 선택하십시오.

### 이상적인 사용 사례

- 프롬프트 변경 후 기존 데이터를 다시 보강하는 백필(backfill, 과거 데이터를 소급해 처리하는 작업)
- 야간 분류 또는 태깅 작업
- 과거 데이터에 대한 평가(eval) 실행
- 대량 마스킹(redaction, 민감 정보 가리기) 또는 변환

### 적합하지 않은 경우

- 사용자와 직접 상호작용하는 흐름
- 1시간 미만의 SLA가 필요한 워크로드(workload, 처리해야 할 작업량)
- 일부만 완료되는 것을 허용할 수 없는 워크로드

---

## 비용 점검 패턴

모든 Claude 워크로드에 대해 다음을 수행합니다.

1. 1000건의 요청에 걸쳐 캐시 적중률을 측정합니다
2. 요청당 평균 캐시 읽기 토큰, 쓰기 토큰, 일반 입력 토큰, 출력 토큰을 계산합니다
3. 현재 요금을 곱해 평균 요청 비용을 구합니다
4. 캐싱이 완벽했을 경우, 그리고 Batch API를 사용했을 경우의 이론적 비용과 비교합니다

5줄 정도의 설정 변경만으로 50% 이상 개선되는 경우가 많습니다.

---

## 시험 핵심 포인트

- `cache_control`을 넣는 위치 (콘텐츠 블록에)
- TTL (기본 5분, 연장 1시간)
- 최소 캐시 가능 크기 (1024, Haiku는 2048)
- 손익분기 읽기 횟수
- Batch API 할인율 (50%)과 SLA (24시간)
- `custom_id`를 통한 배치 결과 연결
- 배치 결과의 항목별 상태

---

## 핵심 용어

- **프롬프트 캐싱(Prompt caching)** - 요청의 프리픽스를 서버 측에 저장해 두었다가, 같은 프리픽스를 가진 이후 요청에서 저렴하게 재사용합니다.
- **cache_control** - 콘텐츠 블록에 붙이는 표시로, 해당 블록과 그 앞의 모든 내용을 캐시 브레이크포인트로 만듭니다.
- **Batch API** - 작업을 50% 할인된 가격으로 비동기 실행하며, 결과는 24시간 이내에 제공됩니다.
- **custom_id** - 각 배치 요청에 붙이는 여러분의 상관 키로, 결과를 여러분의 레코드에 다시 매핑하는 데 사용합니다.
