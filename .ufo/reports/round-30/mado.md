# mado — round 30 report

Lane tip at write: `92d3c8676f4801b2ed2692cf45280796c166c88c` (pushed, `ahead=0`
via `jj-lane.sh state`). Base: `8f51071b5bc44c815eeb5da76bb7f1947994ffb8`
(round-29 closure: admitted; the r29 verifier spot-check routed the 41/43
navigation gap here). Attempt 1; no inherited uncommitted leftovers (clean
worktree at dispatch; `lane-dead-no-report mado round=30` absent from
watchdog.log — `launch mado round=30 ... attempt=1` at 03:44:14-03).

## Work performed

Declared claims (3, distinct axes, one on the lowest active scored axis):

- **C1 — coverage / admitted-note reachability** (routed defect; sourced S185):
  the two missing `corpus/README.md` index rows land
  (`workspace-rules-r27.md`, `mutation-testing-r28.md`; 41/43 → 43/43).
- **C2 — calibration / lesson-grounded admission criteria** (lowest scored
  axis: literal 0.7000, resolved-active 0.7949 at base): every active QUALITY
  criterion resolves a `lessons/` citation (31/39 → 40/40 resolved-active).
- **C3 — operability, capability acquisition** (sourced S185): the
  index-completeness gate `quality/check-index.py`, demonstrated red at base
  and green at tip.

Work items, each with an evidence pointer:

