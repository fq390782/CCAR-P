# Claude 자격증 학습 자료

Claude 자격증 연습문제를 모아 문제은행과 개념서를 만든다.
- 시험: CCAO-F · CCDV-F · CCAR-F · CCAR-P (CCDV-P는 가이드 미공개, 다루지 않음)
- git 저장소가 아니다. 되돌릴 수단이 없으므로 파일을 지우거나 덮어쓰기 전에 사용자에게 확인한다.

## 폴더
| 폴더 | 용도 | 수정 |
|---|---|---|
| `reference/` | 기준 자료: `exams/{시험}/domains.json`, `chapter_map.json`, `knowbook_outline.md` | 사용자 확인 후에만 |
| `reference/history/` | 과거 작업의 프롬프트 원문 (기록용, 경로가 옛 위치를 가리킴) | 금지 |
| `_repos/`, `docs/doc(data)/` | 원본 문제 자료 | 금지 (읽기 전용) |
| `output/{시험}/` | 시험별 문항: `00_bronze`(생데이터) → `10_silver`(전처리 중) → `20_gold/all.json`(최종) | 스크립트로만 |
| `output/CCTOTALQA/` | 문제은행 `question_bank.html` | `work/scripts/build_bank.py`로만 |
| `output/Know(CCDV-F)/` | 개념서(CCDV-F 기준 원본): 장별 md + `svg/` | 아래 "개념서" 참조 |
| `output/Know(CCAR-F&P)/` | 개념서(CCAR-F·CCAR-P 보강판): `Know(CCDV-F)`를 복사한 것 | 아래 "개념서" 참조 |
| `work/scripts/` | 빌드·검사 스크립트 | 자유 |
| `work/` (그 밖) | 중간 산출물 | 자유 |

## 사실의 출처
- 도메인 이름과 비중은 `reference/exams/{시험}/domains.json`에서만 읽는다. 기억으로 쓰지 않는다.
- 문항은 `output/{시험}/20_gold/all.json`이 최신이다. `work/valid/`는 예전 파이프라인의 산출물이라 개수가 다르다.
- 시험 도메인과 개념서 장의 연결은 `reference/chapter_map.json`이 기준이다.
- Claude의 기능·API·Claude Code 동작에 대한 사실은 공식 문서가 기준이다. 목차(llms.txt)에서 해당 페이지를 찾아 읽고 확인한다. 기억으로 판단하지 않는다. 내려받아 두지 않고 매번 새로 읽는다.
  - Claude API·플랫폼: https://platform.claude.com/llms.txt
  - Claude Code·Agent SDK: https://code.claude.com/docs/llms.txt
- 설계 문서: 문제은행은 `docs/superpowers/specs/`, 개념서는 `reference/knowbook_outline.md`.

## 개념서 (output/Know(CCDV-F), output/Know(CCAR-F&P))
- 11개 장으로 구성한다. 1~8장은 CCDV-F 기준으로 완성, 9~11장은 미작성이다. 상태와 남은 일은 `reference/knowbook_outline.md`에 있다.
- `output/Know(CCAR-F&P)`는 `Know(CCDV-F)`를 바탕으로 만든 보강판이다. 기존 내용은 지우지 않고, CCAR-F·CCAR-P 문항에서 찾은 패턴을 글로 덧붙인다. Foundation과 Professional을 모두 커버해야 한다. 보강이 끝나면 공식 문서(llms.txt)로 내용을 검증한다.
- 장을 새로 만들거나 다른 시험 내용을 보강할 때는 `knowbook-chapter` skill을 쓴다.
- 문체 규칙(`.claude/rules/knowbook-style.md`)과 SVG 규칙(`.claude/rules/knowbook-svg.md`)은 해당 파일을 다룰 때 적용된다.
- 모든 지식에는 근거 문항 id를 단다. 문항에 없는 내용은 쓰지 않는다.
- 해설이 공식 Anthropic 문서와 어긋나 보이면 지우지 말고 ⚠️와 이유 한 줄을 남긴다.
- 기존 장을 고친 뒤의 완료 기준: `python3 -I work/scripts/check_knowbook.py <수정 전> <수정 후>`가 PASS.

## 작업 방식
- 문항 수십 개 이상을 읽거나 쓰는 작업은 subagent에게 나눠 맡긴다: `extractor`, `classifier`, `knowledge-writer`, `svg-drawer`.
- 글을 쓴 subagent와 검증하는 subagent는 따로 둔다.
- 기술 용어·파일명·설정 키는 영어 원문, 설명은 한국어로 쓴다.
- 스크립트는 `work/scripts/` 위치를 기준으로 프로젝트 루트를 찾는다(`parents[2]`). 이 폴더를 옮기면 전부 깨진다.
