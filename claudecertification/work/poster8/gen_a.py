"""8장 통합 개념 지도 zone a(① Tool 호출 루프) SVG 생성기. 표준 라이브러리만 사용.

실행: python3 -I work/poster8/gen_a.py  → work/poster8/zone-a.svg
넘침 · 겹침 · 화살표 관통 · 여백 위반을 스스로 검사해 WARN으로 출력한다.
"""
from pathlib import Path
from xml.sax.saxutils import escape

W, H, Z = 1400, 1500, "8map-a"
FONT = "Apple SD Gothic Neo, Noto Sans KR, Malgun Gothic, sans-serif"
INK, SUB = "#1F2937", "#6B7280"
PAL = {  # kind: (fill, stroke)
    "g": ("#F3F4F6", "#9CA3AF"), "b": ("#DBEAFE", "#2563EB"), "r": ("#FEE2E2", "#DC2626"),
    "d": ("#FEF3C7", "#D97706"), "ok": ("#DCFCE7", "#16A34A"),
}
ARROW = {"n": INK, "b": "#2563EB", "r": "#DC2626", "ok": "#16A34A"}

out, leaf, frames, labels, segs, warns = [], [], [], [], [], []


def tw(s, size, bold=False):
    w = 0.0
    for ch in s:
        if ch == " ":
            w += size * 0.3
        elif ch in "·'":
            w += size * 0.45
        elif ord(ch) < 128:
            w += size * 0.58
        else:
            w += size
    return w * (1.05 if bold else 1)


def parse(line):
    """'#' = 14 bold(backbone), '!' = 13 bold, '~' = 11, 그 외 13."""
    if line[0] == "#":
        return line[1:], 14, True
    if line[0] == "!":
        return line[1:], 13, True
    if line[0] == "~":
        return line[1:], 11, False
    return line, 13, False


def text_block(name, cx, cy, lines, maxw, maxh):
    parsed = [parse(l) for l in lines]
    hs = [18 if s >= 13 else 15 for _, s, _ in parsed]
    total = sum(hs)
    if total > maxh:
        warns.append(f"{name}: text height {total} > {maxh}")
    y = cy - total / 2
    for (t, s, b), h in zip(parsed, hs):
        if tw(t, s, b) > maxw:
            warns.append(f"{name}: '{t}' width {tw(t, s, b):.0f} > {maxw:.0f}")
        weight = ' font-weight="bold"' if b else ""
        out.append(f'<text x="{cx:g}" y="{y + h * 0.74:g}" font-size="{s}"{weight} '
                   f'text-anchor="middle" fill="{INK}">{escape(t)}</text>')
        y += h


def box(name, x, y, w, h, kind, lines):
    f, s = PAL[kind]
    out.append(f'<rect id="{Z}-{name}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="6" '
               f'fill="{f}" stroke="{s}" stroke-width="1.5"/>')
    text_block(name, x + w / 2, y + h / 2, lines, w - 14, h - 8)
    leaf.append((name, x, y, x + w, y + h))


def diamond(name, cx, cy, w, h, lines):
    f, s = PAL["d"]
    pts = f"{cx:g},{cy - h / 2:g} {cx + w / 2:g},{cy:g} {cx:g},{cy + h / 2:g} {cx - w / 2:g},{cy:g}"
    out.append(f'<polygon id="{Z}-{name}" points="{pts}" fill="{f}" stroke="{s}" stroke-width="1.5"/>')
    text_block(name, cx, cy, lines, w * 0.62, h * 0.7)
    leaf.append((name, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2))


def frame(name, x, y, w, h, title):
    out.append(f'<rect id="{Z}-{name}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="6" '
               f'fill="#FFFFFF" stroke="#9CA3AF" stroke-width="1"/>')
    out.append(f'<text x="{x + 12:g}" y="{y + 24:g}" font-size="16" font-weight="bold" fill="{INK}">{escape(title)}</text>')
    frames.append((name, x, y, x + w, y + h))
    labels.append((name + "-title", x + 12, y + 9, x + 12 + tw(title, 16, True), y + 28))


