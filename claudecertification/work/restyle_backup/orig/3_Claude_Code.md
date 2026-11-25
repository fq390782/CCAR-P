# 3. Claude Code — 반드시 알아야 할 지식
> 시험 비중 3% · 약 1문항 · 근거 문항 10개

## 1. 핵심 개념

### CLAUDE.md는 지시이고, settings.json은 강제다
- `CLAUDE.md`는 세션 시작 시 자동으로 전체가 로드되는 프로젝트 컨텍스트 파일입니다. 빌드 명령, 코딩 규약, "migrations 디렉터리는 건드리지 말 것" 같은 매번 알아야 할 정보를 둡니다. git에 커밋하면 팀 전체가 공유합니다. [Patrick-0028] [Udemy-0032]
- `CLAUDE.md`(그리고 `.claude/rules/`)는 모델이 참고하는 문맥일 뿐 강제되지 않습니다. 권한이나 "반드시 매번" 지켜야 하는 규칙은 settings의 permissions나 hooks로 처리합니다. [Patrick-0028] [Udemy-0017] [Udemy-0029] [Udemy-0052]
- 판단 축은 두 가지입니다. "누구에게 적용할지"(팀, 개인 전체, 이 프로젝트의 개인)와 "강제할지, 알려 주기만 할지"(settings 또는 CLAUDE.md). [Udemy-0029]

![CLAUDE.md는 모델 판단을 거치는 문맥이고 settings.json은 매번 강제되는 권한·hook이라는 비교](svg/3-claudemd-vs-settings.svg)
*그림: 같은 규칙도 CLAUDE.md에 두면 확률적 지시, settings.json에 두면 결정론적 강제가 된다.*

### 설정 파일의 범위
- `.claude/settings.json`: 프로젝트 공유 설정입니다. 커밋해서 팀 전원에게 같은 permissions, hooks, plugins를 배포합니다. [Preporato-0029] [Udemy-0029] [Udemy-0031]
- `.claude/settings.local.json`: 이 프로젝트에서만 쓰는 개인 덮어쓰기입니다. gitignore되므로(Claude Code가 만들 때 git에서 제외) 다른 팀원에게 영향을 주지 않습니다. 팀 공유용으로 쓰면 안 됩니다. [Patrick-0044] [Preporato-0029] [Udemy-0029]
- `~/.claude/settings.json`: 사용자 설정입니다. 한 사람에게 모든 프로젝트에 걸쳐 적용됩니다. [Preporato-0029] [Udemy-0029]
- `CLAUDE.local.md`는 개인용 지시, `.mcp.json`은 MCP 서버 설정입니다. 둘 다 권한 설정 파일이 아닙니다. [Preporato-0029] [Udemy-0029]
- 우선순위(높은 순): managed, command line, local, shared project, user. permissions.allow 같은 리스트형 설정은 덮어쓰지 않고 합쳐집니다. [Udemy-0029]

![설정 층 다섯 개의 우선순위와 각 층의 적용 대상](svg/3-settings-scope.svg)
*그림: 충돌하면 위쪽 층(managed > command line > local > project > user)이 이기고, permissions.allow 같은 리스트는 합쳐진다.*

### Headless / CI 실행
- `claude -p`(`--print`)는 비대화형으로 실행하고 결과를 stdout으로 돌려줍니다. 기계가 읽어야 하면 `--output-format json`을 쓰고, schema로 검증까지 붙입니다. [Amey-0049] [Udemy-0017]
- `-p` 실행에는 승인할 사람이 없으므로 허가가 필요한 작업은 거부됩니다. 필요한 도구는 `--allowedTools`로 미리 허용합니다. `--permission-mode dontAsk`를 함께 쓰면 허용 목록 밖의 작업은 묻지 않고 거부됩니다. [Udemy-0017]
- 해설에 따르면 커밋된 `.claude/settings.json`의 `permissions.allow`는 workspace trust를 수락한 뒤에만 적용되고, `-p`는 trust 대화상자를 띄우지 않습니다. 그래서 CI가 새로 checkout한 폴더에서는 이 허용 규칙이 쓰이지 않는다고 합니다. CI에서는 `--allowedTools` 또는 runner의 user/managed 설정에 허용을 둡니다. [Udemy-0017]
  - ⚠️ 공식 보안 문서는 "`-p` 비대화형 실행에서는 trust verification이 비활성화된다"고만 적고 있어, 해설과 어긋나 보입니다. 버전에 따라 동작이 다를 수 있으니 확인이 필요합니다.
