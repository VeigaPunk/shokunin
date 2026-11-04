# mado — round 68 report

Lane: mado (`mado-shokunin`). Round 68, attempt 1, hyaku run 15. Date 2026-11-03.
Base (pre-r68 tip): `510100c81e6cf63fec6be380c2f2f9c670f32cbc`.
Freeze: `e0727cda15621766c35dcf8b70c211b6531aab45` (`claims-declaration-r68.md` +
`controls/c2-controls.json`).
Measured content (final, after the critic-driven counter fixes):
`180e5b2f55e2c4388f3496ace7574f4288af1450` (pre-fix content `379e97f884a6cf7ed3ac96068b0165d63495524f`).
Record landing: `67b47df401927053cf47a287377985806961f762`; closure fixes `180e5b2f`.
Lane tip (cited at filing): `80c6d7aa350f8c66044f002753f6434632446fb0`.

## Work performed

The round declares two claims on distinct axes, both frozen before any candidate data.

- **C1 — calibration: the control harness kills its own forged kill credit.** The r67 control
  harness credits `killed` from a decision body its hermetic selftest never runs, so a forced
  `mr_killed`/`mz_killed`/`killed` keeps a green selftest (round-67 outside spot-check routed
  defect 3). The round lands a successor harness whose `--selftest` drives the real `measure()`
  body with scripted children, plus the counter that scores three frozen forced-credit recipes
  against it and against the pinned r67 harness.
- **C2 — operability: the standing gates read git objects only through a guarded environment.**
  Twelve of the thirteen `quality/check-*.py` object readers build or inherit a git environment
  without `GIT_NO_REPLACE_OBJECTS` at the base. The round repairs every one and lands the census
  gate that counts the population, with an eleven-case classifier control set.

Work items, each with its evidence pointer:

- Pre-freeze baseline and frozen controls: counters `c1-r68-selfmutants.py`,
  `c2-r68-reader-guard.py`, the eleven-case `controls/c2-controls.json`
  (sha256 `b7a1c939…faf6a91`), the round-start census and the baseline receipt — landed at
  `2ca2bec39c42770a3176989f013e8c1cbbdb7df3`
  (`.ufo/waves/round-68/control-baseline-r68.txt`).
- Freeze declaration with predicates, recipes, kill rules and limits — `e0727cda`.
- Successor harness `quality/counters/c1-r68-landing-controls.py` (52/52 selftest) and the wave
  dispatch evidence (spec, dispatch, ready) — `40d2bef8`.
- Counter defect 1, seat-reported: the declared C2 command passed `--scratch-root`, which the
  counter did not accept (exit 2). Fixed; red-before and after receipts in
  `.ufo/waves/round-68/c2-command-erratum-r68.txt` — `2a39e741`.
- Counter defect 2, reviewer-reported (RevC2 finding 1): the C2 verdict did not enforce the frozen
  `population=20` / `readers=13`, so deleting every quoted object-read verb from one gate scored
  `TARGET_MET`. Fixed with `verdict_met()` and five denominator assertions; guard detection now
  also honours the `update()` keyword and annotated bindings the declaration names. Receipt
  `.ufo/waves/round-68/c2-denominator-erratum-r68.txt` — `686d6345`.
- Twelve gate repairs, drafts from four executor seats (`w1/R68ExecGate1.md`, `R68ExecGate2.md`,
  `R68ExecGate3.md`, `R68ExecHazard.md`): anchor-cover, axis-scores, control-receipts,
  deliverables, evidence-pointers, freeze-order, index, index-rows, landed-contract,
  round-outcome-first, session-material, wave-done. Diffs are guard-only; behavior pairs in the
  seat reports and in `w1/R68RevC2.md` — `425d4b2f`.
- Knowledge entry `corpus/knowledge/gate-git-read-guards-r68.md`, lesson
  `corpus/lessons/round-68.md`, SOURCES row S437, README index row — `47819d79`; eight evidence
  rows added after criterion 107 read `rows=0` on the first landing (`379e97f8`).
- Ledger rows for the three new instruments and the S436 `used-by` back-reference (the used-by
  counter caught the missing pair before landing) — `18d692f3`.
- Default citation-scope receipt for the standing instrument — `1df69fc8`.
- Landing block, mistakes M68-3/M68-4, SCORECARD round-68 section (with a fresh axis
  publication) and the LOG entry — `67b47df4`; mutation-battery residuals appended — `ff255b7f`.
