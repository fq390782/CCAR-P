@@ ADD-TO: ### Headless / CI 실행
| 구분 | 내용 |
|---|---|
| 여러 대화 처리 | `-p` + `--output-format json`<br>→ 결과의 `session_id` 기록 |
| 특정 대화 재개 | `claude -p "<prompt>" --resume "$session_id"`<br>→ 재개 + 첫 후속 prompt를 한 명령으로 |

<sub>근거: CCAR-F-Udemy01-0051</sub>

@@ NEW-SECTION
### plan mode와 direct execution 선택
**불확실성 큰 작업 = plan · 범위 명확 = direct**

| 구분 | plan mode | direct execution |
|---|---|---|
| 규모 | 대규모 · 여러 파일 수정 | 작고 범위 명확한 변경 |
| 접근법 | 타당한 방법 2개 이상 | 방침 확정 |
| 판단 | 아키텍처 · 경계 결정 필요 | 원인 · 위치 특정 완료 |
| 코드 이해 | 낯선 코드 · 의존 관계 불명확 | 내용 충분히 이해 |
| 한 문장 기준 | diff를 한 문장으로 설명 ✗ | 한 문장 설명 가능<br>→ 계획 생략 |

| 단서 | 선택 |
|---|---|
| 파일 40~60개 이상 마이그레이션 · 구조 재편 | plan mode |
| 연동 방식 미정<br>(예: webhook · bot token · Slack App) | plan mode<br>→ 장단점 비교 후 방향 합의 |
| 영향 범위 큼 + 판단 여지 큼<br>(예: 전체 흐름 조사 후 방침 결정) | plan mode |
| 고칠 때마다 다른 곳이 깨짐<br>(공유 모듈 · fixture 얽힘) | plan mode<br>→ 의존 관계 파악 후 수정 |
| 의존 그래프 불명확 · 설계안 복수<br>과거 즉시 편집 → 광범위 rewrite · revert | plan mode<br>→ 편집 전 조사 먼저 |
| 접근 비교를 direct로 의뢰 → 편집 시작 → 되돌림 | plan mode<br>→ 탐색 · 설계와 편집 분리 |
| 설계 의견 대립 + 담당자가 코드에 낯섦 | plan mode + `AskUserQuestion` |
| 함수 1개 guard clause · 오타 · 로그 추가 | direct execution |
| 원인 행 특정 + 실패 test 보유 | direct execution<br>→ 수정 후 test 실행 |

<sub>근거: CCAR-F-Amey-Thakur-0041, CCAR-F-MyPractice-0032, CCAR-F-MyPractice-0034, CCAR-F-Udemy01-0015, CCAR-F-Udemy01-0057, CCAR-F-Udemy02-0004, CCAR-F-Udemy03-0005, CCAR-F-Udemy03-0009, CCAR-F-Udemy03-0011, CCAR-F-Udemy04-0050, CCAR-F-Udemy05-0055, CCAR-F-Udemy06-0012, CCAR-F-Udemy06-0057, CCAR-F-paullarionov-0032, CCAR-F-paullarionov-0034, CCAR-F-preporato-0020</sub>

@@ NEW-SECTION
### plan mode 운용과 권한 모드
**조사는 plan · 승인 뒤 direct로 전환**

| 구분 | 내용 |
|---|---|
| 성격 | 접근 방식을 사람이 검토하는 관문<br>모든 작업에 쓰는 것 ✗ · 위험 있을 때 |
| 동작 | 읽기 · 조사 → 계획 제시<br>승인 전 소스 편집 ✗ |
| Agent SDK | `permission_mode`="plan"<br>→ 탐색 · 계획만 수행 · 편집 ✗ |
| 비용 | 계획 왕복 = 오버헤드<br>→ 소규모 작업은 생략 |
| 권장 흐름 | 조사 = plan mode<br>→ 계획 승인 → 구현 = direct |
| 계획 편집 | 승인 전 `Ctrl+G`로 계획 수정<br>판단 갈리는 점 명기 → 이후 논의 감소 |
| 계획 요청 구성 | 실패 fixture · 공유 제약 · 검증 명령 포함<br>변경 범위 한정 (예: parser + 공유 fixture) |
| 계획 승인 조건 | 구 방식 동작의 재현 방법 명시 후 승인<br>(예: 구 library의 retry → 새 library) |
| 관련 결함 여러 개 | 범위 · 제약 · 검증 방법을 한 요청에 묶어<br>plan 시작 → 인수 test로 완료 판정<br>(예: 각 항목 1회만 표시되는지 확인) |

