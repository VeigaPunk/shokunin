# kengaku round 29 — attempt 2 (hyaku run 6): shokuknow assimilation + standing adoption gate

Lane: `/home/vgpnk/Projects/shokunin/kengaku-shokunin`, branch `master`, HEAD
**`5fd54a41c34f1275cf47d50bf1fbecde61c4e6ca`** (pushed, ahead 0 / behind 0). Baseline
`1f3b0f1ec41ec297130e8944ff97968d32324632`; frozen prereg `plans/round-29-attempt2-claims.md`,
freeze commit `8c14a5dcd15ac364a352d544660c69f521c3a6af`.

Attempt 1 of round 29 landed 2026-10-21 (`31934e5`..`1f3b0f1`, fleet report `2ae9ba1c` + erratum
`17d58281`) and was then held by the operator on source-history/credential-copy disposition. Run 6
re-dispatched round 29; this attempt carries two new claims and never re-claims the
generated-config projection. **Inherited state:** no uncommitted lane-authored leftovers existed at
start (`jj-lane.sh state` → tracked 0 / untracked 0); attempt-1's committed evidence was re-used only
as historical context and is cited, never re-scored. Files this lane did not author
(`round-29-source-copy-containment.md`, the operator lessons) were left untouched.

## Work performed

**Declared claims (2).** C1 — shokuknow assimilation on the **coverage** axis (the lane's lowest
non-retired axis, tied at 7): adopt one knowledge entry from the lane's campaign package under one
theme, with every cited source re-opened this round. C2 — **operability**, capability acquisition: a
standing source-adoption gate plus the one-command counter an adoption round needs. Neither claim
moves the generated-config work of attempt 1.

- **C1 built and landed.** `corpus/knowledge/benchmark-task-validity-checklist.md` (S077, S078,
  S079, S080, S090): a ten-axis checklist where each axis names a published artefact and its locus,
  read from four pinned primary documents. Sources re-opened 2026-10-25 by five scout seats and six
  independent reviewer seats; all digests reproduced.
  Evidence: `corpus/knowledge/benchmark-task-validity-checklist.md:1-8`; `.ufo/waves/round-29/attempt2/build/R29a2SrcS077.md`,
  `…SrcS078.md`, `…SrcS079.md`, `…SrcS080.md`, `…SrcS090.md`, `…RevQuoteS077.md`, `…RevQuoteS078.md`,
  `…RevQuoteS079.md`, `…RevQuoteS080.md`, `…RevQuoteS090.md`, `…SrcIntegrity.md`.
- **C1 rows appended.** S077–S080 and S090 enter `corpus/SOURCES.md` as `mined` with
  `used-by corpus/knowledge/benchmark-task-validity-checklist.md`, `opened=2026-10-25`,
  `recheck=180d`; S090 enters tier **A** rather than the package's B (a first-party maintainer
  statement is tier A, and the package's "no visible date" reason is page-scoped — the publisher's
  news index dates the post 2025-11-07). Evidence: `corpus/SOURCES.md:100-104`;
  `.ufo/waves/round-29/attempt2/build/R29a2RevQuoteS090.md`.
- **C1 counts re-derived, not copied.** The package said "92 top-level task directories" (92 root
  entries = 89 dirs + 3 files) and "109 task directories" (109 entries = 108 dirs + `task_conflict.json`).
  Both corrected with their commands in-entry. Evidence:
  `corpus/knowledge/benchmark-task-validity-checklist.md` §Counts; `…RevQuoteS079.md` F1/F4,
  `…RevQuoteS080.md` F3, `…SrcIntegrity.md` R1/R2.
- **C1 prior art priced; no novelty credit taken.** A prior-art scout opened the Agentic Benchmark
  Checklist (arXiv 2507.02825) and judged the entry **INCREMENTAL**; the entry now states what it
  adds (the per-benchmark observability table) and what it does not. S091 was opened and appended as
  the pricing row. Evidence: `corpus/lessons/round-29.md` §Attempt 2 §Prior-art;
  `corpus/knowledge/benchmark-task-validity-checklist.md` §Prior art;
  `.ufo/waves/round-29/attempt2/build/R29a2PriorArt.md`.
