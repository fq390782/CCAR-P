@@ ADD-TO: ### 1-1. Eval set: 변경은 측정한 뒤 ship

| 상황 | 정답 방향 |
|---|---|
| 대량 batch 앞두고 pilot에서 결함 발견<br>(섹션 누락 · 판정 불일치 · 근거란 누락) | prompt 템플릿화<br>대표 eval set · 명확한 기준으로 개선·재평가<br>→ 동기 dry run 성공 후 전체 투입 |
| 규모 확대 판단 | 품질 측정 수단 준비가 전제<br>결함은 건수만큼 복제 |
| 전체 batch 먼저 → 불량 행만 재전송 ✗ | 비동기 처리(최대 24시간)<br>→ 수정 · 재처리 사이클 길어짐 |
| Claude가 쓴 prompt를 그대로 batch ✗<br>(prompt 개선 기능 1회 실행 포함) | 기준 · 테스트 세트 불변 = 검증 없음 |
| schema 엄격화 · tool 사용 강제 | 형식만 보장<br>누락 · 출처 품질은 못 잡음 ✗ |

| 구분 | 내용 |
|---|---|
| 보고에 쓴 example로 prompt tuning | eval set이 개발에 유출<br>→ 점수 부풀림(test 98% · production 84%) |
| 유출 해결 | 별도 개발 세트로 tuning<br>production 반영 held-out으로 보고 |
| 같은 종류 example 몇 개 추가 ✗ | 같은 유출 그대로 |
| 모델 상향 · production 트래픽 걸러내기 ✗ | 측정 문제는 그대로 |
| tuning · 학습에 쓴 data로 측정 | 점수 = 암기 측정 · 일반화 ✗<br>→ 쓰지 않은 대표 held-out 필요 |
| 높은 점수(예: 99%)의 신뢰 근거 | held-out 세트<br>+ judge를 사람 label로 calibration |
| held-out 구성 | production 반영<br>(edge · adversarial case 포함) |
| held-out 비용 | 학습 pool 축소<br>judge 보정용 사람 label 시간 |

<sub>근거: CCAR-F-Udemy01-0010, CCAR-F-Udemy03-0051, CCAR-P-jrajath94-0308, CCAR-P-jrajath94-0554, CCAR-P-preporato-0017</sub>

@@ NEW-SECTION
### Eval set 구성: 대표성 · 층화 · 최신성
**크기가 아니라 production 분포 대표성**

| 상황 | 정답 방향 |
|---|---|
| 이미 잘 처리하는 사례만 포함 | 성능 과장 · 중요한 실패 가림<br>크기로 해결 ✗ · 특정 분야만의 문제 ✗ |
| 최근 티켓 50개 | 최신성 ≠ 포괄성<br>희귀 유형 빠짐 → 실패 안 보임 |
| 문서 유형 12종 · 희귀 유형까지 포함 필요 | 층화(stratified) 표본<br>유형별 최소 개수 · 희귀 유형 · 알려진 edge case<br>규모 수백 개 |
| 다른 모델이 만든 합성 예시 | 생성 모델 편향 반영<br>실제 문서 다양성 ✗ |
| eval 생략 후 출시 후 평점 의존 ✗ | 테스트 없는 배포<br>출시 전 확신 ✗ |
| production 입력이 지저분함<br>(오타 · stack trace · 대문자, 15%) | 들어오는 비율 그대로 반영<br>edge · adversarial · malformed 포함 |
| 위 상황에서 깨끗한 티켓 추가 ✗ | 이미 통과하는 것만 늘림 |
| 위 상황에서 기준 낮춤 ✗ | 기준은 사용자를 따름 · eval 편의 ✗ |
| 위 상황에서 지저분한 입력 필터링 ✗ | 실제 고객 삭제<br>입력이 악용이면 필터링은 제품 결정 |
| 대표성 vs 크기 | 대표성 > 크기<br>깨끗한 1,000개로는 15%를 못 봄 |

