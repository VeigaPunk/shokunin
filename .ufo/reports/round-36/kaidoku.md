# kaidoku — round 36 report (fresh-start round, hyaku run 8)

L1 `KaidokuR36` (holds the §3 planner seat). Lane `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, branch `main`.
Base `cab59f221fe19726b5692bfa4d9a9679e96b8a73` → final lane hash in **Landed changes**. Fresh-start: the previous three
closures were rejected (`corpus/lessons/round-3{3,4,5}-verifier-spotcheck.md` read first); both claims were scored
against do-nothing/skip controls with their frozen counters before any claimed data existed.

## Work performed

Declared claims (2): **R36-C1 — coverage**: sasquatch SquashFS recursion moves from the PROVINCE Frontier bullet into
`## Round-36 additions to Core` (REA `extract-firmware`, rea-agents 6.5.0, unblob 26.6.4, four frozen carriers).
**R36-C2 — calibration**: mismatches between the self-assessment surfaces (SCORECARD `## Owned axes` / `## Capabilities`
rows, SHONEN boxes) and observed repo state, 3 → 0. Lowest-axis rule: owned axes tied at 10, C1 works coverage.

- Claims, predicates, counters + selftests (C1 14 cases, C2 13), carriers, `unsquashfs` oracle and before receipts frozen — `790561d4` (`plans/round-36-claims.md`).
- Seven controls scored with the frozen counters before data, all exit 1 for their intended guard — `6a870b92` (`.ufo/waves/round-36/controls/`); re-derived 7/7 by `w1/R36ReviewerControls.md`.
- sasquatch 4.5.1 installed from the official deb (after the controls), C1 after receipts on K1–K4 — `3310d8fa` (`corpus/evidence/round-36/c1/K*/after.json`).
- C2 repairs (coverage row restated; `receipts-B/` and `ScoutSkillPlacement.md` repaired by document) — `d2e46ef5`; counter green there before any C1 entry existed (`.ufo/waves/round-36/c2/after-at-d2e46ef5.json`).
- C1 landing: entry `corpus/knowledge/2026-10-26-r36-sasquatch-squashfs-recursion.md`, S107–S109, PROVINCE Core row + Frontier note + dated Adjacent tooling bullet, README rows, SKILL decision table + eight-field instrument registry — `ffc81341` (`.ufo/waves/round-36/after/c1-at-ffc81341.json`).
- Assimilation (theme sasquatch/unblob, `merge/kaidoku`): 1 entry admitted with corrections (`corpus/knowledge/2026-10-26-unblob-sasquatch-dependency.md`, S110/S111 renumbered by document), 3 refused — `ffc81341`; gate in `corpus/lessons/round-36.md` `## Gate`.
- Lesson M36-1..M36-7, QUALITY 77–78, SCORECARD round-36 section + capability row, LOG, routed-defect corrections (r34 D-2/D-3, R35-D1..D5) — `01a44dbf`.
- Wave-2 corrections (assimilated entry scope/attribution, S107 asset set, S111 teaches, quote count, dated pointers on superseded lines) — `38c1a8be`; r4u-03 supersession note — `2618cf07`.
- Independent evidence: four carrier reproductions (`w1/R36ExecReproK{1,2,3,4}.md`), a fresh-download K3 reproduction (`w2/R36W2ExecReproFresh.md`), K3 second oracle via the AppImage runtime's own `--appimage-extract` 2130/2130 (`w1/R36ExecAppImageExtract.md`), evidence-id recompute 0 mismatches by three routes (`w1/R36ExecEvidenceIds.md`).

**Findings against the round, disclosed (frozen bytes not changed):** C1's counter checks receipt integrity, not provenance — an
oracle-copy envelope re-hashed with REA's digest code scores green (`w1/R36CriticC1Shortcut.md` F1; such envelopes fail REA's own
`parseEvidence`, `w2/R36W2CriticC1Verdict.md`); C2's counter admits shadow rows, second statements, same-basename decoys, population
shrink (`w1/R36CriticC2Shortcut.md` A1–A6); mutants alive C1 2/10, C2 7/14 (`w1/R36MutantC1.md`, `w1/R36MutantC2.md`); predicate-identity
divergences (`w1/R36CriticPredicateIdentity.md`); own-QUALITY rows not met by the instruments: 33, 39, 45, 58, 60, 68 (`w1/R36ReviewerQualityBar.md`).
Routed as QUALITY 77/78 and lesson M36-3/M36-4/M36-6.

