@@ ADD-TO: ### 1-1. tool_use ↔ tool_result 왕복 (client tools)

| 구분 | 내용 |
|---|---|
| 실행 구조 | 앱이 tool 정의 → Claude가 `tool_use` 요청<br>→ 앱이 실행 → `tool_result` 반환 loop |
| 실행 경계 | Claude = 어떤 tool · 어떤 인자 결정<br>앱 = 실행 |
| 권한 검사 뒤 실행해야 할 때 | 앱 코드가 각 tool 실행<br>출력 → `tool_result` 블록으로 반환 |
| loop 제어 | `stop_reason: tool_use`인 동안 요청 반복<br>`end_turn` 등 다른 stop reason에서 종료 |
| 문서마다 다음 행동이 다를 때 | description · schema가 명확한 tool 정의<br>위 loop를 앱이 실행 |

<sub>근거: CCAR-F-Udemy01-0056, CCAR-P-jrajath94-0589</sub>

@@ ADD-TO: ### 1-2. Parallel tool use

| 구분 | 내용 |
|---|---|
| 위치 | `tool_result` user 메시지<br>= `tool_use` 포함 assistant 메시지의 바로 다음<br>사이에 다른 메시지 삽입 ✗ |
| content 순서 | `tool_result` 블록 = 배열 맨 앞<br>덧붙이는 텍스트 = 그 뒤 |
| 요약 텍스트만 전송 | 결과 ↔ 호출 대응 · 실행 여부 파악 ✗<br>assistant 턴 유지 + `tool_use_id` 짝 필요 |
| 점검 3가지 | 역할(user) · 순서(앞) · 메시지 수(하나) |

<sub>근거: CCAR-F-Udemy01-0006</sub>

@@ ADD-TO: ### 1-4. tool_choice

| 요구 | 설정 | 이유 |
|---|---|---|
| 텍스트만 응답 제거<br>출구 tool 여럿 | `any` | 어느 tool이든 호출<br>선택은 모델 |
| 문서 유형 미정<br>추출 schema 여럿 | `any` | `tool` = 한 schema로 고정<br>`auto` = 대화 응답 여지 |
| 출력용 tool 여럿<br>(표 · 텍스트 등) | `any` | 텍스트만으로 끝나는 응답 차단 |
| 출구가 하나<br>특정 tool 필수 | `tool` + `name` | 지정 tool 호출 보장 |
| workflow 첫 단계만 고정 | 첫 요청 `tool`<br>→ 이후 `auto` | 강제 = 요청 단위 설정<br>후속 단계 = 이후 turn |
| 직접 답하기도 하는 coordinator | `auto` | `any` = 매번 호출 강제 |
| 문서마다 다음 행동이 다름 | `auto` | 호출 여부도 Claude 판단 |

| 증상 | 원인 | 조치 |
|---|---|---|
| 모든 요청에 `tool` 고정<br>→ 같은 tool만 반복 | 강제가 후속 tool 호출 차단 | 첫 요청만 `tool`<br>이후 `auto` |
| 텍스트만 응답이 간헐 발생 | `auto`에서 tool 미호출 가능 | `any` + 출구 tool 정의 |
| 텍스트 응답 대부분 = "해당 없음" 결과 | 기록할 출구 tool 부재 | 빈 결과 보고 tool 추가<br>+ `any` |
| `any`만 적용 | "해당 없음"을 기존 tool에 억지 기록<br>→ 추측 기록 | 빈 결과 보고 tool 추가 |

| 문제 | 처방 |
|---|---|
| 잘못된 tool 선택 | description · 이름 · system prompt 수정<br>강제 = 선택 문제를 우회 · 입력별 선택 포기 |
| 올바른 tool + 잘못된 입력 | 입력 형식 · 필수 파라미터 · schema 수정<br>`tool_choice` 강제 ✗ |

| 구분 | 내용 |
|---|---|
| 미지원 설정 | 수동 extended thinking 활성<br>→ `any` · `tool` 오류 · `auto`/`none`만 사용<br>⚠️ 모델 · 설정별 지원 범위가 시점에 따라 변동 |
| 순서 담보 대안 | 첫 요청에서 제공하는 tool 목록을 좁힘<br>`auto` + strict + prompt 유도 |

