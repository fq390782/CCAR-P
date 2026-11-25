@@ ADD-TO: ### 1-6. Tool description과 tool surface 설계

**재설계 신호 · 비신호**

| 관찰 | 판정 |
|---|---|
| 요청 처리 불가 tool을 반복 선택 | 재설계 신호<br>description만으로 tool 구별 불가 = 설계 결함 |
| tool 개수(5개 · 10개 초과) | 그 자체로 결함 ✗ |
| tool이 JSON · 큰 payload 반환 | 신호 ✗ (tool 선택 문제와 별개) |
| 구현이 여러 서비스에 분산 | 신호 ✗ |
| 두 tool 설명이 겹침<br>(둘 다 "고객 찾기"를 처리하는 듯 보임) | capability bloat 신호 |
| 노출 45개 중 호출 로그에 9개만 사용 | capability bloat 신호<br>(미사용 tool도 매 요청에 실림) |
| subagent별 tool 범위 한정 · 읽기 전용 자격 증명<br>description 속 "쓰지 말 때" 명시 | bloat 아님 = 해결책 |

**중복 tool 정리**

| 상황 | 조치 |
|---|---|
| 이름만 다른 동일 기능 tool 2~3개<br>(`quote_rate` · `get_rate_quote`<br>`rate_lookup`) | 하나만 남기고 제거<br>설명 하나 + 명확한 schema |
| "안전을 위해" 중복 유지 | ✗ 같은 동작에 이름 둘 = 오선택 확률 2배 |
| 중복 tool 추가 · 이름 주기적 변경 | ✗ bloat 악화 |
| 겹치는 조회 tool 2개 + 거의 같은 설명 | 구별되는 설명의 tool 하나로 병합 |
| 병합 · 제거 시 숨은 의존성 | 호출 측을 병합 tool로 갱신<br>숨은 workflow 호출 여부 확인 |
| 두 tool이 다른 백엔드 · 다른 SLA | 진짜 중복 아님 → 병합 전 확인 |
| 정리 후 | bloat 주기 검토 필요<br>담당자 없으면 tool 재증가 |

<sub>근거: CCAR-F-Amey-Thakur-0028, CCAR-F-Amey-Thakur-0061, CCAR-P-jrajath94-0158, CCAR-P-jrajath94-0297, CCAR-P-jrajath94-0352, CCAR-P-jrajath94-0414, CCAR-P-jrajath94-0478, CCAR-P-jrajath94-0541, CCAR-P-jrajath94-0630, CCAR-P-preporato-0012</sub>

@@ NEW-SECTION
### 범용 tool 분할 vs 통합
**입출력이 다르면 분할 · 같은 일이면 병합**

| 상황 | 방향 |
|---|---|
| 범용 tool 하나(`analyze_document`)가<br>추출 · 요약 · 검증을 인자로 선택 | 목적별 tool로 분할 예: `extract_data_points`<br>`summarize_content`<br>`verify_claim_against_source` |
| 증상 = 같은 요청인데 출력 형식이 매번 다름 | 원인 = tool 입자도<br>→ 분할 + 각 tool 입출력 사양 명시 |
| 하위 단계가 특정 필드 구조를 기대 | 목적별 tool의 output schema로 형식 고정 |
| 필수 입력 누락<br>(검증 tool이 source 발췌 없이 호출됨) | `input_schema`에서 필수 파라미터로 지정<br>→ schema 단계에서 호출 불성립 |
| 분할 후 tool 수 | 역할이 안 겹치는 소수의 workflow 전용 tool<br>불필요한 tool 추가 ✗ |
| 한 API 호출에 여러 목적 + 전체 tool 노출<br>(리뷰 · 테스트 생성 · 메타 갱신) | 증상 = 목적 밖 tool 호출 · 구조화 객체 대신 평문<br>→ 단계를 역할별로 분리 |
| 같은 일 · 같은 입력 형태의 tool 둘 | `action` 파라미터 + 명확한 설명의<br>tool 하나로 병합 가능 |
| 유사 조회 tool 다수 + 위험한 범용 tool | 좁은 이름의 파라미터화 tool 몇 개로 통합<br>(명시적 쿼리 유형을 가진 reporting tool) |
| 40개 동작을 mode 파라미터 하나로 | ✗ 동작이 선택 단계에서 숨음 |
| 18개 tool을 `action` 파라미터 범용 tool 하나로 | ✗ 목적이 모호한 tool |

