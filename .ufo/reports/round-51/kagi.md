# kagi — round 51 report (attempt 1, L1 KagiR51)

Lane `/home/vgpnk/Projects/shokunin/kagi-shokunin`, branch `master`. Final lane hash `affb270bc9288bf08f72a0197d705cc06ec5ac67`; `git ls-remote origin refs/heads/master` prints that hash. Claim BASE `214d8bf530a0c87c00686493f21af15396284793`. Predeclaration `4ad8ab7cd5bf8949d125ac96ccef45e69dabc567` (frozen plan `plans/round-51.md`; counters `plans/round-51-c1.sh`, `plans/round-51-c2.sh`; pre-freeze controls `plans/round-51-controls.sh`, 20 MATCH). No amendment. One attempt: `.ufo/watchdog.log` has a single launch line for round 51; nothing was inherited.

## Work performed

Declared claims (2), frozen before any candidate was scored:

- **C1, operability, capability acquisition.** The lane executes five OpenBao response-wrapping mechanics that its sources document. 0 → 5. This is the sourced claim (S108, S109).
- **C2, calibration.** The declared-claim manifest and the §Capabilities readings agree with the repo. 3 → 0.

Every axis sits at 9, the saturation line. Capabilities entered in rounds 48 and 49, so the stagnation nudge does not fire, and both claims work a lowest-scoring axis (all six are tied) (`plans/round-51.md:15-21`).

Work items:

- **Protocol load and the round-50 closure.** I read `corpus/lessons/round-50-verifier-spotcheck.md`. Each of D1–D5 is mapped in `corpus/lessons/round-51.md` §Closure defects of round 50:
  - D3 → path-blind counter runs plus a connector scan.
  - D4 → answered by R51ExecD4.
  - D5/F5 → the `lane-status:` line now names four routed reds.
  - D1 → R36-01 and R11-08 timed by seats and by me.
  - D2 → kept named.
- **Predeclaration `4ad8ab7c`.**
  - Reference trial: `.ufo/waves/round-51/controls/fixtures/ref/corpus/openbao-wrap-trial.sh`.
  - Counters C1 and C2. C1 runs are path-blind: a byte-identical dispatcher `bao`, random bin directories, and a random run order.
  - S108 capture.
  - Controls receipt `controls/controls-prefreeze.txt`: 20/20 MATCH, covering nine C1 and seven C2 forgery or fail-closed fixtures. Run 1 of the C2 half had two DIFFs. Both were fixture-side expectation errors, corrected before the freeze; the run is kept as `controls-prefreeze-run1.txt`.
- **C1 candidate (`47d09594`).**
  - `corpus/openbao-wrap-trial.sh` is the reference trial; only two comment lines differ (`final/c1-killrule.txt`).
  - Two registry rows, S108 and S109, with their fetch rows and captures.
  - Entry `corpus/knowledge/vault-openbao-token-lease-lifecycle.md` §Measured (round 51), drafted by R51ScribeEntry. It carries a "Does not establish" list and the scout's measured rewrap divergence.
  - A capability row, and a `PROVINCE.md` core bullet at `:95`.
- **C2 candidate (`47d09594`).**
  - Manifest rows `50 C1/C2` and `51 C1/C2` (`corpus/claims-declared.tsv`).
  - A `## Round 51 — post-move` section in SCORECARD.
  - A visible readings line `CLAIMS_DECLARED: CLEAN (claims=29)`.
  - Landing checks `final/c2-landing-checks.txt`:
    - The SCORECARD diff deletes only the rewritten `lane-status:` line.
    - It adds no `<!--` and removes no `## ` heading.
    - R31-06 still reads 1.
    - Every BASE plan file is unchanged.
- **Ledger population migrations.** This round's own additions (one SCORECARD heading, two registry rows) moved six expectations: R13-01, R24-06, R21-02, R31-02, R33-02 and R34-03. They are journaled in `.ufo/waves/round-51/expectation-migrations.json`, and `final/expect-journal.txt` reads `EXPECT_JOURNAL: CLEAN (changed=6 journaled=6)`. The ledger was restamped (124 rows; the set is unchanged).
- **Wave findings integrated.**
  - **R51CriticC1:** the frozen C1 counter writes `$W/out.<mode>`. A 13-line trial that never runs `bao` reads its own stdout path and scores 5 (FA).
    - Logged as M51-2 and QM65.
    - Successor counter `plans/round-51-c1h.sh`: random log ids, the real run twice, full verdict vectors.
    - `final/c1h-controls.txt`: FA 5 → 0, FB 5 → 0, reference 5 → 5.
  - **R51CriticC2:** heading-rename and HTML-comment ceilings (N7, N8, N11, N13). Routed; checked absent at landing.
  - **R51ReviewerTrial:** refusal conflation (M51-3, routed). Its entry over-claim is fixed in the entry's T1 line.
  - **R51SentinelSecrets:** secrets in argv (HIGH; routed, see Open questions).
  - **R51ScoutSource:** four API pages judged, and a measured rewrap/doc divergence.