<sub>근거: CCAR-F-Udemy01-0056, CCAR-F-Udemy02-0016, CCAR-F-Udemy02-0057, CCAR-F-Udemy03-0027, CCAR-F-Udemy03-0032, CCAR-F-Udemy03-0042, CCAR-F-Udemy03-0056, CCAR-F-Udemy04-0018, CCAR-F-Udemy04-0044, CCAR-F-Udemy05-0002, CCAR-F-Udemy06-0007, CCAR-F-Udemy06-0039, CCAR-F-Udemy06-0048</sub>

@@ ADD-TO: ### 1-5. Strict tool use (입력 스키마 보장)

| 수단 | 보장 수준 |
|---|---|
| prompt로 형식 요청 | 확률적<br>말미 주석 · 필드 누락 · 타입 오류 재발 |
| 사후 검증 · 재시도 | 잘못된 출력의 발생 자체 방지 ✗ |
| API 기능으로 생성 시 제약 | 가장 확실<br>`strict: true` = tool 입력<br>Structured outputs = 응답 본문 |

| 목적 | 방법 |
|---|---|
| 대시보드가 tool 호출을 받는 설계 | `input_schema` client tool + `strict: true`<br>응답을 `tool_use`로 수신 |
| 인계 데이터 일관 | 전용 tool(예: `escalate_to_human`)<br>`input_schema`의 `required` 필드로 지정 |
| 인계 tool 사용 유도 | 인계로 끝나는 대응 → 그 tool 호출 지시<br>schema + 호출 지시 = 둘 다 필요 |
| 모호한 입력이 그대로 전달 | 식별자 유형을 필수 파라미터로 선언<br>→ 입구에서 차단 |
| backend 변경 불가 | tool 정의(description · schema)는 앱에서 수정 가능 |
| 형식이 엄격한 파라미터 | `input_examples` = schema에 맞는 입력 예시 |
| "해당 없음" 보고 tool | 검색 범위 · 이유를 필수 필드로<br>→ coordinator가 추가 조사 판단 |
| 작업 범위 제한(최소 권한) | schema 상한(예: 100행)으로 tool 범위 한정<br>로깅 = 관찰 · 통제 ✗ |
| 상한 강제의 한계 | strict는 `maximum` 등 수치 제약 미지원<br>⚠️ 해설의 "schema 상한이 통제"는 앱 검증 병행 전제 |
| prefill(응답 선두 `{` 채우기) | 신규 모델에서 사용 불가<br>⚠️ 모델 세대에 따라 변동 · 시점 의존 |

<sub>근거: CCAR-F-Udemy01-0016, CCAR-F-Udemy01-0054, CCAR-F-Udemy03-0027, CCAR-F-Udemy03-0032, CCAR-F-Udemy04-0044, CCAR-F-Udemy05-0046, CCAR-P-jrajath94-0477</sub>

@@ ADD-TO: ### 1-6. Tool description과 tool surface 설계

| 구분 | 내용 |
|---|---|
| 오선택 진단 | 첫 확인 = description이 용도 · 경계를 구분하는지<br>증상 구분 = 잘못된 tool 선택 vs 올바른 tool의 잘못된 입력 |
| 입력 | 허용 입력 형식 · 예시 질의 · edge case |
| 경계 | 유사 tool 대비 언제 쓰고 언제 쓰지 말지 |
| 출력 | 반환 항목 · 반환하지 않는 정보 |
| 읽기 · 쓰기 | 읽기 전용 명시<br>레코드 변경 = 다른 tool 사용 안내 |
| 범위 | 데이터 소스 · 수록 기간 · 검색어 예시 |
| 넣지 않을 내용 | 구현 언어 · framework · SLA · 소유 팀<br>→ 선택 단서 ✗ |
| 한 줄 description | 유사 tool 간 선택 신뢰도 하락<br>신규 tool이 안 불리는 원인 |
| 새 tool 추가 시 | 기존 유사 tool description에도 구분 사용법 추가 |

| 구분 | 내용 |
|---|---|
| tool 이름 | 대상 · 범위가 드러나게<br>예: `extract_web_results`<br>예: `search_own_archive_1990_2015` |
| 파라미터 이름 | 모호한 `id` · `q` → `line_id` · `machine_id`<br>허용 ID 형식을 description에 기재 |
| 이름만 변경 | description 그대로면 정보량 불변 → 효과 미미 |
| 이름 · description 거의 동일한 tool 둘 | 모델이 고를 근거 부재 = 결함<br>코드 중복 · latency · 비용 = 부차적 |

