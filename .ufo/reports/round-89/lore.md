# fleet report — lore r89 (round-89, world-bible lane)

Lane: `lore-shokunin` · Repo HEAD measured: `1b09f3ff8016b26a2259e086f673d0112f4f54e5` (`1b09f3f`).
Baseline: `51b286b5a1e503e6e6ace1f8da0bd606a3c10d94` (`51b286b`, r88 closure).
Wave: 32 work seats (`.ufo/waves/round-89/`; 33 `.md` reports + 27 `patches/`) + a follow-up
judging wave (`.ufo/waves/round-89/followup/`). That wave was still landing artifacts while this
report was drafted; **snapshot cutoff for this report: `2026-10-17T04:37:54-03:00`, 62 artifacts,
30 seat tags** (JAXIS, JCAL2/JCAL4, H4, Q1, W1, SE2 and the final P2/P3 revisions landed after the
first read pass and are folded in at their cutoff revisions). Every measurement below is taken on
the delivered tree at `1b09f3f` — never on intent, and never on a scratch patch. Scratch was used
for probes/controls only (this seat's scratch: `/tmp/P1-r89/`).
Tree state at measure (this seat): `git status --porcelain` → ` M l0-questions.md` (K1's authorized
append, uncommitted) and `?? .ufo/waves/round-89/followup/`; no other working-tree change
(`corpus/fixtures/__pycache__/` is absent). Protocol checks: #1 `2026-10-17T04:28:54-03:00` (36
artifacts), #2 `2026-10-17T04:30:36-03:00` (36), stabilization `04:35:29` (61), cutoff `04:37:54`
(62); HEAD `1b09f3f` at every check, no dependency outstanding.

**Axis verdicts: `PENDING-L1` — the setter of verdicts is L1.** The follow-up wave's own axis
synthesizer (`JAXIS.md`) recommends: **calibration improved (bounded)** (JCAL1/JCAL2/JCAL3/JCAL4/
JCAL5 + H3/H4 corroboration), **coverage improved (bounded)** (JCOV1–JCOV5 + JDEP4), and **depth
harmed (bounded)** on the documentation-parity surface (`D-D1` boundary-doc drift + governance
sub-cases), with the transition rule *"improved (bounded) if repairs R1–R3 land at closure"* and an
admission recommendation of **repair-then-admit** (alternative: admit with depth harmed recorded and
R1–R4 as first r90 items). JDEP1/JDEP3/JDEP4 read the *artifact* surface as improved; JDEP2 finds
one sub-case of each of R8/R9/R10 undecided. A trade anywhere is not an improvement — the candidate
harms below are recorded, not netted away.

## Work performed

Three claims were declared for round 89, one per owned axis (`.ufo/waves/round-89/wave-spec.md`):

- **C1 — calibration** (lowest-axis obligation): (i) durable fixtures pin the six unexercised
  first-cause branches (invalid tick, invalid `from_holder`, invalid `to_holder`, dangling
  `to_holder`, dangling `from_holder`, invalid `source_id`); (ii) valid-key multi-defect records emit
  the complete combined cause summary (precedence settled by naming ALL simultaneous latching
  causes); (iii) FN-2 qualifies chain-break findings when the expected holder identity is not
  uniquely resolvable, and FN-1 distinguishes "absent from the resolved index" from truly absent.
  Prior 149 tuples preserved except enumerable deltas, 0 exit changes.
- **C2 — coverage**: the r87 cluster reaches 22/22 under the D1 support rule by delivering four
  in-world source excerpts (`gate-witness`, `dune-register`, `shell-charter`, `tide-bell-tally`)
  supporting the 14 previously metadata-only facts; the ETCSL ledger row gains the
  `external-only / text not delivered` marker.
- **C3 — depth**: the D1 table gains R8 (rights-blocked element disposition), R9 (excerpt
  delivery-mode) and R10 (cross-cluster contradiction procedure), plus a durable R9 demo fixture and
  an R10 worked example.

Work items and evidence pointers:

- **C1 implementation + fixtures** — landed by `1b09f3f`: `corpus/fixtures/check_bible.py`
  (`git diff --numstat 51b286b..1b09f3f -- corpus/fixtures/check_bible.py` → `54 14`, 435 lines,
  sha256 `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`) plus eight
  cause-branch fixtures and the FN-2 pair. Implementation `X1.md` (+ `patches/X1-c1.patch`,
  `patches/X1-tuple-delta.json`); alternatives `X2.md`/`X3.md`; code scout `S1.md`; baseline
  reproducer `B3.md` (+ `patches/B3-before-state.json`); fixture authors `F1.md`/`F2.md`/`F3.md`
  (+ `patches/F{1,2}-cause-fixtures.patch`, `patches/F3-fn2-fixtures.patch`); critics `C5.md`/`C6.md`;
  independent delta predictor `C8.md` (+ `patches/C8-delta.json`); wording panel `E1.md`
  (+ `patches/E1-r89-wording.md`).
- **C2 excerpts + ledger marker** — landed by `1b09f3f`. Drafts `M1.md`/`M3.md`
  (+ `patches/M{1,3}-excerpts.patch`); synthesis + fact-to-source map `M4.md`
  (+ `patches/M4-verify.json`); ledger marker `M5.md` (+ `patches/M5-ledger-marker.patch`);
  support-sweep scout `S2.md` (+ `patches/S2-fact-map.json`); consistency scout `S4.md`;
  discipline critic `C7.md`; connector `K1.md`.
