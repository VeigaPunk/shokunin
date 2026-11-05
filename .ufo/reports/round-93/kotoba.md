# kotoba — round 93 report (attempt 1, L1 KotobaR93; Linux host, omp)

Lane repo: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, branch `master`. Pushed lane tip at report time: **`e0c82d5511a765d84beab8ea4fc282458e89eeac`** (`git ls-remote origin refs/heads/master` = this hash; `jj-lane.sh state` → `ahead=0 behind=0`). Landing (code) commit: `ab151b17f08e8910efd5ce0d243a791b21365711`. Record commit: `372195d32e3f4f176740e41ca73afce20aa07e68`. Wave-evidence commit: `e0c82d55…` (the tip). Freeze commit: `6d7eee0570912d9f3b9d3e3d0137f3c755451233`. Round base: `5549fa9ed3cd91aeb0349178b5ba75dfe41711e7`.

## Work performed

**Declared claims (2; distinct axes; frozen before data in `plans/round-93.md` at `6d7eee05`):**

- **C1 — depth (lowest owned non-retired axis; score held 9).** The mutation battery's `--rev` path refuses a committed manifest whose kill-row count differs from `KILL_SET_PINNED` as could-not-evaluate (rc 2) naming `kill-set-size`, and labels no other baseline failure that way (round-92 closure routed defect 2 / addendum A3). Sourced on S267 (gitrevisions `<rev>:<path>`, opened this round). Measured reading: MET at `ab151b17`.
- **C2 — consistency (calibration sub-axis; score held 10).** A frozen `BATTERY` script without an `INSTRUMENT_PINS` key is a named `instrument-pin` failure; before, deleting a key silently dropped that instrument from the pin guard (round-92 routed defect 4, MutTesterBattery F-4). Measured reading: MET at `ab151b17`, with a scope limit disclosed below (the frozen predicate exercises one key).

Work items, each with its evidence pointer:

1. Pre-data, committed at the freeze `6d7eee05`: frozen counters `verifiers/fixtures/round-93/c1-killpin-rev.sh` and `c2-pinkey.sh`; forgery patches `verifiers/fixtures/round-93/forgery-c1.patch` (prefix every could-not-evaluate line with `arm kill-set-size:`) and `forgery-c2.patch` (key-count check); do-nothing receipts `.ufo/waves/round-93/receipts/redbefore-c1-base.txt` → `C1-PREDICATE-UNMET` rc 1 and `redbefore-c2-base.txt` → `C2-PREDICATE-UNMET` rc 1; forgery receipts `forgery-c1-run.txt` → UNMET (other world names `kill-set-size`) and `forgery-c2-run.txt` → UNMET (keyswap world silent on the dropped key); the positive (honest) conjuncts held in all four runs. Census at round start: `receipts/census-before.txt` rc 0.
2. Wave `r93-w1` (one v1 wave, 12 seats): `.ufo/waves/round-93/r93-w1-spec.json`, `r93-w1-dispatch.json` (`counts.spawn = 12`, one `taskCall`), `r93-w1.ready` / `.ready.dispatched`, `r93-w1-results.json`; seat outputs under `.ufo/waves/round-93/w1/`. Every seat prompt now leads with `/skill:godspeed` followed by the binding's directive bytes (`gen-w1.py` `GOD`; round-92 closure defect 3).
3. Builders: ExecKillPinRev (`w1/ExecKillPinRev/ExecKillPinRev.patch`, C1), ExecPinCoverage (`w1/ExecPinCoverage/ExecPinCoverage.patch`, C2; self-test 74 → 80), ExecReceiptRevs (`w1/ExecReceiptRevs/ExecReceiptRevs.patch`, the mined-mistake check), ScribeCorpusR93 (`w1/ScribeCorpusR93/ScribeCorpusR93.patch`: S267, S268, lesson, README row); scout ScoutGitRevs (`w1/ScoutGitRevs.md`); connector ConnectorOverlapR93 (`w1/ConnectorOverlapR93.md`, O1–O5).
4. Attack seats: ReviewerKillPin (`w1/ReviewerKillPin.md` — one blocking finding, see 5), MutTesterKillPin (`w1/MutTesterKillPin.md` — 7 mutants; the frozen counter killed 5; m3 working-tree read and m5 reorder survived it), MutTesterPinCov (`w1/MutTesterPinCov/MutTesterPinCov.md` — 6 mutants; m5 one-key hardcode survived counter and self-test), CriticClaimsR93 (`w1/CriticClaimsR93/CriticClaimsR93.md` — both MET on its candidate, defects D1–D3 in the receipt check), ReviewerPinCov (no file written; its final output in `r93-w1-results.json` records the coverage-removal mutation failing 4 new arms, and it ended while waiting on its counter run), SentinelScopeR93 (`w1/SentinelScopeR93.md`, S1–S8 PASS).
5. Integration repairs (`plans/round-93-addendum-1.md`, before any landing reading): A1 — the C1 builder's self-test rebinds `KILL_SET_PINNED` to fixture values and never restored it, so the round-92 live dropped-row arm passed against a leaked pin of 9 (ReviewerKillPin, blocking); the L1 captures the module pin on entry, passes it to both live arms and restores it in `finally` (`verifiers/check_mutation_battery.py`, self-test `0 failure(s) over 31 assertions`). Critic D1 — the receipt check's bare-word `scratch` exemption hid round-92 `bat-rev.txt:24`; only `world rev`, `forgery` or a `/scratch/` path token now exempts a line (record commit `372195d3`).
6. Landing measurements at the committed lane revision `ab151b17` (`.ufo/waves/round-93/receipts/landing/landing-rev.txt` = `REV=ab151b17…`; round-92 closure defect 1): `c1-counter.txt`, `c2-counter.txt`, `controls-run.txt`, `gate-registry.txt`, `tip-battery.txt`, `bat-selftest.txt`, `tip-selftest.txt`, `floors-selftest.txt`, `census-validate.txt`; `corpus-integrity-laneroot.txt` at the record commit.
7. Frontier step: S267 and S268 appended; same-round reject recorded; mistake `receipt-identity` mined with a fix shown able to fail (`corpus/lessons/round-93.md` § Gate, § Mistakes, § Settlement).