**분할을 받쳐 주는 장치**

| 장치 | 효과 |
|---|---|
| description에 쓸 때 · 쓰지 말 때 경계 | tool 선택 안정 |
| 입출력을 JSON schema로 정의 | 결과 형태 고정 |
| 단계별로 필요한 tool만 노출 | 단계 밖 tool 호출 원천 차단 |
| 구조화 출력이 필수인 단계 | `tool_choice`로 보고용 tool 지정<br>⚠️ 신규 모델 일부 `any`/`tool` 400 → `strict` |
| tool 이름의 namespace | 보조 수단 · 노출 범위는 못 좁힘 |
| output schema를 coordinator 측 검증에도 사용 | 형식이 깨진 결과 조기 검출 |
| tool 반환값에 출처 문서명 · 발췌 위치 | 통합 단계의 출처 보존 |

<sub>근거: CCAR-F-Amey-Thakur-0028, CCAR-F-Udemy02-0048, CCAR-F-Udemy03-0004, CCAR-F-Udemy04-0029, CCAR-F-Udemy06-0030, CCAR-F-Udemy06-0056, CCAR-P-Amey-Thakur-0003, CCAR-P-Amey-Thakur-0038, CCAR-P-jrajath94-0078, CCAR-P-jrajath94-0630</sub>

@@ NEW-SECTION
### 역할별 tool 범위 (subagent tool 제한)
**agent마다 맡은 역할의 tool만 부여**

| 구분 | 내용 |
|---|---|
| 원칙 | agent별 tool set = 그 역할에 필요한 것만 |
| tool 과다의 증상 | 판단 복잡도 증가 → tool 선택 신뢰성 저하<br>전문 밖 tool 오용<br>(문서 분석 agent의 웹 검색 · 서식 tool) |
| 가이드 예시 | 18개 공유 → 역할당 4~5개로 축소<br>⚠️ 4~5개 = 가이드 예시 수치<br>공식 문서 기준 = 30~50개 초과 시 정확도 저하 |
| Agent SDK | subagent별 `tools`로 사용 가능 tool 지정<br>(`AgentDefinition`의 `tools`) |
| 운영 확인 | tool 호출 로그 정기 점검 → 역할 밖 호출 모니터링 |

**오류 유형별 1차 수단**

| 오류 유형 | 1차 수단 |
|---|---|
| 비슷한 tool 사이 혼동 | description 개선 |
| 역할 밖 tool 사용 | tool 배분 재검토(역할별 제한) |

**역할 횡단 · 역할 경계 처리**

| 상황 | 방향 |
|---|---|
| 전문 agent가 타 역할 tool(web_search) 보유<br>→ 미검증 출처 혼입 · 필요 빈도 낮음(약 10%) | tool 제거<br>추가 조사는 coordinator 경유 routing |
| 타 역할 필요가 빈번 · 대부분 단순 확인(예: 85%) | 범위 제한 tool(`verify_fact`) 부여 |
| 복잡 · 깊은 조사(예: 15%) | 기존 경로 유지<br>coordinator → 전문 agent |
| 전문 agent에 타 역할 tool 전체 부여 | ✗ 역할 확대 · 오용 가능성 유지 |
| 추가 조사가 필요한 이유 | 구조화해 coordinator에 반환<br>→ 초점 좁힌 위임 |
| 역할 안에서 빈번한 조회(예: 직종 코드 60%) | 읽기 전용 · 조회 한정 tool(`lookup_job_code`) 추가<br>tool 전부 박탈 ✗ (coordinator 왕복 증가) |
| 범용 tool(`fetch_url`)이 역할 밖 기능 허용 | 용도 한정 tool(`load_document`)로 교체<br>→ interface 단계에서 기능 제한 |
| 전문 agent의 쓰기 작업<br>(DB 직접 쓰기 · 티켓 등록 · CRM 갱신) | 쓰기 = coordinator · 별도 단계 담당<br>전문 agent = 읽기 + 구조화 결과 반환까지 |

