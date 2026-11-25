@@ ADD-TO: ### 1-1. Eval set: 변경은 측정한 뒤 ship
| production-ready 근거 ✓ | 정의된 성공 기준<br>+ 대표 데이터에 대해 측정된 성능<br>(준비 상태 = 측정된 주장) |
| 데모 · 이해관계자 인상 | 일화일 뿐 → 작동 입증 ✗ |
| 엔지니어링 동의 · 팀 투표 | 합의일 뿐 → 작동 입증 ✗ |
| 비용 추정 완료 | 작동 여부와 무관 ✗ |
| 모델 자체 평점 · 신뢰도 점수 | 같은 모델이 자기 출력 채점 → 지표 ✗<br>보정 안 됨 · prompt injection 가능 |
| rubric 없이 모델에게 채점 요청 | 점수 보정 안 됨 · 임계값 없음 ✗ |

<sub>근거: CCAR-P-Amey-Thakur-0020, CCAR-P-Amey-Thakur-0057, CCAR-P-jrajath94-0182, CCAR-P-jrajath94-0307, CCAR-P-jrajath94-0597</sub>

@@ ADD-TO: ### 1-2. Grader 선택: free-form prose에는 LLM-as-judge
| 채점 사다리 ✓ | code 검사 → 보정된 judge<br>→ 사람 표본 점검 (싼 것부터) |
| 사람 전수 채점 | 가장 신뢰 · 비용 약 10배<br>(예: 실행당 $250 vs $25.60) |
| 실행 주기 배분 | 매일 실행 = 사다리<br>release · 분쟁 = 전체 사람 채점 |
| judge 보정 | 사람 label로 1회 보정<br>→ 보정 범위 안에서만 신뢰 |
| 보정 범위 밖 입력 | 사람 확인 필요<br>"밖"의 기준 = 팀이 정의 |
| 보정 안 된 judge | 싸다는 이유로 채택 ✗ → 채점자 아님 |
| 비용 때문에 eval 월 1회로 축소 | 회귀를 몇 주 놓침 ✗ |

<sub>근거: CCAR-P-jrajath94-0188</sub>

@@ NEW-SECTION
### 지표 정의: 모호한 요구를 측정 가능한 기준으로
**형용사는 지표 · 임계값 · 담당자로 바꾼 뒤 구축**

1. 형용사 → 작업 성공 지표로 변환
2. 지표별 임계값(숫자) 설정
3. 안전 · 비용 가드 지표 추가
4. 지표마다 담당자 지정

| 모호한 요구 | 측정 가능한 기준 |
|---|---|
| 더 도움이 됨 | 에스컬레이션 없이 해결 85%<br>+ 안전 · 비용 가드 · 담당자 |
| 몇 초 안에<br>(월 $2,000 · 50,000건) | p95 5초 미만<br>채팅당 비용 $0.04 이하 |
| 좋은 번역 | 사람 평가 adequacy 4/5 이상<br>표본 크기 · 평가자 간 일치도 명시 |
| "사기를 잡는다" | 확인된 사기 recall 95% 이상<br>오탐률 2% 이하<br>held-out 세트에서 측정 |
| 출시 가능한 요약 | 고정 test set rubric 4/5 이상<br>+ 담당 lead 서명 |

| 구분 | 내용 |
|---|---|
| 성공 기준 요건 | 지표 · 임계값 · 지정된 책임자 |
| 임계값 확정 시점 | tuning · 다음 실행 전 |
| 주요 지표 | 목표를 직접 재는 지표 1개<br>(예: held-out 해결률) |
| 지표 여러 개 검토 후 선택 | dashboard 15개 나열 ✗ |
| 임계값만 있는 기준 | 샘플링 방법 · 표본 크기 · 주기 미정<br>→ cherry-picking 위험 |
| 출시 결정용 기준 | 통과 · 실패 결과 + 서명자 |
| 주관 서술 | "잘 읽힘" · "팀이 좋다고 느낌" ✗ |
| 임계값 없는 점수 | 상승해도 출시 근거 ✗ |
| 구축 후 정의 | 목표 도달 여부 판단 불가 ✗ |
| 쉬운 지표 선택 | 평균 응답 길이 등 ✗<br>의미가 아니라 쉬움이 기준 |
| 한계 | 첫 임계값 = 첫 추정<br>baseline은 나중에 측정 |

