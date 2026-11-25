@@ ADD-TO: ### 1.7 PII 보호: 데이터 최소화

| 구분 | 내용 |
|---|---|
| 규제 데이터 경계 | 제공자로 PHI 전달 금지 + 자유 형식 질의 필요<br>→ 비식별화 계층으로 둘 다 충족 |
| 비식별화 계층 | API 호출 전 PHI 제거 · tokenization<br>→ 결과를 로컬에서 재연결<br>→ 경계 로깅 · 주기적 감사 |
| 출력 금지 데이터<br>(카드 번호 등) | 입력 최소화: 검색 context redact (모델 도달 전)<br>+ deterministic 출력 필터: 패턴 차단 · 마스킹 (전송 전)<br>→ 독립 2층 → "0건" 달성 |
| 로깅 경계 | PII redact · 제거 후 저장<br>보존 = 문서화된 목적에 묶은 짧은 기간 (예: 30일)<br>연장 = 승인 필요 |
| 로그 열람 | 필요한 사람으로 접근 제한 + 보존 기한 설정<br>로그 · trace = 유출 경로 |
| 감사용 전문 로깅 요청 | 감사가 실제로 요구하는 바 확인<br>→ 필요 이상 보관 ✗ · 감사 목적 충족 |
| 발송 side effect<br>(타인 정보 혼입) | 발송 전 코드 검사<br>수신자 · 상세 = 지원자 기록과 일치<br>불일치 → 발송 차단 |

| 오답 | 이유 |
|---|---|
| 임상의에게 "식별자 입력 금지" 요청 · 신뢰 | 신뢰 = 통제 ✗ |
| system prompt "PHI를 잊어라 · 무시하라" | 지시는 데이터가 이미 넘어간 뒤 작동 |
| 자유 형식 질의 전면 차단 | 명시된 비즈니스 요구 미충족 |
| system prompt "never share card numbers" | user instruction이 덮어쓸 수 있음<br>→ 보장 ✗ |
| 지원팀 교육 | 사람만 통제<br>적대적 입력의 agent 출력 통제 ✗ |
| 출력 전량 기록 + 주간 검토 | 사후 탐지 → 며칠 지연<br>제약이 예방이면 ✗ |
| 12개월 로그 유지 + 저장 시 암호화 | 기밀성만 보호 · 최소화 ✗<br>키 · 접근 침해 시 전량 노출 |
| 접근 권한 유지 + 로그 암호화 | 열람자 전원이 여전히 데이터 열람 |
| cold storage 이전 | 비용만 변경 · 노출 불변 |
| "디버깅에 필요" 전량 보관 | 디버깅 = 최근 · 관련 로그로 충분<br>쌓아 두기 ≠ 역량 |
| "로그는 내부용이라 위험 없음" | 엔지니어 수백 명에게 고객 데이터 노출 |
| 모델에게 응답에서 PII 제외 요청 | prompt 속 PII 그대로<br>모델 준수 신뢰 ✗ |
| 감사 우선 → 일괄 구현 / 위험 → 일괄 거부 | 한쪽 제약 무시 |
| 응답만 로깅 (prompt 제외) | 요구사항 모르면 임의 분할 |
| 발송 후 사과 · 실수 기록 | 기록 = 피해 기록뿐<br>보완책일 뿐 단독 ✗ |

<sub>근거: CCAR-P-Amey-Thakur-0008, CCAR-P-Amey-Thakur-0024, CCAR-P-Amey-Thakur-0041, CCAR-P-Amey-Thakur-0059, CCAR-P-jrajath94-0034, CCAR-P-jrajath94-0093, CCAR-P-jrajath94-0562, CCAR-P-preporato-0024</sub>

@@ NEW-SECTION
### 보존(retention)·삭제 설계
**보존 = 기본값이 아닌 아키텍처 결정**

