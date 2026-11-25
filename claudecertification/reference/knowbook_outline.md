# 개념서 장 구성 (output/Know(CCDV-F))

결정일: 2026-11-21. 시험 도메인과 장의 연결은 `chapter_map.json`이 기준이다.

## 왜 11개 장인가
- 1~8장은 CCDV-F의 8개 도메인을 그대로 따라 만들었다(2026-11-18, CCDV-F 207문항 기준).
- CCAR-F와 CCAR-P를 커버하려면 CCDV-F에 없는 내용이 필요해서 9~11장을 추가한다.
- 장은 시험 도메인이 아니라 개념 기준으로 나눈다. 어느 시험을 준비하든 필요한 장만 골라 볼 수 있게, 장 제목 아래에 `커버: CCDV-F D2 · CCAR-F D4` 형식의 줄을 넣는다.

## 장 목록과 상태

| 장 | 제목 | 파일 | 상태 | 남은 일 |
|---|---|---|---|---|
| 1 | Agents and Workflows | `1_Agents_and_Workflows.md` | `Know(CCAR-F&P)`에 CCAR-F D1 · CCAR-P D1 보강 완료 (2026-11-24, 191문항, 1.9~1.26 신설) | ⚠️ 공식 문서 검증 완료 (2026-11-25, 남은 ⚠️ 4건 = 불일치·미확인) |
| 2 | Applications and Integration | `2_Applications_and_Integration.md` | `Know(CCAR-F&P)`에 CCAR-P D3(일부) · CCAR-F D4(일부) 보강 완료 (2026-11-24, 50문항, 1.16~1.20 신설) | ⚠️ 공식 문서 검증 완료 (2026-11-25, 남은 ⚠️ 4건 = 불일치·미확인) |
| 3 | Claude Code & Developer Productivity | `3_Claude_Code.md` | `Know(CCAR-F&P)`에 CCAR-F D3 · CCAR-P D7 보강 완료 (2026-11-24, 215문항) | ⚠️ 공식 문서 검증 완료 (2026-11-25, 남은 ⚠️ 7건 = 불일치·미확인) |
| 4 | Eval, Testing, Observability & Debugging | `4_Eval_Testing_and_Debugging.md` | `Know(CCAR-F&P)`에 CCAR-P D4·D3(일부) · CCAR-F D4(일부) 보강 완료 (2026-11-24, 133문항, 1-9.~1-26. 신설) | ⚠️ 공식 문서 검증 완료 (2026-11-25, 남은 ⚠️ 7건 = 불일치·미확인) |
| 5 | Model Selection and Optimization | `5_Model_Selection_and_Optimization.md` | `Know(CCAR-F&P)`에 CCAR-P D2·D4(일부) 보강 완료 (2026-11-24, 82문항, 1-10.~1-20. 신설) | ⚠️ 공식 문서 검증 완료 (2026-11-25, 남은 ⚠️ 16건 = 불일치·미확인) |
| 6 | Prompt, Structured Output & Context Engineering | `6_Prompt_and_Context_Engineering.md` | `Know(CCAR-F&P)`에 CCAR-F D4·D5 · CCAR-P D2(일부) 보강 완료 (2026-11-24, 195문항, 1.9~1.29 신설) | ⚠️ 공식 문서 검증 완료 (2026-11-25, 남은 ⚠️ 7건 = 불일치·미확인) |
| 7 | Security, Safety & Governance | `7_Security_and_Safety.md` | `Know(CCAR-F&P)`에 CCAR-P D5(일부) 보강 완료 (2026-11-24, 96문항, 1.10~1.27 신설) + CCAR-P D3 보안 문항 23개 8장에서 이동 (2026-11-25, 1.28 신설) | ⚠️ 공식 문서 검증 완료 (2026-11-25, 남은 ⚠️ 4건 = 불일치·미확인) |
| 8 | Tools and MCPs | `8_Tools_and_MCPs.md` | `Know(CCAR-F&P)`에 CCAR-F D2 · CCAR-P D3(일부) 보강 완료 (2026-11-24, 180문항, 1-15.~1-26. 신설) → 보안 문항 23개 7장으로 이동 (2026-11-25, 157문항, 1-15.~1-25.) | ⚠️ 공식 문서 검증 완료 (2026-11-25, 남은 ⚠️ 3건 = 불일치·미확인) |
| 9 | RAG & Retrieval | `9_RAG_and_Retrieval.md` | `Know(CCAR-F&P)`에 CCAR-P D3(일부)로 신규 작성 완료 (2026-11-25, 44문항, 1.1~1.13) | ⚠️ 공식 문서 검증 완료 (2026-11-25, 남은 ⚠️ 1건 = 불일치·미확인) |
| 10 | Reliability, Escalation & Human Oversight | `10_Reliability_Escalation_and_Oversight.md` | `Know(CCAR-F&P)`에 CCAR-F D5 · CCAR-P D5(일부)로 신규 작성 완료 (2026-11-24, 84문항, 1.1~1.21) | ⚠️ 공식 문서 검증 완료 (2026-11-25, 남은 ⚠️ 0건 = 불일치·미확인) |
| 11 | Solution Design & Stakeholder Communication | `11_Solution_Design_and_Stakeholder_Communication.md` | `Know(CCAR-F&P)`에 CCAR-P D1·D6(일부)로 신규 작성 완료 (2026-11-25, 155문항, 1.1~1.23) | ⚠️ 공식 문서 검증 완료 (2026-11-25, 남은 ⚠️ 1건 = 불일치·미확인) |

