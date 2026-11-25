@@ ADD-TO: ### Headless / CI 실행

| 구분 | 내용 |
|---|---|
| headless 적합 | 범위 분명 · 반복 가능 · 무인 실행<br>예: 모든 PR마다 도는 명세 분명한 검사 |
| headless 부적합 | 탐색적 디버깅 · 아키텍처 설계 · pair programming<br>= 사람 개입 필요 → interactive |
| 적합성 기준 ✗ | 도구 수 · 출력 길이 |
| 멈춤 원인 ① | `claude "..."` = 대화형 시작 → 입력 대기<br>→ `-p`(`--print`)로 시작 |
| 멈춤 원인 ② | 후속 확인 prompt에 응답할 사람 없음<br>→ 필요 도구 사전 승인 (`--allowedTools` · 권한 설정) |
| 무인 실행 조건 | 실행 모드 + 권한, 2곳 모두 사람 대기 제거 |
| 점검 순서 | 자동화 멈춤 → 시작 모드가 사람 입력 전제인지 먼저 확인 |

| 출력 · 결과 처리 | 내용 |
|---|---|
| `--output-format text` | 기본값 · 평문 |
| `--output-format json` | 결과 + session ID · 비용 등 metadata 묶음 |
| `--output-format stream-json` | 실행 중 이벤트 순차 전송<br>= 리뷰 결과 자체 ✗ |
| `--json-schema` + `json` | schema 적합 데이터<br>→ 결과 JSON의 `structured_output` 필드 |
| 비용 · 소요시간 | `json` 출력 metadata에서 읽기<br>(예: `total_cost_usd`) |
| 요건 분리 | 내용 형식 = `--json-schema`<br>실행 기록 = `json` metadata |
| 성공 판정 | 종료 코드 0 = 성공 · 0 아님 = 실패<br>→ 스크립트가 종료 상태로 분기 |
| 집계 값 | 사람이 읽는 문장 정규식 추출 ✗<br>→ `structured_output`에서 읽기 |
| prompt 서식 지시 | "마지막 줄에 `N` 형식" 지시<br>→ 표현 흔들림 확률적으로 잔존 ✗ |
| PR inline 코멘트 자동화 | `-p` + `json` + `--json-schema`<br>→ file path · line · severity · 수정 제안 필드 강제 |
| 코멘트 게시 | 출력 파싱 → GitHub API로 inline 게시 |
| schema 없는 prompt 지시 | 검증 구조 없음 → 유효 데이터 보장 ✗ |

| 도구 · context | 내용 |
|---|---|
| `--tools` | 실행에 존재하는 내장 도구 제한<br>예: Read · Grep만 |
| `--allowedTools` | 나열 도구를 prompt 없이 실행 허용<br>= 제한 ✗ |
| 제한 + 실패 시 job 실패 | `--tools` + `claude -p`<br>→ 다음 CI 단계에서 종료 상태 확인 |
| `--bare` | `CLAUDE.md` 포함 자동 탐색 생략<br>→ 프로젝트 규약 미로드 |
| `--bare`의 context 전달 | `--append-system-prompt-file` 등 플래그 |
| 증상 판별 | 일부 규약 위반이 아니라 전면 미사용<br>→ 규약 전체 미전달 변경 의심 |
| 로드와 무관한 것 | `--output-format` 지정 · 비대화형 모드 |
| CI 명령 변경 | 소수 PR로 규약 준수 확인 → 전체 적용 |
| ⚠️ `--bare` | 공식 문서에 "향후 `-p` 기본값 예정" 기재<br>→ 버전별 `CLAUDE.md` 로드 동작 달라질 수 있음 · 확인 필요 |

<sub>근거: CCAR-F-Amey-Thakur-0006, CCAR-F-Amey-Thakur-0019, CCAR-F-Amey-Thakur-0046, CCAR-F-Amey-Thakur-0056, CCAR-F-MyPractice-0016, CCAR-F-MyPractice-0026, CCAR-F-Udemy01-0034, CCAR-F-Udemy02-0005, CCAR-F-Udemy03-0039, CCAR-F-Udemy04-0001, CCAR-F-Udemy05-0039, CCAR-F-paullarionov-0016, CCAR-F-paullarionov-0026, CCAR-P-jrajath94-0704, CCAR-P-jrajath94-0705</sub>

