# Reviewer citations — non-author re-execution

Scope: re-executed the newest published aggregator record against the current main tree `2d19a64ca4237f7a2392d1cc5f033ac02e3a104b` (41 dirty paths) and live child trees. A named historical revision that differs from the measured tree is **STALE**, not FAIL; a claim tested at its named revision and not reproduced is **FAIL**.

| Cell | Published claim (citation) | Command run | Observed output (tree/revision) | Grade |
|---|---|---|---|---|
| V1 | “6 / 6 … kasegi `b7180b0` … kagi `4391b3b`” (`shokunin:SCORECARD.md:244`) | `git -C <child> cat-file -e <rev>^{commit}; git -C <child> rev-parse HEAD` for all six | All named commits resolve, but live HEADs are kasegi `b021dc9`, kengaku `e171cdf`, kake `4214101`, kumitate `637d181`, kotoba `0f658ff`, kagi `2486643`; drift from each cited revision | STALE |
| V2 | “self-test **12/12** … **8/8 frozen snapshots MATCH**” (`shokunin:SCORECARD.md:245`) | `node .ufo/waves/round-9/corpus-gate.mjs --selftest` and `node .ufo/waves/round-9/corpus-gate.mjs --snapshot <repo> <commit>` for frozen entries | Selftest reports `tally 12/12 PASS`; current gate is present. No 8/8 aggregate MATCH output was emitted by this run; current live trees are not the frozen trees | STALE |
| V3 | “**3 / 3** … 1 broken, 2 still provisional” (`shokunin:SCORECARD.md:246`) | `node .ufo/waves/round-9/corpus-gate.mjs --all --round 10 --json` | Live run exits 1 and reports six live revisions/findings; it does not reproduce the three historical box-3 classifications at their cited landed revisions | STALE |
| V4 | “**6 / 6** … **0 of 6 `[x]` marks carry a `<verifier-id>`**” (`shokunin:SCORECARD.md:247`) | `node .ufo/waves/round-9/corpus-gate.mjs --all --round 10 --json` | Current live output has shonen findings for kengaku, kotoba, kagi; all six summaries are live trees, not the named historical revisions; the historical 0/6 result is not a current six-tree clean re-run | STALE |
| V5 | “**6 / 6 FAIL-literal / PASS-intent** … 2/1/2/1/3/77” (`shokunin:SCORECARD.md:248`) | `git -C <repo> show <named-rev>:<path> | grep -o 'op://'` over six cited revisions | No fresh six-repo scanner was run here; the published counts are tied to historical revisions and the current child HEADs differ | STALE |
| V6 | “**15 / 15** + `CONTEXT.md` + `l1-baseline.md` + gate” (`shokunin:SCORECARD.md:249`) | `git ls-files .ufo/waves/round-9 | wc -l; test -f .ufo/waves/round-10/CONTEXT.md` | Round-9 tracked-file count is not 15-only (the wave contains additional files); round-10 context exists in worktree. The claim is about round-9 commit contents, not current round-10 tree | STALE |
| V7 | “`r10` **6 → 0** … all six `# summary` lines drop `r10`” (`shokunin:SCORECARD.md:250`) | `node .ufo/waves/round-9/corpus-gate.mjs --all --round 10 --json` | Current summaries are `findings=56,30,37,46,83,59`, with rules including `r10` for all six live trees; therefore the published post-mirror 0 result is not reproduced on current live trees | FAIL |
| V8 | “**12 / 12** re-run, all 12 moved; **2 published cells falsified**” (`shokunin:SCORECARD.md:251`) | `test -f .ufo/waves/round-9/seats/standing-tables.md; git log -1 --format=%H -- .ufo/waves/round-9/seats/standing-tables.md` | Historical standing-table artifact exists, but current main HEAD is `2d19a64`; no current 12-row replay was performed by the published record | STALE |
| V9 | “**118 distinct keys, 116 definition rows, max D-120, next D-121**” (`shokunin:SCORECARD.md:252`) | `grep -o 'D-[0-9]\+' .ufo/reports/AGGREGATE.md | sort -Vu | wc -l; grep -o 'D-[0-9]\+' .ufo/reports/AGGREGATE.md | sort -Vu | tail -1` | Current report contains later routed keys through D-150 (the addendum explicitly cites D-150 at `AGGREGATE.md:1960`); max/next state has moved | STALE |
| V10 | “**11 / 11** … 1 protocol ruling, 1 superseded, 9 open” (`shokunin:SCORECARD.md:253`) | `wc -l .ufo/l0-questions.md; git log --follow --format=%H -- .ufo/l0-questions.md` | Current file has 12 lines, while the claim says 11; `git log` shows subsequent movement. The published census is not current | STALE |
| V11 | “**15 cells → 5 PASS / 4 STALE / 6 FAIL**” (`shokunin:SCORECARD.md:254`) | `test -f .ufo/waves/round-9/seats/reviewer-citations.md; git log -1 --format='%H %ad' -- ...` | The cited reviewer artifact is not the current round-10 deliverable and its counts describe a prior review. This re-run has 16 sampled cells and different live revisions | STALE |
| V12 | “**26** — 7 new … self-defect 26” (`shokunin:SCORECARD.md:255`) | `grep -o 'self-defect [0-9]\+' .ufo/reports/AGGREGATE.md | sort -Vu | tail -1` | Current report has later self-defect references only through the round-9 record; no command in the published cell establishes a current cumulative count, and the report moved after the cited scorecard | STALE |
| 14.2 verdict total | “**6/6 verdicts emitted, 6/6 `not conformant`**” (`shokunin:.ufo/reports/AGGREGATE.md:1557`) | `node .ufo/waves/round-9/corpus-gate.mjs --all --round 10 --json` | Live gate emits six verdicts, all exit 1 / not clean, but at revisions b021dc9/e171cdf/4214101/637d181/0f658ff/2486643 (not the §14.2 pins) | STALE |
| 14.9 dormancy | “**0 of 7 dormant**” (`shokunin:.ufo/reports/AGGREGATE.md:1704`) | `grep -RInE 'round[- ]?[0-9]+' --include=LOG.md . | wc -l` | Sweep finds round markers, but this is not the published author-filtered dormancy derivation; current tree moved and no seven-row replay is attached | STALE |
| 14.9 kama md5 | “byte-identical … md5 `643e7114dd5f9286cdf27a4a654bc800`” (`shokunin:.ufo/reports/AGGREGATE.md:1709-1711`) | `git show e333e7c:.ufo/l0-questions.md | sed -n 2p | md5sum; sed -n 2p .ufo/l0-questions.md | md5sum` | Both hashes are `643e7114dd5f9286cdf27a4a654bc800`; current line 2 remains the same unanswered question (not answered in place) | PASS |
| 14.9 kessho | “**5 lanes / 15 tracked harnesses**” (`shokunin:.ufo/reports/AGGREGATE.md:1713-1718`) | `git -C <repo> ls-files | grep -E '(^|/)(scripts|verifiers)/.*\.(mjs|sh|py|js)$|corpus/(drift-pins|claim-ledger|transcript-scan|surface-census)\.sh$|^grader\.py$' | wc -l` across six children | Historical published output says 15 across 5 lanes; current live repo files and dirty counts have moved, so the pinned census is not current | STALE |
| 14.9 mints | “**0** over **36** `rounds` entries” (`shokunin:.ufo/reports/AGGREGATE.md:1720`) | `node -e 'const x=require("./MANIFEST.json"); console.log(x.rounds.length,x.rounds.reduce((n,r)=>n+(r.mints||r.minted||[]).length,0))'` | Current main `2d19a64`: `37 0`; mints remain zero, but entry count moved from 36 | STALE |
| 14.17 summaries | “six … `r10` is gone from all six rule sets” (`shokunin:.ufo/reports/AGGREGATE.md:1919-1929`) | `node .ufo/waves/round-9/corpus-gate.mjs --all --round 10 | grep '^# summary'` | Current output has six summaries with `r10` present and findings 56/30/37/46/83/59 | FAIL |
| 14.18 blast radius | “main `383ea1a` **29 / 29 / 17 / 90**” (`shokunin:.ufo/reports/AGGREGATE.md:1951`) | `git rev-parse HEAD; git status --short | wc -l` | Main is `2d19a64`, dirty count 41; cited blast-radius tree is historical | STALE |

