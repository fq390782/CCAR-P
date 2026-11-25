# 1. Agents and Workflows — 반드시 알아야 할 지식

> 커버: CCAR-P D1
> CCAR-P판: `Know(CCAR-F&P)`에서 자동 생성. 직접 고치지 않는다.

## 1. 핵심 개념

### 1.1 Workflow vs Agent — 다음 단계를 누가 정하나
**구분 기준 = 다음 단계 결정 주체 (코드 vs 모델)**

| 구분 | 정의 |
|---|---|
| Workflow | LLM · tool을 predefined code path로 엮은 시스템 |
| Workflow 흐름 | control flow = 설계 시점 고정 |
| Workflow 모델 호출 | 정해진 지점에서만 호출 |
| Agent | 모델이 실행 중 다음 단계 · tool 사용법 결정 |

| 오답 | 이유 |
|---|---|
| 길이 · tool 개수 · structured output 필요 여부로 구분 | 구분 기준 아님 |
| "workflow는 모델 못 부름" · "agent는 tool 못 씀" | workflow도 모델 호출 · agent도 tool 사용 |

| 상황 | 판단 |
|---|---|
| 중간 결과를 보기 전엔 필요한 단계를 모름<br>(= 경로를 실행 중 발견) | agent 필요 (유일한 신호) |
| 경로 고정 | 결정론적 orchestration → 저렴 · 빠름<br>테스트 · 감사 · 디버깅 용이 |
| 경로 고정 시 agent의 대가 | 비용 · 지연 · 비결정성 · 오류 연쇄 위험만 증가 |

**판단 순서**
1. 복잡도 · 경로 고정 여부 · 코드로 싼 오류 방지 가능 여부 확인
2. 요구를 만족하는 **가장 단순한 구성** 선택

| 상황 | 가장 단순한 구성 |
|---|---|
| 매핑 고정 변환 | deterministic script (agent loop ✗) |
| 해석 필요 필드 존재 | schema 둔 단일 모델 호출 |

| 상황 | 판단 |
|---|---|
| 절차를 사전에 확정 가능한 업무 | 고정 경로 orchestration 적합 |
| 같은 유형 요청도 필요한 대응이 건마다 다름<br>(설명만 · 주문 조회 · escalation 선행) | 고정 경로 ✗ → agent loop |
| `tool_choice` `auto` (기본값) | tool 사용 · 직접 답변을 매 turn Claude가 판단 |
| 앱 상태로 다음 tool 강제<br>· 분류기로 정형 체인에 분기 | 판단을 앱 코드로 되돌림<br>→ 가변 요청에 부적합 |

**작업 형태별 패턴 선택**

| 작업 형태 | 패턴 |
|---|---|
| 순서 고정 · 규칙 알려짐 · 입력 형식 일정 | deterministic workflow<br>모델 호출 = 모호한 부분에만 |
| 고정 경로 + 열린 단계 1개<br>(리뷰 코멘트 작성 등) | augmented LLM = 도구 가진 workflow<br>agentic ✗ |
| 검색 1회 + 판단 1회로 해결 | augmented single call<br>loop · multi-agent ✗ |
| 단계를 실행 전엔 나열 불가<br>발견이 다음 검색을 결정 | agentic loop<br>+ step 상한 · 중지 규칙 |
| 같은 순서 · 같은 trace 요구<br>(고정 체크리스트 검토 등) | deterministic workflow<br>agent = 실행마다 계획이 달라짐 |
| 고정 형식 파싱 (EDI 등) | parser · 결정론적 코드<br>모델 · 최상위 tier ✗ |
| 맞춤 답장 작성<br>(판단 1회 + 도구) | augmented single call<br>발송 전 어조 · 사실 확인 |
| 원인 모르는 장애 조사 | step budget 둔 agentic loop |

**이름이 통제를 결정**

| 구분 | 내용 |
|---|---|
| 판단 기준 | tool 사용 여부 ✗<br>단계를 누가 정하나 |
| 고정 경로 | validation gate 필요<br>loop 통제(반복 제한 · escalation) 불필요 |
| 진짜 agentic loop | 반복 제한 · 중지 조건 필요 |
| 오분류 | 고정 pipeline에 loop 통제 적용<br>→ 복잡성만 증가 |

**고정 순서 pipeline이 실패하는 경우**

| 증상 | 조치 |
|---|---|
| 질문마다 필요한 절차가 다름<br>(테스트 실행 필요 · 파일 5개 초과) | tool 정의 후 loop에 위임<br>다음 tool = 결과를 본 Claude가 결정 |
| tool 선택 근거 부족 | 각 tool `description`에 용도 · 다른 tool과의 구분 기재<br>= tool 성능에 가장 큰 영향 |

**아키텍처 리뷰에서 workflow를 고르는 근거**

| 구분 | 내용 |
|---|---|
| 올바른 근거 | 경로가 사전에 확정<br>→ 결정론적 orchestration이 저렴<br>· 테스트 가능 · 감사 가능 · 신뢰 |
| 판단 틀 | 구조적 적합성<br>경로 알려짐 = 결정론 · 경로 열림 = agent |
| 자율성 정당화 | 모델이 경로를 골라야 하는 곳에서만 |

![Workflow와 agent를 다음 단계 결정 주체로 비교한 흐름도](svg/1-workflow-vs-agent.svg)
*그림: 중간 결과를 봐야 다음 단계를 알 수 있을 때만 agent이고, 경로가 고정이면 코드가 순서를 정하는 workflow가 맞다*

<sub>근거: Amey-0004, Amey-0023, Amey-0024, Amey-0040, Amey-0074, CCAR-F-Amey-Thakur-0011, CCAR-F-Amey-Thakur-0016, CCAR-F-Amey-Thakur-0051, CCAR-F-Udemy03-0060, CCAR-F-Udemy04-0028, CCAR-P-Amey-Thakur-0005, CCAR-P-Amey-Thakur-0045, CCAR-P-jrajath94-0013, CCAR-P-jrajath94-0018, CCAR-P-jrajath94-0117, CCAR-P-jrajath94-0118, CCAR-P-jrajath94-0337, CCAR-P-jrajath94-0400, CCAR-P-jrajath94-0463, Patrick-0012, Patrick-0022, Preporato-0016, Udemy-0014, Udemy-0053</sub>

### 1.2 Workflow 패턴 구분
**패턴 차이 = 분해를 누가 · 언제 정하나**

| 패턴 | 동작 | 특징 |
|---|---|---|
| prompt chaining | 고정 subtask 순차 호출<br>각 단계가 앞 단계 출력 수신<br>호출 순서 = 앱 코드 | 단계 사이 programmatic gate 삽입 가능<br>(schema 검증 · 필수 항목 검사)<br>지연 소폭 증가 → 정확도 · 예측 가능성 향상 |
| routing | 입력 분류 → 전용 후속 처리로 보내고 끝 | 분해 · 결과 통합 ✗ |
| parallelization (voting) | 같은 작업 여러 번 실행<br>→ 다수결 등으로 확신도 향상 | 작업 분해 ✗ |
| orchestrator-workers | 중심 LLM이 입력 보고 즉석에서 subtask 결정<br>→ worker LLM 위임 → 결과 통합 | 결정적 차이 = subtask 사전 정의 ✗<br>입력마다 분해가 달라지는 작업용 |
| evaluator-optimizer | 평가자 LLM 채점<br>→ 기준 넘을 때까지 생성 · 수정 반복 | 명확한 평가 기준 + 하나의 출력 다듬기<br>(번역 퇴고 등)<br>서로 다른 단계 순차 처리 ✗ |

- 단계 사이 checkpoint 필요 시 거대 prompt 1개 ✗ → 검증 지점 소실

**Chaining · routing 보강**

| 구분 | 내용 |
|---|---|
| chaining 분리 신호 | "중간 산출물을 로그로 남김" = 단계 분리 힌트<br>한 prompt에 전 파일 · 전 추출 결과 ✗<br>→ 파일별 오류 누락 · 합계 모순 |
| chaining 구성 | 파일별 검토 호출 → 중간 산출물 로그<br>→ 마지막 통합 호출로 전체 합계 도출 |
| chaining 대체안 ✗ | 1회 자기 비평 · 동일 prompt 반복 · 더 큰 prompt<br>→ 거대 context 의존 그대로 |
| chaining 적합 조건 | 앞 단계 출력 = 다음 단계 입력 (진짜 순서 의존)<br>독립 조각의 chain = 지연만 가산 |
| chaining 누적 결함 | 단계마다 초안 재작성 → 오류 누적<br>총 지연 = 전 호출 합산 |
| chaining 개선 | 독립 조각 병렬 fan-out · 재작성 제거<br>확실한 하위 작업 = deterministic code<br>병합에 validation gate 추가 |
| 개선의 한계 | 조각별 독립성 검증 필요<br>독립성 오판 → 병합 충돌 · 병합 계약 사전 작성 |
| routing 시점 | 유형별 처리가 다름 → route 단계가 먼저 분류<br>→ 유형별 경로로 분기 |
| routing 경로 | 경로마다 맞는 도구 · 방식 부착<br>(고정 조회 선행 경로 · tool 판단 경로 등) |
| chain ≠ routing | 모든 입력을 모든 단계에 통과 ✗<br>chain 길이를 늘려도 분기가 아님 |
| routing 전제 | 분류 체계(taxonomy) 필요<br>오분류 = 엉뚱한 경로 → fallback · 라우터 자체 평가 |
| 질의 형태 혼재 | 형태별로 분해<br>현재값 = 도구 호출 · 독립 문서 다수 = fan-out |
| multi-agent 호출 범위 | 요청마다 전 전문 agent 호출 ✗<br>→ 결과가 정확해도 무관 정보 혼입 · context 낭비 |
| triage | 복잡도 판정 → 투입 agent 수 · 호출 수 조정<br>단순 사실 확인 = agent 1개 · tool 3~10회 수준 |
| 호출 원칙 | 필요할 때만 위임<br>단순 확인 = 직접 답변 · 전문 케이스만 위임<br>coordinator가 케이스 검사 → 필요한 subagent만 호출 |

**Parallelization · critique 보강**

| 구분 | 내용 |
|---|---|
| sectioning | 독립 서브태스크로 분할 → 동시 실행<br>→ 프로그램으로 결과 집계<br>속도 · 정확도 동시 향상 |
| voting 오용 | 순차 대화에 voting → 비용 증가 · 컨텍스트 분절 |
| sectioning 이점 | 항목마다 별도 호출 → 집중 확보<br>긴 섹션이 다른 항목을 밀어내는 누락 방지<br>호출마다 관련 섹션만 전달 |
| 병렬 근거 | "서로 의존 없음" 명시 = 병렬화 근거<br>(예: 최종 schema 검증 전까지 독립) |
| fan-out / fan-in | 독립 조각 병렬 → 병합 → validation gate |
| 병합 계약 | 공통 스키마 · 인용 형식 사전 작성<br>병합이 출처 · 인용 누락 → 검사 통과해도 내용 빈약 |
| fan-in 충돌 | 결과가 어긋날 때 처리할 disagree rule 필요 |
| 병합 검증 | 합계 · 수치 = 결정론적 코드 검사<br>(인용된 표와 대조)<br>서로 다른 시스템 수치 = 병합 전 대조(validation) |
| 인용 시점 | 숫자 생성 시점에 출처 부착<br>초안 후 인용 추가 · 기억 기반 인용 ✗ → 신뢰 불가 |
| 대규모 병렬 번역 | 병렬 fan-out → 기한 충족<br>공통 용어집을 모든 호출에 주입 → 용어 일관<br>계층적 병합 → 섹션 간 drift 포착 |
| critique | 점검자 · 기준 문서 · 수정 loop 명시<br>품질 편차 대응 · 배포 전 모든 초안 대조 |
| critique 결합 | fan-out 분기마다 critique → fan-in 병합<br>독립 규모 + 품질 편차 = 서로 다른 두 문제<br>→ 패턴 두 개 결합 |
| critique 비용 | 점검 호출 추가 → 산출물당 비용 약 2배<br>체크리스트 필요 · 병합에 엄격한 스키마 필요 |

