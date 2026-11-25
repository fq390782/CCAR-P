@@ ADD-TO: ### 1.1 Workflow vs Agent — 다음 단계를 누가 정하나

| 상황 | 판단 |
|---|---|
| 절차를 사전에 확정 가능한 업무 | 고정 경로 orchestration 적합 |
| 같은 유형 요청도 필요한 대응이 건마다 다름<br>(설명만 · 주문 조회 · escalation 선행) | 고정 경로 ✗ → agent loop |
| `tool_choice` `auto` (기본값) | tool 사용 · 직접 답변을 매 turn Claude가 판단 |
| 앱 상태로 다음 tool 강제<br>· 분류기로 정형 체인에 분기 | 판단을 앱 코드로 되돌림<br>→ 가변 요청에 부적합 |

<sub>근거: CCAR-F-Udemy03-0060</sub>

@@ ADD-TO: ### 1.2 Workflow 패턴 구분

| 상황 | 정답 |
|---|---|
| 단계 · 순서 고정<br>(파일 읽기 → 테스트 실행 → 보고) | 앱 코드가 순서 유지<br>모델 = 보고서 텍스트 작성에만 사용 |
| 다음 단계 시작 전 결과 확인 필요 | 앱 코드가 각 결과 검증<br>실패 시 체인 조기 중단 |
| 단계 B가 단계 A 출력에 의존<br>(이름 추출 → 수수료 계산) | A 직후 · B 직전에 코드 검사<br>실패 시 체인 중단 → 잘못된 값 B 유입 차단 |

| 오답 | 이유 |
|---|---|
| 결과마다 모델이 tool 목록에서 다음 단계 선택 | 유연해 보여도 순서가 코드 아닌 모델에 의존 |
| 의존 단계를 병렬 실행 | 속도 이득 있어도 선행 값 검증 불가 |
| B 이후에 코드로 확인 · 검토자 전달 | B 실행 전 차단 요구 → 이미 유입 |
| compaction으로 잘못된 값 제거 | 이전 턴 요약 작성일 뿐 · 값 검증 ✗ |

<sub>근거: CCAR-P-jrajath94-0604, CCAR-P-jrajath94-0609</sub>

@@ ADD-TO: ### 1.4 Agentic loop (Messages API 직접 사용 시)

**loop 판정 — 안티패턴 3종**

| 구분 | 내용 |
|---|---|
| 판정 근거 | `stop_reason` = Claude가 주는 구조화된 신호<br>`tool_use` → 계속 · `end_turn` → 종료 |
| 안티패턴 1 | 자연어 문구 파싱<br>("끝났습니다" · "더 도와드릴까요" · "조사 완료") |
| 안티패턴 2 | 반복 횟수 상한을 주된 중지 메커니즘으로 사용 |
| 안티패턴 3 | assistant text 유무 = 완료 판정 |
| 안티패턴 증상 | text + `tool_use` 응답에서 loop 종료<br>→ 미실행 tool 호출 잔류 · 불완전한 결과 반환 |
| 흔한 상황 | Claude는 tool 호출 전 설명 text를 자주 씀<br>("먼저 파일을 검색합니다") |

| 오답 수정 | 이유 |
|---|---|
| 종료 문구 후보 추가 · 키워드 판정 | 안티패턴 형태만 바뀜 |
| `tool_choice` `any`로 매 응답 tool 호출 강제 | 판정 메커니즘 수정 ✗ · 모델 출력에 맞춘 우회 |
| system prompt로 "tool 호출 시 설명 text 금지" | 판정 메커니즘 수정 ✗ · 우회 |
| 첫 요청만 `max_tokens` 상향 | 우회 · 판정 결함과 무관 |

**대화 이력 구조 — `tool_use` ↔ `tool_result`**

| 구분 | 내용 |
|---|---|
| API | stateless → 요청마다 대화 전체 전송 |
| 순서 | assistant 메시지(`tool_use` block)<br>→ 바로 다음 user 메시지에 대응 `tool_result` |
| 연결 | `tool_use_id`로 짝 · 사이에 다른 메시지 ✗ |
| user 메시지 내부 | `tool_result`를 text보다 앞(content 배열 맨 앞)<br>text 먼저 = API 오류 |
| 결과 위치 | user turn 안<br>system prompt ✗ · assistant text ✗ |
| 새 `tool_use_id` 발급 | ✗ (원래 id 사용) |
| 증상 1 | assistant turn 누락<br>→ 후속 요청 400 오류 (`tool_use_id`가 가리킬 대상 없음) |
| 증상 2 | 결과가 tool 결과 형식이 아님<br>→ Claude가 같은 tool 반복 요청 |

**위임(Task) 결과 · loop 결함 진단**

