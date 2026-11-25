# 6. Prompt and Context Engineering — 반드시 알아야 할 지식
> 시험 비중 11% · 약 3문항 · 근거 문항 23개

## 1. 핵심 개념

### 1.1 System prompt vs user message 역할 분리
- 역할(role), 행동 규칙, 안전 제약처럼 **모든 턴에 일관되게 적용할 안정적 지침**은 system prompt에 둔다. 매번 바뀌는 사용자 질문·참조 데이터는 user message에 둔다. [Amey-0028] [Amey-0061] [Udemy-0012]
- 지침을 user 턴(첫 메시지, 마지막 메시지, 매 메시지 반복)에 두면 configuration과 input이 뒤섞여 drift가 생긴다. 사용자 입력 문구에 따라 지침이 약해지거나 덮어써질 수 있고, 유지보수도 어려워진다. [Amey-0028] [Amey-0061] [Udemy-0012]
- system prompt를 쓸 수 없는 환경에서는 지시를 user message에 쓰는 방식도 실제로 쓰이고 Claude도 대체로 따른다. 하지만 원칙은 아니다. [Udemy-0012]
- 반대로 사용자별 질문까지 system prompt에 넣으면 신뢰할 수 없는 입력을 지침과 같은 권위로 다루게 된다. 항상 참조할 배경 정보(운영 규칙 요점 등)를 system prompt에 넣는 것은 일반적이다. [Udemy-0012]
- Messages API에서 `system`은 top-level 파라미터로 대화 전체의 전제를 주고, `messages`의 user 턴이 개별 요청을 담당한다. [Udemy-0012]
- Tool description은 tool 선택을 좌우하는 곳이지, 매 턴 적용할 행동 지침을 두는 곳이 아니다. [Amey-0061]
- system prompt로 role을 설정하면 행동과 어조가 용도에 맞게 안정된다. [Udemy-0012]

![system prompt와 user message에 각각 무엇을 두는지와 잘못된 배치 세 가지](svg/6-system-vs-user.svg)
*그림: 안정적 지침은 top-level system에, 매번 바뀌는 입력은 user 턴에 두며, 이를 뒤섞으면 drift나 권위 혼동이 생긴다.*

### 1.2 인터페이스마다 다른 컨텍스트
- 모델이 받는 것은 지시문만이 아니라 그 주변 컨텍스트 전체다. claude.ai/모바일 앱은 자체 system prompt(현재 날짜, 응답 스타일 등)를 넣고 이는 API에는 적용되지 않는다. Claude Code는 여기에 tool 정의, CLAUDE.md, auto memory, 세션 상태 등을 더한다. [Udemy-0015]
- Messages API에서는 `system`과 `messages`를 개발자가 직접 조립한다. 일관된 동작이 필요한 프로덕션은 API/SDK 위에 구축하고 **실제 제공 환경에서 평가**한다. [Udemy-0015]
- 같은 지시인데 인터페이스별 결과가 다르면 버그가 아니라 설계상 차이다. 세 인터페이스가 같은 system prompt로 동작하지 않는다. 지시문만 고쳐서는 지시문 바깥의 컨텍스트 차이가 남는다. [Udemy-0015]

![같은 지시문에 claude.ai, Claude Code, Messages API가 각각 다른 컨텍스트를 붙이는 흐름](svg/6-interface-context.svg)
*그림: 인터페이스별 결과 차이는 지시문 바깥에 붙는 컨텍스트 차이에서 오므로, 프로덕션은 API/SDK로 만들고 실제 환경에서 평가한다.*