def arrow(pts, label, lx, ly, anchor="middle", color="n", bb=False, size=None):
    """pts: 꺾이는 점 목록. 마지막 점이 화살촉 끝. label은 (lx, ly) baseline에 둔다."""
    size = size or (13 if bb else 11)
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    d = max(abs(x2 - x1), abs(y2 - y1))
    if d < 16:
        warns.append(f"arrow '{label}': last segment only {d}px")
    ex, ey = x2 - (x2 - x1) / d * 4, y2 - (y2 - y1) / d * 4  # 화살촉 길이만큼 선을 줄인다
    path = " ".join(f"{x:g},{y:g}" for x, y in pts[:-1] + [(ex, ey)])
    out.append(f'<polyline points="{path}" fill="none" stroke="{ARROW[color]}" '
               f'stroke-width="{2.5 if bb else 1.5}" marker-end="url(#arr-{Z}{"" if color == "n" else "-" + color})"/>')
    for a, b in zip(pts, pts[1:]):
        if a[0] != b[0] and a[1] != b[1]:
            warns.append(f"arrow '{label}': diagonal segment")
        segs.append((label, a, b))
    w = tw(label, size, bb)
    x0 = lx - w / 2 if anchor == "middle" else (lx if anchor == "start" else lx - w)
    weight = ' font-weight="bold"' if bb else ""
    out.append(f'<text x="{lx:g}" y="{ly:g}" font-size="{size}"{weight} text-anchor="{anchor}" '
               f'fill="{INK if bb else SUB}">{escape(label)}</text>')
    labels.append((label, x0, ly - size * 0.85, x0 + w, ly + size * 0.25))


# ───────────────────────── backbone 노드 ─────────────────────────
CX = 1276  # 오른쪽 열 중심
box("req", 24, 244, 240, 152, "b",
    ["#① 요청 조립 (앱)", "messages", "tools (정의 · strict)", "tool_choice"])           # port 왼쪽 (0,320)
box("claude", 600, 276, 240, 88, "b",
    ["#② Claude 판단", "어떤 tool · 어떤 인자 결정", "~tool_use 요청만 · 실행은 앱"])
diamond("stop", CX, 320, 196, 90, ["#③ stop_reason?"])
box("final", 1180, 96, 192, 80, "ok", ["#최종 답", "loop 종료"])
box("tooluse", 1176, 460, 200, 90, "b",
    ["#④ tool_use 블록", "id · name · input", "~한 턴에 여러 개 = 병렬"])
box("exec", 1176, 850, 200, 100, "b",
    ["#⑤ 앱이 tool 실행", "앱 코드가 각 tool 실행", "~권한 검사 · 게이트 = 앱"])      # port 오른쪽 (1400,900)
diamond("okq", 1050, 900, 170, 96, ["#⑥ 실행", "#성공?"])
box("result", 580, 856, 300, 88, "b",
    ["#⑦ tool_result → 한 user 메시지", "모든 결과 · 같은 tool_use_id로 짝", "~assistant tool_use 턴 바로 다음"])
box("next", 24, 500, 300, 90, "b",
    ["#⑧ 다음 요청", "messages 전체 재전송", "~stateless: 모델이 기억 ✗"])

# ───────────────────────── backbone 화살표 ─────────────────────────
arrow([(264, 320), (600, 320)], "messages + tools + tool_choice", 432, 311, color="b", bb=True)
arrow([(840, 320), (1178, 320)], "응답 (content + stop_reason)", 1009, 311, color="b", bb=True)
arrow([(CX, 275), (CX, 176)], "end_turn 등", CX + 9, 230, "start", "ok", True)
arrow([(CX, 365), (CX, 460)], "tool_use", CX + 9, 418, "start", "b", True)
arrow([(CX, 550), (CX, 850)], "블록마다 실행", CX + 9, 705, "start", "b", True)
arrow([(1176, 900), (1135, 900)], "결과", 1157, 890, color="b", bb=True)
arrow([(965, 900), (880, 900)], "성공", 924, 890, color="b", bb=True)
arrow([(1050, 948), (1050, 1016)], "실패", 1059, 969, "start", "r", True)
arrow([(860, 1016), (860, 944)], "is_error: true", 869, 969, "start", "b", True)
arrow([(580, 900), (64, 900), (64, 590)], "assistant 턴 + user 메시지를 이력에 추가", 330, 890, color="b", bb=True)
arrow([(64, 500), (64, 396)], "재전송", 73, 453, "start", "b", True)

