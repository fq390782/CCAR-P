"""8장 통합 개념 지도 zone c (통제 · 권한) SVG 생성. 실행: python3 -I work/poster8/gen_c.py"""
from pathlib import Path
from xml.sax.saxutils import escape

W, H = 1400, 1500
INK, SUB = "#1F2937", "#6B7280"
KIND = {  # fill, stroke
    "gen": ("#F3F4F6", "#9CA3AF"), "ok": ("#DBEAFE", "#2563EB"), "bad": ("#FEE2E2", "#DC2626"),
    "ask": ("#FEF3C7", "#D97706"), "end": ("#DCFCE7", "#16A34A"), "frame": ("#FFFFFF", "#9CA3AF"),
}
COL = {"ink": INK, "blue": "#2563EB", "red": "#DC2626", "green": "#16A34A"}
out, warn = [], []


def tw(s, size):
    """글자 폭 추정(한글 = size, 영문·숫자 ≈ 0.58 size)."""
    n = 0.0
    for ch in s:
        if ch == " ":
            n += 0.3
        elif ch in "·":
            n += 0.4
        elif ord(ch) < 128:
            n += 0.58
        else:
            n += 1.0
    return n * size


def parse(line):
    """'b|' = 13px bold, 's|' = 11px, 그 밖 = 13px."""
    if line.startswith("b|"):
        return line[2:], 13, True
    if line.startswith("s|"):
        return line[2:], 11, False
    return line, 13, False


def text(x, y, s, size=11, bold=False, anchor="start", fill=INK):
    b = ' font-weight="bold"' if bold else ""
    out.append(f'<text x="{x}" y="{y}" font-size="{size}"{b} text-anchor="{anchor}" fill="{fill}">{escape(s)}</text>')


def lines_in(cx, cy, lines, maxw, maxh, tag):
    parsed = [parse(l) for l in lines]
    lh = [17 if sz == 13 else 15 for _, sz, _ in parsed]
    if sum(lh) > maxh:
        warn.append(f"높이 넘침: {tag} {lines[0]}")
    top = cy - sum(lh) / 2
    for (s, sz, b), h in zip(parsed, lh):
        if tw(s, sz) * (1.05 if b else 1) > maxw:
            warn.append(f"폭 넘침({tw(s, sz):.0f}>{maxw:.0f}): {s}")
        text(cx, round(top + h * 0.76, 1), s, sz, b, "middle")
        top += h


def box(x, y, w, h, kind, lines):
    f, s = KIND[kind]
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{f}" stroke="{s}" stroke-width="1.5"/>')
    lines_in(x + w / 2, y + h / 2, lines, w - 16, h - 10, "box")


def diamond(cx, cy, hw, hh, lines):
    f, s = KIND["ask"]
    out.append(f'<polygon points="{cx},{cy-hh} {cx+hw},{cy} {cx},{cy+hh} {cx-hw},{cy}" fill="{f}" stroke="{s}" stroke-width="1.5"/>')
    lines_in(cx, cy, lines, hw * 1.25, hh * 1.0, "diamond")


def arrow(pts, color="ink", width=1.5):
    mid = "arr-8map-c" + ("-bb" if width > 2 else "" if color == "ink" else "-" + color)
    p = " ".join(f"{x},{y}" for x, y in pts)
    out.append(f'<polyline points="{p}" fill="none" stroke="{COL[color]}" stroke-width="{width}" marker-end="url(#{mid})"/>')


def link(x1, y1, x2, y2):
    out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="1.5"/>')


def frame(x, y, w, h, title):
    f, s = KIND["frame"]
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{f}" stroke="{s}" stroke-width="1.5"/>')
    if tw(title, 16) * 1.05 > w - 32:
        warn.append(f"제목 넘침: {title}")
    text(x + 16, y + 28, title, 16, True)


def marker(mid, color, size):
    return (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="{size}" markerHeight="{size}" '
            f'markerUnits="userSpaceOnUse" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{color}"/></marker>')


