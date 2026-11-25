@@ ADD-TO: ### 1-7. Debugging: 결함 위치부터 찾기(localize)
- 변경 날짜 · 증거 → 의심 계층 결정

| 상황 | 판단 |
|---|---|
| 실패 시작일 = 특정 변경일 | 그 변경이 닿은 계층 먼저 의심<br>→ trace로 확인한 뒤 수정 |
| 변경 2건(월 prompt · 화 re-ingest)<br>하락은 화요일 시작 | 화요일 계층(index)이 첫 용의자<br>prompt = 두 번째 용의자 |
| 습관적 용의자(prompt · index · tier) | 변경 로그가 습관보다 우선<br>날짜가 계층을 지목 |
| rerank 단계 배포 후 latency 3배 | 변경된 단계가 용의자<br>모델 탓 ✗ |
| 변경 없음 · trace에 오류 없음<br>사용자 평점만 하락 | 먼저 instrument<br>증거 없이 수정 ✗ |
| 위 상황의 instrument 대상 | 사용자 결과 tracing(문제를 해결했는가)<br>사람이 라벨링한 production sampling |
| 위 상황의 한계 | instrument 동안 사용자 불편 지속<br>distribution shift(새 주제)도 확인 |
| 모델 ID pin · infra update 후 품질 하락<br>코드 불변 | pin = weight 고정<br>→ 서빙 infra가 유력 원인 |
| 위 상황의 증거 | live 지표를 update 이전 baseline과 비교<br>지표마다 model ID 기록<br>같은 기간 prompt · data 변경 확인 |

- 신호 → 지목 계층 → 조치

| 신호 | 계층 | 조치 |
|---|---|---|
| chunk 도착 · 답 틀림<br>(paraphrase 질문도 동일) | model(generation) | prompt · 모델 선택 수정<br>검증 gate 추가 |
| 위와 같음 · 환불 기간 오답 | grounding | retrieve된 구절만으로 답 · 인용 지시 강화<br>faithfulness 평가 |
| 새 prompt가 output schema 누락<br>retrieval trace 정상 | prompt | schema 복원 → 재테스트 |
| 새 prompt가 "cite your source" 제거<br>chunk 정상 · 답이 chunk 이탈 | prompt | 지시 복원 → 재테스트 |
| template가 입력을 200자로 절단<br>trace가 template 지목 | template | 전체 텍스트 전달하도록 수정<br>tier 상향 ✗ |
| 초안이 chunk에 없는 조항 인용 | verification | 초안 ↔ chunk 대조 단계 수리<br>(chunk는 정상) |
| 지난 분기 가격 인용<br>catalog는 어제 update | retrieval(index) | re-ingestion + freshness check |
| embedding 모델만 교체<br>chunk · prompt · LLM 불변 | retrieval | 새 embedding으로 retrieval eval 재실행 |
| context 조립 0.5 → 7초<br>retrieval · 추론 시간 불변 | context | retrieval 범위 지정 · compaction · 중복 제거 |

- 단계별 측정이 지연 원인 계층을 지목

| 구분 | 내용 |
|---|---|
| 방법 | 단계별 시간 측정<br>움직인 단계만 수정 대상 |
| 불변 단계 | 업그레이드 · 재구축 ✗<br>(모델 tier · index) |
| 근거 없는 원인 | network 재시도 추가 ✗<br>증거 없이 원인 지어내기 |
| 한계 | retrieval 범위 지정은 유용한 오래된 문서 누락 가능 |

- 데이터 계층 지목 = 원인 사실 + 시점 일치 두 가지

| 증상 | 지목 사실 | 무혐의 · 중립 |
|---|---|---|
| 입력 feed가 절단 텍스트 전송 | feed 절단<br>시점 = 하락 시작 | 모델 버전 불변 · latency 정상 |
| 문서 절반이 검증 안 된 mirror 출처 | 출처 변경 · re-ingest<br>시점 = 저하 시작 | chunk 정상 도착<br>모델 등급 불변 |
| index rebuild가 문서 30% 누락 | 누락 사실<br>시점 = 저하 시작 | 모델 버전 불변 · latency 양호 |
| 모델 버전이 같은 날 바뀐 경우 | 모델 결함 주장 강화 | 무관한 사실(예: 사무실 이전)은 중립 |

