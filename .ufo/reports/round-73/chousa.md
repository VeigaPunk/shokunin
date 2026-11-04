# chousa — round 73, attempt 1

## Work performed

Declared claims: **C1 operability** (lowest scored non-retired axis, historical 3/10): complete the direct research-gate battery and full preflight on the returned Linux host. **C2 calibration**: correct the two routed round-72 record defects append-only, measured by the frozen seven-check counter. **C1 met its completing predicate; C2 failed its frozen counter. Round not admitted.**

- Freeze `a0f094c272dcb09f1bf79e2c9057d7ea20b7ac7b`, base `f748abbb6bf58388e732facd4ecec5612419c457`: claims, controls, sizing receipt, counter and planned section. See `corpus/evidence/round73/claims.md`.
- Executed the actual end-to-end instrument task, sequentially: direct battery **PASS (275 cases, 0 skipped), rc 0**, 80 s; full preflight **8/8, FAILED=none ENV=none SKIPPED=none, rc 0**, 92 s. Both receipts name measured freeze revision and instrument digests: `corpus/evidence/round73/controls/{battery-r73,preflight-r73}.txt`. No research-gate/preflight implementation bytes changed. This is host-qualified completion evidence, not a new implementation capability or retroactive approval of the Windows runs.
- Corrected V72-1/V72-2 in LOG, SCORECARD and the round-72 lesson. Empirical harness demonstrates the missing-file grep survives and the unguarded assignment exits 2: `controls/v72-killline-harness.{sh,txt}`, PASS 8/8 twice, byte-identical outputs.
- One validated v1 wave, **11 seats**: 2 scout, 1 connector, 3 executor, 1 scribe, 1 revenger, 1 reviewer, 1 critic, 1 mutation-tester. Attack share 3/11; one connector; L1 holds canonical planner seat. No residual or replacement. Parent delivered **WAVE-DONE**, all 11 settled, no dead seats reported: `.ufo/waves/round-73/w1-results.json`. No model overrides passed; roles used host routing. Results do not expose actual answering models.
- Attacks found a real frozen-counter loader error: numstat additions read as deletions, so compliant append fails 6/7 while deletion can pass C2-6. Pure selftest 7/7 bypasses the loader. Other limits: substring `:84350` survivor, inverted-role/denial text, mutable local diff attributes, fabricated C1 receipts satisfying all three greps. Evidence: wave `R73M01/mutations.txt`, `R73C01/receipts.txt`, `R73R01/review.md`. Frozen counter unchanged; no forged receipt substituted for actual execution.

## Landed changes

Final pushed lane hash **`4b76c7c2892bee44ee153f79a75685da9324ed97`**; `git ls-remote origin refs/heads/master` printed that exact hash before this report.

- Freeze: `a0f094c272dcb09f1bf79e2c9057d7ea20b7ac7b`.
- Measured runs, append-only corrections, S180/S181, lesson, index and QUALITY 132–133: `5aec90775fc7cc1fe9ad442e0d5491731323eec1`.
- Settled wave artifacts, final counting receipts, empirical harness, loader-failure evidence and misroot recovery: `4b76c7c2892bee44ee153f79a75685da9324ed97`.

All tied to `LOG.md` headings **Round 72 correction entry** and **Round 73 — host remeasurement and routed corrections**. Historical claims/counter/receipts retained; no numeric axis-score delta or capability row. New counter registered as frozen/known invalid in `SKILL.md`.

**Erratum to round-72 report:** its lines 20/54 incorrectly attribute termination to the missing-file grep: `research-gate.sh:8426` is errexit-exempt in `&&`; the unguarded assignment at `:8435` inherits pin rc=2 and exits. Its line 21's “verdicts tree” attribution is superseded: after-count receipt names landing `7f7ea19a945e0998f009f82b9c651cb08aec1c12` (SCORECARD count 2), whereas verdicts tree `6dd6c82405989083f16e101d6573656d39211879` has 3 because its verdict row adds a quotation. Original report/receipt bytes and r72 honest-stop ruling remain untouched. S180 grounds this correction.

## Before → after measurements

**C1 improved on its frozen completion predicate**, actual gate PASS disclosed. Base control: r72 anchored verdict count 0 and no r72 completing preflight. Fresh runs measured at freeze; counts re-derived at landing `5aec90775fc7cc1fe9ad442e0d5491731323eec1` in `controls/after-c1-r73.txt`:

```sh
grep -c '^RESEARCH_GATE_SELFTEST:' corpus/evidence/round73/controls/battery-r73.txt
# 1, exit 0; actual verdict PASS (275 cases, 0 skipped), SELFTEST_RC=0
grep -c 'SKIPPED=none' corpus/evidence/round73/controls/preflight-r73.txt
# 1, exit 0; PREFLIGHT=8/8 FAILED=none ENV=none SKIPPED=none, PREFLIGHT_RC=0
grep -c '^PREFLIGHT=' corpus/evidence/round73/controls/preflight-r73.txt
# 1, exit 0
```

