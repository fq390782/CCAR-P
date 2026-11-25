@@ ADD-TO: ### 1.3 Least privilege와 tool 설계

**구성 감사: 불필요한 tool · 과대 반환 데이터**

| 상황 | 조치 |
|---|---|
| 역할은 읽기 · 초안 작성뿐<br>agent는 update · delete 가능 | update · delete 기능을 구성에서 제거<br>→ 공격 · 오류 표면 자체 소멸 |
| 프로덕션 레코드 읽기 · 수정 agent | 읽기 · 쓰기 권한 분리<br>쓰기 = 역할상 필요한 곳에만 부여 |
| 6개월 미사용 `drop_table`<br>어떤 작업도 안 쓰는 delete · write · wire tool | 제거 → 미사용 파괴적 tool = 순수 위험<br>제거 전 숨은 호출자 · 6개월 trace 확인 |
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

<sub>근거: CCAR-P-Amey-Thakur-0001, CCAR-P-Amey-Thakur-0050, CCAR-P-jrajath94-0157, CCAR-P-jrajath94-0159, CCAR-P-jrajath94-0351, CCAR-P-jrajath94-0415, CCAR-P-jrajath94-0477, CCAR-P-jrajath94-0540</sub>

@@ ADD-TO: ### 1.4 Human-in-the-loop (approval gate)

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

<sub>근거: CCAR-P-Amey-Thakur-0050, CCAR-P-jrajath94-0354</sub>

@@ ADD-TO: ### 1.5 Authorization 전파

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

<sub>근거: CCAR-P-jrajath94-0160, CCAR-P-jrajath94-0161, CCAR-P-jrajath94-0298, CCAR-P-jrajath94-0305, CCAR-P-jrajath94-0353, CCAR-P-jrajath94-0416, CCAR-P-jrajath94-0417, CCAR-P-jrajath94-0479, CCAR-P-jrajath94-0480, CCAR-P-jrajath94-0542, CCAR-P-jrajath94-0632</sub>

@@ ADD-TO: ### 1.6 API key / secret 관리

**설정 파일 속 개인 credential**

| 상황 | 조치 |
|---|---|
| 개발자 개인 credential을<br>공유 설정에 하드코딩<br>→ 내부 tool이 DB 호출 | 귀속 ✗ · rotation ✗<br>개발자 퇴사 시 credential도 이탈<br>→ 범위 제한 접근의 서비스 ID로 교체 |

<sub>근거: CCAR-P-jrajath94-0543</sub>

@@ NEW-SECTION
### 서드파티 MCP server 신뢰 경계
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

@@ RULES
| 역할은 읽기 · 초안뿐인데 update · delete 가능 | 해당 기능을 구성에서 제거<br>(로깅 · 확인창 · 시간 제한 ✗) |
| 프로덕션 읽기 · 수정 agent | 읽기 · 쓰기 권한 분리<br>쓰기는 필요한 역할에만 + 명시적 승인 뒤 |
| 미사용 destructive tool<br>(`drop_table` · `delete_*`<br>· `wire_transfer`) | 제거 (숨은 호출자 확인 후)<br>"나중에 유용" 근거 유지 ✗ |
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
<sub>근거: CCAR-P-Amey-Thakur-0001, CCAR-P-Amey-Thakur-0050, CCAR-P-jrajath94-0008, CCAR-P-jrajath94-0079, CCAR-P-jrajath94-0157, CCAR-P-jrajath94-0159, CCAR-P-jrajath94-0160, CCAR-P-jrajath94-0161, CCAR-P-jrajath94-0298, CCAR-P-jrajath94-0305, CCAR-P-jrajath94-0351, CCAR-P-jrajath94-0353, CCAR-P-jrajath94-0354, CCAR-P-jrajath94-0415, CCAR-P-jrajath94-0416, CCAR-P-jrajath94-0417, CCAR-P-jrajath94-0477, CCAR-P-jrajath94-0479, CCAR-P-jrajath94-0480, CCAR-P-jrajath94-0540, CCAR-P-jrajath94-0542, CCAR-P-jrajath94-0543, CCAR-P-jrajath94-0632</sub>