| 상황 | 정답 |
|---|---|
| coordinator가 Task `tool_use` 요청 | 각 Task 실행<br>→ `tool_use` id별 `tool_result`를 user turn으로 반환<br>`end_turn`까지 호출 지속 |
| `tool_result` 미전송 증상 | 최종 결과가 최초 text만 근거 |
| trace에 tool 요청만 있고<br>결과 · 최종 답 없음 | loop 구현 결함 의심 (실행 · 결과 반환 누락)<br>→ SDK agent loop 사용 |

| 오답 | 이유 |
|---|---|
| 반복 3회 제한 · Task 생략 | 결과가 안 돌아간 원인 미해결 |
| system prompt에 "Claude가 직접 backend 실행" | 모델이 수행할 수 없는 역할 요구 |
| 완료 문구 검출 | 원인과 무관 |
| 사전 일괄 tool 실행 후 1 turn 요약 | 대화에 따른 tool 선택 포기 |

**`pause_turn` 세부**

| 구분 | 내용 |
|---|---|
| 의미 | server-side tool loop가 작업 도중 반복 한도 도달 |
| 처리 | 응답을 최근 assistant turn으로 포함해 후속 요청<br>→ Claude가 멈춘 지점부터 이어감 |
| 오답 1 | `end_turn`과 동일 취급 → 반쯤 한 결과 반환 |
| 오답 2 | `max_tokens` 올려 원요청 재전송 → 처음부터 · 비용 2회 |
| 오답 3 | 로컬 실행 후 `tool_result` 반환<br>→ server tool은 응답할 `tool_use` 없음 |

<sub>근거: CCAR-F-MyPractice-0058, CCAR-F-Udemy02-0006, CCAR-F-Udemy02-0020, CCAR-F-Udemy03-0008, CCAR-F-Udemy03-0019, CCAR-F-Udemy04-0014, CCAR-F-Udemy05-0017, CCAR-F-Udemy06-0023, CCAR-F-paullarionov-0058, CCAR-F-preporato-0009, CCAR-F-preporato-0010</sub>

@@ ADD-TO: ### 1.5 Loop 종료, 안전장치, 상태

**종료 장치 설계**

| 상황 | 정답 |
|---|---|
| 같은 tool 반복 호출 · 두 tool 왕복<br>· 결론 불가 | 명시적 종료 장치 설계<br>= 반복 횟수 예산 · 반복 호출 감지 · escalation 경로 |
| 종료 + 유용한 산출물 보장 | hard 반복 예산 + 명시적 stop condition<br>+ 산출물 체크리스트(= 완료 정의)<br>+ 예산 소진 시 부분 결과와 함께 사람 escalation |
| 소프트 통제 | "효율적으로 · 신속히" prompt = 요청일 뿐<br>비슷한 지시가 있어도 loop 발생 |

| 오답 | 이유 |
|---|---|
| `max_tokens` · context window · 모델 크기 상향 | 수렴 보장 ✗ · 증상만 지연 |
| 필요한 tool 제거 (검색 tool 등) | 작업 자체 불가 · agent 존재 이유 상실 |
| `temperature` 하향 · 0 | 반복 횟수 제한 ✗<br>결정적 agent는 같은 호출을 결정적으로 반복 |
| 상한 숫자만 증가 (3 → 10 · 8 → 30) | 구조 동일 · 상한 도달 응답을 최종 답으로 취급 ✗ |

**반복 상한의 위치**

| 구분 | 내용 |
|---|---|
| 정상 종료 판정 | `stop_reason` (`end_turn`) |
| tool 호출 횟수 | 모델이 context 기반으로 판단 |
| 상한 설정 | 충분히 크게 · 안전장치로만 유지 |
| 상한이 주된 중단일 때 | 4회 이상 필요한 건만 중간 절단<br>단순 건은 1회 완료 → 복잡도와 무관하게 작동 |
| 상한 도달 시 | 로그 기록 · 이상으로 취급<br>미완료로 기록 (완료 처리 ✗) · 사람 escalation |
| 모니터링 지표 | 상한 도달 횟수 · 예기치 않은 `stop_reason` 값 |

**token · 비용 예산**

| 구분 | 내용 |
|---|---|
| 원칙 | token 예산 = 모델 밖에서 강제 |
| 측정 | loop 안에서 각 응답의 `usage` 필드로<br>입력 · 출력 token 누적 추적 |
| 대응 | 예산 도달 → 코드가 loop 중단<br>예산 약 80% → 마무리 지시 주입 (약한 경고) |
| 오답 1 | Claude에게 사용량 질문 = 추정 · 측정 ✗ |
| 오답 2 | system prompt "50,000 token 이하" = 확률적 |
| 오답 3 | `max_tokens` 50 = 모든 응답 잘림 |

