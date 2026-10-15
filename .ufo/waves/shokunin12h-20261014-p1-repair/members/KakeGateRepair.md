# KakeGateRepair — final handoff (wave shokunin12h-20261014-p1-repair)

Seat: `KakeGateRepair` · lane: `kake-shokunin` · steered round: 19  
Start HEAD: `b0feb30886585d8df6d4671845a2d18989ca722b`  
Before: `.ufo/waves/shokunin12h-20261014-p1-repair/evidence/kake-before.json`

Advisory only. No notes/SCORECARD/LOG/pins edits. No tests run this seat. No further peer work.

## Changed paths (current tree)

| Path | Role |
|---|---|
| `kake-shokunin/scripts/freshness-sweep.mjs` | **only** gate implementation mutation |
| `.ufo/waves/…/members/KakeGateRepair.md` | this handoff (wave members, not lane content) |

`git status` in lane: `M scripts/freshness-sweep.mjs` (plus untracked `plans/` pre-existing / not this seat).

## Authorized narrow fixes (retained)

1. **History SUSPEND fail-closed** — `pins.probeHistoryAbsent` suspends only the canonical default `~/Projects/webzites/state/probe-history.jsonl` when missing; explicit bad `KAKE_PROBE_HISTORY` → exit 2.
2. **`probeHistoryAbsent` known-set** — consumed pin, not “unused / not evaluated”.
3. **Hermetic selftest resolve** — case A present-file under owned selftest temp dir (`dir` / annotated fixture); HOME-relative `~/` + `path.relative(os.homedir(), presentFile)` cite for PATH_RE; **no** `~/.cache/kake-freshness-selftest` or other persistent HOME/global state.
4. **Selftest-only canonical rebind** — `KAKE_SELFTEST_CANONICAL_HISTORY` only when `KAKE_IN_SELFTEST=1`; `run()` forces marker **last** after env spread. Do not export.
5. Selftest cases **j/k/l** — canonical-missing SUSPEND vs explicit-bad exit 2 vs known-set.

Persisted expected values (pins) untouched. `charterGhpDeploy` left unused/informational.

## Parent commands (planned)

```bash
cd /home/vgpnk/Projects/shokunin/kake-shokunin
git rev-parse HEAD
git diff --stat -- scripts/freshness-sweep.mjs

node scripts/freshness-sweep.mjs --selftest
# expect: all pass; must NOT create ~/.cache/kake-freshness-selftest
test ! -e "$HOME/.cache/kake-freshness-selftest"

node scripts/freshness-sweep.mjs --offline
node scripts/freshness-sweep.mjs --json --offline
# footer: probeHistoryAbsent NOT under unused; §history SUSPENDED on live canonical default while webzites absent

KAKE_PROBE_HISTORY=/tmp/kake-explicit-missing-history.jsonl \
  node scripts/freshness-sweep.mjs --section=history --json
# expect: exit 2 (explicit bad; pin must not suspend)

KAKE_SELFTEST_CANONICAL_HISTORY=/tmp/not-canonical.jsonl \
  KAKE_PROBE_HISTORY=/tmp/kake-explicit-missing-history.jsonl \
  node scripts/freshness-sweep.mjs --section=history --json
# expect: exit 2 (ambient rebind ignored without KAKE_IN_SELFTEST)

node scripts/freshness-sweep.mjs
# online: expect exit 1 DRIFT PQ-2/PQ-14 while domain roots absent (named debt)
```

## Stop

GateRepair handoff complete. No further mutations from this seat.
