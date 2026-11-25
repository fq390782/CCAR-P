@@ NEW-SECTION
### 문제 형태별 적합한 구조
**사실이 필요하면 retrieval · 동작이 필요하면 classifier**

| 상황 | 적합한 구조 | 이유 |
|---|---|---|
| 매일 바뀌는 대규모 카탈로그 기반 제품 질문 | 갱신되는 index 검색<br>+ 검색 context로 답변 | 자주 바뀌는 지식 = 검색의 몫<br>(가중치 · context window ✗) |
| 월 갱신 300페이지 매뉴얼 · 단일 턴 · 인용 필요 | augmented LLM<br>(retrieval + 단일 호출 + 구절 인용) | 범위 정해진 근거 호출 하나로 충족 |
| 고정 카테고리 · 안정적 정의 · retrieval 불필요<br>(티켓 분류) | classifier<br>(fine-tuned 또는 규칙 기반) | 필요한 것 = 사실 ✗ · 안정적 동작<br>retrieval = 토큰만 추가 · 경계 불변 |
| 형태가 다른 잘 알려진 두 문제<br>(정책 질문 인용 답변 + 결정 데이터 → 통지서) | 단순 구성요소 둘<br>= 검색 증강 답변 서비스 + 템플릿 생성 workflow | 독립 테스트 · 통제<br>각자 자체 지표로 평가 |

| 기각 대상 | 이유 |
|---|---|
| 매일 밤 fine-tune | 갱신 지식을 가중치에 넣기 ✗ |
| 매월 fine-tuning | 무겁고 재인덱싱보다 업데이트 느림 · 인용 ✗ |
| 카탈로그를 system prompt에 적재 | 갱신 지식 = context window ✗ |
| 공개 웹 탐색 자율 agent | 갱신 index 검색으로 충족 · 자율성 불필요 |
| 자율 agent · multi-agent 리서치 | 작업에 불필요한 자율성 → 비용 · 지연 증가 |
| 두 작업을 multi-agent 하나로 | "문서를 다룬다" = 아키텍처 논거 ✗ |
| 모든 도구를 가진 단일 agent | 무관한 위험 프로파일 결합 |
| 두 작업을 fine-tuned 모델 하나로 | 검색 · 템플릿이 이미 해결 → 가장 비싼 경로 |
| 고정 카테고리에 RAG | 필요한 것은 사실이 아닌 동작 |

- RAG가 정답으로 바뀌는 조건 = 카테고리가 매주 변경 · 감사 담당자가 출처 요구
<sub>근거: CCAR-P-Amey-Thakur-0004, CCAR-P-Amey-Thakur-0036, CCAR-P-jrajath94-0526, CCAR-P-preporato-0001</sub>

@@ NEW-SECTION
### 복잡성은 요구사항으로 정당화
**복잡성 = 지속 비용 · 명시 요구사항으로 구매**

| 상황 | 정답 방향 | 이유 |
|---|---|---|
| 두 설계가 기능 요구사항 충족<br>· 하나가 더 단순 | 추가 capability가 명시 요구사항에 필요한지<br>vs 복잡성 비용으로 결정 | 복잡성 = 운영 · 유지보수의 지속 비용 |
| 과잉 설계의 가장 분명한 징후 | 어떤 명시 요구사항도 의존하지 않는 구성요소 | 정당화 ✗ 구성요소 = 썩게 될 부분 |
| 여러 모델 · 평가 스위트 · 승인 단계 | 과잉 설계 징후 ✗ | 요구사항이 있으면 방어 가능 |

| 오답 근거 | 이유 |
|---|---|
| 더 능력 있는 설계 · 여유 용량 | 능력 자체는 정당화 ✗ · 비용만 발생 |
| 팀이 흥미롭게 여기는 설계 · 선호 | 선호는 요구사항 ✗ |
| 구성요소를 늘린 설계 | 추측에 근거한 유연성 · 정당화 없는 비용 |
<sub>근거: CCAR-P-Amey-Thakur-0017, CCAR-P-Amey-Thakur-0019, CCAR-P-Amey-Thakur-0054</sub>

@@ NEW-SECTION
### 자동화 경계와 책임 소재
**자동화 경계는 책임이 정하는 아키텍처 결정**

| 상황 | 정답 | 이유 |
|---|---|---|
| 이해관계자가 승인 프로세스 전체를<br>자율 agent로 요청 | 첫 확인 = 책임이 따르는 결정 중<br>사람에게 남길 것 | 책임 위치가 솔루션 형태와<br>자동화 가능 범위를 결정 |
| 고객 영향 결정의 자동화 경계 | 결정 책임이 있는 곳<br>· 사람이 맡도록 유지 | 경계 = 아키텍처상 결정 |
| 규제 통제가 모델의 올바른 동작에 의존 | 수용 ✗ → 모델 밖에서 결정론적 강제 | 필수 통제 = 보장 필요<br>확률적 동작 = 보장 제공 ✗ |

| 오답 | 이유 |
|---|---|
| 모델 선택 · 토큰 비용 · 일정부터 확인 | 경계 확정 뒤의 하위 문제 |
| 테스트 성능 · 예산 · 고객 요청이 경계 | 책임 문제를 다루지 않음 |
| 높은 평가 정확도 · 더 큰 모델 | 경향을 보장으로 바꾸지 못함 |
| 규제 기관 면책 문구 · 잔여 위험 문서화 | 경향을 보장으로 바꾸지 못함 |
<sub>근거: CCAR-P-Amey-Thakur-0016, CCAR-P-Amey-Thakur-0018, CCAR-P-Amey-Thakur-0055, CCAR-P-Amey-Thakur-0056</sub>

@@ NEW-SECTION
### Discovery: 요구사항 구체화와 제약 분류
**한계 없는 요구는 구체화 · 제약은 hard vs 목표로 분류**

