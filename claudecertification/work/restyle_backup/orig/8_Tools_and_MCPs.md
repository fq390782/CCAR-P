# 8. Tools and MCPs — 반드시 알아야 할 지식
> 시험 비중 10% · 약 3문항 · 근거 문항 21개

## 1. 핵심 개념

### 1-1. tool_use ↔ tool_result 왕복 (client tools)
- Claude가 tool을 쓰기로 하면 응답이 `stop_reason: tool_use`로 끝나고, content에 `tool_use` 블록(id, name, input)이 담겨 옵니다. 실행은 앱이 합니다. [Patrick-0002] [Udemy-0013]
- 다음 요청에는 ① `tool_use` 블록이 든 assistant 턴을 그대로 붙이고 ② 이어서 **user** 역할 메시지에 `tool_result` 블록을 넣습니다. 각 `tool_result`는 같은 `tool_use_id`로 짝을 맞춥니다. [Patrick-0002] [Patrick-0017]
- Messages API는 stateless라서 모델이 "기억"하지 않습니다. assistant 턴을 빼거나 id를 빼면 graceful recovery가 아니라 에러가 납니다. [Patrick-0017] [Udemy-0016]
- tool 결과를 보내는 전용 SDK 메서드(예: `submit_result()`)는 없습니다. system 메시지나 assistant 메시지로 보내는 것도 아닙니다. [Patrick-0002]

![tool_use와 tool_result 왕복 sequence](svg/8-tool-use-roundtrip.svg)
*그림: 앱이 tool_use를 실행하고, 다음 요청에서 assistant 턴을 그대로 둔 채 user 메시지의 tool_result(같은 tool_use_id)로 결과를 돌려줍니다.*

### 1-2. Parallel tool use
- 한 assistant 턴에 `tool_use` 블록이 여러 개 올 수 있습니다(기본 동작). 모두 실행한 뒤 모든 `tool_result`를 **한 user 메시지**에 담아 돌려줍니다. [Patrick-0018]
- 결과를 여러 메시지로 나눠 보내면 모델이 병렬 호출을 덜 하게 되어 나중에 latency가 늘어납니다. 한 턴에 호출 하나로 제한하려면 `disable_parallel_tool_use`를 씁니다. [Patrick-0018]

![병렬 tool use 결과 반환 방식 비교](svg/8-parallel-tool-use.svg)
*그림: 여러 tool_use의 결과는 한 user 메시지에 모아 돌려주고, 메시지를 나누면 이후 병렬 호출이 줄어듭니다.*

### 1-3. Tool 에러 처리
- tool이 실패하면 에러 내용을 content에 넣고 `is_error: true`를 붙인 `tool_result`로 모델에 돌려줍니다. 그러면 모델이 인자를 고치거나, 다른 방법을 고르거나, 사용자에게 설명할 수 있습니다. [Amey-0032] [Udemy-0036]
- 무엇이 일어났고 다음에 무엇을 시도할지 구체적으로 적어 주면 모델이 추측 없이 회복합니다. [Udemy-0036]
- 실패를 빈 결과로 위장하면 안 됩니다. 모델이 "해당 데이터 없음"으로 오해합니다(예: 알레르겐 없음으로 착각). 빈 `tool_result`는 결과가 정말 없을 때만 씁니다. [Udemy-0036]
- 같은 호출을 무한 재시도하거나, raw 에러를 최종 사용자에게 보여 주거나, 실행 전체를 중단하는 것은 오답입니다. 일시적 장애에 대한 제한된 재시도와 복구 불가능한 장애(예: 인증 만료) 시 중단은 상황에 따라 맞을 수 있습니다. [Amey-0032] [Udemy-0036]
- `is_error`는 호출 **뒤의** 회복 수단입니다. 잘못된 tool 선택 자체를 막지는 못하고, 되돌리기 어려운 작업(예약 확정·취소)은 호출되는 순간 영향이 생깁니다. [Udemy-0045] [Udemy-0025]

![tool 실패 시 처리 방식 분기](svg/8-tool-error-is-error.svg)
*그림: 실패는 is_error: true인 tool_result로 알려야 모델이 회복하며, 빈 결과·무한 재시도·raw 에러 노출·대화 종료는 오답입니다.*

