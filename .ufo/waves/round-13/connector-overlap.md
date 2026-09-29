# Connector overlap survey — round 13

## Findings

The lane boundaries are mostly sound: the protocol lane owns cross-lane closure and the `PROTOCOL.md` contract; kumitate's `round-gate.mjs` is an intentional same-lane pre-check, not a second fleet closure authority; kagi's claim ledger is a different evidence ledger. I found no sibling lane independently compacting `PROTOCOL.md` in the requested report/LOG/SCORECARD sweep.

The significant overlap risk is not a second implementation but a contract seam: `round-gate.mjs`'s local SHONEN predicate rejects kotoba's numbered `## 9. SHONEN` heading, and its documentation still cites old `PROTOCOL.md` line numbers. Keep the local gate, correct its stale citations, and preserve the protocol checker as the only fleet-level MANIFEST/closure authority.

## Gate/probe registry coverage

### Search method and counts

Tracked runtime verifier candidates were enumerated from the current lane entry-point directories. The count command and output were:

```text
$ printf 'kagi: '; git -C kagi-shokunin ls-files 'corpus/*.sh' | wc -l; printf 'kotoba: '; git -C kotoba-shokunin ls-files 'verifiers/*.sh' 'verifiers/*.py' | wc -l; printf 'kengaku: '; git -C kengaku-shokunin ls-files 'grader.py' | wc -l; printf 'kumitate: '; git -C kumitate-shokunin ls-files 'scripts/*.mjs' | wc -l; printf 'kake: '; git -C kake-shokunin ls-files 'scripts/*.mjs' | wc -l
kagi: 5
kotoba: 5
kengaku: 1
kumitate: 5
kake: 1
```

The full tracked-script pattern sweep used `--selftest|--self-test|SystemExit|sys.exit|process.exit|exit\([0-9]` over `.sh`, `.py`, and `.mjs` files in each lane. It found 25 pattern-bearing files: kagi 5, kotoba 5, kengaku 9, kumitate 5, kake 1. Eight of the kengaku hits are under `corpus/evidence/` and are historical analysis/mutation helpers, not current lane entry-point verdicts: `round10-fleet/{mutate_test.sh,probe_ref.py,schema_probe.py}`, `round11-fleet/{grader_r11_draft.py,mutate_r11.sh,recompute_r11_draft.py}`, `round11-power/recompute_r11.py`, and `round9-fleet/test_harness.py`. For example, `mutate_test.sh` says it mutates copies to test `grader.py` (`kengaku-shokunin/corpus/evidence/round10-fleet/mutate_test.sh:2-7`); `grader_r11_draft.py` labels itself a DRAFT (`.../round11-fleet/grader_r11_draft.py:1-7`); `schema_probe.py` says “Exit 0 always (research probe, not a pass/fail grader)” (`.../round10-fleet/schema_probe.py:2-6`). I exclude these archive helpers from the active registry count, but flag `schema_probe.py` as a scope edge: if it remains an offered, current probe rather than archived research, Gate standard requires a `probe` row or an explicit retirement note.

The active inventory is 16 gate candidates plus the one probe that explicitly self-identifies as a report rather than a gate (`kake-shokunin/scripts/probe-delta.mjs:24-26`). The tracked entry-point census produced the lane counts above and these files:

| Candidate script | Observed kind | Registry row | Missing fields |
|---|---|---|---|
| `kagi-shokunin/corpus/claim-ledger.sh` | gate | absent | ALL-8 |
| `kagi-shokunin/corpus/drift-pins.sh` | gate | absent | ALL-8 |
| `kagi-shokunin/corpus/op-ref-probe.sh` | gate (contract verdict) | absent | ALL-8 |
| `kagi-shokunin/corpus/surface-census.sh` | gate | absent | ALL-8 |
| `kagi-shokunin/corpus/transcript-scan.sh` | gate | absent | ALL-8 |
| `kotoba-shokunin/verifiers/fault_injection_corpus.sh` | gate/test harness | absent | ALL-8 |
| `kotoba-shokunin/verifiers/verify_corpus_independent.py` | gate | absent | ALL-8 |
| `kotoba-shokunin/verifiers/verify_corpus_integrity.py` | gate | absent | ALL-8 |
| `kotoba-shokunin/verifiers/verify_harness_claims.py` | gate | absent | ALL-8 |
| `kotoba-shokunin/verifiers/verify_surfaces.py` | gate | absent | ALL-8 |
| `kengaku-shokunin/grader.py` | gate | absent | ALL-8 |
| `kumitate-shokunin/scripts/cite-check.mjs` | gate | absent | ALL-8 |
| `kumitate-shokunin/scripts/claims-check.mjs` | gate | absent | ALL-8 |
| `kumitate-shokunin/scripts/proxy-check.mjs` | gate | absent | ALL-8 |
| `kumitate-shokunin/scripts/round-gate.mjs` | gate | absent | ALL-8 |
| `kumitate-shokunin/scripts/surface-probe.mjs` | gate (verdict-bearing) | absent | ALL-8 |
| `kake-shokunin/scripts/probe-delta.mjs` | probe (report; exit 0 on parsed history) | absent | ALL-8 |

