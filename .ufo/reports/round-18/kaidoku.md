# kaidoku — round 18 report (hyaku phase 2, attempt 1)

Lane repo `kaidoku-shokunin`, branch `main`. Baseline `9011581d84527ba34c675f9cf912e54d2e72d470` (r17 verifier spot-check). Delivered lane tip **`a245bb00c581ae3423a10a055c77d4bc873918df`** (every hash below was printed by `scripts/hyaku/jj-lane.sh` as `landed <hash>`; `git ls-remote origin refs/heads/main` showed the tip before this report). Launch `2026-10-20T12:07:53-03:00 launch kaidoku round=18 pgid=4070059 driver=hyaku-inline attempt=1`; no `lane-dead-no-report kaidoku round=18` line, so nothing inherited. The session paused once on an Anthropic 429 (orchestrator recovery steer) and resumed under the same identity.

## Work performed

Declared claims (`kaidoku-shokunin/.ufo/waves/round-18/claims.json`, with an `amendments` block written after wave 1 and committed before any `analyze`):

- **C1 — calibration** (tied-lowest owned axis at 10.0): discharge the six defects routed by `corpus/lessons/round-17-verifier-spotcheck.md:137-147` and turn the one partial outside disagreement (pin-map sentence, `:108`) into a lesson-backed QUALITY criterion.
- **C2 — operability** (fleet axis, no owned proxy): make the three HEAD-keyed live revision pins routed by `/home/vgpnk/Projects/shokunin/.ufo/waves/hyaku/jj-w1/reports/JjAuditKaidoku.md` §5 read the branch tip under jj.
- **C3 — depth** (the filed sourced claim: S034/S035, with S023/S003/S033): replay the r17 aether INFERENCE (Ghidra 12.1.4 reads Go 1.24/1.25 Swiss map types with the `OldMapType` layout) on carriers the prediction was not calibrated on, with predictions frozen in Git before any `analyze`.

Work items:

