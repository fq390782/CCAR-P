"""Step 6b + 7: apply classifier results, collect review_needed, write output/<EXAM>/*.json and output/REPORT.md."""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; W = ROOT / "work"; OUT = ROOT / "output"
EXAMS = ("CCAO-F", "CCDV-F", "CCAR-F", "CCAR-P")
def key(t): return re.sub(r"[^0-9a-z]+", "", (t or "").lower())
review, problems, per_exam = [], [], {}
for exam in EXAMS:
    doms = json.loads((W / "domains" / exam / "domains.json").read_text())["domains"]
    names = {f"{d['number']}. {d['name']}": d for d in doms}
    qs = json.loads((W / "mapped" / f"{exam}.json").read_text()); byid = {q["id"]: q for q in qs}
    for f in sorted((W / "classify" / exam).glob("batch-*.json")):
        if f.name.endswith(".result.json"): continue
        want = [x["id"] for x in json.loads(f.read_text())]
        rf = f.with_name(f.stem + ".result.json")
        res = json.loads(rf.read_text()) if rf.exists() else []
        got = {r["id"]: r for r in res}
        if sorted(got) != sorted(want): problems.append(f"{rf.name}: ids differ from batch ({len(got)} vs {len(want)})")
        for i in want:
            r = got.get(i)
            if not r or r.get("domain") not in names or r.get("confidence") not in ("high", "medium", "low"):
                problems.append(f"{exam} {i}: invalid classifier result {r}"); byid[i]["domain_confidence"] = "low"; continue
            byid[i]["domain"], byid[i]["domain_confidence"] = r["domain"], r["confidence"]
    valid = {q["id"]: q for q in json.loads((W / "valid" / f"{exam}.json").read_text())}
    for q in qs:
        if q["domain_confidence"] == "low":
            review.append({"id": q["id"], "exam": exam, "reason": "섹션 분류 확신 낮음 (classifier confidence=low)" if q["domain"] else "섹션 미분류", "domain": q["domain"], "question": q["question"]})
        # duplicate sources that disagree on the correct answer (compared by answer choice text)
        mine = sorted(key(q["choices"][a]) for a in q["answer"])
        for o in q.get("also_in", []):
            v = valid[o["id"]]
            if sorted(key(v["choices"][a]) for a in v["answer"]) != mine:
                review.append({"id": q["id"], "exam": exam, "reason": f"중복 출처 간 정답 불일치: {q['source_file']} → {q['answer']}, {o['source_file']} → {v['answer']}", "domain": q["domain"], "question": q["question"]})
    d = OUT / exam; d.mkdir(parents=True, exist_ok=True)
    for old in d.glob("*.json"): old.unlink()
    counts = {}
    for name, dm in names.items():
        sec = [q for q in qs if q["domain"] == name]; counts[name] = len(sec)
        fn = f"{dm['number']}_" + re.sub(r"[^0-9A-Za-z]+", "_", dm["name"].replace("&", "and")).strip("_") + ".json"
        (d / fn).write_text(json.dumps(sec, indent=1, ensure_ascii=False) + "\n")
    unc = [q for q in qs if not q["domain"]]
    if unc: (d / "_unclassified.json").write_text(json.dumps(unc, indent=1, ensure_ascii=False) + "\n")
    (d / "all.json").write_text(json.dumps(qs, indent=1, ensure_ascii=False) + "\n")
    per_exam[exam] = {"total": len(qs), "sections": counts, "unclassified": len(unc),
                      "from_source": sum(q["domain_confidence"] == "source" for q in qs),
                      "classified": {c: sum(q["domain_confidence"] == c for q in qs) for c in ("high", "medium", "low")},
                      "weights": {f"{x['number']}. {x['name']}": x["weight"] for x in doms}}
(W / "review_needed.json").write_text(json.dumps(review, indent=1, ensure_ascii=False) + "\n")
(W / "assemble_stats.json").write_text(json.dumps({"per_exam": per_exam, "problems": problems}, indent=1, ensure_ascii=False) + "\n")
print(json.dumps(per_exam, indent=1, ensure_ascii=False)); print("review_needed", len(review)); print("problems", problems)
