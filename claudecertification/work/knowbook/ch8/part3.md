@@ ADD-TO: ### 1-1. tool_use ↔ tool_result 왕복 (client tools)

| 구분 | 내용 |
|---|---|
| 수동 loop 이력 | assistant `tool_use` 턴 유지<br>바로 다음 user 메시지에 `tool_result`<br>(같은 `tool_use_id`) |
| 사이에 다른 메시지 | 확인 메시지 등 삽입 ✗<br>(배열 규칙 위반) |
| 결과를 prefill 요약으로 전송 | `tool_result`로 인식 ✗<br>⚠️ 해설의 "현행 모델에서는 오류" = 모델별로 다를 수 있음 |
| 서버 호출 성공 + Claude가 결과 모름 | 결과가 이력의 올바른 위치 · 형태에 없음<br>→ trace로 로그 저장본과 실제 전송 이력 대조 |

<sub>근거: CCAR-F-Udemy03-0021</sub>

@@ ADD-TO: ### 1-3. Tool 에러 처리

| 구분 | 내용 |
|---|---|
| 일률적 에러 문구 | 모든 실패에 같은 "Operation failed"<br>→ 재시도 가능 여부 판단 불가 |
| `is_error: true`만 부착 | 판단 재료 부족<br>→ 불필요 재시도 · 비일관 escalate |
| 올바른 응답 | 실패 분류 · 재시도 가능 여부<br>메시지 · 시정 힌트를 구조화해 반환 |
| 에러 코드 · 스택 트레이스만 | 다음 수 결정 불가<br>→ 구체적 · 실행 가능한 개선점 필요 |
| 두 독자 | agent용 = 분류 · 재시도 가능 여부<br>사람용 = 고객이 이해할 설명 |
| 비즈니스 규칙 위반 | 재시도 불가 플래그 + 이해하기 쉬운 설명 |
| 입력 오류 | 시정 힌트 = 유효 형식 · 후보 ID<br>ID 조회 tool 안내 |
| 처리 불가 인자 | 정보 담긴 에러 반환<br>가장 비슷한 결과 추측 · 빈 결과 ✗ (조용히 틀린 결과) |
| 필드 이름 | `errorCategory` · `isRetryable`<br>= tool 측이 설계하는 metadata의 예<br>MCP 사양이 정한 값 ✗ |
| 설계 점검 질문 | "이 응답만 읽고 다음 인자를 정할 수 있는가" |

| 증상 | 원인 | 조치 |
|---|---|---|
| 같은 호출 4~5회 반복<br>+ "시스템 장애" 오안내 | 한도 초과 · 규칙 위반 · 입력 오류를 일시 장애와 구별 ✗ | 분류 · 재시도 불가 · 사유 설명 반환 |
| 접근 거부 후 검색어만 바꿔 반복<br>보고서에 "일부 취득 불가"만 기재 | 분류 · 재시도 가능 여부 · 사유 부재 | 시도 중단 + 취득 못 한 이유 정확히 보고 |
| 정책 차단을 성공처럼 반환<br>→ 표현만 바꿔 같은 요청 반복 | 실패 신호 부재 | `isError: true` + 재시도 가능 여부 구조화 |
| "검증 실패" 텍스트를 일반 결과로 반환 | 같은 호출 반복 · 하위 시스템이 성공으로 처리 | `isError: true` + 종류 · 수정 힌트 |

| 에러 종류 | 예 | 대응 |
|---|---|---|
| 일시적 | timeout · 429 · 서비스 불가 | 대기 후 재시도 |
| 검증 | 존재 않는 ID · 형식 불량 · 불가능한 날짜 | 입력 수정 후 재호출 |
| 비즈니스 | 한도 초과 · 마감 규칙 · 정책 차단 | 재시도 ✗<br>사유 안내 · escalate |
| 권한 | 접근 거부 · 계약 외 데이터 · 라이선스 만료 | 재시도 ✗<br>다른 정보원 탐색 · 부족으로 보고 |

