# 7. Security and Safety — 반드시 알아야 할 지식
> 시험 비중 8% · 약 3문항 · 근거 문항 17개

> 커버: CCDV-F D7 · CCAR-P D5(일부) · CCAR-P D3(일부)

## 1. 핵심 개념

### 1.1 Prompt injection: 방어는 구조적으로
**injection 방어 = 분리 + 권한 제한 (모델 바깥)**

| 구분 | 내용 |
|---|---|
| untrusted input | 웹 페이지 · 검색 결과 · fetch 문서 · 사용자 제출 콘텐츠<br>→ 지시 ✗, 데이터로 취급 |
| hidden text 지시 | 동일하게 untrusted 데이터<br>예: 대화 기록 외부 전송 · system prompt 공개 |
| 설계 전제 | 모델은 가끔 주입된 지시를 따름<br>→ 실제 통제 = 모델 바깥의 권한 제한<br>모델 순응 기대 ✗ |

| 공식 | 내용 |
|---|---|
| 분리 | untrusted content와 instructions 분리 |
| 권한 | 위험 capability 미부여 (least privilege)<br>→ 주입 지시가 실행할 tool 없음 → 공격 실패<br>예: fetch · 요약 agent → `send_email` · `delete_file` · refund 불필요 |
| 승인 | 결과가 큰 행동 → guardrail · 사람 승인 뒤 |

| 오답 | 이유 |
|---|---|
| "악성 지시 무시" 한 줄만으로 "해결" 판단 | 도움 가능하나 probabilistic<br>enforcement · 보장 ✗ |

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



![Prompt injection 공격 경로와 모델 바깥의 구조적 방어](svg/7-injection-defense.svg)
*그림: untrusted content의 지시를 모델이 따르더라도, 위험 tool이 없거나 승인 게이트가 있으면 공격은 실패한다*

<sub>근거: Amey-0008, Amey-0033, Amey-0042, Amey-0047, Amey-0064, CCAR-P-Amey-Thakur-0025, CCAR-P-jrajath94-0208, CCAR-P-jrajath94-0212, CCAR-P-jrajath94-0316, CCAR-P-jrajath94-0375, CCAR-P-jrajath94-0437, CCAR-P-jrajath94-0563, Patrick-0013, Patrick-0024, Preporato-0026</sub>

### 1.2 Untrusted 입력 삽입
**사용자 입력 = XML tag로 감싼 데이터**

| 방법 | 판정 | 이유 |
|---|---|---|
| XML tag(`<user_query>` 등)로 감싸기<br>+ system prompt: tag 안 = 데이터, 지시 ✗ 선언 | ✓ | 지시 · 입력 경계 설계 |
| + least privilege · 모델 바깥 enforcement | ✓ | 경계 설계 위에 겹침<br>(1.1과 상충 ✗) |
| 직접 연결<br>(구분자 없이 지시문 중간에 이어 붙임) | ✗ | 지시 · 입력 경계 소멸<br>→ prompt injection 입구 |
| 기호 제거 | ✗ | 효과 = 기호가 문법 의미를 갖는 경우만(SQL · HTML 등)<br>자연어 injection = 문자만으로 작성 → 차단 ✗<br>정상 정보 훼손(화학물질명 · 모델 번호의 기호) |
| 다른 모델로 요약 · 재작성 | ✗ | 세부 정보 손실<br>요약 모델 자신도 injection 영향 가능<br>구조적 분리 대체 ✗ |

![직접 연결과 XML tag 경계 비교](svg/7-xml-tag-wrapping.svg)
*그림: 입력을 XML tag로 감싸고 '데이터'라고 선언해야 경계가 생기며, 기호 제거나 요약은 대안이 아니다*

<sub>근거: Amey-0033, Udemy-0049</sub>

### 1.3 Least privilege와 tool 설계
**금지는 prompt가 아니라 권한으로 강제**

| 구분 | 내용 |
|---|---|
| integration 노출 범위 | 작업에 필요한 operation만<br>건드려도 되는 범위로 축소<br>→ 실수 · 조작 시 피해 범위 제한 |
| 금지 강제 수단 | tool 구성 · hooks<br>executor 내 authorization<br>(prompt ✗) |
| "절대 하면 안 되는 행동" | 해당 tool 미부여로 보장 |
| 외부로 데이터 전송 | 코드 안의 deterministic gate로 차단 · 보류 |

| 오답 | 이유 |
|---|---|
| full credentials + "쓰기 금지" 지시<br>read · write 권한 그대로 부여 | 통제 ✗ → 모델 행동에 의존 |
| schema 없는 범용 tool | "유연함" ✗ → 경계 제거 |

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

**구성 감사: 불필요한 tool · 과대 반환 데이터**

| 상황 | 조치 |
|---|---|
| 역할은 읽기 · 초안 작성뿐<br>agent는 update · delete 가능 | update · delete 기능을 구성에서 제거<br>→ 공격 · 오류 표면 자체 소멸 |
| 프로덕션 레코드 읽기 · 수정 agent | 읽기 · 쓰기 권한 분리<br>쓰기 = 역할상 필요한 곳에만 부여 |
| 6개월 미사용 `drop_table`<br>어떤 작업도 안 쓰는 delete · write tool | 제거 → 미사용 파괴적 tool = 순수 위험<br>제거 전 숨은 호출자 · 6개월 trace 확인 |
| "나중에 유용할 수도" 근거로<br>`delete_event` 유지 주장 | 최소 권한 = 현재 작업 기준<br>→ 지금 제거, 필요해지면 검토 후 재추가 |
| 이름만 필요한 작업에서<br>`list_users`가 전체 SSN 반환 | 반환 필드를 필요한 값(이름)으로 축소<br>→ 데이터 가시성 제한 |
| 행 제한 없는 `export_csv`<br>작업은 최대 100행 | schema에서 100행 상한 → 작업 범위로 한정<br>schema 상한 = 통제 |
| 오해석으로 `delete_account` 호출 사고 | tool 제거 또는 범위 엄격 제한<br>(코드의 확인 단계 · 영향 범위 제한 · 대상 allow-list) |
| 하루 500회 쓰는 `refund`<br>(gate 적용 완료) | 유지 → 민감성은 gate가 처리<br>제거 ✗ |
| 사용 중인 tool | 사용 ≠ 범위 보증<br>schema · 반환 데이터도 최소 권한 점검 대상 |

| 구분 | 내용 |
|---|---|
| 로깅 · 모니터링 · 호출 횟수 dashboard | 포렌식 · 가시성 → 권한은 활성 상태로 잔존<br>"로깅은 제거가 아님" |
| 확인 대화상자 · 업무 시간 제한 | 존재해서는 안 되는 권한을 둘러싼 보완 통제<br>시간 제한 = 노출 시간대만 축소 |
| 예외: 인시던트 대응에 필요한 tool | 제거 ✗ → 감시 · gate 상태로 유지 |
| 범위 제한 설계의 한계 | 범위 확인 · 허용 대상 승인 담당자 필요<br>지나치게 좁은 범위 = 정당한 삭제 차단 |





![행동에 기대는 권한 부여와 모델 바깥 강제 비교](svg/7-least-privilege.svg)
*그림: 금지는 prompt가 아니라 tool 구성·hooks·executor authorization과 deterministic gate로 강제한다*

<sub>근거: Amey-0034, Amey-0042, CCAR-P-Amey-Thakur-0001, CCAR-P-Amey-Thakur-0050, CCAR-P-jrajath94-0094, CCAR-P-jrajath94-0157, CCAR-P-jrajath94-0159, CCAR-P-jrajath94-0212, CCAR-P-jrajath94-0351, CCAR-P-jrajath94-0415, CCAR-P-jrajath94-0438, CCAR-P-jrajath94-0477, CCAR-P-jrajath94-0501, CCAR-P-jrajath94-0540, CCAR-P-preporato-0021, Patrick-0024, Preporato-0026</sub>

### 1.4 Human-in-the-loop (approval gate)
**막을 행동은 미부여 · 위험 행동은 승인**

| 상황 | 조치 |
|---|---|
| consequential · irreversible<br>· destructive tool | human approval gate 뒤에 배치<br>→ least privilege를 빠져나간 것 포착 |
| 꼭 막아야 하는 행동 | tool 미부여 (승인보다 우선) |

| 오답 | 이유 |
|---|---|
| 모델에 "환불 전 확인" 지시 | enforcement ✗ |

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

**쓰기 · 대량 반출의 gate 위치**

| 상황 | 정답 |
|---|---|
| 프로덕션 레코드 쓰기 agent | 쓰기를 명시적 승인 뒤에 배치<br>+ 읽기 · 쓰기 권한 분리<br>→ 모니터링 ✗, 공격 표면 자체 축소 |
| 정책: 1,000행 초과 export는 관리자 승인 | export tool 실행 전 코드에서 검사<br>행 수 계산 → 승인 token 요구<br>→ token 없으면 거부 |

