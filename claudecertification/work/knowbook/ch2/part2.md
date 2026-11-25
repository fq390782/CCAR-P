@@ ADD-TO: ### 1.5 Message Batches API

**workload 배정: 기다리는 사람이 있는가**

| 상황 | 배정 |
|---|---|
| 개발자 · 작업자 · 고객이 결과 대기<br>(PR merge 차단 검사 · 화면 앞 · 채팅 응답) | 동기 호출 |
| 일정 작업 · 마감 여유<br>(야간 · 주간 · 월말 마감 후 감사) | batch(50% 절감) |
| 이미 밤새 실행 · 완료 polling 구조 | batch 적합 |
| 한 시스템에 두 유형 혼재 | 작업별 분리<br>blocking = 동기 · 지연 허용 = batch |
| 판별 질문 | "누군가 결과를 기다리는가"<br>대기자의 사내 · 사외 구분 = 무관 |
| blocking 경로에 부적합한 이유 | 지연 시간 SLA 없음<br>처리 최대 24시간 |

**전송 주기 계산 (SLA 기반)**

| 구분 | 내용 |
|---|---|
| 최악 지연 | 전송 간격 + 전처리<br>+ batch 최대 24시간 + 후처리 |
| 간격 상한 | SLA − (전처리 + 24시간 + 후처리) |
| 계산 기준 | 최악의 경우를 합산<br>평소 처리 시간(1시간 이내) · 평균 ✗ |
| 예: SLA 30시간 | 상한 6시간 → 4시간 간격(28시간) ✓<br>8시간(32) · 12시간(36) · 24시간(48) → 초과 ✗ |
| 예: SLA 36시간<br>(전처리 2 · 후처리 2) | 상한 8시간 → 8시간 간격(36시간) ✓<br>12시간 간격 → 초과 ✗ |
| 건수 기준 전송<br>(N건 쌓일 때마다) | 접수 적은 시기 대기 상한 없음<br>→ SLA 보장 ✗ |
| 검증 실패분 | 후처리 시간 안에 동기 API로 개별 재처리 |
| 운영 팁 | 계산 상한보다 약간 짧은 간격<br>(단계별 지연 대비) |

**실패 request 재처리**

| 결과 유형 | 처리 |
|---|---|
| `expired` | 24시간 내 모델 미전송 · 과금 ✗<br>→ 내용 그대로 재전송 |
| `errored` + `invalid_request_error`<br>(예: 문서가 context 상한 초과) | 요청 본문 문제 · 과금 ✗<br>→ 수정(예: chunk 분할) 후 재전송<br>같은 요청 그대로 재투입 ✗ |
| 결과 유형 4종 | `succeeded` · `errored`<br>· `canceled` · `expired` |
| 판단 기준 | "같은 내용으로 다시 보내면 성공하는가" |
| 재전송 대상 | 실패한 `custom_id`만 |
| 대상 식별 · 결과 대응 | `custom_id`<br>(제출 순서 ✗) |
| 운영 팁 | 야간 job에서 유형별 집계<br>→ 실패 `custom_id`만 재전송 |

**tool · 반복 workflow와 batch**

| 구분 | 내용 |
|---|---|
| 처리 모델 | fire-and-forget 비동기<br>요청마다 독립 처리 |
| 핵심 제약 | 요청 도중 tool 실행 · 결과 반환 ✗<br>→ 반복 tool 호출 workflow와 불일치 |
| tool 정의 | batch 요청에 포함 가능<br>(tool use 지원) |
| client tool<br>(직접 구현) | Claude가 호출 요청 반환<br>→ 앱이 실행 → 후속 Messages 요청으로 결과 전달 |
| server tool | batch 안에서 실행까지 완결 |
| 실행 주체 | 동기 · batch 동일 |
| 설계 | batch = 초기 분석 · tool 요청까지<br>→ 후속 요청으로 각 case 계속 |
| 작성 → 실행 → 수정 반복<br>(예: 야간 테스트 생성) | 반복 = 동기 유지<br>한 응답으로 끝나는 입력 완비 부분만 batch |
| 요청 간 참조 | 이전 요청 결과 참조 ✗<br>(`custom_id` 연번으로도 불가) |
| 운영 팁 | batch로 test 안 생성<br>→ 다음 날 동기 job에서 실행 → 실패분만 수정 |