| 상황 | 정답 방향 |
|---|---|
| 헤드라인 수치(환각 1%)가 eval 구성 기준 | 집계 함정<br>production 구성과 다름 |
| 모호 · 저context query<br>(production 20% · eval 2%) | 난이도로 층화 · 어려운 tail 오버샘플링<br>production 구성으로 가중한 층별 비율 보고 |
| 구성 각주만 붙여 1% 보고 ✗ | 결정은 여전히 1% 수치 기반 |
| 모호한 query 삭제 ✗ | 지표만 깨끗해지고 실패 숨김 |
| 쉬운 query 추가 ✗ | 이미 측정한 것 재측정 · 사각지대 유지 |

| 상황 | 정답 방향 |
|---|---|
| production 구성 변경(새 제품 line)<br>eval 전부 green · 실제 품질 나쁨 | eval 새로고침 · 현재 구성에 맞춤<br>주제 · 최신성으로 층화 · 새 line 포함<br>새 세트로 점수 재baseline |
| eval이 측정하는 것 | 추출된 시점의 세계<br>production이 변하면 eval도 갱신 |
| 옛 티켓 추가 ✗ | 없어진 세계에 정밀도만 상승<br>(stale-evaluation 함정) |
| 한 분기 대기 후 자연 축적 ✗ | 그 기간 눈 감고 운영 |
| 옛 eval 점수 올리려 모델 tuning ✗ | 새 line 질문 성능 증명 ✗ |
| click-through 서서히 하락 · 1년 된 drawer | 원인 후보 = 오래된 eval<br>regression suite green이어도 사용자 고통<br>→ 최근 대표 data로 refresh |
| 반례 | trace가 새 data에서 모델 실패를 보이면<br>모델이 원인 |

| 요구 | 정답 방향 |
|---|---|
| 실제 traffic과 일치 | 최근 production traffic 샘플링<br>→ 실제 작업 구성 반영 |
| 특이 입력 포괄 | 빈 · 긴 · 무관 입력을 edge case로 추가<br>기대 답변은 code로 확인 가능하게 |
| 싼 daily run · 빠른 check loop | 확인 가능한 case는 code 기반 check<br>(출력 형식이 허용하는 곳마다) |
| 사람 panel로 전 답변 채점 ✗ | 느리고 비쌈 |
| 세트 낡음 방지용 매시간 재구축 ✗ | 요구 조건에 없는 관리 |
| ⚠️ Console 샘플러 · 자동 label | 해설이 "문서에 설명 없음"으로 배제<br>문서 변경 시 달라질 수 있음 |

| 상황 | 정답 방향 |
|---|---|
| production 대화 mining<br>(계좌번호 · 건강 정보 · 공유 bucket) | trust boundary 벗어나기 전 PII 제거 |
| 수정된 bug(예: 잘못된 복용량 안내) | regression drawer에 유지 · 변경마다 실행<br>수정됨 = 방어됨 |
| "현실적 data 필요"로 PII 유지 ✗ | 경계보다 우선 ✗ |
| bucket만 trust boundary 안으로 이동 ✗ | PII 그대로 · drawer 미지정 |
| 고친 bug case 삭제 ✗ | 다음 변경이 조용히 되살림 |
| 제거 후 검증 | 제거로 맥락 소실 가능<br>→ case가 동작을 계속 테스트하는지 확인 |
| 반례 | 접근 제어된 경계 안 bucket이면<br>PII 제거는 선택 |
| sampling 갱신 | production이 바뀌는 만큼 갱신 |

<sub>근거: CCAR-P-Amey-Thakur-0021, CCAR-P-Amey-Thakur-0058, CCAR-P-jrajath94-0025, CCAR-P-jrajath94-0086, CCAR-P-jrajath94-0089, CCAR-P-jrajath94-0186, CCAR-P-jrajath94-0189, CCAR-P-jrajath94-0435, CCAR-P-jrajath94-0656, CCAR-P-jrajath94-0658, CCAR-P-jrajath94-0688</sub>