- **C2 tool landed.** `plans/sources_adopt.py` — id collisions under the census's own 0–3-space
  anchor, staged-row schema (11 cells, escaped pipe, status, recheck), prose-`recheck` normalization
  with the stripped prose reported, `used-by` projection, strict-by-default refusal plus an explicit
  `--scope-to-admit` for a targeted append. `plans/adoption_check.py` — the frozen C1 counter.
  Evidence: `plans/sources_adopt.py`; `plans/adoption_check.py`;
  `corpus/evidence/round29-attempt2/gate-selftest.txt`.
- **C2 demonstrated against the real package, both modes.** Strict: `registry=82 staged=173
  collisions=6 malformed=2 duplicates=0 defects=167 prose=167`, exit 3 (the package is stale relative
  to what landed and carries S093/S101 escaped-pipe rows). Targeted on the pre-append registry: exit 0,
  five-row block. Evidence: `corpus/evidence/round29-attempt2/gate-strict.txt`, `gate-scoped.txt`.
- **Register quarantine slice hand-checked (2 rows).** `kengaku round2 S091` → **quote-present**, the
  register's "quote" being a `- Command:` line lifted from the lane's own staging file (extraction
  artifact, not fabrication; real anchor at byte 43351). `kengaku round3 S105` → **quote-present**;
  the quoted Japanese text is METI's WAF error shell returned to a bare client, and the row's hold-out
  quote is present in the 200 snapshot. Evidence: `…/build/R29a2QuarS091.md`, `…R29a2QuarS105.md`;
  `corpus/lessons/round-29.md` §Attempt 2 Gate.
- **Three staged entries rejected on property, with flips** (card design-vs-amendment; judge threshold
  already held in-lane; grader semantics generalised from one task plus a malformed row). Evidence:
  `corpus/lessons/round-29.md` §Attempt 2 §Rejected candidates; `…/build/R29a2RejectScan.md`.
- **`considerthese` mined, one proposal recorded (not implemented).** `considerthese/2026-10-21.md:44-49`
  (seat-yield ledger) is the one still-unimplemented proposal cheapest to ground; the scout measured
  its motivating gap (first-pass yield 1/179 in r25, 11/125 in r26) and confirmed it is absent
  (`test -e .ufo/waves/yield.tsv` → exit 1). Landed as a QUALITY criterion rather than an
  implementation, because the round's claim slots were spent. Evidence: `corpus/QUALITY.md` Q19;
  `…/build/R29a2Considerthese.md`.
- **Waves.** One 36-seat v1 wave (`kengaku-r29a2-build`, band 32–64, policy
  `scripts/hyaku/ufo-wave-policy.json`, validated exit 0), roles scout 10 / reviewer 10 / scribe 3 /
  executor 3 / critic 3 / connector 2 / simplifier 2 / mutation-tester 1 / revenger 1 / sentinel 1 —
  14 attack seats (39%). One residual ordinary `task` call of 4 seats (3 reviewer, 1 critic) carried
  the post-repair checks; wave 2 was not dispatched because the wave yielded fewer than 32 further
  *distinct* attacks. L1 holds the canonical planner seat. **Round total 40 seats, 0 dead seats.**
  Evidence: `.ufo/waves/round-29/attempt2/{build-spec.json,build-dispatch.json,build-registry-record.txt}`,
  `build/swarm-registry.json`, `.ufo/waves/round-29/attempt2/build/*.md` (36 reports),
  `.ufo/waves/round-29/attempt2/residual/`.
