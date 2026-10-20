# tabi — round 12 (attempt 1), 2026-10-20

## Work performed

Declared claims: **C1 — freshness**, substantive source-claim rechecks of three named
claim families, **0→3**; **C2 — coverage**, documentation-held accessible locator / ARIA
snapshot entry, **0→1**. Initial proposed scalar increases were withdrawn after critique;
freshness remains **8**, coverage **9** (delta **0**). Counts do not establish full domain
coverage or runtime capability. Baseline: the kaika scores admitted by the outside
`tabi-shokunin/corpus/lessons/round-1-verifier-spotcheck.md:17`, not the earlier training tables.

- C1 reopened primary text and compared actual claims, not just hashes. Corrected the
  profile note's same-port address retry / approval-mode port-fallback conflation; qualified
  rolling-stable retry documentation. BiDi mappings remain specification-only.
  Evidence: `tabi-shokunin/corpus/evidence/round-12/source-recheck.json`,
  `tabi-shokunin/corpus/knowledge/source-recheck-round-12.md:14-77` and the dated appendices
  in `chrome-remote-debugging-profile-boundary.md:119-138` / `web-flake-retry-evidence.md:172-181`.
- C2 opened S023/S024/S025 and admitted the scoped note, transitioned queued→mined, indexed
  both new notes and distinguished Playwright YAML from webbridge `@e`, pixels, network
  evidence and accessibility certification. Evidence:
  `tabi-shokunin/corpus/knowledge/playwright-accessible-locators-and-snapshots.md:1-121`,
  `tabi-shokunin/SKILL.md:1631-1663`, `tabi-shokunin/corpus/README.md:201-226`.
- Mined the outside source-inference/host-observation disagreement into QUALITY14 and a
  bounded structured-record gate. Same claim/evidence/id with only modality/scope fixed:
  red exit1 `observation_without_runtime`, green exit0; isolated self-test9/9 clean.
  Evidence: `tabi-shokunin/corpus/lessons/round-12.md` §Mistakes,
  `tabi-shokunin/corpus/evidence/round-12/mistake-red.json`, `mistake-green.json`,
  `mistake-selftest.json`. This is not NLP truth verification.
- Critique was acted on: unsupported coverage9→10 withdrawn; counter restricted to the
  three exact C1 targets with committed note digests and evidence; C2 requires provenance,
  mined rows, used-by, index and lesson admission. A proposed false correction of S011's
  literal “remains unchanged” sentence was rejected by reopening it. Evidence:
  `tabi-shokunin/.ufo/waves/round-12/w1/ClaimAttack.txt`, `CoverageAttack.txt`,
  `FreshnessAttack.txt`, and the correction dossier.
- One validated **32-seat** wave, one unchanged validator `taskCall`: executor5, scout9,
  connector4, reviewer6, critic4, sentinel1, scribe2, revenger1. L1 held canonical planner;
  PlanningWalk was the bounded scout data-walk. No model argument. Evidence:
  `tabi-shokunin/.ufo/waves/round-12/w1/spec.json`, `dispatch.json`, `swarm-registry.json`.
  Absolute reportDir was refused (`invalid_report_dir`); orchestrator confirmed lane-relative
  reportDir under absolute UFO_PROJECT_ROOT is correct and fixed the prompt addendum for
  later rounds. All item/context paths named the absolute lane. No L0 question needed.

## Landed changes

**Pushed lane HEAD: `37ffbef29486ec93e004a4d3e39fdfa78006024d`** (origin/master).
Lane identity: `tabi-shokunin <tabi@shokunin.local>`. Push output:
`f032f2d..37ffbef master -> master`.

| Landed work | LOG entry | Carrying commit |
|---|---|---|
| Source rechecks, append-only corrections, new correction dossier; accessible evidence note, SOURCES/index/SKILL integration; QUALITY criteria, lesson, registered mistake gate, wave evidence and exercised checks | `tabi-shokunin/LOG.md:535-585` | `0d82098e8151ac8c1f58f55716b9f6569bd1844a` |
| Measured SCORECARD, exact committed-revision counter outputs and current index count | `tabi-shokunin/LOG.md:586-591` | `37ffbef29486ec93e004a4d3e39fdfa78006024d` |

