@@ ADD-TO: ### 1.3 Coordinator(orchestrator) 1개 + Subagent n개 구조

**Subagent 분리 · 분해 판단**

| 구분 | 내용 |
|---|---|
| 분리 근거 | 흐름마다 자기 context 필요<br>섞이면 양쪽 품질 저하 (= context 오염) |
| 근거 아님 | 단계 수 · 길이 · 출력 조립 · 속도<br>도구 차이 단독 · 병렬 가능성<br>→ 한 context · workflow로 처리 가능 |
| 위임 비용 | 명시 안 한 부모 context 손실<br>지연 = 보통 감소 ✗ · 증가 |
| 분해 정당 | 독립 하위 작업 + 서로 다른 도구 · 출처<br>→ 범위 한정 subagent 병렬 → synthesis 단계 |
| 영역별 위임 | 영역마다 고유 prompt · tool 필요<br>→ lead가 subagent에 위임 → 보고서 병합<br>subagent별 대화 기록 따로 유지 |
| 단일 agent 한계 | tool 전부 부여 = capability bloat<br>순차 수행 = 병렬 포기 · context 혼합 |
| 단일 agent 우위 | 작업이 얽혀 하나의 진화하는 context 공유 |
| 병렬 + 중앙 판단 | 메인이 Agent로 기동 → 요약 수신<br>모순 해소 · 후속 결정 = 한 곳 |

**Hub-and-spoke 통신**

| 구분 | 내용 |
|---|---|
| 흐름 | 결과 · 후속 위임 모두 coordinator 경유<br>subagent = 구조화 최종 결과 반환 |
| 이점 | 모든 상호작용 관찰<br>error 일관 처리<br>subagent별 전달 정보 통제 |
| 결과 통합 | 두 결과를 synthesis agent에 전달<br>→ 한곳에서 통합 · 제어 유지 |
| 직접 통신 증상 | 실패 간과 · 중복 요청 · 흐름 추적 불가<br>원인 = 전체를 관리하는 주체 없는 구성 |
| 속도 vs 통제 | coordinator 경유 = 대기 시간 단점<br>비동기 = 조정 · 상태 일관성 · error 전파 곤란 |

**위임 prompt 작성**

| 구분 | 내용 |
|---|---|
| 포함 항목 | 목적 · 출력 형식<br>도구 · 정보원 지침 · 작업 경계 |
| 지시 방식 | 목표 · 품질 기준 전달 → 방법은 subagent 판단<br>(예: 단위 · 2020년 이후 · 1차 자료)<br>단계별 절차서 ✗ → 예상 밖 상황 대응 불가 |
| 정보원 | 범위 = 조건으로 제시<br>탐색 순서 = subagent에 위임 |
| 필요 사실 | 판단에 필요한 최소 사실만 명시<br>(order id · 총액 · 구매일 · 고객 사유) |
| 선행 결과 | 결과 · 출처 metadata를 prompt에 직접 삽입<br>양 많으면 파일 저장 → 경로 + 요점 전달 |
| 기준 미달 시 | "기준 충족 정보 없음"을 결과에 명기<br>→ coordinator가 coverage 부족 판단 |

**위임 누락 진단**

| 증상 | 원인 | 조치 |
|---|---|---|
| 일반론만 · 수치 · 출처 없음<br>"앞서 언급한 조사" 표현 | 지시가 참조뿐<br>데이터 미전달 | 결과 · 출처를<br>prompt에 삽입 |
| 짧은 지시 후 인용 약함 | 출처가 통합 쪽에 미도달 | 데이터 삽입<br>+ 주장별 인용 요구 |
| PR 고유 증거 없는 일반 지적 | 일반 subagent = 빈 context | diff 발췌 · 실패 test 출력<br>· 리뷰 기준 삽입 |
| 상류 subagent 정상 · 통합만 실패 | 고장 지점 = 통합으로의 전달 | 로그에서 위임 prompt 확인 |

**Context 공유 방식 비교**

