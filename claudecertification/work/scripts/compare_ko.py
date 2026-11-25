#!/usr/bin/env python3
"""ko_v2 번역 vs 기존(gold) 번역 비교표. 사용: compare_ko.py pilot  -> work/translate/ko_v2/pilot_compare.md"""
import json, sys
from pathlib import Path
R = Path(__file__).resolve().parents[2]; name = sys.argv[1]
new = json.load(open(R / f"work/translate/ko_v2/out/{name}.json", encoding="utf-8"))
gold = {x["id"]: x for x in json.load(open(R / "output/CCAR-F/20_gold/all.json", encoding="utf-8"))}
sil = {x["id"]: x for x in json.load(open(R / "output/CCAR-F/10_silver/all.json", encoding="utf-8"))}
o = []
for n in new:
    i = n["id"]; g = gold[i]; s = sil[i]
    o.append(f"## {i}\n\n**EN** {s['question']}\n\n**기존** {g['q']}\n\n**신규** {n['question']}\n")
    for k in n["choices"]:
        o.append(f"- {k}. 기존: {g['ch'][k]}\n  - 신규: {n['choices'][k]}")
    o.append(f"\n**해설 EN** {s['explanation']}\n\n**해설 기존** {g['ex']}\n\n**해설 신규** {n['explanation']}\n")
    if n.get("notes"): o.append(f"> notes: {n['notes']}\n")
(R / f"work/translate/ko_v2/{name}_compare.md").write_text("\n".join(o), encoding="utf-8")
print(len(new), "문항 ->", f"work/translate/ko_v2/{name}_compare.md")