| 구분 | 내용 |
|---|---|
| 무기한 저장 제안 | 제기할 질문: 왜 필요 · 얼마나 오래 · 보관이 만드는 의무<br>"보관은 항상 더 안전" ✗ (의무 · 위험 발생)<br>저장 비용 · 속도 = 부차 |
| 보존 규칙 구성 | 요구사항에 연결한 기간<br>+ 담당자 · 시행 증거 · 검토 주기<br>+ 요청 시 삭제 경로 |
| 예시 | 티켓 3년 후 자동 삭제 + 고객 요청 시 조기 삭제 = 타당<br>숫자(3년)만으로는 불충분 |
| 보존 기간 미설정 | 대화 기록 무제한 누적<br>→ 기간 수치 + 예약 삭제 + 삭제 로그 |
| 민감 데이터가 든 로그<br>(계좌 번호 등) | 규제가 통제하는 산출물<br>→ 보존 · 접근 · 책임자 · 증거 · 주기 전체 필요 |
| 삭제권 이행 | 삭제 pipeline = 저장된 모든 사본 탐색<br>(로그 · 평가 샘플 · 백업)<br>→ 법정 기한 내 삭제 |
| 삭제 vs 디버깅 충돌 | 규칙 유지 (예: 90일 후 삭제 + 삭제 로그)<br>디버깅 = 마스킹된 · 짧은 기간 재현 데이터 |
| 규칙을 바꾸는 경우 | 규제 당국이 더 긴 일정 승인<br>→ 담당자 · 증거 · 주기를 갖춘 행으로 재작성<br>→ 더 긴 일정이 예외가 아닌 규칙 |
| 한계 | 마스킹 재현 데이터가 인시던트 재현 실패 가능<br>→ 짧은 기간 데이터에서 재도출<br>비용 = 규칙의 대가 |

| 오답 | 이유 |
|---|---|
| 보존 기간을 2년으로 연장 | 편의와 규칙 맞교환<br>침해 표면 24배 증가 |
| 다음 인시던트 검토까지 삭제 중단 | 담당자 · 일자 없음 → 중단이 영구화 |
| 영구 보관 + 시니어 접근 제한 | 독자 목록만 줄인 "모두 보관"<br>일수 미정 |
| 모든 티켓 하루 후 삭제 | 비즈니스 · 규제 증거 파괴<br>규칙이 실제로 요구할 때만 정답 |
| 사본이 남은 상태의 삭제 이행 | 백업 · 평가 샘플에 남으면 삭제 무의미 |

<sub>근거: CCAR-P-Amey-Thakur-0071, CCAR-P-jrajath94-0037, CCAR-P-jrajath94-0093, CCAR-P-jrajath94-0222, CCAR-P-jrajath94-0225, CCAR-P-jrajath94-0380, CCAR-P-jrajath94-0505</sub>

@@ NEW-SECTION
### 규제 프레임워크 매핑 (GDPR · HIPAA · FedRAMP)
**프레임워크 = 데이터 유형 · 관할권이 결정**

| 프레임워크 | 적용 대상 | 설계 요구 |
|---|---|---|
| GDPR | EU 거주자 개인 데이터<br>(회사 소재지 무관) | 최소화 · 목적 제한 · 삭제 능력<br>처리자 DPA · EU residency |
| HIPAA | 미국 건강 정보(PHI) | BAA · 적격 구성<br>최소 필요 · audit logging |
| FedRAMP | 미국 연방 기관용 클라우드 서비스 | 인가 환경 · 경계 문서화<br>audit logging |
| 부모 동의 규정<br>(어린이 앱) | 아동 음성 클립 수집 | 코드 내 동의 gate + 최소화 |
| 주별 동의 규칙<br>(원격 의료) | 여러 주 환자 | 코드의 주별 분기 + 증거 체인 |

| 구분 | 내용 |
|---|---|
| 복수 프레임워크 | 미국 원격 의료 + 독일 환자 → HIPAA + GDPR 동시<br>"미국 회사라 HIPAA만" ✗<br>"제3자 서비스라 해당 없음" ✗ (벤더 이용 ≠ 면제) |
| FedRAMP 비적용 | 연방 기관 서비스가 아니면 대상 ✗ |
| 설계를 좌우하는 GDPR 요구 | 데이터 최소화 · 목적 제한 · 요청 시 삭제<br>지연 시간 · 언어 · 제공자 수 = 무관 |
| 삭제권 + 비학습 요구 | 제공자 측: DPA + zero data retention(또는 문서화된 비학습)<br>회사 측: 전 사본 삭제 pipeline<br>→ 두 측면 모두 필요 |
| 부모 동의 + 최소화 | 검증된 부모 동의 없이 수집 ✗ (코드 gate)<br>필요한 클립만 보관 · 나머지 일정에 따라 자동 삭제<br>+ 담당자 · 증거 |
| 주별 동의 | 인증된 기록으로 확인한 환자의 주 규칙을 코드가 적용<br>모든 주에 추측한 단일 규칙 ✗ (법 추측) |

