# 5. Model Selection and Optimization — 반드시 알아야 할 지식
> 시험 비중 17% · 약 5문항 · 근거 문항 28개

## 1. 핵심 개념

### 1-1. 모델 선택 원칙: 요구 수준에 맞추고, 측정해서 정한다
- 모델 선택은 "요구 품질을 충족하는 가장 효율적인 모델"을 고르는 일입니다. 정확도를 무한정 높일 목표로 보지 않고, 요구 수준을 넘는 품질에 드는 비용은 낭비로 봅니다. [Amey-0019] [Amey-0057] [Udemy-0035]
- 판단 근거는 실제 task를 대표하는 sample과 그 task의 quality bar로 측정한 결과(eval)입니다. published benchmark, 더 최신 모델이라는 점, 더 큰 모델이라는 점은 근거가 되지 못합니다. [Amey-0022] [Patrick-0019]
- 작은 모델로 내리는 시점은 "작은 모델이 정해 둔 quality bar를 충족한다는 측정 결과"가 나왔을 때입니다. 예산 초과, 호출량 증가, latency 불만은 검토를 시작할 이유일 뿐, 바꿔도 된다는 근거는 아닙니다. [Amey-0072] [Preporato-0012]
- 두 모델의 품질이 같다면 싼 모델을 배포합니다. 입력이 달라질 경우는 그때 다시 평가해서 대응하며, 큰 모델을 "보험"으로 쓰지 않습니다. [Amey-0057]
- 모델 선택은 한 번 정하고 끝나는 일이 아닙니다. 후속 모델은 같은 가격에 품질이나 속도가 나아지는 경우가 많고, 모델 ID마다 retirement 일정이 있으므로 eval set으로 주기적으로 다시 평가합니다. [Udemy-0035] [Udemy-0002]
- 기본 모델이 무엇인지 확인하지 않고 SDK나 quickstart 예제의 기본 모델을 그대로 쓰지 않습니다. 모델 라인업이 바뀌므로 현재 model ID는 문서에서 확인합니다. [Patrick-0019]

![예산·호출량·latency 트리거에서 eval을 거쳐 모델 하향 여부를 정하고 주기적으로 재평가하는 흐름](svg/5-measure-before-downgrade.svg)
*그림: 예산 초과나 latency 불만은 검토 계기일 뿐이며, 작은 모델이 quality bar를 충족한다는 측정 결과가 있어야 내린다.*

### 1-2. 계층(Opus / Sonnet / Haiku)별 적합한 작업
- **Haiku(fast tier)**: 가장 빠르고 가장 저렴합니다. 대량의 단순 작업이나 latency가 중요한 작업(classification, extraction, routing, 언어 판별, 형식 변환, autocomplete)에 맞습니다. [Udemy-0035] [Amey-0020] [Preporato-0015]
- **Sonnet(balanced tier)**: 속도와 지능의 균형이 가장 좋습니다. escalated drafting처럼 어느 정도 능력이 필요한 작업에 Opus 대신 쓸 수 있는 선택지입니다. [Udemy-0035] [Patrick-0011]
- **Opus(most capable)**: 여러 시스템이 맞물린 multi-step 계획, 상호작용하는 제약을 따지며 계획을 수정해 가는 작업, 오래 걸리는 agent 작업, 품질이 사업 가치를 좌우하는 분석에 씁니다. 능력 차이는 이런 작업에서 드러납니다. [Amey-0020] [Amey-0058] [Udemy-0035]
- 추론이 많이 필요한 작업을 작은 모델 여러 개로 나누면 추론이 끊어집니다. prompt를 길게 쓰거나 다듬어도 모델 자체의 능력 차이는 메워지지 않습니다. [Amey-0058] [Udemy-0035]
- ⚠️ 해설은 Fable 5.2를 Opus보다 위 계층으로 소개합니다. 모델 라인업은 시점마다 다르므로 시험에서는 Opus, Sonnet, Haiku 세 계층이 각각 어떤 작업에 맞는지를 기준으로 판단합니다. [Udemy-0035]

