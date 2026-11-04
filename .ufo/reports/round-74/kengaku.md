# Round 74 — kengaku

Lane: kengaku · round 74 (attempt 1) · hyaku run 15 · 2026-11-04 UTC
Base `b7910802549978404218937d4be6a75acae0e020` → tip `cbb8b8d802ec68240b6bb78ec7c9cd96a5e94b87` (pushed, ls-remote verified).

## Work performed

Declared claims (2):

- **R74-C1 / coverage** (lowest owned non-retired axis, L0-capped at 7) — the registry-completeness
  gate decouples advertised-universe discovery from `SKILL.md`'s `## Gate/probe registry` table and
  fixes hyphenated-path regex matching, eliminating circular self-advertising.
- **R74-C2 / calibration** (held at ceiling 10, exercised) — the registry declaration audit prices
  the four round-73 blind spots: named `MALFORMED-ROW` defects (no silent skips), entry-flag
  verification, self-test runner existence, and all-items errata revision consistency.

Work items, each with an evidence pointer:

- Froze both claims before data: `plans/round-74-claims.md` (freeze `f4d651c5`), counters
  `plans/round74_c1_registry.py` + `plans/round74_c2_registry_audit.py`, receipts under
  `corpus/evidence/round74/` (c1 before/selftest/control/after, c2 red-before/controls/after).
- Ran the §2b frontier step: S250 (Python 3.15.2 argparse docs) opened live with capture +
  sha256 + located quote (`corpus/evidence/round74/sources/argparse-docs.html`, 334994 bytes,
  `ad9095cdaa99c953046f510d6cd86cd6f7a1086c5aa35743c26e3fa41e4b5b8d`, quote at line 908, 24 words);
  row appended to `corpus/SOURCES.md`; lesson `corpus/lessons/round-74.md` with Gate + Mistakes
  M74-1…7; census before → after (241 → 242 rows, rc 0 both ends).