<sub>근거: CCAR-P-jrajath94-0182, CCAR-P-jrajath94-0364, CCAR-P-jrajath94-0427, CCAR-P-jrajath94-0489, CCAR-P-jrajath94-0553, CCAR-P-jrajath94-0597, CCAR-P-jrajath94-0653</sub>

@@ NEW-SECTION
### 대리 지표(proxy)와 목표 지표
**지표가 녹색이어도 목표가 적색이면 proxy → 교체**

| 상황 | 정답 |
|---|---|
| 유창성 95 녹색<br>작업 성공 60% | 작업 성공 = 주요 지표<br>유창성 = 진단용으로 강등 |
| 유창성 +12%<br>해결률 불변 | held-out 해결률 = 주요 지표<br>임계값 · 담당자 먼저 확정 |
| ROUGE 3개월 고정<br>불만 티켓 3배 | 사람 평가 eval<br>+ 티켓 주제를 지표로 추적 |
| 지어낸 내용 금지 요구<br>ROUGE로 측정 | faithfulness로 교체 |

| 지표 | 재는 것 |
|---|---|
| ROUGE · BLEU | n-gram 중복(표현 유사)<br>유창한 날조도 고득점 |
| faithfulness | 전사본으로 검증 가능한 주장 비율<br>사람 표본 평가 + 자동 claim 검사 |
| 사람 평가 eval | production 요약 샘플링<br>작업 기반 기준(핵심 포인트 · 날조 인용 없음) |
| 티켓 주제 추적 | 사용자 불편 → 팀이 움직일 지표 |

| 오답 | 이유 |
|---|---|
| 녹색 proxy로 계속 출시 | 녹색 proxy는 목표 증명 ✗ |
| proxy 기준 상향(유창성 98) | 목표 아닌 기준 상승 → 60% 그대로 |
| proxy와 목표 지표 평균 | 77.5가 둘 다 가림 |
| 더 높은 ROUGE 목표 | 점수 상승 · 나쁜 요약 → 품질과 분리된 최적화 |
| ROUGE로 eval set 확대 | 틀린 숫자에 확신만 증가 |
| ROUGE → BLEU 교체 | 같은 overlap proxy 계열<br>proxy 교체는 proxy 문제 해결 ✗ |
| 길이 · 지연 시간으로 품질 대체 | 품질 지표 ✗<br>짧은 요약도 날조 가능 |

- 한계: 작업 성공은 측정이 어려움 → 측정 투자 없으면 지표 부패

<sub>근거: CCAR-P-jrajath94-0024, CCAR-P-jrajath94-0085, CCAR-P-jrajath94-0183, CCAR-P-jrajath94-0653</sub>

@@ NEW-SECTION
### 주요 지표 · 가드 지표 · 비즈니스 지표
**주요 지표는 제약 · 위험을 직접 재는 것**

| 요구 · 위험 | 주요 지표 |
|---|---|
| 지어낸 액션 아이템 금지<br>요약에 대한 신뢰 | groundedness<br>(주장 → 원문 추적) |
| 보안 버그를 잡아야 함 | 알려진 취약점 클래스 recall<br>(실제 버그 중 잡은 비율) |
| 사기 탐지 | recall + 오탐률 |
| 채용 순위 · 편향 규제 | groundedness<br>+ 하위 집단별 공정성 |
| 예산이 제약 | 성공한 작업당 비용<br>(비즈니스 지표) |
| 안전 · 보안이 걸림 | 임계값 0 가드 지표 |
| 오답 · 느림 · 청구액 증가<br>(계약 추출 불만 3종) | 필드 단위 정확도 (label 데이터셋)<br>p95 · p99 지연<br>문서당 비용 · 작업당 토큰 |