@@ NEW-SECTION
### Eval drawer 5종: 빠진 서랍 찾기
**representative · edge · adversarial · malformed · regression**

| drawer | 담는 것 |
|---|---|
| representative | 실제 traffic 구성<br>(지원하는 모든 언어 · 유형) |
| edge | 드물지만 유효한 입력<br>(흔치 않은 소득 유형 · 비전형 증상) |
| adversarial | 시스템을 속이도록 만든 입력<br>(위장 피싱 · 편향 · 거짓 유도 · unsafe code 유도) |
| malformed | 깨짐 · 일부만 · 오타 · 빈 입력 |
| regression | 과거 bug case<br>(변경마다 실행) |

| 상황 | 빠진 drawer |
|---|---|
| 정직한 이메일로 98% · 정교한 피싱 통과 | adversarial<br>정직 data 정확도 ≠ 공격 내성 |
| triage bot: 교과서 사례만 | edge + adversarial<br>(둘 다 안전 직결) |
| 대출 설명: 전형적 신청서 1,000건 | edge + adversarial<br>representative는 이미 가득 |
| code assistant: Python 과제만 | 다른 언어 representative<br>+ adversarial(unsafe code 유도) |
| 여행 bot: 영어 query만 | 다른 언어 representative<br>+ malformed(실제 traffic은 지저분) |
| 오답 보기 공통 | 같은 case 더 추가 · training set 재사용 ✗<br>분량만 늘고 다양성 ✗ |
| 빈 입력만 추가 | malformed로는 셋째 추가 항목 후보<br>단독 정답 ✗ |
| adversarial 유지 | red team 사례 필요<br>공격이 바뀌면 갱신 |

<sub>근거: CCAR-P-jrajath94-0313, CCAR-P-jrajath94-0366, CCAR-P-jrajath94-0429, CCAR-P-jrajath94-0492, CCAR-P-jrajath94-0555</sub>

@@ ADD-TO: ### 1-2. Grader 선택: free-form prose에는 LLM-as-judge

| 구분 | 내용 |
|---|---|
| grading 순서 | code → LLM judge → 사람 표본<br>가장 빠르고 신뢰할 수 있고 확장되는 방법 선택 |
| code grader | 정확 일치 · 확인 가능한 field에 최적<br>가장 빠르고 신뢰할 수 있음 · 저비용 |
| LLM judge | 어조 같은 판단 영역 담당<br>신뢰성 테스트 후에만 대량 적용 |
| 사람 grading | 느리고 비쌈 → 전수 채점 ✗<br>표본 점검 · 정기 audit용 |
| 혼합 batch(예: 야간 30,000건) | 정확 일치 field → code<br>어조 → 신뢰성 확인된 LLM judge |
| 신뢰성 테스트 없이 전량 LLM 채점 ✗ | judge 신뢰 미확인 |
| 두 번째 LLM으로 각 판정 교차 검증 ✗ | 신뢰성 테스트를 대신 못 함 |

| 구분 | 내용 |
|---|---|
| 미보정 judge 점수 | 측정값 ✗ · 의견일 뿐<br>사람 label이 측정값으로 만듦 |
| 보정 절차 | 대표 sample에 사람 label 수집<br>→ judge를 label에 맞춰 calibrate<br>→ 그 뒤에야 점수 신뢰 |
| re-baseline | drift가 발생한 기간의 기준선 재설정 |
| judge 점수 상승 · 사용자 불만 증가 | judge가 사람 판단과 어긋났다는 신호<br>→ 보정이 먼저 |
| 일치율 낮음(예: 100건 표본에서 60%) | 채점 결과 신뢰 ✗<br>judge 수정 · 교체 또는 code · 사람 채점 |
| 일치율 높고 불일치 특성 파악(예: 95%) | judge 사용 가능 |
| ⚠️ 일치율 수치 | 해설의 "60% = 우연 수준"은 척도에 따라 다름<br>수치 기준은 공식 문서에 없음 · 예시로만 암기 |
| 보정 비용 | 사람 label은 시간 · 비용<br>→ 한 번 보정 후 grading 순서로 운용 |

