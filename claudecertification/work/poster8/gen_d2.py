"""8장 통합 개념 지도 zone d2 (MCP 연결 · 운영) SVG 생성. 실행: python3 -I work/poster8/gen_d2.py"""
from pathlib import Path
from xml.sax.saxutils import escape

W, H = 2360, 1300
Z = "8map-d2"
KIND = {
    "gray": ("#F3F4F6", "#9CA3AF"), "blue": ("#DBEAFE", "#2563EB"), "red": ("#FEE2E2", "#DC2626"),
    "yellow": ("#FEF3C7", "#D97706"), "green": ("#DCFCE7", "#16A34A"), "frame": ("#FFFFFF", "#9CA3AF"),
}
COL = {"dark": "#1F2937", "blue": "#2563EB", "red": "#DC2626", "green": "#16A34A"}
out, warn, n = [], [], [0]


def tw(s, size=13, bold=False):
    w = sum(size if ord(c) > 0x2000 else size * 0.58 for c in s)
    return w * (1.06 if bold else 1)


def nid(p):
    n[0] += 1
    return f"{Z}-{p}{n[0]}"


def text(x, y, s, size=13, anchor="start", bold=False, fill="#1F2937"):
    b = ' font-weight="bold"' if bold else ""
    out.append(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}"{b} fill="{fill}" xml:space="preserve">{escape(s)}</text>')


def norm(lines, bold_first):
    r = []
    for i, l in enumerate(lines):
        s, size = (l, 13) if isinstance(l, str) else l
        r.append((s, size, bold_first and i == 0))
    return r


def box(x, y, w, h, lines, kind="gray", bold_first=True, align="middle", lh=19):
    f, s = KIND[kind]
    out.append(f'<rect id="{nid("b")}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{f}" stroke="{s}" stroke-width="1.5"/>')
    ls = norm(lines, bold_first)
    if len(ls) * lh > h - 6:
        warn.append(f"tall: {ls[0][0]}")
    by = y + h / 2 - (len(ls) - 1) * lh / 2 + 4.5
    for i, (t, size, b) in enumerate(ls):
        if tw(t, size, b) + 20 > w:
            warn.append(f"wide {tw(t, size, b) + 20:.0f}>{w}: {t}")
        tx = x + w / 2 if align == "middle" else x + 12
        text(tx, round(by + i * lh, 1), t, size, align, b)


def diamond(cx, cy, hw, hh, lines, lh=18):
    f, s = KIND["yellow"]
    out.append(f'<polygon id="{nid("d")}" points="{cx},{cy - hh} {cx + hw},{cy} {cx},{cy + hh} {cx - hw},{cy}" fill="{f}" stroke="{s}" stroke-width="1.5"/>')
    by = cy - (len(lines) - 1) * lh / 2 + 4.5
    for i, t in enumerate(lines):
        if tw(t, 13, True) > hw * 1.25:
            warn.append(f"diamond wide: {t}")
        text(cx, by + i * lh, t, 13, "middle", True)


def arrow(pts, label=None, lx=0, ly=0, anchor="start", color="dark", w=1.5, size=13):
    m = f"arr-{Z}" + ("" if color == "dark" else f"-{color}")
    p = " ".join(f"{x},{y}" for x, y in pts)
    out.append(f'<polyline points="{p}" fill="none" stroke="{COL[color]}" stroke-width="{w}" marker-end="url(#{m})"/>')
    if label:
        text(lx, ly, label, size, anchor)
    else:
        warn.append(f"no label {pts}")


def frame(x, y, w, h, title, key, cid):
    f, s = KIND["frame"]
    out.append(f'<rect id="{Z}-{cid}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{f}" stroke="{s}" stroke-width="1.5"/>')
    text(x + 20, y + 28, title, 16, bold=True)
    text(x + 20, y + 47, key, 11, fill="#6B7280")


# ---------- 1-14 MCP connector ----------
frame(24, 84, 1132, 476, "1-14 MCP connector · Messages API의 mcp_servers",
      "전제 = 앱이 MCP client 직접 구현 ✗ · beta 기능 → beta 헤더 첨부", "c14")
box(600, 16, 72, 50, [("MCP", 12), ("connector", 11)], "blue", lh=16)
box(44, 150, 316, 180, ["앱 (MCP client 구현 ✗)", "요청에 적는 3가지 = 활성화", "① mcp_servers = 접속(URL · 인증)",
                        ("     type · url · name · authorization_token", 11), "② tools의 mcp_toolset = tool 활성화",
                        ("     mcp_server_name으로 서버 참조", 11), "③ beta 헤더"], "blue", align="start", lh=22)
