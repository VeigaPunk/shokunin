# kengaku-shokunin — round 10 report

Lane: `kengaku` (child repo `kengaku-shokunin/`, axes **novelty + calibration**; domain: LLM eval/research). Report model: L1 `@m_qwen` per `MISSION.md` fleet table; L2 fleet routed per the `MISSION.md` route buckets (scout/executor/scribe @m_flash; critic/reviewer/connector/labrat/mutation-tester @m_zfl).
Axis-move: **operability 4 → 6** — a hermetic in-repo grader (`grader.py`, repo root) that replays the committed probe evidence offline and exits 0/1/2.
Pre-round HEAD `1bd17ec`; child-repo round-10 commit **`0c51208`** (pushed: `1bd17ec..0c51208 master -> master`, `VeigaPunk/kengaku-shokunin`); main-repo report commit: the commit adding this file (verify: `git -C ~/projects/shokunin log -1 --format=%h -- .ufo/reports/round-10/kengaku.md`; not cited by hash here because round 7's amended-away `85b22e3` citation is this fleet's orphaned-hash precedent).

## The move — `grader.py`, a hermetic replay gate

`python3 grader.py [--selftest] [--r8-jsonl P] [--r8-runlog P] [--r9-jsonl P] [--r9-md P]` — 936 lines, sha256 `ce64f16aeee54376296b874ae9e6ee49f4191174a416eed0299a1e8e56665e96`, stdlib only, no network, byte-identical output under `PYTHONHASHSEED` 1/99/unset. Defaults resolve beside the script: `corpus/evidence/round8-horizon/{results.jsonl,run.log}` (268 records) and `corpus/evidence/round9-replication/{results-r9.jsonl,replication.md}` (284 records). Exit 0 = every recomputed value matches the stored one; 1 = ≥1 mismatch, each printed `MISMATCH <check-id>: stored=<x> recomputed=<y>`; 2 = missing/unreadable input. Layers: md5 **pins** on the 4 evidence files (fire on default paths only, so mutated copies grade without pin noise); **meta regeneration** from seeds (r8 `700+pid*13` 10/10; r9 `2000+pid*29` 8/8, incl. the `+977` retry chain); **per-record replay** — every graded record (r8: 140 A + 32 B + 16 C; r9: 128 A) re-parsed from stored `raw` through the shipped `extract_json_block` (brace-fallback included — 2 r9 records parse only via it) and re-graded against meta-derived truth, B corrupt/propagate semantics and C `grade_c` ported verbatim from `horizon.py`; **summary replay** — all 11 `run.log` SUMMARY lines plus every stored number in `replication.md` (observed table incl. mean final `nwrong`, census, exact-binomial sign tests, onset ladder, failure classes, ack compliance, cross-round table, prediction-scoring table vs `predictions-r9.md`, sha256 chain, ordering proof). `--selftest` corrupts temp copies three ways and passes only if all three are caught with their expected check-ids (kagi `drift-pins.sh` convention). One stored value is pinned as an **adjudicated erratum pair** (`ERRATA`): r9 final-turn state errors, stored 12/32, recomputed **24/32** — editing either side without a recorded ruling fails the gate (`replication.md` §Errata; md5 pin moved `a70980a5…` → `d9235e41…`, appendix-only, reason in LOG).

Falsifiable target, quoted from `SCORECARD.md` §Planned (pre-round `1bd17ec:79-90`):

> Falsifiable target: `find . \( -name '*.py' -o -name '*.sh' \) -not -path './.git/*' | wc -l` ≥ 12 **and** the grader exits 0 on the committed files while exiting 1 on a deliberately corrupted copy (one flipped `ok` field), with both runs recorded in `LOG.md`.