| 방식 | context | 적합 · 부적합 |
|---|---|---|
| 일반 subagent | 빈 context + 위임 prompt | 격리 · 좁은 작업 |
| fork (subagent) | 부모 대화 전체 상속 | 상속 필요 시 적합 (PR 증거 등)<br>격리 · 부모 보호 목적 ✗<br>(분기마다 이력 부담) |
| `fork_session`<br>(Agent SDK) | 이력 사본으로 시작<br>고유 session ID | 같은 분석에서 다른 방침 시도<br>독립 리뷰 ✗ (생성 시 추론 상속) |
| 새 session<br>· reviewer subagent | 생성 시 이력 없음 | 독립 리뷰<br>(diff · 사양 · 리뷰 기준만 전달) |
| agent team | 여러 session<br>공유 task list · peer 직접 메시지 | 판단 분산형<br>⚠️ 공식: 실험적 · 기본 비활성 → 시점에 따라 변동 |

**탐색 · 조사 위임**

| 구분 | 내용 |
|---|---|
| 대상 | 파일 목록 · 검색 결과 · test log로<br>메인이 반복해서 차는 긴 조사 |
| 방법 | 읽기 전용 subagent(`Explore` · 범용)에 위임<br>→ 경로 · 줄번호 요약만 반환 |
| 효과 | 탐색 수만 token → 요약 1,000~2,000 token<br>(해설 인용 규모)<br>메인 = 조정 담당 유지 |
| 조사 vs 수정 | 초점 좁은 읽기 전용 조사 먼저 → 요약으로 판단<br>원인 특정 전 변경 ✗ |

**병렬 worker 충돌 방지**

| 구분 | 내용 |
|---|---|
| 증상 | 결과 덮어쓰기 · 같은 대상 중복 조사 |
| 해법 | orchestrator가 겹치지 않는 범위 할당<br>결과 = 고유 키 달린 공유 구조화 저장소<br>orchestrator가 마지막에 병합 |
| 효과 | 범위 분리 → 중복 ✗ · 키 → 덮어쓰기 ✗<br>orchestrator 전체 가시성 유지 |

**호출 범위 · 도구 범위**

| 구분 | 내용 |
|---|---|
| 호출 | 고정 순서 지시 폐기<br>질문 요구 분석 → 필요한 subagent만 |
| 근거 | subagent 설명에 담당 작업 + 호출 조건 명시 |
| 작업량 | 단순 사실 확인 = agent 1개 + 소수 tool 호출<br>비교 · 복잡 조사 = subagent 증가 |
| 도구 | 역할 경계 = subagent별 `tools` 한정 |
| 경미한 확인 | 좁은 목적 tool(예: `verify_fact`) 부여<br>범위 넘는 조사 = coordinator로 반환 |

<sub>근거: CCAR-F-Amey-Thakur-0012, CCAR-F-Amey-Thakur-0052, CCAR-F-Amey-Thakur-0067, CCAR-F-MyPractice-0002, CCAR-F-MyPractice-0008, CCAR-F-Udemy01-0011, CCAR-F-Udemy01-0014, CCAR-F-Udemy01-0018, CCAR-F-Udemy01-0036, CCAR-F-Udemy01-0048, CCAR-F-Udemy02-0060, CCAR-F-Udemy03-0024, CCAR-F-Udemy03-0037, CCAR-F-Udemy04-0043, CCAR-F-Udemy04-0048, CCAR-F-Udemy05-0024, CCAR-F-Udemy05-0036, CCAR-F-Udemy05-0054, CCAR-F-Udemy06-0011, CCAR-F-paullarionov-0002, CCAR-F-paullarionov-0008, CCAR-F-preporato-0001, CCAR-P-jrajath94-0016, CCAR-P-jrajath94-0119, CCAR-P-jrajath94-0605, CCAR-P-preporato-0004</sub>

@@ NEW-SECTION
### Handoff 데이터 형식 — 출처 · 근거 보존
**본문과 metadata를 분리한 구조화 레코드로 전달**

| 구분 | 내용 |
|---|---|
| 증상 | 각 단계는 정상인데 최종 인용이 주장과 불일치<br>(provenance 소실 · 다른 논문 결론과 연결) |
| 원인 | 출처가 문장에 섞임<br>요약 압축 · 말 전달 게임식 중계 |
| 형식 | 본문 + metadata(URL · 문서명 · page 번호) 분리<br>근거 레코드 = 주장 · 출처 위치 · 취득 조건 |
| 이유 | 본문을 고쳐 써도 대응 관계가 데이터로 유지 |
| 확장 | 발견마다 고유 ID<br>보고서 주장 → ID 연결 → 사후 검증 가능 |

