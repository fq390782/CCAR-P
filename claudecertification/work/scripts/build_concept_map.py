"""8장 통합 개념 지도를 조립한다: work/poster8/zone-*.svg 5개를 한 캔버스에 놓고 zone 사이 화살표를 그린다.

사용: python3 -I work/scripts/build_concept_map.py
입력: work/poster8/zone-{a,b,c,d1,d2}.svg, work/poster8/links.json ({"L1": ["라벨 1줄", "2줄"], ...}; 없는 id는 그리지 않는다)
결과: output/Know(CCAR-F&P)/svg/8-concept-map.svg
"""
import json
import re
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "work" / "poster8"
DEST = ROOT / "output" / "Know(CCAR-F&P)" / "svg" / "8-concept-map.svg"
FONT = "Apple SD Gothic Neo, Noto Sans KR, Malgun Gothic, sans-serif"
W, H = 4728, 3228

# zone 키: (제목, x, y, w, h)
ZONES = {
    "b": ("② Tool 정의 설계", 64, 204, 1400, 1500),
    "a": ("① Tool 호출 루프", 1664, 204, 1400, 1500),
    "c": ("③ 통제 · 권한", 3264, 204, 1400, 1500),
    "d1": ("④ MCP 선택 · 프로토콜", 64, 1864, 2040, 1300),
    "d2": ("⑤ MCP 연결 · 운영", 2304, 1864, 2360, 1300),
}
# link id: (x1, y1, x2, y2) — zone 테두리에서 테두리까지
LINKS = {
    "L1": (1464, 524, 1664, 524),
    "L2": (3264, 1104, 3064, 1104),
    "L3": (1980, 1864, 1980, 1704),
    "L4": (2940, 1864, 2940, 1704),
    "L5": (3960, 1704, 3960, 1864),  # 최소 권한(③)이 원칙, MCP tool(⑤)이 적용 대상
    "L6": (760, 1864, 760, 1704),
}


def main():
    labels = json.loads((SRC / "links.json").read_text(encoding="utf-8"))
    out = []
    for key, (title, x, y, w, h) in ZONES.items():
        src = (SRC / f"zone-{key}.svg").read_text(encoding="utf-8")
        root = re.search(r"<svg\b[^>]*>", src)
        size = tuple(int(re.search(rf'(?<![-\w]){k}="(\d+)"', root.group(0)).group(1)) for k in ("width", "height"))
        assert size == (w, h), f"zone-{key}: 크기 {size} != {(w, h)}"
        inner = src[root.end():src.rindex("</svg>")]
        out.append(f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{inner}</svg>')
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="none" stroke="#1F2937" stroke-width="2.5"/>')
        out.append(f'<text x="{x + 28}" y="{y + 50}" font-size="30" font-weight="bold" fill="#1F2937">{escape(title)}</text>')
    for lid, (x1, y1, x2, y2) in LINKS.items():
        lines = labels.get(lid)
        if not lines:
            continue
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#2563EB" stroke-width="5" marker-end="url(#arr-8map)"/>')
        horizontal = y1 == y2
        tx = (x1 + x2) // 2 if horizontal else x1 + 22
        ty = y1 - 16 - 22 * (len(lines) - 1) if horizontal else (y1 + y2) // 2 - 11 * (len(lines) - 1) + 6
        anchor = "middle" if horizontal else "start"
        for i, line in enumerate(lines):
            out.append(f'<text x="{tx}" y="{ty + 22 * i}" font-size="17" font-weight="bold" fill="#2563EB" text-anchor="{anchor}">{escape(line)}</text>')

    label = "8. Tools and MCPs — 장 전체를 한 장으로 이은 개념 지도"
    DEST.write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
        f'aria-label="{label}" font-family="{FONT}">\n<title>{label}</title>\n'
        f'<rect width="100%" height="100%" fill="#FFFFFF"/>\n'
        f'<defs><marker id="arr-8map" markerWidth="5" markerHeight="5" refX="4.2" refY="2.5" orient="auto">'
        f'<path d="M0,0 L5,2.5 L0,5 z" fill="#2563EB"/></marker></defs>\n'
        f'<text x="64" y="104" font-size="56" font-weight="bold" fill="#1F2937">8. Tools and MCPs — 개념 지도</text>\n'
        f'<text x="64" y="150" font-size="22" fill="#6B7280">① 호출 루프가 중심이다. ② 정의 설계와 ③ 통제가 양옆에서 들어오고, ④⑤ MCP가 아래에서 같은 루프로 올라온다. '
        f'파란 굵은 화살표 = zone 사이 연결.</text>\n'
        + "\n".join(out) + "\n</svg>\n", encoding="utf-8")
    ids = re.findall(r'\bid="([^"]+)"', DEST.read_text(encoding="utf-8"))
    assert len(ids) == len(set(ids)), "id가 중복된다"
    print(f"{DEST}  {W}x{H}  links {sorted(k for k in LINKS if labels.get(k))}")


if __name__ == "__main__":
    main()
