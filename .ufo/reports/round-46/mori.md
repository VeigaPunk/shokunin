# mori — round 46

Lane repo: `/home/vgpnk/Projects/shokunin/mori-shokunin`. Lane commit pushed: `2f04605ab1d113ecf27e77adc0202a21c9bb6ec7`.

## Work performed

Declared one claim, C1 — calibration: re-pin four round-45-verifier-flagged registry cells so their selftest tallies and byte/line-count pins match observed instrument state. Calibration is the target surface because the routed defect is false self-assessment, even though freshness also benefits. The counter result met its literal red-control/green-repair target, but a falsifier showed the predicate can be satisfied with stale strings in the wrong cells; C1 is therefore **unprovable**, not admitted.

- Re-pinned `SKILL.md:184,190,191,194`; the actual C1/C2/auditor/mutant digests, selftest counts and auditor line count were independently re-derived in the wave reports `w1/ScoutDigests.md`, `w1/ScoutTally.md`, and `w1/ExecAuditorLines.md`. These changes and the claim disposition are in the round-46 `LOG.md` entry, carried by lane commit `2f04605`.
- Appended the named 27/27 correction to the round-45 freeze-manifest tally in `LOG.md`; the original 29/29 wording remains untouched. The correction cites the exact `sha256sum -c` command and the 27-check result (`LOG.md:2655-2657`), carried by `2f04605`.
- Added the closure-reconciled round-45 C1/C2/C3 outcomes and the round-46 calibration claim/limitation to `SCORECARD.md`; all scores remain unchanged, with C2 recorded as harmed per the non-author closure (`SCORECARD.md:2547-2561`), carried by `2f04605`.
- Updated the four SHONEN lines to `[~]` with evidence pointers only; no non-author promotion check is claimed (`SHONEN.md:5-8`), carried by `2f04605`.
- Added the round-46 lesson with two mistakes, the Gate source quote, the false-green finding and the consideration disposition (`corpus/lessons/round-46.md:3-20`); added opened own-work source S474 and its bounded-search note (`corpus/SOURCES.md:253-304`), carried by `2f04605`.
- Falsification wave found that the frozen counter accepts stale receipt strings appended to non-semantic cells while the actual cells remain stale (`.ufo/waves/round-46/w1/CritControl.md`, `CritVerdict.md`). It also documented row-wide matching limitations and other findings in the 32 individual reports under `.ufo/waves/round-46/w1/`. The frozen predicate was not edited after scoring. The claim contract records that its text was written after preliminary runs, an ordering defect not backdated (`.ufo/waves/round-46/contract.md`).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed no round-46 mori seat files at fleet root; unrelated operator/sibling paths were left untouched.

## Landed changes

| Change | LOG entry | Lane commit |
|---|---|---|
| Four registry-cell re-pins; frozen counter, prior-SKILL control, contract, spec/dispatch, registry and 32 seat reports | `LOG.md` “Round 46 (L1 calibration repair; claim unprovable)” | `2f04605ab1d113ecf27e77adc0202a21c9bb6ec7` |
| Round-45 C1/C2/C3 scorecard rows and round-46 claim verdict | same round-46 entry | `2f04605ab1d113ecf27e77adc0202a21c9bb6ec7` |
| SHONEN `[~]` assessments, S474 and round-46 lesson | same round-46 entry | `2f04605ab1d113ecf27e77adc0202a21c9bb6ec7` |
| Append-only correction from 29/29 to 27/27 | `LOG.md` “Round-46 correction — round-45 freeze-manifest tally” | `2f04605ab1d113ecf27e77adc0202a21c9bb6ec7` |

## Before → after measurements

- **C1 calibration (frozen result: unprovable).** Counting command: `python3 .ufo/waves/round-46/count-repins.py <SKILL.md>`. Prior committed control (`control-skill.md`, exact snapshot from `12c89ea63491fcca0f46169d809740711d3d052e`): `MORI_R45_REPINS mismatches=4 rows=4`, exit 1. Repaired `SKILL.md`: `MORI_R45_REPINS mismatches=0 rows=4`, exit 0. Control receipt and counter are committed under `.ufo/waves/round-46/`; counter SHA-256 `ebb6a6d3fe08d78791a45643d1ebda2243e5fff271eaada1d7f682317c673327`. The observed counterexample invalidates the intended implication from green to accurate pins: adding stale values outside the target cells also yields green. No score delta; `SCORECARD.md` records the claim unprovable. Independently measured facts do match the corrected text: C1 selftest `pass=16`, C2 selftest `pass=14`, auditor selftest `pass=15`, auditor `743` lines; full hashes are in the cited wave reports and `SKILL.md`.
- Freeze-manifest correction: at the round-45 landing bytes, `grep -v '^#' .ufo/waves/round-45/evidence/freeze-r45.txt | sha256sum -c` produced **27 OK**, rc 0; 28 non-comment lines include one blank, leaving 27 checks. The historical bytes and command are recorded in `LOG.md`; this is a correction, not a separate claim.
- Lane measurement revision for C1: `2f04605ab1d113ecf27e77adc0202a21c9bb6ec7`.

## Sources & frontier

- `corpus/SOURCES.md` row count before → after: **246 → 247**, command: `git show 12c89ea63491fcca0f46169d809740711d3d052e:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'` then `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`.
- Census before: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori` → `mori ok`, rc 0, with the existing W04 duplicate-URL warnings. Census after: same command → `mori ok`, rc 0, same W04 warning set. S474 is the one new tier-A `own-work` row; no rows were touched old→new; no frontier rows advanced. Row quote/source date and the bounded search record are in `corpus/lessons/round-46.md` and `corpus/SOURCES.md`.
- Assimilation: none; no shokuknow package entry was adopted.
- Considerthese: read `considerthese/2026-10-24.md`; considered the proposal to reproduce headline numbers mechanically. The attempt is not claimed as implementation because the frozen counter's false-green mutation proves its text-match is not a measurement. The lesson records the finding and flip condition (`corpus/lessons/round-46.md:6`).
- Misconception mined: calibration / false-green predicate; evidence `w1/CritControl.md` and `w1/CritVerdict.md`; captured-by QUALITY 40; fix and red-before condition in `corpus/lessons/round-46.md`.

## Trend verdicts

- **expansion — unchanged:** no new admitted knowledge entry or uncovered coverage-map ground; S474 is a source row, not expansion credit.
- **quality — unchanged:** no corpus knowledge entry was re-verified or superseded this round.
- **discernment — unchanged:** wave findings are lane-authored; no independent non-author spot-check of this round's Gate decisions is recorded yet.

## SHONEN

- [~] Decision tables, error patterns, checklists and cited sources — `SHONEN.md:5`.
- [~] End-to-end domain task logged — `SHONEN.md:6`.
- [~] Executable instructions without oral context — `SHONEN.md:7`.
- [~] No cross-domain bleed; PROVINCE accurate — `SHONEN.md:8`.

## Round shape and report extras

One v1 wave, 32 seats; one validated and dispatched batched task call. Role mix: reviewer 9, critic 6, mutation-tester 5, scout 4, scribe 4, executor 3, connector 1. The L1 held the planner seat; connector sibling scan was a dedicated item. All 32 seats returned reports; dead seats 0. No wave 2 or residual call. Round total: 32.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Open L0 questions: none. Tool installs/upgrades: none.
