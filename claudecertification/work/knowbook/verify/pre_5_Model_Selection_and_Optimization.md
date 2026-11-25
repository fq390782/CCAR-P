# 5. Model Selection and Optimization — 반드시 알아야 할 지식
> 시험 비중 17% · 약 5문항 · 근거 문항 28개

> 커버: CCDV-F D5 · CCAR-P D2·D4(일부)

## 1. 핵심 개념

### 1-1. 모델 선택 원칙
**요구 품질 충족하는 가장 효율적 모델 = eval로 선택**

| 구분 | 내용 |
|---|---|
| 목표 | 요구 품질 충족하는 가장 효율적 모델<br>정확도 무한정 추구 ✗ |
| 과잉 품질 | 요구 수준 넘는 품질의 비용 = 낭비 |
| 판단 근거 | 실제 task 대표 sample · 그 task quality bar<br>→ 측정 결과(eval) |
| 하향 시점 | 작은 모델의 quality bar 충족 측정 결과 |
| 품질 동일 | 싼 모델 배포 |
| 입력 변화 | 그 시점에 재평가 |
| 재평가 주기 | eval set으로 주기적 재평가<br>일회성 결정 ✗ |
| 재평가 이유 | 후속 모델 → 같은 가격에 품질 · 속도 개선 사례 다수<br>모델 ID마다 retirement 일정 존재 |

| 오답 | 이유 |
|---|---|
| published benchmark · 더 최신 모델 · 더 큰 모델 | 판단 근거 ✗ |
| 예산 초과 · 호출량 증가 · latency 불만 → 하향 | 검토 시작 이유일 뿐<br>하향 근거 ✗ |
| 큰 모델을 "보험"으로 사용 | 품질 동일 → 싼 모델 배포<br>입력 변화는 그때 재평가로 대응 |
| SDK · quickstart 기본 모델 확인 없이 사용 | 라인업 변경<br>→ 현재 model ID는 문서 확인 |

| 구분 | 내용 |
|---|---|
| 품질 하한<br>(quality floor) | 작업별 허용 최저 품질<br>충족한 가장 낮은 tier = 최저 가격<br>그 위 상위 tier = 지출 |
| 다작업 솔루션 | 작업마다 요구사항 충족하는 가장 작은 모델<br>→ 그 선택도 eval로 검증 |
| 획일 선택 | 하나로 통일 · 전부 최대 · 전부 최신<br>= 적합성 ✗ · 편의 최적화 |
| SLA 기준 | SLA 충족하는 가장 작고 빠른 모델<br>(예: SLA 95%에 97% 달성 → 그 모델) |
| 기준 초과 여유 | 필요 없는 품질 여유 = 순수 비용<br>호출량 클수록 낭비 증가 |
| 측정 없는 절충 | 중간 tier · 무작위 교대 = 선택 기준 ✗<br>무작위 교대 = 평가 방법 ✗ |
| 일부 트래픽만 상위 tier | 측정 없는 이동 = 낭비의 절반<br>tier 변경 중 canary로만 정당 |
| eval 대표성 | 낡은 eval = 격차 은폐<br>새 프로덕션 sample로 재실행 |
| 파라미터 수 | 품질 측정 신호 ✗ |
| "안전을 위해" 항상 최상위 | 측정 없는 비용 · 근거 없는 예산<br>→ 두려움 아닌 eval 기준 선택 |
| 최상위가 정당한 경우 | eval이 최상위만 floor 충족 입증<br>쉬운 클래스의 오류 비용도 큼 |

| 구분 | 내용 |
|---|---|
| 오류 비용 큰 작업 | 심각도 가중한 전용 eval set<br>(예: 놓친 emergency > 오경보) |
| 선택 | 안전 기준 통과하는 가장 싼 모델<br>전체 최저가 모델 ✗ |
| 일반 benchmark | 평균 근접 → 드문 치명적 누락 은폐<br>task 오류 측정 ✗ |
| few-shot 추가 | 특정 실패 모드(놓친 emergency) 해결 증거 ✗ |
| 어려운 입력 분류 생략 | 가장 중요한 입력 작업 포기 ✗ |
| 집계 점수 | 종합 점수 = 카테고리별 실패 은폐 가능<br>확정 전 카테고리별 점수 확인<br>(예: 보안 결함 카테고리) |
| 비용 vs 정확도 | "더 높은 정확도는 항상 가치" ✗<br>하한 위 추가 정확도 = 비용 정당화 필요 |

| 상황 | 대응 |
|---|---|
| 작은 격차 · 오류 고르게 분산<br>(예: 93% vs 95%) | 한 단계 위 tier 이동<br>→ eval 재실행 |
| 한 단계로 부족 | 한 단계씩 더 올림 · 단계마다 입증 |
| 최상위 직행 | 작은 격차에 최상위 가격 ✗<br>격차 큰 경우(예: 15포인트)만 정당 |
| prompt 조치<br>(few-shot · 지시 재작성) | prompt 원인 증거 있을 때만<br>증거 없음 = 추측 → tier 단계가 먼저 |
| eval set | 비교 내내 고정 |

| 구분 | 내용 |
|---|---|
| floor 충족 최저 tier | 해당 작업 최저 가격<br>예: Haiku 5.5 입력 $0.10/1M(≤100K prompt) |
| 최상위 tier 안전 마진 | floor가 요구 안 하는 비용 추가 |
| ⚠️ 라인업 · 가격 | 해설 기준 최상위 = Fable 5.1<br>시점 변동 → 현재 문서 확인 |



![예산·호출량·latency 트리거에서 eval을 거쳐 모델 하향 여부를 정하고 주기적으로 재평가하는 흐름](svg/5-measure-before-downgrade.svg)
*그림: 예산 초과나 latency 불만은 검토 계기일 뿐이며, 작은 모델이 quality bar를 충족한다는 측정 결과가 있어야 내린다.*

<sub>근거: Amey-0019, Amey-0022, Amey-0057, Amey-0072, CCAR-P-Amey-Thakur-0030, CCAR-P-Amey-Thakur-0063, CCAR-P-jrajath94-0052, CCAR-P-jrajath94-0059, CCAR-P-jrajath94-0072, CCAR-P-jrajath94-0132, CCAR-P-jrajath94-0136, CCAR-P-jrajath94-0290, CCAR-P-jrajath94-0343, CCAR-P-jrajath94-0406, CCAR-P-jrajath94-0469, CCAR-P-jrajath94-0532, CCAR-P-jrajath94-0533, CCAR-P-jrajath94-0614, Patrick-0019, Preporato-0012, Udemy-0002, Udemy-0035</sub>

### 1-2. 계층(Opus · Sonnet · Haiku)별 적합 작업
**대량 단순 = Haiku · 균형 = Sonnet · 고난도 = Opus**

| tier | 특징 | 적합 작업 |
|---|---|---|
| Haiku<br>(fast tier) | 가장 빠름 · 가장 저렴 | 대량 단순 작업 · latency 중요 작업<br>classification · extraction · routing<br>언어 판별 · 형식 변환 · autocomplete |
| Sonnet<br>(balanced tier) | 속도 · 지능 균형 최고 | 어느 정도 능력 필요한 작업<br>escalated drafting 등에서 Opus 대체 선택지 |
| Opus<br>(most capable) | 가장 capable<br>→ 오른쪽 작업에서 능력 차이 드러남 | 여러 시스템 맞물린 multi-step 계획<br>상호작용 제약 따지며 계획 수정 · 장시간 agent 작업<br>품질이 사업 가치 좌우하는 분석 |

| 오답 | 이유 |
|---|---|
| 추론 많은 작업을 작은 모델 여러 개로 분할 | 추론 단절 |
| prompt 길게 쓰기 · 다듬기 | 모델 능력 차이 메우기 ✗ |

| 구분 | 내용 |
|---|---|
| ⚠️ 해설 라인업 | Fable 5.2 = Opus 위 계층으로 소개 |
| ⚠️ 시점 변동 | 라인업은 시점마다 상이 |
| ⚠️ 시험 판단 | Opus · Sonnet · Haiku 3계층별 적합 작업 기준 |

<sub>근거: Amey-0020, Amey-0058, Patrick-0011, Preporato-0015, Udemy-0035</sub>

### 1-3. Routing: 요청별 맞는 모델로 전송
**쉬운 대량 → 작은 모델 · 계획 → capable 모델**

| 구분 | 내용 |
|---|---|
| 정의 | Model routing = 각 요청을 처리 가능한 가장 싼 모델로 전송 |
| 단일 모델 문제 | 쉬운 요청 → 비용 과다<br>어려운 요청 → 품질 부족 |
| 패턴 1: 난이도 분리 | 대량 쉬운 작업(분류 · 추출) → Haiku<br>소량 어려운 작업 → Sonnet · Opus<br>(escalated reply · deep analysis) |
| 패턴 2: orchestrator–worker | 계획 수립 orchestrator → capable model<br>좁고 반복적인 worker subtask → 작고 빠른 모델 |

| 오답 | 이유 |
|---|---|
| 가장 어려운 단계(계획 수립)에 가장 약한 모델 배치 | 틀린 구성 ✗<br>계획 수립 = capable model 담당 |

| 구분 | 내용 |
|---|---|
| 클래스별 tier 기준 | 오류 비용이 tier 결정<br>물량 ✗ |
| 다수 쉬운 클래스 | Fast tier<br>(FAQ · 조회 · 안내 · 업무시간 문의) |
| 오류 비용 큰 소수 클래스 | 더 강한 tier + quality floor<br>(배치 망침 · 법적 책임 · 금전 손해 · 발 묶임) |
| quality floor 예 | 답변이 근거 문서(가이드) 인용 의무 |
| 거꾸로 배정 | 쉬운 곳 강한 tier · 위험 클래스 Fast ✗ |
| 전부 최상위 | 안전하나 낭비<br>(쉬운 90%대 트래픽에 최상위 지불) |
| 전부 Fast | 어려운 소수에서 위험 |
| 전부 최상위가 맞는 경우 | 쉬운 클래스 답변도 오류 비용 큼 |
| 전부 Fast가 맞는 경우 | eval이 Fast의 floor 충족 입증 |
| 새 실패 지점 | 라우터<br>오분류된 위험 요청 → 저렴한 tier |

| 구분 | 내용 |
|---|---|
| 하향 전제 | router의 "쉬움" 판정 = eval로 입증<br>입증된 호출만 더 싼 tier로 이동<br>가정만으로 하향 ✗ |
| batch 작업에 적용 | 야간 대량 문서 → 난이도 분류<br>쉬운 문서 → Fast tier<br>어려운 문서 → 현행 tier 유지 · floor 유지 |
| 규모 효과 | 처리량이 클수록 절감 폭 증가 |
| 운영 부담 | 신뢰할 난이도 분류기 필요<br>오분류 가능 · 트래픽 변하면 재입증<br>모니터링 필요 |



![router가 난이도별로 Haiku와 Sonnet/Opus에 요청을 나누는 구조와 orchestrator–worker 구조](svg/5-routing.svg)
*그림: 쉬운 대량 요청은 작은 모델로, 어려운 요청과 계획 단계는 capable 모델로 보내야 한다.*

<sub>근거: CCAR-P-jrajath94-0201, CCAR-P-jrajath94-0290, CCAR-P-jrajath94-0311, CCAR-P-jrajath94-0343, CCAR-P-jrajath94-0406, CCAR-P-jrajath94-0434, CCAR-P-jrajath94-0469, CCAR-P-jrajath94-0532, Patrick-0011, Patrick-0019, Patrick-0037</sub>

### 1-4. 사고량 조절: effort, adaptive thinking, extended thinking
**thinking · effort = workload별 eval 결정**

