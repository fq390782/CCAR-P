# 1. Agents and Workflows — 반드시 알아야 할 지식
> 시험 비중 15% · 약 4문항 · 근거 문항 27개

## 1. 핵심 개념

### 1.1 Workflow vs Agent — 구분 기준은 "다음 단계를 누가 정하나"
- **Workflow**: LLM과 tool을 미리 정의한 코드 경로(predefined code path)로 엮은 시스템. control flow가 설계 시점에 고정되고, 모델은 정해진 지점에서만 호출된다. [Amey-0074] [Udemy-0053]
- **Agent**: 모델이 실행 중에 다음 단계와 tool 사용법을 스스로 정하는 시스템. [Amey-0074] [Udemy-0053]
- 길이, tool 개수, structured output 필요 여부, "workflow는 모델을 못 부른다", "agent는 tool을 못 쓴다"는 구분 기준이 아니다. workflow도 모델을 호출하고 agent도 tool을 쓴다. [Amey-0074] [Amey-0024]
- Agent가 정말 필요한 신호는 단 하나: **중간 결과를 보기 전에는 필요한 단계를 알 수 없는 경우**(경로를 실행 중에 발견해야 함). [Amey-0024] [Patrick-0022] [Udemy-0053]
- 경로가 고정이면 결정론적 orchestration이 더 싸고, 빠르고, 테스트·감사·디버깅이 쉽다. agent는 비용, 지연, 비결정성, 오류 연쇄 위험만 늘린다. [Amey-0004] [Amey-0023] [Amey-0040] [Patrick-0012] [Udemy-0053]
- 판단 순서: "복잡한가 / 경로가 알려져 있나 / 코드로 싸게 오류를 막을 수 있나"를 먼저 묻고, 요구를 만족하는 **가장 단순한 구성**을 고른다. 매핑이 고정된 변환이면 agent loop 없이 deterministic script, 해석이 필요한 필드가 있으면 schema를 둔 단일 모델 호출이면 된다. [Preporato-0016] [Udemy-0053] [Udemy-0014]

![Workflow와 agent를 다음 단계 결정 주체로 비교한 흐름도](svg/1-workflow-vs-agent.svg)
*그림: 중간 결과를 봐야 다음 단계를 알 수 있을 때만 agent이고, 경로가 고정이면 코드가 순서를 정하는 workflow가 맞다*

### 1.2 Workflow 패턴 구분 — "분해 내용을 누가, 언제 정하나"
- **prompt chaining**: 고정된 subtask를 순서대로 호출하고 각 단계가 앞 단계 출력을 받는다. 호출 순서는 앱 코드가 정한다. 단계 사이에 programmatic gate(schema 검증, 필수 항목 검사)를 끼울 수 있다. 지연은 조금 늘지만 정확도와 예측 가능성이 오른다. [Patrick-0012] [Patrick-0022] [Udemy-0053]
- **routing**: 입력을 분류해 전용 후속 처리로 보내고 끝난다. 분해나 결과 통합은 하지 않는다. [Udemy-0006]
- **parallelization (voting)**: 같은 작업을 여러 번 돌려 다수결 등으로 확신도를 높인다. 작업 분해가 아니다. [Udemy-0006]
- **orchestrator-workers**: 중심 LLM이 입력을 보고 그 자리에서 subtask를 정해 worker LLM에 위임하고 결과를 통합한다. subtask가 사전 정의되지 않는다는 점이 결정적 차이이며, 입력마다 분해가 달라지는 작업에 쓴다. [Udemy-0006] [Patrick-0022] [Udemy-0053]
- **evaluator-optimizer**: 평가자 LLM이 채점하고 기준을 넘을 때까지 생성과 수정을 반복한다. 명확한 평가 기준이 있고 하나의 출력을 다듬는 작업(번역 퇴고 등)에 맞는다. 서로 다른 단계를 순서대로 처리하는 일에는 맞지 않는다. [Udemy-0053]
- 단계 사이에 checkpoint가 필요하면 "하나의 거대한 prompt에 전부 요청"은 오답이다. 검증 지점이 사라진다. [Amey-0023] [Patrick-0012] [Patrick-0022]

