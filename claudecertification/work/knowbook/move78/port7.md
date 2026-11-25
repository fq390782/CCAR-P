@@ ADD-TO: ### 1.5 Authorization 전파
| 구분 | 내용 |
|---|---|
| 귀속 불필요한<br>read-only 내부 대시보드 | 공유 credential 허용<br>(귀속이 중요할 때만 공유 ✗) |
| 공유 credential | 로그에 공유 ID 하나로 합쳐짐<br>→ 지시자 특정 ✗ |
| 공유 credential + 앱 로그에 이름 | ERP는 여전히 단일 ID만 인가<br>두 로그가 서로 어긋날 수 있음 |
| `anthropic-workspace-id` 헤더 | 팀 workspace 지정<br>직원 식별 ✗ |
| token 주기 교체 | 수명 위협 대응<br>audience 바인딩 대체 ✗ |
| 시스템 프롬프트 속 사용자 role 주장 | authorization 근거 ✗ |
| 원본 시스템 ACL | 유지 |
![사용자 입력 claim과 코드 인가 검사의 흐름](svg/8-claim-vs-enforced.svg)
*그림: 사용자 입력은 claim일 뿐이며, 인가는 인증된 신원을 대상 명단과 코드에서 읽기 전에 대조해 강제합니다.*
<sub>근거: CCAR-P-jrajath94-0160, CCAR-P-jrajath94-0161, CCAR-P-jrajath94-0298, CCAR-P-jrajath94-0417, CCAR-P-jrajath94-0632</sub>

@@ ADD-TO: ### 1.28 서드파티 MCP server 신뢰 경계
| 구분 | 내용 |
|---|---|
| 원격 설정 파일에서 description 로드<br>(서버 작성자가 호스팅) | 조용한 업데이트로 내용 변조 가능<br>→ 버전 고정으로 차단 |
<sub>근거: CCAR-P-jrajath94-0008</sub>

@@ RULES
| 귀속 불필요한 read-only 내부 대시보드 | 공유 credential 허용 |
<sub>근거: CCAR-P-jrajath94-0417</sub>

@@ TRAPS
| 더 큰 모델로 tenant filter · 인가 해결 | 신뢰 경계를 성능 문제로 취급<br>모델은 누가 권한을 가졌는지 모름 |
| `anthropic-workspace-id` 헤더로 직원 귀속 | 팀 workspace 지정 · 직원 식별 ✗ |
<sub>근거: CCAR-P-jrajath94-0298, CCAR-P-jrajath94-0305, CCAR-P-jrajath94-0632</sub>

@@ MEMO
| System of record | 기록 · 권한 기준 시스템 (예: ERP)<br>귀속 기준 = 이 시스템의 로그 |
<sub>근거: CCAR-P-jrajath94-0160</sub>