| 상황 | 정답 |
|---|---|
| 단계 · 순서 고정<br>(파일 읽기 → 테스트 실행 → 보고) | 앱 코드가 순서 유지<br>모델 = 보고서 텍스트 작성에만 사용 |
| 다음 단계 시작 전 결과 확인 필요 | 앱 코드가 각 결과 검증<br>실패 시 체인 조기 중단 |
| 단계 B가 단계 A 출력에 의존<br>(이름 추출 → 수수료 계산) | A 직후 · B 직전에 코드 검사<br>실패 시 체인 중단 → 잘못된 값 B 유입 차단 |

| 오답 | 이유 |
|---|---|
| 결과마다 모델이 tool 목록에서 다음 단계 선택 | 유연해 보여도 순서가 코드 아닌 모델에 의존 |
| 의존 단계를 병렬 실행 | 속도 이득 있어도 선행 값 검증 불가 |
| B 이후에 코드로 확인 · 검토자 전달 | B 실행 전 차단 요구 → 이미 유입 |
| compaction으로 잘못된 값 제거 | 이전 턴 요약 작성일 뿐 · 값 검증 ✗ |

![5가지 workflow 패턴의 흐름 비교](svg/1-workflow-patterns.svg)
*그림: 패턴은 분해를 코드가 미리 정하는지(chaining, routing, voting), 실행 중에 LLM이 정하는지(orchestrator-workers), 기준 통과까지 반복하는지(evaluator-optimizer)로 갈린다*

<sub>근거: Amey-0023, CCAR-F-Udemy01-0055, CCAR-F-Udemy02-0007, CCAR-F-Udemy02-0024, CCAR-F-Udemy03-0003, CCAR-F-Udemy03-0016, CCAR-P-jrajath94-0021, CCAR-P-jrajath94-0066, CCAR-P-jrajath94-0116, CCAR-P-jrajath94-0123, CCAR-P-jrajath94-0124, CCAR-P-jrajath94-0125, CCAR-P-jrajath94-0289, CCAR-P-jrajath94-0340, CCAR-P-jrajath94-0402, CCAR-P-jrajath94-0403, CCAR-P-jrajath94-0529, CCAR-P-jrajath94-0604, CCAR-P-jrajath94-0609, Patrick-0012, Patrick-0022, Udemy-0006, Udemy-0053</sub>

### 1.3 Coordinator(orchestrator) 1개 + Subagent n개 구조
**위임 prompt + subagent 정의에 적은 것만 전달 · 요약만 반환**

**Coordinator 역할**

| 역할 | 내용 |
|---|---|
| 작업 분해 | 입력에 맞춰 subtask 결정 |
| 위임 | 독립 · 자기완결 subtask를 subagent에 전달<br>독립이면 병렬 실행 |
| 결과 통합 | subagent의 compact 요약 수집<br>→ 최종 결과 (비교 · 계획 등)<br>실패 격리 |

**Subagent 역할**

| 역할 | 내용 |
|---|---|
| 격리된 컨텍스트 | 부모와 별도 대화 컨텍스트에서 실행<br>자료 읽기 · 중간 tool 호출 · 결과는 subagent 안에만 |
| 좁은 범위 | 자기완결 subtask 하나만<br>(PDF 한 개 요약, 검사 항목 하나 등) |
| 요약 반환 | 최종 메시지만 Agent tool 결과로 부모에 반환<br>→ 부모 context window가 장황한 중간 결과로 안 참<br>= subagent의 주된 구조적 가치 |

**Coordinator → Subagent 전달 범위**

| 구분 | 내용 |
|---|---|
| 넘길 것 | 위임 prompt에 subtask용 컨텍스트 명시<br>(file path, 판단 근거, 이전 결정 등) |
| 전달 경로 | Agent tool의 prompt 문자열<br>+ subagent 자신의 정의<br>(`AgentDefinition`의 `prompt`)뿐 |
| 안 넘어감 | 부모 대화 이력 · tool 결과 · 부모 system prompt<br>일반 subagent = 빈 컨텍스트에서 시작 |
| 예외 | fork형 subagent(현재 대화 분기)만 부모 이력 상속 |
| 공통 방침 | 각 subagent 정의<br>또는 설정에 따라 로드되는 프로젝트 `CLAUDE.md`에 기재 |
| 품질 저하 원인 | 최유력 = handoff 컨텍스트 누락 |
| 위임의 성격 | 컨텍스트를 내주고 격리를 얻는 거래 |
| 품질 저하 대책 | 큰 모델 · subagent 추가로 해결 ✗ |

**Subagent → Coordinator 반환 범위**

| 구분 | 내용 |
|---|---|
| 돌려줄 것 | compact 요약 · 결론 |
| 돌려주지 말 것 | 원문 자료 · 중간 tool 출력<br>→ 그대로 반환 시 격리 의미 소실 |

**구조상 주의점**

| 상황 | 판단 |
|---|---|
| 컨텍스트 격리 | 총 토큰 감소 ✗<br>subagent마다 자료 별도 읽기 · API 별도 호출<br>→ 증가 가능 |
| 비용 절감 | 별도 수단 필요<br>예: subagent별 `model`에 가벼운 모델 지정 |
| subagent 수 증가 | handoff 결함도 비례 증가 |

| 오답 | 이유 |
|---|---|
| subagent끼리 직접 결과 교환 | 결과 통합 · 실패 격리하는 coordinator 소실 |
| 합의용 같은 prompt 2회 실행 · rate limit 우회<br>메인 모델 장애 대비 fallback | subagent의 올바른 용도 아님 |

**단일 agent · workflow가 나은 경우**

| 상황 | 판단 |
|---|---|
| 단계 고정 | subagent · orchestrator 모두 ✗<br>→ 동적 분해 대상 없음 |
| supervision hierarchy | 위임이 필요한 문제 전용 · 고정된 몇 단계엔 ✗ |

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
| 속도 vs 통제 | 동기 실행 = 대기 시간 단점<br>비동기 = 조정 · 상태 일관성 · error 전파 곤란 |

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
| agent team | 여러 session<br>공유 task list · peer 직접 메시지 | 판단 분산형<br>공식: 실험적 · 기본 비활성 |

**탐색 · 조사 위임**

| 구분 | 내용 |
|---|---|
| 대상 | 파일 목록 · 검색 결과 · test log로<br>메인이 반복해서 차는 긴 조사 |
| 방법 | `Explore`(읽기 전용) 또는 범용 subagent에 위임<br>→ 경로 · 줄번호 요약만 반환 |
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

**Multi-agent 적합 · 부적합 판단**

| 상황 | 판단 |
|---|---|
| 하위 작업 독립 · 상태 비공유<br>· 도구 상이 · 결과 병합 필요 | multi-agent 유리<br>fan-in에 병합 · disagree rule |
| 조각이 상태 공유 | 단일 agent · 순차 chain |
| 순차 대화<br>(각 응답이 이전 내용에 의존) | fan-out ✗ → 단일 agent<br>병렬 agent = 작업 분할 아닌 작업 중복 |
| 병렬성이 실제로 있는 부분 | 그 부분만 병렬 유지 |
| 라운드마다 이전 결과 · 전체 이력 필요<br>(다회 협상) | 단일 agent loop 유지<br>이력 · 라운드 로그를 한 컨텍스트에 보유 |
| supervisor + worker로 분할 | handoff마다 전체 이력 운반<br>→ 병렬 이득 없이 조율 비용만 |
| 라운드마다 handoff 내용 변동 | handoff 계약이 낡음 |
| 단일 agent 컨텍스트 증가 | 집중 희석 점검 · 라운드 사이 compact |
| 단계별 공유 문서 편집<br>(각 단계가 직전 결과 필요) | 하나의 thread + 고정 순서<br>단계마다 확인 → 일관된 문서 유지 |
| 공유 sandbox | 공유 컨텍스트 ✗<br>subagent는 각자 대화 기록 별도 유지 |

**과분해(over-decomposition)**

| 상황 | 판단 |
|---|---|
| 작은 작업 · 한 영역 · context 하나에 수용 | subagent 분해 ✗<br>격리 이득 없이 orchestration 비용만 증가 |
| 개선 방향 | 단일 모델 호출<br>+ 필요 시 가벼운 검증 단계 |
| 각 단계가 앞 단계 출력을 필요로 하는 chain | 병렬 실행 부적합 |
| 지연 · 비용의 원인 | 설계 자체<br>→ 큰 모델 교체 · 출력 cache로 해소 ✗ |

**Super-agent 분해 · 소유권**

| 구분 | 내용 |
|---|---|
| 문제 | 단일 loop + 공유 memory<br>→ 실패 원인 귀속 · 독립 평가 · 독립 배포 불가 |
| 분해 | 경계 있는 agent(RAG · search · analytics)<br>+ 명시적 입력/출력 계약 |
| orchestrator | 얇게 유지<br>(또 하나의 super-agent ✗) |
| 소유권 | 팀별로 agent + eval 세트 소유<br>실패 = 계약을 위반한 agent에 귀속 |
| 독립 배포 | 계약을 별도 버전 관리<br>+ agent별 eval 스위트로 릴리스 gate<br>→ 한 팀 변경이 다른 팀 부분을 조용히 파손 ✗ |

![Coordinator 1개와 subagent 3개의 위임과 반환 흐름](svg/1-coordinator-subagents.svg)
*그림: coordinator는 위임 prompt를 내려보내고, 자료와 중간 tool 결과는 각 subagent 안에 남으며 요약만 올라온다*

![Agent tool 경계를 넘는 것과 넘지 않는 것](svg/1-handoff-boundary.svg)
*그림: 부모 이력·tool 결과·system prompt는 넘어가지 않고 위임 prompt에 명시한 것만 넘어가며, 돌아오는 것은 요약뿐이다*