**batch 적용 판단 · 결과 대응**

| 상황 | 판단 |
|---|---|
| 실시간 chat 비용 절반 목적으로 batch 이전 | 반려 · 지연 보장 ✗<br>(대부분 1시간 내 · 최대 24시간) |
| 실시간 chat 비용 절감 대안 | prompt caching<br>일상 메시지를 저렴한 tier로 라우팅 |
| batch 요청 매개변수 | 일반 Messages 요청과 동일<br>(system prompt 가능) |
| polling 간격 단축 | 처리 속도 불변 |
| 한 모듈 결과에 다른 모듈 내용 | 개별 내용은 정확 · 대응만 어긋남<br>원인 = 결과 행 순서로 할당<br>→ `custom_id`로 할당 |
| 캐시 혼입 · 요청 병합 | batch 메커니즘에 없는 현상 |
| `custom_id` 값 | 의미 있는 식별자<br>(모듈명 · 청구서 번호)<br>→ 대조 · 재전송 · 조사 용이 |

<sub>근거: CCAR-F-MyPractice-0018, CCAR-F-MyPractice-0019, CCAR-F-MyPractice-0021, CCAR-F-MyPractice-0030, CCAR-F-Udemy02-0023, CCAR-F-Udemy02-0034, CCAR-F-Udemy04-0040, CCAR-F-Udemy04-0056, CCAR-F-Udemy05-0021, CCAR-F-Udemy05-0053, CCAR-F-Udemy06-0049, CCAR-F-paullarionov-0018, CCAR-F-paullarionov-0019, CCAR-F-paullarionov-0021, CCAR-F-paullarionov-0030, CCAR-F-preporato-0027</sub>

@@ ADD-TO: ### 1.8 구조화 출력 (Structured outputs)

**방식 선택 · 보장 범위**

| 구분 | 내용 |
|---|---|
| 첫 분기 | downstream이 받는 것<br>최종 응답 → `output_config.format`<br>tool 호출 → strict tool use |
| 보장 방식 | 두 계통 모두 schema 준수를 메커니즘으로 제약<br>prompt 유도 ✗ |
| 최종 응답이 인계물<br>(예: escalation packet) | `output_config.format`으로 packet 생성<br>→ 큐 투입 전 같은 JSON Schema로 검증<br>→ 부적합 시 반려 |
| 투입 전 검증 이유 | `max_tokens` 중단 · `refusal`<br>→ schema 불일치 가능 |
| 수신자 이력 미수신 | packet 안에 필요한 필드 완결<br>(식별자 · 추정 원인 · 다음 action) |
| 보장 대상 | 형식: 유효 JSON · schema 구조 · 타입<br>(constrained decoding) |
| 보장 밖: 값 | 원문과 값 일치 ✗ |
| 보장 밖: 의미 | 합계 · 날짜 같은 비즈니스 규칙<br>→ 검증은 pipeline에 유지 |
| 요청 방식 | `output_config.format`<br>`tool_choice` 강제와 무관 |

**텍스트 JSON 파싱 실패 → 구조화 전환**

| 구분 | 내용 |
|---|---|
| 증상 | JSON 앞뒤 설명문 · 필수 키 누락<br>→ 저장 전 파싱 실패 |
| 원인 | "JSON만" 지시 = 부탁<br>보장 메커니즘 ✗ |
| 해법 1 | JSON Schema를 `output_config.format`에 지정<br>→ 응답 자체 제약 |
| 해법 2 | `input_schema` + `strict: true` tool<br>+ `tool_choice` 강제<br>→ `tool_use` 블록의 `input` 객체 읽기 |
| tool 경로 조건 | 호출 강제 필요<br>(`auto` = tool 미호출 가능) |
| 선택지 판별 | 출력을 "부탁"하는가 · 메커니즘으로 "제약"하는가 |
| ⚠️ 모델 · 시점 의존<br>(해설 보충) | 해설: 일부 모델(예: Opus 5.5)<br>`any` · `tool` 강제 → 400<br>대안 = `auto` + `strict: true` tool<br>· structured outputs<br>2026년 9월 업데이트 · 시험 가이드(2026년 7월판)보다 새로움<br>→ 시험은 강제 가능 전제로 출제될 수 있음 |

