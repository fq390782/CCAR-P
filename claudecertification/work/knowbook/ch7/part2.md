@@ ADD-TO: ### 1.4 Human-in-the-loop (approval gate)

**gate = 행동 전 · 실제 컨텍스트 · 기록**

| 구분 | 내용 |
|---|---|
| 삭제 기능 유지 필요 | 3겹 조합: 확인 gate · dry-run · 최소 권한 범위<br>→ 모델 단일 실수 ≠ 비가역 삭제 |
| 3겹의 역할 | 확인 gate = 단일 실수의 실행 차단<br>dry-run = 실행 전 영향 범위 표시<br>최소 권한 = 도구 도달 범위 제한 |
| 승인 시점 | 행동 전(pre-action)만 유효<br>post-action 검토 = 이미 실행된 뒤 ✗ |
| 규제가 사람 승인 요구 | 3요소 모두 충족<br>① 행동 전 ② 이름 명시된 면허 검토자<br>③ 결정 logging |
| 검토자에게 줄 정보 | 승인 버튼만 ✗<br>실제 의사결정 컨텍스트(신청서 · 확인 결과 · 명령) |
| 검토 강도 결정 | 결과 · 가역성 · 규제에 맞춤<br>의무가 가장 먼저, 그다음 측정된 비율 |
| 운영 조건 | 검토자 배치 · 순환 · 세션 상한<br>없으면 gate = 도장 찍기<br>대기열 SLA 필요 → 처리 지연 감수 |
| 전건 사람 검토 | 일일 건수가 많으면 실현 ✗<br>소량 · 극단적 위험일 때만 성립 |
| 구현: Managed Agents | `always_ask` permission policy<br>= 도구 실행 전 세션 일시 중지<br>→ 리뷰어 응답까지 대기 |

**상황별 검토 형태**

| 상황 | 검토 형태 |
|---|---|
| 비가역 + 보호 대상 파괴 (철거 허가) | 전체 컨텍스트 갖춘 pre-action 승인 |
| 서명 · 계약 구속 | pre-action 승인(전체 컨텍스트) |
| 법적 책임 문서 (해고 통지서) | pre-action 승인(전체 컨텍스트) |
| 지연 = 피해 (의료 triage 권고) | pre-action 검토 + 실제 컨텍스트 |
| 비가역 삭제 + 판정 가끔 오류 | fail-closed 검사 + pre-action 승인<br>logging = 보완책일 뿐 |
| 사용자 명의 발송 + 수신자 모호 | 추측 발송 ✗ → 거부 · 확인 |
| 가역 · 저위험 · 정보성 | post-action 검토로 충분 |

| 오답 | 이유 |
|---|---|
| 규제 의무에 post-action 검토 | 의무 = 행동 전 승인<br>이미 노출 · 실행 뒤 |
| 규제 요건을 prompt 지침 · 문구로 충족 | 규제 = 문장 ✗, 사람 요구<br>문구 ≠ 면허 |
| 삭제 도구에 rate limit | 속도만 늦춤<br>잘못된 삭제 1회 못 막음 |
| 필요한 삭제 기능 제거 | 통제 ✗ → 필요 기능 소멸 |
| 승인 후 logging만 배치 | 손실 기록일 뿐 → 단독 대책 ✗ |
| 연 단위 통계 검토 | 개별 철거 · 삭제 못 막음 |
| status idled webhook을 일시 중지 제어로 사용 | webhook = 통지 수단<br>일시 중지는 `always_ask`가 수행 |

<sub>근거: CCAR-P-jrajath94-0036, CCAR-P-jrajath94-0207, CCAR-P-jrajath94-0220, CCAR-P-jrajath94-0317, CCAR-P-jrajath94-0377, CCAR-P-jrajath94-0436, CCAR-P-jrajath94-0441, CCAR-P-jrajath94-0499, CCAR-P-jrajath94-0504, CCAR-P-jrajath94-0677</sub>

@@ NEW-SECTION
### Fail-closed 기본값 (검사 불능 시 거부)
**검사를 못 하면 위험 행동은 거부**