| GDPR Art. 22 | 내용 |
|---|---|
| 적용 대상 | 법적 효과 · 이에 준하는 중대한 영향을 주는<br>전적으로 자동화된 결정 (대출 승인 = 전형) |
| 성격 | 조건부 허용 (해설 기준: 금지 ✗) |
| 허용 근거 | 계약 이행 필요성 · 법적 의무 · 명시적 동의 |
| 안전장치 | 사람 개입 · 의견 표명 · 이의 제기 · 설명 받을 권리 |
| 사람 개입의 질 | 의미 있는 역할 필요<br>형식적 승인(24시간 내 승인) = 여전히 전적 자동 |
| 오답 | "마케팅 개인화에만 적용" ✗<br>"전면 금지 → 모든 결정에 사람 승인자" ✗ |

| 오답 | 이유 |
|---|---|
| 경영진 분석 대시보드 익명화 | 위생 관리일 뿐<br>삭제 · 학습 요구 어느 쪽도 미충족 |
| 가장 저렴한 리전에 로그 저장 | EU 밖일 수 있음 → data residency 문제 추가 |
| 응답 지연 · 프로그래밍 언어 · 제공자 수로 GDPR 대응 | 아키텍처를 좌우하는 요구 아님 |

<sub>근거: CCAR-P-Amey-Thakur-0044, CCAR-P-jrajath94-0037, CCAR-P-jrajath94-0092, CCAR-P-jrajath94-0443, CCAR-P-jrajath94-0506, CCAR-P-preporato-0023</sub>

@@ NEW-SECTION
### HIPAA · BAA 적용 범위
**BAA = 서명 계약 + plan · 구성 속성 + 경로별 범위**

| 구분 | 내용 |
|---|---|
| 최소 규정 준수 구성 | HIPAA 적격 배포 (예: 적격 구성의 Bedrock · Vertex)<br>+ 서명된 BAA + 최소 필요 데이터 수집<br>+ PHI 접근 audit logging |
| 요소별 대응 | 법적 수단 = BAA<br>적격 서비스 구성<br>minimum-necessary · 감사 가능성 |
| BAA 가능 여부 | plan의 속성 + 서명된 계약 (설정 ✗)<br>Team · consumer plan = 적용 대상 ✗ |
| 적용 대상 plan | Enterprise 또는 서명된 BAA가 있는 first-party API<br>→ 이전 끝날 때까지 PHI 처리 중단 |
| BAA 범위 | Anthropic의 처리만 포괄<br>agent가 호출하는 모든 tool ✗ |
| 서드파티 MCP connector | 별도 데이터 흐름<br>→ 벤더와 자체 BAA 또는 해당 경로 PHI 제외 |
| connector 서명 전 | PHI 경로에서 connector 비활성화<br>대시보드 = 대기 또는 de-identified 데이터 |
| 분석 벤더의 지위 | 고객이 선택한 도구 ≠ Anthropic subprocessor<br>subprocessor 조건 적용 ✗ |
| ⚠️ 시점 변동 | plan별 BAA 적용 · HIPAA 적격 서비스 목록은 바뀜<br>공식 문서: HIPAA readiness = Claude API 조직(Console)<br>Bedrock · Google managed = 각 플랫폼 문서 확인 |

| 오답 | 이유 |
|---|---|
| HTTPS 암호화만 있으면 아무 API 가능 | 필요하나 불충분<br>BAA · 적격성 · 감사 추적 없음 |
| 온프레미스만 사용 | 법적 요구 아님<br>HIPAA 적격 클라우드 구성이 존재 |
| 환자 동의서만 수령 | BAA · 안전장치 · 최소 필요 대체 ✗ |
| 임상의 개별 기밀 유지 계약 | 벤더 처리 미포괄<br>Anthropic이 BAA 보유 필요 |
| 이름 제거로 익명화 후 Team plan 유지 | 신뢰할 de-identification ✗<br>plan 적용 대상도 불변 |
| 관리자 설정의 HIPAA 토글 | 그런 토글 없음<br>비대상 plan에서 준수 활성화 ✗ |
| Anthropic BAA가 서드파티 connector까지 포괄 | BAA-scope 함정<br>적용 범위의 제3자 확산 가정 |

<sub>근거: CCAR-P-jrajath94-0038, CCAR-P-jrajath94-0095, CCAR-P-jrajath94-0096</sub>

@@ NEW-SECTION
### Zero data retention (ZDR)
**ZDR = 조직별 활성화 · 기능별 적격 · Console 제외**

