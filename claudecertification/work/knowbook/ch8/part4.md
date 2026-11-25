@@ ADD-TO: ### 1-10. 확장 수단 선택: MCP server vs Tool vs Skill

| 수단 | 쓰는 경우 | 특징 |
|---|---|---|
| 기성 MCP server | 표준 서비스의 표준 조작<br>(GitHub · Slack · GitLab<br>ServiceNow · Jira) | 연결만으로 사용<br>유지보수 = 제공처(upstream) |
| custom MCP server | 팀 고유 workflow<br>(2단계 승인 · 예약 절차 · release 판정) | 범위를 좁혀 고유 로직만 구현 |

**기성 vs custom 분리 기준**

| 구분 | 내용 |
|---|---|
| 판별 | 많은 조직이 공통 사용 = 기성 서버<br>자사에만 존재 = custom 서버 |
| 요건 분해 | 표준 조작 · 자체 로직으로 나눔<br>각각 가장 수고가 적은 수단 적용 |
| 혼합 구성 예 | 표준 조작 = 기성 서버<br>release 판정 · 승인 준비 = custom 서버 |
| 인력 제약 | 개발자 1명 · 보수 최소화 = 기성 서버 우선 |
| 기성 서버 채택 전 확인 | 제공처 · 업데이트 상황 · 요구 권한 범위 |
| 공유 · 인증 | 팀 서버 = project scope `.mcp.json`<br>custom 서버 토큰 = 환경 변수 확장 |

<sub>근거: CCAR-F-Udemy02-0049, CCAR-F-Udemy03-0028, CCAR-F-Udemy04-0004, CCAR-F-Udemy06-0003</sub>

@@ ADD-TO: ### 1-11. MCP primitives: tools / resources / prompts

**요구 → primitive 대응**

| 요구 | primitive |
|---|---|
| 동작 수행 (Jira 티켓 생성) | tool |
| 사용자가 첨부하는 읽기 전용 데이터<br>(API schema 파일) | resource |
| 재사용 템플릿 · 노하우<br>(심각도 기준이 담긴 triage 템플릿) | prompt |
| host에서 목록 탐색<br>+ 선택분만 context 첨부<br>+ 탐색 turn 회피 | resources<br>(`resources/list` → `resources/read`) |
| 정적 카탈로그 + 조작 | 카탈로그 = resource<br>tool = 조작만(예: `create_return`) |

| 구분 | 내용 |
|---|---|
| 선택 단서 | 문제문에서 "누가 언제 쓰는가" 확인<br>모델 = tool · host = resource · 사용자 = prompt |
| 카탈로그를 tool로 조회 | 모델의 탐색 turn 발생<br>(예: 작업마다 7회 호출) |
| 카탈로그를 `CLAUDE.md`에 복사 | 상시 로딩 |
| Claude Code 첨부 | 연결 서버의 resource를 `@`로 참조 |
| 운영 | 내용 개정 시 resource 갱신<br>변경을 client에 알림 |

<sub>근거: CCAR-F-Udemy02-0008, CCAR-F-Udemy05-0008, CCAR-F-preporato-0014</sub>

@@ ADD-TO: ### 1-13. MCP transport: stdio vs Streamable HTTP

**Claude Code transport 선택**

| transport | 용도 | 인증 · 비고 |
|---|---|---|
| stdio | 자기 머신의 로컬 프로세스 | 로컬 실행 |
| `http` | 원격 MCP server 연결(권장) | OAuth 2.0 사용 가능<br>`claude mcp add --transport http <URL>`<br>→ `/mcp`에서 브라우저 인증 |
| `sse` | 구방식 | deprecated → HTTP 가능하면 HTTP<br>⚠️ 시점에 따라 바뀜: 현재 공식 문서 기준 |
| WebSocket | 서버가 이벤트를 자발 전송<br>양방향 지속 연결 | 헤더 인증만 · OAuth ✗ |

| 선택 순서 | 확인 내용 |
|---|---|
| ① 연결 대상 위치 | 로컬 프로세스 · 원격 |
| ② 통신 방향 | 요청 응답만 · 서버 push |
| ③ 인증 방식 | OAuth 필요 여부 |

- 사내 클라우드 · 응답만 · OAuth 로그인 = 3조건 모두 HTTP
- 로컬 프로세스 → 사내 클라우드 이전 = 각자 `--transport http`로 URL 추가

<sub>근거: CCAR-F-Udemy02-0046, CCAR-P-jrajath94-0649</sub>

@@ ADD-TO: ### 1-14. MCP connector (Messages API의 `mcp_servers`)