<sub>근거: CCAR-F-Udemy01-0047, CCAR-F-Udemy03-0017, CCAR-F-Udemy03-0044, CCAR-F-preporato-0025</sub>

@@ NEW-SECTION
### tool_choice 모드와 추출 tool 강제
**`any` = 호출 보장 · 특정 tool 보장은 `tool`**

| 모드 | 보장 | 한계 |
|---|---|---|
| `auto` | 호출 여부는 모델 판단 | tool 없이 텍스트만 반환 가능<br>→ 구조화 출력 누락 |
| `any` | 제공 tool 중 하나 반드시 호출 | 어느 tool인지 보장 ✗<br>호출 순서 보장 ✗ |
| `{"type": "tool", "name": ...}` | 지정 tool 반드시 호출 | 문서 종류 불명이면 사용 ✗ |

| 상황 | 정답 |
|---|---|
| `auto`에서 일부 요청이 텍스트만 반환<br>+ 문서 종류 불명 · 추출 schema 여러 개 | `tool_choice: {"type": "any"}`<br>+ 각 tool description에 고유 기재 항목<br>· 타 종류와 구별법 |
| `any`인데 조회 tool이 추출보다 먼저 호출 | `any`는 순서 보장 ✗<br>→ 첫 요청에 `tool` 지정 강제 |
| enrichment 전에 특정 추출 확실히 실행 | 첫 요청만 추출 tool 강제<br>이후 turn은 `tool_choice` 되돌려 조회 진행 |
| `any` 이후 종류 혼동 | 선택은 description이 좌우<br>→ 선택 tool과 실제 종류를 표본 확인 |
| 강제 미지원 모델 | `auto` + `strict: true` tool<br>또는 structured outputs |
| ⚠️ 모델 · 시점 의존<br>(해설 보충) | 해설: 2026년 9월 이후 일부 모델<br>`any` · `tool` 강제 → 400<br>시험 가이드(2026년 7월판)보다 새로움<br>→ 시험은 강제 가능 전제로 출제될 수 있음 |

<sub>근거: CCAR-F-Udemy03-0017, CCAR-F-Udemy03-0044, CCAR-F-Udemy06-0005, CCAR-F-Udemy06-0053</sub>

@@ RULES

| 상황 | 정답 |
|---|---|
| 한 시스템에 blocking 작업(PR merge 차단)<br>과 야간 · 주간 작업 혼재 | 작업별 API 분리<br>blocking = 동기 · 일정 작업 = batch |
| 작업자 · 고객이 화면 앞에서 대기 | 동기 호출<br>(사내 · 사외 구분 무관) |
| 지연 SLA T시간 · batch 전송 주기 결정 | 간격 ≤ T − (전처리 + 24시간 + 후처리)<br>최대 24시간 기준 · 건수 기준 전송 ✗ |
| batch 결과 중 `expired` | 내용 그대로 새 batch로 재전송 |
| batch 결과 중<br>`errored` + `invalid_request_error` | 요청 수정(예: chunk 분할) 후 재전송<br>실패 `custom_id`만 대상 |
| 반복 tool 실행(작성 → 실행 → 수정)의 비용 절감 | 반복은 동기 유지<br>한 응답으로 끝나는 부분만 batch |
| batch 안에서 client tool 필요 | batch에서 tool 요청까지 수신<br>→ 앱이 실행 → 후속 Messages 요청으로 계속 |
| 실시간 chat 비용 절감 | prompt caching · 저렴한 tier 라우팅<br>batch ✗ |
| JSON 텍스트 파싱 실패<br>(앞뒤 설명문 · 필수 키 누락) | `output_config.format`<br>또는 strict tool + `tool_choice` 강제 |
| 수신 큐가 최종 응답을 요구 | `output_config.format` + 투입 전 schema 검증 |
| 추출 값의 합계 · 날짜 일관성 | 비즈니스 규칙 검증을 pipeline에 유지 |
| 문서 종류 불명 + 추출 tool 여러 개 | `tool_choice: any` + description 보강 |
| 특정 추출을 후속 단계보다 먼저 보장 | 첫 요청에 `tool` 이름 지정 강제 |