| 구간 | 조치 |
|---|---|
| subagent 반환 | 고정 schema로 필수 근거 반환<br>(file path · test 이름 · code 발췌) |
| coordinator → 통합 | 구조화 데이터를 요약 없이 그대로 전달<br>(요약 = 세부 소실 지점 증가) |
| 통합 전 | record에 비교용 metadata 있는지 검증<br>(관측 기간 · 측정 방법) |
| 통합 요청 | 주장마다 근거 인용 요구를 prompt에 명시 |

| 증상 | 원인 |
|---|---|
| 조건 다른 통계값이 한 경향으로 묶임 | 문장 요약 반환 → 비교용 metadata 누락 |
| 인용이 다른 문서와 연결 | 출처가 문장 속 → 통합 중 다시 쓰다 대응 붕괴 |
| 요약에서 파일 경로 · test명 · 코드 누락 | 반환 schema에 근거 항목 없음 |

<sub>근거: CCAR-F-Amey-Thakur-0003, CCAR-F-Udemy01-0003, CCAR-F-Udemy02-0012, CCAR-F-Udemy04-0024</sub>

@@ NEW-SECTION
### Coordinator 평가 · 재위임 · 실패 처리
**coordinator가 평가 → 부족분만 재위임 · 실패는 subagent 안에서 흡수**

| 구분 | 내용 |
|---|---|
| 평가 | 통합 출력을 품질 기준과 대조<br>(예: 숫자 주장 = 독립 출처 2개 이상 · 필수 관점 6개) |
| 재위임 | 부족한 부분만 범위 좁힌 query로<br>검색 · 분석 subagent에 재위임 → 통합 재호출 |
| 반복 | coverage 충족까지 반복<br>반복 상한 설정 |
| 상한 도달 | 미해결 항목에 주석(coverage 표기) → 보고서 진행 |
| 기준 위치 | 품질 기준 = coordinator prompt에 명기 |
| 누락 증상 | 통합 출력을 그대로 최종 보고서로 사용<br>→ 빠진 관점 · 근거 1개 주장 방치 |

| 구분 | 내용 |
|---|---|
| 일시 오류 | subagent 안에서 재시도 |
| 해결 안 될 때 | 오류 내용 · 시도 내용 · 확보한 정보원을 구조화 반환<br>→ coordinator가 내부를 안 보고 다음 수 결정 |
| 원칙 | 내부 실패 처리 = 내부<br>밖으로는 판단용 요약만 |
| 설계 방침 | 실패를 어디서 흡수하고 무엇을 위로 올릴지 설계<br>tool 실패를 agent에 알려 적응<br>+ 재시도 같은 확정적 안전장치 조합 |

<sub>근거: CCAR-F-Udemy01-0005, CCAR-F-Udemy04-0009, CCAR-F-Udemy06-0022</sub>

@@ NEW-SECTION
### Handoff contract와 불일치(disagree) 규칙
**contract = 입력 · 출력 · 병합 · 불일치 규칙**

| 요소 | 내용 |
|---|---|
| 입력 | worker별 입력 문서 (작업 한정) |
| 출력 | worker별 출력 형식 |
| 병합 규칙 | coordinator가 조각을 하나로 결합하는 방식<br>병합 규칙 없음 → 좋은 검토 3개가 한 보고서 ✗ |
| 불일치 규칙 | 충돌 시 우선 근거 또는 arbiter<br>coordinator가 적용 · 결정 기록 |
| checkpoint | 각 handoff 저장 → worker 실패 시 재개 |
| 비요소 | 문체 · 모델 등급 · 근무 시간<br>→ 비일관성 방지 못함 |
| ⚠️ 용어 | 해설 자체 용어 · 공식 문서에서 동일 정의 미확인<br>→ 구성 항목은 해설 기준 |

