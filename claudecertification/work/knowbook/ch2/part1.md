@@ ADD-TO: ### 1.1 Messages API 기본 구조

| 구분 | 내용 |
|---|---|
| 후속 답변이 이전 턴 무시 | 원인 = 앱이 각 메시지를 개별 전송<br>해결 = 앱이 대화 기록 저장 + 요청마다 전체 전송 |
| 모델 | 그대로 유지 가능<br>이력 전송만으로 이전 턴 활용 |

| 오답 | 이유 |
|---|---|
| API가 이전 턴을 보관한다고 가정 | 호출 사이에 턴 보관 ✗ |
| 더 큰 모델 티어가 턴을 기억 | 서버 측 메모리 ✗ · 모델 크기 무관 |
| 턴 저장 후 최신 메시지만 전송 | 이전 턴이 요청에 없으면 활용 ✗ |

<sub>근거: CCAR-P-jrajath94-0599</sub>

@@ ADD-TO: ### 1.3 Streaming

| 상황 | 내용 |
|---|---|
| 응답에 최대 15분 · 사용자가 도착하는 대로 읽음 | streaming(SSE)<br>→ 완료 전 텍스트 읽기 가능 |
| 첫 단어를 전체 답변 완료 전에 표시 | streaming<br>모델 · 답변 품질 그대로 |
| Batch로 대체 | 처리 후에야 결과 반환<br>→ 도착하는 대로 읽기 ✗ |
| 클라이언트 타임아웃을 24시간으로 연장 | 일부 네트워크는 타임아웃과 무관하게 유휴 연결 종료<br>→ 긴 호출 해결책 ✗ |

| 스트림 오류 처리 | 내용 |
|---|---|
| `error` 이벤트 | HTTP 200 이후에도 도착 가능<br>→ 200 = 스트림 완료 ✗ |
| 처리 루프 | content 이벤트와 같은 루프에서 `error`도 처리 |
| 부분 텍스트 | 최종 메시지 도착 전까지 잠정(초안)<br>최종 답변으로 확정 ✗ |
| 끊어진 스트림 이어가기 | 요청 `resume` 플래그 ✗<br>문서 = 최신 모델의 continuation 메시지 |

<sub>근거: CCAR-P-jrajath94-0591, CCAR-P-jrajath94-0592, CCAR-P-jrajath94-0635</sub>

@@ ADD-TO: ### 1.5 Message Batches API

| 상황 | 정답 |
|---|---|
| 매일 밤 대량 분류 · 마감 = "특정 시각까지" | Batch API<br>(약 50% 저렴 · 최대 24시간 처리) |
| 결과를 마감 전에 아무도 안 읽음 | 상호작용성 가치 없음<br>→ 실시간 가격 지불 낭비 |
| 지연 요구의 유일한 조건 | 마감 시각 하나 |

| 오답 | 이유 |
|---|---|
| 실시간 streaming 유지 ("가장 빠름") | 빠름이 얻는 것 없음 |
| 입력 일부만 샘플링 | 나머지가 조용히 누락<br>작업을 줄여 비용 절감 |
| 스트리밍 API 키 2개로 분할 | 처리량만 2배 · 불필요<br>실시간 가격 그대로 |

<sub>근거: CCAR-P-jrajath94-0081</sub>

@@ ADD-TO: ### 1.10 오류 처리 · retry · rate limit

| 구분 | 내용 |
|---|---|
| 429 + `retry-after: 30` · 요청 유효 | 30초 대기 → 같은 요청 재전송<br>요청 수정 불필요 |
| 대기 · 재전송 주체 | 앱<br>프롬프트로 모델에게 요청 ✗ |

| 오답 | 이유 |
|---|---|
| 지연 없이 루프에서 즉시 재전송 | 서버가 알려 준 대기 시간 무시 |
| 프롬프트에 "30초 후 재전송" 지시 | 재전송 주체 = 앱 · 모델 ✗ |
| 재시도마다 새 큐 서비스로 이동 | 대기 시간 준수를 직접 충족 ✗ |

<sub>근거: CCAR-P-jrajath94-0590</sub>

@@ ADD-TO: ### 1.11 동시성 · 비동기 통합 패턴