### 1-4. tool_choice
- `auto`(기본값, 호출 여부를 모델이 판단), `any`(어떤 tool이든 반드시 사용), `tool`(지정한 tool을 반드시 사용), `none`(tool 사용 안 함). [Udemy-0036]
- "답하기 전에 반드시 특정 tool을 호출"이 요구되면 지원 모델에서는 `tool_choice`로 그 tool을 지정합니다. `auto`로는 보장되지 않습니다. [Udemy-0036]
- 일부 신규 모델(Claude Opus 5.5, Claude Fable 5.1 등)은 `any`/`tool`에 400을 반환합니다. 이때는 `auto` + 프롬프트 지시 + strict tool use를 조합합니다. 이 변경은 시험 가이드(2026년 7월판)보다 새로우므로 시험에서는 강제가 된다는 전제로 나올 수 있습니다. [Udemy-0036]
- `tool_choice: auto`는 기본값이라 설정해도 아무것도 바뀌지 않습니다. 입력 형식 문제를 해결하지 못합니다. [Preporato-0025]

![tool_choice 옵션 비교와 강제 호출 판단](svg/8-tool-choice.svg)
*그림: 특정 tool을 반드시 호출해야 하면 tool_choice로 지정하고, any/tool을 지원하지 않는 모델은 auto + 프롬프트 + strict로 대신합니다.*

### 1-5. Strict tool use (입력 스키마 보장)
- tool 정의에 `strict: true`를 두면 tool 입력이 `input_schema`를 따르도록 스키마 검증이 걸립니다. 타입 오류(문자열로 온 숫자)나 필수 필드 누락을 **근원에서** 막습니다. [Preporato-0025]
- 더 긴 description은 tool 선택과 입력 작성에 도움이 되지만 형식을 보장하지는 못합니다. temperature를 낮추는 것도 타입을 보장하지 못합니다. [Preporato-0025]

![strict 유무에 따른 tool 입력 비교](svg/8-strict-tool-use.svg)
*그림: strict: true만 input_schema 검증으로 타입 오류와 필수 필드 누락을 근원에서 막고, description·temperature·auto는 보장하지 못합니다.*

### 1-6. Tool description과 tool surface 설계
- tool을 올바르게 호출하는지는 description과 파라미터 설명이 얼마나 명확한지에 가장 크게 좌우됩니다. description은 모델이 tool을 고르고 쓰는 유일한 근거입니다. [Amey-0030] [Amey-0063] [Udemy-0045]
- 좋은 description에는 ① tool이 하는 일 ② 언제 쓰고 언제 쓰지 말아야 하는지 ③ 각 파라미터의 의미와 영향 ④ 제약(반환하지 않는 정보 등)이 들어갑니다. 공식 권장은 tool 하나당 3~4문장 이상입니다. [Amey-0063] [Udemy-0045]
- 간결함보다 명확함이 우선입니다. 구현 언어나 함수명과 일치하는지는 선택에 도움이 되지 않습니다. [Amey-0063]
- 의미 있는 이름(서비스명 접두어 등)도 도움이 되지만 description을 대신할 수 없습니다. 모든 tool에 같은 범용 설명을 붙이면 구별할 단서가 사라집니다. [Udemy-0045]
- tool끼리 겹쳐서 잘못 고르는 것은 interface 설계 문제입니다. 관련 작업을 통합하고 각 tool의 목적이 뚜렷해지도록 tool surface를 다듬어 해결합니다. "신중히 고르라"는 지시, 더 큰 context window, 정렬 순서로는 해결되지 않습니다. [Amey-0031] [Udemy-0045]
- MCP 서버를 추가한 뒤 성공률이 떨어지면 먼저 새 tool이 기존 tool과 겹치는지, description이 구별되는지를 확인합니다. uptime·latency 문제는 에러나 지연으로 드러나고, 모델은 바뀌지 않았습니다. [Amey-0078]
- tool 개수와 선언 순서는 description보다 영향이 훨씬 작고, JSON 반환 여부는 선택이 아니라 결과 소비에 영향을 줍니다. [Amey-0030]

