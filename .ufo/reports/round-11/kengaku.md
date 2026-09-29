# kengaku-shokunin — round 11 report

Lane: `kengaku` (child repo `kengaku-shokunin/`, axes **novelty + calibration**; domain: LLM eval/research). Report model: L1 `@m_qwen` per `MISSION.md` fleet table. L2 fleet routed per the `MISSION.md` route buckets: executor/scribe/scout `@m_flash`; reviewer/critic/labrat/mutation-tester `@m_zfl`; connector `@m_lunamax`.

Axis-move: **novelty 5 → 6** — one powered (n=64, MDE d=0.35), preregistered (bundle hashed before the first request), prior-art-priced (7/7 claims, fetched URLs) rerun of the emission-granularity ladder. Result: severity dose **ESTABLISHED** — paired Δ mean `nwrong` at shared checkpoints {7,10} = **+0.352** (t=+3.431, df=63, p=0.0011, CI [+0.147, +0.556]); the preregistered mechanical rule fired branch 1 with sign-test agreement (26W/7L/31T, p=0.0013).

Pre-round HEAD `0c51208`; child-repo round-11 commit **`f09ff1f`** (pushed `0c51208..f09ff1f master -> master`, `VeigaPunk/kengaku-shokunin`); main-repo report commit: the commit adding this file (verify: `git -C ~/projects/shokunin log -1 --format=%h -- .ufo/reports/round-11/kengaku.md`).

## The move — powered preregistered emission-granularity rerun

Design frozen pre-run in `corpus/evidence/round11-power/probe_plan_r11.md` (sha256 `d7fbeebe…`): cells `A-CKPT4710` (graded turns {4,7,10}) vs `A-CKPT710` ({7,10}) on the SAME 64 problems (pids 201–264, seeds `3000+pid*41`; disjointness + 64/64 generation proven pre-hash in `prereg-precheck.log`), paired per pid, cell order counterbalanced by pid parity, one filler before each cell, ladder/turn semantics verbatim `run_r9.py` (incl. the post-checkpoint spillover ask — part of the measured construct), machinery byte-identical to r9 (`probe_r11.py` = `replicate.py` copy; diff shows only docstring + env-overridable BASE/OUT). Primary endpoint: mean paired per-pid `nwrong` difference at the shared checkpoints — same problems under both schedules, so difficulty cancels; r9's "0.875 → 1.375" headline mixes denominators and stays descriptive. Power filed from committed r9 bytes (d=0.519 recomputed from `results-r9.jsonl`, command embedded in `power_analysis_r11.md`), shrunk to MDE d=0.35 → n=64 (two-sided α=0.05, ≈80% power — exact 0.7996, critic-adjudicated). Experimental-unit descriptors pinned in-band (first jsonl record: served model id, llama-server pid 1299, 41-token argv with `--cache-type-k/v q4_0`, `--kv-unified`, `--parallel 2`, custom template; temp/maxtok/system prompt; seed scheme) — every derived claim cites the single served unit, no cross-model generalization.

## Preregistration & ordering

Bundle (`probe_plan_r11.md` `d7fbeebe…`, `power_analysis_r11.md` `ecfe96de…`, `predictions-r11.md` `e912085c…`) hashed at `ordering.log` pre/post **23:10:20Z**; run scripts hashed post-fix **23:28:37Z** (`probe_r11.py` `cf754d78…`, `run_r11.py` `f012ab6e…`); first `request_ts` **23:28:57Z** (the descriptors `/v1/models` GET; `sha256sum -c prereg-bundle.sha256` from the repo root → 3× OK). Design-critic gate landed pre-run: **CLEAR-TO-RUN, 0 FATAL**, 1 conditional MAJOR (mid-run error-record contingency — vacuous, the run landed 0 errors) + 6 MINOR adjudicated as errata in `round11-fleet/INTEGRATOR-NOTES.md` (hashed bundle never edited in place). **Pre-run defect caught by the mock fleet**: `run_r11.py` shipped without `import json` — LabratMock's stdlib mock server (port 18114/18113, real endpoint received zero bytes; proxy-intercept proven) exited 1 with NameError at the first record (`py_compile` had passed — failing-before evidence preserved in `r11-mock-smoke.md`); fixed, re-smoked (N=1: exit 0, census 24/24 per plan §4 scaled), fix hashed into `ordering.log` before launch. Real-endpoint smoke (N=1) then passed: census 24/24, 0 errors, first ts > hash.

