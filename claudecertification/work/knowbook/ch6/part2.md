@@ ADD-TO: ### 1.4 출력 형식 지정
| 변환 규칙을 한 문장 지시로만 전달 | ✗ | 항목 내용 · 순서가 해석에 맡겨짐<br>→ 출력 편차 |
| 대표 입력 + edge case의 이상적 출력 예시 | ✓ | 형식 · 톤 · 구조 안정<br>(가장 확실한 수단 중 하나) |
| 필수 요소 · 배열 순서를 정의한 템플릿 | ✓ | 한 항목에 넣을 것 · 순서 고정 |
| 내용 유형별 표현 분리<br>(재무 = 표 · 뉴스 = 문장 · 기술 조사 = 구조화 리스트) | ✓ | 성질이 다른 내용에 맞는 표현 대응 |
| 모든 내용을 같은 글머리 기호로 변환 | ✗ | 수치 비교 · 뉴스 흐름 파악 불가 |
| 통합 subagent가 결과에 내용 유형 라벨 부여<br>(재무 · 뉴스 · 기술) | ✓ | 보고서 생성 측 표현 전환 확실 |

<sub>근거: CCAR-F-Udemy01-0046, CCAR-F-Udemy04-0032</sub>

@@ ADD-TO: ### 1.5 Structured outputs, tool 강제, prefill 폐지
| schema 선언 = 계약 | 구조가 요청이 아니라 계약의 일부<br>수신 시 validation → 계약 준수 확인<br>prompt 요청 · 사후 수정 · temperature → 우연에 맡김 |
| 확정적 보장 2계층 | 생성 제약(structured outputs)<br>+ 하위 시스템 전달 전 코드 validator<br>validator schema = 하위 시스템 schema와 일치 |
| schema 버전 관리 | schema를 하위 시스템과 함께 버전 관리<br>schema drift → validator 파손 |
| 확정 보장이 아닌 것 | prompt 속 형태 지침 → 샘플링으로 형태 깨짐<br>temperature 상향 → 변동 증가<br>문서화 → 통제 아님 |
| `output_config.format` schema | 응답 형태 제한 → 형태 오류용 재시도 루프 대부분 불필요<br>텍스트 파싱 전 `stop_reason` 확인 유지<br>"JSON만 요청" prompt → 텍스트 제한 ✗ |
| 스키마 위반 근원 해결 | constrained decoding으로 위반 제거<br>semantic 검사 · `stop_reason` 처리 = 별도 필요<br>retry · 지시 → 줄일 뿐 없애지 못함 |
| regex 복구 | 의도 추측 → 데이터 조용히 손상 |
| forced tool use 거부 모델<br>(Claude Opus 5.5) | 이름 지정 `tool_choice` → 400 error<br>`tool_choice` `auto` + strict tool use<br>또는 enum 포함 structured outputs → 라벨 1개 |
| forced tool use 지원 여부 | ⚠️ 모델 버전별로 상이<br>공식 `tool_choice` 문서의 모델별 표에서 재확인 |
| prefill 제거 후 형식 유지 | system prompt 지시로 출력 형식 유지<br>thinking 끄기 ✗ → prefill은 계속 400<br>⚠️ 4.6 이후 모델 기준 · 버전에 따라 바뀜 |

<sub>근거: CCAR-F-Amey-Thakur-0023, CCAR-F-Amey-Thakur-0058, CCAR-P-jrajath94-0139, CCAR-P-jrajath94-0618, CCAR-P-jrajath94-0621, CCAR-P-jrajath94-0622, CCAR-P-preporato-0009</sub>

@@ NEW-SECTION
### Schema 설계: nullable · enum · 출처 필드
**schema는 현실 반영 · 없음은 null · 미분류는 other**

**필드 유형별 설계**

| 설계 | 판정 | 이유 |
|---|---|---|
| 원본에 없을 수 있는 필드 = nullable | ✓ | 진짜 없음 vs 추출 실패 구분 |
| 조건부로 필요한 항목 = nullable + 후단 검증 | ✓ | schema는 현실 반영 · 조건은 코드로 |
| 전부 required | ✗ | 정상 문서에서도 값 날조 · 추출 실패 |
| 전부 optional | ✗ | 진짜 놓친 경우 감지 불가 |
| 값 없음을 말없이 생략 | ✗ | 없음 vs 실패 구분 불가 |
| 그럴듯한 기본값 | ✗ | 데이터 날조 · 오염 |
| 빈 문자열 | ✗ | 값 없음 vs 빈 값 구별 불가 |
| 메모 필드에 사유 기록 | ✗ | 기계가 읽을 수 있는 상태 아님 |

