# kagi — round 50 report (attempt 2, L1 KagiR50a2)

Lane `/home/vgpnk/Projects/shokunin/kagi-shokunin`, branch `master`. Final lane hash `23de560402260a6062b9ee834b46bc9fd4344152`; `git ls-remote origin refs/heads/master` prints that hash. Claim BASE `565c43a874b59cd216f4a55c8742db48fa854f16`. Predeclaration `7d3b2c01b375d5459abd7da79bb4063b7d728fc7` (attempt 1; frozen plan `plans/round-50.md`, counters `plans/round-50-c1.sh` and `plans/round-50-c2.sh`, controls `plans/round-50-controls.sh`). No amendment.

## Work performed

Declared claims (2), both frozen by attempt 1 before any data and run unchanged here:

- **C1, operability.** The OpenBao trial leaves no dev server behind when its shell is SIGKILLed. 0 → 3 kill points. This is the sourced claim (S106, S107).
- **C2, calibration.** The claim ledger agrees with the observed repo state on ten drifted rows. 10 → 0.

Work items:

- **Inherited state (attempt 1 died; `.ufo/watchdog.log` 20:22:55 `lane-dead-no-report kagi round=50`).**
  - Re-verified and kept: the C1 working-tree change, the S106/S107 rows, their fetch rows and captures, and the build-wave evidence.
    - The C1 change equals the frozen reference fixture except one header comment.
    - The captures were re-fetched live at 23:25Z and are byte-identical: sha256 `5e72367e…` and `3bc0de99…`.
  - Nothing inherited was discarded.
  - Evidence: `corpus/lessons/round-50.md:7`; commit `9e4dcbcc`.
- **C1 candidate.** `corpus/openbao-token-trial.sh` starts the dev server with `setpriv --pdeathsig KILL bao server -dev …` and gives `SETUP` when setpriv is missing.
  - Commit `9e4dcbcc8666b22aa871037138826693fa0ba4fa`.
  - Receipts: `.ufo/waves/round-50/final/c1-candidate.txt` and `c1-final.txt`.
- **C2 candidate.** Ten expectations moved to the lines measured on a clean clone of `6963a350`.
  - The journal `.ufo/waves/round-50/expectation-migrations.json` gives one reason per row. Each reason names the commits that grew the population, found by walking the commits with `git show`/`git archive`.
  - `expect-journal.sh` reads `CLEAN (changed=10 journaled=10)`. The ledger was restamped.
  - Commit `e4abab1d23b731c0c042be9bc50b19c9f9313dcb`.
- **Curation and lesson.**
  - S106 and S107 (tier A); the prctl(2) row was rejected.
  - Mistakes M50-1..M50-4 and erratum E50-1 are in the lesson; criteria QM62 and QM63 are new.
  - The `PROVINCE.md` round-49 bullet now states the gpg/sigstore ceiling (closure D5).
  - Commits `6963a3502ffadffbc1e08da8ca66d5c4254c3c7b` and `d4994e3d15c03e62132a784d708bd56e00fa9d0d`.
- **Harm found and repaired before this report.**
  - A full `claim-ledger.sh verify` on `e4abab1d` showed R36-03 FAILED with `unbound=2`: S106/S107 had been added as `on-release` with no bound release clock.
  - Both rows were moved to `180d`, and R36-03 reads CLEAN again.
  - Receipt `.ufo/waves/round-50/final/r36-03-repair.txt` (rc 1 → rc 0); recorded as M50-4 and QM63; fixed in commit `d4994e3d`.
- **Residual attack call, 4 seats.** Its reports are in `.ufo/waves/round-50/residual/`.
  - C1 not falsified: R50bReviewerC1 read value=3 on the candidate and 0 at BASE, and ran an independent SIGKILL demo (server dead vs alive).
  - C2 not falsified: R50bCriticC2 read 0 and 10, re-derived every journal commit, and named ceilings F1–F5.
  - Mutants: 5 killed and 4 survived (R50bMutCounters); no survivor changes a verdict at BASE or at the candidates.
  - R50bReviewerLesson found one dangling receipt pointer and three wording notes. All four were fixed in `d4994e3d`.
- **Closure defects of round 49 (`corpus/lessons/round-49-verifier-spotcheck.md:96-100`).**
  - D1 → M50-1, E50-1 and QM62.
  - D2 → C2 guards G2 and G5.
  - D3 → routed again.
  - D4 → C1.
  - D5 → the `PROVINCE.md` sentence.
  - Mapped at `corpus/lessons/round-50.md` §Closure defects.

## Landed changes