| 상황 | 해결 |
|---|---|
| worker 평가 충돌 + 규칙 없음 | 명명된 불일치 규칙<br>→ critic 단계 (원문 + 두 근거로 재검토)<br>→ 증거로 해결 불가 시 사람 escalation |
| 전문가 간 의견 충돌<br>(전사 vs 번역 12%) | contract가 중재자(arbiter) 지정<br>coordinator 적용 · 결정 기록<br>중재자 = 두 출력 + 원본 필요 |
| finding 우선순위 충돌 | 심각도 순서 또는 arbiter를 병합 시 적용 · 기록 |
| 반려 30% · 사유 없음 | 반려 사유 코드 + 재작업 경로 명시 |
| 매번 한쪽 worker 선택 | 암묵적 기본값 ✗<br>분쟁마다 우선 증거 · 이유 기록<br>log가 규칙 적용을 증명 |
| 병렬 독립 검토 + 마감 + 병합 | coordinator + 전문가 worker<br>contract(입력 · 출력 · 병합 규칙) + checkpoint |

| 구분 | 내용 |
|---|---|
| 한계 | critic = "해결 불가" 정의 없으면 전부 escalation<br>arbiter = 병목 · 중재 품질이 전체 품질 제한<br>나쁜 병합 규칙 = 일관되지만 틀린 결과 |
| 증설이 맞는 경우 | 문제가 충돌이 아닌 처리량<br>또는 작업이 독립 조각으로 더 나뉨 |
| 대안이 맞는 경우 | 평균 = 저위험 수치 추정<br>다수결 = 독립 다수 투표자 + 명확한 라벨 분류 |

<sub>근거: CCAR-P-jrajath94-0119, CCAR-P-jrajath94-0121, CCAR-P-jrajath94-0122, CCAR-P-jrajath94-0285, CCAR-P-jrajath94-0338, CCAR-P-jrajath94-0401, CCAR-P-jrajath94-0464, CCAR-P-jrajath94-0527</sub>

@@ NEW-SECTION
### 사람에게 handoff (escalation)
**검증 불가 · 명시적 요구는 사람에게 → 구조화 요약과 함께**

| 상황 | 처리 |
|---|---|
| 결과를 검증할 수 없는 단계 | 드러내기 → 행동 전 사람 확인 |
| 명시적 사람 요구 | 난이도 무관 즉시 사람 review |
| 단순 수정 요청<br>(원문에 명확한 근거) | 자동 복구 제공<br>복구 후 검증 실패 시 escalation |
| 판단이 망설여지는 지점 | 처리 중단 → checkpoint에서 사람 피드백 |

| 항목 | 내용 |
|---|---|
| 수신자 조건 | 대화 기록 접근 불가<br>(별도 ticket 시스템에서 작업) |
| 사실 | 검증된 customer ID · 근본 원인 분석<br>시도한 대처 · 사안별 항목(환불 금액 등) |
| 판단 | 권장 다음 조치 + 근거 |
| 기준 | 담당자가 되묻지 않고 대응 시작 가능한가 |
| 운영 | `escalate_to_human` 입력 schema에서 항목 필수화<br>→ 품질 편차 방지 |

<sub>근거: CCAR-F-Amey-Thakur-0015, CCAR-F-Udemy01-0060, CCAR-F-Udemy05-0010</sub>

