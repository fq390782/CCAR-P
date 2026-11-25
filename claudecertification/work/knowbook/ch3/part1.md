@@ NEW-SECTION
### CLAUDE.md 위치별 범위와 결합
**공유 범위는 파일 위치가 결정**

| 위치 | 적용 대상 | 로드 · 용도 |
|---|---|---|
| 프로젝트 `./CLAUDE.md`<br>또는 `./.claude/CLAUDE.md` | 팀 전원<br>commit → 버전 관리 · 리뷰 | 작업 디렉터리 · 상위 = 시작 시 로드<br>저장소 전체 규칙 · 팀 컨벤션 |
| `~/.claude/CLAUDE.md` | 본인 · 모든 프로젝트<br>버전 관리 공유 ✗ | 개인 선호 (예: 설명 방식)<br>팀 규약 기재 ✗ |
| `CLAUDE.local.md` | 본인 · 이 프로젝트만 | `.gitignore` 추가<br>(예: 개인 검증 서버 · 담당 데이터 번호) |
| 하위 디렉터리 `CLAUDE.md` | 팀 · 그 디렉터리 작업 | Claude가 그 디렉터리 파일을 읽을 때 추가 로드<br>디렉터리 한정 규약용 |

| 구분 | 내용 |
|---|---|
| 결합 방식 | 발견된 파일 = 덮어쓰기 ✗ → 연결해 context 투입<br>"자식이 부모 덮어쓰기" 전제 = 오답 |
| 로드 순서 | 사용자 수준 → 프로젝트 수준<br>디렉터리 = 루트 → 하위 |
| 시작 위치 | 작업 디렉터리 · 상위 = 시작 시 로드<br>하위 = 읽을 때 로드<br>→ 시작 위치에 따라 로드 파일 상이 |
| 모순 지시 | 수준 간 충돌 → Claude가 한쪽 임의 선택<br>→ session · 멤버별 결과 불일치 |
| 모순 해소 | 같은 항목을 한 수준에만 남김<br>(루트 규약 범위 한정 · 개인 파일 지시 제거)<br>"상위보다 우선" 문구 · 루트 삭제 ✗ |

| 구분 | 내용 |
|---|---|
| 팀 · 개인 판단 기준 | 전원에게 같은 적용이 필요한가<br>위반 시 팀 산출물에 영향이 나오는가 |
| 팀 규약 | 시간대 저장(UTC) · 빌드 명령(`make ci`)<br>commit 서식 |
| 개인 선호 | 설명 방식 (예: 짧은 bullet) |
| 개인 + 이 프로젝트 한정 | `CLAUDE.local.md`<br>`~/.claude/CLAUDE.md` = 다른 프로젝트에도 로드<br>→ 부적합 |
| `.claude/rules/` | 팀 공유 파일 · `paths`는 사람이 아니라 파일로 범위 축소<br>→ 개인용 ✗ |

<sub>근거: CCAR-F-Amey-Thakur-0018, CCAR-F-Amey-Thakur-0055, CCAR-F-Udemy01-0041, CCAR-F-Udemy03-0046, CCAR-F-Udemy04-0007, CCAR-F-Udemy05-0012, CCAR-F-Udemy05-0058, CCAR-F-Udemy06-0016</sub>

@@ NEW-SECTION
### 팀 일관성과 CLAUDE.md 크기
**커밋된 짧은 공통 파일이 일관성의 기반**

| 증상 | 원인 | 조치 |
|---|---|---|
| 한 명만 잘 동작<br>팀 결과 들쭉날쭉 | 컨벤션이 한 사람의 로컬 환경에만 존재 | 저장소에 commit<br>(장비 · 저장소 크기 · terminal ✗) |
| 기존 멤버만 지침 준수<br>신규 입사자 미준수 | 지침이 기존 멤버의 사용자 수준<br>`~/.claude/CLAUDE.md`에만 존재 | 프로젝트 `CLAUDE.md`로 이동 · commit<br>→ 현재 · 미래 팀원 자동 적용 |
| 리더 환경만 준수<br>신규 멤버 · CI 미준수 | 규약이 리더의 `CLAUDE.local.md`에만 존재<br>(신규 `/context` = 공유 `CLAUDE.md`만 표시) | 공유 `CLAUDE.md`로 이동 |
| 새 코드엔 도움<br>레거시엔 해가 됨 | 레거시에 commit된 컨텍스트 · 관례 부재 | 조사 대상 = 컨텍스트 · 관례<br>교육 · 더 큰 모델 · 재작성 = 진단 전 과잉 |
| 기존 코드베이스 성과 저조 | 관례 · 구조를 설명하는<br>commit된 컨텍스트 부재 | 팀이 직접 고칠 수 있는 원인<br>(크기 · 언어 · 기여자 수 = 원인 ✗) |
| `CLAUDE.md` 수천 줄 | 중요한 지시가 무관한 내용과 경쟁 · 희석 | 많다고 좋아짐 ✗ · 속도 개선 ✗<br>기준 = 파일당 200줄 미만 |
| 개인 내용을 commit 파일에 기재 | 다른 멤버 Claude 오동작<br>해당 줄 편집 → merge 충돌 | 공통 내용만 commit 파일에 유지<br>개인 내용 → `CLAUDE.local.md` |

