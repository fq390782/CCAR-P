# 4. Eval, Testing, and Debugging — 반드시 알아야 할 지식
> 시험 비중 3% · 약 1문항 · 근거 문항 16개

## 1. 핵심 개념

### 1-1. Eval set: 변경은 측정한 뒤 ship
- 손으로 고른 3~5개 example이 좋아 보여도 실제 개선인지 noise인지 구분할 수 없다. 실제 분포를 대표하는 held-out eval set을 미리 정한 기준(defined criteria, success criteria)으로 돌려 비교한 뒤 ship한다. [Amey-0035] [Amey-0065]
- 모델에게 "어느 prompt가 나은가"를 묻는 self-assessment는 측정이 아니다. flag나 일부 traffic에 먼저 내보내고 지켜보는 방식은 사용자를 test set으로 쓰는 셈이다. [Amey-0035] [Amey-0065]
- 소수 example을 손으로 확인하는 것은 경향을 파악하는 첫걸음일 뿐이다. 드문 입력에서 생기는 깨짐이나 출력 형식 변화를 놓치기 쉽고, 결과를 재현할 수 없다. [Udemy-0027] [Patrick-0030]

![기준 측정, prompt 변경, 재측정, ship으로 이어지는 eval 사이클](svg/4-eval-cycle.svg)
*그림: 같은 held-out eval set과 기준으로 재측정해 개선이 확인될 때만 ship하며, 손 example·self-assessment·일부 traffic 배포는 측정을 대신하지 못한다.*

### 1-2. Grader 선택: free-form prose에는 LLM-as-judge
- free-form prose는 같은 정답도 표현이 달라 exact string match로 채점할 수 없다. 주관적 품질(예: faithfulness to source)에는 LLM-as-judge를 쓴다. [Patrick-0014] [Patrick-0030]
- 단, judge에게 맨 점수만 요청하지 말고 rubric을 줘야 한다(예: 출처에 충실한가, 지어낸 주장이 없는가). judge 자체도 human label 표본과 대조해 validation한다. [Patrick-0014] [Patrick-0030]
- 출력이 valid JSON인지만 보는 검사는 형식 검사일 뿐 품질 eval이 아니다. [Patrick-0014]

![free-form prose 품질 평가에 쓰는 grader 선택 트리](svg/4-grader-choice.svg)
*그림: 주관적 prose 품질은 rubric을 준 LLM-as-judge로 채점하고 judge는 human label로 검증하며, 형식 검사와 exact match는 품질 eval이 아니다.*

### 1-3. Regression suite
- regression은 정의상 조용히 일어난다. 목표 동작은 좋아졌는데 다른 동작이 몰래 깨지는 변화가 그 예다. 깨지면 안 되는 것을 계속 테스트해서 잡는다. 이 점이 일회성 eval과 다르다. [Amey-0080]
- latency, rate limit, cost는 운영 신호이지 correctness 신호가 아니다. [Amey-0080]
- eval set은 versioning해서 regression suite로 겸용한다. 모든 prompt 변경과 model upgrade 때마다 돌리고, production에서 실패한 사례는 새 case로 추가한다. [Patrick-0030] [Patrick-0014]

![prompt 변경과 model upgrade 때마다 도는 regression suite 흐름](svg/4-regression-suite.svg)
*그림: versioned eval set을 변경 때마다 돌려 조용한 회귀를 ship 전에 잡고, production 실패 사례를 새 case로 되먹인다.*

### 1-4. Model 업그레이드와 운영
- production에서는 model ID를 고정(pin)한다. 새 모델은 regression eval로 성능 저하가 없는지 확인한 뒤 원하는 시점에 옮긴다. [Udemy-0027]
- 해설에 따르면 Claude Opus 5.5는 temperature 같은 sampling 설정 변경과 thinking 비활성화를 받지 않는다. 이처럼 모델이 바뀌면 이전에 쓰던 parameter가 error가 될 수 있다. [Udemy-0027]
  - ⚠️ 공식 문서로 확인되지 않음.
- API 호환성이 유지돼도 같은 prompt에 대한 길이, 형식, 판단 경향이 달라질 수 있다. 이전 모델에 맞춘 지시와 설정을 그대로 가져가지 말고 다시 eval한다. "새 모델이니 더 낫다"는 가정이나 vendor benchmark는 근거가 되지 않는다. [Udemy-0027] [Patrick-0030]
- 모델 목록에는 각 모델의 retirement(폐기) 예정일이 있다. 따라서 migration은 일정에 넣어 계획적으로 진행한다. [Udemy-0027] [Udemy-0037]
- release 이후 운영·보존 단계: uptime만 감시해서는 부족하다. 응답 품질과 이용 현황을 monitoring하고, 모델 교체나 외부 근거(제도·문서) 변경의 영향을 eval set으로 확인한 뒤 계획적으로 수정한다. [Udemy-0037]
- Claude API 모델은 운영 중 대화나 사용자 피드백 버튼으로 스스로 재학습하지 않는다. 피드백은 운영 측이 prompt, 참조 데이터, eval set을 고치는 데 쓴다. [Udemy-0037]