<sub>근거: CCAR-P-jrajath94-0194, CCAR-P-jrajath94-0195, CCAR-P-jrajath94-0196, CCAR-P-jrajath94-0197, CCAR-P-jrajath94-0310, CCAR-P-jrajath94-0314, CCAR-P-jrajath94-0368, CCAR-P-jrajath94-0369, CCAR-P-jrajath94-0431, CCAR-P-jrajath94-0432, CCAR-P-jrajath94-0557, CCAR-P-jrajath94-0558, CCAR-P-jrajath94-0670, CCAR-P-preporato-0019</sub>

@@ NEW-SECTION
### RAG 실패의 계층별 수정: retrieval · chunking · grounding
**지목된 계층의 구성 요소를 고친다**

| 증상 | 수정 | 오답 |
|---|---|---|
| 최상위 chunk = 포럼 게시물<br>사양서는 5위 | ranking에서 권위 출처 우대<br>(또는 사양 corpus로 filter)<br>source-type metadata 추가 → retrieval에서 우선 | 모델 tier 상향 ✗<br>system prompt 재작성 ✗<br>(proxy 수정) |
| 규칙 chunk만 retrieve<br>예외는 다음 문단에 있음 | 문서 구조(섹션 전체) 따라 re-chunk<br>약간의 overlap<br>→ 규칙과 예외 함께 유지 | chunk 5 → 30개 ✗(노이즈)<br>큰 모델 ✗(못 받은 문단 활용 불가)<br>"예외 기억" 지시 ✗ |
| chunk가 조항을 문장 중간에서 분할 | chunking 계층 수정 | 계층은 증상이 아니라 trace가 결정 |
| 그럴듯한 가짜 판례 인용<br>(실제 같은 이름 · 올바른 형식) | 진단 = ungrounded generation<br>(환각 하위 유형, parametric memory에서 생성) | "환각하지 말 것" 지시 ✗(검증 불가)<br>더 큰 모델 ✗<br>재시도 ✗(같은 분포 표본) |
| 위 증상의 검증 가능한 수정 | 인용이 검색된 출처로 해소되도록 요구<br>인용-출처 검증 단계<br>groundedness 지표 = 판례의 corpus 내 존재 확인 | prompt 호소 = 검증 불가 |
| 180K 문서에서 100K 이후 위치 사실 정확도 급락<br>(200K window 모델) | 광고된 context ≠ 유효 context<br>→ retrieve-then-read<br>위치 구간별 정확도 평가 | 100K로 절단 ✗(사실 삭제)<br>"끝부분 주의" prompt ✗<br>다음 모델 릴리스 대기 ✗ |
| 위 원인 | 먼 위치에서 attention 저하<br>(lost in the middle · 후반부 위치 감쇠) | window에 들어간다고 균일하게 활용 ✗ |
| retrieve-then-read 원리 | 관련 섹션을 먼저 가져옴<br>작고 집중된 context에서 추론<br>→ 균일한 신뢰도 회복 | 긴 context 모델의 알려진 특성<br>특정 릴리스의 결함 ✗ |

<sub>근거: CCAR-P-jrajath94-0028, CCAR-P-jrajath94-0032, CCAR-P-jrajath94-0310, CCAR-P-jrajath94-0495, CCAR-P-preporato-0020</sub>

@@ NEW-SECTION
### Trace 수집 범위: hop 단위 재구성과 run id
**최종 출력만으로는 실패 계층을 못 좁힘**

| 구분 | 내용 |
|---|---|
| 수집 ✓ | 출력 + tool call · 검색된 context<br>· 의사결정 지점 trace |
| 최종 출력만 · 집계 latency만<br>사용자 feedback만 | 실패를 특정 계층으로 좁힐 수 없음 ✗ |
| 감사 가능성 | 결정을 추적 · 통제를 검사할 수 있는<br>아키텍처 속성 |
| 모델 패밀리 · 비용 · 리전만 | 동작을 설명할 수 있게 되지 않음 ✗ |
| 호출별 단계 이름 + token 수 | 모델 호출을 해당 단계에 연결 |
| stop reason 횟수 | 호출이 끝난 방식 확인<br>(예: `max_tokens` 중단) |
| 합계 오류 단계 찾기 | 단계 이름 · token 수 · stop reason 로그<br>→ 모델 변경 전에 문제 단계 특정 |
| 더 큰 tier 전환 · prompt caching | 문제 단계를 가리고 비용 증가 ✗<br>caching은 단계를 기록하지 않음 |
| 고정 · 기록 | prompt · schema · 모델 버전 고정<br>출력과 함께 기록 → 비교 · 재현 |
| 일관성 오답 | 문서 순서 섞기 ✗(무관)<br>token 한도 증가 ✗(길이에만 영향)<br>2회 실행 ✗(변동성 측정일 뿐) |

