# 11장(신규) — writer 공통 지시

11장 "Solution Design & Stakeholder Communication"을 새로 만든다. 155문항을 2명이 나눠 쓴다. 너는 `w{N}.json` 하나를 맡는다.

## 담당 주제 (소절이 겹치지 않게)
- w1 (CCAR-P D1 Solution Design & Architecture, 53문항): 문제 적합성 판단(Claude가 맞는/안 맞는 문제), discovery·요구사항(functional·non-functional·제약), end-to-end 아키텍처, 아키텍처 패턴 선택 기준, decomposition
- w2 (CCAR-P D6 Stakeholder Communication & Lifecycle, 102문항): business value·ROI, trade-off·결정을 청중별로 전달, 기대치·SLA·피드백 루프, 문서화·handoff, lifecycle(discovery→design→handoff→monitoring→iteration), 이해관계자 커뮤니케이션
- 네 문항이 상대 담당 주제에 더 맞아 보여도 버리지 말고 네 파일 안 가장 가까운 소절에 넣는다.

## 먼저 읽을 것
1. `.claude/rules/knowbook-style.md` (R1~R12)
2. `reference/knowbook_outline.md`의 "11장" 목차 초안 (11.1~11.10)
3. 형식 참고: `output/Know(CCAR-F&P)/10_Reliability_Escalation_and_Oversight.md`
4. 네 입력 `work/knowbook/ch11/w{N}.json` (필드 id, q, ch(선택지), answer, ex)

## 쓸 것: `work/knowbook/ch11/part{N}.md` 하나 (다른 파일은 건드리지 않는다)
블록 헤더를 정확히 이 문자열로 쓴다:
```
@@ NEW-SECTION
### <소제목>        ← 번호 없이. 나중에 1.N 번호가 자동으로 붙는다
**핵심 한 줄**
(표)
<sub>근거: ...</sub>

@@ RULES   ("상황 | 정답" 표의 행만, 머리 없이)
<sub>근거: ...</sub>
@@ TRAPS   ("오답 | 이유" 행만)
<sub>근거: ...</sub>
@@ MEMO    ("이름 | 의미" 행만)
<sub>근거: ...</sub>
@@ CHECK   (`- [ ]` 항목 3~6개)
<sub>근거: ...</sub>
```
- NEW-SECTION은 6~12개. 문항이 많은 주제는 나눈다.
- 그림 줄(`![...]`)은 쓰지 않는다.
- 문항 정답·해설이 뒷받침하는 지식만 쓴다. 문제를 옮겨 적지 말고, 처음 보는 문제에도 쓸 수 있게 일반화한다.
- 해설이 공식 문서와 어긋나 보이면 그 행에 `⚠️` + 이유 한 줄.

## 근거 규칙
- id는 JSON의 `id` 그대로(예: `CCAR-P-jrajath94-0084`), `<sub>근거: ...</sub>` 줄에만.
- 입력 문항은 모두 한 번 이상 인용. 끝나면 python3 -I로 입력 id가 part 파일에 전부 있는지 대조.

## 보고
NEW-SECTION 소제목 목록, 인용 id 수/입력 id 수, ⚠️ 개수만 짧게.
