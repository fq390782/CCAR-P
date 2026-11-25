"""part*.md(NEW-SECTION·RULES·TRAPS·MEMO·CHECK 블록) → 새 장 파일. usage: python3 -I assemble.py <out> "<제목>" "<커버>" part1.md ..."""
import re, sys
out, title, cover, parts = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
SUB = re.compile(r'^<sub>근거: (.*)</sub>$')
new, tail = [], {'RULES': [], 'TRAPS': [], 'MEMO': [], 'CHECK': []}
for p in parts:
    for b in re.split(r'^@@ ', open(p, encoding='utf-8').read(), flags=re.M)[1:]:
        head, _, body = b.partition('\n')
        (new if head.startswith('NEW-SECTION') else tail[head.strip()]).append(body.strip('\n'))
o = [title, cover, '', '## 1. 핵심 개념', '']
for k, b in enumerate(new, 1):
    o += [re.sub(r'^### (\d+\.\d+ )?', f'### 1.{k} ', b, count=1, flags=re.M), '']
HEAD = {'RULES': ('## 2. 상황별 정답 판단 규칙', '| 상황 | 정답 |'), 'TRAPS': ('## 3. 자주 나오는 오답 함정', '| 오답 | 이유 |'),
        'MEMO': ('## 4. 암기 목록', '| 이름 | 의미 |'), 'CHECK': ('## 5. 시험 직전 체크리스트', None)}
for k, (h, th) in HEAD.items():
    lines, ids = [], set()
    for b in tail[k]:
        for l in b.split('\n'):
            m = SUB.match(l.strip())
            if m: ids |= {i.strip() for i in m.group(1).split(',') if i.strip()}
            elif th and l.startswith('|') and not re.match(r'^\|[-| :]+\|$', l) and not re.match(r'^\|\s*(상황|오답|이름)\s*\|', l): lines.append(l)
            elif not th and l.startswith('- [ ]'): lines.append(l)
    o += [h, '']
    if th: o += [th, '|---|---|']
    o += lines + ['', '<sub>근거: ' + ', '.join(sorted(ids)) + '</sub>', '']
open(out, 'w', encoding='utf-8').write('\n'.join(o).rstrip('\n') + '\n')
print('sections', len(new), {k: len(v) for k, v in tail.items()})