<sub>근거: CCAR-F-MyPractice-0018, CCAR-F-MyPractice-0019, CCAR-F-MyPractice-0021, CCAR-F-MyPractice-0030, CCAR-F-Udemy01-0047, CCAR-F-Udemy02-0023, CCAR-F-Udemy02-0034, CCAR-F-Udemy03-0017, CCAR-F-Udemy03-0044, CCAR-F-Udemy04-0040, CCAR-F-Udemy04-0056, CCAR-F-Udemy05-0021, CCAR-F-Udemy05-0053, CCAR-F-Udemy06-0005, CCAR-F-Udemy06-0049, CCAR-F-Udemy06-0053, CCAR-F-paullarionov-0018, CCAR-F-paullarionov-0019, CCAR-F-paullarionov-0021, CCAR-F-paullarionov-0030, CCAR-F-preporato-0025, CCAR-F-preporato-0027</sub>

@@ TRAPS

| 오답 | 이유 |
|---|---|
| batch에 출력 ↔ 입력 연결 ID 없음 | `custom_id`로 연결 |
| Batch API는 요청에 tool 정의 불가 | 정의 포함 가능<br>제약 = 요청 도중 실행 · 결과 반환 ✗ |
| batch 지연이 유일한 문제 · workflow 자체는 동작 | 핵심 제약 = 도중 tool 결과 반환 불가 |
| 세 작업 모두 batch + polling | blocking 검사까지 최대 24시간 지연 |
| 세 작업 모두 동기 + caching | 마감 여유 작업의 batch 50% 절감 포기 |
| 야간 테스트 생성은 동기 유지 | 마감 여유 작업 = batch 대상 |
| 두 workflow 모두 batch + 지연 시 동기 대체 | blocking 검사는 batch 대상 아님<br>지연 SLA 없음 |
| batch 결과 순서 걱정 → 동기 고집 | `custom_id`로 대응 가능 |
| 사내 작업자 대기 작업은 batch 가능 | 기준 = 기다리는 사람 유무<br>사내 · 사외 구분 무관 |
| 실시간 chat에 batch(품질 동일 · 가격 절반) | 지연 보장 ✗ |
| batch 1초 polling으로 실시간 응대 | 처리 속도 불변 |
| batch 요청에 system prompt 불가 | 일반 Messages 매개변수와 동일 |
| 결과 파일 행 순서로 레코드 할당 | 순서 보장 ✗ → 내용 뒤바뀜 |
| 캐시 공유 · 요청 병합 탓 | batch 메커니즘에 없는 현상 |
| 전송 간격을 평소(1시간 이내) 처리 시간 기준 계산 | 기준 = 최대 24시간 |
| 접수 N건마다 전송 | 접수 적은 시기 대기 상한 없음 |
| 12시간 간격(SLA 36시간 · 전처리 · 후처리 2시간씩) | 전 · 후처리 4시간 누락 → 40시간 |
| `errored`(`invalid_request_error`)를<br>서버 일시 오류로 보고 그대로 재투입 | 요청 본문 문제 → 수정 필요 |
| 전체 재전송 + 제출 순서로 원본 매칭 | 실패 `custom_id`만 재전송<br>순서 매칭 ✗ |
| `custom_id` 연번으로 이전 요청 결과 참조 | 요청 간 참조 ✗ · 독립 처리 |
| batch 각 요청에 Bash tool 정의 후 처리 중 실행 | 요청 도중 실행 ✗ |
| batch worker가 client tool 실행<br>· 자체 tool을 server tool로 취급 | client tool 실행 주체 = 앱 |
| structured outputs = 값이 원문과 일치 보장 | 보장 대상 = 형식 |
| structured outputs 사용 → 합계 · 날짜 검증 불필요 | 의미 검증은 pipeline 몫 |
| structured outputs는 `tool_choice` 강제 때만 작동 | `output_config.format` 요청과 별개 |
| 지시 강화 · schema XML tag 감싸기<br>· 산문 응답 폐기 후 재생성 | 부탁일 뿐 · 보장 메커니즘 ✗ |
| tool 등록 + `tool_choice: auto`로 사용 여부 위임 | tool 미호출 가능 |
| schema를 `CLAUDE.md`에 저장<br>· `tool_result` 이후 텍스트 파싱 | 둘 다 텍스트 의존 |
| prefill `{` + 첫 balanced object 파싱<br>⚠️ 해설: prefill은 Claude 4.6 세대 이후 모델에서 불가 | 텍스트 의존<br>⚠️ 모델 버전 의존(시점에 따라 바뀜) |
| escalation packet을 tool 호출 인자로 인계 | "최종 응답" 조건 위반 |
| 생 발췌 + 대화 이력 인계 → 수신자가 재구성 | 수신자는 대화 · tool 이력 미수신 |
| `any`로 추출 tool 순서 보장 | 어느 tool이든 호출만 보장 |
| 문서 종류 불명인데 특정 tool 강제<br>(예: 건수 많은 종류) | 다른 종류도 해당 schema로 추출 |
| `auto` + system prompt<br>· description 보강으로 순서 보장 | 확률적 방법 |
| 조회 결과 비면 추출부터 재실행 | 오류 검출 전제의 사후 대응 |
| 텍스트 응답을 정규식으로 판정 → tool 재실행 | API 설정 대신 앱의 깨지기 쉬운 보완 |