- Attack and screen seats: C1 review (`w1/R68RevC1.md`: sound as bounded; survivors named), C2
  review (`w1/R68RevC2.md`: two counter defects + a false-positive table), mutation battery
  (`w1/R68MutBattery.md`: kill matrices for both counters and the harness recipes), connector
  (`w1/R68ConnSiblings.md`: sibling prior art, assimilation screen, and the guard-dominance
  hazard), source scout (`w1/R68ScoutSources.md`: three byte-identical fetches, tag pin, 12/12
  citation audit).
- Auxiliary probes outside both denominators: the repaired `check-axis-scores.py` reads
  `original bytes` under a planted `refs/replace` while its committed base bytes read
  `forged bytes` (`R68ExecHazard.md`); a guard-dominance variant built as
  `dict(os.environ, GIT_NO_REPLACE_OBJECTS="1")` filtered by `GIT_*` reads forged bytes while the
  census still classifies it guarded (`.ufo/waves/round-68/aux-dominance-r68.txt`).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| Two counters, frozen control set, baseline receipt and round-start census | LOG round-68 bullet 1 and "Instruments" | `2ca2bec3` |
| Frozen declaration (claims, predicates, recipes, kill rules, limits) | LOG round-68 bullet 1 ("Claims frozen at") | `e0727cda` |
| Successor harness + wave spec/dispatch/ready evidence | LOG round-68 "Instruments" bullet | `40d2bef8` |
| C2 counter accepts the declared `--scratch-root` | LOG round-68 "two counter defects" bullet | `2a39e741` |
| C2 verdict enforces the frozen denominator; guard shapes match the declaration | LOG round-68 "two counter defects" bullet | `686d6345` |
| Twelve gates guard their git reads; SKILL r68 gate rows; PROVINCE instrument paragraph; QUALITY 110 | LOG round-68 "Instruments" bullet | `425d4b2f` |
| Knowledge entry, lesson, S437 row, README index row | LOG round-68 "Knowledge" bullet | `47819d79` |
| Entry evidence rows (criterion 107) | LOG round-68 "Knowledge" bullet | `379e97f8` |
| Tool-ledger rows for the three instruments; S436 `used-by` change | LOG round-68 "Knowledge" bullet (cell change) | `18d692f3` |
| Round-68 citation scope for the standing landing instrument | LOG round-68 "Measured at" bullet | `1df69fc8` |
| Landing block, mistakes M68-1..M68-5, SCORECARD section + axis publication, LOG entry | this entry | `67b47df4` |
| Mutation-battery counter-wiring residuals in the lesson | LOG round-68 "Disclosed" bullet | `ff255b7f` |
| Wave settlement, critic report, misroot/diff-scope/chronology receipts | LOG round-68 closure addendum | `049c2e0c`, `b21f2742`, `a4cb56fe` |
| Critic-driven counter fixes (M68-6), declaration erratum, mistake renumbering, closure records, final re-measurement + wave receipt | LOG round-68 closure addendum | `180e5b2f`, `80c6d7aa` |

Every change above is read-only lane work: no desktop probe, no compositor/socket/service write,
no package transaction, no `MANIFEST.json` edit, no sibling-lane write.

## Before → after measurements

Both commands are run from the lane root; `DIR` is caller scratch.

**C1 — calibration.** `python3 quality/counters/c1-r68-selfmutants.py --repo . --rev REV --base-rev
510100c81e6cf63fec6be380c2f2f9c670f32cbc --scratch-root DIR`

- Before, at base `510100c8`: `MADO_R68_SELFMUTANTS: selftest=absent killed=0/3 applied=0/3
  base=0/3 verdict=TARGET_MISSED` rc 1 — and with the same three recipes applied to the r67
  harness that exists there, all three survive its green 47/47 selftest
  (`MADO_R68_BASE_CONTROL survivors=S1,S2,S3 killed=0/3 applied=3`).
- After, at measured content `180e5b2f` (and identically at the pre-fix content `379e97f8`):
  `selftest=0 killed=3/3 applied=3/3 base=0/3 verdict=TARGET_MET` rc 0; candidate harness sha256
  `25470bc4…f5527`, selftest 52/52; each mutant's own selftest exits nonzero (51/52, 51/52,
  50/52); the counter's own selftest 27/27.
- Bounded score `10 × killed / 3`: 0.0000 → 10.0000. Receipt:
  `.ufo/waves/round-68/measurement-final-r68.txt`.

**C2 — operability.** `python3 quality/counters/c2-r68-reader-guard.py --repo . --rev REV
--controls .ufo/waves/round-68/controls/c2-controls.json --scratch-root DIR`

- Before, at base `510100c8`: `population=20 readers=13 guarded=1 unguarded=12 controls=11/11
  verdict=TARGET_MISSED` rc 1 (only `check-tool-ledger.py` guarded).