<sub>근거: Amey-0004, Amey-0023, Amey-0025, Amey-0041, CCAR-F-Amey-Thakur-0012, CCAR-F-Amey-Thakur-0052, CCAR-F-Amey-Thakur-0067, CCAR-F-MyPractice-0002, CCAR-F-MyPractice-0008, CCAR-F-Udemy01-0011, CCAR-F-Udemy01-0014, CCAR-F-Udemy01-0018, CCAR-F-Udemy01-0036, CCAR-F-Udemy01-0048, CCAR-F-Udemy02-0060, CCAR-F-Udemy03-0024, CCAR-F-Udemy03-0037, CCAR-F-Udemy04-0043, CCAR-F-Udemy04-0048, CCAR-F-Udemy05-0024, CCAR-F-Udemy05-0036, CCAR-F-Udemy05-0054, CCAR-F-Udemy06-0011, CCAR-F-paullarionov-0002, CCAR-F-paullarionov-0008, CCAR-F-preporato-0001, CCAR-F-preporato-0011, CCAR-P-jrajath94-0016, CCAR-P-jrajath94-0066, CCAR-P-jrajath94-0070, CCAR-P-jrajath94-0119, CCAR-P-jrajath94-0120, CCAR-P-jrajath94-0402, CCAR-P-jrajath94-0605, CCAR-P-jrajath94-0607, CCAR-P-preporato-0004, Patrick-0012, Preporato-0019, Udemy-0004, Udemy-0006</sub>

### 1.5 Loop 종료, 안전장치, 상태
**종료 = success condition + ceiling · 결정은 명시적 state**

| 구분 | 내용 |
|---|---|
| 정상 종료 | 명시적 success condition |
| 안전망 | step ceiling (hard 상한) |
| step ceiling 주된 목적 | agent 비수렴 시 피해 · 비용 제한 |
| 목적 아님 | 성공한 실행의 비용 절감 · 속도 · prompt 단순화 |
| 오답 종료 조건 | 고정 반복 횟수 · wall-clock timeout만 사용<br>컨텍스트 소진 (= 실패) |
| ⚠️ `end_turn` 종료 | 공식 문서: tool call 없으면 `end_turn` 종료<br>해설(Amey 0060번) = 모델 판단만으론 보장 ✗<br>→ 앱 수준 success condition 강조 |
| 시험 대응 | "success condition + ceiling" 선택<br>`end_turn` 처리도 숙지 |

**장기 실행 결정 유지**

| 구분 | 내용 |
|---|---|
| 기록 위치 | compaction과 무관하게 전달되는 명시적 state |
| 이유 | context window 유한 · compaction = 정보 손실 |

**종료 장치 설계**

| 상황 | 정답 |
|---|---|
| 같은 tool 반복 호출 · 두 tool 왕복<br>· 결론 불가 | 명시적 종료 장치 설계<br>= 반복 횟수 예산 · 반복 호출 감지 · escalation 경로 |
| 종료 + 유용한 산출물 보장 | hard 반복 예산 + 명시적 stop condition<br>+ 산출물 체크리스트(= 완료 정의)<br>+ 예산 소진 시 부분 결과와 함께 사람 escalation |
| 소프트 통제 | "효율적으로 · 신속히" prompt = 요청일 뿐<br>비슷한 지시가 있어도 loop 발생 |

| 오답 | 이유 |
|---|---|
| `max_tokens` · context window · 모델 크기 상향 | 수렴 보장 ✗ · 증상만 지연 |
| 필요한 tool 제거 (검색 tool 등) | 작업 자체 불가 · agent 존재 이유 상실 |
| `temperature` 하향 · 0 | 반복 횟수 제한 ✗<br>결정적 agent는 같은 호출을 결정적으로 반복 |
| 상한 숫자만 증가 (3 → 10 · 8 → 30) | 구조 동일 · 상한 도달 응답을 최종 답으로 취급 ✗ |

**반복 상한의 위치**

| 구분 | 내용 |
|---|---|
| 정상 종료 판정 | `stop_reason` (`end_turn`) |
| tool 호출 횟수 | 모델이 context 기반으로 판단 |
| 상한 설정 | 충분히 크게 · 안전장치로만 유지 |
| 상한이 주된 중단일 때 | 4회 이상 필요한 건만 중간 절단<br>단순 건은 1회 완료 → 복잡도와 무관하게 작동 |
| 상한 도달 시 | 로그 기록 · 이상으로 취급<br>미완료로 기록 (완료 처리 ✗) · 사람 escalation |
| 모니터링 지표 | 상한 도달 횟수 · 예기치 않은 `stop_reason` 값 |

**token · 비용 예산**

| 구분 | 내용 |
|---|---|
| 원칙 | token 예산 = 모델 밖에서 강제 |
| 측정 | loop 안에서 각 응답의 `usage` 필드로<br>입력 · 출력 token 누적 추적 |
| 대응 | 예산 도달 → 코드가 loop 중단<br>예산 약 80% → 마무리 지시 주입 (약한 경고) |
| 오답 1 | Claude에게 사용량 질문 = 추정 · 측정 ✗ |
| 오답 2 | system prompt "50,000 token 이하" = 확률적 |
| 오답 3 | `max_tokens` 50 = 모든 응답 잘림 |

**Agent SDK 상한 · 재개**

| 구분 | 내용 |
|---|---|
| 기본값 | agent loop = turn · 비용 한도 없음<br>범위 넓은 prompt → 실행 장기화 |
| 한도 설정 | `max_turns` · `max_budget_usd`<br>production agent의 기본 선택 |
| 한도 도달 구분 | `ResultMessage`의 `subtype`으로 성공과 구별<br>(`error_max_turns` 등) |
| 이어하기 | `session_id` 저장 → `resume` |
| 단발 `query()` | error result 반환 후 예외 발생<br>→ try로 감싸 다음 요청 진행 |
| 평가 포인트 | "어디서 멈추나" + "멈춘 뒤 어떻게 다루나" 둘 다 필요 |
| 오답 1 | `effort` `"low"` = turn당 소비만 변경 · 상한 ✗ |
| 오답 2 | Stop hook = loop 끝날 때까지 발화 ✗ → 중도 차단 불가 |

**`session budget` (Managed Agents)**

| 구분 | 내용 |
|---|---|
| 동작 | list cost가 상한 도달 → 새 모델 요청 중단<br>세션 일시 중지 |
| 적합 상황 | 단계 미정 agent loop + 세션별 고정 지출 상한 |
| 기능 상태 | 공식 문서상 Managed Agents beta 기능 |
| workflow run 여러 개 | 모두 하나의 `session budget`에 포함<br>→ 전체 세션에 budget 1개 |
| 병렬 읽기 + 진행 표시<br>(lead 후속 메시지 금지) | workflow run 1개 + `session budget` 1개 |

| 오답 | 이유 |
|---|---|
| `effort` low | 지출 통제처럼 보여도 상한에서 요청 중단 ✗ |
| session budget 없이 subagent 6개 + 병합 | 폭주 지출 상한 부재 |
| 검색 단계를 코드에 하드코딩 | 단계 미정 작업에 부적합 |
| run마다 별도 budget | run은 하나의 budget에 포함 → 이중 설정 |
| subagent별 후속 메시지 · lead → worker 후속 메시지 | 제약 위반 (후속 메시지 금지) |

**상태 설계 진단 · 복구**

| 상황 | 판단 |
|---|---|
| 같은 인자로 비싼 tool 반복 호출 | 결과 보관 · 재사용 실패 = 상태 설계 문제<br>정상 재시도 ✗ |
| crash 후 worker가 확인된 사실 · 판단 소실<br>(filesystem 비공유 · 로컬 JSONL 보존 불확실) | 사실 · 판단을 JSON state manifest로 영속화<br>→ 재시작 시 prompt에 주입 |
| host를 넘어 session 재개 | 공유 스토리지로 mirror 필요<br>(`SessionStore` adapter) |
| 복구 수단의 기준 | 실행 환경에 의존하지 않는 앱 정의 state |

**Loop 제어 책임**

| 구분 | 내용 |
|---|---|
| loop 담당 | Agent SDK = SDK<br>Messages API 직접 구현 = 개발자 |
| 반복 상한 | 폭주 방지 안전장치 · 충분히 큰 값<br>주된 중지 조건으로 사용 = 안티패턴 |

![success condition과 hard step ceiling으로 이루어진 loop 종료 흐름](svg/1-loop-termination.svg)
*그림: loop는 success condition으로 정상 종료하고, 수렴하지 못하면 hard ceiling이 안전망으로 끊는다*

![context window와 명시적 state의 결정 유지 비교](svg/1-explicit-state.svg)
*그림: context window에만 둔 결정은 compaction과 재시작으로 사라지고, 명시적 state에 둔 결정은 유지된다*

<sub>근거: Amey-0026, Amey-0036, Amey-0060, Amey-0073, CCAR-F-Amey-Thakur-0001, CCAR-F-Amey-Thakur-0013, CCAR-F-Amey-Thakur-0066, CCAR-F-Udemy01-0045, CCAR-F-Udemy02-0036, CCAR-F-Udemy04-0014, CCAR-F-Udemy04-0028, CCAR-F-Udemy05-0045, CCAR-F-Udemy06-0023, CCAR-F-preporato-0013, CCAR-P-jrajath94-0023, CCAR-P-jrajath94-0603, CCAR-P-jrajath94-0606, Patrick-0038</sub>

### 1.6 Tool 설계
**목적 겹치는 tool → 잘못된 tool 선택 증가**

| 구분 | 내용 |
|---|---|
| 겹치는 tool | 선택 모호 → 잘못된 tool 선택 빈발 |
| 속도 · 비용 · 오류 처리 | 이득 ✗ |

<sub>근거: Amey-0059</sub>

### 1.8 Deployment 선택 — 3축 확인
**loop · tool · state 위치 3축 확인**

| 축 | 확인 항목 |
|---|---|
| loop | loop 실행 주체 |
| tool | tool 실행 위치 |
| state | 대화 로그 저장 위치 |

| 상황 | 정답 |
|---|---|
| data residency<br>(실행 · 데이터 · 세션 로그까지 자사 네트워크) | self-hosted (Agent SDK) |
| production 출시 속도 우선 | Managed Agents |

![loop, tool 실행, state 위치로 본 deployment 비교](svg/1-deployment-axes.svg)
*그림: Managed Agents는 sandbox를 자사에 두어도 session과 event log가 Anthropic에 남으므로 residency 요구에는 self-hosted Agent SDK다*

<sub>근거: Preporato-0018, Udemy-0051</sub>

### 1.11 Handoff contract와 불일치(disagree) 규칙
**contract = 입력 · 출력 · 병합 · 불일치 규칙**

| 요소 | 내용 |
|---|---|
| 입력 | worker별 입력 문서 (작업 한정) |
| 출력 | worker별 출력 형식 |
| 병합 규칙 | coordinator가 조각을 하나로 결합하는 방식<br>병합 규칙 없음 → 좋은 검토 3개가 한 보고서 ✗ |
| 불일치 규칙 | 충돌 시 우선 근거 또는 arbiter<br>coordinator가 적용 · 결정 기록 |
| checkpoint | 각 handoff 저장 → worker 실패 시 재개 |
| 비요소 | 문체 · 모델 등급 · 근무 시간<br>→ 비일관성 방지 못함 |
| ⚠️ 용어 | 해설 자체 용어 · 공식 문서에 동일 정의 없음<br>→ 구성 항목은 해설 기준 (공식 문서 미확인) |

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

### 1.14 동적 분해 절차 — 탐색 · 우선순위 · 계획 갱신
**먼저 훑고 · 우선순위 정하고 · 발견으로 갱신**

1. 짧고 넓은 탐색으로 구조 · 중요 영역 파악
2. 영향 큰 영역 식별
3. 우선순위 서브태스크 계획 작성 · 산출물로 기록
4. 의존 관계 발견 시 계획 갱신 · 변경 이유 기록
5. 결과 통합 후 공백 확인 → 공백에만 2차 할당

