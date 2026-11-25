# 한국어 번역 샘플 (원문 ↔ 번역)

## CCAR-P-jrajath94-0351

**[원문]**

A travel agent carries an admin_delete_booking tool. No task deletes bookings. The team proposes monitoring its calls. What is the correct response?

- A. Keep the tool and monitor it.
- B. Remove the tool from the config. Logging is not removal.
- C. Keep the tool but hide it from the docs.
- D. Add a second delete tool for backup.

해설: The decisive phrase is "No task deletes bookings." An unneeded dangerous tool is only an attack surface. Monitoring watches the risk. Removal deletes the risk. The exam rule is blunt. Counterfactual: A wins if you need the tool for incident response. Then it stays watched and gated.

**[번역]**

한 여행 에이전트가 admin_delete_booking 도구를 가지고 있다. 어떤 작업도 예약을 삭제하지 않는다. 팀은 그 도구의 호출을 모니터링하자고 제안한다. 올바른 대응은 무엇인가?

- A. 도구를 유지하고 모니터링한다.
- B. 설정에서 도구를 제거한다. 로깅은 제거가 아니다.
- C. 도구를 유지하되 문서에서 숨긴다.
- D. 백업용으로 두 번째 삭제 도구를 추가한다.

해설: 결정적인 문구는 "어떤 작업도 예약을 삭제하지 않는다"이다. 필요하지 않은 위험한 도구는 공격 표면일 뿐이다. 모니터링은 위험을 지켜본다. 제거는 위험을 없앤다. 시험의 규칙은 직설적이다. 반사실: A는 인시던트 대응에 그 도구가 필요하다면 정답이 된다. 그 경우 도구는 감시되고 gate된 채로 남는다.

## CCAR-P-jrajath94-0046

**[원문]**

Sales promises a client. The support bot will resolve 95 percent of tickets automatically. The pilot data shows 78 percent resolution. The other tickets need humans. People draft the contract now.

Constraint: the SLA in the contract must be achievable and measurable, or the company will pay penalties.

What should the architect do about the SLA?

- A. Refuse the contract entirely.
- B. Accept the 95 percent SLA; the model will improve with more data.
- C. Push back with pilot data: propose a tiered SLA (for example 80 percent auto-resolution with defined response times for the human-handled remainder), measured monthly with a clear definition of "resolved."
- D. Sign the 95 percent SLA but define "resolved" loosely so it is easy to hit.

해설: Why C is correct: The pilot data shows the 95 percent figure is not true. A tiered, measurable SLA uses real numbers. This SLA protects both sides. It has achievable targets. It handles the remainder explicitly. Defining "resolved" exactly prevents gaming.
B is wrong. "will improve" is a hope. It is not a basis for a penalty-bearing contract.
D is wrong. A loosely defined metric is dishonest. It will fail at the first client audit.
A is wrong. It abandons the deal. It does not negotiate an honest SLA.

**[번역]**

영업팀이 고객에게 약속한다. 지원 봇이 티켓의 95퍼센트를 자동으로 해결할 것이라고. 파일럿 데이터는 78퍼센트 해결을 보여 준다. 나머지 티켓은 사람이 필요하다. 지금 사람들이 계약서를 작성하고 있다.

제약 조건: 계약의 SLA는 달성 가능하고 측정 가능해야 하며, 그렇지 않으면 회사가 위약금을 물게 된다.

아키텍트는 SLA에 대해 무엇을 해야 하는가?

- A. 계약을 전면 거절한다.
- B. 95퍼센트 SLA를 수락한다. 데이터가 더 쌓이면 모델이 개선될 것이다.
- C. 파일럿 데이터로 반박한다. 단계별 SLA(예: 80퍼센트 자동 해결, 사람이 처리하는 나머지에 대해서는 정의된 응답 시간)를 제안하고, "해결됨"에 대한 명확한 정의와 함께 매월 측정한다.
- D. 95퍼센트 SLA에 서명하되 쉽게 달성할 수 있도록 "해결됨"을 느슨하게 정의한다.

해설: C가 정답인 이유: 파일럿 데이터는 95퍼센트라는 수치가 사실이 아님을 보여 준다. 단계별이면서 측정 가능한 SLA는 실제 수치를 사용한다. 이 SLA는 양측을 보호한다. 달성 가능한 목표를 가진다. 나머지를 명시적으로 다룬다. "해결됨"을 정확히 정의하면 조작을 방지한다.
B는 오답이다. "개선될 것이다"는 희망이다. 위약금이 따르는 계약의 근거가 아니다.
D는 오답이다. 느슨하게 정의된 지표는 부정직하다. 고객의 첫 감사에서 실패할 것이다.
A는 오답이다. 거래를 포기하는 것이다. 정직한 SLA를 협상하는 것이 아니다.

