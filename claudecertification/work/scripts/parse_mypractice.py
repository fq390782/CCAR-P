#!/usr/bin/env python3
"""docs/doc(data)/CCAR-F/fq390782__MyPractice.md -> output/CCAR-F/00_bronze/MyPractice.json (76문제).
한국어 본문 + EN/JA 병기. 구조가 어긋나면 assert 로 멈춘다."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "docs/doc(data)/CCAR-F/fq390782__MyPractice.md"
DST = ROOT / "output/CCAR-F/00_bronze/MyPractice.json"

strip_b = lambda t: re.sub(r"^\*\*|\*\*$", "", t.strip()).strip()

def section(txt, start, end):
    """start 마커 뒤 ~ end 마커 앞 (마커 줄의 나머지 텍스트 포함)."""
    i = txt.index(start) + len(start)
    j = txt.index(end, i) if end else len(txt)
    return txt[i:j].strip()

out = []
for blk in re.split(r"\n---\n", SRC.read_text(encoding="utf-8")):
    m = re.search(r"^## 문제 *(\d+)\s*\((.*?)\)\s*$", blk, re.M)
    if not m:
        assert "- A)" not in blk, "질문 같은 블록이 헤더 없이 있음: " + blk[:60]
        continue
    n, scenario = int(m.group(1)), re.sub(r"^시나리오:\s*", "", m.group(2))
    sit_ko = section(blk, "**상황:**", "**[EN] Situation:**")
    sit_en = section(blk, "**[EN] Situation:**", "**[JA] 状況:**")
    sit_ja = section(blk, "**[JA] 状況:**", None)
    # JA 상황 이후 ~ 첫 보기 전: (메모) + 질문 줄 ko/en/ja
    mid_start = blk.index("**[JA] 状況:**")
    mid = blk[mid_start: blk.index("\n- A)")]
    mid = mid.split("\n", 1)[1] if "\n" in mid else ""
    sit_ja = sit_ja.split("\n")[0].strip()   # JA 상황 본문은 한 줄
    lines = [l for l in mid.split("\n") if l.strip()]
    q_ko = q_en = q_ja = None
    note = []
    for l in lines:
        if l.startswith("**[EN]"):
            q_en = strip_b(re.sub(r"^\*\*\[EN\]\s*", "**", l))
        elif l.startswith("**[JA]"):
            q_ja = strip_b(re.sub(r"^\*\*\[JA\]\s*", "**", l))
        elif l.startswith("**답"):
            note.append(l)
        elif l.startswith("**") and q_ko is None:
            q_ko = strip_b(l)
        else:
            note.append(l)
    assert q_ko and q_en, (n, "질문 줄 없음")
    # 보기
    ch, ans = {}, []
    for k, t in re.findall(r"^- ([A-E])\) (.*)$", blk, re.M):
        if t.rstrip().endswith("**[정답]**"):
            ans.append(k)
            t = t.rstrip()[: -len("**[정답]**")].rstrip()
        ch[k] = t
    assert len(ch) == 4 and len(ans) == 1, (n, ch.keys(), ans)
    # 해설
    mex = re.search(r"\*\*([A-E])인 이유:\*\*", blk)
    assert mex and mex.group(1) == ans[0], (n, "해설 정답 불일치", ans)
    ex_ko = section(blk, mex.group(0), "**[EN] Why")
    ex_en = re.search(r"\*\*\[EN\] Why [A-E]:\*\*\s*(.*?)\n\n\*\*\[JA\]", blk, re.S)
    ex_ja = re.search(r"\*\*\[JA\][^*]*:\*\*\s*(.*)$", blk.split("**[EN] Why")[1], re.S)
    assert ex_en and ex_ja, (n, "EN/JA 해설")
    out.append({
        "id": f"CCAR-F-MyPractice-{n:04d}", "exam": "CCAR-F", "source_repo": "MyPractice (fq390782)",
        "source_file": "MyPractice.md", "source_number": n, "scenario": scenario,
        "question": sit_ko + "\n\n" + q_ko, "question_en": sit_en + "\n\n" + q_en,
        "question_ja": sit_ja + "\n\n" + (q_ja or ""),
        "choices": ch, "answer": ans, "select_count": 1,
        "explanation": ex_ko, "explanation_en": ex_en.group(1).strip(), "explanation_ja": ex_ja.group(1).strip(),
        "memo": "\n".join(note) or None,
        "domain": None,
    })

nums = [r["source_number"] for r in out]
assert len(out) == 76 and len(set(nums)) == 76, (len(out), sorted(nums)[:5])
DST.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(out), "문제 ->", DST)
