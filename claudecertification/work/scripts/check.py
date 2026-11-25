"""Step 4: merge chunk outputs, compare counts per job/file, verbatim spot-check, normalize to the common
format, and split valid vs rejected. Writes work/check_report.json, work/rejected.json, work/valid/<EXAM>.json."""
import html, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; W = ROOT / "work"
EXAMS = ("CCAO-F", "CCDV-F", "CCAR-F", "CCAR-P")
REPO = {"Amey-Thakur": "Amey-Thakur/CLAUDE-CERTIFICATIONS", "preporato": "preporato/claude-certification-guide",
        "raybeecham": "raybeecham/claude-certified-associate-foundations", "PatrickWiloak": "PatrickWiloak/ai-zero-to-hero",
        "paullarionov": "paullarionov/claude-certified-architect", "jrajath94": "jrajath94/ccar-p-study-guide"}
# original repo path of every exam-folder file, from the SOURCES.md tables
ORIG = {}
for e in EXAMS:
    for line in (ROOT / e / "SOURCES.md").read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in line.strip("|").split("|")]
        if len(c) == 5 and c[0].endswith((".md", ".json", ".html")):
            ORIG[f"{e}/{c[0]}"] = c[2].split(" (")[0]

def norm(t):  # for verbatim checks only
    t = re.sub(r"</?(?:code|strong|em|b|i|span|a)[^>]*>", "", t or "")  # inline tags: no space
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    t = re.sub(r"[*_`#>\\]", "", t)
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", t).strip().lower()

jobs = json.loads((W / "jobs.json").read_text())["jobs"]
JSON_SRC = {f"{e}/{n}": None for e in EXAMS for n in ("Amey-Thakur__question-bank.json",)}
JSON_SRC.update({"CCAO-F/preporato__practice__ccao-f.json": None, "CCDV-F/preporato__practice__ccdv-f.json": None,
                 "CCAR-F/preporato__practice__cca-f.json": None, "CCAR-P/preporato__practice__ccar-p.json": None,
                 "CCAO-F/raybeecham__questions.json": None})
def json_count(src):
    d = json.loads((ROOT / src).read_text(encoding="utf-8"))
    return len(d["questions"]) if isinstance(d, dict) else len(d)

report = {"jobs": [], "files": [], "retry": []}
by_parent = {}
for j in jobs:
    p = ROOT / j["out"]; status, recs = "ok", None
    try:
        recs = json.loads(p.read_text(encoding="utf-8"))
        if not isinstance(recs, list): status, recs = "not a JSON array", None
    except FileNotFoundError: status = "missing output"
    except Exception as ex: status = f"invalid JSON: {ex}"[:120]
    got = len(recs) if recs is not None else None
    # verbatim check: question start and every choice must appear in the source text
    src = "".join((ROOT / r).read_text(encoding="utf-8") for r in j["read"])
    if "paullarionov" in j["out"]:
        src = " ".join(json.dumps(json.loads(l), ensure_ascii=False) for l in src.splitlines() if l.strip())
        src = src.replace('\\"', '"')
    src = re.sub(r"</p>\s*<p[^>]*>\s*<strong>Question\.</strong>", " ", src)  # Scenario/Question paragraphs may be joined
    ns, bad = norm(src), []
    for r in recs or []:
        parts = [x[:80] for x in re.split(r"\n\s*\n", r.get("question") or "")] + list((r.get("choices") or {}).values())
        miss = [x for x in parts if norm(x) and norm(x)[:60] not in ns]
        if miss: bad.append({"number": r.get("number"), "not_found": [m[:80] for m in miss]})
    if status == "ok" and got != j["expected"]: status = f"count mismatch {got}/{j['expected']}"
    if status == "ok" and bad: status = f"text not verbatim in {len(bad)} question(s)"
    report["jobs"].append({"out": j["out"], "expected": j["expected"], "got": got, "status": status, "not_verbatim": bad[:5]})
    if status != "ok": report["retry"].append(j["out"])
    by_parent.setdefault(j["source_file"], []).append((j, recs, status))

records = {e: [] for e in EXAMS}
def add(exam, src_file, recs):
    for r in recs:
        records[exam].append({"_file": src_file, **r})

for src_file, items in by_parent.items():
    exam = src_file.split("/")[0]
    expected = sum(j["expected"] for j, _, _ in items)
    ok = all(s == "ok" for _, _, s in items)
    got = sum(len(r) for _, r, _ in items if r is not None)
    report["files"].append({"file": src_file, "original_count": expected, "extracted_count": got, "match": ok and got == expected})
    if ok:
        merged = [x for _, r, _ in sorted(items, key=lambda t: t[0]["out"]) for x in r]
        if len(items) > 1:  # chunked source -> one merged file per original
            (W / "extracted" / exam / f"{Path(src_file).name}.json").write_text(json.dumps(merged, indent=1, ensure_ascii=False) + "\n")
        add(exam, src_file, merged)
for src_file in JSON_SRC:
    exam = src_file.split("/")[0]
    recs = json.loads((W / "extracted" / exam / f"{Path(src_file).name}.json").read_text())
    report["files"].append({"file": src_file, "original_count": json_count(src_file), "extracted_count": len(recs), "match": len(recs) == json_count(src_file)})
    add(exam, src_file, recs)

rejected, counters = [], {}
for exam in EXAMS:
    valid = []
    for r in records[exam]:
        f = r.pop("_file"); pre = Path(f).name.split("__")[0]
        counters[(exam, pre)] = counters.get((exam, pre), 0) + 1
        q = {"id": f"{exam}-{pre}-{counters[(exam, pre)]:04d}", "exam": exam, "source_repo": REPO[pre],
             "source_file": ORIG[f], "question": r.get("question"), "choices": r.get("choices") or {},
             "answer": r.get("answer"), "select_count": r.get("select_count"), "explanation": r.get("explanation"),
             "domain": None, "domain_confidence": None,
             "source_number": r.get("number"), "source_heading": r.get("heading"), "source_section": r.get("source_section")}
        why = []
        if not (q["question"] or "").strip(): why.append("question 이 비어 있음")
        if len(q["choices"]) < 2: why.append("choices 가 2개 미만")
        a = q["answer"]
        if a is None: why.append("answer 가 null")
        elif not isinstance(a, list) or not a or any(x not in q["choices"] for x in a): why.append("answer 에 choices 에 없는 기호가 있음")
        if isinstance(a, list) and a and len(a) != q["select_count"]: why.append(f"answer 개수({len(a)})와 select_count({q['select_count']})가 다름")
        if why: rejected.append({**q, "reasons": why})
        else: valid.append(q)
    (W / "valid").mkdir(exist_ok=True)
    (W / "valid" / f"{exam}.json").write_text(json.dumps(valid, indent=1, ensure_ascii=False) + "\n")
    print(exam, "valid", len(valid))
(W / "rejected.json").write_text(json.dumps(rejected, indent=1, ensure_ascii=False) + "\n")
(W / "check_report.json").write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n")
print("rejected", len(rejected), {r: sum(r in x["reasons"] for x in rejected) for r in {y for x in rejected for y in x["reasons"]}})
print("jobs not ok:", len(report["retry"]))
for x in report["jobs"]:
    if x["status"] != "ok": print("  ", x["status"], x["out"])