| 증상 | 원인 | 조치 |
|---|---|---|
| 읽기 tool이 변경 요청 처리<br>(조회 후 "변경 완료" 응답) | description 경계 부재 | 각 tool 용도 · 전환 조건 기재<br>읽기 전용 명시 |
| 같은 일을 하는 tool 여럿<br>(파일 읽기 3종) | 선택 근거 부재 | 하나로 통합<br>또는 description 구분 |
| 분리 유지 요건 있음<br>(출력 사양 · 감사 로그) | 통합 불가 | 대상 드러낸 이름<br>+ 사용 · 비사용 경계 description |
| 내장 tool(Grep)이 MCP tool보다 우선 | MCP description 최소 | 반환 값 · 내장보다 나은 상황 기재 |
| 신규 tool이 거의 안 불림 | 범위 없는 이름 · 한 줄 설명 | 수록 범위 · 검색어 예시<br>+ 범위 드러낸 이름 |
| 올바른 tool에 잘못된 입력 | 선택이 아닌 입력 형식 문제 | 입력 형식 · `input_examples`<br>필수 파라미터 |
| 모호한 표현이 검색 tool로 전달 | 허용 입력 정보 부재 | 허용 형식 · 입력 예 · edge case<br>사용 범위 기재 |

<sub>근거: CCAR-F-Amey-Thakur-0010, CCAR-F-Amey-Thakur-0031, CCAR-F-Amey-Thakur-0039, CCAR-F-Amey-Thakur-0075, CCAR-F-MyPractice-0007, CCAR-F-MyPractice-0046, CCAR-F-MyPractice-0057, CCAR-F-Udemy01-0026, CCAR-F-Udemy02-0016, CCAR-F-Udemy02-0057, CCAR-F-Udemy03-0027, CCAR-F-Udemy04-0018, CCAR-F-Udemy04-0021, CCAR-F-Udemy04-0060, CCAR-F-Udemy05-0046, CCAR-F-Udemy05-0052, CCAR-F-Udemy06-0007, CCAR-F-Udemy06-0018, CCAR-F-Udemy06-0052, CCAR-F-paullarionov-0007, CCAR-F-paullarionov-0046, CCAR-F-paullarionov-0057, CCAR-F-preporato-0016</sub>

@@ ADD-TO: ### 1-7. Tool 결과 크기 설계

| 상황 | 반환 | 이유 |
|---|---|---|
| 큰 payload가 context 대부분 차지 | 작업 관련 결과만<br>상세는 별도 요청으로 제공 | 추론에 쓸 context 확보 |
| 사용자 설명에 쓸 값이 UUID · 코드뿐 | 의미 있는 이름 · 상태 우선 | 자연어 이름 → 정확도 상승<br>hallucination 감소 |
| 이름(설명용) + ID(후속 호출용) 둘 다 필요 | `response_format` enum<br>`concise` = 이름 · 상태(기본)<br>`detailed` = ID 포함 | 한 tool로 두 수요 충족 |
| 검색 후보 여럿(모호) | 후보 전부 + 식별 정보<br>(ID · 상태 · 등록일) | 모호함을 드러내 추측 방지 |
| 후보 여럿일 때의 동작 | description에 "작업 전 확인 요청" 명시 | 한 건 임의 채택 방지 |

| 구분 | 내용 |
|---|---|
| 설계 기준 | agent가 결과만 읽고 다음 행동을 정할 수 있는가 |
| 반환 원칙 | 다음 판단에 필요한 식별자 · 정보만 |
| identifier만 반환 | ✓ 다음 호출에만 쓰는 값<br>✗ 사용자 설명에 필요한 값 |

<sub>근거: CCAR-F-Amey-Thakur-0030, CCAR-F-Udemy01-0007, CCAR-F-Udemy03-0057</sub>

@@ NEW-SECTION
### system prompt 지시가 만드는 tool 선택 왜곡
**description이 명확해도 키워드 지시가 덮어씀**

| 증상 | 원인 | 조치 |
|---|---|---|
| description 보강 · 경계 명기 후에도<br>특정 단어 포함 요청만 오선택 | system prompt의<br>키워드 반응형 지시 | 지시 삭제<br>또는 질문 대상에 따라 고르는 표현 |
| 특정 단어 유무로 첫 호출 tool이 갈림 | 단어 → tool 매핑 지시 | 같은 조치 |
| 규제 · 확인 어구 등장 시 전용 tool 과호출 | "CRITICAL: You MUST" 류 강한 표현<br>+ 넓은 적용 범위 | 평이한 표현(`Use this tool when...`)<br>정식 대상으로 범위 축소<br>prompt · description 양쪽 수정 |
| "먼저 로그 검색" 지시 → 내장 Grep 편중 | 일반 지시가 MCP tool 사용 억제 | 지시의 대상 한정<br>+ MCP description 보강 |
| 한 단어("검색")로 tool 지정 → 한 tool 편중 | 키워드 지시 + 겹치는 이름 | 이름 · description 정비<br>지시를 질문 대상 기준으로 수정 |

