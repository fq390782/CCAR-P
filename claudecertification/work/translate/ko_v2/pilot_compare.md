## CCAR-F-Amey-Thakur-0042

**EN** A repeated multi-step review procedure should be available to the whole team as a single invocation. What is the right mechanism?

**기존** 반복되는 여러 단계의 리뷰 절차를 팀 전체가 단일 호출로 사용할 수 있어야 한다. 올바른 메커니즘은 무엇인가?

**신규** 여러 단계로 된 검토 절차를 반복해서 쓰는데, 팀 전체가 한 번에 호출할 수 있게 하려면 어떤 방법이 맞는가?

- A. 기존: 단계를 설명하는 공유 문서
  - 신규: 단계를 설명한 공유 문서
- B. 기존: 더 긴 CLAUDE.md
  - 신규: 더 길어진 CLAUDE.md
- C. 기존: 저장된 채팅 transcript
  - 신규: 저장해 둔 채팅 기록
- D. 기존: 저장소에 커밋된 커스텀 slash command 또는 skill
  - 신규: 저장소에 커밋한 custom slash command 또는 skill

**해설 EN** Repeatable team procedures belong in committed commands or skills, not prose

**해설 기존** 반복 가능한 팀 절차는 산문이 아니라 커밋된 command나 skill에 속한다

**해설 신규** 팀이 반복하는 절차는 글로 풀어 쓰지 말고 커밋한 command나 skill로 두어야 한다.

## CCAR-F-Amey-Thakur-0020

**EN** A skill and a subagent could both address a need. What decides between them?

**기존** skill과 subagent 모두 하나의 필요를 해결할 수 있다. 둘 사이를 결정하는 것은 무엇인가?

**신규** skill과 subagent 중 어느 쪽으로도 해결할 수 있는 요구가 있다. 둘 중 무엇으로 정할지는 무엇이 결정하는가?

- A. 기존: skill이 항상 더 낫다
  - 신규: skill이 항상 더 낫다
- B. 기존: 그 필요가 재사용 가능한 노하우인지, 자체 컨텍스트를 가진 격리된 작업 흐름인지
  - 신규: 그 요구가 재사용할 노하우인지, 자체 context를 가진 독립된 작업 흐름인지
- C. 기존: 작업이 긴지 여부
  - 신규: 작업이 긴지 아닌지
- D. 기존: 저장소에 이미 CLAUDE.md가 있는지 여부
  - 신규: 저장소에 이미 CLAUDE.md가 있는지

**해설 EN** **B.** The two solve different problems: a skill packages reusable procedure, a subagent isolates context. A blanket preference (A), duration (C), and existing files (D) do not address that distinction.

**해설 기존** **B.** 둘은 서로 다른 문제를 푼다. skill은 재사용 가능한 절차를 패키징하고, subagent는 컨텍스트를 격리한다. 일괄적인 선호(A), 기간(C), 기존 파일(D)은 이 구분을 다루지 않는다.

**해설 신규** **B.** 둘은 푸는 문제가 다르다. skill은 재사용할 절차를 묶어 두는 것이고, subagent는 context를 격리하는 것이다. 무조건 한쪽을 선호하는 것(A), 작업 길이(C), 기존 파일 유무(D)는 이 차이와 관계가 없다.

## CCAR-F-Amey-Thakur-0051

**EN** A pipeline has four steps whose order never varies and whose outputs are each checkable. What should it be?

**기존** 파이프라인에 순서가 절대 바뀌지 않고 각 출력을 검사할 수 있는 네 단계가 있다. 무엇이어야 하는가?

**신규** 순서가 바뀌지 않고 각 단계의 출력을 검증할 수 있는 4단계 pipeline이 있다. 어떻게 구성해야 하는가?

- A. 기존: 매 실행을 계획하는 에이전트
  - 신규: 실행할 때마다 계획을 세우는 agent
- B. 기존: 단계당 하나씩, 네 개의 에이전트
  - 신규: 단계마다 하나씩, agent 4개
- C. 기존: 정의된 지점에서 모델을 호출하는 결정적 워크플로
  - 신규: 정해진 지점에서만 모델을 호출하는 deterministic workflow
- D. 기존: 네 단계를 모두 다루는 단일 프롬프트
  - 신규: 네 단계를 모두 담은 prompt 하나

**해설 EN** A known fixed order is encoded rather than rediscovered, which is cheaper and testable per step. Runtime planning (A, B) adds nondeterminism, and one prompt (D) removes the checkpoints

**해설 기존** 알려진 고정 순서는 다시 알아내는 대신 인코딩하며, 그러면 더 저렴하고 단계별로 테스트할 수 있다. 런타임 계획(A, B)은 비결정성을 더하고, 하나의 프롬프트(D)는 검사 지점을 없앤다

**해설 신규** 순서가 고정돼 있다면 매번 새로 찾아내게 하지 말고 코드로 박아 두는 편이 비용도 적고 단계별로 테스트하기도 쉽다. 실행 중에 계획을 세우면(A, B) 비결정성이 생기고, prompt 하나로 합치면(D) 중간 검증 지점이 사라진다.

## CCAR-F-Amey-Thakur-0007

**EN** The automated reviewer flags dozens of trivial style nits per pull request, and engineers have started ignoring it. Which change addresses the false-positive problem the way the blueprint suggests?

**기존** 자동 리뷰어가 pull request마다 사소한 스타일 지적을 수십 개씩 표시해서 엔지니어들이 무시하기 시작했다. blueprint가 제안하는 방식으로 오탐(false positive) 문제를 해결하는 변경은 무엇인가?

**신규** 자동 리뷰어가 pull request마다 사소한 스타일 지적을 수십 개씩 내놓아서 엔지니어들이 리뷰어를 무시하기 시작했다. blueprint가 제안하는 방식으로 false positive 문제를 해결하는 변경은 무엇인가?

- A. 기존: 프롬프트에 명시적인 리뷰 기준을 정의한다: 무엇을 표시하고 무엇을 무시할지, 심각도 기준선, 그리고 범위 안과 범위 밖 발견 사항에 대한 몇 가지 구체적인 예시를 포함한다
  - 신규: prompt에 명확한 리뷰 기준을 정의한다. 무엇을 지적하고 무엇을 무시할지, 심각도 기준선을 적고, 지적 대상에 해당하는 사례와 해당하지 않는 사례를 보여 주는 예시도 몇 개 넣는다