| 구분 | 내용 |
|---|---|
| 원칙 | 보안 제어는 backing service 중단 시 거부<br>보안 제어에서 가용성 = 부차적 |
| 기본값의 비용 | fail-closed = 지연 · 정상 요청 손실<br>fail-open = 금전 · 피해 |
| fail-closed 대상 | 돈 이동 authorization gate<br>신뢰 불가 입력 screener<br>구매 · 개인 데이터(이메일) 접근 |
| fail-open 함정 | sandbox · input screener를 가동시간 위해 허용 전환<br>→ 중단 = 공격 창 |
| 적용 제외 | 사용량 대시보드 = 제어 ✗<br>→ fail-closed 대상 아님 |
| 모호한 입력 | 추측 ✗ → 거부<br>(귀속 · 비가역 행동 + 모호 → 거부) |
| 한도 gate 설계 | 정책 = 모델 밖 코드<br>도구 실행 전 검사 · 중단 시 거부<br>양방향 screening (호출마다 지연 추가) |
| prompt에 한도 기재 | injection이 prompt를 덮어씀<br>→ 중단 · 공격 시 보장 ✗ |
| 복구 경로 | 대기열 → 복구 시 비움<br>격리 경로 → 폐기 메시지 검토 |
| 숨은 의존성 | sandbox가 도구를 실제로 가둠<br>복구 시 대기열 정상 소진 |
| 한계 | 중단 중 정상 payout 지연 · 정상 메시지 폐기<br>→ 알림으로 중단 해소 단축 |

<sub>근거: CCAR-P-jrajath94-0207, CCAR-P-jrajath94-0209, CCAR-P-jrajath94-0373, CCAR-P-jrajath94-0436</sub>

@@ NEW-SECTION
### 위험 평가 (출시 전 테스트 · 등록부 · 실패 모드)
**출시 전 = 공격 테스트 + 잔여 위험 등록**

| 구분 | 내용 |
|---|---|
| 안전 계획 2요소 | red team + risk register |
| red team | 안전 통제를 적극 공격<br>(금지 요청 거절 · 내부 데이터 보호 · 적대 사용자 앞 역할 유지) |
| risk register | 잔여 위험을 심각도 · 승인과 함께 기록<br>출시 후 발견 ✗ → 관리되는 결정으로 전환 |
| 역할 분담 | 테스트 = 구멍 발견<br>register = 구멍을 관리 결정으로 변환 |
| 실패 모드 식별 | 도구 조합 + 감독 유무로 판단 |
| 전사 이메일 도구 | 피해 범위(blast radius) = 회사 전체 |
| 파일 접근 + 이메일 도구 | 결합 시 데이터 유출 경로 |
| 무감독 야간 실행 | 위 두 위험을 배가 |
| 무관한 항목 | 어조 개선 · 신뢰성 활동 · 외형적 항목<br>→ 안전성 제약과 무관 |

<sub>근거: CCAR-P-jrajath94-0041, CCAR-P-jrajath94-0376</sub>

@@ NEW-SECTION
### 위험별 통제 · incident 대응 · kill switch
**위험마다 예방 · 탐지 · 복구를 짝지음**

| 위험 | 통제 |
|---|---|
| 비용 고갈 (루프 폭주) | 예방 = 호출 · 지출 상한<br>탐지 = 지출 알림(상한보다 먼저) |
| 벤더의 무고지 모델 버전 변경 | 예방 = 버전 고정<br>탐지 = 회귀 실행(refusal · 정책 사례 포함)<br>복구 = 롤백(실제 테스트) |
| 서드파티 MCP server<br>(비공개 · 광범위 읽기 · 조용한 업데이트) | 예방 = 버전 고정 + 파일 접근 범위 한정<br>탐지 = 업데이트별 검토 |
| 과도한 agency (계획 밖 도구 호출) | 복구 = 실행 종료 + 세션 revoke |
| 간접 주입 (검색 context 속 지시) | 복구 = 출처 격리 + 담당자 알림 |
| 팀 단위 월 hard 한도 | 별도 workspace + 자체 spend limit |

**Incident 대응 순서**