| 구분 | 내용 |
|---|---|
| 의미 | 응답 반환 후 Anthropic이 prompt · response를 at rest 저장 ✗ |
| 활성화 | account team이 조직별로 활성화<br>(설정 토글 ✗) |
| 적격 여부 | 기능마다 다름<br>→ 출시 전 사용 기능을 각각 확인 |
| 범위 밖 | Console 사용 (playground 포함)<br>→ 규제 데이터를 playground에 입력 ✗<br>→ 해당 조직 key로 API 호출만 사용 |
| HIPAA readiness와 차이 | HIPAA readiness = 보호 장치 추가<br>각 응답 후 삭제 요구 ✗<br>"저장 안 함" 요구에 부적합 |
| 계약상 비학습 | DPA + ZDR(또는 문서화된 비학습) 조건 |
| ⚠️ 시점 변동 | ZDR 적격 기능 · 제외 범위는 계약 · 문서에 따라 바뀜<br>공식 문서: Legacy ZDR · HIPAA readiness · EFS ZDR(beta)로 구분<br>해설은 "ZDR" 하나로 서술 |

| 오답 | 이유 |
|---|---|
| platform activity log 활성화 | 데이터 통제처럼 보이나 ZDR 활성화 ✗ |
| 규제 prompt를 Console playground에 두기 | ZDR이 Console 미포함 |
| 기본 retention 유지 + 클라이언트 측 암호화 | Anthropic 쪽 저장 유지 → "저장 금지" 계약 미충족 |
| HIPAA readiness로 각 응답 후 저장 차단 | 보호 장치일 뿐 삭제 요구 ✗ |

<sub>근거: CCAR-P-jrajath94-0037, CCAR-P-jrajath94-0595, CCAR-P-jrajath94-0680</sub>

@@ NEW-SECTION
### Data residency
**residency = 위치를 통제로 강제 + 증거로 입증**

| 구분 | 내용 |
|---|---|
| 요구 | EU 데이터는 EU 안에 유지<br>→ EU 리전에 저장 · 처리 배포<br>+ 증거 체인 구축 |
| 위반 신호 | EU 데이터를 US 리전에 저장<br>"클라우드는 글로벌" = 통제 ✗ |
| 증거 | 의도가 아닌 실제 저장 위치를 보여야 함<br>예: 리전 설정 + 월간 삭제 로그 |
| 이동 비용 | 리전 이동 = 데이터 migration 필요<br>리전 2개 = 모든 것 2벌 → 비용 · 복잡성 |
| 유지 비용 | 리전 설정 어긋남 · 소유자 변경 · 주기 없으면 증거 낡음 |
| 면제 | 적용되는 residency 규칙이 없으면 문제 없음 |

| Claude API 설정 | 내용 |
|---|---|
| `inference_geo` | 요청별 inference 실행 위치 (`us` 등) |
| `default_inference_geo` | 요청이 `inference_geo` 생략 시 적용되는 workspace 기본값 |
| `allowed_inference_geos` | 다른 geo 지정 요청 거부<br>→ 앱 코드가 규칙 우회 ✗ |
| 정답 조합 | workspace에 default + allowed = `us`<br>→ 코드가 설정을 생략해도 미국 내 유지 |
| ⚠️ 시점 변동 | 지원 = Claude 4.6 이상 모델 · 지원 플랫폼 한정 (공식 문서 기준)<br>Bedrock · Google managed = 엔드포인트 · profile이 리전 결정 |

| 오답 | 이유 |
|---|---|
| 앱 서버 리전을 US로 설정 | inference 위치는 `inference_geo`가 제어 |
| 요청별 `inference_geo`만 + 허용 목록 열어 둠 | 코드가 생략 · 변경 가능 → 규칙 보장 ✗ |
| 저장 시 암호화 | 잘못된 리전에 영구 잔존 · 모두 열람 가능 |
| DB 행에 EU 플래그 | 레이블이지 통제 ✗ → 데이터는 US 잔존 |
| 개인정보 안내문 추가 | 아키텍처 없는 말뿐 |
| README 메모 "EU 안에 머문다" | 의도 문서화 → 감사자가 인정 ✗ |
| 어디에 호스팅되든 더 큰 모델 | residency 무시 → 설계상 위반 |
| 가장 저렴한 리전에 저장 | EU 밖 가능 → residency 문제 |

