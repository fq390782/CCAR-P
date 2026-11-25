"""검증 결과 반영. usage: python3 -I apply_fixes.py <md> <fixes.json>
fixes.json = {"add": {"<### 또는 ## 머리 줄>": [id, ...]}, "rep": [["옛 문구", "새 문구"], ...]}
add: 그 머리 아래(다음 머리 전까지)의 <sub>근거:</sub> 줄에 id 합집합. rep: 정확히 1회 등장해야 함."""
import json, re, sys
p, spec = sys.argv[1], json.load(open(sys.argv[2], encoding='utf-8'))
L = open(p, encoding='utf-8').read().split('\n')
SUB = re.compile(r'^<sub>근거: (.*)</sub>$')
add, done, cur = spec.get('add', {}), set(), None
for i, l in enumerate(L):
    if l.startswith(('## ', '### ')):
        cur = l if l in add else None
    m = SUB.match(l)
    if m and cur:
        L[i] = '<sub>근거: ' + ', '.join(sorted({x.strip() for x in m.group(1).split(',')} | set(add[cur]))) + '</sub>'
        done.add(cur)
t = '\n'.join(L)
bad = []
for a, b in spec.get('rep', []):
    if t.count(a) != 1: bad.append(a); continue
    t = t.replace(a, b)
open(p, 'w', encoding='utf-8').write(t)
print('add targets missed:', sorted(set(add) - done))
print('rep not unique/missing:', bad)
