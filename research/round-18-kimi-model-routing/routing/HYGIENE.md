# Secrets hygiene — R18 routing artifacts (mission M4)

Gate: `python3 hygiene_check.py` scans every file in this directory plus
`.ufo/reports/round-18/kengaku.md` for (1) the exact credential values configured in
the live `~/.kimi-code/config.toml` and (2) generic credential shapes.

Credential values are read from the config inside the scan process and are never
printed, passed as arguments, or written to disk; only counts leave it. The scan was
run before this file existed and again after it was written, so the recorded run below
is the one that covers this file too.

```
$ python3 hygiene_check.py
scan root:        /home/vgpnk/Projects/shokunin/.tower/worktrees/wt-4/research/round-18-kimi-model-routing/routing
files scanned:    7
distinct configured credential values tested: 12

exact  provider alibaba-token-plan api_key                  hits=0
exact  provider alibaba-token-plan-2 api_key                hits=0
exact  provider alibaba-token-plan-3 api_key                hits=0
exact  provider cursor api_key                              hits=0
exact  provider devin api_key                               hits=0
exact  provider ds-flash-cascade api_key                    hits=0
exact  provider glm-flash-cascade api_key                   hits=0
exact  provider hyper api_key                               hits=0
exact  provider openai-codex api_key                        hits=0
exact  provider opencode-go api_key                         hits=0
exact  provider xai-oauth api_key                           hits=0
exact  provider zai-coding-plan api_key                     hits=0
shape  credential prefix                                    hits=0
shape  bearer token                                         hits=0
shape  assigned secret                                      hits=0

TOTAL HITS: 0
RESULT: PASS -- no credential value or credential-shaped string in any artifact
```

Exit status: 0 (0 = clean).

Scope notes:

- The tree contains no credential values by construction: the routing table names
  providers and lanes, never keys; `APPLY.md` describes steps generically; the splice
  tool reads the live file only when the operator runs it and prints hashes and diffs,
  not values.
- `splice_secondary.py` copies the target config to a timestamped backup with
  `shutil.copy2` (mode preserved) but never prints or stores credential values.
- The live `~/.kimi-code/config.toml` was opened read-only throughout this mission and
  was never written by it; its pinned hashes are in the routing table header and in
  `APPLY.md`.
- Re-run after the operator lane-policy revision (2026-10-15, post-review): identical
  output — 7 files scanned, 12 configured credential values tested, 0 hits, exit 0.