## Landed changes

| change | commit | LOG.md / record |
|---|---|---|
| freeze: `plans/round-93.md`, counters `c1-killpin-rev.sh`, `c2-pinkey.sh`, forgery patches, pre-data receipts, `gen-w1.py` | `6d7eee05` | LOG § Round 93 (claims as frozen; pre-data controls) |
| C1: `verifiers/check_mutation_battery.py` (`--rev` kill-set check after the target-set check; 3 rev-path self-test arms; A1 pin restore) | `ab151b17` | LOG § Round 93 (landing; integration A1) |
| C2: `verifiers/check_tip_battery.py` (coverage under `instrument-pin`; 6 self-test arms; two single-pin arms given full pins) | `ab151b17` | LOG § Round 93 (landing) |
| mistake fix `verifiers/fixtures/round-93/check-receipt-revs.sh` (new) | `ab151b17`; D1 repair `372195d3` | LOG § Round 93 (frontier step; integration D1) |
| corpus: `corpus/SOURCES.md` S267 + S268 (192 → 194), `corpus/lessons/round-93.md`, `corpus/README.md` lesson row | `ab151b17`; lesson settlement `372195d3` | LOG § Round 93 (frontier step) |
| `plans/round-93-addendum-1.md` (A1, A2) | `ab151b17` | LOG § Round 93 (integration) |
| record: LOG § Round 93, SCORECARD round-93 annotations and round-94 intentions, landing receipts | `372195d3` | LOG § Round 93 |
| wave evidence `.ufo/waves/round-93/` (spec, dispatch, ready, results, 12 seat outputs), corpus-integrity receipt | `e0c82d55` | LOG § Round 93 (wave) |

No change to SKILL.md (600 lines, byte-identical), `verifiers/fixtures/round-91/`, `verifiers/fixtures/round-92/`, the battery manifest, or any `corpus/lessons/round-*-verifier-spotcheck.md`.

## Before → after measurements

**C1 — depth.** Counting command: `bash verifiers/fixtures/round-93/c1-killpin-rev.sh <rev>` (frozen at `6d7eee05`).
- Before (base `5549fa9e`, `receipts/redbefore-c1-base.txt`): drop world rc 2 names `kill-set-size` **no** (`could-not-evaluate: baseline bat-self-test exit 1, declared 0…`); other rc 2 names no; honest rc 0 → `C1-PREDICATE-UNMET`, rc 1.
- After (`ab151b17`, `receipts/landing/c1-counter.txt`): drop rc 2 names **yes**; other rc 2 names no; honest rc 0 names no → `C1-PREDICATE-MET`, rc 0.
- Forgery (`forgery-c1-run.txt`): drop yes, other names **yes** → UNMET. Self-test 28 → 31 assertions, rc 0.
- Routed, not claimed: the counter builds only clean committed worlds, so a check that reads the working-tree manifest (MutTesterKillPin m3) survives it; there is no added-row world (m2b caught only via the honest conjunct); the self-test does not isolate the label-every-CNE forgery (F4); the other world reads rc 2 ∧ not-named without attributing cause (CriticClaimsR93 R2).