| 증상 | 원인 | 조치 |
|---|---|---|
| 중요 모듈 테스트 0건<br>단순 함수에 예산 소진<br>(알파벳 순 처리) | 순서에 중요도 미반영<br>(처리량 부족 ✗) | 구조 파악 → 영향 큰 영역 우선 계획 |
| 대규모 수정을 디렉터리 순 진행<br>→ 대부분 재작업 | 모듈 의존 관계 미파악 | 의존 파악 · 우선순위 계획 · 갱신 |
| 시작 시점 문구로 서브태스크 고정<br>→ 중간 단서 누락 | 계획 고정 | 발견 따라 서브태스크 추가 · 우선순위 재검토 |
| subagent는 할당 완수<br>낯선 주제 포괄성 낮음 | 할당 생성 방식 | 사전 탐색으로 할당 생성<br>공백에만 2차 할당 |
| 문장은 좋으나 범위 불균형<br>지엽 조사에 노력 소진 | coordinator가 조사 대상을 파악 못함 | 탐색 조사 → 우선순위 할당<br>목차는 조사 후 확정 |

| 구분 | 내용 |
|---|---|
| 큰 종합 작업<br>(출처 200개 → 장문 보고서) | 구조 계획 → 섹션별 근거 병렬 수집 → 종합<br>단계마다 다룰 수 있는 context |
| 포괄성 진단 | 실행 문제 vs 할당 문제 구분<br>할당 완수인데 누락 = 할당 방식이 원인 |
| 공백 보완 | 추가 조사 후 반영<br>통합 단계 임의 보완 ✗ |
| 할당 수 증가 | 전 주제 일률 증가 ✗ · 공백에만 추가 |
| 기록 | 분해 결과 · 변경 이유 기록<br>→ 결론 도달 경위 설명 · 다음 실행이 이어받음 |

![고정 chain과 동적 분해의 선택 기준과 동적 분해 절차](svg/1-decomposition-choice.svg)
*그림: 절차를 사전에 확정할 수 있으면 고정 chain, 발견에 따라 달라지면 탐색 · 우선순위 · 계획 갱신으로 동적 분해한다*

<sub>근거: CCAR-F-Udemy02-0045, CCAR-F-Udemy03-0050, CCAR-F-Udemy04-0022, CCAR-F-Udemy05-0019, CCAR-F-Udemy06-0038, CCAR-P-jrajath94-0015</sub>

### 1.16 의존성 기반 병렬 · 순차 결정
**독립은 병렬 · 의존은 순차 · 합류점은 fan-in**

| 조건 | 실행 |
|---|---|
| 입력이 다른 작업 출력 불필요 | 병렬 |
| 입력이 다른 작업 출력 필요 | 선행 완료 후 순차 |
| 독립 작업을 순차 실행 | 이득 없이 지연 · 소요 = 합계 |
| 독립 작업을 병렬 실행 | 소요 = 최댓값 (SLA 대응) |
| 모든 선행이 필요한 합류 작업 | fan-in에서 선행 완료 신호 확인 후 실행 |
| 의존 무시 병렬 | 최적화 ✗ · 결함 (안전 위반 가능) |
| 의존 쌍 외 나머지 | 순서 자유 (병렬 · 순차 모두 유효) |
| 의존 조건이 바뀜 | 정답도 바뀜 → 문항의 선행 조건이 결정 |
| 자원 공유 작업 | 독립성 붕괴 (예: 장비 1대 공유) → 병렬 ✗ |

**혼합 구조 패턴**

| 구조 | 실행 |
|---|---|
| 독립 N개 → 합류 1개 | N개 병렬 → fan-in 1개<br>(저장소별 스캔 → 통합 보고서) |
| 선행 1개 + 독립 작업 | 독립 작업은 처음부터 병렬<br>의존 작업만 선행 완료 후 |
| 선행 1개 → 병렬 2개 → 합류 | 빌드 → 테스트 ∥ 스캔 → 배포 |
| 독립 N개 + 비교 1개 | N개 병렬 → 비교는 N개 결과 수신 후 |

**병렬 기동 방법**

| 구분 | 내용 |
|---|---|
| 병렬 기동 | coordinator 한 응답에서<br>Agent tool 호출 여러 개 출력 |
| 순차 기동 | 응답마다 호출 1개 → 결과 대기 → 다음 위임<br>→ 소요 = 작업 수 배 |
| tool 이름 | 문항 표기 = Agent tool(구 Task tool)<br>2.1.63에서 Task → Agent로 변경<br>(구 `Task(...)` 표기는 alias) |
| 의존 작업 | 선행 결과 수신 후 별도 호출<br>전부 동시 위임 ✗ |
| 의존 명시 | coordinator prompt에 작업 간 의존 관계 기재<br>→ 병렬 · 순차 판단 안정 |
| 대기 제거 | 각 subagent에 자기완결 brief 전달<br>앞 subagent 요약 대기 ✗ |

**복합 요청 분해**

| 구분 | 내용 |
|---|---|
| 증상 | 한 요청에 용건 여러 개<br>→ 첫 용건만 해결 후 종료 · 재문의<br>순차 조사 · 같은 고객 데이터 중복 조회 |
| 분해 | 개별 이슈로 분해<br>→ 공유 고객 context로 병렬 조사<br>→ 하나의 해결안으로 종합 |
| 효과 | 중복 조회 제거 · tool 호출 loop 총 횟수 감소<br>한 번의 응대로 전 용건 해결 |
| 마무리 | 용건별 결과 나열 → 누락 확인 |
| 판별 기준 | 노력 · 판단을 고객 · 담당자에 떠넘김 ✗<br>확인 끝난 정보 재사용 여부 |

![의존성에 따른 병렬, 순차, fan-in 실행 구조와 소요 시간 비교](svg/1-dependency-parallel.svg)
*그림: 독립 작업은 병렬로 기동하고 의존 작업은 선행 완료 뒤에 실행하며 합류 작업은 fan-in에서 기다린다*

<sub>근거: CCAR-F-MyPractice-0048, CCAR-F-Udemy02-0024, CCAR-F-Udemy03-0016, CCAR-F-Udemy04-0054, CCAR-F-Udemy05-0035, CCAR-F-paullarionov-0048, CCAR-F-preporato-0005, CCAR-P-jrajath94-0286, CCAR-P-jrajath94-0339, CCAR-P-jrajath94-0465, CCAR-P-jrajath94-0466, CCAR-P-jrajath94-0528</sub>

### 1.18 전제 조건 gate 설계
**gate 조건 = "호출됨"이 아니라 "검증됨"**

| 구분 | 내용 |
|---|---|
| 전제 조건 | 선행 단계 완료 전까지 후속 tool 호출 차단<br>(programmatic) |
| 예 | `get_customer`가 검증된 ID 반환 전<br>`lookup_order` · `process_refund` 차단 |
| '완료' 정의 | 호출 사실 ✗ · 검증된 결과(ID) 획득 ✓ |
| 오류 사례 | 호출 여부만 보는 gate<br>→ 후보 여러 명 일치에도 통과 → 타인 계정 환불 |
| 보강 1 | 검증된 ID를 session 상태에 유지<br>`process_refund` 인수의 ID와 일치 확인 |
| 보강 2 | 후보 다수 → 추측 선택 ✗<br>추가 식별 정보를 고객에게 질문 |
| 사고 후 진단 | gate가 있는데 사고 → gate 조건 자체를 의심 |

| 상황 | 정답 |
|---|---|
| tool 호출 순서 위반<br>(`get_customer` 건너뛰고 `lookup_order` 직행) | 코드 수준 precondition |
| subagent 순서 위반<br>(분석 결과 · 출처 반환 전 보고서 위임) | orchestration 계층 precondition<br>필요한 결과 · 출처 대응 갖출 때까지 위임 거부 |
| 본인 확인 전 배송지 변경 | 코드로 확인 → 미확인 시 tool 거부 |
| gate 거부 시 | 이유를 tool 결과로 agent에 반환<br>→ 올바른 절차로 복귀 |
| 위반 조작 차단 후 | 대체 workflow로 유도<br>(plan 결과 담당자 확인 등) |
| 운영 | 거부 건수 기록 → 절차 생략 지점 · prompt 개선 진척 추적 |

| 오답 | 이유 |
|---|---|
| 순서를 보여 주는 few-shot | 확률적 · 건너뜀 가능성 잔존 |
| system prompt 더 강하게 명시 | 확률적 · 실패율 0 ✗ |
| routing classifier로 tool 일부만 활성화 | 건너뜀 가능성 자체를 제거 못함 |
| 반복 횟수 증가 · `tool_choice` 강제 | 순서를 제어하는 메커니즘 ✗ |
| 지시 강화 (coordinator) | 요청에 그침 |

**gate 판정을 실행에 연결**

| 구분 | 내용 |
|---|---|
| 핵심 | gate 판정이 코드에서 출시 결정으로 연결 · fail closed |
| 차단 없는 verification | 장식 (guardrail ✗ · 대시보드) |
| gate 역할 | gate마다 하나 · 다른 gate 역할 대신 ✗ |
| 조치 | 코드로 차단 + 실패 원인 계층(retrieval · prompt) 수정 |
| 전제 | 원인 수정에 실패 trace 필요 |
| 부작용 | 차단 → false-positive 차단 증가 가능<br>→ 원인 수정 신속 필요 |

| 오답 (gate 있는데 실패 초안 출시) | 이유 |
|---|---|
| 모든 답변 사람 검토 | 하루 50,000건 × 30초 = 417 검토자-시간<br>원인 미수정 |
| 10% 표본 검토 | 실패의 90% 통과 |
| gate 제거 | 작동하는 탐지기 파괴 → 눈 가리고 출시 |

| 조건 변화 | 정답 변화 |
|---|---|
| 하루 100건 + 답변마다 법적 노출 | 전면 사람 검토 |
| 실패 드묾 + 표본을 eval 라벨 세트로 활용 | 표본 검토 |
| gate false-positive가 탐지율 초과 + 더 나은 검사 존재 | gate 교체 · 제거 |

<sub>근거: CCAR-F-MyPractice-0051, CCAR-F-Udemy01-0019, CCAR-F-Udemy01-0020, CCAR-F-Udemy04-0005, CCAR-F-Udemy04-0016, CCAR-F-Udemy04-0053, CCAR-F-Udemy06-0051, CCAR-F-paullarionov-0051, CCAR-P-jrajath94-0114</sub>

### 1.19 비가역 작업 통제와 사람 승인
**위험 = 피해 크기 · 모델 밖에서 통제**

| 구분 | 내용 |
|---|---|
| 운영 위험을 가장 키우는 특성 | checkpoint 없이 되돌릴 수 없는 작업 수행 |
| 이유 | 되돌릴 수 있는지 = 틀렸을 때 비용 · 피해 범위 결정 |
| 영향 작은 것 | 모델 수 · 구조 · 실행 시간<br>→ 비용 · 복잡도에만 영향 |
| 오류 확률 vs 피해 | 모델 성능 · prompt 길이 · tool 수 = 오류 확률에 영향<br>피해 크기 · 비용에는 영향 ✗ |