box(516, 150, 240, 56, ["Messages API", ("tool 목록 조회 → 제시 → 호출 대행", 12)], "blue")
box(916, 150, 220, 56, ["원격 MCP server", ("HTTP: Streamable HTTP · SSE", 12)])
arrow([(636, 150), (636, 66)], "API가 조회 · 호출 대행", 646, 124, w=2.5)
arrow([(360, 168), (516, 168)], "요청", 438, 162, "middle")
arrow([(516, 192), (360, 192)], "mcp_tool_use ·", 438, 207, "middle", size=11)
text(438, 220, "mcp_tool_result 함께 수신", 11, "middle")
arrow([(756, 168), (916, 168)], "목록 조회 · 호출", 836, 162, "middle")
arrow([(916, 192), (756, 192)], "tool 결과", 836, 209, "middle")
box(384, 244, 416, 56, ["✗ mcp_tool_use 수신 후 앱이 tools/call 재실행", "→ API가 이미 실행 · 쓰기 작업 중복 위험"], "red")
arrow([(636, 206), (636, 244)], "앱이 다시 실행하면", 644, 230, color="red")
box(384, 340, 416, 56, ["mcp_toolset 설정: default_config = 전체 기본값", "configs = tool별 enabled 덮어쓰기"], bold_first=False)
arrow([(300, 330), (300, 368), (384, 368)], "tool별 설정", 306, 385, size=11)
box(384, 440, 200, 100, ["다중 서버", "서버마다 mcp_toolset 1개", "→ 한 요청에서 횡단 선택"], "blue")
box(600, 440, 200, 100, ["읽기 전용 제한", ("쓰기 tool만 enabled: false", 12), "= denylist", "allowlist 형태도 가능"], "blue")
arrow([(484, 396), (484, 440)], "서버 여러 개", 492, 424, color="blue")
arrow([(700, 396), (700, 440)], "읽기 전용", 708, 424, color="blue")
box(44, 404, 316, 60, ["✗ mcp_toolset 생략 → 자동 검출 의존", "서버마다 정확히 1개 참조 규칙 위반"], "red")
box(44, 480, 316, 60, ["✗ 서버별로 요청 나눠 JSON 수동 전달", "한 요청 안 횡단 선택 요건 미충족"], "red")
box(836, 244, 300, 56, ["✗ 로컬 stdio 서버 연결", "HTTP 공개 서버만 연결 가능"], "red")
arrow([(1026, 206), (1026, 244)], "stdio 서버라면", 1034, 230, color="red")
box(836, 320, 300, 56, [("✗ resources(약관 문서) · prompts 읽힘", 12), "MCP 사양 중 tool 호출만 지원"], "red")
arrow([(986, 376), (986, 414)], "문서를 읽혀야 하면", 994, 400, color="blue")
box(836, 414, 300, 56, ["앱이 직접 가져와 메시지에 포함", "또는 문서 반환 tool을 서버에 구현"], "blue", bold_first=False)
box(836, 484, 300, 56, ["미제공: Amazon Bedrock ·", "Google Cloud(Google managed)"], bold_first=False)

# ---------- 1-25 인증 방침 · connector tool 제어 ----------
frame(1180, 84, 1156, 476, "1-25 인증 방침 · connector tool 제어", "인증은 신뢰 경계가 있는 곳에만", "c25")
box(1496, 16, 320, 46, ["인증 방침 · connector tool 제어"], "blue")
diamond(1656, 190, 120, 40, ["MCP server", "연결 대상?"])
arrow([(1656, 62), (1656, 150)], "① 인증 방침", 1664, 138, w=2.5)
arrow([(1760, 62), (1760, 104), (2088, 104), (2088, 146)], "② claude.ai connector tool 제어", 1924, 98, "middle", w=2.5)
diamond(2088, 186, 150, 40, ["connector tool을", "Claude가 보기 전 차단?"])
arrow([(1536, 190), (1320, 190), (1320, 262)], "로컬 stdio (사용자가 spawn)", 1428, 184, "middle", color="blue")
box(1200, 262, 240, 56, ["사용자 신뢰 상속", "OAuth는 얻는 것 없음"], "blue")
arrow([(1656, 230), (1656, 262)], "원격 (네트워크 경유)", 1664, 251, color="blue")
box(1511, 262, 290, 72, ["OAuth 필수", ("⚠️ 1-13은 OAuth '권장' · 해설 표현 차이", 11),
                         ("공식 문서: MCP 인증 OPTIONAL · HTTP는 SHOULD", 11)], "blue")