**Agent SDK 상한 · 재개**

| 구분 | 내용 |
|---|---|
| 기본값 | agent loop = turn · 비용 한도 없음<br>범위 넓은 prompt → 실행 장기화 |
| 한도 설정 | `max_turns` · `max_budget_usd`<br>production agent의 기본 선택 |
| 한도 도달 구분 | `ResultMessage`의 `subtype`으로 성공과 구별<br>(`error_max_turns` 등) |
| 이어하기 | `session_id` 저장 → `resume` |
| 단발 `query()` | error result 반환 후 예외 발생<br>→ try로 감싸 다음 요청 진행 |
| 평가 포인트 | "어디서 멈추나" + "멈춘 뒤 어떻게 다루나" 둘 다 필요 |
| 오답 1 | `effort` `"low"` = turn당 소비만 변경 · 상한 ✗ |
| 오답 2 | Stop hook = loop 끝날 때까지 발화 ✗ → 중도 차단 불가 |

**`session budget` (Managed Agents)**

| 구분 | 내용 |
|---|---|
| 동작 | list cost가 상한 도달 → 새 모델 요청 중단<br>세션 일시 중지 |
| 적합 상황 | 단계 미정 agent loop + 세션별 고정 지출 상한 |
| ⚠️ 기능 상태 | 공식 문서상 Managed Agents beta 기능<br>→ 이름 · 동작 변경 가능성 |
| workflow run 여러 개 | 모두 하나의 `session budget`에 포함<br>→ 전체 세션에 budget 1개 |
| 병렬 읽기 + 진행 표시<br>(lead 후속 메시지 금지) | workflow run 1개 + `session budget` 1개 |

| 오답 | 이유 |
|---|---|
| `effort` low | 지출 통제처럼 보여도 상한에서 요청 중단 ✗ |
| session budget 없이 subagent 6개 + 병합 | 폭주 지출 상한 부재 |
| 검색 단계를 코드에 하드코딩 | 단계 미정 작업에 부적합 |
| run마다 별도 budget | run은 하나의 budget에 포함 → 이중 설정 |
| subagent별 후속 메시지 · lead → worker 후속 메시지 | 제약 위반 (후속 메시지 금지) |

<sub>근거: CCAR-F-Amey-Thakur-0001, CCAR-F-Amey-Thakur-0013, CCAR-F-Udemy01-0045, CCAR-F-Udemy04-0014, CCAR-F-Udemy05-0045, CCAR-F-Udemy06-0023, CCAR-F-preporato-0013, CCAR-P-jrajath94-0023, CCAR-P-jrajath94-0603, CCAR-P-jrajath94-0606</sub>

@@ ADD-TO: ### 1.7 구현 수단 비교

**동기 Messages API vs Message Batches API**

| 상황 | 정답 |
|---|---|
| 결과를 바로 받아야 하는 blocking 판정<br>(PR merge 전 pass/fail gate) | 동기 `POST /v1/messages` |
| 즉시성 불필요 대량 감사<br>(주간 40,000건 · 다음 날 검토) | Message Batches API + 요청별 `custom_id` |
| 야간 재처리 + 대화형 검증 혼재 | 재처리 = Batches<br>대화형 검증 = 동기 Messages API |
| 반복되는 공통 prefix<br>(추출 지시 · JSON schema) | prompt caching → 읽기분 입력 요금 절감 |

| 항목 | 내용 |
|---|---|
| 판단 순서 | 워크로드별 대기 허용도 먼저 확인<br>→ 반복 입력 유무 확인 |
| ⚠️ 요금 · 시간 | 일반 요금의 50% · 대부분 1시간 이내 · 최대 24시간<br>→ 시점 따라 변동 가능 |
| 결과 조회 | 전체 처리 완료 또는 24시간 경과 시점 |
| 결과 순서 | 투입 순서 보장 ✗ → `custom_id`로 대조 |
| prompt caching 병행 | batch에서도 사용 가능 · 할인 중첩 가능 |

| 오답 | 이유 |
|---|---|
| 둘 다 Batches (+ 상태 polling) | blocking 판정을 비동기로 만듦 |
| 배정 반대 (검증 = Batches · 감사 = 동기) | 대기 불가 처리를 비동기로 만듦 |
| streaming 동시 요청으로 대량 감사 | 대기 시간 차이를 잘못 파악 |
| 대화형 검증이 1시간 내 끝나길 기대 | 최대 24시간 걸릴 수 있음 |

<sub>근거: CCAR-F-Udemy01-0021, CCAR-F-Udemy03-0047</sub>

@@ NEW-SECTION
### 프로그램 강제 vs prompt 지시
**확실히 지켜야 하면 모델 밖 코드로 강제**

