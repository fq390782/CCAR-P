# 2. Applications and Integration — 반드시 알아야 할 지식
> 시험 비중 33% · 약 10문항 · 근거 문항 65개

## 1. 핵심 개념

### 1.1 Messages API 기본 구조
- Messages API는 stateless입니다. 서버에 대화 상태가 남지 않으므로 매 요청마다 user/assistant가 번갈아 나오는 `messages` 배열 전체(대화 이력)를 다시 보냅니다. session ID나 conversation token 같은 것은 없습니다. [Patrick-0015][Preporato-0001][Udemy-0030]
- 첫 메시지는 user여야 합니다. 이력이 길어질수록 입력 토큰(비용)이 늘어나고, 다시 보내는 비용은 prompt caching으로 줄입니다. [Patrick-0015]
- system prompt는 `messages` 안에 `"role": "system"`으로 넣지 않습니다. 최상위 `system` 파라미터로 보냅니다. `messages`에 넣으면 오류가 납니다. assistant 턴에 넣거나 매 user 턴에 반복하는 우회책은 지시를 약하게 만들고 토큰을 낭비합니다. [Patrick-0001][Patrick-0040]
- context window에는 system prompt, `messages`의 모든 메시지(tool result와 이미지 포함), tool 정의, 그 턴의 출력(thinking 포함)이 모두 계산됩니다. `max_tokens`는 출력 길이 상한일 뿐 window 크기와는 다른 개념입니다. [Udemy-0030][Udemy-0001]
- 실제 토큰 사용량은 응답의 `usage`(`input_tokens`, `output_tokens`)로 확인합니다. [Udemy-0030]
- 요청이 window에 들어가는지와 비용이 얼마인지는 token counting endpoint에 실제 요청(system, tools, messages)을 그대로 넣어 측정합니다. "4글자 = 1토큰" 같은 어림셈이나 Claude에게 직접 세게 하는 방법은 부정확합니다. [Preporato-0010]

![Messages API 요청 body와 응답 구조, 매 턴 전체 이력을 다시 보내는 흐름](svg/2-messages-api-stateless.svg)
*그림: 서버는 대화 상태를 기억하지 않으므로 system은 최상위 파라미터로, 이력은 messages 전체로 매번 다시 보낸다.*

![context window 구성과 window 초과 시 동작](svg/2-context-window-budget.svg)
*그림: window에는 입력과 출력이 모두 계산되며, 입력만으로 넘으면 400, 생성 중 한계에 닿으면 model_context_window_exceeded로 멈춘다.*

### 1.2 stop_reason 해석
- `end_turn`: 자연스럽게 끝남. `max_tokens`: 요청에서 정한 출력 상한에 걸려 잘림(문장 중간에 끊기는 증상). `stop_sequence`: 지정한 문자열에서 멈춤. `tool_use`: tool 결과를 기다림. `pause_turn`: server-side tool loop가 일시 정지했으므로 다시 보내서 이어감. `refusal`: 거부. [Patrick-0016][Amey-0018][Amey-0053][Preporato-0002]
- `model_context_window_exceeded`: 사용자가 정한 `max_tokens`가 아니라 모델 context window 한계에 걸려 생성이 멈춘 경우입니다. Claude 4.5 이후 모델은 입력 + `max_tokens`가 window를 넘는 요청도 받아들이고, 생성이 window 한계에 닿으면 이 reason으로 멈춥니다. [Preporato-0002][Udemy-0030]
- `max_tokens`와 `model_context_window_exceeded`는 출력이 미완성일 수 있다는 뜻이므로, 완성된 답으로 파싱하면 안 됩니다. [Preporato-0002][Udemy-0044]
- 입력 자체가 window를 넘으면 오래된 부분이 자동으로 잘리지 않습니다. 생성 전에 400 `invalid_request_error`(prompt is too long)로 실패합니다. [Udemy-0001][Amey-0018]
- `tool_use`로 멈춘 것은 오류가 아니라 넘겨받은 작업입니다. 애플리케이션이 tool을 실행하고 결과를 돌려주면 루프가 이어집니다. [Amey-0068]

![stop_reason 7종별 처리 분기](svg/2-stop-reason-branching.svg)
*그림: stop_reason에 따라 완성 처리, 다시 요청해 이어가기, 미완성으로 보고 파싱하지 않기로 나뉜다.*

### 1.3 Streaming
- `stream: true`를 주면 응답이 HTTP 위 server-sent events(SSE)로 조금씩 옵니다. 서버에서 클라이언트로 가는 단방향 통신이며 WebSocket이 아닙니다. 중간에 입력을 추가하려면 새 요청을 보냅니다. [Udemy-0040][Udemy-0026]
- 이벤트 순서: `message_start` → (블록마다) `content_block_start` → `content_block_delta`… → `content_block_stop` → `message_delta` → `message_stop`. 중간에 `ping`이 섞일 수 있습니다. [Patrick-0007][Udemy-0040]
- 텍스트는 `content_block_delta` 안의 `text_delta`로 옵니다. 최종 `stop_reason`과 누적 output token usage는 `message_delta`에 담깁니다. `message_start`는 생성이 끝나기 전에 오므로 최종 reason을 알 수 없고, `ping`은 연결 유지용입니다. [Udemy-0040][Patrick-0031]
- tool 입력은 `input_json_delta`의 `partial_json` 조각으로 옵니다. 조각 하나하나는 올바른 JSON이 아니므로 모두 이어 붙인 뒤 `content_block_stop` 후에 한 번 파싱합니다. SDK streaming helper가 이 작업을 대신해 줍니다. streaming은 tools를 지원합니다. [Patrick-0033]
- streaming이 해결하는 것은 두 가지입니다. (1) 첫 글자가 나오기까지의 체감 지연(perceived latency, TTFT), (2) `max_tokens`가 큰 요청에서 생기는 HTTP timeout. 토큰 단가, 정확도, rate limit은 바꾸지 않습니다. [Preporato-0003][Amey-0012][Udemy-0040]
- `max_tokens`가 큰 non-streaming 요청에는 SDK가 timeout을 피하라며 streaming을 쓰도록 요구할 수 있습니다. [Udemy-0038][Udemy-0040]

