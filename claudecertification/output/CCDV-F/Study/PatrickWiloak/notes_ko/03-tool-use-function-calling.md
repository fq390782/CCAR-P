# 03 - 도구 사용과 함수 호출

도구 사용(tool use, Claude가 외부 기능이나 프로그램을 호출해 실제 작업을 수행하는 방식)은 Claude가 행동하는 방법입니다. 이 노트에서는 라이프사이클(lifecycle, 요청부터 결과 반환까지의 전체 흐름), 선택 모드, 병렬 도구 사용, 강제 선택을 통한 구조화된 출력(structured output, 정해진 형식에 맞춘 데이터 출력), 그리고 관용적인 루프(loop, 같은 처리를 반복하는 구조) 구성 방법을 다룹니다.

---

## 도구 정의

도구는 세 가지 필드(field, 데이터의 항목)로 선언합니다.

```json
{
  "name": "get_weather",
  "description": "Look up current weather for a city. Returns null if unknown.",
  "input_schema": {
    "type": "object",
    "properties": {
      "city": {"type": "string", "description": "City name"},
      "units": {"type": "string", "enum": ["c", "f"], "default": "c"}
    },
    "required": ["city"]
  }
}
```

`description`은 일종의 프롬프트(prompt, 모델에 주는 지시문)입니다. 시간을 들여 작성하십시오. 언제 사용하는지, 무엇이 반환되는지, 부작용(side effect, 데이터 변경 등 호출로 인해 생기는 부수적인 영향), 그리고 파라미터(parameter, 도구에 넘기는 입력값)가 명확하지 않은 경우에는 호출 예시까지 포함하십시오.

---

## 도구 선택 모드

- `tool_choice: {"type": "auto"}` (기본값) - 도구를 호출할지 여부를 Claude가 결정합니다
- `tool_choice: {"type": "any"}` - Claude는 사용 가능한 도구 중 하나를 반드시 호출해야 합니다
- `tool_choice: {"type": "tool", "name": "get_weather"}` - Claude는 이 특정 도구를 반드시 호출해야 합니다
- `tool_choice: {"type": "none"}` - Claude는 도구를 호출할 수 없습니다

일반적인 에이전트(agent, 스스로 판단하며 여러 단계의 작업을 수행하는 AI 프로그램)에는 `auto`를 사용합니다. 어떤 행동이 반드시 필요할 때는 `any`를 사용합니다. 구조화된 출력을 보장하려면 특정 도구를 지정하는 형태를 사용합니다.

---

## 도구 사용 라이프사이클

1. `tools`를 정의하고 사용자 메시지를 담아 요청(request, API에 보내는 호출)을 보냅니다
2. Claude가 응답합니다. 도구를 사용하려는 경우 `stop_reason: tool_use`가 되며, 어시스턴트 메시지에 하나 이상의 `tool_use` 콘텐츠 블록(content block, 메시지를 구성하는 단위 조각)이 포함됩니다.

```json
{
  "type": "tool_use",
  "id": "toolu_01ABC...",
  "name": "get_weather",
  "input": {"city": "Austin"}
}
```

3. 여러분의 코드에서 `get_weather("Austin")`를 실행합니다
4. 새 메시지를 보냅니다.

```json
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01ABC...",
      "content": "Sunny, 28C"
    }
  ]
}
```

5. 계속 진행합니다. Claude는 도구를 더 사용하거나 `end_turn` 텍스트 응답을 생성할 수 있습니다.

중요: `tool_result`는 항상 `user` 메시지에 넣습니다. `tool_use_id`는 반드시 일치해야 합니다.

---

## 병렬 도구 사용

최신 Claude 모델은 하나의 응답에서 여러 개의 `tool_use` 블록을 생성할 수 있습니다. 여러분의 루프는 이를 처리할 수 있어야 합니다.

```python
if response.stop_reason == "tool_use":
    tool_results = []
    for block in response.content:
        if block.type == "tool_use":
            result = execute(block.name, block.input)
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": result,
            })
    history.append({"role": "user", "content": tool_results})
```

모든 tool_result 블록은 하나의 user 메시지에 함께 담아 보내십시오. 여러 턴(turn, 대화에서 한 번 주고받는 차례)에 나누어 보내지 마십시오.

---

## 도구의 오류

오류는 구조화된 형태로 반환합니다.

```json
{
  "type": "tool_result",
  "tool_use_id": "toolu_01ABC",
  "content": "Order 12345 not found. Use search_orders if you only have the customer name.",
  "is_error": true
}
```

정보가 담긴 오류 메시지가 있어야 Claude가 복구할 수 있습니다. "Failed"나 "Error 500" 같은 메시지는 쓸모가 없습니다.

---

## 강제 도구 선택을 통한 구조화된 출력

구조화된 데이터를 추출하는 가장 깔끔한 방법입니다.