| 구분 | 내용 |
|---|---|
| 한도 초과 → 일시적으로 분류 | 시간 지나도 안 풀림 → 잘못된 정보 · 재시도 조장 |
| 모든 실패에 같은 재시도 | 검증 오류엔 낭비<br>횟수 · 간격 · 캐시 조정만으로 해결 ✗ |
| 일률적 지수 백오프 | 종류 구분 없는 재시도 고착 |
| 재시도 위치 | 일시적 실패 = tool · subagent 내부 재시도<br>(횟수 상한) |
| 상위 전파 대상 | 로컬에서 못 푼 에러만<br>부분 결과 + 시도한 내용 + 마지막 에러와 함께 |
| 일시 에러를 coordinator에 전달 | 위임 반복 · context · 토큰 낭비 |
| tool 수준 처리 근거 | tool = 에러 유형을 확정적으로 앎<br>agent의 플래그 해석 · prompt 준수에 의존 ✗ |
| 영구 에러(구문 오류 등) | 재시도 ✗ → 에러로 반환 |
| 오답 | 전용 retry subagent = 처리 위치만 이동<br>전체 중단 = 일시 실패에 과잉 반응 |
| 받는 쪽 방침 | 재시도 가능 여부에 따라 재시도 · 전환 · escalate 지시<br>slash command에도 에러 종류별 동작 명시 |
| 필요 조합 | 에러 정보량(tool) + 행동 방침(호출 측) 둘 다 |

| 상황 | 반환 | 의미 |
|---|---|---|
| 검색 성공 · 일치 0건 | 성공 + 빈 결과 | "없음" 확인 완료 |
| timeout · 접근 실패 | `is_error: true` 에러 | "확인 못 함" · 재시도 대상 |
| 둘 다 빈 배열 | ✗ | 실패가 "확인된 부재"로 보고됨 |
| 둘 다 에러 | ✗ | 유효한 빈 결과 소실 |
| 실패 시 캐시 반환 | ✗ | 낡은 정보가 새 결과처럼 보임 |
| 실패 시 관련성 지어내기 | ✗ | 적용 안 되는 정책 인용 |
| 빈 결과에 검색 조건 첨부 | 제품명 · 대상 DB | 어디서 못 찾았는지 보고 가능 |
| 하위 시스템 전달 | 조회 결과를 레코드의 독립 상태 항목으로 보존 | 구분 유지 |
| `stop_reason` | tool 성공 여부 표시 ✗ | 구분 수단 아님 |

| 경로 | 대상 | 모델 전달 |
|---|---|---|
| JSON-RPC 프로토콜 에러 | 알 수 없는 tool · 잘못된 형식 요청<br>서버 에러 | 요청 구조 문제<br>모델이 고치기 어려움 |
| tool 실행 에러<br>(`isError: true`) | API 실패 · 입력 검증 · 비즈니스 로직 | 실행 가능한 피드백 포함<br>client가 모델에 전달 → 자가 수정 |
| 오용 | 형식 불량 번호 · 취소된 예약을 JSON-RPC 에러로 | 이유 전달 보장 ✗<br>→ "시스템 장애"로 답하고 종료 |

| 구분 | 내용 |
|---|---|
| 필수 절차 (검증 성공 전 제출 ✗) | 앱이 실행 전 게이트로 판정<br>Claude = `tool_use` 요청만 · 실행 = 앱 |
| 게이트 거부 응답 | `is_error: true` + 이유 + 다음 절차<br>→ 검증 · 검토 ticket으로 복귀 |
| 오답 | 문구로 loop 중단 · `tool_choice` 일시 강제<br>→ 제출 자체 저지 ✗ |

