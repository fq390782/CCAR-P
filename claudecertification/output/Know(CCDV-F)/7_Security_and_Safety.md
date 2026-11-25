# 7. Security and Safety — 반드시 알아야 할 지식
> 시험 비중 8% · 약 3문항 · 근거 문항 17개

## 1. 핵심 개념

### 1.1 Prompt injection: 방어는 구조적으로
**injection 방어 = 분리 + 권한 제한 (모델 바깥)**

| 구분 | 내용 |
|---|---|
| untrusted input | 웹 페이지 · 검색 결과 · fetch 문서 · 사용자 제출 콘텐츠<br>→ 지시 ✗, 데이터로 취급 |
| hidden text 지시 | 동일하게 untrusted 데이터<br>예: 대화 기록 외부 전송 · system prompt 공개 |
| 설계 전제 | 모델은 가끔 주입된 지시를 따름<br>→ 실제 통제 = 모델 바깥의 권한 제한<br>모델 순응 기대 ✗ |

| 공식 | 내용 |
|---|---|
| 분리 | untrusted content와 instructions 분리 |
| 권한 | 위험 capability 미부여 (least privilege)<br>→ 주입 지시가 실행할 tool 없음 → 공격 실패<br>예: fetch · 요약 agent → `send_email` · `delete_file` · refund 불필요 |
| 승인 | 결과가 큰 행동 → guardrail · 사람 승인 뒤 |

| 오답 | 이유 |
|---|---|
| "악성 지시 무시" 한 줄만으로 "해결" 판단 | 도움 가능하나 probabilistic<br>enforcement · 보장 ✗ |

![Prompt injection 공격 경로와 모델 바깥의 구조적 방어](svg/7-injection-defense.svg)
*그림: untrusted content의 지시를 모델이 따르더라도, 위험 tool이 없거나 승인 게이트가 있으면 공격은 실패한다*

<sub>근거: Amey-0008, Amey-0033, Amey-0042, Amey-0047, Amey-0064, Patrick-0013, Patrick-0024, Preporato-0026</sub>

### 1.2 Untrusted 입력 삽입
**사용자 입력 = XML tag로 감싼 데이터**

| 방법 | 판정 | 이유 |
|---|---|---|
| XML tag(`<user_query>` 등)로 감싸기<br>+ system prompt: tag 안 = 데이터, 지시 ✗ 선언 | ✓ | 지시 · 입력 경계 설계 |
| + least privilege · 모델 바깥 enforcement | ✓ | 경계 설계 위에 겹침<br>(1.1과 상충 ✗) |
| 직접 연결<br>(구분자 없이 지시문 중간에 이어 붙임) | ✗ | 지시 · 입력 경계 소멸<br>→ prompt injection 입구 |
| 기호 제거 | ✗ | 효과 = 기호가 문법 의미를 갖는 경우만(SQL · HTML 등)<br>자연어 injection = 문자만으로 작성 → 차단 ✗<br>정상 정보 훼손(화학물질명 · 모델 번호의 기호) |
| 다른 모델로 요약 · 재작성 | ✗ | 세부 정보 손실<br>요약 모델 자신도 injection 영향 가능<br>구조적 분리 대체 ✗ |

![직접 연결과 XML tag 경계 비교](svg/7-xml-tag-wrapping.svg)
*그림: 입력을 XML tag로 감싸고 '데이터'라고 선언해야 경계가 생기며, 기호 제거나 요약은 대안이 아니다*

<sub>근거: Amey-0033, Udemy-0049</sub>

### 1.3 Least privilege와 tool 설계
**금지는 prompt가 아니라 권한으로 강제**

| 구분 | 내용 |
|---|---|
| integration 노출 범위 | 작업에 필요한 operation만<br>건드려도 되는 범위로 축소<br>→ 실수 · 조작 시 피해 범위 제한 |
| 금지 강제 수단 | tool 구성 · hooks<br>executor 내 authorization<br>(prompt ✗) |
| "절대 하면 안 되는 행동" | 해당 tool 미부여로 보장 |
| 외부로 데이터 전송 | 코드 안의 deterministic gate로 차단 · 보류 |