# ───────────────────────── 1-5 strict (위 띠) ─────────────────────────
frame("c15", 24, 84, 1126, 120, "1-5 Strict tool use — 입력 형식 보장 수단 = strict: true뿐")
box("c15-limit", 36, 118, 234, 74, "g",
    ["!strict의 한계", "~maximum 등 수치 제약 미지원", "~→ 상한 통제 = 앱 · SDK 검증 병행"])
box("c15-strict", 326, 118, 250, 74, "b",
    ["!strict: true (tool 정의)", "~input이 input_schema를 따르도록 검증", "~타입 오류 · 필수 필드 누락 근원 차단"])
diamond("c15-q", 745, 155, 190, 74, ["!입력 형식", "!보장 수단?"])
box("c15-trap", 900, 118, 238, 74, "r",
    ["!형식 보장 ✗", "~prompt 형식 요청 · 검증 후 재시도", "~description 늘림 · temperature 낮춤", "~tool_choice: auto (기본값)"])
arrow([(650, 155), (576, 155)], "생성 시 제약", 613, 147, color="b")
arrow([(326, 155), (270, 155)], "한계", 298, 147)
arrow([(840, 155), (900, 155)], "그 외", 870, 147, color="r")
arrow([(144, 204), (144, 244)], "strict: true", 153, 229, "start", "b")

# ───────────────────────── 1-4 tool_choice ─────────────────────────
frame("c14", 350, 410, 450, 430, "1-4 tool_choice")
diamond("c14-q1", 450, 478, 176, 64, ["!호출 강제", "!필요?"])
box("c14-auto", 596, 450, 192, 56, "g", ["!auto (기본값)", "~호출 여부 = 모델 판단", "~호출 보장 ✗"])
diamond("c14-q2", 450, 576, 176, 64, ["!출구 tool", "!몇 개?"])
box("c14-any", 596, 546, 192, 60, "b", ["!any", "~어느 tool이든 호출 · 선택 = 모델", "~+ 빈 결과 보고 tool"])
box("c14-tool", 362, 640, 178, 52, "b", ["!tool + name", "~지정 tool 호출 보장"])
box("c14-first", 596, 640, 192, 52, "g", ["!첫 단계만 고정", "~첫 요청 tool → 이후 auto"])
box("c14-400", 362, 704, 426, 62, "g",
    ["!any · tool 미지원(오류) → auto + prompt 지시 + strict",
     "~일부 신규 모델 · 수동 extended thinking 활성",
     "~400 변경 = 시험 가이드(2026년 7월판) 이후 · 시험 = 강제 가능 전제"])
box("c14-t1", 362, 778, 208, 50, "r", ["!모든 요청에 tool 고정 ✗", "~같은 tool만 반복 · 후속 호출 차단"])
box("c14-t2", 580, 778, 208, 50, "r", ["!오선택을 강제로 교정 ✗", "~선택 문제 우회 → description 수정"])
arrow([(538, 478), (596, 478)], "아니오", 566, 470)
arrow([(450, 510), (450, 544)], "예", 458, 531, "start")
arrow([(538, 576), (596, 576)], "여럿", 566, 568, color="b")
arrow([(450, 608), (450, 640)], "하나", 458, 628, "start", "b")
arrow([(540, 666), (596, 666)], "요청 단위", 568, 658)
arrow([(350, 450), (200, 450), (200, 396)], "tool_choice", 276, 442, color="b")

