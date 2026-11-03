# kengaku — round 65 report (attempt 1)

Lane: `kengaku-shokunin`, branch `master`. Lane landing commit (pushed; `git ls-remote origin refs/heads/master` = `edbb0bc086b7f3c3962ba04202785f0c868d540d`): `edbb0bc0`. Freeze landing before any scored run: `b5032ff8`. Base: `12a6255170bcc466029bf82037885fd69e20370f` (round-64 closure tip). Wave: `.ufo/waves/round-65/w1` (v1, 12 seats). Stale-lane: no (respawn-per-round; no other mission of this lane is open). Tool installs: none (gcc 16.2.1, gcov 16.2.1, bwrap 0.13.1, uv 0.13.0 and sqlite3 3.54.0 were already present; the SQLite amalgamation was downloaded as a source artifact, not installed; pacman not invoked).

## Work performed

**Declared claims (2), distinct axes.**
- **R65-C1 — coverage** (lowest owned axis, L0-capped at 7; capability acquisition `offline-db-state-grader-probe`): execute the `db-state` TB2 grader `sqlite-with-gcov` offline, against five frozen cases × three legs. Predicate and counting command: `plans/round-65-claims.md` R65-C1. **Verdict: predicate met on the frozen text fields; coverage held at 7 (L0 cap); capability enters.** Carried limitation (sentinel M-1, must-fix, routed — see below): the counting command admits a hand-fabricated receipt, so the verdict is stated as "predicate met on the text fields; live witness `corpus/evidence/round65/battery-run.txt`".
- **R65-C2 — calibration** (held at ceiling 10, exercised): the round-64 non-author closure's four routed defects (`corpus/lessons/round-64-verifier-spotcheck.md` §7.1–§7.4) land as dated, append-only corrections. **Verdict: predicate met under Amendment A1; calibration held at 10.**

