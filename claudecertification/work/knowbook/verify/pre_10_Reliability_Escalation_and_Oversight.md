# 10. Reliability, Escalation & Human Oversight — 반드시 알아야 할 지식
> 커버: CCAR-F D5(일부) · CCAR-P D5(일부) · 근거 문항 84개

## 1. 핵심 개념

### 1.1 Escalation 트리거
**escalation = 사람 요청 · 정책 공백 · 진전 불가 · 규정 의무**

| 상황 | 판정 | 이유 |
|---|---|---|
| 고객이 사람 담당자 요청 | ✓ | 명시적 요청 = 언제든 사유 |
| 정책 예외 · 정책 공백<br>예: 경쟁사 가격 맞춤<br>예: 타사 선박 구간 지연 보상 | ✓ | agent의 정책 발명 ✗<br>해석 · 확장 = 사람 판단 |
| 정해 둔 횟수 시도 후 진전 없음<br>예: 같은 안내 4회 · 40분 지속 | ✓ | 문서화된 escalation 기준 |
| 정책상 사람 승인 필수<br>예: `$400` 환불 > 승인 기준 `$250` | ✓ | 기준 초과 = 이관 의무 |
| 규정이 담당 부서를 지정한 안건<br>예: 적응외 사용 상담 · 부작용 보고 | ✓ | 안건 내용으로 정의 |
| 고객 격앙 + 정책상 환불 가능한 `$90` | ✗ | 공감하며 agent가 직접 처리 |
| 도구 호출 3회 필요 · 5 turn 초과<br>· 주문 30일 경과 · 지원 언어 사용 | ✗ | 기준 아님<br>복잡도 감당 = agent 몫 |
| 배송 후 마음 변경 우려<br>· 상반 증거 제시의 관계 부담<br>· 복수 이슈 조율 | ✗ | 정책 공백 아님 |

- 선행 = `get_customer` · `lookup_order` 조회 완료
- 조회 후에도 정책 공백 → `escalate_to_human`
- 감정 · 자기 보고 confidence = 복잡도 지표 ✗

![escalation 사유 5종과 직접 처리 대상을 가르는 판단 흐름](svg/10-escalation-triggers.svg)
*그림: 사람 요청 · 정책 공백 · 진전 없음 · 승인 필수 · 규정 안건만 escalate_to_human이고 감정 · confidence · 복잡도는 사유가 아니다*

<sub>근거: CCAR-F-Amey-Thakur-0038, CCAR-F-MyPractice-0050, CCAR-F-Udemy04-0039, CCAR-F-Udemy05-0023, CCAR-F-Udemy06-0043, CCAR-F-paullarionov-0050, CCAR-F-preporato-0002</sub>

### 1.2 Escalation 경계 보정과 handoff
**경계는 명시 기준 + few-shot으로 교육**

| 증상 | 조치 |
|---|---|
| 단순 사례(파손 상품 표준 교환)는 escalation<br>정책 예외 사례는 자체 처리<br>→ 첫 응대 해결률 55% (목표 80%) | system prompt에 명시적 escalation 기준<br>+ escalation vs 자체 해결 few-shot |
| 정책 공백 요청에 대응이 제각각<br>(규정 준용 · 일률 거절 혼재) | 정책 공백 = escalation 기준으로<br>system prompt에 명기 |
| 규정상 필수 안건이 자체 처리됨<br>(차분한 어조 · confidence 0.9 전후) | 필수 안건 유형을 기준으로 명시<br>+ 경계 few-shot |
| 담당자가 대화를 처음부터 재독 | 구조화 handoff 요약<br>(고객 ID · 근본 원인 · 권장 조치) |
| 담당자가 같은 안내를 반복 | handoff 요약에 시도한 절차 · 결과 포함 |

| 오답 | 이유 |
|---|---|
| 별도 classifier 모델 배포 | 근본 원인 = 판단 경계 불명확<br>추가 인프라 없이 prompt로 교육 가능 |
| 감정 분석 임계값 → 자동 escalation | 감정 = 케이스 복잡도 지표 ✗ |
| 자기 평가 1~10점 → 임계값 아래 사람 | 자기 보고 confidence = 복잡도 지표 ✗ |
| 감정 · confidence 임계값의 높낮이 조정 | 원인 = 지표 선택 자체<br>(정형 안건 43% 이관 · 필수 안건 자체 처리) |
| 조건 구현 위치만 변경<br>(app code ↔ system prompt) | 같은 지표 → 결과 동일 |
| 정책 공백을 일률 거절 · 자사 규정 준용 | agent 독단으로 공백을 메움<br>handoff 문제도 미해결 |

<sub>근거: CCAR-F-MyPractice-0049, CCAR-F-Udemy04-0039, CCAR-F-Udemy05-0023, CCAR-F-Udemy06-0043, CCAR-F-paullarionov-0049</sub>

### 1.3 다건 일치 시 확인 질문
**다건 일치 = 추측 대신 사용자에게 식별자 요청**

| 구분 | 내용 |
|---|---|
| 문제 | 이름 검색이 다건 반환(동명이인 3건 등)<br>→ Claude가 최근 주문 · 구매 · 로그인 1건 선택<br>→ 오계정 15% · 30% · 타인 예약 변경 |
| 정답 | 다건 반환 시 고객별 작업 전 추가 식별자 요청<br>(이메일 · 전화번호 · 주문 번호 · 학번 · 생년월일) |
| 이유 | 신원은 사용자가 확실히 앎<br>대화 한 턴 추가 < 오계정 오류 비용 |
| 구현 | 도구 결과에 일치 건수 포함<br>2건 이상 → 식별자 요구 절차<br>절차를 도구 설명 + system prompt 양쪽에 명시 |

| 오답 | 이유 |
|---|---|
| 최근 활동 기준 선택 규칙을 prompt에 명문화 | 추측을 고정할 뿐 |
| 추측으로 선택 + 근거 기록 | 근거를 남겨도 추측은 추측 |
| 일치 후보 전원 목록 제시 후 선택 | 다른 학생 개인정보 공개 |
| 다건 일치 시 일률 escalation | 자율 해결 가능한 경우까지 이관 |
| 85% confidence 임계 · 미만이면 질문 | 사용자 확인이 가장 확실한 방법 |
| 순위 알고리즘으로 1건만 반환<br>· 모호 일치 few-shot 추가 | 사용자 확인을 대체 ✗ |

- 판단 포인트 = 대상 확정에 부족한 정보가 무엇인지 · 누구에게서 얻을지

<sub>근거: CCAR-F-MyPractice-0055, CCAR-F-Udemy04-0039, CCAR-F-Udemy06-0036, CCAR-F-paullarionov-0055</sub>

### 1.4 모순 · 모호 요청: 확인 vs 가정 명시
**모순 선호는 확인 · 모호 요청은 가정 명시 후 진행**

| 상황 | 정답 | 이유 |
|---|---|---|
| 사용자 선호가 직접 모순<br>(위험 허용도 낮음 vs 수익 극대화)<br>→ "무엇에 투자?" | 충돌을 드러내고<br>우선순위 확인 요청 | 양립 어려운 목표 = 사람의 결정<br>다른 접근 = 틀릴 수 있는 가정 |
| 모호한 요청 + 되묻기 질문 다수<br>(3~4개 이상) → 이탈 35% · 40%<br>(파티 장소 예약 · 보고서 도움) | 합리적 가정을 명시하고 진행<br>수정 가능함을 안내 | 즉시 유용한 응답 + 통제권 유지<br>왕복 제거 |

| 오답 | 이유 |
|---|---|
| 가장 최근 선호로 진행 | 틀릴 수 있는 가정 |
| 두 시나리오 별도 추천 | 틀릴 수 있는 가정 |
| 충돌 무시 + 균형 포트폴리오 | 틀릴 수 있는 가정 |
| 숨은 기본값 · 가정 미공개 사전 정의 해석 | 무엇이 가정됐는지 사용자가 모름<br>의도와 다르면 혼란 |
| 질문 전부를 하나의 복합 메시지로 | 사용자에게 선행 노력 요구 |
| turn당 질문 1개로 제한 | 여전히 여러 턴 왕복 |
| 구조화 intake form | 마찰 증가 → 이탈 감소 목표와 반대 |
| 작은 모델로 모호성 classification | 핵심 UX 문제 미해결<br>지연 · 인프라 복잡성 추가 |

<sub>근거: CCAR-F-MyPractice-0063, CCAR-F-MyPractice-0074, CCAR-F-MyPractice-0076</sub>

### 1.5 에러 전파: 구조화 error context
**실패 정보는 복구 판단용 context째 전달**

| 전달 항목 | 용도 |
|---|---|
| 실패 유형 | timeout · 권한 · 파싱 구분 |
| 실행한 쿼리 · 시도한 내용 | 쿼리 수정 retry 판단 |
| 부분 결과 | 부분 결과로 계속 진행 |
| 대안 접근 | 다른 파싱 · 대체 출처 · 사용자 알림 |