# ───────────────────────── 1-2 parallel ─────────────────────────
frame("c12", 820, 410, 265, 390, "1-2 Parallel tool use")
box("c12-turn", 832, 448, 241, 56, "g", ["!한 assistant 턴", "~tool_use 블록 여러 개 가능"])
box("c12-one", 832, 544, 241, 72, "b",
    ["!결과 = 한 user 메시지에 모음", "~tool_result 블록 = 배열 맨 앞", "~덧붙이는 텍스트 = 그 뒤"])
box("c12-t1", 832, 628, 241, 52, "r", ["!여러 메시지로 분할 ✗", "~병렬 호출 감소 → 이후 latency 증가"])
box("c12-t2", 832, 688, 241, 48, "r", ["!요약 텍스트만 전송 ✗", "~결과 ↔ 호출 대응 파악 ✗"])
box("c12-dis", 832, 744, 241, 46, "g", ["!disable_parallel_tool_use", "~한 턴 1호출로 제한"])
arrow([(1176, 476), (1085, 476)], "여러 블록", 1131, 468)
arrow([(952, 504), (952, 544)], "모두 실행", 960, 529, "start", "b")
arrow([(850, 800), (850, 856)], "점검: 역할(user) · 순서(앞) · 메시지 수(하나)", 859, 831, "start", "b")

# ───────────────────────── 오른쪽 열 곁 함정 ─────────────────────────
box("t-direct", 1103, 596, 158, 78, "r", ["!모델이 직접", "!API 호출 ✗", "~client tool = 앱 실행", "~권한 검사 우회"])
box("t-first", 1103, 716, 158, 78, "r", ["!첫 tool_use만", "!유효 ✗", "~모두 실행", "~→ 결과 전부 반환"])
box("loopnote", 880, 344, 270, 48, "g", ["!loop 제어", "~tool_use인 동안 요청 반복 · 그 외 종료"])

# ───────────────────────── 왼쪽 열 함정 (⑧ 옆) ─────────────────────────
box("t-summary", 94, 626, 230, 56, "r", ["!요약 후 새로 시작 ✗", "~tool_use / tool_result 짝 끊김"])
box("t-memory", 94, 702, 230, 56, "r", ["!'모델이 tool을 기억' ✗", "~stateless → assistant 턴 재전송"])
box("t-stop", 94, 778, 230, 56, "r", ["!stop_reason = tool_result ✗", "~tool_result = 블록 유형"])

# ───────────────────────── 1-1 왕복 (messages 배열) ─────────────────────────
frame("c11", 24, 980, 606, 270, "1-1 tool_use ↔ tool_result 왕복 — messages 배열")
box("c11-m1", 36, 1018, 158, 70, "g", ["!user 메시지", "~원래 요청"])
box("c11-m2", 248, 1018, 158, 70, "b", ["!assistant 턴", "tool_use (id = A)", "~그대로 첨부"])
box("c11-m3", 460, 1018, 158, 70, "b", ["!user 메시지", "tool_result", "~tool_use_id = A"])
arrow([(194, 1053), (248, 1053)], "이어서", 221, 1045)
arrow([(406, 1053), (460, 1053)], "바로 다음", 433, 1045, color="b")
box("c11-t1", 36, 1104, 285, 60, "r", ["!system · assistant 메시지로 전송 ✗", "~전용 SDK 메서드(submit_result()) ✗"])
box("c11-t2", 333, 1104, 285, 60, "r", ["!사이에 확인 메시지 삽입 ✗", "~배열 규칙 위반"])
box("c11-t3", 36, 1176, 285, 62, "r", ["!prefill 요약으로 전송 ✗", "~tool_result 인식 ✗ · Claude 4.6 이상 = 400"])
box("c11-t4", 333, 1176, 285, 62, "r", ["!assistant 턴 · id 누락 → 에러", "~graceful recovery ✗"])
arrow([(600, 980), (600, 944)], "배열 규칙", 592, 969, "end", "b")