| 구분 | 프로그램 강제 | prompt 지시 |
|---|---|---|
| 수단 | hook · gate · 전제 조건<br>· tool 권한 · CI gate<br>· tool 구현 내 검증 | system prompt · `CLAUDE.md`<br>· tool description · few-shot |
| 보장 | 결정적 (모델 판단 ✗) | 확률적 · 실패율 0 ✗ |
| 적합 | 예외 불인정<br>위반 = 법령 · 금전 · 비가역 피해 | 문체 · 설명 품질 · 안내 덧붙이기<br>유연한 판단 · 위반 영향 작음 |

| 상황 | 정답 |
|---|---|
| "확실하게 막는다" · "예외 불인정"<br>· "~일 때만 실행" | 모델 밖에서 판정하는 메커니즘 |
| 금액 · 건수처럼 기계 판정 가능한 규칙 | 코드 강제 (가치 높음) |
| prompt에 규칙이 있는데도 위반 발생<br>(월 수 건 · 0.8% · `CLAUDE.md` 금지 무시) | prompt 강화 ✗ → hook · gate 추가 |
| 법령 위반 · 금전 손실 직결 + tool 호출로 검사 가능<br>(예: 수출 관리 대상 발송) | hook으로 강제 |
| 유연한 판단 · 위반 영향 작음<br>(어조 · 안내 문구) | prompt 지시로 충분 |
| 필수 artifact 없이 승인 · 공개 실행 금지 | `PreToolUse` hook 거부<br>+ 실행 전 CI gate · tool 권한 제거 |
| 임계값 초과 환불 차단 + 사람 인계 | 앱 측 guard 또는 tool 구현 내 금액 검증<br>→ `escalate_to_human`으로 유도 |

**강제 수단별 동작**

| 수단 | 동작 |
|---|---|
| `PreToolUse` hook | tool 실행 직전 검사 → `permissionDecision` `"deny"`<br>`permissionDecisionReason`으로 이유를 모델에 전달 |
| hook 평가 시점 | 권한 평가보다 먼저 실행<br>deny 시 `bypassPermissions` 모드에서도 차단 |
| `PostToolUse` hook | 실행 후 동작 → 방지 수단 ✗ |
| hook matcher | `Bash`로 좁힘 → `tool_input`의 `command` 검사<br>(`apply` · `destroy` 등 파괴적 하위 명령 일괄 판정) |
| subagent `tools` 제한 | 부여 안 된 tool은 그 subagent에 비노출<br>예: 공개 tool은 coordinator만 보유 |
| 앱 측 guard | client tool = Claude는 호출 요청만<br>실행 여부 최종 결정 = 앱 |
| tool 구현 내 검증 | 요청 금액 검증 → 임계값 초과 거부 |
| CI gate | Claude Code 단계 전 합격 artifact 없으면 job 실패 |

| 오답 | 이유 |
|---|---|
| 지시 추가 · 강조 · 문서 맨 앞으로 이동 · 영향 설명 | 요청일 뿐 · 같은 확률적 메커니즘 |
| `PostToolUse` hook 사후 검사 · 알림 · rollback | 이미 실행됨 → 방지 ✗ |
| `tool_choice`로 특정 tool 강제 | 순서 · 조건 판정 수단 ✗<br>일률 강제 → 소액 정당 환불까지 차단 · 해결률 저하 |
| `temperature` 0 · few-shot · 평가 반복 | 확률적 동작을 결정적으로 못 바꿈 |
| tool description에 조건 기재 | prompt 지시와 같은 확률적 준수 |
| 사후 로그 감지 · 담당자 취소 | 잘못된 실행 자체를 못 막음 |
| tool 제거 (`process_refund` 삭제) | 정당한 처리까지 차단 |
| 완료 후 hook으로 artifact 확인 | 실행 후 → 방지 ✗ |
| 공개 tool을 `PostToolUse`로 사후 거부 | 이미 공개됨 |
| coordinator 지시에 "검증 후 공개" 추가 | 요청에 그침 |

<sub>근거: CCAR-F-Udemy01-0019, CCAR-F-Udemy02-0010, CCAR-F-Udemy02-0032, CCAR-F-Udemy04-0016, CCAR-F-Udemy04-0053, CCAR-F-Udemy05-0016, CCAR-F-Udemy06-0050, CCAR-F-Udemy06-0051</sub>

@@ NEW-SECTION
### 전제 조건 gate 설계
**gate 조건 = "호출됨"이 아니라 "검증됨"**