<sub>근거: CCAR-F-Amey-Thakur-0022, CCAR-F-Amey-Thakur-0069, CCAR-F-MyPractice-0037, CCAR-F-Udemy04-0007, CCAR-F-Udemy05-0026, CCAR-F-Udemy05-0047, CCAR-F-Udemy06-0060, CCAR-F-paullarionov-0037, CCAR-P-Amey-Thakur-0035, CCAR-P-Amey-Thakur-0080</sub>

@@ NEW-SECTION
### @import로 공통 표준 재사용
**@import는 정리용 · 로드량은 불변**

| 구분 | 내용 |
|---|---|
| 문법 | `CLAUDE.md` 안 `@경로`<br>상대 · 절대 경로 모두 허용 |
| 상대 경로 기준 | import를 포함한 파일의 위치<br>작업 디렉터리 ✗ |
| 로드 시점 | 시작 시 · 포함한 파일과 함께 로드<br>→ context 소비 감소 ✗ (정리 효과만) |
| 로드 제외 | code span · fenced code block 안의 `@경로` |
| 용도 | 표준 정본 1곳 + 패키지별 필요한 것만 import<br>→ 본문 복사 제거 · 표준 개정 시 일괄 반영 |

| 방식 | 판정 |
|---|---|
| 공통 = 루트 `CLAUDE.md`<br>고유 표준 = 패키지 `CLAUDE.md`의 `@import` | ✓ 공통은 전원 · 고유는 해당 패키지만<br>(개발자가 패키지에서 시작하는 조건) |
| 모든 도메인 표준을 루트에 집약 | ✗ 모든 패키지가 전 도메인 지시 상속 |
| README 링크 · 문장으로 "읽어라" | ✗ 자동 로드 · 로드 보장 없음 |
| 각 패키지에 본문 복사 | ✗ 개정 시 일부만 stale → 패키지별 규약 상이 |
| CI 스크립트로 자동 복사 | ✗ 복제 구조 유지 |
| import를 fenced code block 안에 배치 | ✗ 로드 안 됨 |
| `@docs/standards/x.md`가<br>`packages/x/CLAUDE.md`에서 미로드 | 원인 = 상대 경로가 그 파일 위치 기준으로 해석<br>→ 경로를 `../../docs/standards/x.md`로 수정 |
| 항상 루트에서 시작 · 복사<br>`~/.claude/CLAUDE.md`로 이동 | ✗ 기준 오해 · 공유 · 선택적 import 방침 붕괴 |

<sub>근거: CCAR-F-Udemy03-0029, CCAR-F-Udemy04-0042, CCAR-F-Udemy04-0059, CCAR-F-Udemy05-0047, CCAR-F-Udemy06-0031</sub>

@@ NEW-SECTION
### CLAUDE.md 로드 진단
**수정 전에 로드 상태부터 관찰**

| 확인 수단 | 보여 주는 것 |
|---|---|
| `/context`의 "Memory files" | 현재 session에 로드된 지시 파일<br>목록에 없으면 Claude에게 안 보임 |
| `/memory` | 사용자 · 프로젝트 메모리 파일 위치 목록<br>(없는 파일 포함) · 열어 편집용 · 로드 확인 ✗ |
| `/status`의 Setting sources | 설정 파일 로드 현황 · 지시 파일 ✗ |
| `InstructionsLoaded` hook 로그 | 로드된 지시 · 규칙 파일 기록<br>→ path rule 로드 여부 검증 |
| 하위 디렉터리 파일 읽기 | 하위 `CLAUDE.md`는 그 디렉터리 파일을 읽을 때 로드 |
| ⚠️ 명령 표기 | 현재 공식 문서 = `/context all` 안내<br>fullscreen의 `/context`만으로 목록 접힘<br>→ 문항 표기와 차이 |

| 상황 | 첫 조치 |
|---|---|
| 같은 요청인데 시작 위치마다 동작 상이 | 시작 디렉터리 ↔ `CLAUDE.md` 위치 대조<br>+ 각 session `/context` Memory files 비교 |
| 내 환경에서만 재현 · 신규 환경 ✗ | 관련 `CLAUDE.md`가 로드되는 위치에 있는지 확인<br>+ `/context`에서 로드 여부 확인 |
| 루트에서 시작 · `/context`에 하위 `CLAUDE.md` 없음 | 결함 ✗ · 온디맨드 로드의 정상 동작<br>→ 그 하위 파일을 Claude에게 읽혀 로드 확인 |
| 지시 효과 없어 보임 | 설정 변경 전 로드 위치 확인이 출발점 |
| 진단이 아닌 변경 | `/init` 재실행 · auto memory 비활성화<br>`settings.local.json`에 규약 기재 · 내용 루트로 이동 |

<sub>근거: CCAR-F-Udemy01-0039, CCAR-F-Udemy03-0046, CCAR-F-Udemy04-0020, CCAR-F-Udemy04-0059, CCAR-F-Udemy05-0026, CCAR-F-Udemy06-0016</sub>

@@ NEW-SECTION
### path-specific rules (.claude/rules/)
**규칙 범위는 디렉터리가 아니라 파일 경로 패턴**

