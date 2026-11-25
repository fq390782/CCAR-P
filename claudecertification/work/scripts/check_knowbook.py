"""Usage: python3 -I check.py <orig.md> <new.md>  -> prints PASS/FAIL + metrics. Exit 1 on hard failure."""
import re, sys

# 1~8장의 CCDV-F 근거는 짧은 id(Amey-0004), 그 밖의 시험은 gold id 전체(CCAR-P-jrajath94-0084)
ID = r'(?:CC[A-Z]{2}-[FP]-[A-Za-z][A-Za-z0-9-]*?-\d{4}|(?:Amey|Patrick|Preporato|Udemy)-\d{4})'
o, n = (open(p, encoding='utf-8').read() for p in sys.argv[1:3])
fails, warns = [], []

ids_o, ids_n = set(re.findall(ID, o)), set(re.findall(ID, n))
if ids_o - ids_n: fails.append(f'R9 missing ids: {sorted(ids_o - ids_n)}')
if ids_n - ids_o: fails.append(f'R10 new ids not in original: {sorted(ids_n - ids_o)}')
inline = re.findall(r'\[' + ID + r'\]', n)
if inline: fails.append(f'R9 inline [id] remain: {len(inline)}')
stray = [l for l in n.splitlines() if re.search(ID, l) and not l.strip().startswith('<sub>근거:')]
if stray: fails.append(f'R9 ids outside <sub>근거:</sub> lines: {len(stray)} e.g. {stray[0][:80]!r}')

if n.count('⚠️') < o.count('⚠️'): fails.append(f'R10 ⚠️ count {o.count("⚠️")} -> {n.count("⚠️")}')

fig = lambda t: [l for l in t.splitlines() if l.startswith('![') or l.startswith('*그림:')]
if fig(o) != fig(n): fails.append('R11 figure/caption lines changed, reordered or missing')

h = lambda t, p: [l for l in t.splitlines() if l.startswith(p)]
if h(o, '# ') != h(n, '# ') or h(o, '> 시험') != h(n, '> 시험'): fails.append('R12 title/header line changed')
if [x[:6] for x in h(o, '## ')] != [x[:6] for x in h(n, '## ')]: fails.append('R12 ## chapters changed')
num = lambda t: [re.match(r'### ([\d.\-]+)', l).group(1) for l in h(t, '### ') if re.match(r'### [\d.\-]+', l)]
if num(o) != num(n): fails.append(f'R12 ### numbering changed: {num(o)} -> {num(n)}')

# style metrics (soft)
body = [l for l in n.splitlines() if l.strip() and not l.startswith(('#', '>', '![', '*그림', '<sub>', '|---', '```'))]
prose_end = [l for l in body if re.search(r'(다|요)\.?\s*(\*\*)?$', l.split('|')[-2] if l.startswith('|') and l.count('|') > 2 else l)]
if prose_end: warns.append(f'R4 서술형 종결 줄 {len(prose_end)}개 e.g. {prose_end[0][:70]!r}')
fillers = re.findall(r'(또한|즉,|따라서|그래서|다만|게다가|참고로|사실상)', n)
if fillers: warns.append(f'R7 군더더기 {len(fillers)}개: {sorted(set(fillers))}')
longs = [s for l in body for s in re.split(r'<br>|\|', l) if len(re.sub(r'`|\*\*', '', s.strip(' -[]'))) > 60]
if longs: warns.append(f'R5 60자 초과 조각 {len(longs)}개 e.g. {longs[0].strip()[:70]!r}')
tables = len(re.findall(r'^\|[-| :]+\|$', n, re.M))
paras = [l for l in body if not l.startswith(('|', '-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '**'))]
if paras: warns.append(f'R2 줄글 문단 의심 {len(paras)}개 e.g. {paras[0][:70]!r}')

print(f'tables={tables} chars {len(o)}->{len(n)} ({len(n)*100//max(len(o),1)}%) ids={len(ids_n)}/{len(ids_o)}')
for w in warns: print('WARN', w)
for f in fails: print('FAIL', f)
print('PASS' if not fails else 'FAIL')
sys.exit(1 if fails else 0)