| 구분 | 내용 |
|---|---|
| 전제 조건 | 선행 단계 완료 전까지 후속 tool 호출 차단<br>(programmatic) |
| 예 | `get_customer`가 검증된 ID 반환 전<br>`lookup_order` · `process_refund` 차단 |
| '완료' 정의 | 호출 사실 ✗ · 검증된 결과(ID) 획득 ✓ |
| 오류 사례 | 호출 여부만 보는 gate<br>→ 후보 여러 명 일치에도 통과 → 타인 계정 환불 |
| 보강 1 | 검증된 ID를 session 상태에 유지<br>`process_refund` 인수의 ID와 일치 확인 |
| 보강 2 | 후보 다수 → 추측 선택 ✗<br>추가 식별 정보를 고객에게 질문 |
| 사고 후 진단 | gate가 있는데 사고 → gate 조건 자체를 의심 |

| 상황 | 정답 |
|---|---|
| tool 호출 순서 위반<br>(`get_customer` 건너뛰고 `lookup_order` 직행) | 코드 수준 precondition |
| subagent 순서 위반<br>(분석 결과 · 출처 반환 전 보고서 위임) | orchestration 계층 precondition<br>필요한 결과 · 출처 대응 갖출 때까지 위임 거부 |
| 본인 확인 전 배송지 변경 | 코드로 확인 → 미확인 시 tool 거부 |
| gate 거부 시 | 이유를 tool 결과로 agent에 반환<br>→ 올바른 절차로 복귀 |
| 위반 조작 차단 후 | 대체 workflow로 유도<br>(plan 결과 담당자 확인 등) |
| 운영 | 거부 건수 기록 → 절차 생략 지점 · prompt 개선 진척 추적 |

| 오답 | 이유 |
|---|---|
| 순서를 보여 주는 few-shot | 확률적 · 건너뜀 가능성 잔존 |
| system prompt 더 강하게 명시 | 확률적 · 실패율 0 ✗ |
| routing classifier로 tool 일부만 활성화 | 건너뜀 가능성 자체를 제거 못함 |
| 반복 횟수 증가 · `tool_choice` 강제 | 순서를 제어하는 메커니즘 ✗ |
| 지시 강화 (coordinator) | 요청에 그침 |

**gate 판정을 실행에 연결**

| 구분 | 내용 |
|---|---|
| 핵심 | gate 판정이 코드에서 출시 결정으로 연결 · fail closed |
| 차단 없는 verification | 장식 (guardrail ✗ · 대시보드) |
| gate 역할 | gate마다 하나 · 다른 gate 역할 대신 ✗ |
| 조치 | 코드로 차단 + 실패 원인 계층(retrieval · prompt) 수정 |
| 전제 | 원인 수정에 실패 trace 필요 |
| 부작용 | 차단 → false-positive 차단 증가 가능<br>→ 원인 수정 신속 필요 |

| 오답 (gate 있는데 실패 초안 출시) | 이유 |
|---|---|
| 모든 답변 사람 검토 | 하루 50,000건 × 30초 = 417 검토자-시간<br>원인 미수정 |
| 10% 표본 검토 | 실패의 90% 통과 |
| gate 제거 | 작동하는 탐지기 파괴 → 눈 가리고 출시 |

| 조건 변화 | 정답 변화 |
|---|---|
| 하루 100건 + 답변마다 법적 노출 | 전면 사람 검토 |
| 실패 드묾 + 표본을 eval 라벨 세트로 활용 | 표본 검토 |
| gate false-positive가 탐지율 초과 + 더 나은 검사 존재 | gate 교체 · 제거 |

<sub>근거: CCAR-F-MyPractice-0051, CCAR-F-Udemy01-0019, CCAR-F-Udemy01-0020, CCAR-F-Udemy04-0005, CCAR-F-Udemy04-0016, CCAR-F-Udemy04-0053, CCAR-F-Udemy06-0051, CCAR-F-paullarionov-0051, CCAR-P-jrajath94-0114</sub>

@@ NEW-SECTION
### 비가역 작업 통제와 사람 승인
**위험 = 피해 크기 · 모델 밖에서 통제**

| 구분 | 내용 |
|---|---|
| 운영 위험을 가장 키우는 특성 | checkpoint 없이 되돌릴 수 없는 작업 수행 |
| 이유 | 되돌릴 수 있는지 = 틀렸을 때 비용 · 피해 범위 결정 |
| 영향 작은 것 | 모델 수 · 구조 · 실행 시간<br>→ 비용 · 복잡도에만 영향 |
| 오류 확률 vs 피해 | 모델 성능 · prompt 길이 · tool 수 = 오류 확률에 영향<br>피해 크기 · 비용에는 영향 ✗ |