**C2 — consistency.** Counting command: `bash verifiers/fixtures/round-93/c2-pinkey.sh <rev>` (frozen at `6d7eee05`).
- Before (`5549fa9e`, `receipts/redbefore-c2-base.txt`): honest `guard instrument-pin PASS`, `guards 5 of 5`; keydrop `guard instrument-pin PASS`, `guards 5 of 5` (silent); keyswap names only the junk key → `C2-PREDICATE-UNMET`, rc 1.
- After (`ab151b17`, `receipts/landing/c2-counter.txt`): honest PASS, `guards 5 of 5`; keydrop and keyswap `FAIL guard instrument-pin: verifiers/check_correction_sweep.py has no INSTRUMENT_PINS key (battery instrument unpinned)`, `guards 4 of 5` → `C2-PREDICATE-MET`, rc 0.
- Forgery (`forgery-c2-run.txt`): keydrop named, keyswap silent → UNMET. Tip self-test 74 → 80 assertions, rc 0.
- **Scope limit (MutTesterPinCov m5):** the frozen predicate and the new self-test arms both drop the same key (`check_correction_sweep.py`). A coverage set hardcoded to that one key passes both, and a hand world that drops only `check_gate_registry.py`'s key reads `guards 5 of 5` under that mutant. The landed code iterates all six `BATTERY` paths (`check_tip_battery.py` `run_guards`); that the other five are covered is shown by code reading, not by measurement. The claim stands as frozen (one key); the five-key generalisation is routed to round 94.

**No-harm at landing (`ab151b17`).** Round-92 `controls-run.sh` → `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2`, rc 0. Gate registry `74 of 74 lane verifiers; phantom 0`, rc 0. Tip battery `guards 5 of 5; tip battery exit 0: 3 of 6` (rc 1; the same three reds as the round-92 landing: `verify_skill_checklist`, `verify_corpus_integrity`, `verify_corpus_independent`). Floors self-test `0 failure(s) over 176 assertions`. Corpus integrity at the lane root `4/9 checks pass`, the same five DRIFT names as round 92 (the two unindexed files are the closure-authored round-91 and round-92 spot-checks). Census validate rc 0. SKILL.md byte-identical.

## Sources & frontier

- **SOURCES.md rows before → after:** 192 → 194 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` at `6d7eee05` and at `e0c82d55`). Census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`: round start `receipts/census-before.txt` exit 0 (33 pre-existing W04 warnings); round end `receipts/landing/census-validate.txt` exit 0 (same W04 set, final line `kotoba ok …/corpus/SOURCES.md`), re-run after the last commit, final line `ok`.
- **Rows added by tier:** tier A ×2 — S267 (git-scm gitrevisions(7), `<rev>:<path>`, HTTP 200, 74526 B, used-by `corpus/lessons/round-93.md,plans/round-93.md`), S268 (git-cat-file(1) `-e`, HTTP 200, 79360 B). Tier B 0, tier C 0. Status `mined` ×2.
- **Rows touched old→new:** none (append-only; no existing `status`/`recheck`/`used-by` cell changed — lesson § Status changes).
- **Rejected this round (same-round reject, round-92 closure defect 5):** a 2016 Stack Overflow answer on `git show rev:path` — tier C, canonical URL answers 403 on this host, never states the naming rule; reason and flip condition in `corpus/lessons/round-93.md` § Gate.
- **Sourced claim:** C1 cites S267 (lesson § Gate, SCORECARD round-93 annotation).
- **Mined mistake:** `receipt-identity` (round-92 landing receipts named scratch revision `cd355c47…`, which never resolved in the lane) · captured-by `none` · fix `verifiers/fixtures/round-93/check-receipt-revs.sh`, shown able to fail: `.ufo/waves/round-92/receipts/landing` → `1 resolved, 5 unresolved over 18 files`, rc 1 (`receipts/landing/receipt-revs-round-92-receipts-landing.txt`); round-93 receipts → `9 resolved, 0 unresolved`, rc 0; a synthetic fabricated `REV=` line → rc 1.
- **Frontier rows advanced:** the committed-revision read class (`<rev>:<path>`) now grounds the battery's `--rev` kill-set check; receipt-identity is now a checkable property.
- **Assimilation:** none. L0 `kotoba | round-88` (55-id collision) is still open and no claim depends on it.
- **Considerthese:** `considerthese/2026-10-26.md` re-read; nothing implemented; proposal 3 carried (SKILL.md is at the 600/600 ceiling).

## Trend verdicts

