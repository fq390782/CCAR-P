@@ ADD-TO: ### 1.2 Workflow 패턴 구분

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
| voting과 구분 | voting = 같은 작업 반복<br>sectioning = 서로 다른 부분 분할 |
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

<sub>근거: CCAR-F-Udemy01-0055, CCAR-F-Udemy02-0007, CCAR-F-Udemy02-0024, CCAR-F-Udemy03-0003, CCAR-F-Udemy03-0016, CCAR-P-jrajath94-0021, CCAR-P-jrajath94-0116, CCAR-P-jrajath94-0123, CCAR-P-jrajath94-0124, CCAR-P-jrajath94-0125, CCAR-P-jrajath94-0289, CCAR-P-jrajath94-0340, CCAR-P-jrajath94-0402, CCAR-P-jrajath94-0403, CCAR-P-jrajath94-0529</sub>

@@ ADD-TO: ### 1.3 Coordinator(orchestrator) 1개 + Subagent n개 구조

**Multi-agent 적합 · 부적합 판단**

| 상황 | 판단 |
|---|---|
| 하위 작업 독립 · 상태 비공유<br>· 도구 상이 · 결과 병합 필요 | multi-agent 유리<br>fan-in에 병합 · disagree rule |
| 조각이 상태 공유 | 단일 agent |
| 순차 대화<br>(각 응답이 이전 내용에 의존) | fan-out ✗ → 단일 agent<br>병렬 agent = 작업 분할 아닌 작업 중복 |
| 병렬성이 실제로 있는 부분 | 그 부분만 병렬 유지 |
| 라운드마다 이전 결과 · 전체 이력 필요<br>(다회 협상) | 단일 agent loop 유지<br>이력 · 라운드 로그를 한 컨텍스트에 보유 |
| supervisor + worker로 분할 | handoff마다 전체 이력 운반<br>→ 병렬 이득 없이 조율 비용만 |
| 라운드마다 handoff 내용 변동 | handoff 계약이 낡음 |
| 단일 agent 컨텍스트 증가 | 집중 희석 점검 · 라운드 사이 compact |
| 단계별 공유 문서 편집<br>(각 단계가 직전 결과 필요) | 하나의 thread + 고정 순서<br>단계마다 확인 → 일관된 문서 유지 |
| 공유 sandbox | 공유 컨텍스트 ✗<br>subagent는 각자 대화 기록 별도 유지 |

<sub>근거: CCAR-P-jrajath94-0066, CCAR-P-jrajath94-0120, CCAR-P-jrajath94-0402, CCAR-P-jrajath94-0607</sub>

@@ NEW-SECTION
### 분해 방식 선택 — 고정 chain vs 동적 분해
**절차를 사전에 정할 수 있나로 선택**

| 작업 성격 | 분해 | 근거 |
|---|---|---|
| 정형 · 반복 점검<br>(PR 체크 · 템플릿 검수) | 고정 순차 chain | 확인 항목 · 순서 고정<br>→ 일관성 · 검증 용이 |
| 범위 미정 조사 · 원인 탐색 | 동적 분해 | 발견에 따라 다음 단계 변동 |
| 한 도구에 두 유형 공존 | 의뢰 유형 판정 → 분기 | 정형 = chain<br>조사 = 동적 분해 |

| 판단 단서 | 선택 |
|---|---|
| "이후 절차는 발견 결과에 따라 달라짐" | 동적 분해<br>(orchestrator가 분해 · 위임 · 통합) |
| 확인 항목 목록이 사전 확정 | 고정 chain |
| 실행마다 확인 항목이 빠지거나 늘어남 | 정형 작업을 범용 agent에 맡긴 결과<br>→ 항목 고정 chain 필요 |
| 다음 확인 대상이 이전 확인 결과로 결정 | 열린 조사 → 동적 분해 |
| 재사용 workflow 중 일부 절차만 가변 | 읽기 단계 고정<br>이후 = 조사 결과로 서브태스크 생성 · 통합 |
| 커버리지 > 지연 시간 | 동적 분해 허용 |
| 동적 분해 도입 | 비용 증가 · 탈선 위험<br>→ 모델 바깥에서 강제하는 한도 병행 |