- **C3 R8–R10 rows + demos** — landed by `1b09f3f`. Row-set drafts `D1.md` (+ `patches/D1-rows.md`)
  and `D2.md` (+ `patches/D2-rows.md`); reviewer `R1.md` (D2's set only, do not merge D1);
  cross-check `T1.md`; demos `D3.md` (+ `patches/D3-r9-demos.patch`); scout `S3.md`
  (+ `patches/S3-r8-r10-sketches.md`).
- **Boundary / census / record** — baseline censuses `B1.md`/`B2.md` (+ `patches/B*-tuples.json`);
  sentinel `SE1.md`; clerk `W1.md`; scribe `W2.md`
  (+ `patches/W2-{log,scorecard,report}-r89.*`).
- **Follow-up judging** (`followup/`, 62 artifacts at cutoff) — axis synthesis: `JAXIS.md`
  (+ `JAXIS-verdicts.json`); calibration: `JCAL1.md` (+ `JCAL1-delta.json`), `JCAL2.md`
  (+ `JCAL2-probes.json`, adversarial), `JCAL3.md` (+ `JCAL3-fixtures.json`, fixtures + mutation
  matrix), `JCAL4.md` (+ `JCAL4-wording.json`, wording audit), `JCAL5.md`/`JCAL5-delta.json`
  (method-varied third census); harm sweeps: `H1.md` (+ `H1-census.json`), `H2.md`
  (+ `H2-delta.json`), `H3.md` (+ `H3-mutation-delivered.json`, `H3-r88-compare.json`), `H4.md`
  (+ `H4-replay.json`, live probes + lineage), `H5.md` (README audit); coverage: `JCOV1.md`
  (+ `JCOV1-probes.json`), `JCOV2.md`, `JCOV3.md` (+ `JCOV3-probes.json`), `JCOV4.md`, `JCOV5.md`
  (+ `JCOV5-probes.json`); depth: `JDEP1.md` (+ `JDEP1-receipts.json`), `JDEP2.md`
  (+ `JDEP2-probes.json`), `JDEP3.md` (+ `JDEP3-probes.json`), `JDEP4.md`
  (+ `JDEP4-evidence.json`); drift & repair proposals: `CB1.md` + `CB1-boundary-refresh.md`,
  `E1.md` + `E1-drift.json` + `E1-boundary-update-proposal.md`; connector/L0: `K1.md`
  (+ `K1-receipts.json`); debt/process/record: `Q1.md` + `Q1-r89-debt.json` (r89 debt census +
  r90 planner), `W1.md` + `W1-disposition.json` (r88-debt disposition verifier), `Q2.md`
  (methodology), `P2.md` + `P2-scorecard-r89.md` (SCORECARD drop-in), `P3.md` + `P3-log-r89.md`
  (append-ready LOG entry, finalization addendum 04:32), `P4-shonen.md`, `SE2.md` (+
  `SE2-snapshot.json`, terminal freeze); writer: `P1.md` + `P1-manifest-entry.json` +
  `P1-measurements.json` (this seat).

## Landed changes

- **C1 — `corpus/fixtures/check_bible.py` (+54/−14, sha256 `e2bb9639…e3556`)** and eleven new
  fixture dirs: `r89-c1-invalid-{tick,from-holder,to-holder,malformed-source-id}`,
  `r89-c1-multi-cause-valid`, `r89-f2-dangling-{from,to}`, `r89-f2-invalid-source-id`,
  `r89-fn2-{control,unresolved-chain-break}`, `r89-inspiration-paraphrase`. Commit **`1b09f3f`**.
  `V2.md` froze the revision: the delivered checker is byte-identical to `51b286b` +
  `patches/X1-c1.patch` (patch sha256 `8789dcb4…`), so no undocumented integrator amendment rides
  along; `JCAL1`, `JCAL3`, `H1` and `JCAL2` re-verified the same provenance.
- **C2 — four new excerpts in `corpus/fixtures/r87-myth-cluster/`**
  (`gate-witness-excerpt.md`, `dune-register-excerpt.md`, `shell-charter-excerpt.md`,
  `tide-bell-tally-excerpt.md`) and the ETCSL marker in `corpus/knowledge/reference-ledger.md`
  (`git diff --numstat` → `1 1`). Commit **`1b09f3f`**.
- **C3 — `corpus/knowledge/r88-sourced-inspiration-decision-table.md` (+17 lines: R8/R9/R10 rows +
  an integration-boundary note) and the new `corpus/knowledge/r89-cross-cluster-contradiction.md`
  (32 lines, prose)**. Commit **`1b09f3f`**. `JDEP2.md` shows by sequence ratio that the delivered
  rows are D2's text plus the integrator's Owner sentence; D1's name-identity guard was not carried.
- **Wave evidence — `.ufo/waves/round-89/` (32 seat reports + `wave-spec.md` + `patches/`)**.
  Commit **`1b09f3f`**; `git diff --name-only 51b286b 1b09f3f | sed 's#/.*##' | sort | uniq -c` →
  `76 corpus`, `60 .ufo` (136 files, +12330/−15). Single commit, sole parent `51b286b`; author =
  committer = `lore-shokunin <lore@shokunin.local>`.
- **Not committed (open for the integrator):**
  - **`l0-questions.md` round-89 line (K1)** — the authorized one-line append (4 → 5 lines, +1
    insertion only; `SE2` independently confirmed nothing else is modified), ` M` in the working
    tree; it corrects the r88 kotodama line's now-false "absent in both lanes" premise (the contract
    is tracked in kotodama-shokunin at `49ac1a5`, sha256 `e834f503…`,
    `contract_id kotodama-lore-adjacency` rev 1.0.0). `K1.md`'s final revision records "no *second*
    append"; `P3`'s finalization addendum corroborates.
  - **Follow-up judging artifacts** — `.ufo/waves/round-89/followup/` (62 artifacts) is untracked.
  - **Round record (LOG/SCORECARD)** — `git diff --name-only 51b286b 1b09f3f -- LOG.md SCORECARD.md
    SHONEN.md PROVINCE.md README.md l0-questions.md` → empty. Drafts only:
    `patches/W2-log-r89.proposal.md`, `patches/W2-scorecard-r89.proposal.md`, plus the follow-up
    `P3-log-r89.md` (append-ready LOG text) and `P2-scorecard-r89.md` (drop-in SCORECARD section,
    verdicts `PENDING-L1`).
- **No push:** `git rev-list --left-right --count origin/main...main` → `0 7` (7 ahead, 0 behind).

## Before → after measurements