1. 종료: 진행 중인 run 중지
2. revoke: 세션 + 캐시된 credential 무효화
3. 격리: 주입 출처를 포렌식용으로 보존한 채 분리
4. 알림: 담당자에게 통지

| 구분 | 내용 |
|---|---|
| 상한 값 | 정당한 작업의 측정된 최대치 위로 설정<br>둥근 숫자 ✗ → 정당 작업 중단 = 자초한 장애 |
| 알림 | 상한보다 먼저 울림<br>행동할 담당자 필요 |
| 작업 도중 중단 | 고유한 피해 범위 존재 → 먼저 측정 |
| 월 hard 한도 | 별도 workspace의 spend limit<br>한도 도달 → 해당 팀 요청 중단 |
| ⚠️ Default Workspace | 해설: spend limit 불가<br>공식 문서: 불가 = Google Cloud · AWS 플랫폼 한정<br>Console은 설정 가능하나 일부 사용 미집계 |
| rate limit | 분당 요청 수 제어 ≠ 월 지출 제어 |
| 사용량 보고서 | 현황 확인용 → 사용 중단 ✗ |
| 사고 대응의 본질 | 대응 = 종료 · revoke · 격리 · 알림<br>더 나은 모델 · tier 업그레이드 ✗ |
| 한계 | 버전 고정 = 새 모델 채택 지연 · 회귀 suite 유지보수<br>업데이트 검토 = 기능 출시 지연<br>run 종료 = 정당한 진행 작업 중단 가능 |
| 격리 비용 | 분석가 시간 필요 → 대안보다 나음 |
| 버전 변경 감지 | 벤더 변경 로그 ✗ → 팀 자체 회귀 실행 |

<sub>근거: CCAR-P-jrajath94-0213, CCAR-P-jrajath94-0214, CCAR-P-jrajath94-0215, CCAR-P-jrajath94-0321, CCAR-P-jrajath94-0585</sub>

@@ NEW-SECTION
### 감사 증거 · 추적성 (audit log)
**감사인은 정책이 아니라 기록물을 요구**

| 구분 | 내용 |
|---|---|
| 증거의 조건 | 실제 실행을 보여 주는 산출물<br>정책 · 안내문 · 주장 ✗ |
| 보존 통제 증거 | 삭제 log(월간) + 접근 검토(분기)<br>= 주기를 갖춘 증거 사슬 |
| 증거 아닌 것 | 앱 내 안내문 → 실행 증명 ✗<br>암호화 인증서 → 삭제 증명 ✗<br>가동률 → 보존 증명 ✗ |
| log 보호 | 변조 방지 필수<br>삭제 log 자체도 민감 → 별도 접근 통제 |
| 결정 재생(replay) | trace에 입력 · 담당자 · 버전 기록<br>+ 분기별 재실행 |
| 사람 승인 기록 | 이름 명시된 검토자 + 결정 logging |
| 자체 key(CMEK) + 읽기 기록 + 키 폐기 후 감사 기록 | CMEK를 첫 요청 전에 설정 → 이후 새 데이터 전부 포괄<br>Activity Feed = 누가 무엇을 읽었는지 기록<br>Anthropic 키 아래 → 키 폐기 후에도 유지 |
| CMEK 적용 시점 | 적용 후 기록된 데이터만 보호<br>이전 데이터 재암호화 ✗ |

<sub>근거: CCAR-P-jrajath94-0220, CCAR-P-jrajath94-0223, CCAR-P-jrajath94-0229, CCAR-P-jrajath94-0682</sub>

@@ NEW-SECTION
### 공정성 평가 (bias · 하위 그룹 측정)
**합산 수치는 그룹 격차를 가림 → 그룹별 측정**