### 1-3. Routing: 요청마다 맞는 모델 보내기
- Model routing은 각 요청을 그 요청을 처리할 수 있는 가장 싼 모델로 보내는 방식입니다. 모델 하나로 모든 요청을 처리하면 쉬운 요청에는 돈을 더 쓰고, 어려운 요청에서는 품질이 모자랍니다. [Patrick-0011] [Patrick-0019]
- 대표 패턴은 두 가지입니다. (1) 대량의 쉬운 작업(분류, 추출)은 Haiku에, 소량의 어려운 작업(escalated reply, deep analysis)은 Sonnet이나 Opus에 맡깁니다. (2) 계획을 세우는 orchestrator에는 capable model을, 범위가 좁고 반복되는 worker subtask에는 작고 빠른 모델을 씁니다. [Patrick-0011] [Patrick-0037]
- 가장 어려운 단계(계획 수립)에 가장 약한 모델을 배치하는 구성은 틀린 구성입니다. [Patrick-0037]

![router가 난이도별로 Haiku와 Sonnet/Opus에 요청을 나누는 구조와 orchestrator–worker 구조](svg/5-routing.svg)
*그림: 쉬운 대량 요청은 작은 모델로, 어려운 요청과 계획 단계는 capable 모델로 보내야 한다.*

### 1-4. 사고량 조절: effort, adaptive thinking, extended thinking
- Thinking은 multi-step 문제에서는 정확도를 높이지만, 다른 작업에서는 output token과 latency만 늘립니다. 그래서 모든 요청에 켜거나 모든 요청에서 끄지 말고, eval 결과를 근거로 workload별로 정합니다. 인사 같은 단순한 응답에서는 줄입니다. [Preporato-0013] [Udemy-0009]
- `output_config.effort`는 모델을 바꾸지 않고 응답 전체(thinking과 tool call 포함)에 쓰는 token 양을 조절합니다. 일상적인 작업은 effort를 낮추고 어려운 작업은 높게 둡니다. 단, eval로 품질이 유지되는지 확인한 뒤에 바꿉니다. [Preporato-0012]
- Adaptive thinking은 요청마다 생각을 할지, 얼마나 깊이 할지를 Claude가 정하고, effort(low부터 max까지)로 그 경향을 조정하는 방식입니다. effort를 높이면 더 적극적이고 깊게 생각합니다. [Udemy-0009]
- Thinking에 쓴 token은 output token으로 과금되고 latency도 늘어납니다. 그래서 형식이 정해진 단순 분류에 effort max를 쓰는 것은 비용 대비 효과가 없습니다. [Udemy-0009]
- 역할 구분: few-shot 예시는 "어떤 형태로 답할지"(형식, 톤, 분류 경계)를 정하고, thinking/effort는 "얼마나 생각할지"를 정합니다. 예시를 많이 넣어도 추론을 대신하지 못합니다. 권장 예시 수는 관련성 있고 다양한 3~5개입니다. [Udemy-0009]
- ⚠️ 해설에 따르면 `budget_tokens`로 사고량을 고정하는 예전 extended thinking 방식은 Claude Opus 4.7 이후 모델에서 받아들여지지 않습니다. 모델 버전에 따라 달라지는 내용이므로 현재 문서를 확인해야 합니다. [Udemy-0009]

![workload 유형에 따라 effort와 few-shot을 고르고 eval로 확인하는 decision tree와 effort 스케일](svg/5-effort-thinking.svg)
*그림: thinking과 effort는 일괄 설정하지 않고 workload별로 정하며, effort를 높일수록 output token과 latency가 늘어난다.*

