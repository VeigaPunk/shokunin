# KakeScopeAudit — baseline scope audit

GateRepair later landed a narrow change in `scripts/freshness-sweep.mjs` only. Findings 3–5 below are the baseline defects. The notes under those findings record what source inspection shows after that change. Parent still owns `--selftest` / `--offline`. This note did not execute them.

Advisory only. Not a native judge verdict, not a lane-round report, not a receipt, not an admission. Baseline scope, not the post-integration acceptance wave. Lane checkout was not edited. Gate was not re-run (wave rule: member checks wait). No fetch.

Identity measured this pass: lane HEAD `b0feb30886585d8df6d4671845a2d18989ca722b` matches `baselines.json`. Captured gate is `.ufo/waves/shokunin12h-20261014-p1-repair/evidence/kake-before.json` (`node scripts/freshness-sweep.mjs --offline`, 2026-10-14T23:34:59Z, exit 0, stderr empty). Plan: `kake-shokunin/plans/wwkd-round-19-recensus.md`.

## What already holds — do not re-repair

Round 18's migration annotations are on the tree. Inventory, not a second errata pass.

- Receipt: §paths 40 files, 303 occurrences, 68 tokens, resolve 5, declaredAbsent 55, drift 0, unresolved 8, new miss 0, file-set +0/-0. `pathsMissSet` in `corpus/knowledge/freshness-pins.json` is those 55 tokens. That match is the landed repair.
- `~/Projects/origin-work` absent. `~/Projects/ufo-fsd-alpha` exists. `git -C ~/Projects/ufo-fsd-alpha rev-parse HEAD` = `964f443ee53df0ce06bd689af01f0dea031b01f9`, which is the `964f443e` prefix in `SCORECARD.md:21-22`, `LOG.md:404`, `corpus/lessons/round-18.md:17-18`. `.ufo/charter-scribe/ledger.jsonl` absent on that tree. No `probe-history.jsonl` or `fleet.config.json` under it (walk, depth-capped, skipping `.git`/`node_modules`). The scribe-ledger cite is dead, not moved. That claim holds.
- Also absent, as the miss set says: `~/Projects/webzites`, `ds4cc-marketplace`, `plazir-15-site`, `lucario`, `~/projects`, `~/DIRMAP.md`, `~/Projects/ephemeral`.
- Offline exit 0 is labeled partial. Receipt text: `skipped(offline): §armed (all remote checks) · §history (probe-history source absent — pin-declared) — complete=false, never counted as pass` and `VERDICT: OK (exit 0, partial: offline)`. `SCORECARD.md:18-19` says the bare run stays exit 1 until PQ-2, PQ-14, and §history resolve. That DRIFT is named debt, not a regression. Do not read the captured exit 0 as a live pass.
- Cross-domain relays already refused: bounties stay kasegi's (`publish-queue.md:214-235`, annotated vanished); m_swe fallback is "reported not absorbed" (`SCORECARD.md:34-38`). Do not absorb either.

