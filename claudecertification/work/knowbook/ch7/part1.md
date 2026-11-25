@@ ADD-TO: ### 1.1 Prompt injection: 방어는 구조적으로

**간접 injection 경로별 통제 조합**

| 입력 경로 | 통제 조합 |
|---|---|
| 검색 PDF · 문서<br>(refund tool 실행 가능) | 검색 텍스트 = untrusted 데이터<br>context 조립 전 screening<br>+ 돈 tool 앞 코드 authorization gate |
| 회의 초대장<br>(email tool 보유) | 초대장 텍스트 = 데이터<br>email tool을 코드의 인가로 gate<br>→ 참석자 목록 exfil 차단 |
| 이메일 첨부 송장<br>(결제 가능) | 모델이 읽기 전 첨부 screening<br>+ 결제 전 코드 gate<br>(합계를 원본 문서와 대조) |
| 인터넷 업로드 | 모델이 읽기 전 screening<br>+ 처리 시 sandboxing |
| 웹 fetch + 파일 도구<br>(`rm -rf` 지시 포함) | 간접 injection으로 명명<br>sandbox · shell 미부여 · screening<br>+ 페이지 격리 · 담당자 알림 |

**untrusted 콘텐츠 판단 기준**

| 구분 | 내용 |
|---|---|
| 신뢰 불가 출처 콘텐츠 | 처음부터 끝까지 untrusted 데이터<br>내용과 무관하게 모델 권한 제한 |
| 지속 가능한 통제 | 콘텐츠가 모델을 어떻게 설득해도<br>모델이 자기 권한을 못 넘는 구조 |
| tool 가진 agent의 읽기 | 수동적 행동 ✗<br>= 지시 채널 |
| 모델의 한계 | 문구만으로 신뢰 불가 지시를<br>안정적으로 구분 못 함 |
| screening · gate 한계 | screener = 새 공격 놓침<br>gate = 지연 · 실패 지점 추가<br>둘 다 담당자 필요 |
| tool 제거 | 공격 경로 소멸 · 업무 기능도 소멸<br>업무상 불필요한 기능일 때만 정답 |

| 오답 | 이유 |
|---|---|
| 알려진 공격 문자열 검사로 안전 판단 | 우회 가능 |
| 암호화 채널(TLS)로 안전 판단 | 전송 보안 = 콘텐츠에 대해 보장 ✗ |
| system prompt에 "조심하라" 추가 | 모델이 문구만으로 구분 불가<br>→ 해결책 ✗ |
| 모든 tool 호출 log 후 나중 검토 | monitoring = gate 대체 ✗<br>완벽한 기록 ≠ 예방 |
| 모델이 읽으면 untrusted도 안전 | 읽어도 데이터, 지시 ✗ |

<sub>근거: CCAR-P-Amey-Thakur-0025, CCAR-P-jrajath94-0208, CCAR-P-jrajath94-0212, CCAR-P-jrajath94-0316, CCAR-P-jrajath94-0375, CCAR-P-jrajath94-0437, CCAR-P-jrajath94-0563</sub>

@@ ADD-TO: ### 1.3 Least privilege와 tool 설계

**권한 초과 · 비대화 · 우회 사례**

| 상황 | 위험 · 조치 |
|---|---|
| 읽기 전용 보고 agent에<br>전체 write 권한 `run_sql` | 위험 = excessive agency + 데이터 노출<br>→ 읽기 전용으로 제한 또는 tool 제거<br>injection · 오류가 write로 유도 가능 |
| tool 35개 · 다수 중복<br>→ 오선택이 잘못된 환불 | 위험 = 기능 비대화 → tool 남용<br>→ 최소 권한 축소 · 중복 제거<br>progressive discovery 검토 |
| 역할극 jailbreak로<br>고객 목록 CSV export | prompt 패치 = 우회 가능한 한 계층<br>대량 export 불가 최소 권한 credential<br>→ "구조적 불가능" 충족 |

| 구분 | 내용 |
|---|---|
| 계층 구성 | 입력 검증<br>+ 대량 export 불가 최소 권한 credential<br>+ 민감 작업 출력 검토 |
| prompt 지시의 위치 | 한 계층으로 유지<br>모델을 속여도 구조가 export 차단 |
| tool 위험의 해결 | 더 작은 tool 범위<br>더 똑똑한 모델 ✗ |