| 구분 | 내용 |
|---|---|
| Thinking 효과 | multi-step 문제 → 정확도 향상<br>그 외 작업 → output token · latency만 증가 |
| 설정 방침 | 전부 켜기 · 전부 끄기 ✗ → eval 근거로 workload별 결정<br>thinking: 인사 같은 단순 응답 → 축소<br>effort: 일상 작업 → 낮춤 · 어려운 작업 → 높임 |
| 변경 조건 | effort 변경 전 eval로 품질 유지 확인 |
| `output_config.effort` | 모델 변경 없이 응답 전체 token 양 조절<br>(thinking · tool call 포함) |
| Adaptive thinking | 요청마다 생각 여부 · 깊이를 Claude가 결정 |
| effort 범위 | low ~ max로 adaptive thinking의 경향 조정<br>높을수록 더 적극적 · 깊은 사고 |
| 과금 | thinking token = output token 과금 · latency 증가 |
| few-shot | "어떤 형태로 답할지" 결정<br>(형식 · 톤 · 분류 경계) |
| thinking · effort | "얼마나 생각할지" 결정 |
| 권장 예시 수 | 관련성 있고 다양한 3~5개 |

| 오답 | 이유 |
|---|---|
| 형식 고정 단순 분류에 effort max | thinking token 과금 · latency 증가<br>→ 비용 대비 효과 ✗ |
| 예시 많이 넣어 추론 대체 | few-shot = 형식 담당<br>추론 대체 ✗ |

| 구분 | 내용 |
|---|---|
| ⚠️ `budget_tokens` | 사고량 고정하는 예전 extended thinking 방식 |
| ⚠️ 해설 기준 | Claude Opus 4.7 이후 모델에서 미지원 |
| ⚠️ 확인 | 모델 버전별 상이 → 현재 문서 확인 |

| 구분 | 내용 |
|---|---|
| 단계 건너뛰기 실패<br>(다단계 계산 · 적용 순서 오류) | Chain-of-thought(또는 extended thinking)<br>→ 최종 숫자 전에 각 단계 순서대로 출력 |
| 효과 | 단계별 정확도 향상<br>오류 감사 가능 |
| 오답 | 최종 답만 few-shot: 중간 단계 학습 ✗<br>temperature 낮춤: 일관되게 틀림<br>더 큰 context window: 무관 |
| 기준 이미 충족 + 단순 대량 호출 | explicit reasoning 추가 ✗<br>측정된 이득 없이 output token · latency 증가 |
| 기법 선택 | eval 통과하는 가장 단순한 기법<br>reasoning = 더 어려운 작업용 상위 단계 |
| reasoning 정당한 경우 | 어려운 작업 + 검증 가능한 단계<br>+ eval에서 이득 확인 |
| 일부 트래픽 영구 분할 | 이득 평가 없이 비용 고정 ✗<br>결정 날짜 있는 임시 실험만 정당 |
| few-shot → 긴 system prompt 교체 | 작동하는 단계를 미입증 단계로 교체 ✗ |

| 구분 | 내용 |
|---|---|
| 초저지연 작업<br>(예: autocomplete p99 300ms) | extended thinking 끔<br>빠른 모델 + 작은 `max_tokens` + 작업에 맞춘 effort |
| 실패 사례 | thinking 켠 뒤 p99 2.1초 |
| 오답 | thinking budget 증가 → 더 느려짐<br>로딩 spinner → 증상만 가림<br>completion 캐시 → 처음 보는 prefix는 여전히 느림 |
| ⚠️ 해설 "Haiku = extended thinking 없음" | 공식 문서상 Haiku 5.5는 effort 지원<br>모델 세대별 상이 → 문서 확인 |

| 구분 | 내용 |
|---|---|
| 같은 모델 유지 + 소수 요청 floor 미달 | 미달 요청만 effort 상향(예: high)<br>나머지는 기본값(medium) 유지 |
| effort 적용 단위 | 같은 모델에서 요청별 설정<br>모델 가격 tier 이동 ✗ |
| 대부분 요청이 기본 effort로 floor 충족 | 모델 유지 + 단순 요청 low effort<br>미달 요청만 한 단계 위 tier로 escalate |
| 오답 | 전체 트래픽 최상위 이전<br>전체 effort xhigh<br>`budget_tokens` 설정 → Haiku 5.5에서 400 오류 |
| ⚠️ 모델 사양 | Haiku 5.5 high 지원 · 기본 medium<br>해설 기준 · 시점 변동 → 문서 확인 |

| 구분 | 내용 |
|---|---|
| 확인 가능한 작업 | 1차 = low effort 실행<br>실패한 작업만 high effort 재실행<br>같은 통과율에서 비용 약 40% 감소 |
| 출시 전제 | eval 세트에서 low effort 통과율 측정<br>통과율 확인 후 변경 출시 |
| 오답 | 비용 확인 전 모든 작업 effort 상향<br>실패 작업 재실행 할인 기대 → 문서에 없음 |
| ⚠️ 수치 | 약 40% = Anthropic 테스트 수치<br>모델 · workload별 차이 → 현재 문서 확인 |



![workload 유형에 따라 effort와 few-shot을 고르고 eval로 확인하는 decision tree와 effort 스케일](svg/5-effort-thinking.svg)
*그림: thinking과 effort는 일괄 설정하지 않고 workload별로 정하며, effort를 높일수록 output token과 latency가 늘어난다.*

<sub>근거: CCAR-P-jrajath94-0055, CCAR-P-jrajath94-0075, CCAR-P-jrajath94-0143, CCAR-P-jrajath94-0614, CCAR-P-jrajath94-0615, CCAR-P-jrajath94-0616, CCAR-P-jrajath94-0661, Preporato-0012, Preporato-0013, Udemy-0009</sub>

### 1-5. 비용 진단과 절감 수단
**비용 증가 → 요청당 token 진단 먼저 · tier 하향은 마지막**

| 증상 | 조치 |
|---|---|
| 호출량 그대로 · 비용 상승 | 요청 1건당 token 사용량 먼저 확인<br>매 호출 재전송 context 양 확인 |
| 품질 OK · 비용 증가<br>(tier 하향 전 선행 조치 2개) | (1) 불필요 tool output · history trimming<br>→ context 축소<br>(2) 불변 prefix(tools · system prompt) caching |

| 구분 | 내용 |
|---|---|
| latency | 과금 대상 ✗ |
| API key 개수 | 비용 영향 ✗ |
| tier 변경 | eval 근거 있을 때만 |
| `max_tokens` 높임 | 지출 증가 가능 |
| 비용 견적 | 실제 호출 모델로 token counting endpoint 호출<br>tokenizer = 모델 세대마다 다름 |
| model ID 형식 | 같은 모델 → alias · snapshot 어느 형식이든 단가 동일 |
| 절감 수단 | Batch 할인 · prompt caching · 더 작은 모델 선택 |

| 오답 | 이유 |
|---|---|
| `max_tokens` 낮춤 | 비용 절감 ✗<br>작업 단가 그대로 · 답 중간 잘림 |
| 과대 context window 모델 | task에 불필요한 cost · latency 부담<br>정확도 · rate limit · 구조화 출력 신뢰성 향상 ✗ |
| 타사 tokenizer · "글자 수 ÷ 4" 추정 | Claude token 과소 집계<br>(code · 비영어 텍스트에서 두드러짐) |

| 구분 | 내용 |
|---|---|
| ⚠️ 공식 과금 | 실제 사용 token 기준 · window 크기 자체 과금 ✗ |
| ⚠️ 비용 차이 | window보다 모델 tier 단가에서 발생 |

![요청당 token 진단에서 원인별 절감 수단으로 연결되는 매핑과 효과 없는 수단 목록](svg/5-cost-diagnosis.svg)
*그림: 비용이 늘면 요청당 token부터 보고, 원인에 맞춰 trimming·caching·Batch·effort·tier 하향 순으로 고른다.*

<sub>근거: Amey-0021, Amey-0071, Patrick-0029, Patrick-0037, Preporato-0011, Preporato-0012, Udemy-0002</sub>

### 1-6. Batch API
**기다려도 되는 대량 작업만 Batch · interactive ✗**

| 구분 | 내용 |
|---|---|
| Batch 적합 | 대량 · 균일 형태 · 대기 가능 작업 → 가장 저렴<br>(예: 사용자 상호작용 없는 야간 대량 처리) |
| Batch 부적합 | 비동기 → 사람이 기다리는 interactive 작업 ✗ |
| interactive 작업 예 | live chat · escalated reply<br>autocomplete |
| Streaming | interactive 용도<br>비용 절감 ✗ |
| concurrency 높임 | 비용 절감 ✗<br>단가 그대로 |

| 구분 | 내용 |
|---|---|
| 할인 | 표준 API 가격의 50%<br>기다려도 되는 작업에 적용 |
| 적합 사례 | 야간 티켓 · 문서 채점 · 무인 채점<br>사용자가 기다리지 않는 eval 실행 |
| 혼재 workload | 대기 가능 야간 작업 → Message Batches API<br>사용자 대면 호출 → 동기 Messages API 유지 |
| 크기 한도 | batch 하나 = 최대 100,000 request 또는 256 MB<br>먼저 도달하는 한도 적용 |
| 한도 초과 | 한도 안으로 나눠 batch 여러 개 제출<br>모든 결과 세트 수집<br>(150,000건 → 100,000건 미만 batch 2개) |
| 256 | 요청 수 ✗ · batch 크기(MB) 한도 |
| 처리 시간 | 대부분 1시간 내 · 최대 24시간<br>결과 = batch 종료 후 도착<br>작성되는 대로 읽기 ✗ |
| 결과 이용 | 생성 후 29일간 다운로드<br>기간 내 모든 batch 결과 읽기<br>29일 = 결과 기간 · 만료 설정값 ✗ |
| 없는 옵션 | batch용 priority(5분 내 반환) 옵션 ✗<br>문서에 설명 없음 |
| ⚠️ 수치 | 50% · 100,000 · 256 MB · 29일 = 해설 기준<br>시점별 변동 가능 → 현재 문서 확인 |



![사람이 기다리는지에 따라 Batch와 동기 호출/streaming을 고르는 decision tree](svg/5-batch-vs-realtime.svg)
*그림: Batch는 기다려도 되는 대량 작업에만 쓰고, 사람이 기다리는 요청은 동기 호출이나 streaming으로 처리한다.*

<sub>근거: Amey-0056, CCAR-P-jrajath94-0598, CCAR-P-jrajath94-0608, CCAR-P-jrajath94-0610, CCAR-P-jrajath94-0636, CCAR-P-jrajath94-0665, CCAR-P-jrajath94-0667, Patrick-0011, Preporato-0011, Preporato-0015</sub>

### 1-7. Prompt caching
**breakpoint = 공유 prefix 마지막 block · 변하는 값은 뒤**

| 구분 | 내용 |
|---|---|
| `cache_control` 위치 | 개별 content block에 부착<br>요청 최상위 · model parameter ✗ |
| breakpoint 배치 | 공유 영역(preamble) 마지막 block<br>(보통 system prompt 마지막 content block)<br>→ 그 앞 prefix 전체 = cache key |
| 매번 바뀌는 질문 | cache 밖(breakpoint 뒤) |
| breakpoint 상한 | 요청당 최대 4개 |
| 일치 조건 | 정확한 byte 단위 prefix 일치 |
| 렌더링 순서 | tools → system → messages |

| 오답 | 이유 |
|---|---|
| 바뀌는 부분 뒤 breakpoint | 요청마다 다른 cache entry write만<br>read ✗ |

| 무효화 원인 | 증상 | 조치 |
|---|---|---|
| system prompt에 timestamp · UUID 삽입 | cache 전체 무효<br>`cache_read_input_tokens` 계속 0 | 바뀌는 내용을 마지막 breakpoint 뒤로 이동 |
| 요청마다 tool set 변경 | cache 전체 무효<br>`cache_read_input_tokens` 계속 0 | 바뀌는 내용을 마지막 breakpoint 뒤로 이동 |

| TTL | 판단 |
|---|---|
| 5분 ephemeral cache | 몇 분 burst 후 몇 시간 공백 → 적합 |
| 1시간 cache | write 비용 더 비쌈<br>이 패턴에서 추가 hit ✗ |
| permanent cache | 옵션 없음 |

