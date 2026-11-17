"""Step 7: write output/REPORT.md from the stats files."""
import json
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; W = ROOT / "work"
A = json.loads((W / "assemble_stats.json").read_text())["per_exam"]
D = json.loads((W / "dedup_stats.json").read_text())
C = json.loads((W / "check_report.json").read_text())
REJ = json.loads((W / "rejected.json").read_text())
REV = json.loads((W / "review_needed.json").read_text())
NEAR = json.loads((W / "near_duplicates.json").read_text())
SK = json.loads((W / "jobs.json").read_text())["skipped"]
E = list(A)
L = ["# 문제 통합 보고서", "",
     "원본 파일은 수정하지 않았고, 문제·보기·정답·해설은 원본 그대로입니다. 섹션은 각 시험의 공식 exam-guide.pdf (`work/domains/<시험코드>/domains.json`) 기준입니다.", "",
     "## 1. 시험별 요약", "",
     "| 시험 | 추출 | 제외(검사 실패) | 중복 제거 | 최종 문제 수 | 원본 섹션 표기 사용 | classifier 분류 | 검토 필요 |",
     "|---|---:|---:|---:|---:|---:|---:|---:|"]
rc = Counter(r["exam"] for r in REJ); vc = Counter(r["exam"] for r in REV)
for e in E:
    a = A[e]; cl = a["classified"]
    L.append(f"| {e} | {D[e]['before'] + rc[e]} | {rc[e]} | {D[e]['removed']} | {a['total']} | {a['from_source']} | {sum(cl.values())} (high {cl['high']} / medium {cl['medium']} / low {cl['low']}) | {vc[e]} |")
t = lambda k: sum(D[e][k] for e in E)
L.append(f"| **합계** | {t('before') + len(REJ)} | {len(REJ)} | {t('removed')} | {sum(A[e]['total'] for e in E)} | {sum(A[e]['from_source'] for e in E)} | {sum(sum(A[e]['classified'].values()) for e in E)} | {len(REV)} |")
L += ["", "## 2. 섹션별 문제 수", ""]
for e in E:
    L += [f"### {e}", "", "| 섹션 | 공식 비중 | 문제 수 | 비율 |", "|---|---:|---:|---:|"]
    for s, n in A[e]["sections"].items():
        L.append(f"| {s} | {A[e]['weights'][s]} | {n} | {n / A[e]['total']:.0%} |")
    L.append("")
L += ["## 3. 제외된 문제 (`work/rejected.json`)", ""]
if REJ:
    L += ["| 이유 | 개수 |", "|---|---:|"] + [f"| {k} | {v} |" for k, v in Counter(x for r in REJ for x in r["reasons"]).items()]
else:
    L.append("0개. 모든 문제가 검사(본문 있음, 보기 2개 이상, 정답이 보기 안에 있음, 정답 수 = select_count)를 통과했습니다.")
L += ["", "## 4. 중복", "",
      f"- 본문을 정리(공백·대소문자·기호 제거)해 같으면 중복으로 보고 1개만 남겼습니다. 나머지 출처는 `also_in` 필드에 있습니다. 제거: **{t('removed')}개**.",
      "- 본문이 같아도 보기가 다르면 다른 문제로 보고 남깁니다.",
      f"- 비슷하지만 같지 않은 문제(유사도 0.85 이상): **{len(NEAR)}쌍** (`work/near_duplicates.json`).",
      "- 중복이 많은 이유: 같은 레포 안에서 md 와 json 이 같은 문제를 담고 있음 (Amey-Thakur md ↔ question-bank.json, preporato md ↔ practice/*.json, raybeecham 모듈 퀴즈 ↔ practice-exam-01/02 ↔ data/questions.json).", "",
      "## 5. 검토가 필요한 문제 (`work/review_needed.json`)", "",
      "| ID | 이유 |", "|---|---|"]
L += [f"| {r['id']} | {r['reason']} |" for r in REV]
L += ["", "## 6. 건너뛴 파일 / 섹션", "", "| 파일 | 이유 |", "|---|---|"]
L += [f"| {s['file']} | {s['reason']} |" for s in SK]
L += ["| CCAO-F/raybeecham__practice-exam-0N-answers.md (3개) | 따로 추출하지 않음 — 문제 파일과 짝지어 정답·해설을 가져옴 |",
      "| 학습 노트·요약만 있는 파일 | 해당 없음 (시험 폴더에는 문제 파일만 있음) |"]
L += ["", "## 7. 원본 파일별 문제 수 비교", "", "| 원본 파일 | 원본 문제 수 | 추출된 문제 수 | 일치 |", "|---|---:|---:|---|"]
L += [f"| {f['file']} | {f['original_count']} | {f['extracted_count']} | {'✅' if f['match'] else '❌'} |" for f in C["files"]]
L += ["", "## 8. 처리 방식 메모", "",
      "- `.claude/agents/extractor.md`, `classifier.md` 를 만들었지만 실행 중인 세션에는 등록되지 않아, 같은 지침을 프롬프트에 넣고 지정 모델(extractor = haiku, classifier = sonnet)로 실행했습니다. 다음 세션부터는 이름으로 바로 쓸 수 있습니다.",
      "- JSON 파일 9개는 Python 으로 변환했습니다 (`work/scripts/convert_json.py`). preporato CCA-F JSON 은 시나리오 지문이 별도 필드라서 문제 본문 앞에 붙였습니다 (md 판과 같은 형태).",
      "- 큰 HTML (paullarionov, jrajath94) 은 문제 경계에서 조각내어 조각마다 extractor 1개씩 맡긴 뒤 합쳤습니다 (`work/chunks/`, 줄바꿈만 추가).",
      "- 검사: 개수 비교 + 문제·보기 문장이 원본에 그대로 있는지 확인. 원본과 다르게 옮긴 조각 5개는 extractor 에게 다시 맡겨 고쳤습니다. HTML 769문제의 정답을 원본에서 정규식으로 뽑은 정답과 대조해 모두 일치했습니다 (`work/answer_crosscheck.json`, 자동 추출이 안 된 2개는 직접 확인).",
      "- 원본 섹션 표기는 **이름**으로 공식 섹션에 맞췄습니다 (번호는 쓰지 않음). 예: raybeecham 모듈 1 'Claude Platform & Model Foundations' → 3. Product and Model Selection, preporato `d1` → 해당 이름의 공식 섹션, jrajath94 `D3`/`V2-D3.x` → 레포 자체 범례의 이름(D3. Integration) → 3. Integration.",
      "- `domain_confidence`: 원본 표기를 쓴 문제는 `source`, classifier 가 분류한 문제는 `high`/`medium`/`low`.",
      "- preporato JSON 출처 문제의 해설에 있는 `{a}` 같은 표기는 원본 그대로입니다 (원본 빌드 스크립트가 보기 기호로 바꾸는 자리표시)."]
(ROOT / "output/REPORT.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print("\n".join(L[:20]))