| 오답 | 이유 |
|---|---|
| system prompt에 승인 규칙 기재 | 지침일 뿐 → 강제 ✗ |
| 다운로드 완료 후 감사 | 유출 이후 → 보완책일 뿐 단독 충분 ✗ |
| 분석가의 기억에 의존 | 통제 아님 |





![human approval gate 판단 흐름](svg/7-approval-gate.svg)
*그림: 꼭 막을 행동은 tool을 주지 않고, consequential 행동만 사람 승인 뒤에 실행한다*

<sub>근거: Amey-0042, CCAR-P-Amey-Thakur-0050, CCAR-P-jrajath94-0036, CCAR-P-jrajath94-0207, CCAR-P-jrajath94-0220, CCAR-P-jrajath94-0317, CCAR-P-jrajath94-0354, CCAR-P-jrajath94-0377, CCAR-P-jrajath94-0436, CCAR-P-jrajath94-0441, CCAR-P-jrajath94-0499, CCAR-P-jrajath94-0504, CCAR-P-jrajath94-0677, Patrick-0013, Patrick-0024, Preporato-0026</sub>

### 1.5 Authorization 전파
**tool 실행 = 호출 사용자의 검증된 token 기준**

| 방식 | 판정 | 이유 |
|---|---|---|
| 강한 권한의 공유 service account 하나로 전 사용자 처리 | ✗ | 사용자별 authorization · audit trail 소멸<br>→ 모델 = 강한 권한 대리인<br>→ 타인 데이터 조회 가능 |
| 호출 사용자의 identity · 권한으로 실행<br>+ tool 호출마다 사용자 기준 log | ✓ | 근본 해결 |
| MCP: 앱이 로그인 사용자의 검증된 token을 요청에 첨부<br>→ server가 매번 접근 범위 판정 | ✓ | 사용자 식별 = 검증된 token<br>(client · 모델이 넘긴 값 ✗) |
| 대상 사용자 ID를 모델이 tool argument로 전달 | ✗ | 원래와 같은 결함<br>argument 값 = 모델이 결정<br>→ 대화로 유도 시 타인 ID 삽입 가능 |
| 출력 검사만으로 대체<br>(다른 모델로 이름 확인) | ✗ | 보조 수단일 뿐<br>authorization 대체 ✗<br>권한 밖 데이터는 이미 모델이 읽은 상태 |

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

**귀속(attribution) · 사용자별 위임**

| 상황 | 정답 |
|---|---|
| ERP를 공유 서비스 credential로 호출<br>오입력 후 지시자 특정 필요 | 사용자별 위임<br>= agent가 요청 사용자 ID로 동작<br>→ ERP가 사용자 권한 강제 · 기록 |
| 3개 팀이 공유 API key 사용<br>사고 조사에서 호출 팀 귀속 필요 | 팀별 credential(또는 token)<br>→ 각 호출이 호출자 신원 포함 |
| 사내 어시스턴트 → 원격 MCP server<br>server가 요청 직원 기록 필요 | 사용자별 OAuth token을<br>server의 `authorization_token`에 전달<br>→ server가 bearer token으로 로그인 사용자 식별 |
| 주문 조회 agent에<br>회사 master API key 부여 | ambient authority → confused deputy<br>→ 좁은 scope의 사용자별 위임 token |

| 구분 | 내용 |
|---|---|
| 규칙 | 귀속이 중요하면 공유 credential ✗ |
| 필요 조건 | identity provider가 사용자별 token 발급<br>대상 시스템이 token을 권한에 매핑 |
| 기록 기준 | system of record(ERP)의 로그<br>앱 로그의 이름 ✗ |
| 한계 | ID 배관 구축 → 공유 secret 하나보다 무거움 |

**신뢰 경계를 넘는 token**

| 구분 | 내용 |
|---|---|
| bearer token → partner API | audience 바인딩 + 수신 시 바인딩 확인<br>→ 잘못된 서비스에서의 재사용(replay) 차단 |
| 자사 청구 시스템의 환불 | 인가 = 소유 시스템에서 결정론적 강제<br>+ fail closed<br>→ 모델이 틀려도 무단 환불 차단 |
| 한계 | partner의 바인딩 확인 협조 필요<br>청구 시스템에 승인 기록 통합 필요 |

**사용자 제공 값 = 주장(claim)**

| 설계 | 판정 | 이유 |
|---|---|---|
| 채팅에 입력한 clinic 이름 · `tenant_id`로 filter | ✗ | 사용자가 스스로 선언한 값<br>→ 타 clinic · tenant 데이터 접근 |
| 드롭다운 선택 · 편집 가능한<br>profile `company` 필드로 filter | ✗ | 선택 · 편집 = 사용자 주장<br>→ 값 한 번 변경으로 타 사 데이터 열람 |
| 코드가 인증된 신원의 소속을<br>명단과 대조해 filter | ✓ | 검증된 신원이 결정<br>데이터 읽기 전에 실행 |
| 값이 서버 설정 · 검증된 세션에서 옴 | ✓ | 사용자가 바꿀 수 없는 값일 때만 성립 |
| 로그인 확인 후 입력한 이름의 학생 전부 표시 | ✗ | authentication만 존재<br>login = 신원 증명, 해당 학생을 볼 권리 확인 ✗<br>→ 보호자 명단 대조 코드 검사 필요 |
| 답변 생성 뒤에 filter | ✗ | 데이터를 이미 읽은 뒤 → 유출 발생 |

**부작용 tool 앞 authorization 검사 위치**

| 위치 | 판정 | 이유 |
|---|---|---|
| tool 실행 전 코드<br>호출자 신원 + 권한 확인 → 허용 · 거부 | ✓ | 부작용 이전에 결정<br>결정적 · 감사 가능 |
| system prompt 규칙 | ✗ | 통제 수단 아님 (prompt 함정) |
| tool 실행 후 audit log | ✗ | 이미 변경됨<br>→ 보완책으로만 유효 |
| 대화가 그럴듯한지 모델이 판단 | ✗ | 모델 = 신원 · 정책 · 잠금장치 ✗<br>→ authorization 주체 금지 |

| 구분 | 내용 |
|---|---|
| 한계 | 명단 · 보호자-학생 mapping 최신 유지 필요<br>낡으면 정당한 요청 차단 또는 이전 사용자 허용 |





![공유 service account, 모델이 넘기는 ID, 검증된 token 비교](svg/7-authorization-propagation.svg)
*그림: 사용자 식별은 검증된 token에서 얻고 server가 요청마다 권한을 판정해야 한다*

<sub>근거: CCAR-P-jrajath94-0160, CCAR-P-jrajath94-0161, CCAR-P-jrajath94-0298, CCAR-P-jrajath94-0305, CCAR-P-jrajath94-0353, CCAR-P-jrajath94-0416, CCAR-P-jrajath94-0417, CCAR-P-jrajath94-0479, CCAR-P-jrajath94-0480, CCAR-P-jrajath94-0502, CCAR-P-jrajath94-0542, CCAR-P-jrajath94-0617, CCAR-P-jrajath94-0632, Preporato-0028, Udemy-0041</sub>

### 1.6 API key / secret 관리
**노출 key → rotate · 서버 보관**

| 상황 | 조치 |
|---|---|
| browser JavaScript에 key | 클라이언트 전송분 → 사용자 열람 가능<br>→ key rotate + key를 가진 backend로 호출 이전 |
| repository · system prompt template 속 key | 이미 노출<br>→ rotate 후 env var · secret manager 보관 |
| credential 사용 위치 | tool 실행 코드의 인증 시만<br>모델 context(prompt) 투입 ✗<br>→ 모델은 credential 미열람 |

| 오답 | 이유 |
|---|---|
| 난독화(obfuscation) · local storage<br>클라이언트 코드 내 IP 제한 | key가 여전히 클라이언트에 있음<br>또는 우회 가능 |
| Base64 인코딩 | 즉시 복원 가능 |
| "key 공개 금지" 지시 | probabilistic |
| key를 prompt 끝으로 이동 | 여전히 prompt 안 |

**prompt 안 secret의 전파 경로**

| 상황 | 조치 |
|---|---|
| system prompt에 production DB 비밀번호<br>("직접 연결"용) | prompt = credential 저장소 ✗<br>prompt를 거치는 모든 시스템이 비밀번호 획득<br>(log · cache · vendor) |
| 연결 방식 | secret manager로 이전<br>tool 계층이 agent 대신 DB 연결 |
| "비밀번호가 필요하니 문제 없음" | 오답 → 필요 = tool 계층의 몫 |

