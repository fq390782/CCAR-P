#!/usr/bin/env python3
"""8장 통합 개념 지도 zone d1 (④ MCP 선택 · 프로토콜) SVG 생성기.

사용: python3 -I work/poster8/gen_d1.py  → work/poster8/zone-d1.svg
끝에서 글자 넘침 · 상자 겹침 · 화살표 관통 · 캔버스 이탈을 검사해 문제를 출력한다.
"""
import sys
from pathlib import Path
from xml.sax.saxutils import escape

W, H = 2040, 1300
Z = "8map-d1"
C = {"g": ("#F3F4F6", "#9CA3AF"), "b": ("#DBEAFE", "#2563EB"), "r": ("#FEE2E2", "#DC2626"),
     "d": ("#FEF3C7", "#D97706"), "ok": ("#DCFCE7", "#16A34A"), "w": ("#FFFFFF", "#9CA3AF")}
INK, SUB = "#1F2937", "#6B7280"
ARROW = {"k": INK, "b": "#2563EB", "r": "#DC2626", "ok": "#16A34A"}

out, rects, segs, errs = [], [], [], []


def tw(s, size):
    """글자 폭 추정: 한글·기호 = size, 공백 = 0.3, 그 외 = 0.58."""
    return sum(size if ord(c) > 0x1FFF else size * 0.3 if c == " " else size * 0.58 for c in s)


def reg(x, y, w, h, what):
    rects.append((x, y, w, h, what))
    if x < 24 or y < 24 or x + w > W - 24 or y + h > H - 24:
        if not what.startswith("port"):
            errs.append(f"margin: {what} {x:.0f},{y:.0f},{w:.0f},{h:.0f}")
    if x < 600 and y < 70:
        errs.append(f"title area: {what}")


def text(x, y, s, size=13, bold=False, anchor="middle", fill=INK):
    b = ' font-weight="bold"' if bold else ""
    out.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}"{b} text-anchor="{anchor}" fill="{fill}">{escape(s)}</text>')


def label(x, y, s, size=11, anchor="middle", bold=False, fill=INK):
    w = tw(s, size)
    lx = x - w / 2 if anchor == "middle" else x - w if anchor == "end" else x
    reg(lx, y - size, w, size + 3, f"label:{s}")
    text(x, y, s, size, bold, anchor, fill)


def lh(i, head):
    return 18 if (head and i == 0) else 15


def box_h(lines, head=True):
    return 14 + sum(lh(i, head) for i in range(len(lines)))


def box(x, y, w, kind, lines, head=True, h=None, align=None, sw=1.5, stroke=None, what=None):
    need = box_h(lines, head)
    h = h or need
    if h < need:
        errs.append(f"box too short: {lines[0]}")
    fill, st = C[kind]
    out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="6" fill="{fill}" stroke="{stroke or st}" stroke-width="{sw}"/>')
    align = align or ("start" if kind == "r" else "middle")
    cur = y + (h - (need - 14)) / 2
    for i, s in enumerate(lines):
        size = 13 if (head and i == 0) else 11
        if tw(s, size) > w - 12:
            errs.append(f"overflow: '{s}' {tw(s, size):.0f} > {w - 12:.0f}")
        step = lh(i, head)
        tx = x + 8 if align == "start" else x + w / 2
        text(tx, cur + step * 0.74, s, size, head and i == 0, align)
        cur += step
    reg(x, y, w, h, what or f"box:{lines[0]}")
    return (x, y, w, h)


def diamond(cx, cy, w, h, lines):
    fill, st = C["d"]
    out.append(f'<polygon points="{cx:.1f},{cy - h / 2:.1f} {cx + w / 2:.1f},{cy:.1f} {cx:.1f},{cy + h / 2:.1f} {cx - w / 2:.1f},{cy:.1f}" fill="{fill}" stroke="{st}" stroke-width="1.5"/>')
    cap = w * (1 - 15 / (h / 2))
    ys = [cy + 4] if len(lines) == 1 else [cy - 4, cy + 12]
    for s, ty in zip(lines, ys):
        if tw(s, 13) > cap:
            errs.append(f"diamond overflow: '{s}' {tw(s, 13):.0f} > {cap:.0f}")
        text(cx, ty, s, 13)
    reg(cx - w / 2, cy - h / 2, w, h, f"diamond:{lines[0]}")


