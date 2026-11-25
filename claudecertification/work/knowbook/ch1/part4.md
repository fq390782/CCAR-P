@@ ADD-TO: ### 1.1 Workflow vs Agent — 다음 단계를 누가 정하나

**작업 형태별 패턴 선택**

| 작업 형태 | 패턴 |
|---|---|
| 순서 고정 · 규칙 알려짐 · 입력 형식 일정 | deterministic workflow<br>모델 호출 = 모호한 부분에만 |
| 고정 경로 + 열린 단계 1개<br>(리뷰 코멘트 작성 등) | augmented LLM = 도구 가진 workflow<br>agentic ✗ |
| 검색 1회 + 판단 1회로 해결 | augmented single call<br>loop · multi-agent ✗ |
| 단계를 실행 전엔 나열 불가<br>발견이 다음 검색을 결정 | agentic loop<br>+ step 상한 · 중지 규칙 |
| 같은 순서 · 같은 trace 요구<br>(고정 체크리스트 검토 등) | deterministic workflow<br>agent = 실행마다 계획이 달라짐 |
| 고정 형식 파싱 (EDI 등) | parser · 결정론적 코드<br>모델 · 최상위 tier ✗ |
| 맞춤 답장 작성<br>(판단 1회 + 도구) | augmented single call<br>발송 전 어조 · 사실 확인 |
| 원인 모르는 장애 조사 | step budget 둔 agentic loop |

**이름이 통제를 결정**

| 구분 | 내용 |
|---|---|
| 판단 기준 | tool 사용 여부 ✗<br>단계를 누가 정하나 |
| 고정 경로 | validation gate 필요<br>loop 통제(반복 제한 · escalation) 불필요 |
| 진짜 agentic loop | 반복 제한 · 중지 조건 필요 |
| 오분류 | 고정 pipeline에 loop 통제 적용<br>→ 복잡성만 증가 |

**고정 순서 pipeline이 실패하는 경우**

| 증상 | 조치 |
|---|---|
| 질문마다 필요한 절차가 다름<br>(테스트 실행 필요 · 파일 5개 초과) | tool 정의 후 loop에 위임<br>다음 tool = 결과를 본 Claude가 결정 |
| tool 선택 근거 부족 | 각 tool `description`에 용도 · 다른 tool과의 구분 기재<br>= tool 성능에 가장 큰 영향 |

**아키텍처 리뷰에서 workflow를 고르는 근거**

| 구분 | 내용 |
|---|---|
| 올바른 근거 | 경로가 사전에 확정<br>→ 결정론적 orchestration이 저렴<br>· 테스트 가능 · 감사 가능 · 신뢰 |
| 판단 틀 | 구조적 적합성<br>경로 알려짐 = 결정론 · 경로 열림 = agent |
| 자율성 정당화 | 모델이 경로를 골라야 하는 곳에서만 |

<sub>근거: CCAR-F-Amey-Thakur-0011, CCAR-F-Amey-Thakur-0016, CCAR-F-Amey-Thakur-0051, CCAR-F-Udemy04-0028, CCAR-P-Amey-Thakur-0005, CCAR-P-Amey-Thakur-0045, CCAR-P-jrajath94-0013, CCAR-P-jrajath94-0018, CCAR-P-jrajath94-0117, CCAR-P-jrajath94-0118, CCAR-P-jrajath94-0337, CCAR-P-jrajath94-0400, CCAR-P-jrajath94-0463</sub>

@@ ADD-TO: ### 1.3 Coordinator(orchestrator) 1개 + Subagent n개 구조

**과분해(over-decomposition)**

| 상황 | 판단 |
|---|---|
| 작은 작업 · 한 영역 · context 하나에 수용 | subagent 분해 ✗<br>격리 이득 없이 orchestration 비용만 증가 |
| 개선 방향 | 단일 모델 호출<br>+ 필요 시 가벼운 검증 단계 |
| 각 단계가 앞 단계 출력을 필요로 하는 chain | 병렬 실행 부적합 |
| 지연 · 비용의 원인 | 설계 자체<br>→ 큰 모델 교체 · 출력 cache로 해소 ✗ |

**Super-agent 분해 · 소유권**

| 구분 | 내용 |
|---|---|
| 문제 | 단일 loop + 공유 memory<br>→ 실패 원인 귀속 · 독립 평가 · 독립 배포 불가 |
| 분해 | 경계 있는 agent(RAG · search · analytics)<br>+ 명시적 입력/출력 계약 |
| orchestrator | 얇게 유지<br>(또 하나의 super-agent ✗) |
| 소유권 | 팀별로 agent + eval 세트 소유<br>실패 = 계약을 위반한 agent에 귀속 |
| 독립 배포 | 계약을 별도 버전 관리<br>+ agent별 eval 스위트로 릴리스 gate<br>→ 한 팀 변경이 다른 팀 부분을 조용히 파손 ✗ |

<sub>근거: CCAR-F-preporato-0011, CCAR-P-jrajath94-0070</sub>

@@ ADD-TO: ### 1.5 Loop 종료, 안전장치, 상태