| 방식 | 판정 | 이유 |
|---|---|---|
| context 담은 error를 coordinator에 반환 | ✓ | 건너뜀 · 대체 파싱 · 알림을 근거로 판단<br>실패가 계속 보임 |
| structured error context<br>(유형 · 쿼리 · 부분 결과 · 대안) | ✓ | coordinator 판단용 context 최대 보존 |
| 빈 결과 집합을 성공으로 반환 | ✗ | 오류 은폐 · 복구 근거 소실 |
| 손상 문서를 조용히 건너뜀 | ✗ | 실패 가시성 소멸 |
| 에러 없이 보고서 진행 | ✗ | 실패 사실이 어디에도 없음 |
| 일반 "실패" · "search unavailable" 상태만 반환 | ✗ | 복구 판단 정보 없음 |
| 성공할 때까지 조용히 반복하는 retry loop | ✗ | 해소 안 되는 에러에 retry 반복 = 피해야 할 대응 |
| 부분 결과를 성공 상태로 반환<br>에러는 metadata · coordinator는 모두 성공 취급 | ✗ | 실패를 성공으로 취급 |
| 예외를 최상위 handler까지 전파 → workflow 종료 | ✗ | 1건 실패로 완료분까지 소실 |

- coordinator 선택지 = 재시도 · 빈틈 기록 후 제외 · 중단
- 선택하려면 충분한 context를 함께 전달

![subagent 실패가 structured error context로 coordinator에 전달되는 흐름](svg/10-error-context-propagation.svg)
*그림: 실패는 유형 · 쿼리 · 부분 결과 · 대안을 담아 올려야 coordinator가 재시도 · 제외 · 중단을 고를 수 있다*

<sub>근거: CCAR-F-Amey-Thakur-0045, CCAR-F-MyPractice-0003, CCAR-F-MyPractice-0006, CCAR-F-MyPractice-0009, CCAR-F-Udemy04-0015, CCAR-F-paullarionov-0003, CCAR-F-paullarionov-0006, CCAR-F-paullarionov-0009</sub>

### 1.6 에러 처리 계층과 실패 유형 구분
**일시 실패는 subagent 안에서 · 해결 불가만 올림**

| 구분 | 내용 |
|---|---|
| 원칙 | 해결할 수 있는 가장 낮은 수준에서 처리<br>→ coordinator의 일상 에러 관여 감소 |
| 로컬 복구 | 일시 실패 = subagent · wrapper 안에서 retry |
| 올리는 것 | 복구 불가 에러만<br>시도한 단계 + 부분 결과 + 전체 context 동봉 |
| 부모에게 보이는 것 | 최종 메시지만 (중간 도구 호출 · 결과는 subagent 내부)<br>→ 얻은 findings + 미해결 error를 최종 결과에 포함 |

| 결과 | 의미 | 대응 |
|---|---|---|
| `Connection timeout` | 접근 실패 | retry 여부를 coordinator가 판단<br>예: 특허 DB 재시도 |
| `0 results` | 쿼리 성공 · 결과 없음<br>= 유효한 빈 결과 | 정보가 되는 발견으로 수용<br>예: 업계 보고서 0건 |
| 권한 오류<br>(유료 계약자 전용 DB) | 기다려도 해소 ✗ | backoff retry ✗<br>→ 대체 수단 |

| 오답 | 이유 |
|---|---|
| timeout · `0 results` 모두 개입 필요 실패로 보고 | 두 결과의 의미 구분 소실 |
| 성공률 하나(`67% source coverage`)로 집계<br>· 로그는 요청 시 제공 | 실패 유형 정보 손실<br>→ 재시도 대상 판단 불가 |
| 내부 retry 후 지속 에러만 보고 | 단독으로 불충분<br>접근 실패 vs 유효한 빈 결과 구분 필요 |
| 전용 에러 처리 agent + 공유 queue + 재시작 명령 | 가장 낮은 수준 처리 원칙과 반대 |
| coordinator가 사전 검증 후 문서 거부 | 복구를 coordinator가 떠안음 |
| 실패 보고 전 exponential backoff 3회 자동 retry | context 담은 error 반환이 우선 |
| subagent 내부에서 성공 표시한 빈 결과 반환 | 오류 은폐 |

<sub>근거: CCAR-F-MyPractice-0003, CCAR-F-MyPractice-0006, CCAR-F-MyPractice-0009, CCAR-F-MyPractice-0012, CCAR-F-Udemy02-0022, CCAR-F-Udemy04-0041, CCAR-F-paullarionov-0003, CCAR-F-paullarionov-0006, CCAR-F-paullarionov-0009, CCAR-F-paullarionov-0012</sub>

### 1.7 부분 실패 복구
**성공분은 보존 · 실패분만 보완**

| 상황 | 정답 |
|---|---|
| 12개 지역 병렬 검색 중 1곳 timeout<br>→ 예외 전파로 전체 종료 · 11곳 결과 폐기 | 실패를 structured error로 반환<br>coordinator가 계속 · retry 판단 |
| 8개국 중 7개 성공 · A국 권한 오류<br>에러에 대체 수단(관보 리콜 공시) 제시<br>coordinator가 8개국 전체 재위임 | 성공 7개국은 재검색 없이 통합에 사용<br>A국만 관보 검색을 위임 |
| 병렬 tool 호출 중<br>`get_customer` 성공 · `lookup_order` timeout | 성공 결과 + `is_error: true` 실패 결과<br>둘 다 반환하고 대화 계속 |
| 일시 timeout | wrapper 안에서 retry 후 결과 반환 |

| 오답 | 이유 |
|---|---|
| 실패 호출을 빈 주문 목록으로 성공 처리 | 실패를 거짓 사실로 변환 |
| 실패마다 대화 전체 중단 | 성공한 결과까지 폐기 |
| 최상위 wrapper로 전체 최대 3회 재실행 | 낭비 증가 · 실패분만 다루지 못함 |
| 실패 지역을 빈 결과로 두고 11개 지역으로 보고서 | 오류를 삼키는 안티패턴 |
| timeout 30초 → 10분 연장 | 실패 자체가 없어진다는 전제 |
| 같은 지시로 8개국 전체 재위임 | 권한 오류 3회 반복 · 비용 약 4배 |
| 권한 오류에 backoff retry 3회 | 기다려도 해소 ✗ |
| 실패 즉시 실행 전체 중단 + 사람에게 보고 | 대체 수단이 있는데 복구 기회 포기 |
| 병렬 호출 비활성화 후 순차 요청 | 실패 취급 방식 불변 |
| `PreToolUse` hook으로 이후 `lookup_order` 차단 | 일시 오류 → 영구 중단 |
| 부모가 subagent의 중간 Bash 호출 확인 | 구조상 불가 (부모에는 최종 메시지만) |

- 실패 시 `tool_result`에 `is_error: true` + 오류 내용
- Claude가 retry · 설명 · escalation 중 선택
- 에러의 대체 수단을 읽어 복구 = coordinator 책임

![8개국 병렬 검색에서 A국 권한 오류 시 성공분 보존과 A국만 재위임하는 흐름](svg/10-partial-failure-recovery.svg)
*그림: 성공 7개국은 재검색 없이 쓰고 실패한 A국만 에러의 대체 수단으로 다시 위임한다*

<sub>근거: CCAR-F-Udemy02-0022, CCAR-F-Udemy02-0029, CCAR-F-Udemy04-0015, CCAR-F-Udemy04-0041</sub>

### 1.8 Coverage annotation
**빈틈은 최종 산출물까지 가시화 (graceful degradation)**

| 구분 | 내용 |
|---|---|
| 정의 | 합성 출력에 근거가 탄탄한 결론과<br>출처를 확보하지 못한 공백을 표기 |
| 효과 | 완료분 가치 보존 + 불확실성 전파<br>→ 독자가 결과를 얼마나 믿을지 판단 |
| 전달 범위 | subagent → coordinator에서 끝나면 ✗<br>최종 보고서 독자까지 도달해야 가치 |
| 표기 항목 | 검토한 파일 · 건너뛴 파일과 사유 · coverage 수치 |
| 병합 보고서 | scanner별 coverage 표기를 합친 보고서에도 유지 |
| 가치 | "문제 없음" vs "실행된 부분에서는 문제 없음" 구별<br>→ 건너뛴 파일을 대기열에 넣어 집중 점검 |
| 운용 | 보고서 첫머리 요약에도 게재<br>누락 출처 + 다음 확인 방법 병기<br>예: "이 지역은 정보원을 이용할 수 없었음" |

| 오답 | 이유 |
|---|---|
| 성공분만으로 종합 · 누락 미언급 | 공백 은폐 |
| 불완전 데이터를 이유로 error 반환<br>→ 전체 retry · 실패 처리 | 완료분 가치 소실 |
| 더 긴 timeout retry 후 synthesis 시작<br>· 해소될 때까지 retry 반복 | 해소 안 되는 에러에 retry 반복 |
| 실패 카테고리를 전주 보고서 내용으로 대체 | 오래된 정보로 에러 은폐 |
| 한 카테고리 실패 시 보고서 중단 · 다음 주 대기 | workflow 전체 중단 |
| scanner별 신뢰도 점수 | 보정 안 됨 · 건너뛴 대상 미표시 |
| 더 긴 서술형 요약 | 수치 없이 글만 증가 |
| 더 강한 모델 | budget에 걸릴 수 있음<br>보고서는 여전히 빈틈을 숨김 |

<sub>근거: CCAR-F-MyPractice-0005, CCAR-F-Udemy04-0015, CCAR-F-Udemy04-0041, CCAR-F-Udemy06-0015, CCAR-F-paullarionov-0005, CCAR-F-preporato-0008</sub>

### 1.9 중단 복구: checkpoint · idempotent
**중단 = checkpoint + idempotent side effect로 지연 전환**