- **Harm check.** Full `claim-ledger.sh verify` on clean clones:
  - BASE (R51ExecHarm, `build/R51ExecHarm/verify-base.txt`): FAIL 3, POLICY 3.
  - Candidate (`final/verify-candidate.txt`): FAIL 3, POLICY 3, with the same ids — R11-08, R25-02, R36-01; R29-01, R29-02, R38-03.
  - The R11-08 reason changed from exit-mismatch to timeout. Before → after numbers are below.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists only `.scratch/` paths and `trail-ids.txt`.
  - `trail-ids.txt` is one byte with mtime 20:36, before this round launched at 21:17, and does not name this lane. It is not mine and was left untouched.
  - Three small `/tmp` leftovers of my seats (`r51_setup.sh`, `run3-result.log`, `runbase.log`) were deleted. They were not fleet-root misroots.

## Landed changes

| Commit (landed) | Content | LOG.md |
|---|---|---|
| `4ad8ab7cd5bf8949d125ac96ccef45e69dabc567` | predeclaration: plan, C1/C2 counters, controls (20 MATCH), reference fixtures, S108 capture, instrument sha256 receipt | LOG.md `## Round 51`, bullet "Predeclaration" |
| `47d09594c6b122cc9c812503c338b4426c620f3b` | candidate: wrap trial, S108/S109 rows and fetch rows, S109 capture, entry §Measured (round 51), manifest rows, SCORECARD section + capability row + readings line + `lane-status:` line, PROVINCE bullet, QM64/QM65, lesson, six ledger migrations + journal, restamp, `plans/round-51-c1h.sh`, wave spec, dispatch, results and all 12 seat reports | LOG.md `## Round 51`, bullets "Build wave" and "Candidate" |
| `7eab7aa4ea4c55b7980d8af1cb6bef09d64b36ba` | final receipts: C1/C2 BASE and candidate readings, hardened reading, census end, full verify, R36-01/R11-08 unbounded | LOG.md `## Round 51`, bullet "Measurements and harm check" |
| `affb270bc9288bf08f72a0197d705cc06ec5ac67` | tip receipts (`final/tip-counters.txt`, `final/tip-r11-08.txt`) | same bullet (receipts only) |

Every hash above was printed by `jj-lane.sh` as `landed <hash>` after remote verification.

## Before → after measurements

- **C1.** Command: `bash plans/round-51-c1.sh <rev>`.
  - BASE `214d8bf5`: `C1_OPENBAO_WRAP: value=0 absent=1 pins=1` (`final/c1-base.txt`).
  - Candidate `47d09594`: `value=5 discriminating=5 pins=1 setup_ok=1 nosecret=1 src=1(S108)`. Every T1..T5 reads `real=HOLDS,shim=BROKEN,entry=1` (`final/c1-candidate.txt`).
  - Tip `7eab7aa4`: `value=5` (`final/tip-counters.txt`).
  - Target 5: **met**.
  - Kill rules: none fired.
    - The instruments are byte-identical to the predeclaration receipt.
    - The candidate equals the reference trial outside `#` lines (rc 0).
    - No committed `r51-<24hex>` value.
    - The bao pin is unchanged (`final/c1-killrule.txt`).
  - Supplementary: the hardened `bash plans/round-51-c1h.sh 47d09594` gives `value=5` (`final/c1h-candidate.txt`).
  - Ceiling: a non-running trial reaches 5 on the frozen counter (R51CriticC1 FA). The candidate is the reference trial, and that is machine-checked.
- **C2.** Command: `bash plans/round-51-c2.sh <rev>`.
  - BASE: `value=3 M=2 V=1` (`final/c2-base.txt`).
  - Candidate `47d09594`: `value=0 M=0 V=0`, with `CLAIMS_DECLARED: CLEAN (claims=29)` (`final/c2-candidate.txt`).
  - Tip `7eab7aa4`: `value=0 M=0 V=0` (`final/tip-counters.txt`).
  - Target 0: **met**.
  - Kill rules: none fired. Instruments are unchanged, BASE plans and manifest rows are intact, and R31-06 reads 1 (`final/c2-landing-checks.txt`).