| 상황 | 정답 |
|---|---|
| 자율 단계가 production 데이터 수정 | 사람 승인 checkpoint 또는 되돌림 장치<br>모델 밖에서 강제 |
| 틀린 결정의 비용 최소화 | 동작을 되돌릴 수 있게 구성<br>또는 확인을 거쳐야 실행되게 구성 |
| 금전 이동 · 고객 대상 메시지<br>(모델 단독 실행 금지) | 모델은 제안 · gate가 처분<br>작성 = 자동 · 발송 · 환불 = gate 뒤 |
| gate 구성 예 | 규칙 엔진이 정책 · 금액 · 사기 flag 확인<br>발송 = 사람 승인 |
| `dry_run` 우회 방지<br>(미리보기 후 실행 강제) | preview · execute 두 tool 분리<br>preview = 영향 세부 + 1회용 confirmation token<br>execute = token 필수 → 실행을 preview에 바인딩 |

| 오답 | 이유 |
|---|---|
| 더 큰 모델 · 더 긴 system prompt · 재시도 | 피해 범위 제한 ✗ |
| "double-check the policy" 지시 | 여전히 모델 판단 → prompt-plea 함정 |
| 행동 전 추론 상세 설명 요구 | 결정 주체 불변 · 모델 단독 실행 |
| 두 agent 투표 · 둘 다 동의 시 실행 | 모델 판단 2개 · 결정론적 점검 ✗ · 사람 점검 ✗ |
| 직전 60초 내 `dry_run=true` 이력 validation | 시간 간격 heuristic 의존 |
| tool에 confirmation 표시 + orchestration 계층이 승인 요청 | orchestration 계층의 정상 동작에 의존 |
| tool 설명 · few-shot으로 preview 먼저 호출 지시 | LLM 지시 준수에 의존 |

![모델 제안, 규칙 엔진, 사람 승인, 실행으로 이어지는 비가역 작업 통제와 preview · execute 분리](svg/1-irreversible-approval.svg)
*그림: 비가역 작업은 모델이 제안만 하고, 실행은 모델 밖 gate와 사람 승인 또는 preview에 묶인 token 뒤에서만 일어난다*

<sub>근거: CCAR-F-Amey-Thakur-0014, CCAR-F-Amey-Thakur-0053, CCAR-F-Amey-Thakur-0068, CCAR-F-MyPractice-0061, CCAR-P-jrajath94-0067</sub>

### 1.21 기타 — trace · 경계 계약 · retrieval 분할
**진단 = trace · 경계 = 계약 · 혼입 = 분할**

| 상황 | 정답 |
|---|---|
| production agent 디버깅 · 실패 원인 진단 | 단계별 trace 기록<br>(각 단계 입력 · tool 호출 · 출력) |
| trace가 필요한 이유 | 비결정적 실행을 사후 재구성 가능 |
| 각 구성요소는 정상인데 경계에서 간헐 실패 | 둘 사이 계약(interface) 불충분<br>특히 edge case · 오류 case |
| 여러 지역 · 팀 정책이 답변에 혼입 | 데이터 도메인별 분할<br>문서에 지역 tag<br>→ semantic search 전 사용자 지역으로 retrieval 필터 |

| 오답 | 이유 |
|---|---|
| tool 수 축소 · 단일 모델 통일 | 단순화일 뿐 원인 설명 ✗ |
| step 한도 상향 | 실패만 길어짐 · 더 분명해지지 않음 |
| 최종 출력 · token 총량 · 모델 버전만 기록 | 어느 지점에서 어긋났는지 알 수 없음 |
| 더 큰 모델 · 구성요소 추가 (경계 실패) | 인터페이스 정의 ✗ |
| 재시도 (경계 실패) | 문제 은폐 |
| 전 지역 정책 전부 투입 | context stuffing |
| 지역별 agent 14개가 협상 | retrieval 문제에 조율 장치만 추가 |
| 사용자에게 지역 언급 요청만 | 혼합 retrieval 유지 |

<sub>근거: CCAR-F-Amey-Thakur-0017, CCAR-F-Amey-Thakur-0054, CCAR-P-Amey-Thakur-0070, CCAR-P-preporato-0005</sub>

### 1.22 Hybrid 설계 — 고정 뼈대 + 열린 판단
**고정 단계는 코드 · 열린 판단만 모델 · 사이에 gate**

| 구분 | 내용 |
|---|---|
| 분기 규칙 | 입력 형태별 lane 배정<br>고정 매핑 → 결정론적 코드<br>열린 입력 → Claude + gate |
| 구조 | 고정 단계 = deterministic workflow<br>모호한 소수 사례(3~10%) → agent 호출<br>→ 이후 workflow 복귀(지급 · 경고 · 게시) |
| handoff 지점 | workflow ↔ agent 전환 지점 |
| 두 형태 작업<br>(열린 평가 + 고정 발행) | agentic loop로 평가 → 고정 schema<br>→ deterministic workflow로 발행 |
| 연결 조건 | loop 출력 = workflow schema 계약<br>loop = step 상한으로 평가 비용 제한 |
| 정답 형태 | 두 형태 작업의 표준 정답 = hybrid<br>패턴 하나만 고르기 ✗ |

**패턴 스펙트럼 판단 축**

| 축 | 판단 |
|---|---|
| 점수 기준 | 예측 가능성 · 되돌림 가능성<br>오류 비용 · 지연 · 비용 |
| 오류 비용 높음 + 되돌리기 어려움 | 결정론 쪽(스펙트럼 왼쪽)으로 이동 |
| 계획 필요성 높은 단계 (평가 · 조사) | agent |
| 예측 가능성 필요한 단계 (발행 · 지급) | workflow |
| 결정 요인 | 작업의 형태 (구호 ✗) |

**Gate · 사람 검토의 확장성**

| 상황 | 판단 |
|---|---|
| 고정 사례 규칙 처리<br>+ 열린 사례 Claude 처리 | 모든 초안 · 지급에 code gate<br>(원본 대조 · 사진 · 기록 검사 통과 전 차단) |
| gate 입력 | 검사가 원본(메시지 · 사진 · 기록)을 볼 수 있어야 함 |
| 모든 건을 사람이 검토 | 대량엔 불가<br>(12,000건 × 30초 ≈ 하루 100 간호사-시간) |
| 전수 사람 검토가 맞는 경우 | 물량 소량(하루 40~60건)<br>+ 건당 법적 책임 |
| 검사 없는 agent · 최상위 tier | gate 없음 → 오류 비용 한도 위반 |

**비용 절감 = lane 선택**

| 상황 | 정답 |
|---|---|
| 고정 layout 80% + 열린 형식 20%<br>precision 하한 유지 | 고정분 → deterministic parser<br>열린 20% → Claude<br>합계 검사 gate 유지 |
| 절감의 원천 | tier 선택 ✗ · lane 선택 ✓ |
| 새 layout 등장 | parser가 학습할 때까지 Claude로 라우팅 |
| 유지보수 비용 | 양식 변경마다 규칙 세트 · parser 갱신 |
| ⚠️ 수치 | 문항 toy 수치: 월 $540 → $132(약 4배 절감)<br>최상위 tier ≈ Fast tier의 10~14배<br>공식 문서: Fable 5.2 ≈ Haiku 5.5의 80배(MTok) |

**확실한 하위 작업의 결정론적 분리**

| 구분 | 내용 |
|---|---|
| 분리 대상 | 합산 · 평일 검사 등 정답이 확정된 하위 작업 |
| 역할 | 코드 = 계산 · 검증<br>Claude = 검증된 값을 둘러싼 글쓰기 |
| 조건 | 표 형식 계약 필요 (형식 변경 시 script 갱신)<br>글이 숫자를 재계산 ✗ |
| 원리 | 능력 ≠ 확실성<br>→ 확실한 하위 작업 = 코드 |

**쓰기 통제권 유지**

| 구분 | 내용 |
|---|---|
| 고정 단계 + 분류 판단 1회 | 앱 코드가 단계 실행<br>모델 호출 = 분류 1회<br>게시(쓰기) = 앱 코드 |
| 통제권 상실 | 모델이 직접 게시<br>(MCP connector · 네트워크<br>· server-executed tool) |
| agent loop의 대가 | 계획 단계 = 고정 코드에 불필요한 비용 · 변동 |

![입력 형태에 따라 고정 단계 코드와 Claude agentic loop로 갈라지고 gate를 거쳐 workflow로 합류하는 hybrid 구조](svg/1-hybrid-lanes.svg)
*그림: 고정 단계는 결정론적 코드가, 열린 판단만 Claude가 맡고, 둘 사이와 쓰기 앞에는 code gate를 둔다*

<sub>근거: CCAR-P-jrajath94-0107, CCAR-P-jrajath94-0110, CCAR-P-jrajath94-0115, CCAR-P-jrajath94-0118, CCAR-P-jrajath94-0126, CCAR-P-jrajath94-0282, CCAR-P-jrajath94-0284, CCAR-P-jrajath94-0336, CCAR-P-jrajath94-0399, CCAR-P-jrajath94-0462, CCAR-P-jrajath94-0521, CCAR-P-jrajath94-0525, CCAR-P-jrajath94-0602</sub>

### 1.23 구조적 통제 · gate 위치 · trust boundary
**보장이 필요하면 prompt가 아닌 구조로 강제**

| 요구 | 구조적 수단 |
|---|---|
| 지어낸 거절 이유 0건<br>(내부 agent → 가입자 대상 확대) | 결정론 단계가 실제 decision record 조회<br>모델 = 기록 바꿔 말하기만<br>자체 이유 제시 ✗ |
| 테넌트 간 데이터 격리<br>(통제 = 강제 가능) | tenant별 session context(아키텍처 계층)<br>tenant 범위 credential · 필터된 tool 접근<br>모델 밖 data partitioning |
| 격리 효과 | 다른 tenant 데이터에 도달 불가<br>→ prompt 실패로도 유출 ✗ |
| 원칙 | prompt 지시 = 권고적 · 우회 가능<br>보안 경계로 검증 불가 |
| 확대 위험 | 내부용 agent는 제약된 적 없음<br>외부 대상 확대 = 위험 상승 → 방어 장치 추가 |

**Gate 위치와 강도**

| 구분 | 내용 |
|---|---|
| 위치 | 모델 출력 뒤 · 부수 효과 앞<br>(발송 · 지급 · 공지 · 수여) |
| 되돌릴 수 없음 + 중대 | 효과 전 사람 검토<br>검토자가 제안 · 증거 · system of record를<br>한 화면에서 확인 |
| 되돌릴 수 있음 | 코드 검사 유지<br>(자격 입력 vs 원본 문서 대조) |
| 대외적 난처함 위험 | 코드 검사 + 사람 표본 검토 |
| 검토 SLA | gate가 실제 긴급 대응을 지연 ✗ 하도록 설정 |
| 원칙 | 검토 강도 = 결과 중대성 · 되돌림 가능성에 비례 |

**Trust boundary**

| 구분 | 내용 |
|---|---|
| 경계 ① | 신뢰할 수 없는 입력이 들어오는 지점<br>(폭언 · 조작 가능 채팅 → 검증 단계) |
| 경계 ② | 모델 출력이 부수 효과로 나가는 지점<br>(티켓 쓰기 = 코드에서 권한 부여) |
| 경계 아님 | 내부 구간<br>(logger → disk · 순수 함수 사이<br>· system of record 읽기 → 모델) |
| system of record | 신뢰 출처 · 점검 기준 |
| 파이프라인 순서 | 입력 → 검증 → context 조립 → 모델<br>→ 검증 → 부수 효과 → 피드백 |