| Commit (landed) | Content | LOG.md |
|---|---|---|
| `9e4dcbcc8666b22aa871037138826693fa0ba4fa` | C1 trial change plus attempt-1 wave evidence | LOG.md `## Round 50`, bullet "C1 candidate" |
| `6963a3502ffadffbc1e08da8ca66d5c4254c3c7b` | S106/S107, lesson, QM62, SCORECARD/LOG round-50 sections, PROVINCE D5 sentence, C1 receipt, restamp | LOG.md `## Round 50`, bullet "Curation" |
| `e4abab1d23b731c0c042be9bc50b19c9f9313dcb` | C2: ten ledger expectations plus journal, restamp | LOG.md `## Round 50`, bullet "C2 candidate" |
| `d4994e3d15c03e62132a784d708bd56e00fa9d0d` | harm repair (180d), M50-4, QM63, residual evidence, lesson corrections, SCORECARD/LOG measurements, restamp | LOG.md `## Round 50`, bullets "Harm check" and "Residual attack call" |
| `23de560402260a6062b9ee834b46bc9fd4344152` | final receipts (`final/c1-final.txt`, `c2-final.txt`, `verify-final.txt`, `census-end.txt`, `r36-01-timing.txt`) | receipts only (`.ufo/`, unstamped) |

Every hash above was printed by `jj-lane.sh` as `landed <hash>` after remote verification.

## Before → after measurements

- **C1.** Command: `bash plans/round-50-c1.sh <rev>`.
  - BASE `565c43a`: `C1_ORPHAN_SAFE: value=0 positive=1 reaped=3` (`final/c1-base.txt`, and K1-0 in `controls/controls-prefreeze.txt`).
  - Candidate `9e4dcbcc`: `value=3 positive=1 reaped=0 K1/K2/K3 survivors=0`, rc 0 (`final/c1-candidate.txt`).
  - Tip `d4994e3d`: `value=3` (`final/c1-final.txt`).
  - Target 3: **met**.
- **C2.** Command: `bash plans/round-50-c2.sh <rev>`.
  - BASE: `C2_LEDGER_DRIFT: value=10` (`final/c2-base.txt`).
  - Candidate `e4abab1d`: `value=0 ids=10 changed=10`, every id OK (`final/c2-candidate.txt`).
  - Tip `d4994e3d`: `value=0` (`final/c2-final.txt`).
  - Target 0: **met**.
- **Kill rules.**
  - Instruments are unchanged since the predeclaration (residual R50bReviewerC1 (b): the stat diff is empty).
  - The trial diff touches only the header, the setup check and the launch line.
  - No `r49-<24hex>` string appears in the tree.
  - R25-02, R29-01, R29-02 and R38-03 are byte-identical (R50bCriticC2 (c)).
- **Harm check.** Full ledger verify on a clean clone, counted with `grep -c '^FAIL'`:
  - BASE `controls/verify-base.txt`: 12 FAIL and 3 POLICY.
  - Candidate `final/verify-candidate.txt`: 4 FAIL (R11-08, R25-02, R36-01, R36-03).
  - Tip `final/verify-final.txt`: **3 FAIL** (R11-08 timeout, R25-02, R36-01 timeout) and 3 POLICY.
  - R36-01 times out only because of host load. It reads `0` (= expect) at both BASE (753 s) and candidate (351 s); the host load average was 38–44 (`final/r36-01-timing.txt`).
  - R11-08 was FAIL at BASE too. On the tip it timed out, so its value there is unmeasured.
  - The round-49 counter still reads 5 on the candidate (`positive=1`).

## Sources & frontier

- **Rows.** `corpus/SOURCES.md` went from 105 to 107. Counted with `bash corpus/sources-census.sh`: `SOURCES_CENSUS: CLEAN (rows=107 A=103 … captures=107 …)`.
  - Added: tier A 2 (S106 PR_SET_PDEATHSIG(2const), S107 setpriv(1)).
  - Touched old→new: none from before this round. S106/S107 changed `recheck on-release → 180d` within the round (M50-4).
  - Rejected: prctl(2), which only cross-references PR_SET_PDEATHSIG.