**설정 파일 속 개인 credential**

| 상황 | 조치 |
|---|---|
| 개발자 개인 credential을<br>공유 설정에 하드코딩<br>→ 내부 tool이 DB 호출 | 귀속 ✗ · rotation ✗<br>개발자 퇴사 시 credential도 이탈<br>→ 범위 제한 접근의 서비스 ID로 교체 |





![API key 관리 흐름](svg/7-secret-management.svg)
*그림: 노출된 key는 rotate하고 서버 쪽 secret manager에 두며, tool 코드만 인증에 쓰고 모델은 credential을 보지 않는다*

<sub>근거: CCAR-P-jrajath94-0543, CCAR-P-jrajath94-0564, Patrick-0043, Preporato-0027</sub>

### 1.7 PII 보호: 데이터 최소화
**PII 보호 = 유출 확산 범위 최소화**

| 구분 | 내용 |
|---|---|
| 기본 원칙 | data minimization + least privilege<br>"모델에 보여 주는 것" · "모델이 접근 가능한 것" 모두 최소 |
| 방법: 전달 | 작업에 필요한 항목만 전달<br>직접 식별자(이름 등) → 전송 전 masking · tokenization(임시 ID) |
| 방법: 접근 · 기록 | tool 접근 범위 = 담당 대상 한정<br>log · URL에 PII 미기록 |
| audit log | 정당한 운영<br>이름 든 전문 그대로 저장 → 유출 경로 증가<br>→ masking 또는 항목 한정 필요 |
| TLS · 저장 시 암호화 | 전송 경로 · 보관 보호 |
| 판단 기준 | "유출되면 어디까지 퍼지는가"<br>→ 범위가 가장 작은 선택지 |

| 오답 | 이유 |
|---|---|
| 전체 사용자 기록을 system prompt에 상주 | injection 1회 · 잘못된 출력 1회<br>→ 담당 밖 정보까지 유출 가능 |
| TLS · 저장 시 암호화로 최소화 대체 | 모델 출력 · injection을 통한<br>유출 위험 감소 ✗ |

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



![PII 최소화 dataflow](svg/7-pii-minimization.svg)
*그림: 필요한 항목만 masking해 넘기고 tool 범위를 좁혀, 유출 시 퍼지는 범위를 최소로 만든다*

<sub>근거: CCAR-P-Amey-Thakur-0008, CCAR-P-Amey-Thakur-0024, CCAR-P-Amey-Thakur-0041, CCAR-P-Amey-Thakur-0059, CCAR-P-jrajath94-0034, CCAR-P-jrajath94-0093, CCAR-P-jrajath94-0562, CCAR-P-preporato-0024, Udemy-0039</sub>

### 1.8 출력 처리 (output handling)
**모델 출력 = untrusted → 렌더링 전 escape**

| 방법 | 판정 | 이유 |
|---|---|---|
| 모델 출력 → web page 렌더링 전 반드시 escape · sanitize | ✓ | untrusted (입력의 영향 가능)<br>출처 무관 |
| "markup 생성 금지" 지시 | ✗ | 통제 ✗ |

![모델 출력 처리 흐름](svg/7-output-handling.svg)
*그림: 모델 출력은 입력의 영향을 받는 untrusted 데이터이므로 렌더링 전에 escape/sanitize한다*

<sub>근거: Amey-0079</sub>

### 1.9 Guardrail 다층 방어 (defense in depth)
**guardrail = 사전 차단 층 + 사후 탐지 층**

| 구분 | 내용 |
|---|---|
| 원칙 | 어떤 대책도 단독으로는 빠져나갈 여지<br>→ 입력 · 지시 · 출력 · 운영 monitoring 각 단계에 층 중첩 |
| 공식 권장 조합: 입력 · 지시 | 경량 모델(Haiku 계열)의 harmlessness screen<br>알려진 공격 패턴 입력 검증<br>경계 · 거절 방식을 명시한 system prompt |
| 공식 권장 조합: 운영 · 출력 | 반복 위반자 대응<br>출력 filter + 지속적 monitoring |
| 출시 전 red teaming | 중요하나 단독 부족<br>→ 가동 후 새 표현 · 수법 등장 |
| 규제 업종(금융 등) | 사전 차단 층 · 사후 탐지 층 모두 존재 여부 확인 |
| prompt 강화 · 출력 검사 | 다층 방어의 한 층으로 가치<br>단독 = probabilistic 대책 |

**입력 screening 설계 (모델 호출 전)**

| 상황 | 정답 |
|---|---|
| 자유 텍스트 → main 호출 전 검사<br>코드가 셀 수 있는 판정 필요 | 경량 모델이 각 메시지 선별<br>→ structured output = boolean 판정<br>→ 유해 판정이면 코드가 차단 |
| 아동(8~12세) 대상 bot<br>(PII · 자해 신호 입력) | 코드 입력 screening (모델 노출 전)<br>PII 탐지 → masking 또는 block<br>자해 신호 → 안전 protocol로 route |
| 경량 모델 예시 | Haiku 5.5 |

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



![guardrail 다층 방어 구조](svg/7-defense-in-depth.svg)
*그림: 입력·지시·출력의 사전 차단 층과 monitoring 사후 탐지 층을 겹쳐 빠져나간 공격을 잡는다*

<sub>근거: CCAR-P-jrajath94-0320, CCAR-P-jrajath94-0671, Udemy-0041, Udemy-0050</sub>

### 1.10 Sandboxing: 실행 경계는 모델 밖에서
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

### 1.11 Claude Code 차단 수단: permission rule · sandbox
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

![Claude Code 실행 경계: prompt 메모와 sandbox 비교, 경로별 차단 수단](svg/7-sandbox-boundary.svg)
*그림: 실행 경계는 prompt 메모가 아니라 모델 밖의 sandbox와 permission rule이 지키며, 막으려는 경로마다 수단이 다르다*

<sub>근거: CCAR-P-jrajath94-0631, CCAR-P-jrajath94-0673</sub>

### 1.12 운영 monitoring · 모델 안전장치 변동 대응
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

### 1.13 위험 식별: 시나리오 신호 → 위험 이름
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

<sub>근거: CCAR-P-jrajath94-0212, CCAR-P-jrajath94-0316, CCAR-P-jrajath94-0375, CCAR-P-jrajath94-0439, CCAR-P-jrajath94-0502, CCAR-P-jrajath94-0565</sub>

### 1.14 자동화 결정의 책임 소재
**자동화해도 결과 책임은 배포 조직**

| 주체 | 판정 | 이유 |
|---|---|---|
| 배포 조직 | ✓ | 자동화 결정을 배포 = 결과 소유 |
| 모델 제공자 | ✗ | 기능만 공급 |
| prompt 작성 엔지니어 | ✗ | 개인의 작성이 조직 책임을 이전 못 함 |
| "자동화라 아무도 없음" | ✗ | 자동화 ≠ 책임 소멸 |

- 자동화의 경계 = 아키텍처상의 결정

<sub>근거: CCAR-P-Amey-Thakur-0026, CCAR-P-Amey-Thakur-0060</sub>

### 1.15 Fail-closed 기본값 (검사 불능 시 거부)
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

![검사 불능 시 거부하는 fail-closed gate 흐름](svg/7-fail-closed.svg)
*그림: 검사를 못 하면 위험 행동은 거부하고, 가동시간을 위한 fail-open 전환은 공격 창이 된다*

<sub>근거: CCAR-P-jrajath94-0207, CCAR-P-jrajath94-0209, CCAR-P-jrajath94-0373, CCAR-P-jrajath94-0436</sub>

### 1.16 위험 평가 (출시 전 테스트 · 등록부 · 실패 모드)
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

### 1.17 위험별 통제 · incident 대응 · kill switch
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
| ⚠️ Default Workspace | 해설 "spend limit 불가"와 달리 공식 문서:<br>Google Cloud · Claude Platform on AWS만 불가<br>Console은 설정 가능하나 일부 사용 미집계 |
| rate limit | 분당 요청 수 제어 ≠ 월 지출 제어 |
| 사용량 보고서 | 현황 확인용 → 사용 중단 ✗ |
| 사고 대응의 본질 | 대응 = 종료 · revoke · 격리 · 알림<br>더 나은 모델 · tier 업그레이드 ✗ |
| 한계 | 버전 고정 = 새 모델 채택 지연 · 회귀 suite 유지보수<br>업데이트 검토 = 기능 출시 지연<br>run 종료 = 정당한 진행 작업 중단 가능 |
| 격리 비용 | 분석가 시간 필요 → 대안보다 나음 |
| 버전 변경 감지 | 벤더 변경 로그 ✗ → 팀 자체 회귀 실행 |