**역할별 tool 범위 사례**

| agent | 부여 범위 |
|---|---|
| 저장소 scanner subagent | 읽기 전용(`Read` · `Grep` · `Glob` · 의존성 검사)<br>티켓 등록 = 합쳐진 결과 기반 coordinator만 |
| 추출 subagent | 문서 읽기 + 추출 결과 제출만<br>웹 검색 · 검증 전 DB 쓰기 ✗ |
| 추출 agent의 CRM · 메일 · 캘린더 | 별도 agent · 별도 단계로 분리 |
| 여러 MCP server 연결 agent | agent마다 책임에 필요한 server만 제공 |

<sub>근거: CCAR-F-MyPractice-0010, CCAR-F-MyPractice-0015, CCAR-F-Udemy04-0019, CCAR-F-Udemy04-0047, CCAR-F-Udemy05-0040, CCAR-F-Udemy06-0030, CCAR-F-paullarionov-0010, CCAR-F-paullarionov-0015, CCAR-F-preporato-0007, CCAR-P-preporato-0013</sub>

@@ NEW-SECTION
### 최소 권한 tool surface (불필요 기능 제거)
**필요 없는 권한은 감시가 아니라 제거**

| 통제 수단 | 판정 |
|---|---|
| 불필요 tool · 기능 제거<br>(update · delete · 쓰기 작업) | ✓ 공격 · 오류 표면 자체를 없앰 |
| 필요한 쓰기 · 삭제 tool의 범위 제한<br>(코드 내 확인 · 영향 범위 상한 · 허용 대상) | ✓ |
| 읽기 / 쓰기 권한 분리<br>쓰기는 역할상 필요한 곳만 + 명시적 승인 게이트 | ✓ |
| 로깅 · 감사 추적 · 대시보드 · 모니터링 | 포렌식 · observability용<br>권한 제거 ✗ → 로그는 유지하되 해결책으로 보지 않음 |
| 확인 대화상자 · 업무 시간 제한 | 보완 통제 · 권한은 활성 상태 |
| 두 번째 모델의 호출 검토 | ✗ 같은 오해석 반복 · tool은 활성 |
| 문서화 · 이름 변경 · 숨김 | ✗ 기능 접근 그대로 |
| 더 긴 system prompt · 자가 재확인 | ✗ 확률적 |
| 모든 tool 제거 | ✗ 최소 권한 아닌 권한 없음 |

**제거 · 유지 판정**

| 상황 | 판정 |
|---|---|
| 어떤 작업도 안 쓰는 위험 tool<br>(`drop_table` · `delete_*`<br>`wire_transfer` · `mass_email`) | 제거 |
| "나중에 유용할지도" | 작업 기준 아님 → 지금 제거<br>필요해지면 검토 후 재추가 |
| 매일 쓰는 정당한 tool | 유지 |
| 고빈도 + gate 정상인 민감 tool(`refund`) | 유지 · 민감성은 gate가 처리 |
| 사고를 낸 `delete_account` | 제거 또는 범위 제한<br>(코드 확인 · 영향 범위 제한 · 허용 대상) |
| 사고 대응에 실제로 필요한 삭제 tool | 유지 + 감시 + gate (반례) |
| 사용 중이어도 필요 이상 데이터 반환<br>(전체 SSN · 결제 정보 포함 프로필) | 반환 필드를 작업 필요분으로 축소<br>다른 작업이 필요하면 tool 분리 |
| 하루 1회 쓰는데 스키마 4,000 토큰 | 사용 여부만으로 유지 정당화 ✗<br>호출마다 스키마 토큰 계산 → 스키마 축소 대상 |
| "미사용" 판정 전 | 장기 trace(예: 6개월)로 확인<br>숨은 호출자 · workflow 확인 |