- **Master coordination.** Every seat was read-only against production; the L1 is the only writer.
  Both seats that misrooted a report at the fleet root self-disclosed and remediated it the same
  minute; a post-hoc sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`, no pathspec;
  `find -maxdepth 3 -newermt "2026-10-25 03:30" -name "*kengaku*"` outside the lane) shows no kengaku
  round-29 byte at the fleet root. Evidence: `…/build/R29a2ScopeSentinel.md`, `…R29a2EntryDraft.md`,
  `…R29a2GateBlock.md`.
- **Safety.** The sentinel scanned the new bytes and 39/40 wave blobs for credential shapes: 0 hits.
  `shokuknow` was read only (no campaign tool run, no write, no fetch, no push); the fleet root,
  sibling lanes and `.ufo/state` were untouched. Evidence: `…/build/R29a2ScopeSentinel.md`.

## Landed changes

| Helper hash | Changes | LOG entry |
|---|---|---|
| `8c14a5dcd15ac364a352d544660c69f521c3a6af` | frozen claims, both tools, expectation file, do-nothing control receipt, real-package gate receipt | LOG §Round 29 attempt 2 |
| `8cf7b60650afadc9478426ae6bb40dc0d36ca45e` | entry, S077–S090 rows, README index/coverage/frontier, PROVINCE, lesson §Attempt 2, SCORECARD §Round 29 attempt 2, evidence dir, wave evidence | LOG §Round 29 attempt 2 |
| `ff476d017107ec5ee3df735a16713c5967592b71` | prior-art row S091 + entry pricing, gate/counter repairs found by the wave, receipts | LOG §… first corrections batch |
| `4b82ff7acb73e548f9af71b25e3218ae4c839b88` | six entry widenings removed, `used-by` exactness, census-actually-ran gating, `round28_census.py` row anchor | LOG §… second corrections batch |
| `7bc2aaf5dd3ada995689a352479bb8f4bbbe9ff1` | Q5 source labels, a command per count, refreshed adopted receipts | LOG §Round 29 attempt 2 |
| `c88310fb7cb71e77e6ce6c56ea8a92609ad1244c` | dead gate code deleted after a simplifier proved it behaviour-neutral | LOG §Round 29 attempt 2 |
| `5fd54a41c34f1275cf47d50bf1fbecde61c4e6ca` | `corpus/QUALITY.md` Q19 (seat-yield obligation) and `.ufo/waves/yield.tsv` with the round-29 rows | `corpus/QUALITY.md` Q19; `…/build/R29a2Considerthese.md` |

Every change is motivated in `LOG.md` §"Round 29 attempt 2" (including both appended correction
batches) and in `corpus/lessons/round-29.md` §"Attempt 2" (M92–M103, Gate, rejected candidates,
sources opened).

## Before → after measurements

**C1 — assimilation (coverage axis).** Counting command, run at the frozen baseline and again on
`c88310fb` / `5fd54a41` (no counted byte changed between them).

```
python3 plans/adoption_check.py --expect .ufo/waves/round-29/attempt2/adoption-expect.json --census
```

- **Before (control, committed at freeze `8c14a5d`):** `entries=0 indexed=0 cited_rows=0
  rows_present=0 rows_mined=0 usedby_ok=0 census=skipped` — exit 1
  (`corpus/evidence/round29-attempt2/control-nothing.txt`, `.ufo/waves/round-29/attempt2/control.nothing.txt`).
- **After:** `entries=1 indexed=1 cited_rows=5 rows_present=5 rows_mined=5 usedby_ok=1 census=ok` — exit 0
  (`corpus/evidence/round29-attempt2/adoption-measured.txt`), reproduced byte-for-byte by an
  independent residual reviewer (`cmp` exit 0, sha256 `810c54e0…f76d1cb`).
- **Supporting counts, same commit:** registry rows 76 → **82** (S077–S080, S090, S091); tiers
  A 70 → **76**, B 4, C 2 (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` → 82);
  knowledge files 37 → **38** and index rows 37 → **38**; fleet census exit 0 at both ends
  (`corpus/evidence/round29-attempt2/census-before.txt`, `census-after.txt`, 14 pre-existing W04
  duplicate-URL warnings retained).

**C2 — adoption gate (operability axis).**

```
python3 plans/sources_adopt.py --selftest
```

- **Before:** `git cat-file -e 1f3b0f1ec41ec297130e8944ff97968d32324632:plans/sources_adopt.py` → exit 128
  (absent; no baseline script carries the logic).
- **After:** `SELFTEST cases=10 failed=0` exit 0 (`corpus/evidence/round29-attempt2/gate-selftest.txt`);
  strict package run `collisions=6 malformed=2 defects=167 prose=167` exit 3 (`gate-strict.txt`);
  targeted run exit 0 with a five-row block (`gate-scoped.txt`).
- **Kill evidence:** sixteen mutants over the round; the four that survived an earlier revision
  (`no-recheck-normalize`, `twelve-cell-accepted`, `anchor-column-zero`, `drop-dupe-check`) all die on
  the landed bytes (re-run by the L1; case names in
  `.ufo/waves/round-29/attempt2/build/R29a2FixtureMutations.md`, `…R29a2GateAudit.md`).
- **Gaming paths closed:** a 3-of-5 entry and a 1-of-5 `used-by` linkage each exit 1
  (`…R29a2SimpCheck.md`, `…R29a2CounterAudit.md`, `…R29a2CritClaimC1.md`); `…-checklist.md.bak` exits 1.