def arrow(pts, lab, lpos, color="k", width=1.5, anchor="middle", dash=False):
    """pts: 꺾은선 좌표. lab: 라벨, lpos: 라벨 (x, baseline y)."""
    col = ARROW[color]
    d = ' stroke-dasharray="5 4"' if dash else ""
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    mk = f"arr-{Z}" if color == "k" else f"arr-{Z}-{color}"
    out.append(f'<polyline points="{p}" fill="none" stroke="{col}" stroke-width="{width}"{d} marker-end="url(#{mk})"/>')
    for a, b in zip(pts, pts[1:]):
        segs.append((a, b, lab))
    label(lpos[0], lpos[1], lab, anchor=anchor)


def harrow(x1, x2, y, lab, color="k", **kw):
    arrow([(x1, y), (x2, y)], lab, ((x1 + x2) / 2, y - 6), color, **kw)


def varrow(x, y1, y2, lab, color="k", side="right", **kw):
    if side == "right":
        arrow([(x, y1), (x, y2)], lab, (x + 8, (y1 + y2) / 2 + 4), color, anchor="start", **kw)
    else:
        arrow([(x, y1), (x, y2)], lab, (x - 8, (y1 + y2) / 2 + 4), color, anchor="end", **kw)


def heading(x, y, s):
    label(x, y, s, 13, "start", True)


# ---------- 열 배치 ----------
COLS = [(24, 402), (442, 402), (860, 402), (1278, 402), (1696, 320)]
FY0, FY1 = 150, 1276
BB_Y, BB_H, BB_W = 82, 52, 250
DW, DH, GAP = 198, 104, 36


def frame(i, title, sub, gid):
    x, w = COLS[i]
    out.append(f'<g id="{Z}-{gid}">')
    out.append(f'<rect x="{x}" y="{FY0}" width="{w}" height="{FY1 - FY0}" rx="6" fill="#FFFFFF" stroke="#9CA3AF" stroke-width="1.5"/>')
    label(x + 10, 178, title, 16, "start", True)
    label(x + 10, 197, sub, 11, "start", fill=SUB)
    return x + 10, w - 20


def chain(x0, iw, y, rows, gap=16):
    """왼쪽 = 마름모(또는 주 상자) 세로 사슬, 오른쪽 = 결과 상자 + 바로 아래 오답 상자."""
    rx, rw = x0 + DW + GAP, iw - DW - GAP
    cx = x0 + DW / 2
    prev_bottom, prev_down = None, None
    for r in rows:
        if "d" in r:
            hb = box_h(r["side_box"])
            cy = y + max(DH, hb) / 2
            left_top, left_bottom = cy - DH / 2, cy + DH / 2
            if prev_bottom is not None:
                varrow(cx, prev_bottom, left_top, prev_down)
            diamond(cx, cy, DW, DH, r["d"])
            kind = r.get("kind", "b")
            box(rx, cy - hb / 2, rw, kind, r["side_box"])
            harrow(x0 + DW, rx, cy, r["side"], "ok" if kind == "ok" else "b")
            bottom = max(left_bottom, cy + hb / 2)
            if r.get("under"):
                uk, ul = r["under"]
                b = box(rx, cy + hb / 2 + 8, rw, uk, ul, head=False)
                bottom = max(bottom, b[1] + b[3])
        else:
            if prev_bottom is not None:
                varrow(cx, prev_bottom, y, prev_down)
            b = box(x0, y, DW, r.get("kind", "b"), r["box"])
            left_bottom = bottom = y + b[3]
            if r.get("under"):
                uk, ul = r["under"]
                b2 = box(rx, y, rw, uk, ul, head=False)
                bottom = max(bottom, y + b2[3])
        prev_bottom, prev_down = left_bottom, r.get("down")
        y = max(bottom + gap, left_bottom + 44)
    chain.last = (cx, left_bottom, prev_down)
    return y


def pairs(x0, iw, y, rows, lw):
    """조건 | 정답 2칸 행 (화살표 없음)."""
    for a, b in rows:
        h = max(box_h(a, False), box_h(b, False))
        box(x0, y, lw, "g", a, head=False, h=h)
        box(x0 + lw, y, iw - lw, "b", b, head=False, h=h)
        y += h + 6
    return y