| 상황 | 조치 |
|---|---|
| prompt만 로깅<br>tool call · 검색 결과 · hop 결정 없음 | hop별 tracing 추가 · request id 하나로 연결<br>(모델 호출 · 검색 · tool call · 결정)<br>hop별 token · 비용 기록 |
| 위 조치 이후 | 새 trace로 조사<br>남은 증거도 함께 보존 |
| 보존 기간 연장(7일 → 90일) | 이미 있는 것의 연장일 뿐 ✗<br>보존 = 시간, trace = 내용 |
| prompt 로그 정독 · agent 재시작 | tool 결정이 로그에 없음 ✗<br>재시작은 아무것도 알아내지 못함 ✗ |
| hop별 로그 존재 · 공통 id 없음 | 결제 tool · queue에 전파되는 run id 하나 |
| 배정 누락 · queue 이벤트 없음 | run id 전파로 end-to-end 재구성<br>누락 이벤트가 사슬의 틈으로 드러남 |
| queue가 correlation id를 drop | queue가 id를 받아서 전달 |
| run id 전파 조건 | 모든 hop(queue 포함)이 받아서 전달<br>시계 규율 · trace 저장소 필요 |
| timeout 원인이 queue인지 외부 API인지 불명 | run id 하나의 trace에 hop별 지연 시간 |
| hop 이벤트는 있으나 timing 없음 | hop별 timing 추가<br>→ 느린 hop vs 누락 hop 구분 |
| 로그 line 추가 · 큰 모델 · 두 번째 queue | 연결 없는 로그 = noise ✗<br>두 번째 queue = 손실 지점 추가 ✗ |
| 로그 추가가 맞는 예외 | 어떤 hop이 아무것도 로깅하지 않을 때 |

<sub>근거: CCAR-F-Amey-Thakur-0026, CCAR-P-Amey-Thakur-0048, CCAR-P-Amey-Thakur-0066, CCAR-P-jrajath94-0166, CCAR-P-jrajath94-0300, CCAR-P-jrajath94-0356, CCAR-P-jrajath94-0419, CCAR-P-jrajath94-0482, CCAR-P-jrajath94-0545, CCAR-P-jrajath94-0601</sub>

@@ NEW-SECTION
### Trace 비용 · 보존 · 데이터 경계
**샘플링 · skeleton · redaction으로 비용과 비밀 통제**

| 상황 | 정답 | 오답 |
|---|---|---|
| 하루 1,000만 호출<br>full trace가 모델 호출보다 비쌈 | 일부 sample = deep trace<br>나머지 = skeleton trace<br>모든 오류 = full trace 보관 | trace 안 함 · 사용자 불만 의존 ✗<br>모든 호출 full trace ✗(규모에서 비실현) |
| 위 설계의 비용 귀속 | 모든 호출에 hop별 token · 달러 기록 | 90일 full 보관 ✗<br>(skeleton이면 실패 재현 불가) |
| 위 설계의 조건 | sample은 대표성 필요<br>skeleton은 request id · 결과 포함 | full trace는 하루 1,000건 규모에서 ✓ |
| 위 설계의 한계 | sample은 드문 실패 모드 누락 가능<br>→ 전체 보관된 오류 stream 감시 | 관측은 전부 아니면 전무 ✗ |
| trace에 계좌번호 · 비밀번호 포함<br>3rd-party 분석 서비스로 전송 | trust boundary 넘기 전에 비밀 · PII redact<br>redaction을 코드로 유지 · 테스트 | tracing 중단 ✗(진단 신호 상실)<br>vendor 약속 ✗(통제 아님)<br>암호화 ✗(vendor가 복호화) |
| 위 해결의 한계 | redaction pattern 유지보수 필요<br>새 비밀 형식은 pattern 학습 전까지 유출 | 암호화 = pipe 보호<br>redaction = 이동 가능 데이터 결정 |
| prompt 텍스트는 trace에 금지<br>tool hop 찾기 필요 | 실행마다 trace 하나<br>모델 hop · tool hop마다 span<br>metadata only 모드 | span에 전체 prompt 저장 ✗<br>시간별 usage 보고서 ✗<br>하위 span 없는 단일 span ✗ |
| 데이터 규칙 = metadata만 허용<br>3개 service에 걸친 요청 실패 | metadata 전용 export<br>실패 요청의 hop별 trace 읽기 | 전체 content export 후 검색 ✗<br>custom span 형식 사전 구축 ✗ |
| ⚠️ metadata only 모드 | 해설의 설정명은 공식 monitoring 문서에서<br>확인되지 않음<br>문서상 span은 기본으로 prompt text 제외 | 문서로 재확인 |

