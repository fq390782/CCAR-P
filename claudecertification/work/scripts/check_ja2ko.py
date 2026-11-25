#!/usr/bin/env python3
"""ja2ko 번역(일본어 문제·보기 -> 한국어) 구조 검사. 사용: check_ja2ko.py [배치명...]
검사: id/순서, 보기 키, 빈 값, 가나 잔존, 문단 수(\\n\\n), 인라인 코드·숫자 보존."""
import json, re, sys
from pathlib import Path
D = Path(__file__).resolve().parents[2] / "work/translate/ja2ko"
kana = lambda s: re.findall(r"[ぁ-んァ-ヶ]", s)
spans = lambda s: re.findall(r"`[^`\n]+`", s)
# 한 자리 수(2つ -> 두 가지 등)는 한국어 수사로 바뀌므로 제외하고, 두 자리 이상·소수만 비교
nums = lambda s: sorted(x for x in re.findall(r"\d+(?:\.\d+)?", re.sub(r"(\d)割", r"\g<1>0%", s).translate(str.maketrans("０１２３４５６７８９", "0123456789"))) if len(x) > 1)
names = sys.argv[1:] or sorted(p.stem for p in (D / "out").glob("j*.json"))
bad = 0
for n in names:
    a = json.load(open(D / "in" / f"{n}.json", encoding="utf-8"))
    try: b = json.load(open(D / "out" / f"{n}.json", encoding="utf-8"))
    except Exception as e: print(n, "읽기 실패", e); bad += 1; continue
    if [x["id"] for x in a] != [x.get("id") for x in b]: print(n, "id/순서 불일치"); bad += 1; continue
    for x, y in zip(a, b):
        e = []
        if set(x["choices"]) != set(y.get("choices") or {}): e.append("보기 키")
        elif not y.get("question") or any(not v for v in y["choices"].values()): e.append("빈 값")
        else:
            sx = x["question"] + "\n".join(x["choices"].values()); sy = y["question"] + "\n".join(y["choices"].values())
            if kana(sy): e.append(f"가나 잔존 {''.join(kana(sy))[:10]}")
            if x["question"].count("\n\n") != y["question"].count("\n\n"): e.append(f"문단 수 {x['question'].count(chr(10)*2)}->{y['question'].count(chr(10)*2)}")
            m = [s for s in spans(sx) if s not in sy]
            if m: e.append(f"인라인 코드 누락 {m[:2]}")
            if nums(sx) != nums(sy): e.append("숫자 불일치")
        if e: print(n, x["id"], e); bad += 1
print(f"{len(names)}개 배치 검사, 문제 {bad}건")