| 모드 | 동작 | 적합 |
|---|---|---|
| plan mode | 읽기 · 조사 + 계획 제시 | 방침 미정 · 영향 큼 |
| `acceptEdits` | 파일 편집 확인 생략 | 방침 확정 뒤 반복 작업 |
| `bypassPermissions` | 모든 확인 생략 | 격리 환경 무인 실행 |
| 직접 구현 | 변경 먼저 · 검토 사후 | 작고 명확한 변경 |

- 모드 선택 기준: 지금 편집을 시작해도 되는 단계인가

<sub>근거: CCAR-F-Amey-Thakur-0041, CCAR-F-Udemy01-0057, CCAR-F-Udemy02-0004, CCAR-F-Udemy03-0005, CCAR-F-Udemy03-0013, CCAR-F-Udemy04-0050, CCAR-F-Udemy05-0049, CCAR-F-Udemy05-0055, CCAR-F-Udemy06-0012, CCAR-F-Udemy06-0057</sub>

@@ NEW-SECTION
### 요구 불명확 시 인터뷰 패턴
**미확정 요건은 구현 전 인터뷰로 spec 확정**

1. 최소 prompt로 시작
2. `AskUserQuestion`으로 Claude가 인터뷰 (구현 · 엣지 케이스 · 우려 · trade-off)
3. 결과를 spec 문서(`SPEC.md`)로 정리
4. 새 session에서 구현 (인터뷰 대화 영향 ✗)

| 신호 | 판단 |
|---|---|
| 요건 미결<br>(무엇이 actionable? 무엇으로 검증?) | 구현 의뢰 전 인터뷰 |
| 개발자가 영역에 낯섦<br>(캐시 무효화 · 장애 모드 등) | 인터뷰로 설계 고려사항 발굴 |
| 과거 같은 방식 의뢰 → 고려 누락 → 재작업 | 질문으로 논점 발굴<br>+ 합의 내용을 수락 조건으로 spec화 |
| 설계 의견 대립 | `AskUserQuestion` 선택식 질문으로 합의 |

| 구분 | 내용 |
|---|---|
| 미결 요건 두고 의뢰 | Claude가 그럴듯한 전제로 빈틈 메움<br>→ 큰 재작업 |
| 계획 · 보수적 구현 · test 주도 | 요건 명확이 전제<br>→ 요건 부족 자체는 못 메움 |
| subagent | `AskUserQuestion` 사용 ✗ |
| 판별 질문 | 논점을 끌어내는 대화가 있는가 |

<sub>근거: CCAR-F-Udemy02-0019, CCAR-F-Udemy03-0006, CCAR-F-Udemy03-0011, CCAR-F-Udemy05-0042</sub>

@@ NEW-SECTION
### 예시 · test case로 요구 전달
**글 설명이 흔들리면 입출력 예시 · test case**

| 증상 | 조치 | 이유 |
|---|---|---|
| 글 요구를 매번 다르게 해석<br>(중첩 · timestamp · 단위 · 소수 자릿수) | 구체적 입출력 예시 2~3개 | 기대 변환을 직접 제시<br>→ 모호함 제거 |
| 글 수정 2~3회 → 다른 엣지 케이스가 깨짐 | 입력 + 기대 출력 test case | 기대값 유일 전달<br>+ 회귀 test |
| 설명 2회 → 다른 데이터에 같은 오류 | 구체적 test case<br>(예: null 처리) | 원인 = 검증 수단 부재<br>설명 추가 ✗ |
| 제안이 기존 것과 중복<br>(test 제안 10개 중 6개) | 기존 test 파일을 context에 포함 | 있는 것을 알아야 회피 가능 |

| 구분 | 내용 |
|---|---|
| 예시 보존 | 입출력 예시 → test case로 저장<br>→ 수정 후 기존 케이스 깨짐 확인 |
| 패턴 누적 | 발견된 엣지 케이스마다 test 추가<br>(null · 연호 · 미입력 · 전각 숫자) |
| 자가 검증 | Claude가 직접 실행해 합격 확인할 check 제공<br>→ 작업 · 확인 · 수정 loop 자력 반복 |
| 증상 해석 | 같은 오류 잔존 = 수정 정확성 확인 못 하고 종료 |
| 구분 기준 | 요건 확정 · 전달 방식만 문제 → 예시 |

<sub>근거: CCAR-F-MyPractice-0024, CCAR-F-MyPractice-0031, CCAR-F-Udemy04-0035, CCAR-F-Udemy04-0058, CCAR-F-Udemy06-0025, CCAR-F-Udemy06-0044, CCAR-F-paullarionov-0024, CCAR-F-paullarionov-0031</sub>