**범용 tool → 범위 제한 tool**

| 범용 tool | 교체 방향 |
|---|---|
| 임의 SQL(`run_sql` · raw SQL) | 검증된 고객 ID만 받아 그 범위만 반환<br>(`get_account_summary`) |
| DB 전체를 노출하는 범용 query tool 하나 | model 권한이 무제한 → least privilege 적용 불가 |
| 교체 효과 | 조회 범위를 코드로 결정론적 제한 |
| 이중 방어 | 교체 tool 내부에서 전달 ID = 본인 확인 결과인지 검사 |
| 낮은 오류율(예: 0.4%) | 면제 사유 ✗ · 범용 tool이 남는 한 타 고객 데이터 도달 가능 |
| 이 용도에 불필요한 쓰기 작업을 노출한 MCP tool | 제거 |

<sub>근거: CCAR-F-Amey-Thakur-0063, CCAR-F-Amey-Thakur-0077, CCAR-F-Udemy06-0041, CCAR-P-Amey-Thakur-0001, CCAR-P-Amey-Thakur-0050, CCAR-P-jrajath94-0078, CCAR-P-jrajath94-0157, CCAR-P-jrajath94-0158, CCAR-P-jrajath94-0159, CCAR-P-jrajath94-0297, CCAR-P-jrajath94-0351, CCAR-P-jrajath94-0352, CCAR-P-jrajath94-0415, CCAR-P-jrajath94-0478, CCAR-P-jrajath94-0540, CCAR-P-jrajath94-0541</sub>

@@ NEW-SECTION
### Tool 과다 대응 (progressive discovery · tool search)
**전부 노출하지 않고 필요할 때 로드**

| 증상 | 내용 |
|---|---|
| 정의만으로 토큰 소비 | 예: 220개 ≈ 60,000 토큰<br>200개 ≈ 100,000 스키마 토큰/호출 |
| 이름이 비슷한 tool 혼동 증가 | 표면이 클수록 오선택 증가<br>공식 문서: 30~50개 초과 시 정확도 저하 |
| 다수 agent · 다수 MCP server<br>(예: 6 server 300개 · 8 시스템 45개) | 전부 선로드 → 비용 증가 + 선택 부정확 |

| 해법 | 내용 |
|---|---|
| tool search tool + `defer_loading: true` | deferred 정의는 검색에서 발견될 때만 context에 전개<br>모든 tool 계속 사용 가능 |
| 자주 쓰는 3~5개 | non-deferred 유지 → 검색 왕복 없음 |
| tool search tool 자체 | `defer_loading` 적용 ✗<br>최소 1개는 non-deferred |
| deferred tool + `cache_control` | 400 오류 |
| progressive discovery | 이름 목록 먼저 → 전체 스키마는 필요 시<br>작업별 가시 선택지 축소 |
| 판정 시점 | 표면 약 20개 초과 + 토큰이 제약이면 사용<br>⚠️ 약 20개 = 해설 자체 기준 · 공식 문서는 30~50개 초과 |
| 책임별 범위 지정 | agent마다 필요한 server · tool 집합만 제공<br>나머지는 점진적 발견 |
| 그룹화 | 이름 잘 지은 소수 함수 · namespace 있는 MCP server<br>구분되는 소수의 진입점 + 세부는 필요 시 |
| 트레이드오프 | 조회 단계 추가<br>이름 색인이 부정확하면 올바른 tool 못 찾음 |

