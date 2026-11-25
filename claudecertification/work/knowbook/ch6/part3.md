@@ ADD-TO: ### 1.7 Context는 예산이다 (context rot)

**예산 배분과 품질 저하 원인**

| 구분 | 내용 |
|---|---|
| 예산 배분 | window = 희소 자원<br>지침 · 검색 자료 · 작업 상태 사이 의도적 배분 |
| 가득 채우기 | 희석 유발 ✗<br>긴 문서 외에서도 문제 |
| window 확대 | 배분 문제 미해결<br>품질 저하 시 키우기 ✗ |
| 긴 agentic 실행 품질 저하 | 원인 = context 누적<br>관련 내용과 오래된 내용 경쟁 |
| 원인 아님 | 모델 버전 변경 (실행 중 불변)<br>낮은 temperature (다양성만 감소)<br>tool 지연 (정확도 무관) |
| 50턴 후 지연 · 비용 증가 | 원인 = 전체 이력이 매 API 요청에 포함<br>(Claude API = stateless) |
| 짧은 대화(2,500 token)에서 지침 이탈 | assistant 응답 누적 → system prompt 비율 감소<br>모델이 자기 이전 출력에 패턴 매칭 → drift |
| 지침 약화 원인 아님 | system prompt 1회 전송 ✗ (매 호출 포함)<br>주의 저하 ✗ (짧은 길이에서 설명 안 됨) |
| 비대한 system prompt<br>(절차 수십 개 · 요청당 1~2개만 사용) | 핵심 role · 규칙만 system prompt<br>절차별 Skill · 검색 모듈 → 관련 시 로드 |

**입력 크기와 출력 상한**

| 구분 | 내용 |
|---|---|
| context window | 한 턴의 입력 + 새 출력을 함께 담음 |
| `max_tokens` | 응답 출력만 제한<br>window 확보 수단 ✗ |
| 보고서가 window에 들어감 | 한 요청으로 전송 · `max_tokens` = 예상 출력<br>청크별 분할 요청 ✗ |
| ⚠️ 모델별 window 크기 | 시점에 따라 변함<br>공식 문서(context windows)로 확인 |
| 입력 예산 준수 + 모델 고정 | 전송 전 대상 모델 ID로 token 계산<br>예산 초과 이력은 앱이 절단 |
| 사전 확인 수단 아님 | 응답 `usage` 필드 (호출 후 도착)<br>`effort` low · 큰 window 모델로 전환 |

<sub>근거: CCAR-F-Amey-Thakur-0032, CCAR-F-Amey-Thakur-0064, CCAR-F-MyPractice-0067, CCAR-F-MyPractice-0075, CCAR-P-Amey-Thakur-0031, CCAR-P-Amey-Thakur-0064, CCAR-P-jrajath94-0587, CCAR-P-jrajath94-0623, CCAR-P-preporato-0008</sub>

@@ ADD-TO: ### 1.8 Context hygiene: prune, compact, isolate

**실패 신호와 범위 격리**

| 구분 | 내용 |
|---|---|
| 조기 신호 | 같은 일 반복 · 앞선 결정과 모순<br>= 상태 소실의 행동 증상 |
| 신호 아님 | 소요 시간 · token 비용 · tool error<br>(원인 다양 · 무관) |
| 고객 간 오염<br>(다른 고객 조회를 재사용) | 원인 = context 범위 설정 결함<br>window 크기 문제 ✗ |
| 처방 | 대화마다 context 범위 = 고객 1명<br>대상 변경 시 이전 조회 결과 삭제 · 격리 |
| 대안 ✗ | window 확대 · tool 제거<br>"고객 신원에 주의" 지시 |

**Tool 결과 입구 축소**

| 구분 | 내용 |
|---|---|
| 입구 trim | tool wrapper가 필요 필드만 `tool_result`로 반환<br>예: 45필드 중 5개 · 40+ 필드 중 관련 항목 |
| 구현 위치 | tool 구현 변경<br>`PostToolUse` hook으로 모델 전달 전 변환 |
| 효과 | 필요 수치가 대량 정보에 묻히는 문제 방지<br>(혼동 예방) |
| context editing과 차이 | 쌓인 결과를 나중에 지움 = 대증요법<br>payload 크기(원인) 미해결 |
| 첫 검토 항목 | 정보가 context에 들어오는 입구에서 줄일 수 있나 |
| 대안 ✗ | 이전 결과 전부 삭제 → 필요한 사실 손실<br>단계적 요약 → 수치 모호화<br>큰 window → 묻힘 해결 ✗ |
| 보조 | 사실은 `case facts` 블록으로 별도 유지 |