| 증상 | 원인 | 조치 |
|---|---|---|
| 27번째 저장소에서 중단<br>→ 재실행 시 1번부터 | 진행 상태가 프로세스 밖에 없음 | manifest 파일에 checkpoint 저장<br>(완료 · 남은 저장소 · 지금까지 결과)<br>→ 중단 후 이어서 시작 |
| 재실행 시 같은 finding 티켓 중복 | side effect가 멱등이 아님 | 티켓 생성 idempotent<br>예: 저장소 + finding id를 키로 사용 |
| 오류 없이 background check 2% 건너뜀<br>(빈 결과 반환 → 다음 단계 진행) | handoff를 검증하지 않음 | 계획을 checkpoint로 저장<br>다음 단계 전 각 handoff 검증<br>건너뜀 시 소유자 알림 · checkpoint에서 재개 |

| 오답 | 이유 |
|---|---|
| scanner context window 확대로 이전 실행 기억 | 프로세스가 죽으면 context 소멸 |
| 시작 시 coordinator에게 완료 저장소 질의 | API stateless → 이전 실행 기억 없음 |
| 실행 빈도 축소(매일 → 매주) | 문제 그대로 |
| 건너뛴 단계에 더 큰 모델 | 성능 문제가 아닌 단계<br>대리 해법 |
| 건너뛴 단계의 로깅 필드 추가 | 건너뜀을 기록할 뿐 막지 못함 |
| 건너뛴 단계를 두 번 실행 | 검증 안 된 단계를 2배로 늘림 |

| 한계 | 내용 |
|---|---|
| handoff 검사 | 단계마다 지연 추가 |
| checkpoint | 저장 공간 · 보존 규칙 필요 |
| 소유자 알림 | 뒤를 받치는 runbook 필요 |

- 빈 결과 ≠ 성공 → handoff 검사가 빈 결과를 포착
- 깔끔히 반환된 단계 = 올바르게 실행된 단계라는 가정 ✗

![manifest checkpoint에서 중단 후 이어서 재개하는 흐름](svg/10-checkpoint-idempotent.svg)
*그림: 진행 상태는 프로세스 밖 manifest에 두고 side effect는 idempotent로 만들어 중단 후 남은 저장소부터 재개한다*

<sub>근거: CCAR-F-preporato-0006, CCAR-P-jrajath94-0216</sub>

### 1.10 조용한 실패 방지: 검증 · fail closed
**감지 단계 + 감지 시 조치 = 신뢰성의 최소 단위**

| 요구 | 설계 |
|---|---|
| 잘못된 출력이 조용히 나가면 안 됨 | 출력을 거부하고 정해 둔 fallback을 실행하는 검증 단계 |
| 오류가 눈치채지 못한 채 전달 불가 | 감지 단계 + 감지 시 취할 조치 |
| 성공 기준 정의 | 기준 없으면 완료 · 실패 구별 불가<br>→ 멈추지도 측정하지도 못함 |
| production 정상 여부 | 정의한 기준 대비 작업 성공<br>+ 실패의 비율 · 양상 |
| 결정 불가 · 모호 (예: 약 용량 "지시대로 복용") | fail closed: 기본 거부 + 약사 이관<br>추측 ✗ |
| 값이 원본 레코드와 일치해야 함<br>(검사는 코드 · 모델 호출 추가 ✗) | structured outputs로 스키마 고정<br>+ 코드에서 각 값을 원본과 비교 |

| 오답 | 이유 |
|---|---|
| 더 큰 모델 · 더 긴 prompt · 예시 · 더 긴 context | 평균 개선일 뿐 잘못된 출력 감지 ✗ |
| token 총량 · 평균 응답 시간 · 호출 횟수 측정 | 비용 · 동작 신호 → 정확성 정보 ✗ |
| 모호할 때 가장 흔한 용량으로 승인<br>· 더 그럴듯한 해석 선택 | 추측이 환자에게 도달 |
| 모호성을 기록하고 승인 | 해로운 추측의 완벽한 기록 |
| prompt로 모델에게 반환 전 자기 검사 요청 | 검사는 코드에서 실행해야 하는 제약 위반 |
| 초안을 모델에 다시 보내 원본과 비교 | 모델 호출 추가 → 제약 위반 |
| strict tool use로 값 일치 보장 | tool 이름 · 입력만 스키마 검증<br>값 대조 ✗ |

- fail closed = 불확실하면 행동을 멈춤
- 안전 게이트의 올바른 출력 = "결정할 수 없으니 멈춘다"
- fail closed 후 약사 대기열에 처리 시간 SLA 필요

<sub>근거: CCAR-F-Amey-Thakur-0034, CCAR-F-Amey-Thakur-0035, CCAR-F-Amey-Thakur-0079, CCAR-F-Amey-Thakur-0080, CCAR-P-jrajath94-0216, CCAR-P-jrajath94-0315, CCAR-P-jrajath94-0600</sub>

### 1.11 대규모 탐색: subagent로 출력 격리
**탐색은 subagent에 격리 · 메인은 설계 · 구현 몫**

| 상황 | 정답 |
|---|---|
| 120개 파일 wrapper 작업<br>1단계에서 호출 지점 수백 개 출력 → context 소진 | 1단계에 `Explore` subagent 사용<br>요약만 수신<br>2~3단계(설계 · 구현)는 메인 대화 |
| 신규 문서 유형 지원<br>(추출 모듈 수십 개 · validator · fixture 관례 조사) | 조사를 `Explore` subagent에 위임<br>범위 · 관례 명시 → 요약된 발견으로 구현 |
| 페이즈마다 새 subagent<br>2페이즈가 1페이즈의 38개 파일 재독<br>(token 약 절반 중복) | 이전 페이즈 핵심 발견을 요약해<br>다음 subagent 초기 context에 주입 |

| 구분 | 내용 |
|---|---|
| subagent context | 독립된 새 context<br>호출한 쪽 대화 이력 안 보임<br>중간 도구 출력은 내부 · 최종 결과만 메인으로 |
| `Explore` | 변경 없이 코드베이스 검색 · 이해에 특화<br>Claude가 스스로 위임하기도 함 |
| 위임 지시 | `Explore` · `Plan`은 `CLAUDE.md` 미로드<br>→ 지킬 관례 · 범위를 위임 지시에 포함 |
| 페이즈 요약 형식 | 확인 완료 파일 · 판명된 의존 관계 · 미해결 의문 |
| 원인 진단 단서 | 위임 prompt에 의뢰문만 있음<br>→ "조사를 마쳤음"을 subagent가 모름 |

- ⚠️ `Explore` · `Plan`의 `CLAUDE.md` 미로드<br>버전에 따라 바뀜 · 2026-11 공식 문서와 일치

| 오답 | 이유 |
|---|---|
| 모든 단계를 메인에서 + 주기적 `/compact` | 쌓인 뒤의 사후 처리 · 격리 ✗ |
| 모듈 · fixture 일괄 로딩 slash command | 문제를 확대 |
| 전체를 plan mode에서 진행 | 편집할 수 없는 모드 · 출력 격리 ✗ |
| headless `--continue` + batch 간 요약<br>· `CLAUDE.md` + 공유 memory + 여러 session | 탐색 출력 격리 수단 아님 |
| Grep 미허용 · 작은 `max_turns`<br>· 부모 context 압축 | 다른 증상의 요인<br>검색 비효율 · 도중 종료 · 판단 흔들림 |

<sub>근거: CCAR-F-MyPractice-0045, CCAR-F-Udemy03-0034, CCAR-F-Udemy04-0025, CCAR-F-paullarionov-0045</sub>

### 1.12 장시간 session의 context 열화
**확인한 사실은 대화 밖에 기록**

| 증상 · 단서 | 해석 |
|---|---|
| 구체 클래스 대신 "전형적 패턴"으로 답변 | context 열화 (context rot) |
| 이전 답변과 불일치하는 설명 | context 열화 |
| 조사 끝낸 파일을 Grep으로 재탐색<br>초반 "변경 금지" 지시 무시 | 긴 도구 출력 누적 → 초반 정보 참조 약화 |
| 증상이 후반에 발생 · context 대부분이 Grep · Read 출력<br>`CLAUDE.md` 불변 | 원인 = session 길이 · 도구 출력 누적<br>(설정 · 외부 변경 ✗) |
| compaction 이후 초반 발견 누락 | 컴팩션 = 구조화된 요약으로 대체<br>도구 출력 전문 · 중간 추론은 남지 않음 |

| 조치 | 내용 |
|---|---|
| 구조화 노트 파일 | `investigation-notes.md` 등에 확인된 의존성 기록<br>후속 질문 전에 읽게 함 |
| scratchpad 파일 | 클래스 이름 · 파일 경로 · 역할 · 미확인 사항 기록<br>이후 질문에서 참조 · 인수인계에도 유용 |
| `/compact` | 남길 조사 결과를 지시로 덧붙여 같은 session 계속<br>Agent SDK: prompt 문자열로 `/compact` 전송 |
| subagent 위임 | 장황한 출력을 메인 대화에서 제외 |
| 지켜야 할 제약 | `CLAUDE.md`에 작성 |

- 선택 기준: 남길 정보가 대화 밖에 있는가
- `/compact` = 요약 의존<br>노트 · scratchpad 파일이 선택지에 있으면 우선

| 오답 | 이유 |
|---|---|
| plan mode로 전환 | plan = 구현 방침 문서 · 이전 분석 상세 보존 ✗ |
| `/compact` 초점 지시 단독<br>(노트 파일 선택지가 있을 때)<br>· 시작 시 지시를 길게 | 요약의 영향을 받는 곳에 정보를 둠<br>노트 선택지가 없으면 `/compact` 지시 ✓ |
| 새 session + 이전 조사 미전달 | 인수인계 요건 위반 · 조사 결과 소실 |
| `allowed_tools`에서 Grep 제거<br>· `max_turns` 상향 | 이미 가득 찬 context에 효과 ✗ |
| 더 큰 context window 모델 | 열화를 뒤로 미룰 뿐 |
| 답변마다 "구체 클래스명으로" 지시 | 원인을 건드리지 않음 |
| 자동 압축으로 `CLAUDE.md` 소실 · `CLAUDE.md` 낡은 기술<br>· 타 멤버의 파일 변경 | 사실과 불일치 · 두 증상을 동시에 설명 못함 |