| 오답 | 이유 |
|---|---|
| full credentials + "쓰기 금지" 지시<br>read · write 권한 그대로 부여 | 통제 ✗ → 모델 행동에 의존 |
| schema 없는 범용 tool | "유연함" ✗ → 경계 제거 |

![행동에 기대는 권한 부여와 모델 바깥 강제 비교](svg/7-least-privilege.svg)
*그림: 금지는 prompt가 아니라 tool 구성·hooks·executor authorization과 deterministic gate로 강제한다*

<sub>근거: Amey-0034, Amey-0042, Patrick-0024, Preporato-0026</sub>

### 1.4 Human-in-the-loop (approval gate)
**막을 행동은 미부여 · 위험 행동은 승인**

| 상황 | 조치 |
|---|---|
| consequential · irreversible<br>· destructive tool | human approval gate 뒤에 배치<br>→ least privilege를 빠져나간 것 포착 |
| 꼭 막아야 하는 행동 | tool 미부여 (승인보다 우선) |

| 오답 | 이유 |
|---|---|
| 모델에 "환불 전 확인" 지시 | enforcement ✗ |

![human approval gate 판단 흐름](svg/7-approval-gate.svg)
*그림: 꼭 막을 행동은 tool을 주지 않고, consequential 행동만 사람 승인 뒤에 실행한다*

<sub>근거: Amey-0042, Patrick-0013, Patrick-0024, Preporato-0026</sub>

### 1.5 Authorization 전파
**tool 실행 = 호출 사용자의 검증된 token 기준**

| 방식 | 판정 | 이유 |
|---|---|---|
| 강한 권한의 공유 service account 하나로 전 사용자 처리 | ✗ | 사용자별 authorization · audit trail 소멸<br>→ 모델 = 강한 권한 대리인<br>→ 타인 데이터 조회 가능 |
| 호출 사용자의 identity · 권한으로 실행<br>+ tool 호출마다 사용자 기준 log | ✓ | 근본 해결 |
| MCP: 앱이 로그인 사용자의 검증된 token을 요청에 첨부<br>→ server가 매번 접근 범위 판정 | ✓ | 사용자 식별 = 검증된 token<br>(client · 모델이 넘긴 값 ✗) |
| 대상 사용자 ID를 모델이 tool argument로 전달 | ✗ | 원래와 같은 결함<br>argument 값 = 모델이 결정<br>→ 대화로 유도 시 타인 ID 삽입 가능 |
| 출력 검사만으로 대체<br>(다른 모델로 이름 확인) | ✗ | 보조 수단일 뿐<br>authorization 대체 ✗<br>권한 밖 데이터는 이미 모델이 읽은 상태 |

![공유 service account, 모델이 넘기는 ID, 검증된 token 비교](svg/7-authorization-propagation.svg)
*그림: 사용자 식별은 검증된 token에서 얻고 server가 요청마다 권한을 판정해야 한다*

<sub>근거: Preporato-0028, Udemy-0041</sub>

### 1.6 API key / secret 관리
**노출 key → rotate · 서버 보관**

| 상황 | 조치 |
|---|---|
| browser JavaScript에 key | 클라이언트 전송분 → 사용자 열람 가능<br>→ key rotate + key를 가진 backend로 호출 이전 |
| repository · system prompt template 속 key | 이미 노출<br>→ rotate 후 env var · secret manager 보관 |
| credential 사용 위치 | tool 실행 코드의 인증 시만<br>모델 context(prompt) 투입 ✗<br>→ 모델은 credential 미열람 |

| 오답 | 이유 |
|---|---|
| 난독화(obfuscation) · local storage<br>클라이언트 코드 내 IP 제한 | key가 여전히 클라이언트에 있음<br>또는 우회 가능 |
| Base64 인코딩 | 즉시 복원 가능 |
| "key 공개 금지" 지시 | probabilistic |
| key를 prompt 끝으로 이동 | 여전히 prompt 안 |