![red team과 risk register에서 위험별 통제, incident 대응 순서로 이어지는 흐름](svg/7-risk-control-incident.svg)
*그림: 위험마다 예방 · 탐지 · 복구를 짝짓고, 사고가 나면 종료 · revoke · 격리 · 알림 순서로 대응한다*

<sub>근거: CCAR-P-jrajath94-0213, CCAR-P-jrajath94-0214, CCAR-P-jrajath94-0215, CCAR-P-jrajath94-0321, CCAR-P-jrajath94-0585</sub>

### 1.18 감사 증거 · 추적성 (audit log)
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

### 1.19 공정성 평가 (bias · 하위 그룹 측정)
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

![합산 점수와 하위 그룹별 측정 및 출시 gate 흐름](svg/7-fairness-subgroup.svg)
*그림: 합산 수치는 그룹 격차를 가리므로 그룹별 기준선으로 출시를 막고 원인은 상류에서 고친다*

<sub>근거: CCAR-P-jrajath94-0039, CCAR-P-jrajath94-0091, CCAR-P-jrajath94-0227, CCAR-P-jrajath94-0228, CCAR-P-jrajath94-0230, CCAR-P-jrajath94-0319, CCAR-P-jrajath94-0444, CCAR-P-jrajath94-0507, CCAR-P-jrajath94-0570, CCAR-P-jrajath94-0685</sub>

### 1.20 투명성 · AI 고지 · 이의 신청
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

![고지 · 설명 · 이의 신청이 trace에서 생성되는 흐름](svg/7-transparency-flow.svg)
*그림: 설명과 고지는 trace가 뒷받침하는 이유만 진술하고, 연결되지 않으면 출시를 막으며 이의 신청 경로를 둔다*

<sub>근거: CCAR-P-jrajath94-0042, CCAR-P-jrajath94-0229, CCAR-P-jrajath94-0231, CCAR-P-jrajath94-0381</sub>

### 1.21 보존(retention)·삭제 설계
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
| 보존 기간을 2년으로 연장 | 편의와 규칙 맞교환<br>침해 표면 24배 증가<br>⚠️ 해설 수치 · 90일→2년은 약 8배 (공식 문서 미확인) |
| 다음 인시던트 검토까지 삭제 중단 | 담당자 · 일자 없음 → 중단이 영구화 |
| 영구 보관 + 시니어 접근 제한 | 독자 목록만 줄인 "모두 보관"<br>일수 미정 |
| 모든 티켓 하루 후 삭제 | 비즈니스 · 규제 증거 파괴<br>규칙이 실제로 요구할 때만 정답 |
| 사본이 남은 상태의 삭제 이행 | 백업 · 평가 샘플에 남으면 삭제 무의미 |

![보존 규칙에서 예약 삭제와 삭제 요청 이행으로 이어지는 흐름](svg/7-retention-deletion.svg)
*그림: 보존은 기간 · 담당자 · 삭제 경로를 갖춘 규칙이며, 예약 삭제와 요청 삭제 모두 삭제 로그로 증거를 남긴다*

<sub>근거: CCAR-P-Amey-Thakur-0071, CCAR-P-jrajath94-0037, CCAR-P-jrajath94-0093, CCAR-P-jrajath94-0222, CCAR-P-jrajath94-0225, CCAR-P-jrajath94-0318, CCAR-P-jrajath94-0380, CCAR-P-jrajath94-0505</sub>

### 1.22 규제 프레임워크 매핑 (GDPR · HIPAA · FedRAMP)
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

![데이터 유형 · 관할권에서 프레임워크와 Claude 쪽 선택으로 이어지는 매핑](svg/7-regulatory-mapping.svg)
*그림: 데이터 유형과 관할권이 프레임워크를 정하고, 프레임워크가 설계 요구와 ZDR · BAA · 인가 경로 선택을 정한다*

<sub>근거: CCAR-P-Amey-Thakur-0044, CCAR-P-jrajath94-0037, CCAR-P-jrajath94-0038, CCAR-P-jrajath94-0040, CCAR-P-jrajath94-0092, CCAR-P-jrajath94-0226, CCAR-P-jrajath94-0318, CCAR-P-jrajath94-0443, CCAR-P-jrajath94-0506, CCAR-P-preporato-0023</sub>

### 1.23 HIPAA · BAA 적용 범위
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
| HIPAA readiness 범위 | 공식 문서: HIPAA readiness = Claude API 조직(Console)<br>Bedrock · Google managed = 각 플랫폼 문서 확인 |

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

### 1.24 Zero data retention (ZDR)
**ZDR = 조직별 활성화 · 기능별 적격 · Console 제외**

| 구분 | 내용 |
|---|---|
| 의미 | 응답 반환 후 Anthropic이 prompt · response를 at rest 저장 ✗ |
| 활성화 | account team이 조직별로 활성화 |
| 적격 여부 | 기능마다 다름<br>→ 출시 전 사용 기능을 각각 확인 |
| 범위 밖 | Console 사용 (playground 포함)<br>→ 규제 데이터를 playground에 입력 ✗<br>→ 해당 조직 key로 API 호출만 사용 |
| HIPAA readiness와 차이 | HIPAA readiness = 보호 장치 추가<br>각 응답 후 삭제 요구 ✗<br>"저장 안 함" 요구에 부적합 |
| 계약상 비학습 | DPA + ZDR(또는 문서화된 비학습) 조건 |
| ⚠️ 시점 변동 | ZDR 적격 기능 · 제외 범위는 계약 · 문서에 따라 바뀜<br>공식 문서: Legacy ZDR · HIPAA readiness · EFS ZDR(beta)로 구분<br>해설은 "ZDR" 하나로 서술 (문서상 = Legacy ZDR) |

| 오답 | 이유 |
|---|---|
| platform activity log 활성화 | 데이터 통제처럼 보이나 ZDR 활성화 ✗ |
| 규제 prompt를 Console playground에 두기 | ZDR이 Console 미포함 |
| 기본 retention 유지 + 클라이언트 측 암호화 | Anthropic 쪽 저장 유지 → "저장 금지" 계약 미충족 |
| HIPAA readiness로 각 응답 후 저장 차단 | 보호 장치일 뿐 삭제 요구 ✗ |

<sub>근거: CCAR-P-jrajath94-0037, CCAR-P-jrajath94-0595, CCAR-P-jrajath94-0680</sub>

### 1.25 Data residency
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
| `inference_geo` 지원 범위 | 지원 = Claude 4.6 이상 모델 · 지원 플랫폼 한정 (공식 문서 기준)<br>Bedrock · Google managed = 엔드포인트 · profile이 리전 결정 |

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

<sub>근거: CCAR-P-jrajath94-0037, CCAR-P-jrajath94-0222, CCAR-P-jrajath94-0224, CCAR-P-jrajath94-0318, CCAR-P-jrajath94-0568, CCAR-P-jrajath94-0681</sub>

### 1.26 FedRAMP · 인가 환경 배포
**FedRAMP = 서비스 경계에 귀속 · 경로가 곧 요구사항**

| 구분 | 내용 |
|---|---|
| 인가의 귀속 | 서비스 경계에 귀속<br>상용 직접 API = 인가 ✗ (해설 기준) |
| 인가 경로 | Claude for Government (Anthropic FedRAMP High 플랫폼)<br>AWS Bedrock GovCloud · Vertex AI Assured Workloads<br>→ 해당 클라우드 인가 상속 |
| 감사자 확인 대상 | audit logging + 인가 경계(authorization boundary) 문서화 |
| 첫 아키텍처 조치 | deployment-route 행 구축<br>= 승인 환경 실행 + baseline 통제별 담당자 · 증거 매핑<br>+ 검토 주기 설정 |
| 선행 의존성 | 조달 리드 타임 · 기관의 통제 목록<br>→ 시간 · 비용 · 운영 제약을 예산에 반영 |
| 우선순위 | 단순함 < 조달 규정<br>보안 기능이 승인 환경 대체 ✗ |
| ⚠️ 시점 변동 | 인가 상태 · 경로(플랫폼 · 인가 수준)는 바뀜<br>공식 문서: FedRAMP High · IL4 · IL5 필요 시<br>Bedrock 권고 · 그 외 경로 (공식 문서 미확인) |

| 오답 | 이유 |
|---|---|
| "FedRAMP는 인프라용, AI API는 대상 아님" | 기관 데이터를 다루는 AI API도 범위 |
| 직접 API가 통제를 충족한다는 자체 증명 | 자체 증명 ≠ 인가 → 조달 심사 탈락 |
| 분석가 노트북에서 실행 | 중앙 로깅 · 패치 통제 없음<br>기관 요구 회피 ✗ |
| 상용 리전 + 전체 암호화 | 잘못된 환경 · 암호화는 배포 문제의 대체 ✗ |
| 로그인 페이지의 정부 사용 고지 | 고지일 뿐 통제 ✗ |
| 기관에 "모델이 안전하다" 약속 | 기관 요구 = 약속이 아닌 baseline |