<sub>근거: CCAR-F-Amey-Thakur-0037, CCAR-F-Amey-Thakur-0076, CCAR-F-MyPractice-0062, CCAR-F-Udemy01-0013, CCAR-F-Udemy01-0027, CCAR-F-Udemy01-0031, CCAR-F-Udemy02-0002, CCAR-F-Udemy02-0054, CCAR-F-Udemy03-0015, CCAR-F-Udemy03-0054, CCAR-F-Udemy03-0055, CCAR-F-Udemy04-0027, CCAR-F-Udemy04-0030, CCAR-F-Udemy04-0036, CCAR-F-Udemy05-0004, CCAR-F-Udemy05-0028, CCAR-F-Udemy05-0033, CCAR-F-Udemy06-0009, CCAR-F-Udemy06-0024, CCAR-F-preporato-0003</sub>

@@ ADD-TO: ### 1-6. Tool description과 tool surface 설계

| 증상 | 의미 |
|---|---|
| 특정 키워드가 있을 때만 특정 tool 선호<br>(예: 78% 대 93%) | system prompt에 키워드 기반 routing 지시 존재 신호<br>description이 명확해도 prompt 지시가 동작을 이끎 |
| 불필요한 tool 호출 | 원인 후보 3가지<br>description · `tool_choice` · system prompt 지시 |
| description이 용도 명시 + `tool_choice: auto` | 남는 원인 = system prompt의 지시 |
| "find · search라 하면 반드시 검색 tool" | 광범위 키워드 지시 → 호출 과다(overtrigger) |
| 조치 | 실제 조사가 필요할 때만으로 규칙 축소<br>⚠️ "최근 모델은 system prompt를 잘 따름"<br>= 모델 세대에 따라 달라질 수 있음 |
| 오답 | description 보강 · tool 이름 변경 = 원인 밖<br>`tool_choice: any` = 호출 강제 → 악화 |

<sub>근거: CCAR-F-Udemy01-0052, CCAR-F-paullarionov-0056</sub>

@@ ADD-TO: ### 1-9. Client tools vs Server tools

| 구분 | 내용 |
|---|---|
| Message Batches API | Messages API와 같은 파라미터 · tool 사용 포함 가능<br>비동기 일괄 처리 |
| batch 안에서 Anthropic이 실행 | server tool(예: 웹 검색)뿐 |
| client tool 호출 | 결과에 `tool_use` 포함<br>→ 결과를 받은 쪽(앱)이 실행 |
| 처리 순서 | `custom_id`로 어느 요청인지 특정<br>→ tool 실행 → `tool_result` 포함 후속 요청 |
| 오답 | server tool(`web_search`)로 대체 = 검증 대상 달라짐<br>`tool_choice` 강제 = 실행 주체 불변<br>예측한 `tool_result` = 실행 결과 아님 |

<sub>근거: CCAR-F-Udemy01-0012</sub>

@@ ADD-TO: ### 1-13. MCP transport: stdio vs Streamable HTTP

| 구분 | 내용 |
|---|---|
| host-client-server | host가 서버마다 MCP client 하나 생성<br>각 client = 대응 서버와 전용 연결 유지 |
| 다중 서버 | 한 host가 여러 서버에 동시 연결 = 표준 형태 |
| tool 목록 통합 | 서버마다 `tools/list`<br>→ host가 모아 제시 · 호출은 소유 서버로 분배 |
| subagent 할당 | 필요한 서버 동시 연결 + 역할별 서버만 할당<br>연결 유지 |
| 오답 | subagent당 서버 1개만 활성 + 필요 시 재연결 = 단계마다 중단<br>자체 서버로 집약 = 불필요한 개발 부담 |

<sub>근거: CCAR-F-Udemy01-0044</sub>

@@ NEW-SECTION
### 내장 도구 선택 (Read · Write · Edit · Bash · Grep · Glob)
**이름은 Glob · 내용은 Grep · 일부는 Edit · 전체는 Write**

