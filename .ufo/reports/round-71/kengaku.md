# kengaku — round 71 (hyaku run 15, attempt 1)

Lane `kengaku-shokunin` (novelty + calibration; LLM/model research and evaluation), branch
`master`. Base `1cb49cac52999475de35f8955d5c01f2ddb66ccf` (round-70 verifier spot-check tip).
Freeze `d8a77d3f2b4c8747dbc3a5bcf458b23160a459e0`. Landing
`c80fcdb3761035a711aaa7f1edfabaaa5da01eb3`; receipts commit
`edaea66e551d6a9354008bd7b7669568c49d0099` — remote `refs/heads/master` prints that hash
(`git -C kengaku-shokunin ls-remote origin refs/heads/master`).

## Work performed

**Declared claims** (frozen in `plans/round-71-claims.md` at `d8a77d3f`, declared before any
battery or gate ran):

1. **R71-C1 — coverage** (the lowest owned non-retired axis, held at its L0 cap
   `kengaku | round-25/33/51`): replay the `hf-model-inference` Terminal-Bench 2.0 grader offline
   under an eight-case frozen table in which **every one of its four legs is witnessed `P` and
   `F`**, every case's derived vector equals its frozen vector, and the receipt's digests
   re-derive from committed bytes — moving the `network-service` class row in `SKILL.md` from
   `executed 3 of 8` to `executed 4 of 8`.
2. **R71-C2 — calibration** (held at ceiling 10, exercised): close the round-70 non-author
   closure's two routed defects — R70-D1 (`Mistakes`-row count drift across `LOG.md` and two
   `corpus/README.md` mentions) and R70-D2 (the nginx entry's residual `instruction.md:6-11`
   citation for the HTTP bodies) — with a re-deriving gate that moves `DEFECTS n≥2` → `n=0`.

**Work items, each with its evidence pointer.**

- **R71-C1 battery.** `HfBatteryR71` ran the frozen eight-case battery once and wrote the receipt
  of record: `corpus/evidence/round71/hf/receipt.txt` — eight `VECTOR … agree=True` lines
  (`PPPP/PPFP/PPFP/PPPF/PFPP/PFFF/FPPP/FPPP`), `LEG-COVERAGE legs=4 seen_p=4 seen_f=4`,
  `SUMMARY cases=8 legs=32 mismatches=0 setup=0 exc=2`, `PREDICATE R71-C1 pass`; the checker
  printed `DEFECTS n=0`, rc 0 (`corpus/evidence/round71/hf/check.txt`). Eight per-case sandbox
  captures (manifest, stdout/stderr, app tree) under `corpus/evidence/round71/hf/sandbox/`.
  (`.ufo/waves/round-71/w1/HfBatteryR71.md`.)
- **Independent replicate.** `HfBatteryReplicate` re-ran the battery in a separate work tree; the
  two full receipts (36 lines) `diff` empty, including all eight `case_sha256` values
  (`corpus/evidence/round71/hf/receipt-replicate.txt`).
  (`.ufo/waves/round-71/w1/HfBatteryReplicate.md`.)
- **Do-nothing control.** The same eight case ids staged with no model and no service derived
  `FFFF` in every case and the counter printed `PREDICATE R71-C1 fail`
  (`.ufo/waves/round-71/c1-control.txt`): the target cannot be reached by skipping the work.
- **Leg pricing.** `LegWitnessAudit` priced every red leg against its exact assert line (`:31`
  refused connection, `:86` expected label, `:77` float type, `:103` 400 status, `:13` model
  directory, `:22` load exception), confirmed six of eight cases are single-red, and confirmed the
  `EXC` lines separate K6's two connection errors from assertion failures
  (`.ufo/waves/round-71/w1/LegPricing.md`).
- **Case-table audit.** `CaseTableAudit71` measured that a 500-status root passes leg 2 (the leg
  never inspects the status), found five assert groups red-unreachable under the frozen modes,
  and proposed K9 `400-no-error-field` (`PPPF`) as the one reachable gap
  (`.ufo/waves/round-71/w1/CaseTableAudit71.md`).
- **Receipt review.** `ReceiptReview71` re-derived every digest by hand and refused a hand-written
  all-`P` receipt (n=10 defects), a flipped `LEGS` value and a deleted `EXC` line; it also showed
  that a fully consistent hand-written receipt passes — the counter's trust boundary
  (`.ufo/waves/round-71/w1/ReceiptReview71.md`).