### 1-5. 비용 진단과 절감 수단
- 호출량은 그대로인데 비용이 올랐다면, 요청 1건당 token 사용량, 특히 매 호출마다 다시 보내는 context 양을 먼저 확인합니다. latency에는 과금되지 않고, API key 개수도 비용과 무관합니다. [Amey-0021]
- 품질에 문제가 없는데 비용이 늘었다면 모델 tier를 내리기 전에 두 가지를 먼저 합니다. (1) 더 이상 필요 없는 tool output과 history를 잘라 context를 줄이고, (2) 변하지 않는 prefix(tools, system prompt)를 caching합니다. tier 변경은 eval 근거가 있을 때만 합니다. [Preporato-0011]
- `max_tokens`를 낮춰도 작업 자체의 단가는 내려가지 않고 답이 중간에 잘릴 뿐입니다. 반대로 `max_tokens`를 높이면 지출이 늘 수 있습니다. [Patrick-0037] [Preporato-0011] [Preporato-0012]
- task에 필요한 것보다 훨씬 큰 context window를 가진 모델을 고르면, task에 필요 없는 cost와 latency를 치르게 됩니다. 큰 window 자체가 정확도, rate limit, 구조화 출력의 신뢰성을 높여 주지는 않습니다. [Amey-0071]
  - ⚠️ 공식 과금은 실제로 사용한 token 기준이며 window 크기 자체에는 과금되지 않습니다. 비용 차이는 window보다 모델 tier의 단가에서 생긴다고 이해합니다.
- 비용 견적은 실제로 호출할 모델로 token counting endpoint를 불러서 구합니다. tokenizer는 모델 세대마다 다르고, 다른 회사 모델용 tokenizer나 "글자 수 ÷ 4" 같은 추정은 Claude token을 적게 셉니다(특히 code와 영어가 아닌 텍스트에서). [Patrick-0029]
- 같은 모델이라면 어떤 형식의 model ID(alias 또는 snapshot)로 지정해도 단가가 같습니다. 비용을 줄이는 수단은 Batch 할인, prompt caching, 더 작은 모델 선택입니다. [Udemy-0002]

![요청당 token 진단에서 원인별 절감 수단으로 연결되는 매핑과 효과 없는 수단 목록](svg/5-cost-diagnosis.svg)
*그림: 비용이 늘면 요청당 token부터 보고, 원인에 맞춰 trimming·caching·Batch·effort·tier 하향 순으로 고른다.*

### 1-6. Batch API
- 대량이고 형태가 균일하며 기다려도 되는 작업(예: 사용자 상호작용이 없는 야간 대량 처리)은 Batch로 제출하는 것이 가장 쌉니다. [Amey-0056]
- Batch는 비동기 방식이므로 사람이 기다리는 interactive 작업(live chat, escalated reply, autocomplete)에는 맞지 않습니다. [Patrick-0011] [Preporato-0011] [Preporato-0015]
- Streaming은 interactive 용도이며 비용을 줄이지 않습니다. concurrency를 높여도 단가는 그대로입니다. [Amey-0056]

![사람이 기다리는지에 따라 Batch와 동기 호출/streaming을 고르는 decision tree](svg/5-batch-vs-realtime.svg)
*그림: Batch는 기다려도 되는 대량 작업에만 쓰고, 사람이 기다리는 요청은 동기 호출이나 streaming으로 처리한다.*

### 1-7. Prompt caching
- `cache_control`은 요청 최상위나 model parameter가 아니라 개별 content block에 붙입니다. 공유하는 영역의 마지막 block(보통 system prompt의 마지막 content block)에 두면 그 앞의 prefix 전체가 cache key가 됩니다. [Patrick-0003]
- breakpoint는 공유 preamble의 마지막 block에 두고, 매번 바뀌는 질문은 cache 밖에 둡니다. 바뀌는 부분 뒤에 breakpoint를 두면 요청마다 서로 다른 cache entry가 쓰이기만 하고 다시 읽히지 않습니다. 한 요청에 breakpoint는 최대 4개입니다. [Patrick-0021]
- Caching은 정확한 byte 단위의 prefix 일치로 동작합니다. 렌더링 순서는 tools → system → messages이므로, system prompt에 timestamp나 UUID를 넣거나 tool set을 요청마다 바꾸면 cache 전체가 무효가 됩니다. 이 경우 `cache_read_input_tokens`가 계속 0으로 나옵니다. 바뀌는 내용은 마지막 breakpoint 뒤로 옮깁니다. [Patrick-0020]
- TTL 선택: 요청이 몇 분 안에 몰리고 이후 몇 시간 동안 없다면 5분 ephemeral cache가 맞습니다. 1시간 cache는 write 비용이 더 비싸고, 이런 패턴에서는 hit가 더 생기지 않습니다. permanent cache 옵션은 없습니다. [Patrick-0008]