@@ NEW-SECTION
### 테스트 주도 반복과 요청 묶기
**test가 구현보다 먼저 · 연관 문제는 한 요청에**

| 구분 | 내용 |
|---|---|
| 테스트 선행 | suite 먼저 작성<br>→ 실패를 공유하며 단계적 개선 |
| test 포함 항목 | 기대 동작 · 엣지 케이스 · 성능 요건 |
| 구현 + test 동시 의뢰 | test가 구현 분기만 추종<br>→ 경계 조건 누락 (날짜 경계 · 상한 횟수) |
| 구현 후 커버리지 목표 · 일괄 의뢰 | test가 구현을 뒤따름 ✗ |
| 버그 발견 시 | 재현 test 먼저 추가 → 수정<br>→ 재발 방지 |
| 판별 기준 | test가 구현보다 먼저 요건을 정하는가 |

| 문제 관계 | 요청 방식 |
|---|---|
| 상호 영향<br>(한쪽 수정 → 다른 기대값 변경) | 단일 상세 메시지로 함께 |
| 독립 (CSV 열 순서 · 오타) | 순서대로 반복 |
| 상호 영향 문제를 함께 요청 | 기대 결과를 test case로 첨부 |

<sub>근거: CCAR-F-Udemy05-0005, CCAR-F-Udemy05-0048</sub>

@@ NEW-SECTION
### AI 작업물 merge 전 검증
**완료 보고는 주장 · 증거는 실행 · 검사 · 대조 · 스캔**

| 요소 | 확인 내용 |
|---|---|
| 실행 | test 실제 실행<br>(실행 안 한 test = 증명 ✗) |
| 검사 | 사람이 결과를 읽음 |
| 대조 | 보고한 주장 = 실행 결과 일치 |
| secret 스캔 | diff · fixture · 붙여넣은 로그에 secret ✗ |
| 의존 조건 | test가 수정 사항을 다룸<br>스캔이 키 형식을 인식 |

| 작업 | 필요한 증거 |
|---|---|
| 수정 완료 보고<br>(예: auth 모듈 "fixed") | 4요소 전부 |
| 리팩터링 후 "all green" | 수정 전 red 로그 + 수정 후 green 로그<br>→ PR에 첨부 |
| AI가 작성한 unit test | 실행 + 결과 검사 + secret 확인<br>(fixture = 유출 경로) |
| AI가 작성한 DB migration | diff 검토 · staging 실행<br>결과 점검 · secret 확인 → 기준 충족 |
| AI 작성 postmortem · 사고 요약 | 기술적 주장 검증 + secret 점검 |
| test 불가 작업 (repo 구조 요약) | 인용한 파일 경로<br>+ 동작 주장은 실행한 예제 |
| 부정 주장<br>(예: "재시도 로직 없음") | 파일 경로 + 실행 예제<br>파일 집합이 완전해야 함 |

| 원칙 | 내용 |
|---|---|
| 책임 | AI는 속도 활용 · 정확성 책임 = 엔지니어 |
| "AI가 썼다" | 검토됨 ✗ · 검증 = 사람의 일 |
| 약한 suite의 통과 | 검증 아님 |
| 미검증 요약에 따른 대응 | 엉뚱한 방향<br>(예: 잘못된 서비스 지목) |
| 모델 자기 보고 | 검증 ✗ |

| flaky test 단계 | 내용 |
|---|---|
| 1 증거 | 실패 증거 먼저 수집 |
| 2 진단 | 원인 진단 |
| 3 수정 | test 강도 유지 (assertion 삭제 ✗) |
| 4 검증 | 반복 실행으로 수정 확인 |

<sub>근거: CCAR-P-jrajath94-0061, CCAR-P-jrajath94-0266, CCAR-P-jrajath94-0267, CCAR-P-jrajath94-0270, CCAR-P-jrajath94-0273, CCAR-P-jrajath94-0329, CCAR-P-jrajath94-0393, CCAR-P-jrajath94-0456, CCAR-P-jrajath94-0519, CCAR-P-jrajath94-0582</sub>

@@ NEW-SECTION
### 증거 게이트 설계와 비례 적용
**merge를 게이트 · 강도는 실패 비용에 비례**

| 구분 | 내용 |
|---|---|
| revert 비율 상승 | 원인 = 검증 안 된 주장<br>→ 증거 기준으로 merge 게이트 |
| 게이트 구성 | hook이 매 편집마다 실제 suite 실행<br>로그 요건 · 주장 확인 · secret 스캔 |
| 전제 | hook = 실제 suite 실행<br>리뷰어 = 로그를 실제로 읽음 |
| 비용 논리 (문항 예시) | revert 9건 × $600 = $5,400/월<br>게이트 후 1건 → $600 → 절감 $4,800 |
| 한계 | 에이전트가 무검증 test로 gate 우회 가능<br>→ red-before-green 계속 필수 |
| red-before-green | 한 번도 실패 안 한 test = 증명 ✗<br>수정 전 red 실행 → test가 버그를 본다는 증명 |
| red 재현 비용 | agent 루프 1회 추가 · 재현 어려운 버그 존재<br>그래도 재현 = 신뢰의 대가 |