![API key 관리 흐름](svg/7-secret-management.svg)
*그림: 노출된 key는 rotate하고 서버 쪽 secret manager에 두며, tool 코드만 인증에 쓰고 모델은 credential을 보지 않는다*

<sub>근거: Patrick-0043, Preporato-0027</sub>

### 1.7 PII 보호: 데이터 최소화
**PII 보호 = 유출 확산 범위 최소화**

| 구분 | 내용 |
|---|---|
| 기본 원칙 | data minimization + least privilege<br>"모델에 보여 주는 것" · "모델이 접근 가능한 것" 모두 최소 |
| 방법: 전달 | 작업에 필요한 항목만 전달<br>직접 식별자(이름 등) → 전송 전 masking · tokenization(임시 ID) |
| 방법: 접근 · 기록 | tool 접근 범위 = 담당 대상 한정<br>log · URL에 PII 미기록 |
| audit log | 정당한 운영<br>이름 든 전문 그대로 저장 → 유출 경로 증가<br>→ masking 또는 항목 한정 필요 |
| TLS · 저장 시 암호화 | 전송 경로 · 보관 보호 |
| 판단 기준 | "유출되면 어디까지 퍼지는가"<br>→ 범위가 가장 작은 선택지 |

| 오답 | 이유 |
|---|---|
| 전체 사용자 기록을 system prompt에 상주 | injection 1회 · 잘못된 출력 1회<br>→ 담당 밖 정보까지 유출 가능 |
| TLS · 저장 시 암호화로 최소화 대체 | 모델 출력 · injection을 통한<br>유출 위험 감소 ✗ |

![PII 최소화 dataflow](svg/7-pii-minimization.svg)
*그림: 필요한 항목만 masking해 넘기고 tool 범위를 좁혀, 유출 시 퍼지는 범위를 최소로 만든다*

<sub>근거: Udemy-0039</sub>

### 1.8 출력 처리 (output handling)
**모델 출력 = untrusted → 렌더링 전 escape**

| 방법 | 판정 | 이유 |
|---|---|---|
| 모델 출력 → web page 렌더링 전 반드시 escape · sanitize | ✓ | untrusted (입력의 영향 가능)<br>출처 무관 |
| "markup 생성 금지" 지시 | ✗ | 통제 ✗ |

![모델 출력 처리 흐름](svg/7-output-handling.svg)
*그림: 모델 출력은 입력의 영향을 받는 untrusted 데이터이므로 렌더링 전에 escape/sanitize한다*

<sub>근거: Amey-0079</sub>

### 1.9 Guardrail 다층 방어 (defense in depth)
**guardrail = 사전 차단 층 + 사후 탐지 층**

| 구분 | 내용 |
|---|---|
| 원칙 | 어떤 대책도 단독으로는 빠져나갈 여지<br>→ 입력 · 지시 · 출력 · 운영 monitoring 각 단계에 층 중첩 |
| 공식 권장 조합: 입력 · 지시 | 경량 모델(Haiku 계열)의 harmlessness screen<br>알려진 공격 패턴 입력 검증<br>경계 · 거절 방식을 명시한 system prompt |
| 공식 권장 조합: 운영 · 출력 | 반복 위반자 대응<br>출력 filter + 지속적 monitoring |
| 출시 전 red teaming | 중요하나 단독 부족<br>→ 가동 후 새 표현 · 수법 등장 |
| 규제 업종(금융 등) | 사전 차단 층 · 사후 탐지 층 모두 존재 여부 확인 |
| prompt 강화 · 출력 검사 | 다층 방어의 한 층으로 가치<br>단독 = probabilistic 대책 |

![guardrail 다층 방어 구조](svg/7-defense-in-depth.svg)
*그림: 입력·지시·출력의 사전 차단 층과 monitoring 사후 탐지 층을 겹쳐 빠져나간 공격을 잡는다*

<sub>근거: Udemy-0041, Udemy-0050</sub>

## 2. 상황별 정답 판단 규칙