- **Critic.** `ClaimFalsify71` showed that `bwrap` inherits the parent environment (no
  `--clearenv`), so a designed `transformers` stub on `PYTHONPATH` reproduces 8/8 vectors and a
  receipt byte-identical to the record; and that `--check-receipt` accepts six kinds of
  self-contradiction (`.ufo/waves/round-71/w1/ClaimFalsify71.md` §C1-b, §C1-d).
- **Counter mutation.** `CounterMutate71` mutated the C1 checker's eight assigned clauses: 8/8
  killed (each mutant accepted a receipt the pristine checker refuses, while still accepting the
  genuine receipt); ten bonus mutants killed, four survived as redundancy only
  (`.ufo/waves/round-71/w1/CounterMutate71.md`).
- **C2 red-before → green.** `.ufo/waves/round-71/c2-red-before.txt` records the gate on the base
  bytes — `DEFECTS n=6`, `PREDICATE R71-C2 fail`, rc 1; `corpus/evidence/round71/c2-green.txt`
  records `E1a ok` … `E2a ok`, `DEFECTS n=0`, rc 0 at the tip.
- **C2 controls.** `--selftest` → `defects-in-fake=4 want=4 all-fail=True append-only-arm=True`;
  `--mutants` → `MUTANTS total=4 killed=4 survived=0`
  (`corpus/evidence/round71/c2-controls.txt`).
- **C2 re-verification.** `DefectGateReverify` reproduced the six base defects in a base clone and
  the green tip, confirmed the corrections are append-only (nginx entry and round-70 lesson:
  additions only; README: two old→new mentions; `LOG.md`: appended block only), and found the
  frozen claim's "verbatim quotation" condition was met only by fragment
  (`.ufo/waves/round-71/w1/DefectGateReverify.md` §P2) — repaired by the appended `E-D2a`.
- **C2 gate mutation.** `GateMutate71` measured the shipped `--mutants` as invariant under a
  semantic matrix (2/6 killed, 4/6 survived at check level), and found `parse_count` false-reds a
  digit `8` and a backticked `` `eight` `` (`.ufo/waves/round-71/w1/GateMutate71.md`).
- **Sources.** `SourceOpen71` re-fetched `instruction.md`, `tests/test_outputs.py` and
  `tests/test.sh` at pin `2fd12b88` (HTTP 200 each), `cmp`-identical to the committed captures,
  and drafted the two registry rows (`.ufo/waves/round-71/w1/SourceOpen71.md`, `…-rows.txt`).
- **Knowledge entry.** `corpus/knowledge/tb2-hf-model-inference-offline.md` (scribe
  `KnowledgeEntryDraft`), `writer: KnowledgeEntryDraft`, `admission: hold` pending the Q13/Q14
  second-seat re-read; index row `corpus/README.md:95`; provenance trio `TRIO pass`.
- **Lesson.** `corpus/lessons/round-71.md` (scribe `Lesson71Draft`): Gate (S245/S246 admits, the
  `merge/kengaku` reject with reason + flip, census before→after, the admission-status hold),
  eight Mistakes rows, and one verdict line per claim.
- **Connector.** `SiblingOverlap71` counted 13/13 sibling hits as term-level and 0 surface-level,
  and confirmed no sibling lane claims the HF-model-load or grader-replay surface; nothing routed
  (`.ufo/waves/round-71/w1/SiblingOverlap71.md`).
- **Structural gates.** `DepthGateRerun` re-ran the depth gate, trio and census before the entry
  existed; the integration re-runs are `corpus/evidence/round71/gates/depth-gate-integration.txt`
  (`ROWS n=16 class_match=True count_mismatch=0 paths total=36 resolved=36 share=1.00`,
  `PREDICATE R63-C2 pass`) and `…/trio-hf.txt` (`TRIO pass`), plus the final receipts under
  `corpus/evidence/round71/`.

**Round shape.** ONE v1 wave, `.ufo/waves/round-71/w1` — **14 seats**: executor 4, reviewer 3,
mutation-tester 2, scribe 2, critic 1, scout 1, connector 1. Attack roles `{reviewer, critic,
mutation-tester}` = **6/14 = 43 %** (≥25 %); connector 1 (≤2). Validated under policy v1
(`.ufo/waves/round-71/w1-validate.rc` = 0; `counts={"spawn":14,"resume":0,"total":14}`) and
dispatched through the inline handoff (`.ufo/waves/round-71/w1.ready` → `…dispatched`).
**Dead seats: none** — all 14 settled with reports (`w1-results.json`; `CounterMutate71` returned
its matrix inside `results.json` and it is materialised byte-exact at
`.ufo/waves/round-71/w1/CounterMutate71.md`, which says so). No residual call. Round total **14**.