# ---------- 원칙 (우상단 띠) ----------
text(726, 46, "원칙: 예외 없는 통제는 prompt 지시가 아니라 코드와 tool 범위로 강제", 14, True)
text(726, 64, "가운데 굵은 띠가 주 흐름 (오른쪽 → 왼쪽) · 위아래 묶음이 각 단계의 상세", 11, fill=SUB)

# ---------- backbone (y 860~940) ----------
box(1110, 860, 240, 80, "ok", ["b|누구에게 줄지", "s|역할별 tool 범위 [1-17]"])
box(760, 860, 240, 80, "ok", ["b|무엇을 남길지", "s|최소 권한 tool surface [1-18]"])
box(400, 860, 240, 80, "ok", ["b|언제 줄지", "s|state machine + tool gating [1-8]"])
box(12, 860, 280, 80, "ok", ["b|실행 직전 도구 경계에서 검사", "s|코드 게이트 [1-21] → 통과 시 앱이 tool 실행"])
for x1, x2, lab in ((1110, 1000, "역할 tool set"), (760, 640, "남은 tool만"), (400, 292, "허용된 호출")):
    arrow([(x1, 900), (x2, 900)], "blue", 2.5)
    text((x1 + x2) / 2, 890, lab, 11, anchor="middle")
link(1230, 860, 1230, 836)
link(880, 940, 880, 964)
link(520, 860, 520, 836)
link(152, 940, 152, 964)

# ---------- 1-8 (좌상) ----------
frame(24, 80, 666, 756, "1-8 워크플로 순서를 코드로 강제 (state machine + tool gating)")
text(40, 136, "필수 순서 예 · 전환 기준 = 코드로 검증 가능한 사실 (예: 본인 확인 tool 성공)", 11, fill=SUB)
for i, name in enumerate(["본인 확인", "정보 수집", "확인 · 동의", "실행"]):
    x = 40 + i * 170
    box(x, 150, 105, 40, "gen", [name])
    if i < 3:
        arrow([(x + 105, 170), (x + 170, 170)])
        text(x + 136, 163, "코드 검증", 11, anchor="middle")
arrow([(262, 190), (262, 244)])
text(270, 222, "현재 단계", 11)
box(112, 244, 300, 44, "gen", ["b|앱이 현재 단계를 상태로 보유"])
box(440, 238, 234, 56, "gen", ["s|역할 분담", "s|대화 유연성 = Claude", "s|깨지면 안 되는 순서 = 코드"])
arrow([(262, 288), (262, 340)])
text(270, 318, "tools 구성", 11)
diamond(262, 390, 130, 50, ["tool 정의를 단계마다", "바꿔도 되나?"])
arrow([(132, 390), (90, 390), (90, 490)], "blue")
text(111, 382, "예", 11, anchor="middle")
arrow([(392, 390), (522, 390), (522, 490)], "blue")
text(400, 382, "아니오: 정의 변경 → prompt cache 전체 무효화", 11)
box(40, 490, 290, 56, "ok", ["b|상태별 허용 tool만 tools에 포함"])
box(370, 490, 304, 56, "ok", ["b|tool 정의 고정", "s|상태에 안 맞는 호출을 앱이 거부 · 에러 반환"])
arrow([(185, 546), (185, 610)], "green")
text(193, 582, "효과", 11)
arrow([(522, 546), (522, 610)], "green")
text(530, 582, "절차를 건너뛴 호출", 11)
box(40, 610, 290, 56, "end", ["본인 확인 전 요청엔", "변경 tool 부재 → 호출 불가"])
box(370, 610, 304, 56, "end", ["거부: is_error: true", "+ 이유 + 다음 절차"])
box(40, 716, 634, 84, "bad", [
    "b|✗ prompt 쪽 수단으로 필수 순서 강제",
    "s|system 프롬프트 · 번호 목록 · few-shot · effort 상향 · \"다음 단계 이름 JSON 출력\"",
    "s|→ 최종 판단이 모델에 남음 = 확률적 · 보장 ✗",
])

