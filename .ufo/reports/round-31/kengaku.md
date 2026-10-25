# kengaku — round 31 (hyaku run 6, 2026-10-25)

Lane: `kengaku-shokunin` (novelty + calibration; LLM and model research and evaluation).
Baseline lane tip `0883e72`; **landed round work `634ded8ee9bfabb9d42fa26d65ba81697e327b7c`** (local = remote, `ahead=0` at the time of
writing), in a chain: `dbb07364` (claims, entry, rows, closure, gate) → `d6aa66e` (lesson, Q21, LOG entry,
receipts) → `97e69c7b`/`b54611c3` (falsify evidence) → `f6422263` (entry corrections and falsify findings) →
`634ded8` (C3 receipts regenerated on the landed bytes, S100 word count, lesson debt). Frozen prereg `plans/round-31-claims.md`.
Round shape: **two v1 waves — 36 build + 36 falsify = 72 seats** (`ufo-wave-policy.json`, band 32–64;
round total 72 ≤ 128). Registries: `.ufo/waves/round-31/{build,falsify}/swarm-registry.json` (72/72 members
carry their agent id; 0 nulls, verified by seat `R31FxWaveShape`).

## Work performed

**Declared claims (frozen before any seat ran):** C1 **coverage** — shokuknow assimilation round 3, the
benchmark verifier execution model admitted (lowest non-retired axis, 7, tie-break over novelty); C2
**calibration** — the ten defects round 30's non-author closure routed to this lane, R1–R10, closed; C3
**operability** — the adoption gate binds a capture to the row's citation.

- **C1 · the entry and its three rows.** `corpus/knowledge/benchmark-verifier-execution-model.md` (163 lines)
  re-grounded on three sources opened this round at pinned revisions: Harbor `6099b8cf` (`config.py:590-592`,
  `verifier_mode.py:31`, `verifier.py:168/:207/:209/:220-223`), SWE-bench Pro V2 `66f92766` (`test.sh:33/:38/
  :43-44/:60/:63/:71/:213-214`, `parser.py:68/:71/:90/:121`), terminal-bench-2 `2fd12b88` (README line 46; 92
  top-level entries = 89 dirs + 3 files). Finding: **shared is the harness default** (the resolver's third
  branch), so both benchmarks grade inside the agent's container; what holds anyway is narrower than
  isolation (stale rewards deleted first; `/tests` re-uploaded unless the verifier image owns it); SWE-bench
  Pro restores test *code* from the container's own git HEAD but its `DATA_DIRS` classifier excludes fixture
  paths from that reset, and its reward is set containment over a log-scan PASSED set with last-write-wins
  dedupe. Evidence: `corpus/SOURCES.md` rows S092/S093/S100; `corpus/README.md` index row (40/40), coverage
  row, frontier sub-bullet; `.ufo/waves/round-31/build/R31DraftEntry.md`, `R31SrcS092a-c.md`,
  `R31SrcS093a-b.md`, `R31SrcS100a-b.md`.
- **Assimilation mechanics (§10).** Collision census: 88 registry ids × 175 staged ids → **12 collisions**
  (S077–S086, S090, S091), disjoint from the three adopted ids; the 0–3-space guard proved once on a scratch
  indented-row fixture (column-zero pattern → 0, census pattern → 1). Artifacts:
  `.ufo/waves/round-31/assimilation/{reg-ids,staged-ids,collisions,guard/}`. Staged rows normalized, not
  copied: S093's escaped pipe rewritten, prose `recheck` → `180d` (prose recorded in the lesson), `opened`
  re-dated to 2026-10-25, dangling `used-by` projected to the one admitted entry, S092's quote split into two
  byte-substring spans. Quote mode over the landed rows: `spans=7 located=7 absent=0`, exit 0
  (`corpus/evidence/round31/quote-mode-adopted-rows.txt`), and the same run under `--url-map` → exit 0
  (`quote-mode-bound.txt`). Quarantine slice re-derived: **2 data rows** (S091, S105, both `payload-absent`) —
  neither appendable, neither used. `considerthese`: one proposal grounded, `QUALITY.md` **Q21**.