<sub>근거: CCAR-P-jrajath94-0065, CCAR-P-jrajath94-0069, CCAR-P-jrajath94-0283, CCAR-P-jrajath94-0523, CCAR-P-jrajath94-0524</sub>

## 2. 상황별 정답 판단 규칙

**패턴 선택**

| 상황 | 정답 |
|---|---|
| 단계 고정 · 순서 동일 · 모든 입력에서 동일 | 결정론적 workflow (prompt chaining)<br>모델은 필요한 지점에서만 호출 |
| 고정 단계 사이 검증 필요 | 단계 사이 validation gate<br>(programmatic · schema check) |
| 매핑 고정 형식 변환 | deterministic script<br>해석 필요 시 schema 둔 단일 호출<br>agent loop ✗ |
| 중간 결과를 봐야 다음 단계 결정 | agent |
| 입력마다 조사 · subtask가 다름<br>+ 결과 통합 필요 | orchestrator-workers<br>(orchestrator가 동적 분해 · 위임 · 통합) |
| 입력 유형별 다른 처리로 보내기만 | routing |
| 같은 작업을 여러 관점으로 돌려 확신도 향상 | parallelization (voting) |
| 명확한 평가 기준 + 하나의 출력 반복 개선 | evaluator-optimizer |

**Subagent · 컨텍스트**

| 상황 | 정답 |
|---|---|
| 독립 문서 여러 개 → 단일 agent 컨텍스트 초과 | orchestrator가 문서별 subagent 병렬 실행<br>→ 요약만 받아 통합 |

**Loop · state**

| 상황 | 정답 |
|---|---|
| loop 종료 시점 | success condition<br>(또는 `tool_use` 아님)<br>+ step ceiling(최대 반복 cap) |
| step ceiling 이유 | 비수렴 시 피해 · 비용 제한 |

**구현 수단**

| 상황 | 정답 |
|---|---|
| 파일 · shell · context 관리 · permission<br>갖춘 agent (loop 구현 없이) | Claude Agent SDK |
| 인프라 운영 없이 최단 production | Managed Agents |
| 실행 환경 · 세션 로그 모두 자사 인프라 | Agent SDK를 자사 프로세스에서 실행<br>(self-hosted) |
| durable execution · human-in-the-loop<br>· state 영속화 필요한 장시간 agent | LangGraph 등 orchestration 프레임워크 |
| subagent 직접 통신 → 실패 간과 · 중복 · 추적 불가 | 모든 통신 coordinator 경유 |
| 통합 결과가 품질 기준 미달 | coordinator가 평가 → 부족분만 재위임<br>→ 통합 재호출 (반복 상한 + 미해결 주석) |
| 병렬 worker가 덮어쓰기 · 중복 | 겹치지 않는 범위 + 고유 키 저장소<br>+ orchestrator 마지막 병합 |
| worker 의견 충돌 | contract 불일치 규칙 (critic · arbiter)<br>적용 · 기록 |
| 정형 · 반복 점검 (항목 고정) | 고정 순차 chain |
| 범위 미정 조사 · 원인 탐색 · 레거시 전반 작업 | 동적 분해<br>(구조 파악 → 우선순위 → 갱신) |
| 한 도구에 정형 + 조사 의뢰 공존 | 유형 판정 후 분기<br>(정형 = chain · 조사 = 동적) |
| 열린 조사에 동적 분해 적용 | 모델 바깥에서 강제하는 한도 병행 |
| 고정 순서 chain에서 오류 누적 · 지연 합산 | 독립 조각 병렬 · 재작성 제거<br>확실한 작업 = deterministic code<br>병합에 validation gate |
| agent 간 결과 중복 · token 증가 | 위임 전 조사 영역 분할<br>담당 · 비담당 범위 기재 |
| 독립 관점 · 항목 다수 | sectioning 병렬 → 집계 |
| 독립 작업 + 합류 작업 | 독립 병렬 → fan-in → 합류 작업 순차 |
| 의존 관계가 주어진 일정 · 절차 | 의존 쌍은 순차 · 나머지만 병렬 |
| 순차 대화 · 라운드 의존 · 얽힌 작업 | 단일 agent (fan-out ✗) |
| 단계별 공유 문서 편집 | 하나의 thread · 고정 순서 · 단계별 확인 |
| 유형별 처리가 다른 입력 | route 먼저 · 유형별 경로 |
| 질의 형태 혼재 (현재값 + 독립 문서 다수) | 현재값 = 도구 호출 · 문서 = fan-out + 병합 gate |
| 독립 조각 + 품질 편차 | fan-out + critique(점검자 · 기준) → 병합 |
| 병합 숫자 · 인용 정합 필요 | 코드 검사 gate · 인용은 생성 시점에 부착 |
| 대규모 번역 · 용어 일관 | 병렬 fan-out + 공통 용어집 주입 + 계층적 병합 |
| 무한 loop · tool 왕복 · 결론 불가 | 종료 장치 설계: 반복 예산 · 반복 호출 감지 · escalation |
| 반복 횟수 상한 | 안전장치로만 사용 · 도달 시 미완료 기록 + escalation |
| 단계 미정 + 세션별 고정 지출 상한 | agent loop + `session budget` |
| "확실히 막는다" · 예외 불인정 | 모델 밖 강제: `PreToolUse` hook · gate · tool 구현 검증 |
| prompt에 규칙이 있는데 위반 발생 | hook · gate 추가 (prompt 강조 ✗) |
| 비가역 · 금전 · 고객 발송 | 사람 승인 · gate · 되돌림 장치 (모델은 제안) |
| 단계 간 값 의존 | 다음 단계 전 코드 검사 → 실패 시 체인 중단 |
| 지역별 정책 혼입 | tag + retrieval 필터링 |
| 순서 고정 · 입력 일정 · 규칙 알려짐 | deterministic 구현<br>모델은 모호한 부분에만 |
| 고정 경로 + 열린 단계 1개 | augmented LLM (도구 가진 workflow)<br>loop 통제 불필요 |
| 검색 1회 + 판단 1회로 종결 | augmented single call |
| 단계를 실행 전엔 모름<br>각 발견이 다음 단계 결정 | agentic loop + step 상한 · 중지 규칙 |
| 같은 순서 · 같은 trace 요구 | deterministic workflow |
| 고정 단계 + 소수(3~10%) 모호 사례 | hybrid<br>(workflow → agent 호출 → workflow 복귀) |
| 열린 평가 + 고정 형식 발행 | agentic loop → schema 계약 → workflow 발행 |
| 고정 사례 + 열린 사례 혼재<br>+ 비용 · 안전 제약 | 고정 = 규칙 · 열린 = Claude<br>모든 출력 code gate |
| 비용 절감 + precision 하한 | lane 분기 (tier 상향 ✗) |
| 정확해야 하는 합계 · 날짜 규칙 | 코드로 분리<br>Claude = 검증된 값 둘러싼 글쓰기 |
| 쓰기 통제권 유지 | 앱 코드가 쓰기 · 모델은 판단 1회 |
| 여러 팀 소유 super-agent<br>→ 실패 귀속 불가 | 경계 agent + 계약 + 얇은 orchestrator<br>+ agent별 eval · 버전 관리 |
| 지어낸 설명 · tenant 유출 0건 요구 | 구조적 통제<br>(결정 기록 조회 · tenant 범위 credential) |
| 되돌릴 수 없는 부수 효과 | 효과 전 사람 검토 (전체 context 제공) |
| 되돌릴 수 있음 + 대외적 난처함 | 코드 검사 + 사람 표본 검토 |
| trust boundary 위치 | 비신뢰 입력 진입점 · 모델 → 부수 효과 지점 |

![2장 규칙의 workflow 패턴과 agent 선택 decision tree](svg/1-rule-architecture-tree.svg)
*그림: 고정 단계부터 확인하고, agent는 중간 결과를 봐야 다음 단계가 정해질 때만 고른다*

![2장 규칙의 컨텍스트·subagent·state·tool 문제 진단](svg/1-rule-context-tree.svg)
*그림: 컨텍스트 문제마다 정답(격리, handoff 보강, 명시적 state, 겹침 제거)과 흔한 오답이 짝을 이룬다*

<sub>근거: Amey-0004, Amey-0023, Amey-0024, Amey-0026, Amey-0040, Amey-0060, CCAR-F-Amey-Thakur-0001, CCAR-F-Amey-Thakur-0011, CCAR-F-Amey-Thakur-0013, CCAR-F-Amey-Thakur-0015, CCAR-F-Amey-Thakur-0016, CCAR-F-Amey-Thakur-0051, CCAR-F-Amey-Thakur-0053, CCAR-F-MyPractice-0011, CCAR-F-Udemy01-0055, CCAR-F-Udemy02-0007, CCAR-F-Udemy02-0009, CCAR-F-Udemy02-0010, CCAR-F-Udemy02-0024, CCAR-F-Udemy03-0003, CCAR-F-Udemy03-0016, CCAR-F-Udemy03-0043, CCAR-F-Udemy04-0002, CCAR-F-Udemy04-0008, CCAR-F-Udemy04-0009, CCAR-F-Udemy04-0022, CCAR-F-Udemy04-0028, CCAR-F-Udemy04-0043, CCAR-F-Udemy04-0054, CCAR-F-Udemy05-0019, CCAR-F-Udemy05-0045, CCAR-F-Udemy06-0022, CCAR-F-Udemy06-0023, CCAR-F-Udemy06-0026, CCAR-F-Udemy06-0029, CCAR-F-Udemy06-0038, CCAR-F-Udemy06-0050, CCAR-F-paullarionov-0011, CCAR-F-preporato-0005, CCAR-F-preporato-0012, CCAR-P-Amey-Thakur-0005, CCAR-P-Amey-Thakur-0045, CCAR-P-jrajath94-0013, CCAR-P-jrajath94-0015, CCAR-P-jrajath94-0016, CCAR-P-jrajath94-0018, CCAR-P-jrajath94-0021, CCAR-P-jrajath94-0023, CCAR-P-jrajath94-0065, CCAR-P-jrajath94-0066, CCAR-P-jrajath94-0067, CCAR-P-jrajath94-0069, CCAR-P-jrajath94-0070, CCAR-P-jrajath94-0107, CCAR-P-jrajath94-0110, CCAR-P-jrajath94-0115, CCAR-P-jrajath94-0116, CCAR-P-jrajath94-0117, CCAR-P-jrajath94-0118, CCAR-P-jrajath94-0120, CCAR-P-jrajath94-0122, CCAR-P-jrajath94-0123, CCAR-P-jrajath94-0124, CCAR-P-jrajath94-0125, CCAR-P-jrajath94-0126, CCAR-P-jrajath94-0282, CCAR-P-jrajath94-0283, CCAR-P-jrajath94-0284, CCAR-P-jrajath94-0285, CCAR-P-jrajath94-0286, CCAR-P-jrajath94-0289, CCAR-P-jrajath94-0336, CCAR-P-jrajath94-0337, CCAR-P-jrajath94-0339, CCAR-P-jrajath94-0340, CCAR-P-jrajath94-0399, CCAR-P-jrajath94-0400, CCAR-P-jrajath94-0401, CCAR-P-jrajath94-0402, CCAR-P-jrajath94-0403, CCAR-P-jrajath94-0462, CCAR-P-jrajath94-0463, CCAR-P-jrajath94-0465, CCAR-P-jrajath94-0466, CCAR-P-jrajath94-0521, CCAR-P-jrajath94-0523, CCAR-P-jrajath94-0524, CCAR-P-jrajath94-0525, CCAR-P-jrajath94-0528, CCAR-P-jrajath94-0529, CCAR-P-jrajath94-0602, CCAR-P-jrajath94-0603, CCAR-P-jrajath94-0607, CCAR-P-jrajath94-0609, CCAR-P-preporato-0005, Patrick-0012, Patrick-0022, Patrick-0038, Patrick-0039, Preporato-0016, Preporato-0017, Preporato-0018, Preporato-0019, Udemy-0006, Udemy-0014, Udemy-0019, Udemy-0051, Udemy-0053</sub>