<sub>근거: CCAR-F-Udemy01-0004, CCAR-F-Udemy05-0030, CCAR-F-Udemy05-0044, CCAR-F-Udemy06-0055</sub>

### 1.13 검토 형태: 되돌림 가능성 · 결과 중대성
**검토 형태는 되돌림 가능성 · 중대성 · 물량으로 결정**

| 상황 | 검토 형태 |
|---|---|
| 되돌림 가능 · 저위험 · 대량<br>예: 내부 업데이트 2,000건/일 · 블로그 글(몇 분 내 롤백)<br>· 소셜 게시물(몇 초 내 삭제) | post-action 표본 검토 + audit logging<br>탐지 후 수정 > 전량 gate |
| 되돌림 가능 + 일부 법적 리스크<br>예: 기사 500건/일 · 200건 중 1건 법적 리스크 | 되돌림 가능 등급: post-action 표본 + 테스트한 롤백<br>법적 리스크 등급: pre-action 승인<br>(전체 기사 + 정책 chunk 열람) |
| 책임 발생 · 물량이 사람 gate에 맞음<br>예: 계약서 초안 30건/일 | pre-action 승인<br>(변호사가 고객 전달 전 조항 검토) |
| 공개 헤드라인 + 편집자가 읽고 게시 | 컨텍스트를 갖춘 pre-action 승인 ✓ |
| 되돌릴 수 있는 파일 편집 5,000 session/일 | 무작위 session 샘플 오프라인 검토<br>플래그 동작은 사람에게<br>테스트된 롤백 경로로 되돌림 |

| 변수 | 판단 |
|---|---|
| 되돌림 가능 + 저위험 | post-action 검토 · 롤백이 위험에 답함 |
| 규제 대상 · 되돌림 불가 | pre-action 승인 |
| 대량에서 pre-action 전량 | 형식적 도장 찍기 (게이트가 연극) |
| 롤백이 작동 안 함 | 그 등급은 pre-action 대상 |

| 오답 | 이유 |
|---|---|
| 모든 초안 · 글 · 게시물에 pre-action 승인 | 대량에서 형식적 승인 · 롤백이 덮은 위험에 지연만 구매 |
| 초안마다 CEO · 글마다 이사회 · 게시물마다 법무 | 저위험 · 되돌림 가능 건에 과잉 gate |
| 로깅 없음 | 표본 검토 + 완전 로그 = 저렴한 실질 탐지 |
| 법적 책임 계약서를 사후 샘플링 | 결과 중대 → pre-action 필요 |
| 모든 편집 전 승인 + 결정 기록 | 사후 검토를 허용하는 제약에 과잉 |
| `evaluated_permission` = `review`로 편집 일시 중지 | 필드는 tool 호출 이벤트의 결정을 보고할 뿐 |
| 모델이 "95% 확신"이면 전부 자동 승인 | 측정된 비율이 아닌 문구 신뢰 |

| 한계 | 내용 |
|---|---|
| post-action 방식 | 롤백을 정기 테스트해야 함 |
| 법적 리스크 pre-action | 법적 리스크 분류기가 정확해야 함<br>놓친 기사는 gate를 건너뜀 |

![되돌림 가능성과 결과 중대성으로 검토 형태를 고르는 decision tree](svg/10-review-form-by-risk.svg)
*그림: 되돌릴 수 있고 저위험이면 post-action 표본 검토, 중대하거나 되돌릴 수 없으면 pre-action 승인이다*

<sub>근거: CCAR-P-jrajath94-0219, CCAR-P-jrajath94-0378, CCAR-P-jrajath94-0440, CCAR-P-jrajath94-0503, CCAR-P-jrajath94-0566, CCAR-P-jrajath94-0567, CCAR-P-jrajath94-0679</sub>

### 1.14 위험도 routing · 물량 · 규제 요건
**사람은 위험이 큰 곳에 · 일상 물량은 표본으로**

| 상황 | 설계 |
|---|---|
| 신뢰도 · 영향 혼재 대량 | 신뢰도 낮거나 영향 큰 건 → 사람<br>일상 건 → 그대로 처리 |
| 저위험 댓글 500,000건/일<br>+ 가끔 법적 위협 | 일상 결정 = 자동화 + 표본 QA<br>법적 위협 · 시스템 설정 임계값 미달 → 사람 |
| 인보이스 6,000건/일<br>(8% > `$2,000` · 건당 3분 · 시간당 `$35`) | `$2,000` 초과 8% = pre-action 승인<br>나머지의 2%만 표본 검토<br>모든 검토자에게 전체 의사결정 컨텍스트 |
| 규제: 모든 거절은 전달 전 사람 승인 · 예외 없음 | agent가 모든 결정 초안 + 근거 첨부<br>임계값 미만 승인은 자동 발급<br>모든 거절은 대기열 → 사람 검토 · 승인 |

| 인보이스 비용 산술 | 값 |
|---|---|
| 전량 검토 | 6,000 × 3분 = 300시간 → `$10,500`/일 |
| 고위험 480건 | 24시간 → `$840` |
| 나머지 5,520건 중 2% 표본 110건 | 5.5시간 → `$192.50` |
| 합계 | `$1,032.50`/일 |
| 무작위 50% | 3,000건 · 150시간 → `$5,250`/일 |

| 오답 | 이유 |
|---|---|
| 위험과 무관하게 모든 출력 검토 | 효율 소실 · 대기열 붕괴 · 검토자 피로 |
| 고정 10% 무작위 표본 · 무작위 50% | 위험 무시 → 고위험도 같은 비율로 통과 |
| 사용자가 불평하는 것만 검토 | 위험 기반 라우팅 아님 |
| 사람을 완전히 배제 | 법적 위협이 방치됨 |
| 모델 자기 보고 신뢰도가 낮을 때 escalation | 보정 미비 → 임계값은 시스템이 설정 |
| 거절을 agent가 직접 발급 + 감사용 기록 | 기록은 검토가 아님 |
| 거절을 직접 발급 + 사후 5% 표본 | 거절 95%가 무검토 → "예외 없음" 위반 |
| 사람이 결정 작성 + agent는 형식만 | agent 가치 제거<br>제약은 거절에 대한 사람 검토 요구 |

| 한계 | 내용 |
|---|---|
| 표본 검토 | 표본 사이의 새 실패 모드를 놓칠 수 있음<br>표본 비율은 오류율을 따라야 함 |
| 승인 건수 | 검토자는 하루 480건에도 피로 |
| 설계 전제 | 표본은 무작위 · 컨텍스트 번들은 결정 전 도달 |
| 신뢰도 신호 | calibration 전제 (→ 1.17) |

<sub>근거: CCAR-P-Amey-Thakur-0042, CCAR-P-jrajath94-0035, CCAR-P-jrajath94-0217, CCAR-P-preporato-0022</sub>

### 1.15 Reviewer 효과성: 컨텍스트 · 피로 · triage
**검토자에게 실제 의사결정 컨텍스트 + 피로 관리**

| 증상 | 원인 | 조치 |
|---|---|---|
| 승인율 98%<br>승인 환불 40%가 정책 근거 없음 | 검토자가 금액 · 고객 메시지만 봄<br>(볼 수 없음 ≠ 느림) | 결정 전 제안 · 검색된 정책 chunk<br>· tool 인자 · 금액 표시 |
| 6시간째 건당 몇 초<br>오후 내내 오류율 상승 | 검토자 피로 = 고무도장 | 검토자 순환 · 세션 길이 상한<br>+ 위험도 연동 · 전체 컨텍스트 |
| PR당 발견 15개 · 40% false positive<br>조사 시간이 병목 · 필터링 금지 | 각 발견을 클릭해 근거 확인 | 각 발견에 근거 + confidence 추정치 직접 포함<br>→ 빠른 triage · 전부 표시 |

| 오답 | 이유 |
|---|---|
| 건당 검토 시간 증가 | 같은 빈약한 시야 · 더 느릴 뿐 |
| 같은 화면을 보는 두 번째 검토자 | 보지 못하는 검토자 둘이 동의 |
| 검토자를 더 큰 모델로 대체 | 사람 판단 제거 · 검증 안 된 제안으로 회귀 |
| 검토자 증원 + 전량 동일 방식 | 피로를 확대 → 도장 증가 |
| 모델로 대체 + 월 spot-check | 위험도가 요구하는 통제 제거 |
| 표본을 0.5%로 축소 | 표본 사이에 새 실패 모드 은폐 |
| 과거 false positive와 일치 항목 자동 억제<br>· 높은 confidence 발견만 표시 | 발견을 숨김 → 필터링 금지 제약 위반 |
| 발견을 "차단 이슈"와 "제안"으로 분류 | 근거 확인 시간을 직접 줄이지 못함 |

| 한계 | 내용 |
|---|---|
| 컨텍스트 번들 | token 비용 · 물량이 많으면 번들 자체가 비용 |
| 순환 | 충분한 수의 훈련된 검토자 필요<br>짧은 세션 = handoff 오버헤드 |

- 컨텍스트 번들의 chunk = agent가 실제로 검색한 것
- 위험도 극단 결정 = four-eyes 검토<br>(양쪽 모두 전체 컨텍스트 보유)