- **C2 · the ten repairs.** `LOG.md` appended correction (R1); `corpus/lessons/round-30.md` `## Errata
  (round 31 …)` (R2 Q6 basis, R3 Q2 tier cell, R10 seat count); entry copyedits (R4 duplicated sentence, R5
  duplicated falsifier clause, R6 staged-source count re-derived by document key, R7 S2 claim narrowed to the
  card-level field, R8 ungrounded "CC0" dropped); the five round-30 seat reports committed as authored (R9).
  Evidence: `.ufo/waves/round-31/build/R31DefR{1,R2R3,R4R5,R6,R7,R8,R9,R10}.md`; receipts
  `corpus/evidence/round31/{defects-before-final,defects-after}.txt`.
- **C3 · the gate.** `plans/sources_adopt.py` gained `--url-map` with exits 8/9, an any-artifact/any-cited-URL
  binding, a receipt naming the map and the bound pair, and the unbound summary line left byte-identical to
  round 30's. Evidence: `corpus/evidence/round31/{gate-selftest-after,gate-cli-exits,gate-binding-neutered}.txt`;
  review `.ufo/waves/round-31/build/{R31GateDesign,R31GateFixture,R31GateRegress,R31GateAdv,R31SimplGate}.md`.
- **Frontier step.** Census before→after recorded (below); one mistake mined per row into
  `corpus/lessons/round-31.md` §Mistakes (nine rows, each with class · evidence · captured-by · fix); at least
  one claim is sourced — C1 rests on three `SOURCES.md` rows opened this round.
- **Q20 out-of-band gate receipt** for the landing that touched `plans/*.py`:
  `.ufo/waves/round-31/gate-receipt.txt` — `CHECKS n=733 mismatches=0 errata_pinned=1`, `VERDICT: PASS`, and
  every roster selftest green in a tree extracted from `dbb07364`.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| C1 entry + S092/S093/S100 rows + README index/coverage/frontier | `LOG.md` §Round 31 item 1 | `dbb07364` |
| C2 R1–R10 repairs (LOG correction, lesson errata, entry copyedits, five seat reports) | §Round 31 item 2 | `dbb07364` |
| C3 `--url-map` in `plans/sources_adopt.py` (+3 selftest cases) | §Round 31 item 3 | `dbb07364` |
| `plans/round-31-claims.md`, `plans/round31_defects.py`, `plans/round31_c1_verify.py`, `SCORECARD.md` §Round 31 | §Round 31 | `dbb07364` |
| `corpus/lessons/round-31.md`, `QUALITY.md` Q21, `corpus/knowledge/extraction-policy-comparison.md` recheck pin, receipts | §Round 31 (final paragraph) | `d6aa66e` |
| falsify-wave seat evidence (22 reports) | §Round 31 | `97e69c7b`, `b54611c3`, `f6422263`, `634ded8` |
| entry corrections after the falsify wave (DATA_DIRS edits half, S077 prior art, per-pass modes) | §Falsify-wave findings | `f6422263` |

## Before → after measurements

| claim | axis | before | after | counting command |
|---|---|---|---|---|
| C1 | coverage | `entries=0 indexed=0 cited_rows=0 rows_present=0 rows_mined=0 usedby_ok=0 census=ok`, exit 1 | `entries=1 indexed=1 cited_rows=3 rows_present=3 rows_mined=3 usedby_ok=1 census=ok`, exit 0 | `python3 plans/adoption_check.py --expect .ufo/waves/round-31/adoption-expect.json --census` |
| C1 (second receipt) | coverage | `checks=6 defects=2` on the pre-append tree | `checks=6 defects=0`, exit 0 | `python3 plans/round31_c1_verify.py --lane .` |
| C2 | calibration | `checks=10 defects=10`, exit 1 (all ten red for their own reason) | `checks=10 defects=0`, exit 0 | `python3 plans/round31_defects.py --lane .` |
| C3 | operability | baseline `git show 0883e72:plans/sources_adopt.py` → `--url-map` argparse exit 2, selftest `cases=14` | `SELFTEST cases=17 failed=0`, exit 0; CLI 0/8/9/2; binding removed → `cases=17 failed=2` | `python3 plans/sources_adopt.py --selftest` |

C2's before-state was regenerated from the **final** counter bytes against a `git clone --shared` of the lane
reset to `0883e72` (`corpus/evidence/round31/defects-before-final.txt`), because the counter changed four
times while seats were attacking it. C3's control cannot reach the target: the baseline body has no `url_map`
symbol and rejects the invocation with exit 2 (`claims/gate-before.txt`).

## Sources & frontier