| 구분 | 내용 |
|---|---|
| 시간별 usage 보고서 | token 합계를 모델 · workspace · key별로 묶음<br>tool 단위 상세 ✗ |
| metadata 전용 span | 식별자 · 타이밍 포함<br>→ 데이터 규칙 충족 |
| 단일 trace ID | 각 모델 hop · tool hop을 연결<br>→ 동작을 수행한 hop 식별 |

<sub>근거: CCAR-P-jrajath94-0167, CCAR-P-jrajath94-0168, CCAR-P-jrajath94-0638, CCAR-P-jrajath94-0669</sub>

@@ NEW-SECTION
### Claude Code telemetry · 비용 · 지연 관측
**요구하는 신호에 맞는 관측 수단 선택**

| 요구 | 수단 | 오답 |
|---|---|---|
| 개발자 전원의 OTLP 목적지 고정 | managed settings에 OTLP endpoint · 자격 증명 고정 | repo 설정 파일에서 telemetry 활성화 ✗ |
| 위 오답의 이유 | Claude Code는 project 설정의<br>OTel exporter 변수를 무시 | 간단해 보이는 함정 |
| MCP tool 인수를 감사 추적에 기록 | `OTEL_LOG_TOOL_DETAILS=1`<br>(MCP server 이름 · tool 이름 · 입력 인수) | `OTEL_LOG_USER_PROMPTS=1` ✗<br>(tool 인수는 TOOL_DETAILS 몫) |
| prompt 변경 후 비용 증가<br>원인 확인이 먼저 | 영향받은 각 session에서 `/usage` 실행<br>→ session별 비용 확인 | 즉시 작은 모델 전환 ✗(원인 놓침 · 품질 저하)<br>session 확인 전 dashboard 구축 ✗ |
| 비용 원인에 session 지표 사용 | `claude_code.session.count` ✗<br>= session 시작 시점의 count일 뿐 | prompt별 비용 · hop timing 아님 |
| traffic 급증을 수 초 안에 확인 | 각 live 응답의 `usage` 필드를 반환 즉시 기록 | API 분당 polling ✗ · 월간 지출 alert ✗<br>주간 비용 검토 ✗ |
| ⚠️ 집계 report 지연 | 해설: 집계는 요청보다 최대 5분 지연<br>(legacy Usage and Cost API)<br>신규 Analytics API는 보통 4시간 · 최대 24시간 | 시점에 따라 바뀜 → 문서로 재확인 |
| streaming 기능의 비용 · latency · 품질 한 대시보드 | streaming 호출 = time to first token<br>다른 호출 = 전체 응답 기준 latency | Usage API에서 latency 읽기 ✗<br>(token 수 보고, 응답 시간 아님) |
| 위 대시보드의 비용 | 완료된 작업당 비용을 품질 임계값 옆에 표시<br>Usage · Cost API 일간 합계 사용 | 경로별 percentile 20개 ✗<br>각각 별도 alert 담당자 ✗ |

<sub>근거: CCAR-P-jrajath94-0640, CCAR-P-jrajath94-0655, CCAR-P-jrajath94-0669, CCAR-P-jrajath94-0693, CCAR-P-jrajath94-0708</sub>

@@ NEW-SECTION
### Monitoring 설계: watch 대상과 drift 감지
**dashboard가 아니라 감지 · 알림 · 담당자**

| 상황 | 정답 | 오답 |
|---|---|---|
| 하루 2M 요청<br>24시간 내 hallucination drift 감지<br>전체 저장은 비용 초과 | 구조화 trace(호출당 span, token · latency 포함)<br>transcript 일부 sampling<br>샘플에 매일 자동 faithfulness 평가 | 오류 로그만 + 주간 검토 ✗(환각은 오류 안 냄)<br>latency · 비용 dashboard만 ✗<br>전부 저장 + 검토자 ✗ |
| 승인율이 2개월간 상승 drift<br>alert 없음 · 불만으로 발견 | drift detection(기준선 비교)<br>지정 담당자에게 alert<br>대표 eval data의 regression suite | 큰 모델 · 로그 추가 ✗<br>두 번째 어시스턴트 ✗ |
| 위 해결의 역할 | regression suite = drift가 품질 변화인지<br>모집단 변화인지 구분 | 필요 조건: baseline 기간 · threshold<br>한계: alert 피로 → threshold 조정 · runbook 권한 |
| 경쟁사 sale 후 전환율 하락<br>추적 watch 없음 | business outcome watch<br>(baseline · window · 담당자 · alert) | 큰 모델 ✗ · 로그 추가 ✗ |
| 위 watch의 원칙 | 시스템이 존재하는 이유인 성과가 첫 watch | system 지표만 보기 ✗ |
| 유해성 비율이 3개월 서서히 상승<br>latency · 비용만 모니터링 | 안전 지표 monitoring<br>(baseline · window · 담당자 · alert) | latency monitoring 추가 ✗ |
| 위 watch의 원칙 | 시스템의 위험이 monitoring 목록 결정 | 큰 모델 ✗ |