| 상황 | 정답 |
|---|---|
| 자율 단계가 production 데이터 수정 | 사람 승인 checkpoint 또는 되돌림 장치<br>모델 밖에서 강제 |
| 틀린 결정의 비용 최소화 | 동작을 되돌릴 수 있게 구성<br>또는 확인을 거쳐야 실행되게 구성 |
| 금전 이동 · 고객 대상 메시지<br>(모델 단독 실행 금지) | 모델은 제안 · gate가 처분<br>작성 = 자동 · 발송 · 환불 = gate 뒤 |
| gate 구성 예 | 규칙 엔진이 정책 · 금액 · 사기 flag 확인<br>발송 = 사람 승인 |
| `dry_run` 우회 방지<br>(미리보기 후 실행 강제) | preview · execute 두 tool 분리<br>preview = 영향 세부 + 1회용 confirmation token<br>execute = token 필수 → 실행을 preview에 바인딩 |

| 오답 | 이유 |
|---|---|
| 더 큰 모델 · 더 긴 system prompt · 재시도 | 피해 범위 제한 ✗ |
| "double-check the policy" 지시 | 여전히 모델 판단 → prompt-plea 함정 |
| 행동 전 추론 상세 설명 요구 | 결정 주체 불변 · 모델 단독 실행 |
| 두 agent 투표 · 둘 다 동의 시 실행 | 모델 판단 2개 · 결정론적 · 사람 점검 없음 |
| 직전 60초 내 `dry_run=true` 이력 validation | 시간 간격 heuristic 의존 |
| tool에 confirmation 표시 + orchestration 계층이 승인 요청 | orchestration 계층의 정상 동작에 의존 |
| tool 설명 · few-shot으로 preview 먼저 호출 지시 | LLM 지시 준수에 의존 |

<sub>근거: CCAR-F-Amey-Thakur-0014, CCAR-F-Amey-Thakur-0053, CCAR-F-Amey-Thakur-0068, CCAR-F-MyPractice-0061, CCAR-P-jrajath94-0067</sub>

@@ NEW-SECTION
### 병렬 tool 호출과 loop 수 줄이기
**독립 호출은 한 turn에 · 결과는 한 user 메시지에**

| 구분 | 내용 |
|---|---|
| 기본 동작 | Claude = 한 응답에서 여러 tool 호출(parallel tool use) 가능 |
| 호출 쪽 | 독립 호출을 한 assistant turn에서 함께 발행 |
| 반환 쪽 | 모든 `tool_result`를 하나의 user 메시지로 묶어 반환 |
| 결과 분리 반환 | 별도 user 메시지 → 병렬 호출 회피를 Claude에게 학습시킴 |
| `disable_parallel_tool_use` | `tool_choice` 안에서 `true`면 병렬 비활성<br>→ 기본값 `false` 유지 |
| 요령 | 호출 방식 + 결과 반환 방식 둘 다 확인 |

| 상황 | 정답 |
|---|---|
| 독립 subagent 조사 3개를 순차 처리 | 한 assistant turn에서 Agent 호출 함께 발행<br>결과는 다음 user 메시지에 묶어 반환<br>`disable_parallel_tool_use` 기본값 유지 |
| 처음부터 둘 다 필요한 tool을 별도 turn에 요청<br>→ API loop 수 과다 | prompt로 관련 tool 요청을 한 turn에 묶게 지시<br>결과를 함께 반환 후 다음 호출<br>(구조 변경 최소) |

| 오답 | 이유 |
|---|---|
| 한 번에 하나씩 호출 + background 지정 | 순차 대기 잔존 |
| subagent 요약을 완료 즉시 개별 user 메시지로 반환 | 순차 대기 잔존 · 병렬 회피 학습 |
| 필요할 만한 tool 자동 병렬 호출 (speculative execution) | 요청하지 않은 tool 실행 · 결과 반환 |
| `max_tokens` 상향 | 출력 제한 · tool 요청 결합과 무관 |
| composite tool (`get_customer_with_orders`) | tool 설계 변경 필요 · 최소 변경 아님 |

<sub>근거: CCAR-F-MyPractice-0053, CCAR-F-Udemy01-0028, CCAR-F-Udemy03-0008, CCAR-F-paullarionov-0053</sub>

@@ NEW-SECTION
### 기타 — trace · 경계 계약 · retrieval 분할
**진단 = trace · 경계 = 계약 · 혼입 = 분할**

| 상황 | 정답 |
|---|---|
| production agent 디버깅 · 실패 원인 진단 | 단계별 trace 기록<br>(각 단계 입력 · tool 호출 · 출력) |
| trace가 필요한 이유 | 비결정적 실행을 사후 재구성 가능 |
| 각 구성요소는 정상인데 경계에서 간헐 실패 | 둘 사이 계약(interface) 불충분<br>특히 edge case · 오류 case |
| 여러 지역 · 팀 정책이 답변에 혼입 | 데이터 도메인별 분할<br>문서에 지역 tag<br>→ semantic search 전 사용자 지역으로 retrieval 필터 |