| 구분 | 내용 |
|---|---|
| 주관 품질(예: 법률 조항 요약)을 측정 가능하게 | 중요한 실패 유형을 담은 rubric<br>전문가와 함께 만든 labeled 세트<br>rubric 기반 model 채점 + 정기 사람 audit |
| 출시 후 불만 건수 집계 ✗ | 너무 늦게 측정 |
| 참조 요약과 정확 일치 ✗ | 타당한 바꿔 쓰기도 실패 처리 |
| 출력 길이 · thumbs-up 수만 ✗ | 품질 측정 ✗ |

<sub>근거: CCAR-P-Amey-Thakur-0006, CCAR-P-Amey-Thakur-0039, CCAR-P-jrajath94-0187, CCAR-P-jrajath94-0428, CCAR-P-jrajath94-0491, CCAR-P-jrajath94-0657</sub>

@@ NEW-SECTION
### 혼합 평가와 사람 검토 표본
**자동 지표의 사각지대는 judge + 사람 표본으로 보강**

| 상황 | 정답 방향 |
|---|---|
| code agent: unit test 통과 82%<br>가독성 · 관례 불만 · 엉뚱한 문제 풀이도 통과 | LLM judge로 style guide 기준 채점<br>(가독성 · 관례, 전 과제 확장 가능)<br>+ 사람 spot-check로 표본의 의도 일치 확인 |
| 원칙 | 자동 test · judge · 사람 검토 병행<br>각각이 나머지의 빈틈 보완 |
| test를 300 → 3,000개로 확대 ✗ | 같은 지표의 사각지대 그대로 |
| token 효율 측정 ✗ | 불만과 무관<br>간결하나 읽기 어려운 code에 보상 가능 |

| 사람 검토의 역할 | 내용 |
|---|---|
| 판단 기준점 | 주관 품질은 사람 label로 anchor |
| 정기 audit | rubric 기반 model 채점 결과를 labeled 세트로 감사 |
| 표본 spot-check | 문제를 실제로 해결했는지(의도 일치) 확인 |
| judge 보정 | 대표 sample에 사람 label |

| 상황 | 정답 방향 |
|---|---|
| 자동 review 지적의 기각률 상승(29% → 46%)<br>지적 문구가 매번 달라 집계 불가 | schema에 `detected_pattern` 추가<br>지적을 낳은 code 구조 기록<br>→ pattern별 지적 수 · 기각률 집계 |
| 운영 | 값 목록 고정<br>새 pattern은 `other`로 받아 정기 재검토 |
| 활용 | 기각률 높은 pattern<br>→ review 기준 재검토 · 일시 보고 중단 |
| 확신도 threshold 미만 지적 미게시 ✗ | 지적 종류를 구별 ✗ |
| 자유 기술 기각 사유 집계 ✗ | 집계 어려움 |
| PR별 기각률 · 작성자에게 확인 촉구 ✗ | 지적 종류를 구별 ✗ |
| 판별 기준 | 지적의 "종류"라는 분석 단위를 만드는가 |

<sub>근거: CCAR-F-Udemy05-0057, CCAR-P-Amey-Thakur-0006, CCAR-P-Amey-Thakur-0039, CCAR-P-jrajath94-0031</sub>

@@ ADD-TO: ### 1-3. Regression suite

