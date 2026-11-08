# tameshi round 99 — tally-receipt reconciliation (C1, calibration) and recorder-alias sites (C2, coverage)

Lane: `tameshi-shokunin` (verification-fixture craft). Round 99, attempt 1 (L1 `TameshiR99`).
Lane base at round start: `ff93fa16a1f65e66385b7c7f564f03b218d91ea2`. Instruments `46651051`;
freeze `ab598d03`; wave spec `27a5e49e`; records revision R
`808a43778701cf1b05762584954d435481dc6fa2` (`.ufo/waves/round-99/records-rev.txt`); landing
`7cd85a42`; ledger/late reports `e4cfbbb1`; wave results `cec42d97`; handoff markers `e209a1fe`.
**Lane tip at filing: `e209a1fe7f42d866eddeb3c7a6d50ca1e49ff897`** (`git -C tameshi-shokunin
ls-remote origin refs/heads/master` prints it; `jj-lane.sh state` → `local=e209a1fe remote=e209a1fe
ahead=0 behind=0 tracked=0 untracked=0`).

## Work performed

Declared claims (two, distinct axes, causally separable — R99C1 re-derived each with the other
tool deleted, `w1/R99C1-separability.txt`; frozen in `plans/round-99.plan.md` and
`.ufo/waves/round-99/claims.json`, amended A1-A12 from wave artifacts):