<sub>근거: CCAR-P-jrajath94-0040, CCAR-P-jrajath94-0226</sub>

### 1.27 컴플라이언스 증거 체인과 감사 로그
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

![요구사항 · 통제 · 담당자 · 증거 · 주기 5고리 증거 체인](svg/7-audit-evidence-chain.svg)
*그림: 통제 이름만으로는 미완결이며 5고리가 모두 있어야 감사 증거가 된다*

<sub>근거: CCAR-P-Amey-Thakur-0008, CCAR-P-Amey-Thakur-0041, CCAR-P-jrajath94-0038, CCAR-P-jrajath94-0040, CCAR-P-jrajath94-0222, CCAR-P-jrajath94-0224, CCAR-P-jrajath94-0225, CCAR-P-jrajath94-0226, CCAR-P-jrajath94-0318, CCAR-P-jrajath94-0379, CCAR-P-jrajath94-0442, CCAR-P-jrajath94-0505, CCAR-P-jrajath94-0506, CCAR-P-jrajath94-0569</sub>

### 1.28 서드파티 MCP server 신뢰 경계
**tool description = 공격자가 쓸 수 있는 입력**

| 구분 | 내용 |
|---|---|
| 주입 경로 | 서드파티 server의 description · schema<br>= 모델 입력 → 악의 · 침해 server가 지시 주입<br>예: description 읽은 뒤 API key 유출 시도 |
| 근본 원인 | 프로토콜 결함 ✗<br>= 신뢰 불가 콘텐츠 |
| 완화 | MCP tool schema = untrusted 입력으로 취급<br>server 버전 고정 → 조용한 업데이트 차단<br>파괴적 tool call = sandbox 또는 확인 gate |
| sandbox · gate의 역할 | 가로채진 호출이 할 수 있는 일을 제한 |

**결제 tool을 가진 서드파티 server**

| 구분 | 내용 |
|---|---|
| 전제 | description · server가 악의적이라 가정<br>그래도 승인 없는 자금 이동 불가 |
| 통제 1 | server = untrusted 취급 · 검토된 버전 고정<br>최소 권한 credential (단독 자금 이동 불가)<br>자체 시스템 안 사람 동의 (결제 실행 전) |
| 통제 2 | tool 결과 검증<br>결제 승인 = 효과를 수행하는 계층의 자체 코드에서 강제<br>→ 설명만으로 자금 이동 유발 ✗ |
| 원칙 | 결제 결정이 제3자의 말에 의존 ✗ |

| 오답 | 이유 |
|---|---|
| MCP 프로토콜 탓 → 사용 중단 · 전부 직접 재작성 | 결함 = 신뢰 불가 콘텐츠<br>공격 경로 미해결 · MCP 가치 상실 |
| 유출 후 key만 삭제 | 증상만 처리<br>다음 시도 · 주입 경로 미해결 |
| 벤더 SOC 2 보고서 · 훌륭한 description 신뢰 | 보고서 = 벤더 통제 설명<br>이 server에 결제 권한을 줘도 안전한지 ✗<br>description = 여전히 untrusted |
| prompt에 "두 번 요청 전 결제 금지" | 우회 가능 (prompt-plea 함정) |

<sub>근거: CCAR-P-jrajath94-0008, CCAR-P-jrajath94-0079</sub>

## 2. 상황별 정답 판단 규칙

| 상황 | 정답 |
|---|---|
| fetch한 웹 페이지 · 문서에 "이전 지시를 무시하고 ~하라" | content = untrusted 데이터<br>권한은 모델 바깥에서 제한 |
| 요약 agent에 email · 삭제 · 환불 tool<br>+ injection 당함 | 해당 tool 제거 (least privilege)<br>남는 consequential tool → human approval 뒤 |
| "agent가 절대 X 금지" 보장 위치 | X tool 미부여<br>tool configuration · hooks로 강제 |
| 외부 주소로 데이터 전송 위험 (2개 선택) | 코드의 deterministic gate<br>+ least privilege (tool 제거 또는 승인) |
| integration에 DB 접근 부여 | 필요한 operation만, 범위 축소 노출 |
| 공유 service account로 타인 데이터 유출 | 호출 사용자의 identity · 권한으로 실행<br>사용자 기준 log |
| MCP tool이 전 데이터 읽기 가능, 제한은 prompt에만 | 로그인 사용자 token을 요청에 첨부<br>server 쪽 권한 판정 |
| browser JS에 API key | rotate + backend proxy로 이전 |
| repo · prompt template에 key | rotate 후 env var · secret manager<br>tool 코드가 인증 → 모델은 credential 미열람 |
| PII 포함 데이터를 Claude에 전달 | 필요한 항목만 · 직접 식별자 masking<br>tool 권한 축소 |
| 사용자 자유 기술 입력을 template에 삽입 | XML tag로 감싸기<br>system prompt에 "tag 안 = 데이터" 선언 |
| 모델 출력을 HTML에 렌더링 | untrusted 취급 → escape · sanitize |
| 규제 업종 chatbot의 견고한 guardrail | 입력 screen + system prompt 거절 방침<br>+ 출력 filter + monitoring 다층 |
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
| 역할은 읽기 · 초안뿐인데 update · delete 가능 | 해당 기능을 구성에서 제거<br>(로깅 · 확인창 · 시간 제한 ✗) |
| 프로덕션 읽기 · 수정 agent | 읽기 · 쓰기 권한 분리<br>쓰기는 필요한 역할에만 + 명시적 승인 뒤 |
| 미사용 write · destructive tool<br>(`drop_table` · `delete_employee`<br>· `write_policy`) | 제거 (숨은 호출자 확인 후)<br>"나중에 유용" 근거 유지 ✗ |
| 작업에 불필요한 PII(SSN)를 반환하는 tool | 반환 필드를 필요한 값만으로 축소 |
| export 행 수 무제한, 작업은 100행 | schema에 100행 상한 |
| 삭제 tool이 오해석으로 호출된 사고 | tool 제거 또는 범위 제한<br>(코드 확인 · 영향 범위 제한 · allow-list)<br>로깅만 추가 ✗ |
| 서드파티 MCP description을 읽고<br>agent가 key 유출 시도 | description · schema = untrusted 입력<br>→ 버전 고정 + 파괴적 호출 sandbox · 확인 gate |
| 악의적이어도 자금 이동 불가여야 하는 서드파티 결제 server | 최소 권한 credential + 사람 동의<br>+ 결제 승인을 자체 코드(효과 계층)에서 강제 |
| 채팅 · 드롭다운 · 편집 가능 profile이<br>준 tenant 값으로 filter | 값 = 주장(claim)<br>→ 코드가 인증된 신원의 소속으로 filter |
| login은 확인하나 입력한 이름의 학생 전부 표시 | authentication만 있고 authorization 없음<br>→ 보호자 명단 대조 코드 검사 |
| 성적 변경 등 부작용 tool의 권한 검사 위치 | tool 실행 전 코드<br>(호출자 신원 + 권한 확인 → 허용 · 거부) |
| 1,000행 초과 export는 관리자 승인 | tool 실행 전 코드: 행 수 계산<br>→ 승인 token 요구 → 없으면 거부 |
| agent에 회사 master API key | ambient authority · confused deputy<br>→ 좁은 scope의 사용자별 위임 token |
| 공유 서비스 credential + 감사에서 지시자 특정 필요 | 사용자별 위임<br>(요청 사용자 ID로 동작 → 대상 시스템이 권한 강제) |
| 여러 팀이 공유 API key + 호출 팀 귀속 필요 | 팀별 credential(또는 token) |
| 원격 MCP server가 요청 직원 기록 필요 | 사용자별 OAuth token을<br>`authorization_token`에 전달 |
| bearer token이 신뢰 경계를 넘어 partner API로 이동 | audience 바인딩 + 수신 시 확인<br>환불 인가는 청구 시스템에서 결정론적 강제 · fail closed |
| 개발자 개인 credential이 설정에 하드코딩 | 범위 제한 접근의 서비스 ID |

![injection과 tool 통제 판단 트리](svg/7-decision-injection-tools.svg)
*그림: 외부 content의 지시와 위험 tool은 모델 바깥(tool 제거·hooks·gate·범위 축소)에서 통제한다*

![권한·secret·PII 판단 트리](svg/7-decision-identity-secrets.svg)
*그림: 권한은 사용자 token으로, key는 rotate 후 서버에, PII는 최소화·masking으로 다룬다*

