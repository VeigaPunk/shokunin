# tsukuroi — round 27 report (attempt 2, 2026-10-22)

Lane repo `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin`, branch `master`. Pushed lane tip cited by this report: `02996e4c868824a504cd1adb0530e8420fbb997a` (`jj-lane.sh state`: local = remote, ahead 0, behind 0, untracked 0). Claim base `3beab8ddcf4ed2ae9fdf12eab6ac7f840c74e333` (unchanged from attempt 1). Attempt 2 launched 2026-10-22T17:30:06Z (`.ufo/watchdog.log` line `launch tsukuroi round=27 pgid=1002786 driver=hyaku-inline attempt=2`). Attempt 1 ended in the omp process restart at 17:26Z with its lane commits pushed up to `099c7b3f` and no report.

## Work performed

Declared claims (`SCORECARD.md` section "Round 27 — declaration, attempt 1", commit `db9eecfa`, refined before measurement in `099c7b3f`; unchanged by attempt 2):

- **C1 — depth (tied lowest at 8), learning claim, sourced S140 to S145:** kernel-taint entry `corpus/knowledge/kernel-taint-r27.md` and `.json`, rows KT1 to KT6 (how this host's taint value 12288 decodes, when O and E are set, why a signed DKMS module still sets E, the per-module taint file, persistence, bug-report meaning). Counting command `python3 tools/check-kernel-taint.py --revision <REV>`, field `verified_rows`; declared after-value 6. The declaration's "new PROVINCE frontier area" wording is withdrawn (deeper ground inside the driver and firmware Core area).
- **C2 — adjacency (tied lowest at 8):** overlap register `corpus/knowledge/adjacency-mori-oom-r27.md` and `.json`, rows OV1 to OV6, against mori's admitted `userspace-oom-killers-r26.md` at mori `ef9dbee1`. Counting command `python3 tools/check-adjacency-overlap.py --revision <REV>`, field `anchored_rows`; declared after-value 6.

Calibration is not claimed (third claim in a row avoided, per the session note).

Work items, attempt 1 (inherited, re-verified by attempt 2 and by wave-2 seats):

- Capture, sources and snapshots: `.ufo/waves/round-27/capture/capture.txt` (sha256 `88d02d98…7841`); S140 to S145 re-fetched by wave-2 RevSrcS140 to RevSrcS145, all six hash to their anchors (`.ufo/waves/round-27/w2a2/RevSrcS14*.md`).
- Counters committed before data: C1 `75f410c8` → data `b1647ff2`; C2 `dd94cb1f` → data `75784ea4`. Byte identity at the tip confirmed (`git diff --quiet` exit 0 for both; wave-2 RerunC1, RerunC2).
- Round-26 spot-check routed defects 1 to 5 (`corpus/lessons/round-26-verifier-spotcheck.md:112-118`): commits `4c487fc9`, `5583d75c`; dispositions in `corpus/lessons/round-27.md:37-46`, corrected by attempt 2 at `corpus/lessons/round-27.md:62-69` (see below).

Work items, attempt 2:

- Re-measured at the inherited tip before any change: C1 6 exit 0, C2 6 exit 0, four selftests exit 0, census exit 0 (`.ufo/waves/round-27/measure/a2-start/`, commit `2e519d61`).
- Falsify wave w2a2, 44 seats, every item naming what it attacks (`.ufo/waves/round-27/w2a2-spec.json`, `w2a2-dispatch.json`, 44 reports in `.ufo/waves/round-27/w2a2/`).
- Routed defect 5 (the "tooling-directive append" defect), cause located: the L1 payload equals the validated `taskCall`; the host task tool appends the 996-byte `~/.omp/agent/RULES.md` block to every seat text (77 of 77 recorded seat texts; `w2a2/RevDispatchFidelity.md`, `w2a2/RevDispatchFidelityA2.md`). The lane cannot change host injection; L0 question filed. Defect 2's undisclosed re-measure (7 of 27 at `099c7b3f`) and defect 1's residual SH6 phrase are now recorded and repaired (`corpus/lessons/round-27.md:62-69`).
- Harm found by wave 2 and repaired: registry-coverage gate FAIL at `099c7b3f` (2 missing rows, `measure/a2-start/registry-099c7b3f.json`) → `SKILL.md:2438` round27 registry table, 31 of 31; round-26 axes table 5 stale counts → `SCORECARD.md:1021` round-27 axes table (ordinals unchanged); OV5 and one SH6 withdrawal missing from JSON companions → `corrections_r27` markers in `memory-pressure-r25.json` and `storage-health-r26.json`.
- C1 entry corrections from row reviewers RevRowKT1 to RevRowKT6, CritC1Learning, RevSkillKernelTaint: KT6 verdict split (`.md` DEGRADED vs JSON and SKILL HEALTHY) corrected in place and disclosed; KT1 to KT6 narrowed branches and unmarked inferences corrected by appended section "Wave-2 corrections" and JSON `corrections_r27_a2` (`kernel-taint-r27.md`, commits `a99d9e8b`, `0c5e3006`).
- C2 register corrections (ConnMoriHeadDrift, CritClaimSizingFinal, CritC2Tool, RevRowOV6): OV6 line 196→198, "pointers replayed" narrowed to OV1 and OV2, sibling-availability behaviour disclosed, mori HEAD `df886be1` observation (`adjacency-mori-oom-r27.md` appended section).
- Lesson section "Attempt 2" with six Mistakes rows (`corpus/lessons/round-27.md:85`), QUALITY 70 to 72 (`corpus/QUALITY.md:138-140`), `SCORECARD.md:1034` measured outcome and `:1045` falsify-wave outcome, LOG entry `LOG.md:1241`.

## Landed changes

Every commit carries `tsukuroi-shokunin <tsukuroi@shokunin.local>` and was landed by `jj-lane.sh` with remote verification (`landed <hash>`).

| Commit | What | LOG.md entry |
|---|---|---|
| `db9eecfa876a865f799aa56856a780d299b4f067` | Declaration, frozen capture, mori snapshot, census before (attempt 1) | "Round 27 — kernel taint entry and mori overlap register" (`LOG.md:1231`) |
| `75f410c825a941f819717e4183bcc82f9c368469` | C1 counter before data | same |
| `b1647ff2e332128b2dfe8bf7d7ab22ed16f6205e` | C1 entry, S140-S145, Gate, SKILL section, README row | same |
| `4c487fc9fc4ee7bf9e9b522bbba2de5807f5f0cf` | Routed defects 1 and 3 | same |
| `dd94cb1f3d514a2eaf1fca86f3e1ce1b283c14ad` | C2 counter before data | same |
| `75784ea465e0773a985b4920ecd60a1bb1a69a3f` | C2 register, PROVINCE section, OV5 notice | same |
| `5583d75c9f354bc5e116b68d8b8997d8c742d0a9` | Routed defect 2 (QUALITY 65) | same |
| `099c7b3f42d073203d9448807860f04c175eccd7` | Declaration refinements, QUALITY 67-69, wave-1 evidence, attempt-1 wave-2 spec | same |
| `2e519d615135ba3b3d60dcd19a5642dc0d4391f9` | Attempt 2 start: inherited leftover, re-measure, w2a2 spec/dispatch/registry | "Round 27 — attempt 2: falsify wave and repairs" (`LOG.md:1241`) |
| `a99d9e8b303e6359d91ff10164e76ad14328aed7` | Wave-2 repairs, registry table, axes table, outcome sections, lesson, QUALITY 70-72, 42 wave-2 reports | same |
| `0c5e3006c392b3e1820f37992a6d34b22702533e` | KT4 further correction, last two reports, receipts at `a99d9e8b` | same |
| `02996e4c868824a504cd1adb0530e8420fbb997a` | Final receipts at `0c5e3006` | same |

Inherited state: the one untracked attempt-1 path, `.ufo/waves/round-27/w2/swarm-registry.json` (36 members, every agent id null, no report anywhere; wave-2 RevInheritA1), was re-verified and committed as evidence in `2e519d61`. Nothing was reverted. Files not authored by this lane were not edited: `corpus/lessons/round-26-verifier-spotcheck.md` (read only).

## Before → after measurements

| Claim | Command | Before at `3beab8dd` | After | Measured revision | Author verdict |
|---|---|---|---|---|---|
| C1 | `python3 tools/check-kernel-taint.py --revision <REV>` → `verified_rows` | exit 2, `KT-CAPTURE-MISSING`, 0 (`measure/c1-3beab8dd.json`) | exit 0, 6 of 6 | `b1647ff2`, `099c7b3f`, `a99d9e8b`, and final `0c5e3006` (`measure/a2-final2/c1.json`) | Declared target met. The count proves complete evidence links, not true statements: KT3 counts as `UNVERIFIED`, and wave-2 found narrowed branches in every row, now corrected by appended sections. Counter rule gaps disclosed (CritC1Tool; MutC1Counter 27 of 30 rule mutants killed). |
| C2 | `python3 tools/check-adjacency-overlap.py --revision <REV>` → `anchored_rows` | exit 2, `register-missing`, 0 (`measure/c2-3beab8dd.json`) | exit 0, 6 of 6, `sibling-verified` | `75784ea4`, `099c7b3f`, `a99d9e8b`, and final `0c5e3006` (`measure/a2-final2/c2.json`) | Declared target met as a count of anchors only. The pinned counter also scores 6 on 19 of 24 should-fail register mutants (CritC2Tool; MutC2Counter 21 of 44 killed); the live rows use none of those shapes, and class and owner rest on RevRowOV1 to RevRowOV6 (OV1, OV2, OV3, OV5, OV6 hold; OV4 holds with a corrected bookkeeping claim). It counts 0 when a mori checkout lacks `ef9dbee1`. |

Tool bytes at the measured revisions equal the pins (`git diff --quiet 75f410c8 <REV> -- tools/check-kernel-taint.py` and `dd94cb1f` for C2, both exit 0). Other gates at `0c5e3006`: self-assessment 0 of 27 (7 at `099c7b3f`; not a claim, repair of harm), registry-coverage PASS 31 of 31 (FAIL 2 missing at `099c7b3f`), memory-pressure 6, storage-health 6, five selftests exit 0, QUALITY 71 verdict-agreement command prints `[]` (`['KT6']` at `099c7b3f`) (`measure/a2-final2/`). No ordinal changed; no capability entered the table.

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`.

- Round start (attempt 1, `.ufo/waves/round-27/census-before.txt`): exit 0, `tsukuroi ok`, 25 W04 warnings, 139 rows.
- Round end (at `0c5e3006`, `.ufo/waves/round-27/measure/a2-final2/census.txt`): exit 0, `tsukuroi ok`, 25 W04 warnings (none new; ScoutCensus), 145 rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Frozen manual census (wave-2 ScoutCensus): malformed 0 → 0; tiers A/B/C 129/3/7 → 135/3/7; statuses mined/queued/rejected 125/5/9 → 131/5/9; no duplicates, no enum breaks, no missing used-by paths.
- Rows added by tier: 6, all tier A, all `mined`, opened 2026-10-22, recheck `on-release`: S140 to S145 (Linux v7.2 `tainted-kernels.rst`, `panic.c`, `panic.h`, `module/main.c`, `module/signing.c`, `module-signing.rst`); Gate in `corpus/lessons/round-27.md:7-35`.
- Rows touched old → new: none (no `status`, `recheck` or `used-by` change). Teaches-cell incompleteness found by wave 2 for S143, S144 and S145 is recorded in the entry's appended corrections, not by editing the rows.
- Frontier advanced: deeper ground inside the driver and firmware Core area (mechanism, decoding, per-module reading, persistence, operator actions); no new PROVINCE frontier paragraph. Sibling adjacency source opened: mori `corpus/knowledge/userspace-oom-killers-r26.md@ef9dbee1` (snapshot `.ufo/waves/round-27/siblings/mori/…`, sha256 `a5368ee7…0b29d`), used by C2 as an adjacency import, not absorbed.
- Sourced claim: C1 rests on S140 to S145.
- Mistakes mined: attempt 1 R27-COMPANION-UNSWEPT, R27-DECLARED-FRONTIER-OVERCLAIM, R27-CHECKER-DOC-LAG, R27-SEAT-SUDO-SCOPE, R27-WAVE-DEAD-ROUTE; attempt 2 R27-REGISTRY-ROW-MISSING, R27-OWN-COMPANION-RULE-BROKEN, R27-COUNTER-PERMISSIVE, R27-SIBLING-POINTER-DRIFT, R27-HOST-APPENDED-DIRECTIVE, R27-INHERITED-WAVE-LOST (`corpus/lessons/round-27.md:48-56,85-94`). QUALITY 70 and 71 have red-to-green controls (registry 2 missing → 0; verdict agreement `['KT6']` → `[]`).

## Trend verdicts

- **expansion: unchanged.** The taint lines were already in `driver-firmware-plane.md:101-106` and `SKILL.md:49` at the base; C1 deepens existing Core ground, and Linux kernel source rows existed before (wave-2 CritTrendVerdicts). The register adds an adjacency record, not new domain ground. `verified-at:` lines were added to both new entries, so admission does not breach QUALITY 8.
- **quality: improved (provisional, owed to the outside spot-check).** Earlier admitted entries were re-verified or superseded with sourced statements: the driver-firmware note's "unsigned" reading is superseded and its two taint journal lines are re-observed at capture lines 136-137; the `memory-pressure-r25` `--kernel-oom` exception is withdrawn by OV5 in both `.md` and JSON; the storage JSON carries six correction markers. The new entry itself needed wave-2 corrections; each is appended and none is left false and unmarked that wave 2 found.
- **discernment: improved (provisional).** Wave-2 disagreements became six Mistakes rows and QUALITY 70 to 72; QUALITY 69 now has its lesson row (R27-SIBLING-POINTER-DRIFT); the overstated routed-defect dispositions are corrected in the lesson. Limit: the Gate records six admits and no reject, so an outside check cannot sample a reject this round.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SHONEN.md` box 1 evidence line; `SKILL.md:2420` kernel-taint table and error patterns (S140-S145), `SKILL.md:2438` round27 registry; no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:1231` (capture → entry → operator actions for taint) and `corpus/knowledge/host-health-report-r3.md`.
- [~] Instructions executable by an agent without oral context — `SHONEN.md` box 3 evidence line; KT4's signal command needed a fix (`SKILL.md` round-27 wave-2 note); whole-SKILL retest not run.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` section `## Adjacent — mori userspace OOM killers (round 27)`; register reports, never absorbs (RevRowOV1 to RevRowOV6).

## Round shape, seats and process

- Shape: default two v1 waves (policy `scripts/hyaku/ufo-wave-policy.json`). Wave 1 build (attempt 1): 33 seats (19 scribe, 4 executor, 4 reviewer, 3 critic, 2 connector, 1 scout); 23 dead at spawn (every scribe and executor, "Error: No model selected."). Wave 2 falsify (attempt 2): 44 seats (30 reviewer, 8 critic, 4 mutation-tester, 1 connector, 1 scout); 0 dead, 0 refusals, 44 reports. Round total of the two waves: 77. Attack roles (reviewer, critic, mutation-tester) 7 + 42 = 49 of 77. No residual call.
- Lost wave: attempt-1 wave 2 (36 seats: 27 reviewer, 7 critic, 1 connector, 1 scout) was dispatched at 17:13Z and lost to the 17:26Z omp restart with no report; its seats were never resumed or messaged. Counting it, 113 seats were dispatched for round 27 across both attempts.
- Planner seat: held by the L1 (the validator rejects `planner`).
- Seat gate: `wave-slot.sh acquire tsukuroi tsukuroi-r27-a2-w2 44 3600` granted at 17:46:00Z (live 10, cap 85); released after all 44 seats returned. No job-cap refusal.
- Routing: no `model` passed. Answering models self-reported in wave 2: zai/glm-5.3-flash (11), devin/swe-2 (12), minimax-code/MiniMax-M3.1-Flash (3, the restored m_mim route: all three mutation testers that named a model), opencode-go/deepseek-v4.1-flash (1), Cursor Auto (2), not exposed (15). No claim depends on a seat's model.
- Payload: the validated `taskCall` context and tasks were passed unchanged plus one `solutionSpace` string per task; the host appended the RULES.md block (see routed defect 5).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists untracked fleet-root files (`MANPAGE.md`, `base.c`, `main.c`, `meminfo.c`, `oom_kill.c`, `sd-main.c`, `user@.service.in`, `nama.html`, `live_s228.html`, `tf_bavelas.html`, `.ufo/reports/round-31/kake.md`); none names tsukuroi or round 27 (grep exit 1; wave-2 RevSeatScope), so none was moved. The staged `write` file predates the round.
- Cross-lane items for mori (reported, not absorbed; wave-2 ConnMoriHeadDrift, CritC2Adjacency, RevRowOV4, RevRowOV5): (1) mori `PROVINCE.md:66` should point at tsukuroi `PROVINCE.md:30-33,44-53`; (2) mori `SKILL.md:345` should point at tsukuroi `PROVINCE.md:28`; (3) the r26 entry's F8 sentence lacks the `OOMRules=` and `systemd-oomd.socket` qualifiers (OV4); (4) source row S133 and entry lines 289-290 say oomd monitors "only" `kill` units, but systemd v262 also monitors `OOMRules=` units; (5) mori's r12 entries (`oom-kill-counter-kernel-only-r12.md` lines 14, 21, 30; `userspace-oom-killers-r12.md:13`) still present `--kernel-oom` as a live exception, contradicting mori's own F7 (OV5).
- Lane debt owed (recorded in `corpus/lessons/round-27.md` "Owed lane debt"): MP4 qualifier in `SKILL.md:2316` and the MP4 JSON action; mori's correction of the "+200 band" reading; `driver-firmware-plane.md:276` `[unk]`; further unmarked storage JSON statements; C1 and C2 counter rule gaps; three self-assessment selftest cases and its hyphenated-heading gap.
- Snapshot-boot premise P3 and the update-safety gate: operator-owned; nothing lifted, no package transaction (the pacman pause holds).
- Installs: none by the L1; all 44 wave-2 seats reported `Installs: none`.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open; this mission is progressing (four lane-authored commits in attempt 2 after eight in attempt 1).
- L0 questions: one opened this round (`.ufo/l0-questions.md`, `tsukuroi | round-27 | …`): which text binds seats when the host appends RULES.md (pacman-first) after the validated taskCall while the pacman pause holds.