**Context editing: `clear_tool_uses`**

| 구분 | 내용 |
|---|---|
| ⚠️ 활성화 | beta header<br>`context-management-2025-06-27`<br>beta 단계 · 시점에 따라 변함 |
| 전략 | `clear_tool_uses_20250919` |
| 동작 | 입력 token이 trigger 초과 → 서버 측에서<br>오래된 tool result를 placeholder로 대체<br>`keep`으로 지정한 최근 결과만 유지 |
| 제외 | `exclude_tools` = 지우면 안 되는 tool 지정<br>(예: 초반 `get_incident` 정의 결과) |
| 요약 호출 | 불필요 (규칙 기반 제거)<br>추가 모델 호출 금지 제약에 적합 |
| 설계 순서 | tool별 재참조 필요 여부 정리 → 삭제 설정 |
| 대안 ✗ | `search_logs` 반환 건수 증가 = 총량 불변<br>앞에서부터 절단 = 초반 핵심 정보 손실<br>매 턴 전 tool 결과 삭제 = 최근 작업 손실 |

<sub>근거: CCAR-F-Amey-Thakur-0036, CCAR-F-Amey-Thakur-0078, CCAR-F-Udemy02-0051, CCAR-F-Udemy03-0010, CCAR-F-Udemy06-0004, CCAR-P-jrajath94-0624</sub>

@@ NEW-SECTION
### Context 결함 5종 진단

**증상 → 결함 이름 → 처방 1:1 대응**

| 결함 | 증거 문구 | 처방 |
|---|---|---|
| growth | 매 호출 대량 로드<br>(한 학기 · 한 시즌 · 분기 전체) | just-in-time retrieval |
| duplication | 같은 내용 반복 삽입<br>(정책 4번 · 측정값 2~3번) | 조립 시점 dedupe<br>(표준 fact key 필요) |
| loss | compaction 후 이름 · 결정 · 숫자 소실 | 요약이 사실을 보존하도록 수정 |
| exhaustion | 작업 도중 window 가득 → 중단 · 오류 | 여유 공간 확보 · 이른 compaction<br>(임계값 튜닝 필요) |
| dilution | 엉뚱한 구간에 attention<br>(7월 질문에 3월 데이터 · 틀린 판례) | 더 적고 더 잘 배치된 chunk |

**진단 규칙**

| 구분 | 내용 |
|---|---|
| 선택 기준 | 증거가 명시된 결함만 선택 |
| exhaustion 제외 | overflow · 오류 언급 없음 |
| loss 제외 | turn 소실 언급 없음 |
| 흔한 조합 | 대량 로드 + 엉뚱한 답 → growth + dilution<br>대량 로드 + 반복 삽입 → growth + duplication |
| 처방 | 결함마다 처방이 다름<br>한 처방으로 전부 해결 ✗ |
| duplication에 chunk 추가 ✗ | 반복 배가 |
| exhaustion에 턴별 요약 ✗ | drift · 비용 누적 |
| 감사관이 전체 대화 요구 | growth 아님 → 별도 보관 필요<br>(다음 소절) |

<sub>근거: CCAR-P-jrajath94-0149, CCAR-P-jrajath94-0296, CCAR-P-jrajath94-0348, CCAR-P-jrajath94-0412, CCAR-P-jrajath94-0475, CCAR-P-jrajath94-0538</sub>

@@ NEW-SECTION
### Just-in-time retrieval · 원본 보관 분리

**window 확대 ✗ · working set 축소**

| 상황 | 정답 방향 |
|---|---|
| 매 호출 전체 로드, 질문은 일부만 필요<br>(논문 25편 중 2~3편 · 매뉴얼 중 한 챕터) | 관련 부분만 just-in-time retrieval |
| 긴 이력 + 비용 증가 + 혼동<br>(6개월 정비 이력 · 3시간 session · 선례 40건) | JIT retrieval + compaction<br>(중복 있으면 dedupe 추가) |
| 턴마다 token 증가 · 초기 세부 정보 필요<br>(30턴 60,000 token · 비용 3배) | 오래된 턴 = JIT retrieval<br>token 임계값에서 compaction trigger<br>→ working set 작게 유지 |
| 전체 이력 장기 보관 의무<br>(7년 · 규제 당국이 임의 session 요구) | 전체 = 비용 책정 · 상한 있는 저장소<br>active context = working set<br>필요 시 JIT 검색 |