# ---------- 머리말 ----------
out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
           f'aria-label="MCP 선택과 프로토콜: 통합 방식 선택에서 확장 수단, primitives, transport, tools/list와 tools/call까지 이어지는 흐름" '
           f'font-family="Apple SD Gothic Neo, Noto Sans KR, Malgun Gothic, sans-serif">')
out.append("<title>④ MCP 선택 · 프로토콜: 통합 방식 → 확장 수단 → primitives → transport → discovery · 호출</title>")
out.append('<rect width="100%" height="100%" fill="#FFFFFF"/>')
out.append("<defs>")
for k, col in ARROW.items():
    mid = f"arr-{Z}" if k == "k" else f"arr-{Z}-{k}"
    out.append(f'<marker id="{mid}" markerUnits="userSpaceOnUse" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{col}"/></marker>')
out.append("</defs>")

# ---------- backbone ----------
out.append(f'<g id="{Z}-backbone">')
BB = [("① 어떻게 연결하나", "통합 방식 선택"), ("② 무엇으로 확장하나", "확장 수단 선택"),
      ("③ 무엇을 노출하나", "MCP primitives"), ("④ 어떤 경로로 잇나", "MCP transport"),
      ("⑤ 어떻게 찾고 부르나", "discovery · 호출")]
BBL = ["MCP 선택", "MCP server 선택", "노출 내용 확정", "연결 수립"]
bbx = []
for i, (x, w) in enumerate(COLS):
    cx = x + w / 2
    bx = cx - BB_W / 2
    bbx.append(bx)
    box(bx, BB_Y, BB_W, "g", list(BB[i]), h=BB_H, sw=2.5, stroke=INK, what=f"backbone{i}")
    out.append(f'<line x1="{cx}" y1="{BB_Y + BB_H}" x2="{cx}" y2="{FY0}" stroke="{INK}" stroke-width="2.5"/>')
for i in range(4):
    harrow(bbx[i] + BB_W, bbx[i + 1], BB_Y + BB_H / 2, BBL[i], width=2.5)
# port (위 변)
box(606, 6, 180, "b", ["MCP tools = tool 정의"], h=34, what="port-696")
arrow([(696, BB_Y), (696, 40)], "서버의 tools → 모델용 tool 정의 증가", (706, 66), "b", 2.5, anchor="start")
box(1818, 6, 196, "b", ["tools/list · tools/call"], h=34, what="port-1916")
arrow([(1916, BB_Y), (1916, 40)], "발견 · 실행", (1906, 66), "b", 2.5, anchor="end")
out.append("</g>")

# ---------- 1-24 통합 방식 선택 ----------
x0, iw = frame(0, "1-24 통합 방식 선택", "재사용이 실제로 있을 때만 MCP", "c1-24")
y = chain(x0, iw, 214, [
    dict(d=["연결 상대가 agent?", "(자체 plan · tools)"], side="예",
         side_box=["agent-to-agent", "+ handoff 계약", "agent ↔ agent 연결", "비용: 담당자 · 계약 필요"],
         under=("r", ["✗ REST API · CRM에 연결", "→ CRM은 agent ✗", "✗ 별개 벤더 agent에 MCP", "→ MCP = agent ↔ tool"]),
         down="아니오"),
    dict(d=["소비자 여러 개?", "(호스트 · 언어 · 팀)"], side="예",
         side_box=["MCP server 1개", "schema 1개", "agent ↔ tool · 데이터", "비용: 새로 소유할", "service"],
         under=("r", ["✗ \"MCP는 표준\" · \"미래", "재사용\" 근거로 구축", "→ 비용만 · 얻는 기능 없음", "✗ 일회성 · 단일 쌍에 MCP"]),
         down="아니오"),
    dict(d=["기능이 CLI로만", "존재?"], side="예",
         side_box=["CLI wrapper", "+ 형식 변경 테스트", "일회성 · 소비자 1", "비용: 취약한 parsing"],
         under=("r", ["✗ 언어별 CLI wrapper", "→ 취약한 parsing이", "언어 수만큼 증가", "✗ CLI 위에 MCP를 얹음", "→ 계층마다 실패 모드"]),
         down="아니오"),
    dict(box=["직접 API/SDK", "프로토콜 계층 생략", "호스트 1 · 언어 1 · 소비자 1", "비용: 소비자마다 client 업데이트"],
         under=("r", ["✗ 단일 호스트에 stdio", "서버 등록 · MCP wrapper", "→ 불필요한 프로토콜 계층", "✗ MCP + 직접 REST 병행", "→ 유지보수 범위 2배"]),
         down="두 번째 팀 · 언어 등장"),
    dict(box=["통합 방식 재평가", "비교 기준: 재사용 · 보안 경계", "소유권 · 운영 복잡도"], kind="g"),
], gap=14)
y += 6
heading(x0, y + 12, "그 밖의 조건 → 방식")
y = pairs(x0, iw, y + 24, [
    (["독점 SDK만 존재 + 여러 팀"], ["SDK를 MCP server 하나로 감쌈"]),
    (["공유 기능 + 소비자 8개"], ["MCP server 또는 공유 library"]),
    (["필요한 것이 tool 하나"], ["tool만 노출한 MCP server"]),
    (["벤더가 typed API 출시"], ["CLI wrapper → 직접 API 이전"]),
    (["규제로 schema 공유 불가"], ["소비자별 개별 구현"]),
    (["운영 부담 0 요구"], ["관리형 런타임"]),
], 180)
print("c1 end", y)
out.append("</g>")

