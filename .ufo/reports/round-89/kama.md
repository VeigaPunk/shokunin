# kama — round 89 report

L1 `KamaR89`, attempt 1. Lane `kama-shokunin`, branch `master`. Base `56174a1fa6a27faa91d3664ef4730b48dd3149c0`,
freeze `4eb75c62f6deb1a586a291d611b71775049b34a6`, C1 measured `4f9eacf720aa59ed806b31b758571e364658179b` and
re-measured after the wave-1 repair at `5b1e0fb360c41f688a6fbc3a467769d6f2dfc1db`, C2 measured
`21b9e36d6192e0a691550b32e0e6c38412227f4c` and re-measured at `0f539b4591131c7194dfc87c12b5644f2b1944f0`, final lane tip
`68bb020864a5488c0d25bdf99bf3eba73a8b20d5` (`git ls-remote origin refs/heads/master` prints this hash).

## Work performed

Declared claims (frozen in `plans/round-89-claims.md` at `4eb75c62`; two claims on distinct axes; no exploratory claim):

- **C1 — operability (sourced S583/S584/S585):** a llama.cpp router entry that is `unloaded` on an autoload router
  but whose model file cannot load was graded `MODEL_OK router-unloaded-autoload`. A real request answers
  `500 model name=<id> failed to load`. Counter `tools/round89-unloadable-cells.py` runs 11 live cells on lane-owned
  b12177 router children. Each cell's expected verdict is the router's answer to a real completion; there are no
  canned expectations (this answers r88 R1/R7).
- **C2 — depth (tied-lowest axis, 7):** a new `SKILL.md` section, `## Router error signatures (llama.cpp router mode)`,
  with eight rows. Counter `tools/round89-signature-rows.py` binds each row's endpoint, HTTP code and exact
  `error.message` to an answer captured from b12177 (`.ufo/waves/round-89/measured/router-signatures.jsonl`).

Work items:

- Fresh-start reads before declaring: the r86, r87 and r88 verifier spot-checks (`corpus/lessons/round-89.md:6-8`).
  The last six closures (r83–r88) were all rejected.
- Domain discovery: in pre-freeze recon on both b11755 and the current release b12177, every unloadable file (missing,
  non-GGUF, bad header, truncated, deleted) is listed `unloaded` and graded `MODEL_OK` by the probe, while the request
  returns 500 (`.ufo/waves/round-89/controls/c1-base.out`, `mismatches=5`).
- Tool install: llama.cpp **b12177**, official release asset `llama-b12177-bin-ubuntu-x64.tar.gz`, sha256
  `5d936162de06187654d1353fe94d65390904f1c67cd1a887023dbc9b0b207284` (GitHub digest verified), installed into
  `~/.local/opt/llama-b12177/` to re-verify router behaviour on the current release (`LOG.md` §Round 89).
- Controls were executed and committed before freeze (`4eb75c62`):
  - C1 do-nothing: `mismatches=5 positive_mismatches=0`.
  - C1 forgeries, using real historical probes: F1 r88-measured `138a7543` gives 3/3; F2 pre-router `9b4c7af1` gives 7/2.
  - C2 do-nothing: `rows=0`.
  - C2 forgery battery: `bound=1 unbound=5 duplicates=1`.
  - Harm baselines: `controls/harm-base-*.out`.
- C1 implementation `4f9eacf7`. `tools/kama-probe.sh` reads the absolute model, mmproj and draft paths in `status.args`
  and applies the b12177 loader's GGUF header checks (S584), with the type-size table generated from S585.
- C2 SKILL table and corpus work `21b9e36d`:
  - knowledge entry `corpus/knowledge/router-unloadable-model.md`;
  - S583–S585 admitted, S586 (GGUF spec) rejected;
  - QUALITY KQ144;
  - README round-89 coverage and frontier;
  - lesson M1/M2.
