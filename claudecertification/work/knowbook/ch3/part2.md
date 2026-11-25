@@ ADD-TO: Hooks: 결정론적 실행

**exit code · 반환값별 효과**

| hook · 반환 | 효과 |
|---|---|
| `PreToolUse` + exit 2 | 호출 차단<br>stderr(또는 JSON 거부 사유) → Claude 전달 |
| `PreToolUse` + exit 0 + 경고 출력 | 차단 ✗ → 호출 계속 |
| JSON `permissionDecision: allow` | 경고와 함께 실행 허용 → 차단 ✗ |
| `PostToolUse` + exit 2 | 이미 실행됨 → 쓰기 취소 ✗<br>stderr → Claude 전달 → 후속 대응 가능 |
| `Stop` + exit 2 | Claude 종료 ✗<br>stderr 전달 → 실패 테스트 계속 수정 |
| `SessionEnd` | 세션 닫히는 시점 실행 → 막을 대상 없음 |
| `UserPromptSubmit` | prompt 제출 시점 → 작업 전에 실행 |

**hook 시점 선택**

| 요건 | 정답 |
|---|---|
| 수정 직후 팀 전체 Prettier | `PostToolUse` + matcher `Edit\|Write`<br>commit된 `.claude/settings.json`에 정의 |
| 테스트 실패 중 작업 종료 금지 | `Stop` + 실패 시 stderr 출력 + exit 2 |
| 쓴 파일에서 API key 발견 | `PostToolUse` = 사후 대응만<br>(파일 이미 존재 · 쓰기 취소 ✗) |
| 쓰기 자체 차단 | `PreToolUse`에서 검사 → exit 2 |

**강제 수단 선택**

| 요건 | 정답 |
|---|---|
| 정해진 시점 · 모델 무관 · deterministic 동작 | hook<br>(지침 · context = project memory<br>모델 선택 = 설정) |
| 권한 규칙으로 표현 불가한 shell 검사 | `PreToolUse` + shell matcher<br>검사 실패 시 exit 2 |
| workspace 밖 경로 명령 차단 + 위반 피드백 | `PreToolUse` 경로 검증<br>→ 이유 포함 차단 |
| 필수 순서 (대상 확인 → 상태 변경) | `PreToolUse` 전제 gate<br>확인 기록 전까지 Bash 거부 |
| 필수 순서 (tool 설계) | 상태 변경 전용 tool<br>확인된 ID 필수 입력 + 불일치 호출 거부 |
| API key commit 방지 | pre-commit hook = diff 스캔<br>일치 시 commit 차단 · fail closed |

**pre-commit secret 스캔의 조건 · 한계**

| 구분 | 내용 |
|---|---|
| 시점 | 이력에 들어가기 전 차단<br>(merge 이후 스캔 = 포렌식 · 백스톱) |
| fail closed | scanner 고장 → 통과 ✗ · 차단 |
| 패턴 목록 | 새 키 형식 누락 가능 → 담당자 필요 |
| 유출 발생 시 | 키 교체(rotation) 여전히 필요 |

**Bash 출력 정규화 (실행은 그대로)**

| 구분 | 내용 |
|---|---|
| 수단 | `PostToolUse` + matcher `Bash`<br>→ `updatedToolOutput` 반환 |
| 효과 | Claude 전달 전 도구 출력 교체 |
| 값 형태 | 도구 출력 shape 일치<br>Bash = stdout · stderr<br>· interrupted · isImage 객체 |
| 적용 범위 | 성공한 Bash만 교체 · 실패 = 원본 출력<br>(오류 상세 삭제 → 잘못된 전제로 작업) |
| MCP 전용 | `updatedMCPToolOutput`<br>→ 모든 도구용 `updatedToolOutput` 권장 |
| 교체 불가 | `PostToolUse` exit 2 + stderr ✗<br>`PreToolUse` = 실행 전이라 출력 처리 ✗ |

