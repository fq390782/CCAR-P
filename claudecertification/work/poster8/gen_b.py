"""8장 통합 개념 지도 zone b (② Tool 정의 설계) SVG 생성. 표준 라이브러리만 쓴다.

사용: python3 -I work/poster8/gen_b.py  → work/poster8/zone-b.svg
글자 폭을 추정해 상자를 넘치면 WARN을 찍는다.
"""
from pathlib import Path
from xml.sax.saxutils import escape

W, H = 1400, 1500
FONT = "Apple SD Gothic Neo, Noto Sans KR, Malgun Gothic, sans-serif"
COL = {"gray": ("#F3F4F6", "#9CA3AF"), "blue": ("#DBEAFE", "#2563EB"), "red": ("#FEE2E2", "#DC2626"),
       "dia": ("#FEF3C7", "#D97706"), "green": ("#DCFCE7", "#16A34A")}
INK, SUB = "#1F2937", "#6B7280"
out, warns, nid = [], [], [0]


def tw(s, size):
    w = 0.0
    for ch in s:
        if ch == " ":
            w += 0.3
        elif ord(ch) >= 0x1100 or ch in "→✗✓≈≠":
            w += 1.0
        elif ch.isupper():
            w += 0.68
        else:
            w += 0.56
    return w * size


def parse(line):
    if line.startswith("!"):
        return line[1:], 13, True
    if line.startswith("~"):
        return line[1:], 11, False
    return line, 13, False


def text(x, y, s, size=13, bold=False, anchor="middle", fill=INK):
    b = ' font-weight="bold"' if bold else ""
    out.append(f'<text x="{x:g}" y="{y:g}" font-size="{size}" text-anchor="{anchor}" fill="{fill}"{b}>{escape(s)}</text>')


def lines_at(cx, y, h, lines, limit, tag):
    ps = [parse(l) for l in lines]
    lhs = [16 if p[1] == 13 else 14 for p in ps]
    cur = y + (h - sum(lhs)) / 2
    if sum(lhs) > h - 6:
        warns.append(f"HEIGHT {tag}: {lines[0]}")
    for (s, size, bold), lh in zip(ps, lhs):
        if tw(s, size) > limit:
            warns.append(f"WIDTH {tag}: {s!r} {tw(s, size):.0f} > {limit:.0f}")
        text(cx, cur + lh * 0.76, s, size, bold)
        cur += lh


def box(x, y, w, h, kind, lines, bid=None):
    f, s = COL[kind]
    nid[0] += 1
    i = bid or f"8map-b-n{nid[0]}"
    out.append(f'<rect id="{i}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="6" fill="{f}" stroke="{s}" stroke-width="1.5"/>')
    lines_at(x + w / 2, y, h, lines, w - 10, "box")


def dia(cx, cy, w, h, lines):
    f, s = COL["dia"]
    nid[0] += 1
    pts = f"{cx:g},{cy - h / 2:g} {cx + w / 2:g},{cy:g} {cx:g},{cy + h / 2:g} {cx - w / 2:g},{cy:g}"
    out.append(f'<polygon id="8map-b-n{nid[0]}" points="{pts}" fill="{f}" stroke="{s}" stroke-width="1.5"/>')
    lines_at(cx, cy - h / 2, h, lines, w * (1 - 26 / h), "dia")


