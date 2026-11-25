# 6. Prompt and Context Engineering — 반드시 알아야 할 지식
> 시험 비중 11% · 약 3문항 · 근거 문항 23개

> 커버: CCDV-F D6 · CCAR-F D4·D5(일부) · CCAR-P D2(일부)

## 1. 핵심 개념

### 1.1 System prompt vs user message 역할 분리
**안정적 지침 = system · 가변 입력 = user**

| 구분 | 내용 |
|---|---|
| system prompt | 모든 턴에 일관 적용할 안정적 지침<br>(role · 행동 규칙 · 안전 제약) |
| user message | 매번 바뀌는 사용자 질문 · 참조 데이터 |
| API 구조 | `system` = top-level 파라미터, 대화 전체의 전제<br>`messages`의 user 턴 = 개별 요청 |
| role 설정 | 행동 · 어조가 용도에 맞게 안정 |
| 항상 참조할 배경 정보 | system prompt에 배치 (일반적)<br>(운영 규칙 요점 등) |

| 배치 | 결과 |
|---|---|
| 지침을 user 턴에 ✗<br>(첫 · 마지막 · 매 메시지 반복) | configuration · input 혼재 → drift<br>입력 문구로 지침 약화 · 덮어쓰기 가능<br>유지보수 어려움 |
| system prompt 불가 환경에서 user message에 지시 | 동작함 · Claude 대체로 준수<br>원칙 ✗ |
| 사용자별 질문까지 system prompt에 ✗ | 신뢰할 수 없는 입력을 지침과 같은 권위로 처리 |
| 행동 지침을 tool description에 ✗ | tool description = tool 선택용<br>매 턴 적용할 행동 지침 자리 아님 |

| 구분 | 내용 |
|---|---|
| 지속 행동 지침<br>(어조 · 추론 설명 · clarification 질문) | system prompt에 정의<br>대화 전체에 적용되는 지속 제약용으로 설계 |
| 지침을 매 user message에 첨부 ✗ | 불필요한 overhead |
| 지침을 첫 assistant 메시지에 ✗ | 모델이 이전 진술에서 벗어날 수 있음<br>→ 신뢰 ✗ |
| 지침을 환경 변수에 ✗ | 모델 동작에 영향 없음 |
| system prompt에 넣을 내용 | 행동을 바꾸는 정보(역할 · 규칙 · 형식)<br>규칙("정책에서만 답한다") → 정확성<br>형식 지정 → 일관성 |
| system prompt에 넣지 않을 내용 | 답변에 영향 없는 회사 배경 → token만 소비<br>농담조 persona → 신뢰 · 일관성 저하 |
| 자주 바뀌는 정책 본문 | retrieval 컨텍스트에 배치<br>system prompt에 고정 삽입 ✗<br>⚠️ 변하는 정책 한정 · "캐시 낭비"는 해설 주장 |
| 규칙이 매달 바뀌는 검수 | prompt의 서면 규칙 · 예시 = 통제 수단<br>→ 텍스트 수정만 · 새 학습 데이터 불필요 |
| 판정 결과를 JSON schema로 제약 | 각 판정 파싱 가능 유지 |
| 지시 · 데이터 · 출력 형식이 한 문장에 혼재 | 첫 개선 = 구조 부여<br>→ 모델이 지시와 데이터를 구별 |

**대화 중 실시간 이벤트(webhook) 주입**

| 방법 | 판정 | 이유 |
|---|---|---|
| 다음 user message 앞에 상태 업데이트 prefix | ✓ | 자연스러운 대화 경계에서 실시간 context 주입<br>대화 흐름 유지 |
| 상태를 system prompt에 추가 | ✗ | session 재구성 필요<br>architecture상 번거로움 |
| 즉시 합성 user message 전송 | ✗ | 자연스러운 대화 흐름 단절<br>attribution 혼란 |
| 매 턴 상태 tool 호출 강제 | ✗ | 이벤트가 드문 경우 낭비 |



![system prompt와 user message에 각각 무엇을 두는지와 잘못된 배치 세 가지](svg/6-system-vs-user.svg)
*그림: 안정적 지침은 top-level system에, 매번 바뀌는 입력은 user 턴에 두며, 이를 뒤섞으면 drift나 권위 혼동이 생긴다.*

<sub>근거: Amey-0028, Amey-0061, CCAR-F-Amey-Thakur-0027, CCAR-F-MyPractice-0071, CCAR-F-MyPractice-0073, CCAR-P-jrajath94-0054, CCAR-P-jrajath94-0683, Udemy-0012</sub>

### 1.2 인터페이스마다 다른 컨텍스트
**결과 차이 = 지시문 바깥 컨텍스트 차이**

| 인터페이스 | 모델이 받는 컨텍스트 |
|---|---|
| 공통 | 지시문 · 주변 컨텍스트 전체 |
| claude.ai / 모바일 앱 | 자체 system prompt(현재 날짜 · 응답 스타일 등)<br>API에는 미적용 |
| Claude Code | tool 정의 · `CLAUDE.md`<br>auto memory · 세션 상태 등 추가 |
| Messages API | `system` · `messages`를 개발자가 직접 조립 |

| 판단 | 내용 |
|---|---|
| 프로덕션 | 일관된 동작 필요 → API/SDK 위에 구축<br>실제 제공 환경에서 평가 |
| 인터페이스별 결과 차이 | 버그 ✗<br>설계상 차이<br>세 인터페이스가 같은 system prompt로 동작 ✗ |
| 지시문만 수정 ✗ | 지시문 바깥 컨텍스트 차이 잔존 |

![같은 지시문에 claude.ai, Claude Code, Messages API가 각각 다른 컨텍스트를 붙이는 흐름](svg/6-interface-context.svg)
*그림: 인터페이스별 결과 차이는 지시문 바깥에 붙는 컨텍스트 차이에서 오므로, 프로덕션은 API/SDK로 만들고 실제 환경에서 평가한다.*

<sub>근거: Udemy-0015</sub>

### 1.3 Few-shot 예시 (multishot)
**few-shot = 형식 고정용 · 소수 · 다양 · 무모순**

| 구분 | 내용 |
|---|---|
| 적합 상황 | 출력 형식 · edge-case 처리 불일치<br>예시로 목표 동작 제시 가능 |
| 효과 | 형식 · edge-case 동작<br>→ 지시 추가보다 예시가 훨씬 잘 고정 |
| 부적합 | 사실 지식 보충 ✗ · latency 감소 ✗<br>작은 context window 해결 ✗<br>(예시 = token 소비) |
| 여러 제약 동시 준수 | 규칙을 지킨 출력 예시(worked example)<br>→ 제약 간 상호작용까지 제시 · 산문 설명으로는 불가 |
| 지시 vs 예시 모순 | 정해진 우선순위 없음<br>→ 두 쪽 사이 동작 예측 불가 |
| 모순 시 흔한 오해 | 지시가 항상 이김 ✗ · 예시가 항상 이김 ✗<br>요청 거부 ✗ |
| robustness 테스트용 모순 예시 ✗ | 모델이 지시를 무시하도록 학습 |

| 권장 구성 | 내용 |
|---|---|
| relevant | 실제 용도와 가까운 예시 |
| diverse | 경계 사례까지 포함 |
| 개수 | 소수 3~5개 (문항에 따라 2~4개) |
| 분리 | `<example>` 태그로 지시 · 실제 입력과 분리 |
| 까다로운 classification | reject할 negative case 포함<br>→ 경계 학습 |
| 질 > 개수 | 선별 없는 수십 개 → 편향 · 잘못된 예시의 의도치 않은 패턴 학습<br>컨텍스트 점유 |
| 좁은 예시 ✗ | 모두 같은 label · 거의 같은 예시 50개<br>→ 좁은 패턴만 학습 |

| 예시 선택 | 내용 |
|---|---|
| 모호 시나리오용 | 2~4개 · 초점 예시<br>타당해 보이는 대안이 아니라<br>특정 action이 선택된 이유를 시연 |
| 판단 경계 전달 | "문제 있음" · "문제 없음" 양쪽 예시 + 판단 이유<br>→ 오탐 · 누락 동시 대응 |
| 허용 패턴 vs 진짜 문제 | 대비시킨 예시 → 오탐 감소 · 판단 일반화 |
| 건수 vs 선택 | 건수보다 어떤 케이스 · 어떤 이유를 고르는지가 핵심 |
| 명백한 버그 예시 40개 추가 | 경계 미제시 → 일관성 불변<br>input token 약 2배 ✗ |
| 예시 = 일치시킬 목록 ✗ | 판단 근거를 전달하는 재료로 사용 |
| 같은 작성 방식 예시만 3개 | 다른 형태의 결함 누락 (예: 9건 중 7건) |
| 일반화용 구성 | 작성 방식이 다른 정례<br>+ 비슷하지만 문제 아닌 부정례 + 이유 |
| 놓친 케이스만 그대로 추가 ✗ | 목록 일치에 머묾 · 판단 근거 미전달 |
| 출력 형식 시연 | 위치 · 문제 · 심각도 · 수정안 구조를 예시에 포함 |
| 근접 오류(near-miss)가 대부분 | 거부(reject) 예시 → 라벨 경계 학습 |
| 근접 오류 쌍 | 정교하게 선별 필요<br>나쁜 예시 = 잘못된 경계 학습 |
| 기준 문장 + 예시 | 구체적 지시와 다양한 예를 병용 |
| 예시 유지보수 | 기각된 지적 · 판정이 갈린 지적 · 정정 로그에서 후보 수집<br>→ 주기적 교체 |
| 놓침 · 오탐 발생 시 | 표면적 작성 방식이 아니라<br>전달 안 된 판단을 특정 → 예시 재선정 |



![few-shot을 쓸 때와 쓰지 말아야 할 때, 그리고 지시와 예시가 모순될 때의 decision tree](svg/6-fewshot-when.svg)
*그림: few-shot은 형식과 edge-case가 흔들릴 때만 쓰고, 소수의 다양한 예시를 지시와 모순 없이 넣어야 한다.*

<sub>근거: Amey-0027, Amey-0046, Amey-0062, Amey-0075, CCAR-F-Udemy01-0029, CCAR-F-Udemy02-0001, CCAR-F-Udemy04-0034, CCAR-F-Udemy05-0043, CCAR-F-Udemy05-0059, CCAR-F-Udemy06-0013, CCAR-F-Udemy06-0035, CCAR-P-jrajath94-0142, Preporato-0022, Udemy-0042</sub>

### 1.4 출력 형식 지정
**형식은 긍정형 · 예시 · XML 구조로 지정**

| 방법 | 판정 | 이유 |
|---|---|---|
| 긍정형 지정 ("~형식으로 출력하라") | ✓ | 원하는 형태 직접 제시 |
| 금지 목록 ("목록으로 쓰지 마라", "설명을 붙이지 마라") | ✗ | 원하는 형태 미제시 |
| XML 태그로 출력 구조 제시 | ✓ | 필요 시 · 예시와 함께 쓰면 효과 큼 |
| 형식 설명만 | ✗ | 항목 순서 · 표기 변형(단위 등) 세부 전달 어려움 |
| 가장 중요한 제약 강조 · 프롬프트 끝 제약 반복 | ✗ | 다시 말할 뿐 명확화 아님 |
| "깔끔하게(neat)" 같은 모호한 형용사 | ✗ | 아무것도 규정 안 함 |
| temperature 상향 | ✗ | variance 증가 → 일관성 · 신뢰성과 반대 방향 |
| 더 큰 모델 | ✗ | 당신의 형식을 모름 |
| 변환 규칙을 한 문장 지시로만 전달 | ✗ | 항목 내용 · 순서가 해석에 맡겨짐<br>→ 출력 편차 |
| 대표 입력 + edge case의 이상적 출력 예시 | ✓ | 형식 · 톤 · 구조 안정<br>(가장 확실한 수단 중 하나) |
| 필수 요소 · 배열 순서를 정의한 템플릿 | ✓ | 한 항목에 넣을 것 · 순서 고정 |
| 내용 유형별 표현 분리<br>(재무 = 표 · 뉴스 = 문장 · 기술 조사 = 구조화 리스트) | ✓ | 성질이 다른 내용에 맞는 표현 대응 |
| 모든 내용을 같은 글머리 기호로 변환 | ✗ | 수치 비교 · 뉴스 흐름 파악 불가 |
| 통합 subagent가 결과에 내용 유형 라벨 부여<br>(재무 · 뉴스 · 기술) | ✓ | 보고서 생성 측 표현 전환 확실 |

<sub>근거: Amey-0027, Amey-0045, Amey-0062, CCAR-F-Udemy01-0046, CCAR-F-Udemy04-0032, Udemy-0042</sub>

### 1.5 Structured outputs, tool 강제, prefill 폐지
**스키마 보장 = structured outputs · prefill → 400**

| 수단 | 내용 |
|---|---|
| structured outputs<br>(constrained decoding) | 스키마 검증 통과 JSON 보장<br>요청 `output_config.format`에 JSON schema<br>JSON을 산문으로 감싸는 류 실패 원천 제거 |
| forced tool choice | tool 1개, `input_schema` = 원하는 JSON 형태<br>`tool_choice`로 강제 → 반드시 그 tool 호출<br>`input` = 구조화 객체 |
| 확률적 수단 ✗ | system prompt "JSON으로 답하라"<br>temperature 0 · 자유 텍스트 regex parser<br>→ 스키마 준수 보장 ✗ |
| assistant 턴 prefill<br>(예: `{`로 시작) | 과거의 형식 강제 기법<br>Claude 4.6부터 마지막 assistant 턴 prefill<br>→ 400 error |
| 마이그레이션 가이드 | prefill 제거 · structured outputs로 대체<br>대안 ✗ · 대체재 |
| 프로덕션 추출 endpoint | 모델 출력 = untrusted input<br>tool use 스키마 강제 → 파싱 결과 검증 |
| 검증 실패 시 | validation error 붙여 1회 retry<br>→ 모델 자가 수정 |
| schema 선언 = 계약 | 구조가 요청이 아니라 계약의 일부<br>수신 시 validation → 계약 준수 확인<br>prompt 요청 · 사후 수정 · temperature → 우연에 맡김 |
| 확정적 보장 2계층 | 생성 제약(structured outputs)<br>+ 하위 시스템 전달 전 코드 validator<br>validator schema = 하위 시스템 schema와 일치 |
| schema 버전 관리 | schema를 하위 시스템과 함께 버전 관리<br>schema drift → validator 파손 |
| 확정 보장이 아닌 것 | prompt 속 형태 지침 → 샘플링으로 형태 깨짐<br>temperature 상향 → 변동 증가<br>문서화 → 통제 아님 |
| `output_config.format` schema | 응답 형태 제한 → 형태 오류용 재시도 루프 대부분 불필요<br>텍스트 파싱 전 `stop_reason` 확인 유지<br>"JSON만 요청" prompt → 텍스트 제한 ✗ |
| 스키마 위반 근원 해결 | constrained decoding으로 위반 제거<br>semantic 검사 · `stop_reason` 처리 = 별도 필요<br>retry · 지시 → 줄일 뿐 없애지 못함 |
| regex 복구 | 의도 추측 → 데이터 조용히 손상 |
| forced tool use 거부 모델<br>(Claude Opus 5.5) | 이름 지정 `tool_choice` → 400 error<br>`tool_choice` `auto` + strict tool use<br>또는 enum 포함 structured outputs → 라벨 1개 |
| forced tool use 지원 여부 | ⚠️ 모델 버전별로 상이<br>공식 `tool_choice` 문서의 모델별 표에서 재확인 |
| prefill 제거 후 형식 유지 | system prompt 지시로 출력 형식 유지<br>thinking 끄기 ✗ → prefill은 계속 400<br>⚠️ 4.6 이후 모델 기준 · 버전에 따라 바뀜 |

**해설 vs 공식 문서**

| 구분 | 내용 |
|---|---|
| ⚠️ 해설 | tool 강제 = "가장 신뢰할 수 있는 방법" |
| ⚠️ 현재 공식 문서 | 스키마 준수 보장 = structured outputs<br>(`strict` tool 포함) |
| ⚠️ strict 없는 tool 강제 | 신뢰성 높음 · 보장 ✗ |
| ⚠️ 선택지에 structured outputs 있음 | structured outputs 우선 |

**응답 시작 문구("Certainly!") 제어 — 해설 vs 현재 동작**

| 수단 | 해설 판정 | 이유 |
|---|---|---|
| partial assistant message로<br>직접 답변 시작 prefill | 정답 | 생성 수준에서 인사 패턴 방지<br>prefill 뒤에서 이어서 생성 |
| system prompt에 해당 문구 회피 지시 | ✗ | 도움은 되나 변형 생성 가능 → 덜 신뢰 |
| 후처리로 인사말 제거 | ✗ | 취약한 우회 |
| temperature ↓ | ✗ | 무작위성 제어 · 특정 문구 패턴 제어 ✗ |

- ⚠️ 해설의 prefill 정답은 위 표의 "Claude 4.6부터 마지막 assistant 턴 prefill → 400 error"와 충돌 · 구 모델 한정 해설로 읽을 것



![스키마 준수 JSON 필요 여부에 따라 structured outputs, forced tool choice, 확률적 방법을 고르는 decision tree](svg/6-output-format-tree.svg)
*그림: 스키마 보장이 필요하면 structured outputs, 선택지에 없으면 tool 강제이며, 지시·temperature·regex·prefill은 보장 수단이 아니다.*

![추출 결과를 검증하고 실패하면 validation error를 붙여 retry하는 루프](svg/6-validation-retry.svg)
*그림: 모델 출력은 untrusted input이므로 검증에 실패하면 숨기거나 땜질하지 말고 error를 붙여 다시 요청한다.*

<sub>근거: Amey-0039, CCAR-F-Amey-Thakur-0023, CCAR-F-Amey-Thakur-0058, CCAR-F-MyPractice-0072, CCAR-P-jrajath94-0139, CCAR-P-jrajath94-0618, CCAR-P-jrajath94-0621, CCAR-P-jrajath94-0622, CCAR-P-preporato-0009, Patrick-0004, Patrick-0026, Preporato-0021, Udemy-0042</sub>

### 1.6 긴 문서(long context) 배치
**긴 문서는 태그로 감싸 위에 · 질문은 끝 · 먼저 인용**

| 구분 | 내용 |
|---|---|
| 위치 효과 | 한가운데 내용 → 가장자리(앞 · 끝)보다 놓치기 쉬움 |
| 흔한 오해 | 위치 무관 ✗<br>가운데가 더 잘 지켜짐 ✗<br>오류 발생 ✗ |
| 배치 (약 20K tokens 초과) | 문서 = 프롬프트 위쪽, 지시 · 질문 = 맨 끝<br>복잡한 multi-document 테스트에서 응답 품질 최대 30% 향상 |
| 문서 태그 | `<contract>` 같은 태그로 감쌈 |
| 여러 문서 태그 | 문서마다 `<document>`로 감쌈<br>하위 태그 `<document_content>` · `<source>`<br>→ 본문 · 출처(metadata) 구분 · 문서 간 혼동 방지 |
| 인용 | 답 전에 관련 부분 먼저 인용(quote) → 집중에 도움 |

**구조 문제 해결 ✗**

| 수단 | 이유 |
|---|---|
| effort | thinking · 응답 token 양 조절뿐 |
| prompt caching (`cache_control`) | 반복 질의의 비용 · 속도용<br>모델이 읽는 내용 불변 |
| 사전 요약 | 창에 안 들어가거나 개요만 필요할 때용<br>세부 · 출처 손실 |

**집계 입력 재구성 (multi-agent synthesis 등)**

| 구분 | 내용 |
|---|---|
| 증상 | 앞 · 끝 자료는 반영, 가운데 자료만 누락<br>(subagent 출력 연결 · 약 75K~80K token) |
| 정답 구조 | 입력 맨 앞에 핵심 발견 · 출처 요약(지식 맵)<br>세부 결과는 출처 · 주제별 섹션 제목으로 정리 |
| 효과 | 앞 요약 = primacy effect 활용<br>섹션 제목 = 가운데 내용 탐색 보조<br>→ lost in the middle 직접 완화 |
| 원인 판단 | 정보량보다 배열 방식을 먼저 재검토 |
| 재조사 불가 제약 | 입력 재구성이 가장 직접적인 개선 |
| 근거 유지 요건 | 요약은 앞에 추가 · 상세는 보존<br>요약으로 대체 → 원래 근거 손실 |
| 실무 | subagent가 요약 + 상세로 나눠 반환<br>→ 앞 요약을 기계적으로 조립 |

**검색 기반 해법 (창에 들어가도 중간 누락)**

| 상황 | 정답 |
|---|---|
| 150K token 문서가 창에 들어가도 중간 사실 누락<br>(더 큰 window 구매 불가) | retrieve-then-read<br>관련 섹션만 검색 → 작은 집합에서 추론<br>개요 질문 = 섹션별 map-reduce 요약 |
| 40K token 매뉴얼 전체를 매 요청 붙여넣기<br>→ 비용↑ · 정확도↓ | 매뉴얼 1회 임베딩<br>질문마다 상위 chunk만 context에 투입<br>→ 비용 · 중간 누락 동시 개선 |
| 검색 passage 40개 중 답이 중간에 위치<br>(2개 선택) | re-rank → 가장 관련 있는 소수만 전달<br>passage 앞 · 질문과 지시 맨 끝 |
| chunk 20개가 길고 겹침 · 중간 chunk 답 오류 | 더 적고 짧은 chunk<br>문서 구조 경계에서 re-chunking<br>관련성 순위 후 window에 배치 |
| re-chunking 위험 | 과격한 chunking → 한 사실이 경계에서 분할<br>→ eval 세트로 검증 |
| dilution vs recall 구분 | dilution = 사실은 있으나 묻힘 → 구성 조정<br>recall = 사실 자체가 없음 → 더 많이 검색 |