**JIT 전제 · 한계**

| 구분 | 내용 |
|---|---|
| 보관 vs context | 보관 = 저장소의 일<br>context = working set |
| 저장소 요건 | 보관 기간 · 접근 제어 · redaction |
| 비용 | 7년치 session = 실제 비용 → 비용 책정 필요 |
| JIT 전제 | 이력이 엘리베이터 · 날짜 등으로 색인 |
| JIT 한계 | 관련 있는 오래된 기록 누락 가능<br>색인 품질 = 답 품질 상한 |
| 연결 끊김 | JIT 경로 테스트 필요<br>끊기면 이력 고립 |
| compaction trigger 전제 | 요약이 결정 · 사실 보존 |

**대안 평가**

| 대안 | 판정 |
|---|---|
| 더 큰 window | 증가 곡선 불변 · 청구서만 지연<br>예외: 매 호출 전체가 필요 + 예산 허용 |
| 더 강한 tier | 모델 계층 문제용<br>(chunk 존재 · 답 틀림일 때만) |
| 더 긴 prompt | 토큰 문제에 토큰 추가 |
| 매 턴 전체 요약 | 호출 비용 · 요약 누적 drift |
| 오래된 턴 말없이 절단 | 무엇이 빠졌는지 불투명<br>필요한 초기 세부 정보 소실 |
| 야간 요약 후 원본 삭제 | 규제 요구 증거 삭제 (요약 ≠ session) |
| 마지막 10턴만 유지 | 규제 당국 행동에 도박 |
| 전체 이력을 active context에 | 비용 · dilution 폭발 |

<sub>근거: CCAR-P-jrajath94-0147, CCAR-P-jrajath94-0150, CCAR-P-jrajath94-0293, CCAR-P-jrajath94-0349, CCAR-P-jrajath94-0411, CCAR-P-jrajath94-0474, CCAR-P-jrajath94-0537</sub>

@@ NEW-SECTION
### Compaction 요약 계약 · 절단 지점

**임계값 = 언제 · 계약 = 무엇이 남나**

| 구분 | 내용 |
|---|---|
| compaction 경계 | 설계상 정보 손실<br>유지할 결정 · 제약을 요약에 명시 |
| 요약 계약 | 보존 항목 명시: 이름 · 결정 · 숫자 · 미해결 항목<br>체크리스트로 검증 |
| 계약 유지 | 새 사실 유형 → 계약에 추가<br>요약 형식 = 파싱 가능 |
| 임계값 조정 | 낮춤 → 손실 요약이 더 자주 → 소실 가속<br>높임 → 작동 시 같은 손실<br>내용 결함은 임계값으로 못 고침 |
| compaction 제거 | 작업 도중 window 포화 (exhaustion) |
| 대안 ✗ | 모델 기억 의존 · window 확대<br>작업 재시작 (해 둔 작업 폐기) |

**기본 요약이 초기 제약을 잃을 때**

| 구분 | 내용 |
|---|---|
| 요약 내용 | 커스텀 요약 prompt로 초기 제약 포함 요구 |
| 최근 turn 원문 유지 | 절단 지점(cut point)을 앱이 결정<br>이후 turn을 요약 block 뒤에 전송 |
| ⚠️ `keep_recent_turns` | 유지 turn 지정 파라미터 없음<br>compaction API는 beta · 시점에 따라 변함 |
| 기본 요약 신뢰 ✗ | 모든 제약 유지 보장 없음 |

<sub>근거: CCAR-F-Amey-Thakur-0033, CCAR-F-Amey-Thakur-0065, CCAR-P-jrajath94-0151, CCAR-P-jrajath94-0625</sub>

@@ NEW-SECTION
### Case facts · 구조화 상태 레이어

**정확한 값은 요약 밖 구조화 블록에**