@@ TRAPS
| 불필요한 delete · write tool 유지<br>+ 로깅 · dashboard | 가시성일 뿐 → 권한은 활성 상태로 잔존<br>"로깅은 제거가 아님" |
| 위험 tool 앞 확인 대화상자 · 업무 시간 제한만 추가 | 존재해서는 안 되는 권한의 보완 통제<br>시간 제한 = 노출 시간대만 축소 |
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
| 부서별 credential | 부서 ≠ 사람 → 감사에서 사람 특정 ✗ |
| 공유 OAuth token 하나로 전 사용자 호출 | server가 호출 사용자 식별 ✗ |
| TLS를 token 신뢰 근거로 사용 | TLS = 전송 중 보호<br>audience 바인딩 = 사용처 증명 (다른 위협) |
| token 주간 교체 + 검토 모델 | 교체 ≠ 바인딩<br>검토 모델도 같은 신뢰 불가 입력을 읽음 |
| token을 system prompt에 보관 · 환불 승인 캐시 | secret은 prompt 밖<br>캐시된 승인 = 승인자가 내린 적 없는 승인 |
| "접근이 필요하니" master key 부여 | ambient authority → 전원 주문 노출 |
| 개인 credential 하드코딩 "동작하니 문제없음" | 귀속 · rotation 붕괴<br>개발자 퇴사 시 credential 이탈 |
<sub>근거: CCAR-P-Amey-Thakur-0001, CCAR-P-jrajath94-0008, CCAR-P-jrajath94-0079, CCAR-P-jrajath94-0157, CCAR-P-jrajath94-0159, CCAR-P-jrajath94-0160, CCAR-P-jrajath94-0161, CCAR-P-jrajath94-0298, CCAR-P-jrajath94-0305, CCAR-P-jrajath94-0351, CCAR-P-jrajath94-0353, CCAR-P-jrajath94-0354, CCAR-P-jrajath94-0415, CCAR-P-jrajath94-0416, CCAR-P-jrajath94-0417, CCAR-P-jrajath94-0477, CCAR-P-jrajath94-0479, CCAR-P-jrajath94-0480, CCAR-P-jrajath94-0540, CCAR-P-jrajath94-0542, CCAR-P-jrajath94-0543, CCAR-P-jrajath94-0632</sub>

@@ MEMO
| Ambient authority | master key처럼 호출자와 무관하게 쥔 광범위 권한<br>→ confused deputy 위험 |
| Confused deputy | agent가 강한 권한으로 타인 데이터 접근<br>→ 사용자별 위임 token으로 대체 |
| Per-user delegation | agent가 요청 사용자 ID로 동작<br>대상 시스템이 권한 강제 · 기록 |
| `authorization_token` | 원격 MCP server별 사용자 OAuth token 전달 필드 |
| Audience 바인딩 | token을 수신 서비스에 묶음<br>잘못된 서비스에서의 재사용(replay) 차단 |
| 주장(claim) | 사용자가 입력 · 선택 · 편집한 값<br>authorization 근거 ✗ |
| Authentication vs authorization | 신원 증명 ≠ 해당 데이터에 접근할 권리 |
| 서비스 ID | 범위 제한 접근을 가진 서비스용 신원<br>개인 credential 대체 |
| Tool description injection | 서드파티 MCP description · schema 속 지시<br>→ 모델 입력 경로 |
<sub>근거: CCAR-P-jrajath94-0008, CCAR-P-jrajath94-0160, CCAR-P-jrajath94-0161, CCAR-P-jrajath94-0298, CCAR-P-jrajath94-0305, CCAR-P-jrajath94-0353, CCAR-P-jrajath94-0479, CCAR-P-jrajath94-0480, CCAR-P-jrajath94-0543, CCAR-P-jrajath94-0632</sub>

@@ CHECK
- [ ] 사용자가 입력 · 선택 · 편집한 값 = 주장 → 인증된 신원 + 코드 검사
- [ ] 권한 검사 = tool 실행 전 코드 (prompt · 사후 log ✗)
- [ ] 귀속 필요 → 공유 credential ✗, 사용자별 위임 token
- [ ] 불필요한 tool · 과대 반환 필드 = 제거 · 축소 (로깅 ≠ 제거)
<sub>근거: CCAR-P-Amey-Thakur-0001, CCAR-P-jrajath94-0159, CCAR-P-jrajath94-0160, CCAR-P-jrajath94-0305, CCAR-P-jrajath94-0351, CCAR-P-jrajath94-0353, CCAR-P-jrajath94-0417, CCAR-P-jrajath94-0479, CCAR-P-jrajath94-0542</sub>