- B. 기존: 리뷰를 두 번 실행하고 두 번 모두 나타나는 발견 사항만 게시한다
  - 신규: 리뷰를 두 번 돌려서 두 번 다 나온 지적만 게시한다
- C. 기존: 리뷰어를 pull request당 세 개의 발견 사항으로 제한한다
  - 신규: 리뷰어가 pull request당 지적을 최대 세 개까지만 하게 제한한다
- D. 기존: 모든 발견 사항을 아무도 읽지 않는 채널로 보낸다
  - 신규: 모든 지적을 아무도 읽지 않는 채널로 보낸다

**해설 EN** **A.** Precision comes from explicit criteria and few-shot examples that draw the boundary between signal and noise. Double-running (B) filters randomness but not systematic nit-picking, an arbitrary cap (C) drops real findings on bad days, and (D) is surrender.

**해설 기존** **A.** 정밀도는 신호와 잡음의 경계를 그어 주는 명시적 기준과 few-shot 예시에서 나온다. 두 번 실행(B)은 무작위성은 걸러내지만 체계적인 사소한 지적은 걸러내지 못하고, 임의의 상한(C)은 상태가 나쁜 날 실제 발견 사항을 버리며, (D)는 포기이다.

**해설 신규** **A.** 정밀도는 명확한 기준과 few-shot 예시로 신호와 잡음의 경계를 그어 줄 때 나온다. 두 번 돌리면(B) 무작위성은 걸러져도 늘 반복되는 사소한 지적은 그대로 남는다. 임의로 개수를 제한하면(C) 문제가 많은 날에는 진짜 지적까지 버려진다. (D)는 문제를 포기하는 것이다.

## CCAR-F-Amey-Thakur-0010

**EN** Your codebase-exploration agent has get_file_contents, read_source, and fetch_file tools that all read files, and it frequently picks poorly among them. What is the correct fix?

**기존** 코드베이스 탐색 에이전트에 모두 파일을 읽는 get_file_contents, read_source, fetch_file 도구가 있고, 이들 중에서 자주 잘못 고른다. 올바른 해결책은 무엇인가?

**신규** 코드베이스 탐색 agent에 get_file_contents, read_source, fetch_file 도구가 있다. 셋 다 파일을 읽는 도구라서 agent가 자주 엉뚱한 것을 고른다. 올바른 해결책은 무엇인가?

- A. 기존: 더 나은 네 번째 파일 읽기 도구를 추가한다
  - 신규: 더 나은 파일 읽기 도구를 네 번째로 추가한다
- B. 기존: 도구 목록으로 모델을 fine-tuning한다
  - 신규: 도구 목록으로 모델을 fine-tuning한다
- C. 기존: harness가 어떤 도구를 dispatch할지 무작위로 정한다
  - 신규: harness가 어떤 도구를 호출할지 무작위로 정하게 한다
- D. 기존: 파일 읽기 도구 하나로 통합하거나, 남기는 도구들에는 각각 언제 적용되는지를 정확히 밝히는 뚜렷이 구분되는 설명을 부여한다
  - 신규: 파일 읽기 도구를 하나로 합친다. 아니면 남기는 도구마다 어떤 경우에 쓰는지 분명히 구분되도록 description을 쓴다

**해설 EN** **D.** Tool selection runs on descriptions; overlapping tools with vague descriptions produce dithering. Consolidation or sharp differentiation is the documented cure. Adding overlap (A) worsens it, fine-tuning (B) is disproportionate, and randomization (C) institutionalizes the confusion.

**해설 기존** **D.** 도구 선택은 설명을 기반으로 이루어지며, 설명이 모호하고 겹치는 도구들은 망설임을 낳는다. 통합하거나 뚜렷하게 구분하는 것이 문서화된 해법이다. 겹치는 도구를 더하면(A) 악화되고, fine-tuning(B)은 과도하며, 무작위화(C)는 혼란을 제도화한다.

**해설 신규** **D.** 도구 선택은 description을 보고 이루어진다. 기능이 겹치는데 description까지 모호하면 agent가 갈팡질팡한다. 하나로 합치거나 description을 뚜렷하게 구분하는 것이 문서에 나온 해결법이다. 겹치는 도구를 더하면(A) 더 나빠지고, fine-tuning(B)은 과하며, 무작위 선택(C)은 혼란을 제도로 굳힐 뿐이다.

## CCAR-F-paullarionov-0053

**EN** Production metrics show your agent averages 4+ API loops per resolution. Analysis reveals Claude often requests `get_customer` and `lookup_order` in separate sequential turns even when both are needed initially. What is the most effective way to reduce the number of loops?

What is the most effective way to reduce loops?

**기존** 프로덕션 지표에 따르면 agent는 해결당 평균 4회 이상의 API 루프를 수행한다. 분석 결과, 처음부터 둘 다 필요한 경우에도 Claude가 `get_customer`와 `lookup_order`를 별도의 순차적 턴에서 요청하는 경우가 많다. 루프 수를 줄이는 가장 효과적인 방법은 무엇인가?

루프를 줄이는 가장 효과적인 방법은 무엇인가?

**신규** 운영 지표를 보니 agent가 한 건을 처리하는 데 평균 4번 넘게 API loop를 돈다. 분석해 보면 처음부터 둘 다 필요한 상황에서도 Claude가 `get_customer`와 `lookup_order`를 별도의 turn에 차례로 요청하는 경우가 많다. loop 수를 줄이는 가장 효과적인 방법은 무엇인가?

- A. 기존: 요청된 도구와 병렬로 필요할 가능성이 높은 도구를 자동으로 호출하고, 무엇을 요청했는지와 관계없이 모든 결과를 반환하는 speculative execution을 구현한다.
  - 신규: 요청된 도구가 무엇이든 필요할 만한 도구를 자동으로 병렬 호출하고, 요청 여부와 상관없이 모든 결과를 반환하는 speculative execution을 구현한다.