| 상황 | 정답 | 오답 |
|---|---|---|
| dashboard 6주 녹색<br>설문 = 한 달 전부터 악화<br>suite 4개월 불변 · 주제 이동 | suite가 stale → 담당자 호출 · suite 갱신<br>새 제품 line case 추가 · baseline 재설정<br>녹색이 drift를 놓친 이유 post-mortem | 녹색 = 정상 ✗<br>설문 영향력 낮추기 ✗(suite가 놓친 신호) |
| 위 상황의 모델 튜닝 | suite 갱신으로 model 계층 결함이 확인된 뒤에만 ✓ | 지금 튜닝 ✗(사각지대 남음) |
| 위 해결의 조건 · 한계 | 새 line case 라벨링 필요<br>갱신에는 labeling 비용<br>suite review를 달력에 일정화 | stale을 사용자가 발견하게 둠 ✗ |
| 장애는 분 단위, drift는 주 단위 | 빠른 line + 느린 line 짝<br>빠른: 오류율 · traffic 분 단위 alert<br>느린: 사람 라벨 sample 성공률 주 단위 추세 | 일일 평균 1개 ✗(장애 하루 지연)<br>일일 평균 10개 ✗(여전히 일 단위)<br>실패마다 alert ✗(alert 피로) |
| 위 설계의 한계 | 두 threshold · 두 담당자 필요<br>느린 line label은 지속 비용 | 일일 평균은 위험도 낮은 제품에서만 ✓ |
| claims assistant 요구<br>성공률 95% 하한 · p95 2초<br>월 비용 예산 · 규제 감사 | 단계별 지표 계측(모델 · retrieval · tool · 의존성)<br>담당자가 대표성을 유지하는 eval suite<br>변경마다 regression suite + 하락 시 page | 월 1회 수동 dashboard 검토 ✗<br>latency만 alert ✗<br>비용 아끼려 trace 미보관 ✗ |
| 위 오답의 이유 | 수동 검토 = 품질 하락을 42일 뒤 발견<br>압박 시 가장 먼저 버려짐 | latency만 = 품질 · 비용은 조용히 drift<br>trace 없으면 "any decision" 감사 불가 |
| 위 설계의 조건 | 단계별 지표 = request id 필요<br>page = threshold 필요 | suite 대표성 유지 예산 없으면 썩음 |
| 모델 · prompt 불변인데 같은 질문에 수치 불일치<br>새 모델 없이 ungrounded 답 flag | 같은 prompt를 여러 번 실행<br>핵심 수치가 다른 답변 표시 | 큰 tier ✗<br>Messages API 일관성 flag ✗(문서에 없음) |
| 위 검사의 의미 | 핵심 수치 불일치 = hallucination 가능성 | 새 모델 불필요 |

<sub>근거: CCAR-P-jrajath94-0006, CCAR-P-jrajath94-0202, CCAR-P-jrajath94-0203, CCAR-P-jrajath94-0206, CCAR-P-jrajath94-0312, CCAR-P-jrajath94-0498, CCAR-P-jrajath94-0561, CCAR-P-jrajath94-0663</sub>

@@ NEW-SECTION
### Alert 운영: 담당자 · runbook · 위생
**담당자 없는 alert = monitoring 아님**