![5가지 workflow 패턴의 흐름 비교](svg/1-workflow-patterns.svg)
*그림: 패턴은 분해를 코드가 미리 정하는지(chaining, routing, voting), 실행 중에 LLM이 정하는지(orchestrator-workers), 기준 통과까지 반복하는지(evaluator-optimizer)로 갈린다*

### 1.3 Coordinator(orchestrator) 1개 + Subagent n개 구조
**Coordinator의 역할**
- 작업 분해: 입력에 맞춰 subtask를 정한다. [Udemy-0006]
- 위임: 독립적이고 자기완결적인 subtask를 subagent에 넘기고, 독립적이면 병렬로 실행한다. [Preporato-0019] [Amey-0041]
- 결과 통합: subagent의 compact한 요약을 모아 최종 결과(비교, 계획 등)를 만든다. 또 실패를 격리한다. [Preporato-0019] [Udemy-0006]

**Subagent의 역할**
- 격리된 컨텍스트: 부모와 별도의 대화 컨텍스트에서 돈다. 자료 읽기와 중간 tool 호출·결과는 subagent 안에만 남는다. [Udemy-0004] [Amey-0041]
- 좁은 범위: 자기완결적인 subtask 하나(PDF 한 개 요약, 검사 항목 하나 등)만 맡는다. [Preporato-0019] [Udemy-0004]
- 요약 반환: 최종 메시지만 Agent tool의 결과로 부모에게 돌아간다. 그래서 부모의 context window가 장황한 중간 결과로 차지 않는다. 이것이 subagent의 주된 구조적 가치다. [Udemy-0004] [Amey-0041] [Preporato-0019]

![Coordinator 1개와 subagent 3개의 위임과 반환 흐름](svg/1-coordinator-subagents.svg)
*그림: coordinator는 위임 prompt를 내려보내고, 자료와 중간 tool 결과는 각 subagent 안에 남으며 요약만 올라온다*

**Coordinator → Subagent로 넘길 것 / 넘어가지 않는 것**
- 넘길 것: 위임 prompt 안에 subtask에 필요한 컨텍스트(file path, 판단 근거, 이전 결정 등)를 **명시적으로** 적는다. 부모에서 subagent로 가는 것은 Agent tool의 prompt 문자열과 subagent 자신의 정의(`AgentDefinition`의 `prompt`)뿐이다. [Udemy-0004] [Amey-0025]
- 자동으로 넘어가지 않는 것: 부모의 대화 이력, tool 결과, 부모의 system prompt. 일반 subagent는 빈 컨텍스트에서 시작한다(부모 이력을 이어받는 것은 현재 대화를 분기하는 fork형 subagent뿐). [Udemy-0004]
- 공통 방침을 모든 subagent에 지키게 하려면 각 subagent 정의나, 설정에 따라 로드되는 프로젝트 `CLAUDE.md`에 적는다. [Udemy-0004]
- subagent를 넣었더니 품질이 떨어졌다면 가장 유력한 원인은 handoff에서 필요한 컨텍스트가 빠진 것이다. 위임은 컨텍스트를 내주고 격리를 얻는 거래다. 더 큰 모델이나 subagent 추가로는 해결되지 않는다. [Amey-0025]

**Subagent → Coordinator로 돌려줄 것 / 돌려주지 말 것**
- 돌려줄 것: compact한 요약과 결론. [Preporato-0019] [Udemy-0004]
- 돌려주지 말 것: 원문 자료, 중간 tool 출력. 그대로 돌려주면 격리하는 의미가 없어진다. [Amey-0041] [Udemy-0004]