| 구분 | 내용 |
|---|---|
| 서버 ↔ toolset | `mcp_servers`의 서버마다<br>`mcp_toolset` 정확히 1개가 참조 |
| 다중 서버 | 서버마다 `mcp_toolset` 1개<br>→ 한 요청에서 여러 서버 tool을 횡단 선택 |
| 역할 분담 | `mcp_servers` = 접속(URL · 인증)<br>`mcp_toolset` = tool 활성화 |
| `mcp_toolset` 생략 | 규칙 위반 · 자동 검출 의존 ✗ |
| 실시간 원격 데이터 | API가 원격 서버 tool 호출 → 앱의 MCP client 불필요 |
| 활성화 | `mcp_servers` 정의<br>+ `mcp_toolset` 참조 + beta 헤더 |
| 실시간 요건 | 저장 스냅샷 · 주기 복사 인덱스 ✗ |

<sub>근거: CCAR-F-Udemy03-0031, CCAR-P-jrajath94-0646</sub>

@@ NEW-SECTION
### MCP server scope와 `.mcp.json` credential (Claude Code)
**공유 = project · 개인 = user · 비밀 = `${VAR}`**

| scope | 저장 위치 | 공유 · 로드 범위 |
|---|---|---|
| local (기본값) | `~/.claude.json`<br>(현재 프로젝트용) | 본인만 · 현재 프로젝트에서만 로드 |
| project | 프로젝트 루트 `.mcp.json` | 버전 관리로 팀 공유 |
| user | `~/.claude.json` | 공유 ✗<br>본인의 모든 프로젝트에서 로드 |

| 상황 | 정답 |
|---|---|
| 팀 전원이 쓰는 서버 | `--scope project` → `.mcp.json` commit |
| 기본 명령으로 추가한 서버가 동료에게 안 보임 | local scope 저장이 원인<br>→ `--scope project`로 재추가 |
| 개인 · 실험 서버를 여러 repo에서 사용 | `claude mcp add --scope user` |
| 시험 서버가 팀용으로 굳어짐 | project scope로 이동 |
| 특정 프로젝트에서만 개인 시험 | local scope |
| 팀 공유 서버 + 개인별 token | project `.mcp.json` + `${VAR}` 참조 |

| credential 처리 | 내용 |
|---|---|
| `${VAR}` | 환경 변수 확장<br>(예: `headers`의 `Bearer ${PR_API_TOKEN}`) |
| `${VAR:-default}` | 기본값을 붙이는 확장 형태 |
| 실제 값 | 각 개발자 · 각 환경에서 설정 |
| 필요 변수명 | README · 온보딩 문서에 기재 |
| `$VAR` (중괄호 없음) | 문서화된 확장 구문 ✗ |
| Claude Code · 알려진 credential 변수명 | 원격 서버 url · headers에서 의도적으로 빈 값 처리<br>→ 자체 변수명 사용 |
| token 직접 삽입 | 접근 제한과 무관하게 유출 |

| 증상 | 원인 | 조치 |
|---|---|---|
| 일부 멤버만 401<br>`claude mcp list`에 미설정 변수 경고 | 해당 환경에 `${VAR}` 미설정 | 각자 환경 변수에 token 설정 후 Claude Code 시작 |
| 변수 미설정 + default 없음 | config는 로드<br>경고 표시 · `${VAR}` 원문 그대로 사용 | 변수 설정 또는 `:-default` |
| project scope 서버 승인 거부 | 대화형 session 첫 사용 시 승인 요구 | `claude mcp reset-project-choices` |

- 신규 멤버 절차서 = 필요 환경 변수 목록 · `claude mcp list` 경고 확인 · 승인 조작

<sub>근거: CCAR-F-MyPractice-0044, CCAR-F-Udemy01-0037, CCAR-F-Udemy02-0013, CCAR-F-Udemy04-0010, CCAR-F-Udemy05-0006, CCAR-F-Udemy06-0010, CCAR-F-paullarionov-0044, CCAR-F-preporato-0015</sub>

@@ NEW-SECTION
### 여러 MCP server를 한 session에 연결 (Agent SDK) · tool search
**서버를 나누거나 합치지 않고 한 session에 연결**

| 구분 | 내용 |
|---|---|
| 연결 시 | 설정된 모든 MCP server의 tool 검색<br>→ agent에서 동시 사용 |
| 설정 | Agent SDK `mcpServers` 옵션 또는 `.mcp.json`<br>→ 여러 서버 등록 |
| tool 이름 | `mcp__서버이름__tool이름`<br>한 session에 나열 |
| 서버 횡단 요청 | 서버 하나만 연결한 session ✗<br>(요청이 매번 중간에 중단) |
| 권한 | 허용되지 않은 MCP tool 호출 = 권한 확인으로 이동<br>`allowedTools`에 서버 단위 와일드카드로 허용<br>(예: `mcp__caselaw__*`) |
| 상태 확인 | `system/init` 메시지의 서버별 연결 상태<br>`failed` · `needs-auth` 감지 |