### 1.3 Few-shot 예시 (multishot)
- Few-shot이 맞는 상황은 **출력 형식이나 edge-case 처리가 일관되지 않고, 예시로 목표 동작을 보여 줄 수 있을 때**다. 형식과 edge-case 동작은 지시를 더 쓰는 것보다 예시로 훨씬 잘 고정된다. [Amey-0046] [Amey-0062] [Udemy-0042]
- Few-shot은 사실 지식을 보충하지 못하고, latency를 줄이거나 작은 context window를 해결하는 수단도 아니다(예시는 오히려 token을 쓴다). [Amey-0046]
- 여러 제약을 동시에 지켜야 할 때는 **규칙을 지킨 출력 예시**(worked example)가 제약들의 상호작용까지 보여 준다. 산문 설명으로는 이것이 안 된다. [Amey-0027]
- 권장 구성: 실제 용도와 가까운(relevant) 예시와 경계 사례까지 포함한(diverse) 예시를 소수(3~5개, 문항에 따라 2~4개)만 쓰고 `<example>` 태그로 감싸 지시·실제 입력과 분리한다. [Udemy-0042] [Preporato-0022]
- 까다로운 classification에서는 다양한 예시에 **모델이 거부(reject)해야 할 negative case**를 넣어 경계를 가르친다. 모두 같은 label인 예시나 거의 같은 예시 50개는 좁은 패턴만 가르친다. [Preporato-0022]
- 예시는 개수보다 질이다. 선별 없이 수십 개를 넣으면 편향되거나 잘못된 예시에서 의도치 않은 패턴을 배우고 컨텍스트도 차지한다. [Udemy-0042]
- 지시와 예시가 서로 모순되면 정해진 우선순위 없이 **두 쪽 사이에서 동작이 예측 불가능**해진다. 지시와 예시 어느 쪽도 확실히 이기지 않고, 요청이 거부되지도 않는다. 모순된 예시는 robustness 테스트가 아니라 모델이 지시를 무시하게 가르친다. [Amey-0075] [Preporato-0022]

![few-shot을 쓸 때와 쓰지 말아야 할 때, 그리고 지시와 예시가 모순될 때의 decision tree](svg/6-fewshot-when.svg)
*그림: few-shot은 형식과 edge-case가 흔들릴 때만 쓰고, 소수의 다양한 예시를 지시와 모순 없이 넣어야 한다.*

### 1.4 출력 형식 지정
- 형식은 "~하지 마라"가 아니라 "~형식으로 출력하라"처럼 **긍정형**으로 지정한다. "목록으로 쓰지 마라", "설명을 붙이지 마라" 같은 금지 목록은 원하는 형태를 보여 주지 못한다. [Udemy-0042]
- 필요하면 XML 태그로 출력 구조를 보여 준다. 형식 설명만으로는 항목 순서나 표기 변형(단위 등)을 세세하게 전달하기 어렵다. 예시와 함께 쓸 때 효과가 크다. [Udemy-0042]
- 강조(가장 중요한 제약 강조), 프롬프트 끝에서 제약 반복은 다시 말할 뿐 명확하게 하지 않는다. "깔끔하게(neat)" 같은 모호한 형용사는 아무것도 규정하지 않는다. [Amey-0027] [Amey-0062]
- temperature를 올리면 variance가 커져 일관성·신뢰성과 반대 방향이 된다. 더 큰 모델도 당신의 형식을 알지 못한다. [Amey-0027] [Amey-0062] [Amey-0045]

### 1.5 Structured outputs, tool 강제, prefill 폐지
- **스키마 검증을 통과하는 JSON을 보장**해야 하면 structured outputs(constrained decoding)를 쓴다. 요청의 `output_config.format`에 JSON schema를 넣는다. JSON을 산문으로 감싸는 류의 실패를 원천적으로 없앤다. [Patrick-0026] [Preporato-0021] [Udemy-0042]
- tool을 하나 정의해 그 `input_schema`를 원하는 JSON 형태로 두고 `tool_choice`로 그 tool을 강제하면 Claude가 반드시 그 tool을 호출하고, `input`이 구조화된 객체가 된다. [Patrick-0004]
  - ⚠️ 해설은 이것을 "가장 신뢰할 수 있는 방법"이라 하지만, 현재 공식 문서상 스키마 준수가 *보장*되는 것은 structured outputs(`strict` tool 포함)다. strict 없는 tool 강제는 매우 신뢰성이 높을 뿐 보장은 아니다. 선택지에 structured outputs가 있으면 그쪽이 우선이다.