- Wave 1 (13 seats) found two real problems at `4f9eacf7`:
  - EX02 measured an extra 1.3–1.4 s per live check;
  - SN01 found a 41 s stall from a 219-byte answer, listener-chosen `/proc` opens, and a stat/open race.

  Repair `5b1e0fb3`:
  - only the matching autoload candidates are checked;
  - a 4 s deadline and a 4 M-read budget; when either runs out the result is "undecidable" (no verdict change);
  - files are opened `O_NONBLOCK` and checked with `fstat`;
  - nothing under `/proc`, `/sys` or `/dev` is opened;
  - vocabularies are skipped in chunks.

  Re-measured at `5b1e0fb3`:
  - C1 still green (`measured/c1-final.out`);
  - harm suites unchanged (`measured/harm-final.out`);
  - EX01 held-out cells give identical classes (`measured/heldout-Mprime.out`);
  - the SN01 bombs end in ≤1.6 s as undecidable (`measured/sn01-bombs-Mprime.out`).
- Other wave fixes at `0d751aab`:
  - CR02: SKILL row 2 named the wrong reason after a failure; corrected to `router-unloaded-failed`, plus a new decision row.
  - R5 (r88 closure): `tests/probe-verdicts/check.py` now grades `MODEL_UNLOADED` rows and can stage files.
    `RouterUnloaded.json` adds 5 rows: 77/77 at `5b1e0fb3`, and the 3 `router-model-*` rows fail on base.
    Fault-control pins are updated (`measured/harness-r5.out`).
  - R6: the answering model per seat is recorded (`.ufo/waves/round-89/w1-seat-models.txt`).
  - R2: SCORECARD capability row `router-mode-readiness` is re-pointed to a green of the landed rule.
  - R3: every round-89 receipt names a full hash.
- R4 (`round75-instruments` red): cause found by EX04. The audit's exempt-head eligibility is monotone in `<to>`.
  The only byte-preserving fix deletes 19 rows from an append-only register, so it was not applied; an L0 question is filed.

## Landed changes

All commits are by `kama-shokunin <kama@shokunin.local>` via `jj-lane.sh`, tied to `LOG.md` §"Round 89":

| Commit | Content | LOG.md |
|---|---|---|
| `4eb75c62f6deb1a586a291d611b71775049b34a6` | freeze: plan, three round-89 tools, pre-freeze controls, signature receipt | Round 89 intro |
| `4f9eacf720aa59ed806b31b758571e364658179b` | C1 probe change | C1 bullet |
| `21b9e36d6192e0a691550b32e0e6c38412227f4c` | C2 SKILL table; knowledge; S583–S586; KQ144; README; lesson; C1 receipts | C2 / knowledge bullets |
| `c8db858691e883955f10cf9d7e1dec8f8d732bc8` | C2 receipt; wave spec and dispatch | C2 bullet |
| `5b1e0fb360c41f688a6fbc3a467769d6f2dfc1db` | wave-1 probe repair (latency, CPU stall, `/proc`, race) | Wave 1 bullet |
| `0d751aab836ac4a30c0a815cece1ad01249031aa`, `0f539b4591131c7194dfc87c12b5644f2b1944f0` | integration: R5 harness, SKILL corrections, SCORECARD §Round 89 and anchors, PROVINCE, lesson M3/M4, final receipts, wave evidence | Wave 1 bullet |
| `83297283601b11a20d9c2a422805e8e155ea10a5`, `68bb020864a5488c0d25bdf99bf3eba73a8b20d5` | C2 final receipt, census end, terminal gate receipt | — (receipts only) |

No `lane-dead-no-report kama round=89` line exists; nothing was inherited; no operator commits arrived during the round.

## Before → after measurements

**C1 (operability)** — `python3 tools/round89-unloadable-cells.py --repo . --rev <R> --work <scratch>`. The counter
sha256 is `1d86194c…` at freeze, M and M′.

| Revision | Output | Receipt |
|---|---|---|
| base `56174a1f` | `cells=11 mismatches=5 positive_mismatches=0`, exit 1 | `controls/c1-base.out` |
| F1 `138a7543` / F2 `9b4c7af1` | `3/3` and `7/2`, exit 1 | `controls/c1-f1.out`, `c1-f2.out` |
| M `4f9eacf7` | `cells=11 mismatches=0 positive_mismatches=0`, exit 0 | `measured/c1.out` |
| M′ `5b1e0fb3` (final probe) | `cells=11 mismatches=0 positive_mismatches=0`, exit 0 | `measured/c1-final.out` |