![tool surface 설계 Before/After](svg/8-tool-surface-design.svg)
*그림: 엉뚱한 tool 선택은 겹치는 tool 통합과 4요소 description으로 고치며, 지시문·context 확장·정렬로는 고쳐지지 않습니다.*

### 1-7. Tool 결과 크기 설계
- 객체가 크고 모델이 다음 호출에만 필요로 한다면 전체 객체 대신 identifier(handle)를 반환해 context를 아낍니다. "항상 전체" 또는 "항상 id만"은 둘 다 틀립니다. 작업에 따라 정합니다. [Amey-0077]

![tool 결과 크기 결정 트리](svg/8-tool-result-size.svg)
*그림: 큰 객체가 다음 호출에만 필요하면 identifier를 반환하고, 아니면 필요한 전체를 반환합니다.*

### 1-8. 워크플로 순서를 코드로 강제 (state machine + tool gating)
- 반드시 지켜야 할 순서(본인 확인 → 정보 수집 → 확인·동의 → 실행)는 프롬프트가 아니라 코드로 보장합니다. 앱이 현재 단계를 상태로 갖고, 그 상태에서 허용되는 tool만 `tools`에 넣습니다. 본인 확인 전 요청에는 변경 tool이 아예 없으므로 호출할 수 없습니다. [Udemy-0016]
- 상태 전환은 본인 확인 tool의 성공처럼 코드로 검증할 수 있는 사실을 기준으로 합니다. 대화의 유연성은 Claude에 맡기고, 깨지면 안 되는 순서만 코드로 강제합니다. [Udemy-0016]
- 대안: tool 정의를 바꾸면 prompt cache 전체가 무효화되므로, 정의는 고정하고 상태에 맞지 않는 호출을 앱이 거부해 에러로 돌려주는 방식도 가능합니다. [Udemy-0016]
- 번호 목록, few-shot, effort 상향, "다음 단계 이름을 JSON으로 출력"은 모두 최종 판단을 모델에 남기므로 확률적일 뿐 보장이 아닙니다. [Udemy-0016]

![state machine과 tool gating 흐름](svg/8-state-machine-gating.svg)
*그림: 앱이 단계를 상태로 갖고 상태별 허용 tool만 tools에 넣어 필수 순서를 코드로 강제합니다.*

### 1-9. Client tools vs Server tools
- tool은 **코드가 실행되는 위치**로 구분합니다. [Udemy-0013]
- Client tools(직접 정의한 tool, 그리고 `bash`·`text_editor`처럼 Anthropic이 스키마를 정한 tool)는 앱에서 실행됩니다. `tool_use`를 받으면 앱이 처리하고 `tool_result`를 돌려줍니다. 사내 인프라 안의 시스템(SIEM 등)에는 client tool로 접근합니다. [Udemy-0013]
- Server tools(`web_search`, `web_fetch`, `code_execution`, `tool_search` 등)는 Anthropic 인프라에서 실행되며 결과가 같은 응답에 바로 들어옵니다. 앱은 실행하지도 않고 `tool_result`를 보내지도 않습니다. [Preporato-0023] [Udemy-0013]
- Server tools도 일반 tool처럼 `tools` 파라미터에 선언하며, MCP 전용도 Batch API 전용도 아니고 일반 요청에서 동작합니다. [Preporato-0023]
- Server tools는 Anthropic이 제공하는 기능일 뿐 사용자가 사내 시스템용으로 정의할 수 없고, 사내 네트워크에도 닿지 않습니다. [Udemy-0013]

![client tools와 server tools 실행 위치 비교](svg/8-client-vs-server-tools.svg)
*그림: client tool은 앱이 실행해 tool_result를 보내고, server tool은 Anthropic 인프라에서 실행되어 결과가 같은 응답에 들어옵니다.*