All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin` unless noted. Baseline reference
artifact for the delta: the committed `patches/B1-tuples.json` (149 dirs; `JCAL1.md`, `JCAL5.md`
and `H2.md` independently re-derived `51b286b` and reproduce it exactly — 149 keys, 0 mismatching
rows).

### Census and delta (measurement, not an axis claim)

Census harness (`/tmp/P1-r89/census.py`): for every immediate `corpus/fixtures/*` dir, run
`python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>` with the repo root as cwd and record
`(exit, stdout, stderr)`. Paths are repo-root-relative (the r88 caveat: absolute paths make the five
`cannot load JSON` fixtures echo the argument and read as spurious deltas).

```
$ python3 /tmp/P1-r89/census.py . /tmp/P1-r89/deliv-tuples.json
root=. dirs=160 exits={0: 32, 1: 128} violations=399 stderr_nonempty=0

$ delta vs patches/B1-tuples.json (stdout sha256 + exit + violation count compared per path)
baseline dirs 149  delivered dirs 160
new 11 ['r89-c1-invalid-from-holder', 'r89-c1-invalid-tick', 'r89-c1-invalid-to-holder',
 'r89-c1-malformed-source-id', 'r89-c1-multi-cause-valid', 'r89-f2-dangling-from',
 'r89-f2-dangling-to', 'r89-f2-invalid-source-id', 'r89-fn2-control',
 'r89-fn2-unresolved-chain-break', 'r89-inspiration-paraphrase']
gone 0 []   changed 4 ['r87-probe-multi-invalid', 'r87-probe-record-and-chain',
 'r88-mixed-stop', 'r88-nonholder-stop']
exit_changes []   violation_count_changes_on_shared []
changed per-dir findings before->after: 5->5, 46->46, 6->6, 4->4
exit histogram base {0: 31, 1: 118} -> head {0: 32, 1: 128}
violation totals base/head 367 -> 399 ; new-dir finding sum = 32
```

- **Delta enumerable: `changed=4, new=11, missing=0, exit_changes=0, stderr_changes=0`.**
  160 dirs, `367 → 399` violation lines, 0 non-empty stderr both sides. 145 of the baseline tuples
  are byte-identical.
- **Every changed fixture kept its exact violation-line count** (5/46/6/4) and the four changed dirs
  contributed net zero findings; the identity `399 − 367 = 32` equals the summed finding count of
  the 11 new dirs (`3+4+3+3+4+4+4+4+1+2+0 = 32`). `JCAL1.md` classified all 12 changed lines
  mechanically: 2 combined-summary + 10 FN-1 wording + 0 qualification/footer/OTHER — all inside
  existing `first stop:` disclosure lines, no finding line touched.
- The same delta is reproduced independently seven ways (C8's predictor, H1, H2, JCAL1, JCAL3,
  JCAL5's method-varied run, this seat). `H2.md` adds the strongest preservation property: no shared
  path changed its violation count, exit, or stderr; `H4.md` shows the five r85 probes byte-identical
  at both revisions and the four changed dirs differ only in the FN-1 cause clause.

### C1 — calibration

**(i) The six claimed branches + `source_id`, each naming that cause as the first stop** (delivered
tree, verbatim tails; re-verified by this seat, `JCAL3.md`, `V2.md`, `P4-shonen.md`, `H4.md`):

| fixture | first-stop clause (delivered) | exit / findings |
|---|---|---|
| `r89-c1-invalid-tick` | `malformed record (invalid tick)` at `entities[3].provenance[1]` | 1 / 4 |
| `r89-c1-invalid-from-holder` | `malformed record (invalid from_holder)` at `entities[3].provenance[1]` | 1 / 3 |
| `r89-c1-invalid-to-holder` | `malformed record (invalid to_holder)` at `entities[3].provenance[1]` | 1 / 3 |
| `r89-c1-malformed-source-id` | `malformed record (invalid source_id)` at `entities[2].provenance[1]` | 1 / 3 |
| `r89-f2-dangling-to` | `holder reference to_holder 'r89-f2-missing-to' absent from raw entities and absent from the resolved index` | 1 / 4 |
| `r89-f2-dangling-from` | `holder reference from_holder 'r89-f2-missing-from' absent from raw entities and absent from the resolved index` | 1 / 4 |
| `r89-f2-invalid-source-id` | `source reference 'r89-f2-unknown-source' absent from raw sources and absent from the resolved index` | 1 / 4 |

Each fixture discloses at the arming record and at every later record of the item, and every line
carries `(input-structural finding, not sourced-canon)`. `JCAL3.md`'s 9-mutation matrix shows each of
the nine non-control fixtures is caught by at least one wrong-implementation mutation; 4 of the 8
cause-branch fixtures produce byte-identical output on the baseline checker (the branch already
worked — they pin the vocabulary and catch mutations, not the r89 delta itself).

**(ii) Valid-key multi-defect combined summary.** `python3 corpus/fixtures/check_bible.py
corpus/fixtures/r89-c1-multi-cause-valid` (exit 1, 4 findings) emits one joined first-stop clause:

```
VIOLATION: entities[2].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (invalid tick); ambiguous holder identity to_holder 'r89-c1-multi-cause-valid-ambiguous-holder' at entities[2].provenance[0]
```

and the changed tuple `r87-probe-multi-invalid` shows the r88 precedence bound closed on the
non-shape-cause pair (ambiguous holder + unknown source, both named):

```
- …; first stop: ambiguous holder identity from_holder 'vault' at entities[5].provenance[1]
+ …; first stop: ambiguous holder identity from_holder 'vault'; source reference 'ghost-source' absent from raw sources and absent from the resolved index at entities[5].provenance[1]
```

Scope bound (`JCAL1.md`, JAXIS C1 note): the `'; '`-joined summary already existed on the
*unexpected-field-set* branch (`r87-probe-shape-ambiguous`, `r88-shape-ambiguous-armed` are unchanged
and already combined); what C1(ii) adds is the *valid-key* branch (`check_bible.py:316`).
`JCAL2`'s probe p8 shows the valid-key summary is complete and in validation order.

**(iii) FN-1 / FN-2.** FN-1: all four changed tuples replace `unknown source '{id}'` /
`dangling holder {field} '{id}'` with the raw-vs-resolved wording above. FN-2 is a discriminating
pair (`V2.md`, `JCAL3.md`, `JCAL2.md`, `H2.md`):

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-fn2-control
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'f3-dup', got 'mira'      (exit 1, 1 finding)

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-fn2-unresolved-chain-break
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'      (exit 1, 2 findings)
```

`JCAL3.md` verified the pair's `entities.json` differ by exactly one inserted `f3-dup` row; `H2.md`
verified the qualification qualifies without suppressing. Two coverage bounds: FN-1's "present in
raw … but absent from the resolved index" branch has **zero durable fixtures** (JCAL1, JCAL3 Debt 3,
JCAL2 F1, H2 F6, H5 §5 — scratch-verified only), and the FN-2 clause is invisible to the 149-dir
manifest (only the two new fixtures exercise it).

**(iv) Candidate harm — nullable-holder misclassification (this seat's probe; JCAL2 Findings 1–3;
JCAL4 F3(a); E1 DR-5).** `holder_identity_detail` returns a detail string whenever
`raw_count != 1 or indexed_count != 1` (`check_bible.py:168-174`), so the schema-valid sentinel
`from_holder: null` (0 raw / 0 indexed) is reported as an unresolved identity. Two scratch fixtures
(`/tmp/P1-r89/probe-null-chain`, `probe-null-tick`):

```
$ python3 corpus/fixtures/check_bible.py /tmp/P1-r89/probe-null-chain
VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got None; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)

$ python3 corpus/fixtures/check_bible.py /tmp/P1-r89/probe-null-tick
VIOLATION: entities[3].provenance[1].tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index); provenance tick 0 must be greater than previous tick 0
VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: … (as above)
```

A **definite** chain break is labelled "possible … not a definite identity mismatch", and a
**definite** tick-order violation is qualified as identity-uncertain — though holder resolution is
not a cause of `tick <= previous_tick`. `JCAL2.md` independently reproduced this at three sites
(null sentinel; the pre-existing tick finding; the first-record case) and issues the rider: these are
*new losses of definiteness* relative to the baseline; under the fleet's trade rule they must be
recorded as a bounded harm and repaired in r90 (gate the qualifier on non-null ids and
identity-dependent comparisons only). `JCAL4.md` recommends recording the axis as improved (bounded)
with this regression named; `E1` DR-5 prescribes the one-line fix plus a durable fixture.

### C2 — coverage

**Anchor sweep (14 fixed-string queries, delivered tree, this seat's run).**

```
$ python3 (grep -nF -- '<anchor>' <delivered excerpt>) per S2 fact row
ANCHORS 14/14
E1 gate-witness-excerpt.md:5      E2 dune-register-excerpt.md:5    E3 dune-register-excerpt.md:6
E4 shell-charter-excerpt.md:7     E5 shell-charter-excerpt.md:8    E6 tide-bell-tally-excerpt.md:9
R1 shell-charter-excerpt.md:9     R2 shell-charter-excerpt.md:10   R3 shell-charter-excerpt.md:11
R4 dune-register-excerpt.md:7     T1 gate-witness-excerpt.md:6     T2 tide-bell-tally-excerpt.md:10
T3 gate-witness-excerpt.md:7      T4 dune-register-excerpt.md:8
```

**22/22 accounting.** The r87 cluster's D1 obligation set is 7 entity claims + 7 `first_appearance`
pointers + 4 relation edges + 4 timeline events = 22. Baseline: 0/14 delivered anchors
(`JCOV1.md`: `BASELINE 51b286b anchors=0/14`; 1/7 pointers with a delivered excerpt). Delivered:
14/14 anchors + 7/7 pointers + the hymn claim = **22/22 under the spec's grep-anchor rule**
(JCOV1's independent D1-rule replay: `D1-rule facts=22 supported=22 unsupported=0`; JCOV4, JAXIS
and JDEP4 reproduce). Caveat named by `H1.md` F1 and `JCOV1.md` D1: `M4-verify.json`'s own recorded
probe script returns **8/22 both before and after** (it tests literal `statement in prose`), so its
`after.facts_supported: 22` is a hand-composed 8 + 14 — true, but not reproducible from its own
command. Any closure text stating 22/22 must name the anchor rule explicitly.

- **Cluster replay:** `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster` →
  `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0 (JAXIS, JCOV2, JCOV4, H4
  reproduce). The structural checker does not read excerpts; it is not prose-support evidence.
- **`contradictions.json` untouched** — the Hara/Sen place disagreement is preserved and unresolved;
  JCOV2 confirms no excerpt anchor negates another fact (its one PASS pair is the recorded
  contradiction).
- **ETCSL marker:** `grep -n external-only corpus/knowledge/reference-ledger.md` → line 8 (ETCSL
  row) reads `external-only / text not delivered at lore; citation is a research lead with verified
  line locators, not delivered support. …` Ledger census: 7 table lines = header + separator +
  **5 data rows**, every row `ncols=4`, `empty_cells=0`; diff `1 1`; cells 0–2 byte-identical
  (three open questions stay separate; JCOV2/JCOV4).
- **PROVINCE refusals respected** (JCOV4): no canon without in-world citation, contradiction
  preserved, no rights conclusion, no real-world token in the four excerpts. Seam named: lore is now
  authoring in-world source prose to substantiate its own metadata claims (adjacent to kotodama's
  generative province; no violation).
- **Bounds:** no in-corpus claim-to-excerpt map for r87 (evidence lives only in
  `.ufo/waves/round-89/patches/{M4-verify,S2-fact-map}.json`); R9 delivery mode absent on the four
  new excerpts; `keeps_watch_with` is a relation type with no definition surface; JCOV2's three
  unextracted in-world detail lines should be re-scanned in a future extraction pass.

### C3 — depth

**Rows.** `corpus/knowledge/r88-sourced-inspiration-decision-table.md` census: 12 table lines =
header + separator + **10 data rows**, every row `ncols=6`, `empty_cells=0`;
`grep -c '^| R8 —\|^| R9 —\|^| R10 —'` → `3` (lines 22/23/24). R8 (rights-blocked element
materiality + disposition), R9 (delivery mode `verbatim` / `translation` / `paraphrase` /
`summary`; a paraphrase is not the source's own text) and R10 (cross-cluster contradiction register
procedure) each end their rule cell with an explicit owner: *"**Owner:** the lore lane applies this
row at integration; unresolved disputes are appended to `l0-questions.md` for the operator — the row
is an editorial screen, never a rights or canon determination."* A closure note scopes all three
prospectively, and the integration-boundary paragraph states R8 is not rights advice, R9's anchor
check is not fidelity evidence, and R10's register is manual until a corpus-wide validator exists.

**Render defect (JDEP1 D1, measured with a real GFM parser; P3 re-verified).** The R8–R10 block has
no header or delimiter row, so a GFM renderer emits the three rows as a paragraph of literal pipe
text — the rows are *not* in the rendered table. `V2.md`'s column-count check still passes (pipes
well-formed), so this is a rendering, not a syntax, defect. The header's sixth column still says
"r87 / round-88".

**R9 durable demo fixture** — `corpus/fixtures/r89-inspiration-paraphrase/`:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-inspiration-paraphrase
CLEAN: schema, citations, relations, timeline; 0 violations        [exit=0]
$ grep -nF -- 'moved to the west stair' corpus/fixtures/r89-inspiration-paraphrase/ash-ledger-excerpt.md
9:A modern paraphrase says that the keeper later summarized the ledger for the court: the tide-mark had been moved to the west stair.
```

The map's pointer (`ash-ledger-excerpt.md:9`) matches the anchor line; the excerpt declares
`**Delivery mode:** paraphrase`; the map's `R9 support result` cell reads `Fails: …`. JCOV3 audited
7/7 rule statements in README+map and confirmed the underlying source wording is genuinely
undelivered. JCOV3's scratch verbatim twin returns the identical `CLEAN` + identical anchor, so the
discrimination is declarative, not mechanical — the artifact states exactly that.

**R10 worked example** — `corpus/knowledge/r89-cross-cluster-contradiction.md` (new, 32 lines).
JCOV3 audited 17/17 R10-named elements; this seat verified the real pointers resolve
(`timeline.json#moon-basin-vow-gate-account.place_id` → `mother-tide-gate` via `gate-witness`;
`…#moon-basin-vow-dune-account.place_id` → `ash-dune-sanctuary` via `dune-register`), the second
cluster path is absent as the demo states, and the live register
(`corpus/knowledge/cross-cluster-contradictions.md`) is correctly absent. JDEP3: register-readiness
**improved**, register *operability* **unprovable-but-better** (no real second cluster shares a
referent with r87; r87's own Hara/Sen pair is correctly intra-cluster).

**Attack results (JDEP2 — three constructed cases, all `CLEAN` under the checker, so the rows carry
the whole burden):** R8 **uncovered** for the unrecorded-but-plausible influence case (every
disposition presupposes recorded material; the landed r87 ETCSL motif carries no marker and no named
disposition); R9 **uncovered** for a translation whose source version is unidentified (the
declaration clause is satisfiable while the eligibility clause fails); R10 **uncovered (partial)** —
the no-register-entry answer is covered, the required record for a dismissed name-overlap near-miss
is not (D1's name-identity guard is absent from the delivered row). JDEP2 issues D-JDEP2-1…6.

**Prospective scoping vs. this round's own work (named debt).** The R9 closure note says r87/r88
"are annotated at their next content touch", but the r87 cluster **was** content-touched this round
(four new excerpts, none declaring a mode) — JCOV4 D2, JCOV1 D4, P4 D2, H5 §6. Also JCOV3 D1: the R9
row never writes the fixture path `corpus/fixtures/r89-inspiration-paraphrase`; JDEP1 D5: the note's
"(named debt, r89 ledger)" points at a LOG entry that does not exist yet.

**Capabilities assessment (JDEP4): FOR** a second capabilities row, `in-world excerpt support
verification` — the sweep runs `facts=22 OK=22 not-OK=0 (pointers 7/7, hymn 1/1, anchored 14/14)` on
the delivered tree, 10/10 on the Maya cluster, and returns a negative verdict on the R9 paraphrase
where the checker is `CLEAN`. Preconditions: repair the structured `## Capabilities` table (still
`— none yet —`, while the r88 narrative claims row 1 entered) with both rows in one edit; put the
evidence command in the round report. Bounds: the r87 map is wave-resident, and the positive
delivery-mode path is unexercised.

### Documentation parity (measurement, and the round's candidate harm)

`corpus/knowledge/holder-assessment-boundary.md` (tracked blob `1a2f816b`, 492 lines) is the doc the
r87 fixture README names as "the current contract". The C1 change drifted it and it is **unrepaired
on the delivered tree**. Independent inventories: `CB1.md`/`CB1-boundary-refresh.md` (r89 revision:
drift items + full refresh draft), `E1.md` + `E1-drift.json` (DR-1…DR-15) +
`E1-boundary-update-proposal.md`, `H5.md`, `JCAL3.md` Debt 2, `JCAL2.md`, `H2.md` F5,
`P4-shonen.md` D3, `JAXIS` D-D1/D-D5. Measured surfaces:

- **Cause-table rows 9/10/13** still declare `dangling holder to_holder {id!r}`,
  `dangling holder from_holder {id!r}`, `unknown source {id!r}` — three retired strings
  (`:152-153`, `:156`; this seat re-confirmed).
- **Precedence claims** `:169` and `:219-225`: "names only the FIRST check … later causes are NOT
  appended … The only combined clause is the shape-invalid one" — falsified by the delivered
  `r89-c1-multi-cause-valid`.
- **Pasted receipts:** the doc's r85 probe block reproduces byte-for-byte on the delivered tree
  (`P4-shonen.md`, `E1.md`, `H4.md`), but its `r88-mixed-stop` / `r88-nonholder-stop` "delivered
  output" block (`:338-348`) still shows `first stop: unknown source '…'` — a replay on `1b09f3f`
  emits the FN-1 wording (this seat; H5 §4; H2 F5; JCAL3 Debt 2; JAXIS).
- **Shifted anchors:** every cited `:NNN` moved (H5 §3, E1 DR-9); `r87-probe-source-prefix/README.md:1`
  cites stale lines too.
- **Self-contradiction:** the doc's banner says `> **PROPOSAL — not applied.**` while the file *is*
  the applied tracked content (E1 DR-11).

This is the same defect class r88's follow-up found and repaired before admission (LOG.md:2073).
Two apply-ready replacements are delivered unapplied: `followup/CB1-boundary-refresh.md` (full
refresh) and `followup/E1-boundary-update-proposal.md` (section-level replacement text; the file
E1's report first described as missing appeared at 04:36 and **is** present at the cutoff).

## SHONEN

`SHONEN.md` is unchanged this round (`git diff --stat 51b286b 1b09f3f -- SHONEN.md` → empty); four
boxes at `SHONEN.md:5,6,8,9`. **No `[x]` is claimed** — no named non-author verifier has executed
the lane's instructions cold. Drafted from `followup/P4-shonen.md` (L1's call on box 3 below).

- `SHONEN.md:5` — `[ ]` *SKILL.md contains real decision tables, error patterns, checklists, cited
  sources* — **unchanged**. `test -e SKILL.md` → `ABSENT`; `git ls-files | grep -Ei 'skill'` → no
  matches. The box's subject does not exist to assert. The r89 governance material landed in
  `corpus/knowledge/` (R8–R10 rows at `:22-24`, the R9 demo fixture, the R10 worked example), not in
  a `SKILL.md`.
- `SHONEN.md:6` — `[~]` *At least one end-to-end domain task executed and logged in LOG.md* —
  **lane assertion retained; evidence improved**. The clause is satisfied at the delivered revision
  by the round-87 record (`LOG.md:1699`) and the round-88 record (`LOG.md:1908`). Round 89 adds a
  third end-to-end set (160-dir census, 8 durable cause fixtures, FN-2 pair, 14/14 anchors, R9
  fixture, R10 demo), but r89's own LOG entry is **not** appended (last section is `## Round 88`;
  drafts only: `W2-log-r89.proposal.md`, `P3-log-r89.md`'s append-ready text). The box's own evidence
  pointer is still stale (round-1 only); P4 recommends adding `LOG.md:1699`/`:1908`.
- `SHONEN.md:8` — `[ ]` *Instructions executable by an agent without oral context* — **P4 proposes
  `[ ]` → `[~]`; this seat records both sides and leaves the move to L1.** For the move: the D1
  support rule has two demonstrated applications (Maya 10/10; r87 14/14 → 22/22), the boundary doc's
  r85 probe replay block reproduces byte-for-byte, and the r87 decision table is bannered
  `SUPERSEDED (round-88 closure)`. Against the move: the same boundary doc still contradicts the
  shipped checker, the r87 application has no in-corpus claim-to-excerpt map, and the four new
  excerpts declare no delivery mode. Either way the box cannot reach `[x]` without a named
  non-author verifier executing the instructions cold.
- `SHONEN.md:9` — `[~]` *No cross-domain bleed (PROVINCE.md still accurate)* — **lane assertion
  retained; evidence strengthened**. `PROVINCE.md` bytes unchanged (`sha256`
  `94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa` at both commits); every changed
  path is under `corpus/` (76) or `.ufo/` (60); the new artifacts keep attribution, rights, and
  AI-training as three separate open questions and assert no rights conclusion
  (JCOV2/JCOV4/JCOV5 reach the same reading on independent probes); the ETCSL ledger row carries the
  external-only marker. `l0-questions.md`'s only change is K1's authorized round-89 append
  (`SE2` terminal check: `l0-questions.md | 1 +`, nothing else modified, nothing staged).

## Verdicts (ruled by L1 at closure)

calibration **improved (bounded)** — valid-key combined summary, FN-2 qualification, FN-1
resolved-index wording; 4+11 enumerable delta, 0 exit changes, five independent censuses;
bounds: two hedged wording shapes (null-holder, unrelated-identity tick) recorded as a bounded
definiteness regression queued for r90 (disclosed, not netted); FN-1 raw-present half unpinned.

coverage **improved (bounded)** — four delivered in-world excerpts, 14/14 anchors (22/22 under
the anchor rule — M4-verify's own script disqualified as the receipt), ETCSL external-only
marker; bounds: no R9 mode labels yet (prospective), no in-corpus claim→excerpt map.

depth **improved (bounded)** — R8/R9/R10 integrated (owner + prospective scoping), demo
fixture + worked example; JDEP2's undecided sub-cases named for r90; the recurring
documentation-parity harm (boundary doc + READMEs + render defect) was repaired in the closure
commit and is recorded transparently here, in SCORECARD.md, and in LOG.md.

**Round admitted** — every claim verifies; no unresolved trade. Repair materials came from the
follow-up wave itself (CB1's verified refresh + E1's corrections; measured README fixes).
## Findings & named debt

- **D-doc-drift (JAXIS R1 / D-D1, blocking; unrepaired).**
  `corpus/knowledge/holder-assessment-boundary.md`: three retired cause strings, the now-false
  precedence/combined-clause claim, the stale "delivered output" block, shifted `:NNN` anchors,
  self-contradicting PROPOSAL banner, stale census prose (CB1-CB1-R1…R19 revised; E1 DR-1…DR-15;
  H5 §4; JCAL2; JCAL3 Debt 2; H2 F5; JAXIS). Apply-ready replacements delivered **unapplied**:
  `followup/CB1-boundary-refresh.md`, `followup/E1-boundary-update-proposal.md`.
- **D-null-holder (measured harm candidate; JAXIS C-D4).** `holder_identity_detail` treats
  `from_holder: null` as an unresolved identity, downgrading a definite chain break to "possible"
  and qualifying a definite tick violation (this seat's probes; JCAL2 Findings 1–3; JCAL4 F3(a);
  E1 DR-5; C5/C6). Fix: gate the qualifier on non-null ids + identity-dependent comparisons only.
- **D-f2-readmes (JAXIS R2 / C-D3, blocking).** Three fixtures delivered *by this round* quote the
  pre-FN-1 cause strings (`r89-f2-dangling-from/README.md:9`, `-to/README.md:9`,
  `-invalid-source-id/README.md:9`); a naive line-by-line replay scores the delivered checker as
  failing them (JCAL3 Debt 1, V2 item 2, H5 §1, H2 F3, JCAL2, JCAL4, JAXIS).
- **D-fn2-readme.** Both FN-2 fixtures' READMEs still head their expectation section
  *"(integration verification pending)"*; the delivered pair now matches them (V2; P2).
- **D-fn1-branch (JAXIS C-D1).** FN-1's "present in raw … but absent from the resolved index" half
  has zero durable fixtures (JCAL1, JCAL2 F1, JCAL3 Debt 3, H2 F6, H5 §5).
- **D-no-map (JAXIS V-D1).** No in-corpus claim-to-excerpt map for the r87 cluster; 22/22 is
  reproducible only from wave evidence (JCOV4 D1, JCOV1 D1, JDEP4 F5, P4 D1, Q1).
- **D-r9-prospective (JAXIS V-D2).** The R9 carve-out does not cover the r87 cluster having been
  content-touched this round by four excerpts that declare no delivery mode (JCOV4 D2, JCOV1 D4,
  H5 §6, P4 D2).
- **D-r9-path.** The R9 row never writes the fixture path (JCOV3 D1).
- **D-r8-marker (JAXIS R4).** R8's element-side marker `external-only / unverified inspiration`
  occurs only inside the R8 row itself; three `external-only / …` variants coexist with no
  per-surface authority (K1 F2/F4, JCOV2 debts 1–2, JDEP2 D-2/D-3, JDEP4 F6, JCOV4 D4).
- **D-jdep2-cases (JAXIS D-D3).** R8/R9/R10 each leave a sub-case their own text cannot decide;
  the checker never reads the rows (JDEP2 D-JDEP2-1…6).
- **D-jdep1-render (JAXIS R4/D-D2).** The R8–R10 block is not in the rendered GFM table
  (JDEP1 D1, P3 re-verified); stale sixth-column label; R10 evidence freshness; "(named debt, r89
  ledger)" points at a nonexistent LOG entry (JDEP1 D2–D5).
- **D-fixtures-readme (JAXIS R3 / Q89-016).** `corpus/fixtures/README.md`'s last section is
  `## Round 88`; `grep -c 'r89'` → `0` — third round running (JCOV3 D2, JCOV4 D3, H1 F2, H2 F4,
  H5 §4, P4 D3, Q1).
- **D-r87-readme (JAXIS R3).** `corpus/fixtures/r87-myth-cluster/README.md` names none of the four
  new support excerpts (JCOV4 D3, JCOV1 D2, H1 F2, H5 §6).
- **D-source-prefix-readme (JAXIS R4).** `r87-probe-source-prefix/README.md:1` cites
  `:306`/`:308`/`:310`; delivered lines are `:333`/`:344`/`:350` (H5 §3).
- **D-r10-naming.** Demo `r89-cross-cluster-contradiction.md` (singular) vs durable register
  `cross-cluster-contradictions.md` (plural) (JCOV3 D3, E1 DR-15).
- **D-capabilities-table (JAXIS D-D7).** The structured table still reads `— none yet —`; JDEP4's
  row-2 preconditions require repairing it with row 1 in one edit (P2 concurs; defer if not).
- **D-spence-row (JAXIS V-D5).** The Spence ledger row sits outside the table (pre-existing,
  carried; JDEP1 out-of-scope note, JDEP4 F7b).
- **D-r8-unexercised (JAXIS D-D4).** No R8 demo fixture; `verbatim`, `translation`, `summary` modes
  unexercised (JDEP2, JDEP4 F6).
- **D-keeps-watch-with.** `keeps_watch_with` occurs once in the corpus with no definition surface;
  JCOV2's three unextracted detail lines should be re-scanned (JCOV2 debts 3–4).
- **D-round-record (JAXIS R3 / Q89-050).** LOG/SCORECARD unchanged at `1b09f3f`; append-ready
  `P3-log-r89.md` + `P2-scorecard-r89.md` exist; the r89 closure must also retire the SCORECARD
  shape-valid-bound (E1 DR-14, JAXIS C-D6).
- **The recurrence is the headline (Q1).** The instruction/expectation surface drifts every time
  the checker's disclosure family moves: repaired at `51b286b`, stale again at `1b09f3f` — three
  rounds running. Root cause: README expectations and doc replay blocks are prose with no harness.
  `Q1.md` census: 53 rows — 41 open, 8 bound, 2 closed, 1 unlanded, 1 resolved (open_count 42);
  every JAXIS debt id maps onto a Q89 row. `Q1-r89-debt.json` is the r90 planner
  (`lowest_axis_basis` → depth).
- **r88-debt disposition (W1).** `W1-disposition.json` re-verifies all 49 rows of the r88 Q1 debt
  ledger at `1b09f3f` (closed / closed-bounded / partially-closed / re-opened / open / carried /
  superseded-recorded; closure credit split between `51b286b` and `1b09f3f`).
- **Terminal freeze (SE2).** Sentinel checks at the terminal state: `followup/` naming 0 violations,
  no subdirectories, no zero-byte files; only `l0-questions.md` modified (+1 line, nothing staged)
  plus the untracked `followup/`; HEAD `1b09f3f`; no seat commits; no writes outside the allowlist.
  (SE2's in-report inventory was taken at an earlier moment than this report's cutoff; the
  authoritative count here is 62 files at `04:37:54`.)
- **Process debt (Q2.md).** Poll protocol widely missed (19/32 first artifacts ≤ deadline; 23/32
  wrote after it; 10 seats hit the 600 s cap); roster prose drifted; one reviewer recommendation
  (C7's M3+M5 preference) overridden without a wave-visible record; r88's freeze-then-verify debt
  held (V2). Q2's three r90 improvements: freeze-and-reverify the delivered revision; dependency
  barrier/calibrated deadlines; roster-as-data. Landing record: 21 of 31 non-clerk seats had
  artifacts at the 03:52:53 work-wave cutoff; M2's alternative excerpts never arrived.
- **No push, no registry write, no sibling-repo write.** `followup/` (62 artifacts) and the l0 line
  are left for the integrator's commit decision.

## Pointers

- Wave reports + patches: `lore-shokunin/.ufo/waves/round-89/` (32 seat reports + `wave-spec.md`, `patches/`).
- Follow-up artifacts: `lore-shokunin/.ufo/waves/round-89/followup/` (62 files at the
  `2026-10-17T04:37:54-03:00` cutoff).
- Work commit: `lore-shokunin@1b09f3f` (baseline `51b286b`). No push (7 ahead of `origin/main`).
- Uncommitted: `l0-questions.md` (K1's authorized round-89 line, +1 line only);
  `.ufo/waves/round-89/followup/` (untracked).
- Round-record drafts: `patches/W2-log-r89.proposal.md`, `patches/W2-scorecard-r89.proposal.md`,
  `patches/W2-report-r89.skeleton.md`, `followup/P3-log-r89.md` (append-ready LOG text),
  `followup/P2-scorecard-r89.md` (drop-in SCORECARD section), `followup/P4-shonen.md`.
- Doc-refresh proposals (unapplied): `followup/CB1-boundary-refresh.md`,
  `followup/E1-boundary-update-proposal.md` (+ `CB1.md`, `E1-drift.json`).
- Debt ledger / planner: `followup/Q1-r89-debt.json` (+ `Q1.md`), `followup/W1-disposition.json`
  (+ `W1.md`), `followup/JAXIS-verdicts.json` (+ `JAXIS.md`).
- MANIFEST closure entry draft: `.ufo/waves/round-89/followup/P1-manifest-entry.json`.
- Seat report + receipts for this writer: `.ufo/waves/round-89/followup/P1.md`,
  `followup/P1-measurements.json`.

## Handoff

- **Delivered revision and verification scratch:** `1b09f3f`; scratch `/tmp/P1-r89/`
  (`census.py`, `deliv-tuples.json`, `probe-null-chain/`, `probe-null-tick/`). This seat re-ran, on
  the delivered tree: the 160-dir census + delta vs `patches/B1-tuples.json` (4 changed + 11 new,
  0 exit/count/stderr changes), the 14-anchor sweep, the ledger/table/`grep` census, the
  boundary-doc drift probes, and the two nullable-holder probes. Every figure in "Before → after
  measurements" is this seat's observed output; the machine-readable bundle is
  `followup/P1-measurements.json`.
- **Integrated claim artifacts:** C1 — `corpus/fixtures/check_bible.py` + 11 new fixture dirs; C2 —
  4 excerpts in `corpus/fixtures/r87-myth-cluster/` + `reference-ledger.md` marker; C3 — R8/R9/R10
  rows in `corpus/knowledge/r88-sourced-inspiration-decision-table.md` +
  `corpus/knowledge/r89-cross-cluster-contradiction.md` + `corpus/fixtures/r89-inspiration-paraphrase/`.
- **Judging coverage:** axis synthesis (JAXIS), calibration (JCAL1–JCAL5), coverage (JCOV1–JCOV5),
  depth (JDEP1–JDEP4), harm (H1–H5), drift (CB1/E1), connector + L0 (K1), debt/process/record
  (Q1/W1/Q2/P2/P3), SHONEN (P4), freeze (V2), sentinel (SE2) — all read and cited above.
  Protocol checks ran four times (04:28:54 / 04:30:36 / 04:35:29 / 04:37:54); the wave was still
  landing after the first two, so this report names its snapshot cutoff explicitly.
- **Remaining TODOs (L1):** rule the three axes (JAXIS recommends calibration improved (bounded),
  coverage improved (bounded), depth harmed (bounded) with transition on R1–R3) and the admission
  mode; if repairing before admission — R1 boundary-doc refresh (both proposals delivered), R2 the
  three F2 READMEs, R3 fixture index/SCORECARD/r87 README, R4 cheap repairs — then fix the nullable-
  holder predicate and the FN-1 raw-present fixture in r90; commit the round record
  (`P3-log-r89.md`/`P2-scorecard-r89.md`) and decide on the uncommitted `followup/` and l0 line.
- **Overall round assessment:** the declared C1/C2/C3 claims all verify on the delivered tree with
  independent reproduction; candidate harms (nullable-holder definiteness loss, boundary-doc drift,
  governance sub-case gaps) are measured and left for L1 rather than netted away. No admission,
  score, or axis verdict is claimed here.

## Closure addendum (L1)

- [to be filled by L1: verdicts, repairs applied, admission decision, closure commit]

## Closure addendum (L1, 2026-10-17)

- **Lore closure commit (this round's record):** SCORECARD/LOG round-89 sections; the
  documentation-parity repair (boundary doc re-derived from CB1's verified refresh with E1's
  corrections; three f2 READMEs measured and fixed; R8–R10 table header/delimiter; capabilities
  table gains both rows; fixtures README Round 89 section; R8 marker on the r87 note; stale
  pending-verification markers resolved; source-prefix anchors re-pinned), all follow-up
  artifacts, and K1's sanctioned `l0-questions.md` line 5 (kotodama contract now tracked at
  `49ac1a5`; lore-side acknowledgement untriggered).
- **Post-closure census re-verified after the prose batch:** 160 dirs, 32/128, the same
  4 enumerable changes; no tuple moved.
- **Substrate note:** the follow-up wave ran 12 seats on `hyper/deepseek-v4.1-flash` and 20 on
  `opencode-go/deepseek-v4.1-flash` after hyper credit exhaustion (402) — the declared
  fallback chain; the regimen's stop rule was not triggered (a fallback lane served).
- L0 carries the kotodama contract-authorship question (round-88 line) and the R8 owner-
  escalation path. No push, no registry write, no sibling-repo write.
