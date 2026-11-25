#!/usr/bin/env python3
"""work/translate/ko/out/*.json 검증. 문제가 있는 배치 파일은 out/_bad/ 로 옮긴다(--keep 이면 이동 안 함).
검사: 유효한 JSON / id·순서 일치 / 보기·보기별해설 키 일치 / 빈 값 / 한글 비율 / 코드 블록·인라인 코드 보존."""
import json, re, sys
from pathlib import Path

TR = Path(__file__).resolve().parents[2] / "work/translate/ko"
hangul = lambda s: len(re.findall(r"[가-힣]", s))
letters = lambda s: len(re.findall(r"[A-Za-z가-힣ぁ-んァ-ン一-龥]", s))
spans = lambda s: re.findall(r"`[^`\n]+`", s)

def texts(o):
    return [o.get("question", ""), o.get("explanation", "")] + list((o.get("choices") or {}).values()) + list((o.get("choice_explanations") or {}).values())

def check(name):
    inp = json.load(open(TR / "in" / f"{name}.json", encoding="utf-8"))
    try:
        out = json.load(open(TR / "out" / f"{name}.json", encoding="utf-8"))
    except Exception as e:
        return [f"invalid JSON: {e}"]
    errs = []
    if [r.get("id") for r in out] != [r["id"] for r in inp]:
        return ["id/순서 불일치"]
    for a, b in zip(inp, out):
        i = a["id"]
        if name.startswith("en"):
            if set(b.get("choices") or {}) != set(a["choices"]): errs.append(f"{i}: 보기 키")
            if not b.get("question") or not b.get("explanation"): errs.append(f"{i}: 빈 값")
            if any(not v for v in (b.get("choices") or {}).values()): errs.append(f"{i}: 빈 보기")
            src, dst = " ".join(texts(a)), " ".join(texts(b))
            if hangul(b.get("question", "")) < 0.2 * max(1, letters(b.get("question", ""))): errs.append(f"{i}: 한글 부족")
        else:
            if not b.get("explanation"): errs.append(f"{i}: 빈 해설")
            if set(b.get("choice_explanations") or {}) != set(a.get("choice_explanations") or {}): errs.append(f"{i}: 보기별 해설 키")
            src = " ".join([a.get("explanation", "")] + list((a.get("choice_explanations") or {}).values())); dst = " ".join(texts(b))
            if hangul(dst) < 0.2 * max(1, letters(dst)): errs.append(f"{i}: 한글 부족")
        if src.count("```") != dst.count("```"): errs.append(f"{i}: 코드블록 개수")
        miss = [s for s in spans(src) if s not in dst]
        if miss: errs.append(f"{i}: 인라인 코드 누락 {miss[:3]}")
    return errs

if __name__ == "__main__":
    keep = "--keep" in sys.argv
    names = sorted(p.stem for p in (TR / "out").glob("*.json"))
    bad = {}
    for n in names:
        e = check(n)
        if e: bad[n] = e
    missing = sorted(p.stem for p in (TR / "in").glob("*.json") if p.stem not in names)
    print(f"out {len(names)}개 검사: 문제 {len(bad)}개 배치, 아직 없음 {len(missing)}개")
    for n, e in bad.items(): print(" ", n, e[:4], "..." if len(e) > 4 else "")
    json.dump({"bad": bad, "missing": missing}, open(TR / "check_report.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if bad and not keep:
        (TR / "out/_bad").mkdir(exist_ok=True)
        for n in bad: (TR / "out" / f"{n}.json").rename(TR / "out/_bad" / f"{n}.json")
        print("문제 배치를 out/_bad/ 로 옮김 -> prepare_ko_batches.py 로 다시 배치 가능")