# ---------- 1-10 확장 수단 선택 ----------
x0, iw = frame(1, "1-10 확장 수단 선택", "공유 · 독립 유지보수 = MCP server · 절차 = Skill", "c1-10")
y = chain(x0, iw, 214, [
    dict(d=["행동 · 데이터 접근", "필요?"], side="아니오",
         side_box=["Skill", "지시 · 템플릿 · 절차 묶음", "작업 일치 시 로드", "live connection ✗"],
         under=("r", ["✗ Skill로 API 연결", "→ live connection 없음", "✗ 절차에 MCP server ·", "fine-tuning → 과함"]),
         down="예"),
    dict(d=["여러 앱 공유 +", "독립 유지보수?"], side="아니오",
         side_box=["앱의 Tools", "행동 · 데이터 접근 추가", "(MCP server와 공통)"],
         under=("r", ["✗ 데이터를 매일 system", "prompt에 붙여 넣기", "→ 낡음 · context 낭비"]),
         down="예"),
    dict(box=["MCP server", "서버가 tools/resources 노출", "여러 client 연결", "플랫폼 팀이 독립 유지보수"],
         under=("r", ["✗ 앱마다 서버 코드 복사", "→ 복사본끼리 어긋남", "✗ Messages API 대체 ·", "모델과 같은 프로세스 필요", "→ 둘 다 ✗"]),
         down="어느 서버를 쓰나"),
    dict(d=["많은 조직이", "공통 사용?"], side="예",
         side_box=["기성 MCP server", "GitHub · Slack · Jira", "연결만으로 사용", "유지보수 = 제공처"],
         under=("g", ["채택 전 확인", "제공처 · 업데이트 상황", "요구 권한 범위"]),
         down="아니오 (자사에만 존재)"),
    dict(box=["custom MCP server", "팀 고유 workflow", "(2단계 승인 · 예약 · release 판정)", "범위를 좁혀 고유 로직만"],
         under=("r", ["✗ 표준 서비스까지", "custom으로 직접 구축", "→ 표준 조작의", "유지보수까지 떠안음"])),
], gap=14)
y += 4
heading(x0, y + 12, "혼합 구성")
y += 24
b = box(x0, y, iw, "g", ["요건 분해", "표준 조작 · 자체 로직으로 나눠 각각 가장 수고 적은 수단"])
y2 = y + b[3] + 46
bw = (iw - 10) / 2
box(x0, y2, bw, "b", ["기성 서버", "표준 조작"])
box(x0 + bw + 10, y2, bw, "b", ["custom 서버", "release 판정 · 승인 준비"])
varrow(x0 + bw / 2, y + b[3], y2, "표준 조작", "b")
varrow(x0 + bw + 10 + bw / 2, y + b[3], y2, "자체 로직", "b")
y = y2 + box_h(["a", "b"]) + 10
b = box(x0, y, iw, "g", ["개발자 1명 · 보수 최소화 = 기성 서버 우선",
                         "팀 서버 = project scope .mcp.json · 토큰 = 환경 변수 확장"], head=False)