| 오답 | 이유 |
|---|---|
| tool을 목록에서 숨기되 호출 가능 | 숨김에 의존한 보안 ✗<br>이름 유출 시 즉시 작동 |
| 거부 예시로 모델 추가 학습 | 여전히 모델 행동 · 구조적 장벽 ✗<br>모든 역할극 변형 대응 불가 |
| 역할극 거부 문구로 system prompt 강화 | 이미 뚫린 통제의 반복<br>(jailbreak 이후 prompt-plea 함정) |
| 더 큰 모델로 업그레이드 | 판단력만 구매, 경계 ✗<br>보호 없는 shell의 똑똑한 모델도 삭제 실행 |

**결정론적 통제 vs prompt 기반 통제**

| 구분 | 예 | 성격 |
|---|---|---|
| 결정론적 ✓ | 전체 계좌번호 포함 응답 차단 출력 필터<br>호출당 환불 `$100` 한도 tool 권한<br>+ 초과액은 사람 승인 | 모델 판단과 무관<br>코드에서 강제 |
| prompt 기반 ✗ | few-shot 거절 예시<br>system prompt 규칙<br>persona 지시 | 확률적 유도<br>교묘한 이메일이 우회 유도 |

<sub>근거: CCAR-P-jrajath94-0094, CCAR-P-jrajath94-0212, CCAR-P-jrajath94-0438, CCAR-P-jrajath94-0501, CCAR-P-preporato-0021</sub>

@@ ADD-TO: ### 1.5 Authorization 전파

**데이터 접근 분리 (tenant 격리) · 과대 credential**

| 상황 | 정답 |
|---|---|
| 고객 간 주문 데이터 비공개<br>(모든 사용자 입력에서 유지) | 호출 전 코드에서 로그인 고객 ID로<br>주문 레코드 filter<br>→ 모델은 본인 레코드만 수신 |
| agent를 CEO credential로 실행<br>("일을 더 빨리 처리") | 위험 = excessive agency + 데이터 노출<br>최대 권한 + 최대 데이터 = 영향 범위 최대<br>least privilege 미적용 → 수용 불가 |

| 오답 | 이유 |
|---|---|
| 전체 레코드 전송 후<br>모델에 "본인 것만 보여라" 요청 | 소유권 확인이 모델 판단에 의존<br>모델이 이미 타인 데이터 수신 |
| system prompt에 더 엄격한 규칙 | prompt = 지침 → 접근 강제 ✗<br>코드가 강제해야 함 |
| 출력 스키마로 고객 ID 필드만 나열 | 소유권 검사 ✗<br>레코드 수신 전 코드 확인 필요 |

<sub>근거: CCAR-P-jrajath94-0502, CCAR-P-jrajath94-0617</sub>

@@ ADD-TO: ### 1.6 API key / secret 관리

**prompt 안 secret의 전파 경로**

| 상황 | 조치 |
|---|---|
| system prompt에 production DB 비밀번호<br>("직접 연결"용) | prompt = credential 저장소 ✗<br>prompt를 거치는 모든 시스템이 비밀번호 획득<br>(log · cache · vendor) |
| 연결 방식 | secret manager로 이전<br>tool 계층이 agent 대신 DB 연결 |
| "비밀번호가 필요하니 문제 없음" | 오답 → 필요 = tool 계층의 몫 |

<sub>근거: CCAR-P-jrajath94-0564</sub>

@@ ADD-TO: ### 1.9 Guardrail 다층 방어 (defense in depth)

**입력 screening 설계 (모델 호출 전)**

| 상황 | 정답 |
|---|---|
| 자유 텍스트 → main 호출 전 검사<br>코드가 셀 수 있는 판정 필요 | 경량 모델이 각 메시지 선별<br>→ structured output = boolean 판정<br>→ 유해 판정이면 코드가 차단 |
| 아동(8~12세) 대상 bot<br>(PII · 자해 신호 입력) | 코드 입력 screening (모델 노출 전)<br>PII 탐지 → masking 또는 block<br>자해 신호 → 안전 protocol로 route |
| 경량 모델 예시 | Haiku 5.5<br>⚠️ 모델 버전명은 시점에 따라 바뀜 |