**hook 배포 · 점검**

| 구분 | 내용 |
|---|---|
| 팀 전체 적용 | commit된 `.claude/settings.json`<br>`~/.claude/settings.json` = 설정한 본인만 |
| 로드 확인 | `/hooks` = 현재 session hook 구성 표시<br>읽기만 → 파일 변경 ✗ |
| 점검 수단 ✗ | `CLAUDE.md` 안내 줄 = hook 시작 ✗<br>`/context` = hook match · exit code 목록 ✗ |

<sub>근거: CCAR-F-Amey-Thakur-0021, CCAR-F-Amey-Thakur-0057, CCAR-F-Udemy01-0002, CCAR-F-Udemy01-0024, CCAR-F-Udemy03-0036, CCAR-F-preporato-0017, CCAR-F-preporato-0018, CCAR-F-preporato-0019, CCAR-P-jrajath94-0269, CCAR-P-jrajath94-0678, CCAR-P-jrajath94-0707</sub>

@@ ADD-TO: 구성 요소 구분 (로드 시점 · 작성자)

**배치 판단: `CLAUDE.md` · skill · subagent**

| 상황 | 배치 |
|---|---|
| 모든 session 항상 적용<br>(코딩 표준 · 테스트 규칙) | `CLAUDE.md`<br>(모든 session 로드) |
| 해당 작업 때만 적용<br>(PR 리뷰 · 배포 · migration) | trigger 키워드 지정 skill<br>(Claude가 감지 → on-demand 호출) |
| 새 endpoint 생성 때만 쓰는 예시 2~3개 | skill + slash command 호출<br>→ 메인 context 깨끗하게 유지 |
| 요구 = 재사용할 노하우 · 절차 | skill |
| 요구 = 자체 context의 독립 작업 흐름 | subagent (context 격리) |
| skill vs subagent 선택 기준 ✗ | 작업 길이 · `CLAUDE.md` 유무<br>"skill이 항상 낫다" |

<sub>근거: CCAR-F-Amey-Thakur-0020, CCAR-F-MyPractice-0033, CCAR-F-MyPractice-0038, CCAR-F-paullarionov-0033, CCAR-F-paullarionov-0038</sub>

@@ NEW-SECTION
### Skill · custom command 위치와 공유
**위치가 공유 범위와 우선순위를 결정**

**저장 위치 → 사용 범위**

| 위치 | 범위 |
|---|---|
| 저장소 `.claude/commands/` | 프로젝트 command<br>commit → clone · update한 모두 자동 사용 |
| `~/.claude/commands/` | 개인 command<br>본인 전 프로젝트 · 팀원 ✗ |
| 저장소 `.claude/skills/<이름>/SKILL.md` | 프로젝트 skill<br>저장소와 함께 버전 관리 → 팀 공유 |
| `~/.claude/skills/<이름>/SKILL.md` | 개인 skill<br>본인 전 프로젝트 |
| `.claude/skills/<이름>.md` 단일 파일 | skill로 로드 ✗<br>(폴더 + `SKILL.md` 필요) |
| `.claude/config.json` commands 배열 | command 위치 ✗ |
| `CLAUDE.md` 기재 | 명령으로 호출 ✗ |

**command · skill 관계**

| 구분 | 내용 |
|---|---|
| 통합 | command · skill 동일 취급<br>`.claude/commands/` 파일 계속 사용 가능 |
| 신규 작성 | skill 권장 |
| 보조 파일 | 체크리스트 · 예시 기록<br>→ `SKILL.md`에서 참조 |

**같은 이름 충돌 처리**