- Landed both new registry rows in `SKILL.md:706-707` (8-field standard; verified by
  RegistryReviewerR74's matrix).
- Dispatched one v1 wave of 16 seats (spec `.ufo/waves/round-74/w1-spec.json`, validated
  `w1-validate.rc=0`); WAVE-DONE received; results in `.ufo/waves/round-74/w1-results.json`.
- Integrated 4 returned seat reports; recorded 12 dead seats (empty output, no report files)
  in the lesson; re-ran the C2 discriminating fixture and both selftests/mutants as L1
  integration evidence (`c2-discriminating-rerun.txt`).
- In-round corrections (each re-derived): Amendment A1 (74e2e15) fixing the claims-doc Before
  prose; regenerated `c1-control-decoupled.txt` from the plans/*.md-only advertisement fixture;
  Q1 triad added to both held candidates.

## Landed changes

All changes committed via `jj-lane.sh` and pushed; `git ls-remote origin refs/heads/master`
prints `cbb8b8d802ec68240b6bb78ec7c9cd96a5e94b87`.

- `cbb8b8d8` — round-74 integration: SKILL.md rows + line-17 census correction, LOG.md,
  SCORECARD.md round-74 section, corpus/README.md round-74 artifacts, regenerated control
  receipt, Q1 triad fixes, discriminating rerun, wave results/registry, dead-seat record.
- `74e2e15a` — Amendment A1 (claims-doc Before description correction).
- `cea7ebf3` — wave w1 ready file.
- `f4d651c5` — freeze: claims doc, both instruments, registry row S250, census captures,
  C1/C2 before+control receipts, wave spec+dispatch.
- LOG.md round-74 entry; SCORECARD.md round-74 section (both in `cbb8b8d8`).

## Before → after measurements

R74-C1 (coverage) — counting command `python3 plans/round74_c1_registry.py --lane .`:

- Before (legacy control, `corpus/evidence/round74/c1-before.txt`): `UNIVERSE mode=legacy
  files=78`, `ADVERTISED total=115`, `REGISTERED total=115 rows=116`, `MISSING 0`,
  `PREDICATE R52-C2 pass`, `PREDICATE R74-C1 fail`, rc 1. Legacy self-advertises every
  registry row, so incompleteness is invisible (the frozen false-green).
- After (`corpus/evidence/round74/c1-after.txt`): `UNIVERSE mode=decoupled files=136
  plans_seen=90`, `ADVERTISED total=116`, `REGISTERED total=116 rows=116`, all six legs 0,
  `PREDICATE R74-C1 pass`, rc 0. Measured at tip `cbb8b8d8`.
- Control (`c1-control-decoupled.txt`): instrument advertised only via `plans/*.md`, row
  dropped → decoupled `MISSING 1` rc 1; legacy drops it from both sides, `MISSING 0`,
  `PREDICATE R52-C2 pass` (false green reproduced).

R74-C2 (calibration) — counting command `python3 plans/round74_c2_registry_audit.py --lane .`:

- Before (`c2-red-before.txt`, 9-cell malformed-row fixture): round-73 audit `MISMATCH 0`,
  rc 0 (silent skip); round-74 audit `MALFORMED defect n=1`, `MISMATCH 1`, rc 1.
- After (`c2-after.txt`): `INSTRUMENTS total=116 derived=registry rows=116`,
  `PARSED scripts=116 failed=0`, `D1–D4 ok n=0`, `MALFORMED ok n=0`, `MISMATCH 0`,
  `DEFECTS n=0`, `PREDICATE R74-C2 pass`, rc 0. Measured at tip `cbb8b8d8`.
- Controls (`c2-controls.txt`): `--selftest` arms=4 red=3 ok=True; `--mutants` total=7
  killed=7 survived=0 invalid=0 null_detected=1; discriminating rerun `c2-discriminating-rerun.txt`.

## Sources & frontier

Command (both ends):
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`

- Before: 241 rows, rc 0, 25 W04 warnings (`.ufo/waves/round-74/census-before.txt`).
- After: 242 rows, rc 0, 25 W04 warnings (`corpus/evidence/round74/census-after.txt`).
- Rows added: 1 tier-A row (S250, Python 3.15.2 argparse docs, opened live this round).
- Rows touched old→new: none (single appended row only).
- Frontier: S250 grounds the held candidate `corpus/knowledge/registry-argv-and-flag-audit.md`
  (admission: hold — outside non-author spot-check still required per Q13/Q14). Earlier held
  entries remain held (offline, provenance, derivation). Assimilation: none.
- New capability row: none.

## Trend verdicts

- **expansion: unchanged.** One A-tier row (241→242), no admitted knowledge entry, no
  capability row; the two new instruments repair existing registry machinery rather than
  opening new measurement surface.
- **quality: improved.** Four named round-73 blind spots now priced with named defects and
  killed mutants (7/7); the C1 gate can no longer be circularly self-satisfied; two
  reference-drift defects in the round's own claims doc/receipt were caught by seats and
  corrected in-round (A1, M74-7) rather than smoothed.
- **discernment: improved.** The wave's returned seats wrote the defects down (C1Decoupled-
  AuditR74's MEDIUM receipt-fidelity finding, EntryFalsifyR74's Q1-triad findings), the L1
  landed fixes for each, and 12 dead seats are recorded by name instead of silently dropped.

## SHONEN

- [~] Box 1 — evidence quality: two new gates run green with selftest + mutant batteries
  (`c2-controls.txt`, `c1-selftest.txt`); receipts byte-verified by an independent seat.
  Non-author closure remains the promoter.
- [~] Box 2 — claim sizing: both claims are single-command predicates with frozen sentences,
  controls and kill rules (`plans/round-74-claims.md`); no axis harmed (round diff
  deletion column = 1 line, the documented SKILL.md line-17 correction).
- [~] Box 3 — registry/index: both new rows pass the 8-field standard (RegistryReviewerR74
  matrix); README round-74 section added; S250 row is census-clean.
- [~] Box 4 — lane hygiene: dead seats named, scratch cleaned, no fleet-root misroots from
  this round's seats; `jj-lane.sh state` clean at push.

Stale-lane: none — respawn-per-round driver; no other mission of this lane is open.

Tool installs: none this round (pacman guard respected; all work used in-repo Python 3).

Open L0 questions carried unchanged: `kengaku | round-25/33/51`, `round-54`, `round-56`,
`round-63`, `round-65`, `round-66`, `round-67`.

Dead seats (12, recorded honestly): C1CriticR74, C2AuditReplayR74, C2BlindSpotR74,
C2CriticR74, SourcesArgparseR74, KnowledgeEntryR74, LessonR74, SiblingConnectorR74,
CredentialSentinelR74, RoundStateScoutR74, C1FixtureControlR74, C2FixtureControlR74 —
all settled with empty output and no report files in `.ufo/waves/round-74/w1/`.