### 1-10. 확장 수단 선택: MCP server vs Tool vs Skill
- 여러 앱이 같은 기능을 쓰고, 그 기능을 플랫폼 팀이 앱과 독립적으로 유지보수해야 한다면 MCP server입니다. 서버가 tools/resources를 노출하고 여러 client가 붙습니다. [Amey-0009] [Amey-0044]
- MCP server는 Messages API를 대체하지 않고, 모델과 같은 프로세스에서 돌 필요도 없으며, 앱마다 서버 코드를 복사하지도 않습니다(복사본은 서로 어긋납니다). [Amey-0009] [Amey-0044]
- Skill은 지시·템플릿·절차(know-how)를 묶은 것으로, 작업이 일치하면 로드됩니다. 외부 시스템 없이 "절차를 따르게 하기"만 필요하면 Skill입니다(claude.ai, Claude Code, API 공통). [Preporato-0024]
- Tools와 MCP server는 **행동(action)이나 데이터 접근**을 추가합니다. Skill은 live connection을 제공하지 않습니다. [Amey-0009] [Preporato-0024]
- 문서 하나로 충분한 절차에 fine-tuning을 쓰는 것은 과합니다. 데이터를 매일 system prompt에 붙여 넣으면 데이터가 낡고 context를 낭비합니다. [Preporato-0024] [Amey-0009]

![확장 수단 선택 decision tree](svg/8-extension-choice.svg)
*그림: 행동·데이터 접근이 없으면 Skill, 여러 앱이 공유하고 독립 유지보수하면 MCP server, 그 외에는 앱의 tool입니다.*

### 1-11. MCP primitives: tools / resources / prompts
- 세 primitive는 **누가 주도하는지**로 구분합니다. tools는 모델, resources는 앱, prompts는 사용자가 주도합니다. [Udemy-0025]
- **tools**: 모델이 상황에 따라 찾아 호출합니다. [Udemy-0025]
- **resources**: 파일, DB 스키마, 문서 같은 참조 데이터를 URI로 노출하고, 어떤 것을 context에 넣을지는 앱이 정합니다. tool 사양서를 resource로 읽혀도 호출 가능한 tool로 등록되지 않습니다. [Udemy-0025] [Udemy-0011]
- **prompts**: 재사용 가능한 프롬프트 템플릿이며, 사용자가 slash command 등으로 명시적으로 고릅니다. 모델이 자동으로 tool을 찾는 용도가 아닙니다. [Udemy-0025]

![MCP primitives와 주도 주체](svg/8-mcp-primitives.svg)
*그림: tools는 모델이, resources는 앱이, prompts는 사용자가 주도합니다.*

### 1-12. MCP tool discovery (tools/list, tools/call)
- tools capability를 선언한 서버는 client의 `tools/list`에 각 tool의 `name`, `description`, `inputSchema`(JSON Schema)를 돌려줍니다. client는 이를 모델용 tool 정의로 바꿔 전달하므로, 서버에 tool을 추가해도 앱 코드는 그대로 둔 채 모델에 노출됩니다. [Udemy-0025]
- 모델이 고른 tool은 client가 `tools/call`로 실행합니다. 입력 검증 에러는 `isError`가 붙은 tool 실행 에러로 모델에 돌아가 자가 수정에 쓰입니다(발견 수단이 아님). [Udemy-0025]
- 목록이 바뀌면 `listChanged`를 선언한 서버가 `notifications/tools/list_changed`를 보내 client가 다시 가져가게 합니다. [Udemy-0025]
- ⚠️ 해설에 "2026-07-28판 사양은 stateless이며, 연결별로 tool 목록을 바꾸는 것은 금지하되 요청의 인가에 따라 바꾸는 것은 허용"한다는 내용이 있습니다. 공식 MCP 사양으로 확인하지 못했으므로 참고만 하세요. [Udemy-0025]

![MCP tools/list와 tools/call sequence](svg/8-mcp-discovery.svg)
*그림: client가 tools/list로 받은 inputSchema를 모델용 tool 정의로 바꿔 노출하고, 모델이 고른 tool을 tools/call로 실행합니다.*