![streaming SSE 이벤트 순서와 각 이벤트에서 할 일](svg/2-streaming-event-order.svg)
*그림: 최종 stop_reason은 message_delta에서 오고, input_json_delta 조각은 content_block_stop 뒤에 한 번 파싱한다.*

### 1.4 Prompt caching
- 같은 대용량 prefix(system prompt, 정책 문서, 계약서 등)를 반복해서 보낼 때 가장 먼저 검토할 방법입니다. 내용을 잃지 않으면서 비용과 time-to-first-token을 함께 줄입니다. 지시를 짧게 줄이거나 모델을 바꾸는 방법은 품질을 희생합니다. [Amey-0001][Amey-0011][Amey-0038][Amey-0051]
- 캐시는 prefix 일치 방식입니다. prefix는 tools → system → messages 순서로 고정되어 있고 순서를 바꿀 수 없습니다. breakpoint(`cache_control`)까지의 내용이 이전 요청과 완전히 같아야 hit가 납니다. [Preporato-0004][Udemy-0034]
- 설계 기본형: 변하지 않는 내용을 앞에 두고 그 끝에 `cache_control`을 붙이며, 매번 바뀌는 내용(질문, 시각 등)은 breakpoint 뒤에 둡니다. 바뀌는 블록에 breakpoint를 두면 hit가 한 번도 나지 않고 write 비용만 계속 나갑니다. [Udemy-0034][Amey-0038]
- tool 목록의 구성이나 순서가 요청마다 바뀌면 prefix의 맨 앞이 깨집니다. 그러면 뒤에 오는 system prompt까지 캐시가 무효가 됩니다. 요금제(plan)마다 tool 목록을 고정하고 정렬 순서도 일정하게 유지합니다. [Preporato-0004]
- 모델마다 minimum cacheable length가 있습니다(현재 모델 기준 512~4,096토큰, 예: 1,024). 이보다 짧으면 `cache_control`을 붙여도 오류 없이 캐시되지 않습니다. 실제 캐시 여부는 `usage`의 `cache_creation_input_tokens`와 `cache_read_input_tokens`로 확인합니다. beta header는 필요 없습니다. [Preporato-0005][Udemy-0034]
- 가격 배율(base input 대비): 5분 TTL write 1.25배, 1시간 TTL write 2배, read 0.1배(Opus 5.5와 Sonnet 5.5는 0.05배, Fable 5.2와 Fable 5.1은 0.025배). 재사용이 많을수록 write 할증은 금방 회수됩니다. [Udemy-0034][Udemy-0047]
- TTL은 write 또는 read 요청이 시작된 시점부터 세며, 쓰일 때마다 추가 비용 없이 연장됩니다. 요청이 끊임없이 오면 5분 TTL로 충분하고, 재사용 간격이 5분을 넘으면 1시간 TTL을 씁니다. [Udemy-0047]
- Batch에는 1시간 TTL을 권장합니다. 처리 시간이 5분을 넘을 수 있고, batch의 cache hit는 best-effort이기 때문입니다. caching과 batch는 함께 쓸 수 있고, 함께 쓰면 할인이 겹칩니다. [Preporato-0006][Patrick-0005][Patrick-0023]
- 캐시는 workspace 단위로 분리됩니다. 같은 workspace 안에서는 사용자가 달라도 prefix가 같으면 캐시를 공유하므로, 사용자마다 따로 write할 필요가 없습니다. [Udemy-0047]
- 캐시가 바꾸는 것은 요금과 지연뿐입니다. 캐시된 prefix도 context window를 그대로 차지하고 매번 요청에 포함해서 보내야 합니다. 그래서 window 한계 문제나 요청 크기 문제는 해결하지 못합니다. 많은 모델에서 cache hit 부분이 ITPM에 계산되지 않는 것은 window 용량과 별개의 이야기입니다. [Udemy-0001][Udemy-0034][Udemy-0043]
- caching은 실제로 보낸 내용에만 적용됩니다. 이전 턴을 "기억"하게 해 주는 기능이 아닙니다. [Preporato-0001]

![prompt caching prefix 배치에 따른 cache hit와 miss 사례](svg/2-prompt-caching-prefix.svg)
*그림: breakpoint까지의 prefix가 완전히 같을 때만 hit가 나므로 고정 내용을 앞에, 바뀌는 내용을 breakpoint 뒤에 둔다.*

### 1.5 Message Batches API
- 대량이고 지연을 허용하는 작업(야간 분류, "다음 날 아침까지" 같은 조건)에 씁니다. 입력과 출력 모두 표준 가격의 50%이고, 대부분 1시간 안에 끝나며 최대 24시간 안에 처리됩니다. [Amey-0002][Amey-0013][Amey-0037][Patrick-0023][Udemy-0048]
- 한계: batch 하나에 최대 100,000 requests 또는 256 MB까지 넣을 수 있습니다. 24시간 안에 처리되지 않은 request는 expired가 되며 과금되지 않습니다. 결과는 29일 동안 보관됩니다. [Patrick-0023][Udemy-0048][Preporato-0007]
- 진행 상황은 `processing_status`를 polling해서 확인하고, `ended`가 되면 `results_url`에서 `.jsonl` 결과를 받습니다(stream으로 받아도 됩니다). [Patrick-0023][Udemy-0048][Udemy-0010]
- 결과 순서는 제출 순서를 보장하지 않습니다. 각 request의 `custom_id`로 입력과 결과를 매칭해야 하며, 위치(순서)로 매칭하면 레코드끼리 결과가 뒤바뀝니다. [Patrick-0034][Preporato-0007][Udemy-0048]
- batch 안에서는 `stream`을 쓸 수 없고 multi-turn tool calling도 할 수 없습니다. 개별 응답 속도를 보장하지 않으며, 수요가 많으면 더 느려질 수 있습니다. [Amey-0048][Udemy-0048]
- 사용자가 화면 앞에서 기다리거나 1초 안에 표시해야 하는 실시간 요구에는 맞지 않습니다. [Udemy-0008][Udemy-0026]
- 모든 입력을 요청 하나에 몰아넣는 방식은 context window를 넘으므로 batch를 대신할 수 없습니다. [Amey-0002][Amey-0037]