y += b[3] + 8
b = box(x0, y, iw, "r", ["✗ 여러 통합을 custom server 하나로 통합", "→ 표준 연동 유지보수 부담 잔존"], head=False)
y += b[3]
print("c2 end", y)
out.append("</g>")

# ---------- 1-11 MCP primitives ----------
x0, iw = frame(2, "1-11 MCP primitives", "주도 = tools 모델 · resources 앱 · prompts 사용자", "c1-11")
P = [
    ("모델 주도", ["tools", "상황에 따라 찾아 호출", "동작 수행 (예: Jira 티켓 생성)"],
     ["✗ 카탈로그 목록을 tool로 조회", "→ 모델의 탐색 turn 발생", "(예: 작업마다 7회 호출)"]),
    ("앱 주도", ["resources", "참조 데이터를 URI로 노출", "(파일 · DB 스키마 · 문서)", "context 포함 여부 = 앱 결정"],
     ["✗ tool 사양서를 resource로", "→ 호출 가능 tool 등록 ✗"]),
    ("사용자 주도", ["prompts", "재사용 프롬프트 템플릿", "slash command 등으로 선택"],
     ["✗ 카탈로그를 prompt로 공개", "→ 사용자가 기동하는 템플릿", "✗ 모델의 자동 tool 탐색 용도"]),
]
pdw, pdh = 156, 90
bx, bw = x0 + 204, iw - 204
y, centers = 214, []
for lab, blue, red in P:
    b = box(bx, y, bw, "b", blue)
    centers.append(y + b[3] / 2)
    r = box(bx, y + b[3] + 8, bw, "r", red, head=False)
    y = r[1] + r[3] + 42
cx, cy = x0 + pdw / 2, centers[1]
diamond(cx, cy, pdw, pdh, ["누가 언제", "쓰는가?"])
arrow([(cx, cy - pdh / 2), (cx, centers[0]), (bx, centers[0])], P[0][0], ((cx + bx) / 2 + 4, centers[0] - 6), "b")
harrow(x0 + pdw, bx, cy, P[1][0], "b")
arrow([(cx, cy + pdh / 2), (cx, centers[2]), (bx, centers[2])], P[2][0], ((cx + bx) / 2 + 4, centers[2] - 6), "b")
y += 2
heading(x0, y + 12, "정적 카탈로그 + 조작 → resource + tool")
y += 26
hb = box(x0, y, 110, "g", ["host", "목록 탐색", "선택분만 첨부"], h=62)
sb = box(x0 + iw - 120, y, 120, "g", ["MCP server", "카탈로그", "= resource"], h=62)
harrow(x0 + 110, x0 + iw - 120, y + 18, "resources/list", "b")
harrow(x0 + 110, x0 + iw - 120, y + 46, "resources/read (선택분)", "b")
y2 = y + 62 + 56
varrow(x0 + 55, y + 62, y2, "context에 첨부", "ok")
varrow(x0 + iw - 60, y + 62, y2, "조작만 tool로", "b", side="left")
box(x0, y2, 176, "ok", ["모델", "탐색 turn 회피"])
box(x0 + iw - 190, y2, 190, "b", ["tool = 조작만", "예: create_return"])
y = y2 + box_h(["a", "b"]) + 12
b = box(x0, y, iw, "r", ["✗ 카탈로그를 CLAUDE.md에 복사 → 상시 로딩",
                         "✗ 목록 tool의 반환 건수 확대 · description에 목록 전문",
                         "→ 대량 정보를 매번 context에 투입"], head=False)
y += b[3] + 22
heading(x0, y + 12, "요구 → primitive")
y = pairs(x0, iw, y + 24, [
    (["동작 수행 (Jira 티켓 생성)"], ["tool"]),
    (["사용자가 첨부하는 읽기 전용 데이터", "(API schema 파일)"], ["resource"]),
    (["재사용 템플릿 · 노하우", "(심각도 기준 triage 템플릿)"], ["prompt"]),
], 250) + 16
heading(x0, y + 12, "운영 · 첨부")
y += 24
b1 = box(x0, y, 150, "g", ["내용 개정", "resource 갱신"])
b2 = box(x0 + iw - 150, y, 150, "g", ["client", "Claude Code = @로 참조"])
harrow(x0 + 150, x0 + iw - 150, y + b1[3] / 2, "변경 알림")
y += b1[3]
print("c3 end", y)
out.append("</g>")