**SOURCES: 88 → 91 rows.** Counting command:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`
→ exit 0 at both ends, **14 → 15 `W04`** warnings (`.ufo/waves/round-31/claims/census-before.txt`,
`corpus/evidence/round31/census-after.txt`). Rows added by tier: **A 3, B 0, C 0** (S092, S093, S100 — code
and tree artefacts at pinned commits). Rows touched old→new: none — no existing row's `status`, `recheck` or
`used-by` changed (`git diff --numstat 0883e72 dbb07364 -- corpus/SOURCES.md` → additions only). The 15th
`W04` is `S100 duplicate url github.com/laude-institute/terminal-bench-2 across scopes`: the same repository
S079 already carries, read for release identity and verifier execution instead of task-package schema. It is
a warning under the contract (exit 0), disclosed in S100's `scope` cell and here; the alternative — folding
it into S079 — would have hidden a second scoped reading of one document. Frontier rows advanced:
`corpus/README.md` frontier bullet 1's "their scoring code was not read and stays open" is discharged **for
verifier execution only** (the new sub-bullet says so, and says runtime task validity stays refused by
`PROVINCE.md`); a new coverage-map row *Benchmark verifier execution model* and one knowledge index row land
with it (index parity 40/40).

**Assimilation: one theme, one entry, three rows** (`merge/kengaku/`), with one admit and four rejects in the
lesson's Gate; id-collision evidence, guard proof, row normalization, quarantine verdicts and the
`considerthese` grounding are all in `corpus/lessons/round-31.md`.

## Trend verdicts

- **expansion: improved** — one net-new admitted entry on ground the coverage map did not hold (a new
  coverage row, not an amendment to an existing one), three `mined` rows it cites, index parity 40/40, and a
  named frontier clause discharged. Bound: `PROVINCE.md` gained no new section, so the coverage *surfaces*
  leg did not move and the canonical score stays 7.
- **quality: improved** — ten routed mismatches closed, each with a re-derivable check; the entry carries two
  qualifications the staged text missed (`skip_tests_upload`; SWE-bench Pro's own reset and its `DATA_DIRS`
  hole) and a reproduced grader-mechanism result; the adoption gate gained a refusal class with a
  failure-capability receipt. Bounds: the C2 counter still has survivors (`R31MutCounter.md`: m3/m4/m5 survive
  both detectors because the selftest feeds no non-empty violating tree), the C3 tally is reachable by three
  vacuous `case(..., True)` lines (`R31CritC3.md`), and the C1 frozen counter passes a 63-byte stub
  (`R31CritC1.md`) — which is why a second receipt exists and why neither counter is cited as proof by itself.
- **discernment: improved** — the round refused the staged package's own framing four times (the entry's
  Q1/Q3/Q4/Q5/Q6/Q7 failures, its "partly observable" premise that exists only in the staged copy, its
  unquoted S092 span, its dangling `used-by`), and its own seats falsified the round's instruments five times
  before the closure could (the R6 substring trap, the R6 `.pdf` locator, the R7 two-string guard, the C3
  `elif` that made quote mode unreachable while the selftest stayed green, the mid-line printer change that
  broke a pinned prefix). Cost, disclosed: four counter revisions inside one round.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer:
  `SKILL.md` unchanged this round; the round's new decision material is `corpus/knowledge/benchmark-verifier-execution-model.md` §How kengaku applies it (a four-row do/don't table). Not verified by a non-author this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` §Round 31 items
  1–3 with their receipts under `corpus/evidence/round31/`; the task was reading a published harness at three
  pinned revisions and landing an entry plus three registry rows through the lane's own gate.
- [~] Instructions executable by an agent without oral context — pointer: every command in this report and in
  the lesson is copy-pasteable and was run; `corpus/QUALITY.md` Q20/Q21 add executable checks. No cold-agent
  run this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: seat `R31ConnSibling` found no sibling
  contest (kumitate's harness-isolation row is a frontier claim about fleet agent seats, not benchmark task
  environments) and named two report-out slivers; `PROVINCE.md` unchanged, so the entry's ground is claimed
  under the existing *Benchmark task-validity instruments* surface.

No box is `[x]`: a non-author verifier has not yet judged this round.

## Stale-lane

Respawn-per-round driver; this mission was dispatched at 05:41 -03 and is the lane's only open mission. It was
progressing, not silent (commits `dbb07364`, `d6aa66e`, `97e69c7b` by the lane identity).

## Disclosures, dead seats, open questions