| 도구 | 대상 | 쓰는 경우 |
|---|---|---|
| `Glob` | 파일 경로(이름 · 확장자 패턴) | 명명 규칙으로 파일 열거(`**/*.test.tsx`) |
| `Grep` | 파일 내용 패턴 | 함수명 · 에러 메시지 · import 검색<br>호출처 · 출력 위치 특정 |
| `Read` | 개별 파일 읽기 | Grep으로 찾은 파일 확인 · import 추적 |
| `Edit` | 정확히 한 곳과 일치하는 텍스트 | 범위를 좁힌 변경 |
| `Write` | 파일 전체 | 전체 재생성 · 파일 전체 작업 |
| `Bash` | 셸 명령 | macOS · Linux = Bash `find` · `grep`으로<br>검색 대체하는 구성 존재 |

| 상황 | 선택 |
|---|---|
| 에러 메시지가 출력되는 위치 | `Grep` |
| 함수의 모든 호출처 | `Grep` |
| 함수명 단서가 있는 정의 · 진입점 | `Grep` |
| `contract.template.spec.ts` 같은 이름 규칙 파일 열거 | `Glob` |
| 오답: 흔한 단어("template")를 Grep | 무관한 일치 대량 · 누락 |
| 오답: Glob · `find`로 내용 정보 추정 | 이름만으론 불확실 · 누락 |

| 구분 | 내용 |
|---|---|
| 판별 기준 | 찾는 정보가 파일 이름에 있나 · 내용에 있나 |
| subagent `tools`에 Glob · Grep 지정 + Bash 제외 | 그 subagent에서 Glob · Grep 사용 가능 |
| macOS · Linux 기본 | Glob · Grep 대신 Bash `find` · `grep` 사용<br>⚠️ 기본 도구 세트는 플랫폼 · 버전에 따라 변동<br>(현재 공식 문서와 일치 확인) |

대규모 코드베이스 탐색 순서

1. 경로로 좁히기: `Glob`으로 후보 디렉터리
2. 내용으로 찾기: `Grep`으로 식별자 · 진입점
3. 필요한 것만 읽기: 일치한 파일을 `Read` → import 따라 흐름 추적

| 구분 | 내용 |
|---|---|
| 전체 파일을 처음부터 통독(수백 파일) | context 소진 · 노이즈 · 느림 |
| 처리 흐름의 연결 고리 | 파일 이름 ✗ · 함수 호출 관계와 import |
| 파일명으로만 좁히기 · `cat` 일괄 읽기 · 분할 통독 | 읽는 양 안 줄어듦 · 관계 파악 어려움 |
| 설계 문서로 추정 | 구현 확인 ✗ |
| 탐색 결과 기록 | 진입 파일 · 경유 모듈 · 출력 위치를<br>메모 · scratchpad 파일에 저장<br>→ 같은 조사 반복 ✗ |

별칭 re-export 사용처 전수 추적

1. wrapper 모듈을 `Read` → export된 이름(별칭 포함) 파악
2. 각 이름으로 코드베이스 전체 `Grep`
3. 발견한 별칭이 다시 re-export되는지 같은 절차로 확인

| 구분 | 내용 |
|---|---|
| 별칭 신호 | 원래 이름 검색 결과가 실제보다 적음 |
| 대소문자 무시 검색 | 표기 흔들림에만 효과 · 별칭 ✗ |
| Glob · 파일 통독 | 검색 대체 ✗ |
| 테스트 실행으로 추적 | 실행된 경로만 보임 → 망라성 부족 |
| 위치 목록 파일 저장 | 교체 후 목록과 대조 → 누락 확인 |
| 변경 전 | Grep 위치를 Read로 열어 전후 문맥 확인<br>→ 같은 이름의 다른 함수 · 문자열 오변경 방지 |

| 구분 | 내용 |
|---|---|
| `Edit` 동작 | 완전 일치 문자열 치환<br>정규식 · 모호한 일치 ✗ |
| `old_string` 조건 | 파일 안에 정확히 한 번 |
| 여러 번 일치할 때 | ① 앞뒤 문맥을 포함해 한 곳으로 유일화<br>② `replace_all: true`로 모두 치환 |
| 둘 다 불가 | `Read`로 현재 내용 → 완성본 조립 → `Write` |