| 상황 | 정답 |
|---|---|
| 레거시 = 2초 타임아웃 동기 endpoint · 작업 = 긴 추론 | 요청 수락 → 식별자 즉시 반환<br>→ 결과는 비동기 전달 (제출 · 전달 분리) |
| webhook 전달 보장 | 한 번 이상 전달(중복 가능) |
| 멱등성 강제 위치 | 효과를 수행하는 서비스<br>(예: 청구하는 결제 서비스) |
| 멱등 키 | 트리거 이벤트 ID<br>청구 전 키 확인 |
| 보장 범위 | 재시작 · 재시도 · 중복 전달에도 정확히 1회 |

| 오답 | 이유 |
|---|---|
| 모델이 2초 안에 답하도록 강제<br>· 가장 작은 모델 사용 | 추론을 잘라 작업 희생 |
| 레거시 타임아웃 증가 | 레거시 변경은 대개 선택지 아님<br>= 제약 자체 |
| agent 대화 메모리에서 중복 제거 | 세션별 · 일시적<br>재시작 · 두 번째 인스턴스가 잊음 |
| webhook 수신기 인메모리 캐시 | 프로세스와 함께 소실<br>멱등성 핵심 = 내구성 |
| 청구 전 고객에게 확인 | UX 나쁨 · 경쟁 상태(racy) |

<sub>근거: CCAR-P-Amey-Thakur-0014, CCAR-P-jrajath94-0084</sub>

@@ ADD-TO: ### 1.13 SDK · 플랫폼 client

| 구분 | 내용 |
|---|---|
| Claude Platform on AWS model ID | first-party ID 그대로 (예: `claude-haiku-5-5`)<br>`anthropic.` 접두사 · Bedrock 스타일 ID ✗ |
| outbound web identity federation | 기본 비활성<br>→ 활성화 전까지 요청 실패 |
| 호출자별 IAM 제어 | SigV4 서명<br>+ IAM 정책을 워크스페이스 ARN으로 범위 지정 |
| OAuth · 동의 화면 | Claude Platform on AWS 미지원 |

| 오답 | 이유 |
|---|---|
| 호출자가 공유하는 1개 역할로 SigV4 | 호출자별 제어 요구 불충족 |
| IAM 생략 + 코드에 장기 API 키 | IAM 제어 요구 불충족 |
| 사용자별 OAuth 동의 화면 추가 | 플랫폼이 OAuth 미지원 |

| 주의 | 내용 |
|---|---|
| ⚠️ model ID 표기 | 모델 버전 · 플랫폼별 ID는 시점에 따라 변동<br>출제 시점 공식 문서로 재확인 |

<sub>근거: CCAR-P-jrajath94-0588, CCAR-P-jrajath94-0633</sub>

@@ NEW-SECTION
### 배포 플랫폼 선택 · 데이터 거주
**요구사항이 배포 경로를 결정 · 계약과 설정으론 대체 ✗**

| 상황 | 정답 |
|---|---|
| 요청 데이터가 고객 AWS 계정 밖으로 나가면 안 됨<br>(추론을 고객 AWS 계정 내부에서 실행) | 고객 계정 · 리전의 Amazon Bedrock |
| Google Cloud 표준화 · ID · 과금 · 감사를 기존 통제로 처리 | Vertex AI 경유 배포<br>→ 기존 통제 중복 없이 적용 |
| 데이터 거주 규칙이 다른 두 리전의 사용자 | 데이터가 각 리전 경계 안에 머무는 별도 배포 |
| 솔루션이 두 클라우드에 걸쳐 실행 | 동일해야 할 동작 정의<br>→ 각 플랫폼에서 그 동작 평가 |
| PHI · 리전 고정 · 학습 금지 · 완전 감사 (모두 법적 요구) | 병원 리전의 Bedrock<br>+ PHI 적격 구성 + 서명된 BAA<br>+ 추론 로그를 병원 감사 저장소로 |