<sub>근거: CCAR-P-jrajath94-0037, CCAR-P-jrajath94-0222, CCAR-P-jrajath94-0318, CCAR-P-jrajath94-0568, CCAR-P-jrajath94-0681</sub>

@@ NEW-SECTION
### FedRAMP · 인가 환경 배포
**FedRAMP = 서비스 경계에 귀속 · 경로가 곧 요구사항**

| 구분 | 내용 |
|---|---|
| 인가의 귀속 | 서비스 경계에 귀속<br>상용 직접 API = 인가 ✗ (해설 기준) |
| 인가 경로 | Claude for Government (Anthropic FedRAMP High 플랫폼)<br>AWS Bedrock GovCloud · Vertex AI Assured Workloads<br>→ 해당 클라우드 인가 상속 |
| 감사자 확인 대상 | audit logging + 인가 경계(authorization boundary) 문서화 |
| 첫 아키텍처 조치 | deployment-route 행 구축<br>= 승인 환경 실행 + baseline 통제별 담당자 · 증거 매핑<br>+ 검토 주기 설정 |
| 선행 의존성 | 조달 리드 타임 · 기관의 통제 목록<br>→ 시간 · 비용 · 운영 제약을 예산에 반영 |
| 우선순위 | 단순함 < 조달 규정<br>보안 기능이 승인 환경 대체 ✗ |
| ⚠️ 시점 변동 | 인가 상태 · 경로(플랫폼 · 인가 수준)는 바뀜<br>현재 인가 여부는 공식 문서 · 조달 심사에서 확인 |

| 오답 | 이유 |
|---|---|
| "FedRAMP는 인프라용, AI API는 대상 아님" | 기관 데이터를 다루는 AI API도 범위 |
| 직접 API가 통제를 충족한다는 자체 증명 | 자체 증명 ≠ 인가 → 조달 심사 탈락 |
| 분석가 노트북에서 실행 | 중앙 로깅 · 패치 통제 없음<br>기관 요구 회피 ✗ |
| 상용 리전 + 전체 암호화 | 잘못된 환경 · 암호화는 배포 문제의 대체 ✗ |
| 로그인 페이지의 정부 사용 고지 | 고지일 뿐 통제 ✗ |
| 기관에 "모델이 안전하다" 약속 | 기관 요구 = 약속이 아닌 baseline |

<sub>근거: CCAR-P-jrajath94-0040, CCAR-P-jrajath94-0226</sub>

@@ NEW-SECTION
### 컴플라이언스 증거 체인과 감사 로그
**통제 이름만으로는 미완결 · 5고리 체인**

| 고리 | 완결 조건 |
|---|---|
| 요구사항 | 규정이 요구하는 것 (예: EU 데이터는 EU 유지) |
| 통제 | 구현 수단 (예: EU 리전 배포 · 역할 범위 접근) |
| 담당자 | 지정된 소유자 (인턴 · 공란 ✗) |
| 증거 | 산출물 (로그 · 설정 · 보고서)<br>"신뢰한다" · 주장 ✗ |
| 주기 | 일정 (월간 · 분기)<br>"never" · 없음 ✗ |

| 상황 | 정답 |
|---|---|
| 접근 통제는 있으나 담당자 · 검토 일정 없음 | 지정된 담당자 + 검토 주기 추가<br>아바타 · 긴 system prompt · 큰 모델 = 고리 ✗ |
| 규제 기관이 접근 통제 증거 요구 | 5고리 체인 (로그 · 설정이 증거)<br>"통제가 있다" 진술 · 비밀번호 길이 ✗ |
| 완결된 행 예시 1 | EU 데이터 유지 → EU 리전 배포 · DPO<br>→ 리전 설정 + 월간 삭제 로그 · 매월 |
| 완결된 행 예시 2 | 케어팀만 열람 → 사용자별 역할 접근 · 보안 책임자<br>→ 분기별 접근 검토 + 읽기 감사 로그 · 분기별 |
| 마스킹 통제 행 | "마스킹을 신뢰" ✗<br>증거 열에 분기별 날짜의 trace 감사 보고서 있으면 유효 |
| 규제 데이터가 있는 시나리오 | "규제 데이터 없음" 행 ✗<br>(실제로 없는 봇이면 고지로 충분) |
| 규제 데이터 저장소의 복합 결함<br>(리전 · 공유 계정 · 무기한 보존) | 리전 · 접근 · 보존 각각 행 + 소유자 · 증거 · 주기<br>EU 리전 · 사용자별 신원 역할 접근 · 읽기 감사 로그<br>· 예약 삭제 · 삭제 로그 |
| 은행 모델 리스크 문서 | 모델 인벤토리 (모델 · 버전 · 사용 사례)<br>+ 검증 증거 (모델별 eval 결과 · 한계 · monitoring 계획) |
| 체인 유지 | 매핑에 검토 주기 필요 → 확인 없는 매핑은 부패 |