![model ID pin부터 계획적 migration까지의 모델 업그레이드 절차](svg/4-model-upgrade.svg)
*그림: 새 모델은 pin을 유지한 채 regression eval을 통과한 뒤에만 계획한 시점에 migration한다.*

![release 이후 monitoring과 eval을 거쳐 계획적으로 수정하는 운영 루프](svg/4-ops-feedback.svg)
*그림: 운영 중 피드백과 외부 변경은 모델이 스스로 배우지 않으므로 운영 측이 eval로 영향을 확인해 prompt·참조 데이터·eval set을 고친다.*

### 1-5. Prompt를 SDLC에 통합
- prompt는 출력을 좌우하는 산출물이므로 code처럼 repository에서 version control한다. pull request에서 review와 eval 결과를 확인한 뒤 merge한다. 그래야 diff 확인, revert, eval 결과 대응이 가능하다. [Udemy-0018]
- 관리 화면에서 production prompt를 바로 수정하거나 DB에 저장해 두면 이력과 review가 남지 않는다. production A/B test는 사전 eval을 통과한 후보 중에서 고르는 마지막 단계일 뿐이다. [Udemy-0018]

![repository, PR, review와 eval, merge로 이어지는 prompt 관리 파이프라인](svg/4-prompt-sdlc.svg)
*그림: prompt는 PR에서 review와 eval을 통과해야 merge되며, A/B test는 통과 후보 중 고르는 마지막 선택 단계다.*

### 1-6. 안전한 refactoring
- 먼저 현재 동작을 고정하는 테스트(characterization test)를 만든다. 그다음 작고 검증 가능한 단위로 바꾸고, 매번 test와 review를 통과시킨다. 문제가 생기면 바로 전 단계로 되돌린다. [Udemy-0003]
- refactoring은 외부 동작을 유지한다. 기능 추가나 bug fix처럼 동작을 바꾸는 작업을 같은 변경에 섞으면 원인을 가를 수 없다. big-bang rewrite와 수동 화면 확인만으로는 안전성이 보장되지 않는다. [Udemy-0003]

![characterization test 후 작은 단계로 바꾸고 실패 시 되돌리는 refactoring 절차](svg/4-safe-refactoring.svg)
*그림: 동작을 test로 고정한 뒤 작은 단계마다 검증하고, 실패하면 직전 단계로 되돌려야 원인을 가를 수 있다.*

### 1-7. Debugging: 결함 위치부터 찾기(localize)
- trace를 보니 모델이 받은 입력에 대해서는 올바르게 추론하는데 입력 문서가 틀렸다면, 결함은 retrieval/integration layer(search, indexing)에 있다. 모델 upgrade나 prompt 문구 강화로는 잘못된 입력을 고칠 수 없다. [Amey-0010] [Amey-0050]
- API 경계에서 실패를 분류한다. 4xx(예: 400 `invalid_request_error`)는 API가 요청을 받지 않은 것이므로 자사의 request 조립 코드를 본다. 200 이후 parse/validation에서 실패했다면 `stop_reason`과 원본 응답 본문을 보고 모델 출력 문제인지 자사 parser 문제인지 가른다. [Udemy-0023]
- `stop_reason`이 `max_tokens`면 응답이 중간에 잘린 것이다. 이는 200 이후 parse 실패의 한 원인이 될 수 있지만 400과는 관계가 없다. [Udemy-0023]
- 모든 응답에는 `request-id` header가 붙는다. 이를 기록해 두면 trace와 API 측 기록을 맞춰 볼 수 있다. [Udemy-0023]
- 일반 원칙: 해결책을 시도하기 전에 실패가 어디서 일어나는지 특정하는 절차를 먼저 고른다. [Udemy-0023]

![검색 단계의 결함이 모델 추론까지 흘러가는 pipeline](svg/4-trace-retrieval.svg)
*그림: trace에서 추론은 맞고 입력 문서가 틀렸다면 retrieval layer를 고쳐야 하며, 모델이나 prompt를 바꿔서는 해결되지 않는다.*