**긴 입력에서 지시 · few-shot 보호 (truncation)**

| 구분 | 내용 |
|---|---|
| 증상 | 짧은 입력은 형식 정상<br>긴 이메일에서 형식 이탈 · 예시가 잘림 |
| 해설 정답 | 작업 지시문 · few-shot을 user 콘텐츠 앞으로<br>= 안정적 prefix로 잔존 |
| 해설 전제 | truncation은 context 끝에서부터 제거 |

- ⚠️ 위 1.6 "지시 · 질문 = 맨 끝" 권고와 방향 상충 · 해설은 앱 측 끝 절단 전제
- ⚠️ 공식 문서에 입력 절단 동작 서술 없음 · 한도 초과 시 Claude 4.5+ = `model_context_window_exceeded`로 생성 중단, 이전 모델 = validation error



![질문을 앞에 두고 문서를 이어 붙인 배치와 문서를 태그로 감싸 위에 두고 질문을 끝에 둔 배치 비교](svg/6-long-doc-order.svg)
*그림: 긴 입력은 문서를 문서별 태그로 감싸 위에, 인용 지시와 질문을 끝에 둔다.*

![긴 프롬프트의 앞, 가운데, 끝 중 가운데가 놓치기 쉬움을 보여 주는 그림](svg/6-lost-in-middle.svg)
*그림: 긴 프롬프트 한가운데 내용은 놓치기 쉬우므로 중요한 지시는 앞이나 끝으로 옮긴다.*

<sub>근거: Amey-0076, CCAR-F-MyPractice-0013, CCAR-F-Udemy01-0009, CCAR-F-Udemy02-0021, CCAR-F-Udemy06-0019, CCAR-F-paullarionov-0013, CCAR-F-preporato-0029, CCAR-P-jrajath94-0056, CCAR-P-jrajath94-0071, CCAR-P-jrajath94-0073, CCAR-P-jrajath94-0148, Preporato-0020, Udemy-0012, Udemy-0024</sub>

### 1.7 Context는 예산이다 (context rot)
**컨텍스트 = 예산 · 불필요한 자료는 정확도도 하락**

| 구분 | 내용 |
|---|---|
| 성격 | 공짜 자원 ✗ · 예산 |
| 느슨한 배경 자료<br>("혹시 도움이 될까") | 관련 자료와 attention 경쟁<br>→ 비용 · 정확도 하락 |
| 모델 동작 | 질문이 참조하지 않는 내용을 알아서 무시 ✗ |
| context rot | token 증가 → 앞서 읽은 내용을 정확히 끌어오지 못하는 현상 |
| 선택 vs 용량 | 무엇을 넣을지 선택 = 용량만큼 중요 |
| 창 상한 vs 정확도 | 창에 들어감 ≠ 정확도 유지 (별개) |
| 큰 창 (1M token 등) | 긴 자료를 한 번에 읽힐 때 유용<br>전체 이력 계속 유지<br>→ context rot · 비용 · latency 증가 |

**예산 배분과 품질 저하 원인**

| 구분 | 내용 |
|---|---|
| 예산 배분 | window = 희소 자원<br>지침 · 검색 자료 · 작업 상태 사이 의도적 배분 |
| 가득 채우기 | 희석 유발 ✗<br>긴 문서 외에서도 문제 |
| window 확대 | 배분 문제 미해결<br>품질 저하 시 키우기 ✗ |
| 긴 agentic 실행 품질 저하 | 원인 = context 누적<br>관련 내용과 오래된 내용 경쟁 |
| 원인 아님 | 모델 버전 변경 (실행 중 불변)<br>낮은 temperature (다양성만 감소)<br>tool 지연 (정확도 무관) |
| 50턴 후 지연 · 비용 증가 | 원인 = 전체 이력이 매 API 요청에 포함<br>(Claude API = stateless) |
| 짧은 대화(2,500 token)에서 지침 이탈 | assistant 응답 누적 → system prompt 비율 감소<br>모델이 자기 이전 출력에 패턴 매칭 → drift |
| 지침 약화 원인 아님 | system prompt 1회 전송 ✗ (매 호출 포함)<br>주의 저하 ✗ (짧은 길이에서 설명 안 됨) |
| 비대한 system prompt<br>(절차 수십 개 · 요청당 1~2개만 사용) | 핵심 role · 규칙만 system prompt<br>절차별 Skill · 검색 모듈 → 관련 시 로드 |

**입력 크기와 출력 상한**

| 구분 | 내용 |
|---|---|
| context window | 한 턴의 입력 + 새 출력을 함께 담음 |
| `max_tokens` | 응답 출력만 제한<br>window 확보 수단 ✗ |
| 보고서가 window에 들어감 | 한 요청으로 전송 · `max_tokens` = 예상 출력<br>청크별 분할 요청 ✗ |
| ⚠️ 모델별 window 크기 | 시점에 따라 변함<br>공식 문서(context windows)로 확인 |
| 입력 예산 준수 + 모델 고정 | 전송 전 대상 모델 ID로 token 계산<br>예산 초과 이력은 앱이 절단 |
| 사전 확인 수단 아님 | 응답 `usage` 필드 (호출 후 도착) |
| 오답 | 큰 window 모델로 전환 = 모델 고정 제약 위반<br>`effort` low (오답 보기) |



![관련 자료만 넣은 context window와 배경 자료와 이력을 다 넣은 context window 비교](svg/6-context-budget-rot.svg)
*그림: 불필요한 자료는 관련 자료와 attention을 놓고 경쟁해 비용뿐 아니라 정확도도 떨어뜨린다.*

<sub>근거: Amey-0007, Amey-0029, CCAR-F-Amey-Thakur-0032, CCAR-F-Amey-Thakur-0064, CCAR-F-MyPractice-0067, CCAR-F-MyPractice-0075, CCAR-P-Amey-Thakur-0031, CCAR-P-Amey-Thakur-0064, CCAR-P-jrajath94-0587, CCAR-P-jrajath94-0623, CCAR-P-preporato-0008, Udemy-0020, Udemy-0022</sub>

### 1.8 Context hygiene: prune, compact, isolate
**bloat 해법 = prune · compact · isolate · `max_tokens` ✗**

| 구분 | 내용 |
|---|---|
| 증상<br>(장시간 assistant) | 반복 · 이전 사례 혼동<br>최근 지시 망각 · 자기모순<br>장황한 tool output으로 컨텍스트 가득 |
| 진단 | context drift/bloat |
| prune | tool output 잘라내기 · 요약 |
| compact | 대화 이력 압축 |
| isolate | 독립 subtask를 subagent로 분리<br>→ main context 경량 유지 |

**Messages API 전제 · 이력 관리**

| 구분 | 내용 |
|---|---|
| Messages API | stateless<br>매번 system prompt · 과거 messages 재전송<br>→ 전부 context window · input token 과금에 누적 |
| 최신 메시지만 전송 ✗ | Claude가 앞의 경위 모름 |
| server 측 대화 상태 보존 | Anthropic-hosted managed agent 세션 등에 존재<br>Messages API의 전제 ✗ |
| session hygiene | 용건(task) 변경 → 세션 분리(isolate)<br>오래된 턴 요약(compaction) · 불필요 부분 잘라냄<br>관련 컨텍스트만 유지 |
| 오래된 턴 vs 최근 턴 | 오래된 턴 요약 · compact, 최근 턴 원문 유지<br>→ 중요 사실(예: 고객의 원래 문제) 보존 · 공간 확보 |
| 이력 없이 새 대화 ✗ | 문제 자체를 잊음 |
| Compaction | 오래된 턴 → Claude가 server 측에서 작성한 요약으로 대체<br>긴 대화 · 장시간 agent를 상한 내에서 잇는 핵심 전략 |
| Context editing | 오래된(stale) tool result 제거 |
| `max_tokens` | 응답 1회의 출력 상한<br>(응답이 잘려 `stop_reason` = `max_tokens`일 때 상향) |
| bloat 대응으로 `max_tokens` 조정 ✗ | context window 용량 확장 ✗<br>올려도 줄여도 bloat 해법 ✗ |

**tool output 증가 대응 (2단계)**

| 단계 | 대응 |
|---|---|
| 입구 | tool 응답이 다음 판단에 필요한 항목만 반환하도록 설계<br>(공식 tool 설계 지침) |
| 누적 | compaction · context editing으로 축소 |

- 미사용 tool 제거: tool 정의 token 감소 · 단 핵심 기능 tool 제거 ✗ → 목적 자체 붕괴
- 원인 = 가공 없이 쌓이는 결과 · tool 존재 ✗

**실패 신호와 범위 격리**

| 구분 | 내용 |
|---|---|
| 조기 신호 | 같은 일 반복 · 앞선 결정과 모순<br>= 상태 소실의 행동 증상 |
| 신호 아님 | 소요 시간 · token 비용 · tool error<br>(원인 다양 · 무관) |
| 고객 간 오염<br>(다른 고객 조회를 재사용) | 원인 = context 범위 설정 결함<br>window 크기 문제 ✗ |
| 처방 | 대화마다 context 범위 = 고객 1명<br>대상 변경 시 이전 조회 결과 삭제 · 격리 |
| 대안 ✗ | window 확대 · tool 제거<br>"고객 신원에 주의" 지시 |

**Tool 결과 입구 축소**

| 구분 | 내용 |
|---|---|
| 입구 trim | tool wrapper가 필요 필드만 `tool_result`로 반환<br>예: 45필드 중 5개 · 40+ 필드 중 관련 항목 |
| 구현 위치 | tool 구현 변경<br>`PostToolUse` hook으로 모델 전달 전 변환 |
| 효과 | 필요 수치가 대량 정보에 묻히는 문제 방지<br>(혼동 예방) |
| context editing과 차이 | 쌓인 결과를 나중에 지움 = 대증요법<br>payload 크기(원인) 미해결 |
| 첫 검토 항목 | 정보가 context에 들어오는 입구에서 줄일 수 있나 |
| 대안 ✗ | 이전 결과 전부 삭제 → 필요한 사실 손실<br>단계적 요약 → 수치 모호화<br>큰 window → 묻힘 해결 ✗ |
| 보조 | 사실은 `case facts` 블록으로 별도 유지 |

**Context editing: `clear_tool_uses`**

| 구분 | 내용 |
|---|---|
| ⚠️ 활성화 | beta header<br>`context-management-2025-06-27`<br>beta 단계 · 시점에 따라 변함 |
| 전략 | `clear_tool_uses_20250919` |
| 동작 | 입력 token이 trigger 초과 → 서버 측에서<br>오래된 tool result를 placeholder로 대체<br>`keep`으로 지정한 최근 결과만 유지 |
| 제외 | `exclude_tools` = 지우면 안 되는 tool 지정<br>(예: 초반 `get_incident` 정의 결과) |
| 요약 호출 | 불필요 (규칙 기반 제거)<br>추가 모델 호출 금지 제약에 적합 |
| 설계 순서 | tool별 재참조 필요 여부 정리 → 삭제 설정 |
| 대안 ✗ | `search_logs` 반환 건수 증가 = 총량 불변<br>앞에서부터 절단 = 초반 핵심 정보 손실<br>매 턴 전 tool 결과 삭제 = 최근 작업 손실 |

**Stateless 증상 진단**

| 증상 | 원인 · 조치 |
|---|---|
| 사용자가 선호를 이미 말했는데 Claude가 다시 질문 | 원인 = 앱이 이전 메시지를 `messages` 배열에 미포함<br>조치 = 매 요청에 전체 대화 기록 포함 |
| 오진 후보 | vector database 필요 ✗ · `session_id` 필요 ✗<br>두 메시지 교환에서 context window 초과 ✗ |
| 전제 | Claude에 server 측 memory 없음<br>모든 API 호출 stateless |



![context drift/bloat 증상에서 prune, compact, isolate 세 해법으로 갈라지는 그림](svg/6-context-hygiene.svg)
*그림: drift/bloat는 prune, compact, isolate로 다루며, 큰 창이나 max_tokens 조정은 해법이 아니다.*

![stateless Messages API에서 요청마다 이력이 쌓이고 compaction으로 줄이는 흐름](svg/6-stateless-compaction.svg)
*그림: Messages API는 매 요청에 이력을 다시 보내므로 오래된 턴은 요약하고 최근 턴은 원문으로 남긴다.*

![tool 결과를 입구에서 줄이고 누적분을 compaction과 context editing으로 정리하는 두 단계](svg/6-tool-output-two-stage.svg)
*그림: tool output은 입구에서 필요한 항목만 반환하고, 누적분은 compaction과 context editing으로 줄인다.*

<sub>근거: Amey-0007, Amey-0045, CCAR-F-Amey-Thakur-0036, CCAR-F-Amey-Thakur-0078, CCAR-F-MyPractice-0064, CCAR-F-Udemy02-0051, CCAR-F-Udemy03-0010, CCAR-F-Udemy06-0004, CCAR-P-jrajath94-0624, Patrick-0041, Udemy-0020, Udemy-0022</sub>

### 1.9 명시적 기준으로 false positive 줄이기
**정밀도 = 명시적 기준 + 경계 예시 · 확신도 ✗**

| 모호한 지시 | 문제 | 명시 기준 |
|---|---|---|
| "주석이 정확 · 최신인지 확인" | 무엇이 부정확인지 미정<br>→ TODO · 문구 지적 다수, 진짜 모순 누락 | 주장 동작이 실제 코드 동작과<br>모순될 때만 지적 |
| "꼼꼼하게 보되 사소한 지적은 피하라" | 모델이 기준선을 짐작<br>→ 스타일 지적 들쭉날쭉 · 취약점 누락 | 범주 · 최소 심각도 · 제외 대상 명시<br>→ 준수 여부 확인 가능 |
| "의심스러운 합계를 플래그" | 측정 불가 기준<br>→ 무해한 표기 차이 플래그 · 계산 오류 누락 | 명세 합계와 기재 합계가 모순되는 조건을 수치로 정의 |
| "영향의 크기에 따라 심각도 판단" | 영향 정의 없음<br>→ 같은 문제가 critical · minor로 갈림 | 심각도 수준별 구체적 코드 예시 포함 기준 |
| "높은 확신의 문제만 보고" | 취향성 스타일 지적에도 높은 확신 가능<br>→ 보고 대상 미축소 | 보고할 종류 · 건너뛸 종류를 검증 가능하게 정의<br>+ 노이즈원 항목을 체크리스트에서 제외 |

| 원칙 | 내용 |
|---|---|
| 노이즈의 원인 | 확신도가 아니라 보고 범위 |
| 판정 흔들림의 원인 | 지시에 남은 측정 불가한 말 |
| 기준 작성 | 보고 조건 + 보고 제외 대상을 양쪽 모두 구체화 |
| 기준 + 예시 | 기준으로 신호와 잡음의 경계를 긋고<br>예시로 경계를 시연 |
| 성공 기준 | 구체적 · 측정 가능 |

| "보수적으로 · 확신도 높은 것만" 지시 | 내용 |
|---|---|
| 결과 | 오탐 38% → 36%만 감소<br>실제 버그 누락 증가 |
| 이유 1 | 보고 · 비보고의 판단 경계를 바꾸지 않음 |
| 이유 2 | 확신도 선별 = 미보정 자기 보고 확신도에 의존 |
| 원인 위치 | 지시의 위치 · 실행 방법 ✗<br>지시의 내용 ○ |
| 대안 | 보고 대상(로직 오류 · 보안)<br>제외 대상(사소한 스타일 · 국소 패턴)<br>→ 범주별 정의 + 예시 병행 |

| 편차의 종류 | 처방 |
|---|---|
| 형태 흔들림<br>(형식 · validation 실패) | JSON schema |
| 판단 흔들림<br>(단정 · 유보 · 제외가 실행마다 다름) | 판단 규칙을 prompt에 명시<br>+ 경계 사례 예시(3~5개 · `<example>`) |
| 진단 질문 | 흔들리는 것이 형태인가 판단인가 |

| 근거 필드를 요구할 때 | 내용 |
|---|---|
| 설계 원칙 | 근거를 붙이게 하는 것과<br>근거가 없을 때의 동작을 분리해 설계 |
| 입력에 근거 없음<br>(예: 해당 정책 미제공) | validator가 빈 인용을 기각 = 정상 동작 |
| 처방 1 | 부족한 근거를 입력에 공급 |
| 처방 2 | 근거 없으면 정보 부족으로 게시 보류 |
| 이유 | 불확실하면 "모른다"고 답하게 하고<br>인용으로 뒷받침 안 되는 주장은 철회 |
| 효과 없음 ✗ | `max_tokens` 상향 · schema 필수화<br>→ 없는 근거를 만들지 못함 |

![모호한 지시 다섯 가지를 보고 조건과 제외 대상이 있는 명시적 기준으로 바꾸는 비교](svg/6-explicit-criteria.svg)
*그림: 노이즈의 원인은 확신도가 아니라 보고 범위이므로, 모호한 지시를 측정 가능한 기준으로 바꿔야 오탐이 준다.*

<sub>근거: CCAR-F-Amey-Thakur-0007, CCAR-F-Amey-Thakur-0047, CCAR-F-MyPractice-0022, CCAR-F-Udemy01-0053, CCAR-F-Udemy02-0027, CCAR-F-Udemy02-0055, CCAR-F-Udemy03-0053, CCAR-F-Udemy05-0001, CCAR-F-Udemy05-0041, CCAR-F-Udemy06-0040, CCAR-F-paullarionov-0022, CCAR-F-preporato-0023</sub>

### 1.10 범주별 오탐 관리와 신뢰 회복
**오탐 높은 범주만 일시 중단 · 개선 후 재개**

| 상황 | 대응 |
|---|---|
| 범주별 오탐률 편차<br>(security 8% · style 52% 등) | 오탐 높은 범주 일시 비활성화<br>정확한 범주는 유지 |
| 오탐 범주가 정확한 범주 신뢰까지 훼손 | 개발자가 모든 지적을 읽지 않고 닫음 |
| 비활성화의 효과 | 모두 무시하게 만드는 노이즈 제거<br>→ 신뢰 하락 즉시 정지 |
| 비활성화 동안 | prompt 개선(명시 기준으로 재작성) |
| 재개 전 | 과거 PR로 개선 후 정밀도 측정<br>→ 다른 범주 수준 확인 후 재개 |
| 재개 후 | 기각된 지적을 범주별로 계속 집계<br>→ 오탐률 하락 확인 |
| 문제가 일부 범주에 집중 | 해당 범주만 중단 + 기준 재작성<br>전체 중단 ✗ (정확한 범주 가치 상실) |
| severity 판정 불일치 | 신뢰 훼손 → 심각도 수준별 기준 · 코드 예시<br>경계 가까운 실제 사례를 모아 추가 |

<sub>근거: CCAR-F-MyPractice-0023, CCAR-F-MyPractice-0029, CCAR-F-Udemy04-0037, CCAR-F-Udemy05-0041, CCAR-F-Udemy06-0042, CCAR-F-paullarionov-0023, CCAR-F-paullarionov-0029</sub>

### 1.11 Few-shot 실패 증상별 처방
**증상의 원인(단서 부족) 진단 → 해당 단서를 예시로**

| 증상 | 원인 | 처방 |
|---|---|---|
| 상세 지시에도 피드백 상세도 · 구조가 들쭉날쭉 | 추상 지시는 따를 패턴이 없음 | 원하는 구조(문제 · 위치 · 수정안)를 보여 주는 예시 3~4개 |
| 지시한 4항목 순서가 무너짐 · 규정이 문장에 묻힘 | 지시 문장에만 의존 | 완성 예시 여러 경우 + `<example>` 태그<br>(순서 · 줄바꿈 · 위치는 글로 전달 어려움) |
| JSON 필드 이름 · 형식이 호출마다 다름 | 형식 준수 = 패턴 매칭 | 예시 3~5개 → 필드 이름 · 중첩 · type 정의 |
| 텍스트 변환 불일치<br>(내부 ID 잔존 · 파괴적 변경 완화 · 근거 없는 부풀림) | 규칙만으로는 본보기 부족 | 기대하는 입출력 예시 |
| 흔한 입력은 정확, 드문 형식은 실패 | 드문 경우를 명세한 적 없음 | 예시 + 필드 부재 시 처리 규칙 명시 |
| 값이 원문에 있는데 필드가 null<br>(표 · 서명 · 산문 · 코드 블록) | 값이 어떤 모양으로 나타나는지 단서 부족 | 형식별 입력 → 출력 예시 3~5개<br>+ 필드별 출현 위치 · 읽는 법 명시 |
| 비격식 표현을 추측 값으로 채움 | 확정 불가 표현의 처리가 미전달 | 비격식 표현 → 올바른 추출 결과 예시<br>+ 확정 불가 시 확인 요청 예시 |
| 상세 기준 · 고정 template에도 오탐 · 누락 동시 | 기준 문장은 경계를 전달 못 함 | 문제 있음 · 없음 양쪽 예시 + 이유 |
| 모호한 요청의 분류(조사 · 계획 · 직접 답장) 흔들림 | 규칙 추가로는 경계 사례 부재 | 모호 요청별 정답 대응<br>+ 대안을 물리치는 간결한 이유<br>+ `<example>` 태그 |
| 키워드 포함만으로 표시(예: 'fire' → 'firewall') | positive만 본 상태 | 까다로운 negative 예시 → 경계 학습 |
| 모호한 질의에서 tool 오선택 | 비교 판단 과정 미전달 | 오류 나는 모호 시나리오 겨냥 예시<br>+ 이 tool이 나은 이유 명시 |
| 다중 이슈 메시지에서 정확도 하락<br>(하나만 처리 · parameter 뒤섞임) | 분해 · routing 패턴 미전달 | 이슈 분해 · tool 배정 · parameter 분리<br>를 보여 주는 예시 |