| 감사 요구 | 남길 로그 · 산출물 |
|---|---|
| PHI 접근 | audit logging |
| 대화 기록 열람 | 읽기 감사 로그 + 사용자별 신원 |
| 삭제 이행 | 삭제 로그 |
| 규제 경계 통과 (비식별화 계층) | 경계 로깅 + 주기적 감사 |
| 인가 환경 (FedRAMP) | audit logging + 경계 문서화 |

| 오답 | 이유 |
|---|---|
| README 메모 · 의도 문서화 | 감사자는 의도를 인정 ✗ |
| "준수할 의도가 있다" | 의도는 체인의 고리 ✗ |
| 기록 없는 통제 · 담당자 인턴 · 주기 없음 | 증거 없는 통제 = 희망 |
| 저장 시 암호화로 컴플라이언스 충족 | 암호화 = 제자리 보호<br>residency · 접근 · 보존 = 별개 행 + 별개 증거 |
| 마케팅 브로셔 · 점심 메뉴를 모델 리스크 패키지에 포함 | 산출물 형태 = 인벤토리 + 검증 증거 |
| 단일 규칙을 추측해 전 주에 적용 | 법 추측 |

<sub>근거: CCAR-P-jrajath94-0038, CCAR-P-jrajath94-0222, CCAR-P-jrajath94-0224, CCAR-P-jrajath94-0225, CCAR-P-jrajath94-0226, CCAR-P-jrajath94-0318, CCAR-P-jrajath94-0379, CCAR-P-jrajath94-0442, CCAR-P-jrajath94-0505, CCAR-P-jrajath94-0506, CCAR-P-jrajath94-0569, CCAR-P-Amey-Thakur-0008, CCAR-P-Amey-Thakur-0041</sub>

@@ RULES
| 상황 | 정답 |
|---|---|
| PHI가 제공자로 넘어가면 안 됨 + 자유 형식 질의 필요 | 비식별화 계층: 호출 전 제거 · tokenization<br>→ 로컬 재연결 + 경계 로깅 · 감사 |
| agent 출력에 카드 번호 전체 금지 | 입력 redact (모델 도달 전) + deterministic 출력 필터 |
| 감사용 전체 prompt · 응답 로깅 요청 | 감사가 실제 요구하는 바 확인<br>→ 필요 이상 보관 ✗ |
| 로그에 PII · 고객 데이터 존재 | 로깅 경계에서 redact + 짧은 보존 + 접근 제한 |
| 모든 상호작용 무기한 저장 제안 | 목적 · 기간 · 의무 질문 → 보존 = 아키텍처 결정 |
| 보존 규칙 vs 디버깅 요구 충돌 | 규칙 유지 + 삭제 로그<br>마스킹 · 짧은 기간 재현 데이터로 디버깅 |
| GDPR 삭제권 + 비학습 | DPA + ZDR(또는 비학습 조건) + 전 사본 삭제 pipeline |
| 자동 대출 결정 (EU) | Art. 22: 적법 근거 + 안전장치<br>의미 있는 사람 개입 |
| 미국 원격 의료 + 독일 환자 | HIPAA + GDPR 동시 적용 |
| Team plan에서 PHI pilot | BAA 가능한 환경(Enterprise · 서명 BAA의 first-party API)으로 이전<br>그때까지 PHI 처리 중단 |
| BAA 후 서드파티 connector가 PHI 전송 | connector 자체 BAA 또는 PHI 제외 → 서명 전 비활성화 |
| 계약상 prompt · 응답 at rest 저장 금지 | account team에 ZDR 활성화 + 사용 기능별 적격 확인<br>Console에 PHI 입력 ✗ |
| 모든 요청이 미국 내 inference (코드가 생략해도) | workspace `default_inference_geo` + `allowed_inference_geos` = `us` |
| EU 데이터가 US 리전에 저장 | EU 리전으로 저장 · 처리 이전 + 증거 체인 |
| 연방 기관 + FedRAMP 요구 | 인가 경로(Claude for Government · GovCloud · Assured Workloads)<br>+ audit logging + 경계 문서화 |
| 규제 기관이 증거 요구 | 요구사항 → 통제 → 담당자 → 증거 → 주기 체인 |
| 발송이 타인 정보를 섞음 | 발송 전 코드 일치 검사 · 불일치 시 차단 |
| 은행 모델 리스크 문서 | 모델 인벤토리 + 검증 증거 |

