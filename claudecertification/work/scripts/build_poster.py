"""개념서 한 장의 기존 SVG 그림을 큰 포스터 SVG 한 장으로 이어 붙인다.

사용: python3 -I work/scripts/build_poster.py "output/Know(CCAR-F&P)/8_Tools_and_MCPs.md"
결과: 같은 폴더의 svg/{장번호}-overview-poster.svg
그림 순서·제목은 md의 `![..](svg/..)` 줄과 그 위 ### 제목에서 읽는다. 내용은 새로 만들지 않는다.
"""
import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape

COLS, CELL_W, GAP, PAD, CAP_H, BAND_H, TITLE_H = 4, 960, 48, 64, 40, 72, 120
FONT = "Apple SD Gothic Neo, Noto Sans KR, Malgun Gothic, sans-serif"


def main(md_arg):
    md = Path(md_arg)
    chap = md.name.split("_")[0]
    title, groups, sub = md.stem, [], ""  # groups: [(## 제목, [(### 제목, svg 경로)])]
    for line in md.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            title = line[2:].split("—")[0].strip()
        elif line.startswith("## "):
            groups.append((line[3:].strip(), []))
            sub = ""
        elif line.startswith("### "):
            sub = line[4:].strip()
        elif m := re.match(r"!\[(.*?)\]\((svg/[^)]+\.svg)\)", line):
            groups[-1][1].append((sub or m.group(1), md.parent / m.group(2)))
    groups = [g for g in groups if g[1]]

    width = PAD * 2 + COLS * CELL_W + (COLS - 1) * GAP
    out, y, n = [], PAD + TITLE_H, 0
    for gname, figs in groups:
        out.append(f'<rect x="{PAD}" y="{y}" width="{width - PAD * 2}" height="{BAND_H - 16}" rx="6" fill="#DBEAFE" stroke="#2563EB" stroke-width="1.5"/>')
        out.append(f'<text x="{PAD + 24}" y="{y + 39}" font-size="30" font-weight="bold" fill="#1F2937">{escape(gname)}</text>')
        y += BAND_H
        for i in range(0, len(figs), COLS):
            row, row_h = figs[i:i + COLS], 0
            for c, (cap, path) in enumerate(row):
                src = path.read_text(encoding="utf-8")
                root = re.search(r"<svg\b[^>]*>", src)
                w, h = (int(re.search(rf'\b{k}="(\d+)"', root.group(0)).group(1)) for k in ("width", "height"))
                inner = src[root.end():src.rindex("</svg>")]
                x = PAD + c * (CELL_W + GAP)
                out.append(f'<text x="{x}" y="{y + 24}" font-size="22" font-weight="bold" fill="#1F2937">{escape(cap)}</text>')
                out.append(f'<svg x="{x}" y="{y + CAP_H}" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{inner}</svg>')
                out.append(f'<rect x="{x}" y="{y + CAP_H}" width="{w}" height="{h}" rx="6" fill="none" stroke="#9CA3AF" stroke-width="1.5"/>')
                row_h, n = max(row_h, h), n + 1
            y += CAP_H + row_h + GAP
        y += GAP // 2
    height = y + PAD - GAP

    label = escape(f"{title} — 전체 그림 {n}개를 한 장에 모은 포스터")
    dest = md.parent / "svg" / f"{chap}-overview-poster.svg"
    dest.write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        f'role="img" aria-label="{label}" font-family="{FONT}">\n<title>{label}</title>\n'
        f'<rect width="100%" height="100%" fill="#FFFFFF"/>\n'
        f'<text x="{PAD}" y="{PAD + 56}" font-size="56" font-weight="bold" fill="#1F2937">{escape(title)}</text>\n'
        f'<text x="{PAD}" y="{PAD + 96}" font-size="22" fill="#6B7280">장 전체 그림 {n}개 · 본문 순서대로 배치</text>\n'
        + "\n".join(out) + "\n</svg>\n", encoding="utf-8")
    assert n == len(re.findall(r"!\[.*?\]\(svg/", md.read_text(encoding="utf-8"))), "빠진 그림이 있다"
    print(f"{dest}  {width}x{height}  그림 {n}개")


if __name__ == "__main__":
    main(sys.argv[1])