| 실패 지점 | 예시가 가르칠 것 |
|---|---|
| 특이한 형식(예: 시골 경로 · 사서함) | edge-case 경계 |
| 특이한 직함을 skill로 오분류 | 거부 예시로 경계 |
| 두 범주에 걸친 티켓 | tie-break 규칙 |
| 여러 페이지 송장에서 품목 합침 | 페이지 경계 |
| 라벨 인접 혼동 | 거부 예시 |
| 형식(엄격한 schema 추출) | schema로 고정 · 예시와 역할 분담 |

<sub>근거: CCAR-F-Amey-Thakur-0024, CCAR-F-Amey-Thakur-0060, CCAR-F-MyPractice-0020, CCAR-F-MyPractice-0047, CCAR-F-MyPractice-0060, CCAR-F-Udemy01-0029, CCAR-F-Udemy01-0043, CCAR-F-Udemy02-0001, CCAR-F-Udemy02-0050, CCAR-F-Udemy02-0058, CCAR-F-Udemy05-0043, CCAR-F-Udemy06-0035, CCAR-F-paullarionov-0020, CCAR-F-paullarionov-0047, CCAR-F-paullarionov-0060, CCAR-F-preporato-0024, CCAR-P-jrajath94-0053, CCAR-P-jrajath94-0142, CCAR-P-jrajath94-0347, CCAR-P-jrajath94-0410, CCAR-P-jrajath94-0473, CCAR-P-jrajath94-0536</sub>

### 1.12 기법 선택: 평가를 통과하는 가장 단순한 기법
**오류 형태가 기법을 고름 · 통과하면 승급 ✗**

| 원칙 | 내용 |
|---|---|
| 선택 기준 | eval을 통과하는 가장 단순한 기법 |
| 오류 형태 → 기법 | 근접 오류 → 거부 예시<br>어렵고 검증 가능한 다단계 → 명시적 추론<br>엄격한 schema → 구조화 출력 + 코드 검사 |
| few-shot 위치 | zero-shot 위에서 가장 저렴한 단계 |
| 이미 eval 통과 | 상위 기법으로 승급 ✗ |
| 승급 조건 | 좋은 예시 · 전체 컨텍스트로도 실패할 때 |
| fine-tuning | 예시가 실패한 뒤의 단계 |
| 학습 예산 없음 · 새 라벨 정확도 미달 | `<example>` 태그 예시 3~5개로 시작<br>측정 후 eval에서 필요할 때만 추가 |
| 짝짓기 | 가설 → eval 재실행으로 확인 |

| 작업 | 기법 |
|---|---|
| 짧은 티켓을 4개 라벨로 분류 | 거부 예시 few-shot |
| 여러 단계 계산, 각 단계 검증 가능 | 명시적 단계 추론 |
| 엄격한 JSON schema 추출 | 구조화 출력 + 코드 검사<br>(서술형 설명 ✗) |
| 자유 텍스트 → 고정 형식 견적<br>+ 범위 밖 작업 거절 | 거절 예시 few-shot(경계 사례 포함)<br>+ structured schema |

| 대안 | 한계 |
|---|---|
| CoT(추론 token) | 모든 호출에 token 추가<br>경계 문제는 더 오래 생각이 아니라 경계 제시가 필요 |
| 라벨 50,000건 fine-tuning | 예시로 메울 수 있는 4포인트 차이에 과함 |
| 거부 예시 few-shot의 한계 | 근접 오류 쌍 선별 필요<br>새 edge case마다 예시 유지보수 |
| 구조화 출력의 한계 | 견적 형식에 맞춘 schema 버전 관리 |

<sub>근거: CCAR-P-jrajath94-0142, CCAR-P-jrajath94-0144, CCAR-P-jrajath94-0292, CCAR-P-jrajath94-0347, CCAR-P-jrajath94-0620</sub>

### 1.13 대화가 길어질 때 instruction drift
**drift = 규칙 대신 예시 · 주기적 reminder**

| 구분 | 내용 |
|---|---|
| 증상 | 10~15턴 후 system prompt 지침 이탈<br>(token 한도 내에서도 발생) |
| 처방 1 | 행동 reminder를 주기적으로 주입<br>→ 대화 누적 중 제약 재확립 |
| 처방 2 | 선언적 규칙(2,800 token)<br>→ 구체적 few-shot 예시로 교체<br>예: 숙련도별 적응을 시연하는 예시 |
| 처방 2의 이유 | 선언적 규칙은 매 턴 추론 필요 → drift 취약<br>예시는 맞출 명확한 행동 패턴 제공 |
| reminder의 한계 | 증상 대응 · 예시 교체가 더 안정 |
| 끝 batch 배치 | 초기에만 도움 · 턴 수준 drift에 부족 |
| 재생성 | 수정 비용이 큼 |
| 오답: 지침을 첫 user message로 이동 | 권위 낮아짐 |
| 오답: 새 대화 시작 | context 소실 |
| 오답: 응답 후 validation | 예방 아닌 교정 · 상당한 지연 |
| ⚠️ 기존 1.8 "매 턴 system prompt 반복 ✗"와 구분 | 정답은 "주기적 reminder"<br>주기 · 분량 기준은 해설에 없음 |

<sub>근거: CCAR-F-MyPractice-0069, CCAR-F-MyPractice-0070</sub>

### 1.14 Schema 설계: nullable · enum · 출처 필드
**schema는 현실 반영 · 없음은 null · 미분류는 other**

**필드 유형별 설계**

| 설계 | 판정 | 이유 |
|---|---|---|
| 원본에 없을 수 있는 필드 = nullable | ✓ | 진짜 없음 vs 추출 실패 구분 |
| 조건부로 필요한 항목 = nullable + 후단 검증 | ✓ | schema는 현실 반영 · 조건은 코드로 |
| 전부 required | ✗ | 정상 문서에서도 값 날조 · 추출 실패 |
| 전부 optional | ✗ | 진짜 놓친 경우 감지 불가 |
| 값 없음을 말없이 생략 | ✗ | 없음 vs 실패 구분 불가 |
| 그럴듯한 기본값 | ✗ | 데이터 날조 · 오염 |
| 빈 문자열 | ✗ | 값 없음 vs 빈 값 구별 불가 |
| 메모 필드에 사유 기록 | ✗ | 기계가 읽을 수 있는 상태 아님 |

**값 날조의 원인 진단**

| 구분 | 내용 |
|---|---|
| 증상 | 필수 필드를 채우려고 없는 값 출력<br>(예: 존재하지 않는 종료일 `2099-12-31`) |
| 원인 | prompt 아님 · schema 설계 |
| 해결 | 해당 필드 nullable |
| 조합 | 별도 필드(자동 갱신 여부) + null 종료일<br>→ 하위 시스템이 계약 종류 판단 |
| 운영 | null 건수를 문서 종류별 집계<br>→ 값이 있어야 할 문서의 null 여부 점검 |

**결측 표기 일관성**

| 상황 | 정답 |
|---|---|
| 결측이 null · `""` · `"N/A"` · 필드 생략으로 혼재<br>문장 규칙 추가 후에도 지속 | 예시 3~5개 (relevant · diverse · 태그 구조)<br>+ schema로 결측 = null만 허용<br>→ 나머지 표기는 검증에서 탈락 |

**enum 분류 설계**

| 구분 | 내용 |
|---|---|
| 닫힌 enum의 한계 | 목록 밖 입력 → 가까운 값으로 억지 분류<br>또는 범위 밖 값 생성 → 하류 validation 실패 |
| structured outputs와 enum | 값 범위는 보장 · 분류 정확성은 보장 ✗ |
| `other` + 상세 문자열 필드 | 해당 없음을 그대로 표현 · 내용 보존 |
| `unclear` 값 | 판단 불가 수용 → 사람 리뷰로 전달 |
| 운영 | `other` 출현 모니터링<br>→ 정착된 유형을 정식 값으로 승격<br>(새 유형이 계속 늘어나는 조건) |

**출처 필드**

| 구분 | 내용 |
|---|---|
| 값마다 원본 위치 기록 필요 | 출처 필드를 schema에 선언 |
| 근거 | 출력에 담을 정보 = 선언한 형태 안에 있어야 함<br>필드 요구 시 두 번째 pass 불필요 |

![값이 없을 수 있는 필드, 목록 밖 분류, 출처 요구에 대한 schema 설계와 피할 설계](svg/6-schema-design.svg)
*그림: schema는 값 없음 · 목록 밖 분류 · 출처를 표현할 자리를 선언해야 값 날조와 억지 분류를 막는다.*

<sub>근거: CCAR-F-Amey-Thakur-0008, CCAR-F-Amey-Thakur-0025, CCAR-F-Amey-Thakur-0048, CCAR-F-Amey-Thakur-0059, CCAR-F-Amey-Thakur-0074, CCAR-F-Udemy01-0042, CCAR-F-Udemy03-0018, CCAR-F-Udemy04-0006, CCAR-F-Udemy05-0037</sub>

### 1.15 Validation 실패 처리: 의미 검증 · 재요청 설계
**schema = 구조 보장 · 의미 오류는 구체 오류로 재요청**

**구조 오류 vs 의미 오류**

| 구분 | 예 | 대응 |
|---|---|---|
| 구조 오류 | JSON 구문 오류 · 타입 · 필수 항목 | schema 선언 · structured outputs<br>· `strict`로 제거 |
| 의미 오류 | 값이 엉뚱한 필드에 입력 · 합계 불일치<br>존재하지 않는 행 번호 · 잘못된 페이지 번호<br>인용 원문 누락 | schema 밖 검증 코드 |
| 업무 규칙 위반 | 변경 없는 파일 지적 · 정책 위반 지적<br>상품 크레딧이 `shipping_refund`에 입력 | 실행 전 업무 규칙 검증<br>→ 위반 내용을 구체적으로 반환 |
| 오배치 예방 | 취합 착오가 나는 필드 | 필드 `description` 구체화 + 검증 코드 |

| 구분 | 내용 |
|---|---|
| 판별 기준 | 실패가 형식 오류인가 의미 오류인가<br>→ 대응 선택의 출발점 |
| 파싱 가능 · 필수 필드 충족 · 타입 일치 | 형식의 올바름 ≠ 업무상 올바름 |
| 구문 오류가 이미 사라진 상태 | 남은 오류 = 의미 문제<br>`strict: true` · `tool_choice` 강제<br>→ 효과 없음 |
| 효과 확인 | 불일치 건수를 필드별 집계 |

**재시도 요청 구성**

| 재료 | 역할 |
|---|---|
| 원본 문서 | 올바른 값 대조 (날짜 교정 · 소스에 없는 handler 이름 확인) |
| 거부된 JSON | 고칠 대상 |
| validator의 구체 오류 | 무엇이 틀렸는지<br>(필드 누락 · 잘못된 enum · 소스에 없는 값은 성격이 다름) |
| XML 태그 구분 | 지시 · 문맥 · 입력 혼동 방지 |
| 응답 지시 | 수정이 끝난 데이터만 반환 |
| 성공 조건 | 모델이 오류를 고칠 증거를 손에 쥐었는가 |

**업무 규칙 거부 시 tool 호출 처리**

| 구분 | 내용 |
|---|---|
| 상황 | tool 입력이 schema에 맞는데 애플리케이션 규칙이 거부 |
| 반환 | `tool_result` + `is_error: true`<br>+ 구체적 이유 |
| 이력 | 주고받음을 대화 이력에 남긴 채 다음 요청 |
| 메시지 내용 | 무슨 일이 일어났는지 · 다음에 시도할 것 |
| 둘 중 하나 누락 | 수정 재료가 Claude에 전달되지 않음 |

**retry가 통하는 경우 vs 안 통하는 경우**

| 상황 | 효과 | 대응 |
|---|---|---|
| 정보는 입력에 있고 표기만 다름<br>(예: 날짜 ISO 8601 변환) | 있음 | 검증 오류 붙여 재요청 |
| 정보가 입력에 없음<br>(별도 파일에만 존재) | 없음 | 누락 원본 제공<br>→ 그래도 없으면 null · "이용 불가" 허용 |
| 소스 자체가 모순<br>(증명서 합계 전기 오류) | 없음 | `stated_total` · `calculated_total`<br>모두 추출 + `conflict_detected`<br>→ 사람에게 |
| 재시도 N회에도 해소 0건 | 없음 | 입력에 정보 없다는 신호 |

| 구분 | 내용 |
|---|---|
| 검증 실패 지속 시 첫 점검 | 모델이 필요한 정보를 가졌는가<br>(prompt · schema 수정보다 먼저) |
| 원인 분리 | 입력 측 문제 vs 출력 측 문제 구분 |
| 재시도 · strict · few-shot | 없는 정보를 모델이 채우게 하는 방향 |
| 필수 충족용 날조 방지 | 원본에 없을 수 있는 필드 = null 허용 |
| 운영 | 오류 종류별 재시도 성공률 기록<br>→ 안 고쳐지는 오류 조기 식별 |
| 운영 | 재시도 후 남은 불일치를 공급자별 집계<br>→ 개선 요청에 활용 |

**validation 운영 원칙**

| 구분 | 내용 |
|---|---|
| 신뢰성 패턴 | schema 강제 + validation-retry loop |
| 경계 validation | 결함이 하류로 퍼지기 전 차단<br>비용 절감 · 모델 정확도 향상 아님 |
| 드문 실패<br>(수백 호출에 1회) | 정해진 처리 경로 필요<br>막을 것 = 잘못된 데이터의 조용한 통과 |
| 검증 loop 3요소 | 검출 · 수정 단서(구체 오류 + 원본) · 최종 수용처 |
| 최종 수용처 | 재시도로 해소되지 않는 건 → 사람 검토 |

**`stop_reason`과 값 정확성**

| 구분 | 내용 |
|---|---|
| `stop_reason: "max_tokens"` | 응답이 상한에서 끊김<br>structured outputs의 schema 준수 보장 ✗ |
| 대응 | `max_tokens` 상향 후 재시도<br>또는 요청을 작게 분할 → 중단 자체 감소 |
| 값 정확성 | schema 보장 = 구조 · 타입까지<br>행 번호 등은 참조 대상과 대조 → 구체 오류 반환 |
| `pause_turn` | 서버 tool loop 일시 정지 · 이 문제와 무관 |
| 원칙 | 구조 검증과 의미 검증 = 별개 수단 |

![구조 검증과 의미 검증 뒤에 구체 오류로 재요청하거나 최종 수용처로 보내는 흐름](svg/6-validation-semantic.svg)
*그림: 의미 오류는 정보가 입력에 있을 때만 구체 오류를 붙여 재요청하고, 입력에 없으면 null 허용이나 사람 검토로 보낸다.*

<sub>근거: CCAR-F-Amey-Thakur-0049, CCAR-F-Amey-Thakur-0072, CCAR-F-Amey-Thakur-0073, CCAR-F-Udemy01-0023, CCAR-F-Udemy01-0025, CCAR-F-Udemy01-0032, CCAR-F-Udemy02-0018, CCAR-F-Udemy02-0026, CCAR-F-Udemy03-0048, CCAR-F-Udemy04-0033, CCAR-F-Udemy04-0045, CCAR-F-Udemy05-0003, CCAR-F-Udemy05-0032, CCAR-F-Udemy06-0020, CCAR-F-preporato-0026</sub>

### 1.16 Multi-pass 리뷰 · 독립 리뷰어
**리뷰는 생성과 분리 · 큰 입력은 국소 + 통합 pass**

**자기 리뷰의 한계와 독립 리뷰**

| 구분 | 내용 |
|---|---|
| 같은 session 자기 리뷰 | 생성 시 추론 · 전제를 그대로 보유<br>→ 경우를 고려하고도 자기 방식이 맞다고 결론<br>= 확증 편향 |
| 독립 리뷰 instance | 생성자의 추론에 접근 ✗ → 확증 편향 회피<br>근본 원인 직접 해결<br>= 사람 동료 리뷰의 fresh eyes |
| 독립성 조건 | 별도 instance + 생성 시 추론 · 대화 기록 미전달<br>둘 다 충족 필요 |
| 리뷰 입력 | diff · 요구사항 명세 · 리뷰 기준만<br>→ 입력 한정 템플릿을 pipeline에 고정 |
| Writer/Reviewer 패턴 | 한 session 작성 · 다른 session 리뷰<br>새 context = 직전 코드에 대한 편향 없음 |
| 판별 기준 | 리뷰하는 쪽이 만든 쪽의 사고 과정에서 분리됐는가 |
| extended thinking 예산을 늘려도 불변 | 원인 = 사고 깊이 아닌 context 공유 |
| 같은 대화 안 "직전 결과 확인" follow-up | 검증이 느슨해짐<br>→ 별도 API 호출에 원본 · 결과 · 판정 기준 전달 |

**리뷰 기준과 결과 게시**

| 구분 | 내용 |
|---|---|
| 리뷰 기준 | `CLAUDE.md`로 제공 |
| 보고 범위 | 올바름 · 요건 문제만 보고<br>→ 세세한 취향 지적(과잉 수정) 방지 |
| 결과 게시 | `--output-format json`<br>+ `--json-schema`로 구조화<br>→ PR 코멘트 게시 · 사람 확인 용이 |

**자기 비평 단계 (evaluator-optimizer)**

| 구분 | 내용 |
|---|---|
| 적합한 문제 | 정답은 맞는데 설명 완전성이 케이스마다 들쭉날쭉<br>(정책 · 일정 · 다음 절차 누락) · 사람 감독 추가 ✗ |
| 설계 | 초안 내기 전 구체 기준에 비추어 자기 평가 |
| 패턴 | 생성 → 기준 평가 → 피드백 반영<br>(한 LLM 생성 · 다른 LLM 평가 형태도 있음) |

**큰 입력을 나누는 pass 설계**

| 상황 | 설계 |
|---|---|
| 대형 PR(14~42개 파일) single-pass<br>→ 깊이 편차 · 뻔한 버그 누락 · 모순 피드백 | 원인 = attention dilution (context rot)<br>→ 파일별 집중 pass로 같은 깊이 확보 |
| 파일 간 문제<br>(의존성 · 데이터 흐름 · 필드명 변경 미반영) | 별도 통합 pass<br>입력 = 파일별 결과 + 변경된 interface 목록 |
| 설계 원칙 | 국소 pass + 횡단 통합 pass 둘 다 필요<br>한쪽만 있으면 다른 쪽 결함 누락 |
| 자유도 높은 조사 처리 회피 요건 | 분할 · 통합 모두 고정 절차 workflow<br>= 자율 agent와의 차이 |
| prompt chaining | 고정 단계 · 단계 출력을 다음에 전달<br>단계가 단순 → 정확도 상승<br>중간 gate · 기록 · 채점 가능 |
| 섹션 구조를 예측할 수 있는 긴 문서<br>(60쪽 대출 신청 패키지) | 섹션별 추출 → 통합 후 대조 pass<br>(중복 entity · 합계 불일치 · 관계 오류) |
| source 묶음 속 근거 없는 주장 · 모순<br>(같은 출처를 지지 · 반박 양쪽에 사용) | claim–source 쌍마다 독립 리뷰 pass<br>→ 통합 pass에서 모순 · 누락 확인 |
| 검증 위임 시 | 주장 + 대조할 출처 발췌를 함께 전달 |
| 생성 전 기록 · 채점할 checkpoint 요구 | 출처 단위 리뷰 chain + 최종 통합<br>→ 단계별 산출물이 남음 |
| 분해 방식 판단 | 입력 구조를 사전에 아는가<br>결함이 어느 단계에서 생기는가 |

**확신도 · 심각도 routing**

| 구분 | 내용 |
|---|---|
| 포괄적 1차 분석 + 전부 같은 우선순위 | 포괄성 유지 + 별도 검증 pass<br>출력 schema = confidence<br>· severity · evidence |
| 대응 규칙 | confidence × severity 조합 → 경로 매핑<br>(자동 해결 · 사람 리뷰 · 추세 분석) |
| 확신도 출처 | 모델 자기 신고 값 · API 응답에 없는 값 |
| 캘리브레이션 | 정답 라벨 데이터로 확신도–결과 관계 측정<br>→ 임계값 결정 (예: 개발자 대응 · 기각 기록) |
| 임계값 유지 | 코드베이스 · 규약 변화에 맞춰 기록과 정기 대조 |
| 후보 지적 검증 | 코드와 대조해 오탐 제거 후 게시<br>(Claude Code 관리형 코드 리뷰 구성) |
| 오탐 40% · 확인 시간 병목 · 필터링 금지 | 지적마다 근거 · 신뢰도를 바로 포함<br>→ 전부 노출 · 개발자 분류 가속 |