**상태 설계 진단 · 복구**

| 상황 | 판단 |
|---|---|
| 같은 인자로 비싼 tool 반복 호출 | 결과 보관 · 재사용 실패 = 상태 설계 문제<br>정상 재시도 ✗ |
| crash 후 worker가 확인된 사실 · 판단 소실<br>(filesystem 비공유 · 로컬 JSONL 보존 불확실) | 사실 · 판단을 JSON state manifest로 영속화<br>→ 재시작 시 prompt에 주입 |
| host를 넘어 session 재개 | 공유 스토리지로 mirror 필요<br>(`SessionStore` adapter) |
| 복구 수단의 기준 | 실행 환경에 의존하지 않는 앱 정의 state |

**Loop 제어 책임**

| 구분 | 내용 |
|---|---|
| loop 담당 | Agent SDK = SDK<br>Messages API 직접 구현 = 개발자 |
| 반복 상한 | 폭주 방지 안전장치 · 충분히 큰 값<br>주된 중지 조건으로 사용 = 안티패턴 |

<sub>근거: CCAR-F-Amey-Thakur-0066, CCAR-F-Udemy02-0036, CCAR-F-Udemy04-0028</sub>

@@ NEW-SECTION
### Hybrid 설계 — 고정 뼈대 + 열린 판단
**고정 단계는 코드 · 열린 판단만 모델 · 사이에 gate**

| 구분 | 내용 |
|---|---|
| 분기 규칙 | 입력 형태별 lane 배정<br>고정 매핑 → 결정론적 코드<br>열린 입력 → Claude + gate |
| 구조 | 고정 단계 = deterministic workflow<br>모호한 소수 사례(3~15%) → agent 호출<br>→ 이후 workflow 복귀(지급 · 경고 · 게시) |
| handoff 지점 | workflow ↔ agent 전환 지점 |
| 두 형태 작업<br>(열린 평가 + 고정 발행) | agentic loop로 평가 → 고정 schema<br>→ deterministic workflow로 발행 |
| 연결 조건 | loop 출력 = workflow schema 계약<br>loop = step 상한으로 평가 비용 제한 |
| 정답 형태 | 두 형태 작업의 표준 정답 = hybrid<br>패턴 하나만 고르기 ✗ |

**패턴 스펙트럼 판단 축**

| 축 | 판단 |
|---|---|
| 점수 기준 | 예측 가능성 · 되돌림 가능성<br>오류 비용 · 지연 · 비용 |
| 오류 비용 높음 + 되돌리기 어려움 | 결정론 쪽(스펙트럼 왼쪽)으로 이동 |
| 계획 필요성 높은 단계 (평가 · 조사) | agent |
| 예측 가능성 필요한 단계 (발행 · 지급) | workflow |
| 결정 요인 | 작업의 형태 (구호 ✗) |

**Gate · 사람 검토의 확장성**

| 상황 | 판단 |
|---|---|
| 고정 사례 규칙 처리<br>+ 열린 사례 Claude 처리 | 모든 초안 · 지급에 code gate<br>(원본 대조 · 사진 · 기록 검사 통과 전 차단) |
| gate 입력 | 검사가 원본(메시지 · 사진 · 기록)을 볼 수 있어야 함 |
| 모든 건을 사람이 검토 | 대량엔 불가<br>(12,000건 × 30초 ≈ 하루 100 간호사-시간) |
| 전수 사람 검토가 맞는 경우 | 물량 소량(하루 40~60건)<br>+ 건당 법적 책임 |
| 검사 없는 agent · 최상위 tier | gate 없음 → 오류 비용 한도 위반 |

**비용 절감 = lane 선택**

| 상황 | 정답 |
|---|---|
| 고정 layout 80% + 열린 형식 20%<br>precision 하한 유지 | 고정분 → deterministic parser<br>열린 20% → Claude<br>합계 검사 gate 유지 |
| 절감의 원천 | tier 선택 ✗ · lane 선택 ✓ |
| 새 layout 등장 | parser가 학습할 때까지 Claude로 라우팅 |
| 유지보수 비용 | 양식 변경마다 규칙 세트 · parser 갱신 |
| ⚠️ 수치 | 문항 toy 수치: 월 $540 → $132(약 4배 절감)<br>최상위 tier ≈ Fast tier의 10~14배<br>→ 가격 · tier 구성은 시점에 따라 바뀜 |

**확실한 하위 작업의 결정론적 분리**

| 구분 | 내용 |
|---|---|
| 분리 대상 | 합산 · 평일 검사 등 정답이 확정된 하위 작업 |
| 역할 | 코드 = 계산 · 검증<br>Claude = 검증된 값을 둘러싼 글쓰기 |
| 조건 | 표 형식 계약 필요 (형식 변경 시 script 갱신)<br>글이 숫자를 재계산 ✗ |
| 원리 | 능력 ≠ 확실성<br>→ 확실한 하위 작업 = 코드 |

**쓰기 통제권 유지**

