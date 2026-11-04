# kengaku — round 72 (hyaku run 15, attempt 1)

Lane `kengaku-shokunin` (novelty + calibration; LLM/model research and evaluation), branch
`master`. Base `c63229724893c40b11661194ef1dff2987c177e9` (round-71 verifier spot-check tip).
Freeze `b6336136e0e891522b113a94d8e0bd65e0eae8de`. Landing `08df910a461620741d433def3df38a8406efe9f`;
the final counter receipts were re-run at that tip and committed in
`db78d059587c8ecc543afc4c7a4638a88132269d`, which is what remote `refs/heads/master` prints
(`git -C kengaku-shokunin ls-remote origin refs/heads/master`).

## Work performed

**Declared claims** (frozen in `plans/round-72-claims.md` at `b6336136`, declared before any battery
or gate ran):

1. **R72-C1 — coverage** (the lowest owned non-retired axis, held at its L0 cap
   `kengaku | round-25/33/51`): the `hf-model-inference` Terminal-Bench 2.0 grader is replayed
   offline under a **nine-case** table — every one of its four legs witnessed `P` and `F`, K9
   `400-no-error-field` (`PPPF`) pricing the `assert "error" in error_data` site at
   `tests/test_outputs.py:107` that the round-71 eight-case table could not reach — with a
   **provenance witness** (`bwrap --clearenv` plus an explicit nine-variable allowlist, the
   sandbox's own `transformers.__file__`, a plantable canary) and a stub-injection control.
2. **R72-C2 — calibration** (held at ceiling 10, exercised): the round-71 non-author closure's
   routed defects **R71-R1** (neither round-71 instrument had a `SKILL.md` registry row) and
   **R71-R7** (two freeze-commit labels claim content the freeze commit does not hold) closed by a
   re-deriving gate that moves `DEFECTS n=6` → `n=0`, with the R71-R5 count-parser class repaired
   and the invariant `--mutants` metric replaced by a green/red fixture matrix with an attribution
   arm and a deliberate null.

**Round shape.** ONE v1 wave, `.ufo/waves/round-72/w1` — **16 seats**: executor 6, scribe 3,
reviewer 2, mutation-tester 2, critic 1, scout 1, connector 1. Attack roles `{reviewer, critic,
mutation-tester}` = **5/16 = 31 %** (≥25 %); connector 1 (≤2). Validated under policy v1
(`.ufo/waves/round-72/w1-validate.rc` = 0; `counts={"spawn":16,"resume":0,"total":16}`) and
dispatched through the inline handoff (`w1.ready` → `w1.ready.dispatched`). No residual call;
round total **16**. **Dead seats: none** — all 16 settled and all 16 wrote a report in the wave dir
(`w1-results.json`: `seats=16`, 16 results). **Planner seat:** the validator rejects the `planner` role, so the L1 holds the
canonical §3 planner seat (R71-R3's routed item); the planning data-walk rode `SurfaceScoutR72`
(class-row census, assert-site inventory, host re-verification) and `C2RedBeforeR72` (base/tip
revisions).

**Work items, each with its evidence pointer.**

- **C1 battery.** `HfBatteryR72` ran the frozen nine-case table and wrote the receipt of record
  `corpus/evidence/round72/hf/receipt.txt` (3494 B, sha256 `fa060b7f…4087`): nine
  `VECTOR … agree=True`, `LEG-COVERAGE legs=4 seen_p=4 seen_f=4`,
  `SUMMARY cases=9 legs=36 mismatches=0 setup=0 exc=2`, `PREDICATE R72-C1 pass`; the checker printed
  `DEFECTS n=0` / `PREDICATE R72-C1 pass`, rc 0 (`corpus/evidence/round72/hf/check.txt`); nine
  per-case sandbox captures under `corpus/evidence/round72/hf/sandbox/K1..K9/`, every manifest's
  `prov.canary` = `ABSENT`, `prov.cwd=/app`, `prov.executable=/venv/bin/python3`
  (`.ufo/waves/round-72/w1/HfBatteryR72.md`).
- **K9's assert site.** `corpus/evidence/round72/hf/sandbox/K9/manifest.json` carries
  `"AssertionError: Error response should contain 'error' field"` — leg 4 passes `:103` and reds
  `:107`; K4 reds `:103` instead, so the pair witnesses both assert sites of leg 4
  (`HfBatteryR72.md` §K9).
- **Independent replicate.** `HfReplicateR72` re-ran the battery in its own work tree;
  `receipt-replicate.txt` is byte-identical to the receipt of record (`cmp` rc 0, same sha256
  `fa060b7f…4087`) and all nine `case_sha256` values re-derive
  (`.ufo/waves/round-72/w1/HfReplicateR72.md`).
- **Stub before → after.** `StubBeforeAfterR72` staged a raising `transformers` package in `/app`
  and exported `PYTHONPATH=/app/stub`: against the **round-71** probe the injection is imported and
  six of eight vectors flip (`corpus/evidence/round72/hf/stub-before-v1.txt`, `PREDICATE R71-C1
  fail`); against the **round-72** probe the same injection is invisible and all nine vectors hold
  (`stub-after-v2.txt`, `PROVENANCE … transformers_file=/venv/…`, `PREDICATE R72-C1 pass`). The
  shipped control prints `STUB-CONTROL exposed=False vectors_unchanged=True`
  (`stub-control.txt`) (`.ufo/waves/round-72/w1/StubBeforeAfterR72.md`).
- **Do-nothing control.** The nine case ids staged with no model and no service derive `FFFF` in
  every case and the counter refuses: `CONTROL cases=9 derived_set=FFFF predicate=fail
  counter_refuses_do_nothing=True` (`.ufo/waves/round-72/c1-control.txt`). `ReceiptReviewR72`
  cross-checked the control's `case_sha256` against `sha256("\n")` (`01ba4719…546b`, the empty-tree
  digest) — the staging is genuinely empty.
- **C2 red-before → green.** `C2RedBeforeR72` ran the freeze instrument at both revisions: base
  `c6322972` → `DEFECTS n=6` (four `row-absent`, `E1b no-errata-section`, `E2 no-errata-section`),
  `PREDICATE R72-C2 fail`, rc 1 (`corpus/evidence/round72/c2-red-before.txt`, a red-*data* run with
  the freeze instrument, labelled as such); tip `b6336136` → `E1a ok … E2 ok`, `DEFECTS n=0`,
  `PREDICATE R72-C2 pass`, rc 0 (`corpus/evidence/round72/c2-green.txt`). The same seat measured
  `git diff --numstat c6322972 master -- SKILL.md plans/round-71-claims.md` → `5 0` / `20 0`
  (25 insertions, 0 deletions) and the positional relation (labels at offsets 3753/7641,
  `## Errata — round 72` at 8907, last `##` section at line 137)
  (`.ufo/waves/round-72/w1/C2RedBeforeR72.md`).
- **C2 controls.** `C2ControlsR72` captured `--selftest` (`SELFTEST defects-in-fake=3 want=3
  all-fail=True append-only-arm=True positional-arm=True parser-arm=True ok=True`) and `--mutants`
  (`MUTANTS total=7 killed=6 survived=0 invalid=0 null_detected=1`, `ARM accept-green=ok
  refuse-red=ok attribution=ok`) into `corpus/evidence/round72/c2-controls.txt`, plus the C1
  `--selftest` (`red_refused=8/8 accept_ok=1 state_sensitive=1 path_independent=1`) into
  `corpus/evidence/round72/c1-selftest.txt` and a replicate of the C1 control
  (`.ufo/waves/round-72/w1/C2ControlsR72.md`).
- **Provenance attacked.** `ProvenanceAttackR72` ran four attacks — the `/app` stub under a caller
  `PYTHONPATH`, a `transformers.py` in the sandbox cwd, `BASH_ENV`/`PYTHONSTARTUP`/`PYTHONHOME`
  injection, and a write into the bound venv — and none succeeded; `sys.path` inside the sandbox
  begins `/probe`, not `/app`, and the `/venv` bind answers `OSError:[Errno 30] Read-only file
  system` (`.ufo/waves/round-72/w1/ProvenanceAttackR72.md`).
- **Receipt reviewed.** `ReceiptReviewR72` re-derived all 14 bindings (including nine
  `case_sha256` values re-staged with the probe's own `stage_case` and an independent
  `tree_digest`), refused a hand-written all-`P` receipt with 11 defects, refused a `LEGS K9`
  contradiction, and demonstrated the declared trust boundary: a fully forged receipt with a
  self-consistent `PROVENANCE` passes (`DEFECTS n=0`, rc 0), and `transformers_file` is checked
  only by its `/venv/` prefix (`.ufo/waves/round-72/w1/ReceiptReviewR72.md`).
- **Checker mutated.** `CounterMutateR72` built eight single-clause mutants of `check_receipt`
  (provenance absent, `env_cleared`, `distinct`/path, `canary_seen`, `allowlist_seen`, K9 case-set,
  `LIBRARIES`, `PROBE_BLOB`) and scored each on the genuine receipt plus a refusal target: six are
  load-bearing, and two are not — the K9 case-set membership is a duplicate of four clauses that
  already price K9 (`case-digest-unique`, the per-case digest re-stage, the vector loop and
  `cases_ok`), and the `PROBE_BLOB`/`PROBE` equality is implied by the two individual digest clauses
  (9/9 pairs identical) (`.ufo/waves/round-72/w1/CounterMutateR72.md`, `corpus/evidence/round72/c1-counter-mutants.txt`).
- **Gate metric attacked.** `GateMutateR72` confirmed the shipped matrix is not invariant (6 killed,
  1 null) and built six fresh semantic mutants the shipped table does not cover
  (`.ufo/waves/round-72/w1/GateMutateR72.md`).
- **Claims falsified.** `ClaimFalsifyR72` attacked both claims — a hand-written receipt, K9
  reachability, leg/assert granularity, a content-free erratum, and a factually wrong registry row
  (`.ufo/waves/round-72/w1/ClaimFalsifyR72.md`).
- **Registry audited.** `RegistryAuditR72` checked the four new rows' eight cells against the
  scripts' real flags and listed every `plans/round7[12]_*.py` file against its row
  (`.ufo/waves/round-72/w1/RegistryAuditR72.md`).
- **Entry and index audited.** `KnowledgeIndexR72` re-checked the provenance trio, every quoted
  line against the committed captures, and index parity in both directions
  (`.ufo/waves/round-72/w1/KnowledgeIndexR72.md`).
- **Sources.** S247 (`bwrap(1)` `--clearenv`) and S248 (the `distilbert-base-uncased-finetuned-sst-2-english`
  model card) were fetched live this round, captured byte-exact under
  `corpus/evidence/round72/sources/`, and appended as tier-A rows.
- **Knowledge entry.** `corpus/knowledge/tb2-hf-model-inference-provenance.md` (six reuse rules for
  the next `network-service` replay), indexed at `corpus/README.md:96`.
- **Lesson.** `corpus/lessons/round-72.md` (scribe `LessonDraftR72`): Gate (S247/S248 admits, the
  `merge/kengaku` verdict with reason + flip, census before→after, the entry's admission status),
  the Mistakes table (the L1's two own rows plus the wave's findings), Census, Verdicts, Limits.
- **Structural gates.** `DepthGateR72` re-ran both: depth `ROWS n=16 class_match=True
  count_mismatch=0 paths total=36 resolved=36 share=1.00`, `PREDICATE R63-C2 pass`; trio
  `SWEEP files=72 trio_open=43 addendum=29 red=0`, `PREDICATE R64-C3 pass`; class-row counters
  `executed 4 of 8` = 1 (rc 0) and `executed 3 of 8` = 0 (rc 1, no match)
  (`corpus/evidence/round72/gates/`, `.ufo/waves/round-72/w1/DepthGateR72.md`).
- **Overlap scan.** `SiblingOverlapR72` classified every fleet hit for the round's terms as
  term-level vs surface-level and found no sibling owning a sandbox-provenance witness, a
  registry-conformance gate or a fixture-matrix mutation metric
  (`.ufo/waves/round-72/w1/SiblingOverlapR72.md`).

**Round-72 wave findings (reported, not smoothed).** F1 the sandbox's observed key set is 11, not 9
(`PWD` from bwrap, `TORCHINDUCTOR_CACHE_DIR` from torch's first `from_pretrained`; the latter leaks
the host account name through `/tmp`, `HfBatteryR72.md` F1); F2 a fully forged receipt passes
`--check-receipt` (declared limitation (v), demonstrated by `ReceiptReviewR72` §2b) and
`transformers_file` is prefix-checked only; F3 `E1b` is presence-only — an erratum with the two
revisions swapped still passes (`C2RedBeforeR72.md` F1); F4 `E1a` is first-row-wins and
duplicate-blind, and prices three of the row's six content fields (`C2RedBeforeR72.md` F2/F3); F5
the mutant matrix prices 6 of the gate's ~13 refusal sites (`C2RedBeforeR72.md` F4); F6 the frozen
`SUMMARY` quotation omits the `exc=2` term the checker recomputes (`HfBatteryR72.md` F2); F7 the
frozen selftest string is a prefix of the emitted line (`C2RedBeforeR72.md` F6). F8 `ClaimFalsifyR72` landed six receipt variants that pass `--check-receipt` with no battery behind them, including a stale `REV`/`PROBE_BLOB rev` (any ancestor of `master` passes), a `PROBE_BLOB` claiming a blob at a commit that lacks the file, a black-hole `/venv/DOES-NOT-EXIST/…` provenance path, and `EXC K9 …=E` declaring K9's L4 red an exception rather than the `:107` assert (`ClaimFalsifyR72.md` §C1-a, variants table); its K9-mechanism and leg-witness attacks failed. F9 `RegistryAuditR72` scored 9 of 32 cells of the first four registry rows defective and no row conformant — every row's usage path exits 1 where the row says 2, both c1 `0` cells contradicted their scripts' own `0 if PREDICATE … pass else 1` return, both write scopes omitted `--receipt`/`--evidence-dir` and `--share-net`, and the r71 c1 self-test cell was false; all four rows were rewritten before landing and the gate re-run green. F10 `GateMutateR72` showed the shipped mutant line is non-invariant but is not a coverage certificate: five of six fresh semantic mutants land in `null` because `REDS` lacks their fixtures, `E1c` and the fixture builder are structurally ungradeable, and the author-declared `target` field is unchecked.

**Routed defect R72-D1 (pre-existing, not introduced this round).** `plans/round52_c2_registry.py
--lane .` prints `ADVERTISED total=110 REGISTERED total=105 rows=107 MISSING 5 DUPLICATE 0` and
`PREDICATE R52-C2 fail`, rc 1 (`corpus/evidence/round72/registry-debt.txt`); at base it printed
`MISSING 7` with the two round-71 instruments among them, so this round closes exactly those two and
leaves five pre-existing rows absent (`round66_c1_tensor_probe`, `round69_c1_nginx_probe`,
`round69_c2_routed_defects`, `round70_c1_nginx_probe`, `round70_c2_routed_defects`). Round 73 must
add them; none is claimed here.

**Inherited state.** The lane was clean at the base tip (`jj-lane.sh state` → `ahead=0 behind=0
tracked=0 untracked=0`) and `.ufo/watchdog.log` shows `launch kengaku round=72 … attempt=1` with no
earlier `lane-dead-no-report kengaku round=72` line, so there was no earlier attempt to inherit.
Files I did not author were left untouched.

**Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` (no pathspec) is run
before the report; `clean: only `.scratch/` files (orchestrator-owned), another lane's `.ufo/reports/round-73/tsukuroi.md`, and the pre-existing `after` file (mtime 20:05, before this round). No seat of this lane wrote a byte into the fleet root, so nothing was copied or deleted`.

**Tool installs: none.** `bubblewrap 0.13.1, python 3.13.16, torch 2.14.1+cu130, transformers 5.21.0 and requests 2.34.2 were already present on the host; no install or upgrade was needed or performed, and pacman stayed paused`

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| `plans/round-72-claims.md`; `plans/round72_c1_hf_probe.py`; `plans/round72_c2_routed_defects.py`; `SKILL.md` four registry rows; `plans/round-71-claims.md` `## Errata — round 72`; `corpus/SOURCES.md` S247/S248; `corpus/knowledge/tb2-hf-model-inference-provenance.md` + its `corpus/README.md:96` row; `corpus/evidence/round72/sources/**`; census-before; C2 red-before; the C1 do-nothing control; wave spec/dispatch/validate/ready | "Claims (frozen `b6336136` …)", "Landed (R72-C1)/(R72-C2)", "Sources" | `b6336136` |
| `LOG.md` round-72 entry; `SCORECARD.md` round-72 section + the `Superseded (round 72)` line; `corpus/README.md` knowledge row, lesson row, evidence row, `Partly discharged round 72` frontier line and supporting-artifacts block; `corpus/SOURCES.md` S248 line-count correction; the four registry rows rewritten in place (9 defective cells, `RegistryAuditR72`); the entry's three corrected statements; `corpus/lessons/round-72.md` | "Landed (R72-C1)/(R72-C2)", "Mistakes mined" and the scorecard section | `08df910a` |
| `corpus/evidence/round72/**` (receipt, check, replicate, stub before/after/control, nine sandbox captures + replicate captures, C1 selftest, C2 green/controls/gate-mutants/counter-mutants, registry-debt, gates, census-after) and `.ufo/waves/round-72/**` (16 seat reports, results, registry, spec/dispatch/validate/ready) | "Landed (R72-C1)/(R72-C2)", "Verification run this round" | `08df910a` |
| the final counter receipts re-run at the landing tip: `final-c1-check.txt`, `c2-green.txt`, `c2-controls-final.txt`, `census-after.txt` | "Verification run this round" | `db78d059` |
## Before → after measurements

1. **R72-C1** — counting command
   `python3 plans/round72_c1_hf_probe.py --lane . --check-receipt corpus/evidence/round72/hf/receipt.txt
   --work <scratch>`, measured at `08df910a461620741d433def3df38a8406efe9f` against the receipt produced at `b6336136`:
   `DEFECTS n=0`, `PREDICATE R72-C1 pass`, rc 0 (`corpus/evidence/round72/hf/check.txt`). Before at
   `c6322972`: the instrument is absent (`git cat-file -e c6322972:plans/round72_c1_hf_probe.py` →
   rc 128), and the class's previous instrument under the same injection fails — v1 +
   `PYTHONPATH=/app/stub` → `SUMMARY cases=8 … mismatches=6`, `PREDICATE R71-C1 fail`
   (`corpus/evidence/round72/hf/stub-before-v1.txt`) where v2 under the same injection carries
   `PROVENANCE … canary_seen=0 transformers_file=/venv/…` and `PREDICATE R72-C1 pass`
   (`stub-after-v2.txt`). After: nine `VECTOR … agree=True` with K9 `PPPF`,
   `LEG-COVERAGE legs=4 seen_p=4 seen_f=4`, `SUMMARY cases=9 legs=36 mismatches=0 setup=0 exc=2`,
   `PROVENANCE env_cleared=True allowlist_seen=9/9 distinct=1 canary_seen=0`, and
   `STUB-CONTROL exposed=False vectors_unchanged=True`.
2. **R72-C2** — counting command `python3 plans/round72_c2_routed_defects.py --lane .`, measured at
   `08df910a461620741d433def3df38a8406efe9f`: `E1a ok`, `E1b ok`, `E1c ok`, `E2 ok`, `DEFECTS n=0`, `PREDICATE R72-C2 pass`, rc 0
   (`corpus/evidence/round72/c2-green.txt`). Before at `c6322972` with the freeze instrument:
   `DEFECTS n=6`, `PREDICATE R72-C2 fail`, rc 1 (`corpus/evidence/round72/c2-red-before.txt`).
   Controls: `--selftest` → `defects-in-fake=3 want=3 all-fail=True append-only-arm=True
   positional-arm=True parser-arm=True`; `--mutants` → `MUTANTS total=7 killed=6 survived=0
   invalid=0 null_detected=1` (`corpus/evidence/round72/c2-controls.txt`).
3. **No axis harmed (counters).** `python3 plans/round63_gate_checks.py depth --skill SKILL.md
   --receipt corpus/evidence/round62/class-survey.txt` → `ROWS n=16 class_match=True
   count_mismatch=0 paths total=36 resolved=36 share=1.00`, `PREDICATE R63-C2 pass`;
   `python3 plans/round64_trio_sweep.py --sweep --lane .` → `SWEEP files=72 trio_open=43
   addendum=29 red=0`, `PREDICATE R64-C3 pass`; the round's whole diff carries **0 deletions**
   (`git diff --numstat c6322972 master | awk '{d+=$2} END {print d}'` → 0);
   `sources-census.sh validate --root … kengaku` → rc 0, 240 rows, 25 `W04`.

**Named limitations of the verdicts (found this round, recorded, not smoothed).** (i) The candidate
is a lane-written stdlib HTTP server, not the Flask app the task asks; the grader's own requests
decide the legs. (ii) `torch`/`transformers` come from `/fast/ComfyUI/.venv` bound read-only
(python 3.13.16, torch 2.14.1+cu130, transformers 5.21.0, requests 2.34.2); `LIBRARIES` is measured
on the host by design, and the sandbox sees 11 environment keys, not 9 (`PWD` from bwrap,
`TORCHINDUCTOR_CACHE_DIR` added by torch's first `from_pretrained`, which embeds the host account
name). (iii) The staged model is a five-file synthetic fixture, not distilbert (S248): the replay
prices the grader's logic, not a model's accuracy. (iv) `test_flask_api_running` accepts any HTTP
answer; K5 prices the only failing mode a live listener can have. (v) `--check-receipt` is a
consistency check over committed bytes: a fully forged, internally consistent receipt passes, and
`transformers_file` is checked by its `/venv/` prefix only (`ReceiptReviewR72` §2b) — the nine
per-case sandbox captures are the live witness. (vi) The covered unit is the assert site only where a case reaches it: 7 of the grader's 19 assert
sites are priced (`SurfaceScoutR72` §2). Of the 12 unpriced, 10 fall in five server-priceable groups
and 2 (`:19`, `:20`) are priceable only by the stub the provenance witness exists to exclude — the
claim's "five groups" is right only under that exclusion, and the exclusion is stated here. K6's
L3/L4 `F` cells are connection exceptions recorded on `EXC`, not assertion failures. (vii) R72-C2's
erratum check is presence-only: an erratum that quotes both labels and both revisions passes even if
the revisions are attributed to the wrong artifacts (`C2RedBeforeR72.md` F1); `E1a` is first-row-wins
and duplicate-blind (F2) and prices three of a row's six content fields (F3); the mutant matrix prices
6 of ~13 refusal sites (F4). (viii) The base `n=6` conflates "round-71 rows added" with "round-72
instruments exist at tip" (F5). (ix) The Q13/Q14 second-seat re-read of
`corpus/knowledge/tb2-hf-model-inference-provenance.md` is not on record from a `w2`/`falsify`
registry, so the entry lands `admission: hold`; `plans/gate_timing_check.py` prints `no admit rows …
failed=1` and that FAIL is the honest state. (x) The claim's kill rule names a duplicated `PROVENANCE`
line, but `check_receipt` reads only `prov_lines[0]`; a duplicated line is not refused (lesson row 3).
The receipt of record carries exactly one, so the evidence is unaffected — the rule is unimplemented.
(xi) The first version of the four registry rows was defective in 9 of 32 cells and was rewritten in
place before landing (`RegistryAuditR72`); the freeze commit preserves the defective text, and the
gate was re-run green after the rewrite. (xii) The knowledge entry was drafted before the battery and
carried three statements its receipts contradict (an "exactly the `--setenv` list" claim, "19 KB", and
`env_cleared=True` presented as evidence); all three were corrected before landing and the correction
is a lesson row. (xiii) Index parity is not claimed: at the base tip the README already lacked one
knowledge row, 30 lesson rows and 39 evidence rows. This round adds one row per new file in each table
(knowledge 71→72 files and 70→71 rows, lessons 116→117 and 86→87, evidence 62→63 dirs and 23→24
rows), so the pre-existing deficits are unchanged and named, not closed. (xiv) The process-level
verification of the provenance witness is inside-out: the harness under test reports its own
environment and library file; kama's round-50 instrument reads `/proc/<pid>/environ` from outside, and
the lane has not adopted that shape (`SiblingOverlapR72` §F2(ii); `StubBeforeAfterR72` F4/F7).
## Sources & frontier

Census, the frozen command, run at round start and round end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku
```

- **Before** (`.ufo/waves/round-72/census-before.txt`): exit **0**, 238 data rows,
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 238, 25 `W04` warnings.
- **After** (`corpus/evidence/round72/census-after.txt`): exit **0**, 240 data rows, the same 25
  `W04` warnings, `ok …/corpus/SOURCES.md`.

**Rows added by tier.** Tier A **+2** (S247 the `bwrap(1)` manual's `--clearenv` entry, 27981 bytes,
sha256 `708f56ee…68de7`; S248 the `distilbert-base-uncased-finetuned-sst-2-english` model card, 10512
bytes, sha256 `75f17282…7588851`); tier B +0; tier C +0. Both rows are `status: mined`,
`used-by: corpus/knowledge/tb2-hf-model-inference-provenance.md`, `recheck: 2027-05-02`; each Gate
entry carries the access date (2026-11-03), the byte count and a located ≤25-word quote
(`--clearenv`: "Unset all environment variables, except for PWD and any that are subsequently set by
--setenv"; `README.md:145`: `model = DistilBertForSequenceClassification.from_pretrained(...)`).

**Rows touched old→new.** None edited; S247 and S248 are new rows appended inside the `## Registry`
section. S245/S246 were re-derived from their committed captures this round, with no row change.

**Frontier rows advanced.** The README frontier bullet on agentic benchmark task-spec audits gains a
`Partly discharged round 72` line: the first `network-service` replay in this lane whose model-load
witness is a provenance check rather than an outcome check, and whose table prices both assert sites
of leg 4. The clause stays open for the remaining TB2 graders, the twelve unpriced assert sites, and
runtime task validity (refused to this lane).

**Assimilation: none.** One `merge/kengaku` entry was considered and refused — reason, flip
condition and the re-opened bytes are recorded in `corpus/lessons/round-72.md` `## Gate`. No row from
the package was appended.

## Trend verdicts

- **expansion: improved** — the `hf-model-inference` replay moves from leg-level to
  provenance-witnessed + assert-site-priced evidence (nine cases, K9 reaching
  `tests/test_outputs.py:107`, `PROVENANCE … canary_seen=0`), the class row's receipt pointer now
  cites the round-72 receipt, the new entry adds six reuse rules for every `network-service` replay,
  and the registry gains four rows (census 238 → 240; `ADVERTISED` 108 → 110 with the two round-71
  rows closed).
- **quality: improved** — the round-71 closure's two routed defects close by a gate that moves
  `n=6` → `n=0`, is killed 6/6 with an attribution arm and a demonstrated null, and repairs the
  `parse_count` false-red class; the corrected probe's selftest arms (8/8) replace the two defective
  round-71 arms; the C1 stub injection that defeated round 71 now fails.
- **discernment: improved** — the wave's attack seats wrote the round's defects down instead of
  smoothing them: the provenance attacks all failed and are recorded as failed; the forged-receipt
  pass, the presence-only erratum check, the duplicate-blind registry check and the mutation matrix's
  unpriced sites are all named; the do-nothing control refuses; the entry is held rather than
  self-admitted; and the pre-existing registry debt (5 missing rows) is routed, not absorbed.
- **adjacency: unchanged** — `SiblingOverlapR72` found **12 surface-level sibling sites** in six
  lanes (tabi's `check-gate-registry.mjs` for (b); kama's `KAMA_R50_CANARY` + `/proc/<pid>/environ`
  arm for (a); tabi, kasegi, souji and tameshi mutation metrics for (c)), each named with file and
  line and routed, not absorbed. The province boundary is unchanged — the replay and its evidence
  remain this lane's — but the round built its three instruments without citing that prior art,
  which is recorded as a lesson row rather than scored as a move. No score change.
- **novelty: unchanged** — no instrument-level construct is claimed: `--clearenv` is a restoration
  of the lane's round-64…67 probes (`SiblingOverlapR72` §T5), and the new artefact is the provenance
  line plus the ninth case, both recorded as coverage evidence.

## SHONEN

Four boxes in `SHONEN.md`, all `[~]` with a resolvable pointer:

- [~] **SKILL.md contains real decision tables, error patterns, checklists, cited sources** —
  `SKILL.md` `## Decision table — grader class → offline replay recipe` (16 rows, the
  `network-service` row reading `executed 4 of 8`) plus the four new `## Gate/probe registry` rows at
  `:695-698`; `python3 plans/round63_gate_checks.py depth …` → `PREDICATE R63-C2 pass`
  (`corpus/evidence/round72/gates/depth-gate.txt`).
- [~] **At least one end-to-end domain task executed and logged in LOG.md** — the nine-case replay:
  `LOG.md` "Landed (R72-C1)" → `corpus/evidence/round72/hf/receipt.txt` at `08df910a461620741d433def3df38a8406efe9f`.
- [~] **Instructions executable by an agent without oral context** —
  `corpus/knowledge/tb2-hf-model-inference-provenance.md` `recheck:` carries the full command
  (probe, work dir, port lock, receipt, check), re-derived at `b6336136` and independently
  re-checked by `KnowledgeIndexR72`.
- [~] **No cross-domain bleed (PROVINCE.md still accurate)** — `SiblingOverlapR72` classified every
  fleet hit as term-level vs surface-level and found no sibling owning the provenance witness, the
  registry-conformance gate or the fixture-matrix metric; `PROVINCE.md` unchanged this round.

## Addendum — L0, process notes, stale lane

- **L0 carried (no new question):** `kengaku | round-25/33/51`, `round-54`, `round-56`,
  `round-63`, `round-65`, `round-66`, `round-67` (labrat role).
- **Process note:** the L1's first control invocation omitted `--control`, so the receipt written to
  the control path was a *passing battery*; it was re-run with the flag and the receipt of record now
  reads `CONTROL … derived_set=FFFF`. The mistake is a lesson row.
- **Process note:** the first clean check of a pre-freeze receipt printed
  `DEFECT probe-blob … sha256=unknown`; batteries of record run after the freeze commit. Lesson row.
- **Routed defect R72-D1** (above): five pre-existing instruments still lack registry rows;
  `plans/round52_c2_registry.py` is red at both ends of this round (`MISSING 7` → `5`).
- **Stale-lane:** respawn-per-round driver; this was round 72 attempt 1 and no other mission of this
  lane is open. Round 73 starts from the planned row in `SCORECARD.md`.
