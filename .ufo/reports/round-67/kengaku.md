# kengaku — round 67 (hyaku run 15, attempt 1), 2026-11-03

Lane-root base, stated once: `/home/vgpnk/Projects/shokunin/kengaku-shokunin`. Wave paths below are relative to it (`.ufo/waves/round-67/w1/...`). Lane tip at filing: `f600c6d3f03a8bc4f10e624897a65b520ec81a6f` (`git -C /home/vgpnk/Projects/shokunin/kengaku-shokunin ls-remote origin refs/heads/master` prints the same hash). Base `4bc29fd8`; freeze `dcc39ea3`; round commit `69ccfd04` (receipt of record under counter A1, strict-gate landing, wave evidence); evidence commit `f600c6d3` (pre-landing `--strict` absence receipt, SCORECARD erratum). Fleet L0 questions appended in `.ufo/l0-questions.md` (two lines, round-67).

## Work performed

**Declared claims (2).**
- **R67-C1 — coverage** (lowest owned axis, L0-capped at 7; capability acquisition `offline-torch-pipeline-parallel-grader-probe`). Execute the pinned TB2 `torch-pipeline-parallelism` grader offline against six frozen cases (four legs each). **Verdict: admitted on the amended counter** — predicate met, capability enters, coverage held at 7 (a grader execution does not lift the L0 cap `kengaku | round-25/33/51`).
- **R67-C2 — operability** (held at ceiling 10; round-65 SecurityScan M-1 successor). Add a `--strict` mode to the R65 sqlite receipt checker that refuses the fabricated fixture and accepts the committed R65 receipt, with the default mode unchanged. **Verdict: admitted on the frozen predicate** (kill rules a, b, c not triggered). Score held at 10. Named gap found by the attack seats and stated as found: strict does not bind ENV values (`ENV G5 version=0.0.0-forged-no-such-binary` passes; `corpus/evidence/round67/...` ClaimFalsifier A3, `.ufo/waves/round-67/w1/ClaimFalsifier/falsify.md`).

Frontier step (inside the claim cap, not a claim): two live-opened sources S238 (grader) and S239 (instruction), one sourced claim (C1 rests on S238/S239); mistake mining (lesson rows 1–10); knowledge entry `corpus/knowledge/tb2-torch-pipeline-parallel-offline.md`; Assimilation: none; considerthese: not mined this round.

