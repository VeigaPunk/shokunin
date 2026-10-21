# mori — round19, mori19attempt2

Final landed lane tip: **2061780117e6ca637725004897bd288d3ba7e988**.
Entering tip: `b3602869dadd4016675aeba8db2adf3fa1e1b531`.
Final same-instrument measurement: `11795ac0e0a44db6549534eb1239e26353446370`.
Six-script suite/replay revision: `c0fe0b230769ffba7168955f87985ec3ce08f41d`;
its six tested script blobs are identical at the final tip. Only the repaired
counting harness pair was re-exercised afterward.

## Work performed

Declared claims: **C1 adjacency6 (capability)** — a bounded, blob-bound content-review
coverage gate that refuses missing/stale/unresolved/provenance-only clearance;
**C2 calibration5 (lowest non-retired tie)** — intrinsically revision-bound freeze
receipts with exact loaded-input/script digests, resolved claim commits and argv.
Scores are held, not increased for fixture volume. These are two distinct claims,
not a new claim for every routed repair.

- Froze the exact194-path population and original requirement oracle before implementation
  (`5e393d20`; `.ufo/waves/round-19/frozen/{content-population,expected}.json`).
  The dirty/external-input refinement and generated fixture-value oracle are explicitly
  co-evolved; the original expected bytes remain unchanged.
- Implemented `tools/mori-content-review.py`, extended `tools/mori-freeze-order.py`,
  and added the runnable finite regression instrument (`SKILL.md` registry;
  `evidence/final-stability-coda.json`). C1 is independently demonstrated by its CLI
  selftest and by passing10/10 even during the first C2 failure; C2 has standalone
  historical replays and selftests, independent of C1.
- C1's real outcome is **not privacy clearance**: all194 blobs are bound,43 have
  content-reviewed decisions,151 are provenance-only, and155 dispositions remain
  unresolved. The actual gate exits1 as required. No missing worker review was
  fabricated or silently removed from the population (`content-reviews.json`,
  `evidence/content-population-final-command.json`).
- Minimized the six named r16 account-qualified location loci; r17 JjEnvFacts host
  environment/config-presence observations; r16 SourceChain runtime-location disclosure;
  r13 JSONAttack account/group observations; and the r18 dead-seat receipt's exact
  alias/payload/resume time. SW1's four reports were read and disposed by their actual
  content, not their same-wave origin (`corpus/lessons/round-19.md` residual table).
- Corrected r18 trends to unchanged/unchanged/improved, source additions to A9/B1/C5,
  four missing rejected-source Gate quotes, intrinsic old-JSON replay binding, and the
  real AXES capabilities table. Original filed report/lesson/LOG bytes were not rewritten
  (`LOG.md` round19; `SCORECARD.md` round19; lesson Gate and Mistakes).
- Opened S064/S065, retained four scoped rejections after source re-opening, and obtained
  a **Main non-author** admit/reject decision check. Main agreed S064 admit-A and S065
  reject-C; the lesson records its method and does not invent a Main URL fetch.
- Kept actual failures: malformed intermediate transport copies; first smoke's missing
  JSON import; the before counter's assumed absence, replaced by actual CLI observations.
  The original oracle was not relaxed (`finite-after.json`, corrected observed pair,
  `q13-stable-paths.json`; lesson M5/M8/M9).

### Actual parallel work and settlement

W1: **64 returned IDs**, one validated unchanged native task call;
roles executor3/reviewer44/scout8/critic3/connector3/scribe3. L1 held the frozen
planner seat. Sixteen reports remain, with8 observed provider failures,1 cancellation
and39 unreported terminal causes that are **unknown**, not successful reviews or
inferred permanent deaths (`wave1-settlement.json`, build registry).

W2: **70 returned IDs**, one validated unchanged native task call;
roles reviewer39/scout26/critic3/connector1/sentinel1. Forty-eight reports remain;
22 seats failed on provider capacity/rate limits (`wave2-settlement.json`, falsify
registry). Round total **134**, replacements0. Connector proposal seats were dispatched
but produced no completed proposal; they were not silently substituted.