Inherited working tree: clean at start; no inherited uncommitted lane-authored outputs to
reuse or discard. Base HEAD `f032f2d...` was protocol-authored bookkeeping, not credited
as this round's work. No operator/aggregator/outside-verifier files were edited. Seat-authored
duplicate `.md` summaries were removed by their authors; assigned evidence was retained.

**Named inherited gate debt:** the outside kaika verifier requested SHONEN rebaselining.
The old SHONEN pin conflicts with the operator-ordered canonical `[~]` regeneration at
`5cdc976`; legacy gates report `history_rewritten`. The required new `round-12.md` lesson
also matches the legacy user's overbroad round-N diff guard. The earlier user's `round_count`
6/10 defect remains behind that history check. Evidence:
`tabi-shokunin/.ufo/waves/round-12/w1/GateDebt.txt:4-53`, `ProtectedMap.txt`,
`tabi-shokunin/LOG.md:519-525`. **Decision:** carry named debt, not an untested production
exception. Orchestrator clarified lane scripts are writable; a correct repair still needs
fixture coverage of SHONEN/census/PSTACK policy. No HARD_BASELINE/PSTACK_PIN moves, old
fixture edits, SHONEN rollback or gate weakening. Legacy gates were **not re-run** this
round; no pass is claimed. New source/mistake checks do not clear that debt.

## Before → after measurements

Measured content revision **`0d82098e8151ac8c1f58f55716b9f6569bd1844a`**; final lane HEAD
adds only measured scorecard/index/log bookkeeping and the receipt. Both named revision
measurements exited0:

```sh
node .ufo/waves/round-12/measure.mjs f032f2dccc8a99632eea52edafa8220284b5c919
node .ufo/waves/round-12/measure.mjs 0d82098e8151ac8c1f58f55716b9f6569bd1844a
```

```json
{"revision":"f032f2dccc8a99632eea52edafa8220284b5c919","source_rechecks":0,"accessible_locator_entry":0}
{"revision":"0d82098e8151ac8c1f58f55716b9f6569bd1844a","source_rechecks":3,"accessible_locator_entry":1}
```

- **C1 freshness: improved**, bounded source-claim rechecks0→3; two discrepancies corrected
  or qualified, one family confirmed. No full-note freshness claim for unreviewed paper,
  abstract, WPT or host-runtime material. Original/after note SHA256 values are pinned.
- **C2 coverage: improved**, docs-held entry0→1 with mined citations and map/lesson
  admission. Not a complete-province fraction; Playwright runtime remains unmeasured.
- depth, operability, calibration, adjacency: **unchanged claimed axes**. Source gate and
  bounded mistake witness passed, historical gate debt remains named; no global no-harm
  certification or independent admission is fabricated. Scalars remain8/9/8/8/9/8 in
  depth/coverage/operability/freshness/calibration/adjacency order.

Exact commands/stdout and index counter:
`tabi-shokunin/corpus/evidence/round-12/measurements.json`.
Index output `{"knowledge_notes":31,"mapped":31,"missing":[]}`, exit0.
Counter is a counting probe, not a source-truth gate.

Exercised once after all seats landed:
- `node .ufo/waves/round-12/w1/mistake/check-claim-record.mjs --file fixtures/m2-observation-source-only.jsonl`: exit1, expected `observation_without_runtime`.
- Same entry with `--file fixtures/m2-inference-source-scoped.jsonl`: exit0, clean.
- Same entry with `--self-test`: exit0, `CLAIM_SELFTEST verdict=clean cases=9/9`.
- `node scripts/check-sources.mjs --self-test`: exit0, `SOURCES_SELFTEST verdict=clean cases=26`.
- `node scripts/check-sources.mjs`: exit0, 28rows / no findings.
Receipts: `tabi-shokunin/corpus/evidence/round-12/`. No browser/runner smoke or legacy-gate
pass is asserted. Admission remains pending the orchestrator's non-author closure.

## Sources & frontier