| 구분 | 내용 |
|---|---|
| 주요 지표 선택 기준 | 제약이 고름<br>안전 → 가드 · 예산 → 비용 · SLA → p95 |
| 정확도 = 항상 주요 지표 | ✗ → 안전 · 예산이 제약이면 다른 지표 |
| 활동 지표 | 프롬프트 수정 횟수 · 응답 길이<br>분당 리뷰 줄 수 · 분당 추출 수<br>→ 불만 해결 여부 증명 ✗ |
| 속도 · 비용 · 가용성 지표 | 품질 · 위험 지표 대체 ✗<br>(uptime · token 비용 · 지연) |

**가드 지표**

| 구분 | 내용 |
|---|---|
| 가드 지표 | 피해를 직접 측정<br>임계값 0 · 위반 1건 → 출시 차단 |
| 정확도로 안전 대체 | ✗ 평균은 거짓말 · 피해는 집중<br>95%가 5% 중증 오배정을 숨길 수 있음 |
| 가드 표현 | 0 또는 정의된 검토 거친 0에 근접 |
| 가드 요건 | 도메인 정의 + label<br>모호한 가드 = 구호 |
| 지연 지표 추가(p99) · 토큰당 비용 추가 | 빠진 것이 안전이면 ✗ |

**비즈니스 · 공정성 · 지연 지표**

| 구분 | 내용 |
|---|---|
| 성공당 비용 지표 | 어려운 건 거부 유인<br>→ 정확도 지표가 균형추 |
| 비용 지표 폐기 | 예산이 제약이면 ✗ |
| 하위 집단 공정성 | 순위 품질을 집단별 측정<br>집계값 하나 ✗ |
| 공정성 · groundedness 비용 | 집단 label → 개인정보 처리 요구<br>groundedness = 주장마다 검증 비용 |
| p50 중앙값 SLA | 느린 5% 은폐 · 사용자는 tail 체감<br>(p50 1.8초 · p95 9초 → 불만) |
| interactive SLA | p95 또는 p99 기준으로 재작성 |
| tail latency | 피크 시간대 느림 → p95 · p99 추적 |

<sub>근거: CCAR-P-jrajath94-0024, CCAR-P-jrajath94-0184, CCAR-P-jrajath94-0185, CCAR-P-jrajath94-0307, CCAR-P-jrajath94-0363, CCAR-P-jrajath94-0371, CCAR-P-jrajath94-0426, CCAR-P-jrajath94-0489, CCAR-P-jrajath94-0552, CCAR-P-preporato-0016</sub>

@@ NEW-SECTION
### 집계 점수 분해: 세그먼트 · 카테고리별 precision/recall
**숫자 하나 뒤의 내역을 열어야 원인이 보임**

| 상황 | 정답 |
|---|---|
| 전체 정확도 97.4%<br>→ 사람 review 축소 요구 | review 축소 조건 = 세그먼트별 목표 정확도<br>목표를 먼저 정함 |
| 위 상황 (측정 단계) | 문서 종류 · 필드별 정확도를<br>신뢰할 건수로 측정 → 검증 세트 확대 |
| 정확도 94% | 나머지 6%의 양상 + 실패당 비용 확인 후 실행 |
| 품질 gate 한 카테고리 오탐 연발<br>→ 보고서 전체 무시 | 그 카테고리만 일시 제외<br>정의 · 실례 · precision/recall eval로 재구축 |
| review 봇: 보안 수용 · style 기각<br>→ 결과 전체 무시 | 카테고리별 precision/recall 측정<br>실례 기반으로 style 기준 축소 · 비활성화 |
| 채용 순위 공정성 | 하위 집단별 측정 (집계 ✗) |

- 원칙: 문제 범위만 분리 → 양호한 부분의 가치 유지
- 집계 평균은 편향 · 집중된 오류를 가림

| 오답 | 이유 |
|---|---|
| 같은 검증 세트로 prompt 재비교<br>exact-match 일률 전환 | 집계 하나로 판단하는 구조 그대로 |
| 주의 문구 달고 수동 무시 요청 | 신뢰 저하 방치 |
| 품질 gate 전체 중지 | 양호한 시그널까지 손실 |
| JSON schema 준수 = 주 신뢰 지표 | 형식과 내용 혼동 |
| 전체 수용률만 추적 | 편향을 평균으로 가림 |
| 전 카테고리 임계값 일괄 상향 | 양호한 카테고리까지 영향 |
| 보안 지적을 위로 이동 | 노이즈 양 그대로 |

