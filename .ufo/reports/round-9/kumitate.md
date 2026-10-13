# kumitate — round 9 of ≤1024 (fleet-2)

**Lane:** kumitate-shokunin · **cwd** `/home/vgpnk/projects/shokunin/kumitate-shokunin`
**Axes:** operability + coverage (orchestration/tooling).
**Round move:** one axis-move, operability. **Score 2 → 6** on the frozen proxy.
**Repo commit:** `d65aa24` (`round-9`), pushed to
`github.com/VeigaPunk/kumitate-shokunin` (`31f09cd..d65aa24`).

## Axis-move and measurement

Frozen proxy since round 8 (`SCORECARD.md`): `f_O = (A + C) / (A + C + 3)`,
score `= floor(10 × f_O)`.

| Term | Before (r8 close) | After (r9) | Command |
|---|---|---|---|
| A — runnable artifacts with documented invocation + verdict exit | 1 | **2** | `scripts/cite-check.mjs`, `scripts/surface-probe.mjs` |
| C — `SKILL.md` GFM task items naming a runnable command | 0 | **4** | `grep -c '^\s*- \[' SKILL.md` → 4 |
| `f_O` ⇒ score | 1/4 ⇒ 2 | **6/9 ⇒ 6** | `floor(10 × 0.667)` |

The C term is not a list: all four items are *executed* —
`node scripts/surface-probe.mjs --checklists` → `CHECKLIST: 4/4 pass`,
`VERDICT: PASS`, exit 0 (each item names a command, an accepted exit set and an
expected verdict substring; a miss fails the item).

Coverage was re-measured as bookkeeping only (the axis stays 7): C2 README-map
rows/files **31/31 → 34/34** (rows added for the new note, this round's lesson,
and the previously unrowed third-party `lessons/round-6-aggregator-audit.md`);
file-level residue **105/211 → 140/211 ≈ 0.664**; C1 unchanged 14/18.

## What landed

1. **`scripts/surface-probe.mjs`** (new, 1438 L, zero deps, ESM, node ≥20,
   contract `kumitate-surface-probe-v1`, sha256 `86bdcd9a…` at acceptance) — a
   read-only conformance probe over two live surfaces this province documents
   but could not previously execute: `bash scripts/ufo-sighting surface --json`
   and `node scripts/fleet-dispatcher.mjs status`. 12 checks:
   `SURFACE_REACH MANIFEST_PARSE MANIFEST_KIND DIGEST_INPUT_SET DIGEST_PER_FILE
   DIGEST_CONCAT VERB_DISPATCH ERROR_CODES PIN_DIGEST STATUS_REACH STATUS_SHAPE
   STATUS_QUEUE_SCHEMA`. 21 finding codes; 38 hermetic fixtures; `--json`,
   `--strict` (non-gating warns disclosed), `--checklists`; exit 0/1/2/64.
   Live: `SURFACE_PROBE: CLEAN (surfaces=2 checks=12 errors=0 warnings=1)`,
   exit 0, 0.19 s. `--selftest`: 38/38, exit 0, 0.35 s.
2. **`scripts/cite-check.mjs` — suite split.** `--selftest` is now hermetic:
   **19/19, `VERDICT: PASS`, exit 0, 0.076 s**, including under
   `--src /nonexistent --self /nonexistent`. Live-tree assertions moved behind
   `--integrations` (exit 1, the same findings named); `--selftest
   --integrations` runs both. The live block is now gated on
   `opts.integrations` (`scripts/cite-check.mjs:1493-1504`).
3. **`SKILL.md`** — `## Verifiable checklist` (4 executable items) plus a
   Working-rules bullet for the new gate, including the two-digest trap.
4. **Docs** — `corpus/knowledge/live-surface-probe.md` (new),
   `corpus/lessons/round-9.md` (new), `corpus/README.md` rows, `SCORECARD.md`,
   `LOG.md`.