**Axis verdicts.** C1: coverage **7 → 7 held** — the round moves a named frontier bullet from
unopened lead to an admitted checklist, but the canonical coverage number stays capped by the open
round-25 L0 and this entry does not move it. C2: operability **8 → 8 held**, one capability row
added. No axis is claimed to rise; none is harmed (see the re-run gates below).

**No-harm re-runs on the landed tree.** `python3 grader.py` → `CHECKS n=733 mismatches=0
errata_pinned=1`, `VERDICT: PASS`, exit 0; `python3 plans/round28_census.py --revision 6baa3090…` →
`rows 82`, exit 0; `python3 plans/config_projection.py --summary` → `TOTAL findings=0`, exit 0; fleet
census exit 0. A revenger seat reproduced all four at base and at the landed tip with byte-identical
grader/projection output (`…/build/R29a2Regression.md`,
`corpus/evidence/round29-attempt2/round28-census-after.txt`).

**Claim terms as implemented (disclosed).** C2 clause 3 as frozen said a prose `recheck` normalizes to
the *frozen access date*; the landed tool writes `180d` and stamps `opened=2026-10-25`, because the
frozen value made every adopted row 0 days overdue (caught by the regression seat). The mechanism
(normalize, report the stripped prose) is unchanged; the value differs and is recorded in
`LOG.md` §corrections batch 1 and `plans/round-29-attempt2-claims.md` §Scope clarification. C2 clause 4
is implemented as a strict default refusal with an opt-in `--scope-to-admit`, disclosed in the same
place. The closure should rule on both.