- system prompt의 "JSON으로 답하라" 지시, temperature 0, 자유 텍스트에 regex parser는 모두 확률적이어서 스키마 준수를 보장하지 못한다. [Patrick-0004] [Patrick-0026]
- assistant 턴 prefill(예: `{`로 시작)은 과거의 형식 강제 기법이다. **Claude 4.6 모델부터** 마지막 assistant 턴 prefill은 400 error로 거부되고, 마이그레이션 가이드는 structured outputs를 대체 수단으로 지정한다(prefill은 제거). 대안이 아니라 대체재다. [Patrick-0026] [Preporato-0021]
- 프로덕션 추출 endpoint는 모델 출력을 **untrusted input**으로 다룬다. tool use로 스키마를 강제하고, 파싱한 결과를 검증하고, 실패하면 validation error를 덧붙여 한 번 retry해 모델이 스스로 고치게 한다. [Amey-0039]

![스키마 준수 JSON 필요 여부에 따라 structured outputs, forced tool choice, 확률적 방법을 고르는 decision tree](svg/6-output-format-tree.svg)
*그림: 스키마 보장이 필요하면 structured outputs, 선택지에 없으면 tool 강제이며, 지시·temperature·regex·prefill은 보장 수단이 아니다.*

![추출 결과를 검증하고 실패하면 validation error를 붙여 retry하는 루프](svg/6-validation-retry.svg)
*그림: 모델 출력은 untrusted input이므로 검증에 실패하면 숨기거나 땜질하지 말고 error를 붙여 다시 요청한다.*

### 1.6 긴 문서(long context) 배치
- 긴 프롬프트 한가운데 묻힌 내용은 가장자리(앞·끝)에 둔 내용보다 놓치기 쉽다. 위치는 중립이 아니고, 가운데 둔다고 더 잘 지켜지지도 않으며, 오류가 나지도 않는다. [Amey-0076]
- 약 20K tokens를 넘는 긴 입력은 **문서를 프롬프트 위쪽에, 지시·질문을 맨 끝에** 둔다. 복잡한 multi-document 입력 테스트에서 응답 품질이 최대 30% 향상되었다. [Preporato-0020] [Udemy-0024] [Udemy-0012]
- 문서는 `<contract>` 같은 태그로 감싼다. 여러 문서는 각각 `<document>` 태그로 감싸고 `<document_content>`, `<source>` 등의 하위 태그로 본문과 출처(metadata)를 구분한다. 그러면 어느 내용이 어느 문서에서 왔는지 혼동하지 않는다. [Preporato-0020] [Udemy-0024]
- 답하기 전에 관련 부분을 먼저 **인용(quote)**하게 하면 Claude가 집중하는 데 도움이 된다. [Preporato-0020] [Udemy-0024]
- 구조 문제는 parameter나 다른 기능으로 해결되지 않는다. effort는 thinking·응답 token 양을 조절할 뿐이고, prompt caching(`cache_control`)은 반복 질의의 비용·속도용이라 모델이 읽는 내용을 바꾸지 않는다. 사전 요약은 창에 안 들어가거나 개요만 필요할 때용이고 세부와 출처를 잃는다. [Udemy-0024]

![질문을 앞에 두고 문서를 이어 붙인 배치와 문서를 태그로 감싸 위에 두고 질문을 끝에 둔 배치 비교](svg/6-long-doc-order.svg)
*그림: 긴 입력은 문서를 문서별 태그로 감싸 위에, 인용 지시와 질문을 끝에 둔다.*

![긴 프롬프트의 앞, 가운데, 끝 중 가운데가 놓치기 쉬움을 보여 주는 그림](svg/6-lost-in-middle.svg)
*그림: 긴 프롬프트 한가운데 내용은 놓치기 쉬우므로 중요한 지시는 앞이나 끝으로 옮긴다.*

### 1.7 Context는 예산이다 (context rot)
- 컨텍스트는 공짜 자원이 아니라 예산이다. "혹시 도움이 될까" 넣은 느슨한 배경 자료는 관련 자료와 attention을 놓고 경쟁해 **비용뿐 아니라 정확도도** 떨어뜨린다. 모델은 질문이 참조하지 않는 내용을 알아서 무시해 주지 않는다. [Amey-0029]
- token이 늘수록 앞서 읽은 내용을 정확히 끌어오지 못하는 현상을 **context rot**라고 한다. 무엇을 넣을지 고르는 것이 용량만큼 중요하다. [Udemy-0020] [Udemy-0022]
- 창의 상한에 들어가는 것과 정확도가 유지되는 것은 별개다. 1M token 같은 큰 창은 긴 자료를 한 번에 읽힐 때 유용하지만, 전체 이력을 계속 끌고 가면 context rot와 비용·latency가 커진다. [Udemy-0020] [Udemy-0022] [Amey-0007]