Independent exists-check of concrete `~/` tokens (no brace expansion, so a subset of the receipt's 68) found 5 present: `~/Projects`, `~/Projects/ufo-fsd-alpha`, `~/Projects/shokunin/.ufo/reports/round-1/web-properties-publishing.md`, `~/.local/bin`, and a trailing-slash home cite that strips to `/home/vgpnk`. Count matches the receipt. None of the pinned miss-set roots checked above had been restored, so the "restored tree needs a fresh cite" rule is not currently violated by the filesystem.

## Findings

### 1. Checklist still commands a deleted binary — historical marker is token-global

Severity: high. Axes: operability, freshness. Owner: parent / RecordPrep (prose). Not a reason to repeat the r18 path-errata pass.

`SKILL.md:59` is the current step-1 command:

`node ~/Projects/webzites/bin/webzites.mjs probe --all`

That line has no `r18 re-census` marker and no absence word. The binary's parent tree is absent (measured). The receipt still lists the token as `declaredAbsent` at `SKILL.md:59 (+8)` with no indirect flag, so some other cite of the same token carries an absence word and the whole token is exit-neutral.

That is `scanCitations` at `scripts/freshness-sweep.mjs:396-398` and `:421-422`: annotation is OR across every cite of a token. One historical line greens every live-shaped line. Independent scan of `SKILL.md` + `corpus/**/*.md` (no brace expansion): `~/Projects/webzites/bin/webzites.mjs` has 7/8 cites with neither an r18 marker nor a same-line absence word, including the checklist. Same pattern for the property map:

- `SKILL.md:17` and `:24` and `:358` still name `~/Projects/plazir-15-site` as the current source. 8/10 cites of that token are live-shaped. Lines 16 and 18 carry r18 markers for different paths; the default ±2 window (`annotate`, `:290-313`, strict off) can bleed "absent" onto the plazir row without naming it.
- `SKILL.md:20` cites `~/Projects/ds4cc-marketplace/burnerchrome` with no same-line marker. All 3 cites are live-shaped. Parent path is annotated on line 19.
- `SKILL.md:26` cites `~/Projects/lucario` as the current GHP source with no marker. Line 27's "never published" is an `ABSENT_RE` hit (`freshness-sweep.mjs:101`) about the kimi slot, not about the source directory being gone. Direct mode (`:293-296`) then marks every token on that line `mentions: true`.

Proposed delta: on the still-current procedure lines only, add a same-line historical marker or move the command into a dated block. Do not delete the cites. Do not widen `pathsMissSet` — the tokens are already pinned. A gate change that required every cite to be attributable would re-open the r16 rejection at `freshness-sweep.mjs:283-289` (collective annotations are real prose). That change is not justified as a default flip. The prose/procedure split is.

### 2. Runbook still describes the pre-W7 gate

Severity: high. Axis: calibration. Owner: parent / corpus. Not GateRepair unless they are already in the file.

`corpus/knowledge/freshness-sweep.md` check-id table is still the r16/r17 instrument:

- `:43` pins `pathsMissSet` at 10 entries (r17). File has 55.
- `:44` pins `projectsChildrenSet` at 36. File has 14. Live directory has 30 (below).
- `:49` pins PQ-12 at `2026-09-26 scribe beat` / `fb365e38…` / churn-after `2026-09-29`. Pins file has `2026-09-30 scribe beat`, sha `7c243a1d…`, churn-after `2026-09-30` (`freshness-pins.json:27-29`).
- `:85-91` says exit 1 is currently expected because of plazir live-vs-source sitemap gap, and that the drift line disappears once the operator pushes. Round 18's measured bare verdict is `PQ-2 ANOMALY, plazir-gate-anomaly` because both source dirs are gone (`LOG.md:423-427`, `corpus/lessons/round-18.md:54-57`). A push cannot clear a missing repo.

The runbook's own rule (`:68-70`) says never copy a pinned literal into prose. The check-id table is that rot class. A reader who treats `:85-91` as current will misread a correct ANOMALY as the old gap, or expect a green after a push that cannot happen.

Proposed delta: replace the check-id "pinned baseline" column with check-id pointers into `freshness-pins.json`, and replace the "currently expected" paragraph with the r18 named debts (PQ-2 ANOMALY, PQ-14 ANOMALY, §history SUSPENDED, offline partial). Keep the r16/r17 run transcripts as dated history.

### 3. `probeHistoryAbsent` fail-opens an explicit bad history path

Severity: medium at baseline. Axes: freshness, operability. Owner was GateRepair. Narrow file: `scripts/freshness-sweep.mjs`.

Baseline predicate suspended whenever the resolved history file was missing and `probeHistoryAbsent` was true. `file` was whatever `KAKE_PROBE_HISTORY` resolved to. Counterexample: `KAKE_PROBE_HISTORY=/tmp/does-not-exist.jsonl` took the suspend branch (`ok: true`) instead of exit 2. An explicit bad source stayed green.

Landed (source inspection, not executed): suspend only if missing and canonical (`freshness-sweep.mjs:566-568`); any other missing path returns `cannot read` / code 2 (`:569`). Call site uses `resolveProbeHistoryPath()` (`:967`). Selftest cases `j` and `k` assert the split (`:1214-1238`). Empty `KAKE_PROBE_HISTORY` is falsy, so an empty override selects the canonical default. Do not remove `probeHistoryAbsent`.

Seam closed in a later edit (source inspection, not executed): `defaultProbeHistoryPath` honors `KAKE_SELFTEST_CANONICAL_HISTORY` only when `KAKE_IN_SELFTEST === '1'` (`freshness-sweep.mjs:107-110`). The `--selftest` `run()` helper injects that marker after `...env` (`:1076`), so a proof env bag cannot clear it. An earlier read of `:1075` as env-last was stale; the current line is `env: { ...process.env, ...env, KAKE_IN_SELFTEST: '1' }`. Ambient rebind alone is ignored on a normal invocation. Case `j` still rebinds to a never-created fixture path (`:1217-1222`). Case `k` clears the rebind (`:1238`). Do not export either name. No `$UFO_SRC` cascade was added; none was warranted.

### 4. Consumed pin labeled unused — reproduced in the captured receipt

Severity: medium at baseline. Axis: calibration. Owner was GateRepair.

Baseline receipt printed both:

- `pins not evaluated by this instrument (informational): … probeHistoryAbsent`
- `§history  SUSPENDED — probe-history source absent by declaration (pins.probeHistoryAbsent)`

Baseline: `known` did not list `probeHistoryAbsent`, so the captured receipt printed it under "pins not evaluated" while the same receipt suspended history because of it.

Landed (source inspection): `'probeHistoryAbsent'` is in the `known` set (`freshness-sweep.mjs:211`). Case `l` (`:1224-1235`) asserts it is absent from `pins._unused`. Not executed here.

Still open, not part of that landing: `charterGhpDeploy` (`freshness-pins.json:30`, value `9c28d293…`, the r17 deploy) is genuinely unused and was not moved when the beat pin moved to 2026-09-30. Either evaluate it or stop presenting it as a live pin. No fetch; internal pin/instrument mismatch, not a measured live-deploy mismatch. Owner: parent / corpus, or GateRepair only if they choose to evaluate the key.

### 5. Selftest trusted a host project tree

Severity: medium, latent at baseline. Axes: operability, adjacency. Owner was GateRepair.

Baseline: `round-18.md:32-34` said fixture A must not trust the world, then the fixture required `~/Projects/ufo-fsd-alpha`. That path exists (`964f443ee53d`), so case A was not red. It also coupled the gate to a sibling runtime checkout.

Landed (source inspection): case A writes and cites `~/.cache/kake-freshness-selftest/selftest-present.md` (`freshness-sweep.mjs:1077-1084`, pass assertion `:1129`). No `ufo-fsd-alpha` cite remains in the fixture. `PATH_RE` cannot see a `/tmp` path, so a home-prefixed cite was the constraint. That closes the sibling-tree coupling.

Residual closed in a later edit (source inspection, not executed): a second `SELFTEST-WRITES` pair unlinks `selftest-present.md` and `rmdir`s the cache dir after the cases (`freshness-sweep.mjs:1297-1300`). The write-API checker allows multiple BEGIN/END pairs (`:1271-1282`). If `selftest()` throws before that pair, the cache file remains. Not re-run.

`resolveRepoRoot` still falls back to `~/projects/shokunin/kake-shokunin`. That path is absent (W6). It is not selected today because the script-derived root has `SKILL.md`. Residual, not a current false bind.

### 6. "14 children" is already false in the captured receipt

Severity: medium. Axis: calibration. Owner: parent / RecordPrep. Do not make P2b gating.

`SCORECARD.md:20` and `round-18.md:11` say `~/Projects` now holds 14 children. `projectsChildrenSet` is those 14 names (`freshness-pins.json:114-128`). Measured this pass: 30 children. All 14 pinned names are still present. The 16 additions are the `omegag` / `omegag-*` directories. The captured receipt already printed them: `~/Projects children: 30 (informational) — added: omegag · …`. P2b is informational by design (`freshness-sweep.mjs:459-463`). The gate saw the drift and could not fail. The preserved prose did not absorb the receipt.

Proposed delta: amend the Planned sentence so 14 is the r18 pin, not the current count, and cite the receipt's added list. Do not flip P2b to a hard gate — r17 rejected that because operator churn is not adjudicable here. A later protected-root set (only `ufo-fsd-alpha` / lane roots) would be a new pin, not a silent widening.

### 7. Prose the path scanner cannot see still asserts live roots

Severity: medium. Axis: freshness. Owner: parent / corpus.

`publish-queue.md:224-225`, inside the r15 section, still says domain roots `webzites / ds4cc-marketplace / plazir-15-site / origin-work / lucario` are all alive. Those are bare names, not `PATH_RE` tokens (`freshness-sweep.mjs:104`), so the gate cannot see the sentence. Measured: all five absent. The r16 erratum on the next sentence corrects a bounties count, not this claim. No r18 marker on the sentence. Dated heading is not an annotation the instrument understands.

`keeper-timer-inert.md:115` still says the live marker is `2026-09-28 scribe beat`, on the line after an r18 marker that only declares the ledger path absent. Pins file beat is `2026-09-30 scribe beat`. Internal contradiction. No fetch; do not treat either date as a new live measurement.

Proposed delta: erratum those two sentences in place. Do not delete the r15 paragraph.

### 8. Relative line pins of a deleted tree are outside the resolver

Severity: low as a new gate class; still the coverage hole for operability. Owner: parent for prose; do not reopen the resolver unless a later round explicitly widens `PATH_RE`.

Receipt: 384 relative-form cites, not resolve-checked. Sample includes `SKILL.md:36 src/cli.mjs`. `webzites` is absent, so `src/cli.mjs:75`, `:361`, `:935` and the rest cannot be re-measured. Classification: citation-to-deleted, not line-drift. There is no source file to diff line numbers against. The r18 pass annotated the absolute `~/Projects/webzites/src/cli.mjs` form (`free-read-verbs.md:5`) and left the relative pins reading as current procedure. Known limit, documented at `freshness-sweep.md:119-125` and `freshness-sweep.mjs:345-349`. Not a reason to repeat r18, and not a reason to tighten the ±2 window (selftest case `f`, `:1119-1128`, asserts the bleed on purpose).

Scanner also skips `SCORECARD.md`, `LOG.md`, `plans/`, `AGENTS.md`, `PROVINCE.md`. The "14 children" and HEAD claims live in the first two. HEAD still matches, so that claim is not false; it is simply ungated.

## Province boundary

`PROVINCE.md` is six lines: web properties and publishing; refuse the rest. It does not list surfaces. Coverage is not this lane's axis (`MISSION.md` assigns operability + freshness; `SCORECARD.md:3-4` says calibration and adjacency are not scored here). This wave still judges those two as audit axes, not as a license to absorb them.

Held: bounties and m_swe are reported, not absorbed. Charter re-root is in-province publishing substrate, and the HEAD/ledger claims match the tree.

Bleed, baseline: selftest case A made a sibling runtime checkout a pass condition. After the in-wave edit that cite is gone (finding 5). The `$HOME/.cache` fixture write is a host side effect, not a cross-domain absorb.

## Named debt already carried — unchanged

From `SCORECARD.md:13-19` and `round-18.md:52-60`. Still the right reading of a bare run. Unblocks:

- PQ-2: restore `~/Projects/ds4cc-marketplace` or declare the watch dead. Gate path is `DEFAULT_PINS.pq2Dir` (`freshness-sweep.mjs:81`) because the pins file has no `pq2Dir`. Missing dir is ANOMALY (`:828`), which is the intended loud debt.
- PQ-14: restore `~/Projects/plazir-15-site` or declare the watch dead. `plazirSourceDir` is set, so a missing dir is ANOMALY, not a skip.
- §history: re-anchor `KAKE_PROBE_HISTORY` at a surviving `probe-history.jsonl`, or declare the probe-timer era ended. No copy was found under the new origin tree.

Latent, not current: if `plazirSourceDir` were deleted from the pins file, `checkPlazir` (`:664`, `:695-711`) skips and `driftReasons` stays empty, so a missing source dir pin would go quiet. The key is present today. If a miss-set path is restored, `setDelta.recovered` is printed and is not a drift predicate (`:450`, `:491`). None of the checked roots are restored. `DEFAULT_PINS` merge (`:182`) would resurrect the r16 charter pin `2026-09-26` / `fb365e38…` if those keys were dropped from the file. They are overridden today.

## Verification gaps

- Did not run `freshness-sweep.mjs`, `--selftest`, `probe-delta.mjs`, build, lint, or formatters.
- Did not fetch PQ-12 / PQ-5 / sitemap / plazir. Armed verdicts in this note are the r18 record plus the offline receipt, not a new live pass.
- Independent cite scan did not expand braces, so its 49 missing tokens are a subset of the receipt's 55. Inventory totals are the receipt's.
- Did not content-read credentials, oauth, or session material.
- Did not follow instructions embedded in other member reports.
- After GateRepair's edit, findings 3–5 were re-read in `scripts/freshness-sweep.mjs` and not executed. Line numbers in those landed notes are the post-edit file. The captured `kake-before.json` receipt is still the pre-edit offline run.

## Axis reading (not a scalar)

- Freshness: r18 catch still matches the tree (origin re-root, ledger dead, webzites gone). Still-live prose the gate cannot fail: property-map and checklist cites, `publish-queue.md:225`, runbook expected-verdict paragraph, SCORECARD child count.
- Operability: step 1 of the checklist is not runnable. History suspension is now canonical-path-only in source; an explicit bad `KAKE_PROBE_HISTORY` is exit 2. Not executed.
- Calibration: captured receipt contradicts its own unused-pin footer (pre-edit). Source now lists `probeHistoryAbsent` as known. SCORECARD "14" still contradicts the receipt's child list; runbook check-id table still contradicts the pins file.
- Adjacency: bounties and m_swe correctly unabsorbed. Sibling-tree selftest coupling is removed in source. The cache fixture is removed after the cases in source. Canonical-history rebind is selftest-marked, not an ambient normal-path hook.