Observed terminal classes: retry-budget exhaustion after5 with
`turn_rate_limit_exceeded`, HTTP429 vendor type1302, and one Haiku rate-limit response
with reported retry-after5495000ms. No failed seat was re-woken or replaced. No model,
route, account or provider configuration was changed. The later routing update applies
to fresh seats, not these captured chains.

Slot grants were `round-19-attempt2-wave1`64 at target240 and
`round-19-attempt2-wave2`70 at target240; both were released after settlement.
The erroneous parent stand-down was reversed, preserving this author and the same base;
no duplicate W1 was started. The preceding empty failed author wake was never resumed.

All round19 wave/evidence paths in this report are relative to
`.ufo/waves/round-19/` inside the mori lane unless written in full.

## Landed changes

Every row is motivated/logged in `LOG.md`'s round19 entries.

| Landed commit | Change |
|---|---|
| `5e393d20daa628a0b4ca9aa6a1626aa54285b3f0` | Original requirements, population and oracle freeze |
| `290f6c0ecda171fa50a8bb00b20c948fd37eac43` | Validated W1 payload before dispatch |
| `7d949b4d394e3b12c56b6d04793c80bd43d53458` | Routed lessons and supplementary binding counterexamples |
| `367927c56eb1a00613e1fed65e5c47245fd570b9` | Intermediate integration; malformed projection copy retained as a red control, not the final implementation |
| `7fa136f9d03b9c27667ab50487910ab299e617f2` | Validated70-item fresh falsification payload |
| `a4f79dd4dd8fedb6ab062bf53a0f4bebaa6cf42e` | Settled implementation/evidence candidate, followed by the recorded failing smoke |
| `c0fe0b230769ffba7168955f87985ec3ce08f41d` | Missing-import repair and retained actual red smoke evidence |
| `11795ac0e0a44db6549534eb1239e26353446370` | Actual-response-derived before counter; final measured code |
| `2061780117e6ca637725004897bd288d3ba7e988` | All final wave evidence, counts, outside source check, lessons, SCORECARD and LOG |

Three actual sparse writer worktrees had unique branches and observed base5e393d20.
Their source was integrated by the sole production writer. Duplicate/stale private
copies and unused timed-out checkout-creation directories are retained, not force-deleted
or presented as additional landed work (`worktree-disposition.json`). No fleet scripts,
templates, MANIFEST, driver state, sibling lane or operator configuration was edited.

## Before → after measurements

### C1 — adjacency capability: verified at its finite scope

```sh
jq -s '[.[].c1.counts.capability_absent]' .ufo/waves/round-19/evidence/finite-before-observed.json .ufo/waves/round-19/evidence/finite-after-observed.json
# [10,0]
```

Both use the same final harness at11795ac0 and original expected SHA
`c5c6c67f104ed1baa57a56bfb22728a2e871ca174a4915ff4005eb3485abe22a`.
The entering revision genuinely lacks the tool (cat-file exit128,
`evidence/entering-content-capability-absence.json`). Ten unmet capability requirements
are **not ten previous production defects**. After10/10 match.

Actual committed-population run:194/194 blobs and review rows,155
`CONTENT_REVIEW_UNRESOLVED`, exit1. This is a correct negative observation,
not a failed-clearance result disguised as green. The capability claim does not
assert that all194 content reviews are complete or that private content is absent.

### C2 — calibration provenance: verified

```sh
jq -s '[.[].c2.counts.capability_absent]' .ufo/waves/round-19/evidence/finite-before-observed.json .ufo/waves/round-19/evidence/finite-after-observed.json
# [10,0]
jq -s '[.[].c2.counts.pass]' .ufo/waves/round-19/evidence/finite-before-observed.json .ufo/waves/round-19/evidence/finite-after-observed.json
# [2,12]
```

Same measured instrument11795ac0:12/12 metadata requirements and4/4 extra
binding controls after. Before mode actually calls the old compatible/bound/invalid
variants and retains their outcomes; it no longer assigns absence solely from a phase
label. The legacy instrument bytes match the entering commit.