`ALL-8` means the whole registry row is absent, so every row field is missing: **name; `gate|probe`; entry command; verdict map; self-test command and spelling; pinned-value path; write scope; owner.** This uses `PROTOCOL.md` §Gate standard, which says the rows live in each lane's `SKILL.md` and enumerates those fields (“name, `gate|probe`, entry command, verdict map … pinned-value path, write scope, owner”; §Gate standard, “Registry”).

The structured-row sweep across all five lane `SKILL.md` files was `^\|.*\|\s*(gate|probe)\s*\|`; output: `kagi: rows=0`, `kotoba: rows=0`, `kengaku: rows=0`, `kumitate: rows=0`, `kake: rows=0`, `total rows=0`. Thus the registry has no active rows and every listed candidate lacks all eight row fields, even where scattered prose supplies some commands or verdict details. The aggregator ledger is explicitly not the missing inventory: `PROTOCOL.md` §Gate standard says “The aggregator ledger stays the routed-defect queue, not a second inventory; a fleet index is pointers to lane rows, never copied expected values.”

One additional boundary signal: kotoba's `SKILL.md` advertises `verifiers/verify_skill_checklist.py` at lines 259-263, but `git -C kotoba-shokunin status --short -- verifiers` returned it as `??`, alongside its fixture directory and `checklist-command-vocabulary.json`. It is untracked and therefore excluded from the tracked-script count; it cannot yet satisfy a committed gate row.

## Overlap and ownership

### `PROTOCOL.md` compaction

The search sweep `(?i)PROTOCOL.{0,40}compact|compact.{0,40}PROTOCOL` over `.ufo/reports/round-{12,13,14,15}/*.md` and each child lane's `LOG.md`/`SCORECARD.md` returned only the protocol lane's own `.ufo/reports/round-12/protocol.md:484-485` (the stated 526-to-470-line move). No sibling lane's report or scorecard claims an independent protocol compaction. No work should be migrated to another lane.

### Same checks, different authority

- **Kumitate `round-gate.mjs`: necessary local pre-check, not duplicated fleet closure.** Its own boundary says it is not fleet report-conformance authority and checks only kumitate's report; the knowledge note says it “never assigns a lane-round status” (`kumitate-shokunin/scripts/round-gate.mjs:13-19`; `kumitate-shokunin/corpus/knowledge/round-close-gate.md:81-89`). It intentionally overlaps citation/SHONEN predicates to catch local defects before filing. Protocol still owns reading all lane reports, prompts, and MANIFEST status. Retain both; do not port the local checker into the aggregator or replace protocol closure with it.
- **Kagi claim ledger: adjacent, not a duplicate of MANIFEST.** `corpus/claim-ledger.tsv` stores per-command expected output/exit claims, including transcript-scan `HITS=2` (`kagi-shokunin/corpus/claim-ledger.tsv:1-10,20-22`); it does not adjudicate cross-lane `rounds[]`. The routed defect remains real because those transcript expectations are not enforced inside `transcript-scan.sh` itself (`kagi-shokunin/corpus/transcript-scan.sh:76-80,276-282`). Keep the claim ledger for its own claim surface; add the gate's own persisted expected-value check rather than copying MANIFEST closure semantics into it.
- **Aggregator: queue only.** Keep `AGGREGATE.md`/the routed defect ledger as the queue and references to lane-owned rows. It must not become a second registry with duplicated expected values, consistent with `PROTOCOL.md` §Gate standard, “Registry.”
- **Host/runtime doctrine: analogous freeze mechanism, separate contract.** Native dispatch already freezes `{bytes,text,digest}` inputs and rechecks drift (`kumitate-shokunin/corpus/knowledge/native-trial-launch.md:17-20,89-113`); native handoff binds a verdict digest and derives `mission_goal` only from plan acceptance criteria (`kumitate-shokunin/corpus/knowledge/native-judge-pipeline.md:91-119`). These are useful implementation precedents for immutable evidence, not an owner for the fleet's historical MANIFEST closure. `PROTOCOL.md` §Gate standard, “Scope,” explicitly says a lane verdict never defines `loop_stop`/`mission_goal` or stands in for the native judge.