**값 날조의 원인 진단**

| 구분 | 내용 |
|---|---|
| 증상 | 필수 필드를 채우려고 없는 값 출력<br>(예: 존재하지 않는 종료일 `2099-12-31`) |
| 원인 | prompt 아님 · schema 설계 |
| 해결 | 해당 필드 nullable |
| 조합 | 별도 필드(자동 갱신 여부) + null 종료일<br>→ 하위 시스템이 계약 종류 판단 |
| 운영 | null 건수를 문서 종류별 집계<br>→ 값이 있어야 할 문서의 null 여부 점검 |

**결측 표기 일관성**

| 상황 | 정답 |
|---|---|
| 결측이 null · `""` · `"N/A"` · 필드 생략으로 혼재<br>문장 규칙 추가 후에도 지속 | 예시 3~5개 (relevant · diverse · 태그 구조)<br>+ schema로 결측 = null만 허용<br>→ 나머지 표기는 검증에서 탈락 |

**enum 분류 설계**

| 구분 | 내용 |
|---|---|
| 닫힌 enum의 한계 | 목록 밖 입력 → 가까운 값으로 억지 분류<br>또는 범위 밖 값 생성 → 하류 validation 실패 |
| structured outputs와 enum | 값 범위는 보장 · 분류 정확성은 보장 ✗ |
| `other` + 상세 문자열 필드 | 해당 없음을 그대로 표현 · 내용 보존 |
| `unclear` 값 | 판단 불가 수용 → 사람 리뷰로 전달 |
| 운영 | `other` 출현 모니터링<br>→ 정착된 유형을 정식 값으로 승격<br>(새 유형이 계속 늘어나는 조건) |

**출처 필드**

| 구분 | 내용 |
|---|---|
| 값마다 원본 위치 기록 필요 | 출처 필드를 schema에 선언 |
| 근거 | 출력에 담을 정보 = 선언한 형태 안에 있어야 함<br>필드 요구 시 두 번째 pass 불필요 |

<sub>근거: CCAR-F-Amey-Thakur-0008, CCAR-F-Amey-Thakur-0025, CCAR-F-Amey-Thakur-0048, CCAR-F-Amey-Thakur-0059, CCAR-F-Amey-Thakur-0074, CCAR-F-Udemy01-0042, CCAR-F-Udemy03-0018, CCAR-F-Udemy04-0006, CCAR-F-Udemy05-0037</sub>

@@ NEW-SECTION
### Validation 실패 처리: 의미 검증 · 재요청 설계
**schema = 구조 보장 · 의미 오류는 구체 오류로 재요청**

**구조 오류 vs 의미 오류**

| 구분 | 예 | 대응 |
|---|---|---|
| 구조 오류 | JSON 구문 오류 · 타입 · 필수 항목 | schema 선언 · structured outputs<br>· `strict`로 제거 |
| 의미 오류 | 값이 엉뚱한 필드에 입력 · 합계 불일치<br>존재하지 않는 행 번호 · 잘못된 페이지 번호<br>인용 원문 누락 | schema 밖 검증 코드 |
| 업무 규칙 위반 | 변경 없는 파일 지적 · 정책 위반 지적<br>상품 크레딧이 `shipping_refund`에 입력 | 실행 전 업무 규칙 검증<br>→ 위반 내용을 구체적으로 반환 |
| 오배치 예방 | 취합 착오가 나는 필드 | 필드 `description` 구체화 + 검증 코드 |

| 구분 | 내용 |
|---|---|
| 판별 기준 | 실패가 형식 오류인가 의미 오류인가<br>→ 대응 선택의 출발점 |
| 파싱 가능 · 필수 필드 충족 · 타입 일치 | 형식의 올바름 ≠ 업무상 올바름 |
| 구문 오류가 이미 사라진 상태 | 남은 오류 = 의미 문제<br>`strict: true` · `tool_choice` 강제<br>→ 효과 없음 |
| 효과 확인 | 불일치 건수를 필드별 집계 |

**재시도 요청 구성**

| 재료 | 역할 |
|---|---|
| 원본 문서 | 올바른 값 대조 (날짜 교정 · 소스에 없는 handler 이름 확인) |
| 거부된 JSON | 고칠 대상 |
| validator의 구체 오류 | 무엇이 틀렸는지<br>(필드 누락 · 잘못된 enum · 소스에 없는 값은 성격이 다름) |
| XML 태그 구분 | 지시 · 문맥 · 입력 혼동 방지 |
| 응답 지시 | 수정이 끝난 데이터만 반환 |
| 성공 조건 | 모델이 오류를 고칠 증거를 손에 쥐었는가 |