| 증상 | 원인 | 처방 |
|---|---|---|
| 20턴 전 "15% 할인"이 "프로모션 논의됨"으로 압축 → 틀린 값 | 요약은 정확한 세부를 잃음 | 금액 · 날짜 · 주문 번호를 `case facts` 블록으로 추출<br>요약 밖 · 매 prompt에 포함 |
| 금리 · 만기 · 담보액이 "저금리 · 담보 충분"으로 → 비교표 오류 | 사실이 요약 대상 이력에만 존재 | 값 + 출처(자료 · 페이지) 기록<br>→ 사후 검증 |
| 한 달 조사 중 정확한 기준액 · SLA % · 마감일이<br>"그럭저럭 · 높은 가용성 · 근미래"로 변질 | 반복 요약에서 정확한 값이 뭉뚱그려짐 | 요약에서 수치 · 날짜 · 조건 원문 유지 필수화<br>+ 요약 대상 아닌 구조화 scratchpad |
| 30턴+ 다중 이슈 session<br>(금액 혼동 · 해결 건 재조사) | 안건별 사실이 대화에 섞임 | 안건별 번호 · 금액 · 상태를 별도 레이어에 구조화<br>매 턴 전달 |

**처방 판정**

| 처방 | 판정 | 이유 |
|---|---|---|
| `case facts` 블록 · scratchpad | ✓ | 요약된 turn 수와 무관하게 핵심 정보 유지 |
| 요약 prompt에 원문 보존 지시 | 보조 | 열화 발생원 억제<br>scratchpad와 병행 시 정답 |
| 안건 레이어에 "고객에게 전달한 내용" 기록 | ✓ | 사람 담당자 인계 요약으로 재사용 |
| 요약 임계값 상향 (70→85%) | ✗ | 문제를 뒤로 미룰 뿐 |
| 외부 저장 + "앞서 말했듯이" 감지 검색 | ✗ | 정답 = 매 prompt에 상시 포함 |
| 의도 우선 요약 · 세부 축소 | ✗ | 열화를 의도적으로 진행 |
| 안건을 하나의 요약문으로 병합 | ✗ | 구조 붕괴 |
| 해결된 안건 turn 삭제 | ✗ | 대화 일관성 상실 |
| 원시 tool 출력을 많이 두고 늦게 요약 | ✗ | 문제 지연 |

**근본 원인 판별 단서**

| 가설 | 판정 | 이유 |
|---|---|---|
| lost in the middle | ✗ | 수치가 입력에 남아 있어야 함 |
| 앞 turn 잘림 | ✗ | 잘리면 기술 자체가 사라짐 |
| 발언 · tool 결과 혼동 | ✗ | 다른 수치가 나타남 |
| 사실이 요약 이력에만 존재 | ✓ | 후반에 남은 것 = 수치 없는 모호한 요약 |

<sub>근거: CCAR-F-MyPractice-0054, CCAR-F-Udemy01-0030, CCAR-F-Udemy04-0023, CCAR-F-Udemy04-0049, CCAR-F-paullarionov-0054</sub>

@@ NEW-SECTION
### 이력 관리 방식 선택 (hybrid · retrieval)

**중요 사실 추출 + 일반 요약 + 최근 원문**

| 상황 | 정답 방향 |
|---|---|
| 78K token 요리 session<br>(알레르기 · 수량 · 선호 중요) | 하이브리드<br>중요 structured data = 추출<br>일반 논의 = 요약 · 최근 교환 = 원문 |
| 최근 25쌍만 유지 → 이전 주제 · 선호 놓침 | 오래된 메시지 요약 + 최근 메시지 원문 |
| 3개월 · 85K token 기록<br>("고립 주제 결론이 뭐였지?") | semantic embeddings로 관련 교환 on-demand 검색 |
| 단일 요리 session | 외부 저장 + semantic search<br>= architecture 과함 |

**방식별 한계**

| 방식 | 한계 |
|---|---|
| 전체 요약 | 중요한 식이 정보 등 정밀 정보 손실 위험 |
| 최근 N token만 유지<br>(rolling window) | 기록 대부분 폐기 · 중요 정보 손실 위험 |
| window 확대 (25 → 50쌍) | 같은 문제 지연 |
| vector similarity search 단독 | 현재 질의와 의미가 다른 중요 context 누락 |
| 매 턴 전체 요약 | overhead · 요약 오류 누적 |
| 점진적 summary | 구체적 결론이 추상화로 소실 |
| XML 태그로 결론 표시 | 과거 콘텐츠 전부 재구성 필요 · 검색 문제 미해결 |

<sub>근거: CCAR-F-MyPractice-0065, CCAR-F-MyPractice-0066, CCAR-F-MyPractice-0068</sub>

@@ NEW-SECTION
### 세션 이어가기 · 상태 인계

**전제 데이터 변경 시 이력 대신 판단만 인계**

