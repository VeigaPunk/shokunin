# kengaku — round 58 report (hyaku run 13, 2026-11-01)

Lane: `fleet/kengaku-shokunin`, branch `master`. Base `a6b209cf434dae69f924858b4ea9a1bcf015eecc`
(the round-57 verifier spot-check tip). Measurement environment: WSL2 Ubuntu-24.04 (python
3.12.3, bwrap 0.9.0, git 2.56.0, numpy 2.5.4; uv/pytest absent — the r56 A3.4 canonical
counter environment preserved; no environment mutation this round). Executions ran from
script files with in-file EXIT capture (the r56 relay lesson), counters on clean master
clones (the tip clones are named in each receipt).

## Work performed

- **R57-W1 discharged first (carry-in).** The cited r57 before-count
  `grep -c 'fourteenth' PROVINCE.md` → 0 at base is SUPERSEDED: re-measured against the
  base commit's bytes, the true value is **1** — the round-56 PROVINCE section's own
  negation "this round adds the oracle, **not a fourteenth task**", `PROVINCE.md:683`. The
  honest r57 before→after by the plain command was 1→3. Dated erratum recorded in
  `plans/round-58-claims.md` (freeze `d6bc6027`) and here; **standing rule adopted**: every
  cited before-count is re-run against the base commit's bytes before it is frozen, and
  counting anchors must exclude negations (structural anchors used this round: SOURCES row
  ids, instrument paths, ROW-line patterns). Evidence: `.ufo/waves/round-58/recon/base-byte-counts.txt`
  (`git show c9ce9a71:PROVINCE.md | grep -c fourteenth` → 1 at the r57 base; → 3 at the r58
  base; `fifteenth` → 0 at the r58 base before use).
- **Carried opens discharged with evidence (before any freeze):** (1) `round50-c1` —
  per-fixture rebuild of all 126 population fixtures in the counter's own native-fs
  environment (`recon/r50-ev3n/`): 1/126 matcher (`n10-empty-repo`, the only fixture whose
  build runs no git plumbing beyond `git init`; stable + EQ-pin across 3 rebuilds), 125
  deterministic drifters; full double-build discriminator (`recon/r50-ev2n/table2.txt`):
  `match_b1=1 unstable=0` — the pin froze git-plumbing store bytes no cross-host rebuild
  reproduces; re-pin sound. (2) R56-F1 — falsifier fixtures built and measured at base with
  the OLD checker BEFORE the fix (`recon/esc-falsifier.txt`: fx-good false-positives
  `line:1`, fx-red true positive, fx-words hides a real words defect); the fixed checker's
  receipts (`esc-falsifier-fixed-checker.txt`). (3) The three L0 questions
  (`kengaku | round-25/33/51` coverage cap; `kengaku | round-56` L2 surface + ledger host
  column) remain open — nothing assumed answered; coverage is claimed predicate-met with
  the score held at 7 again.
- **R58-C1 (operability; the R56-F1 repair)** — see the claim table below.
- **R58-C2 (freshness; round50-c1)** — see the claim table below.
- **R58-C3 (coverage, the lowest owned axis, L0-capped)** — see the claim table below.
- **The repair cascade — captured, not laundered.** The wave F/P/C3 landings broke four
  tip counters before closure and every break was diagnosed and honestly repaired or
  re-declared: the round36-c2 W4 leg caught my doubled README/PROVINCE rows (a mid-flight
  edit race — mined in the lesson); round51-routing's frozen disposition vocabulary caught
  two out-of-vocabulary dispositions (R56-F1/F2 normalized, dated) and two broken landed
  check fields (one greped a file that never existed; one held prose, not a command —
  repaired, dated, correction history in the findings rows); the r40 `a_tok` fixture caught
  S214's duplicate digest (fixture edit scoped to the `| S111 |` row, dated); the
  round-close E11 leg held the used-by paths until the knowledge entry landed.
  round51-routing honestly flipped GREEN (`PREDICATE R51-C2 pass`) — the repair cascade
  closed every routed defect it touched (findings file now 79 rows: R56-F1 closed
  fixed-verified, R56-F2 normalized, R58-F1 and R58-F2 born closed).