| 상황 | 정답 |
|---|---|
| 모든 일치를 똑같이 변경 + 비슷한 문자열은 유지 | `replace_all` + `old_string`에 닫는 따옴표까지 포함<br>(`class="salary"` ✓ · `salary-note` 제외) |
| 한쪽만 변경 + 반복 문구라 유일화 불가 + 완성본 조립 가능 | `Read` → `Write`로 전체 덮어쓰기 |
| 자동 생성 파일 전체 재생성 | `Write` 한 번 |
| 같은 문자열 수십 곳을 `Edit` 수십 회 | 일부 실패 → 중간까지 갱신된 파일 잔존 ✗ |
| 오답 | `replace_all`(한쪽만 변경) = 범위 과다<br>`old_string` 단축 · 정규식<br>Grep으로 줄 지정 = 일치 방식 불변 |
| `Read` + `Write` | 단순 일괄 치환엔 과함 |
| 사후 확인 | 치환 후 Grep으로 건수 확인<br>Write 후 JSON 파싱 가능 여부 검증 |

<sub>근거: CCAR-F-Udemy01-0050, CCAR-F-Udemy02-0039, CCAR-F-Udemy03-0059, CCAR-F-Udemy04-0012, CCAR-F-Udemy04-0052, CCAR-F-Udemy04-0057, CCAR-F-Udemy05-0009, CCAR-F-Udemy05-0011, CCAR-F-Udemy05-0018, CCAR-F-Udemy06-0008, CCAR-F-Udemy06-0032, CCAR-F-Udemy06-0046</sub>

@@ NEW-SECTION
### 도구 경계에서 강제하는 통제 (정책 한도 · 파괴적 작업 · 서드파티 MCP)
**예외 없는 통제는 prompt가 아니라 도구 경계에서 강제**

| 상황 | 강제 위치 |
|---|---|
| 정책 한도(예: 직접 환불 상한)<br>초과 시 사람이 처리 | 도구 계층에서 결정적으로 검사 |
| 되돌릴 수 없는 작업 · 삭제 | 모델을 둘러싼 시스템이 권한 · 범위 · 확인 통제 |
| 실행 중 편집 · 셸 금지 skill | skill 프런트매터 `disallowed-tools`로 도구 풀에서 제외 |
| 필수 절차 위반 방지 | 앱이 실행 전 코드로 판정하는 게이트 |

| 수단 | 효과 |
|---|---|
| prompt 문구 · 경고 · description | 요청일 뿐 · 확률적 · 보장 ✗ |
| 모델의 판단 | 확률적 → 예외 없는 요구와 불일치 |
| 직원 교육 | agent 제약 ✗ |
| parameter 추가 · 선언 순서 변경 | 권한 제약 ✗ |
| CLAUDE.md 지시 · slash command 안의 요청 | 모델 guidance · 강제력 ✗ |

| 항목 | `allowed-tools` | `disallowed-tools` |
|---|---|---|
| 의미 | 호출 turn 동안 확인 없이 사용<br>(사전 승인) | skill 활성 동안 도구 풀에서 제외 |
| 도구 제한 효과 | ✗ (사용 가능 도구를 제한하지 않음) | ✓ |
| 전체 적용 | — | `permissions`의 `deny` |

| 구분 | 내용 |
|---|---|
| tool description · schema | 모델 입력 = 주입 경로<br>악의적 · 침해된 서버가 지시 주입 가능 |
| 원격 설정 파일에서 description 로드 | 조용한 업데이트로 변조 가능 → 버전 고정 |
| 완화책 | 버전 고정 · schema를 신뢰 불가로 취급<br>샌드박스 · 확인 게이트로 가로챈 호출의 영향 제한 |
| 결함의 위치 | 프로토콜 ✗ · 신뢰할 수 없는 콘텐츠 |
| 자금 이동 tool(closed-source 벤더 server) | 최소 권한 자격 증명 + 사람의 승인 |
| 승인 강제 위치 | 효과를 수행하는 계층 |
| 결제 결정 | 제3자 설명(description)에 의존 ✗ |

