"""Build work/domains/<EXAM>/domains.json from the official exam-guide PDFs (pdftotext -layout)."""
import json, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT / "_repos/Amey-Thakur__CLAUDE-CERTIFICATIONS"
EXAMS = {"CCAO-F": "associate-foundations", "CCDV-F": "developer-foundations",
         "CCAR-F": "architect-foundations", "CCAR-P": "architect-professional"}
FOOT = re.compile(r"^Claude Certification Program\s+Exam guide$")
for code, folder in EXAMS.items():
    pdf = REPO / folder / "exam-guide.pdf"
    lines = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, check=True).stdout.splitlines()
    # blueprint table: "<n>   <name>   <weight>%"
    i = next(k for k, l in enumerate(lines) if re.match(r"^Domain\s+Content Domain\s+Weight", l))
    table = []
    for l in lines[i + 1:]:
        if l.startswith("| Total"): break
        m = re.match(r"^(\d+)\s{2,}(.+?)\s{2,}([\d.]+%)\s*$", l)
        if m: table.append((int(m[1]), m[2].strip(), m[3]))
    # objective blocks: from "Domain N: Name" heading to next heading / next numbered chapter
    heads = [k for k, l in enumerate(lines) if re.match(r"^Domain \d+: ", l)]
    domains = []
    for n, name, w in table:
        k = next(h for h in heads if lines[h].startswith(f"Domain {n}: "))
        end = next((h for h in heads if h > k), None)
        block = []
        for l in lines[k + 1:end]:
            if re.match(r"^\d+\. [A-Z]", l) or l.startswith("Domains reinforced"): break
            if FOOT.match(l.strip()): continue
            block.append(l.rstrip())
        objs, cur = [], None
        for l in block:
            s = l.strip()
            start = s.startswith("•") or re.match(r"^Task Statement \d+\.\d+:", s) or (re.match(r"^[A-Z][^.]*\([\d.]+%\)$", s) and not l.startswith(" "))
            if code == "CCAR-F" and s.startswith("•"): start = False  # CCAR-F bullets are knowledge/skill details, keep task statements only
            if start:
                cur = s.lstrip("• ").strip(); objs.append(cur)
            elif code == "CCDV-F" and s and cur is not None:
                objs[-1] += (" — " if objs[-1].endswith("%)") else " ") + s  # skill description paragraph
            elif s and cur is not None and objs and l.startswith("  ") and not s.startswith(("Knowledge", "Skills")):
                objs[-1] += " " + s  # wrapped continuation of a bullet
            elif code == "CCAR-F" and s and cur is not None and re.match(r"^Task Statement", objs[-1]) and not s.startswith(("Knowledge", "Skills", "•")) and not objs[-1].endswith("."):
                objs[-1] += " " + s; cur = None  # wrapped task statement title (one line)
            else:
                cur = None if not s or s.startswith(("Knowledge", "Skills")) else cur
        domains.append({"number": n, "name": name, "weight": w, "objectives": objs})
    out = ROOT / "work/domains" / code / "domains.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"exam": code, "source": f"_repos/Amey-Thakur__CLAUDE-CERTIFICATIONS/{folder}/exam-guide.pdf", "domains": domains}, indent=1, ensure_ascii=False) + "\n")
    print(code, [(d["number"], d["name"], d["weight"], len(d["objectives"])) for d in domains])