arrow([(1656, 334), (1656, 372)], "인증을 빼면", 1664, 358, color="red")
box(1511, 372, 290, 72, ["✗ 인증 없음 (네트워크 = principal ✗)", "✗ 로컬 API key + 원격 무인증", "= 배치 반대"], "red", bold_first=False)
arrow([(1320, 318), (1320, 368)], "예외 조건 확인", 1328, 348)
diamond(1320, 412, 120, 44, ["socket listen 또는", "여러 사용자 공유?"])
arrow([(1320, 456), (1320, 488)], "예", 1328, 477, color="blue")
box(1200, 488, 240, 52, ["방침 반전 → 인증 필요", "여러 사용자 공유 = OAuth 필요"], "blue")
arrow([(1440, 412), (1480, 412), (1480, 511), (1511, 511)], "아니오인데 OAuth 추가", 1488, 469, color="red")
box(1511, 482, 290, 58, ["✗ 경계 없는데도 모든 server에 OAuth", "= 보안 쇼 · 구성 비용"], "red", bold_first=False)
arrow([(2088, 226), (2088, 270)], "blocked만 제거 가능", 2096, 253, color="blue")
box(1968, 270, 240, 72, ["조직 제어 blocked", "Claude가 보기 전에", "목록에서 tool 제거"], "blue")
arrow([(1938, 186), (1900, 186), (1900, 440)], "allow 규칙?", 1908, 418, color="red")
arrow([(2238, 186), (2276, 186), (2276, 440)], "idle timeout?", 2268, 418, "end", color="red")
box(1860, 440, 220, 72, ["✗ allow 규칙", "프롬프트 없이 실행 허용", "차단 ✗"], "red")
box(2096, 440, 220, 72, ["✗ idle timeout 0", "tool 숨김 수단 ✗"], "red")

# ---------- backbone ----------
diamond(170, 662, 130, 50, ["MCP server를", "어디에서 연결?"])
for x, y in ((590, 640), (900, 686), (1400, 686), (1656, 640)):
    out.append(f'<polyline points="300,662 {x},662 {x},{y}" fill="none" stroke="#1F2937" stroke-width="2.5" marker-end="url(#arr-{Z})"/>')