@@ NEW-SECTION
### CI PR 리뷰 설계
**리뷰는 수정 session과 분리 · 이전 결과는 context로**

| 리뷰 독립성 | 내용 |
|---|---|
| 자기 리뷰 | 코드를 생성한 같은 session = 독립 리뷰보다 효과 낮음<br>(`--continue` · `--resume` = 같은 대화 이어감) |
| 독립 리뷰 | `--continue` 없는 별도 `claude -p` 실행<br>또는 새 context의 subagent |
| 효과 | 수정 시 추론 없이 diff 평가 → 편향 제거 |
| 리뷰 job 입력 | diff + `CLAUDE.md`(리뷰 기준)만 |
| 작성자 무관 | Claude 작성 PR도 사람 PR과 같은 리뷰 workflow |
| 이상 신호 | 사람 PR 대비 Claude PR 지적률 극단적으로 낮음<br>+ merge 후 결함이 Claude 변경에 집중 |
| 판별 질문 | 리뷰하는 context에 수정 시 대화가 남아 있는지 확인 |

| 재리뷰 중복 | 내용 |
|---|---|
| 증상 | push 후 재리뷰가 이미 고친 코드에 같은 코멘트 반복 |
| 해법 | 이전 리뷰 결과를 context에 포함<br>+ "새 문제 · 미해결 문제만 보고" 지시 |
| 효과 | Claude가 해결된 문제와 새 문제 구분 → 철저함 유지 |
| 관리형 Code Review | `@claude review once` = 단발 리뷰<br>`@claude review always` = push마다 리뷰 구독 |
| `REVIEW.md` | 리뷰 전용 지시<br>(심각도 정의 · 지적 건수 상한 · skip 규칙 · 이미 리뷰된 PR 동작) |
| 관리형 재리뷰 중복 | `REVIEW.md`에 "과거 지적 고려, 새 · 미해소만 보고" 기재 |
| ⚠️ `REVIEW.md` 재리뷰 지시 | 해설 기준 · 공식 customize 문서에서 해당 항목 직접 확인 ✗<br>→ 검증 필요 |
| 기동 방식 변경 | `review always` · Checks 재실행 · 수작업 close<br>= 리뷰 내용 불변 → 중복 원인 그대로 |

| PR 리뷰 봇 | 내용 |
|---|---|
| 범위 | 기계적 검사 한정 (테스트 존재 · 스타일 · 명백한 버그)<br>문서화된 팀 규칙 기준 |
| 출력 | 리뷰 코멘트 게시 → 결정권 = 사람 |
| 권한 | merge 금지 · 승인 = 사람 → 자율 승인 방지 |
| 효과 | 리뷰어 = 설계에 집중 · 기계적 항목 지연 감소 |

<sub>근거: CCAR-F-MyPractice-0025, CCAR-F-Udemy02-0025, CCAR-F-Udemy04-0051, CCAR-F-Udemy06-0058, CCAR-F-paullarionov-0025, CCAR-P-jrajath94-0062</sub>

@@ NEW-SECTION
### CI 테스트 생성 품질
**diff만 주지 말고 기존 테스트 · 규약을 보여준다**

| 구분 | 내용 |
|---|---|
| 증상 | 기존 테스트와 같은 시나리오 반복<br>`conftest.py` fixture와 같은 helper 재정의 |
| 원인 | job이 diff만 전달 → 기존 테스트 · fixture 존재 모름 |
| 해법 ① | 대상 모듈 기존 테스트 + `conftest.py` 읽기<br>→ 기존 시나리오 제외 |
| 해법 ② | 테스트 표준 · 좋은 테스트 기준 · 사용 가능 fixture<br>→ 저장소 `CLAUDE.md`에 커밋 |
| `CLAUDE.md` 역할 | CI의 Claude Code에 프로젝트 context 전달<br>(테스트 표준 · fixture 규약 · 리뷰 기준) |
| 개인정보 | 규약에 "개인 식별 값은 fixture 외 사용 금지" 명시<br>+ PR 리뷰에서 확인 → 이중 방어 |
| 전달 정보 기준 | 중복 판단에 도움 + 양 적절 |
| 전제 | `CLAUDE.md`가 실제 로드될 때만 효과 (`--bare` 주의) |