<sub>근거: CCAR-F-Amey-Thakur-0002, CCAR-F-Amey-Thakur-0029, CCAR-F-Amey-Thakur-0062, CCAR-F-Udemy03-0058, CCAR-P-jrajath94-0008, CCAR-P-jrajath94-0079</sub>

@@ RULES

| 상황 | 정답 |
|---|---|
| tool이 모든 실패에 같은 문구 반환 + agent가 재시도 · 오안내 | `is_error: true` + 분류 · 재시도 가능 여부 · 사람용 설명 |
| 실패 종류가 섞임<br>(timeout · 입력 오류 · 한도 초과 · 접근 거부) | 일시적만 재시도 · 나머지는 재시도 ✗ + 사유 보고 · escalate |
| 같은 빈 배열이 timeout과 0건에 모두 쓰임 | 0건 = 성공 빈 결과 · timeout = 에러 |
| subagent가 429 · timeout을<br>coordinator에 계속 전파 | subagent 내부 로컬 재시도(상한)<br>못 푼 것만 부분 결과 · 시도 내용과 함께 전파 |
| 영구 에러와 일시 에러가 한 tool에 섞임 | tool 수준에서 결정적 retry 처리 |
| MCP tool의 업무 실패(형식 불량 번호 · 취소된 예약) | `isError: true` tool 실행 에러<br>JSON-RPC 에러 = 요청 구조 문제용 |
| 정책 차단을 성공처럼 반환 + agent가 표현만 바꿔 재시도 | `isError: true` + 재시도 가능 여부 |
| 처리할 수 없는 인자를 받음 | 정보 담긴 에러 반환 |
| 필수 절차를 건너뛴 호출 | 앱 게이트가 거부 → `is_error: true` + 이유 + 다음 절차 |
| 함수 호출처 · 에러 메시지 위치 찾기 | `Grep` |
| 명명 규칙 파일 열거 | `Glob` |
| 대규모 repo에서 처리 흐름 파악 | `Grep`으로 진입점 → `Read`로 import 추적 |
| 별칭 re-export로 사용처 누락 | wrapper `Read` → 노출 이름마다 `Grep` |
| `Edit` 다중 일치 + 모두 동일 변경 | `replace_all`<br>(`old_string`은 닫는 따옴표까지 포함) |
| `Edit` 다중 일치 + 한쪽만 변경 + 유일화 불가 | `Read` → `Write` 전체 |
| 자동 생성 파일 재생성 | `Write` |
| 불필요한 tool 호출<br>+ description · `tool_choice` 정상 | system prompt의 광범위 키워드 지시 축소 |
| 정책 한도 · 파괴적 작업 · 도구 사용 금지 | 도구 경계 · 도구 풀 제외로 강제 (prompt ✗) |
| 서드파티 MCP 서버 연동 | 버전 고정 + description 신뢰 불가 취급<br>+ 샌드박스 · 확인 게이트 |
| 서드파티 server의 결제 tool | 최소 권한 자격 증명 + 사람의 승인(효과 계층) |
| Batches API + client tool | `custom_id`로 특정 → 앱이 실행<br>→ `tool_result` 후속 요청 |
| 여러 MCP 서버 + 여러 subagent | 동시 연결 · 통합 registry · 역할별 서버 할당 |
| 수동 loop에서 Claude가 tool 결과를 모름 | assistant `tool_use` 턴 유지<br>+ 결과를 `tool_result`에 저장 |

