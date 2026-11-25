---
paths:
  - "output/Know*/svg/**"
---

# 개념서 SVG 그림 규칙

## 무엇을 그리나
- 대상: workflow, flowchart, dataflow, decision tree, sequence(요청과 응답 왕복), state transition, 아키텍처 비교(before/after, 옵션 A와 B), 계층·범위 구조.
- 단순 나열이나 정의뿐이고 흐름이 없는 내용은 그리지 않는다.
- "2. 상황별 정답 판단 규칙" 표는 같은 주제끼리 묶어 decision tree 1~3개로 만든다.
- 그림 하나에는 주장 하나만 담는다. 이름만 적은 상자가 아니라 메커니즘을 그린다(무엇이 어디로 흐르는지, 어떤 경계를 넘는지, 옵션끼리 무엇이 다른지).
- 화살표에는 라벨을 붙인다(예: `tool_use`, `요약만 반환`, `429 → backoff`).
- 내용은 md 파일에 이미 적힌 지식만 사용한다. 새 사실을 지어내지 않는다.

## 파일과 삽입
- 저장 위치: 담당 md 파일과 같은 폴더의 `svg/` (예: `output/Know(CCAR-F&P)/svg/`)
- 파일 이름: `{장번호}-{짧은-영문-slug}.svg` (예: `1-coordinator-subagents.svg`)
- md 파일에서는 그림이 설명하는 소절(### 제목) 내용 바로 아래, 또는 2장 표 바로 아래에 다음 형식으로 넣는다.
  ```
  ![그림 설명 한 문장](svg/1-coordinator-subagents.svg)
  *그림: 그림이 보여 주는 주장 한 문장*
  ```
- 그림을 넣을 때 기존 본문은 지우거나 바꾸지 않는다.

## SVG 형식 (모든 파일에서 통일)
- 루트: `<svg xmlns="http://www.w3.org/2000/svg" width="W" height="H" viewBox="0 0 W H" role="img" aria-label="...">`. W는 640~960. `<title>`도 넣는다.
- 첫 요소는 `<rect width="100%" height="100%" fill="#FFFFFF"/>`. 다크 모드 뷰어에서도 읽히게 하려는 것이다.
- `<script>`, `<style>`, `<foreignObject>`, 외부 이미지, 외부 폰트는 쓰지 않는다. 속성(attribute)으로만 스타일을 지정한다.
- 폰트: `font-family="Apple SD Gothic Neo, Noto Sans KR, Malgun Gothic, sans-serif"`. 라벨 13px, 소제목 14px bold, 보조 설명 11px.
- 색상 팔레트 (이 외의 색은 쓰지 않는다):

| 용도 | fill | stroke |
|---|---|---|
| 기본 텍스트와 선 | `#1F2937` | – |
| 보조 텍스트 | `#6B7280` | – |
| 일반 상자 | `#F3F4F6` | `#9CA3AF` |
| 권장/정답 경로 | `#DBEAFE` | `#2563EB` |
| 오답/안티패턴 | `#FEE2E2` | `#DC2626` |
| 판단 분기(마름모) | `#FEF3C7` | `#D97706` |
| 성공/종료 | `#DCFCE7` | `#16A34A` |

- 상자: `rx="6"`, stroke-width 1.5. 그리드에 맞춰 정렬하고 간격은 일정하게 둔다.
- 화살표: `<defs><marker id="arr-{slug}" ...>`. id는 파일마다 고유하게 짓는다.
- 점선(`stroke-dasharray="5 4"`)은 선택적이거나 비동기적인 흐름에만 쓴다. 점선을 쓰는 그림에는 범례를 단다.
- 텍스트가 상자를 넘치지 않게 한다. 폭은 13px 기준으로 한글 한 글자 약 13px, 영문·숫자 한 글자 약 7.5px로 계산한다. 긴 라벨은 `<tspan x=".." dy="16">`로 줄바꿈한다.
- 영어 용어(API 이름, 파라미터)는 원문 그대로, 설명은 한국어로 쓴다.

## 검증 (반드시 수행)
1. `xmllint --noout 파일.svg`로 오류가 없는지 확인한다.
2. `qlmanage -t -s 1000 -o <scratchpad의 render 폴더> 파일.svg`로 PNG를 만들고, Read 도구로 PNG를 열어 직접 본다.
   - 확인할 것: 글자가 상자를 넘치는지, 요소가 겹치는지, 화살표가 엉뚱한 곳을 가리키는지, 잘린 부분이 있는지.
   - 문제가 있으면 고친 뒤 다시 렌더링한다.
3. md 파일에서 `![`로 참조한 svg 파일이 모두 존재하는지 확인한다.