<sub>근거: CCAR-F-Udemy01-0022, CCAR-F-Udemy02-0011, CCAR-F-Udemy02-0030, CCAR-P-Amey-Thakur-0073, CCAR-P-jrajath94-0307</sub>

@@ NEW-SECTION
### 통계적 유의성 vs 비즈니스 유의성
**p-value는 효과가 실재한다는 뜻 · 배포는 비용이 결정**

| 구분 | 내용 |
|---|---|
| p-value | 상승이 실재하는지 가르는 관문<br>가치가 있는지는 말하지 않음 |
| 전환에 실제 비용 | 비즈니스 유의성이 결정<br>p-value만으로 배포 ✗ |
| 전환이 무료 | 유의한 상승 → 그대로 배포 |
| "유의하면 무엇이든 배포" | 가격 무시 ✗ |
| "p-value는 의미 없음" | 관문 역할 무시 ✗ |
| 유의한 0.5pt 이득 | 비용 대비 손해 가능 |

| 계산 | 값 |
|---|---|
| 일 추가 성공 건수 | 일 요청 수 × 성공률 상승폭<br>(예: 1M × 0.6pt = 6,000건) |
| 일 추가 비용 | 일 요청 수 × 요청당 추가 비용<br>(예: 1M × $0.004 = $4,000) |
| 손익분기 | 일 추가 비용 ÷ 일 추가 성공 건수<br>(예: 약 $0.67 / 성공) |
| 판정 | 성공 1건 가치 > 손익분기 → 배포<br>성공의 가격을 매겨야 판정 가능 |

<sub>근거: CCAR-P-jrajath94-0192, CCAR-P-jrajath94-0193</sub>

@@ NEW-SECTION
### A/B 테스트 설계: 공정한 비교
**동시 · 무작위 · 일관 할당 · 사전 정의**

| 설계 요소 | 내용 |
|---|---|
| 동시 무작위 분할 | 같은 기간 · 같은 트래픽 구성<br>시간 교란 제거 |
| 일관된 할당 | 사용자는 test 내내 한 arm<br>사용자별 · 고정 할당 규칙 |
| 반증 가능한 가설 | 데이터 보기 전에 명시<br>(예: 성공률 3pt 이상 상승) |
| 주요 지표 · baseline | 사전 정의 |
| 가드 지표 | 주요 지표가 놓치는 퇴보 포착<br>(안전 · 지연 시간) |
| 사전 등록 | 사후 지표 골라 쓰기 방지 |
| 최소 표본 수 | 승자 선언 전 요구<br>주장하는 상승폭에서 계산 |
| 한 번에 한 변경 | 두 변경 동시 배포 → 귀인 불가 |
| 전환에 비용 | 비즈니스 유의성 확인<br>(p-value만 ✗) |

| 잘못된 설계 | 문제 |
|---|---|
| 이번 주 vs 지난주 비교 | 트래픽 구성 · 외부 변화가<br>프롬프트 효과로 위장 |
| 월요일 A · 화요일 B | variant와 요일 교락 |
| page load마다 무작위 배정 | 한 사용자가 두 variant 노출<br>측정 · 경험 모두 손상 |
| 리전 추가 | 시간 교란 해결 ✗ (구조적 결함) |
| offline eval 통과 → live test 생략 | production 분포 변화 미포괄 |
| 하루 400건이면 충분 | 표본 크기는 주장 상승폭이 결정 |
| 스팟 체크 15건 더 · 선호 질문 | 측정 ✗ |
| 스팟 체크 우세로 변경 3개 일괄 배포 | 귀인 불가 · 측정 근거 부족 |