![입력·출력·guardrail 판단 트리](svg/7-decision-io-guardrails.svg)
*그림: 입력은 XML tag로 감싸고, 출력은 escape하고, guardrail은 다층으로 쌓는다*

<sub>근거: Amey-0008, Amey-0033, Amey-0034, Amey-0042, Amey-0064, Amey-0079, CCAR-P-Amey-Thakur-0001, CCAR-P-Amey-Thakur-0008, CCAR-P-Amey-Thakur-0024, CCAR-P-Amey-Thakur-0025, CCAR-P-Amey-Thakur-0026, CCAR-P-Amey-Thakur-0041, CCAR-P-Amey-Thakur-0044, CCAR-P-Amey-Thakur-0050, CCAR-P-Amey-Thakur-0059, CCAR-P-Amey-Thakur-0060, CCAR-P-Amey-Thakur-0071, CCAR-P-jrajath94-0008, CCAR-P-jrajath94-0033, CCAR-P-jrajath94-0034, CCAR-P-jrajath94-0036, CCAR-P-jrajath94-0037, CCAR-P-jrajath94-0038, CCAR-P-jrajath94-0039, CCAR-P-jrajath94-0040, CCAR-P-jrajath94-0041, CCAR-P-jrajath94-0042, CCAR-P-jrajath94-0079, CCAR-P-jrajath94-0091, CCAR-P-jrajath94-0092, CCAR-P-jrajath94-0093, CCAR-P-jrajath94-0094, CCAR-P-jrajath94-0095, CCAR-P-jrajath94-0096, CCAR-P-jrajath94-0157, CCAR-P-jrajath94-0159, CCAR-P-jrajath94-0160, CCAR-P-jrajath94-0161, CCAR-P-jrajath94-0207, CCAR-P-jrajath94-0208, CCAR-P-jrajath94-0209, CCAR-P-jrajath94-0210, CCAR-P-jrajath94-0211, CCAR-P-jrajath94-0212, CCAR-P-jrajath94-0213, CCAR-P-jrajath94-0214, CCAR-P-jrajath94-0215, CCAR-P-jrajath94-0220, CCAR-P-jrajath94-0222, CCAR-P-jrajath94-0223, CCAR-P-jrajath94-0224, CCAR-P-jrajath94-0225, CCAR-P-jrajath94-0226, CCAR-P-jrajath94-0227, CCAR-P-jrajath94-0228, CCAR-P-jrajath94-0229, CCAR-P-jrajath94-0230, CCAR-P-jrajath94-0231, CCAR-P-jrajath94-0298, CCAR-P-jrajath94-0305, CCAR-P-jrajath94-0316, CCAR-P-jrajath94-0317, CCAR-P-jrajath94-0318, CCAR-P-jrajath94-0319, CCAR-P-jrajath94-0320, CCAR-P-jrajath94-0321, CCAR-P-jrajath94-0351, CCAR-P-jrajath94-0353, CCAR-P-jrajath94-0354, CCAR-P-jrajath94-0373, CCAR-P-jrajath94-0374, CCAR-P-jrajath94-0375, CCAR-P-jrajath94-0377, CCAR-P-jrajath94-0379, CCAR-P-jrajath94-0380, CCAR-P-jrajath94-0381, CCAR-P-jrajath94-0415, CCAR-P-jrajath94-0416, CCAR-P-jrajath94-0417, CCAR-P-jrajath94-0436, CCAR-P-jrajath94-0437, CCAR-P-jrajath94-0438, CCAR-P-jrajath94-0439, CCAR-P-jrajath94-0441, CCAR-P-jrajath94-0442, CCAR-P-jrajath94-0443, CCAR-P-jrajath94-0444, CCAR-P-jrajath94-0477, CCAR-P-jrajath94-0479, CCAR-P-jrajath94-0480, CCAR-P-jrajath94-0499, CCAR-P-jrajath94-0500, CCAR-P-jrajath94-0501, CCAR-P-jrajath94-0502, CCAR-P-jrajath94-0504, CCAR-P-jrajath94-0505, CCAR-P-jrajath94-0506, CCAR-P-jrajath94-0507, CCAR-P-jrajath94-0540, CCAR-P-jrajath94-0542, CCAR-P-jrajath94-0543, CCAR-P-jrajath94-0562, CCAR-P-jrajath94-0563, CCAR-P-jrajath94-0564, CCAR-P-jrajath94-0565, CCAR-P-jrajath94-0568, CCAR-P-jrajath94-0569, CCAR-P-jrajath94-0570, CCAR-P-jrajath94-0585, CCAR-P-jrajath94-0595, CCAR-P-jrajath94-0617, CCAR-P-jrajath94-0631, CCAR-P-jrajath94-0632, CCAR-P-jrajath94-0671, CCAR-P-jrajath94-0673, CCAR-P-jrajath94-0677, CCAR-P-jrajath94-0680, CCAR-P-jrajath94-0681, CCAR-P-jrajath94-0682, CCAR-P-jrajath94-0684, CCAR-P-jrajath94-0685, CCAR-P-preporato-0021, CCAR-P-preporato-0023, CCAR-P-preporato-0024, Patrick-0013, Patrick-0024, Patrick-0043, Preporato-0026, Preporato-0027, Preporato-0028, Udemy-0039, Udemy-0041, Udemy-0049, Udemy-0050</sub>

## 3. 자주 나오는 오답 함정

| 오답 | 이유 |
|---|---|
| system prompt에 "악성 지시는 무시하라" | probabilistic · enforcement ✗<br>모델은 가끔 따름 |
| "ignore" 등 keyword · 알려진 phrase filter | 쉽게 우회(trivially evaded)<br>정당한 답변까지 차단 |
| 더 큰 모델 · instruction following 좋은 모델 | attack surface 동일 → 보안 통제 ✗ |
| temperature 낮추기 · 높이기<br>더 큰 context window | 보안과 무관 |
| 모델에 "실행 전 확인" 지시 | 모델 자체 확인 = enforcement ✗<br>→ tool 미부여 또는 사람 승인 필요 |
| full · read-write 권한 + "쓰기 회피" 지시 | 통제 ✗ → 행동에 의존 |
| 대상 ID를 모델이 tool argument로 전달해 범위 축소 | 값을 모델이 결정 → 유도 가능<br>→ 검증된 token 필요 |
| 출력 검사(별도 모델, 이름 탐지)만 배치 | 탐지 → authorization 대체 ✗<br>데이터는 이미 모델에 유입 |
| 민감 데이터 자체를 시스템에서 삭제 | 정당한 업무까지 손상 |
| API key 난독화 · Base64 · local storage<br>prompt 안 위치만 이동 | 여전히 노출 또는 즉시 복원 가능 |
| key를 rotate 없이 이동만 | 이미 노출된 key → rotate 필수 |
| TLS · 저장 시 암호화만 있으면 PII 최소화 불필요 | 출력 · injection 경유 유출 차단 ✗ |
| audit용 이름 든 전문 log | 유출 경로 증가 |
| 입력 기호 제거 · 다른 모델 요약으로 sanitize | 자연어 injection 차단 ✗<br>정보만 훼손 |
| "모델 출력은 안전" → 그대로 렌더링 | 출력은 입력 영향 → escape 필요 |
| guardrail 층 하나만<br>(입력 screen만, 사전 red teaming만) | 빠져나간 공격 포착 층 없음 |
| 공격 문자열 검사 · TLS로 안전 판단 | 문자열 = 우회 가능<br>TLS = 콘텐츠에 대해 보장 ✗ |
| "조심하라" system prompt | 모델은 문구만으로 구분 불가 |
| tool 호출 log · 주간 검토를 통제로 제시 | 기록 ≠ 예방<br>파일은 첫날에 유출 |
| tool을 숨기되 호출 가능하게 유지 | 숨김 의존 보안 ✗ |
| 거부 예시 추가 학습 · 거부 문구 강화 | 여전히 모델 행동<br>이미 뚫린 통제의 반복 |
| 더 똑똑한 모델로 tool 위험 해결 | 판단력만 구매<br>해결 = 더 작은 tool 범위 |
| prompt 메모로 쓰기 경로 제한 | 코드에서 제한 ✗ → 경계 ✗ |
| 공격 표면 제거로 업무에 필요한 tool · 기능 삭제 | 업무 기능도 소멸 |
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
| prompt 문구로 한도 · 규제 요건 충족 | 주입이 덮어씀 · 규제 = 문장 ✗ 사람<br>enforcement ✗ |
| 삭제 도구에 rate limit | 속도만 늦춤 → 잘못된 삭제 1회 못 막음 |
| 업무에 필요한 기능 자체를 제거 | 통제 ✗ → 업무 기능만 상실 |
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
| 불필요한 delete · write tool 유지<br>+ 로깅 · dashboard | 가시성일 뿐 → 권한은 활성 상태로 잔존<br>"로깅은 제거가 아님" |
| 역할에 불필요한 위험 tool에<br>확인 대화상자 · 업무 시간 제한만 추가 | 존재해서는 안 되는 권한의 보완 통제<br>시간 제한 = 노출 시간대만 축소<br>필요한 tool이면 승인 gate (1.4) |
| 두 번째 모델로 tool 호출 검토 | 같은 신뢰 불가 입력을 읽음 · 활성 tool 잔존 |
| 25개 tool 전부 제거 | 정당한 기능 상실 = 권한 없음 ≠ 최소 권한 |
| gate된 · 자주 쓰는 `refund` tool 제거 | 민감성은 gate가 처리 → 정당 기능 상실 |
| 사용 중인 tool은 구성 그대로 적정 | 사용 ≠ 범위 보증<br>schema · 반환 데이터도 점검 대상 |
| "나중에 유용할 수도" tool 유지 | 추측에 근거한 tool = 추측성 공격 표면 |
| 무제한 export 유지 + 로깅 | 로그 = 관찰 가능성 · 해결책 ✗ |
| 서드파티 server 문제를 프로토콜 · key 삭제로 해결 | 결함 = 신뢰 불가 콘텐츠<br>주입 경로 미해결 |
| 벤더 SOC 2 · 훌륭한 description 신뢰 | 벤더 통제 설명 ≠ 결제 권한의 안전성 |
| 사용자 입력 · 선택 · 편집 값을 filter 기준으로 사용 | 사용자 주장 ≠ authorization<br>값 하나 변경 → 타 tenant 데이터 열람 |
| 답변 후 filter | 이미 읽은 뒤 → 유출 발생 |
| login 확인만으로 접근 허용 | authentication ≠ authorization |
| 권한 규칙을 system prompt · 모델 판단에 위임 | 모델 = 신원 · 정책 · 잠금장치 ✗ |
| 실행 후 audit log로 권한 확인 | 이미 변경됨 → 보완책일 뿐 단독 통제 ✗ |
| prompt에 직원 이름 기재 · 앱 로그에 이름 기록 | prompt ≠ identity<br>대상 시스템은 credential 하나만 인식 |
| 부서별 credential<br>(사람 단위 귀속이 필요할 때) | 부서 ≠ 사람 → 감사에서 사람 특정 ✗<br>부서 단위 귀속만 필요하면 충분 |
| 공유 OAuth token 하나로 전 사용자 호출 | server가 호출 사용자 식별 ✗ |
| TLS를 token 신뢰 근거로 사용 | TLS = 전송 중 보호<br>audience 바인딩 = 사용처 증명 (다른 위협) |
| token 주간 교체 + 검토 모델 | 교체 ≠ 바인딩<br>검토 모델도 같은 신뢰 불가 입력을 읽음 |
| token을 system prompt에 보관 · 환불 승인 캐시 | secret은 prompt 밖<br>캐시된 승인 = 승인자가 내린 적 없는 승인 |
| "접근이 필요하니" master key 부여 | ambient authority → 전원 주문 노출 |
| 개인 credential 하드코딩 "동작하니 문제없음" | 귀속 · rotation 붕괴<br>개발자 퇴사 시 credential 이탈 |