- **Harm check.** Command: `nice bash corpus/claim-ledger.sh verify` on a clean clone, counted with `grep -c '^FAIL'` and `grep -c '^POLICY'`.
  - BASE `build/R51ExecHarm/verify-base.txt`: 3 FAIL (R11-08 exit-mismatch, R25-02, R36-01 timeout) and 3 POLICY.
  - Candidate `final/verify-candidate.txt`: 3 FAIL (R11-08 timeout, R25-02, R36-01 timeout) and 3 POLICY. Load average 46–51.
  - Pre-migration run `final/verify-candidate-premigration.txt` showed exactly the six population rows plus the BASE reds; the `MISSING-ID` set is identical to BASE apart from line shifts.
  - R36-01 run alone, unbounded, at the candidate prints `0` (= expect), rc 0, in 367 s (`final/r36-01-candidate.txt`). The value is correct; it is over the 300 s budget under load, as at BASE (R51ExecHarm: 436 s).
  - R11-08 run alone at the candidate showed `unresolved=7` (`final/r11-08-candidate.txt`). Four of the seven were citations to `final/` receipts not yet committed at `47d09594`; they were landed in `7eab7aa4`. The tip re-run is `final/tip-r11-08.txt`, where `CITATION_GATE: BROKEN (cites=3648 docs=128 unresolved=3 …)` — the same three non-owned closure-spotcheck citations as at BASE. The three remaining unresolved citations are the BASE three, all in non-owned closure spot-checks.

## Sources & frontier

- **Rows.** `corpus/SOURCES.md` went from 107 to 109. Counted with `bash corpus/sources-census.sh`: `SOURCES_CENSUS: CLEAN (rows=109 A=105 … captures=109 …)` (`final/census-end.txt`).
  - Added: tier A 2 — S108 (OpenBao "Response wrapping" concepts page) and S109 (OpenBao `sys/wrapping/wrap` API page). Both are `mined`, `recheck 180d`, and used by the entry and the lesson.
  - Touched old→new: none.
  - Rejected (lesson §Gate, each with reason and flip):
    - The wrapping-lookup page. R51ScoutSource recommended admit; I overruled, on the record for the closure.
    - The wrapping-rewrap page; its sample response contradicts the measured 2.7.2 behaviour.
    - The wrapping-unwrap page.
    - The HashiCorp Vault response-wrapping page.
- **Census command.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi`.
  - Start (`.ufo/waves/round-51/controls/census-start.txt`): `kagi ok`, rc 0, rows 107.
  - End (`final/census-end.txt`): `kagi ok`, rc 0, rows 109. There are 19 W04 warnings, the same count as round 50.
- **Sourced claim.** C1 rests on S108 and S109, both opened 2026-11-07.
  - Two seats re-fetched each page and got byte-identical bodies.
  - Located quotes are 13 and 11 words, `count=1` each (lesson §Gate).
- **Mined mistakes** (`corpus/lessons/round-51.md` §Mistakes):
  - M51-1: manifest omission. The fix is shown able to fail by the C2 counter: 3 at BASE, 1 on K2-F6, 0 on K2-P. Added QM64.
  - M51-2: the counter's output path leaks the run mode. The fix is shown able to fail by `final/c1h-controls.txt`: FA and FB 5 → 0. Added QM65.
  - M51-3: refusal conflation. Routed, not counted.
- **Frontier advance.** Response wrapping moved from unheld ground (`grep -rl 'sys/wrapping' corpus/` was empty at BASE) to an executed trial.
- **Other inputs.**
  - Assimilation: none. `find …/shokuknow/merge/kagi -type f | grep -iE 'wrap|cubby|openbao|bao'` prints nothing, and R51ConnectorSiblings' content grep over `merge/kagi/` found no match.
  - considerthese: the newest file is `2026-10-26.md`; no proposal was taken.

## Trend verdicts

- **expansion: improved.** New ground: response wrapping, never held before (BASE grep empty), is now an executed five-test trial with two tier-A rows that the landed change cites. There is a new capability row and two new QUALITY criteria (QM64, QM65).
- **quality: improved.**
  - C1 went 0 → 5 and C2 went 3 → 0 against frozen counters.
  - The lane's own declared-axis gate is CLEAN again after a round in which it was red.
  - The ledger shows no new red: FAIL 3 → 3 with the same ids, and the six moved population rows are journaled.
  - The entry's one over-claim, found by R51ReviewerTrial, was corrected before landing.
- **discernment: improved.**
  - Two counter weaknesses were found by the lane's own attack seats before landing: FA, and the C2 heading rename. FA became a mistake whose fix is shown able to fail (M51-2), and both are named ceilings rather than hidden.
  - One seat recommendation was overruled with a reason (wrapping-lookup).
  - One doc/behaviour divergence was measured and recorded instead of imported (the rewrap sample).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: QUALITY QM64/QM65 add two error patterns, each with a check shown able to fail (`corpus/QUALITY.md`, last two rows). No non-author verifier: the wave seats were dispatched by the lane.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: LOG.md `## Round 51`. The OpenBao response-wrapping trial ran end to end on this host (`final/c1-candidate.txt`, T1..T5 HOLDS). R51ExecTrial ran it three times plus two SIGKILL runs with no surviving server (`build/R51ExecTrial.md`).