- B. 기존: Claude가 계획하고 도구 요청을 자연스럽게 결합할 여유를 더 갖도록 `max_tokens`를 늘린다.
  - 신규: `max_tokens`를 늘려서 Claude가 계획을 세울 여유를 주고, 도구 요청을 자연스럽게 합치도록 한다.
- C. 기존: 일반적인 조회 조합을 단일 호출로 묶는 `get_customer_with_orders` 같은 복합 도구를 만든다.
  - 신규: `get_customer_with_orders`처럼 자주 쓰는 조회 조합을 하나의 호출로 묶은 composite tool을 만든다.
- D. 기존: 도구 요청을 한 턴에 묶고 다음 API 호출 전에 모든 결과를 함께 반환하도록 프롬프트에서 Claude에 지시한다.
  - 신규: prompt에서 Claude에게 도구 요청을 한 turn에 묶어 보내라고 지시한다. 결과는 모두 함께 돌려주고 나서 다음 API 호출로 넘어간다.

**해설 EN** Prompting Claude to bundle related tool requests into a single turn leverages its native ability to request multiple tools at once. It directly fixes the sequential-call pattern with minimal architectural change.

**해설 기존** 관련된 도구 요청을 단일 턴으로 묶도록 Claude에 프롬프트하면 여러 도구를 한 번에 요청하는 Claude의 기본 능력을 활용한다. 아키텍처 변경을 최소화하면서 순차 호출 패턴을 직접 해결한다.

**해설 신규** 관련된 도구 요청을 한 turn에 묶으라고 prompt로 지시하면, Claude가 원래 갖고 있는 여러 도구 동시 요청 능력을 활용하게 된다. 구조를 거의 바꾸지 않고도 순차 호출 패턴을 바로 해결한다.

## CCAR-F-paullarionov-0035

**EN** Your team created a `/analyze-codebase` skill that performs deep code analysis—dependency scanning, test coverage counts, and code quality metrics. After running the command, team members report Claude becomes less responsive in the session and loses the context of the original task.

How do you most effectively fix this while keeping full analysis capabilities?

**기존** 팀이 의존성 스캔, 테스트 커버리지 집계, 코드 품질 지표 같은 심층 코드 분석을 수행하는 `/analyze-codebase` skill을 만들었다. 이 명령을 실행한 후 팀원들은 세션에서 Claude의 반응이 느려지고 원래 작업의 컨텍스트를 잃는다고 보고한다.

전체 분석 기능을 유지하면서 이를 가장 효과적으로 해결하는 방법은 무엇인가?

**신규** 팀에서 의존성 스캔, 테스트 coverage 집계, 코드 품질 지표 같은 심층 코드 분석을 수행하는 `/analyze-codebase` skill을 만들었다. 이 명령을 실행하고 나면 세션에서 Claude의 응답이 느려지고 원래 하던 작업의 context를 잃는다는 보고가 나온다.

분석 기능은 그대로 두면서 가장 효과적으로 고치는 방법은 무엇인가?

- A. 기존: skill frontmatter에 `context: fork`를 추가하여 분석을 격리된 subagent 컨텍스트에서 실행한다.
  - 신규: skill frontmatter에 `context: fork`를 추가해서 분석을 격리된 subagent context에서 실행한다.
- B. 기존: frontmatter에 `model: haiku`를 추가하여 분석에 더 빠르고 저렴한 모델을 사용한다.
  - 신규: frontmatter에 `model: haiku`를 추가해서 분석에 더 빠르고 저렴한 모델을 쓴다.
- C. 기존: skill을 각각 더 적은 출력을 내는 세 개의 더 작은 skill로 분할한다.
  - 신규: skill을 세 개로 쪼개서 각각 출력이 줄어들게 한다.
- D. 기존: 결과를 표시하기 전에 모든 결과를 짧은 요약으로 압축하도록 skill에 지침을 추가한다.
  - 신규: 결과를 보여 주기 전에 전부 짧은 요약으로 압축하라는 지시를 skill에 추가한다.

**해설 EN** `context: fork` runs the analysis in an isolated subagent context so the large output does not pollute the main session’s context window and Claude does not lose track of the original task. It preserves full analysis capability while keeping the main session responsive.

**해설 기존** `context: fork`는 분석을 격리된 subagent 컨텍스트에서 실행하므로 대량의 출력이 메인 세션의 context window를 오염시키지 않고 Claude가 원래 작업을 놓치지 않는다. 전체 분석 기능을 유지하면서 메인 세션의 반응성도 유지한다.

**해설 신규** `context: fork`는 분석을 격리된 subagent context에서 실행한다. 그래서 분량이 큰 출력이 메인 세션의 context window를 채우지 않고, Claude도 원래 작업을 놓치지 않는다. 분석 기능은 그대로 두면서 메인 세션의 응답성을 지킨다.

## CCAR-F-paullarionov-0007

**EN** Production logs show a persistent pattern: requests like “analyze the uploaded quarterly report” are routed to the web-search agent 45% of the time instead of the document analysis agent. Reviewing tool definitions, you find that the web-search agent has a tool `analyze_content` described as “analyzes content and extracts key information,” while the document analysis agent has a tool `analyze_document` described as “analyzes documents and extracts key information.” How should you fix the misrouting problem?

How should you fix the misrouting problem?

**기존** 프로덕션 로그에서 지속적인 패턴이 나타난다. “업로드된 분기 보고서를 분석해 줘” 같은 요청이 문서 분석 agent가 아니라 웹 검색 agent로 45%의 확률로 라우팅된다. 도구 정의를 검토해 보니, 웹 검색 agent에는 “콘텐츠를 분석하고 핵심 정보를 추출한다”라고 설명된 `analyze_content` 도구가 있고, 문서 분석 agent에는 “문서를 분석하고 핵심 정보를 추출한다”라고 설명된 `analyze_document` 도구가 있다. 이 잘못된 라우팅 문제를 어떻게 고쳐야 하는가?

이 잘못된 라우팅 문제를 어떻게 고쳐야 하는가?