![Message Batches API 생명주기와 custom_id 매칭](svg/2-batch-lifecycle.svg)
*그림: batch는 제출 후 ended까지 polling하고, 순서가 보장되지 않는 결과를 custom_id로 입력과 매칭한다.*

### 1.6 Files API · 이미지 · PDF 입력
- 같은 PDF나 이미지를 여러 요청이나 여러 턴에서 참조할 때는 Files API에 한 번 업로드하고 `file_id`로 참조합니다. PDF는 `document` block, 이미지는 `image` block의 `source`에 `type: file`로 지정합니다. 파일은 삭제할 때까지 남아 있습니다. [Patrick-0025][Udemy-0043]
- `file_id`로 참조해도 문서 토큰은 포함될 때마다 input으로 과금됩니다. 안정적인 prefix라면 prompt caching과 함께 씁니다. [Patrick-0025]
- `image` source 종류는 세 가지입니다. `base64`(요청 본문에 포함), `url`(온라인 이미지), `file`(Files API). base64는 이력에 남아 있는 한 매 턴 다시 전송됩니다. URL을 텍스트로 프롬프트에 적으면 Claude가 링크를 열어 보지 않습니다. [Udemy-0043]
- Amazon Bedrock과 Google Cloud(Google managed)를 통하면 현재 base64만 쓸 수 있습니다. [Udemy-0043]
- 이미지는 모델의 최대 native resolution보다 크면 Anthropic 쪽에서 축소되므로, 큰 이미지는 업로드 시간과 지연만 늘립니다. 정확도가 유지된다면 앱에서 미리 resize합니다. 이미지 토큰은 픽셀 면적에 비례해 늘어납니다. 이미지는 텍스트보다 앞에 두는 것을 권장합니다. [Preporato-0009]

![Files API 업로드 후 file_id로 여러 요청에서 참조하는 흐름](svg/2-files-api-flow.svg)
*그림: 반복 참조할 파일은 한 번 업로드해 file_id로 참조하지만, 문서 토큰은 포함될 때마다 과금된다.*

### 1.7 Citations
- 주장마다 출처 문서나 구절을 보여 줘야 하는 경우(RAG, 감사 대응)에는 문서를 `document` content block으로 넘기고 `citations: {enabled: true}`를 켭니다. 응답에 원문 구간과 연결된 구조화된 citation span이 돌아옵니다. [Patrick-0010][Patrick-0035]
- 프롬프트로 `[source]` 표시나 페이지 번호를 쓰게 하거나 JSON `sources` 배열을 받는 방식은 검증되지 않은 자유 텍스트입니다. 별도 호출로 출처를 추론하는 방식도 마찬가지로 신뢰할 수 없습니다. [Patrick-0010][Patrick-0035]

![citations 기능의 흐름과 프롬프트 출처 표시 안티패턴 비교](svg/2-citations-flow.svg)
*그림: document block에 citations를 켜야 원문 구간에 연결된 citation span이 오고, 프롬프트로 쓰게 한 출처는 검증할 수 없다.*

### 1.8 구조화 출력 (Structured outputs)
- 타입이 있는 DB 레코드처럼 정해진 형태가 필요하면 스키마로 출력을 제약합니다. 응답 본문은 `output_config.format`(JSON schema)으로, tool 입력은 strict tool use(`strict: true`)로 제약합니다. 구버전 `output_format`은 deprecated입니다. constrained decoding이라 파싱 오류, 필수 필드 누락, 타입 불일치를 막습니다. [Udemy-0044][Amey-0015]
- 이 보장은 정상적으로 끝난 응답에만 적용됩니다. `refusal`이나 `max_tokens`로 끝난 응답은 스키마와 맞지 않을 수 있으므로, 데이터를 넣기 전에 `stop_reason`을 확인합니다. [Udemy-0044]
- 모델 출력은 신뢰할 수 없는 입력으로 다룹니다. tool schema로 형태를 강제하고, 검증하고, 실패하면 오류 내용을 함께 넘겨 다시 시도합니다. 실패를 조용히 건너뛰면 데이터가 사라집니다. [Amey-0003]
- 지시문을 대문자로 강조하기, temperature 0, 정규식 후처리, `max_tokens` 줄이기는 형식을 보장하지 못합니다. `max_tokens`를 너무 작게 잡으면 오히려 JSON이 중간에 잘립니다. [Amey-0003][Amey-0015][Udemy-0044]

![구조화 출력에서 stop_reason 확인과 검증 후 재시도 흐름](svg/2-structured-output-check.svg)
*그림: 스키마로 제약해도 refusal과 max_tokens는 보장 밖이므로 stop_reason을 확인하고, 검증 실패는 오류와 함께 재시도한다.*

### 1.9 Extended thinking 제약
- thinking의 `budget_tokens`는 출력의 일부로 계산되므로 `max_tokens`보다 작아야 합니다. budget 최솟값은 100,000보다 훨씬 작습니다. thinking은 system prompt와 함께 쓸 수 있습니다. [Patrick-0036]
- 수동 extended thinking(`thinking: {type: "enabled", budget_tokens}`)에서는 `tool_choice`로 `auto`와 `none`만 쓸 수 있습니다. `any`나 특정 tool을 강제하면 400이 납니다. tool을 쓰게 유도하려면 프롬프트에 언제 쓸지 적습니다. adaptive thinking은 대부분의 모델에서 강제 tool을 허용하지만, Opus 5.5와 Sonnet 5.5는 강제 tool을 항상 거부합니다. [Patrick-0042]

![수동 extended thinking의 budget_tokens와 tool_choice 제약 판단](svg/2-thinking-constraints.svg)
*그림: 수동 thinking은 budget_tokens가 max_tokens보다 작아야 하고 tool_choice는 auto와 none만 허용한다.*