**Work items, each with its evidence pointer.**
- Protocol load: `skill://godspeed`, the round prompt in full, `RULES.md`, MISSION/AXES, SCORECARD (round-66 post-move, planned round 67), SHONEN, PROVINCE, QUALITY, README frontier, round-66 closure (`corpus/lessons/round-66-verifier-spotcheck.md`).
- Dev build check (disclosed; no table change): one `run_case` of `q1-ref` in scratch (`PPPP`, 13 s) before the freeze. The table was written before that run.
- Host install (tool record below): `venv-pipe` with torch `2.15.0+cpu`, transformers `5.22.1`, pytest `9.2.0`.
- Frozen C1 artifacts at `dcc39ea3`: `plans/round67_c1_pipeline_probe.py`, `plans/round-67-claims.md`, `corpus/evidence/round67/pipe/cases/{q1-ref,q3-stub,q4-hooks-noop,q5-full-model,q6-unscaled-loss}/pipeline_parallel.py` (q2-none is an empty `/app`), `corpus/evidence/round67/sources/` (S238 grader, S239 instruction; `cmp`-identical to the round-52 capture, `corpus/evidence/round52/graders/SHA256SUMS:169`), registry rows S238/S239 in `corpus/SOURCES.md`.
- Receipt of record, post-freeze (`python3 plans/round67_c1_pipeline_probe.py --run --work /fast/scratch/hyaku/kengaku-r67/record`): `corpus/evidence/round67/pipe/receipt-prea1.txt` (+ `receipt-prea1.junit/`), `CHECK ok cases=6` / `PREDICATE R67-C1 pass`; all six `VECTOR` lines `frozen=match` (q1-ref PPPP, q2-none FFFF, q3-stub PPFF, q4-hooks-noop PFPP, q5-full-model PPPF, q6-unscaled-loss PPFF).
- Wave `w1` (13 seats, §Round shape) reviewed the counter: ProbeReview M1 (missing VECTOR accepted), M2 (VECTOR before CASE silently unbound), S1–S4, N1–N6 (`.ufo/waves/round-67/w1/ProbeReview/review.md`); ProbeMutate survivors m02, m11, m12, X (`.ufo/waves/round-67/w1/ProbeMutate/mutations.md`).
- **Amendment A1 (dated, `plans/round-67-claims.md`, appended)**: counter enforces its own frozen predicate sentence; the record re-issued under it: `corpus/evidence/round67/pipe/receipt.txt` (PROBE sha `32bacf1d…`), `receipt.junit/`; `python3 plans/round67_c1_pipeline_probe.py --check-receipt corpus/evidence/round67/pipe/receipt.txt; echo $?` → `CHECK ok cases=6`, `PREDICATE R67-C1 pass`, exit 0. Red-after evidence: `corpus/evidence/round67/pipe/a1-mutants.txt` (8 killed, 1 accepted by design: line order is not in the predicate). Self-test: `--selftest --work …` → `SELFTEST green_rc=0 red_rc=1 ok`.
- Case audit (CaseAudit): all six files conform to the claim text; sha256 of each committed case equals the receipt's `case_sha256`; junit sha binding holds (`.ufo/waves/round-67/w1/CaseAudit/audit.md`).
- Labrat-style hypothesis H-AFAB (AfabLab, run as executor; the labrat role is rejected by the policy): a one-forward-one-backward variant passes the ws1 leg of the frozen grader; the dictionary-order AFAB check does not separate it from AFAB at world size 1; world size 2 not run (`.ufo/waves/round-67/w1/AfabLab/labrat.md`).
- Falsification (ClaimFalsifier, critic): A1 hook-name evasion earns `exists=P no_hooks=P ws1=P` (the table has no row for it; named limitation); A2 forged receipt with hand-written junit passes `--check-receipt` (BROKEN THROUGH: yes; named limitation, not patched after data); A3 strict accepts an ENV-value forgery (overclaim of the C2 limitation sentence, mined as lesson row 8); A4 overclaim in two claim sentences (mined as row 10) (`.ufo/waves/round-67/w1/ClaimFalsifier/falsify.md`).
- Sandbox review (SecurityScan, sentinel): must-fix — a candidate-spawned process can write `/ctl/junit.xml` after the verdict (lane-authored cases only; no kill rule triggered; routed, not patched) (`.ufo/waves/round-67/w1/SecurityScan.md`).
- Source re-read (SourceReview, Q10 second seat): S238 and S239 re-fetched live at the pin (HTTP 200; sha256 `23574246…` and `989bfcf0…`), every quote and line verified verbatim (`.ufo/waves/round-67/w1/SourceReview/source-review.md`).
- Connector sibling scan (ConnectorOverlap): 5 term-level overlaps, none routed, no frozen text needs change (`.ufo/waves/round-67/w1/ConnectorOverlap/overlap.md`).
- **R67-C2 strict gate**: the StrictGateBuild proposal (`.ufo/waves/round-67/w1/StrictGateBuild/proposed/round65_c1_sqlite_probe.py`, sha `27e8b41f…`) implements clauses s1–s6 as frozen (`.ufo/waves/round-67/w1/StrictGateBuild/report.md`); landed byte-for-byte into `plans/round65_c1_sqlite_probe.py` (`f44b7283…` → `27e8b41f…`). Pre-landing `--strict` absent: `corpus/evidence/round67/strict/before-strict-absent.txt` (usage error, rc 2). Post-landing: fabricated `--strict` rc 1 with 24 `CHECK defect:` lines (`corpus/evidence/round67/strict/fabricated-strict.txt`); committed `--strict` rc 0 `PREDICATE R65-C1 strict-pass` (`corpus/evidence/round67/strict/committed-strict.txt`); default mode over the committed receipt byte-identical before and after (`corpus/evidence/round67/strict/committed-default-before.txt` vs `committed-default-after.txt`, `cmp` rc 0); default over the fabricated fixture unchanged, rc 0 (`fabricated-default-after.txt`, the pre-existing M-1 limitation stays stated).
- Fixture runner: ReceiptMutate built 11 fixtures (clauses s1–s6) with `expected.tsv`; `sh .ufo/waves/round-67/w1/ReceiptMutate/run_strict_fixtures.sh plans/round65_c1_sqlite_probe.py` → `RESULT fixtures=11 mismatches=0`, rc 0 (`corpus/evidence/round67/strict/fixture-runner.txt`).
- Knowledge entry and lesson drafted by scribes (`.ufo/waves/round-67/w1/KnowledgeDraft/entry.md`, `LessonDraft/lesson.md`), landed as `corpus/knowledge/tb2-torch-pipeline-parallel-offline.md` (with appended post-data findings) and `corpus/lessons/round-67.md`; knowledge trio gate `python3 plans/round63_gate_checks.py trio corpus/knowledge/tb2-torch-pipeline-parallel-offline.md` → `TRIO pass`.
- Depth gate after the SKILL row update: `python3 plans/round63_gate_checks.py depth --skill SKILL.md --receipt corpus/evidence/round62/class-survey.txt` → `ROWS n=16 class_match=True count_mismatch=0 paths total=32 resolved=32 share=1.00`, `PREDICATE R63-C2 pass`, rc 0 (a first attempt failed on a missing pointer cell; repaired before the commit).

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| Frozen R67-C1 probe, six cases, claims doc, sources S238/S239, registry rows | LOG.md Round 67 (Landed R67-C1) | `dcc39ea3` (freeze, pushed) |
| Receipt of record and junit under counter A1; A1 amendment in claims doc; A1 mutants | LOG.md Round 67 (Amendment A1) | `69ccfd04` |
| R67-C2 strict mode in `plans/round65_c1_sqlite_probe.py` (proposal sha `27e8b41f…`); strict evidence | LOG.md Round 67 (Landed R67-C2) | `69ccfd04` |
| Knowledge entry `corpus/knowledge/tb2-torch-pipeline-parallel-offline.md` (+ post-data findings); lesson `corpus/lessons/round-67.md` (Mistakes 1–10) | LOG.md Round 67 | `69ccfd04` |
| SKILL process-environment row (executed 2 of 3); `corpus/README.md` index row and round-67 block | LOG.md Round 67 | `69ccfd04` |
| Wave w1 evidence (spec, dispatch, seat reports, results) | LOG.md Round 67 | `69ccfd04` |
| SCORECARD round-67 section; pre-landing absence receipt; SCORECARD erratum | LOG.md Round 67 | `f600c6d3` |

