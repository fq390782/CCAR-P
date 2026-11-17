"""Step 3 prep: list extractor jobs for md/html files, chunk big HTML files at question boundaries.
Chunks are raw slices of the original file; only line breaks are inserted after closing tags so the
Read tool gets short lines. No text is changed. Writes work/jobs.json."""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
W = ROOT / "work"
jobs, skipped = [], []

def rel(p): return str(Path(p).relative_to(ROOT))
def cnt(p, pat): return len(re.findall(pat, (ROOT / p).read_text(encoding="utf-8"), re.M))
def job(exam, files, expected, note="", part=None, chunk=None):
    stem = Path(files[0]).name
    out = W / "extracted" / exam / (f"{stem}.part{part:02d}.json" if part is not None else f"{stem}.json")
    jobs.append({"key": rel(out), "exam": exam, "source_file": files[0], "read": [chunk] if chunk else files,
                 "extra_read": files[1:] if not chunk else [], "out": rel(out), "expected": expected, "note": note,
                 "parent": f"{exam}/{stem}" })

def breaks(html):  # whitespace-only: newline after block-level closing tags
    return re.sub(r"(</(?:p|li|div|ol|ul|h[1-6]|details|summary|table|tr)>)", r"\1\n", html)

def chunked(exam, src, pieces, per, note):
    d = W / "chunks" / exam / Path(src).name; d.mkdir(parents=True, exist_ok=True)
    for k in range(0, len(pieces), per):
        part = k // per + 1; body = pieces[k:k + per]
        p = d / f"part{part:02d}.txt"
        p.write_text("\n".join(body), encoding="utf-8")
        job(exam, [src], len(body), note, part, rel(p))

AMEY = r"^\*\*\d+\."
for exam in ("CCAO-F", "CCDV-F", "CCAR-F", "CCAR-P"):
    job(exam, [f"{exam}/Amey-Thakur__practice-questions.md"], cnt(f"{exam}/Amey-Thakur__practice-questions.md", AMEY),
        "Each question starts with '**N. <Domain name>.**' — the domain name goes in source_section. Answer and rationale are in the <details> block under each question.")
    for i in (1, 2, 3):
        f = f"{exam}/Amey-Thakur__mock-exam-{i}.md"
        job(exam, [f], cnt(f, AMEY), "Answers, domain and the 'Why' text are in the '## Answer key' table at the end: Answer -> answer, Domain -> source_section, Why -> explanation.")
    f = f"{exam}/preporato__practice-questions.md"
    job(exam, [f], cnt(f, r"^### Question"), "The italic line under '### Question N' is the domain -> source_section. Answer and explanation are in the <details> block. '(Select TWO)' style text in the stem sets select_count.")

# raybeecham CCAO-F: question file + separate answer file are one job
for f in ("practice-exam-01", "practice-exam-02", "practice-exam-03-blueprint-weighted"):
    q, a = f"CCAO-F/raybeecham__{f}.md", f"CCAO-F/raybeecham__{f}-answers.md"
    job("CCAO-F", [q, a], cnt(q, r"^### \d+\."),
        f"Questions and choices are in {q}. Answers, rationales and the domain label are in {a} (read both files). In the answer file, '### N. X | <domain>' heading: X = answer, text after '|' = source_section (or use its domain scoring map table). Explanation = the 'Why ... is best' text plus the distractor notes, verbatim. '**Select two.**' sets select_count.")
for q in sorted(ROOT.glob("CCAO-F/raybeecham__*__quiz.md")):
    job("CCAO-F", [rel(q)], cnt(rel(q), r"^### \d+\.") // 2,
        "Each question appears twice: first the question list, then again inside the 'Answer key and rationales' <details> block with Answer/Rationale. Output each question ONCE (8 total) using the answer-key copy for answer/explanation. Explanation = Rationale + 'Why the other options are weaker' notes. The module title (file '# Quiz: ...' heading) goes in source_section.")

f = "CCDV-F/PatrickWiloak__scenarios.md"
job("CCDV-F", [f], cnt(f, r"^## Scenario"), "Each '## Scenario N - <title>' is one question; the heading goes in heading. Answer is the '**Answer: X.**' line, explanation is the text after it. Code blocks in the stem belong to question (keep the ``` fences).")
f = "CCDV-F/PatrickWiloak__practice-questions__anthropic-claude-developer-foundations.md"
job("CCDV-F", [f], cnt(f, r"^### Question"), "Answer and explanation are in the <details> block ('**Correct: X**', '**Why:**'). Code blocks in the stem belong to question.")

# paullarionov CCAR-F: one JSON-in-JS array on a single line -> one object per line
src = "CCAR-F/paullarionov__practical_test_en.html"
s = (ROOT / src).read_text(encoding="utf-8")
arr = re.search(r"const QUESTIONS\s*=\s*(\[.*?\]);\s*\n", s, re.S).group(1)
objs = [m.group(0) for m in re.finditer(r'\{"n": .*?"global_n": \d+\}', arr)]
assert len(objs) == len(json.loads(arr)) == 60
chunked("CCAR-F", src, objs, 15, "This chunk is a slice of the JavaScript QUESTIONS array from the HTML file; each line is one question object. question = situation + blank line + question. choices from options[].letter/text. answer from \"correct\". explanation from \"explanation\". The \"scenario\" value is NOT an exam domain: put it in heading, leave source_section null.")
skipped.append({"file": "CCAR-F/paullarionov__practical_test_ko.html", "reason": "같은 문제의 한국어판 — 영어판(_en)만 추출"})