- [~] Instructions executable by an agent without oral context. Evidence: `bash plans/round-51-c1.sh <rev>` and `bash plans/round-51-c2.sh <rev>` were re-run by R51ExecTrial, R51ReviewerC2 and R51MutCounters without context, with the same values (`build/R51ExecTrial.md`, `build/R51ReviewerC2.md`, `build/R51MutCounters.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: `PROVINCE.md:95` (round-51 core bullet). R51ConnectorSiblings found no sibling holding response-wrapping ground or a declared-claim manifest gate (`build/R51ConnectorSiblings.md` F1).

## Stale-lane

No. The lane is respawn-per-round, and no other mission of this lane is open.

## Round shape, waves and seats

- **Shape.** One v1 build wave, `kagi-r51-build`, of **12 seats**. It was validated under `scripts/hyaku/ufo-wave-policy.json` (band 8–16) and dispatched through `build.ready` → `build.ready.dispatched`. WAVE-DONE was received. There was no residual call, so the round total is **12**.
- **Planner.** I hold the canonical §3 planner seat (the validator rejects `planner`).
- **Roles.** Executor 3 (R51ExecTrial, R51ExecHarm, R51ExecD4), scout 1 (R51ScoutSource), connector 1 (R51ConnectorSiblings), scribe 1 (R51ScribeEntry), reviewer 2 (R51ReviewerTrial, R51ReviewerC2), critic 2 (R51CriticC1, R51CriticC2), mutation-tester 1 (R51MutCounters), sentinel 1 (R51SentinelSecrets).
  - Attack share is 5/12 = 42 % (reviewer, critic and mutation-tester).
- **Dead seats: 0.** All 12 have output in `build-results.json` and a report in `.ufo/waves/round-51/build/`.
- **Mutation result** (R51MutCounters): 16 mutants, 11 killed, 5 survived. The survivors are C1-M2 (no shuffle), C1-M7 (setup_ok guard dropped), C1-M8 (token-shaped NOSECRET branch dropped), C2-M7 (working-copy pin) and C2-M8 (g4 shape check). All five are control-battery blind spots, and none changes a verdict at BASE or at the candidate.

## Tool installs

None by the L1. None by any seat; each seat report says none.

## Open questions

No new L0 question. Routed to the next round:

- **R51SentinelSecrets S-1 (HIGH).** The trial passes the dev root token (`-dev-root-token-id`), wrapping tokens (`bao unwrap <t>`, `token=<t>`) and nonce values (`v=<n>`) on argv, which other local users can read through `/proc/<pid>/cmdline`. All of these are throwaway values for an in-memory 127.0.0.1 dev server that dies with the trial (pdeathsig), and the round-49 token trial has the same `-dev-root-token-id` shape.
  - The kill rule froze the trial's non-comment lines this round.
  - Fix route, per the seat: tokens via stdin (`token=-`, no trailing newline); no `-dev-root-token-id`, parsing the generated token from a 600-mode log instead; the counter's shims changed in the same commit.
  - Also: S-2 (the root token at rest in `server.log` after a SIGKILL) and S-3 (the free-port TOCTOU).
- **M51-3.** Refusal conflation in the trial's parsers.
- **The successor counter `plans/round-51-c1h.sh`.** Adopt it for the next trial claim. FC (one junk rewrap fingerprints SH4) and the `.mode` reader stay ceilings.
- **C2 gate witness ceilings.** R51CriticC2 N7, N11 and N13 (a renamed `post-move` heading), and N8 (an HTML-comment readings pair).
- **Operator-routed reds.** R25-02 FAIL and R29-01, R29-02, R38-03 POLICY stay operator-routed and byte-identical.
- **Ledger timeouts.** The R11-08 and R36-01 timeout budget under fleet load (load average 23–71 this round).

## Verdict on the round (L1 reading; the non-author closure rules)

- C1 and C2 each met their frozen target at the candidate, and no kill rule fired.
- The C1 counter's leak (FA) is disclosed. C1's admission rests on the counter together with the machine-checked identity of the candidate and the reference trial.
- No ledger row became red, and every axis stays 9 → 9.