| 상황 | 정답 방향 |
|---|---|
| 코퍼스 재인덱싱 · 원본 갱신 · 검토자 수정 후 재실행 | 새 session 시작<br>검증된 결과 · 판단 · 재확인 source를 구조화 요약으로 전달<br>갱신된 코퍼스로 search · analysis subagent 재실행 |
| 이력이 여전히 정확함 | continue (직전) · resume (ID 지정)<br>fork (이력 복사 후 분기) |
| 전제 변경 후 resume · fork<br>+ "옛 tool 결과 무시" 지시 | ✗ 오래된 관측을 이력째 승계<br>무시 지시로 혼입 못 막음 |
| 반복 실행 리뷰 (push마다 PR review) | 매 실행 빈 context 시작<br>→ 이전 지적을 영속화해 재실행에 전달<br>신규 · 미해결만 보고 지시 |
| 이전 지적 재확인 | 지적한 코드를 다시 검사<br>→ 남아 있는 문제만 재보고 |
| 중복 제거 vs 해결 항목 제거 | path + line 일치만으로 dedupe ✗ (미해결 은폐)<br>수동 요청 전환 ✗ (판정을 사람에게 이전) |

**이전 결과 · 결정을 후속 호출에 유지**

| 상황 | 정답 방향 |
|---|---|
| 후단 호출이 이전 subagent 지식 무시<br>(로그에 최신 지시 · 출력만 존재) | 원인 = Messages API stateless<br>요청에 포함된 내용만 모델에 보임 |
| 처방 | 관련 `messages` 배열 재전송<br>(과거 assistant 출력 · tool 결과 · 현재 user 턴)<br>또는 갱신되는 요약을 매 요청에 포함 |
| 대안 ✗ | 자동 prompt caching = 이미 보낸 prefix 처리 재사용<br>session ID 저장 + 최신 결과만 전송 = 같은 실패 |
| 초기 판단(분류체계)이 후반에 무시 | 구조화 research state file<br>(분류체계 ↔ source 매핑) → 후단 prompt에 로드 |
| 원인 | 이력이 길어 초기 판단이 tool 출력 속에 묻힘<br>(context rot: token 증가<br>→ 정확도 · recall 저하) |
| 대안 ✗ | caching · `max_tokens` 증가<br>"일반 카테고리 피하라" 지시 |

**Claude Code 장시간 session**

| 구분 | 내용 |
|---|---|
| 증상 | 이전 아키텍처 결정과 모순되는 제안 |
| 원인 | 결정이 대량 tool 출력에 묻힘 · 자동 압축으로 요약됨 |
| 대화 중에만 전달한 지시 | compaction 후 소실 가능 |
| `CLAUDE.md` (프로젝트 루트) | 항구적 설계 결정<br>`/compact` 후에도 디스크에서 재주입 |
| 구조화 facts 파일 | session 중 늘어나는 결정 · 제약<br>작업 중 참조 · 갱신 |
| 점검 질문 | "이 정보는 대화가 압축돼도 남는가?" |
| 대안 ✗ | 전문 계속 승계 · 주기적 요약<br>= 결정 보존을 대화 이력에 의존 |

<sub>근거: CCAR-F-Udemy01-0017, CCAR-F-Udemy01-0058, CCAR-F-Udemy02-0033, CCAR-F-Udemy03-0041, CCAR-F-Udemy03-0045</sub>

@@ NEW-SECTION
### Multi-agent 간 context 반환 · 인계

**반환은 구조화 발췌 · 인계는 근거까지**

| 구분 | 내용 |
|---|---|
| 위임 이유 | context 격리<br>방대한 자료는 subagent 쪽 · 정리된 결과만 상향 |
| subagent → coordinator 반환 | 인용 · 신뢰도 붙인 구조화 발췌<br>문서 전문 = subagent context · scratchpad 파일 |
| upstream 합산 155K token<br>(synthesis 최적 입력 50K 미만) | upstream agent가 구조화 데이터 반환<br>(핵심 사실 · 인용 · 관련성 점수) |
| 미전달 대상 | 장황한 페이지 내용 · 추론 기록 |
| 해결 위치 | 근본 원인 해결 = token을 출처에서 축소 |

**반환 대안 평가**