<sub>근거: Amey-0008, Amey-0033, Amey-0034, Amey-0042, Amey-0047, Amey-0064, Amey-0079, CCAR-P-Amey-Thakur-0001, CCAR-P-Amey-Thakur-0008, CCAR-P-Amey-Thakur-0024, CCAR-P-Amey-Thakur-0025, CCAR-P-Amey-Thakur-0026, CCAR-P-Amey-Thakur-0041, CCAR-P-Amey-Thakur-0044, CCAR-P-Amey-Thakur-0059, CCAR-P-Amey-Thakur-0060, CCAR-P-Amey-Thakur-0071, CCAR-P-jrajath94-0008, CCAR-P-jrajath94-0033, CCAR-P-jrajath94-0034, CCAR-P-jrajath94-0036, CCAR-P-jrajath94-0037, CCAR-P-jrajath94-0038, CCAR-P-jrajath94-0039, CCAR-P-jrajath94-0040, CCAR-P-jrajath94-0041, CCAR-P-jrajath94-0042, CCAR-P-jrajath94-0079, CCAR-P-jrajath94-0091, CCAR-P-jrajath94-0092, CCAR-P-jrajath94-0093, CCAR-P-jrajath94-0094, CCAR-P-jrajath94-0095, CCAR-P-jrajath94-0096, CCAR-P-jrajath94-0157, CCAR-P-jrajath94-0159, CCAR-P-jrajath94-0160, CCAR-P-jrajath94-0161, CCAR-P-jrajath94-0207, CCAR-P-jrajath94-0208, CCAR-P-jrajath94-0209, CCAR-P-jrajath94-0210, CCAR-P-jrajath94-0211, CCAR-P-jrajath94-0212, CCAR-P-jrajath94-0213, CCAR-P-jrajath94-0214, CCAR-P-jrajath94-0215, CCAR-P-jrajath94-0220, CCAR-P-jrajath94-0222, CCAR-P-jrajath94-0223, CCAR-P-jrajath94-0224, CCAR-P-jrajath94-0225, CCAR-P-jrajath94-0226, CCAR-P-jrajath94-0227, CCAR-P-jrajath94-0228, CCAR-P-jrajath94-0230, CCAR-P-jrajath94-0231, CCAR-P-jrajath94-0298, CCAR-P-jrajath94-0305, CCAR-P-jrajath94-0316, CCAR-P-jrajath94-0317, CCAR-P-jrajath94-0318, CCAR-P-jrajath94-0319, CCAR-P-jrajath94-0320, CCAR-P-jrajath94-0321, CCAR-P-jrajath94-0351, CCAR-P-jrajath94-0353, CCAR-P-jrajath94-0354, CCAR-P-jrajath94-0374, CCAR-P-jrajath94-0379, CCAR-P-jrajath94-0380, CCAR-P-jrajath94-0415, CCAR-P-jrajath94-0416, CCAR-P-jrajath94-0417, CCAR-P-jrajath94-0437, CCAR-P-jrajath94-0438, CCAR-P-jrajath94-0439, CCAR-P-jrajath94-0442, CCAR-P-jrajath94-0443, CCAR-P-jrajath94-0477, CCAR-P-jrajath94-0479, CCAR-P-jrajath94-0480, CCAR-P-jrajath94-0499, CCAR-P-jrajath94-0500, CCAR-P-jrajath94-0501, CCAR-P-jrajath94-0502, CCAR-P-jrajath94-0505, CCAR-P-jrajath94-0506, CCAR-P-jrajath94-0540, CCAR-P-jrajath94-0542, CCAR-P-jrajath94-0543, CCAR-P-jrajath94-0562, CCAR-P-jrajath94-0565, CCAR-P-jrajath94-0568, CCAR-P-jrajath94-0569, CCAR-P-jrajath94-0585, CCAR-P-jrajath94-0595, CCAR-P-jrajath94-0617, CCAR-P-jrajath94-0631, CCAR-P-jrajath94-0632, CCAR-P-jrajath94-0673, CCAR-P-jrajath94-0677, CCAR-P-jrajath94-0680, CCAR-P-jrajath94-0681, CCAR-P-jrajath94-0682, CCAR-P-jrajath94-0684, CCAR-P-jrajath94-0685, CCAR-P-preporato-0023, CCAR-P-preporato-0024, Patrick-0013, Patrick-0024, Patrick-0043, Preporato-0026, Preporato-0027, Preporato-0028, Udemy-0039, Udemy-0041, Udemy-0049, Udemy-0050</sub>

## 4. 암기 목록