# ───────────────────────── 1-3 에러 처리 ─────────────────────────
frame("c13", 670, 980, 706, 270, "1-3 Tool 에러 처리")
box("c13-ret", 682, 1016, 250, 64, "b",
    ["!is_error: true + 구조화 반환", "~분류 · 재시도 가능 여부", "~사람용 설명 · 시정 힌트"])
diamond("c13-q", 1050, 1048, 170, 64, ["!에러 종류?"])
box("c13-empty", 1150, 1016, 214, 64, "g",
    ["!빈 tool_result", "~실제 결과 없음(0건)일 때만", "~0건 = 성공 · timeout = 에러"])
arrow([(965, 1048), (932, 1048)], "반환", 949, 1040, color="b")
TYPES = [
    ("c13-y1", "g", ["!일시적", "~timeout · 429 · 서비스 불가", "~→ 대기 후 재시도(상한)"], "재시도 ✓"),
    ("c13-y2", "g", ["!검증", "~없는 ID · 형식 불량", "~→ 입력 수정 후 재호출"], "수정"),
    ("c13-y3", "g", ["!비즈니스", "~한도 초과 · 정책 차단", "~→ 사유 안내 · escalate"], "재시도 ✗"),
    ("c13-y4", "g", ["!권한", "~접근 거부 · 라이선스 만료", "~→ 다른 정보원 · 부족 보고"], "재시도 ✗"),
]
TRAPS13 = [
    ["!빈 결과로 위장 ✗", "~'데이터 없음'으로 오해"],
    ["!무한 재시도 ✗", "~raw 에러 노출 · 전체 중단 ✗"],
    ["!같은 에러 문구 ✗", "~원인 구별 ✗ → 재시도 오판"],
    ["!JSON-RPC 에러로 ✗", "~업무 실패 이유 전달 ✗"],
]
BUS = 1094
out.append(f'<polyline points="1050,1080 1050,{BUS}" fill="none" stroke="{INK}" stroke-width="1.5"/>')
out.append(f'<polyline points="763.5,{BUS} 1282.5,{BUS}" fill="none" stroke="{INK}" stroke-width="1.5"/>')
for i, (name, kind, lines, lab) in enumerate(TYPES):
    x = 682 + i * 173
    box(name, x, 1114, 163, 60, kind, lines)
    arrow([(x + 81.5, BUS), (x + 81.5, 1114)], lab, x + 89, 1108, "start", "b" if i < 2 else "r")
    box(f"c13-t{i + 1}", x, 1186, 163, 52, "r", TRAPS13[i])

# ───────────────────────── 1-9 client vs server (아래 띠) ─────────────────────────
frame("c19", 24, 1270, 1352, 206, "1-9 Client tools vs Server tools — 구분 기준 = 코드가 실행되는 위치")
diamond("c19-q", 650, 1330, 190, 60, ["!코드 실행", "!위치?"])
box("c19-client", 196, 1392, 240, 78, "b",
    ["!Client tools", "tool_use 수신 → 앱 실행", "~→ tool_result 반환 (위 loop)"])             # port 아래 (316,1500)
box("c19-server", 1188, 1392, 176, 78, "g",
    ["!Server tools", "~같은 응답에 결과 포함", "~앱 실행 ✗ · tool_result ✗"])                  # port 아래 (1276,1500)
arrow([(650, 944), (650, 1300)], "tool_result 필요?", 659, 969, "start")
arrow([(555, 1330), (316, 1330), (316, 1392)], "앱", 436, 1322, color="b")
arrow([(745, 1330), (CX, 1330), (CX, 1392)], "Anthropic 인프라", 1010, 1322)
box("c19-t0", 36, 1392, 148, 72, "r", ["!client tool을", "!Anthropic 실행 ✗", "~실행 위치 혼동"])
box("c19-n1", 448, 1368, 234, 46, "g", ["!직접 정의 · bash · text_editor", "~사내 시스템(SIEM 등) = client tool"])
box("c19-n2", 694, 1368, 236, 46, "g", ["!Batches API + client tool", "~custom_id로 특정 → 앱 실행 → 후속 요청"])
box("c19-n3", 942, 1368, 234, 46, "g", ["!web_search · web_fetch", "~code_execution · tool_search 등"])
box("c19-t1", 448, 1420, 234, 44, "r", ["!사내 시스템을 server tool로 ✗", "~사용자 정의 ✗ · 사내망 도달 ✗"])
box("c19-t2", 694, 1420, 236, 44, "r", ["!Batches: web_search로 대체 ✗", "~tool_choice 강제 · 예측 tool_result ✗"])
box("c19-t3", 942, 1420, 234, 44, "r", ["!server tool = MCP 전용 ✗", "~Batch 전용도 ✗ · 일반 요청 tools에 선언"])