## Sources & frontier

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku
```

Run at round start and at round end; **both exit 0**. Outputs: `corpus/evidence/round29-attempt2/census-before.txt`
(14 W04 + `ok`) → `census-after.txt` (the same 14 W04 + `ok`; no new warning class).

- **Rows before → after:** 76 → **82** (six added: S077, S078, S079, S080, S090, S091). Malformed 0 → 0.
  Tiers A 70 → 76, B 4 → 4, C 2 → 2. Status mined 57 → 70 / queued 8 / rejected 4 (counts over 82).
- **Rows added by tier:** 6 tier-A. **Rows touched old→new:** none — no existing row's status,
  recheck or used-by changed this attempt (S077–S091 never existed before this round).
- **Frontier rows advanced:** `corpus/README.md` §Frontier bullet 1 ("Agentic benchmark task-spec
  audits") — the `primary specs` half of its "unopened leads" phrase is discharged for Terminal-Bench
  2.0, SWE-bench Pro V2 and Toolathlon-Verified (`corpus/README.md:271`); scoring code was not read and
  stays open. A new coverage-map bullet for "Benchmark task-validity instruments" was added
  (`corpus/README.md:249`). Contamination-transparency cards, runtime task validity, hosted judges,
  deployment configs and model performance remain open.
- **Assimilation:** `merge/kengaku` → **1 entry + 6 rows adopted** (S077–S080, S090 cited by the
  entry; S091 the prior-art pricing row). **3 entries rejected on property with flip conditions**
  (card design-vs-amendment; judge thresholds already held; grader semantics generalised from one
  task). **168 staged rows and 64 staged entries not appended** — CORPUS rule 4: a row no admitted
  entry cites is not appended. Id collision guard: registry ids vs staged ids → **0 collisions**
  (`collisions` empty for S077+); the guard was proven failure-capable on a 1-space-indented fixture
  (case `collision-one-space`) and on the 4-space boundary (case `four-space-not-a-row`).
- **Re-grounding:** every new row carries this lane's 2026-10-25 access date and a located ≤25-word
  quote inside the lesson's Gate table; the campaign's `opened`/quote values were never reused.

## Trend verdicts

- **expansion: improved** — one admitted entry on frontier ground the lane did not hold, six
  source rows, a new coverage-map row and a frontier discharge. Capped surfaces unchanged and stated.
- **quality: improved** — a ten-case gate with four killed survivors and three closed gaming paths,
  plus eight defects the wave found in this round's own work and repaired (two count units, one
  non-verbatim quote, six entry widenings, a stale receipt, a silently under-counting census anchor).
  Bounded, not exhaustive: the gate has no quote/word validation, and the campaign package still
  cannot be appended wholesale.
- **discernment: unchanged** — same-lane attack seats caught a level of defect the earlier rounds'
  self-checks did not (a frozen target the counter itself violated; an entry quote that was not a
  byte substring; a register row whose "absent" verdict was an extraction artifact). But closure is
  still author-side: no outside admit/reject spot-check exists for this attempt.

## SHONEN

- [~] **Real decision tables / error patterns / checklists / cited sources** — the adopted entry is a
  ten-axis checklist with a locus per axis, and `plans/sources_adopt.py` carries the adoption decision
  rules; no outside promotion verifier is claimed.
- [~] **End-to-end domain task executed and logged** — one entry adopted end-to-end (open → locate →
  draft → admit → index → register → gate), logged in `LOG.md` §Round 29 attempt 2 with the receipts
  in `corpus/evidence/round29-attempt2/`.
- [~] **Executable without oral context** — `--selftest`, `--check-package`, `--scope-to-admit`,
  `--adoption_check --census`, documented exit codes (0/3/4/5) and committed receipts; ten cases and
  sixteen mutants observed, not universal coverage.
- [~] **No cross-domain bleed, PROVINCE accurate** — the entry is a publish-document synthesis with
  five route-outs named (kama, chousa, kake, kotoba, kumitate) and deployment/runtime/judge/contamination
  left explicitly open (`PROVINCE.md` §Round29 attempt-2; `…/build/R29a2RevEntryScope.md`).

## Report extras

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open. Only round 29 was
  worked; no round 30 was started or claimed.
- **Tool installs:** none by the L1. One seat reinstalled `coverage` via `uv tool install coverage
  --force` → 7.17.0 (its uv-tool target had vanished mid-audit) to measure deletion coverage; no
  pacman transaction was attempted by any seat (the host-wide pause was respected).
- **L0 questions:** none new. The two inherited round-25 questions (coverage cap, novelty conversion)
  remain open and C1 does not convert either. No operator decision blocked this round.
- **Wave accounting:** 36-seat v1 build wave + 4-seat residual call = 40 seats; 0 dead; no seat
  replaced; every `task` dispatch carried the validator's `taskCall` unchanged; routing left to the
  operator's role map (no `model` parameter passed anywhere).
- **Yield ledger (Q19, landed this round):** `.ufo/waves/yield.tsv` now carries one row per seat for
  round 29 — 40 rows, **27 of 40 caused a landed correction, supersede or verdict change**
  (`awk -F'\t' '$1==29 && $5=="yes"' .ufo/waves/yield.tsv | wc -l` → 27), against 1/179 in round 25
  and 11/125 in round 26. `corpus/QUALITY.md` Q19 makes the ledger a per-round obligation.
- **Honest limits:** this is an author-side measurement; independent non-author closure decides
  admission. Two claim-term deviations are disclosed above for that ruling.

## Appendix A — attempt-1 filed report (2026-10-21), preserved verbatim

The earlier attempt of this round filed its report at this same path; run 6 re-dispatched round 29 and
this attempt replaces it as the round report. The attempt-1 bytes are reproduced below verbatim from
fleet commit `17d58281` (`git show 17d58281:.ufo/reports/round-29/kengaku.md`), so no filed evidence is
lost by the replacement. Attempt 1 is history: it was held on source-history/credential-copy
disposition and is not re-scored here.

# Kengaku round29 — generated-config projection, crash-recovered

## Work performed

**Declared claim C1 — capability acquisition, lowest legacy novelty7 → canonical coverage/constructs:**
0 dedicated generated-config audits at baseline → source-faithful offline projection of all812 raw tasks
under3 frozen synthetic profiles (2436 task/profile records), occurrence/field provenance and output-index
mapping, with separately authored oracle agreement. **Measured improvement; novelty7 and calibration8 held.**
No new method, actual deployment config, runtime/task validity, model-performance or contamination claim.

- Recovered held claim29/attempt1 without redispatch or starting30. Baseline
  `ed26bdf5d924755697cd6812129be2fa441c42a3`; inherited prereg/frozen inputs
  `31934e5660f1814326c6472eefdfa0c41e642a2f`. Authenticated manifest/generator/raw/profile pins before reuse.
- Reused41 build reports; all3 production executors died without code. Replacement coordinator authored
  `plans/config_projection.py`, adopting3 seat-authored hand fixtures byte-exact. Independent9 error/domain
  cases and portable oracle were later adopted byte-exact from FOracleLeaf/FOracleText.
  Evidence: `plans/fixtures/r29/`, `.ufo/waves/round-29/build-dead-seats.json`, lesson M87–M91.
- One fresh77-seat post-crash falsification attacked integrated artifacts, not a one-for-one replacement
  of dead seats. Four oracle reports and the portable oracle compare2436objects,4248changed leaves and
 1435provenance records. Exact-v5 source/number re-reads by FEntrySources and FEntryNumbers returned PASS.
- Repaired actual falsification findings: order/control blind spots, normalization/category survivors,
  narrowed URL-template and forced-zero-exit survivors, permissive AST guard, optimized Python disabling
  assertions, child/temp environment isolation, key-order emission, and missing persisted error cases.
  `plans/fixtures/r29/mutation_witness.py` retains exact patches;31 selftest cases and12/12 mutants pass.
- Candidate v1–v5 and earlier red/PARTIAL reports remain historical. S075/S076 correct Python locator
  rendering/load–loads inheritance. No observed count changed to make a gate pass.
- Scope/supporting artifacts, source links, index/coverage, province and gate registry updated together;
  `corpus/QUALITY.md` Q18 mines the unscorable-F3 lesson. Outside round closure remains separate.

## Landed changes

Every change is motivated in `LOG.md` Round29 and `corpus/lessons/round-29.md`.

| Landed helper hash | Changes |
|---|---|
| `31934e5660f1814326c6472eefdfa0c41e642a2f` (inherited) | frozen claim/input/profile package and baseline receipts |
| `b98dcf317b6c50179ac5c70b6ba3dacc7e2976fe` | integrated tool, adopted hand fixtures, S070–S073 and build evidence |
| `56fd949a6478342531e61f4feecb4a685d831640` | candidate-v1 freeze |
| `dbcecded4a04247cf6fd12919327af973da10bdd` | first falsify repairs, S074, candidate-v2 and returned evidence |
| `6baa3090b6cf2d50e56b94b806a69f41220081df` | exact-v5 knowledge admission, final controls/oracle/cases, S075/S076, final reports and safety cleanup |
| `6a2c2df788a4fdb216dd5790f9ae6dd326169f47` | actual measured-revision receipts and trial/landed tree-equality proof |

**Final lane:** master local=remote=`6a2c2df788a4fdb216dd5790f9ae6dd326169f47`, ahead0/behind0,
tracked0/untracked0 (helper state output). Measured admission is6baa3090…, not the later receipt commit.

**Inherited/discarded:**41 reports plus3 independent fixtures reverified/reused; dead executors supplied no
implementation. Empty nested clones and ignored bytecode discarded; committed research evidence retained.
A dead executor left local branch `round29/R29ExecCore` at31934e5; disclosed and not mutated. No r28
outside-spotcheck/operator lesson file existed in the lane to edit. Fleet misroot sweep found no own files;
other lanes/runtime changes were left untouched.

**Safety conformance incident:** FRevEnumerate's broad downloaded source scratch accidentally included
upstream account-default/endpoint copies in an earlier helper commit. FSentinelSecrets identified5paths;
all5 were removed before admission and its final bounded absence recheck is PASS. No values are repeated
here. **Historical Git objects were not purged; final-tree cleanup is not historical-material compliance.**
See `credential-copy-removal.txt` and the appended sentinel report. No actual auth-state, cookies or host
credential values were read. This incident remains disclosed for outside closure, not waived by the PASS.

## Before → after measurements

**C1, measured on admission6baa3090…:**

- Before: `git cat-file -e ed26bdf5d924755697cd6812129be2fa441c42a3:plans/config_projection.py` → absent,
  exit128 (`corpus/evidence/round29-calibration/instrument-before.txt`).
- After: `python3 plans/config_projection.py --summary` →812tasks/812IDs/3profiles/**2436projections**,
 1435occurrences/1416changed string leaves per profile,1355URL-path/61non-URL-path leaves,0remaining six
  tokens, index==task_id812/812, findings0/exit0. WIKIPEDIA0 is a population no-op, not an exclusion.
- `python3 plans/config_projection.py --selftest` →31cases, exit0; includes9 separately authored persisted
  domain/error cases. `python3 plans/fixtures/r29/mutation_witness.py` →12/12killed, exit0.
- `python3 plans/config_projection.py --json > <capture>` then
  `python3 plans/fixtures/r29/projection_oracle.py --root <lane> --diff <capture>` →DISAGREEMENTS0,
 2436objects/12180scalar comparisons/4248leaves/1435provenance rows, oracle findings[], exit0.
  JSON SHA256 `a4fb5d6dd9b7d509be55ae9d5c779dccaf9e29a7727447a30c568a174579d851`.
- `python3 plans/gate_timing_check.py --lesson corpus/lessons/round-29.md --commit 6baa3090b6cf2d50e56b94b806a69f41220081df`
  →admissions1/passed1/failed0/77reports, exit0. Separate `admission_check.py --commit <same>` →all
  exact-candidate/code/final-PASS/digest checks true, exit0.
- The pre-landing isolated trial and landed admission share **tree33d75ccd8be05c941045f00e05b12ce9ee0cd4af**.
  Trial88d687df… passed both checks before the lane helper moved master; actual-tree receipts followed.
  This is exact-tree timing evidence, not a structural check substituted for endorsement.
- Preservation: r28 audit812/5/27/16/651 and67tests; reference diagnostic13/35/12/0 and15tests; all exit0.
  `python3 plans/round28_census.py --revision 6baa3090b6cf2d50e56b94b806a69f41220081df` →source76/malformed0,
  knowledge/index37/37, historical329/318MATCH/0MISMATCH/6SUPERSEDED/5offline; P4 remains48MATCH/
 1SUPERSEDED/2offline. OOP32 is additive disclosure, not newly proven assertions.

Receipts: `corpus/evidence/round29-calibration/{final-*,actual-*,trial-*,receipt-generations.json}`.
Build/repair receipts retain earlier20/28case and3/10mutant observations; the generation manifest names
supersession explicitly. Shell receipts append `exit=N` after stdout. Capability is improved; scores held.
Forecasts F1/F2/F4/F5 true, F3unscorable under ambiguous frozen wording; **no calibration credit**.

## Sources & frontier

Command at start and end:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`.
Both exit0. Exact outputs: `sources-before.txt` (11W04+ok) → `sources-after.txt` (14W04+ok).
Source rows69→76; malformed0→0; tiers A63→70/B4→4/C2→2; mined57→64/queued8→8/rejected4→4.