# ---------- 1-17 (우상) ----------
frame(710, 80, 666, 756, "1-17 역할별 tool 범위 (subagent tool 제한)")
box(726, 128, 290, 68, "bad", [
    "b|✗ 모든 subagent가 같은 18개 tool 공유",
    "s|판단 복잡도 증가 → tool 선택 신뢰성 저하",
    "s|전문 밖 tool 오용 (문서 분석 agent의 웹 검색)",
])
arrow([(1016, 162), (1090, 162)], "blue")
text(1053, 154, "역할별 제한", 11, anchor="middle")
box(1090, 128, 270, 68, "ok", [
    "b|역할에 필요한 tool만 부여",
    "s|가이드 예시: 역할당 4~5개",
    "s|Agent SDK: AgentDefinition의 tools",
])
text(726, 216, "⚠️ 4~5개 = 가이드 예시 수치 · 공식 문서: 30~50개 초과 시 tool 선택 정확도 저하", 11, fill=SUB)
box(726, 232, 634, 50, "gen", [
    "b|coordinator",
    "s|쓰기(티켓 등록 · DB 쓰기 · CRM 갱신) · 역할 밖 추가 조사 routing 담당",
])
arrow([(825, 346), (825, 282)])
text(833, 310, "합쳐진 결과", 11)
text(833, 325, "→ 티켓 등록은 coordinator만", 11)
arrow([(1043, 282), (1043, 346)])
text(1051, 310, "초점 좁힌", 11)
text(1051, 325, "위임", 11)
arrow([(1261, 346), (1261, 282)])
text(1269, 310, "추가 조사 이유", 11)
text(1269, 325, "(구조화해 반환)", 11)
box(726, 346, 198, 76, "ok", ["b|저장소 scanner", "s|Read · Grep · Glob · 의존성 검사", "s|읽기 전용"])
box(944, 346, 198, 76, "ok", ["b|추출 subagent", "s|문서 읽기 + 추출 결과 제출만", "s|웹 검색 · 검증 전 DB 쓰기 ✗", "s|CRM · 메일 · 캘린더 = 별도 agent"])
box(1162, 346, 198, 76, "ok", ["b|전문 agent", "s|읽기 + 구조화 결과 반환까지", "s|쓰기 = coordinator · 별도 단계"])
text(726, 442, "운영 확인: tool 호출 로그 정기 점검 → 역할 밖 호출 모니터링", 11, fill=SUB)
diamond(830, 548, 95, 58, ["타 역할 기능", "필요 빈도?"])
arrow([(830, 490), (830, 478), (1040, 478)], "blue")
text(846, 470, "낮음(약 10%) · 미검증 출처 혼입", 11)
arrow([(925, 548), (1040, 548)], "blue")
text(930, 540, "빈번 · 단순 확인(85%)", 11)
arrow([(830, 606), (830, 618), (1040, 618)], "blue")
text(846, 610, "역할 안 조회 빈번(예: 60%)", 11)
box(1040, 449, 320, 58, "ok", ["b|tool 제거 + coordinator 경유 routing", "s|추가 조사 이유를 구조화해 반환"])
box(1040, 519, 320, 58, "ok", ["b|범위 제한 tool(verify_fact) 부여", "s|복잡 · 깊은 조사(15%)는 coordinator 경로 유지"])
box(1040, 589, 320, 58, "ok", ["b|조회 한정 tool(lookup_job_code) 추가", "s|읽기 전용 · tool 전부 박탈 ✗ (coordinator 왕복 증가)"])
box(726, 664, 250, 56, "gen", ["b|범용 fetch_url", "s|역할 밖 기능(검색)까지 허용"])
arrow([(976, 692), (1040, 692)], "blue")
text(1008, 684, "교체", 11, anchor="middle")
box(1040, 664, 320, 56, "ok", ["b|용도 한정 load_document", "s|interface 단계에서 기능 제한"])
box(726, 736, 309, 84, "bad", [
    "b|✗ 타 역할 tool 전체 부여",
    "s|(synthesis에 web-search 전부)",
    "s|→ 역할 확대 · 미검증 출처 혼입 유지",
    "s|✗ 출처 신뢰도 표기만 추가 → 혼입 못 막음",
])
box(1051, 736, 309, 84, "bad", [
    "b|✗ 역할 밖 오용을 prompt 금지로 처리",
    "s|→ 확률적 · tool 접근 그대로",
    "s|✗ fetch_url에 검색 엔진 도메인 차단 필터",
    "s|정답 = 배분 재검토 (혼동이면 description 개선)",
])