<sub>근거: CCAR-F-MyPractice-0028, CCAR-P-jrajath94-0218, CCAR-P-jrajath94-0221</sub>

### 1.16 자기 보고 confidence의 한계
**자기 보고 신뢰도 ≠ 정확성 보증**

| 사실 | 내용 |
|---|---|
| 자기 보고 신뢰도 | 보정이 잘 안 됨 → escalation trigger로 신뢰 ✗<br>예: 자격 판정 신뢰도 0.62 |
| 높은 신뢰도 | 정확성 보증 ✗ → 자신 있게 틀림<br>예: confidence 0.95 전후로 지급일 오독 3주 지속 |
| 감정 · 자기 보고 confidence 기반 자동 이관 | 정형 안건 43%가 이관<br>필수 안건은 confidence 0.9대로 자체 처리 |
| 중대 결과 출력 | 모델과 독립적인 것에 대해 검증하도록 설계 |
| 임계값 설정 주체 | 시스템 (모델이 자기 보고로 escalation ✗) |

| 오답 | 이유 |
|---|---|
| 신뢰도 신호를 믿음 | 신뢰도는 증거가 아님 |
| 모델에게 다시 확인 요청 | 자기 점검 = 독립적이지 않음 |
| 두 모델의 일치 결과 채택 | 두 모델이 일치하면서 둘 다 틀릴 수 있음 |

- 신뢰도가 쓸모 있는 조건 = 보정 후 (→ 1.17)

<sub>근거: CCAR-F-Udemy04-0038, CCAR-F-Udemy05-0023, CCAR-F-preporato-0002, CCAR-P-Amey-Thakur-0072, CCAR-P-preporato-0022</sub>

### 1.17 필드 단위 calibration과 review 배분
**리뷰는 오류 가능성이 높은 곳에 우선 배분**

| 단계 | 내용 |
|---|---|
| 1 | 구조화 출력에 필드별 confidence 출력 |
| 2 | 라벨 검증 세트로 필드별 confidence vs 실제 정확도 측정<br>→ 임계값을 필드별로 개별 설정 (calibration) |
| 3 | 낮은 confidence 추출<br>+ 소스가 모호 · 모순인 추출을 우선 리뷰 |
| 4 | 자동 등록분도 일정 수 계속 추출해 정확도 측정<br>→ 공급처 · 서식 변경 시 어긋남 감지 |
| 5 | 문서 유형별로 임계값 재검토<br>정확도 낮은 세그먼트는 기준을 엄격하게 |

| 근거 신호 | 검출 수단 |
|---|---|
| 문서 간 불일치 | 참조 소스 간 정합성 검사로 기계적 검출 |
| 문맥에서 약한 추측 | schema에 필드별 confidence · ambiguity<br>· contradiction · 근거 발췌 필드 |
| 플래그된 레코드 | 클린 레코드보다 먼저 reviewer 큐 |

| 상황 | 시사점 |
|---|---|
| 모델명 대체로 정확 · 위험물 분류 자주 오류 | 배분 단위 = 필드 |
| 알레르겐 칸 confidence ≥ 0.9인데 약 6% 오류<br>품명 칸 0.7대도 거의 정확 | 필드마다 confidence와 정확도의 어긋남 |
| 처리 2,000건 vs 리뷰 300건/일 | 우선순위 지정 필요 (도착순 300건 ✗) |

| 오답 | 이유 |
|---|---|
| 전체 정확도 상회 → 리뷰량 축소 + 균일 샘플링 | 필드별 정확도 차이를 가림 |
| 문서 단위 단일 점수 + 승인 문서의 전 필드 공개 | 입도가 너무 거침 |
| `stop_reason: end_turn`을 고신뢰로 보고<br>리뷰 생략 | 끝까지 생성됐다는 뜻일 뿐<br>내용 정확성 보증 ✗ |
| 전 필드 임계값 일률 0.97 | confidence와 정확도의 대응 미확인 |
| prompt에 "불확실하면 낮게 출력" 추가 | 대응 미확인 · 숫자만 조작 |
| 문서 단위 1~10점 자기 신고 후 8점 이상 자동 등록 | 보정 안 된 자기 보고 |
| 도착순 300건 · 무작위 300건 리뷰 | 오류 가능성 미고려 |
| OpenAI SDK 층으로 `logprobs` 요청 | OpenAI SDK 호환 층에서 무시됨 |
| citations + JSON schema 출력 병용 | 함께 쓰면 400 에러 |

- ⚠️ OpenAI SDK 층 `logprobs` 무시<br>citations + structured outputs = 400<br>둘 다 시점에 따라 바뀜 · 2026-11 문서와 일치

<sub>근거: CCAR-F-Udemy02-0044, CCAR-F-Udemy02-0052, CCAR-F-Udemy05-0051, CCAR-F-Udemy06-0054</sub>

### 1.18 표본 검증: 편향 측정 · 층화 샘플링
**성공분만 재면 부풀려짐 · 고신뢰 구간도 층화 표본**

| 문제 | 올바른 방법 |
|---|---|
| validation 통과 레코드만으로 정확도 측정<br>(98% · 97%)<br>→ 시스템이 이미 성공한 곳만 측정 | 실패 · 간신히 통과한 문서 포함<br>전체 입력을 대표하는 라벨링 표본 |
| 전체 정확도(97%)만 확인<br>→ 특정 유형 · 필드의 저성능을 가림 | 문서 유형 · 필드별 정확도 측정<br>목표(95%) 충족 구분만 리뷰 축소 |
| 고신뢰 구간 무검토<br>예: 양식 변경 후 0.95 confidence로 3주 오독 | 고신뢰 구간도 층화 무작위 추출 (거래처 · 문서 유형)<br>→ 층별 오류율 측정 |
| 일률 확인 중단 | 확인을 그만둔 구분도 층화 추출로 계속 확인 |

| 요건 | 방식 |
|---|---|
| 프로덕션 오류율 측정 | 고신뢰 출력을 일정 수 이상 계속 샘플 리뷰<br>(cutoff 상향 후에도) |
| 드문 영역 실패 모드 포착 | 변경 유형 · 언어 · 지적 카테고리로 층화<br>오류와 신종 패턴을 나눠 라벨링 |
| 새 실패의 재발 감시 | 자동 평가 세트로 회귀 점검<br>발견한 실패를 평가 세트에 추가 |
| 구분별 오류 패턴 | 문서 종류 · 중요 필드별로 고신뢰 레코드 추출 |
| 조기 경보 | 층별 오류율 대시보드 + 급상승 경고 조건 |

| 오답 | 이유 |
|---|---|
| 균일 샘플링 + 파이프라인 전체 집계 오류율 하나 | 건수 적은 영역을 희석 |
| 저신뢰 우선 + 고신뢰는 월 전체 정확도만 | 드문 오류가 평균에 묻힘 |
| 고신뢰 전체에서 단일 무작위 샘플 + 주간 집계만 | 드문 실패에 둔감 |
| 저신뢰 · 모호 문서만 리뷰 · 고신뢰는 정확하다고 가정 | 자신 있게 틀린 오류를 놓침 |
| 자동 송신 임계값 0.90 → 0.97 상향 | 알려진 문제 대처 · 조기 검출 요구 ✗ |
| 새 양식을 few-shot으로 추가 | 알려진 문제 대처 |
| 양식 변경 통보 후 해당 거래처 전수 리뷰 | 예고 없는 변화에 무력 |
| 무작위 50건 재확인 → 95% 이상이면 전체 확인 중단 | 구분별 차이를 보지 못함 |

- 단서 = "오류 수정" vs "유사 문제 조기 검출"

<sub>근거: CCAR-F-Amey-Thakur-0009, CCAR-F-Amey-Thakur-0050, CCAR-F-Udemy02-0003, CCAR-F-Udemy03-0014, CCAR-F-Udemy04-0038, CCAR-F-Udemy05-0031</sub>

### 1.19 Provenance 보존
**claim-source 쌍을 구조화해 synthesis까지 유지**

| 증상 | 원인 | 조치 |
|---|---|---|
| subagent는 정확한데<br>최종 보고서 출처가 엉뚱 | handoff 형식에 주장 + 출처 없음<br>→ 단계 넘으며 provenance 소실 | 주장과 출처를 함께 담은 handoff 형식 |
| "평균 12% 증가"의 근거 논문 추적 불가 | 요약 단계에서 출처 소실 | 주장별 출처 URL · 문서명 · 발췌를 구조화 출력<br>통합에서도 유지 |
| 피어 리뷰 논문 · 벤더 벤치마크 · 사내 설문을<br>같은 비중으로 취급 | 간결한 요약 + 일반 출처 목록만 반환 | 구조화 claim record 반환<br>(출처 위치 · 발행일 · 근거 발췌)<br>+ 통합 단계에서 출처 종류별 가중 |
| 2021년 호환성 주의와 2024년 릴리스 공지를<br>같은 현재 정보로 취급 | 부모가 요약만 수신<br>날짜 metadata 소실 | subagent가 finding별 출처 날짜 + 날짜 근거 JSON 반환<br>+ `CLAUDE.md`에 날짜 모순 시 신규 우선 규칙 |