Added S070generator, S071JSON docs, S072workflow, S073prepare boundary, S074BrowserGym prior practice,
S075stable-section and S076load/loads locator corrections: **7tier-A scoped rows,0new rejections**.
S070–S074 entered queued/— then mined/lesson+entry use; S075/S076 enter mined/lesson+entry use.
S068 gains the new knowledge path only; existing status/recheck and other immutable cells unchanged.
Every new URL/date/≤25-word located quote and mutable-cell old→new is in the lesson Gate. A bounded
search log is also in `corpus/SOURCES.md`; no global absence/new-method claim.

Frontier moves only for offline source-faithful projection under synthetic values. Actual deployment
configs, runtime validity, hosted judges, contamination and other named benchmark specifications remain open.

## Trend verdicts

- **expansion: improved** — one admitted entry and capability on previously unheld generated-config
  observability; knowledge/index36→37, explicit coverage-map/province append and opened source links.
- **quality: improved**, with the safety conformance incident above explicitly retained — stronger tests,
  scope/locator corrections, unchanged r28 instruments and exact-byte re-reads; no false v1/v2 claim left
  as current authority. Current controls are bounded, not exhaustive mutation coverage.
- **discernment: unchanged** — author-side attacks caught defects and Q18 is grounded, but outside admit/
  reject spot-check is pending. Same-lane seats do not supply independent round closure.