## Landed changes

| commit | what | LOG |
|---|---|---|
| `790561d4e3aca732a434081aa9573ec2fa5fd7d0` | freeze | LOG.md `## 2026-10-26 — round 36` bullet 1 |
| `6a870b9290e9566468d7d9e6d1b8308daf025b12` | control receipts | bullet 1 |
| `3310d8fa27bfaa95ad858c4aaad6f6377f853982` | C1 after receipts | bullet 2 |
| `d2e46ef5e2b2e8ba681b2fa55d50f298c4c4b8be` | C2 repairs | bullet 3 |
| `ffc813417d3bceeeb7b028b12ce0be8a5dc33d95` | C1 landing + assimilation | bullets 2, 5 |
| `01a44dbf45913a1bdcabbbfb85b7bb9d232cb930` | lesson, QUALITY, SCORECARD, LOG, routed corrections, wave-1 reports | bullets 4, 6 |
| `6f2ba761bb5bcd6482d45523379376dcb6a386f6` | wave-1 results (43/43), wave-2 spec | bullet 4 |
| `38c1a8be78906b1b031eb2035766d9f24d22f0d7` | wave-2 corrections, final receipts | bullet 4 |
| `2618cf0726d8a96360e489482b29ad4cfd455199` | r4u-03 supersession note, census end | bullet 6 |
| `a6c433b545fa57eac3426cd6c234d2d76f18c51d` | wave-2 adjacency fix (tsukuroi update-safety gate clause in the Adjacent tooling bullet), two shorthand pointers expanded | bullet 4 |
| `018ae62889cb0717be5a02a8bb74de055bd104cf` | wave-2 results (36/36), final receipts `.ufo/waves/round-36/after/c{1,2}-final.json` (C1 exit 0, C2 0 mismatches at `a6c433b5`) — **final lane hash, pushed** (`git ls-remote origin refs/heads/main` → `018ae628…`) | — |

## Before → after measurements

- **R36-C1** — `python3 -I -B tools/round-36/c1-counter.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --rev <REV> --freeze 790561d4e3aca732a434081aa9573ec2fa5fd7d0 --pkg65 /home/vgpnk/.npm/_npx/ad9a3fdbcad992c6/node_modules/rea-agents`. Before at `cab59f22`: `carriers_matched 0`, bindings false, exit 1. After at `ffc81341` (and again at `38c1a8be`, `.ufo/waves/round-36/after/c1-final.json`): `carriers_matched 4` (K1 3/3, K2 4/4, K3 2130/2130, K4 2130/2130), all five bindings true, `met_target true`, exit 0. **Verdict: met under the frozen rule; provenance by independent reproduction (QUALITY 78).**
- **R36-C2** — `python3 -I -B tools/round-36/c2-counter.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --rev <REV> --base cab59f221fe19726b5692bfa4d9a9679e96b8a73`. Before at `cab59f22`: 3 mismatches, exit 1. After: 0, `guards_ok`, exit 0 at `d2e46ef5` (before C1), `ffc81341`, and `38c1a8be` (`.ufo/waves/round-36/after/c2-final.json`). **Verdict: met under the frozen rule; the counter's blind spots (QUALITY 77) mean the closure should check the actual diff `git diff cab59f22 <final> -- SCORECARD.md SHONEN.md`, which edits the existing rows in place (no duplicate units).**
- No axis harmed: coverage proxy 122/122 → 124/124, depth 17/17 unchanged, calibration 3 → 0; owned scores 10 → 10.

## Sources & frontier