![관련 자료만 넣은 context window와 배경 자료와 이력을 다 넣은 context window 비교](svg/6-context-budget-rot.svg)
*그림: 불필요한 자료는 관련 자료와 attention을 놓고 경쟁해 비용뿐 아니라 정확도도 떨어뜨린다.*

### 1.8 Context hygiene: prune, compact, isolate
- 장시간 assistant가 반복하고, 이전 사례를 혼동하고, 최근 지시를 잊고, 자기모순을 보이며 컨텍스트가 장황한 tool output으로 가득 찼다면 → context drift/bloat다. 해법은 세 가지다. [Amey-0007] [Amey-0045]
  - prune: tool output을 잘라내고 요약한다.
  - compact: 대화 이력을 압축한다.
  - isolate: 독립된 subtask를 subagent로 분리해 main context를 가볍게 유지한다.
- Messages API는 **stateless**다. 대화를 이어가려면 system prompt와 과거 messages를 매번 다시 보내고, 그 전부가 context window와 input token 과금에 쌓인다. 최신 메시지만 보내면 Claude는 앞의 경위를 모른다. [Udemy-0020]
- 세션 관리(session hygiene): 용건(task)이 바뀌면 세션을 나누고(isolate), 오래된 턴은 요약(compaction)하고, 불필요한 부분은 잘라낸다. 관련 컨텍스트만 남긴다. [Udemy-0020] [Patrick-0041]
- **오래된 턴은 요약·compact하고 최근 턴은 원문 그대로** 둔다. 그러면 중요한 사실(예: 고객의 원래 문제)은 남기면서 공간을 비운다. 이력 없이 새 대화를 시작하면 문제 자체를 잊는다. [Patrick-0041]
- Compaction: 오래된 턴을 Claude가 server 측에서 작성한 요약으로 대체한다. 긴 대화와 장시간 agent를 상한 내에서 이어가는 핵심 전략이다. Context editing: 오래된(stale) tool result를 제거한다. [Udemy-0022] [Patrick-0041]
- Agent의 tool output이 커지는 문제는 2단계로 다룬다. [Udemy-0022]
  - ① 입구: tool 응답이 다음 판단에 필요한 항목만 반환하도록 설계한다(공식 tool 설계 지침).
  - ② 누적: compaction / context editing으로 줄인다.
- `max_tokens`는 한 번 응답의 **출력** 상한이다(응답이 잘려 `stop_reason`이 `max_tokens`일 때 올림). context window 용량을 늘리지 않는다. 올려도 줄여도 bloat의 해법이 아니다. [Udemy-0022] [Patrick-0041] [Amey-0045]
- 쓰지 않는 tool을 빼면 tool 정의가 차지하는 token은 줄지만, 핵심 기능의 tool을 끊으면 목적 자체가 무너진다. 문제는 tool의 존재가 아니라 가공 없이 쌓이는 결과다. [Udemy-0022]
- server에 대화 상태를 보존하는 구조는 Anthropic-hosted managed agent 세션 등에는 있지만, Messages API의 전제는 아니다. [Udemy-0020]

![context drift/bloat 증상에서 prune, compact, isolate 세 해법으로 갈라지는 그림](svg/6-context-hygiene.svg)
*그림: drift/bloat는 prune, compact, isolate로 다루며, 큰 창이나 max_tokens 조정은 해법이 아니다.*

![stateless Messages API에서 요청마다 이력이 쌓이고 compaction으로 줄이는 흐름](svg/6-stateless-compaction.svg)
*그림: Messages API는 매 요청에 이력을 다시 보내므로 오래된 턴은 요약하고 최근 턴은 원문으로 남긴다.*

![tool 결과를 입구에서 줄이고 누적분을 compaction과 context editing으로 정리하는 두 단계](svg/6-tool-output-two-stage.svg)
*그림: tool output은 입구에서 필요한 항목만 반환하고, 누적분은 compaction과 context editing으로 줄인다.*