`evidence/c2-{before,after}-replay.json` intrinsically bind inputs to29b0dc7 and3127c3a,
respectively, with current executing-code identity separately recorded. All six original
verdict rows and totals match the untouched r18 JSON. The old raw4→0 decomposes into
**one historical r17-C3 correction plus three prospective r18 labels**, not four
historical repairs or a new round19 four-defect claim. The partial historical C3 ruling
is not converted into a universal preregistration claim
(`evidence/c2-historical-binding-wrapper.json`).

### Exercised suite and failures

The final suite ran once atc0fe0b2: content CLI selftest marker clean; freeze12/12;
retention21/21; dispatch14/14; census134/134; context31 arms. Tested script bytes are
unchanged at the final tip. The repaired counting harness alone was re-exercised in both
modes at11795ac0. Q13-style parser control is9 malformed intermediate paths→0; the
final harness additionally ran successfully on its actual delivered bytes.

The first after-smoke exited1 because the new freeze checker lacked `import json`;
its evidence remains. The initial assumed-before counter is also retained and superseded
by the observed pair. No red result, failed seat or expectation was erased.

W2's existing dispatch verifier reports1/1 bound row, `LEDGER_CLEAN`, exit0.
**W1 conformance debt:** its original custom-object/noncanonical-hash ledger is not
retroactively called conformant. Actual IDs and unchanged payload remain retained;
there was no replay to repair bookkeeping (`wave1-attempts.json`, lesson M6).

### Actual final-tip retention and out-of-metric re-sweep

After the final lane commit, without writing another lane file, I executed:

```sh
python3 tools/mori-retention-gate.py scan --repo /home/vgpnk/Projects/shokunin/mori-shokunin --rev 2061780117e6ca637725004897bd288d3ba7e988 --policy .ufo/waves/round-18/frozen/c1-policy.json --allowlist corpus/evidence/retention-allowlist.json
python3 .ufo/waves/round-19/final-sweep-recipe.py 2061780117e6ca637725004897bd288d3ba7e988
```

Final-tip results: retention exit0 `RETENTION_CLEAN`, metric0, routed0,
allowlisted86, non-author5. The original policy and allowlist bytes are unchanged,
so there is no silent allowlist/denominator cut. Old C2 JSON and all63 old source rows
are also unchanged. Final-tip stdout SHA-256: **8f5313c471feaf1437d4d4fcc505935ce324a53b121c1803fb1f80386689bfc5**.

Out-of-metric exit0, **169 blobs**: all163 retained round18 blobs plus the six named
r16 files. Matching lines: account-qualified dotpaths7, personal-document path tokens8,
session-directory identities0. Direct context inspection classified the7 as mandatory
shared RULES instructions, and the8 as7 do-not-open surface instructions plus one
generic negative example. Each of the six minimized r16 files matches0.
Final-tip stdout SHA-256: **8638036aa5fd4af2d3fd37fe06b2d474a42866cedacf2df91b2a125c34598bc3**. Its scoped rows match the committed
`evidence/out-of-metric-final-command.json` input rows; this is an actual final-tip
replay, not the old e2bfbd6 sweep before later edits.

All194 population blob hashes and the three measured scripts were separately checked
unchanged at the final tip. Token-family counts, caller-supplied expected pins,
self-attested content bases, free-form reasons and line digests do **not** establish
global privacy, authenticity or erased history. The155 unresolved dispositions remain
explicit. Original exposure/history action stays operator/kagi-owned.

## Sources & frontier

