"""Step 3 (JSON sources): convert JSON question files to the extractor record format, no agents.
Text is copied as-is; only field names/letter case are mapped."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "work/extracted"
def save(exam, name, recs):
    p = OUT / exam / f"{name}.json"; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(recs, indent=1, ensure_ascii=False) + "\n", encoding="utf-8"); print(exam, name, len(recs))

for exam in ("CCAO-F", "CCDV-F", "CCAR-F", "CCAR-P"):
    d = json.loads((ROOT / exam / "Amey-Thakur__question-bank.json").read_text(encoding="utf-8"))
    save(exam, "Amey-Thakur__question-bank.json", [{
        "number": q["id"], "heading": None, "question": q["question"], "choices": q["options"],
        "answer": [q["answer"]] if isinstance(q["answer"], str) else q["answer"], "select_count": 1,
        "explanation": q.get("rationale"), "source_section": q.get("domain")} for q in d["questions"]])

for exam, f in (("CCAO-F", "ccao-f"), ("CCDV-F", "ccdv-f"), ("CCAR-F", "cca-f"), ("CCAR-P", "ccar-p")):
    d = json.loads((ROOT / exam / f"preporato__practice__{f}.json").read_text(encoding="utf-8"))
    names = {x["id"]: x["name"] for x in d["domains"]}
    scen = {x["id"]: x["text"] for x in d.get("scenarios") or []}
    recs = []
    for i, q in enumerate(d["questions"], 1):
        stem = q["stem"]
        if q.get("scenario"):  # CCA-F groups questions under a shared scenario; its text is part of the question
            stem = scen[q["scenario"]] + "\n\n" + stem
        if q.get("code"):
            stem += f"\n\n```{q['code'].get('lang', '')}\n{q['code']['text']}\n```"
        recs.append({"number": str(i), "heading": None, "question": stem,
                     "choices": {k.upper(): v for k, v in q["options"].items()},
                     "answer": [a.upper() for a in q["answer"]], "select_count": len(q["answer"]),
                     "explanation": q.get("explanation"), "source_section": names.get(q.get("domain"))})
    save(exam, f"preporato__practice__{f}.json", recs)

import re
MODULES = {}  # module titles taken from the repo's own module READMEs ("# Module N: Title")
for r in (ROOT / "_repos/raybeecham__claude-certified-associate-foundations/modules").glob("0*/README.md"):
    m = re.search(r"^# Module (\d+): (.+)$", r.read_text(encoding="utf-8"), re.M)
    if m: MODULES[int(m[1])] = m[2].strip()
assert len(MODULES) >= 7, MODULES
d = json.loads((ROOT / "CCAO-F/raybeecham__questions.json").read_text(encoding="utf-8"))
save("CCAO-F", "raybeecham__questions.json", [{
    "number": q["id"], "heading": None, "question": q["scenario"], "choices": q["options"],
    "answer": [q["answer"]] if isinstance(q["answer"], str) else q["answer"], "select_count": 1,
    "explanation": q["rationale"] + "".join(f"\n- {k}: {v}" for k, v in (q.get("distractor_rationales") or {}).items()),
    "source_section": f"Module {q['domain']}: {MODULES[q['domain']]}"} for q in d])