![API status로 실패를 분류해 결함 위치를 찾는 절차](svg/4-localize-defect.svg)
*그림: 4xx는 자사 request 조립 코드, 200 이후 parse 실패는 stop_reason과 원본 본문으로 잘림·모델 출력·자사 parser를 가른다.*

### 1-8. API error와 retry policy
- 429 `rate_limit_error`, 500 `api_error`, 529 `overloaded_error`는 일시적인 error다. exponential backoff와 jitter를 쓰고 server가 준 `retry-after`를 지켜서 retry한다. [Patrick-0032] [Patrick-0006]
- 400, 401, 403, 404 같은 client error는 요청 자체가 잘못된 것이라 retry해도 매번 같은 이유로 실패한다. 요청을 고친다. 잘못된 retry policy는 느린 응답과 비용 증가로 나타난다. [Patrick-0006] [Patrick-0032]
  - ⚠️ 해설은 "429를 뺀 4xx는 모두 retry 불가"로 일반화하지만, 공식 SDK는 408, 409도 기본으로 retry한다. 시험에서는 400, 401, 403, 404를 retry 불가로 기억하면 된다.
- 즉시 retry하는 tight loop는 과부하를 더 키운다. 첫 일시적 error에서 job 전체를 실패시키면 쓸데없이 fragile해진다. 여러 API key를 돌려 rate limit을 피하는 방식은 오답이다. [Patrick-0027] [Patrick-0032]
- 공식 SDK는 429를 자동으로 retry하고, status code마다 typed exception(예: `RateLimitError`)을 제공한다. 이것으로 retry할 수 있는 실패(429, 5xx, connection error)와 없는 실패(400, 404)를 구분한다. [Patrick-0027]
- tool 이름은 `^[a-zA-Z0-9_-]{1,128}$` pattern만 허용한다. 공백이 들어간 이름(예: `get order status`)은 400을 낸다. 해결책은 이름 변경(`get_order_status`)이다. [Preporato-0030]
  - ⚠️ 공식 tool use 가이드에는 길이 상한이 `{1,64}`로 적혀 있는 곳이 있다. 허용 문자(영문, 숫자, `_`, `-`)는 같고, 길이 상한은 문서에서 다시 확인해야 한다.

![error 종류에 따라 retry 여부를 가르는 retry policy 분기](svg/4-retry-policy.svg)
*그림: 429·500·529와 connection error만 backoff·jitter·retry-after로 retry하고, 400·401·403·404는 요청을 고친다.*

## 2. 상황별 정답 판단 규칙

| 이런 상황이면 | 정답 방향 | 근거 |
|---|---|---|
| prompt 변경이 몇 개 example에서 좋아 보임 | 대표성 있는 held-out eval set + defined criteria로 비교 후 ship | [Amey-0035] [Amey-0065] |
| free-form prose의 품질·faithfulness 평가 | rubric 기반 LLM-as-judge, human label로 judge validation | [Patrick-0014] [Patrick-0030] |
| prompt나 model이 바뀔 때마다 생기는 회귀를 잡고 싶음 | versioned regression suite를 변경 때마다 실행, production 실패를 case로 추가 | [Amey-0080] [Patrick-0030] |
| 새 모델 release | model ID pin 유지 → regression eval 통과 후 계획적 migration | [Udemy-0027] |
| 모델 추론은 맞는데 받은 문서가 틀림 | retrieval/integration layer(search, indexing) 수정 | [Amey-0010] [Amey-0050] |
| 400 vs 200 이후 parse 실패가 섞여 있음 | API 경계에서 분류: 4xx는 request 조립 코드, 200 이후는 `stop_reason`·원본 본문으로 모델과 parser 구분 | [Udemy-0023] |
| 429 / 500 / 529 발생 | backoff + jitter + `retry-after`로 retry | [Patrick-0032] [Patrick-0027] |
| 400 / 401 / 403 / 404 발생 | retry 금지, 요청을 수정 | [Patrick-0006] [Preporato-0030] |
| tool 추가 후 모든 요청이 400 | tool name pattern 위반 확인 후 rename | [Preporato-0030] |
| prompt를 자주 고치는 팀 | repository 관리 + PR에서 review·eval 후 merge | [Udemy-0018] |
| 대규모 legacy code refactoring | characterization test → 작은 단계별 변경과 검증 | [Udemy-0003] |
| release 이후 운영 단계 | 품질·이용 현황 monitoring, 모델·외부 변경의 영향을 eval한 뒤 계획적으로 수정 | [Udemy-0037] |

![실패 증상별 판단 규칙 decision tree](svg/4-rules-failure.svg)
*그림: API status와 parse 결과, trace를 차례로 보면 고칠 곳이 retry 정책, request, parser, retrieval 중 어디인지 정해진다.*

