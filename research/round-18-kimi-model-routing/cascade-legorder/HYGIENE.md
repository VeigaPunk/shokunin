# Secrets hygiene — R18 cascade-legorder artifacts (mission M7)

Gate: `python3 hygiene_check.py` scans every file under this directory for (1) the exact
credential values configured in the live `~/.kimi-code/config.toml`, (2) the leg defaults
the live `~/.local/share/ds-flash-shim/shim.py` carries, and (3) generic credential shapes.

Credential values are read from the config and the shim inside the scan process and are
never printed, passed as arguments, or written to disk; only counts leave the process.
Exit status 0 = clean, 1 = hits found. The scan was run before this file existed and again
after it was written, so the recorded run below covers this file too.

```
$ python3 hygiene_check.py
scan root:        /home/vgpnk/Projects/shokunin/.tower/worktrees/wt-7/research/round-18-kimi-model-routing/cascade-legorder
files scanned:    15
distinct credential values tested: 17

exact  config provider alibaba-token-plan api_key   hits=0
exact  config provider alibaba-token-plan-2 api_key hits=0
exact  config provider alibaba-token-plan-3 api_key hits=0
exact  config provider cursor api_key               hits=0
exact  config provider devin api_key                hits=0
exact  config provider ds-flash-cascade api_key     hits=0
exact  config provider glm-flash-cascade api_key    hits=0
exact  config provider hyper api_key                hits=0
exact  config provider openai-codex api_key         hits=0
exact  config provider opencode-go api_key          hits=0
exact  config provider opencode-go header x-opencode-session hits=0
exact  config provider xai-oauth api_key            hits=0
exact  config provider zai-coding-plan api_key      hits=0
exact  shim default DS_LEG1_KEY                     hits=0
exact  shim default DS_LEG2_KEY                     hits=0
exact  shim default DS_LEG3_KEY                     hits=0
exact  shim default DS_LEG3_SESSION                 hits=0
shape  credential prefix                            hits=0
shape  opencode key                                 hits=0
shape  bearer token                                 hits=0
shape  jwt                                          hits=0
shape  assigned secret                              hits=0

TOTAL HITS: 0
RESULT: PASS -- no credential value or credential-shaped string in any artifact
```

Exit status: 0 (0 = clean).

## Gate history (the gate caught a real defect)

The first run over this directory (13 files) **failed with 7 hits**, all in one file:
`raw/shim-py-diff-masked.txt`. The diff recorder had masked credentials by *shape* only
(`sk-...` runs), and the token-plan key and the opencode session value contain characters
that end such a run early, so the full values survived into the artifact. The recorder was
changed to mask every configured credential by exact match — keeping a 4-character prefix
and the length — and the artifact was regenerated from disk. No credential-bearing artifact
was committed, pushed, or published at any point: the affected file lived only in this
worktree, and the delivered tree passes the gate above with 0 hits.

## Scope notes

- The tree contains no credential values by construction. `LEGORDER.md` names endpoints and
  providers, never keys; the masked diffs show `xxyy...<masked:NN chars>` in place of every
  secret; `apply-record-*.json` holds hashes, byte counts and line numbers only.
- `scripts/apply_legorder.py` reads the token-plan key from the live config inside the
  process to write it into the live shim; it prints a masked diff and stores no value.
- The shim's own leg keys remain in `~/.local/share/ds-flash-shim/shim.py` as module
  defaults — that is how the file was built and how it must stay for the shim to start
  without env overrides. The unit file's commented plaintext keys (the M1 vuln finding) were
  preserved byte-for-byte, not touched by this mission.
- The host files this mission edited are outside the repository, so no credential material
  can enter the branch diff through them.