## CCAR-F-Udemy01-0001

**JA** ある消費財メーカーは、Claude Agent SDKを使用してマルチエージェントの市場調査システムを構築しています。コーディネーターが、市場調査・文書分析・統合・レポート生成をそれぞれ担当する専門サブエージェントに作業を委任しています。

このチームは、競合価格分析レポートを作成するための長大なチェックリストを、ルートのメモリファイルに追加しました。チェックリストは、出典の選別手順、価格帯のグルーピング、引用の書式、最終レポートの組み立てを段階的に記した手順書です。しかし、この手順はごく一部のリサーチタスクにしか関係がありません。

開発者たちは、無関係なClaude Codeセッションまでもが、この専門的な手順をコンテキストとして読み込んでいることに気づきました。

このチームが取るべき対応として、最も適切なものはどれですか。

**KO** 한 소비재 제조사는 Claude Agent SDK를 사용해 multi-agent 시장 조사 시스템을 구축하고 있습니다. coordinator가 시장 조사, 문서 분석, 통합, 보고서 생성을 각각 담당하는 전문 subagent에게 작업을 위임합니다.

이 팀은 경쟁사 가격 분석 보고서를 작성하기 위한 긴 체크리스트를 루트 메모리 파일에 추가했습니다. 체크리스트는 출처 선별 절차, 가격대 그룹화, 인용 형식, 최종 보고서 구성을 단계별로 적은 절차서입니다. 하지만 이 절차는 극히 일부 리서치 작업에만 관련이 있습니다.

개발자들은 관련 없는 Claude Code session에서도 이 전문 절차가 context로 로드되고 있다는 사실을 알아차렸습니다.

이 팀이 취해야 할 조치로 가장 적절한 것은 무엇입니까?

- A. JA: チェックリストを、各項目が完了するまでレポート生成をブロックするPreToolUseフックに置き換える。
  - KO: 체크리스트를, 각 항목이 완료될 때까지 보고서 생성을 차단하는 PreToolUse hook으로 대체합니다.
  - EN: Replace the checklist with a PreToolUse hook that blocks report generation until each item is completed.
- B. JA: 引用・出典管理のルールも含めて手順全体をスキルに移し、CLAUDE.mdは空にする。
  - KO: 인용·출처 관리 규칙까지 포함해 절차 전체를 skill로 옮기고, CLAUDE.md는 비웁니다.
  - EN: Move the entire procedure, including the citation and source management rules, into a skill, and leave CLAUDE.md empty.
- C. JA: 競合価格分析の手順はSKILL.mdのスキルに移し、CLAUDE.mdには全タスクに共通する規約だけを残す。
  - KO: 경쟁사 가격 분석 절차는 SKILL.md의 skill로 옮기고, CLAUDE.md에는 모든 작업에 공통되는 규약만 남깁니다.
  - EN: Move the competitive pricing analysis procedure into a skill defined in SKILL.md, and leave only the conventions common to all tasks in CLAUDE.md.
- D. JA: 競合価格分析の手順全体をCLAUDE.mdに残したまま、関係しないときは無視するよう注記を加える。
  - KO: 경쟁사 가격 분석 절차 전체를 CLAUDE.md에 그대로 둔 채, 관련이 없을 때는 무시하라는 주석을 추가합니다.
  - EN: Keep the entire competitive pricing analysis procedure in CLAUDE.md and add a note telling Claude to ignore it when it is not relevant.

## CCAR-F-Udemy01-0002

**JA** あるチームは、社内のコードベース調査や定型的なリファクタリングを自動化するために、Claude Agent SDKをベースにしたエンジニアリング支援エージェントを構築しています。このエージェントは、組み込みツール（Read、Write、Bash、Grep、Glob）に加えて、複数のMCPサーバーと連携します。

試験運用中、エンジニアが「ワークスペース内を丸ごと整理して」といったあいまいなクリーンアップ依頼を出すと、エージェントがワークスペース外のパスまで変更するBashコマンドを実行してしまうことがありました。

ワークスペースの境界を越えないことは、絶対に譲れないルールです。次の2点を満たす必要があります。

ワークスペース外を対象とするコマンドは、実行前に必ず停止させる

その違反についてのフィードバックを、Claudeに返す

このチームが行うべき変更はどれですか。

**KO** 한 팀은 사내 코드베이스 조사와 정형화된 refactoring을 자동화하기 위해 Claude Agent SDK 기반의 엔지니어링 지원 agent를 구축하고 있습니다. 이 agent는 내장 도구(Read, Write, Bash, Grep, Glob)와 함께 여러 MCP server와 연동합니다.

시범 운영 중에 엔지니어가 "워크스페이스 안을 통째로 정리해 줘" 같은 모호한 정리 요청을 하면, agent가 워크스페이스 밖의 경로까지 변경하는 Bash 명령을 실행하는 일이 있었습니다.

워크스페이스 경계를 넘지 않는 것은 절대 양보할 수 없는 규칙입니다. 다음 두 가지를 만족해야 합니다.

워크스페이스 밖을 대상으로 하는 명령은 실행 전에 반드시 중단시킵니다

그 위반에 대한 피드백을 Claude에게 돌려줍니다

이 팀이 해야 할 변경은 무엇입니까?

- A. JA: ワークスペース外のコマンドをログに記録するだけで、ブロックはしないPreToolUseコマンドフックを追加する。
  - KO: 워크스페이스 밖의 명령을 로그에 기록만 하고 차단하지는 않는 PreToolUse command hook을 추가합니다.
  - EN: Add a PreToolUse command hook that only logs commands outside the workspace without blocking them.
- B. JA: 対象パスを検証し、ワークスペース外のコマンドを理由付きでブロックするPreToolUseフックを追加する。
  - KO: 대상 경로를 검증해, 워크스페이스 밖의 명령을 이유와 함께 차단하는 PreToolUse hook을 추가합니다.
  - EN: Add a PreToolUse hook that validates the target paths and blocks commands outside the workspace, with a stated reason.
- C. JA: Bashコマンドを一つずつ確認してワークスペース外のパスを避けるよう、システムプロンプトの指示を強める。
  - KO: Bash 명령을 하나씩 확인해 워크스페이스 밖의 경로를 피하도록 system prompt의 지시를 강화합니다.
  - EN: Strengthen the system prompt instructions so that Claude checks each Bash command one by one and avoids paths outside the workspace.
- D. JA: Bashの変更をPostToolUseコマンドフックで検知し、Claudeに元に戻すよう依頼するフックを追加する。
  - KO: Bash의 변경을 PostToolUse command hook으로 감지해, Claude에게 되돌리도록 요청하는 hook을 추가합니다.
  - EN: Add a PostToolUse command hook that detects Bash changes and asks Claude to revert them.

## CCAR-F-Udemy01-0003

**JA** ある気候研究コンソーシアムは、Claudeを使用して、長大な観測レポートから情報を抽出する構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持する必要があります。エッジケースを適切に処理し、下流のシステムと連携する必要もあります。

研究チームは、長い文書を分割し、複数の抽出サブエージェントに処理させています。検証の過程で、統合エージェントが抽出された複数の統計値を1つの傾向としてまとめてしまいました。レビュー担当者は後になって、2つの値が実際には比較できない条件で得られたものだったことに気づきました。

ログを見ると、各抽出サブエージェントは関連する知見の簡潔な文章要約を返していました。

統合の信頼性を最も直接的に改善する変更はどれですか。（2つ選択してください。）

**KO** 한 기후 연구 컨소시엄은 Claude를 사용해, 방대한 관측 보고서에서 정보를 추출하는 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지해야 합니다. edge case를 적절히 처리하고 downstream 시스템과 연동해야 합니다.

연구팀은 긴 문서를 나눠 여러 추출 subagent가 처리하게 하고 있습니다. 검증 과정에서 통합 agent가 추출된 여러 통계값을 하나의 추세로 묶어 버렸습니다. 리뷰 담당자는 나중에서야 두 값이 실제로는 비교할 수 없는 조건에서 얻은 것이었다는 사실을 알아차렸습니다.

로그를 보면 각 추출 subagent는 관련 발견 사항을 간결한 문장으로 요약해 반환했습니다.

통합의 신뢰성을 가장 직접적으로 개선하는 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 全文書から抽出したテキストを丸ごと統合エージェントに送り、出所の情報をそこから独自に再構築させる。
  - KO: 모든 문서에서 추출한 텍스트를 통째로 통합 agent에 보내, 출처 정보를 거기서 스스로 재구성하게 합니다.
  - EN: Send the full extracted text from all documents to the synthesis agent and have it reconstruct provenance information on its own.
- B. JA: 各抽出サブエージェントをforkとして実行し、要約を返す前に親の会話を引き継がせる。
  - KO: 각 추출 subagent를 fork로 실행해, 요약을 반환하기 전에 부모 대화를 이어받게 합니다.
  - EN: Run each extraction subagent as a fork so that it inherits the parent conversation before returning its summary.
- C. JA: 値をまとめる前に、各サブエージェントのレコードに観測期間と測定方法が入っているかを検証する。
  - KO: 값을 묶기 전에, 각 subagent의 레코드에 관측 기간과 측정 방법이 들어 있는지 검증합니다.
  - EN: Before combining values, verify that each subagent's record includes the observation period and measurement method.
- D. JA: 主張と出典位置、取得条件を含む構造化された根拠レコードを各サブエージェントに返させる。
  - KO: 주장과 출처 위치, 획득 조건을 포함하는 구조화된 근거 레코드를 각 subagent가 반환하게 합니다.
  - EN: Have each subagent return a structured evidence record that includes the claim, the source location, and the acquisition conditions.

## CCAR-F-Udemy01-0004

**JA** ある航空会社の乗務員スケジューリングシステム改修チームは、Claude Codeを使って数時間に及ぶ調査作業を行っています。Claude Codeは、序盤にレガシーなスケジューリング依存関係をいくつか正しく特定しました。

しかし、多数のファイル読み込みや検索、コンパクション（会話履歴の圧縮）を経た後、後続の回答ではそれらの依存関係への言及が抜け落ち始めました。具体的な調査結果ではなく、よくあるパターンを答えるようになっています。

後続の質問に備えて調査の状態を保つ変更として、最も効果的なものはどれですか。

**KO** 한 항공사의 승무원 스케줄링 시스템 개편 팀은 Claude Code로 몇 시간에 걸친 조사 작업을 하고 있습니다. Claude Code는 초반에 레거시 스케줄링 의존 관계 몇 가지를 정확히 찾아냈습니다.

그러나 수많은 파일 읽기와 검색, compaction(대화 기록 압축)을 거친 뒤로는 이후 답변에서 그 의존 관계에 대한 언급이 빠지기 시작했습니다. 구체적인 조사 결과 대신 흔한 패턴을 답하게 된 것입니다.

이후 질문에 대비해 조사 상태를 유지하는 변경으로 가장 효과적인 것은 무엇입니까?

- A. JA: 改修作業をプランモードに切り替え、以前のファイル分析の詳細はそのプランが保持してくれることに頼る。
  - KO: 개편 작업을 plan mode로 전환하고, 이전 파일 분석의 세부 내용은 그 plan이 유지해 줄 것이라고 기대합니다.
  - EN: Switch the modernization work to plan mode and rely on the plan to retain the details of the earlier file analysis.
- B. JA: 確認済みの依存関係をinvestigation-notes.mdに記録させ、後続の質問の前に読み込ませる。
  - KO: 확인된 의존 관계를 investigation-notes.md에 기록하게 하고, 이후 질문 전에 읽어 들이게 합니다.
  - EN: Have Claude record the confirmed dependencies in investigation-notes.md and read it before later questions.
- C. JA: /compactに依存関係を残すよう焦点の指示を渡し、要約の中に調査結果を含めさせる。
  - KO: /compact에 의존 관계를 남기라는 초점 지시를 전달해, 요약 안에 조사 결과를 포함시킵니다.
  - EN: Pass focus instructions to /compact to preserve the dependencies, so that the summary includes the investigation findings.
- D. JA: セッション開始時の指示を長くし、特定した依存関係を一つ残らず覚えておくようClaudeに伝える。
  - KO: session 시작 시의 지시를 길게 늘려, 찾아낸 의존 관계를 하나도 빠짐없이 기억하라고 Claude에게 전달합니다.
  - EN: Lengthen the instructions at the start of the session and tell Claude to remember every identified dependency.

## CCAR-F-Udemy01-0005

**JA** あるチームは、Claude Agent SDKを使用して、複数のサブエージェントを統括するマルチエージェントの市場調査システムを構築しています。コーディネーターエージェントは、専門化されたサブエージェント（Web検索担当、資料分析担当、知見の統合担当、レポート生成担当）に作業を委任します。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

評価中、Web検索サブエージェントが、いくつかの有用な情報源を見つけた後で一時的なネットワークエラーに遭遇することがありました。その際、コーディネーターには汎用的な失敗メッセージしか渡されず、レポート生成を止めるか、その節を省略するかのどちらかになってしまいます。

サブエージェントの分離を保ちながら、レジリエンスを最も改善する変更はどれですか。

**KO** 한 팀은 Claude Agent SDK를 사용해 여러 subagent를 총괄하는 multi-agent 시장 조사 시스템을 구축하고 있습니다. coordinator agent는 전문화된 subagent(웹 검색 담당, 자료 분석 담당, 발견 사항 통합 담당, 보고서 생성 담당)에게 작업을 위임합니다. 이 시스템은 주제를 조사하고 출처를 명시한 포괄적인 보고서를 작성합니다.

평가 중에 웹 검색 subagent가 유용한 정보원 몇 개를 찾은 뒤 일시적인 네트워크 오류를 만나는 경우가 있었습니다. 이때 coordinator에는 일반적인 실패 메시지만 전달되어, 보고서 생성을 멈추거나 해당 절을 생략하는 둘 중 하나로 끝나 버립니다.

subagent의 격리를 유지하면서 회복력(resilience)을 가장 크게 개선하는 변경은 무엇입니까?

- A. JA: コーディネーターに検索サブエージェントの中間的なツール呼び出しを検査させ、リトライするか部分的な情報源のまま続行するかを判断させる。
  - KO: coordinator가 검색 subagent의 중간 도구 호출을 검사해, 재시도할지 일부 정보원만으로 계속할지 판단하게 합니다.
  - EN: Have the coordinator inspect the search subagent's intermediate tool calls and decide whether to retry or continue with partial sources.
- B. JA: 検索が失敗するたびに検索サブエージェントに空の成功結果を返させ、統合エージェントにカバレッジの欠落を推測させる。
  - KO: 검색이 실패할 때마다 검색 subagent가 빈 성공 결과를 반환하게 하고, 통합 agent가 빠진 범위를 추측하게 합니다.
  - EN: Have the search subagent return an empty success result whenever a search fails, and have the synthesis agent infer the coverage gaps.
- C. JA: 検索サブエージェント内で一時的な失敗をリトライさせ、解決しなければエラー内容と取得済みの情報源を返させる。
  - KO: 검색 subagent 안에서 일시적인 실패를 재시도하게 하고, 해결되지 않으면 오류 내용과 이미 확보한 정보원을 반환하게 합니다.
  - EN: Have the search subagent retry transient failures internally and, if they remain unresolved, return the error details along with the sources already retrieved.
- D. JA: 検索サブエージェントに親のツールを継承させ、主要な検索経路が失敗するたびに別のツールで代替させる。
  - KO: 검색 subagent가 부모의 도구를 상속받게 하고, 주요 검색 경로가 실패할 때마다 다른 도구로 대체하게 합니다.
  - EN: Have the search subagent inherit the parent's tools and substitute a different tool whenever the primary search path fails.

## CCAR-F-Udemy01-0006

**JA** あなたは、Claudeを使用して自動請求書処理システムを構築しています。このシステムは、非構造化のスキャン文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携する必要があります。

Claudeがstop_reasonとして"tool_use"を返し、同じassistantターンの中に2つのvalidate_invoiceツール呼び出し（tool_useブロック）を含めてきました。あなたのラッパーは、両方のバリデーターを実行した後、その結果を要約したプレーンテキストのユーザーメッセージだけを含む新しいリクエストを開始しています。

Claudeが次の抽出アクションについて正しく推論できるようにするために、ラッパーが代わりに行うべきことはどれですか。

**KO** 당신은 Claude를 사용해 자동 청구서 처리 시스템을 구축하고 있습니다. 이 시스템은 비구조화 스캔 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동해야 합니다.

Claude가 stop_reason으로 "tool_use"를 반환하면서, 같은 assistant turn 안에 validate_invoice 도구 호출(tool_use 블록) 2개를 포함했습니다. 당신의 wrapper는 두 validator를 모두 실행한 뒤, 그 결과를 요약한 일반 텍스트 user 메시지만 담은 새 요청을 시작하고 있습니다.

Claude가 다음 추출 작업을 올바르게 추론할 수 있도록, wrapper가 대신 해야 할 일은 무엇입니까?

- A. JA: tool_useを含むassistant応答を履歴に残し、tool_use_idで対応付けた2つのtool_resultを1つのuserメッセージで返す。
  - KO: tool_use가 담긴 assistant 응답을 기록에 남기고, tool_use_id로 대응시킨 tool_result 2개를 하나의 user 메시지로 반환합니다.
  - EN: Keep the assistant response containing the tool_use blocks in the history, and return the two tool_result blocks, matched by tool_use_id, in a single user message.
- B. JA: tool_resultを送る前に、バリデーターの出力を要約した新しいuserテキストメッセージを追加してから続ける。
  - KO: tool_result를 보내기 전에, validator 출력을 요약한 새 user 텍스트 메시지를 추가한 뒤 계속합니다.
  - EN: Before sending the tool_result blocks, add a new user text message summarizing the validator output, and then continue.
- C. JA: 両方のバリデーターの出力を、tool_use_idで対応付けたtool_resultブロックとして1つのassistantメッセージに入れて追加する。
  - KO: 두 validator의 출력을 tool_use_id로 대응시킨 tool_result 블록으로 만들어, 하나의 assistant 메시지에 넣어 추가합니다.
  - EN: Add the outputs of both validators as tool_result blocks, matched by tool_use_id, in a single assistant message.
- D. JA: 後続のuserメッセージを2つ追加し、それぞれに対応するtool_resultブロックを1つずつ入れて送る。
  - KO: 이어지는 user 메시지 2개를 추가하고, 각각에 대응하는 tool_result 블록을 하나씩 넣어 보냅니다.
  - EN: Send two subsequent user messages, each containing one corresponding tool_result block.

## CCAR-F-Udemy01-0007

**JA** データパイプラインの保守作業を加速するために、Claude Codeを使用しています。チームでは、コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行をどのように使い分けるかを理解する必要があります。

カスタムの/resolve-incidentコマンドは、コードを編集してコミットメッセージを生成する前に、インシデント検索用のMCPツールを使います。テストでは、インシデントのタイトル検索で類似したインシデントが複数返った場合に、Claude Codeが最新のインシデントをそのまま採用し、誤った内容を実装してしまうことがあります。

信頼性を改善するためにこのチームが行うべき変更はどれですか。（2つ選択してください。）

**KO** 데이터 pipeline 유지보수 작업을 빠르게 하기 위해 Claude Code를 사용하고 있습니다. 팀에서는 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 씁니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하고, plan mode와 직접 실행을 어떻게 구분해 쓸지 이해해야 합니다.

custom /resolve-incident 명령은 코드를 편집하고 commit 메시지를 생성하기 전에 인시던트 검색용 MCP 도구를 사용합니다. 테스트에서 인시던트 제목 검색으로 비슷한 인시던트가 여러 개 반환되면, Claude Code가 가장 최근 인시던트를 그대로 채택해 잘못된 내용을 구현하는 경우가 있습니다.

신뢰성을 개선하기 위해 이 팀이 해야 할 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 一致するインシデントが複数あるときはタイトルの類似度を優先して選ぶよう、CLAUDE.mdを更新する。
  - KO: 일치하는 인시던트가 여러 개일 때는 제목 유사도를 우선해 고르도록 CLAUDE.md를 업데이트합니다.
  - EN: Update CLAUDE.md to prioritize title similarity when multiple incidents match.
- B. JA: 検索ツールの説明を更新し、候補のインシデントが複数返ったときは作業前に確認を求めさせる。
  - KO: 검색 도구의 설명을 업데이트해, 후보 인시던트가 여러 개 반환되면 작업 전에 확인을 요청하게 합니다.
  - EN: Update the search tool's description so that Claude is made to ask for confirmation before working when multiple candidate incidents are returned.
- C. JA: プロジェクトのファイルを変更する前に、一致した中で最も新しいインシデントを選ぶようコマンドを更新する。
  - KO: 프로젝트 파일을 변경하기 전에, 일치한 것 중 가장 최근 인시던트를 고르도록 명령을 업데이트합니다.
  - EN: Update the command to select the most recent of the matching incidents before modifying any project files.
- D. JA: 検索ツールから候補のインシデントをすべて、IDなどの識別情報付きで返させる。
  - KO: 검색 도구가 후보 인시던트를 모두 ID 같은 식별 정보와 함께 반환하게 합니다.
  - EN: Have the search tool return all candidate incidents together with identifying information such as IDs.

## CCAR-F-Udemy01-0008

**JA** ある証券会社のプラットフォームチームは、社内の約150のリポジトリでClaude Codeを利用しています。セキュリティ部門は、開発者がどのリポジトリで作業する場合でも、Claude Codeが.envファイルを読み取れないようにしたいと考えています。

この制限には、次の条件があります。

開発者が自分の設定ファイル、リポジトリ内の設定、起動時のオプションを変えても緩められない

今後新しく作られるリポジトリにも、追加作業なしで適用される

最も適切な方法はどれですか。

**KO** 한 증권사의 플랫폼 팀은 사내 약 150개 저장소에서 Claude Code를 사용하고 있습니다. 보안 부서는 개발자가 어느 저장소에서 작업하든 Claude Code가 .env 파일을 읽지 못하게 하려고 합니다.

이 제한에는 다음 조건이 있습니다.

개발자가 자신의 설정 파일, 저장소 안의 설정, 실행 옵션을 바꿔도 완화할 수 없어야 합니다

앞으로 새로 만들어지는 저장소에도 추가 작업 없이 적용되어야 합니다

가장 적절한 방법은 무엇입니까?

- A. JA: .envの読み取りを拒否するdenyルールを、MDMで配布するmanaged-settings.jsonに書く。
  - KO: .env 읽기를 거부하는 deny 규칙을, MDM으로 배포하는 managed-settings.json에 작성합니다.
  - EN: Write a deny rule that blocks reading .env in a managed-settings.json distributed via MDM.
- B. JA: .envの読み取りを拒否するdenyルールを、各リポジトリの.claude/settings.jsonに書いてコミットする。
  - KO: .env 읽기를 거부하는 deny 규칙을 각 저장소의 .claude/settings.json에 작성해 commit합니다.
  - EN: Write a deny rule that blocks reading .env in each repository's .claude/settings.json and commit it.
- C. JA: .envの読み取りを拒否するdenyルールを、各開発者の~/.claude/settings.jsonに追加してもらう。
  - KO: .env 읽기를 거부하는 deny 규칙을 각 개발자가 자신의 ~/.claude/settings.json에 추가하게 합니다.
  - EN: Ask each developer to add a deny rule that blocks reading .env to their own ~/.claude/settings.json.
- D. JA: .envの読み取りを拒否するdenyルールを--settingsで渡す起動用スクリプトを配布し、それで起動させる。
  - KO: .env 읽기를 거부하는 deny 규칙을 --settings로 전달하는 실행용 스크립트를 배포하고, 그 스크립트로 실행하게 합니다.
  - EN: Distribute a launcher script that passes a deny rule blocking reading .env via --settings, and have developers start Claude Code with it.

## CCAR-F-Udemy01-0009

**JA** あるチームは、Claude Agent SDKを使用して、投資先候補を調べるマルチエージェントのデューデリジェンス支援システムを構築しています。コーディネーターエージェントは、専門化されたサブエージェント（Web検索担当、資料分析担当、知見の統合担当、レポート生成担当）に作業を委任します。このシステムは対象企業を調査し、出典を明記した包括的なレポートを作成します。

評価では、統合エージェントが、各サブエージェントの出力を時系列順に連結した非常に長いプロンプトを受け取っています。最終レポートの状況は次のとおりです。

最初期のWeb検索結果からの知見は、毎回一貫して反映される

末尾に置かれた直近のレポート作成指示も、毎回一貫して反映される

集約された入力の中ほどに埋もれた資料分析の知見は、いくつかが漏れてしまう

調査をやり直さずに、レポートの網羅性を最も直接的に改善する変更はどれですか。

**KO** 한 팀은 Claude Agent SDK를 사용해 투자 대상 후보를 조사하는 multi-agent 실사(due diligence) 지원 시스템을 구축하고 있습니다. coordinator agent는 전문화된 subagent(웹 검색 담당, 자료 분석 담당, 발견 사항 통합 담당, 보고서 생성 담당)에게 작업을 위임합니다. 이 시스템은 대상 기업을 조사하고 출처를 명시한 포괄적인 보고서를 작성합니다.

평가에서 통합 agent는 각 subagent의 출력을 시간 순서대로 이어 붙인 매우 긴 prompt를 받고 있습니다. 최종 보고서의 상황은 다음과 같습니다.

가장 초기의 웹 검색 결과에서 나온 발견 사항은 매번 일관되게 반영됩니다

끝부분에 놓인 최근의 보고서 작성 지시도 매번 일관되게 반영됩니다

취합된 입력의 중간에 묻힌 자료 분석 발견 사항은 일부가 누락됩니다

조사를 다시 하지 않고, 보고서가 빠짐없이 다루는 정도를 가장 직접적으로 개선하는 변경은 무엇입니까?

- A. JA: 中ほどの知見を出典なしのトピック要約に置き換えてから統合エージェントに渡し、レポートを書かせる。
  - KO: 중간의 발견 사항을 출처 없는 주제 요약으로 바꾼 뒤 통합 agent에 넘겨 보고서를 쓰게 합니다.
  - EN: Replace the middle findings with uncited topic summaries before passing them to the synthesis agent to write the report.
- B. JA: 知見と出典の簡潔な一覧を統合プロンプトの冒頭に置き、詳しい根拠はラベル付きの節に残す。
  - KO: 발견 사항과 출처의 간결한 목록을 통합 prompt의 맨 앞에 두고, 자세한 근거는 라벨이 붙은 절에 남깁니다.
  - EN: Place a concise list of findings and sources at the beginning of the synthesis prompt, and keep the detailed evidence in labeled sections.
- C. JA: 統合プロンプトの末尾に、提供されたすべての知見を検討するよう求める最終チェックリストを追加する。
  - KO: 통합 prompt의 끝에, 제공된 모든 발견 사항을 검토하도록 요구하는 최종 체크리스트를 추가합니다.
  - EN: Add a final checklist to the end of the synthesis prompt asking the agent to consider all of the findings provided.
- D. JA: 応答の長さ上限を引き上げ、統合エージェントが最終レポートにより多くの知見と出典を含められるようにする。
  - KO: 응답 길이 상한을 올려, 통합 agent가 최종 보고서에 더 많은 발견 사항과 출처를 담을 수 있게 합니다.
  - EN: Raise the response length limit so that the synthesis agent can include more findings and sources in the final report.

## CCAR-F-Udemy01-0010

**JA** Claude Agent SDKを使用して、マルチエージェントの調査システムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、Web検索を行うもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

ある法務調査チームは、6万件の判例トピックを一晩で処理する計画を立てています。各トピックは独立したMessages APIのレポート生成リクエストとし、Message Batches APIを通じて送信します。

パイロットサンプルでは、次の問題が分かりました。

レポート生成用のプロンプトが、必須のレポートセクションを省略することがある

下流のパーサーが拒否するJSONメタデータを出力することがある

全件を送信する前に取るべき次のステップとして、最も適切なものはどれですか。

**KO** Claude Agent SDK를 사용해 multi-agent 조사 시스템을 구축하고 있습니다. coordinator agent가 전문화된 subagent에게 작업을 위임합니다. subagent에는 웹 검색을 하는 것, 문서를 분석하는 것, 조사 결과를 통합하는 것, 보고서를 생성하는 것이 있습니다. 이 시스템은 주제를 조사하고 출처를 명시한 포괄적인 보고서를 작성합니다.

한 법무 조사팀은 판례 주제 6만 건을 하룻밤 사이에 처리할 계획을 세우고 있습니다. 각 주제는 독립된 Messages API 보고서 생성 요청으로 만들어 Message Batches API로 전송합니다.

파일럿 샘플에서 다음 문제가 드러났습니다.

보고서 생성용 prompt가 필수 보고서 섹션을 빠뜨리는 경우가 있습니다

downstream 파서가 거부하는 JSON metadata를 출력하는 경우가 있습니다

전체를 전송하기 전에 밟아야 할 다음 단계로 가장 적절한 것은 무엇입니까?

- A. JA: プロンプトをテンプレート化し、本番と同じリクエスト形式のエッジケース評価で改善を重ね、同期のドライラン成功後にバッチを送る。
  - KO: prompt를 템플릿화하고, 운영 환경과 같은 요청 형식의 edge case 평가로 개선을 거듭한 뒤, 동기 방식의 dry run이 성공하면 batch를 전송합니다.
  - EN: Templatize the prompt, iterate on improvements using edge-case evaluations in the same request format as production, and submit the batch after a successful synchronous dry run.
- B. JA: Claudeにレポート生成プロンプトを書き直させ、採点基準もテストセットも変えずにその版でバッチを送信する。
  - KO: Claude에게 보고서 생성 prompt를 다시 쓰게 하고, 채점 기준도 테스트 세트도 바꾸지 않은 채 그 버전으로 batch를 전송합니다.
  - EN: Have Claude rewrite the report generation prompt, and submit the batch with that version without changing the grading rubric or the test set.
- C. JA: 先に全件をバッチで送信し、終了した結果から検証や品質の失敗を洗い出して、該当する判例トピックだけを修正版で再送する。
  - KO: 먼저 전체를 batch로 전송하고, 완료된 결과에서 검증·품질 실패를 찾아낸 뒤, 해당 판례 주제만 수정본으로 다시 전송합니다.
  - EN: Submit everything as a batch first, identify validation and quality failures from the completed results, and resubmit only the affected case law topics with a fixed version.
- D. JA: レポート生成のスキーマを厳格にしてツールの使用を強制し、網羅性や出典の品質の問題はスキーマ検証に任せる。
  - KO: 보고서 생성 schema를 엄격하게 하고 도구 사용을 강제하며, 누락 여부나 출처 품질 문제는 schema 검증에 맡깁니다.
  - EN: Tighten the report generation schema and force tool use, and leave completeness and citation quality issues to schema validation.

## CCAR-F-Udemy01-0011

**JA** あなたは、Claude Agent SDKを使用して開発者の生産性向上ツールを構築しています。このエージェントは、エンジニアが不慣れなコードベースを探索し、レガシーシステムを理解し、ボイラープレートコードを生成し、反復的なタスクを自動化するのを支援します。組み込みツール（Read、Write、Bash、Grep、Glob）を使用し、Model Context Protocol（MCP）サーバーと統合します。

ある小売チェーンの在庫管理システムを長時間にわたって調査する過程で、メインの会話がファイル一覧・検索結果・テストログで繰り返し埋め尽くされてしまいます。リード開発者は、冗長な調査出力によって重要なコンテキストが失われないようにしたうえで、メインエージェントには引き続きアーキテクチャを把握するための調整役を担わせたいと考えています。

この問題に最も適した変更はどれですか。（2つ選択してください。）

**KO** 당신은 Claude Agent SDK를 사용해 개발자 생산성 향상 도구를 구축하고 있습니다. 이 agent는 엔지니어가 익숙하지 않은 코드베이스를 탐색하고, 레거시 시스템을 이해하고, boilerplate 코드를 생성하고, 반복 작업을 자동화하도록 돕습니다. 내장 도구(Read, Write, Bash, Grep, Glob)를 사용하고 Model Context Protocol(MCP) server와 통합합니다.

한 소매 체인의 재고 관리 시스템을 오랫동안 조사하는 과정에서, 메인 대화가 파일 목록·검색 결과·테스트 로그로 거듭 가득 차 버립니다. 리드 개발자는 장황한 조사 출력 때문에 중요한 context가 밀려나지 않게 하면서, 메인 agent에게는 계속 아키텍처를 파악하는 조정 역할을 맡기고 싶어 합니다.

이 문제에 가장 적합한 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 汎用（general-purpose）サブエージェントに探索させ、パスと行番号付きの要約だけをメインに返させる。
  - KO: 범용(general-purpose) subagent에게 탐색을 맡기고, 경로와 줄 번호가 붙은 요약만 메인에 반환하게 합니다.
  - EN: Have a general-purpose subagent perform the exploration and return only a summary with paths and line numbers to the main conversation.
- B. JA: 調査する分岐ごとにforkを作成し、親の会話全体を継承させたうえで結果をメインに返させる。
  - KO: 조사할 분기마다 fork를 만들어 부모 대화 전체를 상속받게 한 뒤, 결과를 메인에 반환하게 합니다.
  - EN: Create a fork for each branch being investigated, have it inherit the entire parent conversation, and have it return its results to the main conversation.
- C. JA: Grep・Glob・Read・Bashをメインの会話で直接実行し、大きな探索が終わるたびに会話をコンパクト化する。
  - KO: Grep·Glob·Read·Bash를 메인 대화에서 직접 실행하고, 큰 탐색이 끝날 때마다 대화를 compact합니다.
  - EN: Run Grep, Glob, Read, and Bash directly in the main conversation, and compact the conversation each time a large exploration finishes.
- D. JA: コード検索とファイル探索をExploreサブエージェントに任せ、簡潔な調査結果だけをメインの会話に返させる。
  - KO: 코드 검색과 파일 탐색을 Explore subagent에 맡기고, 간결한 조사 결과만 메인 대화에 반환하게 합니다.
  - EN: Delegate code search and file exploration to an Explore subagent, and have it return only concise findings to the main conversation.

## CCAR-F-Udemy01-0012

**JA** あなたのチームは、インフラ構成変更（Infrastructure as Code）のプルリクエストのレビューを、Message Batches APIを使って毎晩実行したいと考えています。

各レビューでは、Claudeが最終的なフィードバックを書く前に、アプリケーション側で実行するクライアントツールrun_infra_checksが必要になる場合があります。このツールは、ローカルでterraform planとポリシーチェックを実行します。

このワークフローを最も適切に処理する設計はどれですか。

**KO** 당신의 팀은 인프라 구성 변경(Infrastructure as Code) pull request 리뷰를 Message Batches API로 매일 밤 실행하려고 합니다.

각 리뷰에서는 Claude가 최종 피드백을 쓰기 전에, 애플리케이션 쪽에서 실행하는 client tool인 run_infra_checks가 필요할 수 있습니다. 이 도구는 로컬에서 terraform plan과 정책 검사를 실행합니다.

이 workflow를 가장 적절하게 처리하는 설계는 무엇입니까?

- A. JA: レビュー用プロンプトをバッチ項目として送信し、tool_choiceをrun_infra_checksに設定し、最終フィードバックを返す前にバッチワーカーがクライアントツールを実行してくれる前提にする。
  - KO: 리뷰용 prompt를 batch 항목으로 전송하고 tool_choice를 run_infra_checks로 설정한 뒤, 최종 피드백을 반환하기 전에 batch 워커가 client tool을 실행해 줄 것이라고 가정합니다.
  - EN: Submit the review prompt as a batch item, set tool_choice to run_infra_checks, and assume that the batch worker will run the client tool before returning the final feedback.
- B. JA: プロンプト、予測したtool_resultブロック、最終レビュー指示を1つのバッチ項目にまとめて送信し、Claudeが1回のリクエストでループを完結できるようにする。
  - KO: prompt, 예측한 tool_result 블록, 최종 리뷰 지시를 하나의 batch 항목으로 묶어 전송해, Claude가 한 번의 요청으로 loop를 끝낼 수 있게 합니다.
  - EN: Combine the prompt, a predicted tool_result block, and the final review instructions into a single batch item so that Claude can complete the loop in one request.
- C. JA: レビュー用プロンプトをバッチ項目として送信し、custom_idでtool_useの結果を取得し、要求されたクライアントツールを実行したうえで、tool_resultブロックを含む後続リクエストを送信する。
  - KO: 리뷰용 prompt를 batch 항목으로 전송하고, custom_id로 tool_use 결과를 가져와 요청된 client tool을 실행한 뒤, tool_result 블록을 담은 후속 요청을 보냅니다.
  - EN: Submit the review prompt as a batch item, retrieve the tool_use results by custom_id, run the requested client tool, and then send a follow-up request containing the tool_result block.
- D. JA: レビュー用プロンプトをバッチ項目として送信し、run_infra_checksの代わりにweb_searchを使い、サーバーツールの実行結果でローカルリポジトリの検証を代替する。
  - KO: 리뷰용 prompt를 batch 항목으로 전송하되 run_infra_checks 대신 web_search를 사용해, server tool의 실행 결과로 로컬 저장소 검증을 대신합니다.
  - EN: Submit the review prompt as a batch item and use web_search instead of run_infra_checks, substituting the server tool's execution results for validation of the local repository.

## CCAR-F-Udemy01-0013

**JA** あなたは、Claudeを使用して給与計算用のデータ抽出システムを構築しています。このシステムは、タイムシートなどの非構造化文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流の給与システムと連携する必要があります。

検証中、あるMCPツールが次の2点を検知しました。

抽出された勤務日が、実在しない日付である

申告された合計勤務時間が、抽出した内訳の合計と一致しない

このツールは現在、「検証に失敗しました」というテキストを含む通常の結果を返しています。その結果、Claudeが同じ呼び出しを繰り返したり、下流のシステムが抽出を成功とみなしたりすることがあります。

復旧動作を改善する変更として、最も効果的なものはどれですか。

**KO** 당신은 Claude를 사용해 급여 계산용 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 근무 기록표 같은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 급여 시스템과 연동해야 합니다.

검증 중에 한 MCP 도구가 다음 두 가지를 감지했습니다.

추출된 근무일이 존재하지 않는 날짜입니다

신고된 총 근무 시간이 추출한 내역의 합계와 일치하지 않습니다

이 도구는 현재 "검증에 실패했습니다"라는 텍스트가 담긴 일반 결과를 반환하고 있습니다. 그 결과 Claude가 같은 호출을 반복하거나, downstream 시스템이 추출을 성공으로 간주하는 경우가 있습니다.

복구 동작을 개선하는 변경으로 가장 효과적인 것은 무엇입니까?

- A. JA: tools/callリクエストに対してJSON-RPCのエラー応答を返し、検証の失敗をプロトコル層のエラーとして報告する。
  - KO: tools/call 요청에 JSON-RPC 오류 응답을 반환해, 검증 실패를 프로토콜 계층의 오류로 보고합니다.
  - EN: Return a JSON-RPC error response to the tools/call request, reporting the validation failure as a protocol-level error.
- B. JA: 抽出結果は空のまま、文書を検証できなかった理由を説明するテキストを本文に入れた成功扱いのCallToolResultを返す。
  - KO: 추출 결과는 비워 둔 채, 문서를 검증할 수 없었던 이유를 설명하는 텍스트를 본문에 넣은 성공으로 처리되는 CallToolResult를 반환합니다.
  - EN: Return a CallToolResult treated as successful, with the extraction result left empty and text in the body explaining why the document could not be validated.
- C. JA: 日付と合計値の書式をツールの説明文に追記し、Claudeが不正な引数を送らないよう予防する。
  - KO: 날짜와 합계 값의 형식을 도구 설명에 추가해, Claude가 잘못된 인수를 보내지 않도록 예방합니다.
  - EN: Add the date and total value formats to the tool description to prevent Claude from sending invalid arguments.
- D. JA: CallToolResultのisErrorをtrueにし、エラー種別と修正のヒントをstructuredContentで返す。
  - KO: CallToolResult의 isError를 true로 하고, 오류 유형과 수정 힌트를 structuredContent로 반환합니다.
  - EN: Set isError to true in the CallToolResult, and return the error type and a hint for correcting it in structuredContent.

## CCAR-F-Udemy01-0014

**JA** ある銀行で、コアバンキング基盤の大規模なリファクタリングを進めています。チームは、Claude Codeにデータベース移行レビュー、API互換性レビュー、テストカバレッジレビューを並行して実行させたいと考えています。また、矛盾する指摘事項を解消し、どのフォローアップ作業を行うかを決める場所は、1か所にまとめたいと考えています。

Claude Codeのサブエージェントモデルに最も合致するオーケストレーション設計はどれですか。

**KO** 한 은행에서 코어뱅킹 기반의 대규모 refactoring을 진행하고 있습니다. 팀은 Claude Code가 데이터베이스 마이그레이션 리뷰, API 호환성 리뷰, 테스트 커버리지 리뷰를 병렬로 실행하게 하려고 합니다. 또한 서로 모순되는 지적 사항을 해소하고 어떤 후속 작업을 할지 결정하는 곳은 한 곳으로 모으려고 합니다.

Claude Code의 subagent 모델에 가장 잘 맞는 orchestration 설계는 무엇입니까?

- A. JA: レビュアーのサブエージェント同士に直接メッセージを交換させ、共有タスクリスト上で調整した最終プランを送らせる。
  - KO: 리뷰어 subagent끼리 직접 메시지를 주고받게 하고, 공유 작업 목록에서 조정한 최종 계획을 보내게 합니다.
  - EN: Have the reviewer subagents exchange messages directly with one another and submit a final plan coordinated on a shared task list.
- B. JA: メインエージェントがAgentで各レビュアーに必要な情報を渡して起動し、返った要約をもとに中央で方針を決める。
  - KO: 메인 agent가 Agent로 각 리뷰어에게 필요한 정보를 넘겨 실행하고, 돌아온 요약을 바탕으로 중앙에서 방침을 정합니다.
  - EN: Have the main agent launch each reviewer through Agent, passing it the information it needs, and make decisions centrally based on the summaries returned.
- C. JA: メインエージェントのツールからAgentを外し、CLAUDE.mdに書いたレビュアー用の指示からClaudeに暗黙的に選ばせる。
  - KO: 메인 agent의 도구에서 Agent를 빼고, CLAUDE.md에 적은 리뷰어용 지시를 바탕으로 Claude가 암묵적으로 고르게 합니다.
  - EN: Remove Agent from the main agent's tools, and have Claude implicitly select reviewers based on reviewer instructions written in CLAUDE.md.
- D. JA: 各レビュアーを独立したサブエージェントとして起動しつつメインの履歴を継承させ、振り分けの段を設けずに指摘をまとめる。
  - KO: 각 리뷰어를 독립된 subagent로 실행하면서 메인 기록을 상속받게 하고, 분류(triage) 단계 없이 지적 사항을 취합합니다.
  - EN: Launch each reviewer as an independent subagent that inherits the main history, and merge the findings without a triage stage.

## CCAR-F-Udemy01-0015

**JA** Claudeを使用して、構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携する必要があります。

このチームは、Claude Codeを使って抽出用のリポジトリを更新しています。

Claudeにデフォルトモードで直接変更させるのではなく、実装前にプランモードを使うのに最も適したタスクはどれですか。（2つ選択してください。）

**KO** Claude를 사용해 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동해야 합니다.

이 팀은 Claude Code로 추출용 저장소를 업데이트하고 있습니다.

Claude가 default mode에서 바로 변경하게 하는 대신, 구현 전에 plan mode를 쓰기에 가장 적합한 작업은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 既知のスキーマファイルを開かせ、誤字のあるフィールドラベルを直させて、明白な1行の修正を適用させる。
  - KO: 이미 알고 있는 schema 파일을 열게 하고, 오타가 있는 필드 라벨을 고쳐 명백한 한 줄 수정을 적용하게 합니다.
  - EN: Have Claude open a known schema file, fix a misspelled field label, and apply the obvious one-line fix.
- B. JA: 既に特定済みの検証関数を開かせ、失敗時のログ出力を1行追加させて、その小さな変更を保存させる。
  - KO: 이미 특정한 검증 함수를 열게 하고, 실패 시 로그 출력을 한 줄 추가해 그 작은 변경을 저장하게 합니다.
  - EN: Have Claude open an already identified validation function, add one line of failure logging, and save that small change.
- C. JA: 検証と修復がパイプライン全体でどう作用し合うかを調べさせ、部分的に妥当な文書の扱いを提案させる。
  - KO: 검증과 복구가 pipeline 전체에서 어떻게 서로 영향을 주는지 조사하게 하고, 부분적으로만 유효한 문서의 처리 방법을 제안하게 합니다.
  - EN: Have Claude investigate how validation and repair interact across the entire pipeline, and propose how to handle partially valid documents.
- D. JA: 既存の保険金請求の抽出フローを調べさせ、あいまいな請求額の表現を変えるための移行計画を提案させる。
  - KO: 기존 보험금 청구 추출 흐름을 조사하게 하고, 모호한 청구 금액 표현을 바꾸기 위한 마이그레이션 계획을 제안하게 합니다.
  - EN: Have Claude investigate the existing insurance claim extraction flow and propose a migration plan for changing how ambiguous claim amount expressions are handled.

## CCAR-F-Udemy01-0016

**JA** ある通信キャリアのカスタマーサポート部門は、自社のカスタマーサポート解決エージェントを見直しています。その中で、エスカレーションされたサポートチケットに、「顧客は請求金額について不満を持っている」といったあいまいなメモしか残っていないことが多い、という問題が見つかりました。

これらのチケットを受け取る人間の担当者は、元のチャット履歴にアクセスできません。また、下流のサポート管理ツールは、一貫した引き継ぎデータを前提としています。

この問題に最も適した実装上の変更はどれですか。（2つ選択してください。）

**KO** 한 통신사의 고객 지원 부서는 자사의 고객 지원 해결 agent를 재검토하고 있습니다. 그 과정에서 escalation된 지원 티켓에 "고객이 청구 금액에 불만이 있음" 같은 모호한 메모만 남아 있는 경우가 많다는 문제가 발견되었습니다.

이 티켓을 넘겨받는 사람 담당자는 원래 채팅 기록에 접근할 수 없습니다. 또한 downstream 지원 관리 도구는 일관된 인계 데이터를 전제로 합니다.

이 문제에 가장 적합한 구현상의 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 引き継ぎメモの必須項目をシステムプロンプトに箇条書きで列挙し、自由記述で出力させる。
  - KO: 인계 메모의 필수 항목을 system prompt에 글머리표로 나열하고, 자유 형식으로 출력하게 합니다.
  - EN: List the required fields for handoff notes as bullet points in the system prompt, and have Claude output them as free-form text.
- B. JA: 人への引き継ぎで対応を終える場合はエスカレーション用ツールを呼び出すよう、システムプロンプトで指示する。
  - KO: 사람에게 인계하는 것으로 대응을 마칠 때는 escalation용 도구를 호출하도록 system prompt에서 지시합니다.
  - EN: Instruct in the system prompt that Claude should call the escalation tool when it concludes handling by handing off to a human.
- C. JA: 顧客IDや根本原因、推奨対応をinput_schemaの必須項目にしたescalate_to_humanツールを定義する。
  - KO: 고객 ID, 근본 원인, 권장 조치를 input_schema의 필수 항목으로 둔 escalate_to_human 도구를 정의합니다.
  - EN: Define an escalate_to_human tool whose input_schema makes the customer ID, root cause, and recommended action required fields.
- D. JA: チケットを作成する前に返金の引数が検証されるよう、tool_choiceでprocess_refundを強制的に呼ばせる。
  - KO: 티켓을 만들기 전에 환불 인수가 검증되도록, tool_choice로 process_refund를 강제로 호출하게 합니다.
  - EN: Force a call to process_refund with tool_choice so that the refund arguments are validated before the ticket is created.

## CCAR-F-Udemy01-0017

**JA** Claude Agent SDKを使用して、マルチエージェントの競合製品調査システムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、Web検索を行うもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

コーディネーターは昨日調査を完了し、Web検索の出力・文書分析ツールの結果・統合のメモ・レポート生成の下書きを含むセッションを保存しました。それ以降、次の変化がありました。

文書コーパスが再インデックスされた

複数の情報源文書が更新された

レビュー担当者が、従来の調査結果のうちどれが引き続き有効かを修正した

チームは、次の実行では有効な分析上の判断だけを引き継ぎ、昨日のツールの古い観測結果は持ち越さないようにしたいと考えています。

コーディネーターが次に行うべきことはどれですか。（2つ選択してください。）

**KO** Claude Agent SDK를 사용해 multi-agent 경쟁 제품 조사 시스템을 구축하고 있습니다. coordinator agent가 전문화된 subagent에게 작업을 위임합니다. subagent에는 웹 검색을 하는 것, 문서를 분석하는 것, 조사 결과를 통합하는 것, 보고서를 생성하는 것이 있습니다. 이 시스템은 주제를 조사하고 출처를 명시한 포괄적인 보고서를 작성합니다.

coordinator는 어제 조사를 마치고, 웹 검색 출력·문서 분석 도구 결과·통합 메모·보고서 생성 초안이 담긴 session을 저장했습니다. 그 뒤로 다음과 같은 변화가 있었습니다.

문서 코퍼스가 다시 색인되었습니다

여러 정보원 문서가 업데이트되었습니다

리뷰 담당자가 기존 조사 결과 중 어느 것이 여전히 유효한지 수정했습니다

팀은 다음 실행에서 유효한 분석상의 판단만 이어받고, 어제 도구로 얻은 오래된 관측 결과는 가져가지 않으려고 합니다.

coordinator가 다음에 해야 할 일은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 保存済みのセッションをforkし、そのforkの中で修正版のレポートを検討させる。
  - KO: 저장된 session을 fork하고, 그 fork 안에서 수정판 보고서를 검토하게 합니다.
  - EN: Fork the saved session and have the coordinator consider the revised report within that fork.
- B. JA: 保存済みのセッションをIDで再開し、昨日の古いツール結果は無視するようコーディネーターに指示する。
  - KO: 저장된 session을 ID로 재개하고, 어제의 오래된 도구 결과는 무시하라고 coordinator에 지시합니다.
  - EN: Resume the saved session by ID and instruct the coordinator to ignore yesterday's stale tool results.
- C. JA: 再インデックス後のコーパスに対して、Web検索と文書分析のサブエージェントを実行し直す。
  - KO: 다시 색인된 코퍼스를 대상으로 웹 검색 subagent와 문서 분석 subagent를 다시 실행합니다.
  - EN: Re-run the web search and document analysis subagents against the corpus after reindexing.
- D. JA: 新しいセッションを開始し、検証済みの結果と判断、再確認する情報源を構造化した要約で渡す。
  - KO: 새 session을 시작하고, 검증된 결과와 판단, 다시 확인할 정보원을 구조화한 요약으로 전달합니다.
  - EN: Start a new session and pass it a structured summary of the verified results and conclusions and of the sources to be rechecked.

## CCAR-F-Udemy01-0018

**JA** あるEコマース企業は、Claude Agent SDKを使用してマルチエージェントの商品リサーチシステムを構築しています。コーディネーターが、市場調査・文書分析・統合・レポート生成をそれぞれ担当する専門サブエージェントに作業を委任し、根拠付きの詳細なレポートを作成します。

テストでは、初期の調査ステップは出典を豊富に含む調査結果をコーディネーターに返しています。それにもかかわらず、統合サブエージェントは出典を記載しない要約をたびたび生成しています。統合作業を委任するメッセージは、「これまでに集めた調査結果を使って、出典付きのレポートを作成してください」という内容です。

このチームが行うべき変更はどれですか。（2つ選択してください。）

**KO** 한 전자상거래 기업은 Claude Agent SDK를 사용해 multi-agent 상품 리서치 시스템을 구축하고 있습니다. coordinator가 시장 조사, 문서 분석, 통합, 보고서 생성을 각각 담당하는 전문 subagent에게 작업을 위임해, 근거를 갖춘 상세한 보고서를 작성합니다.

테스트에서 초기 조사 단계는 출처가 풍부한 조사 결과를 coordinator에 반환하고 있습니다. 그런데도 통합 subagent는 출처를 적지 않은 요약을 자주 생성합니다. 통합 작업을 위임하는 메시지의 내용은 "지금까지 모은 조사 결과를 사용해 출처가 포함된 보고서를 작성해 주세요"입니다.

이 팀이 해야 할 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 統合サブエージェントが、自身のツール設定からAgentを呼び出して他のサブエージェントを起動できるようにする。
  - KO: 통합 subagent가 자신의 도구 설정에서 Agent를 호출해 다른 subagent를 실행할 수 있게 합니다.
  - EN: Allow the synthesis subagent to invoke Agent from its own tool configuration to launch other subagents.
- B. JA: 関連する調査結果と出典メタデータを、統合タスクのメッセージに直接渡す。
  - KO: 관련 조사 결과와 출처 metadata를 통합 작업 메시지에 직접 담아 전달합니다.
  - EN: Pass the relevant research findings and source metadata directly in the synthesis task message.
- C. JA: 最終レポート作成のたびに、統合サブエージェントを@メンションで呼び出す。
  - KO: 최종 보고서를 작성할 때마다 통합 subagent를 @멘션으로 호출합니다.
  - EN: Invoke the synthesis subagent with an @-mention each time the final report is created.
- D. JA: 収集した調査結果と出典メタデータをファイルに書き出し、そのファイルパスを統合タスクのメッセージで渡す。
  - KO: 수집한 조사 결과와 출처 metadata를 파일로 쓰고, 그 파일 경로를 통합 작업 메시지로 전달합니다.
  - EN: Write the collected research findings and source metadata to a file, and pass the file path in the synthesis task message.

## CCAR-F-Udemy01-0019

**JA** Claude Agent SDKを使用して、マルチエージェントのデューデリジェンス調査システムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、Web検索を行うもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

規制対象のトピックを扱う実行で、コーディネーターがすべての主要な主張について出典対応表の検証を終える前に、レポート生成サブエージェントが、下書きを公開するMCPツールを呼び出してしまうことがあります。

チームは、出典対応表（citation manifest）が無い限り公開ツールが実行されないよう、確定的に制御したいと考えています。

行うべき変更はどれですか。（2つ選択してください。）

**KO** Claude Agent SDK를 사용해 multi-agent 실사(due diligence) 조사 시스템을 구축하고 있습니다. coordinator agent가 전문화된 subagent에게 작업을 위임합니다. subagent에는 웹 검색을 하는 것, 문서를 분석하는 것, 조사 결과를 통합하는 것, 보고서를 생성하는 것이 있습니다. 이 시스템은 주제를 조사하고 출처를 명시한 포괄적인 보고서를 작성합니다.

규제 대상 주제를 다루는 실행에서, coordinator가 모든 주요 주장에 대한 출처 대응표 검증을 마치기 전에 보고서 생성 subagent가 초안을 공개하는 MCP 도구를 호출해 버리는 경우가 있습니다.

팀은 출처 대응표(citation manifest)가 없으면 공개 도구가 실행되지 않도록 결정적으로(deterministic) 제어하려고 합니다.

해야 할 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 公開ツールに対して、必須の出典対応表が欠けている呼び出しをブロックするPreToolUseフックを設定する。
  - KO: 공개 도구에, 필수 출처 대응표가 빠진 호출을 차단하는 PreToolUse hook을 설정합니다.
  - EN: Configure a PreToolUse hook on the publishing tool that blocks calls that are missing the required citation manifest.
- B. JA: 公開用のMCPツールをレポート生成サブエージェントの許可ツールから外し、コーディネーターだけが呼べる状態にする。
  - KO: 공개용 MCP 도구를 보고서 생성 subagent의 허용 도구에서 빼고, coordinator만 호출할 수 있게 합니다.
  - EN: Remove the publishing MCP tool from the report generation subagent's allowed tools so that only the coordinator can call it.
- C. JA: 公開の前には出典対応表を検証するよう、各サブエージェントに向けた指示をコーディネーターのプロンプトに追加する。
  - KO: 공개하기 전에는 출처 대응표를 검증하라는 각 subagent 대상 지시를 coordinator의 prompt에 추가합니다.
  - EN: Add instructions directed at each subagent to the coordinator's prompt telling them to verify the citation manifest before publishing.
- D. JA: 公開ツールに、必須の出典対応表が欠けた出力を拒否するPostToolUseフックを設定して実行後に検査する。
  - KO: 공개 도구에, 필수 출처 대응표가 빠진 출력을 거부하는 PostToolUse hook을 설정해 실행 후에 검사합니다.
  - EN: Configure a PostToolUse hook on the publishing tool that rejects output missing the required citation manifest by inspecting it after execution.

## CCAR-F-Udemy01-0020

**JA** ある非営利団体は、Claude Agent SDKを使用してマルチエージェントの政策リサーチシステムを構築しています。コーディネーターが、Web調査・文書分析・統合・レポート生成をそれぞれ担当する専門サブエージェントに作業を委任し、出典を明記した包括的なレポートを作成します。

コーディネーターは、文書分析サブエージェントが証拠の抜粋と出典メタデータを返す前に、レポート生成サブエージェントへ委任してしまうことがあります。その結果、レポートはよく書けているものの、元の出典まで遡れない主張を含んでしまいます。

この失敗を最も効果的に防ぐ変更はどれですか。

**KO** 한 비영리 단체는 Claude Agent SDK를 사용해 multi-agent 정책 리서치 시스템을 구축하고 있습니다. coordinator가 웹 조사, 문서 분석, 통합, 보고서 생성을 각각 담당하는 전문 subagent에게 작업을 위임해, 출처를 명시한 포괄적인 보고서를 작성합니다.

coordinator는 문서 분석 subagent가 증거 발췌와 출처 metadata를 반환하기 전에 보고서 생성 subagent에게 위임해 버리는 경우가 있습니다. 그 결과 보고서는 잘 쓰였지만, 원래 출처까지 거슬러 올라갈 수 없는 주장이 섞이게 됩니다.

이 실패를 가장 효과적으로 막는 변경은 무엇입니까?

- A. JA: コーディネーターの反復回数の上限を増やし、不足している証拠を再要求できる機会を増やす。
  - KO: coordinator의 반복 횟수 상한을 늘려, 부족한 증거를 다시 요청할 기회를 늘립니다.
  - EN: Increase the coordinator's iteration limit to give it more opportunities to re-request missing evidence.
- B. JA: tool_choiceでレポート生成ツールを強制し、Claudeが常に指定されたレポート作成ステップを選択するようにする。
  - KO: tool_choice로 보고서 생성 도구를 강제해, Claude가 항상 지정된 보고서 작성 단계를 선택하게 합니다.
  - EN: Force the report generation tool with tool_choice so that Claude always selects the designated report-writing step.
- C. JA: 証拠のメタデータがすべて揃った後にのみレポート生成を行うよう、コーディネーターへの指示を強化する。
  - KO: 증거 metadata가 모두 갖춰진 뒤에만 보고서를 생성하도록 coordinator에 대한 지시를 강화합니다.
  - EN: Strengthen the instructions to the coordinator so that report generation takes place only after all of the evidence metadata is available.
- D. JA: 必要な結果と出典の対応付けが揃うまでレポート生成への委任を拒否する、オーケストレーション層の前提条件を追加する。
  - KO: 필요한 결과와 출처의 대응 관계가 갖춰질 때까지 보고서 생성 위임을 거부하는, orchestration 계층의 전제 조건을 추가합니다.
  - EN: Add a prerequisite in the orchestration layer that refuses to delegate to report generation until the required results and source mappings are in place.

## CCAR-F-Udemy01-0021

**JA** あなたは、Claude Agent SDKを使用して、複数のエージェントで構成される法務契約レビューシステムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、判例を検索するもの、契約書を解析するもの、調査結果を統合するもの、引用付きの意見書を作成するものがあります。

このシステムに、次の2つの評価ワークフローを追加する必要があります。

プルリクエストがマージされる前に必ずpass/failを返す必要がある、ブロッキングの引用品質ゲート

完了済みの意見書40,000件を対象に毎週実施する監査（結果は翌朝レビューされる）

これらの要件に最も適したAPIの使い方はどれですか。

**KO** 당신은 Claude Agent SDK를 사용해 여러 agent로 구성된 법률 계약 검토 시스템을 구축하고 있습니다. coordinator agent가 전문화된 subagent에게 작업을 위임합니다. subagent에는 판례를 검색하는 것, 계약서를 분석하는 것, 조사 결과를 통합하는 것, 인용이 포함된 의견서를 작성하는 것이 있습니다.

이 시스템에 다음 두 가지 평가 workflow를 추가해야 합니다.

pull request가 merge되기 전에 반드시 pass/fail을 반환해야 하는 블로킹 방식의 인용 품질 게이트

완료된 의견서 40,000건을 대상으로 매주 실시하는 감사(결과는 다음 날 아침에 검토)

이 요구 사항에 가장 적합한 API 사용 방법은 무엇입니까?

- A. JA: 両方のワークフローでストリーミングのMessages API呼び出しを使い、毎週の監査は多数の同時ストリーミングリクエストとして実行する。
  - KO: 두 workflow 모두 streaming Messages API 호출을 사용하고, 주간 감사는 다수의 동시 streaming 요청으로 실행합니다.
  - EN: Use streaming Messages API calls for both workflows, and run the weekly audit as many concurrent streaming requests.
- B. JA: マージゲートにはPOST /v1/messagesを使い、毎週の監査はcustom_id付きでMessage Batches APIに送る。
  - KO: merge 게이트에는 POST /v1/messages를 사용하고, 주간 감사는 custom_id를 붙여 Message Batches API로 보냅니다.
  - EN: Use POST /v1/messages for the merge gate, and send the weekly audit to the Message Batches API with a custom_id.
- C. JA: 両方のワークフローをMessage Batches APIで送信し、各pass/failの結果が得られるまでバッチのステータスをポーリングする。
  - KO: 두 workflow 모두 Message Batches API로 전송하고, 각 pass/fail 결과를 얻을 때까지 batch 상태를 polling합니다.
  - EN: Submit both workflows through the Message Batches API, and poll the batch status until each pass/fail result is available.
- D. JA: マージゲートにはMessage Batches APIを使い、出力の順序を保つために毎週の監査にはPOST /v1/messagesを使う。
  - KO: merge 게이트에는 Message Batches API를 사용하고, 출력 순서를 유지하기 위해 주간 감사에는 POST /v1/messages를 사용합니다.
  - EN: Use the Message Batches API for the merge gate, and use POST /v1/messages for the weekly audit in order to preserve output ordering.

## CCAR-F-Udemy01-0022

**JA** あなたは、Claudeを使用して、不動産の賃貸借契約書から情報を抽出する構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携する必要があります。

最新の評価では、検証セット全体で97.4%の総合抽出精度が報告されました。関係者は、この結果をもとに人によるレビューを減らしたいと考えています。

レビューポリシーを変更する前に、このチームが行うべきことはどれですか。（2つ選択してください。）

**KO** 당신은 Claude를 사용해, 부동산 임대차 계약서에서 정보를 추출하는 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동해야 합니다.

최근 평가에서 검증 세트 전체의 종합 추출 정확도가 97.4%로 보고되었습니다. 이해관계자들은 이 결과를 근거로 사람의 검토를 줄이려고 합니다.

검토 정책을 바꾸기 전에 이 팀이 해야 할 일은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 同じ検証セットでプロンプト比較を再実行し、平均スコアが高い方のプロンプトを本番に採用する。
  - KO: 같은 검증 세트로 prompt 비교를 다시 실행하고, 평균 점수가 높은 쪽 prompt를 운영 환경에 채택합니다.
  - EN: Re-run the prompt comparison on the same validation set, and adopt the prompt with the higher average score in production.
- B. JA: 抽出チェックを一律に完全一致の採点へ切り替え、その集計結果を承認の根拠にする。
  - KO: 추출 검사를 일괄적으로 완전 일치 채점으로 바꾸고, 그 집계 결과를 승인 근거로 삼습니다.
  - EN: Switch the extraction checks uniformly to exact-match scoring, and use that aggregate result as the basis for approval.
- C. JA: 文書の種類ごと、フィールドごとの精度を信頼できる件数で測れるよう、検証セットを拡大する。
  - KO: 문서 유형별, 필드별 정확도를 신뢰할 수 있는 건수로 측정할 수 있도록 검증 세트를 확대합니다.
  - EN: Expand the validation set so that accuracy by document type and by field can be measured with reliable sample sizes.
- D. JA: レビューを減らしてよい条件として、セグメントごとに満たすべき精度の目標値を先に定める。
  - KO: 검토를 줄여도 되는 조건으로, 세그먼트별로 충족해야 할 정확도 목표치를 먼저 정합니다.
  - EN: Define in advance the per-segment accuracy targets that must be met as the condition under which review may be reduced.

## CCAR-F-Udemy01-0023

**JA** ある保険会社は、Claude Agent SDKを使用して社内向けの開発者の生産性向上ツールを構築しています。このエージェントは、エンジニアが不慣れなコードベースを探索し、レガシーシステムを理解し、ボイラープレートコードを生成し、反復的なタスクを自動化するのを支援します。組み込みツール（Read、Write、Bash、Grep、Glob）を使用し、MCPサーバーとも連携します。

このチームは、ReadとGrepを使って、レガシーの請求処理ソースファイルから構造化されたリファクタ候補を抽出しています。JSONスキーマによって不正な形式のJSONは防げるようになりましたが、ログにはまだ次の2つの問題が残っています。

一部の応答が、stop_reason: "max_tokens"で返ってくる

スキーマ上は正当な一部の知見が、参照先ファイルに実在しない行番号を引用している

信頼性を改善するために、抽出ループが行うべきことはどれですか。（2つ選択してください。）

**KO** 한 보험사는 Claude Agent SDK를 사용해 사내용 개발자 생산성 향상 도구를 구축하고 있습니다. 이 agent는 엔지니어가 익숙하지 않은 코드베이스를 탐색하고, 레거시 시스템을 이해하고, boilerplate 코드를 생성하고, 반복 작업을 자동화하도록 돕습니다. 내장 도구(Read, Write, Bash, Grep, Glob)를 사용하고 MCP server와도 연동합니다.

이 팀은 Read와 Grep으로 레거시 청구 처리 소스 파일에서 구조화된 refactoring 후보를 추출하고 있습니다. JSON schema 덕분에 형식이 잘못된 JSON은 막을 수 있게 되었지만, 로그에는 아직 다음 두 가지 문제가 남아 있습니다.

일부 응답이 stop_reason: "max_tokens"로 반환됩니다

schema상으로는 유효한 일부 발견 사항이, 참조 대상 파일에 실제로 없는 줄 번호를 인용합니다

신뢰성을 개선하기 위해 추출 loop가 해야 할 일은 무엇입니까? (2개를 선택하십시오.)

- A. JA: stop_reasonを確認して、打ち切られた生成は出力上限を上げてリトライし、意味的な検証エラーは具体的に返して修正させる。
  - KO: stop_reason을 확인해, 잘린 생성은 출력 상한을 올려 재시도하고, 의미상의 검증 오류는 구체적으로 돌려주어 수정하게 합니다.
  - EN: Check stop_reason; retry truncated generations with a higher output limit, and return semantic validation errors with specifics so Claude can correct them.
- B. JA: pause_turnをクライアント側ツールの失敗として扱い、エラーのtool_resultを送信して抽出を最初からやり直す。
  - KO: pause_turn을 클라이언트 측 도구의 실패로 취급해, 오류 tool_result를 보내고 추출을 처음부터 다시 합니다.
  - EN: Treat pause_turn as a client-side tool failure, send an error tool_result, and restart the extraction from the beginning.
- C. JA: 各ソースファイルを小さな抽出リクエストに分割し、1リクエストあたりの候補数を抑える。
  - KO: 각 소스 파일을 작은 추출 요청으로 나눠, 요청당 후보 수를 줄입니다.
  - EN: Split each source file into smaller extraction requests to limit the number of candidates per request.
- D. JA: スキーマに適合したJSONを信頼し、行番号の検証は省略して、JSONパーサーが構文エラーを出したときだけリトライする。
  - KO: schema에 맞는 JSON을 신뢰하고 줄 번호 검증은 생략하며, JSON 파서가 구문 오류를 낼 때만 재시도합니다.
  - EN: Trust schema-conformant JSON, skip line-number validation, and retry only when the JSON parser raises a syntax error.

## CCAR-F-Udemy01-0024

**JA** インシデント対応の手順書（ランブック）を自動化するSREエージェントを構築しています。このエージェントは、組み込みツール（Read、Write、Bash、Grep、Glob）を使用し、Model Context Protocol（MCP）サーバーとも連携します。

本番環境のトレースを確認すると、エージェントがReadやGrepで対象クラスタを確認する前に、クラスタの状態を変更するBashコマンドを実行してしまうことがあります。システムプロンプトでは、対象環境の確認を必須と指示しています。

この必須の実行順序を最も確実に強制するために、行うべき変更はどれですか。（2つ選択してください。）

**KO** 인시던트 대응 절차서(runbook)를 자동화하는 SRE agent를 구축하고 있습니다. 이 agent는 내장 도구(Read, Write, Bash, Grep, Glob)를 사용하고 Model Context Protocol(MCP) server와도 연동합니다.

운영 환경의 trace를 확인해 보면, agent가 Read나 Grep으로 대상 클러스터를 확인하기 전에 클러스터 상태를 변경하는 Bash 명령을 실행해 버리는 경우가 있습니다. system prompt에서는 대상 환경 확인을 필수로 지시하고 있습니다.

이 필수 실행 순서를 가장 확실하게 강제하기 위해 해야 할 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: クラスタの状態を変えるBashコマンドの前にReadかGrepを行うよう、システム指示をより強い表現で書き直す。
  - KO: 클러스터 상태를 바꾸는 Bash 명령 전에 Read나 Grep을 실행하도록, 시스템 지시를 더 강한 표현으로 다시 씁니다.
  - EN: Rewrite the system instructions in stronger language, requiring Read or Grep before any Bash command that changes cluster state.
- B. JA: 安全でないBashコマンドを実行後に検出して拒否し、Claudeにリトライを促すPostToolUseのチェックを追加する。
  - KO: 안전하지 않은 Bash 명령을 실행 후에 감지해 거부하고, Claude에게 재시도를 유도하는 PostToolUse 검사를 추가합니다.
  - EN: Add a PostToolUse check that detects and rejects unsafe Bash commands after they run and prompts Claude to retry.
- C. JA: 状態を変える操作を専用ツールに移し、確認済みのクラスタIDを必須にして記録と一致しない呼び出しを拒否する。
  - KO: 상태를 바꾸는 작업을 전용 도구로 옮기고, 확인된 클러스터 ID를 필수로 해 기록과 일치하지 않는 호출을 거부합니다.
  - EN: Move state-changing operations into a dedicated tool that requires a confirmed cluster ID and rejects calls that do not match the recorded one.
- D. JA: 対象環境の確認が記録されるまでBashを拒否する、PreToolUseの前提条件ゲートを追加する。
  - KO: 대상 환경 확인이 기록될 때까지 Bash를 거부하는 PreToolUse 전제 조건 게이트를 추가합니다.
  - EN: Add a PreToolUse prerequisite gate that denies Bash until confirmation of the target environment has been recorded.

## CCAR-F-Udemy01-0025

**JA** あるエネルギー事業者のプラットフォームエンジニアリングチームは、Claude Agent SDKを使用して社内向けの開発者の生産性向上ツールを構築しています。このエージェントは、エンジニアが不慣れなコードベースを探索し、レガシーシステムを理解し、ボイラープレートコードを生成し、反復的なタスクを自動化するのを支援します。組み込みツール（Read、Write、Bash、Grep、Glob）を使用し、MCPサーバーとも連携します。

このチームは自動化されたコードベース棚卸しを実行しており、エージェントはレガシーのルーター定義ファイルからエンドポイントのメタデータを、後続ツール用のJSONとして抽出しています。バリデーターは、次の理由でこの抽出を拒否しました。

必須フィールドが1つ欠けている

列挙値が1つ不正である

ハンドラー名が1つ、ソースコード中に存在しない

リトライのフォローアップリクエストとして最も適切な設計はどれですか。

**KO** 한 에너지 기업의 플랫폼 엔지니어링 팀은 Claude Agent SDK를 사용해 사내용 개발자 생산성 향상 도구를 구축하고 있습니다. 이 agent는 엔지니어가 익숙하지 않은 코드베이스를 탐색하고, 레거시 시스템을 이해하고, boilerplate 코드를 생성하고, 반복 작업을 자동화하도록 돕습니다. 내장 도구(Read, Write, Bash, Grep, Glob)를 사용하고 MCP server와도 연동합니다.

이 팀은 코드베이스 전수 점검을 자동으로 실행하고 있으며, agent는 레거시 라우터 정의 파일에서 엔드포인트 metadata를 후속 도구용 JSON으로 추출하고 있습니다. validator는 다음 이유로 이 추출을 거부했습니다.

필수 필드가 하나 빠져 있습니다

열거값 하나가 잘못되었습니다

핸들러 이름 하나가 소스 코드에 존재하지 않습니다

재시도를 위한 후속 요청으로 가장 적절한 설계는 무엇입니까?

- A. JA: 同じスキーマでスキーマ制約付きのJSON出力を使ってリトライし、欠けているソースの詳細はスキーマの強制に補わせる。
  - KO: 같은 schema로 schema 제약이 걸린 JSON 출력을 사용해 재시도하고, 빠진 소스 세부 정보는 schema 강제로 채우게 합니다.
  - EN: Retry with schema-constrained JSON output using the same schema, and let schema enforcement fill in the missing source details.
- B. JA: 元の文書と拒否されたJSON、バリデーターのエラーをXMLタグで区切り、修正版だけを返させる新しいリクエストを送る。
  - KO: 원본 문서와 거부된 JSON, validator 오류를 XML 태그로 구분해 담고, 수정본만 반환하게 하는 새 요청을 보냅니다.
  - EN: Send a new request that delimits the original document, the rejected JSON, and the validator errors with XML tags, and asks for only the corrected version to be returned.
- C. JA: バリデーターのエラーだけを含む短い修正リクエストを送り、どのフィールドをどう直すかは前回の試行からClaudeに推測させる。
  - KO: validator 오류만 담은 짧은 수정 요청을 보내고, 어떤 필드를 어떻게 고칠지는 이전 시도를 바탕으로 Claude가 추측하게 합니다.
  - EN: Send a short correction request containing only the validator errors, and have Claude infer from the previous attempt which fields to fix and how.
- D. JA: temperatureを0にし、元の文書とスキーマに「JSONの妥当性にもっと注意して」という指示を添えて、最初の抽出をリトライする。
  - KO: temperature를 0으로 하고, 원본 문서와 schema에 "JSON의 유효성에 더 주의하세요"라는 지시를 덧붙여 처음 추출을 재시도합니다.
  - EN: Retry the initial extraction with temperature set to 0, adding the instruction "pay more attention to JSON validity" to the original document and schema.

## CCAR-F-Udemy01-0026

**JA** あるフィンテック企業の開発ツールチームは、Claude Codeに2つのMCPサーバーを追加しました。その後、次のような誤りがよく起きています。

開発者がリポジトリ内のシンボルについて質問すると、Claude Codeがドキュメント検索ツールを呼び出す

開発者がフレームワークのポリシーページについて質問すると、Claude Codeがリポジトリ検索ツールを呼び出す

ツールの名前はそれぞれ異なりますが、どちらも検索型の質問を受け付けます。

ツール選択の信頼性を改善するために、このチームがまず変更すべきことはどれですか。

**KO** 한 핀테크 기업의 개발 도구 팀은 Claude Code에 MCP server 2개를 추가했습니다. 그 뒤로 다음과 같은 오류가 자주 일어나고 있습니다.

개발자가 저장소 안의 심볼에 대해 질문하면, Claude Code가 문서 검색 도구를 호출합니다

개발자가 프레임워크의 정책 페이지에 대해 질문하면, Claude Code가 저장소 검색 도구를 호출합니다

두 도구의 이름은 서로 다르지만, 둘 다 검색형 질문을 받습니다.

도구 선택의 신뢰성을 개선하기 위해 이 팀이 가장 먼저 바꿔야 할 것은 무엇입니까?

- A. JA: 各ツールの説明を、使うべき場面と使うべきでない場面、入力の形式と返す内容まで具体的に書き直す。
  - KO: 각 도구의 설명을, 써야 할 상황과 쓰지 말아야 할 상황, 입력 형식과 반환 내용까지 구체적으로 다시 씁니다.
  - EN: Rewrite each tool's description to be specific about when to use it and when not to, including the input format and what it returns.
- B. JA: 各タスクを始める前に、開発者に正しい検索ツールを選ばせるプロジェクト用スラッシュコマンドを追加する。
  - KO: 각 작업을 시작하기 전에 개발자가 올바른 검색 도구를 고르게 하는 프로젝트용 slash command를 추가합니다.
  - EN: Add a project slash command that makes developers choose the correct search tool before starting each task.
- C. JA: 対象のデータソースが分かる長い名前に各ツールを改名し、既存の説明文は変えずに残しておく。
  - KO: 대상 데이터 소스를 알 수 있는 긴 이름으로 각 도구의 이름을 바꾸고, 기존 설명은 바꾸지 않고 그대로 둡니다.
  - EN: Rename each tool with a longer name that identifies its target data source, leaving the existing descriptions unchanged.
- D. JA: リポジトリ検索が失敗するまではドキュメント検索ツールを使わないよう、CLAUDE.mdに指示を追加する。
  - KO: 저장소 검색이 실패하기 전까지는 문서 검색 도구를 쓰지 않도록 CLAUDE.md에 지시를 추가합니다.
  - EN: Add an instruction to CLAUDE.md not to use the documentation search tool until the repository search fails.

## CCAR-F-Udemy01-0027

**JA** あなたは、Claudeを使用して、通関用の出荷マニフェストから情報を抽出する構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携する必要があります。

抽出バリデーターと下流提出用ツールは現在、is_errorをtrueに設定したtool_resultブロックを返しています。しかし、その内容は、次のどの場合でも常に"Operation failed"という同じ文字列です。

スキーマ検証の失敗

元データの形式不正

サービスのタイムアウト

権限拒否

ログを見ると、Claudeはリトライ不可能な失敗をリトライしたり、リトライ可能な失敗を一貫性なくエスカレーションしたりしています。

復旧動作を最も改善する変更はどれですか。（2つ選択してください。）

**KO** 당신은 Claude를 사용해, 통관용 선적 매니페스트에서 정보를 추출하는 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동해야 합니다.

추출 validator와 downstream 제출용 도구는 현재 is_error를 true로 설정한 tool_result 블록을 반환하고 있습니다. 그러나 그 내용은 다음 중 어떤 경우든 항상 "Operation failed"라는 같은 문자열입니다.

schema 검증 실패

원본 데이터의 형식 오류

서비스 timeout

권한 거부

로그를 보면 Claude는 재시도할 수 없는 실패를 재시도하거나, 재시도할 수 있는 실패를 일관성 없이 escalation하고 있습니다.

복구 동작을 가장 크게 개선하는 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: ツールの説明文を拡張し、汎用的な失敗には多くの原因がありうることをClaudeに説明しておく。
  - KO: 도구 설명을 확장해, 일반적인 실패에는 여러 원인이 있을 수 있다고 Claude에게 설명해 둡니다.
  - EN: Expand the tool descriptions to explain to Claude that a generic failure can have many causes.
- B. JA: 失敗の分類とリトライ可否、具体的なメッセージと是正のヒントを構造化したtool_resultエラーを返す。
  - KO: 실패 분류와 재시도 가능 여부, 구체적인 메시지와 해결 힌트를 구조화한 tool_result 오류를 반환합니다.
  - EN: Return a structured tool_result error that includes the failure category, whether it is retryable, a specific message, and a remediation hint.
- C. JA: タイムアウトのようにリトライ可能と分類できる失敗だけをバックオフ付きでリトライし、他はエラーとして返す。
  - KO: timeout처럼 재시도 가능으로 분류할 수 있는 실패만 backoff를 두고 재시도하고, 나머지는 오류로 반환합니다.
  - EN: Retry with backoff only failures that can be classified as retryable, such as timeouts, and return all others as errors.
- D. JA: 失敗した抽出ツールの呼び出し結果を、下流の提出用スキーマを満たす空のJSONオブジェクトに置き換えて返す。
  - KO: 실패한 추출 도구의 호출 결과를, downstream 제출용 schema를 만족하는 빈 JSON 객체로 바꿔 반환합니다.
  - EN: Replace the result of a failed extraction tool call with an empty JSON object that satisfies the downstream submission schema.

## CCAR-F-Udemy01-0028

**JA** インフラ構成のコード化（IaC）作業を支援するため、Messages APIの上に自作のオーケストレータを構築しています。オーケストレータは、サブエージェントに調査を委任するAgent相当のツールをClaudeが使えるようにしており、変更を提案する前に、ネットワークトポロジー、IAMポリシー、コスト見積もりを調査させます。

ログを見ると、この3つの調査は互いに独立しているにもかかわらず、メインスレッドは次の順に1つずつ処理しています。

ネットワークトポロジーのサブエージェントを起動し、その要約を待つ

IAMポリシーのサブエージェントを起動し、その要約を待つ

コスト見積もりのサブエージェントを起動する

分析の範囲を変えずに、このツール呼び出しの逐次化を最も減らせる変更はどれですか。（2つ選択してください。）

**KO** 인프라 구성의 코드화(IaC) 작업을 지원하기 위해 Messages API 위에 자체 orchestrator를 구축하고 있습니다. orchestrator는 subagent에게 조사를 위임하는, Agent에 해당하는 도구를 Claude가 쓸 수 있게 하고, 변경을 제안하기 전에 네트워크 토폴로지, IAM 정책, 비용 견적을 조사하게 합니다.

로그를 보면 이 세 조사는 서로 독립적인데도, 메인 스레드는 다음 순서로 하나씩 처리하고 있습니다.

네트워크 토폴로지 subagent를 실행하고 그 요약을 기다립니다

IAM 정책 subagent를 실행하고 그 요약을 기다립니다

비용 견적 subagent를 실행합니다

분석 범위를 바꾸지 않고, 이렇게 도구 호출이 순차로 처리되는 것을 가장 줄일 수 있는 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 1ターンに1つのAgent呼び出しを保ち、各サブエージェントの最終結果を待ってから次をbackground指定で起動する。
  - KO: 한 turn에 Agent 호출 하나를 유지하고, 각 subagent의 최종 결과를 기다린 뒤 다음 것을 background 지정으로 실행합니다.
  - EN: Keep one Agent call per turn, waiting for each subagent's final result before launching the next with the background option.
- B. JA: 各サブエージェントの要約を完了直後に個別のuserメッセージで返し、全部揃ってからメインスレッドを進める。
  - KO: 각 subagent의 요약을 완료 직후 개별 user 메시지로 반환하고, 모두 모인 뒤 메인 스레드를 진행합니다.
  - EN: Return each subagent's summary in its own separate user message immediately upon completion, and advance the main thread only after all have arrived.
- C. JA: 独立したAgent呼び出しを1回のアシスタントターンでまとめて発行し、結果は次のuserメッセージでまとめて返す。
  - KO: 독립된 Agent 호출을 한 번의 assistant turn에서 한꺼번에 발행하고, 결과는 다음 user 메시지로 한꺼번에 반환합니다.
  - EN: Issue the independent Agent calls together in a single assistant turn, and return the results together in the next user message.
- D. JA: tool_choiceのdisable_parallel_tool_useを既定値のfalseから変更しない。
  - KO: tool_choice의 disable_parallel_tool_use를 기본값인 false에서 바꾸지 않습니다.
  - EN: Leave tool_choice's disable_parallel_tool_use at its default value of false.

## CCAR-F-Udemy01-0029

**JA** ある開発チームが、Claude Codeの/reviewコマンドを運用しています。このコマンドには詳細なレビュー基準と固定の出力テンプレートがありますが、見慣れないリファクタリングに対しては挙動が一貫しません。具体的には、次のことが起きています。

無害なローカルの慣習を、欠陥として誤って指摘することがある

チェックリストの例とは異なる実際の欠陥を、見逃すことがある

次に取るべきプロンプトの変更として、最も適切なものはどれですか。

**KO** 한 개발팀이 Claude Code의 /review 명령을 운영하고 있습니다. 이 명령에는 상세한 리뷰 기준과 고정된 출력 템플릿이 있지만, 익숙하지 않은 refactoring에 대해서는 동작이 일관되지 않습니다. 구체적으로는 다음과 같은 일이 일어나고 있습니다.

무해한 로컬 관례를 결함으로 잘못 지적하는 경우가 있습니다

체크리스트의 예와 다른 실제 결함을 놓치는 경우가 있습니다

다음에 해야 할 prompt 변경으로 가장 적절한 것은 무엇입니까?

- A. JA: これまでに見られたすべてのパターンを列挙する大きなチェックリストを追加し、完全一致した場合にのみ報告するよう指示する。
  - KO: 지금까지 나온 모든 패턴을 나열한 큰 체크리스트를 추가하고, 완전히 일치하는 경우에만 보고하라고 지시합니다.
  - EN: Add a large checklist enumerating every pattern seen so far, and instruct it to report only on exact matches.
- B. JA: 問題あり・問題なしの両方の事例を、判断の境界を示す簡潔な理由付きで多様に示すfew-shotの例を追加する。
  - KO: 문제가 있는 사례와 없는 사례를 모두, 판단의 경계를 보여 주는 간결한 이유와 함께 다양하게 보여 주는 few-shot 예시를 추가합니다.
  - EN: Add few-shot examples that show both problematic and non-problematic cases, varied, with brief reasoning that shows where the judgment boundary lies.
- C. JA: 直近の1件のリファクタリングから抜き出した複数の例を追加し、その表現や重大度ラベルをそのままコピーするよう指示する。
  - KO: 가장 최근 refactoring 한 건에서 뽑은 예시 여러 개를 추가하고, 그 표현과 심각도 라벨을 그대로 복사하라고 지시합니다.
  - EN: Add several examples extracted from the single most recent refactoring, and instruct it to copy their wording and severity labels exactly.
- D. JA: 例を示さず、レビュー担当は保守的であるべきだと述べるCLAUDE.mdのルールを追加する。
  - KO: 예시 없이, 리뷰어는 보수적이어야 한다고 적은 CLAUDE.md 규칙을 추가합니다.
  - EN: Add a CLAUDE.md rule stating that the reviewer should be conservative, without giving any examples.

## CCAR-F-Udemy01-0030

**JA** あなたは、コンプライアンス担当者が保険金請求ファイルを数週間かけて監査する作業を支援するエージェントを構築しています。このエージェントは、組み込みツール（Read、Write、Bash、Grep、Glob）を使用し、Model Context Protocol（MCP）サーバーとも連携します。

レガシーな請求処理システムを1か月にわたって調査する過程で、エージェントが生成する経過サマリーの中の正確な数値・条件が、次のようにあいまいな表現に置き換わっていってしまいます。

「エスカレーション基準額は3000ドル」→「そこそこの基準額」

「応答SLAは99.95%」→「高い可用性」

「契約更新の締切は2026年6月30日」→「近い将来の締切」

「契約上、期中の保険料変更は行わない」→「安定した保険料」

後続の作業で誤った修正が行われるリスクを減らすために、行うべき変更はどれですか。（2つ選択してください。）

**KO** 당신은 컴플라이언스 담당자가 보험금 청구 파일을 몇 주에 걸쳐 감사하는 작업을 돕는 agent를 구축하고 있습니다. 이 agent는 내장 도구(Read, Write, Bash, Grep, Glob)를 사용하고 Model Context Protocol(MCP) server와도 연동합니다.

레거시 청구 처리 시스템을 한 달에 걸쳐 조사하는 동안, agent가 생성하는 진행 요약 속의 정확한 수치·조건이 다음과 같이 모호한 표현으로 바뀌어 갑니다.

"escalation 기준액은 3000달러" → "적당한 기준액"

"응답 SLA는 99.95%" → "높은 가용성"

"계약 갱신 마감은 2026년 6월 30일" → "가까운 시일 내의 마감"

"계약상 기간 중 보험료 변경은 하지 않음" → "안정적인 보험료"

이후 작업에서 잘못된 수정이 이루어질 위험을 줄이기 위해 해야 할 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: サマリーでは数値や日付、契約条件を言い換えず、原文のまま残すことを必須にする。
  - KO: 요약에서 수치, 날짜, 계약 조건을 바꿔 말하지 않고 원문 그대로 남기도록 의무화합니다.
  - EN: Require that summaries keep figures, dates, and contract terms verbatim from the source rather than paraphrasing them.
- B. JA: 大まかな意図を優先してサマリーを書き直させ、エージェントが追跡すべき細部を減らす。
  - KO: 대략적인 의도를 우선해 요약을 다시 쓰게 하고, agent가 추적해야 할 세부 사항을 줄입니다.
  - EN: Have the agent rewrite summaries to prioritize the general intent, reducing the details it needs to track.
- C. JA: 生のツール出力をコンテキストに多めに残し、ウィンドウがほぼ埋まってから要約させる。
  - KO: 원본 도구 출력을 context에 넉넉히 남겨 두고, window가 거의 찬 뒤에 요약하게 합니다.
  - EN: Keep more raw tool output in context, and summarize only once the window is nearly full.
- D. JA: 圧縮される会話履歴とは別に、正確な事実を記録する構造化スクラッチパッドを維持して更新する。
  - KO: 압축되는 대화 기록과 별도로, 정확한 사실을 기록하는 구조화된 scratchpad를 유지하고 갱신합니다.
  - EN: Maintain and update a structured scratchpad that records exact facts, separate from the conversation history that gets compressed.

## CCAR-F-Udemy01-0031

**JA** あるオンライン学習プラットフォームの開発チームは、アプリケーションのエラーログからサポートチケットを自動作成する独自のMCPツールを、Claude Codeに追加しました。

サポートチケット発行サービスが不正な形式のコースIDを拒否した場合、アダプタ（MCPサーバー）はこの失敗をツール結果としてClaudeに返し、Claudeが状況を把握して復旧できるようにする必要があります。

アダプタが返す内容として適切なものはどれですか。（2つ選択してください。）

**KO** 한 온라인 학습 플랫폼의 개발팀은 애플리케이션 오류 로그로 지원 티켓을 자동 생성하는 자체 MCP 도구를 Claude Code에 추가했습니다.

지원 티켓 발행 서비스가 형식이 잘못된 강좌 ID를 거부하면, adapter(MCP server)는 이 실패를 도구 결과로 Claude에 돌려주어 Claude가 상황을 파악하고 복구할 수 있게 해야 합니다.

adapter가 반환할 내용으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: isError: trueを付け、チケットが作成されていないことと候補のコースIDを含むJSONをcontentに入れて返す。
  - KO: isError: true를 붙이고, 티켓이 생성되지 않았다는 사실과 후보 강좌 ID를 담은 JSON을 content에 넣어 반환합니다.
  - EN: Return isError: true, with JSON in content stating that no ticket was created and listing candidate course IDs.
- B. JA: isError: trueを付け、エラー分類とリトライ可否、正しいID形式の例を含むJSONをcontentに入れて返す。
  - KO: isError: true를 붙이고, 오류 분류와 재시도 가능 여부, 올바른 ID 형식의 예를 담은 JSON을 content에 넣어 반환합니다.
  - EN: Return isError: true, with JSON in content containing the error category, whether it is retryable, and an example of the correct ID format.
- C. JA: isError: trueを付け、「操作に失敗しました。しばらくしてからリトライしてください。」という汎用の文字列をcontentに入れて返す。
  - KO: isError: true를 붙이고, "작업에 실패했습니다. 잠시 후 다시 시도해 주세요."라는 일반적인 문자열을 content에 넣어 반환합니다.
  - EN: Return isError: true, with the generic string "The operation failed. Please try again later." in content.
- D. JA: ツール呼び出しを未捕捉の例外で終了させ、チケット発行サービスの応答内容はClaude Codeのデバッグログで確認する。
  - KO: 도구 호출을 처리되지 않은 예외로 종료시키고, 티켓 발행 서비스의 응답 내용은 Claude Code의 디버그 로그에서 확인합니다.
  - EN: End the tool call with an uncaught exception, and check the ticketing service's response in Claude Code's debug logs.

## CCAR-F-Udemy01-0032

**JA** あなたは、Claude Agent SDKを使用して、特許の先行技術調査を行うマルチエージェントシステムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、特許データベースを検索するもの、先行技術文書を解析するもの、調査結果を統合するもの、新規性レポートを生成するものがあります。

テスト中、文書解析サブエージェントが、抽出した複数のレコードにクレーム（請求項）の要約が欠けているという理由で、検証に繰り返し失敗しています。ログを確認すると、これらの特許についてサブエージェントには要約ページしか渡されていませんでした。クレームのセクションは別ファイルにあり、そもそもサブエージェントに提供されていなかったことが分かりました。

チームが最初に変更すべきことはどれですか。

**KO** 당신은 Claude Agent SDK를 사용해 특허 선행 기술 조사를 하는 multi-agent 시스템을 구축하고 있습니다. coordinator agent가 전문화된 subagent에게 작업을 위임합니다. subagent에는 특허 데이터베이스를 검색하는 것, 선행 기술 문서를 분석하는 것, 조사 결과를 통합하는 것, 신규성 보고서를 생성하는 것이 있습니다.

테스트 중에 문서 분석 subagent가, 추출한 여러 레코드에 청구항 요약이 빠져 있다는 이유로 검증에 계속 실패하고 있습니다. 로그를 확인하니 이 특허들에 대해 subagent에는 요약 페이지만 전달되었습니다. 청구항 섹션은 별도 파일에 있었고, 애초에 subagent에 제공되지 않았던 것으로 드러났습니다.

팀이 가장 먼저 바꿔야 할 것은 무엇입니까?

- A. JA: 検証エラーを添えて、すべてのクレーム要約フィールドが埋まるまで同じ抽出をリトライする。
  - KO: 검증 오류를 첨부해, 모든 청구항 요약 필드가 채워질 때까지 같은 추출을 재시도합니다.
  - EN: Retry the same extraction with the validation error attached until all claim summary fields are filled.
- B. JA: 抽出ツールでstrictなツール使用を有効にし、ツール呼び出しの際に欠けているクレームの内容を復元できるようにする。
  - KO: 추출 도구에서 strict 도구 사용을 활성화해, 도구 호출 시 빠진 청구항 내용을 복원할 수 있게 합니다.
  - EN: Enable strict tool use on the extraction tool so that the missing claim content can be recovered at tool call time.
- C. JA: クレーム要約のfew-shot例を追加し、サブエージェントが欠けているセクションを一貫して推測できるようにする。
  - KO: 청구항 요약의 few-shot 예시를 추가해, subagent가 빠진 섹션을 일관되게 추측할 수 있게 합니다.
  - EN: Add few-shot examples of claim summaries so that the subagent can consistently infer the missing sections.
- D. JA: 欠けているクレームの情報源を提供し、根拠となる情報がコンテキストに無い場合は「利用不可」の値を許容するようにする。
  - KO: 빠진 청구항의 정보원을 제공하고, 근거가 되는 정보가 context에 없으면 "이용 불가" 값을 허용합니다.
  - EN: Provide the source for the missing claims, and allow an "unavailable" value when the grounding information is not in context.

## CCAR-F-Udemy01-0033

**JA** Claudeを使用して、構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携する必要があります。

評価中、記載されたコンテナ総数と明細行の合計が食い違う出荷マニフェストが、レビュー段階をすり抜けてしまうことがよくあります。

現在のフローでは、まずClaudeにJSONを抽出させます。その後、同じ会話の中で、「アプリケーションがスキーマ検証を実行する前に、直前の抽出結果を確認してください」というフォローアップのプロンプトを続けて送っています。

検証ステップ自体は維持しつつ、このレビューの見落としに最も効果的に対処できる変更はどれですか。

**KO** Claude를 사용해 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동해야 합니다.

평가 중에, 기재된 컨테이너 총수와 명세 행의 합계가 어긋나는 선적 매니페스트가 검토 단계를 빠져나가는 일이 자주 있습니다.

현재 흐름에서는 먼저 Claude에게 JSON을 추출하게 합니다. 그다음 같은 대화 안에서 "애플리케이션이 schema 검증을 실행하기 전에 직전 추출 결과를 확인해 주세요"라는 후속 prompt를 이어서 보내고 있습니다.

검증 단계 자체는 유지하면서, 이 검토 누락에 가장 효과적으로 대처할 수 있는 변경은 무엇입니까?

- A. JA: 抽出結果を合成のアシスタントメッセージとして会話に挿入し、Claudeにそれをスキーマと照合して監査するよう求める。
  - KO: 추출 결과를 담아 인위적으로 만든 assistant 메시지로 대화에 끼워 넣고, Claude에게 그것을 schema와 대조해 감사하라고 요청합니다.
  - EN: Insert the extraction result into the conversation as a synthetic assistant message, and ask Claude to audit it against the schema.
- B. JA: 元の文書、抽出されたJSON、明示的な不整合判定基準を受け取る独立したレビューリクエストを別途実行する。
  - KO: 원본 문서, 추출된 JSON, 명시적인 불일치 판정 기준을 받는 독립된 검토 요청을 따로 실행합니다.
  - EN: Run a separate, independent review request that receives the original document, the extracted JSON, and explicit inconsistency criteria.
- C. JA: 検証の前にClaudeへ、自分の直前の抽出結果に懐疑的になるよう求めるフォローアップのプロンプトを追加する。
  - KO: 검증 전에 Claude에게 자신의 직전 추출 결과를 의심해 보라고 요구하는 후속 prompt를 추가합니다.
  - EN: Add a follow-up prompt before validation asking Claude to be skeptical of its own previous extraction result.
- D. JA: スキーマ検証を実行する前に、抽出した各フィールドに確信度の値を含めることを必須にする。
  - KO: schema 검증을 실행하기 전에, 추출한 각 필드에 확신도 값을 반드시 포함하게 합니다.
  - EN: Require each extracted field to include a confidence value before schema validation runs.

## CCAR-F-Udemy01-0034

**JA** あるゲームスタジオの開発者ツールチームは、Claude Agent SDKを使用して開発者の生産性向上ツールを構築しています。このエージェントは、エンジニアが不慣れなコードベースを探索し、レガシーシステムを理解し、ボイラープレートコードを生成し、反復的なタスクを自動化するのを支援します。組み込みツール（Read、Write、Bash、Grep、Glob）を使用し、MCPサーバーとも連携します。

このチームは、変更されたファイルをレビューしてインラインで提案コメントを投稿するCIコマンドを、追加しようとしています。要件は次のとおりです。

PRボットは、file・line・severity・messageのフィールドを持つアプリケーションスキーマに一致するJSONオブジェクトを受け取る

Claudeが有効なデータを生成できない場合は、コメントを投稿せずに失敗させる

経費計算のための実行メタデータも取得する

採用すべき実装はどれですか。（2つ選択してください。）

**KO** 한 게임 스튜디오의 개발자 도구 팀은 Claude Agent SDK를 사용해 개발자 생산성 향상 도구를 구축하고 있습니다. 이 agent는 엔지니어가 익숙하지 않은 코드베이스를 탐색하고, 레거시 시스템을 이해하고, boilerplate 코드를 생성하고, 반복 작업을 자동화하도록 돕습니다. 내장 도구(Read, Write, Bash, Grep, Glob)를 사용하고 MCP server와도 연동합니다.

이 팀은 변경된 파일을 리뷰하고 인라인으로 제안 댓글을 다는 CI 명령을 추가하려고 합니다. 요구 사항은 다음과 같습니다.

PR 봇은 file·line·severity·message 필드를 가진 애플리케이션 schema에 맞는 JSON 객체를 받습니다

Claude가 유효한 데이터를 생성하지 못하면, 댓글을 달지 않고 실패로 처리합니다

비용 정산을 위한 실행 metadata도 가져옵니다

채택해야 할 구현은 무엇입니까? (2개를 선택하십시오.)

- A. JA: Claude Codeを既定のテキスト出力で実行し、スキーマに沿ったJSONだけを返すようプロンプトで指示する。
  - KO: Claude Code를 기본 텍스트 출력으로 실행하고, schema에 맞는 JSON만 반환하라고 prompt로 지시합니다.
  - EN: Run Claude Code with the default text output, and instruct it in the prompt to return only JSON that conforms to the schema.
- B. JA: Claude Codeを-pと--output-format jsonで実行し、結果のJSONに含まれるコストや所要時間を経費計算に使う。
  - KO: Claude Code를 -p와 --output-format json으로 실행하고, 결과 JSON에 담긴 비용과 소요 시간을 비용 정산에 사용합니다.
  - EN: Run Claude Code with -p and --output-format json, and use the cost and duration in the resulting JSON for expense accounting.
- C. JA: Claude Codeを-pと--output-format jsonに--json-schemaを加えて実行し、structured_outputを読み取る。
  - KO: Claude Code를 -p와 --output-format json에 --json-schema를 더해 실행하고, structured_output을 읽습니다.
  - EN: Run Claude Code with -p and --output-format json plus --json-schema, and read structured_output.
- D. JA: Claude Codeを-pと--output-format stream-jsonで実行し、流れてくる各イベントをレビュー結果として検証する。
  - KO: Claude Code를 -p와 --output-format stream-json으로 실행하고, 흘러 들어오는 각 이벤트를 리뷰 결과로 검증합니다.
  - EN: Run Claude Code with -p and --output-format stream-json, and validate each streamed event as a review result.

## CCAR-F-Udemy01-0035

**JA** ある旅行予約プラットフォームのエンジニアリングチームは、社内オペレーター向けの支援エージェントをMessages APIで構築しています。アプリケーションは自前のMCPクライアントで、予約・決済・在庫・顧客管理・チケット管理・監視の6つのMCPサーバーに接続し、取得した約220個のツール定義をすべてtoolsに渡しています。

オペレーターの依頼がどの業務領域にまたがるかは事前に分からないため、1つの会話からどのツールも使える状態を保つ必要があります。

最近の計測で、次のことが分かりました。

作業を始める前から、ツール定義だけで約6万トークンを消費している

名前の似たツールを取り違える呼び出しが増えている

このチームが行うべき変更はどれですか。

**KO** 한 여행 예약 플랫폼의 엔지니어링 팀은 사내 운영자용 지원 agent를 Messages API로 구축하고 있습니다. 애플리케이션은 자체 MCP client로 예약·결제·재고·고객 관리·티켓 관리·모니터링의 6개 MCP server에 연결하고, 가져온 약 220개의 도구 정의를 모두 tools에 전달하고 있습니다.

운영자의 요청이 어떤 업무 영역에 걸칠지 미리 알 수 없으므로, 하나의 대화에서 어떤 도구든 쓸 수 있는 상태를 유지해야 합니다.

최근 측정에서 다음 사실이 확인되었습니다.

작업을 시작하기도 전에 도구 정의만으로 약 6만 토큰을 소비하고 있습니다

이름이 비슷한 도구를 혼동하는 호출이 늘고 있습니다

이 팀이 해야 할 변경은 무엇입니까?

- A. JA: ツール検索ツールをtoolsに加え、よく使う数個を除くツール定義にdefer_loading: trueを付ける。
  - KO: tool search tool을 tools에 추가하고, 자주 쓰는 몇 개를 제외한 도구 정의에 defer_loading: true를 붙입니다.
  - EN: Add a tool search tool to tools, and set defer_loading: true on all tool definitions except a few frequently used ones.
- B. JA: 各ツールのdescriptionを1行程度に短くし、ツール定義全体のトークン数を削減する。
  - KO: 각 도구의 description을 한 줄 정도로 줄여, 도구 정의 전체의 토큰 수를 줄입니다.
  - EN: Shorten each tool's description to about one line to reduce the total token count of the tool definitions.
- C. JA: tool_choiceを{"type": "any"}に設定し、各ターンでいずれかのツールを呼び出させる。
  - KO: tool_choice를 {"type": "any"}로 설정해, 매 turn 어떤 도구든 하나를 호출하게 합니다.
  - EN: Set tool_choice to {"type": "any"} so that some tool is called on every turn.
- D. JA: toolsの最後の定義にcache_controlを付け、すべてのツール定義をプロンプトキャッシュの対象にする。
  - KO: tools의 마지막 정의에 cache_control을 붙여, 모든 도구 정의를 prompt caching 대상으로 만듭니다.
  - EN: Attach cache_control to the last definition in tools so that all tool definitions are covered by prompt caching.

## CCAR-F-Udemy01-0036

**JA** あなたは、Claude Agent SDKを使用して、財務監査レポートを分析するマルチエージェントシステムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、規制当局への提出書類を検索するもの、財務諸表を解析するもの、開示情報を突き合わせるもの、監査所見のレポートを作成するものがあります。

長時間のデバッグセッションの中で、財務諸表解析やクロスリファレンスの出力段階では存在していた引用情報が、最終レポートでは失われてしまうことがあります。

チームは、次のような具体的な疑問をClaude Codeに調査させたいと考えています。

引用情報はどこに保存されているか

統合処理のどこで書き換えが起きているか

レポート生成をどのテストがカバーしているか

その際、メインの会話は、生の検索ログやファイル内容ではなく、調整作業に集中させておきたいと考えています。

この目的に最も適した作業フローはどれですか。

**KO** 당신은 Claude Agent SDK를 사용해 재무 감사 보고서를 분석하는 multi-agent 시스템을 구축하고 있습니다. coordinator agent가 전문화된 subagent에게 작업을 위임합니다. subagent에는 규제 당국 제출 서류를 검색하는 것, 재무제표를 분석하는 것, 공시 정보를 대조하는 것, 감사 소견 보고서를 작성하는 것이 있습니다.

긴 디버깅 session 중에, 재무제표 분석이나 교차 참조의 출력 단계에서는 있던 인용 정보가 최종 보고서에서는 사라지는 경우가 있습니다.

팀은 다음과 같은 구체적인 질문을 Claude Code가 조사하게 하려고 합니다.

인용 정보가 어디에 저장되어 있는지

통합 처리의 어느 부분에서 재작성이 일어나는지

보고서 생성을 어떤 테스트가 커버하고 있는지

이때 메인 대화는 원본 검색 로그나 파일 내용이 아니라 조정 작업에 집중하게 하려고 합니다.

이 목적에 가장 적합한 작업 흐름은 무엇입니까?

- A. JA: 汎用（general-purpose）サブエージェントに、引用消失の原因を調査させながらレポート生成コードの修正も行わせる。
  - KO: 범용(general-purpose) subagent에게 인용 소실의 원인을 조사하게 하면서 보고서 생성 코드 수정도 함께 맡깁니다.
  - EN: Have a general-purpose subagent investigate the cause of the citation loss while also fixing the report generation code.
- B. JA: 焦点を絞った読み取り専用の調査をサブエージェントに委任し、返された要約をメインの会話で活用する。
  - KO: 초점을 좁힌 읽기 전용 조사를 subagent에 위임하고, 반환된 요약을 메인 대화에서 활용합니다.
  - EN: Delegate focused, read-only investigations to subagents, and use the summaries they return in the main conversation.
- C. JA: 調査ごとに独立したClaude Codeセッションを実行し、その完全なトランスクリプトをメインの会話に貼り付ける。
  - KO: 조사마다 독립된 Claude Code session을 실행하고, 그 전체 transcript를 메인 대화에 붙여 넣습니다.
  - EN: Run a separate Claude Code session for each investigation, and paste its full transcript into the main conversation.
- D. JA: メインの会話に関連するすべてのファイルを直接調べさせ、各フェーズの後に会話をコンパクト化する。
  - KO: 메인 대화에서 관련된 모든 파일을 직접 조사하게 하고, 각 단계가 끝날 때마다 대화를 compact합니다.
  - EN: Have the main conversation directly examine all relevant files, and compact the conversation after each phase.

## CCAR-F-Udemy01-0037

**JA** あるチームは、Claude Agent SDKを使用して、複数のサブエージェントを統括するマルチエージェントの調査システムを構築しています。コーディネーターエージェントは、専門化されたサブエージェント（Web検索担当、資料分析担当、知見の統合担当、レポート生成担当）に作業を委任します。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

カスタムのMCPサーバーが、複数のサブエージェントが調査中に必要とする出典データベースと資料カタログを公開しています。あるメンバーが、自分のノートPC上でClaude CodeのMCPコマンドを既定のまま使ってこのサーバーを追加しました。しかし、他のメンバーがリポジトリをクローンしても、そのサーバーは見えません。

また、チームとしては、認証情報をソース管理にコミットしたくないと考えています。

このチームが取るべき行動はどれですか。（2つ選択してください。）

**KO** 한 팀은 Claude Agent SDK를 사용해 여러 subagent를 총괄하는 multi-agent 조사 시스템을 구축하고 있습니다. coordinator agent는 전문화된 subagent(웹 검색 담당, 자료 분석 담당, 발견 사항 통합 담당, 보고서 생성 담당)에게 작업을 위임합니다. 이 시스템은 주제를 조사하고 출처를 명시한 포괄적인 보고서를 작성합니다.

custom MCP server가, 여러 subagent가 조사 중에 필요로 하는 출처 데이터베이스와 자료 카탈로그를 제공합니다. 한 팀원이 자신의 노트북에서 Claude Code의 MCP 명령을 기본값 그대로 사용해 이 server를 추가했습니다. 그런데 다른 팀원이 저장소를 clone해도 그 server가 보이지 않습니다.

또한 팀은 인증 정보를 소스 관리에 commit하고 싶지 않습니다.

이 팀이 취해야 할 행동은 무엇입니까? (2개를 선택하십시오.)

- A. JA: サーバーの認証情報は各メンバーがローカルで設定する環境変数に保持し、必要な環境変数名をオンボーディングガイドに記載する。
  - KO: server의 인증 정보는 각 팀원이 로컬에서 설정하는 환경 변수에 두고, 필요한 환경 변수 이름을 온보딩 가이드에 적습니다.
  - EN: Keep the server's credentials in environment variables that each team member sets locally, and list the required environment variable names in the onboarding guide.
- B. JA: サーバーを--scope projectで追加し直し、環境変数のプレースホルダーを使って生成された.mcp.jsonをコミットする。
  - KO: server를 --scope project로 다시 추가하고, 환경 변수 placeholder를 사용해 생성된 .mcp.json을 commit합니다.
  - EN: Re-add the server with --scope project, and commit the generated .mcp.json that uses environment variable placeholders.
- C. JA: サーバーを--scope userで追加し直し、各メンバーが自分の~/.claude.jsonに個別に設定し直すようにする。
  - KO: server를 --scope user로 다시 추가하고, 각 팀원이 자신의 ~/.claude.json에 개별적으로 다시 설정하게 합니다.
  - EN: Re-add the server with --scope user, and have each team member configure it again individually in their own ~/.claude.json.
- D. JA: 最初のメンバーの~/.claude.jsonをリポジトリにチェックインし、他のメンバーにそのファイルを再利用させる。
  - KO: 처음 추가한 팀원의 ~/.claude.json을 저장소에 체크인하고, 다른 팀원이 그 파일을 재사용하게 합니다.
  - EN: Check the first team member's ~/.claude.json into the repository, and have the other team members reuse that file.

## CCAR-F-Udemy01-0038

**JA** あるフィンテック企業のプラットフォームエンジニアリングチームは、Claude Agent SDKを使用して社内向けの開発者の生産性向上ツールを構築しています。このエージェントは、エンジニアが不慣れなコードベースを探索し、レガシーシステムを理解し、ボイラープレートコードを生成し、反復的なタスクを自動化するのを支援します。組み込みツール（Read、Write、Bash、Grep、Glob）を使用し、MCPサーバーとも連携します。

このチームは、Claude Code GitHub Actionsを使ったプルリクエストレビューのジョブを追加しようとしています。初期のレビューでは、リポジトリのテスト方針、フィクスチャの命名規則、スタイルに関する指摘を報告すべき基準が無視されています。

このガイダンスは、開発者間で共有され、かつCI実行中のClaude Codeからも参照できる状態にする必要があります。

このチームが取るべき行動はどれですか。（2つ選択してください。）

**KO** 한 핀테크 기업의 플랫폼 엔지니어링 팀은 Claude Agent SDK를 사용해 사내용 개발자 생산성 향상 도구를 구축하고 있습니다. 이 agent는 엔지니어가 익숙하지 않은 코드베이스를 탐색하고, 레거시 시스템을 이해하고, boilerplate 코드를 생성하고, 반복 작업을 자동화하도록 돕습니다. 내장 도구(Read, Write, Bash, Grep, Glob)를 사용하고 MCP server와도 연동합니다.

이 팀은 Claude Code GitHub Actions를 사용한 pull request 리뷰 job을 추가하려고 합니다. 초기 리뷰에서는 저장소의 테스트 방침, fixture 명명 규칙, 스타일 관련 지적을 보고해야 하는 기준이 무시되고 있습니다.

이 지침은 개발자 사이에 공유되면서, CI 실행 중인 Claude Code에서도 참조할 수 있어야 합니다.

이 팀이 취해야 할 행동은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 各CIランナーのイメージに、同じガイダンスを入れた~/.claude/CLAUDE.mdを配置しておく。
  - KO: 각 CI 러너 이미지에 같은 지침을 담은 ~/.claude/CLAUDE.md를 배치해 둡니다.
  - EN: Place a ~/.claude/CLAUDE.md containing the same guidance in each CI runner image.
- B. JA: フィクスチャの命名規則を書いたCLAUDE.mdをtestsディレクトリにコミットし、その配下の作業で読ませる。
  - KO: fixture 명명 규칙을 적은 CLAUDE.md를 tests 디렉터리에 commit해, 그 하위에서 작업할 때 읽게 합니다.
  - EN: Commit a CLAUDE.md describing the fixture naming conventions to the tests directory, so that it is read for work under that directory.
- C. JA: ガイダンスをワークフローのclaude_argsに書き、--append-system-promptでシステムプロンプトに追加する。
  - KO: 지침을 workflow의 claude_args에 적고, --append-system-prompt로 system prompt에 추가합니다.
  - EN: Put the guidance in the workflow's claude_args, and append it to the system prompt with --append-system-prompt.
- D. JA: テスト方針とフィクスチャの命名規則、レビュー基準を書いたCLAUDE.mdをリポジトリのルートにコミットする。
  - KO: 테스트 방침과 fixture 명명 규칙, 리뷰 기준을 적은 CLAUDE.md를 저장소 루트에 commit합니다.
  - EN: Commit a CLAUDE.md describing the testing policy, fixture naming conventions, and review criteria to the repository root.

## CCAR-F-Udemy01-0039

**JA** あなたは、IoTデバイスのファームウェア開発を加速するためにClaude Codeを使用しています。チームでは、コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行をどのように使い分けるかを理解する必要があります。

ある新人開発者から、Claude Codeがリポジトリのコーディングスタイルと単体テストの規約を適用してくれない、という報告がありました。シニアエンジニアは自分のマシンでは規約どおりの動作を再現できますが、新人開発者のマシンでは再現できません。チームは、関連する指示ファイルが新人開発者のセッションで実際に読み込まれているかどうかを把握できていません。

設定階層の問題を診断するために、まず行うべきことはどれですか。（2つ選択してください。）

**KO** 당신은 IoT 기기 펌웨어 개발을 빠르게 하기 위해 Claude Code를 사용하고 있습니다. 팀에서는 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 씁니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하고, plan mode와 직접 실행을 어떻게 구분해 쓸지 이해해야 합니다.

한 신입 개발자가 Claude Code가 저장소의 코딩 스타일과 단위 테스트 규약을 적용하지 않는다고 보고했습니다. 시니어 엔지니어는 자기 컴퓨터에서는 규약대로의 동작을 재현할 수 있지만, 신입 개발자의 컴퓨터에서는 재현할 수 없습니다. 팀은 관련 지시 파일이 신입 개발자의 session에서 실제로 로드되고 있는지 파악하지 못하고 있습니다.

설정 계층의 문제를 진단하기 위해 먼저 해야 할 일은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 新人開発者のセッションで/statusを実行し、StatusタブのSetting sourcesの行に並ぶ設定ファイルを確認する。
  - KO: 신입 개발자의 session에서 /status를 실행해, Status 탭의 Setting sources 줄에 나열된 설정 파일을 확인합니다.
  - EN: Run /status in the new developer's session and check the configuration files listed in the Setting sources row of the Status tab.
- B. JA: 関連するCLAUDE.mdが、新人のセッションで読み込まれる場所に実際に置かれているかを確認する。
  - KO: 관련 CLAUDE.md가 신입 개발자의 session에서 로드되는 위치에 실제로 놓여 있는지 확인합니다.
  - EN: Verify that the relevant CLAUDE.md is actually placed in a location that is loaded in the new developer's session.
- C. JA: チームの規約を新人開発者のマシンの.claude/settings.local.jsonに書き込み、その後の挙動を確認する。
  - KO: 팀의 규약을 신입 개발자 컴퓨터의 .claude/settings.local.json에 적은 뒤 동작을 확인합니다.
  - EN: Write the team's conventions into .claude/settings.local.json on the new developer's machine, then observe the behavior afterward.
- D. JA: 新人開発者のセッションで/contextを実行し、「Memory files」に並ぶ読み込み済みの指示ファイルを確認する。
  - KO: 신입 개발자의 session에서 /context를 실행해, "Memory files"에 나열된 로드된 지시 파일을 확인합니다.
  - EN: Run /context in the new developer's session and check the loaded instruction files listed under "Memory files".

## CCAR-F-Udemy01-0040

**JA** インフラ自動化の開発を加速するために、Claude Codeを使用しています。チームでは、コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行をどのように使い分けるかを理解する必要があります。

リポジトリには、すでに.claude/skills/code-review/SKILL.mdにチーム共有のプロジェクトスキルがあります。あなたは、自分専用のより厳格なレビューワークフローを、自分が関わるすべてのプロジェクトで使えるようにしたいと考えています。ただし、次のことは避けたいと考えています。

チームメイトの挙動を変える

既存の/code-reviewスキルを覆い隠す

取るべき対応として、最も適切なものはどれですか。

**KO** 인프라 자동화 개발을 빠르게 하기 위해 Claude Code를 사용하고 있습니다. 팀에서는 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 씁니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하고, plan mode와 직접 실행을 어떻게 구분해 쓸지 이해해야 합니다.

저장소에는 이미 .claude/skills/code-review/SKILL.md에 팀이 공유하는 프로젝트 skill이 있습니다. 당신은 자신만 쓰는 더 엄격한 리뷰 workflow를, 자신이 참여하는 모든 프로젝트에서 쓸 수 있게 하려고 합니다. 단, 다음은 피하려고 합니다.

팀원의 동작을 바꾸는 것

기존 /code-review skill을 가리는 것

가장 적절한 대응은 무엇입니까?

- A. JA: .claude/skills/code-review/SKILL.mdをより厳格なルールに編集し、/code-reviewとして呼び出す。
  - KO: .claude/skills/code-review/SKILL.md를 더 엄격한 규칙으로 편집하고, /code-review로 호출합니다.
  - EN: Edit .claude/skills/code-review/SKILL.md with stricter rules, and invoke it as /code-review.
- B. JA: プロジェクトのCLAUDE.mdにより厳格なレビュー指示を追記し、既存の/code-reviewを呼び出す。
  - KO: 프로젝트 CLAUDE.md에 더 엄격한 리뷰 지시를 추가하고, 기존 /code-review를 호출합니다.
  - EN: Add stricter review instructions to the project's CLAUDE.md, and invoke the existing /code-review.
- C. JA: ~/.claude/skills/my-code-review/SKILL.mdを作成し、/my-code-reviewとして呼び出す。
  - KO: ~/.claude/skills/my-code-review/SKILL.md를 만들고, /my-code-review로 호출합니다.
  - EN: Create ~/.claude/skills/my-code-review/SKILL.md, and invoke it as /my-code-review.
- D. JA: ~/.claude/skills/code-review/SKILL.mdを作成し、/code-reviewとして呼び出す。
  - KO: ~/.claude/skills/code-review/SKILL.md를 만들고, /code-review로 호출합니다.
  - EN: Create ~/.claude/skills/code-review/SKILL.md, and invoke it as /code-review.

## CCAR-F-Udemy01-0041

**JA** あるメディア分析企業のチームは、マルチエージェントの記事要約システムをClaude Codeで開発・保守しています。このシステムでは、コーディネーターが調査・分析・要約・レポート生成の各サブエージェントに作業を委任します。

このチームは、次のようにしたいと考えています。

引用や出典の扱いに関する規約は、すべての開発者に共有する

レポート生成サブエージェント固有のガイダンスは、そのサブエージェントの作業ディレクトリで作業する場合にだけ適用する

個人のエディタ設定の好みは、非公開のままにする

Claude Codeのメモリ階層に最も合致する設定方法はどれですか。

**KO** 한 미디어 분석 기업의 팀은 multi-agent 기사 요약 시스템을 Claude Code로 개발·유지보수하고 있습니다. 이 시스템에서는 coordinator가 조사·분석·요약·보고서 생성 subagent에게 작업을 위임합니다.

이 팀은 다음과 같이 하려고 합니다.

인용과 출처 처리에 관한 규약은 모든 개발자와 공유합니다

보고서 생성 subagent 고유의 지침은 그 subagent의 작업 디렉터리에서 작업할 때만 적용합니다

개인 에디터 설정 취향은 비공개로 유지합니다

Claude Code의 메모리 계층에 가장 잘 맞는 설정 방법은 무엇입니까?

- A. JA: 規約は~/.claude/CLAUDE.mdにまとめ、レポート生成向けの注記は.claude/settings.jsonに書き、各開発者に同じファイルをコピーさせる。
  - KO: 규약은 ~/.claude/CLAUDE.md에 모으고, 보고서 생성용 메모는 .claude/settings.json에 적은 뒤, 각 개발자가 같은 파일을 복사하게 합니다.
  - EN: Put the conventions together in ~/.claude/CLAUDE.md, write the notes for report generation in .claude/settings.json, and have each developer copy the same file.
- B. JA: 共有規約はレポート生成ディレクトリのCLAUDE.md、個人の好みはルートのCLAUDE.mdに置き、子の内容で親を上書きさせる。
  - KO: 공유 규약은 보고서 생성 디렉터리의 CLAUDE.md에, 개인 취향은 루트 CLAUDE.md에 두고, 하위 내용이 상위를 덮어쓰게 합니다.
  - EN: Put the shared conventions in the report generation directory's CLAUDE.md and personal preferences in the root CLAUDE.md, letting child content override the parent.
- C. JA: 共有規約はCLAUDE.local.md、レポート生成向けは~/.claude/CLAUDE.mdに置き、ユーザーレベルのファイルをチーム用にコミットする。
  - KO: 공유 규약은 CLAUDE.local.md에, 보고서 생성용은 ~/.claude/CLAUDE.md에 두고, 사용자 수준 파일을 팀용으로 commit합니다.
  - EN: Put the shared conventions in CLAUDE.local.md and the report generation guidance in ~/.claude/CLAUDE.md, and commit the user-level file for the team.
- D. JA: 共有規約はルートのCLAUDE.md、レポート生成向けはそのディレクトリのCLAUDE.md、個人の好みは~/.claude/CLAUDE.mdに置く。
  - KO: 공유 규약은 루트 CLAUDE.md에, 보고서 생성용은 해당 디렉터리의 CLAUDE.md에, 개인 취향은 ~/.claude/CLAUDE.md에 둡니다.
  - EN: Put the shared conventions in the root CLAUDE.md, the report generation guidance in that directory's CLAUDE.md, and personal preferences in ~/.claude/CLAUDE.md.

## CCAR-F-Udemy01-0042

**JA** あなたは、Claudeを使用して、経費精算文書から情報を抽出する構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携する必要があります。

検証の結果、抽出器が欠落した金額を、依然として次のように一貫性なく表現していることが分かりました。

null

空文字列

"N/A"

フィールドそのものの省略

簡潔な文章のルールはすでに追加しましたが、同じ失敗パターンが続いています。

次に行うべきことはどれですか。（2つ選択してください。）

**KO** 당신은 Claude를 사용해, 경비 정산 문서에서 정보를 추출하는 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동해야 합니다.

검증 결과, 추출기가 누락된 금액을 여전히 다음과 같이 일관성 없이 표현하고 있다는 사실이 드러났습니다.

null

빈 문자열

"N/A"

필드 자체의 생략

간결한 문장 규칙은 이미 추가했지만, 같은 실패 패턴이 계속되고 있습니다.

다음에 해야 할 일은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 典型的なケースとエッジケースの欠落値を含む、タグで区切った元の文書の抜粋と期待するJSONの例を3〜5個追加する。
  - KO: 전형적인 사례와 edge case의 누락값을 포함해, 태그로 구분한 원본 문서 발췌와 기대하는 JSON의 예시를 3~5개 추가합니다.
  - EN: Add 3 to 5 tag-delimited examples, each pairing an excerpt from the original document with the expected JSON, including missing values in both typical and edge cases.
- B. JA: 文章のルールに、欠落値を表す同義語と、正規化を求めるより強い言い回しを書き足す。
  - KO: 문장 규칙에 누락값을 뜻하는 동의어와, 정규화를 요구하는 더 강한 표현을 덧붙입니다.
  - EN: Add to the prose rule synonyms for missing values and stronger wording that demands normalization.
- C. JA: 正規化の要件をユーザーレベルのCLAUDE.mdに移し、すべてのローカルClaude Codeセッションで読み込まれるようにする。
  - KO: 정규화 요구 사항을 사용자 수준 CLAUDE.md로 옮겨, 모든 로컬 Claude Code session에서 로드되게 합니다.
  - EN: Move the normalization requirement into the user-level CLAUDE.md so that it is loaded in all local Claude Code sessions.
- D. JA: 採用する欠落値の表現をJSONスキーマ自体で定め、フィールドを必須にしたうえで空の値はnullだけを許可する。
  - KO: 채택할 누락값 표현을 JSON schema 자체에서 정하고, 필드를 필수로 한 뒤 빈 값은 null만 허용합니다.
  - EN: Define the accepted representation of missing values in the JSON schema itself, making the field required and allowing only null as an empty value.

## CCAR-F-Udemy01-0043

**JA** あなたは、AIアシスタントを使って社内の文書処理を自動化しているエンジニアです。チームは、新入社員のオンボーディング資料からメタデータを抽出し、人事システム用のJSONカタログを生成するカスタムコマンドを運用しています。

評価の結果、manager（上長）やstart_date（入社日）などの必須フィールドがnullとして返される問題が、繰り返し起きていることが分かりました。この問題は、情報が表・メール署名・自由記述の説明文など、さまざまな形式で記載されている場合に起きています。

該当フィールドは元の文書に確かに存在します。しかし、コマンドのプロンプトには、スキーマの説明と「すべての必須フィールドを抽出すること」という指示しか含まれていません。

抽出の一貫性を最も直接的に改善する変更はどれですか。（2つ選択してください。）

**KO** 당신은 AI 어시스턴트로 사내 문서 처리를 자동화하는 엔지니어입니다. 팀은 신입사원 온보딩 자료에서 metadata를 추출해 인사 시스템용 JSON 카탈로그를 생성하는 custom command를 운영하고 있습니다.

평가 결과, manager(상사)나 start_date(입사일) 같은 필수 필드가 null로 반환되는 문제가 반복해서 발생하고 있었습니다. 이 문제는 정보가 표, 이메일 서명, 자유 서술 설명문 등 다양한 형식으로 적혀 있을 때 발생합니다.

해당 필드는 원본 문서에 분명히 있습니다. 그러나 명령의 prompt에는 schema 설명과 “모든 필수 필드를 추출할 것”이라는 지시만 들어 있습니다.

추출의 일관성을 가장 직접적으로 개선하는 변경은 무엇입니까? (2개 선택하십시오.)

- A. JA: コマンドのtemperatureを下げ、実行のたびに抽出の挙動がより決定的になるよう調整する。
  - KO: 명령의 temperature를 낮춰, 실행할 때마다 추출 동작이 더 결정적이 되도록 조정합니다.
  - EN: Lower the command's temperature so that extraction behavior becomes more deterministic on each run.
- B. JA: 必須フィールドが現れやすい箇所と、表や署名、本文それぞれからの値の読み取り方を指示に書き加える。
  - KO: 필수 필드가 나타나기 쉬운 위치와, 표·서명·본문 각각에서 값을 읽어 내는 방법을 지시에 추가합니다.
  - EN: Add to the instructions where required fields tend to appear, and how to read values from tables, signatures, and body text respectively.
- C. JA: 多様なソース形式とその抽出結果を示す、関連性の高い構造化された例を3〜5個追加する。
  - KO: 다양한 원본 형식과 그 추출 결과를 보여 주는, 관련성 높은 구조화된 예시를 3~5개 추가합니다.
  - EN: Add 3 to 5 relevant, structured examples showing diverse source formats and their extraction results.
- D. JA: 該当するスキーマのフィールドをnullableに変更し、値が取れない場合でも検証エラーにしない。
  - KO: 해당 schema 필드를 nullable로 바꿔, 값을 얻지 못해도 검증 오류가 나지 않게 합니다.
  - EN: Change the relevant schema fields to nullable so that a missing value does not cause a validation error.

## CCAR-F-Udemy01-0044

**JA** あなたは、Claude Agent SDKを使用して、製薬分野の文献レビューを行うマルチエージェントシステムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を解析するもの、調査結果を統合するもの、レポートを生成するものがあります。

検索サブエージェントと文書解析サブエージェントは、臨床試験データベース検索用・社内文書アクセス用・引用エクスポート用の、それぞれ別々のMCPサーバーに接続することになっています。

ある設計案は、ランタイムがサブエージェントごとに1つのサーバーだけを有効にしておき、サブエージェントが別のサーバーのツールを必要としたときに、その都度再接続する方式です。

この設計案の代わりに推奨すべきものはどれですか。（2つ選択してください。）

**KO** 당신은 Claude Agent SDK로 제약 분야의 문헌 리뷰를 수행하는 multi-agent 시스템을 구축하고 있습니다. coordinator agent가 전문화된 subagent에게 작업을 위임합니다. subagent에는 웹을 검색하는 것, 문서를 분석하는 것, 조사 결과를 통합하는 것, 보고서를 생성하는 것이 있습니다.

검색 subagent와 문서 분석 subagent는 임상시험 데이터베이스 검색용, 사내 문서 접근용, 인용 내보내기용으로 각각 별도의 MCP server에 연결하게 되어 있습니다.

한 설계안은 런타임이 subagent마다 server를 하나만 활성화해 두고, subagent가 다른 server의 도구가 필요해지면 그때마다 다시 연결하는 방식입니다.

이 설계안 대신 권장해야 할 것은 무엇입니까? (2개 선택하십시오.)

- A. JA: サブエージェントに必要な各MCPサーバーへ接続してツール一覧を取得し、統一されたレジストリとして公開して呼び出しを所有サーバーへルーティングする。
  - KO: subagent에 필요한 각 MCP server에 연결해 도구 목록을 가져오고, 하나로 통합된 레지스트리로 공개한 뒤 호출을 해당 도구를 소유한 server로 routing합니다.
  - EN: Connect to each MCP server a subagent needs and retrieve the tool lists, expose them as a unified registry, and route calls to the server that owns each tool.
- B. JA: 各サブエージェントには自身の役割に実際に必要なMCPサーバーだけを割り当て、それらすべてを実行中ずっと接続したままにする。
  - KO: 각 subagent에는 자기 역할에 실제로 필요한 MCP server만 할당하고, 그 server들을 실행 내내 모두 연결된 상태로 유지합니다.
  - EN: Assign each subagent only the MCP servers its role actually requires, and keep all of them connected for the entire run.
- C. JA: 次の調査フェーズに必要なMCPサーバーだけを接続し、フェーズの間で再接続し、各ステップの前にサブエージェントのツールを再構築する。
  - KO: 다음 조사 단계에 필요한 MCP server만 연결하고, 단계 사이에 다시 연결하며, 각 단계 전에 subagent의 도구를 다시 구성합니다.
  - EN: Connect only the MCP servers needed for the next research phase, reconnect between phases, and rebuild the subagents' tools before each step.
- D. JA: 外部サービスを1つの自作MCPサーバーの背後にまとめ、個別のサーバーを廃止して、サブエージェントには集約された1つの調査ツールだけを公開する。
  - KO: 외부 서비스를 직접 만든 MCP server 하나 뒤로 모으고, 개별 server를 없앤 뒤, subagent에는 통합된 조사 도구 하나만 공개합니다.
  - EN: Consolidate the external services behind a single custom MCP server, retire the individual servers, and expose only one aggregated research tool to the subagents.

## CCAR-F-Udemy01-0045

**JA** ある製薬会社の研究開発チームは、Claude Agent SDKで夜間に無人で動く文献調査エージェントを運用しています。毎晩数十件の調査依頼をそれぞれ別のquery()で実行し、翌朝に研究者が結果を確認します。

ほとんどの依頼は20ターン前後で終わります。しかし、「この領域の最新動向を網羅的に調べる」のような範囲の広い依頼では、ツール呼び出しが数百回続き、1件で一晩分の予算の大半を使ってしまうことがあります。

チームは、次の2つを実現したいと考えています。

1件あたりの実行量に確実な上限を設ける

途中で止まった依頼を完了した調査と取り違えず、後から続きを処理できるようにする

行うべき変更はどれですか。（2つ選択してください。）

**KO** 한 제약회사의 연구개발팀은 Claude Agent SDK로 밤사이 무인으로 동작하는 문헌 조사 agent를 운영하고 있습니다. 매일 밤 수십 건의 조사 요청을 각각 별도의 query()로 실행하고, 다음 날 아침 연구자가 결과를 확인합니다.

대부분의 요청은 20 turn 안팎에서 끝납니다. 그러나 “이 분야의 최신 동향을 빠짐없이 조사하라” 같은 범위가 넓은 요청에서는 도구 호출이 수백 번 이어져, 한 건이 하룻밤 예산의 대부분을 써 버리기도 합니다.

팀은 다음 두 가지를 실현하려고 합니다.

건당 실행량에 확실한 상한을 두는 것

도중에 멈춘 요청을 완료된 조사로 착각하지 않고, 나중에 이어서 처리할 수 있게 하는 것

어떤 변경을 해야 합니까? (2개 선택하십시오.)

- A. JA: 累計の費用が限度を超えた時点で実行を打ち切るStopフックを、各query()のオプションに登録する。
  - KO: 누적 비용이 한도를 넘는 시점에 실행을 중단하는 Stop hook을 각 query()의 옵션에 등록합니다.
  - EN: Register a Stop hook in the options of each query() that terminates the run when the cumulative cost exceeds a limit.
- B. JA: 結果のsubtypeがerror_max_turns等ならsession_idを保存し、後でresumeする。
  - KO: 결과의 subtype이 error_max_turns 등이면 session_id를 저장해 두었다가 나중에 resume합니다.
  - EN: If the result's subtype is error_max_turns or similar, save the session_id and resume it later.
- C. JA: ClaudeAgentOptionsのeffortを"low"にし、各ターンの推論に使うトークン量を減らす。
  - KO: ClaudeAgentOptions의 effort를 "low"로 설정해, 각 turn의 추론에 쓰는 토큰 양을 줄입니다.
  - EN: Set effort in ClaudeAgentOptions to "low" to reduce the number of tokens used for reasoning in each turn.
- D. JA: max_turnsとmax_budget_usdを設定し、1件ごとのターン数と費用に限度を設ける。
  - KO: max_turns와 max_budget_usd를 설정해, 건당 turn 수와 비용에 한도를 둡니다.
  - EN: Set max_turns and max_budget_usd to place limits on the number of turns and the cost per request.

## CCAR-F-Udemy01-0046

**JA** あるコンサルティング会社は、Claude Agent SDKを使用して、環境影響評価のためのマルチエージェント調査システムを構築しています。コーディネーターエージェントは、専門化されたサブエージェント（Web検索担当、資料分析担当、知見の統合担当、レポート生成担当）に作業を委任します。このシステムは案件を調査し、出典を明記した包括的なレポートを作成します。

レポート生成ステップは、統合サブエージェントから常に同じ構造化された知見データを受け取っていますが、生成される文章表現には毎回ばらつきがあります。ある回では1つの知見につき出典付きの箇条書きを1件にしていますが、別の回では次のようになります。

複数の知見を1つにまとめてしまう

根拠となる抜粋を省く

出典の日付を脚注に追いやる

現在の指示は、「各知見を、出典の詳細を完全な形で含む簡潔な出典付き箇条書きに変換してください」というものです。

この変換の一貫性を最も直接的に改善する変更はどれですか。（2つ選択してください。）

**KO** 한 컨설팅 회사는 Claude Agent SDK로 환경영향평가를 위한 multi-agent 조사 시스템을 구축하고 있습니다. coordinator agent는 전문화된 subagent(웹 검색 담당, 자료 분석 담당, 발견 사항 통합 담당, 보고서 생성 담당)에게 작업을 위임합니다. 이 시스템은 안건을 조사해 출처를 명시한 종합 보고서를 작성합니다.

보고서 생성 단계는 통합 subagent로부터 항상 같은 구조화된 발견 사항 데이터를 받지만, 생성되는 문장 표현은 매번 달라집니다. 어떤 실행에서는 발견 사항 하나당 출처가 달린 글머리표 항목을 하나씩 만들지만, 다른 실행에서는 다음과 같이 됩니다.

여러 발견 사항을 하나로 합쳐 버립니다

근거가 되는 발췌문을 빠뜨립니다

출처의 날짜를 각주로 밀어냅니다

현재 지시는 “각 발견 사항을, 출처의 세부 정보를 완전한 형태로 포함한 간결한 출처 포함 글머리표 항목으로 변환하십시오”입니다.

이 변환의 일관성을 가장 직접적으로 개선하는 변경은 무엇입니까? (2개 선택하십시오.)

- A. JA: 代表的な知見の入力例と、理想的な出典付き箇条書きの出力例を示す例示ブロックを追加する。
  - KO: 대표적인 발견 사항 입력 예시와, 이상적인 출처 포함 글머리표 출력 예시를 보여 주는 예시 블록을 추가합니다.
  - EN: Add an examples block showing a representative finding as input and an ideal cited bullet point as output.
- B. JA: 出典付き箇条書きの明示的な出力テンプレートを追加し、必須要素とその記載順序を定義する。
  - KO: 출처 포함 글머리표의 명시적인 출력 템플릿을 추가하고, 필수 요소와 그 기재 순서를 정의합니다.
  - EN: Add an explicit output template for the cited bullet point that defines the required elements and the order in which they appear.
- C. JA: 出典付き箇条書きが発行日を省いている場合にレポート作成を止めるPreToolUseフックを追加する。
  - KO: 출처 포함 글머리표에 발행일이 빠져 있으면 보고서 작성을 멈추는 PreToolUse hook을 추가합니다.
  - EN: Add a PreToolUse hook that halts report creation when a cited bullet point omits the publication date.
- D. JA: 「簡潔に」「完全な形で」といった指示の語を、太字や大文字を使った強い表現に書き換える。
  - KO: “간결하게”, “완전한 형태로” 같은 지시 문구를 굵은 글씨나 대문자를 쓴 강한 표현으로 바꿔 씁니다.
  - EN: Rewrite instruction words such as "concise" and "complete" into stronger phrasing using bold text or capital letters.

## CCAR-F-Udemy01-0047

**JA** ある通信キャリアの請求紛争処理チームは、Claudeを使用して構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSONスキーマを使用して出力を検証します。エッジケースを適切に処理し、下流のシステムと連携する必要があります。

抽出処理の途中で、明細書の内容が顧客アカウントのデータと矛盾するため、一部のレコードはエスカレーションが必要になります。エスカレーションには、次の条件があります。

レビュー担当者は、モデルの会話全体やツール利用履歴を受け取らない

受付キューが受け取るエスカレーション用のパケットは、ツール呼び出しの引数ではなく、モデルの最終応答そのものでなければならない

顧客識別子・推定される根本原因・推奨される次のアクションを含む一貫したJSONが必要である

このチームが採用すべき設計はどれですか。（2つ選択してください。）

**KO** 한 통신사의 청구 분쟁 처리팀은 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증합니다. edge case를 적절히 처리하고 downstream 시스템과 연동해야 합니다.

추출 처리 도중, 명세서 내용이 고객 계정 데이터와 모순되어 일부 레코드는 escalation이 필요합니다. escalation에는 다음 조건이 있습니다.

검토 담당자는 모델의 대화 전체나 도구 사용 이력을 받지 않습니다

접수 큐가 받는 escalation용 패킷은 도구 호출의 인수가 아니라 모델의 최종 응답 그 자체여야 합니다

고객 식별자, 추정 근본 원인, 권장 다음 조치를 담은 일관된 JSON이 필요합니다

이 팀이 채택해야 할 설계는 무엇입니까? (2개 선택하십시오.)

- A. JA: Structured outputsでスキーマに適合したエスカレーション用パケットを最終応答として生成する。
  - KO: Structured outputs로 schema에 맞는 escalation용 패킷을 최종 응답으로 생성합니다.
  - EN: Use Structured outputs to produce a schema-conforming escalation packet as the final response.
- B. JA: スキーマを定義したエスカレーション用ツールを呼ばせ、その呼び出し引数をレビュー担当への引き渡しにする。
  - KO: schema를 정의한 escalation용 도구를 호출하게 하고, 그 호출 인수를 검토 담당자에게 넘기는 데이터로 삼습니다.
  - EN: Have the model call an escalation tool with a defined schema, and use the call arguments as the handoff to the reviewer.
- C. JA: 受付キューに入れる前に同じJSONスキーマでパケットを検証し、適合しないものは差し戻す。
  - KO: 접수 큐에 넣기 전에 같은 JSON schema로 패킷을 검증하고, 맞지 않는 것은 되돌려 보냅니다.
  - EN: Validate the packet against the same JSON schema before it enters the intake queue, and send back any that do not conform.
- D. JA: 抽出した生の抜粋と会話履歴をそのまま引き渡し、レビュー担当者に内容を再構成してもらう。
  - KO: 추출한 원본 발췌문과 대화 이력을 그대로 넘기고, 검토 담당자가 내용을 재구성하게 합니다.
  - EN: Hand over the raw extracted excerpts and the conversation history as they are, and have the reviewer reconstruct the contents.

## CCAR-F-Udemy01-0048

**JA** ある物流会社は、Claude Agent SDKを使用して社内向けの調査アシスタントを構築しています。コーディネーターエージェントが、経路検索・書類分析・統合・レポート生成をそれぞれ担当する専門サブエージェントに作業を委任します。

評価の結果、次の2つの問題が繰り返し起きていることが分かりました。

些細な根拠確認のたびに、レポート生成が停滞する

以前、統合サブエージェントの役割を広げたところ、経路検索サブエージェントと同じ作業まで行うようになった

この設計の改善として最も適切な変更はどれですか。

**KO** 한 물류 회사는 Claude Agent SDK로 사내용 조사 어시스턴트를 구축하고 있습니다. coordinator agent가 경로 검색, 서류 분석, 통합, 보고서 생성을 각각 맡는 전문 subagent에게 작업을 위임합니다.

평가 결과, 다음 두 가지 문제가 반복해서 발생하고 있었습니다.

사소한 근거 확인을 할 때마다 보고서 생성이 정체됩니다

이전에 통합 subagent의 역할을 넓혔더니, 경로 검색 subagent와 같은 작업까지 하게 되었습니다

이 설계를 개선하는 변경으로 가장 적절한 것은 무엇입니까?

- A. JA: 統合サブエージェントにも、経路検索サブエージェントと同じRead・Grep・Globの権限を与える。
  - KO: 통합 subagent에도 경로 검색 subagent와 같은 Read·Grep·Glob 권한을 줍니다.
  - EN: Give the synthesis subagent the same Read, Grep, and Glob permissions as the route search subagent.
- B. JA: 統合とレポート生成を1つのサブエージェントにまとめ、プロンプトとツール権限を共有させる。
  - KO: 통합과 보고서 생성을 하나의 subagent로 합쳐, prompt와 도구 권한을 공유하게 합니다.
  - EN: Combine synthesis and report generation into a single subagent that shares a prompt and tool permissions.
- C. JA: 統合サブエージェントのツールを外し、根拠を確認するたびにコーディネーターの承認を得てから次の作業へ進ませる。
  - KO: 통합 subagent의 도구를 제거하고, 근거를 확인할 때마다 coordinator의 승인을 받은 뒤 다음 작업으로 넘어가게 합니다.
  - EN: Remove the synthesis subagent's tools and make it obtain the coordinator's approval each time it verifies evidence before moving on to the next task.
- D. JA: 統合サブエージェントに範囲の狭いverify_factツールだけを与え、広い調査はコーディネーターに戻させる。
  - KO: 통합 subagent에는 범위가 좁은 verify_fact 도구만 주고, 넓은 조사는 coordinator에게 돌려보내게 합니다.
  - EN: Give the synthesis subagent only a narrowly scoped verify_fact tool, and have it return broader investigations to the coordinator.

## CCAR-F-Udemy01-0049

**JA** あるチームは、Claudeを使用して、医療記録から情報を抽出する構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSON（JavaScript Object Notation）スキーマを使用して出力を検証し、高い精度を維持する必要があります。エッジケースを適切に処理し、下流のシステムと連携する必要もあります。

ある検証ロールアウトで、後続のコードがいまだに古い抽出フィールド名insured_partyを期待しているため、処理が失敗し始めました。状況は次のとおりです。

どのファイルがそのフィールドを参照しているかは分からない

ファイル名自体には、その文字列は含まれていない

このセッションでは、組み込みのGlobとGrepが有効になっている

最初に行うべきClaude Codeのツール操作として、最も適切なものはどれですか。

**KO** 한 팀은 Claude로 의료 기록에서 정보를 추출하는 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON(JavaScript Object Notation) schema로 출력을 검증하며, 높은 정확도를 유지해야 합니다. edge case를 적절히 처리하고 downstream 시스템과 연동해야 하기도 합니다.

한 검증 롤아웃에서, 후속 코드가 아직도 예전 추출 필드 이름 insured_party를 기대하고 있어 처리가 실패하기 시작했습니다. 상황은 다음과 같습니다.

어느 파일이 그 필드를 참조하는지 모릅니다

파일 이름 자체에는 그 문자열이 들어 있지 않습니다

이 session에서는 내장 Glob과 Grep이 활성화되어 있습니다

가장 먼저 해야 할 Claude Code 도구 조작으로 가장 적절한 것은 무엇입니까?

- A. JA: Bashでgit logを実行し、insured_partyに触れたコミットメッセージを探す。
  - KO: Bash로 git log를 실행해, insured_party를 다룬 commit 메시지를 찾습니다.
  - EN: Run git log with Bash and look for commit messages that touched insured_party.
- B. JA: Grepで、insured_partyという文字列をリポジトリのファイル内容から検索する。
  - KO: Grep으로 insured_party라는 문자열을 저장소의 파일 내용에서 검색합니다.
  - EN: Use Grep to search the contents of the repository's files for the string insured_party.
- C. JA: Globを使って、ファイル名にinsured_partyという文字列を含むリポジトリのパスを探す。
  - KO: Glob으로 파일 이름에 insured_party라는 문자열이 들어간 저장소 경로를 찾습니다.
  - EN: Use Glob to find repository paths whose file names contain the string insured_party.
- D. JA: Readでプロジェクトルートを読み込み、ディレクトリ一覧から候補を目視で調べる。
  - KO: Read로 프로젝트 루트를 읽고, 디렉터리 목록에서 후보를 눈으로 살펴봅니다.
  - EN: Use Read to read the project root and visually examine candidates from the directory listing.

## CCAR-F-Udemy01-0050

**JA** 壊れたテストフィクスチャを自動修正するQAオートメーションエージェントを構築しています。このエージェントは、組み込みツール（Read、Write、Bash、Grep、Glob）を使用し、Model Context Protocol（MCP）サーバーとも連携します。

ある自動修正処理の中で、指定したold_stringが同じソースファイル内に複数回出現するため、Edit呼び出しが失敗しました。状況は次のとおりです。

意図している変更は、ファイルの最終的な内容に対する一回限りの修正であり、一致するすべての箇所を置き換えることではない

周辺の文脈を加えてold_stringを一意にしようとしたが、それでも一意にできなかった

望ましいファイル全体の内容は、組み立てられる状態にある

確実に修正するために、次に行うべきことはどれですか。

**KO** 깨진 테스트 fixture를 자동으로 고치는 QA 자동화 agent를 구축하고 있습니다. 이 agent는 내장 도구(Read, Write, Bash, Grep, Glob)를 사용하며, Model Context Protocol(MCP) server와도 연동합니다.

한 자동 수정 처리에서, 지정한 old_string이 같은 소스 파일 안에 여러 번 나타나 Edit 호출이 실패했습니다. 상황은 다음과 같습니다.

의도한 변경은 파일의 최종 내용에 대한 일회성 수정이며, 일치하는 모든 위치를 바꾸는 것이 아닙니다

주변 문맥을 덧붙여 old_string을 고유하게 만들려 했지만, 그래도 고유하게 만들 수 없었습니다

원하는 파일 전체 내용은 조립할 수 있는 상태입니다

확실하게 수정하려면 다음에 무엇을 해야 합니까?

- A. JA: 目的の出現箇所にゆるく一致する、正規表現風のold_stringでEditをリトライする。
  - KO: 목표 위치에 느슨하게 일치하는 정규식 형태의 old_string으로 Edit을 재시도합니다.
  - EN: Retry Edit with a regex-style old_string that loosely matches the target occurrence.
- B. JA: replace_all: trueを付けてEditをリトライし、一致する箇所をまとめて同じ内容に更新する。
  - KO: replace_all: true를 붙여 Edit을 재시도하고, 일치하는 위치를 한꺼번에 같은 내용으로 갱신합니다.
  - EN: Retry Edit with replace_all: true and update all matching locations to the same content at once.
- C. JA: Grepで対象の行番号を特定してから、同じ一意でないold_stringのままEditを呼び出す。
  - KO: Grep으로 대상 줄 번호를 확인한 뒤, 고유하지 않은 old_string을 그대로 둔 채 Edit을 호출합니다.
  - EN: Identify the target line number with Grep, and then call Edit with the same non-unique old_string.
- D. JA: 現在のファイルをReadで読み込み、望ましい全体の内容を組み立ててからWriteで上書きする。
  - KO: 현재 파일을 Read로 읽고, 원하는 전체 내용을 조립한 뒤 Write로 덮어씁니다.
  - EN: Read the current file with Read, assemble the desired full contents, and overwrite the file with Write.

## CCAR-F-Udemy01-0051

**JA** あるエンジニアは、社内システムのリファクタリング・デバッグ・ドキュメント作成にClaude Codeを活用しています。カスタムスラッシュコマンドやCLAUDE.mdの設定を整え、プランモードと直接実行をどう使い分けるかも把握しています。

昨日、リファクタリング計画について長時間の会話をした際、そのセッションIDを環境変数session_idに控えておきました。今日は、ターミナルから最初のフォローアップのプロンプトを送ると同時に、その特定の過去の会話を再開したいと考えています。

取るべき行動はどれですか。

**KO** 한 엔지니어는 사내 시스템의 refactoring, 디버깅, 문서 작성에 Claude Code를 활용하고 있습니다. custom slash command와 CLAUDE.md 설정을 갖춰 두었고, plan mode와 직접 실행을 어떻게 나눠 쓸지도 알고 있습니다.

어제 refactoring 계획에 관해 긴 대화를 나누면서, 그 session ID를 환경 변수 session_id에 적어 두었습니다. 오늘은 터미널에서 첫 후속 prompt를 보내면서 동시에 그 특정한 과거 대화를 재개하려고 합니다.

어떤 행동을 해야 합니까?

- A. JA: claude -p "昨日の調査を続けて" --continueを実行する。
  - KO: claude -p "어제 조사를 계속해 줘" --continue를 실행합니다.
  - EN: Run claude -p "昨日の調査を続けて" --continue.
- B. JA: claudeを起動し、session_idの値を貼り付けてから、昨日の調査を続けるよう頼む。
  - KO: claude를 실행하고 session_id 값을 붙여 넣은 뒤, 어제 조사를 계속하라고 요청합니다.
  - EN: Start claude, paste the value of session_id, and then ask it to continue yesterday's investigation.
- C. JA: claude -p "昨日の調査を続けて" --resume "$session_id"を実行する。
  - KO: claude -p "어제 조사를 계속해 줘" --resume "$session_id"를 실행합니다.
  - EN: Run claude -p "昨日の調査を続けて" --resume "$session_id".
- D. JA: claude -p "$session_id の調査を続けて"を実行する。
  - KO: claude -p "$session_id의 조사를 계속해 줘"를 실행합니다.
  - EN: Run claude -p "$session_id の調査を続けて".

> notes: 명령 안의 prompt 문자열(昨日の調査を続けて)은 자연어라 한국어로 옮김. 원문 일본어를 그대로 두려면 되돌릴 것.

## CCAR-F-Udemy01-0052

**JA** ある物流企業の開発生産性チームは、コードベースに関する作業を支援するため、Messages APIでツール使用の仕組みを実装しています。

テスト中、開発者が次のような質問をすると、コードベースの参照が不要な場合でも、Claudeがリポジトリgrepツールや、MCPリポジトリ検索ツールを呼び出してしまいます。

「このヘルパーのもっとシンプルな名前を考えて」

「エッジケースについてのあなたの推論を検索して」

現在の設定は次のとおりです。

これらのツールの説明には、リポジトリの内容やMCPが提供するプロジェクトデータを調べるためのものだと、すでに明記されている

リクエストは、デフォルトのtool_choiceの挙動を使っている

システムプロンプトには、「ユーザーがfind、search、locate、look upと言ったときは、回答する前に必ず検索ツールを使うこと」という一文が含まれている

最初に行うべき変更はどれですか。

**KO** 한 물류 기업의 개발 생산성팀은 코드베이스 관련 작업을 돕기 위해 Messages API로 tool use 구조를 구현하고 있습니다.

테스트 중 개발자가 다음과 같은 질문을 하면, 코드베이스를 참조할 필요가 없는데도 Claude가 저장소 grep 도구나 MCP 저장소 검색 도구를 호출합니다.

“이 헬퍼의 더 간단한 이름을 생각해 줘”

“edge case에 대한 당신의 추론을 검색해 줘”

현재 설정은 다음과 같습니다.

이 도구들의 설명에는 저장소 내용이나 MCP가 제공하는 프로젝트 데이터를 조사하기 위한 것이라고 이미 명시되어 있습니다

요청은 기본 tool_choice 동작을 사용합니다

system prompt에는 “사용자가 find, search, locate, look up이라고 말하면 답하기 전에 반드시 검색 도구를 사용할 것”이라는 문장이 들어 있습니다

가장 먼저 해야 할 변경은 무엇입니까?

- A. JA: 広いキーワードのルールを、リポジトリやMCPのデータを調べる必要がある場合だけ検索する指示に置き換える。
  - KO: 넓은 키워드 규칙을, 저장소나 MCP 데이터를 조사해야 할 때만 검색하라는 지시로 바꿉니다.
  - EN: Replace the broad keyword rule with an instruction to search only when repository or MCP data needs to be examined.
- B. JA: tool_choiceを{"type":"any"}に設定し、毎回のユーザーターンで最適なツールを選ばせる。
  - KO: tool_choice를 {"type":"any"}로 설정해, 매 사용자 turn마다 가장 적합한 도구를 고르게 합니다.
  - EN: Set tool_choice to {"type":"any"} and have the model choose the best tool on every user turn.
- C. JA: リポジトリgrepツールとMCPツールの説明に、それぞれのツールを呼び出すべきでないリクエストの例をさらに追加する。
  - KO: 저장소 grep 도구와 MCP 도구의 설명에, 각 도구를 호출하면 안 되는 요청의 예를 더 추가합니다.
  - EN: Add more examples of requests for which each tool should not be called to the descriptions of the repository grep tool and the MCP tool.
- D. JA: 検索系のツール名を、findやsearchといった利用者がよく使う単語に似ない名前へ変更する。
  - KO: 검색 계열 도구의 이름을, find나 search처럼 사용자가 자주 쓰는 단어와 비슷하지 않은 이름으로 바꿉니다.
  - EN: Rename the search tools to names that do not resemble words users commonly use, such as find and search.

## CCAR-F-Udemy01-0053

**JA** Claudeを使用して、構造化データ抽出システムを構築しています。このシステムは、購買発注書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携する必要があります。

検証ログを見ると、JSONは構文的に正しいものの、レビューキューには数量・金額の不整合フラグが大量に溜まっています。

フラグの多くは、無害な表記の違いによるものである

一方で、実際の計算ミスの一部は見逃されている

現在の指示は、「疑わしい合計を見つけてレビューにフラグを立ててください」となっています。

一貫性を最も直接的に改善するプロンプトの変更はどれですか。

**KO** Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 구매 발주서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동해야 합니다.

검증 로그를 보면 JSON은 구문상 올바르지만, 검토 큐에는 수량·금액 불일치 플래그가 대량으로 쌓여 있습니다.

플래그의 대부분은 무해한 표기 차이 때문입니다

한편 실제 계산 실수 중 일부는 놓치고 있습니다

현재 지시는 “의심스러운 합계를 찾아 검토용 플래그를 다십시오”입니다.

일관성을 가장 직접적으로 개선하는 prompt 변경은 무엇입니까?

- A. JA: 保守的に判断して、確信度の高い合計の異常だけをレビューに回すよう、指示を強める。
  - KO: 보수적으로 판단해 확신도가 높은 합계 이상만 검토로 넘기도록 지시를 강화합니다.
  - EN: Strengthen the instruction so that it judges conservatively and sends only high-confidence total anomalies to review.
- B. JA: 最終的なJSONを出力する前に、疑わしい合計の異常をすべて説明するようClaudeに求める。
  - KO: 최종 JSON을 출력하기 전에, 의심스러운 합계 이상을 모두 설명하도록 Claude에 요구합니다.
  - EN: Ask Claude to explain every suspicious total anomaly before outputting the final JSON.
- C. JA: あいまいなフラグ付け指示を、解析した明細項目が記載された合計と矛盾する場合の測定可能なルールに置き換える。
  - KO: 모호한 플래그 지시를, 파싱한 명세 항목이 기재된 합계와 모순되는 경우에 대한 측정 가능한 규칙으로 바꿉니다.
  - EN: Replace the ambiguous flagging instruction with a measurable rule for when the parsed line items contradict the stated total.
- D. JA: 温度（temperature）を上げて、Claudeが各発注書のレイアウトについてより多くの解釈を検討できるようにする。
  - KO: temperature를 높여, Claude가 각 발주서의 레이아웃에 대해 더 많은 해석을 검토할 수 있게 합니다.
  - EN: Raise the temperature so that Claude can consider more interpretations of each purchase order's layout.

## CCAR-F-Udemy01-0054

**JA** ある可観測性エンジニアリングチームは、本番ログの分析中に、Claude Messages APIを使って異常マップを生成しています。この異常マップは、社内ダッシュボードで使われます。

現在のプロンプトには「このスキーマに一致するJSONのみを返してください」と書かれています。しかしログを見ると、次のような理由でパーサーが失敗することが時折あります。

余計なコメントが末尾に付く

フィールドが欠落する

配列が期待される箇所に文字列値が入る

ダッシュボード側の連携は、自由形式のアシスタントのテキストではなく、ツール呼び出しを受け取るように設計されています。

スキーマに準拠した出力を最も確実に強制する変更はどれですか。

**KO** 한 observability 엔지니어링팀은 프로덕션 로그를 분석하면서 Claude Messages API로 이상 징후 맵을 생성하고 있습니다. 이 이상 징후 맵은 사내 대시보드에서 쓰입니다.

현재 prompt에는 “이 schema에 맞는 JSON만 반환하십시오”라고 적혀 있습니다. 그러나 로그를 보면 다음과 같은 이유로 파서가 가끔 실패합니다.

불필요한 코멘트가 끝에 붙습니다

필드가 빠집니다

배열이 와야 할 자리에 문자열 값이 들어갑니다

대시보드 쪽 연동은 자유 형식의 어시스턴트 텍스트가 아니라 도구 호출을 받도록 설계되어 있습니다.

schema를 준수하는 출력을 가장 확실하게 강제하는 변경은 무엇입니까?

- A. JA: input_schemaを持つクライアントツールをstrict: trueで定義し、応答をtool_useとして受け取る。
  - KO: input_schema를 가진 클라이언트 도구를 strict: true로 정의하고, 응답을 tool_use로 받습니다.
  - EN: Define a client tool with an input_schema and strict: true, and receive the response as tool_use.
- B. JA: 応答の後でパース済みのJSONを検証し、不正なダッシュボード用ペイロードを拒否するカスタムMCPサーバーを作成する。
  - KO: 응답 후 파싱된 JSON을 검증해 잘못된 대시보드용 페이로드를 거부하는 custom MCP server를 만듭니다.
  - EN: Write a custom MCP server that validates the parsed JSON after the response and rejects invalid dashboard payloads.
- C. JA: アシスタントの応答を開き波括弧でプリフィルし、停止シーケンスを追加して、返されたテキストをJSONとして解析する。
  - KO: 어시스턴트 응답을 여는 중괄호로 prefill하고 stop sequence를 추가한 뒤, 반환된 텍스트를 JSON으로 파싱합니다.
  - EN: Prefill the assistant response with an opening curly brace, add a stop sequence, and parse the returned text as JSON.
- D. JA: プロンプトにJSONスキーマを残したまま、有効なJSONしか受け付けないという強い言い回しを足し、パースに失敗したらリトライする。
  - KO: prompt에 JSON schema를 그대로 둔 채, 유효한 JSON만 받는다는 강한 표현을 추가하고, 파싱에 실패하면 재시도합니다.
  - EN: Leave the JSON schema in the prompt, add stronger wording saying that only valid JSON is accepted, and retry if parsing fails.

## CCAR-F-Udemy01-0055

**JA** あなたは、Claudeを使用して、企業合併のデューデリジェンス文書レビューを行う構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携する必要があります。

テストでは、30ファイルからなる文書パケットをレビューする際に、すべての元ファイルとすべての抽出済みJSONオブジェクトを、1つのレビュー用プロンプトにまとめて送っています。この方法では、次の問題が起きています。

ファイル固有の抽出エラーを見落とすことが多い

パケット全体の合計値について、矛盾した結論を返すことがある

また、レビューの中間成果物を、ログに残して評価できるようにする必要があります。

取るべき対応として、最も適切なものはどれですか。

**KO** 당신은 Claude로 기업 인수합병 실사(due diligence) 문서 검토를 수행하는 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동해야 합니다.

테스트에서는 30개 파일로 이루어진 문서 패킷을 검토할 때, 모든 원본 파일과 추출된 모든 JSON 객체를 하나의 검토용 prompt에 한꺼번에 보내고 있습니다. 이 방식에서는 다음 문제가 발생하고 있습니다.

파일 고유의 추출 오류를 놓치는 경우가 많습니다

패킷 전체의 합계값에 대해 서로 모순된 결론을 내놓기도 합니다

또한 검토의 중간 산출물을 로그로 남겨 평가할 수 있어야 합니다.

취해야 할 대응으로 가장 적절한 것은 무엇입니까?

- A. JA: 明示的なプロンプトチェイニングでファイル単位のレビューを行い、その所見を別の統合呼び出しでまとめる。
  - KO: 명시적인 prompt chaining으로 파일 단위 검토를 수행하고, 그 소견을 별도의 통합 호출로 정리합니다.
  - EN: Perform per-file reviews using explicit prompt chaining, and consolidate those findings in a separate synthesis call.
- B. JA: すべてのファイル・スキーマ・これまでのメモ・より厳格なチェック指示を含めた、さらに大きな1回のレビュー呼び出しを使う。
  - KO: 모든 파일, schema, 지금까지의 메모, 더 엄격한 점검 지시를 담은 더 큰 검토 호출 한 번을 사용합니다.
  - EN: Use a single, even larger review call that includes all files, the schema, the notes so far, and stricter check instructions.
- C. JA: Claude自身に最終的な問題リストを返す前に自らの所見を批評させる、1回のレビュー呼び出しを使う。
  - KO: 최종 문제 목록을 반환하기 전에 Claude가 스스로 자기 소견을 비평하게 하는 검토 호출 한 번을 사용합니다.
  - EN: Use a single review call that has Claude critique its own findings before returning the final list of issues.
- D. JA: 低いtemperatureでパケット全体を対象としたレビュー呼び出しを繰り返し行い、複数回の実行で共通して現れた所見だけを採用する。
  - KO: 낮은 temperature로 패킷 전체를 대상으로 한 검토 호출을 반복하고, 여러 번의 실행에서 공통으로 나타난 소견만 채택합니다.
  - EN: Repeatedly run review calls over the entire packet at a low temperature, and adopt only the findings that appear consistently across multiple runs.

## CCAR-F-Udemy01-0056

**JA** Claudeを使用して、構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携する必要があります。

チームは、classify_document、extract_claim_fields、validate_extraction、queue_human_reviewという名前のクライアントツールを追加しました。文書によって性質が大きく異なり、次のようなものがあります。

複数回の検証パスが必要な記録

レビューに回すべき記録

ツール呼び出しが一切不要な依頼

文書ごとにClaudeが次の行動を変えられるようにしつつ、ツールの実行はアプリケーション側が受け持つ設計として、最も適したものはどれですか。（2つ選択してください。）

**KO** Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동해야 합니다.

팀은 classify_document, extract_claim_fields, validate_extraction, queue_human_review라는 이름의 클라이언트 도구를 추가했습니다. 문서마다 성격이 크게 다르며, 다음과 같은 것이 있습니다.

여러 번의 검증 패스가 필요한 기록

검토로 넘겨야 할 기록

도구 호출이 전혀 필요 없는 요청

문서마다 Claude가 다음 행동을 바꿀 수 있게 하면서, 도구 실행은 애플리케이션이 맡는 설계로 가장 적합한 것은 무엇입니까? (2개 선택하십시오.)

- A. JA: tool_choiceをデフォルトのauto（自動）の挙動のままにし、ツール呼び出しが不要な依頼にはツールを呼ばずに応答できる状態を保つ。
  - KO: tool_choice를 기본값인 auto(자동) 동작으로 두어, 도구 호출이 필요 없는 요청에는 도구를 호출하지 않고 응답할 수 있는 상태를 유지합니다.
  - EN: Leave tool_choice at the default auto behavior, so that requests that need no tool calls can be answered without calling any tools.
- B. JA: classify_document、extract_claim_fields、validate_extraction、queue_human_reviewを常にこの順番で呼び出す固定のコントローラーを構築する。
  - KO: classify_document, extract_claim_fields, validate_extraction, queue_human_review를 항상 이 순서로 호출하는 고정 컨트롤러를 구축합니다.
  - EN: Build a fixed controller that always calls classify_document, extract_claim_fields, validate_extraction, and queue_human_review in that order.
- C. JA: 明確な説明とスキーマでツールを定義し、各tool_useリクエストを実行して対応するtool_resultブロックを返すループを実行する。
  - KO: 명확한 설명과 schema로 도구를 정의하고, 각 tool_use 요청을 실행해 대응하는 tool_result 블록을 반환하는 loop를 실행합니다.
  - EN: Define the tools with clear descriptions and schemas, and run a loop that executes each tool_use request and returns the corresponding tool_result block.
- D. JA: Claudeの自然言語による応答を解析し、「検証が必要」のようなフレーズを探して、対応する抽出ツールを呼び出す。
  - KO: Claude의 자연어 응답을 파싱해 “검증이 필요” 같은 문구를 찾고, 해당하는 추출 도구를 호출합니다.
  - EN: Parse Claude's natural-language responses, look for phrases such as "validation is needed", and call the corresponding extraction tool.

## CCAR-F-Udemy01-0057

**JA** Claudeを使用して、構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携する必要があります。

スキーマを更新した後、次の3つの抽出失敗が同時に発生しました。

キャリアの別名解決

配送日の正規化

運賃の合計照合

どの失敗も同じパーサーモジュールと共有のテストフィクスチャに関わっており、1つを単独で修正すると別の1つを壊してしまう状態が続いています。

このチームが次に使うべきClaude Codeのワークフローはどれですか。（2つ選択してください。）

**KO** Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동해야 합니다.

schema를 갱신한 뒤, 다음 세 가지 추출 실패가 동시에 발생했습니다.

운송사(carrier) 별칭 해석

배송일 정규화

운임 합계 대조

모든 실패가 같은 파서 모듈과 공유 테스트 fixture에 얽혀 있어, 하나를 단독으로 고치면 다른 하나가 깨지는 상태가 이어지고 있습니다.

이 팀이 다음에 사용해야 할 Claude Code workflow는 무엇입니까? (2개 선택하십시오.)

- A. JA: 変更範囲をパーサーモジュールと共有フィクスチャに限定し、無関係な下流の整理は今回含めない。
  - KO: 변경 범위를 파서 모듈과 공유 fixture로 한정하고, 관련 없는 downstream 정리는 이번에 포함하지 않습니다.
  - EN: Limit the scope of changes to the parser module and the shared fixtures, and do not include unrelated downstream cleanup this time.
- B. JA: 現在の会話をそのまま続け、検証を実行するたびに残っている失敗をその都度修正していく。
  - KO: 현재 대화를 그대로 이어 가며, 검증을 실행할 때마다 남아 있는 실패를 그때그때 고쳐 나갑니다.
  - EN: Continue the current conversation as is, and fix any remaining failures one by one each time the validation is run.
- C. JA: 失敗しているすべてのフィクスチャ、共有のスキーマ制約、検証コマンドを揃えてプランモードを開始する。
  - KO: 실패하는 모든 fixture, 공유 schema 제약, 검증 명령을 갖춰 plan mode를 시작합니다.
  - EN: Start plan mode with all of the failing fixtures, the shared schema constraints, and the validation command gathered together.
- D. JA: 失敗しているフィクスチャごとに直接編集を個別に実行し、検証コマンドの合間にコンテキストをクリアする。
  - KO: 실패하는 fixture마다 직접 편집을 따로 실행하고, 검증 명령 실행 사이사이에 context를 비웁니다.
  - EN: Run direct edits separately for each failing fixture, and clear the context between validation command runs.

## CCAR-F-Udemy01-0058

**JA** あるSaaS企業の開発ツールチームは、Claude Code上に構築したPRレビューヘルパーを運用しています。このヘルパーはプッシュのたびに実行され、GitHub上にインラインコメントを投稿します。

しかし、後続の実行では、以前の実行ですでに指摘した内容を繰り返し報告してしまうことがよくあります。このチームは、まだ解消されていない問題は隠さずに、繰り返し実行されるレビューを役に立つものにしたいと考えています。

このチームが行うべき変更はどれですか。（2つ選択してください。）

**KO** 한 SaaS 기업의 개발 도구팀은 Claude Code 위에 구축한 PR 리뷰 헬퍼를 운영하고 있습니다. 이 헬퍼는 push할 때마다 실행되어 GitHub에 인라인 코멘트를 게시합니다.

그러나 이후 실행에서는 이전 실행에서 이미 지적한 내용을 다시 보고하는 일이 잦습니다. 이 팀은 아직 해결되지 않은 문제는 숨기지 않으면서, 반복 실행되는 리뷰를 쓸모 있게 만들고 싶어 합니다.

이 팀이 해야 할 변경은 무엇입니까? (2개 선택하십시오.)

- A. JA: ファイルパスと行番号の一致だけを基準に重複を排除してから、後続のコメントを投稿する。
  - KO: 파일 경로와 줄 번호의 일치만을 기준으로 중복을 제거한 뒤 후속 코멘트를 게시합니다.
  - EN: Deduplicate based only on matching file paths and line numbers before posting subsequent comments.
- B. JA: 以前のPRの指摘事項を永続化し、各再実行に渡して、新規または未解消の問題だけを報告するよう指示する。
  - KO: 이전 PR의 지적 사항을 저장해 두었다가 매 재실행에 전달하고, 새로운 문제나 해결되지 않은 문제만 보고하도록 지시합니다.
  - EN: Persist the findings from earlier PR runs, pass them to each rerun, and instruct it to report only new or unresolved issues.
- C. JA: 後続のレビューを手動リクエストに切り替え、繰り返しコメントを生成する価値があるかを開発者に判断させる。
  - KO: 후속 리뷰를 수동 요청 방식으로 바꾸고, 반복 코멘트를 생성할 가치가 있는지 개발자가 판단하게 합니다.
  - EN: Switch subsequent reviews to manual requests, and let developers decide whether generating repeated comments is worthwhile.
- D. JA: 以前に指摘した箇所のコードを毎回あらためて確認し、問題が依然として残っている場合にだけ再度報告する。
  - KO: 이전에 지적한 위치의 코드를 매번 다시 확인하고, 문제가 여전히 남아 있을 때만 다시 보고합니다.
  - EN: Re-examine the code at the previously flagged locations each time, and report again only if the problem still remains.

## CCAR-F-Udemy01-0059

**JA** ある保険会社の請求処理自動化チームは、Claudeを使用して構造化データ抽出システムを構築しています。このシステムは、非構造化文書である請求書類から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持する必要があります。

抽出コーディネーターには、表解析・条項抽出・スキーマ修復を担当する専門サブエージェントが用意されていますが、SDKの設定ではファイル閲覧系のツールしか自動承認されていません。そのため、コーディネーターは個別のサブタスクを委任せず、抽出作業をすべて自分自身で行い続けています。

このチームが行うべき変更はどれですか。（2つ選択してください。）

**KO** 한 보험회사의 청구 처리 자동화팀은 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서인 청구 서류에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지해야 합니다.

추출 coordinator에는 표 분석, 조항 추출, schema 복구를 맡는 전문 subagent가 마련되어 있지만, SDK 설정에서는 파일 열람 계열 도구만 자동 승인됩니다. 그래서 coordinator는 개별 하위 작업을 위임하지 않고, 추출 작업을 모두 스스로 계속 처리하고 있습니다.

이 팀이 해야 할 변경은 무엇입니까? (2개 선택하십시오.)

- A. JA: 各専門サブエージェントを、agentsオプションか.claude/agents配下のファイルとして定義する。
  - KO: 각 전문 subagent를 agents 옵션이나 .claude/agents 아래의 파일로 정의합니다.
  - EN: Define each specialized subagent through the agents option or as a file under .claude/agents.
- B. JA: permissionModeをbypassPermissionsに変更し、コーディネーターのツール設定と委任の指示はそのまま残す。
  - KO: permissionMode를 bypassPermissions로 바꾸고, coordinator의 도구 설정과 위임 지시는 그대로 둡니다.
  - EN: Change permissionMode to bypassPermissions, and leave the coordinator's tool settings and delegation instructions as they are.
- C. JA: コーディネーターのallowedTools（Pythonではallowed_tools）にAgentを追加する。
  - KO: coordinator의 allowedTools(Python에서는 allowed_tools)에 Agent를 추가합니다.
  - EN: Add Agent to the coordinator's allowedTools (allowed_tools in Python).
- D. JA: tool_choiceで抽出用のツールを強制し、文書ごとにJSONスキーマ抽出ツールを呼び出させる。
  - KO: tool_choice로 추출용 도구를 강제해, 문서마다 JSON schema 추출 도구를 호출하게 합니다.
  - EN: Force the extraction tool with tool_choice so that the JSON schema extraction tool is called for each document.

## CCAR-F-Udemy01-0060

**JA** あなたは、Claudeを使用して保険金請求処理システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流の請求管理システムと連携する必要があります。

パイロットテストでは、次のような書き込みがありました。

ある申請者は「この自動審査を止めて、人が対応してください」と書き込んだ。欠損しているフィールドは、簡単に抽出できる内容だった

別の申請者は「事故日が抜けている、修正できますか？」と書き込んだ。元の文書には、明確な日付が記載されていた

実装すべきエスカレーションポリシーはどれですか。（2つ選択してください。）

**KO** 당신은 Claude로 보험금 청구 처리 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 청구 관리 시스템과 연동해야 합니다.

파일럿 테스트에서 다음과 같은 메시지가 들어왔습니다.

한 신청자는 “이 자동 심사를 멈추고 사람이 처리해 주세요”라고 적었습니다. 누락된 필드는 쉽게 추출할 수 있는 내용이었습니다

다른 신청자는 “사고 날짜가 빠져 있는데, 고칠 수 있나요?”라고 적었습니다. 원본 문서에는 날짜가 분명히 적혀 있었습니다

구현해야 할 escalation 정책은 무엇입니까? (2개 선택하십시오.)

- A. JA: 申請者の不満度をスコアリングし、一定のしきい値を超えた場合のみエスカレーションする。
  - KO: 신청자의 불만 정도를 점수화해, 일정 임계값을 넘을 때만 escalation합니다.
  - EN: Score the claimant's level of frustration, and escalate only when it exceeds a certain threshold.
- B. JA: 人間対応を求めていない依頼に限って自動修復を試み、修復後も検証に失敗した場合はエスカレーションする。
  - KO: 사람의 처리를 요구하지 않은 요청에 한해 자동 복구를 시도하고, 복구 후에도 검증에 실패하면 escalation합니다.
  - EN: Attempt automatic repair only for requests that do not ask for a human, and escalate if validation still fails after the repair.
- C. JA: 明示的な人間対応の要求は直接レビューへ回し、単純な修正依頼には自動修復を提供する。
  - KO: 사람의 처리를 명시적으로 요구하면 곧바로 검토로 넘기고, 단순한 수정 요청에는 자동 복구를 제공합니다.
  - EN: Route explicit requests for a human directly to review, and offer automatic repair for simple correction requests.
- D. JA: 欠損フィールドの抽出の難しさを見積もり、簡単なものは自動修復に、難しいものはレビューに回す。
  - KO: 누락 필드를 추출하기가 얼마나 어려운지 추정해, 쉬운 것은 자동 복구로, 어려운 것은 검토로 넘깁니다.
  - EN: Estimate how difficult it is to extract each missing field, and route easy ones to automatic repair and difficult ones to review.

## CCAR-F-Udemy02-0001

**JA** あるクラウドインフラ企業のプラットフォームチームは、Claude Codeを使ってソフトウェア開発を加速しています。コード生成、リファクタリング、デバッグ、ドキュメント作成に活用し、カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合しています。プランモードと直接実行をどのように使い分けるかも理解する必要があります。

このチームが独自に作成した/upgrade-planコマンドは、リポジトリのアップグレードガイドを解析して、下流の自動化処理向けのJSONに変換します。

評価では有効なJSONが得られていますが、元の情報が次のような形で書かれている場合に、rollback_commandやcompatibility_noteといった必須フィールドがnullとして返されてしまいます。

フェンス付きのシェルブロック

Markdownのチェックリスト

散文の段落

情報自体は元資料の中にあります。また、現在のプロンプトはすでにスキーマを列挙し、必須フィールドを省略しないよう指示しています。

この抽出の失敗に最も直接的に対処できる変更はどれですか。（2つ選択してください。）

**KO** 한 클라우드 인프라 기업의 플랫폼팀은 Claude Code로 소프트웨어 개발 속도를 높이고 있습니다. 코드 생성, refactoring, 디버깅, 문서 작성에 활용하며, custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하고 있습니다. plan mode와 직접 실행을 어떻게 나눠 쓸지도 이해해야 합니다.

이 팀이 직접 만든 /upgrade-plan 명령은 저장소의 업그레이드 가이드를 분석해 downstream 자동화 처리용 JSON으로 변환합니다.

평가에서는 유효한 JSON이 나오지만, 원본 정보가 다음과 같은 형태로 적혀 있으면 rollback_command나 compatibility_note 같은 필수 필드가 null로 반환됩니다.

펜스로 감싼 셸 블록

Markdown 체크리스트

산문 단락

정보 자체는 원본 자료 안에 있습니다. 또한 현재 prompt는 이미 schema를 나열하고, 필수 필드를 생략하지 말라고 지시하고 있습니다.

이 추출 실패에 가장 직접적으로 대처할 수 있는 변경은 무엇입니까? (2개 선택하십시오.)

- A. JA: スキーマの説明をCLAUDE.mdに移し、このコマンドの実行時に毎回読み込まれる状態にする。
  - KO: schema 설명을 CLAUDE.md로 옮겨, 이 명령을 실행할 때마다 읽히도록 합니다.
  - EN: Move the schema description into CLAUDE.md so that it is loaded every time this command runs.
- B. JA: temperatureを引き上げ、さまざまなアップグレードガイドの形式をより広く解釈させる。
  - KO: temperature를 높여, 다양한 업그레이드 가이드 형식을 더 폭넓게 해석하게 합니다.
  - EN: Raise the temperature so that it interprets a wider range of upgrade guide formats.
- C. JA: 多様なガイド形式を期待されるJSONフィールドに対応づけた構造化例を3〜5個追加する。
  - KO: 다양한 가이드 형식을 기대되는 JSON 필드에 대응시킨 구조화된 예시를 3~5개 추가합니다.
  - EN: Add 3 to 5 structured examples that map diverse guide formats to the expected JSON fields.
- D. JA: 必須フィールドごとに、元資料のどこにどの形（シェルブロックやチェックリスト等）で現れるかを書く。
  - KO: 필수 필드마다, 원본 자료의 어디에 어떤 형태(셸 블록이나 체크리스트 등)로 나타나는지 적습니다.
  - EN: For each required field, describe where in the source material and in what form (shell block, checklist, etc.) it appears.

## CCAR-F-Udemy02-0002

**JA** ある法律事務所では、Claude Agent SDKを使用して、判例調査を行うマルチエージェントシステムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、判例データベースを検索するもの、判例文書を分析するもの、論点を統合するもの、法律メモを生成するものがあります。このシステムはトピックを調査し、引用付きの包括的なメモを作成します。

文書分析サブエージェントは、クライアント側のツールを使って、ライセンス契約済みの判例データベースから文書を読み取り、根拠となる記述を抽出します。文書が利用できない場合、ツールはis_error: trueのtool_resultを返します。ただしその内容は、次のような原因にかかわらず、常に「操作に失敗しました」という固定の文言です。

ライセンス切れ

一時的なタイムアウト

非対応のファイル形式

該当箇所が無い有効な検索結果

その結果、コーディネーターは、リトライ、そのソースの破棄、エスカレーションのいずれかを予測できない形で選んでしまいます。

復旧動作を最も改善できる変更はどれですか。（2つ選択してください。）

**KO** 한 법률 사무소에서는 Claude Agent SDK로 판례 조사를 수행하는 multi-agent 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent에는 판례 데이터베이스를 검색하는 것, 판례 문서를 분석하는 것, 쟁점을 통합하는 것, 법률 메모를 생성하는 것이 있습니다. 이 시스템은 주제를 조사해 인용이 달린 종합 메모를 작성합니다.

문서 분석 subagent는 클라이언트 측 도구로, 라이선스 계약을 맺은 판례 데이터베이스에서 문서를 읽어 근거가 되는 서술을 추출합니다. 문서를 쓸 수 없으면 도구는 is_error: true인 tool_result를 반환합니다. 그런데 그 내용은 다음과 같은 원인과 상관없이 항상 “작업에 실패했습니다”라는 고정 문구입니다.

라이선스 만료

일시적인 timeout

지원하지 않는 파일 형식

해당 부분이 없는 유효한 검색 결과

그 결과 coordinator는 재시도, 해당 출처 폐기, escalation 중 하나를 예측할 수 없는 방식으로 고르고 있습니다.

복구 동작을 가장 크게 개선할 수 있는 변경은 무엇입니까? (2개 선택하십시오.)

- A. JA: 失敗した文書の読み取りを空の結果セットとして返し、統合処理をそのまま続行させる。
  - KO: 실패한 문서 읽기를 빈 결과 집합으로 반환하고, 통합 처리를 그대로 계속하게 합니다.
  - EN: Return a failed document read as an empty result set and let the synthesis process continue as is.
- B. JA: リトライ可能と示されたエラーだけをリトライし、他はソースの切り替えかエスカレーションに回させる。
  - KO: 재시도 가능하다고 표시된 오류만 재시도하고, 나머지는 출처 전환이나 escalation으로 넘기게 합니다.
  - EN: Make it retry only errors indicated as retryable, and route the others to switching sources or escalation.
- C. JA: 原因の分類とリトライの可否を含むtool_resultエラーを返す。
  - KO: 원인 분류와 재시도 가능 여부를 담은 tool_result 오류를 반환합니다.
  - EN: Return a tool_result error that includes the classification of the cause and whether a retry is possible.
- D. JA: 文書ツールの説明文を拡張し、失敗する可能性のあるツールの使用をClaudeに避けさせる方向へ誘導する。
  - KO: 문서 도구의 설명을 늘려, 실패할 가능성이 있는 도구는 Claude가 쓰지 않도록 유도합니다.
  - EN: Expand the document tool's description to steer Claude toward avoiding the use of tools that might fail.

## CCAR-F-Udemy02-0003

**JA** あるゲームスタジオのライブ運用チームは、Claude CodeをCI/CDパイプラインに統合しています。このシステムは、自動コードレビューを実行し、テストケースを生成し、プルリクエストにフィードバックを返します。具体的で実行可能なフィードバックを返し、誤検知を最小限に抑えるプロンプトを設計する必要があります。

運用開始から3か月が経ち、このシステムは、構造化されたレビューの指摘や生成したテスト提案の大半に、高い確信度スコアを付けるようになりました。

人手によるレビュー体制は縮小される予定です。それでもチームは、次のことを続ける必要があります。

本番環境でのエラー率を測定する

マイグレーション、セキュリティに関わる変更、言語固有の規約といった領域で、まれな失敗モードを捕捉する

この目的に最も適した監視アプローチはどれですか。（2つ選択してください。）

**KO** 한 게임 스튜디오의 라이브 운영팀은 Claude Code를 CI/CD pipeline에 통합했습니다. 이 시스템은 자동 코드 리뷰를 실행하고, 테스트 케이스를 생성하며, pull request에 피드백을 남깁니다. 구체적이고 실행 가능한 피드백을 주면서 오탐(false positive)을 최소화하는 prompt를 설계해야 합니다.

운영을 시작한 지 3개월이 지나자, 이 시스템은 구조화된 리뷰 지적 사항과 생성한 테스트 제안 대부분에 높은 확신도 점수를 매기게 되었습니다.

사람이 하는 리뷰 체계는 축소될 예정입니다. 그래도 팀은 다음을 계속해야 합니다.

프로덕션 환경의 오류율 측정

마이그레이션, 보안 관련 변경, 언어별 규칙 같은 영역에서 드문 실패 유형 포착

이 목적에 가장 적합한 모니터링 방식은 무엇입니까? (2개 선택하십시오.)

- A. JA: 確信度のカットオフ値を引き上げた後も、高確信度の出力について一定数以上のサンプルをレビューし続ける。
  - KO: 확신도 기준값을 높인 뒤에도, 높은 확신도 출력에 대해 일정 수 이상의 샘플을 계속 검토합니다.
  - EN: Even after raising the confidence cutoff, continue to review at least a certain number of samples of high-confidence outputs.
- B. JA: 変更の種類や言語、指摘のカテゴリで層別化して高確信度の指摘をサンプリングし、誤りと新種を分けてラベル付けする。
  - KO: 변경 유형, 언어, 지적 카테고리별로 층화해 높은 확신도 지적을 샘플링하고, 오류와 새로운 유형을 구분해 라벨을 붙입니다.
  - EN: Sample high-confidence findings stratified by change type, language, and finding category, and label errors and novel failure types separately.
- C. JA: すべてのリポジトリにわたって高確信度の指摘を一様にサンプリングし、パイプライン全体について1つの集計エラー率を公表する。
  - KO: 모든 저장소에 걸쳐 높은 확신도 지적을 균일하게 샘플링하고, pipeline 전체에 대해 하나의 집계 오류율을 공개합니다.
  - EN: Sample high-confidence findings uniformly across all repositories, and publish a single aggregate error rate for the entire pipeline.
- D. JA: 低確信度の指摘を優先してレビューし、高確信度帯は月次の全体精度だけを確認する。
  - KO: 낮은 확신도 지적을 우선해 검토하고, 높은 확신도 구간은 월별 전체 정확도만 확인합니다.
  - EN: Prioritize reviewing low-confidence findings, and for the high-confidence band, check only the overall monthly accuracy.

## CCAR-F-Udemy02-0004

**JA** あなたは、ソフトウェア開発を加速するためにClaude Codeを使用しています。チームでは、コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行をどのように使い分けるかを理解する必要があります。

ある電子カルテプラットフォームのチームが、50を超えるファイルで使われている共有認証ライブラリを移行しようとしています。実現可能な移行アプローチは2つあり、それぞれインフラ要件が異なります。保守担当者は、実装を始める前に、Claude Codeにコードベースを調査させ、アプローチを提案してほしいと考えています。

最初に取るべきワークフローとして最も適切なものはどれですか。

**KO** 당신은 소프트웨어 개발 속도를 높이기 위해 Claude Code를 사용하고 있습니다. 팀에서는 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 씁니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하며, plan mode와 직접 실행을 어떻게 나눠 쓸지 이해해야 합니다.

한 전자의무기록 플랫폼팀이 50개가 넘는 파일에서 쓰이는 공유 인증 라이브러리를 마이그레이션하려고 합니다. 실현 가능한 마이그레이션 방식은 두 가지이며, 각각 인프라 요구 사항이 다릅니다. 유지보수 담당자는 구현을 시작하기 전에 Claude Code가 코드베이스를 조사해 방식을 제안해 주기를 원합니다.

가장 먼저 취해야 할 workflow로 가장 적절한 것은 무엇입니까?

- A. JA: プランモードに入り、Claudeに影響範囲を調査させ、実行モードを選ぶ前に提案されたプランをレビューする。
  - KO: plan mode에 들어가 Claude가 영향 범위를 조사하게 하고, 실행 모드를 고르기 전에 제안된 plan을 검토합니다.
  - EN: Enter plan mode, have Claude investigate the scope of impact, and review the proposed plan before choosing an execution mode.
- B. JA: bypassPermissionsで開始し、Claudeにコマンドを自由に実行させ、リグレッションの有無は事後にテストで確認する。
  - KO: bypassPermissions로 시작해 Claude가 명령을 자유롭게 실행하게 하고, 회귀 여부는 나중에 테스트로 확인합니다.
  - EN: Start with bypassPermissions, let Claude run commands freely, and check for regressions with tests afterward.
- C. JA: acceptEditsで開始し、Claudeに移行を適用させ、変更が完了した後で差分をレビューする。
  - KO: acceptEdits로 시작해 Claude가 마이그레이션을 적용하게 하고, 변경이 끝난 뒤 diff를 검토합니다.
  - EN: Start with acceptEdits, let Claude apply the migration, and review the diff after the changes are complete.
- D. JA: 直接実装を指示するプロンプトから始め、Claudeにアプローチを選ばせて、編集しながら設計を練り上げる。
  - KO: 바로 구현하라고 지시하는 prompt로 시작해 Claude가 방식을 고르게 하고, 편집하면서 설계를 다듬습니다.
  - EN: Start with a prompt that directs direct implementation, let Claude choose the approach, and refine the design while editing.

## CCAR-F-Udemy02-0005

**JA** ある物流会社の社内ヘルプデスクでは、配送遅延、返品対応、アカウント権限の問題などのあいまいな問い合わせを解決するエージェントを、Claude Agent SDKで構築しています。このエージェントは、カスタムのModel Context Protocol（MCP）ツール（get_employee、lookup_ticket、issue_replacement、escalate_to_manager）を通じて、社内システムにアクセスします。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を達成することです。

このチームでは、交換対応やエスカレーションのロジックへの変更を検査するため、夜間のプルリクエストチェックでClaude Codeを呼び出しています。しかしCI環境には、フォローアップの確認プロンプトに応答するターミナルの利用者がいません。そのため、ジョブはプロンプトを表示したまま、ランナーがタイムアウトするまで待ち続けてしまいます。

この障害を防ぐために最も適切な変更はどれですか。（2つ選択してください。）

**KO** 한 물류 회사의 사내 헬프데스크에서는 배송 지연, 반품 처리, 계정 권한 문제 같은 모호한 문의를 해결하는 agent를 Claude Agent SDK로 구축하고 있습니다. 이 agent는 custom Model Context Protocol(MCP) 도구(get_employee, lookup_ticket, issue_replacement, escalate_to_manager)를 통해 사내 시스템에 접근합니다. 목표는 escalation해야 할 시점을 판단하면서 1차 해결률 80% 이상을 달성하는 것입니다.

이 팀은 교환 처리와 escalation 로직의 변경을 검사하려고 야간 pull request 점검에서 Claude Code를 호출합니다. 그러나 CI 환경에는 후속 확인 prompt에 응답할 터미널 사용자가 없습니다. 그래서 job이 prompt를 띄운 채 러너가 timeout될 때까지 계속 기다립니다.

이 장애를 막기 위해 가장 적절한 변경은 무엇입니까? (2개 선택하십시오.)

- A. JA: .claude/commands/に共有のスラッシュコマンドを作成し、CIジョブからそのコマンドを呼び出す。
  - KO: .claude/commands/에 공유 slash command를 만들고, CI job에서 그 명령을 호출합니다.
  - EN: Create a shared slash command in .claude/commands/ and invoke that command from the CI job.
- B. JA: Claude Codeを-p（--print）フラグ付きで実行し、レビュー用プロンプトを非対話的に渡す。
  - KO: Claude Code를 -p(--print) 플래그와 함께 실행해, 리뷰용 prompt를 비대화식으로 전달합니다.
  - EN: Run Claude Code with the -p (--print) flag and pass the review prompt non-interactively.
- C. JA: レビューに必要なツールを、CIジョブの権限設定で事前承認する。
  - KO: 리뷰에 필요한 도구를 CI job의 권한 설정에서 미리 승인합니다.
  - EN: Pre-approve the tools needed for the review in the CI job's permission settings.
- D. JA: Claude Codeをプランモードで実行し、生成されたプランをジョブが自動承認するようにする。
  - KO: Claude Code를 plan mode로 실행하고, 생성된 plan을 job이 자동 승인하게 합니다.
  - EN: Run Claude Code in plan mode and have the job automatically approve the generated plan.

## CCAR-F-Udemy02-0006

**JA** サプライチェーン分析を手がけるスタートアップが、Claude Agent SDKを使用して、マルチエージェントの調査レポートシステムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、サプライヤーのデータを収集するもの、出荷リスクを分析するもの、調査結果を統合するもの、経営層向けレポートを作成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

ある評価実行で、コーディネーターの最初のMessages APIレスポンスには、短いテキストブロックと、Taskの2つのtool_useブロックが含まれていました。しかし実行履歴を確認すると、レポート生成の前にtool_resultメッセージが一度も送信されていませんでした。レポートは常に、コーディネーターの最初のテキストだけに基づいています。

コーディネーターのループに加えるべき変更はどれですか。（2つ選択してください。）

**KO** 공급망 분석을 다루는 한 스타트업이 Claude Agent SDK로 multi-agent 조사 보고서 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent에는 공급업체 데이터를 수집하는 것, 출하 리스크를 분석하는 것, 조사 결과를 통합하는 것, 경영진용 보고서를 작성하는 것이 있습니다. 이 시스템은 주제를 조사해 출처를 명시한 종합 보고서를 작성합니다.

한 평가 실행에서 coordinator의 첫 Messages API 응답에는 짧은 텍스트 블록과 Task의 tool_use 블록 2개가 들어 있었습니다. 그런데 실행 이력을 확인해 보니, 보고서를 생성하기 전에 tool_result 메시지가 한 번도 전송되지 않았습니다. 보고서는 항상 coordinator의 첫 텍스트만을 바탕으로 합니다.

coordinator의 loop에 어떤 변경을 해야 합니까? (2개 선택하십시오.)

- A. JA: 各サブエージェントの出力を、tool_useのidごとにuserターンのtool_resultブロックとして送る。
  - KO: 각 subagent의 출력을 tool_use의 id별로 user turn의 tool_result 블록으로 보냅니다.
  - EN: Send each subagent's output as a tool_result block in a user turn, keyed by the tool_use id.
- B. JA: コーディネーターのテキストブロックを統合処理へそのまま転送し、Taskの実行は省いて、テキストがあればその時点でターンを終える。
  - KO: coordinator의 텍스트 블록을 통합 처리로 그대로 넘기고, Task 실행은 생략하며, 텍스트가 있으면 그 시점에 turn을 끝냅니다.
  - EN: Forward the coordinator's text block as-is to the synthesis step, skip executing the Task calls, and end the turn at that point if there is text.
- C. JA: コーディネーターを3回の反復に制限し、部分的な調査結果を要約して、上限に達したら停止させる。
  - KO: coordinator를 3회 반복으로 제한하고, 부분적인 조사 결과를 요약해 상한에 도달하면 멈추게 합니다.
  - EN: Limit the coordinator to three iterations, summarize partial findings, and stop when the limit is reached.
- D. JA: 要求された各Taskを実行してtool_resultを返し、stop_reasonがend_turnになるまで呼び出しを続ける。
  - KO: 요청된 각 Task를 실행해 tool_result를 반환하고, stop_reason이 end_turn이 될 때까지 호출을 계속합니다.
  - EN: Execute each requested Task and return a tool_result, and keep calling until stop_reason is end_turn.

## CCAR-F-Udemy02-0007

**JA** ある通信キャリアは、Claude Agent SDKを使用して顧客対応エージェントを構築しています。このエージェントは、料金請求に関する問い合わせ、SIM交換、端末保証などのあいまいな問い合わせを処理します。カスタムのModel Context Protocol（MCP）ツール（get_subscriber、lookup_invoice、process_credit、escalate_to_tier2）を通じて、社内システムにアクセスします。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を達成することです。

本番環境のトレースを確認すると、すべての受信リクエストが、次の個別のサブエージェントに順に送られていることが分かりました。

本人確認

請求内容

クレジットポリシー

エスカレーション要約

単純な請求状況の確認だけで済む質問でもレイテンシが高くなっており、一部の回答には、無関係なクレジットポリシーの注意書きまで含まれています。

専門のワーカーを本当に必要なケースのために残しつつ、設計を最も改善できる変更はどれですか。（2つ選択してください。）

**KO** 한 통신사는 Claude Agent SDK로 고객 응대 agent를 구축하고 있습니다. 이 agent는 요금 청구 문의, SIM 교체, 단말 보증 같은 모호한 문의를 처리합니다. custom Model Context Protocol(MCP) 도구(get_subscriber, lookup_invoice, process_credit, escalate_to_tier2)를 통해 사내 시스템에 접근합니다. 목표는 escalation해야 할 시점을 판단하면서 1차 해결률 80% 이상을 달성하는 것입니다.

프로덕션 환경의 트레이스를 확인해 보니, 들어오는 모든 요청이 다음의 개별 subagent를 차례로 거치고 있었습니다.

본인 확인

청구 내역

크레딧 정책

escalation 요약

단순한 청구 상태 확인만으로 끝나는 질문인데도 지연 시간이 길고, 일부 답변에는 관계없는 크레딧 정책 안내 문구까지 들어 있습니다.

전문 worker는 정말 필요한 경우를 위해 남겨 두면서, 설계를 가장 크게 개선할 수 있는 변경은 무엇입니까? (2개 선택하십시오.)

- A. JA: すべてのサブエージェントに同じバックエンドツールを持たせ、不要な場合は各ワーカー自身にスキップするよう指示する。
  - KO: 모든 subagent에 같은 백엔드 도구를 주고, 필요 없을 때는 각 worker가 스스로 건너뛰도록 지시합니다.
  - EN: Give all subagents the same backend tools and instruct each worker to skip them on its own when they are not needed.
- B. JA: 単純な請求状況の確認は直接回答し、専門的な処理が必要なケースだけサブエージェントに委任する。
  - KO: 단순한 청구 상태 확인은 직접 답하고, 전문적인 처리가 필요한 경우에만 subagent에 위임합니다.
  - EN: Answer simple billing status checks directly, and delegate to subagents only for cases that need specialized handling.
- C. JA: 本人確認と請求のサブエージェントを1つに統合し、経由する段数を減らす。
  - KO: 본인 확인 subagent와 청구 subagent를 하나로 합쳐, 거치는 단계 수를 줄입니다.
  - EN: Merge the identity verification and billing subagents into one to reduce the number of hops.
- D. JA: ケースを検査し、必要なサブエージェントだけを呼び出して、それぞれに自己完結したタスク要約を渡すコーディネーターの工程を追加する。
  - KO: 사례를 검사해 필요한 subagent만 호출하고, 각각에 자기 완결적인 작업 요약을 넘기는 coordinator 단계를 추가합니다.
  - EN: Add a coordinator step that inspects the case, invokes only the subagents that are needed, and passes each a self-contained task summary.

## CCAR-F-Udemy02-0008

**JA** あるフィンテック企業のプラットフォームチームは、Claude Codeを使ってソフトウェア開発を加速しています。コード生成、リファクタリング、デバッグ、ドキュメント作成に活用し、カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合しています。プランモードと直接実行をどのように使い分けるかも理解する必要があります。

このチームは、エンジニアリング参考資料（設計ドキュメント、運用手順書、データベーススキーマ、アーキテクチャノート）を扱うため、独自のMCPサーバーとクライアント側の統合を追加しようとしています。開発者の要望は次のとおりです。

ホスト側に、これらの参考資料をブラウズできる一覧を表示させる

必要なときにだけ、選択したコンテンツをClaudeのコンテキストに添付する

何が存在するかを調べるためだけに、Claudeが探索的な関数呼び出しにターンを費やすことは避ける

MCPの制御モデルに最も合致する設計はどれですか。

**KO** 한 핀테크 기업의 플랫폼팀은 Claude Code로 소프트웨어 개발 속도를 높이고 있습니다. 코드 생성, refactoring, 디버깅, 문서 작성에 활용하며, custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하고 있습니다. plan mode와 직접 실행을 어떻게 나눠 쓸지도 이해해야 합니다.

이 팀은 엔지니어링 참고 자료(설계 문서, 운영 절차서, 데이터베이스 schema, 아키텍처 노트)를 다루기 위해 자체 MCP server와 클라이언트 측 통합을 추가하려고 합니다. 개발자의 요구는 다음과 같습니다.

host가 이 참고 자료를 둘러볼 수 있는 목록을 보여 줄 것

필요할 때만 선택한 콘텐츠를 Claude의 context에 첨부할 것

무엇이 있는지 알아보려는 목적만으로 Claude가 탐색용 함수 호출에 turn을 쓰는 일은 피할 것

MCP의 제어 모델에 가장 잘 맞는 설계는 무엇입니까?

- A. JA: list_reference_materialツールを追加して最初に呼ばせ、選んだ文書は追加のツール呼び出しで取得させる。
  - KO: list_reference_material 도구를 추가해 먼저 호출하게 하고, 고른 문서는 추가 도구 호출로 가져오게 합니다.
  - EN: Add a list_reference_material tool and have Claude call it first, then retrieve the chosen documents with additional tool calls.
- B. JA: 資料カタログをCLAUDE.mdにコピーしてリポジトリ更新のたびに更新し、Claudeに開発者へ文書名を尋ねさせる。
  - KO: 자료 카탈로그를 CLAUDE.md에 복사해 저장소가 갱신될 때마다 업데이트하고, Claude가 개발자에게 문서 이름을 묻게 합니다.
  - EN: Copy the material catalog into CLAUDE.md, update it every time the repository is updated, and have Claude ask the developer for document names.
- C. JA: resources機能を宣言し、resources/listで一覧を示してresources/readで読ませる。
  - KO: resources capability를 선언하고, resources/list로 목록을 보여 주며 resources/read로 읽게 합니다.
  - EN: Declare the resources capability, present the list via resources/list, and have the content read via resources/read.
- D. JA: 各参考資料をプロンプトとして公開し、開発者がスラッシュコマンドで実行して文書本文を注入する。
  - KO: 각 참고 자료를 prompt로 공개하고, 개발자가 slash command로 실행해 문서 본문을 주입합니다.
  - EN: Expose each reference material as a prompt, and have developers run it with a slash command to inject the document body.

## CCAR-F-Udemy02-0009

**JA** あなたは、レガシーシステムの保守を担当するチームで、Claude Codeを使って開発ワークフローを効率化しています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行をどのように使い分けるかを理解する必要があります。

チームは、見慣れないレガシーな請求計算モジュールに包括的なテストを追加するための、再利用可能なワークフローを必要としています。作業は通常、モジュールの読み込みから始まりますが、その後の手順は次の点によって変わります。

見つかった依存関係

既存のテストパターン

コードの継ぎ目（シーム）の有無

チームは、レイテンシの最小化よりも、有用なカバレッジを生み出すことを重視しています。

最も適したオーケストレーションの選択はどれですか。

**KO** 당신은 레거시 시스템 유지보수를 맡은 팀에서 Claude Code로 개발 workflow를 효율화하고 있습니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하며, plan mode와 직접 실행을 어떻게 나눠 쓸지 이해해야 합니다.

팀은 익숙하지 않은 레거시 청구 계산 모듈에 포괄적인 테스트를 추가하기 위한, 재사용 가능한 workflow가 필요합니다. 작업은 보통 모듈을 읽는 것에서 시작하지만, 그 뒤의 절차는 다음에 따라 달라집니다.

발견된 의존 관계

기존 테스트 패턴

코드 이음새(seam)의 유무

팀은 지연 시간을 최소화하는 것보다 쓸모 있는 커버리지를 만드는 것을 더 중시합니다.

가장 적합한 orchestration 선택은 무엇입니까?

- A. JA: 広範なスラッシュコマンドを1つ使い、ファイル一式と要件を制約のない1つのリクエストでClaudeに渡す。
  - KO: 폭넓은 slash command 하나를 써서, 파일 전체와 요구 사항을 제약 없는 요청 하나로 Claude에 넘깁니다.
  - EN: Use one broad slash command that gives Claude the full set of files and requirements in a single unconstrained request.
- B. JA: 動的な分解を使い、Claudeにモジュールを調査させ、発見内容からサブタスクを作ってテスト計画に統合させる。
  - KO: 동적 분해를 사용해, Claude가 모듈을 조사하고 발견한 내용으로 하위 작업을 만들어 테스트 계획으로 통합하게 합니다.
  - EN: Use dynamic decomposition: have Claude investigate the module, create subtasks from what it discovers, and consolidate them into a test plan.
- C. JA: 固定のプロンプトチェーンを使い、Claudeに毎回、ファイル分析・テスト作成・テスト実行・失敗の修正をこの順序で行わせる。
  - KO: 고정된 prompt chain을 사용해, Claude가 매번 파일 분석, 테스트 작성, 테스트 실행, 실패 수정을 이 순서로 수행하게 합니다.
  - EN: Use a fixed prompt chain that has Claude analyze the files, write tests, run tests, and fix failures, in that order, every time.
- D. JA: 直接実行を使い、Claudeにすぐテストを書き始めさせ、不足しているコンテキストには失敗が現れてから対処させる。
  - KO: 직접 실행을 사용해 Claude가 곧바로 테스트를 쓰기 시작하게 하고, 부족한 context는 실패가 나타난 뒤에 대처하게 합니다.
  - EN: Use direct execution: have Claude start writing tests immediately and deal with missing context only after failures appear.

## CCAR-F-Udemy02-0010

**JA** あなたは、Claude Agent SDKを使用して、通信キャリアのカスタマーサポート解決エージェントを構築しています。このエージェントは、返金、請求に関する異議申し立て、アカウントの問題など、あいまいさの高いリクエストを処理します。カスタムのModel Context Protocol（MCP）ツール（get_customer、lookup_order、process_refund、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を維持することです。

あるカスタマーサポート基盤では、Messages APIのクライアント側のツール使用ループを使っています。ベータテスト期間中のポリシーでは、500ドルを超える返金には人によるレビューが必須です。

感情の高ぶった請求トラブルのケースがいくつか発生しました。その中でエージェントは、lookup_orderの後に、しきい値を超える金額でprocess_refundのtool_useリクエストを発行し、アプリケーションはそのリクエストをそのまま実行してしまいました。

このワークフローの要件を最も効果的に強制できる変更はどれですか。（2つ選択してください。）

**KO** 당신은 Claude Agent SDK로 통신사의 고객 지원 해결 agent를 구축하고 있습니다. 이 agent는 환불, 청구 이의 제기, 계정 문제 등 모호성이 높은 요청을 처리합니다. custom Model Context Protocol(MCP) 도구(get_customer, lookup_order, process_refund, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation해야 할 시점을 판단하면서 1차 해결률 80% 이상을 유지하는 것입니다.

한 고객 지원 플랫폼에서는 Messages API의 클라이언트 측 tool use loop를 사용합니다. 베타 테스트 기간의 정책상, 500달러를 넘는 환불에는 사람의 검토가 반드시 필요합니다.

감정이 격해진 청구 분쟁 사례가 몇 건 발생했습니다. 그중에서 agent는 lookup_order 다음에 임계값을 넘는 금액으로 process_refund tool_use 요청을 보냈고, 애플리케이션은 그 요청을 그대로 실행해 버렸습니다.

이 workflow 요구 사항을 가장 효과적으로 강제할 수 있는 변경은 무엇입니까? (2개 선택하십시오.)

- A. JA: しきい値を超えるprocess_refundの呼び出しをアプリ側で止め、escalate_to_humanへ回す。
  - KO: 임계값을 넘는 process_refund 호출을 앱 쪽에서 막고, escalate_to_human으로 넘깁니다.
  - EN: Block process_refund calls above the threshold on the application side and route them to escalate_to_human.
- B. JA: 返金を伴う請求トラブルでは、tool_choiceでescalate_to_humanの呼び出しを毎回強制する。
  - KO: 환불이 따르는 청구 분쟁에서는 tool_choice로 escalate_to_human 호출을 매번 강제합니다.
  - EN: Use tool_choice to force a call to escalate_to_human every time for billing disputes involving refunds.
- C. JA: しきい値を超える返金はescalate_to_humanに送るよう、システムプロンプトに明記する。
  - KO: 임계값을 넘는 환불은 escalate_to_human으로 보내라고 system prompt에 명시합니다.
  - EN: State explicitly in the system prompt that refunds above the threshold must be sent to escalate_to_human.
- D. JA: process_refundの実装で要求金額を検証し、しきい値を超えるリクエストをそこで拒否する。
  - KO: process_refund 구현에서 요청 금액을 검증하고, 임계값을 넘는 요청은 그 자리에서 거부합니다.
  - EN: Validate the requested amount in the process_refund implementation and reject requests above the threshold there.

## CCAR-F-Udemy02-0011

**JA** ある投資リサーチデスクは、Claude Agent SDKを使用してマルチエージェントの株式調査システムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、財務ニュースと開示資料を検索するもの、証券アナリストのPDFレポートを分析するもの、知見を統合するもの、レポートを生成するものがあります。

このチームは、公開前に草稿レポートの所見を分類する、プロンプトベースの品質ゲートを追加しました。

そのうちの1つのカテゴリ「根拠のない市場動向の主張」が、出典が十分に示された統合した段落に対して誤検知を多く出すようになりました。一方、引用の欠落や出典間の矛盾といったほかのカテゴリは良好に機能しています。その結果、エンジニアは品質レポート全体を無視するようになってしまいました。

このチームが次に行うべきことはどれですか。

**KO** 한 투자 리서치 데스크는 Claude Agent SDK로 multi-agent 주식 조사 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent에는 금융 뉴스와 공시 자료를 검색하는 것, 증권 애널리스트의 PDF 리포트를 분석하는 것, 발견 사항을 통합하는 것, 보고서를 생성하는 것이 있습니다.

이 팀은 공개 전에 초안 보고서의 소견을 분류하는, prompt 기반 품질 게이트를 추가했습니다.

그중 한 카테고리인 “근거 없는 시장 동향 주장”이, 출처가 충분히 제시된 통합 단락에 대해 오탐을 많이 내기 시작했습니다. 반면 인용 누락이나 출처 간 모순 같은 다른 카테고리는 잘 작동하고 있습니다. 그 결과 엔지니어들이 품질 보고서 전체를 무시하게 되었습니다.

이 팀이 다음에 해야 할 일은 무엇입니까?

- A. JA: ノイズの多いカテゴリは有効なまま、誤検知がありうるという注意書きを添え、手動で無視するよう頼む。
  - KO: 노이즈가 많은 카테고리는 켜 둔 채, 오탐이 있을 수 있다는 주의 문구를 덧붙이고 수동으로 무시해 달라고 요청합니다.
  - EN: Leave the noisy category enabled, add a note that false positives are possible, and ask engineers to ignore them manually.
- B. JA: ノイズの多いカテゴリだけを一時的に外し、実例と定義、適合率・再現率の評価で作り直す。
  - KO: 노이즈가 많은 카테고리만 일시적으로 빼고, 실제 사례와 정의, 정밀도·재현율 평가로 다시 만듭니다.
  - EN: Temporarily remove only the noisy category, and rebuild it with real examples and definitions, evaluated with precision and recall.
- C. JA: 品質ゲートに厳格なJSONを返させて不正な出力を却下し、スキーマ準拠を主な信頼指標にする。
  - KO: 품질 게이트가 엄격한 JSON을 반환하게 해 잘못된 출력을 거부하고, schema 준수를 주요 신뢰 지표로 삼습니다.
  - EN: Have the quality gate return strict JSON and reject malformed output, and use schema conformance as the main trust metric.
- D. JA: 1リリースサイクルの間は品質ゲート全体を止め、プロンプトを直してから全カテゴリを再開する。
  - KO: 한 릴리스 주기 동안 품질 게이트 전체를 멈추고, prompt를 고친 뒤 모든 카테고리를 재개합니다.
  - EN: Pause the entire quality gate for one release cycle, fix the prompt, and then re-enable all categories.

## CCAR-F-Udemy02-0012

**JA** ある教育系SaaS企業は、Claude Codeをコードレビュー自動化パイプラインに統合しています。このシステムは、プルリクエストごとに自動レビューを実行し、テストケースを生成し、具体的で実行可能なフィードバックを返します。誤検知を最小限に抑えるプロンプトを設計する必要があります。

コーディネーターは、あるプルリクエストのレビューを、セキュリティ、テストカバレッジ、保守性をそれぞれ担当する専門サブエージェントに委任しています。各サブエージェントは有用な指摘をコーディネーターに返していますが、最終的なレビュー要約では、コーディネーターがすでに受け取っていたはずの次の情報がしばしば省略されています。

具体的なファイルパス

失敗したテストの名前

根拠となるコードスニペット

この信頼性の問題に最も効果的に対処できる変更はどれですか。（2つ選択してください。）

**KO** 한 교육 SaaS 기업은 Claude Code를 코드 리뷰 자동화 pipeline에 통합하고 있습니다. 이 시스템은 pull request마다 자동 리뷰를 실행하고, 테스트 케이스를 생성하며, 구체적이고 실행 가능한 피드백을 돌려줍니다. 오탐을 최소화하는 prompt를 설계해야 합니다.

coordinator는 한 pull request의 리뷰를 보안, 테스트 커버리지, 유지보수성을 각각 맡은 전문 subagent에게 위임하고 있습니다. 각 subagent는 유용한 지적 사항을 coordinator에게 돌려주지만, 최종 리뷰 요약에서는 coordinator가 이미 받았을 다음 정보가 자주 빠집니다.

구체적인 파일 경로

실패한 테스트의 이름

근거가 되는 코드 스니펫

이 신뢰성 문제에 가장 효과적으로 대처할 수 있는 변경은 무엇입니까? (2개 선택하십시오.)

- A. JA: セキュリティとテストカバレッジの指示をCLAUDE.mdに保存し、次回以降のCI実行で読み込ませる。
  - KO: 보안과 테스트 커버리지 지시를 CLAUDE.md에 저장해, 다음 CI 실행부터 읽히게 합니다.
  - EN: Save the security and test coverage instructions in CLAUDE.md so that subsequent CI runs load them.
- B. JA: 各専門サブエージェントの結果をコーディネーターが要約してから統合サブエージェントに渡し、入力を小さく保つ。
  - KO: 각 전문 subagent의 결과를 coordinator가 요약한 뒤 통합 subagent에 넘겨, 입력을 작게 유지합니다.
  - EN: Have the coordinator summarize each specialized subagent's results before passing them to the synthesis subagent, to keep the input small.
- C. JA: 各サブエージェントが返した構造化データを要約せず、そのまま統合サブエージェントのプロンプトに渡す。
  - KO: 각 subagent가 반환한 구조화된 데이터를 요약하지 않고 그대로 통합 subagent의 prompt에 넘깁니다.
  - EN: Pass the structured data returned by each subagent as-is, without summarizing, into the synthesis subagent's prompt.
- D. JA: 各専門サブエージェントに、指摘ごとの根拠（ファイルパスやテスト名、コード抜粋）を必須とする固定スキーマで返させる。
  - KO: 각 전문 subagent가 지적마다 근거(파일 경로, 테스트 이름, 코드 발췌)를 필수로 하는 고정 schema로 결과를 반환하게 합니다.
  - EN: Have each specialized subagent return results in a fixed schema that requires per-finding evidence (file paths, test names, and code excerpts).

## CCAR-F-Udemy02-0013

**JA** あるモバイルアプリ企業のプラットフォームチームは、Claude CodeをCI/CDパイプラインに統合しています。このシステムは、自動コードレビューを実行し、テストケースを生成し、プルリクエストにフィードバックを返します。具体的で実行可能なフィードバックを返し、誤検知を最小限に抑えるプロンプトを設計する必要があります。

このチームのCIレビュージョブには、プルリクエストのメタデータを扱う、プロジェクトスコープのHTTP MCPサーバーが必要です。このサーバーは、Authorizationヘッダーにベアラートークンを要求します。チームの要件は次の2つです。

MCPの設定は、すべてのチェックアウトで共有する

認証情報はコミットしない

この要件を最もよく満たす実装はどれですか。

**KO** 한 모바일 앱 기업의 플랫폼팀은 Claude Code를 CI/CD pipeline에 통합하고 있습니다. 이 시스템은 자동 코드 리뷰를 실행하고, 테스트 케이스를 생성하며, pull request에 피드백을 남깁니다. 구체적이고 실행 가능한 피드백을 주면서 오탐을 최소화하는 prompt를 설계해야 합니다.

이 팀의 CI 리뷰 job에는 pull request metadata를 다루는 project scope의 HTTP MCP server가 필요합니다. 이 server는 Authorization 헤더에 bearer token을 요구합니다. 팀의 요구 사항은 다음 두 가지입니다.

MCP 설정은 모든 체크아웃에서 공유할 것

인증 정보는 commit하지 않을 것

이 요구 사항을 가장 잘 충족하는 구현은 무엇입니까?

- A. JA: MCPサーバーをAuthorizationトークンごと~/.claude.jsonにだけ登録し、手動での設定手順を全員向けに文書化する。
  - KO: MCP server를 Authorization 토큰과 함께 ~/.claude.json에만 등록하고, 수동 설정 절차를 모두가 볼 수 있게 문서화합니다.
  - EN: Register the MCP server, including the Authorization token, only in ~/.claude.json, and document manual setup steps for everyone.
- B. JA: headersでBearer ${PR_API_TOKEN}を参照する.mcp.jsonをコミットし、値は各環境で設定する。
  - KO: headers에서 Bearer ${PR_API_TOKEN}을 참조하는 .mcp.json을 commit하고, 값은 각 환경에서 설정합니다.
  - EN: Commit a .mcp.json that references Bearer ${PR_API_TOKEN} in headers, and set the value in each environment.
- C. JA: headersでBearer $PR_API_TOKEN（波括弧なし）を参照する.mcp.jsonをコミットし、接続時の展開に任せる。
  - KO: headers에서 Bearer $PR_API_TOKEN(중괄호 없음)을 참조하는 .mcp.json을 commit하고, 연결 시점의 변수 확장에 맡깁니다.
  - EN: Commit a .mcp.json that references Bearer $PR_API_TOKEN (without braces) in headers, and rely on expansion at connection time.
- D. JA: ベアラートークンをheadersに直接書いた.mcp.jsonをコミットし、リポジトリへのアクセスを承認済みメンテナーに限る。
  - KO: bearer token을 headers에 직접 적은 .mcp.json을 commit하고, 저장소 접근은 승인된 maintainer로 제한합니다.
  - EN: Commit a .mcp.json with the bearer token written directly in headers, and limit repository access to approved maintainers.

## CCAR-F-Udemy02-0014

**JA** ある環境政策シンクタンクでは、Claude Agent SDKを使用して、政策リサーチシステムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、知見を統合するもの、報告書を生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的な報告書を作成します。

評価の過程で、最終報告書は出典を引用してはいるものの、同じ主張について次の根拠を同等に扱ってしまうことがあると分かりました。

査読付きの学術研究

ベンダーが公表したベンチマーク

内部アンケート調査

検索サブエージェントと文書分析サブエージェントは現在、簡潔な知見の要約と、参照した出典の一般的なリストだけを返しています。

後続の統合を正確にするために、最も適切な変更はどれですか。（2つ選択してください。）

**KO** 한 환경 정책 싱크탱크에서는 Claude Agent SDK로 정책 리서치 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent에는 웹을 검색하는 것, 문서를 분석하는 것, 발견 사항을 통합하는 것, 보고서를 생성하는 것이 있습니다. 이 시스템은 주제를 조사해 출처를 명시한 종합 보고서를 작성합니다.

평가 과정에서, 최종 보고서가 출처를 인용하기는 하지만 같은 주장에 대해 다음 근거들을 동등하게 다루는 경우가 있다는 사실이 드러났습니다.

동료 심사를 거친 학술 연구

벤더가 공개한 벤치마크

내부 설문 조사

검색 subagent와 문서 분석 subagent는 현재 간결한 발견 사항 요약과, 참조한 출처의 일반적인 목록만 반환하고 있습니다.

후속 통합을 정확하게 하기 위해 가장 적절한 변경은 무엇입니까? (2개 선택하십시오.)

- A. JA: 各サブエージェントに、出典の所在・発行日・根拠の抜粋を含む構造化された主張レコードを返させる。
  - KO: 각 subagent가 출처의 위치, 발행일, 근거 발췌를 담은 구조화된 주장 레코드를 반환하게 합니다.
  - EN: Have each subagent return structured claim records that include the source's location, publication date, and an excerpt of the evidence.
- B. JA: 統合の工程で、根拠を出典の種類に応じて重み付けする。
  - KO: 통합 단계에서 출처 유형에 따라 근거에 가중치를 둡니다.
  - EN: In the synthesis step, weight the evidence according to the type of source.
- C. JA: コーディネーターにサブエージェントの完全な会話記録を保持させ、統合エージェントにそこから出典の由来を推測させる。
  - KO: coordinator가 subagent의 전체 대화 기록을 보관하게 하고, 통합 agent가 거기서 출처의 유래를 추측하게 합니다.
  - EN: Have the coordinator keep the subagents' complete conversation transcripts, and have the synthesis agent infer source provenance from them.
- D. JA: 各サブエージェントに、要約を作成する前にすべての利用可能な出典を調査できるよう、より広いツールアクセス権を与える。
  - KO: 각 subagent가 요약을 작성하기 전에 사용 가능한 모든 출처를 조사할 수 있도록, 더 넓은 도구 접근 권한을 줍니다.
  - EN: Give each subagent broader tool access so that it can investigate all available sources before writing its summary.

## CCAR-F-Udemy02-0015

**JA** 太陽光発電設備のリース事業を営む会社が、Claude Agent SDKを使用して顧客対応エージェントを構築しています。このエージェントは、料金に関する紛争、設備の不具合、アカウントの問題などのあいまいな問い合わせを処理します。カスタムのModel Context Protocol（MCP）ツール（get_customer、lookup_order、process_refund、escalate_to_human）を通じて、社内システムにアクセスします。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を達成することです。

このチームは、サポートエンジニアがオンデマンドで実行できる、case-reviewという名前のClaude Codeワークフローを用意したいと考えています。要件は次のとおりです。

長文の調査メモを作成するため、メインの会話コンテキストの外側で実行する

Claudeが、権限確認プロンプトを繰り返し出さずに、プロジェクトファイルを読み取り・検索できる

開発者が呼び出すときに、想定されるケースIDを表示する

これらの要件に最も合致する設定はどれですか。

**KO** 태양광 발전 설비 리스 사업을 하는 한 회사가 Claude Agent SDK로 고객 응대 agent를 구축하고 있습니다. 이 agent는 요금 분쟁, 설비 고장, 계정 문제 같은 모호한 문의를 처리합니다. custom Model Context Protocol(MCP) 도구(get_customer, lookup_order, process_refund, escalate_to_human)를 통해 사내 시스템에 접근합니다. 목표는 escalation해야 할 시점을 판단하면서 1차 해결률 80% 이상을 달성하는 것입니다.

이 팀은 지원 엔지니어가 필요할 때 실행할 수 있는 case-review라는 Claude Code workflow를 마련하려고 합니다. 요구 사항은 다음과 같습니다.

긴 조사 메모를 작성하므로 메인 대화 context 바깥에서 실행할 것

Claude가 권한 확인 prompt를 반복해 띄우지 않고 프로젝트 파일을 읽고 검색할 수 있을 것

개발자가 호출할 때 예상되는 케이스 ID를 표시할 것

이 요구 사항에 가장 잘 맞는 설정은 무엇입니까?

- A. JA: .claude/skills/case-review/SKILL.mdをcontext: fork、allowed-toolsを排他的な許可リストとして、argument-hintをバリデータとして設定する。
  - KO: .claude/skills/case-review/SKILL.md를 context: fork로 하고, allowed-tools를 배타적인 허용 목록으로, argument-hint를 검증기로 설정합니다.
  - EN: Set up .claude/skills/case-review/SKILL.md with context: fork, allowed-tools as an exclusive allowlist, and argument-hint as a validator.
- B. JA: .claude/skills/case-review.mdをcontext: fork、allowed-toolsにReadとGrep、argument-hint: [case-id]で作成する。
  - KO: .claude/skills/case-review.md를 context: fork, allowed-tools에 Read와 Grep, argument-hint: [case-id]로 작성합니다.
  - EN: Create .claude/skills/case-review.md with context: fork, allowed-tools of Read and Grep, and argument-hint: [case-id].
- C. JA: .claude/skills/case-review/SKILL.mdをcontext: main、allowed-toolsにReadとGrep、argument-hint: [case-id]で作成する。
  - KO: .claude/skills/case-review/SKILL.md를 context: main, allowed-tools에 Read와 Grep, argument-hint: [case-id]로 작성합니다.
  - EN: Create .claude/skills/case-review/SKILL.md with context: main, allowed-tools of Read and Grep, and argument-hint: [case-id].
- D. JA: .claude/skills/case-review/SKILL.mdをcontext: fork、allowed-toolsにReadとGrep、argument-hint: [case-id]で作成する。
  - KO: .claude/skills/case-review/SKILL.md를 context: fork, allowed-tools에 Read와 Grep, argument-hint: [case-id]로 작성합니다.
  - EN: Create .claude/skills/case-review/SKILL.md with context: fork, allowed-tools of Read and Grep, and argument-hint: [case-id].

## CCAR-F-Udemy02-0016

**JA** ある投資リサーチデスクは、Claude Agent SDKを使用してマルチエージェントの株式調査システムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、財務ニュースと開示資料を検索するもの、証券アナリストのPDFレポートを分析するもの、知見を統合するもの、レポートを生成するものがあります。

統合フェーズには、次の2つのクライアントツールが与えられています。

analyze_content（Web検索の抜粋を分析する）

analyze_content_docs（アップロードされたPDFを分析する）

評価の過程で、モデルは検索結果に対してPDF向けのツールを呼び、PDFの抜粋に対してWeb向けのツールを呼ぶ、という誤りを頻繁に起こしています。両方のツールの説明文はほぼ同じで、「コンテンツを分析して主要な知見を返す」としか書かれていません。

チームは、出力仕様と監査ログを別々に管理するため、Web抜粋向けとPDF向けの分析ツールを今後も別々に公開する必要があります。

誤ったツール呼び出しを最も効果的に減らせる変更はどれですか。

**KO** 한 투자 리서치 데스크는 Claude Agent SDK로 multi-agent 주식 조사 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent에는 금융 뉴스와 공시 자료를 검색하는 것, 증권 애널리스트의 PDF 리포트를 분석하는 것, 발견 사항을 통합하는 것, 보고서를 생성하는 것이 있습니다.

통합 단계에는 다음 두 클라이언트 도구가 주어져 있습니다.

analyze_content(웹 검색 발췌를 분석)

analyze_content_docs(업로드된 PDF를 분석)

평가 과정에서 모델은 검색 결과에 PDF용 도구를 호출하고, PDF 발췌에 웹용 도구를 호출하는 실수를 자주 저지릅니다. 두 도구의 설명문은 거의 같으며, “콘텐츠를 분석해 주요 발견 사항을 반환한다”라고만 적혀 있습니다.

팀은 출력 사양과 감사 로그를 따로 관리하기 때문에, 웹 발췌용과 PDF용 분석 도구를 앞으로도 따로 공개해야 합니다.

잘못된 도구 호출을 가장 효과적으로 줄일 수 있는 변경은 무엇입니까?

- A. JA: ソースを示す名前に変え、各説明文に使う場面と使わない場面の境界を書く。
  - KO: 출처를 나타내는 이름으로 바꾸고, 각 설명문에 써야 할 때와 쓰지 말아야 할 때의 경계를 적습니다.
  - EN: Rename the tools to indicate their sources, and write in each description the boundaries of when to use and when not to use it.
- B. JA: ツール名はそのままにして、統合フェーズのプロンプトに例を足し、慎重に選ぶようClaudeに頼む。
  - KO: 도구 이름은 그대로 두고, 통합 단계 prompt에 예시를 추가해 Claude에게 신중히 고르라고 요청합니다.
  - EN: Leave the tool names as they are, add examples to the synthesis phase prompt, and ask Claude to choose carefully.
- C. JA: 2つの分析ツールを汎用ツール1つに統合し、ソースごとの扱いはツール内部で判断させる。
  - KO: 두 분석 도구를 범용 도구 하나로 합치고, 출처별 처리는 도구 내부에서 판단하게 합니다.
  - EN: Merge the two analysis tools into one general-purpose tool, and let the tool decide internally how to handle each source.
- D. JA: tool_choiceでまず文書分析ツールを強制し、結果が不十分なときだけWeb分析ツールを呼ばせる。
  - KO: tool_choice로 먼저 문서 분석 도구를 강제하고, 결과가 불충분할 때만 웹 분석 도구를 호출하게 합니다.
  - EN: Use tool_choice to force the document analysis tool first, and call the web analysis tool only when the results are insufficient.

## CCAR-F-Udemy02-0017

**JA** あなたは、Claude Agent SDKを使用して、医療保険の会員対応エージェントを構築しています。このエージェントは、保険金請求の異議申し立て、保険料請求、保障内容の確認など、あいまいさの高いリクエストを処理します。カスタムのModel Context Protocol（MCP）ツール（get_member、lookup_claim、process_reimbursement、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を維持することです。

ある保険会社のサポート自動化チームでは、MCPツールの呼び出しは成功しているものの、返り値の形式が一貫していません。次の2種類のレスポンスが混在しています。

Unixタイムスタンプと数値のステータスコードを使うレスポンス

ISO 8601形式の日付と文字列のステータス値を使うレスポンス

Claudeは、請求が払い戻しの対象かどうかを判断する際に、これらのフィールドを取り違えることがあります。

Claudeが成功したツール結果を推論に使う前に、正規化された表現を与えるため、このチームが実装すべきものはどれですか。（2つ選択してください。）

**KO** 당신은 Claude Agent SDK로 의료보험 가입자 응대 agent를 구축하고 있습니다. 이 agent는 보험금 청구 이의 제기, 보험료 청구, 보장 내용 확인 등 모호성이 높은 요청을 처리합니다. custom Model Context Protocol(MCP) 도구(get_member, lookup_claim, process_reimbursement, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation해야 할 시점을 판단하면서 1차 해결률 80% 이상을 유지하는 것입니다.

한 보험회사의 지원 자동화팀에서는 MCP 도구 호출은 성공하지만 반환값 형식이 일관되지 않습니다. 다음 두 종류의 응답이 섞여 있습니다.

Unix 타임스탬프와 숫자 상태 코드를 쓰는 응답

ISO 8601 형식 날짜와 문자열 상태 값을 쓰는 응답

Claude는 청구가 환급 대상인지 판단할 때 이 필드들을 혼동하기도 합니다.

Claude가 성공한 도구 결과를 추론에 쓰기 전에 정규화된 표현을 주려면, 이 팀은 무엇을 구현해야 합니까? (2개 선택하십시오.)

- A. JA: MCPツールの実装側で日付とステータスのフィールドを正規化し、正規化済みの値を返すようにする。
  - KO: MCP 도구 구현 쪽에서 날짜와 상태 필드를 정규화해, 정규화된 값을 반환하게 합니다.
  - EN: Normalize the date and status fields in the MCP tool implementation so that it returns normalized values.
- B. JA: tool_responseを読み取り、正規化されたフィールドを含むhookSpecificOutput.updatedToolOutputを返すPostToolUseフックを追加する。
  - KO: tool_response를 읽어 정규화된 필드를 담은 hookSpecificOutput.updatedToolOutput을 반환하는 PostToolUse hook을 추가합니다.
  - EN: Add a PostToolUse hook that reads tool_response and returns hookSpecificOutput.updatedToolOutput containing the normalized fields.
- C. JA: 一貫性のないフィールドについてのマッピングを含むhookSpecificOutput.additionalContextを返すPostToolUseフックを追加する。
  - KO: 일관되지 않은 필드에 대한 매핑을 담은 hookSpecificOutput.additionalContext를 반환하는 PostToolUse hook을 추가합니다.
  - EN: Add a PostToolUse hook that returns hookSpecificOutput.additionalContext containing a mapping for the inconsistent fields.
- D. JA: ツールレスポンスが非正規のフィールドを使っている場合にdecision: "block"を返すPostToolUseフックを追加する。
  - KO: 도구 응답이 정규화되지 않은 필드를 쓰면 decision: "block"을 반환하는 PostToolUse hook을 추가합니다.
  - EN: Add a PostToolUse hook that returns decision: "block" when a tool response uses non-normalized fields.

## CCAR-F-Udemy02-0018

**JA** あなたはフィンテック企業で、Messages APIを使ってClaudeをリリースパイプラインの自動レビューエージェントとして組み込んでいます。このエージェントは、プルリクエストごとに静的解析を実行し、テストケースの提案とレビューのフィードバックを生成します。

あるPRのレビュー中に、Claudeはsubmit_review_findingsツールを呼び出しました。引数のJSONは構文的に正しく、スキーマにも完全に準拠していました。しかし社内のCI検証ロジックは、次の指摘が含まれていることを理由に、この実行を拒否しました。

変更されていないファイルを参照する指摘

社内のレビューポリシーに違反する指摘

Claudeがレビュー出力を修正しやすくするために、この統合が次に行うべき対応はどれですか。（2つ選択してください。）

**KO** 당신은 핀테크 기업에서 Messages API로 Claude를 릴리스 pipeline의 자동 리뷰 agent로 넣고 있습니다. 이 agent는 pull request마다 정적 분석을 실행하고, 테스트 케이스 제안과 리뷰 피드백을 생성합니다.

한 PR을 리뷰하는 중에 Claude가 submit_review_findings 도구를 호출했습니다. 인수 JSON은 구문상 올바르고 schema도 완전히 준수했습니다. 그러나 사내 CI 검증 로직은 다음 지적 사항이 들어 있다는 이유로 이 실행을 거부했습니다.

변경되지 않은 파일을 참조하는 지적

사내 리뷰 정책을 위반하는 지적

Claude가 리뷰 출력을 쉽게 고칠 수 있도록, 이 통합이 다음에 해야 할 대응은 무엇입니까? (2개 선택하십시오.)

- A. JA: 拒否されたtool_useとそのエラー結果を会話履歴に残したまま、次のリクエストを送る。
  - KO: 거부된 tool_use와 그 오류 결과를 대화 이력에 남긴 채 다음 요청을 보냅니다.
  - EN: Send the next request while keeping the rejected tool_use and its error result in the conversation history.
- B. JA: 検証を通った指摘だけを公開し、拒否された指摘は破棄して実行を完了させる。
  - KO: 검증을 통과한 지적만 공개하고, 거부된 지적은 버린 뒤 실행을 완료합니다.
  - EN: Publish only the findings that passed validation, discard the rejected findings, and complete the run.
- C. JA: そのtool_use_idにis_error: trueのtool_resultを返し、拒否理由を指摘ごとに書く。
  - KO: 그 tool_use_id에 is_error: true인 tool_result를 반환하고, 거부 이유를 지적마다 적습니다.
  - EN: Return a tool_result with is_error: true for that tool_use_id, stating the reason for rejection for each finding.
- D. JA: 「レビュー指摘は社内ポリシーを満たすこと」という一般的な指示をシステムプロンプトに追加して再実行する。
  - KO: “리뷰 지적은 사내 정책을 충족할 것”이라는 일반적인 지시를 system prompt에 추가하고 다시 실행합니다.
  - EN: Add the general instruction "Review findings must satisfy internal policy" to the system prompt and rerun.

## CCAR-F-Udemy02-0019

**JA** あるゲームスタジオのライブ運用チームは、Claude CodeをCI/CDパイプラインに統合しています。このシステムは、自動コードレビューを実行し、テストケースを生成し、プルリクエストにフィードバックを返します。具体的で実行可能なフィードバックを返し、誤検知を最小限に抑えるプロンプトを設計する必要があります。

このチームは、フレーキーテスト（不安定なテスト）のリスクを検出する、新しい自動レビュー機能を設計しています。ただし、求められる挙動について、製品やワークフローの面で次のような疑問が未解決のまま残っています。

どのようなコメントが対応可能で、どのようなコメントがノイズなのか

何を検証すれば、実装が正しいと証明できるのか

Claude Codeに実装を依頼する前に、このチームがまず行うべきことはどれですか。

**KO** 한 게임 스튜디오의 라이브 운영팀은 Claude Code를 CI/CD pipeline에 통합하고 있습니다. 이 시스템은 자동 코드 리뷰를 실행하고, 테스트 케이스를 생성하며, pull request에 피드백을 남깁니다. 구체적이고 실행 가능한 피드백을 주면서 오탐을 최소화하는 prompt를 설계해야 합니다.

이 팀은 flaky test(불안정한 테스트)의 위험을 감지하는 새 자동 리뷰 기능을 설계하고 있습니다. 다만 원하는 동작에 대해 제품과 workflow 측면에서 다음과 같은 의문이 아직 풀리지 않았습니다.

어떤 코멘트가 대응 가능한 것이고, 어떤 코멘트가 노이즈인가

무엇을 검증해야 구현이 올바르다고 증명할 수 있는가

Claude Code에 구현을 맡기기 전에 이 팀이 먼저 해야 할 일은 무엇입니까?

- A. JA: 最近のプルリクエストの議論から不足している要件を推測する、自律的なClaude Codeジョブを定期実行する。
  - KO: 최근 pull request 논의에서 부족한 요구 사항을 추론하는 자율적인 Claude Code job을 정기적으로 실행합니다.
  - EN: Periodically run an autonomous Claude Code job that infers the missing requirements from recent pull request discussions.
- B. JA: Agentツールで委任したサブエージェントにAskUserQuestionで質問させ、その記録を実装担当のセッションへ渡す。
  - KO: Agent 도구로 위임한 subagent가 AskUserQuestion으로 질문하게 하고, 그 기록을 구현 담당 session에 넘깁니다.
  - EN: Have a subagent delegated through the Agent tool ask questions with AskUserQuestion, and pass the record to the implementing session.
- C. JA: 詳細なレビューチェックリストをプロンプトに含めて直接実行し、最初のCI失敗を見て調整する。
  - KO: 상세한 리뷰 체크리스트를 prompt에 넣어 직접 실행하고, 첫 CI 실패를 보고 조정합니다.
  - EN: Include a detailed review checklist in the prompt, run it directly, and adjust after seeing the first CI failures.
- D. JA: AskUserQuestionでClaudeに質問させながらSPEC.mdをまとめさせ、新しいセッションで実装する。
  - KO: Claude가 AskUserQuestion으로 질문하면서 SPEC.md를 정리하게 하고, 새 session에서 구현합니다.
  - EN: Have Claude ask questions with AskUserQuestion while compiling a SPEC.md, and then implement in a new session.

## CCAR-F-Udemy02-0020

**JA** あなたは、Claude Agent SDKを使用して保険金請求対応エージェントを構築しています。このエージェントは、支払い調整、補償範囲の照会、払戻し可否など、あいまいさの高い問い合わせを処理します。カスタムのMCPツール（get_policyholder、lookup_claim、issue_payout、escalate_to_adjuster）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を維持することです。

ある保険会社のエンジニアリングチームが、Claude Agent SDKとこれらのMCPツールを使って、このエージェントを構築しています。テスト中にエージェントのトレースを見ると、ClaudeはMCP経由でlookup_claimをリクエストしているものの、請求内容の照会結果が観測されていません。セッションは、顧客への最終的な回答を出さないまま終了してしまいます。

このチームが行うべき実装上の変更はどれですか。

**KO** 당신은 Claude Agent SDK로 보험금 청구 대응 agent를 구축하고 있습니다. 이 agent는 지급 조정, 보장 범위 조회, 환급 가능 여부 등 모호성이 높은 문의를 처리합니다. custom MCP 도구(get_policyholder, lookup_claim, issue_payout, escalate_to_adjuster)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation해야 할 시점을 판단하면서 1차 해결률 80% 이상을 유지하는 것입니다.

한 보험회사의 엔지니어링팀이 Claude Agent SDK와 이 MCP 도구들로 이 agent를 구축하고 있습니다. 테스트 중 agent의 트레이스를 보면, Claude는 MCP를 통해 lookup_claim을 요청하지만 청구 조회 결과는 관측되지 않습니다. session은 고객에게 최종 답변을 내지 못한 채 끝나 버립니다.

이 팀이 해야 할 구현상의 변경은 무엇입니까?

- A. JA: 起動前にサポート用のMCPツールを一通り実行し、その出力をClaudeに1ターンで要約させる。
  - KO: 시작 전에 지원용 MCP 도구를 한 번씩 모두 실행하고, 그 출력을 Claude가 한 turn에 요약하게 합니다.
  - EN: Run all the support MCP tools before startup and have Claude summarize their outputs in one turn.
- B. JA: アシスタントの文章から完了を示す言い回しを検出し、解決したと述べた時点でワークフローを終える。
  - KO: 어시스턴트 문장에서 완료를 나타내는 표현을 감지해, 해결했다고 말한 시점에 workflow를 끝냅니다.
  - EN: Detect phrases indicating completion in the assistant's text, and end the workflow when it says the issue is resolved.
- C. JA: 各MCPバックエンド操作はClaude自身が実行してから回答するよう、システム指示に追加する。
  - KO: 각 MCP 백엔드 작업은 Claude 자신이 실행한 뒤 답하라고 system 지시에 추가합니다.
  - EN: Add to the system instructions that Claude itself must execute each MCP backend operation before responding.
- D. JA: SDKのエージェントループで実行し、ツール呼び出しの結果を返して最終応答まで処理を続けさせる。
  - KO: SDK의 agent loop에서 실행해, 도구 호출 결과를 돌려주고 최종 응답까지 처리를 이어 가게 합니다.
  - EN: Run in the SDK's agent loop, returning the results of tool calls and continuing processing until the final response.

## CCAR-F-Udemy02-0021

**JA** ある再生可能エネルギー会社では、Claude Agent SDKを使用して、送電網の系統連系フィージビリティ調査システムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、技術文書を分析するもの、知見を統合するもの、報告書を生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的な報告書を作成します。

評価の過程で、統合サブエージェントが、サブエージェントの出力を連結した長いテキストを受け取ったときに、次のような傾向があることが分かりました。

束の途中にある根拠のしっかりした知見を、繰り返し省いてしまう

冒頭と末尾付近の知見は保持される

統合ステップを元の根拠に基づかせたまま、この失敗を最も効果的に減らせる変更はどれですか。

**KO** 한 재생에너지 회사에서는 Claude Agent SDK로 송전망 계통 연계 타당성 조사 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent에는 웹을 검색하는 것, 기술 문서를 분석하는 것, 발견 사항을 통합하는 것, 보고서를 생성하는 것이 있습니다. 이 시스템은 주제를 조사해 출처를 명시한 종합 보고서를 작성합니다.

평가 과정에서, 통합 subagent가 여러 subagent의 출력을 이어 붙인 긴 텍스트를 받으면 다음과 같은 경향을 보인다는 사실이 드러났습니다.

묶음 중간에 있는, 근거가 탄탄한 발견 사항을 반복해서 빠뜨립니다

앞부분과 끝부분 근처의 발견 사항은 유지됩니다

통합 단계가 원래 근거에 기반하도록 유지하면서, 이 실패를 가장 효과적으로 줄일 수 있는 변경은 무엇입니까?

- A. JA: 詳細な根拠を段階的に短くした要約に置き換え、最新の要約だけを統合エージェントに渡す。
  - KO: 상세한 근거를 단계적으로 짧게 줄인 요약으로 바꾸고, 가장 최근 요약만 통합 agent에 넘깁니다.
  - EN: Replace the detailed evidence with progressively shorter summaries, and pass only the latest summary to the synthesis agent.
- B. JA: 集約された出力の前に簡潔な知見マップを付加し、詳細な根拠を出典とトピックの明示的な見出しでグループ化する。
  - KO: 집계된 출력 앞에 간결한 발견 사항 맵을 붙이고, 상세한 근거를 출처와 주제별 명시적 제목 아래에 묶습니다.
  - EN: Prepend a concise findings map before the aggregated output, and group the detailed evidence under explicit headings by source and topic.
- C. JA: すべての出典URLを末尾の付録に移し、説明的な根拠は1つの連続したセクションにまとめておく。
  - KO: 모든 출처 URL을 끝의 부록으로 옮기고, 설명적인 근거는 하나의 연속된 섹션에 모아 둡니다.
  - EN: Move all source URLs to an appendix at the end, and keep the descriptive evidence together in a single continuous section.
- D. JA: サブエージェントの出力を完了順に連結し、統合エージェントに束全体から主要テーマを推測させる。
  - KO: subagent 출력을 완료 순서대로 이어 붙이고, 통합 agent가 묶음 전체에서 주요 주제를 추론하게 합니다.
  - EN: Concatenate the subagent outputs in order of completion, and have the synthesis agent infer the main themes from the whole bundle.

## CCAR-F-Udemy02-0022

**JA** ある投資リサーチデスクは、Claude Agent SDKを使用してマルチエージェントの株式調査システムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、財務ニュースと開示資料を検索するもの、証券アナリストのPDFレポートを分析するもの、知見を統合するもの、レポートを生成するものがあります。

リファクタリング計画を確定する前に変更対象のパッケージを調査するため、依存関係の影響を調べる名前付きサブエージェントを使っています。

ところが、サブエージェントが影響対象のファイルを複数特定した後に、ローカルのテストコマンドが断続的にタイムアウトします。親の会話には「impact analysis failed」という結果だけが返されるため、有用な知見が計画から抜け落ちてしまいます。

親の会話を生の調査出力で溢れさせずに、失敗への耐性を最もよく保てる変更はどれですか。

**KO** 한 투자 리서치 데스크는 Claude Agent SDK로 multi-agent 주식 리서치 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 금융 뉴스·공시 자료 검색용, 증권사 애널리스트 PDF 보고서 분석용, 발견 내용 통합용, 보고서 생성용이 있습니다.

refactoring 계획을 확정하기 전에 변경 대상 패키지를 조사하려고, 의존성 영향을 조사하는 이름 있는(named) subagent를 사용하고 있습니다.

그런데 subagent가 영향받는 파일을 여러 개 찾아낸 뒤에 로컬 테스트 명령이 간헐적으로 timeout됩니다. 부모 대화에는 "impact analysis failed"라는 결과만 돌아오기 때문에, 유용한 발견 내용이 계획에서 빠져 버립니다.

부모 대화를 날것의 조사 출력으로 넘치게 하지 않으면서, 실패에 대한 내성을 가장 잘 유지할 수 있는 변경은 무엇입니까?

- A. JA: 親がサブエージェントの途中のBash呼び出しを確認し、失敗したコマンドだけを計画前に再実行する。
  - KO: 부모가 subagent의 중간 Bash 호출을 확인하고, 실패한 명령만 계획 전에 다시 실행합니다.
  - EN: Have the parent inspect the subagent's intermediate Bash calls and re-run only the failed commands before planning.
- B. JA: toolsとdisallowedToolsを未設定のままにし、継承されたアクセス権でBashのリトライを抑える。
  - KO: tools와 disallowedTools를 설정하지 않은 채로 두고, 상속된 접근 권한으로 Bash 재시도를 억제합니다.
  - EN: Leave tools and disallowedTools unset, and use the inherited access to suppress Bash retries.
- C. JA: サブエージェント内で一時的な失敗をリトライさせ、得られた知見と未解決のエラーを最終結果に含めさせる。
  - KO: subagent 안에서 일시적인 실패를 재시도하게 하고, 얻은 발견 내용과 해결되지 않은 오류를 최종 결과에 포함하게 합니다.
  - EN: Have the subagent retry transient failures internally and include the findings it obtained and any unresolved errors in its final result.
- D. JA: 依存関係の影響の調査を親の会話に戻し、計画作成の材料としてコマンドログを残す。
  - KO: 의존성 영향 조사를 부모 대화로 되돌리고, 계획 작성 자료로 명령 로그를 남깁니다.
  - EN: Move the dependency impact investigation back into the parent conversation, and keep the command logs as material for creating the plan.

## CCAR-F-Udemy02-0023

**JA** あなたは、Claude Agent SDKを使用して、動画配信サービスのカスタマーサポート解決エージェントを構築しています。このエージェントは、解約、請求に関する異議申し立て、アカウントの問題など、あいまいさの高いリクエストを処理します。カスタムのModel Context Protocol（MCP）ツール（get_customer、lookup_order、process_refund、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を維持することです。

このチームは、緊急性の低い解決後の品質チェックを、Message Batches APIに移行したいと考えています。条件は次のとおりです。

ケースは継続的に到着する

監査のトリアージのため、各チェックは、ケースの到着から30時間以内にバッチの最終結果が得られている必要がある

バッチは、結果が得られるか期限切れになるまでに、ドキュメントに記載された24時間の処理ウィンドウをすべて使う場合があるものとする

チームが使うべき送信間隔はどれですか。

**KO** 당신은 Claude Agent SDK로 동영상 streaming 서비스의 고객 지원 해결 agent를 구축하고 있습니다. 이 agent는 해지, 청구 이의 제기, 계정 문제처럼 모호성이 높은 요청을 처리합니다. custom Model Context Protocol(MCP) 도구(get_customer, lookup_order, process_refund, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation이 필요한 시점을 가려내면서 첫 응대 해결률 80% 이상을 유지하는 것입니다.

이 팀은 긴급하지 않은 해결 후 품질 점검을 Message Batches API로 옮기려고 합니다. 조건은 다음과 같습니다.

케이스는 계속해서 들어옵니다

감사 트리아지를 위해, 각 점검은 케이스가 들어온 뒤 30시간 이내에 batch의 최종 결과를 받아야 합니다

batch는 결과가 나오거나 만료되기까지, 문서에 명시된 24시간 처리 윈도를 모두 쓸 수 있다고 가정합니다

팀이 사용해야 할 전송 간격은 무엇입니까?

- A. JA: custom_idで各ケースの結果を突き合わせながら、蓄積したリクエストを1日に1回送信する。
  - KO: custom_id로 각 케이스의 결과를 대조하면서, 쌓인 요청을 하루에 한 번 전송합니다.
  - EN: Submit the accumulated requests once a day, matching each case's result by custom_id.
- B. JA: custom_idで各ケースの結果を突き合わせながら、蓄積したリクエストを8時間ごとに送信する。
  - KO: custom_id로 각 케이스의 결과를 대조하면서, 쌓인 요청을 8시간마다 전송합니다.
  - EN: Submit the accumulated requests every 8 hours, matching each case's result by custom_id.
- C. JA: custom_idで各ケースの結果を突き合わせながら、蓄積したリクエストを12時間ごとに送信する。
  - KO: custom_id로 각 케이스의 결과를 대조하면서, 쌓인 요청을 12시간마다 전송합니다.
  - EN: Submit the accumulated requests every 12 hours, matching each case's result by custom_id.
- D. JA: custom_idで各ケースの結果を突き合わせながら、蓄積したリクエストを4時間ごとに送信する。
  - KO: custom_id로 각 케이스의 결과를 대조하면서, 쌓인 요청을 4시간마다 전송합니다.
  - EN: Submit the accumulated requests every 4 hours, matching each case's result by custom_id.

## CCAR-F-Udemy02-0024

**JA** あるコンサルティング企業のリサーチチームは、Claude Agent SDKを使用してマルチエージェントリサーチシステムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

広いトピックでベンチマークを実行すると、処理が遅く、カバー範囲にもムラがあります。ログを見ると、コーディネーターは次の順で処理していました。

1人の専門サブエージェントに、すべての観点を順番に調査させる

圧縮した文章の要約を、次の専門サブエージェントへ渡す

そのあとで初めて、最終レポートを依頼する

関連する観点は開始時点ですでに判明しており、互いに依存関係もありません。

レイテンシとカバー範囲を改善しつつ、一貫性のある最終レポートを維持するために、最も効果的な設計変更はどれですか。（2つ選択してください。）

**KO** 한 컨설팅 기업의 리서치 팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 웹 검색용, 문서 분석용, 조사 결과 통합용, 보고서 생성용이 있습니다. 이 시스템은 주제를 조사해 출처를 명시한 종합 보고서를 작성합니다.

넓은 주제로 벤치마크를 실행하면 처리가 느리고 커버리지도 고르지 않습니다. 로그를 보니 coordinator는 다음 순서로 처리하고 있었습니다.

전문 subagent 하나에게 모든 관점을 차례로 조사하게 합니다

압축한 텍스트 요약을 다음 전문 subagent에게 넘깁니다

그다음에야 최종 보고서를 요청합니다

관련된 관점은 시작 시점에 이미 파악되어 있고, 서로 의존 관계도 없습니다.

일관성 있는 최종 보고서를 유지하면서 지연 시간(latency)과 커버리지를 개선하는 데 가장 효과적인 설계 변경은 무엇입니까? (2개를 고르십시오.)

- A. JA: 各専門サブエージェントに、未完了の観点を別の専門サブエージェントへ引き継がせ、互いの非公開のコンテキストを統合したうえで、統合済みの回答をコーディネーターへ返させる。
  - KO: 각 전문 subagent가 끝내지 못한 관점을 다른 전문 subagent에게 넘기게 하고, 서로의 비공개 context를 합친 뒤 통합된 답변을 coordinator에게 돌려주게 합니다.
  - EN: Have each specialized subagent hand off its unfinished aspects to another specialized subagent, merge each other's private context, and return the merged answer to the coordinator.
- B. JA: コーディネーターが並列のツール利用を無効化して各観点を別々のターンで処理し、生の結果をすべて追記していき、最後のサブタスクの後に統合する。
  - KO: coordinator가 병렬 도구 사용을 끄고 각 관점을 별도의 turn에서 처리하며, 날것의 결과를 모두 덧붙여 나간 뒤 마지막 하위 작업이 끝나면 통합합니다.
  - EN: Have the coordinator disable parallel tool use and handle each aspect in a separate turn, appending all raw results as it goes, and synthesize after the last subtask.
- C. JA: コーディネーターが依頼を観点ごとのサブタスクに分け、共有の制約条件を添えて独立した専門サブエージェントをまとめて呼び出し、それぞれの知見を統合する。
  - KO: coordinator가 요청을 관점별 하위 작업으로 나누고, 공통 제약 조건을 붙여 독립된 전문 subagent들을 한꺼번에 호출한 뒤 각각의 발견 내용을 통합합니다.
  - EN: Have the coordinator split the request into per-aspect subtasks, invoke independent specialized subagents together with shared constraints attached, and then consolidate their findings.
- D. JA: コーディネーターが各専門サブエージェントに自己完結したブリーフを渡し、どの専門サブエージェントもほかのサブエージェントの要約を待たずに済むようにする。
  - KO: coordinator가 각 전문 subagent에게 그 자체로 완결된 브리프를 넘겨, 어떤 전문 subagent도 다른 subagent의 요약을 기다리지 않아도 되게 합니다.
  - EN: Have the coordinator give each specialized subagent a self-contained brief so that no specialized subagent has to wait for another subagent's summary.

## CCAR-F-Udemy02-0025

**JA** 医療保険の請求処理システムを提供する会社では、会員からのあいまいな問い合わせ（保険金請求の異議申し立て、加入資格の確認、アカウントの問題など）を解決するエージェントを、Claude Agent SDKで構築しています。このエージェントは、カスタムのModel Context Protocol（MCP）ツール（get_member、lookup_claim、process_adjustment、escalate_to_specialist）を通じて、社内システムにアクセスします。目標は、必要な場合には専門担当者にエスカレーションしながら、初回解決率80%以上を達成することです。

このチームは、保険金調整やエスカレーションのポリシーの変更をGitHubで管理しており、スケジュールされたレビューバッチのときだけ、マネージド版のClaude Code Reviewを依頼しています。

あるレビュアーが@claude review onceとコメントし、修正がプッシュされた後に、もう一度@claude review onceとコメントしました。すると、解消済みのはずのいくつかの指摘が、新しいインラインコメントとして繰り返されてしまいました。

チームは、次回の手動での再レビューで、最初のレビューで見つかった未解消の問題は確実に表示させつつ、レビュアーの信頼を損なわないようにしたいと考えています。

変更すべきことはどれですか。

**KO** 의료보험 청구 처리 시스템을 제공하는 회사에서는 회원의 모호한 문의(보험금 청구 이의 제기, 가입 자격 확인, 계정 문제 등)를 해결하는 agent를 Claude Agent SDK로 구축하고 있습니다. 이 agent는 custom Model Context Protocol(MCP) 도구(get_member, lookup_claim, process_adjustment, escalate_to_specialist)를 통해 사내 시스템에 접근합니다. 목표는 필요할 때 전문 담당자에게 escalation하면서 첫 응대 해결률 80% 이상을 달성하는 것입니다.

이 팀은 보험금 조정과 escalation 정책의 변경을 GitHub에서 관리하며, 예약된 리뷰 batch 때에만 managed 버전의 Claude Code Review를 요청하고 있습니다.

한 리뷰어가 @claude review once라고 댓글을 달았고, 수정 사항이 push된 뒤 다시 @claude review once라고 댓글을 달았습니다. 그러자 이미 해결되었어야 할 몇몇 지적이 새 inline 댓글로 반복되었습니다.

팀은 다음번 수동 재리뷰에서 첫 리뷰에서 발견된 미해결 문제는 확실히 표시되게 하면서도, 리뷰어의 신뢰를 잃지 않기를 원합니다.

무엇을 변경해야 합니까?

- A. JA: 再レビューでは過去の指摘を踏まえて新規または未解消の問題だけを報告するよう、REVIEW.mdにガイダンスを追加する。
  - KO: 재리뷰에서는 이전 지적을 고려해 새로운 문제나 미해결 문제만 보고하도록 REVIEW.md에 가이드를 추가합니다.
  - EN: Add guidance to REVIEW.md so that, on re-reviews, Claude takes past findings into account and reports only new or unresolved issues.
- B. JA: 手動コマンドを@claude review alwaysに変え、以後はプッシュのたびにプルリクエストをレビューさせる。
  - KO: 수동 명령을 @claude review always로 바꿔, 이후에는 push할 때마다 pull request를 리뷰하게 합니다.
  - EN: Change the manual command to @claude review always so that the pull request is reviewed on every push from now on.
- C. JA: レビュー用の指示は変更せず、再レビューのたびにメンテナーが重複したインラインスレッドを手作業でクローズする。
  - KO: 리뷰 지시는 바꾸지 않고, 재리뷰할 때마다 메인테이너가 중복된 inline 스레드를 수작업으로 닫습니다.
  - EN: Leave the review instructions unchanged, and have a maintainer manually close the duplicate inline threads after each re-review.
- D. JA: GitHubのChecksタブからレビューを再実行し、Claude Codeに新しいコミットに対するコメントを更新させる。
  - KO: GitHub의 Checks 탭에서 리뷰를 다시 실행하고, Claude Code가 새 commit에 대한 댓글을 갱신하게 합니다.
  - EN: Re-run the review from the GitHub Checks tab and have Claude Code update its comments for the new commit.

## CCAR-F-Udemy02-0026

**JA** あなたは、Claude Agent SDKを使用して、インテリア・家具のEC事業者向けにカスタマーサポート解決エージェントを構築しています。このエージェントは、返品、請求に関する異議申し立て、アカウントの問題など、あいまいさの高いリクエストを処理します。カスタムのModel Context Protocol（MCP）ツール（get_customer、lookup_order、process_refund、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を維持することです。

パイロットテストの間に、返金提案のステップは、パース可能な構造化データを常に生成するようになりました。必須フィールドはすべてそろっており、数値の型も正しくなっています。残っている不具合は次の2つです。

商品クレジットが、shipping_refundフィールドに入れられてしまう

明細ごとの調整額の合計が、要求された返金総額と一致しない

このチームが次に行うべき変更はどれですか。

**KO** 당신은 Claude Agent SDK로 인테리어·가구 이커머스 사업자를 위한 고객 지원 해결 agent를 구축하고 있습니다. 이 agent는 반품, 청구 이의 제기, 계정 문제처럼 모호성이 높은 요청을 처리합니다. custom Model Context Protocol(MCP) 도구(get_customer, lookup_order, process_refund, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation이 필요한 시점을 가려내면서 첫 응대 해결률 80% 이상을 유지하는 것입니다.

파일럿 테스트를 거치면서 환불 제안 단계는 이제 항상 파싱 가능한 구조화 데이터를 생성합니다. 필수 필드는 모두 갖춰져 있고 숫자 타입도 올바릅니다. 남은 결함은 다음 두 가지입니다.

상품 크레딧이 shipping_refund 필드에 들어갑니다

항목별 조정액의 합계가 요청된 환불 총액과 일치하지 않습니다

이 팀이 다음으로 해야 할 변경은 무엇입니까?

- A. JA: プレーンなJSONの指示に切り替え、抽出ステップからツールスキーマを取り除く。
  - KO: 일반 JSON 지시로 바꾸고, 추출 단계에서 도구 schema를 제거합니다.
  - EN: Switch to plain JSON instructions and remove the tool schema from the extraction step.
- B. JA: スキーマの返金フィールドを必須にし、抽出時にnull許容の値を拒否する。
  - KO: schema의 환불 필드를 필수로 만들고, 추출할 때 null을 허용하는 값을 거부합니다.
  - EN: Make the refund fields in the schema required and reject nullable values during extraction.
- C. JA: ツール定義にstrict: trueを設定し、返金提案の入力をスキーマに厳密に一致させる。
  - KO: 도구 정의에 strict: true를 설정해, 환불 제안 입력이 schema와 정확히 일치하게 합니다.
  - EN: Set strict: true in the tool definition so that refund proposal inputs match the schema exactly.
- D. JA: 返金の実行前に業務ルールの検証を追加し、具体的な違反内容を差し戻して修正させる。
  - KO: 환불을 실행하기 전에 업무 규칙 검증을 추가하고, 구체적인 위반 내용을 되돌려 보내 수정하게 합니다.
  - EN: Add business-rule validation before the refund is executed, and send the specific violations back to be corrected.

## CCAR-F-Udemy02-0027

**JA** ある保険会社の社内開発チームは、Claude Codeをコードレビュー自動化パイプラインに統合しています。このシステムは、プルリクエストごとに自動レビューを実行し、具体的で実行可能なフィードバックを返します。

このチームのレビュー用プロンプトは、Claudeにポリシー違反の可能性を検出させ、各指摘にpolicy_sectionとsupporting_quote（根拠となる引用）を必ず含めるよう求めています。

あるプルリクエストは、カスタマーサポートの通話記録（トランスクリプト）の保持（retention）ロジックを追加するものでした。しかし、Claudeに渡したポリシーの抜粋はアプリケーションログと分析イベントに関するものだけで、トランスクリプトに関するポリシーは含まれていませんでした。バリデーターは、supporting_quoteが空であることを理由に、Claudeの指摘を却下しました。

このパイプラインがとるべき対応はどれですか。（2つ選択してください。）

**KO** 한 보험사의 사내 개발팀은 Claude Code를 코드 리뷰 자동화 pipeline에 통합하고 있습니다. 이 시스템은 pull request마다 자동 리뷰를 실행하고, 구체적이고 실행 가능한 피드백을 돌려줍니다.

이 팀의 리뷰용 prompt는 Claude에게 정책 위반 가능성을 찾아내게 하고, 각 지적에 policy_section과 supporting_quote(근거가 되는 인용)를 반드시 포함하도록 요구합니다.

어떤 pull request는 고객 지원 통화 기록(transcript)의 보존(retention) 로직을 추가하는 것이었습니다. 그런데 Claude에게 전달한 정책 발췌는 애플리케이션 로그와 분석 이벤트에 관한 것뿐이었고, transcript에 관한 정책은 들어 있지 않았습니다. validator는 supporting_quote가 비어 있다는 이유로 Claude의 지적을 거부했습니다.

이 pipeline이 취해야 할 대응은 무엇입니까? (2개를 고르십시오.)

- A. JA: 引用を示せない場合は情報不足として返し、引用が付くまで指摘を投稿しない。
  - KO: 인용을 제시할 수 없으면 정보 부족으로 반환하고, 인용이 붙을 때까지 지적을 게시하지 않습니다.
  - EN: If a quote cannot be provided, return the finding as insufficient information and do not post it until a quote is attached.
- B. JA: max_tokensを引き上げ、不足しているポリシーの根拠を応答の続きで補わせる。
  - KO: max_tokens를 늘려, 부족한 정책 근거를 응답의 이어지는 부분에서 보충하게 합니다.
  - EN: Raise max_tokens and have Claude fill in the missing policy evidence in a continuation of the response.
- C. JA: 構造化出力スキーマでsupporting_quoteを必須フィールドにして出力を強制する。
  - KO: 구조화 출력 schema에서 supporting_quote를 필수 필드로 지정해 출력을 강제합니다.
  - EN: Make supporting_quote a required field in the structured output schema to force the output.
- D. JA: 通話トランスクリプトの保持に関するポリシー抜粋を、レビュー用プロンプトに追加で渡す。
  - KO: 통화 transcript 보존에 관한 정책 발췌를 리뷰용 prompt에 추가로 전달합니다.
  - EN: Additionally pass the policy excerpts on call transcript retention to the review prompt.

## CCAR-F-Udemy02-0028

**JA** ある製薬会社では、Claude Agent SDKを使用して、競合情報のリサーチシステムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、規制当局への申請文書を検索するもの、臨床試験文書を分析するもの、知見を統合するもの、報告書を生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的な報告書を作成します。

評価の過程で、最終報告書はよく書けているものの、次の問題が起きることがあると分かりました。

根拠のない主張が含まれる

セクション間の矛盾を見落とす

現在の設計では、報告書生成エージェントが公開前に自分自身の草稿をレビューしています。

レビューの信頼性を最も効果的に改善できるアーキテクチャの変更はどれですか。（2つ選択してください。）

**KO** 한 제약회사는 Claude Agent SDK로 경쟁 정보 리서치 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 규제 당국 제출 문서 검색용, 임상시험 문서 분석용, 발견 내용 통합용, 보고서 생성용이 있습니다. 이 시스템은 주제를 조사해 출처를 명시한 종합 보고서를 작성합니다.

평가 과정에서 최종 보고서는 잘 쓰여 있지만, 다음 문제가 가끔 생긴다는 것을 알게 되었습니다.

근거 없는 주장이 포함됩니다

섹션 간의 모순을 놓칩니다

현재 설계에서는 보고서 생성 agent가 게시 전에 자기 초안을 직접 리뷰합니다.

리뷰의 신뢰성을 가장 효과적으로 개선할 수 있는 아키텍처 변경은 무엇입니까? (2개를 고르십시오.)

- A. JA: 主張と出典の組ごとに独立したレビュアーで検証し、その後で矛盾と抜けを確認する統合パスを実行する。
  - KO: 주장과 출처의 쌍마다 독립된 리뷰어로 검증한 다음, 모순과 누락을 확인하는 통합 패스를 실행합니다.
  - EN: Verify each claim-source pair with an independent reviewer, and then run a synthesis pass that checks for contradictions and gaps.
- B. JA: 検証をサブエージェントに任せ、検証対象の主張と照合すべき出典の抜粋を一緒に渡す。
  - KO: 검증을 subagent에게 맡기고, 검증할 주장과 대조할 출처 발췌를 함께 전달합니다.
  - EN: Delegate verification to a subagent, and pass it the claims to verify together with the source excerpts they should be checked against.
- C. JA: 報告書生成エージェントに、既存の会話履歴のまま草稿直後に拡張版のセルフレビューを行わせる。
  - KO: 보고서 생성 agent가 기존 대화 기록을 그대로 둔 채, 초안 직후에 확장된 셀프 리뷰를 하게 합니다.
  - EN: Have the report generation agent perform an extended self-review immediately after the draft, using the existing conversation history as is.
- D. JA: 統合エージェントに全サブエージェントの出力を一度にまとめさせ、公開前に根拠のない主張へ印を付けさせる。
  - KO: 통합 agent가 모든 subagent의 출력을 한 번에 정리하게 하고, 게시 전에 근거 없는 주장에 표시를 하게 합니다.
  - EN: Have the synthesis agent consolidate all subagent outputs at once and flag unsupported claims before publication.

## CCAR-F-Udemy02-0029

**JA** あなたは、Claude Agent SDKを使用して、航空会社のカスタマーサポート解決エージェントを構築しています。このエージェントは、払い戻し、請求に関する異議申し立て、アカウントの問題など、あいまいさの高いリクエストを処理します。カスタムのModel Context Protocol（MCP）ツール（get_customer、lookup_order、process_refund、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を維持することです。

ある請求トラブルのフローで、Claudeは同じアシスタントターン内でget_customerとlookup_orderをリクエストします。get_customerの呼び出しは成功しますが、lookup_orderは断続的にタイムアウトします。

本番環境のログを見ると、これまでに次の2つの修正が試みられていました。

lookup_orderの結果を、空の注文リストとして成功扱いにする

lookup_orderが失敗するたびに、会話全体を中断する

この信頼性の問題に最も適切に対応できる変更はどれですか。（2つ選択してください。）

**KO** 당신은 Claude Agent SDK로 항공사의 고객 지원 해결 agent를 구축하고 있습니다. 이 agent는 환불, 청구 이의 제기, 계정 문제처럼 모호성이 높은 요청을 처리합니다. custom Model Context Protocol(MCP) 도구(get_customer, lookup_order, process_refund, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation이 필요한 시점을 가려내면서 첫 응대 해결률 80% 이상을 유지하는 것입니다.

어떤 청구 분쟁 흐름에서 Claude는 같은 assistant turn 안에서 get_customer와 lookup_order를 요청합니다. get_customer 호출은 성공하지만, lookup_order는 간헐적으로 timeout됩니다.

프로덕션 로그를 보면 지금까지 다음 두 가지 수정이 시도되었습니다.

lookup_order의 결과를 빈 주문 목록으로 간주해 성공으로 처리하는 방식

lookup_order가 실패할 때마다 대화 전체를 중단하는 방식

이 신뢰성 문제에 가장 적절하게 대응할 수 있는 변경은 무엇입니까? (2개를 고르십시오.)

- A. JA: 並列呼び出しを無効にし、get_customerの結果を確認してからlookup_orderを順に要求させる。
  - KO: 병렬 호출을 끄고, get_customer의 결과를 확인한 뒤 lookup_order를 순서대로 요청하게 합니다.
  - EN: Disable parallel calls and have Claude request lookup_order sequentially after checking the get_customer result.
- B. JA: タイムアウトしたlookup_orderをツールラッパー内でリトライしてから、そのツール結果を返す。
  - KO: timeout된 lookup_order를 도구 wrapper 안에서 재시도한 뒤 그 도구 결과를 반환합니다.
  - EN: Retry the timed-out lookup_order inside the tool wrapper before returning that tool result.
- C. JA: 成功したget_customerと、is_error: trueを付けたlookup_orderの結果を両方返し、会話を続ける。
  - KO: 성공한 get_customer 결과와 is_error: true를 붙인 lookup_order 결과를 모두 반환하고, 대화를 이어 갑니다.
  - EN: Return both the successful get_customer result and the lookup_order result marked with is_error: true, and continue the conversation.
- D. JA: lookup_orderがタイムアウトしたら、PreToolUseフックで以後のlookup_orderの呼び出しを止める。
  - KO: lookup_order가 timeout되면, PreToolUse hook으로 이후의 lookup_order 호출을 막습니다.
  - EN: When lookup_order times out, use a PreToolUse hook to block subsequent lookup_order calls.

## CCAR-F-Udemy02-0030

**JA** 写真共有アプリを開発するスタートアップでは、コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行を使い分けています。

このチームの/reviewコマンドは、正確性・セキュリティ・パフォーマンス・スタイルの4カテゴリで、PRにフィードバックを投稿します。評価データを見ると、次のような傾向があります。

セキュリティに関する指摘は、概ね受け入れられている

スタイルに関するコメントは、「個人の好みの些細な指摘」として却下されることが多い

その結果、開発者はセキュリティの指摘も含めて、レビュー結果全体を無視するようになってしまいました。

最初に行うべき変更はどれですか。

**KO** 사진 공유 앱을 개발하는 스타트업에서는 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 사용하고 있습니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하고, plan mode와 직접 실행을 상황에 맞게 나눠 씁니다.

이 팀의 /review 명령은 정확성·보안·성능·스타일의 4개 카테고리로 PR에 피드백을 게시합니다. 평가 데이터를 보면 다음과 같은 경향이 있습니다.

보안 관련 지적은 대체로 받아들여집니다

스타일 관련 댓글은 "개인 취향에 따른 사소한 지적"으로 거부되는 경우가 많습니다

그 결과, 개발자들은 보안 지적까지 포함해 리뷰 결과 전체를 무시하게 되었습니다.

가장 먼저 해야 할 변경은 무엇입니까?

- A. JA: カテゴリ別に適合率と再現率を測り、実例をもとにノイズの多いスタイル基準を絞るか無効にする。
  - KO: 카테고리별로 정밀도(precision)와 재현율(recall)을 측정하고, 실제 사례를 바탕으로 노이즈가 많은 스타일 기준을 좁히거나 비활성화합니다.
  - EN: Measure precision and recall per category, and narrow or disable the noisy style criteria based on concrete examples.
- B. JA: 全体の受け入れ率だけを追跡し、その集計値が目標を下回ったときにプロンプト全体を見直す。
  - KO: 전체 수용률만 추적하고, 그 집계 값이 목표를 밑돌면 prompt 전체를 다시 검토합니다.
  - EN: Track only the overall acceptance rate, and revise the entire prompt when that aggregate falls below the target.
- C. JA: 全カテゴリの報告しきい値を一律に引き上げ、どのカテゴリでもClaudeにより保守的に指摘させる。
  - KO: 모든 카테고리의 보고 임곗값을 일괄적으로 올려, 어느 카테고리에서든 Claude가 더 보수적으로 지적하게 합니다.
  - EN: Raise the reporting threshold uniformly across all categories so that Claude flags issues more conservatively in every category.
- D. JA: セキュリティの指摘をレポートの先頭に移し、開発者の必読項目として目立たせる。
  - KO: 보안 지적을 보고서 맨 앞으로 옮겨, 개발자가 꼭 읽어야 할 항목으로 눈에 띄게 합니다.
  - EN: Move security findings to the top of the report and make them stand out as required reading for developers.

## CCAR-F-Udemy02-0031

**JA** ある投資ファームでは、Claude Agent SDKを使用して、M&Aデューデリジェンスのリサーチシステムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、公開資料を検索するもの、契約書を分析するもの、リスクに関する知見を統合するもの、デューデリジェンス報告書を生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的な報告書を作成します。

最近の評価で、次の問題が分かりました。

最終報告書で、同じ出典が、ある主張を裏付けるものとしても矛盾するものとしても扱われることがある

長い出典の束の中にある根拠のない主張を、レビュアーが見落とすことがある

チームは、報告書が生成される前に記録・採点できるレビューのチェックポイントも欲しいと考えています。

このチームが行うべきことはどれですか。

**KO** 한 투자 회사는 Claude Agent SDK로 M&A 실사(due diligence) 리서치 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 공개 자료 검색용, 계약서 분석용, 리스크 관련 발견 내용 통합용, 실사 보고서 생성용이 있습니다. 이 시스템은 주제를 조사해 출처를 명시한 종합 보고서를 작성합니다.

최근 평가에서 다음 문제가 드러났습니다.

최종 보고서에서 같은 출처가 어떤 주장을 뒷받침하는 근거로도, 그 주장과 모순되는 근거로도 다뤄지는 경우가 있습니다

긴 출처 묶음 속에 있는 근거 없는 주장을 리뷰어가 놓치는 경우가 있습니다

팀은 보고서가 생성되기 전에 기록하고 채점할 수 있는 리뷰 체크포인트도 원합니다.

이 팀이 해야 할 일은 무엇입니까?

- A. JA: 引用された主張ごとに確信度スコアを付け、スコアの低い主張を別のレビュアーに回す。
  - KO: 인용된 주장마다 확신도 점수를 매기고, 점수가 낮은 주장을 다른 리뷰어에게 넘깁니다.
  - EN: Assign a confidence score to each cited claim, and route low-scoring claims to a different reviewer.
- B. JA: 出典の束全体を1人のレビュアーに送り、報告書生成の前により長いチェックリストを課す。
  - KO: 출처 묶음 전체를 리뷰어 한 명에게 보내고, 보고서 생성 전에 더 긴 체크리스트를 적용합니다.
  - EN: Send the entire source bundle to a single reviewer and impose a longer checklist before report generation.
- C. JA: 同一のレビュアーを複数起動して出典の束全体を読ませ、最も多く一致した結果を採用する。
  - KO: 동일한 리뷰어를 여러 개 실행해 출처 묶음 전체를 읽게 하고, 가장 많이 일치한 결과를 채택합니다.
  - EN: Launch multiple identical reviewers to read the entire source bundle, and adopt the result that most of them agree on.
- D. JA: 出典ごとのレビューパスをプロンプトチェーンで実行し、その後に別の統合パスを実行する。
  - KO: 출처별 리뷰 패스를 prompt chaining으로 실행한 뒤, 별도의 통합 패스를 실행합니다.
  - EN: Run a per-source review pass using prompt chaining, followed by a separate synthesis pass.

## CCAR-F-Udemy02-0032

**JA** 旅行予約プラットフォームを運営する企業は、Claude Codeをコードレビュー自動化パイプラインに統合しています。このシステムは、プルリクエストごとに自動レビューを実行し、テストケースを生成し、具体的で実行可能なフィードバックを返します。誤検知を最小限に抑えるプロンプトを設計する必要があります。

コンプライアンスレビューの結果、必須のテスト結果アーティファクトが添付される前に、システムが承認レビューを投稿してしまうプルリクエストがまれにあることが分かりました。

このルールに例外は認められません。承認の操作は、アーティファクトがすでに存在し、かつ合格している場合にだけ実行する必要があります。

このチームが行うべき変更はどれですか。（2つ選択してください。）

**KO** 여행 예약 플랫폼을 운영하는 기업은 Claude Code를 코드 리뷰 자동화 pipeline에 통합하고 있습니다. 이 시스템은 pull request마다 자동 리뷰를 실행하고, 테스트 케이스를 생성하며, 구체적이고 실행 가능한 피드백을 돌려줍니다. 오탐을 최소화하는 prompt를 설계해야 합니다.

컴플라이언스 검토 결과, 필수 테스트 결과 artifact가 첨부되기 전에 시스템이 승인 리뷰를 게시해 버리는 pull request가 드물게 있다는 것이 밝혀졌습니다.

이 규칙에는 예외가 허용되지 않습니다. 승인 작업은 artifact가 이미 존재하고, 또한 통과한 경우에만 실행되어야 합니다.

이 팀이 해야 할 변경은 무엇입니까? (2개를 고르십시오.)

- A. JA: Claude Codeのステップの前にCIゲートを置き、合格済みアーティファクトが無ければジョブを失敗させる。
  - KO: Claude Code 단계 앞에 CI 게이트를 두고, 통과한 artifact가 없으면 job을 실패시킵니다.
  - EN: Place a CI gate before the Claude Code step that fails the job if there is no passing artifact.
- B. JA: 承認コマンドの完了後に発火するPostToolUseフックで、アーティファクトの有無を確認する。
  - KO: 승인 명령이 완료된 뒤 실행되는 PostToolUse hook에서 artifact가 있는지 확인합니다.
  - EN: Use a PostToolUse hook that fires after the approve command completes to check whether the artifact exists.
- C. JA: 承認前にアーティファクトを確認するよう、システムプロンプトの指示を強い表現に書き換える。
  - KO: 승인 전에 artifact를 확인하도록, system prompt의 지시를 더 강한 표현으로 고쳐 씁니다.
  - EN: Rewrite the system prompt instructions in stronger wording so that Claude checks for the artifact before approving.
- D. JA: 合格済みアーティファクトが無いときに承認コマンドを拒否するPreToolUseフックを追加する。
  - KO: 통과한 artifact가 없을 때 승인 명령을 거부하는 PreToolUse hook을 추가합니다.
  - EN: Add a PreToolUse hook that rejects the approve command when there is no passing artifact.

## CCAR-F-Udemy02-0033

**JA** あなたは、Claude Agent SDKを使用して、マルチエージェントの市場インテリジェンスシステムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、競合他社の価格情報を収集するもの、レビューを分析するもの、知見を統合するもの、提言レポートを生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

長時間の調査を実行していると、後段の統合ターンが、Web検索や文書分析のサブエージェントが以前に返した知見を無視してしまうことがあります。ログを確認すると、後段のMessages API呼び出しには、現在のコーディネーターの指示と最新のサブエージェントの出力しか含まれていません。

この一貫性の問題に最も効果的に対処できる変更はどれですか。（2つ選択してください。）

**KO** 당신은 Claude Agent SDK로 multi-agent 시장 인텔리전스 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 경쟁사 가격 정보 수집용, 리뷰 분석용, 발견 내용 통합용, 제언 보고서 생성용이 있습니다. 이 시스템은 주제를 조사해 출처를 명시한 종합 보고서를 작성합니다.

장시간 조사를 실행하다 보면, 후반의 통합 turn이 웹 검색이나 문서 분석 subagent가 앞서 반환한 발견 내용을 무시하는 경우가 있습니다. 로그를 확인해 보니 후반의 Messages API 호출에는 현재 coordinator의 지시와 최신 subagent 출력만 들어 있었습니다.

이 일관성 문제에 가장 효과적으로 대처할 수 있는 변경은 무엇입니까? (2개를 고르십시오.)

- A. JA: 自動プロンプトキャッシュを有効にし、以前のサブエージェントの知見が、後続のリクエストに含めなくても記憶されるようにする。
  - KO: 자동 prompt caching을 켜서, 이전 subagent의 발견 내용을 이후 요청에 포함하지 않아도 기억되게 합니다.
  - EN: Enable automatic prompt caching so that earlier subagent findings are remembered without being included in subsequent requests.
- B. JA: コーディネーターのセッション識別子を保存し、フォローアップリクエストごとに最新のサブエージェント結果だけを送信する。
  - KO: coordinator의 session 식별자를 저장하고, 후속 요청마다 최신 subagent 결과만 전송합니다.
  - EN: Store the coordinator's session identifier and send only the latest subagent results with each follow-up request.
- C. JA: 関連するmessages配列（過去のアシスタント出力・ツール結果・現在のユーザーターン）を保持して再送する。
  - KO: 관련된 messages 배열(이전 assistant 출력·도구 결과·현재 user turn)을 보관해 두었다가 다시 보냅니다.
  - EN: Retain and resend the relevant messages array (past assistant outputs, tool results, and the current user turn).
- D. JA: これまでのサブエージェントの知見を継続的に更新される要約として保持し、後続のリクエストごとにその最新版を含める。
  - KO: 지금까지의 subagent 발견 내용을 계속 갱신되는 요약으로 유지하고, 이후 요청마다 그 최신판을 포함합니다.
  - EN: Maintain the subagent findings so far as a continuously updated summary, and include its latest version in each subsequent request.

## CCAR-F-Udemy02-0034

**JA** あなたは、Claude Agent SDKを使用して保険金請求のトリアージエージェントを構築しています。このエージェントは、返金請求、保険料の相違、契約者情報の問題など、あいまいさの高い依頼を処理します。カスタムのModel Context Protocol（MCP）ツール（get_member、lookup_claim、process_adjustment、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を達成することです。

このチームは夜間のバックログ処理で、数千件の未解決の会話をMessage Batches APIで一括投入する計画を立てています。バッチの入力には、会員・請求システム向けのMCPバックエンドのクライアントツール定義が含まれます。これらのバックエンドは、チーム自身のサービスが実装しています。

最も適切な設計はどれですか。（2つ選択してください。）

**KO** 당신은 Claude Agent SDK로 보험금 청구 트리아지 agent를 구축하고 있습니다. 이 agent는 환급 청구, 보험료 차이, 계약자 정보 문제처럼 모호성이 높은 요청을 처리합니다. custom Model Context Protocol(MCP) 도구(get_member, lookup_claim, process_adjustment, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation이 필요한 시점을 가려내면서 첫 응대 해결률 80% 이상을 달성하는 것입니다.

이 팀은 야간 백로그 처리에서, 해결되지 않은 대화 수천 건을 Message Batches API로 한꺼번에 투입할 계획입니다. batch 입력에는 회원·청구 시스템용 MCP 백엔드의 client tool 정의가 포함됩니다. 이 백엔드들은 팀 자체 서비스가 구현하고 있습니다.

가장 적절한 설계는 무엇입니까? (2개를 고르십시오.)

- A. JA: 各バッチ項目にcustom_idを設定し、返されたツールリクエストを正しい会話に突き合わせられるようにする。
  - KO: 각 batch 항목에 custom_id를 설정해, 반환된 도구 요청을 올바른 대화와 대조할 수 있게 합니다.
  - EN: Set a custom_id on each batch item so that returned tool requests can be matched to the correct conversation.
- B. JA: 返金処理がフォローアップリクエストなしで完了できるよう、すべてのカスタマーサポートツールをサーバーツールとしてバッチリクエストに組み込む。
  - KO: 환불 처리가 후속 요청 없이 끝날 수 있도록, 모든 고객 지원 도구를 server tool로 batch 요청에 넣습니다.
  - EN: Include all customer support tools in the batch request as server tools so that refund processing can complete without follow-up requests.
- C. JA: 初期分析またはツールリクエストにはバッチを使用し、返されたクライアントツールを実行してから、各案件を後続のMessagesリクエストで継続する。
  - KO: 초기 분석이나 도구 요청에는 batch를 사용하고, 반환된 client tool을 실행한 다음 각 건을 후속 Messages 요청으로 이어 갑니다.
  - EN: Use the batch for the initial analysis or tool requests, execute the returned client tools, and then continue each case with a subsequent Messages request.
- D. JA: 各バッチ項目にクライアントツールのスキーマを含め、バッチワーカーに、レスポンスを確定する前にバックエンドツールを実行させる。
  - KO: 각 batch 항목에 client tool의 schema를 포함하고, batch 워커가 응답을 확정하기 전에 백엔드 도구를 실행하게 합니다.
  - EN: Include the client tool schemas in each batch item, and have the batch worker execute the backend tools before finalizing the response.

## CCAR-F-Udemy02-0035

**JA** あるゲームスタジオのライブ運用チームは、Claude Codeを継続的インテグレーション／継続的デプロイ（CI/CD）パイプラインに統合しています。このシステムは、自動コードレビューを実行し、テストケースを生成し、プルリクエストにフィードバックを返します。具体的で実行可能なフィードバックを返し、誤検知を最小限に抑えるプロンプトを設計する必要があります。

リポジトリのメインの指示ファイルは400行を超え、次の内容が混在するようになっています。

レビューのトーン

テスト規約

API設計ルール

デプロイ時のチェックリスト

CIの実行結果を見ると、Claude Codeが日常的な単体テストのレビューにまでデプロイ時のガイダンスを適用し、開発者が重視するテスト固有の基準を見落とすことがあると分かりました。

共有のレビュー基準は引き続き利用できるようにしたまま、無関係なコンテキストを減らすために、このチームが行うべき変更はどれですか。（2つ選択してください。）

**KO** 한 게임 스튜디오의 라이브 운영팀은 Claude Code를 지속적 통합/지속적 배포(CI/CD) pipeline에 통합하고 있습니다. 이 시스템은 자동 코드 리뷰를 실행하고, 테스트 케이스를 생성하며, pull request에 피드백을 돌려줍니다. 구체적이고 실행 가능한 피드백을 돌려주면서 오탐을 최소화하는 prompt를 설계해야 합니다.

저장소의 메인 지시 파일은 400줄을 넘었고, 다음 내용이 뒤섞여 있습니다.

리뷰 톤

테스트 규약

API 설계 규칙

배포 시 체크리스트

CI 실행 결과를 보면, Claude Code가 일상적인 단위 테스트 리뷰에까지 배포 관련 가이드를 적용하고, 개발자가 중시하는 테스트 고유의 기준을 놓치는 경우가 있었습니다.

공통 리뷰 기준은 계속 쓸 수 있게 하면서 관련 없는 context를 줄이려면, 이 팀은 무엇을 변경해야 합니까? (2개를 고르십시오.)

- A. JA: ルートの指示ファイルを、すべての変更に共通するレビュー基準だけに絞り込む。
  - KO: 루트 지시 파일을 모든 변경에 공통되는 리뷰 기준만 남도록 줄입니다.
  - EN: Trim the root instruction file down to only the review criteria common to all changes.
- B. JA: 各パッケージディレクトリにCLAUDE.mdを作り、関連するテスト・API・デプロイのガイダンスを複製する。
  - KO: 각 패키지 디렉터리에 CLAUDE.md를 만들고, 관련된 테스트·API·배포 가이드를 복제합니다.
  - EN: Create a CLAUDE.md in each package directory and duplicate the relevant test, API, and deployment guidance there.
- C. JA: トピック別のガイダンスをpathsなしで.claude/rules/へ移し、ディレクトリ単位の読み込みに任せる。
  - KO: 주제별 가이드를 paths 없이 .claude/rules/로 옮기고, 디렉터리 단위 로딩에 맡깁니다.
  - EN: Move the topic-specific guidance into .claude/rules/ without paths, and rely on directory-level loading.
- D. JA: トピック別のガイダンスを.claude/rules/のファイルへ移し、特定ファイル向けのものにはpathsを付ける。
  - KO: 주제별 가이드를 .claude/rules/의 파일로 옮기고, 특정 파일용인 것에는 paths를 붙입니다.
  - EN: Move the topic-specific guidance into files under .claude/rules/, and add paths to those intended for specific files.

## CCAR-F-Udemy02-0036

**JA** あなたは、Claude Agent SDKを使用して保険金請求対応エージェントを構築しています。このエージェントは、支払い調整、補償範囲の照会、払戻し可否など、あいまいさの高い問い合わせを処理します。カスタムのMCPツール（get_policyholder、lookup_claim、issue_payout、escalate_to_adjuster）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を維持することです。

チームは、長時間かかる案件を処理できるよう、エージェントをコーディネーター型にリファクタリングしています。コーディネーターは、支払い調整と補償範囲の調査ステップをサブエージェントに委任できます。

テスト中に、係争案件の途中でコンテナがクラッシュしました。その後を引き継いだワーカーは、次の情報を失っていました。

確認済みの契約者ID

それまでの請求内容の調査結果

「この案件はエスカレーションが必要」という判断

ワーカー間でファイルシステムは共有されておらず、ローカルのセッションJSONLファイルも、再起動後に確実に残っているとは限りません。

クラッシュから安全に復旧するために、最も効果的な変更はどれですか。

**KO** 당신은 Claude Agent SDK로 보험금 청구 대응 agent를 구축하고 있습니다. 이 agent는 지불 조정, 보장 범위 조회, 보험금 지급 가능 여부처럼 모호성이 높은 문의를 처리합니다. custom MCP 도구(get_policyholder, lookup_claim, issue_payout, escalate_to_adjuster)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation이 필요한 시점을 가려내면서 첫 응대 해결률 80% 이상을 유지하는 것입니다.

팀은 오래 걸리는 건을 처리할 수 있도록 agent를 coordinator 방식으로 refactoring하고 있습니다. coordinator는 지불 조정과 보장 범위 조사 단계를 subagent에게 위임할 수 있습니다.

테스트 중에 분쟁 건을 처리하던 도중 컨테이너가 크래시되었습니다. 이후 작업을 넘겨받은 워커는 다음 정보를 잃은 상태였습니다.

확인된 계약자 ID

그때까지의 청구 내용 조사 결과

"이 건은 escalation이 필요하다"는 판단

워커 간에 파일 시스템은 공유되지 않으며, 로컬 session JSONL 파일도 재시작 후에 반드시 남아 있다고 보장할 수 없습니다.

크래시에서 안전하게 복구하기 위해 가장 효과적인 변경은 무엇입니까?

- A. JA: システムプロンプトに状態を覚えておくよう強い指示を加え、直近の顧客メッセージから再開する。
  - KO: system prompt에 상태를 기억하라는 강한 지시를 넣고, 가장 최근 고객 메시지부터 재개합니다.
  - EN: Add a strongly worded instruction to the system prompt to remember state, and resume from the most recent customer message.
- B. JA: 確認済みの事実と判断をJSONの状態マニフェストに永続化し、再起動時にプロンプトへ注入する。
  - KO: 확인된 사실과 판단을 JSON 상태 manifest에 영구 저장하고, 재시작할 때 prompt에 주입합니다.
  - EN: Persist the verified facts and decisions in a JSON state manifest, and inject it into the prompt on restart.
- C. JA: ローカルのJSONLトランスクリプトを可能なときにコピーし、引き継いだワーカーで最新に見えるセッションを再開する。
  - KO: 가능할 때 로컬 JSONL transcript를 복사해 두고, 작업을 넘겨받은 워커에서 가장 최신으로 보이는 session을 재개합니다.
  - EN: Copy the local JSONL transcript when possible, and resume the session that appears most recent on the worker that took over.
- D. JA: Agent SDKのセッションをcontinueで再開し、最新のローカルなトランスクリプトから状態を組み立て直す。
  - KO: Agent SDK session을 continue로 재개하고, 가장 최근의 로컬 transcript에서 상태를 다시 구성합니다.
  - EN: Resume the Agent SDK session with continue, and reconstruct the state from the most recent local transcript.

## CCAR-F-Udemy02-0037

**JA** あるサイバーセキュリティ企業では、Claude Agent SDKを使用して、脅威インテリジェンスの調査システムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、OSINT情報源を検索するもの、マルウェア検体を分析するもの、知見を統合するもの、報告書を生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的な報告書を作成します。

ある実行で広範な情報源のレビューが完了し、有用なベースライン分析が得られました。チームは、同じ出発点から2つの異なる対応戦略を比較したいと考えています。それぞれの戦略の探索は、ベースラインのセッション履歴を変更せずに、独自の会話履歴を持つ必要があります。

このチームが行うべきことはどれですか。（2つ選択してください。）

**KO** 한 사이버보안 기업은 Claude Agent SDK로 위협 인텔리전스 조사 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 OSINT 정보원 검색용, 악성코드 샘플 분석용, 발견 내용 통합용, 보고서 생성용이 있습니다. 이 시스템은 주제를 조사해 출처를 명시한 종합 보고서를 작성합니다.

어떤 실행에서 광범위한 정보원 검토가 끝나 유용한 baseline 분석을 얻었습니다. 팀은 같은 출발점에서 서로 다른 두 가지 대응 전략을 비교하려고 합니다. 각 전략의 탐색은 baseline session 기록을 바꾸지 않고, 각자 고유한 대화 기록을 가져야 합니다.

이 팀이 해야 할 일은 무엇입니까? (2개를 고르십시오.)

- A. JA: 各戦略についてファイルのチェックポイント機能を有効にし、チェックポイントをセッション履歴の分岐の仕組みとして使う。
  - KO: 전략마다 파일 checkpoint 기능을 켜고, checkpoint를 session 기록을 분기하는 수단으로 사용합니다.
  - EN: Enable the file checkpointing feature for each strategy, and use checkpoints as the mechanism for branching session history.
- B. JA: 各戦略についてSDKのフォークオプションを有効にしてベースラインのセッションを再開し、新しく生成されたセッションIDを追跡する。
  - KO: 전략마다 SDK의 fork 옵션을 켠 상태로 baseline session을 재개하고, 새로 생성된 session ID를 추적합니다.
  - EN: Resume the baseline session for each strategy with the SDK's fork option enabled, and track the newly generated session ID.
- C. JA: ベースライン分析が完了した時点でそのセッションIDを記録し、各戦略のワーカーに渡す。
  - KO: baseline 분석이 끝난 시점에 그 session ID를 기록해, 각 전략의 워커에 전달합니다.
  - EN: Record the session ID once the baseline analysis is complete, and pass it to the worker for each strategy.
- D. JA: 各戦略のワーカーでcontinueを使い、SDKにカレントディレクトリ内の最新セッションを選択させる。
  - KO: 각 전략의 워커에서 continue를 사용해, SDK가 현재 디렉터리의 가장 최근 session을 선택하게 합니다.
  - EN: Use continue in each strategy's worker, and let the SDK select the most recent session in the current directory.

## CCAR-F-Udemy02-0038

**JA** 健康管理アプリを開発するプロダクトチームでは、コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行を使い分けています。

このチームは、コードレビュー用とドキュメント作成用に、SDKで管理するサブエージェントを追加しようとしています。要件は次の2つです。

Claudeが用途に応じて、適切なサブエージェントに作業を振り分けられる

ドキュメント作成用のサブエージェントには、ファイルの読み取りは許可するが、ファイルの編集やコマンドの実行はさせない

採用すべき構成はどれですか。

**KO** 건강 관리 앱을 개발하는 제품팀에서는 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 사용하고 있습니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하고, plan mode와 직접 실행을 상황에 맞게 나눠 씁니다.

이 팀은 코드 리뷰용과 문서 작성용으로, SDK에서 관리하는 subagent를 추가하려고 합니다. 요구 사항은 다음 두 가지입니다.

Claude가 용도에 따라 적절한 subagent에게 작업을 배분할 수 있어야 합니다

문서 작성용 subagent에는 파일 읽기는 허용하지만, 파일 편집이나 명령 실행은 허용하지 않습니다

채택해야 할 구성은 무엇입니까?

- A. JA: agentsマップに各サブエージェントのdescriptionとpromptを定義し、ドキュメント用のtoolsは読み取り系に限る。
  - KO: agents 맵에 각 subagent의 description과 prompt를 정의하고, 문서용 tools는 읽기 계열로만 제한합니다.
  - EN: Define a description and prompt for each subagent in the agents map, and limit the documentation subagent's tools to read-only ones.
- B. JA: agentsマップを表示名で定義し、用途はprompt内に書き、トップレベルのdisallowedToolsで編集系ツールを止める。
  - KO: agents 맵을 표시 이름으로 정의하고, 용도는 prompt 안에 쓰며, 최상위 disallowedTools로 편집 계열 도구를 막습니다.
  - EN: Define the agents map by display names, write the purpose inside the prompt, and block editing tools with the top-level disallowedTools.
- C. JA: トップレベルのallowedToolsに読み取り系ツールを並べ、ルーティングの方針はCLAUDE.mdに書き、サブエージェント個別のツール設定は省く。
  - KO: 최상위 allowedTools에 읽기 계열 도구를 나열하고, routing 방침은 CLAUDE.md에 쓰며, subagent별 도구 설정은 생략합니다.
  - EN: List read-only tools in the top-level allowedTools, write the routing policy in CLAUDE.md, and omit per-subagent tool settings.
- D. JA: サブエージェントをファイル名で区別し、ルーティングの手がかりは名前に任せ、ツール制限は親の権限設定に委ねる。
  - KO: subagent를 파일 이름으로 구분하고, routing 단서는 이름에 맡기며, 도구 제한은 부모의 권한 설정에 맡깁니다.
  - EN: Distinguish subagents by file name, leave routing cues to the names, and delegate tool restrictions to the parent's permission settings.

## CCAR-F-Udemy02-0039

**JA** あなたは、Claude Agent SDKを使用して保険金請求対応エージェントを構築しています。このエージェントは、支払い調整、補償範囲の照会、払戻し可否など、あいまいさの高い問い合わせを処理します。カスタムのMCPツール（get_policyholder、lookup_claim、issue_payout、escalate_to_adjuster）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を維持することです。

インシデントの振り返りで、このチームは、大規模なリポジトリの中で払戻しエスカレーションの判断がどこで行われているかを、Claude Codeに把握させる必要があります。このセッションでは、組み込みのRead・Grep・Globが有効になっています。

過去の調査では、関連するフローを特定する前にサービス用ディレクトリ全体をコンテキストに読み込んでしまい、セッションがノイズだらけで遅くなっていました。

このチームがまず取るべきアプローチはどれですか。（2つ選択してください。）

**KO** 당신은 Claude Agent SDK로 보험금 청구 대응 agent를 구축하고 있습니다. 이 agent는 지불 조정, 보장 범위 조회, 보험금 지급 가능 여부처럼 모호성이 높은 문의를 처리합니다. custom MCP 도구(get_policyholder, lookup_claim, issue_payout, escalate_to_adjuster)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation이 필요한 시점을 가려내면서 첫 응대 해결률 80% 이상을 유지하는 것입니다.

인시던트 회고에서, 이 팀은 대규모 저장소 안에서 보험금 지급 escalation 판단이 어디서 이루어지는지를 Claude Code가 파악하게 해야 합니다. 이 session에서는 내장 Read·Grep·Glob이 활성화되어 있습니다.

과거 조사에서는 관련 흐름을 찾기도 전에 서비스용 디렉터리 전체를 context에 읽어 들이는 바람에, session이 노이즈투성이가 되고 느려졌습니다.

이 팀이 먼저 취해야 할 접근 방식은 무엇입니까? (2개를 고르십시오.)

- A. JA: まずGlobで対象となるサービス用ディレクトリの候補を絞り込み、そのパスの範囲だけでGrepを実行する。
  - KO: 먼저 Glob으로 대상 서비스용 디렉터리 후보를 좁히고, 그 경로 범위 안에서만 Grep을 실행합니다.
  - EN: First use Glob to narrow down the candidate service directories, and run Grep only within that path scope.
- B. JA: サービス用ディレクトリのREADMEと設定ファイルを先に一通りReadし、設計文書の記述から払戻し判断の箇所を推定する。
  - KO: 서비스용 디렉터리의 README와 설정 파일을 먼저 한 차례 Read하고, 설계 문서의 기술 내용에서 보험금 지급 판단 위치를 추정합니다.
  - EN: First Read through the service directories' READMEs and configuration files, and infer where payout decisions are made from the descriptions in the design documents.
- C. JA: 払戻しとエスカレーションの識別子に対してGrepを使い、一致したファイルだけをReadで読み込み、そのエントリポイントからimportをたどる。
  - KO: 보험금 지급과 escalation 식별자에 대해 Grep을 사용하고, 일치한 파일만 Read로 읽은 뒤 그 entry point에서부터 import를 따라갑니다.
  - EN: Use Grep for payout and escalation identifiers, use Read to load only the matching files, and follow imports from those entry points.
- D. JA: 払戻しとエスカレーションの識別子に対してGlobを使い、返されたパスの一致結果から制御フローを推測する。
  - KO: 보험금 지급과 escalation 식별자에 대해 Glob을 사용하고, 반환된 경로 일치 결과에서 제어 흐름을 추측합니다.
  - EN: Use Glob for payout and escalation identifiers, and infer the control flow from the returned path matches.

## CCAR-F-Udemy02-0040

**JA** 物流プラットフォームを開発する社内チームでは、コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行を使い分けています。

このチームのモノレポでは、単体テストとコンポーネントテストが、services/・packages/・apps/の各配下で、対象のソースファイルのすぐ近くに置かれています。

ところが、同じようなテスト規約の指示が複数のディレクトリ階層のメモリファイルにコピーされており、一部のディレクトリには更新が反映されていません。そのため、Claude Codeが適用するテストの指示に一貫性がありません。

テスト規約の保守を容易にしつつ、テストに関係のない作業では不要なコンテキストを避けるために、変更すべきことはどれですか。（2つ選択してください。）

**KO** 물류 플랫폼을 개발하는 사내 팀에서는 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 사용하고 있습니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하고, plan mode와 직접 실행을 상황에 맞게 나눠 씁니다.

이 팀의 monorepo에서는 단위 테스트와 컴포넌트 테스트가 services/·packages/·apps/ 각각의 아래에서 대상 소스 파일 바로 옆에 놓여 있습니다.

그런데 비슷한 테스트 규약 지시가 여러 디렉터리 계층의 memory 파일에 복사되어 있고, 일부 디렉터리에는 업데이트가 반영되지 않았습니다. 그래서 Claude Code가 적용하는 테스트 지시에 일관성이 없습니다.

테스트 규약을 쉽게 유지보수하면서 테스트와 관련 없는 작업에서는 불필요한 context를 피하려면, 무엇을 변경해야 합니까? (2개를 고르십시오.)

- A. JA: テスト規約をルートのCLAUDE.mdに移す。
  - KO: 테스트 규약을 루트 CLAUDE.md로 옮깁니다.
  - EN: Move the test conventions into the root CLAUDE.md.
- B. JA: テスト規約を.claude/commands/配下のプロジェクトスラッシュコマンドにまとめ、開発者にテスト編集前に実行してもらう。
  - KO: 테스트 규약을 .claude/commands/ 아래의 프로젝트 slash command로 모으고, 개발자가 테스트를 편집하기 전에 실행하게 합니다.
  - EN: Consolidate the test conventions into a project slash command under .claude/commands/, and have developers run it before editing tests.
- C. JA: pathsのglobパターンでテストファイルを指定した.claude/rules/testing.mdを作成し、共有のテスト規約をそこに一元化する。
  - KO: paths의 glob 패턴으로 테스트 파일을 지정한 .claude/rules/testing.md를 만들고, 공통 테스트 규약을 그곳에 한데 모읍니다.
  - EN: Create .claude/rules/testing.md that specifies test files with a paths glob pattern, and centralize the shared test conventions there.
- D. JA: ディレクトリ単位のメモリファイルに複製されたテスト規約を削除し、共有規約の置き場を1か所に統一する。
  - KO: 디렉터리 단위 memory 파일에 복제된 테스트 규약을 삭제하고, 공통 규약을 두는 곳을 한 군데로 통일합니다.
  - EN: Delete the test conventions duplicated in the directory-level memory files, and unify the location of the shared conventions into one place.

## CCAR-F-Udemy02-0041

**JA** 地域ニュース配信サービスを運営する企業の開発チームは、Claude Agent SDKを使用してマルチエージェントリサーチシステムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

このチームは、literature-gap-auditという名前のClaude Codeスキルを作成しました。そのSKILL.mdでは、誰かがコーディネーターを編集する前に、次の作業をするようClaudeに指示しています。

リポジトリ内のプロンプトを検索する

レポートテンプレートを調査する

不足している出典検証の観点をブレインストーミングする

開発者がこのスキルを呼び出すと、大量のファイル検索メモや、検討の末に却下した代替案がメインセッションに残り続けます。その結果、その後のレポート生成の編集作業で焦点がぼやけてしまいます。

このスキルの設定で変更すべきことはどれですか。

**KO** 지역 뉴스 배포 서비스를 운영하는 기업의 개발팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 웹 검색용, 문서 분석용, 조사 결과 통합용, 보고서 생성용이 있습니다. 이 시스템은 주제를 조사해 출처를 명시한 종합 보고서를 작성합니다.

이 팀은 literature-gap-audit라는 이름의 Claude Code skill을 만들었습니다. 그 SKILL.md는 누군가 coordinator를 편집하기 전에 다음 작업을 하도록 Claude에게 지시합니다.

저장소 안의 prompt를 검색합니다

보고서 템플릿을 조사합니다

부족한 출처 검증 관점을 브레인스토밍합니다

개발자가 이 skill을 호출하면, 대량의 파일 검색 메모와 검토 끝에 기각한 대안들이 메인 session에 계속 남습니다. 그 결과 이후의 보고서 생성 편집 작업에서 초점이 흐려집니다.

이 skill의 설정에서 무엇을 변경해야 합니까?

- A. JA: 監査のために/forkを呼び出し、現在の会話全体の履歴を引き継がせる。
  - KO: 감사를 위해 /fork를 호출해, 현재 대화 전체의 기록을 이어받게 합니다.
  - EN: Invoke /fork for the audit so that the entire current conversation history is carried over.
- B. JA: 監査の指示をCLAUDE.mdに移し、監査が終わった後に/compactを実行する。
  - KO: 감사 지시를 CLAUDE.md로 옮기고, 감사가 끝난 뒤 /compact를 실행합니다.
  - EN: Move the audit instructions into CLAUDE.md, and run /compact after the audit finishes.
- C. JA: disable-model-invocation: trueを設定し、開発者が「/名前」で明示的に呼び出す形にする。
  - KO: disable-model-invocation: true를 설정해, 개발자가 "/이름"으로 명시적으로 호출하는 방식으로 바꿉니다.
  - EN: Set disable-model-invocation: true so that developers invoke it explicitly with "/name".
- D. JA: SKILL.mdにcontext: forkを追加し、監査自体は明示的なタスク指示として維持する。
  - KO: SKILL.md에 context: fork를 추가하고, 감사 자체는 명시적인 작업 지시로 유지합니다.
  - EN: Add context: fork to SKILL.md, and keep the audit itself as an explicit task instruction.

## CCAR-F-Udemy02-0042

**JA** あるゲームスタジオの社内ツールチームは、Claude Codeを使って、コード生成、リファクタリング、デバッグ、ドキュメント作成の作業を加速しています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行をどのように使い分けるかを理解する必要があります。

カスタムのparallel-reviewコマンドは、v2.1.63より前のClaude Code設定に固定されたリポジトリでSDKの実行を開始し、Taskツールでサブエージェントに作業を委任します。この実行は、複数の専門レビュー用サブエージェントにファンアウトする想定です。

現在のSDKオプションで自動承認されているのはRead・Grep・Globだけで、各実行は、最初にサブエージェントへの委任を試みた時点で、対話的な権限確認プロンプトによって止まってしまいます。

このチームが変更すべきことはどれですか。（2つ選択してください。）

**KO** 한 게임 스튜디오의 사내 도구팀은 Claude Code로 코드 생성, refactoring, 디버깅, 문서 작성 작업의 속도를 높이고 있습니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하고, plan mode와 직접 실행을 어떻게 나눠 쓸지 이해해야 합니다.

custom parallel-review 명령은 v2.1.63 이전의 Claude Code 설정에 고정된 저장소에서 SDK 실행을 시작하고, Task 도구로 subagent에게 작업을 위임합니다. 이 실행은 여러 전문 리뷰용 subagent로 fan-out하는 것을 전제로 합니다.

현재 SDK 옵션에서 자동 승인되는 것은 Read·Grep·Glob뿐이어서, 각 실행은 처음으로 subagent에게 위임을 시도하는 시점에 대화형 권한 확인 prompt 때문에 멈춰 버립니다.

이 팀이 변경해야 할 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: permissionModeをacceptEditsにして、編集系ツールの確認を省く。
  - KO: permissionMode를 acceptEdits로 설정해, 편집 계열 도구의 확인을 생략합니다.
  - EN: Set permissionMode to acceptEdits to skip confirmation for editing tools.
- B. JA: 入れ子の委任のためにワーカー側のサブエージェントのtoolsにAgentを加え、コーディネーターの設定は変えない。
  - KO: 중첩 위임을 위해 워커 쪽 subagent의 tools에 Agent를 추가하고, coordinator의 설정은 바꾸지 않습니다.
  - EN: Add Agent to the worker-side subagents' tools for nested delegation, without changing the coordinator's configuration.
- C. JA: SDKの実行に権限判定のコールバックを与え、Taskによる委任呼び出しをプログラム的に承認する。
  - KO: SDK 실행에 권한 판정 callback을 제공해, Task를 통한 위임 호출을 프로그램으로 승인합니다.
  - EN: Provide the SDK run with a permission-decision callback that programmatically approves Task delegation calls.
- D. JA: コーディネーターを実行するSDKのallowedTools（またはallowed_tools）リストにTaskを追加する。
  - KO: coordinator를 실행하는 SDK의 allowedTools(또는 allowed_tools) 목록에 Task를 추가합니다.
  - EN: Add Task to the allowedTools (or allowed_tools) list of the SDK that runs the coordinator.

## CCAR-F-Udemy02-0043

**JA** フィンテック企業のプラットフォームチームは、Claude Codeを使ってソフトウェア開発を加速しています。ある開発者が、プランモードで長時間調査したあと、変更を加える前にセッションIDを保存しました。

開発者は、この分析済みのコンテキストから、次の2つの異なる試みを検証したいと考えています。

最小限のパッチ案

より大掛かりなリファクタリング案

ただし、どちらの試みも、同じ作業ディレクトリ内の重複するファイルを変更します。

会話履歴とファイルの状態を混同せずに、それぞれの試みを独立して検証するのに最も適した方法はどれですか。（2つ選択してください。）

**KO** 핀테크 기업의 플랫폼팀은 Claude Code로 소프트웨어 개발 속도를 높이고 있습니다. 한 개발자가 plan mode에서 오랫동안 조사한 뒤, 변경을 가하기 전에 session ID를 저장했습니다.

개발자는 이미 분석을 마친 이 context에서 출발해, 다음 두 가지 서로 다른 시도를 검증하려고 합니다.

최소한의 패치안

더 대규모의 refactoring안

다만 두 시도 모두 같은 작업 디렉터리 안의 겹치는 파일을 변경합니다.

대화 기록과 파일 상태를 섞지 않고 각 시도를 독립적으로 검증하는 데 가장 적합한 방법은 무엇입니까? (2개를 고르십시오.)

- A. JA: 同じプロジェクトディレクトリからcontinueを2回実行し、どちらの試みを基準にするかはClaude Codeに自動で選ばせる。
  - KO: 같은 프로젝트 디렉터리에서 continue를 두 번 실행하고, 어느 시도를 기준으로 삼을지는 Claude Code가 자동으로 고르게 합니다.
  - EN: Run continue twice from the same project directory, and let Claude Code automatically choose which attempt to base each on.
- B. JA: 保存したセッションIDをforkせずに2回resumeし、Claudeに各試みを分けて扱うよう依頼する。
  - KO: 저장한 session ID를 fork하지 않고 두 번 resume하고, Claude에게 각 시도를 따로 다루도록 요청합니다.
  - EN: Resume the saved session ID twice without forking, and ask Claude to treat each attempt separately.
- C. JA: 保存したセッションIDを試みごとにforkオプション付きでresumeし、チェックポイントから巻き戻せるようにしておく。
  - KO: 저장한 session ID를 시도마다 fork 옵션을 붙여 resume하고, checkpoint에서 되돌릴 수 있게 해 둡니다.
  - EN: Resume the saved session ID with the fork option for each attempt, and keep checkpoints available so that you can rewind.
- D. JA: 各試みをリポジトリの別々の作業コピーで実行し、重複するファイルへの編集が互いに混ざらないようにする。
  - KO: 각 시도를 저장소의 별도 작업 사본에서 실행해, 겹치는 파일에 대한 편집이 서로 섞이지 않게 합니다.
  - EN: Run each attempt in a separate working copy of the repository so that edits to overlapping files do not get mixed together.

## CCAR-F-Udemy02-0044

**JA** 研究用機器を製造するバイオテック企業が、開発ワークフローを加速するためにClaude Codeを使っています。チームでは、コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使い、カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合しています。プランモードと直接実行をどのように使い分けるかも理解する必要があります。

このチームは、作業指示書から、機器の校正レポートと安全適合ラベルをClaude Codeに生成させています。公開前にレビュアーが確認できるのは、生成されたフィールドのごく一部だけです。

パイロット運用の結果、フィールドによって精度が大きく異なることが分かっています。

機器モデル名は、概ね正しい

危険物分類は、しばしば誤っている

人によるレビューを、最も効果の大きい項目に振り分けるために、最も適切な変更はどれですか。

**KO** 연구용 장비를 제조하는 바이오테크 기업이 개발 workflow 속도를 높이기 위해 Claude Code를 사용하고 있습니다. 팀은 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 사용하며, custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하고 있습니다. plan mode와 직접 실행을 어떻게 나눠 쓸지도 이해해야 합니다.

이 팀은 작업 지시서를 바탕으로 장비 교정 보고서와 안전 적합 라벨을 Claude Code가 생성하게 하고 있습니다. 게시 전에 리뷰어가 확인할 수 있는 것은 생성된 필드의 극히 일부뿐입니다.

파일럿 운영 결과, 필드에 따라 정확도가 크게 다르다는 것이 밝혀졌습니다.

장비 모델명은 대체로 정확합니다

위험물 분류는 자주 틀립니다

사람의 리뷰를 효과가 가장 큰 항목에 배분하려면, 어떤 변경이 가장 적절합니까?

- A. JA: パイロット運用から得た全体の精度を使い、それが目標を上回ったらレビュー量を減らし、残りの出力は一様にサンプリングしてレビューする。
  - KO: 파일럿 운영에서 얻은 전체 정확도를 사용해, 그것이 목표를 넘으면 리뷰량을 줄이고 나머지 출력은 균일하게 샘플링해 리뷰합니다.
  - EN: Use the overall accuracy from the pilot, reduce review volume once it exceeds the target, and review a uniform sample of the remaining outputs.
- B. JA: 構造化出力にフィールドごとの確信度を出させ、ラベル付き事例でしきい値をキャリブレーションし、低確信度のフィールドをレビューへ回す。
  - KO: 구조화 출력에 필드별 확신도를 내게 하고, 라벨이 붙은 사례로 임곗값을 보정(calibration)한 뒤, 확신도가 낮은 필드를 리뷰로 보냅니다.
  - EN: Have the structured output provide a per-field confidence, calibrate thresholds using labeled examples, and route low-confidence fields to review.
- C. JA: 文書単位で1つの確信度スコアを算出し、しきい値を下回った文書だけをレビューし、承認された文書はすべてのフィールドをそのまま公開する。
  - KO: 문서 단위로 확신도 점수를 하나 계산해 임곗값보다 낮은 문서만 리뷰하고, 승인된 문서는 모든 필드를 그대로 게시합니다.
  - EN: Compute a single confidence score per document, review only the documents that fall below the threshold, and publish all fields of approved documents as is.
- D. JA: 処理が正常終了したことを高信頼の指標とみなしてそれらの出力のレビューを省略し、途中で打ち切られた応答だけをレビューする。
  - KO: 처리가 정상 종료된 것을 높은 신뢰도의 지표로 보고 그런 출력의 리뷰는 생략하며, 도중에 잘린 응답만 리뷰합니다.
  - EN: Treat normal completion of processing as a high-reliability indicator and skip review of those outputs, reviewing only responses that were cut off midway.

## CCAR-F-Udemy02-0045

**JA** あなたは、Claude Agent SDKを使用してマルチエージェントリサーチシステムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

このシステムが、「製造業におけるAI在庫管理導入について、出典付きの包括的なレポートを作成してほしい」という広い依頼を受け取りました。コーディネーターは、実際の調査を各サブエージェントに委任する前に、どう着手するかを決める必要があります。

過去の実行では、文章としてはよく書けたレポートが得られたものの、カバー範囲にムラがあり、本筋から外れた細部の調査に労力を費やしていました。

この種のタスクに最も効果的に対処できるコーディネーターの戦略はどれですか。（2つ選択してください。）

**KO** 당신은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 웹 검색용, 문서 분석용, 조사 결과 통합용, 보고서 생성용이 있습니다. 이 시스템은 주제를 조사해 출처를 명시한 종합 보고서를 작성합니다.

이 시스템이 "제조업의 AI 재고 관리 도입에 대해 출처를 포함한 종합 보고서를 작성해 달라"는 범위가 넓은 요청을 받았습니다. coordinator는 실제 조사를 각 subagent에게 위임하기 전에 어떻게 착수할지 정해야 합니다.

과거 실행에서는 글 자체는 잘 쓰인 보고서가 나왔지만, 커버리지가 고르지 않았고 본론에서 벗어난 세부 사항을 조사하는 데 노력을 쏟았습니다.

이런 종류의 작업에 가장 효과적으로 대처할 수 있는 coordinator 전략은 무엇입니까? (2개를 고르십시오.)

- A. JA: 最初に探索的な調査でトピックの構造と重要領域をつかみ、判明した依存関係に応じてサブタスクを組み替える。
  - KO: 먼저 탐색적 조사로 주제의 구조와 중요 영역을 파악하고, 드러난 의존 관계에 따라 하위 작업을 재구성합니다.
  - EN: Start with an exploratory investigation to grasp the structure of the topic and its key areas, then reorganize the subtasks according to the dependencies that are discovered.
- B. JA: 検索からレポート作成までの固定パイプラインで開始し、最初の割り当て後は調査範囲を変更しない。
  - KO: 검색부터 보고서 작성까지 이어지는 고정 pipeline으로 시작하고, 첫 할당 이후에는 조사 범위를 바꾸지 않습니다.
  - EN: Start with a fixed pipeline from search to report generation, and do not change the research scope after the initial assignment.
- C. JA: レポートの目次は調査結果に応じて後から確定し、優先度の高い知見から各セクションを埋める。
  - KO: 보고서 목차는 조사 결과에 따라 나중에 확정하고, 우선순위가 높은 발견 내용부터 각 섹션을 채웁니다.
  - EN: Finalize the report's table of contents later, based on the research findings, and fill in each section starting with the highest-priority findings.
- D. JA: 最も目立つキーワードごとの並行調査を最初に割り当て、完了した知見を統合サブエージェントにまとめさせる。
  - KO: 가장 눈에 띄는 키워드별 병렬 조사를 먼저 할당하고, 완료된 발견 내용을 통합 subagent가 정리하게 합니다.
  - EN: Initially assign parallel research for each of the most prominent keywords, and have the synthesis subagent consolidate the findings once they are complete.

## CCAR-F-Udemy02-0046

**JA** ある物流企業のプラットフォームチームは、インシデント管理システムを操作するMCPサーバーを、社内の開発者向けに提供しています。これまでは、各開発者が自分のマシンでサーバーのプロセスを起動し、Claude Codeからローカルに接続していました。

今回、このサーバーを社内クラウドに移し、全員が同じURLに接続する形に切り替えます。新しいサーバーの条件は次のとおりです。

Claudeからの要求に応答するだけで、イベントを自発的に送ることはない

利用者には、ブラウザでのOAuth 2.0ログインを求める

移行期間中は、古いクライアント向けにSSEのエンドポイントも併せて公開する

各開発者がClaude Codeにこのサーバーを追加する方法として、最も適切なものはどれですか。

**KO** 한 물류 기업의 플랫폼팀은 인시던트 관리 시스템을 조작하는 MCP server를 사내 개발자에게 제공하고 있습니다. 지금까지는 각 개발자가 자기 머신에서 서버 프로세스를 띄우고, Claude Code에서 로컬로 연결했습니다.

이번에 이 서버를 사내 클라우드로 옮겨, 모두가 같은 URL에 연결하는 방식으로 바꿉니다. 새 서버의 조건은 다음과 같습니다.

Claude의 요청에 응답만 하며, 이벤트를 스스로 보내지는 않습니다

사용자에게 브라우저를 통한 OAuth 2.0 로그인을 요구합니다

전환 기간 동안에는 오래된 클라이언트를 위해 SSE endpoint도 함께 공개합니다

각 개발자가 Claude Code에 이 서버를 추가하는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: claude mcp add --transport httpでサーバーのURLを追加し、/mcpからブラウザで認証する。
  - KO: claude mcp add --transport http로 서버 URL을 추가하고, /mcp에서 브라우저로 인증합니다.
  - EN: Add the server's URL with claude mcp add --transport http, and authenticate in the browser from /mcp.
- B. JA: サーバーのパッケージを各自で取得し、claude mcp add --transport stdioでローカルに追加する。
  - KO: 서버 패키지를 각자 받아서, claude mcp add --transport stdio로 로컬에 추가합니다.
  - EN: Have each developer obtain the server's package and add it locally with claude mcp add --transport stdio.
- C. JA: claude mcp add --transport sseでSSEのエンドポイントを追加し、/mcpからブラウザで認証する。
  - KO: claude mcp add --transport sse로 SSE endpoint를 추가하고, /mcp에서 브라우저로 인증합니다.
  - EN: Add the SSE endpoint with claude mcp add --transport sse, and authenticate in the browser from /mcp.
- D. JA: .mcp.jsonにtype: "ws"でサーバーのURLを書き、Authorizationヘッダーにトークンを設定する。
  - KO: .mcp.json에 type: "ws"로 서버 URL을 적고, Authorization 헤더에 토큰을 설정합니다.
  - EN: Write the server's URL in .mcp.json with type: "ws", and set a token in the Authorization header.

## CCAR-F-Udemy02-0047

**JA** オンライン教育プラットフォームを運営する企業では、Claude CodeをCI/CDパイプラインに統合しています。このシステムは、自動コードレビューを実行し、テストケースを生成し、プルリクエストにフィードバックを返します。具体的で実行可能なフィードバックを返し、誤検知を最小限に抑えるプロンプトを設計する必要があります。

プルリクエストのレビューで誤検知が発生しています。原因は、データベースマイグレーション固有のレビュー基準が、フロントエンドやドキュメントの変更にまで適用されていることです。マイグレーションファイルは、services・apps・共有ライブラリなど、複数のパッケージの配下に置かれる可能性があります。

Claudeが関連するファイルを読み取ったときにだけこれらの規約を読み込ませるために、このチームが行うべき変更はどれですか。

**KO** 온라인 교육 플랫폼을 운영하는 기업에서는 Claude Code를 CI/CD pipeline에 통합하고 있습니다. 이 시스템은 자동 코드 리뷰를 실행하고, 테스트 케이스를 생성하며, pull request에 피드백을 돌려줍니다. 구체적이고 실행 가능한 피드백을 돌려주면서 오탐을 최소화하는 prompt를 설계해야 합니다.

pull request 리뷰에서 오탐이 발생하고 있습니다. 원인은 데이터베이스 마이그레이션 고유의 리뷰 기준이 프런트엔드나 문서 변경에까지 적용되고 있다는 점입니다. 마이그레이션 파일은 services·apps·공유 라이브러리 등 여러 패키지 아래에 놓일 수 있습니다.

Claude가 관련 파일을 읽을 때만 이 규약을 불러오게 하려면, 이 팀은 무엇을 변경해야 합니까?

- A. JA: マイグレーションのチェックリストをルートのCLAUDE.mdに移し、関連ファイルにだけ適用するよう指示する。
  - KO: 마이그레이션 체크리스트를 루트 CLAUDE.md로 옮기고, 관련 파일에만 적용하라고 지시합니다.
  - EN: Move the migration checklist to the root CLAUDE.md and instruct Claude to apply it only to relevant files.
- B. JA: pathsにマイグレーションのglobパターンを書いた.claude/rules/database-migrations.mdに基準を置く。
  - KO: paths에 마이그레이션 glob 패턴을 적은 .claude/rules/database-migrations.md에 기준을 둡니다.
  - EN: Put the criteria in .claude/rules/database-migrations.md, with the migration glob patterns in paths.
- C. JA: マイグレーション用のglobパターンを書いた~/.claude/rules/database-migrations.mdを各レビュアーに入れてもらう。
  - KO: 마이그레이션용 glob 패턴을 적은 ~/.claude/rules/database-migrations.md를 각 리뷰어가 설치하게 합니다.
  - EN: Have each reviewer install a ~/.claude/rules/database-migrations.md that contains the migration glob patterns.
- D. JA: フロントマターなしの.claude/rules/database-migrations.mdを作り、ファイル名で対象を絞らせる。
  - KO: frontmatter 없는 .claude/rules/database-migrations.md를 만들고, 파일 이름으로 대상을 좁히게 합니다.
  - EN: Create a .claude/rules/database-migrations.md without frontmatter and let the file name narrow the scope.

## CCAR-F-Udemy02-0048

**JA** オンライン薬局サービスを運営する企業は、Claude Codeをコードレビュー自動化パイプラインに統合しています。このシステムは、プルリクエストごとに自動レビューを実行し、テストケースを生成し、具体的で実行可能なフィードバックを返します。誤検知を最小限に抑えるプロンプトを設計する必要があります。

このシステムは、プルリクエストのレビュー、テストの生成、PRメタデータの更新のすべてを、1回のMessages API呼び出しでまとめて処理しています。ログを見ると、次の問題が起きています。

レビュー段階で、テストできないスタイルのコメントに対しても、テスト作成用ツールが呼び出されることがある

パイプラインが期待する構造化された指摘オブジェクトではなく、ただの文章が返されることがある

パイプラインのほかの箇所での自動テスト生成は維持しつつ、ツール選択の信頼性を最も改善できる変更はどれですか。（2つ選択してください。）

**KO** 온라인 약국 서비스를 운영하는 기업은 Claude Code를 코드 리뷰 자동화 pipeline에 통합하고 있습니다. 이 시스템은 pull request마다 자동 리뷰를 실행하고, 테스트 케이스를 생성하며, 구체적이고 실행 가능한 피드백을 돌려줍니다. 오탐을 최소화하는 prompt를 설계해야 합니다.

이 시스템은 pull request 리뷰, 테스트 생성, PR metadata 갱신을 모두 한 번의 Messages API 호출로 묶어 처리하고 있습니다. 로그를 보면 다음 문제가 일어나고 있습니다.

리뷰 단계에서, 테스트할 수 없는 스타일 관련 댓글에 대해서도 테스트 작성용 도구가 호출되는 경우가 있습니다

pipeline이 기대하는 구조화된 지적 객체 대신 그냥 텍스트가 반환되는 경우가 있습니다

pipeline의 다른 곳에서 이루어지는 자동 테스트 생성은 유지하면서, 도구 선택의 신뢰성을 가장 크게 개선할 수 있는 변경은 무엇입니까? (2개를 고르십시오.)

- A. JA: レビューとテスト生成のステップを分離し、それぞれの役割に必要なツールだけを公開し、レビューステップではtool_choiceでレポート用ツールの使用を強制する。
  - KO: 리뷰 단계와 테스트 생성 단계를 분리해 각 역할에 필요한 도구만 공개하고, 리뷰 단계에서는 tool_choice로 보고용 도구 사용을 강제합니다.
  - EN: Separate the review and test-generation steps, expose only the tools each role needs, and use tool_choice to force the use of the reporting tool in the review step.
- B. JA: 各ツールの説明文を、レビュー段階で使う場面と使わない場面の境界が分かる形に書き直す。
  - KO: 각 도구의 설명을, 리뷰 단계에서 쓰는 경우와 쓰지 않는 경우의 경계가 드러나도록 고쳐 씁니다.
  - EN: Rewrite each tool's description so that the boundary between when to use it and when not to use it during the review stage is clear.
- C. JA: 共有の1つのCIステップを維持し、ツール名をカテゴリごとに名前空間で分け、tool_choiceはautoのままモデルの柔軟性に任せる。
  - KO: 공유하는 CI 단계 하나를 유지하고, 도구 이름을 카테고리별 namespace로 나누며, tool_choice는 auto로 둔 채 모델의 유연성에 맡깁니다.
  - EN: Keep a single shared CI step, namespace the tool names by category, and leave tool_choice as auto to rely on the model's flexibility.
- D. JA: 両方のステップにすべてのCIツールを公開し、レビュー中はtool_choiceをnoneに設定し、アシスタントのテキストからJSONを解析する。
  - KO: 두 단계 모두에 모든 CI 도구를 공개하고, 리뷰 중에는 tool_choice를 none으로 설정해 assistant 텍스트에서 JSON을 파싱합니다.
  - EN: Expose all CI tools in both steps, set tool_choice to none during the review, and parse JSON from the assistant's text.

## CCAR-F-Udemy02-0049

**JA** あなたは、Claude Codeを使ってソフトウェア開発を加速しています。チームでは、コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行をどのように使い分けるかを理解する必要があります。

このチームは、日常の開発タスクのために、Claude CodeをServiceNowのチケットと連携させたいと考えています。さらに、チケットのフィールドに社内限定のサービス所有権ルールと内部デプロイチェックを組み合わせた、リリース判定のワークフローも必要です。

再利用性、保守性、チーム固有の挙動を最もよく両立できる統合方法はどれですか。

**KO** 당신은 Claude Code로 소프트웨어 개발 속도를 높이고 있습니다. 팀은 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 사용합니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하고, plan mode와 직접 실행을 어떻게 나눠 쓸지 이해해야 합니다.

이 팀은 일상적인 개발 작업을 위해 Claude Code를 ServiceNow 티켓과 연동하려고 합니다. 또한 티켓 필드에 사내 전용 서비스 소유권 규칙과 내부 배포 점검을 조합한, 릴리스 판정 workflow도 필요합니다.

재사용성, 유지보수성, 팀 고유의 동작을 가장 잘 양립시킬 수 있는 통합 방법은 무엇입니까?

- A. JA: ServiceNowの各操作ごとにプロジェクトスラッシュコマンドを作成し、どのAPI呼び出しを選ぶかはClaude Codeのプロンプトに任せる。
  - KO: ServiceNow 작업마다 프로젝트 slash command를 만들고, 어떤 API 호출을 고를지는 Claude Code의 prompt에 맡깁니다.
  - EN: Create a project slash command for each ServiceNow operation, and leave it to Claude Code's prompt to choose which API call to make.
- B. JA: ServiceNow操作を再実装し、リリース判定ワークフローも処理する1つのカスタムMCPサーバーを構築する。
  - KO: ServiceNow 작업을 다시 구현하고, 릴리스 판정 workflow까지 처리하는 custom MCP server 하나를 구축합니다.
  - EN: Build a single custom MCP server that reimplements the ServiceNow operations and also handles the release-decision workflow.
- C. JA: ServiceNow操作用にメンテナンスされた既存のMCPサーバーを設定し、リリース判定ワークフロー用にはカスタムMCPサーバーを実装する。
  - KO: ServiceNow 작업에는 유지보수되고 있는 기존 MCP server를 설정하고, 릴리스 판정 workflow용으로는 custom MCP server를 구현합니다.
  - EN: Configure an existing, maintained MCP server for the ServiceNow operations, and implement a custom MCP server for the release-decision workflow.
- D. JA: ServiceNowのREST手順をCLAUDE.mdに保存し、Bashを呼び出すスラッシュコマンドでチケット更新を行う。
  - KO: ServiceNow REST 절차를 CLAUDE.md에 저장하고, Bash를 호출하는 slash command로 티켓을 갱신합니다.
  - EN: Store the ServiceNow REST procedures in CLAUDE.md, and update tickets with slash commands that call Bash.

## CCAR-F-Udemy02-0050

**JA** あるゲームスタジオのライブ運用チームは、Claude Codeを使ってソフトウェア開発を加速しています。コード生成、リファクタリング、デバッグ、ドキュメント作成に活用し、カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合しています。プランモードと直接実行をどのように使い分けるかも理解する必要があります。

このチームの/release-noteワークフローは、生のコミットメッセージを顧客向けの変更履歴エントリに書き換えます。レビュー担当者は、変換結果に次のような一貫性のなさがあることに気づきました。

社内チケットIDがそのまま残ることがある

破壊的変更が、あいまいな表現に和らげられることがある

簡潔なバグ修正コミットが、根拠のない詳細情報で水増しされることがある

このワークフローの一貫性を最も直接的に改善できる変更はどれですか。

**KO** 한 게임 스튜디오의 라이브 운영팀은 Claude Code로 소프트웨어 개발 속도를 높이고 있습니다. 코드 생성, refactoring, 디버깅, 문서 작성에 활용하며, custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하고 있습니다. plan mode와 직접 실행을 어떻게 나눠 쓸지도 이해해야 합니다.

이 팀의 /release-note workflow는 원본 commit 메시지를 고객용 변경 이력 항목으로 고쳐 씁니다. 리뷰 담당자는 변환 결과에 다음과 같은 일관성 없는 부분이 있다는 것을 알아챘습니다.

사내 티켓 ID가 그대로 남는 경우가 있습니다

호환성을 깨는 변경(breaking change)이 모호한 표현으로 누그러지는 경우가 있습니다

간결한 버그 수정 commit이 근거 없는 세부 정보로 부풀려지는 경우가 있습니다

이 workflow의 일관성을 가장 직접적으로 개선할 수 있는 변경은 무엇입니까?

- A. JA: release-note用の指示をプロジェクト設定に移し、チーム共有の設定でワークフローを実行する。
  - KO: release-note용 지시를 프로젝트 설정으로 옮기고, 팀 공유 설정으로 workflow를 실행합니다.
  - EN: Move the release-note instructions into the project settings and run the workflow with the team-shared settings.
- B. JA: 社内チケットIDを含む変更履歴の書き込みをブロックするPreToolUseフックを追加する。
  - KO: 사내 티켓 ID가 포함된 변경 이력 쓰기를 차단하는 PreToolUse hook을 추가합니다.
  - EN: Add a PreToolUse hook that blocks changelog writes containing internal ticket IDs.
- C. JA: プランモードでワークフローを実行し、Claudeに編集前の段階で作成方針を提示させる。
  - KO: plan mode로 workflow를 실행해, Claude가 편집 전 단계에서 작성 방침을 제시하게 합니다.
  - EN: Run the workflow in plan mode and have Claude present its writing approach before editing.
- D. JA: エッジケースを含む変換前後の代表例を3つ、タグで区切った例示セクションに追加する。
  - KO: edge case를 포함한 변환 전후의 대표 예시 3개를, 태그로 구분한 예시 섹션에 추가합니다.
  - EN: Add three representative before-and-after examples, including edge cases, to an examples section delimited by tags.

## CCAR-F-Udemy02-0051

**JA** ある物流会社では、輸送書類（船荷証券・通関申告書）を自動レビューするAIエージェントを、文書処理パイプラインに統合しています。このシステムは書類の自動レビューを実行し、修正指摘のフィードバックを担当者に返します。フィードバックは実用的で、誤検知を最小限に抑える必要があります。

長い輸送書類ほど、レビューステップがコンテキスト上限に近づく問題が起きています。トレースを確認すると、書類解析ツールを呼び出すたびに、大きなtool_resultペイロードが追加されていました。ペイロードには次の情報が含まれますが、実際のレビューで使うのはその一部のフィールドだけです。

書類メタデータ全体

関係者データ

全文の通関履歴

依存関係の詳細

この信頼性の問題に最も適切に対応できる変更はどれですか。

**KO** 한 물류 회사에서는 운송 서류(선하증권·통관 신고서)를 자동으로 리뷰하는 AI agent를 문서 처리 pipeline에 통합하고 있습니다. 이 시스템은 서류 자동 리뷰를 실행하고, 수정할 점에 대한 피드백을 담당자에게 돌려줍니다. 피드백은 실용적이어야 하며, 오탐을 최소화해야 합니다.

운송 서류가 길수록 리뷰 단계가 context 한도에 가까워지는 문제가 생기고 있습니다. trace를 확인해 보니, 서류 분석 도구를 호출할 때마다 큰 tool_result payload가 추가되고 있었습니다. payload에는 다음 정보가 들어 있지만, 실제 리뷰에 쓰이는 것은 그중 일부 필드뿐입니다.

서류 metadata 전체

관계자 데이터

전체 통관 이력

의존 관계 세부 정보

이 신뢰성 문제에 가장 적절하게 대응할 수 있는 변경은 무엇입니까?

- A. JA: コンテキストエディット機能を有効にし、設定したしきい値をリクエストが超えた時点で古いツール結果をクリアする。
  - KO: context editing 기능을 켜고, 요청이 설정한 임곗값을 넘으면 오래된 도구 결과를 지웁니다.
  - EN: Enable the context editing feature and clear old tool results once a request exceeds a configured threshold.
- B. JA: ツールラッパーを変更し、必要なフィールドだけを含むレビュー用のコンパクトなtool_resultペイロードを返すようにする。
  - KO: 도구 wrapper를 바꿔, 필요한 필드만 담은 리뷰용 간결한 tool_result payload를 반환하게 합니다.
  - EN: Change the tool wrapper so that it returns a compact tool_result payload for review that contains only the required fields.
- C. JA: ツール定義と繰り返し登場するレビュー用プレフィックスにプロンプトキャッシュを適用し、コンテキストウィンドウの圧迫を軽減する。
  - KO: 도구 정의와 반복되는 리뷰용 prefix에 prompt caching을 적용해, context window의 부담을 줄입니다.
  - EN: Apply prompt caching to the tool definitions and the repeated review prefix to reduce pressure on the context window.
- D. JA: レビュー応答のmax_tokensを増やし、無関係なtool_resultフィールドを無視するようClaudeに指示する。
  - KO: 리뷰 응답의 max_tokens를 늘리고, 관련 없는 tool_result 필드는 무시하라고 Claude에게 지시합니다.
  - EN: Increase max_tokens for the review response and instruct Claude to ignore the irrelevant tool_result fields.

## CCAR-F-Udemy02-0052

**JA** あなたは、ソフトウェア開発チームで、Claude Codeを使ったドキュメント抽出ワークフローを運用しています。設計ドキュメントやプルリクエストの説明文を、JSON形式の作業アイテムに変換する抽出ジョブです。レビュアーが目視で確認できるのは、全体の約20％だけです。

現在のジョブは、stop_reason: end_turnを返したレスポンスを、そのままトラッカーに投入しています。抜き取り検査では、次の場合に不良な作業アイテムが発生していることが分かりました。

2つの参照元の文書の内容が食い違っている場合

ある項目が、文脈から弱く推測されている場合

このレビューワークフローを最も改善できる変更はどれですか。（2つ選択してください。）

**KO** 당신은 소프트웨어 개발팀에서 Claude Code를 이용한 문서 추출 workflow를 운영하고 있습니다. 설계 문서와 pull request 설명문을 JSON 형식의 작업 항목으로 변환하는 추출 job입니다. 리뷰어가 눈으로 확인할 수 있는 것은 전체의 약 20%뿐입니다.

현재 job은 stop_reason: end_turn을 반환한 응답을 그대로 tracker에 넣고 있습니다. 샘플 검사에서, 다음 경우에 불량 작업 항목이 생긴다는 것이 밝혀졌습니다.

두 참조 문서의 내용이 서로 어긋나는 경우

어떤 항목이 문맥에서 약하게 추론된 경우

이 리뷰 workflow를 가장 크게 개선할 수 있는 변경은 무엇입니까? (2개를 고르십시오.)

- A. JA: 2つの参照元ファイルの内容が食い違っている作業アイテムにフラグを立てる、参照元間の整合性チェックを追加する。
  - KO: 두 참조 파일의 내용이 어긋나는 작업 항목에 플래그를 다는, 참조 문서 간 정합성 검사를 추가합니다.
  - EN: Add a cross-source consistency check that flags work items whose two source files conflict.
- B. JA: JSONスキーマにフィールドごとの確信度・あいまいさ・矛盾・根拠抜粋のフィールドを追加し、フラグが立ったレコードをクリーンなレコードより先にレビュアーへキューイングする。
  - KO: JSON schema에 필드별 확신도·모호성·모순·근거 발췌 필드를 추가하고, 플래그가 달린 레코드를 깨끗한 레코드보다 먼저 리뷰어 큐에 넣습니다.
  - EN: Add per-field confidence, ambiguity, contradiction, and evidence-excerpt fields to the JSON schema, and queue flagged records to reviewers ahead of clean records.
- C. JA: OpenAI SDK層を経由してlogprobsとtop_logprobsを要求し、低確率のレコードを整形済みレコードより先にレビュアーへキューイングする。
  - KO: OpenAI SDK 계층을 거쳐 logprobs와 top_logprobs를 요청하고, 확률이 낮은 레코드를 형식이 올바른 레코드보다 먼저 리뷰어 큐에 넣습니다.
  - EN: Request logprobs and top_logprobs through the OpenAI SDK layer, and queue low-probability records to reviewers ahead of well-formed records.
- D. JA: ソース文書に対してcitations機能を有効にしてJSONスキーマ出力と併用し、citationブロックが欠落しているレコードを他のレコードより先にレビュアーへキューイングする。
  - KO: 원본 문서에 citations 기능을 켜서 JSON schema 출력과 함께 쓰고, citation 블록이 빠진 레코드를 다른 레코드보다 먼저 리뷰어 큐에 넣습니다.
  - EN: Enable the citations feature on the source documents and use it together with JSON schema output, and queue records with missing citation blocks to reviewers ahead of other records.

## CCAR-F-Udemy02-0053

**JA** 製薬会社の規制情報チームは、Claude Agent SDKを使用してマルチエージェントリサーチシステムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

このチームは、引用検証用のテストをエージェントのコードのすぐそばに置いています。テストファイルは、packages/search/・packages/synthesis/・apps/reporting/の各配下にあります。チームの要望は次の2つです。

これらのテストファイルを編集するときは、常に同じテスト規約をClaude Codeに適用させる

関係のない本番用ファイルを編集するときは、その規約を読み込ませない

このチームが行うべきことはどれですか。

**KO** 제약회사의 규제 정보팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 웹 검색용, 문서 분석용, 조사 결과 통합용, 보고서 생성용이 있습니다. 이 시스템은 주제를 조사해 출처를 명시한 종합 보고서를 작성합니다.

이 팀은 인용 검증용 테스트를 agent 코드 바로 옆에 두고 있습니다. 테스트 파일은 packages/search/·packages/synthesis/·apps/reporting/ 각각의 아래에 있습니다. 팀의 요구 사항은 다음 두 가지입니다.

이 테스트 파일들을 편집할 때는 항상 같은 테스트 규약을 Claude Code가 적용해야 합니다

관련 없는 프로덕션 파일을 편집할 때는 그 규약을 불러오지 않아야 합니다

이 팀이 해야 할 일은 무엇입니까?

- A. JA: 各パッケージディレクトリにCLAUDE.mdを置き、同じテスト規約をそれぞれのファイルに複製して記載する。
  - KO: 각 패키지 디렉터리에 CLAUDE.md를 두고, 같은 테스트 규약을 각각의 파일에 복제해 적습니다.
  - EN: Place a CLAUDE.md in each package directory and duplicate the same testing conventions in each one.
- B. JA: 各開発者のユーザーレベルのCLAUDE.mdにテスト規約を追加し、編集時に読み込ませる。
  - KO: 각 개발자의 사용자 수준 CLAUDE.md에 테스트 규약을 추가해, 편집할 때 불러오게 합니다.
  - EN: Add the testing conventions to each developer's user-level CLAUDE.md so that they are loaded when editing.
- C. JA: テストファイルのglobパターンをpathsに書いたルールファイルを.claude/rules/に置く。
  - KO: 테스트 파일의 glob 패턴을 paths에 적은 rule 파일을 .claude/rules/에 둡니다.
  - EN: Place a rule file in .claude/rules/ with the test file glob patterns in paths.
- D. JA: テスト規約をルートのCLAUDE.mdの専用セクションに追加する。
  - KO: 테스트 규약을 루트 CLAUDE.md의 전용 섹션에 추가합니다.
  - EN: Add the testing conventions to a dedicated section of the root CLAUDE.md.

## CCAR-F-Udemy02-0054

**JA** あなたは、Claude Agent SDKを使用して保険金請求対応エージェントを構築しています。このエージェントは、支払い調整、補償範囲の照会、払戻し可否など、あいまいさの高い問い合わせを処理します。カスタムのMCPツール（get_policyholder、lookup_claim、issue_payout、escalate_to_adjuster）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を維持することです。

本番環境のログを確認したところ、請求内容が補償対象期間外の場合に、issue_payoutが「Payout blocked by policy」という内容を含む、一見成功したように見えるツール結果を返すことがあると分かりました。

Claudeはこの結果を受けて、状況を顧客に説明したり適切にエスカレーションしたりせずに、言い回しを少し変えただけの同じ支払いリクエストを繰り返し試みています。

エージェントのこの復旧時の挙動を最も改善できる変更はどれですか。

**KO** 당신은 Claude Agent SDK로 보험금 청구 대응 agent를 구축하고 있습니다. 이 agent는 지불 조정, 보장 범위 조회, 보험금 지급 가능 여부처럼 모호성이 높은 문의를 처리합니다. custom MCP 도구(get_policyholder, lookup_claim, issue_payout, escalate_to_adjuster)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation이 필요한 시점을 가려내면서 첫 응대 해결률 80% 이상을 유지하는 것입니다.

프로덕션 로그를 확인한 결과, 청구 내용이 보장 기간 밖일 때 issue_payout이 "Payout blocked by policy"라는 내용을 담은, 겉보기에는 성공한 것 같은 도구 결과를 반환하는 경우가 있었습니다.

Claude는 이 결과를 받고 나서 고객에게 상황을 설명하거나 적절히 escalation하지 않고, 표현만 조금 바꾼 같은 지불 요청을 반복해서 시도하고 있습니다.

agent의 이러한 복구 시 동작을 가장 크게 개선할 수 있는 변경은 무엇입니까?

- A. JA: CallToolResultにisError: trueを付け、リトライの可否をstructuredContentで示す。
  - KO: CallToolResult에 isError: true를 붙이고, 재시도 가능 여부를 structuredContent로 나타냅니다.
  - EN: Set isError: true on the CallToolResult and indicate whether a retry is possible in structuredContent.
- B. JA: 通常のCallToolResultを返し、contentに払戻しポリシーの詳しい説明と次に取れる対応の候補を書く。
  - KO: 일반 CallToolResult를 반환하고, content에 보험금 지급 정책에 대한 자세한 설명과 다음에 취할 수 있는 대응 후보를 적습니다.
  - EN: Return a normal CallToolResult, and write a detailed explanation of the payout policy and candidate next actions in content.
- C. JA: issue_payoutの説明文に、補償期間外の支払いを要求しないようClaudeへの警告を追記する。
  - KO: issue_payout의 설명에, 보장 기간 밖의 지불을 요청하지 말라는 Claude용 경고를 덧붙입니다.
  - EN: Add a warning to Claude in the issue_payout description not to request payouts outside the coverage period.
- D. JA: 業務ポリシーに違反する支払い要求には、tools/callからJSON-RPCのプロトコルエラーを返す。
  - KO: 업무 정책을 위반하는 지불 요청에는 tools/call에서 JSON-RPC protocol error를 반환합니다.
  - EN: For payout requests that violate business policy, return a JSON-RPC protocol error from tools/call.

## CCAR-F-Udemy02-0055

**JA** 音楽ストリーミングサービスを開発する企業は、Claude Codeをコードレビュー自動化パイプラインに統合しています。このシステムは、プルリクエストごとに自動レビューを実行し、テストケースを生成し、具体的で実行可能なフィードバックを返します。誤検知を最小限に抑えるプロンプトを設計する必要があります。

数週間運用したところ、開発者から自動レビューは「ノイズが多い」という声が上がっています。実例を見ると、次の2種類のコメントが混在しています。

変数名の付け方、好みのアサーションスタイル、テスト不足についてのコメント

null参照の実バグや認可バイパスといった、本物の問題についてのコメント

現在のプロンプトには、「高い確信を持てる問題のみを報告すること」とだけ書かれています。

レビューの有用性を最も直接的に改善できるプロンプトの変更はどれですか。（2つ選択してください。）

**KO** 음악 streaming 서비스를 개발하는 기업은 Claude Code를 코드 리뷰 자동화 pipeline에 통합하고 있습니다. 이 시스템은 pull request마다 자동 리뷰를 실행하고, 테스트 케이스를 생성하며, 구체적이고 실행 가능한 피드백을 돌려줍니다. 오탐을 최소화하는 prompt를 설계해야 합니다.

몇 주 운영해 보니, 개발자들 사이에서 자동 리뷰가 "노이즈가 많다"는 말이 나오고 있습니다. 실제 사례를 보면 다음 두 종류의 댓글이 섞여 있습니다.

변수 이름 짓는 방식, 선호하는 assertion 스타일, 테스트 부족에 관한 댓글

실제 null 참조 버그나 인가 우회(authorization bypass) 같은 진짜 문제에 관한 댓글

현재 prompt에는 "확신이 높은 문제만 보고할 것"이라고만 적혀 있습니다.

리뷰의 유용성을 가장 직접적으로 개선할 수 있는 prompt 변경은 무엇입니까? (2개를 고르십시오.)

- A. JA: 自動検出の結果を1つのノンブロッキングな要約コメントにまとめ、インラインには投稿しない。
  - KO: 자동 검출 결과를 non-blocking 요약 댓글 하나로 모으고, inline에는 게시하지 않습니다.
  - EN: Consolidate the automatically detected results into a single non-blocking summary comment, and do not post them inline.
- B. JA: レビュー範囲は今のまま広く保ち、各インラインコメントに数値の確信度スコアと簡潔な根拠の説明を添えさせる。
  - KO: 리뷰 범위는 지금처럼 넓게 유지하고, 각 inline 댓글에 수치로 된 확신도 점수와 간결한 근거 설명을 붙이게 합니다.
  - EN: Keep the review scope as broad as it is now, and have Claude attach a numeric confidence score and a brief rationale to each inline comment.
- C. JA: 報告する問題の種類（本番バグやセキュリティ欠陥など）とスキップする種類を、検証できる基準で定義する。
  - KO: 보고할 문제의 종류(프로덕션 버그나 보안 결함 등)와 건너뛸 종류를 검증 가능한 기준으로 정의합니다.
  - EN: Define, with verifiable criteria, the kinds of issues to report (such as production bugs and security flaws) and the kinds to skip.
- D. JA: 命名やフォーマット、アサーションスタイルの好みに関する項目を、レビューのチェックリストから外す。
  - KO: 이름 짓기나 포매팅, assertion 스타일 취향에 관한 항목을 리뷰 체크리스트에서 뺍니다.
  - EN: Remove items about naming, formatting, and assertion-style preferences from the review checklist.

## CCAR-F-Udemy02-0056

**JA** 自律型ドローン配送を手がけるスタートアップが、Claude CodeをCI/CDパイプラインに統合しています。このシステムは、自動コードレビューを実行し、テストケースを生成し、プルリクエストにフィードバックを返します。具体的で実行可能なフィードバックを返し、誤検知を最小限に抑えるプロンプトを設計する必要があります。

最近のCI実行の結果、20〜40ファイルにまたがるプルリクエストでは、レビューが表面的なスタイルの問題ばかりを報告し、ファイル横断の相互作用に依存する問題を見逃していることが分かりました。

チームは、レビューを自由度の高い調査的な処理にはせずに、より信頼できるレビュー設計にしたいと考えています。

行うべき変更はどれですか。

**KO** 자율 드론 배송을 하는 스타트업이 Claude Code를 CI/CD pipeline에 통합하고 있습니다. 이 시스템은 자동 코드 리뷰를 실행하고, 테스트 케이스를 생성하며, pull request에 피드백을 돌려줍니다. 구체적이고 실행 가능한 피드백을 돌려주면서 오탐을 최소화하는 prompt를 설계해야 합니다.

최근 CI 실행 결과, 20~40개 파일에 걸친 pull request에서는 리뷰가 표면적인 스타일 문제만 보고하고, 파일 간 상호작용에 따라 생기는 문제를 놓친다는 것이 밝혀졌습니다.

팀은 리뷰를 자유도가 높은 탐색형 처리로 만들지 않으면서, 더 신뢰할 수 있는 리뷰 설계로 바꾸고 싶어 합니다.

해야 할 변경은 무엇입니까?

- A. JA: ファイルのグループごとに独立した並列レビュアーを実行し、統合の工程を挟まずにそれぞれのコメントをそのまま公開する。
  - KO: 파일 그룹마다 독립된 병렬 리뷰어를 실행하고, 통합 단계를 거치지 않고 각각의 댓글을 그대로 공개합니다.
  - EN: Run independent parallel reviewers for each group of files, and publish each one's comments as they are, without an integration step.
- B. JA: 差分全体を1つのレビュープロンプトに渡し、コメントを出す重大度のしきい値を引き上げる。
  - KO: diff 전체를 하나의 리뷰 prompt에 넘기고, 댓글을 다는 심각도 임곗값을 올립니다.
  - EN: Pass the entire diff to a single review prompt and raise the severity threshold for emitting comments.
- C. JA: ファイル単位の集中レビューを固定の段階として順に実行し、最後に横断チェックの段階を置く。
  - KO: 파일 단위의 집중 리뷰를 고정된 단계로 차례로 실행하고, 마지막에 파일 간 교차 점검 단계를 둡니다.
  - EN: Run focused per-file reviews sequentially as fixed stages, and place a cross-file check stage at the end.
- D. JA: 各プルリクエストについて、Claudeが自分自身でレビューの進め方とツールを動的に選択できるようにする。
  - KO: pull request마다 Claude가 리뷰 진행 방식과 도구를 스스로 동적으로 선택하게 합니다.
  - EN: Let Claude dynamically choose its own review approach and tools for each pull request.

## CCAR-F-Udemy02-0057

**JA** 特許調査を専門とする法律事務所は、Claude Agent SDKを使用してマルチエージェントリサーチシステムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

このシステムのコーディネーターは、MCPで実装されたWeb検索サブエージェントと文書分析サブエージェントにタスクを振り分けています。評価の過程で、次のような誤った振り分けが多く見られました。

ユーザーがアップロードした特許明細書PDFの分析を依頼しているのに、文献レビュー系のタスクをWeb検索サブエージェントに送る

最新動向の確認が必要なWeb系のタスクを、文書分析サブエージェントに送る

ツールの実装自体は、一度正しく呼び出されれば正常に動作します。

ツール選択の信頼性を改善するために、このチームが最初に行うべきツール定義の変更はどれですか。（2つ選択してください。）

**KO** 특허 조사를 전문으로 하는 법률 사무소는 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 웹 검색용, 문서 분석용, 조사 결과 통합용, 보고서 생성용이 있습니다. 이 시스템은 주제를 조사해 출처를 명시한 종합 보고서를 작성합니다.

이 시스템의 coordinator는 MCP로 구현된 웹 검색 subagent와 문서 분석 subagent에 작업을 배분하고 있습니다. 평가 과정에서 다음과 같은 잘못된 배분이 많이 보였습니다.

사용자가 업로드한 특허 명세서 PDF의 분석을 요청했는데도, 문헌 리뷰 계열 작업을 웹 검색 subagent로 보냅니다

최신 동향을 확인해야 하는 웹 계열 작업을 문서 분석 subagent로 보냅니다

도구 구현 자체는 한 번 올바르게 호출되면 정상적으로 동작합니다.

도구 선택의 신뢰성을 개선하기 위해 이 팀이 가장 먼저 해야 할 도구 정의 변경은 무엇입니까? (2개를 고르십시오.)

- A. JA: 各リサーチターンで、結果をコーディネーターに返す前に必ずいずれか1つの利用可能なツールを呼び出すよう、モデルAPIを通じて強制する。
  - KO: 각 리서치 turn에서 결과를 coordinator에게 돌려주기 전에 사용 가능한 도구 중 하나를 반드시 호출하도록, 모델 API를 통해 강제합니다.
  - EN: Force, through the model API, that on each research turn the model must call exactly one of the available tools before returning results to the coordinator.
- B. JA: 各ツール定義を、想定される用途・想定されない用途・入力・返されるデータ・注意点を網羅した詳細な説明文に書き換える。
  - KO: 각 도구 정의를, 의도된 용도·의도되지 않은 용도·입력·반환 데이터·주의 사항을 빠짐없이 다룬 자세한 설명으로 고쳐 씁니다.
  - EN: Rewrite each tool definition as a detailed description that covers its intended uses, unintended uses, inputs, returned data, and caveats.
- C. JA: Webクエリ・PDF分析・引用検索それぞれについて、JSON Schemaのフィールド説明の中にリクエスト例を追加する。
  - KO: 웹 쿼리·PDF 분석·인용 검색 각각에 대해, JSON Schema 필드 설명 안에 요청 예시를 추가합니다.
  - EN: Add request examples to the JSON Schema field descriptions for web queries, PDF analysis, and citation lookup.
- D. JA: 各ツールの名前を、ライブのWeb検索結果を扱うのか、アップロードされた文書を扱うのかが分かる名前に変更する。
  - KO: 각 도구의 이름을, 실시간 웹 검색 결과를 다루는지 업로드된 문서를 다루는지 알 수 있는 이름으로 바꿉니다.
  - EN: Rename each tool so that the name makes clear whether it handles live web search results or uploaded documents.

## CCAR-F-Udemy02-0058

**JA** あなたは、カスタマーサポート業務を支援するAIエージェントを運用しています。チームはこのエージェントに、問い合わせごとに次のどの対応をとるかを判断させています。

問い合わせ内容を調査する

対応方針を立案する

直接返信を作成する

この判断ロジックは、カスタムコマンド/triageとして実装されています。しかし評価テストでは、「この件を確認して」「エラーを調べて」「この文面を改善できる？」のようなあいまいな依頼に対して、挙動に一貫性がありません。詳細なルールを文書化して追加しても、判断基準は安定していません。

次に変更すべきことはどれですか。

**KO** 당신은 고객 지원 업무를 돕는 AI agent를 운영하고 있습니다. 팀은 이 agent가 문의마다 다음 중 어떤 대응을 할지 판단하게 하고 있습니다.

문의 내용 조사

대응 방침 수립

직접 답장 작성

이 판단 로직은 custom command인 /triage로 구현되어 있습니다. 그러나 평가 테스트에서 "이 건 확인해 줘", "에러 좀 살펴봐 줘", "이 문구 더 좋게 고칠 수 있어?" 같은 모호한 요청에 대해 동작이 일관되지 않습니다. 자세한 규칙을 문서로 정리해 추가해도 판단 기준이 안정되지 않습니다.

다음으로 무엇을 변경해야 합니까?

- A. JA: 計画作業を示唆しうる依頼では直接の返信作成を避ける、という強い指示を追加する。
  - KO: 계획 작업을 암시할 수 있는 요청에서는 직접 답장 작성을 피하라는 강한 지시를 추가합니다.
  - EN: Add a strong instruction to avoid writing direct replies for requests that might imply planning work.
- B. JA: 調査・計画・直接返信のそれぞれを起動すべきフレーズを網羅的に列挙した、より長いチェックリストを追加する。
  - KO: 조사·계획·직접 답장 각각을 시작해야 할 표현을 빠짐없이 나열한, 더 긴 체크리스트를 추가합니다.
  - EN: Add a longer checklist that exhaustively lists the phrases that should trigger each of investigation, planning, and direct reply.
- C. JA: あいまいな依頼の類似例を2〜4件、選ぶべき対応と他案を退ける理由を添えてタグ付きで追加する。
  - KO: 모호한 요청의 비슷한 예시 2~4개를, 골라야 할 대응과 다른 안을 배제한 이유와 함께 태그로 감싸 추가합니다.
  - EN: Add two to four similar examples of ambiguous requests, in tags, each with the action to choose and the reason the alternatives were rejected.
- D. JA: タグ付けしていない過去のやりとりを大量に追加し、Claudeにチームの好みを推測させる。
  - KO: 태그를 붙이지 않은 과거 대화를 대량으로 추가해, Claude가 팀의 선호를 추측하게 합니다.
  - EN: Add a large amount of untagged past interactions and have Claude infer the team's preferences.

## CCAR-F-Udemy02-0059

**JA** あなたは、Claude Agent SDKを使用して、マルチエージェントの財務分析レポートシステムを構築しています。コーディネーターエージェントが、専門サブエージェントに作業を委任します。サブエージェントには、市場データを収集するもの、決算資料を分析するもの、知見を統合するもの、レポートを生成するものがあります。

このチームには、レポート中の主張を引用元と突き合わせて検証するようClaude Codeに依頼する、カスタムの/source-checkスラッシュコマンドがあります。あるエンジニアがsource-check.mdを~/.claude/commands/の下に保存しています。このコマンドは本人には使えますが、リポジトリをクローンしたチームメイトには使えません。

同じコマンドをリポジトリから利用できるようにするために、チームが行うべきことはどれですか。

**KO** 당신은 Claude Agent SDK로 multi-agent 재무 분석 보고서 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 시장 데이터를 수집하는 것, 결산 자료를 분석하는 것, 분석 결과를 통합하는 것, 보고서를 생성하는 것이 있습니다.

이 팀에는 보고서 속 주장을 인용 출처와 대조해 검증하도록 Claude Code에 요청하는 custom /source-check slash command가 있습니다. 한 엔지니어가 source-check.md를 ~/.claude/commands/ 아래에 저장해 두었습니다. 이 명령은 본인은 쓸 수 있지만, 저장소를 clone한 팀원들은 쓸 수 없습니다.

같은 명령을 저장소에서 사용할 수 있게 하려면 팀은 무엇을 해야 합니까?

- A. JA: source-check.mdを~/.claude/commands/に保持したまま、プロジェクトのREADMEにこのコマンドを文書化する。
  - KO: source-check.md를 ~/.claude/commands/에 그대로 두고, 프로젝트 README에 이 명령을 문서화합니다.
  - EN: Keep source-check.md in ~/.claude/commands/ and document the command in the project README.
- B. JA: source-checkの指示をルートのCLAUDE.mdに追加し、手動で呼び出す。
  - KO: source-check 지시 사항을 루트 CLAUDE.md에 추가하고, 수동으로 호출합니다.
  - EN: Add the source-check instructions to the root CLAUDE.md and invoke them manually.
- C. JA: source-check.mdを.claude/commands/に保持しつつ、.claudeディレクトリをバージョン管理から除外する。
  - KO: source-check.md를 .claude/commands/에 두되, .claude 디렉터리를 버전 관리에서 제외합니다.
  - EN: Keep source-check.md in .claude/commands/ but exclude the .claude directory from version control.
- D. JA: source-check.mdをリポジトリ内の.claude/commands/に移動し、そのファイルをコミットする。
  - KO: source-check.md를 저장소 안의 .claude/commands/로 옮기고, 그 파일을 commit합니다.
  - EN: Move source-check.md to .claude/commands/ in the repository and commit the file.

## CCAR-F-Udemy02-0060

**JA** 動画配信プラットフォームを開発する企業は、Claude Codeをコードレビュー自動化パイプラインに統合しています。このシステムは、プルリクエストごとに自動レビューを実行し、テストケースを生成し、具体的で実行可能なフィードバックを返します。誤検知を最小限に抑えるプロンプトを設計する必要があります。

あるPRのレビュー中に、メインセッションは変更されたファイルを読み取り、失敗しているテストに気づきました。そのうえで、fork（会話を引き継ぐ方式）ではなく、通常の名前付きのセキュリティレビュー用サブエージェントに作業を委任しました。

このサブエージェントは一般的な指摘しか返さず、差分やテスト出力から得られるはずのPR固有の証拠を見落としていました。

レビューの信頼性を最も直接的に改善できる変更はどれですか。（2つ選択してください。）

**KO** 동영상 streaming 플랫폼을 개발하는 회사가 Claude Code를 코드 리뷰 자동화 pipeline에 통합했습니다. 이 시스템은 pull request마다 자동 리뷰를 실행하고, 테스트 케이스를 생성하며, 구체적이고 실행 가능한 피드백을 돌려줍니다. 오탐(false positive)을 최소화하는 prompt를 설계해야 합니다.

어떤 PR을 리뷰하던 중에 main session은 변경된 파일을 읽고 실패하는 테스트를 발견했습니다. 그런 다음 fork(대화를 이어받는 방식)가 아니라, 일반적인 이름 있는 보안 리뷰용 subagent에게 작업을 위임했습니다.

이 subagent는 일반적인 지적만 돌려주었고, diff와 테스트 출력에서 얻을 수 있었을 PR 고유의 증거를 놓쳤습니다.

리뷰의 신뢰성을 가장 직접적으로 개선할 수 있는 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 通常の名前付きサブエージェントではなくforkで委任し、親の会話を引き継いだ状態から分岐させる。
  - KO: 일반적인 이름 있는 subagent 대신 fork로 위임해, 부모 대화를 이어받은 상태에서 분기시킵니다.
  - EN: Delegate with a fork instead of a regular named subagent, branching from a state that inherits the parent conversation.
- B. JA: レビュー結果を生成する前に、親の会話のトランスクリプトを読み取るようサブエージェントに指示する。
  - KO: 리뷰 결과를 생성하기 전에 부모 대화의 transcript를 읽도록 subagent에게 지시합니다.
  - EN: Instruct the subagent to read the parent conversation's transcript before producing review results.
- C. JA: 変更ファイルと差分の抜粋、失敗したテストの出力、レビュー基準をサブエージェントのプロンプトに含める。
  - KO: 변경된 파일과 diff 발췌, 실패한 테스트의 출력, 리뷰 기준을 subagent의 prompt에 포함합니다.
  - EN: Include the changed files and diff excerpts, the failing test output, and the review criteria in the subagent's prompt.
- D. JA: 名前付きサブエージェントを新規に呼び出し、それ以前のCIステップから引き継いだ記録済みのトランスクリプトに頼る。
  - KO: 이름 있는 subagent를 새로 호출하고, 그 이전 CI 단계에서 넘겨받은 기록된 transcript에 의존합니다.
  - EN: Invoke a fresh named subagent and rely on the recorded transcript carried over from earlier CI steps.

## CCAR-F-Udemy03-0001

**JA** あなたはEコマース企業のエンジニアリングチームで、開発を加速するためにClaude Codeを使用しています。チームでは、コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行をどのように使い分けるかを理解する必要があります。

このチームは、注文データベースの長時間の分析を終えたところで、同じ基準点（ベースライン）から2つの異なるデータベース移行戦略を比較したいと考えています。要件は次のとおりです。

それぞれの調査で、ベースラインの文脈を保持する

一方の戦略の推論履歴が、もう一方を汚さないようにする

後で再利用できるように、元の分析セッションをそのまま残す

このチームが取るべき対応はどれですか。

**KO** 당신은 이커머스 회사의 엔지니어링 팀에서 개발 속도를 높이기 위해 Claude Code를 사용하고 있습니다. 팀은 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 씁니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하고, plan mode와 직접 실행을 어떻게 구분해 쓸지 이해해야 합니다.

이 팀은 주문 데이터베이스를 오랫동안 분석하는 작업을 막 마쳤고, 같은 기준점(baseline)에서 서로 다른 두 가지 데이터베이스 마이그레이션 전략을 비교하려고 합니다. 요구 사항은 다음과 같습니다.

각 조사에서 baseline의 context를 유지한다

한 전략의 추론 기록이 다른 전략을 오염시키지 않게 한다

나중에 다시 쓸 수 있도록 원래 분석 session을 그대로 남겨 둔다

이 팀은 어떻게 대응해야 합니까?

- A. JA: fork_sessionを有効にしてベースラインのセッションIDで再開し、各戦略の調査をそれぞれ新しいセッションで実行する。
  - KO: fork_session을 활성화해 baseline의 session ID로 재개하고, 각 전략의 조사를 각각 새 session에서 실행합니다.
  - EN: Resume with the baseline session ID with fork_session enabled, and run the investigation of each strategy in its own new session.
- B. JA: ベースラインのセッションを通常どおり再開し、それぞれの戦略を回答内の別々のセクションに分けて記述するようClaudeに依頼する。
  - KO: baseline session을 평소처럼 재개하고, 각 전략을 응답 안의 별도 섹션으로 나눠 쓰도록 Claude에 요청합니다.
  - EN: Resume the baseline session as usual, and ask Claude to write each strategy in a separate section within its response.
- C. JA: プロジェクトフォルダを2回複製し、複製した各フォルダが独立したセッション履歴を持つことに依存する。
  - KO: 프로젝트 폴더를 두 번 복제하고, 복제한 각 폴더가 독립된 session 기록을 갖는 데 의존합니다.
  - EN: Duplicate the project folder twice, and rely on each duplicated folder having its own independent session history.
- D. JA: 同じディレクトリの最新セッションをcontinueで2回再開し、各戦略に異なるプロンプトラベルを割り当てる。
  - KO: 같은 디렉터리의 최신 session을 continue로 두 번 재개하고, 각 전략에 서로 다른 prompt 라벨을 붙입니다.
  - EN: Resume the most recent session in the same directory twice with continue, and assign a different prompt label to each strategy.

## CCAR-F-Udemy03-0002

**JA** あるエネルギー政策シンクタンクが、Claude Agent SDKを使用してマルチエージェントリサーチシステムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムは再生可能エネルギープロジェクトに関するトピックを調査し、出典を明記した包括的なレポートを作成します。

文書分析サブエージェントは、各プロジェクト記事の主要な資金提供元を抽出し、抽出した値の引用を示す必要があります。しかし複数の記事では、資金提供元らしき手がかりが、アプリケーション側で付けた文書タイトルのメタデータにしかありません。文書本文には、資金提供に関する記述も、資金提供者の名前を挙げた箇所もまったくありません。

バリデーターは、裏付けとなる引用が無いという理由で、これらの記録を却下しています。

このチームが取るべき対応はどれですか。

**KO** 한 에너지 정책 싱크탱크가 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 웹을 검색하는 것, 문서를 분석하는 것, 조사 결과를 통합하는 것, 보고서를 생성하는 것이 있습니다. 이 시스템은 재생에너지 프로젝트에 관한 주제를 조사하고, 출처를 명시한 종합 보고서를 작성합니다.

문서 분석 subagent는 프로젝트 기사마다 주요 자금 제공처를 추출하고, 추출한 값의 인용을 제시해야 합니다. 그런데 여러 기사에서 자금 제공처로 보이는 단서가 애플리케이션 쪽에서 붙인 문서 제목 metadata에만 있습니다. 문서 본문에는 자금 제공에 관한 서술도, 자금 제공자의 이름을 언급한 부분도 전혀 없습니다.

validator는 뒷받침하는 인용이 없다는 이유로 이 레코드들을 거부하고 있습니다.

이 팀은 어떻게 대응해야 합니까?

- A. JA: 資金提供元をスキーマ上の必須フィールドとし、統合ステップの前に抽出ツールの使用を強制する。
  - KO: 자금 제공처를 schema의 필수 필드로 지정하고, 통합 단계 전에 추출 도구 사용을 강제합니다.
  - EN: Make the funding source a required field in the schema, and force use of the extraction tool before the synthesis step.
- B. JA: 裏付けとなる引用可能な本文の記述が存在しない場合、資金提供元を「不明」として返し、証拠が不足している旨の注記を添える。
  - KO: 뒷받침할 수 있는 인용 가능한 본문 서술이 없으면 자금 제공처를 "불명"으로 반환하고, 증거가 부족하다는 메모를 덧붙입니다.
  - EN: When no supporting citable passage exists in the body text, return the funding source as "unknown" and attach a note that evidence is insufficient.
- C. JA: 抽出呼び出しのmax_tokensを増やし、欠落している資金提供元の引用を補完するために解析を再実行する。
  - KO: 추출 호출의 max_tokens를 늘리고, 빠진 자금 제공처 인용을 채우기 위해 분석을 다시 실행합니다.
  - EN: Increase max_tokens on the extraction call and rerun the parsing to fill in the missing funding source citations.
- D. JA: 同じソースに対して文書分析サブエージェントを再実行し、資金提供に関する記述をより網羅的に検索させる。
  - KO: 같은 출처에 대해 문서 분석 subagent를 다시 실행해, 자금 제공에 관한 서술을 더 빠짐없이 검색하게 합니다.
  - EN: Rerun the document analysis subagent on the same sources and have it search more exhaustively for statements about funding.

## CCAR-F-Udemy03-0003

**JA** ある保険会社が、Claude Agent SDKを使用してカスタマーサポート解決エージェントを構築しています。このエージェントは、返金、保険料に関する異議、契約内容の問い合わせなど、あいまいさの高い依頼を処理します。カスタムのModel Context Protocol（MCP）ツール（get_policyholder、lookup_claim、process_payout、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を達成することです。

パイロットで分析したところ、現在のコーディネーターは、回答する前に毎回すべての専門エージェントへ、支払い資格、アカウントアクセス権限、エスカレーションの適否に関する質問を送っていることが分かりました。結果自体は正確ですが、次の問題が起きています。

保険料に関する異議のうち、あいまいな案件に不要なアカウント復旧の詳細が含まれてしまう

単純な依頼でも、コンテキストを過剰に消費している

このオーケストレーションの問題に最も適した変更はどれですか。（2つ選択してください。）

**KO** 한 보험회사가 Claude Agent SDK로 고객 지원 해결 agent를 구축하고 있습니다. 이 agent는 환불, 보험료 이의 제기, 계약 내용 문의처럼 모호성이 높은 요청을 처리합니다. custom Model Context Protocol(MCP) 도구(get_policyholder, lookup_claim, process_payout, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation해야 할 시점을 판단하면서 1차 해결률 80% 이상을 달성하는 것입니다.

파일럿을 분석해 보니, 현재 coordinator는 답변하기 전에 매번 모든 전문 agent에게 지급 자격, 계정 접근 권한, escalation 적합성에 관한 질문을 보내고 있었습니다. 결과 자체는 정확하지만, 다음과 같은 문제가 생기고 있습니다.

보험료 이의 제기 중 모호한 건에 불필요한 계정 복구 세부 정보가 포함된다

단순한 요청에서도 context를 과도하게 소비한다

이 orchestration 문제에 가장 적합한 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: コーディネーターが、役割の説明が現在の案件に合う専門エージェントだけを選んで呼び出すようにする。
  - KO: coordinator가 역할 설명이 현재 건에 맞는 전문 agent만 골라 호출하게 합니다.
  - EN: Have the coordinator select and call only the specialist agents whose role descriptions match the current case.
- B. JA: コーディネーターが最終的な顧客向け回答を作成する前に、すべての専門エージェントがより短い要約を返すようにする。
  - KO: coordinator가 고객에게 보낼 최종 답변을 작성하기 전에, 모든 전문 agent가 더 짧은 요약을 반환하게 합니다.
  - EN: Have every specialist agent return a shorter summary before the coordinator composes the final customer-facing answer.
- C. JA: すべての専門エージェント用プロンプトをコーディネーターに統合し、1つの共有コンテキストウィンドウであらゆる案件を処理できるようにする。
  - KO: 모든 전문 agent용 prompt를 coordinator에 통합해, 하나의 공유 context window에서 모든 건을 처리하게 합니다.
  - EN: Consolidate all specialist agent prompts into the coordinator so that every case is handled in a single shared context window.
- D. JA: 単純な依頼はどの専門エージェントも呼び出さずにそのまま解決するトリアージのステップを設ける。
  - KO: 단순한 요청은 어떤 전문 agent도 호출하지 않고 바로 해결하는 triage 단계를 둡니다.
  - EN: Introduce a triage step that resolves simple requests directly without calling any specialist agent.

## CCAR-F-Udemy03-0004

**JA** ある特許調査会社が、Claudeを使用して構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSON（JavaScript Object Notation）スキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携できる必要があります。

現在、クライアントツールとして公開しているのはanalyze_documentの1つだけです。このツールは、文書のテキスト、実行する操作、出力形式を引数として受け取ります。

評価では、次の2つの問題が起きています。

下流のバリデーターは抽出済みのフィールドを受け取る前提なのに、Claudeがこのツールで要約を作ってしまうことがある

Claudeが、検証に必要なソースの抜粋を渡さないまま、クレーム（主張内容）の検証を試みることがある

不要なツールを増やさずに、ツール選択と下流での信頼性を最も改善できる再設計はどれですか。（2つ選択してください。）

**KO** 한 특허 조사 회사가 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON(JavaScript Object Notation) schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동할 수 있어야 합니다.

현재 클라이언트 도구로 공개한 것은 analyze_document 하나뿐입니다. 이 도구는 문서 텍스트, 실행할 작업, 출력 형식을 인자로 받습니다.

평가에서 다음 두 가지 문제가 발생하고 있습니다.

downstream validator는 추출된 필드를 받는다고 전제하는데, Claude가 이 도구로 요약을 만들어 버리는 경우가 있다

Claude가 검증에 필요한 출처 발췌를 넘기지 않은 채 claim(주장 내용) 검증을 시도하는 경우가 있다

불필요한 도구를 늘리지 않으면서 도구 선택과 downstream 신뢰성을 가장 크게 개선할 수 있는 재설계는 무엇입니까? (2개를 선택하십시오.)

- A. JA: 操作の指示はシステムプロンプトに移し、既存の連携部分の改修を抑えるため、ツールスキーマは今のまま維持する。
  - KO: 작업 지시는 system prompt로 옮기고, 기존 연동 부분의 수정을 줄이기 위해 도구 schema는 지금 그대로 유지합니다.
  - EN: Move the operation instructions into the system prompt, and keep the tool schema as it is to limit changes to existing integrations.
- B. JA: analyze_documentを、役割の説明と入力スキーマが明確で、互いに重複しない少数のワークフロー専用ツールに置き換える。
  - KO: analyze_document를 역할 설명과 입력 schema가 명확하고 서로 겹치지 않는 소수의 workflow 전용 도구로 대체합니다.
  - EN: Replace analyze_document with a small number of workflow-specific tools that have clear role descriptions and input schemas and do not overlap with one another.
- C. JA: クレーム検証用の入力スキーマでソースの抜粋を必須パラメータにし、抜粋がないと検証を呼び出せないようにする。
  - KO: claim 검증용 입력 schema에서 출처 발췌를 필수 파라미터로 지정해, 발췌가 없으면 검증을 호출할 수 없게 합니다.
  - EN: In the input schema for claim verification, make the source excerpt a required parameter so the verification cannot be called without an excerpt.
- D. JA: analyze_documentはそのまま残し、スキーマの列挙型に操作名をさらに追加したうえで、呼び出しのたびにClaudeに正確な操作を選ばせる。
  - KO: analyze_document는 그대로 두고 schema의 enum에 작업 이름을 더 추가한 뒤, 호출할 때마다 Claude가 정확한 작업을 고르게 합니다.
  - EN: Keep analyze_document as is, add more operation names to the schema's enum, and have Claude choose the exact operation on every call.

## CCAR-F-Udemy03-0005

**JA** あるアパレルECマーケットプレイスのチームが、ソフトウェア開発を加速するためにClaude Codeを使用しています。コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っており、カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合しています。プランモードと直接実行をどのように使い分けるかも理解しておきたいと考えています。

あるシニアエンジニアが、複数のパッケージから利用されている共有の認可レイヤーを移行しようとしています。状況は次のとおりです。

依存関係グラフが不明瞭

実現可能な設計案が複数ある

これまでにすぐ編集を始めた試みでは、広範な書き換えが起き、後で差し戻すことになった

このエンジニアが最初に取るべき行動はどれですか。（2つ選択してください。）

**KO** 한 의류 이커머스 마켓플레이스 팀이 소프트웨어 개발 속도를 높이기 위해 Claude Code를 사용하고 있습니다. 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 쓰고 있으며, custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합했습니다. plan mode와 직접 실행을 어떻게 구분해 쓸지도 이해하고 싶어 합니다.

한 시니어 엔지니어가 여러 패키지에서 사용하는 공유 인가(authorization) 레이어를 마이그레이션하려고 합니다. 상황은 다음과 같습니다.

의존성 그래프가 불분명하다

실현 가능한 설계안이 여러 개 있다

이전에 곧바로 편집부터 시작했던 시도에서는 광범위한 재작성이 일어나 나중에 되돌려야 했다

이 엔지니어가 가장 먼저 해야 할 행동은 무엇입니까? (2개를 선택하십시오.)

- A. JA: acceptEditsモードでClaude Codeを起動し、影響を受ける範囲を調査させたうえで、結果として生じたソースコードの変更をレビューする。
  - KO: acceptEdits 모드로 Claude Code를 시작해 영향 범위를 조사하게 한 뒤, 그 결과로 생긴 소스 코드 변경을 리뷰합니다.
  - EN: Start Claude Code in acceptEdits mode, have it investigate the affected scope, and then review the resulting source code changes.
- B. JA: 認可レイヤーを利用しているパッケージの依存関係グラフをClaude Codeに調査させ、設計案を選ぶ前にその結果を報告させる。
  - KO: 인가 레이어를 사용하는 패키지들의 의존성 그래프를 Claude Code에 조사하게 하고, 설계안을 고르기 전에 그 결과를 보고하게 합니다.
  - EN: Have Claude Code investigate the dependency graph of the packages that use the authorization layer and report its findings before choosing a design option.
- C. JA: bypassPermissionsモードに切り替え、Claudeに自由に調査・編集させ、悪い変更はテストで検出することに頼る。
  - KO: bypassPermissions 모드로 전환해 Claude가 자유롭게 조사·편집하게 하고, 잘못된 변경은 테스트로 잡아내는 데 의존합니다.
  - EN: Switch to bypassPermissions mode, let Claude investigate and edit freely, and rely on tests to catch bad changes.
- D. JA: プランモードでClaude Codeを起動し、影響を受ける範囲を調査させ、提案されたプランをレビューしたうえで、編集を承認する。
  - KO: plan mode로 Claude Code를 시작해 영향 범위를 조사하게 하고, 제안된 plan을 리뷰한 뒤 편집을 승인합니다.
  - EN: Start Claude Code in plan mode, have it investigate the affected scope, review the proposed plan, and then approve the edits.

## CCAR-F-Udemy03-0006

**JA** あなたは、Claude Agent SDKを使用して保険金請求のトリアージエージェントを構築しています。このエージェントは、返品、請求内容の照会、口座に関する問題など、あいまいさの高いリクエストを処理します。カスタムのModel Context Protocol（MCP）ツール（get_policyholder、lookup_claim、process_payout、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を達成することです。

バックエンドツールを呼び出す前に支払い資格の判定結果をキャッシュする、大きな機能を追加しようとしています。しかしエンジニアは、次の点に詳しくありません。

ポリシーのエッジケース

キャッシュ無効化のリスク

古い資格データによる障害モード

この変更の実装をClaude Codeに依頼する前に、エンジニアが行うべきことはどれですか。

**KO** 당신은 Claude Agent SDK로 보험금 청구 triage agent를 구축하고 있습니다. 이 agent는 반품, 청구 내용 문의, 계좌 관련 문제처럼 모호성이 높은 요청을 처리합니다. custom Model Context Protocol(MCP) 도구(get_policyholder, lookup_claim, process_payout, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation해야 할 시점을 판단하면서 1차 해결률 80% 이상을 달성하는 것입니다.

백엔드 도구를 호출하기 전에 지급 자격 판정 결과를 캐시하는 큰 기능을 추가하려고 합니다. 그런데 엔지니어는 다음 사항을 잘 모릅니다.

정책의 edge case

캐시 무효화의 위험

오래된 자격 데이터로 인한 장애 모드

이 변경의 구현을 Claude Code에 맡기기 전에 엔지니어가 해야 할 일은 무엇입니까?

- A. JA: Claude Codeに現在のコードベースから詳細な実装計画を作成させ、その計画が技術的に整合しているように見えたら実装に進む。
  - KO: Claude Code가 현재 코드베이스를 바탕으로 상세한 구현 계획을 작성하게 하고, 그 계획이 기술적으로 일관돼 보이면 구현으로 넘어갑니다.
  - EN: Have Claude Code create a detailed implementation plan from the current codebase, and proceed to implementation once the plan looks technically consistent.
- B. JA: Claude Codeに短い有効期限を持つ保守的なキャッシュを実装させ、その後ポリシーやエスカレーション処理の抜け漏れがないか差分を確認する。
  - KO: Claude Code가 유효기간이 짧은 보수적인 캐시를 구현하게 한 뒤, 정책이나 escalation 처리에 빠진 부분이 없는지 diff를 확인합니다.
  - EN: Have Claude Code implement a conservative cache with a short expiration time, and then review the diff for gaps in policy or escalation handling.
- C. JA: コードの計画に入る前に、AskUserQuestionでエッジケースや障害モードに関する要件をClaude Codeに聞き取らせる。
  - KO: 코드 계획에 들어가기 전에, Claude Code가 AskUserQuestion으로 edge case와 장애 모드에 관한 요구 사항을 물어보게 합니다.
  - EN: Before moving on to planning the code, have Claude Code interview the engineer about requirements related to edge cases and failure modes using AskUserQuestion.
- D. JA: Claude Codeに一般的な支払い資格キャッシュのシナリオに対するテストを作成させ、失敗するテストを使って段階的に実装を進める。
  - KO: Claude Code가 일반적인 지급 자격 캐시 시나리오에 대한 테스트를 작성하게 하고, 실패하는 테스트를 이용해 단계적으로 구현을 진행합니다.
  - EN: Have Claude Code write tests for common payout eligibility caching scenarios, and use the failing tests to drive the implementation incrementally.

## CCAR-F-Udemy03-0007

**JA** あるモーゲージ（住宅ローン）貸付会社が、Claudeを使用して構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSON（JavaScript Object Notation）スキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携できる必要があります。

本番環境で評価したところ、60ページのローン申込パッケージで精度が下がることが分かりました。このパッケージは、申込フォーム、審査担当者のメモ、請求書、添付資料といった、予測可能なセクションで構成されています。

現在の、全体を一度に抽出する方式は、個々のセクション内のフィールドは取得できるものの、次のような出力を生成することがあります。

重複したエンティティ

金額合計の不整合

スキーマ上は妥当だが、関係性が誤ったJSON

このチームがまず採用すべきタスク分解の戦略はどれですか。

**KO** 한 모기지(주택담보대출) 대출 회사가 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON(JavaScript Object Notation) schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동할 수 있어야 합니다.

운영 환경에서 평가해 보니, 60페이지짜리 대출 신청 패키지에서 정확도가 떨어지는 것으로 나타났습니다. 이 패키지는 신청서, 심사 담당자 메모, 청구서, 첨부 자료처럼 예측 가능한 섹션으로 구성되어 있습니다.

전체를 한 번에 추출하는 현재 방식은 개별 섹션 안의 필드는 잡아내지만, 다음과 같은 출력을 만들어 내는 경우가 있습니다.

중복된 엔티티

금액 합계의 불일치

schema상으로는 유효하지만 관계가 잘못된 JSON

이 팀이 먼저 채택해야 할 작업 분해 전략은 무엇입니까?

- A. JA: パッケージ全体を1つの大きな抽出プロンプトに送り、返す前にClaudeにJSONを自己チェックさせる。
  - KO: 패키지 전체를 하나의 큰 추출 prompt로 보내고, 반환하기 전에 Claude가 JSON을 스스로 점검하게 합니다.
  - EN: Send the entire package in a single large extraction prompt and have Claude self-check the JSON before returning it.
- B. JA: セクション単位で抽出パスを実行し、その後の調整パスで重複の除去とセクション間の整合確認を行う。
  - KO: 섹션 단위로 추출 패스를 실행한 뒤, 이어지는 조정 패스에서 중복 제거와 섹션 간 정합성 확인을 합니다.
  - EN: Run extraction passes per section, and then use a subsequent reconciliation pass to remove duplicates and verify consistency across sections.
- C. JA: 各ページを読むたびに次のサブタスクを動的に生成し、必要なフィールドが揃ったとエージェントが判断した時点で停止する。
  - KO: 페이지를 읽을 때마다 다음 하위 작업을 동적으로 생성하고, 필요한 필드가 다 모였다고 agent가 판단하면 멈춥니다.
  - EN: Dynamically generate the next subtask as each page is read, and stop when the agent decides the required fields have been collected.
- D. JA: まずパッケージ全体を1つの散文の要約にまとめ、その要約から最終パスで必要なスキーマフィールドを抽出する。
  - KO: 먼저 패키지 전체를 하나의 산문 요약으로 정리하고, 마지막 패스에서 그 요약으로부터 필요한 schema 필드를 추출합니다.
  - EN: First condense the entire package into a single prose summary, and then extract the required schema fields from that summary in a final pass.

## CCAR-F-Udemy03-0008

**JA** あなたは、Claude Agent SDKを使用して法務分野の判例調査アシスタントを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに処理を委任します。サブエージェントには、判例データベースを検索するもの、提出済みの準備書面を分析するもの、判例の要点を整理したメモを作成するもの、最終的な申立書をまとめるものがあります。このシステムは法的論点を調査し、引用付きの申立書を作成します。

あるテスト実行で、コーディネーターは次の順に処理しました。

判例検索サブエージェントと書面分析サブエージェントを実行し、それぞれのtool_resultブロックを送信した

stop_reasonが"tool_use"で、メモ作成サブエージェントの呼び出しを要求するアシスタント応答を受け取った

しかし現在のループは、その応答をそのまま最終回答として扱い、そのテキストを申立書の作成処理に渡しています。そのため、判例の要点分析が欠けた申立書が作られています。

行うべき変更はどれですか。（2つ選択してください。）

**KO** 당신은 Claude Agent SDK로 법무 분야의 판례 조사 어시스턴트를 구축하고 있습니다. coordinator agent가 전문 subagent에게 처리를 위임합니다. subagent로는 판례 데이터베이스를 검색하는 것, 제출된 준비서면을 분석하는 것, 판례의 요점을 정리한 메모를 작성하는 것, 최종 신청서를 작성하는 것이 있습니다. 이 시스템은 법적 쟁점을 조사하고 인용이 달린 신청서를 작성합니다.

한 테스트 실행에서 coordinator는 다음 순서로 처리했습니다.

판례 검색 subagent와 서면 분석 subagent를 실행하고, 각각의 tool_result 블록을 전송했다

stop_reason이 "tool_use"이고 메모 작성 subagent 호출을 요청하는 assistant 응답을 받았다

그러나 현재 loop는 그 응답을 그대로 최종 답변으로 취급하고, 그 텍스트를 신청서 작성 처리로 넘기고 있습니다. 그 결과 판례 요점 분석이 빠진 신청서가 만들어지고 있습니다.

어떤 변경을 해야 합니까? (2개를 선택하십시오.)

- A. JA: stop_reasonがtool_useの間はツールを実行して結果を返し、end_turnの応答だけを最終回答にする。
  - KO: stop_reason이 tool_use인 동안에는 도구를 실행해 결과를 반환하고, end_turn 응답만 최종 답변으로 삼습니다.
  - EN: While stop_reason is tool_use, execute the tool and return the result, and treat only an end_turn response as the final answer.
- B. JA: 応答のテキストに「まとめる準備ができた」などの文言があるかを見て、次のサブエージェントを実行するか判断する。
  - KO: 응답 텍스트에 "정리할 준비가 됐다" 같은 문구가 있는지 보고 다음 subagent를 실행할지 판단합니다.
  - EN: Decide whether to run the next subagent by checking whether the response text contains phrasing such as "ready to summarize."
- C. JA: 要求されたtool_useブロックごとにtool_resultを1つずつ作り、1つのユーザーメッセージにまとめて返す。
  - KO: 요청된 tool_use 블록마다 tool_result를 하나씩 만들어, 하나의 user 메시지에 모아서 반환합니다.
  - EN: Create one tool_result for each requested tool_use block, and return them together in a single user message.
- D. JA: メモ作成サブエージェントの結果に新しいtool_use_idを付けたtool_resultとして送り、申立書の作成を再開する。
  - KO: 메모 작성 subagent의 결과를 새 tool_use_id를 붙인 tool_result로 보내고, 신청서 작성을 재개합니다.
  - EN: Send the memo creation subagent's result as a tool_result with a new tool_use_id, and resume creating the motion.

## CCAR-F-Udemy03-0009

**JA** ある開発チームが、コード生成、リファクタリング、デバッグ、ドキュメント作成を効率化するために、Claude Codeを開発ワークフローに導入しています。カスタムスラッシュコマンドやCLAUDE.mdの設定を活用しており、プランモードと直接実行をどのように使い分けるかも理解しておく必要があります。

あるチームメンバーは、既知の1つの関数に、負の数量を拒否するガード節を1つだけ追加し、そのファイルの既存の単体テストを実行してほしいと考えています。対象ファイルのパスと期待される挙動はすでにわかっており、API・スキーマ・アーキテクチャの変更は一切伴いません。

開発者が取るべき対応はどれですか。

**KO** 한 개발팀이 코드 생성, refactoring, 디버깅, 문서 작성을 효율화하기 위해 Claude Code를 개발 workflow에 도입하고 있습니다. custom slash command와 CLAUDE.md 설정을 활용하고 있으며, plan mode와 직접 실행을 어떻게 구분해 쓸지도 이해해야 합니다.

한 팀원은 이미 알고 있는 함수 하나에 음수 수량을 거부하는 guard 절을 하나만 추가하고, 그 파일의 기존 단위 테스트를 실행하고 싶어 합니다. 대상 파일 경로와 기대 동작은 이미 알고 있으며, API·schema·아키텍처 변경은 전혀 없습니다.

개발자는 어떻게 대응해야 합니까?

- A. JA: まずacceptEditsモードに切り替えてClaudeに編集させ、その後で差分を確認する。
  - KO: 먼저 acceptEdits 모드로 전환해 Claude가 편집하게 하고, 그 뒤에 diff를 확인합니다.
  - EN: First switch to acceptEdits mode and let Claude make the edit, and then review the diff afterward.
- B. JA: Claude Codeにその小さな変更を直接行わせ、指定された単体テストを実行させる。
  - KO: Claude Code가 그 작은 변경을 직접 하게 하고, 지정한 단위 테스트를 실행하게 합니다.
  - EN: Have Claude Code make the small change directly and run the specified unit tests.
- C. JA: まずbypassPermissionsを有効にし、Claude Codeが権限確認なしに編集とテストを行えるようにする。
  - KO: 먼저 bypassPermissions를 활성화해, Claude Code가 권한 확인 없이 편집과 테스트를 할 수 있게 합니다.
  - EN: First enable bypassPermissions so that Claude Code can edit and test without permission prompts.
- D. JA: まずプランモードに入り、計画を確認したうえで、調査を経て実装を承認する。
  - KO: 먼저 plan mode로 들어가 계획을 확인하고, 조사를 거친 뒤 구현을 승인합니다.
  - EN: First enter plan mode, review the plan, and then approve the implementation after investigation.

## CCAR-F-Udemy03-0010

**JA** あるSaaS企業のSREチームは、Messages APIの上に独自のエージェントループを実装し、障害調査エージェントを運用しています。エージェントの動きは次のとおりです。

調査の冒頭でget_incidentを呼び出し、インシデントの定義（影響サービス、重大度、発生時刻）を取得する

その後、search_logsで毎回数千トークンのログ抜粋を受け取りながら、1件の調査で数十回の検索を行う

ログ抜粋は、一度分析すれば見返すことはほとんどありません。一方、インシデントの定義は、最終報告を書くまで繰り返し参照されます。

調査の後半になると、入力トークンがコンテキストウィンドウの上限に近づき、応答の遅延と費用も増えています。

インシデントの定義を保ったまま、コンテキストの肥大化を抑えられる変更はどれですか。（2つ選択してください。）

**KO** 한 SaaS 회사의 SRE 팀은 Messages API 위에 자체 agent loop를 구현해 장애 조사 agent를 운영하고 있습니다. agent의 동작은 다음과 같습니다.

조사 초반에 get_incident를 호출해 인시던트 정의(영향 서비스, 심각도, 발생 시각)를 가져온다

그 뒤 search_logs로 매번 수천 토큰 분량의 로그 발췌를 받으면서, 조사 한 건에 수십 번 검색한다

로그 발췌는 한 번 분석하고 나면 다시 볼 일이 거의 없습니다. 반면 인시던트 정의는 최종 보고서를 쓸 때까지 반복해서 참조됩니다.

조사 후반이 되면 입력 토큰이 context window 한도에 가까워지고, 응답 지연과 비용도 늘어나고 있습니다.

인시던트 정의를 유지하면서 context 비대화를 억제할 수 있는 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 送信前に入力トークン数を数え、閾値を超えたら会話の先頭にある古いメッセージから順に消去する。
  - KO: 전송 전에 입력 토큰 수를 세고, 임계값을 넘으면 대화 맨 앞의 오래된 메시지부터 차례로 삭제합니다.
  - EN: Count input tokens before sending, and when a threshold is exceeded, delete messages starting with the oldest ones at the beginning of the conversation.
- B. JA: clear_tool_usesを有効にし、直近の数回分を除いた古いツール結果を消去させる。
  - KO: clear_tool_uses를 활성화해, 최근 몇 번을 제외한 오래된 도구 결과를 지우게 합니다.
  - EN: Enable clear_tool_uses so that old tool results, except for the most recent few, are cleared.
- C. JA: get_incidentをexclude_toolsに指定し、インシデントの定義の結果は最終報告まで残す。
  - KO: get_incident를 exclude_tools에 지정해, 인시던트 정의 결과는 최종 보고서까지 남겨 둡니다.
  - EN: Specify get_incident in exclude_tools so that the incident definition result is retained until the final report.
- D. JA: search_logsが1回に返す件数を増やし、少ない呼び出し回数で広い範囲のログを受け取らせる。
  - KO: search_logs가 한 번에 반환하는 건수를 늘려, 더 적은 호출 횟수로 넓은 범위의 로그를 받게 합니다.
  - EN: Increase the number of results that search_logs returns per call, so that a wide range of logs is received with fewer calls.

## CCAR-F-Udemy03-0011

**JA** あるヘルスケアデータプラットフォームのチームが、ソフトウェア開発を加速するためにClaude Codeを使用しています。コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っており、カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合しています。プランモードと直接実行をどのように使い分けるかを理解する必要があります。

このチームは、自社開発の認可レイヤーをポリシーエンジンに置き換える作業を、APIハンドラー、ミドルウェア、テストの全体にわたって進めようとしています。状況は次のとおりです。

ポリシー境界をどこに置くべきかについて、エンジニアの間で意見が分かれている

この作業を担当する開発者は、影響を受ける複数のパッケージに不慣れである

実装に着手する前に選ぶべきワークフローはどれですか。（2つ選択してください。）

**KO** 한 헬스케어 데이터 플랫폼 팀이 소프트웨어 개발 속도를 높이기 위해 Claude Code를 사용하고 있습니다. 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 쓰고 있으며, custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합했습니다. plan mode와 직접 실행을 어떻게 구분해 쓸지 이해해야 합니다.

이 팀은 자체 개발한 인가(authorization) 레이어를 정책 엔진으로 교체하는 작업을 API 핸들러, 미들웨어, 테스트 전반에 걸쳐 진행하려고 합니다. 상황은 다음과 같습니다.

정책 경계를 어디에 둘지를 두고 엔지니어들의 의견이 갈린다

이 작업을 맡은 개발자는 영향을 받는 여러 패키지에 익숙하지 않다

구현에 착수하기 전에 선택해야 할 workflow는 무엇입니까? (2개를 선택하십시오.)

- A. JA: AskUserQuestionでポリシー境界の配置候補をClaude Codeに提示させ、実装前に意見の相違を決着させる。
  - KO: Claude Code가 AskUserQuestion으로 정책 경계의 배치 후보를 제시하게 하고, 구현 전에 의견 차이를 정리합니다.
  - EN: Have Claude Code present candidate placements for the policy boundary using AskUserQuestion, and settle the disagreement before implementation.
- B. JA: プランモードでClaude Codeにコードベースを調査させ、ファイルを編集する前に変更案を提示させる。
  - KO: plan mode에서 Claude Code가 코드베이스를 조사하게 하고, 파일을 편집하기 전에 변경안을 제시하게 합니다.
  - EN: In plan mode, have Claude Code investigate the codebase and present its proposed changes before editing any files.
- C. JA: opusモデルエイリアスを選択したうえで、Claude Codeに直接実行でリファクタリングを最後まで完了させる。
  - KO: opus 모델 alias를 선택한 뒤, Claude Code가 직접 실행으로 refactoring을 끝까지 완료하게 합니다.
  - EN: Select the opus model alias, and then have Claude Code complete the refactoring through to the end using direct execution.
- D. JA: 直接実行でClaude Codeにすぐ編集を始めさせ、テストの失敗を通じてアーキテクチャを把握させる。
  - KO: 직접 실행으로 Claude Code가 곧바로 편집을 시작하게 하고, 테스트 실패를 통해 아키텍처를 파악하게 합니다.
  - EN: Using direct execution, have Claude Code start editing immediately and learn the architecture through test failures.

## CCAR-F-Udemy03-0012

**JA** あなたは、Claude Agent SDKを使用してカスタマーサポート解決エージェントを構築しています。このエージェントは、返品、請求トラブル、アカウントの問題など、あいまいさの高い依頼を処理します。カスタムのModel Context Protocol（MCP）ツール（get_customer、lookup_order、process_refund、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を達成することです。

あるサポートエンジニアリングチームには、難しい請求トラブルの事実関係をすでに収集したエージェントがあります。チームは、その同じ時点から、2つの異なる解決方針を試したいと考えています。要件は次のとおりです。

それぞれの方針が、後から再開できる独自の会話履歴を持つ

元の分析スレッド自体は変更しない

チームが採用すべきアプローチはどれですか。

**KO** 당신은 Claude Agent SDK로 고객 지원 해결 agent를 구축하고 있습니다. 이 agent는 반품, 청구 분쟁, 계정 문제처럼 모호성이 높은 요청을 처리합니다. custom Model Context Protocol(MCP) 도구(get_customer, lookup_order, process_refund, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation해야 할 시점을 판단하면서 1차 해결률 80% 이상을 달성하는 것입니다.

한 지원 엔지니어링 팀에는 까다로운 청구 분쟁의 사실관계를 이미 수집한 agent가 있습니다. 팀은 바로 그 시점에서 서로 다른 두 가지 해결 방침을 시험해 보려고 합니다. 요구 사항은 다음과 같습니다.

각 방침이 나중에 재개할 수 있는 고유한 대화 기록을 갖는다

원래 분석 스레드 자체는 변경하지 않는다

팀이 채택해야 할 접근 방식은 무엇입니까?

- A. JA: 各方針でresume=baseline_session_idとfork_session=Trueを指定し、新しいsession_idを保存する。
  - KO: 각 방침에서 resume=baseline_session_id와 fork_session=True를 지정하고, 새 session_id를 저장합니다.
  - EN: For each approach, specify resume=baseline_session_id and fork_session=True, and save the new session_id.
- B. JA: 各方針についてresume=baseline_session_idを指定してquery()を実行し、その後アプリケーション側のメタデータで結果を区別する。
  - KO: 각 방침마다 resume=baseline_session_id를 지정해 query()를 실행한 뒤, 애플리케이션 쪽 metadata로 결과를 구분합니다.
  - EN: For each approach, run query() with resume=baseline_session_id, and then distinguish the results using application-side metadata.
- C. JA: 各方針の前にファイルチェックポイントを有効にし、そのチェックポイントに頼って別々の会話履歴を作成する。
  - KO: 각 방침 전에 파일 checkpoint를 활성화하고, 그 checkpoint에 의존해 별도의 대화 기록을 만듭니다.
  - EN: Enable file checkpointing before each approach, and rely on those checkpoints to create separate conversation histories.
- D. JA: 同じディレクトリでcontinue_conversation=Trueを指定してquery()を2回実行し、最新のセッション出力を保存する。
  - KO: 같은 디렉터리에서 continue_conversation=True를 지정해 query()를 두 번 실행하고, 최신 session 출력을 저장합니다.
  - EN: Run query() twice in the same directory with continue_conversation=True, and save the latest session output.

## CCAR-F-Udemy03-0013

**JA** あなたは、Claude Agent SDKを使用してマルチエージェントの助成金申請調査システムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

リファクタリングの後、生成されるレポートに、関連する2つの不具合が現れるようになりました。

最終レポートの中で、引用が二重に表示される

統合サブエージェントの出力がレポート生成エージェントに渡されるときに、根拠となる抜粋の一部が消える

原因は、主張と出典のスキーマ、統合用のプロンプト、レポートのテンプレートにまたがっていると考えられます。受け入れテストでは、各主張が根拠の抜粋と出典URLとともに1回だけ表示されることを確認する必要があります。

この不具合に最も効果的に対処できる、Claude Codeの使い方はどれですか。（2つ選択してください。）

**KO** 당신은 Claude Agent SDK로 multi-agent 보조금 신청 조사 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 웹을 검색하는 것, 문서를 분석하는 것, 조사 결과를 통합하는 것, 보고서를 생성하는 것이 있습니다. 이 시스템은 주제를 조사하고, 출처를 명시한 종합 보고서를 작성합니다.

refactoring 이후 생성되는 보고서에 서로 관련된 두 가지 결함이 나타나기 시작했습니다.

최종 보고서에서 인용이 두 번씩 표시된다

통합 subagent의 출력이 보고서 생성 agent로 넘어갈 때 근거 발췌 일부가 사라진다

원인은 주장·출처 schema, 통합용 prompt, 보고서 템플릿에 걸쳐 있는 것으로 보입니다. 인수 테스트에서는 각 주장이 근거 발췌 및 출처 URL과 함께 정확히 한 번만 표시되는지 확인해야 합니다.

이 결함에 가장 효과적으로 대처할 수 있는 Claude Code 사용법은 무엇입니까? (2개를 선택하십시오.)

- A. JA: プランモードで両方の不具合と影響範囲、制約、検証方法を1つの依頼にまとめ、計画を確認してから編集させる。
  - KO: plan mode에서 두 결함과 영향 범위, 제약 조건, 검증 방법을 하나의 요청으로 묶고, 계획을 확인한 뒤 편집하게 합니다.
  - EN: In plan mode, combine both defects, along with the scope of impact, constraints, and verification method, into a single request, and have Claude make edits after you review the plan.
- B. JA: 不具合ごとに/clearした別々のセッションを開いて割り当てたファイルだけを編集させ、後で結果をマージする。
  - KO: 결함마다 /clear한 별도 session을 열어 할당한 파일만 편집하게 하고, 나중에 결과를 병합합니다.
  - EN: Open a separate /clear-ed session for each defect, have each edit only its assigned files, and merge the results later.
- C. JA: 各主張が抜粋と出典URL付きで1回だけ出ることを確かめる受け入れテストを追加して実行する。
  - KO: 각 주장이 발췌와 출처 URL과 함께 정확히 한 번만 나오는지 확인하는 인수 테스트를 추가하고 실행합니다.
  - EN: Add and run an acceptance test that verifies each claim appears exactly once with its excerpt and source URL.
- D. JA: 計画は省いてClaudeに報告書まわりの不具合を幅広く直させ、作業が終わった後で差分をまとめて確認する。
  - KO: 계획은 생략하고 Claude가 보고서 주변의 결함을 폭넓게 고치게 한 뒤, 작업이 끝나면 diff를 한꺼번에 확인합니다.
  - EN: Skip planning and have Claude broadly fix the defects around the report, and review the diff all at once after the work is finished.

## CCAR-F-Udemy03-0014

**JA** あなたは、不動産管理会社向けに、Claudeを使用して構造化データ抽出システムを構築しています。このシステムは、賃貸契約書、入居申込書、修繕依頼書といった非構造化の文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携できる必要があります。

現在このシステムはスキーマ適合出力率99%を報告しており、ほとんどの賃貸契約書、入居申込書、修繕依頼書は、フィールド単位で高い確信度スコアを得ています。

レビュアーが毎週手作業で確認できるのは、高確信度レコードのうちごく一部だけです。しかし、レビューをさらに縮小する前に、本番環境でのエラー率を推定し、稀な新しい失敗パターンを検出する必要があります。

取るべき対応はどれですか。（2つ選択してください。）

**KO** 당신은 부동산 관리 회사를 위해 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 임대차 계약서, 입주 신청서, 수리 요청서 같은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동할 수 있어야 합니다.

현재 이 시스템은 schema 적합 출력률 99%를 보고하고 있으며, 대부분의 임대차 계약서, 입주 신청서, 수리 요청서가 필드 단위로 높은 확신도 점수를 받고 있습니다.

리뷰어가 매주 수작업으로 확인할 수 있는 것은 고확신도 레코드 중 극히 일부뿐입니다. 하지만 리뷰를 더 줄이기 전에, 운영 환경에서의 오류율을 추정하고 드물게 나타나는 새로운 실패 패턴을 찾아내야 합니다.

어떻게 대응해야 합니까? (2개를 선택하십시오.)

- A. JA: 文書種別と重要フィールドごとに高確信度レコードを抽出し、エラーのパターンを区分別に追跡する。
  - KO: 문서 유형과 핵심 필드별로 고확신도 레코드를 샘플링하고, 오류 패턴을 구분별로 추적합니다.
  - EN: Sample high-confidence records by document type and key field, and track error patterns by segment.
- B. JA: 低確信度のレコードとあいまいな文書だけをレビュー対象にし、高確信度のレコードは検証後も正確だと見なす。
  - KO: 저확신도 레코드와 모호한 문서만 리뷰 대상으로 삼고, 고확신도 레코드는 검증 후에도 정확하다고 간주합니다.
  - EN: Review only low-confidence records and ambiguous documents, and treat high-confidence records as accurate after validation.
- C. JA: 層別の手動サンプリングと並行して自動評価セットを回帰チェックに使い、新しい失敗パターンを加えていく。
  - KO: 층화 수동 샘플링과 병행해 자동 평가 세트를 회귀 점검에 쓰고, 새로운 실패 패턴을 계속 추가해 나갑니다.
  - EN: Use an automated evaluation set for regression checks alongside stratified manual sampling, and keep adding new failure patterns to it.
- D. JA: 高確信度のレコード全体から1つのランダムサンプルを抽出し、週ごとの集計精度だけを経営層に報告する。
  - KO: 고확신도 레코드 전체에서 하나의 무작위 샘플을 뽑고, 주간 집계 정확도만 경영진에게 보고합니다.
  - EN: Draw a single random sample from all high-confidence records, and report only the weekly aggregate accuracy to executives.

## CCAR-F-Udemy03-0015

**JA** あなたは、ソフトウェア開発を加速するためにClaude Codeを使用しています。チームでは、コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行をどのように使い分けるかを理解する必要があります。

あるリリースノート基盤チームには、デプロイのたびに共有の/publishコマンドから呼び出されて、リリースノートを公開するカスタムMCPツールがあります。

対象のCMSスペースがロックされている場合、このツールは現在、「operation failed」というプレーンテキストの文字列を返すだけです。そのため、Claude Codeは開発者に何が起きたかを尋ねる前に、同じ公開処理を何度もリトライしてしまいます。

一時的な失敗からの復旧を維持しつつ、無駄なリトライを最も効果的に防げる変更はどれですか。（2つ選択してください。）

**KO** 당신은 소프트웨어 개발 속도를 높이기 위해 Claude Code를 사용하고 있습니다. 팀은 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 씁니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하고, plan mode와 직접 실행을 어떻게 구분해 쓸지 이해해야 합니다.

한 릴리스 노트 플랫폼 팀에는 배포할 때마다 공유 /publish 명령에서 호출되어 릴리스 노트를 게시하는 custom MCP 도구가 있습니다.

대상 CMS 스페이스가 잠겨 있으면, 이 도구는 현재 "operation failed"라는 일반 텍스트 문자열만 반환합니다. 그래서 Claude Code는 개발자에게 무슨 일이 있었는지 묻기 전에 같은 게시 작업을 여러 번 재시도합니다.

일시적인 실패로부터의 복구는 유지하면서 불필요한 재시도를 가장 효과적으로 막을 수 있는 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 失敗を報告する前に、あらゆる公開処理の失敗を指数バックオフでリトライするようコマンドを設定する。
  - KO: 실패를 보고하기 전에 모든 게시 실패를 exponential backoff로 재시도하도록 명령을 설정합니다.
  - EN: Configure the command to retry every publishing failure with exponential backoff before reporting the failure.
- B. JA: CMSスペースがロックされている場合には成功扱いの空の結果を返し、Claude Codeがそのままワークフローを続けられるようにする。
  - KO: CMS 스페이스가 잠겨 있으면 성공으로 처리되는 빈 결과를 반환해, Claude Code가 workflow를 그대로 이어 가게 합니다.
  - EN: When the CMS space is locked, return an empty result treated as a success so that Claude Code can continue the workflow as is.
- C. JA: isErrorを設定し、ロックと一時的なエラーを区別できる構造化された内容のMCPエラー結果を返す。
  - KO: isError를 설정하고, 잠금과 일시적 오류를 구분할 수 있는 구조화된 내용의 MCP 오류 결과를 반환합니다.
  - EN: Set isError and return an MCP error result with structured content that distinguishes locks from transient errors.
- D. JA: 一時的なエラーはリトライし、ロックによる失敗は開発者に確認するよう/publishコマンドに明記する。
  - KO: 일시적 오류는 재시도하고, 잠금으로 인한 실패는 개발자에게 확인하도록 /publish 명령에 명시합니다.
  - EN: State explicitly in the /publish command that transient errors should be retried and that failures caused by a lock should be raised with the developer.

## CCAR-F-Udemy03-0016

**JA** あなたは、法律事務所向けに、Claudeを使用して契約書の条項抽出システムを構築しています。このシステムは、非定型の契約書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携できる必要があります。

ベンチマークの結果、次のことが分かりました。

独立した複数の抽出対象（indemnification条項、termination条項、liability条項など）を含む長い契約書は、処理が遅い

いずれかのセクションが異常に長いと、最終的なJSONから別の条項が欠落することが多い

各抽出対象は同じ契約書のメタデータと原文を使用しますが、最終的なスキーマ検証の段階までは互いに依存関係を持ちません。

この待ち時間と網羅性の問題に最も効果的に対応できる設計変更はどれですか。（2つ選択してください。）

**KO** 당신은 법률 사무소를 위해 Claude로 계약서 조항 추출 시스템을 구축하고 있습니다. 이 시스템은 정형화되지 않은 계약서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동할 수 있어야 합니다.

벤치마크 결과 다음과 같은 사실이 확인되었습니다.

독립된 여러 추출 대상(indemnification 조항, termination 조항, liability 조항 등)을 포함한 긴 계약서는 처리가 느리다

어느 한 섹션이 비정상적으로 길면, 최종 JSON에서 다른 조항이 빠지는 일이 많다

각 추출 대상은 같은 계약서 metadata와 원문을 사용하지만, 최종 schema 검증 단계 전까지는 서로 의존 관계가 없습니다.

이 대기 시간과 누락 문제에 가장 효과적으로 대응할 수 있는 설계 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 並列でのツール利用を無効化して各条項を固定の順序で処理し、検証結果の注記を最終的なJSONに追記する。
  - KO: 병렬 도구 사용을 비활성화해 각 조항을 고정된 순서로 처리하고, 검증 결과 메모를 최종 JSON에 덧붙입니다.
  - EN: Disable parallel tool use, process each clause in a fixed order, and append validation result notes to the final JSON.
- B. JA: 各抽出タスクから次のタスクを直接呼び出して中間状態を共有させ、完了した順にJSONの断片を返させる。
  - KO: 각 추출 작업이 다음 작업을 직접 호출해 중간 상태를 공유하게 하고, 완료된 순서대로 JSON 조각을 반환하게 합니다.
  - EN: Have each extraction task directly call the next task to share intermediate state, and return JSON fragments in the order they complete.
- C. JA: 各条項の抽出タスクには、契約書のうち担当する条項に関連するセクションだけを渡す。
  - KO: 각 조항 추출 작업에는 계약서 중 담당 조항과 관련된 섹션만 넘깁니다.
  - EN: Give each clause extraction task only the sections of the contract that are relevant to the clause it is responsible for.
- D. JA: 条項ごとの抽出を並列のタスクに分けて共通の契約書メタデータを渡し、最後に統合して検証する。
  - KO: 조항별 추출을 병렬 작업으로 나눠 공통 계약서 metadata를 넘기고, 마지막에 통합해 검증합니다.
  - EN: Split extraction for each clause into parallel tasks that are given the common contract metadata, and then merge and validate the results at the end.

## CCAR-F-Udemy03-0017

**JA** あるEコマースプラットフォームのエンジニアリングチームが、ソフトウェア開発を加速するためにClaude Codeを使用しています。コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っており、カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合しています。プランモードと直接実行をどのように使い分けるかを理解する必要があります。

/release-noteコマンドは、プルリクエストの差分をClaudeに送信し、title、risk_level、testing_summary、breaking_changeといったフィールドを持つ型付きオブジェクトを受け取る必要があります。

プロトタイプでは、ClaudeにJSONを返すよう依頼したうえで、アシスタントのテキストをパースしています。しかし、ClaudeがJSONの前に説明文を含めると、パースが失敗します。

スキーマに基づく抽出という要件を保ったまま、信頼性を最も改善できる実装の変更はどれですか。

**KO** 한 이커머스 플랫폼의 엔지니어링 팀이 소프트웨어 개발 속도를 높이기 위해 Claude Code를 사용하고 있습니다. 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 쓰고 있으며, custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합했습니다. plan mode와 직접 실행을 어떻게 구분해 쓸지 이해해야 합니다.

/release-note 명령은 pull request의 diff를 Claude에 보내고, title, risk_level, testing_summary, breaking_change 같은 필드를 가진 타입이 지정된 객체를 받아야 합니다.

프로토타입에서는 Claude에 JSON을 반환하라고 요청한 뒤 assistant 텍스트를 파싱합니다. 그런데 Claude가 JSON 앞에 설명문을 넣으면 파싱이 실패합니다.

schema 기반 추출이라는 요구 사항을 유지하면서 신뢰성을 가장 크게 개선할 수 있는 구현 변경은 무엇입니까?

- A. JA: リリースノートのフィールド用のinput_schemaを持つクライアント側の抽出ツールを宣言し、そのツール呼び出しを必須にし、tool_useの入力オブジェクトを読み取る。
  - KO: 릴리스 노트 필드용 input_schema를 가진 클라이언트 측 추출 도구를 선언하고, 그 도구 호출을 필수로 지정한 뒤, tool_use의 입력 객체를 읽습니다.
  - EN: Declare a client-side extraction tool with an input_schema for the release note fields, force that tool call to be required, and read the input object of the tool_use block.
- B. JA: Claudeがツールを要求した後にローカルの抽出関数を実行し、tool_resultを送信して、後続のアシスタントのテキストをパースする。
  - KO: Claude가 도구를 요청한 뒤 로컬 추출 함수를 실행하고, tool_result를 보낸 다음, 이어지는 assistant 텍스트를 파싱합니다.
  - EN: After Claude requests a tool, run a local extraction function, send a tool_result, and parse the subsequent assistant text.
- C. JA: リリースノートのスキーマをCLAUDE.mdに保存し、スラッシュコマンドにそれに従うよう求め、最終的なアシスタントのテキストをパースする。
  - KO: 릴리스 노트 schema를 CLAUDE.md에 저장하고, slash command가 그것을 따르도록 요구한 뒤, 최종 assistant 텍스트를 파싱합니다.
  - EN: Store the release note schema in CLAUDE.md, ask the slash command to follow it, and parse the final assistant text.
- D. JA: テキストでJSONを求めるプロンプトを維持し、アシスタントの応答を開き波括弧でプリフィルしたうえで、アシスタントのテキストから最初のバランスの取れたオブジェクトをパースする。
  - KO: 텍스트로 JSON을 요청하는 prompt를 유지하고, assistant 응답을 여는 중괄호로 prefill한 뒤, assistant 텍스트에서 괄호 짝이 맞는 첫 번째 객체를 파싱합니다.
  - EN: Keep the prompt that asks for JSON in text, prefill the assistant response with an opening curly brace, and parse the first balanced object from the assistant text.

## CCAR-F-Udemy03-0018

**JA** あなたは、Claude Agent SDKを使用して、法務調査のためのマルチエージェントシステムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、判例データベースを検索するもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムは論点を調査し、出典を明記した包括的なレポートを作成します。

文書分析サブエージェントは、citation_typeフィールドをJSON Schemaのenumで抽出しています。enumの値は、statute（制定法）、case_law（判例）、regulation（規則）、treatise（学術文献）です。テストでは、次の問題が見つかりました。

あいまいな引用箇所が、無理やりいずれかのカテゴリに分類される

新しい種類の出典で、enumの値の範囲外の値が生成され、下流のバリデーションが失敗することがある

信頼できる分類を維持しながら、スキーマ設計を最も改善できる変更はどれですか。（2つ選択してください。）

**KO** 당신은 Claude Agent SDK로 법무 조사를 위한 multi-agent 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 판례 데이터베이스를 검색하는 것, 문서를 분석하는 것, 조사 결과를 통합하는 것, 보고서를 생성하는 것이 있습니다. 이 시스템은 쟁점을 조사하고, 출처를 명시한 종합 보고서를 작성합니다.

문서 분석 subagent는 citation_type 필드를 JSON Schema의 enum으로 추출합니다. enum 값은 statute(제정법), case_law(판례), regulation(규칙), treatise(학술 문헌)입니다. 테스트에서 다음 문제가 발견되었습니다.

모호한 인용 부분이 억지로 어느 한 카테고리로 분류된다

새로운 종류의 출처에서 enum 값 범위를 벗어난 값이 생성되어, downstream 검증이 실패하는 경우가 있다

신뢰할 수 있는 분류를 유지하면서 schema 설계를 가장 크게 개선할 수 있는 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: enumにunclearとotherを追加してother_detailフィールドも設け、それぞれの使いどころを指示する。
  - KO: enum에 unclear와 other를 추가하고 other_detail 필드도 두며, 각각을 언제 쓸지 지시합니다.
  - EN: Add unclear and other to the enum and also provide an other_detail field, and give instructions on when to use each.
- B. JA: citation_typeからenum制約を取り除き、各サブエージェントに最適だと思うカテゴリラベルを自由に書かせる。
  - KO: citation_type에서 enum 제약을 없애고, 각 subagent가 가장 알맞다고 생각하는 카테고리 라벨을 자유롭게 쓰게 합니다.
  - EN: Remove the enum constraint from citation_type and let each subagent freely write whatever category label it thinks is best.
- C. JA: 現在のenumリストはそのまま維持し、どの引用箇所でも最も近いカテゴリを1つ選ぶようモデルに指示する。
  - KO: 현재 enum 목록은 그대로 유지하고, 어떤 인용 부분이든 가장 가까운 카테고리 하나를 고르도록 모델에 지시합니다.
  - EN: Keep the current enum list as it is, and instruct the model to choose the single closest category for every citation.
- D. JA: otherとunclearの出現頻度を監視し、繰り返し現れる出典の種類を独立したenum値に昇格させる。
  - KO: other와 unclear의 출현 빈도를 모니터링하고, 반복해서 나타나는 출처 유형을 독립된 enum 값으로 승격합니다.
  - EN: Monitor how often other and unclear appear, and promote source types that appear repeatedly to their own enum values.

## CCAR-F-Udemy03-0019

**JA** あなたはゲームスタジオのビルド自動化チームで、開発を加速するためにClaude Codeを使用しています。チームでは、コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行をどのように使い分けるかを理解する必要があります。

あるワークフロースクリプトが、クライアント側で実行されるrun_build_previewツールについて、stop_reason: "tool_use"を含む応答を受け取りました。スクリプトはビルドプレビューの生成に成功していますが、Claudeは結果を解釈せず、同じツールを再度呼び出すよう求め続けています。

次のリクエストで、スクリプトが変更すべきことはどれですか。

**KO** 당신은 게임 스튜디오의 빌드 자동화 팀에서 개발 속도를 높이기 위해 Claude Code를 사용하고 있습니다. 팀은 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 씁니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하고, plan mode와 직접 실행을 어떻게 구분해 쓸지 이해해야 합니다.

한 workflow 스크립트가 클라이언트 측에서 실행되는 run_build_preview 도구에 대해 stop_reason: "tool_use"가 담긴 응답을 받았습니다. 스크립트는 빌드 미리보기 생성에 성공했지만, Claude는 그 결과를 해석하지 않고 같은 도구를 다시 호출해 달라고 계속 요청하고 있습니다.

다음 요청에서 스크립트가 바꿔야 할 것은 무엇입니까?

- A. JA: まずユーザーのテキスト要約を追加し、その同じターンの後半で対応するtool_resultブロックを含める。
  - KO: 먼저 user 텍스트 요약을 추가하고, 같은 turn의 뒷부분에 대응하는 tool_result 블록을 넣습니다.
  - EN: First add a user text summary, and include the corresponding tool_result block later in that same turn.
- B. JA: アシスタントのツール使用ターンを会話履歴に追加し、その直後に対応するtool_resultブロックを含むユーザーターンを追加する。
  - KO: assistant의 도구 사용 turn을 대화 기록에 추가하고, 바로 뒤에 대응하는 tool_result 블록을 담은 user turn을 추가합니다.
  - EN: Append the assistant's tool-use turn to the conversation history, and immediately after it append a user turn that contains the corresponding tool_result block.
- C. JA: ビルドプレビューの出力を含むアシスタントのテキストターンを追加し、続けてClaudeに続行を促すユーザーターンを追加する。
  - KO: 빌드 미리보기 출력을 담은 assistant 텍스트 turn을 추가하고, 이어서 Claude에게 계속 진행하라고 요청하는 user turn을 추가합니다.
  - EN: Append an assistant text turn containing the build preview output, followed by a user turn that prompts Claude to continue.
- D. JA: ビルドプレビューの出力を含むユーザーのテキストターンを追加し、通常のユーザー指示として会話を再開する。
  - KO: 빌드 미리보기 출력을 담은 user 텍스트 turn을 추가하고, 일반적인 사용자 지시로 대화를 재개합니다.
  - EN: Append a user text turn containing the build preview output, and resume the conversation as a normal user instruction.

## CCAR-F-Udemy03-0020

**JA** あなたは、家電メーカー向けに、Claude Agent SDKを使用して競合情報収集システムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、調査結果を統合するもの、報告書を作成するものがあります。このシステムはトピックを調査し、出典を明記した包括的な報告書を作成します。

ある競合製品の調査ワークフローで、探索の段階を終えた後に、次のことが起きています。

後続フェーズのサブエージェントが、前段のサブエージェントが既に完了した検索を繰り返し実行している

特定の情報源をなぜ採用しなかったのかという判断の根拠が、引き継がれていない

コーディネーターは前段のサブエージェントから簡潔な出力しか受け取っておらず、次のフェーズの作業は、まるで探索が行われなかったかのように始まっています。

次のフェーズのサブエージェントを起動する前に、コーディネーターが変更すべきことはどれですか。

**KO** 당신은 가전 제조사를 위해 Claude Agent SDK로 경쟁 정보 수집 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 웹을 검색하는 것, 문서를 분석하는 것, 조사 결과를 통합하는 것, 보고서를 작성하는 것이 있습니다. 이 시스템은 주제를 조사하고, 출처를 명시한 종합 보고서를 작성합니다.

한 경쟁 제품 조사 workflow에서 탐색 단계를 마친 뒤 다음과 같은 일이 일어나고 있습니다.

후속 단계의 subagent가 앞 단계 subagent가 이미 마친 검색을 반복 실행한다

특정 정보원을 왜 채택하지 않았는지에 대한 판단 근거가 넘어가지 않는다

coordinator는 앞 단계 subagent로부터 간결한 출력만 받았으며, 다음 단계의 작업은 마치 탐색이 전혀 없었던 것처럼 시작되고 있습니다.

다음 단계의 subagent를 시작하기 전에 coordinator가 바꿔야 할 것은 무엇입니까?

- A. JA: これまでの探索結果を情報源へのリンク付きの要約に凝縮し、それを次の各サブエージェントへの委任プロンプトに含める。
  - KO: 지금까지의 탐색 결과를 정보원 링크가 달린 요약으로 압축하고, 그것을 다음 각 subagent에 대한 위임 prompt에 포함합니다.
  - EN: Condense the exploration results so far into a summary with links to sources, and include it in the delegation prompt for each next subagent.
- B. JA: 前段の調査結果は最終的な統合プロンプト用に取っておき、次のサブエージェントへの委任は互いに独立したままにする。
  - KO: 앞 단계의 조사 결과는 최종 통합 prompt용으로 남겨 두고, 다음 subagent들에 대한 위임은 서로 독립적으로 유지합니다.
  - EN: Reserve the earlier findings for the final synthesis prompt, and keep delegation to each next subagent independent of one another.
- C. JA: 前段のサブエージェントの完全な会話記録を、詳細を省略せずに次の各委任へ添付する。
  - KO: 앞 단계 subagent의 전체 대화 기록을 세부 사항을 생략하지 않고 다음 각 위임에 첨부합니다.
  - EN: Attach the full conversation transcripts of the earlier subagents to each next delegation, without omitting any detail.
- D. JA: 次のサブエージェントを通常どおり起動し、親の履歴へのアクセスは各サブエージェントの独立したコンテキストウィンドウに任せる。
  - KO: 다음 subagent를 평소처럼 시작하고, 부모 기록에 대한 접근은 각 subagent의 독립된 context window에 맡깁니다.
  - EN: Launch the next subagents as usual, and leave access to the parent's history to each subagent's independent context window.

## CCAR-F-Udemy03-0021

**JA** あなたは、Claude Agent SDKを使用して通信キャリアのアカウントサポートエージェントを構築しています。このエージェントは、解約手続き、請求内容の照会、アカウントの問題など、あいまいさの高いリクエストを処理します。カスタムのModel Context Protocol（MCP）ツール（get_subscriber、lookup_invoice、process_credit、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を達成することです。

カスタマーサポートのエンジニアリングチームは、get_subscriberのための手動のMessages APIクライアントツールループを実装しています。統合テストでは、次の順に処理が進みました。

Claudeがget_subscriberを要求する

アプリケーションがMCPサーバーの呼び出しに成功する

次のClaudeのターンが、加入者情報が存在しないかのように進む

リクエストのトレースを見ると、照会結果はアプリケーションのログに保存されていました。一方、次のMessages APIリクエストには、元のユーザーメッセージと、照会結果を要約した新しいアシスタントのプリフィルだけが含まれていました。

手動のオーケストレーションループに対して行うべき変更はどれですか。（2つ選択してください。）

**KO** 당신은 Claude Agent SDK로 통신사의 계정 지원 agent를 구축하고 있습니다. 이 agent는 해지 절차, 청구 내용 문의, 계정 문제처럼 모호성이 높은 요청을 처리합니다. custom Model Context Protocol(MCP) 도구(get_subscriber, lookup_invoice, process_credit, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation해야 할 시점을 판단하면서 1차 해결률 80% 이상을 달성하는 것입니다.

고객 지원 엔지니어링 팀은 get_subscriber를 위한 수동 Messages API 클라이언트 도구 loop를 구현하고 있습니다. 통합 테스트에서는 다음 순서로 처리가 진행되었습니다.

Claude가 get_subscriber를 요청한다

애플리케이션이 MCP server 호출에 성공한다

다음 Claude turn이 가입자 정보가 없는 것처럼 진행된다

요청 trace를 보면 조회 결과는 애플리케이션 로그에 저장되어 있었습니다. 반면 다음 Messages API 요청에는 원래의 user 메시지와, 조회 결과를 요약한 새로운 assistant prefill만 들어 있었습니다.

수동 orchestration loop에 해야 할 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 照会結果を、発行されたtool_use_idに対応するtool_resultのcontentに入れて返す。
  - KO: 조회 결과를 발급된 tool_use_id에 대응하는 tool_result의 content에 넣어 반환합니다.
  - EN: Return the lookup result in the content of a tool_result that corresponds to the issued tool_use_id.
- B. JA: アシスタントのtool_use応答を残し、続けて対応するtool_resultを含むユーザーメッセージを送る。
  - KO: assistant의 tool_use 응답을 남겨 두고, 이어서 대응하는 tool_result를 담은 user 메시지를 보냅니다.
  - EN: Keep the assistant's tool_use response, and follow it with a user message containing the corresponding tool_result.
- C. JA: 照会結果を返す前にユーザーへの確認メッセージを1つ挟み、その次のメッセージで照会結果を含めて送る。
  - KO: 조회 결과를 반환하기 전에 사용자에게 보내는 확인 메시지를 하나 끼워 넣고, 그다음 메시지에 조회 결과를 담아 보냅니다.
  - EN: Insert a single confirmation message to the user before returning the lookup result, and include the lookup result in the message after that.
- D. JA: 照会結果を要約したアシスタントメッセージを追加し、そのプリフィルした要約の続きからClaudeに生成させる。
  - KO: 조회 결과를 요약한 assistant 메시지를 추가하고, prefill한 그 요약에 이어서 Claude가 생성하게 합니다.
  - EN: Add an assistant message summarizing the lookup result, and have Claude generate a continuation from that prefilled summary.

## CCAR-F-Udemy03-0022

**JA** あなたはフィンテック企業のエンジニアリングチームで、決済SDKのアップグレードに向けた開発を加速するためにClaude Codeを使用しています。チームでは、コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行をどのように使い分けるかを理解する必要があります。

このチームは、ドキュメントの調査を別のClaude Codeサブエージェントに委任しています。最近まとめた決済SDKのアップグレードガイドでは、2021年の互換性に関する注意書きと2024年のリリース告知が、どちらも現在の情報として同等に扱われてしまいました。親の会話が、各サブエージェントから短い要約しか受け取っていなかったためです。

今後生成されるドキュメントで、情報の新旧を正しく扱えるようにするために最も直接的に効く変更はどれですか。（2つ選択してください。）

**KO** 당신은 핀테크 회사의 엔지니어링 팀에서 결제 SDK 업그레이드를 위한 개발 속도를 높이려고 Claude Code를 사용하고 있습니다. 팀은 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 씁니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합하고, plan mode와 직접 실행을 어떻게 구분해 쓸지 이해해야 합니다.

이 팀은 문서 조사를 별도의 Claude Code subagent에게 위임하고 있습니다. 최근 정리한 결제 SDK 업그레이드 가이드에서는 2021년의 호환성 관련 주의 사항과 2024년의 릴리스 공지가 둘 다 똑같이 현재 정보로 취급되었습니다. 부모 대화가 각 subagent로부터 짧은 요약만 받았기 때문입니다.

앞으로 생성되는 문서에서 정보의 신구를 올바르게 다루게 하는 데 가장 직접적으로 효과가 있는 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 情報源の日付を比べて矛盾したら新しい所見を優先するよう、CLAUDE.mdで親エージェントに指示する。
  - KO: 정보원의 날짜를 비교해 서로 모순되면 더 새로운 결과를 우선하도록 CLAUDE.md에서 부모 agent에게 지시합니다.
  - EN: Instruct the parent agent in CLAUDE.md to compare source dates and prefer the newer finding when they conflict.
- B. JA: 各調査サブエージェントに、所見ごとの情報源の日付と日付の根拠を含むJSONを返させる。
  - KO: 각 조사 subagent가 결과마다 정보원의 날짜와 그 날짜의 근거를 담은 JSON을 반환하게 합니다.
  - EN: Have each research subagent return JSON that includes the source date for each finding and the basis for that date.
- C. JA: 要約された所見同士が矛盾して見える場合に限り、親エージェントが各サブエージェントに散文での再要約を求める。
  - KO: 요약된 결과끼리 모순돼 보일 때에만 부모 agent가 각 subagent에게 산문으로 다시 요약해 달라고 요청합니다.
  - EN: Only when summarized findings appear to contradict each other, have the parent agent ask each subagent to re-summarize in prose.
- D. JA: 調査に使う情報源で引用機能を有効にし、引用された箇所の位置情報から時期の文脈を補わせる。
  - KO: 조사에 쓰는 정보원에서 citations 기능을 활성화하고, 인용된 부분의 위치 정보로 시기 맥락을 보완하게 합니다.
  - EN: Enable the citations feature on the sources used for research, and use the location information of the cited passages to supply temporal context.

## CCAR-F-Udemy03-0023

**JA** あなたは、Claude Agent SDKを使用してITヘルプデスクの解決エージェントを構築しています。このエージェントは、インシデント報告、ライセンスの不具合、アクセス権限の問題など、あいまいさの高いリクエストを処理します。カスタムのModel Context Protocol（MCP）ツール（get_employee、lookup_ticket、resolve_access_request、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を達成することです。

本番環境でのテストでは、エージェントの一次分析が、周辺的なものも含めて、考えられるインシデントやアクセスの問題をすべて列挙しています。レビュー担当者からは、すべての結果が同じ優先度で届くため、それぞれが次のどれに当たるかを判断できないという苦情が出ています。

自動で解決するもの

人によるレビューに回すもの

傾向分析にだけ使うもの

幅広い網羅性を保ったまま、キャリブレーションされた基準でレビューを振り分けられるようにする変更はどれですか。（2つ選択してください。）

**KO** 당신은 Claude Agent SDK로 IT 헬프데스크 해결 agent를 구축하고 있습니다. 이 agent는 인시던트 보고, 라이선스 오류, 접근 권한 문제처럼 모호성이 높은 요청을 처리합니다. custom Model Context Protocol(MCP) 도구(get_employee, lookup_ticket, resolve_access_request, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation해야 할 시점을 판단하면서 1차 해결률 80% 이상을 달성하는 것입니다.

운영 환경 테스트에서 agent의 1차 분석은 주변적인 것까지 포함해 생각할 수 있는 인시던트와 접근 문제를 모두 나열하고 있습니다. 리뷰 담당자들은 모든 결과가 같은 우선순위로 들어오기 때문에 각각이 다음 중 어디에 해당하는지 판단할 수 없다고 불만을 제기하고 있습니다.

자동으로 해결할 것

사람의 리뷰로 넘길 것

경향 분석에만 쓸 것

폭넓은 커버리지를 유지하면서, calibration된 기준으로 리뷰를 분류할 수 있게 하는 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 各所見に確信度と重大度を付ける、スキーマで制約した検証パスを別に実行する。
  - KO: 각 결과에 확신도와 심각도를 붙이는, schema로 제약한 검증 패스를 별도로 실행합니다.
  - EN: Run a separate schema-constrained verification pass that assigns a confidence and severity to each finding.
- B. JA: 確信度と重大度の組み合わせを振り分け先に対応させる、明示的な振り分けルールを定める。
  - KO: 확신도와 심각도의 조합을 처리 경로에 대응시키는 명시적인 분류 규칙을 정합니다.
  - EN: Define explicit routing rules that map combinations of confidence and severity to routing destinations.
- C. JA: 一次分析のパスには、顧客影響の重大度ラベルを付けた高確信度の問題だけを返すよう指示する。
  - KO: 1차 분석 패스에는 고객 영향 심각도 라벨을 붙인 고확신도 문제만 반환하도록 지시합니다.
  - EN: Instruct the initial analysis pass to return only high-confidence issues labeled with a customer-impact severity.
- D. JA: Messages APIの各レスポンスに含まれる確信度の値を読み取り、それを基準にケースを振り分ける。
  - KO: Messages API의 각 응답에 포함된 확신도 값을 읽어, 그것을 기준으로 케이스를 분류합니다.
  - EN: Read the confidence value included in each Messages API response and use it as the criterion for routing cases.

## CCAR-F-Udemy03-0024

**JA** ある製薬会社の競合分析チームが、Claude Agent SDKを使用してマルチエージェントリサーチシステムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

パイロット期間中に、あるエンジニアから、サブエージェント同士が中間的な調査結果を直接送り合えるようにする案が出ました。そうすれば、コーディネーターが次の委任を出すのを待たずに、より速く連携できるという理由です。

このチームが採用すべき設計はどれですか。

**KO** 한 제약회사의 경쟁 분석 팀이 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 웹을 검색하는 것, 문서를 분석하는 것, 조사 결과를 통합하는 것, 보고서를 생성하는 것이 있습니다. 이 시스템은 주제를 조사하고, 출처를 명시한 종합 보고서를 작성합니다.

파일럿 기간 중 한 엔지니어가 subagent끼리 중간 조사 결과를 직접 주고받게 하자는 안을 냈습니다. 그러면 coordinator가 다음 위임을 내릴 때까지 기다리지 않고 더 빠르게 협업할 수 있다는 이유입니다.

이 팀이 채택해야 할 설계는 무엇입니까?

- A. JA: サブエージェントが自由に更新できる共有スクラッチパッドを作成し、最終的な矛盾の解消はレポート生成サブエージェントに任せる。
  - KO: subagent가 자유롭게 갱신할 수 있는 공유 scratchpad를 만들고, 최종적인 모순 해소는 보고서 생성 subagent에 맡깁니다.
  - EN: Create a shared scratchpad that subagents can update freely, and leave the final resolution of contradictions to the report generation subagent.
- B. JA: 後続作業はコーディネーターを経由させ、追加の委任に対してはサブエージェントに構造化された最終結果を返させるようにする。
  - KO: 후속 작업은 coordinator를 거치게 하고, 추가 위임에 대해서는 subagent가 구조화된 최종 결과를 반환하게 합니다.
  - EN: Route follow-up work through the coordinator, and have subagents return structured final results for additional delegations.
- C. JA: サブエージェント同士が中間的な調査結果を交換し、互いに直接作業を依頼できるようにするピアメッセージングツールを追加する。
  - KO: subagent끼리 중간 조사 결과를 교환하고 서로 직접 작업을 요청할 수 있게 하는 peer 메시징 도구를 추가합니다.
  - EN: Add a peer messaging tool that lets subagents exchange intermediate findings and request work from each other directly.
- D. JA: すべてのサブエージェントに同じ会話履歴全体を与え、次にどのサブエージェントが動くべきかを各自が判断できるようにする。
  - KO: 모든 subagent에 같은 전체 대화 기록을 주어, 다음에 어떤 subagent가 움직여야 할지 각자 판단하게 합니다.
  - EN: Give every subagent the same full conversation history so that each can decide which subagent should act next.

## CCAR-F-Udemy03-0025

**JA** あなたは、Claudeを使用して構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携できる必要があります。

Claudeに抽出スキーマとバリデーションのリトライロジックを生成させましたが、その後も、見つけにくい欠陥が下流のテストまで残り続けています。特に多いのは、あいまいなフィールドと合計値の不整合です。

現在のレビューは、実装を設計してその判断を正当化したのと同じ長いセッションの中で、そのまま行われています。

レビューのアーキテクチャを最も効果的に改善できる変更はどれですか。

**KO** 당신은 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동할 수 있어야 합니다.

Claude에게 추출 schema와 검증 재시도 로직을 생성하게 했지만, 그 뒤에도 찾기 어려운 결함이 downstream 테스트 단계까지 계속 남아 있습니다. 특히 많은 것은 모호한 필드와 합계값 불일치입니다.

현재 리뷰는 구현을 설계하고 그 판단을 정당화했던 바로 그 긴 session 안에서 그대로 이루어지고 있습니다.

리뷰 아키텍처를 가장 효과적으로 개선할 수 있는 변경은 무엇입니까?

- A. JA: 新しいコンテキストで別のClaudeセッションを実行し、要件と差分にレビューのチェックリストを添えて渡す。
  - KO: 새 context에서 별도의 Claude session을 실행하고, 요구 사항과 diff에 리뷰 체크리스트를 곁들여 넘깁니다.
  - EN: Run a separate Claude session in a fresh context, giving it the requirements and the diff along with a review checklist.
- B. JA: 生成中のセッションで/compactを使用し、その後スキーマとリトライロジックの監査をそのセッションに依頼する。
  - KO: 생성 중인 session에서 /compact를 사용한 뒤, schema와 재시도 로직의 감사를 그 session에 요청합니다.
  - EN: Use /compact in the generating session, then ask that session to audit the schema and retry logic.
- C. JA: 実装の設計根拠を再読させたうえで、生成を行ったClaudeセッション自身にコードをレビューさせる。
  - KO: 구현의 설계 근거를 다시 읽게 한 뒤, 생성을 맡았던 Claude session이 직접 코드를 리뷰하게 합니다.
  - EN: Have the Claude session that did the generation review the code itself after re-reading the design rationale for the implementation.
- D. JA: 生成用プロンプトにfew-shotの抽出例をさらに追加し、別のレビュー工程は省略する。
  - KO: 생성용 prompt에 few-shot 추출 예시를 더 추가하고, 별도의 리뷰 단계는 생략합니다.
  - EN: Add more few-shot extraction examples to the generation prompt and skip the separate review step.

## CCAR-F-Udemy03-0026

**JA** あなたは、Claude Agent SDKを使用して、通信キャリア向けのカスタマーサポート解決エージェントを構築しています。このエージェントは、料金プランの変更、請求の誤り、契約内容の確認など、あいまいさの高い依頼を処理します。カスタムのModel Context Protocol（MCP）ツール（get_subscriber、lookup_billing、apply_credit、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を達成することです。

あるオンライン通信キャリアのサポートエンジニアリングチームは、プラン変更ロジックの変更をレビューする再利用可能な/plan-change-auditワークフローを、Claude Codeに追加したいと考えています。このワークフローの要件は次のとおりです。

リポジトリと一緒にバージョン管理される

チェックリストとサンプルの対応記録を、補助ファイルとして含む

ワークフローの実行中は、ファイル変更ツールやシェルコマンドを使用できないようにする

これらの要件に最も適した実装はどれですか。

**KO** 당신은 Claude Agent SDK로 통신사용 고객 지원 해결 agent를 구축하고 있습니다. 이 agent는 요금제 변경, 청구 오류, 계약 내용 확인처럼 모호성이 높은 요청을 처리합니다. custom Model Context Protocol(MCP) 도구(get_subscriber, lookup_billing, apply_credit, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation해야 할 시점을 판단하면서 1차 해결률 80% 이상을 달성하는 것입니다.

한 온라인 통신사의 지원 엔지니어링 팀은 요금제 변경 로직의 변경을 리뷰하는 재사용 가능한 /plan-change-audit workflow를 Claude Code에 추가하려고 합니다. 이 workflow의 요구 사항은 다음과 같습니다.

저장소와 함께 버전 관리된다

체크리스트와 샘플 응대 기록을 보조 파일로 포함한다

workflow 실행 중에는 파일 변경 도구나 셸 명령을 쓸 수 없게 한다

이 요구 사항에 가장 적합한 구현은 무엇입니까?

- A. JA: ~/.claude/skills/plan-change-audit/SKILL.mdを作成し、そこから補助ファイルを参照させ、disable-model-invocation: trueを設定する。
  - KO: ~/.claude/skills/plan-change-audit/SKILL.md를 만들어 거기서 보조 파일을 참조하게 하고, disable-model-invocation: true를 설정합니다.
  - EN: Create ~/.claude/skills/plan-change-audit/SKILL.md, reference the supporting files from it, and set disable-model-invocation: true.
- B. JA: .claude/skills/plan-change-audit/SKILL.mdを作成し、補助ファイルを参照させ、disallowed-toolsにWrite Edit NotebookEdit Bashを設定する。
  - KO: .claude/skills/plan-change-audit/SKILL.md를 만들어 보조 파일을 참조하게 하고, disallowed-tools에 Write Edit NotebookEdit Bash를 설정합니다.
  - EN: Create .claude/skills/plan-change-audit/SKILL.md, reference the supporting files, and set disallowed-tools to Write Edit NotebookEdit Bash.
- C. JA: .claude/skills/plan-change-audit/SKILL.mdを作成し、そこから補助ファイルを参照させ、allowed-toolsをReadとGrepに設定する。
  - KO: .claude/skills/plan-change-audit/SKILL.md를 만들어 거기서 보조 파일을 참조하게 하고, allowed-tools를 Read와 Grep으로 설정합니다.
  - EN: Create .claude/skills/plan-change-audit/SKILL.md, reference the supporting files from it, and set allowed-tools to Read and Grep.
- D. JA: .claude/commands/plan-change-audit.mdを作成して補助ファイルへのリンクを含め、allowed-toolsをReadとGrepに設定する。
  - KO: .claude/commands/plan-change-audit.md를 만들어 보조 파일 링크를 넣고, allowed-tools를 Read와 Grep으로 설정합니다.
  - EN: Create .claude/commands/plan-change-audit.md including links to the supporting files, and set allowed-tools to Read and Grep.

## CCAR-F-Udemy03-0027

**JA** ある家電量販店が、Claude Agent SDKを使用してカスタマーサポート解決エージェントを構築しています。このエージェントは、返品、料金請求に関する問い合わせ、アカウントの問題など、あいまいさの高い依頼を処理します。カスタムのModel Context Protocol（MCP）ツール（get_customer、lookup_order、process_refund、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を達成することです。

本番環境のトレースによると、顧客が注文を間接的に説明した場合、エージェントは「去年の冬に買ったジャケット」や「カードに来た請求」のようなあいまいな表現を、そのままlookup_orderに送っています。一方、バックエンドが最もよく機能するのは、次のような入力です。

正確な注文ID

確認済みの顧客IDと日付範囲

メールの受領確認への参照

あいまいな一致のときは、当て推量で返金処理をするのではなく、確認の依頼かエスカレーションにつなげる必要があります。また、バックエンドの仕様は今回のスプリント中には変更できません。

このチームが最初に行うべきツール設計上の変更はどれですか。（2つ選択してください。）

**KO** 한 가전 양판점이 Claude Agent SDK로 고객 지원 해결 agent를 구축하고 있습니다. 이 agent는 반품, 요금 청구 문의, 계정 문제처럼 모호성이 높은 요청을 처리합니다. custom Model Context Protocol(MCP) 도구(get_customer, lookup_order, process_refund, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation해야 할 시점을 판단하면서 1차 해결률 80% 이상을 달성하는 것입니다.

운영 환경 trace를 보면, 고객이 주문을 간접적으로 설명할 때 agent는 "작년 겨울에 산 재킷"이나 "카드로 청구된 금액" 같은 모호한 표현을 그대로 lookup_order에 보내고 있습니다. 반면 백엔드가 가장 잘 동작하는 입력은 다음과 같습니다.

정확한 주문 ID

확인된 고객 ID와 날짜 범위

이메일 수령 확인에 대한 참조

일치 여부가 모호할 때는 추측으로 환불을 처리하지 말고 확인 요청이나 escalation으로 이어져야 합니다. 또한 백엔드 사양은 이번 스프린트 중에는 바꿀 수 없습니다.

이 팀이 가장 먼저 해야 할 도구 설계상의 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: システムプロンプトに成功した注文検索の例をさらに追加しつつ、ツールのメタデータは最小限に保つ。
  - KO: system prompt에 성공한 주문 검색 예시를 더 추가하되, 도구의 metadata는 최소한으로 유지합니다.
  - EN: Add more successful order lookup examples to the system prompt while keeping the tool metadata minimal.
- B. JA: 注文関連のやり取りではtool_choiceでlookup_orderの使用を強制し、エージェントに一致を注意深く確認するよう求める。
  - KO: 주문 관련 대화에서는 tool_choice로 lookup_order 사용을 강제하고, agent에게 일치 여부를 신중히 확인하도록 요구합니다.
  - EN: Force the use of lookup_order with tool_choice for order-related interactions, and ask the agent to verify matches carefully.
- C. JA: lookup_orderに、渡す識別子がどの受け付け形式に当たるかを示す必須パラメータを追加する。
  - KO: lookup_order에, 넘기는 식별자가 어느 허용 형식에 해당하는지 나타내는 필수 파라미터를 추가합니다.
  - EN: Add a required parameter to lookup_order that indicates which accepted format the supplied identifier corresponds to.
- D. JA: ツールと各フィールドの説明に、受け付け可能な入力形式と入力例、エッジケースや利用範囲を明記する。
  - KO: 도구와 각 필드의 설명에 허용되는 입력 형식과 입력 예시, edge case와 사용 범위를 명시합니다.
  - EN: Document the accepted input formats and examples, edge cases, and scope of use in the descriptions of the tool and of each field.

## CCAR-F-Udemy03-0028

**JA** あなたは、Claude Agent SDKを使用して、製薬会社向けの規制動向リサーチシステムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、規制関連文書を分析するもの、調査結果を統合するもの、報告書を作成するものがあります。このシステムはトピックを調査し、出典を明記した包括的な報告書を作成します。

このシステムには、報告書の中でGitHubのIssueを参照する次の機能が必要です。

関連するIssueを検索する

Issueの内容を読み取る

引用したIssue番号を報告書にリンクする

加えて、Issueのラベルを社内の審査ステージや報告書のセクションに対応付ける、独自の承認準備状況ワークフローも必要です。

推奨すべき構成はどれですか。

**KO** 당신은 제약회사를 위해 Claude Agent SDK로 규제 동향 리서치 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 웹을 검색하는 것, 규제 관련 문서를 분석하는 것, 조사 결과를 통합하는 것, 보고서를 작성하는 것이 있습니다. 이 시스템은 주제를 조사하고, 출처를 명시한 종합 보고서를 작성합니다.

이 시스템에는 보고서에서 GitHub Issue를 참조하는 다음 기능이 필요합니다.

관련 Issue를 검색한다

Issue 내용을 읽는다

인용한 Issue 번호를 보고서에 링크한다

이와 함께, Issue 라벨을 사내 심사 단계와 보고서 섹션에 대응시키는 자체 승인 준비 상태 workflow도 필요합니다.

권장해야 할 구성은 무엇입니까?

- A. JA: 標準的なIssue操作は保守されているGitHub用MCPサーバーを使い、独自のワークフローには専用のカスタムMCPサーバーを作る。
  - KO: 표준적인 Issue 조작에는 유지보수되고 있는 GitHub용 MCP server를 쓰고, 자체 workflow에는 전용 custom MCP server를 만듭니다.
  - EN: Use a maintained GitHub MCP server for standard issue operations, and build a dedicated custom MCP server for the custom workflow.
- B. JA: 各実行前にGitHubのIssueを静的ファイルへエクスポートしておき、文書分析サブエージェントにそのエクスポート済みファイルを読み取らせる。
  - KO: 실행할 때마다 미리 GitHub Issue를 정적 파일로 export해 두고, 문서 분석 subagent가 export된 파일을 읽게 합니다.
  - EN: Export GitHub issues to static files before each run, and have the document analysis subagent read the exported files.
- C. JA: コーディネーターのプロンプトにGitHubに関する指示を追加し、ウェブ検索サブエージェントに通常の検索を通じてIssueページを探させる。
  - KO: coordinator의 prompt에 GitHub 관련 지시를 추가하고, 웹 검색 subagent가 일반 검색으로 Issue 페이지를 찾게 합니다.
  - EN: Add GitHub instructions to the coordinator's prompt, and have the web search subagent find issue pages through ordinary search.
- D. JA: GitHub Issueの操作を再実装し、独自の承認準備状況ワークフローも同じインターフェースに含めた、1つのカスタムMCPサーバーを構築する。
  - KO: GitHub Issue 조작을 다시 구현하고 자체 승인 준비 상태 workflow도 같은 인터페이스에 넣은, 하나의 custom MCP server를 구축합니다.
  - EN: Build a single custom MCP server that reimplements GitHub issue operations and also includes the custom approval readiness workflow in the same interface.

## CCAR-F-Udemy03-0029

**JA** あなたは、Claudeを使用して構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSON（JavaScript Object Notation）スキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携できる必要があります。

リポジトリには見積書、発注書、保証請求のパッケージがあり、それぞれ抽出上のエッジケースと検証の慣例が異なります。開発者は通常、編集対象のパッケージからClaude Codeを起動しています。

メンテナーは、すべてのパッケージに全ドメインのガイダンスを継承させずに、パッケージ固有の標準を自動的に読み込ませたいと考えています。

このワークフローに最も適した設定はどれですか。

**KO** 당신은 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON(JavaScript Object Notation) schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동할 수 있어야 합니다.

저장소에는 견적서, 발주서, 보증 청구 패키지가 있으며, 각각 추출상의 edge case와 검증 관례가 다릅니다. 개발자는 보통 편집할 패키지에서 Claude Code를 실행합니다.

메인테이너는 모든 패키지가 전체 도메인의 가이드를 물려받지 않게 하면서, 패키지별 표준을 자동으로 불러오게 하고 싶어 합니다.

이 workflow에 가장 적합한 설정은 무엇입니까?

- A. JA: 各パッケージの標準を別々のMarkdownファイルに保存し、インポートする代わりにパッケージのREADMEからリンクする。
  - KO: 각 패키지의 표준을 별도의 Markdown 파일에 저장하고, import하는 대신 패키지 README에서 링크합니다.
  - EN: Store each package's standards in a separate Markdown file, and link to them from the package README instead of importing them.
- B. JA: ドメインごとの標準をルートのCLAUDE.mdに集約し、見積書・発注書・保証請求ごとに見出しで区切る。
  - KO: 도메인별 표준을 루트 CLAUDE.md에 모으고, 견적서·발주서·보증 청구별로 제목을 달아 구분합니다.
  - EN: Consolidate the standards for every domain in the root CLAUDE.md, separated by headings for quotes, purchase orders, and warranty claims.
- C. JA: 共通の慣例はルートのCLAUDE.mdに残し、各パッケージのCLAUDE.mdで関連する標準だけを@インポートする。
  - KO: 공통 관례는 루트 CLAUDE.md에 두고, 각 패키지의 CLAUDE.md에서 관련 표준만 @import합니다.
  - EN: Keep common conventions in the root CLAUDE.md, and have each package's CLAUDE.md use @imports for only the relevant standards.
- D. JA: 各パッケージのCLAUDE.mdの中で、フェンス付きコードブロックの中に各標準ファイルへの@インポートを配置する。
  - KO: 각 패키지의 CLAUDE.md 안에서, fenced code block 안에 각 표준 파일에 대한 @import를 둡니다.
  - EN: In each package's CLAUDE.md, place @imports of each standard file inside a fenced code block.

## CCAR-F-Udemy03-0030

**JA** あるゲノム解析プラットフォーム企業が、Claudeを使用して構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSON（JavaScript Object Notation）スキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携できる必要があります。

このチームは、42ファイルから成る抽出パイプラインを、1回のパスでまとめてレビューするようClaudeに依頼しています。このパイプラインには、パーサー、正規化ルール、JSONスキーマ、バリデーター、下流へのマッピングコードが含まれます。

最近のレビューは一貫性に欠けています。明白な欠陥が見つかることもある一方で、パイプラインのどの部分がレビューの中心になるかによって、別の問題が見落とされることがあります。

このチームが採用すべきレビュー設計はどれですか。

**KO** 한 유전체 분석 플랫폼 회사가 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON(JavaScript Object Notation) schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동할 수 있어야 합니다.

이 팀은 42개 파일로 이루어진 추출 pipeline을 한 번의 패스로 몰아서 리뷰하도록 Claude에 요청하고 있습니다. 이 pipeline에는 파서, 정규화 규칙, JSON schema, validator, downstream 매핑 코드가 들어 있습니다.

최근 리뷰는 일관성이 없습니다. 명백한 결함을 찾아낼 때도 있지만, pipeline의 어느 부분이 리뷰의 중심이 되느냐에 따라 다른 문제를 놓치기도 합니다.

이 팀이 채택해야 할 리뷰 설계는 무엇입니까?

- A. JA: すべてのファイルとすべての要件を含む、より大きな1つのレビュープロンプトを実行し、あらゆる欠陥を見つけ出すようより厳格な指示を加える。
  - KO: 모든 파일과 모든 요구 사항을 담은 더 큰 리뷰 prompt 하나를 실행하고, 모든 결함을 찾아내라는 더 엄격한 지시를 추가합니다.
  - EN: Run a single, larger review prompt that includes all files and all requirements, and add stricter instructions to find every defect.
- B. JA: 複数の独立したパイプライン全体のレビューを並列に実行し、少なくとも2つのレビュー出力に共通して現れた指摘事項だけを統合する。
  - KO: pipeline 전체를 대상으로 한 독립적인 리뷰를 여러 개 병렬로 실행하고, 최소 두 개의 리뷰 출력에 공통으로 나타난 지적 사항만 통합합니다.
  - EN: Run multiple independent whole-pipeline reviews in parallel, and merge only the findings that appear in at least two of the review outputs.
- C. JA: パース処理から検証・下流へのエクスポートまで抽出フィールドを追跡する、ファイル横断の統合レビューだけを実行する。
  - KO: 파싱부터 검증·downstream export까지 추출 필드를 추적하는, 파일 간 통합 리뷰만 실행합니다.
  - EN: Run only a cross-file integration review that traces the extracted fields from parsing through validation to downstream export.
- D. JA: まず焦点を絞ったファイル単位のレビューパスを実行し、その後、要約された局所的な指摘事項とファイル横断のデータフローに対して別の統合パスを実行する。
  - KO: 먼저 범위를 좁힌 파일 단위 리뷰 패스를 실행하고, 그 뒤 요약된 국소적 지적 사항과 파일 간 데이터 흐름을 대상으로 별도의 통합 패스를 실행합니다.
  - EN: First run focused per-file review passes, then run a separate integration pass over the summarized local findings and the cross-file data flow.

## CCAR-F-Udemy03-0031

**JA** ある海運物流会社が、Claudeを使用して構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSON（JavaScript Object Notation）スキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携できる必要があります。

このチームは、Messages APIのMCPコネクタを使い、次の3つの独立したMCPサーバーに接続しています。

スキーマ選択

エンティティのエンリッチメント

下流キューへの配信

文書ごとに使う連携を1つ事前に選ぶのではなく、1回の抽出リクエストの中で、3つの連携すべてから必要に応じてツールを選べるようにしたいと考えています。

このチームが実装すべきものはどれですか。

**KO** 한 해운 물류 회사가 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON(JavaScript Object Notation) schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동할 수 있어야 합니다.

이 팀은 Messages API의 MCP connector를 사용해 다음 세 개의 독립된 MCP server에 연결하고 있습니다.

schema 선택

엔티티 enrichment

downstream 큐로의 전달

문서마다 쓸 연동 하나를 미리 고르는 대신, 한 번의 추출 요청 안에서 세 연동 모두의 도구를 필요에 따라 고를 수 있게 하고 싶어 합니다.

이 팀은 무엇을 구현해야 합니까?

- A. JA: mcp_serversに3つのサーバーを定義し、tools内にサーバーごとのmcp_toolsetを1つずつ追加する。
  - KO: mcp_servers에 세 server를 정의하고, tools 안에 server마다 mcp_toolset을 하나씩 추가합니다.
  - EN: Define the three servers in mcp_servers, and add one mcp_toolset per server in tools.
- B. JA: 3つの別々のリクエストを実行し、それぞれに1つのmcp_toolsetを設定して、抽出したJSONをリクエスト間で手動で受け渡す。
  - KO: 별도의 요청 세 개를 실행해 각각에 mcp_toolset을 하나씩 설정하고, 추출한 JSON을 요청 사이에서 수동으로 주고받습니다.
  - EN: Run three separate requests, each with one mcp_toolset, and manually pass the extracted JSON between requests.
- C. JA: 1つの汎用プロキシツールを作成して各操作をそれ経由でルーティングし、サーバー固有のツールのメタデータをClaudeから隠す。
  - KO: 범용 프록시 도구 하나를 만들어 모든 작업을 그 도구로 routing하고, server별 도구 metadata는 Claude에게 숨깁니다.
  - EN: Create one generic proxy tool and route each operation through it, hiding the server-specific tool metadata from Claude.
- D. JA: mcp_serversに3つのサーバーを定義し、mcp_toolsetのエントリは省略して、接続先からツールが自動で検出されることに頼る。
  - KO: mcp_servers에 세 server를 정의하되 mcp_toolset 항목은 생략하고, 연결된 곳에서 도구가 자동으로 발견되는 데 의존합니다.
  - EN: Define the three servers in mcp_servers, omit the mcp_toolset entries, and rely on tools being discovered automatically from the connections.

## CCAR-F-Udemy03-0032

**JA** あなたは、物流会社向けに、Claude Agent SDKを使用して書類分類・抽出システムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、調査結果を統合するもの、報告書を作成するものがあります。このシステムはトピックを調査し、出典を明記した包括的な報告書を作成します。

評価では、文書分析サブエージェントを、AnthropicのクライアントSDKからClaude Messages APIのツール使用で呼び出しています。このサブエージェントは、次の3つの抽出スキーマのいずれかに対応するツール呼び出しを返す必要があります。

extract_invoice

extract_purchase_order

extract_shipping_manifest

文書の種類は事前には分かりません。しかし実行の6%で、サブエージェントがスキーマ用のツールを呼び出さずに会話的な要約を返してしまい、コーディネーターが引用に必要なメタデータを取得できなくなっています。

特定のスキーマに固定せずに、構造化された抽出を最も効果的に強制できる変更はどれですか。

**KO** 당신은 물류 회사를 위해 Claude Agent SDK로 서류 분류·추출 시스템을 구축하고 있습니다. coordinator agent가 전문 subagent에게 작업을 위임합니다. subagent로는 웹을 검색하는 것, 문서를 분석하는 것, 조사 결과를 통합하는 것, 보고서를 작성하는 것이 있습니다. 이 시스템은 주제를 조사하고, 출처를 명시한 종합 보고서를 작성합니다.

평가에서는 문서 분석 subagent를 Anthropic의 클라이언트 SDK에서 Claude Messages API의 tool use로 호출하고 있습니다. 이 subagent는 다음 세 추출 schema 중 하나에 해당하는 도구 호출을 반환해야 합니다.

extract_invoice

extract_purchase_order

extract_shipping_manifest

문서 종류는 미리 알 수 없습니다. 그런데 실행의 6%에서 subagent가 schema용 도구를 호출하지 않고 대화형 요약을 반환해, coordinator가 인용에 필요한 metadata를 얻지 못하고 있습니다.

특정 schema에 고정하지 않으면서 구조화된 추출을 가장 효과적으로 강제할 수 있는 변경은 무엇입니까?

- A. JA: tool_choiceを{"type": "auto"}に設定し、すべての抽出ツールを提供する。
  - KO: tool_choice를 {"type": "auto"}로 설정하고, 모든 추출 도구를 제공합니다.
  - EN: Set tool_choice to {"type": "auto"} and provide all extraction tools.
- B. JA: toolsを省略し、望ましいJSONの書き出し部分をアシスタント応答にプリフィルする。
  - KO: tools를 생략하고, 원하는 JSON의 시작 부분을 assistant 응답에 prefill합니다.
  - EN: Omit tools and prefill the assistant response with the beginning of the desired JSON.
- C. JA: tool_choiceを{"type": "any"}に設定し、すべての抽出ツールを提供する。
  - KO: tool_choice를 {"type": "any"}로 설정하고, 모든 추출 도구를 제공합니다.
  - EN: Set tool_choice to {"type": "any"} and provide all extraction tools.
- D. JA: すべての文書に対してtool_choiceを{"type": "tool", "name": "extract_invoice"}に固定する。
  - KO: 모든 문서에 대해 tool_choice를 {"type": "tool", "name": "extract_invoice"}로 고정합니다.
  - EN: Pin tool_choice to {"type": "tool", "name": "extract_invoice"} for all documents.

## CCAR-F-Udemy03-0033

**JA** あるフィンテック企業のプラットフォームチームが、ソフトウェア開発を加速するためにClaude Codeを使用しています。コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っており、カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合しています。プランモードと直接実行をどのように使い分けるかを理解する必要があります。

このチームには、リファクタリングの後にREADMEのセクション、APIリファレンス、移行時の注意事項を更新する、カスタムのドキュメント作成スキル（スラッシュで起動するコマンド）があります。

このコマンドの全体的な採用率は高いものの、レビューデータによると、誤った出力は関数シグネチャと移行時の警告という一部のフィールドに集中しています。

人手によるレビューを縮小する前に、チームが行うべきことはどれですか。

**KO** 한 핀테크 회사의 플랫폼 팀이 소프트웨어 개발 속도를 높이기 위해 Claude Code를 사용하고 있습니다. 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 쓰고 있으며, custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합했습니다. plan mode와 직접 실행을 어떻게 구분해 쓸지 이해해야 합니다.

이 팀에는 refactoring 후 README 섹션, API 레퍼런스, 마이그레이션 주의 사항을 갱신하는 custom 문서 작성 skill(slash로 실행하는 명령)이 있습니다.

이 명령의 전체 채택률은 높지만, 리뷰 데이터를 보면 잘못된 출력은 함수 시그니처와 마이그레이션 경고라는 일부 필드에 몰려 있습니다.

사람의 리뷰를 줄이기 전에 팀이 해야 할 일은 무엇입니까?

- A. JA: 全体の採用率をリリースゲートとして使用し、統合後の出力を週次でサンプリングする。
  - KO: 전체 채택률을 릴리스 게이트로 사용하고, 병합된 출력을 주 단위로 샘플링합니다.
  - EN: Use the overall adoption rate as a release gate, and sample the merged output weekly.
- B. JA: コマンドのファイル単位の確信度が固定の閾値を超えた場合にドキュメントの変更を承認する。
  - KO: 명령의 파일 단위 확신도가 고정된 임계값을 넘으면 문서 변경을 승인합니다.
  - EN: Approve documentation changes when the command's file-level confidence exceeds a fixed threshold.
- C. JA: 全てのドキュメント更新について、変更を適用する前にコマンドをプランモードに切り替える。
  - KO: 모든 문서 갱신에 대해, 변경을 적용하기 전에 명령을 plan mode로 전환합니다.
  - EN: For all documentation updates, switch the command to plan mode before applying changes.
- D. JA: フィールド単位の確信度出力を必須にし、ラベル付き検証例を用いてレビューの閾値をキャリブレーションする。
  - KO: 필드 단위 확신도 출력을 필수로 하고, 라벨이 달린 검증 예시로 리뷰 임계값을 calibration합니다.
  - EN: Require field-level confidence output, and calibrate review thresholds using labeled validation examples.

## CCAR-F-Udemy03-0034

**JA** あなたは、経費精算プラットフォーム企業向けに、Claudeを使用して構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携できる必要があります。

このシステムを、新しい文書の種類として公共料金の請求書に対応させようとしています。そのためには、まずClaude Codeが、既存の次のものを調査する必要があります。

数十個の抽出モジュール

スキーマバリデーター

フィクスチャの慣例

エラー処理の経路

試験実行では、メインの会話が検索結果やファイル読み取りの出力で埋め尽くされ、実装の段階になる頃には、対象とすべきスキーマの変更点を見失っています。

有用な文脈を保ちながら調査も適切に行える、最も適したワークフローはどれですか。

**KO** 당신은 경비 정산 플랫폼 회사를 위해 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동할 수 있어야 합니다.

이 시스템이 새로운 문서 유형으로 공과금 청구서를 처리할 수 있게 하려고 합니다. 이를 위해서는 먼저 Claude Code가 다음과 같은 기존 요소를 조사해야 합니다.

수십 개의 추출 모듈

schema validator

fixture 관례

오류 처리 경로

시험 실행에서는 main 대화가 검색 결과와 파일 읽기 출력으로 가득 차서, 구현 단계에 이를 무렵에는 대상으로 삼아야 할 schema 변경 사항을 놓치고 있습니다.

유용한 context를 유지하면서 조사도 충분히 할 수 있는 가장 적합한 workflow는 무엇입니까?

- A. JA: 抽出モジュール・フィクスチャ・スキーマファイルを一括でプロンプトに読み込む共有のスラッシュコマンドを作成してから編集する。
  - KO: 추출 모듈·fixture·schema 파일을 한꺼번에 prompt로 불러오는 공유 slash command를 만든 뒤 편집합니다.
  - EN: Create a shared slash command that loads the extraction modules, fixtures, and schema files into the prompt all at once, then edit.
- B. JA: 探索的な調査はスコープと慣例を明示してExploreサブエージェントに委任し、要約された所見をもとに実装する。
  - KO: 탐색적 조사는 범위와 관례를 명시해 Explore subagent에게 위임하고, 요약된 결과를 바탕으로 구현합니다.
  - EN: Delegate the exploratory investigation to an Explore subagent with the scope and conventions specified, and implement based on the summarized findings.
- C. JA: タスク全体をプランモードに切り替え、調査・編集・検証を1つの継続した文脈の中で行わせる。
  - KO: 작업 전체를 plan mode로 전환해, 조사·편집·검증을 하나의 이어진 context 안에서 하게 합니다.
  - EN: Switch the entire task to plan mode, and have it perform investigation, editing, and verification within one continuous context.
- D. JA: メインの会話の中で検索を一通り実行し、スキーマとバリデーターの変更を実装する直前に/compactを使用する。
  - KO: main 대화 안에서 검색을 한 차례 모두 실행하고, schema와 validator 변경을 구현하기 직전에 /compact를 사용합니다.
  - EN: Run the full set of searches in the main conversation, and use /compact just before implementing the schema and validator changes.

## CCAR-F-Udemy03-0035

**JA** あなたは、ソフトウェア開発を加速するためにClaude Codeを使用しています。チームでは、コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行をどのように使い分けるかを理解する必要があります。

ある物流プラットフォームの開発生産性チームは、/find-callersコマンドを追加しようとしています。このコマンドの要件は次のとおりです。

リネームされたヘルパー関数へのすべての参照を見つける

検索対象をTypeScriptのソースファイルに限定する

開発者が各一致箇所へ直接ジャンプできるだけのコンテキストを返す

チームのClaude Codeでは、組み込みのRead・Grep・Globが有効になっています。

このコマンドで使う、Claude Codeの組み込みツールの設定はどれですか。（2つ選択してください。）

**KO** 소프트웨어 개발 속도를 높이기 위해 Claude Code를 사용하고 있습니다. 팀은 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 쓰고 있습니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합했으며, plan mode와 직접 실행을 어떻게 구분해 쓸지 이해해야 합니다.

한 물류 플랫폼의 개발 생산성 팀이 /find-callers 명령을 추가하려고 합니다. 이 명령의 요구 사항은 다음과 같습니다.

이름이 바뀐 helper 함수에 대한 모든 참조 찾기

검색 대상을 TypeScript 소스 파일로 한정하기

개발자가 각 일치 위치로 바로 이동할 수 있을 만큼의 context 반환하기

팀의 Claude Code에서는 내장 Read·Grep·Glob이 활성화되어 있습니다.

이 명령에서 사용할 Claude Code 내장 도구 설정은 무엇입니까? (2개를 선택하십시오.)

- A. JA: Grepの-nを有効にし、一致行を行番号付きで返して該当箇所へ移動できるようにする。
  - KO: Grep의 -n을 활성화해 일치하는 줄을 줄 번호와 함께 반환하고, 해당 위치로 이동할 수 있게 합니다.
  - EN: Enable Grep's -n to return matching lines with line numbers so developers can navigate to the locations.
- B. JA: Grepでヘルパー関数名をpatternに指定し、glob: "**/*.ts"で範囲を絞り、output_mode: "content"を設定する。
  - KO: Grep에서 helper 함수 이름을 pattern으로 지정하고, glob: "**/*.ts"로 범위를 좁힌 뒤 output_mode: "content"를 설정합니다.
  - EN: Use Grep with the helper function name as the pattern, narrow the scope with glob: "**/*.ts", and set output_mode: "content".
- C. JA: Globをpattern: "**/*.ts"で使用し、その後Readで各ファイルの内容をすべて会話に読み込ませてスキャンする。
  - KO: Glob을 pattern: "**/*.ts"로 사용한 뒤, Read로 각 파일 내용을 전부 대화에 읽어 들여 훑어봅니다.
  - EN: Use Glob with pattern: "**/*.ts", then use Read to load the full contents of each file into the conversation and scan them.
- D. JA: Grepで関数名をpatternに指定し、output_mode: "files_with_matches"のまま該当ファイル一覧だけを返す。
  - KO: Grep에서 함수 이름을 pattern으로 지정하고, output_mode: "files_with_matches"를 그대로 두어 해당 파일 목록만 반환합니다.
  - EN: Use Grep with the function name as the pattern, leaving output_mode: "files_with_matches" so that it returns only the list of matching files.

## CCAR-F-Udemy03-0036

**JA** ある開発チームが、コード生成、リファクタリング、デバッグ、ドキュメント作成を効率化するために、Claude Codeを開発ワークフローに導入しています。カスタムスラッシュコマンドやCLAUDE.mdの設定を活用しており、プランモードと直接実行をどのように使い分けるかも検討しています。

Claude CodeがBash経由でnpm testを実行すると、標準出力には依存関係の警告や絶対パスなど、冗長な情報が大量に含まれます。

チームは、Bashコマンドの実行自体は変えずに、成功したBashの結果を短く正規化してからClaudeに読ませたいと考えています。

選択すべき実装はどれですか。（2つ選択してください。）

**KO** 한 개발팀이 코드 생성, refactoring, 디버깅, 문서 작성을 효율화하기 위해 Claude Code를 개발 workflow에 도입하고 있습니다. custom slash command와 CLAUDE.md 설정을 활용하고 있으며, plan mode와 직접 실행을 어떻게 구분해 쓸지도 검토하고 있습니다.

Claude Code가 Bash로 npm test를 실행하면, 표준 출력에 의존성 경고나 절대 경로 같은 장황한 정보가 대량으로 포함됩니다.

팀은 Bash 명령 실행 자체는 바꾸지 않고, 성공한 Bash 결과를 짧게 정규화한 뒤에 Claude가 읽게 하려고 합니다.

선택해야 할 구현은 무엇입니까? (2개를 선택하십시오.)

- A. JA: BashにマッチするPostToolUseフックを設定し、Bashの結果と同じ形のupdatedToolOutputを返す。
  - KO: Bash에 매칭되는 PostToolUse hook을 설정하고, Bash 결과와 같은 형태의 updatedToolOutput을 반환합니다.
  - EN: Configure a PostToolUse hook that matches Bash, and return updatedToolOutput in the same shape as the Bash result.
- B. JA: BashにマッチするPreToolUseフックを設定し、受け取ったツール入力の中の標準出力を書き換える。
  - KO: Bash에 매칭되는 PreToolUse hook을 설정하고, 전달받은 도구 입력 안의 표준 출력을 다시 씁니다.
  - EN: Configure a PreToolUse hook that matches Bash, and rewrite the standard output within the received tool input.
- C. JA: BashにマッチするPostToolUseフックを設定し、終了コード2で終了して正規化した出力を標準エラーに書き込む。
  - KO: Bash에 매칭되는 PostToolUse hook을 설정하고, 종료 코드 2로 종료하면서 정규화한 출력을 표준 에러에 씁니다.
  - EN: Configure a PostToolUse hook that matches Bash, exit with exit code 2, and write the normalized output to standard error.
- D. JA: そのフックがupdatedToolOutputを返すのは成功したBashの結果に限り、失敗時は生の出力を渡す。
  - KO: 그 hook이 updatedToolOutput을 반환하는 것은 성공한 Bash 결과로 한정하고, 실패했을 때는 원래 출력을 그대로 넘깁니다.
  - EN: Have the hook return updatedToolOutput only for successful Bash results, and pass through the raw output on failure.

## CCAR-F-Udemy03-0037

**JA** ある経営コンサルティング会社が、Claude Agent SDKを使用してマルチエージェントリサーチシステムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムは製造業のサプライチェーンに関するトピックを調査し、出典を明記した包括的なレポートを作成します。

何回か実行したところ、最終レポートは洗練された要約になっているものの、引用の網羅性が弱いことが分かりました。Web検索サブエージェントと文書分析サブエージェントは、有用なソースの詳細情報をコーディネーターに返しています。しかしその後、統合サブエージェントは「テーマと提言をまとめよ」という短い指示だけで呼び出されています。

オーケストレーションの設計を最も改善できる変更はどれですか。（2つ選択してください。）

**KO** 한 경영 컨설팅 회사가 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. coordinator agent가 전문화된 subagent에게 작업을 위임합니다. subagent는 웹 검색, 문서 분석, 조사 결과 통합, 보고서 생성을 각각 맡습니다. 이 시스템은 제조업 공급망에 관한 주제를 조사하고, 출처를 명시한 포괄적인 보고서를 작성합니다.

몇 차례 실행해 보니, 최종 보고서는 잘 다듬어진 요약이지만 인용의 포괄성이 약하다는 것을 알게 되었습니다. 웹 검색 subagent와 문서 분석 subagent는 유용한 출처의 상세 정보를 coordinator에게 반환하고 있습니다. 그런데 그 뒤 통합 subagent는 '주제와 권고 사항을 정리하라'라는 짧은 지시만으로 호출되고 있습니다.

orchestration 설계를 가장 크게 개선할 수 있는 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 統合サブエージェントへのAgentプロンプトで、各テーマと提言に根拠となる出典の引用を求める。
  - KO: 통합 subagent에 보내는 Agent prompt에서, 각 주제와 권고 사항마다 근거가 되는 출처의 인용을 요구합니다.
  - EN: In the Agent prompt to the synthesis subagent, require citations of supporting sources for each theme and recommendation.
- B. JA: リサーチ用のサブエージェント同士が直接やり取りし、統合の前にソースの詳細を共有できるようにする。
  - KO: 리서치용 subagent끼리 직접 주고받게 해서, 통합 전에 출처의 상세 정보를 공유할 수 있게 합니다.
  - EN: Let the research subagents communicate directly with each other so they can share source details before synthesis.
- C. JA: レポートごとに共有タスクリストで連携する、独立したエージェントチームのセッションに作り替える。
  - KO: 보고서마다 공유 작업 목록으로 협업하는, 독립된 agent team session으로 재구성합니다.
  - EN: Rebuild it as independent agent team sessions that coordinate through a shared task list for each report.
- D. JA: 関連する調査結果と出典のメタデータを、統合サブエージェントのAgentプロンプトに直接含める。
  - KO: 관련 조사 결과와 출처 metadata를 통합 subagent의 Agent prompt에 직접 포함합니다.
  - EN: Include the relevant findings and source metadata directly in the synthesis subagent's Agent prompt.

## CCAR-F-Udemy03-0038

**JA** ある研究チームが、データ分析パイプラインの開発を加速するためにClaude Codeを使用しています。コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っており、カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合しています。プランモードと直接実行をどのように使い分けるかを理解する必要があります。

カスタムの/experiment-summaryコマンドの試験運用で、このチームは次の3つのエージェントに、同じツール一式（Read、Grep、Glob、Bash、WebSearch、WebFetch、実験管理MCPツール）を与えています。

差分解析エージェント

異常値トリアージエージェント

最終統合エージェント

コーディネーターが差分と異常値の完全な要約を渡しているにもかかわらず、最終統合エージェントは、WebSearchや実験管理ツールで広範な問い合わせを実行し、要約に無関係な項目を追加してしまうことがよくあります。

この挙動に最も適切に対処できる変更はどれですか。

**KO** 한 연구팀이 데이터 분석 pipeline 개발 속도를 높이기 위해 Claude Code를 사용하고 있습니다. 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 쓰고 있으며, custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합했습니다. plan mode와 직접 실행을 어떻게 구분해 쓸지 이해해야 합니다.

custom /experiment-summary 명령을 시범 운영하면서, 이 팀은 다음 3개 agent에 같은 도구 세트(Read, Grep, Glob, Bash, WebSearch, WebFetch, 실험 관리 MCP 도구)를 주고 있습니다.

diff 분석 agent

이상값 triage agent

최종 통합 agent

coordinator가 diff와 이상값에 대한 완전한 요약을 넘겨주는데도, 최종 통합 agent는 WebSearch나 실험 관리 도구로 광범위한 조회를 실행해 요약과 관계없는 항목을 덧붙이는 경우가 많습니다.

이 동작에 가장 적절하게 대처할 수 있는 변경은 무엇입니까?

- A. JA: 委任された調査結果だけを使って統合するレポート例をfew-shotで追加する。
  - KO: 위임받은 조사 결과만으로 통합한 보고서 예시를 few-shot으로 추가합니다.
  - EN: Add a few-shot example of a synthesis report that uses only the delegated findings.
- B. JA: 広範な参照ツールの名前を変更し、調査専用であることを示す。
  - KO: 광범위한 조회 도구의 이름을 바꿔, 조사 전용임을 나타냅니다.
  - EN: Rename the broad lookup tools to indicate that they are for investigation only.
- C. JA: 各エージェントを役割ごとのツールに制限し、追加の参照はコーディネーター経由にする。
  - KO: 각 agent를 역할에 맞는 도구로 제한하고, 추가 조회는 coordinator를 거치게 합니다.
  - EN: Restrict each agent to the tools for its role, and route any additional lookups through the coordinator.
- D. JA: 統合エージェントのプロンプトを強化し、要約提供後の探索的な検索を禁止する。
  - KO: 통합 agent의 prompt를 강화해, 요약을 받은 뒤의 탐색적 검색을 금지합니다.
  - EN: Strengthen the synthesis agent's prompt to prohibit exploratory searches after the summaries are provided.

## CCAR-F-Udemy03-0039

**JA** あなたは、Claude Agent SDKを使用してITヘルプデスクの一次対応エージェントを構築しています。このエージェントは、パスワードリセット、ソフトウェアのアクセス権申請、ハードウェア障害など、あいまいさの高い問い合わせを処理します。カスタムのModel Context Protocol（MCP）ツール（get_employee、lookup_ticket、reset_password、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を達成することです。

CIパイプラインでは、夜間のトリアージチェックを実行しています。このチェックでは、Claude Codeにプロンプトを処理させて結果を標準出力に書き出させ、開発者の応答を待たずに終了させる必要があります。

現在のジョブは対話モードのclaudeコマンドを起動しており、ランナー上で断続的にハングしてしまいます。

この自動化ワークフローに最も適した変更はどれですか。

**KO** Claude Agent SDK로 IT 헬프데스크의 1차 대응 agent를 구축하고 있습니다. 이 agent는 비밀번호 재설정, 소프트웨어 접근 권한 신청, 하드웨어 장애처럼 모호성이 높은 문의를 처리합니다. custom Model Context Protocol(MCP) 도구(get_employee, lookup_ticket, reset_password, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation이 필요한 시점을 판단하면서 첫 문의 해결률 80% 이상을 달성하는 것입니다.

CI pipeline에서 야간 triage 검사를 실행하고 있습니다. 이 검사에서는 Claude Code가 prompt를 처리해 결과를 표준 출력에 쓰고, 개발자의 응답을 기다리지 않고 종료해야 합니다.

현재 job은 대화형 모드의 claude 명령을 실행하고 있으며, runner에서 간헐적으로 멈춥니다.

이 자동화 workflow에 가장 적합한 변경은 무엇입니까?

- A. JA: 通常の対話モードのclaudeコマンドに--output-format jsonを追加し、標準出力から応答をパースする。
  - KO: 일반 대화형 모드의 claude 명령에 --output-format json을 추가하고, 표준 출력에서 응답을 파싱합니다.
  - EN: Add --output-format json to the regular interactive claude command, and parse the response from standard output.
- B. JA: 通常の対話モードのclaudeコマンドを起動し、プロンプト内で「回答したら終了してください」と指示する。
  - KO: 일반 대화형 모드의 claude 명령을 실행하고, prompt 안에서 '답변하면 종료하십시오'라고 지시합니다.
  - EN: Launch the regular interactive claude command, and instruct it in the prompt to "exit once you have answered."
- C. JA: ジョブの中でClaude Codeをclaude -p "..."またはclaude --print "..."で呼び出す。
  - KO: job 안에서 Claude Code를 claude -p "..." 또는 claude --print "..."로 호출합니다.
  - EN: Invoke Claude Code in the job with claude -p "..." or claude --print "...".
- D. JA: 対話モードのclaudeコマンドをtimeoutでラップし、失敗時にジョブをリトライする。
  - KO: 대화형 모드의 claude 명령을 timeout으로 감싸고, 실패하면 job을 재시도합니다.
  - EN: Wrap the interactive claude command in timeout, and retry the job on failure.

## CCAR-F-Udemy03-0040

**JA** あなたは、Claude Agent SDKを使用してマルチエージェントの政策分析システムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

Claude Codeを使って、この調査システムのTypeScriptリポジトリを保守しています。引用検証のテスト、レポート描画のテスト、オーケストレーションのテストは、複数のトップレベルフォルダにまたがって、実装ファイルと並べて配置されています。

各パッケージにガイダンスを重複させずに、Claude Codeがテストファイルを扱っているときにだけ、同じテスト用のガイダンスが適用されるようにしたいと考えています。

取るべき対応はどれですか。

**KO** Claude Agent SDK로 multi-agent 정책 분석 시스템을 구축하고 있습니다. coordinator agent가 전문화된 subagent에게 작업을 위임합니다. subagent는 웹 검색, 문서 분석, 조사 결과 통합, 보고서 생성을 각각 맡습니다. 이 시스템은 주제를 조사하고, 출처를 명시한 포괄적인 보고서를 작성합니다.

Claude Code로 이 조사 시스템의 TypeScript 저장소를 유지보수하고 있습니다. 인용 검증 테스트, 보고서 렌더링 테스트, orchestration 테스트는 여러 최상위 폴더에 걸쳐 구현 파일 옆에 배치되어 있습니다.

패키지마다 지침을 중복해서 두지 않고, Claude Code가 테스트 파일을 다룰 때만 같은 테스트용 지침이 적용되게 하려고 합니다.

어떻게 대응해야 합니까?

- A. JA: テストファイルのパターンに一致するpathsフロントマターを付けた.claude/rules/testing.mdにガイダンスを書く。
  - KO: 테스트 파일 패턴과 일치하는 paths frontmatter를 붙인 .claude/rules/testing.md에 지침을 작성합니다.
  - EN: Write the guidance in .claude/rules/testing.md with a paths frontmatter that matches test file patterns.
- B. JA: テスト用のガイダンスをルートのCLAUDE.mdファイルに配置し、どのClaude Codeセッションにも同じ指示が届くようにする。
  - KO: 테스트용 지침을 루트의 CLAUDE.md 파일에 두어, 모든 Claude Code session에 같은 지시가 전달되게 합니다.
  - EN: Place the testing guidance in the root CLAUDE.md file so that the same instructions reach every Claude Code session.
- C. JA: テストを含む各ディレクトリにCLAUDE.mdファイルを追加し、同じテスト用のガイダンスを各ファイルに繰り返し記載する。
  - KO: 테스트가 있는 각 디렉터리에 CLAUDE.md 파일을 추가하고, 같은 테스트용 지침을 파일마다 반복해 적습니다.
  - EN: Add a CLAUDE.md file to each directory containing tests, and repeat the same testing guidance in each file.
- D. JA: フロントマターを付けずに.claude/rules/testing.mdを作成し、ファイル名によってテストファイルに限定されることを期待する。
  - KO: frontmatter 없이 .claude/rules/testing.md를 만들고, 파일 이름 덕분에 테스트 파일로 한정되기를 기대합니다.
  - EN: Create .claude/rules/testing.md without frontmatter, expecting it to be limited to test files by its file name.

## CCAR-F-Udemy03-0041

**JA** あなたは、Claude Agent SDKを使用して、競合分析のためのマルチエージェント調査システムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

ある長時間の調査実行で、初期の文書分析により、最終レポートの軸にすべきドメイン固有の分類体系が特定されました。

しかし、多数の検索、ツール結果、修正を経た後、後段の統合パスが汎用的なカテゴリでまとめようとし始め、時折その初期の分類体系と矛盾する内容になっています。アプリケーションは、蓄積したメッセージ履歴を毎回送り直しています。

信頼性を最も改善できる変更はどれですか。

**KO** Claude Agent SDK로 경쟁 분석을 위한 multi-agent 조사 시스템을 구축하고 있습니다. coordinator agent가 전문화된 subagent에게 작업을 위임합니다. subagent는 웹 검색, 문서 분석, 조사 결과 통합, 보고서 생성을 각각 맡습니다. 이 시스템은 주제를 조사하고, 출처를 명시한 포괄적인 보고서를 작성합니다.

장시간 진행된 한 조사 실행에서, 초기 문서 분석을 통해 최종 보고서의 축으로 삼아야 할 도메인 고유의 분류 체계가 확인되었습니다.

그러나 수많은 검색, 도구 결과, 수정을 거친 뒤 후반부의 통합 단계가 범용적인 카테고리로 내용을 정리하기 시작했고, 때때로 초기 분류 체계와 모순되는 결과를 내고 있습니다. 애플리케이션은 누적된 메시지 기록을 매번 다시 보내고 있습니다.

신뢰성을 가장 크게 개선할 수 있는 변경은 무엇입니까?

- A. JA: 後段の統合呼び出しのmax_tokensを増やし、蓄積した会話の全記録をそのまま送り続ける。
  - KO: 후반 통합 호출의 max_tokens를 늘리고, 누적된 대화 전체 기록을 그대로 계속 보냅니다.
  - EN: Increase max_tokens on the later synthesis calls, and keep sending the entire accumulated conversation transcript as is.
- B. JA: 蓄積されたプレフィックスに対してプロンプトキャッシュを有効にし、コンテキストウィンドウに影響を与えずに初期の知見を再利用できるようにする。
  - KO: 누적된 prefix에 prompt caching을 활성화해, context window에 영향을 주지 않고 초기 발견 사항을 재사용할 수 있게 합니다.
  - EN: Enable prompt caching on the accumulated prefix so that early findings can be reused without affecting the context window.
- C. JA: 会話の全記録が明示的に裏付けている場合を除き、汎用的なカテゴリを避けるよう統合の指示を追加する。
  - KO: 대화 전체 기록이 명시적으로 뒷받침하는 경우가 아니면 범용 카테고리를 피하라는 통합 지시를 추가합니다.
  - EN: Add synthesis instructions to avoid generic categories unless the full conversation transcript explicitly supports them.
- D. JA: 発見された分類体系と出典のマッピングを記録した構造化された調査ステートファイルを維持し、後段の統合プロンプトに読み込ませる。
  - KO: 발견된 분류 체계와 출처의 매핑을 기록한 구조화된 조사 상태 파일을 유지하고, 후반 통합 prompt에 읽어 들이게 합니다.
  - EN: Maintain a structured research state file that records the discovered taxonomy and the mapping to sources, and load it into the later synthesis prompt.

## CCAR-F-Udemy03-0042

**JA** あなたは、Claude Agent SDKを使用してマルチエージェントの特許動向調査システムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

文書分析サブエージェントには、次の3つの抽出ツールが用意されています。

extract_metadata

extract_claims

enrich_sources

各文書のワークフローの最初のリクエストでは、ほかの抽出や補完の処理より先に、コーディネーターがサブエージェントに必ずextract_metadataを呼び出させる必要があります。

この要件に最も適した設定はどれですか。（2つ選択してください。）

**KO** Claude Agent SDK로 multi-agent 특허 동향 조사 시스템을 구축하고 있습니다. coordinator agent가 전문화된 subagent에게 작업을 위임합니다. subagent는 웹 검색, 문서 분석, 조사 결과 통합, 보고서 생성을 각각 맡습니다. 이 시스템은 주제를 조사하고, 출처를 명시한 포괄적인 보고서를 작성합니다.

문서 분석 subagent에는 다음 3개 추출 도구가 준비되어 있습니다.

extract_metadata

extract_claims

enrich_sources

각 문서 workflow의 첫 요청에서는 다른 추출이나 보강 처리보다 먼저, coordinator가 subagent에게 반드시 extract_metadata를 호출하게 해야 합니다.

이 요구 사항에 가장 적합한 설정은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 最初の分析リクエストでは、tool_choiceを{"type": "tool", "name": "extract_metadata"}にする。
  - KO: 첫 분석 요청에서는 tool_choice를 {"type": "tool", "name": "extract_metadata"}로 설정합니다.
  - EN: For the first analysis request, set tool_choice to {"type": "tool", "name": "extract_metadata"}.
- B. JA: tool_choiceを省略し、抽出ツールが提供されているときの既定の挙動に任せてClaudeに選ばせる。
  - KO: tool_choice를 생략하고, 추출 도구가 제공될 때의 기본 동작에 맡겨 Claude가 선택하게 합니다.
  - EN: Omit tool_choice and let Claude choose, relying on the default behavior when extraction tools are provided.
- C. JA: コーディネーターがスキーマを選び終えるまでは、文書分析のリクエストでtool_choiceを{"type": "none"}に設定する。
  - KO: coordinator가 schema 선택을 마칠 때까지는 문서 분석 요청에서 tool_choice를 {"type": "none"}으로 설정합니다.
  - EN: Set tool_choice to {"type": "none"} on document analysis requests until the coordinator has finished selecting the schema.
- D. JA: 2回目以降のリクエストではtool_choiceを{"type": "auto"}にし、残りのツールを必要に応じて選ばせる。
  - KO: 두 번째 이후 요청에서는 tool_choice를 {"type": "auto"}로 설정해, 나머지 도구를 필요에 따라 선택하게 합니다.
  - EN: For the second and subsequent requests, set tool_choice to {"type": "auto"} and let it choose the remaining tools as needed.

## CCAR-F-Udemy03-0043

**JA** あなたは、不動産管理会社向けに、Claudeを使用して構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携できる必要があります。

評価の過程で、Claude Codeのサブエージェントに、500件の賃貸借契約書、入居申込書、更新通知にまたがる抽出エラーを調査させています。現在のアプローチでは、各サブエージェントに「すべての文書にわたるスキーマ検証失敗の原因を見つけること」という同じ指示を与えています。その結果、所見が重複し、統合時のコンテキストも大きくなっています。

調査を適切に分割しつつ、統合の質を維持できる変更として最も適切なものはどれですか。

**KO** 부동산 관리 회사를 위해 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동할 수 있어야 합니다.

평가 과정에서 Claude Code의 subagent에게 임대차 계약서, 입주 신청서, 갱신 통지서 500건에 걸친 추출 오류를 조사하게 하고 있습니다. 현재 방식은 각 subagent에게 '모든 문서에 걸친 schema 검증 실패의 원인을 찾을 것'이라는 같은 지시를 줍니다. 그 결과 발견 사항이 중복되고, 통합할 때의 context도 커지고 있습니다.

조사를 적절히 분할하면서 통합 품질을 유지할 수 있는 변경으로 가장 적절한 것은 무엇입니까?

- A. JA: 各サブエージェントに文書グループまたは抽出対象の観点ごとに明確に異なる担当を割り当て、必要な文脈を与え、統合のための簡潔な所見を求める。
  - KO: 각 subagent에게 문서 그룹이나 추출 대상 관점별로 명확히 구분되는 담당을 배정하고, 필요한 맥락을 제공한 뒤, 통합을 위한 간결한 발견 사항을 요청합니다.
  - EN: Assign each subagent a clearly distinct responsibility, by document group or by extraction-target perspective, give it the necessary context, and ask for concise findings for consolidation.
- B. JA: すべてのサブエージェントに全体の文書コーパスを独立にレビューさせ、重複する所見を比較したうえで、共通するスキーマの問題を統合する。
  - KO: 모든 subagent가 전체 문서 코퍼스를 각자 독립적으로 검토하게 하고, 중복되는 발견 사항을 비교한 뒤 공통된 schema 문제를 통합합니다.
  - EN: Have all subagents independently review the entire document corpus, compare the overlapping findings, and then consolidate the common schema issues.
- C. JA: 文書の種類ごとに1つの入れ子になったサブエージェントの連鎖を作成し、各階層で詳細な要約を求めたうえで、最終的な出力を統合する。
  - KO: 문서 유형마다 중첩된 subagent 체인을 하나씩 만들고, 각 계층에서 상세한 요약을 요청한 뒤 최종 출력을 통합합니다.
  - EN: Create one chain of nested subagents per document type, request detailed summaries at each level, and then consolidate the final output.
- D. JA: 重複する文書のサブセットを複数のサブエージェントに割り当て、それぞれにスキーマの問題を見つけるよう依頼し、後で重複を解消する。
  - KO: 겹치는 문서 하위 집합을 여러 subagent에 배정해 각각 schema 문제를 찾게 하고, 나중에 중복을 해소합니다.
  - EN: Assign overlapping subsets of documents to multiple subagents, ask each to find schema issues, and resolve the duplicates later.

## CCAR-F-Udemy03-0044

**JA** ある旅行予約会社が、Claude Agent SDKを使用してカスタマーサポート解決エージェントを構築しています。このエージェントは、予約変更、料金請求に関する問い合わせ、アカウントの問題など、あいまいさの高い依頼を処理します。カスタムのModel Context Protocol（MCP）ツール（get_customer、lookup_order、process_refund、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を達成することです。

監査対応のロールアウトで、チームはcustomer_id、order_id、action_taken、escalation_reason、policy_basisを含む解決記録を必須にしました。現在の実装では、Claudeに「有効なJSONのみ」で応答するよう指示しています。しかし本番環境のログでは次のことが起きており、ケースを保存する前のパース処理が失敗することがあります。

応答の末尾に余分な文章が付く

必須キーが欠落する

アプリケーションコードが利用できる、スキーマに準拠した記録を最も確実に生成できる変更はどれですか。（2つ選択してください。）

**KO** 한 여행 예약 회사가 Claude Agent SDK로 고객 지원 해결 agent를 구축하고 있습니다. 이 agent는 예약 변경, 요금 청구 문의, 계정 문제처럼 모호성이 높은 요청을 처리합니다. custom Model Context Protocol(MCP) 도구(get_customer, lookup_order, process_refund, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation이 필요한 시점을 판단하면서 첫 문의 해결률 80% 이상을 달성하는 것입니다.

감사 대응을 위한 롤아웃에서, 팀은 customer_id, order_id, action_taken, escalation_reason, policy_basis를 포함한 해결 기록을 필수로 정했습니다. 현재 구현은 Claude에게 '유효한 JSON만'으로 응답하라고 지시합니다. 그러나 운영 환경 로그를 보면 다음과 같은 일이 생겨, 케이스를 저장하기 전의 파싱 처리가 실패하는 경우가 있습니다.

응답 끝에 불필요한 문장이 붙음

필수 키가 누락됨

애플리케이션 코드가 활용할 수 있는, schema를 준수하는 기록을 가장 확실하게 생성할 수 있는 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 解決記録のJSON Schemaをoutput_config.formatに指定し、応答自体を制約する。
  - KO: 해결 기록의 JSON Schema를 output_config.format에 지정해, 응답 자체를 제약합니다.
  - EN: Specify the JSON Schema for the resolution record in output_config.format to constrain the response itself.
- B. JA: 「有効なJSONのみ」の指示を強め、スキーマをXMLタグで囲み、散文を含む応答は破棄して再生成させる。
  - KO: '유효한 JSON만' 지시를 강화하고, schema를 XML 태그로 감싸며, 산문이 섞인 응답은 버리고 다시 생성하게 합니다.
  - EN: Strengthen the "valid JSON only" instruction, wrap the schema in XML tags, and discard and regenerate any response that contains prose.
- C. JA: 解決記録用のツールを登録するが、tool_choiceはautoのままにして、使うかどうかはClaudeに判断させる。
  - KO: 해결 기록용 도구를 등록하되 tool_choice는 auto로 두어, 사용 여부를 Claude가 판단하게 합니다.
  - EN: Register a tool for the resolution record, but leave tool_choice as auto and let Claude decide whether to use it.
- D. JA: 解決記録用にinput_schemaを持つstrictなツールを定義し、tool_choiceで使用を強制する。
  - KO: 해결 기록용으로 input_schema를 가진 strict 도구를 정의하고, tool_choice로 사용을 강제합니다.
  - EN: Define a strict tool with an input_schema for the resolution record and force its use with tool_choice.

## CCAR-F-Udemy03-0045

**JA** あるヘルステック企業のエンジニアリングチームが、Claude Codeを使ってバックエンドサービスの開発を進めています。コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っており、カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合しています。プランモードと直接実行をどのように使い分けるかも理解しておきたいと考えています。

長時間のリファクタリングセッションで、ファイルの読み込み、テスト結果、デバッグのやり取りが積み重なるうちに、Claude Codeが以前に決めたアーキテクチャ上の判断と矛盾する提案をし始めることに、チームは気づきました。

チームは、会話の全履歴が確実に保持され続けることに頼らずに、譲れない設計判断を守れるようにワークフローを変えたいと考えています。

チームが取るべき対応はどれですか。（2つ選択してください。）

**KO** 한 헬스테크 기업의 엔지니어링 팀이 Claude Code로 백엔드 서비스를 개발하고 있습니다. 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 쓰고 있으며, custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합했습니다. plan mode와 직접 실행을 어떻게 구분해 쓸지도 이해해 두려고 합니다.

장시간의 refactoring session에서 파일 읽기, 테스트 결과, 디버깅 대화가 쌓여 가면서, Claude Code가 앞서 정한 아키텍처 결정과 모순되는 제안을 하기 시작한다는 것을 팀이 알아차렸습니다.

팀은 대화 전체 기록이 확실히 유지된다는 데 의존하지 않고, 양보할 수 없는 설계 결정을 지킬 수 있도록 workflow를 바꾸려고 합니다.

팀이 취해야 할 대응은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 会話の全文を継続セッションへ引き継ぎ、大きなコンテキストウィンドウで過去の決定を保持させる。
  - KO: 대화 전문을 이어지는 session으로 넘기고, 큰 context window로 과거 결정을 유지하게 합니다.
  - EN: Carry the full conversation over to a continued session and rely on the large context window to retain past decisions.
- B. JA: 主要な決定事項と制約を構造化した事実ファイルに記録し、作業中に参照・更新させる。
  - KO: 주요 결정 사항과 제약을 구조화된 사실 파일에 기록하고, 작업 중에 참조·갱신하게 합니다.
  - EN: Record key decisions and constraints in a structured facts file, and have Claude reference and update it as work progresses.
- C. JA: 譲れない設計判断をプロジェクトのCLAUDE.mdに記載し、各セッションの開始時に読み込ませる。
  - KO: 양보할 수 없는 설계 결정을 프로젝트의 CLAUDE.md에 적어, 각 session을 시작할 때 읽어 들이게 합니다.
  - EN: Document the non-negotiable design decisions in the project's CLAUDE.md and have it loaded at the start of each session.
- D. JA: 数ターンごとに会話を要約させ、それまでの決定事項を最新の要約文に置き換えていく。
  - KO: 몇 turn마다 대화를 요약하게 하고, 그때까지의 결정 사항을 최신 요약문으로 바꿔 나갑니다.
  - EN: Have the conversation summarized every few turns and replace the earlier decisions with the latest summary text.

## CCAR-F-Udemy03-0046

**JA** あなたは、Claudeを使用して構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSON（JavaScript Object Notation）スキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携できる必要があります。

抽出プロンプトの開発中に、同じClaude Codeへのリクエストでも、開発者がどこからセッションを開始するかによって挙動が異なることが分かりました。領収書のパッケージにはパッケージ固有のCLAUDE.mdがあり、欠落した加盟店の税務IDはnullとして表すよう書かれています。しかし、一部のセッションではこの指示に従っていません。

現在のセッションでClaude Codeが意図した指示を受け取っているかどうかを、まず診断するために行うべきことはどれですか。（2つ選択してください。）

**KO** Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON(JavaScript Object Notation) schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동할 수 있어야 합니다.

추출 prompt를 개발하던 중, 같은 Claude Code 요청이라도 개발자가 어디에서 session을 시작하느냐에 따라 동작이 달라진다는 것을 알게 되었습니다. 영수증 패키지에는 패키지 전용 CLAUDE.md가 있고, 누락된 가맹점 세무 ID는 null로 나타내라고 적혀 있습니다. 그러나 일부 session은 이 지시를 따르지 않습니다.

현재 session의 Claude Code가 의도한 지시를 받고 있는지 먼저 진단하려면 무엇을 해야 합니까? (2개를 선택하십시오.)

- A. JA: 各開発者がClaude Codeを起動したディレクトリと、receiptsパッケージのCLAUDE.mdの場所を突き合わせる。
  - KO: 각 개발자가 Claude Code를 실행한 디렉터리와 receipts 패키지의 CLAUDE.md 위치를 대조합니다.
  - EN: Cross-check the directory from which each developer launched Claude Code against the location of the receipts package's CLAUDE.md.
- B. JA: 影響を受けた各セッションで/contextを実行し、「Memory files」に並ぶメモリファイルを比較する。
  - KO: 영향을 받은 각 session에서 /context를 실행하고, 'Memory files'에 나열된 메모리 파일을 비교합니다.
  - EN: Run /context in each affected session and compare the memory files listed under "Memory files".
- C. JA: 自動メモリを無効化して同じプロンプトを再実行し、リポジトリの指示だけが影響していることを確かめる。
  - KO: auto memory를 비활성화하고 같은 prompt를 다시 실행해, 저장소의 지시만 영향을 주고 있는지 확인합니다.
  - EN: Disable auto memory and rerun the same prompt to confirm that only the repository's instructions are having an effect.
- D. JA: リポジトリのルートで/initを再実行し、プロジェクトのCLAUDE.mdを再生成してからセッションの挙動を比べる。
  - KO: 저장소 루트에서 /init을 다시 실행해 프로젝트의 CLAUDE.md를 재생성한 뒤 session 동작을 비교합니다.
  - EN: Rerun /init at the repository root to regenerate the project's CLAUDE.md, and then compare session behavior.

## CCAR-F-Udemy03-0047

**JA** あなたは、Claudeを使用して保険金請求書類の構造化データ抽出システムを構築しています。このシステムは、非構造化の請求書類から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携できる必要があります。

このシステムには、2つの抽出ワークロードがあります。

担当者が書類を提出する前に、検証結果を待つ対話的なアップロードフロー

結果を翌営業日にレビューする、夜間のアーカイブ再処理ジョブ

経営層は、ユーザー向けのフローの体験を損なうことなく、トークンコストを削減したいと考えています。

アーキテクトが推奨すべきものはどれですか。（2つ選択してください。）

**KO** Claude로 보험금 청구 서류의 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 청구 서류에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동할 수 있어야 합니다.

이 시스템에는 2가지 추출 workload가 있습니다.

담당자가 서류를 제출하기 전에 검증 결과를 기다리는 대화형 업로드 흐름

결과를 다음 영업일에 검토하는 야간 아카이브 재처리 job

경영진은 사용자용 흐름의 경험을 해치지 않으면서 토큰 비용을 줄이려고 합니다.

아키텍트가 권장해야 할 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 両方のワークロードをMessage Batches APIに回し、対話的な検証は通常1時間以内に終わることを当てにする。
  - KO: 두 workload를 모두 Message Batches API로 보내고, 대화형 검증은 보통 1시간 안에 끝난다는 점에 기댑니다.
  - EN: Route both workloads to the Message Batches API, counting on interactive validation usually finishing within an hour.
- B. JA: 夜間のアーカイブ再処理はMessage Batches APIに回し、対話的な検証は同期のMessages APIのままにする。
  - KO: 야간 아카이브 재처리는 Message Batches API로 보내고, 대화형 검증은 동기식 Messages API에 그대로 둡니다.
  - EN: Route the nightly archive reprocessing to the Message Batches API and keep interactive validation on the synchronous Messages API.
- C. JA: 共通の抽出指示とJSONスキーマにプロンプトキャッシュを適用し、繰り返すプレフィックスの料金を下げる。
  - KO: 공통 추출 지시와 JSON schema에 prompt caching을 적용해, 반복되는 prefix의 요금을 낮춥니다.
  - EN: Apply prompt caching to the shared extraction instructions and JSON schema to reduce the cost of the repeated prefix.
- D. JA: 対話的な検証をMessage Batches APIに回し、同期呼び出しは夜間のアーカイブ再処理のために確保する。
  - KO: 대화형 검증을 Message Batches API로 보내고, 동기 호출은 야간 아카이브 재처리용으로 확보해 둡니다.
  - EN: Route interactive validation to the Message Batches API and reserve synchronous calls for the nightly archive reprocessing.

## CCAR-F-Udemy03-0048

**JA** あなたは訴訟支援企業のeディスカバリーチームで、開発を加速するためにClaude Codeを使用しています。チームでは、コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行をどのように使い分けるかを理解する必要があります。

ある訴訟データ処理チームの抽出ジョブでは、Claudeと厳格なツールスキーマを使って、証言録取記録を事実要約レコードに変換しています。ツール入力のスキーマ自体は有効ですが、アプリケーション側のバリデーターが、次のようなレコードを却下しています。

事実項目が誤ったページ番号を引用している

必要な引用原文が欠落している

現在のリトライプロンプトには「無効なJSONを修正してください」としか書かれておらず、同じ引用の欠陥が何度も再発しています。

レコードを受理する前に、抽出ループが行うべきことはどれですか。

**KO** 소송 지원 기업의 e-discovery 팀에서, 개발 속도를 높이기 위해 Claude Code를 사용하고 있습니다. 팀은 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 쓰고 있습니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합했으며, plan mode와 직접 실행을 어떻게 구분해 쓸지 이해해야 합니다.

한 소송 데이터 처리 팀의 추출 job에서는 Claude와 엄격한 도구 schema를 사용해 증언 녹취록을 사실 요약 레코드로 변환하고 있습니다. 도구 입력의 schema 자체는 유효하지만, 애플리케이션 쪽 validator가 다음과 같은 레코드를 거부하고 있습니다.

사실 항목이 잘못된 페이지 번호를 인용함

필요한 인용 원문이 누락됨

현재 재시도 prompt에는 '잘못된 JSON을 수정하십시오'라고만 적혀 있어, 같은 인용 결함이 계속 재발합니다.

레코드를 수락하기 전에 추출 loop가 해야 할 일은 무엇입니까?

- A. JA: バリデーターを廃止してより広範なプロンプト指示に置き換え、毎回の実行でClaudeに引用を慎重に扱うよう依頼する。
  - KO: validator를 없애고 더 폭넓은 prompt 지시로 대체해, 실행할 때마다 Claude에게 인용을 신중하게 다루도록 요청합니다.
  - EN: Retire the validator and replace it with broader prompt instructions, asking Claude to handle citations carefully on every run.
- B. JA: 厳格なツール入力がスキーマに一致した時点でレコードを受理し、引用の誤りはレビュー担当者が後から見つけることに委ねる。
  - KO: 엄격한 도구 입력이 schema와 일치하는 시점에 레코드를 수락하고, 인용 오류는 검토 담당자가 나중에 찾아내도록 맡깁니다.
  - EN: Accept the record as soon as the strict tool input matches the schema, and leave it to reviewers to catch citation errors later.
- C. JA: バリデーターが検出したフィールドと引用の不備を原文とともに返してリトライさせ、解消しないものはレビューに回す。
  - KO: validator가 감지한 필드와 인용의 결함을 원문과 함께 돌려주어 재시도하게 하고, 해소되지 않은 것은 검토로 넘깁니다.
  - EN: Retry by returning the fields and citation defects detected by the validator along with the source text, and route anything that remains unresolved to review.
- D. JA: 同じリクエストをより高いtemperatureでリトライし、却下された出力と異なる最初の応答を受理する。
  - KO: 같은 요청을 더 높은 temperature로 재시도하고, 거부된 출력과 다른 첫 응답을 수락합니다.
  - EN: Retry the same request at a higher temperature and accept the first response that differs from the rejected output.

## CCAR-F-Udemy03-0049

**JA** あなたは、ソフトウェア開発を加速するためにClaude Codeを使用しています。チームでは、コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っています。カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合し、プランモードと直接実行をどのように使い分けるかを理解する必要があります。

このチームの/lint-reportコマンドは、プルリクエストの指摘事項を、セキュリティ上の問題、スタイル違反、非推奨APIの使用、未使用エクスポートの4つに分類しています。

この1か月、セキュリティ上の問題とスタイル違反の指摘はおおむね採用されていますが、未使用エクスポートの指摘は頻繁に却下されています。Claudeが、次のようなエクスポートまで指摘してしまうためです。

プラグインシステムのために意図的に公開されているエントリーポイント

リフレクションで参照されるエクスポート

複数の開発者が、レビューの出力全体を読み流したり、ミュートしたりするようになっています。

まず行うべき変更はどれですか。（2つ選択してください。）

**KO** 소프트웨어 개발 속도를 높이기 위해 Claude Code를 사용하고 있습니다. 팀은 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 쓰고 있습니다. custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합했으며, plan mode와 직접 실행을 어떻게 구분해 쓸지 이해해야 합니다.

이 팀의 /lint-report 명령은 pull request의 지적 사항을 보안 문제, 스타일 위반, deprecated API 사용, 미사용 export의 4가지로 분류합니다.

지난 한 달 동안 보안 문제와 스타일 위반 지적은 대체로 채택되었지만, 미사용 export 지적은 자주 기각되었습니다. Claude가 다음과 같은 export까지 지적하기 때문입니다.

plugin 시스템을 위해 의도적으로 공개한 entry point

reflection으로 참조되는 export

여러 개발자가 리뷰 출력 전체를 대충 훑고 넘기거나 음소거하기 시작했습니다.

먼저 해야 할 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 分類ごとに適合率と再現率を測り、ノイズの多い未使用エクスポートのチェックを絞るか止める。
  - KO: 분류별로 precision과 recall을 측정하고, 노이즈가 많은 미사용 export 검사를 좁히거나 중단합니다.
  - EN: Measure precision and recall for each category, and narrow or turn off the noisy unused-exports check.
- B. JA: プラグインのエントリーポイントとリフレクションで参照されるエクスポートを、コマンドの除外リストに加える。
  - KO: plugin entry point와 reflection으로 참조되는 export를 명령의 제외 목록에 추가합니다.
  - EN: Add plugin entry points and reflection-referenced exports to the command's exclusion list.
- C. JA: レビューの各分類を1つの品質スコアに統合し、そのスコアが下がったときにだけプロンプトを調整する。
  - KO: 리뷰의 각 분류를 하나의 품질 점수로 합치고, 그 점수가 떨어질 때만 prompt를 조정합니다.
  - EN: Merge the review categories into a single quality score, and adjust the prompt only when that score drops.
- D. JA: セキュリティ上の問題とスタイル違反の指摘の重大度を引き上げ、開発者が有用な指摘に気づきやすくする。
  - KO: 보안 문제와 스타일 위반 지적의 심각도를 높여, 개발자가 유용한 지적을 알아차리기 쉽게 합니다.
  - EN: Raise the severity of security-issue and style-violation findings so that developers more easily notice the useful ones.

## CCAR-F-Udemy03-0050

**JA** あなたは、Claude Agent SDKを使用してマルチエージェントの学術文献レビューシステムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

評価の結果、なじみの薄い研究トピックのレポートでは、網羅性にばらつきがあることが分かりました。よく知られたサブ領域は詳しく扱われる一方で、目立たないが重要な観点が欠落しています。

サブエージェントは通常、割り当てられた作業を最後までやり遂げています。すべてのトピックで割り当ての数を単純に増やすことなく、調査の網羅性を改善したいと考えています。

調査の網羅性を最も改善できるオーケストレーションの変更はどれですか。（2つ選択してください。）

**KO** Claude Agent SDK로 multi-agent 학술 문헌 리뷰 시스템을 구축하고 있습니다. coordinator agent가 전문화된 subagent에게 작업을 위임합니다. subagent는 웹 검색, 문서 분석, 조사 결과 통합, 보고서 생성을 각각 맡습니다. 이 시스템은 주제를 조사하고, 출처를 명시한 포괄적인 보고서를 작성합니다.

평가 결과, 익숙하지 않은 연구 주제의 보고서에서는 포괄성에 편차가 있다는 것이 드러났습니다. 잘 알려진 하위 분야는 자세히 다루는 반면, 눈에 띄지 않지만 중요한 관점은 빠져 있습니다.

subagent는 보통 배정된 작업을 끝까지 완수합니다. 모든 주제에서 배정 수를 단순히 늘리지 않고 조사의 포괄성을 개선하려고 합니다.

조사의 포괄성을 가장 크게 개선할 수 있는 orchestration 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: コーディネーターに集まった所見を見直させ、未着手の観点についてだけ第2回の割り当てを出させる。
  - KO: coordinator가 모인 발견 사항을 다시 검토하게 하고, 아직 다루지 않은 관점에 대해서만 2차 배정을 내리게 합니다.
  - EN: Have the coordinator review the collected findings and issue a second round of assignments only for the aspects that remain unexplored.
- B. JA: 統合エージェントに、追加の調査は行わせずに、入手済みの要約だけを材料として網羅性のギャップを埋めさせる。
  - KO: 통합 agent에게 추가 조사는 시키지 않고, 이미 확보한 요약만을 재료로 포괄성의 공백을 메우게 합니다.
  - EN: Have the synthesis agent fill coverage gaps using only the summaries already obtained, without conducting any additional research.
- C. JA: コーディネーターにまず初期の調査結果をざっと確認させ、そこで見つかった作業リストから的を絞った割り当てを作らせる。
  - KO: coordinator가 먼저 초기 조사 결과를 대략 훑어보게 하고, 거기서 드러난 작업 목록을 바탕으로 초점을 좁힌 배정을 만들게 합니다.
  - EN: Have the coordinator first skim the initial research results and create targeted assignments from the work list identified there.
- D. JA: 取得した出典を1件ずつ別々のサブエージェントのタスクに分割させ、コーディネーターが並列性を最大限に高める。
  - KO: 확보한 출처를 1건씩 별도의 subagent 작업으로 나누고, coordinator가 병렬성을 최대한 높이게 합니다.
  - EN: Split each retrieved source into a separate subagent task, with the coordinator maximizing parallelism.

## CCAR-F-Udemy03-0051

**JA** あなたは、Claude Agent SDKを使用して、旅行予約サービス向けのカスタマーサポート解決エージェントを構築しています。このエージェントは、予約変更、キャンセル、払い戻しなど、あいまいさの高い依頼を処理します。カスタムのMCPツール（get_booking、check_availability、issue_refund、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を達成することです。

アーカイブされた4万件のサポート記録をMessage Batches APIで一括処理する前に、25件で試験実行しました。その結果、次の問題が見つかりました。

判定結果に一貫性がない

一部の出力で、根拠の記載が欠落している

プロダクトマネージャーは、このまま全件をバッチ実行し、不良な行は翌日に再送すればよいと提案しています。

次に取るべき行動はどれですか。

**KO** Claude Agent SDK로 여행 예약 서비스용 고객 지원 해결 agent를 구축하고 있습니다. 이 agent는 예약 변경, 취소, 환불처럼 모호성이 높은 요청을 처리합니다. custom MCP 도구(get_booking, check_availability, issue_refund, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation이 필요한 시점을 판단하면서 첫 문의 해결률 80% 이상을 달성하는 것입니다.

보관된 지원 기록 4만 건을 Message Batches API로 일괄 처리하기 전에 25건으로 시험 실행했습니다. 그 결과 다음 문제가 발견되었습니다.

판정 결과에 일관성이 없음

일부 출력에서 근거 기재가 누락됨

프로덕트 매니저는 이대로 전체 건을 batch로 실행하고, 불량 행은 다음 날 다시 보내면 된다고 제안합니다.

다음으로 취해야 할 행동은 무엇입니까?

- A. JA: 現在のテンプレートに対してプロンプト改善機能を1回実行し、改善後のプロンプトをそのまま採用して、夜間の全件バッチ処理を開始する。
  - KO: 현재 템플릿에 prompt improver를 1회 실행하고, 개선된 prompt를 그대로 채택해 야간 전체 batch 처리를 시작합니다.
  - EN: Run the prompt improver once on the current template, adopt the improved prompt as is, and start the overnight full batch.
- B. JA: 代表的な評価用データセットを作り、明確な基準でプロンプトを改善してから再実行して確認する。
  - KO: 대표성 있는 평가용 데이터셋을 만들고, 명확한 기준으로 prompt를 개선한 뒤 다시 실행해 확인합니다.
  - EN: Build a representative evaluation dataset, improve the prompt against clear criteria, and rerun to confirm.
- C. JA: 全アーカイブを1つのバッチとして提出し、終了後に結果をレビューして、判定や項目に誤りがある行だけを再送する。
  - KO: 전체 아카이브를 하나의 batch로 제출하고, 끝난 뒤 결과를 검토해 판정이나 항목이 잘못된 행만 다시 보냅니다.
  - EN: Submit the entire archive as a single batch, review the results when it finishes, and resubmit only the rows with incorrect decisions or fields.
- D. JA: JSON出力の制約をより厳格にし、現在の指示はそのまま維持したうえで、バッチ実行の結果から判定の誤りを見つけ出す。
  - KO: JSON 출력 제약을 더 엄격하게 하되 현재 지시는 그대로 유지하고, batch 실행 결과에서 판정 오류를 찾아냅니다.
  - EN: Make the JSON output constraints stricter, keep the current instructions as they are, and find incorrect decisions from the batch run results.

## CCAR-F-Udemy03-0052

**JA** あるフィンテック企業のプラットフォームチームが、ソフトウェア開発を加速するためにClaude Codeを使用しています。コード生成、リファクタリング、デバッグ、ドキュメント作成にClaude Codeを使っており、カスタムスラッシュコマンドやCLAUDE.mdの設定を用いて開発ワークフローに統合しています。プランモードと直接実行をどのように使い分けるかも理解しておきたいと考えています。

このチームは、不慣れなコードベースについての疑問に答えるための、プロジェクト専用の/investigateコマンドを作っています。想定している疑問は、「なぜ手数料が二重計上されることがあるのか」「インポーターにテストをどこに追加すべきか」といったものです。このコマンドは、プランを提案する前に、独立した調査をサブエージェントに委任できるコーディネーターを使います。

適応性を保ちながら出力の信頼性も維持できる、最も適したプロンプト設計はどれですか。（2つ選択してください。）

**KO** 한 핀테크 기업의 플랫폼 팀이 소프트웨어 개발 속도를 높이기 위해 Claude Code를 사용하고 있습니다. 코드 생성, refactoring, 디버깅, 문서 작성에 Claude Code를 쓰고 있으며, custom slash command와 CLAUDE.md 설정으로 개발 workflow에 통합했습니다. plan mode와 직접 실행을 어떻게 구분해 쓸지도 이해해 두려고 합니다.

이 팀은 익숙하지 않은 코드베이스에 대한 질문에 답하기 위해 프로젝트 전용 /investigate 명령을 만들고 있습니다. 예상하는 질문은 '왜 수수료가 이중으로 계상되는 경우가 있는가', 'importer에 테스트를 어디에 추가해야 하는가' 같은 것입니다. 이 명령은 plan을 제안하기 전에 독립된 조사를 subagent에게 위임할 수 있는 coordinator를 사용합니다.

적응성을 유지하면서 출력의 신뢰성도 지킬 수 있는, 가장 적합한 prompt 설계는 무엇입니까? (2개를 선택하십시오.)

- A. JA: 依頼された問いに応じて、どの独立した調査を委任するかをコーディネーターに判断させる。
  - KO: 요청받은 질문에 따라, 어떤 독립 조사를 위임할지 coordinator가 판단하게 합니다.
  - EN: Let the coordinator decide which independent investigations to delegate, depending on the question asked.
- B. JA: リポジトリのスキャン・ファイル読み込み・grepパターン・テストコマンド・レポートの節立てを固定の手順で指定する。
  - KO: 저장소 스캔·파일 읽기·grep 패턴·테스트 명령·보고서 절 구성을 고정된 절차로 지정합니다.
  - EN: Specify a fixed procedure for the repository scan, file reads, grep patterns, test commands, and report section structure.
- C. JA: 各サブエージェントに依頼領域を制約なしで広く調査させ、有用と思われる観察結果を何でも返させる。
  - KO: 각 subagent가 요청 영역을 제약 없이 폭넓게 조사하고, 유용해 보이는 관찰 결과는 무엇이든 반환하게 합니다.
  - EN: Have each subagent investigate the requested area broadly without constraints and return any observations it considers useful.
- D. JA: 各調査の目的・求める証拠・出力形式・担当範囲の境界を、委任時の指示で定義する。
  - KO: 각 조사의 목적·필요한 증거·출력 형식·담당 범위의 경계를 위임할 때의 지시에서 정의합니다.
  - EN: Define each investigation's purpose, required evidence, output format, and scope boundaries in the delegation instructions.

## CCAR-F-Udemy03-0053

**JA** あなたは、Claude Agent SDKを使用してマルチエージェントの競合分析システムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、ウェブを検索するもの、文書を分析するもの、調査結果を統合するもの、レポートを生成するものがあります。このシステムはトピックを調査し、出典を明記した包括的なレポートを作成します。

レポート生成サブエージェントは、必須のセクション見出しには従っています。しかし、ある調査結果を次のどれで扱うかの判断が、実行のたびにばらついています。

自信を持って断定的に記述する

根拠が限定的であると留保を付けて記述する

記載を見送る

引き渡されるデータには、出典URL、公開日、根拠となる抜粋がすでに含まれており、出力フォーマット自体はバリデーションに失敗していません。

この判断のばらつきを改善するために最も効果的な変更はどれですか。（2つ選択してください。）

**KO** Claude Agent SDK로 multi-agent 경쟁 분석 시스템을 구축하고 있습니다. coordinator agent가 전문화된 subagent에게 작업을 위임합니다. subagent는 웹 검색, 문서 분석, 조사 결과 통합, 보고서 생성을 각각 맡습니다. 이 시스템은 주제를 조사하고, 출처를 명시한 포괄적인 보고서를 작성합니다.

보고서 생성 subagent는 필수 섹션 제목은 지키고 있습니다. 그러나 어떤 조사 결과를 다음 중 어느 방식으로 다룰지에 대한 판단이 실행할 때마다 달라집니다.

확신을 갖고 단정적으로 서술하기

근거가 제한적이라는 단서를 달아 서술하기

기재하지 않기

전달되는 데이터에는 출처 URL, 공개일, 근거가 되는 발췌가 이미 포함되어 있으며, 출력 형식 자체는 검증에 실패하지 않고 있습니다.

이러한 판단의 편차를 개선하는 데 가장 효과적인 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 最終的なレポート生成ステップにJSONスキーマを強制し、各セクションの項目と出力形式を固定する。
  - KO: 최종 보고서 생성 단계에 JSON schema를 강제해, 각 섹션의 항목과 출력 형식을 고정합니다.
  - EN: Enforce a JSON schema on the final report generation step to fix each section's fields and output format.
- B. JA: 主張と根拠の事例やエッジケースを含む、理想的な書き方の例を3〜5個XMLタグで囲んで追加する。
  - KO: 주장과 근거의 사례 및 edge case를 포함한 이상적인 작성 예시 3~5개를 XML 태그로 감싸 추가합니다.
  - EN: Add 3 to 5 examples of ideal writing, including cases and edge cases of claims and evidence, wrapped in XML tags.
- C. JA: どの根拠の条件なら断定し、どの条件なら留保を付けるか省略するかを、判断ルールとして明示する。
  - KO: 어떤 근거 조건이면 단정하고, 어떤 조건이면 단서를 달거나 생략할지를 판단 규칙으로 명시합니다.
  - EN: State explicitly as decision rules which evidence conditions warrant an assertion and which warrant a caveat or omission.
- D. JA: より幅広い文体に触れさせる目的で、今回とは無関係なレポートの例を多数プロンプトに追加する。
  - KO: 더 다양한 문체를 접하게 할 목적으로, 이번 작업과 무관한 보고서 예시를 prompt에 많이 추가합니다.
  - EN: Add many unrelated report examples to the prompt for the purpose of exposing the model to a wider range of writing styles.

## CCAR-F-Udemy03-0054

**JA** あなたは、保険会社向けに、Claudeを使った保険金請求の受付システムを構築しています。このシステムは、提出書類から情報を抽出し、その結果を検証します。検証のうえで請求を確定し、対応が必要な場合はレビュー担当者向けのチケットを作成します。高い精度が求められるシステムです。クライアント側で実行されるツールとして、extract_claim_fields、validate_claim、submit_claim、create_adjuster_ticketの4つを公開しています。

本番環境のログを確認すると、必須項目の内容があいまいな場合に、Claudeが値を推測し、validate_claimによる検証が成功していないのにsubmit_claimを呼び出してしまうことがあります。アプリケーションはその要求どおりにツール呼び出しを実行するため、本来レビューに回すべき請求がそのまま処理されています。

この必須のワークフローを最も効果的に強制できる変更はどれですか。（2つ選択してください。）

**KO** 보험사를 위해 Claude를 활용한 보험금 청구 접수 시스템을 구축하고 있습니다. 이 시스템은 제출 서류에서 정보를 추출하고, 그 결과를 검증합니다. 검증을 거쳐 청구를 확정하고, 조치가 필요하면 검토 담당자용 티켓을 생성합니다. 높은 정확도가 요구되는 시스템입니다. 클라이언트 쪽에서 실행되는 도구로 extract_claim_fields, validate_claim, submit_claim, create_adjuster_ticket의 4개를 공개하고 있습니다.

운영 환경 로그를 확인해 보니, 필수 항목의 내용이 모호할 때 Claude가 값을 추측하고, validate_claim 검증이 성공하지 않았는데도 submit_claim을 호출하는 경우가 있습니다. 애플리케이션은 요청받은 그대로 도구 호출을 실행하므로, 원래 검토로 넘겨야 할 청구가 그대로 처리되고 있습니다.

이 필수 workflow를 가장 효과적으로 강제할 수 있는 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 同じ請求でvalidate_claimが成功していない限り、submit_claimの実行をアプリケーション側で拒否する。
  - KO: 같은 청구에 대해 validate_claim이 성공하지 않았다면, 애플리케이션 쪽에서 submit_claim 실행을 거부합니다.
  - EN: Have the application reject execution of submit_claim unless validate_claim has succeeded for the same claim.
- B. JA: 検証前のsubmit_claim呼び出しにはis_errorを設定したtool_resultを返し、先に必要な手順を伝える。
  - KO: 검증 전의 submit_claim 호출에는 is_error를 설정한 tool_result를 반환해, 먼저 필요한 절차를 알립니다.
  - EN: For a submit_claim call made before validation, return a tool_result with is_error set that tells Claude which step is required first.
- C. JA: アシスタントのテキストに「提出の準備ができた」のような文言が含まれるたびにエージェントループを停止する。
  - KO: assistant 텍스트에 '제출 준비가 되었다' 같은 문구가 포함될 때마다 agent loop를 멈춥니다.
  - EN: Stop the agent loop whenever the assistant text contains wording such as "ready to submit."
- D. JA: 抽出プロンプトであいまいな項目に言及がある場合は、tool_choiceをvalidate_claimに固定して検証を先に強制する。
  - KO: 추출 prompt에서 모호한 항목이 언급되면 tool_choice를 validate_claim으로 고정해 검증을 먼저 강제합니다.
  - EN: When the extraction prompt mentions an ambiguous field, pin tool_choice to validate_claim to force validation first.

## CCAR-F-Udemy03-0055

**JA** あなたは、Claudeを使用して構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSON（JavaScript Object Notation）スキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携できる必要があります。

検証の際、このシステムはクライアント側のルックアップツールを呼び出し、社内の契約書アーカイブから一致する文書IDを探します。

本番環境のトレースによると、次の2つがどちらも、空の配列を含むtool_resultブロックとしてClaudeに返されています。

ツールのタイムアウト

検索は成功したが、一致する文書が実際に無かった場合

そのため、エージェントはアクセス障害を「確認済みの不在」として扱ってしまっています。

下流の処理のためにこの区別を最も確実に維持できる変更はどれですか。（2つ選択してください。）

**KO** Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON(JavaScript Object Notation) schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동할 수 있어야 합니다.

검증할 때 이 시스템은 클라이언트 쪽 조회 도구를 호출해, 사내 계약서 아카이브에서 일치하는 문서 ID를 찾습니다.

운영 환경 트레이스에 따르면, 다음 두 경우가 모두 빈 배열을 담은 tool_result 블록으로 Claude에게 반환되고 있습니다.

도구 timeout

검색은 성공했지만 일치하는 문서가 실제로 없었던 경우

그 때문에 agent는 접근 장애를 '확인된 부재'로 취급하고 있습니다.

downstream 처리를 위해 이 구분을 가장 확실하게 유지할 수 있는 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 照会の結果を抽出レコード内の独立したステータスフィールドに記録し、下流で区別できるようにする。
  - KO: 조회 결과를 추출 레코드 안의 별도 상태 필드에 기록해, downstream에서 구분할 수 있게 합니다.
  - EN: Record the outcome of the lookup in a separate status field within the extraction record so that it can be distinguished downstream.
- B. JA: 一致なしは成功した空の結果として、タイムアウトはリトライの情報を含むエラーのtool_resultとして返す。
  - KO: 일치 없음은 성공한 빈 결과로, timeout은 재시도 정보를 담은 에러 tool_result로 반환합니다.
  - EN: Return no match as a successful empty result, and return a timeout as an error tool_result that includes retry information.
- C. JA: 一致なしの検索とタイムアウトの失敗をどちらも成功した空の結果として返し、抽出スキーマを単純に保つ。
  - KO: 일치 없는 검색과 timeout 실패를 모두 성공한 빈 결과로 반환해, 추출 schema를 단순하게 유지합니다.
  - EN: Return both the no-match search and the timeout failure as successful empty results, keeping the extraction schema simple.
- D. JA: 成功したMessagesレスポンスのstop_reasonを手がかりに、アーカイブの照会をリトライすべきかどうかを推測させる。
  - KO: 성공한 Messages 응답의 stop_reason을 단서로, 아카이브 조회를 재시도해야 할지 추측하게 합니다.
  - EN: Have Claude infer from the stop_reason of a successful Messages response whether the archive lookup should be retried.

## CCAR-F-Udemy03-0056

**JA** あなたは、通関業務の自動化チーム向けに、Claudeを使用して構造化データ抽出システムを構築しています。このシステムは、非構造化文書から情報を抽出し、JSONスキーマを使用して出力を検証し、高い精度を維持します。エッジケースを適切に処理し、下流のシステムと連携できる必要があります。

この抽出システムには、正式な輸出入禁制品審査報告書から審査結果を抽出するための専用ツールrestricted_goods_flaggerがあります。本番環境のログを確認すると、通常の出荷マニフェストや商業インボイスに「確認要」や「規制品該当」といった語句が含まれているだけで、実際には禁制品に該当する証跡が無い場合でも、このツールが呼び出されています。

ツールの説明文には、正式な禁制品審査報告書向けであると書かれています。一方、あるシステム指示には「【重要】確認・規制・統制・審査に関する語句が現れた場合は必ずrestricted_goods_flaggerを使用すること」と書かれています。

正当な禁制品審査の抽出機能を維持しつつ、この意図しないツールの関連付けを最も直接的に減らせる変更はどれですか。

**KO** 통관 업무 자동화 팀을 위해 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 이 시스템은 비구조화 문서에서 정보를 추출하고, JSON schema로 출력을 검증하며, 높은 정확도를 유지합니다. edge case를 적절히 처리하고 downstream 시스템과 연동할 수 있어야 합니다.

이 추출 시스템에는 정식 수출입 금지품 심사 보고서에서 심사 결과를 추출하는 전용 도구 restricted_goods_flagger가 있습니다. 운영 환경 로그를 확인해 보니, 일반 선적 매니페스트나 상업 송장에 '확인 필요'나 '규제품 해당' 같은 문구가 들어 있기만 하면, 실제로는 금지품에 해당한다는 증거가 없는데도 이 도구가 호출되고 있습니다.

도구 설명에는 정식 금지품 심사 보고서용이라고 적혀 있습니다. 한편 어떤 시스템 지시에는 '【중요】확인·규제·통제·심사에 관한 문구가 나타나면 반드시 restricted_goods_flagger를 사용할 것'이라고 적혀 있습니다.

정당한 금지품 심사 추출 기능은 유지하면서, 이 의도하지 않은 도구 연관을 가장 직접적으로 줄일 수 있는 변경은 무엇입니까?

- A. JA: 規制に関する語句が出現するたびに、tool_choiceをrestricted_goods_flaggerツールに固定する。
  - KO: 규제 관련 문구가 나타날 때마다 tool_choice를 restricted_goods_flagger 도구로 고정합니다.
  - EN: Pin tool_choice to the restricted_goods_flagger tool whenever regulation-related terms appear.
- B. JA: 説明文やプロンプトの文言を変更せずに、restricted_goods_flaggerをreport_parserという名前に変更する。
  - KO: 설명이나 prompt 문구는 바꾸지 않고, restricted_goods_flagger의 이름을 report_parser로 바꿉니다.
  - EN: Rename restricted_goods_flagger to report_parser without changing the description or prompt wording.
- C. JA: システムプロンプトとツールの説明文を、より狭い適用範囲を示す通常の言葉遣いで書き直す。
  - KO: system prompt와 도구 설명을, 더 좁은 적용 범위를 나타내는 평이한 표현으로 다시 씁니다.
  - EN: Rewrite the system prompt and tool description in ordinary wording that indicates a narrower scope of application.
- D. JA: tool_choiceをanyに設定し、どの書類でもいずれかの抽出ツールを呼び出させる。
  - KO: tool_choice를 any로 설정해, 어떤 서류든 추출 도구 중 하나를 호출하게 합니다.
  - EN: Set tool_choice to any so that one of the extraction tools is called for every document.

## CCAR-F-Udemy03-0057

**JA** ある通信会社は、Claude Agent SDKで構築したカスタマーサポートエージェントで、契約照会用のカスタムMCPツールlookup_contractを使っています。パイロットのトレースを確認したところ、次のことが分かりました。

lookup_contractは、契約ごとに英数字のUUID（contract_id、plan_id、device_id）と内部のステータスコードだけを返している

エージェントは顧客に説明するため、これらの値を別の照会で何度も名称に解決し直している

似たUUIDを取り違えて、別の端末の契約内容を説明してしまうことがある

一方、解約手続きを行うcancel_contractの呼び出しには、contract_idが必要です。

lookup_contractの応答の設計として、最も適切な変更はどれですか。

**KO** 한 통신사는 Claude Agent SDK로 구축한 고객 지원 agent에서 계약 조회용 custom MCP 도구 lookup_contract를 사용하고 있습니다. 파일럿 트레이스를 확인해 보니 다음과 같은 사실이 드러났습니다.

lookup_contract는 계약마다 영숫자 UUID(contract_id, plan_id, device_id)와 내부 상태 코드만 반환함

agent는 고객에게 설명하려고 이 값들을 별도 조회로 몇 번이고 다시 이름으로 변환함

비슷한 UUID를 혼동해, 다른 단말기의 계약 내용을 설명하는 경우가 있음

한편 해지 절차를 수행하는 cancel_contract를 호출하려면 contract_id가 필요합니다.

lookup_contract 응답 설계로서 가장 적절한 변경은 무엇입니까?

- A. JA: response_formatでconciseとdetailedを選ばせ、既定は名称と状態、detailedではIDも返す。
  - KO: response_format으로 concise와 detailed 중 하나를 고르게 하고, 기본값은 이름과 상태를, detailed에서는 ID도 반환합니다.
  - EN: Let the agent choose between concise and detailed via response_format, with names and status as the default and IDs also returned in detailed.
- B. JA: lookup_contractの入力スキーマにstrict: trueを設定し、形式に合わないIDでの呼び出しを受け付けない。
  - KO: lookup_contract의 입력 schema에 strict: true를 설정해, 형식에 맞지 않는 ID로 호출하면 받아들이지 않습니다.
  - EN: Set strict: true on the lookup_contract input schema so that calls with IDs that do not match the format are not accepted.
- C. JA: lookup_contractの結果をページ分割し、1回の応答で返す契約の件数を少なく抑える。
  - KO: lookup_contract 결과를 페이지로 나눠, 한 번의 응답으로 반환하는 계약 수를 적게 유지합니다.
  - EN: Paginate the lookup_contract results so that fewer contracts are returned in a single response.
- D. JA: IDを名称へ変換するresolve_idsツールを追加し、顧客へ説明する前の段階でそれを呼び出させる。
  - KO: ID를 이름으로 변환하는 resolve_ids 도구를 추가하고, 고객에게 설명하기 전 단계에서 그것을 호출하게 합니다.
  - EN: Add a resolve_ids tool that converts IDs to names, and have the agent call it before explaining to the customer.

## CCAR-F-Udemy03-0058

**JA** あなたは、Claude Agent SDKを使用して、マルチエージェントの法律調査システムを構築しています。コーディネーターエージェントが、専門化されたサブエージェントに作業を委任します。サブエージェントには、判例を検索するもの、文書を分析するもの、調査結果を統合するもの、調査メモを作成するものがあります。このシステムはトピックを調査し、出典を明記した包括的な調査メモを作成します。

メモ作成担当のサブエージェントが最終的なメモを起草する前に呼び出す、再利用可能な引用監査スキルを作っています。このスキルは、ローカルのテンプレートや引用例を確認する必要がありますが、実行時にファイルを編集したりシェルコマンドを実行したりできてはなりません。

この制約を設定する最良の方法はどれですか。

**KO** Claude Agent SDK로 multi-agent 법률 조사 시스템을 구축하고 있습니다. coordinator agent가 전문화된 subagent에게 작업을 위임합니다. subagent는 판례 검색, 문서 분석, 조사 결과 통합, 조사 메모 작성을 각각 맡습니다. 이 시스템은 주제를 조사하고, 출처를 명시한 포괄적인 조사 메모를 작성합니다.

메모 작성 담당 subagent가 최종 메모를 기안하기 전에 호출하는, 재사용 가능한 인용 감사 skill을 만들고 있습니다. 이 skill은 로컬 템플릿과 인용 예시를 확인해야 하지만, 실행 중에 파일을 편집하거나 셸 명령을 실행할 수 있어서는 안 됩니다.

이 제약을 설정하는 가장 좋은 방법은 무엇입니까?

- A. JA: このワークフローをCLAUDE.mdに移し、編集を避けるよう指示を記載する。
  - KO: 이 workflow를 CLAUDE.md로 옮기고, 편집을 피하라는 지시를 적습니다.
  - EN: Move this workflow into CLAUDE.md and include an instruction to avoid editing.
- B. JA: このワークフローをプロジェクトのスラッシュコマンドでラップし、読み取り専用の振る舞いを依頼する。
  - KO: 이 workflow를 프로젝트 slash command로 감싸고, 읽기 전용으로 동작해 달라고 요청합니다.
  - EN: Wrap this workflow in a project slash command and ask for read-only behavior.
- C. JA: SKILL.mdのフロントマターにdisallowed-tools: Edit Write NotebookEdit Bashを追加する。
  - KO: SKILL.md의 frontmatter에 disallowed-tools: Edit Write NotebookEdit Bash를 추가합니다.
  - EN: Add disallowed-tools: Edit Write NotebookEdit Bash to the SKILL.md frontmatter.
- D. JA: SKILL.mdのフロントマターにallowed-tools: Read Grep Globを追加し、読み取り系のツールに絞る。
  - KO: SKILL.md의 frontmatter에 allowed-tools: Read Grep Glob을 추가해, 읽기 계열 도구로 좁힙니다.
  - EN: Add allowed-tools: Read Grep Glob to the SKILL.md frontmatter to limit it to read-oriented tools.

## CCAR-F-Udemy03-0059

**JA** あなたは、Claude Agent SDKを使用して、航空会社向けのカスタマーサポート解決エージェントを構築しています。このエージェントは、フライト変更、預け荷物のトラブル、返金依頼など、あいまいさの高い問い合わせを処理します。カスタムのModel Context Protocol（MCP）ツール（get_customer、lookup_booking、process_refund、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を達成することです。

返金ポリシーの文言を定義するリポジトリ内のファイルを更新しているときに、Edit呼び出しが失敗しました。Claude Codeはすでにそのファイルを読み込んでいましたが、指定したold_stringが2つのポリシー例文に一致してしまいました。

今回の変更は一方の出現箇所だけに適用するものですが、定型文が繰り返されているため、一意になる正確な置換文字列を作るのは現実的ではありません。

この変更を確実に行うために、Claude Codeに指示すべきことはどれですか。

**KO** Claude Agent SDK로 항공사용 고객 지원 해결 agent를 구축하고 있습니다. 이 agent는 항공편 변경, 위탁 수하물 문제, 환불 요청처럼 모호성이 높은 문의를 처리합니다. custom Model Context Protocol(MCP) 도구(get_customer, lookup_booking, process_refund, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation이 필요한 시점을 판단하면서 첫 문의 해결률 80% 이상을 달성하는 것입니다.

환불 정책 문구를 정의하는 저장소 내 파일을 수정하던 중 Edit 호출이 실패했습니다. Claude Code는 이미 그 파일을 읽은 상태였지만, 지정한 old_string이 정책 예문 2개와 일치해 버렸습니다.

이번 변경은 두 곳 중 한 곳에만 적용해야 하지만, 정형 문구가 반복되고 있어 고유하게 일치하는 정확한 치환 문자열을 만드는 것은 현실적이지 않습니다.

이 변경을 확실하게 수행하려면 Claude Code에 무엇을 지시해야 합니까?

- A. JA: 同じEdit呼び出しでreplace_all: trueを設定し、一致するポリシー文言をすべて一貫して変更する。
  - KO: 같은 Edit 호출에서 replace_all: true를 설정해, 일치하는 정책 문구를 모두 일관되게 변경합니다.
  - EN: Set replace_all: true in the same Edit call to change all matching policy wording consistently.
- B. JA: 現在のファイル内容を読み込み、意図した完成形のファイル全体を組み立てたうえで、Writeを使ってそのファイルを上書きする。
  - KO: 현재 파일 내용을 읽어 들이고, 의도한 최종 형태의 파일 전체를 구성한 뒤, Write로 그 파일을 덮어씁니다.
  - EN: Read the current file contents, assemble the entire intended final file, and then overwrite the file using Write.
- C. JA: old_stringを短くしてEditをリトライし、Claude Codeに最も近い一致箇所を選ばせる。
  - KO: old_string을 짧게 줄여 Edit을 재시도하고, 가장 가까운 일치 위치를 Claude Code가 고르게 합니다.
  - EN: Shorten old_string and retry the Edit, letting Claude Code choose the closest match.
- D. JA: old_stringを、対象の段落に一致する任意の空白を許容する正規表現パターンに変更する。
  - KO: old_string을, 대상 단락과 일치하면서 임의의 공백을 허용하는 정규 표현식 패턴으로 바꿉니다.
  - EN: Change old_string to a regular expression pattern that matches the target paragraph while allowing arbitrary whitespace.

## CCAR-F-Udemy03-0060

**JA** あるサブスクリプション型動画配信サービスの運用エンジニアリングチームが、Claude Agent SDKを使用してカスタマーサポート解決エージェントを構築しています。このエージェントは、返品、料金請求に関する問い合わせ、アカウントの問題など、あいまいさの高い依頼を処理します。カスタムのModel Context Protocol（MCP）ツール（get_customer、lookup_order、process_refund、escalate_to_human）を通じて、バックエンドシステムにアクセスできます。目標は、エスカレーションすべきタイミングを見極めながら、初回解決率80%以上を達成することです。

このチームは、料金請求に関する紛争の処理を、より低レベルのMessages APIのツールループとして実装しています。パイロットの結果、オーケストレーション層がすべての料金請求の紛争を、同じ固定の経路に割り当てていることが分かりました。しかし実際には、案件によって必要な対応が異なります。

ポリシーの説明だけで済むケース

注文の照会が必要なケース

返金処理の前にエスカレーションすべきケース

Claudeのツール利用モデルに最も合った変更はどれですか。（2つ選択してください。）

**KO** 한 구독형 동영상 streaming 서비스의 운영 엔지니어링 팀이 Claude Agent SDK로 고객 지원 해결 agent를 구축하고 있습니다. 이 agent는 반품, 요금 청구 문의, 계정 문제처럼 모호성이 높은 요청을 처리합니다. custom Model Context Protocol(MCP) 도구(get_customer, lookup_order, process_refund, escalate_to_human)를 통해 백엔드 시스템에 접근할 수 있습니다. 목표는 escalation이 필요한 시점을 판단하면서 첫 문의 해결률 80% 이상을 달성하는 것입니다.

이 팀은 요금 청구 분쟁 처리를 더 저수준인 Messages API의 도구 loop로 구현하고 있습니다. 파일럿 결과, orchestration 계층이 모든 요금 청구 분쟁을 같은 고정 경로에 배정하고 있다는 것이 드러났습니다. 그러나 실제로는 건마다 필요한 대응이 다릅니다.

정책 설명만으로 해결되는 경우

주문 조회가 필요한 경우

환불 처리 전에 escalation해야 하는 경우

Claude의 tool use 모델에 가장 잘 맞는 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 意図分類器を通じて各依頼をルーティングし、そのサブタイプ用にあらかじめ定義された1つのサポートツールの連鎖を選択させる。
  - KO: 의도 분류기를 거쳐 각 요청을 routing하고, 해당 하위 유형용으로 미리 정의된 지원 도구 체인 하나를 선택하게 합니다.
  - EN: Route each request through an intent classifier and select one predefined chain of support tools for that subtype.
- B. JA: stop_reasonが"end_turn"の応答を受け取った時点でループを終了し、その応答のテキストを最終的な顧客向け回答として扱う。
  - KO: stop_reason이 "end_turn"인 응답을 받은 시점에 loop를 종료하고, 그 응답의 텍스트를 고객에게 보낼 최종 답변으로 취급합니다.
  - EN: End the loop when a response with stop_reason "end_turn" is received, and treat that response's text as the final customer-facing answer.
- C. JA: stop_reasonに基づくループを実行し、tool_choiceを{"type":"auto"}に設定して、各ターンでツールの利用か最終回答かをClaudeに選ばせる。
  - KO: stop_reason에 기반한 loop를 실행하고 tool_choice를 {"type":"auto"}로 설정해, 매 turn마다 도구를 쓸지 최종 답변을 할지 Claude가 선택하게 합니다.
  - EN: Run a loop based on stop_reason with tool_choice set to {"type":"auto"}, letting Claude choose on each turn between using a tool and giving a final answer.
- D. JA: tool_choiceを{"type":"tool","name":"process_refund"}のように設定し、アプリケーション側が管理するワークフロー状態に従って、各ターンで次のサポートツールを強制する。
  - KO: tool_choice를 {"type":"tool","name":"process_refund"}처럼 설정해, 애플리케이션이 관리하는 workflow 상태에 따라 매 turn마다 다음 지원 도구를 강제합니다.
  - EN: Set tool_choice to something like {"type":"tool","name":"process_refund"} and force the next support tool on each turn according to workflow state managed by the application.

## CCAR-F-Udemy04-0001

**JA** ある航空機整備会社の開発チームは、CIパイプラインでClaude Codeを使い、プルリクエストごとに整備記録モジュールのユニットテストを生成しています。テストの書き方の規約と、tests/fixtures/にある整備記録のフィクスチャの使い方は、リポジトリのルートのCLAUDE.mdに書いてコミットしています。

先週、CIジョブのコマンドをclaude -pからclaude --bare -p --output-format jsonに変更し、同じ週にCLAUDE.mdへ規約を3項目追記しました。それ以降、生成されるテストはフィクスチャを使わず、整備記録のデータを毎回一から組み立てるようになりました。

最も可能性の高い根本原因はどれですか。

**KO** 한 항공기 정비 회사의 개발팀은 CI pipeline에서 Claude Code를 사용해, pull request마다 정비 기록 모듈의 단위 테스트를 생성합니다. 테스트 작성 규약과 tests/fixtures/에 있는 정비 기록 fixture의 사용법은 저장소 루트의 CLAUDE.md에 적어 commit해 두었습니다.

지난주 CI job의 명령을 claude -p에서 claude --bare -p --output-format json으로 바꾸었고, 같은 주에 CLAUDE.md에 규약 3개 항목을 추가했습니다. 그 이후 생성되는 테스트는 fixture를 쓰지 않고, 정비 기록 데이터를 매번 처음부터 직접 만들고 있습니다.

가장 가능성이 높은 근본 원인은 무엇입니까?

- A. JA: CLAUDE.mdに規約を追記したことで、フィクスチャの使い方の記述が埋もれている。
  - KO: CLAUDE.md에 규약을 추가하면서 fixture 사용법에 대한 내용이 묻혀 버렸습니다.
  - EN: Adding conventions to CLAUDE.md has buried the description of how to use the fixtures.
- B. JA: --output-format jsonの指定により、出力形式の指示がCLAUDE.mdの規約より優先されている。
  - KO: --output-format json을 지정하면서 출력 형식 지시가 CLAUDE.md의 규약보다 우선 적용되고 있습니다.
  - EN: Specifying --output-format json has caused the output format instructions to take precedence over the conventions in CLAUDE.md.
- C. JA: 非対話モードでは、tests/fixtures/のファイルを読む権限が承認されないまま実行されている。
  - KO: 비대화형 모드에서는 tests/fixtures/의 파일을 읽을 권한이 승인되지 않은 채 실행되고 있습니다.
  - EN: In non-interactive mode, the job runs without approval of permission to read files in tests/fixtures/.
- D. JA: --bareを付けたことで、CLAUDE.mdが自動では読み込まれなくなっている。
  - KO: --bare를 붙였기 때문에 CLAUDE.md가 자동으로 로드되지 않게 되었습니다.
  - EN: Adding --bare has caused CLAUDE.md to no longer be loaded automatically.

## CCAR-F-Udemy04-0002

**JA** ある人材紹介会社の開発チームは、Claude Agent SDKでカスタマーサポート解決エージェントを構築しています。エージェントは、求職者からの問い合わせに答えるため、MCPツールget_candidateで登録情報を取得します。ただし、このツールの結果には、個人番号（マイナンバー）と給与振込口座の番号も含まれています。

社内規程では、これらの項目をモデルに渡すことを禁止しています。現在はシステムプロンプトで「個人番号と口座番号は回答に含めないこと」と指示していますが、監査で、モデルへの入力にこれらの項目が含まれていることが問題視されました。

モデルがこれらの項目を受け取らないようにする方法として適切なものはどれですか。（2つ選択してください。）

**KO** 한 인재 소개 회사의 개발팀은 Claude Agent SDK로 고객 지원 해결 agent를 구축하고 있습니다. agent는 구직자의 문의에 답하기 위해 MCP 도구 get_candidate로 등록 정보를 가져옵니다. 그런데 이 도구의 결과에는 개인번호(마이넘버)와 급여 이체 계좌 번호도 포함되어 있습니다.

사내 규정은 이 항목들을 모델에 전달하는 것을 금지합니다. 현재는 system prompt에서 '개인번호와 계좌 번호는 답변에 포함하지 말 것'이라고 지시하고 있지만, 감사에서 모델 입력에 이 항목들이 포함되어 있다는 점이 문제로 지적되었습니다.

모델이 이 항목들을 받지 않도록 하는 방법으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: PostToolUseフックでget_candidateの結果から個人番号と口座番号を除き、updatedToolOutputで置き換える。
  - KO: PostToolUse hook으로 get_candidate 결과에서 개인번호와 계좌 번호를 제거하고, updatedToolOutput으로 바꿔 넣습니다.
  - EN: Use a PostToolUse hook to remove the individual number and account number from the get_candidate result and replace it via updatedToolOutput.
- B. JA: PreToolUseフックでget_candidateの呼び出しをすべて拒否し、登録情報は担当者が確認してから回答する運用にする。
  - KO: PreToolUse hook으로 get_candidate 호출을 모두 거부하고, 등록 정보는 담당자가 확인한 뒤 답변하는 방식으로 운영합니다.
  - EN: Use a PreToolUse hook to deny all get_candidate calls, and adopt a procedure in which a human agent reviews the registration information before responding.
- C. JA: システムプロンプトの指示を強調表現で書き直し、個人番号を回答に含めた悪い例と正しい例をfew-shotで示す。
  - KO: system prompt 지시를 강조 표현으로 다시 쓰고, 개인번호를 답변에 포함한 나쁜 예와 올바른 예를 few-shot으로 보여 줍니다.
  - EN: Rewrite the system prompt instruction with emphasis and show bad and correct examples of including the individual number in a response using few-shot examples.
- D. JA: MCPサーバー側のget_candidateの応答を変更し、個人番号と口座番号をエージェント向けの結果に含めない。
  - KO: MCP server 쪽 get_candidate 응답을 변경해, 개인번호와 계좌 번호를 agent용 결과에 포함하지 않습니다.
  - EN: Change the get_candidate response on the MCP server side so that the individual number and account number are not included in the results for the agent.

## CCAR-F-Udemy04-0003

**JA** ある自動車部品メーカーの開発チームは、継続的インテグレーションのパイプラインにClaude Codeを組み込んでいます。車載ECUのファームウェアについては、Claudeがコードを生成した直後に、同じセッションで「今のコードをレビューして」と指示するステップがあります。

しかし、後の結合試験で、境界値でのオーバーフローや割り込み処理の競合など、見つけにくい不具合が見つかる例が続いています。

レビューの効果を高める変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 자동차 부품 제조사의 개발팀은 지속적 통합 pipeline에 Claude Code를 넣어 두었습니다. 차량용 ECU 펌웨어의 경우, Claude가 코드를 생성한 직후 같은 session에서 '방금 작성한 코드를 리뷰해 줘'라고 지시하는 단계가 있습니다.

하지만 이후 통합 시험에서 경곗값에서의 오버플로나 인터럽트 처리의 경합처럼 찾기 어려운 결함이 발견되는 사례가 이어지고 있습니다.

리뷰 효과를 높이는 변경으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 同じセッションで拡張思考を有効にし、生成したコードを時間をかけて見直させる。
  - KO: 같은 session에서 extended thinking을 활성화해, 생성한 코드를 시간을 들여 다시 검토하게 합니다.
  - EN: Enable extended thinking in the same session and have Claude spend more time reviewing the code it generated.
- B. JA: レビュー側には差分と要件仕様だけを渡し、生成時の説明や推論の過程は渡さない。
  - KO: 리뷰 쪽에는 diff와 요구 사양만 전달하고, 생성 시의 설명이나 추론 과정은 전달하지 않습니다.
  - EN: Give the reviewer only the diff and the requirements specification, and do not pass along the explanations or reasoning from the generation step.
- C. JA: 生成時の会話記録をレビュー側に渡し、設計の意図を理解したうえで確認させる。
  - KO: 생성 시의 대화 기록을 리뷰 쪽에 전달해, 설계 의도를 이해한 상태에서 확인하게 합니다.
  - EN: Pass the conversation record from generation to the reviewer so that it can verify the code after understanding the design intent.
- D. JA: 生成とは別のClaudeインスタンスを起動し、そのインスタンスにレビューを担当させる。
  - KO: 생성과는 별도의 Claude 인스턴스를 띄워, 그 인스턴스가 리뷰를 담당하게 합니다.
  - EN: Launch a separate Claude instance from the one that generated the code and have that instance perform the review.

## CCAR-F-Udemy04-0004

**JA** ある不動産会社の開発チームは、Claude Codeを開発ワークフローに統合しようとしています。Claudeから、次の3つを扱えるようにしたいと考えています。

GitHubのイシューとプルリクエスト

Slackのチャンネル

社内の物件管理データベース（価格改定を2段階で承認する社内独自のワークフローがある）

担当者は、3つすべてについてカスタムのMCPサーバーを自作する計画を立てています。

この計画の見直しとして適切なものはどれですか。（2つ選択してください。）

**KO** 한 부동산 회사의 개발팀은 Claude Code를 개발 workflow에 통합하려고 합니다. Claude에서 다음 3가지를 다룰 수 있게 하려고 합니다.

GitHub의 issue와 pull request

Slack 채널

사내 매물 관리 데이터베이스(가격 변경을 2단계로 승인하는 사내 고유 workflow가 있음)

담당자는 3가지 모두에 대해 custom MCP server를 직접 만들 계획을 세우고 있습니다.

이 계획을 재검토하는 방안으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: カスタムMCPサーバーは、物件管理データベースの承認ワークフローに限って作る。
  - KO: custom MCP server는 매물 관리 데이터베이스의 승인 workflow에 한해서만 만듭니다.
  - EN: Build a custom MCP server only for the property management database's approval workflow.
- B. JA: MCPは使わず、各APIをcurlで呼ぶ手順をCLAUDE.mdに書いてBashで実行させる。
  - KO: MCP는 쓰지 않고, 각 API를 curl로 호출하는 절차를 CLAUDE.md에 적어 Bash로 실행하게 합니다.
  - EN: Do not use MCP; instead, write procedures for calling each API with curl in CLAUDE.md and have Claude run them with Bash.
- C. JA: GitHubとSlackには、既存のコミュニティ製や公式のMCPサーバーを使う。
  - KO: GitHub와 Slack에는 기존 커뮤니티 제작 MCP server나 공식 MCP server를 사용합니다.
  - EN: Use existing community-built or official MCP servers for GitHub and Slack.
- D. JA: 3つの連携を1つのカスタムMCPサーバーにまとめ、保守する対象を1つにする。
  - KO: 3가지 연동을 하나의 custom MCP server로 묶어, 유지보수 대상을 하나로 만듭니다.
  - EN: Combine the three integrations into a single custom MCP server so that there is only one thing to maintain.

## CCAR-F-Udemy04-0005

**JA** ある研究機関の共同利用施設では、外部の研究者からの問い合わせに答えるカスタマーサポート解決エージェントを、Claude Agent SDKで構築しています。装置の利用料を返金するprocess_refundについては、「同じセッション内でget_customerが呼ばれるまで呼び出しを拒否する」前提条件ゲートを実装しました。

ところが監査で、get_customerが「該当する利用者が2名います」という結果を返した会話でも、その後のprocess_refundが実行され、別の研究者の口座に返金されていたことが分かりました。

最も可能性の高い原因はどれですか。

**KO** 한 연구 기관의 공동 이용 시설에서는 외부 연구자의 문의에 답하는 고객 지원 해결 agent를 Claude Agent SDK로 구축하고 있습니다. 장비 이용료를 환불하는 process_refund에는 '같은 session 안에서 get_customer가 호출될 때까지 호출을 거부한다'는 전제 조건 게이트를 구현했습니다.

그런데 감사에서, get_customer가 '해당하는 이용자가 2명 있습니다'라는 결과를 반환한 대화에서도 이후 process_refund가 실행되어 다른 연구자의 계좌로 환불된 사실이 드러났습니다.

가장 가능성이 높은 원인은 무엇입니까?

- A. JA: process_refundの説明が短く、エージェントが使うべき場面を判断できていない。
  - KO: process_refund의 설명이 짧아, agent가 언제 사용해야 하는지 판단하지 못하고 있습니다.
  - EN: The description of process_refund is short, so the agent cannot judge when it should be used.
- B. JA: tool_choiceが"auto"のままで、get_customerの呼び出しが強制されていない。
  - KO: tool_choice가 "auto"인 채로 남아 있어, get_customer 호출이 강제되지 않고 있습니다.
  - EN: tool_choice is still "auto", so calling get_customer is not forced.
- C. JA: システムプロンプトに、返金の前に本人確認を行うという指示が書かれていない。
  - KO: system prompt에 환불 전에 본인 확인을 하라는 지시가 적혀 있지 않습니다.
  - EN: The system prompt does not include an instruction to verify the customer's identity before issuing a refund.
- D. JA: ゲートが、get_customerの呼び出しの有無だけを見て、検証済みのIDを確かめていない。
  - KO: 게이트가 get_customer 호출 여부만 보고, 검증된 ID인지는 확인하지 않습니다.
  - EN: The gate only checks whether get_customer was called and does not check for a verified ID.

## CCAR-F-Udemy04-0006

**JA** ある広告会社の開発チームは、Claudeで構造化データ抽出システムを構築しています。広告主との契約書から、契約開始日・契約終了日・月額料金・自動更新の有無を抽出し、請求システムへ登録します。抽出スキーマでは、4つのフィールドをいずれも必須にしています。

ところが、契約書の約30%は自動更新型で、終了日の記載がありません。その場合でも、「2099-12-31」や「契約開始日の1年後」といった、契約書にない終了日が出力されていました。

最も適切な対処はどれですか。

**KO** 한 광고 회사의 개발팀은 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 광고주와의 계약서에서 계약 시작일·계약 종료일·월 요금·자동 갱신 여부를 추출해 청구 시스템에 등록합니다. 추출 schema에서는 4개 필드를 모두 필수로 지정했습니다.

그런데 계약서의 약 30%는 자동 갱신형이라 종료일이 적혀 있지 않습니다. 그런 경우에도 '2099-12-31'이나 '계약 시작일로부터 1년 후'처럼 계약서에 없는 종료일이 출력되고 있었습니다.

가장 적절한 대처는 무엇입니까?

- A. JA: 契約終了日をnull許容の任意フィールドにし、記載がなければnullを返させる。
  - KO: 계약 종료일을 null을 허용하는 선택 필드로 바꾸고, 기재가 없으면 null을 반환하게 합니다.
  - EN: Make the contract end date an optional, nullable field and have Claude return null when it is not stated.
- B. JA: ツール定義にstrict: trueを設定し、スキーマどおりの値を返させる。
  - KO: 도구 정의에 strict: true를 설정해, schema에 맞는 값을 반환하게 합니다.
  - EN: Set strict: true in the tool definition so that Claude returns values that conform to the schema.
- C. JA: 後処理で、終了日が2099年の値を契約開始日の1年後に置き換えて登録する。
  - KO: 후처리에서 종료일이 2099년인 값을 계약 시작일로부터 1년 후로 바꿔 등록합니다.
  - EN: In post-processing, replace end dates in 2099 with one year after the contract start date before registering them.
- D. JA: プロンプトに「契約書に書かれていない日付は推測しないこと」と追記する。
  - KO: prompt에 '계약서에 적혀 있지 않은 날짜는 추측하지 말 것'이라고 추가합니다.
  - EN: Add "Do not guess dates that are not written in the contract" to the prompt.

## CCAR-F-Udemy04-0007

**JA** ある保険会社の開発チームは、Claude Codeで契約管理システムを開発しています。リポジトリのルートのCLAUDE.mdはチームで共有してコミットしていますが、最近はメンバーが自分専用の内容も書き足すようになりました。たとえば、次のような行です。

「検証環境には自分用のsbx-tanakaサーバーを使う」

「テストには自分が担当する契約番号P-20871を使う」

その結果、他のメンバーのClaudeが別人の検証環境に接続しようとしたり、こうした行の編集でマージの競合が起きたりしています。

CLAUDE.mdの構成の見直しとして適切なものはどれですか。（2つ選択してください。）

**KO** 한 보험사의 개발팀은 Claude Code로 계약 관리 시스템을 개발하고 있습니다. 저장소 루트의 CLAUDE.md는 팀이 공유하며 commit하고 있는데, 최근 팀원들이 자기만을 위한 내용도 덧붙이기 시작했습니다. 예를 들면 다음과 같은 줄입니다.

'검증 환경으로는 내 전용 sbx-tanaka 서버를 쓴다'

'테스트에는 내가 담당하는 계약 번호 P-20871을 쓴다'

그 결과 다른 팀원의 Claude가 다른 사람의 검증 환경에 접속하려 하거나, 이런 줄을 편집하다가 merge 충돌이 일어나고 있습니다.

CLAUDE.md 구성을 재검토하는 방안으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: コミットするCLAUDE.mdには、ビルド手順や規約など、チーム全員に共通する内容だけを残す。
  - KO: commit하는 CLAUDE.md에는 빌드 절차나 규약처럼 팀 전원에게 공통된 내용만 남깁니다.
  - EN: Keep only content common to the whole team, such as build procedures and conventions, in the committed CLAUDE.md.
- B. JA: メンバーごとに.claude/rules/に個人用のファイルを作り、担当するディレクトリをpathsで指定する。
  - KO: 팀원마다 .claude/rules/에 개인용 파일을 만들고, 담당 디렉터리를 paths로 지정합니다.
  - EN: Create a personal file in .claude/rules/ for each member and specify the directories they are responsible for with paths.
- C. JA: 各メンバー専用の内容は、プロジェクトのルートのCLAUDE.local.mdに移し、.gitignoreに追加する。
  - KO: 각 팀원 전용 내용은 프로젝트 루트의 CLAUDE.local.md로 옮기고, .gitignore에 추가합니다.
  - EN: Move each member's personal content to CLAUDE.local.md at the project root and add it to .gitignore.
- D. JA: 各メンバー専用の内容は、各自のホームディレクトリの~/.claude/CLAUDE.mdに移す。
  - KO: 각 팀원 전용 내용은 각자의 홈 디렉터리에 있는 ~/.claude/CLAUDE.md로 옮깁니다.
  - EN: Move each member's personal content to ~/.claude/CLAUDE.md in their own home directory.

## CCAR-F-Udemy04-0008

**JA** あるSaaS企業の開発チームは、Claude Agent SDKで開発者の生産性向上ツールを構築しています。このツールには、次の2つの機能があります。

プルリクエストごとに、ライセンスヘッダー・変更履歴の記載・公開APIの互換性の3点を確認する定型チェック

「レガシーの課金サービスがなぜ遅いのか調べて」のような、範囲の決まっていない調査の依頼

現在はどちらも同じ汎用エージェントが処理しており、定型チェックでは確認項目が実行ごとに抜けたり増えたりしています。

タスク分解の設計として適切なものはどれですか。（2つ選択してください。）

**KO** 한 SaaS 기업의 개발팀은 Claude Agent SDK로 개발자 생산성 향상 도구를 구축하고 있습니다. 이 도구에는 다음 2가지 기능이 있습니다.

pull request마다 라이선스 헤더·변경 이력 기재·공개 API 호환성의 3가지를 확인하는 정형 검사

'레거시 과금 서비스가 왜 느린지 조사해 줘' 같은, 범위가 정해지지 않은 조사 요청

현재는 둘 다 같은 범용 agent가 처리하고 있으며, 정형 검사에서는 실행할 때마다 확인 항목이 빠지거나 늘어나고 있습니다.

작업 분해 설계로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 調査の依頼は、途中の発見に応じてサブタスクを追加する動的な分解で処理する。
  - KO: 조사 요청은 도중의 발견에 따라 하위 작업을 추가하는 동적 분해로 처리합니다.
  - EN: Handle the investigation request with dynamic decomposition, adding subtasks as findings emerge along the way.
- B. JA: 調査の依頼では、最初にsrc配下のファイルを読み込ませてから、1回のプロンプトで原因を特定させる。
  - KO: 조사 요청에서는 먼저 src 아래의 파일을 읽어 들이게 한 뒤, 한 번의 prompt로 원인을 찾아내게 합니다.
  - EN: For the investigation request, first have the agent read the files under src, then identify the cause in a single prompt.
- C. JA: 両機能を1つのエージェントのまま、反復回数の上限を下げて応答のぶれを抑える。
  - KO: 두 기능을 하나의 agent로 유지한 채, 반복 횟수 상한을 낮춰 응답의 편차를 줄입니다.
  - EN: Keep both features in one agent and lower the iteration limit to reduce variation in responses.
- D. JA: 定型チェックは、3つの確認を決まった順に行うプロンプトチェーンにする。
  - KO: 정형 검사는 3가지 확인을 정해진 순서로 수행하는 prompt chain으로 만듭니다.
  - EN: Make the routine check a prompt chain that performs the three checks in a fixed order.

## CCAR-F-Udemy04-0009

**JA** ある出版社の開発チームは、Claude Agent SDKでマルチエージェントリサーチシステムを構築しています。編集部が定めた品質基準には、「市場規模や利用者数などの数値は、2つ以上の独立した出典で裏付ける」とあります。

「国内の電子書籍市場の動向」を調べたところ、統合サブエージェントの草稿には数値を含む主張が14件あり、そのうち3件は出典が1件しかありませんでした。現在のコーディネーターは、統合サブエージェントの草稿を確認せずに、そのままレポート生成サブエージェントに渡しています。

最も適切な改善策はどれですか。

**KO** 한 출판사의 개발팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. 편집부가 정한 품질 기준에는 '시장 규모나 이용자 수 같은 수치는 2개 이상의 독립된 출처로 뒷받침한다'라고 되어 있습니다.

'국내 전자책 시장의 동향'을 조사했더니, 통합 subagent의 초안에 수치를 포함한 주장이 14건 있었고, 그중 3건은 출처가 1건뿐이었습니다. 현재 coordinator는 통합 subagent의 초안을 확인하지 않고 그대로 보고서 생성 subagent에 넘기고 있습니다.

가장 적절한 개선책은 무엇입니까?

- A. JA: 草稿を品質基準と照合し、裏付けの足りない3件だけを再度委任してから統合をやり直す。
  - KO: 초안을 품질 기준과 대조하고, 뒷받침이 부족한 3건만 다시 위임한 뒤 통합을 다시 수행합니다.
  - EN: Check the draft against the quality standard, re-delegate only the 3 insufficiently supported claims, and then redo the synthesis.
- B. JA: 草稿を編集部に回し、担当者が品質基準との照合を終えてから再実行を指示する。
  - KO: 초안을 편집부로 보내, 담당자가 품질 기준과의 대조를 마친 뒤 재실행을 지시하게 합니다.
  - EN: Send the draft to the editorial department, and have the person in charge finish checking it against the quality standard before instructing a rerun.
- C. JA: 出典が1件の主張に「裏付けは1件」と注記させ、そのままレポート生成に進める。
  - KO: 출처가 1건인 주장에 '뒷받침 1건'이라고 주석을 달게 하고, 그대로 보고서 생성으로 넘어갑니다.
  - EN: Have the single-source claims annotated with "supported by one source" and proceed to report generation as is.
- D. JA: 検索・分析・統合のすべてを最初から実行し直し、得られた新しい草稿で置き換える。
  - KO: 검색·분석·통합을 모두 처음부터 다시 실행하고, 새로 얻은 초안으로 교체합니다.
  - EN: Rerun all of search, analysis, and synthesis from the beginning and replace the draft with the new draft obtained.

## CCAR-F-Udemy04-0010

**JA** ある国際協力NGOの開発チームは、開発の生産性を上げるためにClaude Codeを使っています。あるエンジニアが、個人で試している翻訳用のMCPサーバーを、自分が担当する5つのリポジトリのどれで作業するときにも使いたいと考えています。このサーバーはまだ試作段階で、チームの他のメンバーには共有したくありません。

このMCPサーバーの設定方法として最も適切なものはどれですか。

**KO** 한 국제 협력 NGO의 개발팀은 개발 생산성을 높이기 위해 Claude Code를 사용하고 있습니다. 한 엔지니어가 개인적으로 시험 중인 번역용 MCP server를, 자신이 담당하는 5개 저장소 중 어디에서 작업하든 쓰고 싶어 합니다. 이 서버는 아직 시제품 단계라, 팀의 다른 구성원과는 공유하고 싶지 않습니다.

이 MCP server를 설정하는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: 最初に作業するリポジトリで、ローカルスコープとして1回だけ追加する。
  - KO: 처음 작업하는 저장소에서 local scope로 한 번만 추가합니다.
  - EN: Add it once as local scope in the first repository they work in.
- B. JA: 5つのリポジトリそれぞれの.mcp.jsonに追加し、コミットしてチームで共有する。
  - KO: 5개 저장소 각각의 .mcp.json에 추가하고, commit해 팀과 공유합니다.
  - EN: Add it to the .mcp.json of each of the five repositories, commit it, and share it with the team.
- C. JA: ユーザースコープで追加し、~/.claude.jsonに保存されるようにする。
  - KO: user scope로 추가해, ~/.claude.json에 저장되게 합니다.
  - EN: Add it at user scope so that it is stored in ~/.claude.json.
- D. JA: 各リポジトリの.mcp.jsonに追加し、.gitignoreで.mcp.jsonをコミット対象から外す。
  - KO: 각 저장소의 .mcp.json에 추가하고, .gitignore로 .mcp.json을 commit 대상에서 제외합니다.
  - EN: Add it to the .mcp.json of each repository and exclude .mcp.json from being committed via .gitignore.

## CCAR-F-Udemy04-0011

**JA** ある外食業界向け市場調査会社の開発チームは、Claude Agent SDKでマルチエージェントリサーチシステムを構築しています。コーディネーターが、ウェブ検索・文書分析・統合・レポート生成の各サブエージェントに作業を委任します。

「国内フードデリバリー市場の規模」を調査したところ、文書分析サブエージェントが読んだ2つの業界団体レポートで、市場規模が1.8兆円（2025年版）と2.4兆円（2026年版）に食い違っていました。現在のサブエージェントは、矛盾を見つけた時点で分析を打ち切り、「データ不整合」というエラーだけを返しています。

この食い違いの扱いとして適切なものはどれですか。（2つ選択してください。）

**KO** 외식업계를 대상으로 하는 한 시장 조사 회사의 개발팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. coordinator가 웹 검색·문서 분석·통합·보고서 생성의 각 subagent에게 작업을 위임합니다.

'국내 음식 배달 시장의 규모'를 조사했더니, 문서 분석 subagent가 읽은 두 업계 단체 보고서에서 시장 규모가 1.8조 엔(2025년판)과 2.4조 엔(2026년판)으로 서로 달랐습니다. 현재 subagent는 모순을 발견하는 즉시 분석을 중단하고 '데이터 불일치'라는 에러만 반환합니다.

이 불일치를 다루는 방법으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: どちらの値を採用するかの判断はコーディネーターに任せ、サブエージェントには判断材料をそろえて返させる。
  - KO: 어느 값을 채택할지는 coordinator가 판단하도록 맡기고, subagent에게는 판단에 필요한 자료를 갖춰 반환하게 합니다.
  - EN: Leave the decision of which value to adopt to the coordinator, and have the subagent return with the materials needed to make that decision.
- B. JA: 両方の値を出典情報とともに残し、矛盾を明示したうえで分析を最後まで完了させる。
  - KO: 두 값을 출처 정보와 함께 남기고, 모순을 명시한 상태로 분석을 끝까지 완료합니다.
  - EN: Keep both values along with their source information, explicitly flag the contradiction, and complete the analysis to the end.
- C. JA: 公開日が新しい2026年版の値を正として採用し、2025年版の値は出力から外すようサブエージェントに指示する。
  - KO: 공개일이 더 최근인 2026년판 값을 올바른 값으로 채택하고, 2025년판 값은 출력에서 빼도록 subagent에 지시합니다.
  - EN: Instruct the subagent to adopt the value from the 2026 edition, which has the newer publication date, as correct and to remove the 2025 edition value from its output.
- D. JA: 2つの値の平均である2.1兆円を市場規模として算出し、2つの出典を併記して統合サブエージェントに渡す。
  - KO: 두 값의 평균인 2.1조 엔을 시장 규모로 계산하고, 두 출처를 함께 적어 통합 subagent에 넘깁니다.
  - EN: Calculate 2.1 trillion yen, the average of the two values, as the market size, and pass it to the synthesis subagent with the two sources listed together.

## CCAR-F-Udemy04-0012

**JA** ある音楽配信会社の開発チームは、Claude Agent SDKで開発者の生産性向上ツールを構築しています。このエージェントでは、組み込みのRead・Grep・Globが有効になっています。

新しく配属されたエンジニアが「楽曲の再生回数から権利者への分配額を計算する流れを知りたい」と依頼したところ、エージェントはsrc配下の約900ファイルを先頭から順にReadで読み始め、途中でコンテキストが足りなくなりました。なお、分配額の計算をcalculateRoyaltyという関数が担当していることは分かっています。

最初の手順として最も適切なものはどれですか。

**KO** 한 음악 streaming 회사의 개발팀은 Claude Agent SDK로 개발자 생산성 향상 도구를 구축하고 있습니다. 이 agent에서는 내장 Read·Grep·Glob이 활성화되어 있습니다.

새로 배치된 엔지니어가 '곡 재생 횟수로 권리자 배분액을 계산하는 흐름을 알고 싶다'고 요청하자, agent는 src 아래 약 900개 파일을 처음부터 순서대로 Read로 읽기 시작했고, 도중에 context가 부족해졌습니다. 참고로 배분액 계산은 calculateRoyalty라는 함수가 담당한다는 것이 알려져 있습니다.

첫 단계로 가장 적절한 것은 무엇입니까?

- A. JA: Bashのcatでsrc配下のファイルを連結し、1回のツール呼び出しでまとめて読み込む。
  - KO: Bash의 cat으로 src 아래 파일을 이어 붙여, 한 번의 도구 호출로 한꺼번에 읽어 들입니다.
  - EN: Concatenate the files under src with Bash cat and read them all at once in a single tool call.
- B. JA: GrepでcalculateRoyaltyの定義と呼び出し箇所を探し、そこからReadでimportをたどる。
  - KO: Grep으로 calculateRoyalty의 정의와 호출 위치를 찾고, 거기서부터 Read로 import를 따라갑니다.
  - EN: Use Grep to find the definition and call sites of calculateRoyalty, then follow the imports from there with Read.
- C. JA: 分配額の計算フローを推測した説明文をWriteで作成し、それを1ファイルずつ確かめていく。
  - KO: 배분액 계산 흐름을 추측한 설명문을 Write로 작성하고, 그것을 파일 하나씩 확인해 나갑니다.
  - EN: Use Write to create an explanation of the payout calculation flow based on guesses, and then verify it file by file.
- D. JA: Globで**/*.tsを列挙し、ファイル名に「royalty」を含むものから順にすべてReadで読む。
  - KO: Glob으로 **/*.ts를 나열하고, 파일 이름에 'royalty'가 들어간 것부터 순서대로 전부 Read로 읽습니다.
  - EN: Use Glob to list **/*.ts, then Read all of them in order, starting with those whose file names contain "royalty".

## CCAR-F-Udemy04-0013

**JA** ある証券会社の開発チームは、CIパイプラインのClaude Codeで、プルリクエストをファイルごとに分けてレビューしています。各ファイルを個別に分析する方式にしてから、ファイル内の指摘の質と一貫性は改善しました。

ところが、次の不具合がレビューを通過し、本番障害になりました。注文サービス側でorder_qtyフィールドの名前をquantityに変えたのに、それを受け取る決済サービス側は古い名前のままでした。

レビューの改善策として最も適切なものはどれですか。

**KO** 한 증권사의 개발팀은 CI pipeline의 Claude Code로 pull request를 파일별로 나눠 리뷰하고 있습니다. 각 파일을 개별적으로 분석하는 방식으로 바꾼 뒤, 파일 내 지적의 품질과 일관성은 개선되었습니다.

그런데 다음 결함이 리뷰를 통과해 운영 장애로 이어졌습니다. 주문 서비스 쪽에서 order_qty 필드 이름을 quantity로 바꿨는데, 그 값을 받는 결제 서비스 쪽은 옛 이름을 그대로 쓰고 있었습니다.

리뷰 개선책으로 가장 적절한 것은 무엇입니까?

- A. JA: ファイルごとのレビューをやめ、変更されたファイルを1回のパスでまとめてレビューする方式に戻す。
  - KO: 파일별 리뷰를 그만두고, 변경된 파일을 한 번의 pass로 모아서 리뷰하는 방식으로 되돌립니다.
  - EN: Stop the per-file reviews and return to reviewing all changed files together in a single pass.
- B. JA: ファイル単位のレビューで重大度のしきい値を下げ、報告される指摘の件数を増やす。
  - KO: 파일 단위 리뷰에서 심각도 임계값을 낮춰, 보고되는 지적 건수를 늘립니다.
  - EN: Lower the severity threshold in the file-level review to increase the number of reported findings.
- C. JA: ファイル単位のパスに加え、ファイル間のデータの受け渡しを調べる統合パスを追加する。
  - KO: 파일 단위 pass에 더해, 파일 간 데이터 전달을 살펴보는 통합 pass를 추가합니다.
  - EN: In addition to the file-level passes, add an integration pass that examines the data passed between files.
- D. JA: 各ファイルのレビューに、リポジトリ内の他のファイルの全文を参考として添える。
  - KO: 각 파일의 리뷰에 저장소 내 다른 파일의 전문을 참고 자료로 첨부합니다.
  - EN: Attach the full text of the other files in the repository as reference to each file's review.

## CCAR-F-Udemy04-0014

**JA** あるEC物流会社の開発チームは、カスタマーサポート解決エージェントの一部の処理を、Messages APIを直接呼び出す独自のループで実装しています。現在のループは、次のどちらかの条件で終了します。

応答のテキストに「以上で対応は完了です」という文言が含まれる

反復が10回に達する

ログを見ると、次のケースがありました。

テキストとtool_useを同時に含む応答でループが終わり、返金処理が実行されないまま会話が閉じる

調査の途中なのに、10回目で打ち切られる

ループの終了判定の改善として適切なものはどれですか。（2つ選択してください。）

**KO** 한 이커머스 물류 회사의 개발팀은 고객 지원 해결 agent 처리의 일부를, Messages API를 직접 호출하는 자체 loop로 구현했습니다. 현재 loop는 다음 조건 중 하나를 만족하면 종료됩니다.

응답 텍스트에 '이상으로 처리를 완료했습니다'라는 문구가 포함됨

반복이 10회에 도달함

로그를 보니 다음과 같은 사례가 있었습니다.

텍스트와 tool_use를 함께 포함한 응답에서 loop가 끝나, 환불 처리가 실행되지 않은 채 대화가 닫힘

조사가 진행 중인데도 10회째에서 중단됨

loop 종료 판정의 개선책으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 応答にテキストのブロックが含まれていたら、その時点で対応が完了したとみなす。
  - KO: 응답에 텍스트 블록이 포함되어 있으면, 그 시점에 처리가 완료된 것으로 간주합니다.
  - EN: Treat the work as complete as soon as the response contains a text block.
- B. JA: stop_reasonが"tool_use"の間は続け、"end_turn"になったら終了する。
  - KO: stop_reason이 "tool_use"인 동안은 계속하고, "end_turn"이 되면 종료합니다.
  - EN: Continue while stop_reason is "tool_use" and end when it becomes "end_turn".
- C. JA: 反復回数の上限は十分大きな値にし、ループが止まらない場合の安全策としてだけ残す。
  - KO: 반복 횟수 상한은 충분히 큰 값으로 두고, loop가 멈추지 않을 때의 안전장치로만 남깁니다.
  - EN: Set the iteration limit to a sufficiently large value and keep it only as a safeguard in case the loop does not stop.
- D. JA: 終了の文言の候補を増やし、「対応しました」などの表現にも一致するようにする。
  - KO: 종료 문구 후보를 늘려, '처리했습니다' 같은 표현에도 일치하게 합니다.
  - EN: Add more candidate termination phrases so that expressions such as 「対応しました」 also match.

## CCAR-F-Udemy04-0015

**JA** あるエネルギー会社の開発チームは、Claude Agent SDKでマルチエージェントリサーチシステムを構築しています。「各国の洋上風力発電の規制動向」を調べる際、コーディネーターは12の国・地域ごとに検索サブエージェントを並列に起動します。

先週の実行では、1つの地域のサブエージェントが、規制当局のサイトの応答待ちでタイムアウトしました。その例外がトップレベルまで伝わり、ワークフロー全体が終了しました。完了していた11地域分の結果も破棄され、翌日に全体を再実行するコストが発生しています。

最も適切な改善策はどれですか。

**KO** 한 에너지 기업의 개발팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. '각국 해상 풍력 발전의 규제 동향'을 조사할 때, coordinator는 12개 국가·지역별로 검색 subagent를 병렬로 실행합니다.

지난주 실행에서 한 지역의 subagent가 규제 당국 사이트의 응답을 기다리다 timeout되었습니다. 그 예외가 최상위까지 전파되어 workflow 전체가 종료되었습니다. 완료되어 있던 11개 지역의 결과도 폐기되어, 다음 날 전체를 다시 실행하는 비용이 발생했습니다.

가장 적절한 개선책은 무엇입니까?

- A. JA: タイムアウトの時間を30秒から10分に延ばし、応答の遅いサイトでも結果を待つようにする。
  - KO: timeout 시간을 30초에서 10분으로 늘려, 응답이 느린 사이트라도 결과를 기다리게 합니다.
  - EN: Extend the timeout from 30 seconds to 10 minutes so that the system waits for results even from slow-responding sites.
- B. JA: 失敗を構造化されたエラーとして返し、続行かリトライかをコーディネーターに判断させる。
  - KO: 실패를 구조화된 에러로 반환하고, 계속할지 재시도할지를 coordinator가 판단하게 합니다.
  - EN: Return the failure as a structured error and have the coordinator decide whether to continue or retry.
- C. JA: ワークフロー全体を最大3回まで自動で再実行するラッパーを、トップレベルに追加する。
  - KO: workflow 전체를 최대 3회까지 자동으로 다시 실행하는 wrapper를 최상위에 추가합니다.
  - EN: Add a wrapper at the top level that automatically reruns the entire workflow up to 3 times.
- D. JA: 失敗した地域は空の結果として扱い、残りの11地域の結果だけでレポートを完成させる。
  - KO: 실패한 지역은 빈 결과로 취급하고, 나머지 11개 지역의 결과만으로 보고서를 완성합니다.
  - EN: Treat the failed region as an empty result and complete the report using only the results from the remaining 11 regions.

## CCAR-F-Udemy04-0016

**JA** ある海運会社の開発チームは、Claude Agent SDKでカスタマーサポート解決エージェントを構築しています。荷主の依頼で貨物の配送先を変更するchange_delivery_addressツールは、本人確認を済ませてから呼び出す決まりで、システムプロンプトにもそのように明記しています。

しかし直近1か月のログでは、配送先の変更の2.3%が本人確認なしに実行されていました。チームでは、プロンプトの指示をさらに強調する案が出ています。

対応として適切なものはどれですか。（2つ選択してください。）

**KO** 한 해운 회사의 개발팀은 Claude Agent SDK로 고객 지원 해결 agent를 구축하고 있습니다. 화주의 요청에 따라 화물의 배송지를 변경하는 change_delivery_address 도구는 본인 확인을 마친 뒤에 호출하도록 정해져 있고, system prompt에도 그렇게 명시되어 있습니다.

그러나 최근 1개월 로그를 보면 배송지 변경의 2.3%가 본인 확인 없이 실행되었습니다. 팀에서는 prompt의 지시를 더 강조하자는 의견이 나오고 있습니다.

대응으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 本人確認なしで実行された変更をログで検出し、担当者が事後に取り消す運用にする。
  - KO: 본인 확인 없이 실행된 변경을 로그에서 찾아내, 담당자가 사후에 취소하는 방식으로 운영합니다.
  - EN: Detect changes executed without identity verification in the logs and have staff cancel them after the fact.
- B. JA: change_delivery_addressの説明に「本人確認が完了した会話でのみ使う」と条件を書き加える。
  - KO: change_delivery_address의 설명에 "본인 확인이 끝난 대화에서만 사용한다"라는 조건을 추가합니다.
  - EN: Add the condition "use only in conversations where identity verification has been completed" to the description of change_delivery_address.
- C. JA: 本人確認の成功をコードで確かめ、未確認ならchange_delivery_addressを拒否する。
  - KO: 본인 확인의 성공 여부를 코드로 확인하고, 확인되지 않았으면 change_delivery_address를 거부합니다.
  - EN: Verify in code that identity verification succeeded, and reject change_delivery_address if it has not been verified.
- D. JA: 拒否した理由（本人確認が先に必要）をツールの結果としてエージェントに返す。
  - KO: 거부한 이유(본인 확인이 먼저 필요함)를 도구 결과로 agent에게 돌려줍니다.
  - EN: Return the reason for the rejection (identity verification is required first) to the agent as the tool result.

## CCAR-F-Udemy04-0017

**JA** ある旅行会社の開発チームは、Claude Codeで運賃比較のスキルfare-diffを作りました。このスキルは、路線コードと出発日の2つを受け取り、新旧の運賃テーブルでの価格差を表示します。

しかし開発者が引数を付けずに/fare-diffを実行することが多く、そのたびに次のどちらかが起きています。

Claudeが路線を推測して計算する

SKILL.mdの手順にある「指定された路線」が何を指すか分からずに止まる

改善策として適切なものはどれですか。（2つ選択してください。）

**KO** 한 여행사의 개발팀은 Claude Code로 운임 비교 skill인 fare-diff를 만들었습니다. 이 skill은 노선 코드와 출발일 두 가지를 받아, 신구 운임 테이블의 가격 차이를 보여 줍니다.

그런데 개발자가 인수 없이 /fare-diff를 실행하는 경우가 많고, 그때마다 다음 중 하나가 일어나고 있습니다.

Claude가 노선을 추측해서 계산한다

SKILL.md 절차에 있는 "지정된 노선"이 무엇을 가리키는지 몰라 멈춘다

개선책으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: allowed-toolsに路線コードと出発日を列挙して、引数として扱わせる。
  - KO: allowed-tools에 노선 코드와 출발일을 나열해, 인수로 다루게 합니다.
  - EN: List the route code and departure date in allowed-tools so that they are treated as arguments.
- B. JA: SKILL.mdの本文で$0と$1を使い、渡された路線コードと出発日を手順に埋め込む。
  - KO: SKILL.md 본문에서 $0과 $1을 사용해, 전달된 노선 코드와 출발일을 절차에 넣습니다.
  - EN: Use $0 and $1 in the body of SKILL.md to embed the passed route code and departure date into the procedure.
- C. JA: argument-hint: [route-code] [date]を設定し、必要な引数を表示させる。
  - KO: argument-hint: [route-code] [date]를 설정해, 필요한 인수를 표시하게 합니다.
  - EN: Set argument-hint: [route-code] [date] so that the required arguments are displayed.
- D. JA: context: forkを設定し、引数がないときは別のコンテキストで路線を推測させる。
  - KO: context: fork를 설정해, 인수가 없을 때는 별도의 context에서 노선을 추측하게 합니다.
  - EN: Set context: fork so that, when no arguments are given, the route is guessed in a separate context.

## CCAR-F-Udemy04-0018

**JA** あるSaaS企業の開発チームは、Claude Agent SDKでマルチエージェントリサーチシステムを構築しています。次の2つのツールがあり、説明はどちらも「コンテンツを分析して要点を返す」です。

analyze_content（ウェブ検索サブエージェントが取得したページを解析する）

analyze_document（ユーザーがアップロードしたPDFを解析する）

ログを見ると、アップロードされたPDFの約40%がanalyze_contentに送られ、ページ番号などのメタデータが失われていました。

改善策として適切なものはどれですか。（2つ選択してください。）

**KO** 한 SaaS 기업의 개발팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. 다음 두 도구가 있으며, 설명은 둘 다 "콘텐츠를 분석해 요점을 반환한다"입니다.

analyze_content(웹 검색 subagent가 가져온 페이지를 분석한다)

analyze_document(사용자가 업로드한 PDF를 분석한다)

로그를 보니 업로드된 PDF의 약 40%가 analyze_content로 보내져, 페이지 번호 같은 metadata가 사라지고 있었습니다.

개선책으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 誤ったツールが呼ばれたときは、PostToolUseフックでその結果を破棄して再実行させる。
  - KO: 잘못된 도구가 호출되면 PostToolUse hook으로 그 결과를 버리고 다시 실행하게 합니다.
  - EN: When the wrong tool is called, use a PostToolUse hook to discard its result and have the call rerun.
- B. JA: analyze_documentの説明に、アップロードされたPDFを扱い、ページ番号などのメタデータを返すことを書く。
  - KO: analyze_document의 설명에, 업로드된 PDF를 다루며 페이지 번호 같은 metadata를 반환한다고 씁니다.
  - EN: State in the description of analyze_document that it handles uploaded PDFs and returns metadata such as page numbers.
- C. JA: PDFがアップロードされたときは、tool_choiceでanalyze_documentを毎回強制的に選択させる。
  - KO: PDF가 업로드되면 tool_choice로 매번 analyze_document를 강제로 선택하게 합니다.
  - EN: When a PDF is uploaded, use tool_choice to force the selection of analyze_document every time.
- D. JA: analyze_contentをextract_web_resultsに改名し、ウェブ専用の説明に書き換える。
  - KO: analyze_content의 이름을 extract_web_results로 바꾸고, 웹 전용 설명으로 다시 씁니다.
  - EN: Rename analyze_content to extract_web_results and rewrite its description to be web-specific.

## CCAR-F-Udemy04-0019

**JA** あるスポーツデータ分析会社の開発チームは、Claude Agent SDKでマルチエージェントリサーチシステムを構築しています。統合サブエージェントにも、ウェブ検索サブエージェントと同じweb_searchツールを与えています。

最近のレポートでは、統合サブエージェントが自分で追加の検索をした結果、文書分析サブエージェントの検証を経ていない個人ブログの数値が、出典として混ざるようになりました。追加の検索が必要になる場面は、統合の作業全体の1割程度です。

最も適切な改善策はどれですか。

**KO** 한 스포츠 데이터 분석 회사의 개발팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. 통합 subagent에게도 웹 검색 subagent와 같은 web_search 도구를 주었습니다.

최근 리포트에서는 통합 subagent가 직접 추가 검색을 한 결과, 문서 분석 subagent의 검증을 거치지 않은 개인 블로그의 수치가 출처로 섞여 들어가기 시작했습니다. 추가 검색이 필요한 경우는 통합 작업 전체의 10% 정도입니다.

가장 적절한 개선책은 무엇입니까?

- A. JA: 統合サブエージェントに文書分析のツールも与え、検索した資料を自分で検証させる。
  - KO: 통합 subagent에게 문서 분석 도구도 주어, 검색한 자료를 직접 검증하게 합니다.
  - EN: Also give the synthesis subagent the document analysis tools and have it verify the materials it searches for by itself.
- B. JA: 統合サブエージェントからweb_searchを外し、追加の調査はコーディネーターに戻す。
  - KO: 통합 subagent에서 web_search를 빼고, 추가 조사는 coordinator에게 돌려보냅니다.
  - EN: Remove web_search from the synthesis subagent and send additional research back to the coordinator.
- C. JA: 統合サブエージェントのシステムプロンプトに「web_searchは使わないこと」と書く。
  - KO: 통합 subagent의 system prompt에 "web_search는 사용하지 말 것"이라고 씁니다.
  - EN: Write "Do not use web_search" in the synthesis subagent's system prompt.
- D. JA: 統合サブエージェントが検索で得た情報にも、出典の信頼性を付けて区別させる。
  - KO: 통합 subagent가 검색으로 얻은 정보에도 출처의 신뢰도를 붙여 구분하게 합니다.
  - EN: Have the synthesis subagent attach source reliability to the information it obtains through search as well, so that it can be distinguished.

## CCAR-F-Udemy04-0020

**JA** ある鉄道会社の開発チームは、Claude Codeで運行管理システムの開発を進めています。ダイヤを定義する*.schedule.yamlファイルの規約は.claude/rules/schedule.mdにまとめています。paths: ["lines/**/*.schedule.yaml"]をそのフロントマターに指定しています。

既存のダイヤ定義ファイルの修正を依頼すると、規約どおりの内容になります。ところが、旧システムのデータからダイヤ定義ファイルを出力する変換スクリプトtools/convert_timetable.pyの改修を依頼したところ、出力されるファイルの書式が規約に反していました。

読み込まれた指示ファイルを記録するInstructionsLoadedフックのログを見ると、このセッションでschedule.mdは一度も読み込まれていません。

最も可能性の高い根本原因はどれですか。

**KO** 한 철도 회사의 개발팀은 Claude Code로 운행 관리 시스템을 개발하고 있습니다. 운행표를 정의하는 *.schedule.yaml 파일의 규약은 .claude/rules/schedule.md에 정리해 두었습니다. 이 파일의 frontmatter에는 paths: ["lines/**/*.schedule.yaml"]를 지정했습니다.

기존 운행표 정의 파일의 수정을 요청하면 규약대로 작성됩니다. 그런데 구 시스템의 데이터로 운행표 정의 파일을 출력하는 변환 스크립트 tools/convert_timetable.py의 수정을 요청했더니, 출력된 파일의 서식이 규약에 어긋났습니다.

로드된 지시 파일을 기록하는 InstructionsLoaded hook의 로그를 보면, 이 session에서 schedule.md는 한 번도 로드되지 않았습니다.

가장 가능성이 높은 근본 원인은 무엇입니까?

- A. JA: セッションの途中で/compactが実行され、読み込まれていた規約が失われている。
  - KO: session 도중에 /compact가 실행되어, 로드되어 있던 규약이 사라졌습니다.
  - EN: /compact was run partway through the session, and the conventions that had been loaded were lost.
- B. JA: 作業の対象が変換スクリプトだけで、pathsに一致するファイルをClaudeが読み書きしていない。
  - KO: 작업 대상이 변환 스크립트뿐이어서, paths에 일치하는 파일을 Claude가 읽거나 쓰지 않았습니다.
  - EN: The work targeted only the conversion script, and Claude did not read or write any file matching paths.
- C. JA: ルートのCLAUDE.mdに書かれたPythonの規約が、schedule.mdの規約より優先されている。
  - KO: 루트의 CLAUDE.md에 적힌 Python 규약이 schedule.md의 규약보다 우선 적용되고 있습니다.
  - EN: The Python conventions written in the root CLAUDE.md take precedence over the conventions in schedule.md.
- D. JA: pathsのglobパターンが、lines/配下の深い階層にあるファイルに一致していない。
  - KO: paths의 glob 패턴이 lines/ 아래 깊은 계층에 있는 파일과 일치하지 않습니다.
  - EN: The glob pattern in paths does not match files at deep levels under lines/.

## CCAR-F-Udemy04-0021

**JA** ある製造業の開発チームは、Claude Agent SDKで開発者の生産性向上ツールを構築しています。エージェントは組み込みツールに加えて、工場の設備データを扱う社内MCPサーバーのquery_plant_telemetryツールを利用できます。現在の設定は次のとおりです。

query_plant_telemetryは設備IDごとの稼働率と異常フラグを集計して返すが、説明は「テレメトリを照会する」の1文だけ

システムプロンプトには「不具合の調査では、まずログを検索すること」と書かれている

ログを見ると、エージェントは設備の異常に関する質問でもGrepで数GBの生ログを検索し、MCPツールをほとんど使っていません。

改善策として適切なものはどれですか。（2つ選択してください。）

**KO** 한 제조업체의 개발팀은 Claude Agent SDK로 개발자 생산성 향상 도구를 구축하고 있습니다. agent는 내장 도구 외에도, 공장 설비 데이터를 다루는 사내 MCP server의 query_plant_telemetry 도구를 사용할 수 있습니다. 현재 설정은 다음과 같습니다.

query_plant_telemetry는 설비 ID별 가동률과 이상 플래그를 집계해 반환하지만, 설명은 "텔레메트리를 조회한다" 한 문장뿐이다

system prompt에는 "장애를 조사할 때는 먼저 로그를 검색할 것"이라고 적혀 있다

로그를 보면 agent는 설비 이상에 관한 질문에서도 Grep으로 수 GB의 원시 로그를 검색하고, MCP 도구는 거의 사용하지 않습니다.

개선책으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: Grepを無効化し、エージェントが設備データをMCPツールからしか取得できないようにする。
  - KO: Grep을 비활성화해, agent가 설비 데이터를 MCP 도구로만 가져올 수 있게 합니다.
  - EN: Disable Grep so that the agent can obtain equipment data only from the MCP tool.
- B. JA: MCPツールの説明に、返す集計値と異常フラグの内容、生ログ検索より向いている場面を書く。
  - KO: MCP 도구의 설명에, 반환하는 집계값과 이상 플래그의 내용, 그리고 원시 로그 검색보다 적합한 상황을 씁니다.
  - EN: State in the MCP tool's description the contents of the aggregated values and anomaly flags it returns, and the situations in which it is better suited than searching raw logs.
- C. JA: MCPサーバーの登録先をプロジェクトの.mcp.jsonからユーザースコープの~/.claude.jsonに移す。
  - KO: MCP server의 등록 위치를 프로젝트의 .mcp.json에서 user scope의 ~/.claude.json으로 옮깁니다.
  - EN: Move the registration of the MCP server from the project's .mcp.json to user scope in ~/.claude.json.
- D. JA: システムプロンプトの「まずログを検索すること」という一文を、対象を限定した表現に改める。
  - KO: system prompt의 "먼저 로그를 검색할 것"이라는 문장을 대상을 한정한 표현으로 고칩니다.
  - EN: Reword the sentence "search the logs first" in the system prompt into an expression that limits its scope.

## CCAR-F-Udemy04-0022

**JA** あるゲーム会社の開発チームは、継続的インテグレーションのパイプラインにClaude Codeを組み込み、夜間ジョブでテストケースを生成しています。

今回、「ゲームサーバーのレガシーコードに包括的なテストを追加する」という作業を任せたところ、Claudeはディレクトリ名のアルファベット順にファイルを処理し始めました。その結果、一晩の実行予算の大半が、共通ユーティリティの単純な関数のテストに使われました。障害の多い課金モジュールとマッチングモジュールには、1件もテストが追加されませんでした。

このオープンエンドなタスクの分解方法として適切なものはどれですか。（2つ選択してください。）

**KO** 한 게임 회사의 개발팀은 지속적 통합(CI) pipeline에 Claude Code를 넣어, 야간 작업으로 테스트 케이스를 생성하고 있습니다.

이번에 "게임 서버의 레거시 코드에 포괄적인 테스트를 추가한다"라는 작업을 맡겼더니, Claude는 디렉터리 이름의 알파벳 순서대로 파일을 처리하기 시작했습니다. 그 결과 하룻밤 실행 예산의 대부분이 공통 유틸리티의 단순한 함수 테스트에 쓰였습니다. 장애가 잦은 과금 모듈과 매칭 모듈에는 테스트가 단 1건도 추가되지 않았습니다.

이 open-ended 작업을 분해하는 방법으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 最初にモジュール構成と依存関係を把握させ、障害履歴や変更頻度から影響の大きい領域を特定させる。
  - KO: 먼저 모듈 구성과 의존 관계를 파악하게 한 뒤, 장애 이력과 변경 빈도를 바탕으로 영향이 큰 영역을 찾게 합니다.
  - EN: First have Claude understand the module structure and dependencies, then identify high-impact areas from failure history and change frequency.
- B. JA: 影響の大きい領域から順に並べた計画を作らせ、新たな依存関係が見つかるたびに計画を更新させる。
  - KO: 영향이 큰 영역부터 순서대로 나열한 계획을 세우게 하고, 새로운 의존 관계가 발견될 때마다 계획을 갱신하게 합니다.
  - EN: Have Claude create a plan ordered starting from the highest-impact areas, and update the plan each time a new dependency is discovered.
- C. JA: 1回の実行で処理できるファイル数とターン数の上限を引き上げ、すべてのファイルにテストを生成させる。
  - KO: 1회 실행에서 처리할 수 있는 파일 수와 turn 수의 상한을 올려, 모든 파일에 대해 테스트를 생성하게 합니다.
  - EN: Raise the limits on the number of files and turns that can be processed in a single run, and have Claude generate tests for all files.
- D. JA: 全モジュールを同じ粒度のサブタスクに事前に分割し、決めた順番で1つずつ処理するプロンプトチェーンにする。
  - KO: 모든 모듈을 같은 크기의 subtask로 미리 나누고, 정해 둔 순서대로 하나씩 처리하는 prompt chain으로 만듭니다.
  - EN: Split all modules in advance into subtasks of the same granularity and make a prompt chain that processes them one at a time in the predetermined order.

## CCAR-F-Udemy04-0023

**JA** ある銀行の開発チームは、Claude Agent SDKでマルチエージェントリサーチシステムを構築しています。融資担当者は、コーディネーターと何十ターンもやり取りしながら、取引先企業の財務状況と業界動向を調べます。会話が長くなると、コーディネーターは古いターンを段階的に要約しています。

ところが、序盤で確認した「既存融資の金利3.25%、返済期限2027年3月、担保評価額4.2億円」が、後半では「低金利の長期融資があり、担保も十分」という要約に置き換わり、最終的な比較表の数値が誤っていました。比較表は、コーディネーター自身が会話の内容をもとに作成しています。

数値が誤った最も可能性の高い根本原因はどれですか。

**KO** 한 은행의 개발팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. 대출 담당자는 coordinator와 수십 turn에 걸쳐 대화하면서 거래처 기업의 재무 상황과 업계 동향을 조사합니다. 대화가 길어지면 coordinator는 오래된 turn을 단계적으로 요약합니다.

그런데 초반에 확인한 "기존 대출 금리 3.25%, 상환 기한 2027년 3월, 담보 평가액 4.2억 엔"이 후반에는 "저금리 장기 대출이 있고 담보도 충분"이라는 요약으로 바뀌어, 최종 비교표의 수치가 틀렸습니다. 비교표는 coordinator가 대화 내용을 바탕으로 직접 작성합니다.

수치가 틀린 가장 가능성 높은 근본 원인은 무엇입니까?

- A. JA: 「lost in the middle」効果で、長い入力の中間にある数値が見落とされている。
  - KO: "lost in the middle" 효과로 인해, 긴 입력의 중간에 있는 수치를 놓치고 있습니다.
  - EN: Because of the "lost in the middle" effect, figures in the middle of a long input are being overlooked.
- B. JA: 融資担当者の発言とツールの結果が混在し、どの数値が確定値かを区別できていない。
  - KO: 대출 담당자의 발언과 도구 결과가 뒤섞여, 어느 수치가 확정값인지 구분하지 못하고 있습니다.
  - EN: The loan officer's statements and tool results are mixed together, so the coordinator cannot tell which figures are confirmed.
- C. JA: 金利や期限などの事実が、要約される会話履歴の中にしか存在しない。
  - KO: 금리나 기한 같은 사실이 요약 대상인 대화 기록 안에만 존재합니다.
  - EN: Facts such as the interest rate and deadline exist only in the conversation history that gets summarized.
- D. JA: 会話がコンテキストウィンドウの上限を超え、序盤のターンが切り捨てられている。
  - KO: 대화가 context window 상한을 넘어, 초반 turn이 잘려 나갔습니다.
  - EN: The conversation exceeded the context window limit, and the early turns were truncated.

## CCAR-F-Udemy04-0024

**JA** ある製薬会社の開発チームは、Claude Agent SDKでマルチエージェントリサーチシステムを構築しています。文書分析サブエージェントは、臨床試験の論文から得た知見を、「〜という結果が報告されている（Smith et al., 2024, p.12）」のように出典を文中に埋め込んだ文章で返しています。

統合サブエージェントがこれらを言い換えてまとめる過程で、知見と出典の組み合わせがずれ、最終レポートの約15%の引用で、別の論文の結論が紐づいていました。

最も適切な改善策はどれですか。

**KO** 한 제약 회사의 개발팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. 문서 분석 subagent는 임상시험 논문에서 얻은 지견을 "~라는 결과가 보고되었다(Smith et al., 2024, p.12)"처럼 출처를 문장 안에 넣은 글로 반환합니다.

통합 subagent가 이를 바꿔 말하며 정리하는 과정에서 지견과 출처의 짝이 어긋나, 최종 리포트 인용의 약 15%에 다른 논문의 결론이 연결되어 있었습니다.

가장 적절한 개선책은 무엇입니까?

- A. JA: 統合サブエージェントのプロンプトに「出典は正確に保つこと」と明記し、言い換えを控えさせる。
  - KO: 통합 subagent의 prompt에 "출처를 정확하게 유지할 것"이라고 명시하고, 바꿔 말하기를 자제하게 합니다.
  - EN: State "keep sources accurate" in the synthesis subagent's prompt and have it refrain from paraphrasing.
- B. JA: 文書分析サブエージェントの出力を要約せず、論文の全文をそのまま統合サブエージェントに渡す。
  - KO: 문서 분석 subagent의 출력을 요약하지 않고, 논문 전문을 그대로 통합 subagent에게 넘깁니다.
  - EN: Pass the full text of the papers directly to the synthesis subagent without summarizing the document analysis subagent's output.
- C. JA: 知見の本文と、URLやページ番号などのメタデータを分けた形式で返させる。
  - KO: 지견 본문과, URL·페이지 번호 같은 metadata를 분리한 형식으로 반환하게 합니다.
  - EN: Have it return the body of each finding separately from metadata such as the URL and page number.
- D. JA: レポートの完成後に別のエージェントで各主張の出典を検索し直し、引用を付け直す。
  - KO: 리포트가 완성된 뒤 별도의 agent로 각 주장의 출처를 다시 검색해, 인용을 새로 붙입니다.
  - EN: After the report is completed, use a separate agent to search for the source of each claim again and reattach the citations.

## CCAR-F-Udemy04-0025

**JA** ある通信事業者の開発チームは、Claude Agent SDKで開発者の生産性向上ツールを構築しています。このエージェントは、不慣れなコードベースの調査をフェーズ1（課金バッチの依存関係の洗い出し）、フェーズ2（改修箇所の特定）のように分け、フェーズごとに新しいサブエージェントを起動します。

ログを確認したところ、フェーズ2のサブエージェントは、フェーズ1が調べ終えた38個のファイルをReadで読み直しており、トークン使用量の約半分がその重複に使われていました。フェーズ2への委任プロンプトには、「改修箇所を特定してください」という依頼文だけが書かれています。

最も可能性の高い根本原因はどれですか。

**KO** 한 통신사의 개발팀은 Claude Agent SDK로 개발자 생산성 향상 도구를 구축하고 있습니다. 이 agent는 익숙하지 않은 코드베이스 조사를 1단계(과금 batch의 의존 관계 파악), 2단계(수정할 위치 특정)처럼 나누고, 단계마다 새로운 subagent를 실행합니다.

로그를 확인해 보니, 2단계 subagent가 1단계에서 이미 조사를 마친 38개 파일을 Read로 다시 읽고 있었고, 토큰 사용량의 약 절반이 이 중복에 쓰였습니다. 2단계에 위임하는 prompt에는 "수정할 위치를 특정해 주세요"라는 요청문만 적혀 있습니다.

가장 가능성이 높은 근본 원인은 무엇입니까?

- A. JA: フェーズ2のサブエージェントにGrepが許可されておらず、Readで1ファイルずつ開くしか調べる手段がない。
  - KO: 2단계 subagent에 Grep이 허용되지 않아, Read로 파일을 하나씩 여는 것 말고는 조사할 방법이 없습니다.
  - EN: Grep is not permitted for the phase 2 subagent, so its only means of investigating is to open files one at a time with Read.
- B. JA: フェーズ2のサブエージェントのmax_turnsが小さく、上限に達するたびに調査を最初からやり直している。
  - KO: 2단계 subagent의 max_turns가 작아, 상한에 도달할 때마다 조사를 처음부터 다시 하고 있습니다.
  - EN: The phase 2 subagent's max_turns is small, and each time it reaches the limit it restarts the investigation from the beginning.
- C. JA: コーディネーターのコンテキストウィンドウが上限に近づき、フェーズ1の調査結果が自動的に圧縮されている。
  - KO: coordinator의 context window가 상한에 가까워져, 1단계의 조사 결과가 자동으로 압축되고 있습니다.
  - EN: The coordinator's context window is nearing its limit, and the phase 1 investigation results are being automatically compressed.
- D. JA: フェーズ1の主要な調査結果が要約されず、フェーズ2のサブエージェントの初期コンテキストに含まれていない。
  - KO: 1단계의 주요 조사 결과가 요약되지 않아, 2단계 subagent의 초기 context에 포함되어 있지 않습니다.
  - EN: The key findings from phase 1 were not summarized and are not included in the phase 2 subagent's initial context.

## CCAR-F-Udemy04-0026

**JA** ある化学メーカーの開発チームは、Claude Codeでプロジェクト用のスキルを2つ作りました。

1つは、安全データシート（SDS）のYAMLファイルの記載形式を確認するsds-checkです。SDSのファイルを編集するたびに使ってほしいのですが、descriptionが「SDS用」だけのため、Claudeが自動で使うことはほとんどありません。

もう1つは、製造ロットの出荷判定を記録して社内システムに登録するrelease-lotです。担当者が明示的に実行したときだけ動かしたいのに、関連する会話の中でClaudeが自動で呼び出したことがありました。

適切な設定はどれですか。（2つ選択してください。）

**KO** 한 화학 제조업체의 개발팀은 Claude Code로 프로젝트용 skill을 2개 만들었습니다.

하나는 안전 데이터 시트(SDS) YAML 파일의 기재 형식을 확인하는 sds-check입니다. SDS 파일을 편집할 때마다 사용되기를 바라지만, description이 "SDS용"뿐이어서 Claude가 자동으로 사용하는 일은 거의 없습니다.

다른 하나는 제조 로트의 출하 판정을 기록해 사내 시스템에 등록하는 release-lot입니다. 담당자가 명시적으로 실행할 때만 동작하게 하고 싶은데, 관련된 대화 중에 Claude가 자동으로 호출한 적이 있었습니다.

적절한 설정은 무엇입니까? (2개를 선택하십시오.)

- A. JA: release-lotのフロントマターにdisable-model-invocation: trueを設定する。
  - KO: release-lot의 frontmatter에 disable-model-invocation: true를 설정합니다.
  - EN: Set disable-model-invocation: true in the frontmatter of release-lot.
- B. JA: 2つのスキルの内容をCLAUDE.mdに移し、どの会話でも常に読み込まれる状態にする。
  - KO: 두 skill의 내용을 CLAUDE.md로 옮겨, 어느 대화에서든 항상 로드되게 합니다.
  - EN: Move the contents of both skills to CLAUDE.md so that they are always loaded in every conversation.
- C. JA: release-lotにargument-hintを設定し、ロット番号の入力を促して自動実行を防ぐ。
  - KO: release-lot에 argument-hint를 설정해 로트 번호 입력을 유도함으로써 자동 실행을 막습니다.
  - EN: Set argument-hint on release-lot to prompt for a lot number input and thereby prevent automatic execution.
- D. JA: sds-checkのdescriptionに、確認する内容と使うべき場面を書く。
  - KO: sds-check의 description에 확인하는 내용과 사용해야 할 상황을 씁니다.
  - EN: Write in the description of sds-check what it verifies and when it should be used.

## CCAR-F-Udemy04-0027

**JA** ある消費者金融会社の開発チームは、Claude Agent SDKでカスタマーサポート解決エージェントを構築しています。process_refundツールは、1回あたりの返金上限（10万円）を超える依頼に対して、isError: trueと「Operation failed」という文字列だけを返します。

ログでは、上限を超える返金依頼のたびに、エージェントが同じ呼び出しを4〜5回繰り返したうえで、顧客に「現在システム障害が発生しています」と誤った案内をしていました。

process_refundのエラーレスポンスの改善として適切なものはどれですか。（2つ選択してください。）

**KO** 한 소비자 금융 회사의 개발팀은 Claude Agent SDK로 고객 지원 해결 agent를 구축하고 있습니다. process_refund 도구는 1회 환불 상한(10만 엔)을 넘는 요청에 대해 isError: true와 "Operation failed"라는 문자열만 반환합니다.

로그를 보면 상한을 넘는 환불 요청이 올 때마다 agent가 같은 호출을 4~5회 반복한 뒤, 고객에게 "현재 시스템 장애가 발생했습니다"라고 잘못 안내하고 있었습니다.

process_refund의 오류 응답 개선으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: エラーを一時的なエラーに分類し、エージェントが指数バックオフで間隔を空けてリトライするようにする。
  - KO: 오류를 일시적 오류로 분류해, agent가 exponential backoff(exponential backoff)로 간격을 두고 재시도하게 합니다.
  - EN: Classify the error as a transient error so that the agent retries with exponential backoff at spaced intervals.
- B. JA: 「1回の返金上限は10万円で、超える分は担当部署の審査が必要」という顧客向けの説明を含める。
  - KO: "1회 환불 상한은 10만 엔이며, 초과분은 담당 부서의 심사가 필요하다"라는 고객용 설명을 포함합니다.
  - EN: Include a customer-facing explanation: "The per-transaction refund limit is 100,000 yen, and amounts above it require review by the responsible department."
- C. JA: ビジネスルール違反であることを示す分類とともに、isRetryable: falseを返す。
  - KO: 비즈니스 규칙 위반임을 나타내는 분류와 함께 isRetryable: false를 반환합니다.
  - EN: Return isRetryable: false along with a category indicating a business rule violation.
- D. JA: エラーにする代わりに空の成功結果を返し、エージェントが次の手順へ進めるようにする。
  - KO: 오류 대신 빈 성공 결과를 반환해, agent가 다음 단계로 진행할 수 있게 합니다.
  - EN: Instead of returning an error, return an empty success result so that the agent can proceed to the next step.

## CCAR-F-Udemy04-0028

**JA** ある教育サービス企業の開発チームは、Claude APIで開発者の生産性向上ツールを構築しています。現在の実装では、質問を受けると、アプリ側のコードが次の順序を固定で実行し、各ステップの後にClaudeを呼び出しています。

Globでファイルを探す

Grepで検索する

上位5ファイルをReadで読む

回答する

テストの実行結果を確かめないと答えられない質問や、5ファイル以上を読む必要がある質問では、的外れな回答が返っています。

この実装の見直しとして適切なものはどれですか。（2つ選択してください。）

**KO** 한 교육 서비스 기업의 개발팀은 Claude API로 개발자 생산성 향상 도구를 구축하고 있습니다. 현재 구현에서는 질문을 받으면 앱 쪽 코드가 다음 순서를 고정적으로 실행하고, 각 단계 뒤에 Claude를 호출합니다.

Glob으로 파일을 찾는다

Grep으로 검색한다

상위 5개 파일을 Read로 읽는다

답변한다

테스트 실행 결과를 확인하지 않으면 답할 수 없는 질문이나, 5개 이상의 파일을 읽어야 하는 질문에는 엉뚱한 답변이 돌아오고 있습니다.

이 구현을 재검토하는 방법으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: ツールを定義してループに渡し、次にどのツールを呼ぶかは結果を見たClaudeに判断させる。
  - KO: 도구를 정의해 loop에 넘기고, 다음에 어느 도구를 호출할지는 결과를 본 Claude가 판단하게 합니다.
  - EN: Define the tools and pass them to a loop, and let Claude, after seeing the results, decide which tool to call next.
- B. JA: 反復回数の上限を5回に固定し、5回目のツール実行が終わったら回答させる。
  - KO: 반복 횟수 상한을 5회로 고정하고, 5번째 도구 실행이 끝나면 답변하게 합니다.
  - EN: Fix the iteration limit at 5 and have Claude answer once the fifth tool execution finishes.
- C. JA: 各ツールのdescriptionに、用途とほかのツールとの使い分けを書く。
  - KO: 각 도구의 description에 용도와 다른 도구와의 구분 기준을 씁니다.
  - EN: Write in each tool's description its purpose and when to use it rather than the other tools.
- D. JA: 質問の種類ごとに分岐を増やし、テストの実行が必要な質問用の固定手順を追加する。
  - KO: 질문 유형별로 분기를 늘리고, 테스트 실행이 필요한 질문용 고정 절차를 추가합니다.
  - EN: Add more branches for each question type, and add a fixed procedure for questions that require running tests.

## CCAR-F-Udemy04-0029

**JA** ある自治体の情報政策課の開発チームは、Claude Agent SDKでマルチエージェントリサーチシステムを構築しています。他自治体の施策を調べる際、文書分析サブエージェントは汎用のanalyze_documentツールだけを使い、次の3つの用途をこの1つのツールで処理しています。

データを抜き出す

要約する

主張を出典と照合する

その結果、同じ依頼でも出力の形式が毎回異なり、コーディネーターが結果を解析できない事態が週に数十件起きています。

改善策として適切なものはどれですか。（2つ選択してください。）

**KO** 한 지방자치단체 정보정책과의 개발팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. 다른 지자체의 시책을 조사할 때 문서 분석 subagent는 범용 analyze_document 도구만 사용해, 다음 세 가지 용도를 이 도구 하나로 처리합니다.

데이터를 추출한다

요약한다

주장을 출처와 대조한다

그 결과 같은 요청이라도 출력 형식이 매번 달라, coordinator가 결과를 파싱하지 못하는 일이 일주일에 수십 건 일어나고 있습니다.

개선책으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: analyze_documentの説明に3つの用途それぞれの手順を書き込み、1つのツールで対応させる。
  - KO: analyze_document의 설명에 세 가지 용도별 절차를 각각 적어, 도구 하나로 대응하게 합니다.
  - EN: Write the procedures for each of the three uses into the description of analyze_document and have the one tool handle all of them.
- B. JA: 用途ごとに、extract_data_pointsなどの目的別のツールに分割する。
  - KO: 용도별로 extract_data_points 같은 목적별 도구로 나눕니다.
  - EN: Split it into purpose-specific tools for each use, such as extract_data_points.
- C. JA: ツールごとに受け取る引数と返すフィールドを定め、入出力の仕様を説明に書く。
  - KO: 도구마다 받는 인수와 반환하는 필드를 정하고, 입출력 사양을 설명에 씁니다.
  - EN: Define the arguments each tool accepts and the fields it returns, and write the input and output specification in its description.
- D. JA: 分析結果を自由形式の文章で返させ、コーディネーター側で用途に合わせて解釈させる。
  - KO: 분석 결과를 자유 형식의 문장으로 반환하게 하고, coordinator 쪽에서 용도에 맞게 해석하게 합니다.
  - EN: Have it return analysis results as free-form text and let the coordinator interpret them according to the use.

## CCAR-F-Udemy04-0030

**JA** ある製薬会社の開発チームは、Claude Agent SDKでマルチエージェントリサーチシステムを構築しています。文献データベースを検索するサブエージェントは、レート制限（HTTP 429）やタイムアウトが起きるたびに、そのエラーをそのままコーディネーターに返しています。

コーディネーターはそのたびに同じ検索を委任し直しており、ログではコーディネーターのトークンの約30%がこうしたエラーの処理に使われていました。エラーの多くは、数秒待てば成功するものです。

最も適切な改善策はどれですか。

**KO** 한 제약 회사의 개발팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. 문헌 데이터베이스를 검색하는 subagent는 rate limit(HTTP 429)이나 timeout이 발생할 때마다 그 오류를 그대로 coordinator에게 반환합니다.

coordinator는 그때마다 같은 검색을 다시 위임하고 있으며, 로그를 보면 coordinator 토큰의 약 30%가 이런 오류 처리에 쓰였습니다. 오류 대부분은 몇 초만 기다리면 성공하는 것입니다.

가장 적절한 개선책은 무엇입니까?

- A. JA: エラーが一定回数を超えたら、ワークフロー全体を停止して担当者に通知する。
  - KO: 오류가 일정 횟수를 넘으면 workflow 전체를 멈추고 담당자에게 알립니다.
  - EN: Stop the entire workflow and notify a person in charge once the number of errors exceeds a certain threshold.
- B. JA: サブエージェントでエラーを捕捉し、取得できた分だけを成功の結果として返す。
  - KO: subagent에서 오류를 잡아, 가져온 부분만 성공 결과로 반환합니다.
  - EN: Catch the errors in the subagent and return only the data that was retrieved as a successful result.
- C. JA: コーディネーターに、エラーの再委任だけを担当するリトライ専用のサブエージェントを追加する。
  - KO: coordinator에 오류 재위임만 맡는 재시도 전용 subagent를 추가합니다.
  - EN: Add a retry-only subagent to the coordinator whose sole job is to re-delegate failed requests.
- D. JA: 一時的な失敗はサブエージェント内でリトライし、解決しないものだけを伝播させる。
  - KO: 일시적인 실패는 subagent 안에서 재시도하고, 해결되지 않은 것만 전파합니다.
  - EN: Retry transient failures inside the subagent, and propagate only the failures that remain unresolved.

## CCAR-F-Udemy04-0031

**JA** ある航空会社の開発チームでは、エンジニアがClaude Codeで複数の調査を並行して進めています。あるエンジニアは、次の3つの調査を、それぞれ別のセッションで数日にわたって続けています。

運航管理システムの遅延通知の不具合

整備記録のエクスポートの性能問題

乗務員スケジュールの移行準備

毎朝claude --continueで作業を再開していますが、直前に触っていた別の調査のセッションが開いてしまい、説明をやり直す手間がかかっています。

最も適切な対処はどれですか。

**KO** 한 항공사의 개발팀에서는 엔지니어들이 Claude Code로 여러 조사를 병행하고 있습니다. 한 엔지니어는 다음 세 가지 조사를 각각 별도의 session에서 며칠째 이어 가고 있습니다.

운항 관리 시스템의 지연 알림 버그

정비 기록 내보내기의 성능 문제

승무원 스케줄의 마이그레이션 준비

매일 아침 claude --continue로 작업을 재개하는데, 직전에 다루던 다른 조사의 session이 열려 설명을 다시 해야 하는 번거로움이 생기고 있습니다.

가장 적절한 대처는 무엇입니까?

- A. JA: --continueに--fork-sessionを付けて、元のセッションを残したまま再開する。
  - KO: --continue에 --fork-session을 붙여, 원래 session을 남겨 둔 채 재개합니다.
  - EN: Add --fork-session to --continue so that the original session is preserved while resuming.
- B. JA: 調査ごとの進捗をCLAUDE.mdに書き残し、毎朝新しいセッションを開始する。
  - KO: 조사별 진행 상황을 CLAUDE.md에 적어 두고, 매일 아침 새 session을 시작합니다.
  - EN: Write each investigation's progress in CLAUDE.md and start a new session every morning.
- C. JA: 毎回--continueで再開し、違う調査のセッションだったら/clearしてから説明し直す。
  - KO: 매번 --continue로 재개하고, 다른 조사의 session이면 /clear한 뒤 다시 설명합니다.
  - EN: Resume with --continue every time, and if it is the session for a different investigation, run /clear and explain the context again.
- D. JA: 各セッションに/renameで名前を付け、claude --resumeに名前を指定して再開する。
  - KO: 각 session에 /rename으로 이름을 붙이고, claude --resume에 이름을 지정해 재개합니다.
  - EN: Give each session a name with /rename, and resume by specifying the name with claude --resume.

## CCAR-F-Udemy04-0032

**JA** ある物流会社の開発チームは、Claude Agent SDKでマルチエージェントリサーチシステムを構築しています。「国内の倉庫自動化の動向」についてのレポートでは、次の3種類の内容を扱います。

上場各社の設備投資額と営業利益率の比較

業界ニュースの経緯

ロボットの技術仕様の調査結果

現在のレポート生成サブエージェントは、すべての内容を同じ箇条書きの形式に変換しており、読者から「数値を比較しにくい」「ニュースの流れが分からない」という声が出ています。

最も適切な改善策はどれですか。

**KO** 한 물류 회사의 개발팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. "국내 창고 자동화 동향"에 관한 리포트에서는 다음 세 종류의 내용을 다룹니다.

상장사별 설비 투자액과 영업이익률 비교

업계 뉴스의 경과

로봇 기술 사양 조사 결과

현재 리포트 생성 subagent는 모든 내용을 같은 글머리 기호 목록 형식으로 변환하고 있어, 독자들로부터 "수치를 비교하기 어렵다", "뉴스의 흐름을 알 수 없다"는 의견이 나오고 있습니다.

가장 적절한 개선책은 무엇입니까?

- A. JA: レポート全体の形式を箇条書きから表に改め、全項目を列にそろえる。
  - KO: 리포트 전체 형식을 글머리 기호 목록에서 표로 바꾸고, 모든 항목을 열로 맞춥니다.
  - EN: Change the format of the entire report from bulleted lists to tables, aligning all items into columns.
- B. JA: 財務データは文章で解説し、ニュースと技術仕様は表にまとめる。
  - KO: 재무 데이터는 문장으로 설명하고, 뉴스와 기술 사양은 표로 정리합니다.
  - EN: Explain the financial data in prose, and summarize the news and technical specifications in tables.
- C. JA: 汎用テンプレートを1つ用意し、全セクションを同じ見出し構成で出力させる。
  - KO: 범용 템플릿을 하나 준비해, 모든 섹션을 같은 제목 구성으로 출력하게 합니다.
  - EN: Prepare one generic template and have every section output the same heading structure.
- D. JA: 財務データは表、ニュースは文章、技術仕様は構造化リストで表現させる。
  - KO: 재무 데이터는 표, 뉴스는 문장, 기술 사양은 구조화된 목록으로 표현하게 합니다.
  - EN: Have the financial data expressed as a table, the news as prose, and the technical specifications as a structured list.

## CCAR-F-Udemy04-0033

**JA** ある日用品メーカーの開発チームは、Claudeで構造化データ抽出システムを構築しています。取引先から届く商品仕様書から、商品名・内容量・希望小売価格・JANコードを抽出し、商品マスターへ登録します。

以前は応答のテキストからJSONを取り出していたため、構文エラーで処理が止まることがありました。JSONスキーマを入力パラメータにした抽出ツールをtool_useで呼び出す方式に変えたところ、構文エラーはなくなりました。しかし、内容量の「500」が希望小売価格のフィールドに入るなど、値が誤ったフィールドに入る誤りが約4%残っています。

この状況への対応として適切なものはどれですか。（2つ選択してください。）

**KO** 한 생활용품 제조업체의 개발팀은 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 거래처에서 받은 상품 사양서에서 상품명·내용량·희망 소매가격·JAN 코드를 추출해 상품 마스터에 등록합니다.

이전에는 응답 텍스트에서 JSON을 꺼냈기 때문에 구문 오류로 처리가 멈추는 경우가 있었습니다. JSON schema를 입력 파라미터로 삼은 추출 도구를 tool_use로 호출하는 방식으로 바꾸자 구문 오류는 사라졌습니다. 하지만 내용량 "500"이 희망 소매가격 필드에 들어가는 것처럼, 값이 엉뚱한 필드에 들어가는 오류가 약 4% 남아 있습니다.

이 상황에 대한 대응으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 各フィールドの説明に単位と仕様書上の記載位置を明記し、値の取り違えが起きにくくする。
  - KO: 각 필드의 설명에 단위와 사양서상의 기재 위치를 명시해, 값이 뒤바뀌기 어렵게 합니다.
  - EN: Specify the unit and the location in the specification sheet in each field's description to make value mix-ups less likely.
- B. JA: tool_choiceで抽出ツールを強制的に選択させ、毎回必ずこのツールが呼ばれるようにする。
  - KO: tool_choice로 추출 도구를 강제로 선택하게 해, 매번 반드시 이 도구가 호출되게 합니다.
  - EN: Use tool_choice to force selection of the extraction tool so that this tool is always called.
- C. JA: ツール定義にstrict: trueを追加し、出力がスキーマに準拠することを保証して誤りを防ぐ。
  - KO: 도구 정의에 strict: true를 추가해, 출력이 schema를 따르도록 보장함으로써 오류를 막습니다.
  - EN: Add strict: true to the tool definition to guarantee that the output conforms to the schema and prevent the errors.
- D. JA: 価格と内容量の桁や単位の整合など、意味的な正しさはアプリケーション側の検証コードで確認する。
  - KO: 가격과 내용량의 자릿수·단위 정합성 같은 의미상의 정확성은 애플리케이션 쪽 검증 코드로 확인합니다.
  - EN: Check semantic correctness, such as consistency of digits and units between the price and the content volume, with validation code on the application side.

## CCAR-F-Udemy04-0034

**JA** あるセキュリティ企業の開発チームは、CIパイプラインでClaude Codeにプルリクエストのレビューをさせています。現在、次の2つの問題が起きています。

ハードコードされた認証情報の検出で、似たようなコードでもテスト用のダミーのAPIキーを指摘したりしなかったりし、本物のトークンを見逃すこともある

指摘の書き方が実行ごとに異なり、開発者が対応すべき内容を読み取りにくい

プロンプトの改善として適切なものはどれですか。（2つ選択してください。）

**KO** 한 보안 기업의 개발팀은 CI pipeline에서 Claude Code에게 pull request 리뷰를 맡기고 있습니다. 현재 다음 두 가지 문제가 일어나고 있습니다.

하드코딩된 인증 정보를 탐지할 때, 비슷한 코드인데도 테스트용 더미 API 키를 지적하기도 하고 안 하기도 하며, 진짜 토큰을 놓치기도 한다

지적 사항의 작성 방식이 실행할 때마다 달라, 개발자가 무엇에 대응해야 하는지 파악하기 어렵다

prompt 개선으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 「確信度の高い指摘だけを報告すること」と指示し、迷うケースは報告しないようにする。
  - KO: "확신도가 높은 지적만 보고할 것"이라고 지시해, 애매한 경우는 보고하지 않게 합니다.
  - EN: Instruct it to "report only high-confidence findings," so that borderline cases are not reported.
- B. JA: 疑わしい文字列は広めに指摘させ、本物かどうかの判断は開発者に任せる。
  - KO: 의심스러운 문자열은 넓게 지적하게 하고, 진짜인지 여부의 판단은 개발자에게 맡깁니다.
  - EN: Have it flag suspicious strings broadly and leave the judgment of whether they are real to developers.
- C. JA: 出力例を、場所・問題・重大度・修正案の形式でそろえて示す。
  - KO: 위치·문제·심각도·수정안 형식으로 통일한 출력 예시를 보여 줍니다.
  - EN: Show output examples with a consistent format of location, problem, severity, and suggested fix.
- D. JA: ダミー値と本物の認証情報を対比したfew-shotの例を2〜4個示し、判断の理由を添える。
  - KO: 더미 값과 진짜 인증 정보를 대비한 few-shot 예시를 2~4개 보여 주고, 판단 이유를 덧붙입니다.
  - EN: Show two to four few-shot examples that contrast dummy values with real credentials, with the reasoning for each judgment attached.

## CCAR-F-Udemy04-0035

**JA** あるホテルチェーンの開発チームは、Claude Codeで予約データの移行スクリプトを作成しています。旧システムでは、連泊の途中で部屋を移った予約について、最初の部屋のチェックアウト日がnullで保存されています。

移行後のデータを確認すると、これらの予約の宿泊日数が0泊になっていました。開発者は「チェックアウト日がnullの場合は、同じ予約番号の次の部屋のチェックイン日を使う」と2回説明しましたが、修正後も別の予約で同じ誤りが残っています。

次に取るべき対応として最も効果的なものはどれですか。

**KO** 한 호텔 체인의 개발팀은 Claude Code로 예약 데이터 마이그레이션 스크립트를 작성하고 있습니다. 구 시스템에서는 연박 도중에 객실을 옮긴 예약의 경우, 첫 번째 객실의 체크아웃 날짜가 null로 저장되어 있습니다.

마이그레이션 후 데이터를 확인해 보니, 이런 예약의 숙박 일수가 0박으로 되어 있었습니다. 개발자는 "체크아웃 날짜가 null이면 같은 예약 번호의 다음 객실 체크인 날짜를 사용한다"라고 두 번 설명했지만, 수정 후에도 다른 예약에서 같은 오류가 남아 있습니다.

다음에 취할 대응으로 가장 효과적인 것은 무엇입니까?

- A. JA: nullを含む入力レコードと期待される出力を示すテストケースを渡し、通るまで修正させる。
  - KO: null을 포함한 입력 레코드와 기대 출력을 보여 주는 테스트 케이스를 건네고, 통과할 때까지 수정하게 합니다.
  - EN: Provide test cases showing input records that contain null and the expected output, and have it fix the script until they pass.
- B. JA: 新しいセッションを開始し、同じ説明を最初に伝えてからスクリプトを書き直させる。
  - KO: 새 session을 시작해, 같은 설명을 먼저 전달한 뒤 스크립트를 다시 작성하게 합니다.
  - EN: Start a new session, give the same explanation first, and have it rewrite the script.
- C. JA: 「null値に注意して堅牢に処理すること」とプロンプトに追記し、スクリプト全体を見直させる。
  - KO: "null 값에 주의해 견고하게 처리할 것"을 prompt에 추가하고, 스크립트 전체를 재검토하게 합니다.
  - EN: Add "handle null values robustly" to the prompt and have it review the entire script.
- D. JA: プランモードに切り替え、移行スクリプト全体の設計を最初から検討し直させる。
  - KO: plan mode로 전환해, 마이그레이션 스크립트 전체 설계를 처음부터 다시 검토하게 합니다.
  - EN: Switch to plan mode and have it reconsider the design of the entire migration script from scratch.

## CCAR-F-Udemy04-0036

**JA** ある化粧品メーカーの開発チームは、Claude Agent SDKでマルチエージェントリサーチシステムを構築しています。競合製品の成分を調べる検索サブエージェントは、社内の成分データベースに問い合わせるMCPツールsearch_ingredientsを使います。

このツールは現在、一致する成分が0件だった場合も、データベースへの接続がタイムアウトした場合も、空の配列を返しています。そのため最終レポートには、実際には調べられなかった製品について「該当成分なし」と書かれていました。

search_ingredientsの返し方として最も適切なものはどれですか。

**KO** 한 화장품 제조업체의 개발팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. 경쟁 제품의 성분을 조사하는 검색 subagent는 사내 성분 데이터베이스를 조회하는 MCP 도구 search_ingredients를 사용합니다.

이 도구는 현재 일치하는 성분이 0건일 때와 데이터베이스 연결이 timeout되었을 때 모두 빈 배열을 반환합니다. 그래서 최종 리포트에는 실제로는 조사하지 못한 제품에 대해 "해당 성분 없음"이라고 적혀 있었습니다.

search_ingredients의 반환 방식으로 가장 적절한 것은 무엇입니까?

- A. JA: どちらの場合もisError: trueを返し、エラーの文字列に「検索に失敗しました」と書く。
  - KO: 두 경우 모두 isError: true를 반환하고, 오류 문자열에 "검색에 실패했습니다"라고 씁니다.
  - EN: Return isError: true in both cases, and write 「検索に失敗しました」 in the error string.
- B. JA: タイムアウトした場合は、同じ製品について前回の検索で得た結果を成功として返す。
  - KO: timeout된 경우에는 같은 제품에 대해 이전 검색에서 얻은 결과를 성공으로 반환합니다.
  - EN: On a timeout, return the results obtained from the previous search for the same product as a success.
- C. JA: どちらの場合も空の配列を返し、タイムアウトの発生はサーバーのログにだけ記録する。
  - KO: 두 경우 모두 빈 배열을 반환하고, timeout 발생은 서버 로그에만 기록합니다.
  - EN: Return an empty array in both cases, and record the occurrence of the timeout only in the server's logs.
- D. JA: 0件は正常な空の結果、タイムアウトはリトライ可否付きのisError: trueとして返す。
  - KO: 0건은 정상적인 빈 결과로, timeout은 재시도 가능 여부를 포함한 isError: true로 반환합니다.
  - EN: Return zero matches as a normal empty result, and return a timeout as isError: true with an indication of whether it can be retried.

## CCAR-F-Udemy04-0037

**JA** ある建設会社の開発チームは、CIパイプラインでClaude Codeにプルリクエストのレビューをさせています。指摘のカテゴリ別に過去1か月の結果を分析したところ、次のことが分かりました。

SQLインジェクションとN+1クエリの指摘は、ほぼ正しかった

「命名規則」の指摘は約70%、「コメントの正確性」の指摘は約60%が誤検知だった

開発者の多くは、カテゴリにかかわらずレビューコメントを読まずに閉じるようになっています。

対応として適切なものはどれですか。（2つ選択してください。）

**KO** 한 건설 회사의 개발팀은 CI pipeline에서 Claude Code에게 pull request 리뷰를 맡기고 있습니다. 지적 카테고리별로 지난 1개월의 결과를 분석했더니 다음과 같았습니다.

SQL 인젝션과 N+1 쿼리 지적은 거의 정확했다

"명명 규칙" 지적의 약 70%, "주석의 정확성" 지적의 약 60%가 오탐이었다

개발자 대부분은 카테고리와 상관없이 리뷰 코멘트를 읽지 않고 닫게 되었습니다.

대응으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 誤検知の多い2つのカテゴリを一時的に無効化し、プロンプトを改善してから再開する。
  - KO: 오탐이 많은 두 카테고리를 일시적으로 비활성화하고, prompt를 개선한 뒤 다시 켭니다.
  - EN: Temporarily disable the two categories with many false positives, and re-enable them after improving the prompt.
- B. JA: 開発者の信頼が戻るまで、自動レビューを全カテゴリで停止する。
  - KO: 개발자의 신뢰가 돌아올 때까지 모든 카테고리의 자동 리뷰를 중단합니다.
  - EN: Stop automated review for all categories until developers' trust is restored.
- C. JA: コメントの正確性は「記述が実際の動作と矛盾する場合」に限るとプロンプトに書く。
  - KO: 주석의 정확성은 "설명이 실제 동작과 모순되는 경우"로 한정한다고 prompt에 씁니다.
  - EN: State in the prompt that comment accuracy findings are limited to "cases where the description contradicts the actual behavior."
- D. JA: 全カテゴリ共通で「確信度の高い指摘だけを報告すること」と指示する。
  - KO: 모든 카테고리에 공통으로 "확신도가 높은 지적만 보고할 것"이라고 지시합니다.
  - EN: Instruct, for all categories in common, "report only high-confidence findings."

## CCAR-F-Udemy04-0038

**JA** ある出版社の開発チームは、Claudeで構造化データ抽出システムを構築しています。印刷会社や翻訳者から届く請求書から、金額・支払期日・取引先コードを抽出しています。確信度が0.90以上の抽出は人によるレビューを省き、そのまま会計システムへ送っていました。

ところが、ある印刷会社が請求書の様式を変えてから、確信度0.95前後の抽出で支払期日の取り違えが3週間続きました。チームが気づいたのは、支払いの遅延が起きてからでした。

同様の問題を早期に検出するための変更として、最も効果的なものはどれですか。

**KO** 한 출판사의 개발팀은 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 인쇄소와 번역가에게서 받은 청구서에서 금액·지급 기일·거래처 코드를 추출합니다. 확신도가 0.90 이상인 추출 결과는 사람의 리뷰를 생략하고 바로 회계 시스템으로 보내고 있었습니다.

그런데 한 인쇄소가 청구서 양식을 바꾼 뒤, 확신도 0.95 안팎의 추출에서 지급 기일을 잘못 읽는 일이 3주 동안 이어졌습니다. 팀은 지급 지연이 발생한 뒤에야 알아차렸습니다.

비슷한 문제를 조기에 발견하기 위한 변경으로 가장 효과적인 것은 무엇입니까?

- A. JA: 新しい様式の請求書をfew-shotの例として抽出プロンプトに追加し、同じ取り違えが起きないようにする。
  - KO: 새 양식의 청구서를 few-shot 예시로 추출 prompt에 추가해, 같은 오류가 다시 일어나지 않게 합니다.
  - EN: Add invoices in the new format to the extraction prompt as few-shot examples so that the same mix-up does not occur.
- B. JA: 取引先から様式変更の連絡を受けたら、その取引先の請求書をしばらく全件レビューする運用にする。
  - KO: 거래처로부터 양식 변경 연락을 받으면, 그 거래처의 청구서를 한동안 전수 리뷰하도록 운영합니다.
  - EN: Adopt a practice of reviewing every invoice from a vendor for a while after being notified by that vendor of a format change.
- C. JA: 確信度の高い抽出についても、取引先と文書の種類で層に分けた無作為抽出を続け、層ごとのエラー率を測る。
  - KO: 확신도가 높은 추출에 대해서도 거래처와 문서 유형별로 층을 나눈 무작위 샘플링을 계속하고, 층별 오류율을 측정합니다.
  - EN: Continue random sampling of high-confidence extractions as well, stratified by vendor and document type, and measure the error rate for each stratum.
- D. JA: 自動で送る確信度のしきい値を0.90から0.97に引き上げ、人によるレビューに回る件数を増やす。
  - KO: 자동 전송 확신도 임계값을 0.90에서 0.97로 올려, 사람의 리뷰로 넘어가는 건수를 늘립니다.
  - EN: Raise the confidence threshold for automatic sending from 0.90 to 0.97 to increase the number of items routed to human review.

## CCAR-F-Udemy04-0039

**JA** ある家電メーカーの開発チームは、Claude Agent SDKでカスタマーサポート解決エージェントを構築しています。ログを分析したところ、次の2つの問題が見つかりました。

顧客が氏名だけを伝えたときにget_customerが同姓同名の顧客を3件返し、エージェントが直近に購入履歴のある1件を選んで修理の予約を進めた結果、別人の予約を変更していた

洗濯機の排水エラーについて、エージェントが同じリセット手順を言い回しを変えて4回案内し、40分以上解決しないまま会話が続いていた

改善策として適切なものはどれですか。（2つ選択してください。）

**KO** 한 가전제품 제조업체의 개발팀은 Claude Agent SDK로 고객 지원 해결 agent를 구축하고 있습니다. 로그를 분석했더니 다음 두 가지 문제가 발견되었습니다.

고객이 이름만 알려 주었을 때 get_customer가 동명이인 고객 3명을 반환했고, agent가 최근 구매 이력이 있는 1명을 골라 수리 예약을 진행한 결과 다른 사람의 예약을 변경했다

세탁기 배수 오류에 대해 agent가 같은 리셋 절차를 표현만 바꿔 4번 안내했고, 40분 넘게 해결되지 않은 채 대화가 이어졌다

개선책으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 案内できる手順を試しても解決に向けて進展しない場合は、人間の担当者にエスカレーションする。
  - KO: 안내할 수 있는 절차를 시도해도 해결 쪽으로 진전이 없으면, 사람 담당자에게 escalation합니다.
  - EN: If the procedures it can offer have been tried and there is no progress toward resolution, escalate to a human agent.
- B. JA: 複数の候補が一致した場合は、エージェントが最も可能性の高い顧客を選び、その根拠を記録に残す。
  - KO: 후보가 여러 명 일치하면, agent가 가장 가능성 높은 고객을 고르고 그 근거를 기록에 남깁니다.
  - EN: When multiple candidates match, have the agent choose the most likely customer and record its rationale.
- C. JA: 解決しない会話では、顧客の発言から不満の度合いを判定し、強いと判断したときにエスカレーションする。
  - KO: 해결되지 않는 대화에서는 고객의 발언으로 불만 정도를 판정하고, 강하다고 판단되면 escalation합니다.
  - EN: In conversations that are not resolved, judge the level of dissatisfaction from the customer's statements, and escalate when it is judged to be strong.
- D. JA: 複数の候補が一致した場合は、電話番号や注文番号などの追加の識別情報を尋ねてから進める。
  - KO: 후보가 여러 명 일치하면, 전화번호나 주문 번호 같은 추가 식별 정보를 물어본 뒤 진행합니다.
  - EN: When multiple candidates match, ask for additional identifying information such as a phone number or order number before proceeding.

## CCAR-F-Udemy04-0040

**JA** あるEC物流会社の開発チームは、Claudeで構造化データ抽出システムを構築しています。現在、次の3つの処理でリアルタイムのMessages API呼び出しを使っています。

(1)倉庫の作業員が端末の前で待つ間に、配送伝票から住所を抽出してラベル発行の可否を判定する処理

(2)月末に締めた運送会社の請求書を抽出し、翌週の監査担当者に渡す処理

(3)顧客がチャットに添付した伝票画像から追跡番号を抽出し、その場で配送状況を答える処理

コスト削減のため、Message Batches APIの利用を検討しています。

Message Batches APIの使い方として最も適切なものはどれですか。

**KO** 한 이커머스 물류 회사의 개발팀은 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 현재 다음 세 가지 처리에서 실시간 Messages API 호출을 사용하고 있습니다.

(1)창고 작업자가 단말기 앞에서 기다리는 동안, 배송 전표에서 주소를 추출해 라벨 발행 가능 여부를 판정하는 처리

(2)월말에 마감한 운송 회사의 청구서를 추출해, 다음 주에 감사 담당자에게 넘기는 처리

(3)고객이 채팅에 첨부한 전표 이미지에서 추적 번호를 추출해, 그 자리에서 배송 상황을 답하는 처리

비용 절감을 위해 Message Batches API 사용을 검토하고 있습니다.

Message Batches API의 사용 방식으로 가장 적절한 것은 무엇입니까?

- A. JA: (2)だけをバッチ処理に切り替え、(1)と(3)はリアルタイムの呼び出しを維持する。
  - KO: (2)만 batch 처리로 바꾸고, (1)과 (3)은 실시간 호출을 유지합니다.
  - EN: Switch only (2) to batch processing, and keep real-time calls for (1) and (3).
- B. JA: 3つともリアルタイムの呼び出しを維持し、プロンプトキャッシュを使ってコストを下げる。
  - KO: 세 가지 모두 실시간 호출을 유지하고, prompt caching으로 비용을 낮춥니다.
  - EN: Keep real-time calls for all three, and reduce costs by using prompt caching.
- C. JA: (1)と(2)をバッチ処理に切り替え、(3)はリアルタイムの呼び出しを維持する。
  - KO: (1)과 (2)를 batch 처리로 바꾸고, (3)은 실시간 호출을 유지합니다.
  - EN: Switch (1) and (2) to batch processing, and keep real-time calls for (3).
- D. JA: (2)と(3)をバッチ処理に切り替え、(1)はリアルタイムの呼び出しを維持する。
  - KO: (2)와 (3)을 batch 처리로 바꾸고, (1)은 실시간 호출을 유지합니다.
  - EN: Switch (2) and (3) to batch processing, and keep real-time calls for (1).

## CCAR-F-Udemy04-0041

**JA** ある自動車メーカーの品質保証部門は、Claude Agent SDKでマルチエージェントリサーチシステムを構築し、8か国のリコール情報を調べています。各国の規制当局のデータベースを検索するサブエージェントは、失敗したときに、失敗の種類・試行したクエリ・部分的な結果・考えられる代替手段を構造化して返します。

先週の実行では、7か国の検索は成功し、A国だけが権限エラーで失敗しました。エラーには、次の内容が示されていました。

A国のデータベースは有償契約者だけが閲覧できる

代替手段として、同国の官報に載るリコール公示を検索できる

ところがコーディネーターは、エラーを受け取ると8か国すべての検索を同じ指示で委任し直す作りになっていました。そのため、同じ権限エラーが3回繰り返されたうえ、検索のコストは通常の約4倍になりました。

コーディネーターの復旧の判断として適切なものはどれですか。（2つ選択してください。）

**KO** 한 자동차 제조업체의 품질보증 부서는 Claude Agent SDK로 multi-agent 리서치 시스템을 구축해 8개국의 리콜 정보를 조사하고 있습니다. 각국 규제 당국의 데이터베이스를 검색하는 subagent는 실패했을 때 실패 유형·시도한 쿼리·부분 결과·가능한 대안을 구조화해 반환합니다.

지난주 실행에서는 7개국 검색은 성공했고, A국만 권한 오류로 실패했습니다. 오류에는 다음 내용이 담겨 있었습니다.

A국의 데이터베이스는 유료 계약자만 열람할 수 있다

대안으로, 그 나라 관보에 실리는 리콜 공시를 검색할 수 있다

그런데 coordinator는 오류를 받으면 8개국 전체 검색을 같은 지시로 다시 위임하도록 만들어져 있었습니다. 그 때문에 같은 권한 오류가 3번 반복되었고, 검색 비용은 평소의 약 4배가 되었습니다.

coordinator의 복구 판단으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 成功した7か国の結果は再検索せず、部分的な結果としてそのまま統合に使う。
  - KO: 성공한 7개국의 결과는 다시 검색하지 않고, 부분 결과로서 그대로 통합에 사용합니다.
  - EN: Do not re-search the results for the seven successful countries, and use them as they are as partial results for synthesis.
- B. JA: A国については、指数バックオフを入れて、同じクエリのリトライを3回まで行わせる。
  - KO: A국에 대해서는 exponential backoff를 넣어, 같은 쿼리를 최대 3번까지 재시도하게 합니다.
  - EN: For Country A, add exponential backoff and have it retry the same query up to three times.
- C. JA: A国の失敗を受けた時点で実行全体を中断し、失敗の詳細を人間の担当者に報告する。
  - KO: A국의 실패를 받은 시점에 실행 전체를 중단하고, 실패 내용을 사람 담당자에게 보고합니다.
  - EN: Abort the entire run when Country A's failure is received, and report the failure details to a human agent.
- D. JA: A国については、エラーに示された官報のリコール公示を検索する作業を委任する。
  - KO: A국에 대해서는 오류에 제시된 관보의 리콜 공시를 검색하는 작업을 위임합니다.
  - EN: For Country A, delegate the task of searching the recall notices in the official gazette indicated in the error.

## CCAR-F-Udemy04-0042

**JA** ある旅行会社の開発チームは、コード生成やリファクタリングにClaude Codeを使っています。

リポジトリのルートにあるCLAUDE.mdは1,400行に増えており、次の内容も含まれています。

予約エンジンのインフラを定義するTerraformファイル（infra/配下の*.tf）専用の規約（600行）

年に数回しか行わない決済SDKの移行手順（200行）

フロントエンドの作業中もこれらがすべて読み込まれ、コンテキストを圧迫しています。

トークン使用量を減らす変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 여행사의 개발팀은 코드 생성과 refactoring에 Claude Code를 사용하고 있습니다.

저장소 루트에 있는 CLAUDE.md는 1,400줄로 불어났고, 다음 내용도 들어 있습니다.

예약 엔진의 인프라를 정의하는 Terraform 파일(infra/ 아래의 *.tf) 전용 규약(600줄)

1년에 몇 번밖에 하지 않는 결제 SDK 마이그레이션 절차(200줄)

프런트엔드 작업 중에도 이 내용이 모두 로드되어 context를 압박하고 있습니다.

토큰 사용량을 줄이는 변경으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: Terraformの規約を、paths: ["infra/**/*.tf"]を指定した.claude/rules/のファイルに移す。
  - KO: Terraform 규약을 paths: ["infra/**/*.tf"]를 지정한 .claude/rules/ 파일로 옮깁니다.
  - EN: Move the Terraform conventions to a file in .claude/rules/ with paths: ["infra/**/*.tf"] specified.
- B. JA: Terraformの規約をdocs/terraform.mdに書き出し、ルートのCLAUDE.mdから@importで読み込む。
  - KO: Terraform 규약을 docs/terraform.md로 분리하고, 루트의 CLAUDE.md에서 @import로 불러옵니다.
  - EN: Write the Terraform conventions out to docs/terraform.md and load them from the root CLAUDE.md with @import.
- C. JA: Terraformの規約を、各メンバーの~/.claude/rules/terraform.mdに移す。
  - KO: Terraform 규약을 각 멤버의 ~/.claude/rules/terraform.md로 옮깁니다.
  - EN: Move the Terraform conventions to each member's ~/.claude/rules/terraform.md.
- D. JA: 決済SDKの移行手順をスキルにして、必要なときだけ呼び出されて読み込まれるようにする。
  - KO: 결제 SDK 마이그레이션 절차를 skill로 만들어, 필요할 때만 호출되어 로드되게 합니다.
  - EN: Turn the payment SDK migration procedure into a skill so that it is invoked and loaded only when needed.

## CCAR-F-Udemy04-0043

**JA** ある会計事務所の開発チームは、Claude Agent SDKでマルチエージェントリサーチシステムを構築しています。税制改正の影響を調べるにあたり、開発を急いだため、サブエージェントどうしが共有のメッセージキューを通じて直接依頼を送り合う構成にしました。その結果、次の問題が起きています。

文書分析サブエージェントの失敗に誰も気づかないまま、統合が進むことがある

同じ検索が、別々のサブエージェントから重複して依頼される

どの情報がどの経路で流れたかを、ログから追えない

最も適切な改善策はどれですか。

**KO** 한 회계법인의 개발팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. 세제 개정의 영향을 조사하면서 개발을 서두른 탓에, subagent끼리 공유 메시지 큐를 통해 직접 요청을 주고받는 구성으로 만들었습니다. 그 결과 다음 문제가 일어나고 있습니다.

문서 분석 subagent가 실패해도 아무도 알아차리지 못한 채 통합이 진행되는 경우가 있다

같은 검색이 서로 다른 subagent로부터 중복으로 요청된다

어떤 정보가 어떤 경로로 흘렀는지 로그로 추적할 수 없다

가장 적절한 개선책은 무엇입니까?

- A. JA: 失敗したサブエージェントが、他のサブエージェントに直接エラーを通知する仕組みを追加する。
  - KO: 실패한 subagent가 다른 subagent에게 직접 오류를 알리는 구조를 추가합니다.
  - EN: Add a mechanism by which a failed subagent directly notifies other subagents of the error.
- B. JA: サブエージェントどうしの依頼にリトライと重複排除の仕組みを加え、キューの信頼性を上げる。
  - KO: subagent 간 요청에 재시도와 중복 제거 구조를 더해, 큐의 신뢰성을 높입니다.
  - EN: Add retry and deduplication mechanisms to requests between subagents to make the queue more reliable.
- C. JA: サブエージェント間の直接のやり取りをやめ、通信をすべてコーディネーター経由にする。
  - KO: subagent 간 직접 통신을 없애고, 모든 통신이 coordinator를 거치게 합니다.
  - EN: Stop direct communication between subagents and route all communication through the coordinator.
- D. JA: 共有キューに詳細なログ出力を追加し、流れたメッセージを記録して後から追跡できるようにする。
  - KO: 공유 큐에 상세한 로그 출력을 추가해, 흐른 메시지를 기록하고 나중에 추적할 수 있게 합니다.
  - EN: Add detailed logging to the shared queue and record the messages that flowed so they can be traced later.

## CCAR-F-Udemy04-0044

**JA** ある銀行の開発チームは、マルチエージェントリサーチシステムを構築しています。文書分析サブエージェントはMessages APIを直接呼び出すコードとして実装されており、結果を次のどちらかのツールで返す設計です。

report_findings（調査結果を構造化して返す）

report_no_relevant_content（関連する記述がなかったことを理由とともに返す）

コーディネーターは、このツール呼び出しを解析して次の処理を決めます。ところが、全体の約6%で、サブエージェントがどちらのツールも呼ばず、文章だけの要約を返して処理が止まっています。

最も適切な対処はどれですか。

**KO** 한 은행의 개발팀은 multi-agent 리서치 시스템을 구축하고 있습니다. 문서 분석 subagent는 Messages API를 직접 호출하는 코드로 구현되어 있으며, 결과를 다음 두 도구 중 하나로 반환하도록 설계되어 있습니다.

report_findings(조사 결과를 구조화해 반환한다)

report_no_relevant_content(관련 내용이 없었다는 사실을 이유와 함께 반환한다)

coordinator는 이 도구 호출을 파싱해 다음 처리를 결정합니다. 그런데 전체의 약 6%에서 subagent가 어느 도구도 호출하지 않고 텍스트로만 된 요약을 반환해, 처리가 멈추고 있습니다.

가장 적절한 대처는 무엇입니까?

- A. JA: tool_choiceで{"type": "tool", "name": "report_findings"}を指定し、常にこのツールを呼ばせる。
  - KO: tool_choice에 {"type": "tool", "name": "report_findings"}를 지정해, 항상 이 도구를 호출하게 합니다.
  - EN: Specify {"type": "tool", "name": "report_findings"} with tool_choice so that this tool is always called.
- B. JA: tool_choiceを"auto"のままにし、「必ずどちらかのツールで結果を返すこと」とプロンプトで強調する。
  - KO: tool_choice를 "auto"로 둔 채, prompt에서 "반드시 둘 중 한 도구로 결과를 반환할 것"이라고 강조합니다.
  - EN: Leave tool_choice as "auto" and emphasize in the prompt, "always return the result with one of the tools."
- C. JA: 文章だけの応答が返ったら、コーディネーター側で文章を解析して調査結果に変換する。
  - KO: 텍스트만 있는 응답이 오면, coordinator 쪽에서 텍스트를 파싱해 조사 결과로 변환합니다.
  - EN: When a text-only response is returned, have the coordinator parse the text and convert it into research findings.
- D. JA: tool_choiceを"any"に設定し、2つのツールのどちらかを必ず呼び出させる。
  - KO: tool_choice를 "any"로 설정해, 두 도구 중 하나를 반드시 호출하게 합니다.
  - EN: Set tool_choice to "any" so that one of the two tools is always called.

## CCAR-F-Udemy04-0045

**JA** ある化学メーカーの開発チームは、Claudeで構造化データ抽出システムを構築しています。原料メーカーから届く分析証明書から、各成分の含有率と、証明書に記載された合計値を抽出しています。スキーマには次のフィールドがあります。

stated_total（証明書に記載された合計）

calculated_total（抽出した各成分から計算した合計）

conflict_detected（両者の不一致を示す）

現在は、不一致が検出されると最大3回まで再抽出しています。その結果、全体の18%の文書がリトライの上限に達し、APIコストが想定の2倍になりました。調べたところ、上限に達した文書の大半は、証明書そのものの合計欄に転記ミスがあるものでした。

最も適切な改善方法はどれですか。

**KO** 한 화학 제조업체의 개발팀은 Claude로 구조화 데이터 추출 시스템을 구축하고 있습니다. 원료 제조사에서 받은 분석 증명서에서 각 성분의 함유율과, 증명서에 기재된 합계값을 추출합니다. schema에는 다음 필드가 있습니다.

stated_total(증명서에 기재된 합계)

calculated_total(추출한 각 성분으로 계산한 합계)

conflict_detected(두 값의 불일치를 나타낸다)

현재는 불일치가 감지되면 최대 3번까지 재추출합니다. 그 결과 전체 문서의 18%가 재시도 상한에 도달했고, API 비용이 예상의 2배가 되었습니다. 조사해 보니 상한에 도달한 문서 대부분은 증명서 자체의 합계란에 옮겨 적기 실수가 있는 것이었습니다.

가장 적절한 개선 방법은 무엇입니까?

- A. JA: 合計が一致しない文書は抽出結果を破棄し、処理対象から除外して記録だけを残す。
  - KO: 합계가 일치하지 않는 문서는 추출 결과를 버리고, 처리 대상에서 제외한 뒤 기록만 남깁니다.
  - EN: Discard the extraction results for documents whose totals do not match, exclude them from processing, and keep only a record.
- B. JA: リトライは1回までにし、なお一致しない文書はconflict_detectedをtrueのまま担当者のレビューに回す。
  - KO: 재시도는 1번까지만 하고, 그래도 일치하지 않는 문서는 conflict_detected를 true로 둔 채 담당자 리뷰로 넘깁니다.
  - EN: Limit retries to one, and route documents that still do not match to review by a person in charge with conflict_detected left as true.
- C. JA: リトライの上限を3回から5回に増やし、合計が一致するまで再抽出を続ける。
  - KO: 재시도 상한을 3번에서 5번으로 늘리고, 합계가 일치할 때까지 재추출을 계속합니다.
  - EN: Increase the retry limit from three to five, and keep re-extracting until the totals match.
- D. JA: stated_totalをcalculated_totalの値で上書きし、合計が一致した状態で下流システムへ送る。
  - KO: stated_total을 calculated_total 값으로 덮어쓰고, 합계가 일치하는 상태로 하위(downstream) 시스템에 보냅니다.
  - EN: Overwrite stated_total with the value of calculated_total and send the data to downstream systems with the totals in agreement.

## CCAR-F-Udemy04-0046

**JA** ある法律事務所の開発チームは、Claude Codeで社内の契約管理システムの改修を進めています。次の作業は、電子署名サービスを別の事業者へ切り替えるための調査で、署名処理に関わるモジュールを洗い出す必要があります。

前回の同様の調査では、メインのセッションに数百ファイル分の検索結果とファイル内容が読み込まれ、実装を始める頃には重要な判断が会話から押し出されていました。また、調査の途中で誤ってファイルが書き換えられたこともありました。今回は、調査中の編集を確実に防ぎたいと考えています。

最も適切な方法はどれですか。

**KO** 한 법률 사무소의 개발팀은 Claude Code로 사내 계약 관리 시스템을 수정하고 있습니다. 다음 작업은 전자 서명 서비스를 다른 업체로 바꾸기 위한 조사로, 서명 처리와 관련된 모듈을 빠짐없이 찾아내야 합니다.

지난번 비슷한 조사에서는 메인 session에 수백 개 파일 분량의 검색 결과와 파일 내용이 로드되어, 구현을 시작할 즈음에는 중요한 결정 사항이 대화에서 밀려나 있었습니다. 또 조사 도중에 실수로 파일이 수정된 일도 있었습니다. 이번에는 조사 중 편집을 확실히 막고 싶습니다.

가장 적절한 방법은 무엇입니까?

- A. JA: 調査をExploreサブエージェントに任せ、要約だけをメインの会話に返させる。
  - KO: 조사를 Explore subagent에게 맡기고, 요약만 메인 대화로 반환하게 합니다.
  - EN: Delegate the investigation to an Explore subagent and have it return only a summary to the main conversation.
- B. JA: 汎用（general-purpose）サブエージェントに調査を任せ、結果をファイルに書き出させる。
  - KO: 범용(general-purpose) subagent에게 조사를 맡기고, 결과를 파일로 저장하게 합니다.
  - EN: Delegate the investigation to a general-purpose subagent and have it write the results to a file.
- C. JA: メインのセッションで調査し、実装を始める前に/compactで会話を要約する。
  - KO: 메인 session에서 조사하고, 구현을 시작하기 전에 /compact로 대화를 요약합니다.
  - EN: Investigate in the main session, and summarize the conversation with /compact before starting implementation.
- D. JA: メインのセッションをプランモードに切り替え、同じセッションの中で調査を進めさせる。
  - KO: 메인 session을 plan mode로 전환하고, 같은 session 안에서 조사를 진행하게 합니다.
  - EN: Switch the main session to plan mode and carry out the investigation within the same session.

## CCAR-F-Udemy04-0047

**JA** ある半導体メーカーの開発チームは、Claude Agent SDKでマルチエージェントリサーチシステムを構築しています。開発を急いだため、ウェブ検索・文書分析・統合・レポート生成のすべてのサブエージェントに、同じ18個のツールを与えています。

評価では、文書分析サブエージェントが特許文書を分析する途中でウェブ検索やレポートの書式設定のツールを呼び出すなど、ツールの選択を誤るケースが15%ありました。

最も効果的な対処はどれですか。

**KO** 한 반도체 제조업체의 개발팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. 개발을 서두른 탓에 웹 검색·문서 분석·통합·리포트 생성의 모든 subagent에 같은 18개 도구를 주었습니다.

평가에서는 문서 분석 subagent가 특허 문서를 분석하던 도중 웹 검색이나 리포트 서식 설정 도구를 호출하는 등, 도구를 잘못 선택하는 경우가 15% 있었습니다.

가장 효과적인 대처는 무엇입니까?

- A. JA: ツールの呼び出しを記録して、誤った選択があったら分析をやり直す監視処理を追加する。
  - KO: 도구 호출을 기록하고, 잘못된 선택이 있으면 분석을 다시 하는 감시 처리를 추가합니다.
  - EN: Add monitoring that logs tool calls and redoes the analysis if an incorrect selection occurred.
- B. JA: 18個すべてのツールの説明を詳しく書き直し、どのサブエージェントでも正しく選べるようにする。
  - KO: 18개 도구 전체의 설명을 자세히 다시 써서, 어느 subagent든 올바르게 고를 수 있게 합니다.
  - EN: Rewrite the descriptions of all 18 tools in more detail so that any subagent can select correctly.
- C. JA: 文書分析サブエージェントのtool_choiceを"any"に設定し、必ずツールを呼ばせる。
  - KO: 문서 분석 subagent의 tool_choice를 "any"로 설정해, 반드시 도구를 호출하게 합니다.
  - EN: Set the document analysis subagent's tool_choice to "any" so that it always calls a tool.
- D. JA: 各サブエージェントのツールを、その役割に必要な4〜5個に絞る。
  - KO: 각 subagent의 도구를 그 역할에 필요한 4~5개로 줄입니다.
  - EN: Narrow each subagent's tools down to the four to five that its role requires.

## CCAR-F-Udemy04-0048

**JA** ある研究機関の開発チームは、Claude Agent SDKでマルチエージェントリサーチシステムを構築しています。

「国内の再生医療研究の動向」を調べたところ、ウェブ検索サブエージェントは関連する論文と報道を28件見つけ、文書分析サブエージェントも各論文の要点を正しく抽出していました。ところが、統合サブエージェントが作った草稿は、どの調査結果にも触れない一般論ばかりでした。

ログを確認すると、コーディネーターが統合サブエージェントを呼び出したときのプロンプトは、「これまでの検索結果と分析結果を統合して草稿を作ってください」の1文だけでした。

最も可能性の高い根本原因はどれですか。

**KO** 한 연구 기관의 개발팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다.

"국내 재생의료 연구 동향"을 조사했더니, 웹 검색 subagent는 관련 논문과 보도 28건을 찾았고, 문서 분석 subagent도 각 논문의 요점을 정확히 추출했습니다. 그런데 통합 subagent가 만든 초안은 어느 조사 결과도 언급하지 않는 일반론뿐이었습니다.

로그를 확인해 보니, coordinator가 통합 subagent를 호출할 때의 prompt는 "지금까지의 검색 결과와 분석 결과를 통합해 초안을 작성해 주세요" 한 문장뿐이었습니다.

가장 가능성이 높은 근본 원인은 무엇입니까?

- A. JA: 文書分析サブエージェントが要点を短く要約しすぎ、統合に必要な情報が失われている。
  - KO: 문서 분석 subagent가 요점을 지나치게 짧게 요약해, 통합에 필요한 정보가 사라졌습니다.
  - EN: The document analysis subagent summarized the key points too briefly, and information needed for synthesis was lost.
- B. JA: 統合サブエージェントのコンテキストウィンドウが、28件分の検索結果で埋まってあふれている。
  - KO: 통합 subagent의 context window가 28건 분량의 검색 결과로 가득 차 넘쳤습니다.
  - EN: The synthesis subagent's context window is overflowing, filled with the search results for 28 items.
- C. JA: 統合サブエージェントのツールに検索ツールが含まれておらず、自分で情報を集められない。
  - KO: 통합 subagent의 도구에 검색 도구가 없어, 스스로 정보를 모을 수 없습니다.
  - EN: The synthesis subagent's tools do not include a search tool, so it cannot gather information on its own.
- D. JA: 統合サブエージェントには調査結果が自動では渡らず、プロンプトにも含まれていない。
  - KO: 통합 subagent에게는 조사 결과가 자동으로 전달되지 않는데, prompt에도 포함되어 있지 않습니다.
  - EN: The research findings are not passed automatically to the synthesis subagent, and they are not included in the prompt either.

## CCAR-F-Udemy04-0049

**JA** ある通信事業者の開発チームは、Claude Agent SDKでカスタマーサポート解決エージェントを構築しています。ある顧客は1回の問い合わせの中で、次の3つを相談しました。

(1)9月分の請求で通話料が二重に計上されている件

(2)端末の分割払いの残額の件

(3)解約した場合の違約金の件

やり取りが30ターンを超えると、エージェントは二重計上の金額と分割払いの残額を取り違えたり、すでに解決した(1)をもう一度調べ始めたりしました。また、注文照会のツールは1回あたり40以上のフィールドを返しています。

改善策として適切なものはどれですか。（2つ選択してください。）

**KO** 한 통신사의 개발팀은 Claude Agent SDK로 고객 지원 해결 agent를 구축하고 있습니다. 한 고객이 한 번의 문의에서 다음 세 가지를 상담했습니다.

(1)9월분 청구서에 통화료가 이중으로 계상된 건

(2)단말기 할부 잔액 건

(3)해지할 경우의 위약금 건

대화가 30 turn을 넘자, agent는 이중 계상 금액과 할부 잔액을 혼동하거나, 이미 해결된 (1)을 다시 조사하기 시작했습니다. 또한 주문 조회 도구는 1회 호출마다 40개가 넘는 필드를 반환합니다.

개선책으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 解決した案件のターンを会話履歴から削除し、未解決の案件のやり取りだけを残す。
  - KO: 해결된 건의 turn을 대화 기록에서 삭제하고, 미해결 건의 대화만 남깁니다.
  - EN: Delete the turns for resolved matters from the conversation history, and keep only the exchanges for unresolved matters.
- B. JA: 案件ごとの番号・金額・状態を構造化し、会話とは別のレイヤーに保持して毎ターン渡す。
  - KO: 건별 번호·금액·상태를 구조화해 대화와 별도의 레이어에 보관하고, 매 turn 전달합니다.
  - EN: Structure each matter's number, amount, and status, keep them in a layer separate from the conversation, and pass them in every turn.
- C. JA: ツールの出力は、各案件に関係するフィールドだけに切り詰めてから会話に加える。
  - KO: 도구 출력은 각 건과 관련된 필드만 남기도록 잘라 낸 뒤 대화에 추가합니다.
  - EN: Trim tool output to only the fields relevant to each matter before adding it to the conversation.
- D. JA: 3つの案件を1つの要約文にまとめ、古いターンはその要約に置き換えて送信する。
  - KO: 세 가지 건을 하나의 요약문으로 묶고, 오래된 turn을 그 요약으로 대체해 전송합니다.
  - EN: Combine the three matters into a single summary text, and send it with older turns replaced by that summary.

## CCAR-F-Udemy04-0050

**JA** ある家電メーカーの開発チームは、開発者の生産性を上げるためにClaude Codeを使っています。エンジニアが、次の2つの作業を依頼しようとしています。

スマート家電のファームウェア更新に使う通信ライブラリを、新しいメジャーバージョンへ移行する作業（60以上のファイルに影響し、再接続処理の実装方針も複数考えられる）

設定画面に表示されるエラーメッセージの誤字を1か所直す作業

進め方として適切なものはどれですか。（2つ選択してください。）

**KO** 한 가전제품 제조업체의 개발팀은 개발자 생산성을 높이기 위해 Claude Code를 사용하고 있습니다. 엔지니어가 다음 두 작업을 요청하려고 합니다.

스마트 가전의 펌웨어 업데이트에 쓰는 통신 라이브러리를 새 메이저 버전으로 마이그레이션하는 작업(60개가 넘는 파일에 영향을 주며, 재연결 처리의 구현 방향도 여러 가지가 가능하다)

설정 화면에 표시되는 오류 메시지의 오타 한 곳을 고치는 작업

진행 방식으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: ライブラリの移行はプランモードで調査・計画し、計画の承認後に直接実行で実装する。
  - KO: 라이브러리 마이그레이션은 plan mode로 조사·계획하고, 계획이 승인된 뒤 직접 실행으로 구현합니다.
  - EN: Investigate and plan the library migration in plan mode, and implement it with direct execution after the plan is approved.
- B. JA: ライブラリの移行は、影響するファイルを10件ずつに分け、それぞれを直接実行で順に修正する。
  - KO: 라이브러리 마이그레이션은 영향받는 파일을 10개씩 나누어, 각각 직접 실행으로 차례대로 수정합니다.
  - EN: Split the library migration into groups of 10 affected files, and fix each group in turn with direct execution.
- C. JA: 誤字の修正もプランモードで計画を作成させ、内容をレビューしてから実行する。
  - KO: 오타 수정도 plan mode로 계획을 세우게 하고, 내용을 리뷰한 뒤 실행합니다.
  - EN: Have it create a plan in plan mode for the typo fix as well, and execute after reviewing the contents.
- D. JA: 誤字の修正は、プランモードを使わずに直接実行で行う。
  - KO: 오타 수정은 plan mode를 쓰지 않고 직접 실행으로 처리합니다.
  - EN: Carry out the typo fix with direct execution, without using plan mode.

## CCAR-F-Udemy04-0051

**JA** あるスポーツ用品メーカーの開発チームは、GitHub ActionsでClaude Codeを実行し、プルリクエストごとにテストコードの生成と、そのテストのレビューを行っています。現在のジョブは、claude -pでテストを生成したあと、claude -p --continueで同じセッションを続け、「生成したテストをレビューして」と依頼しています。

レビューではほとんど指摘が出ないのに、マージ後にテストの抜けや誤った期待値が見つかっています。

改善策として適切なものはどれですか。（2つ選択してください。）

**KO** 한 스포츠용품 제조업체의 개발팀은 GitHub Actions에서 Claude Code를 실행해, pull request마다 테스트 코드를 생성하고 그 테스트를 리뷰하고 있습니다. 현재 작업은 claude -p로 테스트를 생성한 뒤, claude -p --continue로 같은 session을 이어서 "생성한 테스트를 리뷰해 줘"라고 요청합니다.

리뷰에서는 지적이 거의 나오지 않는데, 머지 후에 테스트 누락이나 잘못된 기댓값이 발견되고 있습니다.

개선책으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 生成のプロンプトに「出力前に自分で確認すること」と追記し、レビューの実行を省く。
  - KO: 생성 prompt에 "출력 전에 스스로 확인할 것"을 추가하고, 리뷰 실행은 생략합니다.
  - EN: Add "verify it yourself before output" to the generation prompt, and skip running the review.
- B. JA: テスト標準とレビュー基準をリポジトリのCLAUDE.mdに書き、レビューの実行でもその基準を参照させる。
  - KO: 테스트 표준과 리뷰 기준을 저장소의 CLAUDE.md에 적고, 리뷰 실행에서도 그 기준을 참조하게 합니다.
  - EN: Write the test standards and review criteria in the repository's CLAUDE.md, and have the review run refer to those criteria as well.
- C. JA: 生成と同じセッションを--resumeで再開し、「厳しく確認すること」とプロンプトを強める。
  - KO: 생성과 같은 session을 --resume으로 재개하고, "엄격하게 확인할 것"이라고 prompt를 강화합니다.
  - EN: Resume the same session as the generation with --resume, and strengthen the prompt with "check strictly."
- D. JA: レビューは--continueを付けない別のclaude -p実行にし、新しいセッションで差分を読ませる。
  - KO: 리뷰는 --continue를 붙이지 않은 별도의 claude -p 실행으로 하고, 새 session에서 diff를 읽게 합니다.
  - EN: Make the review a separate claude -p run without --continue, and have it read the diff in a new session.

## CCAR-F-Udemy04-0052

**JA** ある農業IoT企業の開発チームは、Claude Agent SDKで開発者の生産性向上ツールを構築しています。このエージェントでは、組み込みのRead・Grep・Globが有効になっています。現場の担当者から、「センサーIDが登録されていません」というエラーが出るという報告がありました。エンジニアは、次の2点を知りたいと考えています。

このメッセージがどこで出力されているか

センサーIDを検証するvalidateSensorId関数がどこから呼ばれているか

エージェントに使わせるツールの選び方として適切なものはどれですか。（2つ選択してください。）

**KO** 한 농업 IoT 기업의 개발팀은 Claude Agent SDK로 개발자 생산성 향상 도구를 구축하고 있습니다. 이 agent에는 내장 Read·Grep·Glob이 활성화되어 있습니다. 현장 담당자로부터 "센서 ID가 등록되어 있지 않습니다"라는 오류가 난다는 보고가 들어왔습니다. 엔지니어는 다음 두 가지를 알고 싶어 합니다.

이 메시지가 어디에서 출력되는지

센서 ID를 검증하는 validateSensorId 함수가 어디에서 호출되는지

agent에게 사용하게 할 도구를 고르는 방법으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: Globで**/*sensor*に一致するファイルを列挙し、見つかったファイルを順にReadで読む。
  - KO: Glob으로 **/*sensor*에 일치하는 파일을 나열하고, 찾은 파일을 차례로 Read로 읽습니다.
  - EN: Use Glob to list the files matching **/*sensor*, and read the files found one by one with Read.
- B. JA: Grepでエラーメッセージの文字列を検索し、出力している箇所を特定する。
  - KO: Grep으로 오류 메시지 문자열을 검색해, 출력하는 위치를 특정합니다.
  - EN: Use Grep to search for the error message string and identify where it is output.
- C. JA: Bashのfindで、ファイル名にerrorを含むファイルを探して内容を確認する。
  - KO: Bash의 find로 파일 이름에 error가 들어간 파일을 찾아 내용을 확인합니다.
  - EN: Use Bash find to look for files whose names contain error and check their contents.
- D. JA: Grepでコードベース全体からvalidateSensorIdの呼び出しを検索する。
  - KO: Grep으로 코드베이스 전체에서 validateSensorId 호출을 검색합니다.
  - EN: Use Grep to search the entire codebase for calls to validateSensorId.

## CCAR-F-Udemy04-0053

**JA** ある農業機械メーカーの開発チームは、Claude Agent SDKで開発者の生産性向上ツールを構築しています。このエージェントは、灌漑制御システムのインフラ設定リポジトリでも作業します。本番環境への反映は、担当者がterraform planの結果を確認してから行う決まりです。

しかし先月、エージェントがBashでterraform applyを実行し、ある圃場の給水スケジュールが意図せず変わる事故が起きました。CLAUDE.mdには「applyは実行しないこと」と書かれていました。

再発防止策として適切なものはどれですか。（2つ選択してください。）

**KO** 한 농기계 제조업체의 개발팀은 Claude Agent SDK로 개발자 생산성 향상 도구를 구축하고 있습니다. 이 agent는 관개 제어 시스템의 인프라 설정 저장소에서도 작업합니다. 프로덕션 환경 반영은 담당자가 terraform plan 결과를 확인한 뒤에 하도록 정해져 있습니다.

그런데 지난달 agent가 Bash로 terraform apply를 실행해, 한 농지의 급수 스케줄이 의도치 않게 바뀌는 사고가 일어났습니다. CLAUDE.md에는 "apply는 실행하지 말 것"이라고 적혀 있었습니다.

재발 방지책으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: PreToolUseフックで、terraform applyを含むBashの呼び出しを拒否する。
  - KO: PreToolUse hook으로 terraform apply가 포함된 Bash 호출을 거부합니다.
  - EN: Use a PreToolUse hook to deny Bash calls that contain terraform apply.
- B. JA: 拒否の理由に、planの結果を担当者の確認に回す手順を示し、代わりの手順へ進ませる。
  - KO: 거부 사유에 plan 결과를 담당자 확인으로 넘기는 절차를 제시해, 대체 절차로 진행하게 합니다.
  - EN: In the denial reason, indicate the procedure for routing the plan results to the person in charge for review, and have the agent proceed to the alternative procedure.
- C. JA: CLAUDE.mdの記述を冒頭に移し、「IMPORTANT」を付けて強調して書き直す。
  - KO: CLAUDE.md의 해당 문구를 맨 앞으로 옮기고, "IMPORTANT"를 붙여 강조해 다시 씁니다.
  - EN: Move the statement in CLAUDE.md to the top and rewrite it with emphasis by adding "IMPORTANT."
- D. JA: PostToolUseフックで、applyの実行結果を検出したら直前の状態にロールバックする。
  - KO: PostToolUse hook으로 apply 실행 결과를 감지하면 직전 상태로 롤백합니다.
  - EN: Use a PostToolUse hook to roll back to the previous state when the result of an apply execution is detected.

## CCAR-F-Udemy04-0054

**JA** ある広告代理店の開発チームは、Claude Agent SDKでマルチエージェントリサーチシステムを構築しています。新商品の市場調査では、10代・20代・30代・40代・50代以上の5つの年代について、それぞれ独立に消費動向を調べたうえで、最後に年代間の比較をまとめます。

ログを見ると、コーディネーターは1回の応答でAgentツール（旧Taskツール）を1回だけ呼び出し、結果が返るのを待ってから次の年代を委任していました。そのため、調査全体に想定の5倍の時間がかかっていました。

改善策として適切なものはどれですか。（2つ選択してください。）

**KO** 한 광고 대행사의 개발팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. 신상품 시장 조사에서는 10대·20대·30대·40대·50대 이상의 다섯 연령대에 대해 각각 독립적으로 소비 동향을 조사한 뒤, 마지막에 연령대 간 비교를 정리합니다.

로그를 보니 coordinator는 한 번의 응답에서 Agent 도구(이전 명칭 Task 도구)를 한 번만 호출하고, 결과가 돌아오기를 기다린 뒤에 다음 연령대를 위임하고 있었습니다. 그 때문에 조사 전체에 예상의 5배나 되는 시간이 걸렸습니다.

개선책으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 5つの年代の調査は、コーディネーターの1つの応答で複数のAgentツール呼び出しとして出させる。
  - KO: 다섯 연령대 조사는 coordinator의 한 응답에서 여러 개의 Agent 도구 호출로 내보내게 합니다.
  - EN: Have the coordinator issue the research for the five age groups as multiple Agent tool calls within a single response.
- B. JA: 年代間の比較も含めた6つの委任を、すべて同じ応答で同時に出させる。
  - KO: 연령대 간 비교를 포함한 6개 위임을 모두 같은 응답에서 동시에 내보내게 합니다.
  - EN: Have all six delegations, including the comparison across age groups, issued at the same time in the same response.
- C. JA: 年代間の比較は、5つの調査結果がそろってから、次のターンで委任させる。
  - KO: 연령대 간 비교는 다섯 조사 결과가 모두 모인 뒤, 다음 turn에서 위임하게 합니다.
  - EN: Have the comparison across age groups delegated in the next turn, after the five research results are available.
- D. JA: コーディネーターからAgentツールを外し、5つの年代を1つのプロンプトでまとめて調べさせる。
  - KO: coordinator에서 Agent 도구를 빼고, 다섯 연령대를 하나의 prompt로 한꺼번에 조사하게 합니다.
  - EN: Remove the Agent tool from the coordinator and have it research the five age groups together in a single prompt.

## CCAR-F-Udemy04-0055

**JA** ある会計事務所の開発チームは、Claude Agent SDKで開発者の生産性向上ツールを構築しています。このツールにはセッションの再開機能があり、エンジニアはコードベースの調査を数日に分けて進められます。

今朝、2人のエンジニアが前日の調査の続きを始めようとしています。

Aさんは税額計算モジュールを調査中で、昨日以降の変更はREADMEの誤字修正1件だけ

Bさんは仕訳エンジンを調査中だが、夜間に大規模なリファクタリングがマージされ、昨日分析したファイルの約4割が移動または名前変更された

それぞれの再開方法として最も適切なものはどれですか。

**KO** 한 회계법인의 개발팀은 Claude Agent SDK로 개발자 생산성 향상 도구를 구축하고 있습니다. 이 도구에는 session 재개 기능이 있어, 엔지니어가 코드베이스 조사를 며칠에 나눠 진행할 수 있습니다.

오늘 아침 두 엔지니어가 전날 조사를 이어서 하려고 합니다.

A씨는 세액 계산 모듈을 조사 중이며, 어제 이후 변경은 README 오타 수정 1건뿐이다

B씨는 분개 엔진을 조사 중인데, 밤사이 대규모 refactoring이 머지되어 어제 분석한 파일의 약 40%가 이동되거나 이름이 바뀌었다

각자의 재개 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: Aさん・Bさんとも前日のセッションをそのまま再開し、変更があったファイルの一覧だけを伝える。
  - KO: A씨와 B씨 모두 전날 session을 그대로 재개하고, 변경된 파일 목록만 알려 줍니다.
  - EN: Both Engineer A and Engineer B resume the previous day's session as is, and tell it only the list of files that changed.
- B. JA: Aさんは新しいセッションに前日の要約を注入して開始し、Bさんは前日のセッションをそのまま再開する。
  - KO: A씨는 전날 요약을 주입한 새 session으로 시작하고, B씨는 전날 session을 그대로 재개합니다.
  - EN: Engineer A starts a new session with a summary of the previous day injected, and Engineer B resumes the previous day's session as is.
- C. JA: Aさん・Bさんとも新しいセッションを開始し、前日の調査をそれぞれ最初からやり直させる。
  - KO: A씨와 B씨 모두 새 session을 시작해, 전날 조사를 각자 처음부터 다시 하게 합니다.
  - EN: Both Engineer A and Engineer B start new sessions and have the previous day's investigation redone from the beginning.
- D. JA: Aさんは前日のセッションをそのまま再開し、Bさんは有効な調査結果の要約を新しいセッションに注入する。
  - KO: A씨는 전날 session을 그대로 재개하고, B씨는 유효한 조사 결과의 요약을 새 session에 주입합니다.
  - EN: Engineer A resumes the previous day's session as is, and Engineer B injects a summary of the still-valid investigation findings into a new session.

## CCAR-F-Udemy04-0056

**JA** ある非営利団体の開発チームは、寄付管理システムのCIパイプラインにClaude Codeを組み込み、夜間にテストケースを生成しています。現在の夜間ジョブでは、次のやり取りを1ファイルあたり平均6回繰り返しています。

Claudeがテストを書く

Bashでテストを実行する

失敗した結果を見て修正する

予算が限られているため、50%のコスト削減を見込んでMessage Batches APIへの移行を検討しています。

移行の設計として適切なものはどれですか。（2つ選択してください。）

**KO** 한 비영리 단체의 개발팀은 기부 관리 시스템의 CI pipeline에 Claude Code를 넣어, 야간에 테스트 케이스를 생성하고 있습니다. 현재 야간 작업은 다음 과정을 파일 1개당 평균 6번 반복합니다.

Claude가 테스트를 작성한다

Bash로 테스트를 실행한다

실패한 결과를 보고 수정한다

예산이 한정되어 있어, 50% 비용 절감을 기대하고 Message Batches API로 전환하는 것을 검토하고 있습니다.

전환 설계로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: リクエストのcustom_idを連番にして、1つのリクエストの中で前のリクエストの結果を参照させる。
  - KO: 요청의 custom_id를 일련번호로 매기고, 한 요청 안에서 이전 요청의 결과를 참조하게 합니다.
  - EN: Number the requests' custom_id sequentially, and have one request refer to the results of previous requests.
- B. JA: ソースと既存テストをあらかじめプロンプトに含め、1回の応答で完結するテスト案の生成だけをバッチに送る。
  - KO: 소스와 기존 테스트를 미리 prompt에 넣고, 한 번의 응답으로 끝나는 테스트 초안 생성만 batch로 보냅니다.
  - EN: Include the source and existing tests in the prompt in advance, and send to the batch only the generation of test proposals that are completed in a single response.
- C. JA: テストを実行して失敗を見ながら直す反復は、ツールの結果を返せる同期の実行に残す。
  - KO: 테스트를 실행하고 실패를 보면서 고치는 반복은, 도구 결과를 돌려줄 수 있는 동기 실행으로 남겨 둡니다.
  - EN: Keep the iteration of running tests and fixing based on failures in synchronous execution, which can return tool results.
- D. JA: バッチの各リクエストにBashツールを定義し、バッチの処理中にテストを実行させて結果を受け取る。
  - KO: batch의 각 요청에 Bash 도구를 정의해, batch 처리 중에 테스트를 실행하고 결과를 받게 합니다.
  - EN: Define a Bash tool in each batch request, and have it run tests and receive the results while the batch is being processed.

## CCAR-F-Udemy04-0057

**JA** あるEC事業者の開発チームは、Claude Agent SDKで開発者の生産性向上ツールを構築しています。エンジニアが、割引計算の内部関数applyDiscountの仕様を変える前に、影響を受ける箇所をすべて洗い出そうとしています。

エージェントがGrepでapplyDiscountを検索したところ、見つかった呼び出しは2か所だけでした。しかし実際には、多くの画面がlib/pricing/index.tsというラッパーモジュールを経由しており、そこではexport { applyDiscount as discountedPrice }のように別名で再エクスポートされています。

使用箇所を漏れなく追跡する方法として最も適切なものはどれですか。

**KO** 한 이커머스 사업자의 개발팀은 Claude Agent SDK로 개발자 생산성 향상 도구를 구축하고 있습니다. 엔지니어가 할인 계산 내부 함수 applyDiscount의 사양을 바꾸기 전에, 영향을 받는 위치를 모두 찾아내려고 합니다.

agent가 Grep으로 applyDiscount를 검색하자 발견된 호출은 2곳뿐이었습니다. 하지만 실제로는 많은 화면이 lib/pricing/index.ts라는 래퍼 모듈을 거치고 있고, 그 모듈에서는 export { applyDiscount as discountedPrice }처럼 다른 이름으로 다시 export하고 있습니다.

사용 위치를 빠짐없이 추적하는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: ラッパーがエクスポートする名前をすべて特定し、各名前でGrepをかける。
  - KO: 래퍼가 export하는 이름을 모두 확인하고, 각 이름으로 Grep을 실행합니다.
  - EN: Identify every name the wrapper exports, and run Grep for each of those names.
- B. JA: 画面のコンポーネントのファイルを先頭から順にReadで読み、割引の処理を探す。
  - KO: 화면 컴포넌트 파일을 처음부터 차례로 Read로 읽으며 할인 처리를 찾습니다.
  - EN: Use Read to read the screen component files from the top, looking for discount handling.
- C. JA: Globで**/pricing/**に一致するファイルを列挙し、それらをすべてReadで読んで確認する。
  - KO: Glob으로 **/pricing/**에 일치하는 파일을 나열하고, 모두 Read로 읽어 확인합니다.
  - EN: Use Glob to list the files matching **/pricing/**, then use Read to read and check all of them.
- D. JA: Grepの大文字小文字を区別しない検索でapplyDiscountを再検索し、表記ゆれも拾う。
  - KO: Grep의 대소문자 무시 검색으로 applyDiscount를 다시 검색해, 표기 차이도 잡아냅니다.
  - EN: Search for applyDiscount again with a case-insensitive Grep to catch spelling variations as well.

## CCAR-F-Udemy04-0058

**JA** ある医療機関向けシステムの開発チームは、Claude Codeで検査結果の表示形式を変換する関数を作成しています。検査機器が出力する「GLU 126 H」のような文字列を、「血糖値: 126 mg/dL（基準値より高い）」という表示に変換する必要があります。

変換ルールを文章で詳しく説明しましたが、生成された関数は、単位を付け忘れたり、低値を示す「L」を高値として扱ったりと、生成のたびに解釈がぶれています。

この変換の要件を伝える方法として最も効果的なものはどれですか。

**KO** 한 의료기관용 시스템의 개발팀은 Claude Code로 검사 결과의 표시 형식을 변환하는 함수를 작성하고 있습니다. 검사 장비가 출력하는 "GLU 126 H" 같은 문자열을 "혈당: 126 mg/dL(기준치보다 높음)"이라는 표시로 변환해야 합니다.

변환 규칙을 글로 자세히 설명했지만, 생성된 함수는 단위를 빠뜨리거나 낮은 값을 뜻하는 "L"을 높은 값으로 처리하는 등, 생성할 때마다 해석이 흔들리고 있습니다.

이 변환의 요구사항을 전달하는 방법으로 가장 효과적인 것은 무엇입니까?

- A. JA: インタビューパターンで、変換について確認したい点をClaudeに質問させる。
  - KO: 인터뷰 패턴으로, 변환에 대해 확인하고 싶은 점을 Claude가 질문하게 합니다.
  - EN: Use the interview pattern to have Claude ask questions about the points it wants to confirm regarding the conversion.
- B. JA: 変換前と変換後の組を、高値・低値・基準内を含めて2〜3個具体的に示す。
  - KO: 변환 전과 변환 후의 쌍을 높은 값·낮은 값·기준 범위 내를 포함해 2~3개 구체적으로 보여 줍니다.
  - EN: Show two or three concrete before-and-after pairs, including high, low, and within-range values.
- C. JA: 変換ルールの説明文を、項目ごとの例外も含めて今の3倍の分量に書き足す。
  - KO: 변환 규칙 설명문을 항목별 예외까지 포함해 지금의 3배 분량으로 늘립니다.
  - EN: Expand the description of the conversion rules to three times its current length, including per-item exceptions.
- D. JA: 変換の処理を担当する関数名と引数を指定し、その関数だけを書き直させる。
  - KO: 변환 처리를 맡는 함수 이름과 인수를 지정하고, 그 함수만 다시 작성하게 합니다.
  - EN: Specify the name and parameters of the function responsible for the conversion, and have Claude rewrite only that function.

> notes: 원문의 표시 예 「血糖値: 126 mg/dL（基準値より高い）」를 한국어로 옮김.

## CCAR-F-Udemy04-0059

**JA** ある建設会社の開発チームは、Claude Codeで施工管理システムのモノレポを開発しています。共通の標準はリポジトリのルートのdocs/standards/に置き、各パッケージのメンテナーが必要な標準だけを選んで、パッケージのCLAUDE.mdから@importで取り込む方針です。

見積パッケージのpackages/estimate/CLAUDE.mdに@docs/standards/estimate.mdと書きましたが、/contextで確認すると、この標準ファイルが読み込まれていません。

最も適切な修正はどれですか。

**KO** 한 건설 회사의 개발팀은 Claude Code로 시공 관리 시스템의 모노레포를 개발하고 있습니다. 공통 표준은 저장소 루트의 docs/standards/에 두고, 각 패키지의 메인테이너가 필요한 표준만 골라 패키지의 CLAUDE.md에서 @import로 가져오는 방침입니다.

견적 패키지의 packages/estimate/CLAUDE.md에 @docs/standards/estimate.md라고 적었지만, /context로 확인해 보니 이 표준 파일이 로드되지 않았습니다.

가장 적절한 수정은 무엇입니까?

- A. JA: Claude Codeを常にリポジトリのルートで起動し、パスがルート基準で解決されるようにする。
  - KO: Claude Code를 항상 저장소 루트에서 실행해, 경로가 루트 기준으로 해석되게 합니다.
  - EN: Always launch Claude Code from the repository root so that paths are resolved relative to the root.
- B. JA: @importをやめ、estimate.mdの内容をpackages/estimate/CLAUDE.mdにコピーして貼り付ける。
  - KO: @import를 그만두고, estimate.md의 내용을 packages/estimate/CLAUDE.md에 복사해 붙여 넣습니다.
  - EN: Stop using @import, and copy and paste the contents of estimate.md into packages/estimate/CLAUDE.md.
- C. JA: @importの行を~/.claude/CLAUDE.mdに移し、ユーザーレベルで読み込まれるようにする。
  - KO: @import 줄을 ~/.claude/CLAUDE.md로 옮겨, 사용자 수준에서 로드되게 합니다.
  - EN: Move the @import line to ~/.claude/CLAUDE.md so that it is loaded at the user level.
- D. JA: @importのパスを、CLAUDE.mdがある場所を基準にした相対パスに直す。
  - KO: @import 경로를 CLAUDE.md가 있는 위치를 기준으로 한 상대 경로로 고칩니다.
  - EN: Change the @import path to a relative path based on the location of the CLAUDE.md file.

## CCAR-F-Udemy04-0060

**JA** あるセキュリティ製品の販売会社の開発チームは、Claude Agent SDKでカスタマーサポート解決エージェントを構築しています。エージェントは次の3つのツールを使えますが、どの説明も短い1文だけです。

get_alert_detail（説明は「アラートを取得する」）

get_incident（説明は「インシデントを取得する」）

search_kb（説明は「検索する」）

顧客から「昨夜通知されたブルートフォースのアラートALT-20931は対応済みですか」と聞かれたのに、エージェントはsearch_kbでFAQを検索し、一般的な対処手順を答えていました。

改善策として適切なものはどれですか。（2つ選択してください。）

**KO** 한 보안 제품 판매 회사의 개발팀은 Claude Agent SDK로 고객 지원 해결 agent를 구축하고 있습니다. agent는 다음 세 도구를 쓸 수 있지만, 설명은 모두 짧은 한 문장뿐입니다.

get_alert_detail(설명은 "alert를 가져온다")

get_incident(설명은 "incident를 가져온다")

search_kb(설명은 "검색한다")

고객이 "어젯밤 통지된 brute force alert ALT-20931은 처리되었습니까?"라고 물었는데, agent는 search_kb로 FAQ를 검색해 일반적인 대처 절차를 답했습니다.

개선책으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: search_kbの説明に、FAQ用であり個別のアラートの状況確認には使わないと書く。
  - KO: search_kb의 설명에, FAQ용이며 개별 alert의 상황 확인에는 쓰지 않는다고 씁니다.
  - EN: In the description of search_kb, state that it is for the FAQ and is not to be used to check the status of an individual alert.
- B. JA: search_kbを削除し、アラートとインシデントの2つのツールだけをエージェントに渡す。
  - KO: search_kb를 삭제하고, alert와 incident용 도구 2개만 agent에게 줍니다.
  - EN: Remove search_kb and give the agent only the two tools for alerts and incidents.
- C. JA: get_alert_detailとget_incidentの説明に、IDの形式・返す項目・使い分けを書く。
  - KO: get_alert_detail과 get_incident의 설명에 ID 형식·반환 항목·구분 기준을 씁니다.
  - EN: In the descriptions of get_alert_detail and get_incident, state the ID format, the fields returned, and when to use each.
- D. JA: 「アラート」という語を含む質問ではget_alert_detailを使うよう、システムプロンプトに書く。
  - KO: "alert"라는 단어가 들어간 질문에서는 get_alert_detail을 쓰도록 system prompt에 씁니다.
  - EN: In the system prompt, instruct the agent to use get_alert_detail for any question that contains the word "alert".

## CCAR-F-Udemy05-0001

**JA** ある環境保護団体のIT部門は、寄付の受付プラットフォームのプルリクエストをClaude Codeで自動レビューしています。レビューのプロンプトには「コードのコメントが正確かどうかも確認すること」と書かれています。

コメントに関する指摘は週に約210件あり、そのうち約7割は、コードの動作とは関係のない次のような指摘で、開発者に却下されていました。

言い回しが分かりにくい

句読点が不統一

TODOが古い

一方で、コメントには「金額は税込で返す」とあるのに、実際は税抜で返していたという本当の問題は見落とされていました。

コメントのレビューの精度を高めるために適切な変更はどれですか。（2つ選択してください。）

**KO** 한 환경보호 단체의 IT 부서는 기부 접수 플랫폼의 pull request를 Claude Code로 자동 리뷰하고 있습니다. 리뷰 prompt에는 "코드 주석이 정확한지도 확인할 것"이라고 적혀 있습니다.

주석 관련 지적은 일주일에 약 210건이며, 그중 약 70%는 코드 동작과 관계없는 다음과 같은 지적이어서 개발자가 기각하고 있었습니다.

표현이 이해하기 어렵다

구두점이 통일되어 있지 않다

TODO가 오래되었다

한편, 주석에는 "금액은 세금 포함으로 반환한다"라고 되어 있는데 실제로는 세금 제외 금액을 반환하던 진짜 문제는 놓치고 있었습니다.

주석 리뷰의 정확도를 높이기 위해 적절한 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: プロンプトに「保守的に判断し、確信度の高い指摘だけを報告すること」という指示を加える。
  - KO: prompt에 "보수적으로 판단하고, 확신도가 높은 지적만 보고할 것"이라는 지시를 추가합니다.
  - EN: Add an instruction to the prompt such as "Be conservative in your judgments and report only high-confidence findings."
- B. JA: 言い回しや句読点、動作と矛盾しない古いTODOなど、報告しない対象を具体的に列挙する。
  - KO: 표현, 구두점, 동작과 모순되지 않는 오래된 TODO 등 보고하지 않을 대상을 구체적으로 나열합니다.
  - EN: Specifically list what not to report, such as wording, punctuation, and outdated TODOs that do not contradict the behavior.
- C. JA: 各指摘に確信度を出力させ、確信度が0.8以上の指摘だけをPRに投稿する。
  - KO: 각 지적에 확신도를 출력하게 하고, 확신도가 0.8 이상인 지적만 PR에 게시합니다.
  - EN: Have each finding output a confidence score, and post only findings with a confidence of 0.8 or higher to the PR.
- D. JA: プロンプトの指示を「コメントの記述がコードの動作と矛盾する場合だけ指摘する」に変える。
  - KO: prompt의 지시를 "주석 내용이 코드 동작과 모순되는 경우에만 지적한다"로 바꿉니다.
  - EN: Change the prompt's instruction to "Flag a comment only when its description contradicts the behavior of the code."

## CCAR-F-Udemy05-0002

**JA** ある鉄道会社の技術調査チームは、マルチエージェントリサーチシステムで、車両の故障報告や保守記録を分析しています。このシステムで使っているモデルは、tool_choiceの"any"と特定のツールの指定に対応しています。tool_choiceを見直す対象は、次の3か所です。

コーディネーターは、単純な質問には自分で直接答え、必要な場合だけサブエージェントを呼び出す

文書分析では、毎回、最初にextract_metadataで文書の種類と日付を取り出してから、エンリッチメント（保守台帳の情報を付け加える処理）のツールを使う

レポート生成では、結果をreport_tableかreport_textのどちらかの出力用ツールで返し、会話のテキストだけで終わらせない

tool_choiceの設定として適切なものはどれですか。（2つ選択してください。）

**KO** 한 철도 회사의 기술조사팀은 multi-agent 리서치 시스템으로 차량 고장 보고와 정비 기록을 분석하고 있습니다. 이 시스템에서 쓰는 모델은 tool_choice의 "any"와 특정 도구 지정을 지원합니다. tool_choice를 재검토할 대상은 다음 세 곳입니다.

coordinator는 단순한 질문에는 직접 답하고, 필요한 경우에만 subagent를 호출한다

문서 분석에서는 매번 먼저 extract_metadata로 문서 유형과 날짜를 추출한 뒤, enrichment(정비 대장의 정보를 덧붙이는 처리) 도구를 사용한다

리포트 생성에서는 결과를 report_table이나 report_text 중 하나의 출력용 도구로 반환하고, 대화 텍스트만으로 끝내지 않는다

tool_choice 설정으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 文書分析のすべてのターンでextract_metadataを強制指定し、エンリッチメントも同じ結果から行わせる。
  - KO: 문서 분석의 모든 turn에서 extract_metadata를 강제 지정하고, enrichment도 같은 결과로 수행하게 합니다.
  - EN: Force extract_metadata on every turn of document analysis, and have enrichment also be performed from the same result.
- B. JA: レポート生成のリクエストではtool_choiceを"any"にし、出力用ツールのいずれかを必ず呼ばせる。
  - KO: 리포트 생성 요청에서는 tool_choice를 "any"로 해서, 출력용 도구 중 하나를 반드시 호출하게 합니다.
  - EN: Set tool_choice to "any" for report generation requests so that one of the output tools is always called.
- C. JA: 文書分析の最初のリクエストだけextract_metadataを強制し、残りは後続のターンで行う。
  - KO: 문서 분석의 첫 요청에서만 extract_metadata를 강제하고, 나머지는 이후 turn에서 처리합니다.
  - EN: Force extract_metadata only on the first request of document analysis, and handle the rest in subsequent turns.
- D. JA: コーディネーターではtool_choiceを"any"にし、毎回いずれかのサブエージェントを呼ばせる。
  - KO: coordinator에서는 tool_choice를 "any"로 해서, 매번 subagent 중 하나를 호출하게 합니다.
  - EN: Set tool_choice to "any" for the coordinator so that it always calls one of the subagents every time.

## CCAR-F-Udemy05-0003

**JA** ある家電メーカーは、構造化データ抽出システムを運用しています。このシステムは、顧客から送られてくる保証書の画像から型番・製造番号・購入日・販売店名を抽出し、JSONに変換します。抽出結果は検証スクリプトで確認し、エラーがあれば、検証エラーを添えて最大3回までリトライしています。

先週の検証エラーを分析したところ、内訳は次のとおりでした。

58%は、購入日が「2026年9月14日」のような和文の表記のままで、規定のISO 8601形式に変換されていないもの

残りの42%は型番の欠落で、それらの保証書には型番の欄がなく、型番は同封の購入明細にだけ記載されていた

型番の欠落は、3回リトライしても1件も解消していません。

リトライの運用の見直し方として、最も適切なものはどれですか。

**KO** 한 가전제품 제조업체는 구조화 데이터 추출 시스템을 운영하고 있습니다. 이 시스템은 고객이 보낸 보증서 이미지에서 모델 번호·제조 번호·구입일·판매점 이름을 추출해 JSON으로 변환합니다. 추출 결과는 검증 스크립트로 확인하고, 오류가 있으면 검증 오류를 첨부해 최대 3번까지 재시도합니다.

지난주 검증 오류를 분석해 보니 내역은 다음과 같았습니다.

58%는 구입일이 "2026年9月14日" 같은 일본어 표기 그대로 남아, 규정된 ISO 8601 형식으로 변환되지 않은 것

나머지 42%는 모델 번호 누락으로, 해당 보증서에는 모델 번호 칸이 없고 모델 번호는 함께 들어 있는 구매 명세서에만 적혀 있었다

모델 번호 누락은 3번 재시도해도 단 1건도 해결되지 않았습니다.

재시도 운영을 재검토하는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: 型番の欠落だけをリトライの対象にし、購入日の形式の誤りは人間のレビューに回す。
  - KO: 모델 번호 누락만 재시도 대상으로 하고, 구입일 형식 오류는 사람의 리뷰로 넘깁니다.
  - EN: Retry only missing model numbers, and route format errors in purchase dates to human review.
- B. JA: リトライはやめ、検証エラーはすべて人間のレビューに回す。
  - KO: 재시도를 그만두고, 검증 오류는 모두 사람의 리뷰로 넘깁니다.
  - EN: Stop retrying and route all validation errors to human review.
- C. JA: 2種類のエラーのどちらについても、リトライの上限を3回から5回に増やす。
  - KO: 두 종류의 오류 모두 재시도 상한을 3번에서 5번으로 늘립니다.
  - EN: Increase the retry limit from three to five for both types of errors.
- D. JA: 形式の誤りはリトライで直し、型番の欠落は購入明細を入力に加えて解決する。
  - KO: 형식 오류는 재시도로 고치고, 모델 번호 누락은 구매 명세서를 입력에 추가해 해결합니다.
  - EN: Fix format errors with retries, and resolve missing model numbers by adding the purchase statement to the input.

> notes: 날짜 예시 「2026年9月14日」은 일본어 표기의 예이므로 원문 그대로 둠.

## CCAR-F-Udemy05-0004

**JA** ある証券会社の調査部門は、マルチエージェントリサーチシステムで、銘柄ごとの市場動向レポートを作成しています。市場データを取得するサブエージェントのMCPツールは、現在どのような失敗でも"Operation failed"という一律のエラーを返しており、コーディネーターは失敗のたびに同じ要求を3回繰り返しています。

直近1週間の失敗を調べると、次の3種類がありました。

取引所APIのタイムアウト

存在しない銘柄コードの指定

契約に含まれていない海外取引所のデータへのアクセス拒否

チームは、失敗の種類に応じてエラーレスポンスを返し分けることにしました。

返し方とコーディネーターの対応の組み合わせとして、最も適切なものはどれですか。

**KO** 한 증권사의 리서치 부서는 multi-agent 리서치 시스템으로 종목별 시장 동향 리포트를 작성하고 있습니다. 시장 데이터를 가져오는 subagent의 MCP 도구는 현재 어떤 실패든 "Operation failed"라는 똑같은 오류를 반환하고, coordinator는 실패할 때마다 같은 요청을 3번 반복합니다.

최근 1주일의 실패를 조사해 보니 다음 세 종류가 있었습니다.

거래소 API timeout

존재하지 않는 종목 코드 지정

계약에 포함되지 않은 해외 거래소 데이터에 대한 접근 거부

팀은 실패 유형에 따라 오류 응답을 다르게 반환하기로 했습니다.

반환 방식과 coordinator 대응의 조합으로 가장 적절한 것은 무엇입니까?

- A. JA: 契約外の取引所データの取得拒否を権限エラーとして返し、情報源の不足として報告させる。
  - KO: 계약 외 거래소 데이터의 조회 거부를 권한 오류로 반환하고, 정보원 부족으로 보고하게 합니다.
  - EN: Return the denial of data from an exchange outside the contract as a permission error, and have it reported as a gap in information sources.
- B. JA: 取引所APIのタイムアウトを検証エラーとして返し、入力を修正して呼び直させる。
  - KO: 거래소 API timeout을 검증 오류로 반환하고, 입력을 고쳐 다시 호출하게 합니다.
  - EN: Return the exchange API timeout as a validation error, and have it correct the input and call again.
- C. JA: 存在しない銘柄コードの指定を一時的なエラーとして返し、時間をおいてリトライさせる。
  - KO: 존재하지 않는 종목 코드 지정을 일시적 오류로 반환하고, 시간을 두고 재시도하게 합니다.
  - EN: Return the specification of a nonexistent ticker code as a transient error, and have it retry after waiting some time.
- D. JA: 契約外の取引所データの取得拒否を一時的なエラーとして返し、同じ要求を繰り返させる。
  - KO: 계약 외 거래소 데이터의 조회 거부를 일시적 오류로 반환하고, 같은 요청을 반복하게 합니다.
  - EN: Return the denial of data from an exchange outside the contract as a transient error, and have it repeat the same request.

## CCAR-F-Udemy05-0005

**JA** ある広告配信会社の開発チームは、Claude Codeで、同じユーザーへの広告の表示回数を1日3回までに制限する機能を実装しました。Claudeに「この機能を実装し、テストも書いて」と依頼したところ、42件のテストはすべて成功しました。

しかし本番では、日付が切り替わる日本時間0時の前後と、3回目の表示のときに、制限が正しく働かない不具合が見つかりました。テストを見直すと、実装の分岐をそのままなぞったものがほとんどで、日付の境界や上限ちょうどの回数を確かめるテストはありませんでした。

この機能は、1リクエストあたり5ミリ秒以内という性能要件も満たす必要があります。

この機能の改修で、Claude Codeとの反復の進め方として適切なものはどれですか。（2つ選択してください。）

**KO** 한 광고 송출 회사의 개발팀은 Claude Code로, 같은 사용자에게 광고가 노출되는 횟수를 하루 3번으로 제한하는 기능을 구현했습니다. Claude에게 "이 기능을 구현하고 테스트도 작성해 줘"라고 요청했더니 42개 테스트가 모두 통과했습니다.

그러나 프로덕션에서는 날짜가 바뀌는 일본 시간 0시 전후와 3번째 노출 때 제한이 제대로 작동하지 않는 버그가 발견되었습니다. 테스트를 다시 살펴보니 대부분 구현의 분기를 그대로 따라간 것이었고, 날짜 경계나 상한에 딱 맞는 횟수를 확인하는 테스트는 없었습니다.

이 기능은 요청 1건당 5밀리초 이내라는 성능 요구사항도 충족해야 합니다.

이 기능을 수정할 때 Claude Code와 반복 작업을 진행하는 방법으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 実装が終わった後で、カバレッジが90%を超えるまでテストを追加するようClaudeに依頼する。
  - KO: 구현이 끝난 뒤, 커버리지가 90%를 넘을 때까지 테스트를 추가하도록 Claude에게 요청합니다.
  - EN: After the implementation is finished, ask Claude to add tests until coverage exceeds 90%.
- B. JA: 実装の前に、日付の境界・上限ちょうどの回数・性能要件を確かめるテストを先に用意する。
  - KO: 구현 전에 날짜 경계·상한에 딱 맞는 횟수·성능 요구사항을 확인하는 테스트를 먼저 준비합니다.
  - EN: Before the implementation, prepare tests first that verify date boundaries, the exact count at the limit, and the performance requirement.
- C. JA: 失敗したテスト名と出力を渡して修正を繰り返させ、テスト自体は変更しないよう指示する。
  - KO: 실패한 테스트 이름과 출력을 건네 수정을 반복하게 하고, 테스트 자체는 바꾸지 말라고 지시합니다.
  - EN: Give Claude the names and output of failing tests and have it repeat fixes, instructing it not to modify the tests themselves.
- D. JA: 要件の説明文をより詳しく書き直したうえで、実装とテストを1回の依頼でまとめて作らせる。
  - KO: 요구사항 설명을 더 자세히 다시 쓴 뒤, 구현과 테스트를 한 번의 요청으로 함께 만들게 합니다.
  - EN: Rewrite the requirements description in more detail, and then have Claude create the implementation and tests together in a single request.

## CCAR-F-Udemy05-0006

**JA** ある化学メーカーの研究開発チームは、Claude Codeを使って実験データ管理システム（LIMS）と連携するコードを開発しています。リポジトリにはチームで共有する.mcp.jsonがコミットされており、LIMSのMCPサーバーのheadersには"Authorization": "Bearer ${LIMS_TOKEN}"が指定されています。

今月参加した2名の環境でだけ、次の現象が起きています。

LIMSのツール呼び出しが401エラーで失敗する

claude mcp listを実行すると、このサーバーに未設定の環境変数があるという警告が表示される

他のメンバーは、同じリポジトリで問題なく使えています。

最も可能性の高い原因と対処はどれですか。

**KO** 한 화학 제조업체의 연구개발팀은 Claude Code로 실험 데이터 관리 시스템(LIMS)과 연동하는 코드를 개발하고 있습니다. 저장소에는 팀이 공유하는 .mcp.json이 commit되어 있고, LIMS MCP server의 headers에는 "Authorization": "Bearer ${LIMS_TOKEN}"이 지정되어 있습니다.

이번 달에 합류한 2명의 환경에서만 다음 현상이 일어나고 있습니다.

LIMS 도구 호출이 401 오류로 실패한다

claude mcp list를 실행하면 이 서버에 설정되지 않은 환경 변수가 있다는 경고가 표시된다

다른 멤버는 같은 저장소에서 문제없이 사용하고 있습니다.

가장 가능성이 높은 원인과 대처는 무엇입니까?

- A. JA: headersの値では${LIMS_TOKEN}が展開されないため、トークンの値を.mcp.jsonに直接書いてコミットし直す。
  - KO: headers 값에서는 ${LIMS_TOKEN}이 확장되지 않으므로, 토큰 값을 .mcp.json에 직접 써서 다시 commit합니다.
  - EN: ${LIMS_TOKEN} is not expanded in the headers values, so write the token value directly into .mcp.json and commit it again.
- B. JA: 2名の環境にLIMS_TOKENが設定されていないため、各自の環境変数にトークンを設定してからClaude Codeを起動する。
  - KO: 2명의 환경에 LIMS_TOKEN이 설정되어 있지 않으므로, 각자 환경 변수에 토큰을 설정한 뒤 Claude Code를 실행합니다.
  - EN: LIMS_TOKEN is not set in the two members' environments, so each should set the token in their own environment variables before launching Claude Code.
- C. JA: プロジェクトスコープのサーバーは新しいメンバーには読み込まれないため、各自がclaude mcp add --scope userで登録し直す。
  - KO: project scope 서버는 새 멤버에게는 로드되지 않으므로, 각자 claude mcp add --scope user로 다시 등록합니다.
  - EN: Project-scoped servers are not loaded for new members, so each should register it again with claude mcp add --scope user.
- D. JA: 2名が.mcp.jsonの承認を拒否しているため、claude mcp reset-project-choicesを実行して承認し直す。
  - KO: 2명이 .mcp.json 승인을 거부했으므로, claude mcp reset-project-choices를 실행해 다시 승인합니다.
  - EN: The two members have rejected the approval of .mcp.json, so run claude mcp reset-project-choices and approve it again.

## CCAR-F-Udemy05-0007

**JA** ある通信事業者の開発チームは、料金計算サービスのプルリクエストごとに、Claude Codeでユニットテストを生成するCIジョブを運用しています。ジョブはclaude -pでPRの差分だけを渡し、「この変更に必要なテストを書いて」と指示しています。

生成されたテストを1か月分確認したところ、次のことが分かりました。

38%は、tests/billing/test_rating.pyなどに既にあるテストと同じシナリオだった

conftest.pyに用意済みのフィクスチャとほぼ同じヘルパーを、生成のたびに新しく定義していた

重複を減らすためのCIジョブの変更として、最も適切なものはどれですか。

**KO** 한 통신사의 개발팀은 요금 계산 서비스의 pull request마다 Claude Code로 unit test를 생성하는 CI job을 운영하고 있습니다. 이 job은 claude -p에 PR의 diff만 넘기고 “이 변경에 필요한 테스트를 작성해 줘”라고 지시합니다.

생성된 테스트를 한 달 치 확인해 보니 다음과 같은 사실이 드러났습니다.

38%는 tests/billing/test_rating.py 등에 이미 있는 테스트와 같은 시나리오였습니다

conftest.py에 이미 준비된 fixture와 거의 같은 helper를 생성할 때마다 새로 정의했습니다

중복을 줄이기 위한 CI job 변경으로 가장 적절한 것은 무엇입니까?

- A. JA: リポジトリ全体のテストファイル約2,400件を、毎回プロンプトに連結して渡す。
  - KO: 저장소 전체의 테스트 파일 약 2,400개를 매번 prompt에 이어 붙여 넘깁니다.
  - EN: Concatenate the roughly 2,400 test files of the entire repository into the prompt every time.
- B. JA: 生成後に別のジョブを走らせ、テスト名が既存のテストと一致するものだけを削除する。
  - KO: 생성 후 별도의 job을 돌려, 테스트 이름이 기존 테스트와 일치하는 것만 삭제합니다.
  - EN: Run a separate job after generation that deletes only tests whose names match existing tests.
- C. JA: 直近のカバレッジ率（全体78%）だけを渡し、80%を超えるまでテストを追加するよう指示する。
  - KO: 최근 커버리지(전체 78%)만 넘기고, 80%를 넘을 때까지 테스트를 추가하라고 지시합니다.
  - EN: Pass only the latest coverage rate (78% overall) and instruct it to add tests until it exceeds 80%.
- D. JA: 変更対象モジュールの既存テストとconftest.pyを読ませ、既存のシナリオを除かせる。
  - KO: 변경 대상 모듈의 기존 테스트와 conftest.py를 읽게 하고, 기존 시나리오는 제외하게 합니다.
  - EN: Have it read the existing tests for the changed module and conftest.py, and exclude existing scenarios.

## CCAR-F-Udemy05-0008

**JA** ある会計事務所の開発チームは、Claude Codeで申告書作成ツールのコードを生成しています。社内のMCPサーバーは、次の3つのツールを提供しています。

list_tax_forms（帳票の一覧を20件ずつ返す）

get_tax_form（1つの帳票の項目構成を返す）

create_return（申告書を作成する）

帳票は約1,800種類あり、内容が変わるのは年に1回の改正時だけです。

ログを見ると、Claudeは作業のたびに、使う帳票を探すためにlist_tax_formsとget_tax_formを平均7回呼び出しており、そのたびに作業が中断されています。

MCPサーバーの設計として適切な変更はどれですか。（2つ選択してください。）

**KO** 한 회계법인의 개발팀은 Claude Code로 신고서 작성 도구의 코드를 생성하고 있습니다. 사내 MCP server는 다음 3개의 도구를 제공합니다.

list_tax_forms(서식 목록을 20건씩 반환)

get_tax_form(서식 하나의 항목 구성을 반환)

create_return(신고서를 작성)

서식은 약 1,800종이며, 내용이 바뀌는 것은 1년에 한 번 개정될 때뿐입니다.

로그를 보면 Claude는 작업할 때마다 사용할 서식을 찾느라 list_tax_forms와 get_tax_form을 평균 7회 호출하며, 그때마다 작업이 끊깁니다.

MCP server 설계 변경으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 帳票の一覧と各帳票の項目構成を、MCPリソースとして公開する。
  - KO: 서식 목록과 각 서식의 항목 구성을 MCP resource로 공개합니다.
  - EN: Expose the list of forms and the field structure of each form as MCP resources.
- B. JA: create_returnはツールのまま残し、一覧と項目構成を返すツールは外す。
  - KO: create_return은 도구로 남기고, 목록과 항목 구성을 반환하는 도구는 제거합니다.
  - EN: Keep create_return as a tool, and remove the tools that return the list and field structures.
- C. JA: list_tax_formsが1回で返す件数を、20件から1,800件に増やす。
  - KO: list_tax_forms가 한 번에 반환하는 건수를 20건에서 1,800건으로 늘립니다.
  - EN: Increase the number of items list_tax_forms returns in one call from 20 to 1,800.
- D. JA: 帳票の一覧の全文を、list_tax_formsツールの説明に書き込む。
  - KO: 서식 목록 전문을 list_tax_forms 도구의 설명에 적어 넣습니다.
  - EN: Write the full text of the list of forms into the description of the list_tax_forms tool.

## CCAR-F-Udemy05-0009

**JA** ある人材サービス会社の開発チームは、Claude Codeで求人票のHTMLテンプレートを生成しています。デザインの規約が変わり、job_card.htmlの給与欄のクラス名をsalaryからsalary-rangeに変えることになりました。

ファイルの状況は次のとおりです。

給与欄のclass="salary"が14か所あり、すべて同じように変える

補足欄のclass="salary-note"も6か所あるが、こちらは変えない

各求人カードは同じ構造で、給与欄の前後の行も共通

Claudeに変更を依頼したところ、class="salary"をold_stringに指定したEditが「ファイル内で14か所に一致する」というエラーで失敗しました。

この変更を行う方法として、最も適切なものはどれですか。

**KO** 한 인재 서비스 회사의 개발팀은 Claude Code로 채용 공고의 HTML 템플릿을 생성하고 있습니다. 디자인 규약이 바뀌어 job_card.html의 급여 항목 클래스 이름을 salary에서 salary-range로 바꾸게 되었습니다.

파일 상황은 다음과 같습니다.

급여 항목의 class="salary"가 14곳 있으며, 모두 똑같이 바꿉니다

보충 항목의 class="salary-note"도 6곳 있지만, 이것은 바꾸지 않습니다

각 채용 카드는 구조가 같고, 급여 항목 앞뒤 줄도 공통입니다

Claude에게 변경을 요청하자, class="salary"를 old_string으로 지정한 Edit가 “파일 내 14곳과 일치합니다”라는 오류로 실패했습니다.

이 변경을 수행하는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: old_stringをsalaryだけに短くし、replace_all: trueを指定してEditを呼び出させる。
  - KO: old_string을 salary로만 줄이고, replace_all: true를 지정해 Edit를 호출하게 합니다.
  - EN: Shorten old_string to just salary, and have Edit called with replace_all: true specified.
- B. JA: old_stringをclass="salary"のまま、replace_all: trueを指定してEditを呼び出させる。
  - KO: old_string은 class="salary" 그대로 두고, replace_all: true를 지정해 Edit를 호출하게 합니다.
  - EN: Keep old_string as class="salary", and have Edit called with replace_all: true specified.
- C. JA: old_stringを前後の行まで広げ、14か所を1か所ずつ順にEditで置き換えさせる。
  - KO: old_string을 앞뒤 줄까지 넓혀, 14곳을 한 곳씩 차례로 Edit로 바꾸게 합니다.
  - EN: Extend old_string to include the surrounding lines, and have the 14 occurrences replaced one at a time with Edit in sequence.
- D. JA: Readでファイル全体を読み込み、14か所を書き換えた内容をWriteでファイル全体に書き込ませる。
  - KO: Read로 파일 전체를 읽은 뒤, 14곳을 고친 내용을 Write로 파일 전체에 쓰게 합니다.
  - EN: Have the entire file read with Read, and have the content with the 14 occurrences rewritten written to the whole file with Write.

## CCAR-F-Udemy05-0010

**JA** ある情報セキュリティ企業は、監視サービスの契約者からの問い合わせに対応するカスタマーサポート解決エージェントを運用しています。アラートの誤検知への苦情や、管理画面のアカウントのロックなど、エージェントでは解決できない案件はescalate_to_humanで人間の担当者に引き継ぎます。担当者は別のチケットシステムで作業しており、エージェントとの会話の記録にはアクセスできません。

現在の引き継ぎは「お客様がアラートについて困っています」のような一文だけです。担当者は平均9分かけて顧客に状況を聞き直しており、顧客満足度の調査では「同じ説明を2回させられた」という不満が最も多くなっています。

引き継ぎの内容として適切な改善はどれですか。（2つ選択してください。）

**KO** 한 정보보안 기업은 모니터링 서비스 가입자의 문의에 대응하는 고객 지원 해결 agent를 운영하고 있습니다. 알림 오탐에 대한 불만이나 관리 화면 계정 잠금처럼 agent가 해결할 수 없는 건은 escalate_to_human으로 사람 담당자에게 넘깁니다. 담당자는 별도의 티켓 시스템에서 일하며, agent와 나눈 대화 기록에는 접근할 수 없습니다.

현재 인계 내용은 “고객님이 알림 때문에 곤란해하고 있습니다” 같은 한 문장뿐입니다. 담당자는 평균 9분을 들여 고객에게 상황을 다시 묻고 있으며, 고객 만족도 조사에서는 “같은 설명을 두 번 해야 했다”는 불만이 가장 많습니다.

인계 내용의 개선으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: エージェントとの会話の記録を全文添付し、担当者が必要な箇所を探して読めるようにする。
  - KO: agent와 나눈 대화 기록 전문을 첨부해, 담당자가 필요한 부분을 찾아 읽을 수 있게 합니다.
  - EN: Attach the full transcript of the conversation with the agent so that representatives can find and read the parts they need.
- B. JA: エージェントが推奨する次の対応と、その判断の根拠を、引き継ぎの項目に含める。
  - KO: agent가 권장하는 다음 조치와 그 판단 근거를 인계 항목에 포함합니다.
  - EN: Include the agent's recommended next action and the rationale for that judgment as items in the handoff.
- C. JA: 顧客の感情スコアと会話のターン数を渡し、担当者が対応の優先度を決める材料にする。
  - KO: 고객의 감정 점수와 대화 turn 수를 넘겨, 담당자가 대응 우선순위를 정하는 자료로 삼게 합니다.
  - EN: Pass the customer's sentiment score and the number of conversation turns, as input for representatives to decide response priority.
- D. JA: 検証済みの顧客ID、根本原因の分析、試した対処を、構造化した項目で渡す。
  - KO: 검증된 고객 ID, 근본 원인 분석, 시도한 조치를 구조화된 항목으로 넘깁니다.
  - EN: Pass the verified customer ID, the root cause analysis, and the remedies already tried as structured fields.

## CCAR-F-Udemy05-0011

**JA** ある法律事務所の開発チームは、Claude Codeで契約書テンプレートの生成システムを開発しています。チームは調査用のカスタムサブエージェント.claude/agents/finder.mdを作り、toolsにはRead、Grep、Globだけを指定しています（Bashは含めていません）。

このサブエージェントに「契約書テンプレートのテストファイルをすべて列挙して」と依頼しました。すると、Grepで"template"という文字列をリポジトリ全体から検索し、1,900件を超える一致を読み込んだ末に、一部のファイルを見落としていました。

テストファイルは、各モジュールの中にcontract.template.spec.tsのような名前で散在しています。

このサブエージェントが使うべき方法として、最も適切なものはどれですか。

**KO** 한 법률사무소의 개발팀은 Claude Code로 계약서 템플릿 생성 시스템을 개발하고 있습니다. 팀은 조사용 custom subagent인 .claude/agents/finder.md를 만들고, tools에는 Read, Grep, Glob만 지정했습니다(Bash는 포함하지 않았습니다).

이 subagent에게 “계약서 템플릿의 테스트 파일을 모두 나열해 줘”라고 요청했습니다. 그러자 subagent는 Grep으로 "template"라는 문자열을 저장소 전체에서 검색해 1,900건이 넘는 일치 결과를 읽어 들였지만, 결국 일부 파일을 빠뜨렸습니다.

테스트 파일은 각 모듈 안에 contract.template.spec.ts 같은 이름으로 흩어져 있습니다.

이 subagent가 사용해야 할 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: Readでリポジトリのルートディレクトリを読み込み、ファイルの一覧をたどって探す。
  - KO: Read로 저장소의 루트 디렉터리를 읽고, 파일 목록을 따라가며 찾습니다.
  - EN: Use Read to load the repository's root directory, and follow the file listing to search.
- B. JA: Bashでfindコマンドを実行し、ファイル名のパターンで検索する。
  - KO: Bash로 find 명령을 실행해 파일 이름 패턴으로 검색합니다.
  - EN: Use Bash to run the find command and search by file name pattern.
- C. JA: Grepで"spec"という文字列を検索し、一致したファイルの一覧だけを出力させる。
  - KO: Grep으로 "spec"이라는 문자열을 검색하고, 일치한 파일 목록만 출력하게 합니다.
  - EN: Use Grep to search for the string "spec", and have it output only the list of matching files.
- D. JA: Globでファイル名のパターンを指定し、名前が一致するファイルを列挙する。
  - KO: Glob에 파일 이름 패턴을 지정해 이름이 일치하는 파일을 나열합니다.
  - EN: Use Glob with a file name pattern, and list the files whose names match.

## CCAR-F-Udemy05-0012

**JA** ある航空会社の整備システム部門は、Claude Codeで機体整備記録のアプリケーションを開発しています。最近、一部のメンバーがチームの規約を自分の~/.claude/CLAUDE.mdに書いていたことが分かりました。そのため、メンバーによって生成されるコードの書き方がばらついていました。チームは、ユーザーレベルのファイルに書く内容を見直すことにしました。

選択肢に挙げた指示のうち、各メンバーが自分の~/.claude/CLAUDE.mdに書くのが適切なものはどれですか。

**KO** 한 항공사의 정비 시스템 부문은 Claude Code로 항공기 정비 기록 애플리케이션을 개발하고 있습니다. 최근 일부 팀원이 팀 규약을 자신의 ~/.claude/CLAUDE.md에 적어 두었다는 사실이 드러났습니다. 그 때문에 팀원마다 생성되는 코드의 작성 방식이 제각각이었습니다. 팀은 사용자 수준 파일에 적을 내용을 재검토하기로 했습니다.

보기에 제시된 지시 중, 각 팀원이 자신의 ~/.claude/CLAUDE.md에 적기에 적절한 것은 무엇입니까?

- A. JA: コミットメッセージは、社内で定めた書式に従う。
  - KO: commit 메시지는 사내에서 정한 형식을 따릅니다.
  - EN: Commit messages follow the format defined within the company.
- B. JA: 整備記録の日時は、UTCで保存する。
  - KO: 정비 기록의 일시는 UTC로 저장합니다.
  - EN: Store maintenance record dates and times in UTC.
- C. JA: ビルドとテストはmake ciで実行する。
  - KO: 빌드와 테스트는 make ci로 실행합니다.
  - EN: Run builds and tests with make ci.
- D. JA: 説明は箇条書きで短くまとめて返してほしい。
  - KO: 설명은 글머리 기호로 짧게 정리해서 답해 주면 좋겠습니다.
  - EN: I would like explanations returned in short, concise bullet points.

## CCAR-F-Udemy05-0013

**JA** ある医療機器メーカーの開発チームは、Claude Codeを使って電子カルテとの連携モジュールを開発しています。チームは、すべてのコードに共通する次の規約を.claude/skills/coding-standards/SKILL.mdにまとめ、リポジトリにコミットしました。

患者IDや氏名をログに出力しない

日時はUTCで保存する

セッションの中で/coding-standardsを実行した場合は、規約が守られます。しかし、実行しなかったセッションで生成されたコードを調べたところ、約4割にログへの患者IDの出力が含まれていました。

最も適切な対処はどれですか。

**KO** 한 의료기기 제조사의 개발팀은 Claude Code를 사용해 전자의무기록 연동 모듈을 개발하고 있습니다. 팀은 모든 코드에 공통으로 적용되는 다음 규약을 .claude/skills/coding-standards/SKILL.md에 정리해 저장소에 commit했습니다.

환자 ID나 이름을 로그에 출력하지 않습니다

일시는 UTC로 저장합니다

session 안에서 /coding-standards를 실행한 경우에는 규약이 지켜집니다. 그러나 실행하지 않은 session에서 생성된 코드를 조사해 보니, 약 40%에 환자 ID를 로그에 출력하는 코드가 들어 있었습니다.

가장 적절한 대처는 무엇입니까?

- A. JA: SKILL.mdのフロントマターにdisable-model-invocation: trueを追加し、開発者が明示的に呼び出す運用にする。
  - KO: SKILL.md의 frontmatter에 disable-model-invocation: true를 추가해, 개발자가 명시적으로 호출하는 방식으로 운영합니다.
  - EN: Add disable-model-invocation: true to the frontmatter of SKILL.md so that developers invoke it explicitly.
- B. JA: SKILL.mdのフロントマターにcontext: forkを追加し、規約の確認を分離したサブエージェントで実行する。
  - KO: SKILL.md의 frontmatter에 context: fork를 추가해, 규약 확인을 분리된 subagent에서 실행합니다.
  - EN: Add context: fork to the frontmatter of SKILL.md so that the convention check runs in an isolated subagent.
- C. JA: すべてのコードに共通する規約はプロジェクトのCLAUDE.mdに移し、スキルには特定の作業の手順だけを残す。
  - KO: 모든 코드에 공통인 규약은 프로젝트의 CLAUDE.md로 옮기고, skill에는 특정 작업의 절차만 남깁니다.
  - EN: Move the conventions common to all code into the project's CLAUDE.md, and leave only the procedures for specific tasks in the skill.
- D. JA: セッションの開始時に必ず/coding-standardsを実行するよう、チームの開発手順書に書き加える。
  - KO: session을 시작할 때 반드시 /coding-standards를 실행하도록 팀의 개발 절차서에 추가합니다.
  - EN: Add to the team's development procedures document that /coding-standards must always be run at the start of a session.

## CCAR-F-Udemy05-0014

**JA** あるサイバーセキュリティ企業の開発チームは、Claude Agent SDKで開発者の生産性向上ツールを作っています。エージェントは40分かけて、認証モジュールの脆弱性の原因と、関係するファイルの依存関係を分析しました。その結果は、セッションの中に残っています。

チームは、この分析結果をもとに、次の2つの方針を並行して検討したいと考えています。

既存のセッション管理を改修する方針

認証の仕組みを新しいライブラリに置き換える方針

分析をやり直す時間はかけたくありません。また、2つの検討は互いに影響し合わないようにしたいと考えています。

セッションの扱いとして適切なものはどれですか。（2つ選択してください。）

**KO** 한 사이버보안 기업의 개발팀은 Claude Agent SDK로 개발자 생산성 향상 도구를 만들고 있습니다. agent는 40분에 걸쳐 인증 모듈 취약점의 원인과 관련 파일 사이의 의존 관계를 분석했습니다. 그 결과는 session 안에 남아 있습니다.

팀은 이 분석 결과를 바탕으로 다음 두 가지 방안을 병행해 검토하려고 합니다.

기존 session 관리를 개선하는 방안

인증 구조를 새 라이브러리로 교체하는 방안

분석을 다시 하는 데 시간을 들이고 싶지는 않습니다. 또한 두 검토가 서로 영향을 주지 않게 하려고 합니다.

session을 다루는 방법으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 分析済みのセッションをresumeし、fork_sessionを有効にして方針ごとに分岐させる。
  - KO: 분석을 마친 session을 resume하고, fork_session을 활성화해 방안별로 분기합니다.
  - EN: Resume the analyzed session with fork_session enabled, and branch it for each approach.
- B. JA: 方針ごとのセッションIDを記録し、後から個別に再開して検討結果を比べる。
  - KO: 방안별 session ID를 기록해 두고, 나중에 각각 재개해 검토 결과를 비교합니다.
  - EN: Record a session ID for each approach, and resume them individually later to compare the evaluation results.
- C. JA: 2つの新しいセッションを起動し、それぞれに最初から40分の分析をやり直させる。
  - KO: 새 session 2개를 시작해, 각각 처음부터 40분짜리 분석을 다시 하게 합니다.
  - EN: Start two new sessions and have each redo the 40-minute analysis from the beginning.
- D. JA: 分析済みのセッションIDを、forkせずに2つのプロセスから同時にresumeする。
  - KO: 분석을 마친 session ID를 fork하지 않고 두 프로세스에서 동시에 resume합니다.
  - EN: Resume the analyzed session ID simultaneously from two processes without forking.

## CCAR-F-Udemy05-0015

**JA** ある法律事務所の開発チームは、Claude Agent SDKを使って所内向けの開発者の生産性向上ツールを作っています。連携するMCPサーバーは、判例検索（caselaw）、契約書の文書管理（contracts）、課題管理（tickets）の3つで、ツールは合計11個です。

「判例を調べ、関連する契約書のテンプレートを特定し、結果を課題に記録する」のように、複数のサーバーにまたがる依頼が全体の約半数を占めます。ところが試作版では、依頼の種類に応じて1つのサーバーだけを接続したセッションを起動していたため、こうした依頼は毎回途中で止まっていました。

このツールの設計として適切なものはどれですか。（2つ選択してください。）

**KO** 한 법률사무소의 개발팀은 Claude Agent SDK를 사용해 사내용 개발자 생산성 향상 도구를 만들고 있습니다. 연동하는 MCP server는 판례 검색(caselaw), 계약서 문서 관리(contracts), 이슈 관리(tickets) 3개이며, 도구는 모두 11개입니다.

“판례를 조사하고, 관련 계약서 템플릿을 특정한 뒤, 결과를 이슈에 기록해 줘”처럼 여러 server에 걸친 요청이 전체의 약 절반을 차지합니다. 그런데 시제품에서는 요청 종류에 따라 server 하나만 연결한 session을 시작했기 때문에, 이런 요청은 매번 중간에 멈췄습니다.

이 도구의 설계로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 3つのMCPサーバーをmcpServersにまとめて設定し、1つのセッションで使えるようにする。
  - KO: MCP server 3개를 mcpServers에 함께 설정해 하나의 session에서 사용할 수 있게 합니다.
  - EN: Configure the three MCP servers together in mcpServers so that they can be used in a single session.
- B. JA: allowedToolsにmcp__caselaw__*などのサーバー単位のワイルドカードを指定して許可する。
  - KO: allowedTools에 mcp__caselaw__* 같은 server 단위 wildcard를 지정해 허용합니다.
  - EN: Specify server-level wildcards such as mcp__caselaw__* in allowedTools to permit them.
- C. JA: 依頼の種類を判定するルーターを作り、判定したサーバーだけを接続した新しいセッションを依頼ごとに起動する。
  - KO: 요청 종류를 판정하는 router를 만들고, 판정된 server만 연결한 새 session을 요청마다 시작합니다.
  - EN: Build a router that determines the request type, and launch a new session for each request connected only to the determined server.
- D. JA: 判例検索と文書管理の機能を統合した新しいMCPサーバーを実装し、サーバーを1つにまとめる。
  - KO: 판례 검색과 문서 관리 기능을 통합한 새 MCP server를 구현해 server를 하나로 합칩니다.
  - EN: Implement a new MCP server that integrates the case law search and document management functions, consolidating into a single server.

## CCAR-F-Udemy05-0016

**JA** ある半導体商社は、Claude Agent SDKでカスタマーサポート解決エージェントを構築し、半導体部品の返品・交換・保証に関する問い合わせに対応しています。エージェントはcreate_replacement_orderツールで代替品の発送を手配できます。選択肢に挙げた4つのルールは、現在すべてシステムプロンプトで指示しています。

ログでは、いずれのルールについても、反する応答が全体の0.2〜0.5%見つかっています。チームは、このうち違反すると法令違反や大きな金銭的損失に直結するルールだけを、Agent SDKのフックで確実に強制したいと考えています。

フックで強制すべきルールはどれですか。

**KO** 한 반도체 유통사는 Claude Agent SDK로 고객 지원 해결 agent를 구축해, 반도체 부품의 반품·교환·보증에 관한 문의에 대응하고 있습니다. agent는 create_replacement_order 도구로 대체품 발송을 처리할 수 있습니다. 보기에 제시된 4개의 규칙은 현재 모두 system prompt로 지시하고 있습니다.

로그에서는 어느 규칙이든 이를 어긴 응답이 전체의 0.2~0.5% 발견되고 있습니다. 팀은 이 가운데 위반하면 법령 위반이나 큰 금전적 손실로 직결되는 규칙만 Agent SDK의 hook으로 확실하게 강제하려고 합니다.

hook으로 강제해야 할 규칙은 무엇입니까?

- A. JA: 技術的な説明は、顧客の専門知識の程度に合わせて言い換える。
  - KO: 기술적인 설명은 고객의 전문 지식 수준에 맞춰 바꿔 말합니다.
  - EN: Rephrase technical explanations to match the customer's level of expertise.
- B. JA: 輸出管理の対象品を、許可リスト外の国へ発送しない。
  - KO: 수출 통제 대상 품목을 허용 목록에 없는 국가로 발송하지 않습니다.
  - EN: Do not ship export-controlled items to countries outside the allowlist.
- C. JA: 回答の冒頭で、顧客の会社名を挙げて呼びかける。
  - KO: 답변 첫머리에서 고객의 회사명을 부르며 인사합니다.
  - EN: Begin the response by addressing the customer by their company name.
- D. JA: 保証期間外の問い合わせには、有償修理の案内を添える。
  - KO: 보증 기간이 지난 문의에는 유상 수리 안내를 덧붙입니다.
  - EN: For inquiries outside the warranty period, include guidance on paid repair.

## CCAR-F-Udemy05-0017

**JA** ある資産運用会社の開発チームは、Claude Agent SDKを導入する前に、Messages APIを直接呼び出す独自のエージェントループで開発者の生産性向上ツールを作りました。ループの終了判定は次のとおりです。

応答にテキストのブロックが含まれていれば、「最終回答が得られた」とみなして終了する

テキストがなくツールの呼び出しだけの場合は、ツールを実行して続ける

ログを見ると、タスクの31%が、最初の応答の「まず、該当するファイルを検索します。」というテキストを返しただけで終了していました。これらの応答には、テキストのあとにGrepのtool_useブロックも含まれていました。

最も適切な修正はどれですか。

**KO** 한 자산운용사의 개발팀은 Claude Agent SDK를 도입하기 전에, Messages API를 직접 호출하는 자체 agent loop로 개발자 생산성 향상 도구를 만들었습니다. loop의 종료 판정은 다음과 같습니다.

응답에 텍스트 블록이 들어 있으면 “최종 답변을 얻었다”고 보고 종료합니다

텍스트 없이 도구 호출만 있으면 도구를 실행하고 계속합니다

로그를 보면 작업의 31%가 첫 응답의 “먼저 해당 파일을 검색하겠습니다.”라는 텍스트만 반환하고 종료되었습니다. 이 응답들에는 텍스트 뒤에 Grep의 tool_use 블록도 들어 있었습니다.

가장 적절한 수정은 무엇입니까?

- A. JA: tool_choiceを"any"にして、毎回の応答で必ずツールを呼び出させる。
  - KO: tool_choice를 "any"로 설정해 매 응답에서 반드시 도구를 호출하게 합니다.
  - EN: Set tool_choice to "any" so that a tool is always called in every response.
- B. JA: システムプロンプトに「ツールを呼び出すときは説明のテキストを書かない」と追加する。
  - KO: system prompt에 “도구를 호출할 때는 설명 텍스트를 쓰지 말 것”을 추가합니다.
  - EN: Add "Do not write explanatory text when calling tools" to the system prompt.
- C. JA: テキストの有無で判定するのをやめ、stop_reasonが"tool_use"なら続ける。
  - KO: 텍스트 유무로 판정하는 방식을 버리고, stop_reason이 "tool_use"이면 계속합니다.
  - EN: Stop judging by the presence of text, and continue if stop_reason is "tool_use".
- D. JA: 最初のリクエストだけmax_tokensを増やし、テキストの後のツール呼び出しまで出力させる。
  - KO: 첫 요청만 max_tokens를 늘려, 텍스트 뒤의 도구 호출까지 출력되게 합니다.
  - EN: Increase max_tokens only for the first request so that output extends through the tool call after the text.

## CCAR-F-Udemy05-0018

**JA** あるEC物流企業は、Claude Agent SDKで開発者の生産性向上ツールを作っています。エージェントにはRead、Write、Edit、Bash、Grep、Globの組み込みツールを与えています。

毎晩、配送業者のマスタデータからcarriers.generated.json（約1,200行）を作り直すタスクを実行しています。このファイルは自動生成専用で、人が手で編集することはありません。

ログによると、エージェントは古いファイルを読み込んだうえで、変更のある値ごとにEditを40〜80回呼び出しています。"status": "active"のように同じ文字列が何十か所にもあるため、一意に一致せずに失敗するEditがあり、今月は途中まで更新されたファイルが3回残っていました。

このタスクで使うべき方法として、最も適切なものはどれですか。

**KO** 한 이커머스 물류 기업은 Claude Agent SDK로 개발자 생산성 향상 도구를 만들고 있습니다. agent에는 Read, Write, Edit, Bash, Grep, Glob 내장 도구를 주었습니다.

매일 밤 배송업체 마스터 데이터로 carriers.generated.json(약 1,200줄)을 다시 만드는 작업을 실행합니다. 이 파일은 자동 생성 전용이며, 사람이 손으로 편집하는 일은 없습니다.

로그에 따르면 agent는 기존 파일을 읽은 뒤, 바뀐 값마다 Edit를 40~80회 호출합니다. "status": "active"처럼 같은 문자열이 수십 곳에 있어서 유일하게 일치하지 않아 실패하는 Edit가 생기고, 이번 달에는 중간까지만 갱신된 파일이 남은 일이 3번 있었습니다.

이 작업에 사용해야 할 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: 新しい内容を生成し、Writeでファイル全体を一度に書き込ませる。
  - KO: 새 내용을 생성해 Write로 파일 전체를 한 번에 쓰게 합니다.
  - EN: Have it generate the new content and write the entire file at once with Write.
- B. JA: Editの呼び出しを並列に発行させ、置き換えにかかる時間を短くする。
  - KO: Edit 호출을 병렬로 실행하게 해 교체에 걸리는 시간을 줄입니다.
  - EN: Have it issue Edit calls in parallel to shorten the time taken for replacement.
- C. JA: replace_all: trueを付けたEditで、変更のある値をまとめて置き換えさせる。
  - KO: replace_all: true를 붙인 Edit로 바뀐 값을 한꺼번에 교체하게 합니다.
  - EN: Have it replace the changed values together with Edit using replace_all: true.
- D. JA: Bashのsedで、変更のある行を正規表現でまとめて置き換えさせる。
  - KO: Bash의 sed로 바뀐 줄을 정규 표현식으로 한꺼번에 교체하게 합니다.
  - EN: Have it replace the changed lines together with a regular expression using sed via Bash.

## CCAR-F-Udemy05-0019

**JA** ある旅行会社の調査チームは、マルチエージェントリサーチシステムで「南欧方面の団体ツアーの予約が前年より35%減った理由」を調べています。コーディネーターは、調査の開始時に質問の文面から「競合の価格」「為替」「広告費」の3つのサブタスクを決めます。そして、それぞれをサブエージェントに委任し、結果を統合しています。

最初の調査で、検索サブエージェントは「主要な航空会社が、南欧への直行便を春から減便している」という情報を見つけていました。しかし、開始時に決めたサブタスクに含まれていなかったため、減便の影響は最終レポートで扱われていませんでした。

コーディネーターの計画の立て方として、適切な変更はどれですか。（2つ選択してください。）

**KO** 한 여행사의 조사팀은 multi-agent 리서치 시스템으로 “남유럽 방면 단체 여행 예약이 전년보다 35% 줄어든 이유”를 조사하고 있습니다. coordinator는 조사를 시작할 때 질문 문구를 보고 “경쟁사 가격”, “환율”, “광고비”라는 3개의 subtask를 정합니다. 그리고 각각을 subagent에게 위임하고 결과를 통합합니다.

첫 조사에서 검색 subagent는 “주요 항공사들이 봄부터 남유럽행 직항편을 감편하고 있다”는 정보를 찾아냈습니다. 그러나 시작할 때 정한 subtask에 포함되지 않았기 때문에, 감편의 영향은 최종 보고서에서 다루어지지 않았습니다.

coordinator의 계획 수립 방식으로 적절한 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: サブタスクは調査の開始時に決め、途中で見つかった情報は統合エージェントに渡して最終レポートで補足させる。
  - KO: subtask는 조사를 시작할 때 정하고, 도중에 발견된 정보는 통합 agent에게 넘겨 최종 보고서에서 보충하게 합니다.
  - EN: Determine the subtasks at the start of the investigation, and pass information found along the way to the synthesis agent to add as a supplement in the final report.
- B. JA: 最初に幅広い調査を行わせ、見つかった要因（減便など）に応じて次のサブタスクを追加する。
  - KO: 먼저 폭넓은 조사를 하게 하고, 발견된 요인(감편 등)에 따라 다음 subtask를 추가합니다.
  - EN: Have a broad investigation conducted first, and add the next subtasks according to the factors found (such as flight reductions).
- C. JA: 調査の途中で、得られた結果に応じてサブタスクの優先順位を見直し、影響の小さい調査は打ち切る。
  - KO: 조사 도중 얻은 결과에 따라 subtask의 우선순위를 재검토하고, 영향이 작은 조사는 중단합니다.
  - EN: During the investigation, review the priority of subtasks according to the results obtained, and discontinue investigations with little impact.
- D. JA: 新しい情報を見つけたサブエージェントには、自分の判断でさらにサブエージェントを起動させ、自由に調べさせる。
  - KO: 새 정보를 찾은 subagent가 스스로 판단해 subagent를 더 띄우고 자유롭게 조사하게 합니다.
  - EN: Have a subagent that finds new information launch further subagents on its own judgment and investigate freely.

## CCAR-F-Udemy05-0020

**JA** ある音楽ライブのチケット販売会社は、カスタマーサポート解決エージェントを運用しています。システムプロンプトには「『チケット』という言葉が含まれる問い合わせでは、必ずlookup_orderで注文を確認すること」という指示があります。

先月、各ツールの説明を書き直し、lookup_orderには「個別の注文の状況を確認する。払い戻しの規定などの一般的な質問にはsearch_policyを使う」と境界を明記しました。

それでも、「チケットの払い戻しの規定を教えて」のような一般的な質問の22%で、エージェントはlookup_orderを呼び、顧客に注文番号を尋ねていました。ツールの数は5つで、説明は互いに明確に区別されています。

最も可能性の高い根本原因はどれですか。

**KO** 한 음악 공연 티켓 판매 회사는 고객 지원 해결 agent를 운영하고 있습니다. system prompt에는 “‘티켓’이라는 단어가 들어간 문의에서는 반드시 lookup_order로 주문을 확인할 것”이라는 지시가 있습니다.

지난달 각 도구의 설명을 다시 쓰면서, lookup_order에는 “개별 주문의 상황을 확인한다. 환불 규정 같은 일반적인 질문에는 search_policy를 사용한다”라고 경계를 명시했습니다.

그런데도 “티켓 환불 규정을 알려 줘” 같은 일반적인 질문의 22%에서 agent는 lookup_order를 호출하고 고객에게 주문 번호를 물었습니다. 도구는 5개이며, 설명은 서로 명확히 구분되어 있습니다.

가장 가능성이 높은 근본 원인은 무엇입니까?

- A. JA: lookup_orderの説明がまだ短く、search_policyとの違いが十分に伝わっていない。
  - KO: lookup_order의 설명이 아직 짧아서 search_policy와의 차이가 충분히 전달되지 않습니다.
  - EN: The description of lookup_order is still too short and does not sufficiently convey the difference from search_policy.
- B. JA: 払い戻しの規定に関する質問を示すfew-shotの例が、システムプロンプトに不足している。
  - KO: 환불 규정에 관한 질문을 보여 주는 few-shot 예시가 system prompt에 부족합니다.
  - EN: The system prompt lacks few-shot examples showing questions about refund policies.
- C. JA: ツールの数が多すぎるため、エージェントのツール選択の信頼性が下がっている。
  - KO: 도구 수가 너무 많아 agent의 도구 선택 신뢰성이 떨어졌습니다.
  - EN: There are too many tools, which lowers the reliability of the agent's tool selection.
- D. JA: 特定のキーワードに反応するシステムプロンプトの指示が、ツールの説明より優先されている。
  - KO: 특정 키워드에 반응하는 system prompt의 지시가 도구 설명보다 우선하고 있습니다.
  - EN: An instruction in the system prompt that reacts to a specific keyword is taking precedence over the tool descriptions.

## CCAR-F-Udemy05-0021

**JA** ある銀行の開発チームは、夜間にリポジトリ全体の静的解析の結果をMessage Batches APIで要約し、翌朝モジュールごとのレビューレポートを作成するCIジョブを運用しています。ジョブの実装は次のとおりです。

各リクエストには、custom_idとして"req-0001"から順に連番を振っている

結果ファイルは上から順に読み込み、送信時のモジュール一覧の順番どおりに各モジュールへ割り当てている

先週から、「あるモジュールのレポートに、別のモジュールのクラス名や指摘が書かれている」という報告が12件寄せられています。プロンプトとモデルは変更しておらず、個々の要約は、別のモジュールの解析結果として読めば正確な内容でした。

最も可能性の高い根本原因はどれですか。

**KO** 한 은행의 개발팀은 야간에 저장소 전체의 정적 분석 결과를 Message Batches API로 요약하고, 다음 날 아침 모듈별 리뷰 보고서를 만드는 CI job을 운영하고 있습니다. job의 구현은 다음과 같습니다.

각 요청에는 custom_id로 "req-0001"부터 차례로 일련번호를 붙입니다

결과 파일은 위에서부터 차례로 읽고, 전송할 때의 모듈 목록 순서대로 각 모듈에 할당합니다

지난주부터 “어떤 모듈의 보고서에 다른 모듈의 클래스 이름이나 지적 사항이 적혀 있다”는 보고가 12건 들어왔습니다. prompt와 모델은 바꾸지 않았으며, 각 요약은 다른 모듈의 분석 결과로 읽으면 정확한 내용이었습니다.

가장 가능성이 높은 근본 원인은 무엇입니까?

- A. JA: 結果の順番は送信順と一致する保証がないのに、custom_idでなく行の順番で割り当てている。
  - KO: 결과 순서가 전송 순서와 일치한다는 보장이 없는데, custom_id가 아니라 줄 순서로 할당하고 있습니다.
  - EN: The order of results is not guaranteed to match the submission order, yet results are assigned by row order rather than by custom_id.
- B. JA: プロンプトキャッシュがバッチ内のリクエスト間で共有され、別のモジュールの内容が応答に混ざっている。
  - KO: prompt cache가 batch 안의 요청 사이에서 공유되어, 다른 모듈의 내용이 응답에 섞이고 있습니다.
  - EN: Prompt caching is shared between requests within a batch, and the contents of other modules are mixed into responses.
- C. JA: 夜間は負荷が高いため、Message Batches APIが複数のリクエストを1つにまとめて処理している。
  - KO: 야간에는 부하가 높아서 Message Batches API가 여러 요청을 하나로 묶어 처리하고 있습니다.
  - EN: Because load is high at night, the Message Batches API combines multiple requests into one for processing.
- D. JA: 入力がコンテキストの上限を超えたリクエストで、隣のリクエストの内容が入力に連結されている。
  - KO: 입력이 context 한도를 넘은 요청에서, 인접한 요청의 내용이 입력에 이어 붙고 있습니다.
  - EN: For requests whose input exceeded the context limit, the contents of the adjacent request are concatenated into the input.

## CCAR-F-Udemy05-0022

**JA** ある会計事務所の社内開発チームは、税額計算ライブラリのプルリクエストをClaude CodeのCIレビューで確認しています。現在は、1件のPRあたり平均14件の指摘をすべてインラインコメントとして投稿しています。しかし、開発者が実際に対応した指摘は約3割にとどまり、コメントが読まれなくなりつつあります。

チームは、重要な指摘だけを即時にコメントし、それ以外は週次でまとめて確認する運用に変えたいと考えています。直近3か月分の指摘については、開発者が「対応」「却下」のどちらを選んだかの記録が残っています。

指摘の振り分けの設計として、最も適切なものはどれですか。

**KO** 한 회계법인의 사내 개발팀은 세액 계산 라이브러리의 pull request를 Claude Code CI 리뷰로 확인하고 있습니다. 현재는 PR 1건당 평균 14건의 지적을 모두 인라인 코멘트로 게시합니다. 그러나 개발자가 실제로 대응한 지적은 약 30%에 그쳤고, 코멘트가 점점 읽히지 않고 있습니다.

팀은 중요한 지적만 즉시 코멘트로 달고, 나머지는 매주 모아서 확인하는 방식으로 바꾸려고 합니다. 최근 3개월 치 지적에 대해서는 개발자가 “대응”과 “기각” 중 무엇을 골랐는지 기록이 남아 있습니다.

지적을 분류하는 설계로 가장 적절한 것은 무엇입니까?

- A. JA: 指摘を生成した同じセッションで1〜10の確信度を付けさせ、7以上をそのまま即時コメントにする。
  - KO: 지적을 생성한 같은 session에서 1~10의 확신도를 매기게 하고, 7 이상은 그대로 즉시 코멘트로 답니다.
  - EN: In the same session that generated the findings, have Claude assign a confidence score from 1 to 10, and post findings scoring 7 or higher as immediate comments as-is.
- B. JA: 重大度に関係なく、1PRあたりの即時コメントを上位3件に制限し、残りを週次の確認に回す。
  - KO: 심각도와 상관없이 PR 1건당 즉시 코멘트를 상위 3건으로 제한하고, 나머지는 주간 확인으로 돌립니다.
  - EN: Regardless of severity, limit immediate comments to the top 3 per PR and defer the rest to the weekly review.
- C. JA: 別の検証パスで指摘ごとに確信度を付けさせ、過去の対応記録でキャリブレーションしたしきい値で振り分ける。
  - KO: 별도의 검증 패스에서 지적마다 확신도를 매기게 하고, 과거 대응 기록으로 calibration한 임곗값으로 분류합니다.
  - EN: Have a separate verification pass assign a confidence score to each finding, and triage using a threshold calibrated against the past records of how developers responded.
- D. JA: レビュープロンプトに「確信度の高い指摘だけを報告する」と追記し、出力をすべて即時コメントにする。
  - KO: 리뷰 prompt에 “확신도가 높은 지적만 보고할 것”을 추가하고, 출력을 모두 즉시 코멘트로 답니다.
  - EN: Add “Report only high-confidence findings” to the review prompt and post all output as immediate comments.

## CCAR-F-Udemy05-0023

**JA** ある製薬会社は、医療機関からの製品に関する問い合わせに対応するカスタマーサポート解決エージェントを運用しています。現在は、次のどちらかに当てはまったときに、アプリケーション側で自動的に人間の担当者へ転送する設計です。

感情分析のスコアが一定以下になったとき

エージェントが自己申告する確信度が0.6を下回ったとき

1か月分のログを分析すると、転送された案件の43%は、配送遅延への苦情など定型の手続きで解決できるものでした。一方で、落ち着いた口調で寄せられた適応外使用の相談や副作用の報告は、確信度0.9前後のままエージェントが自分で回答していました。

社内規程では、この2種類は必ず医薬情報部門の担当者が対応することになっています。

最も可能性の高い根本原因はどれですか。

**KO** 한 제약회사는 의료기관의 제품 문의에 대응하는 고객 지원 해결 agent를 운영하고 있습니다. 현재는 다음 중 하나에 해당하면 애플리케이션 쪽에서 자동으로 사람 담당자에게 넘기도록 설계되어 있습니다.

감정 분석 점수가 일정 수준 이하로 떨어졌을 때

agent가 스스로 보고한 확신도가 0.6 미만일 때

한 달 치 로그를 분석해 보니, 넘겨진 건의 43%는 배송 지연 불만처럼 정해진 절차로 해결할 수 있는 것이었습니다. 반면 차분한 어조로 들어온 허가 외 사용 상담이나 부작용 보고에는 agent가 확신도 0.9 안팎을 유지한 채 직접 답변했습니다.

사내 규정상 이 두 유형은 반드시 의약정보 부서 담당자가 대응해야 합니다.

가장 가능성이 높은 근본 원인은 무엇입니까?

- A. JA: 感情分析のしきい値が厳しすぎ、口調が穏やかな顧客の案件が人間の担当者に回されていない。
  - KO: 감정 분석 임곗값이 너무 엄격해서, 어조가 차분한 고객의 건이 사람 담당자에게 넘어가지 않습니다.
  - EN: The sentiment analysis threshold is too strict, so cases from customers with a calm tone are not being routed to human agents.
- B. JA: エスカレーションの条件が、エージェントのシステムプロンプトではなくアプリケーション側のコードにだけ実装されている。
  - KO: escalation 조건이 agent의 system prompt가 아니라 애플리케이션 쪽 코드에만 구현되어 있습니다.
  - EN: The escalation conditions are implemented only in application code, not in the agent's system prompt.
- C. JA: 確信度のしきい値0.6が低すぎ、確信度0.9前後の回答がエスカレーションの対象から漏れている。
  - KO: 확신도 임곗값 0.6이 너무 낮아서, 확신도 0.9 안팎의 답변이 escalation 대상에서 빠집니다.
  - EN: The confidence threshold of 0.6 is too low, so answers with confidence around 0.9 fall outside the escalation criteria.
- D. JA: エスカレーションの判断を、案件の内容と連動しない口調や自己申告の確信度に頼っている。
  - KO: escalation 판단을 건의 내용과 연동되지 않는 어조나 스스로 보고한 확신도에 의존하고 있습니다.
  - EN: The escalation decision relies on tone and self-reported confidence, which are not tied to the content of the case.

## CCAR-F-Udemy05-0024

**JA** ある県庁の政策企画課は、マルチエージェントリサーチシステムで、市区町村ごとの子育て支援策の効果を調べています。コーディネーターは検索サブエージェントに、次の手順をプロンプトで渡しています。

国の統計サイトで検索する

上位3件を要約する

結果を返す

結果を確認すると、国の統計サイトに市区町村単位のデータがないテーマでは、検索サブエージェントが「該当なし」と返して終わっていました。実際には、県や市の公開資料に必要なデータがあるケースも多くありました。また、2019年以前の古い統計を要約して返していたケースもありました。

コーディネーターから検索サブエージェントへの委任の仕方として、適切な変更はどれですか。（2つ選択してください。）

**KO** 한 현청의 정책기획과는 multi-agent 리서치 시스템으로 기초자치단체별 육아 지원책의 효과를 조사하고 있습니다. coordinator는 검색 subagent에게 다음 절차를 prompt로 전달합니다.

국가 통계 사이트에서 검색합니다

상위 3건을 요약합니다

결과를 반환합니다

결과를 확인해 보니, 국가 통계 사이트에 기초자치단체 단위 데이터가 없는 주제에서는 검색 subagent가 “해당 없음”이라고 반환하고 끝냈습니다. 실제로는 현이나 시의 공개 자료에 필요한 데이터가 있는 경우도 많았습니다. 또한 2019년 이전의 오래된 통계를 요약해 반환한 경우도 있었습니다.

coordinator가 검색 subagent에게 위임하는 방식으로 적절한 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 調査の目的と、市区町村単位・2020年以降・一次資料という品質基準を伝える。
  - KO: 조사 목적과 함께, 기초자치단체 단위·2020년 이후·1차 자료라는 품질 기준을 전달합니다.
  - EN: Communicate the purpose of the research and the quality criteria: municipality-level, 2020 or later, and primary sources.
- B. JA: コーディネーターの会話履歴をサブエージェントがすべて引き継ぐ設定を有効にし、背景を伝える。
  - KO: coordinator의 대화 기록을 subagent가 모두 이어받는 설정을 켜서 배경을 전달합니다.
  - EN: Enable the setting that lets the subagent inherit the coordinator's entire conversation history, and convey the background.
- C. JA: 使ってよい情報源の種類と範囲を条件として示し、どの順番で探すかはサブエージェントに任せる。
  - KO: 사용해도 되는 정보원의 종류와 범위를 조건으로 제시하고, 어떤 순서로 찾을지는 subagent에게 맡깁니다.
  - EN: Specify the types and scope of permitted information sources as conditions, and leave the search order to the subagent.
- D. JA: 国の統計サイトで見つからない場合は県のサイト、次に市のサイトを検索する、という手順を追加する。
  - KO: 국가 통계 사이트에서 찾지 못하면 현의 사이트, 그다음 시의 사이트를 검색하는 절차를 추가합니다.
  - EN: Add a procedure: if nothing is found on the national statistics site, search the prefectural site, then the city site.

> notes: 県庁·市区町村은 일본 행정 구역이라 '현청', '기초자치단체'로 옮김.

## CCAR-F-Udemy05-0025

**JA** ある公的研究機関の調査部門は、マルチエージェントリサーチシステムで政策テーマの調査レポートを作っています。過去30件のレポートのうち12件で、レビュー担当者から「テーマの主要な領域が抜けている」と指摘されました。

たとえば「高齢化が地域の公共交通に与える影響」というテーマでは、コーディネーターのログに、情報源の種類ごとの次の3つのサブタスクが記録されていました。

白書・統計を調べる

学術論文を調べる

報道記事を調べる

3つのサブエージェントはどれもテーマの文言をそのまま検索し、返ってきた結果の大半は路線バスの廃止に関するものでした。鉄道、デマンド交通、高齢者の移動需要といったテーマの領域は、どの指示にも現れていませんでした。

レポートの抜けを防ぐために、最も効果的な変更はどれですか。

**KO** 한 공공 연구기관의 조사 부문은 multi-agent 리서치 시스템으로 정책 주제의 조사 보고서를 만들고 있습니다. 지난 30건의 보고서 중 12건에서 리뷰 담당자로부터 “주제의 주요 영역이 빠져 있다”는 지적을 받았습니다.

예를 들어 “고령화가 지역 대중교통에 미치는 영향”이라는 주제에서는, coordinator의 로그에 정보원 종류별로 나눈 다음 3개의 subtask가 기록되어 있었습니다.

백서·통계를 조사합니다

학술 논문을 조사합니다

보도 기사를 조사합니다

3개의 subagent는 모두 주제 문구를 그대로 검색했고, 돌아온 결과의 대부분은 노선버스 폐지에 관한 것이었습니다. 철도, 수요응답형 교통, 고령자의 이동 수요 같은 주제 영역은 어느 지시에도 나타나지 않았습니다.

보고서의 누락을 막는 데 가장 효과적인 변경은 무엇입니까?

- A. JA: 各サブエージェントが取得する検索結果の件数を、10件から30件に増やす。
  - KO: 각 subagent가 가져오는 검색 결과 건수를 10건에서 30건으로 늘립니다.
  - EN: Increase the number of search results each subagent retrieves from 10 to 30.
- B. JA: テーマを構成する領域を洗い出させ、領域ごとに調査範囲を分けて割り当てさせる。
  - KO: 주제를 구성하는 영역을 도출하게 하고, 영역별로 조사 범위를 나누어 할당하게 합니다.
  - EN: Have the coordinator identify the areas that make up the theme and assign a separate research scope to each area.
- C. JA: 自治体の公開資料を調べるサブタスクを加え、情報源の種類を4つに増やす。
  - KO: 지자체 공개 자료를 조사하는 subtask를 추가해 정보원 종류를 4개로 늘립니다.
  - EN: Add a subtask that investigates municipal public materials, increasing the types of information sources to four.
- D. JA: 各情報源のサブタスクに、検索するキーワードの一覧を追加で指定する。
  - KO: 각 정보원 subtask에 검색할 키워드 목록을 추가로 지정합니다.
  - EN: Add a list of search keywords to each information-source subtask.

## CCAR-F-Udemy05-0026

**JA** ある物流会社の開発チームは、Claude Codeで配送ルート計算サービスのコードを生成しています。チームには、次のような規約があります。

距離はメートル単位の整数で扱う

外部APIの呼び出しにはタイムアウトを設定する

リード開発者のセッションでは、これらの規約が守られます。しかし、今月参加した3名のセッションや、CIで実行したClaude Codeでは守られません。

リード開発者のセッションで/contextを実行すると、Memory filesにCLAUDE.mdとCLAUDE.local.mdが表示されます。新しいメンバーのセッションではCLAUDE.mdだけが表示され、その内容はビルドとテストのコマンドだけでした。

最も可能性の高い原因はどれですか。

**KO** 한 물류회사의 개발팀은 Claude Code로 배송 경로 계산 서비스의 코드를 생성하고 있습니다. 팀에는 다음과 같은 규약이 있습니다.

거리는 미터 단위 정수로 다룹니다

외부 API 호출에는 timeout을 설정합니다

리드 개발자의 session에서는 이 규약이 지켜집니다. 그러나 이번 달에 합류한 3명의 session이나 CI에서 실행한 Claude Code에서는 지켜지지 않습니다.

리드 개발자의 session에서 /context를 실행하면 Memory files에 CLAUDE.md와 CLAUDE.local.md가 표시됩니다. 새 팀원의 session에서는 CLAUDE.md만 표시되며, 그 내용은 빌드와 테스트 명령뿐이었습니다.

가장 가능성이 높은 원인은 무엇입니까?

- A. JA: ルートのCLAUDE.mdが長すぎるため、新しい環境では途中で読み込みが打ち切られている。
  - KO: 루트의 CLAUDE.md가 너무 길어서, 새 환경에서는 읽어 들이는 도중에 잘립니다.
  - EN: The root CLAUDE.md is too long, so loading is cut off partway in new environments.
- B. JA: 新しいメンバーがサブディレクトリでClaude Codeを起動しており、ルートのCLAUDE.mdが読み込まれていない。
  - KO: 새 팀원이 하위 디렉터리에서 Claude Code를 실행해, 루트의 CLAUDE.md가 로드되지 않습니다.
  - EN: The new members launched Claude Code in a subdirectory, so the root CLAUDE.md is not loaded.
- C. JA: 新しいメンバーの~/.claude/CLAUDE.mdが空のため、プロジェクトの設定が継承されていない。
  - KO: 새 팀원의 ~/.claude/CLAUDE.md가 비어 있어서 프로젝트 설정이 상속되지 않습니다.
  - EN: The new members' ~/.claude/CLAUDE.md is empty, so the project settings are not inherited.
- D. JA: 規約がリード開発者のCLAUDE.local.mdに書かれており、Gitで共有されていない。
  - KO: 규약이 리드 개발자의 CLAUDE.local.md에 적혀 있어서 Git으로 공유되지 않습니다.
  - EN: The conventions are written in the lead developer's CLAUDE.local.md and are not shared through Git.

## CCAR-F-Udemy05-0027

**JA** ある旅行会社の開発チームは、Claude Codeで運賃ルールの判定ロジックを監査しています。ある開発者は、fare-auditという名前を付けたセッションで、運賃ルールに関係する25ファイルの分析を進めてきました。

翌日、同僚がマージしたプルリクエストによって、このうちfare_rules.py、discount.py、tax_calc.pyの3ファイルが変更されました。残りの22ファイルは変更されていません。開発者は、前日の分析をできるだけ活かして監査を続けたいと考えています。

作業を再開する方法として、最も適切なものはどれですか。

**KO** 한 여행사의 개발팀은 Claude Code로 운임 규칙 판정 로직을 감사하고 있습니다. 한 개발자는 fare-audit라는 이름을 붙인 session에서 운임 규칙과 관련된 파일 25개를 분석해 왔습니다.

다음 날 동료가 merge한 pull request로 인해 이 중 fare_rules.py, discount.py, tax_calc.py 3개 파일이 변경되었습니다. 나머지 22개 파일은 바뀌지 않았습니다. 개발자는 전날의 분석을 최대한 살려 감사를 이어 가려고 합니다.

작업을 재개하는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: 新しいセッションを開始し、25ファイルすべてを最初から読み込んで分析し直させる。
  - KO: 새 session을 시작해 파일 25개를 모두 처음부터 읽고 다시 분석하게 합니다.
  - EN: Start a new session and have Claude load and analyze all 25 files again from scratch.
- B. JA: claude --resume fare-auditで再開し、変更された3ファイルだけを再分析させる。
  - KO: claude --resume fare-audit로 재개하고, 변경된 3개 파일만 다시 분석하게 합니다.
  - EN: Resume with claude --resume fare-audit and have Claude re-analyze only the three changed files.
- C. JA: claude --resume fare-auditで再開し、変更には触れずに前回の作業の続きを進めさせる。
  - KO: claude --resume fare-audit로 재개하고, 변경에 대해서는 언급하지 않은 채 이전 작업을 이어 가게 합니다.
  - EN: Resume with claude --resume fare-audit and have Claude continue the previous work without mentioning the changes.
- D. JA: claude --continueで再開し、「最新の状態を確認してから続けて」とだけ指示する。
  - KO: claude --continue로 재개하고, “최신 상태를 확인한 뒤 계속해 줘”라고만 지시합니다.
  - EN: Resume with claude --continue and instruct only “Check the latest state and then continue.”

## CCAR-F-Udemy05-0028

**JA** ある市役所は、住民からの粗大ごみの収集予約や、各種証明書の郵送申請に対応するカスタマーサポート解決エージェントを運用しています。予約や申請を行うMCPツールは、どのような失敗でも「処理に失敗しました」という一律のエラーメッセージを返しています。

ログを見たところ、次のことが分かりました。

「収集の申し込みは、収集日の3日前の17時まで」という規則に反した予約で、エージェントが同じ予約を4回繰り返して失敗していた

存在しない住所コードを指定した申請では、住民に「システム障害が発生しています」と案内していた

ツールのエラーレスポンスの改善として適切なものはどれですか。（2つ選択してください。）

**KO** 한 시청은 주민의 대형 폐기물 수거 예약과 각종 증명서 우편 신청을 처리하는 고객 지원 해결 agent를 운영하고 있습니다. 예약과 신청을 처리하는 MCP 도구는 어떤 실패든 “처리에 실패했습니다”라는 동일한 오류 메시지를 반환합니다.

로그를 보니 다음과 같은 사실이 드러났습니다.

“수거 신청은 수거일 3일 전 17시까지”라는 규칙을 어긴 예약에서, agent가 같은 예약을 4번 반복해 실패했습니다

존재하지 않는 주소 코드를 지정한 신청에서는 주민에게 “시스템 장애가 발생했습니다”라고 안내했습니다

도구의 오류 응답 개선으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: エラーメッセージは一律のまま、ツールが失敗したら人間の担当者にエスカレーションさせる。
  - KO: 오류 메시지는 동일한 형태로 두고, 도구가 실패하면 사람 담당자에게 escalation하게 합니다.
  - EN: Keep the uniform error message and have the agent escalate to a human agent whenever a tool fails.
- B. JA: エラーメッセージは一律のまま、エージェント側でどの失敗も3回まで間隔をあけてリトライさせる。
  - KO: 오류 메시지는 동일한 형태로 두고, agent 쪽에서 어떤 실패든 간격을 두고 3번까지 재시도하게 합니다.
  - EN: Keep the uniform error message and have the agent retry any failure up to three times at intervals.
- C. JA: 失敗の種類と、リトライで解決できるかどうかを、構造化されたメタデータとして返す。
  - KO: 실패의 종류와 재시도로 해결할 수 있는지를 구조화된 metadata로 반환합니다.
  - EN: Return the type of failure and whether it can be resolved by retrying as structured metadata.
- D. JA: 規則に反した失敗では、住民にそのまま伝えられる分かりやすい説明を含めて返す。
  - KO: 규칙 위반으로 인한 실패에는 주민에게 그대로 전할 수 있는 알기 쉬운 설명을 포함해 반환합니다.
  - EN: For failures caused by rule violations, return a clear explanation that can be relayed to the resident as is.

## CCAR-F-Udemy05-0029

**JA** あるSaaS企業の開発チームは、Claude Codeでモノレポのコード生成を行っています。GraphQLのスキーマとresolverの規約を.claude/rules/graphql.mdにまとめ、フロントマターにpaths: ["**/*.{graphql,ts}"]を指定しました。

規約を適用したいのは、次のファイルだけです。

リポジトリ内のすべての.graphqlファイル

名前が.resolver.tsで終わるファイル

対象のファイルは、packages/billing/src/graphql/やpackages/admin/src/resolvers/のように、各パッケージの深い階層にあります。

ところが、GraphQLと関係のない通常のTypeScriptファイルを編集する作業でも、この規約が毎回読み込まれていました。

pathsの指定として正しいものはどれですか。（2つ選択してください。）

**KO** 한 SaaS 기업의 개발팀은 Claude Code로 monorepo의 코드를 생성하고 있습니다. GraphQL schema와 resolver 규약을 .claude/rules/graphql.md에 정리하고, frontmatter에 paths: ["**/*.{graphql,ts}"]를 지정했습니다.

규약을 적용하려는 대상은 다음 파일뿐입니다.

저장소 안의 모든 .graphql 파일

이름이 .resolver.ts로 끝나는 파일

대상 파일은 packages/billing/src/graphql/이나 packages/admin/src/resolvers/처럼 각 패키지의 깊은 계층에 있습니다.

그런데 GraphQL과 관계없는 일반 TypeScript 파일을 편집하는 작업에서도 이 규약이 매번 로드되었습니다.

paths 지정으로 올바른 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: paths: ["**/*.graphql", "**/*.ts"]を指定する。
  - KO: paths: ["**/*.graphql", "**/*.ts"]를 지정합니다.
  - EN: Specify paths: ["**/*.graphql", "**/*.ts"].
- B. JA: paths: "**/*.graphql,**/*.resolver.ts"を指定する。
  - KO: paths: "**/*.graphql,**/*.resolver.ts"를 지정합니다.
  - EN: Specify paths: "**/*.graphql,**/*.resolver.ts".
- C. JA: paths: ["packages/*/*.graphql", "packages/*/*.resolver.ts"]を指定する。
  - KO: paths: ["packages/*/*.graphql", "packages/*/*.resolver.ts"]를 지정합니다.
  - EN: Specify paths: ["packages/*/*.graphql", "packages/*/*.resolver.ts"].
- D. JA: paths: ["**/*.graphql", "**/*.resolver.ts"]を指定する。
  - KO: paths: ["**/*.graphql", "**/*.resolver.ts"]를 지정합니다.
  - EN: Specify paths: ["**/*.graphql", "**/*.resolver.ts"].

## CCAR-F-Udemy05-0030

**JA** ある出版社の開発チームは、Claude Codeを使って記事配信システム（CMS）の改修を進めています。ある開発者は、記事の公開からキャッシュの削除までの処理の流れを、1つのセッションで3時間以上かけて調べてきました。セッションの序盤には、「キャッシュ層のコードは別チームの担当なので変更しない」とClaudeに伝えています。

ところが後半になると、Claudeに次の変化が現れました。

前半に調べ終えたArticleRepository.tsなどのファイルを、Grepで探し直すようになった

CacheInvalidatorを書き換える修正案まで出すようになった

/contextで確認すると、コンテキストの大半を会話履歴が占めており、その多くはGrepとReadの長い出力でした。CLAUDE.mdはこの間、変更していません。

最も可能性の高い原因はどれですか。

**KO** 한 출판사의 개발팀은 Claude Code를 사용해 기사 배포 시스템(CMS)을 개선하고 있습니다. 한 개발자는 기사 게시부터 캐시 삭제까지의 처리 흐름을 하나의 session에서 3시간 넘게 조사해 왔습니다. session 초반에는 Claude에게 “캐시 계층 코드는 다른 팀 담당이니 변경하지 않는다”고 전달했습니다.

그런데 후반이 되자 Claude에게 다음과 같은 변화가 나타났습니다.

전반에 조사를 끝낸 ArticleRepository.ts 등의 파일을 Grep으로 다시 찾기 시작했습니다

CacheInvalidator를 고치는 수정안까지 내놓기 시작했습니다

/context로 확인하니 context의 대부분을 대화 기록이 차지하고 있었으며, 그중 상당 부분은 Grep과 Read의 긴 출력이었습니다. CLAUDE.md는 그동안 변경하지 않았습니다.

가장 가능성이 높은 원인은 무엇입니까?

- A. JA: 大量のツール出力でコンテキストが埋まり、前半の調査結果や指示を参照しにくくなっている。
  - KO: 대량의 도구 출력으로 context가 가득 차, 전반의 조사 결과나 지시를 참조하기 어려워졌습니다.
  - EN: The context is filled with a large amount of tool output, making it hard to refer to earlier investigation results and instructions.
- B. JA: 調査対象のファイルが途中で他のメンバーに変更され、Claudeが改めて読み直している。
  - KO: 조사 대상 파일이 도중에 다른 팀원에 의해 변경되어, Claude가 다시 읽고 있습니다.
  - EN: The files under investigation were changed by another member partway through, and Claude is re-reading them.
- C. JA: 自動の圧縮でCLAUDE.mdが失われ、プロジェクトの規約を参照できなくなっている。
  - KO: 자동 compaction으로 CLAUDE.md가 사라져, 프로젝트 규약을 참조할 수 없게 되었습니다.
  - EN: Automatic compaction lost CLAUDE.md, so Claude can no longer refer to the project conventions.
- D. JA: CLAUDE.mdにキャッシュ層の変更を促す古い記述が残り、後半はそれが優先されている。
  - KO: CLAUDE.md에 캐시 계층 변경을 권하는 오래된 내용이 남아 있어, 후반에는 그것이 우선되고 있습니다.
  - EN: An outdated entry in CLAUDE.md encouraging changes to the cache layer remains, and it is being prioritized in the later part of the session.

## CCAR-F-Udemy05-0031

**JA** ある大学の入試課は、編入学の志願者から提出される成績証明書から、科目名・単位数・成績・卒業見込み日を抽出する構造化データ抽出システムを導入しようとしています。2,000件の検証データで測った全体の精度は97%で、目標の95%を上回りました。チームは、確信度0.9以上の抽出について、人間による確認をやめることを検討しています。

提出される成績証明書には、国内の大学のPDF、海外の大学の英文の書類、手書きの補足が入ったスキャン画像など、さまざまな種類があります。

人間による確認を減らす前に行うべきこととして、適切なものはどれですか。（2つ選択してください。）

**KO** 한 대학의 입시과는 편입학 지원자가 제출하는 성적증명서에서 과목명·학점·성적·졸업 예정일을 추출하는 구조화 데이터 추출 시스템을 도입하려 하고 있습니다. 검증 데이터 2,000건으로 측정한 전체 정확도는 97%로, 목표인 95%를 넘었습니다. 팀은 확신도 0.9 이상인 추출 결과에 대해 사람의 확인을 없애는 방안을 검토하고 있습니다.

제출되는 성적증명서에는 국내 대학의 PDF, 해외 대학의 영문 서류, 손글씨 보충이 들어간 스캔 이미지 등 다양한 종류가 있습니다.

사람의 확인을 줄이기 전에 해야 할 일로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 全体の精度が目標を上回ったので、確信度0.9以上の抽出は一律に確認をやめる。
  - KO: 전체 정확도가 목표를 넘었으므로, 확신도 0.9 이상인 추출은 일괄적으로 확인을 없앱니다.
  - EN: Since overall accuracy exceeded the target, uniformly end review for all extractions with confidence 0.9 or higher.
- B. JA: 文書の種類（国内・海外・手書きの補足あり）とフィールドごとに、精度を分けて測る。
  - KO: 문서 종류(국내·해외·손글씨 보충 있음)와 필드별로 정확도를 나누어 측정합니다.
  - EN: Measure accuracy separately by document type (domestic, overseas, with handwritten annotations) and by field.
- C. JA: 検証データから無作為に50件を選んで再確認し、95%以上なら全体の確認をやめる。
  - KO: 검증 데이터에서 무작위로 50건을 골라 다시 확인하고, 95% 이상이면 전체 확인을 없앱니다.
  - EN: Randomly select 50 items from the validation data and recheck them; if accuracy is 95% or higher, end review across the board.
- D. JA: 目標の95%を満たした区分だけで人間による確認を減らし、他の区分では確認を続ける。
  - KO: 목표 95%를 충족한 구분에서만 사람의 확인을 줄이고, 다른 구분에서는 확인을 계속합니다.
  - EN: Reduce human review only for segments that meet the 95% target, and continue review for the other segments.

## CCAR-F-Udemy05-0032

**JA** ある消費財メーカーの開発チームは、プルリクエストをClaude Codeでレビューし、指摘をJSONで出力させるCIジョブを運用しています。出力は検証スクリプトで確認し、次の場合は失敗とみなします。

JSONとして読めない

指摘の行番号がPRの差分の範囲外にある

失敗したときは、「前回の出力は不正でした。やり直してください」と指示して、最大5回まで再実行しています。

直近1か月では実行の23%が検証に失敗しており、その内訳は、JSONの構文エラーが60%、差分の範囲外の行番号が40%でした。5回の再実行でも失敗するケースが続いています。

検証とリトライの仕組みとして適切な改善はどれですか。（2つ選択してください。）

**KO** 한 소비재 제조사의 개발팀은 pull request를 Claude Code로 리뷰하고 지적 사항을 JSON으로 출력하게 하는 CI job을 운영하고 있습니다. 출력은 검증 스크립트로 확인하며, 다음 경우에는 실패로 간주합니다.

JSON으로 파싱할 수 없습니다

지적 사항의 줄 번호가 PR diff 범위 밖에 있습니다

실패하면 “이전 출력은 올바르지 않았습니다. 다시 해 주세요”라고 지시해 최대 5번까지 다시 실행합니다.

최근 한 달 동안 실행의 23%가 검증에 실패했으며, 그 내역은 JSON 구문 오류가 60%, diff 범위 밖의 줄 번호가 40%였습니다. 5번 다시 실행해도 실패하는 경우가 계속 나오고 있습니다.

검증과 재시도 구조로 적절한 개선은 무엇입니까? (2개를 선택하십시오.)

- A. JA: リトライのたびに新しい実行を始め、「前回は失敗しました」とだけ伝えて同じ差分を渡す。
  - KO: 재시도할 때마다 새 실행을 시작하고, “이전에는 실패했습니다”라고만 전한 뒤 같은 diff를 넘깁니다.
  - EN: On each retry, start a new run and tell Claude only “The previous attempt failed,” passing the same diff.
- B. JA: 失敗した出力と元の差分をリトライに含め、どの指摘のどの値がなぜ不正かを具体的に示す。
  - KO: 실패한 출력과 원래 diff를 재시도에 포함하고, 어느 지적의 어떤 값이 왜 잘못되었는지 구체적으로 알려 줍니다.
  - EN: Include the failed output and the original diff in the retry, and specify concretely which value in which finding is invalid and why.
- C. JA: リトライの上限を5回から10回に増やし、成功するまで同じ指示で実行させる。
  - KO: 재시도 상한을 5번에서 10번으로 늘리고, 성공할 때까지 같은 지시로 실행하게 합니다.
  - EN: Raise the retry limit from 5 to 10 and run with the same instruction until it succeeds.
- D. JA: --json-schemaで出力のスキーマを固定し、JSONの構文エラーをなくす。
  - KO: --json-schema로 출력 schema를 고정해 JSON 구문 오류를 없앱니다.
  - EN: Fix the output schema with --json-schema to eliminate JSON syntax errors.

## CCAR-F-Udemy05-0033

**JA** ある海運会社は、コンテナ輸送の問い合わせに対応するカスタマーサポート解決エージェントを構築しています。MCPツールlookup_bookingは、予約番号の形式が誤っている場合や予約が取り消し済みの場合に例外を送出し、MCPサーバーはそれをJSON-RPCのエラーレスポンスとして返しています。

ログを確認すると、こうしたケースの72%で、エージェントは「システム障害のため確認できません」と回答して会話を終えていました。予約番号を聞き直したり、取り消し済みであることを顧客に伝えたりできたケースはほとんどありません。

lookup_bookingの失敗の返し方として、最も適切なものはどれですか。

**KO** 한 해운회사는 컨테이너 운송 문의에 대응하는 고객 지원 해결 agent를 구축하고 있습니다. MCP 도구 lookup_booking은 예약 번호 형식이 잘못되었거나 예약이 이미 취소된 경우 예외를 던지고, MCP server는 이를 JSON-RPC 오류 응답으로 반환합니다.

로그를 확인해 보니 이런 경우의 72%에서 agent는 “시스템 장애로 확인할 수 없습니다”라고 답하고 대화를 끝냈습니다. 예약 번호를 다시 묻거나, 이미 취소된 예약이라고 고객에게 알린 경우는 거의 없습니다.

lookup_booking의 실패를 반환하는 방식으로 가장 적절한 것은 무엇입니까?

- A. JA: 例外を送出する前にサーバー内で3回リトライし、それでも失敗した場合だけエラーを返す。
  - KO: 예외를 던지기 전에 server 안에서 3번 재시도하고, 그래도 실패한 경우에만 오류를 반환합니다.
  - EN: Retry three times within the server before throwing an exception, and return an error only if it still fails.
- B. JA: 失敗をツールの結果としてisError: trueで返し、contentに失敗の理由と次に取れる対応を書く。
  - KO: 실패를 도구 결과로 isError: true와 함께 반환하고, content에 실패 이유와 다음에 취할 수 있는 조치를 적습니다.
  - EN: Return the failure as a tool result with isError: true, and write the reason for the failure and possible next actions in content.
- C. JA: 失敗時もisErrorはfalseのままにし、contentに「エラー: 予約番号が無効です」と書いて返す。
  - KO: 실패해도 isError는 false로 두고, content에 “오류: 예약 번호가 유효하지 않습니다”라고 적어 반환합니다.
  - EN: Keep isError as false even on failure, and return content that says “エラー: 予約番号が無効です”.
- D. JA: JSON-RPCのエラーレスポンスのまま、messageに失敗の理由を詳しく書いて返す。
  - KO: JSON-RPC 오류 응답은 그대로 두고, message에 실패 이유를 자세히 적어 반환합니다.
  - EN: Return it as a JSON-RPC error response as is, with a detailed reason for the failure in message.

## CCAR-F-Udemy05-0034

**JA** ある損害保険会社の開発チームは、Claude Codeで保険金請求システムを開発しています。Aさんは、請求データの検証手順をまとめた/claim-validateというカスタムスラッシュコマンドを作り、チームの全員に使ってもらうつもりでした。

Aさんの環境ではこのコマンドを使えますが、他の5名がリポジトリを最新の状態にしても、コマンドの一覧に/claim-validateが表示されません。リポジトリの.claude/ディレクトリにはsettings.jsonだけがあり、commands/やskills/はありません。

最も可能性の高い原因と対処はどれですか。

**KO** 한 손해보험사의 개발팀은 Claude Code로 보험금 청구 시스템을 개발하고 있습니다. A씨는 청구 데이터 검증 절차를 정리한 /claim-validate라는 custom slash command를 만들어 팀 전원이 쓰게 할 생각이었습니다.

A씨의 환경에서는 이 명령을 쓸 수 있지만, 다른 5명은 저장소를 최신 상태로 갱신해도 명령 목록에 /claim-validate가 표시되지 않습니다. 저장소의 .claude/ 디렉터리에는 settings.json만 있고 commands/나 skills/는 없습니다.

가장 가능성이 높은 원인과 대처는 무엇입니까?

- A. JA: コマンドが個人用の場所にあるため、.claude/commands/に移してコミットする。
  - KO: 명령이 개인용 위치에 있으므로 .claude/commands/로 옮겨 commit합니다.
  - EN: The command is in a personal location, so move it to .claude/commands/ and commit it.
- B. JA: 他のメンバーのClaude Codeのバージョンが古いため、全員がアップデートする。
  - KO: 다른 팀원의 Claude Code 버전이 오래되었으므로 모두 업데이트합니다.
  - EN: The other members' Claude Code versions are outdated, so everyone should update.
- C. JA: コマンドのファイルにフロントマターがないため、descriptionを追加してから読み込み直す。
  - KO: 명령 파일에 frontmatter가 없으므로 description을 추가한 뒤 다시 로드합니다.
  - EN: The command file has no frontmatter, so add description and reload.
- D. JA: コマンドの名前が既存のスキルと重複しているため、別の名前にして作り直す。
  - KO: 명령 이름이 기존 skill과 겹치므로 다른 이름으로 다시 만듭니다.
  - EN: The command name duplicates an existing skill, so recreate it with a different name.

## CCAR-F-Udemy05-0035

**JA** ある農業資材の通販会社は、肥料や農機部品の注文に関する問い合わせに対応するカスタマーサポート解決エージェントを運用しています。問い合わせの約21%には、「先週の肥料がまだ届かない。請求も二重になっている気がする。あと、注文したトラクターの部品が自分の機種に合うか知りたい」のように、複数の用件が含まれています。

ログによると、こうした問い合わせでは、エージェントが最初の用件だけを解決して会話を終えることが多く、顧客からの再問い合わせが相次いでいます。初回解決率は61%で、目標の80%を大きく下回っています。

最も効果的な改善策はどれですか。

**KO** 한 농업 자재 통신판매 회사는 비료와 농기계 부품 주문에 관한 문의에 대응하는 고객 지원 해결 agent를 운영하고 있습니다. 문의의 약 21%에는 “지난주 주문한 비료가 아직 안 왔어요. 요금도 두 번 청구된 것 같아요. 그리고 주문한 트랙터 부품이 제 기종에 맞는지 알고 싶어요”처럼 여러 용건이 들어 있습니다.

로그에 따르면 이런 문의에서 agent는 첫 번째 용건만 해결하고 대화를 끝내는 경우가 많아, 고객의 재문의가 잇따르고 있습니다. 첫 문의 해결률은 61%로, 목표인 80%에 크게 못 미칩니다.

가장 효과적인 개선책은 무엇입니까?

- A. JA: 用件を1つずつ順番に処理し、用件ごとに新しい会話を開始してget_customerから本人確認をやり直す。
  - KO: 용건을 하나씩 차례로 처리하되, 용건마다 새 대화를 시작해 get_customer부터 본인 확인을 다시 합니다.
  - EN: Process requests one at a time in order, starting a new conversation for each request and redoing identity verification from get_customer.
- B. JA: 問い合わせを個別の用件に分解し、確認済みの顧客情報を共有して各用件を並列に調べ、1つの回答にまとめる。
  - KO: 문의를 개별 용건으로 분해하고, 확인된 고객 정보를 공유해 각 용건을 병렬로 조사한 뒤 하나의 답변으로 정리합니다.
  - EN: Decompose the inquiry into separate requests, share the verified customer information, investigate each request in parallel, and combine the results into a single response.
- C. JA: 複数の用件を含む問い合わせには、用件ごとに別の問い合わせとして送り直すよう顧客に依頼する。
  - KO: 여러 용건이 담긴 문의에는 용건마다 별도의 문의로 다시 보내 달라고 고객에게 요청합니다.
  - EN: For inquiries containing multiple requests, ask the customer to resubmit each request as a separate inquiry.
- D. JA: 複数の用件を含む問い合わせを検出したら、内容を確認せずに人間の担当者へエスカレーションする。
  - KO: 여러 용건이 담긴 문의를 감지하면 내용을 확인하지 않고 사람 담당자에게 escalation합니다.
  - EN: When an inquiry containing multiple requests is detected, escalate to a human agent without checking the content.

## CCAR-F-Udemy05-0036

**JA** ある自動車部品メーカーの技術調査チームは、Claude Agent SDKでマルチエージェントリサーチシステムを構築しています。コーディネーターは、ウェブ検索、文書分析、統合、レポート生成の4つのサブエージェントに作業を委任します。コーディネーターのプロンプトには「すべての質問で、4つのサブエージェントを順番に呼び出すこと」と書かれています。

利用状況を調べたところ、次のことが分かりました。

質問の約6割は「ある規格の発効日」のような単一の事実確認だが、こうした質問でも4つのサブエージェントをすべて通るため、回答までに平均4分、1件あたり0.9ドルかかっている

文書分析サブエージェントは、添付文書のない質問でも毎回起動され、「分析対象なし」と返している

コーディネーターの設計として適切な変更はどれですか。（2つ選択してください。）

**KO** 한 자동차 부품 제조사의 기술 조사팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. coordinator는 웹 검색, 문서 분석, 통합, 보고서 생성의 4개 subagent에게 작업을 위임합니다. coordinator의 prompt에는 “모든 질문에서 4개의 subagent를 차례로 호출할 것”이라고 적혀 있습니다.

이용 현황을 조사해 보니 다음과 같은 사실이 드러났습니다.

질문의 약 60%는 “어떤 규격의 발효일”처럼 단일 사실 확인인데, 이런 질문도 4개 subagent를 모두 거치기 때문에 답변까지 평균 4분, 1건당 0.9달러가 듭니다

문서 분석 subagent는 첨부 문서가 없는 질문에서도 매번 실행되어 “분석 대상 없음”을 반환합니다

coordinator 설계로 적절한 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 4つのサブエージェントを順番に呼ぶのをやめ、毎回4つとも並列に起動する。
  - KO: 4개 subagent를 차례로 호출하는 방식을 버리고, 매번 4개를 모두 병렬로 실행합니다.
  - EN: Stop calling the four subagents in order and instead launch all four in parallel every time.
- B. JA: コーディネーターの前段に過去の質問で学習させた分類モデルを置き、呼び出すサブエージェントを予測させる。
  - KO: coordinator 앞단에 과거 질문으로 학습시킨 분류 모델을 두어, 호출할 subagent를 예측하게 합니다.
  - EN: Place a classification model trained on past questions in front of the coordinator and have it predict which subagents to call.
- C. JA: 各サブエージェントの説明に、担当する作業と、どのような質問のときに呼び出すべきかを明記する。
  - KO: 각 subagent의 설명에 담당 작업과 어떤 질문일 때 호출해야 하는지를 명시합니다.
  - EN: State in each subagent's description the work it handles and what kinds of questions it should be called for.
- D. JA: 固定の呼び出し順の指示をやめ、質問の要件を分析して必要なサブエージェントだけを呼び出させる。
  - KO: 고정된 호출 순서 지시를 없애고, 질문의 요구 사항을 분석해 필요한 subagent만 호출하게 합니다.
  - EN: Drop the fixed call-order instruction and have the coordinator analyze the question's requirements and call only the necessary subagents.

## CCAR-F-Udemy05-0037

**JA** ある大学の学生支援課は、奨学金の申請書類から申請区分・世帯年収・在籍状況を抽出する構造化データ抽出システムを運用しています。抽出ツールのJSONスキーマでは、申請区分を"給付型"・"貸与型"・"授業料減免"の3つの値を持つenumとして定義しています。

今年度から、留学支援や災害特例のような新しい区分の申請が届くようになりました。抽出結果を監査すると、こうした申請の多くが"授業料減免"に分類されており、全体の約9%が誤った区分のまま下流の審査システムに登録されていました。

新しい区分は、今後も年に数種類ずつ増える見込みです。

スキーマの設計と運用として適切な変更はどれですか。（2つ選択してください。）

**KO** 한 대학의 학생지원과는 장학금 신청 서류에서 신청 구분·가구 연 소득·재학 상태를 추출하는 구조화 데이터 추출 시스템을 운영하고 있습니다. 추출 도구의 JSON schema에서는 신청 구분을 "지급형"·"대여형"·"수업료 감면" 3개 값을 갖는 enum으로 정의하고 있습니다.

올해부터 유학 지원이나 재해 특례 같은 새로운 구분의 신청이 들어오기 시작했습니다. 추출 결과를 감사해 보니 이런 신청 중 상당수가 "수업료 감면"으로 분류되었고, 전체의 약 9%가 잘못된 구분인 채로 하위 심사 시스템에 등록되어 있었습니다.

새로운 구분은 앞으로도 해마다 몇 종류씩 늘어날 전망입니다.

schema 설계와 운영으로 적절한 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: enumに"other"を追加し、内容を記録する詳細の文字列フィールドを設ける。
  - KO: enum에 "other"를 추가하고, 내용을 기록하는 상세 문자열 필드를 둡니다.
  - EN: Add “other” to the enum and provide a detail string field to record the content.
- B. JA: 当てはまる区分がなかった申請を定期的に集計し、件数の多いものはenumの正式な値に加える。
  - KO: 맞는 구분이 없었던 신청을 정기적으로 집계해, 건수가 많은 것은 enum의 정식 값으로 추가합니다.
  - EN: Periodically tally applications for which no category fit, and add frequently occurring ones to the enum as official values.
- C. JA: 申請区分のenumをやめて自由記述の文字列にし、書類に書かれた区分名をそのまま返させる。
  - KO: 신청 구분 enum을 없애고 자유 기술 문자열로 바꿔, 서류에 적힌 구분 이름을 그대로 반환하게 합니다.
  - EN: Drop the application category enum, make it a free-text string, and have Claude return the category name exactly as written in the document.
- D. JA: プロンプトに「3つの区分のうち最も近いものを必ず選ぶ」と書き足し、分類のぶれを減らす。
  - KO: prompt에 “3개 구분 중 가장 가까운 것을 반드시 고를 것”을 추가해 분류 편차를 줄입니다.
  - EN: Add “Always choose the closest of the three categories” to the prompt to reduce classification variability.

> notes: enum 값(給付型·貸与型·授業料減免)도 한국어로 옮김.

## CCAR-F-Udemy05-0038

**JA** あるゲーム会社は、Claude Agent SDKで開発者の生産性向上ツールを作り、クラッシュ報告の調査に使っています。エージェントは3つのMCPサーバーからデータを取得し、各サーバーの応答の形式は次のとおりです。

クラッシュ収集サービスは、時刻をUnixミリ秒で返す

ビルドサーバーは、時刻を+09:00付きのISO 8601で返す

マッチングサーバーは、ステータスを3や7のような数値のコードで返す

3つとも外部のサービスで、応答の形式は変更できません。

ログによると、調査の11%で、エージェントが「ビルドの配布後にクラッシュが増えた」のように、イベントの前後関係を誤って判断していました。システムプロンプトには時刻の形式を説明する文章がありますが、誤りは減っていません。

最も信頼性の高い対策はどれですか。

**KO** 한 게임 회사는 Claude Agent SDK로 개발자 생산성 향상 도구를 만들어 크래시 보고 조사에 사용하고 있습니다. agent는 3개의 MCP server에서 데이터를 가져오며, 각 server의 응답 형식은 다음과 같습니다.

크래시 수집 서비스는 시각을 Unix 밀리초로 반환합니다

빌드 server는 시각을 +09:00이 붙은 ISO 8601로 반환합니다

매칭 server는 상태를 3이나 7 같은 숫자 코드로 반환합니다

3개 모두 외부 서비스여서 응답 형식을 바꿀 수 없습니다.

로그에 따르면 조사의 11%에서 agent가 “빌드 배포 후에 크래시가 늘었다”처럼 이벤트의 선후 관계를 잘못 판단했습니다. system prompt에 시각 형식을 설명하는 문장이 있지만 오류는 줄지 않았습니다.

가장 신뢰할 수 있는 대책은 무엇입니까?

- A. JA: 3つのサーバーの応答をそのまま1つのツール結果に連結し、時系列の判断はClaudeに任せる。
  - KO: 3개 server의 응답을 그대로 하나의 도구 결과로 이어 붙이고, 시간 순서 판단은 Claude에게 맡깁니다.
  - EN: Concatenate the responses of the three servers as is into one tool result and leave chronological judgment to Claude.
- B. JA: PostToolUseフックで、時刻とステータスの形式をClaudeが受け取る前に統一する。
  - KO: PostToolUse hook으로 시각과 상태의 형식을 Claude가 받기 전에 통일합니다.
  - EN: Use a PostToolUse hook to normalize the time and status formats before Claude receives them.
- C. JA: システムプロンプトに各サーバーの時刻の形式とステータスの対応表を載せ、変換してから判断させる。
  - KO: system prompt에 각 server의 시각 형식과 상태 코드 대응표를 넣고, 변환한 뒤 판단하게 합니다.
  - EN: Put each server's time format and a status code mapping table in the system prompt, and have Claude convert before judging.
- D. JA: PreToolUseフックで各ツールの入力に出力形式の指定を加え、サーバーにISO 8601で返させる。
  - KO: PreToolUse hook으로 각 도구 입력에 출력 형식 지정을 추가해, server가 ISO 8601로 반환하게 합니다.
  - EN: Use a PreToolUse hook to add an output format specification to each tool's input and have the servers return ISO 8601.

## CCAR-F-Udemy05-0039

**JA** ある精密機器メーカーの開発チームは、夜間のCIジョブで、Claude Codeに前日の変更に対するテストを生成させています。ジョブのスクリプトはclaude -pで実行しており、終わると標準出力の文章から「N件のテストを生成しました」という部分を正規表現で拾い、生成件数と対象ファイルを集計しています。

この1か月で、次の2つの問題が起きました。

認証の設定が切れてテストが1件も生成されなかった日に、スクリプトがその実行を成功として扱い、後続のジョブに進んだ

Claudeの書き方が「テストを3件追加しました」のように変わるたびに正規表現が一致せず、集計が壊れる

このCIジョブで適切な対応はどれですか。（2つ選択してください。）

**KO** 한 정밀기기 제조사의 개발팀은 야간 CI job에서 Claude Code에게 전날 변경분에 대한 테스트를 생성하게 하고 있습니다. job 스크립트는 claude -p로 실행하며, 실행이 끝나면 표준 출력의 문장에서 “N건의 테스트를 생성했습니다”라는 부분을 정규 표현식으로 찾아 생성 건수와 대상 파일을 집계합니다.

지난 한 달 동안 다음 두 가지 문제가 발생했습니다.

인증 설정이 만료되어 테스트가 한 건도 생성되지 않은 날, 스크립트가 그 실행을 성공으로 처리하고 후속 job으로 넘어갔습니다

Claude의 표현이 “테스트를 3건 추가했습니다”처럼 바뀔 때마다 정규 표현식이 일치하지 않아 집계가 깨집니다

이 CI job에서 적절한 대응은 무엇입니까? (2개를 선택하십시오.)

- A. JA: プロンプトで「最後に『生成件数: N』の形式で書くこと」と指示し、その行を正規表現で拾うようにする。
  - KO: prompt에서 “마지막에 ‘생성 건수: N’ 형식으로 적을 것”이라고 지시하고, 그 줄을 정규 표현식으로 찾게 합니다.
  - EN: Instruct in the prompt to “write at the end in the format ‘生成件数: N’”, and have the regular expression pick up that line.
- B. JA: claudeの終了コードを確認し、0以外であればジョブを失敗として扱う。
  - KO: claude의 종료 코드를 확인해, 0이 아니면 job을 실패로 처리합니다.
  - EN: Check claude's exit code and treat the job as failed if it is nonzero.
- C. JA: --output-format jsonと--json-schemaで、結果を構造化して受け取る。
  - KO: --output-format json과 --json-schema로 결과를 구조화된 형태로 받습니다.
  - EN: Receive the result in structured form with --output-format json and --json-schema.
- D. JA: --max-turnsの値を引き上げ、途中で打ち切られずにテストの生成を最後まで続けさせる。
  - KO: --max-turns 값을 높여, 중간에 끊기지 않고 테스트 생성을 끝까지 이어 가게 합니다.
  - EN: Raise the --max-turns value so that test generation continues to the end without being cut off midway.

## CCAR-F-Udemy05-0040

**JA** ある人材紹介会社は、構造化データ抽出システムを運用しています。このシステムは、応募者から届く履歴書（PDF）から職歴・スキル・希望条件を抽出し、JSONスキーマで検証したうえで候補者データベースに登録します。抽出はサブエージェントが担当しており、現在はシステム全体の18個のツールをすべて利用できる設定です。

ログを確認したところ、次のことが分かりました。

抽出サブエージェントが、検証前のデータを候補者データベースへ直接書き込む呼び出しが週40件ある

応募先企業の情報をウェブ検索する呼び出しが、1件あたり平均3回発生している

抽出の約6割で職種コードマスタの照会が必要で、現在はそのたびにコーディネーターへ処理を戻している

抽出サブエージェントのツール構成として適切な変更はどれですか。（2つ選択してください。）

**KO** 한 인재 소개 회사는 구조화 데이터 추출 시스템을 운영하고 있습니다. 이 시스템은 지원자가 보낸 이력서(PDF)에서 경력·보유 기술·희망 조건을 추출해 JSON schema로 검증한 뒤 후보자 데이터베이스에 등록합니다. 추출은 subagent가 맡고 있으며, 현재는 시스템 전체의 도구 18개를 모두 사용할 수 있도록 설정되어 있습니다.

로그를 확인해 보니 다음과 같은 사실이 드러났습니다.

추출 subagent가 검증 전 데이터를 후보자 데이터베이스에 직접 쓰는 호출이 주 40건 있습니다

지원한 기업의 정보를 웹 검색하는 호출이 1건당 평균 3회 발생합니다

추출의 약 60%에서 직종 코드 마스터 조회가 필요한데, 현재는 그때마다 coordinator에게 처리를 되돌리고 있습니다

추출 subagent의 도구 구성으로 적절한 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 抽出サブエージェントのツールを、文書の読み取りと抽出結果の提出に必要なものだけに絞る。
  - KO: 추출 subagent의 도구를 문서 읽기와 추출 결과 제출에 필요한 것만으로 좁힙니다.
  - EN: Narrow the extraction subagent's tools to only those needed for reading documents and submitting extraction results.
- B. JA: 職種コードマスタを含む候補者データベース全体への読み書き権限を抽出サブエージェントに与える。
  - KO: 직종 코드 마스터를 포함한 후보자 데이터베이스 전체에 대한 읽기·쓰기 권한을 추출 subagent에게 줍니다.
  - EN: Give the extraction subagent read and write permissions to the entire candidate database, including the job code master.
- C. JA: 職種コードマスタだけを照会できる、読み取り専用のlookup_job_codeツールを追加する。
  - KO: 직종 코드 마스터만 조회할 수 있는 읽기 전용 lookup_job_code 도구를 추가합니다.
  - EN: Add a read-only lookup_job_code tool that can query only the job code master.
- D. JA: ツール構成は変えずに、システムプロンプトで「候補者データベースへの書き込みとウェブ検索は行わない」と指示する。
  - KO: 도구 구성은 그대로 두고, system prompt에서 “후보자 데이터베이스 쓰기와 웹 검색은 하지 말 것”이라고 지시합니다.
  - EN: Leave the tool configuration unchanged and instruct in the system prompt, “Do not write to the candidate database or perform web searches.”

## CCAR-F-Udemy05-0041

**JA** ある小売チェーンのEC開発チームは、プルリクエストをClaude Codeで自動レビューし、指摘ごとにcritical・major・minorの重大度を付けてコメントしています。重大度の定義は、レビューのシステムプロンプトに「影響の大きさに応じて判断すること」とだけ書かれています。

直近の監査では、次のような判定の揺れが見つかりました。

決済金額を計算する関数のnullチェック漏れが、あるPRではcritical、別のPRではminorと判定されていた

変数名の表記揺れがmajorと判定された例もあった

開発者の間では、重大度を見ずにコメントを読み流す傾向が広がっています。

重大度の判定を一貫させるために、最も効果的な対策はどれですか。

**KO** 한 소매 체인의 이커머스 개발팀은 pull request를 Claude Code로 자동 리뷰하고, 지적마다 critical·major·minor 심각도를 붙여 코멘트를 답니다. 심각도의 정의는 리뷰 system prompt에 “영향의 크기에 따라 판단할 것”이라고만 적혀 있습니다.

최근 감사에서 다음과 같은 판정 편차가 발견되었습니다.

결제 금액을 계산하는 함수의 null 체크 누락이 어떤 PR에서는 critical, 다른 PR에서는 minor로 판정되었습니다

변수 이름 표기 불일치가 major로 판정된 사례도 있었습니다

개발자들 사이에서는 심각도를 보지 않고 코멘트를 대충 훑고 넘기는 경향이 퍼지고 있습니다.

심각도 판정을 일관되게 만드는 데 가장 효과적인 대책은 무엇입니까?

- A. JA: システムプロンプトに「重大度は慎重に判断し、迷った場合は低いほうを選ぶ」と追記する。
  - KO: system prompt에 “심각도는 신중하게 판단하고, 망설여지면 낮은 쪽을 고를 것”을 추가합니다.
  - EN: Add “Judge severity carefully, and if unsure, choose the lower one” to the system prompt.
- B. JA: 各指摘に重大度とあわせて確信度を出力させ、確信度が0.8以上の指摘だけを投稿する。
  - KO: 각 지적에 심각도와 함께 확신도를 출력하게 하고, 확신도가 0.8 이상인 지적만 게시합니다.
  - EN: Have each finding output a confidence score along with severity, and post only findings with confidence of 0.8 or higher.
- C. JA: 重大度ごとの判定条件を、具体的なコード例とともにシステムプロンプトに追記する。
  - KO: 심각도별 판정 기준을 구체적인 코드 예시와 함께 system prompt에 추가합니다.
  - EN: Add the criteria for each severity level, together with concrete code examples, to the system prompt.
- D. JA: 重大度を「重要」と「その他」の2段階に減らし、判定に迷いが生じる余地を小さくする。
  - KO: 심각도를 “중요”와 “기타” 두 단계로 줄여, 판정에 망설임이 생길 여지를 줄입니다.
  - EN: Reduce severity to two levels, “important” and “other,” to reduce room for uncertainty in determination.

## CCAR-F-Udemy05-0042

**JA** あるレストラン予約サービスの開発チームは、Claude Codeで、満席の時間帯にキャンセル待ちを登録し、空きが出たら順番に案内する機能を実装しようとしています。担当の開発者はキャンセル待ちの仕組みを作った経験がなく、「キャンセル待ち機能を作って」と依頼する予定です。

社内では以前、同じような依頼から作った機能で次の点が考慮されておらず、リリース後に作り直したことがありました。

同時に2件のキャンセルが出たときの案内の順番

通知の送信に失敗した場合の扱い

この機能の実装の進め方として、適切なものはどれですか。（2つ選択してください。）

**KO** 한 레스토랑 예약 서비스의 개발팀은 Claude Code로, 만석인 시간대에 대기 신청을 등록하고 빈자리가 나면 순서대로 안내하는 기능을 구현하려고 합니다. 담당 개발자는 대기 신청 구조를 만들어 본 경험이 없으며, “대기 신청 기능을 만들어 줘”라고 요청할 예정입니다.

사내에서는 예전에 비슷한 요청으로 만든 기능에서 다음 사항을 고려하지 않아, 출시 후 다시 만든 적이 있습니다.

동시에 2건의 취소가 나왔을 때의 안내 순서

알림 전송에 실패했을 때의 처리

이 기능의 구현을 진행하는 방식으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 同時キャンセルや通知失敗時の動作を受け入れ条件として仕様に書き、それから実装を始める。
  - KO: 동시 취소나 알림 실패 시의 동작을 수락 조건으로 명세에 적고, 그다음 구현을 시작합니다.
  - EN: Write the behavior for simultaneous cancellations and notification failures into the spec as acceptance criteria, and then begin implementation.
- B. JA: 実装の前に、設計上の考慮事項をClaudeに質問させ、想定していなかった論点を洗い出す。
  - KO: 구현 전에 Claude가 설계상 고려 사항을 질문하게 해, 예상하지 못한 쟁점을 도출합니다.
  - EN: Before implementation, have Claude ask questions about design considerations to surface issues that had not been anticipated.
- C. JA: 開発者には質問させず、Claudeに詳細な設計書を一人で書かせてから実装を始めさせる。
  - KO: 개발자에게 질문하지 않게 하고, Claude가 상세 설계서를 혼자 쓰게 한 뒤 구현을 시작하게 합니다.
  - EN: Without having Claude ask the developer questions, have it write a detailed design document alone and then begin implementation.
- D. JA: 一般的に妥当と思われる仕様をClaudeに想定させてすぐに実装させ、問題はレビューで直す。
  - KO: 일반적으로 타당해 보이는 명세를 Claude가 가정하게 해 바로 구현하게 하고, 문제는 리뷰에서 고칩니다.
  - EN: Have Claude assume a generally reasonable spec and implement immediately, fixing problems in review.

## CCAR-F-Udemy05-0043

**JA** あるライブ・エンターテインメント企業は、チケットの払い戻しや座席変更の依頼に対応するカスタマーサポート解決エージェントを運用しています。エージェントは顧客のメッセージから枚数・公演日・購入日を抽出し、払い戻し申請のツールに渡します。

ログを調べると、「2、3枚だったと思う」「先月末くらいに買った」のようなくだけた表現の問い合わせで、エージェントが枚数を3、購入日を月末の日付と推測で埋めて申請していました。こうして後から訂正が必要になったケースは、月に140件ありました。

システムプロンプトには抽出の手順が文章で詳しく書かれていますが、例は1つもありません。

抽出のハルシネーションを減らすためのfew-shotの例の使い方として、適切なものはどれですか。（2つ選択してください。）

**KO** 한 라이브 엔터테인먼트 기업은 티켓 환불이나 좌석 변경 요청에 대응하는 고객 지원 해결 agent를 운영하고 있습니다. agent는 고객 메시지에서 매수·공연일·구매일을 추출해 환불 신청 도구에 넘깁니다.

로그를 조사해 보니 “2, 3장이었던 것 같아요”, “지난달 말쯤 샀어요” 같은 구어적인 표현의 문의에서, agent가 매수를 3, 구매일을 월말 날짜로 추측해 채워 신청했습니다. 이 때문에 나중에 정정이 필요해진 경우가 한 달에 140건 있었습니다.

system prompt에는 추출 절차가 글로 자세히 적혀 있지만, 예시는 하나도 없습니다.

추출 hallucination을 줄이기 위한 few-shot 예시 활용법으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 値を一つに確定できない表現のときに、その項目を空のままにして顧客に確認する応答の例を加える。
  - KO: 값을 하나로 확정할 수 없는 표현일 때, 그 항목을 비워 두고 고객에게 확인하는 응답 예시를 추가합니다.
  - EN: Add an example response in which, for expressions where the value cannot be pinned down to one, the field is left empty and the customer is asked to confirm.
- B. JA: 「2、3枚」のようなくだけた表現と正しい抽出結果を示すfew-shotの例を、プロンプトに加える。
  - KO: “2, 3장” 같은 구어적인 표현과 올바른 추출 결과를 보여 주는 few-shot 예시를 prompt에 추가합니다.
  - EN: Add few-shot examples to the prompt that show casual expressions such as “2 or 3 tickets” together with the correct extraction result.
- C. JA: 枚数と購入日を必須フィールドにした抽出ツールの出力例を示し、必ず値を入れて申請させる。
  - KO: 매수와 구매일을 필수 필드로 한 추출 도구의 출력 예시를 보여 주고, 반드시 값을 넣어 신청하게 합니다.
  - EN: Show example outputs of an extraction tool that makes quantity and purchase date required fields, and have it always fill in values when submitting.
- D. JA: 例は加えずに、システムプロンプトに「推測で値を埋めてはならない」と強調して書き加える。
  - KO: 예시는 추가하지 않고, system prompt에 “추측으로 값을 채워서는 안 된다”고 강조해 덧붙입니다.
  - EN: Do not add examples; instead add emphasis in the system prompt: “Never fill in values by guessing.”

## CCAR-F-Udemy05-0044

**JA** ある国際協力NGOのIT部門は、Claude Agent SDKで開発者の生産性向上ツールを作り、寄付管理システムのレガシーコードの調査に使っています。ある開発者は、1つのセッションで2時間以上、寄付の受付から領収書の発行までの処理の流れを調べ続けています。

セッションの前半では、ReceiptIssuerとDonationLedgerの具体的な依存関係を特定していました。しかし後半になると、エージェントは「一般的には、台帳クラスが領収書を発行します」のように、前半で特定したクラス名ではなく典型的なパターンに基づいて答えるようになりました。コンテキストの大半は、GrepとReadの長い出力が占めています。

開発者は、これまでの調査結果を引き継いだまま、同じ調査を続けたいと考えています。

最も適切な対応はどれですか。

**KO** 한 국제협력 NGO의 IT 부서는 Claude Agent SDK로 개발자 생산성 향상 도구를 만들어 기부 관리 시스템의 레거시 코드 조사에 사용하고 있습니다. 한 개발자는 하나의 session에서 2시간 넘게 기부 접수부터 영수증 발급까지의 처리 흐름을 계속 조사하고 있습니다.

session 전반에는 ReceiptIssuer와 DonationLedger의 구체적인 의존 관계를 특정했습니다. 그러나 후반이 되자 agent는 “일반적으로는 원장 클래스가 영수증을 발급합니다”처럼, 전반에 특정한 클래스 이름이 아니라 전형적인 패턴에 기반해 답하기 시작했습니다. context의 대부분은 Grep과 Read의 긴 출력이 차지하고 있습니다.

개발자는 지금까지의 조사 결과를 이어받은 채 같은 조사를 계속하려고 합니다.

가장 적절한 대응은 무엇입니까?

- A. JA: 新しいセッションを起動し、これまでの調査内容は伝えずに、同じ質問を最初から調べ直させる。
  - KO: 새 session을 시작하고, 지금까지의 조사 내용은 전달하지 않은 채 같은 질문을 처음부터 다시 조사하게 합니다.
  - EN: Start a new session and, without conveying the investigation so far, have it investigate the same question from scratch.
- B. JA: allowed_toolsからGrepを外し、以降はReadでファイルを読んで調査を続けさせる。
  - KO: allowed_tools에서 Grep을 빼고, 이후에는 Read로 파일을 읽으며 조사를 계속하게 합니다.
  - EN: Remove Grep from allowed_tools and have it continue the investigation by reading files with Read thereafter.
- C. JA: 残す調査結果を添えて/compactをプロンプトで送り、同じセッションで続ける。
  - KO: 남길 조사 결과를 덧붙여 /compact를 prompt로 보내고, 같은 session에서 계속합니다.
  - EN: Send /compact as a prompt with the findings to retain attached, and continue in the same session.
- D. JA: max_turnsを引き上げ、同じセッションのまま調査を続けさせる。
  - KO: max_turns를 높이고, 같은 session에서 조사를 계속하게 합니다.
  - EN: Raise max_turns and continue the investigation in the same session.

## CCAR-F-Udemy05-0045

**JA** ある航空会社は、予約の変更や手荷物の問い合わせに対応するカスタマーサポート解決エージェントを構築しています。エージェントループはMessages APIを直接呼び出す独自の実装で、「Claudeを呼び出し、ツールの要求があれば実行して結果を返す」処理を最大3回繰り返したあと、その時点の応答テキストを顧客に返します。

1か月分のログでは、振替便の手配のように4回以上のツール呼び出し（get_customer、lookup_order、空席の検索、予約の変更）が必要な案件のうち、18%が「ただいま確認しています」という応答のまま終了していました。一方、単純な問い合わせは1回目の反復で完了しています。

ループの終了判定の改め方として、適切なものはどれですか。（2つ選択してください。）

**KO** 한 항공사는 예약 변경과 수하물 문의에 대응하는 고객 지원 해결 agent를 구축하고 있습니다. agent loop는 Messages API를 직접 호출하는 자체 구현으로, “Claude를 호출하고, 도구 요청이 있으면 실행해 결과를 돌려준다”는 처리를 최대 3번 반복한 뒤 그 시점의 응답 텍스트를 고객에게 반환합니다.

한 달 치 로그를 보면, 대체 항공편 수배처럼 4번 이상의 도구 호출(get_customer, lookup_order, 빈 좌석 검색, 예약 변경)이 필요한 건 중 18%가 “지금 확인하고 있습니다”라는 응답으로 끝났습니다. 반면 단순한 문의는 첫 번째 반복에서 완료됩니다.

loop 종료 판정을 고치는 방법으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 応答テキストに「完了しました」などの語句があれば、ループを終えるよう判定する。
  - KO: 응답 텍스트에 “완료했습니다” 같은 문구가 있으면 loop를 끝내도록 판정합니다.
  - EN: Determine to end the loop if the response text contains a phrase such as “completed.”
- B. JA: 反復回数の上限を3回から10回に引き上げ、10回目の応答を最終回答として顧客に返す。
  - KO: 반복 횟수 상한을 3번에서 10번으로 늘리고, 10번째 응답을 최종 답변으로 고객에게 반환합니다.
  - EN: Raise the iteration limit from 3 to 10 and return the 10th response to the customer as the final answer.
- C. JA: 反復回数の上限は安全装置として大きめに残し、到達した場合は異常として記録する。
  - KO: 반복 횟수 상한은 안전장치로 넉넉하게 남겨 두고, 상한에 도달하면 이상 상황으로 기록합니다.
  - EN: Keep the iteration limit large as a safeguard, and log it as an anomaly if it is reached.
- D. JA: stop_reasonが"tool_use"なら続け、"end_turn"でループを終える。
  - KO: stop_reason이 "tool_use"이면 계속하고, "end_turn"이면 loop를 끝냅니다.
  - EN: Continue if stop_reason is "tool_use", and end the loop on "end_turn".

## CCAR-F-Udemy05-0046

**JA** あるEC物流企業の調査チームは、マルチエージェントリサーチシステムで配送遅延の原因を調べています。検索サブエージェントはMessages APIを直接呼び出す実装で、ツール定義として次の2つを渡しています。

query_tracking_events（説明は「追跡イベントを取得する」、パラメータはq）

search_carrier_notices（説明は「お知らせを検索する」）

追跡番号は「JP」に続く11桁の数字です。

ログを調べたところ、次の誤りが見つかりました。

query_tracking_eventsの呼び出しの34%で、「仙台方面の遅延」のような自由な文章がqに渡されて検証エラーになっていた

個別の荷物の状況をsearch_carrier_noticesで調べようとする呼び出しが、週に120件あった

ツールの選択と入力の誤りを減らすために適切な変更はどれですか。（2つ選択してください。）

**KO** 한 이커머스 물류 기업의 조사팀은 multi-agent 리서치 시스템으로 배송 지연의 원인을 조사하고 있습니다. 검색 subagent는 Messages API를 직접 호출하는 구현이며, 도구 정의로 다음 2개를 넘깁니다.

query_tracking_events(설명은 “추적 이벤트를 가져온다”, 파라미터는 q)

search_carrier_notices(설명은 “공지를 검색한다”)

추적 번호는 “JP” 뒤에 11자리 숫자가 붙는 형식입니다.

로그를 조사해 보니 다음과 같은 오류가 발견되었습니다.

query_tracking_events 호출의 34%에서 “센다이 방면 지연” 같은 자유로운 문장이 q에 전달되어 검증 오류가 났습니다

개별 화물의 상황을 search_carrier_notices로 조사하려는 호출이 주 120건 있었습니다

도구 선택과 입력 오류를 줄이기 위해 적절한 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: query_tracking_eventsに、有効な追跡番号のinput_examplesを数件加える。
  - KO: query_tracking_events에 유효한 추적 번호의 input_examples를 몇 개 추가합니다.
  - EN: Add a few input_examples of valid tracking numbers to query_tracking_events.
- B. JA: 各ツールの説明に、受け付ける入力の形式、返す内容、もう一方のツールを使うべき場面を書き加える。
  - KO: 각 도구의 설명에 받는 입력 형식, 반환하는 내용, 다른 쪽 도구를 써야 하는 경우를 덧붙입니다.
  - EN: Add to each tool's description the input format it accepts, what it returns, and when the other tool should be used instead.
- C. JA: ツールの説明は現在の長さのまま、パラメータ名だけをqからqueryに変更する。
  - KO: 도구 설명은 지금 길이 그대로 두고, 파라미터 이름만 q에서 query로 바꿉니다.
  - EN: Keep the tool descriptions at their current length and only rename the parameter from q to query.
- D. JA: 2つのツールをsearch_logisticsという1つのツールに統合し、入力に応じてサーバー側で振り分ける。
  - KO: 두 도구를 search_logistics라는 하나의 도구로 통합하고, 입력에 따라 server 쪽에서 분기합니다.
  - EN: Merge the two tools into a single tool called search_logistics and route requests on the server side based on the input.

## CCAR-F-Udemy05-0047

**JA** ある通信事業者の開発チームは、Claude Codeで基地局管理システムのコードを生成しています。ルートのCLAUDE.mdは約1,300行あり、起動時に、ファイルが長すぎるという警告が表示されます。そのうち約900行は、次のような特定のファイル種別を扱うときにだけ必要な規約です。

YANGモデル（*.yang）

Terraform（*.tf）

SQLのマイグレーション（*.sql）

画面の改修のように、これらと関係のない作業でも、規約がすべてコンテキストに読み込まれています。チームは、規約を必要なときにだけ読み込ませ、それ以外の作業でのコンテキストの消費を減らしたいと考えています。

適切な変更はどれですか。（2つ選択してください。）

**KO** 한 통신사의 개발팀은 Claude Code로 기지국 관리 시스템의 코드를 생성하고 있습니다. 루트의 CLAUDE.md는 약 1,300줄이며, 시작할 때 파일이 너무 길다는 경고가 표시됩니다. 이 중 약 900줄은 다음과 같은 특정 파일 유형을 다룰 때만 필요한 규약입니다.

YANG 모델(*.yang)

Terraform(*.tf)

SQL migration(*.sql)

화면 개선처럼 이들과 관계없는 작업에서도 규약이 모두 context에 로드되고 있습니다. 팀은 규약을 필요할 때만 로드하게 해서, 그 밖의 작업에서 context 소비를 줄이려고 합니다.

적절한 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: それらの規約を.claude/rules/の個別のファイルに分け、pathsは指定せずにトピック別のフォルダで整理する。
  - KO: 그 규약들을 .claude/rules/의 개별 파일로 나누고, paths는 지정하지 않은 채 주제별 폴더로 정리합니다.
  - EN: Split those conventions into separate files in .claude/rules/, do not specify paths, and organize them in topic-based folders.
- B. JA: 特定のファイル種別の規約を.claude/rules/に分け、各ファイルのpathsにglobを指定する。
  - KO: 특정 파일 유형의 규약을 .claude/rules/로 나누고, 각 파일의 paths에 glob을 지정합니다.
  - EN: Split the conventions for specific file types into .claude/rules/ and specify a glob in the paths of each file.
- C. JA: それらの規約を別のMarkdownファイルに分け、ルートのCLAUDE.mdから@importで読み込む。
  - KO: 그 규약들을 별도의 Markdown 파일로 나누고, 루트의 CLAUDE.md에서 @import로 불러옵니다.
  - EN: Split those conventions into separate Markdown files and load them from the root CLAUDE.md with @import.
- D. JA: ルートのCLAUDE.mdからそれらの規約を削除し、全体に共通する規約だけを残す。
  - KO: 루트의 CLAUDE.md에서 그 규약들을 삭제하고, 전체에 공통인 규약만 남깁니다.
  - EN: Remove those conventions from the root CLAUDE.md and leave only the conventions that are common to everything.

## CCAR-F-Udemy05-0048

**JA** あるガス会社の開発チームは、Claude Codeを使って料金計算モジュールの不具合を修正しています。テストで見つかった問題は次の4件です。

基本料金の日割り計算で、端数の丸め方が仕様と違う

従量料金の計算で、丸めを行う順番が日割りの計算より先になっている

請求書のCSV出力で、列の並び順が仕様と違う

管理画面のエラーメッセージに誤字がある

調べたところ、1と2は、どちらを直すかによってもう一方の期待値が変わる関係にあることが分かりました。3と4は、他の問題とは独立しています。

Claude Codeへの依頼の進め方として適切なものはどれですか。（2つ選択してください。）

**KO** 한 가스 회사의 개발팀은 Claude Code를 사용해 요금 계산 모듈의 버그를 고치고 있습니다. 테스트에서 발견된 문제는 다음 4건입니다.

기본요금 일할 계산에서 끝수 처리 방식이 명세와 다릅니다

사용량 요금 계산에서 끝수를 처리하는 순서가 일할 계산보다 앞서 있습니다

청구서 CSV 출력에서 열 순서가 명세와 다릅니다

관리 화면의 오류 메시지에 오타가 있습니다

조사해 보니 1과 2는 어느 쪽을 고치느냐에 따라 다른 쪽의 기대값이 바뀌는 관계라는 것이 밝혀졌습니다. 3과 4는 다른 문제와 독립적입니다.

Claude Code에 요청을 진행하는 방식으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 1と2は、それぞれ別のセッションで1件ずつ修正させ、最後に結果を突き合わせる。
  - KO: 1과 2는 각각 다른 session에서 한 건씩 수정하게 하고, 마지막에 결과를 맞춰 봅니다.
  - EN: Have items 1 and 2 fixed one at a time in separate sessions, and reconcile the results at the end.
- B. JA: 3と4は、1と2とは分けて、1件ずつ順番に依頼し、確認しながら直す。
  - KO: 3과 4는 1, 2와 분리해 한 건씩 차례로 요청하고, 확인하면서 고칩니다.
  - EN: Handle items 3 and 4 separately from 1 and 2, requesting them one at a time in sequence and fixing them while verifying each.
- C. JA: 1と2は、互いの関係と期待される結果を添えて、1つの詳細なメッセージで依頼する。
  - KO: 1과 2는 서로의 관계와 기대 결과를 덧붙여 하나의 상세한 메시지로 요청합니다.
  - EN: Request items 1 and 2 in a single detailed message that includes their relationship to each other and the expected results.
- D. JA: 4件をまとめて1つのメッセージにし、一度の依頼で修正させる。
  - KO: 4건을 하나의 메시지로 묶어 한 번의 요청으로 수정하게 합니다.
  - EN: Combine all four items into a single message and have them fixed in one request.

## CCAR-F-Udemy05-0049

**JA** ある証券会社の開発チームは、Claude Agent SDKで開発者の生産性向上ツールを作り、エンジニアからの開発依頼を処理させています。依頼の内容に応じて、permission_modeを"plan"にして先に計画を提示させるか、そのまま実装させるかを切り替える方針です。

今週、選択肢に挙げた4件の依頼が届きました。

先に計画を提示させるべき依頼はどれですか。（2つ選択してください。）

**KO** 한 증권사의 개발팀은 Claude Agent SDK로 개발자 생산성 향상 도구를 만들어, 엔지니어의 개발 요청을 처리하게 하고 있습니다. 요청 내용에 따라 permission_mode를 "plan"으로 설정해 먼저 계획을 제시하게 할지, 바로 구현하게 할지를 전환하는 방침입니다.

이번 주에 보기에 제시된 4건의 요청이 들어왔습니다.

먼저 계획을 제시하게 해야 할 요청은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 顧客の認証方式として、社内のシングルサインオンとOAuthのどちらを採用するかを決めて実装する。
  - KO: 고객 인증 방식으로 사내 싱글 사인온과 OAuth 중 무엇을 채택할지 정해 구현합니다.
  - EN: Decide whether to adopt the company's internal single sign-on or OAuth as the customer authentication method, and implement it.
- B. JA: 注文管理の同期処理をメッセージキューによる非同期方式に移し、約50ファイルを変更する。
  - KO: 주문 관리의 동기 처리를 메시지 큐 기반 비동기 방식으로 옮기며, 약 50개 파일을 변경합니다.
  - EN: Move the order management synchronization process to an asynchronous approach using a message queue, changing about 50 files.
- C. JA: 約定通知のログに出力されるメッセージの誤字を、3か所直す。
  - KO: 체결 알림 로그에 출력되는 메시지의 오타를 3곳 고칩니다.
  - EN: Fix typos in the messages output to the execution notification log in three places.
- D. JA: スタックトレースで原因の行が特定済みの、1つの関数に抜けていたnullチェックを追加する。
  - KO: 스택 트레이스로 원인 줄이 이미 특정된, 한 함수에서 빠져 있던 null 체크를 추가합니다.
  - EN: Add a missing null check to a single function, where the offending line has already been identified from the stack trace.

## CCAR-F-Udemy05-0050

**JA** ある建設会社の開発チームは、工程管理システムのプルリクエストごとに、Claude Codeでテストを生成するCIジョブを運用しています。ジョブはリポジトリのルートでclaude -pを実行しており、--bareは付けていません。

生成されたテストを確認したところ、次のことが分かりました。

getterの戻り値を確かめるだけのテストや、依存をすべてモックにして何も検証していないテストが半数を超えていた

tests/factories/に用意しているBuildingFactoryやScheduleFactoryを使わず、テストのたびに建物や工程のデータを一から組み立てていた

テスト生成の品質を高めるために適切な対応はどれですか。（2つ選択してください。）

**KO** 한 건설회사의 개발팀은 공정 관리 시스템의 pull request마다 Claude Code로 테스트를 생성하는 CI job을 운영하고 있습니다. job은 저장소 루트에서 claude -p를 실행하며, --bare는 붙이지 않았습니다.

생성된 테스트를 확인해 보니 다음과 같은 사실이 드러났습니다.

getter의 반환값만 확인하는 테스트나, 의존성을 모두 mock으로 바꿔 아무것도 검증하지 않는 테스트가 절반을 넘었습니다

tests/factories/에 준비된 BuildingFactory나 ScheduleFactory를 쓰지 않고, 테스트마다 건물이나 공정 데이터를 처음부터 조립했습니다

테스트 생성 품질을 높이기 위해 적절한 대응은 무엇입니까? (2개를 선택하십시오.)

- A. JA: プロジェクトのCLAUDE.mdに、工期の境界や資材の上限など、価値のあるテストの基準を書く。
  - KO: 프로젝트의 CLAUDE.md에 공사 기간의 경계나 자재 상한 등 가치 있는 테스트의 기준을 적습니다.
  - EN: Write criteria for valuable tests, such as construction period boundaries and material limits, in the project's CLAUDE.md.
- B. JA: CIのランナーで使うユーザーの~/.claude/CLAUDE.mdに、テストの基準とフィクスチャの使い方を書く。
  - KO: CI runner에서 사용하는 사용자의 ~/.claude/CLAUDE.md에 테스트 기준과 fixture 사용법을 적습니다.
  - EN: Write the test criteria and how to use fixtures in ~/.claude/CLAUDE.md of the user used by the CI runner.
- C. JA: プロジェクトのCLAUDE.mdに、tests/factories/の各ファクトリーの用途と使い方を記載する。
  - KO: 프로젝트의 CLAUDE.md에 tests/factories/의 각 factory 용도와 사용법을 적어 둡니다.
  - EN: Document the purpose and usage of each factory in tests/factories/ in the project's CLAUDE.md.
- D. JA: CIのプロンプトに「質の高い、意味のあるテストを書くこと」という一文を加える。
  - KO: CI prompt에 “질 높고 의미 있는 테스트를 작성할 것”이라는 문장을 추가합니다.
  - EN: Add the sentence "Write high-quality, meaningful tests" to the CI prompt.

## CCAR-F-Udemy05-0051

**JA** ある外食チェーンの本部は、構造化データ抽出システムを運用しています。このシステムは、仕入れ先から届く規格書や納品書（PDFやFAXの画像）から品名・アレルゲン・原産地・単価を抽出し、JSONに変換します。モデルはフィールド単位の確信度スコアも出力しており、現在は確信度0.9以上のフィールドを自動登録し、それ未満を人間のレビューに回しています。

監査の結果、次のことが分かりました。

自動登録されたアレルゲン欄の約6%に誤りがあり、その多くは確信度0.9以上だった

品名欄は、確信度が0.7台でもほぼすべて正しい値だった

レビュー担当者が確認できるのは1日200件までです。

レビューの振り分けを改善するために適切な対応はどれですか。（2つ選択してください。）

**KO** 한 외식 체인 본부는 구조화 데이터 추출 시스템을 운영하고 있습니다. 이 시스템은 공급업체에서 받은 규격서와 납품서(PDF나 팩스 이미지)에서 품명·알레르겐·원산지·단가를 추출해 JSON으로 변환합니다. 모델은 필드 단위의 확신도 점수도 출력하며, 현재는 확신도 0.9 이상인 필드를 자동 등록하고 그 미만은 사람의 리뷰로 돌립니다.

감사 결과 다음과 같은 사실이 드러났습니다.

자동 등록된 알레르겐 항목의 약 6%에 오류가 있었고, 그 대부분은 확신도 0.9 이상이었습니다

품명 항목은 확신도가 0.7대여도 거의 모두 올바른 값이었습니다

리뷰 담당자가 확인할 수 있는 양은 하루 200건까지입니다.

리뷰 배분을 개선하기 위해 적절한 대응은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 全フィールドの自動登録のしきい値を一律0.97に引き上げ、それ未満はすべてレビューに回す。
  - KO: 모든 필드의 자동 등록 임곗값을 일률적으로 0.97로 올리고, 그 미만은 모두 리뷰로 돌립니다.
  - EN: Raise the automatic registration threshold uniformly to 0.97 for all fields, and send everything below it to review.
- B. JA: 確信度が低い抽出と、元の文書があいまいまたは矛盾する抽出を、優先して人間のレビューに回す。
  - KO: 확신도가 낮은 추출과, 원본 문서가 모호하거나 모순되는 추출을 우선해서 사람의 리뷰로 돌립니다.
  - EN: Give priority for human review to extractions with low confidence and to extractions where the source document is ambiguous or contradictory.
- C. JA: ラベル付き検証セットでフィールドごとの確信度と実際の精度を測り、しきい値を個別に決める。
  - KO: 라벨이 붙은 검증 세트로 필드별 확신도와 실제 정확도를 측정해, 임곗값을 개별적으로 정합니다.
  - EN: Measure the per-field confidence and actual accuracy on a labeled validation set, and set the thresholds individually.
- D. JA: プロンプトに「確信が持てないときは確信度を低く出す」と追記し、しきい値は0.9のまま運用する。
  - KO: prompt에 “확신이 없을 때는 확신도를 낮게 출력할 것”을 추가하고, 임곗값은 0.9 그대로 운영합니다.
  - EN: Add "output a low confidence when you are not sure" to the prompt, and keep operating with the threshold at 0.9.

## CCAR-F-Udemy05-0052

**JA** ある工作機械メーカーの開発チームは、Claude Agent SDKで開発者の生産性向上ツールを作り、工場の設備データを扱うMCPサーバーと統合しています。サーバーには、次の2つのツールがあります。

get_line_status（説明は「状態を取得する」、パラメータはid）

get_machine_status（説明は「状態を取得する」、パラメータはid）

生産ラインのIDは「L-12」、個々の機械のIDは「M-0457」のような形式です。

ログを確認すると、「ライン3の稼働状況は？」という質問にget_machine_statusが呼ばれたり、機械のIDがget_line_statusに渡されたりする誤りが、呼び出し全体の37%で起きていました。

誤ったルーティングを減らすために適切な変更はどれですか。（2つ選択してください。）

**KO** 한 공작기계 제조사의 개발팀은 Claude Agent SDK로 개발자 생산성 향상 도구를 만들어, 공장 설비 데이터를 다루는 MCP server와 통합하고 있습니다. server에는 다음 2개의 도구가 있습니다.

get_line_status(설명은 “상태를 가져온다”, 파라미터는 id)

get_machine_status(설명은 “상태를 가져온다”, 파라미터는 id)

생산 라인 ID는 “L-12”, 개별 기계 ID는 “M-0457” 같은 형식입니다.

로그를 확인해 보니 “라인 3의 가동 상황은?”이라는 질문에 get_machine_status가 호출되거나, 기계 ID가 get_line_status에 전달되는 오류가 전체 호출의 37%에서 발생했습니다.

잘못된 routing을 줄이기 위해 적절한 변경은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 各ツールの説明に、対象が生産ライン全体か個々の機械か、もう一方を使うべき場面を書く。
  - KO: 각 도구의 설명에 대상이 생산 라인 전체인지 개별 기계인지, 그리고 다른 쪽 도구를 써야 하는 경우를 적습니다.
  - EN: Write in each tool's description whether it targets an entire production line or an individual machine, and when the other tool should be used.
- B. JA: パラメータ名をline_idとmachine_idに変え、受け付けるIDの形式を説明に書く。
  - KO: 파라미터 이름을 line_id와 machine_id로 바꾸고, 받는 ID 형식을 설명에 적습니다.
  - EN: Rename the parameters to line_id and machine_id, and write the accepted ID format in the description.
- C. JA: 2つのツールの説明を1行に短くそろえ、ツール定義が消費するトークンを抑える。
  - KO: 두 도구의 설명을 한 줄로 짧게 맞춰, 도구 정의가 소비하는 token을 줄입니다.
  - EN: Shorten the descriptions of the two tools to a single line each to reduce the tokens consumed by the tool definitions.
- D. JA: システムプロンプトに「『ライン』という語があればget_line_statusを使う」という規則を追加する。
  - KO: system prompt에 “‘라인’이라는 단어가 있으면 get_line_status를 사용할 것”이라는 규칙을 추가합니다.
  - EN: Add a rule to the system prompt: "If the word 'line' appears, use get_line_status."

## CCAR-F-Udemy05-0053

**JA** あるホテルチェーンは、宿泊者アンケートの自由記述から施設・不満の種類・要望を抽出してJSONに変換する構造化データ抽出システムを、Message Batches APIで運用しています。各ホテルとの取り決めにより、アンケートを受け付けてから36時間以内に、抽出結果を各ホテルに配信する必要があります。アンケートの受付件数は、時期によって1日300件から5,000件まで変動します。

処理の流れは次のとおりです。

受け付けたアンケートを、次のバッチ送信までためておく

送信の直前に、2時間の前処理を行う

バッチを送信する

結果を受け取ったあとに、2時間の検証と配信を行う

検証で失敗した文書は、検証と配信の2時間の中で、同期APIを使って個別に再処理しています。

バッチ送信の頻度の決め方として適切なものはどれですか。（2つ選択してください。）

**KO** 한 호텔 체인은 투숙객 설문의 자유 기술 응답에서 시설·불만 유형·요청 사항을 추출해 JSON으로 변환하는 구조화 데이터 추출 시스템을 Message Batches API로 운영하고 있습니다. 각 호텔과의 약정에 따라, 설문을 접수한 뒤 36시간 이내에 추출 결과를 각 호텔에 전달해야 합니다. 설문 접수 건수는 시기에 따라 하루 300건에서 5,000건까지 변동합니다.

처리 흐름은 다음과 같습니다.

접수한 설문을 다음 batch 전송 때까지 모아 둡니다

전송 직전에 2시간 동안 전처리를 합니다

batch를 전송합니다

결과를 받은 뒤 2시간 동안 검증과 전달을 합니다

검증에 실패한 문서는 검증과 전달에 쓰는 2시간 안에 동기 API를 사용해 개별적으로 재처리합니다.

batch 전송 빈도를 정하는 방법으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 8時間ごとに、その間に受け付けたアンケートをまとめてバッチを送信する。
  - KO: 8시간마다 그동안 접수한 설문을 모아 batch를 전송합니다.
  - EN: Submit a batch every 8 hours, grouping the surveys received during that time.
- B. JA: 送信間隔は、普段の処理時間ではなく、最大24時間の処理時間を前提に計算する。
  - KO: 전송 간격은 평소 처리 시간이 아니라 최대 24시간의 처리 시간을 전제로 계산합니다.
  - EN: Calculate the submission interval based on the maximum processing time of 24 hours, not the usual processing time.
- C. JA: 12時間ごとに、その間に受け付けたアンケートをまとめてバッチを送信する。
  - KO: 12시간마다 그동안 접수한 설문을 모아 batch를 전송합니다.
  - EN: Submit a batch every 12 hours, grouping the surveys received during that time.
- D. JA: 受け付けたアンケートが1,000件たまるたびに、まとめてバッチを送信する。
  - KO: 접수한 설문이 1,000건 쌓일 때마다 모아서 batch를 전송합니다.
  - EN: Submit a batch each time 1,000 received surveys have accumulated.

## CCAR-F-Udemy05-0054

**JA** ある不動産管理会社の開発チームは、Claude Agent SDKで開発者の生産性向上ツールを作っています。エージェントが賃貸契約の更新料を計算するモジュールを改修すると、ツールはその生成セッションをfork_sessionで分岐させ、分岐したセッションに「この変更をレビューして」と依頼します。チームは、生成とは別のセッションIDになるので、独立したレビューになると考えていました。

直近の40件の改修では、次のような結果になりました。

レビューの指摘は合計2件で、文面には「改修時に検討したとおり、端数は切り捨てで問題ありません」のように、生成時の判断を前提にした記述が多く見られた

受け入れテストでは、月の途中で解約した場合の日割り計算の誤りなど、9件の不具合が見つかった

レビューの仕組みとして適切な変更はどれですか。（2つ選択してください。）

**KO** 한 부동산 관리 회사의 개발팀은 Claude Agent SDK로 개발자 생산성 향상 도구를 만들고 있습니다. agent가 임대 계약 갱신료를 계산하는 모듈을 수정하면, 도구는 그 생성 session을 fork_session으로 분기하고 분기된 session에 “이 변경을 리뷰해 줘”라고 요청합니다. 팀은 생성 session과 session ID가 다르므로 독립적인 리뷰가 될 것이라고 생각했습니다.

최근 40건의 수정에서는 다음과 같은 결과가 나왔습니다.

리뷰 지적은 모두 2건이었고, “수정할 때 검토한 대로 끝수는 버림으로 처리해도 문제없습니다”처럼 생성 시의 판단을 전제로 한 서술이 많았습니다

인수 테스트에서는 월 중간에 해지한 경우의 일할 계산 오류 등 9건의 결함이 발견되었습니다

리뷰 구조를 바꾸는 방법으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: 分岐したセッションへの依頼に、生成時の判断を疑って批判的に確認するよう書き加える。
  - KO: 분기된 session에 보내는 요청에, 생성 시의 판단을 의심하고 비판적으로 확인하라는 내용을 덧붙입니다.
  - EN: Add to the request to the branched session an instruction to question the decisions made during generation and check them critically.
- B. JA: 生成セッションをresumeせずに新しいセッションを開始し、レビューを実行させる。
  - KO: 생성 session을 resume하지 않고 새 session을 시작해 리뷰를 실행하게 합니다.
  - EN: Start a new session without resuming the generation session, and run the review in it.
- C. JA: 改修後のファイルと計算規則だけを渡すレビュー用のサブエージェントを定義する。
  - KO: 수정된 파일과 계산 규칙만 전달받는 리뷰용 subagent를 정의합니다.
  - EN: Define a review subagent that is given only the modified files and the calculation rules.
- D. JA: 生成時より上位のモデルを指定して、分岐したセッションでレビューを実行させる。
  - KO: 생성 시보다 상위 모델을 지정해, 분기된 session에서 리뷰를 실행하게 합니다.
  - EN: Specify a higher-tier model than the one used for generation, and run the review in the branched session.

## CCAR-F-Udemy05-0055

**JA** ある自動車メーカーのコネクテッドサービス開発チームは、Claude Codeで車両データの受信APIを改修しています。本番のエラーログから、受信した車台番号（VIN）の桁数を確かめていないために、validate_vin関数で例外が発生していることが分かりました。

スタックトレースで原因の行は特定済みで、この不具合を再現する失敗テストも1件用意してあります。修正は、validate_vin関数に17桁かどうかの確認を1つ加えるだけで済む見込みです。

この修正の進め方として、最も適切なものはどれですか。

**KO** 한 자동차 제조사의 커넥티드 서비스 개발팀은 Claude Code로 차량 데이터 수신 API를 수정하고 있습니다. 운영 환경의 에러 로그를 보니, 수신한 차대번호(VIN)의 자릿수를 확인하지 않아 validate_vin 함수에서 예외가 발생하고 있었습니다.

원인이 된 줄은 스택 트레이스로 이미 특정했고, 이 결함을 재현하는 실패 테스트도 1건 준비해 두었습니다. 수정은 validate_vin 함수에 17자리인지 확인하는 검사 하나만 추가하면 될 것으로 보입니다.

이 수정을 진행하는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: 直接実行でそのまま修正させ、用意した失敗テストと既存のテストが通ることを確かめさせる。
  - KO: 직접 실행으로 바로 수정하게 하고, 준비한 실패 테스트와 기존 테스트가 통과하는지 확인하게 합니다.
  - EN: Use direct execution to have it make the fix as is, and have it confirm that the prepared failing test and the existing tests pass.
- B. JA: インタビューパターンで、VINの検証に関する要件を開発者から聞き取らせてから実装させる。
  - KO: interview pattern으로 VIN 검증 요구사항을 개발자에게서 들은 뒤 구현하게 합니다.
  - EN: Use the interview pattern to have it gather the requirements for VIN validation from the developer, and then implement.
- C. JA: Exploreサブエージェントで、リポジトリ内のVINの扱いをすべて洗い出させてから修正させる。
  - KO: Explore subagent로 저장소 안에서 VIN을 다루는 곳을 모두 찾아낸 뒤 수정하게 합니다.
  - EN: Use an Explore subagent to have it identify everything in the repository that deals with VINs, and then make the fix.
- D. JA: プランモードに入り、車両データの処理全体への影響を調査させてから修正の計画を提示させる。
  - KO: plan mode에 들어가 차량 데이터 처리 전체에 미치는 영향을 조사하게 한 뒤 수정 계획을 제시하게 합니다.
  - EN: Enter plan mode, have it investigate the impact on the entire vehicle data processing, and then have it present a plan for the fix.

## CCAR-F-Udemy05-0056

**JA** ある電力会社のシステム開発チームは、Claude Codeで料金計算システムのコードを生成しています。SQLファイルは、ルートのschema.sqlのほか、services/billing/db/queries/やtools/reports/など複数のディレクトリに散在しています。

チームはSQLの規約を.claude/rules/sql.mdにまとめ、フロントマターにpaths: ["*.sql"]を指定しました。SQL以外の作業では、この規約をコンテキストに読み込ませたくないと考えています。

ところが、ルートのschema.sqlを編集したときは規約が適用されるのに、services/billing/db/queries/配下のSQLファイルを編集したときは適用されません。

最も適切な修正はどれですか。

**KO** 한 전력 회사의 시스템 개발팀은 Claude Code로 요금 계산 시스템의 코드를 생성하고 있습니다. SQL 파일은 루트의 schema.sql 외에도 services/billing/db/queries/나 tools/reports/ 등 여러 디렉터리에 흩어져 있습니다.

팀은 SQL 규칙을 .claude/rules/sql.md에 정리하고, frontmatter에 paths: ["*.sql"]을 지정했습니다. SQL과 관계없는 작업에서는 이 규칙을 context에 불러오고 싶지 않습니다.

그런데 루트의 schema.sql을 편집할 때는 규칙이 적용되지만, services/billing/db/queries/ 아래의 SQL 파일을 편집할 때는 적용되지 않습니다.

가장 적절한 수정은 무엇입니까?

- A. JA: pathsの値を"**/*.sql"に変更し、どの階層にあるSQLファイルにも一致させる。
  - KO: paths 값을 "**/*.sql"로 바꿔, 어느 계층에 있는 SQL 파일에도 일치하게 합니다.
  - EN: Change the paths value to "**/*.sql" so that it matches SQL files at any level of the hierarchy.
- B. JA: sql.mdからpathsを削除し、規約がすべてのセッションで起動時に読み込まれるようにする。
  - KO: sql.md에서 paths를 삭제해, 모든 session에서 시작할 때 규칙을 불러오게 합니다.
  - EN: Remove paths from sql.md so that the conventions are loaded at startup in every session.
- C. JA: sql.mdを.claude/rules/db/に移し、ルールファイルの配置をSQLファイルの構成に合わせる。
  - KO: sql.md를 .claude/rules/db/로 옮겨, 규칙 파일의 위치를 SQL 파일의 구성에 맞춥니다.
  - EN: Move sql.md to .claude/rules/db/ and align the placement of the rule file with the structure of the SQL files.
- D. JA: SQLファイルがある各ディレクトリにCLAUDE.mdを置き、sql.mdと同じ内容を記載する。
  - KO: SQL 파일이 있는 각 디렉터리에 CLAUDE.md를 두고 sql.md와 같은 내용을 적습니다.
  - EN: Place a CLAUDE.md in each directory that contains SQL files and write the same content as sql.md in each.

## CCAR-F-Udemy05-0057

**JA** あるデジタル広告企業の開発チームは、広告配信SDKのプルリクエストをClaude Codeで自動レビューしています。指摘は--json-schemaで定めたJSON形式で出力し、PRのインラインコメントとして投稿しています。直近3か月で、開発者が「却下」した指摘の割合は29%から46%に上がりました。

チームは却下の多い指摘の傾向を調べたいと考えています。しかし、指摘の文面は「非同期処理の例外が握りつぶされています」「catchの中で何もしていません」のように毎回異なり、どの指摘が同じ種類のコードに対するものなのかを集計できません。

却下の傾向を体系的に分析できるようにするための対応として、最も適切なものはどれですか。

**KO** 한 디지털 광고 기업의 개발팀은 광고 송출 SDK의 pull request를 Claude Code로 자동 리뷰하고 있습니다. 지적 사항은 --json-schema로 정한 JSON 형식으로 출력해 PR의 인라인 코멘트로 게시합니다. 최근 3개월 동안 개발자가 “기각”한 지적의 비율은 29%에서 46%로 올랐습니다.

팀은 기각이 많은 지적의 경향을 조사하려고 합니다. 그러나 지적 문구가 “비동기 처리의 예외가 묵살되고 있습니다”, “catch 안에서 아무것도 하지 않습니다”처럼 매번 달라서, 어떤 지적이 같은 종류의 코드에 대한 것인지 집계할 수 없습니다.

기각 경향을 체계적으로 분석할 수 있게 하는 대응으로 가장 적절한 것은 무엇입니까?

- A. JA: 各指摘に確信度を出力させ、確信度0.7未満の指摘はインラインコメントに投稿しない。
  - KO: 각 지적에 확신도를 출력하게 하고, 확신도 0.7 미만인 지적은 인라인 코멘트로 게시하지 않습니다.
  - EN: Have it output a confidence for each finding, and do not post findings with a confidence below 0.7 as inline comments.
- B. JA: スキーマにdetected_patternを加え、指摘の元になったコード構造を記録させる。
  - KO: schema에 detected_pattern을 추가해, 지적의 근거가 된 코드 구조를 기록하게 합니다.
  - EN: Add detected_pattern to the schema and have it record the code structure that gave rise to each finding.
- C. JA: 却下のたびに、開発者に却下の理由を自由記述で入力してもらい、その文章を集計する。
  - KO: 기각할 때마다 개발자에게 기각 이유를 자유 서술로 입력하게 하고, 그 글을 집계합니다.
  - EN: Each time a finding is dismissed, ask the developer to enter the reason for dismissal as free text, and aggregate that text.
- D. JA: PRごとの却下率を集計し、却下率の高いPRの作成者に、指摘を確認するよう促す。
  - KO: PR별 기각률을 집계해, 기각률이 높은 PR의 작성자에게 지적을 확인하도록 권합니다.
  - EN: Aggregate the dismissal rate for each PR, and prompt the authors of PRs with high dismissal rates to review the findings.

## CCAR-F-Udemy05-0058

**JA** ある半導体メーカーの組込みソフトウェアチームは、Claude Codeでファームウェアのコードを生成しています。コードの書き方の指示は、次のように複数のCLAUDE.mdに書かれています。

リポジトリのルートのCLAUDE.mdには「インデントはスペース4つ」

firmware/ディレクトリのCLAUDE.mdには「MISRA Cに準拠し、インデントはスペース2つ」

一部のメンバーの~/.claude/CLAUDE.mdには「インデントはタブを使う」

firmware/配下で生成されたCのコードを調べると、インデントがセッションやメンバーによって、タブ・スペース4つ・スペース2つとばらばらでした。

最も適切な対処はどれですか。

**KO** 한 반도체 제조사의 임베디드 소프트웨어팀은 Claude Code로 펌웨어 코드를 생성하고 있습니다. 코드 작성 방식에 대한 지시는 다음과 같이 여러 CLAUDE.md에 적혀 있습니다.

저장소 루트의 CLAUDE.md: “들여쓰기는 스페이스 4칸”

firmware/ 디렉터리의 CLAUDE.md: “MISRA C를 준수하고, 들여쓰기는 스페이스 2칸”

일부 팀원의 ~/.claude/CLAUDE.md: “들여쓰기는 탭을 사용”

firmware/ 아래에서 생성된 C 코드를 살펴보니, 들여쓰기가 session이나 팀원에 따라 탭, 스페이스 4칸, 스페이스 2칸으로 제각각이었습니다.

가장 적절한 대처는 무엇입니까?

- A. JA: firmware/のCLAUDE.mdの先頭に「上位のCLAUDE.mdより優先する」と書き、他の記述はそのまま残す。
  - KO: firmware/의 CLAUDE.md 맨 앞에 “상위 CLAUDE.md보다 우선한다”라고 쓰고, 다른 내용은 그대로 둡니다.
  - EN: Write "takes precedence over the higher-level CLAUDE.md" at the top of the firmware/ CLAUDE.md, and leave the other entries as they are.
- B. JA: ルートのCLAUDE.mdのインデント規約をfirmware/以外に限り、個人のCLAUDE.mdからインデントの指示を外す。
  - KO: 루트 CLAUDE.md의 들여쓰기 규칙을 firmware/ 이외로 한정하고, 개인 CLAUDE.md에서 들여쓰기 지시를 뺍니다.
  - EN: Limit the indentation convention in the root CLAUDE.md to everything other than firmware/, and remove the indentation instruction from the personal CLAUDE.md files.
- C. JA: ルートのCLAUDE.mdを削除し、各ディレクトリのCLAUDE.mdだけでプロジェクトの規約を管理する。
  - KO: 루트 CLAUDE.md를 삭제하고, 각 디렉터리의 CLAUDE.md만으로 프로젝트 규칙을 관리합니다.
  - EN: Delete the root CLAUDE.md and manage the project's conventions with only the CLAUDE.md in each directory.
- D. JA: firmware/の規約を各メンバーの~/.claude/CLAUDE.mdにも書いてもらい、全員の設定をそろえる。
  - KO: firmware/의 규칙을 각 팀원의 ~/.claude/CLAUDE.md에도 적게 해서 모두의 설정을 맞춥니다.
  - EN: Ask each member to also write the firmware/ conventions in their own ~/.claude/CLAUDE.md so that everyone's settings are aligned.

## CCAR-F-Udemy05-0059

**JA** あるプロスポーツクラブの開発チームは、チケット販売アプリのプルリクエストをClaude Codeで自動レビューするCIパイプラインを運用しています。レビュー用のプロンプトにはN+1クエリを指摘するfew-shotの例が3件ありますが、いずれもforループの中で関連テーブルを参照する、同じ書き方のコードです。

直近3か月の振り返りでは、本番で見つかったN+1クエリ9件のうち7件をレビューが見落としていました。見落とした7件は、内包表記の中での参照やシリアライザー経由での参照など、例とは書き方が異なるものでした。

レビューが例と異なる形の問題にも判断を広げられるようにするための、few-shotの例の見直し方として最も効果的なものはどれですか。

**KO** 한 프로 스포츠 구단의 개발팀은 티켓 판매 앱의 pull request를 Claude Code로 자동 리뷰하는 CI pipeline을 운영하고 있습니다. 리뷰용 prompt에는 N+1 쿼리를 지적하는 few-shot 예시가 3개 있는데, 모두 for loop 안에서 관련 테이블을 참조하는, 같은 방식으로 작성된 코드입니다.

최근 3개월을 돌아보니, 운영 환경에서 발견된 N+1 쿼리 9건 중 7건을 리뷰가 놓쳤습니다. 놓친 7건은 컴프리헨션 안에서의 참조나 serializer를 거친 참조 등 예시와 작성 방식이 다른 것이었습니다.

리뷰가 예시와 다른 형태의 문제에도 판단을 넓힐 수 있도록 few-shot 예시를 개선하는 방법으로 가장 효과적인 것은 무엇입니까?

- A. JA: few-shotの例を外し、N+1クエリの定義と検出条件をシステムプロンプトに詳しく書く。
  - KO: few-shot 예시를 빼고, N+1 쿼리의 정의와 탐지 조건을 system prompt에 자세히 적습니다.
  - EN: Remove the few-shot examples and write a detailed definition of N+1 queries and detection conditions in the system prompt.
- B. JA: 書き方の異なるN+1の例と問題のない一括取得の例を、判断の理由付きでプロンプトに示す。
  - KO: 작성 방식이 다른 N+1 예시와 문제가 없는 일괄 조회 예시를, 판단 이유와 함께 prompt에 제시합니다.
  - EN: Show in the prompt examples of N+1 written in different ways and examples of acceptable bulk fetching, with the reasoning for each judgment.
- C. JA: 既存の例は残し、「類似のパターンも漏れなく報告する」という指示を追記する。
  - KO: 기존 예시는 남기고, “유사한 패턴도 빠짐없이 보고한다”라는 지시를 추가합니다.
  - EN: Keep the existing examples and add the instruction "Report similar patterns without omission."
- D. JA: 見落とした7件のコードを、そのままfew-shotの例として追加する。
  - KO: 놓친 7건의 코드를 그대로 few-shot 예시로 추가합니다.
  - EN: Add the code of the 7 missed cases as is as few-shot examples.

## CCAR-F-Udemy05-0060

**JA** あるホテル予約サイトの開発チームは、CIパイプラインでClaude Codeに料金計算の不具合を修正させ、同じセッションの中で「自分の変更をレビューし、問題があれば指摘して」と依頼しています。レビューの精度を上げるため、拡張思考も有効にしています。

過去30件のPRで、このセルフレビューが指摘した問題は0件でした。しかしリリース後に、連泊割引と消費税の丸めの順序が逆になっている不具合など、4件の不具合が見つかりました。

レビューの仕組みとして適切な改善はどれですか。（2つ選択してください。）

**KO** 한 호텔 예약 사이트의 개발팀은 CI pipeline에서 Claude Code에 요금 계산 결함을 수정하게 하고, 같은 session 안에서 “자기 변경을 리뷰하고 문제가 있으면 지적해 줘”라고 요청합니다. 리뷰 정확도를 높이기 위해 extended thinking도 켜 두었습니다.

지난 30건의 PR에서 이 셀프 리뷰가 지적한 문제는 0건이었습니다. 그러나 릴리스 후에 연박 할인과 소비세 끝수 처리의 순서가 뒤바뀐 결함 등 4건의 결함이 발견되었습니다.

리뷰 구조의 개선으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: レビュー役には差分と仕様・レビュー基準だけを渡し、修正時の説明や推論は渡さない。
  - KO: 리뷰 담당에게는 diff와 사양·리뷰 기준만 전달하고, 수정할 때의 설명이나 추론은 전달하지 않습니다.
  - EN: Give the reviewer only the diff and the specification and review criteria, and do not give it the explanations or reasoning from when the fix was made.
- B. JA: 修正を生成するセッションのeffortを上げ、より深く考えてからレビューさせる。
  - KO: 수정을 생성하는 session의 effort를 올려, 더 깊이 생각한 뒤 리뷰하게 합니다.
  - EN: Raise the effort of the session that generates the fix so that it thinks more deeply before reviewing.
- C. JA: 同じセッションのまま、チェックリストを渡して「より厳しく」レビューし直すよう指示する。
  - KO: 같은 session을 유지한 채 체크리스트를 주고 “더 엄격하게” 다시 리뷰하도록 지시합니다.
  - EN: Stay in the same session, give it a checklist, and instruct it to review again "more strictly."
- D. JA: 修正を生成したセッションとは別の、独立したインスタンスでレビューを実行する。
  - KO: 수정을 생성한 session과는 별개인 독립 인스턴스에서 리뷰를 실행합니다.
  - EN: Run the review in an independent instance separate from the session that generated the fix.

## CCAR-F-Udemy06-0001

**JA** ある農業機械メーカーの開発チームは、圃場センサーのデータを扱うマイクロサービス群のリポジトリでClaude Codeを使っています。Protocol Buffersの定義ファイル（*.proto）の書き方に関する規約を.claude/rules/proto.mdに書き、フロントマターにpaths: ["proto/*.proto"]を指定しました。

ところが、services/irrigation/api/v1/schedule.protoのように各サービスの配下にある定義ファイルを編集するときには、この規約が読み込まれていないことがわかりました。

場所に関係なく、すべての定義ファイルにこの規約を適用するための修正として最も適切なものはどれですか。

**KO** 한 농기계 제조사의 개발팀은 농지 센서 데이터를 다루는 마이크로서비스들의 저장소에서 Claude Code를 사용하고 있습니다. Protocol Buffers 정의 파일(*.proto) 작성 규칙을 .claude/rules/proto.md에 적고, frontmatter에 paths: ["proto/*.proto"]를 지정했습니다.

그런데 services/irrigation/api/v1/schedule.proto처럼 각 서비스 아래에 있는 정의 파일을 편집할 때는 이 규칙이 로드되지 않는다는 것을 알게 되었습니다.

위치와 관계없이 모든 정의 파일에 이 규칙을 적용하기 위한 수정으로 가장 적절한 것은 무엇입니까?

- A. JA: pathsの値を["*.proto"]に変更し、拡張子だけで定義ファイルに一致させる。
  - KO: paths 값을 ["*.proto"]로 바꿔, 확장자만으로 정의 파일에 일치하게 합니다.
  - EN: Change the paths value to ["*.proto"] so that definition files are matched by extension alone.
- B. JA: フロントマターからpathsの行を削除し、ルールを無条件に読み込ませる。
  - KO: frontmatter에서 paths 줄을 삭제해, 규칙을 무조건 로드하게 합니다.
  - EN: Delete the paths line from the frontmatter so that the rule is loaded unconditionally.
- C. JA: 各サービスのディレクトリにCLAUDE.mdを置き、同じ規約をそれぞれに書き写す。
  - KO: 각 서비스 디렉터리에 CLAUDE.md를 두고, 같은 규칙을 각각 옮겨 적습니다.
  - EN: Place a CLAUDE.md in each service's directory and copy the same conventions into each.
- D. JA: pathsの値を["**/*.proto"]に変更し、どの階層の定義ファイルにも一致させる。
  - KO: paths 값을 ["**/*.proto"]로 바꿔, 어느 계층의 정의 파일에도 일치하게 합니다.
  - EN: Change the paths value to ["**/*.proto"] so that it matches definition files at any level of the hierarchy.

## CCAR-F-Udemy06-0002

**JA** ある国際協力NGOの調査部門は、Claude Agent SDKを使って、支援対象地域の保健・教育データを調べるマルチエージェントリサーチシステムを構築しています。コーディネーターのオプションは、次のように設定しました。

agentsパラメータに、web-researcherとdocument-analystの2つのAgentDefinitionを定義する

allowedToolsには、Read・Grep・WebSearchを指定する

ところが実行ログを見ると、サブエージェントは一度も呼び出されず、コーディネーター自身がウェブ検索と文書の読み込みをすべて行っていました。また、2つのdescriptionはどちらも「調査を手伝う」という一文だけでした。

サブエージェントに作業を委任させるための変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 국제협력 NGO의 조사 부문은 Claude Agent SDK로, 지원 대상 지역의 보건·교육 데이터를 조사하는 multi-agent 리서치 시스템을 구축하고 있습니다. coordinator의 옵션은 다음과 같이 설정했습니다.

agents 파라미터에 web-researcher와 document-analyst 두 개의 AgentDefinition을 정의합니다

allowedTools에는 Read·Grep·WebSearch를 지정합니다

그런데 실행 로그를 보니 subagent는 한 번도 호출되지 않았고, coordinator 자신이 웹 검색과 문서 읽기를 모두 수행했습니다. 또한 두 description은 모두 “조사를 돕는다”라는 한 문장뿐이었습니다.

subagent에게 작업을 위임하게 만들기 위한 변경으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: 各サブエージェントのpromptに「コーディネーターの会話履歴を参照すること」と書き加える。
  - KO: 각 subagent의 prompt에 “coordinator의 대화 기록을 참조할 것”이라고 덧붙입니다.
  - EN: Add to each subagent's prompt the instruction "Refer to the coordinator's conversation history."
- B. JA: 2つのサブエージェントの手順をコーディネーターのシステムプロンプトに書き写し、1体で処理させる。
  - KO: 두 subagent의 절차를 coordinator의 system prompt에 옮겨 적고, 하나의 agent가 처리하게 합니다.
  - EN: Copy the procedures of the two subagents into the coordinator's system prompt and have a single agent handle everything.
- C. JA: 各descriptionに、どんな依頼のときにそのサブエージェントを使うかを具体的に書く。
  - KO: 각 description에, 어떤 요청일 때 그 subagent를 사용하는지 구체적으로 적습니다.
  - EN: Write in each description, specifically, for what kinds of requests that subagent should be used.
- D. JA: allowedToolsに、サブエージェントを起動するAgentツール（旧Taskツール）を追加する。
  - KO: allowedTools에 subagent를 실행하는 Agent 도구(이전 Task 도구)를 추가합니다.
  - EN: Add the Agent tool (formerly the Task tool), which launches subagents, to allowedTools.

## CCAR-F-Udemy06-0003

**JA** ある研究機関の情報基盤チームは、研究者がClaude Codeから日常業務のシステムを操作できるよう、MCPサーバーの導入を計画しています。対象は次の3つです。

ソースコードを管理するGitLab

連絡に使うSlack

研究所独自の実験装置予約システム

予約システムには、装置ごとの利用資格の確認と、安全講習の受講記録の照合を経てから予約を確定する独自の手順があります。開発に使える人員は1名で、保守の負担を最小限にしたいと考えています。

MCPサーバーの選び方として適切なものはどれですか。（2つ選択してください。）

**KO** 한 연구 기관의 정보 인프라팀은 연구자가 Claude Code에서 일상 업무 시스템을 조작할 수 있도록 MCP server 도입을 계획하고 있습니다. 대상은 다음 3가지입니다.

소스 코드를 관리하는 GitLab

연락에 쓰는 Slack

연구소 자체의 실험 장비 예약 시스템

예약 시스템에는 장비별 이용 자격 확인과 안전 교육 이수 기록 대조를 거친 뒤에 예약을 확정하는 고유한 절차가 있습니다. 개발에 투입할 수 있는 인원은 1명이고, 유지보수 부담을 최소화하려고 합니다.

MCP server를 고르는 방법으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: MCPサーバーは導入せず、Claudeにcurlで各システムのAPIを直接呼ばせる手順をCLAUDE.mdに書く。
  - KO: MCP server는 도입하지 않고, Claude가 curl로 각 시스템의 API를 직접 호출하는 절차를 CLAUDE.md에 적습니다.
  - EN: Do not introduce MCP servers, and write in CLAUDE.md a procedure for having Claude call each system's API directly with curl.
- B. JA: GitLabとSlackには、公開されている既存のMCPサーバーを採用する。
  - KO: GitLab과 Slack에는 공개된 기존 MCP server를 채택합니다.
  - EN: Adopt existing publicly available MCP servers for GitLab and Slack.
- C. JA: 実験装置予約システムには、独自の予約手順を実装したカスタムMCPサーバーを作る。
  - KO: 실험 장비 예약 시스템에는 고유한 예약 절차를 구현한 custom MCP server를 만듭니다.
  - EN: For the laboratory equipment reservation system, build a custom MCP server that implements its own reservation procedure.
- D. JA: 3つのシステムをまとめて扱う1つのカスタムMCPサーバーを作り、GitLabとSlackのAPIも自前で実装する。
  - KO: 3개 시스템을 함께 다루는 하나의 custom MCP server를 만들고, GitLab과 Slack의 API도 직접 구현합니다.
  - EN: Build a single custom MCP server that handles all three systems together, and implement the GitLab and Slack APIs in-house as well.

## CCAR-F-Udemy06-0004

**JA** ある鉄道会社は、Claude Agent SDKを使って、乗車券の払い戻しや変更の問い合わせに対応するカスタマーサポート解決エージェントを運用しています。予約を照会するlookup_reservationツールは、1回の呼び出しで座席表、経路の詳細、運賃の内訳、ポイントの履歴など約45のフィールドを返します。しかし、払い戻しの判断に使うのは、予約番号、乗車日、区間、支払額、払い戻しの可否の5つです。

複数の予約について問い合わせる長い会話では、照会結果がコンテキストに積み上がり、会話の後半で、序盤に確認した支払額をエージェントが取り違えるケースが見られます。

この問題の原因に直接効く対策として、最も効果的なものはどれですか。

**KO** 한 철도 회사는 Claude Agent SDK로, 승차권 환불이나 변경 문의에 대응하는 고객 지원 해결 agent를 운영하고 있습니다. 예약을 조회하는 lookup_reservation 도구는 한 번 호출에 좌석표, 경로 상세, 운임 내역, 포인트 이력 등 약 45개 필드를 반환합니다. 하지만 환불 판단에 쓰는 것은 예약 번호, 승차일, 구간, 결제 금액, 환불 가능 여부의 5개뿐입니다.

여러 예약에 대해 문의하는 긴 대화에서는 조회 결과가 context에 쌓이고, 대화 후반에 agent가 초반에 확인한 결제 금액을 혼동하는 경우가 보입니다.

이 문제의 원인을 직접 해결하는 대책으로 가장 효과적인 것은 무엇입니까?

- A. JA: 照会結果がコンテキストに入る前に、払い戻しに関係する5つのフィールドだけに切り詰める。
  - KO: 조회 결과가 context에 들어가기 전에, 환불과 관련된 5개 필드만 남기고 잘라냅니다.
  - EN: Before lookup results enter the context, trim them down to only the five fields relevant to refunds.
- B. JA: 照会のたびに、それまでのツール結果をすべて会話履歴から削除してから次の照会を行う。
  - KO: 조회할 때마다 그때까지의 도구 결과를 대화 기록에서 모두 삭제한 뒤 다음 조회를 합니다.
  - EN: Each time a lookup is made, delete all previous tool results from the conversation history before making the next lookup.
- C. JA: より大きなコンテキストウィンドウを持つモデルに切り替え、照会結果をそのまま保持させる。
  - KO: 더 큰 context window를 가진 모델로 바꿔, 조회 결과를 그대로 유지하게 합니다.
  - EN: Switch to a model with a larger context window and keep the lookup results as they are.
- D. JA: 会話が長くなったら、それまでのやり取りを段階的に要約し、古いメッセージを要約に置き換える。
  - KO: 대화가 길어지면 그때까지의 대화를 단계적으로 요약하고, 오래된 메시지를 요약으로 대체합니다.
  - EN: When the conversation gets long, progressively summarize the exchanges so far and replace old messages with the summary.

## CCAR-F-Udemy06-0005

**JA** ある会計事務所は、Claudeを使って、顧問先から届く決算書類のPDFから構造化データを抽出しています。処理は次の2段階です。

extract_metadataで、顧問先名・決算期・書類の種類を抽出する

その結果を使ってlookup_client_ledgerで顧問先の総勘定元帳を照会し、データを補完する

初回のリクエストでは、tool_choiceを{"type": "any"}にしています。しかし、ログを確認すると、約12%のケースで最初にlookup_client_ledgerが呼ばれ、書類から読み取った正式名称ではなく、推測した顧問先名で元帳が照会されていました。

抽出を確実に先に実行させるための変更として最も適切なものはどれですか。

**KO** 한 회계 사무소는 Claude로, 고객사에서 받은 결산 서류 PDF에서 구조화 데이터를 추출하고 있습니다. 처리는 다음 2단계입니다.

extract_metadata로 고객사명·결산기·서류 종류를 추출합니다

그 결과를 사용해 lookup_client_ledger로 고객사의 총계정원장을 조회하고 데이터를 보완합니다

첫 요청에서는 tool_choice를 {"type": "any"}로 설정했습니다. 그런데 로그를 확인하니 약 12%의 경우에 lookup_client_ledger가 먼저 호출되어, 서류에서 읽은 정식 명칭이 아니라 추측한 고객사명으로 원장을 조회하고 있었습니다.

추출을 확실히 먼저 실행하게 하는 변경으로 가장 적절한 것은 무엇입니까?

- A. JA: 初回のリクエストではlookup_client_ledgerの呼び出しを許可し、結果が空なら抽出からやり直す。
  - KO: 첫 요청에서 lookup_client_ledger 호출을 허용하고, 결과가 비어 있으면 추출부터 다시 합니다.
  - EN: Allow the lookup_client_ledger call in the initial request, and start over from extraction if the result is empty.
- B. JA: 初回のリクエストでtool_choiceにextract_metadataを指定し、抽出ツールを強制する。
  - KO: 첫 요청에서 tool_choice에 extract_metadata를 지정해 추출 도구를 강제합니다.
  - EN: In the initial request, specify extract_metadata in tool_choice to force the extraction tool.
- C. JA: lookup_client_ledgerの説明に、extract_metadataの結果を受け取ってから呼ぶことを明記する。
  - KO: lookup_client_ledger의 설명에, extract_metadata의 결과를 받은 뒤에 호출한다고 명시합니다.
  - EN: State explicitly in the description of lookup_client_ledger that it should be called only after receiving the result of extract_metadata.
- D. JA: 初回のリクエストのtool_choiceをautoに戻し、システムプロンプトで抽出を先に行うよう指示する。
  - KO: 첫 요청의 tool_choice를 auto로 되돌리고, system prompt에서 추출을 먼저 하도록 지시합니다.
  - EN: Return the tool_choice of the initial request to auto, and instruct in the system prompt that extraction be performed first.

## CCAR-F-Udemy06-0006

**JA** ある不動産仲介会社の開発チームは、物件検索サービスの改修にClaude Codeを使っています。チームで共有しているスキル/compare-designsは、新機能の設計案を5つほど挙げ、それぞれの長所と短所を検討したうえで推奨案を示します。

ところが、このスキルをメインの会話で実行すると、採用しなかった案の詳しい検討内容が会話に大量に残ります。その結果、その後の実装の段階で、Claudeが不採用の案の考え方をコードに混ぜてしまうことがありました。

メインの会話を汚さずにこのスキルを使えるようにする変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 부동산 중개 회사의 개발팀은 매물 검색 서비스 수정에 Claude Code를 사용하고 있습니다. 팀이 공유하는 skill /compare-designs는 신기능 설계안을 5개 정도 제시하고, 각각의 장단점을 검토한 뒤 추천안을 내놓습니다.

그런데 이 skill을 메인 대화에서 실행하면, 채택하지 않은 안에 대한 상세한 검토 내용이 대화에 대량으로 남습니다. 그 결과 이후 구현 단계에서 Claude가 채택하지 않은 안의 발상을 코드에 섞어 버리는 일이 있었습니다.

메인 대화를 오염시키지 않고 이 skill을 쓸 수 있게 하는 변경으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: SKILL.mdのフロントマターにcontext: forkを追加する。
  - KO: SKILL.md의 frontmatter에 context: fork를 추가합니다.
  - EN: Add context: fork to the frontmatter of SKILL.md.
- B. JA: スキルを実行したあとに毎回/clearを実行し、会話をリセットしてから実装に進む。
  - KO: skill을 실행한 뒤 매번 /clear를 실행해 대화를 초기화하고 나서 구현으로 넘어갑니다.
  - EN: Run /clear every time after running the skill, resetting the conversation before moving on to implementation.
- C. JA: スキルの本文に、最後は推奨案とその理由、比較表だけを要約して返すよう指示を書く。
  - KO: skill 본문에, 마지막에는 추천안과 그 이유, 비교표만 요약해서 반환하라는 지시를 적습니다.
  - EN: In the body of the skill, write an instruction to return, at the end, only a summary of the recommended proposal, its rationale, and a comparison table.
- D. JA: スキルの内容をプロジェクトのCLAUDE.mdに移し、設計の検討を常に読み込まれる手順にする。
  - KO: skill 내용을 프로젝트의 CLAUDE.md로 옮겨, 설계 검토를 항상 로드되는 절차로 만듭니다.
  - EN: Move the contents of the skill to the project's CLAUDE.md, making design deliberation a procedure that is always loaded.

## CCAR-F-Udemy06-0007

**JA** ある広告代理店の開発チームは、Claude Agent SDKを使って、エンジニアが広告配信システムのコードや関連資料を調べるための開発者の生産性向上ツールを構築しています。

エージェントには組み込みツールのほかに、社内のMCPサーバーが提供するsearch_assets（説明は「アセットを検索する」）とsearch_creatives（説明は「クリエイティブを検索する」）があります。前者はコードとインフラ設定のリポジトリを、後者は広告素材の管理システムを検索するツールです。

ログを分析すると、広告素材に関する質問の41%でsearch_assetsが呼ばれていました。また、システムプロンプトには「ユーザーが『検索』と言ったら、まずsearch_assetsを使うこと」という一文がありました。

誤ったルーティングを減らすための変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 광고 대행사의 개발팀은 Claude Agent SDK로, 엔지니어가 광고 송출 시스템의 코드와 관련 자료를 조사하기 위한 개발자 생산성 향상 도구를 구축하고 있습니다.

agent에는 내장 도구 외에, 사내 MCP server가 제공하는 search_assets(설명은 “애셋을 검색한다”)와 search_creatives(설명은 “크리에이티브를 검색한다”)가 있습니다. 전자는 코드와 인프라 설정 저장소를, 후자는 광고 소재 관리 시스템을 검색하는 도구입니다.

로그를 분석하니, 광고 소재에 관한 질문의 41%에서 search_assets가 호출되었습니다. 또한 system prompt에는 “사용자가 ‘검색’이라고 하면 먼저 search_assets를 사용할 것”이라는 문장이 있었습니다.

잘못된 routing을 줄이기 위한 변경으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: search_assetsをsearch_code_and_infraに名前変更し、両ツールの説明に検索対象と使い分けを書く。
  - KO: search_assets의 이름을 search_code_and_infra로 바꾸고, 두 도구의 설명에 검색 대상과 구분해 쓰는 기준을 적습니다.
  - EN: Rename search_assets to search_code_and_infra, and write the search targets and how to choose between them in both tools' descriptions.
- B. JA: tool_choiceでsearch_creativesを強制し、素材に関する質問では必ずこのツールが呼ばれるようにする。
  - KO: tool_choice로 search_creatives를 강제해, 소재에 관한 질문에서는 반드시 이 도구가 호출되게 합니다.
  - EN: Force search_creatives with tool_choice so that this tool is always called for questions about creatives.
- C. JA: 「検索」という語に反応してツールを決める一文を、質問の対象に応じて選ぶ書き方に改める。
  - KO: “검색”이라는 단어에 반응해 도구를 정하는 문장을, 질문 대상에 따라 고르도록 고쳐 씁니다.
  - EN: Rewrite the sentence that decides the tool based on the word "search" so that the tool is chosen according to what the question is about.
- D. JA: search_assetsの結果に素材が含まれない場合は、続けてsearch_creativesを呼ぶようループ側で再実行する。
  - KO: search_assets 결과에 소재가 포함되지 않으면, 이어서 search_creatives를 호출하도록 loop 쪽에서 다시 실행합니다.
  - EN: If the results of search_assets contain no creatives, have the loop re-run by calling search_creatives next.

## CCAR-F-Udemy06-0008

**JA** ある製薬会社の開発チームは、Claude Code（Read・Grep・Globを含む組み込みツールを有効にした構成）を使って、治験データ管理システムのコードを改修しています。

新しく参加したエンジニアが「症例データをCSVで書き出すエクスポート機能が、どのモジュールを経由して出力しているかを説明して」と依頼しました。すると、Claudeはリポジトリ内の約400ファイルを順にReadで読み始め、途中でコンテキストの大半を使い切ってしまいました。

このような依頼でコードベースの理解を段階的に進めるために、Claudeに取らせるべき探索の進め方として最も適切なものはどれですか。

**KO** 한 제약 회사의 개발팀은 Claude Code(Read·Grep·Glob을 포함한 내장 도구를 켠 구성)로 임상시험 데이터 관리 시스템의 코드를 수정하고 있습니다.

새로 합류한 엔지니어가 “증례 데이터를 CSV로 내보내는 export 기능이 어떤 모듈을 거쳐 출력하는지 설명해 줘”라고 요청했습니다. 그러자 Claude는 저장소 안의 약 400개 파일을 차례로 Read로 읽기 시작했고, 도중에 context의 대부분을 다 써 버렸습니다.

이런 요청에서 코드베이스 이해를 단계적으로 넓혀 가기 위해 Claude가 취해야 할 탐색 방식으로 가장 적절한 것은 무엇입니까?

- A. JA: 最初にREADMEとdocs/配下の設計書だけをReadで読ませ、その記述をもとに処理の流れを説明させる。
  - KO: 먼저 README와 docs/ 아래의 설계 문서만 Read로 읽게 하고, 그 내용을 바탕으로 처리 흐름을 설명하게 합니다.
  - EN: Have it first read only the README and the design documents under docs/ with Read, and explain the processing flow based on what they say.
- B. JA: Globで**/*export*.pyに一致するファイルを列挙し、見つかったファイルをすべてReadで読ませる。
  - KO: Glob으로 **/*export*.py에 일치하는 파일을 나열하고, 찾은 파일을 모두 Read로 읽게 합니다.
  - EN: Use Glob to list the files matching **/*export*.py, and have it read all of the files found with Read.
- C. JA: 400ファイルを10ファイルずつに分け、Readで読んで要約する作業を、全ファイルが終わるまで順に繰り返させる。
  - KO: 400개 파일을 10개씩 나눠 Read로 읽고 요약하는 작업을, 모든 파일이 끝날 때까지 차례로 반복하게 합니다.
  - EN: Split the 400 files into groups of 10, and have it repeat the work of reading each group with Read and summarizing it, in order, until all files are done.
- D. JA: Grepで処理の入口となるコマンド名を探し、そこからimportをたどってReadで読ませる。
  - KO: Grep으로 처리의 진입점이 되는 명령 이름을 찾고, 거기서부터 import를 따라가며 Read로 읽게 합니다.
  - EN: Use Grep to find the command name that is the entry point of the processing, and have it follow the imports from there, reading with Read.

## CCAR-F-Udemy06-0009

**JA** ある会計事務所は、Claude Agent SDKを使って、顧問先の業界動向や財務資料を調べるマルチエージェントリサーチシステムを運用しています。文書分析サブエージェントは、所内の文書管理システムのMCPツールfetch_client_documentで資料を取得します。事務所の独立性規程により、監査を担当している顧問先の税務資料は、アドバイザリー部門の調査には使えません。

この規程に該当する要求に対して、ツールは現在「Access denied」とだけ返しています。サブエージェントは資料名や検索語を変えて同じ取得を何度も試みた末に、レポートに「一部の資料を取得できませんでした」とだけ記載していました。

この状況を改善するためのツールの変更として最も適切なものはどれですか。

**KO** 한 회계 사무소는 Claude Agent SDK로, 고객사의 업계 동향과 재무 자료를 조사하는 multi-agent 리서치 시스템을 운영하고 있습니다. 문서 분석 subagent는 사내 문서 관리 시스템의 MCP 도구 fetch_client_document로 자료를 가져옵니다. 사무소의 독립성 규정에 따라, 감사를 맡고 있는 고객사의 세무 자료는 자문 부문의 조사에 사용할 수 없습니다.

이 규정에 해당하는 요청에 대해 도구는 현재 “Access denied”만 반환합니다. subagent는 자료명이나 검색어를 바꿔 가며 같은 조회를 여러 번 시도한 끝에, 보고서에 “일부 자료를 가져오지 못했습니다”라고만 적었습니다.

이 상황을 개선하기 위한 도구 변경으로 가장 적절한 것은 무엇입니까?

- A. JA: isError: trueに、規程による拒否の分類とリトライ不可のフラグを添えて返す。
  - KO: isError: true에, 규정에 따른 거부라는 분류와 재시도 불가 플래그를 함께 담아 반환합니다.
  - EN: Return isError: true with a classification of denial due to the policy and a flag indicating that retrying is not allowed.
- B. JA: 検索結果から該当資料を除外し、存在しないかのように空の結果を返す。
  - KO: 검색 결과에서 해당 자료를 제외하고, 존재하지 않는 것처럼 빈 결과를 반환합니다.
  - EN: Exclude the relevant materials from the search results and return an empty result as if they did not exist.
- C. JA: HTTPのステータスコード403だけを返し、どう対処するかの判断はサブエージェントに任せる。
  - KO: HTTP 상태 코드 403만 반환하고, 어떻게 대처할지는 subagent의 판단에 맡깁니다.
  - EN: Return only the HTTP status code 403 and leave the decision of how to respond to the subagent.
- D. JA: エラーメッセージに「リトライは3回まで」という指示を含めて返す。
  - KO: 에러 메시지에 “재시도는 3회까지”라는 지시를 포함해 반환합니다.
  - EN: Return an error message that includes the instruction "Retry up to 3 times."

## CCAR-F-Udemy06-0010

**JA** あるゲーム開発会社のツールチームは、エンジニアがClaude Codeからゲーム内アセットの管理システムを操作できるよう、社内のMCPサーバーasset-pipelineを用意しました。このサーバーはチーム全員で使い、接続には各自のアクセストークンが必要です。

一方、あるエンジニアは、自作のプロファイラー連携用のMCPサーバーを試験的に使っており、まだチームに共有する段階ではありません。

これらのMCPサーバーの設定方法として適切なものはどれですか。（2つ選択してください。）

**KO** 한 게임 개발 회사의 도구팀은 엔지니어가 Claude Code에서 게임 내 애셋 관리 시스템을 조작할 수 있도록 사내 MCP server asset-pipeline을 마련했습니다. 이 server는 팀 전원이 사용하며, 연결하려면 각자의 액세스 토큰이 필요합니다.

한편 한 엔지니어는 직접 만든 프로파일러 연동용 MCP server를 시험 삼아 쓰고 있으며, 아직 팀에 공유할 단계는 아닙니다.

이 MCP server들을 설정하는 방법으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: プロファイラー連携のサーバーも.mcp.jsonに定義し、個人用であることをサーバー名に含めてコミットする。
  - KO: 프로파일러 연동 server도 .mcp.json에 정의하고, 개인용이라는 것을 server 이름에 넣어 commit합니다.
  - EN: Also define the profiler-integration server in .mcp.json and commit it, including in the server name that it is for personal use.
- B. JA: asset-pipelineは.mcp.jsonに定義し、各自のトークンをそのまま書き込んだうえで.gitignoreに追加する。
  - KO: asset-pipeline은 .mcp.json에 정의하고, 각자의 토큰을 그대로 적은 뒤 .gitignore에 추가합니다.
  - EN: Define asset-pipeline in .mcp.json, write each person's token into it as is, and add the file to .gitignore.
- C. JA: プロファイラー連携のサーバーは、claude mcp add --scope userでユーザースコープに追加する。
  - KO: 프로파일러 연동 server는 claude mcp add --scope user로 user scope에 추가합니다.
  - EN: Add the profiler-integration server at user scope with claude mcp add --scope user.
- D. JA: asset-pipelineは.mcp.jsonに定義し、トークンは${ASSET_API_TOKEN}で参照してコミットする。
  - KO: asset-pipeline은 .mcp.json에 정의하고, 토큰은 ${ASSET_API_TOKEN}으로 참조해 commit합니다.
  - EN: Define asset-pipeline in .mcp.json, reference the token with ${ASSET_API_TOKEN}, and commit it.

## CCAR-F-Udemy06-0011

**JA** ある飲食チェーンの本部は、マルチエージェントリサーチシステムを使って、主要都市での新業態の出店候補を調べるレポートを作成しています。コーディネーターは、ウェブ検索サブエージェントと文書分析サブエージェントの結果を受け取ったあと、統合サブエージェントに「これまでの調査結果をもとに、出店候補の比較レポートを作成して」とだけ指示しています。

統合サブエージェントが返したレポートは「前述の調査によれば」といった表現ばかりで、具体的な数値や出典がほとんど含まれていませんでした。

統合サブエージェントに適切な情報を渡すための変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 외식 체인 본부는 multi-agent 리서치 시스템으로, 주요 도시에서 새 업태 매장의 출점 후보지를 조사하는 보고서를 만들고 있습니다. coordinator는 웹 검색 subagent와 문서 분석 subagent의 결과를 받은 뒤, 통합 subagent에게 “지금까지의 조사 결과를 바탕으로 출점 후보지 비교 보고서를 작성해 줘”라고만 지시합니다.

통합 subagent가 반환한 보고서는 “앞서 언급한 조사에 따르면” 같은 표현뿐이었고, 구체적인 수치나 출처는 거의 없었습니다.

통합 subagent에게 적절한 정보를 전달하기 위한 변경으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: 調査結果を本文と、ソースURLや文書名、ページ番号などのメタデータに分けた構造化データで渡す。
  - KO: 조사 결과를 본문과, 출처 URL·문서명·페이지 번호 같은 metadata로 나눈 구조화 데이터로 전달합니다.
  - EN: Pass the findings as structured data, separated into the body text and metadata such as source URLs, document names, and page numbers.
- B. JA: ウェブ検索と文書分析のツールを統合サブエージェントにも与え、必要な情報を自分で集めさせる。
  - KO: 웹 검색과 문서 분석 도구를 통합 subagent에게도 주고, 필요한 정보를 스스로 모으게 합니다.
  - EN: Give the synthesis subagent the web search and document analysis tools as well, and have it gather the information it needs by itself.
- C. JA: コーディネーターの会話履歴を参照するよう、統合サブエージェントのシステムプロンプトに書き加える。
  - KO: coordinator의 대화 기록을 참조하라는 내용을 통합 subagent의 system prompt에 덧붙입니다.
  - EN: Add to the synthesis subagent's system prompt an instruction to refer to the coordinator's conversation history.
- D. JA: ウェブ検索と文書分析の調査結果を、統合サブエージェントを起動するプロンプトに直接含める。
  - KO: 웹 검색과 문서 분석의 조사 결과를, 통합 subagent를 실행하는 prompt에 직접 포함합니다.
  - EN: Include the web search and document analysis findings directly in the prompt that launches the synthesis subagent.

## CCAR-F-Udemy06-0012

**JA** ある産業機械メーカーの開発チームは、工場の設備監視システムの保守にClaude Codeを使っています。今週は次の2つの作業があります。

サポートが終了するPLC通信ライブラリを新しいライブラリに置き換える作業（約60ファイルに影響し、接続のリトライやタイムアウトの扱いが新旧のライブラリで異なる）

温度センサーの設定画面で、入力値が上限を超えたときにエラーを表示するバリデーションを1つ追加する作業（変更箇所は特定済み）

それぞれの作業に最も適した進め方はどれですか。（2つ選択してください。）

**KO** 한 산업기계 제조사의 개발팀은 공장 설비 모니터링 시스템 유지보수에 Claude Code를 사용하고 있습니다. 이번 주에는 다음 2가지 작업이 있습니다.

지원이 종료되는 PLC 통신 라이브러리를 새 라이브러리로 교체하는 작업(약 60개 파일에 영향을 주며, 연결 재시도와 timeout 처리 방식이 기존 라이브러리와 새 라이브러리에서 다름)

온도 센서 설정 화면에, 입력값이 상한을 넘으면 에러를 표시하는 검증을 하나 추가하는 작업(변경할 위치는 이미 특정함)

각 작업에 가장 알맞은 진행 방식은 무엇입니까? (2개를 고르십시오.)

- A. JA: ライブラリの置き換えは、プランモードで影響範囲と移行方針を計画し、承認後に直接実行で進める。
  - KO: 라이브러리 교체는 plan mode에서 영향 범위와 마이그레이션 방침을 계획하고, 승인한 뒤 직접 실행으로 진행합니다.
  - EN: For the library replacement, use plan mode to plan the scope of impact and the migration approach, and after approval proceed with direct execution.
- B. JA: バリデーションの追加は、直接実行で変更を依頼し、テストで動作を確認する。
  - KO: 검증 추가는 직접 실행으로 변경을 요청하고, 테스트로 동작을 확인합니다.
  - EN: For adding the validation, request the change with direct execution and confirm the behavior with tests.
- C. JA: バリデーションの追加も、作業手順をそろえる目的でプランモードの計画を作り、承認してから実装する。
  - KO: 검증 추가도 작업 절차를 통일하기 위해 plan mode로 계획을 만들고, 승인한 뒤 구현합니다.
  - EN: For adding the validation as well, create a plan in plan mode to standardize the work procedure, and implement after approving it.
- D. JA: ライブラリの置き換えは、直接実行でディレクトリごとに書き換え、ビルドが壊れたら/rewindで戻す。
  - KO: 라이브러리 교체는 직접 실행으로 디렉터리별로 고쳐 쓰고, 빌드가 깨지면 /rewind로 되돌립니다.
  - EN: For the library replacement, use direct execution to rewrite directory by directory, and use /rewind to go back if the build breaks.

## CCAR-F-Udemy06-0013

**JA** ある電力会社のシステム部門は、需給管理システムのリポジトリで、Claude Codeによる自動コードレビューをCIに組み込んでいます。レビューの指摘は、明らかなバグについては精度が高い一方で、「タイムアウト値のハードコード」や「例外を握りつぶすtry/except」など、状況によっては許容されるパターンの判定が実行ごとにばらついています。

チームは改善のため、典型的なバグの指摘例40件をfew-shotの例としてプロンプトに追加しました。しかし、ばらつきは改善せず、1回あたりの入力トークンが約2倍に増えました。

判定の一貫性を高めるために最も効果的な変更はどれですか。

**KO** 한 전력 회사의 시스템 부문은 수급 관리 시스템 저장소에서 Claude Code를 이용한 자동 코드 리뷰를 CI에 넣어 두었습니다. 리뷰 지적은 명백한 버그에 대해서는 정확도가 높지만, “timeout 값 하드코딩”이나 “예외를 묵살하는 try/except”처럼 상황에 따라 허용되는 패턴에 대한 판정은 실행할 때마다 달라집니다.

팀은 개선을 위해 전형적인 버그 지적 예시 40개를 few-shot 예시로 prompt에 추가했습니다. 그러나 판정의 편차는 줄지 않았고, 실행 1회당 입력 토큰이 약 2배로 늘었습니다.

판정의 일관성을 높이기 위해 가장 효과적인 변경은 무엇입니까?

- A. JA: 「判断に迷うパターンは指摘しないこと」という規則を、プロンプトの冒頭に追加する。
  - KO: “판단이 애매한 패턴은 지적하지 말 것”이라는 규칙을 prompt 맨 앞에 추가합니다.
  - EN: Add a rule at the beginning of the prompt saying "Do not flag patterns you are unsure about."
- B. JA: 許容されるパターンかどうかの判定を、指摘ごとに3回実行して多数決で決める。
  - KO: 허용되는 패턴인지에 대한 판정을 지적마다 3회 실행해 다수결로 정합니다.
  - EN: Run the judgment of whether a pattern is acceptable three times for each finding and decide by majority vote.
- C. JA: few-shotの例をさらに80件に増やし、許容されるパターンの例もその中に含めて網羅する。
  - KO: few-shot 예시를 80개로 더 늘리고, 허용되는 패턴의 예시도 그 안에 넣어 빠짐없이 다룹니다.
  - EN: Increase the few-shot examples by another 80, including examples of acceptable patterns among them, to be comprehensive.
- D. JA: 40件の例を、判断の分かれるケースで指摘する・しないの理由を示した少数の例に置き換える。
  - KO: 40개의 예시를, 판단이 갈리는 사례에서 지적하는 이유와 지적하지 않는 이유를 보여 주는 소수의 예시로 바꿉니다.
  - EN: Replace the 40 examples with a small number of examples that show the reasons for flagging or not flagging in cases where judgments differ.

## CCAR-F-Udemy06-0014

**JA** ある電力会社の経営企画部は、マルチエージェントリサーチシステムを使って、国内の家庭用蓄電池の普及状況を調べるレポートを作成しています。

文書分析サブエージェントが、2つの信頼できる情報源から、家庭用蓄電池の累計導入件数として次の異なる値を抽出しました。

政府の統計では約45万件

業界団体の報告書では約62万件

統合サブエージェントは、新しそうに見えた業界団体の値だけを採用してレポートに記載しており、2つの値の調査時点が異なる可能性は検討されていませんでした。

この問題に対処する変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 전력 회사의 경영기획부는 multi-agent 리서치 시스템으로, 국내 가정용 축전지 보급 현황을 조사하는 보고서를 만들고 있습니다.

문서 분석 subagent가 신뢰할 수 있는 두 정보원에서 가정용 축전지 누적 도입 건수로 다음과 같이 서로 다른 값을 추출했습니다.

정부 통계: 약 45만 건

업계 단체 보고서: 약 62만 건

통합 subagent는 더 최신으로 보인 업계 단체의 값만 채택해 보고서에 적었고, 두 값의 조사 시점이 다를 가능성은 검토하지 않았습니다.

이 문제에 대처하는 변경으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: 統合サブエージェントに、より権威のある政府の統計の値を優先して採用する規則を与える。
  - KO: 통합 subagent에게, 더 권위 있는 정부 통계 값을 우선 채택하라는 규칙을 줍니다.
  - EN: Give the synthesis subagent a rule to prioritize and adopt the value from the more authoritative government statistics.
- B. JA: 2つの値の平均をとり、「約53.5万件」という1つの値にまとめてレポートに記載させる。
  - KO: 두 값의 평균을 내어 “약 53.5만 건”이라는 하나의 값으로 보고서에 적게 합니다.
  - EN: Take the average of the two values and have the report state a single value of "about 535,000."
- C. JA: サブエージェントに、各値の公開日とデータの収集日を構造化出力に含めさせる。
  - KO: subagent가 각 값의 공개일과 데이터 수집일을 구조화 출력에 포함하게 합니다.
  - EN: Have the subagent include each value's publication date and data collection date in its structured output.
- D. JA: 矛盾する値は一方を選ばず、それぞれの出典を付けて併記し、矛盾していることを注記させる。
  - KO: 상충하는 값은 한쪽을 고르지 않고 각각의 출처를 붙여 함께 적고, 상충한다는 사실을 주석으로 달게 합니다.
  - EN: Do not pick one of the conflicting values; have the report list both with their respective sources and note that they conflict.

## CCAR-F-Udemy06-0015

**JA** あるセキュリティ企業の脅威インテリジェンスチームは、マルチエージェントリサーチシステムを使って、特定の攻撃グループに関する週次レポートを作成しています。

今週の実行では、8つの情報源カテゴリのうち、有償の脅威フィードがタイムアウトし、脆弱性データベースは権限エラーで参照できませんでした。サブエージェントはこれらの失敗を構造化されたエラーとしてコーディネーターに報告しました。しかし、最終レポートはいつもと同じ体裁で作られ、利用できた6カテゴリの情報だけで書かれていることが、読み手にはわかりませんでした。

読み手が結論の確かさを正しく判断できるようにするための変更として最も適切なものはどれですか。

**KO** 한 보안 기업의 위협 인텔리전스팀은 multi-agent 리서치 시스템으로, 특정 공격 그룹에 관한 주간 보고서를 만들고 있습니다.

이번 주 실행에서는 8개 정보원 카테고리 중 유료 위협 피드가 timeout되었고, 취약점 데이터베이스는 권한 에러로 조회하지 못했습니다. subagent는 이 실패들을 구조화된 에러로 coordinator에게 보고했습니다. 그러나 최종 보고서는 평소와 같은 형식으로 만들어졌고, 이용할 수 있었던 6개 카테고리의 정보만으로 작성되었다는 사실을 독자는 알 수 없었습니다.

독자가 결론의 확실성을 올바르게 판단할 수 있게 하는 변경으로 가장 적절한 것은 무엇입니까?

- A. JA: 参照できなかった2カテゴリについては、前週のレポートの記述をそのまま引き継いで記載する。
  - KO: 조회하지 못한 2개 카테고리는 지난주 보고서의 서술을 그대로 이어받아 적습니다.
  - EN: For the two categories that could not be accessed, carry over the previous week's report text as is.
- B. JA: タイムアウトと権限エラーが解消するまで、サブエージェントにリトライを繰り返させてから統合する。
  - KO: timeout과 권한 에러가 해소될 때까지 subagent에게 재시도를 반복하게 한 뒤 통합합니다.
  - EN: Have the subagents retry repeatedly until the timeout and permission errors are resolved, and then synthesize.
- C. JA: いずれかの情報源カテゴリが失敗した場合は、レポートの作成を中止して翌週の実行まで待つ。
  - KO: 정보원 카테고리 중 하나라도 실패하면 보고서 작성을 중단하고 다음 주 실행까지 기다립니다.
  - EN: If any source category fails, abort report creation and wait until the next week's run.
- D. JA: 統合の出力に、裏付けの十分な結果と情報源が欠けた領域を示すカバレッジの注記を付ける。
  - KO: 통합 결과에, 근거가 충분한 결과와 정보원이 빠진 영역을 보여 주는 coverage 주석을 붙입니다.
  - EN: Attach a coverage note to the synthesis output indicating which areas have well-supported results and which areas lack sources.

## CCAR-F-Udemy06-0016

**JA** ある半導体メーカーの設計自動化チームは、Claude Codeを使ってEDAツール向けのスクリプトを生成しています。タイミング解析のフローだけで使う規約（クロック制約の書き方や、解析レポートのファイル名の付け方など）を、timing/ディレクトリに置いたCLAUDE.mdに書いてコミットしました。チームのエンジニアは普段からリポジトリのルートでClaude Codeを起動し、合成や配置配線のフローも含めて作業しています。

あるエンジニアがルートでClaude Codeを起動して/contextを実行したところ、Memory filesの一覧にはルートのCLAUDE.mdだけが表示され、timing/CLAUDE.mdは表示されませんでした。このエンジニアは「timing/CLAUDE.mdが読み込まれていない」とチームに報告しています。

この報告を受けて、次に取るべき対応として最も適切なものはどれですか。

**KO** 한 반도체 제조사의 설계 자동화팀은 Claude Code로 EDA 도구용 스크립트를 생성하고 있습니다. 타이밍 분석 흐름에서만 쓰는 규칙(클럭 제약을 작성하는 방법, 분석 리포트 파일명을 붙이는 방법 등)을 timing/ 디렉터리에 둔 CLAUDE.md에 적어 commit했습니다. 팀의 엔지니어들은 평소 저장소 루트에서 Claude Code를 시작하고, 합성이나 배치·배선 흐름까지 포함해 작업합니다.

한 엔지니어가 루트에서 Claude Code를 시작해 /context를 실행했더니, Memory files 목록에는 루트의 CLAUDE.md만 표시되고 timing/CLAUDE.md는 표시되지 않았습니다. 이 엔지니어는 “timing/CLAUDE.md가 로드되지 않는다”라고 팀에 보고했습니다.

이 보고를 받고 다음에 취해야 할 대응으로 가장 적절한 것은 무엇입니까?

- A. JA: timing/CLAUDE.mdの内容をルートのCLAUDE.mdに移し、/contextの一覧に表示されることを確かめる。
  - KO: timing/CLAUDE.md의 내용을 루트 CLAUDE.md로 옮기고, /context 목록에 표시되는지 확인합니다.
  - EN: Move the contents of timing/CLAUDE.md into the root CLAUDE.md and confirm that they appear in the /context list.
- B. JA: timing/にあるファイルをClaudeに読ませ、その時点でtiming/CLAUDE.mdが読み込まれるかを見る。
  - KO: timing/에 있는 파일을 Claude에게 읽게 하고, 그 시점에 timing/CLAUDE.md가 로드되는지 봅니다.
  - EN: Have Claude read a file under timing/ and see whether timing/CLAUDE.md is loaded at that point.
- C. JA: timing/CLAUDE.mdを.claude/rules/timing.mdに移し、pathsに"timing/**/*"を指定する。
  - KO: timing/CLAUDE.md를 .claude/rules/timing.md로 옮기고, paths에 "timing/**/*"를 지정합니다.
  - EN: Move timing/CLAUDE.md to .claude/rules/timing.md and specify "timing/**/*" in paths.
- D. JA: ルートのCLAUDE.mdに@timing/CLAUDE.mdを書き、起動時に取り込まれるようにする。
  - KO: 루트 CLAUDE.md에 @timing/CLAUDE.md를 적어, 시작할 때 불러오게 합니다.
  - EN: Write @timing/CLAUDE.md in the root CLAUDE.md so that it is imported at startup.

## CCAR-F-Udemy06-0017

**JA** ある通信事業者の開発チームは、料金計算システムのリポジトリでClaude Codeを使っています。ルートのCLAUDE.mdは、4つのチームが書き足してきた結果1,200行を超え、ネットワーク設定、課金API、リリース手順、テストの規約が1つのファイルに混在しています。

最近は、次の問題が起きています。

同じファイルへの同時編集で、マージの競合が頻繁に起きる

Claudeがファイルの後半に書かれた規約を守らないケースが増えている

この状況を改善する変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 통신 사업자의 개발팀은 요금 계산 시스템 저장소에서 Claude Code를 사용하고 있습니다. 루트의 CLAUDE.md는 4개 팀이 계속 내용을 덧붙인 결과 1,200줄을 넘었고, 네트워크 설정, 과금 API, 릴리스 절차, 테스트 규칙이 한 파일에 뒤섞여 있습니다.

최근에는 다음과 같은 문제가 생기고 있습니다.

같은 파일을 동시에 편집해 머지 충돌이 자주 일어납니다

Claude가 파일 후반부에 적힌 규칙을 지키지 않는 경우가 늘고 있습니다

이 상황을 개선하는 변경으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: CLAUDE.mdの内容を各エンジニアの~/.claude/CLAUDE.mdに分けて移し、チームごとに必要な部分だけを持たせる。
  - KO: CLAUDE.md의 내용을 각 엔지니어의 ~/.claude/CLAUDE.md로 나눠 옮기고, 팀별로 필요한 부분만 갖게 합니다.
  - EN: Split the contents of CLAUDE.md into each engineer's ~/.claude/CLAUDE.md, so that each team holds only the parts it needs.
- B. JA: 規約をトピックごとに分け、.claude/rules/のbilling-api.mdなどのファイルにする。
  - KO: 규칙을 주제별로 나눠 .claude/rules/ 아래 billing-api.md 같은 파일로 만듭니다.
  - EN: Split the conventions by topic into files such as billing-api.md under .claude/rules/.
- C. JA: ルートのCLAUDE.mdには、プロジェクト全体に関わる最小限の内容だけを残す。
  - KO: 루트 CLAUDE.md에는 프로젝트 전체에 관련된 최소한의 내용만 남깁니다.
  - EN: Leave only the minimum content that concerns the whole project in the root CLAUDE.md.
- D. JA: すべての規約をスキルに移し、作業のたびに開発者が該当するスキルを呼び出して読み込ませる。
  - KO: 모든 규칙을 skill로 옮기고, 작업할 때마다 개발자가 해당 skill을 호출해 로드하게 합니다.
  - EN: Move all conventions into skills, and have developers invoke the relevant skill to load it each time they work.

## CCAR-F-Udemy06-0018

**JA** ある新聞社のデータ報道チームは、マルチエージェントリサーチシステムを使って、過去の報道を踏まえた解説記事の下調べをしています。検索サブエージェントには、ウェブを検索するsearch_webと、新たに追加したsearch_archive（説明は「アーカイブを検索する」）があります。

search_archiveは、自社が1990年から2015年に掲載した紙面記事の全文を検索できるツールですが、追加から1か月の間、ほとんど呼ばれていませんでした。2015年以前の自社の報道に関する調査でも、エージェントはsearch_webで他社の記事を探しています。

search_archiveが適切に選ばれるようにするための変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 신문사의 데이터 저널리즘팀은 multi-agent 리서치 시스템으로, 과거 보도를 바탕으로 한 해설 기사의 사전 조사를 하고 있습니다. 검색 subagent에게는 웹을 검색하는 search_web과, 새로 추가한 search_archive(설명은 “아카이브를 검색한다”)가 있습니다.

search_archive는 자사가 1990년부터 2015년까지 게재한 지면 기사의 전문을 검색할 수 있는 도구인데, 추가 후 한 달 동안 거의 호출되지 않았습니다. 2015년 이전 자사 보도에 관한 조사에서도 agent는 search_web으로 다른 언론사의 기사를 찾고 있습니다.

search_archive가 적절히 선택되게 하는 변경으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: search_archiveの名前を、収録範囲が分かるsearch_own_archive_1990_2015に変える。
  - KO: search_archive의 이름을, 수록 범위를 알 수 있는 search_own_archive_1990_2015로 바꿉니다.
  - EN: Rename search_archive to search_own_archive_1990_2015, which makes its coverage clear.
- B. JA: search_archiveの説明に、収録範囲（1990〜2015年の自社紙面）と検索語の例を書く。
  - KO: search_archive의 설명에 수록 범위(1990~2015년 자사 지면)와 검색어 예시를 적습니다.
  - EN: In the description of search_archive, write its coverage (the company's own print editions from 1990 to 2015) and examples of search terms.
- C. JA: tool_choiceを{"type": "any"}にして、検索のたびにいずれかのツールを呼ばせる。
  - KO: tool_choice를 {"type": "any"}로 설정해, 검색할 때마다 어느 하나의 도구를 호출하게 합니다.
  - EN: Set tool_choice to {"type": "any"} so that the agent calls one of the tools on every search.
- D. JA: 検索サブエージェントのsearch_webを一時的に無効にし、search_archiveを優先して使わせる。
  - KO: 검색 subagent의 search_web을 일시적으로 비활성화하고, search_archive를 우선 사용하게 합니다.
  - EN: Temporarily disable search_web for the search subagent so that it uses search_archive preferentially.

## CCAR-F-Udemy06-0019

**JA** ある情報セキュリティ企業は、マルチエージェントリサーチシステムを使って、特定の業界を狙うサイバー攻撃の傾向を四半期ごとにまとめています。12の検索サブエージェントの結果を連結して統合サブエージェントに渡しており、入力は約8万トークンになります。

完成したレポートを確認すると、入力の冒頭と末尾に置かれたサブエージェントの調査結果はよく反映されている一方で、5番目から8番目のサブエージェントが報告した重要な攻撃手法が抜け落ちていました。

統合サブエージェントへの入力の構成を改善する方法として適切なものはどれですか。（2つ選択してください。）

**KO** 한 정보보안 기업은 multi-agent 리서치 시스템으로, 특정 업계를 노리는 사이버 공격의 동향을 분기마다 정리하고 있습니다. 12개 검색 subagent의 결과를 이어 붙여 통합 subagent에게 전달하는데, 입력은 약 8만 토큰이 됩니다.

완성된 보고서를 확인해 보니, 입력의 앞부분과 끝부분에 놓인 subagent의 조사 결과는 잘 반영되었지만, 5번째부터 8번째 subagent가 보고한 중요한 공격 기법은 빠져 있었습니다.

통합 subagent에 대한 입력 구성을 개선하는 방법으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: 統合サブエージェントのmax_tokensを増やし、より長いレポートを出力させる。
  - KO: 통합 subagent의 max_tokens를 늘려, 더 긴 보고서를 출력하게 합니다.
  - EN: Increase the synthesis subagent's max_tokens so that it outputs a longer report.
- B. JA: 入力の冒頭に、各サブエージェントの主要な調査結果の要約を置く。
  - KO: 입력 맨 앞에 각 subagent의 주요 조사 결과 요약을 둡니다.
  - EN: Place a summary of each subagent's key findings at the beginning of the input.
- C. JA: 12の結果の並び順を実行のたびに無作為に入れ替え、特定の結果が毎回中間に来ない状態にする。
  - KO: 12개 결과의 순서를 실행할 때마다 무작위로 섞어, 특정 결과가 매번 중간에 오지 않게 합니다.
  - EN: Randomly shuffle the order of the 12 results on every run so that no particular result ends up in the middle every time.
- D. JA: 詳細な結果を、サブエージェントやトピックごとに明示的なセクション見出しで整理する。
  - KO: 상세한 결과를 subagent별 또는 주제별로 명시적인 섹션 제목을 붙여 정리합니다.
  - EN: Organize the detailed results with explicit section headings by subagent or topic.

## CCAR-F-Udemy06-0020

**JA** ある不動産管理会社は、Claudeを使って、賃貸借契約書から賃料・共益費・駐車場代・月額合計を抽出し、家賃管理システムに登録しています。抽出には、入力をJSONスキーマで定義した抽出ツールを使っており、出力がJSONとして解析できないエラーは発生していません。

ところが、抽出結果の約4%で、次のような誤りがありました。

月額合計が各項目の合計と一致しない

共益費の金額が賃料のフィールドに入っている

担当者は「ツールの定義にstrict: trueを追加すれば解決する」と提案しています。

この問題への対処として最も適切なものはどれですか。

**KO** 한 부동산 관리 회사는 Claude로 임대차 계약서에서 임대료·관리비·주차비·월 합계를 추출해 임대료 관리 시스템에 등록하고 있습니다. 추출에는 입력을 JSON schema로 정의한 추출 도구를 쓰고 있으며, 출력을 JSON으로 파싱할 수 없는 에러는 발생하지 않습니다.

그런데 추출 결과의 약 4%에서 다음과 같은 오류가 있었습니다.

월 합계가 각 항목의 합과 일치하지 않습니다

관리비 금액이 임대료 필드에 들어가 있습니다

담당자는 “도구 정의에 strict: true를 추가하면 해결된다”라고 제안하고 있습니다.

이 문제에 대한 대처로 가장 적절한 것은 무엇입니까?

- A. JA: 月額合計のフィールドをスキーマから削除し、登録するときにシステム側で合計を計算する。
  - KO: 월 합계 필드를 schema에서 삭제하고, 등록할 때 시스템 쪽에서 합계를 계산합니다.
  - EN: Remove the monthly total field from the schema and have the system calculate the total when registering.
- B. JA: 抽出後にコードで合計を照合し、不一致があれば具体的な検証エラーを添えて再抽出させる。
  - KO: 추출 후 코드로 합계를 대조하고, 불일치가 있으면 구체적인 검증 에러를 붙여 다시 추출하게 합니다.
  - EN: After extraction, check the total in code, and if there is a mismatch, have Claude re-extract with a specific validation error attached.
- C. JA: 同じ契約書の抽出を2回実行し、2回の結果が一致した項目に限って登録する。
  - KO: 같은 계약서의 추출을 2번 실행하고, 두 결과가 일치한 항목만 등록합니다.
  - EN: Run the extraction of the same agreement twice, and register only the items on which the two results match.
- D. JA: 担当者の提案どおりツールの定義にstrict: trueを追加し、出力をスキーマに厳密に従わせる。
  - KO: 담당자의 제안대로 도구 정의에 strict: true를 추가해, 출력이 schema를 엄격하게 따르게 합니다.
  - EN: Follow the person in charge's proposal, adding strict: true to the tool definition to make the output strictly follow the schema.

## CCAR-F-Udemy06-0021

**JA** ある市役所の情報システム課は、住民税の計算システムの保守にClaude Codeを使い、CI/CDパイプラインでコードの生成とレビューを自動化しています。現在のパイプラインでは、Claudeが課題に応じてコードを生成したあと、同じセッションで「あなたの変更をレビューし、問題があれば指摘して」と依頼しています。

しかし、本番で見つかった税額の端数処理の不具合3件は、いずれもこのレビューで「問題なし」とされていました。チームは拡張思考の予算を増やしてレビューを再実行しましたが、結果は変わりませんでした。

レビューで見つけにくい問題を検出しやすくするための変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 시청의 정보시스템과는 주민세 계산 시스템 유지보수에 Claude Code를 사용하고, CI/CD pipeline에서 코드 생성과 리뷰를 자동화하고 있습니다. 현재 pipeline에서는 Claude가 이슈에 맞춰 코드를 생성한 뒤, 같은 session에서 “당신의 변경을 리뷰하고 문제가 있으면 지적해 줘”라고 요청합니다.

그러나 운영 환경에서 발견된 세액 끝수 처리 결함 3건은 모두 이 리뷰에서 “문제없음”으로 판정되었습니다. 팀은 extended thinking 예산을 늘려 리뷰를 다시 실행했지만 결과는 달라지지 않았습니다.

리뷰에서 찾기 어려운 문제를 더 쉽게 잡아내기 위한 변경으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: 同じセッションで、生成したコードに対するレビューを3回繰り返させ、毎回異なる観点を指定する。
  - KO: 같은 session에서 생성한 코드에 대한 리뷰를 3번 반복하게 하고, 매번 다른 관점을 지정합니다.
  - EN: In the same session, have the generated code reviewed three times in a row, specifying a different perspective each time.
- B. JA: レビューは、生成時のセッションを引き継がない別のclaude -pの実行として、差分を渡して行う。
  - KO: 리뷰는 생성 때의 session을 이어받지 않는 별도의 claude -p 실행으로, diff를 전달해 수행합니다.
  - EN: Run the review as a separate claude -p execution that does not carry over the generation session, passing the diff to it.
- C. JA: 生成したセッションを--resumeで再開し、レビューの指示をより厳しい表現に書き換えて再度依頼する。
  - KO: 생성한 session을 --resume으로 재개하고, 리뷰 지시를 더 엄격한 표현으로 고쳐 다시 요청합니다.
  - EN: Resume the generation session with --resume, rewrite the review instruction in stricter wording, and ask again.
- D. JA: 独立したレビューでは、CLAUDE.mdに記載した税額計算のレビュー基準に沿って判断させる。
  - KO: 독립된 리뷰에서는 CLAUDE.md에 적어 둔 세액 계산 리뷰 기준에 따라 판단하게 합니다.
  - EN: In the independent review, have it make its judgments according to the tax calculation review criteria written in CLAUDE.md.

## CCAR-F-Udemy06-0022

**JA** ある旅館・ホテルの業界団体は、マルチエージェントリサーチシステムを使って、地方の宿泊施設の人手不足対策に関するレポートを作成しています。調査の依頼では、採用、定着、業務の自動化、外国人材の活用、賃金、地域連携の6つの観点を必ず含めるよう指定しています。

現在のコーディネーターは、検索と文書分析のサブエージェントに作業を委任し、統合サブエージェントの出力をそのまま最終レポートにしています。しかし、完成したレポートで外国人材の活用と地域連携の観点がほとんど扱われていないことがありました。

コーディネーターの改善として最も適切なものはどれですか。

**KO** 한 료칸·호텔 업계 단체는 multi-agent 리서치 시스템으로, 지방 숙박시설의 인력 부족 대책에 관한 보고서를 만들고 있습니다. 조사 요청에서는 채용, 정착, 업무 자동화, 외국인 인력 활용, 임금, 지역 연계의 6가지 관점을 반드시 포함하도록 지정했습니다.

현재 coordinator는 검색과 문서 분석 subagent에게 작업을 위임하고, 통합 subagent의 출력을 그대로 최종 보고서로 삼습니다. 그러나 완성된 보고서에서 외국인 인력 활용과 지역 연계 관점이 거의 다뤄지지 않은 경우가 있었습니다.

coordinator의 개선으로 가장 적절한 것은 무엇입니까?

- A. JA: 検索サブエージェントの検索結果の上限件数を2倍に増やし、より多くの情報源を集めさせる。
  - KO: 검색 subagent의 검색 결과 상한 건수를 2배로 늘려 더 많은 정보원을 모으게 합니다.
  - EN: Double the maximum number of search results for the search subagent so that it gathers more sources.
- B. JA: 統合サブエージェントに、情報が不足する観点を「データなし」と明記させてから出力させる。
  - KO: 통합 subagent에게, 정보가 부족한 관점은 “데이터 없음”이라고 명시한 뒤 출력하게 합니다.
  - EN: Have the synthesis subagent explicitly state "no data" for perspectives with insufficient information before it produces its output.
- C. JA: 統合の出力を観点ごとに評価し、不足があれば的を絞って再委任し、統合をやり直させる。
  - KO: 통합 결과를 관점별로 평가하고, 부족한 부분이 있으면 범위를 좁혀 다시 위임한 뒤 통합을 다시 하게 합니다.
  - EN: Evaluate the synthesis output perspective by perspective, and if there are gaps, re-delegate with a narrowed focus and redo the synthesis.
- D. JA: 統合サブエージェントにウェブ検索のツールを与え、不足する観点を自分で調べて補わせる。
  - KO: 통합 subagent에게 웹 검색 도구를 주고, 부족한 관점을 스스로 조사해 보완하게 합니다.
  - EN: Give the synthesis subagent a web search tool and have it investigate and fill in the missing perspectives by itself.

## CCAR-F-Udemy06-0023

**JA** ある家電メーカーの商品企画部門は、マルチエージェントリサーチシステムを構築しています。コーディネーターエージェントが市場動向の調査をサブエージェントに委任し、出典付きのレポートを作成します。

コーディネーターのエージェントループはClaude APIで独自に実装しており、現在は次の仕組みで終了します。

応答にテキストブロックが含まれていれば、最終回答とみなして終了する

それとは別に、8回の反復で必ず打ち切る

テストでは、調査の途中でループが終了し、実行されていないツール呼び出しが残ったまま、不完全なレポートが返されるケースが見つかりました。

ループの制御を見直す変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 가전 제조사의 상품기획 부문은 multi-agent 리서치 시스템을 구축하고 있습니다. coordinator agent가 시장 동향 조사를 subagent에게 위임하고, 출처가 달린 보고서를 작성합니다.

coordinator의 agent loop는 Claude API로 직접 구현했으며, 현재는 다음 방식으로 종료합니다.

응답에 텍스트 블록이 포함되어 있으면 최종 답변으로 간주하고 종료합니다

이와 별도로, 8회 반복하면 무조건 중단합니다

테스트에서 조사 도중에 loop가 종료되어, 실행되지 않은 도구 호출이 남은 채로 불완전한 보고서가 반환되는 경우가 발견되었습니다.

loop 제어를 재검토하는 변경으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: 反復回数の上限は暴走を止める安全策として残し、通常の終了判定には使わない。
  - KO: 반복 횟수 상한은 폭주를 막는 안전장치로 남기고, 일반적인 종료 판정에는 쓰지 않습니다.
  - EN: Keep the iteration limit as a safety measure to stop runaway behavior, and do not use it for normal termination decisions.
- B. JA: stop_reasonがtool_useなら続行し、end_turnなら終了する。
  - KO: stop_reason이 tool_use이면 계속하고, end_turn이면 종료합니다.
  - EN: Continue if stop_reason is tool_use, and terminate if it is end_turn.
- C. JA: アシスタントの応答テキストに「調査完了」という語が含まれた時点で、ループを終了する。
  - KO: assistant의 응답 텍스트에 “조사 완료”라는 말이 포함된 시점에 loop를 종료합니다.
  - EN: Terminate the loop at the point when the assistant's response text contains the phrase "research complete."
- D. JA: 反復回数の上限を8回から30回に引き上げ、上限に達した時点の応答をそのまま最終回答とする。
  - KO: 반복 횟수 상한을 8회에서 30회로 올리고, 상한에 도달한 시점의 응답을 그대로 최종 답변으로 삼습니다.
  - EN: Raise the iteration limit from 8 to 30, and use the response at the point the limit is reached as the final answer as is.

## CCAR-F-Udemy06-0024

**JA** あるSaaS企業の分析チームは、Claude Agent SDKを使ってマルチエージェントリサーチシステムを構築しています。検索サブエージェントは、社内の利用ログ基盤と外部の業界レポートを検索するMCPツールを使います。

1週間分のログを分析したところ、次のことがわかりました。

ツールのエラーは1,200件あり、そのうち約70%は存在しないワークスペースIDを指定したことによる失敗で、残りは利用ログ基盤のタイムアウトだった

ツールはどの失敗でもisError: trueと「Operation failed」だけを返していた

エージェントはすべての失敗を同じ入力のまま3回ずつリトライしていた

タイムアウトの多くは1回のリトライで成功していた

無駄なリトライを減らすための変更として最も効果的なものはどれですか。

**KO** 한 SaaS 기업의 분석팀은 Claude Agent SDK로 multi-agent 리서치 시스템을 구축하고 있습니다. 검색 subagent는 사내 이용 로그 플랫폼과 외부 업계 보고서를 검색하는 MCP 도구를 사용합니다.

1주일 치 로그를 분석해 다음 사실을 알게 되었습니다.

도구 에러는 1,200건이었고, 그중 약 70%는 존재하지 않는 워크스페이스 ID를 지정해 생긴 실패였으며, 나머지는 이용 로그 플랫폼의 timeout이었습니다

도구는 어떤 실패에서든 isError: true와 “Operation failed”만 반환했습니다

agent는 모든 실패를 같은 입력 그대로 3번씩 재시도했습니다

timeout은 대부분 1번의 재시도로 성공했습니다

불필요한 재시도를 줄이기 위한 변경으로 가장 효과적인 것은 무엇입니까?

- A. JA: すべての失敗に対するリトライ回数を3回から1回に減らし、それでも失敗したらコーディネーターに伝える。
  - KO: 모든 실패에 대한 재시도 횟수를 3번에서 1번으로 줄이고, 그래도 실패하면 coordinator에게 알립니다.
  - EN: Reduce the number of retries for all failures from three to one, and if it still fails, report it to the coordinator.
- B. JA: 失敗したツール呼び出しの入力と結果をキャッシュし、同じ入力での呼び出しには前回のエラーを返す。
  - KO: 실패한 도구 호출의 입력과 결과를 캐시하고, 같은 입력의 호출에는 이전 에러를 반환합니다.
  - EN: Cache the input and result of failed tool calls, and return the previous error for calls with the same input.
- C. JA: 失敗の種類とリトライ可否を示す構造化エラーを返す。
  - KO: 실패 종류와 재시도 가능 여부를 나타내는 구조화된 에러를 반환합니다.
  - EN: Return a structured error indicating the type of failure and whether it can be retried.
- D. JA: リトライの間隔を指数バックオフにして、リトライのたびに次の呼び出しまでの待ち時間を2倍に延ばす。
  - KO: 재시도 간격을 exponential backoff로 바꿔, 재시도할 때마다 다음 호출까지의 대기 시간을 2배로 늘립니다.
  - EN: Use exponential backoff for the retry interval, doubling the wait time until the next call on each retry.

## CCAR-F-Udemy06-0025

**JA** ある化学メーカーの研究開発部門は、Claude Codeを使って、実験記録システムの古いデータを新しい形式に変換するスクリプトを作成しています。変換の要件の1つに、温度の表記をそろえる処理があります。

旧データには「25℃」「298K」「室温」「77°F」など多様な表記があり、Claudeに「温度は摂氏の数値と単位にそろえ、室温のような表記は元の文字列を残して」と文章で依頼しました。しかし、生成された変換処理は、依頼するたびに室温の扱いや小数の桁数が異なっていました。

変換の要件を一貫して伝えるための方法として最も効果的なものはどれですか。

**KO** 한 화학 제조사의 연구개발 부문은 Claude Code로, 실험 기록 시스템의 오래된 데이터를 새 형식으로 변환하는 스크립트를 만들고 있습니다. 변환 요구사항 중 하나는 온도 표기를 통일하는 처리입니다.

기존 데이터에는 “25℃”, “298K”, “실온”, “77°F” 등 다양한 표기가 있어서, Claude에게 “온도는 섭씨 수치와 단위로 통일하고, 실온 같은 표기는 원래 문자열을 남겨 줘”라고 글로 요청했습니다. 그러나 생성된 변환 처리는 요청할 때마다 실온의 처리 방식과 소수 자릿수가 달랐습니다.

변환 요구사항을 일관되게 전달하는 방법으로 가장 효과적인 것은 무엇입니까?

- A. JA: 「298K」→「24.85℃」、「室温」→「室温（未換算）」のような入出力の例を2〜3個示す。
  - KO: “298K”→“24.85℃”, “실온”→“실온(미환산)”처럼 입출력 예시를 2~3개 보여 줍니다.
  - EN: Show two or three input and output examples, such as "298K" -> "24.85℃" and "室温" -> "室温（未換算）".
- B. JA: 変換結果を確認して誤りを文章で指摘し、修正させる反復を続ける。
  - KO: 변환 결과를 확인해 오류를 글로 지적하고 고치게 하는 과정을 반복합니다.
  - EN: Continue iterating by checking the conversion results and pointing out errors in prose to have them corrected.
- C. JA: 依頼文の説明に、摂氏への換算式と、小数第2位で四捨五入する規則を文章で書き足す。
  - KO: 요청문 설명에 섭씨 환산식과, 소수 둘째 자리에서 반올림하는 규칙을 글로 덧붙입니다.
  - EN: Add to the explanation in the request, in prose, the conversion formula to Celsius and a rule to round to two decimal places.
- D. JA: CLAUDE.mdに温度表記の変換規則を箇条書きで追加し、毎回のセッションで読み込ませる。
  - KO: CLAUDE.md에 온도 표기 변환 규칙을 글머리 목록으로 추가해, 매 session에서 로드되게 합니다.
  - EN: Add the temperature notation conversion rules as a bulleted list to CLAUDE.md so that they are loaded in every session.

> notes: 원문 데이터 문자열 「室温」은 한국어 독자를 위해 “실온”으로 옮김. 보기 C의 「小数第2位で四捨五入」는 원문 그대로 '소수 둘째 자리에서 반올림'으로 옮겼으나, 보기 A의 24.85(소수 둘째 자리까지 표시)와 해석이 어긋날 수 있음(en은 'round to two decimal places').

## CCAR-F-Udemy06-0026

**JA** ある旅行会社の商品企画チームは、マルチエージェントリサーチシステムを使って、「訪日客の地方分散の動向」に関するレポートを作成しています。コーディネーターは3つの検索サブエージェントに、同じトピックの説明と同じ指示を渡して並列に調査させています。

直近10回の実行を分析したところ、次のことがわかりました。

3つのサブエージェントが返した情報源の約70%が重複している

検索にかかるトークンは、1体で調べた場合の約3倍になっている

レポートで引用される情報源の数は、ほとんど増えていない

この非効率を解消するためのコーディネーターの変更として最も適切なものはどれですか。

**KO** 한 여행사의 상품기획팀은 multi-agent 리서치 시스템으로 “방일 관광객의 지방 분산 동향”에 관한 보고서를 만들고 있습니다. coordinator는 3개의 검색 subagent에게 같은 주제 설명과 같은 지시를 전달해 병렬로 조사하게 합니다.

최근 10회 실행을 분석해 다음 사실을 알게 되었습니다.

3개 subagent가 반환한 정보원의 약 70%가 중복됩니다

검색에 드는 토큰은 하나의 agent가 조사할 때의 약 3배입니다

보고서에 인용되는 정보원 수는 거의 늘지 않았습니다

이 비효율을 없애기 위한 coordinator의 변경으로 가장 적절한 것은 무엇입니까?

- A. JA: 検索サブエージェントを1体に減らし、同じ指示のまま検索の上限件数を3倍に増やす。
  - KO: 검색 subagent를 1개로 줄이고, 같은 지시를 유지한 채 검색 상한 건수를 3배로 늘립니다.
  - EN: Reduce the search subagents to one, and triple the maximum number of search results with the same instructions.
- B. JA: 統合エージェントに、重複する情報源を除外してから調査結果を統合する手順を新たに追加する。
  - KO: 통합 agent에, 중복되는 정보원을 제외한 뒤 조사 결과를 통합하는 단계를 새로 추가합니다.
  - EN: Add a new step for the synthesis agent to exclude duplicate sources before synthesizing the findings.
- C. JA: 各サブエージェントに、コーディネーターの会話履歴全体をプロンプトとして渡す。
  - KO: 각 subagent에게 coordinator의 대화 기록 전체를 prompt로 전달합니다.
  - EN: Pass the coordinator's entire conversation history to each subagent as its prompt.
- D. JA: サブエージェントごとに、官公庁の統計や業界レポートなど異なる情報源の種類を割り当てる。
  - KO: subagent마다 관공서 통계나 업계 보고서 등 서로 다른 정보원 유형을 할당합니다.
  - EN: Assign each subagent a different type of source, such as government statistics or industry reports.

## CCAR-F-Udemy06-0027

**JA** あるSaaS企業の開発チームは、Claude Codeで2つの調査を並行して進めています。

1つは、請求処理のバッチが特定の条件で二重請求を起こす原因の調査で、billing-dupという名前のセッションで3日前から続けています。この間、請求処理のコードには変更がありません。

もう1つは認証モジュールのパフォーマンスの調査ですが、昨日のセッションのあとに認証モジュールが大幅に書き換えられ、以前に分析したファイルの大半が変わっています。

それぞれの調査を再開する方法として適切なものはどれですか。（2つ選択してください。）

**KO** 한 SaaS 기업의 개발팀은 Claude Code로 두 가지 조사를 병행하고 있습니다.

하나는 청구 처리 batch가 특정 조건에서 이중 청구를 일으키는 원인 조사로, billing-dup이라는 이름의 session에서 3일 전부터 이어 오고 있습니다. 그동안 청구 처리 코드에는 변경이 없었습니다.

다른 하나는 인증 모듈의 성능 조사인데, 어제 session 이후 인증 모듈이 대폭 재작성되어 이전에 분석한 파일 대부분이 바뀌었습니다.

각 조사를 재개하는 방법으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: 認証モジュールの調査は、昨日のセッションを--resumeで再開し、そのまま分析の続きを依頼する。
  - KO: 인증 모듈 조사는 어제 session을 --resume으로 재개하고, 그대로 분석을 이어 가도록 요청합니다.
  - EN: For the authentication module investigation, resume yesterday's session with --resume and ask it to continue the analysis as is.
- B. JA: 二重請求の調査は、claude --resume billing-dupで名前付きセッションを再開して続ける。
  - KO: 이중 청구 조사는 claude --resume billing-dup으로 이름 붙은 session을 재개해 계속합니다.
  - EN: For the double billing investigation, resume the named session with claude --resume billing-dup and continue.
- C. JA: 認証モジュールの調査は、以前の結論を構造化したサマリーにして新しいセッションで始める。
  - KO: 인증 모듈 조사는 이전 결론을 구조화한 요약으로 만들어 새 session에서 시작합니다.
  - EN: For the authentication module investigation, turn the previous conclusions into a structured summary and start in a new session.
- D. JA: 二重請求の調査も、念のため新しいセッションで最初からコードベース全体を探索し直させる。
  - KO: 이중 청구 조사도 만일을 위해 새 session에서 처음부터 코드베이스 전체를 다시 탐색하게 합니다.
  - EN: For the double billing investigation as well, to be safe, start a new session and have it explore the entire codebase again from scratch.

## CCAR-F-Udemy06-0028

**JA** ある農業協同組合の営農支援部は、マルチエージェントリサーチシステムを使って、新しい施肥技術の効果に関するレポートを作成しています。文書分析サブエージェントは各論文の調査結果を要約してコーディネーターに返し、統合サブエージェントがそれらの要約をまとめてレポートを作ります。

完成したレポートには「この技術で収量が平均12%増加した」と書かれていました。しかし、どの論文のどの試験に基づく数値なのかを確認しようとしたところ、要約の段階で出典の情報が失われており、たどれませんでした。

出典を保持したレポートを作るための変更として最も適切なものはどれですか。

**KO** 한 농업협동조합의 영농지원부는 multi-agent 리서치 시스템으로, 새로운 시비 기술의 효과에 관한 보고서를 만들고 있습니다. 문서 분석 subagent는 각 논문의 조사 결과를 요약해 coordinator에게 반환하고, 통합 subagent가 그 요약들을 모아 보고서를 만듭니다.

완성된 보고서에는 “이 기술로 수확량이 평균 12% 증가했다”라고 적혀 있었습니다. 그러나 어느 논문의 어느 시험에 근거한 수치인지 확인하려고 했더니, 요약 단계에서 출처 정보가 사라져 추적할 수 없었습니다.

출처를 유지한 보고서를 만들기 위한 변경으로 가장 적절한 것은 무엇입니까?

- A. JA: 統合サブエージェントに、レポートの最後に参考文献の一覧を付けるよう指示する。
  - KO: 통합 subagent에게 보고서 끝에 참고문헌 목록을 붙이라고 지시합니다.
  - EN: Instruct the synthesis subagent to attach a list of references at the end of the report.
- B. JA: 各主張に情報源のURLや論文名、抜粋を対応付けた構造化データを出力させ、統合でも保持させる。
  - KO: 각 주장에 정보원의 URL, 논문명, 발췌문을 대응시킨 구조화 데이터를 출력하게 하고, 통합 단계에서도 유지하게 합니다.
  - EN: Have the subagents output structured data that maps each claim to a source URL, paper title, and excerpt, and have the synthesis retain it as well.
- C. JA: レポートの作成後に、ウェブ検索で数値の出典を探して脚注を付けるステップを追加する。
  - KO: 보고서를 만든 뒤 웹 검색으로 수치의 출처를 찾아 각주를 다는 단계를 추가합니다.
  - EN: Add a step after the report is created that looks for the source of the figures with web search and adds footnotes.
- D. JA: 文書分析サブエージェントの要約を短くさせ、統合サブエージェントが扱う情報量を減らす。
  - KO: 문서 분석 subagent의 요약을 짧게 해서 통합 subagent가 다루는 정보량을 줄입니다.
  - EN: Have the document analysis subagent make its summaries shorter, reducing the amount of information the synthesis subagent handles.

## CCAR-F-Udemy06-0029

**JA** ある人材紹介会社の開発チームは、Claude Agent SDKを使って、社内エンジニア向けの開発者の生産性向上ツールを構築しています。このツールで、次の2種類の依頼を自動化しようとしています。

毎週の定型作業である「求人票テンプレートの必須項目のチェック、表記ゆれの修正、差分レポートの作成」

「先月から求人マッチングAPIの応答が遅くなった原因を調べる」のような、毎回内容の異なる調査

それぞれの依頼に適したタスク分解の方法として正しいものはどれですか。（2つ選択してください。）

**KO** 한 인재 소개 회사의 개발팀은 Claude Agent SDK로 사내 엔지니어용 개발자 생산성 향상 도구를 구축하고 있습니다. 이 도구로 다음 2가지 요청을 자동화하려고 합니다.

매주 반복하는 정형 작업인 “채용 공고 템플릿의 필수 항목 점검, 표기 불일치 수정, 차이 보고서 작성”

“지난달부터 채용 매칭 API의 응답이 느려진 원인을 조사해 줘”처럼 매번 내용이 다른 조사

각 요청에 맞는 작업 분해 방법으로 올바른 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: 定型作業は、決まった3つの手順を順に実行する固定のプロンプトチェーンにする。
  - KO: 정형 작업은 정해진 3단계를 순서대로 실행하는 고정된 prompt chain으로 만듭니다.
  - EN: For the routine task, use a fixed prompt chain that executes three predetermined steps in order.
- B. JA: 両方の依頼を同じ汎用エージェントに渡し、反復回数の上限を20回にして自由に進めさせる。
  - KO: 두 요청을 같은 범용 agent에 맡기고, 반복 횟수 상한을 20회로 두어 자유롭게 진행하게 합니다.
  - EN: Give both requests to the same general-purpose agent, set the iteration limit to 20, and let it proceed freely.
- C. JA: 原因の調査は、最初に得られた調査結果に応じて次のサブタスクを決める動的な分解にする。
  - KO: 원인 조사는 처음 얻은 조사 결과에 따라 다음 하위 작업을 정하는 동적 분해로 합니다.
  - EN: For the cause investigation, use dynamic decomposition in which the next subtask is decided according to the findings obtained first.
- D. JA: 原因の調査は、関係しそうなファイルを一度に読み込ませる単一のプロンプトで一括して実行する。
  - KO: 원인 조사는 관련 있어 보이는 파일을 한 번에 불러오는 단일 prompt로 일괄 실행합니다.
  - EN: For the cause investigation, run it all at once with a single prompt that loads all potentially relevant files at once.

## CCAR-F-Udemy06-0030

**JA** ある広告会社は、Claudeを使って、広告主との契約書や発注書から出稿期間・媒体・金額などを抽出し、出稿管理システムに登録しています。抽出エージェントには、5種類の抽出ツールに加えて、CRMの検索と更新、メールの送信、カレンダーへの登録、社内チャットへの投稿など、合計18個のツールが与えられています。

評価では、抽出に関係のないツールが呼ばれたり、似た抽出ツールの間で選択を誤ったりするケースが11%ありました。

ツール選択の信頼性を高めるための変更として最も適切なものはどれですか。

**KO** 한 광고 회사는 Claude로 광고주와의 계약서나 발주서에서 게재 기간·매체·금액 등을 추출해 게재 관리 시스템에 등록하고 있습니다. 추출 agent에게는 추출 도구 5종에 더해 CRM 검색과 갱신, 메일 발송, 캘린더 등록, 사내 채팅 게시 등 모두 18개의 도구가 주어져 있습니다.

평가에서는 추출과 관계없는 도구가 호출되거나, 비슷한 추출 도구 사이에서 잘못 선택하는 경우가 11% 있었습니다.

도구 선택의 신뢰성을 높이기 위한 변경으로 가장 적절한 것은 무엇입니까?

- A. JA: 18個のツールを1つの汎用ツールにまとめ、actionパラメータで操作の種類を指定させる。
  - KO: 18개 도구를 하나의 범용 도구로 합치고, action 파라미터로 작업 종류를 지정하게 합니다.
  - EN: Combine the 18 tools into a single general-purpose tool and have it specify the type of operation with an action parameter.
- B. JA: tool_choiceを{"type": "any"}にして、毎回いずれかのツールを呼ぶよう強制する。
  - KO: tool_choice를 {"type": "any"}로 설정해, 매번 어느 하나의 도구를 호출하도록 강제합니다.
  - EN: Set tool_choice to {"type": "any"} to force it to call one of the tools every time.
- C. JA: 18個のツールそれぞれについて、正しい選択を示すfew-shotの例をシステムプロンプトに追加する。
  - KO: 18개 도구 각각에 대해 올바른 선택을 보여 주는 few-shot 예시를 system prompt에 추가합니다.
  - EN: Add few-shot examples showing the correct choice for each of the 18 tools to the system prompt.
- D. JA: 抽出エージェントには抽出に必要なツールだけを与え、CRMやメールは別のエージェントに任せる。
  - KO: 추출 agent에게는 추출에 필요한 도구만 주고, CRM이나 메일은 별도의 agent에게 맡깁니다.
  - EN: Give the extraction agent only the tools needed for extraction, and leave CRM and email to a separate agent.

## CCAR-F-Udemy06-0031

**JA** あるEC企業の開発チームは、8つのパッケージからなるモノレポでClaude Codeを使っています。決済API・在庫API・配送APIの設計標準はdocs/standards/にファイルとしてまとめられていますが、各パッケージのCLAUDE.mdには、そのパッケージに関係する標準の本文がコピーして貼り付けられています。

その結果、標準を改訂しても一部のパッケージのCLAUDE.mdが古いままになり、パッケージによってClaudeが異なる規約でコードを生成するようになりました。どのパッケージにどの標準が関係するかは、各パッケージのメンテナーが把握しています。

最も適切な変更はどれですか。

**KO** 한 EC 기업의 개발팀은 8개 패키지로 이루어진 모노레포에서 Claude Code를 사용하고 있습니다. 결제 API·재고 API·배송 API의 설계 표준은 docs/standards/에 파일로 정리되어 있지만, 각 패키지의 CLAUDE.md에는 그 패키지와 관련된 표준 본문이 복사되어 붙여져 있습니다.

그 결과 표준을 개정해도 일부 패키지의 CLAUDE.md는 예전 내용 그대로 남아, 패키지마다 Claude가 서로 다른 규칙으로 코드를 생성하게 되었습니다. 어느 패키지에 어떤 표준이 관련되는지는 각 패키지의 메인테이너가 알고 있습니다.

가장 적절한 변경은 무엇입니까?

- A. JA: 各パッケージのCLAUDE.mdに標準ファイルのパスを書き、必要なときにClaudeが読むよう文章で指示する。
  - KO: 각 패키지의 CLAUDE.md에 표준 파일 경로를 적고, 필요할 때 Claude가 읽도록 글로 지시합니다.
  - EN: Write the paths of the standards files in each package's CLAUDE.md, and instruct Claude in prose to read them when needed.
- B. JA: 各パッケージのCLAUDE.mdの本文を削除し、選んだ標準ファイルを@importで取り込む。
  - KO: 각 패키지의 CLAUDE.md 본문을 삭제하고, 선택한 표준 파일을 @import로 불러옵니다.
  - EN: Delete the body text of each package's CLAUDE.md and import the selected standards files with @import.
- C. JA: すべての標準ファイルの内容をルートのCLAUDE.mdにまとめ、どのパッケージでも全標準を読み込ませる。
  - KO: 모든 표준 파일의 내용을 루트 CLAUDE.md에 모아, 어느 패키지에서든 전체 표준을 로드하게 합니다.
  - EN: Consolidate the contents of all standards files into the root CLAUDE.md and have every package load all the standards.
- D. JA: 標準を改訂したときに、各パッケージのCLAUDE.mdへ本文を自動でコピーするスクリプトをCIで実行する。
  - KO: 표준을 개정할 때 각 패키지의 CLAUDE.md로 본문을 자동 복사하는 스크립트를 CI에서 실행합니다.
  - EN: Run a script in CI that automatically copies the text into each package's CLAUDE.md whenever a standard is revised.

## CCAR-F-Udemy06-0032

**JA** ある自動車部品メーカーの開発チームは、Claude Code（Read・Grep・Globを含む組み込みツールを有効にした構成）を使って、車載ECU向けの診断ツールのコードを改修しています。低レベルのCAN通信関数send_frameを置き換える前に、その関数が使われている箇所をすべて洗い出す必要があります。

ところが、多くのモジュールはsend_frameを直接importせず、can_bus/__init__.pyというラッパーモジュールが別名（transmit、tx_frameなど）で再エクスポートした名前を使っています。最初にsend_frameという名前で検索したところ、見つかった使用箇所は実際の一部にとどまりました。

使用箇所を漏れなく追跡するための手順として適切なものはどれですか。（2つ選択してください。）

**KO** 한 자동차 부품 제조사의 개발팀은 Claude Code(Read·Grep·Glob을 포함한 내장 도구를 켠 구성)로 차량용 ECU 진단 도구의 코드를 수정하고 있습니다. 저수준 CAN 통신 함수 send_frame을 교체하기 전에, 이 함수가 쓰이는 곳을 모두 찾아내야 합니다.

그런데 많은 모듈은 send_frame을 직접 import하지 않고, can_bus/__init__.py라는 래퍼 모듈이 별칭(transmit, tx_frame 등)으로 re-export한 이름을 사용합니다. 처음에 send_frame이라는 이름으로 검색했더니, 찾은 사용처는 실제의 일부에 그쳤습니다.

사용처를 빠짐없이 추적하는 절차로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: 元の関数名send_frameを正規表現の部分一致に変えて、もう一度コードベース全体を検索する。
  - KO: 원래 함수명 send_frame을 정규식 부분 일치로 바꿔, 코드베이스 전체를 다시 검색합니다.
  - EN: Change the original function name send_frame to a partial-match regular expression and search the entire codebase again.
- B. JA: Bashでテストスイートを実行し、send_frameの呼び出し時に記録したスタックトレースから呼び出し元を集める。
  - KO: Bash로 테스트 스위트를 실행하고, send_frame 호출 시 기록한 스택 트레이스에서 호출한 쪽을 모읍니다.
  - EN: Run the test suite with Bash and collect the callers from stack traces recorded when send_frame is called.
- C. JA: 特定したそれぞれの名前でコードベース全体をGrepで検索し、呼び出し箇所を洗い出す。
  - KO: 확인한 각 이름으로 코드베이스 전체를 Grep으로 검색해 호출 위치를 찾아냅니다.
  - EN: Search the entire codebase with Grep for each of the identified names to find the call sites.
- D. JA: can_bus/__init__.pyをReadで読み、元の関数を再エクスポートしている名前をすべて特定する。
  - KO: can_bus/__init__.py를 Read로 읽고, 원래 함수를 re-export하는 이름을 모두 확인합니다.
  - EN: Read can_bus/__init__.py with Read and identify all the names that re-export the original function.

## CCAR-F-Udemy06-0033

**JA** ある公益財団法人の開発チームは、寄付者管理システムのリポジトリで、プルリクエストごとにClaude Codeでテストケースを自動生成するCIを運用しています。生成されたテストを確認すると、次の問題がありました。

実在しそうな氏名や住所を直接書き込んだテストデータが使われている

既存のテストスイートですでにカバーされているシナリオが、重複して提案されている

リポジトリには、匿名化済みの寄付者データのフィクスチャがtests/fixtures/に用意されています。

テスト生成の品質を高めるための変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 공익재단법인의 개발팀은 기부자 관리 시스템 저장소에서, pull request마다 Claude Code로 테스트 케이스를 자동 생성하는 CI를 운영하고 있습니다. 생성된 테스트를 확인해 보니 다음과 같은 문제가 있었습니다.

실제로 있을 법한 이름과 주소를 직접 적어 넣은 테스트 데이터가 쓰입니다

기존 테스트 스위트에서 이미 다루는 시나리오가 중복으로 제안됩니다

저장소에는 익명화를 마친 기부자 데이터 fixture가 tests/fixtures/에 준비되어 있습니다.

테스트 생성 품질을 높이기 위한 변경으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: 生成後に別のジョブで、テスト名の文字列が既存のテストと一致したものを削除する。
  - KO: 생성 후 별도 job에서, 테스트 이름 문자열이 기존 테스트와 일치하는 것을 삭제합니다.
  - EN: After generation, use a separate job to delete tests whose test name strings match existing tests.
- B. JA: CIを実行するランナーのユーザーの~/.claude/CLAUDE.mdに、テストデータの扱い方を書いておく。
  - KO: CI를 실행하는 runner 사용자의 ~/.claude/CLAUDE.md에 테스트 데이터 다루는 법을 적어 둡니다.
  - EN: Write how to handle test data in ~/.claude/CLAUDE.md of the user on the runner that executes CI.
- C. JA: テストの規約、良いテストの基準、使えるフィクスチャをリポジトリのCLAUDE.mdに書いてコミットする。
  - KO: 테스트 규칙, 좋은 테스트의 기준, 사용할 수 있는 fixture를 저장소의 CLAUDE.md에 적어 commit합니다.
  - EN: Write the testing conventions, the criteria for good tests, and the available fixtures in the repository's CLAUDE.md and commit it.
- D. JA: テストを生成するときに、対象モジュールの既存のテストファイルをコンテキストとして渡す。
  - KO: 테스트를 생성할 때 대상 모듈의 기존 테스트 파일을 context로 전달합니다.
  - EN: When generating tests, pass the existing test files of the target module as context.

## CCAR-F-Udemy06-0034

**JA** ある消費財メーカーのデジタル部門は、3つのブランドサイトで共有しているUIコンポーネントのライブラリを新しいデザインシステムに移行する作業に、Claude Codeを使っています。作業は、各サイトでのコンポーネントの使われ方を調べる調査フェーズと、移行方針を決めて実装するフェーズに分かれます。

前回の試行では、次の2つの問題が起きました。

調査フェーズでClaudeが数百のファイルを読み込んだ結果、実装フェーズに入る前にコンテキストの大半が埋まり、調査の序盤で確認した制約が実装に反映されなかった

調査の途中で一部のコンポーネントを書き換え始めてしまい、方針の決定後に手戻りが生じた

次の試行で取るべき進め方として適切なものはどれですか。（2つ選択してください。）

**KO** 한 소비재 제조사의 디지털 부문은 3개 브랜드 사이트가 공유하는 UI 컴포넌트 라이브러리를 새 디자인 시스템으로 이전하는 작업에 Claude Code를 사용하고 있습니다. 작업은 각 사이트에서 컴포넌트가 어떻게 쓰이는지 조사하는 조사 단계와, 이전 방침을 정해 구현하는 단계로 나뉩니다.

지난 시도에서는 다음 2가지 문제가 생겼습니다.

조사 단계에서 Claude가 수백 개 파일을 읽은 결과, 구현 단계에 들어가기 전에 context 대부분이 차 버려, 조사 초반에 확인한 제약이 구현에 반영되지 않았습니다

조사 도중에 일부 컴포넌트를 고쳐 쓰기 시작해 버려, 방침을 정한 뒤에 재작업이 생겼습니다

다음 시도에서 취해야 할 진행 방식으로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: 調査と実装を同じ会話で続け、コンテキストが上限に近づいたら自動の圧縮に任せる。
  - KO: 조사와 구현을 같은 대화에서 이어 가고, context가 한도에 가까워지면 자동 압축에 맡깁니다.
  - EN: Continue the investigation and implementation in the same conversation, and leave it to automatic compaction when the context approaches its limit.
- B. JA: 調査と方針の設計はプランモードで行い、計画を承認してから直接実行で実装させる。
  - KO: 조사와 방침 설계는 plan mode에서 하고, 계획을 승인한 뒤 직접 실행으로 구현하게 합니다.
  - EN: Do the investigation and approach design in plan mode, and after approving the plan, have it implement with direct execution.
- C. JA: 3つのサイトのファイルをすべて最初にReadで読み込ませ、全体を把握したうえで実装を始めさせる。
  - KO: 3개 사이트의 파일을 모두 먼저 Read로 읽게 하고, 전체를 파악한 뒤 구현을 시작하게 합니다.
  - EN: Have Claude first load all files of the three sites with Read, and start implementation after grasping the whole picture.
- D. JA: 冗長な調査はExploreサブエージェントに任せ、メインの会話には使用状況の要約だけを返させる。
  - KO: 출력이 많은 조사는 Explore subagent에 맡기고, 메인 대화에는 사용 현황 요약만 반환하게 합니다.
  - EN: Delegate the verbose investigation to an Explore subagent, and have it return only a summary of usage to the main conversation.

## CCAR-F-Udemy06-0035

**JA** ある外食チェーンは、Claude Agent SDKを使って、予約の変更やキャンセルに対応するカスタマーサポート解決エージェントを運用しています。予約の変更が完了したときの確認メッセージには、次の4項目をこの順で含めるよう、システムプロンプトで詳しく指示しています。

店舗名

変更前と変更後の日時

人数

キャンセル規定

しかし監査では、確認メッセージの23%で、項目の順序が入れ替わっていたり、キャンセル規定が文章の途中に埋もれていたりしました。

確認メッセージの形式を一貫させるために最も効果的な変更はどれですか。

**KO** 한 외식 체인은 Claude Agent SDK로 예약 변경과 취소에 대응하는 고객 지원 해결 agent를 운영하고 있습니다. 예약 변경이 완료되었을 때의 확인 메시지에는 다음 4개 항목을 이 순서대로 넣으라고 system prompt에서 자세히 지시하고 있습니다.

매장명

변경 전과 변경 후의 일시

인원

취소 규정

그러나 감사에서 확인 메시지의 23%가 항목 순서가 뒤바뀌어 있거나, 취소 규정이 문장 중간에 묻혀 있었습니다.

확인 메시지의 형식을 일관되게 만들기 위해 가장 효과적인 변경은 무엇입니까?

- A. JA: 確認メッセージの作成だけを別のサブエージェントに委任し、そのシステムプロンプトに同じ指示を書く。
  - KO: 확인 메시지 작성만 별도 subagent에 위임하고, 그 system prompt에 같은 지시를 적습니다.
  - EN: Delegate only the writing of confirmation messages to a separate subagent and put the same instructions in its system prompt.
- B. JA: 確認メッセージを送る前に、項目の順序を正規表現で検査して並べ替える後処理を追加する。
  - KO: 확인 메시지를 보내기 전에 항목 순서를 정규식으로 검사해 재배열하는 후처리를 추가합니다.
  - EN: Add post-processing that checks the order of the items with a regular expression and reorders them before the confirmation message is sent.
- C. JA: 4項目の指示に【必須】の見出しを付けて強調し、システムプロンプトの冒頭と末尾の両方に繰り返し書く。
  - KO: 4개 항목 지시에 【필수】 제목을 붙여 강조하고, system prompt의 맨 앞과 맨 끝에 모두 반복해 적습니다.
  - EN: Emphasize the four-item instructions with a [Required] heading and repeat them at both the beginning and the end of the system prompt.
- D. JA: 人数の変更や日時の変更など、ケースごとの確認メッセージの完成例を数件示す。
  - KO: 인원 변경, 일시 변경 등 사례별 확인 메시지의 완성 예시를 몇 개 보여 줍니다.
  - EN: Provide several complete example confirmation messages for individual cases, such as a change in the number of guests and a change in date and time.

## CCAR-F-Udemy06-0036

**JA** ある大学は、Claude Agent SDKを使って、学生からの履修登録や証明書発行の問い合わせに対応するカスタマーサポート解決エージェントを運用しています。エージェントは、氏名でget_studentを呼び出して学生の記録を取得します。

監査の結果、氏名で照会して複数の学生が一致したケースのうち約30%で、エージェントが最近ログインした学生を選んで手続きを進めており、別の学生の履修記録を案内してしまった事例が見つかりました。

この問題への対処として最も適切なものはどれですか。

**KO** 한 대학은 Claude Agent SDK로 학생의 수강 신청이나 증명서 발급 문의에 대응하는 고객 지원 해결 agent를 운영하고 있습니다. agent는 이름으로 get_student를 호출해 학생 기록을 가져옵니다.

감사 결과, 이름으로 조회해 여러 학생이 일치한 경우의 약 30%에서 agent가 최근에 로그인한 학생을 골라 절차를 진행했고, 다른 학생의 수강 기록을 안내해 버린 사례가 발견되었습니다.

이 문제에 대한 대처로 가장 적절한 것은 무엇입니까?

- A. JA: 複数の学生が一致した場合は、問い合わせを自動的に人間の担当者にエスカレーションする。
  - KO: 여러 학생이 일치하면 문의를 자동으로 사람 담당자에게 escalation합니다.
  - EN: When multiple students match, automatically escalate the inquiry to a human agent.
- B. JA: 複数の学生が一致した場合は、学籍番号や生年月日など追加の識別情報を尋ねてから手続きを進める。
  - KO: 여러 학생이 일치하면 학번이나 생년월일 같은 추가 식별 정보를 물어본 뒤 절차를 진행합니다.
  - EN: When multiple students match, ask for additional identifying information such as the student ID number or date of birth before proceeding.
- C. JA: 複数の学生が一致した場合は、最終ログイン日時が最も新しい学生を選ぶ規則をシステムプロンプトに書く。
  - KO: 여러 학생이 일치하면 최종 로그인 일시가 가장 최근인 학생을 고르는 규칙을 system prompt에 적습니다.
  - EN: Write a rule in the system prompt that, when multiple students match, the student with the most recent last login date and time is selected.
- D. JA: 複数の学生が一致した場合は、一致した全員の氏名・学部・学年を一覧で示し、本人に選んでもらう。
  - KO: 여러 학생이 일치하면 일치한 모든 학생의 이름·학부·학년을 목록으로 보여 주고 본인이 고르게 합니다.
  - EN: When multiple students match, display a list of the name, department, and year of all matching students and have the person choose themselves.

## CCAR-F-Udemy06-0037

**JA** ある教育サービス企業の開発チームは、学習管理システムのリポジトリに、コードレビューの手順をまとめたスキルを.claude/skills/review/SKILL.mdとしてコミットし、全員が/reviewで使っています。

先月、チームでレビューの観点に「アクセシビリティの確認」を追加しましたが、あるエンジニアの/reviewだけは、新しい観点を含まない古い手順で動いていました。調べると、このエンジニアは以前、自分の好みに合わせて手順を変えたスキルを~/.claude/skills/review/SKILL.mdに作っていたことがわかりました。

このエンジニアが自分用の手順を残しつつ、チームの更新も受け取れるようにするための対応として最も適切なものはどれですか。

**KO** 한 교육 서비스 기업의 개발팀은 학습 관리 시스템 저장소에 코드 리뷰 절차를 정리한 skill을 .claude/skills/review/SKILL.md로 commit했고, 모두가 /review로 사용하고 있습니다.

지난달 팀은 리뷰 관점에 “접근성 확인”을 추가했는데, 한 엔지니어의 /review만은 새 관점이 빠진 예전 절차로 동작하고 있었습니다. 알아보니 이 엔지니어는 예전에 자기 취향에 맞게 절차를 바꾼 skill을 ~/.claude/skills/review/SKILL.md에 만들어 두었습니다.

이 엔지니어가 자기용 절차를 유지하면서 팀의 업데이트도 받을 수 있게 하는 대응으로 가장 적절한 것은 무엇입니까?

- A. JA: 個人用のスキルのフロントマターにdisable-model-invocation: trueを追加し、自動で読み込まれない設定にする。
  - KO: 개인 skill의 frontmatter에 disable-model-invocation: true를 추가해 자동으로 로드되지 않게 설정합니다.
  - EN: Add disable-model-invocation: true to the frontmatter of the personal skill so that it is not loaded automatically.
- B. JA: 個人用のスキルをreview-strictのような別の名前に変え、/reviewではチームのスキルを使う。
  - KO: 개인 skill의 이름을 review-strict 같은 다른 이름으로 바꾸고, /review로는 팀의 skill을 사용합니다.
  - EN: Rename the personal skill to something like review-strict, and use the team's skill for /review.
- C. JA: 個人用のスキルを残したまま、チームの更新があるたびに差分を手作業で個人用のファイルに反映する。
  - KO: 개인 skill을 그대로 둔 채, 팀의 업데이트가 있을 때마다 변경분을 직접 개인 파일에 반영합니다.
  - EN: Keep the personal skill as it is and manually apply the differences to the personal file each time the team updates its skill.
- D. JA: 個人用のスキルの内容でプロジェクトのスキルを上書きしてコミットし、チーム全員を同じ手順にそろえる。
  - KO: 개인 skill의 내용으로 프로젝트 skill을 덮어써 commit하고, 팀 전원이 같은 절차를 쓰게 합니다.
  - EN: Overwrite the project skill with the contents of the personal skill and commit it, so that the whole team uses the same procedure.

## CCAR-F-Udemy06-0038

**JA** ある鉄道会社のシステム部門は、Claude Agent SDKを使って、開発者の生産性向上ツールを構築しています。エンジニアがレガシーシステムを理解し、反復的な作業を自動化するためのツールです。

あるエンジニアがツールに「運行管理システム全体のエラー処理を、新しい共通の例外クラスに統一して」と依頼しました。対象は約900ファイルで、どのモジュールがどの例外に依存しているかは誰も把握していません。

最初の試行では、エージェントがディレクトリ名の順にファイルを1つずつ書き換え始めました。3時間後、遅延の伝播を計算するモジュールの変更が多数の箇所に影響していることが判明し、作業の大半をやり直すことになりました。

このようなオープンエンドなタスクを分解する方法として最も適切なものはどれですか。

**KO** 한 철도 회사의 시스템 부문은 Claude Agent SDK로 개발자 생산성 향상 도구를 구축하고 있습니다. 엔지니어가 레거시 시스템을 이해하고 반복 작업을 자동화하기 위한 도구입니다.

한 엔지니어가 도구에 “운행 관리 시스템 전체의 에러 처리를 새 공통 예외 클래스로 통일해 줘”라고 요청했습니다. 대상은 약 900개 파일이며, 어느 모듈이 어떤 예외에 의존하는지 아는 사람은 아무도 없습니다.

첫 시도에서 agent는 디렉터리 이름 순서대로 파일을 하나씩 고쳐 쓰기 시작했습니다. 3시간 뒤, 지연 전파를 계산하는 모듈의 변경이 많은 곳에 영향을 준다는 사실이 드러나, 작업 대부분을 다시 해야 했습니다.

이런 open-ended 작업을 분해하는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: 対象のファイルをまとめて1回のリクエストで読み込ませ、変更箇所の一覧を出力させてから書き換えさせる。
  - KO: 대상 파일을 한꺼번에 한 번의 요청으로 불러오게 하고, 변경할 곳 목록을 출력하게 한 뒤 고쳐 쓰게 합니다.
  - EN: Load all the target files in a single request, have it output a list of the places to change, and then have it rewrite them.
- B. JA: まず依存関係を把握して影響の大きい領域から計画を立て、新たな発見に応じて計画を見直させる。
  - KO: 먼저 의존 관계를 파악해 영향이 큰 영역부터 계획을 세우고, 새로 발견한 내용에 따라 계획을 수정하게 합니다.
  - EN: First have it map the dependencies and build a plan starting from the highest-impact areas, then revise the plan as new findings emerge.
- C. JA: 900ファイルを100ファイルずつ9つのサブエージェントに割り当て、同じ指示で並列に書き換えさせる。
  - KO: 900개 파일을 100개씩 9개 subagent에 할당하고, 같은 지시로 병렬로 고쳐 쓰게 합니다.
  - EN: Assign the 900 files to nine subagents of 100 files each and have them rewrite in parallel with the same instructions.
- D. JA: あらかじめ「検索→置換→テスト」の固定チェーンを決め、すべてのファイルに同じ順で適用させる。
  - KO: 미리 “검색→치환→테스트”라는 고정 chain을 정하고, 모든 파일에 같은 순서로 적용하게 합니다.
  - EN: Define a fixed chain of "search -> replace -> test" in advance and apply it to all files in the same order.

## CCAR-F-Udemy06-0039

**JA** ある建設コンサルタント会社は、マルチエージェントリサーチシステムを使って、インフラの老朽化対策の事例を調べています。文書分析サブエージェントには、次の2つのツールがあります。

record_finding（調査結果を記録する）

flag_unreadable（読み取れない文書を報告する）

ログでは、約9%のケースで、サブエージェントがどちらのツールも呼ばずに文章だけを返しており、コーディネーターが結果を集計できていませんでした。文章だけが返されたケースの多くは、文書に関連する記述がなかった場合でした。

この問題に対処する設定と設計として適切なものはどれですか。（2つ選択してください。）

**KO** 한 건설 컨설턴트 회사는 multi-agent 리서치 시스템으로 인프라 노후화 대책 사례를 조사하고 있습니다. 문서 분석 subagent에는 다음 2개의 도구가 있습니다.

record_finding(조사 결과를 기록한다)

flag_unreadable(읽을 수 없는 문서를 보고한다)

로그를 보니 약 9%의 경우에 subagent가 어느 도구도 호출하지 않고 텍스트만 반환해, coordinator가 결과를 집계하지 못했습니다. 텍스트만 반환된 경우의 대부분은 문서에 관련 내용이 없을 때였습니다.

이 문제에 대처하는 설정과 설계로 적절한 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: 関連する記述がなかったことを記録するrecord_no_relevant_contentツールを追加する。
  - KO: 관련 내용이 없었다는 것을 기록하는 record_no_relevant_content 도구를 추가합니다.
  - EN: Add a record_no_relevant_content tool that records that no relevant content was found.
- B. JA: tool_choiceをrecord_findingに固定し、どの文書でも調査結果を記録させる。
  - KO: tool_choice를 record_finding으로 고정해, 어떤 문서든 조사 결과를 기록하게 합니다.
  - EN: Fix tool_choice to record_finding so that findings are recorded for every document.
- C. JA: 文章だけの応答が返ったときは、その文章を要約させてrecord_findingの内容として登録する。
  - KO: 텍스트만 있는 응답이 오면 그 텍스트를 요약하게 해서 record_finding의 내용으로 등록합니다.
  - EN: When a text-only response is returned, have it summarize that text and register it as the content of record_finding.
- D. JA: tool_choiceを{"type": "any"}にして、いずれかのツールを必ず呼ばせる。
  - KO: tool_choice를 {"type": "any"}로 설정해, 어느 하나의 도구를 반드시 호출하게 합니다.
  - EN: Set tool_choice to {"type": "any"} so that one of the tools is always called.

## CCAR-F-Udemy06-0040

**JA** あるEC物流企業の開発チームは、倉庫管理システムのリポジトリで、Claude Codeによる自動コードレビューをCI/CDパイプラインに組み込んでいます。

開発者から誤検知が多いという苦情が出たため、レビュー用のプロンプトに「保守的に判断し、確信度の高い指摘事項のみを報告すること」という一文を追加しました。2週間後に集計したところ、次の結果になりました。

誤検知率は38%から36%にしか下がらなかった

在庫引当ロジックの実際のバグを見逃すケースが増えた

この変更で精度が改善しなかった理由として正しいものはどれですか。（2つ選択してください。）

**KO** 한 EC 물류 기업의 개발팀은 창고 관리 시스템 저장소에서 Claude Code를 이용한 자동 코드 리뷰를 CI/CD pipeline에 넣어 두었습니다.

개발자들이 오탐이 많다고 불만을 제기해서, 리뷰용 prompt에 “보수적으로 판단하고, 확신도가 높은 지적 사항만 보고할 것”이라는 문장을 추가했습니다. 2주 뒤 집계한 결과는 다음과 같았습니다.

오탐률은 38%에서 36%로밖에 내려가지 않았습니다

재고 할당 로직의 실제 버그를 놓치는 경우가 늘었습니다

이 변경으로 정확도가 개선되지 않은 이유로 올바른 것은 무엇입니까? (2개를 고르십시오.)

- A. JA: 「保守的に」という指示は報告する問題としない問題の基準を示しておらず、判断の境界が変わらないため。
  - KO: “보수적으로”라는 지시는 보고할 문제와 보고하지 않을 문제의 기준을 제시하지 않아, 판단 경계가 바뀌지 않기 때문입니다.
  - EN: The instruction to be "conservative" does not specify criteria for which issues to report and which not to, so the decision boundary does not change.
- B. JA: 追加した一文をプロンプトの末尾に置いたことで、長い差分の後ろに隠れて読み飛ばされたため。
  - KO: 추가한 문장을 prompt 끝에 두어, 긴 diff 뒤에 묻혀 읽히지 않고 넘어갔기 때문입니다.
  - EN: Because the added sentence was placed at the end of the prompt, it was hidden behind a long diff and was overlooked.
- C. JA: 自己申告の確信度は誤検知と対応するようキャリブレーションされておらず、誤った指摘にも高い確信度が付くため。
  - KO: 자기 보고한 확신도는 오탐과 대응하도록 calibration되어 있지 않아, 잘못된 지적에도 높은 확신도가 붙기 때문입니다.
  - EN: Self-reported confidence is not calibrated to correspond to false positives, so incorrect findings also receive high confidence.
- D. JA: 確信度に関する指示は、-pフラグで非対話実行したClaude Codeでは無視され、対話モードでしか反映されないため。
  - KO: 확신도에 관한 지시는 -p 플래그로 비대화형 실행한 Claude Code에서는 무시되고, 대화형 모드에서만 반영되기 때문입니다.
  - EN: Instructions about confidence are ignored by Claude Code run non-interactively with the -p flag and are reflected only in interactive mode.

## CCAR-F-Udemy06-0041

**JA** ある証券会社は、Claude Agent SDKを使って、口座の残高照会や取引履歴の問い合わせに対応するカスタマーサポート解決エージェントを運用しています。エージェントには、get_customerで本人確認を行ったあとに、口座データベースに対して任意のSQLを実行できるrun_sqlツールが与えられています。

監査の結果、エージェントが生成したクエリの0.4%で絞り込みの条件が誤っており、本人確認済みの顧客以外の口座情報が応答に含まれていたことがわかりました。

この問題に対する最も適切な対策はどれですか。

**KO** 한 증권사는 Claude Agent SDK로 계좌 잔고 조회나 거래 내역 문의에 대응하는 고객 지원 해결 agent를 운영하고 있습니다. agent에게는 get_customer로 본인 확인을 한 뒤, 계좌 데이터베이스에 임의의 SQL을 실행할 수 있는 run_sql 도구가 주어져 있습니다.

감사 결과, agent가 생성한 쿼리의 0.4%에서 필터 조건이 잘못되어, 본인 확인을 마친 고객이 아닌 다른 사람의 계좌 정보가 응답에 포함되었다는 사실이 드러났습니다.

이 문제에 대한 가장 적절한 대책은 무엇입니까?

- A. JA: run_sqlを呼ぶ前に、生成したクエリが正しいかをエージェント自身に再確認させるステップを追加する。
  - KO: run_sql을 호출하기 전에, 생성한 쿼리가 올바른지 agent 스스로 다시 확인하는 단계를 추가합니다.
  - EN: Add a step that has the agent itself recheck whether the generated query is correct before calling run_sql.
- B. JA: システムプロンプトに、クエリには必ず本人確認済みの顧客IDを条件として含めるよう明記する。
  - KO: system prompt에, 쿼리에는 반드시 본인 확인을 마친 고객 ID를 조건으로 넣으라고 명시합니다.
  - EN: State explicitly in the system prompt that queries must always include the identity-verified customer ID as a condition.
- C. JA: run_sqlを残したまま、実行されたクエリを人間の担当者が毎日事後に確認する運用を追加する。
  - KO: run_sql을 그대로 두고, 실행된 쿼리를 사람 담당자가 매일 사후에 확인하는 운영 절차를 추가합니다.
  - EN: Keep run_sql and add a process in which a human agent reviews the executed queries after the fact every day.
- D. JA: run_sqlを、検証済みの顧客IDの口座だけを返すget_account_summaryに置き換える。
  - KO: run_sql을, 검증된 고객 ID의 계좌만 반환하는 get_account_summary로 대체합니다.
  - EN: Replace run_sql with get_account_summary, which returns only the accounts of the verified customer ID.

## CCAR-F-Udemy06-0042

**JA** あるエンターテインメント企業の開発チームは、チケット販売システムのリポジトリで、Claude Codeによる自動コードレビューをCIに組み込んでいます。指摘をカテゴリ別に集計すると、正しく問題を指摘できた割合は、次のとおりでした。

セキュリティは92%

N+1クエリは88%

命名規則は31%

開発者への聞き取りでは、「どうせ誤検知が多い」という理由で、セキュリティの指摘まで読まずに閉じる人が増えていることがわかりました。

開発者の信頼を回復するために、最初に取るべき対応として最も適切なものはどれですか。

**KO** 한 엔터테인먼트 기업의 개발팀은 티켓 판매 시스템 저장소에서 Claude Code를 이용한 자동 코드 리뷰를 CI에 넣어 두었습니다. 지적을 카테고리별로 집계하니, 문제를 올바르게 지적한 비율은 다음과 같았습니다.

보안: 92%

N+1 쿼리: 88%

명명 규칙: 31%

개발자 인터뷰에서는 “어차피 오탐이 많다”는 이유로 보안 지적까지 읽지 않고 닫는 사람이 늘고 있다는 사실이 드러났습니다.

개발자의 신뢰를 회복하기 위해 가장 먼저 취해야 할 대응으로 적절한 것은 무엇입니까?

- A. JA: 各カテゴリの指摘に確信度を付けさせ、確信度が0.9未満の指摘は投稿しない設定にする。
  - KO: 각 카테고리의 지적에 확신도를 붙이게 하고, 확신도가 0.9 미만인 지적은 게시하지 않도록 설정합니다.
  - EN: Have it attach a confidence level to the findings in each category, and configure it not to post findings with a confidence below 0.9.
- B. JA: 命名規則のカテゴリを一時的に無効にし、その間に命名規則の判定基準と例を改善する。
  - KO: 명명 규칙 카테고리를 일시적으로 끄고, 그동안 명명 규칙의 판정 기준과 예시를 개선합니다.
  - EN: Temporarily disable the naming conventions category, and use that time to improve the criteria and examples for judging naming conventions.
- C. JA: 開発者向けに、誤検知の指摘でも内容を確認してから閉じるよう求める運用ルールを周知する。
  - KO: 개발자에게 오탐 지적이라도 내용을 확인한 뒤 닫으라는 운영 규칙을 공지합니다.
  - EN: Announce an operating rule asking developers to check the content of findings before closing them, even false positives.
- D. JA: 誤検知を減らす目的で、レビューを実行するモデルをより上位のモデルに切り替える。
  - KO: 오탐을 줄이기 위해 리뷰를 실행하는 모델을 더 상위 모델로 바꿉니다.
  - EN: Switch the model that runs the review to a higher-tier model in order to reduce false positives.

## CCAR-F-Udemy06-0043

**JA** ある海運会社は、Claude Agent SDKを使って、荷主からの問い合わせに対応するカスタマーサポート解決エージェントを運用しています。補償ポリシーには、自社船の遅延による補償の条件と金額が定められていますが、提携する他社船に積み替えた区間で発生した遅延については何も定められていません。

ログを確認すると、こうした区間の遅延について補償を求められた際、エージェントは自社船の規定を準用して補償額を提示したり、規定外として断ったりと、対応がばらばらでした。また、エスカレーションされた案件では、引き継いだ担当者が、何を求められているのかを確かめるために会話の記録を最初から読み直していました。

これらの問題への対処として適切なものはどれですか。（2つ選択してください。）

**KO** 한 해운 회사는 Claude Agent SDK로 화주의 문의에 대응하는 고객 지원 해결 agent를 운영합니다. 보상 정책에는 자사 선박의 지연에 대한 보상 조건과 금액이 정해져 있지만, 제휴한 타사 선박으로 환적한 구간에서 생긴 지연에 대해서는 아무것도 정해져 있지 않습니다.

로그를 확인해 보니, 이런 구간의 지연에 대해 보상을 요구받았을 때 agent는 자사 선박 규정을 준용해 보상액을 제시하기도 하고 규정 외라며 거절하기도 하는 등 대응이 제각각이었습니다. 또한 escalation된 건에서는 인계받은 담당자가 무엇을 요구받고 있는지 확인하려고 대화 기록을 처음부터 다시 읽고 있었습니다.

이 문제들에 대한 대처로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: エスカレーション時は、案件の事実と要求を構造化したハンドオフサマリーで渡す。
  - KO: escalation할 때는 건의 사실관계와 요구 사항을 구조화한 handoff 요약으로 넘깁니다.
  - EN: When escalating, hand off a structured handoff summary of the case facts and the request.
- B. JA: 他社船の区間にも自社船の補償規定を準用し、計算した補償額を荷主に提示させる。
  - KO: 타사 선박 구간에도 자사 선박의 보상 규정을 준용해, 계산한 보상액을 화주에게 제시하게 합니다.
  - EN: Apply the company's own vessel compensation rules by analogy to the partner vessel legs and have the agent quote the calculated compensation amount to the shipper.
- C. JA: ポリシーに定めがない要求は規定外として一律に断り、その理由を丁寧に説明させる。
  - KO: 정책에 정해지지 않은 요구는 규정 외로 보고 일률적으로 거절하며, 그 이유를 정중하게 설명하게 합니다.
  - EN: Uniformly decline requests not covered by the policy as outside the policy, and have the agent explain the reason politely.
- D. JA: ポリシーに定めがない要求はエスカレーションする基準を、システムプロンプトに明記する。
  - KO: 정책에 정해지지 않은 요구는 escalation한다는 기준을 system prompt에 명시합니다.
  - EN: State explicitly in the system prompt the criteria for escalating requests that are not covered by the policy.

## CCAR-F-Udemy06-0044

**JA** ある法律事務所のシステム開発チームは、Claude Codeを使って、契約書管理システムのデータ移行スクリプトを作成しています。旧システムの「契約締結日」列をISO 8601形式の日付に変換する処理について、Claudeに「和暦や未入力の値にも対応してほしい」と文章で3回修正を依頼しました。

しかし、そのたびに「令和元年5月1日」が変換エラーになったり、未入力の値が「1970-01-01」に置き換わったりと、別のケースが壊れます。

エッジケースの処理を安定して直すために、次に取るべき対応として最も効果的なものはどれですか。

**KO** 한 법률 사무소의 시스템 개발팀은 Claude Code로 계약서 관리 시스템의 데이터 이전 스크립트를 작성하고 있습니다. 구 시스템의 "계약 체결일" 열을 ISO 8601 형식의 날짜로 변환하는 처리에 대해, Claude에게 "일본 연호 표기나 미입력 값도 처리해 달라"고 글로 세 번 수정을 요청했습니다.

그러나 그때마다 "令和元年5月1日"이 변환 오류가 나거나 미입력 값이 "1970-01-01"로 바뀌는 등 다른 케이스가 깨집니다.

edge case 처리를 안정적으로 고치기 위해 다음에 취할 대응으로 가장 효과적인 것은 무엇입니까?

- A. JA: プランモードに切り替え、和暦と未入力の値を含む日付変換の処理方針をClaudeに計画させてから修正を再開する。
  - KO: plan mode로 전환해, 일본 연호와 미입력 값을 포함한 날짜 변환 처리 방침을 Claude가 계획하게 한 뒤 수정을 재개합니다.
  - EN: Switch to plan mode, have Claude plan the approach for date conversion including Japanese-era dates and blank values, and then resume the fix.
- B. JA: 和暦の元号ごとの換算や未入力の値の意味について、Claudeに質問させるインタビューから始める。
  - KO: 연호별 환산 방법과 미입력 값의 의미에 대해 Claude가 질문하는 인터뷰부터 시작합니다.
  - EN: Start with an interview in which Claude asks questions about the conversion by Japanese era name and the meaning of blank values.
- C. JA: 和暦の換算方法と未入力の値をnullのまま残すルールを、箇条書きでより詳しく説明した依頼文に書き直す。
  - KO: 연호 환산 방법과 미입력 값을 null로 남긴다는 규칙을 글머리 기호로 더 자세히 설명한 요청문으로 다시 씁니다.
  - EN: Rewrite the request to explain in more detail, in bullet points, how to convert Japanese-era dates and the rule of leaving blank values as null.
- D. JA: 「令和元年5月1日」→「2019-05-01」のような入力と期待値のテストケースを示して修正させる。
  - KO: "令和元年5月1日"→"2019-05-01"처럼 입력과 기댓값으로 된 테스트 케이스를 제시하고 수정하게 합니다.
  - EN: Provide test cases with inputs and expected values, such as 「令和元年5月1日」→「2019-05-01」, and have it make the fix.

## CCAR-F-Udemy06-0045

**JA** ある家電メーカーのファームウェア開発チームは、Claude Codeのスキル/flash-auditを作成し、リポジトリにコミットしています。このスキルは、ファームウェアの書き込み手順に関するコードとgit logの履歴を調べて安全上の問題を報告するもので、ファイルを変更してはいけません。

運用を始めると、次の2つの問題が起きました。

スキルの実行中に、Claudeがコメントの誤字をEditで直してしまう事例があった

スキルを実行するたびにgit logの実行で許可を求められ、開発者が毎回承認している

SKILL.mdのフロントマターに加える変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 가전제품 제조사의 펌웨어 개발팀은 Claude Code skill인 /flash-audit을 만들어 저장소에 commit했습니다. 이 skill은 펌웨어 기록(flashing) 절차와 관련된 코드와 git log 이력을 조사해 안전상의 문제를 보고하는 것으로, 파일을 변경해서는 안 됩니다.

운영을 시작하자 다음 두 가지 문제가 생겼습니다.

skill 실행 중에 Claude가 주석의 오타를 Edit로 고쳐 버린 사례가 있었습니다

skill을 실행할 때마다 git log 실행에 대한 허가를 요청받아, 개발자가 매번 승인하고 있습니다

SKILL.md의 frontmatter에 추가할 변경으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: スキルの本文の冒頭に、ファイルを変更しないことを強調した注意書きを加える。
  - KO: skill 본문 첫머리에 파일을 변경하지 말라고 강조하는 주의 문구를 추가합니다.
  - EN: Add a note at the beginning of the skill body that emphasizes that files must not be modified.
- B. JA: disallowed-toolsにEditとWriteを指定し、実行中は使えるツールから外す。
  - KO: disallowed-tools에 Edit와 Write를 지정해, 실행 중에 사용할 수 있는 도구에서 제외합니다.
  - EN: Specify Edit and Write in disallowed-tools to remove them from the tools available during execution.
- C. JA: context: forkを設定し、スキルを分離されたサブエージェントのコンテキストで実行させる。
  - KO: context: fork를 설정해, skill을 분리된 subagent의 context에서 실행하게 합니다.
  - EN: Set context: fork to run the skill in the context of an isolated subagent.
- D. JA: allowed-toolsにBash(git log *)を指定し、確認なしでgit logを実行させる。
  - KO: allowed-tools에 Bash(git log *)를 지정해, 확인 없이 git log를 실행하게 합니다.
  - EN: Specify Bash(git log *) in allowed-tools so that git log runs without confirmation.

## CCAR-F-Udemy06-0046

**JA** ある半導体製造装置メーカーの開発チームは、Claude Code（Read・Grep・Globを含む組み込みツールを有効にした構成）を使って、露光装置の制御ソフトウェアを保守しています。次の2つの調査が必要になりました。

ウェハの位置補正を行う関数apply_wafer_offsetの引数を変更する前に、この関数を呼び出しているすべての箇所を見つける

現場から報告されたALIGN_TIMEOUT: stage not readyというエラーメッセージが、どこで出力されているかを特定する

それぞれの調査で使う方法として適切なものはどれですか。（2つ選択してください。）

**KO** 한 반도체 제조 장비 업체의 개발팀은 Claude Code(Read·Grep·Glob을 포함한 기본 제공 도구를 활성화한 구성)로 노광 장비의 제어 소프트웨어를 유지보수하고 있습니다. 다음 두 가지 조사가 필요해졌습니다.

웨이퍼 위치를 보정하는 함수 apply_wafer_offset의 인자를 변경하기 전에, 이 함수를 호출하는 모든 곳을 찾습니다

현장에서 보고된 ALIGN_TIMEOUT: stage not ready라는 오류 메시지가 어디에서 출력되는지 찾아냅니다

각 조사에 사용할 방법으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: Globで**/*wafer*.pyに一致するファイルを列挙し、その中から呼び出し元を探す。
  - KO: Glob으로 **/*wafer*.py에 일치하는 파일을 나열하고, 그중에서 호출하는 곳을 찾습니다.
  - EN: Use Glob to list files matching **/*wafer*.py, and look for callers among them.
- B. JA: Globで**/*error*.pyや**/*log*.pyに一致するファイルを列挙し、順にReadで読んで出力箇所を探す。
  - KO: Glob으로 **/*error*.py나 **/*log*.py에 일치하는 파일을 나열하고, 차례로 Read로 읽으며 출력 위치를 찾습니다.
  - EN: Use Glob to list files matching **/*error*.py and **/*log*.py, and read them one by one with Read to look for where it is output.
- C. JA: Grepで関数名apply_wafer_offsetをコードベース全体から検索し、すべての呼び出し元を洗い出す。
  - KO: Grep으로 함수 이름 apply_wafer_offset을 코드베이스 전체에서 검색해, 모든 호출 위치를 찾아냅니다.
  - EN: Use Grep to search the entire codebase for the function name apply_wafer_offset and identify all callers.
- D. JA: GrepでALIGN_TIMEOUT: stage not readyの文字列を検索し、出力している箇所を特定する。
  - KO: Grep으로 ALIGN_TIMEOUT: stage not ready 문자열을 검색해, 출력하는 위치를 찾아냅니다.
  - EN: Use Grep to search for the string ALIGN_TIMEOUT: stage not ready and identify where it is output.

## CCAR-F-Udemy06-0047

**JA** ある音楽配信サービスの開発チームは、Claude Codeのスキルとして/release-notesを作成し、.claude/skills/release-notes/SKILL.mdをリポジトリにコミットしています。このスキルは、指定したバージョンタグ以降のコミットからリリースノートを作り、社内のチャットに投稿します。

運用を始めると、次の2つの問題が起きました。

開発者が「最近の変更をまとめて」と頼んだだけで、Claudeがこのスキルを自動で読み込み、投稿まで行ってしまった

開発者がタグを付けずに/release-notesを実行し、意図しない範囲のノートが作られることが多い

SKILL.mdのフロントマターに加える変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 음악 streaming 서비스의 개발팀은 Claude Code skill로 /release-notes를 만들고 .claude/skills/release-notes/SKILL.md를 저장소에 commit했습니다. 이 skill은 지정한 버전 태그 이후의 commit으로 릴리스 노트를 만들어 사내 채팅에 게시합니다.

운영을 시작하자 다음 두 가지 문제가 생겼습니다.

개발자가 "최근 변경 사항을 정리해 줘"라고 요청했을 뿐인데, Claude가 이 skill을 자동으로 불러와 게시까지 해 버렸습니다

개발자가 태그를 지정하지 않고 /release-notes를 실행해, 의도하지 않은 범위의 노트가 만들어지는 경우가 많습니다

SKILL.md의 frontmatter에 추가할 변경으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: context: forkを設定し、スキルを分離されたサブエージェントのコンテキストで実行させる。
  - KO: context: fork를 설정해, skill을 분리된 subagent의 context에서 실행하게 합니다.
  - EN: Set context: fork to run the skill in the context of an isolated subagent.
- B. JA: disable-model-invocation: trueを設定し、明示的な呼び出しに限定する。
  - KO: disable-model-invocation: true를 설정해, 명시적으로 호출할 때만 실행되게 합니다.
  - EN: Set disable-model-invocation: true to limit invocation to explicit calls.
- C. JA: user-invocable: falseを設定し、スキルを「/」メニューに表示させない設定にする。
  - KO: user-invocable: false를 설정해, skill이 "/" 메뉴에 표시되지 않게 합니다.
  - EN: Set user-invocable: false so that the skill is not shown in the "/" menu.
- D. JA: argument-hintに[version-tag]を設定し、必要な引数を補完時に示す。
  - KO: argument-hint에 [version-tag]를 설정해, 필요한 인자를 자동 완성 때 보여 줍니다.
  - EN: Set argument-hint to [version-tag] to show the required argument during autocompletion.

## CCAR-F-Udemy06-0048

**JA** あるゲーム会社のマーケティング部門は、Claude APIを使って、競合タイトルの市場動向を調べるマルチエージェントリサーチシステムを構築しています。文書分析サブエージェントは、記事ごとに次の順でツールを呼び出します。

extract_metadataで、タイトル・発行元・公開日を抽出する

enrich_with_sales_dataで、販売データを付け加える

抽出の前にエンリッチメントが実行される問題を防ぐため、チームはすべてのリクエストでtool_choiceを{"type": "tool", "name": "extract_metadata"}に固定しました。

その結果、抽出は必ず最初に実行されるようになりました。しかし、enrich_with_sales_dataが一度も呼ばれず、同じ記事に対してextract_metadataが繰り返し呼ばれるようになりました。

最も適切な修正はどれですか。

**KO** 한 게임 회사의 마케팅 부서는 Claude API로 경쟁 타이틀의 시장 동향을 조사하는 multi-agent 리서치 시스템을 구축하고 있습니다. 문서 분석 subagent는 기사마다 다음 순서로 도구를 호출합니다.

extract_metadata로 제목·발행처·공개일을 추출합니다

enrich_with_sales_data로 판매 데이터를 덧붙입니다

추출보다 enrichment가 먼저 실행되는 문제를 막으려고, 팀은 모든 요청에서 tool_choice를 {"type": "tool", "name": "extract_metadata"}로 고정했습니다.

그 결과 추출은 항상 먼저 실행되게 되었습니다. 그러나 enrich_with_sales_data는 한 번도 호출되지 않고, 같은 기사에 대해 extract_metadata만 반복해서 호출되었습니다.

가장 적절한 수정은 무엇입니까?

- A. JA: 強制する設定は残し、enrich_with_sales_dataの説明に「extract_metadataの後に呼ぶ」と書き加える。
  - KO: 강제 설정은 그대로 두고, enrich_with_sales_data의 설명에 "extract_metadata 다음에 호출할 것"이라고 덧붙입니다.
  - EN: Keep the forcing setting and add "call after extract_metadata" to the description of enrich_with_sales_data.
- B. JA: ループの反復ごとに、tool_choiceで強制するツールを2つのツールの間で交互に切り替える。
  - KO: loop를 반복할 때마다 tool_choice로 강제하는 도구를 두 도구 사이에서 번갈아 바꿉니다.
  - EN: On each iteration of the loop, alternate the tool forced by tool_choice between the two tools.
- C. JA: tool_choiceを{"type": "any"}に変更し、どちらのツールを呼ぶかをモデルに選ばせる。
  - KO: tool_choice를 {"type": "any"}로 바꿔, 어느 도구를 호출할지 모델이 고르게 합니다.
  - EN: Change tool_choice to {"type": "any"} and let the model choose which tool to call.
- D. JA: 最初のリクエストだけでextract_metadataを強制し、後続のターンはtool_choiceをautoに戻す。
  - KO: 첫 요청에서만 extract_metadata를 강제하고, 이후 turn에서는 tool_choice를 auto로 되돌립니다.
  - EN: Force extract_metadata only on the first request, and set tool_choice back to auto for subsequent turns.

## CCAR-F-Udemy06-0049

**JA** ある化学メーカーの品質保証チームは、Claudeを使って、安全データシート（SDS）から成分名・CAS番号・危険有害性区分を抽出する仕組みを構築しています。抽出結果はJSONスキーマで検証してから、社内の化学物質管理システムに登録します。抽出は、毎晩12,000件の文書をMessage Batches APIでまとめて処理しています。

昨夜のバッチの結果は、次のとおりでした。

succeededが11,620件

erroredが240件

expiredが140件

erroredの240件はすべてinvalid_request_errorで、200ページを超える文書を1リクエストで送ったために、コンテキストの上限を超えていたことがわかりました。

翌晩までに残りの文書の抽出を完了させるための対応として適切なものはどれですか。（2つ選択してください。）

**KO** 한 화학 제조사의 품질보증팀은 Claude로 물질안전보건자료(SDS)에서 성분명·CAS 번호·유해위험성 분류를 추출하는 시스템을 구축하고 있습니다. 추출 결과는 JSON schema로 검증한 뒤 사내 화학물질 관리 시스템에 등록합니다. 추출은 매일 밤 12,000건의 문서를 Message Batches API로 일괄 처리합니다.

어젯밤 batch 결과는 다음과 같았습니다.

succeeded 11,620건

errored 240건

expired 140건

errored 240건은 모두 invalid_request_error였으며, 200페이지가 넘는 문서를 요청 하나로 보내는 바람에 context 한도를 넘었던 것으로 밝혀졌습니다.

다음 날 밤까지 나머지 문서의 추출을 끝내기 위한 대응으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: erroredの240件だけを、文書をチャンクに分割したリクエストに作り直して再送信する。
  - KO: errored 240건만, 문서를 청크로 나눈 요청으로 다시 만들어 재전송합니다.
  - EN: Rebuild only the 240 errored requests as requests that split the documents into chunks and resubmit them.
- B. JA: 12,000件すべてを新しいバッチで再送信し、結果は送信時の順序で元の文書と対応付ける。
  - KO: 12,000건 전체를 새 batch로 재전송하고, 결과는 전송한 순서대로 원래 문서와 대응시킵니다.
  - EN: Resubmit all 12,000 in a new batch, and match the results to the original documents by the order of submission.
- C. JA: erroredの240件はサーバー側の一時的なエラーとみなし、同じリクエストのまま次のバッチに再投入する。
  - KO: errored 240건은 서버 측의 일시적 오류로 보고, 같은 요청 그대로 다음 batch에 다시 넣습니다.
  - EN: Treat the 240 errored requests as transient server-side errors and put the same requests into the next batch as they are.
- D. JA: expiredの140件だけを、リクエストの内容はそのまま新しいバッチで再送信する。
  - KO: expired 140건만, 요청 내용은 그대로 두고 새 batch로 재전송합니다.
  - EN: Resubmit only the 140 expired requests in a new batch, with the request contents unchanged.

## CCAR-F-Udemy06-0050

**JA** ある医療機関グループは、Claude Agent SDKを使って、診療費の支払いや返金の問い合わせに対応するカスタマーサポート解決エージェントを運用しています。院内の規程では、3万円を超える返金はエージェントが処理せず、会計担当者の承認を経る必要があります。

システムプロンプトにこの規程を明記していますが、監査で、3万円を超える返金が月に数件process_refundで実行されていたことがわかりました。

規程を確実に守らせつつ、該当する問い合わせを適切に引き継ぐための変更として最も適切なものはどれですか。

**KO** 한 의료기관 그룹은 Claude Agent SDK로 진료비 결제와 환불 문의에 대응하는 고객 지원 해결 agent를 운영합니다. 원내 규정상 3만 엔을 넘는 환불은 agent가 처리하지 않고, 회계 담당자의 승인을 거쳐야 합니다.

system prompt에 이 규정을 명시해 두었지만, 감사에서 3만 엔을 넘는 환불이 매달 몇 건씩 process_refund로 실행된 사실이 드러났습니다.

규정을 확실히 지키게 하면서 해당 문의를 적절히 인계하기 위한 변경으로 가장 적절한 것은 무엇입니까?

- A. JA: PostToolUseフックで返金の結果を検査し、3万円を超えていた場合は会計担当者に即時通知する。
  - KO: PostToolUse hook으로 환불 결과를 검사하고, 3만 엔을 넘었으면 회계 담당자에게 즉시 알립니다.
  - EN: Inspect the refund result with a PostToolUse hook, and immediately notify the accounting officer if it exceeded 30,000 yen.
- B. JA: PreToolUseフックで3万円超の返金を拒否し、escalate_to_humanへ誘導する。
  - KO: PreToolUse hook으로 3만 엔 초과 환불을 거부하고, escalate_to_human으로 유도합니다.
  - EN: Reject refunds over 30,000 yen with a PreToolUse hook and redirect to escalate_to_human.
- C. JA: システムプロンプトの規程の記述を冒頭に移し、違反した場合の影響を具体的に説明する文を追加する。
  - KO: system prompt의 규정 문구를 맨 앞으로 옮기고, 위반했을 때의 영향을 구체적으로 설명하는 문장을 추가합니다.
  - EN: Move the description of the regulation to the beginning of the system prompt and add a sentence that specifically explains the consequences of violating it.
- D. JA: エージェントのツールからprocess_refundを外し、すべての返金を会計担当者に回す。
  - KO: agent의 도구에서 process_refund를 빼고, 모든 환불을 회계 담당자에게 넘깁니다.
  - EN: Remove process_refund from the agent's tools and route all refunds to the accounting officer.

## CCAR-F-Udemy06-0051

**JA** ある宅配便の会社は、Claude Agent SDKを使って、配達先の変更や再配達の依頼に対応するカスタマーサポート解決エージェントを運用しています。配達先の変更は、SMSのワンタイムコードによる本人確認が完了してからchange_delivery_addressを呼び出す手順で、システムプロンプトでこの順序を指示しています。

評価では99.2%のケースで順序が守られていましたが、残りのケースでは本人確認の前に配達先が変更されていました。チームリーダーは「指示の書き方をさらに工夫すれば100%にできるはずだ」と考えています。

この考えに対する評価として最も適切なものはどれですか。

**KO** 한 택배 회사는 Claude Agent SDK로 배송지 변경과 재배송 요청에 대응하는 고객 지원 해결 agent를 운영합니다. 배송지 변경은 SMS 일회용 코드로 본인 확인을 마친 뒤에 change_delivery_address를 호출하는 절차이며, system prompt에서 이 순서를 지시하고 있습니다.

평가에서는 99.2%의 케이스에서 순서가 지켜졌지만, 나머지 케이스에서는 본인 확인 전에 배송지가 변경되었습니다. 팀 리더는 "지시를 쓰는 방식을 더 다듬으면 100%로 만들 수 있을 것"이라고 생각합니다.

이 생각에 대한 평가로 가장 적절한 것은 무엇입니까?

- A. JA: 指示は確率的にしか守られないため、確実に防ぐには本人確認の完了をコードで検査する前提条件が必要である。
  - KO: 지시는 확률적으로만 지켜지므로, 확실히 막으려면 본인 확인 완료 여부를 코드로 검사하는 전제 조건이 필요합니다.
  - EN: Instructions are followed only probabilistically, so to reliably prevent this, a prerequisite that checks in code that identity verification has been completed is needed.
- B. JA: temperatureを0に設定すれば、同じ入力に対して同じ手順が選ばれ、順序の誤りは再現しなくなる。
  - KO: temperature를 0으로 설정하면 같은 입력에 대해 같은 절차가 선택되므로, 순서 오류는 더 이상 재현되지 않습니다.
  - EN: If temperature is set to 0, the same procedure will be chosen for the same input, and the ordering error will no longer reproduce.
- C. JA: few-shotの例で正しい順序を十分に示せば、振る舞いが決定論的になり、順序が逆になるケースはなくなる。
  - KO: few-shot 예시로 올바른 순서를 충분히 보여 주면 동작이 결정론적이 되어, 순서가 뒤바뀌는 케이스는 사라집니다.
  - EN: If few-shot examples sufficiently demonstrate the correct order, behavior becomes deterministic and cases with the reversed order will disappear.
- D. JA: 指示の改善を続ければ遵守率は100%に近づくので、評価セットを増やして改善を繰り返すべきである。
  - KO: 지시를 계속 개선하면 준수율은 100%에 가까워지므로, 평가 세트를 늘려 개선을 반복해야 합니다.
  - EN: If instructions continue to be improved, the compliance rate will approach 100%, so the evaluation set should be expanded and improvements repeated.

## CCAR-F-Udemy06-0052

**JA** ある損害保険会社の開発チームは、保険金支払いシステムの改修にClaude Codeを使っています。チームは、承認済みの最新の支払いルールを返す社内MCPサーバーを.mcp.jsonで共有しており、このサーバーにはsearch_rules（説明は「ルールを検索する」）というツールがあります。チームのClaude Codeでは、組み込みのRead・Grep・Globが有効になっています。

ところが、Claudeは支払いルールに関する質問のほとんどで、リポジトリ内を検索し、そこに残っている古いルールのコピーをもとに回答しています。search_rulesはほとんど呼ばれていません。

最も効果的な最初の一手はどれですか。

**KO** 한 손해보험사의 개발팀은 보험금 지급 시스템을 개선하는 데 Claude Code를 사용합니다. 팀은 승인된 최신 지급 규칙을 반환하는 사내 MCP server를 .mcp.json으로 공유하고 있으며, 이 서버에는 search_rules(설명은 "규칙을 검색한다")라는 도구가 있습니다. 팀의 Claude Code에서는 기본 제공 Read·Grep·Glob이 활성화되어 있습니다.

그런데 Claude는 지급 규칙에 관한 질문 대부분에서 저장소 안을 검색해, 거기에 남아 있는 오래된 규칙 사본을 바탕으로 답하고 있습니다. search_rules는 거의 호출되지 않습니다.

가장 효과적인 첫 조치는 무엇입니까?

- A. JA: 開発者が依頼するたびに、依頼文の中で「search_rulesを使って」とツールを指定する運用にする。
  - KO: 개발자가 요청할 때마다 요청문 안에서 "search_rules를 사용해"라고 도구를 지정하도록 운영합니다.
  - EN: Establish a practice in which developers specify the tool in the request each time, such as "use search_rules."
- B. JA: permissionsのdenyルールでGrepを禁止し、リポジトリ内を検索させなくする。
  - KO: permissions의 deny 규칙으로 Grep을 금지해, 저장소 안을 검색하지 못하게 합니다.
  - EN: Prohibit Grep with a permissions deny rule so that it can no longer search within the repository.
- C. JA: CLAUDE.mdに「支払いルールの質問には必ずsearch_rulesを使うこと」と書き加える。
  - KO: CLAUDE.md에 "지급 규칙 질문에는 반드시 search_rules를 사용할 것"이라고 추가합니다.
  - EN: Add "Always use search_rules for questions about payment rules" to CLAUDE.md.
- D. JA: search_rulesの説明に、承認済みの最新ルールを返すことと返却項目、使うべき場面を書き足す。
  - KO: search_rules의 설명에 승인된 최신 규칙을 반환한다는 점과 반환 항목, 사용해야 할 상황을 추가합니다.
  - EN: Add to the description of search_rules that it returns the latest approved rules, the fields it returns, and when it should be used.

## CCAR-F-Udemy06-0053

**JA** ある建設会社の工務部門は、Claudeを使って、協力会社から届く書類から構造化データを抽出し、原価管理システムに登録する仕組みを構築しています。

書類は見積書・請求書・工事変更指示書の3種類で、それぞれにextract_estimate、extract_invoice、extract_change_orderという抽出ツールをJSONスキーマ付きで定義しています。ただし、メールの添付ファイル名からは書類の種類がわかりません。

現在はtool_choiceをautoにしており、全体の約7%で、ツールを呼ばずに「この書類は請求書のようです」といった文章だけが返され、登録処理が止まっています。

書類の種類が不明なまま、確実に構造化出力を得るための変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 건설 회사의 공무 부서는 Claude로 협력업체에서 받은 서류에서 구조화 데이터를 추출해 원가 관리 시스템에 등록하는 시스템을 구축하고 있습니다.

서류는 견적서·청구서·공사 변경 지시서 세 종류이며, 각각 extract_estimate, extract_invoice, extract_change_order라는 추출 도구를 JSON schema와 함께 정의해 두었습니다. 다만 메일 첨부 파일 이름으로는 서류 종류를 알 수 없습니다.

현재는 tool_choice를 auto로 두고 있는데, 전체의 약 7%에서 도구를 호출하지 않고 "이 서류는 청구서로 보입니다" 같은 문장만 반환되어 등록 처리가 멈춥니다.

서류 종류를 모르는 상태에서도 구조화 출력을 확실히 얻기 위한 변경으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 文章だけの応答が返ったときは、その文章から書類の種類を正規表現で判定し、該当するツールで再実行する。
  - KO: 문장만 있는 응답이 반환되면, 그 문장에서 정규 표현식으로 서류 종류를 판정하고 해당 도구로 다시 실행합니다.
  - EN: When a text-only response is returned, determine the document type from that text using a regular expression and rerun with the corresponding tool.
- B. JA: tool_choiceを{"type": "tool", "name": "extract_invoice"}にして、件数の多い請求書のツールを強制する。
  - KO: tool_choice를 {"type": "tool", "name": "extract_invoice"}로 해서, 건수가 많은 청구서용 도구를 강제합니다.
  - EN: Set tool_choice to {"type": "tool", "name": "extract_invoice"} to force the tool for invoices, which are the most numerous.
- C. JA: tool_choiceを{"type": "any"}にして、3つの抽出ツールのいずれかを必ず呼ばせる。
  - KO: tool_choice를 {"type": "any"}로 해서, 세 추출 도구 중 하나를 반드시 호출하게 합니다.
  - EN: Set tool_choice to {"type": "any"} so that one of the three extraction tools is always called.
- D. JA: 各抽出ツールの説明に、その書類に特有の記載項目と、ほかの2種類との見分け方を書く。
  - KO: 각 추출 도구의 설명에 그 서류에만 있는 기재 항목과, 나머지 두 종류와 구별하는 방법을 씁니다.
  - EN: In the description of each extraction tool, write the fields specific to that document and how to distinguish it from the other two types.

## CCAR-F-Udemy06-0054

**JA** ある航空会社の整備部門は、Claudeを使って、紙の整備記録をスキャンした文書から作業内容・部品番号・作業者・作業日を抽出し、整備管理システムに登録しています。1日に約2,000件の記録を処理しますが、内容を確認できるレビュー担当者は2名で、確認できるのは1日300件程度です。

現在は到着順に先頭の300件を確認しており、確認されなかった記録に部品番号の読み取り誤りが残っていることがありました。

限られたレビュー担当者の処理能力を有効に使うための設計として適切なものはどれですか。（2つ選択してください。）

**KO** 한 항공사의 정비 부서는 Claude로 종이 정비 기록을 스캔한 문서에서 작업 내용·부품 번호·작업자·작업일을 추출해 정비 관리 시스템에 등록합니다. 하루에 약 2,000건의 기록을 처리하지만, 내용을 확인할 수 있는 리뷰 담당자는 2명이고 하루에 확인할 수 있는 양은 300건 정도입니다.

현재는 도착 순서대로 앞의 300건을 확인하고 있는데, 확인하지 못한 기록에 부품 번호를 잘못 읽은 오류가 남아 있는 경우가 있었습니다.

제한된 리뷰 담당자의 처리 능력을 효과적으로 쓰기 위한 설계로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: フィールド単位の確信度を出力させ、ラベル付き検証セットでレビューのしきい値をキャリブレーションする。
  - KO: 필드 단위의 확신도를 출력하게 하고, 레이블이 붙은 검증 세트로 리뷰 임계값을 보정(calibration)합니다.
  - EN: Have it output field-level confidence, and calibrate the review threshold with a labeled validation set.
- B. JA: 文書ごとに確信度を1〜10で自己申告させ、8以上の文書はレビューせずにそのまま登録する。
  - KO: 문서마다 확신도를 1~10으로 자체 보고하게 하고, 8 이상인 문서는 리뷰 없이 그대로 등록합니다.
  - EN: Have it self-report a confidence from 1 to 10 for each document, and register documents scoring 8 or higher as they are without review.
- C. JA: 2,000件から300件を無作為に選んで確認し、選ばれなかった記録はそのまま登録する。
  - KO: 2,000건 중 300건을 무작위로 골라 확인하고, 선택되지 않은 기록은 그대로 등록합니다.
  - EN: Randomly select 300 of the 2,000 records to check, and register the records that were not selected as they are.
- D. JA: 確信度の低い抽出や、記載があいまいな、または矛盾している記録を優先してレビューに回す。
  - KO: 확신도가 낮은 추출이나, 기재 내용이 모호하거나 모순되는 기록을 우선 리뷰로 보냅니다.
  - EN: Prioritize for review the extractions with low confidence and the records whose entries are ambiguous or contradictory.

## CCAR-F-Udemy06-0055

**JA** あるEC物流企業の開発チームは、Claude Agent SDKを使って、エンジニアが不慣れなコードベースを探索するための開発者の生産性向上ツールを構築しています。

あるエンジニアが、このツールで倉庫管理システムの出荷引当の仕組みを2時間かけて調べていたところ、会話の後半になって次のような変化が見られました。

エージェントが、序盤に特定したAllocationPlannerやReservationLedgerといった具体的なクラスに触れず、「一般的な在庫引当のパターンでは」といった一般論で答えるようになった

以前の回答と食い違う説明も出てきた

この状況への対策として最も適切なものはどれですか。

**KO** 한 전자상거래 물류 기업의 개발팀은 Claude Agent SDK로 엔지니어가 익숙하지 않은 코드베이스를 탐색하기 위한 개발자 생산성 도구를 구축하고 있습니다.

한 엔지니어가 이 도구로 창고 관리 시스템의 출고 할당 구조를 2시간 동안 조사하던 중, 대화 후반에 다음과 같은 변화가 나타났습니다.

agent가 초반에 찾아낸 AllocationPlanner나 ReservationLedger 같은 구체적인 클래스를 언급하지 않고, "일반적인 재고 할당 패턴에서는" 같은 일반론으로 답하게 되었습니다

이전 답변과 어긋나는 설명도 나오기 시작했습니다

이 상황에 대한 대책으로 가장 적절한 것은 무엇입니까?

- A. JA: 回答のたびに「一般論ではなく具体的なクラス名で答えること」とエンジニアが指示を付け加える。
  - KO: 답변을 구할 때마다 엔지니어가 "일반론이 아니라 구체적인 클래스 이름으로 답할 것"이라는 지시를 덧붙입니다.
  - EN: Have the engineer add an instruction to every request, such as "answer with specific class names, not generalities."
- B. JA: より大きなコンテキストウィンドウを持つモデルに切り替えて、長い会話でも履歴を保持させる。
  - KO: 더 큰 context window를 가진 모델로 바꿔, 긴 대화에서도 이력을 유지하게 합니다.
  - EN: Switch to a model with a larger context window so that it retains the history even in long conversations.
- C. JA: /clearで会話をリセットして新しいセッションを始め、最初から同じ調査をやり直させる。
  - KO: /clear로 대화를 초기화하고 새 session을 시작해, 처음부터 같은 조사를 다시 하게 합니다.
  - EN: Reset the conversation with /clear, start a new session, and have it redo the same investigation from the beginning.
- D. JA: 主要な調査結果をスクラッチパッドファイルに記録させ、以降の質問ではそれを参照させる。
  - KO: 주요 조사 결과를 scratchpad 파일에 기록하게 하고, 이후 질문에서는 그 파일을 참조하게 합니다.
  - EN: Have it record key findings in a scratchpad file and refer to that file for subsequent questions.

## CCAR-F-Udemy06-0056

**JA** あるホテルチェーンの経営企画部は、Claude Agent SDKを使って、宿泊客の口コミや競合ホテルの情報を調査するマルチエージェントリサーチシステムを構築しています。

文書分析サブエージェントには、analyze_reviewという汎用ツールが1つだけあります。このツールは、自由記述のinstructionパラメータで「評価点を抜き出す」「要約する」「主張が口コミに書かれているかを確かめる」といった処理を指定して使います。

ログを見ると、同じ目的でもinstructionの書き方が毎回異なり、出力の形式もばらばらでした。そのため、統合エージェントが結果を読み取れないケースが18%ありました。

この問題に対処する変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 호텔 체인의 경영기획부는 Claude Agent SDK로 투숙객 후기와 경쟁 호텔 정보를 조사하는 multi-agent 리서치 시스템을 구축하고 있습니다.

문서 분석 subagent에는 analyze_review라는 범용 도구 하나만 있습니다. 이 도구는 자유 형식의 instruction 파라미터에 "평점을 뽑아낸다", "요약한다", "주장이 후기에 적혀 있는지 확인한다" 같은 처리를 지정해 사용합니다.

로그를 보면 같은 목적이라도 instruction을 쓰는 방식이 매번 달랐고, 출력 형식도 제각각이었습니다. 그 때문에 통합 agent가 결과를 읽어 내지 못한 경우가 18%였습니다.

이 문제에 대처하는 변경으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: analyze_reviewを評価点の抽出、要約、主張の検証の目的別ツールに分ける。
  - KO: analyze_review를 평점 추출, 요약, 주장 검증이라는 목적별 도구로 나눕니다.
  - EN: Split analyze_review into purpose-specific tools for rating extraction, summarization, and claim verification.
- B. JA: 統合エージェントのシステムプロンプトに、形式の異なる結果の読み取り方を詳しく書き加える。
  - KO: 통합 agent의 system prompt에 형식이 다른 결과를 읽는 방법을 자세히 추가합니다.
  - EN: Add detailed instructions to the synthesis agent's system prompt on how to read results in different formats.
- C. JA: instructionパラメータの説明に、よく使う指示文の書き方の例を10件追加する。
  - KO: instruction 파라미터 설명에 자주 쓰는 지시문 작성 예시를 10개 추가합니다.
  - EN: Add ten examples of commonly used instruction phrasing to the description of the instruction parameter.
- D. JA: ツールの入力と出力をJSONスキーマで定義し、説明に使う場面と使わない場面を書く。
  - KO: 도구의 입력과 출력을 JSON schema로 정의하고, 설명에 사용할 상황과 사용하지 않을 상황을 씁니다.
  - EN: Define the tool's input and output with a JSON schema, and write in the description when to use it and when not to.

## CCAR-F-Udemy06-0057

**JA** あるスポーツデータ配信会社の開発チームは、エンジニアが不慣れなコードベースやレガシーシステムを理解するためにClaude Codeを活用しています。

あるエンジニアが、試合速報の配信サービスで使われている定期ポーリング方式の取り込み処理について、webhook方式・メッセージキュー方式・現行方式の改良のどれに置き換えるべきかを比較するよう、直接実行で依頼しました。すると、Claudeは1つ目の方式を調べている途中で12ファイルの編集を始めてしまい、比較を終える前に変更を元に戻す作業が発生しました。

同じ手戻りを防ぐために、このエンジニアが次に取るべきアプローチとして最も適切なものはどれですか。

**KO** 한 스포츠 데이터 제공 회사의 개발팀은 엔지니어가 익숙하지 않은 코드베이스나 레거시 시스템을 이해하는 데 Claude Code를 활용합니다.

한 엔지니어가 경기 속보 제공 서비스에서 쓰는 주기적 폴링 방식의 수집 처리를 webhook 방식·메시지 큐 방식·현행 방식 개선 중 어느 것으로 바꿔야 할지 비교해 달라고 직접 실행으로 요청했습니다. 그러자 Claude는 첫 번째 방식을 조사하던 도중에 파일 12개를 편집하기 시작했고, 비교를 끝내기도 전에 변경을 되돌리는 작업이 생겼습니다.

같은 재작업을 막기 위해 이 엔지니어가 다음에 취할 접근 방식으로 가장 적절한 것은 무엇입니까?

- A. JA: 直接実行のまま方式ごとに依頼を分け、結果が気に入らなければ/rewindでチェックポイントまで戻す。
  - KO: 직접 실행을 유지한 채 방식별로 요청을 나누고, 결과가 마음에 들지 않으면 /rewind로 checkpoint까지 되돌립니다.
  - EN: Stay in direct execution and split the request by approach, and if the result is not satisfactory, go back to a checkpoint with /rewind.
- B. JA: プランモードに切り替えて3つの方式を調査・比較させ、提示された計画を確認してから実装に進む。
  - KO: plan mode로 전환해 세 방식을 조사·비교하게 하고, 제시된 계획을 확인한 뒤 구현으로 넘어갑니다.
  - EN: Switch to plan mode, have it investigate and compare the three approaches, and proceed to implementation after reviewing the plan it presents.
- C. JA: acceptEditsモードに切り替え、各方式の試作をすべて実装させてからテスト結果で比較する。
  - KO: acceptEdits 모드로 전환해 각 방식의 시제품을 모두 구현하게 한 뒤, 테스트 결과로 비교합니다.
  - EN: Switch to acceptEdits mode, have it implement prototypes of all the approaches, and then compare them using test results.
- D. JA: CLAUDE.mdに「承認するまでファイルを編集しないこと」と書き、直接実行のまま同じ依頼をやり直す。
  - KO: CLAUDE.md에 "승인할 때까지 파일을 편집하지 말 것"이라고 쓰고, 직접 실행 상태에서 같은 요청을 다시 합니다.
  - EN: Write "do not edit files until I approve" in CLAUDE.md and redo the same request in direct execution.

## CCAR-F-Udemy06-0058

**JA** ある出版社の開発チームは、電子書籍の制作システムのリポジトリで、継続的インテグレーションにClaude Codeを組み込んでいます。EPUBの検証でエラーが出ると、Claudeがclaude -pで修正を作成し、修正用のプルリクエストを作ります。

人間が作成したプルリクエストは、pull_requestイベントで起動するレビュー用のワークフローが、別のclaude -pの実行でレビューしています。一方、Claudeが作成したプルリクエストは、このワークフローの対象から外しています。

代わりに、修正の実行が返したsession_idを使って、同じジョブで修正のセッションを再開しています。claude -p --resume "$SESSION_ID"を実行し、修正のセッションの続きとして「この修正をレビューして」と依頼しています。

過去2か月の集計では、人間のプルリクエストの約20%で指摘が出たのに対し、Claudeのプルリクエストへの指摘は1%未満でした。ところが、マージ後に目次のリンク切れや代替テキストの欠落が見つかった変更の多くは、Claudeが作成したものでした。

Claudeが作成した修正のレビューの効果を高めるための変更として適切なものはどれですか。（2つ選択してください。）

**KO** 한 출판사의 개발팀은 전자책 제작 시스템 저장소의 지속적 통합(CI)에 Claude Code를 넣어 두었습니다. EPUB 검증에서 오류가 나면 Claude가 claude -p로 수정을 만들고, 수정용 pull request를 생성합니다.

사람이 만든 pull request는 pull_request 이벤트로 시작되는 리뷰용 workflow가 별도의 claude -p 실행으로 리뷰합니다. 반면 Claude가 만든 pull request는 이 workflow의 대상에서 제외하고 있습니다.

대신 수정 실행이 반환한 session_id를 사용해, 같은 job에서 수정 session을 재개합니다. claude -p --resume "$SESSION_ID"를 실행하고, 수정 session의 연장선에서 "이 수정을 리뷰해 줘"라고 요청합니다.

지난 2개월간 집계해 보니 사람의 pull request는 약 20%에서 지적이 나온 반면, Claude의 pull request에 대한 지적은 1% 미만이었습니다. 그런데 병합 후에 목차 링크 깨짐이나 대체 텍스트 누락이 발견된 변경의 상당수는 Claude가 만든 것이었습니다.

Claude가 만든 수정에 대한 리뷰의 효과를 높이기 위한 변경으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: Claudeが作成したプルリクエストも、人間のものと同じレビュー用のワークフローでレビューする。
  - KO: Claude가 만든 pull request도 사람이 만든 것과 같은 리뷰용 workflow로 리뷰합니다.
  - EN: Review Claude-created pull requests with the same review workflow as human ones.
- B. JA: --resumeの実行に--append-system-promptを加え、レビュー担当の役割と確認項目を与える。
  - KO: --resume 실행에 --append-system-prompt를 추가해, 리뷰 담당 역할과 확인 항목을 줍니다.
  - EN: Add --append-system-prompt to the --resume run to give it a reviewer role and a list of items to check.
- C. JA: 修正の実行のプロンプトに「完了後に自分の差分をレビューする」と加え、1回で済ませる。
  - KO: 수정 실행의 prompt에 "완료 후 자신의 diff를 리뷰할 것"을 추가해, 한 번에 끝냅니다.
  - EN: Add "review your own diff after finishing" to the prompt of the fix run, and finish it in a single pass.
- D. JA: 修正の実行の最後に、差分のレビューをサブエージェントに任せ、新しいコンテキストで確認させる。
  - KO: 수정 실행의 마지막에 diff 리뷰를 subagent에 맡겨, 새 context에서 확인하게 합니다.
  - EN: At the end of the fix run, delegate the diff review to a subagent and have it check in a new context.

## CCAR-F-Udemy06-0059

**JA** ある銀行のシステム開発チームは、Claude Codeを使って融資審査システムの金利計算モジュールを調査しています。昨日のセッションでは、Claudeが計算モジュールの約30ファイルを読み、端数処理の不具合の原因について分析をまとめました。

今朝までに、別のメンバーが計算モジュールの大規模なリファクタリングをマージし、昨日読んだファイルのうち20ファイルが変更されています。チームリーダーは、昨日のセッションを--resumeで再開するよりも、昨日の結論を構造化したサマリーにまとめて新しいセッションを始めるべきだと判断しました。

この判断の理由として正しいものはどれですか。（2つ選択してください。）

**KO** 한 은행의 시스템 개발팀은 Claude Code로 대출 심사 시스템의 금리 계산 모듈을 조사하고 있습니다. 어제 session에서 Claude는 계산 모듈의 파일 약 30개를 읽고, 끝수 처리(반올림) 버그의 원인에 대한 분석을 정리했습니다.

오늘 아침까지 다른 팀원이 계산 모듈의 대규모 refactoring을 병합해, 어제 읽은 파일 중 20개가 변경되었습니다. 팀 리더는 어제 session을 --resume으로 재개하기보다, 어제의 결론을 구조화된 요약으로 정리해 새 session을 시작해야 한다고 판단했습니다.

이 판단의 이유로 옳은 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 再開したセッションで調査を続けると、昨日のセッションの記録が上書きされ、元の分析に戻れなくなるため。
  - KO: 재개한 session에서 조사를 계속하면 어제 session의 기록이 덮어써져, 원래 분석으로 돌아갈 수 없게 되기 때문입니다.
  - EN: Continuing the investigation in the resumed session would overwrite yesterday's session record, making it impossible to return to the original analysis.
- B. JA: 再開したセッションには変更前のファイルを読んだ結果が残っており、それを現在のコードとして扱うおそれがあるため。
  - KO: 재개한 session에는 변경 전 파일을 읽은 결과가 남아 있어, 그것을 현재 코드로 취급할 우려가 있기 때문입니다.
  - EN: The resumed session still contains the results of reading the pre-change files, and Claude might treat them as the current code.
- C. JA: サマリーなら確認済みの結論だけを引き継げ、変更で無効になった観察を持ち込まずに済むため。
  - KO: 요약이라면 확인된 결론만 넘겨받을 수 있어, 변경으로 무효가 된 관찰 내용을 가져오지 않아도 되기 때문입니다.
  - EN: A summary can carry over only the verified conclusions, avoiding bringing in observations that the changes have invalidated.
- D. JA: --resumeで再開すると会話履歴が自動で圧縮され、昨日読んだファイルの細かな内容が失われるため。
  - KO: --resume으로 재개하면 대화 이력이 자동으로 압축되어, 어제 읽은 파일의 세부 내용이 사라지기 때문입니다.
  - EN: Resuming with --resume automatically compresses the conversation history, losing the fine details of the files read yesterday.

## CCAR-F-Udemy06-0060

**JA** ある研究機関のデータ解析チームは、共同研究のコードを管理するリポジトリでClaude Codeを使っています。チームリーダーは、匿名化前のデータを扱うスクリプトでは必ず特定の暗号化ライブラリを使うという規則をClaudeに守らせており、リーダーの環境のClaude Codeはこの規則に従ってコードを生成します。

ところが、先月チームに加わった研究員の環境では、この規則を無視したコードが生成されていました。調べると、規則はリーダーの~/.claude/CLAUDE.mdに書かれており、リポジトリのCLAUDE.mdには書かれていませんでした。

最も適切な対応はどれですか。

**KO** 한 연구기관의 데이터 분석팀은 공동 연구 코드를 관리하는 저장소에서 Claude Code를 사용합니다. 팀 리더는 익명화 전 데이터를 다루는 스크립트에서는 반드시 특정 암호화 라이브러리를 사용한다는 규칙을 Claude가 지키게 하고 있으며, 리더 환경의 Claude Code는 이 규칙에 따라 코드를 생성합니다.

그런데 지난달 팀에 합류한 연구원의 환경에서는 이 규칙을 무시한 코드가 생성되고 있었습니다. 조사해 보니 규칙은 리더의 ~/.claude/CLAUDE.md에 적혀 있었고, 저장소의 CLAUDE.md에는 적혀 있지 않았습니다.

가장 적절한 대응은 무엇입니까?

- A. JA: 規則をリポジトリのルートに置いたCLAUDE.local.mdに移し、そのファイルを各自の環境に配布する。
  - KO: 규칙을 저장소 루트에 둔 CLAUDE.local.md로 옮기고, 그 파일을 각자의 환경에 배포합니다.
  - EN: Move the rule to a CLAUDE.local.md placed at the repository root, and distribute that file to each person's environment.
- B. JA: 新しい研究員に、リーダーの~/.claude/CLAUDE.mdをコピーして自分のホームディレクトリに置いてもらう。
  - KO: 새 연구원에게 리더의 ~/.claude/CLAUDE.md를 복사해 자신의 홈 디렉터리에 두게 합니다.
  - EN: Have the new researcher copy the leader's ~/.claude/CLAUDE.md and place it in their own home directory.
- C. JA: 規則をプロジェクトのCLAUDE.mdに移してコミットし、バージョン管理を通じてチーム全員に共有する。
  - KO: 규칙을 프로젝트의 CLAUDE.md로 옮겨 commit하고, 버전 관리를 통해 팀 전원과 공유합니다.
  - EN: Move the rule to the project's CLAUDE.md and commit it, sharing it with the whole team through version control.
- D. JA: 新しい研究員に、コードを生成させるたびにこの規則を依頼文に書き添えるよう案内する。
  - KO: 새 연구원에게 코드를 생성하게 할 때마다 이 규칙을 요청문에 덧붙이도록 안내합니다.
  - EN: Instruct the new researcher to add this rule to the prompt every time they have code generated.

## CCDV-F-Udemy-0001

**JA** あるオンライン旅行代理店が、旅程を手配する長時間実行のエージェントを運用しています。このエージェントは、数十回のツール呼び出しを行います。会話がコンテキストウィンドウの上限に近づき、処理を続けられなくなる問題が起きています。
有効なコンテキスト管理の手法はどれですか。（2つ選択してください。）

**KO** 한 온라인 여행사가 여행 일정을 예약하는 장시간 실행 agent를 운영하고 있습니다. 이 agent는 수십 번의 도구 호출을 합니다. 대화가 context window 한도에 가까워져 처리를 계속할 수 없게 되는 문제가 생기고 있습니다.
효과적인 context 관리 기법은 무엇입니까? (2개를 선택하십시오.)

- A. JA: コンテキスト編集のtool result clearingで、古いツール結果をコンテキストから除く。
  - KO: context editing의 tool result clearing으로 오래된 도구 결과를 context에서 제거합니다.
  - EN: Use tool result clearing, a form of context editing, to remove old tool results from the context.
- B. JA: コンパクションで会話の古いやり取りをサーバー側で要約に置き換え、コンテキストを縮める。
  - KO: compaction으로 대화의 오래된 주고받기를 서버 측에서 요약으로 대체해 context를 줄입니다.
  - EN: Use compaction to replace older exchanges in the conversation with a server-side summary, shrinking the context.
- C. JA: プロンプトキャッシングで会話履歴の接頭辞をキャッシュし、履歴部分の入力トークン料金を下げる。
  - KO: prompt caching으로 대화 이력의 접두부(prefix)를 캐시해, 이력 부분의 입력 토큰 요금을 낮춥니다.
  - EN: Use prompt caching to cache the conversation-history prefix, lowering the input token cost of the history portion.
- D. JA: 429や529のエラーが返ったときに、指数バックオフで同じリクエストを再送する。
  - KO: 429나 529 오류가 반환되면 exponential backoff로 같은 요청을 다시 보냅니다.
  - EN: When a 429 or 529 error is returned, resend the same request with exponential backoff.
- E. JA: max_tokensを引き上げ、1回の応答で生成できる出力トークン数の上限を増やす。
  - KO: max_tokens를 올려, 한 번의 응답에서 생성할 수 있는 출력 토큰 수의 상한을 늘립니다.
  - EN: Raise max_tokens to increase the limit on the number of output tokens that can be generated in a single response.

## CCDV-F-Udemy-0002

**JA** ある製薬会社が、規制対応が求められる本番システムでClaudeを利用します。
モデルを、新しいスナップショットに切り替わっていくエイリアスではなく、特定のスナップショット（固定バージョン）に固定する理由として、最も適切なものはどれですか。

**KO** 한 제약 회사가 규제 대응이 필요한 프로덕션 시스템에서 Claude를 사용합니다.
새 snapshot으로 계속 바뀌는 alias가 아니라 특정 snapshot(고정 버전)에 모델을 고정하는 이유로 가장 적절한 것은 무엇입니까?

- A. JA: 固定したスナップショットには廃止の予定がなく、同じモデルを期限なく使い続けられる。
  - KO: 고정한 snapshot은 폐기 예정이 없어, 같은 모델을 기한 없이 계속 쓸 수 있습니다.
  - EN: A pinned snapshot has no planned deprecation, so the same model can be used indefinitely.
- B. JA: 検証・承認した時点と同じモデルで動かし続け、意図しない切り替えによる挙動の変化を未然に防げる。
  - KO: 검증·승인한 시점과 같은 모델로 계속 운영해, 의도치 않은 전환으로 동작이 바뀌는 것을 미리 막을 수 있습니다.
  - EN: The system keeps running on the same model that was validated and approved, preventing behavior changes caused by unintended switches.
- C. JA: 固定したモデルIDは入力トークンの単価が下がり、規制対応システムの運用費を抑えられる。
  - KO: 고정한 모델 ID는 입력 토큰 단가가 낮아져, 규제 대응 시스템의 운영비를 줄일 수 있습니다.
  - EN: A pinned model ID has a lower per-token input price, keeping down the operating cost of the regulated system.
- D. JA: 後続モデルの改善が固定したIDにも自動で反映され、再検証なしで性能が上がっていく。
  - KO: 후속 모델의 개선이 고정한 ID에도 자동으로 반영되어, 재검증 없이 성능이 올라갑니다.
  - EN: Improvements in successor models are automatically applied to the pinned ID, so performance improves without revalidation.

## CCDV-F-Udemy-0003

**JA** ある会計事務所が、長年運用してきた大規模なレガシー連携コードのリファクタリングに着手します。
安全に進めるための方針として最も適切なものはどれですか。

**KO** 한 회계 사무소가 오랫동안 운영해 온 대규모 레거시 연계 코드의 refactoring에 착수합니다.
안전하게 진행하기 위한 방침으로 가장 적절한 것은 무엇입니까?

- A. JA: 既存の振る舞いを固定するテストを整え、小さな変更を段階的に重ねて都度検証する。
  - KO: 기존 동작을 고정하는 테스트를 갖추고, 작은 변경을 단계적으로 쌓아 가며 그때마다 검증합니다.
  - EN: Put tests in place that lock in the existing behavior, then make small changes incrementally and verify each one.
- B. JA: 振る舞いを変えない作業なので、機能追加とバグ修正も同じ変更にまとめて進める。
  - KO: 동작을 바꾸지 않는 작업이므로, 기능 추가와 버그 수정도 같은 변경에 묶어서 진행합니다.
  - EN: Because the work does not change behavior, bundle feature additions and bug fixes into the same change.
- C. JA: テストを書く工数を省き、変更のたびに担当者が画面操作で動作を確認して進める。
  - KO: 테스트 작성 공수를 생략하고, 변경할 때마다 담당자가 화면을 조작해 동작을 확인하며 진행합니다.
  - EN: Skip the effort of writing tests, and have the person in charge verify behavior by operating the UI after each change.
- D. JA: 新しい設計で全面的に書き直し、完成した時点で旧システムから一括で切り替える。
  - KO: 새 설계로 전면 재작성하고, 완성된 시점에 구 시스템에서 한꺼번에 전환합니다.
  - EN: Rewrite everything with a new design, and switch over from the old system all at once when it is complete.

## CCDV-F-Udemy-0004

**JA** ある出版社が、書籍原稿のレビューエージェントを構築しています。事実確認・文体チェック・引用の権利関係チェックを、それぞれ専門のサブエージェントに委任する設計を検討しています。どのチェックでも、大量の参考資料を読み込む必要があります。
サブエージェントによるコンテキストの分離で得られる利点として、最も適切なものはどれですか。

**KO** 한 출판사가 책 원고를 리뷰하는 agent를 구축하고 있습니다. 사실 확인·문체 점검·인용 권리 관계 점검을 각각 전문 subagent에 위임하는 설계를 검토하고 있습니다. 어느 점검이든 대량의 참고 자료를 읽어 들여야 합니다.
subagent로 context를 분리해서 얻는 이점으로 가장 적절한 것은 무엇입니까?

- A. JA: 親のシステムプロンプトがサブエージェントにも適用され、各チェックを同じ方針で進められる。
  - KO: 부모의 system prompt가 subagent에도 적용되어, 각 점검을 같은 방침으로 진행할 수 있습니다.
  - EN: The parent's system prompt also applies to the subagents, so every check can follow the same policy.
- B. JA: 資料の読み込みや途中のツール結果はサブエージェント内に留まり、親には最終結果だけが返る。
  - KO: 자료 읽기와 중간 도구 결과는 subagent 안에 머물고, 부모에게는 최종 결과만 반환됩니다.
  - EN: Material reading and intermediate tool results stay within the subagent, and only the final result is returned to the parent.
- C. JA: システム全体のトークン消費量が、処理を1つのエージェントで行う場合より少なくなる。
  - KO: 시스템 전체의 토큰 소비량이 하나의 agent로 처리할 때보다 적어집니다.
  - EN: Total token consumption across the system is lower than when a single agent does all the processing.
- D. JA: 各サブエージェントが親の会話履歴とツール結果を引き継ぎ、委任時の指示を短く書ける。
  - KO: 각 subagent가 부모의 대화 이력과 도구 결과를 이어받으므로, 위임할 때의 지시를 짧게 쓸 수 있습니다.
  - EN: Each subagent inherits the parent's conversation history and tool results, so delegation instructions can be kept short.

## CCDV-F-Udemy-0005

**JA** あるスポーツ分析サービスでは、Claudeで試合レポートを生成しています。開発チームは、同じ入力でも実行ごとに出力が変わることに気づきました。
サンプリングパラメータと非決定性について、temperatureの説明として正しいものはどれですか。

**KO** 한 스포츠 분석 서비스는 Claude로 경기 리포트를 생성합니다. 개발팀은 같은 입력이라도 실행할 때마다 출력이 달라진다는 것을 알아챘습니다.
샘플링 파라미터와 비결정성에 관해, temperature에 대한 설명으로 옳은 것은 무엇입니까?

- A. JA: temperatureは応答のレイテンシに作用するパラメータで、生成される内容には影響しない。
  - KO: temperature는 응답 latency에 작용하는 파라미터로, 생성되는 내용에는 영향을 주지 않습니다.
  - EN: temperature is a parameter that affects response latency and has no effect on the generated content.
- B. JA: temperatureを0にすれば、同じ入力に対して毎回まったく同じ出力が返ることが保証される。
  - KO: temperature를 0으로 하면 같은 입력에 대해 매번 완전히 같은 출력이 반환된다는 것이 보장됩니다.
  - EN: Setting temperature to 0 guarantees that exactly the same output is returned every time for the same input.
- C. JA: temperatureはサンプリングのランダム性を調整し、0にしても出力の完全な一致は保証されない。
  - KO: temperature는 샘플링의 무작위성을 조절하며, 0으로 해도 출력이 완전히 일치한다는 보장은 없습니다.
  - EN: temperature adjusts the randomness of sampling, and even at 0, an exact match of outputs is not guaranteed.
- D. JA: temperatureを上げると候補の語をより広く検討するため、生成される内容の事実の正確さが高まる。
  - KO: temperature를 올리면 후보 단어를 더 넓게 검토하므로, 생성되는 내용의 사실 정확도가 높아집니다.
  - EN: Raising temperature makes the model consider a wider range of candidate tokens, which increases the factual accuracy of the generated content.

## CCDV-F-Udemy-0006

**JA** ある物流企業が、配送計画システムを構築しようとしています。このシステムでは、道路状況・車両の空き・荷物の優先度に応じて、毎回異なる調査と再計画が必要になります。
システムは、中心となるマネージャー（オーケストレーター）と複数のワーカーLLMで構成する予定です。
このマネージャー／スーパーバイザー階層で、マネージャーの役割として最も適切なものはどれですか。

**KO** 한 물류 기업이 배송 계획 시스템을 구축하려고 합니다. 이 시스템에서는 도로 상황·차량 가용 여부·화물 우선순위에 따라 매번 다른 조사와 재계획이 필요합니다.
시스템은 중심이 되는 매니저(orchestrator)와 여러 워커 LLM으로 구성할 예정입니다.
이 매니저/슈퍼바이저 계층 구조에서 매니저의 역할로 가장 적절한 것은 무엇입니까?

- A. JA: 配送依頼を種別ごとに分類し、種別ごとに用意した専用のワーカーへ振り分ける。
  - KO: 배송 요청을 유형별로 분류해, 유형마다 준비한 전용 워커에 배분합니다.
  - EN: Classify delivery requests by type, and route each one to a dedicated worker prepared for that type.
- B. JA: 依頼の状況に応じてサブタスクを決めてワーカーへ委任し、結果を統合して計画にまとめる。
  - KO: 요청 상황에 따라 하위 작업(subtask)을 정해 워커에 위임하고, 결과를 통합해 계획으로 정리합니다.
  - EN: Decide on subtasks based on the situation of each request, delegate them to workers, and integrate the results into a plan.
- C. JA: 設計時に決めた順序でワーカーを呼び出し、前段の出力を次段の入力として渡していく。
  - KO: 설계 시점에 정한 순서대로 워커를 호출하며, 앞 단계의 출력을 다음 단계의 입력으로 넘깁니다.
  - EN: Call workers in an order fixed at design time, passing each stage's output as the next stage's input.
- D. JA: 全ワーカーに同じ計画タスクを並列で解かせ、出力の多数決で最終的な配送計画を選ぶ。
  - KO: 모든 워커에게 같은 계획 작업을 병렬로 풀게 하고, 출력의 다수결로 최종 배송 계획을 고릅니다.
  - EN: Have all workers solve the same planning task in parallel, and choose the final delivery plan by majority vote over their outputs.

## CCDV-F-Udemy-0007

**JA** ある海運企業のバッチ処理パイプラインが、負荷が高いときに、Claude APIから断続的にHTTP 429とHTTP 529を受け取っています。
リトライ設計として最も適切なものはどれですか。

**KO** 한 해운 기업의 batch 처리 pipeline이 부하가 높을 때 Claude API로부터 간헐적으로 HTTP 429와 HTTP 529를 받고 있습니다.
재시도 설계로 가장 적절한 것은 무엇입니까?

- A. JA: 429を受けたらバッチ全体をいったん停止し、原因を調べてから翌日に全件を再投入し直す。
  - KO: 429를 받으면 batch 전체를 일단 멈추고, 원인을 조사한 뒤 다음 날 전체 건을 다시 투입합니다.
  - EN: When a 429 is received, pause the entire batch, investigate the cause, and resubmit all items the next day.
- B. JA: 遅延を入れずにその場で再送を繰り返し、成功した時点ですぐ次のリクエストの処理に進めていく。
  - KO: 지연 없이 그 자리에서 재전송을 반복하고, 성공하는 즉시 다음 요청 처리로 넘어갑니다.
  - EN: Resend immediately and repeatedly without any delay, and move on to the next request as soon as one succeeds.
- C. JA: 400を含むあらゆるエラーを、固定の待ち時間をはさんで決まった回数だけ再試行し続ける。
  - KO: 400을 포함한 모든 오류를 고정 대기 시간을 두고 정해진 횟수만큼 계속 재시도합니다.
  - EN: Keep retrying every error, including 400, a fixed number of times with a fixed wait in between.
- D. JA: 429と529はジッター付き指数バックオフで再試行し、retry-afterに従う。
  - KO: 429와 529는 jitter를 넣은 exponential backoff로 재시도하고, retry-after를 따릅니다.
  - EN: Retry 429 and 529 with exponential backoff with jitter, and honor retry-after.

## CCDV-F-Udemy-0008

**JA** ある法務チームが、アップロードされた契約書1件を約40の条項に分け、条項ごとに独立したリスク判定をClaudeで行う機能を作っています。担当者は、画面の前で結果を待っています。
1件ずつ順番に呼び出すと、合計の待ち時間が長すぎます。一方で、組織のレート制限を超えて429を多発させることも避けたいと考えています。
Python SDKを使った実装として最も適切なものはどれですか。

**KO** 한 법무팀이 업로드된 계약서 1건을 약 40개 조항으로 나누고, 조항마다 독립적인 리스크 판정을 Claude로 수행하는 기능을 만들고 있습니다. 담당자는 화면 앞에서 결과를 기다립니다.
1건씩 차례로 호출하면 전체 대기 시간이 너무 깁니다. 한편 조직의 rate limit을 넘어 429가 자주 발생하는 것도 피하고 싶습니다.
Python SDK를 사용한 구현으로 가장 적절한 것은 무엇입니까?

- A. JA: クライアントのmax_retriesを大きくし、1件ずつの呼び出しが失敗したらSDKに自動で再送させる。
  - KO: 클라이언트의 max_retries를 크게 잡고, 1건씩 하는 호출이 실패하면 SDK가 자동으로 재전송하게 합니다.
  - EN: Increase the client's max_retries so that the SDK automatically resends each individual call when it fails.
- B. JA: 1件ずつの呼び出しをストリーミングに切り替え、各条項の結果が届き始めるまでの時間を短くする。
  - KO: 1건씩 하는 호출을 streaming으로 바꿔, 각 조항의 결과가 도착하기 시작할 때까지의 시간을 줄입니다.
  - EN: Switch each individual call to streaming to shorten the time until each clause's result starts arriving.
- C. JA: 40件をMessage Batches APIにまとめて投入し、処理の終了をポーリングしてから結果を表示する。
  - KO: 40건을 Message Batches API에 한꺼번에 투입하고, 처리가 끝날 때까지 폴링한 뒤 결과를 표시합니다.
  - EN: Submit the 40 requests together to the Message Batches API, poll until processing finishes, and then display the results.
- D. JA: AsyncAnthropicで40件を並行に送り、同時に処理中の件数をセマフォで一定数に抑える。
  - KO: AsyncAnthropic으로 40건을 동시에 보내고, 동시에 처리 중인 건수를 세마포어로 일정 수 이하로 제한합니다.
  - EN: Send the 40 requests concurrently with AsyncAnthropic, and use a semaphore to cap the number of requests in flight at a fixed number.

## CCDV-F-Udemy-0009

**JA** ある農業テック企業が、作物病害の現場報告を扱うClaudeアプリを設計しています。処理には、次の2つのサブタスクがあります。
自由記述の報告を、決められた病害カテゴリのいずれかに分類する
相互に影響する多数の制約を考慮して、多段階の灌漑・防除計画を立案する
フューショットプロンプティングと思考モード（エフォートや適応型思考）の使い分けとして、最も適切なものはどれですか。

**KO** 한 농업 테크 기업이 작물 병해 현장 보고를 다루는 Claude 앱을 설계하고 있습니다. 처리에는 다음 두 가지 하위 작업이 있습니다.
자유 형식 보고를 정해진 병해 카테고리 중 하나로 분류합니다
서로 영향을 주는 많은 제약을 고려해, 여러 단계로 된 관개·방제 계획을 세웁니다
few-shot prompting과 사고 모드(effort나 adaptive thinking)를 구분해 쓰는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: 計画立案のプロンプトに数十件の計画例を詰め込み、推論の深さは既定の設定のままにする。
  - KO: 계획 수립 prompt에 수십 건의 계획 예시를 채워 넣고, 추론 깊이는 기본 설정 그대로 둡니다.
  - EN: Pack dozens of example plans into the planning prompt, and leave the reasoning depth at the default setting.
- B. JA: 分類はフューショットプロンプティングで形式と境界を示し、計画立案はエフォートを高めて深く推論させる。
  - KO: 분류는 few-shot prompting으로 형식과 경계를 보여 주고, 계획 수립은 effort를 높여 깊이 추론하게 합니다.
  - EN: For classification, use few-shot prompting to show the format and boundaries; for planning, raise effort so the model reasons deeply.
- C. JA: 両タスクともゼロショットで指示だけを与え、エフォートを最小に設定して応答の速さを優先する。
  - KO: 두 작업 모두 zero-shot으로 지시만 주고, effort를 최소로 설정해 응답 속도를 우선합니다.
  - EN: For both tasks, give only instructions zero-shot, and set effort to the minimum to prioritize response speed.
- D. JA: 両タスクでエフォートをmaxに設定し、分類も計画立案も最も深い推論で処理させる。
  - KO: 두 작업 모두 effort를 max로 설정해, 분류도 계획 수립도 가장 깊은 추론으로 처리하게 합니다.
  - EN: Set effort to max for both tasks so that both classification and planning are handled with the deepest reasoning.

## CCDV-F-Udemy-0010

**JA** ある気象情報会社が、大規模な気象シミュレーション結果の要約生成を、長時間実行の非同期ジョブとして実装します。この処理には、数時間かかることもあります。
ジョブの完了をクライアントに伝える方式について、ポーリングとコールバック（Webhook）を比較した記述として最も適切なものはどれですか。

**KO** 한 기상 정보 회사가 대규모 기상 시뮬레이션 결과의 요약 생성을 장시간 실행되는 비동기 작업(job)으로 구현합니다. 이 처리는 몇 시간이 걸리기도 합니다.
작업 완료를 클라이언트에 알리는 방식에 대해, 폴링과 콜백(Webhook)을 비교한 설명으로 가장 적절한 것은 무엇입니까?

- A. JA: コールバックは受信URLを公開しておけば確実に届くため、再送や重複受信への備えは要らない。
  - KO: 콜백은 수신 URL만 공개해 두면 확실히 전달되므로, 재전송이나 중복 수신에 대비할 필요가 없습니다.
  - EN: Callbacks are delivered reliably as long as the receiving URL is exposed, so there is no need to prepare for redelivery or duplicate receipt.
- B. JA: ポーリングは単純だが検知の遅れと無駄な問合せが出て、コールバックは即時だが受信側の準備が要る。
  - KO: 폴링은 단순하지만 감지 지연과 불필요한 조회가 생기고, 콜백은 즉시 알 수 있지만 수신 측 준비가 필요합니다.
  - EN: Polling is simple but causes detection delays and wasted requests; callbacks are immediate but require preparation on the receiving side.
- C. JA: ポーリングは完了を即時に検知でき、コールバックは受信エンドポイントなしで実装できる。
  - KO: 폴링은 완료를 즉시 감지할 수 있고, 콜백은 수신 엔드포인트 없이 구현할 수 있습니다.
  - EN: Polling can detect completion immediately, and callbacks can be implemented without a receiving endpoint.
- D. JA: 同期呼び出しでHTTP接続を数時間ずっと保持し続ければ、ポーリングもコールバックも用意せずに済む。
  - KO: 동기 호출로 HTTP 연결을 몇 시간 동안 계속 유지하면, 폴링도 콜백도 준비할 필요가 없습니다.
  - EN: If a synchronous call keeps the HTTP connection open for several hours, neither polling nor callbacks are needed.

## CCDV-F-Udemy-0011

**JA** ある保険代理店には、自社のバックエンドからMessages APIを直接呼び出すアプリがあります。このアプリで、インターネットに公開済みのリモートMCPサーバー（Streamable HTTP）が提供する契約照会ツールを、Claudeに使わせたいと考えています。
MCPクライアントは自前で実装せず、MCPコネクタ（mcp_serversパラメータ）を使います。
この構成の設計として正しいものはどれですか。（2つ選択してください。）

**KO** 한 보험 대리점에는 자사 백엔드에서 Messages API를 직접 호출하는 앱이 있습니다. 이 앱에서, 인터넷에 이미 공개된 원격 MCP server(Streamable HTTP)가 제공하는 계약 조회 도구를 Claude가 사용하게 하려고 합니다.
MCP 클라이언트는 직접 구현하지 않고 MCP connector(mcp_servers 파라미터)를 사용합니다.
이 구성의 설계로 옳은 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: mcp_toolsetのconfigsで更新系ツールのenabledをfalseにし、照会系のツールだけを使わせる。
  - KO: mcp_toolset의 configs에서 갱신 계열 도구의 enabled를 false로 해, 조회 계열 도구만 사용하게 합니다.
  - EN: In the mcp_toolset configs, set enabled to false for tools that modify data so that only lookup tools are used.
- B. JA: mcp_serversにサーバーのURLと名前を定義し、tools配列のmcp_toolsetからその名前を参照する。
  - KO: mcp_servers에 서버의 URL과 이름을 정의하고, tools 배열의 mcp_toolset에서 그 이름을 참조합니다.
  - EN: Define the server's URL and name in mcp_servers, and reference that name from an mcp_toolset in the tools array.
- C. JA: サーバーがresourcesとして公開している約款文書も、mcp_toolsetで有効にしてClaudeに読ませる。
  - KO: 서버가 resources로 공개한 약관 문서도 mcp_toolset에서 활성화해 Claude가 읽게 합니다.
  - EN: Also enable, through mcp_toolset, the policy terms documents that the server exposes as resources, and have Claude read them.
- D. JA: 開発者PCでstdio起動している検証用のMCPサーバーも、mcp_serversに起動コマンドを書いて接続する。
  - KO: 개발자 PC에서 stdio로 실행 중인 검증용 MCP server도 mcp_servers에 실행 명령을 적어 연결합니다.
  - EN: Also connect the test MCP server running via stdio on a developer's PC by writing its launch command in mcp_servers.
- E. JA: Claudeがmcp_tool_useを返したら、アプリがtools/callをサーバーへ送り、結果をtool_resultで返す。
  - KO: Claude가 mcp_tool_use를 반환하면, 앱이 tools/call을 서버로 보내고 결과를 tool_result로 반환합니다.
  - EN: When Claude returns mcp_tool_use, the app sends tools/call to the server and returns the result as a tool_result.

## CCDV-F-Udemy-0012

**JA** ある鉄道会社が、乗客を案内するClaudeアシスタントを構築しています。
指示をシステムプロンプトとユーザーメッセージのどちらに置くかについて、原則として最も適切なものはどれですか。

**KO** 한 철도 회사가 승객을 안내하는 Claude 어시스턴트를 구축하고 있습니다.
지시를 system prompt와 사용자 메시지 중 어디에 둘지에 관해, 원칙적으로 가장 적절한 것은 무엇입니까?

- A. JA: 役割や安全上の制約はシステムプロンプトに置き、個別の問い合わせやデータはユーザーメッセージに置く。
  - KO: 역할과 안전상의 제약은 system prompt에 두고, 개별 문의나 데이터는 사용자 메시지에 둡니다.
  - EN: Place the role and safety constraints in the system prompt, and place individual inquiries and data in the user message.
- B. JA: 安全上の制約はユーザーメッセージの側に置き、問い合わせごとに内容を調整する。
  - KO: 안전상의 제약은 사용자 메시지 쪽에 두고, 문의마다 내용을 조정합니다.
  - EN: Place safety constraints on the user message side, and adjust their content for each inquiry.
- C. JA: 指示は毎回のユーザーメッセージの冒頭にまとめて書き、システムプロンプトは使わずに運用する。
  - KO: 지시는 매번 사용자 메시지 첫머리에 모아서 쓰고, system prompt는 쓰지 않고 운영합니다.
  - EN: Write all instructions together at the beginning of every user message, and operate without using the system prompt.
- D. JA: 乗客ごとの問い合わせ内容も含め、指示とデータを丸ごとシステムプロンプトに入れる。
  - KO: 승객별 문의 내용까지 포함해, 지시와 데이터를 통째로 system prompt에 넣습니다.
  - EN: Put all instructions and data, including each passenger's inquiry, into the system prompt.

## CCDV-F-Udemy-0013

**JA** あるセキュリティ運用センター（SOC）が、Claudeアプリを構築しています。このアプリで、自社インフラ内で動く社内SIEMへの独自クエリと、一般的なWeb検索の両方を行いたいと考えています。
クライアント側ツール（client tools）とサーバー側ツール（server tools）の実行場所と使い分けについて、正しいものはどれですか。

**KO** 한 보안 관제 센터(SOC)가 Claude 앱을 구축하고 있습니다. 이 앱에서 자사 인프라 안에서 동작하는 사내 SIEM에 대한 자체 쿼리와 일반 웹 검색을 모두 수행하려고 합니다.
클라이언트 측 도구(client tools)와 서버 측 도구(server tools)의 실행 위치와 용도 구분에 대해 옳은 것은 무엇입니까?

- A. JA: クライアント側ツールもAnthropicのインフラ上で実行され、社内のSIEMには接続できない。
  - KO: 클라이언트 측 도구도 Anthropic 인프라에서 실행되므로, 사내 SIEM에는 연결할 수 없습니다.
  - EN: Client tools are also executed on Anthropic's infrastructure and cannot connect to the internal SIEM.
- B. JA: サーバー側ツールは自分のアプリ内で実行され、実行コードを書いてtool_resultを返す。
  - KO: 서버 측 도구는 자신의 앱 안에서 실행되며, 실행 코드를 작성해 tool_result를 반환합니다.
  - EN: Server tools are executed within your own app; you write the execution code and return a tool_result.
- C. JA: 社内の独自システムにはサーバー側ツールで接続し、Web検索はクライアント側ツールとして自前で実装する。
  - KO: 사내 자체 시스템에는 서버 측 도구로 연결하고, 웹 검색은 클라이언트 측 도구로 직접 구현합니다.
  - EN: Connect to the internal custom system with a server tool, and implement web search yourself as a client tool.
- D. JA: SIEM照会のような自作ツールはアプリ内で実行され、Web検索はAnthropic側で実行される。
  - KO: SIEM 조회 같은 자체 제작 도구는 앱 안에서 실행되고, 웹 검색은 Anthropic 측에서 실행됩니다.
  - EN: Custom-built tools such as the SIEM query are executed within the app, and web search is executed on Anthropic's side.

## CCDV-F-Udemy-0014

**JA** CRMを提供するあるSaaS企業が、長時間実行のエージェントを構築します。このエージェントには、次の機能が必要です。
障害から再開できる耐久実行
人手による承認（human-in-the-loop）
状態の永続化
LangGraphのようなエージェントオーケストレーションフレームワークの採用についての判断として、最も適切なものはどれですか。

**KO** CRM을 제공하는 한 SaaS 기업이 장시간 실행 agent를 구축합니다. 이 agent에는 다음 기능이 필요합니다.
장애 후 재개할 수 있는 내구성 있는 실행(durable execution)
사람에 의한 승인(human-in-the-loop)
상태 영속화
LangGraph 같은 agent orchestration 프레임워크 도입에 대한 판단으로 가장 적절한 것은 무엇입니까?

- A. JA: 障害後の再開や状態の保存の仕組みを自作せずに済ませるために採用し、制御フローをグラフで定義する。
  - KO: 장애 후 재개나 상태 저장 구조를 직접 만들지 않기 위해 도입하고, 제어 흐름을 그래프로 정의합니다.
  - EN: Adopt it so that you do not have to build your own mechanisms for resuming after failures and saving state, and define the control flow as a graph.
- B. JA: LLMの呼び出し回数とトークン消費を自動で減らし、APIコストを下げるために採用する。
  - KO: LLM 호출 횟수와 토큰 소비를 자동으로 줄여 API 비용을 낮추기 위해 도입합니다.
  - EN: Adopt it to automatically reduce the number of LLM calls and token consumption, lowering API costs.
- C. JA: プロンプトやエージェントの構成を自分で書かずに済ませるために採用する。
  - KO: prompt나 agent 구성을 직접 작성하지 않기 위해 도입합니다.
  - EN: Adopt it so that you do not have to write prompts or agent configurations yourself.
- D. JA: 採用は見送り、Messages APIでツール使用ループを直接実装して、承認待ちの状態はプロセスのメモリに保持する。
  - KO: 도입은 보류하고 Messages API로 도구 사용 loop를 직접 구현하며, 승인 대기 상태는 프로세스 메모리에 유지합니다.
  - EN: Forgo adopting it, implement the tool use loop directly with the Messages API, and hold the pending-approval state in process memory.

## CCDV-F-Udemy-0015

**JA** あるEdTech企業が、K-12向けの教材を生成する指示（プロンプト）を、Claude Code・claude.ai・Messages APIの3つで試しました。すると、同じ指示でも解釈や出力が異なりました。
この違いの理由と対処として最も適切なものはどれですか。

**KO** 한 에듀테크 기업이 K-12용 교재를 생성하는 지시(prompt)를 Claude Code·claude.ai·Messages API 세 곳에서 시험해 보았습니다. 그러자 같은 지시인데도 해석과 출력이 달랐습니다.
이 차이의 이유와 대처로 가장 적절한 것은 무엇입니까?

- A. JA: 差の原因は指示の曖昧さにあるため、指示文を詳しく書き直して3つの出力をそろえる。
  - KO: 차이의 원인은 지시의 모호함에 있으므로, 지시문을 자세히 다시 써서 세 출력을 맞춥니다.
  - EN: The difference is caused by ambiguity in the instructions, so rewrite the instructions in more detail to make the three outputs consistent.
- B. JA: 各インターフェースが付け加える文脈が異なるため、文脈を制御できるAPI上に構築する。
  - KO: 각 인터페이스가 덧붙이는 context가 다르므로, context를 제어할 수 있는 API 위에서 구축합니다.
  - EN: Each interface adds different context, so build on the API, where you can control the context.
- C. JA: 3つは同じシステムプロンプトで動くため、差はモデルの不具合としてサポートに報告する。
  - KO: 세 곳 모두 같은 system prompt로 동작하므로, 차이는 모델 결함으로 보고 지원팀에 보고합니다.
  - EN: All three run with the same system prompt, so report the difference to support as a model defect.
- D. JA: 最も良い出力が出たインターフェースを1つに決め、残りの2つでの検証はやめる。
  - KO: 가장 좋은 출력이 나온 인터페이스 하나로 정하고, 나머지 둘에서의 검증은 그만둡니다.
  - EN: Settle on the one interface that produced the best output, and stop testing on the other two.

## CCDV-F-Udemy-0016

**JA** ある銀行が、登録住所の変更をチャットで受け付けるClaudeアシスタントを構築しています。手順は、必ず次の順序で進める必要があります。
本人確認
新住所の聞き取り
内容の復唱と同意
変更の実行
テストでは、利用者に急かされたClaudeが、本人確認の完了前に住所変更ツールを呼び出す事例が見つかりました。
この順序を確実に守らせる設計として最も適切なものはどれですか。

**KO** 한 은행이 등록 주소 변경을 채팅으로 접수하는 Claude 어시스턴트를 구축하고 있습니다. 절차는 반드시 다음 순서로 진행해야 합니다.
본인 확인
새 주소 묻기
내용 복창과 동의
변경 실행
테스트에서 사용자의 재촉을 받은 Claude가 본인 확인이 끝나기 전에 주소 변경 도구를 호출하는 사례가 발견되었습니다.
이 순서를 확실히 지키게 하는 설계로 가장 적절한 것은 무엇입니까?

- A. JA: エフォートを高い値に設定し、応答のたびにClaudeが手順を確認する推論の量を増やす。
  - KO: effort를 높은 값으로 설정해, 응답할 때마다 Claude가 절차를 확인하는 추론의 양을 늘립니다.
  - EN: Set effort to a high value to increase the amount of reasoning Claude spends checking the procedure on every response.
- B. JA: 現在の手順をアプリ側の状態として保持し、その状態で許可したツールだけをリクエストに含める。
  - KO: 현재 단계를 앱 측 상태로 유지하고, 그 상태에서 허용한 도구만 요청에 포함합니다.
  - EN: Keep the current step as state on the application side, and include in the request only the tools allowed in that state.
- C. JA: 次に進む手順名を毎回の応答でClaudeにJSONで出力させ、アプリはその値に従って処理を切り替える。
  - KO: 다음에 진행할 단계 이름을 매 응답마다 Claude가 JSON으로 출력하게 하고, 앱은 그 값에 따라 처리를 전환합니다.
  - EN: Have Claude output the name of the next step as JSON in every response, and have the app switch processing according to that value.
- D. JA: 手順の順序をシステムプロンプトに番号付きで明記し、順序どおりに進む対話をフューショットプロンプティングで示す。
  - KO: 절차 순서를 system prompt에 번호를 붙여 명시하고, 순서대로 진행하는 대화를 few-shot prompting으로 보여 줍니다.
  - EN: Spell out the order of the steps with numbers in the system prompt, and use few-shot prompting to demonstrate a dialogue that follows the order.

## CCDV-F-Udemy-0017

**JA** ある物流企業が、CIパイプラインにClaude Codeを組み込み、プルリクエストのコードレビューを自動化します。
ヘッドレスモードとsettings.jsonの使い方として最も適切なものはどれですか。

**KO** 한 물류 기업이 CI pipeline에 Claude Code를 넣어 pull request 코드 리뷰를 자동화합니다.
headless mode와 settings.json의 사용 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: プロジェクトのsettings.jsonでdefaultModeをbypassPermissionsにし、確認を一括で省く。
  - KO: 프로젝트의 settings.json에서 defaultMode를 bypassPermissions로 해, 확인을 일괄로 생략합니다.
  - EN: Set defaultMode to bypassPermissions in the project's settings.json to skip all confirmations at once.
- B. JA: -pで非対話実行し、必要なツールを--allowedToolsで事前に許可する。
  - KO: -p로 비대화형 실행하고, 필요한 도구를 --allowedTools로 미리 허용합니다.
  - EN: Run non-interactively with -p, and pre-approve the required tools with --allowedTools.
- C. JA: CLAUDE.mdに「CIでは確認なしで実行してよい」と書き、対話モードのまま起動する。
  - KO: CLAUDE.md에 "CI에서는 확인 없이 실행해도 된다"고 쓰고, 대화형 모드 그대로 실행합니다.
  - EN: Write "In CI, you may run without confirmation" in CLAUDE.md, and launch Claude Code in interactive mode.
- D. JA: 対話モードで起動し、表示される権限確認にはCI担当者がその都度応答して進める。
  - KO: 대화형 모드로 실행하고, 표시되는 권한 확인에는 CI 담당자가 그때그때 응답하며 진행합니다.
  - EN: Launch Claude Code in interactive mode, and have a CI engineer respond to each permission prompt as it appears.

## CCDV-F-Udemy-0018

**JA** あるゲーム開発会社が、ノンプレイヤーキャラクターのセリフ生成に使うClaudeのプロンプトを、頻繁に改良しています。
プロンプトの変更を通常のソフトウェア開発ライフサイクル（SDLC）に統合する方法として最も適切なものはどれですか。

**KO** 한 게임 개발사가 논플레이어 캐릭터의 대사 생성에 쓰는 Claude prompt를 자주 개선하고 있습니다.
prompt 변경을 일반적인 소프트웨어 개발 수명 주기(SDLC)에 통합하는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: プロンプトの変更は本番でA/Bテストにかけ、利用者の反応が良かった版を残していく。
  - KO: prompt 변경은 운영 환경에서 A/B 테스트에 부치고, 사용자 반응이 좋았던 버전을 남겨 갑니다.
  - EN: Put prompt changes through A/B tests in production, and keep the versions that get the best user response.
- B. JA: 企画担当が管理画面からプロンプトを直接編集できるようにし、変更を即時に本番へ反映する。
  - KO: 기획 담당자가 관리 화면에서 prompt를 직접 편집할 수 있게 하고, 변경을 즉시 운영 환경에 반영합니다.
  - EN: Let planners edit prompts directly from an admin screen, and apply changes to production immediately.
- C. JA: プロンプト本文は設定データベースで管理し、変更時はコミットメッセージに全文を記録する。
  - KO: prompt 본문은 설정 데이터베이스에서 관리하고, 변경할 때는 commit 메시지에 전문을 기록합니다.
  - EN: Manage the prompt text in a configuration database, and record the full text in the commit message whenever it changes.
- D. JA: プロンプトをリポジトリで管理し、プルリクエストでレビューと評価を通してからマージする。
  - KO: prompt를 저장소에서 관리하고, pull request로 리뷰와 평가를 거친 뒤에 병합합니다.
  - EN: Manage prompts in the repository, and merge changes only after they pass review and evaluation through a pull request.

## CCDV-F-Udemy-0019

**JA** あるEC企業が、返品対応エージェントを開発します。このエージェントは、返品ポリシー文書を読み込み、社内の返品処理スクリプトを実行します。
Anthropicのクライアント（Client）SDKでMessages APIを直接呼び出す方式と比べて、Claude Agent SDKを採用する利点として最も適切なものはどれですか。

**KO** 한 전자상거래 기업이 반품 처리 agent를 개발합니다. 이 agent는 반품 정책 문서를 읽고, 사내 반품 처리 스크립트를 실행합니다.
Anthropic의 Client SDK로 Messages API를 직접 호출하는 방식과 비교해, Claude Agent SDK를 도입하는 이점으로 가장 적절한 것은 무엇입니까?

- A. JA: 応答をストリーミングで逐次受け取れ、長い処理の途中経過をユーザーの画面に表示できる。
  - KO: 응답을 streaming으로 순차적으로 받을 수 있어, 긴 처리의 진행 상황을 사용자 화면에 표시할 수 있습니다.
  - EN: Responses can be received incrementally via streaming, so the progress of long tasks can be displayed on the user's screen.
- B. JA: エージェントをAnthropicのインフラ上でホストでき、実行環境やサンドボックスを運用せずに済む。
  - KO: agent를 Anthropic 인프라에서 호스팅할 수 있어, 실행 환경이나 sandbox를 운영하지 않아도 됩니다.
  - EN: The agent can be hosted on Anthropic's infrastructure, so you do not need to operate an execution environment or sandbox.
- C. JA: ファイル操作やコマンド実行の組み込みツールと、それらを実行して結果を返すエージェントループを利用できる。
  - KO: 파일 조작과 명령 실행을 위한 기본 제공 도구와, 그 도구를 실행해 결과를 돌려주는 agent loop를 이용할 수 있습니다.
  - EN: You can use built-in tools for file operations and command execution, along with an agent loop that executes those tools and returns the results.
- D. JA: claude.aiのアカウントでログインして動かせ、APIキーを発行せずに自社製品へ組み込める。
  - KO: claude.ai 계정으로 로그인해 실행할 수 있어, API 키를 발급하지 않고 자사 제품에 넣을 수 있습니다.
  - EN: The agent can run by logging in with a claude.ai account, so it can be embedded in your own product without issuing an API key.

## CCDV-F-Udemy-0020

**JA** ある小売企業のカスタマーサポートチャットでは、1人の顧客との対話が長時間続きます。
セッションの適切な管理（セッションハイジーン）の観点で、最も適切な設計はどれですか。

**KO** 한 소매 기업의 고객 지원 채팅에서는 고객 한 명과의 대화가 오래 이어집니다.
session의 적절한 관리(session hygiene) 관점에서 가장 적절한 설계는 무엇입니까?

- A. JA: 用件が変わっても同じセッションを使い続け、過去のやり取りを削らずに毎回送り直す。
  - KO: 용건이 바뀌어도 같은 session을 계속 쓰고, 과거 대화를 줄이지 않고 매번 다시 보냅니다.
  - EN: Keep using the same session even when the customer's request changes, and resend all past exchanges every time without trimming them.
- B. JA: 1Mトークンのコンテキストウィンドウを持つモデルを選び、全履歴を上限まで保持する。
  - KO: 1M 토큰 context window를 가진 모델을 골라, 전체 이력을 한도까지 유지합니다.
  - EN: Choose a model with a 1M-token context window, and keep the entire history up to the limit.
- C. JA: 会話の状態はサーバー側に保持させ、クライアントは毎回最新のメッセージだけを送る。
  - KO: 대화 상태는 서버 측이 유지하게 하고, 클라이언트는 매번 최신 메시지만 보냅니다.
  - EN: Have the server side hold the conversation state, and have the client send only the latest message each time.
- D. JA: 用件ごとにセッションを分け、古い履歴は要約したり削ったりして縮め、関連する文脈だけを残す。
  - KO: 용건마다 session을 나누고, 오래된 이력은 요약하거나 잘라 내서 줄이며, 관련된 context만 남깁니다.
  - EN: Use a separate session for each request, shrink old history by summarizing or trimming it, and keep only the relevant context.

## CCDV-F-Udemy-0021

**JA** ある自動車部品メーカーが、設計関連文書を編集するエージェントを運用しています。監査要件により、エージェントがファイルを変更したときは、例外なく毎回、監査ログに記録しなければなりません。
この要件を満たす実装として最も適切なものはどれですか。

**KO** 한 자동차 부품 제조사가 설계 관련 문서를 편집하는 agent를 운영하고 있습니다. 감사 요건에 따라 agent가 파일을 변경했을 때는 예외 없이 매번 감사 로그에 기록해야 합니다.
이 요건을 충족하는 구현으로 가장 적절한 것은 무엇입니까?

- A. JA: EditとWriteにマッチさせたPostToolUseFailureフックを設定し、監査記録スクリプトを実行する。
  - KO: Edit와 Write에 매칭되는 PostToolUseFailure hook을 설정해, 감사 기록 스크립트를 실행합니다.
  - EN: Configure a PostToolUseFailure hook matched to Edit and Write that runs an audit logging script.
- B. JA: 監査記録用のサブエージェントを定義し、ファイル変更後に呼び出すようメインエージェントに指示する。
  - KO: 감사 기록용 subagent를 정의하고, 파일 변경 후 호출하도록 메인 agent에 지시합니다.
  - EN: Define a subagent for audit logging, and instruct the main agent to call it after changing a file.
- C. JA: EditとWriteにマッチさせたPostToolUseフックを設定し、監査記録スクリプトを実行する。
  - KO: Edit와 Write에 매칭되는 PostToolUse hook을 설정해, 감사 기록 스크립트를 실행합니다.
  - EN: Configure a PostToolUse hook matched to Edit and Write that runs an audit logging script.
- D. JA: CLAUDE.mdに「ファイルを編集したら監査ログへ記録する」というルールを記載する。
  - KO: CLAUDE.md에 "파일을 편집하면 감사 로그에 기록한다"는 규칙을 적습니다.
  - EN: Add a rule to CLAUDE.md that says "When you edit a file, record it in the audit log."

## CCDV-F-Udemy-0022

**JA** ある電力会社が、送電網を監視するClaudeエージェントを運用しています。長時間のセッションでは、各ツールがセンサーデータなどの大量のデータを加工せずにそのまま返し、それがコンテキストにたまって、品質が下がるとともにコストとレイテンシが増えています。
コンテキストの肥大化を防ぐ緩和策として、最も適切なものはどれですか。

**KO** 한 전력 회사가 송전망을 감시하는 Claude agent를 운영하고 있습니다. 장시간 session에서는 각 도구가 센서 데이터 같은 대량의 데이터를 가공하지 않고 그대로 반환하고, 그것이 context에 쌓여 품질이 떨어지는 동시에 비용과 latency가 늘고 있습니다.
context 비대화를 막는 완화책으로 가장 적절한 것은 무엇입니까?

- A. JA: max_tokensを引き上げ、大きくなったコンテキストでも長い応答を最後まで出力させる。
  - KO: max_tokens를 올려, 커진 context에서도 긴 응답을 끝까지 출력하게 합니다.
  - EN: Raise max_tokens so that long responses are output to the end even with the enlarged context.
- B. JA: センサーデータを取得するツールの登録を外し、エージェントに生データを取得させない。
  - KO: 센서 데이터를 가져오는 도구의 등록을 해제해, agent가 원시 데이터를 가져오지 못하게 합니다.
  - EN: Unregister the tool that retrieves sensor data so that the agent cannot retrieve raw data.
- C. JA: ツール結果を必要な項目に絞ってから追加し、古いやり取りは要約して短くする。
  - KO: 도구 결과를 필요한 항목으로 좁힌 뒤에 추가하고, 오래된 대화는 요약해서 짧게 만듭니다.
  - EN: Narrow tool results down to the necessary fields before adding them, and summarize old exchanges to shorten them.
- D. JA: 1Mトークンのウィンドウを持つモデルへ移行し、ツールが返したデータをそのまま保持し続ける。
  - KO: 1M 토큰 window를 가진 모델로 옮기고, 도구가 반환한 데이터를 그대로 계속 유지합니다.
  - EN: Migrate to a model with a 1M-token window, and keep holding the data returned by tools as-is.

## CCDV-F-Udemy-0023

**JA** ある決済プラットフォームで、取引照合を行うClaudeベースのエージェントが断続的に失敗しています。トレースには、次の2種類の失敗が記録されています。
APIがHTTP 400 invalid_request_errorを返し、即座に失敗する
APIはHTTP 200を返すが、返ってきた本文を自社のパーサでバリデーションすると、不正な形式として弾かれる
これらの失敗が、統合レイヤー（自社のリクエスト構築・後処理コード）の不具合によるものか、モデル出力そのものの問題によるものかを切り分けるうえで、最も適切なアプローチはどれですか。

**KO** 한 결제 플랫폼에서 거래 대사를 수행하는 Claude 기반 agent가 간헐적으로 실패하고 있습니다. 트레이스에는 다음 두 종류의 실패가 기록되어 있습니다.
API가 HTTP 400 invalid_request_error를 반환하고 즉시 실패합니다
API는 HTTP 200을 반환하지만, 반환된 본문을 자사 파서로 검증하면 잘못된 형식으로 거부됩니다
이 실패들이 통합 계층(자사의 요청 구성·후처리 코드)의 결함 때문인지, 모델 출력 자체의 문제 때문인지 구분하는 데 가장 적절한 접근 방식은 무엇입니까?

- A. JA: max_tokensを引き上げて応答が途中で切れていないことを確かめ、同じ処理を再実行する。
  - KO: max_tokens를 올려 응답이 도중에 잘리지 않았는지 확인하고, 같은 처리를 다시 실행합니다.
  - EN: Raise max_tokens to confirm that responses are not being cut off, and then rerun the same processing.
- B. JA: 失敗したリクエストを一律に指数バックオフで再試行し、成功した場合は解決済みとみなす。
  - KO: 실패한 요청을 일률적으로 exponential backoff로 재시도하고, 성공하면 해결된 것으로 봅니다.
  - EN: Uniformly retry failed requests with exponential backoff, and treat them as resolved if they succeed.
- C. JA: 失敗をAPI境界で分類し、4xxは自社の組み立て、200後の不正は出力か後処理の問題とする。
  - KO: 실패를 API 경계에서 분류해, 4xx는 자사의 요청 구성 문제로, 200 이후의 잘못된 형식은 출력이나 후처리 문제로 봅니다.
  - EN: Classify failures at the API boundary: treat 4xx as a request-construction problem on your side, and malformed output after a 200 as an output or post-processing problem.
- D. JA: より大きなモデルに切り替えて同じ取引を処理し、失敗の頻度が下がるかどうかを観察する。
  - KO: 더 큰 모델로 바꿔 같은 거래를 처리하고, 실패 빈도가 줄어드는지 관찰합니다.
  - EN: Switch to a larger model to process the same transactions, and observe whether the failure frequency decreases.

## CCDV-F-Udemy-0024

**JA** ある監査法人が、子会社3社の監査報告書をまとめてClaudeに渡し、「3社に共通する内部統制上の指摘事項は何か」と尋ねる機能を作っています。報告書は1本あたり数万トークンあります。
現在のプロンプトでは、質問文を先頭に置き、その後ろに3本の報告書を区切りなしで連結しています。しかし、回答の質が安定せず、どの会社の報告書に基づく記述なのかも分かりにくくなっています。
プロンプトの構成の改善として最も適切なものはどれですか。

**KO** 한 회계법인이 자회사 3곳의 감사 보고서를 한꺼번에 Claude에 넘기고 "세 회사에 공통된 내부 통제상 지적 사항은 무엇인가"를 묻는 기능을 만들고 있습니다. 보고서는 한 건당 수만 토큰입니다.
현재 prompt는 질문을 맨 앞에 두고, 그 뒤에 보고서 세 건을 구분 없이 이어 붙였습니다. 그런데 답변 품질이 안정되지 않고, 어느 회사 보고서에 근거한 서술인지도 알기 어렵습니다.
prompt 구성 개선으로 가장 적절한 것은 무엇입니까?

- A. JA: エフォートを高い値に設定し、長い報告書を読み解く思考により多くのトークンを使わせる。
  - KO: effort를 높은 값으로 설정해, 긴 보고서를 해석하는 사고에 더 많은 토큰을 쓰게 합니다.
  - EN: Set effort to a high value so that more tokens are spent on thinking to interpret the long reports.
- B. JA: 3本の報告書をそれぞれ事前に要約させ、その要約だけを質問文の後ろに並べて渡す。
  - KO: 보고서 세 건을 각각 미리 요약하게 하고, 그 요약만 질문 뒤에 나열해 넘깁니다.
  - EN: Have each of the three reports summarized in advance, and pass only those summaries, placed after the question.
- C. JA: 報告書部分の末尾にcache_controlを付け、同じ報告書への2回目以降の質問を速く安くする。
  - KO: 보고서 부분 끝에 cache_control을 붙여, 같은 보고서에 대한 두 번째 이후 질문을 빠르고 저렴하게 합니다.
  - EN: Add cache_control at the end of the reports section to make the second and subsequent questions about the same reports faster and cheaper.
- D. JA: 報告書を先頭に置いて出典名付きのタグで1本ずつ囲み、質問文はその後ろの末尾に置く。
  - KO: 보고서를 맨 앞에 두고 출처명이 붙은 태그로 한 건씩 감싸며, 질문은 그 뒤 맨 끝에 둡니다.
  - EN: Place the reports first, wrapping each one in tags labeled with its source name, and place the question at the end, after the reports.

## CCDV-F-Udemy-0025

**JA** ある工作機械メーカーが、設備点検の予約や履歴照会のツールを提供する社内MCPサーバーを運用しています。このサーバーに、点検日程を変更するreschedule_inspectionツールを新たに追加しました。
このサーバーを使う複数のAIアプリ（ホスト）では、アプリ側のコードを変えずに、新しいツールとその引数をモデルに提示したいと考えています。
MCPでツールとその引数がクライアントに伝わる仕組みとして、正しいものはどれですか。

**KO** 한 공작기계 제조사가 설비 점검 예약과 이력 조회 도구를 제공하는 사내 MCP server를 운영하고 있습니다. 이 서버에 점검 일정을 변경하는 reschedule_inspection 도구를 새로 추가했습니다.
이 서버를 사용하는 여러 AI 앱(host)에서는 앱 측 코드를 바꾸지 않고, 새 도구와 그 인자를 모델에 제시하려고 합니다.
MCP에서 도구와 그 인자가 클라이언트에 전달되는 방식으로 옳은 것은 무엇입니까?

- A. JA: サーバーがpromptsとして公開したテンプレートに引数の説明を含め、利用者に選ばせてモデルへ渡す。
  - KO: 서버가 prompts로 공개한 템플릿에 인자 설명을 포함하고, 사용자가 고르게 해 모델에 넘깁니다.
  - EN: The server includes argument descriptions in templates it exposes as prompts, and the user selects one to pass to the model.
- B. JA: クライアントがtools/listを送り、返されたinputSchemaなどをモデル向けのツール定義に使う。
  - KO: 클라이언트가 tools/list를 보내고, 반환된 inputSchema 등을 모델용 도구 정의에 사용합니다.
  - EN: The client sends tools/list and uses the returned inputSchema and other fields for the tool definitions given to the model.
- C. JA: クライアントが空の引数でtools/callを試し、返されたエラーの内容から必要な引数をモデルに学ばせる。
  - KO: 클라이언트가 빈 인자로 tools/call을 시도하고, 반환된 오류 내용으로 필요한 인자를 모델이 학습하게 합니다.
  - EN: The client tries tools/call with empty arguments and has the model learn the required arguments from the returned error.
- D. JA: サーバーがresourcesとして公開したツール仕様書をクライアントが読み、引数の形式をモデルに推測させる。
  - KO: 서버가 resources로 공개한 도구 사양서를 클라이언트가 읽고, 인자 형식을 모델이 추측하게 합니다.
  - EN: The client reads a tool specification document that the server exposes as resources and has the model infer the argument format.

## CCDV-F-Udemy-0026

**JA** ある通信会社が、コールセンターのオペレーターに通話中の回答候補を提示する、Claudeを活用したアシスタントを企画しています。ビジネス要件は次の2つです。
回答候補の表示が1秒以内に始まること
ピーク時に300件の通話で同時利用できること
この要件から導かれる技術・インフラ要件として最も適切なものはどれですか。

**KO** 한 통신 회사가 콜센터 상담원에게 통화 중 답변 후보를 제시하는 Claude 기반 어시스턴트를 기획하고 있습니다. 비즈니스 요건은 다음 두 가지입니다.
답변 후보가 1초 이내에 표시되기 시작할 것
피크 시간대에 통화 300건에서 동시에 사용할 수 있을 것
이 요건에서 도출되는 기술·인프라 요건으로 가장 적절한 것은 무엇입니까?

- A. JA: ストリーミングで応答を逐次表示し、429エラーが返ったらretry-afterの秒数だけ待って同じ依頼を再試行する。
  - KO: streaming으로 응답을 순차 표시하고, 429 오류가 반환되면 retry-after에 적힌 초만큼 기다린 뒤 같은 요청을 재시도합니다.
  - EN: Display responses incrementally with streaming, and when a 429 error is returned, wait the number of seconds in retry-after and then retry the same request.
- B. JA: Message Batches APIで通話ごとの依頼をまとめて投入し、処理キューの上限に収まるよう件数を調整する。
  - KO: Message Batches API로 통화별 요청을 모아서 투입하고, 처리 큐 상한에 맞도록 건수를 조정합니다.
  - EN: Submit per-call requests together to the Message Batches API, adjusting the count to stay within the processing queue limit.
- C. JA: コンテキストウィンドウが1Mトークンのモデルを選定し、通話の全文字起こしを毎回の入力に含める。
  - KO: context window가 1M 토큰인 모델을 선정하고, 통화 전체 녹취록을 매번 입력에 포함합니다.
  - EN: Select a model with a 1M-token context window, and include the full call transcript in every input.
- D. JA: ストリーミングで応答を逐次表示し、ピーク時のリクエスト数とトークン量に見合うレート制限枠を確保する。
  - KO: streaming으로 응답을 순차 표시하고, 피크 시간대의 요청 수와 토큰량에 맞는 rate limit 한도를 확보합니다.
  - EN: Display responses incrementally with streaming, and secure rate limit capacity that matches the peak request volume and token volume.

## CCDV-F-Udemy-0027

**JA** ある非営利団体が、寄付者対応を支援するClaudeのワークフローを本番運用しています。
新しいモデルバージョンがリリースされたときに、モデルのリリース間で生じる挙動の変化に備える方法として、最も適切なものはどれですか。

**KO** 한 비영리 단체가 기부자 응대를 지원하는 Claude workflow를 운영 환경에서 쓰고 있습니다.
새 모델 버전이 출시될 때, 모델 릴리스 사이에 생기는 동작 변화에 대비하는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: 本番のモデルIDを固定し、新モデルは回帰評価で劣化がないと確かめてから移行する。
  - KO: 운영 환경의 모델 ID를 고정하고, 새 모델은 회귀 평가로 성능 저하가 없음을 확인한 뒤 이전합니다.
  - EN: Pin the production model ID, and migrate to the new model only after regression evaluation confirms that there is no degradation.
- B. JA: 新しいモデルは前の世代より優れているとみなし、既存プロンプトの再テストは省く。
  - KO: 새 모델은 이전 세대보다 우수하다고 보고, 기존 prompt의 재테스트는 생략합니다.
  - EN: Assume that the new model is better than the previous generation, and skip retesting existing prompts.
- C. JA: 移行前に新モデルでプロンプトを数件試し、応答の印象がよければ本番のモデルを切り替える。
  - KO: 이전하기 전에 새 모델로 prompt를 몇 건 시험해 보고, 응답 인상이 좋으면 운영 모델을 바꿉니다.
  - EN: Before migrating, try a few prompts on the new model, and switch the production model if the responses make a good impression.
- D. JA: 新モデルの公開日に本番のモデルIDを差し替え、問題が報告されたら元に戻す。
  - KO: 새 모델 공개일에 운영 환경의 모델 ID를 교체하고, 문제가 보고되면 되돌립니다.
  - EN: Swap the production model ID on the new model's release date, and roll back if problems are reported.

## CCDV-F-Udemy-0028

**JA** ある人材サービス企業が、外部の求人掲載サービスのREST APIと連携し、新しい求人をPOSTで登録するバッチを実装しています。ネットワークエラーやタイムアウトのときは、リクエストを再試行します。
RESTのステータスコードと冪等性を踏まえた実装として最も適切なものはどれですか。

**KO** 한 인재 서비스 기업이 외부 채용 공고 서비스의 REST API와 연동해, 새 채용 공고를 POST로 등록하는 batch를 구현하고 있습니다. 네트워크 오류나 timeout이 나면 요청을 재시도합니다.
REST 상태 코드와 멱등성을 고려한 구현으로 가장 적절한 것은 무엇입니까?

- A. JA: タイムアウトしたPOSTはPUTと同じく冪等とみなして再送し、重複した求人は後から手作業で削除する。
  - KO: timeout된 POST는 PUT처럼 멱등하다고 보고 재전송하며, 중복된 공고는 나중에 수작업으로 삭제합니다.
  - EN: Treat a timed-out POST as idempotent, like PUT, and resend it; delete any duplicate job postings manually afterward.
- B. JA: 5xxが返ったPOSTは登録済みとみなし、再送せずに次の求人の登録処理へ進む。
  - KO: 5xx가 반환된 POST는 등록된 것으로 보고, 재전송하지 않고 다음 공고 등록으로 넘어갑니다.
  - EN: Treat a POST that returned a 5xx as already registered, and move on to registering the next job posting without resending it.
- C. JA: 400が返ったリクエストも指数バックオフで再送し、成功するまで一定回数繰り返す。
  - KO: 400이 반환된 요청도 exponential backoff로 재전송하고, 성공할 때까지 일정 횟수 반복합니다.
  - EN: Resend requests that returned 400 as well, using exponential backoff, repeating up to a fixed number of times until they succeed.
- D. JA: 冪等キーの付与か登録済み確認をしてからPOSTを再送し、429以外の4xxは再送しない。
  - KO: 멱등 키를 붙이거나 이미 등록되었는지 확인한 뒤 POST를 재전송하고, 429 이외의 4xx는 재전송하지 않습니다.
  - EN: Resend a POST only after attaching an idempotency key or confirming whether it was already registered, and do not resend 4xx responses other than 429.

## CCDV-F-Udemy-0029

**JA** ある建設会社の開発チームが、Claude Codeのコーディング規約と権限設定を、チーム全体に配布したいと考えています。
CLAUDE.mdとsettings.jsonの配置と階層の理解として最も適切なものはどれですか。

**KO** 한 건설 회사의 개발팀이 Claude Code의 코딩 규약과 권한 설정을 팀 전체에 배포하려고 합니다.
CLAUDE.md와 settings.json의 배치와 계층에 대한 이해로 가장 적절한 것은 무엇입니까?

- A. JA: 共通の権限はCLAUDE.mdに文章で記載し、settings.jsonの内容は各メンバーに任せる。
  - KO: 공통 권한은 CLAUDE.md에 문장으로 적고, settings.json 내용은 각 구성원에게 맡깁니다.
  - EN: Describe the shared permissions in prose in CLAUDE.md, and leave the contents of settings.json up to each member.
- B. JA: 共通の設定は各メンバーの~/.claude/settings.jsonに配布し、リポジトリには置かない。
  - KO: 공통 설정은 각 구성원의 ~/.claude/settings.json에 배포하고, 저장소에는 두지 않습니다.
  - EN: Distribute the shared settings to each member's ~/.claude/settings.json, and do not put them in the repository.
- C. JA: 共通の規約はCLAUDE.md、共通の権限は.claude/settings.jsonに置きGitで共有する。
  - KO: 공통 규약은 CLAUDE.md에, 공통 권한은 .claude/settings.json에 두고 Git으로 공유합니다.
  - EN: Put the shared conventions in CLAUDE.md and the shared permissions in .claude/settings.json, and share both via Git.
- D. JA: 共通の規約と権限は.claude/settings.local.jsonに書いてコミットし、全員に同じ内容を配る。
  - KO: 공통 규약과 권한은 .claude/settings.local.json에 적어 commit하고, 모두에게 같은 내용을 배포합니다.
  - EN: Write the shared conventions and permissions in .claude/settings.local.json, commit it, and distribute the same contents to everyone.

## CCDV-F-Udemy-0030

**JA** あるニュースメディア企業が、長い記事の要約と、読者との複数ターンの対話を行うClaudeアプリを運用しています。
運用チームが理解しておくべき、トークン使用量とコンテキストウィンドウの基礎について、正しい記述はどれですか。

**KO** 한 뉴스 미디어 기업이 긴 기사 요약과 독자와의 여러 turn에 걸친 대화를 수행하는 Claude 앱을 운영하고 있습니다.
운영팀이 이해해 두어야 할 토큰 사용량과 context window의 기초에 대해 옳은 설명은 무엇입니까?

- A. JA: コンテキストウィンドウは応答の長さの上限で、入力の大きさはウィンドウとは別に管理される。
  - KO: context window는 응답 길이의 상한이며, 입력 크기는 window와 별도로 관리됩니다.
  - EN: The context window is the upper limit on response length; the size of the input is managed separately from the window.
- B. JA: ウィンドウには入力と出力の両方が数えられ、履歴を毎回送るため入力は会話とともに増える。
  - KO: window에는 입력과 출력이 모두 계산되며, 이력을 매번 보내므로 입력은 대화가 진행될수록 늘어납니다.
  - EN: Both input and output count toward the window, and because the history is sent every time, the input grows as the conversation goes on.
- C. JA: 出力トークンはウィンドウに数えられず、上限の対象になるのは送信した入力トークンに限られる。
  - KO: 출력 토큰은 window에 계산되지 않으며, 상한의 대상은 보낸 입력 토큰뿐입니다.
  - EN: Output tokens do not count toward the window; only the input tokens sent are subject to the limit.
- D. JA: 最新のユーザーメッセージだけが入力として課金され、過去のやり取りはサーバー側に保持される。
  - KO: 최신 사용자 메시지만 입력으로 과금되며, 과거 대화는 서버 측에 유지됩니다.
  - EN: Only the latest user message is billed as input; past exchanges are retained on the server side.

## CCDV-F-Udemy-0031

**JA** あるHR系SaaS企業が、チーム全体でClaude Codeのプラグイン（拡張機能）を導入します。
管理上の考慮点として適切なものはどれですか。（2つ選択してください。）

**KO** 한 HR SaaS 기업이 팀 전체에 Claude Code plugin(확장 기능)을 도입합니다.
관리상 고려할 점으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 各メンバーが好きなプラグインをユーザースコープで入れ、チームの共有設定は用意しない。
  - KO: 각 구성원이 원하는 plugin을 user scope로 설치하게 하고, 팀 공유 설정은 마련하지 않습니다.
  - EN: Let each member install whatever plugins they like at user scope, and do not provide shared team settings.
- B. JA: 有効化するプラグインをコミット済みの.claude/settings.jsonで全員に共有する。
  - KO: 활성화할 plugin을 commit된 .claude/settings.json으로 모두와 공유합니다.
  - EN: Share the plugins to enable with everyone through a committed .claude/settings.json.
- C. JA: プラグインのバージョンを固定し、更新は変更内容を確認したうえで意図的に適用する。
  - KO: plugin 버전을 고정하고, 업데이트는 변경 내용을 확인한 뒤 의도적으로 적용합니다.
  - EN: Pin plugin versions, and apply updates deliberately after reviewing what has changed.
- D. JA: マーケットプレイスの自動更新を有効にし、最新版のプラグインが全員に自動で届くようにする。
  - KO: marketplace 자동 업데이트를 켜서, 최신 버전 plugin이 모두에게 자동으로 전달되게 합니다.
  - EN: Enable marketplace auto-updates so that the latest plugin versions reach everyone automatically.
- E. JA: 導入前の審査は説明文と利用者数の確認にとどめ、追加されるフックやMCPサーバーの中身は見ない。
  - KO: 도입 전 심사는 설명문과 사용자 수 확인에 그치고, 추가되는 hook이나 MCP server의 내용은 보지 않습니다.
  - EN: Limit pre-adoption review to checking the description and the number of users, without examining the hooks or MCP servers the plugin adds.

## CCDV-F-Udemy-0032

**JA** ある大学の研究支援チームが、Claude Codeを導入し、構成要素の使い分けを整理しています。
各構成要素の説明として最も適切なものはどれですか。

**KO** 한 대학의 연구 지원팀이 Claude Code를 도입하고, 구성 요소를 어떻게 구분해 쓸지 정리하고 있습니다.
각 구성 요소의 설명으로 가장 적절한 것은 무엇입니까?

- A. JA: CLAUDE.mdは必要時に読み込まれる手順書で、スキルは毎セッション読み込まれる規約である。
  - KO: CLAUDE.md는 필요할 때 읽어 들이는 절차서이고, skill은 매 session 읽어 들이는 규약입니다.
  - EN: CLAUDE.md is a procedure guide loaded when needed, and skills are conventions loaded every session.
- B. JA: サブエージェントは親の会話履歴を引き継ぎ、親と同じコンテキストの中で作業を進める。
  - KO: subagent는 부모의 대화 이력을 이어받아, 부모와 같은 context 안에서 작업을 진행합니다.
  - EN: A subagent inherits the parent's conversation history and works within the same context as the parent.
- C. JA: Agent Memoryは人が書く規約ファイルで、Claudeが学びを自動で書き込むことはない。
  - KO: Agent Memory는 사람이 작성하는 규약 파일이며, Claude가 배운 내용을 자동으로 기록하는 일은 없습니다.
  - EN: Agent Memory is a convention file written by people; Claude never writes what it learns into it automatically.
- D. JA: CLAUDE.mdは毎セッション読み込まれる規約で、スキルは必要時に読み込まれる手順である。
  - KO: CLAUDE.md는 매 session 읽어 들이는 규약이고, skill은 필요할 때 읽어 들이는 절차입니다.
  - EN: CLAUDE.md contains conventions loaded every session, and skills are procedures loaded when needed.

## CCDV-F-Udemy-0033

**JA** ある電子機器メーカーが、次の2つのMCPサーバーを開発しています。
開発者のマシン上でサブプロセスとして動き、ローカルのファイルやCLIにアクセスするサーバー
ネットワーク越しに多数のクライアントへ提供するサーバー
MCPサーバーのトランスポートの選択として最も適切なものはどれですか。

**KO** 한 전자기기 제조사가 다음 두 MCP server를 개발하고 있습니다.
개발자 머신에서 하위 프로세스(subprocess)로 동작하며, 로컬 파일과 CLI에 접근하는 서버
네트워크를 통해 많은 클라이언트에 제공하는 서버
MCP server의 transport 선택으로 가장 적절한 것은 무엇입니까?

- A. JA: サブプロセスで動くローカル用はstdio、多数に提供するリモート用はStreamable HTTPにする。
  - KO: 하위 프로세스로 동작하는 로컬용은 stdio, 많은 클라이언트에 제공하는 원격용은 Streamable HTTP로 합니다.
  - EN: Use stdio for the local server that runs as a subprocess, and Streamable HTTP for the remote server offered to many clients.
- B. JA: ネットワーク提供用のサーバーも各利用者の端末にサブプロセスとして配布し、HTTPは使わない。
  - KO: 네트워크 제공용 서버도 각 사용자 단말에 하위 프로세스로 배포하고, HTTP는 쓰지 않습니다.
  - EN: Distribute the network-facing server to each user's machine as a subprocess as well, and do not use HTTP.
- C. JA: 両方をStreamable HTTPで実装し、開発者の端末で動くサーバーもローカルのHTTPポートで公開する。
  - KO: 둘 다 Streamable HTTP로 구현하고, 개발자 단말에서 동작하는 서버도 로컬 HTTP 포트로 공개합니다.
  - EN: Implement both with Streamable HTTP, exposing even the server that runs on the developer's machine on a local HTTP port.
- D. JA: ローカル用とネットワーク提供用の両方をstdioで実装し、リモートの利用者にも同じ方式で提供する。
  - KO: 로컬용과 네트워크 제공용 모두 stdio로 구현하고, 원격 사용자에게도 같은 방식으로 제공합니다.
  - EN: Implement both the local server and the network-facing server with stdio, and offer them to remote users the same way.

## CCDV-F-Udemy-0034

**JA** ある法律事務所では、数万トークンある契約書について、多数の異なる質問をClaudeに繰り返し送信します。契約書のテキストは毎回同じで、質問の前に置きます。
プロンプトキャッシングでコストを削減する設計として正しいものはどれですか。（2つ選択してください。）

**KO** 한 법률 사무소에서는 수만 토큰 분량의 계약서에 대해 서로 다른 질문을 많이 Claude에 반복해서 보냅니다. 계약서 텍스트는 매번 같으며, 질문 앞에 둡니다.
prompt caching으로 비용을 줄이는 설계로 옳은 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: キャッシュ書き込みは使わずに、同じ契約書への質問を1回のリクエストにまとめて送る。
  - KO: 캐시 쓰기는 사용하지 않고, 같은 계약서에 대한 질문을 요청 하나로 묶어서 보냅니다.
  - EN: Do not use cache writes; instead, bundle the questions about the same contract into a single request.
- B. JA: 毎回変わる受付日時を含むユーザーメッセージの末尾にcache_controlのブレークポイントを置く。
  - KO: 매번 바뀌는 접수 일시가 들어 있는 사용자 메시지 끝에 cache_control breakpoint를 둡니다.
  - EN: Place the cache_control breakpoint at the end of the user message that includes the request timestamp, which changes every time.
- C. JA: キャッシュ済みの契約書をコンテキストウィンドウの枠外として扱い、参考資料をさらに追加する。
  - KO: 캐시된 계약서는 context window 밖으로 취급하고, 참고 자료를 더 추가합니다.
  - EN: Treat the cached contract as outside the context window, and add even more reference material.
- D. JA: 契約書を先頭に置いてその末尾にcache_controlを付け、毎回変わる質問はその後ろに置く。
  - KO: 계약서를 맨 앞에 두고 그 끝에 cache_control을 붙이며, 매번 바뀌는 질문은 그 뒤에 둡니다.
  - EN: Place the contract at the beginning with cache_control at its end, and place the question, which changes every time, after it.
- E. JA: キャッシュ対象の接頭辞が、モデルごとの最小キャッシュ可能トークン数以上になるようにする。
  - KO: 캐시 대상 접두부(prefix)가 모델별 최소 캐시 가능 토큰 수 이상이 되도록 합니다.
  - EN: Ensure that the prefix to be cached is at least the model-specific minimum cacheable token count.

## CCDV-F-Udemy-0035

**JA** あるコンサルティング会社が、複数のワークロードに使うClaudeのモデル（Opus・Sonnet・Haiku）を選定しています。
品質・レイテンシ・コストのトレードオフに基づくモデル選定の考え方として、正しいものはどれですか。（2つ選択してください。）

**KO** 한 컨설팅 회사가 여러 워크로드에 쓸 Claude 모델(Opus·Sonnet·Haiku)을 선정하고 있습니다.
품질·latency·비용의 트레이드오프에 따른 모델 선정 방식으로 옳은 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 一度評価して選んだモデルは、後継のモデルが出ても再評価せずにそのまま使い続ける。
  - KO: 한 번 평가해서 고른 모델은 후속 모델이 나와도 재평가하지 않고 그대로 계속 씁니다.
  - EN: Once a model has been evaluated and selected, keep using it as is without re-evaluation, even when successor models are released.
- B. JA: 品質がコストより重要な複雑で自由度の高い分析には、単価が高くてもOpusを選ぶ。
  - KO: 품질이 비용보다 중요한 복잡하고 자유도가 높은 분석에는 단가가 높더라도 Opus를 고릅니다.
  - EN: For complex, open-ended analysis where quality matters more than cost, choose Opus even though its unit price is higher.
- C. JA: 複雑な分析にも最も安いHaikuを使い、推論の難しさはプロンプトの工夫で補う。
  - KO: 복잡한 분석에도 가장 저렴한 Haiku를 쓰고, 추론의 어려움은 prompt를 다듬어 보완합니다.
  - EN: Use the cheapest model, Haiku, even for complex analysis, and compensate for the difficulty of the reasoning through prompt engineering.
- D. JA: 大量で単純な分類やルーティングで速度とコストを優先するなら、Haikuを選ぶ。
  - KO: 대량의 단순한 분류나 routing에서 속도와 비용을 우선한다면 Haiku를 고릅니다.
  - EN: For high-volume, simple classification or routing where speed and cost take priority, choose Haiku.
- E. JA: 分類から分析までの全ワークロードで、使うモデルをOpusの1種類に統一しておく。
  - KO: 분류부터 분석까지 모든 워크로드에서 사용하는 모델을 Opus 하나로 통일합니다.
  - EN: Standardize on a single model, Opus, for all workloads, from classification to analysis.

## CCDV-F-Udemy-0036

**JA** ある食品メーカーは、自社のClaudeアプリで、回答の前に必ず原材料アレルゲン照合ツールを呼び出させたいと考えています。また、ツールの呼び出しが失敗することもあります。
tool_choiceの制御とツールエラーの扱いについて、最も適切な設計はどれですか。

**KO** 한 식품 제조사는 자사 Claude 앱이 답변하기 전에 반드시 원재료 알레르겐 대조 도구를 호출하게 하려고 합니다. 또한 도구 호출이 실패하는 경우도 있습니다.
tool_choice 제어와 도구 오류 처리에 대해 가장 적절한 설계는 무엇입니까?

- A. JA: tool_choiceはautoのままにし、失敗したときは同じツールをアプリ側で成功するまで何度も再実行する。
  - KO: tool_choice는 auto로 두고, 실패하면 같은 도구를 앱 측에서 성공할 때까지 여러 번 다시 실행합니다.
  - EN: Leave tool_choice as auto, and when a call fails, have the application re-run the same tool repeatedly until it succeeds.
- B. JA: 対応モデルではtool_choiceで指名し、失敗時はis_error付きのtool_resultを返す。
  - KO: 지원 모델에서는 tool_choice로 도구를 지정하고, 실패하면 is_error를 붙인 tool_result를 반환합니다.
  - EN: On supported models, name the tool with tool_choice, and on failure return a tool_result with is_error.
- C. JA: ツールが失敗したら空のtool_resultを返し、Claudeにはエラーがあったことを伝えない。
  - KO: 도구가 실패하면 빈 tool_result를 반환하고, Claude에게는 오류가 있었다는 사실을 알리지 않습니다.
  - EN: When the tool fails, return an empty tool_result and do not tell Claude that an error occurred.
- D. JA: ツールが失敗したら例外を送出して会話を終了し、tool_resultは返さずに処理を打ち切る。
  - KO: 도구가 실패하면 예외를 던져 대화를 끝내고, tool_result를 반환하지 않고 처리를 중단합니다.
  - EN: When the tool fails, raise an exception and end the conversation, aborting processing without returning a tool_result.

## CCDV-F-Udemy-0037

**JA** ある自治体が、住民からの問合せに回答する、Claudeを活用したシステムを本番リリースしました。
ITシステムのライフサイクル管理の観点から、リリース後の運用・保守フェーズの活動として最も適切なものはどれですか。

**KO** 한 지방자치단체가 주민 문의에 답변하는 Claude 기반 시스템을 운영 환경에 출시했습니다.
IT 시스템 수명 주기 관리 관점에서, 출시 후 운영·유지보수 단계의 활동으로 가장 적절한 것은 무엇입니까?

- A. JA: 応答品質と利用状況を監視し、モデル更新や制度改正の影響を評価して計画的に改修していく。
  - KO: 응답 품질과 이용 현황을 모니터링하고, 모델 업데이트나 제도 개정의 영향을 평가해 계획적으로 개선해 나갑니다.
  - EN: Monitor response quality and usage, evaluate the impact of model updates and policy changes, and make planned improvements.
- B. JA: 障害監視とサーバー再起動の手順を整備し、保守の作業を稼働率の維持に集中させる。
  - KO: 장애 감시와 서버 재시작 절차를 정비하고, 유지보수 작업을 가동률 유지에 집중합니다.
  - EN: Establish procedures for failure monitoring and server restarts, and focus maintenance work on maintaining uptime.
- C. JA: 住民が押した評価ボタンの結果をモデルの再学習に回し、回答品質を自動で改善させる。
  - KO: 주민이 누른 평가 버튼 결과를 모델 재학습에 활용해, 답변 품질을 자동으로 개선하게 합니다.
  - EN: Feed the results of the rating buttons that residents press into model retraining so that answer quality improves automatically.
- D. JA: 開発時のテストで品質を確定させ、次回のシステム更改までは回答内容の変更を凍結する。
  - KO: 개발 시 테스트로 품질을 확정하고, 다음 시스템 교체 때까지 답변 내용 변경을 동결합니다.
  - EN: Finalize quality through testing during development, and freeze changes to answer content until the next system replacement.

## CCDV-F-Udemy-0038

**JA** ある音楽ストリーミング企業の開発チームが、Claudeとの統合で、公式Python SDKを使うか、生のHTTPリクエストで直接呼ぶかを検討しています。
SDKとREST APIの関係について正しい記述はどれですか。

**KO** 한 음악 streaming 기업의 개발팀이 Claude 연동에서 공식 Python SDK를 쓸지, 원시 HTTP 요청으로 직접 호출할지 검토하고 있습니다.
SDK와 REST API의 관계에 대해 옳은 설명은 무엇입니까?

- A. JA: SDKは生のHTTPとは別の高速なエンドポイントに接続し、同じ呼び出しでも応答が速い。
  - KO: SDK는 원시 HTTP와는 다른 고속 엔드포인트에 연결되므로, 같은 호출이라도 응답이 빠릅니다.
  - EN: The SDK connects to a faster endpoint separate from the one used by raw HTTP, so the same call returns a response faster.
- B. JA: SDKを使うと、生のHTTPでは呼び出せないSDK専用のモデル機能を利用できる。
  - KO: SDK를 쓰면 원시 HTTP로는 호출할 수 없는 SDK 전용 모델 기능을 이용할 수 있습니다.
  - EN: Using the SDK gives access to SDK-only model features that cannot be called via raw HTTP.
- C. JA: SDKはserver-sent eventsを扱えず、ストリーミングを使う場合は生のHTTPで実装する。
  - KO: SDK는 server-sent events를 처리하지 못하므로, streaming을 쓰려면 원시 HTTP로 구현합니다.
  - EN: The SDK cannot handle server-sent events, so streaming must be implemented with raw HTTP.
- D. JA: SDKは生のHTTPと同じAPIを呼ぶクライアントで、型定義や再試行などの利便を加えるが機能は同じである。
  - KO: SDK는 원시 HTTP와 같은 API를 호출하는 클라이언트로, 타입 정의나 재시도 같은 편의를 더하지만 기능은 같습니다.
  - EN: The SDK is a client that calls the same API as raw HTTP; it adds conveniences such as type definitions and retries, but the functionality is the same.

## CCDV-F-Udemy-0039

**JA** ある在宅介護事業者が、スタッフのケア記録作成を支援するClaudeアシスタントを構築しています。記録には、氏名・住所・健康状態などの個人情報（PII）が含まれます。
PIIの漏えいを防ぐ設計として最も適切なものはどれですか。

**KO** 한 재가 돌봄 사업자가 직원의 돌봄 기록 작성을 돕는 Claude 어시스턴트를 구축하고 있습니다. 기록에는 이름·주소·건강 상태 같은 개인 식별 정보(PII)가 들어 있습니다.
PII 유출을 막는 설계로 가장 적절한 것은 무엇입니까?

- A. JA: タスクに必要な項目だけを渡し、直接識別子はマスキングし、ツールの権限を狭く絞る。
  - KO: 작업에 필요한 항목만 넘기고, 직접 식별자는 마스킹하며, 도구 권한을 좁게 제한합니다.
  - EN: Pass only the fields needed for the task, mask direct identifiers, and narrowly scope tool permissions.
- B. JA: 直接識別子をマスキングし権限も絞るが、全利用者の記録はシステムプロンプトに常時載せておく。
  - KO: 직접 식별자를 마스킹하고 권한도 제한하지만, 모든 이용자의 기록은 system prompt에 항상 올려 둡니다.
  - EN: Mask direct identifiers and narrowly scope permissions, but keep the records of all clients loaded in the system prompt at all times.
- C. JA: 監査に備えて、モデルに送ったプロンプトと応答を氏名入りのまま全文ログに保存する。
  - KO: 감사에 대비해, 모델에 보낸 prompt와 응답을 이름이 들어간 채로 전문 로그에 저장합니다.
  - EN: To prepare for audits, save the full text of the prompts and responses sent to the model in logs, with names left in.
- D. JA: 記録はTLSで送信し保存時も暗号化するため、プロンプトに渡す項目の最小化は行わない。
  - KO: 기록은 TLS로 전송하고 저장할 때도 암호화하므로, prompt에 넘기는 항목은 최소화하지 않습니다.
  - EN: Because records are sent over TLS and also encrypted at rest, do not minimize the fields passed to the prompt.

## CCDV-F-Udemy-0040

**JA** あるレストランチェーンが、モバイルアプリの注文チャットにClaudeを組み込みます。応答が長くなるときでも顧客を待たせないように、Messages APIのストリーミングの採用を検討しています。
ストリーミングの仕組みと利点の説明として正しいものはどれですか。

**KO** 한 레스토랑 체인이 모바일 앱의 주문 채팅에 Claude를 넣습니다. 응답이 길어질 때도 고객을 기다리게 하지 않으려고 Messages API의 streaming 도입을 검토하고 있습니다.
streaming의 구조와 이점에 대한 설명으로 옳은 것은 무엇입니까?

- A. JA: stream: trueでSSEの逐次配信を受け取り、届いた分から画面に表示していく。
  - KO: stream: true로 SSE 순차 전송을 받아, 도착한 부분부터 화면에 표시합니다.
  - EN: With stream: true, the app receives incremental SSE delivery and displays content on screen as it arrives.
- B. JA: 出力トークンの単価が標準の50%に下がり、長い応答ほど注文チャットの費用を抑えられる。
  - KO: 출력 토큰 단가가 표준의 50%로 내려가므로, 응답이 길수록 주문 채팅 비용을 줄일 수 있습니다.
  - EN: The unit price of output tokens drops to 50% of standard, so the longer the response, the more the ordering chat's costs are reduced.
- C. JA: 生成完了後に本文を1つのイベントにまとめて送り、クライアント側で表示を一括で更新する。
  - KO: 생성이 끝난 뒤 본문을 하나의 이벤트로 묶어 보내고, 클라이언트 측에서 표시를 한꺼번에 갱신합니다.
  - EN: After generation completes, the full text is bundled into a single event and sent, and the client updates the display all at once.
- D. JA: WebSocketで双方向接続を張り、生成の途中でも同じ接続で追加の注文を受け付ける。
  - KO: WebSocket으로 양방향 연결을 맺어, 생성 도중에도 같은 연결로 추가 주문을 받습니다.
  - EN: A bidirectional WebSocket connection is opened, and additional orders can be accepted over the same connection even mid-generation.

## CCDV-F-Udemy-0041

**JA** ある小売企業が、従業員向けの人事アシスタントを構築しています。Claudeは、社内MCPサーバーのget_employee_recordツールで人事DBを照会します。現在の構成は次のとおりです。
get_employee_recordツールは、全従業員の記録を読めるサービスアカウントで動いている
「本人の記録と、マネージャーなら部下の記録だけを扱う」という規則は、システムプロンプトに書いてあるだけ
テストでは、言い回しを工夫した質問で、他部署の従業員の評価を引き出せました。
最も適切な是正策はどれですか。

**KO** 한 소매 기업이 직원용 인사 어시스턴트를 구축하고 있습니다. Claude는 사내 MCP server의 get_employee_record 도구로 인사 DB를 조회합니다. 현재 구성은 다음과 같습니다.
get_employee_record 도구는 전 직원의 기록을 읽을 수 있는 서비스 계정으로 동작합니다
"본인의 기록과, 매니저라면 부하 직원의 기록만 다룬다"는 규칙은 system prompt에 적혀 있을 뿐입니다
테스트에서는 표현을 교묘하게 바꾼 질문으로 다른 부서 직원의 평가를 끌어낼 수 있었습니다.
가장 적절한 시정 방안은 무엇입니까?

- A. JA: システムプロンプトの規則を具体的な禁止例とともに書き直し、拒否すべき質問をフューショットプロンプティングで示す。
  - KO: system prompt의 규칙을 구체적인 금지 예시와 함께 다시 쓰고, 거부해야 할 질문을 few-shot prompting으로 보여 줍니다.
  - EN: Rewrite the rule in the system prompt with concrete examples of what is prohibited, and use few-shot prompting to show questions that should be refused.
- B. JA: ログイン中の従業員のトークンをツールの実行に付け、照会できる範囲をサーバーがその権限で判定する。
  - KO: 로그인한 직원의 토큰을 도구 실행에 붙이고, 조회할 수 있는 범위를 서버가 그 권한으로 판정합니다.
  - EN: Attach the logged-in employee's token to tool execution, and have the server determine the queryable scope based on that employee's permissions.
- C. JA: 送信前の応答を別のモデルで検査し、依頼者以外の氏名が含まれていれば回答を差し止めて作り直す。
  - KO: 보내기 전의 응답을 별도 모델로 검사하고, 요청자 외의 이름이 들어 있으면 답변을 막고 다시 만듭니다.
  - EN: Inspect responses with a separate model before sending them, and if a response contains names other than the requester's, block the answer and regenerate it.
- D. JA: 依頼者の従業員番号をClaudeにツールの引数として渡させ、サーバーはその番号の範囲だけを返す。
  - KO: 요청자의 직원 번호를 Claude가 도구 인자로 넘기게 하고, 서버는 그 번호의 범위만 반환합니다.
  - EN: Have Claude pass the requester's employee ID as a tool argument, and have the server return only records within that ID's scope.

## CCDV-F-Udemy-0042

**JA** ある物流倉庫事業者が、入庫伝票の自由記述メモから、SKU・数量・破損の有無を一定の書式で抽出するClaudeの機能を構築しています。抽出結果のフォーマットが実行ごとにばらつくので、これを解消したいと考えています。
フューショットプロンプティングと出力の制約の設計として、最も効果的なアプローチはどれですか。

**KO** 한 물류 창고 사업자가 입고 전표의 자유 형식 메모에서 SKU·수량·파손 여부를 일정한 서식으로 추출하는 Claude 기능을 구축하고 있습니다. 추출 결과의 형식이 실행할 때마다 들쭉날쭉해서 이를 해소하려고 합니다.
few-shot prompting과 출력 제약 설계로 가장 효과적인 접근 방식은 무엇입니까?

- A. JA: 実例に近い代表例を3〜5件exampleタグで示し、出力形式は肯定形で指定する。
  - KO: 실제 사례에 가까운 대표 예시 3~5건을 example 태그로 보여 주고, 출력 형식은 긍정형으로 지정합니다.
  - EN: Show 3–5 representative examples close to real cases in example tags, and specify the output format in positive terms.
- B. JA: 例示は使わずに、出力形式を詳しく説明した段落を指示の冒頭に加えて形式を伝える。
  - KO: 예시는 쓰지 않고, 출력 형식을 자세히 설명한 단락을 지시 첫머리에 추가해 형식을 전달합니다.
  - EN: Do not use examples; instead, convey the format by adding a paragraph that describes the output format in detail at the start of the instructions.
- C. JA: 「箇条書きにしない」「説明を添えない」といった禁止事項を並べて形式を伝える。
  - KO: "글머리 기호로 쓰지 말 것", "설명을 덧붙이지 말 것" 같은 금지 사항을 나열해 형식을 전달합니다.
  - EN: Convey the format by listing prohibitions such as "Do not use bullet points" and "Do not add explanations."
- D. JA: 手元にある伝票メモを選別せずに数十件そのまま並べ、できるだけ多くの例として示す。
  - KO: 가지고 있는 전표 메모를 선별하지 않고 수십 건 그대로 나열해, 최대한 많은 예시로 보여 줍니다.
  - EN: List dozens of slip notes on hand as is without curating them, presenting as many examples as possible.

## CCDV-F-Udemy-0043

**JA** ある不動産会社が、査定を支援するために、物件写真をClaudeで解析するアプリを開発しています。同じ物件写真を、複数ターンの会話や複数のリクエストで繰り返し参照します。そのため、リクエストのたびに画像を送り直して、リクエストのデータ量が膨らむことは避けたいと考えています。
Messages APIへの画像の入力方式として最も適切なものはどれですか。

**KO** 한 부동산 회사가 매물 감정을 돕기 위해 매물 사진을 Claude로 분석하는 앱을 개발하고 있습니다. 같은 매물 사진을 여러 turn의 대화와 여러 요청에서 반복해서 참조합니다. 그래서 요청할 때마다 이미지를 다시 보내 요청 데이터 양이 불어나는 일은 피하려고 합니다.
Messages API에 이미지를 입력하는 방식으로 가장 적절한 것은 무엇입니까?

- A. JA: Files APIに画像を一度アップロードし、返されたfile_idを各リクエストで参照する。
  - KO: Files API에 이미지를 한 번 업로드하고, 반환된 file_id를 각 요청에서 참조합니다.
  - EN: Upload the images once to the Files API, and reference the returned file_id in each request.
- B. JA: 画像のURLをテキストとしてプロンプトに書き、Claudeにリンク先を開いて写真を読ませる。
  - KO: 이미지 URL을 텍스트로 prompt에 적고, Claude가 링크를 열어 사진을 읽게 합니다.
  - EN: Write the image URLs as text in the prompt, and have Claude open the links and read the photos.
- C. JA: 画像をbase64でエンコードし、リクエストのたびにimageブロックへ埋め込んで送る。
  - KO: 이미지를 base64로 인코딩하고, 요청할 때마다 image 블록에 넣어 보냅니다.
  - EN: Encode the images in base64 and embed them in an image block with every request.
- D. JA: 画像のimageブロックにcache_controlを付け、プロンプトキャッシングでキャッシュして再利用する。
  - KO: 이미지의 image 블록에 cache_control을 붙이고, prompt caching으로 캐시해 재사용합니다.
  - EN: Add cache_control to the images' image blocks, and cache and reuse them with prompt caching.

## CCDV-F-Udemy-0044

**JA** ある航空会社が、整備記録の自由記述から、所定のフィールド（機体番号・整備区分・所要時間など）を構造化レコードに抽出するClaudeの機能を構築しています。
モデルがスキーマに準拠した構造化データを確実に返すようにする設計として、適切なものはどれですか。（2つ選択してください。）

**KO** 한 항공사가 정비 기록의 자유 서술 텍스트에서 정해진 필드(기체 번호·정비 구분·소요 시간 등)를 추출해 구조화된 레코드로 만드는 Claude 기능을 구축하고 있습니다.
모델이 schema를 준수하는 구조화 데이터를 확실하게 반환하게 하는 설계로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 結果を使う前に、stop_reasonが拒否（refusal）や上限到達（max_tokens）でないか確かめる。
  - KO: 결과를 사용하기 전에 stop_reason이 거부(refusal)나 상한 도달(max_tokens)이 아닌지 확인합니다.
  - EN: Before using the result, confirm that stop_reason does not indicate a refusal (refusal) or reaching the limit (max_tokens).
- B. JA: 自由文の応答から正規表現で各フィールドを抜き出し、見つからない項目は空欄のまま登録する。
  - KO: 자유 텍스트 응답에서 정규 표현식으로 각 필드를 추출하고, 찾지 못한 항목은 빈칸으로 둔 채 등록합니다.
  - EN: Extract each field from the free-text response with regular expressions, and register any fields that are not found as blank.
- C. JA: max_tokensを小さく設定して出力を短く保ち、スキーマから外れた部分が出ないようにする。
  - KO: max_tokens를 작게 설정해 출력을 짧게 유지함으로써 schema를 벗어난 부분이 나오지 않게 합니다.
  - EN: Set max_tokens low to keep the output short, so that no parts that deviate from the schema appear.
- D. JA: 構造化出力を使えば応答は常にスキーマ準拠が保証されるとみなし、stop_reasonの確認は省略する。
  - KO: structured outputs를 쓰면 응답이 항상 schema를 준수하도록 보장된다고 보고, stop_reason 확인은 생략합니다.
  - EN: Assume that using structured outputs always guarantees a schema-compliant response, and skip checking stop_reason.
- E. JA: output_config.formatのJSONスキーマかstrict tool useで、応答をスキーマに制約する。
  - KO: output_config.format의 JSON schema나 strict tool use로 응답을 schema에 맞게 제약합니다.
  - EN: Constrain the response to the schema with a JSON schema in output_config.format or with strict tool use.

## CCDV-F-Udemy-0045

**JA** あるホテル予約アシスタントには、空室確認・予約確定・予約キャンセルなど、複数のツールが登録されています。Claudeが、状況に合わないツールを呼び出してしまうことがあります。
ツールの説明の書き方とツール選択の精度の関係を踏まえた設計として、最も適切なものはどれですか。

**KO** 한 호텔 예약 어시스턴트에는 빈방 확인·예약 확정·예약 취소 등 여러 도구가 등록되어 있습니다. Claude가 상황에 맞지 않는 도구를 호출하는 경우가 있습니다.
도구 설명을 쓰는 방식과 도구 선택 정확도의 관계를 고려할 때 가장 적절한 설계는 무엇입니까?

- A. JA: descriptionは開発者向けのメモとして短くし、選択の精度はツール名の工夫で補っていく。
  - KO: description은 개발자용 메모로 짧게 쓰고, 선택 정확도는 도구 이름을 잘 지어 보완해 나갑니다.
  - EN: Keep the description short, as a memo for developers, and compensate for selection accuracy by choosing tool names carefully.
- B. JA: どのツールにも同じ汎用的な説明を付け、使い分けはモデルの柔軟な判断に任せておく。
  - KO: 모든 도구에 똑같은 범용 설명을 붙이고, 어떤 도구를 쓸지는 모델의 유연한 판단에 맡겨 둡니다.
  - EN: Give every tool the same generic description, and leave the choice among them to the model's flexible judgment.
- C. JA: 各ツールの用途と使う場面を具体的に書き分け、ツール間の役割の重なりをなくす。
  - KO: 각 도구의 용도와 사용할 상황을 구체적으로 구분해 쓰고, 도구 간 역할이 겹치지 않게 합니다.
  - EN: Write a distinct, specific description of each tool's purpose and when to use it, eliminating overlap in roles between tools.
- D. JA: 誤ったツールが呼ばれたら例外を返し、Claudeに再試行させて正しいツールを選び直させる。
  - KO: 잘못된 도구가 호출되면 예외를 반환하고, Claude가 재시도해 올바른 도구를 다시 고르게 합니다.
  - EN: When the wrong tool is called, return an exception and have Claude retry and reselect the correct tool.

## CCDV-F-Udemy-0046

**JA** ある病院が、診察の音声の書き起こしから診療サマリを自動生成する、Claudeを活用したシステムを企画しています。ビジネス目標は「医師が書類作成に費やす時間を30%削減する」ことです。
このビジネス要件から導かれる「機能要件」として最も適切なものはどれですか。

**KO** 한 병원이 진료 음성을 받아 적은 텍스트에서 진료 요약을 자동 생성하는 Claude 기반 시스템을 기획하고 있습니다. 비즈니스 목표는 "의사가 서류 작성에 쓰는 시간을 30% 줄이는 것"입니다.
이 비즈니스 요구 사항에서 도출되는 "기능 요구 사항"으로 가장 적절한 것은 무엇입니까?

- A. JA: 書き起こしテキストから病院指定の書式で診療サマリを生成し、医師の確認画面に表示すること。
  - KO: 받아 적은 텍스트로 병원이 지정한 서식의 진료 요약을 생성해 의사의 확인 화면에 표시할 것.
  - EN: Generate a clinical summary in the hospital's specified format from the transcript text, and display it on the physician's review screen.
- B. JA: ピーク時に100件の同時リクエストを処理し、応答時間の95パーセンタイルを10秒以内に収めること。
  - KO: 피크 시간에 동시 요청 100건을 처리하고, 응답 시간의 95번째 백분위수를 10초 이내로 유지할 것.
  - EN: Handle 100 concurrent requests at peak, keeping the 95th percentile response time within 10 seconds.
- C. JA: 医師が書類作成に費やす時間を導入前と比べて30%削減し、診療に充てる時間を増やすこと。
  - KO: 의사가 서류 작성에 쓰는 시간을 도입 전보다 30% 줄이고, 진료에 쓰는 시간을 늘릴 것.
  - EN: Reduce the time physicians spend on paperwork by 30% compared with before adoption, increasing the time available for patient care.
- D. JA: 開発を3か月以内に完了し、初年度の構築・運用費用を承認済みの予算内に収めること。
  - KO: 개발을 3개월 이내에 끝내고, 첫해 구축·운영 비용을 승인된 예산 안으로 유지할 것.
  - EN: Complete development within three months, and keep first-year build and operating costs within the approved budget.

## CCDV-F-Udemy-0047

**JA** ある官公庁のポータルが、ほとんど変わらない規制文書のコーパスをもとに、市民からの数千件の問合せに回答しています。どのリクエストでも、先頭に置くシステムプロンプトと規制文書（大量のテキスト）は同じで、変わるのは市民の問合せだけです。
プロンプトキャッシングのコスト設計として正しい記述はどれですか。

**KO** 한 관공서 포털이 거의 바뀌지 않는 규제 문서 코퍼스를 바탕으로 시민의 문의 수천 건에 답하고 있습니다. 모든 요청에서 앞부분에 두는 system prompt와 규제 문서(대량의 텍스트)는 같고, 바뀌는 것은 시민의 문의뿐입니다.
prompt caching의 비용 설계로 옳은 설명은 무엇입니까?

- A. JA: 読み出しは多くのモデルで基本入力の0.1倍、5分TTLの書き込みは1.25倍で、再利用が多いほど安い。
  - KO: 읽기는 많은 모델에서 기본 입력 단가의 0.1배, 5분 TTL 쓰기는 1.25배이므로 재사용이 많을수록 저렴합니다.
  - EN: On many models, cache reads cost 0.1x the base input price and 5-minute TTL writes cost 1.25x, so the more reuse, the cheaper it becomes.
- B. JA: キャッシュは同じ利用者の会話の中でだけ再利用され、市民ごとに別々の書き込みが必要になる。
  - KO: 캐시는 같은 이용자의 대화 안에서만 재사용되므로 시민마다 따로 쓰기가 필요합니다.
  - EN: The cache is reused only within the same user's conversation, so a separate write is needed for each citizen.
- C. JA: 1時間TTLの書き込みは5分TTLの書き込みより安く、再利用の間隔によらず1時間TTLが有利になる。
  - KO: 1시간 TTL 쓰기는 5분 TTL 쓰기보다 저렴하므로 재사용 간격과 관계없이 1시간 TTL이 유리합니다.
  - EN: 1-hour TTL writes are cheaper than 5-minute TTL writes, so the 1-hour TTL is advantageous regardless of the reuse interval.
- D. JA: 5分TTLのキャッシュは5分ごとに書き込み直しが課金され、問い合わせが絶えなくても1時間TTLが有利になる。
  - KO: 5분 TTL 캐시는 5분마다 다시 쓰기 요금이 부과되므로, 문의가 끊이지 않아도 1시간 TTL이 유리합니다.
  - EN: A 5-minute TTL cache is billed for a rewrite every 5 minutes, so the 1-hour TTL is advantageous even when inquiries arrive continuously.

## CCDV-F-Udemy-0048

**JA** ある広告代理店が、蓄積した数万件の広告コピーの表現を毎晩分析する社内システムを設計しています。分析結果は翌朝の定例会議までにそろっていればよく、処理コストの削減を最優先にしています。
この用途でMessage Batches APIを選ぶ根拠として正しいものはどれですか。

**KO** 한 광고 대행사가 축적된 광고 카피 수만 건의 표현을 매일 밤 분석하는 사내 시스템을 설계하고 있습니다. 분석 결과는 다음 날 아침 정례 회의 전까지만 준비되면 되고, 처리 비용 절감을 최우선으로 삼고 있습니다.
이 용도에 Message Batches API를 선택하는 근거로 옳은 것은 무엇입니까?

- A. JA: 結果がserver-sent eventsで逐次届き、分析の進捗を画面に表示し続けられる。
  - KO: 결과가 server-sent events로 순차 도착하므로 분석 진행 상황을 화면에 계속 표시할 수 있습니다.
  - EN: Results arrive incrementally via server-sent events, so the progress of the analysis can be displayed on screen continuously.
- B. JA: 標準料金の50%で非同期に処理され、多くは1時間以内、最長24時間の枠で完了する。
  - KO: 표준 요금의 50%로 비동기 처리되며, 대부분 1시간 이내, 최대 24시간 안에 완료됩니다.
  - EN: Requests are processed asynchronously at 50% of standard pricing, with most completing within 1 hour and a maximum window of 24 hours.
- C. JA: 各リクエストの応答が標準のAPIより速く返り、夜間の分析時間を短縮できる。
  - KO: 각 요청의 응답이 표준 API보다 빨리 돌아오므로 야간 분석 시간을 줄일 수 있습니다.
  - EN: Each request's response returns faster than with the standard API, shortening the overnight analysis time.
- D. JA: 投入した順序どおりに結果が返り、custom_idなしで元の広告コピーと突き合わせられる。
  - KO: 제출한 순서대로 결과가 반환되므로 custom_id 없이도 원래 광고 카피와 대조할 수 있습니다.
  - EN: Results are returned in the same order as submitted, so they can be matched to the original ad copy without custom_id.

## CCDV-F-Udemy-0049

**JA** ある化学メーカーが、Claudeアシスタントを構築しています。このアシスタントは、利用者から送られてくる問い合わせ文をプロンプトのテンプレートに差し込んで回答します。
プロンプトを組み立てるときの、信頼できないユーザー入力の扱い（サニタイズ）として最も適切なアプローチはどれですか。

**KO** 한 화학 제조사가 Claude 어시스턴트를 구축하고 있습니다. 이 어시스턴트는 이용자가 보낸 문의 내용을 prompt 템플릿에 삽입해 답변합니다.
prompt를 구성할 때 신뢰할 수 없는 사용자 입력을 다루는 방법(sanitization)으로 가장 적절한 접근 방식은 무엇입니까?

- A. JA: 入力をuser_queryなどのXMLタグで囲み、中身はデータだとシステムプロンプトに書く。
  - KO: 입력을 user_query 같은 XML 태그로 감싸고, 그 내용은 데이터라고 system prompt에 적습니다.
  - EN: Wrap the input in an XML tag such as user_query, and state in the system prompt that its contents are data.
- B. JA: 入力から記号類を取り除いて文字だけにし、その結果をテンプレートにそのまま差し込んで使う。
  - KO: 입력에서 기호류를 제거해 문자만 남기고, 그 결과를 템플릿에 그대로 삽입해 사용합니다.
  - EN: Strip symbols from the input so that only text characters remain, and insert the result into the template as is.
- C. JA: 入力を指示文の途中にそのまま連結し、指示と入力の区別はモデルの文脈判断に任せておく。
  - KO: 입력을 지시문 중간에 그대로 연결하고, 지시와 입력의 구분은 모델의 문맥 판단에 맡겨 둡니다.
  - EN: Concatenate the input as is into the middle of the instructions, and leave it to the model's contextual judgment to distinguish instructions from input.
- D. JA: 差し込む前に別のモデルで入力を要約させ、言い換えた文のほうをテンプレートに差し込む。
  - KO: 삽입하기 전에 다른 모델이 입력을 요약하게 하고, 바꿔 쓴 문장 쪽을 템플릿에 삽입합니다.
  - EN: Before inserting the input, have a separate model summarize it, and insert the paraphrased text into the template instead.

## CCDV-F-Udemy-0050

**JA** ある証券会社が、顧客向けのClaudeチャットボットを本番導入します。インサイダー取引の助長や顧客情報の開示といった不適切な要求に対して、堅牢なガードレールを設けたいと考えています。
最も適切な設計はどれですか。

**KO** 한 증권사가 고객용 Claude 챗봇을 프로덕션에 도입합니다. 내부자 거래 조장이나 고객 정보 공개 같은 부적절한 요청에 대비해 견고한 guardrail을 마련하려고 합니다.
가장 적절한 설계는 무엇입니까?

- A. JA: システムプロンプトの拒否方針と出力フィルタを置き、入力の事前審査は省いて処理を軽くする。
  - KO: system prompt의 거부 방침과 출력 필터를 두고, 입력 사전 심사는 생략해 처리를 가볍게 합니다.
  - EN: Use a refusal policy in the system prompt and an output filter, and skip pre-screening of input to keep processing light.
- B. JA: 入力を軽量モデルで審査する仕組みを設け、審査を通過した依頼はそのまま処理する。
  - KO: 경량 모델로 입력을 심사하는 구조를 두고, 심사를 통과한 요청은 그대로 처리합니다.
  - EN: Set up a mechanism that screens input with a lightweight model, and process requests that pass screening as is.
- C. JA: リリース前にレッドチーミングで攻撃を試して対策を固め、稼働後の追加の検査は置かない。
  - KO: 출시 전에 red teaming으로 공격을 시도해 대책을 다지고, 가동 후에는 추가 검사를 두지 않습니다.
  - EN: Try attacks through red teaming before release to harden the defenses, and add no further checks after going live.
- D. JA: 入力の審査とシステムプロンプトの拒否方針に、出力のフィルタと監視を重ねて多層で守る。
  - KO: 입력 심사와 system prompt의 거부 방침에 출력 필터링과 모니터링을 겹쳐 다층으로 방어합니다.
  - EN: Layer output filtering and monitoring on top of input screening and a refusal policy in the system prompt, for defense in depth.

## CCDV-F-Udemy-0051

**JA** ある銀行が、顧客データを扱う社内エージェントを構築します。規制対応のため、次の要件を満たす必要があります。
エージェントの実行環境とセッション状態（会話ログ）を、自社で管理するインフラ内に置く
エージェントが、自社ネットワーク内のファイルとサービスを直接操作する
この要件に最も適したデプロイモデルはどれですか。

**KO** 한 은행이 고객 데이터를 다루는 사내 agent를 구축합니다. 규제 대응을 위해 다음 요구 사항을 충족해야 합니다.
agent의 실행 환경과 session 상태(대화 로그)를 자사가 관리하는 인프라 안에 둘 것
agent가 자사 네트워크 안의 파일과 서비스를 직접 조작할 것
이 요구 사항에 가장 적합한 배포 모델은 무엇입니까?

- A. JA: Managed Agentsを採用し、自社インフラ上のセルフホスト型サンドボックスでツールを実行する。
  - KO: Managed Agents를 채택하고, 자사 인프라의 self-hosted sandbox에서 도구를 실행합니다.
  - EN: Adopt Managed Agents, and run tools in a self-hosted sandbox on the bank's own infrastructure.
- B. JA: Message Batches APIを採用し、エージェントの各ステップを非同期のバッチとして投入する。
  - KO: Message Batches API를 채택하고, agent의 각 단계를 비동기 batch로 제출합니다.
  - EN: Adopt the Message Batches API, and submit each step of the agent as an asynchronous batch.
- C. JA: Claude Agent SDKを採用し、自社インフラ上の自社プロセスでエージェントループを実行する。
  - KO: Claude Agent SDK를 채택하고, 자사 인프라의 자사 프로세스에서 agent loop를 실행합니다.
  - EN: Adopt the Claude Agent SDK, and run the agent loop in the bank's own process on its own infrastructure.
- D. JA: Managed Agentsを採用し、Anthropic管理のクラウドサンドボックスでセッションを実行する。
  - KO: Managed Agents를 채택하고, Anthropic이 관리하는 클라우드 sandbox에서 session을 실행합니다.
  - EN: Adopt Managed Agents, and run sessions in an Anthropic-managed cloud sandbox.

## CCDV-F-Udemy-0052

**JA** ある再生可能エネルギー事業者が、運用リポジトリでシェルコマンドを実行できるClaude Codeエージェントを使っています。本番設定の削除などの破壊的なコマンドを、実行される前に、モデルの判断に頼らず決定論的に（確実に）ブロックしたいと考えています。
最も適切なアプローチはどれですか。

**KO** 한 재생에너지 사업자가 운영 저장소에서 셸 명령을 실행할 수 있는 Claude Code agent를 사용하고 있습니다. 프로덕션 설정 삭제 같은 파괴적인 명령을 실행되기 전에, 모델의 판단에 의존하지 않고 결정론적으로(확실하게) 차단하려고 합니다.
가장 적절한 접근 방식은 무엇입니까?

- A. JA: システムプロンプトに「本番設定を削除するコマンドは実行しない」と明記しておく。
  - KO: system prompt에 "프로덕션 설정을 삭제하는 명령은 실행하지 않는다"라고 명시해 둡니다.
  - EN: State explicitly in the system prompt: "Do not run commands that delete production configuration."
- B. JA: 実行前に審査役のサブエージェントを呼ぶよう指示し、破壊的なコマンドかどうかを判断させる。
  - KO: 실행 전에 심사 역할의 subagent를 호출하도록 지시하고, 파괴적인 명령인지 판단하게 합니다.
  - EN: Instruct the agent to call a reviewer subagent before execution, and have the subagent judge whether a command is destructive.
- C. JA: PostToolUseフックでBashの実行結果を検査し、破壊的な操作を検知したら担当者に通知する。
  - KO: PostToolUse hook으로 Bash 실행 결과를 검사하고, 파괴적인 작업을 감지하면 담당자에게 알립니다.
  - EN: Inspect Bash execution results with a PostToolUse hook, and notify the person in charge if a destructive operation is detected.
- D. JA: PreToolUseフックで実行前にコマンドを検査し、該当すればdenyを返して止める。
  - KO: PreToolUse hook으로 실행 전에 명령을 검사하고, 해당하면 deny를 반환해 막습니다.
  - EN: Inspect commands before execution with a PreToolUse hook, and stop them by returning deny if they match.

## CCDV-F-Udemy-0053

**JA** ある保険会社が、保険金請求の一次処理を自動化しようとしています。処理は毎回、次の3ステップをこの順序で実行し、順序が変わることはありません。
提出書類の必須項目チェック
契約条件との照合
顧客向け受領通知文の生成
LLMを活用した実装方針として最も適切なものはどれですか。

**KO** 한 보험사가 보험금 청구의 1차 처리를 자동화하려고 합니다. 처리는 매번 다음 3단계를 이 순서대로 실행하며, 순서가 바뀌는 일은 없습니다.
제출 서류의 필수 항목 점검
계약 조건과의 대조
고객용 접수 통지문 생성
LLM을 활용한 구현 방침으로 가장 적절한 것은 무엇입니까?

- A. JA: マネージャー役のLLMが請求ごとにサブタスクを決め、ワーカーLLMへ委任するorchestrator-workers型で実装する。
  - KO: 관리자 역할의 LLM이 청구마다 하위 작업을 정하고 worker LLM에 위임하는 orchestrator-workers 방식으로 구현합니다.
  - EN: Implement it with the orchestrator-workers pattern, in which a manager LLM decides the subtasks for each claim and delegates them to worker LLMs.
- B. JA: 評価役のLLMが出力を採点し、基準を満たすまで生成と修正を繰り返すevaluator-optimizer型で実装する。
  - KO: 평가 역할의 LLM이 출력을 채점하고, 기준을 충족할 때까지 생성과 수정을 반복하는 evaluator-optimizer 방식으로 구현합니다.
  - EN: Implement it with the evaluator-optimizer pattern, in which an evaluator LLM scores the output and generation and revision repeat until the criteria are met.
- C. JA: 各処理を事前定義したコードパスで順に呼び出すprompt chaining型のワークフローで実装する。
  - KO: 각 처리를 미리 정의한 코드 경로로 차례로 호출하는 prompt chaining 방식의 workflow로 구현합니다.
  - EN: Implement it as a prompt chaining workflow that calls each step in order through predefined code paths.
- D. JA: LLMが実行時にツールの使用順序と処理手順を自ら決める自律型エージェントとして実装する。
  - KO: LLM이 실행 시점에 도구 사용 순서와 처리 절차를 스스로 정하는 자율형 agent로 구현합니다.
  - EN: Implement it as an autonomous agent in which the LLM itself decides at runtime the order of tool use and the processing steps.

## CCDV-F-Udemy2-0001

**JA** ある病院のIT部門が、院内の臨床リファレンス用MCPサーバーを、AIアプリ（ホスト）に統合しようとしています。あるエンジニアは、ホスト・クライアント・サーバーの関係と、サーバーが2つあるときに必要なクライアントの数を混同しています。
MCPのホスト/クライアント/サーバーモデルを正しく説明しているものはどれですか。

**KO** 한 병원의 IT 부서가 원내 임상 레퍼런스용 MCP server를 AI 앱(host)에 통합하려고 합니다. 한 엔지니어는 host·client·server의 관계와, server가 2개일 때 필요한 client 수를 혼동하고 있습니다.
MCP의 host/client/server 모델을 올바르게 설명한 것은 무엇입니까?

- A. JA: ホストがサーバーごとにMCPクライアントを1つずつ作り、各クライアントが専用の接続を保つ。
  - KO: host가 server마다 MCP client를 하나씩 만들고, 각 client가 전용 연결을 유지합니다.
  - EN: The host creates one MCP client per server, and each client maintains a dedicated connection.
- B. JA: MCPサーバーがホストの役割を兼ね、AIアプリはクライアントとしてサーバーに接続する。
  - KO: MCP server가 host 역할을 겸하고, AI 앱은 client로서 server에 연결합니다.
  - EN: The MCP server also acts as the host, and the AI application connects to the server as a client.
- C. JA: ホストが1つのMCPクライアントを作り、そのクライアントが2つのサーバーへ同時に接続する。
  - KO: host가 MCP client 하나를 만들고, 그 client가 두 server에 동시에 연결합니다.
  - EN: The host creates a single MCP client, and that client connects to both servers simultaneously.
- D. JA: stdio用とStreamable HTTP用に、トランスポートごとのクライアントを作ってサーバーを振り分ける。
  - KO: stdio용과 Streamable HTTP용으로 transport별 client를 만들어 server를 나눠 맡깁니다.
  - EN: Separate clients are created per transport, one for stdio and one for Streamable HTTP, and the servers are distributed among them.

## CCDV-F-Udemy2-0002

**JA** ある動画配信サービスが、視聴しながら使うチャットアシスタントで、Messages APIのストリーミング（server-sent events）を直接扱う実装をしています。
SSEイベントを正しく処理する実装として、適切なものはどれですか。（2つ選択してください。）

**KO** 한 동영상 streaming 서비스가 시청 중에 쓰는 채팅 어시스턴트에서 Messages API의 streaming(server-sent events)을 직접 다루도록 구현하고 있습니다.
SSE 이벤트를 올바르게 처리하는 구현으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 最後に届いたcontent_block_deltaのテキストを完成済みの本文とみなし、そのまま画面に表示する。
  - KO: 마지막으로 도착한 content_block_delta의 텍스트를 완성된 본문으로 보고 그대로 화면에 표시합니다.
  - EN: Treat the text of the last content_block_delta received as the completed body, and display it on screen as is.
- B. JA: input_json_deltaのpartial_jsonを受信のたびにJSONとしてパースし、得られた値を引数に反映する。
  - KO: input_json_delta의 partial_json을 받을 때마다 JSON으로 파싱하고, 얻은 값을 인수에 반영합니다.
  - EN: Parse the partial_json of input_json_delta as JSON every time one is received, and apply the resulting value to the arguments.
- C. JA: 未知のイベントタイプを受信したら仕様違反として扱い、例外を送出して接続を切断する。
  - KO: 알 수 없는 이벤트 유형을 받으면 사양 위반으로 처리해 예외를 던지고 연결을 끊습니다.
  - EN: Treat receipt of an unknown event type as a specification violation, throw an exception, and close the connection.
- D. JA: text_deltaをindexごとに順に連結し、stop_reasonはmessage_deltaイベントから読み取る。
  - KO: text_delta를 index별로 순서대로 이어 붙이고, stop_reason은 message_delta 이벤트에서 읽습니다.
  - EN: Concatenate text_delta values in order for each index, and read stop_reason from the message_delta event.
- E. JA: input_json_deltaのpartial_jsonを蓄積し、content_block_stopを受け取ってからパースする。
  - KO: input_json_delta의 partial_json을 누적해 두고, content_block_stop을 받은 뒤에 파싱합니다.
  - EN: Accumulate the partial_json of input_json_delta, and parse it only after receiving content_block_stop.

## CCDV-F-Udemy2-0003

**JA** ある旅行ガイドアプリの開発チームは、以前のモデルで観光地の紹介文を生成する際、確率の低いトークンが選ばれにくくなるよう、top_kを指定して調整していました。
モデルをClaude Sonnet 5に更新したところ、このリクエストがHTTP 400で失敗するようになりました。
サンプリングパラメータの理解と対処として最も適切なものはどれですか。

**KO** 한 여행 가이드 앱의 개발팀은 이전 모델로 관광지 소개문을 생성할 때, 확률이 낮은 token이 덜 선택되도록 top_k를 지정해 조정했습니다.
모델을 Claude Sonnet 5로 업데이트하자 이 요청이 HTTP 400으로 실패하게 되었습니다.
sampling 파라미터에 대한 이해와 대처로 가장 적절한 것은 무엇입니까?

- A. JA: top_kを外し、文体はプロンプトの指示や例で導く。
  - KO: top_k를 제거하고, 문체는 prompt의 지시나 예시로 유도합니다.
  - EN: Remove top_k, and guide the writing style through instructions and examples in the prompt.
- B. JA: top_kは残したまま、top_pを0.99以上に設定し、既定値に近い組み合わせとして受け付けさせる。
  - KO: top_k는 그대로 두고 top_p를 0.99 이상으로 설정해, 기본값에 가까운 조합으로 받아들여지게 합니다.
  - EN: Keep top_k, and set top_p to 0.99 or higher so that the request is accepted as a combination close to the defaults.
- C. JA: top_kを外し、代わりにtemperatureを0に下げて、確率の低い候補が選ばれにくくなるようにする。
  - KO: top_k를 제거하고, 대신 temperature를 0으로 낮춰 확률이 낮은 후보가 덜 선택되게 합니다.
  - EN: Remove top_k, and instead lower temperature to 0 so that low-probability candidates are less likely to be chosen.
- D. JA: top_kを外し、代わりにmax_tokensを小さくして、次のトークンの候補となる数を絞り込む。
  - KO: top_k를 제거하고, 대신 max_tokens를 줄여 다음 token 후보의 수를 좁힙니다.
  - EN: Remove top_k, and instead reduce max_tokens to narrow the number of candidates for the next token.

## CCDV-F-Udemy2-0004

**JA** あるホテルチェーンが、数か月前にClaudeを使ったコンシェルジュアプリを本番導入しました。
システムライフサイクルの運用・保守フェーズで行う、継続的な保守・評価の取り組みとして最も適切なものはどれですか。

**KO** 한 호텔 체인이 몇 달 전에 Claude를 활용한 컨시어지 앱을 프로덕션에 도입했습니다.
시스템 라이프사이클의 운영·유지보수 단계에서 수행하는 지속적인 유지보수·평가 활동으로 가장 적절한 것은 무엇입니까?

- A. JA: 障害の報告を受けたときに個別に原因を調べて直し、評価用のデータセットは持たずに運用する。
  - KO: 장애 보고를 받을 때마다 개별적으로 원인을 조사해 고치고, 평가용 데이터셋 없이 운영합니다.
  - EN: Investigate and fix the cause case by case whenever a failure is reported, and operate without an evaluation dataset.
- B. JA: 利用者満足度のアンケートを四半期ごとに集計し、スコアが下がったときに構成を見直す。
  - KO: 이용자 만족도 설문을 분기마다 집계하고, 점수가 떨어지면 구성을 재검토합니다.
  - EN: Tally user satisfaction surveys every quarter, and review the configuration when the score drops.
- C. JA: 本番出力の品質を継続的に監視し、回帰評価セットを保ちながらプロンプトや構成を改善する。
  - KO: 프로덕션 출력의 품질을 지속적으로 모니터링하고, 회귀 평가 세트를 유지하면서 prompt와 구성을 개선합니다.
  - EN: Continuously monitor the quality of production outputs, and improve the prompts and configuration while maintaining a regression evaluation set.
- D. JA: 導入時の構成を固定し、モデルやプロンプトは次の大規模改修まで変更しない方針で運用する。
  - KO: 도입 시점의 구성을 고정하고, 모델과 prompt는 다음 대규모 개편 때까지 바꾸지 않는 방침으로 운영합니다.
  - EN: Freeze the configuration from launch, and operate under a policy of not changing the model or prompts until the next major overhaul.

## CCDV-F-Udemy2-0005

**JA** あるフィンテック（決済）企業の不正検知エージェントが、長い会話の後半で、初期の指示や口座の制約を無視し始めました。無関係なツール出力に引きずられて、判断もぶれ始めています。
コンテキストドリフト（コンテキストの逸脱）の症状と防止策として最も適切なものはどれですか。

**KO** 한 핀테크(결제) 기업의 부정 거래 탐지 agent가 긴 대화의 후반부에서 초기 지시와 계좌 제약을 무시하기 시작했습니다. 관련 없는 도구 출력에 끌려가 판단도 흔들리기 시작했습니다.
context drift(context 이탈)의 증상과 방지책으로 가장 적절한 것은 무엇입니까?

- A. JA: モデルの一時的な不調とみて、同じ会話のまま時間をおいて処理を再開し、回復するのを待つ。
  - KO: 모델의 일시적인 컨디션 저하로 보고, 같은 대화를 유지한 채 시간을 두었다가 처리를 재개해 회복을 기다립니다.
  - EN: Treat it as a temporary model malfunction, wait a while, and resume processing in the same conversation until the model recovers.
- B. JA: 肥大化した文脈で初期の指示が埋もれた状態とみて、不要なツール結果を削り要約や分離で絞る。
  - KO: 비대해진 context에 초기 지시가 묻힌 상태로 보고, 불필요한 도구 결과를 덜어 내고 요약이나 분리로 context를 줄입니다.
  - EN: Treat it as the initial instructions being buried in a bloated context, and trim unnecessary tool results and narrow the context through summarization or separation.
- C. JA: 初期の指示が足りない状態とみて、同じ指示をシステムプロンプトに何度も書き足して強調する。
  - KO: 초기 지시가 부족한 상태로 보고, 같은 지시를 system prompt에 여러 번 덧붙여 강조합니다.
  - EN: Treat it as a shortage of initial instructions, and emphasize them by appending the same instructions to the system prompt repeatedly.
- D. JA: 情報不足による判断のぶれとみて、関連しそうなツール出力を追加で取得して文脈に加える。
  - KO: 정보 부족으로 판단이 흔들리는 것으로 보고, 관련 있어 보이는 도구 출력을 추가로 가져와 context에 더합니다.
  - EN: Treat it as wavering judgment caused by a lack of information, and fetch additional tool outputs that seem relevant and add them to the context.

## CCDV-F-Udemy2-0006

**JA** ある地図情報サービス会社は、住所表記を正規化する社内ライブラリを複数の開発チームに提供しています。このライブラリはClaudeを使っており、現在のバージョンは2.4.1です。
次の改修では、戻り値のフィールド名confidenceをscoreに変更し、旧名のconfidenceは削除します。
セマンティックバージョニングに従う場合、この改修を公開するバージョンとして最も適切なものはどれですか。

**KO** 한 지도 정보 서비스 회사는 주소 표기를 정규화하는 사내 라이브러리를 여러 개발팀에 제공하고 있습니다. 이 라이브러리는 Claude를 사용하며, 현재 버전은 2.4.1입니다.
다음 개편에서는 반환값의 필드 이름 confidence를 score로 바꾸고, 예전 이름인 confidence는 삭제합니다.
semantic versioning을 따를 때, 이 개편을 공개할 버전으로 가장 적절한 것은 무엇입니까?

- A. JA: 公開APIに後方互換性のない変更として、MAJORを上げて3.0.0として公開する。
  - KO: 공개 API에 대한 하위 호환되지 않는 변경이므로 MAJOR를 올려 3.0.0으로 공개합니다.
  - EN: Release it as 3.0.0, bumping MAJOR, since it is a backward-incompatible change to the public API.
- B. JA: 新しいフィールドを追加する変更として、MINORを上げて2.5.0として公開する。
  - KO: 새 필드를 추가하는 변경이므로 MINOR를 올려 2.5.0으로 공개합니다.
  - EN: Release it as 2.5.0, bumping MINOR, since it is a change that adds a new field.
- C. JA: 内部の不具合修正に準じる変更として、PATCHを上げて2.4.2として公開する。
  - KO: 내부 버그 수정에 준하는 변경이므로 PATCH를 올려 2.4.2로 공개합니다.
  - EN: Release it as 2.4.2, bumping PATCH, since it is a change comparable to an internal bug fix.
- D. JA: 2.4.1の公開物の中身を差し替え、変更点を利用チームへ周知して対応を依頼する。
  - KO: 이미 공개된 2.4.1의 내용을 교체하고, 변경 사항을 이용 팀에 알려 대응을 요청합니다.
  - EN: Replace the contents of the published 2.4.1 release, and notify the consuming teams of the change and ask them to adapt.

## CCDV-F-Udemy2-0007

**JA** ある損害保険会社の査定支援アプリは、事故車両を別々の角度から撮った写真3枚と、損傷箇所の比較を求める質問文を、1回のリクエストでClaudeに送っています。
現在は質問文を先頭に置き、その後ろに写真を続けて並べています。回答中の「2枚目の写真」がどれを指すのか、査定担当者が判断できないことがあります。
ユーザーメッセージ内のimageブロックとテキストの並べ方として最も適切なものはどれですか。

**KO** 한 손해보험사의 손해 사정 지원 앱은 사고 차량을 서로 다른 각도에서 찍은 사진 3장과, 손상 부위 비교를 요청하는 질문을 한 번의 요청으로 Claude에 보냅니다.
현재는 질문을 맨 앞에 두고 그 뒤에 사진을 이어서 배치하고 있습니다. 답변 속 "두 번째 사진"이 어느 사진을 가리키는지 사정 담당자가 판단하지 못하는 경우가 있습니다.
user 메시지 안에서 image 블록과 텍스트를 배치하는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: 3枚の写真を1枚の画像に横並びで結合して送り、質問文の中で左・中央・右と位置で指し示す。
  - KO: 사진 3장을 가로로 이어 붙인 이미지 1장으로 보내고, 질문에서는 왼쪽·가운데·오른쪽처럼 위치로 가리킵니다.
  - EN: Combine the three photos side by side into a single image, and refer to them by position (left, center, right) in the question.
- B. JA: 各写真の直前に「Image 1:」のようなラベルを置いて先に並べ、質問文はその後ろに置く。
  - KO: 각 사진 바로 앞에 "Image 1:" 같은 레이블을 두어 사진을 먼저 배치하고, 질문은 그 뒤에 둡니다.
  - EN: Place the photos first, each immediately preceded by a label such as "Image 1:", and put the question after them.
- C. JA: 3枚の写真はシステムプロンプトに含めて渡し、ユーザーメッセージには質問文だけを置いて送る。
  - KO: 사진 3장은 system prompt에 포함해 전달하고, user 메시지에는 질문만 넣어 보냅니다.
  - EN: Pass the three photos in the system prompt, and send only the question in the user message.
- D. JA: 3枚の写真をFiles APIにアップロードし、質問文の中に各file_idを書き込んで写真を参照させる。
  - KO: 사진 3장을 Files API에 업로드하고, 질문 안에 각 file_id를 적어 사진을 참조하게 합니다.
  - EN: Upload the three photos to the Files API, and write each file_id into the question so that Claude references the photos.

## CCDV-F-Udemy2-0008

**JA** ある広告テクノロジー企業が、エージェントを構築するにあたり、抽象化フレームワーク（LangGraph・Strands・PydanticAIなど）を採用するか、Messages APIで直接実装するかを検討しています。
トレードオフの説明として最も適切なものはどれですか。

**KO** 한 광고 테크놀로지 기업이 agent를 구축하면서 추상화 프레임워크(LangGraph·Strands·PydanticAI 등)를 채택할지, Messages API로 직접 구현할지 검토하고 있습니다.
트레이드오프에 대한 설명으로 가장 적절한 것은 무엇입니까?

- A. JA: 試作の段階で抽象化フレームワークを採用し、エージェントの構成をフレームワークの流儀に合わせる。
  - KO: 프로토타입 단계에서 추상화 프레임워크를 채택하고, agent 구성을 프레임워크의 방식에 맞춥니다.
  - EN: Adopt an abstraction framework at the prototype stage, and shape the agent's architecture to fit the framework's conventions.
- B. JA: まずMessages APIで直接実装し、複雑さに見合う利点がある場合にフレームワークを採用する。
  - KO: 먼저 Messages API로 직접 구현하고, 늘어나는 복잡성을 감수할 만한 이점이 있을 때 프레임워크를 채택합니다.
  - EN: Start by implementing directly with the Messages API, and adopt a framework when its benefits justify the added complexity.
- C. JA: フレームワーク付属の部品を優先して使い、内部プロンプトの確認は不具合が出た時点で行う。
  - KO: 프레임워크에 딸린 구성 요소를 우선 사용하고, 내부 prompt 확인은 문제가 생긴 시점에 합니다.
  - EN: Prefer the components bundled with the framework, and inspect its internal prompts only once a bug appears.
- D. JA: 将来のマルチエージェント化を見込み、複数エージェントを編成できる基盤を先に整えておく。
  - KO: 향후 multi-agent 전환을 내다보고, 여러 agent를 편성할 수 있는 기반을 먼저 갖춰 둡니다.
  - EN: Anticipating a future move to multiple agents, build a foundation for orchestrating multiple agents up front.

## CCDV-F-Udemy2-0009

**JA** ある証券会社が、Claudeでリサーチ要約を生成し、トレーディングダッシュボードに渡すソリューションアーキテクチャを描きました。開発チームは、ここから機能要件を導き出す必要があります。
ソリューションアーキテクチャから機能要件を正しく導く活動はどれですか。

**KO** 한 증권사가 Claude로 리서치 요약을 생성해 트레이딩 대시보드에 전달하는 솔루션 아키텍처를 그렸습니다. 개발팀은 여기서 기능 요구 사항을 도출해야 합니다.
솔루션 아키텍처에서 기능 요구 사항을 올바르게 도출하는 활동은 무엇입니까?

- A. JA: 各部分の入出力と受け入れ基準を、テストで合否を判定できる要件として書き出す。
  - KO: 각 부분의 입출력과 인수 기준을, 테스트로 합격 여부를 판정할 수 있는 요구 사항으로 적어 냅니다.
  - EN: Write down each part's inputs, outputs, and acceptance criteria as requirements whose pass/fail can be determined by tests.
- B. JA: アーキテクチャ図の各コンポーネントを、そのまま開発タスクの一覧として担当者に割り振る。
  - KO: 아키텍처 다이어그램의 각 컴포넌트를 그대로 개발 작업 목록으로 삼아 담당자에게 할당합니다.
  - EN: Assign each component in the architecture diagram to developers as is, as a list of development tasks.
- C. JA: 採用するモデルIDとAPIのパラメータを先に確定し、その設定値を要件定義書に記載する。
  - KO: 채택할 모델 ID와 API 파라미터를 먼저 확정하고, 그 설정값을 요구 사항 정의서에 기재합니다.
  - EN: Finalize the model ID and API parameters first, and record those settings in the requirements definition document.
- D. JA: プロトタイプを先に作ってステークホルダーに見せ、好評だった挙動を要件として追記する。
  - KO: 프로토타입을 먼저 만들어 이해관계자에게 보여 주고, 반응이 좋았던 동작을 요구 사항으로 추가합니다.
  - EN: Build a prototype first and show it to stakeholders, then add the well-received behaviors as requirements.

## CCDV-F-Udemy2-0010

**JA** ある出版社のアプリには、次の2種類の処理があります。
編集者がエディタ上でClaudeに即答を求める対話操作
バックカタログ全体を一括で再整形する大量ジョブ
同期アーキテクチャと非同期アーキテクチャの選択基準として最も適切なものはどれですか。

**KO** 한 출판사의 앱에는 다음 두 종류의 처리가 있습니다.
편집자가 에디터에서 Claude에게 즉답을 요청하는 대화형 작업
백카탈로그 전체를 일괄로 재포맷하는 대량 작업
동기 아키텍처와 비동기 아키텍처를 고르는 기준으로 가장 적절한 것은 무엇입니까?

- A. JA: 両方の処理をMessage Batches APIに投入し、編集者の操作にも結果のポーリングで応答する。
  - KO: 두 처리 모두 Message Batches API에 제출하고, 편집자의 작업에도 결과 polling으로 응답합니다.
  - EN: Submit both types of processing to the Message Batches API, and respond to editor operations by polling for results as well.
- B. JA: 両方の処理を同期のAPI呼び出しで実装し、再整形ジョブにはHTTPのタイムアウトを長めに設定する。
  - KO: 두 처리 모두 동기 API 호출로 구현하고, 재포맷 작업에는 HTTP timeout을 길게 설정합니다.
  - EN: Implement both types of processing with synchronous API calls, and set a longer HTTP timeout for the reformatting job.
- C. JA: 編集者の対話操作は同期で処理し、全カタログの再整形はキューやバッチで非同期に処理する。
  - KO: 편집자의 대화형 작업은 동기로 처리하고, 전체 카탈로그 재포맷은 큐나 batch로 비동기 처리합니다.
  - EN: Process the editors' interactive operations synchronously, and process the full-catalog reformatting asynchronously with queues or batches.
- D. JA: 両方の処理でストリーミングを使い、再整形ジョブも編集者の画面に進捗を流しながら実行する。
  - KO: 두 처리 모두 streaming을 사용하고, 재포맷 작업도 편집자 화면에 진행 상황을 흘려보내며 실행합니다.
  - EN: Use streaming for both types of processing, and run the reformatting job while streaming its progress to the editors' screens.

## CCDV-F-Udemy2-0011

**JA** ある飲食チェーンが、店舗レビューをClaudeで分類・要約しています。運用コストを把握するため、リクエストごとのトークン使用量を追跡したいと考えています。
トークン使用量をリクエスト単位で追跡する方法として最も適切なものはどれですか。

**KO** 한 외식 체인이 매장 리뷰를 Claude로 분류·요약하고 있습니다. 운영 비용을 파악하기 위해 요청별 token 사용량을 추적하려고 합니다.
token 사용량을 요청 단위로 추적하는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: 各レスポンスのusageのinput_tokensやoutput_tokensを記録し、呼び出しごとに集計する。
  - KO: 각 응답의 usage에 있는 input_tokens와 output_tokens를 기록하고, 호출별로 집계합니다.
  - EN: Record input_tokens and output_tokens from the usage field of each response, and aggregate them per call.
- B. JA: 応答の本文に使用したトークン数を書かせ、その値をusageとしてログに記録して集計する。
  - KO: 응답 본문에 사용한 token 수를 쓰게 하고, 그 값을 usage로 로그에 기록해 집계합니다.
  - EN: Have the model write the number of tokens it used in the response body, and log and aggregate that value as usage.
- C. JA: 月末にConsoleのUsage画面で請求額を確認し、その月のリクエスト件数で割って1件あたりのコストとする。
  - KO: 월말에 Console의 Usage 화면에서 청구 금액을 확인하고, 그달의 요청 건수로 나눠 건당 비용으로 삼습니다.
  - EN: Check the billed amount on the Console's Usage page at the end of the month, and divide it by that month's request count to get the cost per request.
- D. JA: 送信前にcount_tokensエンドポイントで数えた入力トークン数を記録し、実際の使用量として集計する。
  - KO: 보내기 전에 count_tokens 엔드포인트로 센 입력 token 수를 기록하고, 실제 사용량으로 집계합니다.
  - EN: Record the input token count measured with the count_tokens endpoint before sending, and aggregate it as the actual usage.

## CCDV-F-Udemy2-0012

**JA** ある映画配給会社が、数万行の短い字幕を多数の言語へ機械翻訳します。各行は短く定型的で、品質は許容範囲で十分です。コストとスループットが最優先です。
モデルの選定として最も妥当なものはどれですか。

**KO** 한 영화 배급사가 짧은 자막 수만 줄을 여러 언어로 기계 번역합니다. 각 줄은 짧고 정형적이며, 품질은 허용 범위면 충분합니다. 비용과 처리량이 최우선입니다.
모델 선정으로 가장 타당한 것은 무엇입니까?

- A. JA: 全行をClaude Opusで翻訳し、エフォートを低めに設定して1行あたりのコストを抑える。
  - KO: 모든 줄을 Claude Opus로 번역하고, effort를 낮게 설정해 줄당 비용을 억제합니다.
  - EN: Translate all lines with Claude Opus, setting effort low to keep the cost per line down.
- B. JA: 言語ごとに複数のモデルで翻訳させ、評価役のLLMが最良の訳を選んで採用する。
  - KO: 언어마다 여러 모델로 번역하게 하고, 평가 역할의 LLM이 가장 좋은 번역을 골라 채택합니다.
  - EN: Have multiple models translate each language, and have an evaluator LLM select and adopt the best translation.
- C. JA: 全行を最速で低価格なClaude Haikuで翻訳し、抜き取り評価で訳文の品質を確認する。
  - KO: 모든 줄을 가장 빠르고 저렴한 Claude Haiku로 번역하고, 표본 평가로 번역 품질을 확인합니다.
  - EN: Translate all lines with Claude Haiku, the fastest and lowest-cost model, and check translation quality with spot-check evaluations.
- D. JA: 全行を最上位のClaude Fableで翻訳し、訳文の品質を最大限に高めてから配信する。
  - KO: 모든 줄을 최상위 모델인 Claude Fable로 번역해 번역 품질을 최대한 높인 뒤 배포합니다.
  - EN: Translate all lines with the top-tier Claude Fable, maximizing translation quality before distribution.

## CCDV-F-Udemy2-0013

**JA** ある航空会社の運航統制センターが、悪天候・乗務員不足・機材変更が絡む運航乱れに対応するシステムを構築したいと考えています。発生する状況は事前に予測できず、その場ごとに必要な手順が変わるため、動的な判断が求められます。
この要件に最も適したアーキテクチャはどれですか。

**KO** 한 항공사의 운항 통제 센터가 악천후·승무원 부족·기재 변경이 얽힌 운항 차질에 대응하는 시스템을 구축하려고 합니다. 발생하는 상황을 미리 예측할 수 없고 그때그때 필요한 절차가 달라지므로, 동적인 판단이 요구됩니다.
이 요구 사항에 가장 적합한 아키텍처는 무엇입니까?

- A. JA: 複数のLLMに同じ再計画案を並列で作らせ、多数決で採用案を決めるparallelizationで実装する。
  - KO: 여러 LLM에게 같은 재계획안을 병렬로 만들게 하고, 다수결로 채택안을 정하는 parallelization으로 구현합니다.
  - EN: Implement it with parallelization, having multiple LLMs produce the same replanning proposal in parallel and choosing the plan to adopt by majority vote.
- B. JA: Claudeが状況を見てツールの使用と次の手順を判断し、結果を確かめながら進むエージェントで実装する。
  - KO: Claude가 상황을 보고 도구 사용과 다음 절차를 판단하며, 결과를 확인하면서 진행하는 agent로 구현합니다.
  - EN: Implement it as an agent in which Claude assesses the situation, decides on tool use and next steps, and proceeds while checking the results.
- C. JA: 入力を運航乱れの種別に分類し、種別ごとに用意した対応フローへ振り分けるroutingで実装する。
  - KO: 입력을 운항 차질 유형별로 분류하고, 유형마다 준비한 대응 흐름으로 보내는 routing으로 구현합니다.
  - EN: Implement it with routing, classifying the input by type of disruption and dispatching it to a response flow prepared for each type.
- D. JA: 対応手順を事前に定義し、各LLM呼び出しが前段の出力を受けて順に進むprompt chainingで実装する。
  - KO: 대응 절차를 미리 정의하고, 각 LLM 호출이 앞 단계의 출력을 받아 차례로 진행하는 prompt chaining으로 구현합니다.
  - EN: Implement it with prompt chaining, defining the response steps in advance so that each LLM call proceeds in order using the previous step's output.

## CCDV-F-Udemy2-0014

**JA** あるニュースメディア企業が、自社の記事について答える一般公開のClaudeチャットボットを運用しています。一部の利用者は、禁止されたコンテンツを生成させようと、ボットをジェイルブレイクする入力を作ってきます（利用者自身が攻撃者となる直接的な脅威）。
最も効果的な緩和策はどれですか。

**KO** 한 뉴스 미디어 기업이 자사 기사에 관해 답하는 일반 공개 Claude 챗봇을 운영하고 있습니다. 일부 이용자는 금지된 콘텐츠를 생성하게 하려고 봇을 jailbreak하는 입력을 만들어 보냅니다(이용자 자신이 공격자가 되는 직접적인 위협).
가장 효과적인 완화책은 무엇입니까?

- A. JA: 軽量モデルで入力を事前審査し、倫理的な境界と断り方を指示し、違反を繰り返す利用者を制限する。
  - KO: 경량 모델로 입력을 사전 심사하고, 윤리적 경계와 거절 방법을 지시하며, 위반을 반복하는 이용자를 제한합니다.
  - EN: Pre-screen inputs with a lightweight model, instruct the bot on ethical boundaries and how to decline, and restrict users who repeatedly violate the rules.
- B. JA: 利用者のメッセージをtool_resultブロックに入れて渡し、信頼できない入力として扱わせる。
  - KO: 이용자 메시지를 tool_result 블록에 넣어 전달해, 신뢰할 수 없는 입력으로 다루게 합니다.
  - EN: Pass user messages inside tool_result blocks so that they are treated as untrusted input.
- C. JA: 取得した記事本文をJSONで符号化して渡し、記事と指示の境界を明確にしてから回答させる。
  - KO: 가져온 기사 본문을 JSON으로 인코딩해 전달하고, 기사와 지시의 경계를 명확히 한 뒤 답하게 합니다.
  - EN: Encode the retrieved article text as JSON to make the boundary between articles and instructions clear before having the bot answer.
- D. JA: 指示追従性の高いモデルに切り替え、禁止事項をシステムプロンプトに列挙し、毎ターン再掲する。
  - KO: 지시를 잘 따르는 모델로 바꾸고, 금지 사항을 system prompt에 나열해 매 turn 다시 제시합니다.
  - EN: Switch to a model with stronger instruction following, list the prohibited items in the system prompt, and restate them every turn.

## CCDV-F-Udemy2-0015

**JA** あるK-12向けの学習支援アプリで、授業開始直後にClaude APIへのリクエストが集中し、429エラーを受けるようになりました。
レートリミットの基礎と対処として最も適切なものはどれですか。

**KO** 한 K-12 대상 학습 지원 앱에서 수업 시작 직후 Claude API 요청이 몰려 429 오류를 받게 되었습니다.
rate limit의 기초와 대처로 가장 적절한 것은 무엇입니까?

- A. JA: retry-afterに従い指数バックオフで再試行し、共通の長い指示はプロンプトキャッシングする。
  - KO: retry-after에 따라 exponential backoff로 재시도하고, 공통의 긴 지시는 prompt caching합니다.
  - EN: Retry with exponential backoff that follows retry-after, and use prompt caching for long shared instructions.
- B. JA: Message Batches APIへ切り替え、授業中の質問への回答をバッチの処理完了後に返す。
  - KO: Message Batches API로 전환하고, 수업 중 질문에 대한 답변을 batch 처리가 끝난 뒤 반환합니다.
  - EN: Switch to the Message Batches API, and return answers to in-class questions after batch processing completes.
- C. JA: max_tokensを小さく設定し直し、OTPMの消費枠を空けて429エラーを回避する。
  - KO: max_tokens를 작게 다시 설정해 OTPM 소비 한도에 여유를 만들어 429 오류를 피합니다.
  - EN: Reset max_tokens to a smaller value to free up OTPM capacity and avoid 429 errors.
- D. JA: リクエストを複数のワークスペースに分散させ、各ワークスペースの上限を合算した枠で処理する。
  - KO: 요청을 여러 workspace에 분산하고, 각 workspace의 한도를 합친 범위에서 처리합니다.
  - EN: Distribute requests across multiple workspaces, and process them within the combined limits of all the workspaces.

## CCDV-F-Udemy2-0016

**JA** ある食品メーカーが、複数のツールを使って生産ラインの点検を自動化するエージェントを運用しています。しかし、ツール使用ループがときどき暴走したり、無限に繰り返したりします。
このようなツール使用ループの失敗を防ぐ対策として、適切なものはどれですか。（2つ選択してください。）

**KO** 한 식품 제조사가 여러 도구를 사용해 생산 라인 점검을 자동화하는 agent를 운영하고 있습니다. 그런데 tool use loop가 가끔 폭주하거나 끝없이 반복됩니다.
이러한 tool use loop 실패를 막는 대책으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 繰り返し呼ばれるツールの定義と結果をプロンプトキャッシングの対象にし、1回あたりの入力コストを下げる。
  - KO: 반복 호출되는 도구의 정의와 결과를 prompt caching 대상으로 삼아 호출당 입력 비용을 낮춥니다.
  - EN: Apply prompt caching to the definitions and results of repeatedly called tools to lower the input cost per call.
- B. JA: 各ステップのツール結果を検証し、ゴールの達成を判定したら終了する停止条件を設ける。
  - KO: 각 단계의 도구 결과를 검증하고, 목표 달성을 판정하면 종료하는 정지 조건을 둡니다.
  - EN: Validate the tool results at each step, and set a stop condition that ends the loop once the goal is judged to be achieved.
- C. JA: disable_parallel_tool_useをtrueにして、1回の応答で呼び出すツールを最大1つに絞る。
  - KO: disable_parallel_tool_use를 true로 설정해 한 번의 응답에서 호출하는 도구를 최대 1개로 제한합니다.
  - EN: Set disable_parallel_tool_use to true to limit each response to at most one tool call.
- D. JA: ツール使用の往復回数に上限（max_turnsなど）を設け、上限に達したらループを打ち切る。
  - KO: 도구 사용 왕복 횟수에 상한(max_turns 등)을 두고, 상한에 도달하면 loop를 중단합니다.
  - EN: Set a cap on the number of tool use round trips (such as max_turns), and stop the loop when the cap is reached.
- E. JA: ループの途中で古いツール結果を要約に置き換え、コンテキストの空きを確保する。
  - KO: loop 도중에 오래된 도구 결과를 요약으로 바꿔 context의 여유 공간을 확보합니다.
  - EN: Replace old tool results with summaries partway through the loop to free up space in the context.

## CCDV-F-Udemy2-0017

**JA** ある法律事務所が、Claudeを使う次の2つの機能を設計しています。
分析機能（複雑な契約書の条項間の整合性を、多段の推論で精査する）
社内FAQ機能（条文番号を尋ねると、即座に定型の回答を返す）
高速モードと拡張思考（適応型思考／エフォートレベル）の使い分けとして、適切なものはどれですか。（2つ選択してください。）

**KO** 한 법률 사무소가 Claude를 사용하는 다음 두 기능을 설계하고 있습니다.
분석 기능(복잡한 계약서의 조항 간 정합성을 다단계 추론으로 면밀히 검토)
사내 FAQ 기능(조항 번호를 물으면 즉시 정형화된 답변을 반환)
fast mode와 extended thinking(adaptive thinking/effort 수준)을 구분해 쓰는 방법으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 契約の整合性分析では、エフォートをhighにして多段の推論に十分な思考を割り当てる。
  - KO: 계약 정합성 분석에서는 effort를 high로 설정해 다단계 추론에 충분한 사고를 할당합니다.
  - EN: For the contract consistency analysis, set effort to high to allocate sufficient thinking to the multi-step reasoning.
- B. JA: FAQ機能では、エフォートをlowにして思考を抑え、応答時間とトークン消費を減らす。
  - KO: FAQ 기능에서는 effort를 low로 설정해 사고를 줄이고, 응답 시간과 token 소비를 줄입니다.
  - EN: For the FAQ feature, set effort to low to limit thinking and reduce response time and token consumption.
- C. JA: FAQ機能でもエフォートをmaxに設定し、単純な条文番号の質問にも十分な思考をさせて回答の質を高める。
  - KO: FAQ 기능에서도 effort를 max로 설정해, 단순한 조항 번호 질문에도 충분히 사고하게 해서 답변 품질을 높입니다.
  - EN: Set effort to max even for the FAQ feature, so that Claude thinks thoroughly even on simple clause-number questions and answer quality improves.
- D. JA: 契約の整合性分析では、思考を無効にして応答を速め、1回の出力で結論を出させる。
  - KO: 계약 정합성 분석에서는 thinking을 비활성화해 응답을 빠르게 하고, 한 번의 출력으로 결론을 내게 합니다.
  - EN: For the contract consistency analysis, disable thinking to speed up responses, and have Claude reach a conclusion in a single output.
- E. JA: FAQ機能では、高速モード（speed: "fast"）を有効にし、回答1件あたりの料金を下げる。
  - KO: FAQ 기능에서는 fast mode(speed: "fast")를 활성화해 답변 1건당 요금을 낮춥니다.
  - EN: For the FAQ feature, enable fast mode (speed: "fast") to lower the price per answer.

## CCDV-F-Udemy2-0018

**JA** ある介護事業者が、毎日蓄積される大量のケア記録を夜間にまとめて処理し、翌朝までに緊急性のない要約レポートを生成したいと考えています。即時応答は不要で、コストを最優先にしています。
Message Batches APIを使う場合の運用として最も適切なものはどれですか。

**KO** 한 요양 서비스 사업자가 매일 쌓이는 대량의 케어 기록을 야간에 일괄 처리해, 다음 날 아침까지 긴급하지 않은 요약 보고서를 생성하려고 합니다. 즉시 응답은 필요 없고 비용을 최우선으로 삼고 있습니다.
Message Batches API를 사용할 때의 운영 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: Message Batches APIに投入し、processing_statusがendedになってから結果を取得する。
  - KO: Message Batches API에 제출하고, processing_status가 ended가 된 뒤에 결과를 가져옵니다.
  - EN: Submit the requests to the Message Batches API, and retrieve the results after processing_status becomes ended.
- B. JA: Message Batches APIの各リクエストにstream: trueを指定し、生成されたトークンを逐次保存する。
  - KO: Message Batches API의 각 요청에 stream: true를 지정하고, 생성된 token을 순차적으로 저장합니다.
  - EN: Specify stream: true on each request in the Message Batches API, and save the generated tokens incrementally.
- C. JA: 記録ごとにMessages APIを同期で呼び出し、夜間の空き時間に順番に処理して結果を保存する。
  - KO: 기록마다 Messages API를 동기로 호출하고, 야간의 빈 시간에 차례로 처리해 결과를 저장합니다.
  - EN: Call the Messages API synchronously for each record, processing them one by one during idle overnight hours and saving the results.
- D. JA: Message Batches APIへの投入直後にresults_urlを取得し、その時点の結果を翌朝のレポートに使う。
  - KO: Message Batches API에 제출한 직후 results_url을 가져오고, 그 시점의 결과를 다음 날 아침 보고서에 사용합니다.
  - EN: Fetch results_url immediately after submitting to the Message Batches API, and use the results available at that point for the next morning's report.

## CCDV-F-Udemy2-0019

**JA** ある建設会社が、現場点検の所見をClaudeに構造化JSONで出力させ、点検日・是正コスト・重大度などのフィールドを型付きのバックエンドに取り込んでいます。
JSONのシリアライズ/デシリアライズと型の扱いとして最も適切なものはどれですか。

**KO** 한 건설사가 현장 점검 소견을 Claude가 구조화된 JSON으로 출력하게 하고, 점검일·시정 비용·심각도 등의 필드를 타입이 지정된 백엔드에 적재하고 있습니다.
JSON 직렬화/역직렬화와 타입 처리로 가장 적절한 것은 무엇입니까?

- A. JA: 受信したJSONをスキーマで検証し、日付や金額は明示的に日付型・Decimal型へ変換する。
  - KO: 받은 JSON을 schema로 검증하고, 날짜와 금액은 명시적으로 날짜형·Decimal형으로 변환합니다.
  - EN: Validate the received JSON against a schema, and explicitly convert dates and amounts to date and Decimal types.
- B. JA: 点検日は文字列のままデータベースへ格納し、比較や集計が必要になった時点で都度解釈する。
  - KO: 점검일은 문자열 그대로 데이터베이스에 저장하고, 비교나 집계가 필요해질 때마다 그때그때 해석합니다.
  - EN: Store the inspection date in the database as a string, and interpret it each time a comparison or aggregation is needed.
- C. JA: JSONの数値をそのまま浮動小数点型として受け取り、是正コストの集計にもその値を使う。
  - KO: JSON의 숫자를 그대로 부동소수점형으로 받고, 시정 비용 집계에도 그 값을 사용합니다.
  - EN: Receive JSON numbers as floating-point values as is, and use those values when aggregating remediation costs as well.
- D. JA: 日付の文字列から日付型への復元はJSONパーサーに任せ、型の変換処理は書かずに取り込む。
  - KO: 날짜 문자열을 날짜형으로 복원하는 일은 JSON 파서에 맡기고, 타입 변환 처리는 작성하지 않고 적재합니다.
  - EN: Leave the restoration of date strings to date types to the JSON parser, and ingest the data without writing any type conversion logic.

## CCDV-F-Udemy2-0020

**JA** ある建設会社がClaude Codeを使っています。標準化された現場安全報告書を作るための同じ多段手順のチェックリスト（書式ルール・必須セクション・レビュー手順）を、毎回チャットに貼り付けています。
このチェックリストをパッケージ化し、関連するときだけ読み込ませて、Claudeに一貫して従わせたいと考えています。
どの仕組みで実現するのが最も適切ですか。

**KO** 한 건설사가 Claude Code를 사용하고 있습니다. 표준화된 현장 안전 보고서를 만들기 위한 동일한 다단계 절차 체크리스트(서식 규칙·필수 섹션·검토 절차)를 매번 채팅에 붙여 넣고 있습니다.
이 체크리스트를 패키지로 만들어 관련 있을 때만 불러오게 하고, Claude가 일관되게 따르게 하려고 합니다.
어떤 메커니즘으로 구현하는 것이 가장 적절합니까?

- A. JA: カスタムツールとして、チェックリストをinput_schemaに落とし込み、Claudeに呼び出させる。
  - KO: custom tool로 구현해, 체크리스트를 input_schema에 녹여 넣고 Claude가 호출하게 합니다.
  - EN: As a custom tool: encode the checklist into an input_schema and have Claude call the tool.
- B. JA: スキルとして、手順と補足資料をSKILL.mdにまとめ、関連する場面で本文を読み込ませる。
  - KO: skill로 구현해, 절차와 보충 자료를 SKILL.md에 정리하고 관련 있는 상황에서 본문을 불러오게 합니다.
  - EN: As a skill: consolidate the steps and supporting materials into SKILL.md, and have its body loaded when relevant.
- C. JA: CLAUDE.mdとして、チェックリストの全文を書き込み、セッション開始時に毎回読み込ませる。
  - KO: CLAUDE.md를 사용해, 체크리스트 전문을 적어 두고 session을 시작할 때마다 불러오게 합니다.
  - EN: As CLAUDE.md: write the full text of the checklist into it, and have it loaded at the start of every session.
- D. JA: MCPサーバーとして、チェックリストをresourceで公開し、Claude Codeから参照させる。
  - KO: MCP server로 구현해, 체크리스트를 resource로 공개하고 Claude Code에서 참조하게 합니다.
  - EN: As an MCP server: expose the checklist as a resource, and have Claude Code reference it.

## CCDV-F-Udemy2-0021

**JA** あるスポーツ分析プラットフォームが、Claude用のツールget_player_statsを定義しています。Claudeは、利用者が指定していないパラメータに推測した値を入れて呼び出したり、誤った型で呼び出したりすることがあります。
ツール呼び出しの正確さを最も高めるinput_schemaの設計はどれですか。

**KO** 한 스포츠 분석 플랫폼이 Claude용 도구 get_player_stats를 정의했습니다. Claude가 이용자가 지정하지 않은 파라미터에 추측한 값을 넣어 호출하거나, 잘못된 타입으로 호출하는 경우가 있습니다.
도구 호출의 정확성을 가장 높이는 input_schema 설계는 무엇입니까?

- A. JA: 全プロパティの型をstringにそろえ、数値や日付への変換は受け取り側のコードで行う。
  - KO: 모든 property의 타입을 string으로 통일하고, 숫자나 날짜로의 변환은 받는 쪽 코드에서 처리합니다.
  - EN: Make every property a string type, and perform conversions to numbers and dates in the receiving code.
- B. JA: requiredの指定を外し、利用者が値を示さなかった引数も省略して呼び出せるスキーマにする。
  - KO: required 지정을 없애, 이용자가 값을 제시하지 않은 인수는 생략하고 호출할 수 있는 schema로 만듭니다.
  - EN: Remove the required specification so that the schema allows calls that omit arguments the user did not provide.
- C. JA: 引数の説明はシステムプロンプトにまとめて書き、input_schemaのpropertiesは空のままにする。
  - KO: 인수 설명은 system prompt에 모아 적고, input_schema의 properties는 비워 둡니다.
  - EN: Write all the argument descriptions in the system prompt, and leave the input_schema properties empty.
- D. JA: 各プロパティに正しい型と、単位・形式を含む説明を付け、本当に必要な引数をrequiredに列挙する。
  - KO: 각 property에 올바른 타입과 단위·형식을 포함한 설명을 붙이고, 정말 필요한 인수를 required에 나열합니다.
  - EN: Give each property the correct type and a description that includes units and format, and list the truly necessary arguments in required.

## CCDV-F-Udemy2-0022

**JA** ある気象情報会社が、Claude Codeで社内の予報配信ツールを開発しています。組織全体の方針、開発者個人の好み、プロジェクトで共有するルールを、CLAUDE.mdで使い分けたいと考えています。
CLAUDE.mdの階層と優先順位の説明として最も適切なものはどれですか。

**KO** 한 기상 정보 회사가 Claude Code로 사내 예보 배포 도구를 개발하고 있습니다. 조직 전체의 방침, 개발자 개인의 선호, 프로젝트에서 공유하는 규칙을 CLAUDE.md로 구분해 관리하려고 합니다.
CLAUDE.md의 계층과 우선순위에 대한 설명으로 가장 적절한 것은 무엇입니까?

- A. JA: settings.jsonと同様に、狭いスコープのCLAUDE.mdが広いスコープの同じ指示を上書きする。
  - KO: settings.json과 마찬가지로, 범위가 좁은 CLAUDE.md가 범위가 넓은 CLAUDE.md의 같은 지시를 덮어씁니다.
  - EN: As with settings.json, a narrower-scope CLAUDE.md overrides the same instruction in a broader-scope CLAUDE.md.
- B. JA: 起動時にはプロジェクト直下のCLAUDE.mdだけを読み込み、ユーザー用のファイルは/memoryで読み込む。
  - KO: 시작할 때는 프로젝트 루트의 CLAUDE.md만 불러오고, 사용자용 파일은 /memory로 불러옵니다.
  - EN: Only the CLAUDE.md at the project root is loaded at startup, and the user file is loaded with /memory.
- C. JA: マネージドポリシー→ユーザー→プロジェクトの順に読み込まれて連結され、組織の方針は除外できない。
  - KO: managed policy→사용자→프로젝트 순으로 불러와 이어 붙이며, 조직의 방침은 제외할 수 없습니다.
  - EN: The files are loaded and concatenated in the order managed policy → user → project, and the organization's policy cannot be excluded.
- D. JA: claudeMdExcludesにマネージドポリシーのパスを指定すれば、個人の環境で組織の方針を除外できる。
  - KO: claudeMdExcludes에 managed policy의 경로를 지정하면 개인 환경에서 조직의 방침을 제외할 수 있습니다.
  - EN: Specifying the managed policy's path in claudeMdExcludes lets an individual exclude the organization's policy in their own environment.

## CCDV-F-Udemy2-0023

**JA** ある物流会社が、出荷ルーティングのバックエンドサービスにClaudeを組み込み、大規模に自動実行したいと考えています。
Claudeを利用するインターフェース（API/SDKの直接利用、Claude Code、Claude Desktop/claude.ai）の選び方として最も適切なものはどれですか。

**KO** 한 물류 회사가 출하 routing 백엔드 서비스에 Claude를 통합해 대규모로 자동 실행하려고 합니다.
Claude를 이용하는 인터페이스(API/SDK 직접 이용, Claude Code, Claude Desktop/claude.ai)를 고르는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: Claude Desktopに社内システムのMCPサーバーを接続し、担当者の指示でルーティングを実行させる。
  - KO: Claude Desktop에 사내 시스템의 MCP server를 연결하고, 담당자의 지시로 routing을 실행하게 합니다.
  - EN: Connect an MCP server for the internal systems to Claude Desktop, and have it execute routing on staff instructions.
- B. JA: Claude Codeをサーバー上で対話モードのまま常駐させ、バックエンドから入力を送り込んで処理させる。
  - KO: Claude Code를 서버에서 대화형 모드로 상주시키고, 백엔드에서 입력을 보내 처리하게 합니다.
  - EN: Keep Claude Code running on a server in interactive mode, and have the backend feed it input for processing.
- C. JA: 担当者がclaude.aiのチャット画面に出荷データを貼り付け、得られた結果を業務システムへ転記する。
  - KO: 담당자가 claude.ai 채팅 화면에 출하 데이터를 붙여 넣고, 얻은 결과를 업무 시스템에 옮겨 적습니다.
  - EN: Have staff paste shipment data into the claude.ai chat screen, and transcribe the results into the business system.
- D. JA: バックエンドのコードからClient SDKでClaude APIを呼び出し、ルーティング処理に組み込む。
  - KO: 백엔드 코드에서 Client SDK로 Claude API를 호출해 routing 처리에 통합합니다.
  - EN: Call the Claude API from the backend code with the Client SDK, and integrate it into the routing process.

## CCDV-F-Udemy2-0024

**JA** ある音楽配信アプリが、ユーザーが自由に投稿したレビューや楽曲説明（ユーザー生成コンテンツ）を、Claudeに要約・分類させる機能を追加します。
ユーザー生成コンテンツを扱う際の設計上の考慮点として、適切なものはどれですか。（2つ選択してください。）

**KO** 한 음악 streaming 앱이 사용자가 자유롭게 올린 리뷰와 곡 설명(사용자 생성 콘텐츠)을 Claude가 요약·분류하는 기능을 추가합니다.
사용자 생성 콘텐츠를 다룰 때의 설계상 고려 사항으로 적절한 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: 投稿を信頼できない入力として扱い、システム指示と分けて渡し、投稿内の指示には従わせない。
  - KO: 게시물을 신뢰할 수 없는 입력으로 다루고, 시스템 지시와 분리해 전달하며, 게시물 안의 지시는 따르지 않게 합니다.
  - EN: Treat posts as untrusted input, pass them separately from the system instructions, and do not let Claude follow instructions inside the posts.
- B. JA: 投稿の審査は通報を受けた後の事後対応とし、要約・分類の処理は事前のチェックなしで進める。
  - KO: 게시물 심사는 신고를 받은 뒤의 사후 대응으로 하고, 요약·분류 처리는 사전 점검 없이 진행합니다.
  - EN: Handle post moderation reactively after reports are received, and run summarization and classification without any prior checks.
- C. JA: 投稿の本文をシステムプロンプトに直接連結し、運営側の指示と同じ文脈で渡す。
  - KO: 게시물 본문을 system prompt에 직접 연결해, 운영자 측 지시와 같은 문맥으로 전달합니다.
  - EN: Concatenate the post text directly into the system prompt, passing it in the same context as the operator's instructions.
- D. JA: max_tokensを小さく設定し、投稿に埋め込まれた指示が長い出力を生む余地を減らす。
  - KO: max_tokens를 작게 설정해, 게시물에 심어진 지시가 긴 출력을 만들어 낼 여지를 줄입니다.
  - EN: Set max_tokens to a small value to reduce the room for instructions embedded in posts to produce long outputs.
- E. JA: 軽量モデルによる事前分類などで投稿を審査し、個人情報や不適切な内容を検出・除去する。
  - KO: 경량 모델을 이용한 사전 분류 등으로 게시물을 심사해, 개인 정보나 부적절한 내용을 탐지·제거합니다.
  - EN: Screen posts, for example with pre-classification by a lightweight model, to detect and remove personal information and inappropriate content.

## CCDV-F-Udemy2-0025

**JA** ある不動産会社が、物件説明文をClaudeで自動生成していますが、出力の粒度やトーンが安定しません。
指示の明確化と反復的な改良の進め方として最も適切なものはどれですか。

**KO** 한 부동산 회사가 매물 설명문을 Claude로 자동 생성하고 있지만, 출력의 상세도와 톤이 안정적이지 않습니다.
지시를 명확히 하고 반복적으로 개선하는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: 良い出力が出るまでプロンプトを書き換えて試し、気に入った出力が出た時点の文面を本番に採用する。
  - KO: 좋은 출력이 나올 때까지 prompt를 고쳐 가며 시험하고, 마음에 드는 출력이 나온 시점의 문안을 프로덕션에 채택합니다.
  - EN: Keep rewriting and testing the prompt until a good output appears, and adopt the wording at the point a satisfying output appears for production.
- B. JA: 粒度とトーンのぶれはモデルの能力不足とみて、より上位のモデルへの切り替えから検討する。
  - KO: 상세도와 톤의 편차는 모델의 능력 부족으로 보고, 더 상위 모델로 바꾸는 것부터 검토합니다.
  - EN: Treat the inconsistency in detail and tone as a lack of model capability, and start by considering a switch to a higher-tier model.
- C. JA: 成功基準とそれを測る評価を先に用意し、具体的な指示や例を加えて結果を見ながら改善する。
  - KO: 성공 기준과 이를 측정할 평가를 먼저 준비하고, 구체적인 지시와 예시를 추가해 결과를 보면서 개선합니다.
  - EN: Prepare success criteria and evaluations that measure them first, then improve the prompt by adding specific instructions and examples while checking the results.
- D. JA: 出力の粒度とトーンを禁止事項で縛り、「〜しないこと」を列挙した指示をプロンプトに加える。
  - KO: 출력의 상세도와 톤을 금지 사항으로 묶어 두고, "~하지 말 것"을 나열한 지시를 prompt에 추가합니다.
  - EN: Constrain the output's level of detail and tone with prohibitions, adding instructions to the prompt that list "do not ..." items.

## CCDV-F-Udemy2-0026

**JA** あるゲームスタジオが、長時間・非同期に動くエージェントを本番で運用したいと考えています。ただし、サンドボックスやセッション状態の基盤を自社で運用する余力はありません。
この状況に適したデプロイモデルと、その特徴の説明として最も適切なものはどれですか。

**KO** 한 게임 스튜디오가 장시간·비동기로 동작하는 agent를 프로덕션에서 운영하려고 합니다. 다만 sandbox나 session 상태 인프라를 자체 운영할 여력은 없습니다.
이 상황에 맞는 배포 모델과 그 특징에 대한 설명으로 가장 적절한 것은 무엇입니까?

- A. JA: Agent SDKを自社のコンテナで動かし、セッションの状態とサンドボックスを自社で運用する。
  - KO: Agent SDK를 자사 컨테이너에서 실행하고, session 상태와 sandbox를 자체 운영합니다.
  - EN: Run the Agent SDK in the company's own containers, and operate the session state and sandboxes in-house.
- B. JA: Messages APIとClient SDKのtool runnerでループを組み、実行環境を自社サーバーに用意する。
  - KO: Messages API와 Client SDK의 tool runner로 loop를 구성하고, 실행 환경을 자사 서버에 마련합니다.
  - EN: Build the loop with the Messages API and the Client SDK's tool runner, and provide the execution environment on the company's own servers.
- C. JA: Claude Managed Agentsを使い、エージェントループとサンドボックスの運用をAnthropicに任せる。
  - KO: Claude Managed Agents를 사용해 agent loop와 sandbox 운영을 Anthropic에 맡깁니다.
  - EN: Use Claude Managed Agents, and leave the operation of the agent loop and sandbox to Anthropic.
- D. JA: Claude Code CLIを-pオプションで非対話実行し、自社のジョブスケジューラから定期的に起動する。
  - KO: Claude Code CLI를 -p 옵션으로 비대화형 실행하고, 자사 작업 스케줄러에서 정기적으로 실행합니다.
  - EN: Run the Claude Code CLI non-interactively with the -p option, and launch it periodically from the company's job scheduler.

## CCDV-F-Udemy2-0027

**JA** ある大学の研究支援エージェントでは、長時間にわたる調査タスクの途中で得た知見を、多くのステップにまたがって保持する必要があります。さらに、セッションを終えた後も、その知見を次回に引き継ぎたいと考えています。
エージェントのメモリパターンの説明として最も適切なものはどれですか。

**KO** 한 대학의 연구 지원 agent는 장시간에 걸친 조사 작업 도중 얻은 지식을 여러 단계에 걸쳐 유지해야 합니다. 또한 session이 끝난 뒤에도 그 지식을 다음 session으로 이어 가려고 합니다.
agent의 메모리 패턴에 대한 설명으로 가장 적절한 것은 무엇입니까?

- A. JA: 得た知見を会話履歴に積み上げ、次回のセッションでは同じ履歴を丸ごと再送して引き継ぐ。
  - KO: 얻은 지식을 대화 기록에 쌓아 두고, 다음 session에서는 같은 기록 전체를 다시 보내 이어 갑니다.
  - EN: Accumulate the insights in the conversation history, and carry them over by resending the same entire history in the next session.
- B. JA: 会話履歴をプロンプトキャッシングでキャッシュし、次回のセッションではキャッシュから知見を読み出す。
  - KO: 대화 기록을 prompt caching으로 캐시하고, 다음 session에서는 캐시에서 지식을 읽어 옵니다.
  - EN: Cache the conversation history with prompt caching, and read the insights from the cache in the next session.
- C. JA: 調査をサブエージェントに委任し、サブエージェントのコンテキストに知見を保持させて次回も参照させる。
  - KO: 조사를 subagent에 위임하고, subagent의 context에 지식을 유지시켜 다음에도 참조하게 합니다.
  - EN: Delegate the research to a subagent, have the subagent's context retain the insights, and have it reference them again next time.
- D. JA: 進行中の作業メモはコンテキスト内に置き、次回へ残す知見はファイル等の外部ストアに書き出す。
  - KO: 진행 중인 작업 메모는 context 안에 두고, 다음 session에 남길 지식은 파일 등 외부 저장소에 기록합니다.
  - EN: Keep in-progress working notes in the context, and write the insights to be carried over to an external store such as files.

## CCDV-F-Udemy2-0028

**JA** ある小売チェーンが、毎週同じ手順で在庫レポートを生成する処理を自動化したいと考えています。工程は常に一定で、次の順に進みます。
販売データを取得する
店舗別に集計する
Claudeで要約文を作る
所定のフォーマットに整形する
この処理に最も適したアプローチはどれですか。

**KO** 한 소매 체인이 매주 같은 절차로 재고 보고서를 생성하는 처리를 자동화하려고 합니다. 공정은 항상 같으며 다음 순서로 진행됩니다.
판매 데이터 가져오기
매장별 집계
Claude로 요약문 작성
정해진 형식으로 정리
이 처리에 가장 적합한 접근 방식은 무엇입니까?

- A. JA: 店舗の規模や業態ごとにデータを分類し、分類別に用意した要約プロンプトへ振り分ける。
  - KO: 매장 규모나 업태별로 데이터를 분류하고, 분류마다 준비한 요약 prompt로 보냅니다.
  - EN: Classify the data by store size and format, and route it to summarization prompts prepared for each category.
- B. JA: Claudeが毎週の販売データを見て、必要な集計と処理の順序をその都度判断しながら進める。
  - KO: Claude가 매주 판매 데이터를 보고, 필요한 집계와 처리 순서를 그때그때 판단하면서 진행합니다.
  - EN: Have Claude look at each week's sales data and proceed while deciding the necessary aggregations and processing order each time.
- C. JA: 各工程をコードで定めた固定の順序で呼び出し、前段の出力を次段へ渡して実行する。
  - KO: 각 공정을 코드로 정한 고정 순서로 호출하고, 앞 단계의 출력을 다음 단계로 넘겨 실행합니다.
  - EN: Call each step in a fixed order defined in code, passing the output of the previous step to the next.
- D. JA: 店舗ごとの要約を並列で生成し、評価役のLLMが採点して基準に届くまで書き直させる。
  - KO: 매장별 요약을 병렬로 생성하고, 평가 역할의 LLM이 채점해 기준에 도달할 때까지 다시 쓰게 합니다.
  - EN: Generate the per-store summaries in parallel, and have an evaluator LLM score them and have them rewritten until they meet the criteria.

## CCDV-F-Udemy2-0029

**JA** ある海運会社が、船荷証券や着荷通知からデータを抽出するClaudeアプリを構築しています。抽出結果は下流の基幹システムに直接投入されるため、決められたフィールドだけを持つJSONオブジェクトを、前置きや後書きの文章を付けずに返す必要があります。
出力フォーマットを最も確実に守らせるプロンプト設計はどれですか。

**KO** 한 해운 회사가 선하증권과 도착 통지서에서 데이터를 추출하는 Claude 앱을 구축하고 있습니다. 추출 결과는 후속 핵심 업무 시스템에 바로 투입되므로, 정해진 필드만 가진 JSON 객체를 앞뒤 설명 문장 없이 반환해야 합니다.
출력 형식을 가장 확실하게 지키게 하는 prompt 설계는 무엇입니까?

- A. JA: stop_sequencesに閉じ括弧を設定し、JSONを閉じた時点で出力の生成を打ち切らせる。
  - KO: stop_sequences에 닫는 괄호를 설정해, JSON이 닫히는 시점에 출력 생성을 끊게 합니다.
  - EN: Set a closing brace in stop_sequences so that output generation is cut off when the JSON closes.
- B. JA: 期待するJSONの構造と出力例を示し、前置きなしでJSONだけを返すよう肯定形で指示する。
  - KO: 기대하는 JSON 구조와 출력 예시를 보여 주고, 서두 없이 JSON만 반환하라고 긍정형으로 지시합니다.
  - EN: Show the expected JSON structure and an example output, and instruct in positive terms to return only JSON with no preamble.
- C. JA: 「前置きを書かないこと」「説明を付けないこと」など、避けるべき書き方を列挙して指示する。
  - KO: "서두를 쓰지 말 것", "설명을 붙이지 말 것" 등 피해야 할 작성 방식을 나열해 지시합니다.
  - EN: List the styles to avoid in the instructions, such as "Do not write a preamble" and "Do not add explanations."
- D. JA: max_tokensをJSONに必要な分まで小さく設定し、前後に文章を書く余地を残さない。
  - KO: max_tokens를 JSON에 필요한 만큼으로 작게 설정해, 앞뒤에 문장을 쓸 여지를 남기지 않습니다.
  - EN: Set max_tokens just large enough for the JSON, leaving no room for text before or after it.

## CCDV-F-Udemy2-0030

**JA** ある損害保険会社が、事故受付の一次対応を支援するClaudeアシスタントを企画しています。要件定義の場で、各部門から次の要件が出ました。
回答候補を2秒以内に表示すること（コールセンター部門）
すべての回答に約款の該当条文を引用して示すこと（コンプライアンス部門）
月額コストを現在の予算内に収めること（IT部門）
検証の結果、3つを同時に最大限満たすのは難しいと分かりました。
要件を確定させる進め方として最も適切なものはどれですか。

**KO** 한 손해보험사가 사고 접수의 1차 대응을 지원하는 Claude 어시스턴트를 기획하고 있습니다. 요구 사항 정의 자리에서 각 부서가 다음 요구 사항을 냈습니다.
답변 후보를 2초 이내에 표시할 것(콜센터 부서)
모든 답변에 약관의 해당 조항을 인용해 보여 줄 것(컴플라이언스 부서)
월 비용을 현재 예산 안으로 유지할 것(IT 부서)
검증 결과, 세 가지를 동시에 최대한 충족하기는 어렵다는 것을 알게 되었습니다.
요구 사항을 확정하는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: 最も役職の高い責任者がいる部門の要件を優先し、残りの要件は次期フェーズの検討事項として記録する。
  - KO: 직급이 가장 높은 책임자가 있는 부서의 요구 사항을 우선하고, 나머지 요구 사항은 다음 단계의 검토 사항으로 기록합니다.
  - EN: Prioritize the requirements of the department with the most senior executive, and record the remaining requirements as items for consideration in the next phase.
- B. JA: 部門横断の会議で優先順位は合意し、受け入れ基準は実装を進めながら開発チームが決めていく。
  - KO: 여러 부서가 참여하는 회의에서 우선순위는 합의하고, 인수 기준은 구현을 진행하면서 개발팀이 정해 나갑니다.
  - EN: Agree on priorities in a cross-departmental meeting, and let the development team decide the acceptance criteria as implementation proceeds.
- C. JA: 各要件の業務上の根拠とトレードオフを示し、ステークホルダーと優先順位と受け入れ基準を合意する。
  - KO: 각 요구 사항의 업무상 근거와 트레이드오프를 제시하고, 이해관계자와 우선순위 및 인수 기준을 합의합니다.
  - EN: Present the business rationale and trade-offs of each requirement, and agree with stakeholders on priorities and acceptance criteria.
- D. JA: 開発チームが技術的に実現しやすい要件から順に採用し、決まった内容を各部門へ結果として通知する。
  - KO: 개발팀이 기술적으로 구현하기 쉬운 요구 사항부터 차례로 채택하고, 정해진 내용을 각 부서에 결과로 통보합니다.
  - EN: Have the development team adopt requirements in order of technical ease, and notify each department of the decisions after the fact.

## CCDV-F-Udemy2-0031

**JA** ある銀行のリスク分析アプリでは、拡張思考を有効にしたモデルが、ツールを使いながら多段の推論を行います。
APIでの思考ブロックの扱いについて、正しい説明はどれですか。

**KO** 한 은행의 리스크 분석 앱에서는 extended thinking을 활성화한 모델이 도구를 사용하면서 다단계 추론을 합니다.
API에서 thinking 블록을 다루는 방법에 대한 올바른 설명은 무엇입니까?

- A. JA: 思考を有効にしたまま、tool_choiceで特定のツールを指定して毎回呼び出させる。
  - KO: thinking을 활성화한 채로 tool_choice로 특정 도구를 지정해 매번 호출하게 합니다.
  - EN: Keep thinking enabled while specifying a particular tool with tool_choice to force it to be called every time.
- B. JA: 思考のトークンを課金対象外として扱い、長い推論を含む応答もコスト見積もりから外す。
  - KO: thinking token은 과금 대상이 아닌 것으로 보고, 긴 추론이 포함된 응답도 비용 견적에서 제외합니다.
  - EN: Treat thinking tokens as non-billable, and exclude responses containing long reasoning from cost estimates.
- C. JA: ツール結果を返すとき、直前の思考ブロックを改変せずにtool_resultと一緒に送る。
  - KO: 도구 결과를 반환할 때 직전의 thinking 블록을 수정하지 않고 tool_result와 함께 보냅니다.
  - EN: When returning tool results, send the preceding thinking block unmodified along with the tool_result.
- D. JA: ツール結果を返すとき、直前の応答の思考ブロックは削除し、tool_resultだけを送る。
  - KO: 도구 결과를 반환할 때 직전 응답의 thinking 블록은 삭제하고 tool_result만 보냅니다.
  - EN: When returning tool results, delete the thinking block from the previous response and send only the tool_result.

## CCDV-F-Udemy2-0032

**JA** あるECサービスが、開発・ステージング・本番の3環境でClaude連携アプリを運用しています。
settings.jsonと環境変数（env）による構成管理で、環境ごとの設定を適切に分離する方針はどれですか。

**KO** 한 전자상거래 서비스가 개발·스테이징·프로덕션 3개 환경에서 Claude 연동 앱을 운영하고 있습니다.
settings.json과 환경 변수(env)로 구성을 관리할 때, 환경별 설정을 적절히 분리하는 방침은 무엇입니까?

- A. JA: 共有設定はsettings.jsonでコミットし、環境差分はenv、個人の上書きはsettings.local.jsonに置く。
  - KO: 공유 설정은 settings.json으로 commit하고, 환경별 차이는 env에, 개인용 덮어쓰기는 settings.local.json에 둡니다.
  - EN: Commit shared settings in settings.json, put environment-specific differences in env, and put personal overrides in settings.local.json.
- B. JA: エンドポイントやモデル名などの設定値をアプリのコードに定数として埋め込み、環境ごとに別々にビルドする。
  - KO: 엔드포인트나 모델 이름 같은 설정값을 앱 코드에 상수로 박아 넣고, 환경마다 따로 빌드합니다.
  - EN: Embed configuration values such as endpoints and model names as constants in the app code, and build separately for each environment.
- C. JA: APIキーを含む設定値を環境別のsettings.jsonファイルに分けて書き込み、3つのファイルともGitにコミットする。
  - KO: API 키를 포함한 설정값을 환경별 settings.json 파일로 나눠 적고, 세 파일 모두 Git에 commit합니다.
  - EN: Write configuration values, including API keys, into separate per-environment settings.json files, and commit all three files to Git.
- D. JA: 全環境で1つのsettings.jsonを共有してコミットし、本番固有の値は障害時に運用担当者が手で書き換える。
  - KO: 모든 환경에서 settings.json 하나를 공유해 commit하고, 프로덕션 고유의 값은 장애 시 운영 담당자가 직접 수정합니다.
  - EN: Share and commit a single settings.json across all environments, and have operators manually edit production-specific values when an incident occurs.

## CCDV-F-Udemy2-0033

**JA** ある電力会社が、大量の設備点検ログをClaudeに要約させています。max_tokensを大きく取った長い応答で、リクエストがときどきタイムアウトします。
長時間かかる応答のタイムアウト対策として最も適切なものはどれですか。

**KO** 한 전력 회사가 대량의 설비 점검 로그를 Claude로 요약하고 있습니다. max_tokens를 크게 잡은 긴 응답에서 요청이 가끔 timeout됩니다.
오래 걸리는 응답의 timeout 대책으로 가장 적절한 것은 무엇입니까?

- A. JA: 点検ログをFiles APIにアップロードし、リクエストにはfile_idだけを含めて送信する。
  - KO: 점검 로그를 Files API에 업로드하고, 요청에는 file_id만 포함해 보냅니다.
  - EN: Upload the inspection logs to the Files API and send the request containing only the file_id.
- B. JA: 非ストリーミングのまま、SDKのタイムアウトとmax_retriesを大きくして同じリクエストを再送させる。
  - KO: non-streaming을 유지한 채 SDK의 timeout과 max_retries를 늘려 같은 요청을 다시 보내게 합니다.
  - EN: Stay with non-streaming, increase the SDK timeout and max_retries, and have the same request resent.
- C. JA: stream: trueで応答をSSEとして逐次受け取り、接続を保ったまま長い生成を受信する。
  - KO: stream: true로 응답을 SSE로 순차 수신해, 연결을 유지한 채 긴 생성 결과를 받습니다.
  - EN: Use stream: true to receive the response incrementally as SSE, receiving the long generation while keeping the connection open.
- D. JA: 点検ログを共通の接頭辞としてプロンプトキャッシングでキャッシュし、リクエストの処理時間を短縮する。
  - KO: 점검 로그를 공통 prefix로 삼아 prompt caching으로 캐시하고, 요청 처리 시간을 줄입니다.
  - EN: Cache the inspection logs as a common prefix with prompt caching to shorten request processing time.

## CCDV-F-Udemy2-0034

**JA** あるオンライン旅行代理店（OTA）のアプリが、長い問い合わせスレッドと旅程データをまとめて、1回のリクエストでClaudeに渡しています。
コンテキストウィンドウを超えたときの挙動として、最も正確なものはどれですか。

**KO** 한 온라인 여행사(OTA)의 앱이 긴 문의 스레드와 여정 데이터를 묶어 한 번의 요청으로 Claude에 전달합니다.
context window를 넘었을 때의 동작으로 가장 정확한 것은 무엇입니까?

- A. JA: 入力単独で上限を超えると400エラーになり、入力とmax_tokensの合計超過なら生成が上限で止まる。
  - KO: 입력만으로 한도를 넘으면 400 오류가 되고, 입력과 max_tokens의 합계가 넘는 경우에는 생성이 한도에서 멈춥니다.
  - EN: If the input alone exceeds the limit, a 400 error is returned; if only the sum of the input and max_tokens exceeds it, generation stops at the limit.
- B. JA: 入力が上限を超えると、APIが古いメッセージから順に自動で削除し、残った履歴で応答を返す。
  - KO: 입력이 한도를 넘으면 API가 오래된 메시지부터 차례로 자동 삭제하고, 남은 기록으로 응답을 반환합니다.
  - EN: If the input exceeds the limit, the API automatically deletes messages starting from the oldest and responds using the remaining history.
- C. JA: 入力が上限を超えると、超過分が別のリクエストに自動で分割され、応答は後で結合されて返る。
  - KO: 입력이 한도를 넘으면 초과분이 별도 요청으로 자동 분할되고, 응답은 나중에 합쳐져 반환됩니다.
  - EN: If the input exceeds the limit, the excess is automatically split into a separate request, and the responses are combined and returned later.
- D. JA: max_tokensを大きく指定するとコンテキストウィンドウもその分だけ広がり、長い入力でも受け付けられる。
  - KO: max_tokens를 크게 지정하면 context window도 그만큼 넓어져 긴 입력도 받아들여집니다.
  - EN: Specifying a larger max_tokens expands the context window by the same amount, so long inputs are accepted.

## CCDV-F-Udemy2-0035

**JA** ある保険会社の開発チームが、Claude Codeで審査支援ツールを整備しています。定型作業は、独自のスラッシュコマンドとして用意したいと考えています。
組み込みコマンドとカスタムスキル（スラッシュコマンド）の関係の説明として最も適切なものはどれですか。

**KO** 한 보험사의 개발팀이 Claude Code로 심사 지원 도구를 정비하고 있습니다. 정형 작업은 자체 slash command로 마련하려고 합니다.
기본 제공 명령과 custom skill(slash command)의 관계에 대한 설명으로 가장 적절한 것은 무엇입니까?

- A. JA: カスタムスキルは~/.claude/skills/に置いたものが有効で、プロジェクトの.claude/skills/は読み込まれない。
  - KO: custom skill은 ~/.claude/skills/에 둔 것만 유효하며, 프로젝트의 .claude/skills/는 불러오지 않습니다.
  - EN: Only custom skills placed in ~/.claude/skills/ are active; the project's .claude/skills/ is not loaded.
- B. JA: /helpなどの組み込みコマンドとは別に、.claude/skills/＜名前＞/SKILL.mdで独自の/＜名前＞を追加できる。
  - KO: /help 같은 기본 제공 명령과 별도로, .claude/skills/＜이름＞/SKILL.md로 자체 /＜이름＞을 추가할 수 있습니다.
  - EN: Separately from built-in commands such as /help, you can add your own /<name> with .claude/skills/<name>/SKILL.md.
- C. JA: 独自のコマンドは.claude/commands/にしか置けず、.claude/skills/のSKILL.mdはClaudeの参照専用になる。
  - KO: 자체 명령은 .claude/commands/에만 둘 수 있으며, .claude/skills/의 SKILL.md는 Claude의 참조 전용이 됩니다.
  - EN: Custom commands can only be placed in .claude/commands/; SKILL.md files in .claude/skills/ are for Claude's reference only.
- D. JA: カスタムスキルはユーザーが/＜名前＞で起動したときだけ動き、descriptionによる自動読み込みは行われない。
  - KO: custom skill은 사용자가 /＜이름＞으로 실행했을 때만 동작하며, description에 따른 자동 로드는 이루어지지 않습니다.
  - EN: Custom skills run only when the user invokes them with /<name>; they are never loaded automatically based on their description.

## CCDV-F-Udemy2-0036

**JA** ある保険会社は、保険金請求書類を次の6段で処理するClaudeのパイプラインを運用しています。
OCRテキストの読み込み
項目抽出
契約照合
査定メモ生成
基幹システムへの登録
通知送信
ある夜間バッチで、1〜3段目が完了して結果を保存した後、4段目の査定メモ生成でHTTP 529 overloaded_errorが返り、処理が止まりました。
復旧戦略として最も適切なものはどれですか。

**KO** 한 보험사는 보험금 청구 서류를 다음 6단계로 처리하는 Claude pipeline을 운영하고 있습니다.
OCR 텍스트 읽기
항목 추출
계약 대조
사정 메모 생성
핵심 업무 시스템 등록
알림 발송
어느 야간 batch에서 1~3단계가 완료되어 결과를 저장한 뒤, 4단계인 사정 메모 생성에서 HTTP 529 overloaded_error가 반환되어 처리가 멈췄습니다.
복구 전략으로 가장 적절한 것은 무엇입니까?

- A. JA: 保存済みの1〜3段目の結果を再利用し、4段目からバックオフ付きで再試行して処理を再開する。
  - KO: 저장된 1~3단계 결과를 재사용하고, 4단계부터 backoff를 적용해 재시도하며 처리를 재개합니다.
  - EN: Reuse the saved results of stages 1–3 and resume processing by retrying from stage 4 with backoff.
- B. JA: 529を恒久的な障害とみなして当該ジョブを打ち切り、担当者に翌日の手動での再実行を依頼する。
  - KO: 529를 영구적인 장애로 보고 해당 작업을 중단한 뒤, 담당자에게 다음 날 수동 재실행을 요청합니다.
  - EN: Treat the 529 as a permanent failure, abort the job, and ask staff to rerun it manually the next day.
- C. JA: 529を入力の不備による失敗とみなし、4段目へ渡す内容を修正してから全段を最初から実行し直す。
  - KO: 529를 입력 결함으로 인한 실패로 보고, 4단계에 넘기는 내용을 수정한 뒤 전 단계를 처음부터 다시 실행합니다.
  - EN: Treat the 529 as a failure caused by invalid input, correct what is passed to stage 4, and then rerun all stages from the beginning.
- D. JA: パイプライン全体を最初から再実行し、1〜3段目の処理と結果の保存もあらためてやり直す。
  - KO: pipeline 전체를 처음부터 다시 실행하고, 1~3단계의 처리와 결과 저장도 새로 합니다.
  - EN: Rerun the entire pipeline from the beginning, redoing the processing of stages 1–3 and saving their results again.

## CCDV-F-Udemy2-0037

**JA** ある自治体が、住民からの問い合わせを受け付けるサービスを構築しています。Claudeはcategory・priority・needs_followupを持つJSONオブジェクトを返し、バックエンドがその値でルーティングします。
チームは構造化出力（json_schema）を有効にしていますが、シニアエンジニアは、それでもアプリ側で防御的なパースが必要だと主張しています。
最も適切な考え方と実装はどれですか。

**KO** 한 지자체가 주민 문의를 접수하는 서비스를 구축하고 있습니다. Claude는 category·priority·needs_followup을 가진 JSON 객체를 반환하고, 백엔드가 그 값으로 routing합니다.
팀은 structured outputs(json_schema)를 활성화했지만, 시니어 엔지니어는 그래도 앱 쪽에서 방어적 파싱이 필요하다고 주장합니다.
가장 적절한 사고방식과 구현은 무엇입니까?

- A. JA: 構造化出力を有効にしたうえで、アプリ側の検証処理は削除し、返った値をそのまま使う。
  - KO: structured outputs를 활성화한 상태에서 앱 쪽 검증 처리는 삭제하고, 반환된 값을 그대로 사용합니다.
  - EN: Enable structured outputs, remove the application-side validation, and use the returned values as-is.
- B. JA: stop_reasonを確認したうえで必須キーと型を検証し、検証に失敗した応答は人手の確認へ回す。
  - KO: stop_reason을 확인한 다음 필수 키와 타입을 검증하고, 검증에 실패한 응답은 사람이 확인하도록 넘깁니다.
  - EN: Check stop_reason, then validate the required keys and types, and route responses that fail validation to human review.
- C. JA: 出力の最後にClaude自身にJSONを見直させる指示を加え、それをアプリ側の検証の代わりとして使う。
  - KO: 출력 끝에 Claude 스스로 JSON을 다시 검토하라는 지시를 추가하고, 이를 앱 쪽 검증 대신 사용합니다.
  - EN: Add an instruction at the end of the output for Claude to review its own JSON, and use that in place of application-side validation.
- D. JA: JSONとしてパースできるまで同じリクエストを繰り返し再試行し、最初にパースできた結果をそのまま使う。
  - KO: JSON으로 파싱될 때까지 같은 요청을 계속 재시도하고, 처음 파싱된 결과를 그대로 사용합니다.
  - EN: Retry the same request repeatedly until the output parses as JSON, and use the first parseable result as-is.

## CCDV-F-Udemy2-0038

**JA** ある再生可能エネルギー事業者は、Claudeを使って風力タービンの保守ログを要約し、故障件数や停止時間などの数値を所見としてまとめています。技術者はその数値をもとに対応を判断しますが、ときどきClaudeが、元のログに存在しない数値を自信たっぷりに示すことがあります。
確信的だが誤った出力に備える設計として、最も効果的なものはどれですか。

**KO** 한 재생에너지 사업자는 Claude로 풍력 터빈의 유지보수 로그를 요약하고, 고장 건수나 정지 시간 같은 수치를 소견으로 정리하고 있습니다. 기술자는 그 수치를 바탕으로 대응을 판단하는데, Claude가 원래 로그에 없는 수치를 자신 있게 제시하는 경우가 가끔 있습니다.
확신에 차 있지만 틀린 출력에 대비하는 설계로 가장 효과적인 것은 무엇입니까?

- A. JA: 上位モデルに切り替え、モデルが高い確信度を示した数値をそのまま技術者向けの所見として採用する。
  - KO: 상위 모델로 바꾸고, 모델이 높은 확신도를 보인 수치를 그대로 기술자용 소견으로 채택합니다.
  - EN: Switch to a higher-tier model, and adopt the figures for which the model shows high confidence directly as findings for engineers.
- B. JA: システムプロンプトで断定的に答えるよう指示し、曖昧な言い回しや留保の表現を減らす。
  - KO: system prompt에서 단정적으로 답하라고 지시해, 모호한 표현이나 유보적인 표현을 줄입니다.
  - EN: Instruct Claude in the system prompt to answer assertively, reducing ambiguous wording and hedging.
- C. JA: ログの数値を逐語で抜き出させて根拠とし、不明時は「わからない」を許し、引用で主張を検証させる。
  - KO: 로그의 수치를 원문 그대로 추출하게 해 근거로 삼고, 불확실할 때는 "모르겠다"고 답하도록 허용하며, 인용으로 주장을 검증하게 합니다.
  - EN: Have Claude extract the figures from the logs verbatim as evidence, allow it to say "I don't know" when unsure, and have it verify its claims with quotes.
- D. JA: エフォートを高く設定して思考を深めさせ、各数値の算出過程をより丁寧に一つずつたどらせる。
  - KO: effort를 높게 설정해 사고를 깊게 하고, 각 수치의 산출 과정을 하나씩 더 꼼꼼하게 따라가게 합니다.
  - EN: Set effort high to deepen thinking, and have Claude trace how each figure was derived more carefully, one by one.

## CCDV-F-Udemy2-0039

**JA** ある気象サービスが、一般向けの荒天警報を発令するツールを持つClaudeエージェントを運用しています（警報は一般に配信されます）。誤発令の代償は大きいため、警報の草案作成と提案はClaudeにさせつつ、自律的に発令させることは避けたいと考えています。
human-in-the-loopの承認パターンとして正しい方法はどれですか。

**KO** 한 기상 서비스가 일반 대상의 악천후 경보를 발령하는 도구를 가진 Claude agent를 운영하고 있습니다(경보는 일반에 배포됩니다). 잘못 발령했을 때의 대가가 크므로, 경보 초안 작성과 제안은 Claude에게 맡기되 자율적으로 발령하게 하는 것은 피하려고 합니다.
human-in-the-loop 승인 패턴으로 올바른 방법은 무엇입니까?

- A. JA: tool_choiceで警報ツールをリクエストごとに指定し、Claudeに毎回警報ツールを呼び出させる。
  - KO: tool_choice로 경보 도구를 요청마다 지정해 Claude가 매번 경보 도구를 호출하게 합니다.
  - EN: Specify the warning tool with tool_choice on every request, so that Claude calls the warning tool every time.
- B. JA: 警報の配信処理をサーバー側ツールとして定義し、Anthropic側で承認と配信を実行させる。
  - KO: 경보 배포 처리를 server tool로 정의하고, Anthropic 쪽에서 승인과 배포를 실행하게 합니다.
  - EN: Define the warning distribution process as a server tool, and have Anthropic perform the approval and distribution.
- C. JA: システムプロンプトで、配信の前に利用者へ確認を求めるようClaudeに指示して守らせる。
  - KO: system prompt에서 배포 전에 이용자에게 확인을 구하라고 Claude에게 지시해 지키게 합니다.
  - EN: Instruct Claude in the system prompt to ask the user for confirmation before distribution, and have it comply.
- D. JA: 警報ツールのハンドラでは配信せずに提案を人の確認へ回し、承認後にアプリが配信を実行する。
  - KO: 경보 도구의 handler에서는 배포하지 않고 제안을 사람의 확인으로 넘기며, 승인 후에 앱이 배포를 실행합니다.
  - EN: In the warning tool's handler, route the proposal to human review instead of distributing it, and have the app distribute it after approval.

## CCDV-F-Udemy2-0040

**JA** あるソフトウェア保守会社が、Messages APIを使って顧客の設定ファイルをClaudeに修正させる機能を開発しています。この機能には、Anthropicがスキーマを定めたテキストエディタツール（text_editor_20250728）を採用しました。
このツールを組み込む際の理解として正しいものはどれですか。（2つ選択してください。）

**KO** 한 소프트웨어 유지보수 회사가 Messages API를 사용해 고객의 설정 파일을 Claude가 수정하는 기능을 개발하고 있습니다. 이 기능에는 Anthropic이 schema를 정한 text editor 도구(text_editor_20250728)를 채택했습니다.
이 도구를 통합할 때의 이해로 올바른 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: ファイルの閲覧や編集はAnthropicのインフラ上で実行され、結果は応答に直接含まれて返ってくる。
  - KO: 파일 열람과 편집은 Anthropic 인프라에서 실행되며, 결과는 응답에 직접 포함되어 돌아옵니다.
  - EN: Viewing and editing of files are executed on Anthropic's infrastructure, and the results are returned directly in the response.
- B. JA: viewやstr_replaceなどのコマンドはアプリ側で実行し、その結果をtool_resultとして返す。
  - KO: view나 str_replace 같은 명령은 앱 쪽에서 실행하고, 그 결과를 tool_result로 반환합니다.
  - EN: Commands such as view and str_replace are executed by the application, and the results are returned as tool_result.
- C. JA: 編集対象のファイルは事前にFiles APIへアップロードし、そのfile_idをツールに渡して編集させる。
  - KO: 편집할 파일은 미리 Files API에 업로드하고, 그 file_id를 도구에 전달해 편집하게 합니다.
  - EN: Upload the files to be edited to the Files API in advance, and pass their file_id to the tool to have them edited.
- D. JA: ツール定義にはtypeとnameを指定すればよく、input_schemaを自分で記述する必要はない。
  - KO: 도구 정의에는 type과 name만 지정하면 되며, input_schema를 직접 작성할 필요는 없습니다.
  - EN: The tool definition only needs type and name; you do not need to write input_schema yourself.
- E. JA: 自社の用途に合わせて、input_schemaにコマンドや引数を追加してツールの挙動を拡張する。
  - KO: 자사 용도에 맞게 input_schema에 명령이나 인수를 추가해 도구의 동작을 확장합니다.
  - EN: Extend the tool's behavior by adding commands and arguments to input_schema to suit your own use case.

## CCDV-F-Udemy2-0041

**JA** ある不動産ポータルが、Messages APIの上に自前のエージェントループを実装しています。web searchのサーバー側ツールを有効にして、物件周辺の再開発計画や交通機関の最新情報をClaudeに調べさせています。
調べる範囲が広い依頼では、応答のstop_reasonがpause_turnとなり、回答が途中で止まってしまいます。
ハーネスの対処として最も適切なものはどれですか。

**KO** 한 부동산 포털이 Messages API 위에 자체 agent loop를 구현했습니다. web search server tool을 활성화해 매물 주변의 재개발 계획과 교통편 최신 정보를 Claude가 조사하게 하고 있습니다.
조사 범위가 넓은 요청에서는 응답의 stop_reason이 pause_turn이 되어 답변이 도중에 멈춥니다.
harness의 대처로 가장 적절한 것은 무엇입니까?

- A. JA: server_tool_useブロックごとにtool_resultを作成し、次のユーザーメッセージとして返して処理を続けさせる。
  - KO: server_tool_use 블록마다 tool_result를 만들고, 다음 user 메시지로 반환해 처리를 계속하게 합니다.
  - EN: Create a tool_result for each server_tool_use block and return them as the next user message to continue processing.
- B. JA: pause_turnを一時的なエラーとして扱い、ジッター付きの指数バックオフで同じリクエストを再試行する。
  - KO: pause_turn을 일시적인 오류로 보고, jitter를 넣은 exponential backoff로 같은 요청을 재시도합니다.
  - EN: Treat pause_turn as a transient error and retry the same request with exponential backoff with jitter.
- C. JA: 返されたアシスタントの応答をそのまま会話に追加し、同じツール定義で再度リクエストして続きを生成させる。
  - KO: 반환된 assistant 응답을 그대로 대화에 추가하고, 같은 도구 정의로 다시 요청해 이어지는 내용을 생성하게 합니다.
  - EN: Append the returned assistant response to the conversation as-is, and send the request again with the same tool definitions to generate the continuation.
- D. JA: max_tokensを引き上げたうえで同じリクエストを最初から送り直し、1回の応答で調査を完了させる。
  - KO: max_tokens를 올린 다음 같은 요청을 처음부터 다시 보내, 한 번의 응답으로 조사를 끝내게 합니다.
  - EN: Raise max_tokens and resend the same request from the beginning so that the research completes in a single response.

## CCDV-F-Udemy2-0042

**JA** ある人材紹介SaaSが、提携先の応募者追跡システム（ATS）から新規応募のwebhookを受信し、イベントごとにClaudeで職務経歴書をスクリーニングしています。
イベント駆動のwebhook受信エンドポイントの基本的な設計として最も適切なものはどれですか。

**KO** 한 인재 소개 SaaS가 제휴사의 지원자 추적 시스템(ATS)에서 신규 지원 webhook을 받아, 이벤트마다 Claude로 경력 기술서를 스크리닝하고 있습니다.
이벤트 기반 webhook 수신 엔드포인트의 기본 설계로 가장 적절한 것은 무엇입니까?

- A. JA: 受信後すぐに2xxを返してキューで非同期に処理し、署名を検証してイベントIDで重複を除く。
  - KO: 수신 즉시 2xx를 반환하고 큐에서 비동기로 처리하며, 서명을 검증하고 이벤트 ID로 중복을 제거합니다.
  - EN: Return 2xx immediately on receipt and process asynchronously via a queue, verifying the signature and deduplicating by event ID.
- B. JA: リクエストの署名は検証するが、再送されたイベントも毎回新しい応募としてスクリーニングする。
  - KO: 요청 서명은 검증하지만, 재전송된 이벤트도 매번 새 지원으로 보고 스크리닝합니다.
  - EN: Verify the request signature, but screen redelivered events as new applications every time.
- C. JA: 受信後すぐに2xxを返してキューで処理し、送信元の確認はIPアドレスの許可リストで済ませる。
  - KO: 수신 즉시 2xx를 반환하고 큐에서 처리하며, 발신자 확인은 IP 주소 허용 목록으로 끝냅니다.
  - EN: Return 2xx immediately on receipt and process via a queue, relying on an IP address allowlist alone to verify the sender.
- D. JA: webhookのハンドラ内でClaudeを同期で呼び出し、スクリーニングの結果をレスポンス本文で返す。
  - KO: webhook handler 안에서 Claude를 동기로 호출하고, 스크리닝 결과를 응답 본문으로 반환합니다.
  - EN: Call Claude synchronously within the webhook handler and return the screening result in the response body.

## CCDV-F-Udemy2-0043

**JA** ある病院が、Claude Agent SDKで患者記録を読み取るエージェントを構築しています。このエージェントには記録の閲覧だけを許可し、ファイルの変更や削除は一切できないようにしたいと考えています。
最も適切な権限の絞り方はどれですか。

**KO** 한 병원이 Claude Agent SDK로 환자 기록을 읽는 agent를 구축하고 있습니다. 이 agent에는 기록 열람만 허용하고, 파일 변경이나 삭제는 전혀 할 수 없게 하려고 합니다.
권한을 제한하는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: システムプロンプトに「ファイルを変更・削除しないこと」と書き、作業方針として守らせる。
  - KO: system prompt에 "파일을 변경·삭제하지 말 것"이라고 적어, 작업 방침으로 지키게 합니다.
  - EN: Write "Do not modify or delete files" in the system prompt and have the agent follow it as a working policy.
- B. JA: 読み取り系のツールをallowed_toolsで許可し、書き込み系はdisallowed_toolsで除外する。
  - KO: 읽기 계열 도구는 allowed_tools로 허용하고, 쓰기 계열은 disallowed_tools로 제외합니다.
  - EN: Allow read-only tools with allowed_tools and exclude write tools with disallowed_tools.
- C. JA: 全ツールをallowed_toolsで許可し、PostToolUseフックで各ツールの実行内容を記録して事後に監査する。
  - KO: 모든 도구를 allowed_tools로 허용하고, PostToolUse hook으로 각 도구의 실행 내용을 기록해 사후에 감사합니다.
  - EN: Allow all tools with allowed_tools, and log each tool's execution with a PostToolUse hook for after-the-fact auditing.
- D. JA: permission_modeをacceptEditsに設定して編集の承認を自動化し、変更内容を作業ログに残す。
  - KO: permission_mode를 acceptEdits로 설정해 편집 승인을 자동화하고, 변경 내용을 작업 로그에 남깁니다.
  - EN: Set permission_mode to acceptEdits to auto-approve edits, and record the changes in a work log.

## CCDV-F-Udemy2-0044

**JA** ある自動車メーカーが、生産スケジューリングAPIに問い合わせ、部品データベースを読み取るClaudeエージェントを本番導入しようとしています。セキュリティ部門は、セキュアバイデザインを求めています。
最小権限とIAMの観点で最も適切な方針はどれですか。

**KO** 한 자동차 제조사가 생산 스케줄링 API를 조회하고 부품 데이터베이스를 읽는 Claude agent를 프로덕션에 도입하려고 합니다. 보안 부서는 secure by design을 요구하고 있습니다.
최소 권한과 IAM 관점에서 가장 적절한 방침은 무엇입니까?

- A. JA: 組織の管理者権限を持つAdmin APIキーをエージェントに渡し、どのAPIも権限エラーなく呼べる状態にする。
  - KO: 조직 관리자 권한을 가진 Admin API 키를 agent에 넘겨, 어떤 API든 권한 오류 없이 호출할 수 있게 합니다.
  - EN: Give the agent an Admin API key with organization administrator privileges so that it can call any API without permission errors.
- B. JA: システムプロンプトでアクセスしてよいリソースを指示し、タスク外のリソースに触れさせない。
  - KO: system prompt에서 접근해도 되는 리소스를 지시해, 작업과 무관한 리소스에 손대지 않게 합니다.
  - EN: Specify the resources it may access in the system prompt so that it does not touch resources outside the task.
- C. JA: 開発・ステージング・本番で1本のAPIキーを共有し、ローテーションを1か所で済ませる。
  - KO: 개발·스테이징·프로덕션에서 API 키 하나를 공유해, 키 교체(rotation)를 한곳에서 끝냅니다.
  - EN: Share a single API key across development, staging, and production so that rotation is done in one place.
- D. JA: エージェント用のキーを必要な範囲に絞り、ワークスペースで環境を分け、キーの利用状況を監査する。
  - KO: agent용 키를 필요한 범위로 좁히고, workspace로 환경을 분리하며, 키 사용 현황을 감사합니다.
  - EN: Scope the agent's key to only what is needed, separate environments with workspaces, and audit key usage.

## CCDV-F-Udemy2-0045

**JA** あるコンサルティング会社が、レポート生成に使うプロンプトを継続的に改善しています。新しいプロンプトに変えると、出力品質が下がることがあります。その場合は、すぐに元へ戻したいと考えています。
プロンプトのバージョン管理とロールバックの方針として最も適切なものはどれですか。

**KO** 한 컨설팅 회사가 보고서 생성에 쓰는 prompt를 지속적으로 개선하고 있습니다. 새 prompt로 바꾸면 출력 품질이 떨어지는 경우가 있는데, 그럴 때는 즉시 원래대로 되돌리려고 합니다.
prompt 버전 관리와 롤백 방침으로 가장 적절한 것은 무엇입니까?

- A. JA: プロンプトは本番環境の設定画面で直接編集し、変更前の内容は編集者が手元のメモに残しておく。
  - KO: prompt는 프로덕션 환경의 설정 화면에서 직접 편집하고, 변경 전 내용은 편집자가 개인 메모로 남겨 둡니다.
  - EN: Edit prompts directly in the production settings screen, and have the editor keep the previous content in personal notes.
- B. JA: プロンプトをバージョン管理して本番のバージョンを固定し、劣化時は良好だったバージョンへ戻す。
  - KO: prompt를 버전 관리하고 프로덕션 버전을 고정해 두며, 품질이 떨어지면 성능이 좋았던 버전으로 되돌립니다.
  - EN: Version-control the prompts and pin the production version, and when quality degrades, roll back to a version that performed well.
- C. JA: 品質が下がったときは、評価結果を見ながらプロンプトをその場で書き直して本番に反映する。
  - KO: 품질이 떨어지면 평가 결과를 보면서 prompt를 그 자리에서 다시 써 프로덕션에 반영합니다.
  - EN: When quality drops, rewrite the prompt on the spot while looking at the evaluation results and push it to production.
- D. JA: プロンプトは実行のたびにClaudeに自動生成させ、生成結果の良かったものを採用していく。
  - KO: prompt는 실행할 때마다 Claude가 자동 생성하게 하고, 생성 결과가 좋았던 것을 채택해 나갑니다.
  - EN: Have Claude automatically generate the prompt on every run, and adopt the ones that produced good results.

## CCDV-F-Udemy2-0046

**JA** ある調査会社が、Claude Agent SDKで動くリサーチエージェントをコンテナ上で運用しています。エージェントは外部のWebページを取得して要約するほか、社内の顧客資料も読み取れます。
取得したページに埋め込まれた隠し指示による注入が成功した場合でも、社内データが任意の外部サーバーへ送信されることを、仕組みとして防ぎたいと考えています。
最も適切な対策はどれですか。

**KO** 한 조사 회사가 Claude Agent SDK로 동작하는 리서치 agent를 컨테이너에서 운영하고 있습니다. 이 agent는 외부 웹 페이지를 가져와 요약할 뿐 아니라 사내 고객 자료도 읽을 수 있습니다.
가져온 페이지에 숨겨진 지시를 통한 injection이 성공하더라도, 사내 데이터가 임의의 외부 서버로 전송되는 것을 구조적으로 막으려고 합니다.
가장 적절한 대책은 무엇입니까?

- A. JA: PostToolUseフックで各ツールの実行内容を記録し、外部への送信の痕跡がないか定期的に監査する。
  - KO: PostToolUse hook으로 각 도구의 실행 내용을 기록하고, 외부 전송 흔적이 없는지 정기적으로 감사합니다.
  - EN: Log each tool's execution with a PostToolUse hook and periodically audit for traces of outbound transmission.
- B. JA: コンテナのネットワークを遮断し、許可したドメインだけに中継するプロキシ経由でのみ外部へ接続させる。
  - KO: 컨테이너의 네트워크를 차단하고, 허용한 도메인으로만 중계하는 proxy를 통해서만 외부에 연결하게 합니다.
  - EN: Cut off the container's network and allow external connections only through a proxy that relays to allowed domains.
- C. JA: システムプロンプトで外部へのデータ送信を禁止し、取得したページは信頼できないデータとして扱うよう指示する。
  - KO: system prompt에서 외부로의 데이터 전송을 금지하고, 가져온 페이지는 신뢰할 수 없는 데이터로 다루라고 지시합니다.
  - EN: Prohibit sending data externally in the system prompt, and instruct the agent to treat fetched pages as untrusted data.
- D. JA: 取得したページを軽量モデルで事前に審査し、注入の疑いがある内容をエージェントに渡す前に除外する。
  - KO: 가져온 페이지를 경량 모델로 사전 심사해, injection이 의심되는 내용을 agent에 넘기기 전에 제외합니다.
  - EN: Pre-screen fetched pages with a lightweight model and remove content suspected of injection before passing it to the agent.

## CCDV-F-Udemy2-0047

**JA** ある会計事務所が、複数の帳簿を横断する長時間の照合タスクを、Claudeエージェントで実行しています。しかし、会話がコンテキストウィンドウの上限に近づくと、作業を続けられなくなります。
長時間のタスクを継続させるコンテキスト管理の方針として最も適切なものはどれですか。

**KO** 한 회계 사무소가 여러 장부를 가로지르는 장시간 대조 작업을 Claude agent로 실행하고 있습니다. 그런데 대화가 context window 한도에 가까워지면 작업을 계속할 수 없게 됩니다.
장시간 작업을 이어 가기 위한 context 관리 방침으로 가장 적절한 것은 무엇입니까?

- A. JA: 会話履歴をプロンプトキャッシングの対象にし、キャッシュ済みの部分を上限の計算から外して続ける。
  - KO: 대화 기록을 prompt caching 대상으로 삼고, 캐시된 부분을 한도 계산에서 빼고 계속합니다.
  - EN: Make the conversation history a target of prompt caching, and continue by excluding the cached portion from the limit calculation.
- B. JA: サーバー側で古いやり取りを要約に置き換え、上限を超えて作業を続ける。
  - KO: 서버 쪽에서 오래된 대화를 요약으로 바꿔, 한도를 넘어서도 작업을 계속합니다.
  - EN: Replace older exchanges with a summary on the server side and continue working beyond the limit.
- C. JA: トークンカウントAPIで入力を見積もり、上限に近づいた時点で新しい会話を最初から始め直す。
  - KO: token counting API로 입력을 추정하고, 한도에 가까워지면 새 대화를 처음부터 다시 시작합니다.
  - EN: Estimate the input with the token counting API, and start a new conversation from scratch when the limit is approached.
- D. JA: 1Mトークンのコンテキストウィンドウを持つモデルへ切り替え、全履歴を保持したまま作業を続ける。
  - KO: 1M token context window를 가진 모델로 바꾸고, 전체 기록을 유지한 채 작업을 계속합니다.
  - EN: Switch to a model with a 1M-token context window and continue working while retaining the full history.

## CCDV-F-Udemy2-0048

**JA** ある化学メーカーのアプリでは、安全データシートの項目を、Claudeと社内システムの間で構造化データとしてやり取りします。
境界をまたぐ入出力スキーマを「契約」として設計する方針として最も適切なものはどれですか。

**KO** 한 화학 제조사의 앱은 안전 데이터 시트의 항목을 Claude와 사내 시스템 사이에서 구조화 데이터로 주고받습니다.
경계를 넘나드는 입출력 schema를 "계약"으로 설계하는 방침으로 가장 적절한 것은 무엇입니까?

- A. JA: フィールド名の一覧だけをプロンプトで示し、型や必須の判断は受け取り側の実装ごとに任せる。
  - KO: 필드 이름 목록만 prompt로 보여 주고, 타입이나 필수 여부 판단은 받는 쪽 구현마다 맡깁니다.
  - EN: Show only a list of field names in the prompt, and leave decisions about types and required fields to each receiving implementation.
- B. JA: 各フィールドの型と必須かどうかを定義したJSON Schemaを契約とし、出力と入力をその定義で検証する。
  - KO: 각 필드의 타입과 필수 여부를 정의한 JSON Schema를 계약으로 삼고, 출력과 입력을 그 정의로 검증합니다.
  - EN: Use a JSON Schema that defines each field's type and whether it is required as the contract, and validate outputs and inputs against that definition.
- C. JA: Claudeには自由文で所見を書かせ、受け取り側で正規表現により項目を抜き出して社内システムに登録する。
  - KO: Claude에게는 자유 텍스트로 소견을 쓰게 하고, 받는 쪽에서 정규 표현식으로 항목을 추출해 사내 시스템에 등록합니다.
  - EN: Have Claude write findings in free text, and have the receiver extract the fields with regular expressions and register them in the internal systems.
- D. JA: 要件が変わるたびにスキーマ検証を外して暫定運用し、仕様が落ち着いてからスキーマを作り直す。
  - KO: 요구 사항이 바뀔 때마다 schema 검증을 빼고 임시로 운영하며, 사양이 안정되면 schema를 다시 만듭니다.
  - EN: Remove schema validation and operate provisionally whenever requirements change, and rebuild the schema once the specification settles.

## CCDV-F-Udemy2-0049

**JA** ある物流会社は、Claude SDKを含む複数のnpmパッケージに依存するNode.jsサービスを毎月リリースしています。package.jsonでは、依存を^付きの範囲で指定しています。
障害を調査したところ、ステージングで回帰評価に合格したビルドと、その後に本番向けに作り直したビルドとで、一部の依存パッケージのバージョンが食い違っていたことが分かりました。
環境をまたいで同じ依存ツリーを再現する方法として最も適切なものはどれですか。

**KO** 한 물류 회사는 Claude SDK를 포함한 여러 npm 패키지에 의존하는 Node.js 서비스를 매월 릴리스합니다. package.json에서는 의존성을 ^가 붙은 범위로 지정하고 있습니다.
장애를 조사한 결과, 스테이징에서 회귀 평가를 통과한 빌드와 그 뒤 프로덕션용으로 다시 만든 빌드 사이에 일부 의존 패키지의 버전이 서로 달랐다는 것이 밝혀졌습니다.
환경이 달라도 같은 의존성 트리를 재현하는 방법으로 가장 적절한 것은 무엇입니까?

- A. JA: package.jsonの範囲指定を^から~に変え、各ビルドではnpm installで最新のパッチ版を取り込んで揃える。
  - KO: package.json의 범위 지정을 ^에서 ~로 바꾸고, 각 빌드에서 npm install로 최신 패치 버전을 받아 맞춥니다.
  - EN: Change the range specifiers in package.json from ^ to ~, and align versions by pulling in the latest patch versions with npm install in each build.
- B. JA: package-lock.jsonを.gitignoreに加え、各環境のnpm installでその環境専用のロックファイルを生成させる。
  - KO: package-lock.json을 .gitignore에 추가하고, 각 환경의 npm install이 그 환경 전용 lock 파일을 생성하게 합니다.
  - EN: Add package-lock.json to .gitignore, and have npm install in each environment generate a lockfile specific to that environment.
- C. JA: 各ビルドの前にnode_modulesを削除してからnpm installを実行し、依存をクリーンな状態で解決し直す。
  - KO: 각 빌드 전에 node_modules를 삭제한 다음 npm install을 실행해, 깨끗한 상태에서 의존성을 다시 해석합니다.
  - EN: Delete node_modules before each build and then run npm install to re-resolve dependencies from a clean state.
- D. JA: package-lock.jsonをリポジトリにコミットし、ステージングと本番のビルドはnpm ciで依存をインストールする。
  - KO: package-lock.json을 저장소에 commit하고, 스테이징과 프로덕션 빌드에서는 npm ci로 의존성을 설치합니다.
  - EN: Commit package-lock.json to the repository, and install dependencies with npm ci for the staging and production builds.

## CCDV-F-Udemy2-0050

**JA** あるセキュリティ運用センター（SOC）が、大量のアラートを毎晩まとめてClaudeで分類しています。緊急性は低く、共通の分類ガイドライン（長い固定プロンプト）をすべてのリクエストで再利用します。
コストモデリングとして最も適切なものはどれですか。

**KO** 한 보안 관제 센터(SOC)가 대량의 경보를 매일 밤 일괄로 Claude로 분류하고 있습니다. 긴급성은 낮으며, 공통 분류 가이드라인(긴 고정 prompt)을 모든 요청에서 재사용합니다.
비용 모델링으로 가장 적절한 것은 무엇입니까?

- A. JA: 固定のガイドラインをプロンプトキャッシングでキャッシュし、Batches APIの割引も重ねてコストを見積もる。
  - KO: 고정 가이드라인을 prompt caching으로 캐시하고, Batches API 할인도 겹쳐 적용해 비용을 추정합니다.
  - EN: Cache the fixed guideline with prompt caching, and estimate costs with the Message Batches API discount stacked on top.
- B. JA: プロンプトキャッシングは使わず、入力トークンを基本入力単価のまま計算してコストを見積もる。
  - KO: prompt caching은 쓰지 않고, 입력 token을 기본 입력 단가 그대로 계산해 비용을 추정합니다.
  - EN: Do not use prompt caching, and estimate costs by calculating input tokens at the base input price.
- C. JA: 入力トークン数に入力単価を掛けて見積もり、件数の少ない出力トークンは計算から外す。
  - KO: 입력 token 수에 입력 단가를 곱해 추정하고, 양이 적은 출력 token은 계산에서 뺍니다.
  - EN: Estimate by multiplying the number of input tokens by the input price, and exclude output tokens from the calculation because they are fewer.
- D. JA: バッチAPIとプロンプトキャッシングは二者択一とみなし、割引率の大きいバッチAPIの割引で見積もる。
  - KO: batch API와 prompt caching은 둘 중 하나만 쓸 수 있다고 보고, 할인율이 큰 batch API 할인으로 추정합니다.
  - EN: Treat the Message Batches API and prompt caching as mutually exclusive, and estimate using the Message Batches API discount, which has the larger discount rate.

## CCDV-F-Udemy2-0051

**JA** あるEdTech企業が、Claudeベースのサービスで扱うAPIキーやシークレットの管理を強化しています。
シークレット管理のベストプラクティスとして正しいものはどれですか。（2つ選択してください。）

**KO** 한 EdTech 기업이 Claude 기반 서비스에서 다루는 API 키와 시크릿 관리를 강화하고 있습니다.
시크릿 관리의 모범 사례로 옳은 것은 무엇입니까? (2개를 선택하십시오.)

- A. JA: シークレットは実行時に環境変数やシークレットマネージャから注入し、ソース管理には置かない。
  - KO: 시크릿은 실행 시점에 환경 변수나 시크릿 매니저에서 주입하고, 소스 관리에는 두지 않습니다.
  - EN: Inject secrets at runtime from environment variables or a secrets manager, and do not keep them in source control.
- B. JA: キーの権限を必要最小限に絞り、有効期限を設けて定期的にローテーションする。
  - KO: 키의 권한을 필요한 최소한으로 좁히고, 유효 기간을 두어 정기적으로 교체(rotation)합니다.
  - EN: Scope key permissions to the minimum necessary, set expiration dates, and rotate them regularly.
- C. JA: 全環境と全チームで1本の長期キーを共有し、発行と管理の手間をまとめる。
  - KO: 모든 환경과 모든 팀이 장기 키 하나를 공유해 발급과 관리의 수고를 줄입니다.
  - EN: Share a single long-lived key across all environments and teams to consolidate the effort of issuing and managing keys.
- D. JA: APIキーを設定ファイルに書き込み、アプリのコードと一緒にリポジトリへコミットする。
  - KO: API 키를 설정 파일에 적고, 앱 코드와 함께 저장소에 commit합니다.
  - EN: Write API keys into configuration files and commit them to the repository along with the app code.
- E. JA: モバイルアプリの中にAPIキーを埋め込み、バックエンドを経由せずに端末から直接Claude APIを呼ぶ。
  - KO: 모바일 앱 안에 API 키를 심어 두고, 백엔드를 거치지 않고 단말기에서 직접 Claude API를 호출합니다.
  - EN: Embed the API key in the mobile app and call the Claude API directly from the device without going through a backend.

## CCDV-F-Udemy2-0052

**JA** ある非営利団体の開発チームが、Claudeを使ってコード変更を生成し、既存のソフトウェア開発プロセスに組み込もうとしています。
ブランチ戦略と、AI生成コードのレビューの進め方として最も適切なものはどれですか。

**KO** 한 비영리 단체의 개발팀이 Claude로 코드 변경을 생성해 기존 소프트웨어 개발 프로세스에 통합하려고 합니다.
브랜치 전략과 AI 생성 코드의 리뷰 방식으로 가장 적절한 것은 무엇입니까?

- A. JA: AI生成の変更はmainブランチに直接コミットし、月末にまとめてコードレビューを実施する。
  - KO: AI가 생성한 변경은 main 브랜치에 직접 commit하고, 월말에 한꺼번에 코드 리뷰를 실시합니다.
  - EN: Commit AI-generated changes directly to the main branch and conduct code reviews in bulk at the end of the month.
- B. JA: AI生成の変更もフィーチャーブランチでプルリクエストにし、人のレビューとCIを経てマージする。
  - KO: AI가 생성한 변경도 feature 브랜치에서 pull request로 만들고, 사람의 리뷰와 CI를 거쳐 머지합니다.
  - EN: Put AI-generated changes into pull requests from feature branches as well, and merge them after human review and CI.
- C. JA: AI生成の変更は専用のリポジトリで管理し、本体とは別の成果物としてリリースする。
  - KO: AI가 생성한 변경은 전용 저장소에서 관리하고, 본체와 별개의 산출물로 릴리스합니다.
  - EN: Manage AI-generated changes in a dedicated repository and release them as an artifact separate from the main codebase.
- D. JA: AI生成の変更はClaudeによる自動レビューを通過したものを、人のレビューなしでマージする。
  - KO: AI가 생성한 변경 중 Claude의 자동 리뷰를 통과한 것은 사람의 리뷰 없이 머지합니다.
  - EN: Merge AI-generated changes that pass an automated review by Claude without human review.

## CCDV-F-Udemy2-0053

**JA** ある小売企業が、在庫照会と需要予測の集計ツールを提供する社内MCPサーバーを、Streamable HTTPで公開しています。利用の増加に合わせて、複数のサーバーインスタンスをロードバランサの背後に並べ、スケールアウトしたいと考えています。
集計ツールの中には、完了までに数分かかり、途中経過を後から問い合わせるものもあります。
2026-07-28版のMCP仕様に沿ったサーバー設計として最も適切なものはどれですか。

**KO** 한 소매 기업이 재고 조회와 수요 예측 집계 도구를 제공하는 사내 MCP server를 Streamable HTTP로 공개하고 있습니다. 이용이 늘어남에 따라 여러 server 인스턴스를 로드 밸런서 뒤에 배치해 scale-out하려고 합니다.
집계 도구 중에는 완료까지 몇 분이 걸리고, 진행 상황을 나중에 조회하는 것도 있습니다.
2026-07-28판 MCP 사양에 맞는 server 설계로 가장 적절한 것은 무엇입니까?

- A. JA: 各要求は_metaに含まれる情報だけで処理し、要求をまたぐ集計ジョブは明示的なIDで共有ストアから参照する。
  - KO: 각 요청은 _meta에 담긴 정보만으로 처리하고, 요청을 넘나드는 집계 작업은 명시적인 ID로 공유 저장소에서 참조합니다.
  - EN: Process each request using only the information contained in its _meta, and reference aggregation jobs that span requests from a shared store using explicit IDs.
- B. JA: ロードバランサでスティッキーセッションを有効にし、同じクライアントの要求を常に同じインスタンスへ送る。
  - KO: 로드 밸런서에서 sticky session을 활성화해, 같은 client의 요청을 항상 같은 인스턴스로 보냅니다.
  - EN: Enable sticky sessions on the load balancer so that requests from the same client are always sent to the same instance.
- C. JA: 最初の要求で受け取ったクライアントの情報と能力をインスタンスのメモリに保持し、以後の要求で使い回す。
  - KO: 첫 요청에서 받은 client 정보와 capability를 인스턴스 메모리에 보관하고, 이후 요청에서 재사용합니다.
  - EN: Store the client information and capabilities received in the first request in the instance's memory and reuse them for subsequent requests.
- D. JA: 接続ごとに会話セッションを割り当て、接続が切れた時点でその接続に属するジョブの状態を破棄する。
  - KO: 연결마다 대화 session을 할당하고, 연결이 끊기면 그 연결에 속한 작업의 상태를 폐기합니다.
  - EN: Assign a conversation session to each connection, and discard the state of the jobs belonging to that connection when it disconnects.