![독립 리뷰어가 파일별 집중 pass를 돌리고 통합 pass로 합치는 구조](svg/6-multipass-review.svg)
*그림: 리뷰는 생성 session과 분리하고, 큰 입력은 파일별 국소 pass와 파일 간 통합 pass를 둘 다 돌려야 한다.*

<sub>근거: CCAR-F-MyPractice-0017, CCAR-F-MyPractice-0027, CCAR-F-MyPractice-0052, CCAR-F-Udemy01-0033, CCAR-F-Udemy02-0028, CCAR-F-Udemy02-0031, CCAR-F-Udemy02-0056, CCAR-F-Udemy03-0007, CCAR-F-Udemy03-0023, CCAR-F-Udemy03-0025, CCAR-F-Udemy03-0030, CCAR-F-Udemy04-0003, CCAR-F-Udemy04-0013, CCAR-F-Udemy05-0022, CCAR-F-Udemy05-0060, CCAR-F-Udemy06-0021, CCAR-F-paullarionov-0017, CCAR-F-paullarionov-0027, CCAR-F-paullarionov-0028, CCAR-F-paullarionov-0052</sub>

### 1.17 Context 결함 5종 진단

**증상 → 결함 이름 → 처방 1:1 대응**

| 결함 | 증거 문구 | 처방 |
|---|---|---|
| growth | 매 호출 대량 로드<br>(한 학기 · 한 시즌 · 분기 전체) | just-in-time retrieval |
| duplication | 같은 내용 반복 삽입<br>(정책 4번 · 측정값 2~3번) | 조립 시점 dedupe<br>(표준 fact key 필요) |
| loss | compaction 후 이름 · 결정 · 숫자 소실 | 요약이 사실을 보존하도록 수정 |
| exhaustion | 작업 도중 window 가득 → 중단 · 오류 | 여유 공간 확보 · 이른 compaction<br>(임계값 튜닝 필요) |
| dilution | 엉뚱한 구간에 attention<br>(7월 질문에 3월 데이터 · 틀린 판례) | 더 적고 더 잘 배치된 chunk |

**진단 규칙**

| 구분 | 내용 |
|---|---|
| 선택 기준 | 증거가 명시된 결함만 선택 |
| exhaustion 제외 | overflow · 오류 언급 없음 |
| loss 제외 | turn 소실 언급 없음 |
| 흔한 조합 | 대량 로드 + 엉뚱한 답 → growth + dilution<br>대량 로드 + 반복 삽입 → growth + duplication |
| 처방 | 결함마다 처방이 다름<br>한 처방으로 전부 해결 ✗ |
| duplication에 chunk 추가 ✗ | 반복 배가 |
| exhaustion에 턴별 요약 ✗ | drift · 비용 누적 |
| 감사관이 전체 대화 요구 | growth 아님 → 별도 보관 필요<br>(다음 소절) |

![growth, duplication, loss, exhaustion, dilution 다섯 결함의 증거 문구와 처방 대응](svg/6-context-defects.svg)
*그림: 증거 문구가 명시된 결함만 골라 결함마다 다른 처방을 1:1로 적용한다.*

<sub>근거: CCAR-P-jrajath94-0149, CCAR-P-jrajath94-0151, CCAR-P-jrajath94-0293, CCAR-P-jrajath94-0296, CCAR-P-jrajath94-0348, CCAR-P-jrajath94-0411, CCAR-P-jrajath94-0412, CCAR-P-jrajath94-0475, CCAR-P-jrajath94-0538</sub>

### 1.18 Just-in-time retrieval · 원본 보관 분리

**window 확대 ✗ · working set 축소**

| 상황 | 정답 방향 |
|---|---|
| 매 호출 전체 로드, 질문은 일부만 필요<br>(논문 25편 중 2~3편 · 매뉴얼 중 한 챕터) | 관련 부분만 just-in-time retrieval |
| 긴 이력 + 비용 증가 + 혼동<br>(6개월 정비 이력 · 3시간 session · 선례 40건) | JIT retrieval + compaction<br>(중복 있으면 dedupe 추가) |
| 턴마다 token 증가 · 초기 세부 정보 필요<br>(30턴 60,000 token · 비용 3배) | 오래된 턴 = JIT retrieval<br>token 임계값에서 compaction trigger<br>→ working set 작게 유지 |
| 전체 이력 장기 보관 의무<br>(7년 · 규제 당국이 임의 session 요구) | 전체 = 비용 책정 · 상한 있는 저장소<br>active context = working set<br>필요 시 JIT 검색 |

**JIT 전제 · 한계**

| 구분 | 내용 |
|---|---|
| 보관 vs context | 보관 = 저장소의 일<br>context = working set |
| 저장소 요건 | 보관 기간 · 접근 제어 · redaction |
| 비용 | 7년치 session = 실제 비용 → 비용 책정 필요 |
| JIT 전제 | 이력이 엘리베이터 · 날짜 등으로 색인 |
| JIT 한계 | 관련 있는 오래된 기록 누락 가능<br>색인 품질 = 답 품질 상한 |
| 연결 끊김 | JIT 경로 테스트 필요<br>끊기면 이력 고립 |
| compaction trigger 전제 | 요약이 결정 · 사실 보존 |

**대안 평가**

| 대안 | 판정 |
|---|---|
| 더 큰 window | 증가 곡선 불변 · 청구서만 지연<br>예외: 매 호출 전체가 필요 + 예산 허용 |
| 더 강한 tier | 모델 계층 문제용<br>(chunk 존재 · 답 틀림일 때만) |
| 더 긴 prompt | 토큰 문제에 토큰 추가 |
| 매 턴 전체 요약 | 호출 비용 · 요약 누적 drift |
| 오래된 턴 말없이 절단 | 무엇이 빠졌는지 불투명<br>필요한 초기 세부 정보 소실 |
| 야간 요약 후 원본 삭제 | 규제 요구 증거 삭제 (요약 ≠ session) |
| 마지막 10턴만 유지 | 규제 당국 행동에 도박 |
| 전체 이력을 active context에 | 비용 · dilution 폭발 |

<sub>근거: CCAR-P-jrajath94-0147, CCAR-P-jrajath94-0150, CCAR-P-jrajath94-0293, CCAR-P-jrajath94-0349, CCAR-P-jrajath94-0411, CCAR-P-jrajath94-0474, CCAR-P-jrajath94-0537</sub>

### 1.19 Compaction 요약 계약 · 절단 지점

**임계값 = 언제 · 계약 = 무엇이 남나**

| 구분 | 내용 |
|---|---|
| compaction 경계 | 설계상 정보 손실<br>유지할 결정 · 제약을 요약에 명시 |
| 요약 계약 | 보존 항목 명시: 이름 · 결정 · 숫자 · 미해결 항목<br>체크리스트로 검증 |
| 계약 유지 | 새 사실 유형 → 계약에 추가<br>요약 형식 = 파싱 가능 |
| 임계값 조정 | 낮춤 → 손실 요약이 더 자주 → 소실 가속<br>높임 → 작동 시 같은 손실<br>내용 결함은 임계값으로 못 고침 |
| compaction 제거 | 작업 도중 window 포화 (exhaustion) |
| 대안 ✗ | 모델 기억 의존 · window 확대<br>작업 재시작 (해 둔 작업 폐기) |

**기본 요약이 초기 제약을 잃을 때**

| 구분 | 내용 |
|---|---|
| 요약 내용 | 커스텀 요약 prompt로 초기 제약 포함 요구 |
| 최근 turn 원문 유지 | 절단 지점(cut point)을 앱이 결정<br>이후 turn을 요약 block 뒤에 전송 |
| ⚠️ `keep_recent_turns` | 유지 turn 지정 파라미터 없음<br>compaction API는 beta · 시점에 따라 변함 |
| 기본 요약 신뢰 ✗ | 모든 제약 유지 보장 없음 |

<sub>근거: CCAR-F-Amey-Thakur-0033, CCAR-F-Amey-Thakur-0065, CCAR-P-jrajath94-0151, CCAR-P-jrajath94-0625</sub>

### 1.20 Case facts · 구조화 상태 레이어

**정확한 값은 요약 밖 구조화 블록에**

| 증상 | 원인 | 처방 |
|---|---|---|
| 20턴 전 "15% 할인"이 "프로모션 논의됨"으로 압축 → 틀린 값 | 요약은 정확한 세부를 잃음 | 금액 · 날짜 · 주문 번호를 `case facts` 블록으로 추출<br>요약 밖 · 매 prompt에 포함 |
| 금리 · 만기 · 담보액이 "저금리 · 담보 충분"으로 → 비교표 오류 | 사실이 요약 대상 이력에만 존재 | 값 + 출처(자료 · 페이지) 기록<br>→ 사후 검증 |
| 한 달 조사 중 정확한 기준액 · SLA % · 마감일이<br>"그럭저럭 · 높은 가용성 · 근미래"로 변질 | 반복 요약에서 정확한 값이 뭉뚱그려짐 | 요약에서 수치 · 날짜 · 조건 원문 유지 필수화<br>+ 요약 대상 아닌 구조화 scratchpad |
| 30턴+ 다중 이슈 session<br>(금액 혼동 · 해결 건 재조사) | 안건별 사실이 대화에 섞임 | 안건별 번호 · 금액 · 상태를 별도 레이어에 구조화<br>매 턴 전달 |

**처방 판정**

| 처방 | 판정 | 이유 |
|---|---|---|
| `case facts` 블록 · scratchpad | ✓ | 요약된 turn 수와 무관하게 핵심 정보 유지 |
| 요약 prompt에 원문 보존 지시 | 보조 | 열화 발생원 억제<br>scratchpad와 병행 시 정답 |
| 안건 레이어에 "고객에게 전달한 내용" 기록 | ✓ | 사람 담당자 인계 요약으로 재사용 |
| 요약 임계값 상향 (70→85%) | ✗ | 문제를 뒤로 미룰 뿐 |
| 외부 저장 + "앞서 말했듯이" 감지 검색 | ✗ | 정답 = 매 prompt에 상시 포함 |
| 의도 우선 요약 · 세부 축소 | ✗ | 열화를 의도적으로 진행 |
| 안건을 하나의 요약문으로 병합 | ✗ | 구조 붕괴 |
| 해결된 안건 turn 삭제 | ✗ | 대화 일관성 상실 |
| 원시 tool 출력을 많이 두고 늦게 요약 | ✗ | 문제 지연 |

**근본 원인 판별 단서**

| 가설 | 판정 | 이유 |
|---|---|---|
| lost in the middle | ✗ | 수치가 입력에 남아 있어야 함 |
| 앞 turn 잘림 | ✗ | 잘리면 기술 자체가 사라짐 |
| 발언 · tool 결과 혼동 | ✗ | 다른 수치가 나타남 |
| 사실이 요약 이력에만 존재 | ✓ | 후반에 남은 것 = 수치 없는 모호한 요약 |

![대화 이력에서 요약과 case facts 블록을 따로 만들어 다음 요청에 함께 넣는 구조](svg/6-compaction-case-facts.svg)
*그림: 요약은 정확한 값을 잃으므로 정확한 값은 요약 밖 case facts 블록에 두고 매 prompt에 포함한다.*

<sub>근거: CCAR-F-MyPractice-0054, CCAR-F-Udemy01-0030, CCAR-F-Udemy04-0023, CCAR-F-Udemy04-0049, CCAR-F-paullarionov-0054</sub>

### 1.21 이력 관리 방식 선택 (hybrid · retrieval)

**중요 사실 추출 + 일반 요약 + 최근 원문**

| 상황 | 정답 방향 |
|---|---|
| 78K token 요리 session<br>(알레르기 · 수량 · 선호 중요) | 하이브리드<br>중요 structured data = 추출<br>일반 논의 = 요약 · 최근 교환 = 원문 |
| 최근 25쌍만 유지 → 이전 주제 · 선호 놓침 | 오래된 메시지 요약 + 최근 메시지 원문 |
| 3개월 · 85K token 기록<br>("고립 주제 결론이 뭐였지?") | semantic embeddings로 관련 교환 on-demand 검색 |
| 단일 요리 session | 외부 저장 + semantic search<br>= architecture 과함 |

**방식별 한계**

| 방식 | 한계 |
|---|---|
| 전체 요약 | 중요한 식이 정보 등 정밀 정보 손실 위험 |
| 최근 N token만 유지<br>(rolling window) | 기록 대부분 폐기 · 중요 정보 손실 위험 |
| window 확대 (25 → 50쌍) | 같은 문제 지연 |
| vector similarity search 단독 | 현재 질의와 의미가 다른 중요 context 누락 |
| 매 턴 전체 요약 | overhead · 요약 오류 누적 |
| 점진적 summary | 구체적 결론이 추상화로 소실 |
| XML 태그로 결론 표시 | 과거 콘텐츠 전부 재구성 필요 · 검색 문제 미해결 |

<sub>근거: CCAR-F-MyPractice-0065, CCAR-F-MyPractice-0066, CCAR-F-MyPractice-0068</sub>

### 1.22 세션 이어가기 · 상태 인계

**전제 데이터 변경 시 이력 대신 판단만 인계**

| 상황 | 정답 방향 |
|---|---|
| 코퍼스 재인덱싱 · 원본 갱신 · 검토자 수정 후 재실행 | 새 session 시작<br>검증된 결과 · 판단 · 재확인 source를 구조화 요약으로 전달<br>갱신된 코퍼스로 search · analysis subagent 재실행 |
| 이력이 여전히 정확함 | continue (직전) · resume (ID 지정)<br>fork (이력 복사 후 분기) |
| 전제 변경 후 resume · fork<br>+ "옛 tool 결과 무시" 지시 | ✗ 오래된 관측을 이력째 승계<br>무시 지시로 혼입 못 막음 |
| 반복 실행 리뷰 (push마다 PR review) | 매 실행 빈 context 시작<br>→ 이전 지적을 영속화해 재실행에 전달<br>신규 · 미해결만 보고 지시 |
| 이전 지적 재확인 | 지적한 코드를 다시 검사<br>→ 남아 있는 문제만 재보고 |
| 중복 제거 vs 해결 항목 제거 | path + line 일치만으로 dedupe ✗ (미해결 은폐)<br>수동 요청 전환 ✗ (판정을 사람에게 이전) |

**이전 결과 · 결정을 후속 호출에 유지**

| 상황 | 정답 방향 |
|---|---|
| 후단 호출이 이전 subagent 지식 무시<br>(로그에 최신 지시 · 출력만 존재) | 원인 = Messages API stateless<br>요청에 포함된 내용만 모델에 보임 |
| 처방 | 관련 `messages` 배열 재전송<br>(과거 assistant 출력 · tool 결과 · 현재 user 턴)<br>또는 갱신되는 요약을 매 요청에 포함 |
| 대안 ✗ | 자동 prompt caching = 이미 보낸 prefix 처리 재사용<br>session ID 저장 + 최신 결과만 전송 = 같은 실패 |
| 초기 판단(분류체계)이 후반에 무시 | 구조화 research state file<br>(분류체계 ↔ source 매핑) → 후단 prompt에 로드 |
| 원인 | 이력이 길어 초기 판단이 tool 출력 속에 묻힘<br>(context rot: token 증가<br>→ 정확도 · recall 저하) |
| 대안 ✗ | caching · `max_tokens` 증가<br>"일반 카테고리 피하라" 지시 |

**Claude Code 장시간 session**

| 구분 | 내용 |
|---|---|
| 증상 | 이전 아키텍처 결정과 모순되는 제안 |
| 원인 | 결정이 대량 tool 출력에 묻힘 · 자동 압축으로 요약됨 |
| 대화 중에만 전달한 지시 | compaction 후 소실 가능 |
| `CLAUDE.md` (프로젝트 루트) | 항구적 설계 결정<br>`/compact` 후에도 디스크에서 재주입 |
| 구조화 facts 파일 | session 중 늘어나는 결정 · 제약<br>작업 중 참조 · 갱신 |
| 점검 질문 | "이 정보는 대화가 압축돼도 남는가?" |
| 대안 ✗ | 전문 계속 승계 · 주기적 요약<br>= 결정 보존을 대화 이력에 의존 |

<sub>근거: CCAR-F-Udemy01-0017, CCAR-F-Udemy01-0058, CCAR-F-Udemy02-0033, CCAR-F-Udemy03-0041, CCAR-F-Udemy03-0045</sub>

### 1.23 Multi-agent 간 context 반환 · 인계

**반환은 구조화 발췌 · 인계는 근거까지**

| 구분 | 내용 |
|---|---|
| 위임 이유 | context 격리<br>방대한 자료는 subagent 쪽 · 정리된 결과만 상향 |
| subagent → coordinator 반환 | 인용 · 신뢰도 붙인 구조화 발췌<br>문서 전문 = subagent context · scratchpad 파일 |
| upstream 합산 155K token<br>(synthesis 최적 입력 50K 미만) | upstream agent가 구조화 데이터 반환<br>(핵심 사실 · 인용 · 관련성 점수) |
| 미전달 대상 | 장황한 페이지 내용 · 추론 기록 |
| 해결 위치 | 근본 원인 해결 = token을 출처에서 축소 |

**반환 대안 평가**

| 대안 | 이유 |
|---|---|
| coordinator에 더 큰 window · 더 큰 모델 | 실패를 미룰 뿐 · 구조 불변 |
| 오래된 메시지 말없이 폐기 | 사라질 정보 불명 |
| 분석 재실행 후 짧은 답 선택 | 구조 불변 |
| 중간 요약 agent · 순차 batch<br>vector DB 검색 tool | 출처에서 줄이는 구조화 반환이 아님 |
| subagent 1개로 축소 · 문서 첫 페이지까지 절단 | 정리된 결과 전달이 아님 |

**후속 subagent 인계**

| 구분 | 내용 |
|---|---|
| 증상 | 후속 subagent가 완료된 검색 반복<br>제외한 source의 이유 미전달 |
| 원인 | fork형이 아니면 부모 이력 없는 새 context<br>부모가 넘기는 것 = Agent tool의 prompt 문자열뿐 |
| 정답 | 탐색 성과 + 제외 이유를 출처 링크 붙은 요약으로 응축<br>각 위임 prompt에 포함 |
| 판단 기준 | 양이 필요충분 · 판단 근거 포함 |
| 대안 ✗ | 미전달 = 현상 유지<br>최종 통합까지 보류 = 다음 단계 중복 못 막음<br>전체 기록 첨부 = context 압박 · 격리 이점 상실 |

<sub>근거: CCAR-F-Amey-Thakur-0004, CCAR-F-Amey-Thakur-0043, CCAR-F-MyPractice-0014, CCAR-F-Udemy03-0020, CCAR-F-paullarionov-0014</sub>

### 1.24 프롬프트 운영: 소유권 · 버전 관리 · drift
**프로덕션 prompt = 코드와 같은 수명주기**

| 상황 | 정답 |
|---|---|
| 프로덕션 동작을 결정하는 prompt 관리 | 코드처럼 버전 관리<br>담당자 지정 · 리뷰 · 변경 시 평가 |
| 세 팀이 유지보수해 prompt가 서로 달라짐 | 소유권 · 검토 · 변경 시 평가를 정의<br>산출물로 버전 관리 |
| 배포한 것 없이 솔루션이 나빠졌다고 보고 | 입력 · 주변 사용 방식 변화 의심<br>(분포 drift가 일반적 원인) |
| 저장한 각 답변을 하나의 prompt와 연결 | 답변마다 prompt version label 로그 |

| 구분 | 내용 |
|---|---|
| 판단 기준 | 프로덕션 동작을 결정하는 것 = 코드 수명주기 필요 |
| 중앙 독점 ✗ | 한 팀에 작성 위임 = 소유권 중앙화가 조직에 안 맞을 수 있음 |
| 동결 ✗ | 출시 후 동결 → 개선 차단 |
| 임시 수정 ✗ | 그 자리 수정 · 공유 문서 보관 → 검토 없는 변경 유발 |
| 위치 이동 ✗ | 전부 system prompt로 이동 = 거버넌스 해결 ✗ |
| drift 오진 ✗ | 모델이 이유 없이 성능 저하 ✗ · prompt는 닳지 않음<br>최초 평가는 첫 번째 의심 대상 아님 |

- ⚠️ 해설이 "(Inference)"로 표시한 항목(답변 ↔ prompt version 연결) = 공식 문서 근거 없는 운영 관행

<sub>근거: CCAR-P-Amey-Thakur-0032, CCAR-P-Amey-Thakur-0077, CCAR-P-Amey-Thakur-0078, CCAR-P-jrajath94-0619</sub>

### 1.25 프롬프트 모듈화 · 재사용 단위 선택
**복사가 병 · 버전 관리되는 단일 출처가 치료**