| 상황 | 정답 |
|---|---|
| chunker + prompt 동시 배포<br>지표 상승 → chunker 공으로 | 분리 · 테스트당 1 변경<br>eval set 고정 |
| 분리 테스트의 비용 | arm별 트래픽 · 시간 2배<br>arm 크기를 팀이 결정 |
| 지표 · baseline · 할당 계획 없음<br>("줄일 것 같다") | 반증 가능 가설<br>+ 주요 지표 · 일관 할당 · baseline |
| 가설 확정 + 검정력만 부족 | 이때만 더 긴 테스트 정답 |
| 여러 변경을 배포하고 싶음 | 성공 지표 · 표본 크기 사전 정의<br>한 번에 한 변수 → 유의한 변경만 배포 |
| 일 400 세션 · 1% 상승 · 1주 | 표본 크기 계산 → 판별 불가<br>대안: offline 평가 suite |
| offline suite 구성(서랍) | 대표 · edge · adversarial<br>· malformed · regression |
| offline 한계 | 실제 비즈니스 성과 측정 ✗<br>트래픽 · 기간 증가를 비용으로 계상 |
| ⚠️ 해설: "몇 달 돌려도 흔들림" | 같은 해설이 더 긴 기간도 대안으로 언급<br>→ 과장 가능 · 시험: 표본 계산 선행으로 암기 |

<sub>근거: CCAR-P-Amey-Thakur-0007, CCAR-P-jrajath94-0027, CCAR-P-jrajath94-0191, CCAR-P-jrajath94-0192, CCAR-P-jrajath94-0309, CCAR-P-jrajath94-0367, CCAR-P-jrajath94-0430, CCAR-P-jrajath94-0556, CCAR-P-jrajath94-0659, CCAR-P-preporato-0018</sub>

@@ NEW-SECTION
### 변경 배포 순서: offline eval → shadow → 통제된 노출
**위험한 변경은 영향 범위(blast radius)부터 제한**

1. 회귀 평가 세트 실행 → 깨짐 포착
2. 위험한 변경 → shadow 먼저
3. 통제된 노출 → 미리 정의한 지표로 현재 prompt와 A/B (실제 traffic)
4. 개선 입증 후 전체 배포

| 상황 | 정답 |
|---|---|
| 데모에서 더 좋아 보이는 prompt 변경 | 회귀 eval + 정의된 지표 A/B<br>→ 전체 배포 |
| 위험한 자동 환불 변경 | shadow → 통제된 노출<br>첫날 전체 traffic ✗ (blast radius 최대) |
| 위험 낮은 문구 변경 | 빠른 test 가능 |

| 오답 | 이유 |
|---|---|
| 데모가 대표성 있다며 배포 | 일화 |
| 팀 투표 | 일화 |
| 피드백 배너 + 전체 배포 | 대조군 없는 실험 |
| offline eval 통과 → live test 생략 | production 분포 변화 미포괄 |

<sub>근거: CCAR-P-Amey-Thakur-0007, CCAR-P-jrajath94-0027, CCAR-P-jrajath94-0493</sub>

@@ NEW-SECTION
### Latency 최적화: 단계별 측정 → 지배 단계
**p95를 단계별로 재고 비중 큰 단계부터**

| 구분 | 내용 |
|---|---|
| 측정 | 단계별 p95 · 전체 합계<br>SLA 대비 필요 감축량 계산 |
| 우선순위 | 비중 큰 단계 → 감축량을 채우는 단계<br>의견이 아닌 측정이 지목 |
| 지배 단계 | 단일 단계 과반(예: OCR 56% · vector search 58%)<br>또는 두 단계 합이 대부분(예: 89%) |
| 작은 단계 최적화 | 0.1~0.2초 감축 = 노이즈<br>격차 못 메움 |
| 중간 비중 단계만 | 감축량보다 작으면 격차 해소 ✗ |
| 단계 추가 | p95 증가 → 잘못된 방향<br>(안전 · 필터 · 번역 · 맞춤법 · cache 단계) |
| reasoning 축소 | 품질 · 안전 하한 유지 필요 |
| 지배 단계가 바뀌면 | 우선순위도 변경<br>(예: retrieval이 지배적이면 retrieval) |

<sub>근거: CCAR-P-jrajath94-0299, CCAR-P-jrajath94-0355, CCAR-P-jrajath94-0418, CCAR-P-jrajath94-0481, CCAR-P-jrajath94-0544</sub>

