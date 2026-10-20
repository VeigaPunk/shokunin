# kaidoku — round 17 report (hyaku phase 2, attempt 1)

Lane HEAD at report: `de6c721be61bf6e8b4001021f09a9cdea38166dd` (pushed; `git rev-list --count @{u}..HEAD` = 0). Baseline `b563c799d97774aae4351276fe43cb897311e349`. Steered round 17 only; round 18 is not started.

## Work performed

Declared claims (`.ufo/waves/round-17/claims.json`):
- **C1 — calibration**, the tied-lowest owned axis at 10.0: discharge the two routed outside defects R16-PROVENANCE and R16-INVOCATION (`corpus/lessons/round-16-verifier-spotcheck.md:183-184`) and add QUALITY #19.
- **C2 — depth, with a capability acquisition**: real, pinned Go carriers through REA 6.5.0 `analyze` (Ghidra 12.1.4), with the Ghidra analyzer log retained and bound to the run, compared against routes predicted from installed source and frozen in Git before the measured runs. This is the sourced claim.

Work items:
- **Pilot (calibration only).** Two REA analyze sessions (shfmt go1.27.0, esbuild 0.25.12 go1.23.12) with a polling log copy. Retained in `kaidoku-shokunin/.ufo/waves/round-17/pilot/` (README, SHA256SUMS). They ran before the claims and predictions, so they are not counted as prospective.
- **Wave 1 (build).** 78 seats, validated under policy v2 and dispatched as one `task` call on the third identical attempt; the first two were refused at the host job cap (`wave1-dispatch-attempts.json`). The wave produced:
  - 11 stdlib tools (`tools/`), plus `measure.py` and `controls.py`;
  - source anchors for the whole Go route chain (GoRttiMapper, GoApiSnapshot, GoBuildInfo, GoVer, REA runtime-root lifecycle);
  - 7 opened external sources;
  - drafts of the entry, lesson, QUALITY rows, SKILL rows and SCORECARD section;
  - adversarial findings that reshaped the contract: route fields, session binding and private TMPDIR, the temporal-sweep undercount, the fallback-route carriers.

  Reports: `kaidoku-shokunin/.ufo/waves/round-17/w1/*.md`.
- **Frozen predictions.** Eight carriers were selected by the L1. Predictions came from `predict.py`, plus a hand prediction for the build-info-less carrier, and were committed and pushed at `271167473d87ef710f07ecdd98caf0ce12091686` before any measured run (`predictions/`, `SHA256SUMS`).
- **First measured pass.** 8/8 carrier-run exit 0 and compare exit 0, 13:47–14:00 UTC; receipts at `da64646`.
- **Wave 2 (falsify).** 69 seats, each attacking a named artifact; 67 completed and 2 died (below). Main findings:
  - `receipt-validate.py` rejected every producer receipt while its own selftest passed (17 seats);
  - the mid-run pin sentence had no retained record (an R16-PROVENANCE recurrence);
  - the frozen-commit token `2716747` was unresolvable;
  - the recheck command was destructive;
  - bytecode had been written into frozen dirs;
  - full environment leaked to the Ghidra JVM;
  - substring and prefix binding could bind a foreign log;
  - `predict.py` disagreed with the real Java `GoVer.parse` on 27 of 366 strings;
  - the aether EOF has a mechanism traceable in the bytes (Swiss map read with the `OldMapType` layout).

  Reports: `kaidoku-shokunin/.ufo/waves/round-17/w2/*.md`.
- **Integration**, at `95e34db` and `d0ab299`: every tool fix (listed in the LOG measured entry and the as-built section of `contract.md`), frozen replicate expectations (`predictions/replicate-expectations.json`, committed at `95e34db`), then a **second measured pass** with the hardened tool. It ran 14:27–14:40 UTC: 8/8 exit 0 and compare 0, mid-run pin checks retained (2–8 per run, all equal), and no leftover session parent.
- **Single verification pass** at source `d0ab2992149a38794e5ef2474ba5d4ef5ee1e905` (`verify.py` → `verification.json`, evidence commit `b31975d`). 79 commands, all with expected exits; tool/prediction pins equal pre/post; no `__pycache__` under `.ufo`.
- **Final rechecks** at `8e7642c`, retained in `final-recheck/*.receipt.json` (commit `de6c721`).

## Landed changes

Each change is tied to `kaidoku-shokunin/LOG.md` entries "round-17 — retained Go carrier diagnostics and routed r16 defects" and "round-17 measured records and final integration".
- `corpus/knowledge/2026-10-20-r17-go-carrier-diagnostics.md`: new entry (written at `da64646`, revised at `d0ab299`).
- `corpus/QUALITY.md` rows 19 (temporal-stability records) and 20 (provider logs bound by their own bytes; request echo is not selection evidence). Rows 1–18 are byte-identical (`d0ab299`).
- `corpus/SOURCES.md`: S024–S032 added (S028 rejected); used-by appended on S003 and S023; Paths, Search log and Leads updated (`da64646`, `d0ab299`).
- `corpus/lessons/round-17.md`: Gate, Mistakes (12 rows), four line-exact R16-PROVENANCE corrections, in-round revisions, executed evidence (`d0ab299`, `8e7642c`).
- `SKILL.md`:
  - citation-drift (`:448`) and custody-pair (`:449`) rows aligned in place to the exercised isolated absolute argv;
  - new section "Retained Go carrier diagnostics — round 17" with a decision table and 10 registry rows (`da64646`, `d0ab299`).