### 1-13. MCP transport: stdio vs Streamable HTTP
- MCP에서는 host(Claude Code 등)가 서버마다 client를 만들어 연결하고, 통신 경로는 transport 계층이 맡습니다. [Udemy-0033]
- **stdio**: 같은 머신의 프로세스끼리 표준 입출력으로 직접 연결합니다. 네트워크 오버헤드가 없고 로컬 파일·CLI 접근에 맞습니다. 서버를 subprocess로 띄우며 보통 client 하나에 제공합니다. 네트워크 너머로는 통신할 수 없습니다. [Udemy-0033] [Udemy-0011]
- **Streamable HTTP**: client→server HTTP POST와 선택적 Server-Sent Events(SSE)를 씁니다. 원격 서버를 여러 client에 제공할 때 쓰고, Bearer 토큰·API key·커스텀 헤더 같은 표준 HTTP 인증을 지원합니다. 토큰 획득에는 OAuth를 권장합니다. [Udemy-0033]
- 로컬 subprocess 서버에 HTTP를 쓰면 오버헤드와 포트 노출·인증 부담만 늘어납니다. 원격 서버를 각 단말에 배포해 stdio로 돌리면 업데이트와 인증을 중앙에서 관리할 수 없습니다. [Udemy-0033]

![stdio와 Streamable HTTP transport 비교](svg/8-mcp-transport.svg)
*그림: 같은 머신의 subprocess는 stdio, 원격 서버를 여러 client에 제공할 때는 Streamable HTTP를 씁니다.*

### 1-14. MCP connector (Messages API의 `mcp_servers`)
- 앱이 MCP client를 직접 구현하지 않고, 요청의 `mcp_servers`에 서버 접속 정보(`type`, `url`, `name`, 필요하면 `authorization_token`)를 적은 뒤 `tools` 배열의 `mcp_toolset`이 `mcp_server_name`으로 그 서버를 참조합니다. beta 기능이라 beta 헤더가 필요합니다. [Udemy-0011]
- 이렇게 하면 API가 서버에서 tool 목록을 가져와 Claude에 제시하고 호출까지 대신합니다. 응답에 `mcp_tool_use`와 `mcp_tool_result`가 함께 오므로 앱이 다시 `tools/call`을 보내거나 `tool_result`를 돌려줄 필요가 없습니다. 다시 실행하면 쓰기 작업이 중복될 수 있습니다. [Udemy-0011]
- `mcp_toolset`의 `default_config`로 전체 기본값을 정하고 `configs`로 tool별 `enabled`를 덮어씁니다. 쓰기 tool만 `enabled: false`로 두는 denylist로 읽기 전용 어시스턴트를 만들 수 있습니다(allowlist 형태도 가능). [Udemy-0011]
- 제약: MCP 사양 중 **tool 호출만** 지원하며 resources와 prompts는 다룰 수 없습니다. HTTP(Streamable HTTP 또는 SSE)로 공개된 서버만 연결되고, 로컬 stdio 서버는 연결할 수 없습니다. Amazon Bedrock과 Google Cloud(Google managed)에서는 제공되지 않습니다. [Udemy-0011]
- 문서를 읽혀야 한다면 앱이 직접 가져와 메시지에 넣거나, 문서를 돌려주는 tool을 서버에 만듭니다. [Udemy-0011]

![MCP connector 요청과 실행 흐름](svg/8-mcp-connector.svg)
*그림: mcp_servers와 mcp_toolset을 적으면 API가 tool 목록 조회와 호출을 대신하므로 앱은 mcp_tool_use를 다시 실행하지 않습니다.*

## 2. 상황별 정답 판단 규칙