# ---------- 1-13 MCP transport ----------
x0, iw = frame(3, "1-13 MCP transport", "로컬 = stdio · 원격 = Streamable HTTP", "c1-13")
y = 214
out.append(f'<rect x="{x0}" y="{y}" width="150" height="124" rx="6" fill="#FFFFFF" stroke="#9CA3AF" stroke-width="1.5"/>')
label(x0 + 75, y + 18, "host", 13, bold=True)
label(x0 + 75, y + 33, "예: Claude Code", 11, fill=SUB)
box(x0 + 10, y + 42, 130, "g", ["client A"], h=32)
box(x0 + 10, y + 82, 130, "g", ["client B"], h=32)
box(x0 + iw - 120, y + 42, 120, "g", ["로컬 server"], h=32)
box(x0 + iw - 120, y + 82, 120, "g", ["원격 server"], h=32)
harrow(x0 + 140, x0 + iw - 120, y + 58, "stdio")
harrow(x0 + 140, x0 + iw - 120, y + 98, "Streamable HTTP")
label(x0 + 160, y + 18, "서버마다 client 하나 · 전용 연결", 11, "start")
y += 124 + 8
b = box(x0, y, iw, "g", ["서버마다 tools/list → host가 모아 제시 · 호출은 소유 서버로 분배"], head=False)
y += b[3] + 44
heading(x0, y + 12, "Claude Code transport 선택 ① 위치 ② 방향 ③ 인증")
y = chain(x0, iw, y + 24, [
    dict(d=["① 연결 대상이", "로컬 프로세스?"], side="예",
         side_box=["stdio", "subprocess · 표준 입출력", "로컬 파일 · CLI 접근", "네트워크 오버헤드 없음"],
         under=("r", ["✗ 원격 서버를 각 단말에", "배포해 stdio → 업데이트", "· 인증 중앙 관리 ✗"]),
         down="아니오 (원격)"),
    dict(d=["② 서버가 이벤트를", "자발 전송?"], side="예",
         side_box=["WebSocket", "양방향 지속 연결", "헤더 인증만 · OAuth ✗"],
         under=("r", ["✗ WebSocket으로", "OAuth 로그인"]),
         down="아니오 (요청 응답만)"),
    dict(box=["http (Streamable HTTP)", "HTTP POST + 선택적 SSE", "원격 서버를 여러 client에 제공", "Bearer · API key · 커스텀 헤더", "토큰 획득 = OAuth 권장"],
         under=("r", ["✗ sse transport 선택", "→ deprecated", "✗ 로컬 subprocess", "서버에 HTTP → 오버헤드", "· 포트 노출 · 인증 부담"]),
         down="③ OAuth 로그인 필요"),
], gap=26)
b = box(x0, y, iw, "ok", ["claude mcp add --transport http <URL>", "→ /mcp에서 브라우저 인증"])
varrow(chain.last[0], chain.last[1], y, chain.last[2], "ok")
y += b[3] + 8
y = pairs(x0, iw, y, [
    (["사내 클라우드 · 응답만 · OAuth"], ["3조건 모두 HTTP"]),
    (["로컬 프로세스 → 사내 클라우드 이전"], ["각자 --transport http로", "URL 추가"]),
], 210) + 40
heading(x0, y + 12, "여러 서버 + subagent")
y += 24
b = box(x0, y, iw, "b", ["필요한 서버에 동시 연결 = 표준 형태", "역할별 서버만 할당 · 연결 유지"])
y += b[3] + 8
b = box(x0, y, iw, "r", ["✗ subagent당 서버 1개 + 필요 시 재연결 → 단계마다 중단",
                         "✗ 자체 서버로 집약 → 불필요한 개발 부담",
                         "✗ 로컬 · 원격 모두 stdio 또는 모두 HTTP",
                         "→ 배포 위치 · 제공 범위에 따라 구분"], head=False)
y += b[3]
print("c4 end", y)
out.append("</g>")