| 오답 | 이유 |
|---|---|
| 보고서 끝에 참고문헌 목록 | 주장 단위 대응을 보여 주지 못함 |
| 작성 후 web search로 출처를 찾아 각주 | 추측에 의한 복원 |
| subagent 요약을 더 짧게 | 출처를 더 잃음 |
| 완전한 대화 기록 보존 + synthesis가 출처 추정 | 추측은 불확실 |
| subagent에 더 넓은 tool 접근 | 출력 형태를 바꾸지 못함 |
| 종합 모델을 크게 · 검색 결과량 축소 · 생성 시점 조정 | 원인은 handoff 형식 |
| citations로 날짜 문맥 보충 | 인용 = 어디에 쓰여 있는가 · 언제 정보인가 ✗ |
| 모순처럼 보일 때만 산문 재요약 요청 | 모순을 알아차리지 못하는 문제 미해결 |
| `CLAUDE.md` 규칙만 · JSON 반환만 | 상류(반환 형식) + 하류(판단 규칙) 둘 다 필요 |

- 출처와 대응 안 된 주장 = 보고서에서 제외
- 출처 부착 여부를 코드로 검증

![요약만 넘기는 방식과 claim record로 넘기는 방식의 provenance 비교](svg/10-provenance-claim-source.svg)
*그림: 출처는 claim-source 쌍으로 구조화해 synthesis까지 넘기고 코드로 검증해야 유지된다*

<sub>근거: CCAR-F-Amey-Thakur-0044, CCAR-F-Udemy02-0014, CCAR-F-Udemy03-0022, CCAR-F-Udemy06-0028</sub>

### 1.20 근거 없는 값과 인용 검증
**근거 없는 값은 채우지 않고 unknown 반환**

| 상황 | 정답 | 이유 |
|---|---|---|
| 인용 필수 추출<br>funder 단서가 문서 title metadata뿐<br>본문에는 funder 기술 없음 | funder를 "불명"으로 반환<br>+ 증거 부족 주석 | title · context = 모델에 전달되나 인용 대상 아님<br>정보 없으면 모른다고 답하게 함 |
| 긴 계약서 요약<br>(모델 유지 · 각 주장이 원문을 가리킴) | 요약 전 원문 그대로의 인용문 요구<br>+ 인용 없는 요약 주장 제거 | 남은 모든 주장을 검증 가능 |

| 오답 | 이유 |
|---|---|
| 필수 필드화 + 추출 tool 강제 | "값을 채우는" 방향 · 근거 없으면 올바른 레코드 불가 |
| `max_tokens` 증가 + 재실행 | 값을 채우는 방향 |
| subagent 재실행으로 더 철저히 재검색 | 값을 채우는 방향 |
| 더 큰 모델 tier | 제약이 같은 모델 유지 |

- 누락 원인 먼저 구분: 못 찾음 vs 존재 안 함

<sub>근거: CCAR-F-Udemy03-0002, CCAR-P-jrajath94-0676</sub>

### 1.21 상충 출처 표기
**상충은 임의로 고르지 않고 출처 · 날짜와 함께 표기**

| 상황 | 정답 |
|---|---|
| 신뢰할 두 출처의 통계가 정면 모순<br>(정부 보고서 40% vs 업계 분석 12%) | 두 값을 모두 담아 분석 완료<br>출처 attribution과 함께 충돌을 명시 주석<br>통합 전에 coordinator가 정합 방법 결정 |
| 문서 분석 subagent가 모순 발견 즉시 중단<br>"데이터 불일치" error만 반환<br>(1.8조 vs 2.4조) | 두 값 + 출처 유지 후 분석을 끝까지 완료<br>선택은 coordinator에 위임 |
| 사내 문서 보증 12개월(2024) vs 24개월(2026) | 출처를 밝혀 답변<br>두 값 + 각 문서 + 날짜 제시<br>더 최신이 현재 기준일 가능성 + 충돌을 검토 대상으로 표시 |
| 정부 45만 vs 업계 62만<br>통합이 "새로워 보여" 한쪽만 채택 | 구조화 출력에 공개일 · 수집일 포함<br>두 값을 출처와 병기 + 모순 주석 |

| 역할 | 내용 |
|---|---|
| 문서 분석 agent | 막히지 않고 핵심 분석 완료<br>충돌하는 두 값을 출처와 함께 보존 |
| coordinator | 더 넓은 context로 조정 방법 결정 |
| synthesis | 임의로 값을 고르지 않음 |
| 운용 | 출력 schema에 모순 유무 + 각 값의 출처<br>→ coordinator가 기계적으로 검출 |
| 날짜 metadata | 시간적 차이를 모순으로 오해하는 것을 방지 |

| 오답 | 이유 |
|---|---|
| confidence heuristic으로 한쪽 선택 + 각주 | 한쪽 값을 임의로 선택 |
| 충돌 표시 없이 두 값 모두 넣고 synthesis가 결정 | 충돌 미표시 · 조정 책임이 잘못된 곳 |
| 분석을 멈추고 coordinator에게 권위 판단 요청 후 대기 | 분석 agent는 막히지 않고 핵심 작업을 끝내야 함 |
| 최신 값만 채택 · 구값을 출력에서 제거 | 이유 확인 없이 한쪽 버림 · 출처 소실 |
| 최신 문서 우선 · 충돌 미언급 | 조용한 선택 = anti-pattern<br>문서끼리 어긋남을 아무도 모름 |
| 두 값의 평균 (18개월 · 2.1조 · 53.5만) | 어느 출처에도 없는 수치 생성 |
| 권위 있는 출처(정부 통계)를 일률 우선 | 이유를 확인하지 않은 선택 |
| 문서가 고쳐질 때까지 답변 거부 | 단서를 달아 줄 수 있는 답을 안 내놓음 |

![상충하는 두 출처 값을 출처와 함께 coordinator까지 전달하는 흐름](svg/10-conflicting-sources.svg)
*그림: 분석 agent는 막히지 않고 두 값과 출처 · 날짜를 보존하고 정합 방법은 coordinator가 정한다*

<sub>근거: CCAR-F-MyPractice-0001, CCAR-F-Udemy04-0011, CCAR-F-Udemy06-0014, CCAR-F-paullarionov-0001, CCAR-F-preporato-0030</sub>

## 2. 상황별 정답 판단 규칙

| 상황 | 정답 방향 |
|---|---|
| 고객이 사람을 요청 · 정책 공백 · 진전 없음 · 정책상 승인 필수 | `escalate_to_human` |
| 감정 격앙 · 낮은 자기 보고 confidence<br>· turn 수 초과 | escalation 사유 ✗ → 직접 처리<br>(진전 없는 반복은 사유 ✓) |
| escalation 경계가 흐려 단순 ↔ 복잡 사례가 뒤바뀜 | system prompt에 명시 기준 + few-shot |
| escalation 시 담당자가 대화를 재독 | 구조화 handoff 요약 |
| 이름 검색이 다건 일치 | 추가 식별자를 사용자에게 요청 |
| 사용자 선호가 직접 모순 | 충돌을 드러내고 확인 질문 |
| 모호한 요청 + 질문 과다로 이탈 | 가정을 명시하고 진행 · 수정 초대 |
| subagent 실패 | structured error context<br>(유형 · 쿼리 · 부분 결과 · 대안) |
| 일시 실패 | subagent 안에서 retry · 해결 불가만 coordinator로 |
| timeout vs `0 results` | 접근 실패와 유효한 빈 결과를 구분 |
| 병렬 tool 호출 일부 실패 | 성공 결과 + `is_error: true` 결과를 함께 반환 |
| 일부 출처 · 지역 실패 | 성공분 보존 + coverage annotation |
| 실행 중단 후 재개 | manifest checkpoint<br>+ idempotent side effect |
| 조용한 실패 · 건너뜀 방지 | 검증 단계 + fallback · handoff 검증 · 소유자 알림 |
| 결정 불가한 안전 게이트 | fail closed → 자격 있는 사람에게 이관 |
| 대규모 탐색으로 메인 context 소진 | `Explore` subagent로 격리 · 요약만 수신 |
| 후속 subagent의 중복 조사 | 이전 핵심 발견을 위임 prompt에 요약 주입 |
| 장시간 session에서 일반론 답변 · 초반 발견 누락 | 확인된 사실을 노트 · scratchpad 파일에 기록<br>(선택지에 없으면 `/compact` + 남길 결과 지시) |
| 되돌림 가능 · 저위험 · 대량 | post-action 표본 검토 + audit logging |
| 결과 중대 · 법적 책임 · 되돌림 불가 | pre-action 승인 (전체 컨텍스트 제공) |
| 검토 대량 + 위험도 이질 | 위험도 · 영향도로 routing · 일상은 표본 QA |
| 검토자 승인율 높은데 결함 잔존 · 피로 | 의사결정 컨텍스트 제공 · 순환 · 세션 상한 |
| 중대 결과 + 모델이 확신하며 틀릴 가능성 | 모델과 독립적인 검증 |
| 리뷰 용량 한정 | 필드별 confidence 보정 + 모호 · 모순 · 저신뢰 우선 |
| 자동화 확대 전 정확도 검증 | 문서 유형 · 필드별 측정 · 충족 구분만 축소 |
| 고신뢰 구간의 새 오류 조기 검출 | 층화 무작위 추출 + 층별 오류율 |
| 주장의 출처 · 날짜 소실 | claim · source · date를 구조화 handoff로 유지 |
| 근거가 본문에 없는 추출 필드 | unknown 반환 + 증거 부족 주석 |
| 신뢰할 출처 간 값 충돌 | 두 값 + 출처 + 날짜 표기 · coordinator가 정합 |

![reliability 상황을 네 갈래로 나눠 정답 방향을 고르는 decision tree](svg/10-decision-reliability.svg)
*그림: 상황이 사람 확인, 실행 실패, 검토 설계, 출처 · 근거 중 어디에 속하는지로 정답 방향이 갈린다*