![Agent tool 경계를 넘는 것과 넘지 않는 것](svg/1-handoff-boundary.svg)
*그림: 부모 이력·tool 결과·system prompt는 넘어가지 않고 위임 prompt에 명시한 것만 넘어가며, 돌아오는 것은 요약뿐이다*

**구조상 주의점**
- subagent끼리 직접 결과를 주고받는 구조는 결과를 합치고 실패를 격리하는 coordinator를 없애므로 오답이다. [Preporato-0019]
- 컨텍스트를 격리해도 **총 토큰은 줄지 않는다.** subagent마다 자료를 따로 읽고 API를 따로 호출하므로 오히려 늘 수 있다. 비용을 줄이려면 subagent별로 `model`에 가벼운 모델을 지정하는 식의 별도 수단을 쓴다. [Udemy-0004]
- subagent의 올바른 용도가 아닌 것: 합의를 위해 같은 prompt를 두 번 실행하기, rate limit 우회, 메인 모델 장애 대비 fallback. [Amey-0041]

**단일 agent나 workflow가 더 나은 경우**
- 단계가 고정되어 있으면 subagent도 orchestrator도 쓰지 않는다. 동적으로 분해할 것이 없다. [Patrick-0012] [Amey-0023] [Amey-0004]
- supervision hierarchy는 위임이 필요한 문제를 위한 것이다. 고정된 몇 단계에는 쓰지 않는다. [Amey-0004]
- subagent 수를 늘리면 handoff 결함도 그만큼 늘어난다. [Amey-0025]

### 1.4 Agentic loop (Messages API를 직접 다룰 때)
- `stop_reason: "tool_use"`가 오면 요청된 tool을 실행하고, 대화에 `tool_result`를 붙인 뒤 API를 다시 호출한다. 모델은 tool 결과를 기다리는 중이다. [Amey-0005] [Udemy-0019]
- `stop_reason: "end_turn"`이고 `tool_use` block이 없으면 턴이 끝난 것이므로 content를 호출자에게 반환한다. [Amey-0036] [Patrick-0038]
- `stop_reason`이 `tool_use`가 아니면 loop를 빠져나간다. `max_tokens` 같은 값은 별도로 처리해야 한다. 응답에 text block이 있다는 사실만으로는 종료 신호가 아니다. text와 tool 호출이 함께 올 수 있다. [Patrick-0038]
  - ⚠️ 공식 문서에는 server tool 사용 중에 `pause_turn`도 온다. 이때는 종료가 아니라 응답을 그대로 다시 보내 이어가야 하므로 "`tool_use`가 아니면 무조건 종료"는 지나치게 단순화한 규칙이다. [Patrick-0038]
- `max_tokens`는 **출력** 길이 제한이다. tool dispatch와도, 입력 컨텍스트 부족과도 관계가 없다. [Amey-0005] [Preporato-0019]

![stop_reason별 agentic loop 분기](svg/1-agentic-loop.svg)
*그림: tool_use와 pause_turn은 다시 API를 호출해 loop를 잇고, end_turn은 반환, max_tokens는 별도 처리한다*

### 1.5 Loop 종료, 안전장치, 상태
- 종료 조건은 명시적인 success condition(정상 종료)과 hard step ceiling(안전망)의 조합이다. [Amey-0060] [Patrick-0038]
  - ⚠️ 공식 agentic loop 예제는 `stop_reason == "end_turn"`(모델이 끝났다고 판단한 것)으로 종료한다. Amey-0060의 해설은 "모델의 판단만으로는 보장되지 않는다"며 앱 수준의 success condition을 강조한다. 시험에서는 "success condition + ceiling" 보기를 고르되, `end_turn` 처리도 함께 알아 둔다. [Amey-0060] [Amey-0036]