# ---------- 1-21 (좌하) ----------
frame(24, 964, 496, 512, "1-21 도구 경계에서 강제하는 통제 (정책 한도 · 파괴적 작업)")
box(40, 1008, 200, 68, "gen", ["b|tool 호출 요청", "s|정책 한도(직접 환불 상한)", "s|되돌릴 수 없는 작업 · 삭제"])
box(296, 1008, 208, 68, "bad", ["b|✗ prompt 문구 · 경고", "s|description · 모델의 판단", "s|= 요청일 뿐 · 확률적 · 보장 ✗"])
arrow([(140, 1076), (140, 1104)])
text(148, 1094, "실행 전 코드 판정", 11)
diamond(140, 1156, 100, 52, ["권한 · 범위 · 한도", "절차 통과?"])
arrow([(240, 1156), (296, 1156)], "blue")
text(268, 1148, "아니오", 11, anchor="middle")
box(296, 1114, 208, 84, "ok", ["b|거부 (결정적)", "s|한도 초과 → 사람이 처리", "s|is_error: true", "s|+ 이유 + 다음 절차"])
arrow([(140, 1208), (140, 1240)], "green")
text(148, 1228, "예", 11)
box(40, 1240, 200, 36, "end", ["b|통과 → 앱이 tool 실행"])
text(296, 1244, "강제 주체 = 모델을 둘러싼 시스템", 11, fill=SUB)
text(296, 1260, "(도구 계층 · 앱의 게이트)", 11, fill=SUB)
text(40, 1304, "skill 실행 중 편집 · 셸 금지 → 프런트매터 선택", 13, True)
box(40, 1314, 224, 84, "bad", ["b|✗ allowed-tools", "s|호출 turn 동안 확인 없이 사용", "s|= 사전 승인", "s|사용 가능 도구 제한 ✗"])
box(280, 1314, 224, 84, "ok", ["b|disallowed-tools", "s|skill 활성 동안", "s|도구 풀에서 제외 ✓", "s|전체 적용 = permissions의 deny"])
box(40, 1410, 464, 50, "bad", [
    "s|✗ 직원 교육 · parameter 추가 · 선언 순서 변경 · CLAUDE.md · slash command 요청",
    "s|→ agent 제약 ✗ · 권한 제약 ✗ · 모델 guidance일 뿐 (강제력 ✗)",
])