@@ RULES
| 각 단계는 정상인데 최종 인용이 주장을 못 뒷받침 | handoff에서 출처 소실<br>→ 본문 + metadata 분리 구조화 레코드 |
| 통합 subagent 결과가 일반론 · 출처 없음 | 위임 prompt에 조사 결과 · 출처 직접 삽입<br>양 많으면 파일 저장 → 경로 전달 |
| 조건 다른 값이 한 경향으로 묶임 | 구조화 근거 레코드 반환<br>통합 전 필수 metadata 검증 |
| subagent 직접 통신 → 실패 간과 · 중복 · 추적 불가 | 모든 통신 coordinator 경유 |
| 통합 결과가 품질 기준 미달 | coordinator가 평가 → 부족분만 재위임<br>→ 통합 재호출 (반복 상한 + 미해결 주석) |
| 검색 subagent 일시 네트워크 오류 | subagent 내 재시도<br>→ 실패 시 오류 · 확보 정보원 구조화 반환 |
| 긴 조사로 메인 context 오염 | 읽기 전용 subagent에 위임<br>→ 경로 · 줄번호 요약만 반환 |
| 생성자와 독립된 리뷰 필요 | 새 session 또는 reviewer subagent<br>(diff · 사양 · 기준만 전달) · fork ✗ |
| 병렬 worker가 덮어쓰기 · 중복 | 겹치지 않는 범위 + 고유 키 저장소<br>+ orchestrator 마지막 병합 |
| worker 의견 충돌 | contract 불일치 규칙 (critic · arbiter)<br>적용 · 기록 |
| 단순 질문에도 전 subagent 호출 | 고정 순서 폐기 · 필요한 subagent만<br>subagent 설명에 호출 조건 명시 |
| 경미한 확인마다 막힘 + 역할 중복 | 좁은 `verify_fact` tool만 부여<br>범위 넘는 조사 = coordinator로 반환 |
| 사용자가 사람 대응을 명시 요구 | 난이도 무관 즉시 사람 review |
| 인수 담당자가 대화 기록 못 봄 | 구조화 handoff 요약<br>(ID · 원인 · 시도 · 권장 조치 + 근거) |
<sub>근거: CCAR-F-Amey-Thakur-0003, CCAR-F-Amey-Thakur-0015, CCAR-F-Udemy01-0003, CCAR-F-Udemy01-0005, CCAR-F-Udemy01-0011, CCAR-F-Udemy01-0018, CCAR-F-Udemy01-0036, CCAR-F-Udemy01-0048, CCAR-F-Udemy01-0060, CCAR-F-Udemy02-0012, CCAR-F-Udemy03-0037, CCAR-F-Udemy04-0009, CCAR-F-Udemy04-0043, CCAR-F-Udemy04-0048, CCAR-F-Udemy05-0010, CCAR-F-Udemy05-0036, CCAR-F-Udemy05-0054, CCAR-F-Udemy06-0011, CCAR-F-Udemy06-0022, CCAR-P-jrajath94-0016, CCAR-P-jrajath94-0122, CCAR-P-jrajath94-0285, CCAR-P-jrajath94-0401</sub>