- **Census command.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi`.
  - Start (attempt 1, `.ufo/waves/round-50/controls/census-start.txt`): `kagi ok`, rc 0.
  - End (`.ufo/waves/round-50/final/census-end.txt`): `kagi ok …/corpus/SOURCES.md`, rc 0 (W04 warnings only).
- **Sourced claim.** C1 rests on S106 and S107, both opened this round. The located quotes have count 1 each and 12 and 8 words (`corpus/lessons/round-50.md` §Gate).
- **Mined mistakes.** M50-1 (round-49 FAIL count) has a fix shown able to fail (rc 1/0). M50-2 (orphan servers) and M50-4 (unbound on-release rows) are each shown able to fail. M50-3 (seat outputs lost) is routed and not counted.
- **Frontier advance.** The OpenBao trial is now safe to run under attack seats: a killed run leaks no server.
- **Other inputs.**
  - Assimilation: none. No `merge/kagi/` file matches pdeath/prctl/process/orphan/bao/vault/lease/token.
  - considerthese: the newest file is `2026-10-26.md`; no proposal taken.

## Trend verdicts

- **expansion: improved.** Two new tier-A rows are cited by a landed change; a new operational property (SIGKILL-safe trial) is measured 0 → 3; there are two new QUALITY criteria (QM62, QM63).
- **quality: improved.** C1 went 0 → 3 and C2 went 10 → 0 against frozen counters. Ledger FAIL rows went 12 → 3, and the remaining reds are operator-routed or timeouts under host load (receipts above).
- **discernment: unchanged.** The admit/reject sample has its usual shape (S106 admitted, prctl(2) rejected). The one harm this round, M50-4, was introduced by the lane and caught by the lane's own harm check, not avoided beforehand.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: the `SKILL.md` tables are unchanged; QUALITY QM62/QM63 add two error patterns with checks shown able to fail (`corpus/QUALITY.md` last two rows). No non-author verifier: the residual seats were dispatched by the lane.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: LOG.md `## Round 50`. The OpenBao trial ran under SIGKILL at three kill points on this host (`final/c1-final.txt`), and R50bReviewerC1 ran an independent kill demo (`.ufo/waves/round-50/residual/R50bReviewerC1.md`).
- [~] Instructions executable by an agent without oral context. Evidence: `bash plans/round-50-c1.sh <rev>` and `bash plans/round-50-c2.sh <rev>` were each re-run by a seat with no context and gave the same values (residual reports).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: `PROVINCE.md:94` now states the binary's verification ceiling. Process-lifetime handling stays inside the lane's own trial. The connector seat (attempt 1) left no output, so no sibling scan was done this round.

## Stale-lane

No. The lane is respawn-per-round, and no other mission of this lane is open.

## Round shape, waves and seats

- **Shape.** One v1 build wave (attempt 1) plus one residual call (attempt 2): 12 + 4 = **16 seats**.
- **Planner.** The L1 holds the canonical §3 planner seat (the validator rejects `planner`).
- **Build wave `kagi-r50-build`, 12 seats.** It was validated under `ufo-wave-policy.json`, and `build.ready` became `build.ready.dispatched` at 19:21.
  - Roles: executor 3 (R50ExecTrial, R50ExecLedger, R50ExecCitations), scout 1, scribe 1, connector 1, reviewer 2, critic 2, mutation-tester 1, sentinel 1. Attack share is 6/12 = 50 %.
  - WAVE-DONE was received. The orchestrator kernel restarted mid-wave, so `build-results.json` holds `output: null` for all 12 seats.
  - Only R50ScoutSources (report and fetches) and R50ScribeLesson (receipts) left files. **10 seats are dead in the evidence**, with no output and no file (M50-3); none was replaced.
- **Residual call `kagi-r50-residual`, 4 seats.** These were ≤4 attack seats, not a validated wave, sent through the inline handoff via `residual-dispatch.json` and `residual.ready`.
  - Seats: R50bReviewerC1 (reviewer), R50bCriticC2 (critic), R50bMutCounters (mutation-tester), R50bReviewerLesson (reviewer).
  - WAVE-DONE was received; all 4 settled and wrote reports.
- **Dead seats total: 10** (attempt-1 build wave).

## Tool installs

None by the L1 or by the residual seats (each reports `none`). The attempt-1 seats recorded none in their surviving files.

## Open questions

No new L0 question. Routed to the next round:

- D3: non-identifying shims and a PATH-reader control.
- C1/C2 counter mutation survivors: M3 OBSERVED, M4 wait, M6b journal equality, M8 POLICY arm.
- R50bC2-F1: G6 does not test anchoring or identity retention.
- F2: the note column is unprotected.
- F3: R38-03 `located=5` sits behind the policy refusal.
- F5: the SCORECARD lane-status line names three routed reds where there are four.
- R11-08's three citations; the ledger timeout budget under fleet load (R11-08, R36-01).

## Verdict on the round (L1 reading; the non-author closure rules)

- C1 and C2 each measured at their frozen targets, at the candidate and again at the tip, and no kill rule fired.
- One harm was introduced: R36-03, the unbound `on-release` rows. It was repaired before landing the report and is receipted.
- Ledger reds went 12 → 3, and none of the three is a content regression by the receipts above.