## CCAR-P-jrajath94-0504

**[원문]**

An HR bot drafts termination letters. A wrong letter
creates legal liability.

Which review shape fits?

- A. Post-action sampled review.
- B. Pre-action approval by HR with the full letter and employee record
shown before anything sends.
- C. No review. The bot is fast.
- D. Annual review.

해설: Decisive phrase: "creates legal liability." Why: consequence plus regulation equals pre-action approval with full
context. A reviews after the liability lands. Counterfactual: A wins
for informational HR FAQs.

**[번역]**

HR 봇이 해고 통지서를 작성한다. 잘못된 통지서는 법적 책임을 초래한다.

어떤 검토 형태가 적합한가?

- A. 사후 작업 표본 검토.
- B. HR의 사전 작업 승인: 무엇이든 발송되기 전에 통지서 전문과 직원 기록이 표시된다.
- C. 검토 없음. 봇은 빠르다.
- D. 연례 검토.

해설: 결정적 문구: "법적 책임을 초래한다." 이유: 결과와 규제가 합쳐지면 전체 컨텍스트를 갖춘 사전 작업 승인이 된다. A는 책임이 발생한 뒤에 검토한다. 반사실: 정보성 HR FAQ에는 A가 정답이 된다.

## CCAR-F-Amey-Thakur-0049

**[원문]**

Which loop gives the most reliable extraction output?

- A. Generate, then manually review every record
- B. Generate three times and take the majority
- C. Enforce a JSON schema through tool use, validate, and on failure retry with the validation error provided to the model
- D. Generate with temperature zero and accept the result

해설: Schema enforcement plus a validation-retry loop is the reliability pattern the guide describes

**[번역]**

어떤 루프가 가장 신뢰할 수 있는 추출 출력을 제공하는가?

- A. 생성한 다음 모든 레코드를 수동으로 검토한다
- B. 세 번 생성하고 다수결로 택한다
- C. tool use를 통해 JSON 스키마를 강제하고, 검증하고, 실패 시 검증 오류를 모델에 제공하여 재시도한다
- D. temperature 0으로 생성하고 결과를 받아들인다

해설: 스키마 강제와 검증-재시도 루프가 가이드에서 설명하는 신뢰성 패턴이다

## CCAR-F-paullarionov-0049

**[원문]**

Your agent achieves 55% first-contact resolution, well below the 80% target. Logs show it escalates simple cases (standard replacements for damaged goods with photo proof) while trying to handle complex situations requiring policy exceptions autonomously. What is the most effective way to improve escalation calibration?

What is the most effective way to improve escalation calibration?

- A. Require the agent to self-rate confidence on a 1–10 scale before each response and automatically route to humans when confidence drops below a threshold.
- B. Deploy a separate classifier model trained on historical tickets to predict which requests need escalation before the main agent starts processing.
- C. Add explicit escalation criteria to the system prompt with few-shot examples showing when to escalate versus resolve autonomously.
- D. Implement sentiment analysis to determine customer frustration level and automatically escalate past a negative sentiment threshold.

해설: Explicit escalation criteria with few-shot examples directly address the root cause—unclear decision boundaries between simple and complex cases. It’s the most proportional, effective first intervention that teaches the agent when to escalate and when to resolve autonomously without extra infrastructure.

**[번역]**

agent의 first-contact resolution이 55%로, 목표인 80%에 크게 못 미친다. 로그를 보면 agent는 단순한 사례(사진 증빙이 있는 파손 상품의 표준 교환)는 escalate하면서, 정책 예외가 필요한 복잡한 상황은 자율적으로 처리하려고 한다. escalation 보정을 개선하는 가장 효과적인 방법은 무엇인가?

escalation 보정을 개선하는 가장 효과적인 방법은 무엇인가?