- step limit을 두는 주된 이유는 agent가 수렴하지 못할 때 피해와 비용을 묶어 두는 것이다. 성공한 실행의 비용 절감, 속도, prompt 단순화가 목적이 아니다. [Amey-0026]
- 고정 반복 횟수, wall-clock timeout만 쓰는 방식, 컨텍스트 소진은 올바른 종료 조건이 아니다. 컨텍스트 소진은 실패다. [Amey-0060] [Patrick-0038]

![success condition과 hard step ceiling으로 이루어진 loop 종료 흐름](svg/1-loop-termination.svg)
*그림: loop는 success condition으로 정상 종료하고, 수렴하지 못하면 hard ceiling이 안전망으로 끊는다*

- 오래 실행되는 agent가 이전 결정을 유지해야 하면 compaction과 무관하게 전달되는 **명시적 state**에 기록한다. context window는 유한하고 compaction은 정보를 잃는다. [Amey-0073]

![context window와 명시적 state의 결정 유지 비교](svg/1-explicit-state.svg)
*그림: context window에만 둔 결정은 compaction과 재시작으로 사라지고, 명시적 state에 둔 결정은 유지된다*

### 1.6 Tool 설계
- 목적이 겹치는 tool이 있으면 선택이 모호해져 잘못된 tool을 고르는 일이 잦아진다. 속도, 비용, 오류 처리 면에서도 이득이 없다. [Amey-0059]

### 1.7 구현 수단 비교: Client SDK / Agent SDK / Managed Agents / 프레임워크
- **Client SDK (Messages API 직접 호출)**: `tool_use`를 받아 tool을 실행하고 `tool_result`를 보내는 loop와 tool 구현을 개발자가 맡는다. loop는 beta tool runner에 맡길 수도 있다. streaming(`messages.stream()`, `stream: true`)과 tool use 자체는 여기서도 되므로 Agent SDK만의 장점이 아니다. [Udemy-0019]
- **Claude Agent SDK**: Claude Code를 움직이는 것과 같은 harness를 Python/TypeScript 라이브러리로 제공한다. agent loop, built-in tool(파일 Read/Edit, Bash 명령 실행, 검색), context management, hooks와 permissions(결정론적 제어), subagents, MCP, sessions를 포함한다. loop와 tool을 직접 만들고 싶지 않을 때 쓴다. [Patrick-0039] [Preporato-0017] [Udemy-0019]
  - Agent SDK가 **제공하지 않는 것**: hosted vector DB, 자동 fine-tuning, 시각적 drag-and-drop designer, Anthropic 인프라 호스팅. [Preporato-0017] [Udemy-0019]
  - 사용자가 운영하는 프로세스 안에서 돌기 때문에 tool은 자사 인프라의 파일과 명령을 직접 다룬다. 세션은 실행 머신 디스크에 JSONL로 저장되며 `SessionStore` adapter로 자사 스토리지에 둘 수 있다. [Udemy-0051]
  - 인증은 API key를 쓴다. 사전 승인 없이 제3자 제품에 claude.ai 로그인이나 그 rate limit을 제공할 수 없다. [Udemy-0019]
- **Managed Agents**: Anthropic이 agent loop와 sandbox를 호스팅한다. 실행 기반 없이 빨리 production에 가거나 장시간 비동기 작업을 돌릴 때 맞다. sandbox는 Anthropic cloud와 self-hosted 중 고를 수 있지만, 어느 쪽이든 **session과 event log는 Anthropic 쪽에 저장된다.** [Udemy-0019] [Udemy-0051] [Preporato-0018]
- **Message Batches API**: 즉시성이 필요 없는 대량 요청을 비동기로 싸게 처리한다. agent loop나 세션 저장소가 아니다. [Patrick-0039] [Udemy-0051]
- token counting endpoint는 크기를 추정할 뿐이고 계획을 세우지 않는다. tool을 prompt에 설명만 해서는 실행되지 않는다. [Patrick-0039]
- **LangGraph 같은 orchestration 프레임워크**: 장시간 실행되는 stateful agent를 위한 저수준 프레임워크다. durable execution(장애 후 재개), human-in-the-loop, state 영속화를 직접 만들지 않아도 되며 control flow는 graph(node/edge)로 명시적으로 설계한다. prompt와 아키텍처를 추상화하지 않는다. 비용 절감 도구가 아니다. 요구가 이 기능들과 맞고 내부 동작을 이해할 수 있을 때만 쓴다. 단순한 agent라면 API를 직접 쓰는 편이 낫다(Anthropic은 단순한 구현부터 시작하라고 권한다). [Udemy-0014] [Preporato-0016]