| 비례 원칙 | 내용 |
|---|---|
| gate 비용 > revert 비용 | gate 생략<br>(예: 주석 오타 = revert 10초 vs gate 20분) |
| 영향 범위가 사소하지 않은 변경 | gate가 더 저렴한 경로 |
| 사소함 판단 | 정직하게 분류<br>로직 건드리는 "오타" = 사소 ✗ |
| 오분류 | 필요한 gate 우회 |
| trade-off | 모든 편집에 10분 suite = 흐름에 세금<br>→ 변경 무게에 맞춤 |

<sub>근거: CCAR-P-jrajath94-0267, CCAR-P-jrajath94-0268, CCAR-P-jrajath94-0272</sub>

@@ NEW-SECTION
### session 이어가기 · fork · rewind
**특정 = resume · 최근 = continue · 분기 = fork**

| 방법 | 동작 | 용도 |
|---|---|---|
| `--continue` | 디렉터리 내 최신 대화 이어감 | 가장 최근 대화 |
| `--resume` + session ID | 지정한 대화 재개 | 특정 과거 대화 |
| fork | 원래 이력 복사 → 새 ID<br>원본 ID · 이력 불변 | 같은 기준점에서 분기 |

| 요건 | 정답 |
|---|---|
| 특정 과거 대화 + 터미널 + 첫 후속 prompt | `claude -p "<prompt>" --resume "$session_id"` |
| 같은 baseline에서 전략 2개 비교<br>추론 혼입 ✗ · 원본 보존 | fork 2개<br>→ 각각 독립 재개 |
| 일반 재개 · continue | 같은 대화에 추가<br>→ 혼입 · 원본 덮어쓰기 불가피 |
| 폴더 복제 | ✗ session은 작업 디렉터리 대응<br>`~/.claude/projects` 아래 저장 |
| fork의 한계 | 분리 = 대화 이력 · 파일 ✗<br>파일 편집 시 별도 작업 트리 · checkpoint 병용 |

| 되돌릴 대상 | 수단 |
|---|---|
| Claude가 편집한 파일 | rewind<br>(session이 유지하는 checkpoint 범위 내) |
| Bash 명령으로만 바뀐 파일 | rewind 추적 ✗<br>→ 버전 관리로 되돌림 |
| 두 종류 모두 | rewind + 버전 관리 병용 |
| rewind 성격 | 사후 복구 수단 · 사전 차단 ✗ |

<sub>근거: CCAR-F-Udemy01-0051, CCAR-F-Udemy03-0001, CCAR-F-Udemy06-0057, CCAR-P-jrajath94-0709</sub>

@@ NEW-SECTION
### 운영 agent 지연 · 유실 · 추적
**지연은 context 먼저 · 유실은 checkpoint + trace**

| 증상 | 조치 |
|---|---|
| p95 지연 급증 | runbook 순서<br>context 크기 → 의존성 지연 → 캐시 적중률 |
| 프롬프트 변경으로 평균 context 12,000 → 90,000 토큰 | context 축소 = 근본 원인 수정<br>(전체 이력 → 최근 N건) |
| 하루 지나며 느려짐 (아침 정상) | context · 의존성 조사<br>(하루에 걸친 증가 = 전형 패턴) |
| 축소 시 주의 | 후속 단계 필요 항목 유지<br>context 크기 경보를 runbook에 추가 |
| 모델 업그레이드 · 로그 증설 · reviewer 추가 | 근본 원인 ✗ (대리 수정) |

| 유실된 실행 | 내용 |
|---|---|
| 필요한 아티팩트 | checkpoint (재개 지점)<br>trace (완료 단계 · 출력) |
| 재개 vs 재시작 | 재시작 = 부수 효과 중복 가능<br>→ 재개 |
| 재시작 허용 | 실행이 idempotent · 저렴 + checkpoint 없음 |
| 더 큰 context window | 유실된 실행 기록 없음 → 복구 ✗ |
| 조건 | checkpoint = plan 상태 포함<br>trace = 처음부터 끝까지 재구성 가능 |
| 비용 | checkpoint = handoff마다 비용<br>trace = 보존 필요 |