<sub>근거: CCAR-F-Amey-Thakur-0002, CCAR-F-Amey-Thakur-0029, CCAR-F-Amey-Thakur-0037, CCAR-F-Amey-Thakur-0062, CCAR-F-Amey-Thakur-0076, CCAR-F-MyPractice-0062, CCAR-F-Udemy01-0012, CCAR-F-Udemy01-0013, CCAR-F-Udemy01-0027, CCAR-F-Udemy01-0044, CCAR-F-Udemy01-0050, CCAR-F-Udemy01-0052, CCAR-F-Udemy02-0002, CCAR-F-Udemy02-0039, CCAR-F-Udemy02-0054, CCAR-F-Udemy03-0021, CCAR-F-Udemy03-0054, CCAR-F-Udemy03-0055, CCAR-F-Udemy03-0058, CCAR-F-Udemy03-0059, CCAR-F-Udemy04-0012, CCAR-F-Udemy04-0030, CCAR-F-Udemy04-0036, CCAR-F-Udemy04-0052, CCAR-F-Udemy04-0057, CCAR-F-Udemy05-0009, CCAR-F-Udemy05-0011, CCAR-F-Udemy05-0018, CCAR-F-Udemy05-0033, CCAR-F-Udemy06-0008, CCAR-F-Udemy06-0032, CCAR-F-Udemy06-0046, CCAR-F-paullarionov-0056, CCAR-F-preporato-0003, CCAR-P-jrajath94-0008, CCAR-P-jrajath94-0079</sub>

@@ TRAPS

| 오답 | 이유 |
|---|---|
| 고정 문구 "Operation failed"<br>+ `is_error: true`만 | 원인 구별 ✗ · 재시도 오판 |
| 실패를 빈 배열 · 빈 JSON · 성공 결과로 변환 | "해당 없음"과 "실패" 혼동 |
| timeout과 0건을 둘 다 에러로 반환 | 유효한 빈 결과 소실 |
| 실패 시 캐시 반환 | 낡은 정보가 새 결과처럼 보임 |
| 한도 초과를 일시적 오류로 분류 | 재시도 조장 · 시간이 지나도 해소 안 됨 |
| 오류 구분 없이 횟수 · 간격 · 백오프 조정 | 어느 한 유형엔 부적절 |
| description에 경고 추가 · 설명 확장 | 실행 시 응답을 못 바꿈 · 예방에 그침 |
| 전용 retry subagent | 처리 위치만 이동 · 왕복 안 줄어듦 |
| 업무 실패를 JSON-RPC 에러로 | 이유 전달 보장 ✗ → "시스템 장애"로 종료 |
| 가장 비슷한 결과를 짐작해 반환 | 조용히 틀린 결과 |
| 문구로 loop 중단<br>`tool_choice` 일시 강제로 필수 절차 보장 | 제출 자체를 저지하는 구조 ✗ |
| 흔한 단어를 Grep · 파일 통독 | 무관한 일치 대량 · context 소진 |
| Glob · `find`로 내용 정보 추정 | 이름만으론 불확실 |
| 대소문자 무시 검색으로 별칭 사용처 추적 | 별칭엔 효과 ✗ |
| 테스트 실행으로 사용처 추적 | 실행된 경로만 보임 |
| `Edit`에서 `old_string` 단축 · 정규식 · Grep으로 줄 지정 | `Edit` 일치 방식 불변 |
| 한쪽만 바꿀 때 `replace_all` | 변경 범위 과다 |
| 단순 일괄 치환에 `Read` + `Write` | 과함 |
| 자동 생성 파일을 `Edit` 수십 회로 갱신 | 유일 일치 실패 → 중간 갱신 파일 잔존 |
| 불필요한 tool 호출을 `tool_choice: any`로 교정 | 호출 강제 → 악화 |
| 도구 제한에 `allowed-tools` | 사전 승인일 뿐 · 제한 ✗ |
| 도구 제한을 CLAUDE.md · slash command 요청으로 | guidance뿐 · 강제력 ✗ |
| 정책 한도를 prompt · 직원 교육 · parameter 추가로 | 결정적 강제 ✗ |
| 서드파티 주입 위험에 더 큰 모델 · 전체 재작성 · 유출 후 키 삭제 | 주입 경로 미해결 · MCP 가치 소실 · 증상만 처리 |
| SOC 2 보고서 · prompt 지시로 결제 안전 확보 | 벤더 통제 설명일 뿐 · 우회 가능 |
| Batches API에서 `web_search` 대체<br>`tool_choice` 강제 · 예측 `tool_result` | 검증 대상 변경 · 실행 주체 불변 · 실행 결과 아님 |
| subagent당 서버 1개 + 필요 시 재연결 | 단계마다 중단 |
| tool 결과를 prefill 요약으로 · 사이에 확인 메시지 삽입 | `tool_result` 인식 ✗ · 배열 규칙 위반 |