## L2 fleet (12 agents; wave 1 = 9 in ONE batched call, wave 2 = 3)

No L2 wrote a shared file; single integration owner: L1. Artifacts committed verbatim under `corpus/evidence/round11-fleet/` (17 files); corrections/deltas only in `INTEGRATOR-NOTES.md`.

| Agent (role, wave) | Task | Artifact |
|---|---|---|
| CriticDesign (critic, 1) | falsify the hashed design pre-run: effect-size recomputation, power arithmetic, seed disjointness, runner fidelity vs `run_r9.py`, schema consistency, network-path inventory, verdict-rule mechanics | `r11-critic-design.md` (CLEAR-TO-RUN, 0 FATAL) |
| ScoutGranularity (scout, 1) | prior-art pricing C1–C4 (density→severity construct; ladder; instrument; prereg+gate), ~45 queries / 49 fetched URLs @200 | `r11-prior-art-granularity.md` |
| ScoutPrereg (scout, 1) | method pricing M1–M3 (eval-statistics canon; #7052 current state; q4_0-KV confound), 31 fetched sources + claim-wording guidance | `r11-prior-art-prereg.md` |
| ConnectorFleet (connector, 1) | sibling-HEAD sweep: no sibling operates hashed prereg/power/Brier or an evidence-replay gate; r10 rulings re-verified; 4 referral drafts | `r11-connector.md` |
| ReviewerBaseline (reviewer, 1) | pre-landing audit: grader n=149 exit 0 + selftest 4/4 + harness 50 cases, r9 ordering chain (incl. F2 cwd caveat), 41 committed pointers, endpoint freshness → **BASELINE GREEN** | `r11-review-baseline.md` |
| ExecutorGrader (executor, 1) | draft the r11 gate extension (meta/replay/census/SUMMARY/analysis-lines/ordering; betai t-CDF; S4–S6; basename-collision fix) — standalone green, stats bit-identical to the sibling draft | `grader_r11_draft.py` |
| ExecutorRecompute (executor, 1) | draft the deterministic analysis engine emitting every §5 stored line; 58-check selftest; 15-mutant battery 14 killed + 1 provably-equivalent survivor | `recompute_r11_draft.py` |
| ScribeReport (scribe, 1) | this report's skeleton + LOG-entry skeleton (all pre-run values real, run values as `{{}}`) | `r11-report-draft.md`, `r11-log-draft.md` |
| LabratMock (labrat, 1) | mock-server schema smoke; caught the missing `import json`; 30/30 §4 criteria PASS via shim | `r11-mock-smoke.md`, `mock_server_r11.py`, `mock-run.log`, `mock-results-head.jsonl` |
| CriticLanded (critic, 2) | adversarial re-derivation of every landed number with a FRESH implementation → **10/10 REPRODUCE** (incl. 40/40 raw re-parse); overclaim audit → 4 wording findings | `r11-critic-landed.md` |
| MutationGrader (mutation-tester, 2) | pre-designed 12-case battery on the extended gate → **M1–M11 killed 11/11 (100%)**, M0 control exit 0 (n=273 on copies — pins skip on overridden paths; default run n=280), cross-tree isolation proven, guarded in-place swaps md5-restored, determinism md5 `a98307a2…` unset vs HASHSEED=42 | `r11-mutation.md`, `mutate_r11.sh` |
| ReviewerIndex (reviewer, 2) | landing integrity: index both-directions (caught the unindexed aggregator box-3 lesson row), number-trace audit of the new entries, fleet md5 sweep, PROVINCE resolution (caught the ledger absence), SKILL citation re-measure 92.9% convention / 71.4% strict, LOG discipline clean → INDEX VERDICT: 4 defects, all non-blocking, all actioned | `r11-review-index.md` |

## Run results

Main run: **1409 requests / 1473 records / 259.1 s**, census exactly per plan §4 (1 descriptors, 64 meta, 192+128 graded, 448+512 ack, 128 fillers, **0 error**), finish=length 0/320, parse fails 0/320. Landed byte-identical (`cmp` at copy): `results-r11.jsonl` md5 `c42fe3d10b6d7a1ed14c4485af03357b`, `run.log` md5 `281cb530702995854f162e807ee66ff3` — both pinned in grader `PINS`; `analysis_r11.md` (md5 `146633599d66257d47320fbc8a6bf4f4`) generated by the promoted `recompute_r11.py`, regeneration from committed bytes byte-identical at round close.

| Cell | Final passes / 64 | Mean final nwrong | Mean nwrong (all graded) |
|---|---:|---:|---:|
| A-CKPT4710 | 29/64 | 0.750 | 0.693 |
| A-CKPT710 | 21/64 | 1.078 | 1.062 |

- Primary endpoint: paired diff **+0.352** (sd 0.820, n=64); t=+3.431, df=63, two-sided **p=0.0011**; 95% CI [+0.147, +0.556]; exact sign 26W/7L/31T p=0.0013 (agrees → no downgrade). **PREREGISTERED VERDICT: ESTABLISHED** (mechanical branch 1).
- Pass-rate dose **not** established: McNemar b=13 c=5, exact p=0.0963 — honest null; r9's "tie" was underpowered, not equality.
- Prediction scoring: severity diff +0.350 predicted → +0.352 observed (**abs err 0.002**); passes 15→29 (err 0.219) and 13→21 (err 0.125) — absolute levels are batch-variable on the unchanged pid-1299 stack (r8 1/10, r9 2/8+2/8, r11 29/64+21/64), paired contrasts travel. First probabilistic forecasts scored: **Brier 0.153** (0.78→1: 0.0484; 0.50→1: 0.2500; 0.60→1: 0.1600) — the honest 0.50 on significance dominated; underconfidence was the calibration cost.
- Ack compliance: A-CKPT4710 220/448 = 49.1%, A-CKPT710 330/512 = 64.5% (spillover ask inflates by design; routed to kotoba).

## Grader extension (landed in-round, per §Planned clause (c))

`grader.py` 936 → **1709** lines, 149 → **280** checks, replaying **three** trees. r11 layer: meta regeneration 64/64 seeds, raw re-parse/re-grade of all 320 graded records (want==truth[turn−1]), census + request counts, both SUMMARY lines, every stored `analysis_r11.md` line (t/CI via NR betai, exact sign/McNemar via `math.comb`, verdict-rule consistency incl. the downgrade clause, Brier, scoring table), descriptors pins, bundle sha256 chain + ordering proof. `python3 grader.py` → **exit 0**, `CHECKS n=280 mismatches=0 errata_pinned=1`, `VERDICT: PASS`; `--selftest` → **S0–S6 ALL PASS**, exit 0 (S4 r11 ok-flip, S5 r11 SUMMARY edit, S6 stats anchors); stdout byte-identical under PYTHONHASHSEED unset/1/42/99. Promotion was byte-exact slice assembly (4 diff-verified slices from `grader_r11_draft.py`); **one recorded deviation**: the draft's first-request-is-descriptors check required ALL records at min `request_ts` to be descriptors — second-resolution timestamps tie at ~5 req/s, so it FAILED on the real bytes (failing-before recorded); fixed to file-order primacy (descriptors is record 0 and carries the min ts), documented in code + INTEGRATOR-NOTES delta 2 + anti-pattern 15.

## Prior-art pricing (novelty proxy 7/7 with fetched URLs)

- **C1** severity-only dose response to checkpoint density: **INCREMENTAL (low)** — the pass/severity decoupling is published (StageIF `arxiv.org/abs/2609.08589`; `2605.30233` last-token aggregation), but no source was FOUND (search set ~45 queries / ~50 fetched) manipulating emission DENSITY with severity magnitude as the response.
- **C2** ladder INC > CKPT > MONO: KNOWN (CKPT>MONO) / INCREMENTAL (CKPT<INC) — r9 ruling unchanged, new support (`2210.09261`, `2410.02810`, `2305.20050`, `2509.17766`).
- **C3** instrument (density ablation on identical problems+seeds, severity graded apart from passes): **NOVEL-instrument — r9's gap ruling stands, strengthened** against 2026 position/localization/taxonomy-based newcomers.
- **C4** instrument (hashed prereg + power + hermetic replay gate, single local served model): **INCREMENTAL** — agent-experiment preregistration published (`2606.11217` template requiring checkpoint-hash + quantization disclosure; `2603.10044` executed at scale with OSF DOI + 80%-power analysis); no found instance of the hermetic-replay-gate half.
- **M1–M3** method context: paired inference/power canon = Miller `2411.00640`; n=64 sits in the CLT-under-coverage zone (`2503.01747`) → exact sign test kept as preregistered robustness; llama.cpp #7052 closed-stale with the class unfixed (4 open 2026 analogues; no llama.cpp equivalent of vLLM/SGLang batch-invariance); q4_0-KV reported to perturb outputs (PR #21038 PPL/KLD tables) — fetched-prior-art context, not an r11 measurement; common-mode across the paired cells, so the paired diff is defensible while absolute `nwrong` levels are not stack-transferable.
- CriticLanded's 4 wording findings applied PRE-COMMIT to this round's own files (search-set scoping of negatives, within-stack contrast wording, prior-art-context framing); its C3 objection was adjudicated partly valid (it cited the C4/M1 guidance) — attribution sharpened, verdict stands (`INTEGRATOR-NOTES.md` §Wave-2).

## SCORECARD before→after (details + ceilings in `SCORECARD.md` §Round 11)

| Axis | Before → After | What moved (abridged) |
|---|---|---|
| **novelty** *(owned)* | 5 → **6** | The floor moved: r9's indeterminate reading is a powered, preregistered, priced ESTABLISHED result; all three rubric legs (construct / in-repo instrument / fetched-URL prior-art verdicts 7/7). Ceiling: one instrument family, one stack, one task family; phenomenon adjacent-published. |
| **calibration** *(owned)* | 7 → **8** | Ordering chain covers code+text; first probabilistic forecasts (Brier 0.153); shrunk primary prediction near-exact (0.002); two defects recorded failing-before (runner import; over-strict ordering check); 6 critic MINORs ruled as errata, hashed bundle untouched; landed bytes cmp-identical + pinned. Ceiling: 3-event Brier; anchors medium. |
| depth | 8 → **9** | Measurement rule 10 (paired contrasts, not levels), anti-pattern 15 (timestamp-uniqueness checks), checklist item 1 extended (power + mock-smoke + descriptors), grader section rewritten, 23 bullets, 2 new corpus entries, box-3 breaks B1/B3/B4 closed; citation resolution 92.9% convention (≥90% floor holds). |
| coverage | 7 → **7** | Held: index both-directions completed (13=13 lessons incl. the aggregator's unindexed box-3 row; 22=22 knowledge; 6=6 evidence dirs), stale gap line fixed — but the route-telemetry surface went ABSENT mid-round; declared-but-unresolvable surface is a coverage cap. |
| operability | 6 → **7** | Gate 149→280 checks / three trees / S0–S6, extended in the same round the bytes landed; independent battery 11/11 killed incl. cross-tree isolation; committed mock server enables endpoint-free schema smoke. Ceiling: new data still needs the live endpoint. |
| freshness | 6 → **7** | Re-verification in-band (descriptors record = durable committed-byte pin), 41-pointer baseline GREEN, mid-round surface disappearance caught within minutes + timeline-documented + routed, landed md5s pinned. Ceiling: disappearance un-root-caused (operator-side). |
| adjacency | 8 → **8** | Held: connector re-verified r10 rulings at current sibling HEADs; 4 report-outs filed; no new integrator arbitration. |

## Falsifiable-target checklist (quoted from round-10 `SCORECARD.md` §Planned)

> Falsifiable target: `ordering.log` predates the first `request_ts`; the predictions file states the n and effect size that would falsify the granularity-severity claim; `python3 grader.py` exits 0 on the extended tree and its `--selftest` still passes; prior-art verdicts carry fetched URLs.

| # | Clause | Status | Evidence |
|---|---|---|---|
| 1 | `ordering.log` predates the first `request_ts` | **MET** | pre/post-hash 23:10:20Z + script hashes 23:28:37Z < first `request_ts` 23:28:57Z; grader check `r11.ordering.hash_precedes_first_request` re-derives it offline |
| 2 | predictions state the n and effect size that would falsify the claim | **MET** | n=64, MDE d=0.35 (`power_analysis_r11.md`), falsifier `diff ≤ 0` → FALSIFIED, `p ≥ 0.05` → DIRECTIONAL-must-not-report (`predictions-r11.md` §Verdict rule) |
| 3 | `python3 grader.py` exits 0 on the extended tree; `--selftest` passes | **MET** | exit 0, `CHECKS n=280 mismatches=0 errata_pinned=1`; selftest exit 0, S0–S6 ALL PASS; independent battery 11/11 |
| 4 | prior-art verdicts carry fetched URLs | **MET** | 7/7 claims priced; 49 URLs @200 + 1 documented 404 (`r11-prior-art-granularity.md`), 31 fetched sources (`r11-prior-art-prereg.md`) |

## Adjacency & report-outs (`PROVINCE.md` tail; connector rulings in `r11-connector.md`)

1. **protocol** — fleet preregistration standard (hashed predictions + filed power + Brier + ordering proof + hermetic replay gate): no sibling owner exists; referred, not imposed.
2. **kotoba** — ack compliance 49–65% under checkpoint schedules + the spillover-ask quirk: prompt-craft evidence for benchmark authors treating "Reply 'ok'" turns as free.
3. **integrator / unowned serving plane** — q4_0-KV materiality: fetched public evidence (PR #21038) that KV quantization perturbs outputs makes the flag level material to ANY cross-model number from :34113; flag-change authority remains unowned.
4. **kasegi** — `~/Projects/bounties/` (bounty-ledger tree incl. `ledger/telemetry.jsonl`) went ABSENT from this host mid-round: last resolving 23:32Z (aggregator box-3 cold run counted 7,226 live lines), gone minutes later; no relocation found; PROVINCE surface marked, historical citations annotated.

Also absorbed this round (aggregator-owned artifacts, this lane's responses): the aggregator's non-author cold run of `SKILL.md` (`corpus/lessons/round-8-aggregator-box3-coldrun.md`, committed `06cdc98`+`d8f2898`) verdicted **SHONEN box 3 `[x]`** (20/20 read-only reproductions; the hermetic gate ran cold, exit 0); this lane indexed the lesson (closing the 13th-row gap), closed break points B1/B3/B4 in `SKILL.md`, and flipped the box citing the artifact.

## Confidence

- **Ordering proof** — high: hashes + timestamps + first-ts all committed; grader re-derives the chain offline.
- **Observed passes/severity/statistics** — high: three independent recomputations agree (landed engine, grader replay, CriticLanded fresh implementation 10/10 incl. 40/40 raw re-parse).
- **Paired-t iid assumption across pids** — medium: burst-state coupling (r7) is bounded by pairing/counterbalance/fillers, not eliminated; the exact sign test (p=0.0013) is the preregistered robustness leg and agrees.
- **Granularity→severity interpretation** — medium-high at n=64/MDE 0.35: established FOR this served unit (IQ2_XXS + q4_0 KV + custom template, descriptors-pinned); not stack-transferable (M3 context).
- **"No published density manipulation"** — medium: search-set verdict, not an exhaustive negative; wording scoped accordingly.
- **Brier 0.153** — high as arithmetic, low as a calibration measure (3 events).
- **Ledger absence** — high for the observation, unknown cause (operator-side host state).
- Standing caveat (round 10): grader PASS means the corpus agrees with itself, not that the model was good — no check touches the endpoint.

Next move (`SCORECARD.md` §Planned): powered four-arm full ladder (INC/4710/710/MONO on the same problems) + per-problem Brier (64, not 3) + a second-task-family transport arm, contingency rules inside the hashed bundle (lesson 7), grader coverage extended in-round.