| 상황 | 조치 | 오답 |
|---|---|---|
| 품질 alert 지난달 3회 발동<br>담당자 없음 · chat thread 논의 후 망각 | 먼저 담당자 지정<br>(튜닝 · 대응 · 폐기 책임 1명) | threshold 조정 ✗(유지할 사람 없음)<br>alert 추가 ✗(noise 증가)<br>alert 끄기 ✗(유일한 신호 상실) |
| 위 조치의 조건 · 한계 | 담당자에게 튜닝 권한 · 대응 시간 필요<br>1명은 병목 → 대리인 · 순환 근무 | 담당자 없는 instrument = dashboard일 뿐 |
| precision 6주 하락<br>아무도 dashboard를 안 봄 | 지정 담당자에게 가는 precision alert<br>대응 runbook | 더 좋은 · 더 많은 dashboard ✗<br>큰 모델 ✗ |
| 위 조치의 원리 | 보는 사람 없는 dashboard = 가구<br>행동하려면 runbook 필요 | 지표가 없을 때만 dashboard 개선 ✓ |
| latency alert가 매주 월요일 발동<br>배치 작업이 수치 왜곡 · 2개월 무시 | alert 재튜닝 또는 폐기<br>배치 시간대 제외 · 업무 시간 traffic으로 이동 | 유지 ✗(무시되는 alert = coverage 아님)<br>더 크게 page ✗<br>threshold 낮춤 ✗(같은 거짓 원인) |
| 위 조치의 원리 | 매주 발동하며 조치 없음 = 잘못된 line<br>조용하고 신뢰받는 채널 > 시끄럽고 무시되는 채널 | alert 많음 = 안전 많음 ✗ |
| 위 조치의 한계 | 배치 시간대에 실제 인시던트 가능<br>→ 제외 자체를 별도 검토 | 발동이 실제였다면 line이 아니라 대응 수정 |
| 음성 봇 p95 2초 미만 threshold<br>책임지는 사람 없음 | 요구사항 체인의 빠진 고리 = 책임자<br>(요구사항 → 지표 → 임계값 → 책임자) | "팀"은 지정된 책임자 아님<br>체인이 갖춰졌다고 답 ✗ |
| 위 상황의 위험 | 책임자 없으면 traffic 구성 변경 시<br>임계값이 표류 | 정답이 되는 경우: 지정 역할이 소유 + 정기 검토 |

<sub>근거: CCAR-P-jrajath94-0204, CCAR-P-jrajath94-0205, CCAR-P-jrajath94-0372, CCAR-P-jrajath94-0490</sub>

@@ RULES
| 실패 시작일에 변경이 2건 | 시작일과 일치하는 계층 먼저 의심 → trace로 확인<br>prompt는 두 번째 용의자 |
| trace가 한 계층을 지목 | 그 계층을 가장 작은 수정으로 고침<br>tier 상향은 대리 수정 ✗ |
| chunk 도착 · 답 틀림 | model · prompt 계층<br>grounding · 인용 지시 · 검증 gate<br>faithfulness 평가 |
| 답이 chunk에 없는 내용 인용 | verification 계층 수리<br>인용 ↔ 출처 대조 · groundedness 지표 |
| 오래된 사실 인용 | index 계층<br>re-ingestion + freshness check |
| 규칙과 예외가 다른 chunk로 분리 | 문서 구조 단위로 overlap 두고 re-chunk |
| 최상위 chunk가 비권위 출처 | ranking · source-type metadata로 권위 출처 우대 |
| 긴 context 위치별 정확도 저하 | retrieve-then-read<br>위치 구간별 정확도 평가 |
| trace 어디에도 오류 없음 · 사용자 평점 하락 | 먼저 instrument(결과 tracing · 라벨 sampling)<br>증거 없이 수정 ✗ |
| 어느 hop에서 사라졌는지 불명 | 모든 hop에 run id 전파 + hop별 timing |
| 대규모에서 trace 비용이 호출 비용 초과 | deep sample + skeleton + 전체 오류 trace<br>모든 호출에 hop별 token · 달러 |
| trace가 3rd-party로 나감 | trust boundary 전에 redact(코드로 유지 · 테스트) |
| 환각 drift를 24시간 내 감지 · 전체 저장 불가 | 구조화 trace + sampling<br>매일 자동 faithfulness 평가 |
| 장애는 분 단위 · drift는 주 단위 | 빠른 line + 느린 line 짝 |
| dashboard 녹색인데 사용자는 악화 | suite stale 의심 → 담당자 호출<br>suite 갱신 · baseline 재설정 |
| 지표는 있는데 아무도 안 봄 | 지정 담당자 + runbook이 있는 alert |
| 매주 발동하는 무조치 alert | 재튜닝 또는 폐기 |
| 성과 · 안전 지표 watch 없음 | watch 추가<br>(baseline · window · 담당자 · alert) |
| 전원 OTLP 목적지 고정 | managed settings에 고정<br>project 설정은 무시됨 |
| MCP tool 인수를 감사 추적에 기록 | `OTEL_LOG_TOOL_DETAILS=1` |
| 수 초 내 spend · traffic 급증 확인 | 응답별 `usage` 필드 기록<br>집계 report는 지연 |
| pin한 model ID · infra update 후 품질 하락 | update 이전 baseline과 비교 + model ID 기록<br>같은 기간 prompt · data 변경 확인 |
<sub>근거: CCAR-P-jrajath94-0006, CCAR-P-jrajath94-0028, CCAR-P-jrajath94-0032, CCAR-P-jrajath94-0167, CCAR-P-jrajath94-0168, CCAR-P-jrajath94-0194, CCAR-P-jrajath94-0195, CCAR-P-jrajath94-0196, CCAR-P-jrajath94-0197, CCAR-P-jrajath94-0202, CCAR-P-jrajath94-0203, CCAR-P-jrajath94-0204, CCAR-P-jrajath94-0205, CCAR-P-jrajath94-0300, CCAR-P-jrajath94-0310, CCAR-P-jrajath94-0372, CCAR-P-jrajath94-0495, CCAR-P-jrajath94-0498, CCAR-P-jrajath94-0561, CCAR-P-jrajath94-0640, CCAR-P-jrajath94-0670, CCAR-P-jrajath94-0693, CCAR-P-preporato-0019, CCAR-P-preporato-0020</sub>