**업무 규칙 거부 시 tool 호출 처리**

| 구분 | 내용 |
|---|---|
| 상황 | tool 입력이 schema에 맞는데 애플리케이션 규칙이 거부 |
| 반환 | `tool_result` + `is_error: true`<br>+ 구체적 이유 |
| 이력 | 주고받음을 대화 이력에 남긴 채 다음 요청 |
| 메시지 내용 | 무슨 일이 일어났는지 · 다음에 시도할 것 |
| 둘 중 하나 누락 | 수정 재료가 Claude에 전달되지 않음 |

**retry가 통하는 경우 vs 안 통하는 경우**

| 상황 | 효과 | 대응 |
|---|---|---|
| 정보는 입력에 있고 표기만 다름<br>(예: 날짜 ISO 8601 변환) | 있음 | 검증 오류 붙여 재요청 |
| 정보가 입력에 없음<br>(별도 파일에만 존재) | 없음 | 누락 원본 제공<br>→ 그래도 없으면 null · "이용 불가" 허용 |
| 소스 자체가 모순<br>(증명서 합계 전기 오류) | 없음 | `stated_total` · `calculated_total`<br>모두 추출 + `conflict_detected`<br>→ 사람에게 |
| 재시도 N회에도 해소 0건 | 없음 | 입력에 정보 없다는 신호 |

| 구분 | 내용 |
|---|---|
| 검증 실패 지속 시 첫 점검 | 모델이 필요한 정보를 가졌는가<br>(prompt · schema 수정보다 먼저) |
| 원인 분리 | 입력 측 문제 vs 출력 측 문제 구분 |
| 재시도 · strict · few-shot | 없는 정보를 모델이 채우게 하는 방향 |
| 필수 충족용 날조 방지 | 원본에 없을 수 있는 필드 = null 허용 |
| 운영 | 오류 종류별 재시도 성공률 기록<br>→ 안 고쳐지는 오류 조기 식별 |
| 운영 | 재시도 후 남은 불일치를 공급자별 집계<br>→ 개선 요청에 활용 |

**validation 운영 원칙**

| 구분 | 내용 |
|---|---|
| 신뢰성 패턴 | schema 강제 + validation-retry loop |
| 경계 validation | 결함이 하류로 퍼지기 전 차단<br>비용 절감 · 모델 정확도 향상 아님 |
| 드문 실패<br>(수백 호출에 1회) | 정해진 처리 경로 필요<br>막을 것 = 잘못된 데이터의 조용한 통과 |
| 검증 loop 3요소 | 검출 · 수정 단서(구체 오류 + 원본) · 최종 수용처 |
| 최종 수용처 | 재시도로 해소되지 않는 건 → 사람 검토 |

**`stop_reason`과 값 정확성**

| 구분 | 내용 |
|---|---|
| `stop_reason: "max_tokens"` | 응답이 상한에서 끊김<br>structured outputs의 schema 준수 보장 ✗ |
| 대응 | `max_tokens` 상향 후 재시도<br>또는 요청을 작게 분할 → 중단 자체 감소 |
| 값 정확성 | schema 보장 = 구조 · 타입까지<br>행 번호 등은 참조 대상과 대조 → 구체 오류 반환 |
| `pause_turn` | 서버 tool loop 일시 정지 · 이 문제와 무관 |
| 원칙 | 구조 검증과 의미 검증 = 별개 수단 |

<sub>근거: CCAR-F-Amey-Thakur-0049, CCAR-F-Amey-Thakur-0072, CCAR-F-Amey-Thakur-0073, CCAR-F-Udemy01-0023, CCAR-F-Udemy01-0025, CCAR-F-Udemy01-0032, CCAR-F-Udemy02-0018, CCAR-F-Udemy02-0026, CCAR-F-Udemy03-0048, CCAR-F-Udemy04-0033, CCAR-F-Udemy04-0045, CCAR-F-Udemy05-0003, CCAR-F-Udemy05-0032, CCAR-F-Udemy06-0020, CCAR-F-preporato-0026</sub>

@@ NEW-SECTION
### Multi-pass 리뷰 · 독립 리뷰어
**리뷰는 생성과 분리 · 큰 입력은 국소 + 통합 pass**

**자기 리뷰의 한계와 독립 리뷰**