# ───────────────────────── 검사 ─────────────────────────
def hit(a, b, pad=0):
    return a[1] < b[3] + pad and b[1] < a[3] + pad and a[2] < b[4] + pad and b[2] < a[4] + pad


PORTS = {"req", "exec", "c19-client", "c19-server"}
for i, a in enumerate(leaf):
    for b in leaf[i + 1:]:
        if hit(a, b, 4):
            warns.append(f"box overlap: {a[0]} / {b[0]}")
    if a[0] not in PORTS and (a[1] < 24 or a[2] < 24 or a[3] > W - 24 or a[4] > H - 24):
        warns.append(f"margin: {a[0]}")
    if a[1] < 600 and a[2] < 70:
        warns.append(f"title area: {a[0]}")
    for f in frames:
        if hit(a, f) and not (f[1] + 8 <= a[1] and a[3] <= f[3] - 8 and f[2] + 8 <= a[2] and a[4] <= f[4] - 4):
            warns.append(f"box {a[0]} straddles frame {f[0]}")
for i, a in enumerate(labels):
    for b in labels[i + 1:]:
        if hit(a, b):
            warns.append(f"label overlap: {a[0]} / {b[0]}")
    for b in leaf:
        if hit(a, b, 1):
            warns.append(f"label '{a[0]}' on box {b[0]}")
    if a[1] < 24 or a[3] > W - 24:
        warns.append(f"label margin: {a[0]}")
    for lab, p, q in segs:
        s = ("seg", min(p[0], q[0]) - 2, min(p[1], q[1]) - 2, max(p[0], q[0]) + 2, max(p[1], q[1]) + 2)
        if hit(a, s):
            warns.append(f"label '{a[0]}' on arrow '{lab}'")
for lab, p, q in segs:
    s = ("seg", min(p[0], q[0]), min(p[1], q[1]), max(p[0], q[0]), max(p[1], q[1]))
    for b in leaf:
        inner = (b[0], b[1] + 2, b[2] + 2, b[3] - 2, b[4] - 2)
        if hit(s, inner):
            warns.append(f"arrow '{lab}' crosses box {b[0]}")

defs = "".join(
    f'<marker id="arr-{Z}{"" if k == "n" else "-" + k}" markerUnits="userSpaceOnUse" markerWidth="12" '
    f'markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L12,5 L0,10 z" fill="{c}"/></marker>'
    for k, c in ARROW.items())
title = "Tool 호출 루프: 요청 조립부터 tool_use, 앱 실행, tool_result 반환, 다음 요청까지의 왕복"
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
       f'aria-label="{title}" font-family="{FONT}">\n<title>{title}</title>\n'
       f'<rect width="100%" height="100%" fill="#FFFFFF"/>\n<defs>{defs}</defs>\n'
       # frame을 먼저 그려 화살표 · 상자가 그 위에 오게 한다
       + "\n".join(sorted(out, key=lambda e: 0 if 'stroke-width="1"/>' in e else 1)) + "\n</svg>\n")
dst = Path(__file__).resolve().parent / "zone-a.svg"
dst.write_text(svg, encoding="utf-8")
print(dst, f"{len(leaf)} boxes, {len(segs)} segments")
print("\n".join("WARN " + w for w in warns) or "checks OK")