## SHONEN

- [~] Real decision tables/error patterns/checklists/cited sources — SKILL registry/workflow, new knowledge
  decision rule, lesson M87–M91. No outside promotion verifier claimed.
- [~] End-to-end domain task executed/logged —812×3 actual pinned-spec projections, independent comparison,
  LOG Round29 and final-oracle receipt.
- [~] Executable without oral context — `--root`/summary/JSON/selftest, portable oracle, persisted mutation
  witness and documented exits;31cases/12mutants observed, not universal coverage.
- [~] No cross-domain bleed/province accurate — FConnectSiblings and appended PROVINCE boundary;
  no deployment/serving ownership absorbed.

### Waves, deaths, tools and remaining boundaries

- Inherited build64: executor3/scout29/reviewer8/critic8/revenger4/mutation4/connector2/scribe2/simplifier4.
- Fresh post-crash falsify77: executor8/scout31/reviewer14/critic10/mutation4/revenger4/sentinel2/
  connector2/simplifier2. L1 holds planner; total141≤200; no dead-seat replacements. Later rechecks
  continued the same registered identities, not additional seats. Actual captured routes retained;
  no explicit model parameter or routing change.
- Dead build23 (no report): R29ExecCore, R29ExecOracle, R29ExecCases, R29Task044, R29Task681,
  R29Task791, R29Task556, R29Task007, R29TokenMap, R29ReviewProfileSchema, R29ReviewProvenance,
  R29ReviewLeafIdentity, R29ReviewIndexMapping, R29ReviewEscaping, R29ReviewGlobalFields,
  R29ReviewMetricUnits, R29ReviewPreservation, R29CritPriorArt, R29CritByteIdentity,
  R29ReverseDeadField247, R29ReverseCascade, R29ReversePriorCorpus, R29MutEscapes.
  Cause: host session SIGHUP2026-10-21T16:10:51Z; no provider-death error inferred. Fresh77 reports returned,
 0dead. Cap refusals spawned0: initial build call and first post-crash call; latter retried same payload
  after180s and spawned77. Receipts retain exact `Background job limit reached (100)` text.