| 구분 | 내용 |
|---|---|
| prefix 순서 | 안정 블록(system · 정책 · 규정집) 앞<br>가변 블록(user context · 질문) 뒤 |
| 가변 블록을 앞에 배치 | prefix 불일치 → 적중률 0에 가까움 |
| 가변 블록에 캐시 | 매 호출 변경 → hit ✗ · anti-pattern<br>write 비용만 과금 |
| 블록 크기 | 결함 원인 = 순서 ✓ · 크기 ✗ |
| 효과 | 동일 정적 prefix 캐싱<br>→ 첫 token까지 시간 · 요청당 비용 동시 감소 |
| 행동 보존 | 내용 · 행동 불변 · 입력 비용만 절감<br>(길고 안정적인 prefix 대상) |
| 오답 | few-shot 삭제 → 행동 · 형식 · 어조 변경<br>예시를 user message로 이동 → 캐시 가능성 파괴<br>요약 교체 → 비용 줄어도 답변 변경 |
| 오답 | 서두 분할 · 요청 시점 요약 · few-shot 블록 이동<br>→ 안정 prefix 캐싱이 지연 · 비용 동시 해결 |
| 오답 | fine-tuning 후 prompt 삭제<br>→ 무겁고 측정 안 된 행동 변경 |

| 구분 | 내용 |
|---|---|
| 이점 큰 workload | 매 턴 같은 system prompt · 도구 정의 재전송<br>(agent loop)<br>여러 사용자가 몇 분 간격으로 같은 대형 문서 질의 |
| 이점 없는 workload | 캐시 가능 최소 길이 미만 단일 요청<br>시작부 timestamp<br>시간 안에 반복 없는 주간 고유 prompt |
| 조건 | 길고 안정적인 prefix가 캐시 수명 안에 반복 |

| 구분 | 내용 |
|---|---|
| 자동 caching | 요청 최상위 `cache_control` 필드 하나<br>→ breakpoint가 마지막 캐시 가능 block으로 자동 이동 |
| 적합 상황 | 턴마다 block 추가되는 멀티턴<br>breakpoint 직접 수정 부담 제거 |
| 명시적 breakpoint 여러 개 | 통제 ↑<br>안정 콘텐츠가 이동할 때마다 수정 필요 |
| ⚠️ 위치 규칙 충돌 | 위 `cache_control` 위치 행(최상위 ✗)과 상충<br>공식 문서는 최상위 필드 = 자동 caching 인정<br>→ 명시 = block 단위 · 자동 = 최상위 구분 |
| 호출 간격 5분 초과<br>(예: 30분마다) | 해당 breakpoint에 `ttl` 1h 지정<br>→ 변하지 않는 tool 목록 유지 |
| 주간 수정되는 문서 | breakpoint 뒤에 배치<br>→ 수정해도 cached prefix miss ✗ |
| 문서를 맨 앞에 배치 | breakpoint 이전 · 위치 변경 → miss |

| 구분 | 내용 |
|---|---|
| 적합 prefix | 길고 안정적인 prefix 반복 호출<br>(역할 · 규칙 · few-shot 예시)<br>월 1회 정도 바뀌는 prefix도 적합 |
| 효과 | prefix 한 번 처리 → 여러 호출에서 재사용<br>입력 token 비용 감소 · 모델 동작 불변 |
| 동작 불변 제약 | few-shot 삭제 · 모델 교체 ✗ → 동작 변경<br>한 호출에 메시지 100개 묶기 ✗<br>→ latency 특성 변화 · 교차 오염 위험 |
| 같은 질문 반복 | 큰 prefix가 확실한 이득 → prefix caching<br>답도 동일 · 안정 → 응답 caching이 우위 |



![올바른 breakpoint 위치와 두 가지 잘못된 위치를 tools·system·messages 띠로 비교한 그림](svg/5-cache-breakpoint.svg)
*그림: breakpoint는 공유 prefix의 마지막 block에 두고, 질문이나 timestamp처럼 바뀌는 값은 그 뒤에 둬야 cache read가 생긴다.*
![burst 요청 뒤 장시간 공백 패턴에서 5분 TTL과 1시간 TTL을 비교한 타임라인](svg/5-cache-ttl.svg)
*그림: 몇 분짜리 burst에는 5분 cache로 충분하고, 1시간 cache는 write만 비싸고 추가 hit가 없다.*

<sub>근거: CCAR-P-Amey-Thakur-0046, CCAR-P-jrajath94-0030, CCAR-P-jrajath94-0057, CCAR-P-jrajath94-0152, CCAR-P-jrajath94-0153, CCAR-P-jrajath94-0370, CCAR-P-jrajath94-0626, CCAR-P-jrajath94-0627, CCAR-P-jrajath94-0628, CCAR-P-preporato-0006, Patrick-0003, Patrick-0008, Patrick-0020, Patrick-0021</sub>

### 1-8. Version pinning과 snapshot
**pin 이점 = 재현성 · 이전 시점 통제**

| 구분 | 내용 |
|---|---|
| Production 방침 | model version pin<br>모델 업데이트 → refusal 등 동작 변화 가능<br>→ 업그레이드 = eval 거친 의도적 변경 |
| pinning과 무관 | 가격 · context window · API 필수 요건 |
| Model ID | 각 ID = 고정 snapshot · weight 불변<br>개선 모델 = 새 ID → 고정 ID에 자동 반영 ✗ |
| pin으로 얻는 것 | 재현성 · audit 설명 용이<br>이전 시점 직접 결정 |
| pin으로 못 얻는 것 | 영속성 · 최신성 |
| 영구 사용 | 보장 ✗<br>ID마다 retirement 일정("이 날짜 전 retire 안 함")<br>→ 후속 모델 검증 · 이전 계획 수립 |
| 같은 ID 동작 변화 | 주변 시스템 업데이트 시 약간 변화 가능<br>(router · safety classifier 등) |

| 오답 | 이유 |
|---|---|
| prompt로 이전 모델처럼 행동 요청 | 계약(보장) ✗ |
| 다른 provider로 failover | 동작 변화 추가 발생 |
| 에러를 빈 응답으로 처리 | 장애 고착 |

| 세대 | snapshot ID | alias ID |
|---|---|---|
| 4.6 세대부터 | 날짜 없는 ID<br>(예: `claude-sonnet-5`) | (해설 언급 없음) |
| 이전 세대 | 날짜 붙은 ID<br>(`claude-haiku-4-5-20251001`) | 날짜 없는 이름<br>(`claude-haiku-4-5`) |

| 구분 | 내용 |
|---|---|
| ⚠️ 출처 | 위 ID 명명 규칙 = 해설 기준 |
| ⚠️ 확인 | 세대마다 상이 → 문서 확인 |

| 구분 | 내용 |
|---|---|
| 감사 대상 워크플로<br>(검증 기간 출력 고정 필요) | 날짜 붙은 snapshot ID pin |
| alias | 해당 minor 버전의 가장 최근 snapshot 지칭<br>고정 ✗ |
| deprecated 사용 탐지 | key별 · 모델별 usage export<br>→ 폐기 일자 전에 호출 식별 |
| 오답 | alias 유지 → 고정된 것처럼 보일 뿐<br>교체 테스트 생략 후 최신 모델로 이전 |
| ⚠️ ID 규칙 | alias · snapshot 형식은 세대별 상이 → 문서 확인 |



![snapshot pin, 새 모델 출시, eval 검증, pin 변경으로 이어지는 업그레이드 루프](svg/5-version-pinning.svg)
*그림: production은 snapshot을 pin하고, 새 ID는 eval을 통과했을 때만 의도적으로 pin을 바꾼다.*

<sub>근거: Amey-0006, Amey-0043, CCAR-P-jrajath94-0675, Udemy-0002</sub>

### 1-9. Sampling(temperature)과 비결정성, 테스트
**temperature 0도 비결정적 → assert · rubric**

| 구분 | 내용 |
|---|---|
| `temperature` | 다음 token 선택 무작위성 조절 |
| 낮음 | 안정적 · 보수적 출력 → 정형 추출 적합 |
| 높음 | 다양 · 창의적 출력 → 아이디어 발상 적합 |
| 오해 | 사실 정확도 향상 ✗<br>latency 조절 파라미터 ✗ |
| `temperature` 0 | 완전 결정적 ✗<br>같은 입력도 호출마다 결과 상이 가능 |
| latency 요인 | 모델 크기 · 입력 · 출력 길이 · 사고량 |

| 방식 | 판정 | 이유 |
|---|---|---|
| golden string 정확 일치 | ✗ | 실패 들쭉날쭉 |
| 구조 · 핵심 사실 assert<br>(schema 유효성 · 필수 필드 · 필수 수치) | ✓ | golden string 대체 |
| rubric 채점 | ✓ | golden string 대체 |
| 통과할 때까지 retry | ✗ | 회귀 은폐 |
| 테스트 삭제 | ✗ | 안전망 소실 |

| 구분 | 내용 |
|---|---|
| ⚠️ 대상 | 해설 기준 Claude Sonnet 5 · Opus 5.5 등 일부 모델 |
| ⚠️ 제약 | `temperature` · `top_p` · `top_k`<br>비기본값 설정 → 에러 |
| ⚠️ 대응 | 출력 방향 = prompt로 조정 |
| ⚠️ 확인 | 모델별 사양 → 문서 확인 |

![temperature 0에서도 비결정적인 출력을 테스트하는 올바른 방법과 오답 경로](svg/5-flaky-test.svg)
*그림: temperature 0도 결정적이지 않으므로 golden string 비교 대신 구조와 핵심 사실을 assert하거나 rubric으로 채점한다.*

<sub>근거: Preporato-0014, Udemy-0005</sub>

### 1-10. Cascade · escalation과 라우터 검증
**escalation 트리거 = 측정된 검사 · 라우터도 eval 대상**

| 구분 | 내용 |
|---|---|
| 유형 기반 routing | 작은 diff → Fast<br>대규모 refactoring → Capable<br>Fast 결과 신뢰도 검사 실패 → Capable escalate |
| 배정 원칙 | 각 유형 = floor 넘는 가장 싼 tier |
| 일관성 기준 | 필요한 것 = floor 일관성<br>tier 일관성 ✗ |
| 필요 요소 | 라우터의 크기 · 복잡도 신호<br>보정된 신뢰도 임계값 |
| 임계값 오보정 | 전부 escalate → 비용 낭비<br>아무것도 안 함 → 품질 하락 |
| 미달 요청만 escalate | 기본 tier 유지<br>floor 미달 요청만 한 단계 위로 |
| round-robin | 유형 아닌 순번으로 배정 ✗ |
| 전부 Capable | 일치하는 작은 diff에 Capable 가격 낭비 |
| 전부 Fast | 어려운 유형에서 floor 위반 |

| 구분 | 내용 |
|---|---|
| escalation 트리거 | 측정된 검사<br>(verifier · quality floor test) |
| 모델 자기 신뢰도 | 보정 안 됨 · prompt injection 가능<br>→ 게이트 ✗ |
| cascade 자체 | 틀린 설계 ✗<br>측정된 트리거 사용 시 좋은 설계 |
| 라우터 오분류 | 어려운 질문 → 저렴한 tier(품질 위험)<br>쉬운 질문 → 비싼 tier(비용 위험) |
| 라우터 검증 | 키워드 목록 포함 모든 라우터 = 자체 eval 필요<br>완벽한 라우터 없음 |

| 상황 | 대응 |
|---|---|
| 빡빡한 latency SLA · cascade p95 초과<br>(예: 20% 호출에 +900ms → p95 2.9초) | 단계 축소 → 하나일 수도 있음<br>SLA 내 floor 충족하는 가장 싼 단일 tier |
| 단일 tier 전환 조건 | cascade 없이 eval 재실행으로 floor 입증<br>비용 상승 가능 = 저가 우선 구조 포기 |
| 세 번째 tier 추가 | hop 증가 → p95 악화 ✗ |
| Fast tier reasoning 심화 | 출력 token · latency 증가 ✗ |
| escalation 줄이려 임계값 상향 | 품질 문제 해결 ✗<br>floor가 희망에 의존 |
| 혼재 트래픽 + 응답시간 목표 | 유형별 eval 통과 후<br>쉬운 유형만 low effort의 빠른 tier |
| 전부 가장 빠른 tier | 어려운 요청 floor 미달 ✗ |