| 구분 | 내용 |
|---|---|
| 자해 신호 protocol | 단순 차단 ✗<br>자격 갖춘 사람에게 연결되는 경로 필요 |
| 계층 구성 | 모델 안전장치 + 입력 · 출력 screening<br>+ 결정론적 통제 + fail-closed 기본값 |
| 한계 | 무해한 메시지 과차단 가능<br>→ 차단 목록 tuning + 사람에게 이의 제기 경로 |

| 오답 | 이유 |
|---|---|
| 더 엄격한 system prompt로 유해 메시지 거절 | 모델이 주입 지시를 따를 수 있음<br>호출을 막는 코드 없음 |
| main 모델 high effort 선별 + reasoning 저장 | 요건 = 경량 모델의<br>파싱 가능한 boolean 판정 |
| prompt로 아동에게 개인 정보 공유 금지 요청 | 아동의 자제에 의존 → 통제 ✗<br>보완책으로만 가치 |
| 채팅 log 후 나중 검토 | 모델이 이미 정보를 본 뒤 |
| 더 긴 context window | 안전과 무관 |

<sub>근거: CCAR-P-jrajath94-0320, CCAR-P-jrajath94-0671</sub>

@@ NEW-SECTION
### Sandboxing: 실행 경계는 모델 밖에서
**경계는 prompt가 아닌 sandbox가 지킴**

| 상황 | 구성 |
|---|---|
| 보고서 쓰기 agent<br>(문서가 file exfil 지시) | 쓰기를 `/reports`로 한정<br>+ 네트워크 거부 + 실행 시간 제한<br>→ 주입 지시가 경계 확대 불가 |
| 모델 생성 script 테스트 실행 | 격리 sandbox<br>네트워크 ✗ · secret 접근 ✗<br>리소스 제한 |
| 임의 URL 방문 browser agent | sandbox: secret · 내부 네트워크 격리<br>+ 고위험 사이트 · 다운로드<br>allow-list 또는 screening |
| 인터넷 업로드 처리 | secret · 네트워크로부터 격리하여 처리<br>+ 모델 읽기 전 screening |

| 구분 | 내용 |
|---|---|
| 생성 코드 | 머신에 대한 untrusted 입력<br>sandbox = 피해 범위 제한 |
| 시간 제한 | 폭주 실행 중단 |
| 한계 | 잘못 구성한 sandbox는 데이터 유출<br>경계 = 설정 품질만큼 → 설정 테스트 필요 |

| 오답 | 이유 |
|---|---|
| 홈 디렉터리 쓰기 허용<br>+ "/reports만" prompt 메모 | 코드에서 제한 ✗ → prompt 메모 = 경계 ✗<br>sandbox와 병행 시 style guide로만 가치 |
| sandbox 없이 주간 검토 | 파일은 첫날에 유출<br>sandbox 보완책으로만 가치 |
| 파일 도구 제거 + 채팅에 보고서 붙여넣기 | 보고서 파일이 산출물이면 기능 상실<br>후속 파일 소비자 없을 때만 정답 |
| 개발자 노트북 · root에서 생성 코드 실행<br>· 모델 코드 신뢰 | 피해 범위 확대 |
| 기업 VPN 전체 접근 | 위협을 crown jewels와 연결 |
| 모든 파일 자동 다운로드 | screening으로 노출 제한 필요 |
| 로그 비활성화 | 팀의 눈 가림 |
| 업로드를 전 직원에게 자동 전달 | 위험 확산 |
| 친절한 system prompt | guidance일 뿐 → 통제 ✗ |

<sub>근거: CCAR-P-jrajath94-0210, CCAR-P-jrajath94-0374, CCAR-P-jrajath94-0437, CCAR-P-jrajath94-0500</sub>

@@ NEW-SECTION
### Claude Code 차단 수단: permission rule · sandbox
**Bash는 sandbox · 내장 Read는 permission rule**