## 3. 자주 나오는 오답 함정

**패턴 선택**

| 오답 | 이유 |
|---|---|
| agent가 fixed code보다 유능 · 고품질 | 경로가 알려진 작업에서 자율성<br>→ 비용 · 비결정성만 증가 |
| agent는 불필요 단계 건너뛰기 가능 | validation 건너뛰기 = 결함 (기능 ✗) |
| 작업 길다 · tool 많다 ·<br>structured output 필요 → agent | 모두 고정 workflow로 충족 |
| 고정 단계에 orchestrator-workers<br>· 단계별 agent | 동적 분해 대상 없음<br>orchestrator 호출만큼 비용 · 불확실성 증가 |
| 고정 단계를 evaluator-optimizer로 | 반복 횟수 미지 → 시간 · 비용 불안정<br>하나의 출력 다듬는 구조도 아님 |
| 하나의 거대한 prompt로 전부 처리 | 단계 사이 checkpoint · 검증 소실 |
| 서로 감독하는 agent 2개 | supervision hierarchy = 위임 필요 문제 전용 |

**Subagent · 컨텍스트**

| 오답 | 이유 |
|---|---|
| subagent가 부모 이력 · system prompt 상속<br>→ 지시 짧게 써도 됨 | 상속은 fork형뿐<br>일반 subagent = 빈 컨텍스트에서 시작 |
| context 격리로 시스템 전체 토큰 감소 | 각자 따로 읽음 → 증가 가능<br>격리 이점 = 부모 컨텍스트 보호 |
| subagent 품질 저하<br>→ 더 큰 모델 · subagent 추가 | 빠진 컨텍스트는 모델 크기로 못 채움<br>subagent 증가 → 결함도 증가 |
| subagent로 합의 · rate limit 우회 · fallback | subagent 가치 = 위임 · 컨텍스트 격리 |
| subagent끼리 직접 통신 | 결과 통합 · 실패 격리하는 coordinator 소실 |

**Loop · state**

| 오답 | 이유 |
|---|---|
| 컨텍스트 부족 → `max_tokens` 상향 | `max_tokens` = 출력 제한 · 문제는 입력 |
| step ceiling 목적<br>= 성공한 실행의 비용 절감 · 속도 | 비수렴(무한 loop) 방지 안전 상한 |
| tool 많을수록 빠르고 저렴 | 겹치는 tool → 선택 오류 증가 |

**구현 수단**

| 오답 | 이유 |
|---|---|
| Agent SDK 장점 = streaming | streaming은 Client SDK에서도 가능 |
| Agent SDK로 Anthropic 인프라 호스팅 | 호스팅 = Managed Agents<br>Agent SDK = 사용자 프로세스 실행 |
| Agent SDK 제품을 claude.ai 로그인으로 사용 | API key 인증 필요 |
| Agent SDK가 vector DB ·<br>fine-tuning · 시각 designer 제공 | 미제공 |
| Managed Agents + self-hosted sandbox<br>→ 세션 로그도 자사 | session · event log = Anthropic 쪽 저장 |
| Message Batches API로 agent 실행 | 비동기 일괄 요청용 · loop · 세션 미제공 |
| LangGraph → 호출 · 토큰 감소 | 비용 절감 도구 ✗ |
| LangGraph → prompt · 구성 직접 작성 불필요 | 저수준 → 구성은 개발자 설계 |
| 공유 대화 기록으로 lead가 모든 턴 열람 | subagent별 대화 기록 따로 유지<br>lead = 최종 보고서 수신 |
| 한 agent에 tool 전부 부여 후 순차 분석 | capability bloat · 병렬 포기 · context 혼합 |
| 병합 없는 별도 agent 3개 + 수작업 병합 | synthesis · 병합 규칙 부재 → 일관성 ✗ |
| 판단 필요한 검토를 모델 없는 workflow로 | 판단 제거 |
| 원본 출력을 이어 붙여 최종 결과로 반환 | synthesis 없음 · 통합 품질 ✗ |
| 한 agent가 다른 agent에 직접 결과 전달 · 요청 | coordinator 제어 상실 |
| 공유 scratchpad · peer 메시지 · 전체 이력 공유 | 조정 책임 분산 → 모순 · 중복 감지 주체 불명 |
| 순차 실행으로 충돌 회피 | 병렬성 파괴 (researcher 6개 = 6배 시간) |
| 개인 memory + 출력 이어 붙임 · peer 채팅 | 중복 · 병합 충돌 · 비구조 · orchestrator 가시성 ✗ |
| 충돌 평가를 평균 · 선착순 · 3번째 worker 다수결 | 아무도 안 낸 판단 · 임의 · 증거 없는 투표 |
| 두 worker 일치할 때까지 재실행 | 종료 보장 없음 · 예산 소진 |
| 전사와 번역 충돌을 다수결 · 특정 worker 우선 | 서로 다른 것을 판단 · 위세로 승자 · 재발 |
| 불일치 해법 = 더 큰 모델 · worker 추가 · timeout 연장 | 자원 추가일 뿐 규칙 아님 |
| 발견 반영이 필요한 조사에 고정 pipeline | 도중 발견을 반영 못함 |
| 더 큰 context window | 구조 부재 미해결 → 훑기만 함 |
| 계획 없이 페이지별 순차 작성 | 일관성 없는 보고서 · 개요 이탈 |
| 출처 대부분 폐기 | 종합 제약 위반 |
| 독립 작업을 chain · 고정 순서 직렬 | 지연만 증가 · 독립성 미활용 |
| 의존 선행 없이 합류 작업 병렬 | 안전 위반 · 결함 |
| 순차 대화를 다중 subagent로 fan-out | 분할이 아닌 중복<br>대화 컨텍스트 분절 |
| subagent 수만 축소 (5 → 3) | 같은 구조 결함 |
| 순차 대화에 voting | 비용 증가 · 컨텍스트 분절 |
| 더 큰 모델로 분해 실수 해결 | 작업이 순차인 한 변함없음 |
| 협상 · 얽힌 작업을 supervisor + worker로 분할 | 파편화 · handoff 비용이 이득 초과 |
| 분할 후 검사자 추가 | 병은 검사 부족이 아닌 분할 |
| 라운드를 사전 고정 | 상대 반응에 따라 적응 필요 |
| 공유 sandbox = 공유 컨텍스트 | subagent는 각자 대화 기록 유지 |
| 한 설계에 패턴 하나만 | 독립 규모 · 품질 편차는 별개 문제 |
| 반복 작업 120건을 한 호출 | context 초과 · 건별 점검 없음 |
| 모든 티켓을 전 단계 chain 통과 | 형태 문제 → 낭비 단계 · 분기 부재 |
| chain 유지 + 추론 추가 · 상위 모델 · caching | 분기 부재 미해결<br>caching = prefix 안정일 때만 이득 |
| 12단계 chain에 상위 모델 | 한 단계 오류 지배 + 그 단계가 어려울 때만 유효<br>초안 재작성 · 지연 합산 그대로 |
| 13번째 비평 단계 추가 | 이미 재작성 과다 · 짧고 검사 가능한 chain에만 유효 |
| caching으로 오류 누적 해결 | 안정 prefix · 지연 문제에만 이득 |
| 현재 가격을 캐시 · 다단계 chain으로 응답 | 스냅샷 = 오래된 답 · 대기 증가 |
| 문서 다수를 한 컨텍스트에 투입 | 중간 문서 묻힘 · 주의 희석 |
| 인용을 기억에서 생성 · 초안 후 추가 | 출처 신뢰 불가 · 추적성 붕괴 |
| 섹션 순차 chain 재작성 | 오류 누적 · 출처 불명 숫자 |
| 공유 용어집 없는 독립 agent | 언어 간 용어 drift 보장 |
| 단일 교정 agent로 전량 검수 | 순차 병목 → 기한 초과 |
| 반복 횟수 상한을 주된 종료 조건으로 사용 | 복잡한 건만 중간 절단 · 상한은 안전장치 |
| `temperature` 0 · 큰 모델 · context 확대로 loop 해결 | 반복 제한 ✗ · 수렴 보장 ✗ |
| `effort` low · Stop hook으로 지출 상한 | turn당 소비만 변경 · loop 끝나야 발화 |
| prompt 강화 · `CLAUDE.md` 강조 · few-shot<br>· `temperature` 0 → 100% 준수 기대 | 확률적 · 실패율 0 ✗ |
| 모델 self-check · 2 agent 투표로 비가역 통제 | 모델 판단 · 결정 주체 불변 |
| 전면 사람 검토 · 10% 표본 검토 | 규모상 비실현 · 실패 90% 통과 |
| 단계 미정 작업을 코드에 하드코딩 | 다음 단계를 결과로 정하는 작업에 부적합 |
| 규칙 고정 작업에 agent<br>(미래 유연성 · step 한도<br>· 관심사 분리 multi-agent) | 필요 없는 비용 그대로<br>비결정성만 추가 |
| agent 3개가 순서를 협상 | 고정 순서에 비결정성만 추가<br>과잉 설계 |
| tool을 쓰니 agentic | 기준 = 단계를 누가 정하나<br>고정 경로 = 도구 가진 workflow |
| 순차 3단계 → agent 3개 | 순차 단계 ≠ agent<br>orchestration overhead만 추가 |
| 모든 리뷰 코멘트를 사람이 승인 | 자동화 목표 무력화 · 설계가 요구 ✗ |
| workflow 선택 이유 = agent는 새롭고 덜 검증<br>· workflow는 항상 정확<br>· 팀 시간 부족 | 엔지니어링 근거 아님<br>근거 = 경로가 알려졌는가 |
| 열린 연구를 고정 10단계 workflow로 | 실행 전에 없는 단계는 나열 불가 |
| 열린 연구를 검색 10회 담은 prompt 1개 | 의외의 발견 시 재계획 지점 없음 |
| super-agent에 label 붙은 memory 섹션 | 소유권 · 독립 평가 생성 ✗<br>귀속 = 여전히 의견 문제 |
| 릴리스마다 각 팀이 전체 prompt 공동 검토 | 팀 결합 → 독립 배포와 정반대 |
| 환각 감소용 더 큰 모델로 라우팅<br>(bigger-model 함정) | 실패는 아키텍처 문제 · 용량 ✗ |
| system prompt에 규제 주의 · 예시 보강<br>(prompt-plea) | 우회 가능 · 검증 불가<br>컴플라이언스 위험 |
| 내부 agent가 가입자 질문에 직접 응답 | 방어 장치 없이 위험만 상승 |
| 두 번째 agent가 유출을 검토 | 검토자도 모델: 놓침 · 속음<br>비용 · 지연 2배 |
| 교차 tenant 접근 로깅 | 유출 후 탐지 · 방지 ✗ |
| 사람이 모든 건 검토 | 대량엔 불가<br>triage 실패는 그대로 남음 |
| 검사 없는 agent · 최상위 tier 일괄 처리 | gate 없음<br>tier 일괄 = 예산 위반 · 고정 건에도 agent 비용 |
| 모든 호출에 explicit reasoning | 기준 충족 상태에서 출력 token · 지연만 추가 |
| 가변 꼬리까지 대화 전체 cache | prefix 불안정 → hit rate ≈ 0<br>write 비용은 계속 청구 |
| few-shot · 큰 tier · 2차 Claude 호출로 산술 보장 | 모두 샘플링 → 보장 ✗ |
| 정확도가 높으니 검토 생략 | 정확도 = 지표<br>지표는 부수 효과를 gate ✗ |
| 원시 입력 단계 검토 | 판단할 제안이 없음 |
| 되돌릴 수 없는 행동 뒤 사후 검토 | 피해 이후 |
| trust boundary = logger · 순수 함수 사이 | 내부 구간 |