| 관측성 | 내용 |
|---|---|
| 증상 | tool call ↔ 사용자 요청 재구성에 몇 시간<br>(request ID 없음 · 자유 텍스트 tool 결과) |
| 투자 | 전파되는 request ID + 구조화된 tool I/O |
| 이유 | 진단 = 상관관계 파악<br>ID 없는 로그 증가 = 건초 더미 증가 |

<sub>근거: CCAR-P-jrajath94-0105, CCAR-P-jrajath94-0274, CCAR-P-jrajath94-0278, CCAR-P-jrajath94-0520</sub>

@@ NEW-SECTION
### 내장 검색 도구 Glob · Grep · Read
**이름 단서 = Glob · 내용 단서 = Grep**

| 도구 | 검색 기준 | 용도 |
|---|---|---|
| `Glob` | 파일 이름 패턴 | 이름으로 파일 찾기 |
| `Grep` | 파일 안의 줄 (ripgrep 기반) | 코드 속 문자열 · 참조 찾기 |
| `Read` | 지정한 파일 | 알려진 파일 읽기<br>횡단 검색 ✗ |

| `Grep` 파라미터 | 역할 |
|---|---|
| `pattern` | 찾을 문자열 |
| `glob` | 파일 범위 한정 (예: `**/*.ts`) |
| `output_mode` = `files_with_matches` | 기본값 · 경로만 |
| `output_mode` = `content` | 일치 행 + 파일명 + 행 번호 |
| `output_mode` = `count` | 건수 |

| 요건 | 구성 |
|---|---|
| 이름에 없는 필드명을 쓰는 파일 탐색 | `Grep` (내용 검색) |
| 함수 참조 전부 + TypeScript만 + 바로 점프 | `pattern` = 함수명<br>`glob` = `**/*.ts`<br>`output_mode` = `content` (행 번호) |
| 판별 기준 | `glob` = 어디를 찾나<br>`output_mode` = 무엇을 돌려받나 |

| 구분 | 내용 |
|---|---|
| ⚠️ 기본 도구 세트 | macOS · Linux · WSL = Glob · Grep 기본 제외<br>→ Bash `find` · `grep`으로 검색<br>플랫폼 · 버전에 따라 변동 가능 (문항은 활성화 전제) |

<sub>근거: CCAR-F-Udemy01-0049, CCAR-F-Udemy03-0035</sub>

@@ NEW-SECTION
### 자동 리뷰 · skill 출력 품질 측정
**측정 단위 = 오류가 몰린 단위**

| 상황 | 조치 |
|---|---|
| 전체 채택률 높음 + 오류가 일부 필드에 집중 | 필드 단위 confidence 출력<br>→ 라벨 달린 검증 예시로 정확도 대응 확인<br>→ 임계값 calibration 후 리뷰 축소 |
| 일부 분류의 오탐 많음<br>→ 개발자가 리뷰 전체 무시 · mute | 분류별 precision · recall 측정<br>→ 노이즈 큰 검사 좁히기 · 일시 중지 |
| 오탐 원인이 알려진 패턴<br>(plugin entry point · reflection 참조) | 제외 대상으로 명시 → 재발 방지 |

| 구분 | 내용 |
|---|---|
| 성공 기준 | 구체적 · 측정 가능 |
| 평가 데이터 | 실제 작업을 반영한 test case |
| 집계값 (전체 채택률 · 단일 점수) | 편향을 평균에 묻음 → 문제 소재 은폐 |
| 판별 기준 | 측정 단위 = 문제 단위 |

<sub>근거: CCAR-F-Udemy03-0033, CCAR-F-Udemy03-0049</sub>

@@ NEW-SECTION
### API 운영 설정 key · workspace · 버전 이행
**유출 범위 분리 · 환경별 workspace · 제거 파라미터 삭제**

| 구분 | 내용 |
|---|---|
| 문제 | key 1개를 모든 환경 · CI job이 공유 → 유출 시 추적 ✗ |
| 범위 한정 | 유출된 key가 할 수 있는 일 제한 |
| 환경별 key | 피해가 미치는 곳 제한 + 추적성 확보 |
| 교체 · 폐기 | 유출이 의미 있는 기간 제한 |
| 요건 | blast radius 축소 + 사용 내역 추적 |

| 요건 | 조치 |
|---|---|
| 개발 · 프로덕션 별도 rate limit + 비용 보고서 | 환경마다 workspace 분리<br>(요청은 정확히 1 workspace에서 실행) |
| Default Workspace | 이름 변경 ✗ → 새 workspace 생성 |