## 2. 상황별 정답 판단 규칙

| 이런 상황이면 | 정답 방향 | 근거 |
|---|---|---|
| 모든 턴에 적용할 role/행동/안전 제약을 어디에 둘까 | system prompt (가변 입력은 user message) | [Amey-0028] [Amey-0061] [Udemy-0012] |
| 같은 지시인데 claude.ai·Claude Code·API 결과가 다름 | 인터페이스별로 붙는 컨텍스트 차이를 이해하고, 프로덕션은 API/SDK로 구축해 실제 환경에서 평가 | [Udemy-0015] |
| 내용은 맞는데 형식이 매번 다름 | 정확한 출력 예시. 관련성 있고 다양한 예시 3~5개를 `<example>` 태그로 + 긍정형 형식 지정 | [Amey-0062] [Udemy-0042] |
| 여러 제약을 동시에 지켜야 함 | 규칙을 지킨 출력 예시를 준다 | [Amey-0027] |
| few-shot을 써야 하나? | 형식·edge-case가 흔들릴 때만. 지식 부족, latency, 작은 창 문제에는 아님 | [Amey-0046] |
| 까다로운 classification few-shot | 다양한 소수 예시 + reject case, `<example>` 태그로 실제 입력과 분리 | [Preporato-0022] |
| 지시와 예시가 모순됨 | 결과는 예측 불가 → 모순 제거 | [Amey-0075] |
| 스키마 검증을 통과하는 JSON을 보장 | structured outputs (`output_config.format` + JSON schema) | [Patrick-0026] |
| 엄격한 스키마 JSON, 선택지에 structured outputs가 없음 | `input_schema` tool + `tool_choice` 강제, `input`을 사용 | [Patrick-0004] |
| prefill `{` 코드가 새 모델에서 400 error | prefill 제거 + structured outputs | [Preporato-0021] |
| 추출 결과에 필수 필드가 가끔 빠져 다운스트림 예외 | tool use 스키마 강제 + 결과 검증 + validation error를 붙여 retry | [Amey-0039] |
| 긴 계약서·보고서에서 답이 관련 조항을 놓침 | 문서를 태그로 감싸 위에, 지시·질문은 끝 + 관련 조항을 먼저 인용하게 함 | [Preporato-0020] |
| 여러 개의 긴 문서를 구분 없이 이어 붙이고 질문은 앞 | 문서를 앞으로, 문서별 `<document>` + `<source>` 태그, 질문은 끝 | [Udemy-0024] |
| 가장 중요한 지시가 긴 프롬프트 한가운데 있음 | 놓치기 쉬움 → 앞이나 끝으로 이동 | [Amey-0076] |
| "혹시 몰라" 배경 자료를 많이 넣음 | 관련 자료와 경쟁해 정확도 하락 → 관련 자료만 | [Amey-0029] |
| 장시간 assistant가 반복·혼동·지시 망각, 컨텍스트가 tool output으로 가득 | prune·요약 / compact / subagent로 isolate | [Amey-0007] [Amey-0045] |
| 수백 턴 support chat이 창 상한에 닿음 | 오래된 턴 요약·compaction, 최근 턴은 원문 유지 | [Patrick-0041] |
| 장시간 고객 대화의 session 설계 | 용건별 세션 분리 + 오래된 부분 요약·제거 | [Udemy-0020] |
| Agent tool이 원시 데이터를 대량 반환해 품질·비용·latency 악화 | tool 결과를 필요한 항목으로 축소 + 오래된 대화 요약 | [Udemy-0022] |

![지침 배치, 인터페이스 차이, JSON 출력 관련 판단 규칙 decision tree](svg/6-rules-placement-output.svg)
*그림: 지침 위치와 JSON 출력 문제는 system prompt, 실제 환경 평가, structured outputs, 검증 후 retry로 답한다.*

![형식과 few-shot 관련 판단 규칙 decision tree](svg/6-rules-fewshot.svg)
*그림: 형식 문제는 예시로 고정하되 reject case를 넣고 지시와 모순되지 않게 하며, 지식·latency·창 문제에는 쓰지 않는다.*

