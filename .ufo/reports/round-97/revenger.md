# revenger — round 97 (hyaku run 15, attempt 1)

Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin` · lane head pushed: `e95e2fd5b841ec50196cb0e03269298ecca02ef9` (`git ls-remote origin refs/heads/main` prints the same hash) · landing commit (measured): `47e4f6c9425c0d74e256991dd29dfa1d98001f22` · claims freeze: `3b4b4e5c1d123d5fc5337ad59015b4752366854a` · v6 counter freeze: `85a2c7eb0a980413a62cd9330ffd5b7e9005c332`.

## Work performed

**Declared claims (2; axes coverage and calibration; `reports/round-97/claims.md`).**
- **C1 — coverage, K 12/15 → 13/15.** Row C02 `partial → held` through a v6 admission counter, on the round-96 candidate entry (vote digest `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923`). Coverage is the lane's lowest owned criterion (K 8.0).
- **C2 — calibration, counter reach over routed forgery vectors.** Frozen v5 accepts 14/19 (round-96 receipts); target v6 accepts 0/19 on the 19 frozen vectors, with a positive control and a stub check.
- **Frontier step (§2b):** sourced claim (S502/S503 re-opened this round), mined mistakes, census before and after, considerthese proposal 1 mined. Assimilation: none (reason in Sources & frontier).

**Wave and dispatch.** One v1 wave, 10 seats (executor ×3, scout ×1, scribe ×1, connector ×1, reviewer ×2, critic ×1, mutation-tester ×1); attack share 4/10 (reviewer ×2, critic, mutation-tester), connector seats 1; planner held by the L1 (not dispatched); no residual call; round total 10. Spec `.ufo/waves/round-97/w1-spec.json`; `plan` rc 0 (`w1-plan.out`, `w1-validate.err` empty); `run` rc 0 (`w1-run.out`, copied to `w1-dispatch.json`); handoff `.ufo/waves/round-97/w1.ready` (dispatched, marker present); `WAVE-DONE w1` received; results `.ufo/waves/round-97/w1-results.json`. Dead seats: none recorded. The orchestrator kernel restarted mid-wave and seat output was not retained, so the wave-dir reports are the evidence; all ten wrote their findings files.

**Work items and evidence pointers.**
- Do-nothing controls, pre-freeze: `reports/round-97/controls/c1-do-nothing-v5.log` (v5 on base `7d380ce`: `C1_VERDICT=fail`, K 12/15, only failing leg `C1_SOURCES`); `controls/c2-v5-reach-from-r96-receipts.txt` (`C2_V5_ACCEPTED 14 / 19`).
- v6 counter (ExecCounterV6): `reports/round-97/c1_k_admit_counter6.py`; red/green/base/self-test logs in `reports/round-97/controls/` (`red-v5-corpus-prefix.log` rc 1 vs `green-v6-corpus-prefix.log` rc 0; `red-v5-decorated.log` `C1_ADMITTED_UNION=pass` vs `green-v6-decorated.log` fail; `base-v6.log` fail 12/15; `selftest-v6.log` rc 0). Seat findings: `.ufo/waves/round-97/w1/ExecCounterV6.md`.
- C2 harness (ExecForgeryHarness): `reports/round-97/forgeries/` (19 vector builders, manifest) and `reports/round-97/forge_reach6.py`. Frozen v5 reproduces 14/19 with a per-delta match against the committed receipts (`controls/c2-v5-reproduced.log`); self-test stubs 19/19 and 0/19 (`controls/c2-stub-selftest.log`). Seat findings: `.ufo/waves/round-97/w1/ExecForgeryHarness.md`.
- Skip-work controls and paper table (ExecControls): `reports/round-97/controls/skip-work/`, `reports/round-97/controls/skip-work-table.md` (six rows), `controls/c2-count-audit.log` (`accepted 14/19`).
- Source re-open (ScoutReopen): S502 and S503 re-fetched 2026-11-05 at `12f6e09`: HTTP 200, 38167 and 35095 bytes, sha256 `c818ee34…`/`b5f17fdf…`, byte-identical to the committed r96 bodies (`cmp` exit 0), located quotes verbatim (grep count 1). S504 located quote absent from the saved bytes (grep count 0) → D1 confirmed, replacement span supplied. `.ufo/waves/round-97/w1/ScoutReopen.md`.
- Connector scan (ConnectorOverlap): no other admission counter normalizes `admission-status` with `used-by` (0 hits in scripts, exit 1); the "skip-work"/"do-nothing" phrase hits are generic (45,278) and are reported, not absorbed. `.ufo/waves/round-97/w1/ConnectorOverlap.md`.
- Claim review (ReviewerClaims): recounts confirmed (12/15 base; 14/19 receipts); the 13-vs-14 mismatch is in the r96 SCORECARD only, not the lesson; "exactly once across the rows" is per-row; the positive control must be part of the frozen C2 output. Adopted as Amendment A in `claims.md`, recorded before the v6 freeze. `.ufo/waves/round-97/w1/ReviewerClaims.md`.
- Advisory Q01–Q17 gate audit (ReviewerGate; not a vote): FAIL 0; vote-binding digest re-derived `2f7d4c1b…d923` (MATCH). `.ufo/waves/round-97/w1/ReviewerGate.md`.
- Fresh holdout (CriticR97): 12 named-class forgeries + 3 unsigned variants, not in FG01–FG20; frozen v5 accepts 8 of 12 named (FR02, FR06, FR07, FR08, FR09, FR10, FR11, FR12). Builder `.ufo/waves/round-97/w1/CriticR97/fresh/build_fresh.py`. `.ufo/waves/round-97/w1/CriticR97.md`.
- Mutation harness (MutationR97): `reports/round-97/mutants/mutate.py`; frozen v5 tree-kill `MUTANT_KILL_V5=81/117` (`.ufo/waves/round-97/w1/MutationR97/mutate-run-v5.out`); `d-host` survives. `.ufo/waves/round-97/w1/MutationR97.md`.
- Post-freeze measurements (L1, committed bytes): see Before → after.
- Lesson: `corpus/lessons/round-97.md` (gate, mistakes M5/M8/M9/M10, frontier, considerthese).
- Registry: SKILL.md gate-registry blocks for `c1_k_admit_counter6`, `forge_reach6`, `mutate` (`SKILL.md:604–622`).

## Landed changes

| commit | content | LOG.md entry |
|---|---|---|
| `3b4b4e5c1d123d5fc5337ad59015b4752366854a` | claims freeze and do-nothing controls (`reports/round-97/claims.md`, `controls/`) | Round 97 entry (motivating evidence) |
| `85a2c7eb0a980413a62cd9330ffd5b7e9005c332` | v6 counter, C2 harness and 19 vectors, skip-work controls, mutation harness, Amendment A, wave-1 evidence | Round 97 entry |
| `47e4f6c9425c0d74e256991dd29dfa1d98001f22` | **landing**: `corpus/README.md` (C02 `partial → held`, knowledge cell = the entry only); `corpus/knowledge/round-96-native-analysis-sessions.md` (`admission-status: candidate → admitted`); `corpus/SOURCES.md` (+S505, supersedes S504); `corpus/lessons/round-97.md`; `SCORECARD.md`; `LOG.md`; `SKILL.md` (three probes); `reports/round-97/controls/`; wave evidence | Round 97 entry |
| `e95e2fd5b841ec50196cb0e03269298ecca02ef9` | adjudication: landing-tree measurement logs (`reports/round-97/controls/measured-at-landing/`) | — |

Fleet repo: `.ufo/l0-questions.md` round-97 line (assimilation id collision) is at HEAD already; no other lane's uncommitted lines were committed.

## Before → after measurements

| claim | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| C1 coverage K | `K_HELD_BACKED` **12/15 (8.0) → 13/15 (8.67)**; C02 `partial → held` | `PYTHONUTF8=1 python3 -B reports/round-97/c1_k_admit_counter6.py --tree <archive of 47e4f6c>` → `C1_K_HELD_BACKED=13/15`, `C1_VERDICT=pass` (`controls/measured-at-landing/c1-v6-landing-47e4f6c.log`, rc 0). Before: same counter on archive of `7d380ce` → `12/15`, `C1_VERDICT=fail` (`controls/base-v6.log`; v5 `controls/c1-do-nothing-v5.log`) | `7d380ce` → `47e4f6c` | **improved on the frozen counter.** Admission awaits the non-author closure (LEARNING.md; the r96 votes are lane-internal). |
| C2 calibration | frozen v5 `C2_ACCEPTED` **14/19 → 0/19** (v6, frozen vectors) | `PYTHONUTF8=1 python3 -B reports/round-97/forge_reach6.py --counter reports/round-97/c1_k_admit_counter6.py --deltas reports/round-97/forgeries --work <scratch>` → `C2_ACCEPTED=0/19` (`controls/c2-v6-frozen.log`, rc 0); v5 reproduction `14/19` (`controls/c2-v5-reproduced.log`) | `85a2c7e` (v6); landing `47e4f6c` | **met on the frozen predicate; contested.** The 19 vectors were used during v6 development (Amendment A5), so 0/19 is a development-set result. |
| C2 positive control | honest landing accepted | `PYTHONUTF8=1 python3 -B reports/round-97/c1_k_admit_counter6.py --tree <full mirror of 47e4f6c>` → `C1_VERDICT=pass` (`controls/c2-positive-landing-v6.log`) | `47e4f6c` | pass |
| C2 stub check | always-pass 19/19; always-fail 0/19 | `PYTHONUTF8=1 python3 -B reports/round-97/forge_reach6.py --self-test --work <scratch>` (`controls/c2-selftest-v6.log`) | `85a2c7e` | pass (harness check, not a gain) |
| C2 fresh holdout (not a target) | **8/12 → 5/12** named forgeries accepted (v5 → v6). v6 accepts FR02, FR08, FR09, FR10, FR12; refuses the other seven. Unsigned variants refused by `C1_VOTES`. | `python3 -B .ufo/waves/round-97/w1/CriticR97/fresh/build_fresh.py --work <scratch> --lane <lane>` (v6 run: scratch copy with `COUNTER` set to the v6 path; `.ufo/waves/round-97/w1/CriticR97/holdout-v6.log`) | `85a2c7e` | reported, not part of the target |
| mutation (tree kill) | v5 **81/117** → v6 **107/140** (self-test v6 137/140) | `python3 -B reports/round-97/mutants/mutate.py --counter <counter> --out <scratch> --kill-tree <base archive> --selftest --label V6 --jobs 6` (`controls/mutate-v6-kill.out`) | `7d380ce` base | denominators differ (117 vs 140), so not a ratio. `d-host` survives on v6. |

Recorded deviations from the claims:
- **Amendment A2** specified the three C2 outputs (`C2_ACCEPTED`, `C2_POSITIVE`, `C2_STUB_SELFTEST`) in one recorded run. They are three logs on the same committed counter bytes (`c2-v6-frozen.log`, `c2-positive-landing-v6.log`, `c2-selftest-v6.log`). This is disclosed; no counter byte changed between them.
- The holdout's printed outcome column contains static labels from the seat script (`ACCEPTED-by-v5`); the verdict column is the observed outcome.
- The C1 landing counter is the same counter; its verdict is `C1_VERDICT=pass` on 47e4f6c, and `C1_ONLY_C02` reports no other coverage row changed.

## Sources & frontier

- **SOURCES census, before** (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`, at `7d380ce`): exit 0; warnings only (21 × W01, 13 × W04); 0 E-codes.
- **SOURCES census, after** (same command on the working tree at the landing bytes; `reports/round-97/controls/census-round-end.log`): exit 0; 0 E-codes; same 34 warnings. Landing archive file check `sources-census.sh validate --file corpus/SOURCES.md`: exit 0 (`controls/measured-at-landing/summary-47e4f6c.txt`).
- **Rows:** 504 → 505 (S505 appended). Rows added by tier: tier A ×1 (S505, own-work, `mined`, opened 2026-11-05, `used-by` the candidate entry exactly once; `teaches` opens `supersedes S504 —`). Rows touched old → new: none in place (S502, S503, S504 keep `mined`, `recheck=on-release`, `opened=2026-11-05`, used-by).
- **Frontier rows advanced:** C02 coverage row `partial → held` (coverage-map frontier → core) on the frozen counter. The row's knowledge cell now cites only the admitted entry; the two pre-contract references it carried (`knowledge/seed.md`, `knowledge/2026-10-12-rea-readiness-checklist.md`) remain in the knowledge base and are no longer cited from that row (disclosed).
- **Sourced claim (§2b.4):** C1 rests on S502 and S503, both re-opened 2026-11-05 at `12f6e0974cc0db0b3a9b86246accc76556837222` (`.ufo/waves/round-97/w1/ScoutReopen.md`), quotes verbatim.
- **Mistakes mined** (`corpus/lessons/round-97.md ## Mistakes`): M5 used-by path-form miss (captured-by none; fixed in v6, red-before shown); M8 the 13-vs-14 count (captured-by none; fixed by counting from receipts); M9 own-work quote not byte-verbatim (captured-by `C1_QUOTES`; fixed by S505, byte-exact leg routed); M10 fresh holdout accepts 8/12 under v5 (captured-by the frozen 19 vectors only; v6 accepts 5/12; routed).
- **Assimilation:** none. `merge/revenger/` stages 155 rows and all 155 staged ids collide with the registry (`.ufo/waves/round-97/assimilation/collisions`, 155 lines; registry 504 ids; guard canary proved). Mass id drift → L0 question (`.ufo/l0-questions.md`); nothing adopted; the round-91 question is still open.
- **considerthese:** proposal 1 of `considerthese/2026-11-05.md` (counter-reachability review) mined and implemented as `reports/round-97/controls/skip-work-table.md`. Not a claim.