**신규** 운영 로그에 계속 나타나는 패턴이 있다. “업로드한 분기 보고서를 분석해 줘”처럼 업로드한 보고서를 분석해 달라는 요청의 45%가 문서 분석 agent가 아니라 web-search agent로 간다. 도구 정의를 살펴보니 web-search agent에는 “analyzes content and extracts key information”이라는 description의 `analyze_content`가, 문서 분석 agent에는 “analyzes documents and extracts key information”이라는 description의 `analyze_document`가 있다.

잘못된 routing을 어떻게 고쳐야 하는가?

- A. 기존: coordinator가 위임을 결정하기 전에, 사용자가 업로드된 파일을 가리키는지 웹 콘텐츠를 가리키는지 탐지하는 사전 라우팅 분류기를 추가한다.
  - 신규: coordinator가 위임을 결정하기 전에, 사용자가 업로드한 파일을 가리키는지 web 콘텐츠를 가리키는지 판별하는 사전 routing 분류기를 추가한다.
- B. 기존: 웹 검색 도구의 이름을 `extract_web_results`로 바꾸고 설명을 “웹 검색과 URL에서 가져온 정보를 처리하여 반환한다”로 수정한다.
  - 신규: web-search 도구 이름을 `extract_web_results`로 바꾸고 description을 “processes and returns information retrieved from web search and URLs.”로 수정한다.
- C. 기존: 올바른 라우팅을 보여 주는 few-shot 예시를 coordinator 프롬프트에 추가한다. “사용자가 분기 보고서를 업로드함 → 문서 분석 agent”와 “사용자가 웹 페이지에 대해 질문함 → 웹 검색 agent”.
  - 신규: coordinator prompt에 올바른 routing을 보여 주는 few-shot 예시를 추가한다. “사용자가 분기 보고서를 업로드함 → 문서 분석 agent”, “사용자가 웹 페이지에 대해 물음 → web-search agent” 같은 식이다.
- D. 기존: 문서 분석 도구 설명에 “업로드된 PDF, Word 문서, 스프레드시트에 사용”과 같은 사용 예시를 추가하여 확장하고, 웹 검색 도구는 그대로 둔다.
  - 신규: web-search 도구는 그대로 두고, 문서 분석 도구의 description에 “Use for uploaded PDFs, Word docs, and spreadsheets,” 같은 사용 예를 추가해 확장한다.

**해설 EN** Renaming the web-search tool to `extract_web_results` and updating its description to explicitly reference web search and URLs directly removes the root cause by eliminating semantic overlap between the two tool names and descriptions. This makes each tool’s purpose unambiguous, enabling the coordinator to reliably distinguish document analysis from web search.

**해설 기존** 웹 검색 도구의 이름을 `extract_web_results`로 바꾸고 설명에 웹 검색과 URL을 명시적으로 언급하면, 두 도구의 이름과 설명 사이의 의미 중복이 사라져 근본 원인이 직접 제거된다. 이로써 각 도구의 목적이 모호하지 않게 되어 coordinator가 문서 분석과 웹 검색을 안정적으로 구별할 수 있다.

**해설 신규** web-search 도구 이름을 `extract_web_results`로 바꾸고 description에 web search와 URL을 분명히 적으면, 두 도구의 이름과 description이 의미상 겹치는 근본 원인이 사라진다. 각 도구의 용도가 분명해지므로 coordinator가 문서 분석과 web search를 안정적으로 구분할 수 있다.

## CCAR-F-paullarionov-0024

**EN** Your automated review generates test-case suggestions for each PR. Reviewing a PR that adds course completion tracking, Claude suggests 10 test cases, but developer feedback shows that 6 duplicate scenarios already covered by the existing test suite. What change most effectively reduces duplicate suggestions?

What change is most effective?

**기존** 자동화된 리뷰가 각 PR에 대한 테스트 케이스 제안을 생성한다. 강의 수료 추적 기능을 추가하는 PR을 리뷰하면서 Claude는 10개의 테스트 케이스를 제안하지만, 개발자 피드백에 따르면 그중 6개는 기존 테스트 스위트가 이미 다루는 시나리오와 중복된다. 중복 제안을 가장 효과적으로 줄이는 변경은 무엇인가?

어떤 변경이 가장 효과적인가?

**신규** 자동 리뷰가 PR마다 테스트 케이스를 제안한다. 수강 완료 추적 기능을 추가하는 PR에서 Claude가 테스트 케이스 10개를 제안했는데, 개발자 피드백을 보면 그중 6개는 기존 테스트 스위트가 이미 다루는 시나리오와 겹친다. 중복 제안을 가장 효과적으로 줄이는 변경은 무엇인가?

- A. 기존: Claude가 이미 어떤 시나리오가 다뤄지고 있는지 판단할 수 있도록 기존 테스트 파일을 컨텍스트에 포함한다.
  - 신규: 기존 테스트 파일을 context에 포함해서 Claude가 어떤 시나리오가 이미 다뤄지는지 파악하게 한다.
- B. 기존: Claude가 가장 가치 있는 케이스를 먼저 우선순위에 둘 것이라고 가정하고, 요청하는 제안 수를 10개에서 5개로 줄인다.
  - 신규: Claude가 가치 높은 케이스부터 고를 것이라고 가정하고, 제안 개수를 10개에서 5개로 줄인다.
- C. 기존: Claude가 성공 경로가 아니라 엣지 케이스와 오류 조건에만 집중하도록 지시하는 내용을 추가한다.
  - 신규: 성공 경로 말고 edge case와 오류 상황에만 집중하라는 지시를 추가한다.
- D. 기존: 설명이 기존 테스트 이름과 키워드 중복으로 일치하는 제안을 걸러내는 후처리를 구현한다.
  - 신규: 제안 설명이 기존 테스트 이름과 키워드가 겹치면 걸러 내는 후처리를 구현한다.

**해설 EN** Including the existing test file fixes the root cause of duplication: Claude can only avoid suggesting already-covered scenarios if it knows what tests already exist. This gives Claude the information needed to propose genuinely new, valuable tests.