| 구분 | 내용 |
|---|---|
| 위치 · 단위 | `.claude/rules/*.md`<br>주제별 1파일<br>(예: `testing.md` · `api-conventions.md`) |
| `paths` 없음 | 시작 시 로드 → 로드량 불변<br>파일명 · 폴더 구성(`rules/db/`)으로 범위 제한 ✗ |
| `paths` 있음 | 일치 파일을 Claude가<br>Read · Write · Edit 할 때만 로드 |
| 로드 계기 | 작업 주제 ✗ · Claude가 다룬 파일 경로 ✓ |
| frontmatter | Claude Code가 읽는 항목 = `paths`뿐 |
| `paths` 값 | YAML 리스트 또는 쉼표 구분 문자열<br>중괄호 확장 `{ts,tsx}` 가능 |
| 사용자 수준 | `~/.claude/rules/` = 개인용 · 팀 공유 ✗ |
| 적합한 경우 | 같은 종류 파일이 여러 디렉터리에 분산<br>(colocated 테스트 · migration<br>`.proto` · `.sql`) |

| 패턴 | 일치 범위 |
|---|---|
| `*.sql` · `*.md` | 프로젝트 루트 파일만 |
| `proto/*.proto` | 루트 `proto/` 바로 아래만 |
| `packages/*/*.graphql` | 얕은 계층만 · 깊은 계층 ✗ |
| `**/*.ts` | 모든 디렉터리의 `.ts` → 범위 넓음 |
| `**/*.sql` · `**/*.proto` | 깊이 무관 해당 확장자 전체 ✓ |
| `**/*.{graphql,ts}` | `**/*.graphql` + `**/*.ts`로 확장<br>→ 모든 TypeScript 파일 일치 |
| `**/*.graphql` + `**/*.resolver.ts` | 의도한 두 종류만 ✓<br>(쉼표 구분 문자열도 가능) |
| `**/*.test.tsx` · `src/api/**/*.ts`<br>`services/payments/**` | 위치 무관 테스트 · 특정 영역 한정 |

| 구분 | 디렉터리 `CLAUDE.md` | `paths` rule |
|---|---|---|
| 범위 결정 | 어느 디렉터리인가 | 어느 파일 패턴인가 |
| 로드 | 그 디렉터리 파일을 읽을 때 | 일치 파일을 다룰 때 |
| 적합 | 디렉터리 한정 규약<br>(예: payments 서비스 · `tests/` fixture 명명) | 흩어진 같은 종류 파일 규약 |
| 분산 파일에 사용 시 | 디렉터리마다 복제 → 유지보수 부담 | 한 곳 정의 |

| 상황 | 정답 배치 |
|---|---|
| payments 코드에서만 로드 (2개 선택) | `services/payments/CLAUDE.md`<br>`paths: ["services/payments/**"]` rule |
| payments 오답 | 루트 `CLAUDE.md` 섹션 = 모든 session 로드<br>`~/.claude/CLAUDE.md` = 개인용<br>`.mcp.json` = 지시 미포함 |
| 공통 commit 규칙 + 영역별 컨벤션 | commit 규칙 = 프로젝트 `CLAUDE.md`<br>영역 컨벤션 = 경로 지정 rule |
| 지시 파일 하나가 비대 · 영역별 규칙 상이 | `.claude/rules/` 주제별 파일 분리<br>`.claude/config.yaml` 매핑 · README 로드<br>= 지원 방식 아님 |

<sub>근거: CCAR-F-Amey-Thakur-0005, CCAR-F-Amey-Thakur-0040, CCAR-F-MyPractice-0040, CCAR-F-MyPractice-0042, CCAR-F-Udemy02-0047, CCAR-F-Udemy02-0053, CCAR-F-Udemy03-0040, CCAR-F-Udemy05-0029, CCAR-F-Udemy05-0056, CCAR-F-Udemy06-0001, CCAR-F-paullarionov-0040, CCAR-F-paullarionov-0042, CCAR-F-preporato-0022</sub>

@@ NEW-SECTION
### 비대한 CLAUDE.md 분할과 paths 점검
**이동 + 원본 삭제 · 둘 다 필요**

| 상황 | 조치 |
|---|---|
| 한 파일에 주제 혼재 (리뷰 톤 · 테스트 · API · 배포) | 루트 = 모든 변경 공통 기준만<br>주제별 = `.claude/rules/`<br>특정 파일용 = `paths` 부여 |
| 특정 파일 종류 규약이 수백 줄<br>(`*.tf` · `*.yang` · `*.sql`) | `paths` rule로 이동 + 루트에서 삭제<br>이동만 · 삭제만 ✗ |
| 테스트 규약이 여러 디렉터리에 복제 · stale | `paths` rule 1개(`testing.md`)로 집약<br>+ 복제본 삭제 |
| 가끔만 쓰는 절차 (예: SDK 마이그레이션) | skill → 필요할 때만 로드 |
| 항상 지킬 규약 | 루트 `CLAUDE.md` 또는 `paths` 없는 rule<br>(시작 시 로드 → 분할해도 누락 ✗) |
| 여러 팀 편집 → merge 충돌 · 후반부 규약 미준수 | 주제별 rule 분할 + 루트 최소화<br>(예: `billing-api.md`) |
| 분할 후 확인 | `/context`로 시작 시 로드된 파일 확인<br>→ 프런트엔드 작업에 무관 규약 미포함 |

