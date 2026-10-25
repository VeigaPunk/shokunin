# tameshi — round 17 report (hyaku phase 2, attempt 1)

Lane repo `tameshi-shokunin`, branch `master`. Dispatch tip `98bea7da5801f4bc58e4187690ee1687c8a5061f`; lane HEAD at report time `30b0ca84b85e33948ba2960584dea1b36c1e8779` (landed, `jj-lane.sh state`: ahead=0 behind=0, tracked=0 untracked=0). This was a repair-first round after round 16 closed rejected-harmed (`corpus/lessons/round-16-verifier-spotcheck.md`).

## Work performed

Declared claims (2):
- **C1 — calibration (lowest owned axis, 6):** cold-read credit keyed to the inputs a read ran against (R16-C2b). The full SKILL.md page was re-read under that rule, so box 3 is earned again. The stale round-14 recipe was repaired (R16-C2a) and the box-3 overclaim corrected by append (R16-C2c).
- **C2 — operability (graded harmed in r16):** the registered round-14/15 disposition capability returns its admitted 0-clean outcome at the branch tip again (R16-OP1). A new monitor runs the registered entry commands, not only selftests (R16-MON1). jj-migration fixes are included.

Work items:
- OP1 re-pin: `tools/evidence-disposition.py` gains an appended v2 manifest schema. It reads only the moved instruments (`tools/mutate-and-run.sh`, `tools/pin-disposition.py`) from ancestor commit `4acc607`, with guards G1–G7 from wave-1 critic K03. The guards refuse unneeded waivers, uncommitted edits, tree/dangling/non-ancestor revs, replace refs, grafts, `GIT_*`, shallow repos and symlink modes. New manifests: `.ufo/evidence/round-17/dispositions.json` (→ 0 clean, 11+1) and `dispositions-before.json` (→ 1, producer_before). Round-14 bytes are untouched. Red-before: `.ufo/evidence/round-17/op1-redbefore-98bea7d.txt` (exit 2). Green: `op1-green-*-2a22ade.txt`. Selftest 34 → 56.
- MON1 monitor: `tools/registry-check.py` (selftest 34 cases) and `tools/registry.json` (29 rows). Each row's `source` is `file@98bea7d:line`; expectations are the admitted outcomes; the old round-14 command stays as a `superseded` row and still runs. `--rev` runs in a scrubbed fleet-mirror clone.
- C2b input-keyed credit: `.ufo/evidence/round-17/measure.py` (selftest 94/94), `coldread/trace-inputs.py` (strace, 27/27), `coldread/assemble.py` (77 checks). Rules: class-independent input gate; commands plus committed trace receipts required; veto aggregation; blob-mode inputs; live-lane reads bound to the rev.
- Red-before on the round-14 bucket (`.ufo/evidence/round-17/redbefore/`): 19 inputs strace-replayed at `e69b488`. The bucket is credited at `e69b488` and `input-drift:tools/mutate-and-run.sh` at `09ee1d0`.
- C2a: SKILL.md round-14 recipe steps 2–3 marked historical, with the working archived invocation. The superseded registry rows at :1601 and :1681 point at the live v2 entry.
- C2c: SHONEN box-3 continuation line appended (`SHONEN.md:11`).
- EV1: dated correction appended to `.ufo/evidence/round-16/round-gate/runner-sha256.txt`.
- jj fixes (`/home/vgpnk/Projects/shokunin/.ufo/waves/hyaku/jj-w1/reports/JjAuditTameshi.md` R1/R2, JjTrialTameshi):
  - `tools/mutate-and-run.sh`: repo-identity guard (`repo_identity_mismatch` SETUP) and `git_clean()` GIT_* scrub. Selftest 83 → 95; the guard-removed and scrub-removed mutants fail.
  - `tools/pin-disposition.py`: branch-tip head observation (`detect_branch`) with `head_differs_from_branch`. Selftest 18 → 19; `.ufo/evidence/round-17/jj/head-vs-branch.sh` exits 1 on the old tool and 0 on the new one.
  - SKILL.md:1027-1035 and four knowledge entries now read the branch tip (ER-jj errata).
  - `.gitignore` gains `.ufo/state/`, `.ufo/watchdog.log` and `__pycache__/`.
  - Declined, with reasons in lesson Gate G8/G9: the `probes.mjs` FXROOT guard (historical evidence bytes) and fail-closed auto-track in the helper (fleet-owned).