def arrow(pts, label=None, color="ink", sw=1.5):
    c = {"ink": INK, "blue": "#2563EB", "red": "#DC2626"}[color]
    m = {"ink": "arr-8map-b", "blue": "arr-8map-b-blue", "red": "arr-8map-b-red"}[color]
    d = "M" + " L".join(f"{x:g},{y:g}" for x, y in pts)
    out.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{sw}" marker-end="url(#{m})"/>')
    if not label:
        warns.append(f"NOLABEL {pts}")
        return
    s, x, y, *a = label
    for k, part in enumerate(s.split("|")):
        text(x, y + 13 * k, part, 11, False, a[0] if a else "middle", SUB)


def frame(key, x, y, w, h, step, title, sub):
    out.append(f'<g id="8map-b-{key}" transform="translate({x},{y})">')
    out.append(f'<rect width="{w}" height="{h}" rx="6" fill="#FFFFFF" stroke="#9CA3AF" stroke-width="1.5"/>')
    out.append(f'<rect width="{w}" height="32" rx="6" fill="#DBEAFE" stroke="#2563EB" stroke-width="1.5"/>')
    text(14, 21, step, 14, True, "start")
    text(14, 56, title, 16, True, "start")
    text(w - 14, 56, sub, 11, False, "end", SUB)
    if tw(title, 16) + tw(sub, 11) > w - 40:
        warns.append(f"TITLE {title}")
    out.append('<g transform="translate(6,0)">')


def end():
    out.append("</g></g>")


FW = 652
LX, RX = 24, 724

# ---------- ①-a  1-16 ----------
frame("c16", LX, 80, FW, 320, "①-a 어떤 tool을 둘지: custom tool의 입자도", "1-16 범용 tool 분할 vs 통합",
      "입출력이 다르면 분할 · 같은 일이면 병합")
box(14, 88, 140, 68, "gray", ["!범용 tool 하나", "analyze_document", "~출력 형식이 매번 다름"])
dia(268, 122, 164, 80, ["목적 · 입출력이", "서로 다른가?"])
arrow([(154, 122), (186, 122)], ("판단", 169, 116))
box(404, 84, 222, 76, "blue", ["!목적별 tool로 분할", "~extract_data_points", "~summarize_content", "~verify_claim_against_source"])
arrow([(350, 122), (404, 122)], ("예", 376, 116), "blue")
arrow([(268, 162), (268, 196)], ("아니오 = 같은 일 · 같은 입력", 276, 183, "start"), "blue")
box(156, 196, 224, 44, "blue", ["action 파라미터 + 명확한 설명의", "!tool 하나로 병합"])
box(156, 250, 224, 56, "red", ["~40개 동작을 mode 하나로 ✗", "~18개 tool을 action 하나로 ✗", "~→ 동작이 선택 단계에서 숨음"])
arrow([(515, 160), (515, 196)], ("받침 장치", 523, 182, "start"), "blue")
box(404, 196, 222, 60, "blue", ["!입출력을 JSON schema로 고정", "~필수 입력 = input_schema 필수 파라미터", "~단계별로 필요한 tool만 노출"])
box(404, 266, 222, 40, "red", ["~namespace만 정리 ✗", "~→ 노출 범위를 못 좁힘"])
box(14, 166, 134, 68, "red", ["~범용 tool 유지 +", "~system prompt 지시 ✗", "~→ 필수 조건을", "~schema로 표현 불가"])
box(14, 244, 134, 62, "gray", ["~한 호출에 여러 목적", "~+ 전체 tool 노출", "~→ 단계를 역할별 분리"])
end()

# ---------- ①-b  1-20 ----------
frame("c20", LX, 444, FW, 440, "①-b 어떤 tool을 둘지: 내장 도구 선택", "1-20 내장 도구 선택",
      "이름은 Glob · 내용은 Grep · 일부는 Edit · 전체는 Write")
dia(104, 116, 180, 76, ["찾는 정보가", "이름? 내용?"])
box(232, 94, 150, 44, "blue", ["!Glob", "~이름 규칙 **/*.test.tsx"])
arrow([(194, 116), (232, 116)], ("이름", 213, 110), "blue")
box(404, 88, 222, 56, "red", ["~Glob · find로 내용 정보 추정 ✗", "~→ 이름만으론 불확실 · 누락"])
arrow([(104, 154), (104, 186)], ("내용", 112, 174, "start"), "blue")
box(14, 186, 180, 44, "blue", ["!Grep", "~호출처 · 에러 메시지 · 진입점"])
box(232, 186, 150, 44, "blue", ["!Read", "~일치 파일만 · import 추적"])
arrow([(194, 208), (232, 208)], ("일치", 213, 202), "blue")
box(404, 180, 222, 56, "red", ["~흔한 단어 Grep · 파일 통독 ✗", "~→ 무관한 일치 대량 · context 소진", "~별칭 추적: 대소문자 무시 · 테스트 ✗"])
arrow([(104, 230), (104, 252)], ("찾은 곳을 변경", 112, 245, "start"))
dia(104, 290, 164, 76, ["바꾸는 범위가", "일부? 전체?"])
dia(322, 290, 176, 76, ["old_string이", "여러 번 일치?"])
arrow([(186, 290), (234, 290)], ("일부=Edit", 210, 284), "blue")
box(426, 250, 200, 82, "red", ["~old_string 단축 · 정규식 ✗", "~Grep으로 줄 지정 ✗", "~→ Edit 일치 방식 불변", "~한쪽만 변경에 replace_all ✗", "~Edit 수십 회 ✗ 중간 갱신 잔존"])
arrow([(104, 328), (104, 370)], ("전체", 112, 354, "start"), "blue")
box(14, 370, 136, 54, "blue", ["!Write 한 번", "~자동 생성 파일", "~전체 재생성"])
box(162, 370, 148, 54, "blue", ["!문맥 포함 Edit", "~앞뒤 문맥으로", "~한 곳으로 유일화"])
box(322, 370, 148, 54, "blue", ["!replace_all: true", "~모두 동일 변경", "~닫는 따옴표까지 포함"])
box(482, 370, 144, 54, "blue", ["!Read → Write 전체", "~한쪽만 변경 +", "~유일화 불가"])
arrow([(322, 328), (322, 344), (236, 344), (236, 370)], ("한 곳만", 230, 361, "end"), "blue")
arrow([(322, 328), (322, 344), (396, 344), (396, 370)], ("전부 동일", 402, 361, "start"), "blue")
arrow([(322, 328), (322, 344), (554, 344), (554, 370)], ("유일화 불가", 548, 361, "end"), "blue")
end()

# ---------- ②  1-6 ----------
frame("c6", LX, 928, FW, 490, "② description · tool surface 작성", "1-6 Tool description과 tool surface 설계",
      "정확도 = description · 겹침 = 설계로 해결")
box(264, 68, 176, 56, "red", ["~'신중히 고르라' 지시 ✗", "~context window 확장 · 정렬 ✗", "~→ 설계 문제 해결 ✗"])
box(452, 68, 174, 56, "red", ["~이름만 변경 ✗", "~description 1줄 통일 ✗", "~→ 정보량 불변 · 단서 소실"])
box(14, 76, 200, 34, "gray", ["!증상: tool 오선택"])
arrow([(114, 110), (114, 134)], ("먼저 구분", 122, 126, "start"))
dia(114, 170, 200, 72, ["틀린 것이", "선택인가 입력인가"])
box(264, 148, 362, 44, "blue", ["!입력 → 입력 형식 · input_examples · 필수 파라미터", "~올바른 tool에 잘못된 입력 = 선택이 아닌 입력 형식 문제"])
arrow([(214, 170), (264, 170)], ("입력", 239, 164), "blue")
arrow([(114, 206), (114, 230)], ("선택", 122, 222, "start"), "blue")
dia(114, 266, 200, 72, ["description이", "용도 · 경계 구분?"])
box(264, 206, 362, 92, "blue", ["!description 보강 (3~4문장 이상 · 명확함 > 간결함)", "~① 하는 일  ② 언제 쓰고 언제 쓰지 말지",
                               "~③ 파라미터 의미 · 영향  ④ 제약(반환하지 않는 정보)", "~이름 = 대상 · 범위 (search_own_archive_1990_2015)",
                               "~새 tool 추가 시 기존 유사 tool description도 수정"])
arrow([(214, 266), (264, 266)], ("아니오", 239, 260), "blue")
arrow([(114, 302), (114, 326)], ("예인데도 반복 오선택", 122, 318, "start"), "blue")
dia(114, 362, 200, 72, ["같은 일을 하는", "tool이 여럿?"])
box(264, 330, 220, 64, "blue", ["!하나만 남기고 통합", "~설명 하나 + 명확한 schema", "~다른 백엔드 · SLA = 진짜 중복 아님"])
arrow([(214, 362), (264, 362)], ("예", 239, 356), "blue")
box(496, 330, 130, 64, "red", ["~네 번째 tool 추가 ✗", "~'안전용' 중복 유지 ✗", "~tool_choice 강제 ✗", "~→ 겹침 악화 · 우회"])
arrow([(114, 398), (114, 430)], ("분리 요건 있음", 122, 418, "start"), "blue")
box(14, 430, 236, 46, "blue", ["!대상 드러낸 이름 + 사용 경계", "~분리 요건 = 출력 사양 · 감사 로그"])
box(264, 430, 362, 46, "blue", ["!MCP 서버 추가 후 성공률 하락 → 중복 · 구별성 먼저",
                               "~uptime · latency 의심 ✗ (에러 · 지연으로 드러남)"], "8map-b-mcpcheck")
arrow([(374, 430), (374, 394)], ("중복이면", 382, 416, "start"), "blue")
end()

# ---------- ⑤  1-19 ----------
frame("c19", RX, 24, FW, 526, "⑤ tool이 너무 많으면: 필요할 때만 로드", "1-19 Tool 과다 대응",
      "progressive discovery · tool search = 전부 노출하지 않고 필요할 때 로드")
box(14, 76, 176, 78, "gray", ["!tool 정의 과다", "~220개 ≈ 60,000 토큰 소비", "~비슷한 이름 혼동 증가", "~30~50개 초과 → 정확도 저하"])
dia(322, 115, 190, 78, ["약 20개 초과 +", "토큰이 제약?"])
arrow([(190, 115), (227, 115)], ("판정", 208, 109))
box(432, 84, 194, 62, "gray", ["~⚠️ 약 20개 = 해설 자체 기준", "~공식 문서: tool 10개 이상 ·", "~정의 10k 토큰 초과 시 권장"])
arrow([(322, 154), (322, 190)], ("예", 330, 176, "start"), "blue")
box(232, 190, 180, 60, "blue", ["!tool search tool", "~deferred 정의를 검색", "~자체엔 defer_loading ✗"])
box(14, 190, 176, 60, "blue", ["!자주 쓰는 3~5개", "~non-deferred 유지", "~→ 검색 왕복 없음"])
box(454, 190, 172, 60, "blue", ["!나머지 tool", "~defer_loading: true", "~발견될 때만 context에 전개"])
arrow([(232, 220), (190, 220)], ("defer|제외", 211, 201), "blue")
arrow([(412, 220), (454, 220)], ("검색", 433, 214), "blue")
arrow([(322, 250), (322, 274)], ("tools에 실음", 330, 266, "start"), "blue")
box(196, 274, 186, 44, "blue", ["모든 tool 계속 사용 가능", "~토큰 · 혼동 문제 대응"])
box(446, 274, 216, 44, "green", ["!tools 정의", "~name · description · input_schema"], "8map-b-port-out")
arrow([(382, 296), (446, 296)], ("산출물", 412, 289), "ink", 2.5)
box(14, 342, 186, 60, "gray", ["!다수 agent · MCP server", "~6 server 300개 · 8 시스템 45개", "~전부 선로드 → 비용 · 부정확"])
box(244, 342, 382, 60, "blue", ["!책임별 범위 지정 + progressive discovery", "~agent마다 필요한 server · tool 집합만 제공", "~이름 목록 먼저 → 전체 schema는 필요 시"])
arrow([(200, 372), (244, 372)], ("축소", 222, 366), "blue")
arrow([(540, 342), (540, 318)], ("노출 집합", 532, 334, "end"), "blue")
box(14, 416, 300, 56, "red", ["~모든 tool에 defer_loading (tool search 포함) ✗", "~→ 자주 쓰는 tool도 검색 왕복", "~deferred tool + cache_control → 400 오류"])
box(326, 416, 300, 56, "red", ["~description 단축 · cache_control ✗", "~tool_choice: any ✗ (호출 여부만 제어)", "~→ 점유 · 혼동 둘 다 해결 ✗"])
box(14, 482, 300, 30, "red", ["~더 큰 모델 · tool 절반 무작위 제거 ✗"])
box(326, 482, 300, 30, "gray", ["~트레이드오프: 조회 단계 추가 · 색인 부정확 시 못 찾음"])
end()

# ---------- ④  1-7 ----------
frame("c7", RX, 594, FW, 380, "④ tool 결과 크기 설계", "1-7 Tool 결과 크기 설계",
      "기준: agent가 결과만 읽고 다음 행동을 정할 수 있는가")
for cy, q, lab, b, r in [
    (120, ["큰 객체를 다음", "호출에만 쓰는가?"], None, ["!identifier(handle)만", "~→ context 절약"],
     ["~'항상 전체' · '항상 id만' ✗", "~→ 전체 vs identifier는", "~작업에 따라 결정"]),
    (204, ["큰 payload가", "context 대부분?"], "아니오 → 필요한 전체", ["!작업 관련 결과만", "~상세는 별도 요청으로"],
     ["~context window 확대 ✗", "~두 번째 모델 호출로 요약 ✗", "~→ payload 불변 · 비용 증가"]),
    (288, ["사용자 설명 값이", "UUID · 코드뿐?"], "아니오", ["!이름 · 상태 우선", "~ID도 필요 → response_format", "~concise(기본) · detailed(ID)"],
     ["~pagination · strict ✗", "~resolve_ids 추가 ✗", "~→ 왕복만 증가"]),
]:
    if lab:
        arrow([(124, cy - 54), (124, cy - 30)], (lab, 132, cy - 38, "start"))
    dia(124, cy, 220, 60, q)
    arrow([(234, cy), (264, cy)], ("예", 249, cy - 6), "blue")
    box(264, cy - 28, 182, 56, "blue", b)
    box(456, cy - 28, 170, 56, "red", r)
arrow([(124, 318), (124, 342)], ("검색 후보가 여럿(모호)", 132, 334, "start"))
box(14, 342, 432, 30, "blue", ["후보 전부 + 식별 정보(ID · 상태 · 등록일) + '작업 전 확인 요청'"])
box(456, 342, 170, 30, "red", ["~최신 · 유사도 자동 선택 ✗"])
end()

# ---------- ③  1-15 ----------
frame("c15", RX, 1018, FW, 400, "③ system prompt 지시가 선택을 왜곡하는지 점검", "1-15 system prompt 지시의 tool 선택 왜곡",
      "description이 명확해도 키워드 지시가 덮어씀")
dia(134, 122, 240, 76, ["description은 명확", "특정 단어에서만 오류?"])
box(290, 100, 170, 44, "blue", ["!system prompt 점검", "~tool 이름 · 키워드 지시"])
arrow([(254, 122), (290, 122)], ("예", 272, 116), "blue")
box(472, 88, 154, 68, "red", ["~description 보강 ✗", "~이름 변경 · few-shot ✗", "~tool_choice: any ✗ 악화", "~→ 원인 = prompt 지시"])
arrow([(134, 160), (134, 182)], ("아니오", 142, 175, "start"))
box(14, 182, 240, 26, "gray", ["~② description 구분성부터 점검"])
arrow([(375, 144), (375, 196), (280, 196), (280, 214)], ("원인별 조치", 383, 176, "start"), "blue")
rows = [
    (214, 28, ["단어 → tool 매핑 지시 (키워드 반응형)"], ["질문 대상에 따라 고르는 표현으로"]),
    (248, 34, ["'CRITICAL: You MUST' 강한 표현", "~+ 넓은 적용 범위 → 전용 tool 과호출"], ["평이한 표현 Use this tool when...", "~범위 축소 · prompt · description 양쪽 수정"]),
    (288, 34, ["'먼저 로그 검색' 일반 지시", "~→ 내장 Grep 편중 · MCP tool 억제"], ["지시의 대상 한정", "~+ MCP description 보강"]),
    (328, 34, ["'find · search면 반드시 검색 tool'", "~→ 호출 과다 (overtrigger)"], ["실제 조사가 필요할 때만으로 축소", "~description · tool_choice: auto 정상일 때"]),
]
for y, h, c, f in rows:
    box(14, y, 292, h, "gray", c)
    box(352, y, 274, h, "blue", f)
    arrow([(306, y + h / 2), (352, y + h / 2)], ("수정", 329, y + h / 2 - 5), "blue")
box(14, 368, 612, 24, "gray", ["~Opus 4.5 · 4.6 = prompt 반응성 높음 (이전 모델용 강한 표현 → 과호출) · tool 추가 시 충돌 표현 점검"])
end()

# ---------- backbone ----------
arrow([(350, 400), (350, 444)], ("custom tool을 정한 뒤 → 내장 도구", 360, 426, "start"), "ink", 2.5)
arrow([(350, 884), (350, 928)], ("둘 tool이 정해지면 → 설명 작성", 360, 910, "start"), "ink", 2.5)
arrow([(676, 1034), (724, 1034)], ("여전히|오선택", 700, 1002), "ink", 2.5)
arrow([(1050, 1018), (1050, 974)], ("선택이 맞으면 → 결과 설계", 1060, 1000, "start"), "ink", 2.5)
arrow([(1050, 594), (1050, 550)], ("tool이 너무 많으면", 1060, 576, "start"), "ink", 2.5)

# ---------- port (아래) ----------
box(486, 1450, 420, 42, "gray", ["!MCP server 추가 등으로 tool 수 증가", "~→ ② 중복 · description 구별성 확인 / ⑤ tool search"], "8map-b-port-in")
arrow([(600, 1450), (600, 1404)], ("성공률 하락 시", 608, 1440, "start"))

mk = lambda i, c: (f'<marker id="{i}" viewBox="0 0 8 8" markerWidth="7" markerHeight="7" refX="7" refY="4" orient="auto">'
                   f'<path d="M0,0.5 L8,4 L0,7.5 z" fill="{c}"/></marker>')
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
       f'aria-label="Tool 정의 설계 순서: 어떤 tool을 둘지, description 작성, system prompt 점검, 결과 크기, tool 과다 대응을 거쳐 tools 정의가 나온다" font-family="{FONT}">',
       "<title>② Tool 정의 설계: 모델이 올바른 tool을 고르게 만드는 설계 순서</title>",
       '<rect width="100%" height="100%" fill="#FFFFFF"/>',
       "<defs>" + mk("arr-8map-b", INK) + mk("arr-8map-b-blue", "#2563EB") + "</defs>"] + out + ["</svg>"]
Path(__file__).with_name("zone-b.svg").write_text("\n".join(svg) + "\n", encoding="utf-8")
print("\n".join(warns) or "no warnings")
