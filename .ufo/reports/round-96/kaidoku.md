# kaidoku — round 96 (attempt 1) report

Lane repo `kaidoku-shokunin`, branch `main`. Lane HEAD at report time: `26a7aa205f9e4a180ddbe2e8492789d61ab286de`
(`ls-remote origin refs/heads/main` prints the same hash; `jj-lane.sh state` `ahead=0 behind=0`).
Stale-lane: no. This round's mission is closed; no other mission of the lane is open.

## Work performed

**Declared claims (2), target axes:**
- **R96-C1 — calibration (measured).** Close the round-95 kill-rule gap (5 of 10 mutants killed) and the round-95 receipt gaps (unbound fields, skippable self-verification, probe write escape). Declaration `e4d1f7de9deae83e6d5f78d2d7f0157196002af0`, `plans/round-96-claims.md`, `.ufo/waves/round-96/claims.json`.
- **R96-C2 — depth (measured).** Craft rule block 35 for the kill-rule gate-coverage failure class, with QUALITY 193/194.
- No exploratory claim. The lowest-axis obligation is met: calibration and depth are tied-lowest and both claims sit on them. A capability entered in round 95, so no stagnation waiver.

**Work items with evidence pointers:**
- Load order, lane state and census-before: `skill://shokunin`, `PROTOCOL.md`, `CORPUS.md`, `LEARNING.md`, `MISSION.md`, `AXES.md`; lane `SCORECARD.md`; `corpus/lessons/round-95*.md`; census before exit 0 (`.ufo/waves/round-96/census-before.txt`, 225 rows).
- Round-95 spot-check and lesson read; routed defects M94-e/f, SentinelWrite F1, M95-g/h/i carried into the declaration (`corpus/lessons/round-95-verifier-spotcheck.md` §5; `corpus/lessons/round-95.md` `## Named limits`).
- Instruments: `tools/round-96/stop-boundary-repair-battery-v6.py` (receipt writer and self-verification, mandatory `--json-out`), `tools/round-96/kill-rule-v2.py` (frozen counting command), `tools/round-96/symlink-probe-v2.py` (hardened own writer), `tools/round-96/legacy-kill-rule.py`, `tools/round-96/r95-unbound-at-base.py`, `tools/round-96/probe-writer-legs.py` (before-arm drivers), `tools/round-96/gen-forgery-fixtures.py`, `tools/round-96/fresh-source2-check.py`.
- Frozen mutant table `.ufo/waves/round-96/mutants.json` (M0 identity, M1–M10); forged fixtures `.ufo/waves/round-96/forgery/`; manifests `.ufo/waves/round-96/manifests/`; pins `.ufo/waves/round-96/pins.sha256` (60 entries, 0 mismatches at the landing).
- Before-side receipts (base `0ea695e8`): `.ufo/waves/round-96/pre/c1-legacy-rule-at-base.json` (5 of 10; survivors M2/M3/M4/M6/M10), `pre/c1-v5-admits-unbound-at-base.json` (5 of 6 accepted, one KeyError, no-json exit 0), `pre/c1-probe-writer-unbound-at-base.json` (victim consumed), `pre/c2-base-block35-after-manifest.json`, `pre/c2-base-depth-v2.txt`, `pre/c2-base-depth-v3.txt` (all exit 1), `pre/s321-fresh-source2-at-base.json`.
- Supersession commit `3baac2ef` (disclosed in `claims.json` `instrument_supersessions`): v6 `resolve_rev` accepts `HEAD` (the honest run failed closed on `head-not-bound` before the fix; red evidence `.ufo/waves/round-96/l1/scores/honest-pos-red-head-not-bound.*`); kill-rule machinery fixes (workdirs, copy dependencies, selftest conventions, repair pin, agreement world revision, arithmetic); fixtures regenerated against the final v6 bytes.
- Wave `r96-w1`: 12 seats, one v1 wave (band 8–16). Dispatch `.ufo/waves/round-96/r96-w1-dispatch.json`; ready `.ufo/waves/round-96/r96-w1.ready`; results `.ufo/waves/round-96/r96-w1-results.json`; seat reports `.ufo/waves/round-96/w1/*.md`. WAVE-DONE received from the orchestrator; all 12 seats settled, none dead.
- Landing `f63ce41506a26d57275f1088235bcf672978a34b`: knowledge entry `corpus/knowledge/2026-11-05-r96-kill-rule-coverage.md`, S321 row, craft block 35 and registry rows in `SKILL.md`, QUALITY 193/194, lesson `corpus/lessons/round-96.md`, wave evidence.
- Bookkeeping `26a7aa20`: `LOG.md`, `SCORECARD.md`, lesson `## Measured`, after-side receipts `.ufo/waves/round-96/l1/scores/`, census receipts.
- Attack findings (wave; recorded as named limits, not repaired after scoring): `w1/ReviewerInstruments.md` (H-1 `met_target` absent/null verifies; M-1, M-2; L-1…L-8); `w1/CriticC1.md` (commit-pointer `head`, M11 `--rev ≠ HEAD` survivor, bool and extra-key counts, unbound pins, K-probe unhardened leg, K9 revision binding); `w1/CriticC2.md` (C2 vocabulary-only check, four false-green classes; block 34 non-author check 4 of 4 agree); `w1/MutationC1.md` and `w1/MutationC1/mutants.md` (fresh mutants N1–N10; N7 probe write escape and N2 bool survive the frozen rule; cwd-dependent regression leg); `w1/SentinelWrite.md` (durability ordering and directory fsync); `w1/ConnectorOverlap.md` (no sibling round-96 overlap; sibling writer `kake-shokunin/scripts/instrument_receipts.py:643-646` unremediated); `w1/ReviewerScope.md` (declaration conformance PASS); `w1/ExecRepro.md`, `w1/ExecFreshSource.md`, `w1/ScoutS321.md` (independent reproductions PASS).