<sub>근거: CCAR-F-Udemy04-0001, CCAR-F-Udemy05-0007, CCAR-F-Udemy06-0033</sub>

@@ NEW-SECTION
### 팀 도입 · 표준화 (enablement)
**공유 기준선 = 저장소에 커밋 + 코드처럼 리뷰**

| 상황 | 정답 방향 |
|---|---|
| 팀별 구성 어긋남 · 신규 입사자 적응 지연 | 공유 기준선 제공<br>→ 팀별 규칙은 그 위에 추가 |
| 기준선 구성 | 버전 관리되는 팀 구성<br>공통 skills · commands<br>온보딩 경로 |
| 여러 저장소 일관 활용 | 각 저장소에 project memory + 공유 skills 커밋<br>→ 코드처럼 리뷰 |
| 파트너 팀 도입 | 기준선 구성과 동일 → 일회성 인수인계 ✗ |
| 지속 원리 | 관례가 저장소 안에 있고 작업과 함께 리뷰될 때 유지 |
| 정책 문서 · 교육 | 시간이 지나면 희미해짐 |

<sub>근거: CCAR-P-Amey-Thakur-0010, CCAR-P-Amey-Thakur-0033, CCAR-P-Amey-Thakur-0049, CCAR-P-Amey-Thakur-0065</sub>

@@ NEW-SECTION
### 성과 · 생산성 · 비용 측정
**활동량이 아니라 성과 · 살아남은 작업을 측정**

| 대상 | 정답 지표 |
|---|---|
| enablement · 라이선스 가치 | 도입 목적이었던 전달 성과의 변화 |
| 에이전트 생산성 ① | 증거 게이트 이후 에이전트 PR의 revert 비율<br>= merge된 작업의 생존 |
| 에이전트 생산성 ② | 검사된 결과가 담긴 실행 로그 포함 PR 비율<br>= 증거 규율 |
| 사용량 지표 = 이익 ✗ | 교육 인원 · 온보딩 수 · 라이선스 활용률<br>도구 호출량 · 사용 시간 |
| 활동 지표 = 생산성 ✗ | 생성 코드 줄 수 = 물량 지표 함정<br>개발자별 토큰 = 비용 귀속 지표<br>에이전트 실행 시간 = 런타임 지표 |
| revert 비율 한계 | 느림 · revert 원인 라벨링 필요<br>(에이전트 잘못 / 사람 잘못 분리) |
| 로그 비율 한계 | 빈 로그로도 좋아 보임<br>→ red-before-green 증명 병행 |

| 비용 통제 | 내용 |
|---|---|
| 지출 가드레일 | 작업별로 저렴한 모델 라우팅<br>+ 월간 지출 수치에 담당자 지정 · 검토 |
| 비용 통제 오해 | AI 덜 쓰기 ✗<br>→ 충분한 성능의 가장 저렴한 모델로 라우팅 + 총액 감시 |
| 담당자 있는 수치 | 깜짝 청구 → 감시 대상 편차로 전환 |
| 전제 | 작업-모델 매핑 정의 · 유지 필요<br>잘못된 매핑 = 어려운 작업이 약한 모델로 → 품질 하한선 보존 |

<sub>근거: CCAR-P-Amey-Thakur-0034, CCAR-P-Amey-Thakur-0079, CCAR-P-jrajath94-0263, CCAR-P-jrajath94-0271</sub>

@@ NEW-SECTION
### 운영 런북 · 증상별 점검 순서
**추측 대신 증상 → 용의 대상 순서로 점검**