### 1.10 오류 처리 · retry · rate limit
- retry할 오류(일시적, 기다리면 풀림): 429 `rate_limit_error`, 529 `overloaded_error`, 500 계열, 연결 오류. jitter를 넣은 exponential backoff로, 시도 횟수에 상한을 두고 재시도하며 `retry-after` header가 있으면 그 시간만큼 기다립니다. [Udemy-0007][Amey-0014][Amey-0055]
- retry하지 않을 오류(요청이나 설정을 고쳐야 함): 400 `invalid_request_error`(잘못된 파라미터, prompt is too long 등), 401(인증) 등 429를 제외한 4xx입니다. 그대로 다시 보내면 매번 같은 이유로 실패합니다. [Amey-0017][Udemy-0007][Udemy-0028][Udemy-0001]
- 잘 동작하던 요청에서 갑자기 인증 오류가 나면 payload가 아니라 credential(만료, rotation, 권한 회수)을 의심합니다. [Amey-0066]
- 즉시 반복 재시도는 부하를 더 키우고, 일시적인 429를 치명적 오류로 처리하면 복구할 수 있는 작업을 버리게 됩니다. 고정 간격 재시도는 과부하 때 재시도가 한꺼번에 몰리기 쉽습니다. [Amey-0014][Udemy-0007]
- 공식 SDK는 연결 오류, 429, 5xx를 기본 2회까지 자동 재시도하며(`retry-after`를 따름) `max_retries`로 횟수를 조정합니다. [Udemy-0007][Udemy-0008][Udemy-0038]
- 사용 tier의 월 지출 한도에 걸려 나는 429에는 `retry-after`가 붙지 않고, 한도가 회복될 때까지 계속 실패합니다. 재시도와 별도로 이 경우를 감지하도록 만듭니다. 트래픽을 갑자기 늘리면 한도 안에서도 429가 날 수 있으므로 단계적으로 늘립니다. [Udemy-0007]
- rate limit은 RPM, ITPM, OTPM으로 측정합니다. 동시 사용자 수 같은 요구는 이 세 값의 용량 계획으로 바꿔서 생각하고, 부족하면 미리 상향을 신청합니다. 429 재시도는 사후 복구책일 뿐 용량 확보를 대신하지 못합니다. [Udemy-0026]
- 여러 API key로 나눠서 한도를 피하는 것은 설계가 아니라 회피입니다. [Amey-0013]

![오류 코드별 retry 판단 트리](svg/2-retry-decision-tree.svg)
*그림: 429·529·5xx·연결 오류는 retry-after나 jitter backoff로 상한까지 재시도하고, 400·401은 재시도하지 않고 원인을 고친다.*

### 1.11 동시성 · 비동기 통합 패턴
- 서로 독립적인 여러 호출이 직렬이라 느린 경우에는 `AsyncAnthropic`(동기 `Anthropic`과 인터페이스가 같음)과 `asyncio.gather`로 병렬 처리합니다. 이때 `asyncio.Semaphore`로 동시 실행 수를 rate limit 안으로 제한하고 SDK 자동 재시도와 함께 씁니다. 총 시간은 가장 느린 1건 정도로 줄어듭니다. [Udemy-0008]
- 느린 원인을 먼저 구분합니다. 직렬 대기가 원인이면 병렬화, 1건의 체감 속도가 문제면 streaming, 처리량과 비용이 문제면 batch입니다. [Udemy-0008]
- 앱과 모델 사이에 queue를 두는 가장 큰 이유는 burst를 흡수해서 작업을 버리지 않고 rate limit 안에 머무르게 하는 것입니다. 그래도 retry는 여전히 필요합니다. [Amey-0069]
- endpoint가 지정된 시간(예: 500 ms) 안에 응답해야 하는데 모델 처리가 더 오래 걸리면, 요청 수락과 완료를 분리합니다. 즉시 ack를 돌려주고 결과는 callback이나 poll로 전달합니다. [Amey-0052]
- 몇 시간 걸리는 작업을 동기 HTTP 연결로 붙잡고 있으면 idle timeout이나 연결 끊김 위험이 큽니다. 비동기 job으로 만들고 polling이나 callback(webhook)으로 처리합니다. [Udemy-0010]
- polling은 클라이언트만으로 완결되어 단순하지만, 간격에 따라 감지가 늦어지거나 불필요한 요청이 늘어나는 trade-off가 있습니다. webhook은 즉시 알려 주지만 수신 endpoint 공개, 인증(서명 검증), 재전송과 중복 수신에 대비한 idempotent 처리, 놓친 알림에 대비한 상태 조회 API가 필요합니다. [Udemy-0010]
- HTTP idempotency: GET, HEAD, PUT, DELETE는 idempotent이고 POST, PATCH는 아닙니다. 결과를 모르는 POST를 다시 보낼 때는 idempotency key를 붙이거나 이미 등록됐는지 확인해서 중복 등록을 막습니다. 5xx는 "처리 완료"를 뜻하지 않습니다. [Udemy-0028]
- request identifier를 통합 전체에 걸쳐 전달하는 목적은 traceability입니다. 특정 응답을 그 응답을 만든 요청까지 추적할 수 있어서 비동기나 batch 작업을 디버깅할 때 필요합니다. 비용이나 정확도와는 관계없습니다. [Amey-0067]
  - ⚠️ 해설은 "API가 요구하는 것이 아닌 설계 관행"이라고 하지만, Message Batches API에서는 각 request에 `custom_id`가 필수입니다. 일반적인 상관 ID 관행에 대한 설명으로만 이해합니다.

![직렬 호출과 AsyncAnthropic 병렬 호출의 총 시간 비교](svg/2-async-parallel-semaphore.svg)
*그림: 독립 호출을 병렬로 돌리면 총 시간이 가장 느린 1건 수준으로 줄고, Semaphore가 동시 수를 rate limit 안으로 묶는다.*

![즉시 ack 후 queue와 worker로 처리하고 polling 또는 webhook으로 완료를 알리는 구조](svg/2-async-job-ack-callback.svg)
*그림: 오래 걸리는 처리는 수락과 완료를 분리해 즉시 ack하고, 결과는 polling이나 webhook으로 전달한다.*

![결과를 모르는 POST 재전송 시 중복 방지 방법](svg/2-post-idempotency-retry.svg)
*그림: POST는 idempotent가 아니므로 결과를 모를 때는 idempotency key를 붙이거나 등록 여부를 확인한 뒤 재전송한다.*