![구현 수단 선택 decision tree](svg/1-implementation-choice.svg)
*그림: 요구 조건을 위에서부터 확인해 Batches, LangGraph, self-hosted Agent SDK, Managed Agents, Agent SDK, Client SDK 중 가장 단순한 것을 고른다*

### 1.8 Deployment 선택 — 3축으로 확인
- "loop를 누가 돌리나 / tool은 어디서 실행되나 / state(대화 로그)는 어디에 남나"를 따로 확인한다. [Udemy-0051]
- data residency 때문에 실행과 데이터, 세션 로그까지 자사 네트워크에 둬야 하면 self-hosted(Agent SDK)를 쓴다. production 출시 속도가 우선이면 managed를 쓴다. [Preporato-0018] [Udemy-0051]

![loop, tool 실행, state 위치로 본 deployment 비교](svg/1-deployment-axes.svg)
*그림: Managed Agents는 sandbox를 자사에 두어도 session과 event log가 Anthropic에 남으므로 residency 요구에는 self-hosted Agent SDK다*

## 2. 상황별 정답 판단 규칙

| 이런 상황이면 | 정답 방향 | 근거 |
|---|---|---|
| 단계가 고정이고, 순서가 같고, 모든 입력에서 동일하다 | 결정론적 workflow (prompt chaining). 모델은 필요한 지점에서만 호출 | Amey-0004, Amey-0023, Amey-0040, Patrick-0012, Patrick-0022, Udemy-0053 |
| 고정 단계 사이에 검증이 필요하다 | 단계 사이에 programmatic validation gate(schema check) | Patrick-0012, Patrick-0022, Udemy-0053 |
| 매핑이 고정된 형식 변환 | deterministic script, 해석이 필요하면 schema를 둔 단일 호출. agent loop 없음 | Preporato-0016 |
| 중간 결과를 봐야 다음 단계가 정해진다 | agent | Amey-0024 |
| 입력마다 필요한 조사나 subtask가 달라지고 결과를 하나로 합쳐야 한다 | orchestrator-workers (manager가 동적으로 분해·위임·통합) | Udemy-0006 |
| 입력 유형별로 다른 처리로 보내기만 하면 된다 | routing | Udemy-0006 |
| 같은 작업을 여러 관점으로 돌려 확신도를 높이고 싶다 | parallelization (voting) | Udemy-0006 |
| 명확한 평가 기준이 있고 하나의 출력을 반복 개선한다 | evaluator-optimizer | Udemy-0053 |
| 독립 문서 여러 개를 처리하다 단일 agent의 컨텍스트가 넘친다 | orchestrator가 문서별 subagent를 병렬 실행하고 요약만 받아 통합 | Preporato-0019 |
| 대량 자료를 읽는 전문 검사를 위임하고 부모 컨텍스트는 보호하고 싶다 | subagent로 격리. 부모에게는 최종 결과만 | Udemy-0004, Amey-0041 |
| subagent를 도입한 뒤 품질이 떨어졌다 | handoff prompt에 빠진 컨텍스트를 명시적으로 넣는다 | Amey-0025 |
| `stop_reason: "tool_use"` | tool 실행 → `tool_result` 추가 → API 재호출 | Amey-0005 |
| `stop_reason: "end_turn"`이고 `tool_use` 없음 | 턴 완료, content 반환 | Amey-0036, Patrick-0038 |
| loop를 언제 멈출지 묻는다 | success condition(또는 `tool_use`가 아님) + 최대 반복 cap | Amey-0060, Patrick-0038 |
| step limit을 두는 이유를 묻는다 | 수렴하지 못할 때 피해와 비용을 제한 | Amey-0026 |
| 오래전 결정을 유지해야 한다 | compaction과 무관한 명시적 state | Amey-0073 |
| tool 목적이 겹친다 | 잘못된 tool 선택이 늘어난다 → 겹침 제거 | Amey-0059 |
| 파일, shell, context 관리, permission까지 갖춘 agent를 loop 구현 없이 만들고 싶다 | Claude Agent SDK | Patrick-0039, Preporato-0017, Udemy-0019 |
| 인프라 운영 없이 가장 빨리 production에 가고 싶다 | Managed Agents (managed) | Preporato-0018, Udemy-0019 |
| 실행 환경과 세션 로그를 모두 자사 인프라에 둬야 한다 | Agent SDK를 자사 프로세스에서 실행 (self-hosted) | Udemy-0051, Preporato-0018 |
| durable execution, human-in-the-loop, state 영속화가 필요한 장시간 agent | LangGraph 같은 orchestration 프레임워크 | Udemy-0014 |
| 실시간성이 필요 없는 대량 일괄 처리 | Message Batches API (agent 용도 아님) | Udemy-0051, Patrick-0039 |

