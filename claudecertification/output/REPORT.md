# 문제 통합 보고서

원본 파일은 수정하지 않았고, 문제·보기·정답·해설은 원본 그대로입니다. 섹션은 각 시험의 공식 exam-guide.pdf (`work/domains/<시험코드>/domains.json`) 기준입니다.

## 1. 시험별 요약

| 시험 | 추출 | 제외(검사 실패) | 중복 제거 | 최종 문제 수 | 원본 섹션 표기 사용 | classifier 분류 | 검토 필요 |
|---|---:|---:|---:|---:|---:|---:|---:|
| CCAO-F | 448 | 0 | 222 | 226 | 226 | 0 (high 0 / medium 0 / low 0) | 1 |
| CCDV-F | 264 | 0 | 110 | 154 | 110 | 44 (high 22 / medium 21 / low 1) | 1 |
| CCAR-F | 280 | 0 | 110 | 170 | 110 | 60 (high 44 / medium 16 / low 0) | 0 |
| CCAR-P | 929 | 0 | 110 | 819 | 683 | 136 (high 67 / medium 62 / low 7) | 7 |
| **합계** | 1921 | 0 | 552 | 1369 | 1129 | 240 | 9 |

## 2. 섹션별 문제 수

### CCAO-F

| 섹션 | 공식 비중 | 문제 수 | 비율 |
|---|---:|---:|---:|
| 1. Prompting and Task Execution | 14% | 32 | 14% |
| 2. Output Evaluation and Validation | 21% | 44 | 19% |
| 3. Product and Model Selection | 12% | 28 | 12% |
| 4. Workflow Integration and Solution Design | 16% | 36 | 16% |
| 5. Configuration and Knowledge Management | 12% | 28 | 12% |
| 6. Governance, Risk, and Responsible Use | 15% | 33 | 15% |
| 7. Troubleshooting and Optimization | 10% | 25 | 11% |

### CCDV-F

| 섹션 | 공식 비중 | 문제 수 | 비율 |
|---|---:|---:|---:|
| 1. Agents and Workflows | 14.7% | 21 | 14% |
| 2. Applications and Integration | 33.1% | 50 | 32% |
| 3. Claude Code | 3.1% | 4 | 3% |
| 4. Eval, Testing, and Debugging | 2.6% | 11 | 7% |
| 5. Model Selection and Optimization | 16.8% | 24 | 16% |
| 6. Prompt and Context Engineering | 11.0% | 17 | 11% |
| 7. Security and Safety | 8.1% | 13 | 8% |
| 8. Tools and MCPs | 10.6% | 14 | 9% |

### CCAR-F

| 섹션 | 공식 비중 | 문제 수 | 비율 |
|---|---:|---:|---:|
| 1. Agentic Architecture & Orchestration | 27% | 33 | 19% |
| 2. Tool Design & MCP Integration | 18% | 26 | 15% |
| 3. Claude Code Configuration & Workflows | 20% | 40 | 24% |
| 4. Prompt Engineering & Structured Output | 20% | 36 | 21% |
| 5. Context Management & Reliability | 15% | 35 | 21% |

### CCAR-P

| 섹션 | 공식 비중 | 문제 수 | 비율 |
|---|---:|---:|---:|
| 1. Solution Design & Architecture | 17% | 119 | 15% |
| 2. Claude Models, Prompting & Context Engineering | 13% | 110 | 13% |
| 3. Integration | 19% | 158 | 19% |
| 4. Evaluation, Testing & Optimization | 16% | 141 | 17% |
| 5. Governance, Safety & Risk Management | 14% | 114 | 14% |
| 6. Stakeholder Communication & Lifecycle Management | 14% | 102 | 12% |
| 7. Developer Productivity & Operational Enablement | 7% | 75 | 9% |

## 3. 제외된 문제 (`work/rejected.json`)

0개. 모든 문제가 검사(본문 있음, 보기 2개 이상, 정답이 보기 안에 있음, 정답 수 = select_count)를 통과했습니다.

## 4. 중복