@@ NEW-SECTION
### Latency · 정확도 trade-off: 측정으로 고르고 eval로 검증
**하한을 지키며 비효율 단계부터 · 삭감마다 eval 재실행**

| 구분 | 내용 |
|---|---|
| 판단 도구 | 단계별 ms · 정확도 포인트 표<br>측정 · 추측 ✗ |
| p95가 SLA 초과 | 정확도 1pt당 ms가 최악인 단계 삭감<br>(예: rerank 700ms/1pt<br>→ 2.9→2.2초 · 93→92%) |
| 삭감 후 | 정확도 하한 위인지 계산 + eval 재실행<br>삭감은 여유 포인트 소모 |
| 1회 삭감 | 완전한 수정 아닐 수 있음<br>(2.2초 > SLA 2초) → 남은 격차 추가 탐색 |
| 가장 큰 ms 단계 삭제 | ✗ 원시 ms가 아니라 비율이 결정 |
| verification 같은 보호 단계 삭제 | ✗ 정확도 하한 붕괴<br>(93 − 4 = 89% < 90%) |
| 더 깊은 reasoning 추가 | p95 이미 초과 시 ✗<br>정확도가 하한 아래일 때만 |
| retrieval 결과 cache | 최악 비율 단계가 아님<br>cache 효과 = 안정적 prefix 필요 |

| 선택 | 판단 |
|---|---|
| 독립 단계 | 병렬화 먼저(latency 제약일 때)<br>정확도 불변 · trace로 독립성 확인 |
| 병렬화 반대 논거 "디버깅 어려움" | latency 논거 ✗ · 기준은 독립성 |
| 측정된 이득 없는 단계 | 제거<br>측정 못 하는 복잡성은 짐 |
| 이득 미측정 단계 추가 | 먼저 측정 · 추가 후 측정 ✗ |
| 제거한 단계 | 되돌릴 수 있음<br>문제 보고 시 eval 붙여 재추가 |
| 단계를 응답 뒤로 이동 | 가치 결정 없이 p95에서 숨김 ✗<br>(비동기에 안전 + 가치 증명 시만) |
| 단계 심화(두 번째 모델) | 미측정 단계에 비용 추가 ✗ |
| 느슨한 SLA + 비싼 오류 | latency 예산을 정확도에 지출 |
| 제약에 따라 규칙이 반대 | latency 제약 → 병렬화 · 삭감<br>정확도 제약 → 예산으로 정확도 구매 |

| 요구 · 현재 상태 | 정답 |
|---|---|
| 정확도 90% 이상 · p95 2초 미만<br>대형 모델: 93% · 6초 | 계층 라우팅<br>빠른 모델 먼저 → 신뢰도 낮으면 대형 모델 |
| 라우팅 검증 | 라벨 eval set으로<br>두 기준 동시 성립 확인 후 출시 |
| 전부 작은 모델 | 정확도 하한 위반 ✗ |
| 캐시로 해결 | 요청이 대부분 고유 → hit ≈ 0 ✗ |
| 출력 토큰 한도 절반 | 6초 → 2초 안정적 감소 ✗<br>추론 잘림 · 정확도 위험 |

<sub>근거: CCAR-P-jrajath94-0005, CCAR-P-jrajath94-0163, CCAR-P-jrajath94-0164, CCAR-P-jrajath94-0165</sub>