- **Round-close discipline** — the pushed head `46fe5398` re-runs its whole advertised
  surface green: registry `PREDICATE R52-C2 pass`, `LANDCHECK PASS n=4`, full entry-truth
  `executed=87 timeout=0 mismatched=0 evidence_missing=0 laundered=0` with
  `BINDING l1=0 l2=0 l3=0` and TIPSTATE 56g/31r declared equal to observed,
  `PREDICATE R55-C2 pass`, exit 0 (receipt
  `.ufo/waves/round-58/waveR/final-tip-receipts-r3.txt`, measured at `bf48fd2072`, the
  parent of the receipt commit — the round-57 closure shape); the closing sequence caught
  three of my own registration mistakes at the tips (the r35 stale fragment, the
  ledger≠registry argv token, the crashing literal `--work DIR`) — each repaired and
  honestly re-declared before the green receipt; census re-validated at round end
  (exit 0, verdict ok); scratch removed.

## Landed changes (all committed via the treecommit helper, pushed to origin master)

| commit | content |
|---|---|
| `d6bc6027` | freeze — R57-W1 erratum + standing rule; claims R58-C1/C2/C3 with predictions frozen BEFORE the first capture run; probe `plans/round58_c2_kl_probe.py`; captures `corpus/evidence/round58/tb2-distribution-search/`; oracle note; SOURCES S209–S212 (201→205); LOG wave entry |
| `0e60ec31` | freeze receipts — pre-freeze measurements (anchor before-state, base-byte counts, falsifier receipts, r50 per-fixture tables + stability + re-pin source) |
| `f58c0d6a` | wave F (R58-C1) — QUOTE_RE escape-aware repair + 3 escaped-quote falsifier selftest fixtures (6/6); S213–S217 supersessions (the repair's exposed defects repaired per Q34); round46_c2 PINS + registry cell + ledger row honestly refreshed/flipped green |
| `c39d0e40` | wave P (R58-C2) — population re-pinned on this host (pin `f41db91b`, dated header, rows byte-preserved); `POPULATION_SHA` refreshed with the old pin named; registry cell dated; round50-c1 ledger honestly flipped green |
| `b0b1d729` | wave C3 (R58-C3) — knowledge entry `corpus/knowledge/tb2-distribution-search-grader.md` + index row + PROVINCE round-58 section (15 of 89); probe registered (registry 86 / ledger 86; receipt `corpus/evidence/round58/kl-probe.txt` sha256 `3c93e06a…53c1f` at tip `c39d0e40`); findings R56-F1 closed, R56-F2 normalized, R58-F1/R58-F2 born closed; `a_tok` fixture scoped; round51-routing flipped green |
| `201a6a08` | wave E — SCORECARD round-58 section + capability row + planned r59; lesson `corpus/lessons/round-58.md`; LOG measured close; claims-doc dated corrections |
| `9defcad6` | wave F2 — the repaired anchor checker registered FIRST-CLASS (registry row + ledger row; the tip registry counter had caught the SCORECARD counting command advertising it: `ADVERTISED 86 / REGISTERED 85`); lesson mistake row added |
| `f93db89b` | wave R — final tip receipts (registry `PREDICATE R52-C2 pass`; `LANDCHECK PASS n=4`; full entry-truth `executed=86 mismatched=0 laundered=0`, TIPSTATE 55g/31r declared==observed, at `9defcad6`) + the r35 stale-expectation fragment honestly refreshed 60/60→61/61 (dated, class unchanged — the known r35 pattern) + census-end receipt exit 0 (20 W04 = 15 pre-existing + 5 supersession duplicates) |
| `3cf16a42` | wave R2 — the round58-c2 ledger argv aligned to its registry cell token (the r55 L1 binding checks the two verbatim; static legs green, `BINDING l1=0 l2=0 l3=0`); its receipts honestly captured the NEXT catch: the probe's entry run crashed on the literal `--work DIR` token (`LAUNDERED round58-c2 declared green, entry exit=1`) |
| `bf48fd2072` | wave R3 — the round58-c2 entry argv set BARE (the r57 eigen-probe form); bare run re-measured green; its receipts captured the final all-green state |
| `46fe5398` | close receipt — re-derived at the pushed head `bf48fd2072`: registry `PREDICATE R52-C2 pass`, `LANDCHECK PASS n=4`, full entry-truth `executed=87 timeout=0 mismatched=0 evidence_missing=0 laundered=0`, `BINDING l1=0 l2=0 l3=0`, TIPSTATE 56g/31r declared==observed, `PREDICATE R55-C2 pass`, exit 0 (`.ufo/waves/round-58/waveR/final-tip-receipts-r3.txt`) — the round-57 closure property reproduces at the pushed head |

LOG entries: the freeze wave entry + the measured-close entry (LOG.md). SCORECARD: round-58
section, capability `tolerance-band-grader-probe`, planned round 59.

## Before → after measurements (counting commands, measured at the named commits)

- **R58-C1 (operability)** — before, at base `a6b209cf` (clean clone,
  `.ufo/waves/round-58/recon/anchor-before.txt`): `python3 plans/anchor_line_check.py --lane .`
  → `ROW S201 state=live defects=line:1` … `ANCHORLINE rows=201 cited=59 captured=52
  uncaptured=7 defective=9 repaired=8 live=1 cells=1`, exit 1 (false positive);
  `python3 plans/round46_c2_verify.py --lane .` → `A anchorline live=1 … DEFECT`,
  `PREDICATE C2 fail`, exit 1. After, at wave F `f58c0d6a` (verified on the fix clone
  before landing; re-derived at the tips): `python3 plans/anchor_line_check.py --lane .` →
  `ROW S201 state=repaired by=S213 defects=words:1` … `ANCHORLINE rows=210 cited=64
  captured=57 live=0`, exit 0; `python3 plans/round46_c2_verify.py --lane .` →
  `PINS total=3 mismatched=0`, `PREDICATE C2 pass`, exit 0; `--selftest` 6/6 (RED, GREEN,
  JUNK unchanged; ESC-GOOD clean; ESC-RED line:1 retained; ESC-WORDS words:1 exposed).
  Measured revision: `f58c0d6a`.
- **R58-C2 (freshness)** — before, at base `a6b209cf` (full run, receipt
  `recon/round50-before.txt`): `POPULATION fixtures=126 pin=b5197f94… mismatched=125
  build_errors=0`, `PREDICATE R50-C1 fail`, exit 1. After, at wave P `c39d0e40` (pre-verified
  on the wave-P clone with the labelled testing-only `--allow-dirty`; the landed-tip re-run
  is in the final receipts): `POPULATION fixtures=126 pin=f41db91b… mismatched=0
  build_errors=0`, `HONEST fixtures=126 admitted=126 refused=0 error=0`, `REFUSALS total=20
  clean=20`, `SEALED 12+20 clean`, `MUTANTS total=15 caught=15 broken=0 floor=12 verdict=met`,
  `PREDICATE R50-C1 pass`, exit 0. Measured revision: `c39d0e40`.
- **R58-C3 (coverage)** — before, at base bytes (R57-W1 rule): `git show
  a6b209cf:PROVINCE.md | grep -c fifteenth` → 0 (rc 1); `git show a6b209cf:corpus/SOURCES.md
  | grep -c S209` → 0 (rc 1); `git cat-file -e a6b209cf:plans/round58_c2_kl_probe.py` →
  absent. After: probe `python3 plans/round58_c2_kl_probe.py --lane . --work <scratch>
  --receipt corpus/evidence/round58/kl-probe.txt` → `cases=12 legs=48 mismatches=0 setup=0
  predicted_u=0`, `PREDICATE R58-C3 pass`, exit 0 (first capture run after the freeze; tip
  re-run receipt sha256 `3c93e06a…53c1f`); `grep -c fifteenth PROVINCE.md` → 2 (both in the
  round-58 section; no negation uses the word); `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  corpus/SOURCES.md` → 210 (201→210); sha-refusal kill: one byte appended to the capture in
  a scratch clone → `SETUP grader sha256 … != frozen pin`, KILL-EXIT=1 (the freeze wrote
  exit 2; measured 1 — dated correction in the claims doc; the refusal property holds: the
  drifted capture is never materialized nor executed). Measured revision: first run at the
  fix clone post-freeze; official receipt at `c39d0e40`.

## Sources & frontier

`SOURCES.md` rows before→after: 201 → 210 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` → 210; census-validated at round end, exit 0, verdict ok — 20 W04
duplicate-url warnings = the 15 pre-existing + 5 from the supersession rows carrying their
originals' URLs, named in the lesson). Rows S209–S212 opened this round (Gate table in
`plans/round-58-claims.md` and `corpus/lessons/round-58.md`: URL, access date 2026-11-01,
≤25-word located quotes, all four admit tier A; no rejections, no flips). S213–S217 are Q34
correction rows (same sources and captures, corrected anchors). C3 is the round's sourced
claim (rides S209–S212 + the oracle note + the probe receipt). Mistake mining:
`corpus/lessons/round-58.md` `## Mistakes` — three rows (freeze-exit-path prediction;
non-idempotent edit script caught by the W4 counter; fixture bytes re-typed instead of
derived). Census receipts: round start exit 0 (15 pre-existing W04 warnings); round end in
the final receipts.