## Trend verdicts

- **expansion: improved.** Coverage K 12/15 → 13/15 (C02 held) on the frozen counter; admission still needs the non-author closure.
- **quality: unchanged.** No new knowledge beyond the C02 entry; S505 is a quote correction, not new knowledge; no depth, freshness or operability move.
- **discernment: improved.** C2 is met on its frozen predicate on the development set (14/19 → 0/19), and the fresh holdout drops 8/12 → 5/12 accepted. It is not fully discriminating: v6 still accepts five holdout forgeries, and `d-host` survives. The verdict is contested by these numbers, not a pass.

No axis harmed: `git diff --stat 7d380ce 47e4f6c -- PROVINCE.md corpus/QUALITY.md` is empty; `C1_ONLY_C02` reports no other coverage row changed; the holdout and mutation results are reported as they are.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — round-97 registry blocks added (`SKILL.md:604–622`) and run (`reports/round-97/controls/c2-v6-frozen.log`). No non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — C02 held on the frozen counter over the landing archive (`reports/round-97/controls/measured-at-landing/c1-v6-landing-47e4f6c.log`; LOG.md round-97 entry). No non-author verifier.
- [~] Instructions executable by an agent without oral context — counter, harness and mutation commands run from committed bytes (`controls/c2-v6-frozen.log`, `controls/mutate-v6-kill.out`). No outside verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` byte-unchanged; connector scan found no overlapping admission counter (`.ufo/waves/round-97/w1/ConnectorOverlap.md`).

## Stale-lane

No. This round progressed (wave writes, lane commits, measurements); no other mission of this lane is open.

## Tool installs

None. The seats and the L1 used only python3 stdlib, curl, git and the lane's own scripts. No pacman, uv, npx or cargo installs. No host sysctl was touched.

## Misroot and inherited-state sweep

- Fleet root `git status --porcelain` at report time: `.scratch/run15-state.json` (orchestrator-owned, not touched), `.ufo/l0-questions.md` (contains my round-97 line already at HEAD, plus two other lanes' uncommitted lines, not committed by me), `.scratch/closure-souji-r69.json` (souji's, not touched), `w4lines.txt` (bare numbers; names no lane or round, so not attributable to this lane's seats; left in place). No misroot from this round's seats.
- Round-96 spot-check items (`corpus/lessons/round-96-verifier-spotcheck.md` §5): D1 done (S505, byte-verbatim span, ScoutReopen §3). D2 (a SCORECARD correction naming M7) **not done**: the v6 counter prints the executed leg count, but no separate SCORECARD line names M7; routed to r98. D3: M5 and M6 done; CriticR96 F1 done (decorated line); F2–F14 addressed for the 19 frozen vectors; M4 (`claude-red-re-bridge.md` index-or-reject) **open**; MutationR96 `d-host` **survives**. D4 (planner seat): no planner dispatched; the L1 held the seat (prompt §2 ruling); not dispatched by validator.
- No `corpus/lessons/operator-*.md` teaching is present in the lane.

## Open items and routed work

- Non-author closure of C02 (LEARNING.md) — required before admission.
- r98 candidates: holdout forgeries FR02, FR08, FR09, FR10, FR12 as frozen v7 legs on a new freeze with a new fresh holdout; a row-set leg (ids C01–C15, one row each), so the K-inflation refusal is designed, not incidental (FR06/FR07 are refused today only by `C1_ADMITTED_UNION`); a byte-exact own-work quote leg (M9); the 33 v6 tree-mutant survivors and `d-host`; M4 index-or-reject; the M7 SCORECARD line (D2).
- L0: the assimilation id collision (`.ufo/l0-questions.md`, round-97 line; round-91 line still open) needs an operator ruling: renumber in scratch or refuse the package.