<sub>근거: CCAR-F-Udemy01-0035, CCAR-P-Amey-Thakur-0003, CCAR-P-Amey-Thakur-0038, CCAR-P-jrajath94-0003, CCAR-P-jrajath94-0179, CCAR-P-jrajath94-0629, CCAR-P-jrajath94-0650, CCAR-P-preporato-0013</sub>

@@ RULES
| 상황 | 정답 |
|---|---|
| tool을 반복해서 잘못 고름 | description만으로 구별 불가<br>→ tool surface 재설계(중복 병합 · 역할 분리) |
| 범용 tool 하나에 여러 목적 + 출력 형식 불안정 | 목적별 tool 분할 + 입출력 schema 명시 |
| 검증 tool이 필수 입력 없이 호출됨 | `input_schema`의 필수 파라미터로 지정 |
| 한 호출에서 리뷰 · 생성 · 갱신 혼재 | 단계 분리 + 단계별 필요 tool만 노출<br>구조화 필수 단계 = `tool_choice`로 보고용 tool 지정 |
| 같은 일을 하는 tool 둘 | 하나 제거 · 또는 `action` 파라미터 tool로 병합 |
| 모든 subagent에 같은 18개 tool + 역할 밖 호출 | agent별 역할 tool(4~5개)로 제한 |
| 비슷한 tool 혼동 vs 역할 밖 tool 사용 | 혼동 = description 개선<br>역할 밖 = 배분 재검토 |
| 범용 `fetch_url`이 검색까지 수행 | 용도 한정 `load_document`로 교체 |
| 전문 agent의 단순 확인 빈도 높음 | 범위 제한 tool 부여 · 복잡 건은 coordinator 경유 |
| 전문 agent의 타 역할 tool 필요 빈도 낮음 | tool 제거 + coordinator routing |
| 읽기 위주 scanner agent | 읽기 전용 tool만 · 쓰기(티켓)는 coordinator만 |
| 작업에 안 쓰는 위험 tool(delete · drop · wire) | 제거 (로깅 · 모니터링 ✗) |
| 임의 SQL tool이 타 고객 데이터 노출 | 검증 ID 범위만 반환하는 tool로 교체 |
| 작업에 필요 없는 필드(SSN · 결제 정보) 반환 | 반환 필드 축소 |
| 읽기 · 쓰기 혼재 agent | 읽기 / 쓰기 분리 + 쓰기는 필요 역할만 + 승인 게이트 |
| tool 수십~수백 개 + 전부 사용 가능 유지 + 토큰 · 혼동 문제 | tool search + `defer_loading`<br>자주 쓰는 3~5개는 non-deferred |
| 여러 팀 agent에 40~45개 tool 노출 | 작업 · 역할별 범위 + progressive discovery |

<sub>근거: CCAR-F-Amey-Thakur-0028, CCAR-F-Amey-Thakur-0061, CCAR-F-Amey-Thakur-0063, CCAR-F-Amey-Thakur-0077, CCAR-F-Udemy01-0035, CCAR-F-Udemy02-0048, CCAR-F-Udemy03-0004, CCAR-F-Udemy04-0019, CCAR-F-Udemy04-0029, CCAR-F-Udemy04-0047, CCAR-F-Udemy05-0040, CCAR-F-Udemy06-0030, CCAR-F-Udemy06-0041, CCAR-F-Udemy06-0056, CCAR-F-paullarionov-0010, CCAR-F-paullarionov-0015, CCAR-F-preporato-0007, CCAR-P-Amey-Thakur-0001, CCAR-P-Amey-Thakur-0003, CCAR-P-Amey-Thakur-0038, CCAR-P-Amey-Thakur-0050, CCAR-P-jrajath94-0003, CCAR-P-jrajath94-0159, CCAR-P-jrajath94-0179, CCAR-P-jrajath94-0629, CCAR-P-jrajath94-0630, CCAR-P-jrajath94-0650</sub>