| 대안 | 이유 |
|---|---|
| coordinator에 더 큰 window · 더 큰 모델 | 실패를 미룰 뿐 · 구조 불변 |
| 오래된 메시지 말없이 폐기 | 사라질 정보 불명 |
| 분석 재실행 후 짧은 답 선택 | 구조 불변 |
| 중간 요약 agent · 순차 batch<br>vector DB 검색 tool | 출처에서 줄이는 구조화 반환이 아님 |
| subagent 1개로 축소 · 문서 첫 페이지까지 절단 | 정리된 결과 전달이 아님 |

**후속 subagent 인계**

| 구분 | 내용 |
|---|---|
| 증상 | 후속 subagent가 완료된 검색 반복<br>제외한 source의 이유 미전달 |
| 원인 | fork형이 아니면 부모 이력 없는 새 context<br>부모가 넘기는 것 = Agent tool의 prompt 문자열뿐 |
| 정답 | 탐색 성과 + 제외 이유를 출처 링크 붙은 요약으로 응축<br>각 위임 prompt에 포함 |
| 판단 기준 | 양이 필요충분 · 판단 근거 포함 |
| 대안 ✗ | 미전달 = 현상 유지<br>최종 통합까지 보류 = 다음 단계 중복 못 막음<br>전체 기록 첨부 = context 압박 · 격리 이점 상실 |

<sub>근거: CCAR-F-Amey-Thakur-0004, CCAR-F-Amey-Thakur-0043, CCAR-F-MyPractice-0014, CCAR-F-Udemy03-0020, CCAR-F-paullarionov-0014</sub>

@@ RULES

| 긴 실행 중 품질이 점진 하락 | 원인 = context 누적 · 관련 · 오래된 내용 경쟁<br>모델 버전 · temperature · tool 지연 ✗ |
| context 관리 실패의 조기 신호 | 같은 일 반복 · 앞선 결정과 모순 |
| 50턴+ 대화에서 지연 · 비용 증가 | 전체 이력이 매 요청에 포함 (stateless) |
| 짧은 대화인데 system prompt 지침 이탈 | assistant 응답 누적에 의한 희석 · drift |
| 비대한 system prompt (절차 수십 개) | 핵심만 system · 절차는 Skill · 검색 모듈 |
| context 증상 → 처방 선택 | 증거로 결함 이름 확정<br>(growth · duplication · loss ·<br>exhaustion · dilution) → 결함별 처방 |
| 매 호출 대량 로드 · 일부만 필요 | just-in-time retrieval (window 확대 ✗) |
| 전체 이력 장기 보관 의무 | 상한 있는 저장소에 전체 보관<br>active context = working set |
| compaction 후 이름 · 결정 소실 | 요약 계약(보존 항목 + 체크리스트) 수정<br>trigger 이동 ✗ |
| 기본 요약이 초기 제약 소실 + 최근 turn 원문 필요 | 커스텀 요약 prompt + 절단 지점 선택 |
| 요약 후 금액 · 날짜 · 조건 오류 | `case facts` 블록 · 구조화 scratchpad<br>요약 prompt 원문 보존 지시는 병행 |
| 다중 이슈 session 혼동 | 안건별 구조화 레이어 + tool 출력 필드 trim |
| tool 결과 중 일부 필드만 사용 | 입구에서 필요 필드만 반환<br>(wrapper · `PostToolUse` hook) |
| 오래된 tool 결과 정리 · 요약 호출 불가 | `clear_tool_uses` 적용<br>`exclude_tools`로 보존 tool 지정 |
| 고객 간 정보 오염 | 대화별 고객 1명으로 범위 한정 · 변경 시 격리 |
| subagent 반환으로 coordinator context 초과 | 인용 붙은 구조화 발췌 반환 · 원문은 subagent 쪽 |
| 후속 subagent의 중복 탐색 | 탐색 성과 · 제외 이유를 출처 포함 요약으로 위임 prompt에 |
| 반복 실행 리뷰의 중복 지적 | 이전 지적 영속화 · 재전달 + 재검사 → 신규 · 미해결만 보고 |
| 재색인 · 원본 갱신 후 재개 | 새 session + 검증된 판단 요약 + 갱신 코퍼스로 재실행 |
| 후단 호출이 이전 findings 무시 | `messages` 재전송 또는 갱신 요약 포함 |
| Claude Code 설계 결정 보호 | `CLAUDE.md` + 구조화 facts 파일 |
| 중요 사실 + 일반 대화가 섞인 긴 session | 하이브리드: 사실 추출 · 일반 요약 · 최근 원문 |
| 수개월 기록에서 특정 과거 결론 조회 | semantic embeddings 검색 |
| 입력 예산 내로 이력 전송 (모델 고정) | 대상 모델 ID로 사전 token 계산 → 초과 이력 절단 |
| window에 들어가는 단일 대형 문서 | 한 요청 전송 · `max_tokens` = 출력 상한 |