| 상황 | 정답 방향 |
|---|---|
| 목표 지표는 개선 · 측정 안 한 동작은 저하 | 잃어선 안 되는 동작을 포괄하는<br>regression suite 유지 |
| 한 번에 하나 변경 · 신중한 review · 변경 빈도 제한 ✗ | 위험만 줄임<br>탐지 ✗ · 안전화 ✗ |
| 재평가 trigger | model · prompt · data 분포 · 요구사항 변경<br>동작 결정 요소가 바뀌면 이전 측정 무효 |
| trigger 아님 | 보고된 사고만 · 고정 연간 일정 · 비용 변화 |
| prompt 수정 후 품질 악화 · 원인 논쟁 | 고정 eval set을 이전 · 새 prompt 모두 실행<br>category별 점수 비교<br>→ prompt를 변수로 분리 · 퇴보 지점 특정 |
| 시점이 같다며 즉시 되돌림 ✗ | 시점 = 상관관계<br>고칠 수 있는 개선까지 버림 |
| 사용자에게 변화를 물음 ✗ | 노이즈 많고 느림<br>(eval은 당일 답) |
| 더 큰 모델로 교체 ✗ | 원인 미확인 · 비용 영구 상승 |

| 구분 | 내용 |
|---|---|
| regression drawer red | 이전 동작이 깨짐 → ship ✗<br>회귀 원인 파악 · 수정<br>또는 case를 의도적으로 update |
| red case 삭제 ✗ | 측정 파괴 |
| prompt 직접 편집으로 형식 파손<br>(downstream parser 중단 · 변경 기록 없음) | prompt를 code처럼 version 관리<br>모든 변경에 CI로 eval 실행<br>회귀 시 배포 차단 · changelog 유지 |
| 효과 | 회귀 없음 증명이 배포 전에 일어남<br>모든 변경을 귀속 가능 |
| 두 번째 엔지니어의 눈 확인 ✗ | 측정 없는 review<br>형식 회귀 예측 불가 |
| 화요일에만 변경 허용 ✗ | 파손 시점만 바뀜 |
| 시니어에게만 편집 허용 ✗ | 경력은 회귀를 줄일 뿐 증명 ✗ |
| prompt 변경 순서 | regression eval<br>→ 사전 정의 지표로 현재 prompt와 통제된 A/B<br>→ 배포 |
| 순서 근거 | prompt 변경 = production 변경 |
| 출시 후 불만 monitoring · 팀 투표 · 피드백 양식 ✗ | 사용자에게 도달한 뒤 감지 |

<sub>근거: CCAR-P-Amey-Thakur-0022, CCAR-P-Amey-Thakur-0023, CCAR-P-Amey-Thakur-0040, CCAR-P-jrajath94-0026, CCAR-P-jrajath94-0090, CCAR-P-jrajath94-0365</sub>

@@ ADD-TO: ### 1-4. Model 업그레이드와 운영

| 상황 | 정답 방향 |
|---|---|
| 기반 model version 업데이트 | production traffic 도달 전 eval suite 재실행 |
| "버전 호환이니 무조치" ✗ | 호환 가정 = 안전 ✗ |
| 일주일 monitoring 강화 · 불만 시 자동 rollback ✗ | 사용자 영향 후에야 감지 |
| vendor update 후 어조가 무례해짐<br>(prompt · retrieval · data 불변) | 실패 계층 = model version<br>version pin 또는 변경 + regression 재실행 |
| version 동작 | production 변경으로 취급 |
| 반례 | prompt가 바뀌었다면 원인은 prompt |

1. 새 prompt를 shadow로 실행(결정 기록 · 조치 ✗)
2. 주요 지표 monitoring하며 통제된 노출
3. 전체 rollout

| 구분 | 내용 |
|---|---|
| 적용 대상 | 사용자 · 돈에 해를 끼칠 수 있는 변경<br>(예: 정당한 환불을 잘못 거부) |
| shadow | 사용자 영향 없이 해를 측정<br>이전 prompt가 계속 서비스 · 며칠 소요 |
| 통제된 노출 | 영향 범위(blast radius) 제한<br>주요 지표에 임계값 필요 |
| 전체 배포 후 주말 dashboard 관찰 ✗ | 측정 전에 모든 사용자 도달 |
| 즉시 50% 배포 ✗ | shadow 생략<br>50,000건 중 25,000명 피해 가능 |
| 모델에게 새 prompt가 안전한지 질문 ✗ | 모델 승인 ≠ test |
| 대규모 traffic이면 test 불필요라는 생각 ✗ | 큰 traffic = 큰 해 |
| 반례 | 되돌릴 수 있고 저위험(문구 · 돈 무관) 조정은<br>단순 배포 가능 |