**해설 기존** 기존 테스트 파일을 포함하는 것이 중복의 근본 원인을 해결한다. Claude는 어떤 테스트가 이미 존재하는지 알아야만 이미 다뤄진 시나리오를 제안하지 않을 수 있다. 이는 Claude에게 진정으로 새롭고 가치 있는 테스트를 제안하는 데 필요한 정보를 제공한다.

**해설 신규** 기존 테스트 파일을 context에 넣으면 중복의 근본 원인이 해결된다. Claude는 어떤 테스트가 이미 있는지 알아야 그 시나리오를 피할 수 있다. 그래야 정말 새롭고 가치 있는 테스트를 제안할 수 있다.

## CCAR-F-paullarionov-0038

**EN** You find that including 2–3 full endpoint implementation examples as context significantly improves consistency when generating new API endpoints. However, this context is useful only when creating new endpoints—not when debugging, reviewing code, or other work in the API directory.

Which configuration approach is most effective?

**기존** 새 API 엔드포인트를 생성할 때 2~3개의 전체 엔드포인트 구현 예시를 컨텍스트로 포함하면 일관성이 크게 향상된다는 것을 발견했다. 그러나 이 컨텍스트는 새 엔드포인트를 만들 때만 유용하며, API 디렉터리에서 디버깅, 코드 리뷰 또는 기타 작업을 할 때는 필요하지 않다.

가장 효과적인 구성 방식은 무엇인가?

**신규** 새 API endpoint를 만들 때 endpoint 구현 예시 2~3개를 전체 코드로 context에 넣으면 일관성이 눈에 띄게 좋아진다. 하지만 이 context는 새 endpoint를 만들 때만 쓸모 있고, 디버깅이나 코드 리뷰 등 API 디렉터리의 다른 작업에는 필요 없다.

어떤 설정 방식이 가장 효과적인가?

- A. 기존: 엔드포인트 예시와 패턴 문서를 프로젝트 CLAUDE.md에 추가하여 항상 사용할 수 있게 한다.
  - 신규: endpoint 예시와 패턴 문서를 프로젝트 CLAUDE.md에 추가해서 항상 쓸 수 있게 한다.
- B. 기존: 모든 생성 요청마다 코드를 프롬프트에 복사하여 엔드포인트 예시를 수동으로 참조한다.
  - 신규: 생성을 요청할 때마다 코드를 prompt에 복사해서 endpoint 예시를 직접 참조시킨다.
- C. 기존: 엔드포인트 예시를 포함하고 API 디렉터리에서 작업할 때 활성화되는 경로별 규칙을 `.claude/rules/api/`에 구성한다.
  - 신규: `.claude/rules/api/`에 endpoint 예시를 담은 path-specific rule을 설정해, API 디렉터리에서 작업할 때 활성화되게 한다.
- D. 기존: 엔드포인트 예시를 참조하고 패턴 준수 지침을 담은 skill을 만들어 슬래시 명령으로 필요할 때 호출한다.
  - 신규: endpoint 예시를 참조하고 패턴을 따르라는 지시를 담은 skill을 만들어, slash command로 필요할 때 호출한다.

**해설 EN** A skill invoked on demand loads the example context only when generating new endpoints, not during unrelated tasks like debugging or review. This keeps the main context clean while preserving high-quality generation when needed.

**해설 기존** 필요할 때 호출하는 skill은 새 엔드포인트를 생성할 때만 예시 컨텍스트를 로드하며, 디버깅이나 리뷰 같은 관련 없는 작업 중에는 로드하지 않는다. 이렇게 하면 메인 컨텍스트를 깨끗하게 유지하면서 필요할 때 고품질 생성을 유지할 수 있다.

**해설 신규** 필요할 때 호출하는 skill은 새 endpoint를 만들 때만 예시 context를 불러오고, 디버깅이나 리뷰 같은 다른 작업에서는 불러오지 않는다. 그래서 메인 context를 깨끗하게 유지하면서, 필요할 때는 높은 생성 품질을 얻을 수 있다.

## CCAR-F-preporato-0002

**EN** A retailer's support system uses a coordinator agent that receives each customer conversation and delegates to three subagents: an order-lookup agent with read-only order tools, a refund agent that can issue refunds, and a policy agent that searches the returns-policy knowledge base. Company policy: refunds above \$250 need a human's approval, and customers can come back to an open conversation within 7 days.

Which TWO events should trigger a handoff to a human agent? (Select TWO)

**기존** 한 소매업체의 지원 시스템은 각 고객 대화를 받아 세 개의 subagent에 위임하는 coordinator agent를 사용한다. 세 subagent는 읽기 전용 주문 도구를 가진 주문 조회 agent, 환불을 처리할 수 있는 환불 agent, 반품 정책 지식 베이스를 검색하는 정책 agent이다. 회사 정책: \$250를 초과하는 환불은 사람의 승인이 필요하며, 고객은 7일 이내에 열려 있는 대화로 돌아올 수 있다.

사람 상담원에게 넘기는 handoff를 유발해야 하는 두 가지 이벤트는 무엇인가? (두 개 선택)

**신규** 소매업체의 고객 지원 시스템에서 coordinator agent가 고객 대화를 하나씩 받아 subagent 세 개에 위임한다. subagent는 읽기 전용 주문 도구를 가진 주문 조회 agent, 환불을 실행할 수 있는 환불 agent, 반품 정책 지식 베이스를 검색하는 정책 agent다. 회사 정책상 \$250을 넘는 환불은 사람의 승인이 필요하고, 고객은 진행 중인 대화에 7일 안에 다시 들어올 수 있다.

사람 상담원에게 넘겨야 하는 이벤트는 무엇인가? (2개 선택)

- A. 기존: 고객의 질문에 답하는 데 도구 호출이 세 번 필요하다
  - 신규: 고객의 질문에 답하는 데 도구 호출이 세 번 필요하다
- B. 기존: 고객이 사람과 통화하기를 요청한다
  - 신규: 고객이 사람과 이야기하고 싶다고 요청한다
- C. 기존: 모델이 자격 판단에 대해 0.62의 confidence score를 보고한다
  - 신규: 모델이 자격 판정에 대해 신뢰도 점수 0.62를 보고한다