| 구분 | 내용 |
|---|---|
| 점검 순서 | ① description 구분성<br>② system prompt의 tool 이름 · 키워드 지시 |
| 단서 | "쓸 수 없다"가 아니라 "쓸 수 있는데 선택 안 됨"<br>description 개선 후에도 특정 단어에서만 오류<br>= prompt 지시 의심 |
| tool 추가 시 | 기존 description · system prompt의 충돌 표현 점검 |
| 모델 의존 | 최근 모델(Opus 4.5 · 4.6) = prompt 반응성 높음<br>이전 모델용 강한 표현 → 과호출<br>⚠️ 모델 세대 기준 서술 · 시점에 따라 변동 |

<sub>근거: CCAR-F-MyPractice-0056, CCAR-F-Udemy03-0056, CCAR-F-Udemy04-0021, CCAR-F-Udemy05-0020, CCAR-F-Udemy06-0007</sub>

@@ RULES
| 지속적 tool 오선택 | 첫 확인 = description의 용도 · 경계 구분<br>입력 형식 · 예시 · 비교 경계까지 확장 |
| 읽기 tool이 변경 요청 처리 | 각 tool 용도 · 전환 조건 기재<br>읽기 전용 명시 |
| 같은 일 하는 tool 여럿 | 하나로 통합 또는 description 구분 |
| 출력 사양 · 감사 로그로 tool 분리 유지 | 대상 드러낸 이름 + 사용 · 비사용 경계 description |
| 내장 tool만 쓰고 MCP tool 미사용 | MCP description 보강 + 일반 지시의 대상 한정 |
| 신규 tool이 거의 안 불림 | 범위 드러낸 이름 + 수록 범위 · 검색어 예시 |
| description 명확한데 특정 단어에서만 오선택 | system prompt 키워드 지시 수정 |
| 올바른 tool에 잘못된 입력 | 입력 형식 · `input_examples` · 필수 파라미터 |
| 텍스트만 응답 제거 + 출구 tool 여럿 | `tool_choice: any` |
| 문서 유형 미정 + 추출 schema 여럿 | `tool_choice: any` |
| workflow 첫 단계만 고정 | 첫 요청 `tool` → 이후 `auto` |
| 해당 없음 결과가 텍스트로 샘 | 빈 결과 보고 tool 추가 + `any` |
| tool 호출 결과를 schema 준수로 수신 | `strict: true` client tool + `tool_use` 수신 |
| 인계 데이터 일관성 | 필수 필드 지정 tool + 호출 지시 |
| tool 작업 범위 제한 | schema 상한 + 앱 검증 ⚠️ 수치 제약은 strict 미지원 |
| 큰 payload가 context 점유 | 작업 관련 결과만 + 상세는 별도 요청 |
| UUID만 반환해 이름 재조회 반복 | `response_format` enum(`concise` · `detailed`) |
| 검색 결과가 모호 | 후보 전부 + 식별 정보 + description에 확인 요청 |
| 권한 검사 뒤 앱 코드에서 tool 실행 | `tool_result` 반환 + `tool_use`인 동안 loop |
<sub>근거: CCAR-F-Amey-Thakur-0010, CCAR-F-Amey-Thakur-0030, CCAR-F-Amey-Thakur-0039, CCAR-F-MyPractice-0056, CCAR-F-Udemy01-0007, CCAR-F-Udemy01-0016, CCAR-F-Udemy01-0054, CCAR-F-Udemy02-0016, CCAR-F-Udemy03-0027, CCAR-F-Udemy03-0032, CCAR-F-Udemy03-0057, CCAR-F-Udemy04-0021, CCAR-F-Udemy04-0044, CCAR-F-Udemy05-0046, CCAR-F-Udemy06-0018, CCAR-F-Udemy06-0039, CCAR-F-Udemy06-0048, CCAR-F-Udemy06-0052, CCAR-F-paullarionov-0057, CCAR-F-preporato-0016, CCAR-P-jrajath94-0477, CCAR-P-jrajath94-0589</sub>