- 해설에 따르면 `permissions.defaultMode`의 `auto`와 `bypassPermissions`는 project/local 설정에서는 효과가 없고, user/managed 설정이나 `--permission-mode`로만 지정할 수 있습니다. `bypassPermissions`는 격리된 환경에서만 써야 합니다. [Udemy-0017]
  - ⚠️ 이 project/local 제한은 공식 문서에서 명시적으로 확인되지 않았습니다. 검증이 필요합니다.

![CI에서 claude -p가 도구 호출을 허용·거부하고 JSON 출력을 검증해 파싱하는 흐름](svg/3-headless-ci.svg)
*그림: 무인 실행에서는 허용을 --allowedTools로 미리 주고, 출력은 --output-format json + schema로 받는다.*

### Hooks: 결정론적 실행
- hook은 lifecycle의 정해진 시점에 실행되는 사용자 정의 처리입니다(shell command, HTTP 호출 등). 모델의 판단을 거치지 않고, `matcher`(예: `Edit|Write`, `Bash`)에 맞으면 매번 실행됩니다. [Udemy-0021] [Udemy-0052]
- `PreToolUse`: 도구 실행 전에 발화하며 유일하게 실행을 막을 수 있습니다. exit code 2로 끝내거나 `hookSpecificOutput.permissionDecision`에 `deny`와 이유를 반환하면 차단됩니다. 반환값은 `allow`, `ask`, `defer`도 가능합니다. [Udemy-0052]
- `PostToolUse`: 도구 호출이 성공한 직후에 발화합니다. 감사 로그, 포맷 정리, 알림에 씁니다. 이미 실행된 뒤이므로 차단하거나 되돌릴 수 없습니다. [Udemy-0021] [Udemy-0052]
- `PostToolUseFailure`: 도구 호출이 실패했을 때만 발화합니다. 성공한 변경은 기록되지 않습니다. [Udemy-0021]

![도구 호출 전후로 PreToolUse, PostToolUse, PostToolUseFailure가 발화하는 시점과 차단 가능 여부](svg/3-hooks-lifecycle.svg)
*그림: 차단은 실행 전 PreToolUse에서만 가능하고, 실행 후 hook은 성공/실패에 따라 나뉘어 관찰만 한다.*

### 구성 요소 구분 (언제 로드되는가, 누가 쓰는가)
- `CLAUDE.md`: 사람이 쓰고, 매 세션 전체가 로드되는 규약입니다. [Udemy-0032]
- Skills: 사람이 쓰는 절차나 참고 자료입니다. 설명문만 항상 보이고, 호출되거나 관련될 때 본문이 로드되므로 길어도 컨텍스트 비용이 작습니다. custom slash command는 skills로 통합되어 `/이름`으로 호출합니다. [Udemy-0032]
- Subagent: 부모의 대화 기록 없이 독립된 컨텍스트에서 일하고 요약만 돌려줍니다. 부모 대화를 그대로 이어받는 것은 fork형 subagent뿐입니다. subagent를 부를지는 모델이 판단하므로 "반드시 매번"은 보장하지 못합니다. [Udemy-0032] [Udemy-0021] [Udemy-0052]
- auto memory(Agent Memory): 사용자의 정정이나 선호를 바탕으로 Claude가 직접 쓰는 메모입니다. 세션 시작 시 앞부분(200줄 또는 25KB까지)이 로드됩니다. [Udemy-0032]

![CLAUDE.md, skills, auto memory, subagent, hooks, plugin이 언제 로드되고 누가 쓰는지](svg/3-components-loading.svg)
*그림: CLAUDE.md는 매 세션 전체, skill은 설명문만 있다가 필요할 때 본문, subagent는 독립 컨텍스트에서 요약만 돌려준다.*

