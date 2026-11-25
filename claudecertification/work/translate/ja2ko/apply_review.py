#!/usr/bin/env python3
"""검수 workflow 결과 반영 + 용어 통일. out_before_review/ 에 원본 백업."""
import json, glob, re
from pathlib import Path
D = Path(__file__).resolve().parent
r = json.load(open(D / "review/workflow_result.json", encoding="utf-8"))
data = {p.stem: json.load(open(p, encoding="utf-8")) for p in sorted((D / "out").glob("j*.json"))}
src = {x["id"]: x for p in sorted((D / "in").glob("j*.json")) for x in json.load(open(p, encoding="utf-8"))}
rec = {y["id"]: y for b in data.values() for y in b}
def get(y, f): return y["question"] if f == "question" else y["choices"][f]
def put(y, f, v):
    if f == "question": y["question"] = v
    else: y["choices"][f] = v
log = []
# 1) 배치별 검수에서 채택된 지적 (용어 일관성 지적은 아래 2·3에서 일괄 처리)
OVERRIDE = {("CCAR-F-Udemy01-0033", "A"): ("추출 결과를 합성한 assistant 메시지로", "추출 결과를 담아 인위적으로 만든 assistant 메시지로")}
for f in r["findings"]:
    if f["source"] == "consistency" or not f["accepted"]: continue
    old, new = OVERRIDE.get((f["id"], f["field"]), (f["final_old"], f["final_new"]))
    y = rec[f["id"]]; s = get(y, f["field"])
    assert s.count(old) == 1, (f["id"], f["field"], old)
    put(y, f["field"], s.replace(old, new)); log.append(("fix", f["id"], f["field"]))
# 2) 시나리오 이름: 한국어로 통일 (용어 일관성 검수 결과)
SCEN = [("customer support resolution agent", "고객 지원 해결 agent"),
        ("multi-agent research system", "multi-agent 리서치 시스템"),
        ("structured data extraction system", "구조화 데이터 추출 시스템"),
        ("구조화된 데이터 추출", "구조화 데이터 추출")]
# 3) 기술 용어: 영어 표기로 통일 (사용자 방침 "기술 용어는 전부 영어", CCAR-F 영어 원문 번역(ko_v2)과도 일치)
TERMS = [(r"리팩[터토]링", "refactoring"), ("다운스트림", "downstream"), ("메타데이터", "metadata"), ("파이프라인", "pipeline"),
         ("커밋", "commit"), ("스트리밍", "streaming"), ("지수 백오프", "exponential backoff"), ("백오프", "backoff"),
         ("타임아웃", "timeout"), ("라우팅", "routing"), ("샌드박스", "sandbox"), ("플러그인", "plugin"), ("호스트", "host"),
         ("MCP 서버", "MCP server"), ("커스텀", "custom")]
for y in rec.values():
    ja = src[y["id"]]["question"] + "".join(src[y["id"]]["choices"].values())
    batch_ok = "バッチ" in ja and "配置" not in ja          # 배치 = バッチ(batch)일 때만. 配置(배치)와 구분
    for f in ["question", *y["choices"]]:
        s0 = s = get(y, f)
        for a, b in SCEN: s = s.replace(a, b)
        for a, b in TERMS: s = re.sub(a, b, s)
        if batch_ok: s = s.replace("배치", "batch")
        if s != s0: put(y, f, s); log.append(("term", y["id"], f))
for n, b in data.items():
    (D / "out" / f"{n}.json").write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
print("검수 반영", sum(1 for x in log if x[0] == "fix"), "/ 용어 통일 필드", sum(1 for x in log if x[0] == "term"))