| 목표 | 수단 |
|---|---|
| 특정 write tool 차단<br>(보고서 read tool은 유지) | 작업 설정에 해당 tool deny rule 추가<br>또는 tool 목록에서 제거<br>→ 권한 자체 종료 |
| shell의 알 수 없는 호스트 접근 차단 | `/sandbox` 실행으로 sandbox 켬<br>shell 네트워크 트래픽 → proxy 경유<br>허용 도메인 목록은 빈 상태로 시작 |
| 내장 Read tool의 credential 파일 열람 차단 | 해당 경로에 permission deny rule<br>(sandbox는 Read tool을 제어하지 않음) |

| 오답 | 이유 |
|---|---|
| tool 호출마다 audit logging 추가 | log 항목 = 기록 · 권한 종료 ✗ |
| tool search로 환불 tool을 deferred 처리 | 모델이 검색하면 deferred tool 로드<br>→ 호출 차단 ✗ |
| sandbox `denyRead` 항목 추가 | sandbox가 Read tool을 막지 않음 |

<sub>근거: CCAR-P-jrajath94-0631, CCAR-P-jrajath94-0673</sub>

@@ NEW-SECTION
### 운영 monitoring · 모델 안전장치 변동 대응
**성공은 출력 측 탐지 · 제어는 코드로**

| 구분 | 내용 |
|---|---|
| 시도 vs 성공 | 시도 = 입력 측 · 노이즈 많음<br>성공 = 출력 측에서 나타남 |
| 성공 탐지 설계 | 출력 측 classifier가 유출된 system 내용 탐지<br>(샘플링한 completion에 실행)<br>+ system prompt에 canary token 심기 |
| canary token | 출력에 등장 = 유출 입증 · 오탐 거의 없음<br>→ alert |
| 효과 | 샘플링 = 고트래픽 비용 감당<br>탐지 = 몇 시간 안 |

| 오답 | 이유 |
|---|---|
| 사용자 메시지에서<br>"ignore previous instructions" 검색 | 성공 아닌 시도 탐지<br>공격자는 표현 변경 · 오탐 폭증 |
| "system" 포함 메시지 전부 차단 | 정상 메시지 차단 ("my system is down")<br>표현 바꾼 공격은 통과 |
| 전 대화 기록 + 분석가 일일 검토 | 고트래픽 감당 불가<br>몇 시간 내 처리 불가 |

**provider 모델 업데이트 후 안전장치 변동**

| 구분 | 내용 |
|---|---|
| 증상 | 모델 업데이트 후 계좌번호가 출력에 등장<br>(팀 코드 변경 없음) |
| 원인 | 모델 내장 거부 동작에 의존<br>→ 안전장치는 예고 없이 변경<br>= 잠금장치 ✗ · 하나의 계층 |
| 수정 | 코드 수준 출력 screening (계좌번호 패턴)<br>+ 모델 버전 고정<br>+ 업데이트마다 회귀 검사 |
| 운영 의존성 | 패턴 목록이 쓰는 계좌 형식 전부 포괄<br>회귀 세트에 거부 사례 포함 |
| 한계 | false positive → 정상 답변 차단 = 고객 비용<br>패턴 목록 담당자 필요 |

| 오답 | 이유 |
|---|---|
| 더 엄격한 system prompt | 여전히 모델 동작<br>= 방금 실패한 방식 |
| 이전 버전 롤백만 | 다음 업데이트에 같은 단일 실패 지점<br>(긴급 롤백 단계로는 유효) |
| 모든 답변 사람 검토 | 20,000건/일 × 1분 ≈ 하루 333 검토자 시간<br>→ 실현 불가<br>(하루 50건 · 극단 위험이면 가능) |

**refusal 집계**

| 구분 | 내용 |
|---|---|
| 거절의 형태 | 오류 ✗<br>`stop_reason`이 `refusal`인 일반 응답 |
| 정책 영역별 집계 | `refusal`일 때 `stop_details` 카테고리 집계<br>→ 오류 파싱 불필요 · 모델 변경 불필요 |
| 오답: HTTP 오류 응답 집계 | refusal = 오류 응답 ✗ |
| 오답: usage 필드 category 읽기 | 정책 영역 = `stop_details`가 명시 |
| 오답: 전체 prompt · 응답 · 헤더 전수 log | 정렬 작업만 늘어남<br>`stop_details`로 집계 가능 |