| tool search 설정 | 동작 |
|---|---|
| 기본 | tool search 활성<br>MCP tool 정의 = 필요할 때까지 로드 지연 |
| `ENABLE_TOOL_SEARCH=auto` | 정의가 context window 10% 도달 전 = 미리 로드<br>도달 후 = tool search 시작 |
| `alwaysLoad` | 한 서버의 tool을 미리 로드<br>임계값 설정 ✗ |
| `ENABLE_TOOL_SEARCH=false` | 전 정의 미리 로드 · 임계값 동작 ✗ |
| 임계값 규칙 충족 | 기본 설정 + `auto`<br>별도 랭킹 서비스 작성 ✗ |

<sub>근거: CCAR-F-Udemy05-0015, CCAR-P-jrajath94-0651</sub>

@@ NEW-SECTION
### 통합 방식 선택: MCP · 직접 API · CLI wrapper · agent-to-agent
**재사용이 실제로 있을 때만 MCP**

| 상황 | 방식 |
|---|---|
| 호스트 1 · 언어 1 · 소비자 1<br>(재사용 명시 ✗) | 직접 API/SDK<br>프로토콜 계층 생략 |
| 호스트 · 언어 · 팀 여러 개가 같은 기능 | MCP server 1개 · schema 1개 |
| 공유 기능 + 소비자 8개 (예: 로깅) | MCP server 또는 공유 library · service |
| 독점 SDK만 존재 + 여러 팀 | SDK를 MCP server 하나로 감쌈<br>벤더 특이 사항을 한 곳에 격리 |
| 기능이 CLI로만 존재 · 일회성 · 소비자 1 | CLI wrapper |
| 벤더가 안정적 typed API 출시 | CLI wrapper → 직접 API 이전 |
| 하위 작업이 자체 plan · tools · context 필요 | agent-to-agent + handoff 계약 |
| 별개 벤더 agent 간 목표 · 상태 교환 | agent-to-agent |
| 운영 부담 0 요구 | 관리형 런타임 |
| 필요한 것이 tool 하나 | tool만 노출한 MCP server 하나 |

| 프로토콜 | 연결 대상 |
|---|---|
| MCP | agent ↔ tool · 데이터 소스 |
| agent-to-agent | agent ↔ agent<br>작업 인계 · 상태 업데이트 · 협상 |
| 직접 REST · function calling | 안정적 단일 API · 소비자 하나 |

| 구분 | 내용 |
|---|---|
| 비교 기준 | 재사용 · 보안 경계 · 소유권 · 운영 복잡도 |
| MCP가 효과적인 경우 | tool 많음 · 동적 탐색<br>agent 간 공유 서버 |
| MCP server 비용 | 새로 소유할 service<br>(구축 · 호스팅 · 보안 · 버전 관리 · 가동 시간) |
| MCP 비용 보상 조건 | 재사용이 실제로 존재 |
| 직접 API 비용 | 소비자마다 client 업데이트<br>API 인증은 여전히 필요 |
| CLI wrapper 비용 | 취약한 parsing<br>형식 변경 테스트 필요 |
| agent-to-agent 비용 | 담당자 · 계약 필요<br>없으면 감독 없는 두 번째 loop |
| 재평가 시점 | 두 번째 팀 · 언어 등장 |

| 대안 | 정답이 되는 조건 |
|---|---|
| 직접 API | 호스트 1 · 언어 1 |
| MCP server | 소비자 여러 개<br>(예: 3팀 · 5팀 · 6서비스 · 8서비스) |
| CLI wrapper | 기능이 CLI로만 존재 · 소비자 1 |
| agent-to-agent | 하위 작업이 자체 plan · tools 필요 |
| 소비자별 개별 구현 | 규제로 schema 공유 불가 |
| 공유 library · service | 소비자 여러 개 (MCP의 대안) |

<sub>근거: CCAR-P-jrajath94-0002, CCAR-P-jrajath94-0012, CCAR-P-jrajath94-0077, CCAR-P-jrajath94-0175, CCAR-P-jrajath94-0176, CCAR-P-jrajath94-0177, CCAR-P-jrajath94-0178, CCAR-P-jrajath94-0303, CCAR-P-jrajath94-0360, CCAR-P-jrajath94-0361, CCAR-P-jrajath94-0423, CCAR-P-jrajath94-0424, CCAR-P-jrajath94-0486, CCAR-P-jrajath94-0487, CCAR-P-jrajath94-0549, CCAR-P-jrajath94-0550, CCAR-P-jrajath94-0647, CCAR-P-jrajath94-0648, CCAR-P-preporato-0011</sub>

