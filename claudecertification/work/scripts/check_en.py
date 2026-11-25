#!/usr/bin/env python3
"""work/translate/en/out/*.json 검증 (일본어->영어). 문제 배치는 out/_bad/ 로 이동(--keep 이면 이동 안 함)."""
import json, re, sys
from pathlib import Path
TR = Path(__file__).resolve().parents[2] / "work/translate/en"
kana = lambda s: len(re.findall(r"[ぁ-んァ-ン]", s))
latin = lambda s: len(re.findall(r"[A-Za-z]", s))
def check(name):
    inp = json.load(open(TR / "in" / f"{name}.json", encoding="utf-8"))
    try:
        out = json.load(open(TR / "out" / f"{name}.json", encoding="utf-8"))
    except Exception as e:
        return [f"invalid JSON: {e}"]
    if [r.get("id") for r in out] != [r["id"] for r in inp]:
        return ["id/순서 불일치"]
    errs = []
    for a, b in zip(inp, out):
        i = a["id"]
        if set(b.get("choices") or {}) != set(a["choices"]): errs.append(f"{i}: 보기 키")
        t = b.get("question", "") + " ".join((b.get("choices") or {}).values())
        if not b.get("question") or any(not v for v in (b.get("choices") or {}).values()): errs.append(f"{i}: 빈 값")
        if latin(t) < 0.6 * max(1, kana(t) + latin(t)) : errs.append(f"{i}: 영어 부족(가나 {kana(t)}자)")
        if a["question"].count("```") != b.get("question", "").count("```"): errs.append(f"{i}: 코드블록")
    return errs
if __name__ == "__main__":
    keep = "--keep" in sys.argv
    names = sorted(p.stem for p in (TR / "out").glob("*.json"))
    bad = {n: e for n in names if (e := check(n))}
    missing = sorted(p.stem for p in (TR / "in").glob("*.json") if p.stem not in names)
    print(f"out {len(names)}개 검사: 문제 {len(bad)}개 배치, 아직 없음 {len(missing)}개")
    for n, e in bad.items(): print(" ", n, e[:4])
    if bad and not keep:
        (TR / "out/_bad").mkdir(exist_ok=True)
        for n in bad: (TR / "out" / f"{n}.json").rename(TR / "out/_bad" / f"{n}.json")
        print("문제 배치를 out/_bad/ 로 이동")