| 구분 | 내용 |
|---|---|
| 우선순위 | enterprise > personal > project |
| 결정 기준 | 선언 ✗ · 위치 ✓<br>`override: true` 필드 없음<br>username 조건 로직 없음 |
| 개인 skill = 같은 이름 | 본인에게만 프로젝트 skill 대체<br>저장소 변경 ✗ · 팀원 영향 ✗ |
| 같은 이름의 부작용 | 팀 업데이트 미수신<br>(옛 절차로 계속 실행) |
| 개인 skill = 다른 이름 | 프로젝트 skill과 공존 · 가리지 않음<br>팀 업데이트 계속 수신 |
| 다른 이름의 약점 | `/commit` · `/my-commit` 동시 활성<br>→ 비슷한 `description` → 자동 선택 예측 어려움<br>팀 문서의 `/commit` 안내 · 습관 깨짐 |
| 운영 방침 | 팀 skill 이름 목록 관리<br>개인 skill = 접미사 명명 약속 |

**공유 · 도입 판단**

| 상황 | 방향 |
|---|---|
| 본인만 `/명령` 사용 · 팀원 목록에 없음 | 개인 위치에 있음<br>→ `.claude/commands/`로 이동 + commit |
| 진단 단서 | 본인 환경만 동작<br>저장소 `.claude/`에 commands · skills 없음<br>이름 중복 · 버전 · frontmatter = 설명 ✗ |
| 팀이 반복하는 다단계 검토 절차 | commit한 custom command · skill |
| 공유 skill commit 조건 | 팀이 실제 반복하는 절차 + 코드처럼 리뷰 가능<br>길이 · 작성자 경력 · edge case 포괄 = 근거 ✗ |
| 신입 온보딩<br>(build · test · deploy · API 소유 서비스) | 선별 Skills · slash command<br>+ 저장소 `CLAUDE.md` 문서화<br>→ 시니어 1회 유지 |
| 위키 prompt 복사 · 낡음 | 반복 workflow = 버전 관리 Skills<br>(리뷰 · 테스트 · 코드와 함께 갱신)<br>위키 = 서술형 글 |

<sub>근거: CCAR-F-Amey-Thakur-0042, CCAR-F-Amey-Thakur-0070, CCAR-F-MyPractice-0036, CCAR-F-MyPractice-0041, CCAR-F-Udemy01-0040, CCAR-F-Udemy02-0059, CCAR-F-Udemy03-0026, CCAR-F-Udemy05-0034, CCAR-F-Udemy06-0037, CCAR-F-paullarionov-0036, CCAR-F-paullarionov-0041, CCAR-P-jrajath94-0063, CCAR-P-jrajath94-0106</sub>

@@ NEW-SECTION
### Skill frontmatter 제어
**필드는 요건의 동사로 고른다**

**필드 → 역할**

| 필드 | 역할 |
|---|---|
| `context: fork` | 새 subagent의 독립 context에서 실행<br>대화 이력 ✗ · 결과만 메인 반환 |
| `allowed-tools` | 호출 turn 동안 나열 tool 확인 없이 사용<br>= 사전 승인 (예: `Bash(git log *)`) |
| `disallowed-tools` | skill 활성 동안 tool 풀에서 제거<br>다음 메시지 전송 시 해제 |
| `disable-model-invocation: true` | Claude 자동 로드 차단<br>→ `/이름` 수동 호출만<br>(부작용 workflow 권장) |
| `user-invocable: false` | 반대 방향 = 개발자 호출 차단 |
| `argument-hint` | 자동 완성 시 기대 인수 표시<br>예: `[case-id]` · `[version-tag]`<br>입력 검증 ✗ |
| `description` | Claude의 자동 적용 판단 근거 |
| `model: haiku` | 모델만 변경 → 출력 위치 변화 ✗ |

**해석 차이**

| 구분 | 내용 |
|---|---|
| ⚠️ 시험 가이드 vs 현행 문서 | 시험 가이드 = `allowed-tools`를 접근 제한으로 설명<br>해설(현행 문서) = 사전 승인 · 제한 ✗<br>→ 사양 변경 가능 · 확인 필요 |
| ⚠️ 복합 설정 문항의 `allowed-tools` | 해설 = "파일 쓰기 작업으로 제한"<br>현행 문서 = 제한 ✗ (제한은 `disallowed-tools`)<br>→ 해설과 어긋나 보임 · 확인 필요 |

