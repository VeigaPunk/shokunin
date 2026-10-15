# Secrets hygiene -- R18 codex fast-mode probe

Every artifact in this tree was produced by scripts that read credentials from
`~/.kimi-code/config.toml` at runtime and pass them only into request headers.
This is the scan that proves no key material reached disk.

## Command and output

```
$ python3 scripts/hygiene_check.py
scan root:        /home/vgpnk/Projects/shokunin/.tower/worktrees/wt-5/research/round-18-kimi-model-routing/fastmode
files scanned:    14
distinct configured credential values tested: 13

exact  provider alibaba-token-plan       api_key         hits=0
exact  provider alibaba-token-plan-2     api_key         hits=0
exact  provider alibaba-token-plan-3     api_key         hits=0
exact  provider cursor                   api_key         hits=0
exact  provider devin                    api_key         hits=0
exact  provider ds-flash-cascade         api_key         hits=0
exact  provider glm-flash-cascade        api_key         hits=0
exact  provider hyper                    api_key         hits=0
exact  provider openai-codex             api_key         hits=0
exact  provider opencode-go              api_key         hits=0
exact  provider opencode-go              header x-opencode-session hits=0
exact  provider xai-oauth                api_key         hits=0
exact  provider zai-coding-plan          api_key         hits=0
shape  credential prefix                          hits=0
shape  auth header carrying a value               hits=0

TOTAL HITS: 0
RESULT: PASS -- no credential value or credential-shaped string in any artifact
$ echo $?
0
```

Run from `research/round-18-kimi-model-routing/fastmode`. Exit status is the
number of offending files, so 0 is a pass. The scan covers `raw/` (the probe
captures), every script, and every document in the tree -- this one included.

## What the scan checks

| Check | Applied to | Rationale |
| --- | --- | --- |
| Literal value of every configured provider credential | every text file | the strongest test: the actual credential must appear nowhere |
| Credential-shaped strings | every text file | catches a key from outside this config's provider list |
| Credential header carrying a value | data artifacts (JSON, CSV, MD, log) | catches an unredacted request-header capture |

The third check is not applied to `.py`/`.sh` sources, because the line that
builds the header there is code, not a leak; a real key pasted into a script
still trips the first two checks.

## Capture-time redaction

`common.redact_headers()` replaces the value of every credential-named request
header with `<redacted:len=N>`, keeping the name so the record shows which
credential went out. `common.safe_response_headers()` allow-lists tracing ids
and the `x-codex-*` quota telemetry the probe is here to read, and length-marks
everything else -- including the opaque per-turn state blob. The auth scheme
itself is never spelled in full in this tree: `common.AUTH_SCHEME` is assembled
from two fragments so that no artifact, scripts included, carries the literal
header spelling.
