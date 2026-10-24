# mado — round 29 report

Lane tip at write: `a30b06857724a0bd2ddaa45008fec53a5da4908c` (pushed, `ahead=0` via
`jj-lane.sh state`). Base: `f652ca99c64631a72e06a7d2f6ffa1708794f65e` (round-28 closure:
rejected-honest-stop). Attempt 1 of round 29; no inherited uncommitted leftovers (the
worktree was clean at dispatch; one runner-regenerated file was reverted, see Landed
changes).

## Work performed

Declared claims (2, distinct axes, at least one on the lowest active scored axis):

- **C1 — operability** (sourced: S184): the round-28 six-leg mutation composite is
  repaired and re-frozen as a committed-bytes gate — count-v4 guard pin corrected to the
  committed bytes, leg h1 re-based per QUALITY 39 to a named committed receipt, freeze
  smoke run per QUALITY 38, standalone boolword-v5 receipts committed.
- **C2 — calibration** (lowest active scored axis): the four defects routed by the
  round-28 closure are repaired in committed records (red-before control, ephemeral-input
  policy at data time, standalone receipts, §6.6 erratum).

Work items, each with an evidence pointer:

- Read the round contract and frozen r28 records: registration
  `.ufo/waves/round-28/registration.md`, spotcheck `corpus/lessons/round-28-verifier-spotcheck.md`
  (4 routed items), lesson `corpus/lessons/round-28.md`, routed-queue analysis
  `.ufo/waves/round-28/w2/reports/RevengerNineDefects.md`.
- Wrote the r29 registration `.ufo/waves/round-29/registration.md` (routed queue quoted,
  two claims, frozen predicates, kill rule, controls, data rule, S184 sourced-claim section).
- Authored the repaired composite `.ufo/waves/round-29/c1/count.py` (two declared rule
  changes vs the frozen r28 counter: pin + h1-receipt basis; legs 2–6 verbatim) and the C2
  counter `.ufo/waves/round-29/c2/count.py` (R1–R4 over committed bytes).
- Ran the before-state composite at base: `evidence/c1-before-f652ca99.txt` — h1 FAIL
  (ephemeral), boolword FAIL (`normal=missing mutant=missing`), four legs PASS,
  `PRED-C1-r28 verdict=TARGET_MISSED` exit 1 (reproduces the r28 receipt byte-for-byte in
  the leg vector).
- Built and scored the three kill-rule controls: `controls/C1K1-r28composite.txt`
  (unrepaired r28 composite at base → TARGET_MISSED), `controls/C1K2-pinonly.txt` + variant
  `controls/C1K2-pinonly-count.py` (pin fixed, h1 ephemeral → `h1-rotation FAIL rc=2
  no-tally` → TARGET_MISSED; the same run proves the repaired pin makes the boolword leg
  print real tallies), `controls/C2K1-donothing.txt` (C2 at base → `R1..R4 FAIL` exit 1).
- Committed the freeze `aeb4f58b15840c7ee229c12b8ff0b1fe200ddcee`; smoke-ran the composite
  once at freeze per QUALITY 38 (`evidence/c1-freeze-smoke-aeb4f58b.txt` → all six legs
  PASS, TARGET_MET, exit 0). The smoke caught one cosmetic defect — the repaired counter's
  self-print label still read `c1-r28`; fixed, re-frozen `3ae437caf71a3a945285109e014d6d2a0b0d2e5b`,
  re-smoked green (`evidence/c1-freeze-smoke-3ae437ca.txt`). Both receipts committed.
- Ran the routed standalone boolword-v5 receipts: `evidence/v5-standalone-normal.txt`
  (`cases_pass=41/41 boolword_pass=2/2 verdict=TARGET_MET`, exit 0) and
  `evidence/v5-standalone-mutant.txt` (`boolword_pass=0/2 verdict=TARGET_MISSED`, exit 1);
  both carry the counter self-print lines and `HOST_SAFETY` coredumps 1338→1338.
- Repaired the §6.6 tenth record defect: append-only `§6.6 erratum (round 29)` block in
  `SCORECARD.md`'s round-27 section (the r27 sentence "the tool's docstring and the
  knowledge entry cite them [S178–S182]" overclaims; the S### citation lives in
  `corpus/knowledge/workspace-rules-r27.md` frontmatter; the docstring cites upstream
  filenames). Fix shown able to fail: `CHECK R4 FAIL` at the C2 do-nothing control.
- Opened S184 (Schuler & Zeller, "Covering and Uncovering Equivalent Mutants", STVR
  2013) at the DOI reader; added the `corpus/SOURCES.md` row; lesson Gate records URL,
  access date and the located quote; mined M27-4 into `corpus/lessons/round-29.md` with the
  honest sweep row (navigation gap found inherited, below).