- A. agent가 각 응답 전에 1~10 척도로 신뢰도를 스스로 평가하게 하고, 신뢰도가 임계값 아래로 떨어지면 자동으로 사람에게 라우팅한다.
- B. 메인 agent가 처리를 시작하기 전에 어떤 요청이 escalation이 필요한지 예측하도록 과거 티켓으로 학습된 별도의 classifier 모델을 배포한다.
- C. 언제 escalate하고 언제 자율적으로 해결해야 하는지 보여 주는 few-shot 예시와 함께 명시적인 escalation 기준을 시스템 프롬프트에 추가한다.
- D. 감정 분석을 구현하여 고객의 불만 수준을 판단하고 부정적 감정 임계값을 넘으면 자동으로 escalate한다.

해설: few-shot 예시를 곁들인 명시적인 escalation 기준은 근본 원인, 즉 단순한 사례와 복잡한 사례 사이의 불분명한 판단 경계를 직접 해결한다. 추가 인프라 없이 agent에게 언제 escalate하고 언제 자율적으로 해결해야 하는지 가르치는, 가장 적절한 규모의 효과적인 첫 개입이다.

## CCAR-F-Udemy02-0060

**[원문 해설(일본어)]**

Claude Codeのサブエージェントは原則として新しいコンテキストで起動し、親の会話履歴を見ません。公式ドキュメントも、親からサブエージェントに渡るのは委任時のプロンプト文字列だけなので、必要なファイルパスやエラーメッセージ、判断はそのプロンプトに直接含めるよう説明しています。例外がforkで、親の会話をそのまま引き継いで分岐します。

したがって、PR固有の証拠をプロンプトに明示して渡すことと、forkで委任することの2つが正解です。前者は継承に頼らずに情報を渡す方法、後者は継承そのものを使う方法という違いがあります。

誤答はどちらも「通常のサブエージェントでも親の文脈や過去のトランスクリプトに届く」という前提に立っており、その前提が成り立ちません。

サブエージェントの設問では、委任先が起動時に何を持っているかを先に確認すると正誤を判断しやすくなります。

보기별: A: 正解。forkは親の会話全体（システムプロンプト、ツール、メッセージ履歴）を引き継いで起動するサブエージェントです。メインセッションが読んだ変更ファイルや失敗したテストの文脈を持ったままレビューでき、途中のツール呼び出しはforkの中にとど… / B: 必要な情報をサブエージェント自身に取りに行かせる設計は、ファイルやログのように共有された場所にある情報なら成り立ちます。しかし通常のサブエージェントには親の会話履歴を読む手段がなく、受け取るのは委任時のプロンプト文字列だけなので、指示しても…

**[번역 해설]**

Claude Code의 서브에이전트는 원칙적으로 새로운 컨텍스트에서 시작하며 부모의 대화 기록을 보지 못합니다. 공식 문서에서도 부모에서 서브에이전트로 전달되는 것은 위임 시의 프롬프트 문자열뿐이므로, 필요한 파일 경로나 에러 메시지, 판단은 그 프롬프트에 직접 포함하도록 설명하고 있습니다. 예외가 fork이며, 부모의 대화를 그대로 이어받아 분기합니다.

따라서 PR 고유의 증거를 프롬프트에 명시하여 전달하는 것과 fork로 위임하는 것, 이 2가지가 정답입니다. 전자는 상속에 의존하지 않고 정보를 전달하는 방법이고, 후자는 상속 자체를 사용하는 방법이라는 차이가 있습니다.

오답은 둘 다 "일반 서브에이전트라도 부모의 문맥이나 과거의 트랜스크립트에 접근할 수 있다"는 전제에 서 있으며, 그 전제는 성립하지 않습니다.

서브에이전트 문제에서는 위임받은 쪽이 시작 시점에 무엇을 가지고 있는지를 먼저 확인하면 정오를 판단하기 쉽습니다.

보기별: A: 정답입니다. fork는 부모의 대화 전체(시스템 프롬프트, 도구, 메시지 이력)를 이어받아 시작하는 서브에이전트입니다. 메인 세션이 읽은 변경 파일이나 실패한 테스트의 문맥을 가진 채로 리뷰할 수 있고, 도중의 도구… / B: 필요한 정보를 서브에이전트 스스로 가져오게 하는 설계는 파일이나 로그처럼 공유된 장소에 있는 정보라면 성립합니다. 그러나 일반 서브에이전트에는 부모의 대화 이력을 읽을 수단이 없고 받는 것은 위임 시의 프롬프트 문자…

## CCAR-F-Udemy01-0060

**[원문 해설(일본어)]**