| 구분 | 내용 |
|---|---|
| hard constraint | 절대 일어나서는 안 되는 조건<br>위반 시 직접 손실 · gate로 강제 |
| 목표 | 임계값 + 담당자를 가진 요구<br>(지원 언어 · 단가 · p95 latency)<br>위반 시 지연 · 사업 결정 |
| 오해 | 번호 매긴 모든 요구사항 = hard constraint ✗ |
| 추적 | hard 아닌 항목도 담당자 있는 목표로 관리 |

| 항목 | hard가 되는 조건 |
|---|---|
| 지원 언어 | 규제 기관이 미지원 언어마다 벌금 |
| 단가 상한 | 초과 시 사업성 음수 → build/no-build gate |
| p95 30초 | 결제 마감 창이 30초에 닫힘 → 늦은 건 거부 |

| 상황 | 정답 | 이유 |
|---|---|---|
| "가능한 한 정확하게" 같은 한계 없는 요구 | 실제 필요한 정확도 + 오류 비용 파악 | 한계 없는 요구 = 설계 · 검증 불가 |
| 규제 하 build vs buy<br>(데이터 경로 통제 유지) | 통제 · 결합도 평가<br>기능 수 = 부차적 | 규제 · lock-in 위험이 결정을 좌우 |

| build vs buy 평가 축 | 질문 |
|---|---|
| 통제 | 시스템이 데이터를 처리 · 저장하는 위치<br>audit trail 소유자 |
| 결합도 | 나중에 model 계층을 교체하는 비용<br>exit 옵션 |
<sub>근거: CCAR-P-Amey-Thakur-0069, CCAR-P-jrajath94-0068, CCAR-P-jrajath94-0109</sub>

@@ NEW-SECTION
### Hard constraint → 설계 분기와 code gate
**첫 행동 = 제약 기록 · 입력 형태 분기 · 코드 gate**

| 구분 | 내용 |
|---|---|
| 적용 상황 | 돈 이동 · 승인 · 차단 · 보상 · 예약 · 조언에<br>"검증 없이 ~ 금지" 규칙 포함 |
| 순서 | 제약을 설계에 기록 → lane 분기<br>→ gate 배치 → 구축 |
| 분기 | 정형 입력(약 75~95%) → 결정론적 규칙 · 파서<br>복잡 · 분쟁 · 열린 형식(5~25%) → Claude |
| gate | 위험 행동 직전 코드가 규칙 강제<br>(결제 전 합계 · 승인 전 시술 코드<br>· 보상 전 태그 · 차단 전 사유 기록) |
| gate 입력 | 파싱한 값 + 원본 문서 둘 다 필요 |
| prompt | guidance ✗ enforcement<br>모델은 따를 수도 아닐 수도 · gate 실행 증명 ✗ |
| prompt 적합 | 어조 · 형식 같은 스타일 안내 |
| 비용 | 이번 주 눈에 보이는 진척 ✗ · 짧은 설계 중단 |

| 오답 | 이유 | 정답이 되는 조건 |
|---|---|---|
| 점검 없는 단일 agent · 최상위 tier | gate 없음 → 절대 규칙 강제 ✗ | 해당 없음 |
| 사람이 전건 검토 | 일 5,000~20,000건 규모 감당 ✗ | 일 40~60건 + 건당 법적 · 사기 · 의료 과실 위험 |
| 이번 주 end-to-end 구축 | 제약이 존재하기 전에 구축 | 돈 이동 없는 일회용 demo · sandbox |
| tier 벤치마크 먼저 | 제약 기록 전 tier 선택 = 잘못된 첫 질문 | gate가 설계에 들어간 뒤 품질 하한 확인 |
| 금지 문구 system prompt | 돈 · 컴플라이언스 규칙을 prompt에 위임 | 스타일 안내 |
<sub>근거: CCAR-P-jrajath94-0108, CCAR-P-jrajath94-0332, CCAR-P-jrajath94-0333, CCAR-P-jrajath94-0395, CCAR-P-jrajath94-0396, CCAR-P-jrajath94-0458, CCAR-P-jrajath94-0459, CCAR-P-jrajath94-0522</sub>

@@ NEW-SECTION
### End-to-end 파이프라인과 feedback loop
**완전한 설계 = 입력 · 처리 · 출력 · 피드백 루프**

| 단계 | 내용(송장 처리 예) |
|---|---|
| 입력 | 이메일 수신 · OCR |
| 처리 | 스키마 검증을 포함한 추출 |
| 출력 | 예외 큐를 갖춘 ERP 전기 |
| 피드백 | 필드별 정확도 평가 · 사용자 수정 · 모니터링<br>→ prompt · 모델 결정에 반영 |

| 불완전한 설계 | 이유 |
|---|---|
| 입력 단계 없음 + 처리량 대시보드 | 대시보드 = 활동 측정 · 품질 피드백 ✗ |
| 최상위 모델 추출 + 피드백 없음 | 피드백 루프 부재 |
| multi-agent 추출 팀 + 출시 공지 | 복잡성만 증가 · 피드백 루프 부재 |
| 평점만 대량 수집(DB 방치) | 피드백은 어딘가로 갈 때만 품질 개선 |

- 피드백 루프 순서 (일정에 따라 반복)
  1. 낮은 평점 답변을 주기(주 1회)로 샘플링
  2. 실패 사례를 eval 세트에 추가
  3. prompt · 검색 수정안을 eval 세트에 대해 검토
  4. 점수를 개선하는 수정만 배포