| 증상 | 조치 |
|---|---|
| API 버전 이행 후 모든 요청 400<br>(`temperature` 전송) | 제거된 파라미터 삭제<br>+ release 전 test gate 통과 |
| ⚠️ 시점 의존 | 특정 API 버전 기준 내용<br>→ 공식 migration 문서에서 확인 필요 |

<sub>근거: CCAR-P-jrajath94-0104, CCAR-P-jrajath94-0698, CCAR-P-jrajath94-0700</sub>

@@ RULES
| 상황 | 정답 |
|---|---|
| 대규모 · 여러 파일 · 복수 접근법 · 아키텍처 결정 | plan mode 조사 · 계획 → 승인 후 구현 |
| 접근 방식 비교가 목적 | plan mode<br>(비교 전 편집 차단) |
| 함수 1개 수정 · 오타 · 원인 특정 + 실패 test | direct execution |
| diff를 한 문장으로 설명 가능 | 계획 생략 |
| 설계 의견 대립 + 담당자가 코드에 낯섦 | plan mode + `AskUserQuestion` |
| 요건 미결 · 낯선 영역 · 과거 고려 누락 | 인터뷰 → spec → 새 session 구현 |
| 글 설명을 매번 다르게 해석 | 입출력 예시 2~3개 |
| 수정 반복해도 엣지 케이스가 깨짐 | 입력 + 기대 출력 test case |
| 같은 오류가 다른 데이터에서 반복 | Claude가 실행할 검증 수단(test) 제공 |
| 자동 리뷰 제안이 기존 test와 중복 | 기존 test 파일을 context에 포함 |
| 구현 + test 동시 의뢰 → 경계 조건 누락 | test 선행 (동작 · 엣지 · 성능) |
| 상호 영향 문제 vs 독립 문제 | 단일 상세 메시지 vs 순차 반복 |
| 여러 곳에 걸친 관련 결함 | plan mode + 인수 test |
| "fixed" 보고 후 merge 직전 | 실행 · 검사 · 대조 · secret 스캔 |
| "all green"의 신뢰 근거 | 수정 전 red → 수정 후 green 로그 |
| test 불가 작업의 증거 | 인용한 파일 경로 + 실행한 예제 |
| agent PR의 revert 증가 | 증거 기준 merge 게이트 |
| 사소한 변경 + revert 비용 < gate 비용 | gate 생략 |
| flaky test 수정 | 증거 → 진단 → 강도 유지 수정 → 반복 실행 |
| 특정 과거 대화 + 첫 후속 prompt | `claude -p "<prompt>" --resume "$session_id"` |
| 같은 baseline에서 갈래 비교 | fork |
| Bash로 바뀐 파일까지 되돌림 | rewind + 버전 관리 |
| 파일 이름 단서 vs 내용 단서 | `Glob` vs `Grep` |
| agent 지연 증가 | context 크기 → 의존성 → 캐시 순 점검 |
| 유실된 agent 실행 복구 | checkpoint + trace 재개 |
| trace 재구성에 몇 시간 | request ID 전파 + 구조화된 tool I/O |
| 전체 채택률 높은데 일부 필드 오류 | 필드별 confidence + 라벨 검증 데이터로 calibration |
| 일부 분류 오탐으로 리뷰 무시 | 분류별 precision · recall + 제외 대상 명시 |
| 공유 key 유출 | 환경별 key + 범위 한정 + 교체 · 폐기 |
| 환경별 rate limit · 비용 보고 | 환경별 workspace |
| API 버전 이행 후 400 | 제거 파라미터 삭제 + test gate |

<sub>근거: CCAR-F-Amey-Thakur-0041, CCAR-F-Udemy01-0049, CCAR-F-Udemy01-0051, CCAR-F-Udemy02-0019, CCAR-F-Udemy03-0001, CCAR-F-Udemy03-0005, CCAR-F-Udemy03-0006, CCAR-F-Udemy03-0009, CCAR-F-Udemy03-0011, CCAR-F-Udemy03-0013, CCAR-F-Udemy03-0033, CCAR-F-Udemy03-0035, CCAR-F-Udemy03-0049, CCAR-F-Udemy04-0035, CCAR-F-Udemy04-0050, CCAR-F-Udemy05-0005, CCAR-F-Udemy05-0042, CCAR-F-Udemy05-0048, CCAR-F-Udemy05-0055, CCAR-F-Udemy06-0025, CCAR-F-Udemy06-0044, CCAR-F-paullarionov-0024, CCAR-F-paullarionov-0031, CCAR-P-jrajath94-0061, CCAR-P-jrajath94-0104, CCAR-P-jrajath94-0105, CCAR-P-jrajath94-0266, CCAR-P-jrajath94-0267, CCAR-P-jrajath94-0268, CCAR-P-jrajath94-0270, CCAR-P-jrajath94-0272, CCAR-P-jrajath94-0274, CCAR-P-jrajath94-0278, CCAR-P-jrajath94-0698, CCAR-P-jrajath94-0700, CCAR-P-jrajath94-0709</sub>