| 증상 | 원인 | 조치 |
|---|---|---|
| 기존 파일 작업은 규약 준수<br>변환 스크립트 작업은 미준수<br>로그상 rule 미로드 | 작업이 `paths` 일치 파일을 읽거나 쓰지 않음 | 작업에서 다루는 파일(생성 스크립트 · 템플릿)을 `paths`에 포함<br>`InstructionsLoaded` 로그로 확인 |
| 루트 파일엔 적용<br>하위 디렉터리엔 미적용 | 패턴 범위 좁음 (`*.sql`) | `**/*.sql` |
| 무관한 TypeScript 작업에도 로드 | 패턴 범위 넓음 (`{graphql,ts}` 확장) | 대상별 패턴으로 좁힘 |
| 범위 과대 · 과소 | 과대 → 무관 context · 토큰 소비<br>과소 → 규약 미적용 | 대상 파일 · 비대상 파일을 각각 읽혀 확인 |

| 방식 | 판정 |
|---|---|
| 테스트 규약을 루트 `CLAUDE.md`로 이동 | 일관성 ✓ · 항상 로드 ✗ |
| 규약을 slash command(`.claude/commands/`)로 | 개발자 수동 실행 의존 ✗ |
| `paths` 없는 rule을 폴더별 정리 | 로드량 불변 ✗ |
| 패키지마다 `CLAUDE.md`에 규약 복제 | 유지보수 ✗ · stale |
| `~/.claude/rules/`로 이동 | 팀 공유 ✗ · `paths` 없으면 시작 시 로드 |
| `@import`로 분리 | 로드량 불변 ✗ |

<sub>근거: CCAR-F-Udemy02-0035, CCAR-F-Udemy02-0040, CCAR-F-Udemy04-0020, CCAR-F-Udemy04-0042, CCAR-F-Udemy05-0029, CCAR-F-Udemy05-0047, CCAR-F-Udemy05-0056, CCAR-F-Udemy06-0017</sub>

@@ ADD-TO: ### 구성 요소 구분 (로드 시점 · 작성자)
| 상황 | 배치 |
|---|---|
| 모든 코드에 항상 적용될 규약<br>(예: 환자 ID 로그 금지 · UTC 저장) | 프로젝트 `CLAUDE.md`<br>skill에 두면 미호출 session 미적용 |
| 특정 작업의 절차 | skill (온디맨드 호출) |
| 가끔 쓰는 절차 | skill → 필요할 때만 로드 |
| `disable-model-invocation`<br>`context: fork` | 호출 방식만 변경 → 상시 적용 요건 충족 ✗ |
| 개발 절차서에 "시작 시 skill 실행" 기재 | 사람 의존 → 누락 발생 |
| 위반 불허 규약 | `CLAUDE.md` + hook · 리뷰 병행 |

<sub>근거: CCAR-F-Udemy04-0042, CCAR-F-Udemy05-0013</sub>

@@ ADD-TO: ### `CLAUDE.md`는 지시, `settings.json`은 강제
| 수단 | 분류 | 이유 |
|---|---|---|
| deny 규칙 (예: `Read(.env)`) | 강제 | 도구 실행 전 평가 · 모델이 뒤집기 ✗ |
| `PreToolUse` hook | 강제 | 호출 실행 전 결정 · 차단 |
| `CLAUDE.md` · memory 파일 · wiki · 팀 메모 | 지침 | 선택 유도만 · 호출 차단 ✗ |
| 굵은 글씨 · 긴 메모 · 더 큰 모델 | 지침 | 판단력 향상 ≠ 잠금 |

| 상황 | 구성 |
|---|---|
| 비밀 읽기 차단 + 모든 편집에 lint | 비밀 경로 deny + `PostToolUse` lint hook<br>공유 settings를 repo에 commit → 모든 clone 적용 |
| 고객사 비밀 보호 (30명 팀) | commit한 settings의 deny (`.env` · 키 파일)<br>+ 유출 차단 hook · `CLAUDE.md` = 워크플로 안내용 |
| 시크릿 출력 금지 | 출력 패턴 deny + vault 출력 가림 hook<br>공유 settings에 commit |
| 에이전트가 배포 스크립트 실행 (사고 2회) | 배포 경로 deny + 릴리스 엔지니어 allow-list 경로 + 감사<br>스크립트 삭제 ✗ → 릴리스 중단 |
| 인턴 월별 합류 · 고객 데이터 내보내기 | commit한 permissions + 경로 deny<br>범위 제한 subagent + 비협상 항목 = managed |
| 보호 대상 없는 개인 scratch repo | `CLAUDE.md` 가벼운 지침 · 강제는 오버헤드<br>managed · 50쪽 정책 · 승인 위원회 ✗ |