![라우터가 유형별로 Fast와 Capable tier에 보내고 측정된 검사 실패 시에만 escalate하는 cascade 흐름](svg/5-cascade-escalation.svg)
*그림: escalation 트리거는 모델 자기 신뢰도가 아니라 측정된 검사이고, 라우터도 자체 eval 대상이다.*

<sub>근거: CCAR-P-jrajath94-0133, CCAR-P-jrajath94-0135, CCAR-P-jrajath94-0407, CCAR-P-jrajath94-0470, CCAR-P-jrajath94-0616, CCAR-P-jrajath94-0666</sub>

### 1-11. 모델 · tier 변경 검증 절차
**tier 변경 · 버전 교체 = 프로덕션 변경 → 측정 먼저**

| 구분 | 내용 |
|---|---|
| tier 하향 전 필수 2단계 | (1) 고정 holdout에서 regression 테스트<br>(2) 실제 트래픽 일부에 canary 적용 |
| holdout 역할 | floor 입증의 첫 단계<br>통과 = 프로덕션 안전 ✗ |
| canary 역할 | 실제 트래픽에서 floor 모니터링 |
| canary 요건 | floor 지표 실시간 계측<br>이전 구성 보존(rollback 경로) |
| 비용 | 며칠 소요 · 이중 serving 비용 |
| 이전 구성 삭제 | canary 중 ✗<br>성공 후 · 아카이브 후 가능 |
| 오답 | 사용자에게 품질 업그레이드로 공지<br>자기 출력으로 분류기 재학습 |

| 구분 | 내용 |
|---|---|
| 같은 tier 새 버전 출시 | 트래픽 이동 전 regression suite 실행<br>고정 baseline과 비교 |
| 같은 tier ≠ 같은 동작 | 버전 간 drift 존재<br>이름 아닌 버전을 테스트 |
| suite 구성 | 대표 · edge · adversarial 사례 |
| 일정 압박 | 서두른 교체 < 늦은 교체 |
| pin 버전 deprecated 예고 | 지금 대체 버전에 regression suite 실행<br>전환 = 프로덕션 변경으로 계획 |
| shadow deploy | 복사 트래픽 · 사용자 영향 없음<br>→ 이 경우에만 프로덕션 관찰 정당 |
| 오답 | 같은 tier 가정 후 ID 교체<br>모델에게 준비 여부 질문<br>종료일 대기 · 100% 라우팅 후 대시보드 관찰 |

![변경 후보가 holdout regression과 canary를 거쳐 전환 확정 또는 rollback으로 이어지는 검증 절차](svg/5-change-validation.svg)
*그림: tier 하향과 버전 교체는 프로덕션 변경이므로 holdout, canary 순서로 측정한 뒤에만 전환한다.*

<sub>근거: CCAR-P-jrajath94-0134, CCAR-P-jrajath94-0295, CCAR-P-jrajath94-0344</sub>

### 1-12. Prompt caching 경제성: 적중률과 손익분기
**절감 = 안정 prefix + 측정 적중률 > 손익분기**

| 구분 | 내용 |
|---|---|
| 이득 결정 요인 | prefix의 호출 간 안정성<br>측정 적중률 > 손익분기 |
| 이득과 무관 | 호출량 단독 · 모델 tier · 질문 길이<br>prefix가 계속 바뀌면 수만 건도 캐시 대상 ✗ |
| 비용 계산 | 적중 횟수 × read 할인 vs write 할증 비교<br>write 할증만 보고 끄기 ✗ |
| 예시 | prefix 10,000 token · 일 50,000회<br>적중률 60% → 캐싱 이득 |
| 절감 주장 전 | 실제 적중률 측정 → 손익분기와 비교 |
| ⚠️ 가격 | write 1.25배 · read 0.1배 · TTL 5분<br>= 해설 기준(2026년 10월)<br>read 배율 모델별 상이 → 문서 확인 |
| ⚠️ 손익분기 수치 | 해설 4~5% = 해설 자체 예시<br>1.25배 · 0.1배 단순 계산(약 22%)과 달라 보임<br>→ 자체 가격 · prefix 크기로 재계산 |

| 구분 | 내용 |
|---|---|
| prompt 버전 | 버전마다 별도 캐시<br>변경 잦으면 적중률 초기화 |
| prefix 수정 | cache 초기화 · write 비용 재지불<br>(예: 주 1회 스타일 가이드 · 월 1회 법령 개정) |
| 이득 한계 | 수정 사이 적중률 vs 손익분기 비교 |
| 5분 TTL | 같은 prefix가 몇 분 안에 반복 → 적중<br>시간당 1회 호출이면 TTL이 hit 차단 |
| 가변 꼬리 캐시 | 적중률 0 유지 · write 계속 과금 → anti-pattern |
| 캐싱 유지 조건 | 불변 prefix + 손익분기 훌쩍 넘는 적중률(예: 92%) |
| 작은 prefix · 복잡성 | 중단 근거 ✗<br>(3,000 token 작음 · 캐싱 복잡) |

| 상황 | 대응 |
|---|---|
| 적중률이 손익분기 미만<br>(예: 3% vs 5%) | prefix 먼저 고침<br>(안정 블록 앞 · 가변 뒤) → 적중률 재측정 |
| 재측정 후에도 미만 | 캐싱 포기 |
| 고침 vs 포기 | 고침이 먼저 |
| 오답 | TTL 연장 → prefix가 매번 바뀌면 hit ✗<br>가변 token 추가 → 안정 블록을 prefix에서 밀어냄<br>시도 전 포기 |
| TTL이 결함인 경우 | prefix 안정 + 호출이 TTL 바로 바깥에 도착 |
| 낮은 hit 해석 | 캐싱 부적합 ✗<br>prefix 부적합 · 순서가 첫 용의자 |

| 구분 | 내용 |
|---|---|
| prompt caching | 안정 prefix 재사용<br>suffix(질문)는 매번 달라도 됨 |
| response caching | 전체 prompt가 동일해야 적용<br>같은 소수 질문이 트래픽 대부분일 때만 정답 |

![측정 적중률을 손익분기와 비교해 캐싱 유지, prefix 수정 후 재측정, 포기를 정하고 cache_miss_reason으로 원인을 확인하는 흐름](svg/5-cache-economics.svg)
*그림: 캐싱 이득은 측정 적중률로 판단하고, 미만이면 포기 전에 cache_miss_reason으로 가장 이른 분기부터 고친다.*

<sub>근거: CCAR-P-jrajath94-0153, CCAR-P-jrajath94-0154, CCAR-P-jrajath94-0294, CCAR-P-jrajath94-0350, CCAR-P-jrajath94-0413, CCAR-P-jrajath94-0476, CCAR-P-jrajath94-0539</sub>

### 1-13. cache miss 진단: `cache_miss_reason`
**miss 원인 = 응답의 `cache_miss_reason`으로 첫 분기 확인**

| 구분 | 내용 |
|---|---|
| 증상 | 공유 템플릿(도구 목록 등) 수정 후 cache read token 0<br>모델은 그대로 |
| 1단계 | 응답의 `cache_miss_reason` 읽기<br>→ 가장 먼저 변경된 block부터 수정 |
| 보고 범위 | 가장 이른 분기 지점 + 사유 유형만<br>이후 변경은 가려질 수 있음 |
| 수정 순서 | 가장 먼저 분기한 지점 먼저 → 이후 사유 재확인 |
| 수정 확인 | 다음 요청의 cache read token 수 |
| 오답 | cache TTL 1시간 연장<br>→ 변경된 prefix = 어떤 TTL에서도 miss |
| 오답 | 템플릿 전체 재작성 + 한 달 측정<br>→ 가장 작은 수정 ✗ |
| 오답 | usage export에서 사유 찾기<br>→ 사유는 응답 자체에 첨부 |

<sub>근거: CCAR-P-jrajath94-0662, CCAR-P-jrajath94-0664</sub>

### 1-14. 비용 절감 레버와 적용 순서
**큰 비용 항목부터 줄이고 floor 유지 입증**

| 레버 | 적용 조건 | 판단 |
|---|---|---|
| context 축소 | 호출당 context가 비용 지배<br>(10,000 token 중 8,000 = 반복 지시문) | caching보다 먼저<br>작은 context > 할인된 큰 context |
| 중복 제거 후 cache | 반복 지시문 중복 제거<br>안정 블록 → cache prefix | 안정 prefix 전제<br>블록 버전 관리 필요 |
| JIT retrieval | 질문이 문서 일부만 필요<br>(30페이지 · 25,000 token 매 호출 전송) | 관련 섹션만 retrieve<br>과대 context = 첫 절감 대상 |
| 증분 처리<br>(call elimination) | 변경분이 소수<br>(재임베딩 중 밤마다 2%만 변경) | 변경 문서만 처리 · 나머지 재사용<br>변경 감지 비용이 더 크면 전체 재처리 |
| 코드 규칙 | 고정 레이아웃 · 고정 필드 추출 | 모델 호출 skip → token 비용 0<br>같은 입력 = 같은 출력<br>열린 입력만 모델 호출 |

| 구분 | 내용 |
|---|---|
| 지배 항목 확인 | 호출당 비용 내역 분해<br>(context · retrieval · generation)<br>가장 큰 항목 먼저 공략 |
| 조합 계획 예<br>(40% 절감 · 정확도 90% 이상) | 반복 prefix caching<br>쉬운 등급 → 더 작은 모델 · 어려운 사례 유지<br>eval 재실행 → 하한선 유지 입증 |
| JIT retrieval 반례 | 올바른 섹션을 줘도 trace에서 실패<br>→ 더 큰 모델 검토 |
| ⚠️ 출력 길이 제한 | 해설 조합 계획에 출력 길이 단축 포함<br>1-5(`max_tokens` 낮춤 = 절감 ✗)와 상충 가능 |

![호출당 비용 분해에서 지배 항목별 절감 레버를 고르고 적용 후 eval로 floor 유지를 확인하는 decision tree](svg/5-cost-levers.svg)
*그림: 가장 큰 비용 항목부터 맞는 레버를 적용하고, 적용 후 eval을 다시 돌려 floor 유지를 입증한다.*

<sub>근거: CCAR-P-jrajath94-0029, CCAR-P-jrajath94-0201, CCAR-P-jrajath94-0433, CCAR-P-jrajath94-0496, CCAR-P-jrajath94-0596</sub>

### 1-15. 품질 floor 보호와 절감 주장 검증
**floor 미충족이면 삭감 금지 · 유지 입증 후 주장**

| 상황 | 정답 | 이유 |
|---|---|---|
| floor 미충족 + SLA 초과<br>(groundedness 88% < 92%) | 삭감 금지<br>품질 먼저 수정 → 유지된 floor 기준 latency 최적화 | 삭감 = 정확도 point 소모<br>미충족 floor에는 쓸 point 없음 |
| 삭감 + 더 큰 tier 동시 적용 | ✗ | tier 변경이 품질 진단을 뒤섞음 |
| floor 기준 하향 | ✗<br>(실제 요구가 낮을 때만 예외) | 기준 = 요구사항 · 시스템 편의 ✗<br>하향은 최적화가 아닌 항복 |
| 절감 후 eval 재실행 | ✓ | floor 유지 입증 |
| eval 세트 · 표본 축소 | ✗ | 하락 은폐 · 측정 연극<br>비용은 그대로 |
| grounding 검사 제거 | ✗ | floor 지키는 검사 삭제 |
| 입력 truncation으로 token 30% 절감<br>→ 품질 불만 증가 | ✗ | 필요한 context 파괴<br>→ 전후 측정 필요 |
| 저렴한 tier 91% < 임계값 95% | 절감 주장 보류 | 같은 eval 세트에서 임계값 통과해야 성립 |