| 구분 | 내용 |
|---|---|
| 고정 단계 + 분류 판단 1회 | 앱 코드가 단계 실행<br>모델 호출 = 분류 1회<br>게시(쓰기) = 앱 코드 |
| 통제권 상실 | 모델이 직접 게시<br>(MCP connector · 네트워크<br>· server-executed tool) |
| agent loop의 대가 | 계획 단계 = 고정 코드에 불필요한 비용 · 변동 |

<sub>근거: CCAR-P-jrajath94-0107, CCAR-P-jrajath94-0110, CCAR-P-jrajath94-0115, CCAR-P-jrajath94-0118, CCAR-P-jrajath94-0126, CCAR-P-jrajath94-0282, CCAR-P-jrajath94-0284, CCAR-P-jrajath94-0336, CCAR-P-jrajath94-0399, CCAR-P-jrajath94-0462, CCAR-P-jrajath94-0521, CCAR-P-jrajath94-0525, CCAR-P-jrajath94-0602</sub>

@@ NEW-SECTION
### 구조적 통제 · gate 위치 · trust boundary
**보장이 필요하면 prompt가 아닌 구조로 강제**

| 요구 | 구조적 수단 |
|---|---|
| 지어낸 거절 이유 0건<br>(내부 agent → 가입자 대상 확대) | 결정론 단계가 실제 decision record 조회<br>모델 = 기록 바꿔 말하기만<br>자체 이유 제시 ✗ |
| 테넌트 간 데이터 격리<br>(통제 = 강제 가능) | tenant별 session context(아키텍처 계층)<br>tenant 범위 credential · 필터된 tool 접근<br>모델 밖 data partitioning |
| 격리 효과 | 다른 tenant 데이터에 도달 불가<br>→ prompt 실패로도 유출 ✗ |
| 원칙 | prompt 지시 = 권고적 · 우회 가능<br>보안 경계로 검증 불가 |
| 확대 위험 | 내부용 agent는 제약된 적 없음<br>외부 대상 확대 = 위험 상승 → 방어 장치 추가 |

**Gate 위치와 강도**

| 구분 | 내용 |
|---|---|
| 위치 | 모델 출력 뒤 · 부수 효과 앞<br>(발송 · 지급 · 공지 · 수여) |
| 되돌릴 수 없음 + 중대 | 효과 전 사람 검토<br>검토자가 제안 · 증거 · system of record를<br>한 화면에서 확인 |
| 되돌릴 수 있음 | 코드 검사 유지<br>(자격 입력 vs 원본 문서 대조) |
| 대외적 난처함 위험 | 코드 검사 + 사람 표본 검토 |
| 검토 SLA | gate가 실제 긴급 대응을 지연 ✗ 하도록 설정 |
| 원칙 | 검토 강도 = 결과 중대성 · 되돌림 가능성에 비례 |

**Trust boundary**

| 구분 | 내용 |
|---|---|
| 경계 ① | 신뢰할 수 없는 입력이 들어오는 지점<br>(폭언 · 조작 가능 채팅 → 검증 단계) |
| 경계 ② | 모델 출력이 부수 효과로 나가는 지점<br>(티켓 쓰기 = 코드에서 권한 부여) |
| 경계 아님 | 내부 구간<br>(logger → disk · 순수 함수 사이<br>· system of record 읽기 → 모델) |
| system of record | 신뢰 출처 · 점검 기준 |
| 파이프라인 순서 | 입력 → 검증 → context 조립 → 모델<br>→ 검증 → 부수 효과 → 피드백 |

<sub>근거: CCAR-P-jrajath94-0065, CCAR-P-jrajath94-0069, CCAR-P-jrajath94-0283, CCAR-P-jrajath94-0523, CCAR-P-jrajath94-0524</sub>

@@ NEW-SECTION
### Session — continue · resume · fork
**이어가기 = resume · 갈라서 시도 = fork**

| 옵션 | 동작 | 용도 |
|---|---|---|
| continue<br>`continue_conversation=True`<br>`claude --continue` | 현재 디렉터리의<br>최신 session 재개 | 최신이 곧 대상일 때<br>분기 원본 보장 ✗ |
| resume<br>`resume=<id>`<br>`claude --resume <name>` | session ID(또는 이름)<br>지정 재개 | 이어가기<br>복귀 사용자의 history 복원 |
| fork<br>`fork_session=True`<br>`--fork-session` · `/branch` | 원본 이력 복사한 새 session<br>새 session ID<br>원본 ID · 이력 불변 | 같은 시점에서 독립 탐색<br>나중에 어느 쪽으로든 복귀 |

**Fork 운용**

| 구분 | 내용 |
|---|---|
| 분기 원본 | 완료 시점 session ID 기록<br>→ 각 분기 worker에 전달 |
| 분기 후 | 새로 생성된 session ID 추적 → 나중에 재개 |
| 분기 대상 | 대화 이력만 (파일 시스템 ✗) |
| 파일 수정이 겹침 | 별도 작업 복사본(git worktree 등) 병행 |
| file checkpoint | 파일 변경 되돌림 기능<br>대화 분기 수단 ✗ |
| 복귀 사용자 + 관리자 실험 | 사용자 = resume (history 복원)<br>관리자 = fork (실험이 원본에 불반영) |