| 단계 경계 설계 | 내용 |
|---|---|
| 단계 | 접수 → 처리 → 출력 → 피드백 |
| handoff | 구조화 handoff · 단계별 typed 결과 + 신뢰도 |
| 사람 라우팅 | 저신뢰 · 실패 결과 → 사람 대기열<br>+ 전체 단계 이력 첨부 |
| 감사 추적 | 모든 handoff 로깅 |
| ⚠️ 신뢰도 | 10장: 자기 보고 confidence = 복잡도 지표 ✗<br>이 문항: 단계별 신뢰도 라우팅이 정답<br>상충 소지 · 문항에 신뢰도 산출 방식 없음 |

| 오답 | 이유 |
|---|---|
| 접수 + 처리를 거대 prompt 하나로 | 단계별 관찰 불가 · 실패 위치 파악 어려움 |
| 네 단계 모두 같은 모델 | 균일성 ≠ 관찰 가능성 · 사람 라우팅 |
| 사람 대기열 없는 완전 자율 | 사람 라우팅 제약 위반 |
<sub>근거: CCAR-P-jrajath94-0017, CCAR-P-jrajath94-0020, CCAR-P-preporato-0002</sub>

@@ NEW-SECTION
### 7 gate와 audit trace
**감사 가능 = gate를 코드에 배치 + request ID 하나의 trace**

| 구분 | 내용 |
|---|---|
| gate 순서 | input → validation →<br>context and retrieval → model and tools<br>→ verification → output → feedback |
| 코드 실행 | validation · authorization<br>= context 조립 전 · trust boundary 코드 |
| verification | 초안을 검색된 원본 chunk와 기록된 방식으로 대조 |
| trace 단위 | 모든 hop이 request ID 하나로 trace 방출 |
| trace 내용 | input hash · chunk ID · 초안 · 검사 결과 |
| 선행 조건 | system of record · trace 보관(retention) |
| 비용 | 가장 무거운 구축 · 기록별 trace 저장 비용 |
| trace 한계 | 모델이 초안을 고른 이유 기록 ✗ |
| 기록 대상 | 무엇이 검사했고 누가 승인했는가 |

| 감사 재현 요소 | 판정 | 필요해지는 조건 |
|---|---|---|
| 검사에 쓴 record ID<br>(system of record 원본 사실) | 필수 | 항상 |
| hop별 기록 = 어떤 gate가 승인했는가 | 필수 | 항상 |
| temperature · top-p | 승인 hop · 검사 record 지목 ✗ | 품질 회귀 디버깅 |
| 전체 prompt 텍스트 | 있으면 좋음 · 명시 목표에 불필요 | 분쟁이 prompt 내용 |
| GPU region | 감사 가치 ✗ | latency · residency 사고 |

| 오답 | 이유 | 정답이 되는 조건 |
|---|---|---|
| 단일 호출 + prompt 로그 | retrieval · 검사 기록 ✗<br>희망은 gate ✗ | 환자 · 감사 없는 내부 demo |
| 사람이 초안 검토 = trace | model context 미기록<br>검사 기록 ✗ | 일 50건 · 법적 위험<br>+ 검색 원본도 확인 |
| 두 번째 모델 호출 = verification | 초안만 봄 · 원본 대조 ✗ | 검사가 어조 · 형식 |
| 더 많이 로깅 = 더 좋은 감사 | 필요한 것 = record와 hop | 해당 없음 |

| 증상 | 원인 gate | 조치 |
|---|---|---|
| 3% 오답 가격<br>validation · verification 통과<br>retrieval이 오래된 가격표 반환 | context and retrieval | 현재 카탈로그 재-ingest<br>실패한 구성요소를 직접 수정 |
| verification 통과 | 초안 = 원본 일치만 증명 | 오래된 원본은 모든 검사 통과 |

| 재-ingest | 내용 |
|---|---|
| 선행 조건 | 현재 카탈로그 · freshness 검사 |
| 한계 | retrieval 순위 해결 ✗ |
| 다음 오류 | chunk 크기 · 경계 문제로 이동 |

| 오답 | 이유 | 정답이 되는 조건 |
|---|---|---|
| verification 이중 확인 | 이미 통과 · 원본이 낡은 것을 못 봄 | 초안이 chunk와 모순인데 검사가 놓침 |
| 상위 tier로 이동 | 같은 낡은 목록 인용 · 비용만 증가 | 모델이 최신 chunk를 잘못 읽음 |
| 가격 형식 regex | 형식은 맞고 값이 틀림 | 낡은 사실이 아닌 잘못 만든 출력 |
<sub>근거: CCAR-P-jrajath94-0111, CCAR-P-jrajath94-0112, CCAR-P-jrajath94-0113</sub>

@@ NEW-SECTION
### Trust boundary · system of record · verification 배치
**경계 = 신뢰 불가 입력 진입점 · side effect 직전**

| 경계 유형 | 위치 | 코드 통제 |
|---|---|---|
| 입력 경계 | 조작 가능한 외부 입력 → 처리 단계<br>(환자 채팅 · 채팅 입력 · 웹 지원서) | input screening · validation |
| 출력 경계 | model · tool → side effect<br>(EHR 쓰기 · 이체 · HR 쓰기) | 코드에서 authorization |

| 경계 아님 | 이유 |
|---|---|
| KB → 모델 · 원장 읽기 → fraud model | 내부 신뢰 경유 |
| 검증 → 모델 · 같은 프로세스 함수 | 내부 경유 |
| mutual TLS 내부 서비스 · 로그 기록기 → 저장소 | 내부 신뢰 교차<br>(서로 다른 trust zone이면 경계) |

| system of record 판단 | 내용 |
|---|---|
| 재고 기준 | POS 판매 원장 + 입고 기록<br>(기계 기록 · 감사 가능) |
| 계산 | 코드가 입고 − 판매로 대조 |
| 판매자 문자 | untrusted input · 경계 밖 |
| 한계 | 입고 기록도 신뢰 필요 · 도난 · 폐기 · 무상 제공 별도 항목 |
| 반사실 | 검증된 앱에서 바코드 스캔 → 보고도 신뢰 입력 |