<sub>근거: CCAR-F-Amey-Thakur-0002, CCAR-F-Amey-Thakur-0029, CCAR-F-Amey-Thakur-0062, CCAR-F-Amey-Thakur-0076, CCAR-F-MyPractice-0062, CCAR-F-Udemy01-0012, CCAR-F-Udemy01-0013, CCAR-F-Udemy01-0027, CCAR-F-Udemy01-0031, CCAR-F-Udemy01-0044, CCAR-F-Udemy01-0050, CCAR-F-Udemy01-0052, CCAR-F-Udemy02-0002, CCAR-F-Udemy02-0039, CCAR-F-Udemy02-0054, CCAR-F-Udemy03-0015, CCAR-F-Udemy03-0021, CCAR-F-Udemy03-0054, CCAR-F-Udemy03-0055, CCAR-F-Udemy03-0058, CCAR-F-Udemy03-0059, CCAR-F-Udemy04-0012, CCAR-F-Udemy04-0030, CCAR-F-Udemy04-0036, CCAR-F-Udemy04-0052, CCAR-F-Udemy04-0057, CCAR-F-Udemy05-0009, CCAR-F-Udemy05-0011, CCAR-F-Udemy05-0018, CCAR-F-Udemy05-0033, CCAR-F-Udemy06-0024, CCAR-F-Udemy06-0032, CCAR-F-Udemy06-0046, CCAR-F-preporato-0003, CCAR-P-jrajath94-0008, CCAR-P-jrajath94-0079</sub>

@@ MEMO

| 이름 | 의미 |
|---|---|
| JSON-RPC 에러 | MCP 프로토콜 에러<br>(알 수 없는 tool · 잘못된 형식 요청 · 서버 에러) |
| `errorCategory` · `isRetryable` | tool 측이 설계하는 에러 metadata의 예<br>(MCP 사양이 정한 값 ✗) |
| `Glob` | 파일 이름 · 확장자 패턴으로 파일 검색 |
| `Grep` | 파일 내용에서 패턴 검색 |
| `Read` | 개별 파일 읽기 |
| `Edit` | 완전 일치 문자열 치환<br>(`old_string`은 파일 안에 한 번) |
| `replace_all` | `Edit`의 모든 일치 치환 옵션 |
| `Write` | 파일 전체 쓰기 |
| `allowed-tools` | skill 호출 turn 동안의 사전 승인<br>(도구 제한 ✗) |
| `disallowed-tools` | skill 활성 동안 도구 풀에서 제외 |
| `custom_id` | Batch 요청 식별자<br>(결과가 어느 요청의 것인지 특정) |

<sub>근거: CCAR-F-Udemy01-0012, CCAR-F-Udemy01-0013, CCAR-F-Udemy03-0058, CCAR-F-Udemy03-0059, CCAR-F-Udemy04-0052, CCAR-F-Udemy05-0004, CCAR-F-Udemy05-0009, CCAR-F-Udemy06-0024, CCAR-F-Udemy06-0046</sub>

@@ CHECK

- [ ] 에러 = 분류 · 재시도 가능 여부 · 설명, 빈 결과와 구분
- [ ] 이름 = Glob · 내용 = Grep
- [ ] `Edit` 다중 일치 = 유일화 · `replace_all` · `Write`
- [ ] 예외 없는 통제 = 도구 경계 강제 (prompt ✗)

<sub>근거: CCAR-F-Amey-Thakur-0002, CCAR-F-Udemy04-0036, CCAR-F-Udemy04-0057, CCAR-F-Udemy05-0004, CCAR-F-Udemy05-0009, CCAR-F-Udemy05-0011</sub>