- D. 기존: 고객이 대문자로 글을 쓰며 정책이 보장하는 \$90 환불 건에 대해 몹시 화가 났다고 말한다
  - 신규: 고객이 대문자로 글을 써서, 정책상 환불 가능한 \$90 환불 건에 몹시 화가 났다고 말한다
- E. 기존: 고객이 정책이 보장하는 주문에 대해 \$400 환불을 요청한다
  - 신규: 고객이 정책상 환불 가능한 주문에 대해 \$400 환불을 요청한다

**해설 EN** An explicit request for a human (B) is a standing escalation trigger, and the \$400 refund (E) crosses the \$250 approval threshold, which makes the handoff mandatory under policy. Sentiment alone (D) is no trigger when the request sits inside clear policy; the agent can resolve it while acknowledging the frustration. Self-reported confidence (C) is poorly calibrated and makes an unreliable trigger. Task complexity (A) is the agent's job.

**해설 기존** 사람을 요청하는 명시적 요구(B)는 상시 적용되는 escalation 트리거이고, \$400 환불(E)은 \$250 승인 기준을 넘으므로 정책상 handoff가 필수이다. 요청이 명확한 정책 범위 안에 있다면 감정만으로는(D) 트리거가 되지 않는다. agent는 불만을 인정하면서 문제를 해결할 수 있다. 모델이 스스로 보고하는 confidence(C)는 보정이 잘 되어 있지 않아 신뢰할 수 없는 트리거이다. 작업의 복잡도(A)는 agent가 처리할 일이다.

**해설 신규** 사람과 연결해 달라는 명시적 요청(B)은 언제든 escalation 사유가 된다. \$400 환불(E)은 승인 기준인 \$250을 넘으므로 정책상 반드시 사람에게 넘겨야 한다. 요청이 명확한 정책 범위 안에 있다면 감정만으로는 사유가 되지 않는다. agent가 불만을 인정하면서 직접 처리하면 된다. 모델이 스스로 보고하는 신뢰도(C)는 보정이 잘 안 되어 있어서 trigger로 믿을 수 없다. 작업이 복잡한지(A)는 agent가 감당할 몫이다.

## CCAR-F-preporato-0018

**EN** A team requires that Claude never ends its work while the test suite is failing. Which hook enforces this?

**기존** 한 팀은 테스트 스위트가 실패하는 동안 Claude가 작업을 끝내지 않도록 요구한다. 어떤 hook이 이를 강제하는가?

**신규** 팀에서 테스트 스위트가 실패하는 동안에는 Claude가 작업을 끝내지 못하게 하려 한다. 어떤 hook으로 이를 강제하는가?

- A. 기존: 테스트를 실행하는 `SessionEnd` hook
  - 신규: 테스트를 실행하는 `SessionEnd` hook
- B. 기존: 테스트를 실행하고, 하나라도 실패하면 실패 내용을 stderr에 출력하면서 종료 코드 2로 종료하는 `Stop` hook
  - 신규: 테스트를 실행하고, 하나라도 실패하면 실패 내용을 stderr에 출력한 뒤 exit code 2로 종료하는 `Stop` hook
- C. 기존: 파일을 읽을 때마다 테스트를 실행하는 `PostToolUse` hook
  - 신규: 파일을 읽을 때마다 테스트를 실행하는 `PostToolUse` hook
- D. 기존: 각 프롬프트 전에 테스트를 실행하는 `UserPromptSubmit` hook
  - 신규: prompt를 제출하기 전에 매번 테스트를 실행하는 `UserPromptSubmit` hook

**해설 EN** Exit code 2 from a `Stop` hook prevents Claude from stopping and feeds the stderr text back, so Claude keeps working on the failures (B). `SessionEnd` (A) fires as the session closes and can't block anything. D tests before the work happens. C runs constantly at the wrong moment and can't stop Claude from finishing.

**해설 기존** `Stop` hook의 종료 코드 2는 Claude가 멈추지 못하게 하고 stderr 텍스트를 Claude에게 되돌려 주므로, Claude는 실패를 계속 해결한다(B). `SessionEnd`(A)는 session이 닫힐 때 발동하며 아무것도 막을 수 없다. D는 작업이 이루어지기 전에 테스트한다. C는 엉뚱한 시점에 끊임없이 실행되며 Claude가 끝내는 것을 막지 못한다.

**해설 신규** `Stop` hook이 exit code 2를 반환하면 Claude는 멈추지 못하고 stderr 내용을 전달받아 실패한 테스트를 계속 고친다(B). `SessionEnd`(A)는 세션이 닫히는 시점에 실행되므로 아무것도 막을 수 없다. D는 작업을 하기 전에 테스트하는 것이다. C는 엉뚱한 시점에 계속 실행될 뿐 Claude가 끝내는 것을 막지 못한다.

## CCAR-F-preporato-0008

**EN** A security team runs a nightly audit across 40 repositories. A coordinator spawns one scanner subagent per repository. Each scanner has `Read`, `Grep` and `Glob` plus a dependency-check tool. The coordinator merges the findings into one report for the morning stand-up and opens tickets for new critical issues.

The morning report said 'No critical issues found across all repositories.' The team later learns that six scanners hit their token budgets and skipped their largest files. What should the report format have required?

**기존** 한 보안 팀이 40개 저장소를 대상으로 매일 밤 감사를 실행한다. coordinator는 저장소당 하나씩 scanner subagent를 생성한다. 각 scanner는 `Read`, `Grep`, `Glob`과 의존성 검사 도구를 갖는다. coordinator는 결과를 하나의 보고서로 병합해 아침 스탠드업에 쓰고, 새로 발견된 critical 이슈에 대한 티켓을 연다.

아침 보고서에는 '모든 저장소에서 critical 이슈가 발견되지 않았다'고 적혀 있었다. 팀은 나중에 scanner 여섯 개가 token 예산에 도달해 가장 큰 파일들을 건너뛰었다는 사실을 알게 된다. 보고서 형식은 무엇을 요구했어야 하는가?