| 오답 | 이유 |
|---|---|
| 판매자 문자를 그대로 신뢰 | 오타가 곧 재고 |
| 모델이 두 출처를 혼합해 추정 | 혼합은 검증 ✗ |
| 가장 최근 보고 우선 | 신뢰 ✗ 최신성 · 새 거짓이 낡은 진실을 이김 |

| 상황 | 위치 · 방법 | 강도 |
|---|---|---|
| 대출 사전 승인<br>(잘못된 승인 = 대출액 손실) | 모델 점수 후 · 결정 통지 전<br>점수 입력을 신용평가기관 데이터와 대조 | 코드 검증 |
| 채용 초대(되돌릴 수 있음) | 랭킹 후 · 초대 전<br>추출 스킬을 원본 이력서와 대조 | 가벼운 코드 검사<br>(사람 gate ✗) |
| 의학 기사(독자 피해) | fact check · 법무 검토 후 · 게시 전<br>코드로 주장을 출처와 대조 | 코드 + 사람 승인 |

| 오답 위치 | 이유 |
|---|---|
| 접수 이전 · 원본 입력에 대해 | 판단할 수 있는 것을 검토 ✗ |
| 통지 · 초대 · 게시 이후 | 피해가 난 뒤 행동 |
| 어디에도 없음 | 통제 없음 |

| 달라지는 조건 | verification 형태 |
|---|---|
| 초대가 구속력 있는 채용 제안 | 사람 gate |
| 되돌릴 수 있는 사전 자격 추정 | 통지 후 검증도 가능 |
| 독자 없는 개인 블로그 | 게시 후 검증도 가능 |
<sub>근거: CCAR-P-jrajath94-0288, CCAR-P-jrajath94-0334, CCAR-P-jrajath94-0335, CCAR-P-jrajath94-0397, CCAR-P-jrajath94-0398, CCAR-P-jrajath94-0460, CCAR-P-jrajath94-0461</sub>

@@ NEW-SECTION
### SLA · 비용 제약과 tier 선택
**정확도 동률이면 명시된 SLA · 비용 제약이 결정**

| 설계 | 구성 | p95 · 비용 |
|---|---|---|
| 설계 1 | 최상위 tier | 6초 · 요청당 $0.09<br>월 약 $180,000 |
| 설계 2 | fast · balanced 라우팅 | 2초 · 요청당 $0.02<br>월 약 $40,000 → 선택 |

| 상황 | 정답 | 이유 |
|---|---|---|
| 정확도 동률 · SLA p95 3초 · 월 2백만 요청 | 3초 SLA 충족 설계 | 비용 pillar도 충족하는 쪽 선택 |
| 장 개시 10배 급증에도 99.9% 가동 · p95 3초 | autoscaling으로 피크 설계<br>+ degraded mode 정의 | 극단 부하의 동작 명시 = 정직한 SLA |
| 전체 pipeline이 3초를 못 맞출 때 | 캐시 답변 · 짧은 답변 · 명확한 banner | 조용히 망가지지 않음 |
| 배치 작업에 최상위 tier 요구<br>(비용 10배 · eval +2%) | 작업 규모에서 +2% 가치 vs 10배 비용<br>+ quality floor로 판단 | 하한이 요구하지 않으면 대개 손해<br>+2%가 구속력 있는 floor면 반전 |

| 오답 | 이유 |
|---|---|
| 정확도 여유 위해 설계 1 | 3초 SLA 위반 |
| 두 설계 무기한 병행 | 이유 없이 비용 · 복잡성 2배 |
| 더 새 모델까지 결정 연기 | 데이터가 이미 뒷받침하는 결정 무시 |
| 평균 부하 프로비저닝 + queue | 장 개시 중 queue = p95 3초 위반 |
| 가장 큰 모델 + 급증 시 느림 감수 | 명시 SLA보다 품질 우선 |
| 장 개시 중 어시스턴트 비활성화 | 설계의 SLA 미충족 인정 |
| "최고" tier · 2% 향상만으로 결정 | 비용 대비 가치 미산정 |
| tier 위신 · 벤더 추천 | 비즈니스 근거 ✗ |
<sub>근거: CCAR-P-jrajath94-0019, CCAR-P-jrajath94-0531, CCAR-P-preporato-0003</sub>

@@ NEW-SECTION
### 순가치 계산과 build / no-build 판단
**순가치 = (기준선 − 새 비용) × 물량 + 회피 오류 − 구축 · 운영**

| 구분 | 내용 |
|---|---|
| 공식 | (기준선 − 새 비용) × 물량<br>+ 회피된 오류 비용 − 구축 · 운영 비용 |
| 필요 입력 | 기준선 · 새 비용 · 회피 오류 · 구축 비용 |
| 기간 맞춤 | 월 = 월 물량 × 단위 절감 − 월 고정비<br>첫해 = 12 × 월 절감 − 일회성 비용 |
| 환산 | 주 → 월 = × 4.33 (주 30시간 ≈ 월 130시간) |
| 결과 | 음수 → 구축 ✗ · "아니오"도 완전한 답 |
| 가정 | 오류당 비용 · 시간 단축 = 가정<br>→ 파일럿으로 실측 |

