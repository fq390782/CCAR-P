#!/usr/bin/env python3
"""일본어 Udemy 문제(en 병기가 없는 것) -> 영어 번역 배치. work/translate/en/in/en-NNN.json
이미 work/translate/en/out/ 에 번역된 id 는 제외한다."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TR = ROOT / "work/translate/en"
(TR / "in").mkdir(parents=True, exist_ok=True)
(TR / "out").mkdir(parents=True, exist_ok=True)
done = set()
for f in (TR / "out").glob("*.json"):
    try:
        done |= {r["id"] for r in json.load(open(f, encoding="utf-8"))}
    except Exception:
        pass
items = []
for ex in ("CCAO-F", "CCAR-F", "CCAR-P", "CCDV-F"):
    for r in json.load(open(ROOT / "output" / ex / "20_gold/all.json", encoding="utf-8")):
        if r["origin"] == "ja" and not r.get("en") and r["id"] not in done:
            items.append({"id": r["id"], "question": r["q"], "choices": r["ch"]})
size = lambda it: len(json.dumps(it, ensure_ascii=False))
batches, cur, n = [], [], 0
for it in items:
    if cur and n + size(it) > 15000:
        batches.append(cur); cur, n = [], 0
    cur.append(it); n += size(it)
if cur:
    batches.append(cur)
man = []
for i, b in enumerate(batches, 1):
    name = f"en-{i:03d}"
    (TR / "in" / f"{name}.json").write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
    man.append([name, len(b)])
(TR / "manifest.json").write_text(json.dumps(man), encoding="utf-8")
print(f"JA->EN {len(items)}문제 -> 배치 {len(batches)}개 (이미 번역됨 {len(done)})")
print(json.dumps(man, separators=(",", ":")))