- Measured both claims at the data commit `cb4e1c00b43de5e5b3f3b3fa3c0cebe458f81c2c`:
  `evidence/c1-after-cb4e1c00.txt` (six legs PASS, `PRED-C1-r29 verdict=TARGET_MET`, exit 0)
  and `evidence/c2-after-cb4e1c00.txt` (`CHECK R1..R4 PASS`, `PRED-C2-r29 verdict=TARGET_MET`,
  exit 0).
- Harm watch: selftest `MADO_SELFTEST: 460/460 assertions passed` exit 0; census exit 0
  start→end; `tools/`, `corpus/knowledge/`, `SKILL.md`, `PROVINCE.md` byte-untouched; oracle
  pins verified before every receipt run; no compositor/config mutation.
- Misroot sweep at fleet root: **0 mado-owned files** misrooted (the prepared wave was
  never dispatched, so no seat files exist; `.ufo/state/*` and `.ufo/watchdog.log` untouched;
  foreign untracked files left alone).
- Found and recorded (not repaired — claim discipline): the navigation counter reads
  41/43 at base and tip alike — `mutation-testing-r28.md` and `workspace-rules-r27.md` are
  missing from `corpus/README.md` index rows (inherited r27/r28 debt; routed to round 30).

## Landed changes

Lane commits (all pushed; `jj-lane.sh` `landed` lines):

- `aeb4f58b15840c7ee229c12b8ff0b1fe200ddcee` — round-29 freeze: registration, repaired
  composite, C2 counter, controls, wave-1 spec + plan, before receipt. LOG entry: round-29
  "Registration ... frozen `aeb4f58b`".
- `3ae437caf71a3a945285109e014d6d2a0b0d2e5b` — re-freeze: composite self-print label
  `c1-r28` → `c1-r29` (QUALITY-38 smoke catch). LOG entry: "re-frozen at `3ae437ca`".
- `cb4e1c00b43de5e5b3f3b3fa3c0cebe458f81c2c` — data: standalone v5 receipts, both freeze
  smoke receipts, census-before, S184 + lesson, SCORECARD §6.6 erratum, LOG entry.
- `a30b06857724a0bd2ddaa45008fec53a5da4908c` — records: both after-receipts, SCORECARD
  round-29 results + harm watch + planned, census-end.

One worktree file regenerated by the composite's q36 leg (`quality/q36-successor-receipts.txt`,
ephemeral temp paths only) was reverted to committed bytes from the branch — the q36 leg
reads the committed blob at REV, so measurement is unaffected; the revert keeps the
byte-identical boundary proof.

Fleet commits: `16e8491628add9997b95cec495381703c41768fa` (`.ufo/l0-questions.md` append —
round-29 L0) and this report's commit (below).

## Before → after measurements

- **C1 (operability)**: before — at `f652ca99`, `python3 -I .ufo/waves/round-28/c1/count.py
  master` prints `LEG boolword-v5 FAIL | normal=missing mutant=missing` and
  `PRED-C1-r28 verdict=TARGET_MISSED` exit 1 (`evidence/c1-before-f652ca99.txt`). After — at
  `cb4e1c00`, `python3 -I .ufo/waves/round-29/c1/count.py cb4e1c00b43de5e5b3f3b3fa3c0cebe458f81c2c`
  prints all six legs PASS and `PRED-C1-r29 verdict=TARGET_MET` exit 0
  (`evidence/c1-after-cb4e1c00.txt`). Measured commit: `cb4e1c00b43de5e5b3f3b3fa3c0cebe458f81c2c`.
  Do-nothing control: the unrepaired r28 composite at base MISSES (`controls/C1K1-r28composite.txt`).
- **C2 (calibration)**: before — at `f652ca99`, `python3 -I .ufo/waves/round-29/c2/count.py
  master` prints `CHECK R1..R4 FAIL`, `PRED-C2-r29 verdict=TARGET_MISSED` exit 1
  (`controls/C2K1-donothing.txt`). After — at `cb4e1c00`, the same counter prints
  `CHECK R1..R4 PASS`, `PRED-C2-r29 verdict=TARGET_MET` exit 0
  (`evidence/c2-after-cb4e1c00.txt`). Measured commit: `cb4e1c00b43de5e5b3f3b3fa3c0cebe458f81c2c`.
  Do-nothing control: the frozen C2 counter at base MISSES all four checks.

## Sources & frontier

Counting command (frozen manual census, `CORPUS.md`): rows
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` etc. Before — 183 rows over the
committed base blob `f652ca99:corpus/SOURCES.md` (receipt
`.ufo/waves/round-29/evidence/census-before.txt`: rows=183, malformed=0, tiers A=176 B=1
C=6, status mined=164 queued=10 rejected=9, exit 0; matches the r28 committed census-end
receipt). After — 184 rows, malformed=0, tiers A=177 B=1 C=6, status mined=165 queued=10
rejected=9, exit 0 (`.ufo/waves/round-29/evidence/census-end.txt`, validator
`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`).

- Rows added by tier: **A +1** (S184 — Schuler & Zeller, "Covering and Uncovering
  Equivalent Mutants", https://doi.org/10.1002/stvr.1473, opened 2026-10-24 at the DOI
  reader, title-level grounding per the S183 treatment; gate quote in
  `corpus/lessons/round-29.md`).
- Rows touched old→new: none (no status/recheck flips on existing rows).
- Frontier rows advanced: none (no queued row mined this round).
- Sourced claim: C1's refpub/equivalent-mutant method rests on S184 (registration
  "Sourced claim" section; lesson `## Gate`).

