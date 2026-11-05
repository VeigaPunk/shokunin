# kagi — round 38 report (attempt 1)

Lane `kagi` (secrets & vault ops; axes freshness + calibration). Lane tip at close: `88374f9539e741cbc6e07505f4c09e42472ee8d1` (`git ls-remote origin refs/heads/master` equals it; `jj-lane.sh state` shows `local=remote`, `ahead=0 behind=0`). Round-38 commits: predeclaration `8c48b7df71066b969ac078205b5ed18cf5f53286`, plan `289e8082ef80e9e14694fcf68f1296bfff26ad9d`, candidate `b94473505e6239cee0073d5be7a1c6f2ee07f564`, close `88374f9539e741cbc6e07505f4c09e42472ee8d1`.

## Work performed

Declared claims (2), both frozen in `plans/round-38.md` before any candidate data:

- **C1 — freshness.** Located-quote gate over committed capture bodies: `bash plans/round-38-c1.sh` 0 → 5 (target 5; claim BASE `a916f4a` reads 0). Verdict: **REPRODUCED** at the candidate (wave: K38ExecQuote, K38CriticClaims).
- **C2 — calibration as declared; operability as measured.** Lane-tree write guard: `bash plans/round-38-c2.sh` 0 → 3 (target 3; BASE 0; do-nothing control 0). Verdict: **REPRODUCED as a runnable guard**; the wave's critic (K38CriticClaims F8) showed that the counter measures operability, so the calibration reading is **withdrawn** and the move is recorded as operability. No calibration score moved.