5. **Doc drift repaired** (found by an L2 scout, verified by L1):
   `maybeEnqueueIterationSuccessor` is at
   `scripts/fleet-dispatcher.mjs:6753-7215`, not `~L6743-7150` — corrected in
   `SKILL.md:114`, `corpus/knowledge/successor-chain.md:3` and `:93`,
   `corpus/knowledge/queue-and-claim.md:4`, `corpus/README.md:21`.

## Two defects were already live at round open — both this lane's

- **The gate failed its own suite.** `--selftest` → `27/28`, `VERDICT: FAIL`,
  because case 21 asserted *live repo doc state* broken by a sibling lane's
  `corpus/lessons/round-6-aggregator-audit.md:23`. A hermetic suite breakable by
  a third party's prose is not a gate.
- **`--selftest` still did live work** even after the split: the planner lane
  read `scripts/cite-check.mjs:1493` and showed the live `runCheck` ran
  unconditionally and was merely filtered from the emitted groups. Fixed by
  gating it; independently re-verified by that lane ("`--selftest` alone skips
  the integration work") and by L1's hostile-config runs.

## Claim falsified inside the round (kept as calibration evidence)

Opening recon called `config/ufo.json:65`'s `sighting.surfaceDigest` *stale* by
comparing it to `manifest.scriptDigest`. That was a category error, and two L2
lanes repeated it from the brief before it was caught. Measured truth:

- pin = `sha256(canonicalJson(manifest))` (`scripts/sync-ufo-contracts.mjs:853-862`)
  = `sha256:de50bca59b159cbd77029bf6e26d1bf26762c9849fc6b89fa2fba572995fc099`
  = the pin ⇒ **match**; the origin's own gating leg agrees
  (`scripts/sync-ufo-contracts.mjs:941`, outcome `match`).
- `manifest.scriptDigest` = sha256 over concatenated file bytes
  (`scripts/ufo-sighting-lib/surface.mjs:43-58`) =
  `sha256:0e98c908bb8dc52353716852b5451605ad5889c98b7bc620fceebd7797725567`,
  recomputable.
- Manifest stdout is **18826 bytes** (18818 was a UTF-16 `String.length`; md5
  `8ed7ef0a…`, byte-identical via shim and module).

The probe encodes the two-function distinction and never compares the pin to
`scriptDigest`.

## L2 concurrency — 10 lanes, one batched dispatch

Route buckets as specified: planner/connector `@m_lunamax`; executor/scribe/scout
`@m_flash`; critic/reviewer/sentinel `@m_zfl`.

| Lane | Role | Delivered |
|---|---|---|
| RoundSpec | planner | `/tmp/kumitate-r9/spec.md` — shipped CLI/modes/exit policy, 21 finding codes with fixture coverage, fixture-tree design, proxy arithmetic + falsifier; caught the non-hermetic `--selftest` block in source; `SPEC_SMOKE: PASS finding-codes=21 checklist-lines=4` |
| SurfaceCensus | scout | verb/error/digest/caps census: 17 = 17 under a 3-rule classification (`trigger-alias` dispatches via `resolveTrigger` at `scripts/ufo-sighting.mjs:64`; `--help`/`-h` at `:331`; `__idle`/`__pane-run`/`__reconcile` internal), 79 = 79 `fail()` codes, 28 = 2 + 26 digest inputs, recomputed digest == manifest |
| DocClaimCensus | scout | 147 literal rows across `SKILL.md:64-150`, `sighting-wall.md`, `queue-summary.md`, `queue-and-claim.md`; none false; found the `L6743` drift and the 4 off-manifest `code:` literals; repeated the digest category error (recorded) |
| ProbeImpl | executor | the artifact + acceptance record (default/`--selftest`/`--json`/exits), hermeticity proof, both digests, 18826 bytes |
| CiteCheckHermetic | executor | the hermetic/integration split, classification table (19 hermetic / 9 integration), diff scoped to header/USAGE/parseArgs/selfTest/main |
| SkillChecklist | scribe | `## Verifiable checklist` draft (grammar-exact) + the 210-line corpus note; `CHECKLIST: 4/4 pass` |
| ClaimCritic | critic | attack on read-only reachability, self-referential checks, suite split, C-term and the pin claim |
| CitationReviewer | reviewer | cite audit over the round's artifacts |
| ReadOnlySentinel | sentinel | 85,365-file before/after snapshot: 31 named files byte/size/mtime identical, no lock, no tmux change, origin HEAD `ee907f1cf`; sole delta ambient `NODE_COMPILE_CACHE` churn (one cache file, size unchanged; `env -u NODE_COMPILE_CACHE` control byte-identical) |
| OverlapConnector | connector | ownership map: freshness/calibration belong to kake/kagi/kengaku; origin pins owned by the origin tree; the third-party artifact owned by the aggregator lane |

L1 re-measured every claim that mattered and falsified two lane errors before
they reached a document (the digest category error above; an interim probe
revision whose `--selftest` took 91 s and read 32/35).

## Evidence (round close)

```
node scripts/cite-check.mjs            → CITE_CHECK: DRIFT (files=36 tokens=2324 errors=2 warnings=52)  exit 1
node scripts/cite-check.mjs --selftest → 19/19 cases passed (hermetic) / VERDICT: PASS                  exit 0
node scripts/cite-check.mjs --integrations → VERDICT: FAIL (live-tree assertions, third-party rows)     exit 1
node scripts/surface-probe.mjs         → SURFACE_PROBE: CLEAN (surfaces=2 checks=12 errors=0 warnings=1) exit 0
node scripts/surface-probe.mjs --selftest  → 38/38 cases passed / VERDICT: PASS                         exit 0
node scripts/surface-probe.mjs --checklists → CHECKLIST: 4/4 pass / VERDICT: PASS                       exit 0
```

Both `errors=2` sit inside the aggregator-owned
`corpus/lessons/round-6-aggregator-audit.md` (`:23` and `:116`, LINE_OOR
`native_contract.rs:10896`) — a *quotation* of a finding is itself a finding;
no quotation exemption exists or was added. The two dangling
`corpus/lessons/round-9.md` pointers that artifact carries resolved implicitly
because this round ships that lesson.

## Cross-domain (reported, never absorbed)

- Aggregator lane owns its audit artifact's ERROR rows (it committed twice into
  this repo during the round: `0ac2272`, `31f09cd`).
