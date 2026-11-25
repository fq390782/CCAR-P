"""Extra check: compare extracted answers with answers parsed by regex from the chunked HTML sources (in order)."""
import json, re
from pathlib import Path
W = Path(__file__).resolve().parents[1]
PAT = {"paullarionov": None,
       "08-question-bank": r'qb-verdict">Answer: ([A-E](?:\s*(?:,|and)\s*[A-E])*)',
       "question-bank.html": r'<strong>(?:Answer|Key)\.</strong>\s*([A-E](?:\s*(?:,|and)\s*[A-E])*)\b',
       "practice-answer-key": r'Answer: ([A-E](?:\s*,\s*[A-E])*)\.'}
bad, total = [], 0
for j in json.loads((W / "jobs.json").read_text())["jobs"]:
    if "chunks" not in j["read"][0]: continue
    src = (W.parent / j["read"][0]).read_text(encoding="utf-8")
    if "paullarionov" in j["out"]:
        want = [[json.loads(l)["correct"]] for l in src.splitlines() if l.strip()]
    else:
        pat = next(v for k, v in PAT.items() if v and k in j["out"])
        blocks = re.split(r"<h3[^>]*>", src)[1:] if "question-bank.html" in j["out"] and "08-" not in j["out"] else [src]
        want = []
        for b in blocks:
            ms = re.findall(pat, b)
            want += [re.findall(r"[A-E]", ms[0])] if len(blocks) > 1 and ms else ([] if len(blocks) > 1 else [re.findall(r"[A-E]", m) for m in ms])
    got = [r.get("answer") for r in json.loads((W.parent / j["out"]).read_text())]
    total += len(got)
    if len(want) != len(got): bad.append({"out": j["out"], "issue": f"parsed {len(want)} answers vs {len(got)} records"}); continue
    for i, (w, g) in enumerate(zip(want, got)):
        if sorted(w) != sorted(g or []): bad.append({"out": j["out"], "index": i, "source": w, "extracted": g})
print("checked", total, "mismatches", len(bad)); print(json.dumps(bad[:20], indent=1))
(W / "answer_crosscheck.json").write_text(json.dumps(bad, indent=1))
