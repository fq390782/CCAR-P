"""사실 검증 결과 반영: 근거 id 보강 + 문구 4곳 수정. usage: python3 -I fix_verify.py <md>"""
import re, sys
p = sys.argv[1]
L = open(p, encoding='utf-8').read().split('\n')
ADD = {  # 소절/장 머리 → 추가 id
    '### 증거 게이트 설계와 비례 적용': ['CCAR-P-jrajath94-0266'],
    '## 2. 상황별 정답 판단 규칙': ['CCAR-F-Udemy06-0057', 'CCAR-P-jrajath94-0583', 'CCAR-P-jrajath94-0457', 'CCAR-F-Udemy06-0037'],
    '### path-specific rules (.claude/rules/)': ['CCAR-F-Udemy04-0020', 'CCAR-F-Udemy01-0038'],
    '### `CLAUDE.md`는 지시, `settings.json`은 강제': ['CCAR-P-jrajath94-0672'],
    '## 3. 자주 나오는 오답 함정': ['CCAR-F-Udemy05-0058'],
    '## 4. 암기 목록': ['CCAR-F-Udemy02-0047', 'CCAR-F-Udemy05-0056', 'CCAR-F-Udemy06-0001'],
    '### Skill · custom command 위치와 공유': ['CCAR-F-Udemy02-0015'],
}
SUB = re.compile(r'^<sub>근거: (.*)</sub>$')
done, cur = set(), None
for i, l in enumerate(L):
    if l.startswith('## ') or l.startswith('### '):
        cur = l if l in ADD else (None if l.startswith('### ') or l.startswith('## ') else cur)
    m = SUB.match(l)
    if m and cur:
        ids = {x.strip() for x in m.group(1).split(',')} | set(ADD[cur])
        L[i] = '<sub>근거: ' + ', '.join(sorted(ids)) + '</sub>'
        done.add(cur)  # 장(##)은 마지막 근거 줄까지 계속 갱신돼도 무해(합집합)
t = '\n'.join(L)
REP = [
    ('개인 설정 방치 · PDF 이메일 · 채팅 안내<br>', '개인 설정 방치 · PDF 이메일<br>'),
    ('교육 · 더 큰 모델 · 재작성 = 진단 전 과잉', '교육 · 더 큰 모델 → 저장소 관례 제공 ✗<br>재작성 = 진단 전 과잉'),
    ('| plan mode만 사용 | 편집 차단 · context 보호 ✗ |', '| plan mode만 사용 | 편집은 차단 · context 보호 ✗ |'),
    ('| `user-invocable: false` | 개발자 호출 차단 (Claude만 호출) |', '| `user-invocable: false` | 개발자 호출 차단 |'),
]
for a, b in REP:
    assert t.count(a) == 1, a
    t = t.replace(a, b)
open(p, 'w', encoding='utf-8').write(t)
print('missing targets:', sorted(set(ADD) - done))