<sub>근거: CCAR-F-Udemy02-0009, CCAR-F-Udemy04-0008, CCAR-F-Udemy06-0029, CCAR-F-preporato-0012</sub>

@@ NEW-SECTION
### 동적 분해 절차 — 탐색 · 우선순위 · 계획 갱신
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

<sub>근거: CCAR-F-Udemy02-0045, CCAR-F-Udemy03-0050, CCAR-F-Udemy04-0022, CCAR-F-Udemy05-0019, CCAR-F-Udemy06-0038, CCAR-P-jrajath94-0015</sub>

@@ NEW-SECTION
### 분해 품질 결함 — 누락 · 중복 · 축 오류
**subagent 정상이면 원인은 coordinator 분해**

| 증상 | 원인 | 조치 |
|---|---|---|
| 전 subagent 정상 완료<br>보고서가 일부 영역만 다룸 | 분해가 좁음<br>(하위 작업이 한 영역에 집중) | 넓은 주제 전체 영역을 덮는 분해 |
| agent 간 결과 중복<br>token 2~3배 · 폭 불변 | 작업 경계 불명 · 같은 지시 | 위임 전 조사 영역 명시 분할 |
| 정보원별 분해인데 영역 누락 | 축 오류<br>= 어디(정보원)만 할당<br>무엇(주제 영역) 미할당 | 주제 영역별 분해 · 담당 할당 |
| 같은 지시 받은 subagent들이<br>같은 소견 반환 | 병렬 효과 ✗ · 통합 부담만 증가 | 문서 그룹 · 추출 관점으로 비중복 분할 |

| 구분 | 내용 |
|---|---|
| subagent 컨텍스트 | 분리 → 서로의 작업 모름<br>같은 지시 = 같은 검색 |
| 중복 방지 책임 | 작업을 분해 · 위임하는 coordinator |
| 분할 축 | 하위 주제 · 정보원 종류<br>문서 그룹 · 추출 관점 |
| 분할 점검 | 담당 범위가 겹치지 않는지<br>통합 측으로 가는 분량이 억제됐는지 |
| 반환 | 간결한 소견만 → 통합 context 비대화 방지 |

**위임 prompt 구성 요소**

| 요소 | 내용 |
|---|---|
| 목적 | 무엇을 위한 조사인지 |
| 출력 형식 | 반환 형식 지정 |
| 도구 · 정보원 지침 | 사용할 도구 · 출처 범위 |
| 작업 경계 | 담당 범위 + 비담당 범위 모두 명시<br>상세 기술 없음 → 중복 · 공백 |
| 필요 context | 분할된 담당에 필요한 정보 전달 |

**진단 순서**

| 단계 | 확인 |
|---|---|
| 로그 확인 | coordinator 분해 목록에 영역 이름이 있는지<br>없음 → 분해 축 결함 |
| 통합 전 점검 | 분해 결과 · 영역별 담당 출력<br>→ 파악 영역 전부 조사됐는지 확인 |
| 선택지 판별 | 분해 단위를 바꾸는 안인지 확인<br>키워드 · 정보원 · 검색 건수 추가 = 양만 조정 |

<sub>근거: CCAR-F-MyPractice-0004, CCAR-F-MyPractice-0011, CCAR-F-Udemy03-0043, CCAR-F-Udemy05-0025, CCAR-F-Udemy06-0026, CCAR-F-paullarionov-0004, CCAR-F-paullarionov-0011</sub>

@@ NEW-SECTION
### 의존성 기반 병렬 · 순차 결정
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
| ⚠️ tool 이름 | 문항 표기 = Agent tool(구 Task tool)<br>이름은 버전 의존 — 2.1.63에서 Task → Agent로 변경<br>(구 `Task(...)` 표기는 alias) |
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

<sub>근거: CCAR-F-MyPractice-0048, CCAR-F-Udemy02-0024, CCAR-F-Udemy03-0016, CCAR-F-Udemy04-0054, CCAR-F-Udemy05-0035, CCAR-F-paullarionov-0048, CCAR-F-preporato-0005, CCAR-P-jrajath94-0286, CCAR-P-jrajath94-0339, CCAR-P-jrajath94-0465, CCAR-P-jrajath94-0466, CCAR-P-jrajath94-0528</sub>