3·4·6·7장의 새 제목은 `chapter_map.json`에만 반영되어 있다. md 파일의 제목과 파일명은 아직 예전 그대로다.

## 9~11장 목차 (초안)

시험 가이드의 objective를 기준으로 잡았다. 문항과 대조하지 않았으므로, 근거 문항이 없는 소절은 빼고 문항이 많은 주제는 소절을 늘린다. 아래는 "1. 핵심 개념"의 소절이고, 2~5장(판단 규칙 / 오답 함정 / 암기 목록 / 체크리스트)은 다른 장과 같다.

### 9. RAG & Retrieval
커버: CCAR-P D3

- 9.1 RAG가 필요한 경우 vs long context · fine-tuning · tool 조회
- 9.2 파이프라인 전체 흐름 (ingest → chunk → index → retrieve → rerank → generate)
- 9.3 Chunking 전략 (크기 · overlap · 문서 구조 기반 · contextual chunk)
- 9.4 Indexing 전략 (embedding · keyword/BM25 · hybrid · metadata)
- 9.5 데이터 형태와 질의 패턴에 맞는 retrieval 선택 (정형 → SQL/tool, 비정형 → vector, 관계형 → graph)
- 9.6 Reranking과 top-k 조절 (정확도 ↔ latency)
- 9.7 Progressive discovery vs monolithic context
- 9.8 검색 결과의 context 배치와 citations
- 9.9 RAG 실패 진단 (retrieval 실패 vs generation 실패)

### 10. Reliability, Escalation & Human Oversight
커버: CCAR-F D5.2~5.6 · CCAR-P D5 일부

- 10.1 Escalation 기준 (명시적 요청 · 정책 공백 · 진전 불가)
- 10.2 모호한 요청 처리 (추측 대신 확인 질문)
- 10.3 Multi-agent 에러 전파 (subagent 실패를 coordinator에 구조화해 전달)
- 10.4 부분 실패와 복구 (retry · fallback · 부분 결과 보고)
- 10.5 대규모 코드베이스 탐색 시 context 관리 (원리는 6장 참조, 여기는 탐색 상황만)
- 10.6 Human review workflow 설계 (출력 품질 검토. 위험한 행동의 승인은 7장)
- 10.7 Confidence calibration (자기 보고 신뢰도의 한계 · 표본 검증)
- 10.8 Provenance 보존 (출처 · 날짜를 synthesis까지 유지)
- 10.9 상충하는 출처와 불확실성 표기

### 11. Solution Design & Stakeholder Communication
커버: CCAR-P D1 · D6 · CCDV-F D2 일부(Understanding Requirements)

- 11.1 비즈니스 문제를 Claude 솔루션으로 번역 (적합한 문제 vs 부적합한 문제)
- 11.2 Discovery와 요구사항 수집 (functional · non-functional · 제약)
- 11.3 End-to-end 아키텍처 (input → processing → output → feedback loop)
- 11.4 아키텍처 패턴 선택 기준 (상세는 1장 참조)
- 11.5 복잡한 문제의 decomposition (상세는 1장 참조)
- 11.6 Business value pillar 정렬 (efficiency · transformation · productivity · cost · performance SLA)
- 11.7 Trade-off와 아키텍처 결정 전달 (청중별 설명)
- 11.8 기대치 관리와 SLA 합의, 피드백 루프
- 11.9 아키텍처 문서화와 구현 가이드 (handoff)
- 11.10 Lifecycle 단계 (discovery → design → handoff → monitoring → iteration)

## 예정: 공식 문서로 검증
- 문항(`output/{시험}/20_gold/all.json`)의 정답·해설과 개념서의 지식을 공식 문서와 대조한다. 아직 시작하지 않았다.
- 기준 주소는 `CLAUDE.md`의 "사실의 출처"에 있다(llms.txt 두 곳, 2026-11-21 접속 확인).
- 먼저 볼 곳: 개념서의 ⚠️ 항목, 그리고 모델 버전·가격·한도처럼 시점에 따라 바뀌는 내용.
- 절차는 처음 검증할 때 skill(`.claude/skills/verify-against-docs/`)로 만든다. 결과를 어디에 남길지(문항에 표시할지, 별도 보고서로 둘지)는 그때 정한다.

## 알아둘 것
- CCAR-F gold의 `미분류`는 0개(2026-11-24 확인). 여러 장에 걸친 도메인의 CCAR 770문항은 장 배정을 마쳤다: `work/knowbook/classify/ccar_chapter_map.json`, 장별 문항은 `work/knowbook/ch{N}.json`.
- CCAO-F는 장 구성에 넣지 않았다(개념서 대상은 CCDV와 CCAR).
- CCDV-P는 시험 가이드가 공개되지 않아 다루지 않는다.