### Plugins의 팀 운영
- plugin은 skills, subagents, hooks, MCP servers를 묶어 설치하는 단위이고, 사용자 본인의 권한으로 실행됩니다. [Udemy-0031]
- 팀에 배포할 때는 project scope로 설치합니다. 그러면 활성화 정보가 커밋되는 `.claude/settings.json`에 기록되고 PR로 리뷰할 수 있습니다. 공유 설정의 일부는 각 멤버가 workspace trust를 수락한 뒤에 적용됩니다. [Udemy-0031]
- marketplace는 tag나 branch로 버전을 고정할 수 있습니다(예: `#v1.2.0`). auto-update는 marketplace별로 켜고 끕니다. 공식 marketplace는 기본값이 ON이지만 팀에서는 고정해 두고, 변경 내용을 확인한 뒤 의도적으로 업데이트합니다. [Udemy-0031]
- 도입 심사에서는 설명문이나 사용자 수만 보지 말고, 설치 화면에 표시되는 "추가되는 것"(hooks, MCP servers, skills)의 내용까지 확인합니다. [Udemy-0031]

![plugin을 심사하고 project scope로 공유한 뒤 버전을 고정해 의도적으로 업데이트하는 흐름](svg/3-plugin-team-deploy.svg)
*그림: 팀 plugin은 심사 → project scope 설치 → PR 커밋 → trust 수락 후 적용, 업데이트는 고정된 버전에서 다시 심사를 거친다.*

## 2. 상황별 정답 판단 규칙

| 이런 상황이면 | 정답 방향 | 근거 |
|---|---|---|
| CI나 스크립트에서 무인 실행하고 출력을 파싱해야 함 | `claude -p` + `--output-format json`(+ schema) | Amey-0049, Udemy-0017 |
| CI에서 확인 프롬프트 없이 필요한 도구만 실행 | `--allowedTools`로 사전 허용, 필요하면 `--permission-mode dontAsk` | Udemy-0017 |
| 매 세션 같은 빌드 명령과 규약을 다시 설명함 | 저장소 루트에 `CLAUDE.md`를 두고 커밋 | Patrick-0028 |
| 팀 공통 권한, hooks, plugins를 배포 | `.claude/settings.json` 커밋 | Preporato-0029, Udemy-0029, Udemy-0031 |
| 팀에는 영향 없이 내 머신에서만 허용 추가 | `.claude/settings.local.json` | Patrick-0044, Preporato-0029 |
| 모든 프로젝트에 걸친 개인 취향 설정 | `~/.claude/settings.json` | Preporato-0029, Udemy-0029 |
| "확실히, 매번, 모델 판단 없이" 지켜야 함 | hooks (프롬프트, CLAUDE.md, subagent는 오답) | Udemy-0021, Udemy-0052 |
| "실행 전에" 막아야 함 | `PreToolUse` + `deny` 또는 exit 2 | Udemy-0052 |
| 성공한 변경을 빠짐없이 기록 | `PostToolUse`(matcher `Edit\|Write`) | Udemy-0021 |
| 실패한 호출만 기록하거나 알림 | `PostToolUseFailure` | Udemy-0021 |
| 가끔 필요한 긴 절차나 참고 자료 | skill (`CLAUDE.md`는 매번 필요한 것만) | Udemy-0032 |
| 대량 탐색으로 부모 컨텍스트를 오염시키고 싶지 않음 | subagent (독립 컨텍스트, 요약 반환) | Udemy-0032 |
| 팀 plugin 운영 | project scope 공유 + 버전 고정 + 의도적 업데이트 | Udemy-0031 |

![강제 여부와 적용 대상, 필요 빈도로 CLAUDE.md·skill·subagent·settings 파일을 고르는 판단 트리](svg/3-decision-where.svg)
*그림: "매번, 모델 판단 없이"면 settings로 강제하고 적용 대상으로 파일을 고르며, 아니면 필요 빈도로 CLAUDE.md·skill·subagent를 고른다.*

![개입 시점으로 PreToolUse, PostToolUse, PostToolUseFailure를 고르는 판단 트리](svg/3-decision-hooks.svg)
*그림: 실행 전 차단은 PreToolUse, 성공 기록은 PostToolUse, 실패만 기록은 PostToolUseFailure.*

## 3. 자주 나오는 오답 함정