| 오답 | 이유 |
|---|---|
| tool 수 축소 · 단일 모델 통일 | 단순화일 뿐 원인 설명 ✗ |
| step 한도 상향 | 실패만 길어짐 · 더 분명해지지 않음 |
| 최종 출력 · token 총량 · 모델 버전만 기록 | 어느 지점에서 어긋났는지 알 수 없음 |
| 더 큰 모델 · 구성요소 추가 (경계 실패) | 인터페이스 정의 ✗ |
| 재시도 (경계 실패) | 문제 은폐 |
| 전 지역 정책 전부 투입 | context stuffing |
| 지역별 agent 14개가 협상 | retrieval 문제에 조율 장치만 추가 |
| 사용자에게 지역 언급 요청만 | 혼합 retrieval 유지 |

<sub>근거: CCAR-F-Amey-Thakur-0017, CCAR-F-Amey-Thakur-0054, CCAR-P-Amey-Thakur-0070, CCAR-P-preporato-0005</sub>

@@ RULES

| 상황 | 정답 |
|---|---|
| 무한 loop · tool 왕복 · 결론 불가 | 종료 장치 설계: 반복 예산 · 반복 호출 감지 · escalation |
| loop 계속 · 종료 판정 | `stop_reason` 확인 (문구 · text 유무 ✗) |
| 반복 횟수 상한 | 안전장치로만 사용 · 도달 시 미완료 기록 + escalation |
| token · 비용 예산 | 코드가 `usage` 누적 측정 → 초과 시 중단<br>약 80%에서 마무리 지시 주입 |
| 무인 Agent SDK 실행 | `max_turns` · `max_budget_usd` + `subtype` 확인<br>+ `session_id` resume |
| 단계 미정 + 세션별 고정 지출 상한 | agent loop + `session budget` |
| 후속 요청 400 · 같은 tool 반복 요청 | assistant `tool_use` turn<br>+ 바로 다음 user `tool_result` 확인 |
| `stop_reason: "pause_turn"` | 응답을 assistant turn으로 보내 이어감 |
| 독립 tool 호출이 순차 처리됨 | 한 turn에 묶어 발행 + 결과를 한 user 메시지로 반환 |
| 같은 유형인데 필요한 대응이 건마다 다름 | 고정 경로 ✗ · `tool_choice` `auto` + loop |
| "확실히 막는다" · 예외 불인정 | 모델 밖 강제: `PreToolUse` hook · gate · tool 구현 검증 |
| prompt에 규칙이 있는데 위반 발생 | hook · gate 추가 (prompt 강조 ✗) |
| 선행 단계 미완료 시 후속 tool 차단 | 검증된 결과(ID)를 조건으로 한 programmatic precondition |
| 비가역 · 금전 · 고객 발송 | 사람 승인 · gate · 되돌림 장치 (모델은 제안) |
| 단계 간 값 의존 | 다음 단계 전 코드 검사 → 실패 시 체인 중단 |
| 결과 즉시 필요 vs 지연 가능 대량 | 동기 Messages API vs Batches + `custom_id` |
| 디버깅 · 실패 진단 | 단계별 trace |
| 지역별 정책 혼입 | tag + retrieval 필터링 |

<sub>근거: CCAR-F-Amey-Thakur-0001, CCAR-F-Amey-Thakur-0013, CCAR-F-Amey-Thakur-0017, CCAR-F-Amey-Thakur-0053, CCAR-F-Amey-Thakur-0054, CCAR-F-Udemy01-0021, CCAR-F-Udemy01-0028, CCAR-F-Udemy01-0045, CCAR-F-Udemy02-0010, CCAR-F-Udemy03-0019, CCAR-F-Udemy03-0060, CCAR-F-Udemy04-0005, CCAR-F-Udemy05-0017, CCAR-F-Udemy06-0050, CCAR-F-paullarionov-0051, CCAR-F-paullarionov-0058, CCAR-F-preporato-0010, CCAR-F-preporato-0013, CCAR-P-jrajath94-0023, CCAR-P-jrajath94-0067, CCAR-P-jrajath94-0603, CCAR-P-jrajath94-0609, CCAR-P-preporato-0005</sub>

@@ TRAPS