| 이름 | 의미 |
|---|---|
| Untrusted input | 웹 페이지 · fetch 문서 · 사용자 입력 · 모델 출력<br>→ 지시 ✗, 데이터로 취급 |
| Least privilege | 필요한 tool · operation만, 범위 축소 부여<br>→ 피해 범위 제한 |
| Human approval gate | consequential · irreversible<br>· destructive 행동 앞 사람 확인 |
| Deterministic gate | 위험 행동(외부 전송 등)을 코드로 차단 · 보류 |
| Hooks · tool configuration | 금지 capability를 prompt 아닌 설정으로 강제하는 수단 |
| Authorization 전파 | 호출 사용자의 identity · 권한(검증된 token)으로 tool 실행<br>사용자별 audit |
| Secret 보관 | env var · secret manager<br>노출 시 rotate<br>tool 코드가 인증 |
| Data minimization | 필요한 항목만 전달<br>직접 식별자 masking · tokenization |
| XML tag 분리 | 사용자 입력을 `<user_query>` 등으로 감싸고 "데이터" 선언 |
| Output escaping | 렌더링 전 escape · sanitize |
| Harmlessness screen | 경량 모델로 입력을 사전 심사하는 guardrail 층 |
| Defense in depth | 입력 screen · system prompt ·<br>출력 filter · monitoring 중첩 |
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
| Adverse-impact ratio | 집단별 통과율 비교 비율 증거 (규제 기관 요구) |
| AI 고지 · 주장별 인용 · 이의 신청 | 투명성 3요소 |
| Trace | 결정 입력 · 담당자 · 버전 기록<br>설명 · 고지 · replay의 근거 |
| Activity Feed | 누가 무엇을 읽었는지 기록<br>Anthropic 키 아래 → 키 폐기 후 유지 |
| CMEK | 자체 암호화 키<br>적용 후 기록된 데이터만 보호 |
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
| Ambient authority | master key처럼 호출자와 무관하게 쥔 광범위 권한<br>→ confused deputy 위험 |
| Confused deputy | agent가 강한 권한으로 타인 데이터 접근<br>→ 사용자별 위임 token으로 대체 |
| Per-user delegation | agent가 요청 사용자 ID로 동작<br>대상 시스템이 권한 강제 · 기록 |
| `authorization_token` | 원격 MCP server별 사용자 OAuth token 전달 필드 |
| Audience 바인딩 | token을 수신 서비스에 묶음<br>잘못된 서비스에서의 재사용(replay) 차단 |
| 주장(claim) | 사용자가 입력 · 선택 · 편집한 값<br>authorization 근거 ✗ |
| Authentication vs authorization | 신원 증명 ≠ 해당 데이터에 접근할 권리 |
| 서비스 ID | 범위 제한 접근을 가진 서비스용 신원<br>개인 credential 대체 |
| Tool description injection | 서드파티 MCP description · schema 속 지시<br>→ 모델 입력 경로 |

<sub>근거: Amey-0033, Amey-0034, Amey-0042, Amey-0079, CCAR-P-Amey-Thakur-0008, CCAR-P-Amey-Thakur-0026, CCAR-P-Amey-Thakur-0041, CCAR-P-Amey-Thakur-0044, CCAR-P-Amey-Thakur-0060, CCAR-P-jrajath94-0008, CCAR-P-jrajath94-0033, CCAR-P-jrajath94-0036, CCAR-P-jrajath94-0037, CCAR-P-jrajath94-0038, CCAR-P-jrajath94-0039, CCAR-P-jrajath94-0040, CCAR-P-jrajath94-0041, CCAR-P-jrajath94-0042, CCAR-P-jrajath94-0091, CCAR-P-jrajath94-0092, CCAR-P-jrajath94-0095, CCAR-P-jrajath94-0160, CCAR-P-jrajath94-0161, CCAR-P-jrajath94-0208, CCAR-P-jrajath94-0209, CCAR-P-jrajath94-0210, CCAR-P-jrajath94-0212, CCAR-P-jrajath94-0213, CCAR-P-jrajath94-0214, CCAR-P-jrajath94-0215, CCAR-P-jrajath94-0220, CCAR-P-jrajath94-0224, CCAR-P-jrajath94-0229, CCAR-P-jrajath94-0231, CCAR-P-jrajath94-0298, CCAR-P-jrajath94-0305, CCAR-P-jrajath94-0316, CCAR-P-jrajath94-0319, CCAR-P-jrajath94-0353, CCAR-P-jrajath94-0375, CCAR-P-jrajath94-0376, CCAR-P-jrajath94-0416, CCAR-P-jrajath94-0437, CCAR-P-jrajath94-0438, CCAR-P-jrajath94-0439, CCAR-P-jrajath94-0479, CCAR-P-jrajath94-0480, CCAR-P-jrajath94-0501, CCAR-P-jrajath94-0502, CCAR-P-jrajath94-0542, CCAR-P-jrajath94-0543, CCAR-P-jrajath94-0565, CCAR-P-jrajath94-0568, CCAR-P-jrajath94-0569, CCAR-P-jrajath94-0595, CCAR-P-jrajath94-0631, CCAR-P-jrajath94-0632, CCAR-P-jrajath94-0677, CCAR-P-jrajath94-0680, CCAR-P-jrajath94-0681, CCAR-P-jrajath94-0682, CCAR-P-jrajath94-0684, CCAR-P-jrajath94-0685, Patrick-0024, Patrick-0043, Preporato-0026, Preporato-0027, Preporato-0028, Udemy-0039, Udemy-0041, Udemy-0049, Udemy-0050</sub>

## 5. 시험 직전 체크리스트

- [ ] 외부 content(웹 · 문서 · 사용자 입력) = 항상 untrusted
- [ ] injection 방어 = 데이터/지시 분리 + least privilege + 모델 바깥 enforcement
- [ ] "무시하라" system prompt 단독 ✗
- [ ] keyword filter · 더 큰 모델 → 보안 통제 ✗
- [ ] temperature · context window → 보안 통제 ✗
- [ ] "절대 안 됨" → tool 미부여 (hooks · configuration)
- [ ] consequential · destructive tool → approval gate 뒤
- [ ] tool 실행 = 호출 사용자 권한(검증된 token)
- [ ] 공유 service account · 모델이 넘기는 ID argument ✗
- [ ] 노출 key → rotate + backend · secret manager
- [ ] API key를 모델 context에 넣기 ✗
- [ ] PII → 최소화 + masking
- [ ] 암호화 → 최소화 대체 ✗
- [ ] 사용자 입력 → XML tag로 감싸고 "데이터" 선언
- [ ] 모델 출력 → 렌더링 전 escape · sanitize
- [ ] guardrail 다층: 입력 screen + system prompt + 출력 filter + monitoring
- [ ] 읽는 콘텐츠도 지시 채널 → 읽기 전 screening + 돈 tool 앞 코드 gate
- [ ] "구조적으로 불가능" → 최소 권한 credential · sandbox (prompt ✗)
- [ ] 성공한 공격 탐지 = 출력 측 classifier + canary token
- [ ] 모델 안전장치 변동 → 코드 출력 screening + 버전 고정 + 회귀 검사
- [ ] 비가역 · 규제 대상 행동 → pre-action 승인 + 실제 컨텍스트
- [ ] 중단 시 보안 제어 → fail-closed
- [ ] 비용 상한 → 측정된 필요치 위 + 상한 전 알림
- [ ] 합산 지표 ✗ → 그룹별 측정 + 하한선 + 상류 수정
- [ ] 투명성 = AI 고지 + 주장별 인용 + 이의 신청
- [ ] 감사 증거 = 실행 기록(log) · trace, 정책 문구 ✗
- [ ] 규제 데이터 = 경계에서 제거 · tokenization, 로그 = redact + 짧은 보존
- [ ] BAA 범위 = Anthropic 처리만, 서드파티 connector = 별도 BAA
- [ ] ZDR = 조직별 · Console 제외, residency = default + allowed geo
- [ ] 컴플라이언스 = 요구사항 → 통제 → 담당자 → 증거 → 주기
- [ ] 사용자가 입력 · 선택 · 편집한 값 = 주장 → 인증된 신원 + 코드 검사
- [ ] 권한 검사 = tool 실행 전 코드 (prompt · 사후 log ✗)
- [ ] 귀속 필요 → 공유 credential ✗, 귀속 단위(사람 · 팀)별 credential · 위임 token
- [ ] 불필요한 tool · 과대 반환 필드 = 제거 · 축소 (로깅 ≠ 제거)

<sub>근거: CCAR-P-Amey-Thakur-0001, CCAR-P-Amey-Thakur-0008, CCAR-P-jrajath94-0033, CCAR-P-jrajath94-0042, CCAR-P-jrajath94-0093, CCAR-P-jrajath94-0094, CCAR-P-jrajath94-0096, CCAR-P-jrajath94-0159, CCAR-P-jrajath94-0160, CCAR-P-jrajath94-0208, CCAR-P-jrajath94-0209, CCAR-P-jrajath94-0211, CCAR-P-jrajath94-0213, CCAR-P-jrajath94-0220, CCAR-P-jrajath94-0223, CCAR-P-jrajath94-0224, CCAR-P-jrajath94-0227, CCAR-P-jrajath94-0229, CCAR-P-jrajath94-0305, CCAR-P-jrajath94-0316, CCAR-P-jrajath94-0351, CCAR-P-jrajath94-0353, CCAR-P-jrajath94-0375, CCAR-P-jrajath94-0416, CCAR-P-jrajath94-0417, CCAR-P-jrajath94-0437, CCAR-P-jrajath94-0479, CCAR-P-jrajath94-0542, CCAR-P-jrajath94-0595, CCAR-P-jrajath94-0680, CCAR-P-jrajath94-0681</sub>