@@ RULES
| 전체 정확도 97.4% → review 축소 요구 | 세그먼트별 목표 정확도 먼저<br>문서 종류 · 필드별로 측정 |
| 정확도 94% 보고 | 나머지 6% 양상 · 실패당 비용 확인 |
| 품질 gate 한 카테고리만 오탐 | 그 카테고리만 제외<br>정의 · 실례 · precision/recall로 재구축 |
| 카테고리별 수용 편차 큰 review 봇 | 카테고리별 precision/recall<br>noisy 기준만 축소 · 비활성화 |
| "더 도움이 됨" 같은 형용사 요구 | 지표 · 임계값 · 가드 · 담당자로 변환 후 구축 |
| 지표 녹색 · 목표 적색 | proxy → 작업 성공 지표로 교체 |
| 지어낸 내용 금지 요구 | groundedness · faithfulness 주요 지표 |
| 보안 버그 포착 요구 | 취약점 클래스 recall |
| 안전 · 보안이 걸림 | 임계값 0 가드 지표 → 위반 시 출시 차단 |
| 예산이 제약 | 성공한 작업당 비용 = 주요 지표 |
| 채용 등 편향 규제 | 하위 집단별 공정성 측정 |
| interactive SLA 설계 | p95 · p99 기준 (p50 ✗) |
| 유의한 p-value + 전환에 비용 | 손익분기 계산으로 배포 결정 |
| 두 변경이 함께 배포 | 분리 · 테스트당 1 변경 |
| prompt A/B 비교 | 동시 무작위 · 일관 할당<br>사전 등록 지표 + 가드 · 최소 표본 |
| 트래픽이 주장 상승폭 판별 불가 | 표본 계산 → offline suite 대안 |
| 위험한 변경 배포 | shadow → 통제된 노출 |
| p95가 SLA 초과 | 단계별 p95 측정 → 지배 단계 최적화 |
| SLA + 정확도 하한 동시 충족 | ms/정확도 포인트 최악 단계 삭감<br>독립 단계 병렬화 · 삭감마다 eval |
| 측정된 이득 없는 단계 | 제거 (되돌릴 수 있음) |
| 매일 eval 비용 부담 | code → 보정 judge → 사람 표본 사다리 |
| production-ready 선언 | 성공 기준 + 대표 데이터 측정 성능 |

<sub>근거: CCAR-F-Udemy01-0022, CCAR-F-Udemy02-0011, CCAR-F-Udemy02-0030, CCAR-P-Amey-Thakur-0007, CCAR-P-Amey-Thakur-0020, CCAR-P-Amey-Thakur-0057, CCAR-P-Amey-Thakur-0073, CCAR-P-jrajath94-0005, CCAR-P-jrajath94-0024, CCAR-P-jrajath94-0027, CCAR-P-jrajath94-0085, CCAR-P-jrajath94-0163, CCAR-P-jrajath94-0164, CCAR-P-jrajath94-0165, CCAR-P-jrajath94-0182, CCAR-P-jrajath94-0183, CCAR-P-jrajath94-0184, CCAR-P-jrajath94-0185, CCAR-P-jrajath94-0188, CCAR-P-jrajath94-0191, CCAR-P-jrajath94-0192, CCAR-P-jrajath94-0193, CCAR-P-jrajath94-0307, CCAR-P-jrajath94-0309, CCAR-P-jrajath94-0363, CCAR-P-jrajath94-0371, CCAR-P-jrajath94-0426, CCAR-P-jrajath94-0493, CCAR-P-jrajath94-0552</sub>

@@ TRAPS
| 데모 · 팀 합의 · 투표 · 비용 추정으로 준비 판정 | 시스템이 작동한다는 입증 ✗ |
| 전체 정확도 · 전체 수용률 하나로 판단 | 세그먼트 · 카테고리 편향을 평균으로 가림 |
| 녹색 proxy의 임계값 상향 · 평균 · 대체 proxy(BLEU) | 목표 지표 개선 ✗<br>proxy 문제 그대로 |
| 모델 자체 평점 · 신뢰도 점수를 지표로 | 같은 모델이 자기 출력 채점<br>보정 안 됨 · prompt injection 가능 |
| gate 전체 중지 · 주의 문구만 추가 | 양호한 시그널 손실 · 신뢰 저하 방치 |
| schema 준수 = 품질 신뢰 지표 | 형식과 내용 혼동 |
| 정확도 하나로 안전 검증 | 평균이 집중된 피해를 숨김 |
| p-value만으로 배포 | 효과 실재 ≠ 비용 대비 가치 |
| 이번 주 vs 지난주 · 요일별 variant 비교 | 시간 · 트래픽 구성과 교락 |
| 페이지 로드마다 variant 무작위 | 한 사용자가 두 variant 경험 |
| 하루 400건이면 충분하다는 가정 | 표본 크기는 상승폭이 결정 |
| 위험한 변경을 첫날 전체 traffic A/B | blast radius 최대 |
| 가장 큰 ms 단계 · 익숙한 단계 최적화 | 측정된 비율 · 비중이 결정 |
| verification · guard 단계 삭제 | 정확도 하한 붕괴 |
| 전부 작은 모델 · cache · 출력 토큰 절반 | 정확도 하한 위반 · hit ≈ 0 · 추론 잘림 |
| 미측정 단계를 응답 뒤로 이동해 p95 숨김 | 가치 결정 없이 숨기기만 함 |
| 스팟 체크 추가 · 이해관계자 선호 · 일괄 배포 | 측정 · 귀인 ✗ |
| 비용 아끼려 eval 월 1회 · 보정 없는 judge | 회귀를 몇 주 놓침 · 채점자 아님 |

