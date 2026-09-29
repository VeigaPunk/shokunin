# Labrat probes — round 10

All measurements below were made from `shokunin` at the working tree used for this seat. Snapshot runs extract committed trees, so their `dirty=0` lines are part of the gate output. Wall time is the measured shell interval in whole seconds from `date +%s`.

## 1. Frozen snapshots

Command (run once per row): `node .ufo/waves/round-9/corpus-gate.mjs --snapshot <repo> <commit>`.

| frozen key | wall time | verbatim expectation line | verbatim process line | process exit |
|---|---:|---|---|---:|
| `kasegi-shokunin@b7180b0` | 0 s | `# expect kasegi-shokunin@b7180b0 MATCH exit=1 ids=49` | `# process-exit 1 (failed)` | 1 |
| `kengaku-shokunin@f09ff1f` | 0 s | `# expect kengaku-shokunin@f09ff1f MATCH exit=1 ids=28` | `# process-exit 1 (failed)` | 1 |
| `kake-shokunin@a209441` | 0 s | `# expect kake-shokunin@a209441 MATCH exit=1 ids=37` | `# process-exit 1 (failed)` | 1 |
| `kake-shokunin@4c9a985` | 0 s | `# expect kake-shokunin@4c9a985 MATCH exit=1 ids=34` | `# process-exit 1 (failed)` | 1 |
| `kumitate-shokunin@7a099b2` | 0 s | `# expect kumitate-shokunin@7a099b2 MATCH exit=1 ids=36` | `# process-exit 1 (failed)` | 1 |
| `kotoba-shokunin@63ceba7` | 0 s | `# expect kotoba-shokunin@63ceba7 MATCH exit=1 ids=75` | `# process-exit 1 (failed)` | 1 |
| `kagi-shokunin@4b8c018` | 0 s | `# expect kagi-shokunin@4b8c018 MATCH exit=1 ids=51` | `# process-exit 1 (failed)` | 1 |
| `kagi-shokunin@4391b3b` | 0 s | `# expect kagi-shokunin@4391b3b MATCH exit=1 ids=46` | `# process-exit 1 (failed)` | 1 |

The first full-output run also printed each corresponding `# tree ... revision=<full commit> dirty=0 mode=snapshot` line and the final `# verdict ... findings=<ids> ...` line; the concise rerun above captured the required expectation/process lines and exit codes.

### Throwaway drift probe

Commands:

```text
cp .ufo/waves/round-9/corpus-gate.mjs /tmp/gate-drift-probe.mjs
cp .ufo/waves/round-9/corpus-gate.expected.json /tmp/corpus-gate.expected.json
# changed one byte in the copied gate's finding-ID prefix: CR- -> CX-
node /tmp/gate-drift-probe.mjs --snapshot kasegi-shokunin b7180b0
rm -f /tmp/gate-drift-probe.mjs /tmp/corpus-gate.expected.json
```

Verbatim output (the line is long; the committed ID list begins as shown):

```text
# expect kasegi-shokunin@b7180b0 DRIFT committed_exit=1 got_exit=1 committed_ids=["CR-kasegi-shokunin-r2-1","CR-kasegi-shokunin-r2-2","CR-kasegi-shokunin-r2-3","CR-kasegi-shokunin-r4-1","CR-kasegi-shokunin-r4-2","CR-kasegi-shokunin-r4-3","CR-kasegi-shokunin-r4-4","CR-kasegi-shokunin-r4-5","CR-kasegi-shokunin-r4-6","CR-kasegi-shokunin-r4-7","CR-kasegi-shokunin-r4-8","CR-kasegi-shokunin-r4-9","CR-kasegi-shokunin-r4-10","CR-kasegi-shokunin-r4-11","CR-kasegi-shokunin-r4-12","CR-kasegi-shokunin-r4-13","CR-kasegi-shokunin-r4-14","CR-kasegi-shokunin-r4-15","CR-kasegi-shokunin-r4-16","CR-kasegi-shokunin-r4-17","CR-kasegi-shokunin-r4-18","CR-kasegi-shokunin-r4-19","CR-kasegi-shokunin-r4-20","CR-kasegi-shokunin-r4-21","CR-kasegi-shokunin-r4-22","CR-kasegi-shokunin-…
# process-exit 3 (failed)
```