# ---------- 1-12 MCP tool discovery ----------
x0, iw = frame(4, "1-12 tool discovery · 호출", "발견 = tools/list · 실행 = tools/call", "c1-12")
ax = x0 + 40
y = 214
b = box(x0, y, iw, "g", ["MCP server", "tools capability 선언"])
y1 = y + b[3]
y = y1 + 70
arrow([(ax, y1), (ax, y)], "tools/list 응답", (ax + 10, y1 + 31), "b", anchor="start")
label(ax + 10, y1 + 47, "name · description · inputSchema", 11, "start")
b = box(x0, y, iw, "b", ["client: 모델용 tool 정의로 변환", "서버에 tool 추가 → 앱 코드 그대로 노출"])
y1 = y + b[3]
y = y1 + 72
varrow(ax, y1, y, "tool 정의 전달", "b")
rh = box_h(["a"] * 5, False)
box(x0, y, 120, "g", ["모델", "tool 선택"], h=rh)
box(x0 + 130, y, iw - 130, "r", ["✗ tool 발견에 prompts ·", "resources 사용", "✗ 빈 인자로 tools/call", "시험 호출", "→ 발견 = tools/list"], head=False)
y1 = y + rh
y = y1 + 72
varrow(ax, y1, y, "고른 tool", "b")
b = box(x0, y, iw, "b", ["client: tools/call", "모델이 고른 tool을 실행"])
y1 = y + b[3]
dw, dh = 150, 90
y = y1 + 72
varrow(x0 + dw / 2, y1, y, "입력 검증")
cy = y + dh / 2
diamond(x0 + dw / 2, cy, dw, dh, ["입력 검증", "통과?"])
gb = box(x0 + dw + 40, cy - 25, iw - dw - 40, "ok", ["tool 결과", "모델에 반환"], h=50)
harrow(x0 + dw, x0 + dw + 40, cy, "예", "ok")
y1 = cy + dh / 2
y = y1 + 60
varrow(x0 + dw / 2, y1, y, "아니오")
b = box(x0, y, iw, "b", ["isError 붙은 tool 실행 에러", "모델에 반환 → 자가 수정용 (발견 수단 ✗)"])
y += b[3] + 34
heading(x0, y + 12, "목록 변경")
y += 24
b = box(x0, y, iw, "g", ["listChanged 선언 서버"], h=34)
y1 = y + 34
y = y1 + 58
arrow([(ax, y1), (ax, y)], "notifications/tools/list_changed", (ax + 10, (y1 + y) / 2 + 4), "k", anchor="start", dash=True)
b = box(x0, y, iw, "g", ["client 재조회 (tools/list)"], h=34)
y += 34 + 8
out.append(f'<line x1="{x0 + 2}" y1="{y + 8}" x2="{x0 + 34}" y2="{y + 8}" stroke="{INK}" stroke-width="1.5" stroke-dasharray="5 4"/>')
label(x0 + 42, y + 12, "점선 = 비동기 알림", 11, "start", fill=SUB)
y += 44
b = box(x0, y, iw, "g", ["2026-07-28판 사양", "프로토콜 session ✗ (stateless)", "연결별 tool 목록 변경 금지",
                         "요청 인가에 따른 변경 허용", "→ 공식 MCP 사양과 일치"])
y += b[3]
print("c5 end", y)
out.append("</g>")
out.append("</svg>")

# ---------- 검사 ----------
def hit(a, b):
    return a[0] < b[0] + b[2] - 0.5 and b[0] < a[0] + a[2] - 0.5 and a[1] < b[1] + b[3] - 0.5 and b[1] < a[1] + a[3] - 0.5


for i, a in enumerate(rects):
    for b in rects[i + 1:]:
        if hit(a, b):
            errs.append(f"overlap: {a[4]} <-> {b[4]}")
for (p, q, lab) in segs:
    sx, sy = min(p[0], q[0]), min(p[1], q[1])
    s = (sx - 0.5, sy - 0.5, abs(p[0] - q[0]) + 1, abs(p[1] - q[1]) + 1, "seg")
    for r in rects:
        inner = (r[0] + 2, r[1] + 2, r[2] - 4, r[3] - 4, r[4])
        if hit(s, inner):
            errs.append(f"arrow '{lab}' crosses {r[4]}")
for e in errs:
    print("ERR", e)
dst = Path(__file__).resolve().parent / "zone-d1.svg"
dst.write_text("\n".join(out) + "\n", encoding="utf-8")
print(dst, "errors:", len(errs))
sys.exit(1 if errs else 0)