**Work items with evidence.**
- Protocol load: `skill://shokunin`, the canonical kimi-shokunin protocol (`PROTOCOL.md`, `CORPUS.md`, `LEARNING.md`, `AXES.md`, `MISSION.md`), `skill://godspeed` (directive bytes `/home/vgpnk/.agents/skills/godspeed/directive.md`), lane SKILL/PROVINCE/SCORECARD/SHONEN, `corpus/QUALITY.md`, `corpus/README.md` `## Frontier`, lessons 61–64, and `corpus/lessons/round-64-verifier-spotcheck.md` (outside check of round 64, §7 routed defects).
- Pre-freeze controls (measured before the freeze; committed): `corpus/evidence/round65/g1-capture.txt` (P/P/P), `g2-capture.txt` (F/F/F, `sqlite3 not found in PATH`), `g4-capture.txt` (P/P/F, `No .gcno files found`), `g5-capture.txt` (P/P/F, unmasked control, `No .gcda files found`); `grader-import-scan.txt` (stdlib-only; three test functions in file order); `c2-before-counters.txt` (all four counters 0 at base); `census-before.txt` (exit 0, 224 rows at start).
- Probe and receipts: `plans/round65_c1_sqlite_probe.py`; receipt of record `corpus/evidence/round65/sqlite-gcov-probe.txt` (sha256 `25c7cab7…535b3ba0`); live witness `corpus/evidence/round65/battery-run.txt`; replication `corpus/evidence/round65/replication-run2-receipt.txt` (same vectors, different PID and timings); checker `check-receipt.txt`, selftest `selftest.txt`, `render-table.txt`.
- Knowledge entry `corpus/knowledge/tb2-sqlite-gcov-offline.md` (provenance trio first; `TRIO pass`).
- Registry: S232 and S233 (`queued` → `mined`, `used-by` set); S234 (`supersedes S230`, `mined`); S230 unchanged byte-for-byte.
- Round-64 corrections (R65-C2): `corpus/lessons/round-64.md` `## Erratum (round 65)` (token `R64-ERRATUM-65`); `corpus/knowledge/tb2-kv-store-grpc-offline.md` `## Citation addendum (round 65)`; `SCORECARD.md` round-64 correction block (`### Round-64 correction (round 65, routed defect 2)`); `corpus/QUALITY.md` Q47 (routed defect 3) and Q48 (from the freeze's own mistakes).
- SKILL: db-state row flipped to `executed 1 of 2` (`SKILL.md:83`); registry row `round65-c1-sqlite-probe` (`SKILL.md:686`); `plans/round54-entrytruth.json` row `round65-c1-sqlite-probe` (`:1253`).
- Claims Amendment A1 (dated, appended to `plans/round-65-claims.md`): restates the byte-prefix clause as zero deleted base lines, places the SCORECARD block at end of file, reads counter 1 as an end-of-round target. Evidence and red control: `corpus/evidence/round65/a1-prefix-check.txt`.
- Mistakes mined: `corpus/lessons/round-65.md` `## Mistakes` rows 1–7 (see below).
- Wave evidence: `.ufo/waves/round-65/w1-spec.json` (validated; policy `scripts/hyaku/ufo-wave-policy.json`), `w1-dispatch.json`, `w1.ready`, `w1.ready.dispatched`; seat outputs `.ufo/waves/round-65/w1/<Seat>.md` and `w1/<Seat>/`.
- Seat outputs used: GraderRecon (S232/S233 re-open, sha and `cmp` identical), ProbeBuild (probe, receipt, battery, selftest), ErrataBuild (C2 artifacts and S234 checks), KnowledgeDraft and LessonDraft (drafts, reconciled by the L1), SiblingOverlap (`OVERLAP: none`), FreezeReview (F1–F16; verdict `freeze-defective F1,F2`), SourceReview (per-row AGREE on S232/S233/S234), ClaimFalsifier (C1(a)–(e), C2(f)–(i)), ProbeMutate (10 of 10 mutants caught; original probe sha unchanged), ControlOrigin (D1–D4 origins re-derived at `21b13dc7`), SecurityScan (M-1 must-fix; L-1..L-6 notes).

**Verification run at round end** (commit `edbb0bc`, lane tree):
- `python3 plans/round65_c1_sqlite_probe.py --check-receipt corpus/evidence/round65/sqlite-gcov-probe.txt; echo $?` → `CHECK ok cases=5`, `PREDICATE R65-C1 pass`, exit 0.
- `python3 plans/round63_gate_checks.py depth --skill SKILL.md --receipt corpus/evidence/round62/class-survey.txt --root .` → `ROWS n=16 class_match=True count_mismatch=0 paths total=28 resolved=28 share=1.00`, `PREDICATE R63-C2 pass`.
- `python3 plans/round63_gate_checks.py trio corpus/knowledge/tb2-sqlite-gcov-offline.md` → `TRIO pass`; `python3 plans/round64_trio_sweep.py --sweep --lane .` → `PREDICATE R64-C3 pass`.
- `python3 plans/round52_c2_registry.py --lane .` → `PREDICATE R52-C2 pass`.
- `python3 plans/round56_landcheck.py --selftest` → `ALL PASS (7/7)`.
- `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku` → exit 0 (round end; W04 duplicate-URL warnings pre-existing plus S234's expected one).

**Mistakes (mined; full rows in `corpus/lessons/round-65.md` `## Mistakes`).** 1) the freeze's own registry placement made the literal byte-prefix clause unsatisfiable (FreezeReview F1; fixed by A1 with a red control; Q48); 2) a SCORECARD block was specified mid-file against an append-only clause (F2; placed at EOF); 3) an unmeasured zip byte count and two misnumbered grader lines were entered into registry rows (caught before the freeze commit; the check is still open); 4) the round-64 rendered f-string quoted as source (corrected by S234 and the erratum); 5) the text-only receipt checker admits a fabricated receipt (ClaimFalsifier C1(e); sentinel M-1; open); 6) the counter file was authored after the freeze (open); 7) C2 counter 1 at target before the round ended, and token-stuffing survives the four greps (open, named).

## Landed changes

| change | file(s) | commit | LOG/SCORECARD pointer |
|---|---|---|---|
| Freeze: claims doc, controls, S232–S234, wave spec and dispatch | `plans/round-65-claims.md`, `corpus/evidence/round65/*` (controls), `corpus/SOURCES.md`, `.ufo/waves/round-65/w1-spec.json` | `b5032ff8` | `LOG.md` round 65 entry |
| Round landing: probe, receipts, knowledge entry, registry flips, SKILL flip and registration, round-64 corrections, Q47/Q48, lesson, SCORECARD and LOG sections, Amendment A1, wave evidence | `plans/round65_c1_sqlite_probe.py`, `corpus/evidence/round65/`, `corpus/knowledge/tb2-sqlite-gcov-offline.md`, `corpus/knowledge/tb2-kv-store-grpc-offline.md`, `corpus/SOURCES.md`, `corpus/lessons/round-64.md`, `corpus/lessons/round-65.md`, `corpus/QUALITY.md`, `corpus/README.md`, `SKILL.md`, `SCORECARD.md`, `LOG.md`, `plans/round-65-claims.md`, `plans/round54-entrytruth.json`, `.ufo/waves/round-65/` | `edbb0bc0` | `LOG.md` round 65 entry and addendum; `SCORECARD.md` Round 65 section and addendum |

## Before → after measurements

**R65-C1 (coverage, L0-capped; capability acquisition).**
- Before (base `12a62551`): `grep -c sqlite-with-gcov corpus/evidence/round52/graders/executed17.lst` → `0` (rc 1); `CLASS db-state count=2`, executed 0 (`corpus/evidence/round62/class-survey.txt`).
- After (measured commit `edbb0bc0`): `python3 plans/round65_c1_sqlite_probe.py --check-receipt corpus/evidence/round65/sqlite-gcov-probe.txt; echo $?` → `CHECK ok cases=5`, `PREDICATE R65-C1 pass`, rc `0`. Vectors G1 P/P/P, G2 F/F/F, G3 P/P/F, G4 P/P/F, G5 P/P/F — the five frozen. Two live battery runs with identical vectors (`replication-run2-receipt.txt`).
- Score: coverage held 7 (L0 cap `kengaku | round-25/33/51`). Capability `offline-db-state-grader-probe` enters.
- Limit (sentinel M-1, must-fix): the checker accepts a fabricated receipt; `.ufo/waves/round-65/w1/SecurityScan.md` reproduces `rc 0` on `ClaimFalsifier/atk/fabricated.txt`. Not fixed this round: pinning the toolchain values would be a checker tightening after the C1 receipts were scored, which the protocol does not admit as this claim's rule. Routed to round 66 as the first counter amendment, frozen before its wave.

**R65-C2 (calibration; held at ceiling 10).**
- Before (base `12a62551`, `corpus/evidence/round65/c2-before-counters.txt`): `grep -c 'supersedes S230' corpus/SOURCES.md` → `0`; `grep -c 'R64-ERRATUM-65' corpus/lessons/round-64.md` → `0`; `grep -c 'addendum-classified' SCORECARD.md` → `0`; `grep -c 'Q47 —' corpus/QUALITY.md` → `0`.
- After (measured commit `edbb0bc0`): `supersedes S230` → `1`; `R64-ERRATUM-65` → `1`; `addendum-classified` → `4` (2 in the round-64 correction block, 2 in the round-65 section; target ≥1); `Q47 —` → `1`.
- Append-only check, base → landing: `git diff --numstat 12a6255170bcc466029bf82037885fd69e20370f -- corpus/SOURCES.md corpus/lessons/round-64.md SCORECARD.md corpus/QUALITY.md corpus/knowledge/tb2-kv-store-grpc-offline.md` → deleted column `0` for all five (`corpus/evidence/round65/a1-prefix-check.txt`, with a fixture red control `deleted_base_lines=1`).
- Score: calibration held at 10.

## Sources & frontier

- `SOURCES.md` rows before → after (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`): **224 → 227**. Census at round start `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku` → exit 0 (`corpus/evidence/round65/census-before.txt`); at round end → exit 0 (`/fast/scratch/hyaku/kengaku-r65/L1/census-after.txt`, W04 warnings only).
- Status histogram, base → end (`awk` on column 9): `mined=203 queued=8 rejected=13` → `mined=206 queued=8 rejected=13`. Tier histogram at end: `A=198 B=24 C=5`.
- Rows added by tier: **A = 3** (S232 sqlite-with-gcov grader, S233 SQLite amalgamation 3.54.1, S234 kv-store-grpc grader superseding S230).
- Rows touched old → new: S232 `status queued → mined`, `used-by — → corpus/knowledge/tb2-sqlite-gcov-offline.md`; S233 `status queued → mined`, `used-by — → corpus/knowledge/tb2-sqlite-gcov-offline.md`; S230 unchanged (byte-identical base → end); S234 new `mined`.
- Located quotes (URL, access date 2026-11-03, ≤25 words): recorded in `corpus/lessons/round-65.md` `## Gate` (S232 lines 51 and 25; S233 zip listing; S234 line 96).
- Frontier rows advanced: `db-state` class (1 of 2 executed; the first toolchain-artifact member); the R65-C1 knowledge entry cites S232 and S233 (a sourced claim, per §2b.4).
- Lesson: `corpus/lessons/round-65.md` (`## Gate`, `## Mistakes`).
- Corpus curation: `considerthese/2026-10-26.md` — its three "proposals only" items were already implemented (proposal 1 → `plans/routed_open.py`; proposal 2 → the V9 counter and QUALITY Q33; proposal 3 → the round-62 class survey). No still-unimplemented proposal remained; none mined this round.
- Assimilation: none — `merge/kengaku/` package remains blocked by id collisions (114 of 175 rows collide with the lane registry; `.ufo/waves/round-54/assimilation/`); L0 `kengaku | round-54` open. Nothing adopted.
- Frontier step, census before and after: recorded above.
- `PROVINCE.md` not edited: the db-state census note (`PROVINCE.md:907–912`) is a dated round-62 record; the round-65 movement is recorded in SKILL, LOG and SCORECARD.

## Trend verdicts

- **expansion: improved.** One admitted knowledge entry on uncovered ground (`tb2-sqlite-gcov-offline.md`, the first executed `db-state` member, a toolchain-artifact grader), citing mined rows S232 and S233; capability `offline-db-state-grader-probe` enters with its receipt.
- **quality: improved.** A weaker entry superseded by a stronger one: S234 supersedes S230's rendered-quote anchor with the grader's verbatim line (`corpus/SOURCES.md`); the round-64 freshness claims are now qualified (`addendum-classified`); no admitted entry found false.
- **discernment: improved (provisional).** A disagreement from the round-64 outside check (§7.3, lane-base citations) became a grounded QUALITY criterion (Q47, `corpus/lessons/round-65.md`), and the freeze's own defects produced Q48 with a red control. The round-65 outside spot-check has not run: the seats that reviewed this round (FreezeReview, SourceReview, ClaimFalsifier, SecurityScan) are lane-dispatched and are not the outside check. The non-author closure must confirm or overturn this verdict.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md:68–85 (class decision table; db-state row `SKILL.md:83`), SKILL.md registry `:686`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round-65 entry (the grader executed offline: trigger `sqlite-with-gcov` pinned grader → action compile and bwrap battery → outcome `PREDICATE R65-C1 pass` → pointer `corpus/evidence/round65/battery-run.txt`).
- [~] Instructions executable by an agent without oral context — `corpus/lessons/round-8-aggregator-box3-coldrun.md:48` (unchanged pointer; the round-65 probe's counting command is runnable as written: `plans/round65_c1_sqlite_probe.py --check-receipt …`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:130` (`### Adjacent`; the SHONEN.md pointer `PROVINCE.md:129` is unchanged).

No box is marked `[x]`: no non-author verifier has checked the round.

## Open items and routed defects

- **Sentinel M-1 (must fix, routed, not landed):** `--check-receipt` accepts a fabricated receipt; remediation (a) pin `TOOLCHAIN` values and bind the receipt to probe sha `f44b7283…4db4eb`, as the first round-66 counter amendment, frozen before its wave; (b) per-case `.gcda`/`.gcno` hashes, round 66.
- Lesson rows 3, 6, 7 (registry numbers not re-derived by a gate; counter authored after freeze; token-stuffing C2 shape) — routed to round 66.
- Sentinel notes L-1 (bwrap shares the host network namespace; `--unshare-net` is a round-66 hardening candidate), L-2 (canary GUID is benchmark data), L-3 (sibling store paths quoted in wave receipts; no secret values), L-4 (third-party links in the captured download page; no link opened), L-6 (two live receipts with different PIDs and timings; both landed and named).
- L0 question appended: `kengaku | round-65 | …` (see `.ufo/l0-questions.md`): whether a post-score checker tightening may land as a dated amendment, or waits for round 66.
- L0 carried, unanswered: `kengaku | round-25/33/51` (coverage cap), `kengaku | round-56`, `kengaku | round-63` (amended K2 detector), `kengaku | round-54` (assimilation id drift). Nothing assumed answered.

## Round shape and seats

- One v1 wave, `.ufo/waves/round-65/w1`, 12 seats, band 8–16 (`scripts/hyaku/ufo-wave-policy.json`), spawned by the orchestrator in tranches from `w1.ready` (`w1.ready.partial`, then `w1.ready.dispatched`). `WAVE-DONE kengaku r65 w1: all 12 seats settled` received.
- Roles: scout 1 (GraderRecon); executor 2 (ProbeBuild, ErrataBuild); scribe 2 (KnowledgeDraft, LessonDraft); connector 1 (SiblingOverlap); reviewer 2 (FreezeReview, SourceReview); critic 1 (ClaimFalsifier); mutation-tester 1 (ProbeMutate); sentinel 1 (SecurityScan); revenger 1 (ControlOrigin).
- Attack share: reviewer 2 + critic 1 + mutation-tester 1 = 4 of 12 (33%, ≥25%). Connector 1 (≤2). Residual call: none.
- Dead seats: none (12 of 12 settled, each with a seat report). `w1-results.json` records no outputs (`note`: the orchestrator kernel restarted mid-wave; output delivered to the orchestrator session); seat outputs are read from `.ufo/waves/round-65/w1/<Seat>.md`.
- The answering model per seat is not recorded in the results file; the run-15 route map applies (`task.agentModelOverrides`).

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` (no pathspec): no untracked or modified round-65 file at the fleet root; no misroot to copy. Orchestrator-owned markers `.ufo/waves/round-63/w1.ready.dispatched` and `.ufo/waves/round-64/w1.ready.dispatched` are untracked in the lane tree and are not round-65 work.

## Scratch

`$HYAKU_SCRATCH/kengaku-r65` (`/fast/scratch/hyaku/kengaku-r65`) removed after landing; seat scratch dirs were removed by their seats before yield (per the sentinel's scope audit).