- `CLAUDE.md`에 권한이나 "CI에서는 확인 없이 실행"을 적음 → 문맥일 뿐 권한 체크에 반영되지 않습니다. [Udemy-0017] [Udemy-0029] [Patrick-0044]
- 시스템 프롬프트로 금지하거나 심사용 subagent를 둠 → 모델 판단에 의존하는 확률적 방법이라 결정론적이지 않습니다. [Udemy-0052] [Udemy-0021]
- `PostToolUse`로 위험한 명령을 차단 → 이미 실행된 뒤라 막을 수 없고 관찰만 가능합니다. [Udemy-0052]
- `PostToolUseFailure`로 감사 로그 → 성공한 변경에서는 발화하지 않습니다. [Udemy-0021]
- 개인 허용을 `.claude/settings.json`에 커밋 → 팀원 전원의 권한이 바뀝니다. [Patrick-0044]
- `.claude/settings.local.json`을 커밋해서 팀에 배포 → 개인용 파일이라 충돌이 생기고 정본 역할을 못 합니다. [Udemy-0029]
- 팀 설정을 각자의 `~/.claude/settings.json`에 수동 배포 → 버전 추적과 리뷰가 불가능합니다. [Udemy-0029] [Preporato-0029]
- CI에서 대화형 모드 사용, 출력 파일 리다이렉트, 화면 스크래핑 → 확인 대기로 멈추거나 구조화되지 않은 출력이 나옵니다. [Amey-0049] [Udemy-0017]
- 프로젝트 설정에서 `bypassPermissions`로 확인을 일괄 생략 → (해설 기준) project 설정에서는 효과가 없고, 전부 무확인은 과도합니다. [Udemy-0017]
- CLAUDE.md와 skill의 로드 시점을 거꾸로 서술 → CLAUDE.md는 항상 로드, skill은 필요할 때 로드됩니다. [Udemy-0032]
- subagent가 부모 대화를 이어받는다고 서술 → fork형만 그렇습니다. [Udemy-0032]
- auto memory를 사람이 쓰는 파일로 서술 → Claude가 씁니다. [Udemy-0032]
- plugin auto-update로 최신판 자동 배포, 설명문만 보고 심사 → 심사를 거치지 않은 hooks나 권한이 유입됩니다. [Udemy-0031]

## 4. 암기 목록

| 명령어/파일/설정 | 의미 |
|---|---|
| `CLAUDE.md` (루트 또는 `.claude/CLAUDE.md`) | 팀 공유 지시, 매 세션 로드, 강제력 없음 |
| `CLAUDE.local.md` | 개인 지시 |
| `.claude/settings.json` | 프로젝트 공유 설정(permissions, hooks, plugins), 커밋 |
| `.claude/settings.local.json` | 프로젝트 개인 덮어쓰기, gitignore |
| `~/.claude/settings.json` | 사용자 설정, 모든 프로젝트 |
| `.mcp.json` | MCP 서버 설정 |
| 우선순위 | managed > command line > local > project > user (리스트는 병합) |
| `claude -p` / `--print` | 비대화형 실행, stdout 출력 |
| `--output-format json` | 구조화된 출력 |
| `--allowedTools` | 도구 사전 허용 (예: `Bash(npm run test *)`) |
| `--permission-mode dontAsk` | 허용 밖의 작업은 묻지 않고 거부 |
| `bypassPermissions` | 모든 확인 생략, 격리 환경 한정 |
| `PreToolUse` | 실행 전, 차단 가능 (`permissionDecision: deny` 또는 exit 2) |
| `PostToolUse` | 성공 후, 기록과 알림, 차단 불가 |
| `PostToolUseFailure` | 실패 후에만 발화 |
| `matcher` | hook 대상 도구 지정 (`Edit\|Write`, `Bash`) |
| marketplace `#v1.2.0` | plugin 버전(tag) 고정 |

## 5. 시험 직전 체크리스트

- [ ] "확실히, 매번"이 나오면 hooks, "실행 전"이 나오면 `PreToolUse`
- [ ] `PostToolUse`는 차단할 수 없음, `PostToolUseFailure`는 실패할 때만 발화
- [ ] CLAUDE.md는 지시(문맥), settings.json은 강제(권한)
- [ ] 팀 공유는 `.claude/settings.json`, 개인 프로젝트용은 `.claude/settings.local.json`, 개인 전체용은 `~/.claude/settings.json`
- [ ] CI 실행은 `-p` + `--output-format json` + `--allowedTools`
- [ ] CLAUDE.md는 항상 로드, skill은 필요할 때 본문 로드
- [ ] subagent는 독립 컨텍스트에서 일하고 요약만 반환 (fork형만 대화를 이어받음)
- [ ] auto memory는 Claude가 직접 씀
- [ ] plugin은 project scope로 공유하고, 버전을 고정하고, 추가되는 hooks와 MCP까지 심사
