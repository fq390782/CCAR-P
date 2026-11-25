"""part*.md 블록을 orig 3장에 끼워 넣어 최종 3장을 만든다. usage: python3 -I merge.py <orig> <out> part1.md ..."""
import re, sys
orig, out, parts = sys.argv[1], sys.argv[2], sys.argv[3:]
L = open(orig, encoding='utf-8').read().split('\n')
add, new, tail = {}, [], {'RULES': [], 'TRAPS': [], 'MEMO': [], 'CHECK': []}
SUB = re.compile(r'^<sub>근거: (.*)</sub>$')

for p in parts:
    blocks = re.split(r'^@@ ', open(p, encoding='utf-8').read(), flags=re.M)[1:]
    for b in blocks:
        head, _, body = b.partition('\n')
        body = body.strip('\n')
        if head.startswith('ADD-TO:'):
            k = head[7:].strip()
            add.setdefault(k if k.startswith('### ') else '### ' + k, []).append(body)
        elif head.startswith('NEW-SECTION'):
            new.append(body)
        else:
            tail[head.strip()].append(body)

def split_ids(bodies):
    lines, ids = [], set()
    for b in bodies:
        for l in b.split('\n'):
            m = SUB.match(l.strip())
            if m: ids |= {i.strip() for i in m.group(1).split(',') if i.strip()}
            else: lines.append(l)
    return lines, ids

def rows(lines):  # 표 머리(열 이름·구분선) 제거, 행만
    return [l for l in lines if l.startswith('|') and not re.match(r'^\|[-| :]+\|$', l)
            and not re.match(r'^\|\s*(상황|오답|이름|구분)\s*\|', l)]

def merge_sub(line, ids):
    m = SUB.match(line)
    old = {i.strip() for i in m.group(1).split(',')}
    return '<sub>근거: ' + ', '.join(sorted(old | ids)) + '</sub>'

o = []
sec = cur = None
i = 0
missing = set(add)
while i < len(L):
    l = L[i]
    if l.startswith('### '):
        cur = l
    if l.startswith('## '):
        if sec == '1':  # 1장 끝 → 새 소절
            o += [b + '\n' for b in new]
        sec = l[3]
        cur = None
    if SUB.match(l) and cur in add:  # 기존 소절 끝에 덧붙임
        lines, ids = split_ids(add[cur]); missing.discard(cur)
        while o and o[-1] == '': o.pop()
        # 그림 줄은 근거 줄 바로 위 유지 → 그림 앞에 삽입
        k = len(o)
        while k and (o[k-1].startswith('![') or o[k-1].startswith('*그림') or o[k-1] == ''): k -= 1
        o[k:k] = [''] + lines + ['']
        o += ['', merge_sub(l, ids)]; i += 1; continue
    o.append(l); i += 1

# 2~5장 꼬리 블록
txt = '\n'.join(o)
def put(section_head, key, anchor_last_table=True):
    global txt
    lines, ids = split_ids(tail[key])
    if not lines and not ids: return
    a = txt.index(section_head); b = txt.find('\n## ', a + 1); b = len(txt) if b < 0 else b
    seg = txt[a:b].split('\n')
    new_lines = rows(lines) if key != 'CHECK' else [x for x in lines if x.startswith('- [ ]')]
    last = max(j for j, x in enumerate(seg) if x.startswith('|' if key != 'CHECK' else '- [ ]'))
    seg[last+1:last+1] = new_lines
    s = [j for j, x in enumerate(seg) if SUB.match(x)]
    if s: seg[s[-1]] = merge_sub(seg[s[-1]], ids)
    else:
        while seg and seg[-1] == '': seg.pop()
        seg += ['', '<sub>근거: ' + ', '.join(sorted(ids)) + '</sub>', '']
    txt = txt[:a] + '\n'.join(seg) + txt[b:]

put('## 2.', 'RULES'); put('## 3.', 'TRAPS'); put('## 4.', 'MEMO'); put('## 5.', 'CHECK')
txt = txt.replace('\n## 1. 핵심 개념', '\n> 커버: CCDV-F D3 · CCAR-F D3 · CCAR-P D7\n\n## 1. 핵심 개념', 1)
open(out, 'w', encoding='utf-8').write(txt.rstrip('\n') + '\n')
print('ADD-TO not matched:', sorted(missing))
print('new sections:', len(new), {k: len(v) for k, v in tail.items()})
