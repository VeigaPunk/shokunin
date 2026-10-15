# Secrets hygiene -- R18 definitions audit

Gate: `bash scripts/hygiene_check.sh` scans every file in this tree, raw
captures included, for (1) the exact credential values in the live config and
(2) generic credential shapes.

Credential values are read from the config inside the scan process and are
never printed, passed as arguments, or written to disk; only counts leave it.

```
scan root:        /home/vgpnk/Projects/shokunin/.tower/worktrees/wt-2/research/round-18-kimi-model-routing
files scanned:    23
distinct configured credential values tested: 12

exact  provider alibaba-token-plan api_key          hits=0 
exact  provider alibaba-token-plan-2 api_key        hits=0 
exact  provider alibaba-token-plan-3 api_key        hits=0 
exact  provider zai-coding-plan api_key             hits=0 
exact  provider hyper api_key                       hits=0 
exact  provider opencode-go api_key                 hits=0 
exact  provider opencode-go header x-opencode-session hits=0 
exact  provider openai-codex api_key                hits=0 
exact  provider devin api_key                       hits=0 
exact  provider xai-oauth api_key                   hits=0 
exact  provider cursor api_key                      hits=0 
exact  provider ds-flash-cascade api_key            hits=0 
exact  provider glm-flash-cascade api_key           hits=0 

shape  credential prefix                            hits=0 
shape  bearer token                                 hits=0 
shape  assigned secret                              hits=0 

TOTAL HITS: 0
RESULT: PASS -- no credential value or credential-shaped string in any artifact
```

Exit status: 0 (0 = clean). Probe captures record credential header
names with a `<redacted:len=N>` marker instead of values
(see scripts/common.py `redact_headers`).
