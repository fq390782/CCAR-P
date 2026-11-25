# 05 - Files API, Citations(인용), PDF

서로 밀접하게 관련된 세 가지 기능으로, 이를 함께 사용하면 Claude가 문서를 다루고 근거가 있으며 출처가 표시된(grounded, attributed) 응답을 생성할 수 있습니다.

---

## Files API

Files API(파일을 미리 업로드해 두고 재사용하는 API)를 사용하면 바이너리(binary, 텍스트가 아닌 원시 데이터 형식) 콘텐츠(PDF, 이미지, JSON(데이터를 주고받기 위한 텍스트 형식) 등)를 한 번만 업로드하고, 여러 요청에서 ID로 참조할 수 있습니다.

### 이유

- 매 요청마다 같은 파일을 다시 업로드하지 않아도 됩니다
- 요청 페이로드(payload, 요청에 실어 보내는 데이터 본문)를 작고 빠르게 유지할 수 있습니다
- 업로드한 콘텐츠를 배치(batch, 여러 요청을 묶어 한꺼번에 처리하는 방식) 요청 전반에서 재사용할 수 있습니다

### 업로드

```python
file = client.files.create(
    file=open("contract.pdf", "rb"),
    purpose="user_data",  # purpose의 의미는 최신 문서 기준
)
print(file.id)  # file_...
```

### Messages에서 참조하기

```python
client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=2048,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "document", "source": {"type": "file", "file_id": file.id}},
                {"type": "text", "text": "Summarize this contract."},
            ],
        }
    ],
)
```

### 수명 주기

- 파일에는 계정별 저장 TTL(Time To Live, 데이터가 보관되는 유효 기간)이 있습니다(최신 문서를 확인하세요)
- 더 이상 필요하지 않으면 `client.files.delete(file.id)`로 삭제합니다
- 재사용을 위해 파일 ID를 자체 데이터 저장소에서 관리합니다

### 제한 사항

- 요청당 및 파일당 최대 파일 크기가 있습니다(문서를 확인하세요)
- 지원 형식: PDF, 이미지(PNG/JPEG/GIF/WebP), 텍스트, JSON 등
- 일부 형식은 베타 헤더(beta header, 시험 단계 기능을 쓰겠다고 요청에 붙이는 표시)가 필요합니다

---

## Vision(이미지 입력)

이미지는 base64(바이너리 데이터를 문자열로 변환하는 인코딩 방식), URL, 또는 file_id로 전달합니다:

```python
{
    "type": "image",
    "source": {
        "type": "base64",
        "media_type": "image/png",
        "data": base64_string,
    },
}
```

URL 형식:

```python
{"type": "image", "source": {"type": "url", "url": "https://..."}}
```

파일 ID 형식:

```python
{"type": "image", "source": {"type": "file", "file_id": file.id}}
```

활용 사례:

- OCR(Optical Character Recognition, 이미지 속 글자를 인식하는 기술) 대체(Claude가 이미지 내용을 읽고 추론합니다)
- UI 스크린샷 분석
- 차트 및 다이어그램 해석
- 시각적 분류

팁:

- 토큰(token, 모델이 글자를 처리하는 단위) 수를 조절하기 위해 매우 큰 이미지는 업로드 전에 크기를 줄입니다
- 이미지 토큰은 과금됩니다. 1080p 이미지는 디테일 수준에 따라 대략 수천 토큰이 듭니다

---

## PDF 지원

PDF는 `document` 콘텐츠 블록(content block, 메시지를 구성하는 내용 단위)으로 전송합니다. Claude는 텍스트와 시각적 레이아웃(차트, 표, 다이어그램)을 모두 읽습니다.

```python
{
    "type": "document",
    "source": {
        "type": "base64",
        "media_type": "application/pdf",
        "data": base64_pdf,
    },
}
```

또는 file_id로 전달합니다(재사용 시 권장):

```python
{"type": "document", "source": {"type": "file", "file_id": file.id}}
```

활용 사례:

- 계약서 분석
- 연구 논문 요약
- 재무 공시 자료 추출
- 컴플라이언스(compliance, 법규·사내 규정 준수) 검토

팁:

- 큰 PDF는 토큰을 많이 사용하므로 먼저 `count_tokens`로 확인합니다
- 같은 PDF를 여러 번 참조할 때는 프롬프트 캐싱(prompt caching, 반복되는 입력을 저장해 비용과 시간을 줄이는 기능)과 함께 사용합니다
- 출처 표시를 위해 citations(다음 섹션)와 함께 사용합니다

---

## Citations(인용)