| 상황 | 정답 |
|---|---|
| fetch한 웹 페이지 · 문서에 "이전 지시를 무시하고 ~하라" | content = untrusted 데이터<br>권한은 모델 바깥에서 제한 |
| 요약 agent에 email · 삭제 · 환불 tool<br>+ injection 당함 | 해당 tool 제거 (least privilege)<br>남는 consequential tool → human approval 뒤 |
| "agent가 절대 X 금지" 보장 위치 | X tool 미부여<br>tool configuration · hooks로 강제 |
| 외부 주소로 데이터 전송 위험 (2개 선택) | 코드의 deterministic gate<br>+ least privilege (tool 제거 또는 승인) |
| integration에 DB 접근 부여 | 필요한 operation만, 범위 축소 노출 |
| 공유 service account로 타인 데이터 유출 | 호출 사용자의 identity · 권한으로 실행<br>사용자 기준 log |
| MCP tool이 전 데이터 읽기 가능, 제한은 prompt에만 | 로그인 사용자 token을 요청에 첨부<br>server 쪽 권한 판정 |
| browser JS에 API key | rotate + backend proxy로 이전 |
| repo · prompt template에 key | rotate 후 env var · secret manager<br>tool 코드가 인증 → 모델은 credential 미열람 |
| PII 포함 데이터를 Claude에 전달 | 필요한 항목만 · 직접 식별자 masking<br>tool 권한 축소 |
| 사용자 자유 기술 입력을 template에 삽입 | XML tag로 감싸기<br>system prompt에 "tag 안 = 데이터" 선언 |
| 모델 출력을 HTML에 렌더링 | untrusted 취급 → escape · sanitize |
| 규제 업종 chatbot의 견고한 guardrail | 입력 screen + system prompt 거절 방침<br>+ 출력 filter + monitoring 다층 |

![injection과 tool 통제 판단 트리](svg/7-decision-injection-tools.svg)
*그림: 외부 content의 지시와 위험 tool은 모델 바깥(tool 제거·hooks·gate·범위 축소)에서 통제한다*

![권한·secret·PII 판단 트리](svg/7-decision-identity-secrets.svg)
*그림: 권한은 사용자 token으로, key는 rotate 후 서버에, PII는 최소화·masking으로 다룬다*

![입력·출력·guardrail 판단 트리](svg/7-decision-io-guardrails.svg)
*그림: 입력은 XML tag로 감싸고, 출력은 escape하고, guardrail은 다층으로 쌓는다*

<sub>근거: Amey-0008, Amey-0033, Amey-0034, Amey-0042, Amey-0064, Amey-0079, Patrick-0013, Patrick-0024, Patrick-0043, Preporato-0026, Preporato-0027, Preporato-0028, Udemy-0039, Udemy-0041, Udemy-0049, Udemy-0050</sub>

## 3. 자주 나오는 오답 함정

| 오답 | 이유 |
|---|---|
| system prompt에 "악성 지시는 무시하라" | probabilistic · enforcement ✗<br>모델은 가끔 따름 |
| "ignore" 등 keyword · 알려진 phrase filter | 쉽게 우회(trivially evaded)<br>정당한 답변까지 차단 |
| 더 큰 모델 · instruction following 좋은 모델 | attack surface 동일 → 보안 통제 ✗ |
| temperature 낮추기 · 높이기<br>더 큰 context window | 보안과 무관 |
| 모델에 "실행 전 확인" 지시 | 모델 자체 확인 = enforcement ✗<br>→ tool 미부여 또는 사람 승인 필요 |
| full · read-write 권한 + "쓰기 회피" 지시 | 통제 ✗ → 행동에 의존 |
| 대상 ID를 모델이 tool argument로 전달해 범위 축소 | 값을 모델이 결정 → 유도 가능<br>→ 검증된 token 필요 |
| 출력 검사(별도 모델, 이름 탐지)만 배치 | 탐지 → authorization 대체 ✗<br>데이터는 이미 모델에 유입 |
| 민감 데이터 자체를 시스템에서 삭제 | 정당한 업무까지 손상 |
| API key 난독화 · Base64 · local storage<br>prompt 안 위치만 이동 | 여전히 노출 또는 즉시 복원 가능 |
| key를 rotate 없이 이동만 | 이미 노출된 key → rotate 필수 |
| TLS · 저장 시 암호화만 있으면 PII 최소화 불필요 | 출력 · injection 경유 유출 차단 ✗ |
| audit용 이름 든 전문 log | 유출 경로 증가 |
| 입력 기호 제거 · 다른 모델 요약으로 sanitize | 자연어 injection 차단 ✗<br>정보만 훼손 |
| "모델 출력은 안전" → 그대로 렌더링 | 출력은 입력 영향 → escape 필요 |
| guardrail 층 하나만<br>(입력 screen만, 사전 red teaming만) | 빠져나간 공격 포착 층 없음 |