| 상황 | 정답 |
|---|---|
| 20개 assistant가 공통 지시를 복붙<br>정책 변경이 14개에만 반영 | 공유 지시를 버전 관리 모듈로 추출<br>(Skill · 공유 prompt component)<br>참조로 포함 → 한 번 업데이트로 전체 전파 |
| 5개 팀이 15단계 절차를 붙여넣기<br>3개 팀은 이전 버전 실행 → 금지 환불 처리 | governed Skill 하나: 이름 · 버전 · 변경 시 검토<br>배포마다 버전 pin |
| 거대 system prompt 하나에 규칙 · 어조<br>· 정책 · 고지 · 사용자 컨텍스트 혼재<br>두 팀이 서로 다른 환불 규칙 필요 | 버전 관리 모듈로 분리<br>안정 지시 = 캐시되는 system prompt<br>팀별 정책 = 모듈 · 사용자 컨텍스트 = 맨 끝 |

| 필요 | 맞는 메커니즘 | 이유 |
|---|---|---|
| 여러 팀이 반복하는 절차 | Skill | 관리 · 버전 관리되는 공유 절차 |
| 많은 prompt가 호출하는 단일 액션 | tool | 스키마가 있는 호출 가능한 단일 액션 |
| 호출자와 다른 권한이 필요한 하위 작업 | subagent | 자체 loop · tool 목록 · context |
| 권한이 아닌 안내(어조 · 단계) | prompt 모듈 | 권한 경계에는 부적합 |

| 구분 | 내용 |
|---|---|
| 실패 원인 | 중복된 진실의 원천(source of truth) |
| 버전 관리 효과 | 각 assistant가 쓴 정책 버전 감사 가능 |
| Skill 비용 | owner · 검토 · 버전 관리 필요(거버넌스 오버헤드) |
| Skill 권한 | 호출자의 범위를 받음<br>두 팀 공유 시 범위가 더 좁은 팀의 envelope 적용 |
| tool 전제 | 최소 권한 범위 설정 |
| subagent 전제 | 완전한 loop(context · 조율) · 계약 · owner |
| 시험 함정 | Skill 이름을 단 subagent<br>사실은 붙여넣은 5개 prompt인 Skill |
| 모듈 운영 전제 | 모듈 owner · version · 배포별 pin<br>silent 수정 = silent 프로덕션 변경 |
| 단순 복사가 이기는 경우 | 거의 안 바뀌는 1인 prototype<br>팀 2개 · 절차 불변 · 거버넌스 비용 > drift 비용 |

<sub>근거: CCAR-P-jrajath94-0058, CCAR-P-jrajath94-0140, CCAR-P-jrajath94-0155, CCAR-P-jrajath94-0156</sub>

### 1.26 지시 위치: CLAUDE.md vs Skill · Skill 투자 판단
**항상 필요 = CLAUDE.md · 일부 작업 절차 = Skill**

| 구분 | 내용 |
|---|---|
| CLAUDE.md | session 시작마다 context에 로드<br>항상 필요한 사실(빌드 절차 · 코딩 규약) |
| Skill | description만 항상 노출 · 본문은 호출 시 로드<br>일부 작업에만 쓰는 절차 |
| 분리 기준 | CLAUDE.md 일부가 사실 → 절차로 커지면 skill로 분리<br>자문: "모든 작업에서 항상 필요한가" |
| 정답 | 일부 작업 전용 긴 체크리스트 → `SKILL.md`<br>CLAUDE.md = 전 작업 공통 규약만 |

| 오답 | 이유 |
|---|---|
| 절차를 CLAUDE.md에 두고 "무시하라" 주석 | 로드 자체를 막지 못함 |
| 공통 규약까지 전부 skill로 이동 · CLAUDE.md 비움 | 일반 작업에 필요한 정보 소실 |
| 체크리스트를 `PreToolUse` hook으로 대체 | hook = context 로드와 무관 |

| 상황 | 정답 |
|---|---|
| 2일짜리 일회성 데이터 마이그레이션 | 평범한 prompt 텍스트 · script<br>Skill = 반복 workflow에서 제값<br>(재사용 · 버전 관리 · 유지보수) |
| 일회성에 버전 관리 Skill 제작 | 반복성 없는 모범 사례 = 과잉 설계 ✗ |
| Skill을 만들되 문서화 생략 | 유지비만 있고 재사용 이점 없음 → prompt 텍스트보다 나쁨 ✗ |
| 마이그레이션 자체를 건너뜀 | 문제 회피 · 비즈니스 요구 미충족 ✗ |

<sub>근거: CCAR-F-Udemy01-0001, CCAR-P-jrajath94-0076</sub>

### 1.27 Prompt caching과 prompt 구조 (cache hit 설계)
**안정 prefix 먼저 · 변동 모듈은 뒤**

| 상황 | 정답 |
|---|---|
| 15K token system prompt 중 12K 안정<br>3개 섹션 매일 변경 → cache hit rate ≈ 0 | 모듈로 분리 · 모듈 사이 cache breakpoint<br>안정적인 것부터 순서대로 배치<br>→ 안정 base 1회 캐시 · 변동 섹션만 재처리 |
| 요청마다 system prompt에 tenant 이름 삽입 | ✗ system 내용 변경<br>→ system · messages 캐시 무효화 |
| 캐시 유지 + 답변 ↔ prompt 연결 (2개 선택) | 안정적 지침 = 버전 관리에 저장된 하나의 system 블록<br>저장 답변마다 prompt version label 로그 |

| 오답 | 이유 |
|---|---|
| caching을 두 번 활성화해 hit rate 2배 | 불가 · 1 byte만 바뀌어도 캐시 덩어리 무효화 |
| 매일 바뀌는 섹션을 맨 앞으로 이동 | 뒤의 모든 것 캐시 오염 (안정 base 포함) |
| 변동 섹션을 prompt에서 제거 | 가격 · 정책에 대한 오답 보장 |
| 모든 내용을 user message로 이동 | 가변 user message가 앞 → prefix caching 깨짐 |
| tenant 이름을 개인화 목적으로 system에 삽입 | 개인화처럼 보여도 캐시 무효화 |
| Claude Console 자동 prompt 버전 기록 켜기 | 해설은 오답 처리(이유 설명 없음) · 정답은 답변별 version 로그 |

<sub>근거: CCAR-P-jrajath94-0074, CCAR-P-jrajath94-0140, CCAR-P-jrajath94-0619</sub>

### 1.28 절대 규칙은 prompt가 아니라 코드로 강제 (gate · filter · permission)
**prompt = 안내 · 강제 = 코드(실행 전 · fail closed)**

| 규칙 | 코드 강제 지점 |
|---|---|
| 금액 한도 (환불 > $50 · 할인 > 10%) | tool 실행 전 코드 gate<br>승인 기록 = 신뢰할 수 있는 출처 · 채팅 텍스트 ✗<br>기록 없으면 중단(fail closed) |
| 할인에 관리자 승인 필요 | 승인 gate를 tool 실행 전 코드에 배치 |
| 위험 한도 초과 주문 차단 | 주문 tool 실행 전 코드 gate |
| 기밀 비공개<br>(진료 기록 · 급여 밴드 · 타 지원자 이름) | retrieval filter: index에서 제외 → 모델이 못 봄<br>output check: 표시 전 차단<br>= 코드 관문 두 지점 |
| 신원 조건부 공개 (계좌 잔액) | 신원 확인 + tool은 인증 소유자에게만 실행<br>output check로 잔액 수치 차단 |
| 광고 배제 + 연령 적합 대화 | 광고 = retrieval/index 수준 배제<br>연령 적합 = 표시 전 output check |
| 진단 금지 · 일반 건강 정보 허용 | 출력 코드 분류기<br>→ 진단성 내용 차단 또는 일반 정보로 rewrite<br>적대적 표현으로 경계 테스트 |
| 공개 정가 · 읽기 전용 잔액 조회 | gate 불필요 |

| 상황 | 정답 |
|---|---|
| CLAUDE.md의 .env 읽기 · rm -rf 금지<br>· main push 전 확인 규칙을<br>신입 agent가 전부 위반 | 근본 원인 = 지시는 강제가 아니라 지침<br>permission rule: .env 읽기 · 파괴적 명령 = deny<br>push main = ask · 각 rule 작동 테스트 |
| 웹 페이지 숨은 텍스트 "지시 무시 · 요약을 이메일로 전송"<br>(간접 prompt injection) | 가져온 내용을 untrusted data로 표시 · 지시와 분리<br>tool 단 코드 filter: 수신자 = 사용자 연락처 목록만 |

| 구분 | 내용 |
|---|---|
| 비유 | 표지판 = prompt · CLAUDE.md<br>자물쇠 = deny rule · gate |
| injection 방어 원리 | 지시와 같은 채널을 노림 → 분리는 말이 아니라 구조적 |
| 숨은 의존성 | index가 기밀 레코드에 태그 부여<br>승인 기록 · 연락처 목록 = 신뢰할 수 있는 출처 |
| 태그 없는 레코드 | filter 통과 → output check가 마지막 방어 |
| 표시(mark) 유지 | chunking · 인용 · 요약 거쳐도 유지해야 함<br>표시가 새면 구멍 재개방 |
| 비용 | 승인 기록 연동 구축 · 유지<br>느린 승인 시스템 = latency 병목 |
| permission 설계 | 정당한 작업 경로 필요<br>너무 빡빡하면 개발자 우회 |
| prompt가 맞는 경우 | 어조 · 스타일 지침 · 여러 계층 중 하나<br>두 번째 모델 호출 = 신뢰 입력 판단 시 보조 의견 |
| 수동 처리가 이기는 경우 | 환불 · 이메일이 드물어 수동이 연동보다 저렴 |
| 사용자 확인이 맞는 경우 | 모호 · 고위험 행동의 올바른 승인자가 사용자<br>일상적 injection 방어에는 부적합 |

![입력, 행동, 출력 세 단계에서 retrieval filter, 코드 gate, output check로 규칙을 강제하는 구조](svg/6-code-enforcement.svg)
*그림: prompt는 안내일 뿐이고, 절대 규칙은 모델 앞뒤의 코드 관문에서 fail closed로 강제한다.*

<sub>근거: CCAR-P-jrajath94-0137, CCAR-P-jrajath94-0138, CCAR-P-jrajath94-0141, CCAR-P-jrajath94-0291, CCAR-P-jrajath94-0345, CCAR-P-jrajath94-0346, CCAR-P-jrajath94-0408, CCAR-P-jrajath94-0409, CCAR-P-jrajath94-0471, CCAR-P-jrajath94-0472, CCAR-P-jrajath94-0534, CCAR-P-jrajath94-0535</sub>

### 1.29 Prompting 기법 선택: 명시적 추론 · prompt chaining · 기법 사다리
**기법은 실패 메커니즘에 맞춰 · 사다리 소진 후 fine-tune**

| 상황 | 정답 |
|---|---|
| 어려운 작업 + 규제상 단계 가시화 · 검증 필요<br>(소득 · 부채 · 비율) | 명시적 추론 단계를 prompt에 요구<br>각 단계 숫자를 원본 file과 대조해 검증<br>단계 = 산출물 · 최종 답 = 그 합 |
| 서로 영향 주는 규칙 6개<br>정확도 우선 · 지연 시간 여유 | 각 규칙을 명시적 기준으로 서술<br>결정 전 단계별 추론 (또는 thinking 활성화)<br>결정 검증 |
| 한 prompt에 필드 30개 추출 · 통화 정규화<br>· 위험 분류 · 임원 요약 → 결과 불안정<br>오류 추적 곤란 | prompt chaining: 추출 → 검증 → 정규화 → 분류 → 요약<br>단계마다 고유 지시 · 점검 |
| 단순하고 모호하지 않은 작업 | zero-shot 적합 |

| 구분 | 내용 |
|---|---|
| chaining 효과 | 단계당 일 하나 · 검증 지점<br>→ 실패가 원인 단계에서 드러남 |
| 명시적 추론 비용 | 출력 token 증가(대량 호출)<br>코드 checker와 짝: 각 단계 산술 검증 |
| 단계 형식 | 파싱 가능해야 검증 가능 |
| few-shot이 이기는 경우 | 실패가 누락된 단계가 아니라 근접 오류 분류 |
| tier ↑이 이기는 경우 | 현재 tier가 산술 · 조항 파싱 자체를 못함(능력 절벽) |
| caching이 이기는 경우 | 가시성이 아니라 지연 시간이 구속 제약 |

**기법 사다리와 그 너머**

| 단계 | 내용 |
|---|---|
| 1 | zero-shot |
| 2 | few-shot 예시 |
| 3 | 거부(negative) 예시 |
| 4 | 명시적 추론 |
| 5 | 사다리 소진 → fine-tuning 또는 작업 재구성<br>(예: 라벨 분할) |

| 구분 | 내용 |
|---|---|
| 5단계 전환 조건 | 1~4 모두 시도 · 목표 97% 대비 최고 93%<br>오류에 이름 붙일 패턴 없음 · 라벨 40,000건 보유 |
| fine-tuning 비용 | 데이터 작업 · 학습 실행<br>튜닝 모델의 자체 평가 · 버전 관리 |
| 재구성 비용 | 새 라벨에 대한 이해관계자 합의 |
| 전환 전 점검 | 예시가 잘못 선택됐으면 사다리 미시도<br>라벨 정의가 모호했으면 prompt 공간 미시도 |
| 핵심 | 사다리에는 꼭대기가 있음 → 그 너머는 더 많은 prompting ✗ |

![zero-shot에서 fine-tuning까지 올라가는 기법 사다리와 각 단계의 한계](svg/6-technique-ladder.svg)
*그림: 평가를 통과하는 가장 단순한 기법에서 멈추고, 1~4단계를 소진한 뒤에만 fine-tuning이나 작업 재구성으로 간다.*

<sub>근거: CCAR-F-preporato-0028, CCAR-P-jrajath94-0145, CCAR-P-jrajath94-0146, CCAR-P-preporato-0007</sub>

## 2. 상황별 정답 판단 규칙