![올바른 breakpoint 위치와 두 가지 잘못된 위치를 tools·system·messages 띠로 비교한 그림](svg/5-cache-breakpoint.svg)
*그림: breakpoint는 공유 prefix의 마지막 block에 두고, 질문이나 timestamp처럼 바뀌는 값은 그 뒤에 둬야 cache read가 생긴다.*
![burst 요청 뒤 장시간 공백 패턴에서 5분 TTL과 1시간 TTL을 비교한 타임라인](svg/5-cache-ttl.svg)
*그림: 몇 분짜리 burst에는 5분 cache로 충분하고, 1시간 cache는 write만 비싸고 추가 hit가 없다.*

### 1-8. Version pinning과 snapshot
- Production에서는 model version을 고정(pin)합니다. 모델 업데이트로 refusal 등 동작이 바뀔 수 있으므로, 업그레이드를 eval을 거친 의도적인 변경으로 관리하기 위해서입니다. pinning은 가격, context window, API 필수 요건과는 관계가 없습니다. [Amey-0006] [Amey-0043]
- Model ID는 각각 고정된 snapshot을 가리키며 weight가 바뀌지 않습니다. 개선된 모델은 새 ID로 나오므로, 고정한 ID에 개선이 자동으로 들어오지 않습니다. 그래서 감사(audit)와 재현성을 설명하기 쉽습니다. [Udemy-0002]
- Pinning이 영구 사용을 보장하지는 않습니다. ID마다 retirement 일정("이 날짜 전에는 retire하지 않음")이 있으므로 후속 모델을 검증하고 이전하는 계획을 세웁니다. 정리하면 pinning으로 얻는 것은 재현성과 이전 시점을 직접 정할 수 있다는 점이고, 영속성이나 최신성은 얻지 못합니다. [Udemy-0002]
- 같은 ID라도 router나 safety classifier 같은 주변 시스템이 업데이트되면 동작이 약간 달라질 수 있습니다. [Udemy-0002]
- 이전 모델처럼 행동하라고 prompt로 요청해도 계약(보장)이 되지 않습니다. 다른 provider로 failover하면 동작 변화가 또 생기고, 에러를 빈 응답으로 처리하면 장애가 굳어집니다. [Amey-0006]
- ⚠️ 해설에 따르면 4.6 세대부터는 날짜 없는 ID(예: `claude-sonnet-5`) 자체가 고정 snapshot이고, 그 이전 세대에서는 날짜 붙은 ID(`claude-haiku-4-5-20251001`)가 snapshot, 날짜 없는 이름(`claude-haiku-4-5`)이 alias입니다. ID 명명 규칙은 세대마다 다르므로 문서를 확인합니다. [Udemy-0002]

![snapshot pin, 새 모델 출시, eval 검증, pin 변경으로 이어지는 업그레이드 루프](svg/5-version-pinning.svg)
*그림: production은 snapshot을 pin하고, 새 ID는 eval을 통과했을 때만 의도적으로 pin을 바꾼다.*