| 증상 | 점검 순서 |
|---|---|
| tool 호출 실패<br>(코드 불변 · 권한 변경 · 마이그레이션 후) | 자격 증명 · 토큰 만료<br>→ 권한 (서비스 ID scope) → 스로틀링 (할당량)<br>→ tool 계약 |
| 비용 급증<br>(품질 · 지연 불변 · 배포 없음) | ① 라우팅: 저렴한 작업이 비싼 모델로 가는지<br>② 컨텍스트: 호출마다 과대 · 중복<br>③ 캐싱: 적중률 하락 |
| 품질 저하<br>(프롬프트 불변 · 코드 불변) | 맵 순서 = 프롬프트 → 모델 → retrieval drift<br>알려진 변경 계층부터 (예: reindex → retrieval)<br>eval 재실행 → 하락 실재 · 위치 확인 |

| 점검 원칙 | 내용 |
|---|---|
| 원인 규명 먼저 | 원인 확인 전 절감 ✗<br>품질 하한선 아래로 감축 ✗ |
| 코드 불변 | 원인은 코드 바깥<br>(자격 증명 · 권한 · 스로틀링 · 계약) |
| 점검 신호 | 인증 로그 = 토큰 만료<br>제공자 헤더 = 스로틀링<br>reindex 전후 eval 분할 = retrieval |
| 비용 사전 계측 | tier별 · 단계별 비용 내역 + 작업별 귀속<br>없으면 누수가 합계에 숨음 |

| 런북 | 내용 |
|---|---|
| 필수 요소 | 순서 정해진 증상-용의 대상 점검 (맵)<br>지정 담당자 + escalation 경로 |
| 본질 | 담당자 있는 절차 → 영웅 의존 종료<br>담당자 없는 문서 = wiki 페이지 |
| 새로운 실패 (일치 항목 없음) | 설계자 호출 → 조사<br>장애 후 리뷰에서 새 항목으로 런북 갱신 |
| 유지보수 | 장애마다 갱신<br>장애 리뷰 = 유지보수 계약 (산출물 = 런북 수정) |
| 낡음 | 런북은 ADR처럼 낡음 → 시스템 변경 후 방치 시 오도 |
| 한계 | 런북 = 알려진 실패만 다룸<br>새 실패는 사람이 조사 → 이후 런북 성장 |

<sub>근거: CCAR-P-jrajath94-0275, CCAR-P-jrajath94-0276, CCAR-P-jrajath94-0277, CCAR-P-jrajath94-0279, CCAR-P-jrajath94-0280, CCAR-P-jrajath94-0281, CCAR-P-jrajath94-0330, CCAR-P-jrajath94-0394, CCAR-P-jrajath94-0457, CCAR-P-jrajath94-0583</sub>

@@ NEW-SECTION
### 에이전트 구성 배포 (canary · rollback)
**구성 변경도 canary로 검증 · 한 명령으로 복구**

| 구분 | 내용 |
|---|---|
| 증상 | 배포 후 agent가 오래된 지시 사용<br>이름 바뀐 tool에서 루프<br>(`CLAUDE.md` · MCP 서버 구성 변경 직후) |
| 요건 | 전체 롤아웃 전 검증 + 문제 시 빠른 복구 |
| canary | 새 `CLAUDE.md` · MCP 구성을 소규모 그룹에 먼저 롤아웃 |
| smoke test | 좋은 출력이 있는 샘플 작업 실행<br>→ 실패 시 배포 자동 중단 |
| rollback | 이전 구성 유지 → 한 번의 명령으로 복구 |
| changelog | 구성 changelog 필수 → fleet 행동 감사 가능 |

<sub>근거: CCAR-P-jrajath94-0064</sub>