| 상황 | 정답 |
|---|---|
| 모든 턴에 적용할 role · 행동 · 안전 제약 위치 | system prompt (가변 입력은 user message) |
| 같은 지시, 인터페이스별 결과 상이<br>(claude.ai · Claude Code · API) | 인터페이스별로 붙는 컨텍스트 차이 이해<br>프로덕션 = API/SDK 구축 · 실제 환경 평가 |
| 내용은 맞는데 형식이 매번 다름 | 정확한 출력 예시<br>relevant · diverse 3~5개 · `<example>` 태그<br>긍정형 형식 지정 |
| 여러 제약 동시 준수 | 규칙을 지킨 출력 예시 |
| few-shot 사용 여부 | 형식 · edge-case 흔들릴 때만<br>지식 부족 · latency · 작은 창 문제 ✗ |
| 까다로운 classification few-shot | 다양한 소수 예시 · reject case<br>`<example>` 태그로 실제 입력과 분리 |
| 지시와 예시 모순 | 결과 예측 불가 → 모순 제거 |
| 스키마 검증 통과 JSON 보장 | structured outputs<br>(`output_config.format` · JSON schema) |
| 엄격한 스키마 JSON, 선택지에 structured outputs 없음 | `input_schema` tool · `tool_choice` 강제<br>→ `input` 사용 |
| prefill `{` 코드가 새 모델에서 400 error | prefill 제거 · structured outputs로 대체 |
| 추출 결과 필수 필드 가끔 누락 → 다운스트림 예외 | tool use 스키마 강제 · 결과 검증<br>validation error 붙여 retry |
| 긴 계약서 · 보고서에서 답이 관련 조항 놓침 | 문서는 태그로 감싸 위, 지시 · 질문은 끝<br>관련 조항 먼저 인용 |
| 긴 문서 여러 개를 구분 없이 연결, 질문은 앞 | 문서를 앞으로<br>문서별 `<document>` · `<source>` 태그<br>질문은 끝 |
| 가장 중요한 지시가 긴 프롬프트 한가운데 | 놓치기 쉬움 → 앞이나 끝으로 이동 |
| "혹시 몰라" 배경 자료 다량 투입 | 관련 자료와 경쟁 → 정확도 하락<br>→ 관련 자료만 |
| 장시간 assistant 반복 · 혼동 · 지시 망각<br>컨텍스트가 tool output으로 가득 | prune · 요약<br>compact<br>subagent로 isolate |
| 수백 턴 support chat이 창 상한 도달 | 오래된 턴 요약 · compaction<br>최근 턴 원문 유지 |
| 장시간 고객 대화의 session 설계 | 용건별 세션 분리<br>오래된 부분 요약 · 제거 |
| Agent tool이 원시 데이터 대량 반환<br>→ 품질 · 비용 · latency 악화 | tool 결과를 필요 항목으로 축소<br>오래된 대화 요약 |
| 자동 리뷰가 사소한 스타일 지적을 쏟아내 무시당함 | 명확한 기준 + 신호 · 잡음 경계 예시 |
| "확인하라" 류 모호 지시, 허용 패턴 지적 · 진짜 모순 누락 | 지적 조건을 명시 기준으로 재정의<br>(예: 주장 동작과 코드 모순 시만) |
| 판정 · 심각도가 PR마다 흔들림 | 측정 가능한 조건 · 심각도 수준별 코드 예시 |
| "보수적으로 · 확신도 높은 것만"으로 오탐 불변 · 누락 증가 | 보고 · 제외 범주를 검증 가능하게 정의 |
| 범주별 오탐률 편차 + 개발자 불신 | 오탐 높은 범주만 일시 비활성화<br>→ 기준 개선 → 재개 |
| 형식은 통과, 판단(단정 · 유보 · 제외)이 흔들림 | 판단 규칙 명시 + 경계 예시 |
| 근거 필드 요구 + 입력에 근거 없음 | 근거 공급 · 없으면 정보 부족으로 보류 |
| 상세 지시에도 출력 구조 · 형식 불균일 | 원하는 구조의 완성 예시 3~4개 |
| 값이 원문에 있는데 필드 null | 형식별 입출력 예시 3~5개<br>+ 필드 출현 위치 설명 |
| 비격식 표현을 추측 값으로 채움 | 비격식 표현 추출 예시 + 확인 요청 예시 |
| 상세 기준에도 오탐 · 누락 동시 | 문제 있음 · 없음 양쪽 예시 + 판단 이유 |
| 허용 패턴 판정 편차 | 허용 패턴 vs 진짜 문제 대비 예시 2~4개<br>(명백한 버그 예시 추가 ✗) |
| 예시와 다른 형태의 결함을 놓침 | 작성 방식이 다른 정례 · 부정례 + 이유 |
| 모호한 질의에서 tool 오선택 | 모호 시나리오 예시 + 선택 이유 명시 |
| 다중 이슈 요청 정확도 하락 | 분해 · routing · parameter 분리 예시 |
| 라벨 근접 오류가 대부분 | 거부 예시 few-shot |
| 학습 예산 없음 + 정확도 미달 | `<example>` 예시 3~5개 → 측정 → 필요 시 추가 |
| 규칙이 매달 바뀌고 새 학습 데이터 없음 | prompt의 규칙 · 예시 수정 + JSON schema |
| 10~15턴 후 지침 이탈 | 주기적 reminder 주입 · 규칙을 예시로 교체 |
| 지속 행동 지침 위치 | system prompt |
| 원본에 없을 수 있는 값(예: PO 번호 · 배송일) | nullable · 조건부 필수는 후단 검증 |
| 필수 필드 때문에 없는 값 날조<br>(예: 존재하지 않는 종료일) | 필드 nullable · prompt 추가 ✗<br>별도 필드와 조합해 계약 종류 판단 |
| enum 분류에서 새 유형이 기존 값으로 오분류 | `other` + 상세 필드 · `unclear` 추가<br>`other` 모니터링 → 정식 값 승격 |
| 값의 원본 위치 기록 필요 | 출처 필드를 schema에 선언 |
| 결측 표기 혼재 · 문장 규칙으로 해결 안 됨 | 예시 3~5개 + schema로 null만 허용 |
| 같은 입력인데 변환 결과 문체 · 구조 편차 | 이상적 출력 예시 + 필수 요소 · 순서 템플릿 |
| 성질이 다른 내용이 섞인 보고서 | 유형별 표현<br>(재무 = 표 · 뉴스 = 문장 · 기술 = 구조화 리스트) |
| 창고 · 하위 시스템 보호 (형태 확정 보장) | structured outputs + 전달 전 코드 validator |
| 형태 오류 재시도 루프 없이 고정 JSON | `output_config.format` schema<br>+ 파싱 전 `stop_reason` 확인 |
| 스키마 위반을 근원에서 제거 | constrained decoding<br>+ semantic 검사 · `stop_reason` 처리 별도 |
| forced tool use 거부 모델에서 enum 라벨 1개 | `auto` + strict tool use<br>또는 enum 포함 structured outputs |
| 새 모델 prefill 400 + 형식 유지 | system prompt 지시 (thinking 끄기 ✗) |
| 구문 오류 해소 후 값이 엉뚱한 필드에 입력 · 합계 불일치 | 의미 검증 코드 + 필드 `description`<br>`strict` · `tool_choice` ✗ |
| 검증 실패 후 retry | 원본 + 거부된 출력 + 구체적 validator 오류 |
| 필드 누락 · 잘못된 enum · 소스에 없는 값 동시 발생 | 세 재료를 태그로 구분해 전달 · 수정본만 반환 |
| 검증이 정보 부재로 반복 실패 | 누락 원본 제공 → 그래도 없으면 "이용 불가" 허용 |
| 소스 자체 모순(합계 전기 오류)으로 retry 한도 소진 | `stated_total` · `calculated_total`<br>· `conflict_detected` → 불일치 기록 후 사람에게 |
| 재시도 N회에도 특정 오류 0건 해소 | 입력에 정보 없음 신호 · 오류 원인별 대응 분리 |
| schema 적합 tool 호출이 업무 규칙에 거부 | `is_error: true` `tool_result` + 구체 이유<br>+ 대화 이력 유지 |
| 응답이 `max_tokens`로 끊김 + 존재하지 않는 행 번호 | 상한 상향 재시도 또는 요청 분할<br>행 번호는 참조 대상과 대조 |
| 드문 validation 실패 | 정해진 처리 경로 · 조용한 통과 차단 |
| 자기 리뷰가 미묘한 결함을 놓침 | 독립 instance · 생성 시 추론 미전달 |
| extended thinking을 늘려도 리뷰 결과 불변 | 원인 = context 공유 → 별도 session 리뷰 |
| 대형 PR 리뷰의 깊이 · 일관성 편차 | 파일별 집중 pass + 통합 pass |
| 파일별 pass 후에도 파일 간 불일치 통과 | 통합 pass 추가 |
| 예측 가능한 섹션의 긴 문서 추출 | 섹션별 추출 chain + 통합 대조 pass |
| 근거 없는 주장 · 출처 모순 + 생성 전 checkpoint 요구 | 출처 단위 리뷰 chain + 통합 pass |
| 설명 완전성이 들쭉날쭉 · 사람 감독 추가 ✗ | 초안 전 자기 비평 단계 (evaluator-optimizer) |
| 포괄적 분석 + 우선순위 구분 불가 | confidence · severity · evidence<br>schema 검증 pass + 경로 대응 규칙 |
| 오탐 많음 + 필터링 금지 + 확인 시간 병목 | 지적마다 근거 · 신뢰도 포함 |
| 확신도 임계값 결정 | 정답 라벨 데이터로 캘리브레이션 |
| 긴 실행 중 품질이 점진 하락 | 원인 = context 누적 · 관련 · 오래된 내용 경쟁<br>모델 버전 · temperature · tool 지연 ✗ |
| context 관리 실패의 조기 신호 | 같은 일 반복 · 앞선 결정과 모순 |
| 50턴+ 대화에서 지연 · 비용 증가 | 전체 이력이 매 요청에 포함 (stateless) |
| 짧은 대화인데 system prompt 지침 이탈 | assistant 응답 누적에 의한 희석 · drift |
| 비대한 system prompt (절차 수십 개) | 핵심만 system · 절차는 Skill · 검색 모듈 |
| context 증상 → 처방 선택 | 증거로 결함 이름 확정<br>(growth · duplication · loss ·<br>exhaustion · dilution) → 결함별 처방 |
| 매 호출 대량 로드 · 일부만 필요 | just-in-time retrieval (window 확대 ✗) |
| 전체 이력 장기 보관 의무 | 상한 있는 저장소에 전체 보관<br>active context = working set |
| compaction 후 이름 · 결정 소실 | 요약 계약(보존 항목 + 체크리스트) 수정<br>trigger 이동 ✗ |
| 기본 요약이 초기 제약 소실 + 최근 turn 원문 필요 | 커스텀 요약 prompt + 절단 지점 선택 |
| 요약 후 금액 · 날짜 · 조건 오류 | `case facts` 블록 · 구조화 scratchpad<br>요약 prompt 원문 보존 지시는 병행 |
| 다중 이슈 session 혼동 | 안건별 구조화 레이어 + tool 출력 필드 trim |
| tool 결과 중 일부 필드만 사용 | 입구에서 필요 필드만 반환<br>(wrapper · `PostToolUse` hook) |
| 오래된 tool 결과 정리 · 요약 호출 불가 | `clear_tool_uses` 적용<br>`exclude_tools`로 보존 tool 지정 |
| 고객 간 정보 오염 | 대화별 고객 1명으로 범위 한정 · 변경 시 격리 |
| subagent 반환으로 coordinator context 초과 | 인용 붙은 구조화 발췌 반환 · 원문은 subagent 쪽 |
| 후속 subagent의 중복 탐색 | 탐색 성과 · 제외 이유를 출처 포함 요약으로 위임 prompt에 |
| 반복 실행 리뷰의 중복 지적 | 이전 지적 영속화 · 재전달 + 재검사 → 신규 · 미해결만 보고 |
| 재색인 · 원본 갱신 후 재개 | 새 session + 검증된 판단 요약 + 갱신 코퍼스로 재실행 |
| 후단 호출이 이전 findings 무시 | `messages` 재전송 또는 갱신 요약 포함 |
| Claude Code 설계 결정 보호 | `CLAUDE.md` + 구조화 facts 파일 |
| 중요 사실 + 일반 대화가 섞인 긴 session | 하이브리드: 사실 추출 · 일반 요약 · 최근 원문 |
| 수개월 기록에서 특정 과거 결론 조회 | semantic embeddings 검색 |
| 입력 예산 내로 이력 전송 (모델 고정) | 대상 모델 ID로 사전 token 계산 → 초과 이력 절단 |
| window에 들어가는 단일 대형 문서 | 한 요청 전송 · `max_tokens` = 출력 상한 |
| 집계 입력에서 앞 · 끝만 반영, 가운데 자료 누락 | 입력 앞에 핵심 발견 · 출처 요약<br>세부는 출처 · 주제별 섹션 제목 |
| 중간 누락 + "원래 근거 유지" 요건 | 요약으로 대체 ✗ → 앞 요약 + 상세 보존 |
| 창에 들어가는 150K token 문서에서 중간 사실 누락 | retrieve-then-read<br>개요 질문 = 섹션별 map-reduce |
| 정책 매뉴얼 전체를 매 요청 붙여넣기 → 비용↑ · 정확도↓ | 임베딩 후 질문마다 상위 chunk만 투입 |
| 검색 passage 다수 · 답이 가운데 (2개 선택) | re-rank 후 소수만 전달<br>passage 앞 · 질문과 지시 끝 |
| 길고 겹치는 chunk 다수 · 중간 chunk 답 오류 | 더 적고 짧은 chunk · 구조 경계 re-chunking<br>관련성 순위 후 배치 |
| 긴 입력에서 형식 이탈 · few-shot이 잘림 (앱 측 끝 절단) | 지시 · few-shot을 user 콘텐츠 앞으로<br>⚠️ 1.6 "질문 끝" 권고와 상충 · 앱 측 절단 전제 |
| 사용자가 이미 말한 내용을 Claude가 다시 질문 | `messages` 배열에 이전 메시지 포함 (stateless) |
| 대화 중 webhook 이벤트를 다음 응답에 반영 | 다음 user message의 prefix로 주입 |
| 응답 시작 상투구 제거 (해설) | prefill<br>⚠️ 구 모델 한정<br>Claude 4.6+ prefill = 400 error |
| 프로덕션 prompt 관리 · 여러 팀 prompt 분기 | 코드처럼 버전 관리 · 소유권 · 리뷰 · 변경 시 평가 |
| 배포 없이 솔루션 품질 저하 | 입력 · 사용 방식 변화(distribution drift) 의심 |
| 공통 지시가 20개 prompt에 복붙 → 일부만 갱신 | 버전 관리 공유 모듈(Skill 등) 단일 출처 |
| 여러 팀이 같은 절차를 붙여넣고 버전 어긋남 | governed Skill · 배포마다 버전 pin |
| 반복 절차 · 단일 액션 · 다른 권한의 하위 작업 | Skill · tool · subagent 순으로 매칭 |
| 거대 prompt + 팀별 규칙 + 주간 변경 | 버전 관리 모듈 분리<br>안정 지시 = cached system prompt<br>사용자 컨텍스트 = 끝 |
| 일부 작업에만 쓰는 긴 절차가 CLAUDE.md에 있음 | `SKILL.md`로 이동 · CLAUDE.md = 공통 규약만 |
| 일회성 작업의 절차 | 평범한 prompt 텍스트 · script (Skill ✗) |
| 안정 base + 일부 섹션 매일 변경 → cache hit ≈ 0 | 안정 → 변동 순 배치 · 모듈 사이 cache breakpoint |
| 캐시 유지 + 저장 답변과 prompt 버전 연결 | 안정 system 블록 1개 · 답변마다 version 로그 |
| "절대 · 반드시" 규칙 (금액 · 승인 · 한도) | tool 실행 전 코드 gate · fail closed |
| 기밀 · 타인 정보 · 광고 · 연령 규칙 | retrieval filter + output check (코드) |
| CLAUDE.md 규칙을 agent가 위반 | permission rule(deny · ask) + 작동 테스트 |
| 신뢰 불가 내용(웹 페이지)에 숨은 지시 | untrusted data 표시 · 분리<br>+ tool 단 코드 filter |
| 어려운 작업 + 단계 검증 필요(규제) | 명시적 추론 단계 + 코드 checker로 검증 |
| 서로 영향 주는 규칙 다수 · 정확도 우선 | 규칙 명시 + 결정 전 단계별 추론(또는 thinking) |
| 한 prompt에 이질적 작업이 쌓여 불안정 | prompt chaining · 단계별 검증 |
| 사다리 소진 · 패턴 없는 오류 · 라벨 다수 | fine-tuning 또는 작업 재구성 |

![지침 배치, 인터페이스 차이, JSON 출력 관련 판단 규칙 decision tree](svg/6-rules-placement-output.svg)
*그림: 지침 위치와 JSON 출력 문제는 system prompt, 실제 환경 평가, structured outputs, 검증 후 retry로 답한다.*

![형식과 few-shot 관련 판단 규칙 decision tree](svg/6-rules-fewshot.svg)
*그림: 형식 문제는 예시로 고정하되 reject case를 넣고 지시와 모순되지 않게 하며, 지식·latency·창 문제에는 쓰지 않는다.*

![긴 문서와 context 관리 관련 판단 규칙 decision tree](svg/6-rules-context.svg)
*그림: 긴 문서는 위·질문은 끝, context는 관련 자료만 남기고 prune·compact·isolate로 관리한다.*

<sub>근거: Amey-0007, Amey-0027, Amey-0028, Amey-0029, Amey-0039, Amey-0045, Amey-0046, Amey-0061, Amey-0062, Amey-0075, Amey-0076, CCAR-F-Amey-Thakur-0004, CCAR-F-Amey-Thakur-0007, CCAR-F-Amey-Thakur-0008, CCAR-F-Amey-Thakur-0024, CCAR-F-Amey-Thakur-0032, CCAR-F-Amey-Thakur-0036, CCAR-F-Amey-Thakur-0043, CCAR-F-Amey-Thakur-0047, CCAR-F-Amey-Thakur-0048, CCAR-F-Amey-Thakur-0072, CCAR-F-Amey-Thakur-0074, CCAR-F-Amey-Thakur-0078, CCAR-F-MyPractice-0013, CCAR-F-MyPractice-0020, CCAR-F-MyPractice-0022, CCAR-F-MyPractice-0023, CCAR-F-MyPractice-0029, CCAR-F-MyPractice-0047, CCAR-F-MyPractice-0060, CCAR-F-MyPractice-0064, CCAR-F-MyPractice-0065, CCAR-F-MyPractice-0067, CCAR-F-MyPractice-0068, CCAR-F-MyPractice-0069, CCAR-F-MyPractice-0070, CCAR-F-MyPractice-0071, CCAR-F-MyPractice-0072, CCAR-F-MyPractice-0073, CCAR-F-MyPractice-0075, CCAR-F-Udemy01-0001, CCAR-F-Udemy01-0009, CCAR-F-Udemy01-0017, CCAR-F-Udemy01-0023, CCAR-F-Udemy01-0025, CCAR-F-Udemy01-0029, CCAR-F-Udemy01-0030, CCAR-F-Udemy01-0032, CCAR-F-Udemy01-0042, CCAR-F-Udemy01-0043, CCAR-F-Udemy01-0046, CCAR-F-Udemy01-0053, CCAR-F-Udemy01-0058, CCAR-F-Udemy02-0018, CCAR-F-Udemy02-0021, CCAR-F-Udemy02-0026, CCAR-F-Udemy02-0027, CCAR-F-Udemy02-0028, CCAR-F-Udemy02-0031, CCAR-F-Udemy02-0033, CCAR-F-Udemy02-0055, CCAR-F-Udemy03-0007, CCAR-F-Udemy03-0010, CCAR-F-Udemy03-0018, CCAR-F-Udemy03-0020, CCAR-F-Udemy03-0023, CCAR-F-Udemy03-0030, CCAR-F-Udemy03-0045, CCAR-F-Udemy03-0053, CCAR-F-Udemy04-0006, CCAR-F-Udemy04-0013, CCAR-F-Udemy04-0032, CCAR-F-Udemy04-0033, CCAR-F-Udemy04-0037, CCAR-F-Udemy04-0045, CCAR-F-Udemy04-0049, CCAR-F-Udemy05-0003, CCAR-F-Udemy05-0022, CCAR-F-Udemy05-0032, CCAR-F-Udemy05-0037, CCAR-F-Udemy05-0041, CCAR-F-Udemy05-0043, CCAR-F-Udemy05-0059, CCAR-F-Udemy05-0060, CCAR-F-Udemy06-0004, CCAR-F-Udemy06-0013, CCAR-F-Udemy06-0019, CCAR-F-Udemy06-0020, CCAR-F-Udemy06-0040, CCAR-F-Udemy06-0042, CCAR-F-paullarionov-0013, CCAR-F-paullarionov-0023, CCAR-F-paullarionov-0027, CCAR-F-paullarionov-0028, CCAR-F-paullarionov-0047, CCAR-F-paullarionov-0052, CCAR-F-paullarionov-0054, CCAR-F-preporato-0023, CCAR-F-preporato-0026, CCAR-F-preporato-0028, CCAR-F-preporato-0029, CCAR-P-Amey-Thakur-0032, CCAR-P-Amey-Thakur-0077, CCAR-P-Amey-Thakur-0078, CCAR-P-jrajath94-0056, CCAR-P-jrajath94-0058, CCAR-P-jrajath94-0071, CCAR-P-jrajath94-0073, CCAR-P-jrajath94-0074, CCAR-P-jrajath94-0076, CCAR-P-jrajath94-0137, CCAR-P-jrajath94-0138, CCAR-P-jrajath94-0139, CCAR-P-jrajath94-0140, CCAR-P-jrajath94-0141, CCAR-P-jrajath94-0142, CCAR-P-jrajath94-0145, CCAR-P-jrajath94-0146, CCAR-P-jrajath94-0148, CCAR-P-jrajath94-0149, CCAR-P-jrajath94-0150, CCAR-P-jrajath94-0151, CCAR-P-jrajath94-0155, CCAR-P-jrajath94-0156, CCAR-P-jrajath94-0291, CCAR-P-jrajath94-0345, CCAR-P-jrajath94-0346, CCAR-P-jrajath94-0408, CCAR-P-jrajath94-0409, CCAR-P-jrajath94-0471, CCAR-P-jrajath94-0472, CCAR-P-jrajath94-0474, CCAR-P-jrajath94-0534, CCAR-P-jrajath94-0535, CCAR-P-jrajath94-0537, CCAR-P-jrajath94-0587, CCAR-P-jrajath94-0618, CCAR-P-jrajath94-0619, CCAR-P-jrajath94-0620, CCAR-P-jrajath94-0621, CCAR-P-jrajath94-0622, CCAR-P-jrajath94-0623, CCAR-P-jrajath94-0624, CCAR-P-jrajath94-0625, CCAR-P-jrajath94-0683, CCAR-P-preporato-0007, CCAR-P-preporato-0008, CCAR-P-preporato-0009, Patrick-0004, Patrick-0026, Patrick-0041, Preporato-0020, Preporato-0021, Preporato-0022, Udemy-0012, Udemy-0015, Udemy-0020, Udemy-0022, Udemy-0024, Udemy-0042</sub>

## 3. 자주 나오는 오답 함정

**Context bloat / 장시간 세션**

| 오답 | 이유 |
|---|---|
| 더 큰 context window(1M) 모델로 옮겨 그대로 계속<br>1M 창에 전체 이력 또는 tool 원시 데이터 유지 | 같은 실패를 늦출 뿐<br>context rot · 비용 · latency 증가 |
| 매 턴 뒤에 system prompt 반복 | bloat 가속 · 지시는 이미 system prompt에 존재 |
| 모델에게 앞선 혼동을 무시하라고 요청 | 메커니즘 아님 |
| temperature를 올려 다양성 유도 | variance만 증가 · drift 미해결 |
| 응답마다 `max_tokens` 줄이기<br>`max_tokens`를 올려 창 확장<br>`max_tokens`를 올려 긴 응답을 끝까지 출력 | `max_tokens` = 출력 상한일 뿐<br>창 용량 · 누적 입력과 무관<br>올리면 창 사용 증가 |
| 상한이 가까우면 이력 없이 새 대화 시작 | 고객의 원래 문제 망각 |
| system prompt를 제거해 공간 확보 | assistant가 지켜야 할 규칙 상실 |
| 용건이 바뀌어도 같은 세션에서 이력을 깎지 않고 매번 재전송 | 무관한 이력 = 노이즈 · input token 과금 증가 |
| 대화 상태는 server에 두고 최신 메시지만 전송 | Messages API = stateless → Claude가 경위 모름 |
| 센서 데이터 tool 등록을 해제 | 핵심 기능 붕괴 · 원인 = 가공 없이 쌓이는 결과 |
| 많은 배경 자료는 정확도를 올린다<br>모델은 질문과 무관한 것은 무시한다<br>영향은 비용뿐 | 모두 ✗<br>관련 자료와 경쟁 → 정확도도 하락 |

**지침 배치**

| 오답 | 이유 |
|---|---|
| 지침을 모든 대화의 첫 user message에<br>가장 신선하도록 마지막 메시지에<br>매 user message에 반복 | configuration · input 혼재 → drift<br>입력에 의해 덮어쓰기 가능 |
| 안전 제약을 user message 쪽에 두고 질문마다 조정 | 입력 문구에 따라 약화 · 덮어쓰기 가능 |
| system prompt 없이 매번<br>user message 앞에 지시를 모아 씀 | 동작은 함<br>지침 유지보수 어려움 · 입력이 지침을 약화할 여지 |
| 질문까지 포함해 전부 system prompt에 | 신뢰할 수 없는 입력을 지침과 같은 권위로 처리 |
| 행동 지침을 tool description에 | tool description = tool 선택용 |

**인터페이스별 차이**

| 오답 | 이유 |
|---|---|
| 지시문만 자세히 고쳐서 맞춤 | 지시 바깥 컨텍스트 차이 잔존 |
| 세 곳이 같은 system prompt이니 모델 버그로 보고 | 전제 ✗ · 각각 다른 컨텍스트 부착 |
| 가장 좋은 하나만 쓰고 검증 중단 | 원인을 모른 채 환경 변경 시 같은 문제 재발 |

**Few-shot / 형식**

| 오답 | 이유 |
|---|---|
| 가장 중요한 제약을 강조 · 프롬프트 끝에 제약 반복 | 다시 말할 뿐 명확화 ✗ |
| temperature를 올려 더 많은 선택지 탐색 | variance 증가 → 신뢰성과 반대 방향 |
| 출력을 "깔끔하게(neat)" 해 달라고 요청 | 모호한 형용사 → 형식 규정 ✗ |
| 더 큰 모델 사용 | 모델은 당신의 형식을 모름 |
| few-shot 용도로<br>사실 지식 보충 · latency 감소<br>작은 context window 해결 | few-shot = 형식 · edge-case 동작을 보여 주는 도구 |
| 예시 없이 형식 설명 단락만 추가 | 항목 순서 · 표기 변형까지 세부 전달 ✗ |
| "목록으로 쓰지 마라" / "설명을 붙이지 마라" 같은 금지사항 나열 | 원하는 형태 미제시 → 긍정형으로 지정 |
| 선별 없이 메모 수십 개를 그대로 예시로<br>거의 같은 예시 50개 | 편향 · 오류 패턴 학습 · 컨텍스트 점유 |
| 모든 예시가 같은 label | 경계 학습 ✗ |
| robustness 테스트로 지시와 모순되는 예시를 넣음 | 모델이 지시를 무시하도록 학습 |
| 지시 · 예시 모순 시<br>지시가 항상 이긴다 · 예시가 항상 이긴다<br>요청이 거부된다 | 정해진 precedence 없음 · 결과 예측 불가 |

**JSON / structured output**

| 오답 | 이유 |
|---|---|
| system prompt에서 JSON으로 답하라고 지시<br>더 강하게 지시 | 확률적 → 보장 ✗ |
| temperature 0 | 결정성과 스키마 준수는 별개 |
| 자유 텍스트나 산문에서 regex로 JSON 추출 | 취약 · 보장 ✗ |
| JSON 요청 + 예시 2개 + 방어적 파싱과 retry | 확률적 · 보장 필요 시 structured outputs |
| assistant 턴을 `{`로 prefill | Claude 4.6부터 400 error<br>"`[`로 prefill"도 prefill |
| 구 모델에 영구히 머무름 | 향후 업그레이드 전부 차단 |
| try로 감싸 실패 시 빈 객체 반환 | 실패를 숨겨 다운스트림으로 전달 |
| 누락 필드를 regex 후처리로 삽입 | 가짜 데이터 생성 · 검증 후 retry가 정답 |

**긴 문서**