@@ TRAPS
| 지목되지 않은 계층에 대리 수정<br>(tier 상향 · index 재구축 · prompt 재작성) | 비용만 증가 · 지목 계층은 그대로<br>깨진 chunk · 잘린 text는 큰 tier도 동일 |
| 더 큰 tier로 잘린 입력 해결 | 모든 tier에 세부 정보 없음 |
| 추론 추가 · 잘린 형식용 학습 data 수집 | 잃은 세부 정보 복구 ✗<br>형식이 bug, data는 bug 아님 |
| 흔한 용의자(prompt)부터 의심 | 변경 로그가 습관보다 우선 |
| 하락 원인을 "질문이 어려워졌다"로 돌림 | 증거 없음 · 변경 로그가 증거 |
| 증거 없이 prompt 재작성 · index 재구축 | 추측 · layer 추측이 가장 비싼 느림 |
| "환각하지 말 것" prompt · 큰 모델 · 재시도 | 검증 불가 · parametric 환각 지속 · 같은 분포 표본 |
| 100K 절단 · "끝부분 주의" prompt · 릴리스 대기 | 사실 삭제 · attention 감쇠는 prompt로 불가 · 알려진 특성 |
| chunk 수만 5 → 30 | 노이즈 증가 · 빠진 문단 보장 ✗ |
| 보존 기간 연장 · prompt 로그 정독 · 재시작 | 없는 hop은 생기지 않음 · 조사 진전 없음 |
| hop 로그 양만 증가 · 두 번째 queue | 연결 없는 로그 = noise · 손실 지점 증가 |
| trace 전부 안 함 · 불만에 의존 | 불만은 monitoring 아님 |
| 모든 호출 full trace · 90일 full 보관만 | 규모에서 비실현 · skeleton은 재현 불가 |
| 암호화로 비밀 보호 · vendor 약속 | vendor가 복호화 · 약속은 통제 아님 |
| tracing 완전 중단 | 진단 신호 상실 |
| 전체 content export 후 prompt 검색 | metadata만 허용하는 data 규칙 위반 |
| 시간별 usage 보고서로 hop 추적<br>`claude_code.session.count`로 hop 추적 | token 합계 · session 시작 count일 뿐 |
| Usage API로 latency 읽기<br>분당 polling으로 초 단위 감지 | token 수 보고 · 집계는 요청보다 지연 |
| project 설정에서 OTel 활성화<br>`OTEL_LOG_USER_PROMPTS`로 tool 인수 | project 설정 무시 · tool 인수는 TOOL_DETAILS |
| 오류 로그만 + 주간 검토 | 환각은 오류를 거의 안 냄 · 24시간 기준 miss |
| latency · 비용 dashboard만 | 답변 품질 무관 |
| dashboard 녹색 = 정상 · 설문 영향력 낮추기 | 녹색 = suite 통과일 뿐 · 설문은 suite가 놓친 신호 |
| 일일 평균 1개 · 10개 · 실패마다 alert | 장애 하루 지연 · 여전히 일 단위 · alert 피로 |
| 담당자 없이 threshold 조정 · alert 추가 · alert 끄기 | 유지할 사람 없음 · noise 증가 · 유일한 신호 상실 |
| 무시되는 alert 유지 · 더 크게 page<br>threshold 낮춤 | 같은 거짓 원인으로 더 자주 발동 |
| 더 좋은 · 더 많은 dashboard | 보는 사람이 없음 |
| infra 동결 · 지표 비교 전 prompt 재작성 · grader 재학습 | 증거 확보 전 변경 |
| Messages API 일관성 flag로 근거 없는 답 차단 | 해당 flag는 문서에 없음 |
| 월 1회 수동 dashboard 검토<br>latency만 alert · trace 미보관 | 42일 뒤 발견 · 품질 · 비용은 조용히 drift · 감사 불가 |
| 문서 순서 섞기 · token 한도 증가 · 2회 실행 | 일관성과 무관 · 길이에만 영향 · 변동성 측정일 뿐 |
<sub>근거: CCAR-F-Amey-Thakur-0026, CCAR-P-jrajath94-0006, CCAR-P-jrajath94-0028, CCAR-P-jrajath94-0032, CCAR-P-jrajath94-0166, CCAR-P-jrajath94-0167, CCAR-P-jrajath94-0168, CCAR-P-jrajath94-0194, CCAR-P-jrajath94-0195, CCAR-P-jrajath94-0197, CCAR-P-jrajath94-0202, CCAR-P-jrajath94-0203, CCAR-P-jrajath94-0204, CCAR-P-jrajath94-0205, CCAR-P-jrajath94-0206, CCAR-P-jrajath94-0300, CCAR-P-jrajath94-0310, CCAR-P-jrajath94-0314, CCAR-P-jrajath94-0372, CCAR-P-jrajath94-0638, CCAR-P-jrajath94-0640, CCAR-P-jrajath94-0655, CCAR-P-jrajath94-0663, CCAR-P-jrajath94-0669, CCAR-P-jrajath94-0670, CCAR-P-jrajath94-0693, CCAR-P-jrajath94-0708, CCAR-P-preporato-0020</sub>