Harm conjunct, base vs M vs M′ (frozen K2): no regression in any frozen harm suite.

- `check.py` 72/72 and `test-snapshot.sh` 30/0 at base, M and M′.
- r88 oracle cells: 0 mismatches at base, M and M′.
- r88 frozen router-cells: `mismatches=2` (C05, C12 only) at base, M and M′.
- Operator router 1234 (GET only): `MODEL_OK router-unloaded-autoload` on all ids at every revision.

Receipts: `controls/harm-base-*.out`, `measured/harm-M.out`, `measured/harm-final.out`.

Not covered by K2: the probe is slower. Median latency for a single-id check went from 0.136 s at base to 0.251 s at M′;
at M it was about 1.3 s slower than base (EX02).

Author verdict: frozen predicate met at M and at M′, with no frozen harm. The wave-found cost and robustness defects
at M (lesson M4) are disclosed. They are outside the frozen kill rules and were repaired without any verdict change.
**Operator/closure rules.**

**C2 (depth)** — `python3 tools/round89-signature-rows.py --repo . --rev <R>`. The counter sha256 is `30f3af7f…`
at freeze and at every measured revision.

| Revision | Output | Receipt |
|---|---|---|
| base `56174a1f` | `rows=0 bound=0 unbound=0 duplicates=0`, exit 1 | `controls/c2-base.out` |
| forgery fixture | `rows=7 bound=1 unbound=5 duplicates=1`, exit 1 | `controls/c2-forgeries.out` |
| M2 `21b9e36d` | `rows=8 bound=8 unbound=0 duplicates=0`, exit 0 | `measured/c2.out` |
| `0f539b45` (after CR02 text fix) | `rows=8 bound=8 unbound=0 duplicates=0`, exit 0 | `measured/c2-final.out` |

Author verdict: met; the depth score is held at 7. Disclosed limits (CR02):

- The counter binds only 3 of the 6 columns.
- A receipt is a writable file, but CR02's independent recapture was byte-identical.

Terminal gate at `83297283`: `PRE_REPORT round=89 arms=14 failed=1 uncommitted=0`. The only red arm is
`round75-instruments` (R4, L0). Receipt: `measured/gate-final.out`.

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`.

- Start: exit 0, `kama ok` (`controls/census-start.out`).
- End: exit 0, `kama ok`; the only non-W04 warning is the pre-existing W01 on S481 (`measured/census-end.out`).

- Rows went from 322 to 326 (all four new rows are tier A, so A 307 → 311; B 11 and C 4 unchanged). By status: mined
  288 → 291, queued 8, rejected 26 → 27.
- Added:
  - **S583** (A, code, mined): llama.cpp `server-models.cpp` @ b12177 `6c01da62`.
  - **S584** (A, code, mined): `ggml/src/gguf.cpp` @ b12177.
  - **S585** (A, code, mined): `gguf-py/gguf/constants.py` @ b12177.
  - **S586** (A, spec, rejected): GGUF spec `docs/gguf.md` @ ggml `57e2c2c`. It describes the format, not what the
    loader enforces (the loader also loads v2 and requires exact tensor contiguity). Flip: the loader enforces exactly the spec.
- Rows touched old→new: none. S582's flip condition now holds, but no admitted entry cites it, so the row stays
  rejected (recorded in the lesson Gate).
- Sourced claim: C1 rests on S583–S585 (`corpus/knowledge/router-unloadable-model.md` `source:` line).
- Frontier:
  - moved to core: router entries whose model file cannot load, and the router error answers (`corpus/README.md`
    §"Coverage and frontier — round 89");
  - new frontier: router aliases (SC01 found a false `MODEL_MISMATCH` for an alias pin, present at base),
    `--models-memory-margin`, split shards, corrupt tensor bytes.
- Mistakes mined (`corpus/lessons/round-89.md` `## Mistakes`):
  - M1: a readiness branch generalized from one healthy asset (fix KQ144).
  - M2: a `git worktree add` in the lane (removed).
  - M3: the r88 "reasons ungraded" counter defect repeated (fixed by the R5 harness grading reasons).
  - M4: the measured commit was correct but 10× slower and stallable (repaired at `5b1e0fb3`).
