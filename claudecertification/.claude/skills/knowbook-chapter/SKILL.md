---
name: knowbook-chapter
description: 개념서(output/Know(CCAR-F&P))의 장을 새로 만들거나, 기존 장에 다른 시험의 문항을 반영해 보강할 때 쓰는 절차. "9장 만들어줘", "3장에 CCAR-F 내용 보강해줘" 같은 요청에 사용한다.
---

# 개념서 장 만들기 · 보강하기

너는 coordinator다. 문항 읽기와 글쓰기는 subagent에게 맡기고, 너는 나누고 검사한다.

## 대상 폴더
- 작업 대상은 `output/Know(CCAR-F&P)`다. 아래에서 `{KB}`는 이 폴더를 뜻한다. 이 폴더는 CCDV-F 내용 위에 CCAR-F·CCAR-P 문항의 지식을 덧붙여, Foundation과 Professional을 모두 커버하는 것이 목표다.
- `output/Know(CCDV-F)`는 CCDV-F 기준 원본이다. 사용자가 이 폴더를 직접 지목한 경우에만 고친다. 그때는 `{KB}`를 이 폴더로 읽는다.
- 폴더 이름에 `(`, `)`, `&`가 있으므로 shell 명령에서는 경로를 항상 작은따옴표로 감싼다.
- subagent를 띄울 때는 md 경로를 `{KB}`가 풀린 전체 경로로 넘긴다.

## 0. 기준 확인
- `reference/chapter_map.json`: 이 장에 들어오는 시험 도메인
- `reference/knowbook_outline.md`: 장 상태, 남은 일, 소절 목차 초안
- 기존 장 하나(예: `{KB}/7_Security_and_Safety.md`)를 열어 형식을 확인한다.

## 1. 문항 모으기
- 출처는 `output/{시험}/20_gold/all.json`이다. `domain` 값이 `chapter_map.json`의 키와 같은 문자열이다.
- 이 장으로 오는 도메인의 문항을 모아 `work/knowbook/ch{N}.json`에 저장한다. 필드는 `id`, `exam`, `domain`, `q`, `ch`, `answer`, `ex`만 남긴다.
- 도메인 하나가 여러 장에 걸친 경우(map 배열의 길이가 2 이상)는 `classifier` subagent에게 30문항씩 맡겨 후보 장 중 하나를 고르게 한다. 후보는 map 배열에 있는 장뿐이다.
- CCAR-F의 `미분류` 문항은 먼저 `reference/exams/CCAR-F/domains.json` 기준으로 분류해야 쓸 수 있다.
- 모은 문항이 20개 미만이면 멈추고 사용자에게 알린다. 근거가 부족한 장은 지어내게 된다.

## 2. 초안 쓰기
- `knowledge-writer` subagent 1개에 장 번호와 제목, 입력 JSON, 출력 경로, 커버 도메인을 넘긴다.
- 문항이 150개를 넘으면 소절 묶음별로 나눠 여러 개를 병렬로 띄우고, 각자 임시 파일에 쓰게 한 뒤 합친다.
- 기존 장 보강: 먼저 `{KB}`의 현재 파일을 `work/knowbook/orig/`에 복사한다. 같은 이름의 파일이 이미 있으면 덮어쓰기 전에 사용자에게 확인한다. writer에게는 "기존 내용과 근거 id는 그대로 두고, 새 문항의 지식만 해당 소절에 더하거나 새 소절로 추가한다"고 지시한다.

## 3. 그림 넣기
- `svg-drawer` subagent에 md 경로와 장 번호를 넘긴다.
- 초안의 소절을 보고 "반드시 그릴 후보"를 3~8개 적어 준다.

## 4. 검사
- 보강한 경우: `python3 -I work/scripts/check_knowbook.py work/knowbook/orig/{파일} '{KB}/{파일}'`이 PASS여야 한다. 기존 근거 id, ⚠️, 그림 줄이 빠지지 않았는지 확인하는 검사다. 새 id가 추가됐다는 FAIL(R10 new ids)은 보강에서는 정상이므로, 그 한 줄만 남았는지 확인한다.
- 새 장: 입력 JSON의 모든 id가 md에 한 번 이상 나오는지 직접 대조한다.
- 글을 쓴 subagent가 아닌 새 subagent에게 사실 검증을 맡긴다. 지시: "입력 문항의 정답·해설과 md를 대조해, md에 있지만 문항에 근거가 없는 주장과 의미가 바뀐 주장을 찾는다. 파일은 고치지 않는다."
- 문체는 `.claude/rules/knowbook-style.md`의 R1~R9를 기준으로 본다.

## 5. 마무리
- 장 제목 아래 `> 커버: ...` 줄이 `chapter_map.json`과 맞는지 확인한다.
- `{KB}/README.md`의 장 표와 `reference/knowbook_outline.md`의 상태 열을 갱신한다.
- 사용자에게 보고: 근거 문항 수, 소절 목록, ⚠️ 개수, 검증에서 나온 문제와 처리 결과.