| 구분 | 내용 |
|---|---|
| 평가 단위 | 집계 ✗ → 하위 그룹별<br>(채용 · 대출 · 만족도 등 사람에 영향) |
| 집계 함정 | 전체 90% = 그룹 하나 68% 가림<br>전체 목표 충족 + 그룹 격차 공존<br>전체 균형 + 한 그룹 절반 비율 |
| 출시 gate | 그룹별 기준선(하한) 미달 그룹 있으면 출시 차단<br>하한선 = 비즈니스 · 법무 승인 필요 |
| 수정 위치 | 상류: 데이터 · rubric · prompt<br>feedback loop도 상류<br>집계 값 튜닝 ✗ (전체 점수만 이동) |
| 원인 규명 | 데이터 감사 → 학습 데이터 · label · rule 중 위치 확인<br>→ 원인에 수정 |
| 민감 필드 1개 제거 | 편향 제거 ✗ → 가정은 rubric · 데이터에 존속 |
| 블라인딩 | 명백한 proxy만 제거<br>표현 방식 · 경력 공백 · 우편번호는 잔존<br>→ 측정 없이 효과 확인 ✗ |
| 데이터 증량 | 편향 제거 ✗ → 기존 패턴 고착 가능 |
| 그룹 · label 삭제 | 격차 그대로 + 측정 불가 → 더 나쁨 |
| 소표본 그룹 | noisy score → 불확실성(구간) 보고<br>+ 표본 확대 후 기준선이 구속 |
| 소표본 대응 비용 | 시간 · 라벨링 노력 → 출시 대기 = 정직한 기준선의 대가 |
| confidence 점수 | 미보정 · 공정성과 무관 → 공정성 신호 ✗ |
| 부수 조건 | 하위 그룹 label = 프라이버시 처리<br>재라벨링 노력 필요 |

**채용 공정성 설계 (선별 · 순위)**

| 요소 | 역할 |
|---|---|
| 블라인딩 | 명백한 proxy 제거 |
| 고정 rubric | 직무 관련 기준 강제 |
| 기록된 점수 | 결정 감사 가능 |
| 불균등 영향 분석 | 공정성을 데이터로 검증<br>(가정 ✗) |

**벤더 · 릴리스 검증**

| 상황 | 요구 증거 |
|---|---|
| 벤더의 "편향 없는 AI" 홍보 | 대표성 있는 데이터의 집단별 adverse-impact ratio<br>= 검증 · 세분화된 증거 |
| 릴리스 검토: 사용자 그룹별 작동 증거 | 그룹별 평가 + 하한선<br>한 그룹이라도 실패 → 릴리스 차단 |
| 릴리스 검토: 사용 모델 확인 | 시스템 카드 + 정확한 모델 ID로 문서화 |

<sub>근거: CCAR-P-jrajath94-0039, CCAR-P-jrajath94-0091, CCAR-P-jrajath94-0227, CCAR-P-jrajath94-0228, CCAR-P-jrajath94-0230, CCAR-P-jrajath94-0319, CCAR-P-jrajath94-0444, CCAR-P-jrajath94-0507, CCAR-P-jrajath94-0570, CCAR-P-jrajath94-0685</sub>

@@ NEW-SECTION
### 투명성 · AI 고지 · 이의 신청
**고지 · 검증 · 구제를 모두 갖춘 투명성**

| 제약 | 대응 요소 |
|---|---|
| 사용자가 AI임을 앎 | 사전 고지 |
| 답변 주장을 검증 | 주장별 인용 |
| 틀린 답변에 구제 | 이의 신청 경로 |

| 구분 | 내용 |
|---|---|
| 책임 있는 AI 요구 | 투명성 · 설명 가능성 · 책임성 · 추적 가능성<br>결정을 그 요인에 연결 → 불투명 ✗ |
| 결정 거절 시 | 신청자에게 결정 + 실제 요인 + 버전 + 참조 제공 |
| 고지와 trace | 고지는 trace에서 생성<br>trace와 별개로 생성 ✗ |
| 설명의 조건 | trace가 뒷받침하는 이유만 진술<br>trace 밖 이유 = 이유 ✗ |
| 지어낸 설명 | 없는 것보다 나쁨<br>(입력에 없는 수치 인용 등) |
| 지어낸 설명의 수정 | 텍스트를 trace에 묶는 인용 규칙<br>근거 없으면 출시 차단<br>모든 설명에 연결 검사 실행 (일회성 감사 ✗) |
| 한계 | 검사 = 설명당 비용 추가<br>신청자가 요인 해석 못 하면 오해<br>→ 쉬운 언어 필요 |
| 짧은 참 vs 긴 허구 | 짧은 참인 이유가 우위 |