**신규** 보안팀이 저장소 40개를 대상으로 매일 밤 감사를 돌린다. coordinator가 저장소마다 scanner subagent를 하나씩 띄우고, 각 scanner는 `Read`, `Grep`, `Glob`과 의존성 점검 도구를 쓴다. coordinator는 결과를 합쳐 아침 stand-up용 보고서 하나로 만들고, 새로 발견된 치명적 문제는 티켓으로 올린다.

아침 보고서에는 '모든 저장소에서 치명적인 문제가 발견되지 않았다'고 적혀 있었다. 그런데 나중에 보니 scanner 여섯 개가 token budget을 다 써서 가장 큰 파일들을 건너뛰었다. 보고서 형식은 무엇을 요구했어야 하는가?

- A. 기존: 없다. scanner에 더 유능한 모델이 필요했을 뿐이다
  - 신규: 요구할 것은 없다. scanner에 더 성능 높은 모델이 필요했을 뿐이다
- B. 기존: 각 scanner의 더 긴 서술형 요약
  - 신규: scanner마다 더 긴 서술형 요약
- C. 기존: 각 scanner의 confidence score
  - 신규: scanner마다 신뢰도 점수
- D. 기존: 모든 scanner의 coverage 주석(검토한 파일, 사유와 함께 건너뛴 파일, coverage 개수)을 병합된 보고서에 포함하는 것
  - 신규: 모든 scanner의 coverage 표기(검토한 파일, 건너뛴 파일과 그 사유, coverage 수치)를 합친 보고서에도 그대로 싣는 것

**해설 EN** Without explicit coverage, 'no issues found' can't be told apart from 'no issues found in the part that ran.' D makes the gap visible so the skipped files can be queued for a focused pass. Self-reported confidence (C) is poorly calibrated and says nothing about what was skipped. A longer summary (B) adds words without the counts. A stronger model (A) can still hit a budget, and the report would still hide it.

**해설 기존** 명시적인 coverage가 없으면 '이슈가 발견되지 않았다'는 말을 '실행된 부분에서는 이슈가 발견되지 않았다'와 구별할 수 없다. D는 빈틈을 드러내어 건너뛴 파일을 집중 점검 대상으로 대기열에 올릴 수 있게 한다. 스스로 보고하는 confidence(C)는 보정이 잘 되어 있지 않고 무엇을 건너뛰었는지는 알려 주지 않는다. 더 긴 요약(B)은 개수 없이 말만 늘린다. 더 강력한 모델(A)도 예산에 도달할 수 있으며, 보고서는 여전히 그 사실을 숨길 것이다.

**해설 신규** coverage를 명시하지 않으면 '문제 없음'과 '실행된 부분에서는 문제 없음'을 구별할 수 없다. D는 빈틈을 눈에 보이게 해서, 건너뛴 파일을 따로 대기열에 넣고 집중 점검할 수 있게 한다. 스스로 보고하는 신뢰도(C)는 보정이 잘 안 되어 있고, 무엇을 건너뛰었는지도 알려 주지 않는다. 요약을 길게 쓰게 해도(B) 수치 없이 글만 늘어난다. 더 강한 모델(A)도 budget에 걸릴 수 있고, 그래도 보고서는 그 사실을 숨긴다.

## CCAR-F-preporato-0003

**EN** A retailer's support system uses a coordinator agent that receives each customer conversation and delegates to three subagents: an order-lookup agent with read-only order tools, a refund agent that can issue refunds, and a policy agent that searches the returns-policy knowledge base. Company policy: refunds above \$250 need a human's approval, and customers can come back to an open conversation within 7 days.

The policy agent's knowledge-base search sometimes fails because the search service times out, and sometimes finds nothing because no policy covers the case. Both situations currently return an empty list. How should the tool respond instead?

**기존** 한 소매업체의 지원 시스템은 각 고객 대화를 받아 세 개의 subagent에 위임하는 coordinator agent를 사용한다. 세 subagent는 읽기 전용 주문 도구를 가진 주문 조회 agent, 환불을 처리할 수 있는 환불 agent, 반품 정책 지식 베이스를 검색하는 정책 agent이다. 회사 정책: \$250를 초과하는 환불은 사람의 승인이 필요하며, 고객은 7일 이내에 열려 있는 대화로 돌아올 수 있다.

정책 agent의 지식 베이스 검색은 검색 서비스가 시간 초과되어 실패하기도 하고, 해당 사례를 다루는 정책이 없어서 아무것도 찾지 못하기도 한다. 현재는 두 경우 모두 빈 목록을 반환한다. 도구는 대신 어떻게 응답해야 하는가?

**신규** 소매업체의 고객 지원 시스템에서 coordinator agent가 고객 대화를 하나씩 받아 subagent 세 개에 위임한다. subagent는 읽기 전용 주문 도구를 가진 주문 조회 agent, 환불을 실행할 수 있는 환불 agent, 반품 정책 지식 베이스를 검색하는 정책 agent다. 회사 정책상 \$250을 넘는 환불은 사람의 승인이 필요하고, 고객은 진행 중인 대화에 7일 안에 다시 들어올 수 있다.

정책 agent의 지식 베이스 검색은 검색 서비스가 timeout되어 실패할 때도 있고, 어떤 정책도 해당 사례를 다루지 않아 아무것도 찾지 못할 때도 있다. 지금은 두 경우 모두 빈 목록을 반환한다. 도구는 어떻게 응답해야 하는가?

- A. 기존: 두 경우 모두 빈 목록을 계속 반환하고 agent가 재시도하도록 한다
  - 신규: 두 경우 모두 빈 목록을 계속 반환하고, agent가 재시도하게 둔다
- B. 기존: 시간 초과에는 구조화된 오류(오류 유형, retryable: true, 시도한 내용)를 반환하고, 일치 항목이 없는 경우에는 성공적인 빈 결과를 반환한다
  - 신규: timeout에는 structured error(error type, retryable: true, 시도한 작업)를 반환하고, 일치하는 정책이 없는 경우에는 성공으로 처리한 빈 결과를 반환한다
- C. 기존: agent가 항상 인용할 거리가 있도록 두 경우 모두 가장 비슷한 정책을 반환한다
  - 신규: 두 경우 모두 가장 비슷한 정책을 반환해서 agent가 항상 인용할 것이 있게 한다