@@ MEMO
| run id (correlation id) | 모든 hop에 전파되는 식별자<br>흩어진 hop 이벤트를 하나의 실행으로 연결 |
| hop별 timing | 느린 hop vs 누락 hop 구분 |
| skeleton trace | request id · 결과만 담은 경량 trace<br>deep sample · 전체 오류 trace와 짝 |
| metadata only export | prompt text 제외 · 식별자 · 타이밍 유지 |
| redaction | trust boundary 전에 비밀 · PII 제거<br>코드로 유지 · 테스트 |
| 변경 날짜 규칙 | 실패가 변경일에 시작 → 그 계층 먼저 의심 |
| 요구사항 → 지표 → 임계값 → 책임자 | 요구사항 체인<br>책임자 누락 시 임계값 표류 |
| 빠른 line · 느린 line | 장애(분 단위) · drift(주 단위) 짝 설계 |
| `OTEL_LOG_TOOL_DETAILS` | tool 입력 · MCP server · tool 이름 기록 |
| `OTEL_LOG_USER_PROMPTS` | user prompt 내용 로깅 |
| `claude_code.session.count` | session 시작 시 count |
| `/usage` | 현재 session 비용 확인 |
| 응답의 `usage` 필드 | 호출 완료 즉시 token 보고 |
| time to first token | streaming 호출의 핵심 latency |
| effective context vs advertised context | window에 들어가도 균일하게 활용 ✗ |
| retrieve-then-read | 관련 섹션 먼저 → 작은 context에서 추론 |
| groundedness 지표 | 인용 · 판례가 corpus에 존재하는지 확인 |
<sub>근거: CCAR-P-jrajath94-0028, CCAR-P-jrajath94-0032, CCAR-P-jrajath94-0167, CCAR-P-jrajath94-0168, CCAR-P-jrajath94-0194, CCAR-P-jrajath94-0203, CCAR-P-jrajath94-0300, CCAR-P-jrajath94-0356, CCAR-P-jrajath94-0490, CCAR-P-jrajath94-0545, CCAR-P-jrajath94-0638, CCAR-P-jrajath94-0640, CCAR-P-jrajath94-0655, CCAR-P-jrajath94-0669, CCAR-P-jrajath94-0693, CCAR-P-jrajath94-0708</sub>

@@ CHECK
- [ ] 실패 시작일 변경 계층 먼저 → trace 확인 → 수정
- [ ] chunk 도착 · 답 틀림 → model · prompt 계층
- [ ] hop 연결 = run id 전파 · 로그 양 ✗
- [ ] alert = 담당자 + runbook · 무조치 alert 폐기
<sub>근거: CCAR-P-jrajath94-0194, CCAR-P-jrajath94-0204, CCAR-P-jrajath94-0205, CCAR-P-jrajath94-0310, CCAR-P-jrajath94-0419</sub>