| 구분 | 내용 |
|---|---|
| 같은 session 자기 리뷰 | 생성 시 추론 · 전제를 그대로 보유<br>→ 경우를 고려하고도 자기 방식이 맞다고 결론<br>= 확증 편향 |
| 독립 리뷰 instance | 생성자의 추론에 접근 ✗ → 확증 편향 회피<br>근본 원인 직접 해결<br>= 사람 동료 리뷰의 fresh eyes |
| 독립성 조건 | 별도 instance + 생성 시 추론 · 대화 기록 미전달<br>둘 다 충족 필요 |
| 리뷰 입력 | diff · 요구사항 명세 · 리뷰 기준만<br>→ 입력 한정 템플릿을 pipeline에 고정 |
| Writer/Reviewer 패턴 | 한 session 작성 · 다른 session 리뷰<br>새 context = 직전 코드에 대한 편향 없음 |
| 판별 기준 | 리뷰하는 쪽이 만든 쪽의 사고 과정에서 분리됐는가 |
| extended thinking 예산을 늘려도 불변 | 원인 = 사고 깊이 아닌 context 공유 |
| 같은 대화 안 "직전 결과 확인" follow-up | 검증이 느슨해짐<br>→ 별도 API 호출에 원본 · 결과 · 판정 기준 전달 |

**리뷰 기준과 결과 게시**

| 구분 | 내용 |
|---|---|
| 리뷰 기준 | `CLAUDE.md`로 제공 |
| 보고 범위 | 올바름 · 요건 문제만 보고<br>→ 세세한 취향 지적(과잉 수정) 방지 |
| 결과 게시 | `--output-format json`<br>+ `--json-schema`로 구조화<br>→ PR 코멘트 게시 · 사람 확인 용이 |

**자기 비평 단계 (evaluator-optimizer)**

| 구분 | 내용 |
|---|---|
| 적합한 문제 | 정답은 맞는데 설명 완전성이 케이스마다 들쭉날쭉<br>(정책 · 일정 · 다음 절차 누락) · 사람 감독 추가 ✗ |
| 설계 | 초안 내기 전 구체 기준에 비추어 자기 평가 |
| 패턴 | 생성 → 기준 평가 → 피드백 반영<br>(한 LLM 생성 · 다른 LLM 평가 형태도 있음) |

**큰 입력을 나누는 pass 설계**

| 상황 | 설계 |
|---|---|
| 대형 PR(14~42개 파일) single-pass<br>→ 깊이 편차 · 뻔한 버그 누락 · 모순 피드백 | 원인 = attention dilution (context rot)<br>→ 파일별 집중 pass로 같은 깊이 확보 |
| 파일 간 문제<br>(의존성 · 데이터 흐름 · 필드명 변경 미반영) | 별도 통합 pass<br>입력 = 파일별 결과 + 변경된 interface 목록 |
| 설계 원칙 | 국소 pass + 횡단 통합 pass 둘 다 필요<br>한쪽만 있으면 다른 쪽 결함 누락 |
| 자유도 높은 조사 처리 회피 요건 | 분할 · 통합 모두 고정 절차 workflow<br>= 자율 agent와의 차이 |
| prompt chaining | 고정 단계 · 단계 출력을 다음에 전달<br>단계가 단순 → 정확도 상승<br>중간 gate · 기록 · 채점 가능 |
| 섹션 구조를 예측할 수 있는 긴 문서<br>(60쪽 대출 신청 패키지) | 섹션별 추출 → 통합 후 대조 pass<br>(중복 entity · 합계 불일치 · 관계 오류) |
| source 묶음 속 근거 없는 주장 · 모순<br>(같은 출처를 지지 · 반박 양쪽에 사용) | claim–source 쌍마다 독립 리뷰 pass<br>→ 통합 pass에서 모순 · 누락 확인 |
| 검증 위임 시 | 주장 + 대조할 출처 발췌를 함께 전달 |
| 생성 전 기록 · 채점할 checkpoint 요구 | 출처 단위 리뷰 chain + 최종 통합<br>→ 단계별 산출물이 남음 |
| 분해 방식 판단 | 입력 구조를 사전에 아는가<br>결함이 어느 단계에서 생기는가 |

**확신도 · 심각도 routing**

| 구분 | 내용 |
|---|---|
| 포괄적 1차 분석 + 전부 같은 우선순위 | 포괄성 유지 + 별도 검증 pass<br>출력 schema = confidence<br>· severity · evidence |
| 대응 규칙 | confidence × severity 조합 → 경로 매핑<br>(자동 해결 · 사람 리뷰 · 추세 분석) |
| 확신도 출처 | 모델 자기 신고 값 · API 응답에 없는 값 |
| 캘리브레이션 | 정답 라벨 데이터로 확신도–결과 관계 측정<br>→ 임계값 결정 (예: 개발자 대응 · 기각 기록) |
| 임계값 유지 | 코드베이스 · 규약 변화에 맞춰 기록과 정기 대조 |
| 후보 지적 검증 | 코드와 대조해 오탐 제거 후 게시<br>(Claude Code 관리형 코드 리뷰 구성) |
| 오탐 40% · 확인 시간 병목 · 필터링 금지 | 지적마다 근거 · 신뢰도를 바로 포함<br>→ 전부 노출 · 개발자 분류 가속 |