**Resume vs 새 session + 요약**

| 상황 | 선택 |
|---|---|
| 이전 context 대체로 유효<br>(변경 미미) | resume |
| 일부 파일만 변경 (예: 25개 중 3개) | resume + 변경 파일을 구체적으로 전달<br>→ 범위 좁힌 재분석 |
| 대규모 변경 (분석 파일의 약 40~65% 변경) | 확인된 결론만 구조화 요약<br>→ 새 session에 주입 |
| 구분 이유 | session = 대화 저장 · 파일 시스템 ✗<br>이력 속 tool 결과가 현재 코드와 어긋남 |
| 요약의 이점 | 유효한 결론만 이어받음<br>낡은 관찰을 현재 코드로 취급 ✗ |
| 판단 축 | 재개한 문맥을 신뢰할 수 있는가 |
| 변경 목록 확보 | `git diff --name-only` 등으로 전달 → 누락 방지 |

**Claude Code 이름 붙인 session**

| 구분 | 내용 |
|---|---|
| 상황 | 며칠에 걸친 병행 조사 여러 개 |
| 이름 붙이기 | 시작 시 `claude -n` · session 중 `/rename` |
| 재개 | `claude --resume <name>`<br>(이름 = 조사 내용을 알 수 있게) |
| `--continue` 한계 | 최신 session만 선택<br>→ 병행 조사에서 엉뚱한 session이 열림 |

<sub>근거: CCAR-F-Udemy02-0037, CCAR-F-Udemy02-0043, CCAR-F-Udemy03-0012, CCAR-F-Udemy04-0031, CCAR-F-Udemy04-0055, CCAR-F-Udemy05-0014, CCAR-F-Udemy05-0027, CCAR-F-Udemy06-0027, CCAR-F-Udemy06-0059, CCAR-F-preporato-0004</sub>

@@ NEW-SECTION
### Agent SDK — subagent 위임 구성 · 권한
**위임 = subagent 정의 + `Agent` tool 허용**

| 구분 | 내용 |
|---|---|
| 전제 ① 위임 대상 | `agents` 파라미터(`AgentDefinition`)<br>또는 `.claude/agents/` 파일로 정의 |
| 전제 ② 위임 수단 | `allowedTools`(`allowed_tools`)에 `Agent` 포함 |
| 증상 | coordinator가 호출 없이 직접 수행<br>→ 전제 ①② 확인 |
| description | Claude가 위임 대상을 고르는 근거<br>추상적("조사를 돕는다") → 위임 ✗ · 오선택 |
| 모니터링 | 로그에서 `Agent` tool_use 발행 · 선택된 subagent 확인 |
| ⚠️ tool 이름 | 공식 문서: `tool_use` 블록 = `Agent`<br>v2.1.63 이전 · `system:init` 목록 = `Task`<br>→ 시점에 따라 바뀜 · 감지 시 둘 다 매칭 |

**AgentDefinition 필드**

| 필드 | 역할 |
|---|---|
| `description` | 어떤 작업을 어느 subagent에 맡길지 판단하는 재료 |
| `prompt` | subagent의 역할 |
| `tools` | subagent별 사용 가능 tool 범위 |

**권한 평가 순서와 설정 범위**

| 구분 | 내용 |
|---|---|
| 평가 순서 | hook → deny rule → ask rule<br>→ permission mode → allow rule<br>→ `canUseTool` callback |
| 미결 호출 | `canUseTool`로 이동<br>callback이 결정 못하면 대화형 확인 → 무인 실행 중단 |
| 최상위 `allowedTools` | 승인 없이 실행할 tool 목록(allow rule)<br>제한 수단 ✗ |
| 최상위 `disallowedTools` | session 전체에 적용<br>subagent 간 권한 분리 ✗ |
| `AgentDefinition.tools` | subagent 단위 제한 ✓ |
| `permissionMode: acceptEdits` | 편집 계열 승인만 생략 → 위임 승인과 무관 |
| `bypassPermissions` | 승인 생략 · tool 무제한 허용<br>위임 대상 제공 ✗ |
| `tool_choice` | 호출 tool 고정<br>위임 대상 제공 ✗ |
| worker `tools`의 `Agent` | 중첩 위임용 · 최초 위임과 무관 |

**무인 실행이 위임에서 멈출 때**

| 상황 | 정답 |
|---|---|
| 자동 승인 = Read · Grep · Glob뿐<br>첫 위임 시도에서 권한 확인 대기 | coordinator `allowedTools`에 위임 tool 추가<br>+ 위임 호출을 승인하는 `canUseTool` callback |
| ⚠️ 위임 tool 이름 | 문항은 v2.1.63 이전 설정 기준 `Task`<br>현행 = `Agent` |

**최소 권한 · 역할 분리**