- Install record: FReviewDeterminism installed **CPython3.9.25 and3.8.20**, uv/python-build-standalone,
  official Astral channel, to probe ast.unparse's version floor. Other3.10–3.15 interpreters preinstalled.
  No pacman/update/service transaction. Final31-case selftest exercised on CPython3.9–3.15.
- /tmp ENOSPC interrupted one L1 test, preserved as incident; own stale scratch removed, rerun passed.
  Parent subsequently reclaimed shared stale scratch. Own temporary trial/heavy scratch is removed after
  copying evidence into the lane. No other lane's scratch touched.
- **Stale-lane:** respawn-per-round; only held r29 was worked. No r30/claim advance/dispatch call.
- **L0:** the2 inherited round25 coverage-cap/novelty-conversion questions remain; no new L0 question.
  No outside admission or history-purge authority claimed. Separate non-author closure decides admission.

## Erratum — compressed copied source remained after the five-path cleanup (2026-10-21)

This appends to, rather than rewrites, the filed report. Its original 11811-byte prefix has
SHA-256 `906b628006ce51fd195c88a8541c87c586a78df546669c123e1829d2cdef705b`.

The safety discussion at lines52–57 described a bounded absence check over five loose paths.
It did **not** establish that their material was absent from every carrier. Independent non-author
review found that the baseline `6a2c2df788a4fdb216dd5790f9ae6dd326169f47` still contained
`.ufo/waves/round-29/scratch/falsify/FCritNovelty/fetch/libwebarena-0.0.5-py3-none-any.whl`.
Its member `webarena/browser_env/env_config.py` is byte-identical, by Git blob identity
`81cf52de7d998c90abb3741416e2c8ab9b434758`, to the removed flagged module. The archive itself
has SHA-256 `5cfdf8abc2b40cc4442905a29af1c45c5fd0ed57bbfe8e3a6421a2e53cb6cb1b` (116645 bytes).
No credential literals or private endpoints are reproduced here; validity was not tested.

The orchestrator integrated current-tree containment through the lane helper:
**landed `1f3b0f1ec41ec297130e8944ff97968d32324632`**. Exactly the known copied wheel was
removed, with an appended LOG correction, a sanitized
`corpus/lessons/round-29-source-copy-containment.md`, and its corpus index row.
An isolated writer prepared the change; a separate read-only metadata reviewer checked identity,
dependency scope and citation effects; the parent integrated it.

Actual committed-object smoke: the wheel exists at the old baseline (`git cat-file -e` exit0)
and is absent at the containment commit (exit128). `plans/config_projection.py` and the canonical
round28 task-raw fixture retain identical Git blob ids across that change. No package, lane gate,
selftest, mutant or oracle was executed to claim a broader pass. The fetch receipt is retained
as a historical fetch record, not a current presence claim.

This is **known-artifact tip containment only**. Git history still retains the wheel and module;
other worktrees, caches, ignored/untracked material and unexamined carrier formats are not certified.
No history rewrite, force-push, rotation, revocation, global-clean statement, outside admission or
new score is claimed. Original projection measurements remain pinned to their original revision,
not re-credited as a result of this removal. Kengaku's safety/history-disposition hold and the
new operator question remain open; the earlier “no new L0 question” sentence is superseded.