<sub>근거: CCAR-F-MyPractice-0017, CCAR-F-MyPractice-0027, CCAR-F-MyPractice-0052, CCAR-F-Udemy01-0033, CCAR-F-Udemy02-0028, CCAR-F-Udemy02-0031, CCAR-F-Udemy02-0056, CCAR-F-Udemy03-0007, CCAR-F-Udemy03-0023, CCAR-F-Udemy03-0025, CCAR-F-Udemy03-0030, CCAR-F-Udemy04-0003, CCAR-F-Udemy04-0013, CCAR-F-Udemy05-0022, CCAR-F-Udemy05-0060, CCAR-F-Udemy06-0021, CCAR-F-paullarionov-0017, CCAR-F-paullarionov-0027, CCAR-F-paullarionov-0028, CCAR-F-paullarionov-0052</sub>

@@ RULES
| 원본에 없을 수 있는 값(예: PO 번호 · 배송일) | nullable · 조건부 필수는 후단 검증 |
| 필수 필드 때문에 없는 값 날조<br>(예: 존재하지 않는 종료일) | 필드 nullable · prompt 추가 ✗<br>별도 필드와 조합해 계약 종류 판단 |
| enum 분류에서 새 유형이 기존 값으로 오분류 | `other` + 상세 필드 · `unclear` 추가<br>`other` 모니터링 → 정식 값 승격 |
| 값의 원본 위치 기록 필요 | 출처 필드를 schema에 선언 |
| 결측 표기 혼재 · 문장 규칙으로 해결 안 됨 | 예시 3~5개 + schema로 null만 허용 |
| 같은 입력인데 변환 결과 문체 · 구조 편차 | 이상적 출력 예시 + 필수 요소 · 순서 템플릿 |
| 성질이 다른 내용이 섞인 보고서 | 유형별 표현<br>(재무 = 표 · 뉴스 = 문장 · 기술 = 구조화 리스트) |
| 창고 · 하위 시스템 보호 (형태 확정 보장) | structured outputs + 전달 전 코드 validator |
| 형태 오류 재시도 루프 없이 고정 JSON | `output_config.format` schema<br>+ 파싱 전 `stop_reason` 확인 |
| 스키마 위반을 근원에서 제거 | constrained decoding<br>+ semantic 검사 · `stop_reason` 처리 별도 |
| forced tool use 거부 모델에서 enum 라벨 1개 | `auto` + strict tool use<br>또는 enum 포함 structured outputs |
| 새 모델 prefill 400 + 형식 유지 | system prompt 지시 (thinking 끄기 ✗) |
| 구문 오류 해소 후 값이 엉뚱한 필드에 입력 · 합계 불일치 | 의미 검증 코드 + 필드 `description`<br>`strict` · `tool_choice` ✗ |
| 검증 실패 후 retry | 원본 + 거부된 출력 + 구체적 validator 오류 |
| 필드 누락 · 잘못된 enum · 소스에 없는 값 동시 발생 | 세 재료를 태그로 구분해 전달 · 수정본만 반환 |
| 검증이 정보 부재로 반복 실패 | 누락 원본 제공 → 그래도 없으면 "이용 불가" 허용 |
| 소스 자체 모순(합계 전기 오류)으로 retry 한도 소진 | `stated_total` · `calculated_total`<br>· `conflict_detected` → 불일치 기록 후 사람에게 |
| 재시도 N회에도 특정 오류 0건 해소 | 입력에 정보 없음 신호 · 오류 원인별 대응 분리 |
| schema 적합 tool 호출이 업무 규칙에 거부 | `is_error: true` `tool_result` + 구체 이유<br>+ 대화 이력 유지 |
| 응답이 `max_tokens`로 끊김 + 존재하지 않는 행 번호 | 상한 상향 재시도 또는 요청 분할<br>행 번호는 참조 대상과 대조 |
| 드문 validation 실패 | 정해진 처리 경로 · 조용한 통과 차단 |
| 자기 리뷰가 미묘한 결함을 놓침 | 독립 instance · 생성 시 추론 미전달 |
| extended thinking을 늘려도 리뷰 결과 불변 | 원인 = context 공유 → 별도 session 리뷰 |
| 대형 PR 리뷰의 깊이 · 일관성 편차 | 파일별 집중 pass + 통합 pass |
| 파일별 pass 후에도 파일 간 불일치 통과 | 통합 pass 추가 |
| 예측 가능한 섹션의 긴 문서 추출 | 섹션별 추출 chain + 통합 대조 pass |
| 근거 없는 주장 · 출처 모순 + 생성 전 checkpoint 요구 | 출처 단위 리뷰 chain + 통합 pass |
| 설명 완전성이 들쭉날쭉 · 사람 감독 추가 ✗ | 초안 전 자기 비평 단계 (evaluator-optimizer) |
| 포괄적 분석 + 우선순위 구분 불가 | confidence · severity · evidence<br>schema 검증 pass + 경로 대응 규칙 |
| 오탐 많음 + 필터링 금지 + 확인 시간 병목 | 지적마다 근거 · 신뢰도 포함 |
| 확신도 임계값 결정 | 정답 라벨 데이터로 캘리브레이션 |

