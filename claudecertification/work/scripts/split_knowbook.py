"""Know(CCAR-F&P) 장 하나를 CCAR-F판 · CCAR-P판으로 나눈다.
usage: python3 -I work/scripts/split_knowbook.py <장 md 파일명> [--out DIR] [--keep-ccdv]
- 1장(핵심 개념): ### 소절의 <sub>근거 id에 그 시험 문항이 있으면 소절째 포함.
- 2~5장: work/knowbook/split/ch<N>_*.json 의 행별 id로 행 단위 포함. 태그 없는 행은 포함하고 경고.
- --keep-ccdv: CCDV-F 근거만 있는 소절·행도 양쪽에 포함(기본은 제외).
"""
import glob, json, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'output' / 'Know(CCAR-F&P)'
SUB = re.compile(r'^<sub>근거: (.*)</sub>$')
SEP = re.compile(r'^\|[-| :]+\|$')

def exam(i): return 'CCAR-F' if i.startswith('CCAR-F-') else 'CCAR-P' if i.startswith('CCAR-P-') else 'CCDV-F'
def ids_of(text):
    return {x.strip() for l in text.split('\n') if SUB.match(l) for x in SUB.match(l).group(1).split(',') if x.strip()}
def wanted(ids, ex, keep_ccdv):
    es = {exam(i) for i in ids}
    return ex in es or (keep_ccdv and es == {'CCDV-F'})

def split(name, ex, tags, keep_ccdv, warn):
    t = (SRC / name).read_text(encoding='utf-8')
    secs = re.split(r'\n(?=## )', t)
    head, out = secs[0].split('\n'), []
    for l in head:
        if l.startswith('> 시험 비중'): continue  # CCDV-F 비중 줄
        if l.startswith('> 커버:'):
            l = '> 커버: ' + ' · '.join(p for p in l[6:].split(' · ') if p.strip().startswith(ex)) \
                + f'\n> {ex}판: `Know(CCAR-F&P)`에서 자동 생성. 직접 고치지 않는다.'
        out.append(l)
    for s in secs[1:]:
        h = s.split('\n')[0]
        if h.startswith('## 1.'):
            blocks = re.split(r'\n(?=### )', s)
            out.append(blocks[0])
            out += [b for b in blocks[1:] if wanted(ids_of(b), ex, keep_ccdv)]
            continue
        L, keep, used = s.split('\n'), [], set()
        for j, l in enumerate(L):
            is_head = j + 1 < len(L) and SEP.match(L[j + 1]) is not None
            is_row = (l.startswith('|') and not SEP.match(l) and not is_head) or l.startswith('- [ ]')
            if SUB.match(l):
                keep.append('<sub>근거: ' + ', '.join(sorted(used)) + '</sub>' if used else ''); continue
            if is_row and l in tags:
                if not tags[l]: warn.append(f'empty ids: {l[:50]}')
                if tags[l] and not wanted(tags[l], ex, keep_ccdv): continue
                used |= {i for i in tags[l] if exam(i) == ex or keep_ccdv}
            elif is_row:
                warn.append(f'untagged: {l[:50]}')
            keep.append(l)
        # 헤더만 남은 표 제거: 열 이름 줄 + 구분선 뒤에 행이 없으면 둘 다 뺀다
        res = []
        for j, l in enumerate(keep):
            if SEP.match(l) and not (j + 1 < len(keep) and keep[j + 1].startswith('|')):
                res.pop(); continue
            res.append(l)
        out.append('\n'.join(res))
    return re.sub(r'\n{3,}', '\n\n', '\n\n'.join(x.strip('\n') for x in out if x.strip())) + '\n'

def main():
    a = sys.argv[1:]
    name = a[0]; keep_ccdv = '--keep-ccdv' in a
    outdir = Path(a[a.index('--out') + 1]) if '--out' in a else ROOT / 'output'
    n = name.split('_')[0]
    tags = {}
    for f in sorted(glob.glob(str(ROOT / 'work/knowbook/split' / f'ch{n}_*.json'))):
        for r in json.load(open(f, encoding='utf-8')): tags[r['row']] = r['ids']
    src_rows = set((SRC / name).read_text(encoding='utf-8').split('\n'))
    stale = [r for r in tags if r not in src_rows]
    for ex in ('CCAR-F', 'CCAR-P'):
        warn = []
        d = outdir / f'Know({ex})'; d.mkdir(parents=True, exist_ok=True)
        if not (d / 'svg').exists(): os.symlink(SRC / 'svg', d / 'svg')
        txt = split(name, ex, tags, keep_ccdv, warn)
        (d / name).write_text(txt, encoding='utf-8')
        src = (SRC / name).read_text(encoding='utf-8')
        print(f'{ex}: {len(src)//1000}k -> {len(txt)//1000}k ({100*len(txt)//len(src)}%), '
              f'### {src.count(chr(10)+"### ")} -> {txt.count(chr(10)+"### ")}, warn {len(warn)}')
        for w in warn[:10]: print('  ', w)
    print('stale tags (row text changed in source):', len(stale))

if __name__ == '__main__':
    main()