- `corpus/README.md:35`: r17 token and clause, in place, line count unchanged. `PROVINCE.md:52`: current-op qualification, in place.
- `SCORECARD.md`: "Round 17" section and capability row `retained REA Ghidra-session log capture` (`8e7642c`).
- Wave evidence under `.ufo/waves/round-17/`: specs, dispatches, registrations, `wave-outcomes.json`, tools, runs, predictions, verify and final-recheck (commits `2711674`, `da64646`, `95e34db`, `d0ab299`, `b31975d`, `de6c721`).

R16-PROVENANCE correction for the fleet report (out of lane, recorded here and not by rewriting the filed bytes): R16-PROVENANCE: `.ufo/reports/round-16/kaidoku.md:60` — map matches committed source-revision blobs; temporal stability not evidenced.

## Before → after measurements

| Claim | Counting command | Before (rev) | After (rev) |
|---|---|---|---|
| C1a R16-PROVENANCE | `python3 -I -B .ufo/waves/round-17/tools/temporal-sweep.py --root <LANE> --rev <REV> --sites-rev b563c79…` | 4 sites, 0 corrected, 4 unqualified (`b563c79`) | 4/4 corrected, 0 unqualified, 0 new (`d0ab299`, `b31975d`, `8e7642c`) |
| C1b R16-INVOCATION | `python3 -I -B .ufo/waves/round-17/tools/invocation-audit.py --root <LANE> --rev <REV>` | 7 rows: 5 exercised, 2 unlabelled_variant (`b563c79`) | 17 rows: 17 exercised_match, 0 unlabelled (`b31975d`, `8e7642c`) |
| C1c criterion / red-before | `controls.py b563c79 <REV>`; `pins.py --selftest`; `receipt-validate.py --selftest` | QUALITY 18 rows | 20 rows, rows 1–18 identical; mutated-file red case exit 1; mid-run-drift red case exit 1 |
| C2 retained diagnostics | `bash .ufo/waves/round-17/run-carriers.sh <LABEL>`; `receipt-validate.py runs/<l>/receipt.json` | 0 retained run-bound analyzer logs; capability rows 6 | 16 runs (8 × 2 passes), 8/8 compare 0 per pass, 8/8 receipts valid; capability rows 7 (`measure.py 8e7642c`: `C2_scorecard_capability_row` 0→1) |

Numeric owned proxies: coverage 10.0→10.0 (map 94/94→95/95), depth 10.0→10.0, calibration 10.0→10.0. The proxies are saturated, so the supplemental counts above carry the moves.

Prediction results for C2: routes matched 8/8 in both passes. Of the six prospective carriers, three tested routes unseen at freeze: notesmd-cli and aether 1.25.x took the `Falling back … to 1.25.0` WARN, and esbuild 0.27.7 had no build info. The other three repeated pilot-seen routes. The pre-registered replicate expectation "Evidence IDs equal the first pass" held for 7/8 and was **falsified for aether** (string_count 29118→29117). aether's symbol-markup EOF (`17645861, 111938854`) was unpredicted, reproduced exactly, and is carried as a labelled INFERENCE.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`.
  - Round start: `kaidoku	ok	…/kaidoku-shokunin/corpus/SOURCES.md`, exit 0.
  - Round end: same output, exit 0. The end run is also retained as verification label `sources-census`.