- **expansion: unchanged.** No `knowledge/` entry was admitted (CORPUS rule 4). S267 and S268 are rows cited by the lesson, plan and claim evidence, not new knowledge entries.
- **quality: improved.** A committed-revision dropped kill row is now refused by name (base: unnamed baseline failure) — `c1-counter.txt` vs `redbefore-c1-base.txt`. A dropped battery pin key is now a named guard failure (base: silent) — `c2-counter.txt` vs `redbefore-c2-base.txt`. Landing receipts now name a resolvable lane revision, and a check exists that fails on receipts that do not. The self-test pin leak and the receipt-check exemption hole were caught by attack seats and repaired before landing.
- **discernment: improved, conditional.** Round-92 closure defects became fixes: D2 → C1; F-4 → C2; defect 1 → mined mistake plus check; defect 5 → a same-round reject on record; defect 3 → the godspeed lead line in every seat prompt. The non-author closure still owes the spot-check of S267, S268 and the Stack Overflow reject.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `SHONEN.md` box 1 pointers (unchanged this round; SKILL.md byte-identical at 600 lines between `6d7eee05` and `e0c82d55`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `LOG.md` § Round 93 (C1/C2 instruments built, attacked and landed; readings at `ab151b17` in `.ufo/waves/round-93/receipts/landing/`).
- [~] Instructions executable by an agent without oral context — evidence: the frozen counters `verifiers/fixtures/round-93/c1-killpin-rev.sh` and `c2-pinkey.sh` were run as committed by seats ExecKillPinRev, ExecPinCoverage, CriticClaimsR93 and MutTester* on their own candidates (`w1/*`); `SHONEN.md` box 3 pointer unchanged.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` § Adjacent unchanged; the sibling census stays red at `province rows 20 matched 4` (carried); ConnectorOverlapR93 § Part 2 sibling grep; no sibling file touched.

## Round shape, seats, and lane status

- **Shape:** ONE v1 wave `r93-w1` (band 8–16), 12 seats: executor 3 (ExecKillPinRev, ExecPinCoverage, ExecReceiptRevs), scout 1 (ScoutGitRevs), scribe 1 (ScribeCorpusR93), connector 1 (ConnectorOverlapR93), reviewer 2 (ReviewerKillPin, ReviewerPinCov), mutation-tester 2 (MutTesterKillPin, MutTesterPinCov), critic 1 (CriticClaimsR93), sentinel 1 (SentinelScopeR93). Attack seats (reviewer, critic, mutation-tester) 5 of 12 = 42 % (≥ 25 %); connectors 1 (≤ 2). No residual call. Round total 12 seats. Routing came from `task.agentModelOverrides` at spawn; no `model` was passed.
- **Planner seat:** the validator rejects `planner`; the L1 held the §3 planner seat (claim choice, freeze, controls, specs, integration). The connector's overlap scan (O1–O5) carried the planning data-walk.
- **Dead seats:** none. All 12 settled (`r93-w1-results.json`, WAVE-DONE received). ReviewerPinCov wrote no report file; its final output (in results.json) ends while it waited on its counter run, after recording the coverage-removal mutation failing 4 of the new self-test arms. ExecReceiptRevs' final output holds only an incident note, but its patch, receipts and `ExecReceiptRevs.md` are on disk.
- **Stale-lane:** none. This respawn-per-round driver has no other open mission for this lane; the round ran to landing in one L1 session.
- **Tooling:** no tool installed or upgraded by the L1 or any seat (seat final outputs); no pacman, no sysctl.
- **Scratch:** all clones were under `/fast/scratch/hyaku/kotoba-r93/`, and the tree was removed after landing (`ls /fast/scratch/hyaku | grep kotoba-r93` → empty).
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` → `M .scratch/run15-kernel.py`, `M .scratch/run15-state.json` (orchestrator-owned, not touched), `?? w4lines.txt` (a list of integers with no kotoba or round-93 content, not attributable to this lane, left in place). No kotoba seat file at the fleet root.
- **Cross-lane incident observed:** ConnectorScope-23 (kake r97) reported deleting the kake-r97 scratch parent. kotoba-r93 scratch was unaffected (ScribeCorpusR93 verified).
- **Commits:** through `jj-lane.sh commit … --as kotoba` only. Landed lines: `6d7eee05…`, `ab151b17…`, `372195d3…`, `e0c82d55…`.

## Open items and L0

- **Routed to round 94:** MutTesterKillPin F1 (no dirty-tree world), F2 (no added-row world), F4 (self-test lacks an arm for the label-every-CNE forgery); MutTesterPinCov m5 (the C2 predicate and self-test exercise one key; the other five keys are unmeasured); CriticClaimsR93 R2 (the other world does not attribute cause), D2 (a 41-hex header is silently dropped), D3 (an indented header is ignored) in the receipt check.
- **Carried, unchanged:** L0 `kotoba | round-88` (assimilation collision), `kotoba | round-73`, `kotoba | round-92` (addendum A3 ruling); sibling census red; province core red; checklist `governance.citation_resolves` red; corpus-integrity DRIFT set (five names).
- **No new L0 question this round.**
- **Verdicts are measured, not admitted:** the claim readings above are the L1's measurements at `ab151b17`. The non-author closure rules the round.