**증상 → 조치**

| 증상 | 조치 |
|---|---|
| 대용량 분석 출력 → 응답 느려짐<br>· 원래 작업 context 소실 | `context: fork` |
| 수천 줄 출력이 메인 대화를 덮음 | `context: fork`<br>`disable-model-invocation` ✗<br>`allowed-tools` · `model` ✗ |
| 탐색 · 대안 brainstorming이 이후 구현에 영향 | `context: fork`<br>(+ 본문에서 결론 · 추천안 · 비교표만 반환 지시) |
| 이전 대화의 schema 정보 유입 | `context: fork` |
| 인수 없이 실행 → 추측 · 정지 | `argument-hint` + 본문에서 `$0` · `$1` 사용<br>(첫머리: 인수 없으면 입력 요청) |
| 요청만 해도 자동 로드 → 게시 · 배포 | `disable-model-invocation: true` |
| 자동으로 거의 안 쓰임<br>(`description` = "SDS용") | `description`에 확인 내용 + 사용 시점 기재 |
| 실행 중 파일 수정 · shell 금지 | `disallowed-tools:`<br>`Write Edit NotebookEdit Bash` |
| 같은 명령 승인 반복 (`git log`) | `allowed-tools: Bash(git log *)` |
| 메인 밖 실행 + Read · Grep 승인 제거 + 인수 표시 | `context: fork`<br>`allowed-tools: Read Grep`<br>`argument-hint: [case-id]` |
| 인수 누락 + context 누수 + 파괴 동작 | `argument-hint` + `context: fork`<br>+ tool 제한 |

**`context: fork` 주의**

| 구분 | 내용 |
|---|---|
| `/fork`와 다름 | `context: fork` = 이력 없는 새 subagent<br>`/fork` = 현재 대화 이력 전부 상속 |
| 지시 단독 성립 | subagent는 이력 ✗<br>→ 절차를 명시적 task 지시로 유지 |
| 격리 아님 | `/clear` = 필요한 context까지 소실<br>`CLAUDE.md` 이동 = 상시 로드<br>`/compact` = 사후 압축 |
| 요약 지시만 추가 | fork 없으면 실행 위치 그대로 → 해결 ✗ |
| 본문 주의 문구 | "수정 금지" 강조 = 확률적 준수 |
| 확실한 차단 | skill 설정 + permissions deny<br>또는 `PreToolUse` hook<br>(skill 밖 작업까지 대응) |

<sub>근거: CCAR-F-MyPractice-0035, CCAR-F-MyPractice-0039, CCAR-F-MyPractice-0043, CCAR-F-Udemy02-0015, CCAR-F-Udemy02-0041, CCAR-F-Udemy03-0026, CCAR-F-Udemy04-0017, CCAR-F-Udemy04-0026, CCAR-F-Udemy06-0006, CCAR-F-Udemy06-0045, CCAR-F-Udemy06-0047, CCAR-F-paullarionov-0035, CCAR-F-paullarionov-0039, CCAR-F-paullarionov-0043, CCAR-F-preporato-0021</sub>

@@ NEW-SECTION
### Subagent 도구 범위와 위임 설계
**권한은 지시가 아니라 도구 목록으로 제한**

**도구 범위**

| 구분 | 내용 |
|---|---|
| `tools` 필드 | subagent가 쓸 수 있는 도구 제한<br>예: `Read` · `Grep`만 |
| `tools` 생략 | 모든 도구 상속 |
| write 도구 미부여 | 호출 가능한 쓰기 경로 없음<br>→ prompt injection이 유도해도 실행 ✗ |
| 최소 권한 | subagent마다 하위 작업에 필요한 도구만<br>프로덕션 자격 증명 ✗ |
| 결과 처리 | subagent = 조사 결과 반환<br>main agent = 그 결과로 행동 |
| handoff | 결과 schema 필요<br>(없으면 main이 조사 내용 오해석) |
| 한계 | 하위 작업 변화에 따라 목록 유지 필요<br>너무 좁으면 정당한 작업 확장 차단 |