| 한계 | 대응 |
|---|---|
| deny glob 부정확 | 빗나감 → 실제 차단 테스트 |
| 영리한 명령 재작성 | deny 우회 가능 → glob 테스트 |
| hook = shell 명령 실행 | 악의적 hook 위험 → 코드처럼 리뷰 |
| 정당한 사용 경로 부재 | 개발자 우회 → 승인된 예외 경로 |
| 규칙 오구성 | 정당한 작업 차단 → 설계 시간 필요 |

<sub>근거: CCAR-P-jrajath94-0257, CCAR-P-jrajath94-0264, CCAR-P-jrajath94-0328, CCAR-P-jrajath94-0391, CCAR-P-jrajath94-0454, CCAR-P-jrajath94-0517, CCAR-P-jrajath94-0518</sub>

@@ ADD-TO: ### 설정 파일의 범위
| 구분 | 내용 |
|---|---|
| 팀 규칙을 commit한 설정에 두는 이유 | 버전 관리 · 리뷰 · CI 포함 모든 사람에게 적용<br>로드 속도 · context 절감 · 덮어쓰기 불가 = 이유 ✗<br>(로컬에서 덮어쓸 수 있음) |
| 팀 표준화 | repo에 공유 구성 commit<br>(`CLAUDE.md` · MCP 서버 목록 · permissions)<br>→ 한 곳 수정 → 전원 전파 |
| 표준화 ✗ | 개인 설정 방치 · PDF 이메일 · 채팅 안내<br>Claude Code 사용 금지 |
| CI 포함 어디서나 금지 | commit한 project settings deny<br>(예: `Bash(git push *)` · `Bash(curl *)`)<br>→ 클라이언트 강제 · CI 포함 적용 |

| 구분 | 내용 |
|---|---|
| 계층 모델 | 개인(local) → 팀(commit 프로젝트 기본값)<br>→ 조직(managed)<br>guidance(`CLAUDE.md`)는 어느 계층도 아님 |
| 개인 예외 | `.claude/settings.local.json`<br>공유 파일 미수정 · 사유 기록 · 기간 한정 |
| 공유 파일 임시 수정 후 복구 | 전원 통제 약화 · 복구 전까지 방치 |
| 팀 규칙 + 개인 예외 | 팀 deny = commit한 공유 settings<br>개인 추가 allow = git 제외 local settings |
| deny 범위 | 어떤 범위의 deny든 여전히 적용 |
| ⚠️ local 예외 | 해설: local 파일이 공유 deny를 덮어씀<br>공식 문서: deny는 범위 불문 allow보다 먼저 평가<br>→ local allow로 공유 deny 해제 ✗ · 확인 필요 |
| ⚠️ 만료 | settings 파일의 자동 만료 기능 확인 ✗<br>"하루 뒤 만료"는 운영 절차(해설 전제) |

| 구분 | 내용 |
|---|---|
| managed settings 특성 | 팀 · 개인 재정의 불가<br>`--settings` · repo 설정 · user 설정으로 완화 ✗<br>새 repo에도 추가 작업 없이 적용 |
| 배포 | MDM으로 `managed-settings.json` 배포 |
| 계층 선택 질문 | 누구에게 적용하고 싶은가<br>누구에게 변경시키고 싶지 않은가 |
| managed에 두는 것 | 비밀 경로 · `.env` 읽기 deny (repo 일괄)<br>모든 커밋 시크릿 스캔 hook + deny<br>모델 · 지출 가드레일 · 협상 불가 항목만 |
| project 기본값에 두는 것 | 팀 hook (예: 편집마다 lint `PostToolUse`)<br>조직 의무화 시에만 managed |
| 개인 config | 에디터 테마 등 개인 취향 |
| 신호 문구 | "어느 팀도 약화 ✗" · "어디서나 · 예외 없이"<br>→ managed |
| committed 파일의 한계 | repo 쓰기 권한자는 편집 가능<br>→ 조직 규칙 보장 ✗ |
| managed 운영 조건 | 조직 플랜 · 관리자 권한 · 비상 해제(break-glass)<br>예외 경로 없으면 shadow workflow |
| ⚠️ 지출 상한 | 해설 = 모델 · 지출 가드레일을 managed에 배정<br>공식 managed settings 문서에서<br>지출 상한 키 확인 ✗ → 검증 필요 |
| ⚠️ permissionless mode | 공식 용어 아님<br>`bypassPermissions` 모드로 추정<br>(`disableBypassPermissionsMode`) |

| 구분 | 내용 |
|---|---|
| 공유 MCP 서버 | 공유 config에 1회 선언 → 전원 같은 도구<br>머신별 drift 종료 |
| 자격 증명 | config의 비밀 처리 방식 안에 보관<br>채팅에 붙여넣기 ✗ (transcript 유출) |
| 한계 | 공유 서버 = 단일 장애점<br>자격 증명 rotation 별도 필요 |
| 오답 | 토큰 계속 붙여넣기 · 서버 금지(검색 기능 상실)<br>개인별 서버 (N개 서버 = N가지 동작) |
| 예외 | 서버가 실제 필요 미충족 → 제거가 정답<br>데이터 경계로 격리 필요 → 각 서버를 공유 config에 선언 |