<sub>근거: CCAR-F-MyPractice-0018, CCAR-F-MyPractice-0019, CCAR-F-MyPractice-0021, CCAR-F-MyPractice-0030, CCAR-F-Udemy01-0047, CCAR-F-Udemy02-0023, CCAR-F-Udemy02-0034, CCAR-F-Udemy03-0017, CCAR-F-Udemy03-0044, CCAR-F-Udemy04-0040, CCAR-F-Udemy04-0056, CCAR-F-Udemy05-0021, CCAR-F-Udemy05-0053, CCAR-F-Udemy06-0005, CCAR-F-Udemy06-0049, CCAR-F-Udemy06-0053, CCAR-F-paullarionov-0018, CCAR-F-paullarionov-0019, CCAR-F-paullarionov-0021, CCAR-F-paullarionov-0030, CCAR-F-preporato-0025, CCAR-F-preporato-0027</sub>

@@ MEMO

| 이름 | 의미 |
|---|---|
| `succeeded` · `errored`<br>· `canceled` · `expired` | batch request 결과 유형 4종 |
| `expired` | 24시간 내 모델 미전송<br>과금 ✗ · 내용 그대로 재전송 |
| `errored` + `invalid_request_error` | batch 요청 본문 문제<br>과금 ✗ · 수정 후 재전송 |
| 간격 상한 = SLA − (전처리 + 24시간 + 후처리) | batch 전송 주기 계산<br>예: SLA 30시간 → 6시간 이하 |
| `tool_choice` `auto` | 호출 여부 모델 판단 · tool 미호출 가능 |
| `tool_choice` `any` | 제공 tool 중 하나 호출<br>어느 tool인지 보장 ✗ |
| `tool_choice`<br>`{"type": "tool", "name": ...}` | 지정 tool 호출 강제 |
| `tool_use` 블록의 `input` | tool 경로 구조화 추출 결과 객체 |
| `input_schema` | tool 입력 schema<br>`strict: true`와 함께 준수 보장 |

<sub>근거: CCAR-F-Udemy01-0047, CCAR-F-Udemy02-0023, CCAR-F-Udemy03-0017, CCAR-F-Udemy03-0044, CCAR-F-Udemy05-0053, CCAR-F-Udemy06-0005, CCAR-F-Udemy06-0049, CCAR-F-Udemy06-0053</sub>

@@ CHECK

- [ ] 사람이 결과 대기 → 동기 · 일정 작업 → batch
- [ ] batch 전송 간격 ≤ SLA − (전처리 + 24시간 + 후처리)
- [ ] batch 실패: `expired` → 그대로 재전송 · `errored` → 수정 후 재전송
- [ ] `any` = 아무 tool 호출 · 특정 tool 보장 = `tool` 지정

<sub>근거: CCAR-F-MyPractice-0019, CCAR-F-MyPractice-0030, CCAR-F-Udemy02-0023, CCAR-F-Udemy05-0053, CCAR-F-Udemy06-0005, CCAR-F-Udemy06-0049, CCAR-F-Udemy06-0053, CCAR-F-paullarionov-0019, CCAR-F-paullarionov-0030</sub>
