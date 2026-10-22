# KakeR28 native planner — datawalk of the full original C2 boundary

Role: `KakeR28AuthorS3.K28NativePlanner` (ordinary native planner, source-only). WT:
`/fast/scratch/hyaku/kake-r28-author`, observed `git rev-parse HEAD` =
`22c1669c1fec83d1a0769de6b9ce686c75657e66` = declared BASE; `git status --porcelain` empty.
Scope: planner datawalk of the range-aware citing-set consumer (original contract C2 +
`gateInterface`), retaining all known failures. No lane code, gate, runner, fixture, counter,
oracle or selftest was executed. Reads were metadata-level: `read`/`glob`/`grep`, `git
rev-parse/status/ls-tree`-class lookups, `sha256sum`, `cat`/`find`/`wc`/`head`, and `python3 -c`
JSON pretty-parsing of data files only (never lane code). No installs; pacman pause honored.
This report is advisory and pre-result: nothing here is a pass, an admission, or a custody claim.

## 1. Authority and pin set actually read

| Input | Location | Identity |
|---|---|---|
| Round-27 contract | `.ufo/waves/round-27/contract.json` | sha256 `6d2d7f51…` (parent pin) |
| Unresolved acceptance | `.ufo/waves/round-27/unresolved-acceptance.json` | sha256 `41e11493…` |
| Verifier spotcheck | `corpus/lessons/round-27-verifier-spotcheck.md` | sha256 `aabcdf3d…` |
| C2 oracle (16 pairs) | `.ufo/waves/round-27/c2-oracle.json` | sha256 `1d038205…` |
| Frozen input manifest | `.ufo/waves/round-27/frozen/expected.json` (28 digests) | sha256 `628b7a05…` |
| Frozen inputs | `frozen/population.json` (32 rows, r26), `frozen/ledger.json` (41 pairs, r26), `frozen/corpus/knowledge/*` (26 files) | byte-pinned |
| Gate | `scripts/citing_set.py` (668 lines) | sha256 `3a361a002f66…ffc228` = falsified candidate `ac46a747` blob `352a471a…` |
| Runner | `scripts/citing_set_selftest.py` (384 lines) | sha256 `3c167895c7f3…a1c` |
| Instruments | `.ufo/waves/round-27/{count_c1.py,c2_count.py,oracle_selftest.py,git_name_selftest.py,fetch_group.py,privacy_selftest.py}` | read; not targets of the C2 repair except where named |
| Fixtures | `scripts/fixtures/citing-set/` 29 case dirs, 118 files | parent pin file `source-input-pins.json` (156 pins) |
| Attack corpus | `.ufo/waves/round-27/w2/*` (86 entries) | key seats read in full |
| Known-failure ledgers | `w2-findings-queue.json`, `w2-additional-findings.json`, `frozen-candidate.json`, `current-interpretation.json`, `final-record-state.json`, `carry-errata.json` | read |
| R26 originals | `.ufo/waves/round-26/{population.json,statements.json}` | 32 rows / 41 pairs; `seatUnverifiable` S001×ghp-served-set 3, S033×static-canonical-preflight 3; +1 erratum unit S007×ghp-custom-domain (carry-errata) |

## 2. Datawalk skeleton — full C2 boundary at BASE

Pipeline stages of `scripts/citing_set.py` (line numbers at BASE):

1. **CLI surface**: `build_parser` :575-586 (plain argparse, store-last-wins, prefix
   abbreviation on, `--json` a no-op flag, `--selftest` delegation flag); `GateParser.error`
   :560-572 (emits `{verdict:"could-not-evaluate",…,"error":"usage: …"}` + stderr, exit 64 —
   undocumented `error` key); missing-option check :637-643; `--help` exits 0 with
   non-JSON argparse text (CliUsage F5/F8).