| 오답 | 이유 |
|---|---|
| 질문을 먼저, 그다음 문서 · 질문을 문서 한가운데 | 장문 가이드와 반대 · 문서는 위, 질문은 끝 |
| 문서를 질문 앞뒤로 두 번 | 비용 · 노이즈만 두 배 |
| 중요 지시의 위치는 상관없다<br>가운데 두면 더 잘 지켜진다<br>오류가 난다 | 오류 ✗<br>가운데 내용은 놓치기 쉬울 뿐 |
| effort를 높여 더 깊이 생각 | 비용 · latency만 증가<br>구조 · 출처 문제 그대로 |
| 보고서를 각각 사전 요약해 요약만 전달 | 세부(공통 지적 사항 등) · 출처 손실<br>입력이 이미 창에 들어가면 불필요 |
| 보고서 끝에 `cache_control` | 비용 · 속도만 개선 · 모델이 읽는 내용 그대로 |
| prompt를 두 번 돌려 겹치는 지적만 채택 | 무작위성만 제거 · 반복되는 사소한 지적 잔존 |
| 지적 개수를 임의로 제한 | 문제 많은 날 진짜 지적도 버려짐 |
| "보수적으로 · 확신도 높은 것만" 지시 | 판단 경계 불변 · 미보정 확신도<br>오탐 거의 불변 · 실제 버그 누락 증가 |
| 확신도 점수 부여 · 요약 코멘트로 집약 | 넓은 범위의 노이즈 지속<br>요약 = 표시 위치만 변경 |
| 설명 요구 · "신중하게" · 구분 축소 | 기준의 모호함을 그대로 남김 |
| 오탐 범주 때문에 리뷰 전체 중단 | 정확한 범주의 가치까지 상실 |
| 확신도 임계값 · 상위 모델 · 운영 규칙으로 신뢰 회복 | 임계값 = 미보정<br>모델 = 기준 문제를 능력 문제로 오인<br>운영 규칙 = 출력 품질 불변 |
| 일률 비지적 규칙 · 다수결 | 판단 기준 없이 결과만 조정 |
| 혼재 prompt를 줄이기 · 위치 이동 · 강조 | 지시와 데이터가 구분되지 않음 |
| null 필드에 같은 지시 강화 · 위치 이동<br>`CLAUDE.md`로 이동 | 단서(필드 출현 양상)가 늘지 않음 |
| 필드를 nullable로 변경 | 실패를 검증에서 숨김 |
| 필수 필드 강조 · 지시 강조로 추측 방지 | 단서 불변 · 필수화는 날조 부추김 |
| 근거 부족에 `max_tokens` 상향 · schema 필수화 | 길이 · 형태만 변경 · 존재하지 않는 근거 보충 불가 |
| 형식 흔들림에 강조 · 후처리 · 위임 | 지시 문장에만 의존하는 상태 유지 |
| 분류 흔들림에 규칙 추가 · 일방향 강한 규칙 · 태그 없는 대량 데이터 | 경계 미제시 · 판단 편향 · 문맥 차이 미처리 |
| 판단 편차에 JSON schema 강제 · 무관한 예시 대량 추가 | 형식은 이미 충족 · 관련성 전제 이탈 |
| 같은 형태 예시 반복 · 놓친 케이스만 추가 | 일치 목록에 머묾 |
| 정의 문장화 · 모호 지시 추가 | 예시의 문제를 해결 못 함 |
| tool 선택에 일반 예시 · 선언적 규칙 | 비교 판단 과정 전달 ✗ |
| JSON 형식 고정에 chain-of-thought | 추론용 · JSON 주변 불필요 텍스트 가능 |
| "JSON이 무엇인지" 설명 추가 | 모델은 이미 앎 · 문제는 어떤 schema인가 |
| 추출 · 형식 편차에 temperature 상향 | variance 증가 → 일관성과 반대 방향<br>⚠️ 해설 "신모델은 기본값 외 지정 불가" = 모델 버전 의존 |
| 추출 실패에 더 큰 모델 · "더 열심히" 당부 | 명세 빈틈을 겨냥 ✗ · 당부는 명세 아님 |
| 형식 · 거절 경계에 더 큰 모델 | 부족한 것은 용량이 아니라 기법 |
| "최선을 다해 보라" | 기술 범위 밖 답변 유발 |
| 경계 오류에 chain-of-thought | 모든 호출에 추론 token 추가<br>경계 제시가 필요 |
| 4포인트 차이에 라벨 50,000건 fine-tuning | 예시로 메울 수 있는 차이에 과함 |
| 이미 eval 통과한 zero-shot을 상위 기법으로 승급 | 통과하는 단계에서 멈춤 |
| schema를 서술형 설명으로 대체 | 코드 검사가 필요한 형태 |
| 학습 예산 없는데 전체 이력으로 커스텀 학습 | 자원 제약 위반 |
| 언어별 커스텀 분류기 | 규칙 변경마다 새 label · 학습 주기 필요 |
| 가장 좋아하는 기법 하나를 모든 작업에 | 오류 형태가 기법을 고름 |
| 회사 배경 3단락 · 농담조 persona를 system prompt에 | 배경 = token 비용만<br>persona = 신뢰 · 일관성 저하 |
| 변하는 정책 본문을 system prompt에 고정 | 정책은 retrieval 컨텍스트 몫 · 업데이트 복잡 |
| 행동 지침을 매 user message에 첨부<br>첫 assistant 메시지 · 환경 변수에 배치 | overhead · 모델 이탈 가능<br>환경 변수 = 모델 동작 영향 없음 |
| drift에 지침을 첫 user message로 이동<br>새 대화 시작 · 응답 후 validation | 권위 낮음 · context 소실<br>validation = 교정일 뿐 · 지연 큼 |
| 모든 필드 required<br>모든 필드 optional | 정상 문서에서도 값 날조 · 실패<br>진짜 놓친 경우 감지 불가 |
| 값 없음을 그럴듯한 기본값 · 빈 문자열 · 생략 · 메모 필드로 표현 | 날조 · 없음 vs 빈 값 구별 불가<br>기계 판독 불가 |
| 필수 종료일 날조에 prompt 추가<br>후처리 보정<br>`strict: true` | schema(필수)와 모순<br>날조를 다른 날조로 교체<br>필수 제약만 더 확실해짐 |
| enum 제거 | 값 흔들림 · 하류 처리 어려움 |
| enum에 가장 가까운 카테고리 선택 강제 | 새 유형 오분류 |
| enum 대신 자유 기술 문자열 | 정해진 값의 하류 처리 이점 상실 |
| 결측 표기 혼재에 문장 규칙 강화<br>`CLAUDE.md`로 이동 | 이미 효과 없던 방법의 연장<br>추출 pipeline 실행 context와 무관 |
| 출처 필드 요구를 큰 모델 · 긴 prompt<br>· 두 번째 pass로 해결 | 필드는 schema에 선언해야 생김 |
| 변환 지시의 단어 강조<br>`PreToolUse` hook | 해석 폭 불변<br>증상 하나만 차단 |
| 표 하나 · 템플릿 하나로 통일<br>재무 데이터를 문장으로 | 획일화 그대로<br>표현은 나눴어도 내용과 대응 틀림 |
| "JSON만 반환" prompt를 schema 대용으로 사용 | 텍스트를 제한하는 장치 없음 |
| prompt 요청 · 텍스트 파싱<br>사후 수정 · temperature 조정 | 형태를 우연에 맡김 |
| prompt 설명 · 문서화를 보장으로 착각 | 샘플링으로 형태 깨짐 · 창고는 문서를 못 읽음<br>보장은 생성 제약 + validator |
| thinking 끄기로 prefill 400 해결 | 마지막 assistant 턴 prefill 자체가 400 |
| forced tool use 거부 모델에서<br>이름 지정 `tool_choice` | 400 error |
| regex로 스키마 위반 복구 | 의도 추측 → 데이터 조용히 손상 |
| 구문 오류 해소 후<br>`strict: true` · `tool_choice` 강제<br>schema 제거 | 형식 쪽 조작 · 이미 충족된 조건 강화 |
| schema만 믿고 행 번호 · 인용 검증 생략 | 의미 오류 방치 |
| 합계를 시스템이 직접 계산<br>같은 추출 2회 실행해 결과 일치만 확인 | 오류가 가려짐<br>일관된 오류를 놓침 |
| 재시도 문구 "다시 하라" · "무효한 JSON 수정"<br>"주의하라" | 무엇이 틀렸는지 전달 ✗ |
| 재시도에서 원본 제외<br>같은 조건 반복<br>모델만 교체 | 교정 재료 소실<br>오류를 낳은 조건 그대로<br>무엇이 잘못됐는지 미전달 |
| 재시도 횟수 · 상한 인상 | 소스에 없는 정보 · 소스 모순에는 무효 · 비용만 증가 |
| 소스 불일치를 덮어쓰기 · 문서 폐기 | 소스 모순이라는 사실 소실 |
| 존재하지 않는 정보에 재시도 · strict · few-shot | 없는 정보를 모델이 채우게 함 |
| 드문 validation 실패 무시<br>validation 끄기 | 잘못된 데이터 조용히 통과 |
| 경계 validation의 이유를 비용 절감 · 정확도 향상으로 설명 | 핵심 = 결함 확산 방지 |
| 업무 규칙 거부를 조용히 삭제<br>일반 지시로 대체<br>`failed`만 반환 | 이번 오류를 Claude에 알릴 경로 없음 |
| `max_tokens` 중단을 `pause_turn`으로 처리 | `pause_turn` = 서버 tool loop 일시 정지 |
| 같은 session 안 보강<br>extended thinking · effort 상향 · 재리뷰<br>`/compact` · 근거 재독 · resume | 생성 시 전제 공유 · 독립성 없음 |
| "회의적으로 보라" 촉구 · 합성 메시지 삽입<br>확신도 필드 추가 | 같은 문맥 안에 머묾<br>대조 구조 아님 |
| 별도 instance에 생성 시 대화 기록 전달 | 독립성 소실 |
| 기존 이력에서 셀프 리뷰 유지<br>통합 1회가 검사까지 겸임 | 같은 전제 공유 · 놓치는 부분 발생 |
| diff · 파일 전체를 single-pass 리뷰<br>한 큰 prompt에 전부 | 주의 분산 · 깊이 편차 |
| 통합 리뷰만 수행<br>통합 없는 병렬 리뷰 · 파일별 pass만 | 국소 결함 누락<br>파일 간 문제 누락 |
| 경로 선택을 모델에 맡기는 자율 조사 | 고정 절차 요건과 반대 |
| 요약을 거친 추출<br>동적 분해 | 세부 정보 손실<br>예측 가능한 구조에는 과함 |
| 확신도 점수 · 동일 리뷰어 다수결 · 긴 체크리스트 | 긴 묶음을 한 번에 처리하는 구조 불변 |
| 높은 확신도만 남김<br>API 응답의 확신도 사용 | 포괄성 상실<br>존재하지 않는 값에 의존 |
| 근거 없는 건수 제한 · 일반 prompt 지시<br>같은 session의 미캘리브레이션 수치 | 실제 데이터의 뒷받침 없음 |
| 지적을 개발자에게 보이기 전 필터링 | 제시된 조건(필터링 반대) 위반 |
| 더 큰 window · 더 강한 tier로 context 문제 해결 | 증가 곡선 · 희석 · 중복 불변<br>tier = 모델 계층 문제용 |
| 더 긴 system prompt로 혼동 해결 | 토큰 문제에 토큰 추가 |
| 오래된 turn을 말없이 절단 | 손실 대상 불투명 · 초기 핵심 정보 소실 |
| 매 턴 전체 이력 요약 | 호출 비용 · 요약 오류 누적 |
| trigger 임계값 조정으로 나쁜 요약 교정 | 임계값 = 시점 · 요약 내용 불변 |
| compaction 제거 | 작업 도중 window 포화 |
| 모델이 중요한 내용을 기억하리라 기대 | compaction은 설계상 손실 |
| 작업을 처음부터 재시작 | 해 둔 작업 폐기 |
| `keep_recent_turns`로 최근 turn 유지 | 해당 파라미터 없음 · 절단 지점으로 제어 |
| 요약 임계값 70% → 85% 상향 | 손실을 뒤로 미룰 뿐 |
| 외부 저장 + "앞서 말했듯이" 감지 검색 | 정답 = 매 prompt에 상시 포함되는 case facts |
| 의도 우선 요약 · 세부 축소 | 열화를 의도적으로 진행 |
| 안건을 하나의 요약문으로 병합 | 구조 붕괴 |
| 해결된 안건 turn 삭제 | 대화 일관성 상실 |
| tool 결과를 쌓은 뒤 context editing만 적용 | 대증요법 · payload 크기 원인 미해결 |
| 이전 tool 결과 전부 삭제 | 필요한 사실 손실 |
| tool 반환 건수 증가로 호출 수 감소 | 쌓이는 총량 불변 |
| 대화 앞에서부터 절단 | 초반 핵심 정보 손실 |
| 매 턴 별도 요약 요청 | 추가 모델 호출 · 요약 호출 배제 제약 위반 |
| 토큰 계산 endpoint로 이력 삭제 | 계산 도구 · 삭제는 `clear_tool_uses` |
| 응답 `usage` 필드로 사전 예산 확인 | 호출 후에 도착 |
| `effort` low로 입력 token 감소 | 오답 보기 (입력 token 감소 수단으로 제시) |
| `max_tokens`를 1,000,000으로 올려 window 확보 | 출력만 제한 |
| 고객 신원에 주의하라는 지시 | 결함 = context 범위 설정 · window 크기 ✗ |
| resume · fork + "옛 결과 무시" 지시 | stale 관측 이력째 승계 · 혼입 못 막음 |
| path + line 일치만으로 dedupe | 미해결 문제까지 은폐 |
| 리뷰를 수동 요청으로 전환 | 판정 부담을 사람에게 이전 |
| prompt caching으로 이전 지식 유지 | 이미 보낸 prefix 재사용 · 미전송 보충 ✗ |
| session ID 저장 + 최신 결과만 전송 | 현재 실패 재현 |
| 전문 승계 · 주기적 요약으로 결정 보호 | 보존을 대화 이력에 의존 |
| subagent 원문 반환 후 coordinator window 확대 | 실패 지연 · 구조 불변 |
| 중간 요약 agent · 순차 batch<br>vector DB 검색 tool | 출처에서 줄이는 구조화 반환이 아님 |
| 후속 subagent 인계에 전체 기록 첨부 | context 압박 · 격리 이점 상실 |
| vector search 단독 (지속 선호 유지) | 의미가 다른 중요 context 누락 |
| 감사 요구를 JIT 검색만으로 대응 | 전체 필요 → 별도 보관 |
| 야간 요약 후 원본 삭제 | 규제 요구 증거 삭제 |
| 절차 40개를 별도 assistant로 분리 · 대문자 강조 | 라우팅 사용자 전가 · prompt 미축소 |
| 중간 누락에 `max_tokens` ↑<br>끝에 "모든 발견 검토" 체크리스트 추가 | 출력 상한일 뿐 · 입력 구조(원인) 불변 |
| 실행마다 결과 순서를 무작위 재배열 · 순환 | 누락되는 위치만 이동 |
| 중간 자료를 출처 없는 요약으로 대체<br>모든 subagent 출력을 사전 요약 | 원래 근거 · 출처 손실 |
| 출처 URL만 끝 부록으로 이동 · 근거를 한 덩어리로 | 근거 구조 불변 |
| 완료 순 연결 + 모델이 주제 추론 | 현상 유지 · 위치 문제 그대로 |
| 더 큰 window · passage · chunk 수 2배 | 가운데 구간만 길어짐 · dilution · 비용↑<br>lost-in-the-middle 미해결 |
| 긴 context 누락에 temperature 조정 | 무작위성 제어 · attention과 무관 |
| 같은 질문 3회 다수결 | 같은 누락을 3번 반복 |
| 중간 섹션 글꼴 키우기 | 사람이 읽는 것 ≠ 모델 처리 · attention 무관 |
| 문서를 chunk로 나눠 무작위 chunk 하나로 답 | 답이 없을 가능성 높음 |
| 매뉴얼을 두 번 붙여넣기 | 비용 2배 · 새 정보 없음 |
| 중간 chunk 누락에 명시적 추론 추가 · 더 유능한 tier | 추론할 사실이 시야에 없음<br>부풀려진 context 중간은 여전히 놓침 |
| 형식 이탈에 few-shot 추가 · 예시를 메시지 중간에 삽입 | 여전히 절단 지점 뒤 · 긴 콘텐츠 하류 |
| 형식 보호하려 사용자 이메일을 축소 | 실제 작업 입력 제거 |
| 재질문 원인을 vector DB · `session_id` 필요로 진단 | Claude에 server 측 memory 없음<br>둘 다 Claude architecture 아님 |
| 프로덕션 prompt를 한 팀에 독점 · 동결<br>그 자리 수정 · 공유 문서 보관 | 중앙화 부적합 · 개선 차단 · 검토 없는 변경 유발 |
| 배포 없는 품질 저하를 모델 저하<br>· prompt 마모 · 최초 평가 탓으로 진단 | 모델은 이유 없이 저하 ✗ · prompt는 닳지 않음<br>최초 평가는 첫 의심 대상 아님 |
| 공유 지시를 더 조심스럽게 복붙 · 한 사람이 20개 prompt 암기<br>20개 assistant를 mega-prompt 하나로 합침 | 복붙 = 다음 변경에 재drift · 사람 기억 ≠ 구성 관리<br>도메인별 튜닝 파괴 · 유지 불가 |
| 새 절차를 팀에 이메일로 요청<br>링크 달린 6번째 prompt 작성<br>절차 삭제 후 수동 처리 | 이메일은 이미 실패 · 링크는 낡고 구속력 없음<br>삭제 = 설계 ✗ · 자동화 소멸 |
| 거대 prompt에 주석만 추가<br>전부 user message로 이동<br>거대 prompt로 fine-tuning | 팀 규칙 충돌 지속 · prefix caching 깨짐<br>이번 주 규칙을 weight에 고정 → 재학습 · 팀별 모델 필요 |
| 권한 경계를 지시문 더 많은 prompt 모듈로 해결 | 산문으로 tool 목록을 가둘 수 없음 |
| 일부 작업 절차를 CLAUDE.md에 두고 "무시" 주석<br>공통 규약까지 skill로 이동<br>`PreToolUse` hook으로 대체 | 로드 자체를 못 막음<br>일반 작업 정보 소실 · hook은 로드와 무관 |
| 일회성 작업에 버전 관리 Skill · 문서 없는 Skill | 반복성 없는 과잉 설계 · 유지비만 존재 |
| caching 두 번 활성화 · 변동 섹션을 앞으로 · 변동 섹션 삭제<br>요청마다 system에 tenant 이름 삽입 | 1 byte 변경에도 무효화 · 뒤 전체 캐시 오염<br>오답 보장 · system 캐시 · messages 캐시 무효화 |
| system prompt 문구 강화 · 규칙 반복<br>더 긴 prompt | 지침일 뿐 · 압박 · injection이면 무시 가능<br>표지판 3개도 표지판 |
| 두 번째 model 호출로 규칙 준수 검사 | 같은 위조 메모를 읽음 · 검사는 입력 출처만큼만 강함 |
| 더 높은 tier로 전환 · 신입 접근 권한 회수 | 같은 지침을 읽음 · 메커니즘 문제<br>다음 신입이 같은 비강제 설정에 부딪힘 |
| tool 제거 · 모든 환불을 수동 처리 · 사용자에게 매번 확인 요구 | 정당한 사용 소멸 · 삭제 ≠ 설계<br>사용자가 그냥 클릭 → 코드 문제를 주의력 문제로 전환 |
| 모델이 기밀 주제를 싫어하도록 fine-tune | 요청마다 보장 증명 ✗ · 감사 불가 |
| 승인 · 기밀 판단을 모델에 위임 · 통제 없음 · "모델을 신뢰" | 돈 · 기밀을 모델 순응에 의존 · 희망은 통제 아님 |
| "페이지 내 지시 따르지 마라"를 system prompt 한 줄로 방어 | 주입 텍스트가 지침을 덮어씀 · 요약하려면 읽어야 함 |
| 규제 단계 요구에 few-shot 20개<br>더 큰 tier · 신청서 caching | 예시는 요청 안 한 단계를 못 만듦<br>tier는 단계를 숨김 · caching은 지연 조치 |
| 규칙 다수 작업에 temperature ↓<br>규칙 없이 few-shot만 · 짧은 zero-shot | 추론 추가 ✗ · 규칙은 명시 필요<br>zero-shot = 단순 작업용 |
| 한 prompt에 `IMPORTANT` 표시<br>더 강한 모델 · 요약을 먼저 요청 | 일의 수 불변 · 오류 추적 불가<br>미검증 필드로 요약 작성 |
| 93% 정체에 few-shot 30개 추가<br>tier ↑ · 라벨 정의 재작성 | 12개가 실패한 곳에 반복<br>능력 결함 증거 없음 · 5번째 prompt 재작성 |