@@ TRAPS
| 오답 | 이유 |
|---|---|
| 모든 작업에 plan mode | 계획 왕복 = 오버헤드<br>작은 수정은 직접 요청 |
| 복잡한 작업을 direct로 시작<br>(`acceptEdits` · `bypassPermissions` 포함) | 변경 먼저 · 검토 사후<br>→ 되돌림 비용 |
| 편집이 시작된 뒤 `/rewind`로 대응 | 사후 복구 수단<br>비교 전 편집을 막지 못함 |
| `CLAUDE.md` 지시로 비교 전 편집 금지 | 확률적 준수 |
| 작은 수정에 plan mode · 인터뷰<br>· Explore subagent | 불확실성 큰 작업용 기법 → 과함 |
| 관련 결함을 session별 분리 · 계획 생략 | 연동된 원인 분단<br>범위 큰 변경이 무질서 |
| fixture별 직접 편집 + context 초기화 | 의존 관계 미확인 변경 반복 |
| 요건 미결 상태에서 직접 실행 · 자율 job · 설계서 단독 작성 | 논점 도출 대화 생략<br>→ 추측으로 채움 |
| subagent로 인터뷰 진행 | `AskUserQuestion` 사용 ✗ |
| 글 설명 추가 · `CLAUDE.md` 규칙 추가 · 지적 반복 | 모두 글 설명 의존<br>→ 해석 흔들림 그대로 |
| 요건 확정인데 인터뷰 · plan mode · 함수 지정 | 목적 다름<br>(함수 지정 = 범위 문제) |
| 구현 후 커버리지 목표 · 일괄 의뢰 | test가 구현을 뒤따름 |
| 문제를 전부 한 메시지로 · 상호 영향 문제를 따로 수정 | 독립 문제 섞임<br>정합성 상실 |
| 산문 보고 · 오래된 green 배지 · 작성 줄 수로 merge 판단 | 주장일 뿐 증거 ✗<br>지난주 green은 이번 편집과 무관 |
| test 수 · 반복 실행 · green만으로 신뢰 | 빈 assertion 200개 = 0이 200개 |
| 확신 문구 · 긴 요약 · 열람 파일 수 · 프롬프트 스크린샷 | 포인터 ✗ · 노력 · 요청만 보여 줌 |
| flaky 수정 = assertion · test 삭제<br>· AI 사용 중단 | 커버리지 파괴<br>도구를 올바르게 쓴 것 ✗ |
| revert 증가 대응 = 모델 교체 · PR 물량 · 속도 · 도입률 | 미검증 주장(원인)에 대응 ✗ |
| 모든 변경에 gate · 오타 방치 · 주석에 회의 | 비용 불균형<br>(gate 절대주의) |
| 모델 자기 보고 · 문장 다듬기 · 서식 | 검증 아님 |
| 지연 → 모델 업그레이드 · 로그 증설 · reviewer 추가 | 근본 원인(context) 미해결 |
| 유실 실행 → 재시작 · 더 큰 window · 사과 | 부수 효과 중복 · 기록 없음 |
| trace 개선 = 로그 verbosity · 큰 모델 · 서술형 요약 | 상관관계 ID 없음 |
| `--continue`로 특정 대화 · prompt에 ID 붙여넣기 | `--continue` = 최근만<br>prompt 속 ID = 재개 지시 ✗ |
| 폴더 복제 · 일반 resume으로 전략 비교 | 혼입 · 원본 덮어쓰기 |
| `Esc` 두 번 = 전체 되돌리기 | Bash 변경은 rewind 추적 ✗ |
| fork가 파일 변경도 분리 | 대화 이력만 분리 |
| `Glob`으로 내용 검색 · commit 이력 검색<br>· `Read`로 훑기 | `Glob` = 이름만<br>commit 이력 = 현재 참조 위치 ✗<br>`Read` = 횡단 검색 부적합 |
| `Glob` 목록 → 전문 `Read`<br>· `files_with_matches` 유지 | context 낭비<br>행 번호 · 문맥 없음 |
| 단일 품질 점수 · 파일 단위 confidence · 전체 채택률 | 편향을 평균에 묻음 |
| 오탐 대응 = 심각도 상향 | 노이즈 그대로 |
| 공유 key 월 교체 · secrets manager<br>· key 사본 증가 | 교체 사이 key 1개가 전부 접근<br>저장 보호일 뿐<br>유출 표면 증가 |
| Default Workspace 이름 변경 | 이름 변경 불가 |
| 400 오류에 backoff retry | 파라미터 자체가 원인 |