| 오답 | 이유 |
|---|---|
| 서명된 데이터 처리 계약 | 데이터가 계정 밖으로 나가는 것은 그대로 |
| 요청 로깅 비활성화 | 계정 경계 충족 ✗ |
| 전송 중 암호화만 충족 | 데이터가 여전히 계정 밖으로 이동 |
| 요구사항이 결정하는 것 = 모델 패밀리 | 모델 패밀리는 별개의 선택 |
| 기능 동등성 위해 다른 클라우드 배포 | 두 번째 통제 평면 생성 |
| Claude API 사용 + 통제 복제 | 비용 큼 · 어긋남 |
| 팀별로 경로 선택 | 거버넌스 소멸 |
| 단일 배포 (싼 리전 · 최저 지연 리전 · 암호화) | 데이터가 경계 너머로 이동<br>지연 시간은 거주 규칙과 무관 |
| 두 곳에서 같은 프롬프트 사용 | 동일 동작 보장 ✗<br>동등성 = 정의 후 검증할 요구사항 |
| 더 저렴한 플랫폼 · 가장 가까운 리전 | 일관성 문제 해결 ✗ |

| 병원 PHI 사례 오답 | 이유 |
|---|---|
| ZDR 켠 직접 API + 앱 수준 감사 로그 | 처리 · 저장을 특정 AWS 리전에 고정 ✗<br>ZDR · BAA는 나머지 두 요구 충족 가능 |
| 기본 구성의 직접 API ("기본적으로 학습 안 함") | 정책상 주장 · 리전 · 계약 통제 ✗<br>→ 거주 · 감사 불충족 |
| 병원 서버에 오픈 웨이트 자체 호스팅 | 보안 강화 · 패치 · 감사 부담 전부 병원<br>모델 품질 하락 · 법적 이득 없음 |

| 주의 | 내용 |
|---|---|
| ⚠️ 직접 API 거주 범위 | 해설: 추론 글로벌 또는 미국 한정 · workspace 저장소 미국 한정<br>지원 범위는 시점에 따라 변동 → 공식 data residency 문서로 재확인 |

<sub>근거: CCAR-P-Amey-Thakur-0011, CCAR-P-Amey-Thakur-0012, CCAR-P-Amey-Thakur-0015, CCAR-P-Amey-Thakur-0051, CCAR-P-Amey-Thakur-0052, CCAR-P-Amey-Thakur-0068, CCAR-P-jrajath94-0010</sub>

@@ NEW-SECTION
### 인증 · 자격 증명 · workspace 격리
**사용자 · 워크로드 단위 최소 권한 · 정적 공유 키 ✗**

| 상황 | 정답 |
|---|---|
| agent가 요청 직원 권한 안에서만 동작<br>· 공유 특권 자격 증명 ✗ | OAuth 2.0 위임 토큰<br>요청마다 요청자 본인 토큰 · 최소 권한 범위 |
| CI가 작업마다 서명 ID 토큰 발급<br>· CI에 정적 API 키 저장 ✗ | CI ID 제공자를 federation issuer로 등록<br>+ 파이프라인용 federation rule 생성 |
| 사용량 조회 + Messages 요청을 한 작업에서 수행 | 사용량(Usage and Cost API) = Admin API 키<br>Messages 요청 = workspace API 키 |
| 테넌트 간 prompt cache · API 키 공유 ✗<br>+ 테넌트별 월 지출 한도 | 테넌트마다 workspace 1개<br>키를 해당 workspace로 범위 지정<br>workspace별 월 지출 한도 설정 |
| 저장소 6개 공유 자격 증명 · 한 사람 구독 의존 ✗ | Claude Console API 키<br>→ 조직 수준 Actions secret 1개 공유 |

| 개념 | 내용 |
|---|---|
| federation 동작 | 워크로드가 서명 ID 토큰을 단기 Anthropic 토큰으로 교환<br>CI에 정적 키 없음 |
| federation rule 역할 | 범위 · 수명 결정 |
| workspace 격리 (Claude API) | prompt cache가 workspace별 격리<br>새 workspace마다 자체 지출 한도 보유 |
| Admin API 키 · workspace API 키 | 키마다 역할 하나<br>workspace 키는 Usage and Cost API 인증 ✗ |
| OAuth 토큰(`setup-token`) | 한 사람의 구독에 묶임 |