@@ RULES
| 상황 | 정답 |
|---|---|
| CI에서 `claude "..."` 실행 후 job 멈춤 | `-p`(`--print`)로 비대화형 실행 |
| CI 후속 확인 prompt 대기 | `-p` + 필요 도구 사전 승인 |
| PR 리뷰를 파이프라인이 기계 파싱 | `-p` + `--output-format json`<br>+ `--json-schema` → `structured_output` |
| PR 발견 사항을 inline 코멘트로 자동 게시 | json + schema로 필드 강제<br>→ 파싱 → GitHub API |
| 실행 비용 · 소요시간 기록 | `json` 출력 metadata |
| 실행 성공 · 실패 판정 | 종료 코드 확인 (0 = 성공) |
| 도구를 Read · Grep로 제한 + 실패 시 job 실패 | `--tools` + `-p`<br>→ 다음 단계에서 종료 상태 확인 |
| CI에서 `CLAUDE.md` 규약이 전혀 안 먹음 | `--bare` 사용 여부 점검<br>→ 필요 context는 플래그로 전달 |
| headless 적합 작업 | 반복 가능 · 명세 분명 · 무인<br>(PR마다 도는 검사) |
| Claude 작성 코드의 리뷰 효과 낮음 | 별도 session · 새 context subagent로 리뷰 분리 |
| 재리뷰에서 중복 코멘트 | 이전 리뷰 결과 context 포함<br>+ 새 · 미해결 문제만 보고 |
| 관리형 Code Review 재리뷰 중복 | `REVIEW.md`에 과거 지적 고려 방침 기재 |
| CI 테스트 생성의 중복 시나리오 · helper | 기존 테스트 + `conftest.py` 제공<br>+ 저장소 `CLAUDE.md` 규약 |
| PR 리뷰 봇으로 리뷰 병목 완화 | 기계적 검사 한정 · 코멘트만 · merge 금지 |
| 팀별 Claude Code 구성 어긋남 | 공유 기준선 (버전 관리 구성 · skills · commands · 온보딩)<br>+ 팀별 규칙 |
| 여러 저장소에서 일관 활용 | 저장소 커밋 project memory + 공유 skills<br>→ 코드처럼 리뷰 |
| 도입 효과 · 라이선스 가치 측정 | 도입 목적이었던 성과의 변화 |
| 에이전트 생산성 지표 | revert 비율 + 증거 로그 포함 PR 비율 |
| 월 지출 통제 | 작업별 모델 라우팅 + 담당자 있는 월간 수치 검토 |
| 월 비용 급증 | 라우팅 → 컨텍스트 → 캐싱 순 점검 |
| tool 실패 (코드 불변 · 권한 변경 후) | 자격 증명 → 권한 → 스로틀링 → tool 계약 |
| 품질 저하 | 변경된 계층부터<br>프롬프트 → 모델 → retrieval drift 순 |
| 당직 런북 작성 | 순서 있는 증상-용의 대상 점검 + 담당자 · escalation |
| 런북에 없는 새 실패 | 설계자 호출 + 장애 후 런북 항목 추가 |
| 런북이 낡음 | 장애마다 갱신 · 장애 리뷰 = 유지보수 계약 |
| `CLAUDE.md` · MCP 구성 변경 배포 | canary → smoke test → 자동 중단<br>→ 한 명령 rollback + changelog |

<sub>근거: CCAR-F-Amey-Thakur-0006, CCAR-F-Amey-Thakur-0019, CCAR-F-Amey-Thakur-0046, CCAR-F-Amey-Thakur-0056, CCAR-F-MyPractice-0016, CCAR-F-MyPractice-0025, CCAR-F-MyPractice-0026, CCAR-F-Udemy01-0034, CCAR-F-Udemy02-0005, CCAR-F-Udemy02-0025, CCAR-F-Udemy03-0039, CCAR-F-Udemy04-0001, CCAR-F-Udemy04-0051, CCAR-F-Udemy05-0007, CCAR-F-Udemy05-0039, CCAR-F-Udemy06-0033, CCAR-F-Udemy06-0058, CCAR-F-paullarionov-0016, CCAR-F-paullarionov-0025, CCAR-F-paullarionov-0026, CCAR-P-Amey-Thakur-0010, CCAR-P-Amey-Thakur-0033, CCAR-P-Amey-Thakur-0034, CCAR-P-Amey-Thakur-0049, CCAR-P-Amey-Thakur-0065, CCAR-P-Amey-Thakur-0079, CCAR-P-jrajath94-0062, CCAR-P-jrajath94-0064, CCAR-P-jrajath94-0263, CCAR-P-jrajath94-0271, CCAR-P-jrajath94-0275, CCAR-P-jrajath94-0276, CCAR-P-jrajath94-0277, CCAR-P-jrajath94-0279, CCAR-P-jrajath94-0280, CCAR-P-jrajath94-0281, CCAR-P-jrajath94-0330, CCAR-P-jrajath94-0394, CCAR-P-jrajath94-0457, CCAR-P-jrajath94-0583, CCAR-P-jrajath94-0704, CCAR-P-jrajath94-0705</sub>