<sub>근거: Amey-0004, Amey-0023, Amey-0024, Amey-0025, Amey-0026, Amey-0041, Amey-0059, CCAR-F-Amey-Thakur-0011, CCAR-F-Amey-Thakur-0012, CCAR-F-Amey-Thakur-0013, CCAR-F-Amey-Thakur-0016, CCAR-F-Amey-Thakur-0051, CCAR-F-Amey-Thakur-0052, CCAR-F-Amey-Thakur-0067, CCAR-F-MyPractice-0002, CCAR-F-MyPractice-0008, CCAR-F-Udemy01-0014, CCAR-F-Udemy01-0036, CCAR-F-Udemy01-0045, CCAR-F-Udemy01-0055, CCAR-F-Udemy02-0007, CCAR-F-Udemy02-0009, CCAR-F-Udemy02-0045, CCAR-F-Udemy02-0060, CCAR-F-Udemy03-0016, CCAR-F-Udemy03-0024, CCAR-F-Udemy04-0008, CCAR-F-Udemy04-0028, CCAR-F-Udemy04-0043, CCAR-F-Udemy04-0048, CCAR-F-Udemy04-0053, CCAR-F-Udemy04-0054, CCAR-F-Udemy05-0045, CCAR-F-Udemy06-0023, CCAR-F-Udemy06-0029, CCAR-F-Udemy06-0051, CCAR-F-paullarionov-0002, CCAR-F-paullarionov-0008, CCAR-F-paullarionov-0051, CCAR-F-preporato-0005, CCAR-F-preporato-0012, CCAR-P-Amey-Thakur-0005, CCAR-P-Amey-Thakur-0045, CCAR-P-jrajath94-0013, CCAR-P-jrajath94-0015, CCAR-P-jrajath94-0016, CCAR-P-jrajath94-0018, CCAR-P-jrajath94-0021, CCAR-P-jrajath94-0023, CCAR-P-jrajath94-0065, CCAR-P-jrajath94-0066, CCAR-P-jrajath94-0067, CCAR-P-jrajath94-0069, CCAR-P-jrajath94-0070, CCAR-P-jrajath94-0107, CCAR-P-jrajath94-0110, CCAR-P-jrajath94-0114, CCAR-P-jrajath94-0115, CCAR-P-jrajath94-0116, CCAR-P-jrajath94-0117, CCAR-P-jrajath94-0119, CCAR-P-jrajath94-0120, CCAR-P-jrajath94-0122, CCAR-P-jrajath94-0123, CCAR-P-jrajath94-0124, CCAR-P-jrajath94-0125, CCAR-P-jrajath94-0126, CCAR-P-jrajath94-0282, CCAR-P-jrajath94-0283, CCAR-P-jrajath94-0285, CCAR-P-jrajath94-0286, CCAR-P-jrajath94-0289, CCAR-P-jrajath94-0523, CCAR-P-jrajath94-0524, CCAR-P-jrajath94-0602, CCAR-P-jrajath94-0603, CCAR-P-jrajath94-0605, CCAR-P-jrajath94-0607, CCAR-P-preporato-0004, Patrick-0012, Patrick-0038, Patrick-0039, Preporato-0017, Preporato-0019, Udemy-0004, Udemy-0014, Udemy-0019, Udemy-0051, Udemy-0053</sub>

## 4. 암기 목록

| 이름 | 의미 |
|---|---|
| `stop_reason: "max_tokens"` | 출력 상한 도달 → 별도 처리 필요 (종료 신호 ✗) |
| `max_tokens` | 출력 길이 제한 · 입력 컨텍스트와 무관 |
| step ceiling = max iteration cap | 비수렴 loop에 대한 안전 상한 |
| prompt chaining | 고정 순서 + 단계 사이 gate |
| routing | 분류 → 전용 처리로 보냄 |
| parallelization (voting) | 같은 작업 여러 번 실행 → 다수결 |
| evaluator-optimizer | 채점 → 수정 반복 |
| `model` (subagent 정의) | subagent별 가벼운 모델 지정 → 비용 절감 |
| tool runner (beta) | Client SDK에서 tool loop 대행 |
| Managed Agents | Anthropic이 loop · sandbox 호스팅<br>session · event log = Anthropic 쪽 저장 |
| LangGraph | 저수준 stateful orchestration<br>durable execution · human-in-the-loop<br>state 영속화 |
| handoff contract | 입력 · 출력 · 병합 규칙 · 불일치 규칙<br>(해설 용어) |
| disagree rule | 충돌 시 우선 근거 · arbiter 지정 + 적용 기록 |
| arbiter | worker 충돌을 contract 규칙대로 결정하는 중재자 |
| critic 단계 | 조항 원문 + 두 근거로 재검토 |
| checkpoint | 각 handoff 저장 → 실패 시 재개<br>판단 망설임 지점 = 사람 피드백 |
| sectioning | 독립 서브태스크 분할 → 동시 실행 → 집계 |
| fan-out / fan-in | 독립 조각 병렬 실행 / 결과 병합 |
| validation gate | 병합 후 코드 · 기준 대조 검사 |
| disagree rule | fan-in에서 결과 충돌을 처리하는 규칙 |
| critique | 점검자 + 기준 + 수정 loop로 품질 편차 대응 |
| triage | 복잡도 판정 → 투입 agent · 호출 수 조정 |
| `session budget` | list cost 상한 → 새 모델 요청 중단<br>Managed Agents beta 기능 |
| augmented LLM · augmented single call | 도구 가진 단일 판단<br>(고정 경로 + 열린 1단계) |
| hybrid | workflow ↔ agent를 오가는 구조<br>(전환 지점 = handoff) |
| lane | 입력 형태별 처리 경로 (규칙 · Claude) |
| code gate | 부수 효과 앞에서 코드로 검사 |
| prompt-plea | 보장을 prompt 지시에 의존하는 함정 |
| bigger-model 함정 | 구조 문제를 큰 모델로 해결하려는 오답 |
| system of record | 신뢰 출처 DB · 점검 기준 |
| trust boundary | 비신뢰 입력 진입점 · 모델 출력의 부수 효과 지점 |

<sub>근거: Amey-0005, Amey-0026, CCAR-F-Udemy01-0003, CCAR-F-Udemy01-0045, CCAR-F-Udemy01-0060, CCAR-F-Udemy03-0003, CCAR-F-Udemy03-0016, CCAR-F-Udemy04-0008, CCAR-F-Udemy04-0016, CCAR-F-Udemy04-0053, CCAR-P-jrajath94-0018, CCAR-P-jrajath94-0065, CCAR-P-jrajath94-0069, CCAR-P-jrajath94-0107, CCAR-P-jrajath94-0110, CCAR-P-jrajath94-0119, CCAR-P-jrajath94-0121, CCAR-P-jrajath94-0122, CCAR-P-jrajath94-0123, CCAR-P-jrajath94-0282, CCAR-P-jrajath94-0283, CCAR-P-jrajath94-0285, CCAR-P-jrajath94-0289, CCAR-P-jrajath94-0336, CCAR-P-jrajath94-0340, CCAR-P-jrajath94-0399, CCAR-P-jrajath94-0400, CCAR-P-jrajath94-0401, CCAR-P-jrajath94-0402, CCAR-P-jrajath94-0524, CCAR-P-jrajath94-0527, CCAR-P-jrajath94-0603, Patrick-0038, Preporato-0019, Udemy-0004, Udemy-0006, Udemy-0014, Udemy-0019, Udemy-0051, Udemy-0053</sub>

## 5. 시험 직전 체크리스트

- [ ] workflow vs agent = 다음 단계 결정 주체(코드 vs 모델)
- [ ] 단계 고정 → prompt chaining + validation gate
- [ ] 단계 고정에 agent · orchestrator ✗
- [ ] 분류만 = routing · 다수결 = voting
- [ ] context 격리 = 부모 window 보호 · 총 토큰 감소 ✗
- [ ] 오래 유지할 결정 → compaction과 무관한 명시적 state
- [ ] 겹치는 tool → 잘못된 tool 선택 증가
- [ ] Agent SDK = 자사 프로세스 실행 · API key 인증
- [ ] Managed Agents = 호스팅 · 세션 로그 모두 Anthropic
- [ ] data residency → self-hosted Agent SDK
- [ ] worker 충돌 → contract 불일치 규칙(critic · arbiter) 적용 · 기록
- [ ] 독립 = 병렬 · 의존 = 순차 · 순차 대화 = 단일 agent
- [ ] 유형별 처리 상이 = routing · 품질 편차 = critique
- [ ] 확실히 막을 규칙 = `PreToolUse` hook · gate (prompt · `PostToolUse` ✗)
- [ ] gate 조건 = 검증된 결과 · 비가역 작업 = 사람 승인 (모델은 제안)
- [ ] 고정 뼈대 + 소수 모호 사례 = hybrid (lane 분기)
- [ ] 0건 보장 요구 = 구조적 통제 · 부수 효과 앞 gate

<sub>근거: Amey-0004, Amey-0023, Amey-0024, Amey-0041, Amey-0059, Amey-0073, CCAR-F-Amey-Thakur-0015, CCAR-F-Udemy01-0019, CCAR-F-Udemy04-0005, CCAR-F-Udemy04-0008, CCAR-F-preporato-0005, CCAR-P-jrajath94-0065, CCAR-P-jrajath94-0066, CCAR-P-jrajath94-0067, CCAR-P-jrajath94-0122, CCAR-P-jrajath94-0124, CCAR-P-jrajath94-0283, CCAR-P-jrajath94-0285, CCAR-P-jrajath94-0336, CCAR-P-jrajath94-0340, Udemy-0004, Udemy-0006, Udemy-0019, Udemy-0051, Udemy-0053</sub>