- **Planner seat.** The L1 held the canonical planner seat (the validator rejects `planner`); planning data-walks rode scout/connector items (w1 `ScoutProtocolGate`, `ConnC3Prediction`, `RevClaimsSeparable`).
- **Wave 1 (build, 89 seats)** — `kaidoku-shokunin/.ufo/waves/round-18/wave1-spec.json`, one `task` call, 89/89 reports in `.ufo/waves/round-18/w1/`. Critics changed the round before measurement: C1 token checks were circular (`w1/CriticC1.md`: a token-only commit closed 6/6); C2's "3" came from audit prose (`w1/CriticC2.md`); C3's methods/nomethods pair was predicted non-diagnostic (`w1/CriticC3.md`, `RevNotesmdMaps.md`). Amendments: `contract.md` tail, `claims.json` `amendments`.
- **C1 tools and corrections.** `tools/routed-defects.py` (named + substance checks), evidence `evidence/validate16/summary.json` (8/8 first-pass receipts validate via remap), `evidence/sums-runlog.json`, `evidence/s032-digests.json`; restored line in `.ufo/waves/round-17/predictions/SHA256SUMS`; appended corrections in `corpus/knowledge/2026-10-20-r17-go-carrier-diagnostics.md:200-207`, `SCORECARD.md:2436-2440`, `LOG.md:2159-2161`; SKILL registry rows `SKILL.md:448,540-545`; QUALITY #21 `corpus/QUALITY.md:31`; S033 `corpus/SOURCES.md:39`.
- **C2 tools and fixes.** `tools/revpin.py`, `tools/head-rev-lint.py`, `tools/jj-red-before.py`; in-place fixes in `.ufo/gates/citation-drift/citation-drift-probe.py` (omitted `--rev` → `refs/heads/main`; `--rev HEAD` off-tip → exit 2 `head_not_branch_tip`), `.ufo/gates/custody-pair/custody-pair.py` (`--repo`, `# repo-branch-tip:`, `# repo-HEAD-is-branch-tip:`, `# repo-dirty:`, never `Path.cwd()`), `.ufo/waves/round-17/verify.py` (source = branch tip, refuses before any command, `LANE` from its own path). Jj-routed evidence: all three sites fixed (JjAuditKaidoku R1/R2/R3); the trial's `.gitignore` suggestion was not adopted (helper `auto-track none()` already protects; nothing is staged by hand).
- **C3 replay.** Toolchains go1.24.6/go1.25.0 (official tarballs), 12 deterministic synthetic carriers (`carriers/build.sh`), real carrier kimi-webbridge (go1.24.13, `w1/RealCarrierCensus.md`), emulator `tools/swiss-misread.py`, freezer `gen-predictions.py`; predictions and `predictions/decision-rule.json` landed at `eb6c2668…` (16:23:55Z, pushed 16:23:57Z); 15 sequential REA 6.5.0 `analyze` runs 16:24:07–16:32:10Z (`runs/run-log.txt`), 15/15 carrier-run 0 / compare 0. Knowledge entry `corpus/knowledge/2026-10-20-r18-swiss-map-replay.md`; SKILL section `SKILL.md:548-565`.
- **Wave 2 (falsify, 98 seats)** at `b2aad08` — `wave2-spec.json`, one `task` call; every item names what it attacks (`w2/`). It held C3 everywhere (15/15 independent per-run re-derivations, byte decodes of both held-out indices: `w2/EmulatorSourceCheck.md`, `KimiWebbridgeDerive.md`; `DecisionRuleApply.md` → confirmed) and broke C1's gate repeatedly (`GatePINMAP`, `GateVALIDATE16`, `GateREGISTRY`, `GateS032`: closure by fabrication), C1's own selftest (exit 1 after a post-freeze amendment), and several tool details (`CitationDriftReview`, `CustodyReview`, `Verify17Review`, `Verify18Review`, `LintBlindSpots`, `JjSandboxSafety`).
- **Integration** at `db4bdb1`: gate hardening (every r18 receipt checked; stdout hash-binding; digit-bounded fraction; `Pinned values:` and `--strict` required), selftest fixture, custody `--no-optional-locks`, verify fixes, in-round revisions of the entry/lesson/SKILL/S034 (listed in `corpus/lessons/round-18.md`, "In-round revisions").
- **Verification pass** `python3 -I -B .ufo/waves/round-18/verify.py 9011581…` at source `db4bdb1`: 69 commands, `unexpected_exits: []`, `pins_equal: true` (`.ufo/waves/round-18/verification.json`). Final rechecks at `454dee6` retained in `.ufo/waves/round-18/final-recheck/*.receipt.json`.
- **Mistakes mined**: 10 rows in `corpus/lessons/round-18.md` `## Mistakes` (5 from r17 routed defects, 5 from this round incl. the recurring C1 vacuity, a post-freeze landing defect, and a freeze-scope overstatement).
- **Misroot sweep** `git -C /home/vgpnk/Projects/shokunin status --porcelain` (14:20 -03): only `M .ufo/watchdog.log`, `?? .ufo/state/*.report-baseline` (driver files) and `?? .ufo/waves/round-19/` (another lane's round 19; `grep -rl kaidoku` → none). No kaidoku seat file misrooted (also w1 `ScoutMisrootFleet.md`, w2 `MisrootSweep.md`).
- **Cross-domain evidence** (reported, not absorbed; w2 `SiblingOverlap2.md`): the jj 0.45.1 git-compatibility document is registered by kaidoku S036, tameshi S061 (`latest`) and tabi S049; the jj routing report assigns the jj fact to kumitate (`JjConnectorProvinces.md:181,189`). Revenger's records list Ghidra as absent on this host although 12.1.4 is installed (revenger-owned). The revenger/kaidoku native-RE contest stays unresolved (integrator-owned).

## Landed changes

Each commit is tied to LOG entries `LOG.md:2125-2167` (round-18 work) and `LOG.md:2169-2217` (measured records):

| Commit (landed) | Content |
|---|---|
| `eb6c2668e5cb7054fd1e16d2f615cb65586d0fe0` | frozen C3 predictions + decision rule; wave-1 tools, evidence, reports; in-place tool fixes (pre-run) |
| `b2aad08ceeee8dd125ce0d316056d8bd766c7f94` | 15 carrier runs; r17 corrections; knowledge entry; QUALITY #21; SOURCES S033–S036; SKILL rows/sections; README row 35 (pre-falsify) |
| `db4bdb16b842a93f8ec07523c1275c6dfe0f5229` | wave-2 integration: gate hardening, tool fixes, in-round revisions, wave-2 evidence (verification source) |
| `454dee6923750698cc36041236db13b52c6fcade` | verification pass evidence (69 commands) |
| `06df0234d6c168aef8c4e5b29b87cf8b1720a47d` | measured records (SCORECARD, LOG), final rechecks, late wave-2 reports |
| `af2861c9ba8cef6672e72d8de0531ee307a4a6fc` | late wave-2 reports, calibration wording, retained controls stdout |
| `a245bb00c581ae3423a10a055c77d4bc873918df` | retained final-recheck controls stdout (delivered tip) |

## Before → after measurements

| Claim | Counting command | Before (`9011581`) | After (`454dee6`, final recheck) |
|---|---|---|---|
| C1 calibration | `python3 -I -B kaidoku-shokunin/.ufo/waves/round-18/tools/routed-defects.py --root <LANE> --rev <REV> --strict` | open 6 (named 6, substance 6), exit 1 | open 0 (named 0, substance 0), exit 0 (`final-recheck/routed-defects.receipt.json`) |
| C1 (criterion) | QUALITY admission rows; `controls.py 9011581 454dee6` | 20 | 21, rows 1–20 byte-identical |
| C2 operability | `python3 -I -B kaidoku-shokunin/.ufo/waves/round-18/tools/head-rev-lint.py --root <LANE> --rev <REV> --strict` | live 3 / fixture 8 / annotated 0, exit 1 | live 0 / fixture 15 / annotated 6, exit 0 (`final-recheck/head-rev-lint.receipt.json`) |
| C2 (behaviour) | `tools/jj-red-before.py --out <RECEIPT>` | — | 14/14 expectations held (`verify/jj-red-before.stdout`); each fixed file restored alone to baseline bytes → exactly 1 live site (w2 `LintMutation.md`) |
| C3 depth | `python3 -I -B kaidoku-shokunin/.ufo/waves/round-18/measure.py <REV>` field `c3.compare_jsons_with_extra` | 0 | 15 (`final-recheck/measure.receipt.json`); mechanism unreplayed INFERENCE → **confirmed** under the frozen rule |

No-harm controls at `454dee6`: LOG/SCORECARD old prefixes preserved; prior knowledge and lesson files byte-identical except the contracted appendable r17 entry; SOURCES S001–S032 evidence cells unchanged (only `used-by` appended for S003/S023, logged old→new); `invocation-audit` 26 rows, 25 exercised_match, 1 labelled unexercised, **0 unlabelled** (baseline 17/17); temporal-sweep 4/4 corrected, 0 new. Owned proxies stay at 10.0 (coverage map 95/95 → 96/96).

Limits kept with the numbers: C1 — wave 2 closed defects by fabrication against the first substance checks; after hardening the validator digest is still format-only and S033's head / producer-pass attribution cannot be resolved offline, so "6 → 0" stands together with the w2 Truth* re-derivations, not alone. C2 — two compare-only HEAD reads behind nested wrappers are invisible to the lint; citation-drift refuses only the literal `HEAD`. C3 — both held-out confirmations are Go 1.24.x; one pass; one Ghidra release.

## Sources & frontier

- Census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`:
  - round start (12:14 -03): `kaidoku	ok	…/corpus/SOURCES.md`, exit 0.
  - round end (14:20 -03): `kaidoku	W04	S033 duplicate url github.com/NationalSecurityAgency/ghidra/pull/9348 across scopes` then `kaidoku	ok	…`, exit 0 (W04 is the expected warning for a superseding row with a narrower scope; w2 `CensusRerun.md`).
- Rows 32 → 36 (census mode: rows 36, A31/B4/C1, mined 34, rejected 2; before A28/B3/C1, mined 30/rejected 2).
- Added by tier: A — S034 (Go 1.24 notes, Swiss maps + `noswissmap`), S035 (go1.24.6/go1.25.0 `internal/abi` map descriptors), S036 (jj 0.45.1 git-compatibility); B — S033 (PR #9348 at head `a214355`, supersedes S032).
- Touched old→new: `used-by` of S003, S023, S033 appended (`corpus/lessons/round-18.md`, Registry changes); S034 revised in-round (teaches/scope/anchor) before closure; S032 unchanged and superseded.
- Frontier/paths: `## Paths` route path drops S032; new paths "Swiss-map replay" and "Revision pins under jj"; search-log entry plus a correction line (identified 12, screened 12, included 4, excluded 8).
- Sourced claim: C3 (entry `source:` cites S034/S035/S023/S003/S033).

## Trend verdicts

- **expansion: unchanged** — the Swiss-map entry deepens held Go ground (`corpus/README.md:35` row, PROVINCE Core); no new coverage-map row, no capability row (w2 `TrendVerdicts.md`, `CapabilityCandidate.md`).
- **quality: improved** — the r17 aether INFERENCE is superseded by a frozen-before-run replay that held on every wave-2 re-derivation; six r17 overstatements corrected append-only; S032 superseded by S033; no admitted entry failed its re-check.
- **discernment: improved** (author-side; outside sample pending) — the r17 partial disagreement became QUALITY #21 with red-before (`round-18.md` Mistakes 1; w2 `Quality21Ground.md` HOLDS); wave-2 falsifications became Mistakes rows 6, 9, 10 with fixes or stated limits.

Axis verdicts: calibration improved (C1), operability improved (C2), depth improved (C3); coverage, freshness, adjacency unchanged. No axis harmed found by the controls or w2 `AxisHarmCheck.md` (its findings were fixed or listed as open, none decreased a proxy). Admission is the closure's ruling.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: `kaidoku-shokunin/SKILL.md:81-314` craft section; round 18 adds decision tables at `SKILL.md:557-561` (Swiss-map replay) and `SKILL.md:575-579` (revision pins under jj), both cited. No non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: round 18 — 15 pinned carriers → REA 6.5.0 analyze → bound retained log → extract → compare against predictions frozen at `eb6c266` (`kaidoku-shokunin/.ufo/waves/round-18/runs/*/receipt.json`, `LOG.md:2125-2217`). Author-side only.
- [~] Instructions executable by an agent without oral context. Evidence: registry rows match exercised argv 25/26 with 1 labelled unexercised and 0 unlabelled (`kaidoku-shokunin/.ufo/waves/round-18/final-recheck/invocation-audit.receipt.json`). Not outside-executed.
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: no sibling holds Go map/Ghidra-Go knowledge (w2 `SiblingOverlap2.md`); but `PROVINCE.md:8-26,44` is stale on REA pins (client configs now 6.7.0, w2 `ProvinceAccuracy.md`) — open freshness debt, not fixed this round.

## Waves, seats, routing

- W1: 89 seats — executor 19, scout 23, reviewer 15, scribe 10, connector 8, critic 6, revenger 4, sentinel 2, simplifier 2; 89/89 reports; `SwissMisreadTool` ended aborted after writing its report (w2 `WaveEvidenceComplete.md`).
- W2: 98 seats — reviewer 53, executor 9, scout 9, critic 8, mutation-tester 4, revenger 4, connector 4, scribe 3, sentinel 2, simplifier 2 (critic+sentinel 10 ≤ cap; 4 critic items were set to reviewer to respect it). Dead: `GateSUMSRUNLOG` (provider refusal, "cyber" usage policy, exit 1) and `GatePRODUCERREV` (`zai/glm-5.3-flash` 429 rate limit after 10 retries, exit 1). Not returned at integration and not used: `TruthREGISTRY`, `ShonenLines`; `DecisionRuleApply`, `AetherDualPath`, `SiblingOverlap2` returned late and were integrated.
- Round total 187 seats (≤ 200). Routing by role through the session table (no `model` passed); mid-round the orchestrator changed role routes (m_flash → m_zfl for analysis roles, then scout/labrat/executor → m_flash, critic/sentinel → m_opus, scribe → m_haiku); W1 seats ran on the routes at 12:24, W2 seats on the routes at 13:42.
- Wave records: `wave1-*.json`, `wave2-*.json` (spec, dispatch, registry, registration, assignments, result) under `kaidoku-shokunin/.ufo/waves/round-18/`.

## Installs

- Go 1.24.6 and Go 1.25.0, official go.dev tarballs, sha256 checked against `https://go.dev/dl/?mode=json&include=all` (`bbca37cc…8712`, `2852af0c…b613`), unpacked to `~/.local/opt/go-1.24.6` and `~/.local/opt/go-1.25.0`, not on PATH. Reason: build deterministic Swiss/noswiss synthetic carriers and read `internal/abi` source. pacman was not used (all transactions paused). Seat installs: one `uv run --with markdown-it-py==4.0.0` ephemeral env (w2 `GateREGISTRY.md`), nothing global.

## Open / routed

- L0 questions: none filed.
- Carried (in `corpus/lessons/round-18.md`, Open): r12 items (S### row, custody disclosure, operability axis decision); PROVINCE REA-pin drift; citation-drift HEAD aliases; custody `repo-root`; jj-red-before env scrub and path guard; validator-digest format-only check; `revpin.py:6` wording (`@-`).
- Operator/protocol: the wave-2 CustodyReview seat observed `~/.config/devin/mcp_config.json` and `~/.omp/agent/mcp.json` rewritten at 13:35:56 -03 (pins now `rea-agents@6.7.0`); not opened, not lane-caused.
- Stale-lane: kaidoku round 18 mission open since 12:07:53 -03 (~2h14m at report time, beyond two 450 s ticks) — **progressing**: seven lane-authored commits `eb6c266`…`a245bb0`; respawn-per-round driver; no other mission of this lane is open.