| 구분 | 내용 |
|---|---|
| canary 롤백 기준 | canary 시작 전에 trigger 사전 등록<br>→ 자동 rollback에 연결<br>(예: escalation 비율 +2pt, 30분 지속) |
| 사전 정의 | 주요 지표 · guardrail 지표<br>최소 실행 시간 · 최소 표본 크기 |
| 사전 정의 효과 | "흔들림"이 신호인지 잡음인지 논쟁 방지 |
| 원칙 | 판단을 실험 이전으로 이동 · 논쟁은 등록 시점에 한 번 |
| canary 중 on-call 경험 판단 ✗ | 사고 중 판단 = 논쟁 · 담당자에 따라 달라짐 |
| on-call 2명 · dashboard 면밀 감시 ✗ | 관찰만 개선 · 결정은 개선 ✗ |

<sub>근거: CCAR-P-Amey-Thakur-0074, CCAR-P-jrajath94-0088, CCAR-P-jrajath94-0190, CCAR-P-jrajath94-0494</sub>

@@ RULES

| 상황 | 정답 |
|---|---|
| pilot 결함 발견 후 대량 batch 앞둠 | 대표 eval set · 기준으로 개선·재평가<br>→ 동기 dry run → 전체 투입 |
| 희귀 유형까지 보여야 하는 eval 구성 | 층화 표본 · 유형별 최소 개수<br>희귀 유형 · edge case 포함 |
| eval은 green · production 품질 나쁨 | production 구성에 맞춰 eval 새로고침<br>층화 후 재baseline |
| 집계 수치(예: 환각 1%)가 어려운 tail을 가림 | 난이도 층화 · tail 오버샘플링<br>production 가중 층별 비율 보고 |
| eval에 정직 · 전형 case만 있음 | 빠진 drawer 추가<br>(edge · adversarial<br>· malformed · regression) |
| production 대화로 eval case 구성 | boundary 벗어나기 전 PII 제거<br>수정된 bug는 regression drawer에 유지 |
| 높은 점수의 신뢰성 확인 | held-out 세트 + judge를 사람 label로 보정<br>같은 example로 tuning · 보고 ✗ |
| judge 점수 상승 · 불만 증가 · judge 미검증 | 대표 sample에 사람 label → calibrate<br>drift 기간 re-baseline |
| 주관 품질(요약 · 법률 검토) 평가 | rubric + labeled 세트 + model 채점<br>+ 정기 사람 audit |
| 확인 가능한 field + 어조 판단 혼재 | field → code grader<br>어조 → 신뢰성 확인된 LLM judge |
| 자동 지표(test 통과율)의 사각지대 | LLM judge(style) + 사람 spot-check(의도) |
| 자동 review 지적의 기각 분석 | schema에 `detected_pattern` 추가<br>값 목록 고정 · 새 값은 `other` |
| 목표 지표 개선 · 다른 동작 저하 | 잃어선 안 되는 동작의 regression suite |
| 재평가 시점 | model · prompt · data 분포 · 요구사항 변경 시 |
| prompt 수정 후 악화 원인 논쟁 | 고정 eval set을 이전 · 새 prompt에 실행<br>category별 비교 |
| regression drawer가 red | ship ✗ · 원인 수정 또는 의도적 case update<br>삭제 ✗ |
| prompt 편집이 downstream 형식 파손 | version 관리 · CI eval gate<br>회귀 시 배포 차단 · changelog |
| prompt 변경 배포 순서 | regression eval → 통제된 A/B → 배포 |
| model version 업데이트 | traffic 도달 전 eval suite 재실행 |
| 변경 없는데 어조만 변함(vendor update) | 원인 = model version<br>pin 또는 변경 후 regression 재실행 |
| 사용자 · 돈에 해를 줄 수 있는 변경 | shadow → 통제된 노출 → 전체 rollout |
| canary 롤백 판단 | 시작 전 trigger 사전 등록 · 자동 rollback<br>지표 · 최소 실행 시간 · 표본 크기 사전 정의 |