# jrajath94 CCAR-P
src = "CCAR-P/jrajath94__08-question-bank.html"
s = (ROOT / src).read_text(encoding="utf-8")
starts = [m.start() for m in re.finditer(r'<div class="qb-q">', s)]
ends = starts[1:] + [s.find("</div>", s.rfind('class="qb-distractors"')) + 30]
pieces = [breaks(s[a:b]) for a, b in zip(starts, ends)]
# the legend that maps D-codes to domain names (from the same file)
legend = "\n".join(re.sub(r"<[^>]+>", "", h).strip() for h in re.findall(r"<h2[^>]*>(D\d\..*?)</h2>", s, re.S))
chunked("CCAR-P", src, pieces, 14, "Each <div class=\"qb-q\"> is one question. question = qb-scenario + constraint-block + qb-ask text, in that order, separated by blank lines (strip tags, decode HTML entities like &quot;). Choices are the <li> items of <ol class=\"qb-opts\" type=\"A\"> in order -> A, B, C, D, E. answer from 'Answer: X' in qb-verdict. explanation = qb-why text + each qb-distractors <li>, verbatim. 'Select two' in qb-head sets select_count. The D-code in qb-head (e.g. D3) goes in source_section exactly as written. heading = qb-num (e.g. Q1).")

src = "CCAR-P/jrajath94__question-bank.html"
s = (ROOT / src).read_text(encoding="utf-8")
h3 = [(m.start(), re.sub(r"<[^>]+>", "", m.group(1)).strip()) for m in re.finditer(r"<h3[^>]*>(.*?)</h3>", s, re.S)]
qh = [(i, t) for i, t in h3 if re.match(r"(Q-D\d+-\d+|Q-M-\d+|M\d+-Q\d+) ", t)]
others = [i for i, t in h3 if not re.match(r"(Q-D\d+-\d+|Q-M-\d+|M\d+-Q\d+) ", t)] + [m.start() for m in re.finditer(r"<h[12][^>]*>", s)] + [len(s)]
pieces = []
for i, t in qh:
    nxt = min(x for x in others + [j for j, _ in qh] if x > i)
    pieces.append(breaks(s[i:nxt]))
assert len(pieces) == 477, len(pieces)
chunked("CCAR-P", src, pieces, 10, "Each <h3> 'Q-D1-01 (V2-D1.1)' / 'Q-M-01 (...)' / 'M1-Q01 (...)' block is one question; the h3 text goes in heading and the 'V2-Dx.y' code in it goes in source_section exactly as written. question = the Scenario paragraph(s) + the Question paragraph, verbatim, without the bold labels 'Scenario.'/'Question.'. Choices are written inline in the Options paragraph(s) as 'A) ... B) ... C) ... D) ...' (may continue in the next <p>): split them on those letter markers, text verbatim. answer from the 'Answer.' paragraph, or in mock exams from the 'Key.' paragraph whose first letters are the answer (e.g. 'Key. B. Decisive phrase...' -> B; may be several letters like 'B, D'). explanation = everything after the answer letters up to the end of the block (method walk / Decisive phrase / Why / Counterfactual / Explanation), verbatim, tags stripped; the paragraph up to the end of the block (method walk and explanation), verbatim, tags stripped. 'Select TWO/THREE' in the heading sets select_count.")
skipped += [{"file": src + " (Prerequisite diagnostic: answer key 섹션)", "reason": "정답표만 있고 문제는 이 레포에 복사하지 않은 crash-course.html 에 있음"},
            {"file": src + " (Counterfactual drills 섹션, 26쌍 52개)", "reason": "보기가 없는 비교 드릴 — 객관식 문제가 아님"}]

src = "CCAR-P/jrajath94__package-v3__practice-answer-key.html"
s = (ROOT / src).read_text(encoding="utf-8")
st = [m.start() for m in re.finditer(r'<div class="item">', s)]
last_end = s.find("</div>", s.find('class="tag">Source.', st[-1])) + len("</div>")
items = [breaks(s[a:b]) for a, b in zip(st, st[1:] + [last_end])]
assert len(items) == 126, len(items)
chunked("CCAR-P", src, items, 21, "Each <div class=\"item\"> is one question. heading = the number label. question = the first <p> text without the number label. 'Select one/two answer(s)' tag sets select_count. Choices = <li> items with their 'A.' labels. answer = letters in 'Answer: X.' (may be 'A, C'). explanation = the rest of the c-rule text after 'Answer: X.' + the c-trap text, verbatim. source_section null.")
skipped.append({"file": "CCAR-P/jrajath94__package-v3__practice-test.html", "reason": "practice-answer-key.html 과 같은 126문제(정답 없음) — 정답이 있는 answer-key 판만 추출"})

(W / "jobs.json").write_text(json.dumps({"jobs": jobs, "skipped": skipped, "legend_08": legend}, indent=1, ensure_ascii=False))
print(len(jobs), "jobs;", sum(j["expected"] for j in jobs), "questions expected"); print(legend)
for j in jobs: print(j["expected"], j["out"])
