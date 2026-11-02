# revenger — round 86 report (hyaku run 23, fresh start)

Round shape: attempt 1 landed the freeze `2311400` and the landing `25041d9`
(claims + instrument + reds + the six fixes + S472 + SKILL.md rows, all pushed)
but died before the adjudication — the after-run receipts, SCORECARD section,
LOG entries and lesson existed only worktree-side. Attempt 2 (this session, the
r73 retry precedent) re-derived every after-run receipt from the COMMITTED
blobs before landing anything, then completed the round: adjudication
`7254587`, receipt completion `4d8716b`, lesson completion `a293816` — all
pushed to `origin/main`. Final tip: `a29381623cbcdffea9fd9cc4331868bf5e3406f3`.

## Work performed

- **Carry-in first (r85 non-author closure, three status-neutral items;
  addressed in the freeze `2311400` before any claim work).** (1) mg_probe.py
  docstring prediction-line vs the registered 0/3 red — ruling recorded as
  `reports/round-85/corrections.md` correction 2 (no in-place rewrite; the
  verified sha pin `1840c30c…3ac03f` stands; standing rule: a docstring
  prediction line states the registration RULE, the registered red receipt
  governs). (2) Census contract-literal form exit 2 (r74–r86 lineage,
  operator-side) — dual round-start receipts landed again
  (`.ufo/waves/round-86/census-round-start-{sanctioned,literal}.log`; sanctioned
  exit 0, 21 W01 + 10 W04, zero E; literal exit 2, routed around). (3) SHONEN
  non-author re-confirmation of the CURRENT SKILL.md bytes — stays
  operator-side, no box marked by the author.