@@ NEW-SECTION
### 외부 통합의 신원 · 인가: 입력은 claim · 강제는 코드
**사용자 입력은 claim · 인가는 코드에서 강제**

| 값의 출처 | 판정 |
|---|---|
| 채팅에 입력한 clinic 이름 · `tenant_id` | claim ✗ |
| 드롭다운에서 고른 자회사 | claim ✗ |
| 사용자가 편집 가능한 profile JSON의 `company` | claim ✗ |
| 시스템 프롬프트 속 사용자 role 주장 | 인가 ✗ |
| 인증된 세션 · 신원에서 얻은 값 | 인가 근거 ✓ |
| 서버가 설정한 편집 불가 필드 | 인가 근거 ✓ |

| 구분 | 내용 |
|---|---|
| tenant 격리 필터 | 인증된 신원을 명단과 코드에서 대조<br>읽기 전에 실행 |
| 응답 생성 후 필터 | ✗ 데이터를 이미 읽은 뒤 → 유출 |
| 부작용 tool<br>(성적 변경 · 환불 · export) | 실행 전 코드에서 결정론적 검사<br>호출자 신원 + 대상 권한 확인 → 허용 · 거부 |
| 정책 예 | 1,000행 초과 export<br>→ 승인 token 없으면 거부 |
| 사후 감사 로그 | 보완용 · 단독 통제 ✗ |
| 원본 시스템 ACL | 유지 |
| 의존성 | 신원 ↔ 대상(학생 · tenant) 매핑 필요<br>명단이 오래되면 정당한 사용자 차단 · 이전 사용자 허용 |

| 구분 | 내용 |
|---|---|
| authentication | 로그인 = 신원 증명 |
| authorization | 입력한 대상(예: 학생)에 접근할 권리 확인<br>보호자 명단과 코드 대조 |
| authN만 구현 | 대상 확인 누락 = 인가 결함 |
| 모델의 역할 | 신원 · 정책 · 잠금장치 ✗<br>누가 권한을 가졌는지 모름 |

<sub>근거: CCAR-P-jrajath94-0298, CCAR-P-jrajath94-0305, CCAR-P-jrajath94-0353, CCAR-P-jrajath94-0354, CCAR-P-jrajath94-0416, CCAR-P-jrajath94-0479, CCAR-P-jrajath94-0542</sub>

@@ NEW-SECTION
### 외부 통합 credential · 귀속 · 신뢰 경계
**귀속이 필요하면 공유 credential ✗**

| 상황 | 정답 |
|---|---|
| 감사에서 지시한 사람 특정 | per-user delegation<br>요청 사용자 ID로 동작 · 대상 시스템이 그 사용자 권한 강제 |
| 팀 단위 귀속 | 팀별 credential · token |
| remote MCP server가 요청 직원 기록 | 사용자별 OAuth token<br>→ `authorization_token`으로 전달 |
| 사용자 데이터 읽기 | 마스터 API key ✗<br>좁은 scope의 사용자별 delegation token |
| 공유 설정 속 개인 credential | scope 제한된 service identity |
| 귀속 불필요한 read-only 내부 대시보드 | 공유 credential 허용 |

| 방식 | 귀속 불가 이유 |
|---|---|
| 공유 credential | 로그에 공유 ID 하나로 합쳐짐 |
| 프롬프트에 직원 이름 | 시스템이 검증 불가 · 인증 ✗ |
| 앱 로그에 이름 기록 | 기록 시스템(ERP)은 단일 ID만 인가<br>두 로그가 어긋날 수 있음 |
| 부서별 credential | 사람 특정 ✗ |
| 공유 OAuth token + 로깅 프록시 | 로그인한 사용자를 식별하는 token ✗ |
| `anthropic-workspace-id` 헤더 | 팀 workspace 지정 · 직원 식별 ✗ |
| 마스터 키 | ambient authority → confused deputy<br>모든 사용자의 데이터 접근 |
| 설정에 하드코딩된 개인 credential | 귀속 ✗ · 교체 ✗<br>개발자 이탈 시 credential도 이탈 |

| 연결 대상 | 인증 방침 |
|---|---|
| 로컬 stdio server<br>(사용자가 spawn) | 사용자 신뢰 상속<br>OAuth는 얻는 것 없음 |
| 원격 MCP server<br>(네트워크 경유) | OAuth 필수<br>⚠️ 1-13은 OAuth '권장' · 해설 표현 차이 |
| 로컬 server가 socket listen | 방침 반전 → 인증 필요 |
| 한 머신에서 여러 사용자가 공유하는 로컬 server | OAuth 필요 |
| 모든 server에 OAuth | 경계 없는 곳 = 보안 쇼 · 구성 비용 |
| 인증 없음 | 네트워크 = principal ✗ |
| 로컬 API key + 원격 무인증 | 배치 반대 |