@@ TRAPS
| 선택 혼동에 네 번째 tool 추가<br>fine-tuning · 무작위 선택 | 겹침 악화 · 과함 · 혼란을 제도화 |
| 첫 대응으로 tool 통합<br>(mode 플래그 · `lookup_entity`) | 근본 원인 = description 정보 부족<br>분리 요건(출력 사양 · 감사 로그) 위반 가능 |
| 사전 routing classifier · 전처리 · routing 계층 | 선택 단서(description) 미개선<br>구조만 복잡 |
| system prompt 한 문장 · few-shot 추가로 교정 | description 수정보다 약한 신호<br>모순 지시가 남으면 근본 해결 ✗ |
| 원인을 description 부족 · tool 수<br>few-shot 부족으로 진단 | description 명확 · tool 5개로 이미 부정된 사실<br>원인 = prompt 키워드 지시 |
| 기본 학습 연관 · fine-tuning · 부정 예시로 설명 | description 이미 명확<br>원인 = prompt 수준 지시 |
| tool 수 축소 · 유사 tool 삭제 | 첫 확인 아님<br>정상 조회 기능 상실 |
| `tool_choice` 강제(고정 · 매 턴 `any`)로 오선택 교정 | 선택 문제를 우회 · 입력별 선택 포기<br>잘못된 tool 강제 가능 |
| 오선택 결과를 hook으로 폐기 · loop에서 재실행 | 원인 방치 · 증상 처치 |
| 내장 tool(Grep) · `search_web` 비활성화 | 선택 문제를 강제로 억제 · 필요 기능 상실 |
| `CLAUDE.md` "항상 사용" 지시 · 요청마다 tool 지정 | 확률적 준수 · 수작업 의존 |
| 서버 등록 스코프 이동 · 개발자에게 tool 선택 위임 | 선택 판단 재료 불변 |
| 이름만 변경 · 파라미터 이름만 변경 | description 그대로 → 정보량 불변 |
| description을 1줄로 통일(토큰 절약) | 구별 단서 소실 |
| "~ 단어 → 이 tool" 키워드 규칙 추가 | 새로운 오라우팅 유발 |
| 입력 예를 JSON Schema 필드 설명에만 추가 | 선택 후 인수 개선 · "무엇을 고르나"에 영향 ✗ |
| description에 구현 언어 · SLA · 소유 팀 기재 | 선택과 무관한 정보 |
| 이름 거의 같은 tool 둘의 결함을<br>코드 중복 · latency · 비용으로 지목 | 결함 = 선택 시점의 근거 부재<br>나머지는 부차적 |
| 텍스트만 응답을 아래로 해결<br>`any` 단독 · `tool` 고정<br>텍스트 후처리 · prompt 강조 | `any` 단독 = 추측 기록<br>`tool` 고정 = 해당 없음 보고처 소멸<br>후처리 · 강조 = 사후 수습 · 확률적 |
| 매 요청 `tool` 고정<br>+ description에 "다음에 호출" 기재<br>또는 반복 전환 | 강제를 description이 못 이김<br>번갈아 강제 = loop 종료 불가 |
| `none` · `tool_choice` 생략 · 매 턴 강제로 순서 확보 | `none` = 필요 tool까지 차단<br>생략 = `auto` 기본값 · 순서 보장 ✗ |
| 구조화 출력에 `tool` 고정 · `auto` · prefill | 문서 유형 무시 고정 · 대화 응답 여지<br>prefill = 신규 모델 사용 ✗ |
| 구조 출력을 사후 검증 server · 지시 강화 + 재시도로 보장 | 잘못된 출력 발생 자체 방지 ✗ |
| 자유 서술 + 항목 bullet 지시 · 무관한 tool 강제 | 형식 보장 ✗ · 강제 대상이 다른 처리 |
| system prompt에 성공 예시만 추가 · 메타데이터 최소 유지 | "모호하면 확인" 판단 지원 ✗ |
| 고정 순서 controller · 응답 텍스트 키워드 파싱 | 적응성 상실 · 구조화 호출 미사용 |
| 모델이 자체 네트워크로 API 직접 호출 | client tool = 앱 실행 · 권한 검사 우회 |
| `stop_reason`을 `tool_result`로 설정 | `tool_result` = 블록 유형 · stop reason ✗ |
| 요약 텍스트만 새 요청 · 요약 먼저<br>결과 분할 · assistant에 결과 | 결과 ↔ 호출 대응 소실 · 순서 · 묶음 · 역할 규칙 위반 |
| context window 확대<br>두 번째 모델 호출로 요약 · 호출 횟수 감소 | 문제 지연 · 비용과 실패 지점 증가 · payload 불변 |
| UUID 문제에 pagination · `strict`<br>`resolve_ids` 추가 | 양 · 입력 형식 문제 해결 · 왕복만 증가 |
| 후보 여럿 중 최신 · 유사도 자동 선택 | 확인 없는 추측 |
| 무제한 export 유지 + 로깅<br>export 전체 제거 · 두 번째 tool 추가 | 로깅 = 관찰 · 통제 ✗<br>제거 = 기능 상실 · 추가 = 범위 문제 미해결 |
<sub>근거: CCAR-F-Amey-Thakur-0010, CCAR-F-Amey-Thakur-0030, CCAR-F-Amey-Thakur-0031, CCAR-F-Amey-Thakur-0039, CCAR-F-Amey-Thakur-0075, CCAR-F-MyPractice-0007, CCAR-F-MyPractice-0046, CCAR-F-MyPractice-0056, CCAR-F-MyPractice-0057, CCAR-F-Udemy01-0006, CCAR-F-Udemy01-0007, CCAR-F-Udemy01-0016, CCAR-F-Udemy01-0026, CCAR-F-Udemy01-0054, CCAR-F-Udemy01-0056, CCAR-F-Udemy02-0016, CCAR-F-Udemy02-0057, CCAR-F-Udemy03-0027, CCAR-F-Udemy03-0032, CCAR-F-Udemy03-0042, CCAR-F-Udemy03-0056, CCAR-F-Udemy03-0057, CCAR-F-Udemy04-0018, CCAR-F-Udemy04-0021, CCAR-F-Udemy04-0044, CCAR-F-Udemy04-0060, CCAR-F-Udemy05-0002, CCAR-F-Udemy05-0020, CCAR-F-Udemy05-0046, CCAR-F-Udemy05-0052, CCAR-F-Udemy06-0007, CCAR-F-Udemy06-0018, CCAR-F-Udemy06-0039, CCAR-F-Udemy06-0048, CCAR-F-Udemy06-0052, CCAR-F-paullarionov-0007, CCAR-F-paullarionov-0046, CCAR-F-paullarionov-0057, CCAR-F-preporato-0016, CCAR-P-jrajath94-0477, CCAR-P-jrajath94-0589</sub>