@@ TRAPS
| 오답 | 이유 |
|---|---|
| tool 개수 · JSON 반환 · 구현 분산 · payload 크기를<br>재설계 신호로 판단 | 그 자체로 결함 아님<br>신호 = 엉뚱한 tool의 반복 선택 |
| 역할 밖 tool 오용을 prompt 금지로 처리<br>(`web_search`를 쓰지 말라는 지시 등) | 확률적 · tool 접근 그대로<br>용도 한정 tool 교체 · 제거가 정답 |
| `fetch_url`에 검색 엔진 도메인 차단 필터 | 해설 정답 = 용도 한정 tool 교체 |
| 전문 agent에 타 역할 tool 전체 부여<br>(synthesis에 web-search 전부) | 역할 확대 · 미검증 출처 혼입 유지 |
| 검증 결과에 출처 신뢰도 표기만 추가 | 혼입 자체를 못 막음 |
| 추출 agent에 DB 전체 읽기 · 쓰기 권한 부여 | 필요 최소 초과 |
| 위험 tool 유지 + 로깅 · 모니터링 · 대시보드 | 가시성 ≠ 통제 · 권한 활성 상태 |
| 확인 대화상자 · 업무 시간 제한 · 두 번째 검토 모델 | 보완일 뿐 · 권한 존재 · 노출 시간대만 축소 |
| 쓰지 않는 tool을 "나중에 쓸지도"로 유지<br>문서화 · 이름 변경 · 숨김 | 기능 접근 그대로<br>최소 권한 = 현재 작업 기준 |
| refund처럼 gate된 고빈도 tool 제거 | 정당한 사용 박탈 · 민감성은 gate 몫 |
| 모든 tool 제거 후 context만으로 답변 | 정당한 기능 상실 |
| SQL 오류를 자가 재확인 · prompt 지시 · 사후 검토로 방어 | 확률적 준수 · 사후 검출 |
| 중복 tool을 "안전용"으로 유지 · 추가<br>이름 주기적 변경 | 오선택 확률 증가 · bloat 악화 |
| 더 긴 description · prompt 문서화로 겹침 해결 | 중복 · 과다 데이터는 못 고침<br>description 개선 = 구별되는 tool에만 유효 |
| tool recommender · 분류기 · 보조 tool 추가 | tool 수 증가 + 실패 경로에 모델 판단 추가 |
| 더 큰 모델 · 최고 등급<br>큰 context window · temperature 상향 | 증상 대응 · 구분 안 되는 선택지 그대로<br>토큰 과금 유지 · temperature = 무작위 증가 |
| tool 절반 무작위 제거 · 플랫폼 기능을 10개로 제한 | 필요 tool 제거 · 요구사항 희생 |
| 모든 description을 일률적으로 한 줄로 단축 | 토큰만 절감 · 선택 품질 하락 |
| 40개 · 18개 동작을 mode · `action` tool 하나로 | 동작이 선택 단계에서 숨음 · 목적 모호 |
| 범용 tool 유지 + 지시를 system prompt로 이동<br>enum에 작업명 추가 | 필수 조건을 schema로 표현 불가 |
| 자유 형식 응답 + 받는 쪽 해석 · 지시문 예시 10개 추가 | 편차를 소비 측으로 이동 · 자유 기술 구조 유지 |
| `tool_choice: none` + 텍스트에서 JSON 파싱 | 구조화 출력 수단 포기 |
| namespace만 정리 | 노출 범위를 못 좁힘 |
| 정의 과다에 description 단축 · `cache_control`<br>`tool_choice: any` | 단축 = 토큰만 · cache = 요금 · latency만<br>any = 호출 여부만 → 점유 · 혼동 둘 다 해결 ✗ |
| 모든 tool에 `defer_loading: true`<br>(tool search 포함) | 400 오류 · 자주 쓰는 tool도 검색 왕복 발생 |
| deferred tool에 `cache_control` | 400 오류 |
| tool 선택 개선용 few-shot · 예시를 prompt에 추가 | tool이 많은 상태 그대로 · 토큰만 증가 |
| 역할 밖 tool 호출에 `tool_choice: any` 설정 | 호출 여부만 제어 · 선택 문제와 무관 |
| 전체 description 재작성 · 오선택 감시 후 재분석 | 역할 밖 사용 = 배분 재검토가 직접 해결<br>감시 · 재분석 = 사후 대응 |