| 상황 | 정답 |
|---|---|
| 용도별 분배 + 문서용만 읽기 전용 | `agents` map에 subagent별<br>`description` + `prompt`<br>문서용 `tools` = 읽기 계열만 |
| 통합 agent가 역할 밖 광범위 검색 | 역할별 tool 제한<br>추가 조회는 coordinator 경유 |
| 원칙 | 예상 밖 행동이 반복되면 지시 강화 전에<br>권한 · tool 부여 방식 재검토 |
| 근거 | tool을 쓸 수 있는 상태에서 말로 유도 = 확률적<br>(문서 리뷰 subagent에 Read · Grep만 부여) |

<sub>근거: CCAR-F-Udemy01-0059, CCAR-F-Udemy02-0038, CCAR-F-Udemy02-0042, CCAR-F-Udemy03-0038, CCAR-F-Udemy06-0002</sub>

@@ NEW-SECTION
### Agent SDK hook — tool 결과 제어 (PostToolUse)
**tool 결과 변환 = PostToolUse + `updatedToolOutput`**

| 필드 · 시점 | 동작 |
|---|---|
| `updatedToolOutput` | 출력 교체 (Claude가 보기 전)<br>MCP tool 포함 |
| `additionalContext` | tool 결과에 정보 덧붙임만 |
| `decision: "block"` | 이유 첨부만<br>Claude는 원래 출력을 계속 봄 |
| PostToolUse | tool 결과가 반환된 시점에 동작 |
| PreToolUse | 호출 전 동작<br>→ 돌아오는 결과 형식 변경 ✗ |
| 구분 요령 | 필드가 교체 · 덧붙임 · 멈춤 중 무엇인지 확인 |

**tool 결과 정규화**

| 상황 | 정답 |
|---|---|
| 여러 MCP tool 출력 형식 혼재<br>(timestamp · ISO 8601 · status code)<br>+ 수정 불가 third-party server | PostToolUse hook으로 정규화<br>= 중앙 집중 · 결정적 · 모든 출력에 일관 적용 |
| 수정 가능한 자사 MCP server | 구현에서 정규화도 유효 (발생원 수정) |
| prompt에 형식 설명 · 변환표 | 오류 감소 ✗<br>변환 여부가 모델에 의존 |
| `normalize_data` tool을 agent가 호출 | 호출 · 변환이 LLM 의존 → 유지보수 열세 |
| 외부 server에 PreToolUse로 형식 지정 | 결과 형식 변경 ✗ · server 형식 변경 불가 |
| 운영 팁 | 정규화 전 값도 로그 보존 → 변환 오류 사후 검증 |

**모델에 전달 금지 항목 (PII)**

| 구분 | 내용 |
|---|---|
| 요구 구분 | "답변에 안 낸다" = 출력 제어<br>"모델에 안 전달한다" = 입력 차단 |
| 정답 수단 | PostToolUse `updatedToolOutput`으로 항목 제거<br>또는 MCP server 응답에서 항목 제외 |
| matcher | `mcp__{서버명}__{tool명}`으로 대상 tool 한정<br>→ 다른 tool 결과 영향 ✗ |
| 감사 지적 = "입력에 포함" | prompt 강화로 해결 ✗ |

<sub>근거: CCAR-F-MyPractice-0059, CCAR-F-Udemy02-0017, CCAR-F-Udemy04-0002, CCAR-F-Udemy05-0038, CCAR-F-paullarionov-0059</sub>

@@ RULES

| 상황 | 정답 |
|---|---|
| 순서 고정 · 입력 일정 · 규칙 알려짐 | deterministic 구현<br>모델은 모호한 부분에만 |
| 고정 경로 + 열린 단계 1개 | augmented LLM (도구 가진 workflow)<br>loop 통제 불필요 |
| 검색 1회 + 판단 1회로 종결 | augmented single call |
| 단계를 실행 전엔 모름<br>각 발견이 다음 단계 결정 | agentic loop + step 상한 · 중지 규칙 |
| 같은 순서 · 같은 trace 요구 | deterministic workflow |
| 고정 단계 + 소수(3~15%) 모호 사례 | hybrid<br>(workflow → agent 호출 → workflow 복귀) |
| 열린 평가 + 고정 형식 발행 | agentic loop → schema 계약 → workflow 발행 |
| 고정 사례 + 열린 사례 혼재<br>+ 비용 · 안전 제약 | 고정 = 규칙 · 열린 = Claude<br>모든 출력 code gate |
| 비용 절감 + precision 하한 | lane 분기 (tier 상향 ✗) |
| 정확해야 하는 합계 · 날짜 규칙 | 코드로 분리<br>Claude = 검증된 값 둘러싼 글쓰기 |
| 쓰기 통제권 유지 | 앱 코드가 쓰기 · 모델은 판단 1회 |
| 작은 작업에 subagent 다수<br>→ 느리고 비쌈 | 단일 호출 + 가벼운 검증으로 축소 |
| 여러 팀 소유 super-agent<br>→ 실패 귀속 불가 | 경계 agent + 계약 + 얇은 orchestrator<br>+ agent별 eval · 버전 관리 |
| 지어낸 설명 · tenant 유출 0건 요구 | 구조적 통제<br>(결정 기록 조회 · tenant 범위 credential) |
| 되돌릴 수 없는 부수 효과 | 효과 전 사람 검토 (전체 context 제공) |
| 되돌릴 수 있음 + 대외적 난처함 | 코드 검사 + 사람 표본 검토 |
| trust boundary 위치 | 비신뢰 입력 진입점 · 모델 → 부수 효과 지점 |
| 돌아온 사용자의 대화 이어가기 | resume |
| 같은 시점에서 독립 탐색 · 원본 불변 | resume + fork 옵션<br>+ 새 session ID 추적 |
| fork 분기에서 파일도 독립 | 별도 작업 복사본 · checkpoint로 되돌림 |
| 이전 분석 유효 + 일부 파일 변경 | resume + 변경 파일 구체 전달 |
| 대규모 변경 후 재개 | 구조화 요약 → 새 session |
| Claude Code 병행 조사 여러 개 | `/rename` → `claude --resume <name>` |
| crash 복구 · 로컬 session 보존 불확실 | JSON state manifest 영속화 · 재시작 시 주입 |
| coordinator가 subagent에 위임 ✗ | `agents` 정의 + `allowedTools`에 `Agent`<br>+ 구체적 `description` |
| 무인 실행이 위임 승인 대기에서 정지 | `allowedTools`에 위임 tool<br>+ `canUseTool` callback |
| subagent별 권한 분리 · 읽기 전용 | `AgentDefinition.tools` |
| agent가 역할 밖 행동 반복 | 역할별 tool 제한 · 추가 조회는 coordinator 경유 |
| 서로 다른 형식의 tool 결과 정규화 | PostToolUse hook + `updatedToolOutput` |
| 모델에 금지 항목 전달 금지 | PostToolUse로 제거 또는 server 응답에서 제외 |