![변경과 평가 상황별 판단 규칙 decision tree](svg/4-rules-change.svg)
*그림: 변경을 평가하거나 내보내는 상황은 모두 eval·review로 측정한 뒤 계획적으로 진행하는 방향이 정답이다.*

## 3. 자주 나오는 오답 함정

- "더 큰 모델로 바꾼다" → 잘못된 입력이나 잘못된 request(400)는 모델을 바꿔도 해결되지 않는다. 실패 빈도를 지켜보는 것만으로는 원인 layer를 알 수 없다. [Amey-0010] [Udemy-0023]
- "prompt에 정확성을 강조하는 문구를 추가한다" → 입력이 틀렸다면 효과가 없다. [Amey-0010] [Amey-0050]
- "모델에게 어느 prompt가 나은지 묻는다" → self-assessment는 측정이 아니다. [Amey-0035] [Amey-0065]
- "flag나 일부 traffic으로 먼저 내보내고 지켜본다" 또는 "release 당일 교체하고 문제가 생기면 되돌린다" → 사용자를 test set으로 쓰는 것이다. [Amey-0035] [Udemy-0027]
- "golden answer와 exact string match" → prose에서는 정답도 표현이 달라 실패한다. [Patrick-0014]
- "새 모델은 더 낫다 / vendor benchmark가 증명한다" → 개별 prompt에서의 동작은 보장되지 않는다. [Patrick-0030] [Udemy-0027]
- "모든 error를 retry한다 / 즉시 retry한다" → 400은 영원히 실패하고, 즉시 retry는 과부하를 키운다. [Patrick-0006] [Patrick-0032]
- "retry가 우연히 성공하면 해결된 것으로 본다" → 근본 원인이 숨는다. [Udemy-0023]
- "max_tokens를 올리고 다시 실행한다"로 400을 해결하려 함 → 출력 길이는 request 형식 오류와 관계없다. [Udemy-0023]
- "사용자 피드백으로 모델이 자동 재학습한다" → Claude API 모델은 운영 중 학습하지 않는다. [Udemy-0037]
- "uptime이나 server 재시작 절차만 정비한다" 또는 "변경을 동결한다" → 답변 내용이 지금도 맞는지는 확인하지 못한다. [Udemy-0037]
- "refactoring에 기능 추가를 같이 넣는다" 또는 "big-bang rewrite" → 원인을 가를 수 없고 되돌릴 수 없다. [Udemy-0003]

## 4. 암기 목록

| 이름/숫자 | 의미 |
|---|---|
| 400 `invalid_request_error` | request 형식이나 내용 오류. retry 금지, 요청 수정 [Udemy-0023] [Patrick-0032] |
| 401 `authentication_error` | 인증 오류. retry 금지 [Udemy-0023] [Patrick-0006] |
| 403 / 404 | client error. retry 금지 [Patrick-0006] |
| 429 `rate_limit_error` | rate limit. backoff 후 retry, `retry-after` 준수. SDK가 자동 retry, `RateLimitError` [Patrick-0027] |
| 500 `api_error` | server error. backoff 후 retry [Patrick-0032] |
| 529 `overloaded_error` | 과부하. backoff 후 retry [Patrick-0032] |
| `request-id` header | 모든 응답에 붙음. trace와 API 측 기록을 대조할 때 사용 [Udemy-0023] |
| `stop_reason: max_tokens` | 응답 잘림. 200 이후 parse 실패의 원인 후보 [Udemy-0023] |
| `^[a-zA-Z0-9_-]{1,128}$` | tool name pattern(⚠️ 길이 상한은 64로 적힌 문서도 있음) [Preporato-0030] |

## 5. 시험 직전 체크리스트

- [ ] 몇 개 example로는 판단하지 않는다. held-out eval set과 defined criteria로 비교한다.
- [ ] prose 품질은 rubric을 준 LLM-as-judge로 보고, judge는 human label로 validation한다.
- [ ] regression suite는 prompt나 model이 바뀔 때마다 돌리고, production 실패를 case로 추가한다.
- [ ] model ID는 pin하고, regression eval을 통과한 뒤 migration한다.
- [ ] trace에서 "추론은 맞는데 입력이 틀림"이 보이면 retrieval layer를 고친다.
- [ ] 4xx는 request 조립 문제, 200 이후 실패는 `stop_reason`과 원본 출력 문제로 본다.
- [ ] 429, 500, 529는 backoff 후 retry하고, 400, 401, 403, 404는 요청을 고친다.
- [ ] prompt는 repository와 PR, eval을 거쳐 merge한다.
- [ ] refactoring은 characterization test를 먼저 만들고 작은 단계로 진행한다.