<sub>근거: CCAR-F-Amey-Thakur-0071, CCAR-F-Udemy01-0008, CCAR-P-jrajath94-0060, CCAR-P-jrajath94-0103, CCAR-P-jrajath94-0258, CCAR-P-jrajath94-0259, CCAR-P-jrajath94-0260, CCAR-P-jrajath94-0262, CCAR-P-jrajath94-0392, CCAR-P-jrajath94-0455, CCAR-P-jrajath94-0580, CCAR-P-jrajath94-0581, CCAR-P-jrajath94-0703, CCAR-P-preporato-0029</sub>

@@ NEW-SECTION
### permissions 설계와 실행 전 강제 수단
**위험 = deny · 안전 = allow · 회색 = ask**

| 구분 | 내용 |
|---|---|
| 평가 | deny 규칙 먼저 평가 · 모델이 결과 뒤집기 ✗ |
| 분류 | 안전 → allow · 위험 → deny<br>판단이 중요한 회색 영역 → ask |
| 전부 ask | 하루 40건 → 3일차 읽지 않고 "허용"<br>위험 요청이 일상 요청에 묻힘 |
| 전부 allow | 통제 제거 |
| 전부 deny | 정당한 작업 차단 → 우회 (우회 경로는 규칙 없음) |
| 관점 | 묻기 = 주의력 예산 · 판단이 가치 더하는 곳에만 사용 |
| 유지 | 안전 · 위험 목록이 워크플로와 일치해야 함<br>변경 시 갱신 · 오분류 = 귀찮음 또는 위험 |
| 반례 | 요청 하루 5건 미만 + 각각 회색 → 전부 ask 가능<br>일상 행동 없는 기밀 환경 → 전부 deny는 명시 결정 |

| 수단 | 판정 |
|---|---|
| 권한 deny 규칙 (deploy 명령) | ✓ 실행 전 평가 · 모델 무관 |
| 시스템 프롬프트에 금지 문장 반복 | ✗ 모델 판단 의존 |
| sandbox 허용 도메인 목록에서 호스트 제외 | ✗ sandbox 안 명령이 닿는 호스트만 제어<br>명령 실행 자체는 금지 ✗ |
| `PostToolUse` hook으로 읽기 차단 | ✗ 도구 호출 성공 후에만 실행 |
| 커밋된 settings의 `Read` deny (secrets 폴더) | ✓ pull 후 모든 clone · 모델이 메모 무시해도 유지 |
| 팀 deny를 개인 user settings에 | ✗ 팀 전체 강제 불가 |
| 팀 deny를 `CLAUDE.md`에 | ✗ `CLAUDE.md`는 permission 강제 ✗ |
| 팀 deny(commit) + 개인 allow(local) | ✓ 팀 규칙 유지 + 개인 예외 |
| ⚠️ deny의 차단 범위 | 해설 = deny가 "모든 시도" 차단<br>공식 문서 = Bash deny는 다른 호출 형태<br>(경로 지정 · `sh -c`) 미차단 → sandbox 병행 |

<sub>근거: CCAR-P-jrajath94-0265, CCAR-P-jrajath94-0672, CCAR-P-jrajath94-0701, CCAR-P-jrajath94-0703, CCAR-P-preporato-0029</sub>

@@ ADD-TO: ### Headless / CI 실행
| 구분 | 내용 |
|---|---|
| 프로젝트 지침 로드 | `claude -p` = 기본 프로젝트 `CLAUDE.md` 로드<br>`--bare` = 자동 로드 생략<br>→ `--append-system-prompt-file` 등 명시 전달 |
| CI 품질 지침 | commit한 `CLAUDE.md`에 기재<br>(가치 있는 테스트 기준 · fixture 용도와 사용법)<br>→ 저가치 테스트 감소 · 기존 factory 재사용 |
| 공유 + CI 동시 충족 | 루트 `CLAUDE.md` = 테스트 방침 · 리뷰 기준<br>하위 `CLAUDE.md` = 그 디렉터리 규약<br>(예: `tests/` fixture 명명) · 간결 유지 |
| CI에서 안 읽히는 곳 | 러너 이미지의 `~/.claude/CLAUDE.md` = repo 밖<br>`claude_args`의 `--append-system-prompt`<br>= workflow 안에서만 유효 |
| 약한 지침 | "질 높은 테스트를 써라" 한 문장 = 구체성 ✗<br>사용자 수준 파일 = 공유 ✗ |
| 기준 보강 | 리뷰에서 반려된 테스트 사례를 모아 기준 기술에 반영 |

<sub>근거: CCAR-F-Udemy01-0038, CCAR-F-Udemy05-0050</sub>

@@ ADD-TO: ### Plugins의 팀 운영
| 구분 | 내용 |
|---|---|
| 전사 동일 버전 배포 | skill + subagent → plugin으로 패키징<br>또는 managed settings로 배포<br>→ 관리되는 버전 1개 |
| 복사 배포 | 채팅에 prompt 게시 · `~/.claude/` 복사<br>→ 원본 변경 즉시 어긋남 |
| `CLAUDE.md`에 붙여넣기 | 항상 적용 지침용<br>subagent · 온디맨드 skill 정의 ✗ |

<sub>근거: CCAR-P-preporato-0030</sub>