<sub>근거: Amey-0008, Amey-0033, Amey-0034, Amey-0042, Amey-0047, Amey-0064, Amey-0079, Patrick-0013, Patrick-0024, Patrick-0043, Preporato-0026, Preporato-0027, Preporato-0028, Udemy-0039, Udemy-0041, Udemy-0049, Udemy-0050</sub>

## 4. 암기 목록

| 이름 | 의미 |
|---|---|
| Untrusted input | 웹 페이지 · fetch 문서 · 사용자 입력 · 모델 출력<br>→ 지시 ✗, 데이터로 취급 |
| Least privilege | 필요한 tool · operation만, 범위 축소 부여<br>→ 피해 범위 제한 |
| Human approval gate | consequential · irreversible<br>· destructive 행동 앞 사람 확인 |
| Deterministic gate | 위험 행동(외부 전송 등)을 코드로 차단 · 보류 |
| Hooks · tool configuration | 금지 capability를 prompt 아닌 설정으로 강제하는 수단 |
| Authorization 전파 | 호출 사용자의 identity · 권한(검증된 token)으로 tool 실행<br>사용자별 audit |
| Secret 보관 | env var · secret manager<br>노출 시 rotate<br>tool 코드가 인증 |
| Data minimization | 필요한 항목만 전달<br>직접 식별자 masking · tokenization |
| XML tag 분리 | 사용자 입력을 `<user_query>` 등으로 감싸고 "데이터" 선언 |
| Output escaping | 렌더링 전 escape · sanitize |
| Harmlessness screen | 경량 모델로 입력을 사전 심사하는 guardrail 층 |
| Defense in depth | 입력 screen · system prompt ·<br>출력 filter · monitoring 중첩 |

<sub>근거: Amey-0033, Amey-0034, Amey-0042, Amey-0079, Patrick-0024, Patrick-0043, Preporato-0026, Preporato-0027, Preporato-0028, Udemy-0039, Udemy-0041, Udemy-0049, Udemy-0050</sub>

## 5. 시험 직전 체크리스트

- [ ] 외부 content(웹 · 문서 · 사용자 입력) = 항상 untrusted
- [ ] injection 방어 = 데이터/지시 분리 + least privilege + 모델 바깥 enforcement
- [ ] "무시하라" system prompt 단독 ✗
- [ ] keyword filter · 더 큰 모델 → 보안 통제 ✗
- [ ] temperature · context window → 보안 통제 ✗
- [ ] "절대 안 됨" → tool 미부여 (hooks · configuration)
- [ ] consequential · destructive tool → approval gate 뒤
- [ ] tool 실행 = 호출 사용자 권한(검증된 token)
- [ ] 공유 service account · 모델이 넘기는 ID argument ✗
- [ ] 노출 key → rotate + backend · secret manager
- [ ] API key를 모델 context에 넣기 ✗
- [ ] PII → 최소화 + masking
- [ ] 암호화 → 최소화 대체 ✗
- [ ] 사용자 입력 → XML tag로 감싸고 "데이터" 선언
- [ ] 모델 출력 → 렌더링 전 escape · sanitize
- [ ] guardrail 다층: 입력 screen + system prompt + 출력 filter + monitoring