- Assimilation: none (no `merge/kama/` theme taken). considerthese: none mined this round.

## Trend verdicts

- **expansion: improved.** One knowledge entry on ground the coverage map did not hold. It cites mined S583–S585 and
  names its prior art (KQ143 sweep; RV02 corrections appended).
- **quality: improved.** Router readiness was re-verified on the current release b12177, alongside the pinned b11755.
  A known false green (unloadable files) is now graded by the runtime's own answer. The wave caught the new entry's
  SKILL row-2 error and the probe's latency and stall defects, and both were corrected in-round; RV02 found no admitted
  entry false.
- **discernment: improved.** Admits S583–S585 and rejects S586, with located quotes. Wave disagreements became lessons:
  CR02 → SKILL fix, MT01 → M3, EX02/SN01 → M4, M1 → KQ144. Non-author agreement on the admit/reject sample awaits the
  closure spot-check.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources → author assertion: `SKILL.md` §"Router error signatures (llama.cpp router mode)" (8 wire-bound rows, `measured/c2-final.out`) and §"Round-89 unloadable router models" (S583–S585); no named non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md → author assertion: `LOG.md` §Round 89; live b12177 router children with real completions (`measured/c1-final.out`, `measured/router-signatures.jsonl`); no non-author mark.
- [~] Instructions executable by an agent without oral context → author assertion: wave seats re-ran the SKILL gates unaided (`w1/CR01ClaimC1.md`, `w1/CR02ClaimC2.md` byte-identical recapture); seats are the lane, not non-authors.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → author assertion: `PROVINCE.md` round-89 paragraph; `w1/CN01SiblingOverlap.md` found no contested scope (it reports kengaku `PROVINCE.md:26-27` as stale, not edited).

## Round shape and seats

- One v1 wave `w1`, 13 seats, validated under `scripts/hyaku/ufo-wave-policy.json` (band 8–16), dispatched by the
  orchestrator's inline handoff (`w1.ready` → `w1.ready.dispatched`; `WAVE-DONE kama r89 w1: all 13 seats settled`).
- Roles: executor 4, reviewer 2, critic 2, mutation-tester 1, sentinel 1, scout 1, connector 1, scribe 1. Attack seats:
  5/13 = 38 %.
- Dead seats: 0. Residual call: none. Round total: 13. The §3 planner seat was held by the L1.
- Answering models (`w1-seat-models.txt`): reviewers on `zai/glm-5.3-flashx`, scout on `minimax-code/MiniMax-M3.1-Flash`,
  all other seats on `amr/deepseek-v4.1-flash`.

## Limits, L0, misroots

- **CR01:** a probe keyed on the fixture names passes the 11 cells, so the counter is necessary but not sufficient. The
  13 held-out cells (EX01) and the R5 harness rows are the extra discriminators.
- **Remaining held-out cells:** 3 LIMIT (chmod-000 file, split model with a missing shard, relative missing path) and
  1 INDETERMINATE (FIFO, caused by a b12177 load hang). There is no HARM cell.
- **Routed to round 90:** SN01 F3 (no response-size cap) and F4 (unsanitised ids), both pre-existing.
- **L0 question appended this round:** `kama | round-89 | …` on deleting 19 stale rows from
  `registry/append-only-late.tsv` (R4). The L0 commit hash is not cited here because this report and the L0 line land
  in one fleet commit.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only ` M .scratch/run15-state.json`,
  `?? .scratch/run15-wrapup/…` (orchestrator-owned) and this round's `.ufo/l0-questions.md` line. No seat misroots.
- **Cleanup:** scratch `/fast/scratch/hyaku/kama-r89` removed; no lane-started llama-server children remain;
  `git worktree list` shows one entry (M2 repaired).
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
