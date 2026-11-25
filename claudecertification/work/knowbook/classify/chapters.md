# 개념서 장 범위 (분류 기준)

문항 하나를 아래 장 중 **그 배치에 주어진 후보 장** 하나에만 배정한다. 기준은 "이 문항의 정답을 고르는 데 필요한 핵심 지식이 어느 장에 실려야 하는가"이다.

- 1 Agents and Workflows: workflow vs agent, workflow 패턴(chaining·routing·parallelization·orchestrator-workers·evaluator-optimizer), coordinator/subagent 구조, agentic loop, 종료·안전장치·상태, 구현 수단 비교(Agent SDK 등), deployment 선택, task decomposition, 아키텍처 패턴 상세
- 2 Applications and Integration: Messages API 구조, stop_reason, streaming, prompt caching(구현), Batch API(구현), Files API·이미지·PDF, citations, structured outputs(API 기능), 오류·retry·rate limit, 동시성·비동기 통합, context window 관리 API, SDK·플랫폼(Bedrock·Vertex), 운영·변경관리
- 4 Eval, Testing, Observability & Debugging: eval set, grader(LLM-as-judge 등), regression suite, model 업그레이드 검증, prompt SDLC, debugging·localize, observability·logging·tracing, A/B 테스트, 출력 품질 측정
- 5 Model Selection and Optimization: 모델 선택(Opus·Sonnet·Haiku), routing, effort·extended/adaptive thinking, 비용·latency 절감, batch·caching의 비용 판단, version pinning, temperature·비결정성
- 6 Prompt, Structured Output & Context Engineering: system prompt, few-shot, 출력 형식·XML, structured output을 얻는 프롬프트/스키마 설계, long context 배치, context rot·hygiene(prune·compact·isolate), multi-pass review, validation·retry loop(출력 검증 후 재요청)
- 7 Security, Safety & Governance: prompt injection, least privilege, approval gate, authorization, secret, PII, output handling, guardrail, 규제(GDPR·HIPAA·FedRAMP), 데이터 보존·감사, 윤리(bias·fairness), 위험 관리
- 8 Tools and MCPs: tool 정의·description·schema, tool_choice, tool 에러, tool 결과 설계, MCP(primitives·transport·connector), built-in tools
- 9 RAG & Retrieval: RAG vs long context vs tool 조회, chunking, embedding·BM25·hybrid indexing, retrieval 선택, reranking·top-k, progressive discovery, 검색 결과 배치·citations, RAG 실패 진단
- 10 Reliability, Escalation & Human Oversight: escalation 기준, 모호한 요청엔 확인 질문, multi-agent 에러 전파, 부분 실패·fallback·복구, 대규모 코드베이스 탐색 시 context 관리, human review workflow(출력 품질 검토), confidence calibration, provenance 보존, 상충 출처·불확실성 표기
- 11 Solution Design & Stakeholder Communication: 비즈니스 문제 → Claude 솔루션 적합성, discovery·요구사항, end-to-end 아키텍처, business value·ROI, trade-off 전달, 기대치·SLA, 문서화·handoff, lifecycle(discovery→design→handoff→monitoring→iteration), 이해관계자 커뮤니케이션

애매하면: 문항이 "무엇을 만들까/누구에게 어떻게 설명할까"면 11, "어떻게 구현할까"면 1·2, "얼마나 잘 되는지 어떻게 알까"면 4, "어떤 모델·비용"이면 5.