### 1-9. Sampling(temperature)과 비결정성, 테스트
- `temperature`는 다음 token을 고를 때의 무작위성을 조절합니다. 낮으면 안정적이고 보수적인 출력이 나오고(정형 추출에 적합), 높으면 다양하고 창의적인 출력이 나옵니다(아이디어 발상에 적합). 사실 정확도를 높이지 않으며, latency를 조절하는 파라미터도 아닙니다. [Udemy-0005]
- `temperature`를 0으로 해도 출력이 완전히 결정적이지는 않습니다. 같은 입력이라도 호출마다 결과가 다를 수 있습니다. [Udemy-0005] [Preporato-0014]
- 따라서 golden string과 정확히 일치하는지 확인하는 테스트는 실패가 들쭉날쭉합니다. 대신 구조와 핵심 사실(schema 유효성, 필수 필드, 반드시 나와야 하는 수치)을 assert하거나 rubric으로 채점합니다. 통과할 때까지 retry하면 회귀를 숨기고, 테스트를 지우면 안전망이 사라집니다. [Preporato-0014]
- latency에 영향을 주는 요소는 모델 크기, 입력과 출력의 길이, 사고량입니다. [Udemy-0005]
- ⚠️ 해설에 따르면 Claude Sonnet 5와 Opus 5.5 같은 일부 모델은 `temperature`, `top_p`, `top_k`를 기본값이 아닌 값으로 설정하면 에러를 냅니다. 이 경우 출력 방향은 prompt로 조정합니다. 모델별 사양이므로 문서를 확인합니다. [Udemy-0005]

![temperature 0에서도 비결정적인 출력을 테스트하는 올바른 방법과 오답 경로](svg/5-flaky-test.svg)
*그림: temperature 0도 결정적이지 않으므로 golden string 비교 대신 구조와 핵심 사실을 assert하거나 rubric으로 채점한다.*

## 2. 상황별 정답 판단 규칙

| 이런 상황이면 | 정답 방향 | 근거 |
|---|---|---|
| 대량의 단순 분류·추출·routing, 빠듯한 latency | Haiku(fast tier) | Patrick-0019, Udemy-0035 |
| 상호작용하는 제약이 많은 multi-step 계획 또는 마이그레이션 | 가장 capable한 모델(Opus) | Amey-0020, Amey-0058 |
| 큰 모델로 거의 완벽한 정확도가 나오는 대량 단순 작업 | 작은 모델이 요구 정확도를 충족하는지 평가 | Amey-0019 |
| 작은 모델과 큰 모델의 정확도가 같음 | 작은 모델 배포 | Amey-0057 |
| 두 모델 중 하나를 골라야 함 | 대표 sample과 quality bar로 둘 다 측정 | Amey-0022 |
| 작업마다 난이도가 다름(쉬운 대량 작업과 어려운 소량 작업) | Routing: 작업별로 tier 분리 | Patrick-0011, Patrick-0019 |
| Orchestrator와 다수의 worker subtask | Orchestrator는 capable, worker는 small·fast | Patrick-0037 |
| 호출량은 그대로인데 비용 급증 | 요청당 token과 다시 보내는 context 확인 | Amey-0021 |
| 품질은 괜찮은데 비용 증가 | context trimming과 stable prefix caching(tier 변경보다 먼저) | Preporato-0011 |
| 사용자 상호작용 없는 대량 야간 처리 | Batch API | Amey-0056 |
| 사용자가 기다리는 interactive 요청 | Batch는 쓰지 않음(stream 또는 동기 호출) | Patrick-0011, Preporato-0015 |
| 수백 ms 안에 응답해야 하는 짧은 autocomplete | Haiku + streaming + 작은 `max_tokens` | Preporato-0015 |
| 일상 작업이 느리고 token을 많이 쓰며, eval로 품질 유지 확인됨 | 해당 작업만 `output_config.effort`를 낮춤 | Preporato-0012 |
| 모든 요청에 thinking을 켰더니 단순 응답까지 느려짐 | workload별로 결정(필요한 곳에만 깊은 추론) | Preporato-0013 |
| 분류 작업과 복잡한 계획 작업이 섞임 | 분류는 few-shot, 계획은 effort를 높임 | Udemy-0009 |
| 긴 system prompt를 caching | 마지막 system content block에 `cache_control` | Patrick-0003 |
| 공유 preamble 뒤에 매번 다른 질문이 붙음 | preamble 마지막 block에 breakpoint | Patrick-0021 |
| `cache_read_input_tokens`가 항상 0 | prefix 안에서 바뀌는 값(timestamp, UUID, tool set)을 뒤로 옮김 | Patrick-0020 |
| 몇 분 안에 몰리는 burst 뒤 몇 시간 동안 요청 없음 | 5분 ephemeral cache | Patrick-0008 |
| 큰 prompt를 보내기 전에 비용을 추정해야 함 | 같은 모델로 token counting endpoint 호출 | Patrick-0029 |
| 모델 출시 후 production 동작이 바뀜, 규제 대응 | snapshot을 pin하고 업그레이드는 eval을 거쳐 진행 | Amey-0006, Udemy-0002 |
| 출력이 매번 달라 테스트가 flaky함 | 구조·핵심 사실 assert 또는 rubric 채점 | Preporato-0014 |

