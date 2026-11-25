## CCAR-F-Amey-Thakur-0001

**EN** Your support agent resolves most tickets but sometimes loops indefinitely, re-calling lookup_order on the same order. What is the correct structural fix?

**기존** 지원 에이전트가 대부분의 티켓을 해결하지만, 가끔 같은 주문에 대해 `lookup_order`를 반복 호출하며 무한히 루프에 빠진다. 올바른 구조적 해결책은 무엇인가?

**신규** 고객 지원 agent가 대부분의 티켓은 해결하지만, 가끔 같은 주문에 `lookup_order`를 계속 다시 호출하며 무한 루프에 빠진다. 구조적으로 올바른 해결 방법은 무엇인가?

- A. 기존: 루프가 끝날 여유가 생기도록 max_tokens를 늘린다
  - 신규: 루프가 끝날 여유가 생기도록 max_tokens를 높인다
- B. 기존: lookup_order 도구를 제거한다
  - 신규: lookup_order 도구를 제거한다
- C. 기존: 명시적인 루프 종료 조건을 추가한다: 도구 반복 횟수에 상한을 두고, 동일한 호출의 반복을 감지하며, 진행이 정체되면 escalate_to_human으로 라우팅한다
  - 신규: 루프 종료 조건을 명시적으로 추가한다. 도구 호출 횟수에 상한을 두고, 똑같은 호출이 반복되는지 감지하며, 진전이 없으면 escalate_to_human으로 넘긴다
- D. 기존: temperature를 낮춘다
  - 신규: temperature를 낮춘다

**해설 EN** **C.** Agent loops need engineered termination: iteration budgets, repeated-call detection, and an escalation path when the agent cannot progress. Token budget (A) delays the symptom, removing a needed tool (B) breaks resolution, and temperature (D) does not bound iteration.

**해설 기존** **C.** 에이전트 루프에는 설계된 종료 장치가 필요하다. 반복 횟수 예산, 반복 호출 감지, 에이전트가 진행하지 못할 때의 escalation 경로가 그것이다. 토큰 예산(A)은 증상을 늦출 뿐이고, 필요한 도구를 제거하면(B) 문제 해결이 불가능해지며, temperature(D)는 반복 횟수를 제한하지 않는다.

**해설 신규** **C.** agent 루프에는 종료 장치를 설계해 넣어야 한다. 반복 횟수 예산, 반복 호출 감지, agent가 더 진행하지 못할 때 쓰는 escalation 경로가 그런 장치다. 토큰 한도를 늘리면(A) 증상이 늦게 나타날 뿐이다. 필요한 도구를 없애면(B) 해결 자체가 불가능해진다. temperature(D)는 반복 횟수를 제한하지 못한다.

## CCAR-F-Amey-Thakur-0002

**EN** process_refund currently accepts any amount. Support policy caps agent-initiated refunds at $200; larger refunds need a human. Where does that rule belong?

**기존** process_refund는 현재 어떤 금액이든 받아들인다. 지원 정책상 에이전트가 시작하는 환불은 $200로 제한되며, 그보다 큰 환불은 사람이 처리해야 한다. 이 규칙은 어디에 두어야 하는가?

**신규** process_refund는 현재 금액에 상관없이 환불을 처리한다. 지원 정책상 agent가 직접 시작하는 환불은 $200까지만 허용하고, 그보다 큰 환불은 사람이 처리해야 한다. 이 규칙은 어디에 두어야 하는가?

- A. 기존: 시스템 프롬프트에 강하게 표현하여 둔다
  - 신규: system prompt에 단호한 어조로 적는다
- B. 기존: 정책을 읽으므로 모델의 추론에 맡긴다
  - 신규: 모델이 정책을 읽고 스스로 판단하도록 맡긴다
- C. 기존: 분기별 직원 교육에 둔다
  - 신규: 분기별 직원 교육에서 알려 준다
- D. 기존: 도구 계층에서 강제한다: 도구가 상한을 넘는 금액을 구조화된 오류로 거부하고, hook 또는 도구 자체가 더 큰 건을 escalation으로 라우팅한다
  - 신규: 도구 계층에서 강제한다. 한도를 넘는 금액은 도구가 구조화된 오류로 거부하고, hook이나 도구 자체가 더 큰 건을 escalation으로 넘긴다

**해설 EN** **D.** Hard policy limits are enforced deterministically at the tool boundary, not requested of the model. Prompt phrasing (A) and model reasoning (B) are probabilistic where the requirement is absolute, and training (C) does not constrain the agent at all.

**해설 기존** **D.** 엄격한 정책 한도는 모델에게 요청하는 것이 아니라 도구 경계에서 결정적으로 강제한다. 프롬프트 표현(A)과 모델의 추론(B)은 확률적인 반면 요구 사항은 절대적이며, 교육(C)은 에이전트를 전혀 제약하지 않는다.

**해설 신규** **D.** 반드시 지켜야 하는 정책 한도는 모델에게 부탁하는 것이 아니라 도구 경계에서 결정적으로 강제해야 한다. prompt 문구(A)와 모델의 판단(B)은 확률적인데, 이 요구사항은 예외가 없어야 한다. 직원 교육(C)은 agent를 전혀 제약하지 못한다.

## CCAR-F-Amey-Thakur-0003

**EN** Your coordinator delegates to search, analysis, and report subagents. Final reports cite sources that do not support their claims, though each subagent behaves sensibly alone. What is the most likely architectural cause?

**기존** coordinator가 검색, 분석, 보고서 subagent에게 작업을 위임한다. 각 subagent는 단독으로는 제대로 동작하는데도, 최종 보고서가 주장을 뒷받침하지 않는 출처를 인용한다. 가장 가능성이 높은 아키텍처상의 원인은 무엇인가?

**신규** coordinator가 search, analysis, report subagent에게 일을 나눠 맡긴다. 각 subagent는 단독으로 보면 제대로 동작하는데, 최종 보고서의 인용 출처가 주장을 뒷받침하지 못한다. 가장 가능성이 높은 아키텍처상의 원인은 무엇인가?

- A. 기존: handoff 과정에서 출처 정보(provenance)가 사라진다: 발견 내용과 그 출처가 구조화된 형태로 함께 전달되지 않아, 보고서 작성자가 추측으로 주장과 인용을 짝짓는다
  - 신규: handoff 과정에서 출처 정보(provenance)가 사라진다. 조사 결과와 그 출처가 구조화된 형태로 함께 전달되지 않아, report 작성 단계가 주장과 인용을 짐작으로 짝지으려 한다
- B. 기존: 보고서 subagent의 모델이 너무 작다
  - 신규: report subagent의 모델이 너무 작다
- C. 기존: 웹은 신뢰할 수 없다
  - 신규: 웹 자료를 믿을 수 없다
- D. 기존: 너무 많은 subagent가 병렬로 실행된다
  - 신규: 병렬로 실행되는 subagent가 너무 많다

**해설 EN** **A.** In multi-agent pipelines, provenance survives only if the handoff format carries claim and source together. That failure mode produces exactly this symptom while every stage looks locally fine. Model size (B), source quality (C), and parallelism (D) do not explain correct facts paired with wrong citations.

**해설 기존** **A.** 멀티 에이전트 파이프라인에서 provenance는 handoff 형식이 주장과 출처를 함께 담을 때만 유지된다. 이 실패 양상은 각 단계가 국소적으로는 모두 정상으로 보이는 상태에서 정확히 이런 증상을 만든다. 모델 크기(B), 출처 품질(C), 병렬성(D)은 올바른 사실이 잘못된 인용과 짝지어지는 현상을 설명하지 못한다.

**해설 신규** **A.** multi-agent 파이프라인에서는 handoff 형식이 주장과 출처를 함께 담아야 출처 정보가 살아남는다. 이 문제가 생기면 각 단계는 따로 볼 때 멀쩡한데도 바로 이런 증상이 나타난다. 모델 크기(B), 출처의 품질(C), 병렬 실행(D)으로는 사실은 맞는데 인용만 틀린 현상을 설명할 수 없다.

## CCAR-F-Amey-Thakur-0004

**EN** The analysis subagent returns 30,000-token document dumps to the coordinator, which then fails on context limits. What is the right fix?

**기존** 분석 subagent가 30,000 토큰짜리 문서 덤프를 coordinator에게 반환하고, coordinator는 컨텍스트 한도 때문에 실패한다. 올바른 해결책은 무엇인가?

**신규** analysis subagent가 30,000 token짜리 문서 원문을 coordinator에게 그대로 돌려보내고, coordinator는 context 한도 때문에 실패한다. 올바른 해결 방법은 무엇인가?

- A. 기존: coordinator에게 더 큰 컨텍스트 윈도우를 준다
  - 신규: coordinator에게 더 큰 context window를 준다
- B. 기존: subagent가 구조화된 추출 결과, 즉 인용과 신뢰도를 갖춘 발견 내용을 반환하게 하고, 전체 문서는 subagent의 컨텍스트나 scratchpad 파일에 둔다
  - 신규: subagent가 인용과 신뢰도를 붙인 조사 결과를 구조화된 발췌본으로 돌려보내게 하고, 문서 전문은 subagent의 context나 scratchpad 파일에 남긴다
- C. 기존: coordinator가 가장 오래된 메시지를 조용히 버리게 한다
  - 신규: coordinator가 가장 오래된 메시지를 말없이 버리게 한다
- D. 기존: 분석을 두 번 실행하고 더 짧은 답을 택한다
  - 신규: 분석을 두 번 실행해서 더 짧은 답을 택한다

**해설 EN** **B.** Context isolation is the point of subagent delegation: raw bulk stays at the edge, distilled results travel. A larger window (A) postpones the failure, silent dropping (C) loses arbitrary information, and rerunning (D) changes nothing structural.

**해설 기존** **B.** 컨텍스트 격리가 subagent 위임의 핵심이다. 원본 대량 데이터는 가장자리에 두고, 정제된 결과만 이동한다. 더 큰 윈도우(A)는 실패를 미룰 뿐이고, 조용한 삭제(C)는 임의의 정보를 잃으며, 재실행(D)은 구조적으로 아무것도 바꾸지 않는다.

**해설 신규** **B.** subagent에게 일을 맡기는 이유가 context 격리다. 방대한 원본은 바깥쪽에 두고 정리된 결과만 전달한다. 더 큰 window(A)는 실패를 미룰 뿐이고, 말없이 버리면(C) 어떤 정보가 사라질지 알 수 없다. 다시 실행해도(D) 구조는 달라지지 않는다.

## CCAR-F-Amey-Thakur-0005

**EN** Your monorepo has frontend and backend directories with different conventions, and one team-wide rule about commit style. Where does each piece of configuration belong?

**기존** 모노레포에 서로 다른 규약을 가진 frontend와 backend 디렉터리가 있고, 커밋 스타일에 관한 팀 전체 규칙이 하나 있다. 각 설정은 어디에 두어야 하는가?

**신규** monorepo에 frontend와 backend 디렉터리가 있고 두 곳의 컨벤션이 서로 다르며, 팀 전체에 적용할 commit 스타일 규칙도 하나 있다. 각 설정은 어디에 두어야 하는가?

- A. 기존: 모든 것을 루트 CLAUDE.md 하나에 둔다
  - 신규: 전부 루트의 CLAUDE.md 하나에 둔다
- B. 기존: 각 엔지니어의 개인 사용자 수준 CLAUDE.md에 둔다
  - 신규: 엔지니어 각자의 user-level CLAUDE.md에 둔다
- C. 기존: 커밋 규칙은 프로젝트 수준 CLAUDE.md에 두고, 영역별 규약은 일치하는 파일을 다룰 때만 로드되는 `.claude/rules/` 아래의 경로 범위 규칙(path-scoped rules)에 둔다
  - 신규: commit 규칙은 project-level CLAUDE.md에 두고, 영역별 컨벤션은 `.claude/rules/` 아래에 경로를 지정한 규칙으로 두어 해당 파일을 다룰 때만 로드되게 한다
- D. 기존: README에서 링크한 위키 페이지에 둔다
  - 신규: README에 링크한 wiki 페이지에 둔다

**해설 EN** **C.** The hierarchy exists for exactly this: shared rules at project scope, conditional conventions path-scoped so context is spent only where relevant. One root file (A) loads everything everywhere, personal files (B) diverge per engineer, and a wiki (D) never reaches the model.

**해설 기존** **C.** 계층 구조는 바로 이런 경우를 위해 존재한다. 공유 규칙은 프로젝트 범위에 두고, 조건부 규약은 경로 범위로 지정해 관련 있는 곳에서만 컨텍스트를 소비한다. 루트 파일 하나(A)는 모든 곳에서 모든 것을 로드하고, 개인 파일(B)은 엔지니어마다 달라지며, 위키(D)는 모델에 전혀 도달하지 않는다.

**해설 신규** **C.** 이 계층 구조는 바로 이런 경우를 위한 것이다. 공유 규칙은 project 범위에 두고, 조건부 컨벤션은 경로로 범위를 좁혀 필요한 곳에서만 context를 쓰게 한다. 루트 파일 하나(A)는 모든 곳에서 전부 로드된다. 개인 파일(B)은 엔지니어마다 달라진다. wiki(D)는 모델에게 전달되지 않는다.

## CCAR-F-Amey-Thakur-0006

**EN** Your CI job runs Claude Code to review pull requests, and the pipeline must parse the results mechanically. Which invocation is correct?

**기존** CI 작업이 Claude Code를 실행해 pull request를 리뷰하며, 파이프라인은 결과를 기계적으로 파싱해야 한다. 올바른 호출 방식은 무엇인가?

**신규** CI 작업에서 Claude Code로 pull request를 리뷰하는데, 파이프라인이 결과를 기계적으로 파싱해야 한다. 올바른 실행 방법은 무엇인가?

- A. 기존: 사람이 출력을 CI에 복사해 넣는 interactive 모드
  - 신규: interactive mode로 실행하고, 사람이 출력을 CI에 복사해 넣는다
- B. 기존: 자동화에 더 안전한 plan mode
  - 신규: automation에는 더 안전한 plan mode를 쓴다
- C. 기존: 사람이 읽는 transcript를 grep하는 셸 스크립트
  - 신규: 사람이 읽는 transcript를 grep하는 shell script를 쓴다
- D. 기존: -p를 사용하는 non-interactive 모드에 --output-format json과 스키마를 지정하여, 리뷰가 기계가 읽을 수 있고 검증된 출력으로 도착하게 한다
  - 신규: `-p`로 non-interactive mode를 쓰고 `--output-format json`과 schema를 지정해, 리뷰가 검증된 기계 판독용 출력으로 나오게 한다

**해설 EN** **D.** Headless CI use is what -p with JSON output and a schema is for: deterministic invocation, parseable results. A human in the loop (A) is not CI, plan mode (B) is a review gate for interactive work rather than an output format, and grepping prose (C) breaks on the first wording change.

**해설 기존** **D.** 헤드리스 CI 사용은 JSON 출력 및 스키마와 함께 쓰는 -p가 존재하는 이유이다. 결정적인 호출과 파싱 가능한 결과를 제공한다. 사람이 개입하는 방식(A)은 CI가 아니고, plan mode(B)는 출력 형식이 아니라 interactive 작업을 위한 검토 관문이며, 산문을 grep하는 방식(C)은 문구가 처음 바뀌는 순간 깨진다.

**해설 신규** **D.** CI처럼 사람 없이 돌리는 환경에서는 `-p`에 JSON 출력과 schema를 함께 쓴다. 호출 방식이 일정하고 결과를 그대로 파싱할 수 있기 때문이다. 사람이 끼어드는 방식(A)은 CI가 아니다. plan mode(B)는 interactive 작업의 검토 단계이지 출력 형식이 아니다. 문장을 grep하는 방식(C)은 문구가 조금만 바뀌어도 깨진다.

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

## CCAR-F-Amey-Thakur-0008

**EN** Invoices sometimes lack a purchase-order number, and your extraction schema must handle that honestly while catching real misses. What is the right schema design?

**기존** 송장에 구매 주문 번호가 없는 경우가 가끔 있으며, 추출 스키마는 이를 정직하게 처리하면서도 실제 누락은 잡아내야 한다. 올바른 스키마 설계는 무엇인가?

**신규** 송장에 구매 주문(PO) 번호가 없는 경우가 가끔 있다. 추출 schema는 이를 정직하게 처리하면서도 실제로 놓친 경우는 잡아내야 한다. 올바른 schema 설계는 무엇인가?

- A. 기존: 아무것도 놓치지 않도록 모든 필드를 필수로 만든다
  - 신규: 놓치는 것이 없도록 모든 필드를 required로 한다
- B. 기존: purchase_order를 nullable로 만들어 부재를 null로 기록하고, 문서 유형상 필요한 경우에는 값이 존재하는지 검증한다
  - 신규: purchase_order를 nullable로 만들어 값이 없으면 null로 기록하고, 문서 유형상 필요한 경우에는 값이 있는지 따로 검증한다
- C. 기존: 검증 오류를 피하도록 모든 것을 선택 사항으로 만든다
  - 신규: 검증 오류를 피하려고 모든 필드를 optional로 한다
- D. 기존: 값이 없을 때 모델이 그럴듯한 번호를 만들어 내게 한다
  - 신규: 번호가 없으면 모델이 그럴듯한 번호를 만들어 넣게 한다

**해설 EN** **B.** Schema design encodes reality: genuinely optional data is nullable, and conditional requirements are validated downstream. All-required (A) forces fabrication or failure on legitimate documents, all-optional (C) blinds you to true misses, and invention (D) is data corruption.

**해설 기존** **B.** 스키마 설계는 현실을 반영한다. 정말로 선택적인 데이터는 nullable로 두고, 조건부 요구 사항은 후속 단계에서 검증한다. 모두 필수(A)는 정당한 문서에서 조작이나 실패를 강요하고, 모두 선택(C)은 진짜 누락을 못 보게 하며, 값을 만들어 내는 것(D)은 데이터 손상이다.

**해설 신규** **B.** schema는 현실을 그대로 반영해야 한다. 실제로 없을 수 있는 데이터는 nullable로 두고, 조건부로 필요한 항목은 후단에서 검증한다. 전부 required(A)이면 정상 문서에서도 값을 지어내거나 실패하게 된다. 전부 optional(C)이면 정말로 놓친 경우를 알아채지 못한다. 값을 지어내는 것(D)은 데이터 오염이다.

## CCAR-F-Amey-Thakur-0009

**EN** Your pipeline reports 98% field accuracy, measured on the documents the schema validated cleanly. An auditor calls the number misleading. Why?

**기존** 파이프라인이 스키마 검증을 깨끗하게 통과한 문서에서 측정한 결과 98%의 필드 정확도를 보고한다. 감사자는 이 수치가 오해의 소지가 있다고 말한다. 그 이유는 무엇인가?

**신규** 파이프라인이 필드 정확도 98%를 보고하는데, 이 수치는 schema 검증을 문제없이 통과한 문서만 대상으로 측정한 것이다. 감사 담당자는 이 수치가 오해를 부른다고 말한다. 그 이유는 무엇인가?

- A. 기존: 정확도는 가장 어려운 문서에서만 측정해야 한다
  - 신규: 정확도는 가장 어려운 문서에서만 측정해야 한다
- B. 기존: 98%는 업계 표준보다 낮다
  - 신규: 98%는 업계 표준보다 낮다
- C. 기존: 검증을 깨끗하게 통과한 문서는 편향된 표본이다: 정직한 측정은 검증에 실패했거나 간신히 통과한 문서를 포함해 모든 문서에서 추출한 레이블된 표본에서 나온다
  - 신규: 검증을 깨끗하게 통과한 문서는 편향된 표본이다. 정직한 측정은 검증에 실패했거나 간신히 통과한 문서까지 포함해 모든 문서에서 뽑은 라벨링 표본으로 해야 한다
- D. 기존: 필드 정확도는 실제 지표가 아니다
  - 신규: 필드 정확도는 실제로 쓰이는 지표가 아니다

**해설 EN** **C.** Measuring only where the system already succeeded inflates the estimate; calibration requires a labeled sample representative of the full input stream. Hardest-only (A) biases in the opposite direction, the standard claim (B) is invented, and (D) is false.

**해설 기존** **C.** 시스템이 이미 성공한 곳에서만 측정하면 추정치가 부풀려진다. 보정에는 전체 입력 스트림을 대표하는 레이블된 표본이 필요하다. 가장 어려운 문서만(A)은 반대 방향으로 편향되고, 표준이라는 주장(B)은 지어낸 것이며, (D)는 거짓이다.

**해설 신규** **C.** 시스템이 이미 성공한 곳만 측정하면 추정치가 부풀려진다. 보정하려면 전체 입력을 대표하는 라벨링 표본이 필요하다. 가장 어려운 문서만 측정하는 것(A)은 반대 방향으로 편향된다. 업계 표준 이야기(B)는 근거가 없고, (D)는 사실이 아니다.

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

## CCAR-F-Amey-Thakur-0011

**EN** A support workflow resolves tickets by looking up an account, checking entitlement, and drafting a reply, always in that order. Which architecture is correct?

**기존** 지원 워크플로가 계정 조회, 자격(entitlement) 확인, 답변 초안 작성을 항상 이 순서로 수행하여 티켓을 해결한다. 올바른 아키텍처는 무엇인가?

**신규** 지원 workflow가 계정을 조회하고, 자격을 확인한 뒤, 답변 초안을 쓰는 순서로 티켓을 처리하며 이 순서는 항상 같다. 올바른 아키텍처는 무엇인가?

- A. 기존: 정의된 각 단계에서 모델을 호출하는 결정적 파이프라인
  - 신규: 정해진 각 단계에서 모델을 호출하는 deterministic pipeline
- B. 기존: 각 단계를 런타임에 결정하는 단일 에이전트
  - 신규: 각 단계를 runtime에 스스로 결정하는 단일 agent
- C. 기존: 서로 순서를 협상하는 세 개의 에이전트
  - 신규: 서로 순서를 협상하는 agent 세 개
- D. 기존: 세 단계를 모두 담은 하나의 프롬프트
  - 신규: 세 단계를 모두 담은 prompt 하나

**해설 EN** **A.** A known, fixed sequence should be encoded rather than rediscovered on every run, which makes it cheaper, faster, and testable step by step. Runtime decisions (B, C) add nondeterminism for no gain, and one prompt (D) removes the checkpoints between steps.

**해설 기존** **A.** 알려져 있고 고정된 순서는 매 실행마다 다시 알아내는 대신 코드로 인코딩해야 하며, 그러면 더 저렴하고 빠르며 단계별로 테스트할 수 있다. 런타임 결정(B, C)은 얻는 것 없이 비결정성만 더하고, 하나의 프롬프트(D)는 단계 사이의 검사 지점을 없앤다.

**해설 신규** **A.** 순서가 고정되어 있다면 매번 새로 찾아내게 하지 말고 코드로 정해 두어야 한다. 그러면 비용이 줄고 속도가 빨라지며 단계별로 테스트할 수 있다. runtime 결정(B, C)은 얻는 것 없이 비결정성만 더한다. prompt 하나(D)로 합치면 단계 사이의 checkpoint가 사라진다.

## CCAR-F-Amey-Thakur-0012

**EN** What is the strongest justification for splitting work across subagents?

**기존** 작업을 subagent들에게 나누는 것을 가장 강력하게 정당화하는 근거는 무엇인가?

**신규** 작업을 subagent로 나누는 가장 강력한 근거는 무엇인가?

- A. 기존: 작업에 단계가 많다
  - 신규: 작업의 단계가 많다
- B. 기존: 서로 다른 작업 흐름이 각각 자체 컨텍스트를 필요로 하며, 이를 섞으면 둘 다 품질이 떨어진다
  - 신규: 서로 다른 작업 흐름마다 자기만의 context가 필요하고, 섞이면 양쪽 모두 품질이 떨어진다
- C. 기존: subagent가 단일 에이전트보다 빠르다
  - 신규: subagent가 단일 agent보다 빠르다
- D. 기존: 출력을 여러 섹션으로 조립해야 한다
  - 신규: 출력을 여러 부분으로 나눠 조립해야 한다

**해설 EN** **B.** Subagents exist to isolate context, so the case for them is contamination between concerns rather than volume. Step count (A) and sectioned output (D) suit a workflow, and delegation usually adds latency rather than removing it (C).

**해설 기존** **B.** subagent는 컨텍스트를 격리하기 위해 존재하므로, 그 근거는 작업량이 아니라 관심사 사이의 오염이다. 단계 수(A)와 섹션별 출력(D)은 워크플로에 적합하고, 위임은 대개 지연을 없애기보다 더한다(C).

**해설 신규** **B.** subagent는 context를 격리하려고 쓰는 것이므로, 분량이 아니라 관심사끼리 context가 서로 섞여 오염되는 문제가 있을 때 subagent로 나누는 근거가 된다. 단계가 많거나(A) 출력이 여러 부분으로 이루어진 경우(D)는 workflow로 충분하다. 위임은 보통 지연 시간을 줄이기보다 늘린다(C).

## CCAR-F-Amey-Thakur-0013

**EN** An agent loops between two tools without converging. What is the most appropriate first control?

**기존** 에이전트가 두 도구 사이를 오가며 수렴하지 못하고 루프를 돈다. 가장 적절한 첫 번째 통제 수단은 무엇인가?

**신규** agent가 두 도구 사이를 오가기만 하고 결론에 이르지 못한다. 가장 먼저 적용할 적절한 통제 수단은 무엇인가?

- A. 기존: 더 많은 기록을 볼 수 있도록 컨텍스트 윈도우를 늘린다
  - 신규: 더 많은 기록을 볼 수 있도록 context window를 늘린다
- B. 기존: 더 큰 모델로 바꾼다
  - 신규: 더 큰 모델로 바꾼다
- C. 기존: 단계 상한을 두고 종료 조건을 명시적으로 정의한다
  - 신규: step 상한을 두고 종료 조건을 명시적으로 정의한다
- D. 기존: 두 도구 중 하나를 제거한다
  - 신규: 두 도구 중 하나를 제거한다

**해설 EN** **C.** Non-termination is bounded by an explicit stop condition and a hard ceiling, which contains cost and makes the failure visible. More context (A) and a larger model (B) do not guarantee convergence, and removing a tool (D) may break the task.

**해설 기존** **C.** 종료되지 않는 문제는 명시적인 중단 조건과 엄격한 상한으로 제한되며, 이는 비용을 억제하고 실패를 눈에 보이게 한다. 더 많은 컨텍스트(A)와 더 큰 모델(B)은 수렴을 보장하지 않으며, 도구를 제거하면(D) 작업이 깨질 수 있다.

**해설 신규** **C.** 끝나지 않는 문제는 명시적인 중단 조건과 강제 상한으로 막는다. 그러면 비용이 억제되고 실패도 눈에 보이게 된다. context를 늘리거나(A) 더 큰 모델을 쓴다고(B) 수렴이 보장되지는 않는다. 도구를 제거하면(D) 작업 자체가 안 될 수 있다.

## CCAR-F-Amey-Thakur-0014

**EN** Which property most increases the operational risk of an agentic design?

**기존** 에이전트 설계의 운영상 위험을 가장 크게 높이는 속성은 무엇인가?

**신규** agentic 설계의 운영 위험을 가장 크게 높이는 특성은 무엇인가?

- A. 기존: 둘 이상의 모델을 호출한다
  - 신규: 모델을 둘 이상 호출한다
- B. 기존: 구조화된 출력을 생성한다
  - 신규: 구조화된 출력을 만든다
- C. 기존: 1분보다 오래 실행된다
  - 신규: 1분보다 오래 실행된다
- D. 기존: 검사 지점 없이 되돌릴 수 없는 작업을 수행한다
  - 신규: checkpoint 없이 되돌릴 수 없는 작업을 수행한다

**해설 EN** **D.** Reversibility governs the cost of being wrong, which is the dominant risk in autonomous execution. Multiple models (A), structure (B), and duration (C) affect cost and complexity rather than blast radius.

**해설 기존** **D.** 되돌릴 수 있는지 여부가 틀렸을 때의 비용을 좌우하며, 이것이 자율 실행에서 지배적인 위험이다. 여러 모델(A), 구조(B), 지속 시간(C)은 피해 범위가 아니라 비용과 복잡성에 영향을 준다.

**해설 신규** **D.** 되돌릴 수 있는지가 틀렸을 때의 비용을 좌우하며, 자율 실행에서는 이것이 가장 큰 위험이다. 여러 모델(A), 구조(B), 실행 시간(C)은 비용과 복잡도에 영향을 줄 뿐 피해 범위와는 관계가 없다.

## CCAR-F-Amey-Thakur-0015

**EN** How should an agentic system handle a step whose result it cannot verify?

**기존** 에이전트 시스템은 결과를 검증할 수 없는 단계를 어떻게 처리해야 하는가?

**신규** agentic system은 결과를 검증할 수 없는 단계를 어떻게 처리해야 하는가?

- A. 기존: 검증할 수 없는 단계를 사람의 확인을 받도록 드러낸 뒤에 그에 따라 행동한다
  - 신규: 검증할 수 없는 단계를 드러내서, 그에 따라 행동하기 전에 사람이 확인하게 한다
- B. 기존: 모델이 대개 옳으므로 그대로 진행한다
  - 신규: 모델이 보통은 맞으니 그대로 진행한다
- C. 기존: 두 번의 실행 결과가 일치할 때까지 단계를 재시도한다
  - 신규: 두 번 실행한 결과가 일치할 때까지 재시도한다
- D. 기존: 단계를 기록하고 계속 진행한다
  - 신규: 그 단계를 기록하고 계속 진행한다

**해설 EN** **A.** An unverifiable result is exactly where human judgment belongs, before it is acted upon. Assuming correctness (B) and logging without stopping (D) both act on unchecked output, and agreement across runs (C) establishes consistency rather than truth.

**해설 기존** **A.** 검증할 수 없는 결과야말로 행동하기 전에 사람의 판단이 필요한 지점이다. 정확하다고 가정하는 것(B)과 멈추지 않고 기록만 하는 것(D)은 모두 검사되지 않은 출력에 따라 행동하며, 실행 간 일치(C)는 진실이 아니라 일관성을 입증한다.

**해설 신규** **A.** 검증할 수 없는 결과야말로 사람의 판단이 필요한 지점이고, 그 결과에 따라 행동하기 전에 확인해야 한다. 맞을 것이라고 가정하거나(B) 기록만 하고 멈추지 않는 것(D)은 둘 다 확인되지 않은 출력을 근거로 행동하는 것이다. 여러 번 실행해서 일치하는 것(C)은 일관성을 보여 줄 뿐 진실을 보장하지 않는다.

## CCAR-F-Amey-Thakur-0016

**EN** A team proposes an agent for a task where every input is well formed and every rule is known. What should the architect recommend?

**기존** 한 팀이 모든 입력이 올바른 형식이고 모든 규칙이 알려진 작업에 에이전트를 제안한다. 아키텍트는 무엇을 권해야 하는가?

**신규** 모든 입력의 형식이 일정하고 모든 규칙이 알려져 있는 작업에 한 팀이 agent를 쓰자고 제안한다. architect는 무엇을 권해야 하는가?

- A. 기존: 향후 유연성을 위해 에이전트
  - 신규: 나중에 유연하게 쓸 수 있도록 agent
- B. 기존: 결정적 구현을 하되, 모델 호출은 정말로 모호한 부분에만 쓴다
  - 신규: deterministic 구현을 쓰고, 모델 호출은 정말로 모호한 부분에만 남겨 둔다
- C. 기존: 단계 제한이 낮은 에이전트
  - 신규: step 한도를 낮게 건 agent
- D. 기존: 관심사 분리를 위한 멀티 에이전트 설계
  - 신규: 관심사 분리를 위한 multi-agent 설계

**해설 EN** **B.** Known rules over well-formed input are code, and using a model there buys nondeterminism at a price. Speculative flexibility (A), a constrained agent (C), and multiple agents (D) all keep the cost without the need.

**해설 기존** **B.** 올바른 형식의 입력에 대한 알려진 규칙은 코드이며, 여기에 모델을 쓰면 비결정성을 대가를 치르고 사게 된다. 추측에 근거한 유연성(A), 제약된 에이전트(C), 여러 에이전트(D)는 모두 필요 없이 비용만 유지한다.

**해설 신규** **B.** 형식이 일정한 입력에 알려진 규칙을 적용하는 일은 코드로 짜는 일이고, 여기에 모델을 쓰면 비용을 들여 비결정성만 얻는다. 미래의 유연성(A), 제한을 건 agent(C), 여러 agent(D)는 모두 필요 없는 비용을 그대로 떠안는다.

## CCAR-F-Amey-Thakur-0017

**EN** What most improves the debuggability of an agentic system in production?

**기존** 프로덕션에서 에이전트 시스템의 디버깅 용이성을 가장 크게 높이는 것은 무엇인가?

**신규** production에서 agentic system의 디버깅 용이성을 가장 크게 높이는 것은 무엇인가?

- A. 기존: 도구 수를 줄이는 것
  - 신규: 도구 수를 줄인다
- B. 기존: 모든 단계에 단일 모델을 사용하는 것
  - 신규: 모든 단계에 모델 하나만 쓴다
- C. 기존: 각 단계의 입력, 도구 호출, 출력을 trace로 기록하는 것
  - 신규: 각 단계의 입력, 도구 호출, 출력을 trace로 기록한다
- D. 기존: 단계 제한을 늘리는 것
  - 신규: step 한도를 늘린다

**해설 EN** **C.** A per-step trace is what makes a nondeterministic run reconstructable after the fact. Fewer tools (A) and one model (B) simplify without explaining, and a higher ceiling (D) makes failures longer rather than clearer.

**해설 기존** **C.** 단계별 trace는 비결정적인 실행을 사후에 재구성할 수 있게 해 준다. 더 적은 도구(A)와 하나의 모델(B)은 설명 없이 단순화만 하고, 더 높은 상한(D)은 실패를 더 명확하게가 아니라 더 길게 만든다.

**해설 신규** **C.** 단계별 trace가 있어야 비결정적인 실행을 나중에 재구성할 수 있다. 도구를 줄이거나(A) 모델을 하나로 통일하면(B) 단순해질 뿐 원인을 설명해 주지는 않는다. 한도를 높이면(D) 실패가 더 길어질 뿐 더 분명해지지는 않는다.

## CCAR-F-Amey-Thakur-0018

**EN** Where should conventions that apply to everyone working in a repository be recorded?

**기존** 저장소에서 작업하는 모든 사람에게 적용되는 규약은 어디에 기록해야 하는가?

**신규** 저장소에서 일하는 모든 사람에게 적용되는 컨벤션은 어디에 기록해야 하는가?

- A. 기존: 각 개발자의 개인 설정에
  - 신규: 각 개발자의 개인 설정
- B. 기존: pull request 템플릿에
  - 신규: pull request template
- C. 기존: 고정된 채팅 메시지에
  - 신규: 고정해 둔 채팅 메시지
- D. 기존: 저장소에 커밋된 CLAUDE.md에
  - 신규: 저장소에 commit한 CLAUDE.md

**해설 EN** **D.** Committed project memory is versioned, reviewable, and shared, which is what a team convention requires. Personal settings (A) do not propagate, and templates (B) and messages (C) are not read as working context.

**해설 기존** **D.** 커밋된 프로젝트 메모리는 버전이 관리되고, 검토할 수 있으며, 공유되므로 팀 규약이 요구하는 바를 충족한다. 개인 설정(A)은 전파되지 않고, 템플릿(B)과 메시지(C)는 작업 컨텍스트로 읽히지 않는다.

**해설 신규** **D.** commit한 project memory는 버전 관리되고 리뷰할 수 있으며 모두가 공유하므로 팀 컨벤션에 필요한 조건을 갖춘다. 개인 설정(A)은 다른 사람에게 퍼지지 않고, template(B)과 메시지(C)는 작업 context로 읽히지 않는다.

## CCAR-F-Amey-Thakur-0019

**EN** What distinguishes work suited to headless mode?

**기존** headless 모드에 적합한 작업을 구별하는 특징은 무엇인가?

**신규** headless mode에 적합한 작업은 어떤 특징이 있는가?

- A. 기존: 잘 정의되어 있고 반복 가능하므로 자동화에서 무인으로 실행될 수 있다
  - 신규: 정의가 분명하고 반복 가능해서 자동화 환경에서 사람 없이 실행할 수 있다
- B. 기존: 복잡하고 면밀한 감독이 필요하다
  - 신규: 복잡해서 세심한 감독이 필요하다
- C. 기존: 많은 도구가 필요하다
  - 신규: 도구가 많이 필요하다
- D. 기존: 긴 출력을 생성한다
  - 신규: 출력이 길다

**해설 EN** **A.** Headless execution suits bounded, repeatable work where no one is watching. Supervision (B) argues for interactive use, and tool count (C) and output length (D) do not determine suitability.

**해설 기존** **A.** headless 실행은 아무도 지켜보지 않는, 범위가 정해져 있고 반복 가능한 작업에 적합하다. 감독이 필요하다면(B) interactive 사용이 맞고, 도구 수(C)와 출력 길이(D)는 적합성을 결정하지 않는다.

**해설 신규** **A.** headless 실행은 범위가 정해져 있고 반복 가능하며 지켜보는 사람이 없는 작업에 맞는다. 감독이 필요하다면(B) interactive 사용이 맞다. 도구 수(C)와 출력 길이(D)는 적합성을 가르는 기준이 아니다.

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

## CCAR-F-Amey-Thakur-0021

**EN** What is the correct use of a hook in a Claude Code workflow?

**기존** Claude Code 워크플로에서 hook의 올바른 용도는 무엇인가?

**신규** Claude Code workflow에서 hook의 올바른 용도는 무엇인가?

- A. 기존: 모델이 따라야 할 지침을 담는 것
  - 신규: 모델이 따라야 할 지침을 담는다
- B. 기존: 프로젝트 컨텍스트를 저장하는 것
  - 신규: project context를 저장한다
- C. 기존: 모델과 무관하게 정해진 시점에 결정적인 동작을 강제하는 것
  - 신규: 정해진 시점에 모델과 상관없이 deterministic한 동작을 강제한다
- D. 기존: 어떤 모델을 사용할지 정의하는 것
  - 신규: 어떤 모델을 쓸지 정의한다

**해설 EN** **C.** Hooks run as code at fixed points, so they enforce rather than request. Instructions (A) and context (B) belong in project memory, and model choice (D) is configuration.

**해설 기존** **C.** hook은 정해진 시점에 코드로 실행되므로 요청하는 것이 아니라 강제한다. 지침(A)과 컨텍스트(B)는 프로젝트 메모리에 속하고, 모델 선택(D)은 설정이다.

**해설 신규** **C.** hook은 정해진 시점에 코드로 실행되므로 부탁하는 것이 아니라 강제한다. 지침(A)과 context(B)는 project memory에 두는 것이고, 모델 선택(D)은 설정의 일이다.

## CCAR-F-Amey-Thakur-0022

**EN** Claude Code performs well for one engineer and inconsistently across the team. What is the most likely cause?

**기존** Claude Code가 한 엔지니어에게는 잘 동작하지만 팀 전체에서는 일관되지 않다. 가장 가능성이 높은 원인은 무엇인가?

**신규** Claude Code가 엔지니어 한 명에게는 잘 동작하는데 팀 전체에서는 결과가 들쭉날쭉하다. 가장 가능성이 높은 원인은 무엇인가?

- A. 기존: 다른 사람들에게는 더 성능 좋은 머신이 필요하다
  - 신규: 다른 사람들에게는 더 성능이 좋은 장비가 필요하다
- B. 기존: 저장소가 너무 크다
  - 신규: 저장소가 너무 크다
- C. 기존: 다른 사람들이 다른 터미널을 사용한다
  - 신규: 다른 사람들은 다른 terminal을 쓴다
- D. 기존: 작업 규약이 저장소가 아니라 한 사람의 로컬 환경에 있다
  - 신규: 작업 컨벤션이 저장소가 아니라 한 사람의 로컬 환경에만 있다

**해설 EN** **D.** Context that is not committed does not travel, which produces exactly this asymmetry. Hardware (A), repository size (B), and terminal choice (C) do not explain a difference in output quality.

**해설 기존** **D.** 커밋되지 않은 컨텍스트는 전파되지 않으며, 이것이 바로 이런 비대칭을 낳는다. 하드웨어(A), 저장소 크기(B), 터미널 선택(C)은 출력 품질의 차이를 설명하지 못한다.

**해설 신규** **D.** commit하지 않은 context는 다른 사람에게 전달되지 않으므로 바로 이런 비대칭이 생긴다. 하드웨어(A), 저장소 크기(B), terminal 종류(C)로는 출력 품질의 차이를 설명할 수 없다.

## CCAR-F-Amey-Thakur-0023

**EN** A pipeline requires output that always validates against a schema. What is the correct approach?

**기존** 파이프라인이 항상 스키마에 맞게 검증되는 출력을 요구한다. 올바른 접근은 무엇인가?

**신규** pipeline이 항상 schema에 맞는 출력을 요구한다. 올바른 접근은 무엇인가?

- A. 기존: 스키마를 모델이 반드시 호출해야 하는 도구로 선언하고, 수신 시 검증한다
  - 신규: schema를 모델이 반드시 호출해야 하는 도구로 선언하고, 받을 때 검증한다
- B. 기존: 프롬프트에서 스키마를 요청하고 이후에 검증한다
  - 신규: prompt에서 schema를 요청하고 나중에 검증한다
- C. 기존: JSON을 요청하고 잘못된 출력은 코드에서 복구한다
  - 신규: JSON을 요청하고, 형식이 깨진 출력은 코드에서 고친다
- D. 기존: 더 낮은 temperature를 사용한다
  - 신규: temperature를 낮춘다

**해설 EN** **A.** A declared schema makes the structure part of the contract rather than a request, and validation on receipt closes the loop. Prompt requests (B), downstream repair (C), and temperature (D) all leave the shape to chance.

**해설 기존** **A.** 선언된 스키마는 구조를 요청이 아니라 계약의 일부로 만들고, 수신 시 검증이 루프를 닫는다. 프롬프트 요청(B), 후속 복구(C), temperature(D)는 모두 형태를 우연에 맡긴다.

**해설 신규** **A.** schema를 선언하면 구조가 요청이 아니라 계약의 일부가 되고, 받을 때 검증하면 그 계약이 지켜졌는지까지 확인할 수 있다. prompt로 요청하는 것(B), 나중에 고치는 것(C), temperature(D)는 모두 출력 형태를 운에 맡긴다.

## CCAR-F-Amey-Thakur-0024

**EN** Extraction is accurate for common cases and fails on rare formats. What is the most effective response?

**기존** 추출은 흔한 경우에는 정확하지만 드문 형식에서는 실패한다. 가장 효과적인 대응은 무엇인가?

**신규** 추출은 흔한 경우에는 정확하지만 드문 형식에서는 실패한다. 가장 효과적인 대응은 무엇인가?

- A. 기존: 유연성을 유도하기 위해 temperature를 높인다
  - 신규: 유연하게 반응하도록 temperature를 높인다
- B. 기존: 드문 형식을 다루는 예시를 추가하고, 필드가 없을 때 무엇을 반환할지 정의한다
  - 신규: 드문 형식을 다루는 예시를 추가하고, 필드가 없을 때 무엇을 반환할지 정의한다
- C. 기존: 더 큰 모델로 바꾼다
  - 신규: 더 큰 모델로 바꾼다
- D. 기존: 특이한 입력에 대해 더 열심히 하라고 모델에게 요청한다
  - 신규: 특이한 입력에서는 더 열심히 해 보라고 모델에게 요청한다

**해설 EN** **B.** Rare cases fail because they are unspecified, and examples plus an explicit absent-field rule specify them. Temperature (A) adds variance, a larger model (C) is not aimed at the gap, and exhortation (D) is not a specification.

**해설 기존** **B.** 드문 경우는 명세되어 있지 않기 때문에 실패하며, 예시와 명시적인 필드 부재 규칙이 이를 명세한다. temperature(A)는 변동성을 더하고, 더 큰 모델(C)은 그 공백을 겨냥하지 않으며, 독려(D)는 명세가 아니다.

**해설 신규** **B.** 드문 경우가 실패하는 이유는 명세가 없어서이고, 예시와 필드 부재 시 규칙을 명시하면 그 명세가 채워진다. temperature(A)는 변동성만 키운다. 더 큰 모델(C)은 이 빈틈을 겨냥한 해법이 아니다. 더 열심히 하라는 당부(D)는 명세가 아니다.

## CCAR-F-Amey-Thakur-0025

**EN** What should a schema define for a field the source document may not contain?

**기존** 원본 문서에 없을 수 있는 필드에 대해 스키마는 무엇을 정의해야 하는가?

**신규** 원본 문서에 없을 수 있는 필드에 대해 schema는 무엇을 정의해야 하는가?

- A. 기존: 아무것도 정의하지 않는다. 모델이 생략할 것이기 때문이다
  - 신규: 아무것도 정의하지 않는다. 모델이 알아서 생략할 것이다
- B. 기존: 그럴듯해 보이는 기본값
  - 신규: 그럴듯해 보이는 기본값
- C. 기존: 부재에 대한 명시적 표현. 누락된 값이 채워지지 않은 값과 구별되도록 한다
  - 신규: 값이 없음을 나타내는 명시적 표현. 그래야 값이 없는 것과 채우지 않은 것을 구별할 수 있다
- D. 기존: 메모를 위한 자유 텍스트 필드
  - 신규: 메모를 적는 free-text 필드

**해설 EN** **C.** Absence must be representable, or downstream code cannot tell a genuine gap from a failure. Silent omission (A) is ambiguous, plausible defaults (B) fabricate data, and a notes field (D) does not make the state machine-readable.

**해설 기존** **C.** 부재를 표현할 수 있어야 하며, 그렇지 않으면 후속 코드가 진짜 공백과 실패를 구별할 수 없다. 조용한 생략(A)은 모호하고, 그럴듯한 기본값(B)은 데이터를 조작하며, 메모 필드(D)는 그 상태를 기계가 읽을 수 있게 만들지 못한다.

**해설 신규** **C.** 값이 없다는 사실을 표현할 수 있어야 후단 코드가 정말로 비어 있는 것과 실패를 구별할 수 있다. 말없이 생략하면(A) 구별이 안 된다. 그럴듯한 기본값(B)은 데이터를 지어내는 것이다. 메모 필드(D)는 그 상태를 기계가 읽을 수 있게 만들지 못한다.

## CCAR-F-Amey-Thakur-0026

**EN** Which practice most improves consistency across a long-running structured extraction job?

**기존** 장시간 실행되는 구조화 추출 작업 전반의 일관성을 가장 크게 높이는 방법은 무엇인가?

**신규** 오래 걸리는 구조화 추출 작업에서 일관성을 가장 크게 높이는 방법은 무엇인가?

- A. 기존: 문서의 순서를 무작위로 섞는 것
  - 신규: 문서 순서를 무작위로 섞는다
- B. 기존: 출력 토큰 제한을 늘리는 것
  - 신규: 출력 token 한도를 늘린다
- C. 기존: 각 문서를 두 번씩 실행하는 것
  - 신규: 문서마다 두 번씩 실행한다
- D. 기존: 프롬프트, 스키마, 모델 버전을 고정하고 출력과 함께 기록하는 것
  - 신규: prompt, schema, 모델 버전을 고정하고 출력과 함께 기록한다

**해설 EN** **D.** Consistency requires that the things that shape output are pinned and recorded, so results remain comparable and reproducible. Ordering (A) is irrelevant, the token cap (B) affects length, and duplicate runs (C) measure variance without removing it.

**해설 기존** **D.** 일관성을 위해서는 출력을 형성하는 요소들이 고정되고 기록되어야 하며, 그래야 결과가 비교 가능하고 재현 가능하게 유지된다. 순서(A)는 무관하고, 토큰 상한(B)은 길이에 영향을 주며, 중복 실행(C)은 변동성을 없애지 않고 측정만 한다.

**해설 신규** **D.** 일관성을 얻으려면 출력을 좌우하는 요소를 고정하고 기록해서 결과를 비교하고 재현할 수 있어야 한다. 순서(A)는 상관이 없고, token 한도(B)는 길이에만 영향을 준다. 두 번 실행하면(C) 변동성을 측정할 뿐 없애지는 못한다.

## CCAR-F-Amey-Thakur-0027

**EN** A prompt mixes the instruction, the data, and the output format in continuous prose. What is the first improvement?

**기존** 프롬프트가 지침, 데이터, 출력 형식을 이어진 산문 속에 섞어 놓고 있다. 첫 번째 개선은 무엇인가?

**신규** prompt가 지시, 데이터, 출력 형식을 구분 없이 이어진 문장으로 섞어 놓았다. 가장 먼저 할 개선은 무엇인가?

- A. 기존: 지침, 입력, 필요한 형식을 구별할 수 있도록 섹션을 분리한다
  - 신규: 지시, 입력, 요구하는 형식을 구별할 수 있도록 섹션을 나눈다
- B. 기존: 프롬프트를 줄인다
  - 신규: 더 짧게 줄인다
- C. 기존: 시스템 프롬프트로 옮긴다
  - 신규: system prompt로 옮긴다
- D. 기존: 형식 요구 사항에 강조를 더한다
  - 신규: 형식 요구사항을 강조한다

**해설 EN** **A.** Structure lets the model tell instruction from data, which is the most common source of confusion in long prompts. Shortening (B) may remove needed detail, relocation (C) does not clarify, and emphasis (D) does not separate.

**해설 기존** **A.** 구조는 모델이 지침과 데이터를 구분하게 해 주며, 이는 긴 프롬프트에서 가장 흔한 혼동의 원인이다. 줄이면(B) 필요한 세부 사항이 사라질 수 있고, 위치 이동(C)은 명확성을 높이지 않으며, 강조(D)는 분리하지 않는다.

**해설 신규** **A.** 구조가 있으면 모델이 지시와 데이터를 구별할 수 있는데, 이것이 긴 prompt에서 가장 흔한 혼란의 원인이다. 줄이면(B) 필요한 세부 내용이 빠질 수 있고, 위치를 옮기는 것(C)으로는 명확해지지 않으며, 강조(D)로는 구분이 되지 않는다.

## CCAR-F-Amey-Thakur-0028

**EN** What is the strongest indicator that a tool surface needs redesign?

**기존** 도구 구성을 재설계해야 한다는 가장 강력한 징후는 무엇인가?

**신규** 도구 구성을 다시 설계해야 한다는 가장 강력한 신호는 무엇인가?

- A. 기존: 도구가 열 개를 넘는다
  - 신규: 도구가 열 개를 넘는다
- B. 기존: 모델이 요청을 수행할 수 없는 도구를 정기적으로 선택한다
  - 신규: 모델이 요청을 처리할 수 없는 도구를 자주 선택한다
- C. 기존: 도구가 JSON을 반환한다
  - 신규: 도구가 JSON을 반환한다
- D. 기존: 도구가 여러 서비스에 걸쳐 구현되어 있다
  - 신규: 도구가 여러 서비스에 나뉘어 구현되어 있다

**해설 EN** **B.** Repeated wrong selection is evidence that the tools are not distinguishable from their descriptions, which is a design fault. Tool count (A), return format (C), and implementation topology (D) are not themselves problems.

**해설 기존** **B.** 반복되는 잘못된 선택은 도구가 설명만으로는 구별되지 않는다는 증거이며, 이는 설계상의 결함이다. 도구 수(A), 반환 형식(C), 구현 토폴로지(D)는 그 자체로 문제가 아니다.

**해설 신규** **B.** 엉뚱한 도구를 반복해서 고른다는 것은 설명만으로는 도구들이 구별되지 않는다는 증거이고, 이는 설계 결함이다. 도구 수(A), 반환 형식(C), 구현이 어떻게 분산되어 있는지(D)는 그 자체로 문제가 아니다.

## CCAR-F-Amey-Thakur-0029

**EN** How should a tool that performs an irreversible action be designed?

**기존** 되돌릴 수 없는 작업을 수행하는 도구는 어떻게 설계해야 하는가?

**신규** 되돌릴 수 없는 작업을 수행하는 도구는 어떻게 설계해야 하는가?

- A. 기존: 모델에게 조심하라고 경고하는 설명을 붙인다
  - 신규: 모델에게 조심하라고 경고하는 설명을 붙인다
- B. 기존: 더 많은 파라미터를 요구하도록 한다
  - 신규: parameter를 더 많이 요구하게 한다
- C. 기존: 권한 부여와 확인이 모델 외부에서 강제되도록 한다
  - 신규: 권한 부여와 확인을 모델 바깥에서 강제하게 한다
- D. 기존: 마지막에 선언되도록 한다
  - 신규: 목록의 맨 마지막에 선언한다

**해설 EN** **C.** Irreversibility is controlled by the surrounding system, because a prompt-level warning is a request rather than a guarantee. Extra parameters (B) and ordering (D) do not constrain authority.

**해설 기존** **C.** 되돌릴 수 없는 작업은 주변 시스템이 통제하는데, 프롬프트 수준의 경고는 보장이 아니라 요청이기 때문이다. 추가 파라미터(B)와 순서(D)는 권한을 제약하지 않는다.

**해설 신규** **C.** 되돌릴 수 없는 작업은 모델을 둘러싼 시스템이 통제해야 한다. prompt에 적은 경고는 부탁일 뿐 보장이 아니기 때문이다. parameter를 늘리거나(B) 선언 순서를 바꾸는 것(D)은 권한을 제약하지 못한다.

## CCAR-F-Amey-Thakur-0030

**EN** A tool returns a large payload that consumes most of the context window. What is the right change?

**기존** 도구가 컨텍스트 윈도우의 대부분을 차지하는 큰 페이로드를 반환한다. 올바른 변경은 무엇인가?

**신규** 도구가 큰 payload를 반환해서 context window의 대부분을 차지한다. 올바른 변경은 무엇인가?

- A. 기존: 컨텍스트 윈도우를 늘린다
  - 신규: context window를 늘린다
- B. 기존: 두 번째 모델 호출로 페이로드를 요약한다
  - 신규: 두 번째 모델 호출로 payload를 요약한다
- C. 기존: 도구를 덜 자주 호출한다
  - 신규: 도구를 덜 자주 호출한다
- D. 기존: 작업에 필요한 것만 반환하고, 더 자세한 내용을 요청할 방법을 제공한다
  - 신규: 작업에 필요한 것만 반환하고, 더 자세한 내용은 따로 요청할 수 있게 한다

**해설 EN** **D.** Tools should return task-relevant results rather than everything available, which keeps context for reasoning. A larger window (A) postpones the problem, a second call (B) adds cost and a failure point, and calling less often (C) does not change the payload.

**해설 기존** **D.** 도구는 사용 가능한 모든 것이 아니라 작업과 관련된 결과를 반환해야 하며, 그래야 추론을 위한 컨텍스트가 유지된다. 더 큰 윈도우(A)는 문제를 미루고, 두 번째 호출(B)은 비용과 실패 지점을 더하며, 덜 자주 호출하는 것(C)은 페이로드를 바꾸지 않는다.

**해설 신규** **D.** 도구는 가능한 모든 것이 아니라 작업과 관련된 결과만 반환해야 추론에 쓸 context가 남는다. 더 큰 window(A)는 문제를 미룰 뿐이다. 모델을 한 번 더 호출하면(B) 비용이 늘고 실패 지점도 하나 더 생긴다. 호출을 줄여도(C) payload는 그대로다.

## CCAR-F-Amey-Thakur-0031

**EN** What belongs in a tool's description?

**기존** 도구의 설명에는 무엇이 들어가야 하는가?

**신규** 도구의 설명(description)에는 무엇이 들어가야 하는가?

- A. 기존: 도구가 무엇을 하는지, 언제 사용하는지, 파라미터가 무엇을 뜻하는지
  - 신규: 도구가 하는 일, 언제 쓰는지, parameter의 의미
- B. 기존: 구현 언어와 프레임워크
  - 신규: 구현 언어와 framework
- C. 기존: 서비스 수준 계약
  - 신규: 서비스 수준 협약(SLA)
- D. 기존: 도구를 소유한 팀의 이름
  - 신규: 도구를 소유한 팀의 이름

**해설 EN** **A.** The description is the model's selection guide, so it must answer purpose, applicability, and parameters. Implementation detail (B), service levels (C), and ownership (D) are irrelevant to the choice.

**해설 기존** **A.** 설명은 모델의 선택 가이드이므로 목적, 적용 시점, 파라미터에 답해야 한다. 구현 세부 사항(B), 서비스 수준(C), 소유권(D)은 선택과 무관하다.

**해설 신규** **A.** 설명은 모델이 도구를 고르는 안내서이므로 용도, 적용 시점, parameter에 답할 수 있어야 한다. 구현 세부 사항(B), 서비스 수준(C), 소유 팀(D)은 도구를 선택하는 데 아무 상관이 없다.

## CCAR-F-Amey-Thakur-0032

**EN** A long agentic run degrades in quality as it proceeds. What is the most likely cause?

**기존** 긴 에이전트 실행이 진행될수록 품질이 저하된다. 가장 가능성이 높은 원인은 무엇인가?

**신규** 긴 agentic 실행이 진행될수록 품질이 떨어진다. 가장 가능성이 높은 원인은 무엇인가?

- A. 기존: 실행 도중 모델 버전이 바뀌었다
  - 신규: 실행 도중에 모델 버전이 바뀌었다
- B. 기존: 컨텍스트가 누적되어 관련 있는 내용이 오래된 내용과 경쟁한다
  - 신규: context가 쌓이면서 관련 있는 내용과 오래된 내용이 서로 경쟁한다
- C. 기존: temperature가 너무 낮게 설정되었다
  - 신규: temperature가 너무 낮게 설정되었다
- D. 기존: 도구가 느려졌다
  - 신규: 도구가 느려졌다

**해설 EN** **B.** Progressive degradation over a long run is the signature of context accumulation and drift. Versions do not change mid-run (A), low temperature (C) reduces variety rather than quality, and tool latency (D) does not affect correctness.

**해설 기존** **B.** 긴 실행에 걸친 점진적 저하는 컨텍스트 누적과 drift의 전형적인 징후이다. 버전은 실행 도중 바뀌지 않으며(A), 낮은 temperature(C)는 품질이 아니라 다양성을 줄이고, 도구 지연(D)은 정확성에 영향을 주지 않는다.

**해설 신규** **B.** 긴 실행에서 품질이 점점 나빠지는 것은 context가 누적되고 흐름이 어긋날 때 나타나는 전형적인 특징이다. 모델 버전은 실행 도중에 바뀌지 않는다(A). temperature가 낮으면(C) 다양성이 줄 뿐 품질이 떨어지지는 않는다. 도구의 지연 시간(D)은 정확성에 영향을 주지 않는다.

## CCAR-F-Amey-Thakur-0033

**EN** What is the right way to carry state across a compaction boundary?

**기존** compaction 경계를 넘어 상태를 이어 가는 올바른 방법은 무엇인가?

**신규** compaction 경계를 넘어 상태를 이어 가는 올바른 방법은 무엇인가?

- A. 기존: 무엇이 중요했는지 모델이 기억하리라고 의존한다
  - 신규: 중요했던 내용을 모델이 기억하리라고 믿는다
- B. 기존: compaction이 필요 없도록 컨텍스트 윈도우를 늘린다
  - 신규: compaction이 필요 없도록 context window를 늘린다
- C. 기존: 계속 유지되어야 하는 결정과 제약을 명시적인 요약에 적어 이어서 전달한다
  - 신규: 계속 유지해야 하는 결정과 제약을 명시적인 요약에 적어서 이어 간다
- D. 기존: compaction 후에 작업을 다시 시작한다
  - 신규: compaction 이후에 작업을 처음부터 다시 시작한다

**해설 EN** **C.** Persistence must be deliberate, because compaction is lossy by design. Relying on recall (A) is unreliable, a larger window (B) only delays the boundary, and restarting (D) discards the work.

**해설 기존** **C.** compaction은 설계상 손실이 있으므로 지속은 의도적이어야 한다. 기억에 의존하는 것(A)은 신뢰할 수 없고, 더 큰 윈도우(B)는 경계를 늦출 뿐이며, 다시 시작하면(D) 작업이 버려진다.

**해설 신규** **C.** compaction은 설계상 정보가 손실되므로 유지할 내용은 의도적으로 남겨야 한다. 모델의 기억에 기대는 것(A)은 믿을 수 없고, 더 큰 window(B)는 경계를 늦출 뿐이며, 다시 시작하면(D) 해 둔 작업이 버려진다.

## CCAR-F-Amey-Thakur-0034

**EN** Which measure most improves reliability for a workflow that must not silently produce wrong output?

**기존** 조용히 잘못된 출력을 내서는 안 되는 워크플로의 신뢰성을 가장 크게 높이는 조치는 무엇인가?

**신규** 잘못된 출력이 조용히 나가서는 안 되는 workflow의 신뢰성을 가장 크게 높이는 조치는 무엇인가?

- A. 기존: 더 큰 모델
  - 신규: 더 큰 모델
- B. 기존: 더 긴 프롬프트
  - 신규: 더 긴 prompt
- C. 기존: 프롬프트에 더 많은 예시
  - 신규: prompt에 예시 추가
- D. 기존: 출력을 거부하고 정의된 fallback을 작동시킬 수 있는 검증 단계
  - 신규: 출력을 거부하고 정해 둔 fallback을 실행할 수 있는 검증 단계

**해설 EN** **D.** Reliability against silent failure requires detection and a defined response, which is what validation with a fallback provides. Model size (A), prompt length (B), and examples (C) improve the average case without catching the bad one.

**해설 기존** **D.** 조용한 실패에 대한 신뢰성은 탐지와 정의된 대응을 필요로 하며, 이는 fallback을 갖춘 검증이 제공하는 바이다. 모델 크기(A), 프롬프트 길이(B), 예시(C)는 평균적인 경우는 개선하지만 나쁜 경우를 잡아내지는 못한다.

**해설 신규** **D.** 조용한 실패를 막으려면 감지하는 장치와 정해진 대응이 필요하며, fallback이 있는 검증이 바로 그 역할을 한다. 모델 크기(A), prompt 길이(B), 예시(C)는 평균적인 경우를 개선할 뿐 잘못된 경우를 잡아내지는 못한다.

## CCAR-F-Amey-Thakur-0035

**EN** What should be measured to know whether a production agentic system is healthy?

**기존** 프로덕션 에이전트 시스템이 건강한지 알려면 무엇을 측정해야 하는가?

**신규** production agentic system이 정상적으로 운영되고 있는지 알려면 무엇을 측정해야 하는가?

- A. 기존: 정의된 기준에 따른 작업 성공 여부, 그리고 실패의 비율과 양상
  - 신규: 정해 둔 기준에 따른 작업 성공 여부, 그리고 실패의 비율과 양상
- B. 기존: 소비된 총 토큰
  - 신규: 소비한 전체 token
- C. 기존: 평균 응답 시간
  - 신규: 평균 응답 시간
- D. 기존: 실행당 도구 호출 횟수
  - 신규: 실행 한 번당 도구 호출 횟수

**해설 EN** **A.** Health is defined by whether the system accomplishes the task and how it fails when it does not. Tokens (B), latency (C), and call counts (D) are cost and behavior signals that say nothing about correctness.

**해설 기존** **A.** 건강 상태는 시스템이 작업을 완수하는지, 그렇지 못할 때 어떻게 실패하는지로 정의된다. 토큰(B), 지연 시간(C), 호출 횟수(D)는 정확성에 대해서는 아무것도 말해 주지 않는 비용 및 동작 신호이다.

**해설 신규** **A.** 시스템이 정상인지는 작업을 해내는지, 해내지 못할 때 어떻게 실패하는지로 판단한다. token(B), 지연 시간(C), 호출 횟수(D)는 비용과 동작을 보여 주는 신호일 뿐 정확성에 대해서는 아무것도 말해 주지 않는다.

## CCAR-F-Amey-Thakur-0036

**EN** The agent occasionally answers billing questions using an order it looked up three turns earlier for a different customer. What is the architectural fix?

**기존** 에이전트가 가끔 세 턴 전에 다른 고객을 위해 조회한 주문을 사용하여 청구 관련 질문에 답한다. 아키텍처상의 해결책은 무엇인가?

**신규** agent가 가끔 청구 관련 질문에 답하면서, 세 turn 전에 다른 고객을 위해 조회한 주문을 사용한다. 아키텍처상의 해결 방법은 무엇인가?

- A. 기존: 컨텍스트 윈도우를 늘린다
  - 신규: context window를 늘린다
- B. 기존: 각 대화의 컨텍스트를 한 고객으로 한정하고, 대상이 바뀔 때 이전 조회를 지우거나 격리한다
  - 신규: 대화마다 context의 범위를 고객 한 명으로 한정하고, 대상이 바뀌면 이전 조회 결과를 지우거나 격리한다
- C. 기존: lookup_order 도구를 제거한다
  - 신규: lookup_order 도구를 제거한다
- D. 기존: 고객 신원에 주의하라고 모델에게 지시한다
  - 신규: 고객 신원에 주의하라고 모델에게 지시한다

**해설 EN** Cross-customer contamination is a context-scoping defect, not a window-size problem

**해설 기존** 고객 간 오염은 윈도우 크기 문제가 아니라 컨텍스트 범위 설정의 결함이다

**해설 신규** 고객 간 오염은 context 범위 설정의 결함이지 window 크기 문제가 아니다

## CCAR-F-Amey-Thakur-0037

**EN** process_refund fails intermittently because the billing backend times out. What should the tool return so the agent can behave sensibly?

**기존** billing 백엔드가 타임아웃되어 process_refund가 간헐적으로 실패한다. 에이전트가 적절하게 행동할 수 있도록 도구는 무엇을 반환해야 하는가?

**신규** billing backend가 시간 초과를 일으켜 process_refund가 간헐적으로 실패한다. agent가 합리적으로 행동하려면 도구는 무엇을 반환해야 하는가?

- A. 기존: 빈 문자열
  - 신규: 빈 문자열
- B. 기존: 사용자에게 나중에 다시 시도하라고 요청하는 메시지
  - 신규: 나중에 다시 시도하라고 사용자에게 안내하는 메시지
- C. 기존: 범주와 retryable 플래그를 담은 구조화된 오류. 에이전트가 의도적으로 재시도하거나 escalation할 수 있게 한다
  - 신규: category와 retryable 플래그가 있는 구조화된 오류. 그러면 agent가 재시도할지 escalation할지 의도적으로 정할 수 있다
- D. 기존: 예외 스택 트레이스
  - 신규: 예외 stack trace

**해설 EN** Structured errors with categories and retryable flags are what let an agent recover deliberately

**해설 기존** 범주와 retryable 플래그를 갖춘 구조화된 오류가 에이전트가 의도적으로 복구할 수 있게 해 준다

**해설 신규** category와 retryable 플래그가 담긴 구조화된 오류가 있어야 agent가 의도적으로 복구할 수 있다

## CCAR-F-Amey-Thakur-0038

**EN** Which condition should route a ticket to escalate_to_human rather than continue autonomous resolution?

**기존** 어떤 조건이 티켓을 자율 해결을 계속하는 대신 escalate_to_human으로 라우팅해야 하는가?

**신규** 어떤 조건이면 자율 처리를 이어 가지 않고 티켓을 escalate_to_human으로 넘겨야 하는가?

- A. 기존: 고객이 에이전트가 지원하는 언어로 글을 쓴다
  - 신규: 고객이 agent가 지원하는 언어로 글을 쓴다
- B. 기존: 주문이 30일을 넘었다
  - 신규: 주문한 지 30일이 넘었다
- C. 기존: 대화가 다섯 턴을 넘는다
  - 신규: 대화가 다섯 turn을 넘었다
- D. 기존: 요청이 문서화된 정책 밖에 있거나, 제한된 횟수의 시도 후에도 에이전트가 진행하지 못한다
  - 신규: 요청이 문서화된 정책 범위를 벗어나거나, 정해 둔 횟수만큼 시도하고도 agent가 진전을 이루지 못한다

**해설 EN** Policy gaps and lack of progress are the documented escalation triggers; turn counts and order age are not

**해설 기존** 정책의 공백과 진행 불능이 문서화된 escalation 트리거이며, 턴 수와 주문 경과 기간은 그렇지 않다

**해설 신규** 정책의 빈틈과 진전 없음이 문서화된 escalation 기준이며, turn 수와 주문 경과 기간은 기준이 아니다

## CCAR-F-Amey-Thakur-0039

**EN** The agent sometimes calls get_customer when it should call lookup_order. What is the most effective change?

**기존** 에이전트가 lookup_order를 호출해야 할 때 가끔 get_customer를 호출한다. 가장 효과적인 변경은 무엇인가?

**신규** agent가 lookup_order를 호출해야 할 때 가끔 get_customer를 호출한다. 가장 효과적인 변경은 무엇인가?

- A. 기존: 각 도구가 언제 적용되는지, 다른 도구와 어떻게 다른지를 정확히 밝히도록 두 도구 설명을 다시 쓴다
  - 신규: 두 도구의 설명을 다시 써서, 각각 언제 적용되는지와 상대와 어떻게 다른지를 정확히 밝힌다
- B. 기존: 설정에서 도구의 순서를 바꾼다
  - 신규: 설정에서 도구의 순서를 바꾼다
- C. 기존: 모드 플래그가 있는 하나의 도구로 합친다
  - 신규: mode 플래그를 둔 하나의 도구로 합친다
- D. 기존: 모델의 temperature를 높인다
  - 신규: 모델의 temperature를 높인다

**해설 EN** Tool selection runs on descriptions, so differentiation is the fix for confusion between similar tools

**해설 기존** 도구 선택은 설명을 기반으로 이루어지므로, 비슷한 도구 사이의 혼동은 구분을 명확히 하는 것이 해결책이다

**해설 신규** 도구 선택은 설명을 근거로 이루어지므로, 비슷한 도구끼리의 혼동은 설명을 차별화해서 해결한다

## CCAR-F-Amey-Thakur-0040

**EN** Backend conventions should apply only when backend files are touched. Where do they belong?

**기존** backend 규약은 backend 파일을 다룰 때만 적용되어야 한다. 어디에 두어야 하는가?

**신규** backend 컨벤션은 backend 파일을 다룰 때만 적용되어야 한다. 어디에 두어야 하는가?

- A. 기존: 항상 사용할 수 있도록 루트 CLAUDE.md에
  - 신규: 항상 쓸 수 있도록 루트 CLAUDE.md에 둔다
- B. 기존: backend 경로와 일치하는 frontmatter를 가진 `.claude/rules/` 아래의 경로 범위 규칙에
  - 신규: `.claude/rules/` 아래에 backend 경로에 맞는 frontmatter를 가진, 경로가 지정된 규칙으로 둔다
- C. 기존: 각 엔지니어의 사용자 수준 설정에
  - 신규: 엔지니어 각자의 user-level 설정에 둔다
- D. 기존: 저장소 위키에
  - 신규: 저장소 wiki에 둔다

**해설 EN** Path-scoped rules load conditionally, which is exactly the stated requirement

**해설 기존** 경로 범위 규칙은 조건부로 로드되며, 이것이 바로 명시된 요구 사항이다

**해설 신규** 경로를 지정한 규칙은 조건부로 로드되므로, 제시된 요구사항에 정확히 맞는다

## CCAR-F-Amey-Thakur-0041

**EN** When is plan mode the appropriate choice over direct execution?

**기존** 직접 실행보다 plan mode가 적절한 선택인 때는 언제인가?

**신규** plan mode가 바로 실행하는 것보다 적절한 때는 언제인가?

- A. 기존: 계획이 항상 더 안전하므로 모든 변경에
  - 신규: 계획을 세우는 쪽이 항상 더 안전하므로 모든 변경에
- B. 기존: 모델이 해당 언어에 익숙하지 않을 때만
  - 신규: 모델이 해당 언어에 익숙하지 않을 때만
- C. 기존: 변경이 충분히 크거나 위험해서 편집이 이루어지기 전에 사람이 접근 방식을 검토해야 할 때
  - 신규: 변경 규모가 크거나 위험해서, 편집하기 전에 사람이 접근 방식을 검토해야 할 때
- D. 기존: 컨텍스트 윈도우가 거의 가득 찼을 때
  - 신규: context window가 거의 찼을 때

**해설 EN** Plan mode is a human review gate for approach, warranted by risk rather than universally

**해설 기존** plan mode는 접근 방식에 대한 사람의 검토 관문이며, 보편적으로가 아니라 위험에 따라 정당화된다

**해설 신규** plan mode는 접근 방식을 사람이 검토하는 관문이다. 모든 작업에 쓰는 것이 아니라 위험이 있을 때 쓴다.

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

## CCAR-F-Amey-Thakur-0043

**EN** Subagents return full source documents to the coordinator, which then exceeds its context limit. What is the correct design change?

**기존** subagent가 원본 문서 전체를 coordinator에게 반환하고, 그 결과 coordinator가 컨텍스트 한도를 초과한다. 올바른 설계 변경은 무엇인가?

**신규** subagent가 원본 문서 전체를 coordinator에 돌려주는 바람에 coordinator가 context 한도를 넘는다. 어떻게 설계를 바꾸는 것이 맞는가?

- A. 기존: subagent가 인용이 포함된 구조화된 발견 내용을 반환하게 하고, 원본 소스는 가장자리나 scratchpad에 둔다
  - 신규: subagent는 인용을 붙인 구조화된 조사 결과를 반환하게 하고, 원본 자료는 subagent 쪽이나 scratchpad에 둔다
- B. 기존: coordinator에게 더 큰 모델을 준다
  - 신규: coordinator에 더 큰 모델을 쓴다
- C. 기존: subagent 수를 하나로 줄인다
  - 신규: subagent를 하나로 줄인다
- D. 기존: 각 문서를 첫 페이지까지만 자른다
  - 신규: 각 문서를 첫 페이지까지만 잘라서 넘긴다

**해설 EN** Delegation exists to keep bulk at the edge and move distilled results

**해설 기존** 위임은 대량 데이터를 가장자리에 두고 정제된 결과를 이동시키기 위해 존재한다

**해설 신규** 작업을 위임하는 이유는 방대한 자료는 subagent 쪽에 두고 정리된 결과만 coordinator로 올려 보내기 위해서다.

## CCAR-F-Amey-Thakur-0044

**EN** Final reports attribute claims to the wrong sources even though each subagent is individually accurate. What is the likely cause?

**기존** 각 subagent는 개별적으로 정확한데도 최종 보고서가 주장을 잘못된 출처에 귀속시킨다. 가능성이 높은 원인은 무엇인가?

**신규** subagent 각각은 정확한데도 최종 보고서가 주장의 출처를 엉뚱하게 표기한다. 가장 가능성 높은 원인은 무엇인가?

- A. 기존: 종합 모델이 너무 작다
  - 신규: 종합을 맡은 모델이 너무 작다
- B. 기존: handoff 형식이 주장과 출처를 함께 담지 않아 단계 사이에서 provenance가 사라진다
  - 신규: handoff 형식이 주장과 출처를 함께 담지 않아서, 단계를 넘어가는 사이 출처 정보(provenance)가 사라진다
- C. 기존: 검색 subagent가 너무 많은 결과를 반환한다
  - 신규: 검색 subagent가 결과를 너무 많이 반환한다
- D. 기존: 분석이 끝나기 전에 보고서가 생성된다
  - 신규: 분석이 끝나기 전에 보고서가 생성된다

**해설 EN** Provenance survives handoffs only when the format carries claim and source together

**해설 기존** provenance는 형식이 주장과 출처를 함께 담을 때만 handoff를 거쳐 유지된다

**해설 신규** handoff 형식이 주장과 출처를 함께 담아야만 provenance가 단계를 넘어서도 유지된다.

## CCAR-F-Amey-Thakur-0045

**EN** A subagent fails permanently on one source. What should the coordinator receive?

**기존** subagent가 한 출처에서 영구적으로 실패한다. coordinator는 무엇을 받아야 하는가?

**신규** subagent가 어떤 자료 하나에서 복구할 수 없게 실패한다. coordinator는 무엇을 받아야 하는가?

- A. 기존: 아무것도 받지 않아 보고서가 계속 진행된다
  - 신규: 아무것도 받지 않아서 보고서가 그대로 진행되게 한다
- B. 기존: 성공할 때까지 조용히 반복되는 재시도 루프
  - 신규: 성공할 때까지 조용히 반복하는 재시도 loop
- C. 기존: 재시도, 공백을 명시한 채 제외, 중단 중에서 결정하기에 충분한 컨텍스트를 갖춘 전파된 오류
  - 신규: 재시도, 빈틈을 기록하고 제외, 중단 중에서 고를 수 있을 만큼 context가 담겨 전파된 에러
- D. 기존: 세부 정보가 없는 일반적인 실패 플래그
  - 신규: 상세 내용 없이 실패했다는 일반적인 표시만 받는다

**해설 EN** Errors must propagate with enough context for the coordinator to choose a recovery path

**해설 기존** 오류는 coordinator가 복구 경로를 선택하기에 충분한 컨텍스트와 함께 전파되어야 한다

**해설 신규** coordinator가 복구 방법을 고를 수 있으려면 충분한 context와 함께 에러가 전달되어야 한다.

## CCAR-F-Amey-Thakur-0046

**EN** The reviewer must emit results a pipeline can parse. Which invocation is correct?

**기존** 리뷰어는 파이프라인이 파싱할 수 있는 결과를 내보내야 한다. 올바른 호출 방식은 무엇인가?

**신규** reviewer가 pipeline에서 파싱할 수 있는 결과를 내야 한다. 어떤 호출 방식이 맞는가?

- A. 기존: 출력을 로그로 리디렉션한 interactive 세션
  - 신규: interactive 세션을 열고 출력을 로그로 리디렉션한다
- B. 기존: 승인 단계가 있는 plan mode
  - 신규: 승인 단계를 둔 plan mode
- C. 기존: transcript를 이메일로 보내는 cron 작업
  - 신규: transcript를 이메일로 보내는 cron job
- D. 기존: JSON 출력과 스키마를 사용하는 non-interactive print 모드
  - 신규: JSON 출력과 schema를 지정한 non-interactive print mode

**해설 EN** CI requires non-interactive invocation with structured, schema-validated output

**해설 기존** CI는 구조화되고 스키마로 검증된 출력을 내는 non-interactive 호출을 필요로 한다

**해설 신규** CI에는 사람 없이 실행되는 호출 방식과, schema로 검증되는 구조화된 출력이 필요하다.

## CCAR-F-Amey-Thakur-0047

**EN** Reviews flag many low-value style nits and engineers now ignore them. Which change addresses this?

**기존** 리뷰가 가치 낮은 스타일 지적을 많이 표시해서 엔지니어들이 이제 이를 무시한다. 이 문제를 해결하는 변경은 무엇인가?

**신규** 리뷰가 가치 낮은 스타일 지적을 너무 많이 올려서 엔지니어들이 이제 리뷰를 무시한다. 어떻게 바꿔야 하는가?

- A. 기존: 프롬프트에 명시적인 리뷰 기준과 심각도 기준선을 정의하고, 범위 안과 범위 밖 발견 사항의 예시를 함께 제공한다
  - 신규: prompt에 명시적인 리뷰 기준과 심각도 기준선을 정의하고, 리뷰 대상인 지적과 아닌 지적의 예시를 함께 준다
- B. 기존: 발견 사항을 별도 채널에 게시한다
  - 신규: 지적 사항을 별도 채널에 올린다
- C. 기존: 큰 pull request에만 리뷰를 실행한다
  - 신규: 큰 pull request에만 리뷰를 돌린다
- D. 기존: 출력을 다섯 개의 발견 사항으로 제한한다
  - 신규: 출력을 지적 5개로 제한한다

**해설 EN** Precision comes from explicit criteria and examples that draw the signal boundary

**해설 기존** 정밀도는 신호의 경계를 그어 주는 명시적 기준과 예시에서 나온다

**해설 신규** 정밀도는 명시적인 기준과, 무엇이 의미 있는 지적인지 경계를 보여 주는 예시에서 나온다.

## CCAR-F-Amey-Thakur-0048

**EN** Some invoices legitimately lack a delivery date. How should the schema express this?

**기존** 일부 송장에는 정당한 사유로 배송일이 없다. 스키마는 이를 어떻게 표현해야 하는가?

**신규** 일부 invoice에는 배송일이 정당한 사유로 없다. schema는 이를 어떻게 표현해야 하는가?

- A. 기존: 필드를 필수로 만들고 추출이 실패하게 둔다
  - 신규: 필드를 필수로 두고, 없으면 추출이 실패하게 한다
- B. 기존: 필드를 nullable로 만들어 부재를 명시적으로 기록하고, 문서 유형상 필요한 경우에는 조건부 검증을 한다
  - 신규: 필드를 nullable로 두어 값이 없다는 사실을 명시적으로 기록하고, 문서 유형상 필요한 경우에는 조건부 validation을 건다
- C. 기존: 스키마에서 필드를 생략한다
  - 신규: schema에서 필드를 뺀다
- D. 기존: 기본값을 오늘 날짜로 한다
  - 신규: 기본값을 오늘 날짜로 한다

**해설 EN** Nullable fields record legitimate absence; required fields force fabrication or failure

**해설 기존** nullable 필드는 정당한 부재를 기록하고, 필수 필드는 조작이나 실패를 강요한다

**해설 신규** nullable 필드는 정당하게 값이 없는 경우를 기록한다. 필수 필드로 두면 모델이 값을 지어내거나 추출이 실패한다.

## CCAR-F-Amey-Thakur-0049

**EN** Which loop gives the most reliable extraction output?

**기존** 어떤 루프가 가장 신뢰할 수 있는 추출 출력을 제공하는가?

**신규** 추출 결과가 가장 믿을 만하게 나오는 loop는 무엇인가?

- A. 기존: 생성한 다음 모든 레코드를 수동으로 검토한다
  - 신규: 생성한 뒤 모든 레코드를 사람이 직접 검토한다
- B. 기존: 세 번 생성하고 다수결로 택한다
  - 신규: 세 번 생성해서 다수결로 정한다
- C. 기존: tool use를 통해 JSON 스키마를 강제하고, 검증하고, 실패 시 검증 오류를 모델에 제공하여 재시도한다
  - 신규: tool use로 JSON schema를 강제하고 validation을 거친 뒤, 실패하면 validation 에러를 모델에 주고 재시도한다
- D. 기존: temperature 0으로 생성하고 결과를 받아들인다
  - 신규: temperature를 0으로 두고 생성한 결과를 그대로 받아들인다

**해설 EN** Schema enforcement plus a validation-retry loop is the reliability pattern the guide describes

**해설 기존** 스키마 강제와 검증-재시도 루프가 가이드에서 설명하는 신뢰성 패턴이다

**해설 신규** schema 강제에 validation-retry loop를 더하는 것이 가이드가 설명하는 신뢰성 패턴이다.

## CCAR-F-Amey-Thakur-0050

**EN** Your team reports 97% accuracy measured only on records that passed validation. Why is that number misleading?

**기존** 팀이 검증을 통과한 레코드에서만 측정한 97%의 정확도를 보고한다. 이 수치가 오해의 소지가 있는 이유는 무엇인가?

**신규** 팀에서 validation을 통과한 레코드만으로 측정해 정확도가 97%라고 보고한다. 이 수치가 오해를 부르는 이유는 무엇인가?

- A. 기존: 정확도는 레코드 단위가 아니라 필드 단위로 측정해야 한다
  - 신규: 정확도는 레코드 단위가 아니라 필드 단위로 측정해야 한다
- B. 기존: 97%는 보고하기에 너무 낮다
  - 신규: 97%는 보고하기에 너무 낮다
- C. 기존: 검증과 정확도는 무관하다
  - 신규: validation과 정확도는 서로 관계가 없다
- D. 기존: 실패를 제외하므로, 모든 문서에 걸친 실제 비율이 아니라 시스템이 이미 성공한 곳을 측정한다
  - 신규: 실패한 레코드가 빠져 있어서, 전체 문서에 대한 실제 비율이 아니라 시스템이 이미 성공한 부분만 측정한 값이다

**해설 EN** Measuring only validated records is a biased sample; calibration needs coverage of all documents

**해설 기존** 검증된 레코드만 측정하는 것은 편향된 표본이며, 보정에는 모든 문서를 포괄하는 범위가 필요하다

**해설 신규** validation을 통과한 레코드만 재면 표본이 편향된다. 보정(calibration)하려면 모든 문서를 다뤄야 한다.

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

## CCAR-F-Amey-Thakur-0052

**EN** What is the principal cost of introducing a subagent?

**기존** subagent를 도입할 때 치르는 주된 비용은 무엇인가?

**신규** subagent를 도입할 때 가장 큰 비용은 무엇인가?

- A. 기존: handoff에 명시적으로 담아 전달하지 않으면 부모가 가지고 있던 컨텍스트를 잃는다
  - 신규: handoff에 명시적으로 담아 주지 않으면 parent agent가 갖고 있던 context를 잃는다
- B. 기존: 더 큰 모델이 필요하다
  - 신규: 더 큰 모델이 필요하다
- C. 기존: 도구를 사용할 수 없다
  - 신규: 도구를 쓸 수 없다
- D. 기존: 모든 경우에 토큰 비용이 두 배가 된다
  - 신규: 모든 경우에 token 비용이 두 배가 된다

**해설 EN** Delegation buys isolation and pays in context, which is why handoffs must be explicit. A subagent does not require a larger model (B), can use tools (C), and cost varies with the work (D)

**해설 기존** 위임은 격리를 얻는 대신 컨텍스트로 대가를 치르며, 그래서 handoff는 명시적이어야 한다. subagent는 더 큰 모델을 필요로 하지 않고(B), 도구를 사용할 수 있으며(C), 비용은 작업에 따라 달라진다(D)

**해설 신규** 위임하면 context를 격리하는 이점을 얻는 대신 context를 내줘야 하므로 handoff를 명시적으로 해야 한다. subagent에 더 큰 모델이 필요한 것도 아니고(B), 도구도 쓸 수 있으며(C), 비용은 작업에 따라 다르다(D).

## CCAR-F-Amey-Thakur-0053

**EN** An autonomous step would modify production data. What does the architecture require?

**기존** 자율 단계가 프로덕션 데이터를 수정하려 한다. 아키텍처는 무엇을 요구하는가?

**신규** 자율적으로 실행되는 단계가 production 데이터를 수정하려 한다. 아키텍처에는 무엇이 필요한가?

- A. 기존: 더 유능한 모델
  - 신규: 더 성능이 높은 모델
- B. 기존: 주의를 당부하는 더 긴 시스템 프롬프트
  - 신규: 주의를 당부하는 더 긴 system prompt
- C. 기존: 재시도 정책
  - 신규: 재시도 정책
- D. 기존: 사람이 해당 작업을 승인하는 checkpoint 또는 되돌릴 수 있는 메커니즘
  - 신규: 사람이 해당 작업을 승인하는 checkpoint, 또는 되돌릴 수 있는 장치

**해설 EN** Irreversible external effects need an authorisation boundary or reversibility, enforced outside the model. Capability (A), instruction (B), and retries (C) do not bound the consequence

**해설 기존** 되돌릴 수 없는 외부 영향에는 모델 바깥에서 강제되는 승인 경계 또는 가역성이 필요하다. 성능(A), 지시(B), 재시도(C)는 결과의 범위를 제한하지 못한다

**해설 신규** 되돌릴 수 없는 외부 영향에는 승인 경계나 되돌릴 수 있는 장치가 필요하고, 이는 모델 바깥에서 강제해야 한다. 모델 성능(A), 지시문(B), 재시도(C)로는 피해 범위를 제한하지 못한다.

## CCAR-F-Amey-Thakur-0054

**EN** What most helps diagnose an agentic failure after the fact?

**기존** agentic 실패를 사후에 진단하는 데 가장 도움이 되는 것은 무엇인가?

**신규** agentic 작업이 실패한 뒤 원인을 진단할 때 가장 도움이 되는 것은 무엇인가?

- A. 기존: 최종 출력만
  - 신규: 최종 출력만
- B. 기존: 각 단계의 입력, 도구 호출, 출력에 대한 trace
  - 신규: 각 단계의 입력, 도구 호출, 출력을 기록한 trace
- C. 기존: 총 토큰 수
  - 신규: 전체 token 수
- D. 기존: 모델 버전
  - 신규: 모델 버전

**해설 EN** A per-step trace reconstructs a nondeterministic run, which is what diagnosis needs. The final output (A), token totals (C), and version (D) do not show where it diverged

**해설 기존** 단계별 trace는 비결정적인 실행을 재구성할 수 있게 해 주며, 이것이 진단에 필요한 것이다. 최종 출력(A), 토큰 합계(C), 버전(D)은 어디서 어긋났는지 보여 주지 못한다

**해설 신규** 단계별 trace가 있어야 매번 결과가 달라질 수 있는 실행을 재구성해 진단할 수 있다. 최종 출력(A), token 총량(C), 버전(D)으로는 어느 지점에서 어긋났는지 알 수 없다.

## CCAR-F-Amey-Thakur-0055

**EN** Where should repository-wide conventions for Claude Code live?

**기존** Claude Code를 위한 저장소 전체 규약은 어디에 두어야 하는가?

**신규** Claude Code용 저장소 전체 규칙은 어디에 두어야 하는가?

- A. 기존: 각 개발자의 로컬 설정
  - 신규: 각 개발자의 로컬 설정
- B. 기존: 저장소에 커밋된 CLAUDE.md
  - 신규: 저장소에 commit한 CLAUDE.md
- C. 기존: 팀의 채팅 채널
  - 신규: 팀 chat 채널
- D. 기존: CI 설정에만
  - 신규: CI 설정에만

**해설 EN** Committed project memory is shared, versioned, and reviewed with the code. Local configuration (A) does not propagate, chat (C) is not read as context, and CI (D) covers automation rather than interactive work

**해설 기존** 커밋된 프로젝트 메모리는 공유되고, 버전 관리되며, 코드와 함께 리뷰된다. 로컬 설정(A)은 전파되지 않고, 채팅(C)은 컨텍스트로 읽히지 않으며, CI(D)는 대화형 작업이 아니라 자동화를 다룬다

**해설 신규** commit한 project memory는 코드와 함께 공유되고 버전 관리되며 리뷰를 받는다. 로컬 설정(A)은 다른 사람에게 전파되지 않고, chat(C)은 context로 읽히지 않으며, CI(D)는 대화형 작업이 아니라 자동화만 다룬다.

## CCAR-F-Amey-Thakur-0056

**EN** Which task is best suited to headless Claude Code in CI?

**기존** CI에서 headless Claude Code에 가장 적합한 작업은 무엇인가?

**신규** CI에서 headless Claude Code로 돌리기에 가장 알맞은 작업은 무엇인가?

- A. 기존: 익숙하지 않은 실패에 대한 탐색적 디버깅
  - 신규: 익숙하지 않은 실패를 탐색하며 디버깅하는 작업
- B. 기존: 새 모듈의 아키텍처 설계
  - 신규: 새 모듈의 아키텍처를 설계하는 작업
- C. 기존: 개발자와의 페어 프로그래밍
  - 신규: 개발자와 함께 하는 pair programming
- D. 기존: 모든 pull request마다 실행되는, 반복 가능하고 명확히 정의된 검사
  - 신규: 모든 pull request마다 실행되는, 반복 가능하고 명세가 분명한 검사

**해설 EN** Headless execution suits bounded, repeatable work that runs unattended. Exploration (A), design (B), and pairing (C) all depend on a person in the loop

**해설 기존** headless 실행은 사람 없이 돌아가는, 범위가 정해진 반복 작업에 적합하다. 탐색(A), 설계(B), 페어링(C)은 모두 사람이 루프에 있어야 한다

**해설 신규** headless 실행은 범위가 정해져 있고 반복되며 사람 없이 돌아가는 작업에 맞는다. 탐색(A), 설계(B), pair programming(C)은 모두 사람이 중간에 있어야 한다.

## CCAR-F-Amey-Thakur-0057

**EN** What is a hook for?

**기존** hook은 무엇을 위한 것인가?

**신규** hook은 무엇을 위한 것인가?

- A. 기존: 모델과 무관하게, 정해진 시점에 결정론적 동작을 실행하는 것
  - 신규: 모델과 무관하게, 정해진 시점에 결정적인(deterministic) 동작을 실행한다
- B. 기존: 재사용 가능한 지시를 저장하는 것
  - 신규: 재사용할 지시문을 저장한다
- C. 기존: 프로젝트 컨텍스트를 보관하는 것
  - 신규: 프로젝트 context를 담는다
- D. 기존: 모델을 선택하는 것
  - 신규: 모델을 선택한다

**해설 EN** Hooks execute as code at fixed points, which is how a guarantee is enforced. Instructions (B) and context (C) belong in project memory, and model choice (D) is configuration

**해설 기존** hook은 정해진 시점에 코드로 실행되며, 이것이 보장을 강제하는 방식이다. 지시(B)와 컨텍스트(C)는 프로젝트 메모리에 속하고, 모델 선택(D)은 설정이다

**해설 신규** hook은 정해진 시점에 코드로 실행되므로 보장을 강제하는 수단이 된다. 지시문(B)과 context(C)는 project memory에 두고, 모델 선택(D)은 설정에 해당한다.

## CCAR-F-Amey-Thakur-0058

**EN** A pipeline needs output that always conforms to a fixed shape. What is the correct mechanism?

**기존** 파이프라인이 항상 고정된 형태에 맞는 출력을 필요로 한다. 올바른 메커니즘은 무엇인가?

**신규** pipeline이 항상 정해진 형태로 나오는 출력을 필요로 한다. 올바른 방법은 무엇인가?

- A. 기존: 프롬프트에서 형태를 요청하고 결과를 파싱하는 것
  - 신규: prompt에서 형태를 요청하고 결과를 파싱한다
- B. 기존: 정규식으로 산문을 후처리하는 것
  - 신규: 산문 형태의 출력을 정규식으로 후처리한다
- C. 기존: 모델이 충족해야 하는 스키마로 형태를 선언하고, 수신 시 검증하는 것
  - 신규: 모델이 반드시 만족해야 하는 schema로 형태를 선언하고, 받을 때 validation한다
- D. 기존: temperature를 낮추는 것
  - 신규: temperature를 낮춘다

**해설 EN** A declared schema makes the shape a contract rather than a request, and validation closes the loop. Prompt requests (A), text parsing (B), and temperature (D) leave the shape to chance

**해설 기존** 선언된 스키마는 형태를 요청이 아니라 계약으로 만들고, 검증이 루프를 닫는다. 프롬프트 요청(A), 텍스트 파싱(B), temperature(D)는 형태를 우연에 맡긴다

**해설 신규** schema로 선언하면 형태가 요청이 아니라 계약이 되고, validation이 그 계약을 완성한다. prompt 요청(A), 텍스트 파싱(B), temperature(D)는 형태를 우연에 맡긴다.

## CCAR-F-Amey-Thakur-0059

**EN** How should a schema handle a value the source may not contain?

**기존** 스키마는 원본에 없을 수도 있는 값을 어떻게 처리해야 하는가?

**신규** 원본에 없을 수도 있는 값을 schema는 어떻게 다뤄야 하는가?

- A. 기존: 해당 필드를 조용히 생략한다
  - 신규: 필드를 말없이 생략한다
- B. 기존: 그럴듯한 기본값을 채운다
  - 신규: 그럴듯한 기본값을 채운다
- C. 기존: 모든 경우에 빈 문자열을 반환한다
  - 신규: 어떤 경우든 빈 문자열을 반환한다
- D. 기존: 부재를 나타내는 명시적 표현을 정의한다
  - 신규: 값이 없음을 나타내는 표현을 명시적으로 정의한다

**해설 EN** Absence must be representable so a genuine gap is distinguishable from a failure. Silent omission (A) is ambiguous, a plausible default (B) fabricates, and an empty string (C) conflates absence with an empty value

**해설 기존** 부재를 표현할 수 있어야 실제로 값이 없는 것과 실패를 구별할 수 있다. 조용한 생략(A)은 모호하고, 그럴듯한 기본값(B)은 값을 날조하며, 빈 문자열(C)은 부재와 빈 값을 뒤섞는다

**해설 신규** 값이 없는 상태를 표현할 수 있어야, 원본에 실제로 값이 없는 경우와 추출 실패를 구분할 수 있다. 말없이 생략하면(A) 의미가 모호하고, 그럴듯한 기본값(B)은 값을 지어내는 것이며, 빈 문자열(C)은 값이 없는 것과 빈 값을 구별하지 못한다.

## CCAR-F-Amey-Thakur-0060

**EN** Extraction succeeds on typical inputs and fails on unusual ones. What is the most effective response?

**기존** 추출이 일반적인 입력에서는 성공하고 특이한 입력에서는 실패한다. 가장 효과적인 대응은 무엇인가?

**신규** 추출이 일반적인 입력에서는 성공하고 특이한 입력에서는 실패한다. 가장 효과적인 대응은 무엇인가?

- A. 기존: temperature를 높인다
  - 신규: temperature를 높인다
- B. 기존: 더 큰 모델을 사용한다
  - 신규: 더 큰 모델을 쓴다
- C. 기존: 특이한 형식을 다루는 예시를 추가하고 필드가 없을 때 무엇을 반환할지 명시한다
  - 신규: 특이한 형식을 다루는 예시를 추가하고, 필드가 없을 때 무엇을 반환할지 명시한다
- D. 기존: 모델에게 특이한 입력에 주의하라고 요청한다
  - 신규: 특이한 입력에 주의하라고 모델에 당부한다

**해설 EN** The unusual cases fail because they were never specified, and examples plus a missing-value rule specify them. Temperature (A) adds variance, model size (B) is not aimed at the gap, and exhortation (D) is not specification

**해설 기존** 특이한 경우는 한 번도 명시된 적이 없어서 실패하며, 예시와 누락값 규칙이 이를 명시한다. temperature(A)는 변동성을 더하고, 모델 크기(B)는 그 공백을 겨냥하지 않으며, 당부(D)는 명세가 아니다

**해설 신규** 특이한 경우에 실패하는 건 그 경우를 한 번도 명세하지 않았기 때문이고, 예시와 값 없음 처리 규칙이 그 명세가 된다. temperature(A)는 편차만 키우고, 모델 크기(B)는 빈틈을 겨냥한 해법이 아니며, 당부(D)는 명세가 아니다.

## CCAR-F-Amey-Thakur-0061

**EN** What is the clearest sign that a tool surface needs redesign rather than better prompting?

**기존** 더 나은 프롬프팅이 아니라 도구 표면의 재설계가 필요하다는 가장 분명한 신호는 무엇인가?

**신규** 프롬프트를 개선하는 것으로는 부족하고 도구 구성(tool surface)을 다시 설계해야 한다는 가장 분명한 신호는 무엇인가?

- A. 기존: 다섯 개를 넘는 도구를 노출한다
  - 신규: 도구가 5개보다 많다
- B. 기존: 모델이 요청을 충족할 수 없는 도구를 반복해서 선택한다
  - 신규: 모델이 요청을 해결할 수 없는 도구를 반복해서 고른다
- C. 기존: 도구가 서로 다른 서비스에서 구현되어 있다
  - 신규: 도구들이 서로 다른 서비스에서 구현되어 있다
- D. 기존: 도구가 큰 페이로드를 반환한다
  - 신규: 도구가 큰 payload를 반환한다

**해설 EN** Repeated wrong selection indicates the tools are not distinguishable from their descriptions, which is a design fault. Tool count (A) and implementation topology (C) are not faults, and payload size (D) is a separate problem

**해설 기존** 반복되는 잘못된 선택은 도구가 설명만으로는 구별되지 않는다는 뜻이며, 이는 설계 결함이다. 도구 개수(A)와 구현 토폴로지(C)는 결함이 아니고, 페이로드 크기(D)는 별개의 문제다

**해설 신규** 잘못된 도구를 반복해서 고른다는 것은 description만으로는 도구를 구별할 수 없다는 뜻이고, 이는 설계 결함이다. 도구 개수(A)나 구현이 나뉜 구조(C)는 결함이 아니고, payload 크기(D)는 별개의 문제다.

## CCAR-F-Amey-Thakur-0062

**EN** How should a tool that deletes records be constrained?

**기존** 레코드를 삭제하는 도구는 어떻게 제약해야 하는가?

**신규** 레코드를 삭제하는 도구는 어떻게 제한해야 하는가?

- A. 기존: 모델 바깥에서 권한과 범위를 강제한다
  - 신규: 모델 바깥에서 권한과 범위를 강제한다
- B. 기존: 모델에게 조심해서 사용하라고 경고하는 설명을 둔다
  - 신규: 조심해서 쓰라고 모델에 경고하는 description을 둔다
- C. 기존: 더 많은 파라미터를 요구한다
  - 신규: 필요한 parameter를 더 많이 요구한다
- D. 기존: 도구 목록의 맨 끝에 선언한다
  - 신규: 도구 목록의 맨 마지막에 선언한다

**해설 EN** Destructive capability is bounded by the surrounding system, since a description is a request rather than a control. Extra parameters (C) and ordering (D) do not limit authority

**해설 기존** 파괴적인 능력은 주변 시스템이 제한하는 것이며, 설명은 통제가 아니라 요청이기 때문이다. 추가 파라미터(C)와 순서(D)는 권한을 제한하지 않는다

**해설 신규** description은 요청일 뿐 통제 수단이 아니므로, 파괴적인 기능은 시스템이 바깥에서 제한해야 한다. parameter를 늘리거나(C) 순서를 바꾸는 것(D)으로는 권한이 제한되지 않는다.

## CCAR-F-Amey-Thakur-0063

**EN** An MCP integration exposes an entire database through one general query tool. What is the architectural concern?

**기존** MCP 통합이 하나의 범용 쿼리 도구로 데이터베이스 전체를 노출한다. 아키텍처상의 우려는 무엇인가?

**신규** MCP 통합이 범용 query 도구 하나로 데이터베이스 전체를 노출한다. 아키텍처상 무엇이 문제인가?

- A. 기존: 모델의 권한이 무제한이 되며, 최소 권한을 적용할 수 없다
  - 신규: 모델의 권한에 한계가 없어서 최소 권한(least privilege)을 적용할 수 없다
- B. 기존: 느려질 것이다
  - 신규: 느려진다
- C. 기존: 토큰을 너무 많이 사용한다
  - 신규: token을 너무 많이 쓴다
- D. 기존: 구조화된 출력을 반환할 수 없다
  - 신규: 구조화된 출력을 반환할 수 없다

**해설 EN** A single unrestricted tool removes the ability to scope what the model may reach. Speed (B) and tokens (C) are secondary, and structured output (D) is achievable either way

**해설 기존** 제한 없는 단일 도구는 모델이 접근할 수 있는 범위를 제한할 수 있는 능력을 없앤다. 속도(B)와 토큰(C)은 부차적이며, 구조화된 출력(D)은 어느 쪽이든 달성할 수 있다

**해설 신규** 제한 없는 도구 하나만 있으면 모델이 접근할 수 있는 범위를 좁힐 수 없다. 속도(B)와 token(C)은 부차적이고, 구조화된 출력(D)은 어느 쪽이든 가능하다.

## CCAR-F-Amey-Thakur-0064

**EN** Quality degrades steadily through a long agentic run. What is the most likely cause?

**기존** 긴 agentic 실행 도중 품질이 꾸준히 저하된다. 가장 가능성이 높은 원인은 무엇인가?

**신규** 긴 agentic 작업을 돌리는 동안 품질이 꾸준히 떨어진다. 가장 가능성 높은 원인은 무엇인가?

- A. 기존: 실행 도중 모델 버전이 바뀌었다
  - 신규: 작업 도중에 모델 버전이 바뀌었다
- B. 기존: 누적된 컨텍스트가 중요한 내용을 희석시켰다
  - 신규: context가 쌓이면서 정말 중요한 내용이 묻혔다
- C. 기존: temperature가 너무 낮다
  - 신규: temperature가 너무 낮다
- D. 기존: 도구가 느려졌다
  - 신규: 도구가 느려졌다

**해설 EN** Progressive degradation over a long run is the signature of context accumulation. Versions do not change mid-run (A), low temperature (C) reduces variety rather than quality, and tool latency (D) does not affect correctness

**해설 기존** 긴 실행 동안 점진적으로 저하되는 것은 컨텍스트 누적의 전형적인 징후다. 버전은 실행 도중 바뀌지 않고(A), 낮은 temperature(C)는 품질이 아니라 다양성을 줄이며, 도구 지연(D)은 정확성에 영향을 주지 않는다

**해설 신규** 긴 작업에서 품질이 점점 나빠지는 것은 context가 누적될 때 나타나는 전형적인 증상이다. 작업 도중에는 버전이 바뀌지 않고(A), 낮은 temperature(C)는 품질이 아니라 다양성을 줄이며, 도구 지연(D)은 정확성에 영향을 주지 않는다.

## CCAR-F-Amey-Thakur-0065

**EN** What must happen for state to survive a compaction boundary?

**기존** 상태가 compaction 경계를 넘어 살아남으려면 무엇이 이루어져야 하는가?

**신규** 상태가 compaction 경계를 넘어 유지되려면 무엇이 필요한가?

- A. 기존: 아무것도 필요 없다. 모델이 중요한 것을 유지한다
  - 신규: 아무것도 필요 없다. 모델이 중요한 내용을 기억한다
- B. 기존: 컨텍스트 윈도우를 확대해야 한다
  - 신규: context window를 늘려야 한다
- C. 기존: 유지되어야 하는 결정과 제약을 명시적으로 이월되는 요약에 기록한다
  - 신규: 유지해야 할 결정과 제약을 다음 단계로 넘기는 요약에 명시적으로 적어 넣는다
- D. 기존: 실행을 다시 시작해야 한다
  - 신규: 작업을 다시 시작해야 한다

**해설 EN** Compaction is lossy, so persistence must be deliberate. Relying on recall (A) is unreliable, a larger window (B) only moves the boundary, and restarting (D) discards the work

**해설 기존** compaction은 손실이 있으므로 유지는 의도적으로 이루어져야 한다. 기억에 의존하는 것(A)은 신뢰할 수 없고, 더 큰 윈도우(B)는 경계를 옮길 뿐이며, 재시작(D)은 작업을 버리는 것이다

**해설 신규** compaction은 정보가 손실되므로 유지할 내용은 의도적으로 남겨야 한다. 모델의 기억에 맡기면(A) 믿을 수 없고, window를 키워도(B) 경계가 뒤로 밀릴 뿐이며, 다시 시작하면(D) 지금까지의 작업이 버려진다.

## CCAR-F-Amey-Thakur-0066

**EN** An agentic design calls the same expensive tool repeatedly with identical arguments. What does this indicate?

**기존** agentic 설계가 비용이 큰 동일한 도구를 동일한 인자로 반복 호출한다. 이는 무엇을 나타내는가?

**신규** agentic 설계에서 비용이 큰 도구를 같은 인자로 계속 반복 호출한다. 이는 무엇을 뜻하는가?

- A. 기존: 건강한 재시도 동작
  - 신규: 정상적인 재시도 동작이다
- B. 기존: 도구가 너무 빠르다
  - 신규: 도구가 너무 빠르다
- C. 기존: agent가 결과를 보유하거나 재사용하지 않고 있으며, 이는 상태 설계를 가리킨다
  - 신규: agent가 결과를 보관하거나 재사용하지 못하고 있으며, 원인은 상태 설계에 있다
- D. 기존: 모델이 너무 유능하다
  - 신규: 모델의 성능이 너무 높다

**해설 EN** Repeating an identical call means the prior result is not available to the agent, which is a state problem. It is not retry behavior (A), and neither tool speed (B) nor capability (D) explains it

**해설 기존** 동일한 호출이 반복된다는 것은 이전 결과를 agent가 사용할 수 없다는 뜻이며, 이는 상태 문제다. 재시도 동작(A)이 아니며, 도구 속도(B)도 능력(D)도 이를 설명하지 못한다

**해설 신규** 똑같은 호출을 반복한다는 것은 이전 결과를 agent가 쓸 수 없다는 뜻이고, 이는 상태 문제다. 재시도 동작도 아니고(A), 도구 속도(B)나 모델 성능(D)으로도 설명되지 않는다.

## CCAR-F-Amey-Thakur-0067

**EN** What determines whether two lines of work belong in separate subagents?

**기존** 두 작업 흐름을 별도의 subagent로 나눌지 여부는 무엇이 결정하는가?

**신규** 두 작업 흐름을 별도의 subagent로 나눠야 하는지는 무엇으로 결정하는가?

- A. 기존: 각각이 상대방이 오염시킬 수 있는 컨텍스트를 필요로 하는지
  - 신규: 한쪽에 필요한 context가 다른 쪽을 오염시키는지
- B. 기존: 둘을 합친 길이
  - 신규: 두 작업을 합친 길이
- C. 기존: 서로 다른 도구를 사용하는지
  - 신규: 서로 다른 도구를 쓰는지
- D. 기존: 병렬로 실행할 수 있는지
  - 신규: 병렬로 실행할 수 있는지

**해설 EN** Context isolation is the reason subagents exist. Length (B), tool difference (C), and parallelism (D) can all be handled within one context

**해설 기존** 컨텍스트 격리가 subagent가 존재하는 이유다. 길이(B), 도구 차이(C), 병렬성(D)은 모두 하나의 컨텍스트 안에서 처리할 수 있다

**해설 신규** subagent가 존재하는 이유는 context를 격리하기 위해서다. 길이(B), 도구 차이(C), 병렬성(D)은 모두 하나의 context 안에서 처리할 수 있다.

## CCAR-F-Amey-Thakur-0068

**EN** Which design most reduces the cost of a wrong autonomous decision?

**기존** 잘못된 자율 결정의 비용을 가장 많이 줄이는 설계는 무엇인가?

**신규** 자율적인 결정이 틀렸을 때의 비용을 가장 많이 줄이는 설계는 무엇인가?

- A. 기존: 더 큰 모델
  - 신규: 더 큰 모델
- B. 기존: 더 긴 프롬프트
  - 신규: 더 긴 prompt
- C. 기존: 더 많은 도구
  - 신규: 더 많은 도구
- D. 기존: 동작을 되돌릴 수 있게 만들거나 확인 뒤에 게이트로 두는 것
  - 신규: 동작을 되돌릴 수 있게 만들거나, 확인을 거쳐야 실행되게 한다

**해설 EN** Reversibility and gating bound the consequence, which is what the risk is. Capability (A), prompt length (B), and tools (C) affect the chance of error rather than its cost

**해설 기존** 가역성과 게이트는 결과의 범위를 제한하며, 이것이 곧 위험이다. 성능(A), 프롬프트 길이(B), 도구(C)는 오류의 비용이 아니라 오류가 날 확률에 영향을 준다

**해설 신규** 되돌릴 수 있게 하거나 확인 단계를 두면 피해 범위가 제한된다. 위험이란 곧 그 피해이기 때문이다. 모델 성능(A), prompt 길이(B), 도구(C)는 오류의 비용이 아니라 오류가 날 가능성에 영향을 준다.

## CCAR-F-Amey-Thakur-0069

**EN** A CLAUDE.md has grown to several thousand lines. What is the likely effect?

**기존** CLAUDE.md가 수천 줄로 늘어났다. 예상되는 영향은 무엇인가?

**신규** CLAUDE.md가 수천 줄까지 커졌다. 어떤 영향이 생길 가능성이 높은가?

- A. 기존: 더 많은 컨텍스트를 쓸 수 있으므로 결과가 더 좋아진다
  - 신규: context가 더 많아져서 결과가 좋아진다
- B. 기존: 중요한 지시가 더 이상 적용되지 않는 내용과 경쟁하게 된다
  - 신규: 중요한 지시문이 더 이상 해당하지 않는 내용과 경쟁하게 된다
- C. 기존: 한 번만 읽히므로 영향이 없다
  - 신규: 한 번만 읽으므로 영향이 없다
- D. 기존: 응답이 더 빨라진다
  - 신규: 응답이 빨라진다

**해설 EN** Project memory is context and dilutes like any other. More is not automatically better (A), it is not free (C), and it does not speed anything up (D)

**해설 기존** 프로젝트 메모리는 컨텍스트이며 다른 컨텍스트와 마찬가지로 희석된다. 많다고 자동으로 좋은 것은 아니고(A), 공짜가 아니며(C), 무엇도 빠르게 만들지 않는다(D)

**해설 신규** project memory도 context이므로 다른 context처럼 희석된다. 많다고 무조건 좋은 것은 아니고(A), 공짜도 아니며(C), 속도를 높여 주지도 않는다(D).

## CCAR-F-Amey-Thakur-0070

**EN** What should be true of a skill before it is committed to a shared repository?

**기존** skill을 공유 저장소에 커밋하기 전에 어떤 조건이 충족되어야 하는가?

**신규** skill을 공유 저장소에 commit하기 전에 무엇이 충족되어야 하는가?

- A. 기존: 쓸모 있을 만큼 길다
  - 신규: 쓸모 있을 만큼 길다
- B. 기존: 팀이 실제로 반복하는 절차를 담고 있으며, 리뷰할 수 있다
  - 신규: 팀이 실제로 반복하는 절차를 담고 있고, 리뷰할 수 있다
- C. 기존: 가장 시니어인 엔지니어가 작성했다
  - 신규: 가장 경력이 많은 엔지니어가 작성했다
- D. 기존: 모든 엣지 케이스를 다룬다
  - 신규: 모든 edge case를 다룬다

**해설 EN** A shared skill is justified by genuine repetition and must be reviewable like code. Length (A), authorship (C), and exhaustiveness (D) do not establish that

**해설 기존** 공유 skill은 실제 반복으로 정당화되며 코드처럼 리뷰할 수 있어야 한다. 길이(A), 작성자(C), 포괄성(D)은 이를 입증하지 못한다

**해설 신규** 공유 skill은 실제로 반복되는 절차가 있어야 정당하고, 코드처럼 리뷰할 수 있어야 한다. 길이(A), 작성자(C), 빠짐없는 포괄성(D)으로는 그것을 입증하지 못한다.

## CCAR-F-Amey-Thakur-0071

**EN** Why is committed configuration preferable to per-developer configuration for team conventions?

**기존** 팀 규약에 대해 개발자별 설정보다 커밋된 설정이 더 나은 이유는 무엇인가?

**신규** 팀 규칙을 개발자별 설정이 아니라 commit한 설정에 두는 편이 나은 이유는 무엇인가?

- A. 기존: 로드가 더 빠르다
  - 신규: 로드가 더 빠르다
- B. 기존: 컨텍스트를 덜 사용한다
  - 신규: context를 덜 쓴다
- C. 기존: 재정의할 수 없다
  - 신규: 덮어쓸 수 없다
- D. 기존: 버전 관리되고 리뷰되며, 자동화를 포함한 모두에게 적용된다
  - 신규: 버전 관리와 리뷰를 거치고, 자동화를 포함한 모든 사람에게 적용된다

**해설 EN** Shared, reviewed, versioned context is what makes a convention hold across people and CI. Speed (A) and context size (B) are not the reason, and it can still be overridden locally (C)

**해설 기존** 공유되고 리뷰되며 버전 관리되는 컨텍스트가 규약이 사람과 CI 전반에서 유지되게 한다. 속도(A)와 컨텍스트 크기(B)는 이유가 아니며, 로컬에서 여전히 재정의할 수 있다(C)

**해설 신규** 공유되고 리뷰를 거치며 버전 관리되는 context여야 규칙이 사람과 CI 전반에서 유지된다. 속도(A)나 context 크기(B)는 이유가 아니고, 로컬에서 덮어쓸 수 있으므로(C) 맞지 않는 설명이다.

## CCAR-F-Amey-Thakur-0072

**EN** A schema-validated response fails validation once in every few hundred calls. What is the correct handling?

**기존** 스키마로 검증하는 응답이 수백 번의 호출 중 한 번꼴로 검증에 실패한다. 올바른 처리는 무엇인가?

**신규** schema로 검증하는 응답이 수백 번 호출에 한 번꼴로 validation에 실패한다. 어떻게 처리해야 하는가?

- A. 기존: fallback 경로를 정의한다. 재시도한 뒤, 잘못된 데이터를 그대로 넘기지 말고 명시적으로 실패시킨다
  - 신규: fallback 경로를 정의한다. 재시도하고, 그래도 안 되면 잘못된 데이터를 그대로 넘기지 말고 명시적으로 실패 처리한다
- B. 기존: 비율이 낮으므로 무시한다
  - 신규: 비율이 낮으니 무시한다
- C. 기존: 실패를 피하기 위해 검증을 끈다
  - 신규: 실패를 피하려고 validation을 끈다
- D. 기존: 출력 토큰 한도를 늘린다
  - 신규: 출력 token 한도를 늘린다

**해설 EN** A rare failure still needs a defined path, and silently passing invalid data is the outcome to prevent. Ignoring it (B) and disabling validation (C) do exactly that, and the token limit (D) is not the cause

**해설 기존** 드문 실패에도 정의된 경로가 필요하며, 잘못된 데이터를 조용히 넘기는 것이 막아야 할 결과다. 무시하기(B)와 검증 끄기(C)가 바로 그렇게 하며, 토큰 한도(D)는 원인이 아니다

**해설 신규** 드문 실패에도 정해진 처리 경로가 있어야 하며, 막아야 할 것은 잘못된 데이터가 조용히 통과하는 결과다. 무시하거나(B) validation을 끄는 것(C)이 바로 그 결과를 낳고, token 한도(D)는 원인이 아니다.

## CCAR-F-Amey-Thakur-0073

**EN** What is the advantage of validating structured output at the boundary rather than downstream?

**기존** 구조화된 출력을 하위 단계가 아니라 경계에서 검증하면 어떤 이점이 있는가?

**신규** 구조화된 출력을 downstream이 아니라 경계에서 validation하면 어떤 점이 유리한가?

- A. 기존: 더 저렴하다
  - 신규: 비용이 더 싸다
- B. 기존: 스키마가 필요 없어진다
  - 신규: schema가 필요 없어진다
- C. 기존: 이후 단계를 오염시키기 전에, 아직 재시도하거나 거부할 수 있는 지점에서 실패를 잡는다
  - 신규: 재시도하거나 거부할 수 있는 시점에 실패를 잡아서, 이후 단계가 오염되기 전에 막는다
- D. 기존: 모델 정확도를 높인다
  - 신규: 모델의 정확도가 올라간다

**해설 EN** Catching at the boundary contains the fault. It is not primarily a cost question (A), the schema is what makes it possible (B), and it does not change the model's accuracy (D)

**해설 기존** 경계에서 잡으면 결함이 확산되지 않는다. 주로 비용의 문제가 아니고(A), 이를 가능하게 하는 것이 바로 스키마이며(B), 모델의 정확도를 바꾸지도 않는다(D)

**해설 신규** 경계에서 잡으면 결함이 퍼지지 않는다. 핵심은 비용이 아니고(A), validation을 가능하게 하는 것이 schema이며(B), 모델의 정확도 자체는 달라지지 않는다(D).

## CCAR-F-Amey-Thakur-0074

**EN** A structured extraction must record where in the source each value came from. What does this require?

**기존** 구조화된 추출이 각 값이 원본의 어디에서 왔는지 기록해야 한다. 이를 위해 필요한 것은 무엇인가?

**신규** 구조화된 추출에서 각 값이 원본의 어디에서 나왔는지 기록해야 한다. 무엇이 필요한가?

- A. 기존: 더 큰 모델
  - 신규: 더 큰 모델
- B. 기존: 더 긴 프롬프트
  - 신규: 더 긴 prompt
- C. 기존: 두 번째 추출 패스
  - 신규: 추출을 한 번 더 하는 두 번째 pass
- D. 기존: 모델이 채워야 하는 출처(provenance) 필드를 포함하는 스키마
  - 신규: 모델이 채워야 하는 provenance 필드를 schema에 포함한다

**해설 EN** Anything the output must carry has to be part of the declared shape. Model size (A) and prompt length (B) do not create a field, and a second pass (C) is unnecessary if the schema asks for it

**해설 기존** 출력이 담아야 하는 것은 무엇이든 선언된 형태의 일부여야 한다. 모델 크기(A)와 프롬프트 길이(B)는 필드를 만들어 내지 못하며, 스키마가 요구한다면 두 번째 패스(C)는 불필요하다

**해설 신규** 출력에 담아야 하는 정보는 선언한 형태 안에 들어 있어야 한다. 모델 크기(A)나 prompt 길이(B)로는 필드가 생기지 않고, schema가 요구하기만 하면 두 번째 pass(C)는 필요 없다.

## CCAR-F-Amey-Thakur-0075

**EN** Two tools do nearly the same thing with different names. What is the architectural fault?

**기존** 두 도구가 이름만 다를 뿐 거의 같은 일을 한다. 아키텍처상의 결함은 무엇인가?

**신규** 이름만 다르고 거의 같은 일을 하는 도구가 두 개 있다. 아키텍처상 무엇이 결함인가?

- A. 기존: 코드 중복
  - 신규: 코드 중복
- B. 기존: 더 높은 지연 시간
  - 신규: 높은 latency
- C. 기존: 모델이 둘 중 하나를 고를 신뢰할 만한 근거가 없다
  - 신규: 모델이 둘 중 하나를 고를 믿을 만한 근거가 없다
- D. 기존: 토큰 비용 증가
  - 신규: token 비용 증가

**해설 EN** Ambiguity at the point of selection is the fault, because the model chooses from descriptions. Code duplication (A), latency (B), and cost (D) are secondary consequences

**해설 기존** 모델은 설명을 보고 선택하므로, 선택 시점의 모호함이 결함이다. 코드 중복(A), 지연 시간(B), 비용(D)은 부차적인 결과다

**해설 신규** 모델은 description을 보고 도구를 고르므로, 선택 시점의 모호함이 결함이다. 코드 중복(A), latency(B), 비용(D)은 부차적인 결과다.

## CCAR-F-Amey-Thakur-0076

**EN** What should a tool do when given arguments it cannot satisfy?

**기존** 도구가 충족할 수 없는 인자를 받았을 때 어떻게 해야 하는가?

**신규** 도구가 처리할 수 없는 인자를 받으면 어떻게 해야 하는가?

- A. 기존: 할 수 있는 가장 비슷한 결과를 반환한다
  - 신규: 가능한 한 가장 비슷한 결과를 반환한다
- B. 기존: 무엇이 잘못되었는지 명확히 밝히는 오류를 반환하여 모델이 호출을 바로잡을 수 있게 한다
  - 신규: 무엇이 잘못되었는지 분명히 밝힌 에러를 반환해서, 모델이 호출을 고칠 수 있게 한다
- C. 기존: 빈 결과를 반환한다
  - 신규: 빈 결과를 반환한다
- D. 기존: 실행을 종료시키는 예외를 발생시킨다
  - 신규: 실행을 종료시키는 exception을 발생시킨다

**해설 EN** An informative error keeps the model able to adapt. A closest-guess (A) and an empty result (C) are silently wrong, and terminating (D) discards a recoverable run

**해설 기존** 유익한 오류는 모델이 적응할 수 있게 해 준다. 가장 비슷한 추측(A)과 빈 결과(C)는 조용히 틀린 것이며, 종료(D)는 복구 가능한 실행을 버리는 것이다

**해설 신규** 정보가 담긴 에러를 줘야 모델이 스스로 대응할 수 있다. 가장 비슷한 결과를 짐작해 반환하거나(A) 빈 결과를 돌려주면(C) 조용히 틀린 결과가 되고, 실행을 종료하면(D) 복구할 수 있는 작업을 버리게 된다.

## CCAR-F-Amey-Thakur-0077

**EN** An MCP tool exposes a write operation that the use case never needs. What should happen?

**기존** MCP 도구가 사용 사례에서 전혀 필요하지 않은 쓰기 작업을 노출한다. 어떻게 해야 하는가?

**신규** MCP 도구가 이 용도에는 전혀 필요 없는 쓰기 작업을 노출하고 있다. 어떻게 해야 하는가?

- A. 기존: 제거한다. 쓰이지 않는 권한은 불필요한 위험이기 때문이다
  - 신규: 제거한다. 쓰지 않는 권한은 불필요한 위험이기 때문이다
- B. 기존: 나중에 유용할 수 있으니 그대로 둔다
  - 신규: 나중에 쓸 수도 있으니 그대로 둔다
- C. 기존: 사용해서는 안 된다고 문서화한다
  - 신규: 사용하지 말라고 문서에 적어 둔다
- D. 기존: 사용을 말리도록 이름을 바꾼다
  - 신규: 쓰지 않도록 이름을 바꾼다

**해설 EN** Authority that is not needed should not be granted. Retaining it for possible future use (B), documenting (C), or renaming (D) all leave the capability reachable

**해설 기존** 필요하지 않은 권한은 부여해서는 안 된다. 앞으로의 사용 가능성을 위해 남겨 두거나(B), 문서화하거나(C), 이름을 바꾸는(D) 것은 모두 그 능력을 접근 가능한 상태로 남겨 둔다

**해설 신규** 필요 없는 권한은 부여하지 않아야 한다. 나중에 쓸지 모른다며 남겨 두거나(B), 문서화하거나(C), 이름을 바꿔도(D) 그 기능에는 여전히 접근할 수 있다.

## CCAR-F-Amey-Thakur-0078

**EN** What is the earliest reliable signal that context management has failed in a long run?

**기존** 긴 실행에서 컨텍스트 관리가 실패했음을 보여 주는 가장 이른 신뢰할 만한 신호는 무엇인가?

**신규** 긴 작업에서 context 관리가 실패했음을 가장 일찍 알려 주는 믿을 만한 신호는 무엇인가?

- A. 기존: agent가 작업을 반복하거나 앞선 결정과 모순되기 시작한다
  - 신규: agent가 같은 일을 반복하거나 앞서 내린 결정과 모순되기 시작한다
- B. 기존: 실행이 예상보다 오래 걸린다
  - 신규: 작업이 예상보다 오래 걸린다
- C. 기존: 토큰 비용이 증가한다
  - 신규: token 비용이 오른다
- D. 기존: 도구가 오류를 반환한다
  - 신규: 도구가 에러를 반환한다

**해설 EN** Repetition and self-contradiction are the behavioral signature of lost state. Duration (B) and cost (C) rise for many reasons, and a tool error (D) is unrelated

**해설 기존** 반복과 자기모순은 상태를 잃었을 때 나타나는 행동적 징후다. 소요 시간(B)과 비용(C)은 여러 이유로 증가하며, 도구 오류(D)는 관련이 없다

**해설 신규** 같은 일을 반복하고 스스로 모순되는 것은 상태를 잃었을 때 나타나는 행동상의 특징이다. 소요 시간(B)과 비용(C)은 여러 이유로 늘어나고, 도구 에러(D)는 관련이 없다.

## CCAR-F-Amey-Thakur-0079

**EN** Why is a defined success criterion necessary for a reliable agentic system?

**기존** 신뢰할 수 있는 agentic 시스템에 정의된 성공 기준이 필요한 이유는 무엇인가?

**신규** 신뢰할 수 있는 agentic 시스템에 성공 기준을 정의해야 하는 이유는 무엇인가?

- A. 기존: 토큰 비용을 줄인다
  - 신규: token 비용이 줄어든다
- B. 기존: 이것이 없으면 완료와 실패를 구분할 방법이 없어, 시스템이 올바르게 멈추거나 측정될 수 없다
  - 신규: 기준이 없으면 완료와 실패를 구별할 수 없어서, 시스템이 제대로 멈추지도 못하고 성능을 측정하지도 못한다
- C. 기존: 프롬프트를 더 짧게 만든다
  - 신규: prompt가 짧아진다
- D. 기존: 플랫폼이 요구한다
  - 신규: 플랫폼이 요구한다

**해설 EN** Termination and measurement both depend on a definition of done. Cost (A), prompt length (C), and platform requirements (D) are not the reason

**해설 기존** 종료와 측정은 모두 완료에 대한 정의에 의존한다. 비용(A), 프롬프트 길이(C), 플랫폼 요구 사항(D)은 이유가 아니다

**해설 신규** 종료와 측정은 둘 다 완료의 정의에 달려 있다. 비용(A), prompt 길이(C), 플랫폼 요구 사항(D)은 이유가 아니다.

## CCAR-F-Amey-Thakur-0080

**EN** A reliability requirement says wrong output must never reach the user unnoticed. What does the design need?

**기존** 신뢰성 요구 사항에 따르면 잘못된 출력이 알려지지 않은 채 사용자에게 도달해서는 안 된다. 설계에는 무엇이 필요한가?

**신규** 신뢰성 요구 사항이 잘못된 출력이 사용자에게 눈치채지 못한 채 전달되어서는 안 된다고 한다. 설계에는 무엇이 필요한가?

- A. 기존: 더 유능한 모델
  - 신규: 더 성능이 높은 모델
- B. 기존: 프롬프트의 더 많은 예시
  - 신규: prompt에 예시 추가
- C. 기존: 탐지가 발동했을 때 취할 동작이 정의된 탐지 단계
  - 신규: 감지 단계, 그리고 감지되었을 때 취할 조치
- D. 기존: 더 긴 컨텍스트 윈도우
  - 신규: 더 긴 context window

**해설 EN** Preventing silent error requires detection plus a response. Capability (A), examples (B), and context (D) improve the average case without catching the bad one

**해설 기존** 조용한 오류를 막으려면 탐지와 대응이 모두 필요하다. 성능(A), 예시(B), 컨텍스트(D)는 평균적인 경우를 개선할 뿐 나쁜 경우를 잡아내지는 못한다

**해설 신규** 오류가 조용히 넘어가는 것을 막으려면 감지와 대응이 함께 있어야 한다. 모델 성능(A), 예시(B), context(D)는 평균적인 경우를 개선할 뿐 잘못된 출력을 잡아내지는 못한다.

## CCAR-F-paullarionov-0001

**EN** A document analysis agent discovers that two credible sources contain directly contradictory statistics for a key metric: a government report states 40% growth, while an industry analysis states 12%. Both sources look credible, and the discrepancy could materially affect the research conclusions. How should the document analysis agent handle this situation most effectively?

Which approach is most effective?

**기존** 문서 분석 agent가 핵심 지표에 대해 신뢰할 만한 두 출처가 정면으로 모순되는 통계를 담고 있음을 발견한다. 정부 보고서는 40% 성장이라고 하고, 업계 분석은 12%라고 한다. 두 출처 모두 신뢰할 만해 보이며, 이 불일치는 연구 결론에 실질적인 영향을 줄 수 있다. 문서 분석 agent는 이 상황을 어떻게 처리하는 것이 가장 효과적인가?

어떤 접근이 가장 효과적인가?

**신규** 문서 분석 agent가 핵심 지표에 대해 신뢰할 만한 두 자료의 통계가 정면으로 모순된다는 것을 발견했다. 정부 보고서는 40% 성장, 업계 분석은 12%라고 한다. 두 자료 모두 믿을 만해 보이고, 이 차이는 연구 결론에 중대한 영향을 줄 수 있다. 문서 분석 agent는 이 상황을 어떻게 처리하는 것이 가장 효과적인가?

어떤 접근이 가장 효과적인가?

- A. 기존: 신뢰도 휴리스틱을 적용해 가장 그럴듯한 정확한 수치를 고르고, 그 값으로 분석을 마치며, 불일치를 언급하는 각주를 추가한다.
  - 신규: 신뢰도 휴리스틱으로 더 맞을 법한 수치를 골라 그 값으로 분석을 마치고, 차이가 있다는 점은 각주로 덧붙인다.
- B. 기존: 두 수치를 상충한다고 표시하지 않은 채 분석 출력에 모두 포함하고, 더 넓은 맥락에 따라 어느 것을 쓸지 synthesis agent가 결정하게 한다.
  - 신규: 두 수치를 충돌한다는 표시 없이 분석 출력에 모두 넣고, 더 넓은 context를 바탕으로 어느 쪽을 쓸지 synthesis agent가 정하게 한다.
- C. 기존: 분석을 멈추고 즉시 coordinator에게 escalation하여, 계속하기 전에 어느 출처가 더 권위 있는지 결정해 달라고 요청한다.
  - 신규: 분석을 멈추고 바로 coordinator에게 escalation해서, 어느 자료가 더 권위 있는지 정해 준 뒤에 계속하도록 한다.
- D. 기존: 두 수치로 분석을 완료하고, 출처를 밝혀 충돌을 명시적으로 주석 처리한 뒤, synthesis로 넘기기 전에 coordinator가 데이터를 어떻게 조정할지 결정하게 한다.
  - 신규: 두 수치를 모두 담아 분석을 마치되 충돌이 있음을 출처와 함께 명시적으로 표시하고, synthesis로 넘기기 전에 coordinator가 데이터를 어떻게 조정할지 정하게 한다.

**해설 EN** This approach preserves separation of responsibilities: the analysis agent completes its core work without blocking, preserves both conflicting values with clear attribution, and correctly passes reconciliation to the coordinator, which has broader context.

**해설 기존** 이 접근은 책임의 분리를 유지한다. 분석 agent는 작업을 막힘 없이 핵심 업무를 완료하고, 상충하는 두 값을 명확한 출처 표기와 함께 보존하며, 더 넓은 맥락을 가진 coordinator에게 조정을 올바르게 넘긴다.

**해설 신규** 이 접근은 역할 분리를 지킨다. 분석 agent는 막히지 않고 핵심 작업을 끝내고, 충돌하는 두 값을 출처와 함께 분명히 남기며, 조정은 더 넓은 context를 가진 coordinator에게 올바르게 넘긴다.

## CCAR-F-paullarionov-0002

**EN** The web-search and document-analysis agents have completed their tasks and returned results to the coordinator. What is the next step for creating an integrated research report?

Which next step is most appropriate?

**기존** 웹 검색 agent와 문서 분석 agent가 작업을 마치고 결과를 coordinator에게 반환했다. 통합된 연구 보고서를 만들기 위한 다음 단계는 무엇인가?

어떤 다음 단계가 가장 적절한가?

**신규** web-search agent와 document-analysis agent가 작업을 마치고 결과를 coordinator에 돌려줬다. 통합된 연구 보고서를 만들려면 다음 단계는 무엇인가?

다음 단계로 가장 적절한 것은 무엇인가?

- A. 기존: 각 agent가 coordinator를 거치지 않고 결과를 보고서 작성 agent에게 직접 보낸다.
  - 신규: 각 agent가 coordinator를 거치지 않고 결과를 보고서 작성 agent에 직접 보낸다.
- B. 기존: 문서 분석 agent가 웹 검색 결과를 요청하여 내부적으로 병합한다.
  - 신규: 문서 분석 agent가 web-search 결과를 요청해서 내부에서 합친다.
- C. 기존: coordinator가 두 결과 집합을 synthesis agent에게 넘겨 통합된 결과로 합친다.
  - 신규: coordinator가 두 결과를 모두 synthesis agent에 넘겨 하나로 통합하게 한다.
- D. 기존: coordinator가 두 agent의 원시 출력을 이어 붙여 최종 결과로 반환한다.
  - 신규: coordinator가 두 agent의 원본 출력을 이어 붙여 최종 결과로 반환한다.

**해설 EN** In a coordinator–subagent architecture, the coordinator forwards both result sets to the synthesis agent for centralized integration, preserving control and ensuring high-quality merging.

**해설 기존** coordinator–subagent 아키텍처에서는 coordinator가 두 결과 집합을 synthesis agent에게 전달해 중앙에서 통합하며, 이로써 통제를 유지하고 고품질 병합을 보장한다.

**해설 신규** coordinator-subagent 아키텍처에서는 coordinator가 두 결과를 synthesis agent에 전달해 한곳에서 통합한다. 그래야 제어가 유지되고 품질 높게 합쳐진다.

## CCAR-F-paullarionov-0003

**EN** A document analysis subagent frequently fails when processing PDF files: some have corrupted sections that trigger parsing exceptions, others are password-protected, and sometimes the parsing library hangs on large files. Currently, any exception immediately terminates the subagent and returns an error to the coordinator, which must decide whether to retry, skip, or fail the whole task. This causes excessive coordinator involvement in routine error handling. What architectural improvement is most effective?

Which improvement is most effective?

**기존** 문서 분석 subagent가 PDF 파일을 처리할 때 자주 실패한다. 일부는 손상된 구간 때문에 파싱 예외가 발생하고, 일부는 비밀번호로 보호되어 있으며, 큰 파일에서는 파싱 라이브러리가 멈추기도 한다. 현재는 어떤 예외든 subagent를 즉시 종료시키고 coordinator에게 오류를 반환하며, coordinator는 재시도, 건너뛰기, 전체 작업 실패 중 무엇을 할지 결정해야 한다. 이 때문에 일상적인 오류 처리에 coordinator가 과도하게 관여하게 된다. 가장 효과적인 아키텍처 개선은 무엇인가?

어떤 개선이 가장 효과적인가?

**신규** 문서 분석 subagent가 PDF 파일을 처리하다가 자주 실패한다. 일부는 손상된 부분 때문에 파싱 exception이 발생하고, 일부는 비밀번호로 보호되어 있고, 큰 파일에서는 파싱 라이브러리가 멈추기도 한다. 지금은 exception이 발생하면 곧바로 subagent가 종료되고 coordinator에 에러가 반환된다. coordinator는 재시도할지, 건너뛸지, 전체 작업을 실패 처리할지 정해야 한다. 이 때문에 일상적인 에러 처리에 coordinator가 지나치게 관여한다. 어떤 아키텍처 개선이 가장 효과적인가?

어떤 개선이 가장 효과적인가?

- A. 기존: 공유 큐를 통해 모든 실패를 모니터링하고 복구 동작을 결정하여 subagent에 직접 재시작 명령을 보내는 전용 오류 처리 agent를 만든다.
  - 신규: 공유 queue로 모든 실패를 감시하며 복구 조치를 정하고 subagent에 재시작 명령을 직접 보내는 에러 처리 전용 agent를 만든다.
- B. 기존: subagent가 항상 성공 상태와 함께 부분 결과를 반환하고 오류 세부 정보는 metadata에 담도록 구성하며, coordinator는 모든 응답을 성공으로 취급한다.
  - 신규: subagent가 항상 성공 상태로 부분 결과를 반환하게 하고 에러 상세는 metadata에 넣는다. coordinator는 모든 응답을 성공으로 취급한다.
- C. 기존: coordinator가 모든 문서를 subagent에 보내기 전에 검증하여, 실패를 일으킬 수 있는 문서를 거부하게 한다.
  - 신규: coordinator가 모든 문서를 subagent에 보내기 전에 검증해서, 실패를 일으킬 수 있는 문서는 거부한다.
- D. 기존: 일시적인 실패는 subagent 안에서 로컬로 복구하고, 스스로 해결할 수 없는 오류만 시도한 단계와 부분 결과를 포함해 coordinator에게 escalation한다.
  - 신규: 일시적인 실패는 subagent 안에서 직접 복구하고, 해결할 수 없는 에러만 시도한 단계와 부분 결과를 함께 담아 coordinator에 escalation한다.

**해설 EN** Handle errors at the lowest level capable of resolving them. Local recovery reduces coordinator workload while still escalating truly unrecoverable issues with full context and partial progress.

**해설 기존** 오류는 이를 해결할 수 있는 가장 낮은 수준에서 처리한다. 로컬 복구는 coordinator의 업무량을 줄이면서도, 정말로 복구할 수 없는 문제는 전체 컨텍스트와 부분 진행 상황과 함께 escalation한다.

**해설 신규** 에러는 해결할 수 있는 가장 낮은 수준에서 처리한다. 로컬에서 복구하면 coordinator의 부담이 줄고, 정말 복구할 수 없는 문제는 전체 context와 진행된 부분 결과를 함께 올려 보낸다.

## CCAR-F-paullarionov-0004

**EN** After running the system on “AI impact on creative industries,” you observe that every subagent completes successfully: the web-search agent finds relevant articles, the document analysis agent summarizes them correctly, and the synthesis agent produces coherent text. However, final reports cover only visual art and completely miss music, literature, and film. In the coordinator logs, you see it decomposed the topic into three subtasks: “AI in digital art,” “AI in graphic design,” and “AI in photography.” What is the most likely root cause?

What is the most likely root cause?

**기존** “창작 산업에 대한 AI의 영향”을 주제로 시스템을 실행한 뒤, 모든 subagent가 성공적으로 완료되었음을 확인한다. 웹 검색 agent는 관련 기사를 찾고, 문서 분석 agent는 이를 올바르게 요약하며, synthesis agent는 일관된 텍스트를 만든다. 그런데 최종 보고서는 시각 예술만 다루고 음악, 문학, 영화는 완전히 빠뜨렸다. coordinator 로그를 보면 주제를 “디지털 아트 속 AI”, “그래픽 디자인 속 AI”, “사진 속 AI”라는 세 개의 하위 작업으로 분해했다. 가장 가능성이 높은 근본 원인은 무엇인가?

가장 가능성이 높은 근본 원인은 무엇인가?

**신규** "AI가 창작 산업에 미치는 영향"을 주제로 시스템을 돌려 봤다. 모든 subagent는 정상적으로 끝났다. web-search agent는 관련 기사를 찾았고, document analysis agent는 그 기사를 제대로 요약했으며, synthesis agent는 문맥이 매끄러운 글을 만들었다. 그런데 최종 보고서는 시각 예술만 다루고 음악, 문학, 영화는 전혀 다루지 않았다. coordinator 로그를 보면 이 주제를 "디지털 아트의 AI", "그래픽 디자인의 AI", "사진의 AI"라는 세 가지 하위 작업으로 나누었다. 가장 가능성이 높은 근본 원인은 무엇인가?

- A. 기존: synthesis agent에게 커버리지 공백을 탐지하라는 지시가 없다.
  - 신규: synthesis agent에게 빠진 범위를 찾아내라는 지시가 없다.
- B. 기존: 문서 분석 agent가 지나치게 엄격한 관련성 기준 때문에 시각적이지 않은 출처를 걸러 낸다.
  - 신규: document analysis agent가 관련성 기준을 지나치게 엄격하게 적용해서 시각 예술이 아닌 출처를 걸러낸다.
- C. 기존: coordinator의 작업 분해가 너무 좁아서, 관련된 모든 영역을 포괄하지 못하는 작업을 subagent에 할당한다.
  - 신규: coordinator의 작업 분해가 너무 좁아서, subagent에게 맡긴 일이 관련 영역 전체를 포괄하지 못한다.
- D. 기존: 웹 검색 agent의 쿼리가 불충분하여 더 많은 분야를 포괄하도록 넓혀야 한다.
  - 신규: web-search agent의 검색어가 부족하므로, 더 많은 분야를 포함하도록 넓혀야 한다.

**해설 EN** The coordinator decomposed a broad topic only into visual-art subtasks, missing music, literature, and film entirely. Since subagents executed their assignments correctly, the narrow decomposition is the obvious root cause.

**해설 기존** coordinator가 넓은 주제를 시각 예술 하위 작업으로만 분해하여 음악, 문학, 영화를 완전히 놓쳤다. subagent들은 맡은 일을 올바르게 수행했으므로, 좁은 분해가 명백한 근본 원인이다.

**해설 신규** coordinator가 넓은 주제를 시각 예술 관련 하위 작업으로만 나누었고, 음악·문학·영화는 아예 빠뜨렸다. subagent들은 맡은 일을 제대로 해냈으므로, 근본 원인은 좁게 이루어진 작업 분해다.

## CCAR-F-paullarionov-0005

**EN** The web-search subagent returns results for only 3 of 5 requested source categories (competitor sites and industry reports succeed, but news archives and social feeds time out). The document analysis subagent successfully processes all provided documents. The synthesis subagent must produce a summary from mixed-quality upstream inputs. Which error-propagation strategy is most effective?

Which error-propagation strategy is most effective?

**기존** 웹 검색 subagent가 요청된 5개 출처 범주 중 3개에 대해서만 결과를 반환한다(경쟁사 사이트와 업계 보고서는 성공했지만 뉴스 아카이브와 소셜 피드는 타임아웃). 문서 분석 subagent는 제공된 모든 문서를 성공적으로 처리한다. synthesis subagent는 품질이 섞인 상류 입력으로 요약을 만들어야 한다. 가장 효과적인 오류 전파 전략은 무엇인가?

어떤 오류 전파 전략이 가장 효과적인가?

**신규** web-search subagent가 요청받은 5개 출처 범주 중 3개에서만 결과를 가져왔다. 경쟁사 사이트와 업계 보고서는 성공했지만 뉴스 아카이브와 소셜 피드는 timeout이 났다. document analysis subagent는 받은 문서를 모두 문제없이 처리했다. synthesis subagent는 품질이 고르지 않은 upstream 입력을 가지고 요약을 만들어야 한다. 가장 효과적인 error propagation 전략은 무엇인가?

- A. 기존: 성공한 출처만으로 synthesis를 계속하고, 어떤 데이터를 사용할 수 없었는지 언급하지 않은 채 출력을 만든다.
  - 신규: 성공한 출처만으로 synthesis를 계속하고, 어떤 데이터가 없었는지는 언급하지 않은 채 결과를 낸다.
- B. 기존: synthesis subagent가 coordinator에게 오류를 반환하여, 불완전한 데이터를 이유로 전체 재시도 또는 작업 실패를 유발한다.
  - 신규: synthesis subagent가 coordinator에게 error를 반환해서, 데이터가 불완전하다는 이유로 전체를 다시 시도하거나 작업을 실패 처리한다.
- C. 기존: synthesis subagent가 coordinator에게, synthesis를 시작하기 전에 타임아웃된 출처를 더 긴 타임아웃으로 재시도해 달라고 요청한다.
  - 신규: synthesis subagent가 coordinator에게 요청해, timeout이 난 출처를 더 긴 timeout으로 다시 시도한 뒤에 synthesis를 시작한다.
- D. 기존: synthesis 출력을, 어떤 결론이 충분히 뒷받침되고 사용할 수 없는 출처 때문에 어디에 공백이 있는지 나타내는 커버리지 주석과 함께 구조화한다.
  - 신규: synthesis 결과에 coverage annotation을 달아, 어떤 결론은 근거가 탄탄하고 어느 부분은 출처를 확보하지 못해 공백이 있는지 표시한다.

**해설 EN** Coverage annotations implement graceful degradation with transparency, preserving value from completed work while propagating uncertainty to enable informed decisions about confidence.

**해설 기존** 커버리지 주석은 투명성을 갖춘 graceful degradation을 구현하여, 완료된 작업의 가치를 보존하면서 불확실성을 전파해 신뢰도에 대한 정보에 입각한 결정을 가능하게 한다.

**해설 신규** coverage annotation은 투명성을 유지하면서 기능을 점진적으로 축소하는 graceful degradation을 구현한다. 이미 끝난 작업의 가치를 살리고, 불확실한 부분도 함께 전달하므로 결과를 얼마나 믿을지 판단할 수 있다.

## CCAR-F-paullarionov-0006

**EN** The document analysis subagent encounters a corrupted PDF file that it cannot parse. When designing the system’s error handling, what is the most effective way to handle this failure?

Which approach is most effective?

**기존** 문서 분석 subagent가 파싱할 수 없는 손상된 PDF 파일을 만난다. 시스템의 오류 처리를 설계할 때, 이 실패를 처리하는 가장 효과적인 방법은 무엇인가?

어떤 접근이 가장 효과적인가?

**신규** document analysis subagent가 손상된 PDF 파일을 만나 파싱하지 못한다. 시스템의 error handling을 설계할 때, 이 실패를 처리하는 가장 효과적인 방법은 무엇인가?

- A. 기존: 컨텍스트와 함께 오류를 coordinator agent에게 반환하여 어떻게 진행할지 결정하게 한다.
  - 신규: context를 담은 error를 coordinator agent에게 반환하고, 이후 처리 방식은 coordinator가 정하게 한다.
- B. 기존: 워크플로가 중단되지 않도록 손상된 문서를 조용히 건너뛰고 나머지 파일 처리를 계속한다.
  - 신규: 작업 흐름이 끊기지 않도록 손상된 문서는 조용히 건너뛰고 나머지 파일을 계속 처리한다.
- C. 기존: 실패를 보고하기 전에 exponential backoff로 문서 파싱을 자동으로 세 번 재시도한다.
  - 신규: 실패를 보고하기 전에 exponential backoff로 문서 파싱을 자동으로 세 번 다시 시도한다.
- D. 기존: 전체 연구 워크플로를 종료시키는 예외를 던진다.
  - 신규: exception을 던져서 리서치 workflow 전체를 중단시킨다.

**해설 EN** Returning an error with context to the coordinator is the most effective approach because it lets the coordinator make an informed decision—skip the file, try an alternative parsing method, or notify the user—while maintaining visibility into the failure.

**해설 기존** 컨텍스트와 함께 오류를 coordinator에게 반환하는 것이 가장 효과적인 접근인데, 실패에 대한 가시성을 유지하면서 coordinator가 파일을 건너뛰거나, 다른 파싱 방법을 시도하거나, 사용자에게 알리는 등 정보에 입각한 결정을 내릴 수 있기 때문이다.

**해설 신규** context를 담은 error를 coordinator에게 반환하는 방식이 가장 효과적이다. 실패 상황을 계속 파악할 수 있는 상태에서, coordinator가 그 파일을 건너뛸지, 다른 파싱 방법을 시도할지, 사용자에게 알릴지를 충분한 정보를 바탕으로 결정할 수 있기 때문이다.

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

## CCAR-F-paullarionov-0008

**EN** A colleague proposes that the document analysis agent should send its results directly to the synthesis agent, bypassing the coordinator. What is the main advantage of keeping the coordinator as the central hub for all communication between subagents?

What is the main advantage of keeping the coordinator as the central hub?

**기존** 동료가 문서 분석 agent가 coordinator를 거치지 않고 결과를 synthesis agent에게 직접 보내야 한다고 제안한다. subagent 간의 모든 통신에서 coordinator를 중앙 허브로 유지하는 주된 이점은 무엇인가?

coordinator를 중앙 허브로 유지하는 주된 이점은 무엇인가?

**신규** 동료가 document analysis agent의 결과를 coordinator를 거치지 않고 synthesis agent에게 직접 보내자고 제안한다. subagent 사이의 모든 통신에서 coordinator가 중심 hub 역할을 하는 구조를 유지할 때 얻는 가장 큰 이점은 무엇인가?

- A. 기존: coordinator가 모든 상호작용을 관찰하고, 오류를 일관되게 처리하며, 각 subagent가 어떤 정보를 받을지 결정할 수 있다.
  - 신규: coordinator가 모든 상호작용을 관찰하고, error를 일관되게 처리하며, 각 subagent에게 어떤 정보를 줄지 결정할 수 있다.
- B. 기존: coordinator가 subagent에 대한 여러 요청을 일괄 처리하여 총 API 호출 수와 전체 지연 시간을 줄인다.
  - 신규: coordinator가 subagent에 대한 여러 요청을 묶어서 보내므로 전체 API 호출 수와 지연 시간이 줄어든다.
- C. 기존: coordinator를 거쳐 라우팅하면 agent 간 직접 호출이 지원할 수 없는 자동 재시도 로직을 사용할 수 있다.
  - 신규: coordinator를 거쳐야 agent끼리 직접 호출할 때는 지원할 수 없는 자동 재시도 로직을 쓸 수 있다.
- D. 기존: subagent는 격리된 메모리를 사용하며, 직접 통신하려면 coordinator만 수행할 수 있는 복잡한 직렬화가 필요하다.
  - 신규: subagent는 메모리가 격리되어 있어서, 직접 통신하려면 복잡한 직렬화가 필요하고 그 일은 coordinator만 할 수 있다.

**해설 EN** The coordinator pattern provides centralized visibility into all interactions, uniform error handling across the system, and fine-grained control over what information each subagent receives—these are the primary advantages of a star-shaped communication topology.

**해설 기존** coordinator 패턴은 모든 상호작용에 대한 중앙 집중식 가시성, 시스템 전반의 일관된 오류 처리, 각 subagent가 받는 정보에 대한 세밀한 통제를 제공하며, 이것이 스타형 통신 토폴로지의 주된 이점이다.

**해설 신규** coordinator 패턴은 모든 상호작용을 한곳에서 볼 수 있게 하고, 시스템 전체에서 error를 일관되게 처리하게 하며, 각 subagent가 받는 정보를 세밀하게 통제할 수 있게 해 준다. 이것이 star 형태 통신 구조의 주된 이점이다.

## CCAR-F-paullarionov-0009

**EN** The web-search subagent times out while researching a complex topic. You need to design how information about this failure is returned to the coordinator. Which error-propagation approach best enables intelligent recovery?

Which error-propagation approach best enables intelligent recovery?

**기존** 웹 검색 subagent가 복잡한 주제를 조사하다가 타임아웃된다. 이 실패에 대한 정보를 coordinator에게 어떻게 반환할지 설계해야 한다. 어떤 오류 전파 접근이 지능적인 복구를 가장 잘 가능하게 하는가?

어떤 오류 전파 접근이 지능적인 복구를 가장 잘 가능하게 하는가?

**신규** 복잡한 주제를 조사하던 web-search subagent에서 timeout이 발생했다. 이 실패 정보를 coordinator에게 어떻게 돌려줄지 설계해야 한다. 어떤 error propagation 방식이 똑똑한 복구를 가장 잘 뒷받침하는가?

- A. 기존: 실패 유형, 실행된 쿼리, 부분 결과, 가능한 대안 접근을 포함한 구조화된 오류 컨텍스트를 coordinator에게 반환한다.
  - 신규: 실패 유형, 실행한 쿼리, 부분 결과, 시도해 볼 만한 대안을 담은 구조화된 error context를 coordinator에게 반환한다.
- B. 기존: subagent 안에서 타임아웃을 잡아 성공으로 표시된 빈 결과 집합을 반환한다.
  - 신규: subagent 안에서 timeout을 잡아 처리하고, 성공으로 표시한 빈 결과 집합을 반환한다.
- C. 기존: subagent 안에 자동 exponential-backoff 재시도를 구현하고, 재시도를 모두 소진한 뒤에만 일반적인 “검색 사용 불가” 상태를 반환한다.
  - 신규: subagent 안에서 exponential backoff 재시도를 자동으로 구현하고, 재시도를 모두 소진한 뒤에야 "검색 불가"라는 일반적인 상태만 반환한다.
- D. 기존: 타임아웃 예외를 최상위 핸들러로 직접 전파하여 전체 연구 워크플로를 종료시킨다.
  - 신규: timeout exception을 최상위 handler까지 그대로 전달해서 리서치 workflow 전체를 중단시킨다.

**해설 EN** Returning structured error context—including failure type, executed query, partial results, and alternative approaches—gives the coordinator everything needed to make intelligent recovery decisions (e.g., retry with a modified query or continue with partial results). It preserves maximum context for informed coordination-level decision-making.

**해설 기존** 실패 유형, 실행된 쿼리, 부분 결과, 대안 접근을 포함한 구조화된 오류 컨텍스트를 반환하면 coordinator가 지능적인 복구 결정(예: 수정한 쿼리로 재시도하거나 부분 결과로 계속 진행)을 내리는 데 필요한 모든 것을 얻는다. 이는 정보에 입각한 coordinator 수준의 의사 결정을 위해 최대한의 컨텍스트를 보존한다.

**해설 신규** 실패 유형, 실행한 쿼리, 부분 결과, 대안을 담은 구조화된 error context를 반환하면 coordinator가 똑똑하게 복구를 결정하는 데 필요한 정보를 모두 얻는다. 예를 들어 쿼리를 바꿔 다시 시도하거나 부분 결과만으로 계속 진행할 수 있다. 이렇게 하면 coordinator 수준에서 충분한 정보를 바탕으로 판단하는 데 필요한 context를 최대한 보존한다.

## CCAR-F-paullarionov-0010

**EN** In your system design, you gave the document analysis agent access to a general-purpose tool `fetch_url` so it could download documents by URL. Production logs show this agent now frequently downloads search engine results pages to perform ad hoc web search—behavior that should be routed through the web-search agent—causing inconsistent results. Which fix is most effective?

Which fix is most effective?

**기존** 시스템 설계에서 문서 분석 agent가 URL로 문서를 다운로드할 수 있도록 범용 도구 `fetch_url`에 대한 접근 권한을 주었다. 프로덕션 로그를 보면 이 agent가 이제 검색 엔진 결과 페이지를 다운로드해 임의의 웹 검색을 수행하는 일이 잦은데, 이 동작은 웹 검색 agent를 통해 라우팅되어야 하며 일관되지 않은 결과를 낳는다. 어떤 수정이 가장 효과적인가?

어떤 수정이 가장 효과적인가?

**신규** 시스템을 설계하면서 document analysis agent에게 범용 도구 `fetch_url`을 줘서 URL로 문서를 내려받게 했다. 그런데 운영 로그를 보니 이 agent가 검색 엔진 결과 페이지를 내려받아 즉석에서 웹 검색을 하는 경우가 잦다. 이런 동작은 web-search agent를 거쳐야 하는데, 이 agent가 직접 검색해 버리니 결과가 일관되지 않다. 가장 효과적인 해결책은 무엇인가?

- A. 기존: `fetch_url`을 URL이 문서 형식을 가리키는지 검증하는 `load_document` 도구로 교체한다.
  - 신규: `fetch_url`을 URL이 문서 형식을 가리키는지 검증하는 `load_document` 도구로 바꾼다.
- B. 기존: 문서 분석 agent에서 `fetch_url`을 제거하고 모든 URL 가져오기를 coordinator를 거쳐 웹 검색 agent로 라우팅한다.
  - 신규: document analysis agent에서 `fetch_url`을 없애고, URL을 가져오는 모든 일을 coordinator를 거쳐 web-search agent가 하게 한다.
- C. 기존: 알려진 검색 엔진 도메인에 대한 `fetch_url` 호출은 차단하고 다른 URL은 허용하는 필터링을 구현한다.
  - 신규: `fetch_url`이 알려진 검색 엔진 도메인을 호출하지 못하도록 막고, 그 밖의 URL은 허용하는 필터를 구현한다.
- D. 기존: `fetch_url`은 검색이 아니라 문서 URL을 다운로드하는 용도로만 써야 한다는 지시를 문서 분석 agent 프롬프트에 추가한다.
  - 신규: document analysis agent의 prompt에 `fetch_url`은 문서 URL을 내려받는 용도로만 쓰고 검색에는 쓰지 말라는 지시를 추가한다.

**해설 EN** Replacing a general-purpose tool with a document-specific tool that validates URLs against document formats fixes the root cause by constraining capability at the interface level. This follows the principle of least privilege, making undesired search behavior impossible rather than merely discouraged.

**해설 기존** 범용 도구를 URL이 문서 형식인지 검증하는 문서 전용 도구로 교체하면 인터페이스 수준에서 능력을 제한하여 근본 원인을 해결한다. 이는 최소 권한 원칙을 따르는 것으로, 원치 않는 검색 동작을 단지 만류하는 데 그치지 않고 불가능하게 만든다.

**해설 신규** 범용 도구를 URL이 문서 형식인지 검증하는 문서 전용 도구로 바꾸면, 인터페이스 단계에서 기능을 제한하므로 근본 원인이 해결된다. 최소 권한 원칙에 따라, 원치 않는 검색 동작을 말리는 데 그치지 않고 아예 할 수 없게 만든다.

## CCAR-F-paullarionov-0011

**EN** While researching a broad topic, you observe that the web-search agent and the document analysis agent investigate the same subtopics, leading to substantial duplication in their outputs. Token usage nearly doubles without a proportional increase in research breadth or depth. What is the most effective way to address this?

What is the most effective way to address this?

**기존** 넓은 주제를 조사하는 동안, 웹 검색 agent와 문서 분석 agent가 같은 하위 주제를 조사하여 출력에 상당한 중복이 생기는 것을 관찰한다. 조사의 폭이나 깊이는 그만큼 늘지 않은 채 토큰 사용량이 거의 두 배가 된다. 이를 해결하는 가장 효과적인 방법은 무엇인가?

이를 해결하는 가장 효과적인 방법은 무엇인가?

**신규** 넓은 주제를 조사하는데, web-search agent와 document analysis agent가 같은 하위 주제를 조사하느라 결과가 상당히 겹친다. token 사용량은 거의 두 배로 늘었는데 조사의 폭이나 깊이는 그만큼 늘지 않았다. 이 문제를 해결하는 가장 효과적인 방법은 무엇인가?

- A. 기존: 두 agent가 병렬로 끝나게 한 다음, coordinator가 겹치는 결과를 중복 제거하여 synthesis agent에게 넘긴다.
  - 신규: 두 agent가 병렬로 끝까지 실행되게 둔 다음, coordinator가 겹치는 결과를 중복 제거해서 synthesis agent에게 넘긴다.
- B. 기존: coordinator가 위임하기 전에 연구 공간을 명시적으로 분할하여 각 agent에 서로 다른 하위 주제나 출처 유형을 할당한다.
  - 신규: coordinator가 작업을 맡기기 전에 조사 영역을 명시적으로 나누고, 각 agent에게 서로 다른 하위 주제나 출처 유형을 배정한다.
- C. 기존: agent가 현재 집중하는 영역을 기록하여 다른 agent가 실행 중에 동적으로 중복을 피할 수 있게 하는 공유 상태 메커니즘을 구현한다.
  - 신규: agent들이 현재 집중하는 영역을 기록하는 공유 상태 메커니즘을 구현해서, 다른 agent가 실행 중에 중복을 동적으로 피하게 한다.
- D. 기존: 웹 검색 결과를 컨텍스트로 사용해 중복을 피하도록, 문서 분석이 웹 검색이 끝난 뒤에만 실행되는 순차 실행으로 전환한다.
  - 신규: 순차 실행으로 바꿔서 web search가 끝난 뒤에 document analysis를 돌리고, web-search 결과를 context로 삼아 중복을 피하게 한다.

**해설 EN** Having the coordinator explicitly partition the research space before delegating is most effective because it addresses the root cause—unclear task boundaries—before any work begins. It preserves parallelism while preventing duplicated effort and wasted tokens.

**해설 기존** coordinator가 위임하기 전에 연구 공간을 명시적으로 분할하는 것이 가장 효과적인 이유는, 작업이 시작되기 전에 근본 원인인 불분명한 작업 경계를 해결하기 때문이다. 병렬성을 유지하면서 중복된 노력과 낭비되는 토큰을 방지한다.

**해설 신규** 작업을 맡기기 전에 coordinator가 조사 영역을 명시적으로 나누는 것이 가장 효과적이다. 작업 경계가 불분명하다는 근본 원인을 일이 시작되기 전에 해결하기 때문이다. 병렬 실행의 이점을 지키면서 중복 작업과 token 낭비도 막는다.

## CCAR-F-paullarionov-0012

**EN** During research, the web-search subagent queries three source categories with different outcomes: academic databases return 15 relevant papers, industry reports return “0 results,” and patent databases return “Connection timeout.” When designing error propagation to the coordinator, which approach enables the best recovery decisions?

Which approach enables the best recovery decisions?

**기존** 조사 중에 웹 검색 subagent가 서로 다른 결과를 내는 세 가지 출처 범주를 쿼리한다. 학술 데이터베이스는 관련 논문 15편을 반환하고, 업계 보고서는 “0 results”를 반환하며, 특허 데이터베이스는 “Connection timeout”을 반환한다. coordinator로의 오류 전파를 설계할 때, 어떤 접근이 최선의 복구 결정을 가능하게 하는가?

어떤 접근이 최선의 복구 결정을 가능하게 하는가?

**신규** 조사 중에 web-search subagent가 세 가지 출처 범주를 검색했는데 결과가 제각각이었다. 학술 데이터베이스에서는 관련 논문 15편이 나왔고, 업계 보고서에서는 "0 results"가 나왔으며, 특허 데이터베이스에서는 "Connection timeout"이 나왔다. coordinator에게 보낼 error propagation을 설계할 때, 가장 좋은 복구 결정을 가능하게 하는 방식은 무엇인가?

- A. 기존: 결과를 하나의 성공률 지표(예: “출처 커버리지 67%”)로 집계하고, 상세 로그는 요청 시 확인할 수 있게 한다.
  - 신규: 결과를 "출처 커버리지 67%" 같은 하나의 성공률 지표로 합치고, 자세한 로그는 필요할 때 볼 수 있게 한다.
- B. 기존: “timeout”과 “0 results”를 모두 coordinator의 개입이 필요한 실패로 보고한다.
  - 신규: "timeout"과 "0 results"를 모두 coordinator가 개입해야 하는 실패로 보고한다.
- C. 기존: 일시적인 실패는 내부에서 재시도하고 지속적인 오류만 보고한다.
  - 신규: 일시적인 실패는 내부에서 다시 시도하고, 계속되는 error만 보고한다.
- D. 기존: 재시도 결정이 필요한 접근 실패(timeout)와, 성공한 쿼리를 나타내는 유효한 빈 결과(“0 results”)를 구분한다.
  - 신규: 다시 시도할지 결정해야 하는 접근 실패(timeout)와, 쿼리는 성공했고 결과만 비어 있는 유효한 빈 결과("0 results")를 구별한다.

**해설 EN** A timeout (access failure) and “0 results” (valid empty result) are semantically different outcomes requiring different responses. Distinguishing them allows the coordinator to retry the patent database while accepting the industry reports “0 results” as a valid, informative finding.

**해설 기존** timeout(접근 실패)과 “0 results”(유효한 빈 결과)는 의미가 서로 다른 결과로, 서로 다른 대응이 필요하다. 이를 구분하면 coordinator는 특허 데이터베이스는 재시도하면서 업계 보고서의 “0 results”는 유효하고 의미 있는 발견으로 받아들일 수 있다.

**해설 신규** timeout(접근 실패)과 "0 results"(유효한 빈 결과)는 의미가 다른 결과여서 대응도 달라야 한다. 둘을 구별하면 coordinator는 특허 데이터베이스는 다시 시도하고, 업계 보고서의 "0 results"는 정보가 되는 유효한 발견으로 받아들일 수 있다.

## CCAR-F-paullarionov-0013

**EN** Production monitoring shows inconsistent synthesis quality. When aggregated results are ~75K tokens, the synthesis agent reliably cites information from the first 15K tokens (web-search headlines/snippets) and the last 10K tokens (document analysis conclusions), but often misses critical findings in the middle 50K tokens—even when they directly answer the research question. How should you restructure the aggregated input?

How should you restructure the aggregated input?

**기존** Production 모니터링에서 synthesis 품질이 일관되지 않게 나타난다. 집계된 결과가 약 75K 토큰일 때, synthesis agent는 처음 15K 토큰(웹 검색 헤드라인/스니펫)과 마지막 10K 토큰(문서 분석 결론)의 정보는 안정적으로 인용하지만, 중간 50K 토큰에 있는 핵심 발견 사항은 연구 질문에 직접 답하는 내용인데도 자주 놓친다. 집계된 입력을 어떻게 재구성해야 하는가?

집계된 입력을 어떻게 재구성해야 하는가?

**신규** 운영 모니터링에서 synthesis 품질이 들쭉날쭉하다. 취합한 결과가 약 75K token일 때, synthesis agent는 앞쪽 15K token(web-search 헤드라인과 스니펫)과 뒤쪽 10K token(document analysis 결론)의 정보는 꾸준히 인용한다. 하지만 가운데 50K token에 있는 핵심 발견은, 연구 질문에 직접 답하는 내용이어도 자주 놓친다. 취합한 입력을 어떻게 재구성해야 하는가?

- A. 기존: 모델이 안정적으로 처리하는 범위 안에 콘텐츠가 들어오도록, 집계 전에 모든 subagent 출력을 20K 토큰 미만으로 요약한다.
  - 신규: 모델이 안정적으로 처리하는 범위 안에 들어오도록, 취합하기 전에 모든 subagent의 출력을 20K token 미만으로 요약한다.
- B. 기존: subagent 결과를 synthesis agent에 점진적으로 스트리밍하여, 웹 검색 결과를 먼저 끝까지 처리한 다음 문서 분석 결과를 추가한다.
  - 신규: subagent 결과를 synthesis agent에게 점진적으로 스트리밍해서, web-search 결과를 먼저 끝까지 처리한 뒤에 document analysis 결과를 더한다.
- C. 기존: 집계된 입력의 시작 부분에 핵심 발견 사항 요약을 배치하고, 상세 결과는 탐색하기 쉽도록 명시적인 섹션 제목으로 구성한다.
  - 신규: 취합한 입력의 맨 앞에 핵심 발견 요약을 두고, 자세한 결과는 명확한 섹션 제목을 붙여 정리해서 찾아보기 쉽게 한다.
- D. 기존: 연구 작업마다 어떤 subagent의 결과가 먼저 오는지를 번갈아 바꾸는 로테이션을 구현하여, 시간이 지나면 두 소스가 동등하게 맨 앞 위치를 차지하도록 한다.
  - 신규: 연구 작업마다 어느 subagent의 결과를 먼저 보여줄지 번갈아 바꾸는 순환 방식을 구현해서, 시간이 지나면 두 출처가 똑같이 앞자리를 차지하게 한다.

**해설 EN** Putting a key-findings summary at the start leverages primacy effects so critical information sits in the most reliably processed position. Adding explicit section headings throughout helps the model navigate and attend to mid-input content, directly mitigating the “lost in the middle” phenomenon.

**해설 기존** 핵심 발견 사항 요약을 시작 부분에 두면 primacy effect를 활용하여 중요한 정보가 가장 안정적으로 처리되는 위치에 놓인다. 입력 전반에 명시적인 섹션 제목을 추가하면 모델이 입력 중간 부분의 내용을 탐색하고 주목하는 데 도움이 되어, “lost in the middle” 현상을 직접적으로 완화한다.

**해설 신규** 핵심 발견 요약을 맨 앞에 두면 primacy effect를 활용해, 중요한 정보가 모델이 가장 안정적으로 처리하는 위치에 놓인다. 입력 전체에 명확한 섹션 제목을 붙이면 모델이 입력 중간 내용도 찾아가 주의를 기울이기 쉬워져서 "lost in the middle" 현상을 직접 완화한다.

## CCAR-F-paullarionov-0014

**EN** In testing, the combined output of the web-search agent (85K tokens including page content) and the document analysis agent (70K tokens including chains of thought) totals 155K tokens, but the synthesis agent performs best with inputs under 50K tokens. Which solution is most effective?

Which solution is most effective?

**기존** 테스트 결과, 웹 검색 agent의 출력(페이지 콘텐츠 포함 85K 토큰)과 문서 분석 agent의 출력(chain of thought 포함 70K 토큰)을 합하면 155K 토큰이지만, synthesis agent는 입력이 50K 토큰 미만일 때 가장 좋은 성능을 보인다. 어떤 해결책이 가장 효과적인가?

어떤 해결책이 가장 효과적인가?

**신규** 테스트해 보니 web-search agent의 출력(페이지 내용 포함 85K token)과 document analysis agent의 출력(chain of thought 포함 70K token)을 합치면 155K token이다. 그런데 synthesis agent는 입력이 50K token 미만일 때 성능이 가장 좋다. 가장 효과적인 해결책은 무엇인가?

- A. 기존: 상위 agent를 수정하여 장황한 콘텐츠와 추론 대신 구조화된 데이터(핵심 사실, 인용문, 관련성 점수)를 반환하게 한다.
  - 신규: upstream agent가 장황한 내용과 추론 대신 구조화된 데이터(핵심 사실, 인용문, 관련성 점수)를 반환하도록 수정한다.
- B. 기존: synthesis로 전달하기 전에 발견 사항을 압축하는 중간 요약 agent를 추가한다.
  - 신규: 발견한 내용을 synthesis에 넘기기 전에 압축하는 중간 요약 agent를 추가한다.
- C. 기존: synthesis agent가 호출 간에 상태를 유지하면서 발견 사항을 순차적인 배치로 처리하게 한다.
  - 신규: synthesis agent가 발견한 내용을 여러 묶음으로 순차 처리하게 하고, 호출 사이에 상태를 유지한다.
- D. 기존: 발견 사항을 vector database에 저장하고, synthesis agent가 작업 중 조회할 수 있도록 검색 도구를 제공한다.
  - 신규: 발견한 내용을 vector database에 저장하고, synthesis agent가 작업 중에 질의할 수 있도록 검색 도구를 준다.

**해설 EN** Modifying upstream agents to return structured data fixes the root cause by reducing token volume at the source while preserving essential information. It avoids passing bulky page content and reasoning traces that inflate tokens without improving the synthesis step.

**해설 기존** 상위 agent가 구조화된 데이터를 반환하도록 수정하면 필수 정보는 보존하면서 소스 단계에서 토큰 양을 줄여 근본 원인을 해결한다. 이는 synthesis 단계를 개선하지 못하면서 토큰만 부풀리는 부피 큰 페이지 콘텐츠와 추론 흔적을 전달하지 않게 해 준다.

**해설 신규** upstream agent가 구조화된 데이터를 반환하도록 고치면, 필수 정보는 지키면서 token 양을 출처에서부터 줄이므로 근본 원인이 해결된다. 부피만 큰 페이지 내용과 추론 기록은 token만 늘릴 뿐 synthesis 단계에는 도움이 되지 않는데, 이런 것을 넘기지 않게 된다.

## CCAR-F-paullarionov-0015

**EN** In testing, you observe that the synthesis agent often needs to verify specific claims while merging results. Currently, when verification is needed, the synthesis agent returns control to the coordinator, which calls the web-search agent and then re-invokes synthesis with the results. This adds 2–3 extra loops per task and increases latency by 40%. Your assessment shows 85% of these verifications are simple fact checks (dates, names, stats) and 15% require deeper research. Which approach most effectively reduces overhead while preserving system reliability?

Which approach is most effective?

**기존** 테스트 중, synthesis agent가 결과를 병합하는 동안 특정 주장을 검증해야 하는 경우가 많다는 것을 관찰한다. 현재는 검증이 필요하면 synthesis agent가 coordinator에게 제어권을 반환하고, coordinator가 웹 검색 agent를 호출한 뒤 그 결과와 함께 synthesis를 다시 호출한다. 이로 인해 작업당 2~3회의 추가 루프가 발생하고 지연 시간이 40% 증가한다. 평가 결과 이러한 검증의 85%는 단순한 사실 확인(날짜, 이름, 통계)이고 15%는 더 깊은 조사가 필요하다. 시스템 신뢰성을 유지하면서 오버헤드를 가장 효과적으로 줄이는 접근 방식은 무엇인가?

어떤 접근 방식이 가장 효과적인가?

**신규** 테스트해 보니 synthesis agent는 결과를 합치는 도중에 특정 주장을 검증해야 할 때가 많다. 지금은 검증이 필요하면 synthesis agent가 coordinator에게 제어권을 돌려주고, coordinator가 web-search agent를 호출한 뒤 그 결과를 가지고 synthesis를 다시 호출한다. 이 때문에 작업마다 loop가 2~3번 더 돌고 지연 시간이 40% 늘었다. 분석해 보니 이런 검증의 85%는 날짜, 이름, 통계 같은 단순한 사실 확인이고, 15%는 더 깊은 조사가 필요하다. 시스템의 신뢰성을 지키면서 오버헤드를 가장 효과적으로 줄이는 방법은 무엇인가?

- A. 기존: synthesis agent가 coordinator 루프 없이 모든 검증 요구를 직접 처리할 수 있도록 모든 웹 검색 도구에 대한 접근 권한을 부여한다.
  - 신규: synthesis agent에게 web-search 도구 전체를 줘서, coordinator loop 없이 어떤 검증이든 직접 처리하게 한다.
- B. 기존: synthesis agent가 모든 검증 요구를 모아 두었다가 마지막에 배치로 coordinator에 반환하고, coordinator가 이를 한 번에 웹 검색 agent로 보내게 한다.
  - 신규: synthesis agent가 검증이 필요한 항목을 모아 두었다가 마지막에 coordinator에게 한꺼번에 반환하고, coordinator가 이를 web-search agent에게 한 번에 보낸다.
- C. 기존: synthesis에서 검증이 필요할 것에 대비하여, 웹 검색 agent가 초기 조사 중에 각 소스 주변의 추가 컨텍스트를 선제적으로 캐시하게 한다.
  - 신규: synthesis에서 검증이 필요할 것에 대비해, web-search agent가 첫 조사 때 각 출처 주변의 추가 context를 미리 cache해 둔다.
- D. 기존: synthesis agent에 단순 확인용으로 범위가 제한된 `verify_fact` 도구를 제공하고, 복잡한 검증은 coordinator를 통해 웹 검색 agent로 라우팅한다.
  - 신규: synthesis agent에게 단순한 확인용으로 범위가 제한된 `verify_fact` 도구를 주고, 복잡한 검증은 계속 coordinator를 거쳐 web-search agent가 맡게 한다.

**해설 EN** A limited-scope fact-verification tool lets the synthesis agent handle 85% of simple checks directly, eliminating most loops, while preserving the coordinator delegation path for the 15% of complex verifications. This applies least privilege while significantly reducing latency.

**해설 기존** 범위가 제한된 사실 검증 도구를 사용하면 synthesis agent가 단순 확인의 85%를 직접 처리하여 대부분의 루프를 없앨 수 있고, 복잡한 검증 15%에 대해서는 coordinator 위임 경로를 그대로 유지한다. 이는 최소 권한 원칙을 적용하면서 지연 시간을 크게 줄인다.

**해설 신규** 범위가 제한된 사실 검증 도구를 쓰면 synthesis agent가 단순 확인 85%를 직접 처리해 loop 대부분을 없앨 수 있다. 복잡한 검증 15%는 그대로 coordinator에게 위임하는 경로를 유지한다. 최소 권한 원칙을 지키면서 지연 시간도 크게 줄인다.

## CCAR-F-paullarionov-0016

**EN** Your CI pipeline runs the Claude Code CLI (in `--print` mode) using CLAUDE.md to provide project context for code review, and developers generally find the reviews substantive. However, they report that integrating findings into the workflow is difficult—Claude outputs narrative paragraphs that must be manually copied into PR comments. The team wants to automatically post each finding as a separate inline PR comment at the relevant place in code, which requires structured data with file path, line number, severity level, and suggested fix. Which approach is most effective?

Which approach is most effective?

**기존** CI 파이프라인이 프로젝트 컨텍스트를 제공하는 CLAUDE.md를 사용하여 코드 리뷰를 위해 Claude Code CLI(`--print` 모드)를 실행하며, 개발자들은 대체로 리뷰가 충실하다고 평가한다. 그러나 Claude가 서술형 문단을 출력하여 PR 코멘트로 수동 복사해야 하므로 발견 사항을 워크플로에 통합하기 어렵다고 보고한다. 팀은 각 발견 사항을 코드의 해당 위치에 별도의 인라인 PR 코멘트로 자동 게시하려 하며, 이를 위해서는 파일 경로, 줄 번호, 심각도, 제안된 수정 사항이 담긴 구조화된 데이터가 필요하다. 어떤 접근 방식이 가장 효과적인가?

어떤 접근 방식이 가장 효과적인가?

**신규** CI pipeline에서 Claude Code CLI(`--print` 모드)를 실행하고, CLAUDE.md로 프로젝트 context를 줘서 코드 리뷰를 한다. 개발자들은 리뷰 내용이 대체로 쓸 만하다고 본다. 하지만 결과를 작업 흐름에 연결하기 어렵다고 한다. Claude가 서술형 문단으로 출력해서 PR 코멘트에 일일이 복사해 붙여야 하기 때문이다. 팀은 발견 사항마다 코드의 해당 위치에 inline PR 코멘트를 자동으로 달고 싶다. 그러려면 파일 경로, 줄 번호, 심각도, 수정 제안이 담긴 구조화된 데이터가 필요하다. 가장 효과적인 방법은 무엇인가?

- A. 기존: CLAUDE.md에 구조화된 발견 사항 예시가 포함된 “Output Format for Review” 섹션을 추가하여, Claude가 프로젝트 컨텍스트로부터 기대되는 형식을 학습하게 한다.
  - 신규: CLAUDE.md에 "Output Format for Review" 섹션을 추가하고 구조화된 발견 사항의 예시를 넣어서, Claude가 프로젝트 context에서 원하는 형식을 익히게 한다.
- B. 기존: CLI 플래그 `--output-format json`과 `--json-schema`를 사용하여 구조화된 발견 사항을 강제한 뒤, 출력을 파싱하여 GitHub API로 인라인 코멘트를 게시한다.
  - 신규: CLI 플래그 `--output-format json`과 `--json-schema`로 구조화된 발견 사항을 강제하고, 출력을 파싱해 GitHub API로 inline 코멘트를 단다.
- C. 기존: 리뷰 프롬프트에 각 발견 사항이 `[FILE:path] [LINE:n] [SEVERITY:level] ...` 같은 파싱 가능한 템플릿을 따르도록 요구하는 명시적 형식 지침을 포함한다.
  - 신규: 리뷰 prompt에 명시적인 형식 지시를 넣어서, 발견 사항마다 `[FILE:path] [LINE:n] [SEVERITY:level] ...` 같은 파싱 가능한 템플릿을 따르게 한다.
- D. 기존: 서술형 리뷰 형식은 유지하되, Claude를 사용하여 발견 사항의 구조화된 JSON 요약을 생성하는 요약 단계를 추가한다.
  - 신규: 서술형 리뷰 형식은 그대로 두고, Claude가 발견 사항을 구조화된 JSON으로 요약하는 단계를 추가한다.

**해설 EN** Using `--output-format json` with `--json-schema` enforces structured output at the CLI level, guaranteeing well-formed JSON with the required fields (file path, line number, severity, suggested fix) that can be reliably parsed and posted as inline PR comments via the GitHub API. It leverages built-in CLI capabilities designed specifically for structured output.

**해설 기존** `--output-format json`과 `--json-schema`를 함께 사용하면 CLI 수준에서 구조화된 출력이 강제되어, 필수 필드(파일 경로, 줄 번호, 심각도, 제안된 수정 사항)를 갖춘 올바른 형식의 JSON이 보장되며, 이를 안정적으로 파싱하여 GitHub API로 인라인 PR 코멘트로 게시할 수 있다. 이는 구조화된 출력을 위해 특별히 설계된 CLI 내장 기능을 활용하는 방식이다.

**해설 신규** `--output-format json`을 `--json-schema`와 함께 쓰면 CLI 수준에서 구조화된 출력을 강제한다. 필요한 필드(파일 경로, 줄 번호, 심각도, 수정 제안)가 갖춰진 올바른 JSON이 보장되므로, 안정적으로 파싱해 GitHub API로 inline PR 코멘트를 달 수 있다. 구조화된 출력을 위해 CLI에 내장된 기능을 그대로 활용하는 방법이다.

## CCAR-F-paullarionov-0017

**EN** Your team uses Claude Code for generating code suggestions, but you notice a pattern: non-obvious issues—performance optimizations that break edge cases, cleanups that unexpectedly change behavior—are only caught when another team member reviews the PR. Claude’s reasoning during generation shows it considered these cases but concluded its approach was correct. Which approach directly addresses the root cause of this self-check limitation?

Which approach directly addresses the root cause?

**기존** 팀은 코드 제안 생성에 Claude Code를 사용하는데, 하나의 패턴을 발견한다. 엣지 케이스를 깨뜨리는 성능 최적화나 동작을 예기치 않게 바꾸는 정리 작업 같은 눈에 띄지 않는 문제는 다른 팀원이 PR을 리뷰할 때에만 발견된다. 생성 중 Claude의 추론을 보면 이러한 경우를 고려했지만 자신의 접근 방식이 옳다고 결론 내렸음을 알 수 있다. 이러한 self-check 한계의 근본 원인을 직접적으로 해결하는 접근 방식은 무엇인가?

어떤 접근 방식이 근본 원인을 직접적으로 해결하는가?

**신규** 팀은 Claude Code로 코드 제안을 생성하는데, 한 가지 패턴이 보인다. 성능 최적화가 edge case를 깨뜨리거나, 정리했을 뿐인데 동작이 예상치 못하게 바뀌는 것처럼 눈에 잘 띄지 않는 문제는 다른 팀원이 PR을 리뷰할 때에야 발견된다. 생성 중 Claude의 추론을 보면 이런 경우를 고려했지만 자기 방식이 맞다고 결론을 내렸다. 이렇게 스스로 점검하는 방식에 한계가 생기는 근본 원인을 직접 해결하는 방법은 무엇인가?

- A. 기존: 생성자의 추론에 접근할 수 없는 두 번째 독립적인 Claude Code 인스턴스를 실행하여 변경 사항을 리뷰하게 한다.
  - 신규: Claude Code의 두 번째 독립 instance를 실행해, 생성한 쪽의 추론은 보지 못한 채 변경 사항을 리뷰하게 한다.
- B. 기존: 제안을 만들기 전에 더 철저히 숙고할 수 있도록 생성 단계에서 extended thinking 모드를 활성화한다.
  - 신규: 생성 단계에서 extended thinking 모드를 켜서, 제안을 내기 전에 더 충분히 숙고하게 한다.
- C. 기존: 최종 출력을 확정하기 전에 Claude가 자신의 제안을 비판하도록 요청하는 명시적인 self-review 지침을 생성 프롬프트에 추가한다.
  - 신규: 생성 prompt에 자기 검토 지시를 명시해서, 출력을 확정하기 전에 Claude가 자기 제안을 비판하게 한다.
- D. 기존: 생성 중에 Claude가 기대되는 동작을 더 잘 이해하도록 전체 테스트 파일과 문서를 프롬프트 컨텍스트에 포함한다.
  - 신규: 테스트 파일과 문서 전체를 prompt context에 넣어서, 생성하는 동안 Claude가 기대 동작을 더 잘 이해하게 한다.

**해설 EN** A second independent Claude Code instance without access to the generator’s reasoning directly addresses the root cause by avoiding confirmation bias. This “fresh eyes” perspective mirrors human peer review, where another reviewer catches issues the author rationalized.

**해설 기존** 생성자의 추론에 접근할 수 없는 두 번째 독립적인 Claude Code 인스턴스는 확증 편향을 피함으로써 근본 원인을 직접적으로 해결한다. 이러한 “fresh eyes” 관점은 작성자가 합리화하고 넘어간 문제를 다른 리뷰어가 잡아내는 사람의 동료 리뷰와 같은 방식이다.

**해설 신규** 생성한 쪽의 추론을 보지 못하는 두 번째 독립 Claude Code instance는 확증 편향을 피하므로 근본 원인을 직접 해결한다. 이런 "새로운 눈"은 사람의 동료 리뷰와 같다. 작성자가 합리화하고 넘어간 문제를 다른 리뷰어는 잡아낸다.

## CCAR-F-paullarionov-0018

**EN** Your code review component is iterative: Claude analyzes the changed file, then may request related files (imports, base classes, tests) via tool calls to understand context before providing final feedback. Your application defines a tool that lets Claude request file contents; Claude calls the tool, gets results, and continues analysis. You’re evaluating batch processing to reduce API cost. What is the primary technical limitation when considering batch processing for this workflow?

What is the primary technical limitation?

**기존** 코드 리뷰 컴포넌트는 반복적으로 동작한다. Claude가 변경된 파일을 분석한 뒤, 최종 피드백을 제공하기 전에 컨텍스트를 이해하기 위해 도구 호출로 관련 파일(import, 기반 클래스, 테스트)을 요청할 수 있다. 애플리케이션은 Claude가 파일 내용을 요청할 수 있는 도구를 정의하며, Claude는 도구를 호출하고 결과를 받아 분석을 이어 간다. API 비용을 줄이기 위해 batch processing을 검토하고 있다. 이 워크플로에 batch processing을 고려할 때 주된 기술적 한계는 무엇인가?

주된 기술적 한계는 무엇인가?

**신규** 코드 리뷰 컴포넌트는 반복적으로 동작한다. Claude가 변경된 파일을 분석하고, 최종 피드백을 내기 전에 context를 파악하려고 tool call로 관련 파일(import, 기반 클래스, 테스트)을 요청하기도 한다. 애플리케이션은 Claude가 파일 내용을 요청할 수 있는 도구를 정의해 두었고, Claude는 그 도구를 호출해 결과를 받고 분석을 이어간다. API 비용을 줄이려고 batch 처리를 검토하는 중이다. 이 workflow에 batch 처리를 적용할 때 가장 큰 기술적 제약은 무엇인가?

- A. 기존: batch processing에는 출력을 입력 요청에 다시 매핑하는 correlation ID가 포함되지 않는다.
  - 신규: batch 처리에는 출력을 입력 요청과 연결해 주는 correlation ID가 없다.
- B. 기존: 비동기 모델은 요청 도중에 도구를 실행하고 Claude가 분석을 이어 갈 수 있도록 결과를 반환할 수 없다.
  - 신규: 비동기 모델에서는 요청 도중에 도구를 실행하고 그 결과를 돌려줘서 Claude가 분석을 이어가게 할 수 없다.
- C. 기존: Batch API는 요청 파라미터의 도구 정의를 지원하지 않는다.
  - 신규: Batch API는 요청 파라미터에 도구 정의를 넣는 것을 지원하지 않는다.
- D. 기존: 최대 24시간에 이르는 batch processing 지연 시간은 pull request 피드백에 너무 느리지만, 그 외에는 워크플로가 동작할 것이다.
  - 신규: batch 처리는 최대 24시간까지 걸려서 pull request 피드백에는 너무 느리다. 다만 workflow 자체는 동작한다.

**해설 EN** A “fire-and-forget” asynchronous Batch API model has no mechanism to intercept a tool call during a request, execute the tool, and return results for Claude to continue analysis. This is fundamentally incompatible with iterative tool-calling workflows that require multiple tool request/response rounds within a single logical interaction.

**해설 기존** “fire-and-forget” 방식의 비동기 Batch API 모델에는 요청 도중 도구 호출을 가로채 도구를 실행하고 Claude가 분석을 이어 가도록 결과를 반환하는 메커니즘이 없다. 이는 하나의 논리적 상호작용 안에서 여러 차례의 도구 요청/응답 라운드가 필요한 반복적 tool-calling 워크플로와 근본적으로 양립할 수 없다.

**해설 신규** "fire-and-forget" 방식의 비동기 Batch API 모델에는 요청 도중에 tool call을 가로채 도구를 실행하고 결과를 돌려줘서 Claude가 분석을 이어가게 하는 장치가 없다. 하나의 논리적 상호작용 안에서 도구 요청과 응답이 여러 번 오가야 하는 반복적 tool calling workflow와는 근본적으로 맞지 않는다.

## CCAR-F-paullarionov-0019

**EN** Your CI/CD system runs three Claude-based analyses: (1) fast style checks on every PR that block merging until completion, (2) comprehensive weekly security audits of the entire codebase, and (3) nightly test-case generation for recently changed modules. The Message Batches API offers 50% savings but processing can take up to 24 hours. You want to optimize API cost while maintaining an acceptable developer experience. Which combination correctly matches each task to an API approach?

Which combination is correct?

**기존** CI/CD 시스템은 세 가지 Claude 기반 분석을 실행한다. (1) 모든 PR에서 완료될 때까지 머지를 차단하는 빠른 스타일 검사, (2) 전체 코드베이스에 대한 포괄적인 주간 보안 감사, (3) 최근 변경된 모듈에 대한 야간 테스트 케이스 생성. Message Batches API는 50% 절감을 제공하지만 처리에 최대 24시간이 걸릴 수 있다. 허용 가능한 개발자 경험을 유지하면서 API 비용을 최적화하려 한다. 각 작업을 API 방식에 올바르게 짝짓는 조합은 무엇인가?

어떤 조합이 올바른가?

**신규** CI/CD 시스템에서 Claude 기반 분석 세 가지를 돌린다. (1) 모든 PR에서 실행되며 끝날 때까지 merge를 막는 빠른 스타일 검사, (2) 코드베이스 전체에 대한 주간 종합 보안 감사, (3) 최근 변경된 모듈에 대한 야간 테스트 케이스 생성. Message Batches API는 50%를 절감해 주지만 처리에 최대 24시간이 걸릴 수 있다. 개발자 경험은 받아들일 만한 수준으로 유지하면서 API 비용을 최적화하려 한다. 각 작업에 API 방식을 올바르게 짝지은 조합은 무엇인가?

- A. 기존: 50% 절감을 극대화하기 위해 세 작업 모두에 Message Batches API를 사용하고, batch 완료를 polling하도록 파이프라인을 구성한다.
  - 신규: 50% 절감을 최대한 누리도록 세 작업 모두 Message Batches API를 쓰고, pipeline이 batch 완료를 polling하게 설정한다.
- B. 기존: PR 스타일 검사에는 동기 호출을 사용하고, 주간 보안 감사와 야간 테스트 생성에는 Message Batches API를 사용한다.
  - 신규: PR 스타일 검사에는 동기 호출을 쓰고, 주간 보안 감사와 야간 테스트 생성에는 Message Batches API를 쓴다.
- C. 기존: 일관된 응답 시간을 위해 세 작업 모두에 동기 호출을 사용하고, prompt caching으로 워크로드 전반의 비용을 줄인다.
  - 신규: 응답 시간을 일정하게 하려고 세 작업 모두 동기 호출을 쓰고, 비용은 prompt caching으로 줄인다.
- D. 기존: PR 스타일 검사와 야간 테스트 생성에는 동기 호출을 사용하고, 주간 보안 감사에만 Message Batches API를 사용한다.
  - 신규: PR 스타일 검사와 야간 테스트 생성에는 동기 호출을 쓰고, 주간 보안 감사에만 Message Batches API를 쓴다.

**해설 EN** PR style checks block developers and require immediate responses via synchronous calls, while weekly security audits and nightly test generation are scheduled tasks with flexible deadlines that can tolerate up to a 24-hour batch window—capturing 50% savings for both.

**해설 기존** PR 스타일 검사는 개발자를 차단하므로 동기 호출을 통한 즉각적인 응답이 필요하다. 반면 주간 보안 감사와 야간 테스트 생성은 마감이 유연한 예약 작업이라 최대 24시간의 batch 처리 시간을 감수할 수 있으므로, 둘 다 50% 절감을 얻을 수 있다.

**해설 신규** PR 스타일 검사는 개발자를 기다리게 하므로 동기 호출로 즉시 응답을 받아야 한다. 반면 주간 보안 감사와 야간 테스트 생성은 일정에 맞춰 도는 작업이고 마감에 여유가 있어서 최대 24시간의 batch 처리 시간을 감수할 수 있다. 그래서 두 작업 모두 50% 절감을 얻는다.

## CCAR-F-paullarionov-0020

**EN** Your automated reviews find real issues, but developers report the feedback is not actionable. Findings include phrases like “complex ticket routing logic” or “potential null pointer” without specifying what exactly to change. When you add detailed instructions like “always include concrete fix suggestions,” the model still produces inconsistent output—sometimes detailed, sometimes vague. Which prompting technique most reliably produces consistently actionable feedback?

Which prompting technique is most reliable?

**기존** 자동화된 리뷰가 실제 문제를 찾아내지만, 개발자들은 피드백이 실행 가능하지 않다고 보고한다. 발견 사항에는 구체적으로 무엇을 바꿔야 하는지 명시하지 않은 채 “complex ticket routing logic”이나 “potential null pointer” 같은 표현이 들어 있다. “always include concrete fix suggestions”와 같은 상세한 지침을 추가해도 모델의 출력은 여전히 일관되지 않아, 때로는 상세하고 때로는 모호하다. 어떤 프롬프팅 기법이 일관되게 실행 가능한 피드백을 가장 안정적으로 만들어 내는가?

어떤 프롬프팅 기법이 가장 안정적인가?

**신규** 자동 리뷰가 실제 문제는 찾아내지만, 개발자들은 피드백이 바로 실행하기 어렵다고 한다. "복잡한 ticket routing 로직"이나 "잠재적 null pointer" 같은 표현만 있고 정확히 무엇을 바꿔야 하는지는 없다. "항상 구체적인 수정 제안을 포함하라" 같은 상세한 지시를 추가해도 모델 출력은 여전히 들쭉날쭉해서, 어떤 때는 자세하고 어떤 때는 모호하다. 일관되게 바로 실행할 수 있는 피드백을 가장 안정적으로 얻는 prompting 기법은 무엇인가?

- A. 기존: 피드백 형식의 각 부분(위치, 문제, 심각도, 제안된 수정)에 대해 더 명시적인 요구 사항으로 지침을 한층 더 다듬는다.
  - 신규: 피드백 형식의 각 부분(위치, 문제, 심각도, 수정 제안)에 대한 요구 사항을 지시문에 더 명시해서 다듬는다.
- B. 기존: 모델이 구체적인 수정 방안을 제안할 충분한 정보를 갖도록 주변 코드베이스를 더 많이 포함하여 context window를 확장한다.
  - 신규: context window를 늘려 주변 코드베이스를 더 많이 포함시켜서, 모델이 구체적인 수정안을 낼 정보를 충분히 갖게 한다.
- C. 기존: 한 프롬프트가 문제를 식별하고 두 번째 프롬프트가 수정을 생성하는 2단계 접근 방식을 구현하여 전문화를 가능하게 한다.
  - 신규: 한 prompt는 문제를 찾고 다른 prompt는 수정안을 만드는 두 단계 방식을 구현해서 역할을 나눈다.
- D. 기존: 식별된 문제, 코드 내 위치, 구체적인 수정 제안이라는 정확한 필수 형식을 보여 주는 3~4개의 few-shot 예시를 추가한다.
  - 신규: 필요한 형식(발견한 문제, 코드 내 위치, 구체적인 수정 제안)을 그대로 보여 주는 few-shot 예시를 3~4개 추가한다.

**해설 EN** Few-shot examples are the most effective technique for achieving consistent output format when instructions alone produce variable results. Providing 3–4 examples that show the exact desired structure (issue, location, concrete fix) gives the model a concrete pattern to follow, which is more reliable than abstract instructions.

**해설 기존** 지침만으로는 결과가 들쭉날쭉할 때 일관된 출력 형식을 얻는 데 가장 효과적인 기법은 few-shot 예시이다. 원하는 정확한 구조(문제, 위치, 구체적인 수정)를 보여 주는 3~4개의 예시는 모델이 따를 구체적인 패턴을 제공하므로 추상적인 지침보다 더 안정적이다.

**해설 신규** 지시문만으로는 결과가 들쭉날쭉할 때 출력 형식을 일관되게 맞추는 데는 few-shot 예시가 가장 효과적이다. 원하는 구조(문제, 위치, 구체적 수정안)를 그대로 보여 주는 예시 3~4개는 모델이 따를 구체적인 패턴이 되므로, 추상적인 지시문보다 안정적이다.

## CCAR-F-paullarionov-0021

**EN** Your CI pipeline includes two Claude-based code review modes: a pre-merge-commit hook that blocks PR merge until completion, and a “deep analysis” that runs overnight, polls for batch completion, and posts detailed suggestions to the PR. You want to reduce API cost using the Message Batches API, which offers 50% savings but requires polling and can take up to 24 hours. Which mode should use batch processing?

Which mode should use batch processing?

**기존** CI 파이프라인에는 두 가지 Claude 기반 코드 리뷰 모드가 있다. 완료될 때까지 PR 머지를 차단하는 pre-merge-commit hook과, 밤새 실행되며 batch 완료를 polling하고 상세한 제안을 PR에 게시하는 “deep analysis”이다. 50% 절감을 제공하지만 polling이 필요하고 최대 24시간이 걸릴 수 있는 Message Batches API로 API 비용을 줄이려 한다. 어떤 모드가 batch processing을 사용해야 하는가?

어떤 모드가 batch processing을 사용해야 하는가?

**신규** CI pipeline에는 Claude 기반 코드 리뷰 모드가 두 가지 있다. 하나는 끝날 때까지 PR merge를 막는 pre-merge-commit hook이고, 다른 하나는 밤새 돌면서 batch 완료를 polling하고 자세한 제안을 PR에 올리는 "deep analysis"다. Message Batches API는 50%를 절감해 주지만 polling이 필요하고 최대 24시간이 걸릴 수 있다. API 비용을 줄이려고 이 API를 쓴다면 어느 모드에 batch 처리를 써야 하는가?

- A. 기존: pre-merge-commit hook만.
  - 신규: pre-merge-commit hook만
- B. 기존: deep analysis만.
  - 신규: deep analysis만
- C. 기존: 두 모드 모두.
  - 신규: 두 모드 모두
- D. 기존: 두 모드 모두 아님.
  - 신규: 어느 쪽도 아님

**해설 EN** Deep analysis is an ideal candidate for batch processing because it already runs overnight, tolerates delay, and uses a polling model before publishing results—matching the asynchronous, polling-based architecture of the Message Batches API while capturing 50% savings.

**해설 기존** Deep analysis는 이미 밤새 실행되고, 지연을 감수할 수 있으며, 결과를 게시하기 전에 polling 모델을 사용하므로 batch processing의 이상적인 후보이다. 이는 Message Batches API의 비동기적이고 polling 기반인 아키텍처와 맞아떨어지면서 50% 절감을 얻을 수 있다.

**해설 신규** deep analysis는 batch 처리에 알맞은 후보다. 이미 밤새 돌아서 지연을 감수할 수 있고, 결과를 올리기 전에 polling하는 방식이라 Message Batches API의 비동기, polling 기반 구조와 맞는다. 게다가 50% 절감도 얻는다.

## CCAR-F-paullarionov-0022

**EN** Your automated review analyzes comments and docstrings. The current prompt instructs Claude to “check that comments are accurate and up to date.” Findings often flag acceptable patterns (TODO markers, simple descriptions) while missing comments describing behavior the code no longer implements. What change addresses the root cause of this inconsistent analysis?

What change addresses the root cause?

**기존** 자동화된 리뷰가 주석과 docstring을 분석한다. 현재 프롬프트는 Claude에게 “check that comments are accurate and up to date”라고 지시한다. 발견 사항은 허용 가능한 패턴(TODO 마커, 단순한 설명)을 자주 지적하는 반면, 코드가 더 이상 구현하지 않는 동작을 설명하는 주석은 놓친다. 이러한 일관되지 않은 분석의 근본 원인을 해결하는 변경은 무엇인가?

어떤 변경이 근본 원인을 해결하는가?

**신규** 자동 리뷰가 주석과 docstring을 분석한다. 지금 prompt는 Claude에게 "주석이 정확하고 최신인지 확인하라"고 지시한다. 그런데 TODO 표시나 단순한 설명처럼 문제없는 패턴은 자주 지적하면서, 코드가 더는 구현하지 않는 동작을 설명하는 주석은 놓친다. 이렇게 분석이 일관되지 않은 근본 원인을 해결하는 변경은 무엇인가?

- A. 기존: Claude가 최근 코드 변경보다 앞서 작성된 주석을 식별할 수 있도록 `git blame` 데이터를 포함한다.
  - 신규: `git blame` 데이터를 포함해서, Claude가 최근 코드 변경보다 오래된 주석을 찾아낼 수 있게 한다.
- B. 기존: 모델이 코드베이스에서 유사한 패턴을 인식하도록 오해를 부르는 주석의 few-shot 예시를 추가한다.
  - 신규: 오해를 부르는 주석의 few-shot 예시를 추가해서, 모델이 코드베이스에서 비슷한 패턴을 알아보게 한다.
- C. 기존: 노이즈를 줄이기 위해 분석 전에 TODO, FIXME 및 설명형 주석 패턴을 필터링한다.
  - 신규: 노이즈를 줄이려고 분석 전에 TODO, FIXME, 설명형 주석 패턴을 걸러낸다.
- D. 기존: 명시적인 기준을 지정한다. 주석이 주장하는 동작이 코드의 실제 동작과 모순될 때에만 해당 주석을 지적한다.
  - 신규: 명확한 기준을 정한다. 주석이 말하는 동작이 코드의 실제 동작과 모순될 때만 지적한다.

**해설 EN** Explicit criteria—flagging comments only when claimed behavior contradicts actual code behavior—directly addresses the root cause by replacing a vague instruction with a precise definition of what constitutes a problem. This reduces false positives on acceptable patterns and misses of truly misleading comments.

**해설 기존** 주석이 주장하는 동작이 실제 코드 동작과 모순될 때에만 지적한다는 명시적 기준은, 모호한 지침을 무엇이 문제인지에 대한 정밀한 정의로 대체함으로써 근본 원인을 직접 해결한다. 이는 허용 가능한 패턴에 대한 false positive와 실제로 오해를 부르는 주석을 놓치는 일을 모두 줄인다.

**해설 신규** 주석이 주장하는 동작이 실제 코드 동작과 모순될 때만 지적한다는 명확한 기준은, 모호한 지시를 무엇이 문제인지에 대한 정확한 정의로 바꾸므로 근본 원인을 직접 해결한다. 문제없는 패턴을 잘못 지적하는 일도, 정말 오해를 부르는 주석을 놓치는 일도 줄어든다.

## CCAR-F-paullarionov-0023

**EN** Your automated code review system shows inconsistent severity ratings—similar issues like null pointer risks are rated “critical” in some PRs but only “medium” in others. Developer surveys show growing distrust—many start dismissing findings without reading because “half are wrong.” High-false-positive categories erode trust in accurate categories. Which approach best restores developer trust while improving the system?

Which approach best restores developer trust?

**기존** 자동화된 코드 리뷰 시스템의 심각도 평가가 일관되지 않다. null pointer 위험 같은 유사한 문제가 어떤 PR에서는 “critical”로, 다른 PR에서는 “medium”으로만 평가된다. 개발자 설문 결과 불신이 커지고 있으며, “절반은 틀렸다”는 이유로 많은 개발자가 읽지도 않고 발견 사항을 무시하기 시작한다. false positive가 많은 카테고리가 정확한 카테고리에 대한 신뢰까지 약화시킨다. 시스템을 개선하면서 개발자의 신뢰를 가장 잘 회복하는 접근 방식은 무엇인가?

어떤 접근 방식이 개발자의 신뢰를 가장 잘 회복하는가?

**신규** 자동 코드 리뷰 시스템의 심각도 평가가 일관되지 않다. null 포인터 위험처럼 비슷한 문제가 어떤 PR에서는 “critical”, 다른 PR에서는 “medium”으로 평가된다. 개발자 설문에서는 불신이 커지고 있다. “절반은 틀린 지적”이라며 내용을 읽지도 않고 넘기는 개발자가 늘고 있다. 오탐이 많은 카테고리 때문에 정확한 카테고리까지 신뢰를 잃고 있는 상황이다. 시스템을 개선하면서 개발자의 신뢰를 되찾는 데 가장 좋은 방법은 무엇인가?

- A. 기존: false positive가 많은 카테고리(스타일, 네이밍, 문서화)를 일시적으로 비활성화하고, 프롬프트를 개선하는 동안 정밀도가 높은 카테고리만 유지한다.
  - 신규: 오탐이 많은 카테고리(style, naming, documentation)를 일시적으로 끄고, 정밀도가 높은 카테고리만 남긴 채 prompt를 개선한다.
- B. 기존: 모든 카테고리를 활성화한 채로 두되, 각 발견 사항에 신뢰도 점수를 표시하여 개발자가 무엇을 조사할지 결정하게 한다.
  - 신규: 모든 카테고리를 켜 두되 각 지적에 신뢰도 점수를 함께 표시해, 개발자가 무엇을 살펴볼지 직접 정하게 한다.
- C. 기존: 모든 카테고리를 활성화한 채로 두고, 향후 몇 주에 걸쳐 각 카테고리의 정확도를 높이도록 few-shot 예시를 추가한다.
  - 신규: 모든 카테고리를 켜 두고, 앞으로 몇 주에 걸쳐 few-shot 예시를 추가해 카테고리별 정확도를 높인다.
- D. 기존: 전체 false positive 비율을 낮추기 위해 모든 카테고리에 일괄적으로 엄격도를 낮추는 조정을 적용한다.
  - 신규: 모든 카테고리의 엄격도를 똑같이 낮춰 전체 오탐률을 떨어뜨린다.

**해설 EN** Temporarily disabling high-false-positive categories immediately stops trust erosion by removing noisy findings that cause developers to dismiss everything, while preserving value from high-precision categories like security and correctness. It also creates space to improve prompts for problematic categories before re-enabling them.

**해설 기존** false positive가 많은 카테고리를 일시적으로 비활성화하면, 개발자가 모든 것을 무시하게 만드는 노이즈 많은 발견 사항을 제거하여 신뢰 약화를 즉시 멈추면서 보안과 정확성 같은 정밀도 높은 카테고리의 가치는 보존한다. 또한 문제가 있는 카테고리를 다시 활성화하기 전에 프롬프트를 개선할 여유를 만들어 준다.

**해설 신규** 오탐이 많은 카테고리를 일시적으로 끄면 개발자가 모든 지적을 무시하게 만드는 노이즈가 사라져, 신뢰가 더 무너지는 것을 바로 막을 수 있다. security나 correctness처럼 정밀도가 높은 카테고리의 가치는 그대로 유지된다. 문제가 있는 카테고리는 그동안 prompt를 개선한 뒤 다시 켜면 된다.

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

## CCAR-F-paullarionov-0025

**EN** After an initial automated review identifies 12 findings, a developer pushes new commits to address issues. Re-running review produces 8 findings, but developers report that 5 duplicate previous comments on code that was already fixed in the new commits. What is the most effective way to eliminate this redundant feedback while maintaining thoroughness?

What is the most effective way to eliminate redundant feedback?

**기존** 최초의 자동화된 리뷰가 12개의 발견 사항을 식별한 후, 개발자가 문제를 해결하기 위해 새 커밋을 푸시한다. 리뷰를 다시 실행하면 8개의 발견 사항이 나오는데, 개발자들은 그중 5개가 새 커밋에서 이미 수정된 코드에 대한 이전 코멘트와 중복된다고 보고한다. 철저함을 유지하면서 이러한 중복 피드백을 없애는 가장 효과적인 방법은 무엇인가?

중복 피드백을 없애는 가장 효과적인 방법은 무엇인가?

**신규** 자동 리뷰가 처음에 12개를 지적했고, 개발자가 이를 반영해 새 commit을 push했다. 리뷰를 다시 돌리니 8개가 나왔는데, 그중 5개는 새 commit에서 이미 고친 코드에 대해 이전과 같은 댓글을 또 단 것이라는 보고가 올라왔다. 리뷰의 철저함은 유지하면서 이런 중복 피드백을 없애는 가장 효과적인 방법은 무엇인가?

- A. 기존: PR이 생성될 때와 머지 직전 최종 상태에서만 리뷰를 실행하고 중간 커밋은 건너뛴다.
  - 신규: PR을 만들 때와 merge 직전 최종 상태에서만 리뷰를 실행하고, 중간 commit은 건너뛴다.
- B. 기존: 코멘트를 게시하기 전에 파일 경로와 문제 설명이 이전 발견 사항과 일치하는 항목을 제거하는 후처리 필터를 추가한다.
  - 신규: 댓글을 달기 전에, 파일 경로와 문제 설명이 이전 지적과 일치하는 항목을 제거하는 후처리 필터를 추가한다.
- C. 기존: 리뷰 범위를 가장 최근 푸시에서 변경된 파일로 제한하고, 이전 커밋의 파일은 제외한다.
  - 신규: 리뷰 범위를 가장 최근 push에서 변경된 파일로 제한하고, 이전 commit의 파일은 제외한다.
- D. 기존: 이전 리뷰 발견 사항을 컨텍스트에 포함하고, Claude에게 새로운 문제나 아직 해결되지 않은 문제만 보고하도록 지시한다.
  - 신규: 이전 리뷰 결과를 context에 포함하고, 새로운 문제나 아직 해결되지 않은 문제만 보고하도록 Claude에게 지시한다.

**해설 EN** Including prior review findings in context lets Claude distinguish new problems from those already addressed in recent commits. This preserves review thoroughness while using Claude’s reasoning to avoid redundant feedback on fixed code.

**해설 기존** 이전 리뷰 발견 사항을 컨텍스트에 포함하면 Claude가 새로운 문제와 최근 커밋에서 이미 해결된 문제를 구별할 수 있다. 이는 리뷰의 철저함을 유지하면서 Claude의 추론을 활용해 수정된 코드에 대한 중복 피드백을 피한다.

**해설 신규** 이전 리뷰 결과를 context에 넣어 주면 Claude가 새 문제와 최근 commit에서 이미 해결된 문제를 구분할 수 있다. 그러면 리뷰의 철저함은 그대로 두고, Claude의 추론으로 이미 고친 코드에 대한 중복 피드백을 피할 수 있다.

## CCAR-F-paullarionov-0026

**EN** Your pipeline script runs `claude "Analyze this pull request for security issues"`, but the job hangs indefinitely. Logs show Claude Code is waiting for interactive input. What is the correct approach to run Claude Code in an automated pipeline?

What is the correct approach?

**기존** 파이프라인 스크립트가 `claude "Analyze this pull request for security issues"`를 실행하지만 작업이 무한정 멈춰 있다. 로그를 보면 Claude Code가 대화형 입력을 기다리고 있다. 자동화된 파이프라인에서 Claude Code를 실행하는 올바른 접근 방식은 무엇인가?

올바른 접근 방식은 무엇인가?

**신규** 파이프라인 스크립트가 `claude "Analyze this pull request for security issues"`를 실행하는데 job이 끝나지 않고 멈춰 있다. 로그를 보면 Claude Code가 interactive 입력을 기다리고 있다. 자동화 파이프라인에서 Claude Code를 실행하는 올바른 방법은 무엇인가?

- A. 기존: `--batch` 플래그를 추가한다: `claude --batch "Analyze this pull request for security issues"`.
  - 신규: `--batch` 플래그를 추가한다: `claude --batch "Analyze this pull request for security issues"`.
- B. 기존: `-p` 플래그를 추가한다: `claude -p "Analyze this pull request for security issues"`.
  - 신규: `-p` 플래그를 추가한다: `claude -p "Analyze this pull request for security issues"`.
- C. 기존: stdin을 `/dev/null`로 리디렉션한다: `claude "Analyze this pull request for security issues" < /dev/null`.
  - 신규: stdin을 `/dev/null`로 리다이렉트한다: `claude "Analyze this pull request for security issues" < /dev/null`.
- D. 기존: 명령을 실행하기 전에 환경 변수 `CLAUDE_HEADLESS=true`를 설정한다.
  - 신규: 명령을 실행하기 전에 환경 변수 `CLAUDE_HEADLESS=true`를 설정한다.

**해설 EN** The `-p` (or `--print`) flag is the documented way to run Claude Code non-interactively. It processes the prompt, prints the result to stdout, and exits without waiting for user input—ideal for CI/CD pipelines.

**해설 기존** `-p`(또는 `--print`) 플래그는 Claude Code를 비대화형으로 실행하기 위해 문서화된 방법이다. 프롬프트를 처리하고 결과를 stdout으로 출력한 뒤 사용자 입력을 기다리지 않고 종료하므로 CI/CD 파이프라인에 이상적이다.

**해설 신규** Claude Code를 non-interactive로 실행하는 공식 방법은 `-p`(또는 `--print`) 플래그다. 프롬프트를 처리하고 결과를 stdout에 출력한 뒤, 사용자 입력을 기다리지 않고 종료한다. CI/CD 파이프라인에 알맞은 방식이다.

## CCAR-F-paullarionov-0027

**EN** A pull request changes 14 files in an inventory tracking module. A single-pass review that analyzes all files together produces inconsistent results: detailed feedback on some files but shallow comments on others, missed obvious bugs, and contradictory feedback (a pattern is flagged in one file but identical code is approved in another file in the same PR). How should you restructure the review?

How should you restructure the review?

**기존** 하나의 pull request가 재고 추적 모듈의 14개 파일을 변경한다. 모든 파일을 함께 분석하는 단일 패스 리뷰는 일관되지 않은 결과를 낸다. 일부 파일에는 상세한 피드백을 주지만 다른 파일에는 얕은 코멘트만 달고, 명백한 버그를 놓치며, 모순된 피드백도 준다(같은 PR의 한 파일에서는 어떤 패턴을 지적하면서 다른 파일의 동일한 코드는 승인한다). 리뷰를 어떻게 재구성해야 하는가?

리뷰를 어떻게 재구성해야 하는가?

**신규** PR 하나가 재고 추적 모듈의 파일 14개를 변경한다. 파일 전체를 한 번에 분석하는 single-pass 리뷰는 결과가 일관되지 않다. 어떤 파일은 자세히 짚는데 다른 파일은 얕은 댓글만 달고, 뻔한 버그를 놓치고, 서로 모순되는 피드백도 한다. 같은 PR 안에서 한 파일의 패턴은 문제라고 지적하면서 똑같은 코드가 있는 다른 파일은 승인하는 식이다. 리뷰를 어떻게 다시 구성해야 하는가?

- A. 기존: PR 전체에 대한 독립적인 리뷰 패스를 세 번 실행하고, 세 번 중 최소 두 번에 나타나는 문제만 지적한다.
  - 신규: PR 전체를 대상으로 독립적인 리뷰를 세 번 돌리고, 세 번 중 최소 두 번 이상 나온 문제만 지적한다.
- B. 기존: 집중된 패스로 나눈다. 각 파일을 개별적으로 리뷰하여 로컬 문제를 찾은 다음, 별도의 통합 중심 패스를 실행하여 파일 간 데이터 흐름을 검토한다.
  - 신규: 집중 pass로 나눈다. 먼저 파일별로 따로 리뷰해 로컬 문제를 찾고, 이어서 별도의 통합 중심 pass로 파일 간 데이터 흐름을 살핀다.
- C. 기존: 자동화된 리뷰를 실행하기 전에 개발자에게 큰 PR을 3~4개 파일 단위의 더 작은 제출물로 나누도록 요구한다.
  - 신규: 자동 리뷰를 돌리기 전에 개발자가 큰 PR을 3~4개 파일 단위의 작은 PR로 나누어 제출하게 한다.
- D. 기존: 한 번의 패스로 14개 파일 모두에 충분히 주의를 기울일 수 있도록 더 큰 context window를 가진 더 큰 모델로 전환한다.
  - 신규: context window가 더 큰 모델로 바꿔, 한 번에 14개 파일 모두에 충분히 주의를 기울이게 한다.

**해설 EN** Focused per-file passes address the root cause—attention dilution—by ensuring consistent depth and reliable local issue detection. A separate integration-oriented pass then covers cross-file concerns such as dependency and data-flow interactions.

**해설 기존** 파일별로 집중된 패스는 일관된 깊이와 신뢰할 수 있는 로컬 문제 탐지를 보장함으로써 근본 원인인 attention dilution을 해결한다. 이어지는 별도의 통합 중심 패스는 의존성 및 데이터 흐름 상호작용 같은 파일 간 사안을 다룬다.

**해설 신규** 파일별 집중 pass는 근본 원인인 attention dilution(주의 분산)을 해결한다. 모든 파일을 같은 깊이로 보게 되고 로컬 문제도 안정적으로 찾을 수 있다. 그다음 통합 중심 pass를 따로 돌리면 의존성이나 데이터 흐름 같은 파일 간 문제를 다룰 수 있다.

## CCAR-F-paullarionov-0028

**EN** Your automated code review averages 15 findings per pull request, and developers report a 40% false-positive rate. The bottleneck is investigation time: developers must click into each finding to read Claude’s rationale before deciding whether to fix or dismiss it. Your CLAUDE.md already contains comprehensive rules for acceptable patterns, and stakeholders rejected any approach that filters findings before developers see them. What change best addresses investigation time?

What change best addresses investigation time?

**기존** 자동화된 코드 리뷰는 pull request당 평균 15개의 발견 사항을 내며, 개발자들은 40%의 false positive 비율을 보고한다. 병목은 조사 시간이다. 개발자는 수정할지 무시할지 결정하기 전에 각 발견 사항을 클릭해 들어가 Claude의 근거를 읽어야 한다. CLAUDE.md에는 이미 허용 가능한 패턴에 대한 포괄적인 규칙이 들어 있고, 이해관계자들은 개발자가 보기 전에 발견 사항을 필터링하는 모든 접근 방식을 거부했다. 조사 시간을 가장 잘 해결하는 변경은 무엇인가?

어떤 변경이 조사 시간을 가장 잘 해결하는가?

**신규** 자동 코드 리뷰가 PR당 평균 15개를 지적하고, 개발자들은 오탐률이 40%라고 한다. 병목은 확인에 드는 시간이다. 개발자가 지적 하나하나를 클릭해 Claude의 근거를 읽어야 고칠지 무시할지 정할 수 있기 때문이다. CLAUDE.md에는 허용되는 패턴에 대한 규칙이 이미 충분히 들어 있다. 또 이해관계자들은 개발자에게 보이기 전에 지적을 걸러내는 방식을 모두 반대했다. 확인 시간 문제를 가장 잘 해결하는 변경은 무엇인가?

- A. 기존: Claude가 각 발견 사항에 근거와 신뢰도 추정치를 직접 포함하도록 요구한다.
  - 신규: 각 지적에 Claude의 근거와 신뢰도 추정치를 바로 포함하도록 한다.
- B. 기존: 발견 사항 패턴을 분석하여 과거 false positive 시그니처와 일치하는 항목을 자동으로 억제하는 후처리기를 추가한다.
  - 신규: 지적의 패턴을 분석해, 과거 오탐 특징과 일치하는 것을 자동으로 숨기는 후처리기를 추가한다.
- C. 기존: 발견 사항을 “blocking issues”와 “suggestions”로 분류하고, 수준별로 서로 다른 리뷰 요건을 둔다.
  - 신규: 지적을 “blocking issues”와 “suggestions”로 분류하고, 등급별로 리뷰 요건을 다르게 둔다.
- D. 기존: 개발자가 보기 전에 불확실한 지적을 걸러내어, Claude가 신뢰도 높은 발견 사항만 보여 주도록 구성한다.
  - 신규: 신뢰도가 높은 지적만 보여 주도록 설정해, 불확실한 지적은 개발자에게 보이기 전에 걸러낸다.

**해설 EN** Including rationale and confidence directly in each finding reduces investigation time by letting developers quickly triage without opening each finding. It satisfies the “no filtering” constraint because all findings remain visible while accelerating developer decision-making.

**해설 기존** 각 발견 사항에 근거와 신뢰도를 직접 포함하면 개발자가 각 발견 사항을 열어 보지 않고도 빠르게 분류할 수 있어 조사 시간이 줄어든다. 모든 발견 사항이 계속 보이므로 “필터링 금지” 제약을 충족하면서도 개발자의 의사 결정을 가속한다.

**해설 신규** 근거와 신뢰도를 각 지적에 바로 넣으면, 개발자가 지적을 일일이 열어 보지 않고도 빠르게 분류할 수 있어 확인 시간이 줄어든다. 모든 지적이 그대로 보이므로 “걸러내지 않는다”는 조건도 지키면서 개발자의 판단은 빨라진다.

## CCAR-F-paullarionov-0029

**EN** Analysis of your automated code review shows large differences in false-positive rates by finding category: security/correctness findings have 8% false positives, performance findings 18%, style/naming findings 52%, and documentation findings 48%. Developer surveys show growing distrust—many start dismissing findings without reading because “half are wrong.” High-false-positive categories erode trust in accurate categories. Which approach best restores developer trust while improving the system?

Which approach best restores developer trust?

**기존** 자동화된 코드 리뷰를 분석한 결과 발견 사항 카테고리별 false positive 비율에 큰 차이가 있다. 보안/정확성 발견 사항은 8%, 성능 발견 사항은 18%, 스타일/네이밍 발견 사항은 52%, 문서화 발견 사항은 48%의 false positive를 보인다. 개발자 설문 결과 불신이 커지고 있으며, “절반은 틀렸다”는 이유로 많은 개발자가 읽지도 않고 발견 사항을 무시하기 시작한다. false positive가 많은 카테고리가 정확한 카테고리에 대한 신뢰까지 약화시킨다. 시스템을 개선하면서 개발자의 신뢰를 가장 잘 회복하는 접근 방식은 무엇인가?

어떤 접근 방식이 개발자의 신뢰를 가장 잘 회복하는가?

**신규** 자동 코드 리뷰를 분석해 보니 카테고리별 오탐률 차이가 크다. security/correctness 지적은 오탐이 8%, performance 지적은 18%, style/naming 지적은 52%, documentation 지적은 48%다. 개발자 설문에서는 불신이 커지고 있다. “절반은 틀린 지적”이라며 내용을 읽지도 않고 넘기는 개발자가 늘고 있다. 오탐이 많은 카테고리 때문에 정확한 카테고리까지 신뢰를 잃고 있는 상황이다. 시스템을 개선하면서 개발자의 신뢰를 되찾는 데 가장 좋은 방법은 무엇인가?

- A. 기존: false positive가 많은 카테고리(스타일, 네이밍, 문서화)를 일시적으로 비활성화하고, 프롬프트를 개선하는 동안 정밀도가 높은 카테고리만 유지한다.
  - 신규: 오탐이 많은 카테고리(style, naming, documentation)를 일시적으로 끄고, 정밀도가 높은 카테고리만 남긴 채 prompt를 개선한다.
- B. 기존: 모든 카테고리를 활성화한 채로 두되, 각 발견 사항에 신뢰도 점수를 표시하여 개발자가 무엇을 조사할지 결정하게 한다.
  - 신규: 모든 카테고리를 켜 두되 각 지적에 신뢰도 점수를 함께 표시해, 개발자가 무엇을 살펴볼지 직접 정하게 한다.
- C. 기존: 모든 카테고리를 활성화한 채로 두고, 향후 몇 주에 걸쳐 각 카테고리의 정확도를 높이도록 few-shot 예시를 추가한다.
  - 신규: 모든 카테고리를 켜 두고, 앞으로 몇 주에 걸쳐 few-shot 예시를 추가해 카테고리별 정확도를 높인다.
- D. 기존: 전체 false positive 비율을 낮추기 위해 모든 카테고리에 일괄적으로 엄격도를 낮추는 조정을 적용한다.
  - 신규: 모든 카테고리의 엄격도를 똑같이 낮춰 전체 오탐률을 떨어뜨린다.

**해설 EN** Temporarily disabling high-false-positive categories immediately stops trust erosion by removing noisy findings that cause developers to dismiss everything, while preserving value from high-precision categories like security and correctness. It also creates space to improve prompts for problematic categories before re-enabling them.

**해설 기존** false positive가 많은 카테고리를 일시적으로 비활성화하면, 개발자가 모든 것을 무시하게 만드는 노이즈 많은 발견 사항을 제거하여 신뢰 약화를 즉시 멈추면서 보안과 정확성 같은 정밀도 높은 카테고리의 가치는 보존한다. 또한 문제가 있는 카테고리를 다시 활성화하기 전에 프롬프트를 개선할 여유를 만들어 준다.

**해설 신규** 오탐이 많은 카테고리를 일시적으로 끄면 개발자가 모든 지적을 무시하게 만드는 노이즈가 사라져, 신뢰가 더 무너지는 것을 바로 막을 수 있다. security나 correctness처럼 정밀도가 높은 카테고리의 가치는 그대로 유지된다. 문제가 있는 카테고리는 그동안 prompt를 개선한 뒤 다시 켜면 된다.

## CCAR-F-paullarionov-0030

**EN** Your team wants to reduce API costs for automated analysis. Currently, synchronous Claude calls support two workflows: (1) a blocking pre-merge check that must complete before developers can merge, and (2) a technical debt report generated overnight for review the next morning. Your manager proposes moving both to the Message Batches API to save 50%. How should you evaluate this proposal?

How should you evaluate this proposal?

**기존** 팀은 자동화된 분석의 API 비용을 줄이려 한다. 현재 동기 방식 Claude 호출이 두 가지 워크플로를 지원한다. (1) 개발자가 머지하기 전에 반드시 완료되어야 하는 차단형 pre-merge 검사, (2) 다음 날 아침 검토를 위해 밤새 생성되는 기술 부채 보고서. 관리자는 50% 절감을 위해 둘 다 Message Batches API로 옮길 것을 제안한다. 이 제안을 어떻게 평가해야 하는가?

이 제안을 어떻게 평가해야 하는가?

**신규** 팀이 자동 분석의 API 비용을 줄이려 한다. 지금은 synchronous Claude 호출로 두 가지 workflow를 돌리고 있다. (1) 개발자가 merge하려면 반드시 끝나야 하는 blocking pre-merge 검사, (2) 다음 날 아침에 확인할 기술 부채 보고서를 밤사이 생성하는 작업이다. 매니저는 비용을 50% 아끼려고 두 workflow를 모두 Message Batches API로 옮기자고 제안한다. 이 제안을 어떻게 평가해야 하는가?

- A. 기존: 둘 다 batch processing으로 옮기고, batch가 너무 오래 걸리면 동기 호출로 fallback한다.
  - 신규: 둘 다 batch 처리로 옮기되, batch가 너무 오래 걸리면 synchronous 호출로 대체한다.
- B. 기존: 두 워크플로 모두 batch processing으로 옮기고, 상태 polling으로 완료를 확인한다.
  - 신규: 두 workflow 모두 batch 처리로 옮기고, 상태를 polling해서 완료 여부를 확인한다.
- C. 기존: 기술 부채 보고서에만 batch processing을 사용하고, pre-merge 검사에는 동기 호출을 유지한다.
  - 신규: batch 처리는 기술 부채 보고서에만 쓰고, pre-merge 검사는 synchronous 호출을 유지한다.
- D. 기존: batch 결과 순서 문제를 피하기 위해 두 워크플로 모두 동기 호출을 유지한다.
  - 신규: batch 결과의 순서 문제를 피하려고 두 workflow 모두 synchronous 호출을 유지한다.

**해설 EN** Message Batches API processing can take up to 24 hours with no latency SLA, which is acceptable for overnight technical debt reports but unacceptable for blocking pre-merge checks where developers wait. This matches each workflow to the right API based on latency requirements.

**해설 기존** Message Batches API 처리는 지연 시간 SLA 없이 최대 24시간이 걸릴 수 있으며, 이는 밤새 생성되는 기술 부채 보고서에는 허용되지만 개발자가 기다리는 차단형 pre-merge 검사에는 허용되지 않는다. 이는 지연 시간 요구 사항에 따라 각 워크플로를 알맞은 API에 짝짓는 것이다.

**해설 신규** Message Batches API는 처리에 최대 24시간이 걸릴 수 있고 지연 시간 SLA도 없다. 밤사이 만드는 기술 부채 보고서에는 문제가 없지만, 개발자가 기다리는 blocking pre-merge 검사에는 받아들일 수 없다. 지연 시간 요건에 맞게 workflow마다 알맞은 API를 짝지은 선택이다.

## CCAR-F-paullarionov-0031

**EN** You asked Claude Code to implement a function that transforms API responses into an internal normalized format. After two iterations, the output structure still doesn’t match expectations—some fields are nested differently and timestamps are formatted incorrectly. You described requirements in prose, but Claude interprets them differently each time.

Which approach is most effective for the next iteration?

**기존** Claude Code에게 API 응답을 내부 정규화 형식으로 변환하는 함수를 구현하도록 요청했다. 두 번의 반복 후에도 출력 구조가 기대와 여전히 맞지 않는다. 일부 필드는 다르게 중첩되어 있고 타임스탬프 형식도 올바르지 않다. 요구 사항을 산문으로 설명했지만 Claude는 매번 다르게 해석한다.

다음 반복에 가장 효과적인 접근 방식은 무엇인가?

**신규** Claude Code에게 API 응답을 내부 정규화 형식으로 변환하는 함수를 구현해 달라고 했다. 두 번 반복했지만 출력 구조는 여전히 기대와 다르다. 일부 필드의 중첩 방식이 다르고 timestamp 형식도 틀리다. 요구사항을 글로 설명했는데 Claude가 매번 다르게 해석한다.

다음 반복에서 가장 효과적인 방법은 무엇인가?

- A. 기존: 기대하는 출력 구조를 설명하는 JSON schema를 작성하고, 매 반복 후 Claude의 출력을 이에 대해 검증한다.
  - 신규: 기대하는 출력 구조를 설명하는 JSON schema를 작성하고, 반복할 때마다 Claude의 출력을 그 schema로 검증한다.
- B. 기존: 대표적인 API 응답에 대해 기대하는 변환을 보여 주는 2~3개의 구체적인 입력-출력 예시를 제공한다.
  - 신규: 대표적인 API 응답에 대해 기대하는 변환 결과를 보여 주는 입력-출력 예시를 2~3개 제공한다.
- C. 기존: 정확한 필드 매핑, 중첩 규칙, 타임스탬프 형식 문자열을 지정하여 요구 사항을 더 기술적으로 정밀하게 다시 작성한다.
  - 신규: 정확한 필드 매핑, 중첩 규칙, timestamp 형식 문자열까지 명시해 요구사항을 더 기술적으로 정밀하게 다시 쓴다.
- D. 기존: 해석이 어디서 갈라지는지 파악하기 위해 Claude에게 현재 요구 사항을 어떻게 이해하고 있는지 설명하도록 요청한다.
  - 신규: Claude에게 요구사항을 어떻게 이해했는지 설명하게 해서, 해석이 어디서 갈리는지 찾는다.

**해설 EN** Concrete input-output examples remove ambiguity inherent in prose descriptions by showing Claude the exact expected transformation results. This directly addresses the root cause—misinterpretation of textual requirements—by providing unambiguous patterns for field nesting and timestamp formatting.

**해설 기존** 구체적인 입력-출력 예시는 Claude에게 기대하는 변환 결과를 정확히 보여 줌으로써 산문 설명에 내재한 모호성을 제거한다. 이는 필드 중첩과 타임스탬프 형식에 대한 명확한 패턴을 제공함으로써 근본 원인인 텍스트 요구 사항의 오해를 직접 해결한다.

**해설 신규** 구체적인 입력-출력 예시는 기대하는 변환 결과를 그대로 보여 주므로, 글로 설명할 때 생기는 모호함이 사라진다. 요구사항을 글로 읽고 오해하는 것이 근본 원인인데, 예시가 필드 중첩과 timestamp 형식에 대한 명확한 패턴을 주어 이를 직접 해결한다.

## CCAR-F-paullarionov-0032

**EN** You need to add Slack as a new notification channel. The existing codebase has clear, established patterns for email, SMS, and push channels. However, Slack’s API offers fundamentally different integration approaches—incoming webhooks (simple, one-way), bot tokens (support delivery confirmation and programmatic control), or Slack Apps (two-way events, requires workspace approval). Your task says “add Slack support” without specifying integration method or requiring advanced features like delivery tracking.

How should you approach this task?

**기존** Slack을 새로운 알림 채널로 추가해야 한다. 기존 코드베이스에는 이메일, SMS, 푸시 채널에 대한 명확하게 확립된 패턴이 있다. 그러나 Slack의 API는 근본적으로 다른 통합 방식을 제공한다. incoming webhook(단순, 단방향), bot token(전달 확인과 프로그래밍 방식 제어 지원), Slack Apps(양방향 이벤트, 워크스페이스 승인 필요). 작업은 통합 방식을 지정하지 않은 채 “add Slack support”라고만 하며, 전달 추적 같은 고급 기능도 요구하지 않는다.

이 작업에 어떻게 접근해야 하는가?

**신규** 알림 채널로 Slack을 새로 추가해야 한다. 기존 코드베이스에는 email, SMS, push 채널의 명확하고 확립된 패턴이 있다. 하지만 Slack API는 연동 방식이 근본적으로 다르다. incoming webhook은 단순하고 단방향이다. bot token은 전송 확인과 프로그래밍 방식의 제어를 지원한다. Slack App은 양방향 이벤트를 지원하지만 workspace 승인이 필요하다. 작업 지시는 “Slack 지원 추가”뿐이며, 연동 방식도 정하지 않았고 전송 추적 같은 고급 기능도 요구하지 않는다.

이 작업을 어떻게 진행해야 하는가?

- A. 기존: 기존의 단방향 알림 패턴에 맞추어 incoming webhook을 사용하는 direct execution 모드로 시작한다.
  - 신규: direct execution mode로 시작해, 기존의 단방향 알림 패턴에 맞게 incoming webhook을 사용한다.
- B. 기존: planning 모드로 전환하여 통합 옵션과 아키텍처상의 영향을 탐색한 뒤, 구현 전에 권장안을 제시한다.
  - 신규: planning mode로 전환해 연동 방식의 선택지와 아키텍처에 미치는 영향을 살펴보고, 구현 전에 추천안을 제시한다.
- C. 기존: 통합 방식 결정은 미루고, 기존 패턴을 사용해 Slack 채널 클래스의 뼈대를 만드는 direct execution 모드로 시작한다.
  - 신규: direct execution mode로 시작해 기존 패턴대로 Slack 채널 클래스의 뼈대를 만들고, 연동 방식 결정은 뒤로 미룬다.
- D. 기존: 전달 확인이 가능하도록 bot-token 방식을 사용하는 direct execution 모드로 시작한다.
  - 신규: direct execution mode로 시작해, 전송 확인이 가능하도록 bot token 방식을 사용한다.

**해설 EN** Slack integration has multiple valid approaches with significantly different architectural implications, and requirements are ambiguous. Planning mode lets you evaluate trade-offs among webhooks, bot tokens, and Slack Apps and align on an approach before implementation.

**해설 기존** Slack 통합에는 아키텍처상의 영향이 크게 다른 여러 유효한 접근 방식이 있고 요구 사항도 모호하다. planning 모드를 사용하면 webhook, bot token, Slack Apps 간의 트레이드오프를 평가하고 구현 전에 접근 방식에 합의할 수 있다.

**해설 신규** Slack 연동에는 타당한 방식이 여러 가지이고 아키텍처에 미치는 영향이 크게 다른데, 요구사항은 모호하다. planning mode에서는 webhook, bot token, Slack App의 장단점을 비교하고 구현에 들어가기 전에 방향을 맞출 수 있다.

## CCAR-F-paullarionov-0033

**EN** Your CLAUDE.md file has grown to 400+ lines containing coding standards, testing conventions, a detailed PR review checklist, deployment instructions, and database migration procedures. You want Claude to always follow coding standards and testing conventions, but apply PR review, deploy, and migration guidance only when doing those tasks.

Which restructuring approach is most effective?

**기존** CLAUDE.md 파일이 코딩 표준, 테스트 규칙, 상세한 PR 리뷰 체크리스트, 배포 지침, 데이터베이스 마이그레이션 절차를 담아 400줄 이상으로 커졌다. Claude가 코딩 표준과 테스트 규칙은 항상 따르게 하되, PR 리뷰, 배포, 마이그레이션 지침은 해당 작업을 할 때에만 적용되게 하려 한다.

어떤 재구성 접근 방식이 가장 효과적인가?

**신규** CLAUDE.md가 400줄이 넘게 커졌다. 코딩 표준, 테스트 규칙, 상세한 PR 리뷰 체크리스트, 배포 방법, 데이터베이스 migration 절차가 들어 있다. Claude가 코딩 표준과 테스트 규칙은 항상 따르고, PR 리뷰, 배포, migration 가이드는 해당 작업을 할 때만 적용하게 하고 싶다.

어떻게 재구성하는 것이 가장 효과적인가?

- A. 기존: 모든 지침을 워크플로 유형별로 구성한 별도의 Skills 파일로 옮기고, CLAUDE.md에는 간단한 프로젝트 설명만 남긴다.
  - 신규: 모든 가이드를 workflow 유형별 Skills 파일로 옮기고, CLAUDE.md에는 간단한 프로젝트 설명만 남긴다.
- B. 기존: 모든 내용을 CLAUDE.md에 유지하되, `@import` 구문을 사용하여 카테고리별로 따로 관리되는 파일로 구성한다.
  - 신규: 모든 내용을 CLAUDE.md에 두되, `@import` 문법으로 카테고리별로 따로 관리하는 파일에 나눠 정리한다.
- C. 기존: CLAUDE.md를 경로에 묶인 glob 패턴을 가진 `.claude/rules/` 아래의 파일로 분할하여, 각 규칙이 관련 파일 유형에서만 로드되게 한다.
  - 신규: CLAUDE.md를 `.claude/rules/` 아래의 파일로 나누고 경로 기반 glob 패턴을 지정해, 각 규칙이 해당 파일 유형에서만 로드되게 한다.
- D. 기존: 보편적인 표준은 CLAUDE.md에 유지하고, 워크플로별 지침(PR 리뷰, 배포, 마이그레이션)은 trigger keyword를 가진 Skills로 만든다.
  - 신규: 공통 표준은 CLAUDE.md에 두고, workflow별 가이드(PR 리뷰, 배포, migration)는 trigger 키워드를 지정한 Skills로 만든다.

**해설 EN** CLAUDE.md content loads in every session, ensuring coding standards and testing conventions always apply, while Skills are invoked on demand when Claude detects trigger keywords—ideal for workflow-specific guidance like PR review, deployment, and migrations.

**해설 기존** CLAUDE.md 내용은 모든 세션에서 로드되므로 코딩 표준과 테스트 규칙이 항상 적용되는 반면, Skills는 Claude가 trigger keyword를 감지할 때 필요에 따라 호출되므로 PR 리뷰, 배포, 마이그레이션 같은 워크플로별 지침에 이상적이다.

**해설 신규** CLAUDE.md 내용은 모든 session에서 로드되므로 코딩 표준과 테스트 규칙이 항상 적용된다. 반면 Skills는 Claude가 trigger 키워드를 감지했을 때 필요에 따라 호출된다. PR 리뷰, 배포, migration처럼 workflow별로 쓰는 가이드에 알맞은 방식이다.

## CCAR-F-paullarionov-0034

**EN** You’re tasked with restructuring your team’s monolithic application into microservices. This impacts changes across dozens of files and requires decisions about service boundaries and module dependencies.

Which approach should you choose?

**기존** 팀의 모놀리식 애플리케이션을 마이크로서비스로 재구성하는 작업을 맡았다. 이는 수십 개 파일에 걸친 변경에 영향을 주며, 서비스 경계와 모듈 의존성에 대한 결정이 필요하다.

어떤 접근 방식을 선택해야 하는가?

**신규** 팀의 monolithic 애플리케이션을 microservice로 재구성하는 일을 맡았다. 수십 개 파일에 걸친 변경이 필요하고, service 경계와 module 의존성에 대한 결정도 필요하다.

어떤 방식을 택해야 하는가?

- A. 기존: planning 모드로 전환하여 코드베이스를 탐색하고 의존성을 파악하며, 변경을 하기 전에 구현 접근 방식을 설계한다.
  - 신규: planning mode로 전환해 코드베이스를 탐색하고 의존성을 파악한 뒤, 변경에 들어가기 전에 구현 방식을 설계한다.
- B. 기존: direct execution 모드로 시작하고, 구현 중에 예상치 못한 복잡성을 만난 뒤에야 planning으로 전환한다.
  - 신규: direct execution mode로 시작하고, 구현 중에 예상치 못한 복잡성을 만나면 그때 planning으로 전환한다.
- C. 기존: direct execution 모드로 시작하여 점진적으로 변경하고, 구현을 통해 자연스러운 서비스 경계가 드러나게 한다.
  - 신규: direct execution mode로 시작해 조금씩 변경하면서, 구현 과정에서 자연스러운 service 경계가 드러나게 한다.
- D. 기존: 각 서비스 구조를 지정하는 상세한 사전 지침과 함께 direct execution을 사용한다.
  - 신규: 각 service의 구조를 구체적으로 지정한 상세한 지시를 미리 주고 direct execution으로 진행한다.

**해설 EN** Planning mode is the right strategy for complex architectural restructuring like splitting a monolith: it allows safe exploration and informed decisions about boundaries before committing to potentially expensive changes across many files.

**해설 기존** planning 모드는 모놀리스 분할 같은 복잡한 아키텍처 재구성에 알맞은 전략이다. 많은 파일에 걸친 비용이 클 수 있는 변경을 확정하기 전에, 안전한 탐색과 경계에 대한 충분한 정보에 기반한 결정을 가능하게 한다.

**해설 신규** monolith를 쪼개는 것처럼 복잡한 아키텍처 재구성에는 planning mode가 맞는 전략이다. 여러 파일에 걸쳐 비용이 클 수 있는 변경을 시작하기 전에, 안전하게 탐색하고 경계에 대해 충분히 알고 결정할 수 있기 때문이다.

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

## CCAR-F-paullarionov-0036

**EN** Your team uses a `/commit` skill in `.claude/skills/commit/SKILL.md`. A developer wants to customize it for their personal workflow (different commit message format, extra checks) without affecting teammates.

What do you recommend?

**기존** 팀은 `.claude/skills/commit/SKILL.md`에 있는 `/commit` skill을 사용한다. 한 개발자가 팀원에게 영향을 주지 않으면서 자신의 개인 워크플로(다른 커밋 메시지 형식, 추가 검사)에 맞게 이를 커스터마이징하려 한다.

무엇을 권장하는가?

**신규** 팀이 `.claude/skills/commit/SKILL.md`에 있는 `/commit` skill을 쓰고 있다. 한 개발자가 자기 작업 방식에 맞게 이 skill을 바꾸고 싶어 한다(commit 메시지 형식을 다르게 하고 검사를 추가). 팀원에게는 영향을 주고 싶지 않다.

어떻게 하라고 권해야 하는가?

- A. 기존: `~/.claude/skills/` 아래에 `/my-commit`처럼 다른 이름으로 개인용 버전을 만든다.
  - 신규: `~/.claude/skills/` 아래에 `/my-commit`처럼 다른 이름으로 개인용 버전을 만든다.
- B. 기존: 프로젝트 skill frontmatter에 사용자 이름에 기반한 조건부 로직을 추가한다.
  - 신규: 프로젝트 skill의 frontmatter에 username을 기준으로 하는 조건 로직을 추가한다.
- C. 기존: `~/.claude/skills/commit/SKILL.md`에 같은 이름으로 개인용 버전을 만든다.
  - 신규: `~/.claude/skills/commit/SKILL.md`에 같은 이름으로 개인용 버전을 만든다.
- D. 기존: 개인 skill frontmatter에 `override: true`를 설정하여 프로젝트 버전보다 우선하게 한다.
  - 신규: 개인 skill의 frontmatter에 `override: true`를 설정해 프로젝트 버전보다 우선하게 한다.

**해설 EN** Skill resolution is positional: enterprise overrides personal, and personal overrides project. A personal skill at `~/.claude/skills/commit/SKILL.md` therefore shadows the team's `.claude/skills/commit/SKILL.md` for that developer alone — nothing in the repository changes, so teammates keep running the project version and `/commit` behaves the same for everyone else. A works mechanically but is the weaker recommendation: the project `/commit` stays active alongside `/my-commit`, and two skills with near-identical `description` fields make Claude's automatic skill selection unpredictable, while breaking the muscle memory and team docs that say to run `/commit`. B fails because skill frontmatter has no conditional or username facility, and it would require editing the shared project file the scenario rules out. D fails because there is no `override` field — precedence comes from location, not from a declaration.

**해설 기존** Skill 해석은 위치에 따라 정해진다. enterprise가 personal을 덮어쓰고, personal이 project를 덮어쓴다. 따라서 `~/.claude/skills/commit/SKILL.md`에 있는 개인 skill은 해당 개발자에게만 팀의 `.claude/skills/commit/SKILL.md`를 가린다. 저장소의 어떤 것도 바뀌지 않으므로 팀원들은 계속 프로젝트 버전을 실행하고 `/commit`은 다른 모든 사람에게 동일하게 동작한다. A는 기계적으로는 동작하지만 더 약한 권장안이다. 프로젝트 `/commit`이 `/my-commit`과 함께 계속 활성 상태로 남고, `description` 필드가 거의 같은 두 skill은 Claude의 자동 skill 선택을 예측할 수 없게 만들며, `/commit`을 실행하라는 몸에 밴 습관과 팀 문서도 깨뜨린다. B는 skill frontmatter에 조건부 기능이나 사용자 이름 기능이 없기 때문에 실패하며, 시나리오가 배제한 공유 프로젝트 파일 수정도 필요하게 된다. D는 `override` 필드가 없기 때문에 실패한다. 우선순위는 선언이 아니라 위치에서 결정된다.

**해설 신규** Skill은 위치에 따라 우선순위가 정해진다. enterprise가 personal보다, personal이 project보다 우선한다. 따라서 `~/.claude/skills/commit/SKILL.md`에 만든 개인 skill은 그 개발자에게만 팀의 `.claude/skills/commit/SKILL.md`를 가린다. 저장소는 전혀 바뀌지 않으므로 팀원은 계속 프로젝트 버전을 쓰고, 다른 사람에게 `/commit`은 똑같이 동작한다. A도 기술적으로는 동작하지만 덜 좋은 권장안이다. 프로젝트의 `/commit`이 `/my-commit`과 함께 활성 상태로 남고, `description`이 거의 같은 skill이 둘이 되어 Claude의 자동 skill 선택을 예측하기 어려워진다. 게다가 `/commit`을 실행하라고 안내하는 팀 문서와 손에 익은 습관도 깨진다. B는 skill frontmatter에 조건이나 username 기능이 없어서 틀렸고, 시나리오에서 제외한 공유 프로젝트 파일을 수정해야 한다는 문제도 있다. D는 `override` 필드가 없어서 틀렸다. 우선순위는 선언이 아니라 위치로 정해진다.

## CCAR-F-paullarionov-0037

**EN** Your team has used Claude Code for months. Recently, three developers report Claude follows the guidance “always include comprehensive error handling,” but a fourth developer who just joined says Claude does not follow it. All four work in the same repo and have up-to-date code.

What is the most likely cause and fix?

**기존** 팀은 몇 달째 Claude Code를 사용해 왔다. 최근 세 명의 개발자는 Claude가 "항상 포괄적인 오류 처리를 포함하라"는 지침을 따른다고 보고하지만, 막 합류한 네 번째 개발자는 Claude가 이를 따르지 않는다고 말한다. 네 사람 모두 같은 repo에서 작업하며 코드는 최신 상태이다.

가장 가능성이 높은 원인과 해결책은 무엇인가?

**신규** 팀은 몇 달째 Claude Code를 쓰고 있다. 최근 개발자 세 명은 Claude가 “항상 포괄적인 error handling을 포함하라”는 지침을 따른다고 하는데, 새로 합류한 네 번째 개발자는 Claude가 따르지 않는다고 한다. 네 명 모두 같은 저장소에서 작업하고 코드도 최신이다.

가장 가능성이 높은 원인과 해결 방법은 무엇인가?

- A. 기존: 해당 지침이 프로젝트의 `.claude/CLAUDE.md`가 아니라 기존 개발자들의 사용자 수준 `~/.claude/CLAUDE.md` 파일에 들어 있다. 모든 팀원이 받을 수 있도록 지침을 프로젝트 수준 파일로 옮긴다.
  - 신규: 이 지침이 프로젝트의 `.claude/CLAUDE.md`가 아니라 기존 개발자들의 사용자 수준 `~/.claude/CLAUDE.md`에만 들어 있다. 팀원 모두가 적용받도록 지침을 프로젝트 수준 파일로 옮긴다.
- B. 기존: 새 개발자의 `~/.claude/CLAUDE.md`에 프로젝트 설정을 덮어쓰는 상충하는 지침이 있으므로, 해당 섹션을 삭제해야 한다.
  - 신규: 새 개발자의 `~/.claude/CLAUDE.md`에 프로젝트 설정을 덮어쓰는 충돌하는 지침이 있다. 그 부분을 삭제해야 한다.
- C. 기존: Claude Code는 시간이 지나면서 사용자별 선호를 학습하므로, 새 개발자는 Claude가 "기억"할 때까지 요구사항을 반복해야 한다.
  - 신규: Claude Code는 시간이 지나면서 사용자별 선호를 학습하므로, 새 개발자는 Claude가 “기억”할 때까지 요구사항을 반복해서 말해야 한다.
- D. 기존: Claude Code는 CLAUDE.md를 처음 읽은 뒤 캐시하며, 기존 개발자들은 캐시된 버전을 사용한다. 모두 Claude Code 캐시를 지워야 한다.
  - 신규: Claude Code는 CLAUDE.md를 처음 읽을 때 cache하고, 기존 개발자들은 cache된 버전을 쓰고 있다. 모두 Claude Code cache를 지워야 한다.

**해설 EN** If the guidance was added only to the original developers’ user-level configs and not to the project-level `.claude/CLAUDE.md`, new team members won’t receive it. Moving it to the project-level configuration ensures all current and future team members automatically get the guidance.

**해설 기존** 지침이 프로젝트 수준 `.claude/CLAUDE.md`가 아니라 기존 개발자들의 사용자 수준 설정에만 추가되었다면, 새 팀원은 그 지침을 받지 못한다. 이를 프로젝트 수준 설정으로 옮기면 현재와 미래의 모든 팀원이 자동으로 지침을 받게 된다.

**해설 신규** 지침이 기존 개발자들의 사용자 수준 설정에만 추가되고 프로젝트 수준 `.claude/CLAUDE.md`에는 없으면, 새 팀원은 그 지침을 받지 못한다. 프로젝트 수준 설정으로 옮기면 현재와 앞으로의 모든 팀원이 자동으로 지침을 적용받는다.

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

## CCAR-F-paullarionov-0039

**EN** Your team created a `/migration` skill that generates database migration files. It takes the migration name via `$ARGUMENTS`. In production you observe three issues: (1) developers often run the skill without arguments, causing poorly named files, (2) the skill sometimes uses database schema details from unrelated prior conversations, and (3) a developer accidentally ran destructive test cleanup when the skill had broad tool access.

Which configuration approach fixes all three problems?

**기존** 팀이 데이터베이스 마이그레이션 파일을 생성하는 `/migration` skill을 만들었다. 이 skill은 `$ARGUMENTS`로 마이그레이션 이름을 받는다. 프로덕션에서 세 가지 문제가 관찰된다. (1) 개발자들이 인자 없이 skill을 자주 실행하여 파일 이름이 부실하게 지어지고, (2) skill이 관련 없는 이전 대화의 데이터베이스 스키마 세부 정보를 가끔 사용하며, (3) skill에 광범위한 도구 접근 권한이 있을 때 한 개발자가 실수로 파괴적인 테스트 정리 작업을 실행했다.

세 가지 문제를 모두 해결하는 구성 방식은 무엇인가?

**신규** 팀이 database migration 파일을 생성하는 `/migration` skill을 만들었다. migration 이름은 `$ARGUMENTS`로 받는다. 운영 중에 세 가지 문제가 생겼다. (1) 개발자들이 인자 없이 skill을 실행하는 일이 잦아 파일 이름이 엉망이 된다. (2) skill이 관련 없는 이전 대화의 database schema 정보를 쓰는 경우가 있다. (3) skill에 도구 권한이 넓게 열려 있을 때 한 개발자가 실수로 파괴적인 테스트 정리 작업을 실행했다.

세 문제를 모두 해결하는 설정 방법은 무엇인가?

- A. 기존: 특정 입력을 강제하도록 `$ARGUMENTS` 대신 위치 매개변수 `$1`과 `$2`를 사용하고, 컨텍스트 제어를 위해 `@` 구문으로 명시적인 스키마 파일 참조를 포함하며, 파괴적인 작업에 대한 경고를 frontmatter description에 추가한다.
  - 신규: `$ARGUMENTS` 대신 위치 매개변수 `$1`, `$2`를 써서 입력을 구체적으로 강제하고, `@` 문법으로 schema 파일을 명시적으로 참조해 context를 통제하고, frontmatter description에 파괴적 작업에 대한 경고를 추가한다.
- B. 기존: 필수 매개변수를 요청하도록 frontmatter에 `argument-hint`를 추가하고, 실행을 격리하기 위해 `context: fork`를 사용하며, `allowed-tools`를 파일 쓰기 작업으로 제한한다.
  - 신규: frontmatter에 `argument-hint`를 추가해 필수 매개변수를 요청하고, `context: fork`로 실행을 격리하고, `allowed-tools`를 파일 쓰기 작업으로 제한한다.
- C. 기존: `/migration-create`와 `/migration-apply` skill로 분리하고, 마이그레이션 이름이 없으면 요청하도록 검증 지침을 추가하며, 각각에 서로 다른 `allowed-tools` 범위를 사용한다.
  - 신규: `/migration-create`와 `/migration-apply` skill로 나누고, migration 이름이 없으면 요청하라는 검증 지시를 추가하고, 각 skill마다 다른 `allowed-tools` 범위를 쓴다.
- D. 기존: `$ARGUMENTS`가 유효한 이름인지 확인하도록 skill SKILL.md에 검증 지침을 추가하고, 이전 대화 컨텍스트를 무시하라는 프롬프트를 추가하며, 피해야 할 금지된 작업을 나열한다.
  - 신규: skill의 SKILL.md에 `$ARGUMENTS`가 유효한 이름인지 확인하라는 검증 지시를 넣고, 이전 대화 context를 무시하라는 prompt를 추가하고, 하지 말아야 할 작업을 나열한다.

**해설 EN** This uses three separate configuration features to address each problem: `argument-hint` improves argument entry and reduces missing arguments, `context: fork` prevents context leakage from prior conversations, and `allowed-tools` constrains the skill to safe file-writing operations, preventing destructive actions.

**해설 기존** 이 방식은 세 가지 별개의 구성 기능으로 각 문제를 해결한다. `argument-hint`는 인자 입력을 개선하여 누락된 인자를 줄이고, `context: fork`는 이전 대화로부터의 컨텍스트 누출을 막으며, `allowed-tools`는 skill을 안전한 파일 쓰기 작업으로 제한하여 파괴적인 동작을 방지한다.

**해설 신규** 문제마다 서로 다른 설정 기능을 쓰는 방식이다. `argument-hint`는 인자 입력을 돕고 인자가 빠지는 일을 줄인다. `context: fork`는 이전 대화의 context가 새어 들어오는 것을 막는다. `allowed-tools`는 skill을 안전한 파일 쓰기 작업으로 제한해 파괴적인 동작을 막는다.

## CCAR-F-paullarionov-0040

**EN** Your codebase contains areas with different coding conventions: React components use functional style with hooks, API handlers use async/await with specific error handling, and database models follow the repository pattern. Test files are distributed across the codebase next to the code under test (e.g., `Button.test.tsx` next to `Button.tsx`), and you want all tests to follow the same conventions regardless of location.

What is the most supported way to ensure Claude automatically applies the correct conventions when generating code?

**기존** 코드베이스에는 코딩 컨벤션이 서로 다른 영역이 있다. React 컴포넌트는 hooks를 사용하는 함수형 스타일을, API 핸들러는 특정 오류 처리와 함께 async/await를, 데이터베이스 모델은 repository 패턴을 따른다. 테스트 파일은 테스트 대상 코드 옆에 코드베이스 전반에 분산되어 있으며(예: `Button.tsx` 옆의 `Button.test.tsx`), 위치와 관계없이 모든 테스트가 동일한 컨벤션을 따르기를 원한다.

Claude가 코드를 생성할 때 올바른 컨벤션을 자동으로 적용하도록 보장하는 가장 널리 지원되는 방법은 무엇인가?

**신규** 코드베이스에는 영역마다 코딩 규칙이 다르다. React 컴포넌트는 hook을 쓰는 함수형 스타일이고, API handler는 특정 error handling과 함께 async/await를 쓰고, database model은 repository 패턴을 따른다. 테스트 파일은 코드베이스 곳곳에서 테스트 대상 코드 옆에 놓여 있고(예: `Button.tsx` 옆의 `Button.test.tsx`), 위치와 상관없이 모든 테스트가 같은 규칙을 따르게 하고 싶다.

Claude가 코드를 생성할 때 알맞은 규칙을 자동으로 적용하게 하는, 가장 잘 지원되는 방법은 무엇인가?

- A. 기존: 모든 컨벤션을 영역별 제목 아래 루트 CLAUDE.md에 넣고, Claude가 어느 섹션이 적용되는지 추론하도록 맡긴다.
  - 신규: 모든 규칙을 루트 CLAUDE.md에 영역별 제목으로 정리해 넣고, 어느 섹션이 적용되는지는 Claude가 추론하게 맡긴다.
- B. 기존: 각 코드 유형별로 `.claude/skills/`에 skill을 만들고 각 SKILL.md에 컨벤션을 포함시킨다.
  - 신규: 코드 유형별로 `.claude/skills/`에 skill을 만들고, 각 SKILL.md에 규칙을 담는다.
- C. 기존: 각 하위 디렉터리에 해당 영역의 컨벤션을 담은 별도의 CLAUDE.md 파일을 둔다.
  - 신규: 각 하위 디렉터리에 해당 영역의 규칙을 담은 CLAUDE.md 파일을 따로 둔다.
- D. 기존: 파일 경로에 따라 조건부로 컨벤션을 적용하도록 glob 패턴을 지정하는 YAML frontmatter가 있는 규칙 파일을 `.claude/rules/` 아래에 만든다.
  - 신규: `.claude/rules/` 아래에 규칙 파일을 만들고, YAML frontmatter에 glob 패턴을 지정해 파일 경로에 따라 규칙이 조건부로 적용되게 한다.

**해설 EN** `.claude/rules/` files with YAML frontmatter and glob patterns (e.g., `**/*.test.tsx`, `src/api/**/*.ts`) enable deterministic, path-based convention application regardless of directory structure. This is the most supported approach for cross-cutting patterns like distributed test files.

**해설 기존** YAML frontmatter와 glob 패턴(예: `**/*.test.tsx`, `src/api/**/*.ts`)을 사용하는 `.claude/rules/` 파일은 디렉터리 구조와 관계없이 결정적인 경로 기반 컨벤션 적용을 가능하게 한다. 이는 분산된 테스트 파일 같은 횡단 패턴에 대해 가장 널리 지원되는 방식이다.

**해설 신규** YAML frontmatter와 glob 패턴(예: `**/*.test.tsx`, `src/api/**/*.ts`)을 쓰는 `.claude/rules/` 파일은 디렉터리 구조와 상관없이 경로를 기준으로 규칙을 항상 일정하게(예측 가능하게) 적용한다. 곳곳에 흩어진 테스트 파일처럼 여러 영역에 걸친 패턴에 가장 잘 지원되는 방법이다.

## CCAR-F-paullarionov-0041

**EN** You want to create a custom slash command `/review` that runs your team’s standard code review checklist. It should be available to every developer when they clone or update the repository.

Where should you create the command file?

**기존** 팀의 표준 코드 리뷰 체크리스트를 실행하는 커스텀 슬래시 명령 `/review`를 만들려고 한다. 이 명령은 모든 개발자가 저장소를 clone하거나 업데이트할 때 사용할 수 있어야 한다.

명령 파일은 어디에 만들어야 하는가?

**신규** 팀의 표준 코드 리뷰 체크리스트를 실행하는 custom slash command `/review`를 만들려고 한다. 모든 개발자가 저장소를 clone하거나 업데이트하면 바로 쓸 수 있어야 한다.

명령 파일을 어디에 만들어야 하는가?

- A. 기존: 각 개발자의 홈 디렉터리에 있는 `~/.claude/commands/`.
  - 신규: 각 개발자의 홈 디렉터리에 있는 `~/.claude/commands/`.
- B. 기존: 프로젝트 저장소의 `.claude/commands/`.
  - 신규: 프로젝트 저장소의 `.claude/commands/`.
- C. 기존: 명령 배열 형태로 `.claude/config.json`.
  - 신규: `.claude/config.json`에 명령 배열로 정의한다.
- D. 기존: 루트 프로젝트 CLAUDE.md.
  - 신규: 루트 프로젝트 CLAUDE.md.

**해설 EN** Putting custom slash commands under `.claude/commands/` inside the project repository ensures they are version-controlled and automatically available to every developer who clones or updates the repo. This is the intended location for project-level custom commands in Claude Code.

**해설 기존** 커스텀 슬래시 명령을 프로젝트 저장소 내부의 `.claude/commands/` 아래에 두면 버전 관리되며, 저장소를 clone하거나 업데이트하는 모든 개발자가 자동으로 사용할 수 있다. 이는 Claude Code에서 프로젝트 수준 커스텀 명령을 위해 의도된 위치이다.

**해설 신규** custom slash command를 프로젝트 저장소 안의 `.claude/commands/`에 두면 버전 관리가 되고, 저장소를 clone하거나 업데이트한 모든 개발자가 자동으로 쓸 수 있다. Claude Code에서 프로젝트 수준 custom command를 두도록 정해진 위치다.

## CCAR-F-paullarionov-0042

**EN** Your team’s CLAUDE.md grew beyond 500 lines mixing TypeScript conventions, testing guidance, API patterns, and deployment procedures. Developers find it hard to locate and update the right sections.

What approach does Claude Code support to organize project-level instructions into focused topical modules?

**기존** 팀의 CLAUDE.md가 TypeScript 컨벤션, 테스트 지침, API 패턴, 배포 절차가 뒤섞인 채 500줄을 넘게 늘어났다. 개발자들은 올바른 섹션을 찾고 업데이트하기 어렵다고 느낀다.

프로젝트 수준 지침을 주제별로 집중된 모듈로 구성하기 위해 Claude Code가 지원하는 방식은 무엇인가?

**신규** 팀의 CLAUDE.md가 500줄을 넘게 커졌고 TypeScript 규칙, 테스트 가이드, API 패턴, 배포 절차가 뒤섞여 있다. 개발자들이 알맞은 부분을 찾아 고치기 어려워한다.

프로젝트 수준 지침을 주제별로 나눈 module로 정리하기 위해 Claude Code가 지원하는 방법은 무엇인가?

- A. 기존: 파일 패턴을 CLAUDE.md 내부의 특정 섹션에 매핑하는 `.claude/config.yaml` 파일을 정의한다.
  - 신규: 파일 패턴을 CLAUDE.md 안의 특정 섹션에 연결하는 `.claude/config.yaml` 매핑 파일을 정의한다.
- B. 기존: `.claude/rules/`에 각각 하나의 주제(예: `testing.md`, `api-conventions.md`)를 다루는 별도의 Markdown 파일을 만든다.
  - 신규: `.claude/rules/`에 주제 하나씩을 다루는 Markdown 파일(예: `testing.md`, `api-conventions.md`)을 따로 만든다.
- C. 기존: 지침을 관련 하위 디렉터리의 README.md 파일로 나누어, Claude가 이를 지침으로 자동 로드하게 한다.
  - 신규: 지침을 관련 하위 디렉터리의 README.md 파일로 나눈다. Claude가 이를 지침으로 자동 로드한다.
- D. 기존: 디렉터리 트리의 여러 수준에 CLAUDE.md라는 이름의 파일을 여러 개 만들고, 각각이 상위 지침을 덮어쓰게 한다.
  - 신규: 디렉터리 트리의 여러 수준에 CLAUDE.md라는 이름의 파일을 여러 개 만들고, 각각 상위 지침을 덮어쓰게 한다.

**해설 EN** Claude Code supports a `.claude/rules/` directory where you can create separate Markdown files for topical guidance (e.g., `testing.md`, `api-conventions.md`), allowing teams to organize large instruction sets into focused, maintainable modules.

**해설 기존** Claude Code는 주제별 지침(예: `testing.md`, `api-conventions.md`)을 담은 별도의 Markdown 파일을 만들 수 있는 `.claude/rules/` 디렉터리를 지원하며, 이를 통해 팀은 대규모 지침 집합을 집중되고 유지보수하기 쉬운 모듈로 구성할 수 있다.

**해설 신규** Claude Code는 `.claude/rules/` 디렉터리를 지원한다. 여기에 주제별 가이드를 Markdown 파일로 따로 만들 수 있다(예: `testing.md`, `api-conventions.md`). 덕분에 팀은 방대한 지침을 주제별로 나눠 관리하기 쉬운 module로 정리할 수 있다.

## CCAR-F-paullarionov-0043

**EN** You create a custom skill `/explore-alternatives` that your team uses to brainstorm and evaluate implementation approaches before choosing one. Developers report that after running the skill, subsequent Claude responses are influenced by the alternatives discussion—sometimes referencing rejected approaches or retaining exploration context that interferes with actual implementation.

How should you most effectively configure this skill?

**기존** 팀이 구현 접근 방식을 선택하기 전에 브레인스토밍하고 평가하는 데 사용하는 커스텀 skill `/explore-alternatives`를 만든다. 개발자들은 이 skill을 실행한 후 이어지는 Claude의 응답이 대안 논의의 영향을 받는다고 보고한다. 이미 기각된 접근 방식을 언급하거나, 실제 구현을 방해하는 탐색 컨텍스트를 유지하기도 한다.

이 skill을 가장 효과적으로 구성하려면 어떻게 해야 하는가?

**신규** 팀이 구현 방식을 고르기 전에 여러 방안을 브레인스토밍하고 평가하는 데 쓰는 custom skill `/explore-alternatives`를 만들었다. 개발자들은 이 skill을 실행한 뒤의 Claude 응답이 대안 논의에 영향을 받는다고 보고한다. 이미 기각한 방식을 언급하거나, 탐색 때 쓴 context가 남아 실제 구현을 방해한다는 것이다.

이 skill을 가장 효과적으로 설정하는 방법은 무엇인가?

- A. 기존: skill에서 `!` 접두사를 사용하여 탐색 로직을 bash 하위 프로세스로 실행한다.
  - 신규: skill에서 `!` 접두사를 사용해 탐색 로직을 bash subprocess로 실행한다.
- B. 기존: skill frontmatter에 `context: fork`를 추가한다.
  - 신규: skill의 frontmatter에 `context: fork`를 추가한다.
- C. 기존: 탐색 컨텍스트를 폐기해야 하는 경계를 표시하기 위해 `/explore-start`와 `/explore-end` 두 개의 skill로 분리한다.
  - 신규: skill을 `/explore-start`와 `/explore-end`로 나눠, 탐색 context를 버려야 하는 경계를 표시한다.
- D. 기존: `.claude/skills/` 대신 `~/.claude/skills/`에 skill을 만든다.
  - 신규: skill을 `.claude/skills/`가 아니라 `~/.claude/skills/`에 만든다.

**해설 EN** `context: fork` runs the skill in an isolated subagent context so exploration discussions do not pollute the main conversation history. This prevents rejected approaches and brainstorming context from influencing subsequent implementation work.

**해설 기존** `context: fork`는 skill을 격리된 subagent 컨텍스트에서 실행하므로 탐색 논의가 메인 대화 기록을 오염시키지 않는다. 이를 통해 기각된 접근 방식과 브레인스토밍 컨텍스트가 이후 구현 작업에 영향을 미치는 것을 방지한다.

**해설 신규** `context: fork`는 skill을 격리된 subagent context에서 실행하므로, 탐색 논의가 메인 대화 기록을 오염시키지 않는다. 그 덕분에 기각된 방식이나 브레인스토밍 context가 이후의 구현 작업에 영향을 주지 않는다.

## CCAR-F-paullarionov-0044

**EN** Your team wants to add a GitHub MCP server for searching PRs and checking CI status via Claude Code. Each of six developers has their own personal GitHub access token. You want consistent tooling across the team without committing credentials to version control.

Which configuration approach is most effective?

**기존** 팀은 Claude Code로 PR을 검색하고 CI 상태를 확인하기 위해 GitHub MCP 서버를 추가하려고 한다. 여섯 명의 개발자는 각자 개인 GitHub 액세스 토큰을 가지고 있다. 자격 증명을 버전 관리에 커밋하지 않으면서 팀 전체에서 일관된 도구를 사용하려고 한다.

가장 효과적인 구성 방식은 무엇인가?

**신규** 팀에서 Claude Code로 PR을 검색하고 CI 상태를 확인할 수 있도록 GitHub MCP server를 추가하려 한다. 개발자 6명은 각자 개인 GitHub access token을 가지고 있다. 팀 전체가 같은 도구 구성을 쓰되, credential은 버전 관리에 커밋하고 싶지 않다.

가장 효과적인 구성 방식은 무엇인가?

- A. 기존: 각 개발자가 `claude mcp add --scope user`를 통해 user 범위로 서버를 추가한다.
  - 신규: 각 개발자가 `claude mcp add --scope user`로 user scope에 server를 추가한다.
- B. 기존: `.env` 파일에서 토큰을 읽고 GitHub API 호출을 프록시하는 MCP 서버 래퍼를 만든 다음, 해당 래퍼를 프로젝트 `.mcp.json`에 추가한다.
  - 신규: `.env` 파일에서 token을 읽어 GitHub API 호출을 대신 전달하는 MCP server wrapper를 만들고, 이 wrapper를 프로젝트 `.mcp.json`에 추가한다.
- C. 기존: 인증을 위해 환경 변수 치환(`${GITHUB_TOKEN}`)을 사용하여 서버를 프로젝트 `.mcp.json`에 추가하고, 필요한 환경 변수를 프로젝트 README에 문서화한다.
  - 신규: 프로젝트 `.mcp.json`에 server를 추가하되 인증에는 환경 변수 치환(`${GITHUB_TOKEN}`)을 쓰고, 필요한 환경 변수를 프로젝트 README에 문서화한다.
- D. 기존: 프로젝트 범위에서 placeholder 토큰으로 서버를 구성한 다음, 개발자들에게 로컬 설정에서 이를 덮어쓰라고 안내한다.
  - 신규: project scope에 placeholder token으로 server를 설정하고, 개발자에게 로컬 설정에서 이 값을 덮어쓰라고 안내한다.

**해설 EN** A project `.mcp.json` with environment variable substitution is idiomatic: it provides a single version-controlled source of truth for MCP configuration while letting each developer supply credentials via environment variables. Documenting the variable makes onboarding easy without committing secrets.

**해설 기존** 환경 변수 치환을 사용하는 프로젝트 `.mcp.json`은 관용적인 방식이다. MCP 구성에 대해 버전 관리되는 단일 기준 출처를 제공하면서도, 각 개발자가 환경 변수를 통해 자격 증명을 제공하도록 한다. 변수를 문서화하면 비밀 정보를 커밋하지 않고도 온보딩이 쉬워진다.

**해설 신규** 프로젝트 `.mcp.json`에 환경 변수 치환을 쓰는 방식이 관례적인 방법이다. MCP 설정은 버전 관리되는 단일 기준으로 유지하고, credential은 개발자마다 환경 변수로 따로 제공한다. 필요한 변수를 문서화해 두면 비밀 값을 커밋하지 않고도 새 팀원이 쉽게 설정할 수 있다.

## CCAR-F-paullarionov-0045

**EN** You’re adding error-handling wrappers around external API calls across a 120-file codebase. The work has three phases: (1) discover all call sites and patterns, (2) collaboratively design the error-handling approach, and (3) implement wrappers consistently. In Phase 1, Claude generates large output listing hundreds of call sites with context, quickly filling the context window before discovery finishes.

Which approach is most effective to complete the task while maintaining implementation consistency?

**기존** 120개 파일로 이루어진 코드베이스 전반에서 외부 API 호출 주위에 오류 처리 래퍼를 추가하고 있다. 작업은 세 단계로 이루어진다. (1) 모든 호출 지점과 패턴을 찾고, (2) 오류 처리 접근 방식을 협업하여 설계하며, (3) 래퍼를 일관되게 구현한다. 1단계에서 Claude는 컨텍스트와 함께 수백 개의 호출 지점을 나열하는 방대한 출력을 생성하여, 탐색이 끝나기 전에 컨텍스트 윈도우가 빠르게 가득 찬다.

구현의 일관성을 유지하면서 작업을 완료하는 데 가장 효과적인 접근 방식은 무엇인가?

**신규** 파일 120개로 이루어진 코드베이스에서 외부 API 호출마다 error-handling wrapper를 씌우는 작업을 하고 있다. 작업은 세 단계다. (1) 모든 호출 지점과 패턴을 찾고, (2) error-handling 방식을 함께 설계하고, (3) wrapper를 일관되게 구현한다. 1단계에서 Claude가 호출 지점 수백 개를 문맥과 함께 나열하는 긴 출력을 내놓는 바람에, 탐색이 끝나기도 전에 context window가 금방 찬다.

구현의 일관성을 지키면서 작업을 끝내는 데 가장 효과적인 방법은 무엇인가?

- A. 기존: 1단계에 Explore subagent를 사용하여 장황한 탐색 출력을 격리하고 요약을 반환하게 한 다음, 2~3단계는 메인 대화에서 계속 진행한다.
  - 신규: 1단계에는 Explore subagent를 써서 길고 장황한 탐색 출력을 격리하고 요약만 받은 뒤, 2~3단계는 메인 대화에서 이어간다.
- B. 기존: 모든 단계를 메인 대화에서 수행하고, 파일을 진행하면서 주기적으로 `/compact`를 사용하여 컨텍스트 사용량을 줄인다.
  - 신규: 모든 단계를 메인 대화에서 진행하되, 파일을 처리하는 중간중간 `/compact`로 context 사용량을 줄인다.
- C. 기존: `--continue`와 함께 headless 모드로 전환하고, 연속성을 유지하기 위해 배치 호출 사이에 명시적인 컨텍스트 요약을 전달한다.
  - 신규: headless mode에서 `--continue`를 쓰고, batch 호출 사이에 명시적인 context 요약을 넘겨 연속성을 유지한다.
- D. 기존: 오류 처리 패턴을 CLAUDE.md에 정의한 다음, 일관성을 위해 공유 메모리 파일에 의존하면서 여러 세션에 걸쳐 파일을 배치로 처리한다.
  - 신규: error-handling 패턴을 CLAUDE.md에 정의하고, 여러 세션에 걸쳐 파일을 batch로 처리하면서 공유 memory 파일로 일관성을 유지한다.

**해설 EN** An Explore subagent isolates the verbose discovery output in a separate context and returns only a concise summary to the main conversation. This preserves the main context window for the collaborative design and consistent implementation phases where retained context is most valuable.

**해설 기존** Explore subagent는 장황한 탐색 출력을 별도의 컨텍스트에 격리하고 간결한 요약만 메인 대화로 반환한다. 이렇게 하면 유지된 컨텍스트가 가장 가치 있는 협업 설계 및 일관된 구현 단계를 위해 메인 컨텍스트 윈도우를 보존할 수 있다.

**해설 신규** Explore subagent는 길고 장황한 탐색 출력을 별도 context에 가두고, 메인 대화에는 간결한 요약만 돌려준다. 그 덕분에 메인 context window는 함께 설계하고 일관되게 구현하는 단계를 위해 남겨 둘 수 있다. 이 단계들에서는 유지된 context가 가장 값지다.

## CCAR-F-paullarionov-0046

**EN** While testing, you notice the agent often calls `get_customer` when users ask about order status, even though `lookup_order` would be more appropriate. What should you check first to address this problem?

What should you check first?

**기존** 테스트하는 동안, 사용자가 주문 상태를 물을 때 `lookup_order`가 더 적절한데도 agent가 `get_customer`를 자주 호출하는 것을 발견한다. 이 문제를 해결하기 위해 가장 먼저 무엇을 확인해야 하는가?

가장 먼저 무엇을 확인해야 하는가?

**신규** 테스트하는 중에 보니, 사용자가 주문 상태를 물을 때 `lookup_order`가 더 적절한데도 agent가 `get_customer`를 자주 호출한다. 이 문제를 해결하려면 가장 먼저 무엇을 확인해야 하는가?

- A. 기존: 주문 관련 요청을 감지하여 `lookup_order`로 직접 라우팅하는 전처리 classifier를 구현한다.
  - 신규: 주문 관련 요청을 감지해 곧바로 `lookup_order`로 보내는 전처리 classifier를 구현한다.
- B. 기존: 선택을 단순화하기 위해 agent가 사용할 수 있는 도구의 수를 줄인다.
  - 신규: 선택을 단순하게 만들기 위해 agent가 쓸 수 있는 도구 수를 줄인다.
- C. 기존: 도구 선택을 개선하기 위해 가능한 모든 주문 요청 패턴을 다루는 few-shot 예시를 시스템 프롬프트에 추가한다.
  - 신규: 도구 선택이 나아지도록 가능한 모든 주문 요청 패턴을 다루는 few-shot 예시를 system prompt에 추가한다.
- D. 기존: 도구 설명이 각 도구의 목적을 명확하게 구분하는지 확인한다.
  - 신규: 도구 description이 각 도구의 용도를 분명하게 구분하고 있는지 확인한다.

**해설 EN** Tool descriptions are the primary input the model uses to decide which tool to call. When an agent consistently picks the wrong tool, the first diagnostic step is to verify that tool descriptions clearly separate each tool’s purpose and usage boundaries.

**해설 기존** 도구 설명은 모델이 어떤 도구를 호출할지 결정하는 데 사용하는 주된 입력이다. agent가 일관되게 잘못된 도구를 선택할 때, 첫 번째 진단 단계는 도구 설명이 각 도구의 목적과 사용 경계를 명확하게 구분하는지 확인하는 것이다.

**해설 신규** 모델은 도구 description을 가장 중요한 단서로 삼아 어떤 도구를 호출할지 정한다. agent가 계속 엉뚱한 도구를 고른다면, 가장 먼저 도구 description이 각 도구의 용도와 사용 범위를 분명하게 구분하는지 확인해야 한다.

## CCAR-F-paullarionov-0047

**EN** Your agent handles single-issue requests with 94% accuracy (e.g., “I need a refund for order #1234”). But when customers include multiple issues in one message (e.g., “I need a refund for order #1234 and also want to update the shipping address for order #5678”), tool selection accuracy drops to 58%. The agent usually solves only one issue or mixes parameters across requests. What approach most effectively improves reliability for multi-issue requests?

What approach is most effective?

**기존** agent는 단일 이슈 요청(예: "주문 #1234에 대해 환불이 필요합니다")을 94%의 정확도로 처리한다. 그러나 고객이 한 메시지에 여러 이슈를 포함하면(예: "주문 #1234에 대해 환불이 필요하고, 주문 #5678의 배송 주소도 변경하고 싶습니다") 도구 선택 정확도가 58%로 떨어진다. agent는 보통 한 가지 이슈만 해결하거나 요청 간에 매개변수를 뒤섞는다. 여러 이슈가 포함된 요청에 대한 신뢰성을 가장 효과적으로 개선하는 접근 방식은 무엇인가?

어떤 접근 방식이 가장 효과적인가?

**신규** 이슈가 하나인 요청(예: “주문 #1234 환불해 주세요”)은 agent가 94% 정확도로 처리한다. 그런데 고객이 한 메시지에 이슈를 여러 개 담으면(예: “주문 #1234 환불해 주시고, 주문 #5678의 배송지도 바꾸고 싶어요”) 도구 선택 정확도가 58%로 떨어진다. agent는 대개 이슈 하나만 해결하거나, 요청 간에 parameter를 뒤섞는다. 이슈가 여러 개인 요청의 신뢰도를 가장 효과적으로 높이는 방법은 무엇인가?

- A. 기존: 별도의 모델 호출을 사용하여 여러 이슈가 담긴 메시지를 별개의 요청으로 분해하고, 각각을 독립적으로 처리한 뒤 결과를 병합하는 전처리 계층을 구현한다.
  - 신규: 별도의 모델 호출로 여러 이슈가 섞인 메시지를 개별 요청으로 나누고, 각각 독립적으로 처리한 뒤 결과를 합치는 전처리 계층을 구현한다.
- B. 기존: 관련된 도구들을 더 적은 수의 범용 도구로 결합한다.
  - 신규: 관련 있는 도구들을 합쳐 더 적은 수의 범용 도구로 만든다.
- C. 기존: 여러 이슈가 포함된 요청에 대한 올바른 추론과 도구 순서를 보여 주는 few-shot 예시를 프롬프트에 추가한다.
  - 신규: 이슈가 여러 개인 요청에서 올바른 추론과 도구 호출 순서를 보여 주는 few-shot 예시를 prompt에 추가한다.
- D. 기존: 불완전한 답변을 감지하고 놓친 이슈를 해결하도록 agent에 자동으로 다시 프롬프트하는 응답 검증을 구현한다.
  - 신규: 불완전한 응답을 감지하는 응답 검증을 구현하고, 놓친 이슈를 처리하도록 agent에게 자동으로 다시 prompt한다.

**해설 EN** Few-shot examples that demonstrate correct reasoning and tool sequencing for multi-issue requests are most effective because the agent already performs well on single issues—what it needs is guidance on the pattern for decomposing and routing multiple issues and keeping parameters separated.

**해설 기존** 여러 이슈가 포함된 요청에 대한 올바른 추론과 도구 순서를 보여 주는 few-shot 예시가 가장 효과적이다. agent는 이미 단일 이슈를 잘 처리하므로, 필요한 것은 여러 이슈를 분해하고 라우팅하며 매개변수를 분리해 유지하는 패턴에 대한 안내이기 때문이다.

**해설 신규** 이슈가 여러 개인 요청에서 올바른 추론과 도구 호출 순서를 보여 주는 few-shot 예시가 가장 효과적이다. agent는 이슈가 하나일 때는 이미 잘 처리하므로, 필요한 것은 여러 이슈를 나누어 각각 알맞은 도구로 보내고 parameter를 섞지 않는 패턴에 대한 안내다.

## CCAR-F-paullarionov-0048

**EN** Production logs show that for simple requests like “refund for order #1234,” your agent resolves the issue in 3–4 tool calls with 91% success. But for complex requests like “I was billed twice, my discount didn’t apply, and I want to cancel,” the agent averages 12+ tool calls with only 54% success—often investigating issues sequentially and fetching redundant customer data for each. What change most effectively improves handling of complex requests?

What change is most effective?

**기존** 프로덕션 로그에 따르면 "주문 #1234 환불" 같은 단순한 요청의 경우 agent는 3~4번의 도구 호출로 91%의 성공률로 문제를 해결한다. 그러나 "두 번 청구되었고, 할인이 적용되지 않았으며, 취소하고 싶습니다" 같은 복잡한 요청의 경우 agent는 평균 12회 이상의 도구 호출에 54%의 성공률에 그치며, 이슈를 순차적으로 조사하고 각각에 대해 중복된 고객 데이터를 가져오는 경우가 많다. 복잡한 요청 처리를 가장 효과적으로 개선하는 변경은 무엇인가?

어떤 변경이 가장 효과적인가?

**신규** production 로그를 보면, “주문 #1234 환불”처럼 단순한 요청은 agent가 도구를 3~4번 호출해 91% 성공률로 해결한다. 반면 “요금이 두 번 청구됐고, 할인도 적용이 안 됐고, 취소도 하고 싶어요” 같은 복잡한 요청에서는 평균 12번 넘게 도구를 호출하면서 성공률은 54%에 그친다. 문제를 하나씩 차례로 조사하고, 그때마다 같은 고객 데이터를 중복해서 가져오는 경우가 많다. 복잡한 요청의 처리를 가장 효과적으로 개선하는 변경은 무엇인가?

- A. 기존: 단계 사이에 명시적인 검증 체크포인트를 추가하여, agent가 다음 이슈로 넘어가기 전에 각 이슈를 해결한 뒤 진행 상황을 기록하도록 요구한다.
  - 신규: 단계 사이에 명시적인 검증 checkpoint를 두고, 이슈 하나를 해결할 때마다 진행 상황을 기록한 뒤에 다음 이슈로 넘어가게 한다.
- B. 기존: `get_customer`, `lookup_order`, 청구 관련 도구를 하나의 `investigate_issue` 도구로 결합하여 도구의 수를 줄인다.
  - 신규: `get_customer`, `lookup_order`, 청구 관련 도구를 `investigate_issue` 하나로 합쳐 도구 수를 줄인다.
- C. 기존: 요청을 별개의 이슈로 분해한 다음, 최종 해결책을 종합하기 전에 공유된 고객 컨텍스트를 사용하여 각 이슈를 병렬로 조사한다.
  - 신규: 요청을 개별 이슈로 나눈 뒤, 공유한 고객 context를 활용해 각 이슈를 병렬로 조사하고 마지막에 최종 해결안으로 종합한다.
- D. 기존: 다양한 복합 청구 시나리오에 대한 이상적인 도구 호출 순서를 보여 주는 few-shot 예시를 시스템 프롬프트에 추가한다.
  - 신규: 여러 측면이 얽힌 다양한 청구 시나리오에서 이상적인 도구 호출 순서를 보여 주는 few-shot 예시를 system prompt에 추가한다.

**해설 EN** Decomposing into separate issues and investigating in parallel with shared customer context fixes both key problems: it eliminates redundant data retrieval by reusing shared context across issues and reduces total tool-call loops by parallelizing investigation before synthesizing a single resolution.

**해설 기존** 별개의 이슈로 분해하고 공유된 고객 컨텍스트로 병렬 조사하면 두 가지 핵심 문제가 모두 해결된다. 이슈 간에 공유된 컨텍스트를 재사용하여 중복된 데이터 조회를 없애고, 단일 해결책을 종합하기 전에 조사를 병렬화하여 전체 도구 호출 루프를 줄인다.

**해설 신규** 요청을 개별 이슈로 나누고 공유한 고객 context로 병렬 조사하면 두 가지 핵심 문제가 함께 풀린다. 이슈마다 같은 context를 재사용하므로 중복 데이터 조회가 사라지고, 조사를 병렬로 진행한 뒤 해결안 하나로 종합하므로 도구 호출 loop의 총 횟수도 줄어든다.

## CCAR-F-paullarionov-0049

**EN** Your agent achieves 55% first-contact resolution, well below the 80% target. Logs show it escalates simple cases (standard replacements for damaged goods with photo proof) while trying to handle complex situations requiring policy exceptions autonomously. What is the most effective way to improve escalation calibration?

What is the most effective way to improve escalation calibration?

**기존** agent의 first-contact resolution이 55%로, 목표인 80%에 크게 못 미친다. 로그를 보면 agent는 단순한 사례(사진 증빙이 있는 파손 상품의 표준 교환)는 escalate하면서, 정책 예외가 필요한 복잡한 상황은 자율적으로 처리하려고 한다. escalation 보정을 개선하는 가장 효과적인 방법은 무엇인가?

escalation 보정을 개선하는 가장 효과적인 방법은 무엇인가?

**신규** agent의 첫 응대 해결률이 55%로, 목표인 80%에 크게 못 미친다. 로그를 보면 단순한 사례(사진 증빙이 있는 파손 상품 표준 교환)는 escalation하면서, 정책 예외가 필요한 복잡한 상황은 스스로 처리하려 한다. escalation 기준을 바로잡는 가장 효과적인 방법은 무엇인가?

- A. 기존: agent가 각 응답 전에 1~10 척도로 신뢰도를 스스로 평가하게 하고, 신뢰도가 임계값 아래로 떨어지면 자동으로 사람에게 라우팅한다.
  - 신규: 응답하기 전에 agent가 확신도를 1~10점으로 스스로 매기게 하고, 확신도가 임계값 아래로 떨어지면 자동으로 사람에게 넘긴다.
- B. 기존: 메인 agent가 처리를 시작하기 전에 어떤 요청이 escalation이 필요한지 예측하도록 과거 티켓으로 학습된 별도의 classifier 모델을 배포한다.
  - 신규: 과거 티켓으로 학습시킨 별도의 classifier 모델을 배포해, 메인 agent가 처리를 시작하기 전에 어떤 요청이 escalation 대상인지 예측한다.
- C. 기존: 언제 escalate하고 언제 자율적으로 해결해야 하는지 보여 주는 few-shot 예시와 함께 명시적인 escalation 기준을 시스템 프롬프트에 추가한다.
  - 신규: system prompt에 명시적인 escalation 기준을 추가하고, escalation할 때와 스스로 해결할 때를 보여 주는 few-shot 예시를 함께 넣는다.
- D. 기존: 감정 분석을 구현하여 고객의 불만 수준을 판단하고 부정적 감정 임계값을 넘으면 자동으로 escalate한다.
  - 신규: 감정 분석으로 고객의 불만 수준을 판단하고, 부정적 감정이 임계값을 넘으면 자동으로 escalation한다.

**해설 EN** Explicit escalation criteria with few-shot examples directly address the root cause—unclear decision boundaries between simple and complex cases. It’s the most proportional, effective first intervention that teaches the agent when to escalate and when to resolve autonomously without extra infrastructure.

**해설 기존** few-shot 예시를 곁들인 명시적인 escalation 기준은 근본 원인, 즉 단순한 사례와 복잡한 사례 사이의 불분명한 판단 경계를 직접 해결한다. 추가 인프라 없이 agent에게 언제 escalate하고 언제 자율적으로 해결해야 하는지 가르치는, 가장 적절한 규모의 효과적인 첫 개입이다.

**해설 신규** 명시적인 escalation 기준과 few-shot 예시는 근본 원인인 단순 사례와 복잡 사례 사이의 불분명한 판단 경계를 직접 해결한다. 별도 인프라 없이도 agent에게 언제 escalation하고 언제 스스로 해결할지 가르치므로, 규모에 맞고 효과적인 첫 조치다.

## CCAR-F-paullarionov-0050

**EN** After calling `get_customer` and `lookup_order`, the agent has all available system data but still faces uncertainty. Which situation is the most justified trigger for calling `escalate_to_human`?

Which situation is most justified for escalation?

**기존** `get_customer`와 `lookup_order`를 호출한 후 agent는 사용 가능한 모든 시스템 데이터를 가지고 있지만 여전히 불확실성에 직면한다. `escalate_to_human`을 호출하는 가장 타당한 계기가 되는 상황은 무엇인가?

어떤 상황이 escalation의 가장 타당한 근거인가?

**신규** agent가 `get_customer`와 `lookup_order`를 호출해 시스템에서 얻을 수 있는 데이터를 모두 확보했는데도 여전히 판단이 불확실하다. 다음 중 `escalate_to_human`을 호출할 근거가 가장 충분한 상황은 무엇인가?

- A. 기존: 고객이 어제 발송되어 내일 도착하는 주문을 취소하려고 한다. 고객이 패키지를 받은 뒤 마음을 바꿀 수 있으므로 agent는 escalate해야 한다.
  - 신규: 고객이 어제 발송되어 내일 도착할 주문을 취소하려 한다. 고객이 물건을 받은 뒤 마음을 바꿀 수도 있으므로 agent는 escalation해야 한다.
- B. 기존: 고객이 주문을 받지 못했다고 주장하지만, 추적 정보에는 사흘 전 고객의 주소에 배송되어 서명까지 받은 것으로 나온다. 모순되는 증거를 제시하면 고객 관계에 해가 될 수 있으므로 agent는 escalate해야 한다.
  - 신규: 고객이 주문을 받지 못했다고 주장하는데, 배송 추적상 사흘 전에 고객 주소로 배달되어 수령 서명까지 된 것으로 나온다. 상반되는 증거를 제시하면 고객 관계에 해가 될 수 있으므로 agent는 escalation해야 한다.
- C. 기존: 고객이 경쟁사 가격 맞춤을 요청한다. 정책은 14일 이내에 자사 사이트에서 가격이 인하된 경우 가격 조정을 허용하지만 경쟁사 가격에 대해서는 아무 언급이 없다. agent는 정책 해석을 위해 escalate해야 한다.
  - 신규: 고객이 경쟁사 가격에 맞춰 달라고 요청한다. 회사 정책은 자사 사이트에서 14일 이내에 가격이 내려간 경우의 가격 조정만 허용하고, 경쟁사 가격에 대해서는 아무 언급이 없다. agent는 정책 해석을 위해 escalation해야 한다.
- D. 기존: 고객 메시지에 청구 질문과 제품 반품이 모두 들어 있다. 사람이 한 번의 상호작용에서 두 이슈를 조율할 수 있도록 agent는 escalate해야 한다.
  - 신규: 고객 메시지에 청구 문의와 상품 반품이 함께 들어 있다. 사람이 두 이슈를 한 번의 응대로 조율할 수 있도록 agent는 escalation해야 한다.

**해설 EN** This is a genuine policy gap: company rules cover price drops on your own site but do not address competitor price matching. The agent must not invent policy and should escalate for human judgment on how to interpret or extend existing rules.

**해설 기존** 이는 진정한 정책 공백이다. 회사 규칙은 자사 사이트의 가격 인하를 다루지만 경쟁사 가격 맞춤은 다루지 않는다. agent는 정책을 만들어 내서는 안 되며, 기존 규칙을 어떻게 해석하거나 확장할지에 대한 사람의 판단을 위해 escalate해야 한다.

**해설 신규** 이것은 실제 정책 공백이다. 회사 규정은 자사 사이트의 가격 인하만 다루고 경쟁사 가격 맞춤은 다루지 않는다. agent가 정책을 지어내서는 안 되며, 기존 규정을 어떻게 해석하거나 확장할지는 사람이 판단하도록 escalation해야 한다.

## CCAR-F-paullarionov-0051

**EN** Production logs show that in 12% of cases your agent skips `get_customer` and calls `lookup_order` directly using only the customer-provided name, sometimes leading to misidentified accounts and incorrect refunds. What change most effectively fixes this reliability problem?

What change is most effective?

**기존** 프로덕션 로그에 따르면 12%의 경우 agent가 `get_customer`를 건너뛰고 고객이 제공한 이름만으로 `lookup_order`를 직접 호출하여, 때때로 계정을 잘못 식별하고 잘못된 환불로 이어진다. 이 신뢰성 문제를 가장 효과적으로 해결하는 변경은 무엇인가?

어떤 변경이 가장 효과적인가?

**신규** production 로그를 보면 12%의 경우 agent가 `get_customer`를 건너뛰고, 고객이 알려 준 이름만으로 `lookup_order`를 곧바로 호출한다. 이 때문에 계정을 잘못 식별해 엉뚱한 환불이 나가기도 한다. 이 신뢰도 문제를 가장 효과적으로 바로잡는 변경은 무엇인가?

- A. 기존: 고객이 자발적으로 주문 세부 정보를 제공하더라도 agent가 항상 `get_customer`를 먼저 호출함을 보여 주는 few-shot 예시를 추가한다.
  - 신규: 고객이 먼저 주문 정보를 알려 주는 경우에도 agent가 항상 `get_customer`를 먼저 호출하는 모습을 보여 주는 few-shot 예시를 추가한다.
- B. 기존: 각 요청을 분석하여 해당 요청 유형에 적합한 도구의 일부만 활성화하는 라우팅 classifier를 구현한다.
  - 신규: 각 요청을 분석해 그 요청 유형에 맞는 도구 일부만 활성화하는 routing classifier를 구현한다.
- C. 기존: `get_customer`가 검증된 고객 식별자를 반환할 때까지 `lookup_order`와 `process_refund`를 차단하는 프로그래밍 방식의 전제 조건을 추가한다.
  - 신규: `get_customer`가 검증된 고객 식별자를 반환할 때까지 `lookup_order`와 `process_refund`를 막는 programmatic precondition을 추가한다.
- D. 기존: 주문 관련 작업 전에 `get_customer`를 통한 고객 검증이 필수임을 명시하도록 시스템 프롬프트를 강화한다.
  - 신규: 주문 관련 작업을 하기 전에 `get_customer`로 고객을 확인하는 것이 필수라고 system prompt에 더 강하게 명시한다.

**해설 EN** A programmatic precondition provides a deterministic guarantee that required sequencing is followed. It’s the most effective approach because it eliminates the possibility of skipping verification, regardless of LLM behavior.

**해설 기존** 프로그래밍 방식의 전제 조건은 필요한 순서가 지켜진다는 결정적인 보장을 제공한다. LLM의 동작과 관계없이 검증을 건너뛸 가능성을 없애므로 가장 효과적인 접근 방식이다.

**해설 신규** programmatic precondition은 필수 호출 순서가 지켜진다는 것을 결정적으로 보장한다. LLM이 어떻게 동작하든 검증을 건너뛸 가능성 자체가 사라지므로 가장 효과적이다.

## CCAR-F-paullarionov-0052

**EN** Production metrics show that when resolving complex billing disputes or multi-order returns, customer satisfaction scores are 15% lower than for simple cases—even when the resolution is technically correct. Root-cause analysis shows the agent provides accurate solutions but inconsistently explains rationale: sometimes omitting relevant policy details, sometimes missing timeline info or next steps. The specific context gaps vary case by case. You want to improve solution quality without adding human oversight. What approach is most effective?

What approach is most effective?

**기존** 프로덕션 지표에 따르면 복잡한 청구 분쟁이나 다중 주문 반품을 해결할 때 고객 만족도 점수가 해결 자체가 기술적으로 올바른 경우에도 단순한 사례보다 15% 낮다. 근본 원인 분석 결과 agent는 정확한 해결책을 제공하지만 근거 설명이 일관되지 않다. 관련 정책 세부 정보를 빠뜨리기도 하고, 일정 정보나 다음 단계를 빠뜨리기도 한다. 구체적인 컨텍스트 공백은 사례마다 다르다. 사람의 감독을 추가하지 않고 해결 품질을 개선하려고 한다. 어떤 접근 방식이 가장 효과적인가?

어떤 접근 방식이 가장 효과적인가?

**신규** production 지표를 보면 복잡한 청구 분쟁이나 여러 주문의 반품을 처리할 때 고객 만족도가 단순 사례보다 15% 낮다. 해결 내용이 기술적으로 정확한 경우에도 마찬가지다. 근본 원인을 분석해 보니 agent는 정확한 해결책을 내놓지만 그 이유를 설명하는 방식이 일정하지 않다. 어떤 때는 관련 정책 내용을 빠뜨리고, 어떤 때는 일정이나 다음 절차를 빠뜨린다. 부족한 context도 사례마다 다르다. 사람의 감독을 추가하지 않고 해결 품질을 높이려 한다. 가장 효과적인 방법은 무엇인가?

- A. 기존: agent가 초안 응답의 완전성을 평가하는 자기 비평 단계를 추가한다. 이는 고객의 이슈를 해결하고, 관련 컨텍스트를 포함하며, 후속 질문을 예상하는지 확인하는 것이다.
  - 신규: agent가 초안 응답을 스스로 비평해 완전성을 평가하는 단계를 추가한다. 고객의 문제를 해결하는지, 관련 context를 담고 있는지, 후속 질문을 예상했는지 확인하게 한다.
- B. 기존: 종료하기 전에 agent가 "이 답변으로 문제가 완전히 해결되셨습니까?"라고 묻는 확인 단계를 추가하여, 필요한 경우 고객이 추가 정보를 요청할 수 있게 한다.
  - 신규: 응답을 마무리하기 전에 agent가 “문제가 모두 해결되셨나요?”라고 묻는 확인 단계를 추가해, 고객이 필요하면 추가 정보를 요청할 수 있게 한다.
- C. 기존: 정의된 복잡도 지표에 따라 라우팅하여 복잡한 사례에서는 모델을 Haiku에서 Sonnet으로 업그레이드한다.
  - 신규: 복잡도 기준을 정해 복잡한 사례를 라우팅하고, 이 사례에는 모델을 Haiku에서 Sonnet으로 올린다.
- D. 기존: 정책 컨텍스트, 일정, 다음 단계를 포함하는 방법을 보여 주면서 다섯 가지 일반적인 복잡한 사례 유형에 대한 완전한 설명을 담은 few-shot 예시를 시스템 프롬프트에 구현한다.
  - 신규: 흔한 복잡 사례 유형 5가지에 대해, 정책 맥락과 일정, 다음 절차를 어떻게 포함하는지 보여 주는 완전한 설명 예시를 few-shot으로 system prompt에 넣는다.

**해설 EN** A self-critique stage (the evaluator-optimizer pattern) directly addresses inconsistent explanation completeness by forcing the agent to assess its own draft against concrete criteria—such as policy context, timelines, and next steps—before presenting it. This catches case-specific gaps without human oversight.

**해설 기존** 자기 비평 단계(evaluator-optimizer 패턴)는 agent가 초안을 제시하기 전에 정책 컨텍스트, 일정, 다음 단계 같은 구체적인 기준에 비추어 스스로 평가하게 함으로써 일관되지 않은 설명의 완전성 문제를 직접 해결한다. 이는 사람의 감독 없이 사례별 공백을 잡아낸다.

**해설 신규** 자기 비평 단계(evaluator-optimizer 패턴)는 설명의 완전성이 들쭉날쭉한 문제를 직접 해결한다. agent가 초안을 내놓기 전에 정책 맥락, 일정, 다음 절차 같은 구체적인 기준에 비추어 스스로 평가하게 하기 때문이다. 이렇게 하면 사람의 감독 없이도 사례마다 다른 빈틈을 잡아낼 수 있다.

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

## CCAR-F-paullarionov-0054

**EN** Production logs show a pattern: customers reference specific amounts (e.g., “the 15% discount I mentioned”), but the agent responds with incorrect values. Investigation shows these details were mentioned 20+ turns ago and condensed into vague summaries like “promotional pricing was discussed.” What fix is most effective?

What fix is most effective?

**기존** 프로덕션 로그에서 한 가지 패턴이 보인다. 고객이 구체적인 금액을 언급하지만(예: "제가 말씀드린 15% 할인") agent는 잘못된 값으로 응답한다. 조사 결과 이러한 세부 정보는 20턴 이상 전에 언급되었고 "프로모션 가격이 논의되었음" 같은 모호한 요약으로 압축되었다. 가장 효과적인 해결책은 무엇인가?

가장 효과적인 해결책은 무엇인가?

**신규** production 로그에서 한 가지 패턴이 보인다. 고객이 특정 금액을 언급하는데(예: “제가 말씀드린 15% 할인”), agent가 틀린 값으로 답한다. 조사해 보니 그 내용은 20턴 넘게 전에 언급된 것으로, “프로모션 가격이 논의됨” 같은 모호한 요약으로 줄어들어 있었다. 가장 효과적인 해결책은 무엇인가?

- A. 기존: 요약이 실행되기 전에 대화에 더 많은 여유가 생기도록 요약 임계값을 70%에서 85%로 높인다.
  - 신규: 요약이 시작되기 전에 대화가 더 오래 이어질 수 있도록 요약 임계값을 70%에서 85%로 높인다.
- B. 기존: 전체 대화 기록을 외부 저장소에 보관하고, agent가 "제가 말씀드린 대로" 같은 참조를 감지하면 검색을 수행하도록 구현한다.
  - 신규: 전체 대화 기록을 외부 저장소에 보관하고, agent가 “아까 말씀드린 것처럼” 같은 표현을 감지하면 검색해 오게 구현한다.
- C. 기존: 거래 관련 사실(금액, 날짜, 주문 번호)을 추출하여 요약된 기록 외부의 모든 프롬프트에 포함되는 지속적인 "case facts" 블록에 넣는다.
  - 신규: 거래와 관련된 사실(금액, 날짜, 주문 번호)을 추출해 “case facts” 블록에 담고, 요약된 기록과 별도로 매번 prompt에 포함한다.
- D. 기존: 모든 숫자, 백분율, 날짜, 고객이 밝힌 기대 사항을 그대로 보존하도록 요약 프롬프트를 명시적으로 수정한다.
  - 신규: 숫자, 백분율, 날짜, 고객이 밝힌 기대 사항을 원문 그대로 보존하도록 요약 prompt를 명시적으로 고친다.

**해설 EN** Summarization inherently loses precise details. Extracting transactional facts into a structured “case facts” block outside the summarized history preserves critical information so it’s reliably available in every prompt regardless of how many turns have been summarized.

**해설 기존** 요약은 본질적으로 정확한 세부 정보를 잃는다. 거래 관련 사실을 요약된 기록 외부의 구조화된 "case facts" 블록으로 추출하면, 몇 턴이 요약되었는지와 관계없이 중요한 정보가 모든 프롬프트에서 안정적으로 사용 가능하게 보존된다.

**해설 신규** 요약은 본질적으로 정확한 세부 정보를 잃는다. 거래 관련 사실을 요약된 기록 밖의 구조화된 “case facts” 블록으로 추출해 두면, 요약된 turn이 얼마나 많든 핵심 정보가 모든 prompt에서 안정적으로 유지된다.

## CCAR-F-paullarionov-0055

**EN** Your `get_customer` tool returns all matches when searching by name. Currently, when there are multiple results, Claude picks the customer with the most recent order, but production data shows this selects the wrong account 15% of the time for ambiguous matches. How should you address this?

How should you address this?

**기존** `get_customer` 도구는 이름으로 검색할 때 일치하는 모든 결과를 반환한다. 현재는 결과가 여러 개일 때 Claude가 가장 최근 주문이 있는 고객을 선택하지만, 프로덕션 데이터에 따르면 모호한 일치의 경우 15%는 잘못된 계정을 선택한다. 이 문제를 어떻게 해결해야 하는가?

이 문제를 어떻게 해결해야 하는가?

**신규** `get_customer` 도구는 이름으로 검색하면 일치하는 결과를 모두 반환한다. 지금은 결과가 여러 개일 때 Claude가 가장 최근에 주문한 고객을 고르는데, production 데이터를 보면 모호한 일치 건의 15%에서 엉뚱한 계정을 고른다. 이 문제를 어떻게 해결해야 하는가?

- A. 기존: 신뢰도가 85%를 넘으면 자율적으로 행동하고 임계값 아래이면 명확화를 요청하는 신뢰도 점수 시스템을 구현한다.
  - 신규: 확신도 점수 체계를 구현해, 확신도가 85%를 넘으면 자율적으로 진행하고 그 아래이면 확인 질문을 하게 한다.
- B. 기존: `get_customer`가 여러 일치 항목을 반환하면 고객별 작업을 수행하기 전에 추가 식별자(이메일, 전화번호 또는 주문 번호)를 요청하도록 Claude에 지시한다.
  - 신규: `get_customer`가 여러 건을 반환하면 고객별 작업을 하기 전에 추가 식별자(이메일, 전화번호, 주문 번호)를 요청하도록 Claude에게 지시한다.
- C. 기존: 모호성을 없애기 위해 순위 알고리즘에 따라 가장 가능성이 높은 단일 일치 항목만 반환하도록 `get_customer`를 수정한다.
  - 신규: `get_customer`를 수정해, 순위 알고리즘으로 가장 가능성이 높은 한 건만 반환하게 해서 모호성을 없앤다.
- D. 기존: 모호한 일치에 대한 올바른 추론과 도구 순서를 보여 주는 few-shot 예시를 프롬프트에 추가한다.
  - 신규: 모호한 일치 건에서 올바른 추론과 도구 호출 순서를 보여 주는 few-shot 예시를 prompt에 추가한다.

**해설 EN** Asking the user for an additional identifier is the most reliable way to resolve ambiguity because the user has definitive knowledge of their identity. One extra conversational turn is a small price to pay to eliminate a 15% error rate caused by choosing the wrong account.

**해설 기존** 사용자는 자신의 신원에 대해 확정적인 지식을 가지고 있으므로, 사용자에게 추가 식별자를 요청하는 것이 모호성을 해결하는 가장 신뢰할 수 있는 방법이다. 잘못된 계정을 선택하여 발생하는 15%의 오류율을 없애기 위해 대화 턴 하나를 더 쓰는 것은 작은 대가이다.

**해설 신규** 사용자에게 추가 식별자를 묻는 것이 모호성을 푸는 가장 확실한 방법이다. 자신이 누구인지는 사용자가 확실히 알고 있기 때문이다. 대화를 한 턴 더 하는 것은, 계정을 잘못 고르는 데서 생기는 15%의 오류율을 없애는 대가로 작다.

## CCAR-F-paullarionov-0056

**EN** Production logs show a consistent pattern: when customers include the word “account” in their message (e.g., “I want to check my account for an order I made yesterday”), the agent calls `get_customer` first 78% of the time. When customers phrase similar requests without “account” (e.g., “I want to check an order I made yesterday”), it calls `lookup_order` first 93% of the time. Tool descriptions are clear and unambiguous. What is the most likely root cause of this discrepancy?

What is the most likely root cause?

**기존** 프로덕션 로그에서 일관된 패턴이 보인다. 고객이 메시지에 "account"라는 단어를 포함하면(예: "어제 한 주문을 확인하려고 내 account를 보고 싶습니다") agent는 78%의 경우 `get_customer`를 먼저 호출한다. 고객이 "account" 없이 비슷한 요청을 표현하면(예: "어제 한 주문을 확인하고 싶습니다") 93%의 경우 `lookup_order`를 먼저 호출한다. 도구 설명은 명확하고 모호하지 않다. 이 불일치의 가장 가능성 높은 근본 원인은 무엇인가?

가장 가능성이 높은 근본 원인은 무엇인가?

**신규** production 로그에서 일관된 패턴이 보인다. 고객 메시지에 “계정”이라는 단어가 들어 있으면(예: “어제 주문한 건을 계정에서 확인하고 싶어요”) agent는 78%의 경우 `get_customer`를 먼저 호출한다. 비슷한 요청이라도 “계정” 없이 말하면(예: “어제 주문한 건을 확인하고 싶어요”) 93%의 경우 `lookup_order`를 먼저 호출한다. 도구 description은 분명하고 모호하지 않다. 이런 차이가 생기는 가장 가능성 높은 근본 원인은 무엇인가?

- A. 기존: 시스템 프롬프트에 "account" 같은 용어에 따라 동작을 유도하는 키워드 민감 지침이 있어 의도하지 않은 도구 선택 패턴을 만들고 있다.
  - 신규: system prompt에 “계정” 같은 단어에 반응해 동작을 유도하는 키워드 기반 지시가 들어 있어서, 의도하지 않은 도구 선택 패턴이 생긴다.
- B. 기존: 모델의 기본 학습이 "account" 용어와 고객 관련 작업 사이의 연관성을 만들어 도구 설명을 덮어쓴다.
  - 신규: 모델의 기본 학습 과정에서 “계정”이라는 용어와 고객 관련 작업이 연결되었고, 이 연결이 도구 description보다 우선한다.
- C. 기존: 모델은 여러 개념이 섞인 메시지에 대한 학습 데이터가 더 필요하며, account와 order 용어를 모두 포함하는 예시로 fine-tuning해야 한다.
  - 신규: 모델이 여러 개념이 섞인 메시지에 대한 학습 데이터가 더 필요하므로, 계정과 주문 용어가 함께 나오는 예시로 fine-tuning해야 한다.
- D. 기존: 이러한 키워드로 인한 혼동을 방지하려면 각 도구를 언제 사용하지 말아야 하는지를 명시하는 부정 예시가 도구 설명에 추가로 필요하다.
  - 신규: 이런 키워드 때문에 생기는 혼동을 막으려면, 각 도구를 언제 쓰지 말아야 하는지를 밝힌 부정 예시를 도구 description에 더 추가해야 한다.

**해설 EN** The systematic keyword-driven pattern (78% vs 93%) strongly indicates explicit routing logic in the system prompt reacting to the word “account” and steering the agent toward customer-related tools. Since tool descriptions are already clear, the discrepancy points to prompt-level instructions creating unintended behavioral steering.

**해설 기존** 체계적인 키워드 기반 패턴(78% 대 93%)은 시스템 프롬프트에 "account"라는 단어에 반응하여 agent를 고객 관련 도구로 유도하는 명시적인 라우팅 로직이 있음을 강하게 시사한다. 도구 설명이 이미 명확하므로, 이 불일치는 프롬프트 수준의 지침이 의도하지 않은 행동 유도를 만들고 있음을 가리킨다.

**해설 신규** 키워드에 따라 체계적으로 달라지는 패턴(78% 대 93%)은, system prompt에 “계정”이라는 단어에 반응해 agent를 고객 관련 도구로 유도하는 명시적 routing 로직이 있음을 강하게 시사한다. 도구 description은 이미 분명하므로, 이런 차이는 prompt 수준의 지시가 의도하지 않은 방향으로 동작을 이끌고 있다는 뜻이다.

## CCAR-F-paullarionov-0057

**EN** Production logs show the agent often calls `get_customer` when users ask about orders (e.g., “check my order #12345”) instead of calling `lookup_order`. Both tools have minimal descriptions (“Gets customer information” / “Gets order details”) and accept similar-looking identifier formats. What is the most effective first step to improve tool selection reliability?

What is the most effective first step?

**기존** 프로덕션 로그에 따르면 사용자가 주문에 대해 물을 때(예: "주문 #12345 확인해 주세요") agent가 `lookup_order` 대신 `get_customer`를 자주 호출한다. 두 도구 모두 설명이 최소한이며("고객 정보를 가져옴" / "주문 세부 정보를 가져옴") 비슷하게 생긴 식별자 형식을 받아들인다. 도구 선택 신뢰성을 개선하기 위한 가장 효과적인 첫 단계는 무엇인가?

가장 효과적인 첫 단계는 무엇인가?

**신규** production 로그를 보면 사용자가 주문을 물을 때(예: “내 주문 #12345 확인해 줘”) agent가 `lookup_order` 대신 `get_customer`를 호출하는 일이 잦다. 두 도구의 description은 “Gets customer information” / “Gets order details”처럼 아주 간단하고, 받는 식별자 형식도 비슷해 보인다. 도구 선택의 신뢰도를 높이기 위한 가장 효과적인 첫 단계는 무엇인가?

- A. 기존: 매 턴 전에 사용자 입력을 분석하여 감지된 키워드와 ID 패턴에 따라 올바른 도구를 미리 선택하는 라우팅 계층을 구현한다.
  - 신규: 매 턴 전에 사용자 입력을 분석해 감지한 키워드와 ID 패턴으로 올바른 도구를 미리 골라 주는 routing 계층을 구현한다.
- B. 기존: 어떤 식별자든 받아들이고 어느 백엔드를 조회할지 내부적으로 결정하는 단일 `lookup_entity`로 두 도구를 결합한다.
  - 신규: 두 도구를 어떤 식별자든 받아서 내부적으로 어느 backend를 조회할지 정하는 `lookup_entity` 하나로 합친다.
- C. 기존: 주문 관련 질의를 `lookup_order`로 라우팅하는 5~8개의 예시와 함께 올바른 도구 선택 패턴을 보여 주는 few-shot 예시를 시스템 프롬프트에 추가한다.
  - 신규: 올바른 도구 선택 패턴을 보여 주는 few-shot 예시를 system prompt에 추가하되, 주문 관련 질의를 `lookup_order`로 보내는 예시를 5~8개 넣는다.
- D. 기존: 각 도구의 설명을 확장하여 입력 형식, 예시 질의, 엣지 케이스, 그리고 유사한 도구와 비교해 언제 사용해야 하는지를 설명하는 경계를 포함한다.
  - 신규: 각 도구의 description을 확장해 입력 형식, 예시 질의, edge case, 그리고 비슷한 도구와 비교해 언제 써야 하는지 경계를 담는다.

**해설 EN** Expanding tool descriptions with input formats, example queries, edge cases, and clear boundaries directly fixes the root cause—minimal descriptions that don’t give the LLM enough information to distinguish similar tools. It’s a low-effort, high-impact first step that improves the primary mechanism the LLM uses for tool selection.

**해설 기존** 입력 형식, 예시 질의, 엣지 케이스, 명확한 경계로 도구 설명을 확장하면 근본 원인, 즉 LLM이 유사한 도구를 구별하기에 충분한 정보를 주지 못하는 최소한의 설명을 직접 해결한다. 이는 LLM이 도구 선택에 사용하는 주된 메커니즘을 개선하는, 노력이 적게 들고 효과가 큰 첫 단계이다.

**해설 신규** 입력 형식, 예시 질의, edge case, 분명한 경계를 담아 도구 description을 확장하면 근본 원인을 직접 해결한다. 지금 문제는 description이 너무 간단해서 LLM이 비슷한 도구를 구분할 정보가 부족하다는 것이다. 적은 노력으로 큰 효과를 내는 첫 단계이며, LLM이 도구를 고를 때 가장 중심으로 삼는 요소를 개선한다.

## CCAR-F-paullarionov-0058

**EN** You are implementing the agent loop for your support agent. After each Claude API call, you must decide whether to continue the loop (run requested tools and call Claude again) or stop (present the final answer to the customer). What determines this decision?

What determines this decision?

**기존** 지원 agent의 agent loop를 구현하고 있다. 각 Claude API 호출 후에는 루프를 계속할지(요청된 도구를 실행하고 Claude를 다시 호출) 중단할지(최종 답변을 고객에게 제시)를 결정해야 한다. 이 결정은 무엇이 좌우하는가?

이 결정은 무엇이 좌우하는가?

**신규** 고객 지원 agent의 agent loop를 구현하고 있다. Claude API를 호출할 때마다 loop를 계속할지(요청된 도구를 실행하고 Claude를 다시 호출), 멈출지(고객에게 최종 답변을 보여 줌) 정해야 한다. 이 결정은 무엇으로 판단하는가?

- A. 기존: Claude 응답의 `stop_reason` 필드를 확인하여, `tool_use`이면 계속하고 `end_turn`이면 중단한다.
  - 신규: Claude 응답의 `stop_reason` 필드를 확인해, `tool_use`이면 계속하고 `end_turn`이면 멈춘다.
- B. 기존: Claude의 텍스트에서 "완료했습니다" 또는 "더 도와드릴 일이 있을까요?" 같은 문구를 파싱한다. 자연어 신호가 작업 완료를 나타낸다.
  - 신규: Claude가 쓴 텍스트에서 “다 끝났습니다”나 “더 도와드릴 일이 있을까요?” 같은 문구를 파싱한다. 이런 자연어 신호가 작업 완료를 나타낸다.
- C. 기존: 최대 반복 횟수(예: 10회 호출)를 설정하고, Claude가 더 많은 작업이 필요하다고 나타내는지와 관계없이 도달하면 중단한다.
  - 신규: 최대 반복 횟수(예: 호출 10번)를 정해 두고, Claude가 더 할 일이 있다고 표시하든 말든 그 횟수에 이르면 멈춘다.
- D. 기존: 응답에 assistant 텍스트 콘텐츠가 포함되어 있는지 확인한다. Claude가 설명 텍스트를 생성했다면 루프를 종료해야 한다.
  - 신규: 응답에 assistant 텍스트 content가 있는지 확인해, Claude가 설명 텍스트를 생성했으면 loop를 끝낸다.

**해설 EN** `stop_reason` is Claude’s explicit structured signal for loop control: `tool_use` indicates Claude wants to run a tool and receive results back, while `end_turn` indicates Claude has completed its response and the loop should end.

**해설 기존** `stop_reason`은 루프 제어를 위한 Claude의 명시적이고 구조화된 신호이다. `tool_use`는 Claude가 도구를 실행하고 결과를 돌려받기를 원함을 나타내고, `end_turn`은 Claude가 응답을 완료했으며 루프를 종료해야 함을 나타낸다.

**해설 신규** `stop_reason`은 loop를 제어하라고 Claude가 명시적으로 알려 주는 구조화된 신호다. `tool_use`는 Claude가 도구를 실행하고 그 결과를 돌려받길 원한다는 뜻이고, `end_turn`은 Claude가 응답을 끝냈으니 loop를 종료해야 한다는 뜻이다.

## CCAR-F-paullarionov-0059

**EN** Production logs show the agent misinterprets outputs from your MCP tools: Unix timestamps from `get_customer`, ISO 8601 dates from `lookup_order`, and numeric status codes (1=pending, 2=shipped). Some tools are third-party MCP servers you cannot modify. Which approach to data format normalization is most maintainable?

Which approach is most maintainable?

**기존** 프로덕션 로그에 따르면 agent가 MCP 도구의 출력을 잘못 해석한다. `get_customer`는 Unix 타임스탬프를, `lookup_order`는 ISO 8601 날짜를, 숫자 상태 코드(1=pending, 2=shipped)를 반환한다. 일부 도구는 수정할 수 없는 서드파티 MCP 서버이다. 데이터 형식 정규화에 대해 가장 유지보수하기 쉬운 접근 방식은 무엇인가?

가장 유지보수하기 쉬운 접근 방식은 무엇인가?

**신규** production 로그를 보면 agent가 MCP 도구의 출력을 잘못 해석한다. `get_customer`는 Unix timestamp를, `lookup_order`는 ISO 8601 날짜를 반환하고, 상태는 숫자 코드(1=대기 중, 2=발송됨)로 나온다. 일부 도구는 직접 수정할 수 없는 third-party MCP server다. 데이터 형식을 정규화하는 방법 중 유지보수성이 가장 좋은 것은 무엇인가?

- A. 기존: PostToolUse hook을 사용하여 도구 출력을 가로채고, agent가 처리하기 전에 형식 변환을 적용한다.
  - 신규: PostToolUse hook으로 도구 출력을 가로채, agent가 처리하기 전에 형식 변환을 적용한다.
- B. 기존: 직접 제어하는 도구는 사람이 읽을 수 있는 형식을 반환하도록 수정하고, 서드파티 도구에는 래퍼를 만든다.
  - 신규: 직접 관리하는 도구는 사람이 읽기 쉬운 형식을 반환하도록 수정하고, third-party 도구에는 wrapper를 만든다.
- C. 기존: agent가 모든 데이터 조회 후에 값을 변환하기 위해 호출하는 `normalize_data` 도구를 만든다.
  - 신규: 데이터를 가져올 때마다 agent가 호출해 값을 변환하는 `normalize_data` 도구를 만든다.
- D. 기존: 각 도구의 데이터 규칙을 설명하는 상세한 형식 문서를 시스템 프롬프트에 추가한다.
  - 신규: 각 도구의 데이터 규칙을 설명하는 자세한 형식 문서를 system prompt에 추가한다.

**해설 EN** A PostToolUse hook provides a centralized, deterministic point to intercept and normalize all tool outputs—including third-party MCP server data—before the agent processes them. It’s more maintainable because transformations live in code and apply uniformly, rather than relying on LLM interpretation.

**해설 기존** PostToolUse hook은 서드파티 MCP 서버 데이터를 포함한 모든 도구 출력을 agent가 처리하기 전에 가로채 정규화할 수 있는 중앙 집중적이고 결정적인 지점을 제공한다. 변환이 코드에 있고 균일하게 적용되며 LLM의 해석에 의존하지 않으므로 유지보수하기가 더 쉽다.

**해설 신규** PostToolUse hook은 third-party MCP server의 데이터를 포함한 모든 도구 출력을, agent가 처리하기 전에 가로채 정규화하는 중앙 집중적이고 결정적인 지점이다. 변환이 코드에 있어 모든 출력에 일관되게 적용되고 LLM의 해석에 의존하지 않으므로 유지보수성이 더 좋다.

## CCAR-F-paullarionov-0060

**EN** Production logs show the agent sometimes chooses `get_customer` when `lookup_order` would be more appropriate, especially for ambiguous queries like “I need help with my recent purchase.” You decide to add few-shot examples to the system prompt to improve tool selection. Which approach most effectively addresses the problem?

Which approach is most effective?

**기존** 프로덕션 로그에 따르면 특히 "최근 구매한 것에 대해 도움이 필요합니다" 같은 모호한 질의에서, `lookup_order`가 더 적절한데도 agent가 가끔 `get_customer`를 선택한다. 도구 선택을 개선하기 위해 시스템 프롬프트에 few-shot 예시를 추가하기로 한다. 어떤 접근 방식이 문제를 가장 효과적으로 해결하는가?

어떤 접근 방식이 가장 효과적인가?

**신규** production 로그를 보면 `lookup_order`가 더 적절한 상황에서 agent가 `get_customer`를 고르는 일이 가끔 있다. 특히 “최근에 산 물건 관련해서 도움이 필요해요” 같은 모호한 질의에서 그렇다. 도구 선택을 개선하려고 system prompt에 few-shot 예시를 추가하기로 했다. 문제를 가장 효과적으로 해결하는 방법은 무엇인가?

- A. 기존: 모호한 경우를 다루는 명시적인 "사용할 때"와 "사용하지 않을 때" 안내를 각 도구 설명에 추가한다.
  - 신규: 각 도구 description에 모호한 경우까지 다루는 명시적인 “사용할 때”와 “사용하지 않을 때” 안내를 추가한다.
- B. 기존: 도구별로 묶은 예시를 추가한다. 모든 `get_customer` 시나리오를 함께 두고, 그다음 모든 `lookup_order` 시나리오를 둔다.
  - 신규: 예시를 도구별로 묶어서 추가한다. `get_customer` 시나리오를 모두 모은 다음, `lookup_order` 시나리오를 모두 모은다.
- C. 기존: 모호한 시나리오를 겨냥한 4~6개의 예시를 추가하고, 각각에 그럴듯한 대안보다 한 도구가 선택된 이유에 대한 근거를 붙인다.
  - 신규: 모호한 시나리오를 겨냥한 예시를 4~6개 추가하고, 각 예시에 그럴듯한 다른 도구가 아니라 이 도구를 고른 이유를 함께 적는다.
- D. 기존: 각 도구에 대해 일반적인 시나리오의 올바른 도구 선택을 보여 주는, 명확하고 모호하지 않은 요청의 예시 10~15개를 추가한다.
  - 신규: 도구마다 일반적인 시나리오에서 올바른 도구 선택을 보여 주는, 분명하고 모호하지 않은 요청 예시를 10~15개 추가한다.

**해설 EN** Targeting few-shot examples at the specific ambiguous scenarios where errors occur, with explicit rationale for why one tool is preferable to alternatives, teaches the model the comparative decision process needed for edge cases. This is more effective than generic examples or declarative rules.

**해설 기존** 오류가 발생하는 특정 모호한 시나리오를 겨냥하고 대안보다 한 도구가 더 나은 이유에 대한 명시적인 근거를 담은 few-shot 예시는, 엣지 케이스에 필요한 비교 판단 과정을 모델에 가르친다. 이는 일반적인 예시나 선언적 규칙보다 더 효과적이다.

**해설 신규** 오류가 생기는 모호한 시나리오를 겨냥한 few-shot 예시에, 다른 도구보다 이 도구가 나은 이유를 명시적으로 덧붙이면 edge case에 필요한 비교 판단 과정을 모델에 가르칠 수 있다. 일반적인 예시나 선언적인 규칙보다 효과적이다.

## CCAR-F-preporato-0001

**EN** A retailer's support system uses a coordinator agent that receives each customer conversation and delegates to three subagents: an order-lookup agent with read-only order tools, a refund agent that can issue refunds, and a policy agent that searches the returns-policy knowledge base. Company policy: refunds above \$250 need a human's approval, and customers can come back to an open conversation within 7 days.

The refund agent needs the order total, the purchase date and the customer's stated reason to decide eligibility. What should the coordinator include when it delegates the task?

**기존** 한 소매업체의 지원 시스템은 각 고객 대화를 받아 세 개의 subagent에 위임하는 coordinator agent를 사용한다. 세 subagent는 읽기 전용 주문 도구를 가진 주문 조회 agent, 환불을 처리할 수 있는 환불 agent, 반품 정책 지식 베이스를 검색하는 정책 agent이다. 회사 정책: \$250를 초과하는 환불은 사람의 승인이 필요하며, 고객은 7일 이내에 열려 있는 대화로 돌아올 수 있다.

환불 agent는 환불 자격을 판단하기 위해 주문 총액, 구매 날짜, 고객이 밝힌 사유가 필요하다. coordinator는 작업을 위임할 때 무엇을 포함해야 하는가?

**신규** 한 소매업체의 고객 지원 시스템은 coordinator agent가 각 고객 대화를 받아 subagent 세 개에 위임하는 구조다. 읽기 전용 주문 도구를 가진 주문 조회 agent, 환불을 처리할 수 있는 환불 agent, 반품 정책 지식 베이스를 검색하는 정책 agent다. 회사 정책은 다음과 같다. \$250를 넘는 환불은 사람의 승인이 필요하고, 고객은 7일 안에 진행 중인 대화로 다시 돌아올 수 있다.

환불 agent가 자격 여부를 판단하려면 주문 총액, 구매 날짜, 고객이 밝힌 사유가 필요하다. coordinator는 작업을 위임할 때 무엇을 포함해야 하는가?

- A. 기존: 환불 agent가 고객에게 세부 정보를 다시 말해 달라고 요청하도록 하는 지시
  - 신규: 환불 agent가 고객에게 세부 정보를 다시 말해 달라고 요청하도록 하는 지시
- B. 기존: 환불 agent가 아무것도 놓치지 않도록 전체 원본 대화 기록과 이전의 모든 도구 출력
  - 신규: 환불 agent가 놓치는 것이 없도록 전체 원본 대화 기록과 이전의 모든 도구 출력
- C. 기존: 환불 agent에 필요한 구체적인 사실을 위임 프롬프트에 직접 적은 것: 주문 id, 총액, 구매 날짜, 고객이 밝힌 사유
  - 신규: 환불 agent에게 필요한 구체적인 사실(주문 id, 총액, 구매 날짜, 고객이 밝힌 사유)을 위임 prompt에 적어서 전달
- D. 기존: 추가로 포함할 것은 없다. subagent가 coordinator의 대화 기록을 읽을 수 있기 때문이다
  - 신규: subagent가 coordinator의 대화 기록을 읽을 수 있으므로 추가로 넘길 것은 없다

**해설 EN** Subagents in a hub-and-spoke design start with their own context window and see only what the coordinator passes to them, so C is the working design: the minimum necessary context, stated explicitly. D assumes an inheritance that doesn't exist. B spends tokens and attention on material the decision doesn't need, which is where lost-in-the-middle errors start. A makes the customer pay for a gap the coordinator could close with facts it already has.

**해설 기존** hub-and-spoke 설계의 subagent는 자체 context window로 시작하며 coordinator가 넘겨주는 내용만 볼 수 있으므로, 필요한 최소한의 context를 명시적으로 적은 C가 올바르게 동작하는 설계이다. D는 존재하지 않는 상속을 가정한다. B는 결정에 필요하지 않은 자료에 토큰과 주의력을 소모하며, 바로 이것이 lost-in-the-middle 오류의 시작점이다. A는 coordinator가 이미 가진 사실로 메울 수 있는 공백의 비용을 고객에게 떠넘긴다.

**해설 신규** hub-and-spoke 설계에서 subagent는 자기만의 context window로 시작하고, coordinator가 넘겨 준 내용만 볼 수 있다. 그래서 필요한 최소한의 context를 명시적으로 적어 넘기는 C가 제대로 작동하는 설계다. D는 존재하지 않는 상속을 가정한다. B는 판단에 필요 없는 자료에 token과 attention을 쓰게 만드는데, lost-in-the-middle 오류가 여기서 시작된다. A는 coordinator가 이미 가진 사실로 메울 수 있는 빈틈을 고객에게 떠넘긴다.

## CCAR-F-preporato-0002

**EN** A retailer's support system uses a coordinator agent that receives each customer conversation and delegates to three subagents: an order-lookup agent with read-only order tools, a refund agent that can issue refunds, and a policy agent that searches the returns-policy knowledge base. Company policy: refunds above \$250 need a human's approval, and customers can come back to an open conversation within 7 days.

Which TWO events should trigger a handoff to a human agent? (Select TWO)

**기존** 한 소매업체의 지원 시스템은 각 고객 대화를 받아 세 개의 subagent에 위임하는 coordinator agent를 사용한다. 세 subagent는 읽기 전용 주문 도구를 가진 주문 조회 agent, 환불을 처리할 수 있는 환불 agent, 반품 정책 지식 베이스를 검색하는 정책 agent이다. 회사 정책: \$250를 초과하는 환불은 사람의 승인이 필요하며, 고객은 7일 이내에 열려 있는 대화로 돌아올 수 있다.

사람 상담원에게 넘기는 handoff를 유발해야 하는 두 가지 이벤트는 무엇인가? (두 개 선택)

**신규** 소매업체의 고객 지원 시스템에서 coordinator agent가 고객 대화를 하나씩 받아 subagent 세 개에 위임한다. subagent는 읽기 전용 주문 도구를 가진 주문 조회 agent, 환불을 실행할 수 있는 환불 agent, 반품 정책 지식 베이스를 검색하는 정책 agent다. 회사 정책상 \$250을 넘는 환불은 사람의 승인이 필요하고, 고객은 진행 중인 대화에 7일 안에 다시 들어올 수 있다.

사람 상담원에게 넘겨야 하는 경우는 무엇인가? (2개 선택)

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

**해설 신규** 사람과 연결해 달라는 명시적 요청(B)은 언제든 escalation 사유가 된다. \$400 환불(E)은 승인 기준인 \$250을 넘으므로 정책상 반드시 사람에게 넘겨야 한다. 요청이 명확한 정책 범위 안에 있다면 감정만으로는 사유가 되지 않는다. agent가 불만에 공감하면서 직접 처리하면 된다. 모델이 스스로 보고하는 신뢰도(C)는 보정이 잘 안 되어 있어서 trigger로 믿을 수 없다. 작업이 복잡한지(A)는 agent가 감당할 몫이다.

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

## CCAR-F-preporato-0005

**EN** A security team runs a nightly audit across 40 repositories. A coordinator spawns one scanner subagent per repository. Each scanner has `Read`, `Grep` and `Glob` plus a dependency-check tool. The coordinator merges the findings into one report for the morning stand-up and opens tickets for new critical issues.

Which execution pattern fits the scanning stage and the report stage?

**기존** 한 보안 팀이 40개 저장소를 대상으로 매일 밤 감사를 실행한다. coordinator는 저장소당 하나씩 scanner subagent를 생성한다. 각 scanner는 `Read`, `Grep`, `Glob`과 의존성 검사 도구를 갖는다. coordinator는 결과를 하나의 보고서로 병합해 아침 스탠드업에 쓰고, 새로 발견된 critical 이슈에 대한 티켓을 연다.

스캔 단계와 보고서 단계에는 어떤 실행 패턴이 적합한가?

**신규** 보안팀이 매일 밤 저장소 40개를 대상으로 감사를 돌린다. coordinator가 저장소마다 scanner subagent를 하나씩 띄운다. 각 scanner는 `Read`, `Grep`, `Glob`과 의존성 검사 도구를 쓸 수 있다. coordinator는 결과를 합쳐 아침 stand-up용 보고서 하나를 만들고, 새로 발견된 critical 이슈는 티켓으로 등록한다.

스캔 단계와 보고서 단계에는 각각 어떤 실행 패턴이 맞는가?

- A. 기존: 40개 스캔은 서로 독립적이므로 병렬로 fan out하고, 정규화된 결과로 보고서를 만드는 병합 단계를 하나 실행한다
  - 신규: 독립적인 40개 스캔은 병렬로 fan out하고, 정규화된 결과로 보고서를 만드는 merge 단계는 하나만 둔다
- B. 기존: 여러 보고서 작성자를 병렬로 실행하고 그 출력을 이어 붙인다
  - 신규: 보고서 작성기를 여러 개 병렬로 돌린 뒤 결과물을 이어 붙인다
- C. 기존: 저장소 간 패턴을 찾아낼 수 있도록 하나의 agent가 단일 context에서 40개 저장소를 모두 스캔한다
  - 신규: 저장소 간 패턴을 찾을 수 있도록 agent 하나가 하나의 context에서 40개 저장소를 모두 스캔한다
- D. 기존: 각 scanner가 이전 scanner의 발견 사항에서 배울 수 있도록 순차적으로 스캔한 다음, 보고서를 섹션별로 병렬 작성한다
  - 신규: 각 scanner가 앞선 scanner의 결과를 참고하도록 순차로 스캔하고, 보고서는 섹션별로 병렬 작성한다

**해설 EN** Independent work runs in parallel and dependent work runs in sequence, so the hybrid in A matches the data dependencies: the scans don't need each other, and the report needs all of them. D serializes independent work and slows the audit for no gain. C pushes 40 repositories into one context, which degrades attention and turns one failure into a total failure. B produces a report with no single view of the findings, which is what the merge step exists for.

**해설 기존** 독립적인 작업은 병렬로, 의존적인 작업은 순차로 실행하므로, 데이터 의존성에 맞는 것은 혼합 방식인 A이다. 스캔은 서로를 필요로 하지 않고, 보고서는 모든 스캔을 필요로 한다. D는 독립적인 작업을 직렬화해 아무 이득 없이 감사를 느리게 한다. C는 40개 저장소를 하나의 context에 밀어 넣어 주의력을 떨어뜨리고 한 번의 실패를 전체 실패로 만든다. B는 발견 사항에 대한 단일한 시각이 없는 보고서를 만들어내며, 병합 단계는 바로 이를 위해 존재한다.

**해설 신규** 독립적인 작업은 병렬로, 의존하는 작업은 순차로 돌린다. 그래서 둘을 섞은 A가 데이터 의존 관계와 맞는다. 스캔끼리는 서로 필요하지 않고, 보고서는 스캔 결과가 전부 있어야 쓸 수 있다. D는 독립적인 작업을 순차로 돌리므로, 얻는 것 없이 감사만 느려진다. C는 저장소 40개를 context 하나에 밀어 넣어 attention이 떨어지고, 한 번의 실패가 전체 실패가 된다. B는 결과를 한눈에 볼 수 있는 보고서가 나오지 않는다. 결과를 한곳에 모으려고 두는 것이 바로 merge 단계다.

## CCAR-F-preporato-0006

**EN** A security team runs a nightly audit across 40 repositories. A coordinator spawns one scanner subagent per repository. Each scanner has `Read`, `Grep` and `Glob` plus a dependency-check tool. The coordinator merges the findings into one report for the morning stand-up and opens tickets for new critical issues.

Last night the audit crashed at repository 27. The rerun started again from repository 1 and opened duplicate tickets for findings already reported. Which TWO changes fix this? (Select TWO)

**기존** 한 보안 팀이 40개 저장소를 대상으로 매일 밤 감사를 실행한다. coordinator는 저장소당 하나씩 scanner subagent를 생성한다. 각 scanner는 `Read`, `Grep`, `Glob`과 의존성 검사 도구를 갖는다. coordinator는 결과를 하나의 보고서로 병합해 아침 스탠드업에 쓰고, 새로 발견된 critical 이슈에 대한 티켓을 연다.

어젯밤 감사가 27번째 저장소에서 중단되었다. 재실행은 1번째 저장소부터 다시 시작했고 이미 보고된 발견 사항에 대해 중복 티켓을 열었다. 이를 해결하는 두 가지 변경은 무엇인가? (두 개 선택)

**신규** 보안팀이 매일 밤 저장소 40개를 대상으로 감사를 돌린다. coordinator가 저장소마다 scanner subagent를 하나씩 띄운다. 각 scanner는 `Read`, `Grep`, `Glob`과 의존성 검사 도구를 쓸 수 있다. coordinator는 결과를 합쳐 아침 stand-up용 보고서 하나를 만들고, 새로 발견된 critical 이슈는 티켓으로 등록한다.

어젯밤 감사가 27번째 저장소에서 중단됐다. 다시 실행하자 1번 저장소부터 새로 시작했고, 이미 보고된 finding에 대해 티켓이 중복으로 생겼다. 이 문제를 해결하는 변경 두 가지는 무엇인가? (2개 선택)

- A. 기존: 진행 상황(완료된 저장소, 대기 중인 저장소, 지금까지의 결과)을 manifest 파일에 checkpoint로 저장하고, 중단 후 이를 기준으로 재개한다
  - 신규: 진행 상황(완료한 저장소, 남은 저장소, 지금까지의 결과)을 manifest 파일에 checkpoint로 저장하고, 중단된 뒤에는 그 파일에서 이어서 시작한다
- B. 기존: scanner가 이전 실행을 기억하도록 더 큰 context window를 제공한다
  - 신규: scanner의 context window를 키워서 이전 실행을 기억하게 한다
- C. 기존: 감사를 매일 밤이 아니라 매주 실행한다
  - 신규: 감사를 매일 밤이 아니라 매주 실행한다
- D. 기존: 재실행이 중복을 만들지 못하도록, 예를 들어 저장소와 발견 사항 id를 키로 삼아 티켓 생성을 idempotent하게 만든다
  - 신규: 티켓 생성을 idempotent하게 만든다. 예를 들어 저장소와 finding id를 키로 삼아, 다시 실행해도 중복 티켓이 생기지 않게 한다
- E. 기존: 시작할 때 coordinator에게 이미 끝낸 저장소가 어디인지 묻는다
  - 신규: 시작할 때 coordinator에게 이미 끝낸 저장소가 어디인지 물어본다

**해설 EN** A manifest (A) lets the restarted coordinator continue from repository 27, and idempotent side effects (D) make any replayed step harmless; together they turn a crash into a delay. Context windows (B) don't survive a process crash, and the coordinator has no memory of the previous run to ask about (E), because the API is stateless. Running less often (C) leaves the failure in place.

**해설 기존** manifest(A)는 재시작한 coordinator가 27번째 저장소부터 이어가게 하고, idempotent한 부수 효과(D)는 재실행되는 어떤 단계도 무해하게 만든다. 둘을 함께 쓰면 중단이 지연으로 바뀐다. context window(B)는 프로세스 중단 이후에 남지 않으며, API는 stateless이므로 coordinator에게는 물어볼 만한 이전 실행의 기억이 없다(E). 실행 빈도를 줄이는 것(C)은 문제를 그대로 둔다.

**해설 신규** manifest(A)가 있으면 다시 시작한 coordinator가 27번 저장소부터 이어갈 수 있고, side effect를 idempotent하게 만들면(D) 재실행된 단계가 무해해진다. 두 가지를 함께 쓰면 중단은 지연으로 바뀐다. context window(B)는 프로세스가 죽으면 남지 않는다. API는 stateless라서 coordinator에게는 이전 실행의 기억이 없고, 그래서 물어봐도 답이 없다(E). 실행 빈도를 줄이면(C) 문제는 그대로 남는다.

## CCAR-F-preporato-0007

**EN** A security team runs a nightly audit across 40 repositories. A coordinator spawns one scanner subagent per repository. Each scanner has `Read`, `Grep` and `Glob` plus a dependency-check tool. The coordinator merges the findings into one report for the morning stand-up and opens tickets for new critical issues.

An engineer proposes giving every scanner the full tool set, including `Write`, `Bash` and the ticketing tool, 'in case they need it.' What is the best response?

**기존** 한 보안 팀이 40개 저장소를 대상으로 매일 밤 감사를 실행한다. coordinator는 저장소당 하나씩 scanner subagent를 생성한다. 각 scanner는 `Read`, `Grep`, `Glob`과 의존성 검사 도구를 갖는다. coordinator는 결과를 하나의 보고서로 병합해 아침 스탠드업에 쓰고, 새로 발견된 critical 이슈에 대한 티켓을 연다.

한 엔지니어가 '필요할 경우를 대비해' 모든 scanner에 `Write`, `Bash`, 티켓 도구를 포함한 전체 도구 세트를 주자고 제안한다. 가장 좋은 대응은 무엇인가?

**신규** 보안팀이 매일 밤 저장소 40개를 대상으로 감사를 돌린다. coordinator가 저장소마다 scanner subagent를 하나씩 띄운다. 각 scanner는 `Read`, `Grep`, `Glob`과 의존성 검사 도구를 쓸 수 있다. coordinator는 결과를 합쳐 아침 stand-up용 보고서 하나를 만들고, 새로 발견된 critical 이슈는 티켓으로 등록한다.

한 엔지니어가 '혹시 필요할지 모르니' 모든 scanner에 `Write`, `Bash`, 티켓 도구까지 전체 도구를 주자고 제안한다. 가장 좋은 대응은 무엇인가?

- A. 기존: Bash가 다른 도구가 하는 모든 일을 할 수 있으므로 scanner의 도구를 Bash 하나로 바꾼다
  - 신규: Bash가 다른 도구의 기능을 전부 할 수 있으니 scanner의 도구를 Bash 하나로 바꾼다
- B. 기존: scanner에 모든 도구를 주고 쓰기를 금지하는 system prompt 규칙을 추가한다
  - 신규: scanner에 모든 도구를 주고, system prompt에 쓰기를 금지하는 규칙을 추가한다
- C. 기존: 각 scanner는 맡은 일에 필요한 읽기 전용 도구만 유지하고, 병합된 결과로 티켓을 여는 일은 coordinator만 하도록 한다
  - 신규: 각 scanner에는 자기 일에 필요한 읽기 전용 도구만 주고, 티켓은 합쳐진 결과를 바탕으로 coordinator만 등록하게 한다
- D. 기존: 도구가 많을수록 scanner가 더 유능해지므로 제안을 받아들인다
  - 신규: 도구가 많을수록 scanner의 능력이 올라가니 제안을 받아들인다

**해설 EN** Least privilege scopes each agent to what its responsibility requires. C also keeps tool selection accurate and stops a misbehaving scanner from changing code or opening tickets. D widens the blast radius and adds selection noise for capabilities nobody uses. B relies on a probabilistic instruction to restrain a capability that should never be there. A hands the scanners the broadest tool of all.

**해설 기존** 최소 권한 원칙은 각 agent를 자기 책임에 필요한 범위로 한정한다. C는 또한 도구 선택의 정확도를 유지하고, 오동작하는 scanner가 코드를 바꾸거나 티켓을 여는 것을 막는다. D는 영향 범위를 넓히고 아무도 쓰지 않는 기능 때문에 선택의 잡음을 더한다. B는 애초에 있어서는 안 될 능력을 확률적인 지시로 억제하려 한다. A는 scanner에게 가장 광범위한 도구를 쥐여 준다.

**해설 신규** least privilege는 각 agent에게 맡은 책임에 필요한 권한만 준다는 원칙이다. C는 도구 선택의 정확도도 지켜 주고, 오작동하는 scanner가 코드를 바꾸거나 티켓을 여는 일도 막는다. D는 피해 범위를 넓히고, 아무도 쓰지 않을 기능 때문에 도구 선택에 잡음만 늘린다. B는 애초에 있으면 안 되는 기능을 확률적인 지시문으로 막으려는 것이다. A는 scanner에게 가장 범위가 넓은 도구를 쥐여 주는 셈이다.

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

## CCAR-F-preporato-0009

**EN** After the first tool call, every follow-up request in your agent loop fails with a 400 error. Here is how the loop builds the next request. What is wrong?

```python
response = client.messages.create(model=MODEL, max_tokens=1024,
                                  tools=tools, messages=messages)
if response.stop_reason == "tool_use":
    call = next(b for b in response.content if b.type == "tool_use")
    result = run_tool(call.name, call.input)
    messages.append({"role": "user", "content": [{
        "type": "tool_result",
        "tool_use_id": call.id,
        "content": result,
    }]})
```

**기존** 첫 번째 도구 호출 이후 agent loop의 모든 후속 요청이 400 오류로 실패한다. 다음은 loop가 다음 요청을 만드는 방식이다. 무엇이 잘못되었는가?

```python
response = client.messages.create(model=MODEL, max_tokens=1024,
                                  tools=tools, messages=messages)
if response.stop_reason == "tool_use":
    call = next(b for b in response.content if b.type == "tool_use")
    result = run_tool(call.name, call.input)
    messages.append({"role": "user", "content": [{
        "type": "tool_result",
        "tool_use_id": call.id,
        "content": result,
    }]})
```

**신규** 첫 번째 도구 호출 이후 agent loop의 모든 후속 요청이 400 오류로 실패한다. 아래는 loop가 다음 요청을 만드는 방식이다. 무엇이 문제인가?

```python
response = client.messages.create(model=MODEL, max_tokens=1024,
                                  tools=tools, messages=messages)
if response.stop_reason == "tool_use":
    call = next(b for b in response.content if b.type == "tool_use")
    result = run_tool(call.name, call.input)
    messages.append({"role": "user", "content": [{
        "type": "tool_result",
        "tool_use_id": call.id,
        "content": result,
    }]})
```

- A. 기존: loop가 첫 번째 호출 이후 `tool_choice`를 `any`로 설정해야 한다
  - 신규: 첫 호출 이후에는 `tool_choice`를 `any`로 설정해야 한다
- B. 기존: `tool_use` 블록을 포함한 assistant 턴이 추가되지 않아, `tool_result`가 다음 요청에 들어 있지 않은 호출을 가리킨다
  - 신규: `tool_use` 블록이 들어 있는 assistant turn을 messages에 추가하지 않아서, `tool_result`가 다음 요청에 없는 호출을 가리킨다
- C. 기존: `tool_result` 블록은 system prompt에 들어가야 한다
  - 신규: `tool_result` 블록은 system prompt에 들어가야 한다
- D. 기존: `max_tokens`가 tool loop에는 너무 낮다
  - 신규: tool loop에 쓰기에는 `max_tokens`가 너무 작다

**해설 EN** The API is stateless, so each request must carry the whole exchange: the assistant message with the `tool_use` block comes first, then the user message with the matching `tool_result` (B). Without it, the `tool_use_id` points at nothing. C misplaces tool results, which go in a user turn. D and A change settings that have nothing to do with a malformed history.

**해설 기존** API는 stateless이므로 각 요청은 전체 교환을 담고 있어야 한다. `tool_use` 블록이 있는 assistant 메시지가 먼저 오고, 그다음에 대응하는 `tool_result`가 있는 user 메시지가 온다(B). 이것이 없으면 `tool_use_id`는 아무것도 가리키지 못한다. C는 도구 결과의 위치를 잘못 알고 있으며, 도구 결과는 user 턴에 들어간다. D와 A는 잘못 구성된 기록과 관련 없는 설정을 바꾸는 것이다.

**해설 신규** API는 stateless라서 요청마다 대화 전체를 담아야 한다. `tool_use` 블록이 있는 assistant 메시지가 먼저 오고, 그다음에 대응하는 `tool_result`가 든 user 메시지가 와야 한다(B). assistant 메시지가 빠지면 `tool_use_id`가 가리킬 대상이 없다. C는 tool result를 둘 자리를 잘못 안 것이다. tool result는 user turn에 넣는다. D와 A는 잘못된 history와 관련 없는 설정을 바꾸는 선택지다.

## CCAR-F-preporato-0010

**EN** Your research agent uses the server-side web search tool. Some responses come back with `stop_reason` `pause_turn`, and the loop treats them as finished, returning half-done research. What is the correct handling?

**기존** 리서치 agent가 server-side web search 도구를 사용한다. 일부 응답은 `stop_reason`이 `pause_turn`으로 돌아오는데, loop는 이를 완료된 것으로 취급해 절반만 끝난 리서치를 반환한다. 올바른 처리 방법은 무엇인가?

**신규** 리서치 agent가 server-side web search 도구를 쓴다. 일부 응답의 `stop_reason`이 `pause_turn`으로 오는데, loop가 이를 끝난 것으로 보고 반쯤 하다 만 리서치를 그대로 돌려준다. 올바른 처리는 무엇인가?

- A. 기존: 일시 중지된 assistant 응답을 그대로 추가한 후속 요청을 보내, Claude가 server-side 작업을 이어갈 수 있게 한다
  - 신규: 멈춘 assistant 응답을 그대로 이어 붙여 후속 요청을 보내서, Claude가 server-side 작업을 계속하게 한다
- B. 기존: `max_tokens`를 올리고 원래 요청을 다시 보낸다
  - 신규: `max_tokens`를 올리고 원래 요청을 다시 보낸다
- C. 기존: `pause_turn`을 `end_turn`과 똑같이 취급한다
  - 신규: `pause_turn`을 `end_turn`과 똑같이 취급한다
- D. 기존: web search를 로컬에서 실행하고 그에 대한 `tool_result`를 반환한다
  - 신규: web search를 로컬에서 직접 실행하고 그 결과를 `tool_result`로 돌려준다

**해설 EN** `pause_turn` means a server-side tool loop reached its iteration limit mid-task. The documented handling is A: return the response as the latest assistant turn, and Claude picks up where it stopped. C is the bug in the question. D treats a server tool like a client tool; there is no `tool_use` for your code to answer. B restarts the work and pays for it twice.

**해설 기존** `pause_turn`은 server-side 도구 loop가 작업 도중 반복 한도에 도달했음을 뜻한다. 문서화된 처리 방법은 A이다. 응답을 가장 최근 assistant 턴으로 반환하면 Claude가 멈춘 지점부터 이어간다. C가 문제에 나온 버그이다. D는 server 도구를 client 도구처럼 취급하는 것이며, 코드가 응답할 `tool_use`는 없다. B는 작업을 처음부터 다시 시작하고 그 비용을 두 번 치른다.

**해설 신규** `pause_turn`은 server-side tool loop가 작업 도중 반복 한도에 도달했다는 뜻이다. 문서에 나온 처리 방법은 A다. 응답을 가장 최근 assistant turn으로 돌려 보내면 Claude가 멈춘 지점부터 이어간다. C가 바로 문제에 나온 버그다. D는 server tool을 client tool처럼 다루는 것이다. 코드가 응답해야 할 `tool_use`는 없다. B는 작업을 처음부터 다시 시작해서 비용을 두 번 낸다.

## CCAR-F-preporato-0011

**EN** A team answers one-line FAQ questions from a two-page policy with a six-subagent pipeline: retriever, reader, drafter, tone checker, fact checker and formatter. Answers take 25 seconds and cost far more than expected. What is the best change?

**기존** 한 팀이 두 페이지짜리 정책 문서로 한 줄짜리 FAQ 질문에 답하기 위해 retriever, reader, drafter, tone checker, fact checker, formatter로 이루어진 여섯 개 subagent 파이프라인을 사용한다. 답변에 25초가 걸리고 비용도 예상보다 훨씬 많이 든다. 가장 좋은 변경은 무엇인가?

**신규** 한 팀이 두 쪽짜리 정책 문서를 보고 한 줄짜리 FAQ 질문에 답하려고 retriever, reader, drafter, tone checker, fact checker, formatter로 이뤄진 subagent 6개짜리 pipeline을 쓴다. 답변에 25초가 걸리고 비용도 예상보다 훨씬 많이 든다. 가장 좋은 개선은 무엇인가?

- A. 기존: 정책을 context에 넣은 단일 모델 호출로 줄이고, 필요하면 가벼운 검증 단계를 추가한다
  - 신규: 정책 문서를 context에 넣고 모델을 한 번만 호출하는 구조로 줄이고, 필요하면 가벼운 검증 단계를 덧붙인다
- B. 기존: 재시도를 줄이기 위해 모든 subagent를 가장 유능한 모델로 옮긴다
  - 신규: 재시도를 줄이려고 모든 subagent를 가장 성능이 높은 모델로 바꾼다
- C. 기존: coordinator 아래에서 여섯 개 subagent를 병렬로 실행한다
  - 신규: coordinator 아래에서 subagent 6개를 병렬로 돌린다
- D. 기존: 각 subagent의 출력을 cache한다
  - 신규: 각 subagent의 출력을 cache한다

**해설 EN** This is over-decomposition: the task is small, single-domain and fits in one context, so the subagents add orchestration cost without any isolation benefit, and A removes the overhead. Parallelizing (C) doesn't fit a chain where each step needs the previous step's output. B raises the cost of a design that shouldn't exist. D helps only with repeated identical questions and leaves the latency of the chain in place.

**해설 기존** 이것은 과도한 분해이다. 작업이 작고 단일 도메인이며 하나의 context에 들어가므로, subagent는 격리의 이점 없이 orchestration 비용만 더하고, A는 그 오버헤드를 없앤다. 각 단계가 이전 단계의 출력을 필요로 하는 체인에는 병렬화(C)가 맞지 않는다. B는 존재해서는 안 될 설계의 비용을 높인다. D는 동일한 질문이 반복될 때만 도움이 되고 체인의 지연은 그대로 둔다.

**해설 신규** 과도한 분해(over-decomposition)다. 작업이 작고 한 영역에 속하며 context 하나에 들어가는데도 subagent를 썼다. 격리로 얻는 이득은 없이 orchestration 비용만 늘었고, A는 그 부담을 없앤다. C는 각 단계가 앞 단계의 출력을 필요로 하는 사슬에는 맞지 않는다. B는 애초에 있으면 안 되는 설계의 비용만 키운다. D는 같은 질문이 반복될 때만 도움이 되고, 사슬 때문에 생기는 지연은 그대로 남는다.

## CCAR-F-preporato-0012

**EN** A payments service's error rate spiked. The cause could be in code, configuration, infrastructure or a third-party API, and what to check next depends on what each check finds. How should the coordinator decompose the investigation?

**기존** 결제 서비스의 오류율이 급증했다. 원인은 코드, 설정, 인프라, 서드파티 API 중 어디에든 있을 수 있고, 다음에 무엇을 확인할지는 각 확인에서 무엇이 발견되는지에 달려 있다. coordinator는 조사를 어떻게 분해해야 하는가?

**신규** 결제 서비스의 오류율이 급증했다. 원인은 코드, 설정, 인프라, 서드파티 API 중 어디에든 있을 수 있고, 다음에 무엇을 확인할지는 각 확인 결과에 따라 달라진다. coordinator는 이 조사를 어떻게 분해해야 하는가?

- A. 기존: Claude에게 근본 원인을 묻는 프롬프트 하나
  - 신규: Claude에게 근본 원인을 알려 달라고 prompt 하나로 요청한다
- B. 기존: 네 가지 확인을 정해진 순서대로 실행하는 고정 파이프라인
  - 신규: 네 가지 확인을 정해진 순서대로 실행하는 고정 pipeline을 쓴다
- C. 기존: 동적 분해: 각 발견 사항에서 다음 하위 작업을 계획하되, token 예산과 반복 횟수 상한을 안전장치로 코드에서 강제한다
  - 신규: 동적 분해를 쓴다. 각 발견을 바탕으로 다음 하위 작업을 계획하고, 안전장치로 token 예산과 반복 횟수 상한을 코드에서 강제한다
- D. 기존: coordinator 없이 생각할 수 있는 모든 확인을 병렬로 실행한다
  - 신규: coordinator 없이 생각해 낼 수 있는 모든 확인을 병렬로 돌린다

**해설 EN** Open-ended investigations, where the next step depends on what you just learned, call for dynamic decomposition. Because that pattern costs more and can wander, C pairs it with limits enforced outside the model. A fixed pipeline (B) suits workflows that are known in advance. D wastes effort and leaves nobody to connect the findings. A asks for an answer without giving the model any way to gather evidence.

**해설 기존** 방금 알게 된 내용에 따라 다음 단계가 달라지는 개방형 조사에는 동적 분해가 맞다. 이 패턴은 비용이 더 들고 헤맬 수 있으므로, C는 모델 바깥에서 강제되는 한도를 함께 둔다. 고정 파이프라인(B)은 미리 알려진 워크플로에 적합하다. D는 노력을 낭비하고 발견 사항을 연결해 줄 주체를 두지 않는다. A는 모델이 증거를 모을 방법을 주지 않은 채 답만 요구한다.

**해설 신규** 방금 알게 된 내용에 따라 다음 단계가 정해지는 열린 조사에는 동적 분해가 맞다. 이 패턴은 비용이 더 들고 엉뚱한 곳으로 흘러갈 수 있어서, C는 모델 바깥에서 강제하는 한도를 함께 둔다. 고정 pipeline(B)은 미리 알려진 workflow에 어울린다. D는 노력을 낭비하고, 발견을 연결해 줄 주체도 없다. A는 모델에게 증거를 모을 방법은 주지 않고 답만 요구한다.

## CCAR-F-preporato-0013

**EN** Long research tasks sometimes use ten times the expected tokens. Which TWO belong in a reliable token-budget design? (Select TWO)

**기존** 긴 리서치 작업이 가끔 예상보다 열 배나 많은 token을 사용한다. 신뢰할 수 있는 token 예산 설계에 포함되어야 하는 두 가지는 무엇인가? (두 개 선택)

**신규** 긴 리서치 작업이 예상보다 token을 열 배나 쓸 때가 있다. 믿을 수 있는 token 예산 설계에 들어가야 할 것 두 가지는 무엇인가? (2개 선택)

- A. 기존: 모든 호출에서 `max_tokens`를 50으로 설정한다
  - 신규: 모든 호출에서 `max_tokens`를 50으로 설정한다
- B. 기존: 매 턴마다 Claude에게 지금까지 token을 얼마나 사용했는지 묻는다
  - 신규: 매 turn마다 Claude에게 지금까지 token을 얼마나 썼는지 묻는다
- C. 기존: Claude에게 50,000 token 이하로 유지하라고 요청하는 system prompt 지시
  - 신규: system prompt에 50,000 token 이하로 유지하라고 지시한다
- D. 기존: loop 안에서 각 응답의 usage 필드로부터 입력과 출력 token의 누적 합계를 추적한다
  - 신규: loop 안에서 각 응답의 usage 필드로 입력·출력 token 누적량을 추적한다
- E. 기존: 예산에 도달하면 코드에서 loop를 중단하고, 예산의 약 80% 시점에 마무리 지시를 주입한다
  - 신규: 예산에 도달하면 코드에서 loop를 멈추고, 예산의 약 80% 지점에서는 마무리하라는 지시를 주입한다

**해설 EN** Budgets are enforced from outside the model: measure from the usage field (D) and act on the measurement with a soft warning and a hard stop (E). An instruction (C) and the model's own estimate (B) are probabilistic and unmeasured. A tiny `max_tokens` (A) truncates every response, so turns end at the cap before they finish.

**해설 기존** 예산은 모델 바깥에서 강제된다. usage 필드로 측정하고(D), 그 측정값에 따라 소프트 경고와 하드 중단으로 대응한다(E). 지시(C)와 모델 자신의 추정(B)은 확률적이며 측정된 값이 아니다. 아주 작은 `max_tokens`(A)는 모든 응답을 잘라 버리므로 턴이 끝나기도 전에 한도에서 종료된다.

**해설 신규** 예산은 모델 바깥에서 강제해야 한다. usage 필드로 측정하고(D), 그 측정값에 따라 약한 경고와 강제 중단으로 대응한다(E). 지시문(C)과 모델이 스스로 한 추정(B)은 확률적이고 측정된 값이 아니다. `max_tokens`를 아주 작게 잡으면(A) 모든 응답이 잘려서, turn이 끝나기 전에 한도에서 멈춘다.

## CCAR-F-preporato-0014

**EN** A team's MCP server should (1) let Claude create Jira tickets, (2) expose the team's API schema files so a user can attach them as context, and (3) provide a reusable 'triage this incident' template with the team's severity rubric. Which MCP primitives fit, in that order?

**기존** 한 팀의 MCP server는 (1) Claude가 Jira 티켓을 만들 수 있게 하고, (2) 사용자가 context로 첨부할 수 있도록 팀의 API 스키마 파일을 노출하며, (3) 팀의 심각도 기준표가 담긴 재사용 가능한 '이 사고를 분류하라' 템플릿을 제공해야 한다. 이 순서대로 어떤 MCP primitive가 적합한가?

**신규** 한 팀의 MCP server가 (1) Claude가 Jira 티켓을 만들 수 있게 하고, (2) 사용자가 context로 첨부할 수 있도록 팀의 API schema 파일을 노출하고, (3) 팀의 심각도 기준이 담긴 '이 장애를 triage하라'는 재사용 가능한 템플릿을 제공해야 한다. 이 순서대로 맞는 MCP primitive는 무엇인가?

- A. 기존: Tool, tool, tool
  - 신규: Tool, tool, tool
- B. 기존: Resource, tool, prompt
  - 신규: Resource, tool, prompt
- C. 기존: Prompt, resource, tool
  - 신규: Prompt, resource, tool
- D. 기존: Tool, resource, prompt
  - 신규: Tool, resource, prompt

**해설 EN** Creating a ticket is an action, so it's a tool. Schema files are read-only data for the client to browse and attach, so they're a resource. The packaged triage template is a prompt. D matches action, data and know-how in that order. A turns data and a template into callable functions. B and C put the action in the wrong primitive.

**해설 기존** 티켓 생성은 행동이므로 tool이다. 스키마 파일은 client가 탐색하고 첨부할 수 있는 읽기 전용 데이터이므로 resource이다. 패키지로 만든 분류 템플릿은 prompt이다. D가 행동, 데이터, 노하우의 순서와 일치한다. A는 데이터와 템플릿을 호출 가능한 함수로 만든다. B와 C는 행동을 잘못된 primitive에 둔다.

**해설 신규** 티켓을 만드는 것은 동작이므로 tool이다. schema 파일은 client가 둘러보고 첨부하는 읽기 전용 데이터이므로 resource다. triage 템플릿은 미리 만들어 둔 prompt다. D는 동작, 데이터, 노하우의 순서와 맞는다. A는 데이터와 템플릿까지 호출 가능한 함수로 만든다. B와 C는 동작을 엉뚱한 primitive에 넣었다.

## CCAR-F-preporato-0015

**EN** Every developer on a team should get the same internal MCP server in Claude Code, and the server needs an API token. Which TWO choices are correct? (Select TWO)

**기존** 팀의 모든 개발자가 Claude Code에서 같은 내부 MCP server를 사용해야 하며, 이 server에는 API token이 필요하다. 올바른 두 가지 선택은 무엇인가? (두 개 선택)

**신규** 팀의 모든 개발자가 Claude Code에서 같은 사내 MCP server를 쓰게 해야 하는데, 이 server에는 API token이 필요하다. 올바른 선택 두 가지는 무엇인가? (2개 선택)

- A. 기존: Claude가 server에 전달할 수 있도록 token을 `CLAUDE.md`에 넣는다
  - 신규: Claude가 server에 전달할 수 있도록 token을 `CLAUDE.md`에 적는다
- B. 기존: 설정을 한 단계로 끝내기 위해 원본 token을 `.mcp.json`에 그대로 붙여 넣는다
  - 신규: 설정을 한 단계로 끝내려고 원본 token을 `.mcp.json`에 그대로 붙여 넣는다
- C. 기존: 프로젝트의 `.mcp.json`에 server를 정의하고 저장소에 커밋한다
  - 신규: server를 프로젝트의 `.mcp.json`에 정의하고 저장소에 commit한다
- D. 기존: `.mcp.json`에서 token을 `${INTERNAL_API_TOKEN}`으로 참조하고 각 개발자가 해당 환경 변수를 설정하게 한다
  - 신규: `.mcp.json`에서는 token을 `${INTERNAL_API_TOKEN}`으로 참조하고, 각 개발자가 그 환경 변수를 설정하게 한다
- E. 기존: 각 개발자가 wiki 페이지를 따라 local scope로 server를 추가하게 한다
  - 신규: 위키 문서를 보고 개발자마다 local scope로 server를 추가하게 한다

**해설 EN** Project scope (C) is the configuration that reaches the whole team through version control, and environment variable expansion (D) keeps the secret out of the repository. B commits a credential. E relies on every developer repeating a manual step, and local scope never propagates. A puts a secret into the model's context, where it can leak through outputs or logs.

**해설 기존** project scope(C)는 버전 관리를 통해 팀 전체에 전달되는 설정이며, 환경 변수 확장(D)은 비밀 값을 저장소 밖에 둔다. B는 자격 증명을 커밋한다. E는 모든 개발자가 수동 단계를 반복하는 데 의존하며, local scope는 다른 사람에게 전파되지 않는다. A는 비밀 값을 모델의 context에 넣어 출력이나 로그를 통해 유출될 수 있게 한다.

**해설 신규** project scope(C)는 버전 관리를 통해 팀 전체에 설정이 전달되는 방식이고, 환경 변수 확장(D)은 비밀 값이 저장소에 들어가지 않게 해 준다. B는 credential을 commit하는 것이다. E는 모든 개발자가 수동 단계를 반복한다는 가정에 기대는 데다, local scope는 다른 사람에게 전파되지 않는다. A는 비밀 값을 모델의 context에 넣어서 출력이나 로그로 새어 나갈 수 있다.

## CCAR-F-preporato-0016

**EN** When users ask to change their email address, Claude often calls `get_customer` instead of `update_customer`, then tells the user the change is done. Both tools exist. What is the first fix?

**기존** 사용자가 이메일 주소 변경을 요청하면 Claude가 `update_customer` 대신 `get_customer`를 호출한 뒤 변경이 완료되었다고 사용자에게 말하는 일이 잦다. 두 도구 모두 존재한다. 첫 번째 해결책은 무엇인가?

**신규** 사용자가 이메일 주소를 바꿔 달라고 하면 Claude가 `update_customer`가 아니라 `get_customer`를 호출하고는 변경이 끝났다고 알려 준다. 두 도구 모두 등록되어 있다. 가장 먼저 할 수정은 무엇인가?

- A. 기존: 업데이트에는 `update_customer`를 사용하라고 Claude에게 알려 주는 system prompt 한 줄을 추가한다
  - 신규: 업데이트에는 `update_customer`를 쓰라는 문장을 system prompt에 추가한다
- B. 기존: 두 설명을 다시 작성한다. 각 도구가 하는 일, 언제 사용하는지, 그리고 대신 다른 도구를 써야 하는 경우를 적고 `get_customer`는 읽기 전용이라고 설명한다
  - 신규: 두 도구의 description을 다시 쓴다. 각 도구가 하는 일, 언제 쓰는지, 언제 다른 도구를 써야 하는지를 적고, `get_customer`는 읽기 전용이라고 명시한다
- C. 기존: `get_customer`의 이름을 `fetch_customer`로 바꾼다
  - 신규: `get_customer`의 이름을 `fetch_customer`로 바꾼다
- D. 기존: agent에서 `get_customer`를 제거한다
  - 신규: agent에서 `get_customer`를 제거한다

**해설 EN** Claude selects tools mainly from their descriptions, so overlapping or vague descriptions are the first thing to fix (B), and the boundary statements ('to change a record, use `update_customer`') are what resolve this confusion. A rename (C) changes little while the descriptions stay vague. A system-prompt patch (A) is weaker than fixing the routing signal itself. Removing the read tool (D) breaks every legitimate lookup.

**해설 기존** Claude는 주로 설명을 보고 도구를 선택하므로, 겹치거나 모호한 설명이 가장 먼저 고칠 대상이며(B), 이 혼동을 해소하는 것은 경계를 밝히는 문장('레코드를 변경하려면 `update_customer`를 사용')이다. 이름 변경(C)은 설명이 모호한 채로 남아 있으면 달라지는 것이 거의 없다. system prompt로 덧대는 방법(A)은 라우팅 신호 자체를 고치는 것보다 약하다. 읽기 도구를 제거하면(D) 정당한 조회가 모두 막힌다.

**해설 신규** Claude는 주로 description을 보고 도구를 고른다. 그래서 겹치거나 모호한 description부터 고쳐야 하고(B), 이 혼동은 경계를 밝히는 문장('레코드를 바꾸려면 `update_customer`를 사용')이 해결한다. description이 모호한 채라면 이름을 바꿔도(C) 달라지는 것이 거의 없다. system prompt로 땜질하는 것(A)은 라우팅 신호 자체를 고치는 것보다 약하다. 읽기 도구를 없애면(D) 정상적인 조회가 전부 막힌다.

## CCAR-F-preporato-0017

**EN** Your team wants every file Claude edits to be formatted with Prettier immediately after each edit, for everyone working in the repository. Which configuration does that?

**기존** 팀은 저장소에서 작업하는 모든 사람에 대해, Claude가 편집하는 모든 파일이 각 편집 직후 Prettier로 포맷되기를 원한다. 어떤 설정이 이를 수행하는가?

**신규** 팀은 저장소에서 작업하는 모두에게, Claude가 파일을 수정할 때마다 곧바로 Prettier 포맷이 적용되게 하려 한다. 어떤 설정이 이를 만족하는가?

- A. 기존: 각 개발자의 `~/.claude/settings.json`에 있는 hook
  - 신규: 각 개발자의 `~/.claude/settings.json`에 둔 hook
- B. 기존: `CLAUDE.md`의 한 줄: '모든 편집 후 Prettier를 실행하라'
  - 신규: `CLAUDE.md`의 '수정할 때마다 Prettier를 실행하라'는 한 줄
- C. 기존: 커밋된 `.claude/settings.json`에서 `Edit|Write`에 매칭되어 편집된 파일에 Prettier를 실행하는 `PostToolUse` hook
  - 신규: commit된 `.claude/settings.json`에서 `Edit|Write`에 매칭되고, 수정된 파일에 Prettier를 실행하는 `PostToolUse` hook
- D. 기존: `Edit`에 대해 Prettier를 실행하는 `PreToolUse` hook
  - 신규: `Edit`에 거는 `PreToolUse` hook으로 Prettier를 실행

**해설 EN** Formatting has to run after the file changes, which is `PostToolUse`, and the committed project settings file shares the hook with the whole team, so C covers both requirements. D runs before the edit exists. B is guidance Claude may skip, while a hook runs every time. A works only for developers who set it up themselves.

**해설 기존** 포맷은 파일이 바뀐 뒤에 실행되어야 하므로 `PostToolUse`이고, 커밋된 프로젝트 settings 파일은 hook을 팀 전체와 공유하므로 C가 두 요구 사항을 모두 충족한다. D는 편집이 존재하기 전에 실행된다. B는 Claude가 건너뛸 수 있는 지침인 반면 hook은 매번 실행된다. A는 직접 설정한 개발자에게만 작동한다.

**해설 신규** 포맷팅은 파일이 바뀐 뒤에 실행해야 하므로 `PostToolUse`이고, commit된 프로젝트 설정 파일이 hook을 팀 전체에 공유하므로 C는 두 조건을 모두 충족한다. D는 수정이 일어나기 전에 실행된다. B는 Claude가 건너뛸 수 있는 안내문이지만 hook은 매번 실행된다. A는 직접 설정한 개발자에게만 적용된다.

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

## CCAR-F-preporato-0019

**EN** A `PostToolUse` hook on `Write` scans each file Claude writes. It finds an API key in a file Claude just wrote and exits with code 2. What happens?

**기존** `Write`에 대한 `PostToolUse` hook이 Claude가 쓰는 각 파일을 스캔한다. 이 hook이 Claude가 방금 쓴 파일에서 API key를 발견하고 종료 코드 2로 종료한다. 무슨 일이 일어나는가?

**신규** `Write`에 건 `PostToolUse` hook이 Claude가 쓰는 파일을 매번 스캔한다. 이 hook이 Claude가 방금 쓴 파일에서 API key를 발견하고 exit code 2로 종료한다. 어떻게 되는가?

- A. 기존: 파일은 이미 쓰인 상태이며, Claude는 hook의 stderr 메시지를 받고 이에 대응할 수 있다. 예를 들어 key를 제거할 수 있다
  - 신규: 파일은 이미 쓰인 상태이고, Claude는 hook의 stderr 메시지를 받아 키를 지우는 식으로 대응할 수 있다
- B. 기존: Claude Code가 session을 종료한다
  - 신규: Claude Code가 세션을 종료한다
- C. 기존: `PostToolUse`에서는 종료 코드 2가 무시되므로 아무 일도 일어나지 않는다
  - 신규: `PostToolUse`에서는 exit code 2가 무시되므로 아무 일도 일어나지 않는다
- D. 기존: 쓰기가 취소되어 파일이 생성되지 않는다
  - 신규: 쓰기가 취소되어 파일이 만들어지지 않는다

**해설 EN** `PostToolUse` fires after the tool has run, so it can't undo the write; exit code 2 shows its stderr to Claude (A). To stop the write itself, the check belongs in a `PreToolUse` hook, where exit code 2 blocks the call, which is the behavior D describes. B and C describe behaviors that don't exist.

**해설 기존** `PostToolUse`는 도구가 실행된 뒤에 발동하므로 쓰기를 되돌릴 수 없으며, 종료 코드 2는 stderr를 Claude에게 보여 준다(A). 쓰기 자체를 막으려면 검사는 종료 코드 2가 호출을 차단하는 `PreToolUse` hook에 있어야 하며, 이것이 D가 설명하는 동작이다. B와 C는 존재하지 않는 동작을 설명한다.

**해설 신규** `PostToolUse`는 도구가 실행된 뒤에 동작하므로 쓰기를 되돌릴 수 없고, exit code 2는 stderr를 Claude에게 보여 준다(A). 쓰기 자체를 막으려면 `PreToolUse` hook에서 검사해야 한다. 거기서는 exit code 2가 호출을 차단하고, D가 설명하는 것이 바로 그 동작이다. B와 C는 존재하지 않는 동작을 설명한다.

## CCAR-F-preporato-0020

**EN** A developer asks Claude Code to migrate 40 files from a callback-based API client to async/await. The change touches shared types, and there are two reasonable migration strategies. What is the best way to start?

**기존** 한 개발자가 Claude Code에게 40개 파일을 callback 기반 API client에서 async/await로 마이그레이션하라고 요청한다. 이 변경은 공유 타입을 건드리며, 합리적인 마이그레이션 전략이 두 가지 있다. 시작하는 가장 좋은 방법은 무엇인가?

**신규** 개발자가 Claude Code에게 파일 40개를 callback 기반 API client에서 async/await로 마이그레이션하라고 요청한다. 변경이 공유 타입까지 건드리고, 합리적인 마이그레이션 전략이 두 가지 있다. 어떻게 시작하는 것이 가장 좋은가?

- A. 기존: 전체 변경을 하나의 프롬프트로 요청하고 최종 diff를 검토한다
  - 신규: 전체 변경을 prompt 하나로 요청하고 최종 diff를 검토한다
- B. 기존: 파일별로 직접 실행하며 문제가 나타나는 대로 고친다
  - 신규: 바로 실행해서 파일을 하나씩 처리하며, 문제가 생기면 그때그때 고친다
- C. 기존: 'async/await를 사용하라'는 `CLAUDE.md` 규칙
  - 신규: 'async/await를 사용하라'는 `CLAUDE.md` 규칙을 추가한다
- D. 기존: Plan Mode: 어떤 파일도 바꾸기 전에 Claude가 코드베이스를 탐색하고 검토할 마이그레이션 계획을 제안하게 한다
  - 신규: Plan Mode를 쓴다. Claude가 코드베이스를 탐색하고 마이그레이션 계획을 제안하게 해서, 파일을 바꾸기 전에 그 계획을 검토한다

**해설 EN** Multi-file, cross-cutting changes with more than one valid approach are Plan Mode's case (D): the strategy gets agreed before 40 files move. B and A commit to an approach before anyone has compared the options, and a wrong choice is expensive to unwind. C states a preference without planning the migration.

**해설 기존** 유효한 접근 방식이 둘 이상인 여러 파일에 걸친 횡단적 변경은 Plan Mode가 맞는 경우(D)이다. 40개 파일이 움직이기 전에 전략이 합의된다. B와 A는 누구도 선택지를 비교하기 전에 하나의 접근 방식을 확정하며, 잘못 고르면 되돌리는 데 비용이 크다. C는 마이그레이션을 계획하지 않은 채 선호만 밝힌다.

**해설 신규** 여러 파일에 걸쳐 있고 타당한 접근이 둘 이상인 변경은 Plan Mode가 맞는 경우다(D). 파일 40개를 건드리기 전에 전략부터 합의한다. B와 A는 아무도 선택지를 비교해 보지 않은 채 한 접근을 확정해 버리고, 잘못 골랐을 때는 되돌리는 비용이 크다. C는 선호를 밝힐 뿐 마이그레이션을 계획해 주지는 않는다.

## CCAR-F-preporato-0021

**EN** A team's dependency-audit skill prints thousands of lines of output, and teammates complain it floods the main conversation. Which frontmatter change fixes this?

**기존** 한 팀의 의존성 감사 skill이 수천 줄의 출력을 내어, 팀원들이 메인 대화를 가득 채운다고 불평한다. 어떤 frontmatter 변경이 이를 해결하는가?

**신규** 한 팀의 dependency-audit skill이 수천 줄의 출력을 쏟아내서, 출력이 메인 대화를 뒤덮는다고 팀원들이 불평한다. 어떤 frontmatter 변경이 이 문제를 해결하는가?

- A. 기존: `context: fork`. skill이 격리된 subagent에서 실행되고 결과만 반환한다
  - 신규: `context: fork`. skill이 격리된 subagent에서 실행되고 결과만 돌려준다
- B. 기존: `disable-model-invocation: true`
  - 신규: `disable-model-invocation: true`
- C. 기존: `allowed-tools: Read`
  - 신규: `allowed-tools: Read`
- D. 기존: `model: haiku`
  - 신규: `model: haiku`

**해설 EN** `context: fork` (A) runs the skill in its own subagent context, so the verbose work stays out of the main conversation. B only stops Claude from invoking the skill automatically; the output still floods the conversation whenever someone runs it. C changes which tools are pre-approved and D changes the model, and neither moves the output.

**해설 기존** `context: fork`(A)는 skill을 자체 subagent context에서 실행하므로 장황한 작업이 메인 대화 밖에 머문다. B는 Claude가 skill을 자동으로 호출하는 것만 막을 뿐이며, 누군가 실행할 때마다 출력은 여전히 대화를 가득 채운다. C는 미리 승인되는 도구를 바꾸고 D는 모델을 바꾸는데, 둘 다 출력의 위치를 옮기지 못한다.

**해설 신규** `context: fork`(A)는 skill을 별도의 subagent context에서 실행하므로, 길게 늘어지는 작업 내용이 메인 대화에 들어오지 않는다. B는 Claude가 skill을 자동으로 호출하지 못하게 할 뿐이라, 누군가 skill을 실행하면 출력이 여전히 대화에 쏟아진다. C는 미리 승인되는 도구를 바꾸고 D는 모델을 바꿀 뿐, 어느 쪽도 출력 위치를 옮기지 못한다.

## CCAR-F-preporato-0022

**EN** In a monorepo, files under `services/payments/` follow strict rules (all amounts in integer cents, no floats). The rules confuse Claude when it works on the frontend. Which TWO placements load these rules only when Claude works in the payments code? (Select TWO)

**기존** monorepo에서 `services/payments/` 아래의 파일은 엄격한 규칙(모든 금액은 정수 센트, float 금지)을 따른다. 이 규칙은 Claude가 프런트엔드를 작업할 때 혼란을 준다. Claude가 payments 코드에서 작업할 때만 이 규칙을 로드하는 두 가지 배치는 무엇인가? (두 개 선택)

**신규** monorepo에서 `services/payments/` 아래 파일에는 엄격한 규칙이 있다(금액은 모두 정수 cent 단위, float 금지). 이 규칙 때문에 Claude가 frontend 작업을 할 때 혼란스러워한다. 이 규칙을 Claude가 payments 코드에서 작업할 때만 로드되게 하는 배치 두 가지는 무엇인가? (2개 선택)

- A. 기존: 루트 `CLAUDE.md`의 'Payments only'라는 제목의 섹션
  - 신규: 루트 `CLAUDE.md`에 'Payments only'라는 제목의 섹션을 둔다
- B. 기존: `services/payments/` 안의 `CLAUDE.md` 파일
  - 신규: `services/payments/` 안에 `CLAUDE.md` 파일을 둔다
- C. 기존: frontmatter에 `paths: ["services/payments/**"]`가 있는 `.claude/rules/`의 파일
  - 신규: `.claude/rules/`에 파일을 두고 frontmatter에 `paths: ["services/payments/**"]`를 지정한다
- D. 기존: 각 개발자의 `~/.claude/CLAUDE.md`
  - 신규: 각 개발자의 `~/.claude/CLAUDE.md`에 둔다
- E. 기존: 프로젝트의 `.mcp.json`
  - 신규: 프로젝트의 `.mcp.json`에 둔다

**해설 EN** A path-scoped rule (C) loads when Claude reads or edits a matching file, and a subdirectory `CLAUDE.md` (B) loads on demand when Claude works with files in that directory. The root `CLAUDE.md` (A) loads in every session, frontend work included. D is personal and reaches nobody else. E configures MCP servers and holds no instructions.

**해설 기존** path 범위가 지정된 규칙(C)은 Claude가 일치하는 파일을 읽거나 편집할 때 로드되고, 하위 디렉터리의 `CLAUDE.md`(B)는 Claude가 해당 디렉터리의 파일로 작업할 때 필요에 따라 로드된다. 루트 `CLAUDE.md`(A)는 프런트엔드 작업을 포함한 모든 session에서 로드된다. D는 개인용이라 다른 누구에게도 전달되지 않는다. E는 MCP server를 설정하는 파일이며 지침을 담지 않는다.

**해설 신규** path-scoped rule(C)은 Claude가 일치하는 파일을 읽거나 수정할 때 로드되고, 하위 디렉터리의 `CLAUDE.md`(B)는 Claude가 그 디렉터리의 파일로 작업할 때 필요에 따라 로드된다. 루트 `CLAUDE.md`(A)는 frontend 작업을 포함한 모든 세션에서 로드된다. D는 개인용이라 다른 사람에게는 전달되지 않는다. E는 MCP server를 설정하는 파일이고 지시문은 담지 않는다.

## CCAR-F-preporato-0023

**EN** A code-review prompt says 'Be thorough but avoid nitpicks.' Reviews flag style issues inconsistently and miss SQL injection. Which rewrite fixes the cause?

**기존** 코드 리뷰 프롬프트에 '꼼꼼하게 하되 사소한 지적은 피하라'고 적혀 있다. 리뷰는 스타일 문제를 일관성 없이 지적하고 SQL injection을 놓친다. 원인을 해결하는 재작성은 무엇인가?

**신규** 코드 리뷰 prompt가 '꼼꼼하게 보되 사소한 지적은 피하라'고 되어 있다. 이 때문에 리뷰가 스타일 문제를 들쭉날쭉하게 지적하고 SQL injection은 놓친다. 원인을 해결하는 수정은 무엇인가?

- A. 기존: '당신은 세계 최고 수준의 시니어 보안 엔지니어이다.'
  - 신규: '당신은 세계 최고 수준의 시니어 보안 엔지니어다.'
- B. 기존: '극도로 꼼꼼하게 하고 아무것도 놓치지 마라.'
  - 신규: '매우 꼼꼼하게 보고 아무것도 놓치지 마라.'
- C. 기존: '코멘트는 보수적으로 달아라.'
  - 신규: '코멘트는 보수적으로 달아라.'
- D. 기존: '다음 이슈만 보고하라: SQL injection, XSS, 인증 우회, 코드 내 비밀 값. 심각도가 high 또는 critical인 것만 보고하라. 포맷팅이나 이름 짓기에 대해서는 코멘트하지 마라.'
  - 신규: '다음 이슈만 보고하라: SQL injection, XSS, 인증 우회, 코드에 들어 있는 secret. 심각도가 high 또는 critical인 것만 보고하라. 포맷팅이나 네이밍에는 코멘트하지 마라.'

**해설 EN** Vague instructions produce inconsistent behavior because the model has to guess the threshold. D names the categories, the severity floor and the exclusions, and anyone reading a review can check whether it followed them. B and C push the same vague guidance in two directions. A role line (A) without criteria leaves the same guesswork.

**해설 기존** 모호한 지시는 모델이 기준선을 추측해야 하므로 일관성 없는 동작을 낳는다. D는 범주, 최소 심각도, 제외 대상을 명시하며, 리뷰를 읽는 누구든 그것을 따랐는지 확인할 수 있다. B와 C는 같은 모호한 지침을 서로 반대 방향으로 밀어붙인다. 기준 없는 역할 한 줄(A)은 같은 추측을 그대로 남긴다.

**해설 신규** 모호한 지시는 모델이 기준선을 짐작해야 하므로 동작이 일정하지 않다. D는 범주, 최소 심각도, 제외 대상을 명시하고, 리뷰를 읽는 사람이 그 기준을 지켰는지 확인할 수 있다. B와 C는 같은 모호한 지침을 서로 반대 방향으로 밀 뿐이다. 기준 없이 역할만 주는 A도 짐작에 맡기는 것은 마찬가지다.

## CCAR-F-preporato-0024

**EN** A classifier should flag support tickets that mention a physical safety risk. In testing it flags every ticket containing the word 'fire', including 'firewall rules reset after update.' What is the best few-shot improvement?

**기존** 분류기는 물리적 안전 위험을 언급하는 지원 티켓에 플래그를 달아야 한다. 테스트에서 이 분류기는 '업데이트 후 firewall 규칙이 초기화됨'을 포함해 'fire'라는 단어가 들어 있는 모든 티켓에 플래그를 단다. 가장 좋은 few-shot 개선은 무엇인가?

**신규** classifier가 물리적 안전 위험을 언급한 지원 티켓을 표시해야 한다. 테스트해 보니 'firewall rules reset after update'를 포함해, 'fire'라는 단어가 들어간 티켓을 전부 표시한다. few-shot을 어떻게 개선하는 것이 가장 좋은가?

- A. 기존: '키워드에 속지 마라'라는 지시
  - 신규: '키워드에 속지 마라'는 지시를 추가한다
- B. 기존: firewall 티켓을 한 줄 사유와 함께 not-safety로 라벨링한 예시, 진짜 안전 티켓, 애매한 사례를 포함한 두 개에서 네 개의 예시
  - 신규: firewall 티켓을 한 줄 이유와 함께 안전 문제 아님으로 라벨링한 예시, 실제 안전 티켓 예시, 애매한 경우 예시를 포함해 2~4개의 예시를 넣는다
- C. 기존: 진짜 안전 티켓 예시 스무 개
  - 신규: 실제 안전 티켓 예시를 스무 개 넣는다
- D. 기존: 더 낮은 temperature
  - 신규: temperature를 낮춘다

**해설 EN** Few-shot examples teach reasoning and edge cases best when they include something the model should leave alone, so the tricky negative in B is the example that matters. C piles on positives and teaches nothing about the false positives. A is vague guidance. Temperature (D) changes randomness and leaves the misunderstanding in place.

**해설 기존** few-shot 예시는 모델이 건드리지 말아야 할 것을 포함할 때 추론과 경계 사례를 가장 잘 가르치므로, B의 까다로운 부정 예시가 중요한 예시이다. C는 긍정 예시만 쌓아 오탐에 대해서는 아무것도 가르치지 못한다. A는 모호한 지침이다. temperature(D)는 무작위성을 바꿀 뿐 오해는 그대로 둔다.

**해설 신규** few-shot 예시는 모델이 건드리지 말아야 할 사례를 포함할 때 추론 방식과 경계 사례를 가장 잘 가르친다. 그래서 B의 까다로운 negative 예시가 핵심이다. C는 positive만 쌓아서 오탐에 대해서는 아무것도 가르치지 못한다. A는 모호한 지침이다. temperature(D)는 무작위성을 바꿀 뿐이라 잘못된 이해는 그대로 남는다.

## CCAR-F-preporato-0025

**EN** Your team plans to use structured outputs (a JSON schema in `output_config.format`) for invoice extraction. Which TWO statements about this feature are true? (Select TWO)

**기존** 팀은 송장 추출에 structured outputs(`output_config.format`의 JSON schema)를 사용할 계획이다. 이 기능에 대한 설명 중 참인 두 가지는 무엇인가? (두 개 선택)

**신규** 팀이 송장(invoice) 추출에 structured outputs(`output_config.format`의 JSON schema)를 쓰려고 한다. 이 기능에 대한 설명 중 맞는 것 두 가지는 무엇인가? (2개 선택)

- A. 기존: 추출된 값이 원본 문서에 대해 정확함을 보장한다
  - 신규: 추출된 값이 원본 문서와 일치한다는 것을 보장한다
- B. 기존: `tool_choice`가 특정 도구를 강제할 때만 작동한다
  - 신규: `tool_choice`로 특정 도구를 강제할 때만 작동한다
- C. 기존: 합계가 항목별 금액과 일치하는지 같은 비즈니스 규칙을 검증할 필요가 없어진다
  - 신규: 합계가 항목별 금액과 맞는지 같은 비즈니스 규칙을 검증할 필요가 없어진다
- D. 기존: Constrained decoding은 응답이 schema의 구조와 타입에 맞는 유효한 JSON이 되게 한다
  - 신규: constrained decoding 덕분에 응답이 유효한 JSON이 되고, schema의 구조와 타입에 맞는다
- E. 기존: refusal이나 `max_tokens` 중단은 여전히 schema와 맞지 않는 출력을 낼 수 있으므로 `stop_reason`을 확인해야 한다
  - 신규: 거부(refusal)나 `max_tokens`로 잘린 경우에는 schema에 맞지 않는 출력이 나올 수 있으므로 `stop_reason`을 확인해야 한다

**해설 EN** Structured outputs guarantee format: valid, schema-compliant JSON (D), with the documented exceptions of refusals and truncation (E). Format says nothing about whether the values are right, so semantic checks such as totals and dates stay in your pipeline, which rules out A and C. B confuses the feature with forced tool use; structured outputs are requested through `output_config.format`.

**해설 기존** Structured outputs는 형식을 보장한다. 즉 schema를 준수하는 유효한 JSON(D)이며, 문서에 명시된 예외는 refusal과 잘림(E)이다. 형식은 값이 맞는지에 대해서는 아무 말도 하지 않으므로 합계와 날짜 같은 의미 검사는 파이프라인에 남으며, 따라서 A와 C는 배제된다. B는 이 기능을 강제 tool use와 혼동한 것이며, structured outputs는 `output_config.format`을 통해 요청한다.

**해설 신규** structured outputs가 보장하는 것은 형식이다. 즉 유효하고 schema에 맞는 JSON이며(D), 문서에 명시된 예외는 거부와 잘림이다(E). 형식은 값이 맞는지와 무관하다. 그래서 합계나 날짜 같은 의미 검사는 pipeline에 남겨야 하고, A와 C는 틀린 설명이다. B는 이 기능을 forced tool use와 혼동한 것이다. structured outputs는 `output_config.format`으로 요청한다.

## CCAR-F-preporato-0026

**EN** An extraction fails validation because `invoice_date` came back as 2026-04-31, a date that doesn't exist. What should the retry request contain?

**기존** `invoice_date`가 존재하지 않는 날짜인 2026-04-31로 반환되어 추출이 검증에 실패한다. 재시도 요청에는 무엇이 들어 있어야 하는가?

**신규** 추출 결과가 검증에서 실패했다. `invoice_date`가 존재하지 않는 날짜인 2026-04-31로 나왔기 때문이다. 재시도 요청에는 무엇을 담아야 하는가?

- A. 기존: 실패한 출력과 '다시 시도해 줘'라는 말
  - 신규: 실패한 출력과 '다시 시도하라'는 말
- B. 기존: 다른 변경 없이 원본 문서를 다시
  - 신규: 아무것도 바꾸지 않은 원본 문서
- C. 기존: 원본 문서, 실패한 출력, 구체적인 오류('`invoice_date` 2026-04-31은 유효한 날짜가 아니다'), 그리고 해당 필드만 수정하라는 지시
  - 신규: 원본 문서, 실패한 출력, 구체적인 오류('`invoice_date` 2026-04-31은 유효한 날짜가 아니다'), 그리고 해당 필드만 고치라는 지시
- D. 기존: 같은 요청을 더 유능한 모델에 보내는 것
  - 신규: 같은 요청을 더 성능이 높은 모델로 보내기

**해설 EN** A useful retry tells the model exactly what failed and gives it the source to fix it against (C). B repeats the conditions that produced the error. A removes the source the model needs to correct the date. D changes the model without telling it what went wrong.

**해설 기존** 유용한 재시도는 무엇이 실패했는지를 모델에게 정확히 알려 주고, 그에 맞춰 고칠 수 있는 원본을 제공한다(C). B는 오류를 낳은 조건을 반복한다. A는 모델이 날짜를 고치는 데 필요한 원본을 없앤다. D는 무엇이 잘못되었는지 알려 주지 않고 모델만 바꾼다.

**해설 신규** 쓸모 있는 재시도는 무엇이 실패했는지 모델에게 정확히 알려 주고, 고칠 때 대조할 원본도 함께 준다(C). B는 오류를 낳은 조건을 그대로 반복한다. A는 날짜를 바로잡는 데 필요한 원본을 없앤다. D는 무엇이 잘못됐는지 알려 주지 않은 채 모델만 바꾼다.

## CCAR-F-preporato-0027

**EN** A product team wants to move its live chat assistant to the Message Batches API to cut costs in half. What is the right assessment?

**기존** 한 제품 팀이 비용을 절반으로 줄이기 위해 라이브 채팅 assistant를 Message Batches API로 옮기려 한다. 올바른 평가는 무엇인가?

**신규** 한 제품팀이 비용을 절반으로 줄이려고 실시간 chat assistant를 Message Batches API로 옮기려 한다. 올바른 판단은 무엇인가?

- A. 기존: batch 요청에는 system prompt를 포함할 수 없으므로 거절한다
  - 신규: batch 요청에는 system prompt를 넣을 수 없으니 반려한다
- B. 기존: 승인한다: 같은 품질을 절반 가격에 얻는다
  - 신규: 품질은 같고 가격은 절반이니 승인한다
- C. 기존: 앱이 1초마다 결과를 polling한다는 조건으로 승인한다
  - 신규: 앱이 1초마다 결과를 polling한다는 조건으로 승인한다
- D. 기존: 거절한다: batch에는 지연 시간 보장이 없으므로(대부분 한 시간 이내에 끝나지만 일부는 최대 24시간이 걸린다) 기다리는 사용자를 응대할 수 없다. 비용은 prompt caching이나 일상적인 메시지를 더 저렴한 tier로 라우팅하는 방식으로 줄인다
  - 신규: 반려한다. batch는 지연 시간을 보장하지 않으므로(대부분 한 시간 안에 끝나지만 최대 24시간 걸리는 경우도 있다) 기다리는 사용자를 응대할 수 없다. 비용은 prompt caching이나 일상적인 메시지를 더 저렴한 tier로 라우팅하는 방법으로 줄인다

**해설 EN** The batch discount comes with asynchronous processing and no latency guarantee, which rules it out for anyone waiting on an answer (D). B ignores the latency. Polling (C) doesn't speed up processing. A is false: batch requests take the same parameters as regular Messages requests.

**해설 기존** batch 할인은 비동기 처리와 지연 시간 보장 없음이라는 조건을 동반하므로, 답을 기다리는 사람에게는 쓸 수 없다(D). B는 지연 시간을 무시한다. polling(C)은 처리 속도를 높이지 않는다. A는 거짓이며, batch 요청은 일반 Messages 요청과 같은 파라미터를 받는다.

**해설 신규** batch 할인은 비동기 처리를 전제로 하고 지연 시간이 보장되지 않아서, 답을 기다리는 사람에게는 쓸 수 없다(D). B는 지연 시간을 무시했다. polling(C)을 해도 처리가 빨라지지는 않는다. A는 사실이 아니다. batch 요청은 일반 Messages 요청과 같은 매개변수를 받는다.

## CCAR-F-preporato-0028

**EN** One prompt asks Claude to extract 30 fields from a contract, normalize every currency, classify the risk clauses and write an executive summary. Results vary from run to run, and errors are hard to trace. What is the best restructuring?

**기존** 하나의 프롬프트가 Claude에게 계약서에서 30개 필드를 추출하고, 모든 통화를 정규화하고, 위험 조항을 분류하고, 경영진 요약을 작성하라고 요청한다. 결과가 실행마다 다르고 오류를 추적하기 어렵다. 가장 좋은 재구성은 무엇인가?

**신규** prompt 하나가 Claude에게 계약서에서 필드 30개를 추출하고, 모든 통화를 정규화하고, 위험 조항을 분류하고, 임원용 요약까지 쓰라고 요구한다. 결과가 실행할 때마다 다르고, 오류를 추적하기도 어렵다. 어떻게 재구성하는 것이 가장 좋은가?

- A. 기존: 각자 고유한 지시와 검사를 가진 집중된 프롬프트의 체인(추출, 검증, 정규화, 분류, 요약)
  - 신규: 추출, 검증, 정규화, 분류, 요약처럼 하나씩 집중한 prompt를 chain으로 잇고, 각 prompt에 고유한 지시와 점검을 둔다
- B. 기존: 같은 단일 프롬프트를 더 유능한 모델에서 실행
  - 신규: 같은 prompt 하나를 더 성능이 높은 모델에서 실행한다
- C. 기존: 경영진 요약을 먼저 요청하고 그다음에 필드를 요청
  - 신규: 임원용 요약을 먼저 요청하고 필드를 그다음에 요청한다
- D. 기존: 같은 단일 프롬프트에서 각 요구 사항에 IMPORTANT를 표시
  - 신규: 같은 prompt 하나에서 각 요구 사항에 IMPORTANT 표시를 붙인다

**해설 EN** Prompt chaining gives each stage one job and a validation point, so a failure shows up in the stage that caused it (A). Emphasis (D) doesn't reduce the number of jobs in one prompt. A stronger model (B) may help a little and leaves errors untraceable. Reordering (C) builds the summary on fields nobody has checked yet.

**해설 기존** prompt chaining은 각 단계에 하나의 역할과 검증 지점을 주므로, 실패가 원인이 된 단계에서 드러난다(A). 강조(D)는 하나의 프롬프트 안에 있는 일의 수를 줄이지 못한다. 더 강력한 모델(B)은 조금 도움이 될 수 있지만 오류는 여전히 추적할 수 없다. 순서를 바꾸면(C) 아무도 검사하지 않은 필드 위에 요약이 만들어진다.

**해설 신규** prompt chaining은 각 단계에 일을 하나씩만 맡기고 검증 지점을 두어서, 실패가 그 원인이 된 단계에서 드러난다(A). 강조 표시(D)는 prompt 하나에 든 일의 수를 줄이지 못한다. 더 강한 모델(B)은 조금 도움이 될 수는 있어도 오류 추적은 여전히 안 된다. 순서를 바꾸면(C) 아무도 검증하지 않은 필드를 바탕으로 요약을 만들게 된다.

## CCAR-F-preporato-0029

**EN** A knowledge-base Q&A agent receives 40 retrieved passages per question. The passage with the answer usually lands near the middle, and answers often miss it. Which TWO changes address this? (Select TWO)

**기존** 지식 베이스 Q&A agent가 질문마다 40개의 검색된 passage를 받는다. 답이 들어 있는 passage는 대체로 중간 부근에 놓이고, 답변이 이를 놓치는 경우가 많다. 이를 해결하는 두 가지 변경은 무엇인가? (두 개 선택)

**신규** 지식 베이스 Q&A agent가 질문마다 검색된 passage 40개를 받는다. 답이 든 passage가 대개 중간쯤에 놓이고, 그 때문에 답변이 그 내용을 놓치는 경우가 많다. 이 문제를 해결하는 변경 두 가지는 무엇인가? (2개 선택)

- A. 기존: 40개 대신 80개의 passage를 검색한다
  - 신규: 40개 대신 passage를 80개 검색한다
- B. 기존: passage를 re-rank하고 가장 관련 있는 소수만 전달한다
  - 신규: passage를 re-rank해서 가장 관련 있는 몇 개만 넘긴다
- C. 기존: temperature를 올린다
  - 신규: temperature를 올린다
- D. 기존: passage를 앞에 두고 질문과 지시를 프롬프트 끝에 둔다
  - 신규: passage를 앞에 두고 질문과 지시문을 prompt 끝에 둔다
- E. 기존: 더 큰 context window를 가진 모델로 바꾼다
  - 신규: context window가 더 큰 모델로 바꾼다

**해설 EN** Attention is weakest in the middle of long contexts, so the fixes shrink the middle and move what matters to the edges: fewer, better passages (B), and long material first with the question last, which Anthropic's long-context guidance recommends (D). A bigger window (E) and more passages (A) make the middle longer. Temperature (C) affects randomness and does nothing for attention.

**해설 기존** 주의력은 긴 context의 중간에서 가장 약하므로, 해결책은 중간을 줄이고 중요한 것을 가장자리로 옮기는 것이다. 더 적고 더 좋은 passage(B), 그리고 긴 자료를 앞에 두고 질문을 마지막에 두는 것(D)이며, 후자는 Anthropic의 long-context 가이드가 권장하는 방식이다. 더 큰 window(E)와 더 많은 passage(A)는 중간을 더 길게 만든다. temperature(C)는 무작위성에 영향을 줄 뿐 주의력에는 아무 도움이 되지 않는다.

**해설 신규** 긴 context에서는 중간 부분의 attention이 가장 약하다. 그래서 중간을 줄이고 중요한 내용을 양쪽 끝으로 옮기는 것이 해결책이다. 더 적고 더 좋은 passage를 쓰거나(B), 긴 자료를 앞에 두고 질문을 맨 뒤에 두는 것이다(D). 후자는 Anthropic의 long-context 가이드가 권장하는 방식이다. 더 큰 window(E)나 더 많은 passage(A)는 중간 구간만 더 길게 만든다. temperature(C)는 무작위성에 영향을 줄 뿐 attention과는 관계가 없다.

## CCAR-F-preporato-0030

**EN** Two internal documents disagree about the warranty period: a 2024 policy says 12 months and a 2026 update says 24 months. What should the agent's answer do?

**기존** 두 개의 내부 문서가 보증 기간에 대해 서로 다르게 기술하고 있다. 2024년 정책은 12개월, 2026년 업데이트는 24개월이라고 한다. 에이전트의 답변은 어떻게 해야 하는가?

**신규** 사내 문서 두 개가 보증 기간에 대해 서로 다르게 말한다. 2024년 정책은 12개월이고, 2026년 갱신본은 24개월이다. agent의 답변은 어떻게 해야 하는가?

- A. 기존: 누군가 문서를 수정할 때까지 답변을 거부한다
  - 신규: 누군가 문서를 고칠 때까지 답변을 거부한다
- B. 기존: 최신 문서가 우선한다는 이유로, 충돌을 언급하지 않고 24개월이라고 말한다
  - 신규: 최신 문서가 우선이니 충돌은 언급하지 않고 24개월이라고만 말한다
- C. 기존: 출처를 밝혀 답변한다. 두 값과 각 문서 및 날짜를 제시하고, 더 최신인 값을 현재 유효할 가능성이 높은 것으로 표시하며, 충돌을 검토 대상으로 알린다
  - 신규: 출처를 밝혀 답한다. 두 값과 각 문서, 날짜를 모두 제시하고, 더 최신인 쪽이 현재 기준일 가능성이 높다고 짚어 주며, 충돌이 있다는 점을 검토 대상으로 표시한다
- D. 기존: 두 값을 평균 내어 18개월이라고 말한다
  - 신규: 두 값을 평균 내서 18개월이라고 말한다

**해설 EN** Provenance keeps each claim tied to its source and surfaces conflicts instead of settling them silently (C). Silently picking one value (B) is the tested anti-pattern even when the choice happens to be right, because nobody learns that the documents disagree. D produces a number neither source supports. A withholds an answer the agent can give with a caveat.

**해설 기존** 출처 추적(provenance)은 각 주장을 그 출처에 연결해 두고, 충돌을 조용히 해소하지 않고 드러낸다(C). 한 값을 조용히 선택하는 것(B)은 선택이 우연히 옳더라도 시험에서 다루는 안티패턴인데, 문서들이 서로 다르다는 사실을 아무도 알 수 없게 되기 때문이다. D는 어느 출처도 뒷받침하지 않는 숫자를 만들어 낸다. A는 에이전트가 단서를 달아 제공할 수 있는 답변을 보류한다.

**해설 신규** provenance는 각 주장을 출처에 연결해 두고, 충돌을 조용히 정리해 버리지 않고 드러낸다(C). 값 하나를 조용히 고르는 것(B)은 시험에서 다루는 anti-pattern이다. 우연히 맞는 선택이라 해도 문서끼리 어긋난다는 사실을 아무도 알 수 없기 때문이다. D는 어느 출처도 뒷받침하지 않는 숫자를 만든다. A는 단서를 달아 줄 수 있는 답을 내놓지 않는 것이다.