<sub>근거: CCAR-F-Udemy01-0010, CCAR-F-Udemy03-0051, CCAR-F-Udemy05-0057, CCAR-P-Amey-Thakur-0006, CCAR-P-Amey-Thakur-0021, CCAR-P-Amey-Thakur-0022, CCAR-P-Amey-Thakur-0023, CCAR-P-Amey-Thakur-0039, CCAR-P-Amey-Thakur-0040, CCAR-P-Amey-Thakur-0058, CCAR-P-Amey-Thakur-0074, CCAR-P-jrajath94-0025, CCAR-P-jrajath94-0026, CCAR-P-jrajath94-0031, CCAR-P-jrajath94-0086, CCAR-P-jrajath94-0088, CCAR-P-jrajath94-0089, CCAR-P-jrajath94-0090, CCAR-P-jrajath94-0187, CCAR-P-jrajath94-0189, CCAR-P-jrajath94-0190, CCAR-P-jrajath94-0308, CCAR-P-jrajath94-0313, CCAR-P-jrajath94-0365, CCAR-P-jrajath94-0494, CCAR-P-jrajath94-0554, CCAR-P-jrajath94-0657, CCAR-P-preporato-0017</sub>

@@ TRAPS

| 오답 | 이유 |
|---|---|
| eval 세트를 크게 만들어 편향 해소 | 편향 표본은 크기로 안 고쳐짐<br>실패 유형이 계속 가려짐 |
| 같은 종류 case 추가 · training set 재사용 | 분량만 늘고 사각지대 유지 |
| 최근 티켓 · 합성 예시로 eval 구성 | 희귀 유형 누락 · 생성 모델 편향 |
| 구성 각주 · 어려운 case 삭제 · 쉬운 case 추가 | 오해 소지 헤드라인 유지<br>실패 숨김 |
| 옛 티켓 추가 · 옛 점수 올리려 tuning<br>한 분기 대기 | stale-evaluation 함정<br>현재 production 예측 ✗ |
| 지저분한 입력 필터링 · 기준 낮춤 | 실제 사용자 삭제 · 기준 후퇴 |
| judge prompt로 점수 낮추기 · 더 큰 judge<br>judge 3개 평균 | 숫자만 이동 · 크기 ≠ ground truth<br>틀린 것 셋의 평균도 틀림 |
| 신뢰성 테스트 없이 LLM 전량 채점<br>두 번째 LLM 교차 검증 | 신뢰성 확인이 선행 조건 |
| 모든 답변을 사람 panel로 채점 | 느리고 비쌈 |
| unit test 수 확대 · token 효율 측정 | 사각지대(가독성 · 의도) 그대로 |
| 확신도 threshold · 자유 기술 사유 · PR별 기각률 | 지적 종류를 집계 못 함 |
| ⚠️ Console 샘플러 · 판정 cache 설정 | 해설이 "문서에 설명 없음"으로 배제<br>문서 변경 시 달라질 수 있음 |
| ⚠️ "60% 일치 = 우연 수준" | 척도 의존 표현 · 공식 문서에 수치 기준 없음 |
| PII 유지 · bucket만 이동 · 고친 bug case 삭제 | 노출 지속 · 회귀 방어 상실 |
| 한 번에 하나 변경 · 신중 review · 변경 빈도 제한 | 위험 감소일 뿐 회귀 탐지 ✗ |
| 사고 · 연간 일정 · 비용을 재평가 trigger로 사용 | 늦거나 실제 변경과 무관 |
| 시점 상관관계로 revert · 사용자 인상 확인 | 증거 아님 · 노이즈 · 느림 |
| 사람 눈 review · 요일 제한 · 시니어 제한 | 측정 없음 · 회귀 증명 ✗ |
| 호환 가정 · monitoring 강화 · 불만 후 자동 rollback | 사용자 영향 후에야 감지 |
| 즉시 50% 배포 · 전체 배포 후 dashboard | shadow 생략 · 측정 전 피해 |
| 모델에게 prompt 안전성 질문 | test 아님 |
| canary 중 on-call 판단 · 감시 인원 증원 | 관찰만 개선 · 결정 개선 ✗ |