Measured: count half was **already 12 pre-move** (critic finding F1 — the round-9 scorecard's "0 → 11" was wrong at birth; `git ls-tree -r 2575be6 … | grep -cE '\.(py|sh)$'` → 12), post-move **18**; the binding exit-code half is met and both runs are recorded (`LOG.md:17`).

## L2 fleet (10 agents, one batched call)

No L2 wrote into the repo (single integration owner: L1). All artifacts committed verbatim under `kengaku-shokunin/corpus/evidence/round10-fleet/` (22 files); corrections only in `INTEGRATOR-NOTES.md` (round-9 convention).

| Agent (role) | Task | Artifact (committed as `round10-fleet/…`) |
|---|---|---|
| ScoutEndpoint (scout) | `:34113` surface: `/v1/models`, `/health`, llama-server pid + full cmdline — closes PROVINCE's "never from the process cmdline" ceiling | `r10-scout-endpoint.md` + `models-34113.json`, `props.json`, `slots.json` |
| ScoutWiki (scout) | llm-wiki digest queue vs disk + freshness sweep | `r10-scout-wiki.md` |
| ScoutBench (scout) | `~/bench-arena` inventory + 3 load-bearing corpus claims re-derived | `r10-scout-bench.md` |
| CriticScorecard (critic) | adversarial re-run of 35 round-9 scorecard pointers | `r10-critic.md` + `recompute_r8.py`, `recompute_r9.py` |
| ReviewerCites (reviewer) | citation resolution: SKILL bullets, knowledge source lines, 23 prior-art URLs | `r10-review-cites.md` + `url-status.txt` |
| ConnectorSiblings (connector) | sibling gate conventions + adoption recommendations + overlap rulings | `r10-connector.md` |
| LabratSchema (labrat) | schema-invariant probe of both JSONLs before the grader was built | `r10-labrat-schema.md` + `schema_probe.py` |
| MutationHarness (mutation-tester) | M0–M3 battery written **before** the grader existed, then executed | `r10-mutation-sh.md` + `mutate_test.sh` (sha256 `ad0511f2…`), `probe_ref.py`, `final-harness.log` |
| ExecutorDocs (executor) | SKILL/README/LOG draft sections (L1 integrated, placeholders filled from own runs) | `r10-drafts.md` |
| ScribeReport (scribe) | this report's skeleton (L1 filled every `{{PLACEHOLDER}}`) | `r10-report-draft.md` + `r10-scribe.md` |

## Results

- Grader on committed bytes: `python3 grader.py` → **exit 0**, `CHECKS n=149 mismatches=0 errata_pinned=1`, `VERDICT: PASS` (145 replay checks + 4 pins).
- `--selftest` → **exit 0**, 4/4 PASS (S0 control; S1 `ok`-flip → `r8.replay.A-INC.ok`; S2 SUMMARY edit → `r8.summary.A-INC`; S3 raw-digit bump → `r9.replay.A-MONO.got`), each asserting exit code **and** expected check-id.
- Independent mutation battery (L2-written pre-grader, executed twice, byte-identical): M0 control exit 0; M1 exit 1 (exactly 1 mismatch — layer isolation proven: the flip is summary-insensitive because SUMMARY counts last-graded-turn oks); M2 exit 1 (`r8.summary.A-INC` + 2 cross-round checks); M3 exit 1 (7 mismatches) → **4/4, 100% kill rate**.
- **Failing-before evidence**: the first landed grader version failed its own M0 control (bogus `predicted_vs_observed` equality check treating the preregistered onset miss 5.0-vs-5.8 as a mismatch); caught by the independent harness (`r10-mutation-sh.md` §7.1), fixed by replacing it with a preregistration-anchor check. Recorded, not hidden.
- `python3 corpus/evidence/round9-fleet/test_harness.py` → still exit 0 (50 cases).
- Post-move runnable count: `find . \( -name '*.py' -o -name '*.sh' \) -not -path './.git/*' | wc -l` → **18**.
- SCORECARD deltas (`SCORECARD.md` §Round-10 post-move, `:116`): **operability 4→6**, calibration 6→7, freshness 5→6, coverage 6→7; depth 8→8 (held — anti-double-count ruling: this round's SKILL bytes document the operability artifact), adjacency 8→8 (held — no new arbitration), novelty 5→5 (hermetic round adds no construct). Both grader runs recorded at `LOG.md:17`.

## Calibration errata (filed, not patched)

- **F1** operability "0 → 11" wrong at birth: 12 at `2575be6` itself; which file was the 12th past the measurement is unrecorded. Filed at `SCORECARD.md` §Round-10 errata (`:68`).
- **F2** `sha256sum -c …predictions-r9.sha256.repo` exits 1 from the repo root (bare relative path; README documents the correct cwd — the scorecard cell was the one wrong statement). Now hermetic inside `grader.py` (`r9.ordering.prediction_sha256`).
- **F3 (partial)** round-9 freshness row cited evidence md5s + recomputation language as living in LOG L14; md5s sit in L13, `recomput*` had 0 hits in LOG.md. Round-10's LOG entry carries the recomputation itself.
- **Path drift**: old §Planned named `corpus/evidence/analyze.py` (absent); actual `corpus/evidence/round9-fleet/analyze.py`; gate landed at repo-root `grader.py` with lineage in its docstring.
- **Evidence erratum**: `replication.md` state-error count 12/32 → **24/32** (adjudicated pair pinned in `ERRATA`; §Errata appended; provenance of "12" labelled conjectural).
- Critic totals: 35 claims re-run → **30 REPRODUCE, 3 falsified (2 full + 1 partial)** — including full reproduction of every r9 SUMMARY cell, sign tests, onset 5.8, ordering proof, r8 SUMMARY, FIX-O blast radius (=1 flip), and md5 identity with live `/tmp/bench-r8` bytes.

## Cross-domain evidence — reported, not absorbed

| Item | Owner | Disposition |
|---|---|---|
| Serving-plane config facts: `--cache-type-k/v q4_0` (4-bit KV — unstated premise of every r8/r9 number), `--kv-unified` (2 slots × full 16384 ctx), `--no-context-shift`, `--parallel 2`, custom non-upstream chat template; pid 1299 argv == `qwen-coder.service` ExecStart (41 tokens, EXACT_MATCH) | **integrator / unowned serving plane** | interpretation kept in-lane (`PROVINCE.md` served-model row, `SKILL.md` scope-limit paragraph); flag-change authority remains unowned — escalated again |
| `~/bench-arena/loop.sh` field-count bug (`:32` emits 5 comma fields, `:63` reads 6 vars → `mok` always empty → `telemetry_source=journal` unconditionally, 33/33 v2 rows; "metrics scrape fails" premise false today — `:8080/metrics` exits 0, JVB openmetrics, 0 prompt/eval lines) — falsifies this lane's own stored causal chain | fix: **kengaku backlog** (own measurement harness; operator rule bars mid-round patching of live surfaces); semantics: **kumitate** informational | errata appended to `corpus/knowledge/bench-arena-fresh-run.md`; operational failure taxonomy must not read `source=journal` rows as scraper outages |
| Gate conventions: no sibling owns an evidence-replay gate (kagi = live-host drift pins + transcript hygiene; kotoba = live-baseline verifier; kumitate `cite-check.mjs` = citation pins — adjacent, different data); fleet-wide gate *standard* | **protocol/integrator** | referred, not imposed: exit 0/1/2 + selftest-with-check-ids + in-repo pins is a candidate fleet standard (`r10-connector.md`); round-9's `novelty`-axis routing to protocol still pending |
| llama.cpp #7052 open/closed state contested between two round-10 fetches (content quotes verify verbatim) | in-lane discipline | §Status note appended to `eval-prior-art-calibration.md`: cite issue content + fetch date, never state, without same-round re-fetch |

## Upstream-bound (operator rule: domain repos read-only)

- `~/bench-arena/loop.sh:32/:63` field-count fix — one-line class fix (emit 6 fields or read 5); battery untouched this round, fix queued in-lane; recorded here so the tooling owner/integrator can route it.
- llm-wiki: no changes needed; digest-queue sources confirmed external (arXiv 2505.06120, arXiv 2307.13702, llama.cpp #7052), fetched-and-cited in-corpus. llm-wiki unchanged since `e66e614` (2026-08-08).
- Unverified carried open: on-disk gguf vs `/v1/models` `meta.size` Δ 5,973,152 B (no 10 GB hash run) — serving-plane question, flagged to integrator.

## SHONEN four boxes (re-marked from `SHONEN.md`, commands in-file)

`[~] [~] [ ] [~]` — unchanged marks, evidence lines updated: box 1 now cites 14 anti-patterns + 472-line SKILL.md (counts re-run: `awk '/^## Benchmark anti-patterns/,/^## Research-note/' SKILL.md | grep -cE '^[0-9]+\. '` → 14); box 3 stays `[ ]` — the gate exists (`python3 grader.py` exit 0 hermetically) but no cold agent has run the checklist end-to-end; box 4 cites PROVINCE re-verified round 10 (9 surfaces, process-level pin) + 3 round-10 report-outs. No self-attested `[x]` (a lane-dispatched subagent is still the lane, `../PROTOCOL.md`).

## Mission-age actuator (fleet state at filing time)

`ls .ufo/reports/round-10/` at filing: kagi, kake, kasegi, kotoba, protocol landed; **kengaku lands with this file**; aggregator/kumitate reports not yet present for round 10.

## Next planned move

`SCORECARD.md` §Planned (`:143`): **novelty (5)** — the floor, unmoved for two rounds. Powered re-run of the emission-granularity ladder (r9's `A-CKPT4710` vs `A-CKPT710` tie 2/8 = 2/8 with severity differential 0.875→1.375) at an n sized by a **filed power analysis** hashed with predictions and ordering-proven before the first `request_ts`; the round-10 serving-stack pin (q4_0 KV, `--kv-unified`, custom template) carried as explicit experimental-unit descriptors; prior-art verdicts with fetched URLs; run bytes landed gradeable — `grader.py` SUMMARY coverage extended in the same round so `python3 grader.py` exits 0 on the extended tree and `--selftest` still passes.

## Push evidence

- Child: `git push origin master` → `1bd17ec..0c51208  master -> master` (`https://github.com/VeigaPunk/kengaku-shokunin`).
- Main: this file committed alone (other lanes' WIP left untouched in the working tree) and pushed to `https://github.com/VeigaPunk/shokunin`; verify with `git -C ~/projects/shokunin log --oneline -1 -- .ufo/reports/round-10/kengaku.md`.
- No commit or push touched any domain source repo (ufo-fsd-alpha, bounties, webzites, llm-wiki) — operator rule received mid-round, complied, and absorbed into `PROVINCE.md` report-outs.