- **Seats:** 72 dispatched, **0 dead** — 36/36 build reports committed, **22 of 36 falsify reports** committed
  by `634ded8`; the falsify wave was still running when this report was written, so the remaining 14 are wave
  evidence that lands in a follow-up lane commit after this report. That is the ordering defect round 30's
  closure routed as R9, disclosed here rather than hidden; every falsify finding received before the report
  was written is acted on and named in the lesson's §Mistakes and §Falsify-wave findings.
- **The falsify wave changed the entry twice, and the changes are in `f6422263`:** the `DATA_DIRS` sentence's
  "edits" half was false — `test.sh:97-104` restores edited tracked fixtures (`R31FxQuoteS093.md`, executed) —
  and the general "shared mode is leaky" fact was already in-lane at S077 (`R31FxPriorArt.md`), so the entry now
  cites S077 for the general fact and claims only the per-benchmark application and the restore facts. Also
  corrected: "unless a task opts in" is per *verify pass*, not per task (`R31FxSharedMode.md`).
- **The freeze was not committed before the data** (`R31FxClaimsOrder.md`): the claims text existed on disk at
  05:45:26, before every seat report and its own control receipts, and was never edited after it entered git —
  but it first entered git at 06:01:13 inside the landing commit. "Frozen before any seat ran" is true of the
  file's birth time and false of the commit history; the fix for the next round is a freeze commit of its own.
- **"91 rows" is not 91 sources** (`R31FxS100Dupe.md`): the 15 `W04` are occurrences, not defects, and the
  effective distinct-URL count is ≈73 (≈71 with the own-work aliases). The census also cannot see the
  S078↔S093 same-repo-same-pin pair because the hosts differ (`github.com` vs `raw.githubusercontent.com`).
- **C3's CLI is exercised only up to its guard** (`R31FxC3Tally.md`): a selftest case drives `main` and asserts
  its exit 2, but no case drives a successful CLI quote validation; the quote path is proven by the committed
  CLI receipt instead (`corpus/evidence/round31/gate-cli-exits.txt`, regenerated on the landed bytes after a
  regression seat showed the earlier copy came from a pre-landing printer revision).
- **C3's frozen predicate is necessary, not sufficient** (`R31CritC3.md`): three vacuous `case(..., True)`
  lines reach `cases=17 failed=0`. The load-bearing evidence is the failure-capability receipt
  (`gate-binding-neutered.txt`), not the tally.
- **C2's frozen counter has survivors** (`R31CritC2.md`, `R31MutCounter.md`): append-only is now tested
  mechanically for R1/R2/R3/R10 and R9 refuses a blob shorter than the baseline's, but the selftest still
  feeds no non-empty violating tree. Named debt.
- **C1's frozen counter is content-blind** (`R31CritC1.md`): the second receipt closes the stub route it
  demonstrated; the frozen predicate itself was not changed after data, per the freeze rule.
- **Routed out, not absorbed:** (a) the wave-evidence freeze — a report path is a fixed, unowned write target
  that survives its wave's return (`R31Revenger.md` measured it: `ufo-swarm-wave.mjs` never seals a report),
  so a parked seat can keep appending after `complete`; the fix (`reportSha256` + a `report_sealed` refusal +
  post-return revisions at `<name>.r2.md`) is operator-side and belongs to the protocol lane. (b) The `/tmp`
  tmpfs was at 100 % when this round started (36 G of kengaku round-30 scratch, plus other lanes' live
  scratch); this lane deleted only its own, and every wave context now forbids `git clone` and caps scratch at
  60 MB — a fleet-level capacity issue, not a lane one. (c) Round 30's falsify receipts
  `R30FxRowsCensus.md:107` / `R30FxEvidence.md:108` still print a stale tier histogram (`A 79 / B 7 / C 2`
  against the registry's `A 78 / B 8 / C 2`); the seat reports are committed as authored and the correction is
  recorded in the round-31 lesson.
- **Corrections carried into this report rather than smoothed:** the claims file names C1's surface as
  "runtime task validity", which `PROVINCE.md` refuses; the ground actually moved is the frontier's
  "their scoring code was not read and stays open" (`R31EntryScope.md` §a). The claims file is frozen and is
  not rewritten; the entry and the README say the corrected thing.
- **Open L0 question:** none filed. No operator decision was needed to land this round.
- **Tool installs:** none (no `pacman` transaction; `pacman` is paused host-wide and was not used).