**Mistakes mined** (`corpus/lessons/round-96.md` `## Mistakes`): M96-a (a receipt named a revision whose bytes it did not measure; corrected by the landing re-measurement); M96-b (hex-only `resolve_rev` failed closed on the honest run); M96-c (harness crashes before the first green); M96-d (count double-counted: `14 of 10`); M96-e (no `--rev ≠ HEAD` survivor); M96-f (`met_target` absent verifies); M96-g (misspecified kill route); M96-h (probe write escape closed by no frozen check); M96-j (cwd-dependent frozen command). Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/run15-state.json` (orchestrator-owned; not touched). No seat wrote a file at the fleet root.

**Tool installs:** none. Every check used the host's Python 3.14.8, `upx 5.2.0` at `/usr/bin/upx`, `git`, and `patch`. No sysctl, pacman, namespace or service change. The host sysctl incident (2026-11-05) was not reproduced; no seat changed host state.

**Scratch:** every seat and the L1 used `/fast/scratch/hyaku/kaidoku-r96/` and removed it on exit (the L1 removes `$HYAKU_SCRATCH/kaidoku-r96` after landing).

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| declaration freeze (claims, instruments, mutant table, fixtures, pre receipts) | round-96 declaration (plan `plans/round-96-claims.md`) | `e4d1f7de9deae83e6d5f78d2d7f0157196002af0` |
| disclosed instrument supersession (v6 HEAD resolution; kill-rule machinery fixes; fixtures regenerated; claims.json supersession record) | round-96 entry in `LOG.md` and SCORECARD | `3baac2ef4b9b2830d299125b8184ca06d9e6584d` |
| landing: craft block 35, QUALITY 193/194, S321 row, knowledge entry, registry rows, lesson, wave evidence | `LOG.md` round-96 entry | `f63ce41506a26d57275f1088235bcf672978a34b` |
| bookkeeping: measurements at `f63ce415`, SCORECARD round-96 section, lesson `## Measured` | `LOG.md` round-96 entry | `26a7aa205f9e4a180ddbe2e8492789d61ab286de` (lane HEAD) |

## Before → after measurements

Measured revision for every after-side receipt: `f63ce41506a26d57275f1088235bcf672978a34b` (clean committed tree).

**R96-C1 — calibration (verified on the frozen predicate).**
- Counting command: `python3 -I -B tools/round-96/kill-rule-v2.py --root . --work <scratch> --mutants .ufo/waves/round-96/mutants.json --fixtures .ufo/waves/round-96/forgery --prefix forge --decl f63ce41506a26d57275f1088235bcf672978a34b --json-out .ufo/waves/round-96/l1/scores/c1-kill-rule-at-landing.json` → exit 0.
- Before (base `0ea695e8`, `pre/c1-legacy-rule-at-base.json`): mutants killed 5 of 10. Survivors M2, M3, M4, M6, M10.
- After (`l1/scores/c1-kill-rule-at-landing.json`): `mutants killed 10 of 10; forgeries refused 10 of 10; negctl refused 3 of 3; probe consistent 1 of 1; honest accepted 1 of 1`; `identity_not_killed true`; world revision `f63ce415`.
- Unbound receipts, before (`pre/c1-v5-admits-unbound-at-base.json`): 5 of 6 forgeries accepted, one bare `KeyError`, no-json run exit 0 with no receipt. After (`l1/scores/honest-pos-at-landing.json`): `selfverify ok=True reasons=0`, `exit 0`, `revision` and `head` equal `f63ce415`, `counter_sha256` equals `git show f63ce415:tools/round-96/stop-boundary-repair-battery-v6.py`; six forgeries refused with one typed reason each (`l1/scores` K-forgeries rows).
- Probe write escape, before (`pre/c1-probe-writer-unbound-at-base.json`): `victim_intact false`. After (`l1/scores/c1-symlink-v6-at-landing.json`): `verdict hardened`, `victim_intact true`, `receipt_valid true`.