- Census start (`.ufo/waves/round-36/census-start.txt`, before any registry edit, at `cab59f22`): `kaidoku ok`, 9 × W04, **exit 0**, 106 rows. Census end (`.ufo/waves/round-36/census-end.txt`, `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`): `kaidoku ok`, same 9 × W04, **exit 0**, 111 rows.
- Rows added (5, all `mined`, opened 2026-10-26): tier A — S107 (sasquatch release), S108 (unblob squashfs.py @26.6.4), S109 (neovim v0.12.6), S110 (unblob README @26.6.4, assimilated); tier B — S111 (devttys0 sasquatch README, assimilated). Rows touched old→new: none (no existing status/recheck/used-by cell changed). Rejected: AppImage Specification as authority for the offset rule (lesson `## Gate`).
- Frontier advanced: PROVINCE Frontier `sasquatch` → Core for LE SquashFS v4; big-endian/AVM stays Frontier. Sourced claim: C1's entry cites S107–S109.
- Assimilation: theme sasquatch/unblob; id lists `.ufo/waves/round-36/assimilation/{reg-ids (106), staged-ids (132)}`, collisions **1 (`S106`, different documents)**, guard proof `S002`; renumber map staged S106→S110, staged S107→S111 (by document); 1 admit, 3 refuse; scratch-mirror census exit 0 before append. Quarantine slice 5 rows re-checked, none appended. `considerthese/`: absent in this lane.
- Mined mistakes M36-1..M36-7 in `corpus/lessons/round-36.md` `## Mistakes`.

## Trend verdicts

- **expansion: improved** — two entries on ground the coverage map did not hold (it said "recursion blocked by missing sasquatch"), each citing mined rows; Frontier area entered; capability row added.
- **quality: improved** — the 2026-10-13 sasquatch-blocked statements are superseded by a measured entry with dated pointers on each superseded line (`2618cf07`, `38c1a8be`), the r34b entry's provenance trio re-verified; the assimilated entry was corrected before it stands (wave-2 `R36W2CriticTrends.md` rated the pre-correction state `harmed`; both legs it named were repaired in-round).
- **discernment: unchanged** — no non-author spot-check exists yet (wave seats are the lane); gate decisions and QUALITY 77–78 await the closure.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — new round-36 decision table + registry (`SKILL.md` `## SquashFS recursion through sasquatch — round 36`); no non-author verifier yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — REA `extract-firmware` on four carriers, LOG.md round-36 bullet 2, receipts `corpus/evidence/round-36/c1/`.
- [~] Instructions executable by an agent without oral context — the recheck command and harness reproduced by five seats (`w1/R36ExecReproK*.md`, `w2/R36W2ExecReproFresh.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:97-125` incl. the dated tooling bullet; sibling scan `w1/R36ConnSiblingOverlap.md` found no contested ground.

## Round shape, seats, extras

- Shape: two v1 waves. **w1 43 seats** (executor 12, scribe 8, scout 7, reviewer 5, critic 4, connector 3, mutation-tester 2, sentinel 1, revenger 1): 43/43 settled, 0 dead (`w1-results.json`). **w2 36 seats** (executor 9, reviewer 8, critic 8, scout 5, connector 3, mutation-tester 2, sentinel 1): 36/36 settled with output, 36 reports, 0 dead (`w2-results.json`). Wave-2 still-open findings, disclosed not repaired: 12 of 17 extra skip controls stay green on the frozen counters (`w2/R36W2CriticDoNothing.md`), the C2 ruling is "verified for the enumerated conditions, not for the sentence's universal lead-in" (`w2/R36W2CriticC2Verdict.md`), C1 "verified, but not by its counter" (`w2/R36W2CriticC1Verdict.md`). Round total 79. No residual call. Planner seat held by the L1. Scratch `/fast/scratch/hyaku/kaidoku-r36` removed.
- Tool installs: sasquatch + sasquatch-v4be 4.5.1 — official GitHub release `sasquatch-v4.5.1-6` deb (sha256 `efbc92bd…ade95`) → `~/.local/bin`; reason: unblob's SquashFS extractor dependency (R36-C1). No pacman.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` — no file from this round's seats (untracked items are orchestrator/older: `.scratch/`, `.tower/`, `.ufo/state/*`, `.ufo/waves/round-30/`, `demo-cwd.txt`).
- Inherited state: lane clean at start; no earlier attempt of round 36.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Open L0 questions: none added.