- Read the round contract files and the r29 routed queue
  (`corpus/lessons/round-29-verifier-spotcheck.md`: "Round 30: close the
  inherited coverage-index gap…").
- Re-derived the bounded sub-axes at base for the lowest-axis selection
  (registration table): calibration literal 28/40 = 0.7000 and
  resolved-active 31/39 = 0.7949, both below coverage-nav 0.9535 and
  operability 1.0 — C2 works the lowest axis.
- Wrote and froze the registration `.ufo/waves/round-30/registration.md`
  at `451e8b3c`, carrying the C2 counter `.ufo/waves/round-30/c2/count.py`,
  the C3 gate `quality/check-index.py`, controls `controls/C2K1-donothing.txt`,
  `C3K1-base-red.txt`, `C3K2-selftest.txt`, and before-receipts
  `evidence/c1-before-8f51071b.txt`, `c2-before-8f51071b.txt`,
  `census-before.txt`.
- Freeze smoke (QUALITY 49): ran all three counters at `451e8b3c` before
  data — all print real tallies (`evidence/freeze-smoke-451e8b3c.txt`).
- Data commit `446dc396`: `corpus/README.md` +2 index rows;
  `corpus/QUALITY.md` +grounding-repair section (rows 41–51 supersede
  1–5/18/19/32/38–40 verbatim with canonical citations, row 52 new);
  `corpus/SOURCES.md` +S185 (own-work, the frozen navigation fence);
  `corpus/lessons/round-30.md` (M30-1, M30-2, `## Gate`).
- Measured all three claims at `446dc396`: `evidence/c1-after-446dc396.txt`
  (`indexed=43/43`, exit 0), `evidence/c2-after-446dc396.txt`
  (resolved-active 40/40, `PRED-C2-r30 verdict=TARGET_MET`, exit 0),
  `evidence/c3-after-446dc396.txt` (base red / tip green / selftest 6/6).
- Harm watch: `MADO_SELFTEST: 460/460` exit 0; `git diff --stat 8f51071b
  master -- tools/ corpus/knowledge/ SKILL.md PROVINCE.md` empty; census
  validate exit 0 start (archived base tree) and end; no compositor/config
  mutation; misroot sweep clean (0 mado-owned files at fleet root).
- W04 disposition (criterion 17 check): the seven duplicate-URL warnings
  (S030/S042/S045/S097/S119/S120/S121) re-verified as supersession or
  distinct-scope reuse with rejected history preserved — no action
  (`corpus/lessons/round-30.md` `## Gate`).

## Landed changes

Lane commits (all pushed; `jj-lane.sh` `landed` lines):

- `451e8b3c7ee3a422bfcc0251ebbc92ace0815ce9` — round-30 freeze: registration,
  C2 counter, `quality/check-index.py`, controls, before-receipts.
- `446dc3966193c81e64896f4880a19a4bd249255b` — round-30 data: README index
  rows, QUALITY grounding rows 41–52, S185, `corpus/lessons/round-30.md`.
- `92d3c8676f4801b2ed2692cf45280796c166c88c` — round-30 records: after
  receipts, freeze smoke, census receipts, wave spec + plan, LOG entry,
  SCORECARD round-30 section.

LOG entry: `LOG.md` "## Round 30 (2026-10-24, attempt 1)". Fleet commit:
this report (below). No L0 append this round (the two answered-by-
implementation questions stay open at `.ufo/l0-questions.md:133-135`).

## Before → after measurements

- **C1 (coverage-nav)**: `REV=<rev> python3` literal fence (the SCORECARD
  "Counting command" block). Before @ `8f51071b`:
  `indexed=41/43 missing=2 dangling=0 duplicates=0 coverage=9.5349/10`,
  exit 1. After @ `446dc396`: `indexed=43/43 missing=0 dangling=0
  duplicates=0 coverage=10.0000/10`, exit 0. Control K1: the same fence at
  base stays red — do-nothing cannot reach 43/43.
- **C2 (calibration)**: `python3 -I .ufo/waves/round-30/c2/count.py REV`.
  Before @ `8f51071b` (= `controls/C2K1-donothing.txt`): literal 28/40,
  resolved-active 31/39, `UNRESOLVED criterion {1,2,3,4,5,38,39,40}`,
  `PRED-C2-r30 verdict=TARGET_MISSED` exit 1. After @ `446dc396`: literal
  40/52, resolved-active 40/40 = 1.0000, `TARGET_MET` exit 0. Superseded
  lines {1–5,18,19,20,32,38,39,40} leave both denominators (criterion
  21→20 precedent); literal and resolved reported side by side
  (criterion 22).
- **C3 (operability/capability)**: `python3 -I quality/check-index.py
  --rev REV --repo .` / `--selftest`. At base rev: `MADO_INDEX:
  indexed=41/43`, exit 1 (red — a green-at-base gate would be vacuous).
  At `446dc396`: `indexed=43/43`, exit 0. Selftest: `MADO_INDEX_SELFTEST:
  6/6 assertions passed`, exit 0 (missing/dangling/duplicate rows, symlink
  refusal, empty tree). Capability row entered SCORECARD round-30 section.

## Sources & frontier

Counting commands: `scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin mado` and the frozen manual census
(`CORPUS.md`). Before — 184 rows over the committed base tree (receipt
`.ufo/waves/round-30/evidence/census-before.txt`: extracted via
`git archive 8f51071b` into scratch, `validate` exit 0, 7 W04 warnings
unchanged). After — 185 rows at tip (`.ufo/waves/round-30/evidence/
census-end.txt`: `validate` exit 0; malformed=0; duplicate ids none;
mined used-by paths all exist).

- Rows added by tier: **A +1** (S185 — own-work, the frozen navigation
  counting command in `SCORECARD.md`; opened 2026-10-24; gate quote in
  `corpus/lessons/round-30.md` `## Gate`).
- Rows touched old→new: none (no status/recheck flips).
- Frontier rows advanced: none (no queued row mined).
- Sourced claim: C3 implements S185's row-set semantics; C1 is the repair
  S185's fence measured (registration "Sourced claim" section).
- Mistakes mined: M30-1 (ungrounded criteria — fix shown able to fail at
  the base control: `UNRESOLVED criterion 1..5,38..40`) and M30-2 (the
  index gap's two-round persistence — the sweep recorded it, no gate
  caught it); both in `corpus/lessons/round-30.md` `## Mistakes`.

## Trend verdicts

- **expansion — improved**: a new capability enters the table
  (`index-completeness gate`, demonstrated red-at-base/green-at-tip,
  `evidence/c3-after-446dc396.txt`); one own-work registry row added.
  No new `corpus/knowledge/` entry — bounded to the capability + the
  index rows.
- **quality — improved**: twelve ungrounded criteria are superseded by
  lesson-cited restatements (resolved-active 31/39 → 40/40); the index
  gap disclosed in r29 is closed rather than carried; each fix is shown
  able to fail (C2K1, C3K1 committed reds).
- **discernment — improved**: M30-1/M30-2 are honest self-mined mistakes
  with `captured-by` gaps named and fixes demonstrated; criterion 52
  grounds the record-then-claim discipline the r29 sweep already
  followed. Outside non-author spot-check of this round's gate decisions
  rides the closure pass (prepared wave not dispatched — same seat
  constraint as r29).

## SHONEN

- [~] SKILL.md real decision tables/error patterns/checklists/cited
  sources — asserted: SKILL.md byte-unchanged this round
  (`git diff 8f51071b master -- SKILL.md` empty); no SKILL work claimed.
- [~] end-to-end domain task executed and logged — asserted: LOG.md
  round-30 entry (index repair + grounding repair + gate, with receipts);
  no new live-desktop task (host pause + read-only substrate in force).
- [~] instructions executable without oral context — asserted: all three
  counters/gates ran end-to-end from committed bytes at named revisions
  with committed receipts (`evidence/c{1,2,3}-after-446dc396.txt`).
- [~] no cross-domain bleed (PROVINCE.md accurate) — asserted:
  `git diff 8f51071b master -- PROVINCE.md SKILL.md` empty;
  `quality/check-index.py` is a lane-internal gate (same class as the
  existing `quality/` checkers; no new province surface); no
  sibling/fleet writes (misroot sweep clean).

No `[x]`: every box lacks a named non-author verifier on record this round.

## Round shape, waves, seats

Shape: **three-claim repair round with a prepared v1 wave** (default
shape). Round total: **33 prepared seats, 0 dispatched, 0 dead**.

- Wave 1 (build + first falsifiers): 33 seats — executors 6, scribes 3,
  scouts 3, connector 1, reviewers 11, critics 4, mutation-testers 2,
  sentinel 1, revenger 1, simplifier 1. Spec
  `.ufo/waves/round-30/w1-spec.json`; validated under policy v1
  (`w1-plan.json`, `ufo-swarm-wave.mjs plan` exit 0, spawn=33,
  band 32–64 satisfied). Attack items: counters re-run at both revisions,
  predicate/kill-rule/controls falsification, counter + gate mutation
  testing, rubric-drift and sourced-claim circularity attacks, record
  chain and report-contract review.
- **Prepared but NOT dispatched**: this L1 seat has no swarm-dispatch
  tool on this host surface (expected, not a conformance defect — the
  orchestrator dispatches prepared waves itself between rounds; same
  constraint as r29, which the r29 spot-check recorded as status-neutral).
  The §3 planner seat is held by the L1 (orchestrator ruling); the
  bounded planning data-walk rides `ScoutAxisScores`.
- Wave 2: not prepared — wave-1 reports do not exist yet.
- Residual call: none.

Tool installs: none (pacman pause in force; no `uv tool`/binary installs
needed — python3/node/git suffice).

Open L0 questions: the two r28/r29 questions (ephemeral-input policy;
guard-pin repair path) remain open for operator overrule
(`.ufo/l0-questions.md:133-135`); no new question this round.

Stale-lane: none — respawn-per-round driver; no other mission of this
lane is open.

Honesty note: the r28 `PRED-C1-r28` record stays rejected-honest-stop;
this round's predicates are new and registered, never a retroactive pass.
C1's rows are navigation only — no new domain claim is admitted through
them. C2's resolved-active rubric is new this round (frozen in the
registration and counter docstring); the literal rubric is reported
unchanged beside it.