| 오답 | 이유 |
|---|---|
| 공유 토큰 주기적 교체 | 피해 범위 불변<br>토큰 1개 유출 시 전원 경비 접근 |
| 직원별 토큰을 전체 관리자 범위로 설정 | 여전히 과도한 권한 |
| 토큰을 agent 설정 파일에 저장 | 새로운 시크릿 난립 |
| 인증 제거 + 사무실 VPN 의존 | VPN = 네트워크 위치만 증명<br>사용자 신원 · 권한 증명 ✗ |
| 만료 30일 workspace API 키를 CI secrets에 | 여전히 CI에 저장된 정적 API 키 |
| workspace 키 1개로 사용량 조회까지 | workspace 키는 Usage and Cost API 인증 ✗ |
| Default Workspace 키를 Admin API 키로 간주 | workspace 키 = Messages 담당 |
| workspace 1개 + 헤더로 테넌트 구분 | prompt cache 1개 · 지출 한도 1개 공유 |
| `setup-token` OAuth 토큰을 조직 secret으로 | 한 사람 구독에 묶임<br>공유하기 쉬워 보여도 ✗ |

<sub>근거: CCAR-P-jrajath94-0004, CCAR-P-jrajath94-0593, CCAR-P-jrajath94-0594, CCAR-P-jrajath94-0634, CCAR-P-jrajath94-0706</sub>

@@ NEW-SECTION
### 통합 아키텍처 · 외부 호출 장애 격리
**단일 통합 지점 · 느슨한 결합 · 장애는 계층 방어**

| 구분 | 내용 |
|---|---|
| 내부 서비스 뒤에 Claude 배치 | 인증 · rate limiting · 로깅 · 모델 라우팅을<br>한 곳에서 일관 적용 · 한 번에 변경 |
| 단일 통합 지점이 안 바꾸는 것 | 토큰 단가 · 평가 필요성<br>추가 hop = 일반적으로 지연 증가 |
| 추상화 없이 단일 클라우드 서비스에 직접 결합 | 결합이 앱 코드까지 확산<br>→ 나중에 옮기는 비용 증가 |
| 결합 위험의 성격 | 아키텍처 관심사 = 결합도가 변경 비용 결정<br>비용 · 정확도 · 지연은 결합 자체의 결과 ✗ |
| 소유자 · 도구 · 정책이 다른 외부 AI agent에게 견적 요청 | agent-to-agent delegation<br>정의된 프로토콜 · 요청/응답 계약 · 인증 · 장애 격리 |

| 외부 API 성능 저하 | 역할 |
|---|---|
| timeout | 대기 시간 제한 |
| bulkhead | 제휴사가 agent 자원을 소모하는 양 제한<br>(동시 호출 제한) |
| circuit breaker | 반복 실패 후 재시도 누적 차단 |
| graceful fallback | 응답성 유지<br>(예: "캐시된 요금을 표시") |

| 오답 | 이유 |
|---|---|
| 더 낮은 토큰 가격 · 평가 불필요 · 지연 보장 | 단일 통합 지점의 이점 아님 |
| retry budget 증가 + exponential backoff | retry storm → 과부하 심화<br>사용자는 여전히 대기 |
| 모든 제휴사 요청을 직렬 큐 처리 | 40초 응답이 사용자의 무한 지연으로 변환 |
| timeout 완전 제거 | 느린 제휴사 1곳이 worker를 무기한 정지 |
| 공급업체 가격표를 프롬프트에 붙여 Claude 직접 호출 | 이미 최신 가격을 가져야만 동작<br>그 가격이 요청 대상 |
| 공급업체 DB에 직접 접근하는 MCP 서버 | 공급업체 agent · 정책 우회<br>얻을 수 없는 접근 권한 가정 |
| 두 회사가 공동 편집하는 system prompt | 두 조직의 통제를 한 프롬프트로 합침 |

<sub>근거: CCAR-P-Amey-Thakur-0013, CCAR-P-Amey-Thakur-0053, CCAR-P-Amey-Thakur-0067, CCAR-P-jrajath94-0083, CCAR-P-preporato-0010</sub>

@@ NEW-SECTION
### 지연 단축 수단 (streaming · fast mode · effort)
**지연 종류마다 수단이 다름 · 첫 단어 = streaming**

| 지연 목표 | 수단 |
|---|---|
| 답변 완료 전 첫 단어 표시 | streaming<br>(모델 · 답변 품질 그대로) |
| 초당 출력 토큰 수 | fast mode |
| 단순 요청의 출력 · thinking 작업량 | effort를 더 낮게 설정 |
| 어려운 요청의 정확도 하한 | medium effort 유지 |
| 출력 길이가 시간을 늘림 | 프롬프트에서 더 짧은 답변 요청 |