<sub>근거: CCAR-F-Amey-Thakur-0009, CCAR-F-Amey-Thakur-0034, CCAR-F-Amey-Thakur-0035, CCAR-F-Amey-Thakur-0038, CCAR-F-Amey-Thakur-0044, CCAR-F-Amey-Thakur-0045, CCAR-F-Amey-Thakur-0050, CCAR-F-Amey-Thakur-0079, CCAR-F-Amey-Thakur-0080, CCAR-F-MyPractice-0001, CCAR-F-MyPractice-0003, CCAR-F-MyPractice-0005, CCAR-F-MyPractice-0006, CCAR-F-MyPractice-0009, CCAR-F-MyPractice-0012, CCAR-F-MyPractice-0028, CCAR-F-MyPractice-0045, CCAR-F-MyPractice-0049, CCAR-F-MyPractice-0050, CCAR-F-MyPractice-0055, CCAR-F-MyPractice-0063, CCAR-F-MyPractice-0074, CCAR-F-MyPractice-0076, CCAR-F-Udemy01-0004, CCAR-F-Udemy02-0003, CCAR-F-Udemy02-0014, CCAR-F-Udemy02-0022, CCAR-F-Udemy02-0029, CCAR-F-Udemy02-0044, CCAR-F-Udemy02-0052, CCAR-F-Udemy03-0002, CCAR-F-Udemy03-0014, CCAR-F-Udemy03-0022, CCAR-F-Udemy03-0034, CCAR-F-Udemy04-0011, CCAR-F-Udemy04-0015, CCAR-F-Udemy04-0025, CCAR-F-Udemy04-0038, CCAR-F-Udemy04-0039, CCAR-F-Udemy04-0041, CCAR-F-Udemy05-0023, CCAR-F-Udemy05-0030, CCAR-F-Udemy05-0031, CCAR-F-Udemy05-0044, CCAR-F-Udemy05-0051, CCAR-F-Udemy06-0014, CCAR-F-Udemy06-0015, CCAR-F-Udemy06-0028, CCAR-F-Udemy06-0036, CCAR-F-Udemy06-0043, CCAR-F-Udemy06-0054, CCAR-F-Udemy06-0055, CCAR-F-paullarionov-0001, CCAR-F-paullarionov-0003, CCAR-F-paullarionov-0005, CCAR-F-paullarionov-0006, CCAR-F-paullarionov-0009, CCAR-F-paullarionov-0012, CCAR-F-paullarionov-0045, CCAR-F-paullarionov-0049, CCAR-F-paullarionov-0050, CCAR-F-paullarionov-0055, CCAR-F-preporato-0002, CCAR-F-preporato-0006, CCAR-F-preporato-0008, CCAR-F-preporato-0030, CCAR-P-Amey-Thakur-0042, CCAR-P-Amey-Thakur-0072, CCAR-P-jrajath94-0035, CCAR-P-jrajath94-0216, CCAR-P-jrajath94-0217, CCAR-P-jrajath94-0218, CCAR-P-jrajath94-0219, CCAR-P-jrajath94-0221, CCAR-P-jrajath94-0315, CCAR-P-jrajath94-0378, CCAR-P-jrajath94-0440, CCAR-P-jrajath94-0503, CCAR-P-jrajath94-0566, CCAR-P-jrajath94-0567, CCAR-P-jrajath94-0600, CCAR-P-jrajath94-0676, CCAR-P-jrajath94-0679, CCAR-P-preporato-0022</sub>

## 3. 자주 나오는 오답 함정

| 오답 유형 | 틀린 이유 |
|---|---|
| 더 큰 모델 · 긴 prompt · 예시 · 긴 context | 평균 개선일 뿐 잘못된 출력 감지 ✗ |
| 감정 · 자기 보고 confidence · turn 수<br>· 주문 경과일을 escalation 기준으로 | 정책 공백 · 진전 없음 · 명시 요청이 기준 |
| 다건 일치에서 최근 활동 기준으로 1건 선택 | 추측 → 오계정 |
| 한쪽 값 임의 선택 · 평균 · 조용한 최신 우선 | 출처 소실 · 없는 수치 생성 |
| 실패를 빈 결과 · 성공으로 변환 | 오류 은폐 |
| 1건 실패로 전체 중단 · 전체 재실행 | 완료분 폐기 · 비용 증가 |
| "실패" 일반 상태만 · 성공률 하나로 집계 | 복구 판단 정보 소실 |
| 권한 오류에 backoff retry | 기다려도 해소 ✗ |
| 가정을 숨기거나 질문을 쏟아냄 | 통제권 없음 · 이탈 |
| 검증 통과분만으로 정확도 보고 · 전체 정확도 하나만 신뢰 | 편향 · 구분별 저성능 은폐 |
| 고신뢰 구간 무검토 · 임계값만 상향 | 자신 있게 틀린 오류 · 신종 오류 놓침 |
| 전량 pre-action · 고정 비율 표본 · 로그 없음 | 위험 · 되돌림 가능성 무시 |
| 검토 시간 · 인원 · 같은 화면 검토자 추가 | 볼 수 없음 · 피로가 원인 |
| 요약 단축 · 참고문헌 목록 · 사후 검색으로 출처 복원 | 주장 단위 대응 소실 |
| 모델이 모델을 검증 (재확인 · 두 모델 일치) | 독립성 없음 |
| 탐색을 메인에서 수행 + `/compact`<br>· plan mode · 일괄 로딩 | 사후 처리 · 격리 ✗ |
| 누락을 값으로 메우는 대응 (필수화 · `max_tokens` · 재검색) | 근거가 없으면 올바른 레코드 불가 |
| 로깅 · 모니터링으로 예방을 대체 | 로그는 건너뜀을 보여 줄 뿐 막지 못함 |
| `strict tool use` · `evaluated_permission`<br>· citations + structured outputs 병용 | 값 검증 · 일시 중지 · 병용 가능으로 오해 |
| 제약을 바꾸는 선택지<br>(모델 교체 · 모델 호출 추가<br>· 전건 검토 요구 시 표본 검토 · 필터링) | 문항 제약 위반 |

<sub>근거: CCAR-F-Amey-Thakur-0009, CCAR-F-Amey-Thakur-0034, CCAR-F-Amey-Thakur-0035, CCAR-F-Amey-Thakur-0038, CCAR-F-Amey-Thakur-0044, CCAR-F-Amey-Thakur-0045, CCAR-F-Amey-Thakur-0050, CCAR-F-Amey-Thakur-0079, CCAR-F-Amey-Thakur-0080, CCAR-F-MyPractice-0001, CCAR-F-MyPractice-0003, CCAR-F-MyPractice-0005, CCAR-F-MyPractice-0006, CCAR-F-MyPractice-0009, CCAR-F-MyPractice-0012, CCAR-F-MyPractice-0028, CCAR-F-MyPractice-0045, CCAR-F-MyPractice-0049, CCAR-F-MyPractice-0050, CCAR-F-MyPractice-0055, CCAR-F-MyPractice-0063, CCAR-F-MyPractice-0074, CCAR-F-MyPractice-0076, CCAR-F-Udemy01-0004, CCAR-F-Udemy02-0003, CCAR-F-Udemy02-0014, CCAR-F-Udemy02-0022, CCAR-F-Udemy02-0029, CCAR-F-Udemy02-0044, CCAR-F-Udemy02-0052, CCAR-F-Udemy03-0002, CCAR-F-Udemy03-0014, CCAR-F-Udemy03-0022, CCAR-F-Udemy03-0034, CCAR-F-Udemy04-0011, CCAR-F-Udemy04-0015, CCAR-F-Udemy04-0025, CCAR-F-Udemy04-0038, CCAR-F-Udemy04-0039, CCAR-F-Udemy04-0041, CCAR-F-Udemy05-0023, CCAR-F-Udemy05-0030, CCAR-F-Udemy05-0031, CCAR-F-Udemy05-0044, CCAR-F-Udemy05-0051, CCAR-F-Udemy06-0014, CCAR-F-Udemy06-0015, CCAR-F-Udemy06-0028, CCAR-F-Udemy06-0036, CCAR-F-Udemy06-0043, CCAR-F-Udemy06-0054, CCAR-F-Udemy06-0055, CCAR-F-paullarionov-0001, CCAR-F-paullarionov-0003, CCAR-F-paullarionov-0005, CCAR-F-paullarionov-0006, CCAR-F-paullarionov-0009, CCAR-F-paullarionov-0012, CCAR-F-paullarionov-0045, CCAR-F-paullarionov-0049, CCAR-F-paullarionov-0050, CCAR-F-paullarionov-0055, CCAR-F-preporato-0002, CCAR-F-preporato-0006, CCAR-F-preporato-0008, CCAR-F-preporato-0030, CCAR-P-Amey-Thakur-0042, CCAR-P-Amey-Thakur-0072, CCAR-P-jrajath94-0035, CCAR-P-jrajath94-0216, CCAR-P-jrajath94-0217, CCAR-P-jrajath94-0218, CCAR-P-jrajath94-0219, CCAR-P-jrajath94-0221, CCAR-P-jrajath94-0315, CCAR-P-jrajath94-0378, CCAR-P-jrajath94-0440, CCAR-P-jrajath94-0503, CCAR-P-jrajath94-0566, CCAR-P-jrajath94-0567, CCAR-P-jrajath94-0600, CCAR-P-jrajath94-0676, CCAR-P-jrajath94-0679, CCAR-P-preporato-0022</sub>

## 4. 암기 목록