| 항목 | 계산(가상 수치) |
|---|---|
| 주문당 $1.10 → $0.18 + 월 고정 $400 | 월 60,000건 × $0.92 − $400 = $54,800 |
| 이의 신청당 $6 → $0.90 + 연 고정 $2,000 | 10,000건 × $5.10 − $2,000 = $49,000 |
| 월 $8,000 → $1,200 + 일회성 $5,000 | 12 × $6,800 − $5,000 = $76,600 |
| 주 30시간 × $35 → 월 $400 | 30 × 4.33 × $35 − $400 ≈ $4,146 |
| 일 2시간 × 시간당 인건비 → 월 $60 | 2 × 30 × 시간당 인건비 − $60 |
| 연 인건비 절감 $156,000 + 회피 오류 $3,000<br>− 구축 $20,000 − 실행 $1,040 | 순가치 약 $137,960 → 구축 |
| 실행비 연 $40,000 vs 절감 연 $25,000<br>· 오류 항목 없음 | 순가치 연 −$15,000 → 구축 ✗ |

| 결정 질문 | 정답 | 이유 |
|---|---|---|
| 단위당 비용만 비교 | 고정비 · 물량 반영한 순가치 | 단위당 차이 ≠ 결정 |
| 파일럿이 예산만큼 가치를 냈는가 | 순가치<br>(기준선 인건비 vs 자동화 비용 − 구축 · 운영) | 재무팀 = 순금액으로 결정 |
| model 비용 50% 절감 제안<br>(월 $200,000 방어 · 놓침 +2%) | 절약 비용 vs 놓친 사기 손실<br>(월 $4,000) + quality floor 영향 | 절감액 > 새 손실이어야 |

| 지표 | 결정 숫자가 되는 조건 |
|---|---|
| 모델 정확도 | 옵션 간 오류율이 다를 때 |
| p95 latency | SLA가 위약금과 함께 latency 명시 |
| 토큰 · 코드 줄 수 · tier 이름 · 화면 크기 | 조건 없이 결정 숫자 ✗ |

| 오답 | 이유 |
|---|---|
| 구축 비용 누락 | 가장 흔한 비즈니스 케이스 오류 |
| 오류 항목 누락 | 이 사례는 작지만 다른 사례는 지배적 |
| "전략적으로 중요" · "비용은 늘 떨어짐" | 가격 매긴 항목 ✗ · 구호 · 희망 |
| 음수인데 더 작은 파일럿 | 수치가 이미 측정됨 → 지연일 뿐 |
| 첫해 순가치에 월 절감만 | 일회성 비용 · 1년 기간 무시 |

| 선택지 | 정답이 되는 조건 |
|---|---|
| 구축 | 오류 · 매출 항목이 순가치를 양수로 전환 |
| 파일럿 | 기준선을 모를 때 |
| "비용은 떨어진다" | 더 낮은 실행비를 보이는 서명된 벤더 견적 |
| 범위를 좁힌 사례 | 식이 바뀌므로 별도로 계산 |
<sub>근거: CCAR-P-jrajath94-0127, CCAR-P-jrajath94-0128, CCAR-P-jrajath94-0287, CCAR-P-jrajath94-0341, CCAR-P-jrajath94-0342, CCAR-P-jrajath94-0404, CCAR-P-jrajath94-0405, CCAR-P-jrajath94-0467, CCAR-P-jrajath94-0530</sub>

@@ NEW-SECTION
### 가치 유형 · 우선순위 · 비즈니스 케이스
**유형이 지표를 정하고 가격 매긴 항목이 우선순위를 정함**

| 가치 유형 | 의미 |
|---|---|
| 효율성 | 같은 일을 더 싸게 (절반 인력 시간으로 같은 송장) |
| 생산성 | 같은 인력으로 더 많은 일 |
| 전환(transformation) | 이전에 불가능했던 일을 수행 |
| 품질 | 오류 감소 · 회피된 벌금 = 오류 비용 항목 |
| 속도 | 지연 시간 = 식에 대한 SLO guard (품질 ✗) |
| 후속 조치 | 유형 명명 = 첫 단계 · 지표 · 임계값 · 담당자 필요 |

| 문항 | 가치 분류 |
|---|---|
| CFO 비즈니스 케이스 | 효율성 · 비용 · 생산성 · 성과 |
| 결과 유형 분류 | 효율성 · 생산성 · 전환 · 품질 |

| 상황 | 정답 | 이유 |
|---|---|---|
| CFO가 비즈니스 케이스 요청 | 솔루션을 가치 기둥에 숫자로 매핑<br>(계약당 절감 시간 · 검토당 비용 전후<br>· 오류율 감소 · 회수 기간) | CFO의 언어 = 숫자 |
| 고정 예산 · 개선 2안 중 1개 | 가격 매긴 가치 항목이 큰 쪽 | 가치 동인이 결정 |
| 효율성 · 비용 기둥 · 3개월 내 측정 · 저위험 안<br>vs 12개월 · 불확실한 수익 안<br>+ 공식 전략 = 비용 규율 | 전략에 맞는 안 선택<br>+ 두 안의 가치 · 비용 · 위험 · 가치 실현 시간 정량화 | 방어 가능한 선택 = 증거 기준 |
| 기준선 미측정 · 이번 주 구축 결정 압박 | 고정 범위 파일럿 → 순가치 → 결정<br>(SKU 집합 · 기간 · 성공 기준 고정) | 없는 숫자에서 뺄셈 ✗<br>범위 미고정 = 느린 구축 |
| 아무도 기다리지 않는 야간 배치의 latency 단축 | 가치 없는 움직임 | 질문 = 그 개선이 무엇을 버는가 |

| 오답 | 이유 |
|---|---|
| 한 분기 안에 완전 변혁 약속 | 측정 불가 = 과대 광고 |
| 아키텍처 우아함 · 최신 모델 강조 | 가치 기둥 아님 · 구현 세부 |
| 지연 시간이 체감된다는 이유로 선택 | 가격 매긴 항목 ✗ · 오류 $500,000 대비 열세 |
| 예산 균등 분할 | 미완성 프로젝트 둘 |
| 둘 다 아니다 | 가격 매긴 $500,000 항목 무시 |
| 변혁은 항상 효율성을 이김 | 구호 · 공식 전략과 측정 가능성 무시 |
| 둘 다 절반 예산 | 우선순위 결정 회피 · 둘 다 부족 |
| 벤더 레퍼런스 고객으로 대체 · 롤아웃 중 측정 | 데이터 · SKU · 비용이 다름 · 지출 먼저 |
| "AI에게 너무 어렵다"며 거절 | 느낌으로 결정 · 식이 예일 수 있음 |
| 지연 시간 단축을 축하 · 더 줄임 · 더 큰 모델 | 가치 근거 없는 최적화 |