The shell exit was `3`. The copy and its copied expected fixture were deleted; the committed gate was not modified.

## 2. D-133 re-test at kagi revision `2486643`

Revision/tree identity: `kagi-shokunin` landed revision `2486643`; the `--all` measurement observed dirty count 12 (`# summary kagi-shokunin rev=2486643 dirty=12 ...`). `kagi-shokunin:SHONEN.md:9` is the box-3 line:

```text
- [x] Instructions executable by an agent without oral context
```

The registry in `kagi-shokunin:SKILL.md` names these gates (lines 31–45): `bash corpus/op-ref-probe.sh`, `bash corpus/surface-census.sh`, `bash corpus/drift-pins.sh`, `bash corpus/claim-ledger.sh verify`, `bash corpus/claim-ledger.sh citations`, and `corpus/transcript-scan.sh` (line 43).

Before running, I inspected each script with the required sweep:

```text
grep -nE '>|tee|rm |git (add|commit|checkout|restore)|mv |cp ' corpus/<script>.sh
```

The sweep found writes, but they are to temporary scratch paths or cleanup paths, not outside `/tmp`/the script's temporary directory. Examples: `kagi-shokunin:corpus/transcript-scan.sh:266` `SNAP=$(mktemp -d); trap 'rm -rf "$SNAP"' EXIT`; `kagi-shokunin:corpus/surface-census.sh:698` `trap 'rm -rf "$SELFTEST_R"' EXIT`; and `kagi-shokunin:corpus/claim-ledger.sh:134` `cleanup_tmp() { [[ -n ${STAMP_TMP:-} ]] && rm -f -- "$STAMP_TMP"; return 0; }`. No refusal was required; no script showed a write to the kagi checkout or a git mutation command.

Executed commands and exact observed verdict lines:

```text
bash corpus/claim-ledger.sh verify
FAIL R13-02 reason=verdict-not-final exit=0
FAIL R14-01 reason=verdict-not-final exit=0
FAIL R13-03 reason=exit-mismatch exit=1 want=0
CLAIM_LEDGER: FAIL (claims=23 failed=3 stamped=48 stale=7 missing=0 unresolved_ids=0 labeled_ids=17)
exit=1

bash corpus/claim-ledger.sh citations
exit=0

bash corpus/transcript-scan.sh
TRANSCRIPT_SCAN: HITS=2 (cells=888 patterns=32+5 warns=2 schema-absent=0) db=/home/vgpnk/.local/state/the-janitor/xdg-data/opencode/opencode.db
exit=1
```

The D-133 contradiction **persists** at `2486643`: the box-3 `[x]` claim remains contradicted by `claim-ledger.sh verify` exit 1 and `transcript-scan.sh` exit 1. `citations` cleared at this revision (exit 0), but that does not clear the claim-ledger and transcript failures. The previously published `4391b3b`/`4b8c018` evidence therefore was not cleared by the landed revision.

## 3. `--round 10` teeth