<sub>근거: CCAR-P-jrajath94-0042, CCAR-P-jrajath94-0229, CCAR-P-jrajath94-0231, CCAR-P-jrajath94-0381</sub>

@@ RULES
| 비가역 행동(삭제 · 철거 · 서명) 앞 검토 형태 | 전체 컨텍스트 갖춘 pre-action 승인<br>post-action 검토 ✗ |
| 삭제 기능은 유지, 단일 실수는 막아야 함 | 확인 gate + dry-run + 최소 권한 범위 |
| 규제가 "사람 승인" 요구 | 행동 전 + 이름 명시 면허 검토자 + 결정 logging |
| 한도 정책 서비스 중단 중 공격자의 큰 금액 지시 | 모델 밖 코드 gate가 중단 시에도 거부 (fail-closed) |
| 하루 수천 건 행동의 승인 설계 | 코드 한도 gate 자동 + 한도 초과분만 사람<br>전건 사람 검토 ✗ |
| 중단 시 fail-closed 대상 선택 | 돈 이동 gate · 신뢰 불가 입력 screener<br>구매 · 이메일 접근 범위<br>대시보드 ✗ |
| 수신자 · 대상이 모호한 비가역 행동 | 추측 실행 ✗ → 거부 · 확인 |
| 무인 실행 loop 비용 폭주 대응 | 측정된 필요치 위 호출 · 지출 상한 + 상한 전 지출 알림 |
| 팀별 월 hard 지출 한도 | 별도 workspace + 자체 spend limit |
| 도구 사고(계획 밖 호출 + 주입 이메일) 대응 | run 종료 + 세션 revoke + 주입 출처 격리 + 알림 |
| 벤더의 무고지 모델 변경 방지 | 버전 고정 + 회귀 실행 + 롤백 준비 |
| 비공개 서드파티 MCP server 도입 | 버전 고정 + 접근 범위 한정 + 업데이트별 검토 |
| 출시 전 안전 계획 2요소 | red team + 잔여 위험 risk register |
| 보존 통제 작동 증거 요구 | 삭제 log + 분기 접근 검토 |
| 모든 결정을 감사자가 replay | 입력 · 담당자 · 버전을 담은 trace + 분기 재실행 |
| 합산 수치는 좋은데 한 그룹이 낮음 | 그룹별 측정 + 하한선 gate + 원인(데이터 · rubric) 수정 |
| 그룹 샘플이 소량 | 불확실성 보고 + 표본 확대<br>기준선 기계 적용 ✗ |
| 채용 선별의 공정성 입증 | 블라인딩 + 고정 rubric + 기록 점수 + 불균등 영향 분석 |
| 벤더의 "편향 없음" 주장 | 집단별 adverse-impact ratio 요구 |
| 공공 서비스 AI 투명성 | 사전 고지 + 주장별 인용 + 이의 신청 경로 |
| 거절 결정에 이유 설명 | trace가 뒷받침하는 실제 요인만 진술 |
| 자체 키 + 키 폐기 후에도 감사 기록 | 첫 요청 전 CMEK + Activity Feed |
<sub>근거: CCAR-P-jrajath94-0036, CCAR-P-jrajath94-0039, CCAR-P-jrajath94-0041, CCAR-P-jrajath94-0042, CCAR-P-jrajath94-0091, CCAR-P-jrajath94-0207, CCAR-P-jrajath94-0209, CCAR-P-jrajath94-0213, CCAR-P-jrajath94-0214, CCAR-P-jrajath94-0215, CCAR-P-jrajath94-0220, CCAR-P-jrajath94-0223, CCAR-P-jrajath94-0227, CCAR-P-jrajath94-0228, CCAR-P-jrajath94-0229, CCAR-P-jrajath94-0230, CCAR-P-jrajath94-0231, CCAR-P-jrajath94-0317, CCAR-P-jrajath94-0319, CCAR-P-jrajath94-0321, CCAR-P-jrajath94-0373, CCAR-P-jrajath94-0377, CCAR-P-jrajath94-0381, CCAR-P-jrajath94-0436, CCAR-P-jrajath94-0441, CCAR-P-jrajath94-0444, CCAR-P-jrajath94-0499, CCAR-P-jrajath94-0504, CCAR-P-jrajath94-0507, CCAR-P-jrajath94-0570, CCAR-P-jrajath94-0585, CCAR-P-jrajath94-0677, CCAR-P-jrajath94-0682, CCAR-P-jrajath94-0685</sub>