Validator command at both ends:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`.

Start, exit0 (`evidence/census-start.txt`):
```text
mori W04 S035 duplicate url raw.githubusercontent.com/systemd/systemd/cf8ebfc6159cf0b3b99aa9a0164ccb07c4c9c5af/catalog/systemd.catalog.in across scopes
mori W04 S037 duplicate url www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html across scopes
mori ok /home/vgpnk/Projects/shokunin/mori-shokunin/corpus/SOURCES.md
```
End, exit0 (`evidence/census-end-command.json`): the same two W04 notices and `mori ok`.
The source bytes are unchanged at the final tip.

Rows63→65; tiers A54/B3/C6→A55/B3/C7; statuses mined33/queued23/rejected7→
mined34/queued23/rejected8 (`evidence/source-counts.json`, exact jq counting argv and
input revisions). Added A1 (S064, none→mined), C1 (S065, none→rejected), B0.
Old status/recheck/used-by cells touched:0; all63 old row bytes were checked equal.
No frontier-ground growth is claimed for retrospective index/capability-table repairs.

Sourced claim: C2 cites S064 [git-rev-parse](https://git-scm.com/docs/git-rev-parse)
for commit resolution, not input-tree equality/publication/authenticity.
S065 [hashlib](https://docs.python.org/3/library/hashlib.html) remains rejected as sole
revision-provenance support. Gate quotes, access dates, four repaired rejected-row quotes,
source disagreements and flips are in `corpus/lessons/round-19.md`.
Main's non-author check agrees on both the new admit and reject; author-side source
reopeners are not substituted for it. No operator teaching files were found by the
explicit `corpus/lessons/operator-*.md` glob.

## Trend verdicts

- **expansion: unchanged** — no newly covered observability ground is claimed;
  retrospective rows and process capabilities are not relabeled as new knowledge growth.
- **quality: unchanged** — no complete re-verification/supersession of an older admitted
  knowledge entry is claimed. Runnable/provenance repairs do not alone prove this trend.
- **discernment: improved** — r18 disagreements became lesson-backed QUALITY57–63;
  Main's non-author S064-admit/S065-reject sample agrees. Own integration/counter failures,
  static-oracle gaps and scope breaches remain recorded, not prettified.

L1 verdicts concern the two bounded claims; independent round admission remains the
non-author closure's duty. No global privacy/no-harm certification or promotion is asserted.

## SHONEN

- [~] Decision tables, error patterns and cited checklists — `SKILL.md` registry,
  fixed population/oracle and lesson Gate; author assessment, no outside box verification.
- [~] End-to-end owned-domain observation — actual194-path negative gate and exact
  historical input-bound C2 replays, recorded in LOG/evidence.
- [~] Executable instructions without oral context — registered CLI/exit maps,
  explicit lane TMPDIR and actual command receipts.
- [ ] No cross-domain bleed — not certified: scope breaches,155 unresolved review
  dispositions and the operator/kagi history decision remain visible.

Stale-lane: this authorized round19 lineage progressed through the commits above;
the parent confirmed the mistaken alternative wake never ran. No subsequent round
or duplicate author/wave was started. Final helper state: local=remote=2061780117e6ca637725004897bd288d3ba7e988,
ahead0/behind0, tracked0/untracked0. Only the generated context-selftest fixture directory
was removed after its results were retained; no unrelated cleanup/forced worktree removal.
Misroot sweep: no pathspec, exit0, empty output, own candidates0, moves/deletions0
(`evidence/misroot-sweep.json`). Tool installs/updates: none. New L0 questions: none;
the existing exposure/history decision remains operator/kagi-owned. Scope deviations:
two critics disclosed broad searches entering retained interactive-session material;
no transcript text was copied into their reports. These are breaches, not compliance credit.

### Appendix — exact source-census output precision

The start/end summaries above are expanded here verbatim (tabs preserved).
Command at both ends:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`.

Start, exit0:
```text
mori	W04	S035 duplicate url raw.githubusercontent.com/systemd/systemd/cf8ebfc6159cf0b3b99aa9a0164ccb07c4c9c5af/catalog/systemd.catalog.in across scopes
mori	W04	S037 duplicate url www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html across scopes
mori	ok	/home/vgpnk/Projects/shokunin/mori-shokunin/corpus/SOURCES.md
```

End, exit0:
```text
mori	W04	S035 duplicate url raw.githubusercontent.com/systemd/systemd/cf8ebfc6159cf0b3b99aa9a0164ccb07c4c9c5af/catalog/systemd.catalog.in across scopes
mori	W04	S037 duplicate url www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html across scopes
mori	ok	/home/vgpnk/Projects/shokunin/mori-shokunin/corpus/SOURCES.md
```