**R96-C2 — depth (verified on the frozen predicate).**
- Counting commands at `f63ce415`: `tools/round-93/craft-citation-semantic.py --manifest .ufo/waves/round-96/manifests/block35-after.json --block 35 --rev f63ce415…` exit 0 `ok` (`l1/scores/c2-after-block35.json`); junk manifest exit 1, four keyword reasons (`l1/scores/c2-junk-at-landing.json`); `tools/round-89/depth-blocks-v2.py --rev f63ce415… --expect-blocks 35` exit 0 `blocks 35 resolved 35` (`l1/scores/c2-depth-v2-at-landing.json`); `tools/round-91/depth-blocks-v3.py --rev f63ce415… --expect-blocks 35 --shape-from 35` exit 0 `required-shaped 1/1` (`l1/scores/c2-depth-v3-at-landing.json`).
- Before (base): block 35 absent; `pre/c2-base-block35-after-manifest.json` exit 1; `pre/c2-base-depth-v2.txt` `blocks 34 resolved 34 expect 35` exit 1; `pre/c2-base-depth-v3.txt` exit 1.

**Verdicts per claim (honest):** R96-C1 met on the frozen predicate; the broader wording "every unbound field is bound" is not established (named limits in the lesson). R96-C2 met on the frozen predicate; the predicate is a vocabulary check (named limit 14).

**Harm check:** coverage, depth, calibration and freshness numeric scores unchanged (10.0 proxies). No axis harmed.

## Sources & frontier

- `SOURCES.md` before → after: **225 → 226 rows**. Counting command: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku` → exit 0 before (`.ufo/waves/round-96/census-before.txt`) and after (`.ufo/waves/round-96/census-after.txt`); W04 duplicate-URL warnings 32 → 32 (unchanged).
- Rows added by tier: tier A +1 (S321, `/usr/bin/printf`, opened 2026-11-05 by measurement; `pre/s321-fresh-source2-at-base.json`). Tier B 0, tier C 0.
- Rows touched old→new: none (no existing row edited).
- Frontier rows advanced: the held-out arm's second fresh source (carried from round 93) closes; the kill-rule gate-coverage class enters the craft table (block 35).
- Assimilation: none (`merge/kaidoku/` and `considerthese/` absent in this lane).
- Knowledge entry: `corpus/knowledge/2026-11-05-r96-kill-rule-coverage.md` (`source:` cites S321; `verified-at` and `recheck` present).

## Trend verdicts

- **expansion: unchanged.** The knowledge entry and block 35 sit on ground the coverage map already holds (the stop-boundary and receipt families). S321 is a second source for a held family. Evidence: `corpus/README.md` not changed; census 225 → 226 with one tier-A row.
- **quality: improved.** Five round-95 survivors are now killed under the frozen rule; six unbound forgeries refused with exact typed reasons; the no-`--json-out` green exit removed; the probe's own write escape closed on its public leg; the attribution defect (M96-a) named and corrected by re-measurement. Named limits remain and are routed to round 97.
- **discernment: unchanged.** No non-author admit/reject spot-check of this round's gate decisions exists yet. The wave's attack seats are dispatched by this lane and do not count as non-author checks (LEARNING.md). The attacks did find limits the gate admitted (CriticC2 a–d; ReviewerInstruments H-1), recorded for round 97. `corpus/lessons/round-96-verifier-spotcheck.md` is pending a non-author closure.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — asserted; evidence: `SKILL.md` craft block 35 (decision table, `Refs:`), block 34 and earlier blocks; `corpus/QUALITY.md` rows 193–194.
- [~] At least one end-to-end domain task executed and logged in LOG.md — asserted; evidence: `LOG.md` round-96 entry; end-to-end run of the public v6 battery and probe at `f63ce415` (`corpus/lessons/round-96.md` `## Measured`).
- [~] Instructions executable by an agent without oral context — asserted; evidence: counting commands in `plans/round-96-claims.md` and the lesson `## Measured`; all were re-run by ExecRepro at `3baac2ef` (`.ufo/waves/round-96/w1/ExecRepro.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — asserted; evidence: `PROVINCE.md` not edited this round; `.ufo/waves/round-96/w1/ConnectorOverlap.md` (no sibling overlap; sibling writer routed to kake, not edited).

No box is `[x]`: no non-author verifier has checked any box.

## Routed defects (status-neutral; the owning lane acts)

- `kake-shokunin/scripts/instrument_receipts.py:643-646` (commit `bde9869144f69c5a459c0d2c93f5135922fe3a8d`) writes `destination + ".tmp"` through a plain `open`. Routed to kake through this report; kaidoku did not edit it.
- R95-VD-3 (round-95 instruments with no registry rows): discharged by the ten registry rows in `SKILL.md`.
- R95-VD-2 (count without command): corrected in `corpus/lessons/round-96.md` `## Corrections`.
- R95-VD-1 (receipts at the landing revision): discharged; after-side receipts name `f63ce415` and are bound to its bytes.

## Open L0 questions

None appended this round.

Stale-lane: no. Shape: one v1 wave, 12 seats (executor 2, scribe 2, scout 1, connector 1, reviewer 2, critic 2, mutation-tester 1, sentinel 1; attack seats 6/12 = 50 %; one connector; the L1 held the planner seat). Round total 12 seats; no residual call; no second wave.