| 이런 상황이면 | 정답 방향 | 근거 |
|---|---|---|
| `stop_reason: tool_use` 뒤에 결과를 보내야 함 | assistant 턴을 그대로 둔 채 user 메시지에 `tool_result`(같은 `tool_use_id`) | [Patrick-0002] [Patrick-0017] |
| 한 턴에 `tool_use`가 여러 개 | 모두 실행하고 `tool_result`를 한 user 메시지에 묶음 | [Patrick-0018] |
| tool 실행이 실패함 | `is_error: true`가 붙은 `tool_result`로 모델에 돌려줌 | [Amey-0032] [Udemy-0036] |
| 답변 전에 반드시 특정 tool을 호출해야 함 | 지원 모델: `tool_choice`로 지정 / 미지원 모델: `auto` + 프롬프트 + strict | [Udemy-0036] |
| tool 입력 타입이 틀리거나 필수 필드가 빠짐 | tool 정의에 `strict: true` | [Preporato-0025] |
| 모델이 엉뚱한 tool을 고름 | description 구체화 + 겹치는 tool 통합·역할 구분 | [Amey-0031] [Udemy-0045] |
| MCP 서버를 추가한 뒤 성공률이 떨어짐 | 새 tool의 중복과 description 구별성부터 확인 | [Amey-0078] |
| tool이 큰 객체를 돌려주는데 다음 호출에만 필요 | identifier(handle)만 반환 | [Amey-0077] |
| 업무 순서를 반드시 지켜야 함(본인 확인 먼저) | 앱 측 state machine으로 상태별 허용 tool만 전달 | [Udemy-0016] |
| 사내망 시스템 조회 + 일반 웹 검색 | 사내 시스템은 client tool, 웹 검색은 server tool(`web_search`) | [Udemy-0013] |
| 여러 앱이 같은 기능 공유 + 독립 유지보수 | MCP server | [Amey-0009] [Amey-0044] |
| 외부 시스템 없이 정해진 절차·템플릿을 따르게 함 | Skill | [Preporato-0024] |
| 서버에 tool을 추가했는데 앱 코드를 바꾸지 않고 노출 | client의 `tools/list` → `inputSchema`로 tool 정의 생성 | [Udemy-0025] |
| 로컬 파일·CLI용 subprocess 서버 | stdio transport | [Udemy-0033] |
| 네트워크로 여러 client에 제공 | Streamable HTTP transport | [Udemy-0033] |
| Messages API에서 원격 MCP 서버를 직접 사용(client 직접 구현 안 함) | `mcp_servers`에 정의 + `tools`의 `mcp_toolset`에서 참조 | [Udemy-0011] |
| MCP connector에서 읽기 전용으로 제한 | `mcp_toolset`의 `configs`로 쓰기 tool `enabled: false` | [Udemy-0011] |

![판단 규칙: tool 호출 결과 처리 decision tree](svg/8-rules-tool-call-handling.svg)
*그림: 실행 주체와 성공 여부에 따라 tool_result 형태가 정해지고, 결과는 모두 한 user 메시지로 돌려줍니다.*

![판단 규칙: 증상별 정답 방향](svg/8-rules-symptom-fix.svg)
*그림: tool 정의·설계 문제는 증상마다 tool_choice, strict, description·통합, identifier, state machine 같은 보장 수단이 정해져 있습니다.*

![판단 규칙: 확장 수단·transport·connector decision tree](svg/8-rules-architecture-tree.svg)
*그림: Skill/tool/MCP server를 먼저 고르고, MCP server는 위치에 따라 stdio/Streamable HTTP, client 미구현이면 MCP connector를 씁니다.*

## 3. 자주 나오는 오답 함정

