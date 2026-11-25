#!/usr/bin/env python3
"""ja2ko 번역 비교표: 일본어 원문 / 영어 참고 / 한국어 번역. 사용: compare_ja2ko.py [배치명...] -> work/translate/ja2ko/compare.md"""
import json, sys
from pathlib import Path
D = Path(__file__).resolve().parents[2] / "work/translate/ja2ko"
names = sys.argv[1:] or sorted(p.stem for p in (D / "out").glob("j*.json"))
o = []
for n in names:
    src = {x["id"]: x for x in json.load(open(D / "in" / f"{n}.json", encoding="utf-8"))}
    for y in json.load(open(D / "out" / f"{n}.json", encoding="utf-8")):
        x = src[y["id"]]
        o.append(f"## {y['id']}\n\n**JA** {x['question']}\n\n**KO** {y['question']}\n")
        for k in y["choices"]:
            o.append(f"- {k}. JA: {x['choices'][k]}\n  - KO: {y['choices'][k]}\n  - EN: {x['en_choices'].get(k, '')}")
        if y.get("notes"): o.append(f"\n> notes: {y['notes']}")
        o.append("")
(D / "compare.md").write_text("\n".join(o), encoding="utf-8")
print(len(names), "배치 ->", D / "compare.md")