<sub>근거: CCAR-F-Amey-Thakur-0011, CCAR-F-Amey-Thakur-0016, CCAR-F-Amey-Thakur-0051, CCAR-F-Amey-Thakur-0066, CCAR-F-MyPractice-0059, CCAR-F-Udemy01-0059, CCAR-F-Udemy02-0017, CCAR-F-Udemy02-0036, CCAR-F-Udemy02-0037, CCAR-F-Udemy02-0038, CCAR-F-Udemy02-0042, CCAR-F-Udemy02-0043, CCAR-F-Udemy03-0012, CCAR-F-Udemy03-0038, CCAR-F-Udemy04-0002, CCAR-F-Udemy04-0028, CCAR-F-Udemy04-0031, CCAR-F-Udemy04-0055, CCAR-F-Udemy05-0014, CCAR-F-Udemy05-0027, CCAR-F-Udemy05-0038, CCAR-F-Udemy06-0002, CCAR-F-Udemy06-0027, CCAR-F-Udemy06-0059, CCAR-F-paullarionov-0059, CCAR-F-preporato-0004, CCAR-F-preporato-0011, CCAR-P-Amey-Thakur-0005, CCAR-P-Amey-Thakur-0045, CCAR-P-jrajath94-0013, CCAR-P-jrajath94-0018, CCAR-P-jrajath94-0065, CCAR-P-jrajath94-0069, CCAR-P-jrajath94-0070, CCAR-P-jrajath94-0107, CCAR-P-jrajath94-0110, CCAR-P-jrajath94-0115, CCAR-P-jrajath94-0117, CCAR-P-jrajath94-0118, CCAR-P-jrajath94-0126, CCAR-P-jrajath94-0282, CCAR-P-jrajath94-0283, CCAR-P-jrajath94-0284, CCAR-P-jrajath94-0336, CCAR-P-jrajath94-0337, CCAR-P-jrajath94-0399, CCAR-P-jrajath94-0400, CCAR-P-jrajath94-0462, CCAR-P-jrajath94-0463, CCAR-P-jrajath94-0521, CCAR-P-jrajath94-0523, CCAR-P-jrajath94-0524, CCAR-P-jrajath94-0525, CCAR-P-jrajath94-0602</sub>

@@ TRAPS