- After, at measured content `180e5b2f` (and identically at `379e97f8`): `population=20
  readers=13 guarded=13 unguarded=0 controls=11/11 verdict=TARGET_MET` rc 0; the counter's own
  selftest 26/26, including the frozen control count and the emitted-line check.
- Bounded score `10 × guarded / readers`: 0.7692 → 10.0000. Receipt: same file; the frozen
  classification cases and the population/reader constants are part of the target.

Both counters re-ran green at the record landing
`67b47df401927053cf47a287377985806961f762` (`.ufo/waves/round-68/record-landing-r68.txt`) and again
at the post-fix content `180e5b2f` (`.ufo/waves/round-68/measurement-final-r68.txt`), where the
standing instrument reads `MADO_LANDING_COUNTERS: GREEN` and `quality/check-axis-scores.py`
reports `checked=3 mismatched=0`.

## Sources & frontier

Census command (both ends; exit 0 at both):
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`

- Rows before: **373** (`census-start-r68.txt`, committed `2ca2bec3`). Rows after: **374**
  (`census-end-r68.txt`, committed at `049c2e0c`). Histogram shift: tier A
  359 → 360; B 7; C 7 unchanged; malformed 0 both ends.
- Rows added: **1**, tier **A** — `S437`, git v2.56.0 `Documentation/git-cat-file.adoc`
  (raw.githubusercontent.com/git/git/v2.56.0/Documentation/git-cat-file.adoc), kind `docs`,
  scope "mado lane tooling: the git object-read contract the round-68 C2 reader census keys on",
  anchor at the tag with line locators `6,21-22,27-28,40-41,44-45,50-51,55,198-199,295-296,303-304`,
  opened 2026-11-03, recheck 90d, status `mined`. Opened three times this round byte-identically
  (lane L1, scribe, scout): sha256 `6c32dbda…a95b2`, 16099 B, tag object `24785443…`,
  peeled `a0189536…`, host `git version 2.56.0`.
- Rows touched old→new: **1 cell** — `S436` `used-by` old `corpus/lessons/round-67.md,
  corpus/knowledge/replace-ref-citation-boundaries-r67.md` → new with
  `corpus/knowledge/gate-git-read-guards-r68.md` appended (logged in the lesson's Gate). No row's
  `status` or `recheck` cell changed.
- Frontier rows advanced: **none** — the round adds no PROVINCE frontier move and no desktop
  knowledge; the new entry is lane-tooling scope and its Scope section says so. The sourced claim
  is C2 (its evidence cites S437); C1 is not sourced.
- Assimilation: **none**. The connector screened `/home/vgpnk/Projects/shokuknow/merge/mado/`
  (147 staged rows, 94/147 id collisions, no theme bearing on C1/C2) and
  `considerthese/2026-10-28.md` (the remaining proposal — the live-tool table — is not
  claim-shaped for this round); no sibling theme was adopted, no campaign tool was run in the
  source repo.

## Trend verdicts

- **expansion: improved (bounded)** — one admitted knowledge entry on ground the coverage map did
  not hold (the lane's gate git-read surface), its `source:` citing the mined `S437`, with its
  README index row landing in the same commit (`git diff --numstat 47819d79^ 47819d79 --
  corpus/knowledge corpus/README.md corpus/SOURCES.md` → entry + row + index row). No desktop or
  PROVINCE frontier move is claimed.
- **quality: improved** — twelve standing gates hardened with behavior identity re-run on the lane
  (base and landed bytes produce identical output and exit status on the sampled runs); a harness
  whose selftest now exercises its own decision body (0/3 → 3/3 kills); two counter defects fixed
  with red-before receipts; the axis publication stale since round 56 re-derived (`checked=3
  mismatched=0`). No admitted entry was found false or stale and left unmarked; one existing
  source cell (`S436` `used-by`) was completed as the back-reference rule requires.
- **discernment: unchanged** — the outside non-author spot-check is the closure's, not this
  report's; QUALITY 110 is grounded in the lane's own caught defects (M68-1..4) and its own attack
  seats, so no outside disagreement is claimed as learned. The round states the boundary: the four
  attack seats found two real counter defects before landing, and the survivors they name (C1
  multi-point forgeries; C2 value-position over-inclusion, guard dominance, counter-wiring
  mutants) are disclosed rather than smoothed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the r68
  gate table and its two rows in `SKILL.md` § Round 68; outside-lane verifier independence is not
  established by this report.
- [~] At least one end-to-end domain task executed and logged in LOG.md — historical round 3
  (`corpus/knowledge/config-health-report-r3.md`); round 68 ran no desktop task (lane-instrument
  scope) and claims none.
- [~] Instructions executable by an agent without oral context — the r68 gate rows and the lesson
  carry the commands; the executed seat reports are the lane's own, not outside-lane proof.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round's instruments are named in
  `PROVINCE.md` § Round-68 refinement; the boundary is asserted by the lane, not re-verified by an
  outside reviewer this round.

## Critic blockers and dispositions

`R68CriticClaims` (383-line report, `w1/R68CriticClaims.md`) filed seven blockers after the first
landing; each is disposed of in `SCORECARD.md` § "Closure corrections (round 68)" and in the
lesson's closure section, and the claim predicates were not changed.

| blocker | finding | disposition |
|---|---|---|
| B1 | the C2 verdict accepted a truncated control set (`controls=10/10 … TARGET_MET`) | fixed (M68-6): `verdict_met()` requires `controls_total == 11`; the truncated-set run prints `TARGET_MISSED rc=1`; selftest 26/26 |
| B2 | the declaration's axis posture cites `78/78`/`108/108` where the receipt reads `79/79`/`110/110`, and `N=3` is not in `SCORECARD.md` § Saturation | append-only erratum `.ufo/waves/round-68/axis-posture-erratum-r68.txt` (declaration not edited); conclusion re-derived |
| B3 | two lesson rows shared `M68-3` | renumbered before closure: M68-3 sweep, M68-4 scratch-root, M68-5 denominator, M68-6 control count |
| B4 | C1 counter docstring said `recipe=none` where the instrument prints `applicable=no` | docstring corrected to the emitted token |
| B5 | `CONTRACT_RE` was never checked on the emitted line | both `measure()` bodies `fullmatch` the assembled line and fail closed (rc 2) |
| B6 | an uncalled dead guard satisfies the census | declared limit restated (erratum §2, entry §5); the twelve repairs are wired, one gate has a runtime hazard receipt, eleven have behaviour-identity runs |
| B7 | C1 was already `TARGET_MET` at the harness cutover, 8 s after dispatch | by design: the scored harness is the round's own instrument; the freeze precedes the registry and the harness, the Before state is the base rev, and no seat is credited with building it |

`R68RevC1` graded C1 sound as bounded (survivors: dropping the `forged_credit` term, crediting
`mz_rc is None`, removing the hermeticity guard, and multi-edit forgeries). `R68RevC2` found the
denominator defect (fixed at `686d6345`) and the guard-classification false positives.
`R68MutBattery` recorded that the *counters' own wiring* is not self-tested (dropping the C1 base
leg, counting `recipe=none` as killed, forcing `unguarded = 0`); those are named residuals outside
both claims' denominators.

## Round shape, wave settlement and residuals

- Shape: **one v1 wave** under `scripts/hyaku/ufo-wave-policy.json` (band 8–16), `reportDir`
  `.ufo/waves/round-68/w1`; **12 seats** dispatched in one batch (executor 4, scribe 2, scout 1,
  connector 1, reviewer 2, critic 1, mutation-tester 1; attack share 4/12 = 33 %); no residual
  task call. The L1 holds the frozen-topology planner seat (the validator rejects `planner`).
- Seat reports landed: all twelve — `R68ExecGate1`, `R68ExecGate2`, `R68ExecGate3`,
  `R68ExecHazard`, `R68ScribeLesson`, `R68ScribeKnowledge`, `R68ScoutSources`, `R68ConnSiblings`,
  `R68RevC1`, `R68RevC2`, `R68CriticClaims`, `R68MutBattery`. Settlement at tip `80c6d7aa`:
  `WAVE wave=w1 ready=1 results=present seats=12 dispatched=12 settled=12 verdict=OK`
  (`.ufo/waves/round-68/wave-done-r68.txt`, committed `80c6d7aa`).
- Dead seats: none.
- Inherited state: the lane worktree was clean at round start (`git status --porcelain` empty,
  jj state `ahead=0`); the fleet-root sweep found no seat misroot (`?? after` and
  `?? .ufo/reports/round-71/kama.md` are not this lane's and were left untouched; `.scratch/*`
  is orchestrator-owned).
- Tool installs: none. No pacman transaction; the host-wide pause was respected.

## Stale-lane

Respawn-per-round driver; this round is the lane's only open mission (no other mado mission is
open; the lane counter is 68, campaign target 100).

## Open L0 questions

- Appended this round: `mado | round-68 | the citecheck tool invoked alone still reports
  TARGET_MET at citations=0 …` (operator-facing contract decision carried from round 67).
- Still open and operator-owned: r57–r60 questions, the L2-floor mapping, the host-recovery
  pacman pause, and the r37/r38 session-material history question.