<sub>근거: CCAR-F-Udemy05-0057, CCAR-P-Amey-Thakur-0006, CCAR-P-Amey-Thakur-0021, CCAR-P-Amey-Thakur-0022, CCAR-P-Amey-Thakur-0023, CCAR-P-Amey-Thakur-0040, CCAR-P-Amey-Thakur-0058, CCAR-P-Amey-Thakur-0074, CCAR-P-jrajath94-0025, CCAR-P-jrajath94-0026, CCAR-P-jrajath94-0031, CCAR-P-jrajath94-0086, CCAR-P-jrajath94-0088, CCAR-P-jrajath94-0089, CCAR-P-jrajath94-0090, CCAR-P-jrajath94-0186, CCAR-P-jrajath94-0187, CCAR-P-jrajath94-0189, CCAR-P-jrajath94-0190, CCAR-P-jrajath94-0366, CCAR-P-jrajath94-0429, CCAR-P-jrajath94-0435, CCAR-P-jrajath94-0491, CCAR-P-jrajath94-0492, CCAR-P-jrajath94-0555, CCAR-P-jrajath94-0656, CCAR-P-jrajath94-0657, CCAR-P-jrajath94-0658, CCAR-P-jrajath94-0688</sub>

@@ MEMO

| 이름 | 의미 |
|---|---|
| eval drawer 5종 | representative · edge · adversarial<br>malformed · regression |
| grading 순서 | code → LLM judge → 사람 표본 |
| stratified 표본 | 유형 · 난이도 · 최신성별로 나눠 추출<br>희귀 유형 최소 개수 보장 |
| held-out 세트 | tuning · 학습에 쓰지 않은 평가 세트 |
| judge calibration | 사람 label과 대조해 judge 보정 |
| re-baseline | drift 기간의 기준선 재설정 |
| stale-evaluation 함정 | production이 변했는데 eval이 옛 세계에 머묾 |
| shadow 모드 | 새 prompt 실행 · 결정 기록 · 조치 ✗ |
| blast radius | 변경 노출 시 피해가 미치는 범위 |
| canary 사전 정의 4종 | 주요 지표 · guardrail 지표<br>최소 실행 시간 · 최소 표본 크기 |
| `detected_pattern` | 지적을 낳은 code 구조를 기록하는 schema 필드<br>기각 pattern 집계용 |

<sub>근거: CCAR-F-Udemy05-0057, CCAR-P-jrajath94-0025, CCAR-P-jrajath94-0086, CCAR-P-jrajath94-0088, CCAR-P-jrajath94-0187, CCAR-P-jrajath94-0190, CCAR-P-jrajath94-0308, CCAR-P-jrajath94-0313, CCAR-P-jrajath94-0554, CCAR-P-jrajath94-0657</sub>

@@ CHECK

- [ ] eval 점검 → 대표성 · 층화 · 최신성 · 빠진 drawer
- [ ] judge 점수 → 사람 label로 보정한 뒤에만 신뢰
- [ ] 변경(prompt · model) → regression suite 재실행 · red면 ship ✗
- [ ] 해를 줄 수 있는 변경 → shadow → 통제된 노출 · rollback trigger 사전 등록

<sub>근거: CCAR-P-jrajath94-0025, CCAR-P-jrajath94-0026, CCAR-P-jrajath94-0088, CCAR-P-jrajath94-0187, CCAR-P-jrajath94-0190, CCAR-P-jrajath94-0313, CCAR-P-jrajath94-0365</sub>