- tool 결과를 system 프롬프트, system 메시지, assistant 메시지에 넣기 → `tool_result`는 user 메시지에 들어가야 하고, assistant 턴과 `tool_use_id`가 없으면 에러가 납니다. [Patrick-0002] [Patrick-0017]
- "모델이 어떤 tool을 불렀는지 기억한다" → API는 stateless라 assistant 턴을 다시 보내야 합니다. [Patrick-0017]
- 대화를 요약해 새로 시작하기 → `tool_use`/`tool_result` 짝이 끊어집니다. [Patrick-0017]
- 병렬 `tool_result`를 메시지 여러 개로 나눠 보내기, 또는 "첫 번째 `tool_use`만 유효" → 한 user 메시지에 모두 담아야 합니다. [Patrick-0018]
- 성공할 때까지 같은 호출을 무한 재시도 → 같은 결함을 반복하고, 장애가 계속되면 응답이 오지 않습니다. [Amey-0032] [Udemy-0036]
- 실패를 빈 `tool_result`로 숨기기 → 모델이 "결과 없음"으로 오해해 잘못된 답을 이어 갑니다. [Udemy-0036]
- 실패할 때마다 예외를 던지고 대화 종료 → 모델이 설명하거나 대안을 낼 기회가 사라집니다. [Udemy-0036]
- raw 에러를 최종 사용자에게 노출 → 내부 정보가 새어 나갑니다. [Amey-0032]
- 입력 형식 문제에 temperature를 낮추거나 description을 늘리거나 `tool_choice: auto`를 쓰기 → 보장 수단은 `strict: true`뿐입니다. [Preporato-0025]
- tool 선택 문제에 "신중히 고르라"는 지시, context window 확장, 알파벳 정렬 → 중복이라는 설계 문제를 해결하지 못합니다. [Amey-0031]
- description은 짧게, 정확도는 이름으로 보완 → description이 가장 중요하며 이름만으로는 사용 시점과 파라미터 의미가 전달되지 않습니다. [Udemy-0045] [Amey-0063]
- 잘못된 tool 호출을 사후 재시도로 바로잡기 → 첫 호출 자체를 막지 못하고, 되돌리기 어려운 작업은 이미 영향이 생깁니다. [Udemy-0045]
- 필수 순서를 system 프롬프트, few-shot, effort 상향, JSON 단계 출력으로 지키게 하기 → 판단이 모델에 남아 있어 보장되지 않습니다. [Udemy-0016]
- server tool은 앱이 실행하고 `tool_result`를 보낸다 / client tool은 Anthropic 쪽에서 돈다 → 실행 위치를 바꿔 생각한 오답입니다. [Preporato-0023] [Udemy-0013]
- server tool은 MCP 전용 또는 Batch API 전용 → 일반 요청의 `tools`에 선언합니다. [Preporato-0023]
- 사내 시스템을 server tool로 연결 → server tool은 Anthropic이 제공하는 것이라 사용자가 정의할 수 없고 사내망에도 닿지 않습니다. [Udemy-0013]
- 공유 기능을 앱마다 복사하거나, 데이터를 system 프롬프트에 매일 붙여 넣거나, Skill로 API 연결하기 → 복사본은 어긋나고, 붙여 넣은 데이터는 낡으며, Skill에는 live connection이 없습니다. [Amey-0009]
- 외부 시스템이 없는 절차에 MCP server, custom tool, fine-tuning 쓰기 → 절차와 know-how는 Skill로 다룹니다. [Preporato-0024]
- MCP server가 Messages API를 대체한다 / 모델과 같은 프로세스여야 한다 → 둘 다 틀립니다. [Amey-0044]
- tool 발견에 prompts, resources를 쓰거나 빈 인자로 `tools/call`을 시험 호출 → 발견은 `tools/list`로 합니다. [Udemy-0025]
- 로컬과 원격 둘 다 stdio로, 또는 둘 다 HTTP로 → 배포 위치와 제공 범위에 따라 나눠 씁니다. [Udemy-0033]
- MCP connector로 resources(약관 문서)를 읽히거나 stdio 서버 연결 → tool 호출만 되고 HTTP 서버만 연결됩니다. [Udemy-0011]
- MCP connector에서 `mcp_tool_use`를 받고 앱이 다시 `tools/call` 실행 → API가 이미 실행했으므로 중복 실행이 됩니다. [Udemy-0011]

## 4. 암기 목록