@@ TRAPS
| prompt 문구로 한도 · 규제 요건 충족 | 주입이 덮어씀 · 규제 = 문장 ✗ 사람<br>enforcement ✗ |
| 삭제 도구에 rate limit | 속도만 늦춤 → 잘못된 삭제 1회 못 막음 |
| 필요한 기능 자체를 제거 | 통제 ✗ → 업무 기능만 상실 |
| 사후(post-action) 검토로 사전 승인 의무 충족 | 이미 실행 · 노출된 뒤 |
| logging · 통계 검토만 배치 | 손실 기록일 뿐 → 개별 행동 못 막음 |
| status idled webhook을 일시 중지 제어로 착각 | 통지 수단 → 일시 중지는 `always_ask` |
| 중단 중 가용성 우선 (fail-open) | 중단 = 공격 창<br>안전 기본값 비용 = 지연, 불안전 = 금전 |
| 사용량 대시보드 · 월간 청구서 검토를 통제로 취급 | 손실 후 확인 ✗ → 예방 · 중단 불가 |
| 둥근 숫자로 비용 상한 설정 | 측정 필요치 아래 → 정당 작업 중단 |
| 더 빠른 모델 · tier 업그레이드로 비용 · 사고 대응 | 루프 · 주입 출처 그대로<br>대응 = 종료 · revoke · 격리 · 알림 |
| rate limit으로 월 지출 제한 | 분당 요청 수 제어일 뿐 |
| 벤더 변경 로그 · 버전 기록만 믿음 | 감지 ✗ → 팀 자체 회귀 실행 필요 |
| 서드파티 MCP에 가격 협상 · 캐싱 · 모델 업그레이드 | 공급망 위험 미해소 |
| 어조 개선 · 신뢰성 활동을 안전성 테스트로 인정 | 통제를 공격하지 않음 |
| 안내문 · 암호화 인증서 · 가동률을 보존 증거로 제출 | 삭제 실행 증명 ✗ |
| 전체 지표 · 목표 충족을 공정성 증거로 사용 | 집계가 그룹 격차를 가림 |
| 집계 값 튜닝으로 공정성 해결 | 그룹 점수 그대로 → 데이터 문제 |
| 민감 필드 제거 · 데이터 증량으로 편향 해소 | rubric · 데이터에 가정 존속 · 기존 패턴 고착 |
| 그룹 · label 삭제 · 혼합 | 측정 불가 → 피해가 측정 없이 출시 |
| 소표본 그룹에 기준선 그대로 적용 | 노이즈가 출시 결정 |
| 벤더 자체 테스트 요약 · 주당 소수 표본 점검 | 주장 재진술 · 수천 건 통계 격차 탐지 불가 |
| 시스템 카드를 공정성 증거로 인용 | 모델 테스트이지 제품 사용자 테스트 ✗ |
| 하단 label · prompt 공개 · 일반 면책 문구로 투명성 | 검증 · 구제 ✗ → 책임 전가 · 내부 구조 노출 |
| 유창한 · 긴 생성 설명 = 투명성 | trace 근거 없는 이유는 허구<br>가독성 ≠ 정직 |
| 투명성 의무 포기로 허구 설명 해소 | 침묵 ≠ 수정 |
| 첫 요청 후 추가한 CMEK 키로 기존 데이터 보호 | 이전 데이터 재암호화 ✗ |
<sub>근거: CCAR-P-jrajath94-0036, CCAR-P-jrajath94-0039, CCAR-P-jrajath94-0041, CCAR-P-jrajath94-0042, CCAR-P-jrajath94-0091, CCAR-P-jrajath94-0207, CCAR-P-jrajath94-0209, CCAR-P-jrajath94-0213, CCAR-P-jrajath94-0214, CCAR-P-jrajath94-0215, CCAR-P-jrajath94-0220, CCAR-P-jrajath94-0223, CCAR-P-jrajath94-0227, CCAR-P-jrajath94-0228, CCAR-P-jrajath94-0230, CCAR-P-jrajath94-0231, CCAR-P-jrajath94-0317, CCAR-P-jrajath94-0319, CCAR-P-jrajath94-0321, CCAR-P-jrajath94-0585, CCAR-P-jrajath94-0677, CCAR-P-jrajath94-0682, CCAR-P-jrajath94-0685</sub>

