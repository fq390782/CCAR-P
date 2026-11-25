@@ ADD-TO: ### 1-1. 모델 선택 원칙

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

<sub>근거: CCAR-P-Amey-Thakur-0030, CCAR-P-Amey-Thakur-0063, CCAR-P-jrajath94-0052, CCAR-P-jrajath94-0059, CCAR-P-jrajath94-0072, CCAR-P-jrajath94-0132, CCAR-P-jrajath94-0136, CCAR-P-jrajath94-0533, CCAR-P-jrajath94-0614</sub>

@@ ADD-TO: ### 1-3. Routing: 요청별 맞는 모델로 전송

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

<sub>근거: CCAR-P-jrajath94-0290, CCAR-P-jrajath94-0343, CCAR-P-jrajath94-0406, CCAR-P-jrajath94-0469, CCAR-P-jrajath94-0532</sub>

@@ NEW-SECTION
### Cascade · escalation과 라우터 검증
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

<sub>근거: CCAR-P-jrajath94-0133, CCAR-P-jrajath94-0135, CCAR-P-jrajath94-0407, CCAR-P-jrajath94-0470, CCAR-P-jrajath94-0616, CCAR-P-jrajath94-0666</sub>

@@ NEW-SECTION
### 모델 · tier 변경 검증 절차
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

<sub>근거: CCAR-P-jrajath94-0134, CCAR-P-jrajath94-0295, CCAR-P-jrajath94-0344</sub>

@@ ADD-TO: ### 1-4. 사고량 조절: effort, adaptive thinking, extended thinking

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

<sub>근거: CCAR-P-jrajath94-0055, CCAR-P-jrajath94-0075, CCAR-P-jrajath94-0143, CCAR-P-jrajath94-0614, CCAR-P-jrajath94-0615, CCAR-P-jrajath94-0616</sub>

@@ ADD-TO: ### 1-7. Prompt caching

| 구분 | 내용 |
|---|---|
| prefix 순서 | 안정 블록(system · 정책 · 규정집) 앞<br>가변 블록(user context · 질문) 뒤 |
| 가변 블록을 앞에 배치 | prefix 불일치 → 적중률 0에 가까움 |
| 가변 블록에 캐시 | 매 호출 변경 → hit ✗ · anti-pattern<br>write 비용만 과금 |
| 블록 크기 | 결함 원인 = 순서 · 크기 ✗ |
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

<sub>근거: CCAR-P-Amey-Thakur-0046, CCAR-P-jrajath94-0057, CCAR-P-jrajath94-0152, CCAR-P-jrajath94-0626, CCAR-P-jrajath94-0627, CCAR-P-jrajath94-0628, CCAR-P-preporato-0006</sub>

@@ NEW-SECTION
### Prompt caching 경제성: 적중률과 손익분기
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

<sub>근거: CCAR-P-jrajath94-0153, CCAR-P-jrajath94-0154, CCAR-P-jrajath94-0294, CCAR-P-jrajath94-0350, CCAR-P-jrajath94-0413, CCAR-P-jrajath94-0476, CCAR-P-jrajath94-0539</sub>

@@ NEW-SECTION
### cache miss 진단: `cache_miss_reason`
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

@@ ADD-TO: ### 1-8. Version pinning과 snapshot

| 구분 | 내용 |
|---|---|
| 감사 대상 워크플로<br>(검증 기간 출력 고정 필요) | 날짜 붙은 snapshot ID pin |
| alias | 해당 minor 버전의 가장 최근 snapshot 지칭<br>고정 ✗ |
| deprecated 사용 탐지 | key별 · 모델별 usage export<br>→ 폐기 일자 전에 호출 식별 |
| 오답 | alias 유지 → 고정된 것처럼 보일 뿐<br>교체 테스트 생략 후 최신 모델로 이전 |
| ⚠️ ID 규칙 | alias · snapshot 형식은 세대별 상이 → 문서 확인 |