@@ RULES

| 상황 | 정답 |
|---|---|
| 정형 · 반복 점검 (항목 고정) | 고정 순차 chain |
| 범위 미정 조사 · 원인 탐색 · 레거시 전반 작업 | 동적 분해<br>(구조 파악 → 우선순위 → 갱신) |
| 한 도구에 정형 + 조사 의뢰 공존 | 유형 판정 후 분기<br>(정형 = chain · 조사 = 동적) |
| 열린 조사에 동적 분해 적용 | 모델 바깥에서 강제하는 한도 병행 |
| 대량 파일 검토 + 중간 산출물 로그 필요 | 파일 단위 호출 chain + 통합 호출 |
| 고정 순서 chain에서 오류 누적 · 지연 합산 | 독립 조각 병렬 · 재작성 제거<br>확실한 작업 = deterministic code<br>병합에 validation gate |
| subagent 정상 + 보고서 영역 누락 | coordinator 분해 범위 점검 (좁은 분해) |
| agent 간 결과 중복 · token 증가 | 위임 전 조사 영역 분할<br>담당 · 비담당 범위 기재 |
| 정보원별 분해 + 주제 영역 누락 | 주제 영역별 분해로 축 변경 |
| 낯선 주제 포괄성 낮음 | 사전 광범위 탐색 + 공백에만 2차 할당 |
| 독립 관점 · 항목 다수 | sectioning 병렬 → 집계 |
| 독립 작업 + 합류 작업 | 독립 병렬 → fan-in → 합류 작업 순차 |
| 의존 관계가 주어진 일정 · 절차 | 의존 쌍은 순차 · 나머지만 병렬 |
| 독립 위임 여러 개 | 한 응답에 Agent tool 호출 동시 출력 |
| 순차 대화 · 라운드 의존 · 얽힌 작업 | 단일 agent (fan-out ✗) |
| 단계별 공유 문서 편집 | 하나의 thread · 고정 순서 · 단계별 확인 |
| 한 문의에 여러 용건 | 이슈별 분해 → 공유 context 병렬 조사 → 종합 |
| 유형별 처리가 다른 입력 | route 먼저 · 유형별 경로 |
| 단순 요청에도 전 전문 agent 호출 | triage + 해당 agent에만 routing<br>단순 확인은 직접 답변 |
| 질의 형태 혼재 (현재값 + 독립 문서 다수) | 현재값 = 도구 호출 · 문서 = fan-out + 병합 gate |
| 독립 조각 + 품질 편차 | fan-out + critique(점검자 · 기준) → 병합 |
| 병합 숫자 · 인용 정합 필요 | 코드 검사 gate · 인용은 생성 시점에 부착 |
| 대규모 번역 · 용어 일관 | 병렬 fan-out + 공통 용어집 주입 + 계층적 병합 |

<sub>근거: CCAR-F-MyPractice-0004, CCAR-F-MyPractice-0011, CCAR-F-MyPractice-0048, CCAR-F-Udemy01-0055, CCAR-F-Udemy02-0007, CCAR-F-Udemy02-0009, CCAR-F-Udemy02-0024, CCAR-F-Udemy02-0045, CCAR-F-Udemy03-0003, CCAR-F-Udemy03-0016, CCAR-F-Udemy03-0043, CCAR-F-Udemy03-0050, CCAR-F-Udemy04-0008, CCAR-F-Udemy04-0022, CCAR-F-Udemy04-0054, CCAR-F-Udemy05-0019, CCAR-F-Udemy05-0025, CCAR-F-Udemy05-0035, CCAR-F-Udemy06-0026, CCAR-F-Udemy06-0029, CCAR-F-Udemy06-0038, CCAR-F-paullarionov-0004, CCAR-F-paullarionov-0011, CCAR-F-paullarionov-0048, CCAR-F-preporato-0005, CCAR-F-preporato-0012, CCAR-P-jrajath94-0015, CCAR-P-jrajath94-0021, CCAR-P-jrajath94-0066, CCAR-P-jrajath94-0116, CCAR-P-jrajath94-0120, CCAR-P-jrajath94-0123, CCAR-P-jrajath94-0124, CCAR-P-jrajath94-0125, CCAR-P-jrajath94-0286, CCAR-P-jrajath94-0289, CCAR-P-jrajath94-0339, CCAR-P-jrajath94-0340, CCAR-P-jrajath94-0402, CCAR-P-jrajath94-0403, CCAR-P-jrajath94-0465, CCAR-P-jrajath94-0466, CCAR-P-jrajath94-0528, CCAR-P-jrajath94-0529, CCAR-P-jrajath94-0607</sub>