Required census command (from fleet root), **start and end**, both exit0:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi
```

Both outputs:
```text
tabi	ok	/home/vgpnk/Projects/shokunin/tabi-shokunin/corpus/SOURCES.md
```
Start: `tabi-shokunin/.ufo/waves/round-12/w1/census-before.txt`.
End: `tabi-shokunin/corpus/evidence/round-12/census-after.json`.

Committed source counting command (run in lane root; exit0):
```sh
node -e "const{execFileSync:g}=require('node:child_process');for(const rev of process.argv.slice(1)){const rows=g('git',['show',rev+':corpus/SOURCES.md'],{encoding:'utf8'}).split('\\n').filter(x=>/^\\| S[0-9]{3,} \\|/.test(x)).map(x=>x.split('|').map(y=>y.trim()));const hist=i=>Object.fromEntries([...new Set(rows.map(r=>r[i]))].sort().map(k=>[k,rows.filter(r=>r[i]===k).length]));console.log(JSON.stringify({revision:rev,rows:rows.length,tier:hist(4),status:hist(8)}));}" f032f2dccc8a99632eea52edafa8220284b5c919 37ffbef29486ec93e004a4d3e39fdfa78006024d
```
```json
{"revision":"f032f2dccc8a99632eea52edafa8220284b5c919","rows":28,"tier":{"A":22,"B":4,"C":2},"status":{"mined":20,"queued":6,"rejected":2}}
{"revision":"37ffbef29486ec93e004a4d3e39fdfa78006024d","rows":28,"tier":{"A":22,"B":4,"C":2},"status":{"mined":23,"queued":3,"rejected":2}}
```

Rows28→28; added by tier **A0/B0/C0**. Touched fields, exact old→new in the lesson:
S023/S024/S025 status queued→mined and used-by `—`→accessible note; S011/S013/S017/S028
used-by adds the correction dossier. No immutable row, original opened date or cadence
changed. All re-open dates/URLs/located ≤25-word quotes are in `round-12.md` §Gate.
No new registry row was claimed merely from a lead. Existing rejected S026/S027 remain.

Frontier advanced: accessible-selectors open→**docs-held**, not runtime-held. Extension↔daemon
handshake, native WebMCP probe, real-site rate/rights records, real-site journeys and WebMCP
spec mining remain open. This was bounded source reopening, not an exhaustive discovery
search. S018/S019 and implementation/runtime data remain outside C1's new dates.

Mistake/failure evidence: source-inference overclaim (outside kaika disagreement) now has
criterion14 and observed red/green fixtures; actual socket-factory attribution corrected.
QUALITY15 repairs the contract-tier pointer without claiming a separate measured fix.
Dispatched lane seats are not outside verifiers. Latest actual outside lesson was
`round-1-verifier-spotcheck.md`; no round-11-verifier file was in the initial lesson census.

## Trend verdicts

- **expansion: improved** — accessible-selector ground previously queued now has a sourced,
  indexed docs-held entry citing mined S023/S024/S025; the counter excludes the correction
  dossier from C2. Evidence: new entry, README round12 and measurements.json.
- **quality: improved** — a false factory attribution is explicitly superseded, rolling
  stable version scope qualified, and source claims rechecked against text rather than
  digest equality alone. False critic correction rejected. Evidence: source-recheck dossier
  and appended note errata. Unreviewed claims were not silently redated.
- **discernment: unchanged** — earlier outside disagreement becomes a lesson-backed rule
  and failure witness, but this round's admit/reject sample still awaits an actual outside
  reviewer. No same-lane reviewer is counted as non-author; no new outside agreement claimed.

## SHONEN

- [~] Real decision tables/error patterns/checklists/cited sources: existing SKILL plus
  `SKILL.md:1631-1663`; author assertion, no new non-author verifier.
- [~] End-to-end domain task executed/logged: historical `knowledge/multi-step-journey.md`
  §§1–2,7 and LOG round3. This round was source work, not a new browser execution.
- [~] Instructions executable without oral context: historical
  `knowledge/executor-test-sufficiency.md` §§0,4; the new structured-record witness ran,
  but does not independently certify the whole skill.
- [~] No cross-domain bleed: `PROVINCE.md:3-19`; no publishing, secret handling, forensic
  work or accessibility certification absorbed. No SHONEN `[x]` or promotion claim.

Stale-lane: respawn-per-round; this was the sole tabi mission, no other open tabi mission
known. This report lands last after pushed lane work. Existing L0 questions remain the
round5 operator-approval request and round1 namespace/dispatch wording; no new L0 question.
Tool installs/updates: **none**. No consequential external action, browser launch, profile
access or upstream source-tree write.