**C2 not verified / honest-stop:** base 2/7 → landing 6/7, exit 1, target 7/7 unmet. The factual corrections exist but the frozen loader incorrectly treats their added lines as deletions:

```sh
python3 -B corpus/evidence/round73/c2-count.py --lane . --rev 5aec90775fc7cc1fe9ad442e0d5491731323eec1 --base f748abbb6bf58388e732facd4ecec5612419c457
# C2=FAIL checks=6/7, exit 1
```

`controls/after-c2-r73.txt` also records independent `git diff --numstat BASE REV -- LOG.md SCORECARD.md corpus/lessons/round-72.md`: additions/deletions 11/0, 21/0, 6/0. That evidence does not replace the failed frozen predicate. Tools, frozen claims/counter and r72 evidence bytes are unchanged at the measured landing; see `after-c1-r73.txt`.

Reviewer caveats retained in the lesson: the 1.79 s sizing observation was not captured in the committed probe receipt and is withdrawn as receipt-rederivable evidence; that probe omitted revision/digest. The decisive completed-run receipts do include both. S180/S181 and wave artifacts were prospective at freeze and landed later. “Carried unchanged” means semantic predicate identity, not byte identity. Swarm/remaining protocol loading occurred late rather than in prescribed order; disclosed, not silently passed.

## Sources & frontier

Command at both ends:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa
```

Before output (`.ufo/waves/round-73/census-start.txt`):

```text
chousa W04 S051 duplicate url www.w3.org/TR/2017/REC-html52-20171214/syntax.html across scopes
chousa W04 S053 duplicate url docs.python.org/3/library/socket.html across scopes
chousa W04 S073 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa W04 S074 duplicate url docs.python.org/3/library/hashlib.html across scopes
chousa W04 S075 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa ok /home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
census_rc=0
```

After output (`.ufo/waves/round-73/census-end.txt`):

```text
chousa W04 S051 duplicate url www.w3.org/TR/2017/REC-html52-20171214/syntax.html across scopes
chousa W04 S053 duplicate url docs.python.org/3/library/socket.html across scopes
chousa W04 S073 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa W04 S074 duplicate url docs.python.org/3/library/hashlib.html across scopes
chousa W04 S075 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa ok /home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
census_rc=0
```

Rows **179→181**: added B=1 (S180 mined verifier record), C=1 (S181 rejected tree attribution); A unchanged. Status totals mined 146→147, rejected 14→15, queued unchanged 19. Row-count command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`. No held status/recheck/used-by cell changed. `corpus/lessons/round-73.md` Gate records access date, source paths, located ≤25-word quotes, rejection reason/flip. C2 cites S180. Mistakes include symptom/kill attribution, measurement-tree mismatch, loader defect, token-only forgeries and misroot.

Assimilation: none. No package adoption, new knowledge entry or frontier coverage-map advance claimed; considerthese/ is unchanged. No external live-target fetch made. Connector reports no overlapping sibling claim to this battery in its bounded scan; host/tooling findings are not absorbed as generic OS expertise.

Misroot sweep: recovered own seat `ns-arm-r73s02.txt` byte-exact into the lane's same relative path, verified `cmp` exit 0, then removed only the fleet copy. Pre-existing unrelated `after` and orchestrator `.scratch/*` left untouched. Round scratch `/fast/scratch/hyaku/chousa-r73` removed after landing. No tool installs/updates. Old L0 fetch-scope, historical Windows flock/load, SHONEN/non-author entailment requests remain unresolved; Linux capability is not an answer for the old host. No new L0 question required.

## Trend verdicts

- **expansion: unchanged** — no new province surface, knowledge entry or capability row.
- **quality: improved** — fresh direct battery PASS 275/275 and full preflight 8/8 complete where the prior host receipts did not; new invalid counter explicitly marked, never admitted as sound.
- **discernment: unchanged** — mistakes and new criteria recorded, but lane-dispatched reviewers are not an outside admit/reject verifier.

Other axes depth/freshness/coverage/adjacency unchanged; calibration unprovable on the frozen counter. No numeric expertise score changed. Admission remains **not admitted**, because C2 did not meet its frozen target.

Stale-lane: respawn-per-round; this chousa mission progressed through committed work and completed measurements; no other mission of this lane is open.

## SHONEN

- [~] Decision tables/error patterns/checklists with sources: `SKILL.md:13-77`, Gates registry; lane assertion, no non-author promotion verifier.
- [~] End-to-end task executed/logged: `LOG.md` Round 73; `corpus/evidence/round73/controls/battery-r73.txt` and `preflight-r73.txt`.
- [~] Executable without oral context: actual battery PASS 275 cases and full preflight 8/8 receipts; counter limitations explicitly registered.
- [~] No cross-domain bleed: `PROVINCE.md`; wave `R73S03.md` sibling-overlap scan; no sibling writes.