| 경계 통제 | 내용 |
|---|---|
| 경계 넘는 bearer token | audience 바인딩<br>수신 시 audience 확인 |
| TLS | 전송 중 privacy · audience 증명 ✗ |
| token 주기 교체 | 수명 위협 대응 · 바인딩 ✗ |
| token · secret 보관 | 시스템 프롬프트 ✗ |
| 환불 인가 | 소유 시스템(청구)에서 결정론 강제 · fail closed |
| 캐시된 승인 | 승인자가 내리지 않은 승인 ✗ |
| 검토용 두 번째 model | 같은 신뢰 못 할 입력을 읽음 |
| 의존성 | 파트너의 바인딩 확인 협조<br>청구 시스템의 승인 통합 |
| per-user delegation 비용 | IdP의 사용자별 token · 대상 시스템 권한 매핑<br>공유 secret보다 무거움 |

| claude.ai connector tool 제어 | 내용 |
|---|---|
| 조직 제어 `blocked` | Claude가 보기 전에 목록에서 tool 제거 |
| allow 규칙 | 프롬프트 없이 실행 허용 · 차단 ✗ |
| idle timeout | tool 숨김 수단 ✗ |

<sub>근거: CCAR-P-jrajath94-0160, CCAR-P-jrajath94-0161, CCAR-P-jrajath94-0162, CCAR-P-jrajath94-0417, CCAR-P-jrajath94-0480, CCAR-P-jrajath94-0543, CCAR-P-jrajath94-0632, CCAR-P-jrajath94-0649</sub>

@@ RULES

| 상황 | 정답 |
|---|---|
| 팀 공유 MCP server + 개인별 token | project `.mcp.json` + `${VAR}` 참조<br>필요 변수는 README에 기재 |
| 기본 명령으로 추가한 서버가 동료에게 안 보임 | `--scope project`로 재추가 → `.mcp.json` commit |
| 개인 · 실험 서버를 여러 repo에서 사용 | `--scope user` |
| 원격 HTTP MCP + Authorization 헤더 + 설정 공유 | `.mcp.json` `headers`<br>→ `Bearer ${VAR}` commit |
| 일부 멤버만 401 + 미설정 변수 경고 | 해당 환경에 변수 설정 |
| 사내 클라우드 서버 + 요청 응답만 + OAuth 로그인 | `claude mcp add --transport http`<br>→ `/mcp` 인증 |
| 서버가 이벤트를 자발 전송 | WebSocket (헤더 인증만) |
| 여러 MCP server를 가로지르는 요청 (Agent SDK) | `mcpServers`에 모두 등록<br>`allowedTools`에 서버 와일드카드 |
| 정의가 window 일정 비율일 때만 tool search | `ENABLE_TOOL_SEARCH=auto` |
| 표준 서비스(GitHub · Slack · GitLab)의 표준 조작 | 기성 MCP server |
| 팀 고유 workflow (승인 · 예약 절차 · release 판정) | custom MCP server (범위 한정) |
| 동작 · 첨부 데이터 · 재사용 템플릿 | tool · resource · prompt 순 |
| host 목록 탐색 + 선택분만 첨부 | resources<br>(`resources/list` · `resources/read`) |
| 정적 카탈로그 때문에 탐색 호출 반복 | 카탈로그 = resource · tool = 조작만 |
| Messages API에서 여러 원격 MCP server 한 요청 사용 | 서버마다 `mcp_toolset` 1개 |
| 앱에 MCP client 없이 실시간 원격 데이터 | `mcp_servers` + `mcp_toolset` + beta 헤더 |
| 호스트 1 · 언어 1 · 안정적 API | 직접 API · MCP ✗ |
| 호스트 · 언어 · 팀 여러 개가 같은 기능 | MCP server 1개 · schema 1개 |
| 기능이 CLI로만 존재 | CLI wrapper + 형식 변경 테스트 |
| 하위 작업이 자체 plan · tools 필요 | agent-to-agent + handoff 계약 |
| 별개 벤더 agent 간 위임 | agent-to-agent (MCP ✗) |
| 사용자 입력 값으로 tenant 필터 | 인증된 신원에서 tenant 도출 · 코드에서 필터 |
| 부작용 tool 권한 검사 | 실행 전 코드에서 결정론적 검사 · fail closed |
| 감사에서 사람 특정 | per-user delegation |
| remote MCP server가 직원별 기록 | 사용자별 OAuth token → `authorization_token` |
| 로컬 stdio vs 원격 MCP 인증 | stdio = 사용자 신뢰 상속<br>원격 = OAuth |
| 신뢰 경계를 넘는 bearer token | audience 바인딩 + 수신 시 확인 |
| Claude가 보기 전에 connector tool 차단 | 조직 제어 `blocked` |