![2장 규칙의 workflow 패턴과 agent 선택 decision tree](svg/1-rule-architecture-tree.svg)
*그림: 고정 단계부터 확인하고, agent는 중간 결과를 봐야 다음 단계가 정해질 때만 고른다*

![2장 규칙의 컨텍스트·subagent·state·tool 문제 진단](svg/1-rule-context-tree.svg)
*그림: 컨텍스트 문제마다 정답(격리, handoff 보강, 명시적 state, 겹침 제거)과 흔한 오답이 짝을 이룬다*

## 3. 자주 나오는 오답 함정
- "agent가 fixed code보다 더 유능하거나 고품질이다" → 경로가 알려진 작업에서 자율성은 비용과 비결정성만 늘린다. [Amey-0004] [Patrick-0022]
- "agent는 필요 없는 단계를 건너뛸 수 있다" → validation을 건너뛰는 것은 기능이 아니라 결함이다. [Amey-0004]
- "작업이 길다, tool이 많다, structured output이 필요하다 → agent" → 모두 고정 workflow로 충족된다. [Amey-0024]
- "고정 단계에 orchestrator-workers나 단계별 agent를 둔다" → 동적으로 분해할 것이 없다. manager 호출만큼 비용과 불확실성이 늘어난다. [Patrick-0012] [Udemy-0053] [Amey-0023]
- "고정 단계를 evaluator-optimizer로 돌린다" → 반복 횟수를 알 수 없어 시간과 비용이 불안정하다. 하나의 출력을 다듬는 구조도 아니다. [Udemy-0053]
- "하나의 거대한 prompt로 전부 처리한다" → 단계 사이의 checkpoint와 검증이 사라진다. [Amey-0023] [Patrick-0022]
- "서로 감독하는 agent 두 개" → supervision hierarchy는 위임이 필요한 문제에만 쓴다. [Amey-0004]
- "subagent는 부모의 대화 이력이나 system prompt를 물려받으므로 지시를 짧게 써도 된다" → 그런 동작은 fork형뿐이다. 일반 subagent는 빈 컨텍스트에서 시작한다. [Udemy-0004]
- "context 격리로 시스템 전체 토큰이 줄어든다" → 각자 따로 읽으므로 오히려 늘 수 있다. 격리의 이점은 부모 컨텍스트 보호다. [Udemy-0004]
- "subagent 품질 저하 → 더 큰 모델 또는 subagent 추가" → 빠진 컨텍스트는 모델 크기로 채워지지 않는다. subagent를 늘리면 결함도 늘어난다. [Amey-0025]
- "subagent로 합의, rate limit 우회, fallback" → subagent의 가치는 위임과 컨텍스트 격리다. [Amey-0041]
- "subagent끼리 직접 통신" → 결과를 통합하고 실패를 격리하는 coordinator가 사라진다. [Preporato-0019]
- "컨텍스트 부족 → `max_tokens` 상향" → `max_tokens`는 출력 제한이고 문제는 입력이다. [Preporato-0019] [Amey-0005]
- "`tool_use`인데 같은 요청을 다시 보내거나 턴을 끝낸다" → 모델은 tool 결과를 기다리고 있다. [Amey-0005]
- "`end_turn`인데 마지막 tool을 다시 실행하거나 빈 `tool_result`를 보낸다" → 이미 완료된 턴이다. [Amey-0036]
- "응답에 text가 있으면 종료" 또는 "정확히 N회 반복 후 종료" → text와 tool 호출은 공존할 수 있고, 고정 횟수는 모델 신호를 무시한다. [Patrick-0038]
- "step limit의 목적은 성공한 실행의 비용 절감이나 속도" → 비수렴(무한 loop)을 막는 안전 상한이다. [Amey-0026]
- "context window가 기억해 줄 것이다" 또는 "주기적으로 재시작" → 컨텍스트는 유한하고 compaction은 손실이 있으며, 재시작하면 결정이 사라진다. [Amey-0073]
- "tool이 많을수록 빠르고 싸다" → 겹치는 tool은 선택 오류를 늘린다. [Amey-0059]
- "Agent SDK의 장점은 streaming이다" → streaming은 Client SDK에서도 된다. [Udemy-0019]
- "Agent SDK로 Anthropic 인프라에 호스팅한다" → 그것은 Managed Agents다. Agent SDK는 사용자 프로세스에서 돈다. [Udemy-0019]
- "Agent SDK 제품을 claude.ai 로그인으로 쓴다" → API key 인증이 필요하다. [Udemy-0019]
- "Agent SDK는 vector DB, fine-tuning, 시각 designer를 제공한다" → 제공하지 않는다. [Preporato-0017]
- "Managed Agents에 self-hosted sandbox를 쓰면 세션 로그도 자사에 남는다" → session과 event log는 Anthropic 쪽에 저장된다. [Udemy-0051]
- "Message Batches API로 agent를 돌린다" → 비동기 일괄 요청용이며 loop나 세션을 제공하지 않는다. [Udemy-0051] [Patrick-0039]
- "LangGraph를 쓰면 호출과 토큰이 줄어든다" 또는 "prompt와 구성을 직접 안 써도 된다" → 비용 절감 도구가 아니며, 저수준이라 구성은 개발자가 설계한다. [Udemy-0014]
- "장시간 승인 대기 state를 프로세스 메모리에 둔다" → 장애나 재시작 때 사라져 재개할 수 없다. [Udemy-0014]