![작업 특성에 따라 Routing·Haiku·Opus·Sonnet 후보를 고르고 측정으로 확정하는 decision tree](svg/5-rules-model-tree.svg)
*그림: 작업 특성으로 tier 후보를 고르되, 최종 결정은 대표 sample과 quality bar로 측정해서 내린다.*
![비용·처리 방식·사고량 관련 상황별 정답 방향 매핑](svg/5-rules-cost-tree.svg)
*그림: 비용·latency·사고량 문제는 증상별로 정답 수단이 정해져 있다.*
![caching·version·테스트 관련 상황별 정답 방향 매핑](svg/5-rules-cache-version-tree.svg)
*그림: caching·version·테스트 문제도 증상을 보면 정답 방향이 하나로 좁혀진다.*

## 3. 자주 나오는 오답 함정

- "모든 작업에 가장 강한 모델을 쓰자(품질 일관성, 설정 단순화)" → 쉬운 작업에 비용과 latency를 낭비합니다. [Patrick-0011] [Patrick-0019] [Udemy-0035]
- "모든 작업에 가장 싼 모델을 쓰자" → 어려운 작업에서 품질이 모자랍니다. [Patrick-0011] [Patrick-0019]
- "prompt를 길게 쓰거나 다듬으면 작은 모델로도 복잡한 추론이 된다" → prompt로는 모델 능력 차이를 메우지 못합니다. [Amey-0058] [Udemy-0035]
- "추론 작업을 작은 모델 여러 개로 나눈다" → 추론이 끊어집니다. [Amey-0058]
- "benchmark 점수가 높거나 최신이거나 큰 모델을 고른다" → 실제 task로 측정한 근거가 아닙니다. [Amey-0022] [Amey-0057]
- "예산을 넘었거나 호출량이 많으니 작은 모델로 내린다" → 검토를 시작할 계기일 뿐입니다. quality bar를 측정으로 확인해야 합니다. [Amey-0072] [Preporato-0011]
- "검증하지 않고 바로 작은 모델이나 fast tier로 옮긴다" → eval로 확인하는 단계를 건너뛴 것입니다. [Preporato-0011] [Preporato-0012]
- "`max_tokens`를 낮춰 비용을 줄인다" → 작업 단가는 그대로이고 답이 잘립니다. [Patrick-0037] [Preporato-0012]
- "`max_tokens`를 높여 잘림을 막으면 비용 문제도 해결된다" → 지출이 오히려 늘 수 있습니다. [Preporato-0011]
- "thinking budget을 늘리거나 thinking을 모든 곳에 켠다", 또는 "모든 곳에서 끈다" → 일괄 설정은 틀립니다. workload별로 정합니다. [Preporato-0013] [Udemy-0009]
- "effort를 max로 두면 분류 품질도 오른다" → output token 비용과 latency만 늘어납니다. [Udemy-0009]
- "few-shot 예시를 수십 개 넣으면 깊은 추론을 대신한다" → context만 압박하고, 모델이 예시의 표면 패턴을 따라 하게 됩니다. [Udemy-0009]
- "live chat까지 포함해 모든 요청을 Batch로 보낸다" → Batch는 비동기라서 interactive 요청에 맞지 않습니다. [Preporato-0011] [Patrick-0011]
- "streaming이나 concurrency를 높이면 비용이 준다" → 단가는 그대로입니다. [Amey-0056]
- "context window가 큰 모델일수록 정확하고 rate limit도 적다" → 이점은 없고 cost와 latency만 늘어납니다. [Amey-0071]
- "`cache_control`을 요청 최상위나 model parameter에 붙인다", "모든 block에 붙인다", "첫 block에만 붙인다" → content block 단위로, 공유 영역의 마지막 block에 붙여야 합니다. [Patrick-0003] [Patrick-0021]
- "질문까지 포함한 prompt 끝에 breakpoint를 둔다" → 요청마다 새 entry를 쓰기만 하고 다시 읽지 않습니다. [Patrick-0021]
- "cache hit가 0이면 캐싱이 고장났거나 모델이 지원하지 않는 것이다" → 대부분 prefix 안에 바뀌는 값이 섞인 경우입니다. [Patrick-0020]
- "1시간 cache가 항상 더 좋다", "permanent cache를 쓴다" → 1시간 cache는 write가 더 비싸고, permanent 옵션은 없습니다. [Patrick-0008]
- "글자 수 ÷ 4로 추정하거나 다른 회사의 tokenizer로 센다", "일단 보낸 뒤 usage를 본다" → 부정확하거나 사전 견적이 아닙니다. [Patrick-0029]
- "pin한 모델은 더 싸다, 영구히 쓸 수 있다, 개선이 자동으로 반영된다" → 셋 다 틀립니다. pinning의 이점은 재현성과 이전 시점을 직접 정할 수 있다는 것입니다. [Udemy-0002] [Amey-0043]
- "이전 버전처럼 행동하라고 prompt로 지시한다", "다른 provider로 failover한다" → 동작이 보장되지 않습니다. [Amey-0006]
- "`temperature` 0이면 완전히 결정적이다", "`temperature`를 높이면 사실 정확도가 오른다" → 둘 다 틀립니다. [Udemy-0005] [Preporato-0014]
- "flaky 테스트는 통과할 때까지 retry하거나 삭제한다" → 회귀를 숨기거나 안전망을 없앱니다. [Preporato-0014]

