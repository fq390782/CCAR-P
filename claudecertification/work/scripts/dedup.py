"""Step 5: exact duplicates (normalized question text) -> keep one, record the rest in also_in.
Similar-but-not-identical questions are only listed in work/near_duplicates.json."""
import json, re
from difflib import SequenceMatcher
from pathlib import Path
W = Path(__file__).resolve().parents[1]
EXAMS = ("CCAO-F", "CCDV-F", "CCAR-F", "CCAR-P")
def key(t): return re.sub(r"[^0-9a-z]+", "", (t or "").lower())   # drop whitespace, case, symbols
def ckey(q): return sorted(key(v) for v in q["choices"].values())
def score(q): return (q["source_section"] is not None, bool(q["explanation"]))  # prefer the richest record
near, stats = [], {}
for exam in EXAMS:
    qs = json.loads((W / "valid" / f"{exam}.json").read_text())
    groups = {}
    for q in qs: groups.setdefault(key(q["question"]), []).append(q)
    kept, removed = [], 0
    for g in groups.values():
        # same text but different choices = different question: do not merge, list as near-duplicate
        sub = {}
        for q in g: sub.setdefault(tuple(ckey(q)), []).append(q)
        if len(sub) > 1:
            near.append({"exam": exam, "kind": "본문 동일, 보기 다름", "ids": [q["id"] for q in g]})
        for same in sub.values():
            best = max(same, key=score)
            others = [q for q in same if q is not best]
            best = dict(best)
            if others:
                best["also_in"] = [{"id": o["id"], "source_repo": o["source_repo"], "source_file": o["source_file"]} for o in others]
                if best["source_section"] is None:
                    best["source_section"] = next((o["source_section"] for o in others if o["source_section"]), None)
                removed += len(others)
            kept.append(best)
    kept.sort(key=lambda q: q["id"])
    # near duplicates among kept records (word-shingle prefilter, then SequenceMatcher)
    def sh(t):
        w = re.findall(r"[0-9a-z]+", t.lower()); return {" ".join(w[i:i + 3]) for i in range(max(1, len(w) - 2))}
    S = [(q, sh(q["question"]), re.sub(r"\s+", " ", q["question"].lower())) for q in kept]
    for i in range(len(S)):
        for k in range(i + 1, len(S)):
            a, b = S[i], S[k]
            if not a[1] or not b[1]: continue
            j = len(a[1] & b[1]) / len(a[1] | b[1])
            if j < 0.5: continue
            r = SequenceMatcher(None, a[2], b[2]).ratio()
            if r >= 0.85:
                near.append({"exam": exam, "kind": "본문 유사", "similarity": round(r, 3), "ids": [a[0]["id"], b[0]["id"]]})
    (W / "deduped").mkdir(exist_ok=True)
    (W / "deduped" / f"{exam}.json").write_text(json.dumps(kept, indent=1, ensure_ascii=False) + "\n")
    stats[exam] = {"before": len(qs), "after": len(kept), "removed": removed}
(W / "near_duplicates.json").write_text(json.dumps(near, indent=1, ensure_ascii=False) + "\n")
(W / "dedup_stats.json").write_text(json.dumps(stats, indent=1) + "\n")
print(stats, "near:", len(near))