@@ RULES
| 상황 | 정답 |
|---|---|
| 저장소 전체 규칙 · 팀 컨벤션 | commit한 프로젝트 `CLAUDE.md` |
| 모든 프로젝트 공통 개인 선호 | `~/.claude/CLAUDE.md` |
| 이 프로젝트 한정 개인 설정 | `CLAUDE.local.md` + `.gitignore` |
| 특정 디렉터리 한정 규약 | 그 디렉터리 `CLAUDE.md` |
| 여러 디렉터리에 흩어진 같은 종류 파일 규약 | `.claude/rules/*.md` + `paths` glob |
| 공통 표준 1곳 + 패키지별 선택 | 루트 공통 + 패키지 `CLAUDE.md`에서 `@import` |
| context 소비를 줄이는 것이 목표 | `paths` rule로 이동 + 원본 삭제<br>(`@import`로는 로드량 불변) |
| 상시 규약 vs 가끔 쓰는 절차 | 상시 = `CLAUDE.md` · 가끔 = skill |
| `CLAUDE.md` 비대 · merge 충돌 | 주제별 rule 분할 + 루트 최소화 |
| 지시가 안 지켜지는 것 같음 | 변경 전 `/context` Memory files · 시작 위치 확인 |
| 모든 clone에 팀 deny 강제 | commit한 공유 settings의 deny |
| 팀 규칙 약화 없는 개인 예외 | `.claude/settings.local.json`<br>+ 사유 · 기간 기록 |
| 조직 전체 · 신규 repo 자동 · 개발자 변경 불가 | managed settings (MDM 배포) |
| 팀 워크플로 hook (편집마다 lint) | commit한 `.claude/settings.json` |
| 권한 요청 피로 | 안전 allow · 위험 deny · 회색만 ask |
| CI에서 프로젝트 지침 전달 | commit한 `CLAUDE.md` (`--bare`면 명시 전달) |
| 공유 MCP 서버 + 토큰 유출 | 공유 config에 1회 선언 · 토큰 채팅 ✗ |
| 전사 동일 skill + subagent 배포 | plugin 패키징 또는 managed settings |
| 보호 대상 없는 개인 repo | 가벼운 `CLAUDE.md` 지침 |

<sub>근거: CCAR-F-Amey-Thakur-0005, CCAR-F-Amey-Thakur-0018, CCAR-F-Amey-Thakur-0071, CCAR-F-Udemy01-0008, CCAR-F-Udemy01-0038, CCAR-F-Udemy01-0039, CCAR-F-Udemy01-0041, CCAR-F-Udemy02-0040, CCAR-F-Udemy03-0029, CCAR-F-Udemy04-0007, CCAR-F-Udemy04-0042, CCAR-F-Udemy05-0012, CCAR-F-Udemy05-0013, CCAR-F-Udemy05-0050, CCAR-F-Udemy05-0056, CCAR-F-Udemy06-0017, CCAR-P-jrajath94-0259, CCAR-P-jrajath94-0262, CCAR-P-jrajath94-0265, CCAR-P-jrajath94-0518, CCAR-P-jrajath94-0581, CCAR-P-jrajath94-0703, CCAR-P-preporato-0030</sub>

@@ TRAPS
| 오답 | 이유 |
|---|---|
| 팀 규약을 `~/.claude/CLAUDE.md`<br>· `CLAUDE.local.md`에 기재 | 팀 공유 ✗ → 신규 멤버 · CI 미적용 |
| "기억할 때까지 반복 요구"<br>· cache 삭제 · 충돌 지시 삭제 | 원인은 지침이 사용자 수준에만 존재 → 프로젝트 파일로 이동 |
| 자식 `CLAUDE.md`가 부모 덮어쓰기 · "상위보다 우선" 문구 | 파일은 연결 → 모순 잔존 → 임의 선택 |
| 개인 파일에 복사 · 요청문마다 규칙 보충 | 팀 공유 구조 ✗ |
| README 링크 · wiki · 채팅 · PR template | 작업 context로 읽히지 않음 |
| `@import`로 context 절감 | 시작 시 로드 → 소비 불변 |
| import 경로를 작업 디렉터리 기준으로 작성 · 루트에서 시작해 해결 | 포함하는 파일 위치 기준으로 해석 |
| fenced code block 안의 `@경로` | 로드 제외 |
| `paths` 없는 rule을 파일명 · 폴더로 범위 지정 | 항상 시작 시 로드 |
| `*.ext` · `dir/*.ext`로 모든 깊이 지정 | 루트 · 바로 아래만 일치 |
| `{graphql,ts}` 중괄호 확장 | `**/*.ts` 전체로 확장 → 과대 일치 |
| 디렉터리마다 `CLAUDE.md` 복제 | 유지보수 부담 · stale 공존 |
| 규약을 slash command로 | 수동 실행 의존 |
| 상시 규약을 skill에 | 미호출 session 미적용 |
| `.claude/config.yaml` 매핑<br>· 하위 README.md 자동 로드 | 지원 방식 아님 → `.claude/rules/` |
| `/memory`로 로드 여부 확인 | 목록 · 편집용 |
| `/status` Setting sources로 지시 파일 확인 | 설정 파일 대상 |
| `/init` 재실행 · auto memory 끄기로 진단 | 진단 전 변경 |
| 하위 `CLAUDE.md`가 `/context`에 없음 = 결함 | 온디맨드 로드의 정상 동작 |
| `CLAUDE.md` · 메모 · 굵은 글씨 · 큰 모델로 비밀 차단 | 지침 · 호출 차단 ✗ |
| 시스템 프롬프트 반복 · sandbox 도메인 제외로 명령 금지 | 모델 판단 의존<br>도메인 목록 = 도달 호스트만 제어 |
| 개인 user · local settings에만 팀 deny | 팀 전체 강제 ✗ |
| 공유 settings 임시 수정 후 복구 | 전원 약화 · 방치 위험 |
| 조직 협상 불가 항목을 project 기본값에 | repo 쓰기 권한자 편집 가능 |
| 중요한 모든 것을 managed에 | 협상 불가 항목만 해당 · 워크플로 선호는 우회 |
| 모든 요청 ask · 모두 allow · 모두 deny | 피로 · 통제 제거 · 우회 |
| 토큰 채팅 붙여넣기 · 개인별 MCP 서버 | 유출 · drift |
| prompt 복사 배포 · `CLAUDE.md`에 subagent 정의 | 원본 변경 시 어긋남 · 정의 불가 |