- D. 기존: 두 경우 모두 예외를 발생시켜 coordinator가 대화를 종료하게 한다
  - 신규: 두 경우 모두 예외를 발생시켜 coordinator가 대화를 종료하게 한다

**해설 EN** B separates a transient failure from a valid empty result, and the two need different recovery: retry the search, or tell the customer no policy applies. With A, the agent can't tell an outage from a real answer and may report that no policy covers the case during an outage. D ends conversations over a recoverable timeout. C invents relevance, which leads the agent to cite a policy that doesn't apply.

**해설 기존** B는 일시적 실패와 유효한 빈 결과를 구분하며, 두 경우는 서로 다른 복구가 필요하다. 검색을 재시도하거나, 적용되는 정책이 없다고 고객에게 알리는 것이다. A에서는 agent가 장애와 실제 답을 구별하지 못해, 장애 중에 해당 사례를 다루는 정책이 없다고 보고할 수 있다. D는 복구 가능한 시간 초과 때문에 대화를 끝낸다. C는 없는 관련성을 만들어내며, 그 결과 agent가 적용되지 않는 정책을 인용하게 된다.

**해설 신규** B는 일시적 장애와 정상적인 빈 결과를 구분한다. 두 경우는 복구 방법이 다르다. 하나는 검색을 재시도하는 것이고, 다른 하나는 해당 정책이 없다고 고객에게 알리는 것이다. A에서는 agent가 장애와 실제 답을 구별하지 못해, 장애 중에 해당 정책이 없다고 보고할 수 있다. D는 복구할 수 있는 timeout 때문에 대화를 끝낸다. C는 없는 관련성을 만들어 내서, agent가 적용되지 않는 정책을 인용하게 된다.

## CCAR-F-preporato-0004

**EN** A retailer's support system uses a coordinator agent that receives each customer conversation and delegates to three subagents: an order-lookup agent with read-only order tools, a refund agent that can issue refunds, and a policy agent that searches the returns-policy knowledge base. Company policy: refunds above \$250 need a human's approval, and customers can come back to an open conversation within 7 days.

A customer returns four days later to continue a conversation about a pending refund. Separately, a supervisor wants to test a different resolution on a copy of that conversation without changing what the customer sees. Which pairing fits?

**기존** 한 소매업체의 지원 시스템은 각 고객 대화를 받아 세 개의 subagent에 위임하는 coordinator agent를 사용한다. 세 subagent는 읽기 전용 주문 도구를 가진 주문 조회 agent, 환불을 처리할 수 있는 환불 agent, 반품 정책 지식 베이스를 검색하는 정책 agent이다. 회사 정책: \$250를 초과하는 환불은 사람의 승인이 필요하며, 고객은 7일 이내에 열려 있는 대화로 돌아올 수 있다.

한 고객이 4일 뒤에 돌아와 보류 중인 환불에 관한 대화를 이어간다. 별도로, 한 감독자는 고객이 보는 내용을 바꾸지 않은 채 그 대화의 복사본에서 다른 해결 방식을 시험해 보려 한다. 어떤 조합이 적절한가?

**신규** 소매업체의 고객 지원 시스템에서 coordinator agent가 고객 대화를 하나씩 받아 subagent 세 개에 위임한다. subagent는 읽기 전용 주문 도구를 가진 주문 조회 agent, 환불을 실행할 수 있는 환불 agent, 반품 정책 지식 베이스를 검색하는 정책 agent다. 회사 정책상 \$250을 넘는 환불은 사람의 승인이 필요하고, 고객은 진행 중인 대화에 7일 안에 다시 들어올 수 있다.

한 고객이 나흘 뒤 다시 돌아와 보류 중인 환불에 관한 대화를 이어 가려 한다. 별도로, 상담 관리자는 고객 화면에 보이는 내용은 건드리지 않고 그 대화의 복사본으로 다른 해결 방식을 시험해 보려 한다. 어떤 조합이 맞는가?

- A. 기존: 둘 다 새 session을 시작하고 마지막 assistant 메시지를 각각의 system prompt에 붙여 넣는다
  - 신규: 둘 다 새 session을 시작하고, 마지막 assistant 메시지를 각 system prompt에 붙여 넣는다
- B. 기존: 고객에게는 session을 fork하고 감독자에게는 resume한다
  - 신규: 고객에게는 session을 fork하고, 관리자에게는 resume한다
- C. 기존: 둘 다 같은 session을 resume한다
  - 신규: 둘 다 같은 session을 resume한다
- D. 기존: 고객의 session을 resume해 전체 기록을 복원하고, 감독자용으로는 별도의 복사본을 fork한다
  - 신규: 고객의 session은 resume해서 전체 history를 복원하고, 관리자용으로는 복사본을 따로 fork한다

**해설 EN** Resuming continues a session with its history intact, which is what the returning customer needs. Forking creates an independent branch from the same history, and changes in the fork never flow back, which is what the supervisor needs. D matches both. B swaps the two. C lets the supervisor's experiment change the customer's conversation. A throws away most of the context and relies on one message to carry it.

**해설 기존** resume은 기록을 그대로 유지한 채 session을 이어가며, 돌아온 고객에게 필요한 것이 바로 이것이다. fork는 같은 기록에서 독립된 분기를 만들고 fork에서의 변경은 원래 session으로 되돌아가지 않으며, 감독자에게 필요한 것이 바로 이것이다. D가 둘 다 충족한다. B는 둘을 뒤바꿨다. C는 감독자의 실험이 고객의 대화를 바꾸게 한다. A는 context 대부분을 버리고 메시지 하나가 그 전부를 전달하기를 기대한다.

**해설 신규** resume은 history를 그대로 유지한 채 session을 이어 가는 것이라 돌아온 고객에게 필요하다. fork는 같은 history에서 독립된 분기를 만들며, 분기에서 바꾼 내용은 원래 session으로 돌아오지 않는다. 관리자에게 필요한 것이 이것이다. D는 둘 다 충족한다. B는 둘을 거꾸로 짝지었다. C는 관리자의 실험이 고객의 대화를 바꿔 버린다. A는 context 대부분을 버리고 메시지 하나에 의존한다.