- Rows: 23 → 32. Tiers A21/B1/C1 → A28/B3/C1; status mined22/rejected1 → mined30/rejected2.
- Rows added by tier:
  - A: S024 (Go `debug/buildinfo`), S025 (Go release history), S026 (linker `X:` suffix), S028 (Go 1.27 notes, **rejected**), S029 (Ghidra upstream range and release status), S030 (GoReSym v3.3 release note), S031 (Go 1.25 DWARF5 notes).
  - B: S027 (golang/go issue 75953), S032 (Ghidra PR #9348, community lead).
- Rows touched old→new: S003 and S023 `used-by` appended. The exact lists are in `corpus/lessons/round-17.md`, "Registry transitions".
- Frontier advanced: two leads resolved and narrowed. GoReSym releases became S030; the remaining question is type recovery on a 1.26 carrier. Ghidra release notes after 12.1.4 became S029: no later release exists, and master names Go 1.26 only.
- Sourced claim: C2's entry uses S024 (`errNotGoExe`, plus a `go version -m` cross-check), S026/S031 (`X:nodwarf5` meaning), S025 (toolchain dating), S029 (release status) and S032 (aether lead).
- Mined mistakes: `corpus/lessons/round-17.md` `## Mistakes`, 12 rows, each with class, evidence, captured-by and a fix with a red state.

## Trend verdicts

- **expansion: unchanged.** The new knowledge entry deepens held Go ground (README Go row). The capability row and new source kinds count as repertoire, not uncovered ground, so no `improved` is claimed.
- **quality: improved.**
  - Source-model predictions (r14–r16) are superseded by runtime-retained, run-bound observations.
  - The r16 temporal overclaims got line-exact corrections.
  - The round's own overclaims were found by w2 and fixed before close: the mid-run pin sentence, the dead commit token, the destructive recheck.
  - No admitted entry failed its recheck: all 8 receipts are valid and all 8 predictions reproduce.
- **discernment: improved** (author-side; awaits outside spot-check). Both prior outside routes became the grounded QUALITY #19 and working fixes. The gate rejected its own overreach (aether cause, op history, 8/8 generality). The pre-registered aether Evidence-ID expectation is reported falsified.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: `kaidoku-shokunin/SKILL.md:81-314` craft section (17/17 bounded citation blocks, `controls.py` craft check unchanged); r17 adds a route decision table at `SKILL.md:521-528`. No non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: the historical 2026-10-15 libjq task, plus round 17: eight pinned carriers → REA analyze → retained bound log → extract → compare against frozen prediction, two passes (`kaidoku-shokunin/.ufo/waves/round-17/runs/*/receipt.json`, LOG round-17 entries). Author-side only.
- [~] Instructions executable by an agent without oral context. Evidence: the registry rows at `kaidoku-shokunin/SKILL.md:537-546` match exercised argv 17/17 (`final-recheck/invocation-audit-final.receipt.json`); the non-destructive `RUNS_DIR` recheck is documented. Not outside-executed.
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: `kaidoku-shokunin/PROVINCE.md:52` qualified in place with line count unchanged. The sibling scans (w1 `ConnSiblingOverlap`, w2 `ConnSiblingRows`) found no lane retaining REA logs. The revenger/kaidoku shipped-artifact contest is unchanged and unresolved (integrator-owned).

## Waves, seats, routing

- **W1**: 78 seats. executor14 (m_swe), scout20, reviewer12, connector8, revenger4, simplifier2 (m_flash), scribe10 (m_haiku), critic6 and sentinel2 (m_opus, 8 ≤ 10). All completed. The dispatch was refused twice whole ("Background job limit reached (100)") and spawned on the third identical payload; nothing was split.
- **W2**: 69 seats. reviewer18, executor16, scout9, critic8, scribe5, mutation-tester4 (m_sol), connector3, revenger3, sentinel2, simplifier1. 67 completed. **Dead seats**: `PinsAttack` and `TemporalSweepAttack` (m_swe, `Devin stream error resource_exhausted: Reached free model rate limit`). They were not respawned; their targets were covered by `MutatePinsCompare`, `MutateTemporalSweep` and the L1's added selftest cases.
- **Round total**: 147 seats (≤ 200).
- **§3 L2 floor**: met inside W1 (planner role held by the L1, as ruled 2026-10-19; connector, executors, scribe, scout, reviewer and critic all present).
- **Records**: `wave{1,2}-spec.json`, `wave{1,2}-dispatch.json`, `wave{1,2}-registration.json`, `wave-outcomes.json`.

## Cross-domain evidence, installs, stale-lane, L0

- Cross-domain:
  - tameshi independently proposes the same pre/post pin shape (w1 `ConnAdjacencyReport`). That is a method convergence, not outside verification.
  - The revenger lane claims the same shipped-artifact domain (contest unchanged, integrator-owned).
  - The aether failure belongs to upstream Ghidra (open PR #9348); it is documented here and nothing is pushed upstream.
- Tool installs:
  - L1: none.
  - Seat `DraftSourcesRows` (w1): Go 1.27.3 linux/amd64 from the official go.dev tarball (sha256 matched `go.dev/dl/?mode=json`) into `~/.local/opt/go-1.27.3`, not on PATH, to read the toolchain source and run `go version -m`.
  - Seat `ScoutReaLogKnob` (w2): materialized `rea-agents@6.7.0` via npm for read-only inspection.
  - No pacman transaction (the pause was honored).
- Host residue: the first pass left eight `/tmp/kr17-rea-*` folders containing only `node-compile-cache`. They were removed, and the second pass left none. Other seats' scratch under `/tmp` is left to its owners.
- Stale-lane: the mission launched 2026-10-20T10:14:11-03:00 and has been open longer than two driver ticks. It is **progressing**: seven lane-authored commits, `2711674` through `de6c721`. No other mission of this lane is open (respawn-per-round driver).
- Inherited state: none. The watchdog search found no `lane-dead-no-report kaidoku round=17`, and the lane was clean at `b563c79`.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed only driver-owned `.ufo/state/*` and `.ufo/watchdog.log`. No seat file had landed in the fleet root.
- Non-lane files not edited: `corpus/lessons/round-16-verifier-spotcheck.md` and earlier verifier files.
- Operator lessons: none present.
- Open L0 questions: none filed this round.