2. **Argument path normalization**: `normalize_relative` :159-171 (rejects absolute,
   `..`, empty; collapses `//`; replaces `\`).
3. **Source selection**: `main` :650-653 — `if arguments.revision:` truthiness, so
   `--revision ""` silently selects working-tree (CliUsage F3, CliJson F4);
   `GitSource._resolve` :271-285 (blank `"   "` → `revision_not_found` — inconsistent).
4. **Document read plane**: `WorkingTreeSource.read_document` :205-215 — realpath
   containment, then blind `open(…,"rb")`, catches only `OSError`: no `lstat`, no
   regularity check → FIFO blocks forever (CLI-FIFO; CliUsage F1, CliPaths F1,
   ReviewInputSafety §4); `GitSource.read_document` :300-301 — `git show rev:path`
   returns symlink target text, so symlinked docs are unreachable in git mode while
   working-tree mode follows them (CliPaths F3).
5. **Corpus enumeration plane** (stricter than the document plane — the asymmetry that
   produced the FIFO defect): `WorkingTreeSource.corpus_files` :217-236 + `_walk` :238-259
   (lstat dir, `symlink_rejected`, `not_a_directory`, `not_a_regular_file`);
   `GitSource.corpus_files` :303-321 (`ls-tree -rz`; mode `120000` → symlink_rejected;
   non-blob/`160000` → not_a_regular_file) — but no `not_a_directory` counterpart: a blob at
   `corpus/knowledge` itself is scanned as a document (CliPaths F2, CliJson F10). Absent
   corpus → `[]` silently in both modes → `clean` with `corpusFiles:0` (CLI-SCOPE-FALSE-GREEN;
   CliUsage F4, CliJson F2, CliPaths F5).
6. **JSON/shape decode**: `load_json_document` :349-360 — `utf-8` decode, `json.loads`,
   catches `ValueError` only → `RecursionError` escapes as exit-1 traceback with no JSON
   (JSON-PROTOCOL F3, stack-dependent threshold); dict-required; `load_population` :363-379
   (any non-blank string id accepted; `mapping`/`display` maps; duplicate spellings folded);
   `load_ledger` :382-397 (row/file non-blank strings; `normalize_ledger_file` :174-181
   strips `./` and rewrites `\`→`/` but not `..` or `//`).
7. **Scan**: `scan_text` :329-341; `_TOKEN_RE` `(?<!\w)S([0-9]{3,})(?!\w)` :108;
   `_RANGE_RE` `\bS(\d{3,})\s*(?:-|–|—|\.\.|through|to)\s*S(\d{3,})\b` :115;
   `id_key` :147-156 (`S001`==`S0001` → `("n",1)`).
8. **Evaluate**: `evaluate` :405-547 — citing set build :422-474 (literal pair =
   `(key, file)` once per file; ranges descending `end<start` or `end-start>200` →
   `citation_range_invalid`, still exit 1 not 2; NOTE the docstring's "endpoints remain
   literal citations" is false for *glued* invalid ranges like `S006toS001` — CliJson F6);
   ledger maps :476-480; findings :482-517 — `display.get(key, str(numeric))` fallback at
   :488/:500/:513 loses original spellings (IDENTITY-PATHS; AttackCase15/17/26);
   deterministic sort :521; verdict :523-531 (`input_invalid` ⇒ could-not-evaluate exit 2);
   result fields :533-547 (`verdict,citingPairs,ledgerPairs,findings,populationRows,
   corpusFiles,outsidePopulation,source,revision`).
9. **Emit** :555-557 — single `json.dumps` doc on stdout.
10. **Consumers/instruments** (boundary-adjacent, not the candidate):
    `citing_set_selftest.py` — `parse_args` :58-72 (`parse_known_args`: silently ignores
    unknown args), `DEFAULT_TMPDIR="/fast/scratch/hyaku/kake-r27"` :49 (stale r27 path),
    `child_env` :102-117 (copies caller env), `parse_report` :120-141 (scans for first
    parseable `{` — tolerant), `finding_ids` :144-164 (id multiset only — ORACLE-GRANULARITY),
    `run_case` :188-279 (never passes `--revision` → zero Git-mode coverage; timeout→row
    failure), floor `--min-cases` :351-375 not enforced by default (ReviewInputSafety §6);
    `c2_count.py` — DECLARATIONS pin :5, snapshot digest check :19-23, hardcoded scratch
    `/fast/scratch/hyaku/kake-r27` :17 (ReviewInputSafety §7), caller `--revision`
    interpolated into git args without `--end-of-options` (ReviewInputSafety §0);
    `oracle_selftest.py` — disposable-clone selftest behind `--selftest`;
    `git_name_selftest.py` — 30-check Git/WT name parity instrument (in wave dir).
    Docs the ruler must re-derive: `SKILL.md` :594-642 (registry rows :616-618),
    `corpus/QUALITY.md` :235-267, docstring :1-80, `contract.json gateInterface` :25-31.

## 3. One concrete trace — fixture `04-hyphen-range-omission`

Input (contract fixture shape): `corpus/knowledge/publish-channels.md` whose metadata line 1
is `source: S001-S007 (corpus/SOURCES.md) - …`; `population.json` rows S001..S007; `ledger.json`
6 pairs: each of S001,S002,S003,S004,S005,S007 × `corpus/knowledge/publish-channels.md`
(S006 deliberately absent); `expected.json` `{exit:1, findings:["unadjudicated_citing_pair"]}`.

Trace at BASE semantics: CLI parses options → `normalize_relative` ok →
`WorkingTreeSource` (no `--revision`) → `read_document` both JSON docs →
`load_population`/`load_ledger` → `corpus_files` = `[corpus/knowledge/publish-channels.md]`
→ `scan_text`: literal regex matches `S001` and `S007`; `_RANGE_RE` matches `S001-S007`
→ expand 1..7, all in population → citing = {S001..S007}×file (7 pairs) → ledger compare:
S006 missing → one `unadjudicated_citing_pair {row:"S006",file:…}` → sort → verdict `failed`,
exit 1 → JSON `{verdict:"failed",citingPairs:7,ledgerPairs:6,findings:[…1…],populationRows:7,
corpusFiles:1,outsidePopulation:0,source:"working-tree",revision:null}`.
Observed agreement: matches `expected.json` and the recorded candidate receipts verbatim.

## 4. Generalization — smallest meaningful COMPLETE repair (not finite16-only)

"Complete" = the contracted interface itself, not the frozen 16-detection. Mandatory repairs
repair **observed falsified behavior**; each optional item changes a contract-silent
convention and needs a Main ruling before it can be a *want*.

### 4a. Mandatory repairs (observed falsifications; original contract/outcomes unchanged)

| # | Repair | Evidence |
|---|---|---|
| M1 | Non-regular document reads must fail `input_invalid` exit 2, never block: `lstat`+`S_ISREG`+symlink rejection on population/ledger before open (same discipline as corpus plane). Termination is mandatory: a hang is `no_termination`, strictly worse than any exit. | `citing_set.py:205-215`; CliUsage F1; CliPaths F1; ReviewInputSafety §4 |
| M2 | JSON-in-every-mode: bound JSON decode depth by a stack-free check (or declared limit) so deep input yields `document_not_json` exit 2 — never traceback, exit 1, or machine-dependent threshold. | :349-360; CliJson F3; contract "JSON … in every mode" |
| M3 | Present-but-empty `--revision` → `revision_not_found` exit 2 (never silent working-tree measurement). | :650; CliUsage F3, CliJson F4 |
| M4 | Absent/zero-regular-file `corpus/knowledge` → `input_invalid` exit 2 — **scope carve-out (Main-confirmed)**: the defect is zero *files*, not zero `citingPairs`. Case `21-no-citations-empty-citing-set` (1 regular corpus file, nonempty population, empty ledger, expected clean exit 0) MUST stay green. Reject absence, never an empty citing set. | :217-236/:303-321; CliUsage F4, CliJson F2, CliPaths F5; parent steer |
| M5 | Git/WT parity on corpus shape: blob at `corpus/knowledge` → `not_a_directory` exit 2 in git mode (not scanned as a document). | :303-321; CliPaths F2, CliJson F10 |
| M6 | Document symlink parity: symlink blob documents → `input_invalid` in git mode; recommend symlink rejection for documents in *both* modes so `source:working-tree|git` describe the same measurement basis (WT-following part is a tightening — see O3). | :300-301 vs :205-215; CliPaths F3 |
| M7 | Ledger-sourced findings must carry the ledger row's **own spelling** (`row:"S019"`, never bare `"19"`); population display map remains the spelling source only for `unadjudicated_citing_pair` rows. | :500/:513; AttackCase15/17/26; w2-findings-queue accepted plan |
| M8 | One truthful POSIX path convention: `normalize_ledger_file` must not silently rewrite `\`→`/` (POSIX `back\slash.md` becomes unadjudicable) nor leave `//` divergent from `normalize_relative`. Smallest truthful repair: reject ledger `file` containing `\`, `..`, absolute or empty segments as `input_invalid`, or normalize identically on both sides — Main picks the convention; silent re-spelling is the defect. | :174-181; CliGitNames F5; AttackCase11 F2 |
| M9 | Docstring vs code on invalid-range endpoints: either expand the endpoint-literal fallback so glued invalid ranges keep endpoints as literals (docstring already declares this), or rule the doc wrong. Recommend honoring the docstring after checking no frozen corpus/glued-invalid-range dependency exists (none observed in the 26 files' falsified-16 output; verify at prereg). | :444-468, docstring :52-56; CliJson F6 |
| M10 | `cited-but-outside-population` ledger rows must not be reported as plain `ledger_pair_not_cited`: keep the id (oracle-compatible) but add an additive `reason`/`detail` field separating non-citation from population exclusion, and expose `outsidePopulation` as a declared field. | :493-503; AttackCase17 F2 |
| M11 | Runner floor: `citing_set_selftest.py` must enforce the contract ≥12-case minimum by default (below-floor ⇒ failed), and the gate's `--selftest` delegation must forward the runner's options (`--tmpdir` etc.) or declare the forwarding set. | `citing_set_selftest.py:49-70,351-380`; ReviewInputSafety §6; AttackCase19 §4 |
| M12 | Scratch isolation: any R28 instrument gets a caller-selectable scratch dir; r27's `c2_count.py` hardcodes `/fast/scratch/hyaku/kake-r27` — do NOT edit r27 bytes; the R28 counter is a new file that references the same frozen pins. | `c2_count.py:17`; ReviewInputSafety §7 |
| M13 | Admission conjunction: the R28 C2 measure must bind finite-16 detection AND the full fixture suite AND parity AND changed-input sensitivity at one revision (a stub/constant gate passing the finite predicate must fail the conjunction). No code change — a measurement-contract requirement. | MutateConstant; AttackC2Oracle D2 |

### 4b. Optional contract tightenings (require a Main ruling; contract currently silent)

- **O1** Reject repeated valued options (last-path-wins silently certifies an unread input — observed false-green B01/B06/B08). Recommend reject → exit 64. (CliUsage F2)
- **O2** `allow_abbrev=False` (kills `--popu` prefix matching). (CliUsage F6)
- **O3** Reject symlinked population/ledger in working-tree mode for full parity (currently followed when in-root). (CliPaths F3 half)
- **O4** Declare `--selftest` + measurement options mutually exclusive; reject contradictory mixes. (CliUsage F7, AttackCase19)
- **O5** Reject duplicate JSON object members and nonfinite literals (`NaN`/`Infinity`) as `document_not_json`. (CliJson F8)
- **O6** Population ids unreachable by the grammar (`S01`, `A01`) — either hard-reject `input_invalid` (breaks no original fixture) or additive `unreachablePopulationIds` diagnostic. Silent zero-pair green is the defect; the fix shape needs ruling. (CliJson F1)
- **O7** Duplicate population row spellings sharing one `id_key` (`S001`+`S0001`) — disclose or reject. (CliJson F8)
- **O8** Span wording: preserve `end-start>200` semantics, clarify "spans more than 200 ids", test both boundary values. (CliJson F7; w2-additional-findings qualification decision)
- **O9** Exit-64 payload: declare the `error` key and its `verdict` field in the schema. (CliUsage F8)
- **O10** `--help`: emit the usage JSON payload (preferred) or declare it outside "every mode". (CliUsage F5)
- **O11** `parse_report`'s scan-for-`{` tolerance and `parse_known_args` swallow of unknown args in the runner — declare or tighten. (selftest :58-72/:120-141)
- **O12** `git` subprocess bound (timeout) so a wedged git can't hang the gate — termination completeness. [INFERENCE: plausible, unobserved]
- **O13** C1-side instrument defect `C1-UNIT-OVERRIDE` (pair-level HOLD erases carried UNVERIFIABLE units — AttackC1Target F1, AttackOracleFreeze R8): a `count_c1.py` repair is OUT of the narrow C2-consumer scope; recommend recording it as an R28 ruler red-case only if Main rules the C1 counter in scope. C1 itself stays unprovable regardless (see §7).

## 5. Independent ruler + expected-fixture proposal (lands BEFORE any candidate)

Naming is a proposal; Main owns final paths. All wants derive from `contract.json`
gateInterface/output/fixtureInterface, the gate docstring, and original fixture inputs —
never from candidate output. Two-writer rule retained: producer of `expected` files and the
runner are separate authors; derivation method recorded per case.

- **R1 interface rulebook** (e.g. `.ufo/waves/round-28/ruler/interface-wants.json`): one row
  per want — {id, contract anchor path:line or docstring line, expectation}. Covers: exits
  0/1/2/64 semantics, JSON-object-on-stdout for every non-usage path and the declared usage
  shape, bounded termination (harness timeout ⇒ `no_termination`, NOT satisfiable by an
  exit-2 expectation), nonregular/missing/unreadable documents, absent corpus, path
  containment (absolute/`..`/escaping), corpus symlink/non-regular rules (retained), git-mode
  equivalents.
- **R2 extended oracle format** for NEW expected files: `{exit:int, findings:[ids],
  findingTuples:[{id,row,file,occurrences?,reason?,scope?,path?}], counters:{citingPairs,
  ledgerPairs,populationRows,corpusFiles,outsidePopulation}, source, revision?}` — optional
  fields asserted only when present. Original 29 `expected.json` bytes are never edited;
  R28 either (a) adds a parallel extended-expected file per original case, or (b) builds a
  new fixture tree re-deriving all 29 original semantics PLUS identity/counter pins. Both
  preserve originals; (b) is cleaner for before/after diffs. Main rules on placement
  (same tree extends `citing_set_selftest.py` discovery past 29 cases — beneficial, but
  changes the shipped suite's count; new tree keeps r27 evidence intact).
- **R3 Git/WT parity runner**: materialize each file-based fixture as a disposable repo
  commit; run `--revision`; assert identical exit + finding multiset + finding identities
  modulo `source`/`revision` fields. Closes the zero-Git-coverage hole. (CliPaths §coverage,
  CliJson F12)
- **R4 harness invariants**: per-case timeout + `no_termination` verdict; stdout must be one
  JSON document; declared stderr rules; scratch dir parameterized; child env scrubbed
  (ruling O11-adjacent); runner never rewrites expectations (existing property, retained).
- **R5 frozen-oracle preservation**: re-pin at R28 declarations revision — c2-oracle 16
  pairs, `frozen/expected.json` 28 digests, contract.json, the 156 pins in
  `source-input-pins.json` (29 cases/118 files), r26 population/ledger. `snapshot_tampered`/
  `frozen_input_changed` semantics retained byte-identical.
- **R6 mutation-sensitivity map** declared in the ruler: which suite elements must kill
  constant16 (MutateConstant), endpoint-only ranges (MutateRanges), duplicate-suppression,
  population-filter removal, row/file misattribution, hardcoded `occurrences` — the measured
  discriminating-power contract, so ruler adequacy is itself checkable.
- **R7 docs conformance seat set**: every documented behavior in `SKILL.md:594-642`,
  docstring :1-80, `contract.gateInterface` re-derived → contradictions (F6/F7 wording,
  `--json` no-op, usage payload) become ruled wants.
- **Fixture case families** (new cases; each causally distinct, not padding): per-separator
  ranges incl. glued + linebreak; descending; span boundary 200/201/202; interior/endpoint
  omissions; population gaps and endpoint-outside; comma lists; metadata/EOF; `.json`
  knowledge files; ledger duplicates (multiplicity/aliased spellings), not-cited,
  outside-population-cited (reason field), absent files, noncanonical paths (`\\`,`//`,`./`,
  `..`, absolute); population malformed JSON/shape/blank-id/duplicates/unreachable ids/deep
  nesting; documents missing/dir/unreadable/non-UTF8/BOM/FIFO/socket/symlink/absolute/
  escaping; CLI repeated options/abbreviations/empty revision/missing/unknown options/help/
  selftest mixes; corpus absent/dir-as-file/symlinked/nonregular/non-UTF8/nested/awkward
  names (space, tab, newline, non-ASCII, backslash); empty-corpus vs zero-citations
  (case-21 carve-out preserved); parity twins for every file-mode case. Estimate: ~60–90
  new cases + 29 retained originals.

## 6. Proposal/evidence wave — honest seat inventory (no padding)

Distinct source-only assignments that genuinely exist at BASE:

- **A — per-case oracle re-derivation**: 29 seats (one per original fixture): independently
  derive exit/id/identity/counter wants from contract+inputs; check the case exercises its
  named dimension (cases 17/26-type critiques); output = per-case evidence + want rows.
  These are 29 distinct *evidence* artifacts collapsing into ~4–6 causal proposals
  (identity pinning, dimension isolation, oracle extension, doc fixes) — disclose as such,
  do NOT count as 29 improvements.
- **B — boundary families**: ~20 seats, one per defect family in §4 (each: contract quote +
  want row + fixture sketch + parity twin).
- **C — data-file audits**: ~8–10 seats over r26 population/statements, frozen inputs,
  pairs.json, complete-ledger.json, discovered-pairs.json, carry-errata.json (consistency,
  which wants the frozen inputs already encode, 18 outside-population debt visibility).
- **D — instrument audits**: ~6–8 seats on `citing_set_selftest.py`, `c2_count.py`,
  `oracle_selftest.py`, `git_name_selftest.py`, `count_c1.py` (read-only; count_c1's
  override hole is C1-side — see blocker B1).
- **E — docs/registry conformance**: ~4–6 seats (SKILL rows, QUALITY criteria, SCORECARD
  stale wording census, README/LOG pointers — per AttackC1Target §Stale-wording).
- **F — grammar/property exhaustiveness**: ~4 seats (separator×position×boundary matrix,
  id-grammar corner cases).
- **G — connector (mandatory)**: 1 seat, sibling-overlap scan.
- Total ≈ 72–79 seats: inside the 64–100 band ONLY if per-case derivation seats count as
  distinct assignments (they do produce distinct artifacts). Honest caveat for Main: causal
  proposals ≈ 30–35; the wave is a *proposal+evidence* wave, not 64 causal fixes. If Main
  wants only causal slices, ~35–40 natural seats and the band target is unmet without
  padding — disclosed sizing debt per the contract clause.

## 7. Preservation declarations

- **Original-target preservation**: every original byte and expectation stays immutable —
  `contract.json`, `c2-oracle.json` (16 pairs), `frozen/expected.json`+28 inputs, all 29
  fixture cases (118 files), r26 `population.json`/`statements.json`/wave tree (279 files),
  `pairs.json`, `carry-errata.json`, `fetched/*`, all `corpus/knowledge/*`, the r27 counters
  and selftests. Findings may only monotonically enlarge obligations. No oracle rewritten to
  candidate output; UNPROVABLE disclosed rather than fitted.
- **Seven unknown units remain unknown**: S001×ghp-served-set (3), S007×ghp-custom-domain
  (1), S033×static-canonical-preflight (3); strict C1 = 55 decided / 58 reviewed. No new
  evidence acquisition or old stopped work is authorized to discharge them; C1 stays
  UNPROVABLE this round regardless of C2 repair. Presence41/57 or58/58 is not strict
  support; mixed 313/318/310 sums are not interchangeable.
- **Retention failures retained, not re-scoped**: RETENTION-FRAGMENT and
  RETENTION-TRUST-BOUNDARY concern `fetch_group.py`/manifest machinery — outside the
  citing-set repair; no source reacquisition or sanitizer repair is claimed here; they stay
  recorded failures (in-scope only as C1 evidence provenance caveats).
- **No-harm clause set**: (i) original-file byte preservation above; (ii) case-21 semantics
  (valid zero-citation clean) preserved under M4; (iii) finding-id vocabulary and exit map
  unchanged — only additive fields, each under ruling; (iv) no edits to the other seven
  `scripts/*`, lane MANIFEST/state/siblings, prior round claims; (v) no r24-stopped work,
  no network, no foreign/unowned artifacts.
- **One integration owner**: Main integrates and commits to canonical; likely implementation
  ownership (post-SRT): `scripts/citing_set.py`, `scripts/citing_set_selftest.py`, the
  fixture tree additions, and R28-owned ruler/evidence paths. Concurrent writers need
  disjoint actual worktrees per the shared contract.
- **What the ruler must land before Main's before-measurement/SRT**: (1) the committed R1
  rulebook + R2 expected files + fixture tree (producer≠runner), (2) the R3 parity runner
  and R4 harness, (3) R5 pins of every input incl. the 156-pin manifest, (4) the R6 mutant-
  kill map, (5) a NEW R28 counter binding finite16 + suite + parity + sensitivity at one
  revision (never `c2_count` alone — D2/M13), (6) documented expected-before values derived
  from contract text for each falsified behavior (e.g. FIFO → `no_termination`, deep JSON →
  `document_not_json`, absent corpus → `input_invalid`, `row:"19"` → original spelling).
  Then Main runs the actual before-CLI at the frozen pin.

## 8. Material blockers / rulings needed

1. **B1** Is `count_c1.py`'s override hole (C1-UNIT-OVERRIDE) in R28 repair scope? It's a
   C1 instrument defect; repairing it cannot make C1 provable. Recommend ruler red-case
   only if ruled in scope; otherwise remains a recorded failure.
2. **B2** Fixture placement: new `expected` schema in-place (extends the shipped 29-case
   suite) vs a parallel R28 tree (r27 suite stays exactly as filed). Recommend parallel
   tree + optional in-place additions under ruling.
3. **B3** Optional tightenings O1–O12 each need a yes/no ruling (they alter contract-silent
   conventions); my recommendations are marked per item.
4. **B4** M9/M10/M8 fix *shapes* (which convention) need ruling even though the defects are
   mandatory — the honest split is defect=mandatory, convention=ruling.
5. **B5** Span semantic declaration (200 vs 201 boundary) — preserve numeric `end-start>200`,
   ruled wording.
6. **B6** In-place edit of `scripts/citing_set.py`/`citing_set_selftest.py` (the falsified
   candidate bytes) is the contract's likely ownership but is a mutation of measured-failed
   source — needs the SRT freeze first; nothing here presumes it.

## 9. What this report does NOT claim

No execution, no pass, no admission, no scalar or promotion claim, no continuous custody or
liveness claim, no private-host authority, no discharge of the seven unknown units, no
retroactive proof that r27's measurements differ from the recorded receipts. All pins are
the parent's recorded values plus my own read-only observations at BASE `22c1669c`.