| 이름 | 의미 |
|---|---|
| escalation 트리거 | 사람 요청 · 정책 예외 · 공백 · 진전 없음<br>· 승인 기준 초과 · 규정 필수 안건 |
| `escalate_to_human` | 사람 담당자 이관 tool |
| 구조화 handoff 요약 | 고객 ID · 근본 원인 · 권장 조치 · 시도한 절차 |
| structured error context | 실패 유형 · 실행한 쿼리 · 부분 결과 · 대안 |
| `is_error: true` | `tool_result`의 실패 표시<br>→ Claude가 retry · 설명 · escalation 선택 |
| 접근 실패 vs 유효한 빈 결과 | `Connection timeout` vs `0 results` |
| coverage annotation | 근거 탄탄한 결론 vs 공백 영역 표기 |
| graceful degradation | 투명성을 유지하며 기능을 점진적으로 축소 |
| checkpoint · manifest | 완료 · 남은 항목 · 결과를 저장해 재개 |
| idempotent | 재실행해도 중복 side effect 없음 |
| fail closed | 결정 불가 시 기본 거부 · 자격 있는 사람에게 이관 |
| pre-action vs post-action | 실행 전 승인 vs 실행 후 표본 검토 |
| 되돌림 가능성 · 결과 중대성 | 검토 형태를 정하는 두 축 |
| four-eyes 검토 | 양쪽 모두 전체 컨텍스트를 갖춘 이중 검토 (위험도 극단 결정) |
| context rot | token 증가에 따른 정확도 · 회상 저하 |
| scratchpad · notes 파일 | 확인한 사실을 대화 밖에 기록 |
| `Explore` subagent | 변경 없이 코드베이스 검색 · 이해, 별도 context |
| calibration | 필드별 confidence를 라벨 검증 세트로 정확도와 대응 |
| 층화 무작위 추출 | 유형별 층에서 무작위 추출해 층별 오류율 측정 |
| provenance | 각 주장을 출처에 연결해 유지 |
| claim record | 출처 위치 · 발행일 · 근거 발췌를 담은 구조 |
| 날짜 metadata | 공개일 · 수집일 → 시간 차이를 모순으로 오해 방지 |
| `stop_reason: end_turn` | 끝까지 생성됨 (정확성 보증 ✗) |
| `evaluated_permission` | tool 호출 이벤트의 결정 보고 필드 (일시 중지 제어 ✗) |

<sub>근거: CCAR-F-Amey-Thakur-0034, CCAR-F-Amey-Thakur-0035, CCAR-F-Amey-Thakur-0038, CCAR-F-Amey-Thakur-0044, CCAR-F-Amey-Thakur-0045, CCAR-F-Amey-Thakur-0079, CCAR-F-Amey-Thakur-0080, CCAR-F-MyPractice-0001, CCAR-F-MyPractice-0003, CCAR-F-MyPractice-0005, CCAR-F-MyPractice-0006, CCAR-F-MyPractice-0009, CCAR-F-MyPractice-0012, CCAR-F-MyPractice-0028, CCAR-F-MyPractice-0045, CCAR-F-MyPractice-0049, CCAR-F-MyPractice-0050, CCAR-F-MyPractice-0063, CCAR-F-MyPractice-0074, CCAR-F-MyPractice-0076, CCAR-F-Udemy01-0004, CCAR-F-Udemy02-0014, CCAR-F-Udemy02-0022, CCAR-F-Udemy02-0029, CCAR-F-Udemy02-0044, CCAR-F-Udemy02-0052, CCAR-F-Udemy03-0022, CCAR-F-Udemy03-0034, CCAR-F-Udemy04-0011, CCAR-F-Udemy04-0015, CCAR-F-Udemy04-0025, CCAR-F-Udemy04-0038, CCAR-F-Udemy04-0039, CCAR-F-Udemy04-0041, CCAR-F-Udemy05-0023, CCAR-F-Udemy05-0030, CCAR-F-Udemy05-0044, CCAR-F-Udemy05-0051, CCAR-F-Udemy06-0014, CCAR-F-Udemy06-0015, CCAR-F-Udemy06-0028, CCAR-F-Udemy06-0043, CCAR-F-Udemy06-0054, CCAR-F-Udemy06-0055, CCAR-F-paullarionov-0001, CCAR-F-paullarionov-0003, CCAR-F-paullarionov-0005, CCAR-F-paullarionov-0006, CCAR-F-paullarionov-0009, CCAR-F-paullarionov-0012, CCAR-F-paullarionov-0045, CCAR-F-paullarionov-0049, CCAR-F-paullarionov-0050, CCAR-F-preporato-0002, CCAR-F-preporato-0006, CCAR-F-preporato-0008, CCAR-F-preporato-0030, CCAR-P-Amey-Thakur-0042, CCAR-P-jrajath94-0035, CCAR-P-jrajath94-0216, CCAR-P-jrajath94-0217, CCAR-P-jrajath94-0218, CCAR-P-jrajath94-0219, CCAR-P-jrajath94-0221, CCAR-P-jrajath94-0315, CCAR-P-jrajath94-0378, CCAR-P-jrajath94-0440, CCAR-P-jrajath94-0503, CCAR-P-jrajath94-0566, CCAR-P-jrajath94-0567, CCAR-P-jrajath94-0600, CCAR-P-jrajath94-0679, CCAR-P-preporato-0022</sub>

## 5. 시험 직전 체크리스트

- [ ] escalation 사유(요청 · 정책 공백 · 진전 없음 · 승인 기준 초과 · 규정 필수 안건)와 비사유 구분
- [ ] 다건 일치는 추측 ✗ · 식별자 요청
- [ ] subagent 실패는 유형 · 쿼리 · 부분 결과 · 대안 전달
- [ ] 빈 결과 성공 처리 · 조용한 건너뜀 · 전체 중단 = 오답
- [ ] timeout vs `0 results` 구분
- [ ] 성공분 보존 + coverage annotation
- [ ] 상충 출처는 두 값 + 출처 + 날짜 표기
- [ ] 출처는 claim-source 구조로 synthesis까지 유지
- [ ] 되돌림 가능 post-action · 중대 pre-action
- [ ] 대표 표본 + 층화 검증 · confidence 보정 전 ✗

<sub>근거: CCAR-F-Amey-Thakur-0009, CCAR-F-Amey-Thakur-0034, CCAR-F-Amey-Thakur-0035, CCAR-F-Amey-Thakur-0038, CCAR-F-Amey-Thakur-0044, CCAR-F-Amey-Thakur-0045, CCAR-F-Amey-Thakur-0050, CCAR-F-Amey-Thakur-0079, CCAR-F-Amey-Thakur-0080, CCAR-F-MyPractice-0001, CCAR-F-MyPractice-0003, CCAR-F-MyPractice-0005, CCAR-F-MyPractice-0006, CCAR-F-MyPractice-0009, CCAR-F-MyPractice-0012, CCAR-F-MyPractice-0028, CCAR-F-MyPractice-0045, CCAR-F-MyPractice-0049, CCAR-F-MyPractice-0050, CCAR-F-MyPractice-0055, CCAR-F-MyPractice-0063, CCAR-F-MyPractice-0074, CCAR-F-MyPractice-0076, CCAR-F-Udemy01-0004, CCAR-F-Udemy02-0003, CCAR-F-Udemy02-0014, CCAR-F-Udemy02-0022, CCAR-F-Udemy02-0029, CCAR-F-Udemy02-0044, CCAR-F-Udemy02-0052, CCAR-F-Udemy03-0002, CCAR-F-Udemy03-0014, CCAR-F-Udemy03-0022, CCAR-F-Udemy03-0034, CCAR-F-Udemy04-0011, CCAR-F-Udemy04-0015, CCAR-F-Udemy04-0025, CCAR-F-Udemy04-0038, CCAR-F-Udemy04-0039, CCAR-F-Udemy04-0041, CCAR-F-Udemy05-0023, CCAR-F-Udemy05-0030, CCAR-F-Udemy05-0031, CCAR-F-Udemy05-0044, CCAR-F-Udemy05-0051, CCAR-F-Udemy06-0014, CCAR-F-Udemy06-0015, CCAR-F-Udemy06-0028, CCAR-F-Udemy06-0036, CCAR-F-Udemy06-0043, CCAR-F-Udemy06-0054, CCAR-F-Udemy06-0055, CCAR-F-paullarionov-0001, CCAR-F-paullarionov-0003, CCAR-F-paullarionov-0005, CCAR-F-paullarionov-0006, CCAR-F-paullarionov-0009, CCAR-F-paullarionov-0012, CCAR-F-paullarionov-0045, CCAR-F-paullarionov-0049, CCAR-F-paullarionov-0050, CCAR-F-paullarionov-0055, CCAR-F-preporato-0002, CCAR-F-preporato-0006, CCAR-F-preporato-0008, CCAR-F-preporato-0030, CCAR-P-Amey-Thakur-0042, CCAR-P-Amey-Thakur-0072, CCAR-P-jrajath94-0035, CCAR-P-jrajath94-0216, CCAR-P-jrajath94-0217, CCAR-P-jrajath94-0218, CCAR-P-jrajath94-0219, CCAR-P-jrajath94-0221, CCAR-P-jrajath94-0315, CCAR-P-jrajath94-0378, CCAR-P-jrajath94-0440, CCAR-P-jrajath94-0503, CCAR-P-jrajath94-0566, CCAR-P-jrajath94-0567, CCAR-P-jrajath94-0600, CCAR-P-jrajath94-0676, CCAR-P-jrajath94-0679, CCAR-P-preporato-0022</sub>