@@ MEMO
| `input_examples` | tool 정의의 선택 필드<br>`input_schema`에 맞는 입력 예시 배열 |
| `required` | `input_schema`의 필수 필드 지정<br>Claude가 채워 호출 |
| `response_format` | 결과 상세도 enum 파라미터<br>`concise`(이름 · 상태) / `detailed`(ID 포함) |
| `tool_choice: {"type": "tool", "name": ...}` | 지정 tool 강제 · 요청 단위 설정 |
| `stop_reason: end_turn` | loop 종료 신호의 하나<br>(`tool_use`인 동안 반복) |
| 빈 결과 보고 tool | "해당 없음"을 기록하는 출구 tool<br>검색 범위 · 이유를 필수 필드로 |
<sub>근거: CCAR-F-Udemy01-0016, CCAR-F-Udemy03-0027, CCAR-F-Udemy03-0042, CCAR-F-Udemy03-0057, CCAR-F-Udemy04-0044, CCAR-F-Udemy05-0046, CCAR-F-Udemy06-0039, CCAR-P-jrajath94-0589</sub>

@@ CHECK
- [ ] 오선택 첫 확인 = description 구분성 · prompt 키워드 지시
- [ ] 텍스트만 응답 제거 = `any` · 첫 단계 고정 = 첫 요청만 `tool`
- [ ] 구조 보장 = 생성 시 제약(`strict`) > 사후 검증
- [ ] 결과 반환 = 필요한 것만 · 이름 포함 · 모호하면 후보 전부
<sub>근거: CCAR-F-Amey-Thakur-0030, CCAR-F-Udemy01-0007, CCAR-F-Udemy01-0054, CCAR-F-Udemy03-0057, CCAR-F-Udemy04-0044, CCAR-F-Udemy05-0020, CCAR-F-Udemy06-0048, CCAR-F-paullarionov-0046</sub>