| 선택지 | 정답이 되는 조건 |
|---|---|
| latency 개선 선택 | 가격 매긴 churn 항목이 지연과 연결 |
| 예산 균등 분할 | 두 개선을 모두 출시할 만큼 저렴 |
| "둘 다 아니다" | 오류 비용이 $500이 아닌 $5 |
| 야간 배치 latency 단축 | 작업이 아침 근무조를 막는 경우 |
<sub>근거: CCAR-P-jrajath94-0014, CCAR-P-jrajath94-0022, CCAR-P-jrajath94-0129, CCAR-P-jrajath94-0130, CCAR-P-jrajath94-0131, CCAR-P-jrajath94-0468</sub>

@@ RULES
| 매일 바뀌는 대규모 지식 기반 Q&A | 갱신되는 index 검색 + 검색 context 답변 |
| 단일 턴 · 월 갱신 문서 · 인용 필요 | augmented LLM (retrieval + 단일 호출) |
| 안정적 고정 카테고리 분류 | classifier (fine-tuned · 규칙 기반) |
| 형태가 다른 잘 알려진 두 문제 | 단순 구성요소 둘 · 각자 지표로 평가 |
| 두 설계가 요구사항을 충족 | 추가 capability 필요성 vs 복잡성 비용으로 결정 |
| 과잉 설계 판별 | 요구사항에 의존하지 않는 구성요소 존재 |
| 전체 프로세스 자율화 요청 | 책임 수반 결정 중 사람에게 남길 것부터 확인 |
| 규제 통제가 모델 동작에 의존 | 모델 밖에서 결정론적 강제 |
| "가능한 한 정확하게" 요구 | 필요 정확도 + 오류 비용 구체화 |
| 절대 일어나서는 안 되는 조건 식별 | hard constraint = gate · 나머지 = 목표 + 담당자 |
| 규제 하 build vs buy | 통제 · 결합도 평가 · 기능 수 부차적 |
| 돈 · 승인 규칙이 걸린 요청의 첫 행동 | 제약 기록 → 입력 형태로 분기 → 코드 gate |
| 완전한 end-to-end 설계 | 입력 · 처리 · 출력 · 피드백 루프 |
| 평점이 쌓이는데 품질 불변 | 샘플링 → eval 추가 → 수정 검토 → 개선분 배포 |
| 단계 관찰 + 실패 청구 유실 방지 | 단계 경계 · typed 결과 · 사람 대기열 · handoff 로깅 |
| 6개월 뒤 재현 가능한 감사 | gate를 코드에 배치 + request ID 하나의 trace |
| verification 통과 후 오답 사고 | trace로 실패 gate 지목 → 그 구성요소 수정 |
| 신뢰 경계 식별 | 조작 가능 입력 진입점 · side effect 직전 |
| 자기 보고 vs 기계 기록 충돌 | 기계 기록 원장 = system of record |
| verification 배치 | 모델 이후 · side effect 이전 · 되돌림 여부로 강도 결정 |
| 정확도 동률 · SLA · 비용 제약 명시 | 제약을 충족하는 설계 선택 |
| 부하 10배 급증에도 SLA 유지 | autoscaling + degraded mode<br>+ SLA에 저하 동작 명시 |
| 구축 여부 결정 | 순가치 공식 (구축 · 오류 · 고정비 · 물량 포함) |
| 순가치가 음수 | 구축 ✗ · 범위를 좁혀 재계산 |
| 비용 절감 · 상위 tier 제안 | 순가치 vs 놓친 손실 · quality floor |
| 기준선 미측정 | 고정 범위 파일럿 → 순가치 → 결정 |
| 고정 예산 · 개선안 2개 | 가격 매긴 가치가 큰 쪽 |
| 전략 · 증거 기준 충돌 | 공식 전략 부합 안 + 정량화 증거 요구 |
| CFO 설득 | 가치 기둥 + 숫자 (시간 · 비용 · 오류율 · 회수) |
| 결과의 가치 유형 분류 | 효율성 · 생산성 · 전환 · 품질 |
| 가치 근거 없는 기술 개선 | 가치 없는 움직임으로 판정 |
<sub>근거: CCAR-P-Amey-Thakur-0004, CCAR-P-Amey-Thakur-0016, CCAR-P-Amey-Thakur-0017, CCAR-P-Amey-Thakur-0018, CCAR-P-Amey-Thakur-0019, CCAR-P-Amey-Thakur-0036, CCAR-P-Amey-Thakur-0054, CCAR-P-Amey-Thakur-0055, CCAR-P-Amey-Thakur-0056, CCAR-P-Amey-Thakur-0069, CCAR-P-jrajath94-0014, CCAR-P-jrajath94-0017, CCAR-P-jrajath94-0019, CCAR-P-jrajath94-0020, CCAR-P-jrajath94-0022, CCAR-P-jrajath94-0068, CCAR-P-jrajath94-0108, CCAR-P-jrajath94-0109, CCAR-P-jrajath94-0111, CCAR-P-jrajath94-0112, CCAR-P-jrajath94-0113, CCAR-P-jrajath94-0127, CCAR-P-jrajath94-0128, CCAR-P-jrajath94-0129, CCAR-P-jrajath94-0130, CCAR-P-jrajath94-0131, CCAR-P-jrajath94-0287, CCAR-P-jrajath94-0288, CCAR-P-jrajath94-0332, CCAR-P-jrajath94-0333, CCAR-P-jrajath94-0334, CCAR-P-jrajath94-0335, CCAR-P-jrajath94-0341, CCAR-P-jrajath94-0342, CCAR-P-jrajath94-0395, CCAR-P-jrajath94-0396, CCAR-P-jrajath94-0397, CCAR-P-jrajath94-0398, CCAR-P-jrajath94-0404, CCAR-P-jrajath94-0405, CCAR-P-jrajath94-0458, CCAR-P-jrajath94-0459, CCAR-P-jrajath94-0460, CCAR-P-jrajath94-0461, CCAR-P-jrajath94-0467, CCAR-P-jrajath94-0468, CCAR-P-jrajath94-0522, CCAR-P-jrajath94-0526, CCAR-P-jrajath94-0530, CCAR-P-jrajath94-0531, CCAR-P-preporato-0001, CCAR-P-preporato-0002, CCAR-P-preporato-0003</sub>