## Trend verdicts

- **expansion: improved** — the frontier moved 14 → 15 of 89 TB2 task graders, and the new
  grader is a CLASS the corpus lacked (a numeric tolerance band on aggregated functionals —
  every previously executed grader decided exact predicates); the probe enters the
  capabilities table (`tolerance-band-grader-probe`); SOURCES 201→210; the score stays 7 by
  the lane's standing L0 design and the report says so rather than moving a capped number.
- **quality: improved** — the repair cascade is the headline: the two landed repairs broke
  six tip-counter surfaces (W4 row-counting, disposition vocabulary, two landed check
  fields, a_tok uniqueness, E11 used-by paths, and the registry advertisement of the
  repaired checker itself) and every break was captured by the designed tip counters BEFORE
  closure, then repaired and honestly re-declared; the pushed tip re-runs its whole
  advertised surface green — registry `PREDICATE R52-C2 pass`, `LANDCHECK PASS n=4`, full
  entry-truth `executed=86 timeout=0 mismatched=0 laundered=0` with TIPSTATE declared equal
  to observed (receipts committed at `f93db89b`, measured at `9defcad6`, re-derivable at
  the pushed head per the round-57 shape); three ledger rows honestly flipped green with
  dated reasons, one red row's fragment honestly refreshed (r35, dated); one fixture, one
  registry registration and two check fields repaired with dated notes.