エスカレーションの設計では、何をきっかけに人へ引き継ぐかを明確に決めておくことが重要です。Anthropicのエージェント設計ガイドは、エージェントが判断に迷う場面や人の確認が必要な場面で処理を止め、人間のフィードバックを受けられるチェックポイントを設けることを勧めています。

本問では、ユーザーが明示的に人の対応を求めたケースと、元の文書から確実に直せる単純な修正依頼という、性質の違う2つの入力が示されています。前者は内容の難易度に関係なく人へ回し、後者には自動修復を用意したうえで、修復後も検証に失敗したら人へ引き継ぐ、という組み合わせが要件に合います。

不満度のスコアや抽出の難易度で判断する案は、明示的な要求という最も確かなシグナルを別の基準に置き換えてしまいます。

ユーザーがはっきり意思表示している場面では、推測による判定を挟まないことが原則です。

보기별: A: 不満度の推定は、明示的な要求がない会話で対応の優先度を付ける補助指標としては使えることがあります。しかし「人に対応してほしい」と書かれた依頼をスコアで判定し直すと、しきい値に届かない限り明確な要求が無視され、パイロットで見つかった問題をその… / B: 正解。自動修復を「人間対応を求めていない依頼」に限定し、修復してもスキーマ検証に通らないものはエスカレーションに回すことで、申請者の明示的な希望を尊重しながら、自動では解決できなかったケースを確実に人へ引き継げます。検証失敗を自動処理の打ち…

**[번역 해설]**

에스컬레이션 설계에서는 무엇을 계기로 사람에게 인계할지를 명확히 정해 두는 것이 중요합니다. Anthropic의 에이전트 설계 가이드는, 에이전트가 판단이 망설여지는 장면이나 사람의 확인이 필요한 장면에서 처리를 멈추고 사람의 피드백을 받을 수 있는 체크포인트를 두도록 권장합니다.

이 문제에서는 사용자가 명시적으로 사람의 대응을 요구한 경우와, 원본 문서에서 확실하게 고칠 수 있는 단순한 수정 요청이라는 성격이 다른 두 입력이 제시되어 있습니다. 전자는 내용의 난이도와 관계없이 사람에게 넘기고, 후자에는 자동 복구를 마련한 뒤 복구 후에도 검증에 실패하면 사람에게 인계하는 조합이 요건에 맞습니다.

불만도 점수나 추출 난이도로 판단하는 안은, 명시적 요구라는 가장 확실한 신호를 다른 기준으로 바꿔 버립니다.

사용자가 분명하게 의사를 표시한 장면에서는 추측에 의한 판정을 끼워 넣지 않는 것이 원칙입니다.

보기별: A: 불만도 추정은, 명시적 요구가 없는 대화에서 대응 우선순위를 매기는 보조 지표로는 쓸 수 있는 경우가 있습니다. 그러나 "사람이 대응해 주길 바란다"고 적힌 요청을 점수로 다시 판정하면, 임계값에 닿지 않는 한 명확… / B: 정답입니다. 자동 복구를 "사람 대응을 요구하지 않은 요청"으로 한정하고, 복구해도 스키마 검증을 통과하지 못하는 것은 에스컬레이션으로 돌리면, 신청자의 명시적 희망을 존중하면서 자동으로는 해결하지 못한 케이스를 확…

## CCDV-F-Udemy-0009

**[원문 해설(일본어)]**

A. 例示は形式や方針を伝えるのに有効ですが、公式ドキュメントが勧める目安は3〜5件で、関連性と多様性のある例を選ぶことが重要です。数十件の計画例はコンテキストを圧迫するうえ、例の表面的なパターンをなぞらせるおそれがあり、多数の制約を突き合わせる推論そのものの代わりにはなりません。
B. 正解。フューショットプロンプティング（マルチショット）は出力の形式・トーン・構造を安定させる最も確実な手段の1つで、固定カテゴリへの分類なら数件の代表例で書式と判断の境界を示せます。 一方、相互に影響する制約を突き合わせる計画立案は多段階の推論が価値を生む典型で、適応型思考ではエフォートを上げるとClaudeがより積極的かつ深く考えるようになります。タスクごとに手段を割り当てれば、品質とコスト・レイテンシの釣り合いが取れます。
C. 指示だけのゼロショットと低いエフォートの組み合わせは、単純な問い合わせを大量に速く処理したい場面では妥当な設定です。しかし分類では例がないと出力形式やカテゴリの境界がぶれやすく、計画立案では推論を抑えることで制約の見落としが起きやすくなるため、どちらのタスクの要件にも合いません。
D. エフォートをmaxにすると、Claudeは最も積極的かつ深く考えるようになり、難しい推論では品質の向上が期待できます。ただし考えた分は出力トークンとして課金され、レイテンシも延びるため、形式が決まった単純な分類にまで適用するのは費用対効果に見合いません。