@@ TRAPS
| 공통 문서 처리를 근거로 단일 시스템<br>· 단일 agent · fine-tuned 모델 하나 | 아키텍처 논거 ✗ · 위험 결합 · 가장 비싼 경로 |
| 갱신 지식을 fine-tune · system prompt에 적재 | 갱신 지식 = 검색의 몫 |
| 단순한 요구에 자율 agent · multi-agent | 불필요한 자율성 → 비용 · 지연 |
| 고정 카테고리 분류에 RAG | 필요한 것 = 동작 · 토큰만 추가 |
| 더 능력 있는 설계 · 선호 · 추측 유연성 | 정당화 없이 복잡성 비용 지불 |
| 높은 정확도 · 더 큰 모델 · 면책 · 문서화로 통제 대체 | 경향 ≠ 보장 |
| 모델 · 비용 · 일정부터 확인 | 책임 경계의 하위 문제 |
| 테스트 성능 · 예산 · 고객 요청이 자동화 경계 | 책임 문제를 다루지 않음 |
| 최대 성능을 기본값으로 · 가장 복잡한 설계 · 파일럿 뒤로 미룸 | 목표 없는 비용 · 기준점 없음 |
| 모든 요구사항을 hard constraint로 취급 | hard = gate · 목표 = 임계값 + 담당자 |
| 기능 수 · 라이선스 비용 · 팀 숙련도로 build vs buy 결정 | 규제 · lock-in · 종료 비용이 결정 |
| 돈 · 컴플라이언스 규칙을 system prompt에 위임 | prompt = guidance · gate 실행 증명 ✗ |
| 제약 기록 전 구축 · tier 벤치마크 | 잘못된 첫 질문 |
| 점검 없는 단일 agent · 전건 사람 검토 | gate 없음 · 대량 처리 불가 |
| 처리량 대시보드 · 최상위 모델 · 평점 수집만 | 피드백 루프 부재 · 활동 ≠ 품질 |
| 단계 합치기 · 같은 모델 균일성 · 완전 자율 | 관찰 불가 · 사람 라우팅 위반 |
| prompt 로그 · 사람 승인 = trace<br>· 두 번째 모델 호출 = verification | 원본 chunk · 검사 기록 부재 |
| sampler 설정 · GPU region · 로그 양 확대 | 승인 hop · 검사 record 지목 ✗ |
| 검증 통과 = 정답으로 간주 · 상위 tier · 형식 regex | 원본이 낡으면 통과 · 실패 구성요소 아님 |
| 내부 신뢰 경유 · mutual TLS · 로그 저장을 경계로 | 경계 = 입력 진입 · side effect |
| 판매자 문자 · 최근 보고 · 모델 혼합을 재고 기준으로 | 신뢰 · 검증 ✗ |
| 접수 전 · 통지 후 · 없음으로 verification | 판단할 것을 검토 ✗ · 피해 후 |
| 최상위 tier 고집 · 평균 부하 + queue<br>· 피크 시 비활성화 | SLA 우선순위 위반 |
| 단위당 절감 · 토큰 · tier 이름이 결정 | 순가치 아님 |
| 구축비 · 오류 항목 누락 | 가장 흔한 케이스 오류 |
| "전략적" · "비용은 떨어짐"으로 음수 정당화 | 가격 매긴 항목 ✗ |
| 절감 비율 · 2% 향상만으로 tier 결정 | 순가치 · quality floor 미반영 |
| 변혁 약속 · 우아함 · 최신 모델로 CFO 설득 | 숫자 · 가치 기둥 부재 |
| 예산 분할 · 쉬운 지표 우선 · 변혁 구호 | 미완성 · 가격 매긴 항목 무시 |
| 벤더 레퍼런스 · 구축 후 측정으로 기준선 대체 | 지출 선약정 |
| 유형 혼동 (벌금 = 생산성 · 속도 = 품질 · 새 역량 = 효율성) | 정의로 분류 |
| 가치 근거 없는 latency 최적화 | 아무도 대기하지 않음 |
<sub>근거: CCAR-P-Amey-Thakur-0004, CCAR-P-Amey-Thakur-0016, CCAR-P-Amey-Thakur-0017, CCAR-P-Amey-Thakur-0018, CCAR-P-Amey-Thakur-0036, CCAR-P-Amey-Thakur-0054, CCAR-P-Amey-Thakur-0055, CCAR-P-Amey-Thakur-0056, CCAR-P-Amey-Thakur-0069, CCAR-P-jrajath94-0014, CCAR-P-jrajath94-0017, CCAR-P-jrajath94-0019, CCAR-P-jrajath94-0020, CCAR-P-jrajath94-0022, CCAR-P-jrajath94-0068, CCAR-P-jrajath94-0108, CCAR-P-jrajath94-0109, CCAR-P-jrajath94-0111, CCAR-P-jrajath94-0112, CCAR-P-jrajath94-0113, CCAR-P-jrajath94-0127, CCAR-P-jrajath94-0128, CCAR-P-jrajath94-0129, CCAR-P-jrajath94-0130, CCAR-P-jrajath94-0131, CCAR-P-jrajath94-0287, CCAR-P-jrajath94-0288, CCAR-P-jrajath94-0332, CCAR-P-jrajath94-0333, CCAR-P-jrajath94-0334, CCAR-P-jrajath94-0335, CCAR-P-jrajath94-0341, CCAR-P-jrajath94-0342, CCAR-P-jrajath94-0395, CCAR-P-jrajath94-0396, CCAR-P-jrajath94-0397, CCAR-P-jrajath94-0398, CCAR-P-jrajath94-0404, CCAR-P-jrajath94-0405, CCAR-P-jrajath94-0458, CCAR-P-jrajath94-0459, CCAR-P-jrajath94-0460, CCAR-P-jrajath94-0461, CCAR-P-jrajath94-0467, CCAR-P-jrajath94-0468, CCAR-P-jrajath94-0522, CCAR-P-jrajath94-0526, CCAR-P-jrajath94-0530, CCAR-P-jrajath94-0531, CCAR-P-preporato-0001, CCAR-P-preporato-0002, CCAR-P-preporato-0003</sub>