![긴 문서와 context 관리 관련 판단 규칙 decision tree](svg/6-rules-context.svg)
*그림: 긴 문서는 위·질문은 끝, context는 관련 자료만 남기고 prune·compact·isolate로 관리한다.*

## 3. 자주 나오는 오답 함정

**Context bloat / 장시간 세션**
- "더 큰 context window(1M) 모델로 옮겨 그대로 계속" / "1M 창에 전체 이력 또는 tool 원시 데이터를 유지" → 같은 실패를 늦출 뿐이고, context rot와 비용·latency가 커진다. [Amey-0007] [Udemy-0020] [Udemy-0022]
- "매 턴 뒤에 system prompt 반복" → 반복은 bloat를 가속하고, 지시는 이미 system prompt에 있다. [Amey-0007] [Amey-0045]
- "모델에게 앞선 혼동을 무시하라고 요청" → 메커니즘이 아니다. [Amey-0007]
- "temperature를 올려 다양성 유도" → variance만 커지고 drift를 고치지 못한다. [Amey-0045]
- "응답마다 `max_tokens` 줄이기" / "`max_tokens`를 올려 창 확장" / "`max_tokens`를 올려 긴 응답을 끝까지 출력" → `max_tokens`는 출력 상한일 뿐 창 용량이나 누적 입력과 무관하다. 올리면 오히려 창을 더 쓴다. [Amey-0045] [Patrick-0041] [Udemy-0022]
- "상한이 가까우면 이력 없이 새 대화 시작" → 고객의 원래 문제를 잊는다. [Patrick-0041]
- "system prompt를 제거해 공간 확보" → assistant가 지켜야 할 규칙을 잃는다. [Patrick-0041]
- "용건이 바뀌어도 같은 세션에서 이력을 깎지 않고 매번 재전송" → 무관한 이력이 노이즈가 되고 input token 과금이 는다. [Udemy-0020]
- "대화 상태는 server에 두고 최신 메시지만 전송" → Messages API는 stateless다. Claude가 경위를 모른다. [Udemy-0020]
- "센서 데이터 tool 등록을 해제" → 핵심 기능이 무너진다. 원인은 가공 없이 쌓이는 결과다. [Udemy-0022]
- "많은 배경 자료는 정확도를 올린다" / "모델은 질문과 무관한 것은 무시한다" / "영향은 비용뿐" → 모두 틀렸다. 관련 자료와 경쟁해 정확도도 떨어진다. [Amey-0029]

**지침 배치 / 인터페이스**
- 지침을 "모든 대화의 첫 user message"에, "가장 신선하도록 마지막 메시지"에, 또는 "매 user message에 반복"해서 두기 → configuration과 input이 섞여 drift가 생기고 입력에 의해 덮어써질 수 있다. [Amey-0028] [Amey-0061]
- "안전 제약을 user message 쪽에 두고 질문마다 조정" → 입력 문구에 따라 약해지거나 덮어써질 수 있다. [Udemy-0012]
- "system prompt 없이 매번 user message 앞에 지시를 모아 씀" → 동작은 하지만 지침 유지보수가 어렵고 입력이 지침을 약화시킬 여지가 생긴다. [Udemy-0012]
- "질문까지 포함해 전부 system prompt에" → 신뢰할 수 없는 입력을 지침과 같은 권위로 다룬다. [Udemy-0012]
- 행동 지침을 "tool description에" 두기 → tool description은 tool 선택용이다. [Amey-0061]
- 인터페이스별 차이에 "지시문만 자세히 고쳐서 맞춤" → 지시 바깥의 컨텍스트 차이는 남는다. [Udemy-0015]
- 인터페이스별 차이에 "세 곳이 같은 system prompt이니 모델 버그로 보고" → 전제가 틀렸다. 각각 다른 컨텍스트를 붙인다. [Udemy-0015]
- 인터페이스별 차이에 "가장 좋은 하나만 쓰고 검증 중단" → 원인을 모른 채 환경이 바뀌면 같은 문제가 재발한다. [Udemy-0015]