<sub>근거: CCAR-F-Amey-Thakur-0008, CCAR-F-Amey-Thakur-0048, CCAR-F-Amey-Thakur-0072, CCAR-F-Amey-Thakur-0074, CCAR-F-Udemy01-0023, CCAR-F-Udemy01-0025, CCAR-F-Udemy01-0032, CCAR-F-Udemy01-0042, CCAR-F-Udemy01-0046, CCAR-F-Udemy02-0018, CCAR-F-Udemy02-0026, CCAR-F-Udemy02-0028, CCAR-F-Udemy02-0031, CCAR-F-Udemy03-0007, CCAR-F-Udemy03-0018, CCAR-F-Udemy03-0023, CCAR-F-Udemy03-0030, CCAR-F-Udemy04-0006, CCAR-F-Udemy04-0013, CCAR-F-Udemy04-0032, CCAR-F-Udemy04-0033, CCAR-F-Udemy04-0045, CCAR-F-Udemy05-0003, CCAR-F-Udemy05-0022, CCAR-F-Udemy05-0032, CCAR-F-Udemy05-0037, CCAR-F-Udemy05-0060, CCAR-F-Udemy06-0020, CCAR-F-paullarionov-0027, CCAR-F-paullarionov-0028, CCAR-F-paullarionov-0052, CCAR-F-preporato-0026, CCAR-P-jrajath94-0139, CCAR-P-jrajath94-0618, CCAR-P-jrajath94-0621, CCAR-P-jrajath94-0622, CCAR-P-preporato-0009</sub>