| 구분 | 내용 |
|---|---|
| 판정 원칙 | 하한선 유지하는 절감만 최적화<br>그 외 = 위장된 품질 삭감 |
| session budget | 지출 제한 수단 · 품질 측정 ✗ |
| 주장 선반영 | 임계값 조정 · eval 세트 재구성 후 재테스트 ✗<br>미통과 tier의 절감액 = 진전 아님 |

<sub>근거: CCAR-P-jrajath94-0029, CCAR-P-jrajath94-0200, CCAR-P-jrajath94-0311, CCAR-P-jrajath94-0560, CCAR-P-jrajath94-0612</sub>

### 1-16. 완료 작업당 비용 기준 비교 · 검증 · 알림
**토큰당 단가 ✗ · 완료 작업당 비용으로 판단**

| 상황 | 정답 | 오답 이유 |
|---|---|---|
| 토큰당 가격 낮은 모델 vs 요청 적게 쓰는 모델 | 작업 하나 완료에 든 모든 요청 가격 합산 후 비교 | 토큰당 정가 비교 ✗<br>요청 많은 모델 = 작업당 비용 ↑ 가능 |
| 정확도 동률 prompt 2개<br>(96.2% vs 96.1%) | 완료 문서당 총비용 비교 → 싼 쪽<br>(input · output · 재시도 · tool 호출) | 0.1점 차이 = 잡음<br>템플릿 token 수 비교 ✗ |
| 동률 확인 절차 | hold-out 세트에서 동률 유지 확인<br>guardrail 지표 점검(latency · 형식 유효성) | 프로덕션 "느낌" 비교 ✗ = 측정 아님 |
| 후보 품질 floor +3점<br>작업당 비용 +25% | 대조군 유지<br>(출시 = floor 초과 AND 작업당 비용 유지 · 하락) | 품질 점수만으로 출시 ✗ |
| 품질 민감 작업 tier 하향<br>자체 테스트 없음 | production 작업 샘플링(실제 트래픽 비중 가중)<br>tier별 점수 vs 지출 도표 | 토큰당 가격만으로 전환 ✗<br>Usage · Cost 합계 = 품질 점수 ✗ |
| 저렴한 모델 이전 후 가치 보고 | 일간 지출 ÷ 완료 작업 수<br>모델 · prompt 버전별 비교 | 월 총지출만 비교 ✗<br>(완료 작업이 지출보다 더 줄 수 있음) |
| 지출 +30% · 완료 작업 동일 · 사전 알림 | 완료 작업당 비용에 알림<br>기준선 이탈 시 조치할 담당자 지정 | token 수 · latency · 사용자별 지출 알림 ✗<br>= 작업 가치 미반영 |

![같은 eval에서 floor 유지를 입증한 뒤 완료 작업당 비용으로 출시를 판단하는 흐름과 floor 우회 오답 목록](svg/5-floor-task-cost.svg)
*그림: 절감은 floor 유지가 입증된 뒤 완료 작업당 비용이 유지되거나 낮아질 때만 출시한다.*

<sub>근거: CCAR-P-jrajath94-0087, CCAR-P-jrajath94-0654, CCAR-P-jrajath94-0660, CCAR-P-jrajath94-0668, CCAR-P-jrajath94-0689, CCAR-P-jrajath94-0690</sub>

### 1-17. latency 최적화: 단계별 측정과 SLA
**point당 ms 큰 단계부터 삭감 · 꼬리 · 완료시간 구분**

| 상황 | 정답 | 이유 |
|---|---|---|
| SLA 초과 · floor 위<br>단계별 latency · 정확도 기여 측정 | ms per point가 가장 큰 단계부터 삭감<br>(thinnest receipt) | 예: rerank 700 ms / 1 point<br>reasoning 450 · verification 75<br>retrieval 67 |
| 가장 큰 · 가장 작은 ms 기준 | ✗ | 원시 ms ≠ receipt<br>최대 ms(reasoning)도 point당 450 ms<br>최소 ms(verification) = 정확성 보호 장치 |
| 삭감 후 | eval 재실행 · floor 감시 | 삭감 = 여유 point 소모 |
| 체감 느림 · SLA = 완료 시간 | streaming 승인 + 실제 삭감 별도 진행 | 첫 token = UX · 완료 = SLA<br>둘은 다른 숫자 |
| streaming만으로 SLA 해결 | ✗ | p95 완료 시간 불변 → SLA 실패 |
| p99 14초 · 중앙값만 개선 | 꼬리 최적화<br>(timeout · 재시도 · 느린 단계) | 대화형 = p95 · p99 목표<br>중앙값 개선은 꼬리 고통 무시 |
| rerank 후보 50개 · 상위 5개가 항상 승 · 1.5초 | 후보 축소(예: 상위 15개) | 단계별 측정이 낭비 노출<br>품질 변화 없이 latency ↓ |

| 구분 | 내용 |
|---|---|
| streaming 예외 | SLA가 time-to-first-token 측정<br>→ streaming이 SLA 이동 |
| 중앙값 예외 | SLA가 중앙값 기준 → 중앙값 개선으로 충분 |
| 후보 축소 반례 | 승자가 목록 깊은 곳에서 나오면 후보 축소 ✗<br>→ 더 많은 후보 rerank가 정답 |
| SLA 삭제 | ✗ (재협상은 가능 · 삭제 불가) |

<sub>근거: CCAR-P-jrajath94-0198, CCAR-P-jrajath94-0199, CCAR-P-jrajath94-0497, CCAR-P-jrajath94-0559</sub>

### 1-18. 토큰 단가로 비용 추정과 요율 구분
**input · output 각자 요율 → 합산 → 요청량 확장**

| 구분 | 내용 |
|---|---|
| 요청당 비용 | (input token × input 요율<br>+ output token × output 요율)<br>÷ 1,000,000 |
| 예 | Haiku 5.5 · input 3,000 · output 800<br>$0.0003 + $0.0004 = $0.0007<br>(프롬프트 100,000 token 미만 요율) |
| 월간 추정 | 요청당 비용 × 요청량 × 일수<br>새 서비스 구축 없이 출시 전 수치 확보 |
| 비용 원장 · 사용량 DB | 요율 계산에 필수 ✗ |
| workspace 지출 한도 | 상한 설정 수단 · 예측 월간 수치 ✗ |

| 요율 | 적용 대상 |
|---|---|
| 기본 요율 | input · output 각각 별도 요율<br>실시간 채팅 = 표준 기본 요율 |
| batch 요율 | 기본 가격보다 50% 낮음<br>24시간 대기 가능한 야간 보고서 |
| cache hit 요율 | 캐시가 실제 반환한 token에만 적용<br>워크로드 전체 요율 ✗ · 무료 ✗(100만 token당 소액) |

| 구분 | 내용 |
|---|---|
| input만 계산 ✗ | output token은 자기 요율로 과금 → 과소 추정 |
| 전체 token에 input 단가 ✗ | output 요율 무시 |
| 모든 워크로드 batch 요율 ✗ | 즉시 답변 필요한 채팅에는 부적합 |
| ⚠️ 단가 · 구간 | Haiku 5.5 요율 · 100,000 token 구간 = 해설 기준<br>가격은 시점별 변동 → 현재 가격표 확인 |

<sub>근거: CCAR-P-jrajath94-0584, CCAR-P-jrajath94-0586, CCAR-P-jrajath94-0596, CCAR-P-jrajath94-0611</sub>

### 1-19. 지출 상한: workspace spend limit · session budget
**상한 = workspace · session 단위 · rate limit ✗**

| 수단 | 단위 | 규칙 |
|---|---|---|
| workspace spend limit | workspace 월간 | 알림 임계값 설정 가능<br>그 workspace로 scope한 key만 한도에 반영<br>팀 · 프로젝트별 예산 = workspace 분리 |
| session budget | session 단위 hard 상한 | session 생성 시 설정 · 청구서 후 설정 ✗<br>상한에서 새 model 요청 중단<br>현재 지출 = session 객체 `usage.list_cost` |
| 코드 내 호출 상한 | 실행당 tool 호출 수 | 폭주 단일 loop를 몇 분 내 중단<br>(해설 추론) |
| rate limit | 모델별 분당 request · input · output token | 월간 지출 상한 ✗<br>높이면 호출 증가 → 지출 증가 |

| 상황 | 정답 |
|---|---|
| 팀별 월간 예산 + 모델별 rate limit | 각 팀 workspace에 월간 spend limit · 알림<br>+ 모델별 rate limit |
| 한 프로젝트 자체 트래픽만 월간 상한 | 전용 workspace 생성<br>key를 그 workspace로 scope<br>→ 그 workspace에 spend limit |
| 조직 하나 · 프로젝트 3개 · 폭주 loop | workspace별 월간 한도 + 알림<br>코드에 실행당 tool 호출 상한 |
| 기다리는 사용자 없는 장기 agent 실행 | session 생성 시 session budget<br>`usage.list_cost`로 지출 확인 |

| 구분 | 내용 |
|---|---|
| spend limit 주기 | 월간 · 분당 지출 한도 ✗ |
| Default Workspace | 해설 = spend limit 설정 불가<br>프로젝트 · 팀 상한 → 별도 workspace |
| ⚠️ Default Workspace | 공식 문서: 직접 API에서는 설정 가능<br>일부 사용량은 미집계 · 차단 안 될 수 있음 |

<sub>근거: CCAR-P-jrajath94-0613, CCAR-P-jrajath94-0674, CCAR-P-jrajath94-0687, CCAR-P-jrajath94-0694</sub>

### 1-20. 비용 보고: Admin API와 Cost 보고서
**청구서 대조 = Admin API key로 cost 보고서**

| 구분 | 내용 |
|---|---|
| 데이터 출처 | 플랫폼 cost 보고서<br>앱 응답 token 합산 × 정가 ✗ · usage 필드 재집계 ✗ |
| 보고서 내용 | USD 합계 · workspace별 group |
| 인증 | Admin API key<br>workspace API key<br>→ usage · cost endpoint 실패 |
| bucket | 월간 내역 · 일간 보고 = 일 단위 bucket<br>시간별 · 1분 단위 ✗ |
| 알림 | 1분 bucket 알림 ✗ → Cost API 일 단위만 지원(해설) |
| ⚠️ bucket 범위 | 공식: legacy cost 보고서 = `1d`만<br>신규 Usage and Cost Analytics API<br>= `1m` · `1h` · `1d` |

![상황별 지출 상한 수단과 Admin API key로 cost 보고서를 조회하는 비용 보고 경로](svg/5-spend-reporting.svg)
*그림: 지출 상한은 workspace와 session 단위로 걸고 rate limit은 상한이 아니며, 청구 대조는 Admin API key의 cost 보고서로 한다.*

<sub>근거: CCAR-P-jrajath94-0639, CCAR-P-jrajath94-0654, CCAR-P-jrajath94-0668, CCAR-P-jrajath94-0692</sub>

## 2. 상황별 정답 판단 규칙

**모델 · routing**

| 상황 | 정답 |
|---|---|
| 대량 단순 분류 · 추출 · routing · 빠듯한 latency | Haiku(fast tier) |
| 상호작용 제약 많은 multi-step 계획 · 마이그레이션 | 가장 capable한 모델(Opus) |
| 큰 모델로 거의 완벽한 정확도 나오는 대량 단순 작업 | 작은 모델의 요구 정확도 충족 여부 평가 |
| 작은 모델 · 큰 모델 정확도 동일 | 작은 모델 배포 |
| 두 모델 중 하나 선택 | 대표 sample · quality bar로 둘 다 측정 |
| 작업별 난이도 상이(쉬운 대량 · 어려운 소량) | Routing: 작업별 tier 분리 |
| Orchestrator · 다수 worker subtask | Orchestrator = capable 모델<br>worker = 작고 빠른 모델(small · fast) |

**비용 · 처리 · 사고량**