Command 1: `node .ufo/waves/round-9/corpus-gate.mjs --all --round 10 | grep -E 'r10|# summary'` (pipeline exit was 1 because the gate's process exit was 1).

Verbatim r10 findings:

```text
CR-kasegi-shokunin-r10-1: no corpus/lessons/round-10-aggregator-*.md — the round-10 review duty has no emitted lesson (CORPUS.md:21)
CR-kengaku-shokunin-r10-1: no corpus/lessons/round-10-aggregator-*.md — the round-10 review duty has no emitted lesson (CORPUS.md:21)
CR-kake-shokunin-r10-1: no corpus/lessons/round-10-aggregator-*.md — the round-10 review duty has no emitted lesson (CORPUS.md:21)
CR-kumitate-shokunin-r10-1: no corpus/lessons/round-10-aggregator-*.md — the round-10 review duty has no emitted lesson (CORPUS.md:21)
CR-kotoba-shokunin-r10-1: no corpus/lessons/round-10-aggregator-*.md — the round-10 review duty has no emitted lesson (CORPUS.md:21)
CR-kagi-shokunin-r10-1: no corpus/lessons/round-10-aggregator-*.md — the round-10 review duty has no emitted lesson (CORPUS.md:21)
```

Round-10 summaries (verbatim):

```text
# summary kasegi-shokunin rev=b021dc9 dirty=1 exit=1 findings=56 rules=r2,r4,r8,r10
# summary kengaku-shokunin rev=e171cdf dirty=4 exit=1 findings=30 rules=r4,r8,r10,shonen
# summary kake-shokunin rev=88a4f4e dirty=0 exit=1 findings=37 rules=r4,r8,r10
# summary kumitate-shokunin rev=637d181 dirty=7 exit=1 findings=46 rules=r2,r4,r8,r10
# summary kotoba-shokunin rev=0f658ff dirty=11 exit=1 findings=83 rules=r4,r8,r10,shonen
# summary kagi-shokunin rev=2486643 dirty=12 exit=1 findings=59 rules=r2,r4,r8,r10,shonen
```

Command 2: `node .ufo/waves/round-9/corpus-gate.mjs --all --round 9 | grep -E 'r10|# summary'` (pipeline exit was 1).

Round-9 summaries (verbatim):

```text
# summary kasegi-shokunin rev=b021dc9 dirty=1 exit=1 findings=55 rules=r2,r4,r8
# summary kengaku-shokunin rev=e171cdf dirty=4 exit=1 findings=29 rules=r4,r8,shonen
# summary kake-shokunin rev=88a4f4e dirty=0 exit=1 findings=36 rules=r4,r8
# summary kumitate-shokunin rev=637d181 dirty=7 exit=1 findings=45 rules=r2,r4,r8
# summary kotoba-shokunin rev=0f658ff dirty=11 exit=1 findings=82 rules=r4,r8,shonen
# summary kagi-shokunin rev=2486643 dirty=12 exit=1 findings=58 rules=r2,r4,r8,shonen
```

Finding-count delta (`round 10 - round 9`), by measured tree/revision: kasegi `+1` (56−55), kengaku `+1` (30−29), kake `+1` (37−36), kumitate `+1` (46−45), kotoba `+1` (83−82), kagi `+1` (59−58). The exact `CR-<repo>-r10-1` text is the six identical-shape lines quoted above, with the repo name substituted.

## What broke

- D-133's published box-3 `[x]` claim still breaks at kagi revision `2486643`: `CLAIM_LEDGER: FAIL ... failed=3` and `TRANSCRIPT_SCAN: HITS=2`, both with exit 1.
- The round-10 teeth are firing for all six measured live child trees: each lacks `corpus/lessons/round-10-aggregator-*.md`, adding exactly one finding per repo relative to round 9.
- No frozen snapshot drift occurred; all eight frozen expectations matched. The throwaway mutated-gate probe correctly produced DRIFT and exit 3.

## Mid-round scope change

The six-repo tables and deltas above are explicitly scoped to the six repos rostered at the
measurement cutoff. During the wave, `kama-shokunin/` was minted by `2d19a64` and reached
`9cee9fc`. The L1 command `node .ufo/waves/round-9/corpus-gate.mjs --repo kama-shokunin --round 10`
returned exit 1 with 12 findings (`r2 2, r4 7, r7 1, r8 1, r10 1`), `dirty=9 provisional=1`.
Because `corpus/knowledge/` and `corpus/lessons/` are untracked at `9cee9fc`, no committed
snapshot can re-derive that verdict. Its `r7-1` is the literal phantom index row
`README.md:18` naming absent `lessons/round-1.md`.

The main-tree scope also changed: `git ls-files kama-shokunin | wc -l` returned 0, and
`MANIFEST.json` rounds became 48. These facts do not alter the frozen eight-key probe set or
the six-rostered-repo deltas reported above.

For attribution context, the command
`git log --diff-filter=A --format='%h %an' -1 -- .ufo/waves/round-10/CONTEXT.md` returned
`fcefcf5 protocol-shokunin`. The separate command
`git log --diff-filter=A --format='%h %aI %an' -1 -- .ufo/waves/round-9/corpus-gate.mjs`
returned `6415a9b 2026-09-28T22:29:46-03:00 aggregator-shokunin`; therefore the claim that
the round-9 gate was uncommitted is false. `git ls-tree -r a2cac72 --name-only
.ufo/waves/round-9 | wc -l` returned 25.