Mistake mined: M27-4 (the §6.6 reference-drift overclaim, routed from the r27 spotcheck)
with fix shown able to fail; plus the honest sweep row recording the inherited navigation
gap (41/43) routed to round 30 — both in `corpus/lessons/round-29.md` `## Mistakes`.

## Trend verdicts

- **expansion — unchanged**: one `SOURCES.md` row added (+S184) but no new admitted
  `corpus/knowledge/` ground (the round's surface is repair, not new domain coverage); no
  capability row enters (the repaired composite re-demonstrates the round-28 gate row).
- **quality — improved**: the vacuous composite leg (guard pin never matching committed
  bytes) is repaired and shown printing real tallies under the frozen counter; the
  ephemeral-leg verification basis is now a named committed receipt instead of a dead
  scratch path; both fixes carry committed red-before evidence; the §6.6 record overclaim
  is corrected in the durable record. No admitted entry left failing.
- **discernment — improved**: the lane mined its own routed defects (vacuous pin M28-1,
  ephemeral loss M28-2, the §6.6 reference-drift M27-4) into grounded repairs, published
  the r28 AND-bit miss verbatim and kept the r28 record untouched, and disclosed the
  inherited navigation gap instead of silently repairing it under the table. Outside
  non-author spot-check of this round's gate decisions rides the next closure pass (this
  round's seats were prepared, not dispatched — see below).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  asserted: SKILL.md current through r28 (rows 633–635 verified by the r28 spotcheck); no
  r29 SKILL change (register in scope).
- [~] At least one end-to-end domain task executed and logged in LOG.md — asserted:
  LOG.md round-29 entry (composite repair, receipts, measurements); no new live-desktop
  task (host package pause + read-only substrate still in force).
- [~] Instructions executable by an agent without oral context — asserted: the frozen
  registration + counters ran end-to-end from committed bytes with committed receipts
  (c1-after/c2-after), no oral context.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — asserted: `git diff
  f652ca99 a30b0685 -- PROVINCE.md SKILL.md` empty; no sibling/fleet writes (misroot
  sweep clean); outside-lane independence not established.

No `[x]`: every box lacks a named non-author verifier on record this round.

## Round shape, waves, seats

Shape: **two-claim repair round with a prepared v1 wave** (default shape declared in the
brief). Round total: **33 prepared seats, 0 dispatched, 0 dead**.

- Wave 1 (build + first falsifiers): 33 seats — executors 4, scribes 3, scouts 3,
  connector 1, reviewers 12, critics 5, mutation-testers 2, revenger 1, sentinel 1,
  simplifier 1. Spec `.ufo/waves/round-29/w1-spec.json`; validated under policy v1
  (`w1-plan.json`, `ufo-swarm-wave.mjs plan` exit 0, band 32–64 satisfied).
- **Prepared but NOT dispatched**: this L1 seat has no swarm-dispatch tool on this host
  surface (expected, not a conformance defect — the orchestrator dispatches prepared waves
  itself between rounds). The L2-floor role mix (connector, executors, scribes, scouts,
  reviewers, critics; the §3 planner seat is held by the L1 per the orchestrator ruling)
  is carried on paper by the 33 prepared items; the report itemizes them here so the
  orchestrator can dispatch `w1-spec.json` unchanged.
- Wave 2: not prepared — wave 1's reports do not exist yet; if the operator dispatches
  wave 1 between rounds, wave 2 (attack, 32–64) follows the ≥32-distinct-attack-items rule.
- Residual call: none (no dispatched seats, so no leftovers).

Tool installs: none (pacman pause in force; no `uv tool`/binary installs needed; oracle
pins verified instead of rebuilt).

Open L0 questions: the two r28 questions (ephemeral-input policy; guard-pin repair path)
are answered-by-implementation and remain open for operator overrule — re-filed as a
round-29 line in `.ufo/l0-questions.md` (fleet commit `16e8491628add9997b95cec495381703c41768fa`).

Stale-lane: none — this is a respawn-per-round driver; no other mission of this lane is open.

Honesty note: the r28 claim stays rejected-honest-stop in the record; this round's green
`PRED-C1-r29` is a new predicate on repaired counters, not a retroactive pass of
`PRED-C1-r28`. The composite's leg 1 verifies a committed reviewer-authored receipt
(textual basis), not a fresh suite run — the boundary is declared in the registration and
in the lesson.