Fleet side: two L0 questions appended to `.ufo/l0-questions.md` (receipt provenance; the labrat role rejected by the wave policy).

## Before → after measurements

Counting commands run at the stated revisions. Revisions: before = `4bc29fd8`; after = `69ccfd04` (`f600c6d3` adds only the absence receipt and the erratum).

| claim / axis | before | after | counting command | verdict / score |
|---|---|---|---|---|
| R67-C1 / coverage (capability) | `git show 4bc29fd8:corpus/evidence/round52/graders/executed17.lst \| grep -c torch-pipeline-parallelism` → `0` (rc 0); no receipt for the pipeline grader; process-environment executed 1 of 3 | `python3 plans/round67_c1_pipeline_probe.py --check-receipt corpus/evidence/round67/pipe/receipt.txt; echo $?` → `CHECK ok cases=6`, `PREDICATE R67-C1 pass`, exit 0 (at `69ccfd04`); process-environment executed 2 of 3 (SKILL row) | the command above; `python3 plans/round67_c1_pipeline_probe.py --selftest --work <scratch>` → `SELFTEST green_rc=0 red_rc=1 ok` | predicate met; capability enters; coverage held at 7 |
| R67-C2 / operability (held at 10) | `python3 plans/round65_c1_sqlite_probe.py --check-receipt corpus/evidence/round66/red/fabricated-r65.txt --strict; echo $?` → usage error, rc 2 (`corpus/evidence/round67/strict/before-strict-absent.txt`); default on fabricated, rc 0 (M-1) | `--strict` fabricated → rc 1 (24 `CHECK defect:`); `--strict` committed → rc 0; default committed byte-identical; fixture runner `RESULT fixtures=11 mismatches=0` | the three commands in the claim and the runner `run_strict_fixtures.sh` | predicate met; kill rules not triggered; score held at 10 with a named ENV gap |
| Counter A1 (R67-C1 instrument) | pre-amendment counter accepted m02, m11, m12, X (all rc 0) | amended: m02, m11, m12, X, duplicate, unknown, GRADER-extra, missing-junit all rc 1; one line-reorder rc 0 by design | `corpus/evidence/round67/pipe/a1-mutants.txt` | instrument gap closed with red→green evidence |