text(590, 681, "Messages API에서", 13, "middle")
text(900, 653, "Claude Code에서", 13, "middle")
text(1400, 653, "Agent SDK에서", 13, "middle")
text(1668, 678, "세 경로 공통", 13)
box(460, 592, 260, 48, ["MCP connector", ("API가 tool 조회 · 호출 대행", 12)], "blue")
box(750, 686, 300, 48, ["server scope · .mcp.json", ("비밀은 ${VAR} · 값은 각자 환경", 12)], "blue")
box(1240, 686, 320, 48, ["한 session에 여러 server", ("tool 정의 로드 = tool search", 12)], "blue")
box(1506, 592, 300, 48, ["인증 방침 · tool 제어", ("신뢰 경계에만 인증 · blocked로 차단", 12)], "blue")
arrow([(590, 592), (590, 560)], "mcp_servers 정의", 598, 581, w=2.5)
arrow([(1656, 592), (1656, 560)], "연결마다 확인", 1664, 581, w=2.5)
arrow([(900, 734), (900, 764)], "claude mcp add --scope", 908, 754, w=2.5)
arrow([(1400, 734), (1400, 764)], "mcpServers 등록", 1408, 754, w=2.5)
# 범례
text(1870, 612, "범례", 14, bold=True)
for i, (k, t) in enumerate((("gray", "일반 단계"), ("blue", "정답 · 권장 경로"), ("red", "오답 함정"),
                            ("yellow", "판단 분기"), ("green", "성공 · 종료"))):
    lx, ly = 1870 + (i % 2) * 230, 628 + (i // 2) * 32
    f, s = KIND[k]
    out.append(f'<rect x="{lx}" y="{ly}" width="30" height="18" rx="4" fill="{f}" stroke="{s}" stroke-width="1.5"/>')
    text(lx + 40, ly + 14, t)
out.append(f'<line x1="2100" y1="701" x2="2130" y2="701" stroke="#1F2937" stroke-width="2.5" marker-end="url(#arr-{Z})"/>')
text(2140, 706, "굵은 화살표 = 주 흐름")

# ---------- 1-22 scope · credential ----------
frame(24, 764, 1132, 512, "1-22 MCP server scope · .mcp.json credential (Claude Code)",
      "공유 = project · 개인 = user · 비밀 = ${VAR}", "c22")
diamond(322, 868, 150, 40, ["이 server를", "누가 · 어디서 쓰나?"])
arrow([(172, 868), (129, 868), (129, 950)], "이 프로젝트만 · 개인 시험", 137, 934, color="blue")
arrow([(322, 908), (322, 950)], "개인 · 여러 repo", 330, 934, color="blue")
arrow([(472, 868), (515, 868), (515, 950)], "팀 전원", 523, 934, color="blue")
box(44, 950, 170, 90, ["local (기본값)", "~/.claude.json", ("본인만 · 현재 프로젝트", 12)], "blue")
box(232, 950, 170, 90, ["user", "~/.claude.json", ("본인 · 모든 프로젝트", 12)], "blue")
box(430, 950, 170, 90, ["project", "루트 .mcp.json", "commit → 팀 공유"], "blue")
arrow([(129, 1040), (129, 1076)], "기본 명령으로 추가", 137, 1063, color="red", size=11)
box(44, 1076, 170, 84, ["✗ 동료에게 안 보임", ("원인 = local 저장", 12), ("→ --scope project", 12), ("로 재추가", 12)], "red", lh=18)
arrow([(322, 1040), (322, 1076)], "팀 공유에 쓰면", 330, 1063, color="red", size=11)
box(232, 1076, 170, 84, ["✗ 팀 공유를", "user scope 재등록으로", "user = 본인만"], "red", bold_first=False)
arrow([(515, 1076), (515, 1040)], "이동", 523, 1063, color="blue", size=11)
box(430, 1076, 170, 84, ["시험 서버가", "팀용으로 굳어짐", "→ project로 이동"], bold_first=False)
box(44, 1188, 556, 64, [("✗ 개인 · 실험 서버를 .mcp.json에 commit (+ .gitignore) → 개인 설정을 팀에 떠넘김", 12),
                        ("✗ 개발자마다 local scope 수동 추가 → 전파 ✗ · 수동 단계 반복", 12)], "red", bold_first=False, align="start", lh=22)
box(696, 826, 440, 92, [("✗ token을 .mcp.json에 직접 기재 (.gitignore · 접근 제한 병행)", 12), "     → 접근 제한과 무관하게 유출",
                        "✗ token을 CLAUDE.md에 기재 → context · 출력 · 로그로 유출",
                        "✗ $PR_API_TOKEN (중괄호 없음) = 문서화된 확장 구문 ✗"], "red", bold_first=False, align="start", lh=20)
arrow([(916, 950), (916, 918)], "값을 직접 적으면", 924, 939, color="red")
box(696, 950, 440, 76, [".mcp.json에는 ${VAR} 참조만 · 실제 값은 각자 환경",
                        ("headers: Bearer ${PR_API_TOKEN} · ${VAR:-default} = 기본값", 12),
                        ("알려진 credential 변수명 = 빈 값 처리 → 자체 변수명 사용", 12)], "blue", lh=21)
arrow([(600, 988), (696, 988)], "개인별 token", 648, 982, "middle", color="blue")
arrow([(806, 1026), (806, 1062)], "Claude Code 시작 시 확장", 814, 1049)
diamond(806, 1102, 110, 40, ["각자 환경에", "변수 설정?"])
arrow([(916, 1102), (966, 1102)], "예", 941, 1096, "middle", color="green")
box(966, 1072, 170, 60, ["${VAR} 확장", "→ 인증 성공"], "green")
arrow([(806, 1142), (806, 1178)], "아니오", 814, 1165, color="red")
box(696, 1178, 440, 74, [("미설정 + default 없음: config 로드 · 경고 · ${VAR} 원문 사용", 12),
                         ("→ 일부 멤버만 401 · claude mcp list에 미설정 변수 경고", 12),
                         ("→ 조치: 각자 token 설정 (✗ scope · 승인 문제로 진단)", 12)], bold_first=False, align="start", lh=21)

# ---------- 1-23 여러 server · tool search ----------
frame(1180, 764, 1156, 512, "1-23 여러 MCP server를 한 session에 (Agent SDK) · tool search",
      "서버를 나누거나 합치지 않고 한 session에 연결", "c23")
box(1200, 828, 300, 76, ["여러 server 모두 등록", "mcpServers 옵션 또는 .mcp.json"], "blue")
arrow([(1350, 904), (1350, 944)], "연결 시 모든 server tool 검색", 1358, 929)
box(1200, 944, 300, 76, ["한 session", "mcp__서버이름__tool이름 으로 나열", ("→ agent에서 동시 사용 · 서버 횡단 요청", 12)])
arrow([(1500, 866), (1893, 866)], "MCP tool 정의를 context에 로드", 1696, 860, "middle")
arrow([(1500, 982), (1600, 982)], "상태 확인", 1550, 976, "middle")
box(1600, 944, 170, 76, ["system/init", "서버별 연결 상태", ("failed · needs-auth", 12)])
arrow([(1350, 1020), (1350, 1060)], "MCP tool 호출", 1358, 1045)
diamond(1350, 1100, 130, 40, ["MCP tool이", "allowedTools에 있나?"])
arrow([(1480, 1100), (1600, 1100)], "아니오", 1540, 1094, "middle")
box(1600, 1070, 170, 60, ["권한 확인으로", "이동"], bold_first=False)
arrow([(1350, 1140), (1350, 1180)], "예", 1358, 1165, color="green")
box(1200, 1180, 300, 64, ["허용 → 실행", ("서버 단위 와일드카드 mcp__caselaw__*", 12)], "green")
box(1560, 1160, 210, 92, ["✗ 서버별 session · 라우터", "· 서버 통합", "✗ 서버 하나만 연결", "→ 요청이 매번 중단"], "red", bold_first=False, lh=20)
diamond(2063, 866, 170, 40, ["ENABLE_TOOL_SEARCH", "설정은?"])
arrow([(2063, 930), (2237, 930), (2237, 960)], "false", 2245, 951, color="red")
arrow([(2063, 906), (2063, 930), (1889, 930), (1889, 960)], "기본", 1897, 951, color="blue")
arrow([(2063, 906), (2063, 960)], "auto", 2071, 951, color="blue")
box(1810, 960, 158, 84, ["tool search 활성", ("필요할 때까지", 12), ("정의 로드 지연", 12)], "blue")
box(1984, 960, 158, 84, [("context window 10%", 12), ("도달 전 = 미리 로드", 12), ("도달 후 = tool search", 11)], "blue")
box(2158, 960, 158, 84, ["✗ 임계값 규칙", "충족 ✗", ("(오답 보기)", 12)], "red")
arrow([(2063, 1044), (2063, 1090)], "비율 조건이 필요하면", 2071, 1072, color="blue")
box(1810, 1090, 506, 56, ["임계값 규칙 = 기본 설정 + ENABLE_TOOL_SEARCH=auto", ("정의가 window 일정 비율일 때만 tool search", 12)], "blue")
arrow([(1932, 1146), (1932, 1184)], "alwaysLoad?", 1940, 1170, color="red")
arrow([(2193, 1146), (2193, 1184)], "직접 구현?", 2201, 1170, color="red")
box(1810, 1184, 245, 60, ["✗ alwaysLoad로 임계값 구현", ("한 서버 tool을 미리 로드할 뿐", 12)], "red", bold_first=False)
box(2071, 1184, 245, 60, ["✗ 별도 랭킹 서비스 작성", ("기본 설정 + auto로 충족", 12)], "red", bold_first=False)

markers = "".join(
    f'<marker id="arr-{Z}{"" if k == "dark" else "-" + k}" markerUnits="userSpaceOnUse" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 z" fill="{c}"/></marker>'
    for k, c in COL.items())
label = "MCP 연결과 운영: Messages API의 MCP connector, Claude Code의 scope와 credential, Agent SDK의 다중 server와 tool search, 공통 인증 방침과 connector tool 제어"
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{label}" '
       f'font-family="Apple SD Gothic Neo, Noto Sans KR, Malgun Gothic, sans-serif">\n<title>{label}</title>\n'
       f'<rect width="100%" height="100%" fill="#FFFFFF"/>\n<defs>{markers}</defs>\n' + "\n".join(out) + "\n</svg>\n")
Path(__file__).with_name("zone-d2.svg").write_text(svg, encoding="utf-8")
print("\n".join(warn) or "no warnings")