<sub>근거: CCAR-F-Amey-Thakur-0004, CCAR-F-Amey-Thakur-0032, CCAR-F-Amey-Thakur-0036, CCAR-F-Amey-Thakur-0043, CCAR-F-Amey-Thakur-0078, CCAR-F-MyPractice-0065, CCAR-F-MyPractice-0067, CCAR-F-MyPractice-0068, CCAR-F-MyPractice-0075, CCAR-F-Udemy01-0017, CCAR-F-Udemy01-0058, CCAR-F-Udemy02-0033, CCAR-F-Udemy03-0010, CCAR-F-Udemy03-0020, CCAR-F-Udemy03-0045, CCAR-F-Udemy04-0049, CCAR-F-Udemy06-0004, CCAR-F-paullarionov-0054, CCAR-P-jrajath94-0149, CCAR-P-jrajath94-0150, CCAR-P-jrajath94-0151, CCAR-P-jrajath94-0587, CCAR-P-jrajath94-0623, CCAR-P-jrajath94-0624, CCAR-P-jrajath94-0625, CCAR-P-preporato-0008</sub>

@@ TRAPS

| 더 큰 window · 더 강한 tier로 context 문제 해결 | 증가 곡선 · 희석 · 중복 불변<br>tier = 모델 계층 문제용 |
| 더 긴 system prompt로 혼동 해결 | 토큰 문제에 토큰 추가 |
| 오래된 turn을 말없이 절단 | 손실 대상 불투명 · 초기 핵심 정보 소실 |
| 매 턴 전체 이력 요약 | 호출 비용 · 요약 오류 누적 |
| trigger 임계값 조정으로 나쁜 요약 교정 | 임계값 = 시점 · 요약 내용 불변 |
| compaction 제거 | 작업 도중 window 포화 |
| 모델이 중요한 내용을 기억하리라 기대 | compaction은 설계상 손실 |
| 작업을 처음부터 재시작 | 해 둔 작업 폐기 |
| `keep_recent_turns`로 최근 turn 유지 | 해당 파라미터 없음 · 절단 지점으로 제어 |
| 요약 임계값 70% → 85% 상향 | 손실을 뒤로 미룰 뿐 |
| 외부 저장 + "앞서 말했듯이" 감지 검색 | 정답 = 매 prompt에 상시 포함되는 case facts |
| 의도 우선 요약 · 세부 축소 | 열화를 의도적으로 진행 |
| 안건을 하나의 요약문으로 병합 | 구조 붕괴 |
| 해결된 안건 turn 삭제 | 대화 일관성 상실 |
| tool 결과를 쌓은 뒤 context editing만 적용 | 대증요법 · payload 크기 원인 미해결 |
| 이전 tool 결과 전부 삭제 | 필요한 사실 손실 |
| tool 반환 건수 증가로 호출 수 감소 | 쌓이는 총량 불변 |
| 대화 앞에서부터 절단 | 초반 핵심 정보 손실 |
| 매 턴 별도 요약 요청 | 추가 모델 호출 · 요약 호출 배제 제약 위반 |
| 토큰 계산 endpoint로 이력 삭제 | 계산 도구 · 삭제는 `clear_tool_uses` |
| 응답 `usage` 필드로 사전 예산 확인 | 호출 후에 도착 |
| `effort` low로 입력 token 감소 | 입력 token 수 줄이는 수단 아님 |
| `max_tokens`를 1,000,000으로 올려 window 확보 | 출력만 제한 |
| 고객 신원에 주의하라는 지시 | 결함 = context 범위 설정 · window 크기 ✗ |
| resume · fork + "옛 결과 무시" 지시 | stale 관측 이력째 승계 · 혼입 못 막음 |
| path + line 일치만으로 dedupe | 미해결 문제까지 은폐 |
| 리뷰를 수동 요청으로 전환 | 판정 부담을 사람에게 이전 |
| prompt caching으로 이전 지식 유지 | 이미 보낸 prefix 재사용 · 미전송 보충 ✗ |
| session ID 저장 + 최신 결과만 전송 | 현재 실패 재현 |
| 전문 승계 · 주기적 요약으로 결정 보호 | 보존을 대화 이력에 의존 |
| subagent 원문 반환 후 coordinator window 확대 | 실패 지연 · 구조 불변 |
| 중간 요약 agent · 순차 batch<br>vector DB 검색 tool | 출처에서 줄이는 구조화 반환이 아님 |
| 후속 subagent 인계에 전체 기록 첨부 | context 압박 · 격리 이점 상실 |
| vector search 단독 (지속 선호 유지) | 의미가 다른 중요 context 누락 |
| 감사 요구를 JIT 검색만으로 대응 | 전체 필요 → 별도 보관 |
| 야간 요약 후 원본 삭제 | 규제 요구 증거 삭제 |
| 절차 40개를 별도 assistant로 분리 · 대문자 강조 | 라우팅 사용자 전가 · prompt 미축소 |