- **discernment: improved** — 48/48 full-commitment predictions confirmed on the first
  capture run (zero U marks — the honest contrast with r57's timing gate, recorded in the
  knowledge entry); the falsifier fixtures pinned both directions BEFORE the fix; the
  branch-A re-pin decision was made from the discriminator's measurements, not hope; the
  kill-exit misprediction is dated-corrected in the freeze rather than papered over.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  SKILL.md (the `## Gate/probe registry` now 86 rows including the round-58 KL probe,
  measured this round; the round46-c2 and round50-c1 cells carry dated refreshes)
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — LOG.md round-58
  entries; the end-to-end domain task is R58-C3: a pinned benchmark grader fetched,
  captured, sha-pinned, executed offline under bwrap against a frozen zero-U prediction
  table, its class findings recorded (R58-C1/R58-C2 are also executed domain work)
- `[~]` Instructions executable by an agent without oral context — this round's evidence:
  every measurement ran from committed instructions alone on fresh clones (the freeze →
  probe runs at the freeze tip; the counters at the wave tips; the final receipts), receipts
  committed under `.ufo/waves/round-58/`
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md round-58 section
  dated; the TB2 refusal list unchanged; nothing absorbed (the fleet-level census script and
  operator files remain read-only; reported out: none)

## Assimilation

`considerthese/` mined (eight files, 2026-10-19…26, unchanged on disk since the round-56
mining): the 2026-10-20 standing round-close-gate proposal is already implemented
(`plans/round_close.py`, used this round — its E11 leg held the used-by paths until the
knowledge entry landed); the 2026-10-25 tip-receipts proposal is implemented and registered
(`plans/tip_receipts.py`); the 2026-10-26 r52-repair proposal stays refused on its
demonstrated regression. Nothing new adoptable this round. `Assimilation: none — shokuknow
unreachable`.

## L2 floor disclosure (standing)

The batched ≥8-L2 dispatch surface is again unavailable in this session (the standing L0
`kengaku | round-56` remains unanswered; nothing assumed answered). The round routed around
it as before: the frozen instruments' own falsification machinery (the falsifier fixtures,
the sha-refusal kill, the double-build discriminator, the tip counters that caught four
breakages, the pre-verified fix clones) and the orchestrator's non-author closure are the
adversarial coverage. Ruling still with the operator.

## Claim sizing (§9)

All three claims are do-nothing-unreachable: C1 requires landing a regex repair + five
supersession rows + three dated counter refreshes and re-measuring at tips (the committed
before-receipts show the same commands red at base — a no-op cannot turn them green); C2
requires the root-cause measurements (double-build discriminator) and the re-pin (the
before-receipt shows mismatched=125 at base); C3 requires live pinned fetches, a
sha-refusing offline executor and bwrap (none exists at base). Not a FRESH-START round; no
prior-rejection spot-check required.