| 오답 | 이유 |
|---|---|
| fast mode로 첫 토큰까지 시간 단축 | 속도 향상 = 초당 출력 토큰 수<br>첫 토큰까지의 시간에는 적용 ✗ |
| 답변을 저장소에 캐시 → 완료 후에만 표시 | 첫 단어가 완료 전에 나타나지 않음 |
| 요청을 Message Batch로 전송 → 다음 날 읽기 | 사용자가 첫 단어를 바로 볼 수 없음 |
| 모든 요청을 high effort 큰 모델로 이동 | 호출마다 오래 걸려 지연 목표 이탈 가능 |

| 주의 | 내용 |
|---|---|
| ⚠️ 해설의 "(Inference)" 표기 | "streaming은 총 생성 작업량 감소 ✗"<br>"큰 모델은 지연 목표 이탈 가능"<br>문서 직접 근거가 아닌 추론 표기 |
| ⚠️ fast mode 지원 모델 | 지원 모델 · 배율은 시점에 따라 변동<br>사용 전 공식 fast mode 문서 확인 |

<sub>근거: CCAR-P-jrajath94-0635, CCAR-P-jrajath94-0637</sub>

@@ RULES

| 상황 | 정답 |
|---|---|
| 후속 답변이 이전 턴 무시 · 모델 유지 | 앱이 기록 저장 + 요청마다 전체 전송 |
| 응답 최대 15분 · 도착하는 대로 읽기 | streaming(SSE) · Batch ✗ · 타임아웃 24시간 ✗ |
| 첫 단어를 답변 완료 전에 표시 | streaming · fast mode ✗(첫 토큰 시간 아님) |
| 스트림에 부분 텍스트 뒤 `error` 이벤트 | content · `error` 같은 루프 처리<br>최종 메시지 전까지 잠정 표시 |
| 야간 대량 분류 · 마감 시각만 있음 | Batch API(약 50% 저렴) · 샘플링 ✗ |
| 429 + `retry-after` · 요청 유효 | 그만큼 대기 → 같은 요청 재전송(앱이 수행) |
| 2초 타임아웃 동기 endpoint + 긴 추론 | 수락 → 식별자 즉시 반환 → 결과 비동기 전달 |
| webhook 중복 전달 · 정확히 1회 효과 | 효과 수행 서비스가 이벤트 ID로 멱등 처리 |
| 지연 목표 빠듯 · 단순 요청 다수 | 단순 요청 effort 낮춤 + medium 유지 + 짧은 답변 요청 |
| 고객 AWS 계정 밖 데이터 이동 ✗ | 고객 계정 · 리전의 Bedrock |
| Google Cloud 표준화 · 기존 ID · 과금 · 감사 | Vertex AI 경유 |
| 거주 규칙이 다른 두 리전 | 경계별 별도 배포 |
| 두 클라우드에 걸친 솔루션 | 동일해야 할 동작 정의 → 플랫폼별 평가 |
| PHI · 리전 고정 · 학습 금지 · 감사 | 병원 리전 Bedrock + BAA + 로그 소유 |
| Claude Platform on AWS 호출 | first-party model ID<br>SigV4 · federation 활성화<br>IAM = 워크스페이스 ARN 범위 |
| agent가 요청자 권한으로만 동작 | OAuth 2.0 위임 토큰(요청자 본인 토큰 · 최소 권한) |
| CI에 정적 API 키 저장 ✗ | federation issuer + federation rule |
| 사용량 조회 + Messages 요청 | Admin API 키 + workspace API 키 |
| 테넌트별 캐시 · 키 · 지출 한도 분리 | 테넌트마다 workspace + 키 범위 지정 + 지출 한도 |
| 여러 저장소 공유 자격 증명 · 개인 구독 ✗ | Console API 키 → 조직 수준 Actions secret |
| 모든 호출을 한 곳에서 인증 · 제한 · 로깅 · 라우팅 | 내부 서비스 뒤에 Claude 배치 |
| 외부 API 느림 · agent 응답성 유지 · 과부하 가중 ✗ | timeout · bulkhead<br>circuit breaker · fallback |
| 소유자 · 정책이 다른 외부 AI agent와 협업 | agent-to-agent delegation(계약 · 인증 · 장애 격리) |