- Origin tree owns `crates/ufo-core-runtime/bundled/omp-seat-routing.json`
  routes-equivalence drift (`sync-ufo-contracts.mjs --check` exit 1, ownerLane
  `nc8-runtime`) and the hit the probe reports as `PIN_DRIFT`-class evidence
  only — the pin itself matches.
- Origin tree grew during the round (`scripts/*/` 41 → 42 members); its two
  pre-existing dirty files are untouched.
- `fleets/registry.json` lane→model routing dispute and the `membrane-seal
  write` argv defect remain as previously filed.

## Residuals / limits (recorded, not hidden)

- `--selftest` no longer measures the repo; `--integrations` does, and it is red
  for third-party content, not for this lane's tooling.
- The probe covers **2 live surfaces of 18 registry families**; S6, S7, R10,
  R11 remain uncovered families and ~34% of in-scope source files are uncited.
- `--checklists` executes `bash -c` on `SKILL.md` task lines by design (opt-in;
  the sentinel audited it as the only arbitrary-shell surface).
- No CI or schedule: every gate here is on-demand.

## Next planned move (round 10)

Operability is still the lowest axis (6). Two candidate moves, decided on
evidence at round open, with the honest scoring consequence stated in
`SCORECARD.md`: (a) probe a third live surface — raises no proxy term, so
operability saturates at 6 until the proxy is re-chartered with a
surface/`checks` term; or (b) widen the executable checklist to the fleet-round
gates (corpus gate, report lands, commit + push), which moves C and therefore
`f_O` again.

## L0 side channel

No operator decision was needed this round; nothing was appended to
`.ufo/l0-questions.md`.