## 4. 암기 목록

| 이름/숫자/파라미터 | 의미 |
|---|---|
| `stop_reason: "tool_use"` | tool 실행 → `tool_result` 추가 → 재호출 (loop 계속) [Amey-0005] |
| `stop_reason: "end_turn"` | 모델이 턴 종료. 결과 반환 [Amey-0036] |
| `stop_reason: "max_tokens"` | 출력 상한 도달. 별도 처리 필요 (종료 신호로 보지 않음) [Patrick-0038] |
| `max_tokens` | 출력 길이 제한. 입력 컨텍스트와 무관 [Preporato-0019] |
| `tool_result` | tool 실행 결과를 대화에 붙여 돌려주는 block [Udemy-0019] |
| step ceiling / max iteration cap | 비수렴 loop에 대한 안전 상한 [Amey-0026] [Patrick-0038] |
| prompt chaining | 고정 순서 + 단계 사이 gate [Udemy-0053] |
| routing | 분류 후 전용 처리로 보냄 [Udemy-0006] |
| parallelization (voting) | 같은 작업을 여러 번 실행, 다수결 [Udemy-0006] |
| orchestrator-workers | 실행 중 동적 분해 → 위임 → 통합 [Udemy-0006] |
| evaluator-optimizer | 채점 → 수정 반복 [Udemy-0053] |
| Agent tool | subagent 호출. 부모에게는 최종 메시지만 반환 [Udemy-0004] |
| `AgentDefinition`의 `prompt` | subagent 자신의 system prompt (부모 system prompt는 상속 안 됨) [Udemy-0004] |
| `model` (subagent 정의) | subagent별로 가벼운 모델을 지정해 비용 절감 [Udemy-0004] |
| fork형 subagent | 현재 대화를 분기해 부모 이력을 이어받는 예외 [Udemy-0004] |
| `CLAUDE.md` | 설정에 따라 로드되는 프로젝트 공통 방침 [Udemy-0004] |
| Claude Agent SDK | loop + built-in tools(Read/Edit/Bash/검색) + context mgmt + hooks/permissions + subagents/MCP/sessions, 자사 프로세스에서 실행 [Preporato-0017] [Udemy-0019] |
| tool runner (beta) | Client SDK에서 tool loop를 대신 돌려 줌 [Udemy-0019] |
| Managed Agents | Anthropic이 loop와 sandbox를 호스팅. session/event log는 Anthropic 측 저장 [Udemy-0051] |
| 세션 JSONL / `SessionStore` | Agent SDK 세션 저장 (디스크, 자사 스토리지 adapter) [Udemy-0051] |
| Message Batches API | 비동기 대량 처리. agent 용도 아님 [Udemy-0051] |
| LangGraph | 저수준 stateful orchestration: durable execution, human-in-the-loop, state 영속화 [Udemy-0014] |