### 1.12 Context window 관리
- 대화가 window를 넘을 것 같으면 이전 턴을 요약한 압축 상태(compaction)를 이어서 들고 갑니다. 오래된 턴을 그냥 잘라내면 사실이 조용히 사라지고, 새 대화로 시작하면 상태를 모두 잃습니다. [Amey-0016]
- server-side compaction: Claude가 서버에서 오래된 턴을 요약으로 바꿔 줍니다. 요약 처리를 직접 구현하지 않아도 되며, window 한계에 가까워진 대화를 다루는 주요 전략입니다. [Udemy-0001]
- context editing의 tool result clearing(`clear_tool_uses_20250919`)은 입력 토큰 수 같은 threshold를 넘으면 오래된 tool result부터 placeholder로 바꿉니다. 최근 결과는 지정한 개수만큼 남깁니다. compaction보다 범위가 좁은 수단입니다. [Udemy-0001]
- 판단 기준은 "window에 올라가는 토큰 자체를 줄이는가"입니다. prompt caching(요금), `max_tokens` 늘리기(출력 상한), backoff 재시도(일시적 오류)는 이력의 양을 줄이지 않습니다. [Udemy-0001]
- tool이 필요 없는 큰 payload(예: 50,000토큰 JSON)를 돌려주면 tool이 작업에 필요한 필드만 돌려주도록 고칩니다. window를 늘리면 문제를 미룰 뿐이고, 두 번째 호출로 요약하면 비용과 실패 지점이 늘어납니다. [Amey-0054]
- 큰 context window 모델에 전체 기록을 매번 넣으면 TTFT와 ITPM 소비가 늘어나 실시간 요구와 맞지 않습니다. [Udemy-0026]

![compaction, tool result clearing, payload 축소와 효과 없는 대응 비교](svg/2-context-window-strategies.svg)
*그림: window 문제는 올라가는 토큰 자체를 줄이는 compaction, tool result clearing, payload 축소로만 해결된다.*