## Erratum — w1 wave findings and C3 gate repair (appended post-report)

After this report was filed, the orchestrator dispatched the prepared
33-seat wave; 24 reports landed (`.ufo/waves/round-30/w1/reports/`,
committed `15ddd7d64a5f30f835533818dac5b7bcc8965181`). Findings and
disposition:

- **C3 gate repaired** (`quality/check-index.py`, new blob): RevC1Fence
  S1–S6, MutC3Gate F1/M3a, RevC3Gate H1 showed the gate was a strict
  superset of the frozen fence — `^\|\s*` vs `^\| ` row grammar,
  `split()` vs `splitlines()`, non-ASCII ls-tree quoting, `--root`
  0/0 false-green on a wrong root, and a silent `master` default. All
  latent on committed bytes. Repair is fence-faithful (literal regex,
  NUL ls-tree, setup-error empty/missing knowledge, explicit `--rev`
  required); selftest 6→8. `PRED-C3-r30` re-verified at `d72243e`:
  `evidence/c3-repair-d72243e.txt` — base red, both tips green, 8/8.
- **Routed to round 31:** table-context laxity in fence AND gate
  (CritKillRules/CritPredicates — rows outside the table or in comments
  count; a fence limitation the claim prose acknowledges), C2 counter
  resolves-citation-not-grounding (empty-lesson cheat), weak kill rules,
  own-work circularity guard, gate wiring into `mado-verify.sh`
  selftest/SKILL gate-registry (RevC1Fence S7 + r30 spot-check routing).