**Few-shot / 형식**
- "가장 중요한 제약을 강조" / "프롬프트 끝에 제약 반복" → 다시 말할 뿐 명확해지지 않는다. [Amey-0027]
- "temperature를 올려 더 많은 선택지 탐색" → variance가 커져 신뢰성과 반대 방향이다. [Amey-0027] [Amey-0062]
- "출력을 깔끔하게(neat) 해 달라고 요청" → 모호한 형용사는 형식을 규정하지 않는다. [Amey-0062]
- "더 큰 모델 사용" → 모델은 당신의 형식을 모른다. [Amey-0062]
- few-shot을 "사실 지식 보충", "latency 감소", "작은 context window 해결"에 쓴다 → few-shot은 형식·edge-case 동작을 보여 주는 도구다. [Amey-0046]
- "예시 없이 형식 설명 단락만 추가" → 항목 순서·표기 변형까지 세세하게 전달하지 못한다. [Udemy-0042]
- "목록으로 쓰지 마라 / 설명을 붙이지 마라 같은 금지사항 나열" → 원하는 형태를 보여 주지 못한다. 긍정형으로 지정한다. [Udemy-0042]
- "선별 없이 메모 수십 개를 그대로 예시로" / "거의 같은 예시 50개" → 편향·오류 패턴을 학습하고 컨텍스트를 차지한다. [Udemy-0042] [Preporato-0022]
- "모든 예시가 같은 label" → 경계를 가르치지 못한다. [Preporato-0022]
- "robustness 테스트로 지시와 모순되는 예시를 넣음" → 모델이 지시를 무시하게 가르친다. [Preporato-0022]
- 지시·예시가 모순될 때 "지시가 항상 이긴다" / "예시가 항상 이긴다" / "요청이 거부된다" → 정해진 precedence가 없고 결과는 예측 불가다. [Amey-0075]

**JSON / structured output**
- "system prompt에서 JSON으로 답하라고 지시" / "더 강하게 지시" → 확률적이라 보장되지 않는다. [Patrick-0004] [Amey-0039]
- "temperature 0" → 결정성과 스키마 준수는 다르다. [Patrick-0004]
- "자유 텍스트나 산문에서 regex로 JSON 추출" → 취약하고 보장되지 않는다. [Patrick-0004] [Patrick-0026] [Preporato-0021]
- "JSON 요청 + 예시 2개 + 방어적 파싱과 retry" → 여전히 확률적이다. 보장이 필요하면 structured outputs다. [Patrick-0026]
- "assistant 턴을 `{`로 prefill" → Claude 4.6부터 400 error다. "`[`로 prefill"도 여전히 prefill이다. [Patrick-0026] [Preporato-0021]
- "구 모델에 영구히 머무름" → 향후 업그레이드가 모두 막힌다. [Preporato-0021]
- "try로 감싸 실패 시 빈 객체 반환" → 실패를 숨겨 다운스트림으로 넘긴다. [Amey-0039]
- "누락 필드를 regex 후처리로 삽입" → 가짜 데이터를 만든다. 검증 후 retry가 맞다. [Amey-0039]

**긴 문서**
- "질문을 먼저, 그다음 문서" / "질문을 문서 한가운데" → 장문 가이드와 반대다. 문서는 위, 질문은 끝. [Preporato-0020] [Amey-0076]
- "문서를 질문 앞뒤로 두 번" → 비용과 노이즈만 두 배다. [Preporato-0020]
- "중요 지시의 위치는 상관없다" / "가운데 두면 더 잘 지켜진다" / "오류가 난다" → 가운데 내용은 놓치기 쉬울 뿐이다. [Amey-0076]
- "effort를 높여 더 깊이 생각" → 비용·latency만 늘고 구조와 출처 문제는 그대로다. [Udemy-0024]
- "보고서를 각각 사전 요약해 요약만 전달" → 공통 지적 사항 같은 세부와 출처를 잃는다. 입력이 이미 창에 들어가면 불필요하다. [Udemy-0024]
- "보고서 끝에 `cache_control`" → 비용·속도만 개선되고 모델이 읽는 내용은 그대로다. [Udemy-0024]

## 4. 암기 목록