## 4. 암기 목록

| 이름/숫자/파라미터 | 의미 |
|---|---|
| Haiku tier | 가장 빠르고 저렴함. classification, extraction, routing, autocomplete [Udemy-0035] [Preporato-0015] |
| Sonnet tier | 속도와 지능의 균형이 가장 좋음 [Udemy-0035] |
| Opus tier | 가장 capable함. multi-step reasoning, 오래 걸리는 agent 작업, 고난도 분석 [Udemy-0035] [Amey-0020] |
| ⚠️ Haiku 5.5 $0.10/$0.50, Sonnet 5.5 $2/$10, Opus 5.5 $4/$20 (per 1M input/output tokens) | 2026년 11월 기준 해설 수치입니다. 시험 가이드(2026년 7월판)는 이전 라인업(예: Haiku 4.5)을 기준으로 할 수 있어 시점에 따라 바뀝니다 [Udemy-0035] |
| ⚠️ "확신이 없으면 Opus 5.5부터" | 해설이 인용한 시점의 안내이며 버전에 따라 다릅니다 [Udemy-0035] |
| `output_config.effort` | 모델을 바꾸지 않고 응답 전체(thinking과 tool call 포함)의 token 사용량을 조절 [Preporato-0012] |
| effort low ~ max | adaptive thinking에서 생각의 적극성과 깊이를 조정 [Udemy-0009] |
| ⚠️ `budget_tokens` | 예전 extended thinking에서 사고량을 고정하던 방식. 해설에 따르면 Opus 4.7 이후 지원하지 않음 [Udemy-0009] |
| thinking token | output token으로 과금되며 latency가 늘어남 [Udemy-0009] [Preporato-0013] |
| few-shot 예시 수 3~5개 | 관련성 있고 다양한 예시를 고름 [Udemy-0009] |
| `max_tokens` | 출력 상한. 낮추면 잘리고, 높이면 지출이 늘 수 있음. 단가를 바꾸지는 않음 [Patrick-0037] [Preporato-0011] |
| `cache_control` | content block 단위로 지정. 공유 영역의 마지막 block에 둠 [Patrick-0003] |
| breakpoint 최대 4개 | 요청 1건당 [Patrick-0021] |
| tools → system → messages | prefix 렌더링 순서. 앞부분이 바뀌면 그 뒤가 모두 무효 [Patrick-0020] |
| `cache_read_input_tokens` | cache hit로 읽은 token 수. 계속 0이면 prefix가 바뀌고 있다는 신호 [Patrick-0020] |
| 5분 ephemeral / 1시간 cache | 짧은 burst에는 5분이 맞음. 1시간은 write 비용이 더 비쌈. permanent 옵션 없음 [Patrick-0008] |
| token counting endpoint | 보내기 전 token 수 견적. 실제로 호출할 모델로 셈 [Patrick-0029] |
| Batch API | 비동기 방식이며 기다려도 되는 대량 작업에서 훨씬 저렴함 [Amey-0056] |
| snapshot / alias | snapshot은 weight가 고정됨. alias는 최신 snapshot을 가리킴. 개선은 새 ID로 제공 [Udemy-0002] |
| retirement 일정 | 모델 ID마다 정해진 retire 예정일. pinning해도 영구히 쓸 수 없음 [Udemy-0002] |
| `temperature` / `top_p` / `top_k` | sampling 무작위성 조절. 0으로 해도 완전히 결정적이지 않음 [Udemy-0005] |