<sub>근거: CCAR-P-Amey-Thakur-0011, CCAR-P-Amey-Thakur-0012, CCAR-P-Amey-Thakur-0013, CCAR-P-Amey-Thakur-0014, CCAR-P-Amey-Thakur-0015, CCAR-P-Amey-Thakur-0051, CCAR-P-Amey-Thakur-0052, CCAR-P-Amey-Thakur-0053, CCAR-P-Amey-Thakur-0068, CCAR-P-jrajath94-0004, CCAR-P-jrajath94-0010, CCAR-P-jrajath94-0081, CCAR-P-jrajath94-0083, CCAR-P-jrajath94-0084, CCAR-P-jrajath94-0588, CCAR-P-jrajath94-0590, CCAR-P-jrajath94-0591, CCAR-P-jrajath94-0592, CCAR-P-jrajath94-0593, CCAR-P-jrajath94-0594, CCAR-P-jrajath94-0599, CCAR-P-jrajath94-0633, CCAR-P-jrajath94-0634, CCAR-P-jrajath94-0635, CCAR-P-jrajath94-0637, CCAR-P-jrajath94-0706, CCAR-P-preporato-0010</sub>

@@ TRAPS

| 오답 | 이유 |
|---|---|
| 서명된 계약 · 로깅 비활성화 · 전송 중 암호화로 계정 경계 요구 충족 | 데이터가 여전히 계정 밖으로 이동 |
| 단일 배포로 두 리전 거주 규칙 충족 | 데이터가 경계 너머로 이동 |
| 같은 프롬프트 = 두 플랫폼 동일 동작 | 동등성은 정의 후 검증 |
| 직접 API + ZDR로 리전 거주 충족 | 특정 AWS 리전 고정 ✗ |
| "기본적으로 학습 안 함" = 법적 통제 | 정책상 주장 · 계약 통제 아님 |
| 오픈 웨이트 자체 호스팅이 법적으로 유리 | 컴플라이언스 부담 전부 자사 · 이득 없음 |
| API가 이전 턴을 보관 · 큰 모델 티어가 기억 | Messages API stateless |
| 클라이언트 타임아웃 24시간 연장 | 일부 네트워크가 유휴 연결 종료 |
| HTTP 200 = 스트림 정상 완료 | `error` 이벤트가 200 이후에도 도착 |
| 요청 `resume` 플래그로 스트림 재개 | continuation 메시지 방식 |
| fast mode가 첫 토큰 시간 단축 | OTPS만 향상 |
| 모든 요청 high effort 큰 모델 | 호출 지연 증가로 목표 이탈 가능 |
| 야간 작업에 실시간 API 유지 · 샘플링 · 키 분할 | 실시간 가격 낭비 · 90% 누락 · 처리량 불필요 |
| 429 후 즉시 재전송 · 프롬프트로 모델이 대기 | 재전송 주체 = 앱 · 서버 대기 시간 준수 |
| 레거시 타임아웃 증가 · 추론 잘라 2초 충족 | 제약 자체 · 작업 희생 |
| 중복 제거를 agent 메모리 · 인메모리 캐시에서 | 일시적 · 재시작에 소실 → 멱등성 내구성 필요 |
| 청구 전 고객 확인으로 중복 방지 | UX 나쁨 · 경쟁 상태 |
| 공유 토큰 교체 · 직원별 관리자 토큰 · VPN | 피해 범위 불변 · 과도한 권한 · 신원 증명 ✗ |
| 만료 30일 API 키 = 단기 자격 증명 | 정적 키 · federation으로 교체 |
| workspace 키로 Usage and Cost API 인증 | Admin API 키 필요 |
| workspace 1개 + 테넌트 헤더 = 격리 | cache · 지출 한도 공유 |
| `setup-token` OAuth 토큰을 공유 자격 증명으로 | 한 사람 구독에 묶임 |
| Bedrock 스타일 ID를 Claude Platform on AWS에 사용 | first-party ID 사용 · 접두사 ✗ |
| Claude Platform on AWS에 OAuth 동의 화면 | OAuth 미지원 → SigV4 + IAM |
| 단일 통합 지점이 비용 · 지연 · 평가 감소 | 일관 적용이 이점 |
| 재시도 증가 · 직렬 큐 · timeout 제거로 느린 제휴사 대응 | retry storm · 무한 지연 · worker 정지 |
| 공급업체 DB 직접 접근 MCP · 공동 system prompt | 공급업체 agent · 정책 우회 · 통제 혼합 |