## 5. 시험 직전 체크리스트
- [ ] Workflow와 agent의 차이는 "다음 단계를 코드가 정하나, 모델이 정하나"다.
- [ ] 단계가 고정이면 prompt chaining과 validation gate를 쓰고 agent/orchestrator는 오답이다.
- [ ] Agent가 필요한 신호는 "중간 결과를 봐야 다음 단계를 알 수 있음" 하나뿐이다.
- [ ] 동적 분해 → 위임 → 통합은 orchestrator-workers, 분류만 하면 routing, 다수결은 voting이다.
- [ ] Coordinator는 분해, 위임, 통합을 맡고 subagent는 격리된 컨텍스트에서 좁은 작업을 하고 요약만 반환한다.
- [ ] Subagent는 부모의 이력과 system prompt를 물려받지 않으므로 필요한 컨텍스트를 위임 prompt에 명시한다.
- [ ] Subagent 도입 후 품질이 떨어지면 handoff에서 빠진 컨텍스트를 의심한다.
- [ ] Context 격리는 부모 window를 보호할 뿐 총 토큰을 줄이지 않는다.
- [ ] `tool_use`이면 실행, `tool_result`, 재호출 / `end_turn`이면 반환한다.
- [ ] Loop 종료는 success condition과 step ceiling의 조합이다. ceiling은 비수렴 대비용이다.
- [ ] `max_tokens`는 출력 제한이며 컨텍스트 부족의 해법이 아니다.
- [ ] 오래 유지할 결정은 compaction과 무관한 명시적 state에 둔다.
- [ ] 겹치는 tool은 잘못된 tool 선택을 늘린다.
- [ ] Agent SDK는 loop, built-in tools, context, hooks/permissions를 제공하고 자사 프로세스에서 돌며 API key로 인증한다.
- [ ] Managed Agents는 Anthropic이 호스팅하고 세션 로그도 Anthropic에 남는다. 데이터 residency가 요구되면 Agent SDK(self-hosted)다.