| 상황 | 정답 |
|---|---|
| 호출량 그대로 · 비용 급증 | 요청당 token · 재전송 context 확인 |
| 품질 OK · 비용 증가 | context trimming · stable prefix caching<br>(tier 변경보다 먼저) |
| 사용자 상호작용 없는 대량 야간 처리 | Batch API |
| 사용자가 기다리는 interactive 요청 | Batch ✗<br>(stream 또는 동기 호출) |
| 수백 ms 내 응답 필요한 짧은 autocomplete | Haiku · streaming · 작은 `max_tokens` |
| 일상 작업 느림 · token 과다<br>eval로 품질 유지 확인 | 해당 작업만 `output_config.effort` 낮춤 |
| 전체 thinking 켬 → 단순 응답까지 느려짐 | workload별 결정(필요한 곳만 깊은 추론) |
| 분류 작업 · 복잡한 계획 작업 혼재 | 분류 = few-shot · 계획 = effort 높임 |
| 큰 prompt 전송 전 비용 추정 | 같은 모델로 token counting endpoint 호출 |

**cache · version · test**

| 상황 | 정답 |
|---|---|
| 긴 system prompt caching | 마지막 system content block에 `cache_control` |
| 공유 preamble 뒤 매번 다른 질문 | preamble 마지막 block에 breakpoint |
| `cache_read_input_tokens` 항상 0 | prefix 내 변하는 값을 뒤로 이동<br>(timestamp · UUID · tool set) |
| 몇 분 burst 후 몇 시간 요청 없음 | 5분 ephemeral cache |
| 모델 출시 후 production 동작 변화 · 규제 대응 | snapshot pin · 업그레이드는 eval 거쳐 진행 |
| 출력이 매번 달라 테스트 flaky | 구조 · 핵심 사실 assert 또는 rubric 채점 |
| 다수 쉬운 클래스 + 오류 비용 큰 소수 클래스 | 쉬운 클래스 = Fast<br>위험 클래스 = 강한 tier + quality floor |
| 이미 SLA 충족하는 작은 모델 존재 | 그 모델 유지<br>상위 tier = 낭비 |
| floor 소폭 미달 · 오류 고르게 분산 | 한 단계 위 tier + eval 재실행 |
| 놓치면 치명적인 분류 작업 | 심각도 가중 eval<br>→ 안전 기준 통과하는 가장 싼 모델 |
| 종합 점수만 SLA 통과 | 확정 전 카테고리별 점수 확인 |
| cascade escalation 트리거 | 측정된 검사(verifier · floor test) |
| cascade 때문에 p95 SLA 초과 | 단계 축소 · floor 충족하는 단일 tier |
| 쉬운 요청 · 어려운 요청 혼재 + 응답시간 목표 | 유형별 eval 통과 후 쉬운 유형만 low effort 빠른 tier |
| tier 하향 전환 | holdout regression + 실제 트래픽 canary |
| 같은 tier 새 버전 · pin 버전 deprecated 예고 | regression suite 실행 + 고정 baseline 비교<br>→ 그다음 트래픽 이동 |
| 단계 건너뛰는 추론 실패 | Chain-of-thought · extended thinking |
| 초저지연 completion | thinking 끔 · 빠른 모델 · 작은 `max_tokens` |
| 같은 모델 유지 · 소수 요청만 floor 미달 | 해당 요청만 effort 상향 |
| 정적 prefix 대량 반복 + 행동 · 내용 유지 | prompt caching<br>(안정 블록 앞 · 가변 뒤) |
| 멀티턴 + breakpoint 수정 부담 회피 | 최상위 `cache_control` 자동 caching |
| 호출 간격 30분 · 불변 tool 목록 유지 | breakpoint `ttl` 1h<br>가변 문서 = breakpoint 뒤 |
| cache read 0 · 변경 층 불명 | `cache_miss_reason` 읽기 → 첫 분기 수정<br>→ cache read로 확인 |
| 적중률 < 손익분기 | prefix 순서 수정 후 재측정 → 그래도 미만이면 포기 |
| prefix 주기적 수정 | 수정 사이 적중률 vs 손익분기 측정 |
| 전체 prompt 동일 반복 | response caching |
| 감사 대상 · 출력 고정 · deprecated 탐지 | 날짜 snapshot pin<br>+ key별 · 모델별 usage export |
| 반복 4,000 token prefix · 동작 불변 필수 | 안정 prefix에 prompt caching |
| 매일 같은 질문 · 큰 가이드 prefix 재처리 | prefix caching<br>(답도 동일 · 안정이면 응답 caching) |
| context 지배 · floor 유지 · 예산 구속 | context 중복 제거 → caching<br>입증된 쉬운 호출만 routing |
| 질문이 문서 한 섹션만 필요 | 관련 섹션 JIT retrieval |
| 야간 batch 대량 문서 · 비용 절감 | 쉬운 문서 Fast tier routing · floor 유지 |
| 변경 2%뿐인 야간 재임베딩 | 변경 문서만 증분 임베딩 |
| 고정 레이아웃 양식의 고정 필드 | 코드 규칙 · 모델 호출 skip |
| 40% 절감 + 정확도 floor 유지 | caching + 쉬운 등급 downtier + eval 재실행 |
| 정확도 동률 두 prompt | 완료 문서당 총비용 비교<br>hold-out · guardrail 확인 → 싼 쪽 |
| SLA 초과 · floor 위 | ms per point 최대 단계부터 삭감 |
| 체감 느림 · SLA = 완료 시간 | streaming 승인 + 실제 삭감 별도 |
| p99 높음 · 중앙값 양호 | 꼬리(timeout · 재시도 · 느린 단계) 최적화 |
| 후보 50개 rerank · 상위 5개가 항상 승 | rerank 후보 축소 |
| floor 미충족 · SLA 초과 | 삭감 금지 · 품질 먼저 수정 |
| 더 싼 tier가 임계값 미달 | 절감 주장 보류 |
| 확인 가능한 작업 · 기본 effort high | low 1차 → 실패만 high 재실행 · eval 확인 |
| 야간 대량 점수 + 실시간 채팅 혼재 | 야간 = Message Batches<br>채팅 = 동기 Messages API |
| 150,000건 batch 처리 | 100,000건 · 256 MB 이내로 분할 · 29일 내 결과 수집 |
| 비용 비교 · 토큰당 가격 상이 | 완료 작업당 비용 |
| 후보 품질 ↑ · 작업당 비용 ↑ | 출시 보류 · 대조군 유지 |
| 지출 증가 · 완료 작업 동일 · 사전 알림 | 완료 작업당 비용 알림 + 담당자 지정 |
| tier 하향 근거 없음 | 실제 트래픽 가중 production 샘플 · tier별 점수 vs 지출 |
| 출시 전 월간 비용 · 새 서비스 금지 | token 종류별 요율 × 수량 합산 → 요청량 · 일수 확장 |
| 24시간 대기 보고서 + 실시간 채팅 | 보고서 batch 요율 · 채팅 표준 요율 |
| 팀별 월간 예산 + 모델별 rate limit | workspace별 월간 spend limit · 알림<br>+ 모델별 rate limit |
| 한 프로젝트만의 월간 상한 | 전용 workspace · key scope · spend limit |
| 장기 agent 실행 상한 | session 생성 시 session budget |
| 폭주 loop · 프로젝트별 상한 | workspace별 월간 한도 + 실행당 tool 호출 상한 |
| workspace별 비용 · 청구서 대조 | Admin API key로 cost 보고서<br>workspace group · 일 bucket |

![작업 특성에 따라 Routing·Haiku·Opus·Sonnet 후보를 고르고 측정으로 확정하는 decision tree](svg/5-rules-model-tree.svg)
*그림: 작업 특성으로 tier 후보를 고르되, 최종 결정은 대표 sample과 quality bar로 측정해서 내린다.*
![비용·처리 방식·사고량 관련 상황별 정답 방향 매핑](svg/5-rules-cost-tree.svg)
*그림: 비용·latency·사고량 문제는 증상별로 정답 수단이 정해져 있다.*
![caching·version·테스트 관련 상황별 정답 방향 매핑](svg/5-rules-cache-version-tree.svg)
*그림: caching·version·테스트 문제도 증상을 보면 정답 방향이 하나로 좁혀진다.*

<sub>근거: Amey-0006, Amey-0019, Amey-0020, Amey-0021, Amey-0022, Amey-0056, Amey-0057, Amey-0058, CCAR-P-Amey-Thakur-0030, CCAR-P-Amey-Thakur-0046, CCAR-P-Amey-Thakur-0063, CCAR-P-jrajath94-0029, CCAR-P-jrajath94-0030, CCAR-P-jrajath94-0052, CCAR-P-jrajath94-0055, CCAR-P-jrajath94-0057, CCAR-P-jrajath94-0059, CCAR-P-jrajath94-0072, CCAR-P-jrajath94-0075, CCAR-P-jrajath94-0087, CCAR-P-jrajath94-0132, CCAR-P-jrajath94-0133, CCAR-P-jrajath94-0134, CCAR-P-jrajath94-0135, CCAR-P-jrajath94-0136, CCAR-P-jrajath94-0153, CCAR-P-jrajath94-0154, CCAR-P-jrajath94-0198, CCAR-P-jrajath94-0199, CCAR-P-jrajath94-0200, CCAR-P-jrajath94-0201, CCAR-P-jrajath94-0290, CCAR-P-jrajath94-0294, CCAR-P-jrajath94-0295, CCAR-P-jrajath94-0311, CCAR-P-jrajath94-0344, CCAR-P-jrajath94-0350, CCAR-P-jrajath94-0370, CCAR-P-jrajath94-0413, CCAR-P-jrajath94-0433, CCAR-P-jrajath94-0434, CCAR-P-jrajath94-0470, CCAR-P-jrajath94-0476, CCAR-P-jrajath94-0496, CCAR-P-jrajath94-0497, CCAR-P-jrajath94-0539, CCAR-P-jrajath94-0559, CCAR-P-jrajath94-0560, CCAR-P-jrajath94-0584, CCAR-P-jrajath94-0586, CCAR-P-jrajath94-0596, CCAR-P-jrajath94-0598, CCAR-P-jrajath94-0608, CCAR-P-jrajath94-0610, CCAR-P-jrajath94-0611, CCAR-P-jrajath94-0612, CCAR-P-jrajath94-0613, CCAR-P-jrajath94-0615, CCAR-P-jrajath94-0627, CCAR-P-jrajath94-0628, CCAR-P-jrajath94-0636, CCAR-P-jrajath94-0639, CCAR-P-jrajath94-0654, CCAR-P-jrajath94-0660, CCAR-P-jrajath94-0661, CCAR-P-jrajath94-0662, CCAR-P-jrajath94-0664, CCAR-P-jrajath94-0665, CCAR-P-jrajath94-0666, CCAR-P-jrajath94-0667, CCAR-P-jrajath94-0668, CCAR-P-jrajath94-0674, CCAR-P-jrajath94-0675, CCAR-P-jrajath94-0687, CCAR-P-jrajath94-0689, CCAR-P-jrajath94-0690, CCAR-P-jrajath94-0692, CCAR-P-jrajath94-0694, Patrick-0003, Patrick-0008, Patrick-0011, Patrick-0019, Patrick-0020, Patrick-0021, Patrick-0029, Patrick-0037, Preporato-0011, Preporato-0012, Preporato-0013, Preporato-0014, Preporato-0015, Udemy-0002, Udemy-0009, Udemy-0035</sub>

## 3. 자주 나오는 오답 함정

**모델 · routing**

| 오답 | 이유 |
|---|---|
| 모든 작업에 가장 강한 모델<br>(품질 일관성 · 설정 단순화) | 쉬운 작업에 비용 · latency 낭비 |
| 모든 작업에 가장 싼 모델 | 어려운 작업에서 품질 부족 |
| prompt 길게 · 다듬기로 작은 모델 복잡 추론 | prompt로 모델 능력 차이 메우기 ✗ |
| 추론 작업을 작은 모델 여러 개로 분할 | 추론 단절 |
| benchmark 점수 높은 · 최신 · 큰 모델 선택 | 실제 task 측정 근거 아님 |
| 예산 초과 · 호출량 많음 → 작은 모델로 하향 | 검토 시작 계기일 뿐<br>quality bar 충족 여부 측정 확인 |
| 검증 없이 작은 모델 · fast tier로 바로 이동 | eval 확인 단계 생략 |

