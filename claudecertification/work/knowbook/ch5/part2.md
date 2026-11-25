@@ ADD-TO: ### 1-3. Routing: 요청별 맞는 모델로 전송

| 구분 | 내용 |
|---|---|
| 하향 전제 | router의 "쉬움" 판정 = eval로 입증<br>입증된 호출만 더 싼 tier로 이동<br>가정만으로 하향 ✗ |
| batch 작업에 적용 | 야간 대량 문서 → 난이도 분류<br>쉬운 문서 → Fast tier<br>어려운 문서 → 현행 tier 유지 · floor 유지 |
| 규모 효과 | 처리량이 클수록 절감 폭 증가 |
| 운영 부담 | 신뢰할 난이도 분류기 필요<br>오분류 가능 · 트래픽 변하면 재입증<br>모니터링 필요 |

<sub>근거: CCAR-P-jrajath94-0201, CCAR-P-jrajath94-0311, CCAR-P-jrajath94-0434</sub>

@@ ADD-TO: ### 1-4. 사고량 조절: effort, adaptive thinking, extended thinking

| 구분 | 내용 |
|---|---|
| 확인 가능한 작업<br>(test · verifier) | 1차 = low effort 실행<br>실패한 작업만 high effort 재실행<br>같은 통과율에서 비용 약 40% 감소 |
| 출시 전제 | eval 세트에서 low effort 통과율 측정<br>통과율 확인 후 변경 출시 |
| 오답 | 비용 확인 전 모든 작업 effort 상향<br>실패 작업 재실행 할인 기대 → 문서에 없음 |
| ⚠️ 수치 | 약 40% = Anthropic 테스트 수치<br>모델 · workload별 차이 → 현재 문서 확인 |

<sub>근거: CCAR-P-jrajath94-0661</sub>

@@ ADD-TO: ### 1-6. Batch API

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

<sub>근거: CCAR-P-jrajath94-0598, CCAR-P-jrajath94-0608, CCAR-P-jrajath94-0610, CCAR-P-jrajath94-0636, CCAR-P-jrajath94-0665, CCAR-P-jrajath94-0667</sub>

@@ ADD-TO: ### 1-7. Prompt caching

| 구분 | 내용 |
|---|---|
| 적합 prefix | 길고 안정적인 prefix 반복 호출<br>(역할 · 규칙 · few-shot 예시)<br>월 1회 정도 바뀌는 prefix도 적합 |
| 효과 | prefix 한 번 처리 → 여러 호출에서 재사용<br>입력 token 비용 감소 · 모델 동작 불변 |
| 동작 불변 제약 | few-shot 삭제 · 모델 교체 ✗ → 동작 변경<br>한 호출에 메시지 100개 묶기 ✗<br>→ latency 특성 변화 · 교차 오염 위험 |
| 같은 질문 반복 | 큰 prefix가 확실한 이득 → prefix caching<br>답도 동일 · 안정 → 응답 caching이 우위 |

<sub>근거: CCAR-P-jrajath94-0030, CCAR-P-jrajath94-0370</sub>

@@ NEW-SECTION
### 비용 절감 레버와 적용 순서
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

<sub>근거: CCAR-P-jrajath94-0029, CCAR-P-jrajath94-0201, CCAR-P-jrajath94-0433, CCAR-P-jrajath94-0496, CCAR-P-jrajath94-0596</sub>

@@ NEW-SECTION
### 품질 floor 보호와 절감 주장 검증
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

@@ NEW-SECTION
### 완료 작업당 비용 기준 비교 · 검증 · 알림
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

<sub>근거: CCAR-P-jrajath94-0087, CCAR-P-jrajath94-0654, CCAR-P-jrajath94-0660, CCAR-P-jrajath94-0668, CCAR-P-jrajath94-0689, CCAR-P-jrajath94-0690</sub>

@@ NEW-SECTION
### latency 최적화: 단계별 측정과 SLA
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
| 후보 축소 반례 | 승자가 목록 깊은 곳에서 나오면 후보 유지 |
| SLA 삭제 | ✗ (재협상은 가능 · 삭제 불가) |

<sub>근거: CCAR-P-jrajath94-0198, CCAR-P-jrajath94-0199, CCAR-P-jrajath94-0497, CCAR-P-jrajath94-0559</sub>

@@ NEW-SECTION
### 토큰 단가로 비용 추정과 요율 구분
**input · output 각자 요율 → 합산 → 요청량 확장**

| 구분 | 내용 |
|---|---|
| 요청당 비용 | (input token × input 요율<br>+ output token × output 요율)<br>÷ 1,000,000 |
| 예 | Haiku 5.5 · input 3,000 · output 800<br>$0.0003 + $0.0004 = $0.0007<br>(프롬프트 100,000 token 이하 요율) |
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

@@ NEW-SECTION
### 지출 상한: workspace spend limit · session budget
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

@@ NEW-SECTION
### 비용 보고: Admin API와 Cost 보고서
**청구서 대조 = Admin API key로 cost 보고서**

| 구분 | 내용 |
|---|---|
| 데이터 출처 | 플랫폼 cost 보고서<br>앱 응답 token 합산 × 정가 ✗ · usage 필드 재집계 ✗ |
| 보고서 내용 | USD 합계 · workspace별 group |
| 인증 | Admin API key<br>workspace API key<br>→ usage · cost endpoint 실패 |
| bucket | 월간 내역 · 일간 보고 = 일 단위 bucket<br>시간별 · 1분 단위 ✗ |
| 알림 | 1분 bucket 알림 ✗ → Cost API 일 단위만 지원(해설) |
| ⚠️ bucket 범위 | 공식: legacy cost 보고서 = `1d`만<br>신규 Usage and Cost Analytics API<br>= `1m` · `1h` · `1d` |