@@ TRAPS

**분해 진단**

| 오답 | 이유 |
|---|---|
| 누락 원인 = subagent 실행 · 요약 품질 | subagent는 할당을 정상 수행<br>원인 = coordinator의 좁은 분해 |
| 통합 단계에서 중복 제외 | 사후 정리 · 경계 불명 원인 미해결 |
| 1개 agent로 집약 | 병렬화 이점 포기 |
| 대화 기록 전체 전달로 범위 구분 | 담당 범위 구분 ✗ |
| 전원이 전체 건 검토 · 중첩 상세 요약 | 중복 · 통합 context 비대 |
| 키워드 · 정보원 · 검색 건수 추가 | 정보원별 분해 유지 → 양만 조정 |
| 통합 단계에서 공백 보완 | 추가 조사 없는 근거 없는 보완 |
| 출처 단위 분할 | 이미 취득한 범위 안의 병렬화 |
| 전 주제 할당 수 일률 증가 | 공백 아닌 전체 증가 → 비용만 상승 |

**동적 · 고정 분해**

| 오답 | 이유 |
|---|---|
| 발견 반영이 필요한 조사에 고정 pipeline | 도중 발견을 반영 못함 |
| 열린 조사를 사전 병렬 분할 | 노력 낭비 · 발견을 연결할 주체 없음 |
| 증거 수집 수단 없이 답만 요구 | 확인할 방법 부재 |
| 처리 상한(예산)만 인상 | 문제는 처리량 아닌 순서 |
| 사전 균등 분할 | 예측 가능한 정형 작업용 분해 |
| 디렉터리 · 알파벳 순 처리 | 작업 편의순 · 중요도 미반영 → 재작업 |
| 의존 파악 없이 병렬 수정 | 미지의 의존 관계 대응 ✗ |
| 더 큰 context window | 구조 부재 미해결 → 훑기만 함 |
| 계획 없이 페이지별 순차 작성 | 일관성 없는 보고서 · 개요 이탈 |
| 출처 대부분 폐기 | 종합 제약 위반 |
| 반복 횟수 조정 | 분해 방식 불변 |
| 전 파일 일괄 로드 | 동적 조사 이점 폐기 |
| 두 유형에 같은 범용 방식 · 일괄 처리 | 작업 성격 차이 무시 |
| 직접 실행으로 시작 | 상황 파악 전에 수정 |

**병렬 · 순차 · 단일 agent**

| 오답 | 이유 |
|---|---|
| 의존 작업까지 전부 동시 위임 | 의존 관계 무시 (비교는 개별 결과 필요) |
| 여러 작업을 하나의 prompt로 묶음 | 병렬화 이점 폐기 |
| 순차 인계 · 병렬 도구 비활성화 | 순차라는 원인 그대로 |
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

**Routing · chain · 병합**

| 오답 | 이유 |
|---|---|
| 모든 티켓을 전 단계 chain 통과 | 형태 문제 → 낭비 단계 · 분기 부재 |
| chain 유지 + 추론 추가 · 상위 모델 · caching | 분기 부재 미해결<br>caching = prefix 안정일 때만 이득 |
| 12단계 chain에 상위 모델 | 한 단계 오류 지배 + 그 단계가 어려울 때만 유효<br>초안 재작성 · 지연 합산 그대로 |
| 13번째 비평 단계 추가 | 이미 재작성 과다 · 짧고 검사 가능한 chain에만 유효 |
| caching으로 오류 누적 해결 | 안정 prefix · 지연 문제에만 이득 |
| 현재 가격을 캐시 · 다단계 chain으로 응답 | 스냅샷 = 오래된 답 · 대기 증가 |
| 문서 다수를 한 컨텍스트에 투입 | 중간 문서 묻힘 · 주의 희석 |
| 인용을 기억에서 생성 · 초안 후 추가 | 출처 신뢰 불가 · 추적성 붕괴 |
| 섹션 순차 chain 재작성 | 오류 누적 · 출처 불명 숫자 |
| 개별 용어집 가진 독립 agent | 언어 간 용어 drift 보장 |
| 단일 교정 agent로 전량 검수 | 순차 병목 → 기한 초과 |
| 응답 단축 | 호출 후 대증요법 · 호출 범위 미조정 |
| prompt 통합 | 전문 분화 폐기 |
| worker가 스스로 skip 판단 | 기동 낭비 그대로 |
| 일부 subagent 통합 | 전 건 순차 통과 구조 유지 |

