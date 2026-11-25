#!/usr/bin/env python3
"""output/ 의 모든 시험 JSON -> output/CCTOTALQA/question_bank.html (데이터 내장, 더블클릭 실행).
사용법:
  python3 build_bank.py gold [시험...]  # 10_silver + 00_bronze -> output/<시험>/20_gold/all.json (페이지 레코드 형식). 시험 생략 시 전부
  python3 build_bank.py                 # 페이지 빌드: 각 시험의 20_gold/all.json 을 그대로 사용
데이터 단계: 00_bronze=생데이터, 10_silver=전처리 중, 20_gold=question_bank.html 에 올라가는 데이터(all.json 하나)
번역(한국어/영어)은 아직 병합하지 않는다: 번역 파일이 생기면 rec() 호출 전에 id 기준으로 ko/en 을 채우는 코드를 추가한다.
(번역이 없는 항목은 원문 + '번역 대기' 태그로 표시된다.)
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output"
HERE = Path(__file__).parent
L = lambda p: json.load(open(p, encoding="utf-8"))

# ---------- 한국어 마크다운(CCAO-F) -> {id: {question, choices, explanation}} ----------
def parse_ko_md(path):
    res = {}
    for blk in re.split(r"\n---\n", Path(path).read_text(encoding="utf-8")):
        m = re.search(r"\*\*ID:\*\* `([^`]+)`", blk)
        if not m:
            continue
        rest = blk[m.end():].split("\n", 1)[1]
        q, _, tail = rest.partition("\n- **A.**")
        tail = "- **A.**" + tail
        body, _, ex = tail.partition("\n**해설:**")
        body = body.split("\n**정답:**")[0]
        ch = dict(re.findall(r"^- \*\*([A-E])\.\*\* (.*)$", body, re.M))
        ex = re.split(r"\n<sub>", ex)[0].strip()
        assert q.strip() and ch and ex, m.group(1)
        res[m.group(1)] = {"question": q.strip(), "choices": ch, "explanation": ex}
    return res

# ---------- 레코드 만들기 ----------
def rec(src, origin, primary, en=None, ko=None):
    """src: 원본 문제(JSON), primary: 화면 기본 언어 본문(ko 번역이 있으면 ko, 없으면 원문)."""
    d = {
        "id": src["id"], "exam": src["exam"], "domain": src.get("domain") or "미분류",
        "source": src.get("source_repo") or src.get("source") or "?",
        "origin": origin, "select_count": src["select_count"], "answer": src["answer"],
        "q": primary["question"], "ch": primary["choices"], "ex": primary["explanation"],
        "px": not ko,                       # 해설이 한국어가 아님
    }
    if src.get("choice_explanations"):
        d["ce"] = src["choice_explanations"]    # Udemy: 보기별 해설
    if src.get("reference") or src.get("ref"):
        d["ref"] = src.get("reference") or src.get("ref")
    if origin == "en":
        d["pq"] = not ko                    # 문제·보기가 한국어가 아님(영어 원문만 표시)
        if ko:
            d["en"] = {"q": src["question"], "ch": src["choices"]}
    elif en:
        d["en"] = {"q": en["question"], "ch": en["choices"]}
    return d

# ---------- 시험별 gold 만들기: silver + bronze -> 20_gold/all.json (페이지 레코드 형식) ----------
def gold_ccao_f(F):   # 영어 원문 + 한국어(md)
    ko = parse_ko_md(F / "10_silver/all_ko.md")
    return [rec(s, "en", ko.get(s["id"]) or s, ko=ko.get(s["id"])) for s in L(F / "10_silver/all.json")]

def gold_ccar_f(F):   # 영어 원문(GitHub 3곳) + Udemy 일본어 + MyPractice
    recs = [rec(s, "en", s) for s in L(F / "10_silver/all.json")]
    for i in range(1, 7):
        for s in L(F / f"00_bronze/CCAR-Udemy{i:02d}.json"):
            s["source_repo"] = "Udemy"
            recs.append(rec(s, "ja", s))
    for s in L(F / "00_bronze/MyPractice.json"):   # 한국어 본문 + 영어 상황/질문 병기(영어 보기 없음)
        ko = {"question": s["question"], "choices": s["choices"], "explanation": s["explanation"]}
        d = rec({**s, "question": s["question_en"]}, "en", ko, ko=ko)
        d["en"]["ch"] = {}
        recs.append(d)
    return recs

def gold_ccar_p(F):   # 영어 원문
    return [rec(s, "en", s) for s in L(F / "10_silver/all.json")]

def gold_ccdv_f(F):   # udemy_ja.json = 한국어 154(all_ko) + 일본어 106, 영어는 all.json / udemy_en.json
    en_all = {s["id"]: s for s in L(F / "10_silver/all.json")}
    en_ud = {s["id"]: s for s in L(F / "00_bronze/udemy_en.json")}
    recs = []
    for s in L(F / "10_silver/udemy_ja.json"):
        if s.get("language") == "ja":
            s["source_repo"] = s.get("source_repo") or "Udemy"
            recs.append(rec(s, "ja", s, en=en_ud.get(s["id"])))
        else:
            recs.append(rec(en_all[s["id"]], "en", s, ko=s))   # 한국어 번역(s) + 영어 원문
    return recs

GOLD = {"CCAO-F": gold_ccao_f, "CCAR-F": gold_ccar_f, "CCAR-P": gold_ccar_p, "CCDV-F": gold_ccdv_f}

def apply_ko(recs):
    """work/translate/ko/out/*.json (id 기준 한국어 번역) 을 gold 레코드에 병합."""
    tr = {}
    for f in sorted((ROOT / "work/translate/ko/out").glob("*.json")):
        for r in L(f):
            tr[r["id"]] = r
    v2 = ROOT / "work/translate/ko_v2/out/all.json"     # CCAR-F 재번역(번역투 제거): 있으면 기존 번역을 덮어쓴다
    if v2.exists():
        for r in L(v2):
            tr[r["id"]] = r
    n = 0
    for d in recs:
        t = tr.get(d["id"])
        if not t:
            continue
        if d["origin"] == "en" and d.get("pq"):        # 영어 원문 -> 한국어 본문 + 영어 병기
            d["en"] = {"q": d["q"], "ch": d["ch"]}
            d["q"], d["ch"], d["ex"] = t["question"], t["choices"], t["explanation"]
            d["pq"] = d["px"] = False
        elif d["origin"] == "ja" and d["px"]:           # 일본어 문제 -> 해설만 한국어
            d["ex"] = t["explanation"]
            if t.get("choice_explanations"):
                d["ce"] = t["choice_explanations"]
            d["px"] = False
        else:
            continue
        n += 1
    return n

def apply_en(recs):
    """work/translate/en/out/*.json (일본어 문제의 영어 번역) 을 gold 레코드의 en 병기로 병합."""
    tr = {}
    for f in sorted((ROOT / "work/translate/en/out").glob("*.json")):
        for r in L(f):
            tr[r["id"]] = r
    n = 0
    for d in recs:
        t = tr.get(d["id"])
        if t and d["origin"] == "ja" and not d.get("en"):
            d["en"] = {"q": t["question"], "ch": t["choices"]}
            n += 1
    return n

def apply_ko_ja(recs):
    """work/translate/ja2ko/out/j*.json (일본어 문제·보기의 한국어 번역) -> 레코드의 ko 필드('한국어 + 일본어' 섹션용)."""
    tr = {r["id"]: r for f in sorted((ROOT / "work/translate/ja2ko/out").glob("j*.json")) for r in L(f)}
    n = 0
    for d in recs:
        t = tr.get(d["id"])
        if t and d["origin"] == "ja" and set(t["choices"]) == set(d["ch"]):
            d["ko"] = {"q": t["question"], "ch": t["choices"]}
            n += 1
    return n

def apply_domain(recs, ex):
    """work/classify_bank/<시험>/out/*.json (classifier 결과: id, domain, confidence) 로 '미분류' 를 채운다."""
    valid = {f"{d['number']}. {d['name']}" for d in L(ROOT / "reference/exams" / ex / "domains.json")["domains"]}
    tr = {r["id"]: r["domain"] for f in sorted((ROOT / "work/classify_bank" / ex / "out").glob("*.json")) for r in L(f)}
    n = 0
    for d in recs:
        if d["domain"] == "미분류" and d["id"] in tr:
            assert tr[d["id"]] in valid, (d["id"], tr[d["id"]])
            d["domain"] = tr[d["id"]]
            n += 1
    return n

def make_gold(exams):
    for ex in exams:
        F = OUT / ex
        recs = GOLD[ex](F)
        k = apply_ko(recs)
        e = apply_en(recs)
        j = apply_ko_ja(recs)
        if j:
            print(f"gold: {ex} 일본어 문제 한국어 번역 병합 {j}")
        c = apply_domain(recs, ex)
        if c:
            print(f"gold: {ex} 분야 분류 병합 {c}")
        assert len({r["id"] for r in recs}) == len(recs), ex + " id 중복"
        (F / "20_gold").mkdir(exist_ok=True)
        (F / "20_gold/all.json").write_text(json.dumps(recs, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"gold: {ex} {len(recs)}문제 (한국어 번역 병합 {k}, 영어 번역 병합 {e}) -> output/{ex}/20_gold/all.json")

def build():
    return [r for ex in GOLD for r in L(OUT / ex / "20_gold/all.json")]

def main():
    recs = build()
    ids = [r["id"] for r in recs]
    assert len(ids) == len(set(ids)), "id 중복"
    for r in recs:
        assert r["answer"] and set(r["answer"]) <= set(r["ch"]), r["id"]
        assert len(r["answer"]) == r["select_count"], r["id"]
    data = json.dumps(recs, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = (HERE / "bank_head.html").read_text(encoding="utf-8") + (HERE / "bank_body.html").read_text(encoding="utf-8")
    html = html.replace("__DATA__", data)
    (OUT / "CCTOTALQA/question_bank.html").write_text(html, encoding="utf-8")
    from collections import Counter
    c = Counter((r["exam"], r["origin"]) for r in recs)
    print(len(recs), "문제", dict(c))

if __name__ == "__main__":
    if sys.argv[1:2] == ["gold"]:
        make_gold(sys.argv[2:] or list(GOLD))
    else:
        main()