@@ TRAPS
| 오답 | 이유 |
|---|---|
| `--batch` · `CLAUDE_HEADLESS=true`<br>stdin `/dev/null` 리다이렉트 | 공식 비대화형 방법 = `-p`(`--print`) |
| 대화형 `claude` + "답변 후 종료" 지시 · timeout + 재시도 | 대화형 유지 → 증상만 대응 |
| 대화형 `claude`에 `--output-format json`만 추가 | 시작 모드 문제 → 해결 ✗ |
| 공유 slash command(`.claude/commands/`)를 CI에서 호출 | 실행 모드 불변 |
| plan mode로 CI 자동화 · plan 자동 승인 | plan mode = interactive 작업의 검토 단계<br>계획 승인 = 또 다른 대화 |
| 대화형 실행 + 출력 로그 리디렉션 · transcript grep · 이메일 | 사람 개입 · 문구 변경에 깨짐 |
| `CLAUDE.md` 출력 형식 섹션 · prompt 파싱 템플릿<br>서술형 뒤 JSON 요약 단계 | CLI 수준 강제 ✗ → 구조화 출력 내장 기능 미사용 |
| prompt 지시만으로 schema 준수 JSON 기대 (text 출력) | 검증 구조 없음 |
| `stream-json` 이벤트를 리뷰 결과로 검증 | 이벤트 = 리뷰 결과 자체 ✗ |
| 정규식으로 "N건 생성" 문장 파싱 · prompt로 서식 고정 | 표현 흔들림 잔존 → 집계 깨짐 |
| 종료 코드 무시 (인증 만료 실행을 성공 처리) | 0 아닌 종료 코드 = 실패 → job 실패 처리 필요 |
| `--max-turns` 인상으로 집계 · 종료 문제 해결 | 두 문제와 무관 |
| `--allowedTools`로 도구 제한 | 사전 허용일 뿐 제한 ✗ → `--tools` |
| 도구 제한에 `--json-schema` 사용 | schema = 출력 형식 · 도구 제한 ✗ |
| 요건에 없는 transcript 전체 DB 저장 추가 | 요건 충족과 무관한 부가 작업 |
| 자유 형식 텍스트 패턴 매칭 + 비용 필드 생략 | 타입 필드 · 비용 값 제공 ✗ |
| `--bare` 추가 후 `CLAUDE.md` 규약 유지 기대 | `--bare` = `CLAUDE.md` 자동 탐색 생략 |
| `--output-format json`이 `CLAUDE.md` 규약보다 우선 | 출력 형식은 지시 로드와 무관 |
| 같은 session `--continue` · `--resume`으로 리뷰 | 같은 대화 이어감 → 자기 리뷰 |
| 리뷰 prompt 강화("엄격히") · 자기 점검 지시<br>`--append-system-prompt` 역할 부여 | 수정 시 대화 이력 유지 → 편향 그대로 |
| Claude 작성 PR을 리뷰 workflow에서 제외 | 자기 리뷰만 남아 지적률 하락 |
| 중간 commit 리뷰 생략 · 최근 push 파일만 리뷰 · 후처리 필터 | 이전 결과를 context에 넣어 Claude가 구분하는 방식 ✗ |
| `@claude review always` 전환 · Checks 탭 재실행<br>수작업 close | 리뷰 방침 불변 → 중복 원인 그대로 |
| 전체 테스트 파일(약 2,400건) 매번 prompt에 연결 | 정보량 과다 |
| 커버리지율만 전달 | 시나리오 정보 없음 → 중복 판단 ✗ |
| 생성 후 테스트 이름 일치분 삭제 | 사후 대응 · 생성 단계 개선 ✗ |
| runner 사용자 `~/.claude/CLAUDE.md`에 테스트 규약 | 버전 관리 ✗ |
| 봇이 깨끗하다고 본 PR auto-merge | 승인 결정을 봇에 이양 → 제약 위반 |
| 금요일에만 봇 실행 | 리뷰 몰림 → 지연 증가 |
| 모든 커밋 전체 출력 팀 전체 이메일 | 소음 · 리뷰 프로세스 ✗ |
| 관례 암기 의무화 | 아무것도 구성하지 않음 |
| 관례 정리까지 Claude Code 금지 | 도구가 주는 생산성 포기 |
| 엔지니어별 개인 설정만 유지 | 처음의 어긋남 그대로 |
| 서면 정책 이메일 배포 · 일회성 교육 | 시간이 지나면 희미해짐 |
| 사용마다 승인 요구 | 활용 방식 전달 ✗ · 마찰만 증가 |
| 녹화 워크스루 · 공유 채팅 채널 · 개별 코칭 | 일회성 인수인계 → 정착 ✗ |
| 교육 인원 · 라이선스 활용률 · 호출량 · 온보딩 수 · 사용 시간으로 효과 판단 | 사용량 측정 · 이익 측정 ✗ |
| 생성 코드 줄 수 · 개발자별 토큰 · 실행 시간을 생산성 지표로 | 활동 측정 · 증거 없는 물량 = revert |
| 개발자가 저렴한 모델 고르기를 신뢰 | 수치 · 담당자 없는 신뢰 = 통제 ✗ |
| 리팩터링에서 에이전트 사용 금지 | 도입 목적인 생산성 상실 |
| 모든 작업을 최고 성능 모델로 | 청구액 최대화 |
| 코드 불변 tool 실패에 더 큰 모델로 tool 재작성 | 원인은 코드 바깥 → 수정 효과 ✗ |
| 백오프 없는 재시도 증가 | 스로틀링 의존성 증폭 · 원인 은폐 |
| 타임아웃 10분 연장 | 만료 토큰 → 느리게 실패할 뿐 |
| 비용 절감 목적으로 grounding check 제거 | 품질 하한선 위반 |
| 비용 급증에 전 호출 최소 모델 전환 | 품질 하한선 미확인 · 맹목적 다운그레이드 |
| 비용 급증에 오래된 로그 삭제 | 모델 청구액 앞의 푼돈 사냥 |
| reindex 직후 품질 저하에 모델 재학습 · 최고 tier 업그레이드 | 변경 계층(retrieval) 미점검 · 망가진 인덱스 위 대리 수정 |
| 프롬프트 불변 상황에서 few-shot 추가 | 변경되지 않은 프롬프트 튜닝 = 헛수고 |
| 런북에 "먼저 모델 업그레이드" · 빈 페이지 · 벤더 상태 URL 하나 | 절차 · 담당자 없음 |
| 런북에 없는 새 실패에 가장 가까운 항목 적용 | 일치하지 않는 체크리스트 → 확신에 찬 오도 |
| 새 실패 무시 · 에이전트 매시간 재부팅 | 호출 대상 방치 · 반복만 가림 |
| 런북 동결 · 삭제 · 시니어 기억에 의존 | 낡은 런북 = 확신에 찬 오류<br>기억 = 시니어와 함께 이탈 |
| 구성 배포를 금요일에만 | 영향받는 사람만 변경 · 깨짐 여부 불변 |
| 초기 설정 후 agent 구성 동결 | 퇴화 누적 · 구성은 저장소와 함께 변경 |
| 각 엔지니어 수동 테스트로 구성 검증 | 확장 ✗ · 일관성 ✗ |