### Recommendation for contested protocol-owned obligations

1. **History pin over `MANIFEST.json.rounds[]`:** keep checker and pin under the protocol/integrator closure artifacts. `PROTOCOL.md` §Round-robin rounds says “`rounds` is append-only after closure,” corrections append typed `closure-correction` rows with `supersedes`, never in-place edits/prepends, and consumers read in array order (“last row for a lane wins”; §Round-robin rounds). A round-13 frozen prefix/pin should detect rewriting an old entry such as the m1 status flip while permitting valid appended rows/corrections. Do not rely only on whether an old fleet-keyed row can be semantically adjudicated. Avoid a whole-file digest rule that rejects every legitimate append; compare protected historical bytes/structure and the append/correction relation.
2. **Generalized `--frozen`:** accept an explicit committed baseline path anywhere in the protocol repo, not a path constrained to `.ufo/waves/round-12/`; record which committed snapshot was read and verify its digest before evaluating the live MANIFEST. Keep the default/expected-value owner in the protocol lane's own wave artifacts, so moving the baseline cannot silently move the expectation with it. This borrows the host's freeze discipline without making native dispatch responsible for fleet closure.
3. **Registry adoption:** each owner puts its row in its own `SKILL.md`; a fleet index, if needed, contains pointers only. Do not have the aggregator mirror rows or expected values. Mark archive-only probes/helpers as retired or keep them in evidence archives rather than silently widening the runtime registry.

Second-order risk: a user-editable frozen path can turn `--frozen` into a “baseline edited together with input” green path; require a committed snapshot/digest. Conversely, pinning the entire current MANIFEST byte-for-byte would reject legitimate append-only closure corrections. The m1 detector must preserve both immutability of closed history and the valid append-only correction form.

## Routed-defect follow-through

The defect baseline is `.ufo/reports/round-12/protocol.md:274-296`. I re-ran the SHONEN predicate used by both the fleet closure checker (`.ufo/waves/round-13/closure-check.py:73-74`) and kumitate's local checker (`kumitate-shokunin/scripts/round-gate.mjs:328-330`): `^#{1,6}\s*SHONEN`. The sweep output was `NO_MATCH` for `.ufo/reports/round-14/kasegi.md`, `.ufo/reports/round-13/kotoba.md`, and `.ufo/reports/round-11/kengaku.md`. The kotoba file literally has `## 9. SHONEN` (`.ufo/reports/round-13/kotoba.md:145`), but the current machine predicate does not recognize that numbered heading; by the implemented contract its SHONEN obligation is still unmet.