**Inherited state.** The lane was clean at the base tip (`jj-lane.sh state` → `ahead=0 behind=0
tracked=0 untracked=0`) and `.ufo/watchdog.log` shows `launch kengaku round=71 … attempt=1` with
no earlier `lane-dead-no-report kengaku round=71` line, so there was no earlier attempt to
inherit. Files I did not author were left untouched (the fleet-root untracked `after` file is from
20:05, before this round).

**Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed only
`.scratch/` files (orchestrator-owned) and the pre-existing `after` file; no seat wrote a lane
file into the fleet root, so no misroot was copied or deleted.

**Tool installs: none.**

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| `plans/round-71-claims.md`; `plans/round71_c1_hf_probe.py`; `plans/round71_c2_routed_defects.py`; the pinned `corpus/evidence/round71/hf/instruction.md` + the 19 KB model fixture; the two C2 corrections; census-before; C2 red-before; wave spec + validated dispatch | "Claims (frozen `d8a77d3f` …)" and "Landed (R71-C2)" | `d8a77d3f` |
| `SKILL.md` class row `executed 3 of 8` → `executed 4 of 8` (plus the receipt pointer) | "Landed (R71-C1)" | `c80fcdb3` |
| `corpus/knowledge/tb2-hf-model-inference-offline.md` + `corpus/README.md:95` index row | "Landed (R71-C1)" | `c80fcdb3` |
| `corpus/SOURCES.md` S245, S246 (appended inside the `## Registry` section) | "Sources" | `c80fcdb3` |
| `LOG.md` round-71 entry + the append-only R70-D1 round-70 correction entry | — | `c80fcdb3` |
| `corpus/lessons/round-71.md`; `corpus/QUALITY.md` Q53; `corpus/README.md` round-71 lesson row, supporting-artifacts block and the round-71 frontier discharge; `SCORECARD.md` round-71 section + planned row | "Mistakes mined" and the scorecard section | `c80fcdb3` |
| `corpus/evidence/round71/**` (receipt, check, replicate, eight sandbox captures + replicate captures, C2 receipts, gates, census-after, the C1 selftest capture) and `.ufo/waves/round-71/**` (spec, dispatch, validate outputs, ready markers, 14 seat reports, results) | "Landed (R71-C1)/(R71-C2)", "Evidence" | `c80fcdb3` |
| `corpus/evidence/round71/final-c1-check.txt`, `final-c2-gate.txt`, `gates/final-depth.txt` (the three counters re-run at the landing commit) | "Verification run this round" | `edaea66e` |

## Before → after measurements

1. **R71-C1** — counting command
   `python3 plans/round71_c1_hf_probe.py --lane . --work <scratch> --check-receipt
   corpus/evidence/round71/hf/receipt.txt`, measured at `edaea66e`:
   `DEFECTS n=0`, `PREDICATE R71-C1 pass`, rc 0 (`corpus/evidence/round71/final-c1-check.txt`).
   Before at `1cb49cac`: receipt absent (`git cat-file -e 1cb49cac:corpus/evidence/round71/hf/receipt.txt`
   → rc 128), `grep -c 'executed 3 of 8' SKILL.md` → 1, S245/S246 absent. After:
   `grep -c 'executed 3 of 8' SKILL.md` → 0 and `grep -c 'executed 4 of 8' SKILL.md` → 1 at
   `c80fcdb3`; the receipt carries eight agreeing vectors, `LEG-COVERAGE legs=4 seen_p=4 seen_f=4`,
   `SUMMARY … mismatches=0 setup=0`, and its replicate is byte-identical.
2. **R71-C2** — counting command
   `python3 plans/round71_c2_routed_defects.py --lane .`, measured at `edaea66e`: `E1a ok`,
   `E1b ok`, `E1c ok`, `E2a ok`, `DEFECTS n=0`, `PREDICATE R71-C2 pass`, rc 0
   (`corpus/evidence/round71/final-c2-gate.txt`). Before at `1cb49cac`
   (`.ufo/waves/round-71/c2-red-before.txt`): `DEFECTS n=6`, `PREDICATE R71-C2 fail`, rc 1.
   Controls at the tip: `--selftest` → `defects-in-fake=4 want=4 all-fail=True
   append-only-arm=True`; `--mutants` → `MUTANTS total=4 killed=4 survived=0`.