- Wave-2 cold read found 7 wrong expectations, all repaired in place with line counts kept:
  - CR13: POLICY exit shape
  - CR27: fleet lane map
  - CR28: T1 live cells and replay receipt
  - CR51: selftest exit sentence
  - CR54: round-16 assemble exits
  - CR57/CR58: missing-ledger exit and commit ordering

  Wave-2 reviewers also found hardening gaps in measure/assemble, which were fixed: `live_lane_reads` was blind, the class dodge was open, `read_rev` was unvalidated, and the lane-external check was weak.
- Knowledge: `corpus/knowledge/input-keyed-coldread-credit.md` (cites S058, S059, S060, S064). QUALITY 23–28 added. README round-17 block added.
- Planner seat: the L1 held the §3 planner seat (the validator rejects `planner`). The planning data-walk rode scouts S01/S13, connector C04 and revenger V01–V03.

## Landed changes

Every change is tied to the LOG.md entry "### Round 17 — live-tree re-pin, entry-command monitor, input-keyed cold-read (2026-10-20)". Lane commits, in order (helper `landed`/`pushed` hashes):
- `2a22adeb7d1de5e7189e62ce41ac679d71a97b44` (pushed): build landing — v2 disposition, registry monitor, measure/trace/assemble, recipe/box-3/receipt corrections, jj fixes, QUALITY 23–27, S058–S064, wave-1 evidence.
- `eb7838b16490ca7ba17ea3242ade76a61f744af2` (landed): hermetic git env for the evidence-disposition selftest. Found by `registry-check --rev`: with `GIT_CONFIG_GLOBAL=/dev/null` the selftest had no identity. Also C2 receipts.
- `fad9e9514237ea93d7a11af854cc5810a7eb6a94` (landed): wave-2 reports and receipts, the 7 SKILL repairs, measure/assemble hardening, jj fixture scrub, QUALITY 28.
- `0ff273448ac4e62893c9b28a4cea7c580712df19` (landed): live-lane reads bound to the measured rev (`.git/` reads, or a blob sha at REV); 40-hex-pinned lane externals accepted.
- `e3827ee67d58673e1e9a1141ba1c8333125f4de8` (landed): residual w3 re-reads, ledger v2 with all receipts, lesson wave-2 section.
- `30b0ca84b85e33948ba2960584dea1b36c1e8779` (landed): SCORECARD round-17 section with corrections, LOG, C2/census end receipts.

## Before → after measurements

- **C1** — `python3 .ufo/evidence/round-17/measure.py --rev REV` (no overrides, strict trace gate):
  - `98bea7d`: 0/54 credited, `box3_full_page` false, `calibration_restraint_score` 6 (`.ufo/evidence/round-17/c1-measure-98bea7d.json`). The closure-ruled score was also 6.
  - `e3827ee`: **58/58, true, 8**, `overrides_used` false (`c1-measure-e3827ee.json`). Re-run at `30b0ca8`: identical.
  - Depth guardrail: command D gives 7 at both revisions.