**비용 · 처리 · 사고량**

| 오답 | 이유 |
|---|---|
| `max_tokens` 낮춰 비용 절감 | 작업 단가 그대로 · 답 잘림 |
| `max_tokens` 높여 잘림 방지 → 비용 문제도 해결 | 지출 증가 가능 |
| thinking budget 늘림 · thinking 전부 켜기 · 전부 끄기 | 일괄 설정 ✗ → workload별 결정 |
| effort max → 분류 품질 향상 | output token 비용 · latency만 증가 |
| few-shot 예시 수십 개 → 깊은 추론 대체 | context 압박 · 예시 표면 패턴 모방 |
| live chat 포함 모든 요청 Batch | Batch = 비동기 → interactive 부적합 |
| streaming · concurrency 높임 → 비용 감소 | 단가 그대로 |
| 큰 context window 모델 = 정확 · rate limit 적음 | 이점 없음 · cost · latency만 증가 |
| 글자 수 ÷ 4 추정 · 타사 tokenizer | 부정확 |
| 일단 전송 후 usage 확인 | 사전 견적 아님 |

**cache · version · test**

| 오답 | 이유 |
|---|---|
| `cache_control`을 요청 최상위 · model parameter에 부착 | content block 단위로 부착 |
| `cache_control`을 모든 block · 첫 block에만 부착 | 공유 영역 마지막 block에 부착 |
| 질문 포함 prompt 끝에 breakpoint | 요청마다 새 entry write만 · read ✗ |
| cache hit 0 = 캐싱 고장 · 모델 미지원 | 대부분 prefix 안에 변하는 값 혼입 |
| 1시간 cache가 항상 우위 | 1시간 = write 더 비쌈 |
| permanent cache 사용 | permanent 옵션 없음 |
| pin 모델 = 더 쌈 | pinning은 가격과 무관<br>pinning 이점 = 재현성 · 이전 시점 직접 결정 |
| pin 모델 = 영구 사용 | 보장 ✗ · ID마다 retirement 일정 |
| pin 모델 = 개선 자동 반영 | 개선 = 새 ID · 고정 ID에 반영 ✗ |
| prompt로 이전 버전처럼 행동 지시 | 동작 보장 ✗ |
| 다른 provider로 failover | 동작 보장 ✗ |
| `temperature` 0 = 완전 결정적 | 0에서도 호출마다 결과 상이 가능 |
| `temperature` 높임 → 사실 정확도 향상 | 사실 정확도 효과 ✗ |
| flaky 테스트를 통과까지 retry | 회귀 은폐 |
| flaky 테스트 삭제 | 안전망 소실 |
| 모델 하나로 통일 · 전부 최대 · 전부 최신 | 적합성 아닌 편의 최적화 |
| 무작위 교대 · 중간 tier 절충 | 측정 없음 · 선택 기준 ✗ |
| 벤치마크 근접 동등 → 최저가 모델 | 평균이 드문 치명적 누락 은폐 |
| "안전을 위해" 항상 최상위 | 측정 없는 비용<br>최상위만 floor 충족 입증 시에만 정당 |
| 작은 격차에 최상위 tier 직행 | 한 단계 위로 충분<br>최상위 가격 낭비 |
| 종합 점수만 보고 확정 | 카테고리별 SLA 실패 은폐 |
| 파라미터 수로 모델 선택 | 측정된 품질 신호 ✗ |
| 쉬운 클래스에 강한 tier · 위험 클래스에 Fast | 거꾸로 배정 |
| cascade 트리거 = 모델 자기 신뢰도 | 보정 안 됨 · prompt injection 가능 |
| 라우터는 완벽하다고 가정 | 오분류 시 품질 · 비용 양방향 위험 |
| latency 초과 시 세 번째 tier 추가 · 임계값 상향 | hop 증가 · floor가 희망에 의존 |
| tier 변경을 사용자에게 품질 업그레이드로 공지 | 비용 조치 → 잘못된 기대 형성 |
| canary 전 이전 tier 구성 삭제 | rollback 경로 파괴 |
| 같은 tier 새 버전 → ID만 교체 | tier 이름 ≠ 동작 보장 · 버전 drift |
| 100% 라우팅 후 대시보드 관찰 | 프로덕션 테스트 · 사용자가 회귀 테스트 |
| 단순 대량 호출에 reasoning 추가 | 측정된 이득 없이 token · latency 증가 |
| autocomplete에 thinking budget 증가<br>또는 spinner | 지연 악화 · 증상만 가림 |
| 단계 건너뛰기에 temperature 낮춤 · 최종 답 few-shot | 일관되게 틀림 · 중간 단계 학습 ✗ |
| `budget_tokens`로 Haiku 5.5 깊이 조절 | 400 오류(해설 기준) |
| 호출량이 많으니 caching 이득 | 이득 = prefix 안정성 + 적중률 > 손익분기 |
| write 1.25배라 caching 끄기 | read 할인 × 적중 횟수와 비교 필요 |
| 변하는 사용자 context를 prefix 앞에 배치 | 적중률 0에 가까움 |
| 적중률 낮을 때 TTL 연장 · 가변 token 추가 | prefix 순서 결함 그대로 |
| cache read 0에서 TTL 1시간 연장 | 변경된 prefix는 어떤 TTL에서도 miss |
| usage export에서 miss 사유 찾기 | 사유는 응답의 `cache_miss_reason` |
| 같은 질문 반복 아닌데 response caching | 전체 prompt 동일 시에만 적용 |
| 예시 삭제 · 요약 교체로 입력 비용 절감 | 행동 · 답변 변경 |
| eval 세트 축소로 평가 비용 절감 | 하락 은폐 · 비용 불변 |
| 모든 처리 가장 싼 모델 · 정확도 유지 기대 | 검증 없는 정확도 → 제약 위반 |
| 평일만 처리 · 문서 절반 삭제 | 서비스 축소 · 비용 효율 개선 ✗ |
| grounding 검사 제거 · 표본 반감 · floor 삭제 | floor 지키는 장치 제거 · 측정 연극 |
| 입력 truncation으로 token 절감 | 필요한 context 파괴 → 품질 불만 |
| 비용 절감에 rerank 추가 · 최상위 tier 일괄 | floor 충족 시 불필요한 비용 증가 |
| 변동 꼬리 포함 전체 대화 cache | prefix 불안정 · write 과금 지속 |
| few-shot 삭제 · 모델 교체로 prefix 비용 절감 | 동작 변경 → 제약 위반 |
| 메시지 100개 한 호출에 묶기 | latency 변화 · 교차 오염 위험 |
| 가장 큰 · 가장 작은 ms 단계 삭감 | 원시 ms ≠ receipt |
| streaming만으로 SLA 해결<br>streaming 거부 · SLA 삭제 | 체감과 완료 시간은 별개 |
| 품질 floor 88% 미달인데 latency 먼저 | 빠른 오답 = 오답 |
| floor 기준을 현 수치로 하향 | 기준은 요구사항 따름 |
| 중앙값 개선으로 만족 | p99 꼬리 고통 방치 |
| rerank 후보 100개로 확대 | 낭비 증가 · 승자는 상위 5개 |
| 실시간 채팅을 Batch로 | 결과는 batch 종료 후 도착 |
| 150,000건 단일 batch · 256건 단위 분할 | 한도 = 100,000건 또는 256 MB |
| batch 만료 29일 설정 | 29일 = 결과 다운로드 기간 |
| batch priority 옵션(5분 반환) | 문서에 설명 없음 |
| Priority Tier 약정으로 가격 절반 | 50% = Batch 사용량 가격 |
| batch 제출 후 전체 세트 표준 경로 재실행 | 이중 지불 (해설 추론) |
| 야간 작업 streaming · rate limit 상향 · 커스텀 큐 | 토큰 단가 불변 · Batches API가 50% 제공 |
| 야간 대량 작업 동기 호출 | 표준 가격 적용 |
| input token만 계산 | output 요율 누락 → 과소 추정 |
| 전체 token에 input 요율 · cache hit 요율 일괄 | cache hit = 반환된 token에만 적용 |
| cache hit = 무료 · 고정 필드 추출에 Opus | 소액 과금 · 코드 규칙이 비용 0 |
| workspace 지출 한도 = 월간 예측 수치 | 한도는 상한 수단 |
| Default Workspace에 팀별 지출 한도 | 해설 기준 설정 불가 → 별도 workspace |
| 청구서 도착 후 session budget 설정 | 생성 시 설정 · 상한에서 요청 중단 |
| rate limit 상향으로 폭주 loop 해결 | 호출 증가 → 지출 증가 |
| workspace 분당 지출 한도 | spend limit = 월간 |
| 토큰당 정가 비교 · 월 총지출만 비교 | 작업당 비용 미반영 |
| 품질 점수만으로 출시 | 작업당 비용 규칙도 충족 필요 |
| Usage · Cost 합계 = 품질 점수 | 지출 ≠ 품질 |
| 총 token · 지표 40개 알림 | 작업 가치 미반영 |
| 앱 응답 token 합산 · workspace key로 cost 조회 | 청구서 대조 = Admin API key · 플랫폼 보고서 |
| Cost API 1분 · 1시간 bucket | 해설 기준 일 단위만 지원<br>⚠️ 공식 신규 API는 `1m` · `1h` · `1d` |
| 이른 절감액 반영 · session budget으로 품질 입증 | budget = 지출 제한 · 품질 측정 ✗ |
| 비용 확인 전 모든 작업 effort 상향 | 비용 증가 · 실패 재실행 할인 문서에 없음 |

<sub>근거: Amey-0006, Amey-0022, Amey-0043, Amey-0056, Amey-0057, Amey-0058, Amey-0071, Amey-0072, CCAR-P-Amey-Thakur-0030, CCAR-P-Amey-Thakur-0046, CCAR-P-Amey-Thakur-0063, CCAR-P-jrajath94-0029, CCAR-P-jrajath94-0030, CCAR-P-jrajath94-0052, CCAR-P-jrajath94-0055, CCAR-P-jrajath94-0057, CCAR-P-jrajath94-0059, CCAR-P-jrajath94-0072, CCAR-P-jrajath94-0075, CCAR-P-jrajath94-0087, CCAR-P-jrajath94-0132, CCAR-P-jrajath94-0134, CCAR-P-jrajath94-0135, CCAR-P-jrajath94-0136, CCAR-P-jrajath94-0143, CCAR-P-jrajath94-0152, CCAR-P-jrajath94-0153, CCAR-P-jrajath94-0154, CCAR-P-jrajath94-0198, CCAR-P-jrajath94-0199, CCAR-P-jrajath94-0200, CCAR-P-jrajath94-0201, CCAR-P-jrajath94-0290, CCAR-P-jrajath94-0294, CCAR-P-jrajath94-0295, CCAR-P-jrajath94-0311, CCAR-P-jrajath94-0344, CCAR-P-jrajath94-0350, CCAR-P-jrajath94-0407, CCAR-P-jrajath94-0413, CCAR-P-jrajath94-0434, CCAR-P-jrajath94-0470, CCAR-P-jrajath94-0476, CCAR-P-jrajath94-0497, CCAR-P-jrajath94-0533, CCAR-P-jrajath94-0559, CCAR-P-jrajath94-0560, CCAR-P-jrajath94-0584, CCAR-P-jrajath94-0586, CCAR-P-jrajath94-0596, CCAR-P-jrajath94-0598, CCAR-P-jrajath94-0608, CCAR-P-jrajath94-0610, CCAR-P-jrajath94-0611, CCAR-P-jrajath94-0612, CCAR-P-jrajath94-0613, CCAR-P-jrajath94-0615, CCAR-P-jrajath94-0626, CCAR-P-jrajath94-0636, CCAR-P-jrajath94-0639, CCAR-P-jrajath94-0654, CCAR-P-jrajath94-0660, CCAR-P-jrajath94-0661, CCAR-P-jrajath94-0662, CCAR-P-jrajath94-0664, CCAR-P-jrajath94-0665, CCAR-P-jrajath94-0667, CCAR-P-jrajath94-0668, CCAR-P-jrajath94-0674, CCAR-P-jrajath94-0675, CCAR-P-jrajath94-0687, CCAR-P-jrajath94-0689, CCAR-P-jrajath94-0690, CCAR-P-jrajath94-0692, CCAR-P-jrajath94-0694, Patrick-0003, Patrick-0008, Patrick-0011, Patrick-0019, Patrick-0020, Patrick-0021, Patrick-0029, Patrick-0037, Preporato-0011, Preporato-0012, Preporato-0013, Preporato-0014, Udemy-0002, Udemy-0005, Udemy-0009, Udemy-0035</sub>