<sub>근거: Amey-0007, Amey-0027, Amey-0028, Amey-0029, Amey-0039, Amey-0045, Amey-0046, Amey-0061, Amey-0062, Amey-0075, Amey-0076, CCAR-F-Amey-Thakur-0004, CCAR-F-Amey-Thakur-0007, CCAR-F-Amey-Thakur-0008, CCAR-F-Amey-Thakur-0023, CCAR-F-Amey-Thakur-0024, CCAR-F-Amey-Thakur-0025, CCAR-F-Amey-Thakur-0027, CCAR-F-Amey-Thakur-0033, CCAR-F-Amey-Thakur-0036, CCAR-F-Amey-Thakur-0043, CCAR-F-Amey-Thakur-0048, CCAR-F-Amey-Thakur-0058, CCAR-F-Amey-Thakur-0059, CCAR-F-Amey-Thakur-0060, CCAR-F-Amey-Thakur-0065, CCAR-F-Amey-Thakur-0072, CCAR-F-Amey-Thakur-0073, CCAR-F-Amey-Thakur-0074, CCAR-F-MyPractice-0013, CCAR-F-MyPractice-0027, CCAR-F-MyPractice-0060, CCAR-F-MyPractice-0064, CCAR-F-MyPractice-0066, CCAR-F-MyPractice-0069, CCAR-F-MyPractice-0071, CCAR-F-Udemy01-0001, CCAR-F-Udemy01-0009, CCAR-F-Udemy01-0017, CCAR-F-Udemy01-0023, CCAR-F-Udemy01-0025, CCAR-F-Udemy01-0030, CCAR-F-Udemy01-0032, CCAR-F-Udemy01-0033, CCAR-F-Udemy01-0042, CCAR-F-Udemy01-0043, CCAR-F-Udemy01-0046, CCAR-F-Udemy01-0053, CCAR-F-Udemy01-0058, CCAR-F-Udemy02-0001, CCAR-F-Udemy02-0018, CCAR-F-Udemy02-0021, CCAR-F-Udemy02-0026, CCAR-F-Udemy02-0027, CCAR-F-Udemy02-0028, CCAR-F-Udemy02-0031, CCAR-F-Udemy02-0033, CCAR-F-Udemy02-0051, CCAR-F-Udemy02-0055, CCAR-F-Udemy02-0056, CCAR-F-Udemy02-0058, CCAR-F-Udemy03-0007, CCAR-F-Udemy03-0010, CCAR-F-Udemy03-0018, CCAR-F-Udemy03-0020, CCAR-F-Udemy03-0023, CCAR-F-Udemy03-0025, CCAR-F-Udemy03-0030, CCAR-F-Udemy03-0045, CCAR-F-Udemy03-0048, CCAR-F-Udemy03-0053, CCAR-F-Udemy04-0003, CCAR-F-Udemy04-0006, CCAR-F-Udemy04-0013, CCAR-F-Udemy04-0032, CCAR-F-Udemy04-0033, CCAR-F-Udemy04-0037, CCAR-F-Udemy04-0045, CCAR-F-Udemy04-0049, CCAR-F-Udemy05-0001, CCAR-F-Udemy05-0003, CCAR-F-Udemy05-0022, CCAR-F-Udemy05-0032, CCAR-F-Udemy05-0037, CCAR-F-Udemy05-0041, CCAR-F-Udemy05-0043, CCAR-F-Udemy05-0059, CCAR-F-Udemy05-0060, CCAR-F-Udemy06-0004, CCAR-F-Udemy06-0013, CCAR-F-Udemy06-0019, CCAR-F-Udemy06-0020, CCAR-F-Udemy06-0021, CCAR-F-Udemy06-0035, CCAR-F-Udemy06-0040, CCAR-F-Udemy06-0042, CCAR-F-paullarionov-0013, CCAR-F-paullarionov-0014, CCAR-F-paullarionov-0027, CCAR-F-paullarionov-0028, CCAR-F-paullarionov-0054, CCAR-F-paullarionov-0060, CCAR-F-preporato-0026, CCAR-F-preporato-0028, CCAR-F-preporato-0029, CCAR-P-Amey-Thakur-0032, CCAR-P-Amey-Thakur-0077, CCAR-P-Amey-Thakur-0078, CCAR-P-jrajath94-0053, CCAR-P-jrajath94-0054, CCAR-P-jrajath94-0056, CCAR-P-jrajath94-0058, CCAR-P-jrajath94-0071, CCAR-P-jrajath94-0073, CCAR-P-jrajath94-0074, CCAR-P-jrajath94-0076, CCAR-P-jrajath94-0137, CCAR-P-jrajath94-0138, CCAR-P-jrajath94-0139, CCAR-P-jrajath94-0140, CCAR-P-jrajath94-0141, CCAR-P-jrajath94-0142, CCAR-P-jrajath94-0144, CCAR-P-jrajath94-0145, CCAR-P-jrajath94-0146, CCAR-P-jrajath94-0147, CCAR-P-jrajath94-0148, CCAR-P-jrajath94-0149, CCAR-P-jrajath94-0150, CCAR-P-jrajath94-0151, CCAR-P-jrajath94-0155, CCAR-P-jrajath94-0156, CCAR-P-jrajath94-0291, CCAR-P-jrajath94-0292, CCAR-P-jrajath94-0293, CCAR-P-jrajath94-0345, CCAR-P-jrajath94-0346, CCAR-P-jrajath94-0408, CCAR-P-jrajath94-0409, CCAR-P-jrajath94-0471, CCAR-P-jrajath94-0472, CCAR-P-jrajath94-0534, CCAR-P-jrajath94-0535, CCAR-P-jrajath94-0587, CCAR-P-jrajath94-0618, CCAR-P-jrajath94-0619, CCAR-P-jrajath94-0620, CCAR-P-jrajath94-0621, CCAR-P-jrajath94-0622, CCAR-P-jrajath94-0623, CCAR-P-jrajath94-0624, CCAR-P-jrajath94-0625, CCAR-P-jrajath94-0683, CCAR-P-preporato-0007, CCAR-P-preporato-0008, CCAR-P-preporato-0009, Patrick-0004, Patrick-0026, Patrick-0041, Preporato-0020, Preporato-0021, Preporato-0022, Udemy-0012, Udemy-0015, Udemy-0020, Udemy-0022, Udemy-0024, Udemy-0042</sub>

## 4. 암기 목록

| 이름 | 의미 |
|---|---|
| System prompt | 대화 전체에 적용할 안정적 지침(role · 행동 · 안전 제약)<br>API의 top-level `system` 파라미터 |
| Few-shot (multishot) | 소수 예시 3~5개 · relevant · diverse<br>경계 · reject case 포함, `<example>` 태그로 분리<br>용도 = 형식 · edge-case |
| Structured outputs | `output_config.format`에 JSON schema<br>→ constrained decoding · 스키마 준수 보장<br>prefill의 대체재(대안 ✗) |
| Prefill | assistant 턴 시작을 미리 채우는 구 기법<br>Claude 4.6부터 마지막 assistant 턴 prefill<br>→ 400 error |
| Forced tool choice | `input_schema`가 목표 JSON인 tool<br>`tool_choice`로 호출 강제<br>`input`을 구조화 객체로 사용 |
| Validation-retry loop | 결과 검증 → 실패 시 validation error 붙여 retry<br>출력 = untrusted input |
| Long-context 배치 | 문서는 태그로 감싸 위, 질문은 끝 · 먼저 인용<br>(약 20K+ tokens, 최대 30% 향상) |
| `<document>` · `<document_content>` · `<source>` | 여러 문서를 하나씩 감싸고 본문 · 출처를 분리하는 XML 태그 |
| Lost in the middle | 긴 입력 한가운데 내용 → 가장자리보다 놓치기 쉬움 |
| Context rot | token 증가 → 앞서 읽은 내용을 정확히 끌어오지 못하는 현상 |
| Compaction | 오래된 턴 → server 측 요약으로 대체<br>최근 턴 원문 유지 |
| Context editing | 오래된(stale) tool result 제거 |
| Prune · Compact · Isolate<br>(context hygiene 3원칙) | prune = tool output 자르기 · 요약<br>compact = 이력 압축<br>isolate = subagent · 세션으로 분리 |
| `max_tokens` | 응답 1회의 출력 상한 · context window와 무관 |
| Effort | thinking · 응답에 쓰는 token 양 조절<br>프롬프트 구조 문제 해결 ✗ |
| `cache_control` (prompt caching) | 같은 접두부 재전송 시 비용 · 속도 개선<br>모델이 읽는 내용 불변 |
| 명시적 기준 | 보고할 것 · 건너뛸 것 · 최소 심각도를 측정 가능하게 쓴 지시 |
| 경계 예시 | 문제 있음 · 없음 양쪽을 판단 이유와 함께 보여 주는 예시 |
| Negative(거부) 예시 | 건드리지 말아야 할 사례를 보여 주는 예시<br>근접 오류 · 오탐 경계 학습용 |
| 미보정 확신도 | 모델 자기 보고 확신도<br>필터 기준으로 신뢰 ✗ |
| 범주별 오탐률 | 카테고리별 기각 비율<br>높은 범주 = 일시 비활성화 대상 |
| 근접 오류(near-miss) | 라벨 경계에서의 혼동 오류 → 거부 예시 |
| Instruction drift | 대화 누적 후 system prompt 지침 이탈<br>처방 = 주기적 reminder · 규칙을 예시로 교체 |
| 평가를 통과하는 가장 단순한 기법 | 기법 선택 원칙 · 통과하면 승급 ✗ |
| Nullable 필드 | 원본에 없을 수 있는 값을 `null`로 표현<br>→ 진짜 없음 vs 추출 실패 구분 |
| `other` + 상세 필드 | 확장 가능한 enum 설계<br>미분류 입력의 오분류 방지 · 내용 보존 |
| `unclear` | 분류 판단 불가 수용 값 → 사람 리뷰 |
| 의미 검증 (semantic validation) | schema 밖 코드로 값 · 필드 간 정합성 확인 |
| 재시도 3재료 | 원본 문서 · 거부된 JSON · validator 구체 오류 |
| `is_error: true` | 실패한 `tool_result` 표시<br>구체적 이유와 함께 반환 |
| `stated_total` · `calculated_total`<br>· `conflict_detected` | 소스 기재 합계 · 계산 합계 · 불일치 플래그<br>→ 소스 모순을 기록한 채 사람에게 |
| `stop_reason: "max_tokens"` | 응답이 상한에서 끊김 · schema 준수 보장 ✗ |
| `pause_turn` | 서버 tool loop 일시 정지 |
| Attention dilution | 한 pass에 너무 많이 넣을 때 주의가 분산되는 현상 |
| 국소 pass · 통합 pass | 파일(섹션)별 집중 분석 · 파일 간 데이터 흐름 분석 |
| Prompt chaining | 작업을 고정 단계로 나눠 출력을 다음 단계에 전달 |
| Evaluator-optimizer | 생성 → 기준 평가 → 피드백 반영 패턴 |
| Writer/Reviewer 패턴 | 한 session이 작성 · 다른 session이 리뷰 |
| Confidence calibration | 확신도를 정답 라벨 데이터로 보정해 임계값 결정 |
| `--output-format json` + `--json-schema` | Claude Code 출력을 schema로 구조화 |
| Context leak 5종 | growth · duplication · loss ·<br>exhaustion · dilution<br>증상마다 처방이 다름 |
| Working set | active context에 두는 작은 집합<br>원본은 상한 있는 저장소 |
| Just-in-time retrieval | 필요한 순간 관련 부분만 로드 |
| 요약 계약 | compaction 요약이 보존할 항목 명시<br>(이름 · 결정 · 숫자 · 미해결 항목) + 체크리스트 |
| 절단 지점 (cut point) | 요약 대상과 원문 유지 turn의 경계 |
| `case facts` 블록 | 거래 사실을 요약 밖에 둔 구조화 블록<br>매 prompt에 포함 |
| Scratchpad · state file | 요약 대상 아닌 외부 기록<br>필요할 때 다시 읽어 들임 |
| continue · resume · fork | 직전 이어가기 · ID로 재개 · 이력 복사 분기 |
| ⚠️ `clear_tool_uses_20250919` | context editing 전략 (beta · 시점에 따라 변함)<br>옵션 trigger · `keep` · `exclude_tools` |
| ⚠️ `context-management-2025-06-27` | context editing beta header |
| 토큰 계산 endpoint | 전송 전 입력 token 확인 (대상 모델 ID 사용) |
| 하이브리드 이력 | 중요 사실 추출 + 일반 논의 요약 + 최근 원문 |
| Retrieve-then-read | 검색으로 관련 섹션만 → 작은 집합에서 추론<br>개요 질문 = 섹션별 map-reduce 요약 |
| 지식 맵 | 집계 입력 맨 앞의 핵심 발견 · 출처 간결 목록<br>세부는 출처 · 주제 섹션 제목 아래 |
| Primacy effect | 입력 앞부분 정보가 안정적으로 처리<br>→ 핵심 요약을 앞에 배치 |
| Dilution | context가 많을수록 쓸 수 있는 지식 감소<br>사실이 없는 recall 결함과 구분 |
| Distribution drift | 입력 분포 변화로 배포 없이 동작 변화 |
| Governed Skill | 이름 · 버전 · 변경 시 검토 · owner<br>배포마다 version pin · 단일 출처 |
| 재사용 단위 | 반복 절차 = Skill · 단일 액션 = tool<br>자체 권한 · loop 하위 작업 = subagent |
| CLAUDE.md vs Skill | 항상 로드되는 사실 vs 호출 시 로드되는 절차 |
| Cache breakpoint 순서 | 안정 모듈 → 변동 모듈 · 모듈 사이 breakpoint |
| Code gate · fail closed | tool 실행 전 코드 검사 · 검증 실패 시 실행 중단 |
| Retrieval filter · Output check | 모델 접촉 전 제외 · 표시 전 차단 |
| Permission rule (deny · ask) | tool 실행 전 검사 · 지시(CLAUDE.md)와 구분 |
| Untrusted data 표시 | 가져온 내용 = 데이터 · 지시와 구조적 분리<br>tool 단 filter 병행 |
| 기법 사다리 | zero-shot → few-shot → 거부 예시 → 명시적 추론<br>→ 소진 시 fine-tuning · 작업 재구성 |
| Prompt chaining | 단일 책임 prompt 연결 · 단계마다 고유 지시 · 점검 |

<sub>근거: Amey-0007, Amey-0039, Amey-0045, Amey-0046, Amey-0076, CCAR-F-Amey-Thakur-0008, CCAR-F-Amey-Thakur-0025, CCAR-F-Amey-Thakur-0033, CCAR-F-Amey-Thakur-0059, CCAR-F-MyPractice-0013, CCAR-F-MyPractice-0065, CCAR-F-MyPractice-0069, CCAR-F-MyPractice-0070, CCAR-F-Udemy01-0001, CCAR-F-Udemy01-0009, CCAR-F-Udemy01-0017, CCAR-F-Udemy01-0023, CCAR-F-Udemy01-0025, CCAR-F-Udemy01-0029, CCAR-F-Udemy01-0030, CCAR-F-Udemy01-0053, CCAR-F-Udemy02-0018, CCAR-F-Udemy02-0021, CCAR-F-Udemy02-0026, CCAR-F-Udemy03-0007, CCAR-F-Udemy03-0010, CCAR-F-Udemy03-0018, CCAR-F-Udemy03-0023, CCAR-F-Udemy03-0025, CCAR-F-Udemy03-0030, CCAR-F-Udemy04-0023, CCAR-F-Udemy04-0037, CCAR-F-Udemy04-0045, CCAR-F-Udemy05-0001, CCAR-F-Udemy05-0022, CCAR-F-Udemy05-0037, CCAR-F-Udemy06-0019, CCAR-F-Udemy06-0021, CCAR-F-Udemy06-0040, CCAR-F-paullarionov-0013, CCAR-F-paullarionov-0027, CCAR-F-paullarionov-0052, CCAR-F-preporato-0023, CCAR-F-preporato-0024, CCAR-F-preporato-0028, CCAR-P-Amey-Thakur-0077, CCAR-P-jrajath94-0056, CCAR-P-jrajath94-0074, CCAR-P-jrajath94-0137, CCAR-P-jrajath94-0138, CCAR-P-jrajath94-0141, CCAR-P-jrajath94-0142, CCAR-P-jrajath94-0144, CCAR-P-jrajath94-0146, CCAR-P-jrajath94-0148, CCAR-P-jrajath94-0149, CCAR-P-jrajath94-0150, CCAR-P-jrajath94-0151, CCAR-P-jrajath94-0155, CCAR-P-jrajath94-0156, CCAR-P-jrajath94-0293, CCAR-P-jrajath94-0345, CCAR-P-jrajath94-0623, CCAR-P-jrajath94-0625, Patrick-0004, Patrick-0026, Patrick-0041, Preporato-0020, Preporato-0021, Preporato-0022, Udemy-0012, Udemy-0020, Udemy-0022, Udemy-0024, Udemy-0042</sub>

## 5. 시험 직전 체크리스트

- [ ] 안정적 지침 = system prompt, 가변 입력 = user message
- [ ] tool description = tool 선택용 · 행동 지침용 ✗
- [ ] 인터페이스별 출력 차이 = 붙는 컨텍스트 차이
- [ ] 프로덕션 = API/SDK 구축 · 실제 환경 평가
- [ ] 형식 불일치 → relevant · diverse 예시 3~5개
- [ ] 예시는 `<example>` 태그로 분리
- [ ] few-shot → 지식 · latency · 창 크기 문제 해법 ✗
- [ ] 형식은 긍정형("~형식으로") 지정
- [ ] few-shot classification → reject case 포함 · 예시와 입력 분리
- [ ] 지시 vs 예시 모순 → 결과 예측 불가 (precedence 없음)
- [ ] 강조 · 반복 · temperature 조정 · 큰 모델 → 신뢰성 해법 ✗
- [ ] 스키마 보장 JSON = structured outputs
- [ ] structured outputs 지정 = `output_config.format`
- [ ] prefill → Claude 4.6부터 400 error
- [ ] 프로덕션 추출 = tool use 스키마 · 검증 · error 붙여 retry
- [ ] 추출 실패를 빈 객체 · regex로 땜질 ✗
- [ ] 긴 문서는 위, 질문은 끝 (최대 30% 향상) · 먼저 인용
- [ ] 여러 문서 → `<document>` · `<source>`로 하나씩 감쌈
- [ ] effort · cache · 사전 요약 → 구조 해결 ✗
- [ ] 컨텍스트 = 예산 · 불필요 자료 → 정확도도 하락 (context rot)
- [ ] drift/bloat → prune · compact · isolate
- [ ] compact = 오래된 턴 요약 · 최근 턴 유지
- [ ] isolate = subagent · 세션 분리
- [ ] drift/bloat에 `max_tokens` · 큰 window → 해법 ✗
- [ ] "보수적으로 · 확신도 높은 것만" → 정밀도 해법 ✗ · 명시적 기준
- [ ] 오탐 높은 범주 → 일시 비활성화 → 기준 개선 → 재개 (전체 중단 ✗)
- [ ] 판단 경계 흔들림 → 문제 있음 · 없음 양쪽 예시 + 이유
- [ ] 형태 흔들림 = schema · 판단 흔들림 = 기준 + 예시
- [ ] 없을 수 있는 값 = nullable · enum = `other` + 상세 필드
- [ ] schema = 구조 보장 · 의미 오류 = 별도 검증 코드
- [ ] 재시도 = 원본 + 거부된 출력 + 구체 오류 · 정보 부재 · 소스 모순에는 무효
- [ ] 리뷰 = 독립 instance · 추론 미전달 · 큰 입력 = 국소 pass + 통합 pass
- [ ] context 문제 = 증거로 결함 확정 → 결함별 처방 (window 확대 ✗)
- [ ] 정확한 값 = `case facts` 블록 · scratchpad (요약 밖)
- [ ] compaction 손실 = 요약 계약 수정 (임계값 이동 ✗)
- [ ] 전제 데이터 변경 → 새 session + 검증된 판단만 인계
- [ ] 집계 입력 중간 누락 → 앞에 핵심 요약 · 세부는 섹션 제목 (재배열 · `max_tokens` ✗)
- [ ] "절대" 규칙(돈 · 기밀 · 부수 효과) → 코드 gate · filter · permission rule (prompt 강화 ✗)
- [ ] 공유 지시 복붙 drift → 버전 관리 모듈 · Skill (일회성 작업은 제외)
- [ ] 사다리 소진(zero-shot → few-shot → 추론) → fine-tuning · 작업 재구성

<sub>근거: CCAR-F-Amey-Thakur-0008, CCAR-F-Udemy01-0017, CCAR-F-Udemy01-0025, CCAR-F-Udemy01-0029, CCAR-F-Udemy01-0030, CCAR-F-Udemy03-0018, CCAR-F-Udemy03-0053, CCAR-F-Udemy04-0003, CCAR-F-Udemy04-0006, CCAR-F-Udemy04-0013, CCAR-F-Udemy04-0037, CCAR-F-Udemy04-0045, CCAR-F-Udemy05-0003, CCAR-F-Udemy06-0019, CCAR-F-Udemy06-0020, CCAR-F-Udemy06-0040, CCAR-F-paullarionov-0054, CCAR-P-jrajath94-0058, CCAR-P-jrajath94-0076, CCAR-P-jrajath94-0146, CCAR-P-jrajath94-0149, CCAR-P-jrajath94-0151, CCAR-P-jrajath94-0291, CCAR-P-jrajath94-0345</sub>