| 오답 | 이유 |
|---|---|
| 규칙 고정 작업에 agent<br>(미래 유연성 · step 한도<br>· 관심사 분리 multi-agent) | 필요 없는 비용 그대로<br>비결정성만 추가 |
| agent 3개가 순서를 협상 | 고정 순서에 비결정성만 추가<br>과잉 설계 |
| tool을 쓰니 agentic | 기준 = 단계를 누가 정하나<br>고정 경로 = 도구 가진 workflow |
| 순차 3단계 → agent 3개 | 순차 단계 ≠ agent<br>orchestration overhead만 추가 |
| 모든 리뷰 코멘트를 사람이 승인 | 자동화 목표 무력화 · 설계가 요구 ✗ |
| workflow 선택 이유 = agent는 새롭고 덜 검증<br>· workflow는 항상 정확<br>· 팀 시간 부족 | 엔지니어링 근거 아님<br>근거 = 경로가 알려졌는가 |
| 열린 연구를 고정 10단계 workflow로 | 실행 전에 없는 단계는 나열 불가 |
| 열린 연구를 검색 10회 담은 prompt 1개 | 의외의 발견 시 재계획 지점 없음 |
| 정해진 도구 순서에 분기만 추가 | 결정 트리만 커짐<br>질문마다 필요 절차가 다름 |
| 반복 5회 고정 후 답변 | 상한 = 안전장치<br>주된 중지 조건 ✗ |
| 과분해 pipeline → 큰 모델 교체<br>· subagent 병렬화 · 출력 cache | 병렬화 = chain에 부적합<br>cache = 같은 질문 반복에만 이득<br>설계 비용은 그대로 |
| super-agent에 label 붙은 memory 섹션 | 소유권 · 독립 평가 생성 ✗<br>귀속 = 여전히 의견 문제 |
| 릴리스마다 각 팀이 전체 prompt 공동 검토 | 팀 결합 → 독립 배포와 정반대 |
| 환각 감소용 더 큰 모델로 라우팅<br>(bigger-model 함정) | 실패는 아키텍처 문제 · 용량 ✗ |
| system prompt에 규제 주의 · 예시 보강<br>(prompt-plea) | 우회 가능 · 검증 불가<br>컴플라이언스 위험 |
| 내부 agent가 가입자 질문에 직접 응답 | 방어 장치 없이 위험만 상승 |
| 두 번째 agent가 유출을 검토 | 검토자도 모델: 놓침 · 속음<br>비용 · 지연 2배 |
| 교차 tenant 접근 로깅 | 유출 후 탐지 · 방지 ✗ |
| 사람이 모든 건 검토 | 대량엔 불가<br>triage 실패는 그대로 남음 |
| 검사 없는 agent · 최상위 tier 일괄 처리 | gate 없음<br>tier 일괄 = 예산 위반 · 고정 건에도 agent 비용 |
| 모든 호출에 explicit reasoning | 기준 충족 상태에서 출력 token · 지연만 추가 |
| 가변 꼬리까지 대화 전체 cache | prefix 불안정 → hit rate ≈ 0<br>write 비용은 계속 청구 |
| few-shot · 큰 tier · 2차 Claude 호출로 산술 보장 | 모두 샘플링 → 보장 ✗ |
| 정확도가 높으니 검토 생략 | 정확도 = 지표<br>지표는 부수 효과를 gate ✗ |
| 원시 입력 단계 검토 | 판단할 제안이 없음 |
| 되돌릴 수 없는 행동 뒤 사후 검토 | 피해 이후 |
| trust boundary = logger · 순수 함수 사이 | 내부 구간 |
| fork 대신 같은 session resume 2회 · 동시 resume | 하나의 이력 공유 → 독립성 ✗ |
| `continue`로 분기 | 최신 session 선택 → 분기 원본 보장 ✗ |
| 분기마다 새 session에서 분석 반복 | 분석 공유 소실 |
| file checkpoint로 대화 이력 분기 | checkpoint = 파일 되돌림 |
| fork가 파일도 분기 | 대화 이력만 분기 |
| 변경 후 session 그대로 resume + 변경 미언급 | 낡은 tool 결과를 현재 코드로 취급 |
| 일부 변경에도 25개 전체 재분석 | 과도한 재작업<br>변경분만 전달해 좁힘 |
| "최신 상태 확인하고 계속" 같은 모호한 지시 | 전체 재탐색 유발 |
| 요약 이유 = resume이 기록 덮어씀<br>· 이력 자동 압축 | resume 동작에 대한 오해 |
| 병행 조사 재개를 `--continue` + `/clear` | `/clear`는 session 전환 ✗ |
| `--continue --fork-session`<br>· CLAUDE.md 진행 기록 + 새 session | fork = 분기 생성 · 유효한 context 폐기 |
| crash 복구 = system prompt 강화 | 잃은 정보를 못 되찾음 |
| crash 복구 = `continue` · 로컬 JSONL 복사 | filesystem 비공유 · 재시작 후 보존 불확실 |
| 위임 안 됨 → `bypassPermissions` · `tool_choice` | 위임 대상 제공 ✗ |
| 위임 안 됨 → 지시를 coordinator prompt로 이식<br>· subagent prompt에 부모 이력 참조 | multi-agent 포기 · 이력 상속 오해 |
| `acceptEdits` · worker `tools`에 `Agent` | 편집 승인 전용 · 중첩 위임 전용 |
| 최상위 `allowedTools`로 제한<br>· `disallowedTools`로 subagent별 분리 | 승인 생략 목록 · session 전체 적용 |
| tool 이름 변경 · few-shot · 금지 prompt<br>(역할 이탈 방지 목적) | tool 접근 가능 상태 → 확률적 |
| 정규화에 `additionalContext`<br>· `decision: "block"` | 덧붙임 · 이유 첨부만 → 원래 출력 유지 |
| 정규화 · 마스킹에 PreToolUse | 호출 전 동작 → 결과 형식 변경 ✗ |
| PII 금지를 system prompt 강조 · few-shot | 출력 제어 · 확률적<br>모델 입력엔 이미 포함 |
| PII 해결로 PreToolUse에서 tool 호출 전면 거부 | 필요한 정보까지 소실 |

