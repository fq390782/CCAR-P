"""Step 6a: use the section the source already gives, matched to domains.json BY NAME (never by number).
Unmatched questions are batched (30 per batch) for the classifier: work/classify/<EXAM>/batch-NN.json."""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; W = ROOT / "work"
EXAMS = ("CCAO-F", "CCDV-F", "CCAR-F", "CCAR-P")
def n(t):
    t = t.lower().replace("&", " and ").replace("claude's", " ").replace("’", "'")
    t = re.sub(r"\bclaude\b", " ", t)
    return " ".join(re.findall(r"[a-z]+", t))

# jrajath94 uses D-codes; its own legend (08-question-bank.html <h2> headings) gives the name for each code.
s = (ROOT / "CCAR-P/jrajath94__08-question-bank.html").read_text(encoding="utf-8")
JR = {m[1]: re.sub(r"\s*\(.*$", "", m[2]).strip() for m in
      (re.match(r"D(\d)\. (.+)", re.sub(r"<[^>]+>", "", h).strip()) for h in re.findall(r"<h2[^>]*>(D\d\..*?)</h2>", s, re.S)) if m}
# raybeecham module titles -> official names, matched by name (module numbers differ from official numbers)
RAY = {"platform and model foundations": "product and model selection",
       "prompting and task execution": "prompting and task execution",
       "evaluating and validating output": "output evaluation and validation",
       "workflow integration and solution design": "workflow integration and solution design",
       "workflow integration and solutions design": "workflow integration and solution design",
       "configuration and knowledge management": "configuration and knowledge management",
       "governance risk and responsible use": "governance risk and responsible use",
       "troubleshooting and optimization": "troubleshooting and optimization"}

def resolve(exam, label, doms):
    if not label: return None, None
    lab = label.strip()
    m = re.match(r"^(?:V2-)?D(\d)(?:\.\d+)?$", lab)
    if exam == "CCAR-P" and m: lab = JR[m[1]]                                  # code -> name via repo legend
    lab = re.sub(r"^(module \d+:|quiz:)\s*", "", lab, flags=re.I)
    k = n(lab); k = RAY.get(re.sub(r"^claude ", "", k), k) if exam == "CCAO-F" else k
    k = RAY.get(k, k) if exam == "CCAO-F" else k
    for d in doms:
        if n(d["name"]) == k: return d, lab
    return None, lab

stats, unmatched = {}, {}
for exam in EXAMS:
    doms = json.loads((ROOT / "reference/exams" / exam / "domains.json").read_text())["domains"]
    qs = json.loads((W / "deduped" / f"{exam}.json").read_text())
    todo = []
    for q in qs:
        d, lab = resolve(exam, q["source_section"], doms)
        if d:
            q["domain"] = f"{d['number']}. {d['name']}"; q["domain_confidence"] = "source"
        else:
            if lab: unmatched.setdefault(exam, {}).setdefault(lab, 0); 
            if lab: unmatched[exam][lab] += 1
            todo.append(q)
    (W / "mapped").mkdir(exist_ok=True)
    (W / "mapped" / f"{exam}.json").write_text(json.dumps(qs, indent=1, ensure_ascii=False) + "\n")
    out = W / "classify" / exam; out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("batch-*.json"): old.unlink()
    for i in range(0, len(todo), 30):
        b = [{"id": q["id"], "question": q["question"], "choices": q["choices"], "explanation": q["explanation"]} for q in todo[i:i + 30]]
        (out / f"batch-{i // 30 + 1:02d}.json").write_text(json.dumps(b, indent=1, ensure_ascii=False) + "\n")
    stats[exam] = {"total": len(qs), "from_source": len(qs) - len(todo), "to_classifier": len(todo), "batches": -(-len(todo) // 30)}
print(json.dumps(stats, indent=1)); print("labels not matched by name (sent to classifier):", json.dumps(unmatched, indent=1, ensure_ascii=False)); print("jrajath legend:", JR)