- Seat observation, resolved: `quality/q36-successor-receipts.txt` was
  regenerated out-of-scope mid-review (ephemeral paths, no verdict moved)
  — reverted to committed bytes, same handling as r29.
- No finding affects the three claims' measured outcomes; all receipts
  reproduce. Lane tip is now `15ddd7d64a5f30f835533818dac5b7bcc8965181`.

## Erratum 2 — counter repair, gate v2, and record corrections (appended)

Lane tip at write: `a0dd664a16f90b1efe129a1ca864e873a5fb1331`
(committed/pushed via `jj-lane.sh`).

- **C2 counter repaired to the frozen rubric** (RevC2Counter S3–S6):
  `M01-M07`-style ranges now expand to all seven ids (was: endpoints
  only); `M<round>-<n>` compounds stay literal; `SUPER_RE` honors
  `<N1>-<N2>` on every list member; supersession is position-guarded
  ("later line"); `active=0` never passes. Byte-identical output at
  `8f51071b`, `446dc396`, `d72243e`, `15ddd7d` — no verdict moves.
- **C3 gate v2** (RevC1Fence post-review addendum): `%(path)` C-quoting
  under `-z` still dropped non-ASCII names; fixed with
  `core.quotepath=off` + a real-git selftest case 9. `MADO_INDEX_SELFTEST`
  is now `9/9`; all rev verdicts unchanged.
- **Record repairs**: `evidence/freeze-smoke-451e8b3c-full.txt`
  (complete 14-line C2 leg, per criterion 49's full-output rule);
  `evidence/selftest-d72243e.txt` (committed 460/460 harm watch);
  criterion row 48 regained its dropped normative accounting sentence.
  Errata noted: registration `:61` off-by-one; `controls/` path scope;
  harm-watch label said `446dc396` but measured at `d72243e`.
- **Recorded limit**: C2's rubric measures citation resolvability, not
  lesson derivation (RevRecordsChain F3, RevC2Counter S7) — the
  seed-five's M30-1 ground is legitimate under the rubric but the
  metric's name overstates it; section-scoped anchor+id conjunction is
  routed to round 31 with the fence/table-context tighten.
- 31 of 33 seat reports are in; the two stragglers land in the next
  sweep. No finding affects the three claims' measured outcomes.

## Erratum 3 — expansion verdict restated (append-only)

Lane tip at write: `274f7355366d38d6e78f641ad62472e68df4686a`.

`w1/reports/RevTrendExpansion.md` (F1/F2, adopted reading F4): the
expansion bullet's supports were overclaimed. Restated verdict:
**expansion — improved, narrow, capability-only.** The single valid
support is the admitted capability row; the SOURCES row (source growth
is not expansion, r21/r29) and C1's index rows (already booked as
r27/r28 expansions) carry no expansion weight. This is the lane's first
capability-only expansion verdict — a reading of `LEARNING.md:33`'s
observable column + `LOG.md:1447/1529` vocabulary; the strict
entries-only cell would read `unchanged` (0 new knowledge entries).
The capability row's scope is corrected in SCORECARD (new surfaces:
`--root`, refusals, `--selftest`, setup-error, exit contract — not
revision scoring, which pre-existed); evidence re-pointed to the
repaired-gate receipt. All three claims' measured outcomes stand; 32 of
33 seats reported.
