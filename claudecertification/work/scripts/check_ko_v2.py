#!/usr/bin/env python3
"""ko_v2 번역 구조 검사: id/순서, 보기 키, 빈 값, 한글 비율, 코드블록·인라인 코드 보존. 사용: check_ko_v2.py [배치명...]"""
import json, re, sys
from pathlib import Path
D = Path(__file__).resolve().parents[2] / "work/translate/ko_v2"
hg = lambda s: len(re.findall(r"[가-힣]", s)); lt = lambda s: len(re.findall(r"[A-Za-z가-힣]", s))
sp = lambda s: re.findall(r"`[^`\n]+`", s)
names = sys.argv[1:] or sorted(p.stem for p in (D / "out").glob("*.json"))
bad = 0
for n in names:
    a = json.load(open(D / "in" / f"{n}.json", encoding="utf-8")); b = json.load(open(D / "out" / f"{n}.json", encoding="utf-8"))
    if [x["id"] for x in a] != [x["id"] for x in b]: print(n, "id/순서 불일치"); bad += 1; continue
    for x, y in zip(a, b):
        e = []
        if set(x["choices"]) != set(y["choices"]): e.append("보기 키")
        if not y["question"] or not y["explanation"] or any(not v for v in y["choices"].values()): e.append("빈 값")
        if hg(y["question"]) < 0.2 * max(1, lt(y["question"])): e.append("한글 부족")
        sx = x["question"] + x["explanation"] + "".join(x["choices"].values()); sy = y["question"] + y["explanation"] + "".join(y["choices"].values())
        if sx.count("```") != sy.count("```"): e.append("코드블록 수")
        m = [s for s in sp(sx) if s not in sy]
        if m: e.append(f"인라인 코드 누락 {m[:3]}")
        if e: print(n, x["id"], e); bad += 1
print(f"{len(names)}개 배치 검사, 문제 {bad}건")