**요건 → 구성**

| 요건 | 정답 |
|---|---|
| 연구 subagent 쓰기 금지 + injection 대비 | `tools: Read, Grep` |
| 메인 context 보호 + 조사 중 편집 차단 | Explore subagent<br>(read-only · Write · Edit 거부 · 요약 반환) |
| 조사 → 구현 다단계 작업 | 조사 = Explore 요약<br>설계 = plan mode → 승인 후 직접 실행 |
| 범용 `/investigate` 명령 | 위임할 조사 = coordinator가 질문별 판단<br>위임 지시 = 목적 · 증거 · 출력 형식 · 범위 경계 |

**위임 설계의 두 축**

| 축 | 내용 |
|---|---|
| 적응성 | 위임 대상 · subagent 수<br>= 질문에 따라 coordinator가 결정<br>고정 절차 ✗ |
| 신뢰성 | 목적 · 요구 증거 · 출력 형식 · 담당 경계를 위임 시 명시<br>제약 없는 폭넓은 조사 ✗ |
| 요약 형태 | Explore 요청 시 돌려받을 형태 지정<br>(컴포넌트 · 사용처 · 제약) → 계획에 바로 사용 |

<sub>근거: CCAR-F-Amey-Thakur-0020, CCAR-F-Udemy03-0052, CCAR-F-Udemy04-0046, CCAR-F-Udemy06-0034, CCAR-P-jrajath94-0261, CCAR-P-jrajath94-0331, CCAR-P-jrajath94-0702</sub>

@@ RULES

| 상황 | 정답 |
|---|---|
| 팀 전체가 호출하는 반복 검토 절차 | commit한 custom command · skill |
| clone한 모두에게 `/review` 제공 | 저장소 `.claude/commands/` + commit |
| 개인 홈 command를 팀원도 사용 | `.claude/commands/`로 이동 + commit |
| 개인 변형으로 팀 skill 대체 · 팀원 영향 ✗ | `~/.claude/skills/<같은 이름>/SKILL.md` |
| 팀 skill 가리지 않기 · 팀 업데이트 수신 | `~/.claude/skills/` 다른 이름 |
| 대용량 출력 · 탐색 context가 메인 오염 | skill `context: fork` |
| 인수 누락 방지 | `argument-hint` + 본문 `$0` · `$1` |
| "확인 없이 쓰게" | `allowed-tools` (사전 승인) |
| "쓸 수 없게" | `disallowed-tools` 또는 permissions deny |
| 부작용 skill 자동 실행 방지 | `disable-model-invocation: true` |
| 항상 적용 + workflow별 지침 혼재 `CLAUDE.md` | 항상 = `CLAUDE.md`<br>workflow별 = trigger 키워드 skill |
| 필수 순서 · 경계 · 금지 | `PreToolUse` gate (+ 상태 변경 전용 tool) |
| 테스트 통과 전 작업 종료 금지 | `Stop` hook + stderr + exit 2 |
| 쓰기 후 팀 전체 포맷 | `PostToolUse` `Edit\|Write` + commit된 설정 |
| Bash 결과만 짧게 정규화 | `PostToolUse` + `updatedToolOutput`<br>(성공 시만) |
| hook 로드 확인 (파일 변경 ✗) | `/hooks` |
| research subagent 쓰기 금지 | `tools: Read, Grep` |
| 조사 context 보호 + 편집 차단 | Explore subagent |
| 조사 → 구현 다단계 | Explore 요약 + plan mode → 승인 후 직접 실행 |
| 범용 `/investigate` | coordinator 위임 판단<br>위임 지시 = 목적 · 증거 · 형식 · 경계 |
| secret commit 방지 | pre-commit 스캔 hook · fail closed |