### 1.13 SDK · 플랫폼 client
- 공식 SDK(Python, TypeScript, C#, Go, Java, PHP, Ruby)는 raw HTTP와 같은 REST API를 호출하는 wrapper입니다. 더하는 것은 typed request/response, streaming helper(`messages.stream()` 등), 자동 retry, typed exception, tool runner 같은 편의 기능뿐이고, 기능이나 속도는 같습니다. [Udemy-0038]
- AWS에서 IAM 인증을 써야 하면 `AnthropicBedrock()`을 AWS credentials로 설정해 씁니다. Messages 인터페이스는 그대로 유지됩니다. Vertex용으로는 `AnthropicVertex()`가 따로 있습니다. [Patrick-0009]

![SDK, raw HTTP, 플랫폼 client가 같은 Messages API를 쓰는 구조](svg/2-sdk-client-layers.svg)
*그림: SDK와 플랫폼 client는 같은 Messages 인터페이스 위에 편의 기능과 인증 방식만 더한다.*

### 1.14 운영 · 변경 관리 · 디버깅
- 코드를 건드리지 않았는데 출력 형식이 바뀌는 사고를 막으려면 production에서 특정 model version을 고정(pin)하고, eval을 돌린 뒤 의도적으로 업그레이드합니다. prompt는 version control이나 prompt registry로 관리하고 바꾸기 전에 eval을 돌립니다. floating alias나 production에서 직접 수정하는 것이 원인이 됩니다. [Preporato-0008]
- 형식은 맞는데 의미가 틀린 응답은 전송 계층이나 rate limit, `max_tokens`가 아니라 해당 입력에 실제로 들어간 prompt와 context부터 조사합니다. [Amey-0070]

![model version pin과 eval을 거친 업그레이드 흐름](svg/2-model-pin-upgrade.svg)
*그림: production은 model version을 pin하고 eval을 통과한 경우에만 의도적으로 업그레이드한다.*

### 1.15 요구사항 분류 (Claude 시스템 기획)
- 비즈니스 요구(목표·KPI, 예: 작성 시간 30% 단축), 기능 요구(시스템이 무엇을 받아 어떻게 처리하고 무엇을 출력하는지, 테스트로 확인 가능), 비기능 요구(성능, 가용성, 보안. 예: 동시 100건, p95 10초), 프로젝트 제약(기간, 예산)을 구분합니다. "시스템은 ~을 받아 ~을 출력한다"로 바꿔 쓸 수 있으면 기능 요구입니다. [Udemy-0046]
- 요구를 "응답 속도"와 "처리량(동시 사용 수)"으로 나눠 각각에 맞는 수단을 붙입니다. 속도에는 streaming, 처리량에는 rate limit 용량 확보입니다. [Udemy-0026]

![요구사항을 비즈니스, 기능, 비기능, 프로젝트 제약으로 분류하는 판단 트리](svg/2-requirements-classification.svg)
*그림: "시스템은 ~을 받아 ~을 출력한다"로 바꿀 수 있으면 기능 요구이고, 성능 요구는 속도와 처리량으로 나눠 수단을 붙인다.*

## 2. 상황별 정답 판단 규칙

| 이런 상황이면 | 정답 방향 | 근거 |
|---|---|---|
| 큰 system prompt나 문서를 매 요청 반복해서 보내 비용과 지연이 큼 | 안정적인 내용을 앞에 두고 prompt caching 적용 | Amey-0001, 0011, 0038, 0051 |
| 시스템 프롬프트는 같은데 cache hit가 거의 0 | tool 목록이나 순서가 바뀌는지 확인 → 고정. 바뀌는 내용 뒤에 breakpoint를 두지 않음 | Preporato-0004, Udemy-0034 |
| `cache_control`을 붙였는데 cache 토큰이 0이고 오류도 없음 | minimum cacheable length 미달 | Preporato-0005, Udemy-0034 |
| 요청이 계속 들어오는 서비스에서 TTL 선택 | 5분 TTL(쓸 때마다 연장). 간격이 5분을 넘거나 batch면 1시간 TTL | Udemy-0047, Preporato-0006 |
| 대량 처리, 다음 날까지만 끝나면 됨, 비용 우선 | Message Batches API(50%) + 공통 prompt caching | Amey-0002, 0037, Patrick-0005, 0023, Udemy-0048 |
| batch 결과가 다른 레코드에 섞임 | 순서가 아니라 `custom_id`로 매칭 | Patrick-0034, Preporato-0007 |
| 사용자가 화면 앞에서 기다리는 여러 독립 호출 | `AsyncAnthropic` 병렬 + Semaphore로 동시 실행 수 제한 | Udemy-0008 |
| 첫 출력이 빨리 보여야 함 / `max_tokens`가 큰 요청이 timeout | streaming(`stream: true`, SSE) | Amey-0012, Preporato-0003, Udemy-0040 |
| 실시간 + 대규모 동시 사용 | streaming + RPM/ITPM/OTPM 용량 확보(상향 신청) | Udemy-0026 |
| 429 / 529 / 5xx | jitter를 넣은 exponential backoff, 횟수 상한, `retry-after` 준수 | Amey-0014, 0055, Udemy-0007 |
| 400 / 잘못된 파라미터 / 401 | retry하지 않고 요청이나 credential 수정 | Amey-0017, 0066, Udemy-0028 |
| 결과를 모르는 POST를 다시 보내야 함 | idempotency key 또는 등록 여부 확인 후 재전송 | Udemy-0028 |
| 응답이 문장 중간에서 끊김 | `stop_reason: max_tokens` → limit 올리기 | Amey-0018, Patrick-0016 |
| model window 한계에서 멈춤 | `model_context_window_exceeded` | Preporato-0002 |
| `stop_reason: tool_use` | tool 실행 → `tool_result`를 돌려주고 루프 계속 | Amey-0068 |
| 챗봇이 이전 대화를 잊음 | 전체 이력(user/assistant 번갈아)을 매번 전송 | Preporato-0001, Patrick-0015 |
| `messages`에 `role: system`을 넣어 오류 | 최상위 `system` 파라미터 사용 | Patrick-0001, 0040 |
| 긴 agent가 window 한계에 다가감 | compaction + context editing(tool result clearing) | Udemy-0001, Amey-0016 |
| tool이 거대한 payload를 돌려줌 | tool이 필요한 필드만 돌려주도록 수정 | Amey-0054 |
| 형식이 정해진 레코드 추출 | `output_config.format` 또는 strict tool use + `stop_reason` 확인 | Udemy-0044, Amey-0015 |
| 주장마다 출처 구절을 표시해야 함 | `document` block + `citations: {enabled: true}` | Patrick-0010, 0035 |
| 같은 PDF나 이미지를 여러 번 참조 | Files API 업로드 → `file_id` 참조(필요하면 caching 추가) | Patrick-0025, Udemy-0043 |
| 고해상도 사진 때문에 지연이 큼 | 앱에서 미리 resize | Preporato-0009 |
| 요청이 window에 들어가는지, 비용이 얼마인지 미리 알아야 함 | token counting endpoint | Preporato-0010 |
| thinking + 특정 tool 강제에서 400 | 수동 thinking은 `tool_choice` `auto`/`none`만 허용 | Patrick-0042 |
| `budget_tokens` ≥ `max_tokens`로 거부됨 | `max_tokens`를 budget보다 크게 | Patrick-0036 |
| AWS IAM 인증 | `AnthropicBedrock()` | Patrick-0009 |
| endpoint 지연 SLA보다 모델 처리가 오래 걸림 | 즉시 ack + callback/poll | Amey-0052 |
| 몇 시간 걸리는 job의 완료 통지 | 비동기 job + polling 또는 webhook(서명, idempotent 처리) | Udemy-0010 |
| 트래픽 burst | 앞단에 queue 배치 | Amey-0069 |
| 모델 출력 형식이 하룻밤 사이에 바뀜 | model version pin + prompt 버전 관리 + eval | Preporato-0008 |
| 형식은 맞는데 의미가 틀림 | prompt와 해당 입력의 context부터 조사 | Amey-0070 |

![비용, 지연, 처리량 상황별 판단 트리](svg/2-decision-cost-latency.svg)
*그림: 비용·지연·처리량 문제는 prefix 반복, 대기 여부, 화면 대기, 트래픽 형태로 나눠 수단을 고른다.*

![오류, 응답 처리, 운영 상황별 판단 트리](svg/2-decision-errors-responses.svg)
*그림: 오류는 일시적인지 영구적인지, 응답은 stop_reason으로 먼저 구분해 처리한다.*

![context, 입력, 출력 형식 상황별 판단 트리](svg/2-decision-context-input.svg)
*그림: window 문제, 출력 형식과 출처, 파일 입력을 각각 맞는 API 기능으로 해결한다.*

## 3. 자주 나오는 오답 함정
- "prompt caching이 이전 대화를 기억해 준다 / window를 늘려 준다" → 캐시는 보낸 내용의 요금과 지연만 줄입니다. 기억하게 하거나 window 용량을 바꾸지 않습니다. [Preporato-0001][Udemy-0001][Udemy-0034]
- "캐시하면 요청에서 그 부분을 빼고 보내도 된다 / 요청 크기가 줄어든다" → 매번 같은 내용을 포함해서 보내야 합니다. 요청 크기를 줄이는 것은 Files API의 `file_id`입니다. [Udemy-0043][Amey-0038]
- "시스템 프롬프트를 tools보다 앞에 둔다" → prefix 순서(tools → system → messages)는 고정이라 바꿀 수 없습니다. [Preporato-0004]
- "1시간 TTL이 항상 유리하다 / 5분 TTL은 5분마다 다시 과금된다" → 1시간 write는 2배이고, 5분 TTL은 쓸 때마다 무료로 연장됩니다. [Udemy-0047]
- "캐시는 사용자별로 따로 써야 한다" → 같은 workspace 안에서 prefix가 같으면 공유됩니다. [Udemy-0047]
- "caching은 batch와 함께 쓸 수 없다" → 함께 쓸 수 있고 할인이 겹칩니다. batch에는 1시간 TTL을 권장합니다. [Preporato-0006][Patrick-0005]
- "streaming은 토큰 단가를 낮춘다 / rate limit을 해결한다 / 정확도를 올린다" → 전달 방식만 바뀝니다. 50% 할인은 Batches API의 특징입니다. [Preporato-0003][Udemy-0040]
- "streaming은 WebSocket 양방향이다 / SDK는 SSE를 처리하지 못한다" → HTTP SSE 단방향이며 SDK가 streaming helper를 기본 제공합니다. [Udemy-0040][Udemy-0038]
- "`input_json_delta`가 깨진 JSON이다 → 스키마 강화나 temperature 0" → 원래 조각입니다. 모아서 `content_block_stop` 후에 파싱합니다. [Patrick-0033]
- "batch는 결과가 제출 순서대로 온다 / 더 빠르다 / 진행 상황을 SSE로 보여 준다" → 순서를 보장하지 않고, 속도를 보장하지 않으며, stream을 쓸 수 없습니다. [Patrick-0034][Udemy-0048]
- "실시간 화면 대기에 Batches API" → 최대 24시간이고 완료 시각을 알 수 없어 맞지 않습니다. [Udemy-0008][Udemy-0026]
- "`max_tokens`를 낮추면 비용이 싸진다 / 형식이 안전해진다" → 토큰 단가는 그대로이고, 너무 낮으면 JSON이 잘립니다. [Amey-0002][Udemy-0044]
- "`max_tokens`를 올리면 window 문제가 해결된다" → 출력 상한일 뿐이고 출력도 window를 차지합니다. [Udemy-0001][Udemy-0030]
- "window를 넘은 입력은 오래된 부분부터 자동으로 잘린다" → 400 오류가 납니다. [Udemy-0001]
- "max_retries만 늘리면 빨라진다" → 직렬 구조는 그대로라 총 시간이 줄지 않습니다. [Udemy-0008]
- "400도 backoff로 재시도 / 429는 치명적이므로 중단 / 즉시 재전송" → 오류 종류(일시적인지 영구적인지)에 따라 다르게 처리해야 합니다. [Udemy-0007][Udemy-0028]
- "timeout 난 POST는 idempotent이므로 그냥 다시 보낸다 / 5xx면 등록된 것으로 간주한다" → POST는 idempotent가 아니고, 5xx는 완료를 뜻하지 않습니다. [Udemy-0028]
- "구조화 출력을 쓰면 `stop_reason` 확인은 필요 없다" → `refusal`과 `max_tokens`는 보장 범위 밖입니다. [Udemy-0044]
- "프롬프트로 `[source]`나 페이지 번호를 쓰게 한다" → 검증할 수 없습니다. citations 기능을 씁니다. [Patrick-0010][Patrick-0035]
- "이미지 URL을 텍스트로 적으면 Claude가 연다" → 문자열로만 읽힙니다. `source.type: url`을 씁니다. [Udemy-0043]
- "SDK는 별도의 빠른 endpoint나 SDK 전용 기능을 쓴다" → 같은 API이고 기능도 같습니다. [Udemy-0038]
- "thinking과 tools는 함께 쓸 수 없다 / Batches로만 가능하다" → `tool_choice` `auto`/`none`이면 함께 쓸 수 있습니다. [Patrick-0042]
- "큰 context window 모델에 전체 기록을 넣는다" → TTFT와 ITPM이 나빠집니다. [Udemy-0026]
- "가장 최신 model alias를 쓴다" → 출력이 조용히 바뀌는 원인이 됩니다. pin하고 eval을 돌립니다. [Preporato-0008]
- "재시도를 queue가 대체한다" → queue는 burst를 흡수할 뿐이고 retry는 여전히 필요합니다. [Amey-0069]
- "성능 요구나 KPI를 기능 요구로 고른다" → 기능 요구는 입력·처리·출력으로 이루어진 시스템 동작입니다. [Udemy-0046]

## 4. 암기 목록

| 이름/숫자/파라미터/상태 코드 | 의미 |
|---|---|
| `system` (최상위) | system prompt를 넣는 위치. `messages`에는 system role이 없음 [Patrick-0001] |
| `max_tokens` | 출력 상한. thinking `budget_tokens`보다 커야 함 [Patrick-0016][Patrick-0036] |
| `end_turn` / `max_tokens` / `stop_sequence` / `tool_use` / `pause_turn` / `refusal` / `model_context_window_exceeded` | stop_reason 종류 [Patrick-0016][Preporato-0002] |
| `stream: true` | SSE 스트리밍 [Udemy-0040] |
| `message_start` → `content_block_start` → `content_block_delta` → `content_block_stop` → `message_delta` → `message_stop` (+`ping`) | 스트림 이벤트 순서 [Patrick-0007] |
| `text_delta` / `input_json_delta`(`partial_json`) | 텍스트 조각 / tool 입력 JSON 조각 [Udemy-0040][Patrick-0033] |
| `message_delta` | 최종 `stop_reason`과 누적 output usage [Patrick-0031] |
| `cache_control` | cache breakpoint [Udemy-0034] |
| tools → system → messages | cache prefix 순서(고정) [Preporato-0004] |
| 512~4,096토큰 | 모델별 minimum cacheable length 범위(미달이면 오류 없이 캐시 안 됨) [Udemy-0034][Preporato-0005] |
| 1.25배 / 2배 / 0.1배 | 5분 write / 1시간 write / read (Opus·Sonnet 5.5 read 0.05배, Fable 5.2·5.1 read 0.025배) [Udemy-0047] |
| `cache_creation_input_tokens` / `cache_read_input_tokens` | 캐시 write와 read를 확인하는 usage 필드 [Preporato-0005] |
| 5분 / 1시간 | cache TTL. 쓸 때마다 무료로 연장 [Udemy-0047] |
| 50% | Batches API 할인(입력·출력 모두) [Patrick-0023][Udemy-0048] |
| 100,000 requests / 256 MB | batch 하나의 상한 [Patrick-0023] |
| 1시간(대부분) / 24시간(최대) | batch 처리 시간 [Udemy-0048] |
| 29일 | batch 결과 보관 기간 [Preporato-0007] |
| `custom_id` | batch request와 결과를 매칭하는 키 [Patrick-0034] |
| `processing_status` = `ended`, `results_url` (.jsonl) | batch 완료 확인 polling과 결과 받기 [Udemy-0048] |
| `file_id`, `source.type: file` / `url` / `base64` | Files API 참조 / 이미지 source 종류 [Udemy-0043][Patrick-0025] |
| `citations: {enabled: true}` | `document` block에서 citations 켜기 [Patrick-0010] |
| `output_config.format` / `strict: true` | 구조화 출력(JSON) / strict tool use. `output_format`은 deprecated [Udemy-0044] |
| `thinking: {type: "enabled", budget_tokens}` | 수동 extended thinking. `tool_choice`는 `auto`/`none`만 허용 [Patrick-0042] |
| `clear_tool_uses_20250919` | context editing의 tool result clearing [Udemy-0001] |
| 400 `invalid_request_error` | 요청 오류(prompt is too long 포함). retry하지 않음 [Udemy-0001][Udemy-0007] |
| 401 | 인증 오류 → credential 점검 [Udemy-0007][Amey-0066] |
| 429 `rate_limit_error` | 일시적. backoff + `retry-after`. 단 지출 한도로 인한 429는 `retry-after`가 없음 [Udemy-0007] |
| 500 / 529 `overloaded_error` | 일시적인 서버 오류 / 과부하 → backoff [Udemy-0007] |
| `retry-after` | 기다릴 초 수를 알려 주는 header [Udemy-0007] |
| `max_retries` (기본 2) | SDK 자동 재시도 횟수 [Udemy-0007][Udemy-0008] |
| RPM / ITPM / OTPM | 분당 요청 수 / 입력 토큰 수 / 출력 토큰 수 rate limit [Udemy-0026] |
| `AsyncAnthropic` + `asyncio.Semaphore` | 비동기 병렬 처리 + 동시 실행 수 제한 [Udemy-0008] |
| `AnthropicBedrock()` / `AnthropicVertex()` | AWS IAM용 / Google Cloud용 client [Patrick-0009] |
| GET·HEAD·PUT·DELETE / POST·PATCH | idempotent / non-idempotent [Udemy-0028] |
| token counting endpoint | 요청의 정확한 토큰 수 측정 [Preporato-0010] |
| 1M 토큰 | 현재 대부분 모델의 context window 크기 [Udemy-0030] |

## 5. 시험 직전 체크리스트
- [ ] Messages API는 stateless라 매번 전체 이력을 보내고, system은 최상위 `system` 파라미터로 보낸다.
- [ ] context window에는 입력(tools·system·messages) + 출력(thinking 포함)이 모두 계산된다.
- [ ] stop_reason 7종(`end_turn`, `max_tokens`, `stop_sequence`, `tool_use`, `pause_turn`, `refusal`, `model_context_window_exceeded`)을 구분한다.
- [ ] window를 넘은 입력은 자동으로 잘리지 않고 400이 난다.
- [ ] 스트림 이벤트 순서를 알고, `stop_reason`과 usage는 `message_delta`에 온다.
- [ ] `input_json_delta`는 모아서 `content_block_stop` 후에 파싱한다.
- [ ] streaming은 TTFT와 HTTP timeout을 해결하고, 가격·정확도·rate limit은 바꾸지 않는다.
- [ ] cache prefix 순서는 tools → system → messages이고, 고정 내용은 앞에, breakpoint는 고정 내용 끝에 둔다.
- [ ] tool 목록이나 순서가 바뀌면 캐시 전체가 무효가 된다.
- [ ] minimum cacheable length 미달이면 오류 없이 캐시되지 않는다 → usage 필드로 확인한다.
- [ ] 캐시 배율: write 1.25배(5분)/2배(1시간), read 0.1배. TTL은 쓸 때마다 연장된다.
- [ ] 캐시는 요금과 지연만 줄이고, window 용량이나 요청 크기는 줄이지 않는다.
- [ ] Batches: 50%, 최대 24시간, 100,000건/256 MB, `custom_id`로 매칭, 순서 보장 없음, stream 불가.
- [ ] batch + caching에는 1시간 TTL을 쓴다.
- [ ] 반복 참조하는 PDF나 이미지는 Files API `file_id`로 참조한다(과금은 매번 발생).
- [ ] 출처 표시는 `document` block + `citations: {enabled: true}`로 한다.
- [ ] 구조화 출력은 `output_config.format` 또는 `strict: true`로 하고, `refusal`/`max_tokens`인지 확인한다.
- [ ] 429·529·5xx는 jitter backoff + `retry-after`, 400·401은 retry하지 않는다. SDK는 기본 2회 재시도한다.
- [ ] 화면 대기 + 독립된 여러 호출에는 `AsyncAnthropic` + Semaphore, 대기 없는 대량 처리에는 Batches를 쓴다.
- [ ] window가 부족하면 compaction / tool result clearing / tool payload 축소로 대응하고, `max_tokens`나 caching으로는 해결되지 않는다.
- [ ] 수동 thinking: `budget_tokens` < `max_tokens`, `tool_choice`는 `auto`/`none`만 허용한다.
- [ ] production에서는 model version을 pin하고, prompt는 버전 관리와 eval을 거친다.

---
### ⚠️ 해설 검토 메모
- ⚠️ [Amey-0014] 해설은 rate limit을 "호출 수로 측정된다"고 설명하지만, 공식 rate limit은 RPM뿐 아니라 ITPM/OTPM(토큰)도 있습니다(Udemy-0026 참고). 요청 크기를 줄이는 것이 토큰 한도에는 영향을 줄 수 있습니다. 다만 정답(backoff + 상한)은 그대로 유효합니다.
- ⚠️ [Patrick-0016] "raise the limit or stream"에서 streaming 자체는 `max_tokens`로 잘리는 문제를 해결하지 않습니다. streaming은 큰 `max_tokens`를 HTTP timeout 없이 쓸 수 있게 해 줄 뿐이며, 해결책은 limit을 올리는 것입니다.
- ⚠️ [Amey-0067] "API가 요구하는 것이 아니다"라는 설명은 일반적인 상관 ID에 대한 것입니다. Message Batches API에서는 `custom_id`가 필수입니다.