- **C1 (calibration) — orphan_sweep v7, per-source citation-sites accounting**
  (the r84/r85 lessons' routed candidate vector 1), with the live used-by
  pointer-drift class surfaced and closed. Instrument
  `reports/round-86/orphan_sweep7.py` sha `f955cd7d…1948618` frozen at
  `2311400`; red pair over ONE pre-fix tree at base `d7fd9d9`
  (`sweep7-v6-blind-prelanding.log`: v6 blind, `grep -c SWEEP_SRC` → 0;
  `sweep7-red-prelanding.log`: v7 `SWEEP_SRC … mismatch=6` with the six
  exception rows S448/S449/S450/S451/S453/S456, identical basis
  `SWEEP_CORPUS fleet-reports=26 lessons=52 log=1` and gating
  `CITED=1050 COMMITTED=988 LANDABLE_ORPHANS=0 ABSENT=62`, both exit 0);
  preprobe per-pointer `grep -cw` cross-check all six CITES=0, each row keeps
  ≥1 citing pointer so `mined` stays valid (`freshstart-probes.log` probes
  4–5); fix = six rule-2 in-place used-by pointer drops, old→new logged
  (`reports/round-86/usedby-fix-log.txt`); green receipt
  `reports/round-86/sweep7-real-after.log` (this session, from the committed
  blob over the committed adjudication tip `7254587`; plus the landing-time
  state section: mismatch=0 with the one expected S472→lesson absent,
  disclosed; plus the v6 blind leg at the tip → 0; plus section 4, the
  receipt's own post-write full-format classification as the single landable
  orphan — the r84 `sweep5-real-after` precedent, resolved by the
  receipt-completion commit `4d8716b`). Mutation check: selftest 21 v6 + 4 SRC
  legs + `SWEEP_SELFTEST=pass` exit 0 (`sweep7-selftest-after.log`, reproduced
  26/26 by this session from the committed blob); ONE frozen one-substitution
  sed mutant (`USED_BY_ACCOUNTING = True` → `False`, diff exactly line 165,
  mutated sha `0bfe69a0…8c3`) dies exit 1 attributed `selftest: used-by
  accounting drifted (used-by class)` (`sweep7-mutant-kill-after.log`,
  reproduced exactly). Evidence pointer: `reports/round-86/` receipts; SOURCES
  row S472 grounds the claim.
- **C2 (depth) — SKILL.md gains the pointer-hygiene decision rows and the M42
  named error signature.** §3 rule table gains the cite-back rule (six named
  r78–r80-vintage specimens), the placeholder-semantics row (em/en dash + ASCII
  hyphens = no citation sites; the em-dash parser class named with its
  20-phantom-row specimen), and the census/sweep division-of-labor row; §4
  gains M42 (pointer-drift: used-by written as evidence-location; the machine
  check that catches it is the v7 `SWEEP_SRC` block; the rule-2 fix). Reds over
  base bytes 9/0/4 → greens over the landing blob 10/2/8
  (`skill-red-greps.log`, `skill-green-greps.log`; both re-derived by this
  session from `git show` blobs).
- **Fresh-start §7 gate (r71/r72/r73 rejected closures re-read + spot-checked;
  what was ruled out and why).** All three are K-admission claims whose
  deciding wave Q-review surface has never settled on this host (r74 L0:
  no dispatch surface — re-read, unanswered); a do-nothing control reaches
  each identically here. Ruled out with FRESH probes, 2026-11-02, receipt
  `reports/round-86/freshstart-probes.log`: coverage/K (operator-blocked, L0
  r74); coverage/F android (`REA_JADX_MCP_JAR` UNSET, no jadx on PATH; S448
  stands); coverage/M, A1, A1v2 (saturated 3/3, 3/3, 5/5 — frozen holds re-run
  over the landing archive, green); coverage/asset-catalog (macOS-gated; 7
  unsupported_host groups printed, same as r85); ghidra-headless repeat (r75
  capability row holds; r85 spot-check concurred); criterion C repair / R full
  extension / N attribution pair (§9-sizing + r75–r86 lineage, stay routed;
  this round's calibration claim is the routed v7 vector instead); exploratory
  claim (none declared — both claims carry counting commands). Lowest-axis
  routing: coverage is the lowest non-retired axis (K 5.3 < saturation line
  7.0, so the stagnation nudge does NOT apply); the obligation routes on
  documented unreachability (probe 6 enumeration), receipts cited, not on the
  nudge.
- **Holds + no-harm.** Frozen holds re-run over the `25041d9` landing archive
  from the committed probe blobs: M 3/3 (10.00), F4 10/11 (9.09), A1v2 5/5
  (10.00), A1 3/3 (10.00), freshness 18/18, K held-rows 8/15
  (`holds-over-landing-archive.log`; PROVINCE byte-unchanged in range). No-harm
  diff `2311400..25041d9` = 3 files, 29 insertions, 6 deletions — SOURCES.md
  limited to the six used-by cells + the S472 append, SKILL.md additions only;
  corpus/live, fixtures, knowledge/, README, QUALITY.md and every standing
  verifier byte-unchanged; v1–v6 sweep instruments + ag_probe + ag_probe2 +
  f_probe4 + mg_probe absent from the range (`noharm-diff.txt`; v6 blob
  `b2db45b0…f12b7` re-verified). Separability: `c1-only.log` (freeze archive +
  landing SOURCES.md: mismatch=0 with the disclosed S472→lesson absent;
  SKILL greps at red 9/0) and `c2-only.log` (base archive + landing SKILL.md:
  greps 10/2 with v7 absent, S449 drift intact) — both trees rebuilt and
  reproduced value-for-value by this session.
- **L2 floor:** no dispatch surface on this host (r74 L0 stands, re-read);
  every verdict re-derives from committed bytes.

## Landed changes

Every change is tied to a LOG.md entry (round-86 block, entries "Carry-in
first", "Claims", "Fresh-start §7", "Holds + honesty", "Mistakes mined",
"Trends", "Adjudication completion (attempt 2)", "Lesson completion"):

- `2311400` (freeze, attempt 1): `reports/round-86/{claims.md,
  freshstart-probes.log, orphan_sweep7.py, skill-red-greps.log,
  sweep7-red-prelanding.log, sweep7-selftest-red.log,
  sweep7-v6-blind-prelanding.log}`, lane `.ufo/waves/round-86/census-round-start-*.log`,
  `reports/round-85/corrections.md` correction 2 — committed before any fix or
  after-run.
- `25041d9` (landing, attempt 1): `corpus/SOURCES.md` (six used-by drops +
  S472 appended inside the Registry directly after S471), `SKILL.md` (two §3
  rule rows + division-of-labor row + §4 M42), `reports/round-86/usedby-fix-log.txt`.
- `7254587` (adjudication, this session): `SCORECARD.md` round-86 section,
  `LOG.md` round-86 entries, `corpus/lessons/round-86.md`, and the eight
  after-run receipts (`c1-only.log`, `c2-only.log`, `census-after.log`,
  `holds-over-landing-archive.log`, `noharm-diff.txt`,
  `skill-green-greps.log`, `sweep7-mutant-kill-after.log`,
  `sweep7-selftest-after.log`) — every receipt re-derived from committed
  blobs first, all values reproduced.
- `4d8716b` (receipt completion, this session): `reports/round-86/sweep7-real-after.log`
  (the C1 green receipt, run over the committed adjudication tip).
- `a293816` (lesson completion, this session): two completing-session mistake
  rows + the final-measured-revision erratum in `corpus/lessons/round-86.md`,
  one LOG line.
- Report file (this document) written fleet-side, not committed by the lane.

## Before → after measurements

- **C1 (calibration — pointer-truth; no criterion score moves, same claim
  shape as r85 C2).** Counting command (frozen at `2311400`):
  `PYTHONUTF8=1 python -B reports/round-86/orphan_sweep7.py --lane <lane-dir>
  --fleet <fleet-root> --format summary | grep -E '^SWEEP_SRC '` →
  **red** `SWEEP_SRC registry=disk rows=451 sites=499 cited=493 mismatch=6
  absent=0` over the base `d7fd9d9` tree (`sweep7-red-prelanding.log`) →
  **green** `SWEEP_SRC registry=disk rows=452 sites=495 cited=495 mismatch=0
  absent=0` over the committed adjudication tip `7254587`
  (`sweep7-real-after.log` section 2; basis `SWEEP_CORPUS fleet-reports=26
  lessons=53 log=1`; gating `CITED=1064 COMMITTED=1001 LANDABLE_ORPHANS=0
  ABSENT=63`, exit 0; standing re-run at final tip `a293816`:
  `CITED=1064 COMMITTED=1002 LANDABLE_ORPHANS=0 ABSENT=62`, exit 0). Blind
  leg `PYTHONUTF8=1 python -B reports/round-85/orphan_sweep6.py … --format
  summary | grep -c SWEEP_SRC` → `0` at both ends (v6 blob `b2db45b0…f12b7`
  unchanged).
- **C2 (depth).** Counting commands (frozen at `2311400`), over `git show`
  blobs: `grep -cE '^\| M[0-9]+ \|' SKILL.md` → **9** (`d7fd9d9`) →
  **10** (`25041d9`); `grep -c 'cite-back' SKILL.md` → **0** → **2**;
  (`grep -c 'used-by' SKILL.md` → 4 → 8, descriptive). Measured commits:
  `d7fd9d9` (red) → `25041d9` (green).
- **Holds (unchanged, no axis harmed).** Over the `25041d9` landing archive:
  `M_RECORDED=3/3 score=10.00`, `F4_COVERAGE=10/11 score=9.09`,
  `A1V2_RECORDED=5/5 score=10.00`, `A1_RECORDED=3/3 score=10.00`, all exit 0
  (`holds-over-landing-archive.log`); freshness
  `grep -cE '^\| [FK][0-9]+ .*\| (holds|STALE)' corpus/knowledge/{seed.md,2026-10-12-rea-readiness-checklist.md}`
  → 18/18; K held-rows 8/15 (operator-blocked route re-checked, not
  attempted).

## Sources & frontier

SOURCES.md rows **471 → 472** (counting command
`grep -cE '^\| S[0-9]+ \|' corpus/SOURCES.md` over `git show` of each end:
471 at `d7fd9d9` → 472 at `25041d9` and the final tip). +S472 (the used-by
pointer-drift evidence row; own-work, tier A; opened this round;
NF=13 checked at landing, 0 malformed, 0 duplicates; appended inside the
Registry directly after S471). C1 is sourced by S472; C2 is grounded by S472 +
the skill's own rule-2 wording. Census: round start sanctioned exit 0 (21 W01
+ 10 W04, zero E — receipts landed with the freeze; literal exit 2, disclosed
r74–r86 lineage); round end sanctioned exit 0 (31 W = 21 W01 + 10 W04, zero E;
`reports/round-86/census-after.log`, regenerated as this session's own dual run;
literal exit 2, routed around). Mistakes mined: full table in
`corpus/lessons/round-86.md` `## Mistakes` — eight rows: the em-dash
placeholder-parse false positive, the probe parse desync, the frozen counting
command vs first wording, the stale-index diff garbage recurrence (414 phantom
changed files / 68019 deletions vs sha-verified byte-identical blobs), the
shell-heredoc truncation recurrence (second host recurrence; repaired per the
mined rule), the count-from-intent recurrence (7 drafted vs 8 grepped, caught
by the pre-commit grep), plus two completing-session rows: the receipt-format
assertion (prose claim derived from the ABSENT 62→63 movement instead of
printed output — `--format summary` prints no absent rows; caught by
re-reading the raw output pre-commit) and the invalid non-git sweep
construction (`SWEEP_ERROR git ls-tree failed` over a bare archive extraction;
caught by reading before citing; rebuilt as a landing-state git repo).

## Trend verdicts

- **expansion: unchanged** — no knowledge admission (K untouched,
  operator-blocked, route re-checked not attempted), no new capability (v7 is
  a superseding measurement instrument over the existing registered
  `cited-evidence orphan sweep` capability, first-working round r80; the
  capabilities table's supersession note is in the SCORECARD section), no
  family or criterion denominator moved (M 3/3, A1v2 5/5, A1 3/3, F4 10/11
  all hold).
- **quality: improved** — the standing hygiene instrument's routed
  per-source accounting vector became machine-caught with a mutation-checked
  switch over a live six-row class (mismatch=6 → mismatch=0, the fix logged
  old→new), and SKILL.md now carries the pointer-hygiene decision ground the
  drift demonstrated missing (9/0/4 → 10/2/8); every after-run receipt
  re-derived from committed blobs before landing.
- **discernment: improved** — eight real defects mined this round (six
  attempt-1, two completing-session), four caught before any committed byte
  could mislead — two by cross-checks between independent implementations, one
  by the frozen-command pre-check, and the completing session's receipt-format
  assertion by re-reading the raw output before committing; the round's
  honest shape (attempt-1 death, worktree-only residue, full re-derivation
  before landing) is recorded in LOG and the lesson erratum rather than
  papered over.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — SKILL.md gained the pointer-hygiene rows and M42 this round
  (`25041d9`); the standing routed need (a non-lane reviewer re-confirming the
  CURRENT bytes) now names the r86 bytes and stays operator-side (r69 spot-check
  V7 lineage; r85 closure item 3 re-recorded; no box marked by the author).
- `[~]` At least one end-to-end domain task executed and logged in LOG.md —
  the round's task is the instrument/registry/skill completion chain; the
  last producer-record execution remains r85 (`corpus/live/runs/round-85/`),
  no new producer run this round (pointer: LOG round-86 block; SCORECARD r86
  holds receipt).
- `[~]` Instructions executable by an agent without oral context — the frozen
  counting commands and the v7 selftest/mutant recipes were executed verbatim
  by this session from committed blobs with observed exits matching promises
  (receipts above); no independent outside instruction verifier.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md
  byte-unchanged in `d7fd9d9..a293816` (`git diff --stat` over the range is
  empty for PROVINCE.md); ADJ-06 remains reported-not-absorbed.

Assimilation: `considerthese/` re-read this round (2026-10-20 through
2026-10-28 — the same eight files; no new proposals since r85; proposals 1–3
grounded out r83/r84, proposal 4 sits in the §9-ruled criterion-C space,
proposal 5 is the bot's own procedure, not lane scope); adopted nothing —
shokuknow unreachable. L0 side channel: no new questions filed this round
(open items — F android jar, K wave surface, census literal form, SHONEN box 1
non-author re-confirmation — are already on file and were routed around, never
treated as answered).

Admission: both claims verify (C1 green reproduced from the committed blob
over the committed tip; C2 greens reproduced over committed blobs; separability
and holds green; no axis harmed — all non-claimed criteria unchanged), so the
round reports **admitted at self-assessment**, per the contract subject to the
non-author closure judge's re-derivation.