<sub>근거: CCAR-F-MyPractice-0044, CCAR-F-Udemy01-0037, CCAR-F-Udemy02-0008, CCAR-F-Udemy02-0013, CCAR-F-Udemy02-0046, CCAR-F-Udemy02-0049, CCAR-F-Udemy03-0028, CCAR-F-Udemy03-0031, CCAR-F-Udemy04-0010, CCAR-F-Udemy05-0006, CCAR-F-Udemy05-0008, CCAR-F-Udemy05-0015, CCAR-F-Udemy06-0003, CCAR-F-Udemy06-0010, CCAR-F-paullarionov-0044, CCAR-F-preporato-0014, CCAR-F-preporato-0015, CCAR-P-jrajath94-0012, CCAR-P-jrajath94-0160, CCAR-P-jrajath94-0161, CCAR-P-jrajath94-0162, CCAR-P-jrajath94-0175, CCAR-P-jrajath94-0176, CCAR-P-jrajath94-0177, CCAR-P-jrajath94-0298, CCAR-P-jrajath94-0305, CCAR-P-jrajath94-0632, CCAR-P-jrajath94-0646, CCAR-P-jrajath94-0649, CCAR-P-jrajath94-0651</sub>

@@ TRAPS

| 오답 | 이유 |
|---|---|
| token을 `.mcp.json`에 직접 기재<br>(`.gitignore` · 접근 제한 병행) | 접근 제한과 무관하게 유출<br>공유 설정 구조 붕괴 |
| token을 `CLAUDE.md`에 기재 | 모델 context에 들어가 출력 · 로그로 유출 |
| 개인 `~/.claude.json`을 repo에 check-in | 인증 정보 유출 |
| 팀 공유를 user scope 재등록으로 해결 | user scope = 본인만 |
| 개발자마다 local scope 수동 추가 | 다른 사람에게 전파 ✗ · 수동 단계 반복 |
| placeholder token + 로컬 override<br>`.env` 읽는 wrapper server | 버전 관리되는 단일 기준 · 환경 변수 방식(관례)이 아님 |
| 개인 · 실험 서버를 `.mcp.json` + `.gitignore` | 공유용 구조를 개인용으로 전용 |
| 개인 서버를 `.mcp.json`에 commit | 개인 설정을 팀에 떠넘김 |
| `$PR_API_TOKEN` (중괄호 없음) | 문서화된 확장 구문 ✗ |
| 일부 멤버의 401을 scope · 승인 문제로 진단 | 일부 멤버만 + 미설정 변수 경고 = 개인 환경 부족 |
| 서버별 session · 라우터 · 서버 통합 | 동시 사용 전제를 모른 불필요한 구조 변경 |
| `sse` transport 선택 | deprecated |
| WebSocket으로 OAuth 로그인 | WebSocket = 헤더 인증만 |
| 카탈로그 목록을 tool로 조회 | 모델의 탐색 turn 발생 |
| 카탈로그를 prompt로 공개 | prompt = 사용자가 기동하는 템플릿 |
| 카탈로그를 `CLAUDE.md`에 복사 | 상시 로딩 |
| 목록 tool 한 번에 반환 건수 확대<br>tool description에 목록 전문 기재 | 대량 정보를 매번 context에 투입 |
| `mcp_toolset` 생략 후 자동 검출 의존 | 서버마다 1개 참조 규칙 위반 |
| 서버별로 요청을 나눠 JSON 수동 전달 | 한 요청 안 횡단 선택 요건 미충족 |
| 범용 proxy tool로 서버 tool 메타데이터 숨김 | tool 선택 단서 박탈 |
| 주기 복사 인덱스 검색 | 저장 스냅샷 · 실시간 ✗ |
| `alwaysLoad`로 임계값 구현 | 한 서버 tool을 미리 로드할 뿐 |
| 별도 랭킹 서비스 작성 | 기본 설정 + `auto`로 충족 |
| 표준 서비스까지 custom MCP server로 직접 구축 | 표준 조작의 유지보수까지 떠안음 |
| 여러 통합을 custom server 하나로 통합 | 표준 연동 유지보수 부담 잔존 |
| GitHub Issue 대신 웹 검색 · 정적 export | 구조화 데이터 · 자체 workflow 희생 |
| `CLAUDE.md` 절차서 + curl · Bash | 구조화된 tool 정의 없음<br>절차 순서 · 인증 처리를 prompt에 의존 |
| 작업별 slash command | API 선택을 Claude prompt에 위임 |
| "MCP는 표준" · "미래 재사용" 근거로 MCP 구축 | 서버 구축 · 호스팅 · 보안 비용 · 얻는 기능 없음 |
| MCP server + 직접 REST tool 병행 | 유지보수 범위 2배 |
| agent-to-agent로 REST API · CRM 연결 | CRM은 agent ✗ |
| 별개 벤더 agent에 MCP로 연결 | MCP = agent ↔ tool |
| 공유 REST polling으로 agent 협업 | 데이터 교환만 · 위임 의미 체계 ✗ |
| 별개 벤더 두 agent를 하나로 합침 | 기술 · 계약상 불가 |
| 팀마다 SDK 직접 호출 · 기능 재구현 | 유지보수 N배 · 벤더 특이 사항 분산 |
| 모델이 SDK 소스를 읽고 임의 호출 | 검토 · 테스트 불가 |
| 호스트별 client 라이브러리 | 사본마다 두 번째 schema |
| 언어별 CLI wrapper parsing | 취약한 parsing이 언어 수만큼 증가 |
| 소비자별 검색 agent | planning 불필요 → 조율 비용만 추가 |
| API를 CLI로 감싼 뒤 MCP를 위에 얹음 | 계층마다 parsing · 실패 모드 추가 |
| CLI 전용 메인프레임에 MCP server | 화면 스크래핑을 감싼 wrapper에 불과 |
| 단일 호스트에 stdio 서버 등록 · MCP wrapper | 불필요한 프로토콜 계층 |
| 속도를 위해 MCP 서버 인증 생략 | 회사 데이터 노출<br>직접 client도 API 인증 필요 |
| 직접 만든 Kubernetes operator로 운영 부담 0 | 운영 부담이 가장 큼 |
| 일회성 · 단일 쌍에 MCP | 한 번 쓰려고 protocol 비용 부담 |
| "모든 통합은 MCP" · 소규모 앱에 fine-tuning | 더 단순한 동작 옵션을 건너뜀 |
| 입력 clinic · `tenant_id`<br>드롭다운 · profile 필드로 필터 | 사용자 claim · 값 변경 한 번에 타 tenant 데이터 읽음 |
| 응답 후 필터 · 사후 감사 로그만 | 읽기 · 변경이 이미 발생 |
| 시스템 프롬프트 · 모델 판단 · 더 큰 모델로 인가 | 모델은 권한 보유자 모름<br>신뢰 경계를 성능 문제로 취급 |
| 로그인만 확인하고 입력한 대상 조회 허용 | authN만 있고 authZ 없음 |
| 프롬프트에 이름 · 앱 로그 · 부서별 credential로 귀속 | 시스템이 검증하는 사용자 ID ✗ |
| 공유 OAuth token + 로깅 프록시<br>`anthropic-workspace-id` 헤더 | 직원별 귀속 수단 ✗ |
| 마스터 API key를 agent에 부여 | ambient authority → confused deputy |
| 모든 server에 OAuth · 모두 무인증 · 로컬 key + 원격 무인증 | 신뢰 경계와 통제 짝이 어긋남 |
| TLS · 주기 교체 · 두 번째 model로 token · 환불 통제 | audience 바인딩 · 소유 시스템 강제 ✗ |
| token을 시스템 프롬프트에 보관 · 환불 승인 캐시 | secret 노출 · 승인자가 내리지 않은 승인 |
| allow 규칙 · idle timeout 0으로<br>connector tool 차단 | 차단 수단 ✗ · 조직 제어 `blocked`만 제거 |