<sub>근거: CCAR-F-Udemy01-0015, CCAR-F-Udemy01-0049, CCAR-F-Udemy01-0051, CCAR-F-Udemy01-0057, CCAR-F-Udemy02-0004, CCAR-F-Udemy02-0019, CCAR-F-Udemy03-0001, CCAR-F-Udemy03-0005, CCAR-F-Udemy03-0006, CCAR-F-Udemy03-0009, CCAR-F-Udemy03-0013, CCAR-F-Udemy03-0033, CCAR-F-Udemy03-0035, CCAR-F-Udemy03-0049, CCAR-F-Udemy04-0035, CCAR-F-Udemy04-0058, CCAR-F-Udemy05-0005, CCAR-F-Udemy05-0042, CCAR-F-Udemy05-0048, CCAR-F-Udemy05-0055, CCAR-F-Udemy06-0025, CCAR-F-Udemy06-0044, CCAR-F-Udemy06-0057, CCAR-P-jrajath94-0061, CCAR-P-jrajath94-0104, CCAR-P-jrajath94-0105, CCAR-P-jrajath94-0266, CCAR-P-jrajath94-0267, CCAR-P-jrajath94-0268, CCAR-P-jrajath94-0270, CCAR-P-jrajath94-0272, CCAR-P-jrajath94-0273, CCAR-P-jrajath94-0274, CCAR-P-jrajath94-0278, CCAR-P-jrajath94-0329, CCAR-P-jrajath94-0698, CCAR-P-jrajath94-0700, CCAR-P-jrajath94-0709</sub>

@@ MEMO
| 이름 | 의미 |
|---|---|
| `AskUserQuestion` | 선택식 질문 도구<br>인터뷰에 사용 · subagent 사용 ✗ |
| `SPEC.md` | 인터뷰 결과 spec 문서<br>→ 새 session에서 구현 |
| `acceptEdits` | 파일 편집 확인 생략 |
| `permission_mode`="plan" | Agent SDK의 plan mode |
| `Ctrl+G` | 승인 전 계획 편집 |
| `--continue` | 가장 최근 대화 이어가기 |
| `--resume` + session ID | 특정 대화 재개 |
| fork | 이력 복사 · 새 ID · 원본 불변 |
| `~/.claude/projects` | session 저장 위치 |
| rewind | Claude가 편집한 파일 복원<br>(checkpoint 범위 내) |
| `Glob` | 파일 이름 패턴 검색 |
| `Grep` | 파일 내용 검색 · ripgrep 기반 |
| `output_mode` | `files_with_matches`(기본)<br>· `content` · `count` |
| red-before-green | 수정 전 실패 test로 탐지 증명 |
| 증거 4요소 | 실행 · 검사 · 대조 · secret 스캔 |
| precision · recall | 분류별 품질 측정 지표 |
| calibration | 검증 데이터로 confidence 임계값 보정 |
| blast radius | key 유출 시 피해 범위 |
| workspace | 환경별 key · rate limit · 비용 보고 단위 |
| request ID | trace 상관관계 키 |

<sub>근거: CCAR-F-Udemy01-0049, CCAR-F-Udemy01-0051, CCAR-F-Udemy02-0004, CCAR-F-Udemy02-0019, CCAR-F-Udemy03-0001, CCAR-F-Udemy03-0006, CCAR-F-Udemy03-0033, CCAR-F-Udemy03-0035, CCAR-F-Udemy03-0049, CCAR-F-Udemy04-0050, CCAR-F-Udemy05-0049, CCAR-P-jrajath94-0104, CCAR-P-jrajath94-0105, CCAR-P-jrajath94-0266, CCAR-P-jrajath94-0267, CCAR-P-jrajath94-0700, CCAR-P-jrajath94-0709</sub>

@@ CHECK
- [ ] plan mode = 범위 큼 · 방침 미정, direct = 한 문장 설명 가능
- [ ] 글 설명이 흔들리면 입출력 예시 · test case
- [ ] "fixed" 보고 → 실행 · 검사 · 대조 · secret 스캔
- [ ] 특정 대화 = `--resume` · 최근 = `--continue` · 분기 = fork

<sub>근거: CCAR-F-Udemy01-0051, CCAR-F-Udemy03-0001, CCAR-F-Udemy04-0050, CCAR-F-Udemy05-0049, CCAR-F-Udemy06-0025, CCAR-F-paullarionov-0031, CCAR-P-jrajath94-0266</sub>