@@ MEMO
| hard constraint | 절대 일어나서는 안 되는 조건 · gate로 강제 · 위반 시 직접 손실 |
| 목표 | 임계값 + 담당자 · 위반 시 지연 · 사업 결정 |
| 결정론적 lane | 정형 입력을 규칙 · 파서로 처리하는 경로 |
| code gate | 위험 행동 직전의 코드 검사 · prompt 지시와 구별 |
| 다섯 고리 체인 | 성과 · 기능 · 수치 · 한계 · 적합성 (건너뛰고 구축 ✗) |
| augmented LLM | retrieval + 단일 모델 호출 + 인용 |
| 7 gate | input · validation<br>context and retrieval · model and tools<br>verification · output · feedback |
| trace 내용 | input hash · chunk ID · 초안 · 검사 결과 |
| request ID | 모든 hop의 trace를 연결하는 하나의 ID |
| system of record | 사실의 신뢰 원본<br>(POS 원장 · EHR · HR 시스템 · 신용평가기관) |
| trust boundary | 조작 가능 입력 진입 · side effect 직전 |
| degraded mode | 부하 초과 시 정의된 저하 동작 · SLA에 명시 |
| quality floor | 결정에서 넘어서는 안 되는 품질 하한 |
| 순가치 | (기준선 − 새 비용) × 물량 + 회피 오류 − 구축 · 운영 |
| 가치 유형 | 효율성 · 생산성 · 전환 · 품질 |
| 가치 기둥(CFO 문항) | 효율성 · 비용 · 생산성 · 성과 |
| 피드백 루프 4단 | 샘플링 · eval 추가 · 수정 검토 · 개선분 배포 |
<sub>근거: CCAR-P-jrajath94-0014, CCAR-P-jrajath94-0017, CCAR-P-jrajath94-0019, CCAR-P-jrajath94-0108, CCAR-P-jrajath94-0109, CCAR-P-jrajath94-0111, CCAR-P-jrajath94-0112, CCAR-P-jrajath94-0127, CCAR-P-jrajath94-0129, CCAR-P-jrajath94-0288, CCAR-P-jrajath94-0334, CCAR-P-jrajath94-0397, CCAR-P-jrajath94-0398, CCAR-P-jrajath94-0405, CCAR-P-jrajath94-0461, CCAR-P-jrajath94-0531, CCAR-P-preporato-0001</sub>

@@ CHECK
- [ ] 갱신 지식 = 검색 · 고정 동작 = classifier · 복잡성은 요구사항으로만
- [ ] 책임 소재 = 자동화 경계 · 필수 통제 = 모델 밖 코드 gate
- [ ] 첫 행동 = 제약 기록 → 입력 분기 → 코드 gate
- [ ] 완전한 설계 = 입력 · 처리 · 출력 · 피드백 루프
- [ ] 경계 = 입력 진입 · side effect 직전 · verification은 그 사이
- [ ] 정확도 동률이면 SLA 결정 · 순가치는 전 항목 반영 · 음수면 구축 ✗
<sub>근거: CCAR-P-Amey-Thakur-0004, CCAR-P-Amey-Thakur-0016, CCAR-P-Amey-Thakur-0017, CCAR-P-Amey-Thakur-0018, CCAR-P-Amey-Thakur-0019, CCAR-P-Amey-Thakur-0036, CCAR-P-Amey-Thakur-0054, CCAR-P-Amey-Thakur-0055, CCAR-P-Amey-Thakur-0056, CCAR-P-jrajath94-0017, CCAR-P-jrajath94-0019, CCAR-P-jrajath94-0020, CCAR-P-jrajath94-0108, CCAR-P-jrajath94-0109, CCAR-P-jrajath94-0111, CCAR-P-jrajath94-0112, CCAR-P-jrajath94-0127, CCAR-P-jrajath94-0128, CCAR-P-jrajath94-0131, CCAR-P-jrajath94-0288, CCAR-P-jrajath94-0333, CCAR-P-jrajath94-0334, CCAR-P-jrajath94-0335, CCAR-P-jrajath94-0396, CCAR-P-jrajath94-0398, CCAR-P-jrajath94-0459, CCAR-P-jrajath94-0461, CCAR-P-jrajath94-0522, CCAR-P-jrajath94-0526, CCAR-P-preporato-0001, CCAR-P-preporato-0002, CCAR-P-preporato-0003</sub>