Citations(인용, 응답의 근거가 된 원문 위치를 표시하는 기능)를 사용하면 Claude가 응답의 특정 구간이 원본 문서의 어느 구간에 근거하는지 표시할 수 있습니다.

### 활성화

`document` 콘텐츠 블록에 `citations: {enabled: true}`를 포함합니다:

```python
{
    "type": "document",
    "source": {"type": "file", "file_id": file.id},
    "citations": {"enabled": true},
    "title": "Acme 2025 Annual Report",
    "context": "Filed with SEC on 2025-12-31",
}
```

### 응답 형태

Claude의 텍스트 콘텐츠 블록에는 구간과 연결된 `citations` 배열이 포함됩니다:

```json
{
  "type": "text",
  "text": "Revenue grew 23% in Q4...",
  "citations": [
    {
      "type": "page_location",
      "cited_text": "Q4 revenue rose to $1.2B from $980M...",
      "document_index": 0,
      "document_title": "Acme 2025 Annual Report",
      "start_page_number": 14,
      "end_page_number": 14
    }
  ]
}
```

인용 유형은 문서 유형에 따라 다릅니다(PDF는 page_location, 텍스트는 char_location).

### 사용 시점

- 컴플라이언스 및 감사(audit) 사례
- "출처"를 보여줘야 하는 고객 대상 RAG(Retrieval-Augmented Generation, 문서를 검색해 그 내용을 바탕으로 답변을 생성하는 방식)
- 리서치 어시스턴트
- 사용자가 출처를 검증해야 하는 모든 워크로드(workload, 시스템이 처리하는 작업)

### 품질 관련 참고

Citations는 문서 내 실제 근거를 바탕으로 Claude가 생성합니다. 완벽하게 정확하지는 않지만, Claude에게 본문 속에 출처 표시를 직접 지어내도록 요청하는 것보다 훨씬 신뢰할 수 있습니다.

### 팁

- Claude가 문서를 구분할 수 있도록 문서별로 `title`과 `context`를 제공합니다
- 가능하면 관련성 순으로 문서를 배치합니다
- 최적의 UX(사용자 경험)를 위해 인용을 인라인 각주나 마우스오버 툴팁으로 표시합니다
- 컴플라이언스를 위해 응답과 함께 인용을 로그로 기록합니다

---

## 조합 패턴

일반적인 출처 표시 포함 RAG 흐름:

```python
# 1. 문서를 한 번만 업로드
docs = [client.files.create(file=open(p, "rb"), purpose="user_data") for p in paths]

# 2. 정적인 시스템 프롬프트를 캐싱
system = [
    {
        "type": "text",
        "text": "You are a research assistant. Always cite your sources.",
        "cache_control": {"type": "ephemeral"},
    }
]

# 3. 문서와 citations를 활성화한 상태로 질의 전송
content = []
for d in docs:
    content.append({
        "type": "document",
        "source": {"type": "file", "file_id": d.id},
        "citations": {"enabled": True},
    })
content.append({"type": "text", "text": user_question})

resp = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=2048,
    system=system,
    messages=[{"role": "user", "content": content}],
)

# 4. 인용 구간과 함께 텍스트를 렌더링
for block in resp.content:
    if block.type == "text":
        render(block.text, block.citations)
```

---

## 흔한 실수

- 매 요청마다 같은 파일을 다시 업로드함(file_id를 사용하세요)
- citations를 명시적으로 활성화하는 것을 잊음
- PDF를 base64로 메모리에 저장한 뒤 해제하는 것을 잊음
- 이미지당 토큰 비용을 측정하지 않음
- citations를 document 블록이 아닌 시스템 프롬프트(system prompt, 모델에 역할과 규칙을 미리 지시하는 입력)에서 사용함

---

## 시험 출제 포인트

- Files API의 한 번 업로드, ID로 참조하는 패턴
- `document` 콘텐츠 블록의 형태
- citations 활성화 및 응답 읽기
- 이미지 입력 방식(base64, URL, file_id)
- 프로덕션(production, 실제 서비스 운영 환경) RAG를 위한 파일 + 캐싱 + citations 조합

---

## 핵심 용어

- **Files API** - 콘텐츠를 한 번 업로드하고 여러 요청에서 ID로 참조할 수 있게 해 줍니다.
- **Citations** - Claude 응답의 구간을 원본 문서의 특정 구간에 연결해 출처를 표시합니다. document 블록에 citations: {enabled: true}를 설정해 활성화합니다.
- **document block** - PDF를 base64, URL 또는 file_id로 전송할 때 사용하는 콘텐츠 블록입니다.