```python
extract_tool = {
    "name": "save_invoice",
    "description": "Save the extracted invoice fields.",
    "input_schema": {
        "type": "object",
        "properties": {
            "invoice_number": {"type": "string"},
            "total": {"type": "number"},
            "line_items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "description": {"type": "string"},
                        "amount": {"type": "number"},
                    },
                    "required": ["description", "amount"],
                },
            },
        },
        "required": ["invoice_number", "total", "line_items"],
    },
}

resp = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=2048,
    tools=[extract_tool],
    tool_choice={"type": "tool", "name": "save_invoice"},
    messages=[{"role": "user", "content": invoice_text}],
)

structured = next(b for b in resp.content if b.type == "tool_use").input
```

도구를 실제로 "실행"할 필요는 없습니다. `input` 필드를 구조화된 출력으로 그대로 사용하면 됩니다.

---

## 스트리밍과 도구 사용

`tool_use` 블록도 스트리밍(streaming, 응답을 한 번에 받지 않고 생성되는 대로 조금씩 받는 방식)됩니다. `content_block_start`가 `tool_use` 블록을 열고, 이어서 `input_json_delta` 이벤트가 입력값의 JSON 조각을 스트리밍합니다. 클라이언트(client, API를 호출하는 쪽 프로그램)에서 이를 다시 조립해야 하며, SDK(Software Development Kit, 개발을 돕는 공식 라이브러리 모음) 헬퍼가 이 작업을 대신 해줍니다.

---

## 에이전트 루프

이해하기 쉽도록 직접 작성한 간단한 루프입니다.

```python
def run_agent(user_prompt, tools, executors, max_iterations=20):
    history = [{"role": "user", "content": user_prompt}]
    for _ in range(max_iterations):
        resp = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=2048,
            tools=tools,
            messages=history,
        )
        history.append({"role": "assistant", "content": resp.content})
        if resp.stop_reason != "tool_use":
            return resp
        tool_results = []
        for block in resp.content:
            if block.type == "tool_use":
                try:
                    result = executors[block.name](**block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(result),
                    })
                except Exception as e:
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": f"Error: {e}",
                        "is_error": True,
                    })
        history.append({"role": "user", "content": tool_results})
    raise RuntimeError("max iterations exceeded")
```

프로덕션(production, 실제 서비스 운영 환경)에서는 스트리밍, 관측 가능성(observability, 시스템 동작을 로그·지표로 파악할 수 있는 능력), 재시도, 예산 제한을 추가하겠지만, 뼈대는 이와 같습니다.

---

## 도구 설계 모범 사례

- 동사-명사 형태의 이름 (`get_customer`, `search_orders`, `create_ticket`)
- 설명은 프롬프트이므로 프롬프트처럼 다루십시오
- 필수 파라미터는 최소한으로, 선택 파라미터는 유연하게
- 가능한 경우 멱등성(idempotent, 같은 호출을 여러 번 해도 결과가 같은 성질)을 갖추십시오
- `is_error: true`를 사용한 구조화된 오류
- 부작용을 명시적으로 문서화하십시오
- 기능이 겹치는 도구는 피하십시오 - 하나로 합치거나 디스패처(dispatcher, 요청을 받아 알맞은 처리로 분배하는 도구)로 묶으십시오

---

## 안티패턴

- 도구 결과를 assistant 메시지에 넣는 것
- `tool_use_id`를 빠뜨리는 것
- 강제 도구 선택 대신 프롬프트 지시로 "JSON으로 응답하라"고 하는 것
- `is_error: true`를 무시하고 모든 결과를 성공으로 처리하는 것
- 병렬로 호출할 수 있는 도구를 순차적으로 호출하는 것

---

## 시험 핵심 포인트

- 도구 결과의 위치 (user 역할)
- `tool_use_id` 필수 요건
- `tool_choice` 모드와 각각을 언제 사용하는지
- 병렬 도구 사용의 동작 방식
- 강제 도구 선택을 통한 구조화된 출력
- 오류 응답의 형태

---

## 핵심 용어

- **tool_use 블록** - Claude가 여러분에게 도구 실행을 요청하는 assistant 메시지 내의 콘텐츠 블록으로, id, name, input을 담고 있습니다.
- **tool_result 블록** - tool_use에 대한 여러분의 응답으로, 일치하는 tool_use_id와 함께 user 메시지에 담아 보냅니다.
- **tool_choice** - Claude가 도구를 호출할 수 있는지를 설정합니다: auto (Claude가 결정), any (하나를 반드시 호출), tool (지정한 도구를 반드시 호출), none.
- **강제 도구 선택(Forced tool choice)** - 도구 호출을 강제하는 tool_choice any 또는 tool입니다. Claude Opus 5.5, Sonnet 5.5, Fable 5.1, Mythos 5.1에서는 400 오류를 반환하므로, 이들 모델에서는 strict tool use(엄격한 도구 사용)와 함께 auto를 사용하거나 structured outputs를 사용하십시오.