- **C2** — `python3 tools/registry-check.py --rev REV --registry <eb7838b:tools/registry.json> --tag baseline --json`:
  - `98bea7d`: `held=22/23 superseded=1`, exit 1; only `evidence-disposition-round17` differs (`.ufo/evidence/round-17/c2-before-98bea7da5801f4bc58e4187690ee1687c8a5061f.json`).
  - `eb7838b`: `held=23/23 superseded=1`, exit 0 (`c2-after-eb7838b.json`).
  - Re-measured at `e3827ee`: 23/23 baseline, 28/28 full.
  - Independently reproduced by w2 RerunC2Before and RerunC2After.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`.
  - Start: exit 0, with W04 for S047/S048 only (`.ufo/evidence/round-17/census-start.txt`).
  - End: exit 0, same two W04 (`census-end.txt`).
- Rows 55 → 62 (frozen manual count, w2 RerunCensus): tier A 47 → 54, B 6, C 2; mined 28 → 35, queued 24, rejected 3, malformed 0. The diff is a pure append; no prior row changed.
- Added (all tier A, mined, opened 2026-10-20; quotes in `corpus/lessons/round-17.md` Gate):
  - S058 Build Systems à la Carte
  - S059 Bazel remote caching
  - S060 strace(1)
  - S061 jj git-compatibility
  - S062 git-rev-parse `--show-toplevel`
  - S063 git(1) repository discovery
  - S064 Bazel hermeticity
- Every row was re-opened by a non-author w2 scout and its quote verified verbatim. Minor notes: the S061 anchor ¶2 should read ¶3, and S060's "stat-only" wording is imprecise for `%file`.
- No existing row's status, recheck or used-by changed.
- Frontier: F7 stays open. No ground moved to Core.
- Sourced claim: C1.
- Mined mistakes: `corpus/lessons/round-17.md` `## Mistakes` (8 rows) plus the wave-2 table (5 rows).

## Trend verdicts

- **expansion: improved** — one new admitted knowledge entry, `input-keyed-coldread-credit.md`, with 7 new opened sources. It was reviewed by w2 KnowledgeEntryReview: sources, numbers and red-before hold. One false exit sentence in §5 is recorded as open debt.
- **quality: improved** — the previously failing round-14 gate and recipe re-verify at the branch tip, and 7 stale page statements are repaired. The no-harm rerun is green on all 16 entry points with strictly additive counts (w2 NoHarmSelftests). One knowledge-entry sentence and QUALITY 27 were found false in-round; 27 was corrected by QUALITY 28 and §5 is named as debt.
- **discernment: improved** — every R16 routed defect is turned into a criterion (QUALITY 23–26) with a red-before that is shown able to fail. The closure's G6 disagreement (sha-only credit) became the measured rule. Wave 2 falsified the lane's own claims, including LessonReview's finding that G5 was false, and those findings are recorded rather than smoothed.

## SHONEN

- [~] Box 1 (decision tables, error patterns, checklists, cited sources): lane assertion, `reports/round-1-calibration.md#box-1`. The round-17 sections add tables cited to S058–S064.
- [~] Box 2 (end-to-end task logged): lane assertion, `reports/round-1-calibration.md#box-2`.
- [~] Box 3 (executable without oral context): lane assertion, with an appended correction of the round-16 overclaim. Evidence is the round-17 input-keyed ledger `tameshi-shokunin/.ufo/evidence/round-17/coldread/ledger.json`, measured 58/58 at `e3827ee`. There is no independent promotion verifier.
- [~] Box 4 (no cross-domain bleed): lane assertion, `reports/round-1-calibration.md#box-4`. Siblings stayed read-only; w2 SiblingImpact found no sibling gate pinning the moved bytes.

## Waves, seats, dead seats

- **w1 (build):** 67 seats (validator policy v2). Roles: 20 scout, 15 executor, 9 reviewer, 6 critic, 6 scribe, 5 connector, 3 revenger, 2 mutation-tester, 1 sentinel. 0 dead.
- **w2 (falsify):** 99 seats. Roles: 73 reviewer (58 cold reads), 12 scout, 5 critic, 4 mutation-tester, 2 sentinel, 2 connector, 1 simplifier.
  - The first task call was refused with "Background job limit reached (100)" at 12:59:53 and spawned on the retry.
  - Dead (not respawned): CriticC1, CriticC2, CriticNoHarm, CriticSeparability, RegistryProvenance, SentinelLanded (m_opus 429), SentinelTraceEscape (Devin quota exhausted). The L1 covered their questions itself: the separability and no-harm checks are in SCORECARD round 17.