<sub>근거: CCAR-P-jrajath94-0033, CCAR-P-jrajath94-0211, CCAR-P-jrajath94-0684</sub>

@@ NEW-SECTION
### 위험 식별: 시나리오 신호 → 위험 이름
**시나리오의 신호가 위험 이름을 결정**

| 시나리오 신호 | 위험 |
|---|---|
| 공개 인터넷 PDF · 이메일 · 초대장 · DM을 읽는 agent | 간접 prompt injection |
| 사람 승인 없이 $50,000 구매 주문<br>사람 gate 없이 신용카드 예약 | excessive agency<br>(행동 반경 > 감독 범위) |
| 확인 이메일 읽기 + 예약 tool 근접 | 간접 injection + excessive agency |
| 브랜드 명의 게시 + DM 읽기 | 간접 injection<br>+ 데이터 노출 (DM 속 개인 데이터 재게시) |
| CEO credential로 실행 | excessive agency + 데이터 노출 |

| 구분 | 내용 |
|---|---|
| 방지 | 입력 screening 계층<br>+ 사전 행동 승인 gate |
| 위험 명명 틀 | 위험마다 예방 · 탐지 · 복구를 갖춤<br>(risk register 행) |
| 완전한 대응 예 | 예방 = sandbox · shell 미부여 · screening<br>복구 = 페이지 격리 + 담당자 알림<br>(포렌식용 페이지 보존) |
| 승인 gate의 비용 | 조달 지연 증가 |

| 오답 (위험 아님) | 이유 |
|---|---|
| 지연(p95) · token 비용<br>· 느린 읽기 · 게시 · 실행 | 성능 문제 · 안전 위험 범주 ✗ |
| 저위험 hallucination<br>(벤더 설립 연도) | 돈을 움직이지 않음<br>(제출 보고서에 쓰이면 위험) |
| 보기 흉한 일정표 · 시끄러운 알림<br>· 문법 · 전력 · 낮은 배터리 · 지루한 콘텐츠 | 외관 · 부수 문제 ✗ |

<sub>근거: CCAR-P-jrajath94-0212, CCAR-P-jrajath94-0316, CCAR-P-jrajath94-0439, CCAR-P-jrajath94-0502, CCAR-P-jrajath94-0565</sub>

@@ NEW-SECTION
### 자동화 결정의 책임 소재
**자동화해도 결과 책임은 배포 조직**

| 주체 | 판정 | 이유 |
|---|---|---|
| 배포 조직 | ✓ | 자동화 결정을 배포 = 결과 소유 |
| 모델 제공자 | ✗ | 기능만 공급 |
| prompt 작성 엔지니어 | ✗ | 개인의 작성이 조직 책임을 이전 못 함 |
| "자동화라 아무도 없음" | ✗ | 자동화 ≠ 책임 소멸 |

- 자동화의 경계 = 아키텍처상의 결정

<sub>근거: CCAR-P-Amey-Thakur-0026, CCAR-P-Amey-Thakur-0060</sub>