| Routed issue | Status | Current evidence |
|---|---|---|
| Kasegi r14 SHONEN heading | **Not landed** | The exact heading sweep above returned `NO_MATCH` for `.ufo/reports/round-14/kasegi.md`; protocol routed the missing heading at `.ufo/reports/round-12/protocol.md:276-277`. |
| Kasegi dead receipt pointer | **Landed as a correction** | r14 report labels the correction and explains that receipt IDs `4028846`/`a169f309` live in `origin-work`, not the named reconcilers (`.ufo/reports/round-14/kasegi.md:52-58`); current `SKILL.md` points to the surviving receipt paths (`kasegi-shokunin/SKILL.md:683`). |
| Kasegi vanished PROVINCE root | **Factual correction landed; scope re-point still operator-owned** | `PROVINCE.md` records that `~/Projects/bounties` was removed and names surviving roots, but explicitly says whether to re-point is an operator decision (`kasegi-shokunin/PROVINCE.md:5-14`). This resolves the false-on-disk premise without claiming authority to re-scope. |
| Kotoba r12 `LANE_HASH` | **Not landed** | `.ufo/reports/round-12/kotoba.md:224` still contains the literal placeholder; `git status --short -- .ufo/reports/round-12/kotoba.md` returned `?? .ufo/reports/round-12/kotoba.md`. |
| Kotoba r13 SHONEN | **Not landed under the actual predicate** | `.ufo/reports/round-13/kotoba.md:145` says `## 9. SHONEN`, but the exact predicate returned `NO_MATCH`; checker regex is `.ufo/waves/round-13/closure-check.py:73-74`. |
| Kotoba `--self-test` | **Not landed** | `verify_harness_claims.py` describes the mode as “check the script's model only” (`kotoba-shokunin/verifiers/verify_harness_claims.py:607-620`), which fails `PROTOCOL.md` §Gate standard, “Self-test” (“a helper-only or model-only self-check does not satisfy this clause”). |
| Kotoba no-baseline mode disagreement | **Not landed** | The same file sets `baseline=None` when absent (`:632-640`), JSON returns `0` with no baseline (`:642-644`), while text prints “no baseline” and returns `3` (`:661-667`). |
| Kengaku r11 SHONEN | **Not landed** | Heading sweep returned `NO_MATCH` for `.ufo/reports/round-11/kengaku.md`; the route is `.ufo/reports/round-12/protocol.md:285-287`. |
| Kengaku bare asserts | **Not landed** | Current `grader.py` still has bare asserts at `kengaku-shokunin/grader.py:1570,1631`. |
| Kengaku verdict revision | **Not landed** | Main output prints only `CHECKS ...` and `VERDICT` then returns (`kengaku-shokunin/grader.py:1695-1701`); it names no measured revision, contrary to `PROTOCOL.md` §Gate standard, “Two evidences.” |
| Kumitate commit identity | **Not landed** | The routed commits are named at `.ufo/reports/round-12/protocol.md:288-289`; current child history also still shows personal-author round commits (`git -C kumitate-shokunin log -4 --format='%h %an <%ae> %s'` returned `637d181 Joao Pedro Veiga <jpveigao10@gmail.com> …`, `dffbf0e Joao Pedro Veiga <jpveigao10@gmail.com> …`, `7a099b2 Joao Pedro Veiga <jpveigao10@gmail.com> …`). |
| Kumitate stale protocol citations | **Not landed** | `round-gate.mjs` still cites `PROTOCOL.md:263-267` and `:264-265` (`kumitate-shokunin/scripts/round-gate.mjs:13-18`); the companion knowledge note repeats the old references (`kumitate-shokunin/corpus/knowledge/round-close-gate.md:81-89`). |
| Kumitate `49/49` stale count | **Corrected in lane evidence; operator queue still stale** | I ran `node scripts/round-gate.mjs --selftest` in `kumitate-shokunin`; observed tail: `ROUND_GATE_SELFTEST: 57/57 pass` and `VERDICT: PASS`. `kumitate-shokunin/LOG.md:335` and `corpus/knowledge/round-close-gate.md:328-332` record the later count; the historical round-10 `49/49` remains correctly labeled as that older revision (`round-close-gate.md:271-288`). The main operator question still says `49/49` (`.ufo/l0-questions.md:8`), so only the sibling correction landed. |
| Kagi r12 report landing | **Not landed** | `git status --short -- .ufo/reports/round-12/kagi.md` returned `?? .ufo/reports/round-12/kagi.md`; the heading sweep also returned `NO_MATCH`. |
| Kagi transcript in-gate pin | **Not landed** | `transcript-scan.sh` comments document `HITS=2`, but the execution path only prints the observed count and exits on hits (`kagi-shokunin/corpus/transcript-scan.sh:76-80,276-282`); expected output is in separate `claim-ledger.tsv` rows (`:20-22`), not compared by this gate. |
| Kake r13 in-place erratum | **Not landed** | `git show --format= --unified=3 1dc7f6b -- .ufo/reports/round-13/kake.md` showed the existing timestamp line replaced with a parenthetical inline r14 erratum (`.ufo/reports/round-13/kake.md:17-18`). The r14 report confirms it was filed with an inline edit (`.ufo/reports/round-14/kake.md:110-115`), not appended after the filed bytes or carried as a separate addendum as routed at `.ufo/reports/round-12/protocol.md:295-296`. |

## Dissent / unresolved edge

There is a legitimate scope choice around archived probes: `schema_probe.py` expressly says it always exits zero and is a research probe, while the active skill entry-point census excludes evidence-archive helpers. My recommendation is to mark archived helpers as such and count only current lane entry points; if a lane still expects operators to invoke `schema_probe.py`, register it as a `probe` rather than treating “research” as an implicit exemption. Also, do not credit kotoba's numbered SHONEN heading unless the checker contract is deliberately changed: current checker behavior is unambiguous.