@@ TRAPS
| 모든 필드 required<br>모든 필드 optional | 정상 문서에서도 값 날조 · 실패<br>진짜 놓친 경우 감지 불가 |
| 값 없음을 그럴듯한 기본값 · 빈 문자열 · 생략 · 메모 필드로 표현 | 날조 · 없음 vs 빈 값 구별 불가<br>기계 판독 불가 |
| 필수 종료일 날조에 prompt 추가<br>후처리 보정<br>`strict: true` | schema(필수)와 모순<br>날조를 다른 날조로 교체<br>필수 제약만 더 확실해짐 |
| enum 제거 | 값 흔들림 · 하류 처리 어려움 |
| enum에 가장 가까운 카테고리 선택 강제 | 새 유형 오분류 |
| enum 대신 자유 기술 문자열 | 정해진 값의 하류 처리 이점 상실 |
| 결측 표기 혼재에 문장 규칙 강화<br>`CLAUDE.md`로 이동 | 이미 효과 없던 방법의 연장<br>추출 pipeline 실행 context와 무관 |
| 출처 필드 요구를 큰 모델 · 긴 prompt<br>· 두 번째 pass로 해결 | 필드는 schema에 선언해야 생김 |
| 변환 지시의 단어 강조<br>`PreToolUse` hook | 해석 폭 불변<br>증상 하나만 차단 |
| 표 하나 · 템플릿 하나로 통일<br>재무 데이터를 문장으로 | 획일화 그대로<br>표현은 나눴어도 내용과 대응 틀림 |
| "JSON만 반환" prompt를 schema 대용으로 사용 | 텍스트를 제한하는 장치 없음 |
| prompt 요청 · 텍스트 파싱<br>사후 수정 · temperature 조정 | 형태를 우연에 맡김 |
| prompt 설명 · 문서화를 보장으로 착각 | 샘플링으로 형태 깨짐 · 창고는 문서를 못 읽음<br>보장은 생성 제약 + validator |
| thinking 끄기로 prefill 400 해결 | 마지막 assistant 턴 prefill 자체가 400 |
| forced tool use 거부 모델에서<br>이름 지정 `tool_choice` | 400 error |
| regex로 스키마 위반 복구 | 의도 추측 → 데이터 조용히 손상 |
| 구문 오류 해소 후<br>`strict: true` · `tool_choice` 강제<br>schema 제거 | 형식 쪽 조작 · 이미 충족된 조건 강화 |
| schema만 믿고 행 번호 · 인용 검증 생략 | 의미 오류 방치 |
| 합계를 시스템이 직접 계산<br>같은 추출 2회 실행해 결과 일치만 확인 | 오류가 가려짐<br>일관된 오류를 놓침 |
| 재시도 문구 "다시 하라" · "무효한 JSON 수정"<br>"주의하라" | 무엇이 틀렸는지 전달 ✗ |
| 재시도에서 원본 제외<br>같은 조건 반복<br>모델만 교체 | 교정 재료 소실<br>오류를 낳은 조건 그대로<br>무엇이 잘못됐는지 미전달 |
| 재시도 횟수 · 상한 인상 | 소스에 없는 정보 · 소스 모순에는 무효 · 비용만 증가 |
| 소스 불일치를 덮어쓰기 · 문서 폐기 | 소스 모순이라는 사실 소실 |
| 존재하지 않는 정보에 재시도 · strict · few-shot | 없는 정보를 모델이 채우게 함 |
| 드문 validation 실패 무시<br>validation 끄기 | 잘못된 데이터 조용히 통과 |
| 경계 validation의 이유를 비용 절감 · 정확도 향상으로 설명 | 핵심 = 결함 확산 방지 |
| 업무 규칙 거부를 조용히 삭제<br>일반 지시로 대체<br>`failed`만 반환 | 이번 오류를 Claude에 알릴 경로 없음 |
| `max_tokens` 중단을 `pause_turn`으로 처리 | `pause_turn` = 서버 tool loop 일시 정지 |
| 같은 session 안 보강<br>extended thinking · effort 상향 · 재리뷰<br>`/compact` · 근거 재독 · resume | 생성 시 전제 공유 · 독립성 없음 |
| "회의적으로 보라" 촉구 · 합성 메시지 삽입<br>확신도 필드 추가 | 같은 문맥 안에 머묾<br>대조 구조 아님 |
| 별도 instance에 생성 시 대화 기록 전달 | 독립성 소실 |
| 기존 이력에서 셀프 리뷰 유지<br>통합 1회가 검사까지 겸임 | 같은 전제 공유 · 놓치는 부분 발생 |
| diff · 파일 전체를 single-pass 리뷰<br>한 큰 prompt에 전부 | 주의 분산 · 깊이 편차 |
| 통합 리뷰만 수행<br>통합 없는 병렬 리뷰 · 파일별 pass만 | 국소 결함 누락<br>파일 간 문제 누락 |
| 경로 선택을 모델에 맡기는 자율 조사 | 고정 절차 요건과 반대 |
| 요약을 거친 추출<br>동적 분해 | 세부 정보 손실<br>예측 가능한 구조에는 과함 |
| 확신도 점수 · 동일 리뷰어 다수결 · 긴 체크리스트 | 긴 묶음을 한 번에 처리하는 구조 불변 |
| 높은 확신도만 남김<br>API 응답의 확신도 사용 | 포괄성 상실<br>존재하지 않는 값에 의존 |
| 근거 없는 건수 제한 · 일반 prompt 지시<br>같은 session의 미캘리브레이션 수치 | 실제 데이터의 뒷받침 없음 |
| 지적을 개발자에게 보이기 전 필터링 | 제시된 조건(필터링 반대) 위반 |