<sub>근거: CCAR-P-Amey-Thakur-0008, CCAR-P-Amey-Thakur-0024, CCAR-P-Amey-Thakur-0041, CCAR-P-Amey-Thakur-0044, CCAR-P-Amey-Thakur-0059, CCAR-P-Amey-Thakur-0071, CCAR-P-jrajath94-0034, CCAR-P-jrajath94-0037, CCAR-P-jrajath94-0038, CCAR-P-jrajath94-0040, CCAR-P-jrajath94-0092, CCAR-P-jrajath94-0093, CCAR-P-jrajath94-0095, CCAR-P-jrajath94-0096, CCAR-P-jrajath94-0222, CCAR-P-jrajath94-0224, CCAR-P-jrajath94-0225, CCAR-P-jrajath94-0226, CCAR-P-jrajath94-0318, CCAR-P-jrajath94-0379, CCAR-P-jrajath94-0380, CCAR-P-jrajath94-0442, CCAR-P-jrajath94-0443, CCAR-P-jrajath94-0505, CCAR-P-jrajath94-0506, CCAR-P-jrajath94-0562, CCAR-P-jrajath94-0568, CCAR-P-jrajath94-0569, CCAR-P-jrajath94-0595, CCAR-P-jrajath94-0680, CCAR-P-jrajath94-0681, CCAR-P-preporato-0023, CCAR-P-preporato-0024</sub>

@@ TRAPS
| 오답 | 이유 |
|---|---|
| 신뢰 · "PHI 잊어라" prompt · 전면 차단 | 통제 ✗ · 이미 넘어간 뒤 작동 · 요구 미충족 |
| "never share" prompt · 직원 교육 · 주간 검토 | 보장 ✗ · 출력 통제 ✗ · 사후 탐지 |
| 암호화만 · cold storage · 접근 유지 | 최소화 ✗ · 노출 불변 |
| 일괄 로깅 · 일괄 거부 · 응답만 로깅 | 감사와 데이터 보호 중 한쪽 무시 · 임의 분할 |
| "보관은 항상 안전" · 보존 연장 · 삭제 중단 | 보존은 의무 · 위험 발생 → 규칙이 이김 |
| 모든 티켓 하루 후 삭제 | 비즈니스 · 규제 증거 파괴 |
| 대시보드 익명화 · 가장 저렴한 리전 | 요구 미충족 · EU 밖 가능 (residency) |
| Art. 22 = 금지 → 사람 승인자 추가 · 형식 승인 | 근거 + 안전장치 필요 · 형식 승인 = 전적 자동 |
| "미국 회사라 HIPAA만" · "제3자라 해당 없음" | 데이터 유형 · 관할권이 결정 |
| HTTPS · 온프레미스 · 동의서만 · 개별 기밀 계약 | BAA · 적격 구성 · 최소 필요 대체 ✗ |
| Team plan HIPAA 토글 · 이름만 제거 | 토글 없음 · 신뢰할 de-identification ✗ |
| Anthropic BAA가 서드파티 connector 포괄 | BAA-scope 함정 · 분석 벤더 ≠ subprocessor |
| platform activity log · HIPAA readiness로 ZDR 대체 | ZDR 활성화 ✗ · 삭제 요구 ✗ |
| Console playground에 규제 prompt | ZDR 범위 밖 |
| 앱 서버 리전 · 요청별 `inference_geo`만 | inference 위치 불제어 · 코드가 생략 가능 |
| EU 플래그 · 안내문 · README 메모 · "글로벌 클라우드" | 레이블 · 말뿐 · 의도 · 통제 ✗ |
| 직접 API 자체 증명 · 노트북 · 정부 고지 · 약속 | FedRAMP 인가 ✗ · 로깅 · 패치 통제 없음 |
| 통제 이름만 · 기록 없음 · 담당자 인턴 · 주기 없음 | 5고리 미완결 → 희망일 뿐 |
| 아바타 · 긴 prompt · 큰 모델로 컴플라이언스 | 체인의 고리 ✗ |
| 발송 후 사과 · 실수 기록 | 사후 기록 → 사전 코드 검사 필요 |