| 이름/기법 | 의미 |
|---|---|
| System prompt | 대화 전체에 적용되는 안정적 지침(role, 행동, 안전 제약)을 둔다. API의 top-level `system` 파라미터 [Udemy-0012] |
| Few-shot (multishot) | 소수 예시(3~5개), relevant + diverse(경계·reject case 포함), `<example>` 태그로 분리. 형식·edge-case용 [Udemy-0042] [Preporato-0022] [Amey-0046] |
| Structured outputs | `output_config.format`에 JSON schema를 넣어 constrained decoding. 스키마 준수 보장. prefill의 대체재 [Patrick-0026] [Preporato-0021] |
| Prefill | assistant 턴 시작을 미리 채우는 구 기법. Claude 4.6부터 마지막 assistant 턴 prefill은 400 error [Preporato-0021] |
| Forced tool choice | `input_schema`가 목표 JSON인 tool + `tool_choice`로 호출 강제. `input`을 구조화 객체로 사용 [Patrick-0004] |
| Validation-retry loop | 결과를 검증하고 실패하면 validation error를 붙여 retry. 출력은 untrusted input [Amey-0039] |
| Long-context 배치 | 문서는 태그로 감싸 위에, 질문은 끝(약 20K+ tokens, 최대 30% 향상) + 먼저 인용 [Preporato-0020] [Udemy-0024] |
| `<document>` / `<document_content>` / `<source>` | 여러 문서를 하나씩 감싸고 본문과 출처를 분리하는 XML 태그 [Udemy-0024] |
| Lost in the middle | 긴 입력 한가운데 내용은 가장자리보다 놓치기 쉬움 [Amey-0076] |
| Context rot | token이 늘수록 앞서 읽은 내용을 정확히 끌어오지 못하는 현상 [Udemy-0020] [Udemy-0022] |
| Compaction | 오래된 턴을 server 측 요약으로 대체, 최근 턴은 원문 유지 [Udemy-0022] [Patrick-0041] |
| Context editing | 오래된(stale) tool result 제거 [Udemy-0022] [Patrick-0041] |
| Prune / Compact / Isolate | context hygiene 3원칙: tool output 자르기·요약 / 이력 압축 / subtask를 subagent·세션으로 분리 [Amey-0007] [Amey-0045] |
| `max_tokens` | 응답 1회의 출력 상한. context window와 무관 [Udemy-0022] |
| Effort | thinking과 응답에 쓰는 token 양을 조절. 프롬프트 구조 문제는 못 고침 [Udemy-0024] |
| `cache_control` (prompt caching) | 같은 접두부 재전송 시 비용·속도 개선. 모델이 읽는 내용은 불변 [Udemy-0024] |

## 5. 시험 직전 체크리스트

- [ ] 안정적 지침은 system prompt, 가변 입력은 user message에 둔다
- [ ] tool description은 tool 선택용이지 행동 지침용이 아니다
- [ ] 인터페이스별 출력 차이 = 붙는 컨텍스트 차이. 프로덕션은 API/SDK로 만들고 실제 환경에서 평가
- [ ] 형식 불일치에는 예시가 답이다 (3~5개, relevant + diverse, `<example>` 태그)
- [ ] few-shot은 지식, latency, 창 크기 문제의 해법이 아니다
- [ ] 형식은 긍정형("~형식으로")으로 지정한다
- [ ] few-shot classification에는 reject case를 넣고 예시와 입력을 분리한다
- [ ] 지시와 예시가 모순되면 결과는 예측 불가다 (precedence 없음)
- [ ] 강조, 반복, temperature 조정, 큰 모델은 신뢰성 해법이 아니다
- [ ] 스키마 보장 JSON = structured outputs(`output_config.format`). prefill은 Claude 4.6부터 400 error
- [ ] 프로덕션 추출 = tool use 스키마 + 검증 + error를 붙여 retry (빈 객체나 regex로 땜질하지 않기)
- [ ] 긴 문서는 위, 질문은 끝 (최대 30% 향상) + 먼저 인용하게 하기
- [ ] 여러 문서는 `<document>` + `<source>`로 하나씩 감싼다. effort, cache, 사전 요약은 구조를 고치지 못한다
- [ ] 컨텍스트는 예산이다. 불필요한 자료는 정확도도 떨어뜨린다 (context rot)
- [ ] drift/bloat에는 prune, compact(오래된 턴 요약, 최근 턴 유지), isolate(subagent/세션 분리). `max_tokens`와 큰 window는 해법이 아니다