@@ MEMO
| Fail-closed | 검사 불능 시 위험 행동 거부<br>fail-open = 중단이 공격 창 |
| Pre-action 승인 | 행동 실행 전 사람 승인<br>post-action 검토와 구분 |
| dry-run | 실행 전 영향 범위 표시 |
| `always_ask` | 도구 실행 전 세션 일시 중지, 리뷰어 응답 대기 |
| Run 종료(kill) | 호출 · 지출 상한 도달 또는 incident 시 실행 중지 |
| Incident 4단계 | 종료 · revoke · 격리 · 알림 |
| 버전 고정 · 회귀 · 롤백 | 공급망 위험의 예방 · 탐지 · 복구 |
| Blast radius | 도구 피해 범위 (예: 전사 이메일 도구) |
| Risk register | 잔여 위험을 심각도 · 승인과 함께 기록 |
| red team | 안전 통제를 적극 공격하는 출시 전 테스트 |
| 하위 그룹 평가 | 집계 아닌 그룹별 측정 + 하한선 |
| proxy 변수 | 블라인딩 후에도 남는 대리 변수<br>(표현 방식 · 경력 공백 · 우편번호) |
| Adverse-impact ratio | 집단별 탈락 비율 증거 (규제 기관 요구) |
| AI 고지 · 주장별 인용 · 이의 신청 | 투명성 3요소 |
| Trace | 결정 입력 · 담당자 · 버전 기록<br>설명 · 고지 · replay의 근거 |
| Activity Feed | 누가 무엇을 읽었는지 기록<br>Anthropic 키 아래 → 키 폐기 후 유지 |
| CMEK | 자체 암호화 키<br>적용 후 기록된 데이터만 보호 |
<sub>근거: CCAR-P-jrajath94-0036, CCAR-P-jrajath94-0041, CCAR-P-jrajath94-0042, CCAR-P-jrajath94-0091, CCAR-P-jrajath94-0209, CCAR-P-jrajath94-0213, CCAR-P-jrajath94-0214, CCAR-P-jrajath94-0215, CCAR-P-jrajath94-0220, CCAR-P-jrajath94-0229, CCAR-P-jrajath94-0231, CCAR-P-jrajath94-0319, CCAR-P-jrajath94-0376, CCAR-P-jrajath94-0677, CCAR-P-jrajath94-0682, CCAR-P-jrajath94-0685</sub>

@@ CHECK
- [ ] 비가역 · 규제 대상 행동 → pre-action 승인 + 실제 컨텍스트
- [ ] 중단 시 보안 제어 → fail-closed
- [ ] 비용 상한 → 측정된 필요치 위 + 상한 전 알림
- [ ] 합산 지표 ✗ → 그룹별 측정 + 하한선 + 상류 수정
- [ ] 투명성 = AI 고지 + 주장별 인용 + 이의 신청
- [ ] 감사 증거 = 실행 기록(log) · trace, 정책 문구 ✗
<sub>근거: CCAR-P-jrajath94-0042, CCAR-P-jrajath94-0209, CCAR-P-jrajath94-0213, CCAR-P-jrajath94-0220, CCAR-P-jrajath94-0223, CCAR-P-jrajath94-0227</sub>