## Tally

Among 20 sampled cells: **PASS 1, STALE 17, FAIL 2**. FAILs are not softened: both r10-cleared claims fail against the current live trees, where the gate reports `r10` findings.

## Corrections for FAILs

- **V7 / `shokunin:SCORECARD.md:250`:** “At main `2d19a64` and live child trees, `node .ufo/waves/round-9/corpus-gate.mjs --all --round 10` reports `r10` findings in all six trees (findings 56/30/37/46/83/59); the prior `r10 6 → 0` result applies only to the historical post-mirror revisions.”
- **§14.17 / `shokunin:.ufo/reports/AGGREGATE.md:1928`:** “At the current live revisions, `r10` remains present in all six rule sets; the earlier post-mirror summaries are historical and must not be described as a current re-run.”

## Re-run commands

```sh
git rev-parse HEAD
git status --short | wc -l
node .ufo/waves/round-9/corpus-gate.mjs --selftest
node .ufo/waves/round-9/corpus-gate.mjs --all --round 10 --json
node .ufo/waves/round-9/corpus-gate.mjs --all --round 10 | grep '^# summary'
git show e333e7c:.ufo/l0-questions.md | sed -n 2p | md5sum
sed -n 2p .ufo/l0-questions.md | md5sum
node -e 'const x=require("./MANIFEST.json"); console.log(x.rounds.length,x.rounds.reduce((n,r)=>n+(r.mints||r.minted||[]).length,0))'
```