Work items (evidence pointers):
- Protocol and fleet load: `skill://shokunin`, `skill://swarm`, `skill://godspeed`; `/home/vgpnk/Projects/kimi-shokunin/skills/shokunin/protocol/` (MISSION, AXES, CORPUS, LEARNING); lane SCORECARD, PROVINCE, SHONEN, QUALITY; round-37 spot-check (`corpus/lessons/round-37-verifier-spotcheck.md`).
- START census before any work: fleet `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi` exit 0; lane `bash corpus/sources-census.sh` → `SOURCES_CENSUS: CLEAN (rows=91 … captures=91 …)` (`.ufo/waves/round-38/controls/start-census-fleet.txt`, `start-census-lane.txt`).
- Claim BASE measured on `a916f4a` with the frozen counters copied in: C1 0, C2 0; the round-36 counter 3 (SD5=3, stale 0).
- Predeclaration `8c48b7df` (`.ufo/waves/round-38/controls/`, `.ufo/waves/round-38/capture/`): instruments `corpus/quote-locate.py`, `corpus/laneguard.sh`; counters `plans/round-38-c1.sh`, `plans/round-38-c2.sh`; controls `plans/round-38-controls.sh`, `plans/round-38.controls.tsv`; generator `plans/round-38-rows.py`; captures of `https://github.com/hashicorp/vault/releases/tag/v2.2.1` and `https://github.com/openbao/openbao/releases/tag/v2.7.2`.
- Pre-freeze gate over the predeclaration: `PREFREEZE: CLEAN (controls=7 mismatch=0)`, `.ufo/waves/round-38/controls/prefreeze-gate.txt`. Forgery controls: quote 4, bytes 4, registry 4; positive 5; do-nothing 0 (C1); positive 3, do-nothing 0 (C2).
- Live re-observation 2026-11-05 (`.ufo/waves/round-38/controls/observe-r38.json`): 30 of 30 clock records equal the pinned round-36 receipt on version, verdict, located flag, HTTP status, sha256 and URL. The new receipt is **not** a usable pin (run as `--receipt` it gives 30 `RECEIPT-MISMATCH`, `FAILED`, exit 1, because the bound rows carry `observed_at` 2026-11-04); recorded as evidence only.
- Frozen plan `289e8082` committed alone.
- Candidate `b944735`: S092 and S093 registry and capture rows; `corpus/quote-bodies.tsv`; ledger migrations and R38-01..R38-04; prose rebinding of the claim-row and stamp counts in SKILL.md, PROVINCE.md and `corpus/README.md`; QM38 and QM39; SKILL gate rows; SCORECARD and LOG round-38 sections; two capability rows.
- Wave `build` (one v1 wave, 10 seats, validated under `scripts/hyaku/ufo-wave-policy.json`, dispatch `.ufo/waves/round-38/build-dispatch.json`, results `.ufo/waves/round-38/build-results.json`). All settled; none dead. Seat verdicts are in `corpus/lessons/round-38.md` §Wave settlement and in `.ufo/waves/round-38/build/<seat>/report.md`.
- Wave-driven corrections (critic and scout), committed in the close: the R37-V2 sentence "re-pointing only the id leaves the gate CLEAN" was wrong for the full re-point (FAILED, 10 DERIVATION); the round-36 counter reading 6 at BASE was wrong (3 at `a916f4a`; 6 appeared only after this round's own claim-row edit); the live receipt was quoted selectively; the M38-2 `git grep` list was stale; the R38-03 verdict row was cited as passing while POLICY; C2 was relabelled as operability; three ledger rows (`R12-03`, `R24-05`, `R24-14`) that passed at BASE failed after the round's own stamp and id growth and were migrated; two inherited reds (`R13-01`, `R24-06`, round-37 headings) were migrated with the cause stated.
- R37-V2 measured in scratch (scout and critic independently): `corpus/lessons/round-38.md` §R37-V2.
- L0 question appended and fleet-committed: `kagi | round-38 | …` for the R38-03 script allowlist (`0a1c648b`, fleet repo).
- Tool installs: none. pacman untouched (host pause respected). No git or jj mutation by any seat.

Routed to round 39 (not claimed; recorded in the lesson with red witnesses): R37-V4 (anchor immutability; `2.2.10` boundary); the quote gate's frozen-counter gaps (body symlink followed out of root, V2 — the committed tree has no symlink, all five bodies are mode 100644; superscript-digit traceback, V5; duplicate ids, V1/V4/V6); the surviving mutants M2, M3, M5, M6 (quote) and G3 (guard); the guard's documented `run LANE -- CMD` form (rejected; implemented form `run -- LANE -- CMD`) and its `git diff` index stat refresh.

## Landed changes

| Change | Where | Commit |
|---|---|---|
| Predeclaration: instruments, frozen controls, captures, live receipt, START census | LOG.md `## Round 38` (line 1733) | `8c48b7df71066b969ac078205b5ed18cf5f53286` |
| Frozen plan (claims, predicates, kill rules) | LOG.md line 1734; `plans/round-38.md` | `289e8082ef80e9e14694fcf68f1296bfff26ad9d` |
| Candidate: S092/S093, manifest, migrations, QM38/QM39, SKILL rows, capability rows, SCORECARD and LOG sections | LOG.md line 1735 | `b94473505e6239cee0073d5be7a1c6f2ee07f564` |
| Close: wave evidence (10 seats), lesson corrections, SCORECARD and LOG corrections, ledger migrations R12-03/R24-05/R24-14/R13-01/R24-06, stamps | LOG.md lines 1737–1743 | `88374f9539e741cbc6e07505f4c09e42472ee8d1` |
| Fleet L0 question (R38-03 script allowlist) | `.ufo/l0-questions.md` line 327 (fleet repo) | `0a1c648b84108adb33888c47377b909d97ea9f3d` |

## Before → after measurements

Counting commands are run at the working tree whose content equals the named commit (the close commit adds no measured bytes beyond it).

| Claim | Command | Claim BASE `a916f4a` | Candidate `b944735` | Close `88374f9` |
|---|---|---|---|---|
| C1 located-quote count | `bash plans/round-38-c1.sh` | 0 (no manifest) | 5 | 5 |
| C1 gate verdict | `python3 -I -B corpus/quote-locate.py` | absent | `QUOTE_LOCATE: CLEAN located=5 rows=5`, exit 0 | same |
| C2 detected planted writes | `bash plans/round-38-c2.sh` | 0 (no guard) | 3 | 3 |
| C2 selftest line | `bash corpus/laneguard.sh --selftest` | absent | `LANE_GUARD_SELFTEST: detected=3 mutants=3 clean=ok`, exit 0 | same |
| C2 do-nothing control | `bash corpus/laneguard.sh --selftest --no-mutate` | absent | `detected=0 mutants=3 clean=ok` (exit 1 by design) | same |
| Round-36 counter (not a claim; a guard on the calibration row) | `bash plans/round-36-c1.sh` | 3 (SD5=3, stale 0) | 0 | 0 |

Verdict per claim: C1 **verified** (5 = target; BASE 0; all three forgery controls read 4). C2 **verified as operability** (3 = target; BASE 0); calibration not claimed. No axis harmed: all six axes remain 9 → 9; the round-36 counter is back to its frozen 0 by the calibration row that names the three routed reds and the rebound claim count.

Ledger state at close (`bash corpus/claim-ledger.sh verify`, measured before the final R24-06 re-pin; R24-06 then re-measured directly): `CLAIM_LEDGER: POLICY (claims=86 policy=3 stamped=122)`; FAIL `R11-08`, `R22-03`, `R24-15`, `R25-02` (all predate this round); POLICY `R29-01`, `R29-02`, `R38-03` (the last is new and operator-owned, routed); `MISSING-ID` 53, all pre-existing. Revision audit `REVISION_AUDIT: CLEAN (stale=0 missing=0 dropped=0 added=59 invalid=0)`.

## Sources & frontier

- SOURCES.md rows before → after: **91 → 93** (captures 91 → 93). Counting command: `bash corpus/sources-census.sh` → before `SOURCES_CENSUS: CLEAN (rows=91 A=87 B=2 C=2 queued=1 mined=87 rejected=3 entries_sourced=14 legacy=21 captures=91 inrow=16 inrow_only=0 inrow_nonreproducing=12)`, exit 0; after `SOURCES_CENSUS: CLEAN (rows=93 A=89 B=2 C=2 queued=1 mined=89 rejected=3 entries_sourced=14 legacy=21 captures=93 inrow=16 inrow_only=0 inrow_nonreproducing=12)`, exit 0. Fleet census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi`: exit 0 before and after (`kagi ok`).
- Rows added by tier: **A 2** (S092 Vault release tag page v2.2.1; S093 OpenBao release tag page v2.7.2), both `mined`, both opened 2026-11-05 with located quotes at byte offset 21886 (`corpus/lessons/round-38.md` §Gate).
- Rows touched old → new: none (`status`, `recheck`, `used-by` of S034, S035, S036, S039, S089–S091 unchanged).
- Frontier rows advanced: none moved to core; S092 and S093 corroborate S089 and S090 with a second surface (tag page), which is verification of held ground, not coverage growth.
- Sourced claim: C1 rests on S092 and S093 (opened 2026-11-05) and re-hashes S089–S091 from committed bodies.
- Mistakes mined (round 38 lesson `## Mistakes`): M38-1 (transcribed freeze hash, erratum with full hash), M38-2 (LANE-GUARD described, not committed: fix C2), M38-3 (quotes checked by hand: fix C1), M38-4 (edit drift, caught by read-back), M38-5 (own counter reading 6 vs 3), M38-6 (own ledger growth turned three rows red; migrated with old→new). Each fix is shown able to fail: C1 forgeries 4 of 5; C2 no-mutate 0 of 3.
- Assimilation: none. Quarantine of the eight `kagi` absent-defect register rows holds (none appended). considerthese: no proposal taken (the round-37 plan records the 2026-10-26 proposals as implemented or discharged).
- Census-before/after and exit codes: above.

## Trend verdicts

- **expansion: unchanged.** No new knowledge entry; two tier-A corroboration rows on held ground; no coverage-map ground entered.
- **quality: unchanged.** The round's quote evidence is now located by a committed gate (positive), but R37-V2 remains open debt; the closure's condition "close it or re-grade the quality trend" is answered by this re-grade. The critic's falsified sentences were corrected in the same close, which is the quality work this round did, but no entry changed status.
- **discernment: unchanged.** Pending the non-author spot-check (`corpus/lessons/round-38.md` §Non-author spot-check is pending outside closure). The wave's critic and scout falsified or overstated ten sentences of the lane's own prose, and all are recorded; the lane's gate decisions (admit S092/S093, refuse the bare feed row and the markup-stripping locate) await the outside check.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `SKILL.md` gate rows 823–824 (two new gates with verdict maps and selftest pointers); unchanged evidence at `LOG.md` earlier rounds.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `LOG.md:1741` (wave `build` settled; C1 and C2 reproduced on the candidate; domain task: located-quote verification of the release-feed and tag-page rows against committed bytes and live pages).
- [~] Instructions executable by an agent without oral context — evidence: `corpus/quote-locate.py` and `corpus/laneguard.sh --selftest` executed by K38ExecQuote and K38ExecGuard from scratch extractions (`.ufo/waves/round-38/build/K38ExecQuote/report.md`, `K38ExecGuard/report.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `.ufo/waves/round-38/build/K38ConnOverlap/report.md` (NO OVERLAP; adjacent sibling-local located-quote gates and a lane-guard term reported, not absorbed).

No box is `[x]`: no non-author verifier has signed any box in this round.

## Round shape and settlement

- Shape: one v1 wave `kagi-r38-build`, 10 seats (within the 8–16 band; L2 floor 8 met). Roles: executor 3, scribe 1, scout 1, connector 1, reviewer 2, critic 1, mutation-tester 1. Attack seats 4/10 = 40 % (≥25 %); connector 1 (≤2). Planner seat held by the L1 (validator rejects `planner`; recorded in the plan).
- Residual call: none. Round total: 10 seats. Dead seats: none (each returned final output without error).
- Models: routed by `task.agentModelOverrides` only; no model was passed.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Open L0 questions

- `kagi | round-38 | Decision needed: ledger row R38-03 is POLICY (python3 on an unregistered script; PYTHON_SCRIPT_RE is operator-owned). Register corpus/quote-locate.py, or accept R38-03 as routed while R38-01 pins the located count 5.` — appended `0a1c648b` (fleet).
- Existing kagi L0 lines (round-28 documentary disposition; round-30 policy red) stay open; not touched.

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` before this report: ` M .scratch/run15-state.json` (orchestrator-owned; not touched) and `?? cited-lines.txt` (paper text, no lane or round name; not written by a round-38 seat; left in place). One stray file written by a seat (`nil`, K38ExecQuote) was deleted by the seat before yield and is absent. No misroot copied into the lane.

## Conformance

- `grep -c '^## SHONEN'` is checked on this report before filing (see the commit step).
- Pre-report gate: `git ls-remote origin refs/heads/master` = `88374f9539e741cbc6e07505f4c09e42472ee8d1` (equal to the lane tip).
- WAVE-DONE received for `build` before the report was filed (`[15c21578fafca1df] Main: WAVE-DONE kagi r38 build: all 10 seats settled`).
- Frozen predicates, controls and kill rules were not amended after data; the instruments in `corpus/` are unchanged after the predeclaration commit (`git diff --stat 8c48b7df -- corpus/quote-locate.py corpus/laneguard.sh plans/round-38-c1.sh plans/round-38-c2.sh plans/round-38-controls.sh plans/round-38-rows.py plans/round-38.controls.tsv` is empty at close).
- Scratch: all seat scratch roots removed by their seats; `/fast/scratch/hyaku/kagi-r38/` holds only the verification copies named here.