Scores after the round: coverage 7 (held, L0 cap), operability 10 (held), calibration 10 (held), depth 10 (held), freshness 10 (held), adjacency 9 (held), novelty 8 (held). No axis harmed.

## Sources & frontier

- **SOURCES before → after.** Data rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`): before `229` (at `4bc29fd8`, `git show 4bc29fd8:corpus/SOURCES.md \| grep -cE …`), after `231` at `69ccfd04`. Rows added by tier: `A` 2 (S238 code A; S239 docs A). Rows touched old→new: none (no `status`, `recheck` or `used-by` of an existing row changed; S238/S239 `used-by` set to the knowledge entry at landing, from the claims doc at freeze, as the census requires).
- **Census.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku` → `kengaku ok …/corpus/SOURCES.md`, rc 0 at round start (229 rows, R66 closure) and at round end (rc 0, 231 rows).
- **Frontier rows advanced.** The TB2 per-task grader frontier (`corpus/README.md` §Frontier, "Agentic benchmark task-spec audits"): discharged for one further task only (`torch-pipeline-parallelism`: grader executed offline and read against its instruction). The remaining TB2 graders, SWE-bench Pro V2 beyond the round-31 task, and Toolathlon stay open.
- **Sourced claims.** R67-C1 rests on S238 (grader) and S239 (instruction), both opened live this round.
- **Assimilation.** none — no `merge/kengaku/` theme adopted; L0 `kengaku | round-54` (id drift) stays open.
- **considerthese.** not mined this round.
- **Mistakes mined.** `corpus/lessons/round-67.md` rows 1–10: rows 1–4 are round-66 carry items (row 1 is the R66-C2 PROBE-line predicate; rows 2–4 are routed landing and pointer defects of round 65/66 with their fixes still open); rows 5–10 are mined this round (A1 counter gaps; forgeable receipts; candidate junit write; ENV overclaim; untracked receipt; claim-text overclaim). Sweep: `corpus/lessons/round-67.md` `## Sweep` section lists the sections read of the round-66 spot-check.
- **Source repo.** Domain source trees not touched; `/home/vgpnk/Projects/shokuknow` not touched.

## Trend verdicts

- **expansion: improved** — a second executed `process-environment` member; two live-opened registry rows; one knowledge entry; the class row moves executed 1 → 2 of 3 (evidence: `corpus/evidence/round67/pipe/receipt.txt`, `corpus/knowledge/tb2-torch-pipeline-parallel-offline.md`).
- **quality: improved** — the round-65 gate refuses the fabricated fixture on strict mode (`corpus/evidence/round67/strict/fabricated-strict.txt`); the R67 counter's mutation-found gaps closed by A1 (`corpus/evidence/round67/pipe/a1-mutants.txt`); census clean at both ends.
- **discernment: unchanged** — no exploratory claim, so no `unprovable-but-better` verdict is available or claimed. The non-author attacks found two overclaims in the lane's own claim text (ClaimFalsifier A3, A4), which are mined (lesson rows 8 and 10) and counted against calibration; no self-attestation.

## SHONEN