<sub>근거: CCAR-F-Amey-Thakur-0008, CCAR-F-Amey-Thakur-0023, CCAR-F-Amey-Thakur-0025, CCAR-F-Amey-Thakur-0048, CCAR-F-Amey-Thakur-0058, CCAR-F-Amey-Thakur-0059, CCAR-F-Amey-Thakur-0072, CCAR-F-Amey-Thakur-0073, CCAR-F-Amey-Thakur-0074, CCAR-F-MyPractice-0027, CCAR-F-Udemy01-0023, CCAR-F-Udemy01-0025, CCAR-F-Udemy01-0032, CCAR-F-Udemy01-0033, CCAR-F-Udemy01-0042, CCAR-F-Udemy01-0046, CCAR-F-Udemy02-0018, CCAR-F-Udemy02-0026, CCAR-F-Udemy02-0028, CCAR-F-Udemy02-0031, CCAR-F-Udemy02-0056, CCAR-F-Udemy03-0007, CCAR-F-Udemy03-0018, CCAR-F-Udemy03-0023, CCAR-F-Udemy03-0025, CCAR-F-Udemy03-0030, CCAR-F-Udemy03-0048, CCAR-F-Udemy04-0003, CCAR-F-Udemy04-0006, CCAR-F-Udemy04-0013, CCAR-F-Udemy04-0032, CCAR-F-Udemy04-0033, CCAR-F-Udemy04-0045, CCAR-F-Udemy05-0003, CCAR-F-Udemy05-0022, CCAR-F-Udemy05-0032, CCAR-F-Udemy05-0037, CCAR-F-Udemy05-0060, CCAR-F-Udemy06-0020, CCAR-F-Udemy06-0021, CCAR-F-paullarionov-0027, CCAR-F-paullarionov-0028, CCAR-F-preporato-0026, CCAR-P-jrajath94-0139, CCAR-P-jrajath94-0618, CCAR-P-jrajath94-0621, CCAR-P-jrajath94-0622, CCAR-P-preporato-0009</sub>

@@ MEMO
| Nullable 필드 | 원본에 없을 수 있는 값을 `null`로 표현<br>→ 진짜 없음 vs 추출 실패 구분 |
| `other` + 상세 필드 | 확장 가능한 enum 설계<br>미분류 입력의 오분류 방지 · 내용 보존 |
| `unclear` | 분류 판단 불가 수용 값 → 사람 리뷰 |
| 의미 검증 (semantic validation) | schema 밖 코드로 값 · 필드 간 정합성 확인 |
| 재시도 3재료 | 원본 문서 · 거부된 JSON · validator 구체 오류 |
| `is_error: true` | 실패한 `tool_result` 표시<br>구체적 이유와 함께 반환 |
| `stated_total` · `calculated_total`<br>· `conflict_detected` | 소스 기재 합계 · 계산 합계 · 불일치 플래그<br>→ 소스 모순을 기록한 채 사람에게 |
| `stop_reason: "max_tokens"` | 응답이 상한에서 끊김 · schema 준수 보장 ✗ |
| `pause_turn` | 서버 tool loop 일시 정지 |
| Attention dilution | 한 pass에 너무 많이 넣을 때 주의가 분산되는 현상 |
| 국소 pass · 통합 pass | 파일(섹션)별 집중 분석 · 파일 간 데이터 흐름 분석 |
| Prompt chaining | 작업을 고정 단계로 나눠 출력을 다음 단계에 전달 |
| Evaluator-optimizer | 생성 → 기준 평가 → 피드백 반영 패턴 |
| Writer/Reviewer 패턴 | 한 session이 작성 · 다른 session이 리뷰 |
| Confidence calibration | 확신도를 정답 라벨 데이터로 보정해 임계값 결정 |
| `--output-format json` + `--json-schema` | Claude Code 출력을 schema로 구조화 |

<sub>근거: CCAR-F-Amey-Thakur-0025, CCAR-F-Amey-Thakur-0059, CCAR-F-Udemy01-0023, CCAR-F-Udemy01-0025, CCAR-F-Udemy02-0018, CCAR-F-Udemy02-0026, CCAR-F-Udemy03-0007, CCAR-F-Udemy03-0018, CCAR-F-Udemy03-0023, CCAR-F-Udemy03-0025, CCAR-F-Udemy03-0030, CCAR-F-Udemy04-0045, CCAR-F-Udemy05-0022, CCAR-F-Udemy05-0037, CCAR-F-Udemy06-0021, CCAR-F-paullarionov-0052</sub>

@@ CHECK
- [ ] 없을 수 있는 값 = nullable · enum = `other` + 상세 필드
- [ ] schema = 구조 보장 · 의미 오류 = 별도 검증 코드
- [ ] 재시도 = 원본 + 거부된 출력 + 구체 오류 · 정보 부재 · 소스 모순에는 무효
- [ ] 리뷰 = 독립 instance · 추론 미전달 · 큰 입력 = 국소 pass + 통합 pass

<sub>근거: CCAR-F-Amey-Thakur-0008, CCAR-F-Udemy01-0025, CCAR-F-Udemy03-0018, CCAR-F-Udemy04-0003, CCAR-F-Udemy04-0006, CCAR-F-Udemy04-0013, CCAR-F-Udemy04-0045, CCAR-F-Udemy05-0003, CCAR-F-Udemy06-0020</sub>