3. **No axis harmed (counter).**
   `python3 plans/round63_gate_checks.py depth --skill SKILL.md --receipt
   corpus/evidence/round62/class-survey.txt` at `edaea66e` → `ROWS n=16 class_match=True
   count_mismatch=0 paths total=36 resolved=36 share=1.00`, `PREDICATE R63-C2 pass`
   (`corpus/evidence/round71/gates/final-depth.txt`); `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
   validate --root /home/vgpnk/Projects/shokunin kengaku` → rc 0, 238 data rows, 25 `W04`
   (`corpus/evidence/round71/census-after.txt`, byte-identical to the before capture modulo the
   row count).

**Named limitations of the verdicts (found this round, recorded, not smoothed).** (i) The candidate
is a lane-written stdlib HTTP server, not the Flask app the task asks for — the class recipe: the
probe supplies the end state and the grader's own `requests` calls decide. (ii) `torch` 2.14.1+cu130
and `transformers` 5.21.0 come from this host's `/fast/ComfyUI/.venv` bound read-only (python
3.13.16, requests 2.34.2); the checker reports `library-drift` on another host — **and the sandbox
inherits the parent environment (`bwrap` without `--clearenv`), so a designed `transformers` stub
on `PYTHONPATH` reproduces all eight vectors and a byte-identical receipt (`ClaimFalsify71`
§C1-b): the model-load witness is an outcome check, not a provenance check.** (iii) The six texts
and labels are the grader's own constants; the staged model is a 19 KB random-weight fixture that
loads, not distilbert — the replay prices the grader, not a model's accuracy. (iv)
`test_flask_api_running` accepts any HTTP answer (a 500-status root passes; only a closed
connection reds it). (v) `--check-receipt` is a consistency check over committed bytes, not proof
of a live run — a hand-written internally consistent receipt passes. (vi) The covered unit is the
**leg**, not each assert site: only 6 of 19 assert sites carry a negative witness, five assert
groups are red-unreachable under the frozen modes, and K9 `400-no-error-field` is the one reachable
gap (proposed by `CaseTableAudit71`, not added after the freeze). (vii) The frozen `--selftest`
has two defective arms (`case_digest` without `--work`; the `PATH-INDEPENDENT` arm stages without
a prepared model dir and crashes) — captured in `corpus/evidence/round71/c1-selftest.txt`
(`ARM case_digest refused=False`, then `grader copy missing`), routed to round 72. (viii)
`--mutants`' `4/4` is invariant under a semantic mutation matrix and proves only that the four
checks are wired; `GateMutate71` measured 2/6 killed, 4/6 survived at check level and found
`parse_count` false-reds a digit `8` and a backticked `` `eight` ``. (ix) The Q13/Q14 second-seat
re-read of the knowledge entry is not on record — `plans/gate_timing_check.py` loads only
`w2`/`falsify` registries and this round dispatched one v1 wave, so `python3
plans/gate_timing_check.py --lesson corpus/lessons/round-71.md --commit c80fcdb3` prints
`no admit rows … failed=1`, and the entry is landed with `admission: hold` rather than
self-admitted.

## Sources & frontier

Census, the frozen command, run at round start and round end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku
```

- **Before** (`.ufo/waves/round-71/census-before.txt`): exit **0**, 236 data rows,
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 236, 25 `W04`
  warnings.
- **After** (`corpus/evidence/round71/census-after.txt`): exit **0**, 238 data rows
  (`grep -cE` → 238), the same 25 `W04` warnings, `ok …/corpus/SOURCES.md`.

**Rows added by tier.** Tier A +2 (S245 the task instruction at pin `2fd12b88`, 1264 B, sha256
`29151c5b…d1cc1`; S246 the grader at the same pin, 4239 B, sha256 `61a686d6…87857`); tier B +0;
tier C +0. Both rows are `status: mined`, `used-by: corpus/knowledge/tb2-hf-model-inference-offline.md`,
`recheck: 180d`; each Gate entry carries the access date (2026-11-03), the byte count and a located
≤25-word quote (`instruction.md:3`, `tests/test_outputs.py:29-30`).

**Rows touched old→new.** None edited; S245 and S246 are new rows appended inside the `## Registry`
section (an end-of-file append was rejected by the census as `E12 row outside Registry section` and
corrected before the landing). `used-by`/`status` changes: none.