<sub>근거: CCAR-F-Amey-Thakur-0011, CCAR-F-Amey-Thakur-0016, CCAR-F-Amey-Thakur-0051, CCAR-F-Amey-Thakur-0066, CCAR-F-Udemy01-0059, CCAR-F-Udemy02-0017, CCAR-F-Udemy02-0036, CCAR-F-Udemy02-0037, CCAR-F-Udemy02-0042, CCAR-F-Udemy02-0043, CCAR-F-Udemy03-0012, CCAR-F-Udemy03-0038, CCAR-F-Udemy04-0002, CCAR-F-Udemy04-0028, CCAR-F-Udemy04-0031, CCAR-F-Udemy04-0055, CCAR-F-Udemy05-0014, CCAR-F-Udemy05-0027, CCAR-F-Udemy05-0038, CCAR-F-Udemy06-0002, CCAR-F-Udemy06-0027, CCAR-F-Udemy06-0059, CCAR-F-preporato-0004, CCAR-F-preporato-0011, CCAR-P-Amey-Thakur-0005, CCAR-P-Amey-Thakur-0045, CCAR-P-jrajath94-0013, CCAR-P-jrajath94-0018, CCAR-P-jrajath94-0065, CCAR-P-jrajath94-0069, CCAR-P-jrajath94-0070, CCAR-P-jrajath94-0107, CCAR-P-jrajath94-0110, CCAR-P-jrajath94-0115, CCAR-P-jrajath94-0117, CCAR-P-jrajath94-0126, CCAR-P-jrajath94-0282, CCAR-P-jrajath94-0283, CCAR-P-jrajath94-0523, CCAR-P-jrajath94-0524, CCAR-P-jrajath94-0602</sub>

@@ MEMO

| 이름 | 의미 |
|---|---|
| augmented LLM · augmented single call | 도구 가진 단일 판단<br>(고정 경로 + 열린 1단계) |
| hybrid | workflow ↔ agent를 오가는 구조<br>(전환 지점 = handoff) |
| lane | 입력 형태별 처리 경로 (규칙 · Claude) |
| code gate | 부수 효과 앞에서 코드로 검사 |
| prompt-plea | 보장을 prompt 지시에 의존하는 함정 |
| bigger-model 함정 | 구조 문제를 큰 모델로 해결하려는 오답 |
| system of record | 신뢰 출처 DB · 점검 기준 |
| trust boundary | 비신뢰 입력 진입점 · 모델 출력의 부수 효과 지점 |
| `continue_conversation` · `--continue` | 현재 디렉터리 최신 session 재개 |
| `resume` · `claude --resume <name>` | ID · 이름 지정 재개 |
| `fork_session` · `--fork-session` · `/branch` | 이력 복사한 새 session 생성 (원본 불변) |
| `claude -n` · `/rename` | session 이름 부여 |
| file checkpointing | 파일 변경 되돌림 (대화 분기 ✗) |
| state manifest | 확인된 사실 · 판단을 담은 JSON 영속 state |
| `agents` 파라미터 | `AgentDefinition` map으로 subagent 정의 |
| `Agent` tool (구 `Task`) | subagent 위임 tool |
| `AgentDefinition` `description` · `tools` | 위임 판단 근거 · subagent별 tool 제한 |
| `allowedTools` · `disallowedTools` | 승인 생략 목록 · session 전체 차단 목록 |
| `canUseTool` callback | 앞 단계에서 결정 안 된 호출의 승인 판단 |
| `PostToolUse` · `PreToolUse` | tool 결과 반환 시점 · 호출 전 hook |
| `updatedToolOutput` | tool 출력을 Claude가 보기 전에 교체 |
| `additionalContext` | tool 결과에 정보 덧붙임 |

<sub>근거: CCAR-F-Udemy01-0059, CCAR-F-Udemy02-0017, CCAR-F-Udemy02-0036, CCAR-F-Udemy02-0037, CCAR-F-Udemy02-0038, CCAR-F-Udemy02-0042, CCAR-F-Udemy02-0043, CCAR-F-Udemy03-0012, CCAR-F-Udemy04-0002, CCAR-F-Udemy04-0031, CCAR-F-Udemy06-0002, CCAR-F-paullarionov-0059, CCAR-P-jrajath94-0018, CCAR-P-jrajath94-0065, CCAR-P-jrajath94-0069, CCAR-P-jrajath94-0283, CCAR-P-jrajath94-0336, CCAR-P-jrajath94-0399, CCAR-P-jrajath94-0524</sub>

@@ CHECK

- [ ] 고정 뼈대 + 소수 모호 사례 = hybrid (lane 분기)
- [ ] 0건 보장 요구 = 구조적 통제 · 부수 효과 앞 gate
- [ ] 이어가기 resume · 분기 fork · 큰 변경은 요약 + 새 session
- [ ] 위임 안 됨 = `Agent` 허용 확인 · 결과 교체 = PostToolUse

<sub>근거: CCAR-F-Udemy02-0017, CCAR-F-Udemy03-0012, CCAR-F-Udemy06-0002, CCAR-P-jrajath94-0065, CCAR-P-jrajath94-0336</sub>