- 본문을 정리(공백·대소문자·기호 제거)해 같으면 중복으로 보고 1개만 남겼습니다. 나머지 출처는 `also_in` 필드에 있습니다. 제거: **552개**.
- 본문이 같아도 보기가 다르면 다른 문제로 보고 남깁니다.
- 비슷하지만 같지 않은 문제(유사도 0.85 이상): **0쌍** (`work/near_duplicates.json`).
- 중복이 많은 이유: 같은 레포 안에서 md 와 json 이 같은 문제를 담고 있음 (Amey-Thakur md ↔ question-bank.json, preporato md ↔ practice/*.json, raybeecham 모듈 퀴즈 ↔ practice-exam-01/02 ↔ data/questions.json).

## 5. 검토가 필요한 문제 (`work/review_needed.json`)

| ID | 이유 |
|---|---|
| CCAO-F-Amey-Thakur-0005 | 중복 출처 간 정답 불일치: associate-foundations/practice-questions.md → ['B'], question-bank.json → ['A'] |
| CCDV-F-PatrickWiloak-0044 | 섹션 분류 확신 낮음 (classifier confidence=low) |
| CCAR-P-jrajath94-0585 | 섹션 분류 확신 낮음 (classifier confidence=low) |
| CCAR-P-jrajath94-0599 | 섹션 분류 확신 낮음 (classifier confidence=low) |
| CCAR-P-jrajath94-0674 | 섹션 분류 확신 낮음 (classifier confidence=low) |
| CCAR-P-jrajath94-0684 | 섹션 분류 확신 낮음 (classifier confidence=low) |
| CCAR-P-jrajath94-0687 | 섹션 분류 확신 낮음 (classifier confidence=low) |
| CCAR-P-jrajath94-0694 | 섹션 분류 확신 낮음 (classifier confidence=low) |
| CCAR-P-jrajath94-0700 | 섹션 분류 확신 낮음 (classifier confidence=low) |

## 6. 건너뛴 파일 / 섹션

| 파일 | 이유 |
|---|---|
| CCAR-F/paullarionov__practical_test_ko.html | 같은 문제의 한국어판 — 영어판(_en)만 추출 |
| CCAR-P/jrajath94__question-bank.html (Prerequisite diagnostic: answer key 섹션) | 정답표만 있고 문제는 이 레포에 복사하지 않은 crash-course.html 에 있음 |
| CCAR-P/jrajath94__question-bank.html (Counterfactual drills 섹션, 26쌍 52개) | 보기가 없는 비교 드릴 — 객관식 문제가 아님 |
| CCAR-P/jrajath94__package-v3__practice-test.html | practice-answer-key.html 과 같은 126문제(정답 없음) — 정답이 있는 answer-key 판만 추출 |
| CCAO-F/raybeecham__practice-exam-0N-answers.md (3개) | 따로 추출하지 않음 — 문제 파일과 짝지어 정답·해설을 가져옴 |
| 학습 노트·요약만 있는 파일 | 해당 없음 (시험 폴더에는 문제 파일만 있음) |

## 7. 원본 파일별 문제 수 비교

| 원본 파일 | 원본 문제 수 | 추출된 문제 수 | 일치 |
|---|---:|---:|---|
| CCAO-F/Amey-Thakur__practice-questions.md | 35 | 35 | ✅ |
| CCAO-F/Amey-Thakur__mock-exam-1.md | 15 | 15 | ✅ |
| CCAO-F/Amey-Thakur__mock-exam-2.md | 15 | 15 | ✅ |
| CCAO-F/Amey-Thakur__mock-exam-3.md | 15 | 15 | ✅ |
| CCAO-F/preporato__practice-questions.md | 30 | 30 | ✅ |
| CCDV-F/Amey-Thakur__practice-questions.md | 35 | 35 | ✅ |
| CCDV-F/Amey-Thakur__mock-exam-1.md | 15 | 15 | ✅ |
| CCDV-F/Amey-Thakur__mock-exam-2.md | 15 | 15 | ✅ |
| CCDV-F/Amey-Thakur__mock-exam-3.md | 15 | 15 | ✅ |
| CCDV-F/preporato__practice-questions.md | 30 | 30 | ✅ |
| CCAR-F/Amey-Thakur__practice-questions.md | 35 | 35 | ✅ |
| CCAR-F/Amey-Thakur__mock-exam-1.md | 15 | 15 | ✅ |
| CCAR-F/Amey-Thakur__mock-exam-2.md | 15 | 15 | ✅ |
| CCAR-F/Amey-Thakur__mock-exam-3.md | 15 | 15 | ✅ |
| CCAR-F/preporato__practice-questions.md | 30 | 30 | ✅ |
| CCAR-P/Amey-Thakur__practice-questions.md | 35 | 35 | ✅ |
| CCAR-P/Amey-Thakur__mock-exam-1.md | 15 | 15 | ✅ |
| CCAR-P/Amey-Thakur__mock-exam-2.md | 15 | 15 | ✅ |
| CCAR-P/Amey-Thakur__mock-exam-3.md | 15 | 15 | ✅ |
| CCAR-P/preporato__practice-questions.md | 30 | 30 | ✅ |
| CCAO-F/raybeecham__practice-exam-01.md | 28 | 28 | ✅ |
| CCAO-F/raybeecham__practice-exam-02.md | 28 | 28 | ✅ |
| CCAO-F/raybeecham__practice-exam-03-blueprint-weighted.md | 60 | 60 | ✅ |
| CCAO-F/raybeecham__01-platform-model-foundations__quiz.md | 8 | 8 | ✅ |
| CCAO-F/raybeecham__02-prompting-task-execution__quiz.md | 8 | 8 | ✅ |
| CCAO-F/raybeecham__03-evaluating-validating-output__quiz.md | 8 | 8 | ✅ |
| CCAO-F/raybeecham__04-workflow-integration-solutions-design__quiz.md | 8 | 8 | ✅ |
| CCAO-F/raybeecham__05-configuration-knowledge-management__quiz.md | 8 | 8 | ✅ |
| CCAO-F/raybeecham__06-governance-risk-responsible-use__quiz.md | 8 | 8 | ✅ |
| CCAO-F/raybeecham__07-troubleshooting-optimization__quiz.md | 8 | 8 | ✅ |
| CCDV-F/PatrickWiloak__scenarios.md | 14 | 14 | ✅ |
| CCDV-F/PatrickWiloak__practice-questions__anthropic-claude-developer-foundations.md | 30 | 30 | ✅ |
| CCAR-F/paullarionov__practical_test_en.html | 60 | 60 | ✅ |
| CCAR-P/jrajath94__08-question-bank.html | 106 | 106 | ✅ |
| CCAR-P/jrajath94__question-bank.html | 477 | 477 | ✅ |
| CCAR-P/jrajath94__package-v3__practice-answer-key.html | 126 | 126 | ✅ |
| CCAO-F/Amey-Thakur__question-bank.json | 80 | 80 | ✅ |
| CCDV-F/Amey-Thakur__question-bank.json | 80 | 80 | ✅ |
| CCAR-F/Amey-Thakur__question-bank.json | 80 | 80 | ✅ |
| CCAR-P/Amey-Thakur__question-bank.json | 80 | 80 | ✅ |
| CCAO-F/preporato__practice__ccao-f.json | 30 | 30 | ✅ |
| CCDV-F/preporato__practice__ccdv-f.json | 30 | 30 | ✅ |
| CCAR-F/preporato__practice__cca-f.json | 30 | 30 | ✅ |
| CCAR-P/preporato__practice__ccar-p.json | 30 | 30 | ✅ |
| CCAO-F/raybeecham__questions.json | 56 | 56 | ✅ |

## 8. 처리 방식 메모

- `.claude/agents/extractor.md`, `classifier.md` 를 만들었지만 실행 중인 세션에는 등록되지 않아, 같은 지침을 프롬프트에 넣고 지정 모델(extractor = haiku, classifier = sonnet)로 실행했습니다. 다음 세션부터는 이름으로 바로 쓸 수 있습니다.
- JSON 파일 9개는 Python 으로 변환했습니다 (`work/scripts/convert_json.py`). preporato CCA-F JSON 은 시나리오 지문이 별도 필드라서 문제 본문 앞에 붙였습니다 (md 판과 같은 형태).
- 큰 HTML (paullarionov, jrajath94) 은 문제 경계에서 조각내어 조각마다 extractor 1개씩 맡긴 뒤 합쳤습니다 (`work/chunks/`, 줄바꿈만 추가).
- 검사: 개수 비교 + 문제·보기 문장이 원본에 그대로 있는지 확인. 원본과 다르게 옮긴 조각 5개는 extractor 에게 다시 맡겨 고쳤습니다. HTML 769문제의 정답을 원본에서 정규식으로 뽑은 정답과 대조해 모두 일치했습니다 (`work/answer_crosscheck.json`, 자동 추출이 안 된 2개는 직접 확인).
- 원본 섹션 표기는 **이름**으로 공식 섹션에 맞췄습니다 (번호는 쓰지 않음). 예: raybeecham 모듈 1 'Claude Platform & Model Foundations' → 3. Product and Model Selection, preporato `d1` → 해당 이름의 공식 섹션, jrajath94 `D3`/`V2-D3.x` → 레포 자체 범례의 이름(D3. Integration) → 3. Integration.
- `domain_confidence`: 원본 표기를 쓴 문제는 `source`, classifier 가 분류한 문제는 `high`/`medium`/`low`.
- preporato JSON 출처 문제의 해설에 있는 `{a}` 같은 표기는 원본 그대로입니다 (원본 빌드 스크립트가 보기 기호로 바꾸는 자리표시).