# ---------- 1-18 (우하) ----------
frame(540, 964, 836, 512, "1-18 최소 권한 tool surface (불필요 기능 제거)")
diamond(696, 1072, 115, 48, ["현재 작업이", "이 tool을 쓰나?"])
arrow([(811, 1072), (865, 1072)])
text(838, 1064, "예", 11, anchor="middle")
diamond(980, 1072, 115, 48, ["필요 이상을", "허용 · 반환하나?"])
arrow([(1095, 1072), (1160, 1072)], "green")
text(1127, 1064, "아니오", 11, anchor="middle")
box(1160, 1030, 200, 84, "end", ["b|유지", "s|매일 쓰는 정당한 tool"])
arrow([(696, 1120), (696, 1230)], "blue")
text(706, 1160, "아니오 · 판정 전 장기 trace(예: 6개월)로", 11)
text(706, 1176, "숨은 호출자 · workflow 확인", 11)
box(556, 1230, 384, 84, "ok", [
    "b|제거 = 공격 · 오류 표면 자체를 없앰",
    "s|어떤 작업도 안 쓰는 위험 tool",
    "s|drop_table · delete_* · wire_transfer · mass_email",
    "s|\"나중에 유용할지도\" → 지금 제거 · 필요해지면 검토 후 재추가",
])
arrow([(980, 1120), (980, 1186), (1090, 1186)], "blue")
arrow([(980, 1186), (980, 1278), (1090, 1278)], "blue")
text(988, 1142, "예", 11)
text(990, 1178, "범용 tool", 11)
text(990, 1270, "과다 데이터 반환", 11)
box(1090, 1144, 270, 84, "ok", [
    "b|범위 제한 tool로 교체",
    "s|run_sql · raw SQL → get_account_summary",
    "s|검증된 고객 ID만 받아 그 범위만 반환",
    "s|내부에서 전달 ID = 본인 확인 결과인지 검사",
])
box(1090, 1244, 270, 68, "ok", [
    "b|반환 필드를 작업 필요분으로 축소",
    "s|전체 SSN · 결제 정보 포함 프로필 반환 ✗",
    "s|다른 작업이 필요하면 tool 분리",
])
box(730, 1340, 307, 84, "bad", [
    "b|✗ 위험 tool 유지 + 로깅 · 모니터링",
    "s|→ 가시성 ≠ 통제 · 권한 활성 (로그는 유지)",
    "s|✗ 문서화 · 이름 변경 · 숨김 → 기능 접근 그대로",
    "s|✗ 더 긴 system prompt · 자가 재확인 → 확률적",
])
box(1053, 1340, 307, 104, "bad", [
    "b|✗ 낮은 오류율(예: 0.4%)을 면제 사유로",
    "s|→ 범용 tool이 남는 한 타 고객 데이터 도달 가능",
    "s|✗ 범용 query tool 하나로 DB 전체 노출",
    "s|→ model 권한 무제한 · least privilege 적용 불가",
    "s|✗ 하루 1회 사용만으로 스키마 4,000 토큰 유지 정당화",
    "s|→ 호출마다 스키마 토큰 계산 · 스키마 축소 대상",
])
# port (아래 변 696,1500)
arrow([(696, 1434), (696, 1314)], "blue")
text(686, 1364, "이 용도에 불필요한", 11, anchor="end")
text(686, 1380, "쓰기 작업 노출", 11, anchor="end")
text(686, 1396, "→ 제거", 11, anchor="end")
box(556, 1434, 280, 56, "ok", ["b|MCP tool도 같은 기준", "s|불필요한 쓰기 작업 노출 여부 점검"])

head = (
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
    'aria-label="8장 개념 지도 zone 3: prompt 지시가 아니라 코드와 tool 범위로 통제와 권한을 강제하는 흐름" '
    'font-family="Apple SD Gothic Neo, Noto Sans KR, Malgun Gothic, sans-serif">\n'
    "<title>③ 통제 · 권한: 역할별 tool 범위 → 최소 권한 → tool gating → 도구 경계 게이트</title>\n"
    '<rect width="100%" height="100%" fill="#FFFFFF"/>\n<defs>'
    + marker("arr-8map-c", INK, 9) + marker("arr-8map-c-bb", COL["blue"], 13)
    + "".join(marker(f"arr-8map-c-{c}", COL[c], 9) for c in ("blue", "red", "green"))
    + "</defs>\n"
)
dst = Path(__file__).with_name("zone-c.svg")
dst.write_text(head + "\n".join(out) + "\n</svg>\n", encoding="utf-8")
print(dst, "| 경고", len(warn))
print("\n".join(warn))