## 5. 시험 직전 체크리스트

- [ ] 모델 선택은 "요구 수준을 충족하는 가장 싼 모델"을 고르는 일이고, 근거는 실제 task 기준 eval이다(benchmark 점수, 최신, 큰 모델이라는 점은 근거가 아니다).
- [ ] Haiku는 대량·단순·저지연 작업, Opus는 multi-step·다중 제약 추론, Sonnet은 균형형이다.
- [ ] 난이도가 섞인 workload는 routing으로 처리한다(orchestrator는 강한 모델, worker는 작은 모델).
- [ ] tier를 내리기 전에 context trimming과 prefix caching을 먼저 한다.
- [ ] 비용이 늘면 먼저 요청당 token과 다시 보내는 context를 본다.
- [ ] `max_tokens`는 비용 절감 수단이 아니다(답이 잘림).
- [ ] thinking과 effort는 workload별로 정하고, 단순 응답에서는 낮춘다. thinking token은 output으로 과금된다.
- [ ] 형식은 few-shot(3~5개)으로, 생각의 깊이는 effort로 조절한다.
- [ ] Batch는 기다려도 되는 대량 작업에만 쓰고, interactive 요청에는 쓰지 않는다.
- [ ] `cache_control`은 공유 prefix의 마지막 block에 두고, breakpoint는 최대 4개다.
- [ ] cache hit가 0이면 prefix 안에서 바뀌는 값(timestamp, UUID, tool set)을 찾는다.
- [ ] 짧은 burst에는 5분 TTL을 쓴다. 1시간 cache는 write가 더 비싸다.
- [ ] 사전 token 견적은 같은 모델로 token counting endpoint를 호출해서 구한다.
- [ ] production에서는 snapshot을 pin하고, 업그레이드는 eval을 거친 의도적 변경으로 한다. retirement 일정도 확인한다.
- [ ] `temperature` 0이어도 출력은 비결정적이므로, 테스트는 구조와 핵심 사실을 assert하거나 rubric으로 채점한다.