Four boxes, `SHONEN.md`. No `[x]`: no non-author verifier has written a box this round (the wave's seats are attack seats, not a box verification by name).

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md:81` (process-environment row, executed 2 of 3; depth gate `PREDICATE R63-C2 pass`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` Round 67 (offline grader run; receipt `corpus/evidence/round67/pipe/receipt.txt`).
- [~] Instructions executable by an agent without oral context — pointer: `corpus/knowledge/tb2-torch-pipeline-parallel-offline.md` (`recheck:` command; `plans/round67_c1_pipeline_probe.py`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `.ufo/waves/round-67/w1/ConnectorOverlap/overlap.md` (5 term-level overlaps, none routed; PROVINCE.md not edited).

## Round shape, seats, and conformance

- Shape: one v1 wave, `kengaku-r67-w1`, 13 seats (build + attack), validated under `scripts/hyaku/ufo-wave-policy.json` (band 8–16), dispatch `.ufo/waves/round-67/w1/w1-dispatch.json`, one batched `taskCall`. Ready handoff `.ufo/waves/round-67/w1.ready` (dispatcher marker `w1.ready.dispatched`).
- Results: `.ufo/waves/round-67/w1/w1-results.json`, 13 of 13 seats settled with output (WAVE-DONE from the orchestrator).
- Seats and roles: TensorRecon (scout); CaseAudit, ProbeReview, SourceReview (reviewer ×3); ProbeMutate, ReceiptMutate (mutation-tester ×2); StrictGateBuild, AfabLab (executor ×2); ConnectorOverlap (connector); SecurityScan (sentinel); KnowledgeDraft, LessonDraft (scribe ×2); ClaimFalsifier (critic).
- Attack roles (reviewer, critic, mutation-tester, labrat-equivalent): 7/13 = 54% (≥25%). Connector seats: 1 (≤2). Residual call: none.
- Dead seats: none. Role note: the policy rejected `labrat` (`.ufo/waves/round-67/w1-validate.stderr` at the first validation; spec corrected to `executor` for AfabLab before the second validation, which passed). The H-AFAB probe therefore rode an executor; its evidence is in its own seat dir.
- Stage note: the first validation failed on that role only; the spec edit (one line) and re-validation are recorded in `.ufo/waves/round-67/w1-validate.out`.
- Planner seat: the validator rejects `planner`; the L1 holds the canonical §3 planner role (claims, freeze, integration).
- Attack note: ProbeMutate and ReceiptMutate were run read-only against committed bytes; no seat used the port except through the probe's own lock; no seat installed anything.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` at the fleet root shows only `.scratch/` orchestrator files and driver markers (`.ufo/waves/round-63/w1.ready.dispatched`, `round-64/w1.ready.dispatched`, `round-66/w1.ready`), none written by this round's seats; nothing copied or deleted.

## Tool installs (tool, version, channel, reason)

- `uv` `0.13.0` (`~/.local/bin/uv`, already installed; used, not installed).
- `uv venv --python /usr/bin/python3 ~/.local/share/kengaku-r67/venv-pipe` → Python `3.14.8`; channel: uv. Reason: a dedicated venv for the grader's imports.
- `uv pip install torch==2.15.0 --index-url https://download.pytorch.org/whl/cpu` → `torch==2.15.0+cpu`; channel: the official PyTorch CPU index. Reason: the grader imports torch; the CPU wheel avoids a CUDA stack.
- `uv pip install pytest==9.2.0 transformers` (default PyPI index) → `pytest==9.2.0`, `transformers==5.22.1`; channel: PyPI via uv. Reason: the grader imports `transformers.LlamaConfig`. The grader's pinned container versions were not read; `transformers 5.22.1` is the version this probe ran against `[INFERENCE for the pinned image]`.
- No pacman; no system package installed or upgraded.

## Open items and L0

- **L0 carried, nothing assumed answered:** `kengaku | round-25/33/51` (coverage cap); `kengaku | round-56`; `kengaku | round-63` (amended K2 detector); `kengaku | round-54` (assimilation id drift).
- **L0 appended this round:** `kengaku | round-67` ×2 in `.ufo/l0-questions.md`: (1) receipt provenance standard (consistency check plus live run versus a result channel the candidate cannot write before any non-lane grader is admitted); (2) the wave policy's `labrat` role rejection.
- **Open, stated as found (not patched after data):** forged-but-consistent receipts pass `--check-receipt` (C1); the candidate can write the junit after the verdict (C1 sandbox; lane-authored cases only); `no_hooks` is a substring test (C1); strict does not bind ENV values (C2); the default R65 predicate still accepts the fabricated fixture (M-1 stays open by design; the strict mode is the successor).
- **Mistake rows 3–4 of round 66 (carried):** dated corrections at `corpus/knowledge/tb2-sqlite-gcov-offline.md:4`, `SKILL.md:686`, `SCORECARD.md:2885`, `LOG.md:2512` remain open; carried to round 68.
- **Erratum (round 67):** the SCORECARD R67-C2 "before" pointer named the pre-landing default run for "mode absent"; corrected by an appended erratum (`f600c6d3`) pointing to `before-strict-absent.txt`.

## Pre-report gate

- Lane pushed: `git -C /home/vgpnk/Projects/shokunin/kengaku-shokunin ls-remote origin refs/heads/master` → `f600c6d3f03a8bc4f10e624897a65b520ec81a6f` (the lane tip cited above).
- SHONEN heading present: `grep -c '^## SHONEN' .ufo/reports/round-67/kengaku.md` → `1`.
- Report committed only via `fleet-commit.sh --as kengaku`.