@@ RULES
| 상황 | 정답 |
|---|---|
| 신뢰 불가 출처 콘텐츠가 모델에 도달하기 전 | 처음부터 끝까지 untrusted 데이터<br>내용과 무관하게 모델 권한 제한 |
| 문서 · 이메일 · 초대장을 읽는 agent에<br>돈 · 전송 tool 부여 | 간접 injection → 읽기 전 screening<br>+ tool 앞 코드 gate |
| 웹 페이지가 `rm -rf` 지시 + 파일 도구 | sandbox · shell 미부여 · screening<br>+ 격리 · 알림 |
| jailbreak 후 "구조적으로 불가능" 요구 | 최소 권한 credential로 export 불가<br>+ 입력 검증 + 출력 검토 |
| 쓰기 전용 agent가 file exfil 시도 | 쓰기 경로 한정 + 네트워크 거부<br>+ 실행 시간 제한 |
| 모델 생성 코드 실행 | 격리 sandbox (네트워크 ✗ · secret ✗ · 리소스 제한) |
| 임의 URL 브라우징 | sandbox + allow-list 또는 screening |
| 읽기 전용 작업인데 write 권한 tool | 읽기 전용 제한 또는 tool 제거 |
| tool 35개 중복 → 잘못된 환불 | 최소 권한 축소 · 중복 제거<br>· progressive discovery 검토 |
| 고객 간 데이터 분리 | 호출 전 코드에서 로그인 ID로 filter |
| CEO credential로 agent 실행 | excessive agency + 데이터 노출 |
| prompt 안 DB 비밀번호 | secret manager로 이전<br>tool 계층이 agent 대신 연결 |
| 특정 write tool만 차단 (Claude Code) | deny rule 추가 또는 tool 목록에서 제거 |
| shell 네트워크 + Read의 credential 파일 | `/sandbox` + Read deny rule |
| main 호출 전 입력 선별 + 파싱 가능한 판정 | 경량 모델 boolean 판정 → 코드가 차단 |
| 아동 대상 bot | 코드 입력 screening → PII masking · block<br>자해 신호 → 안전 protocol |
| 모델 업데이트 후 안전 동작 변동 | 코드 출력 screening + 버전 고정 + 회귀 검사 |
| 성공한 injection 탐지 (고트래픽) | 출력 classifier 샘플링 + canary token |
| 정책 영역별 refusal 집계 | `stop_reason` = `refusal`<br>→ `stop_details` 집계 |
| prompt 아닌 결정론적 통제 2개 | 출력 필터 + 한도 tool 권한 |
| 복수 선택 위험 식별 | 간접 injection · excessive agency · 데이터 노출 |
| 자동화 결정의 오결정 책임 | 배포 조직 |

<sub>근거: CCAR-P-Amey-Thakur-0025, CCAR-P-Amey-Thakur-0026, CCAR-P-Amey-Thakur-0060, CCAR-P-jrajath94-0033, CCAR-P-jrajath94-0094, CCAR-P-jrajath94-0208, CCAR-P-jrajath94-0210, CCAR-P-jrajath94-0211, CCAR-P-jrajath94-0212, CCAR-P-jrajath94-0316, CCAR-P-jrajath94-0320, CCAR-P-jrajath94-0374, CCAR-P-jrajath94-0375, CCAR-P-jrajath94-0437, CCAR-P-jrajath94-0438, CCAR-P-jrajath94-0439, CCAR-P-jrajath94-0500, CCAR-P-jrajath94-0501, CCAR-P-jrajath94-0502, CCAR-P-jrajath94-0563, CCAR-P-jrajath94-0564, CCAR-P-jrajath94-0565, CCAR-P-jrajath94-0617, CCAR-P-jrajath94-0631, CCAR-P-jrajath94-0671, CCAR-P-jrajath94-0673, CCAR-P-jrajath94-0684, CCAR-P-preporato-0021</sub>

@@ TRAPS
| 오답 | 이유 |
|---|---|
| 공격 문자열 검사 · TLS로 안전 판단 | 문자열 = 우회 가능<br>TLS = 콘텐츠에 대해 보장 ✗ |
| "조심하라" system prompt | 모델은 문구만으로 구분 불가 |
| tool 호출 log · 주간 검토를 통제로 제시 | 기록 ≠ 예방<br>파일은 첫날에 유출 |
| tool을 숨기되 호출 가능하게 유지 | 숨김 의존 보안 ✗ |
| 거부 예시 추가 학습 · 거부 문구 강화 | 여전히 모델 행동<br>이미 뚫린 통제의 반복 |
| 더 똑똑한 모델로 tool 위험 해결 | 판단력만 구매<br>해결 = 더 작은 tool 범위 |
| prompt 메모로 쓰기 경로 제한 | 코드에서 제한 ✗ → 경계 ✗ |
| 공격 표면 제거로 tool · 기능 삭제 | 업무 기능도 소멸 |
| 전체 레코드 전송 후 "본인 것만" 요청<br>· 출력 스키마로 제한 | 소유권 확인은 모델 수신 전 코드에서 |
| tool search · audit logging으로 tool 차단 | deferred tool은 검색 시 로드<br>log = 권한 종료 ✗ |
| sandbox `denyRead`로 Read tool 차단 | sandbox는 Read tool 미제어 |
| 입력 키워드 검색 · "system" 단어 차단 | 시도만 탐지 · 정상 메시지 차단 |
| 모든 응답을 사람 검토 (고트래픽) | 20,000건/일은 실현 불가 |
| 이전 모델 버전 롤백만 | 같은 단일 실패 지점 유지 |
| HTTP 오류 응답으로 refusal 집계 | refusal = 일반 응답 |
| prompt로 사용자에게 개인 정보 공유 금지 요청 | 사용자 자제에 의존 → 통제 ✗ |
| 기업 VPN 전체 접근 · root 실행<br>· 노트북 직접 실행 | 피해 범위 확대 |
| 지연 · 비용 · 외관<br>· 사소한 hallucination을 위험으로 선택 | 안전 위험 범주 ✗ |
| 책임을 모델 제공자 · 엔지니어에 전가 | 배포 조직이 결과 소유 |

