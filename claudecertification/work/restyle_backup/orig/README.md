# CCDV-F 반드시 알아야 할 지식 (도메인별)

`output/CCDV-F/Question`의 207문항(정답과 해설)에서 시험 가이드 8개 도메인별로 꼭 알아야 할 지식을 뽑아 정리했습니다.
- 출처: Amey-Thakur 80, PatrickWiloak 44, preporato 30, Udemy 53
- Udemy 53문항은 원본에 도메인이 없어서 새로 분류했습니다. 결과는 `udemy_domain_map.json`에 있고, 이 중 19문항은 분류 확신도가 낮음(low)입니다.

## 학습 순서 (시험 비중순)

| 비중 | 문항 | 도메인 | 파일 | 근거 문항 | ⚠️ |
|---|---|---|---|---|---|
| 33% | 10 | Applications and Integration | [2_Applications_and_Integration.md](2_Applications_and_Integration.md) | 65 | 3건 |
| 17% | 5 | Model Selection and Optimization | [5_Model_Selection_and_Optimization.md](5_Model_Selection_and_Optimization.md) | 28 | 8건 |
| 15% | 4 | Agents and Workflows | [1_Agents_and_Workflows.md](1_Agents_and_Workflows.md) | 27 | 2건 |
| 11% | 3 | Prompt and Context Engineering | [6_Prompt_and_Context_Engineering.md](6_Prompt_and_Context_Engineering.md) | 23 | 1건 |
| 10% | 3 | Tools and MCPs | [8_Tools_and_MCPs.md](8_Tools_and_MCPs.md) | 21 | 1건 |
| 8% | 3 | Security and Safety | [7_Security_and_Safety.md](7_Security_and_Safety.md) | 17 | 0건 |
| 3% | 1 | Claude Code | [3_Claude_Code.md](3_Claude_Code.md) | 10 | 2건 |
| 3% | 1 | Eval, Testing, and Debugging | [4_Eval_Testing_and_Debugging.md](4_Eval_Testing_and_Debugging.md) | 16 | 3건 |

## 파일 구성

모든 파일은 같은 다섯 장으로 되어 있습니다.
1. 핵심 개념
2. 상황별 정답 판단 규칙 (표)
3. 자주 나오는 오답 함정
4. 암기 목록
5. 시험 직전 체크리스트

- **그림**: workflow, flowchart, dataflow, decision tree, sequence, before/after 비교 등 흐름이나 패턴이 있는 부분마다 `svg/` 폴더의 그림 107개를 넣었습니다. 2장 판단 규칙 표 아래에는 같은 내용을 decision tree로 그린 그림이 있습니다. 색 규칙은 다음과 같습니다.
  - 파랑: 정답/권장
  - 빨강: 오답/안티패턴
  - 노랑 마름모: 판단 분기
  - 초록: 종료/성공
- **근거 표기**: bullet 끝의 `[Amey-0004]`, `[Patrick-0038]`, `[Preporato-0030]`, `[Udemy-0012]`는 문항 id에서 `CCDV-F-`를 떼고 출처 이름을 줄인 것입니다. 207문항이 모두 한 번 이상 인용됩니다.
- **⚠️ 표시**: 문항 해설이 공식 Anthropic 문서와 어긋나 보이거나, 모델 버전·가격처럼 시점에 따라 바뀌는 내용입니다. 시험 전에 공식 문서로 다시 확인하세요.

## 멀티에이전트: coordinator 1개 + subagent n개

- 정리하는 내용으로서: `1_Agents_and_Workflows.md`의 1.3절이 이 구조를 다룹니다. coordinator와 subagent가 각각 맡는 역할, subagent에게 넘길 것과 넘기지 말 것, 단일 에이전트나 workflow가 더 나은 경우를 정리했습니다.
- 이 자료를 만든 방식으로서: coordinator 1개가 Udemy 문항 분류(classifier subagent 1개)와 도메인별 문항 분할을 맡았습니다. 이어서 도메인 subagent 8개가 병렬로 각 파일을 작성했고, coordinator가 검수했습니다. 검수 내용은 누락된 문항 인용, id 표기 통일, 빠진 ⚠️ 보완입니다.