<sub>근거: CCAR-F-MyPractice-0044, CCAR-F-Udemy01-0037, CCAR-F-Udemy02-0008, CCAR-F-Udemy02-0013, CCAR-F-Udemy02-0046, CCAR-F-Udemy02-0049, CCAR-F-Udemy03-0028, CCAR-F-Udemy03-0031, CCAR-F-Udemy04-0004, CCAR-F-Udemy04-0010, CCAR-F-Udemy05-0006, CCAR-F-Udemy05-0008, CCAR-F-Udemy05-0015, CCAR-F-Udemy06-0003, CCAR-F-Udemy06-0010, CCAR-F-paullarionov-0044, CCAR-F-preporato-0015, CCAR-P-jrajath94-0002, CCAR-P-jrajath94-0012, CCAR-P-jrajath94-0077, CCAR-P-jrajath94-0160, CCAR-P-jrajath94-0161, CCAR-P-jrajath94-0162, CCAR-P-jrajath94-0175, CCAR-P-jrajath94-0176, CCAR-P-jrajath94-0177, CCAR-P-jrajath94-0178, CCAR-P-jrajath94-0298, CCAR-P-jrajath94-0305, CCAR-P-jrajath94-0353, CCAR-P-jrajath94-0354, CCAR-P-jrajath94-0416, CCAR-P-jrajath94-0417, CCAR-P-jrajath94-0423, CCAR-P-jrajath94-0424, CCAR-P-jrajath94-0479, CCAR-P-jrajath94-0480, CCAR-P-jrajath94-0486, CCAR-P-jrajath94-0542, CCAR-P-jrajath94-0543, CCAR-P-jrajath94-0632, CCAR-P-jrajath94-0646, CCAR-P-jrajath94-0647, CCAR-P-jrajath94-0648, CCAR-P-jrajath94-0649, CCAR-P-jrajath94-0651, CCAR-P-preporato-0011</sub>