<sub>근거: CCAR-P-Amey-Thakur-0011, CCAR-P-Amey-Thakur-0012, CCAR-P-Amey-Thakur-0013, CCAR-P-Amey-Thakur-0014, CCAR-P-Amey-Thakur-0015, CCAR-P-Amey-Thakur-0051, CCAR-P-Amey-Thakur-0053, CCAR-P-Amey-Thakur-0067, CCAR-P-Amey-Thakur-0068, CCAR-P-jrajath94-0004, CCAR-P-jrajath94-0010, CCAR-P-jrajath94-0081, CCAR-P-jrajath94-0083, CCAR-P-jrajath94-0084, CCAR-P-jrajath94-0588, CCAR-P-jrajath94-0590, CCAR-P-jrajath94-0591, CCAR-P-jrajath94-0592, CCAR-P-jrajath94-0593, CCAR-P-jrajath94-0594, CCAR-P-jrajath94-0599, CCAR-P-jrajath94-0633, CCAR-P-jrajath94-0634, CCAR-P-jrajath94-0635, CCAR-P-jrajath94-0637, CCAR-P-jrajath94-0706, CCAR-P-preporato-0010</sub>

@@ MEMO

| 이름 | 의미 |
|---|---|
| `error` 이벤트 | 스트림 중 오류 · HTTP 200 이후에도 도착 |
| `retry-after` (429) | 유효한 요청은 대기 후 같은 요청 재전송 |
| OAuth 2.0 위임 토큰 | agent가 요청 사용자 권한으로 동작 |
| federation issuer · federation rule | CI ID 제공자 등록 · 범위와 수명 결정<br>→ 서명 ID 토큰을 단기 Anthropic 토큰으로 교환 |
| Admin API 키 | Usage and Cost API 인증 |
| workspace API 키 | Messages 요청 인증 |
| `setup-token` | OAuth 토큰 발급 · 한 사람 구독에 묶임 |
| workspace | prompt cache 격리 · 월 지출 한도 단위 (Claude API) |
| 조직 수준 Actions secret | 저장소 여러 개가 저장된 사본 1개 공유 |
| outbound web identity federation | Claude Platform on AWS 사용 전 활성화 필수<br>기본 비활성 |
| SigV4 · 워크스페이스 ARN | Claude Platform on AWS의 IAM 호출자 제어 |
| `claude-haiku-5-5` ⚠️ | Claude Platform on AWS model ID 예<br>모델 ID는 시점에 따라 변동 |
| BAA | PHI 처리를 위한 계약 수단 · HIPAA 적격 서비스와 함께 |
| 단일 통합 지점 | 인증 · rate limiting · 로깅 · 라우팅 일괄 적용 |
| timeout · bulkhead · circuit breaker · fallback | 느린 외부 API 대응 4요소 |
| agent-to-agent delegation | 외부 AI agent 협업 방식 |
| effort (낮음 · medium) | 출력 · thinking 작업량 조절 |

<sub>근거: CCAR-P-Amey-Thakur-0013, CCAR-P-Amey-Thakur-0053, CCAR-P-jrajath94-0004, CCAR-P-jrajath94-0010, CCAR-P-jrajath94-0083, CCAR-P-jrajath94-0588, CCAR-P-jrajath94-0590, CCAR-P-jrajath94-0592, CCAR-P-jrajath94-0593, CCAR-P-jrajath94-0594, CCAR-P-jrajath94-0633, CCAR-P-jrajath94-0634, CCAR-P-jrajath94-0637, CCAR-P-jrajath94-0706, CCAR-P-preporato-0010</sub>

@@ CHECK

- [ ] `error` 이벤트 → 200 이후에도 도착
- [ ] 계정 경계 · 거주 요구 → 배포 경로로 해결
- [ ] 자격 증명 → 위임 OAuth · federation
- [ ] 느린 외부 API → 4요소 방어 · 재시도 증가 ✗

<sub>근거: CCAR-P-Amey-Thakur-0011, CCAR-P-Amey-Thakur-0012, CCAR-P-Amey-Thakur-0051, CCAR-P-Amey-Thakur-0052, CCAR-P-Amey-Thakur-0068, CCAR-P-jrajath94-0004, CCAR-P-jrajath94-0083, CCAR-P-jrajath94-0592, CCAR-P-jrajath94-0593</sub>