<sub>근거: CCAR-P-jrajath94-0639, CCAR-P-jrajath94-0654, CCAR-P-jrajath94-0668, CCAR-P-jrajath94-0692</sub>

@@ RULES

| 상황 | 정답 |
|---|---|
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

<sub>근거: CCAR-P-jrajath94-0029, CCAR-P-jrajath94-0030, CCAR-P-jrajath94-0087, CCAR-P-jrajath94-0198, CCAR-P-jrajath94-0199, CCAR-P-jrajath94-0200, CCAR-P-jrajath94-0201, CCAR-P-jrajath94-0311, CCAR-P-jrajath94-0370, CCAR-P-jrajath94-0433, CCAR-P-jrajath94-0434, CCAR-P-jrajath94-0496, CCAR-P-jrajath94-0497, CCAR-P-jrajath94-0559, CCAR-P-jrajath94-0560, CCAR-P-jrajath94-0584, CCAR-P-jrajath94-0586, CCAR-P-jrajath94-0596, CCAR-P-jrajath94-0598, CCAR-P-jrajath94-0608, CCAR-P-jrajath94-0610, CCAR-P-jrajath94-0611, CCAR-P-jrajath94-0612, CCAR-P-jrajath94-0613, CCAR-P-jrajath94-0636, CCAR-P-jrajath94-0639, CCAR-P-jrajath94-0654, CCAR-P-jrajath94-0660, CCAR-P-jrajath94-0661, CCAR-P-jrajath94-0665, CCAR-P-jrajath94-0667, CCAR-P-jrajath94-0668, CCAR-P-jrajath94-0674, CCAR-P-jrajath94-0687, CCAR-P-jrajath94-0689, CCAR-P-jrajath94-0690, CCAR-P-jrajath94-0692, CCAR-P-jrajath94-0694</sub>

@@ TRAPS

| 오답 | 이유 |
|---|---|
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
| batch 제출 후 전체 세트 표준 경로 재실행 | 이중 지불 |
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

<sub>근거: CCAR-P-jrajath94-0029, CCAR-P-jrajath94-0030, CCAR-P-jrajath94-0087, CCAR-P-jrajath94-0198, CCAR-P-jrajath94-0199, CCAR-P-jrajath94-0200, CCAR-P-jrajath94-0201, CCAR-P-jrajath94-0311, CCAR-P-jrajath94-0497, CCAR-P-jrajath94-0559, CCAR-P-jrajath94-0560, CCAR-P-jrajath94-0584, CCAR-P-jrajath94-0586, CCAR-P-jrajath94-0596, CCAR-P-jrajath94-0598, CCAR-P-jrajath94-0608, CCAR-P-jrajath94-0610, CCAR-P-jrajath94-0611, CCAR-P-jrajath94-0612, CCAR-P-jrajath94-0613, CCAR-P-jrajath94-0636, CCAR-P-jrajath94-0639, CCAR-P-jrajath94-0654, CCAR-P-jrajath94-0660, CCAR-P-jrajath94-0661, CCAR-P-jrajath94-0665, CCAR-P-jrajath94-0667, CCAR-P-jrajath94-0668, CCAR-P-jrajath94-0674, CCAR-P-jrajath94-0687, CCAR-P-jrajath94-0689, CCAR-P-jrajath94-0690, CCAR-P-jrajath94-0692, CCAR-P-jrajath94-0694</sub>

@@ MEMO

| 이름 | 의미 |
|---|---|
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

<sub>근거: CCAR-P-jrajath94-0198, CCAR-P-jrajath94-0199, CCAR-P-jrajath94-0200, CCAR-P-jrajath94-0201, CCAR-P-jrajath94-0311, CCAR-P-jrajath94-0496, CCAR-P-jrajath94-0497, CCAR-P-jrajath94-0598, CCAR-P-jrajath94-0608, CCAR-P-jrajath94-0610, CCAR-P-jrajath94-0611, CCAR-P-jrajath94-0613, CCAR-P-jrajath94-0636, CCAR-P-jrajath94-0639, CCAR-P-jrajath94-0654, CCAR-P-jrajath94-0660, CCAR-P-jrajath94-0661, CCAR-P-jrajath94-0667, CCAR-P-jrajath94-0668, CCAR-P-jrajath94-0674, CCAR-P-jrajath94-0687, CCAR-P-jrajath94-0689, CCAR-P-jrajath94-0692, CCAR-P-jrajath94-0694</sub>

@@ CHECK

- [ ] 절감 · 삭감 전 floor 확인 · 후 eval 재실행
- [ ] 비교 기준 = 완료 작업당 비용 · latency = ms per point
- [ ] Batch 한도 = 100,000건 · 256 MB · 결과 29일
- [ ] 지출 상한 = workspace spend limit · session budget · 보고 = Admin API cost 보고서

<sub>근거: CCAR-P-jrajath94-0087, CCAR-P-jrajath94-0198, CCAR-P-jrajath94-0200, CCAR-P-jrajath94-0560, CCAR-P-jrajath94-0598, CCAR-P-jrajath94-0608, CCAR-P-jrajath94-0613, CCAR-P-jrajath94-0639, CCAR-P-jrajath94-0660, CCAR-P-jrajath94-0667, CCAR-P-jrajath94-0687, CCAR-P-jrajath94-0689</sub>