<sub>근거: CCAR-F-Udemy01-0022, CCAR-F-Udemy02-0011, CCAR-F-Udemy02-0030, CCAR-P-Amey-Thakur-0020, CCAR-P-Amey-Thakur-0057, CCAR-P-jrajath94-0005, CCAR-P-jrajath94-0027, CCAR-P-jrajath94-0085, CCAR-P-jrajath94-0163, CCAR-P-jrajath94-0164, CCAR-P-jrajath94-0183, CCAR-P-jrajath94-0185, CCAR-P-jrajath94-0188, CCAR-P-jrajath94-0192, CCAR-P-jrajath94-0193, CCAR-P-jrajath94-0307, CCAR-P-jrajath94-0309, CCAR-P-jrajath94-0430, CCAR-P-jrajath94-0493, CCAR-P-jrajath94-0556, CCAR-P-jrajath94-0597, CCAR-P-jrajath94-0659, CCAR-P-preporato-0018</sub>

@@ MEMO
| ROUGE · BLEU | n-gram 중복 proxy<br>진실성 · 사용자 경험 측정 ✗ |
| faithfulness | 전사본으로 검증 가능한 주장 비율 |
| groundedness | 주장된 각 사실이 원문으로 추적됨 |
| recall | 실제 대상(버그 · 사기) 중 잡은 비율 |
| 가드 지표 | 임계값 0 · 위반 시 출시 차단 |
| 성공한 작업당 비용 | 예산 제약 시 주요 비즈니스 지표 |
| 하위 집단 공정성 | 순위 품질을 집단별로 측정 |
| p50 · p95 · p99 | 중앙값 · tail<br>interactive SLA = p95 · p99 |
| 손익분기 | 일 추가 비용 ÷ 일 추가 성공 건수 |
| blast radius | 변경 노출 범위<br>위험한 변경 → shadow로 먼저 제한 |
| 채점 사다리 | code → 보정된 judge → 사람 표본 |
| ms/정확도 포인트 | 삭감 우선순위 비율<br>최악 단계부터 |
| offline 평가 서랍 | 대표 · edge · adversarial<br>· malformed · regression |

<sub>근거: CCAR-P-jrajath94-0024, CCAR-P-jrajath94-0085, CCAR-P-jrajath94-0163, CCAR-P-jrajath94-0184, CCAR-P-jrajath94-0185, CCAR-P-jrajath94-0188, CCAR-P-jrajath94-0193, CCAR-P-jrajath94-0307, CCAR-P-jrajath94-0309, CCAR-P-jrajath94-0363, CCAR-P-jrajath94-0371, CCAR-P-jrajath94-0426, CCAR-P-jrajath94-0489, CCAR-P-jrajath94-0493, CCAR-P-jrajath94-0552</sub>

@@ CHECK
- [ ] 형용사 요구 → 지표 · 임계값 · 가드 · 담당자
- [ ] 녹색 proxy · 집계 점수 → 목표 · 세그먼트별 재측정
- [ ] A/B → 동시 · 무작위 · 일관 할당 · 변경 1개
- [ ] p95 초과 → 단계별 측정 → 지배 단계부터

<sub>근거: CCAR-F-Udemy01-0022, CCAR-P-jrajath94-0163, CCAR-P-jrajath94-0182, CCAR-P-jrajath94-0183, CCAR-P-jrajath94-0191, CCAR-P-jrajath94-0299, CCAR-P-jrajath94-0430, CCAR-P-jrajath94-0556</sub>