<sub>근거: CCAR-F-Amey-Thakur-0004, CCAR-F-Amey-Thakur-0033, CCAR-F-Amey-Thakur-0036, CCAR-F-Amey-Thakur-0043, CCAR-F-Amey-Thakur-0065, CCAR-F-MyPractice-0066, CCAR-F-Udemy01-0017, CCAR-F-Udemy01-0030, CCAR-F-Udemy01-0058, CCAR-F-Udemy02-0033, CCAR-F-Udemy02-0051, CCAR-F-Udemy03-0010, CCAR-F-Udemy03-0020, CCAR-F-Udemy03-0045, CCAR-F-Udemy04-0049, CCAR-F-paullarionov-0014, CCAR-F-paullarionov-0054, CCAR-P-jrajath94-0147, CCAR-P-jrajath94-0150, CCAR-P-jrajath94-0151, CCAR-P-jrajath94-0587, CCAR-P-jrajath94-0623, CCAR-P-jrajath94-0624, CCAR-P-jrajath94-0625, CCAR-P-preporato-0008</sub>

@@ MEMO

| Context leak 5종 | growth · duplication · loss ·<br>exhaustion · dilution<br>증상마다 처방이 다름 |
| Working set | active context에 두는 작은 집합<br>원본은 상한 있는 저장소 |
| Just-in-time retrieval | 필요한 순간 관련 부분만 로드 |
| 요약 계약 | compaction 요약이 보존할 항목 명시<br>(이름 · 결정 · 숫자 · 미해결 항목) + 체크리스트 |
| 절단 지점 (cut point) | 요약 대상과 원문 유지 turn의 경계 |
| `case facts` 블록 | 거래 사실을 요약 밖에 둔 구조화 블록<br>매 prompt에 포함 |
| Scratchpad · state file | 요약 대상 아닌 외부 기록<br>필요할 때 다시 읽어 들임 |
| continue · resume · fork | 직전 이어가기 · ID로 재개 · 이력 복사 분기 |
| ⚠️ `clear_tool_uses_20250919` | context editing 전략 (beta · 시점에 따라 변함)<br>옵션 trigger · `keep` · `exclude_tools` |
| ⚠️ `context-management-2025-06-27` | context editing beta header |
| 토큰 계산 endpoint | 전송 전 입력 token 확인 (대상 모델 ID 사용) |
| 하이브리드 이력 | 중요 사실 추출 + 일반 논의 요약 + 최근 원문 |

<sub>근거: CCAR-F-Amey-Thakur-0033, CCAR-F-MyPractice-0065, CCAR-F-Udemy01-0017, CCAR-F-Udemy01-0030, CCAR-F-Udemy03-0010, CCAR-F-Udemy04-0023, CCAR-P-jrajath94-0149, CCAR-P-jrajath94-0150, CCAR-P-jrajath94-0151, CCAR-P-jrajath94-0293, CCAR-P-jrajath94-0623, CCAR-P-jrajath94-0625</sub>

@@ CHECK

- [ ] context 문제 = 증거로 결함 확정 → 결함별 처방 (window 확대 ✗)
- [ ] 정확한 값 = `case facts` 블록 · scratchpad (요약 밖)
- [ ] compaction 손실 = 요약 계약 수정 (임계값 이동 ✗)
- [ ] 전제 데이터 변경 → 새 session + 검증된 판단만 인계

<sub>근거: CCAR-F-Udemy01-0017, CCAR-F-Udemy01-0030, CCAR-F-paullarionov-0054, CCAR-P-jrajath94-0149, CCAR-P-jrajath94-0151</sub>