<sub>근거: CCAR-F-Amey-Thakur-0042, CCAR-F-MyPractice-0033, CCAR-F-MyPractice-0036, CCAR-F-MyPractice-0041, CCAR-F-MyPractice-0043, CCAR-F-Udemy01-0024, CCAR-F-Udemy01-0040, CCAR-F-Udemy02-0059, CCAR-F-Udemy03-0026, CCAR-F-Udemy03-0036, CCAR-F-Udemy03-0052, CCAR-F-Udemy04-0017, CCAR-F-Udemy04-0046, CCAR-F-Udemy06-0006, CCAR-F-Udemy06-0034, CCAR-F-Udemy06-0047, CCAR-F-paullarionov-0033, CCAR-F-paullarionov-0041, CCAR-F-preporato-0017, CCAR-F-preporato-0018, CCAR-F-preporato-0019, CCAR-P-jrajath94-0261, CCAR-P-jrajath94-0269, CCAR-P-jrajath94-0702, CCAR-P-jrajath94-0707</sub>

@@ TRAPS

| 오답 | 이유 |
|---|---|
| `CLAUDE.md` · 시스템 지시로 subagent 편집 금지 | injection이 이미 뚫음<br>`tools` 생략 = 모든 도구 상속 |
| `model` 필드로 subagent 읽기 전용 | 도구 제어 아님 |
| subagent 전체 도구 + 감사 로그 | 편집 뒤 기록뿐 · 파일 이미 변경 |
| subagent 도구 전부 제거 | Read · Grep까지 소실 → 조사 불가 |
| subagent에 main과 같은 도구 | 프로덕션 쓰기 권한 복제 = 범위 최대 |
| 쓰기 도구 주고 "읽기만" 부탁 | 부탁 ≠ 범위 설정 |
| 조사를 권한 있는 main agent에서 수행 | 조사 루프가 쓰기 권한 보유 |
| 범용 subagent + 결과 파일 저장 | context는 보호 · 조사 중 편집 차단 ✗ |
| plan mode만 사용 | 편집 차단 · context 보호 ✗ |
| `/compact` · 자동 압축 | 사후 대응 · 조사 출력이 메인에 남음 |
| 전체 파일을 먼저 Read | 메인 context 소모 |
| 고정된 조사 절차 | 질문별 적응성 ✗ |
| 제약 없는 폭넓은 조사 | 결과 신뢰성 ✗ |
| `PostToolUse` exit 2 = 쓰기 취소<br>(또는 세션 종료 · 무시) | 이미 실행됨<br>stderr → Claude 전달 |
| 경고 출력 + exit 0<br>`permissionDecision: allow` | 차단처럼 보여도 호출 계속 |
| `SessionEnd` · `UserPromptSubmit`<br>읽기 후 `PostToolUse`로 종료 차단 | 시점 불일치 · 종료를 막지 못함 |
| `Edit`에 `PreToolUse`로 Prettier | 수정 전 실행 → 포맷 대상 변경 전 |
| hook을 개인 `~/.claude/settings.json`에 | 설정한 개발자에게만 적용 |
| 로그만 남기는 `PreToolUse` · 사후 되돌리기 요청 | 실행 자체 차단 ✗ |
| 시스템 지시 강화<br>`PostToolUse` 사후 거부로 순서 강제 | 지시 = 이미 실패한 수단<br>사후 검사 = 변경 방지 ✗ |
| `PostToolUse` exit 2로 출력 교체<br>`PreToolUse`에서 stdout 재작성 | 교체는 `updatedToolOutput`<br>`PreToolUse` = 실행 전 |
| 실패 Bash 출력까지 정규화 | 오류 상세 소실 → 잘못된 전제 |
| 모든 shell 명령을 수동 승인 큐로 | shell matcher + exit 2로 필요 검사만 자동 차단 |
| merge 후 스캔 · 분기별 grep · `CLAUDE.md` 경고 | 이력 유입 뒤 발견 · 경고 ≠ gate |
| `CLAUDE.md` 안내 줄 · `/context`로 hook 점검 | hook 시작 ✗ · 점검 수단 = `/hooks` |
| 개인 skill을 팀 skill과 같은 이름으로 + 팀 업데이트 기대 | 개인 skill이 가림 → 옛 절차 실행 |
| `override: true`<br>frontmatter username 조건 | 해당 기능 없음 · 우선순위 = 위치 |
| 모든 지침을 skill로 + `CLAUDE.md`엔 설명만 | 항상 적용할 표준 · 테스트 규칙까지 on-demand |
| `@import` 분할 · 경로 기반 rules | `CLAUDE.md` 내용 전부 로드<br>경로 rules = 디버깅 · 리뷰에도 로드 |
| 예시를 prompt에 매번 복사 | 수동 반복 · skill 호출이 대안 |
| `.claude/config.json` commands 배열 | command 정의 위치 ✗ |
| README 문서화 · `.claude` VCS 제외 | 파일 공유 ✗ |
| `CLAUDE.md` 기재로 command 공유 | 명령으로 호출 ✗ |
| 단일 `.md` 파일을 `.claude/skills/`에 | skill 로드 ✗ · `<이름>/SKILL.md` 필요 |
| `disable-model-invocation`으로 출력 격리 | 자동 호출만 차단 · 수동 실행 출력 그대로 |
| `user-invocable: false`로 자동 실행 방지 | 개발자 호출만 차단 (반대 방향) |
| `argument-hint`로 자동 실행 방지 · 입력 검증 | 자동 완성 표시만 변경 |
| `allowed-tools` · `model: haiku`로 출력 격리 | 사전 승인 · 모델 변경 → 실행 위치 그대로 |
| `/fork`로 skill 격리 | 현재 대화 이력 전부 상속 |
| `/clear` · `/compact`<br>`CLAUDE.md` 이동으로 skill 격리 | context 소실 · 사후 압축 · 상시 로드 |
| skill 분할 · 요약 지시 단독<br>`/explore-start` · `/explore-end` 분리 | 실행 위치 그대로 → 격리 ✗ |
| `!` 접두사 bash subprocess로 탐색 실행 | 격리 수단 = `context: fork` |
| 길이 · 작성자 경력<br>edge case 포괄로 skill commit 판단 | 반복 절차 · 리뷰 가능성 입증 ✗ |
| 온보딩 영상 · 시니어 버디 · 프로덕션 전체 접근 | 영상 = 낡음 · 질의 ✗<br>버디 = 신입마다 시니어 비용<br>프로덕션 접근 = 보안 · 안정성 위험 |
| 위키 삭제 · 갱신 날짜 · 주간 이메일 | 삭제 = 지식 소실<br>날짜 · 이메일 = 버전 관리 ✗ · 낡음 |
| "skill이 항상 낫다"<br>작업 길이로 skill vs subagent 선택 | 노하우 재사용 vs context 격리가 기준 |