| 필드/파라미터/MCP 용어 | 의미 |
|---|---|
| `stop_reason: tool_use` | 모델이 client tool 호출을 요청하며 멈춘 상태 [Patrick-0002] |
| `tool_use` 블록 | assistant content에 담긴 tool 호출(id, name, input) [Patrick-0017] |
| `tool_result` 블록 | user 메시지에 넣는 실행 결과 [Patrick-0002] |
| `tool_use_id` | `tool_result`를 해당 `tool_use`와 짝짓는 id [Patrick-0002] |
| `is_error: true` | `tool_result`에 붙이는 실행 실패 표시 [Udemy-0036] |
| `disable_parallel_tool_use` | 한 턴에 tool 호출을 하나로 제한 [Patrick-0018] |
| `tool_choice: auto` | 기본값. 호출 여부를 모델이 판단 [Udemy-0036] |
| `tool_choice: any` | 어떤 tool이든 반드시 사용 [Udemy-0036] |
| `tool_choice: tool` | 지정한 tool을 반드시 사용 [Udemy-0036] |
| `tool_choice: none` | tool 사용 금지 [Udemy-0036] |
| `strict: true` | tool 입력이 `input_schema`를 따르도록 검증 [Preporato-0025] |
| `input_schema` | tool 입력의 JSON Schema(API tool 정의) [Preporato-0025] |
| `description` | tool 선택과 사용의 핵심 근거: 하는 일·사용 시점·파라미터·제약 [Udemy-0045] |
| client tools | 앱에서 실행(사용자 정의 tool, `bash`, `text_editor`) [Udemy-0013] |
| server tools | Anthropic 인프라에서 실행(`web_search`, `web_fetch`, `code_execution`, `tool_search`) [Udemy-0013] |
| MCP server | 여러 client가 공유하고 독립적으로 유지보수하는 tools/resources 제공자 [Amey-0044] |
| Skill | 작업이 일치하면 로드되는 지시·템플릿 묶음(live connection 없음) [Preporato-0024] |
| MCP tools | 모델이 주도해 호출하는 primitive [Udemy-0025] |
| MCP resources | URI로 노출되는 참조 데이터. context에 넣을지는 앱이 결정 [Udemy-0025] |
| MCP prompts | 사용자가 slash command 등으로 고르는 프롬프트 템플릿 [Udemy-0025] |
| `tools/list` | 서버의 tool 목록(`name`, `description`, `inputSchema`) 조회 [Udemy-0025] |
| `tools/call` | client가 tool 실행을 요청 [Udemy-0025] |
| `inputSchema` | MCP tool 인자를 정의하는 JSON Schema [Udemy-0025] |
| `isError` | MCP tool 실행 에러 표시(입력 검증 실패 포함) [Udemy-0025] |
| `listChanged` / `notifications/tools/list_changed` | tool 목록 변경을 client에 알림 [Udemy-0025] |
| host / client / server | host(Claude Code 등)가 서버마다 client를 만들어 연결 [Udemy-0033] |
| transport: stdio | 같은 머신의 subprocess와 표준 입출력으로 통신. 로컬·단일 client [Udemy-0033] |
| transport: Streamable HTTP | HTTP POST + 선택적 SSE. 원격·다수 client. HTTP 인증과 OAuth [Udemy-0033] |
| `mcp_servers` | MCP connector 서버 정의(`type`, `url`, `name`, `authorization_token`) [Udemy-0011] |
| `mcp_toolset` | `tools` 배열 안의 항목. `mcp_server_name`으로 서버 참조 [Udemy-0011] |
| `default_config` / `configs` | `mcp_toolset`의 전체 기본값 / tool별 `enabled` 덮어쓰기 [Udemy-0011] |
| `mcp_tool_use` / `mcp_tool_result` | MCP connector 응답에 함께 오는 호출·결과 블록(API가 실행) [Udemy-0011] |

## 5. 시험 직전 체크리스트

- [ ] `tool_result`는 user 메시지에 넣고 같은 `tool_use_id`로 짝을 맞춘다 (assistant 턴은 그대로 유지)
- [ ] 병렬 `tool_use`의 결과는 한 user 메시지에 모두 담는다
- [ ] tool 실패는 `is_error: true`로 모델에 알린다 (숨기기, 무한 재시도, 중단은 오답)
- [ ] `tool_choice` 네 가지(auto/any/tool/none)를 구분하고, 강제 호출은 `tool`로 지정한다
- [ ] 입력 타입과 필수 필드 보장은 `strict: true`
- [ ] tool 선택 정확도의 핵심은 description(하는 일, 사용 시점, 파라미터, 제약)
- [ ] tool이 겹치면 통합하고 역할을 나눈다 (지시문, context 확장, 정렬은 오답)
- [ ] 큰 객체가 다음 호출에만 필요하면 identifier를 반환한다
- [ ] 필수 순서는 앱 측 state machine으로 tool을 걸러 강제한다 (프롬프트로는 보장 불가)
- [ ] client tool은 앱에서, server tool은 Anthropic에서 실행된다 (server tool은 `tool_result` 불필요)
- [ ] 공유 + 독립 유지보수는 MCP server, 절차·know-how는 Skill, 행동·데이터 접근은 tool/MCP
- [ ] MCP primitives: tools는 모델, resources는 앱, prompts는 사용자가 주도
- [ ] tool 발견은 `tools/list`(`inputSchema`), 실행은 `tools/call`
- [ ] 로컬 subprocess는 stdio, 원격·다수 client는 Streamable HTTP
- [ ] MCP connector: `mcp_servers` + `mcp_toolset`, tool만 지원, HTTP 서버만, 앱은 다시 실행하지 않는다