<sub>근거: CCAR-P-Amey-Thakur-0008, CCAR-P-Amey-Thakur-0024, CCAR-P-Amey-Thakur-0041, CCAR-P-Amey-Thakur-0044, CCAR-P-Amey-Thakur-0059, CCAR-P-Amey-Thakur-0071, CCAR-P-jrajath94-0034, CCAR-P-jrajath94-0037, CCAR-P-jrajath94-0038, CCAR-P-jrajath94-0040, CCAR-P-jrajath94-0092, CCAR-P-jrajath94-0093, CCAR-P-jrajath94-0095, CCAR-P-jrajath94-0096, CCAR-P-jrajath94-0222, CCAR-P-jrajath94-0224, CCAR-P-jrajath94-0225, CCAR-P-jrajath94-0226, CCAR-P-jrajath94-0318, CCAR-P-jrajath94-0379, CCAR-P-jrajath94-0380, CCAR-P-jrajath94-0442, CCAR-P-jrajath94-0443, CCAR-P-jrajath94-0505, CCAR-P-jrajath94-0506, CCAR-P-jrajath94-0562, CCAR-P-jrajath94-0568, CCAR-P-jrajath94-0569, CCAR-P-jrajath94-0595, CCAR-P-jrajath94-0680, CCAR-P-jrajath94-0681, CCAR-P-preporato-0023, CCAR-P-preporato-0024</sub>

@@ MEMO
| 이름 | 의미 |
|---|---|
| PHI | 보호 대상 건강 정보 (protected health information) |
| BAA | business associate agreement<br>PHI 처리 벤더와 맺는 계약 · plan · 구성 속성 |
| DPA | 데이터 처리 계약<br>GDPR이 처리자(processor)에 요구 |
| Minimum necessary | HIPAA 최소 필요 기준 → 필요한 데이터만 수집 |
| 비식별화 계층 | 호출 전 PHI 제거 · tokenization → 로컬 재연결 |
| ZDR | zero data retention<br>응답 후 prompt · response at rest 저장 ✗ · 조직별 활성화 |
| Data residency | 데이터 저장 · 처리 위치 제약 (EU 데이터 = EU 리전) |
| `inference_geo` | 요청별 inference 실행 위치 |
| `default_inference_geo` | `inference_geo` 생략 시 적용되는 workspace 기본값 |
| `allowed_inference_geos` | 허용 geo 목록 → 밖의 geo 요청 거부 |
| FedRAMP | 미국 연방 기관용 클라우드 인가 · 서비스 경계에 귀속 |
| Claude for Government | Anthropic FedRAMP High 인가 플랫폼 (해설 기준) |
| 인가 경계 (authorization boundary) | FedRAMP 감사자가 확인하는 문서화 대상 |
| GDPR Art. 22 | 전적 자동 결정 → 법적 근거 + 안전장치 |
| 증거 체인 | 요구사항 → 통제 → 담당자 → 증거 → 주기 |
| 모델 리스크 패키지 | 모델 인벤토리 + 검증 증거 |

<sub>근거: CCAR-P-Amey-Thakur-0008, CCAR-P-Amey-Thakur-0041, CCAR-P-Amey-Thakur-0044, CCAR-P-jrajath94-0037, CCAR-P-jrajath94-0038, CCAR-P-jrajath94-0040, CCAR-P-jrajath94-0092, CCAR-P-jrajath94-0095, CCAR-P-jrajath94-0224, CCAR-P-jrajath94-0568, CCAR-P-jrajath94-0569, CCAR-P-jrajath94-0595, CCAR-P-jrajath94-0680, CCAR-P-jrajath94-0681</sub>

@@ CHECK
- [ ] 규제 데이터 = 경계에서 제거 · tokenization, 로그 = redact + 짧은 보존
- [ ] BAA 범위 = Anthropic 처리만, 서드파티 connector = 별도 BAA
- [ ] ZDR = 조직별 · Console 제외, residency = default + allowed geo
- [ ] 컴플라이언스 = 요구사항 → 통제 → 담당자 → 증거 → 주기

<sub>근거: CCAR-P-Amey-Thakur-0008, CCAR-P-jrajath94-0093, CCAR-P-jrajath94-0096, CCAR-P-jrajath94-0224, CCAR-P-jrajath94-0595, CCAR-P-jrajath94-0680, CCAR-P-jrajath94-0681</sub>