<sub>근거: CCAR-F-MyPractice-0004, CCAR-F-MyPractice-0011, CCAR-F-Udemy01-0055, CCAR-F-Udemy02-0007, CCAR-F-Udemy02-0009, CCAR-F-Udemy02-0024, CCAR-F-Udemy02-0045, CCAR-F-Udemy03-0003, CCAR-F-Udemy03-0016, CCAR-F-Udemy03-0043, CCAR-F-Udemy03-0050, CCAR-F-Udemy04-0008, CCAR-F-Udemy04-0022, CCAR-F-Udemy04-0054, CCAR-F-Udemy05-0019, CCAR-F-Udemy05-0025, CCAR-F-Udemy05-0035, CCAR-F-Udemy06-0026, CCAR-F-Udemy06-0029, CCAR-F-Udemy06-0038, CCAR-F-paullarionov-0004, CCAR-F-paullarionov-0011, CCAR-F-paullarionov-0048, CCAR-F-preporato-0005, CCAR-F-preporato-0012, CCAR-P-jrajath94-0015, CCAR-P-jrajath94-0021, CCAR-P-jrajath94-0066, CCAR-P-jrajath94-0116, CCAR-P-jrajath94-0120, CCAR-P-jrajath94-0123, CCAR-P-jrajath94-0124, CCAR-P-jrajath94-0125, CCAR-P-jrajath94-0286, CCAR-P-jrajath94-0289, CCAR-P-jrajath94-0607</sub>

@@ MEMO

| 이름 | 의미 |
|---|---|
| sectioning | 독립 서브태스크 분할 → 동시 실행 → 집계 |
| fan-out / fan-in | 독립 조각 병렬 실행 / 결과 병합 |
| validation gate | 병합 후 코드 · 기준 대조 검사 |
| disagree rule | fan-in에서 결과 충돌을 처리하는 규칙 |
| critique | 점검자 + 기준 + 수정 loop로 품질 편차 대응 |
| triage | 복잡도 판정 → 투입 agent · 호출 수 조정 |
| 동적 분해 | 발견에 따라 서브태스크 생성 · 갱신 |
| 고정 분해 | 사전 확정 절차 = prompt chain |
| 분해 축 | 어디(정보원) vs 무엇(주제 영역) |
| 작업 경계 | 담당 · 비담당 범위<br>(위임 prompt에 명시) |
| Agent tool(구 Task tool) | 한 응답에서 여러 호출 → subagent 병렬 기동 |

<sub>근거: CCAR-F-Udemy03-0003, CCAR-F-Udemy03-0016, CCAR-F-Udemy04-0008, CCAR-F-Udemy04-0054, CCAR-F-Udemy05-0025, CCAR-F-Udemy06-0026, CCAR-P-jrajath94-0123, CCAR-P-jrajath94-0289, CCAR-P-jrajath94-0340, CCAR-P-jrajath94-0402</sub>

@@ CHECK
- [ ] 절차 사전 확정 = chain · 발견 따라 변동 = 동적 분해
- [ ] subagent 정상 + 누락 · 중복 → 분해 · 경계 점검
- [ ] 독립 = 병렬 · 의존 = 순차 · 순차 대화 = 단일 agent
- [ ] 유형별 처리 상이 = routing · 품질 편차 = critique

<sub>근거: CCAR-F-Udemy04-0008, CCAR-F-paullarionov-0004, CCAR-F-preporato-0005, CCAR-P-jrajath94-0066, CCAR-P-jrajath94-0124, CCAR-P-jrajath94-0340</sub>