@@ TRAPS
| 단계 수 · 길이 · 도구 차이 · 속도가 subagent 근거 | 한 context · workflow로 충분<br>위임 = 지연 증가 · 근거 = context 오염 |
| 최대 비용 = 큰 모델 · tool 불가 · token 2배 | 실제 비용 = 명시 안 한 부모 context 손실 |
| Agent tool 제거 + CLAUDE.md 암묵 선택<br>· 리뷰어끼리 직접 메시지 · 이력 상속 | 중앙 판단 · 요약 통합 요건과 불일치 |
| 공유 대화 기록으로 lead가 모든 턴 열람 | subagent별 대화 기록 따로 유지<br>lead = 최종 보고서 수신 |
| 한 agent에 tool 전부 부여 후 순차 분석 | capability bloat · 병렬 포기 · context 혼합 |
| 병합 없는 별도 agent 3개 + 수작업 병합 | synthesis · 병합 규칙 부재 → 일관성 ✗ |
| 판단 필요한 검토를 모델 없는 workflow로 | 판단 제거 |
| 경유 이점 = API 호출 감소 · 자동 retry · 직렬화 | 이점 아님<br>이점 = 관찰 · error 일관 처리 · 정보 통제 |
| 원본 출력을 이어 붙여 최종 결과로 반환 | synthesis 없음 · 통합 품질 ✗ |
| 한 agent가 다른 agent에 직접 결과 전달 · 요청 | coordinator 제어 상실 |
| 공유 scratchpad · peer 메시지 · 전체 이력 공유 | 조정 책임 분산 → 모순 · 중복 감지 주체 불명 |
| 로그 추가 · queue retry · dedup<br>· 직접 error 통지 | 부품 보강일 뿐 구성 문제 미해결<br>직접 주고받기 증가 |
| 통합 부실 원인 = 요약 과다 · window 초과<br>· 검색 tool 부재 | 원인 = 위임 prompt에 데이터 없음<br>(로그의 prompt 내용으로 확인) |
| 부모 이력 상속 설정 · system prompt에 부모 대화 참조 | 일반 subagent는 상속 ✗ |
| @멘션 호출 · 통합 subagent에 Agent tool 추가 | 도달 정보 불변 |
| 직접 통신 · agent team 재구성<br>으로 인용 손실 해결 | 정보 경로만 증가 · 전달 결락 불변 |
| 통합 subagent에 검색 tool 주고 재조사 | 중복 · 오용 위험 · 역할 경계 붕괴 |
| 원본 대화 전체 · 모든 tool 출력 전달 | 무관 자료에 token · attention 낭비<br>(lost-in-the-middle) |
| 위임받은 agent가 고객에게 재질문 | coordinator가 가진 사실로 메울 틈을 고객에 전가 |
| 부모 transcript 읽기 지시<br>· 이전 CI transcript 의존 | 일반 subagent 접근 불가<br>→ prompt 포함 또는 fork |
| 단계별 절차서형 위임 | 예상 밖 상황 대응 수단 ✗<br>품질 기준 미전달 → 오래된 자료 반환 |
| 부모 대화를 fork로 상속시켜 탐색 격리 | 분기마다 무거운 context<br>격리 효과 ✗ |
| 메인 직접 탐색 후 compaction · transcript 붙여넣기 | 압축 전까지 context 비대 · 원본 출력 유입 |
| 조사와 수정을 한 subagent에 동시 | 원인 특정 전 변경 |
| prompt에 "출처 정확히" 명시 · 사후 출처 재부여 | 확률적 대책 · 사후 재부여 = 대응 관계 추측 |
| 논문 전문 · 추출 텍스트 전체를 통합에 전달 | 분할 이점 상실 · context 압박 |
| coordinator가 결과 요약 후 통합에 전달 | 세부 소실 지점 증가 |
| fork로 부모 맥락 상속시켜 출력 형태 개선 | 출력 형태 불변 |
| CLAUDE.md에 지침 저장 → 이번 전달 누락 해결 | 향후 실행용 · 이번 누락 미해결 |
| 평가를 사람에게 회부 · 주석만 달고 진행 · 전체 재실행 | 느림 · 재조사 생략 · 범위 미축소 |
| 검색 상한 2배 · "데이터 없음" 명기 · 통합에 검색 tool | 부족 확인 없는 양 증가 · 조사 전 포기 · 역할 붕괴 |
| coordinator가 내부 tool 호출 검사<br>· 부모 tool 상속 · 대체 tool | subagent 분리 붕괴 |
| 실패 시 빈 성공 결과 반환 | 실패 은폐 → 통합이 누락을 추측 |
| 고정 4개 순차 → 4개 병렬 · 앞단 분류 모델 | 호출 범위 불변 · 과잉 설계 |
| tool 제거 후 확인마다 승인 · 같은 권한 · 역할 합치기 | 정체 악화 · 중복 재발 · 효과 없음 |
| 순차 실행으로 충돌 회피 | 병렬성 파괴 (researcher 6개 = 6배 시간) |
| 개인 memory + 출력 이어 붙임 · peer 채팅 | 중복 · 병합 충돌 · 비구조 · orchestrator 가시성 ✗ |
| fork_session · 비판 지시 · 상위 모델로 독립 리뷰 | 이력에 생성 시 추론 잔존 = self-review |
| 충돌 평가를 평균 · 선착순 · 3번째 worker 다수결 | 아무도 안 낸 판단 · 임의 · 증거 없는 투표 |
| 두 worker 일치할 때까지 재실행 | 종료 보장 없음 · 예산 소진 |
| 전사와 번역 충돌을 다수결 · 특정 worker 우선 | 서로 다른 것을 판단 · 위세로 승자 · 재발 |
| 불일치 해법 = 더 큰 모델 · worker 추가 · timeout 연장 | 자원 추가일 뿐 규칙 아님 |
| 검증 불가 단계를 그대로 진행 · 기록만 · 2회 일치까지 재시도 | 미검증 근거로 행동 · 일관성 ≠ 진실 |
| 불만도 점수 · 추출 난이도로 사람 인계 결정 | 명시 요구라는 가장 확실한 신호를 대체 |
| 인계에 대화 전문 첨부 · 감정 점수 · turn 수 | 요점 불명 · 내용 없음 → 담당자 재질문 |
<sub>근거: CCAR-F-Amey-Thakur-0003, CCAR-F-Amey-Thakur-0012, CCAR-F-Amey-Thakur-0015, CCAR-F-Amey-Thakur-0052, CCAR-F-Amey-Thakur-0067, CCAR-F-MyPractice-0002, CCAR-F-MyPractice-0008, CCAR-F-Udemy01-0003, CCAR-F-Udemy01-0005, CCAR-F-Udemy01-0011, CCAR-F-Udemy01-0014, CCAR-F-Udemy01-0018, CCAR-F-Udemy01-0036, CCAR-F-Udemy01-0048, CCAR-F-Udemy01-0060, CCAR-F-Udemy02-0012, CCAR-F-Udemy02-0060, CCAR-F-Udemy03-0024, CCAR-F-Udemy03-0037, CCAR-F-Udemy04-0009, CCAR-F-Udemy04-0024, CCAR-F-Udemy04-0043, CCAR-F-Udemy04-0048, CCAR-F-Udemy05-0010, CCAR-F-Udemy05-0024, CCAR-F-Udemy05-0036, CCAR-F-Udemy05-0054, CCAR-F-Udemy06-0011, CCAR-F-Udemy06-0022, CCAR-F-paullarionov-0002, CCAR-F-paullarionov-0008, CCAR-F-preporato-0001, CCAR-P-jrajath94-0016, CCAR-P-jrajath94-0119, CCAR-P-jrajath94-0122, CCAR-P-jrajath94-0285, CCAR-P-jrajath94-0605, CCAR-P-preporato-0004</sub>