<sub>근거: CCAR-F-Amey-Thakur-0006, CCAR-F-Amey-Thakur-0046, CCAR-F-MyPractice-0016, CCAR-F-MyPractice-0025, CCAR-F-MyPractice-0026, CCAR-F-Udemy01-0034, CCAR-F-Udemy02-0005, CCAR-F-Udemy02-0025, CCAR-F-Udemy03-0039, CCAR-F-Udemy04-0001, CCAR-F-Udemy04-0051, CCAR-F-Udemy05-0007, CCAR-F-Udemy05-0039, CCAR-F-Udemy06-0033, CCAR-F-Udemy06-0058, CCAR-F-paullarionov-0016, CCAR-F-paullarionov-0025, CCAR-F-paullarionov-0026, CCAR-P-Amey-Thakur-0010, CCAR-P-Amey-Thakur-0033, CCAR-P-Amey-Thakur-0034, CCAR-P-Amey-Thakur-0049, CCAR-P-Amey-Thakur-0065, CCAR-P-Amey-Thakur-0079, CCAR-P-jrajath94-0062, CCAR-P-jrajath94-0064, CCAR-P-jrajath94-0263, CCAR-P-jrajath94-0271, CCAR-P-jrajath94-0275, CCAR-P-jrajath94-0276, CCAR-P-jrajath94-0277, CCAR-P-jrajath94-0279, CCAR-P-jrajath94-0280, CCAR-P-jrajath94-0281, CCAR-P-jrajath94-0704, CCAR-P-jrajath94-0705</sub>

