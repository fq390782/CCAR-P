"""SVG의 정사각형 영역 하나를 PNG로 렌더링한다 (큰 그림을 확대해서 눈으로 검사할 때 쓴다).

사용: python3 -I work/scripts/svg_crop.py <파일.svg> <x> <y> <size> <출력 폴더>
결과: <출력 폴더>/<이름>_<x>_<y>.svg.png (1600px). qlmanage가 정사각형으로 잘라 내므로 영역도 정사각형만 받는다.
"""
import re
import subprocess
import sys
from pathlib import Path

src, x, y, size, outdir = Path(sys.argv[1]), *map(int, sys.argv[2:5]), Path(sys.argv[5])
text = src.read_text(encoding="utf-8")
tag = re.search(r"<svg\b[^>]*>", text).group(0)
new = tag
for key, val in (("width", size), ("height", size), ("viewBox", f"{x} {y} {size} {size}")):
    new = re.sub(rf'(?<![-\w]){key}="[^"]*"', f'{key}="{val}"', new, count=1)
outdir.mkdir(parents=True, exist_ok=True)
crop = outdir / f"{src.stem}_{x}_{y}.svg"
crop.write_text(text.replace(tag, new, 1), encoding="utf-8")
subprocess.run(["qlmanage", "-t", "-s", "1600", "-o", str(outdir), str(crop)], check=True, capture_output=True)
print(f"{crop}.png")