@@ MEMO

| 이름 | 의미 |
|---|---|
| `.mcp.json` | project scope 설정 파일 · commit 대상 |
| `~/.claude.json` | local · user scope 저장 위치 |
| `--scope local\|project\|user` | `claude mcp add` scope 옵션 (기본 local) |
| `${VAR}` · `${VAR:-default}` | `.mcp.json` 환경 변수 확장 |
| `claude mcp list` | 서버 상태 · 미설정 변수 경고 확인 |
| `claude mcp reset-project-choices` | project scope 서버 승인 선택 초기화 |
| `claude mcp add --transport http` | 원격 HTTP 서버 추가 |
| WebSocket transport | 서버가 이벤트 자발 전송 · 헤더 인증만 |
| `resources/list` · `resources/read` | resource 목록 · 내용 조회 |
| `@` | Claude Code에서 resource 참조 · 첨부 |
| `mcpServers` | Agent SDK의 MCP server 등록 옵션 |
| `mcp__서버이름__tool이름` | Agent SDK의 MCP tool 이름 규칙 |
| `allowedTools` | 허용 tool 지정 · 서버 와일드카드 가능 |
| `system/init` | 서버별 연결 상태 메시지<br>(`failed` · `needs-auth`) |
| `ENABLE_TOOL_SEARCH=auto` | 정의가 window 10% 도달 시 tool search 시작 |
| `alwaysLoad` | 한 서버의 tool을 미리 로드 |
| agent-to-agent | agent ↔ agent 위임 · 상태 · 협상 |
| CLI wrapper | CLI-only 기능을 subprocess로 감싸 parsing |
| per-user delegation | 요청 사용자 ID로 동작 · 대상 시스템이 권한 강제 |
| ambient authority | 마스터 키처럼 호출자와 무관하게 가진 넓은 권한 |
| confused deputy | ambient authority를 가진 agent가 사용자 대신 접근 |
| claim | 사용자가 주장한 값 · 인가 근거 ✗ |
| audience 바인딩 | token을 특정 수신 서비스에 묶음 · 수신 시 확인 |
| fail closed | 확인 불가 시 거부 |
| system of record | 기록 · 권한 기준 시스템(예: ERP) |
| 조직 제어 `blocked` | connector tool을 Claude가 보기 전에 제거 |

<sub>근거: CCAR-F-Udemy02-0008, CCAR-F-Udemy02-0046, CCAR-F-Udemy03-0031, CCAR-F-Udemy05-0006, CCAR-F-Udemy05-0008, CCAR-F-Udemy05-0015, CCAR-F-Udemy06-0010, CCAR-F-paullarionov-0044, CCAR-P-jrajath94-0002, CCAR-P-jrajath94-0160, CCAR-P-jrajath94-0161, CCAR-P-jrajath94-0177, CCAR-P-jrajath94-0298, CCAR-P-jrajath94-0480, CCAR-P-jrajath94-0543, CCAR-P-jrajath94-0649, CCAR-P-jrajath94-0651</sub>

@@ CHECK

- [ ] 공유 MCP = project `.mcp.json` + `${VAR}` · 개인 = user scope
- [ ] 재사용이 실제 있을 때만 MCP · 호스트 1 · 언어 1 = 직접 API
- [ ] 입력값(tenant · 이름 · 드롭다운) = claim → 인가는 코드에서 강제
- [ ] 정적 카탈로그 = resource · 귀속 필요 = 사용자별 credential

<sub>근거: CCAR-F-Udemy05-0008, CCAR-F-paullarionov-0044, CCAR-P-jrajath94-0160, CCAR-P-jrajath94-0176, CCAR-P-jrajath94-0298</sub>