<sub>근거: CCAR-F-Amey-Thakur-0028, CCAR-F-Amey-Thakur-0061, CCAR-F-Udemy01-0035, CCAR-F-Udemy02-0048, CCAR-F-Udemy03-0004, CCAR-F-Udemy04-0019, CCAR-F-Udemy04-0029, CCAR-F-Udemy04-0047, CCAR-F-Udemy05-0040, CCAR-F-Udemy06-0030, CCAR-F-Udemy06-0041, CCAR-F-Udemy06-0056, CCAR-F-paullarionov-0010, CCAR-F-paullarionov-0015, CCAR-F-preporato-0007, CCAR-P-Amey-Thakur-0001, CCAR-P-Amey-Thakur-0003, CCAR-P-Amey-Thakur-0050, CCAR-P-jrajath94-0003, CCAR-P-jrajath94-0078, CCAR-P-jrajath94-0157, CCAR-P-jrajath94-0158, CCAR-P-jrajath94-0159, CCAR-P-jrajath94-0179, CCAR-P-jrajath94-0414, CCAR-P-jrajath94-0540, CCAR-P-jrajath94-0629, CCAR-P-jrajath94-0630, CCAR-P-jrajath94-0650, CCAR-P-preporato-0013</sub>

@@ MEMO
| 이름 | 의미 |
|---|---|
| tool surface | 모델에 노출되는 tool 전체 집합<br>(이름 · description · 스키마) |
| capability bloat | 겹치는 설명 · 미사용 tool이 쌓인 상태 |
| least privilege | agent마다 맡은 책임에 필요한 권한만 부여 |
| 범위 제한 tool | 한 용도만 허용하는 tool |
| `load_document` · `verify_fact` | 문서 URL 한정 · 단순 사실 확인 한정 tool |
| `lookup_job_code` | 직종 코드 조회 한정 · 읽기 전용 tool |
| `get_account_summary` | 검증된 고객 ID 범위만 반환하는 tool |
| 역할 횡단 tool | 빈도 높은 타 역할 필요를 범위 제한으로 충족 |
| `AgentDefinition`의 `tools` | Agent SDK에서 subagent별 사용 tool 지정 |
| progressive discovery | 이름 먼저 · 스키마는 필요 시 로드 |
| `defer_loading: true` | tool search로 발견될 때만 context에 전개<br>`cache_control`과 함께 쓰면 400 |

<sub>근거: CCAR-F-Udemy01-0035, CCAR-F-Udemy04-0047, CCAR-F-Udemy05-0040, CCAR-F-Udemy06-0041, CCAR-F-paullarionov-0010, CCAR-F-paullarionov-0015, CCAR-P-jrajath94-0179, CCAR-P-jrajath94-0629, CCAR-P-jrajath94-0650, CCAR-P-preporato-0012, CCAR-P-preporato-0013</sub>

@@ CHECK
- [ ] 반복 오선택 = tool surface 재설계 신호 (개수 · JSON · 구현 분산은 아님)
- [ ] 목적 · 입출력이 다르면 분할 · 같은 일의 중복은 병합 또는 제거
- [ ] agent별 tool = 역할 범위만 · 빈도 높은 단순 요구는 범위 제한 tool
- [ ] 불필요한 위험 tool = 제거 (로깅 · 모니터링 ✗)

<sub>근거: CCAR-F-Amey-Thakur-0061, CCAR-F-Udemy04-0029, CCAR-F-Udemy04-0047, CCAR-F-paullarionov-0015, CCAR-P-jrajath94-0351</sub>