フューショットプロンプティングによる例示は「どんな形で答えるか」を伝える手段で、固定カテゴリへの分類のように答えの形と判断基準が明確なタスクで効果を発揮します。思考モードは「どれだけ考えてから答えるか」を調整する手段です。現行モデルでは適応型思考が標準で、Claudeがリクエストごとに考えるかどうかと深さを判断し、その傾向をエフォート（lowからmaxまで）で方向づけます。
なお以前の拡張思考（budget_tokensで思考量を固定する方式）は、Claude Opus 4.7以降のモデルでは受け付けられません。思考に使ったトークンは出力として課金されるため、推論が品質を左右するタスクに絞って深く考えさせるのが基本です。
誤答は、全タスクで推論を抑える、例示を推論の代わりにする、全タスクで推論を最大化する、といった一律の設定になっており、タスクの性質に合わせて手段を割り当てるという問題の核心から外れています。

**[번역 해설]**

A. 예시는 형식이나 방침을 전달하는 데 유효하지만, 공식 문서가 권장하는 기준은 3~5개이며 관련성과 다양성이 있는 예시를 고르는 것이 중요합니다. 수십 개의 계획 예시는 컨텍스트를 압박할 뿐 아니라 예시의 표면적인 패턴을 따라 하게 할 우려가 있으며, 다수의 제약을 대조하는 추론 자체를 대신하지 못합니다.
B. 정답입니다. 퓨샷 프롬프팅(멀티샷)은 출력의 형식·톤·구조를 안정시키는 가장 확실한 수단 중 하나로, 고정 카테고리로의 분류라면 몇 개의 대표 예시로 서식과 판단의 경계를 보여 줄 수 있습니다. 한편 서로 영향을 주는 제약을 대조하는 계획 수립은 다단계 추론이 가치를 만드는 전형적인 경우이며, 적응형 사고에서는 effort를 높이면 Claude가 더 적극적이고 깊이 생각하게 됩니다. 작업별로 수단을 할당하면 품질과 비용·지연 시간의 균형이 맞춰집니다.
C. 지시만 주는 제로샷과 낮은 effort의 조합은 단순한 문의를 대량으로 빠르게 처리하고 싶은 상황에서는 타당한 설정입니다. 그러나 분류에서는 예시가 없으면 출력 형식이나 카테고리의 경계가 흔들리기 쉽고, 계획 수립에서는 추론을 억제함으로써 제약을 놓치기 쉬워지므로 어느 작업의 요건에도 맞지 않습니다.
D. effort를 max로 하면 Claude는 가장 적극적이고 깊이 생각하게 되어 어려운 추론에서는 품질 향상을 기대할 수 있습니다. 다만 생각한 만큼이 출력 토큰으로 과금되고 지연 시간도 늘어나므로, 형식이 정해진 단순한 분류에까지 적용하는 것은 비용 대비 효과에 맞지 않습니다.

퓨샷 프롬프팅에 의한 예시는 "어떤 형태로 답할 것인가"를 전달하는 수단으로, 고정 카테고리로의 분류처럼 답의 형태와 판단 기준이 명확한 작업에서 효과를 발휘합니다. 사고 모드는 "얼마나 생각한 뒤에 답할 것인가"를 조정하는 수단입니다. 현행 모델에서는 적응형 사고가 표준이며, Claude가 요청마다 생각할지 여부와 깊이를 판단하고, 그 경향을 effort(low에서 max까지)로 방향 짓습니다.
또한 이전의 확장 사고(budget_tokens로 사고량을 고정하는 방식)는 Claude Opus 4.7 이후 모델에서는 받아들여지지 않습니다. 사고에 사용한 토큰은 출력으로 과금되므로, 추론이 품질을 좌우하는 작업으로 한정하여 깊이 생각하게 하는 것이 기본입니다.
오답은 모든 작업에서 추론을 억제한다, 예시를 추론 대신으로 삼는다, 모든 작업에서 추론을 최대화한다와 같이 일률적인 설정으로 되어 있어, 작업의 성격에 맞춰 수단을 할당한다는 문제의 핵심에서 벗어나 있습니다.