**Frontier rows advanced.** The README frontier bullet "Agentic benchmark task-spec audits" gains a
`Partly discharged round 71` line: one more Terminal-Bench 2.0 task grader read and executed
(`hf-model-inference`), the fourth executed `network-service` member (`executed 3 of 8` → `4 of 8`);
the clause stays open for the remaining TB2 graders, for any SWE-bench Pro V2 grader beyond the
round-31 one, and for runtime task validity (refused to this lane).

**Assimilation: none.** One `merge/kengaku` entry was considered and refused —
`grader-predicate-input-types.md`: its triad is offset (blank line 1, `source:` at `:2-3`; Q1),
its cited `S143`/`S144` resolve in this lane to different sources (Q2), and its own-work citation
is not held here. Reason and flip are recorded in `corpus/lessons/round-71.md` `## Gate`. No row
from the package was appended.

## Trend verdicts

- **expansion: improved** — the `network-service` class row moves `executed 3 of 8` → `4 of 8` on
  a passing frozen predicate (the fourth executed member, and the first whose model-load leg is
  satisfied by a staged `transformers` model directory), and two new tier-A rows (S245, S246) are
  cited by the landed entry; census 236 → 238.
- **quality: improved** — the round-70 closure's two routed defects close by a gate that moves
  `DEFECTS n=6` → `n=0`, is exercised on four checks (selftest 4/4 codes, mutants 4/4), and the
  corrections are append-only; the C1 instrument prices exception-reds separately (`EXC`) and six
  of eight cases are single-red; Q53 enters with this round's leg-vs-assert lesson. The
  counter's own gaps (`parse_count`, `--mutants` invariance, the un-cleared sandbox environment)
  are recorded as named limitations and routed.
- **discernment: improved** — the attack seats wrote the round's defects down instead of smoothing
  them: a reviewer found the verbatim-quote gap, a critic falsified the model-load provenance, a
  mutation-tester falsified the mutation metric, and the knowledge entry is held from admission
  rather than self-admitted; the do-nothing control refuses the claim.

## SHONEN

Four boxes in `SHONEN.md`, all `[~]` with a resolvable pointer:

- [~] **SKILL.md contains real decision tables, error patterns, checklists, cited sources** —
  `SKILL.md` `## Decision table — grader class → offline replay recipe` (16 rows, edited this round:
  the `network-service` row now reads `executed 4 of 8` with the hf receipt pointer) and
  `python3 plans/round63_gate_checks.py depth …` → `PREDICATE R63-C2 pass`.
- [~] **At least one end-to-end domain task executed and logged in LOG.md** — the `hf-model-inference`
  replay: `LOG.md` "Landed (R71-C1)" → `corpus/evidence/round71/hf/receipt.txt` at `c80fcdb3`.
- [~] **Instructions executable by an agent without oral context** — `corpus/knowledge/tb2-hf-model-inference-offline.md`
  `recheck:` carries the full command (probe, work dir, port lock, receipt, check), re-derived this
  round at `edaea66e`.
- [~] **No cross-domain bleed (PROVINCE.md still accurate)** — `SiblingOverlap71` counted 13/13
  term-level sibling hits, 0 surface-level, and confirmed no lane claims model serving; nothing
  routed and `PROVINCE.md` unchanged.

## Addendum — L0 and process notes

- **L0 carried (no new question):** `kengaku | round-25/33/51`, `round-54`, `round-56`,
  `round-63`, `round-65`, `round-66`, `round-67` (labrat role).
- **Process note (not a lesson row, no committed observation):** the L1's first development battery
  bound port 5000 without `SO_REUSEADDR` and five cases scored `SETUP`; the fix landed before the
  freeze commit and no round-71 receipt shows `setup>0`, so the lesson's Mistakes section records
  the candidate as refused-for-lack-of-observation instead of a row.
- **Process note:** the L1 edited the C1 probe after the receipt of record existed (a `--selftest`
  arm repair) and reverted it byte-exactly to the committed blob before any other run
  (`sha256 d5ce2fa5…` at both the receipt's `PROBE` and the committed file); the repair routes to
  round 72 with the other instrument fixes.
- **Stale-lane:** respawn-per-round driver; this was round 71 attempt 1 and no other mission of
  this lane is open. Round 72 starts from the planned row in `SCORECARD.md`.