- **w3 (residual):** one ordinary task call, 8 reviewer seats, 10 buckets. One job-cap refusal at 13:46:30.
  - RR2–RR8 hit zai glm-5.3-flash 429s and were resumed under their own identities until each finished. RR1 was re-asked to trace its reads.
- Round total: 174 seats.
- Routing changed mid-round by orchestrator notes. Wave 1 and wave 2 seats ran on the then-current map. w3 reviewers ran on m_zfl (zai glm-5.3-flash).
- Seats appended `solutionSpace` to the validated payloads (the task tool requires it); nothing else was altered.

## Inherited state, incidents, misroot

- No earlier attempt existed: one `launch tameshi round=17` line, `.ufo/watchdog.log:485`.
- I did not edit the non-author `round-16-verifier-spotcheck.md`.
- **Incident:** wave-1 seat R04 ran `GIT_DIR=<live lane>/.git bash tools/mutate-and-run.sh --selftest` from a /tmp clone. Three fixture commits (`f8832ef`, `0559c60`, `e16adb7`) moved the live lane HEAD and index at 12:29:33.
  - I restored them to `98bea7d` with `git read-tree 98bea7d` and `git update-ref --no-deref HEAD 98bea7d`; the reflog message names the repair. This was a plumbing repair outside the helper, disclosed here. No file bytes were lost (R04 verified with `git archive` plus `diff -r`).
  - Root cause fixed: GIT_* scrub in the runner and in all round-17 tools (QUALITY 27/28).
- Seat leftovers removed before commits: untracked `.ufo/evidence/round-15/attempt-N/` and `verification-N.json` written by registered `verify.py` runs on the live lane, and `__pycache__/` directories.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no fleet-root file from my seats. The untracked entries are other lanes' `.ufo/state/*.report-baseline` files and `.ufo/reports/round-19/mado.md`, which were not touched. Two wave-1 seats (S01, S07) self-recovered relative-path writes during wave 1.

## Open debts (named, not closed by prose)

- Selftest survivors:
  - evidence-disposition G3 tag-object and G5 symlink-mode guards
  - registry-check detached checkout and short-rev source regex
  - trace-inputs O_RDWR exclusion, pycache prefix and execve guard
- registry-check: `timeout_s` NaN/Infinity crash, and the timeout can be escaped through setsid.
- evidence-disposition G2/G3 compare against `HEAD`, not the branch tip.
- `tools/bash-witness-study.py` still lacks the GIT_* scrub; it needs a v2 waiver because round-13 `expected.json` pins it.
- The knowledge entry's §5 exit sentence is false.
- measure and assemble keep duplicated sectionizer and path predicates.
- The round-16 lesson debts carry forward: env scrub of the six older legs, `bwrap` confinement, successor sweeps.

## Other

- **Tool installs:** none by the L1. Seat SimplifyNewTools installed `ruff 0.17.1` and `vulture 2.16` via `uv tool install` (official PyPI, for a dead-code scan). No pacman transactions (pause respected).
- **Stale-lane:** respawn-per-round driver. The tameshi mission launched 12:07:32 -03 (`.ufo/watchdog.log:485`) and is still open at report time — progressing (six lane commits authored by tameshi since launch). No other mission of this lane is open.
- **L0 questions:** none.
- **Cross-domain evidence:**
  - mado's w1 reports name the old runner sha as "live harness" (prose only, mado-owned).
  - kaidoku's `ConnFleetJjPractice.md:86-89` claim about the staged pin-disposition is stale at the landing.
  - Both are reported here, not edited.
