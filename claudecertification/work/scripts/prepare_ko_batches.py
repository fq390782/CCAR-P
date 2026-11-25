#!/usr/bin/env python3
"""한국어 번역 배치 준비.
 EN->KO : 영어 원문 문제(pq=True) 전체(문제·보기·해설)      -> work/translate/ko/in/en-NNN.json
 JA->KO : 일본어 Udemy 문제(px=True)의 해설(+보기별 해설)     -> work/translate/ko/in/ja-NNN.json
이미 work/translate/ko/out/ 에 번역이 있는 id 는 제외한다(재실행해도 안전)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output"
TR = ROOT / "work/translate/ko"
(TR / "in").mkdir(parents=True, exist_ok=True)
(TR / "out").mkdir(parents=True, exist_ok=True)

done = set()
for f in (TR / "out").glob("*.json"):
    try:
        done |= {r["id"] for r in json.load(open(f, encoding="utf-8"))}
    except Exception:
        pass

en_items, ja_items = [], []
for ex in ("CCAO-F", "CCAR-F", "CCAR-P", "CCDV-F"):
    for r in json.load(open(OUT / ex / "20_gold/all.json", encoding="utf-8")):
        if r["id"] in done:
            continue
        if r["origin"] == "en" and r.get("pq"):
            en_items.append({"id": r["id"], "question": r["q"], "choices": r["ch"], "explanation": r["ex"]})
        elif r["origin"] == "ja" and r["px"]:
            it = {"id": r["id"], "question": r["q"], "choices": r["ch"], "explanation": r["ex"]}
            if r.get("ce"):
                it["choice_explanations"] = r["ce"]
            ja_items.append(it)

def size(it):
    return len(json.dumps(it, ensure_ascii=False))

def batches(items, budget):
    cur, n, out = [], 0, []
    for it in items:
        s = size(it)
        if cur and n + s > budget:
            out.append(cur); cur, n = [], 0
        cur.append(it); n += s
    if cur:
        out.append(cur)
    return out

manifest = []
for kind, items, budget in (("en", en_items, 32000), ("ja", ja_items, 17000)):
    for i, b in enumerate(batches(items, budget), 1):
        name = f"{kind}-{i:03d}"
        (TR / "in" / f"{name}.json").write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
        manifest.append({"name": name, "kind": kind, "count": len(b), "in": f"work/translate/ko/in/{name}.json", "out": f"work/translate/ko/out/{name}.json"})
(TR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"EN->KO {len(en_items)}문제, JA->KO {len(ja_items)}문제 -> 배치 {len(manifest)}개 (이미 번역됨: {len(done)})")