@@ MEMO
| 이름 | 의미 |
|---|---|
| `--output-format`<br>`text` · `json` · `stream-json` | 평문(기본) · 결과 + metadata · 이벤트 스트림 |
| `--json-schema` | schema 적합 출력<br>→ `json` 결과의 `structured_output` |
| `structured_output` | schema 적합 데이터가 담기는 필드 |
| `total_cost_usd` | `json` 출력의 실행 비용 |
| 종료 코드 | 0 = 성공 · 0 아님 = 실패 |
| `--tools` | 내장 도구 제한<br>(`--allowedTools` = 사전 허용) |
| `--bare` | `CLAUDE.md` 포함 자동 탐색 생략<br>context는 `--append-system-prompt-file` 등으로 전달 |
| `--continue` · `--resume` | 같은 대화 이어감 → 독립 리뷰 ✗ |
| `@claude review once` · `always` | 단발 리뷰 · push마다 리뷰 구독 |
| `REVIEW.md` | 관리형 Code Review 전용 지시 |
| `conftest.py` | 테스트 생성 시 context로 줄 fixture 파일 |
| tool 실패 점검 순서 | 자격 증명 → 권한 → 스로틀링 → 계약 |
| 비용 점검 순서 | 라우팅 → 컨텍스트 → 캐싱 |
| 품질 점검 순서 | 프롬프트 → 모델 → retrieval drift |
| 구성 배포 | canary → smoke test → 자동 중단 → 한 명령 rollback |
| 생산성 지표 | revert 비율 · 증거 로그 포함 PR 비율 |

<sub>근거: CCAR-F-Amey-Thakur-0006, CCAR-F-Udemy01-0034, CCAR-F-Udemy02-0025, CCAR-F-Udemy04-0001, CCAR-F-Udemy04-0051, CCAR-F-Udemy05-0007, CCAR-F-Udemy05-0039, CCAR-F-Udemy06-0058, CCAR-P-jrajath94-0064, CCAR-P-jrajath94-0271, CCAR-P-jrajath94-0275, CCAR-P-jrajath94-0276, CCAR-P-jrajath94-0277, CCAR-P-jrajath94-0704, CCAR-P-jrajath94-0705</sub>

@@ CHECK
- [ ] CI 무인 실행 = `-p` + 도구 사전 허용
- [ ] CI 출력 = `json` + `--json-schema`, 성공 판정 = 종료 코드
- [ ] 도구 제한 = `--tools` (`--allowedTools` ✗)
- [ ] 리뷰 = 수정과 별도 session · 새 context

<sub>근거: CCAR-F-Udemy02-0005, CCAR-F-Udemy04-0051, CCAR-F-Udemy05-0039, CCAR-P-jrajath94-0704</sub>