- **C1 — calibration (the lane's lowest non-retired axis, pinned 8):** `tools/tally-reconcile.py`
  counts mismatches between the lane's recorded selftest tallies (its self-assessment) and the
  receipts those lines cite (observed repo state), from blobs at one revision. Over the twelve
  round-93..98 lessons and plans it prints `TALLY_RECONCILE records=12 tallies=28 pairs=9
  matched=2 mismatched=1 unbound=6 uncited=19` exit 1, the only mismatch being the round-94
  line the round-94 closure found by eye. Mines `considerthese/2026-11-08.md` idea 1.
- **C2 — coverage:** `tools/control-assertion-audit-v2.py` widens the round-98 audit's site set
  to recorder aliases and partials (the round-98 Planned limit "blind to a driver that registers
  through a renamed recorder"); the round-98 audit stays byte-identical as the unmoved
  comparison.

Work items:

- **C1 instrument.** `tools/tally-reconcile.py` (R bytes sha256 `a1c50bb4…`, frozen `60d59bea…`).
  Records at R (bytes executed from `git show R:<tool>`): twelve-record line above, exit 1, one
  `TALLY mismatched corpus/lessons/round-94.md:66 … claimed=8/8 … observed=9/9`
  (`.ufo/evidence/round-99/records/c1-population.out`); round-94 alone `mismatched=1` exit 1
  (`records/c1-r94-only.out`); out-of-set round-93 alone `matched=1` exit 0
  (`records/c1-r93-only.out`, A5); selftest 25/25 (`records/c1-selftest.out`). Wave repairs
  before the records run: A2 (receipt lines graded whatever follows N/M — R99R1 F1), A3 (suffix
  must end the path — R99R1 F3), A4 (URL exclusion narrowed — R99R1 F2), A6 (grammar-boundary
  arms — R99M1 t4/t9), A9 (strict UTF-8, timeouts, read cache — R99SN1 F3/F4), A10 (isolation
  guard — R99SN1 F2). Discrimination: 4 of 8 new arms fail under the frozen tool
  (`records-aux/a1-a9-discrimination.out`).
- **C2 instrument.** `tools/control-assertion-audit-v2.py` (R sha256 `7527e40f…`, frozen
  `acd67ab6…`). At R: alias fixture `CONTROL_ASSERT_RECORDERS aliases=1 … names=add,record` and
  `CONTROL_ASSERT sites=4 measured=3 literal=1 unmeasured=1` exit 1 vs round-98 audit `sites=2
  measured=2 literal=0 unmeasured=0` exit 0 (`records/c2-v{2,1}-alias-driver.out`); renamed
  (`log_entry`) and chain (`rec2`) fixtures give the same v2 summary with `aliases=1`/`2`
  (A5); v1/v2 site and summary lines identical on `controls98.py`/`controls97.py`
  (`records-aux/c2-site-diff-controls{98,97}.out`, empty diff); selftest 38/38. A1 (R99R2
  S5-S8, R99E2, R99M1 v10/v11) repaired walrus, tuple, `del`, match-capture, conditional,
  alias-of-ambiguous, alias-of-partial and partial-import-alias spellings; 9 of 11 new arms fail
  under the frozen v2.
- **Receipt provenance (D3 + A11).** Every round-99 receipt carries its command line; records
  receipts carry the round-78 triple and bind: `RECEIPT_BIND: receipts=16 bound=16 corrected=0
  design=0 unbound=0`, exit 0 (`records-aux/receipt-bytes-bind.out`).
- **Routed defects (round-98 spot-check).** D1: append-only correction in SCORECARD §Round 99
  (round-94 R94-C1 verdict text restored as operative; the rewritten cell left as landed). D2:
  erratum below and in `corpus/lessons/round-99.md` §Errata. D3: above. D4: non-author R99E3
  re-ran the round-98 registry red/green pairs byte-identically and added a round-99 green pair
  (`w1/R99E3.md`). D5: carried limits restated in plan/claims.
- **Frontier.** S324 (Nuijten et al. 2016, statcheck prevalence) and S325 (statcheck FAQ) opened
  and cited by `corpus/knowledge/tally-receipt-reconciliation.md`; S326 (GRIM) rejected with
  reason and flip; mistakes M1-M6 in the lesson; QUALITY 178-179; README round-99 row;
  capability rows `tally-receipt reconciler`, `recorder-alias site audit`.
- **Wave.** One v1 wave `w1`, 13 seats: executor 3 (E1-E3), reviewer 2 (R1, R2), critic 2 (C1,
  L1 — a hypothesis probe; `labrat` is not a swarm role in the validator), mutation-tester 1,
  sentinel 1, connector 1, revenger 1, scout 1, scribe 1. Attack seats by the §8 set 8/13; by
  the policy set (reviewer, critic, mutation-tester) 5/13 = 38 %. All 13 settled with output,
  **no dead seat** (`.ufo/waves/round-99/w1-results.json`). The L1 holds the canonical planner
  seat. Round total 13 seats, no residual call. Seat outcomes in the lesson §Wave.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| instruments: reconciler, v2 audit, alias fixture, S324/S325 snapshots, census-before | Round 99 C1/C2 | `46651051` |
| freeze: plan, claims.json, 15 pre-freeze controls with command headers | Round 99 | `ab598d03` |
| wave w1 spec + validator dispatch (13 seats) | Round 99 wave line | `27a5e49e` |
| records revision R: amended instruments, amendments A1-A11, claims.json, out-of-set fixtures, records runner, wave reports | Round 99 | `808a4377` |
| landing: records receipts, lesson, knowledge entry, S324-S326, QUALITY 178-179, SCORECARD §Round 99 + capabilities + D1, LOG, README | Round 99 | `7cd85a42` |
| A12, falsification ledger, census-after, late reports SC1/S1 | Round 99 | `e4cfbbb1` |
| wave results (13/13 settled) | Round 99 wave line | `cec42d97` |
| wave handoff markers | Round 99 wave line | `e209a1fe` |

## Before → after measurements

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| C1 | at base `ff93fa16` no committed tool prints `TALLY_RECONCILE` (`git grep -c TALLY_RECONCILE ff93fa16 -- .` empty, rc 1; `records-aux/c1-before-token.out`); the round-94 and round-98 mismatches were found only by closures | `TALLY_RECONCILE records=12 tallies=28 pairs=9 matched=2 mismatched=1 unbound=6 uncited=19` exit 1, single mismatch round-94:66 8/8 vs 9/9; round-94-only exit 1; round-93-only `matched=1` exit 0; selftest 25/25 | `python3 -I tools/tally-reconcile.py --repo . --rev 808a43778701cf1b05762584954d435481dc6fa2 --record corpus/lessons/round-93.md --record plans/round-93.plan.md … --record corpus/lessons/round-98.md --record plans/round-98.plan.md` | `808a4377` (pre-freeze same line at `46651051`) |
| C2 | at base no `CONTROL_ASSERT_RECORDERS` (`git grep` rc 1); round-98 audit on the alias fixture `sites=2 measured=2 literal=0 unmeasured=0` exit 0 | v2 `sites=4 measured=3 literal=1 unmeasured=1` exit 1, `aliases=1 names=add,record`; renamed/chain fixtures same summary; v1/v2 equal on both committed drivers; selftest 38/38 | `python3 -I tools/control-assertion-audit-v2.py --repo . --rev 808a43778701cf1b05762584954d435481dc6fa2 --driver .ufo/evidence/round-99/c2/alias-driver.py` (unmoved: same with `tools/control-assertion-audit.py`) | `808a4377` |

## Sources & frontier

`SOURCES:` rows before → after: **183 → 186**, counting command
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`
→ exit 0 both runs (`.ufo/waves/round-99/census-before.txt`, `census-after.txt`). Rows added by
tier: **A 3** (S324 paper `mined`, S325 docs `mined`, S326 paper `rejected`). Rows touched
old → new: none (no in-place cell; `tools/registry-cell-immutability.py --from ff93fa16 --to
7cd85a42` → `shared=183 changed=0 removed=0 added=3`, exit 0). Frontier rows advanced: none
(F1-F11 unchanged; the new entry is calibration ground). Sourced claim: C1's knowledge entry
cites S324/S325, opened 2026-11-08 (quotes 25 / 21 + 7 words, located in the lesson `## Gate`,
re-fetched independently by R99SC1). Assimilation: none (no `merge/tameshi/` package adopted).
considerthese: `2026-11-08.md` idea 1 mined as C1.

## Trend verdicts

- **expansion: improved** — three new registry rows opened this round (two admitted and cited
  by a new knowledge entry on ground the lane did not hold — reported-figure/receipt
  reconciliation; one principled reject), census 183 → 186, exit 0.
- **quality: improved** — two new able-to-fail instruments whose receipts bind 16/16 to the bytes
  that ran; QUALITY 178-179 with receipt pointers; the wave's 12 amendments each cite an
  artifact and 13 of 19 new selftest arms fail under the frozen bytes.
- **discernment: improved** — the round's own wave falsified seven frozen sentences (ledger: 20
  rows, 10 `falsifies-wording`, each with a narrowing) and the L1 repaired or narrowed every one
  before filing; S326 rejected with reason/flip and the scout refused its own candidate (nbval).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  [lane assertion, no independent promotion verifier](reports/round-1-calibration.md#box-1)
- [~] At least one end-to-end domain task executed and logged in LOG.md
  [lane assertion, no independent promotion verifier](reports/round-1-calibration.md#box-2)
- [~] Instructions executable by an agent without oral context
  [lane assertion, input-keyed monitor only; no independent promotion verifier](.ufo/evidence/round-21/coldread/ledger.json)
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  [lane assertion, no independent promotion verifier](reports/round-1-calibration.md#box-4)

## Errata

- **Round-98 report lines 31-32 (spot-check D2).** "Selftest `18/18` (`pre-freeze/c1-audit-selftest.out`
  at the freeze; …)": the freeze receipt prints `CONTROL_ASSERT_SELFTEST: 12/12 pass`; `18/18` is the
  records receipt `records/c1-audit-selftest.out` (A5 at `3b7ae127`, R99RV1). The C1 reconciler flags
  this exact line shape (`w1/R99RV1-d2-fixture-relpaths.txt`: `mismatched … observed=12/12`, exit 1).

## Stale-lane

This is the lane's only open mission (respawn-per-round driver). Launch
`2026-11-08T19:52:55-03:00` → lane tip `e209a1fe`; 8 lane commits after the launch
(`git log --oneline ff93fa16..e209a1fe | wc -l` → 8): `progressing`, not silent. The wave spawned
at 20:03:45 and settled (WAVE-DONE) after all 13 seats filed.

## Tool installs

None this round (pacman paused and unused; no `uv`/`npx` install was needed; no seat reported an
install).

## L0 questions

None opened.

## Prefile falsification

`python3 scripts/hyaku/prefile-falsification.py --lane tameshi --round 99` →
`PREFILE-FALSIFICATION: pass claims=2 rows=20 attack_seats=8 findings=0`, exit 0
(ledger `.ufo/waves/round-99/claim-falsification.tsv`, committed at `e4cfbbb1`).