@@ MEMO
| provenance | 주장과 출처의 대응 정보 · handoff 중 소실 위험 |
| hub-and-spoke (star) | 모든 통신 coordinator 경유<br>(관찰 · error · 정보 통제) |
| 근거 레코드 | 주장 · 출처 위치 · 취득 조건을 담은 구조화 단위 |
| handoff contract | 입력 · 출력 · 병합 규칙 · 불일치 규칙<br>(해설 용어) |
| disagree rule | 충돌 시 우선 근거 · arbiter 지정 + 적용 기록 |
| arbiter | worker 충돌을 contract 규칙대로 결정하는 중재자 |
| critic 단계 | 조항 원문 + 두 근거로 재검토 |
| checkpoint | 각 handoff 저장 → 실패 시 재개 · 사람 피드백 지점 |
| `Explore` | 읽기 전용 내장 subagent · 탐색을 메인에서 격리 |
| `fork_session` | 이력 사본 + 새 session ID로 분기<br>(대안 시도용 · 독립 리뷰 ✗) |
| agent team | 여러 session이 공유 task list로 협조 (실험적) |
| `escalate_to_human` | 사람 인계 tool · 입력 schema로 요약 항목 필수화 |
| `verify_fact` | 좁은 목적 확인 tool 예시 |
<sub>근거: CCAR-F-Amey-Thakur-0003, CCAR-F-Udemy01-0005, CCAR-F-Udemy01-0011, CCAR-F-Udemy01-0014, CCAR-F-Udemy01-0048, CCAR-F-Udemy04-0024, CCAR-F-Udemy04-0043, CCAR-F-Udemy05-0010, CCAR-F-Udemy05-0054, CCAR-P-jrajath94-0016, CCAR-P-jrajath94-0119, CCAR-P-jrajath94-0121, CCAR-P-jrajath94-0122, CCAR-P-jrajath94-0285, CCAR-P-jrajath94-0401, CCAR-P-jrajath94-0527</sub>

@@ CHECK
- [ ] 각 단계 정상 + 최종 오류 → handoff 소실 의심 (prompt 미포함 · metadata 미분리)
- [ ] subagent 간 통신 전부 coordinator 경유 (관찰 · error · 정보 통제)
- [ ] worker 충돌 → contract 불일치 규칙(critic · arbiter) 적용 · 기록
- [ ] 사람 인계 = 명시 요구 즉시 · 구조화 요약(ID · 원인 · 시도 · 권장 조치)
<sub>근거: CCAR-F-Amey-Thakur-0003, CCAR-F-Amey-Thakur-0015, CCAR-F-Udemy01-0060, CCAR-F-Udemy04-0043, CCAR-F-Udemy04-0048, CCAR-F-Udemy05-0010, CCAR-P-jrajath94-0122, CCAR-P-jrajath94-0285</sub>