<sub>근거: CCAR-F-Amey-Thakur-0020, CCAR-F-Amey-Thakur-0070, CCAR-F-MyPractice-0033, CCAR-F-MyPractice-0035, CCAR-F-MyPractice-0036, CCAR-F-MyPractice-0038, CCAR-F-MyPractice-0041, CCAR-F-MyPractice-0043, CCAR-F-Udemy01-0002, CCAR-F-Udemy01-0024, CCAR-F-Udemy01-0040, CCAR-F-Udemy02-0015, CCAR-F-Udemy02-0041, CCAR-F-Udemy02-0059, CCAR-F-Udemy03-0026, CCAR-F-Udemy03-0036, CCAR-F-Udemy03-0052, CCAR-F-Udemy04-0026, CCAR-F-Udemy04-0046, CCAR-F-Udemy05-0034, CCAR-F-Udemy06-0006, CCAR-F-Udemy06-0034, CCAR-F-Udemy06-0037, CCAR-F-Udemy06-0045, CCAR-F-Udemy06-0047, CCAR-F-paullarionov-0033, CCAR-F-paullarionov-0035, CCAR-F-paullarionov-0036, CCAR-F-paullarionov-0038, CCAR-F-paullarionov-0041, CCAR-F-paullarionov-0043, CCAR-F-preporato-0017, CCAR-F-preporato-0018, CCAR-F-preporato-0019, CCAR-F-preporato-0021, CCAR-P-jrajath94-0063, CCAR-P-jrajath94-0106, CCAR-P-jrajath94-0261, CCAR-P-jrajath94-0269, CCAR-P-jrajath94-0331, CCAR-P-jrajath94-0678, CCAR-P-jrajath94-0702, CCAR-P-jrajath94-0707</sub>