<sub>근거: CCAR-F-Amey-Thakur-0018, CCAR-F-Amey-Thakur-0022, CCAR-F-MyPractice-0037, CCAR-F-MyPractice-0042, CCAR-F-Udemy01-0039, CCAR-F-Udemy01-0041, CCAR-F-Udemy02-0040, CCAR-F-Udemy03-0029, CCAR-F-Udemy03-0040, CCAR-F-Udemy03-0046, CCAR-F-Udemy04-0042, CCAR-F-Udemy04-0059, CCAR-F-Udemy05-0013, CCAR-F-Udemy05-0029, CCAR-F-Udemy05-0056, CCAR-F-Udemy06-0016, CCAR-F-Udemy06-0031, CCAR-F-Udemy06-0060, CCAR-F-paullarionov-0037, CCAR-F-paullarionov-0042, CCAR-P-jrajath94-0257, CCAR-P-jrajath94-0258, CCAR-P-jrajath94-0259, CCAR-P-jrajath94-0260, CCAR-P-jrajath94-0262, CCAR-P-jrajath94-0265, CCAR-P-jrajath94-0328, CCAR-P-jrajath94-0672, CCAR-P-jrajath94-0701, CCAR-P-jrajath94-0703, CCAR-P-preporato-0030</sub>

@@ MEMO
| 이름 | 의미 |
|---|---|
| `~/.claude/CLAUDE.md` | 개인 · 모든 프로젝트 · 팀 공유 ✗ |
| 하위 디렉터리 `CLAUDE.md` | 그 디렉터리 파일을 읽을 때 로드 |
| `.claude/rules/*.md` | 주제별 규칙 파일<br>`paths` 없음 = 시작 시 로드 |
| `paths` | rule frontmatter에서 읽는 유일한 항목<br>일치 파일 Read · Write · Edit 시 로드 |
| `**/*.ext` | 모든 깊이의 해당 확장자 |
| `*.ext` | 프로젝트 루트 파일만 |
| `{a,b}` | 중괄호 확장 → 패턴 여러 개 |
| `~/.claude/rules/` | 사용자 수준 규칙 · 개인용 |
| `@경로` | `CLAUDE.md` import<br>포함한 파일 기준 상대 경로 · 시작 시 로드 |
| 200줄 | `CLAUDE.md` 파일당 권장 상한 (미만) |
| `/context` | session의 Memory files 확인 |
| `/memory` | 메모리 파일 위치 목록 · 편집 |
| `InstructionsLoaded` | 로드된 지시 · 규칙 파일 기록 hook |
| `--bare` | `claude -p`의 `CLAUDE.md` 자동 로드 생략 |
| managed settings | 조직 배포 · 어떤 계층도 덮어쓰기 ✗<br>(MDM `managed-settings.json`) |
| deny 평가 | 가장 먼저 · 모델이 뒤집기 ✗ |

<sub>근거: CCAR-F-Udemy01-0008, CCAR-F-Udemy01-0039, CCAR-F-Udemy03-0029, CCAR-F-Udemy03-0046, CCAR-F-Udemy04-0020, CCAR-F-Udemy04-0042, CCAR-F-Udemy04-0059, CCAR-F-Udemy05-0012, CCAR-F-Udemy05-0029, CCAR-F-Udemy05-0047, CCAR-F-Udemy05-0050, CCAR-F-Udemy06-0016, CCAR-P-jrajath94-0672</sub>

@@ CHECK
- [ ] `paths` 규칙 = 일치 파일 다룰 때만 로드 · 없으면 시작 시 로드
- [ ] `**/*.ext` = 모든 깊이 · `*.ext` = 루트만
- [ ] `@import` = 정리용 · context 소비 불변
- [ ] 막아야 하면 deny · 팀 = commit 설정 · 조직 = managed

<sub>근거: CCAR-F-Udemy02-0035, CCAR-F-Udemy05-0047, CCAR-F-Udemy05-0056, CCAR-P-jrajath94-0258</sub>