<sub>근거: CCAR-P-Amey-Thakur-0025, CCAR-P-Amey-Thakur-0026, CCAR-P-Amey-Thakur-0060, CCAR-P-jrajath94-0033, CCAR-P-jrajath94-0094, CCAR-P-jrajath94-0208, CCAR-P-jrajath94-0210, CCAR-P-jrajath94-0211, CCAR-P-jrajath94-0212, CCAR-P-jrajath94-0316, CCAR-P-jrajath94-0320, CCAR-P-jrajath94-0374, CCAR-P-jrajath94-0437, CCAR-P-jrajath94-0438, CCAR-P-jrajath94-0439, CCAR-P-jrajath94-0500, CCAR-P-jrajath94-0501, CCAR-P-jrajath94-0502, CCAR-P-jrajath94-0565, CCAR-P-jrajath94-0617, CCAR-P-jrajath94-0631, CCAR-P-jrajath94-0673, CCAR-P-jrajath94-0684</sub>

@@ MEMO
| 이름 | 의미 |
|---|---|
| Indirect prompt injection | 모델이 데이터로 읽는 콘텐츠 속 지시<br>(PDF · 이메일 · 초대장 · DM · 웹 페이지) |
| Excessive agency | 승인 gate 없이 행동 반경이 감독 범위 초과<br>(돈 집행 · 과대 권한) |
| Screen before context | context 조립 · 모델 읽기 전 입력 screening |
| Gate before tool | 돈 · 상태 변경 tool 앞 코드 authorization gate |
| Sandboxing | 쓰기 경로 · 네트워크 · 시간 · secret 접근을 코드로 격리 |
| Canary token | system prompt에 심은 표식<br>출력에 등장 = 유출 입증 |
| Output-side classifier | 샘플링한 출력에서 유출 내용 탐지 |
| `stop_reason` `refusal` · `stop_details` | 거절 = 일반 응답 · 카테고리 = 정책 영역 |
| 기능 비대화 (tool bloat) | tool 많음 · 중복 → 오선택 → tool 남용 |
| deny rule | Claude Code permission rule · tool 호출 차단 |
| 책임 소재 | 자동화 결정의 결과 = 배포 조직 |

<sub>근거: CCAR-P-Amey-Thakur-0026, CCAR-P-Amey-Thakur-0060, CCAR-P-jrajath94-0033, CCAR-P-jrajath94-0208, CCAR-P-jrajath94-0212, CCAR-P-jrajath94-0316, CCAR-P-jrajath94-0375, CCAR-P-jrajath94-0437, CCAR-P-jrajath94-0439, CCAR-P-jrajath94-0501, CCAR-P-jrajath94-0631, CCAR-P-jrajath94-0684</sub>

@@ CHECK
- [ ] 읽는 콘텐츠도 지시 채널 → 읽기 전 screening + 돈 tool 앞 코드 gate
- [ ] "구조적으로 불가능" → 최소 권한 credential · sandbox (prompt ✗)
- [ ] 성공한 공격 탐지 = 출력 측 classifier + canary token
- [ ] 모델 안전장치 변동 → 코드 출력 screening + 버전 고정 + 회귀 검사

<sub>근거: CCAR-P-jrajath94-0033, CCAR-P-jrajath94-0094, CCAR-P-jrajath94-0208, CCAR-P-jrajath94-0211, CCAR-P-jrajath94-0316, CCAR-P-jrajath94-0375, CCAR-P-jrajath94-0437</sub>