| 오답 | 이유 |
|---|---|
| text가 있으면 · 완료 문구가 있으면 loop 종료 | text와 `tool_use` 공존 · 구조화된 신호 아님 |
| 반복 횟수 상한을 주된 종료 조건으로 사용 | 복잡한 건만 중간 절단 · 상한은 안전장치 |
| 상한 숫자만 증가 | 구조 동일 · 안티패턴 유지 |
| `temperature` 0 · 큰 모델 · context 확대로 loop 해결 | 반복 제한 ✗ · 수렴 보장 ✗ |
| `effort` low · Stop hook으로 지출 상한 | turn당 소비만 변경 · loop 끝나야 발화 |
| assistant turn 없이 `tool_result`만 전송 | 400 오류 · 대응 `tool_use` 소실 |
| `pause_turn`을 `end_turn`처럼 처리<br>· `max_tokens` 올려 재전송 | 반쯤 한 결과 반환 · 처음부터 + 비용 2회 |
| prompt 강화 · `CLAUDE.md` 강조 · few-shot<br>· `temperature` 0 → 100% 준수 기대 | 확률적 · 실패율 0 ✗ |
| `PostToolUse` hook으로 위반 방지 | 실행 후 동작 |
| `tool_choice` 강제로 순서 · 조건 통제 | 제어 메커니즘 ✗ · 일률 강제 부작용 |
| 호출 여부만 보는 gate | 검증된 결과(ID) 확인 아님 |
| 모델 self-check · 2 agent 투표로 비가역 통제 | 모델 판단 · 결정 주체 불변 |
| 전면 사람 검토 · 10% 표본 검토 | 규모상 비실현 · 실패 90% 통과 |
| 둘 다 Batches · 배정 반대 | blocking 판정을 비동기로 만듦 |
| tool 결과를 개별 user 메시지로 반환 | 순차 대기 잔존 · 병렬 회피 학습 |
| 단계 미정 작업을 코드에 하드코딩 | 다음 단계를 결과로 정하는 작업에 부적합 |

<sub>근거: CCAR-F-Udemy01-0021, CCAR-F-Udemy01-0028, CCAR-F-Udemy01-0045, CCAR-F-Udemy02-0006, CCAR-F-Udemy02-0010, CCAR-F-Udemy04-0005, CCAR-F-Udemy04-0014, CCAR-F-Udemy05-0017, CCAR-F-Udemy05-0045, CCAR-F-Udemy06-0023, CCAR-F-Udemy06-0051, CCAR-F-paullarionov-0051, CCAR-F-preporato-0009, CCAR-F-preporato-0010, CCAR-P-jrajath94-0023, CCAR-P-jrajath94-0067, CCAR-P-jrajath94-0114, CCAR-P-jrajath94-0603</sub>

@@ MEMO

| 이름 | 의미 |
|---|---|
| `pause_turn` | server tool loop 반복 한도 도달 → 응답을 이어 보냄 |
| `max_turns` · `max_budget_usd` | Agent SDK의 turn · 비용 상한 |
| `ResultMessage` `subtype` | 성공과 한도 도달 구분 (`error_max_turns` 등) |
| `session_id` | 중단된 요청을 `resume`하는 식별자 |
| `usage` 필드 | 응답별 token 사용량 → 누적 측정 |
| `session budget` | list cost 상한 → 새 모델 요청 중단<br>⚠️ Managed Agents beta 기능 |
| `PreToolUse` hook | 실행 직전 검사 · `deny`로 차단 |
| `PostToolUse` hook | 실행 후 동작 · 방지 수단 ✗ |
| `permissionDecision` · `permissionDecisionReason` | `deny` 결정 · 이유를 모델에 전달 |
| precondition(전제 조건) | 선행 단계 완료 전 후속 tool 차단 |
| `disable_parallel_tool_use` | `true`면 병렬 tool 호출 비활성 (기본 `false`) |
| `tool_choice` `auto` | tool 사용 · 직접 답변을 Claude가 판단 |
| `custom_id` | batch 결과를 요청과 대조하는 키 |

<sub>근거: CCAR-F-Udemy01-0019, CCAR-F-Udemy01-0021, CCAR-F-Udemy01-0028, CCAR-F-Udemy01-0045, CCAR-F-Udemy03-0060, CCAR-F-Udemy04-0016, CCAR-F-paullarionov-0051, CCAR-F-preporato-0010, CCAR-F-preporato-0013, CCAR-P-jrajath94-0603</sub>

@@ CHECK

- [ ] loop 종료 판정 = `stop_reason` · 반복 상한 = 안전장치 (text · 문구 ✗)
- [ ] token · 비용 예산 = 코드가 `usage` 측정 · 중단 (prompt ✗)
- [ ] 확실히 막을 규칙 = `PreToolUse` hook · gate (prompt · `PostToolUse` ✗)
- [ ] gate 조건 = 검증된 결과 · 비가역 작업 = 사람 승인 (모델은 제안)

<sub>근거: CCAR-F-Udemy01-0019, CCAR-F-Udemy01-0045, CCAR-F-Udemy04-0005, CCAR-F-Udemy05-0017, CCAR-F-preporato-0013, CCAR-P-jrajath94-0067</sub>