<sub>근거: CCAR-P-jrajath94-0675</sub>

@@ RULES
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

<sub>근거: CCAR-P-Amey-Thakur-0030, CCAR-P-Amey-Thakur-0046, CCAR-P-Amey-Thakur-0063, CCAR-P-jrajath94-0052, CCAR-P-jrajath94-0055, CCAR-P-jrajath94-0057, CCAR-P-jrajath94-0059, CCAR-P-jrajath94-0072, CCAR-P-jrajath94-0075, CCAR-P-jrajath94-0132, CCAR-P-jrajath94-0133, CCAR-P-jrajath94-0134, CCAR-P-jrajath94-0135, CCAR-P-jrajath94-0136, CCAR-P-jrajath94-0153, CCAR-P-jrajath94-0154, CCAR-P-jrajath94-0290, CCAR-P-jrajath94-0295, CCAR-P-jrajath94-0344, CCAR-P-jrajath94-0470, CCAR-P-jrajath94-0615, CCAR-P-jrajath94-0627, CCAR-P-jrajath94-0628, CCAR-P-jrajath94-0662, CCAR-P-jrajath94-0664, CCAR-P-jrajath94-0666, CCAR-P-jrajath94-0675</sub>

@@ TRAPS
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

<sub>근거: CCAR-P-Amey-Thakur-0030, CCAR-P-Amey-Thakur-0046, CCAR-P-Amey-Thakur-0063, CCAR-P-jrajath94-0052, CCAR-P-jrajath94-0055, CCAR-P-jrajath94-0057, CCAR-P-jrajath94-0059, CCAR-P-jrajath94-0072, CCAR-P-jrajath94-0075, CCAR-P-jrajath94-0132, CCAR-P-jrajath94-0134, CCAR-P-jrajath94-0135, CCAR-P-jrajath94-0136, CCAR-P-jrajath94-0143, CCAR-P-jrajath94-0153, CCAR-P-jrajath94-0154, CCAR-P-jrajath94-0290, CCAR-P-jrajath94-0294, CCAR-P-jrajath94-0295, CCAR-P-jrajath94-0344, CCAR-P-jrajath94-0407, CCAR-P-jrajath94-0413, CCAR-P-jrajath94-0470, CCAR-P-jrajath94-0476, CCAR-P-jrajath94-0533, CCAR-P-jrajath94-0615, CCAR-P-jrajath94-0626, CCAR-P-jrajath94-0662, CCAR-P-jrajath94-0664, CCAR-P-jrajath94-0675</sub>

@@ MEMO
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

<sub>근거: CCAR-P-jrajath94-0055, CCAR-P-jrajath94-0059, CCAR-P-jrajath94-0072, CCAR-P-jrajath94-0132, CCAR-P-jrajath94-0133, CCAR-P-jrajath94-0134, CCAR-P-jrajath94-0152, CCAR-P-jrajath94-0153, CCAR-P-jrajath94-0154, CCAR-P-jrajath94-0294, CCAR-P-jrajath94-0295, CCAR-P-jrajath94-0615, CCAR-P-jrajath94-0627, CCAR-P-jrajath94-0628, CCAR-P-jrajath94-0662, CCAR-P-jrajath94-0664</sub>

@@ CHECK
- [ ] tier = floor 충족하는 가장 싼 tier · 평균 아닌 카테고리 · 결과 가중 eval
- [ ] cascade 트리거 = 측정된 검사 · 자기 신뢰도 ✗
- [ ] tier 변경 · 버전 교체 = regression suite + canary 먼저
- [ ] caching 이득 = 안정 prefix + 적중률 > 손익분기 · 낮으면 순서 먼저 수정

<sub>근거: CCAR-P-jrajath94-0059, CCAR-P-jrajath94-0072, CCAR-P-jrajath94-0134, CCAR-P-jrajath94-0154, CCAR-P-jrajath94-0295, CCAR-P-jrajath94-0470</sub>