## 4. 암기 목록

| 이름 | 의미 |
|---|---|
| Haiku tier | 가장 빠름 · 가장 저렴<br>classification · extraction<br>routing · autocomplete |
| Sonnet tier | 속도 · 지능 균형 최고 |
| Opus tier | 가장 capable<br>multi-step reasoning · 장시간 agent 작업<br>고난도 분석 |
| ⚠️ "확신 없으면 Opus 5.5부터" | 해설 인용 시점의 안내 · 버전별 상이 |
| `output_config.effort` | 모델 변경 없이 응답 전체 token 사용량 조절<br>(thinking · tool call 포함) |
| effort low ~ max | adaptive thinking의 생각 적극성 · 깊이 조정 |
| ⚠️ `budget_tokens` | 예전 extended thinking의 사고량 고정 방식<br>해설 기준 Opus 4.7 이후 미지원 |
| thinking token | output token 과금 · latency 증가 |
| few-shot 예시 수 | 3~5개 · 관련성 있고 다양한 예시 선택 |
| `max_tokens` | 출력 상한<br>낮춤 → 잘림 · 높임 → 지출 증가 가능<br>단가 변화 ✗ |
| `cache_control` | content block 단위 지정 · 공유 영역 마지막 block |
| breakpoint | 요청당 최대 4개 |
| prefix 렌더링 순서 | tools → system → messages<br>앞부분 변경 → 그 뒤 전부 무효 |
| `cache_read_input_tokens` | cache hit로 읽은 token 수<br>계속 0 → prefix 변경 중 신호 |
| 5분 ephemeral · 1시간 cache | 짧은 burst → 5분<br>1시간 = write 비용 더 비쌈 · permanent 옵션 없음 |
| token counting endpoint | 전송 전 token 수 견적 · 실제 호출 모델로 집계 |
| Batch API | 비동기 · 대기 가능 대량 작업에서 훨씬 저렴함 |
| snapshot · alias | snapshot = weight 고정<br>alias = 최신 snapshot 지칭<br>개선 = 새 ID로 제공 |
| retirement 일정 | 모델 ID별 retire 예정일<br>pinning해도 영구 사용 ✗ |
| `temperature` · `top_p` · `top_k` | sampling 무작위성 조절<br>0이어도 완전 결정적 ✗ |

| 모델 | 단가(per 1M input/output tokens) |
|---|---|
| ⚠️ Haiku 5.5 | $0.10 / $0.50 |
| ⚠️ Sonnet 5.5 | $2 / $10 |
| ⚠️ Opus 5.5 | $4 / $20 |

| 구분 | 내용 |
|---|---|
| ⚠️ 기준 시점 | 2026년 11월 기준 해설 수치 |
| ⚠️ 시험 가이드 | 2026년 7월판 · 이전 라인업(예: Haiku 4.5) 기준 가능<br>→ 시점별 변동 |
| quality floor | 작업별 허용 최저 품질<br>floor 충족한 가장 싼 tier 선택 |
| 결과 가중 eval | 오류 심각도에 가중치 부여한 eval<br>(놓친 emergency > 오경보) |
| cascade | Fast 먼저 → 측정 검사 실패 시 상위 tier로 escalate |
| canary | 실제 트래픽 일부에 새 구성 적용<br>floor 모니터링 · rollback 대비 |
| regression suite | 대표 · edge · adversarial 사례<br>고정 baseline과 비교 |
| shadow deploy | 복사 트래픽으로 새 버전 관찰 · 사용자 영향 없음 |
| Chain-of-thought | 최종 답 전에 각 단계 출력<br>건너뛴 단계 노출 · 감사 가능 |
| 자동 caching | 최상위 `cache_control` 필드 하나<br>breakpoint가 마지막 캐시 가능 block으로 이동 |
| `ttl` 1h | breakpoint 단위 TTL 지정<br>호출 간격 5분 초과 시 사용 |
| `cache_miss_reason` | 응답에 첨부 · 가장 이른 분기 지점 + 사유 유형 |
| 손익분기 적중률 | caching 이득이 되는 최소 hit rate<br>자체 가격 · prefix 크기로 재계산 |
| response caching | 전체 prompt 동일 시 적용<br>prompt caching과 구분 |
| ⚠️ 캐시 단가 | write 1.25배 · read 0.1배 · TTL 5분<br>= 해설 기준(2026년 10월)<br>read 배율 모델별 상이 · 시점 변동 |
| ⚠️ Haiku 5.5 effort | high 지원 · 기본 medium = 해설 기준<br>`budget_tokens` 400 · 시점 변동 |
| floor | 품질 하한선<br>절감 · 삭감의 전제 · 미충족 시 삭감 금지 |
| ms per point<br>(thinnest receipt) | 단계 latency ÷ 정확도 기여 point<br>큰 단계부터 삭감 |
| p95 · p99 | 대화형 latency 목표 · 꼬리 지표 |
| 완료 작업당 비용 | 모델 · prompt 비교 · 출시 규칙 · 알림 기준 |
| call elimination | 변경분만 처리 · 불필요 호출 제거 |
| Message Batches 한도 | 100,000 request 또는 256 MB<br>먼저 도달하는 한도 적용 |
| Batch 시간 · 보관 | 대부분 1시간 내 · 최대 24시간<br>결과 29일 다운로드 |
| Batch 할인 | 표준 API 가격의 50% |
| 요청당 비용 공식 | token × 해당 요율 ÷ 1,000,000<br>input · output 각각 계산 후 합산 |
| workspace spend limit | workspace 월간 상한 · 알림 임계값 |
| session budget | session 생성 시 설정하는 hard 상한 |
| `usage.list_cost` | session 객체의 현재까지 list cost |
| Admin API key | usage · cost endpoint 인증 자격 |
| cost 보고서 | USD 합계 · workspace별 group · 일 bucket |
| low → high effort 재실행 | 같은 통과율 · 비용 약 40% 감소<br>⚠️ Anthropic 테스트 수치 · 시점별 변동 |

<sub>근거: Amey-0020, Amey-0056, CCAR-P-jrajath94-0055, CCAR-P-jrajath94-0059, CCAR-P-jrajath94-0072, CCAR-P-jrajath94-0132, CCAR-P-jrajath94-0133, CCAR-P-jrajath94-0134, CCAR-P-jrajath94-0152, CCAR-P-jrajath94-0153, CCAR-P-jrajath94-0154, CCAR-P-jrajath94-0198, CCAR-P-jrajath94-0199, CCAR-P-jrajath94-0200, CCAR-P-jrajath94-0201, CCAR-P-jrajath94-0294, CCAR-P-jrajath94-0295, CCAR-P-jrajath94-0311, CCAR-P-jrajath94-0470, CCAR-P-jrajath94-0496, CCAR-P-jrajath94-0497, CCAR-P-jrajath94-0598, CCAR-P-jrajath94-0608, CCAR-P-jrajath94-0610, CCAR-P-jrajath94-0611, CCAR-P-jrajath94-0613, CCAR-P-jrajath94-0615, CCAR-P-jrajath94-0627, CCAR-P-jrajath94-0628, CCAR-P-jrajath94-0636, CCAR-P-jrajath94-0639, CCAR-P-jrajath94-0654, CCAR-P-jrajath94-0660, CCAR-P-jrajath94-0661, CCAR-P-jrajath94-0662, CCAR-P-jrajath94-0664, CCAR-P-jrajath94-0667, CCAR-P-jrajath94-0668, CCAR-P-jrajath94-0674, CCAR-P-jrajath94-0687, CCAR-P-jrajath94-0689, CCAR-P-jrajath94-0692, CCAR-P-jrajath94-0694, Patrick-0003, Patrick-0008, Patrick-0020, Patrick-0021, Patrick-0029, Patrick-0037, Preporato-0011, Preporato-0012, Preporato-0013, Preporato-0015, Udemy-0002, Udemy-0005, Udemy-0009, Udemy-0035</sub>

## 5. 시험 직전 체크리스트

- [ ] 모델 선택 = 요구 수준 충족하는 가장 싼 모델
- [ ] 모델 선택 근거 = 실제 task 기준 eval
- [ ] benchmark 점수 · 최신 · 큰 모델 = 근거 ✗
- [ ] Haiku = 대량 · 단순 · 저지연 작업
- [ ] Opus = multi-step · 다중 제약 추론
- [ ] Sonnet = 균형형
- [ ] 난이도 혼재 workload → routing
- [ ] orchestrator = capable 모델 · worker = 작은 모델
- [ ] tier 하향 전 context trimming · prefix caching
- [ ] 비용 증가 → 요청당 token · 재전송 context 먼저 확인
- [ ] `max_tokens` = 비용 절감 수단 ✗(답 잘림)
- [ ] thinking · effort = workload별 결정
- [ ] 단순 응답 → thinking · effort 낮춤
- [ ] thinking token = output 과금
- [ ] 형식 = few-shot(3~5개) · 생각 깊이 = effort
- [ ] Batch = 대기 가능 대량 작업 전용
- [ ] interactive 요청 → Batch ✗
- [ ] `cache_control` = 공유 prefix 마지막 block
- [ ] breakpoint = 요청당 최대 4개
- [ ] cache hit 0 → prefix 내 변하는 값 탐색(timestamp · UUID · tool set)
- [ ] 짧은 burst = 5분 TTL
- [ ] 1시간 cache = write 더 비쌈
- [ ] 사전 token 견적 = 같은 모델 token counting
- [ ] production = snapshot pin
- [ ] 업그레이드 = eval 거친 의도적 변경
- [ ] retirement 일정 확인
- [ ] `temperature` 0도 비결정적
- [ ] 테스트 = 구조 · 핵심 사실 assert 또는 rubric 채점
- [ ] tier = floor 충족하는 가장 싼 tier · 평균 아닌 카테고리 · 결과 가중 eval
- [ ] cascade 트리거 = 측정된 검사 · 자기 신뢰도 ✗
- [ ] tier 하향 = holdout regression + canary 먼저
- [ ] 같은 tier 새 버전 · deprecated 대체 = regression suite + baseline 비교
- [ ] caching 이득 = 안정 prefix + 적중률 > 손익분기 · 낮으면 순서 먼저 수정
- [ ] 절감 · 삭감 전 floor 확인 · 후 eval 재실행
- [ ] 비교 기준 = 완료 작업당 비용 · latency = ms per point
- [ ] Batch 한도 = 100,000건 · 256 MB · 결과 29일
- [ ] 지출 상한 = workspace spend limit · session budget · 보고 = Admin API cost 보고서

<sub>근거: CCAR-P-jrajath94-0059, CCAR-P-jrajath94-0072, CCAR-P-jrajath94-0087, CCAR-P-jrajath94-0134, CCAR-P-jrajath94-0154, CCAR-P-jrajath94-0198, CCAR-P-jrajath94-0200, CCAR-P-jrajath94-0295, CCAR-P-jrajath94-0344, CCAR-P-jrajath94-0470, CCAR-P-jrajath94-0560, CCAR-P-jrajath94-0598, CCAR-P-jrajath94-0608, CCAR-P-jrajath94-0613, CCAR-P-jrajath94-0639, CCAR-P-jrajath94-0660, CCAR-P-jrajath94-0667, CCAR-P-jrajath94-0687, CCAR-P-jrajath94-0689</sub>