@@ MEMO

| 이름 | 의미 |
|---|---|
| `.claude/commands/` | 프로젝트 custom command<br>commit → 팀 공유 |
| `~/.claude/commands/` | 개인 command · 팀원 사용 ✗ |
| `.claude/skills/<이름>/SKILL.md` | 프로젝트 skill · 저장소와 함께 버전 관리 |
| `~/.claude/skills/<이름>/SKILL.md` | 개인 skill · 본인 전 프로젝트 |
| skill 우선순위 | enterprise > personal > project<br>(같은 이름 · 위치 기준) |
| `context: fork` | skill을 이력 없는 새 subagent에서 실행<br>(`/fork`와 다름) |
| `allowed-tools` | turn 동안 도구 사전 승인 · 제한 ✗ |
| `disallowed-tools` | skill 활성 동안 도구 풀에서 제거 |
| `disable-model-invocation: true` | Claude 자동 로드 차단 · 수동 호출만 |
| `user-invocable: false` | 개발자 호출 차단 (Claude만 호출) |
| `argument-hint` | 자동 완성 시 기대 인수 표시 |
| `$ARGUMENTS` · `$0` · `$1` | 전체 인수 · 첫째 · 둘째 인수 |
| `Stop` hook + exit 2 | Claude 종료 막고 stderr 전달 |
| `updatedToolOutput` | `PostToolUse`에서 도구 출력 교체 |
| `/hooks` | 현재 session hook 구성 확인 |
| `tools` (subagent) | 사용 가능 도구 제한 · 생략 = 모든 도구 상속 |
| Explore subagent | read-only · Write · Edit 거부 · 요약 반환 |

<sub>근거: CCAR-F-Amey-Thakur-0020, CCAR-F-Udemy02-0015, CCAR-F-Udemy02-0041, CCAR-F-Udemy02-0059, CCAR-F-Udemy03-0026, CCAR-F-Udemy03-0036, CCAR-F-Udemy04-0017, CCAR-F-Udemy04-0046, CCAR-F-Udemy06-0037, CCAR-F-Udemy06-0045, CCAR-F-Udemy06-0047, CCAR-F-paullarionov-0036, CCAR-F-paullarionov-0041, CCAR-F-preporato-0018, CCAR-P-jrajath94-0702, CCAR-P-jrajath94-0707</sub>

@@ CHECK

- [ ] 같은 이름 개인 skill = 대체 · 다른 이름 = 공존
- [ ] "확인 없이" = `allowed-tools` · "쓸 수 없게" = `disallowed-tools`
- [ ] 메인 오염 출력 → `context: fork` (`/fork` 아님)
- [ ] subagent 제한 = `tools` 목록 · 지시문 ✗

<sub>근거: CCAR-F-Udemy01-0040, CCAR-F-Udemy02-0041, CCAR-F-Udemy03-0026, CCAR-F-Udemy06-0037, CCAR-F-paullarionov-0036, CCAR-P-jrajath94-0261, CCAR-P-jrajath94-0702</sub>
