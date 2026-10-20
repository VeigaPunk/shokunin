# kaika W3 — audio round 101 non-author verification

- Lane: `audio-shokunin`, worktree `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/audio-shokunin`, branch `kaika/round`.
- Base `defbe1286`; round head `343cd978ef376fc6e0c3d53a8740b931f7d031df`; first round commit `d00a8d229645c41fab39b4cdc2f396f64216b581`.
- Reviewer: `W3ReviewAudio` (orchestrator-dispatched, read-only). Scratch `/tmp/kaika-verify/audio-review/` removed after use.
- Recommendation: **ADMIT-with-findings** — C1/C2/C3 verify; two required corrections (D1 registry cell, D2 C3 measured-commit pointer) and three low-severity precision items. No axis harmed; scores remain honestly `unmeasured`.

## 1. Provenance — PASS

Command: `git log --format='%h %an <%ae> | %cn <%ce> | %s' defbe1286..343cd978e`.

```
343cd978 audio-shokunin <audio@shokunin.local> | audio-shokunin <audio@shokunin.local> | round-101: record verified measurements and C3 closure
d00a8d22 audio-shokunin <audio@shokunin.local> | audio-shokunin <audio@shokunin.local> | round-101: complete audio corpus and true-peak measurement
```

`git rev-parse --abbrev-ref HEAD` → `kaika/round`; `git status --porcelain | wc -l` → `0`; `git merge-base --is-ancestor defbe1286 HEAD` → exit 0.

## 2. Append-only — PASS

Command: `git diff --numstat defbe1286..343cd978e -- LOG.md corpus/lessons corpus/QUALITY.md`.

```
74	0	LOG.md
30	0	corpus/QUALITY.md
150	0	corpus/lessons/round-101.md
```

Removed prior lines in those paths: `git diff defbe1286..343cd978e -- LOG.md corpus/lessons corpus/QUALITY.md | grep -E '^-[^-]' | grep -c .` → `0`.

- `corpus/SOURCES.md` is absent at base (`git ls-tree --name-only defbe1286 -- corpus/SOURCES.md | wc -l` → `0`) and unchanged between `d00a8d2` and head (`git diff --stat d00a8d2..343cd978e -- corpus/SOURCES.md` empty), so no prior row line was edited in place. The `used-by` old→new values are logged at `corpus/lessons/round-101.md:112-141`.
- No file is deleted or renamed: `git diff --name-status defbe1286..343cd978e | grep -vE '^[AM]'` prints nothing. The 16 deleted lines in the full diff are 4 SCORECARD template placeholders, 3 SHONEN header lines + 4 stale `[x]` boxes, and 5 `measure_audio.py` dispatch/builder lines replaced by the guarded forms (Q16 check below). No knowledge deleted.
- Report's c1d/c1e: `grep -c '\[x\]' SHONEN.md` → `0`; `grep -c '\.shokunin' SHONEN.md` → `0`.

## 3. Claim verdicts (re-run at base and head)

Commands (from the lane root; base values with `git show defbe1286:<path> | grep ...` or `git ls-tree`):

```
grep -cE '^## Round (8[7-9]|9[0-9]|100) verdict' SCORECARD.md                  # c1a
grep -cE '^\| (depth|coverage|calibration) \| \*\*unadjudicated\*\*' SCORECARD.md # c1b
grep -cE '^## Round (87|88) ' LOG.md                                            # c1c
grep -c '\[x\]' SHONEN.md ; grep -c '\.shokunin' SHONEN.md                       # c1d, c1e
ls corpus/knowledge/*.md | wc -l                                                 # c2a
for f in corpus/knowledge/*.md; do head -1 "$f"; done | grep -cE '^source: S[0-9]{3}' # c2b
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md             # c2c
grep -cE '^\| Q[0-9]+ \|' corpus/QUALITY.md                                      # c2d
grep -cE '^- K[1345] — ' corpus/README.md                                        # c2e
grep -c 'probe-truepeak-r101' corpus/fixtures/measure_audio.py                   # c3a
python3 -c "import json,math;t=json.load(open('corpus/live/round-101-truepeak/20261019T233319127994Z/measurements.json'))['measurements']['truepeak_r101'];print(sum(math.isfinite(v['mono']['true_peak_dbtp']) for v in t['artifacts'].values()))" # c3b
```

| Claim | Report before→after | My base | My head | Verdict |
|---|---|---:|---:|---|
| C1 c1a verdict sections 87–100 | 0 → 14 | 0 | 14 | **verified** |
| C1 c1b unadjudicated axis rows | 0 → 18 | 0 | 18 | **verified** |
| C1 c1c LOG 87/88 headings | 0 → 2 | 0 | 2 | **verified** |
| C1 c1d SHONEN `[x]` | 4 → 0 | 4 | 0 | **verified** |
| C1 c1e SHONEN `.shokunin` refs | 4 → 0 | 4 | 0 | **verified** |
| C2 c2a knowledge entries | 14 → 18 | 14 | 18 | **verified** |
| C2 c2b first-line `source:` | 0 → 4 | 0 | 4 | **verified** |
| C2 c2c SOURCES rows | absent → 15 | 0 (file absent) | 15 | **verified** |
| C2 c2d QUALITY criteria | absent → 22 | 0 (file absent) | 22 | **verified** |
| C2 c2e indexed Core-gap rows | 0 → 4 | 0 (README absent) | 4 | **verified** |
| C3 c3a truepeak option occurrences | 0 → 2 | 0 | 2 | **verified** |
| C3 c3b finite artifact true peaks | 0 → 17 | 0 | 17 | **verified at head; D2** |

All after-values except c3b also reproduce at the claimed measured commit `d00a8d2` (I ran each against that tree). c3b does not: `git ls-tree -r --name-only d00a8d2 -- corpus/live/round-101-truepeak/20261019T233319127994Z/measurements.json | wc -l` → `0`, so the stated after-command cannot run at `d00a8d2`; at `343cd978e` it prints `17`. See D2.

Content spot-checks:

- `SCORECARD.md:897-1051` contains the 14 round sections; rounds 87, 88, 93, 98, 99, 100 are `**unadjudicated**` on all three axes (6 × 3 = 18 rows). `SCORECARD.md:905` and `:917` quote the verifiers verbatim; `reports/round-87/r87-verifier.md:20` reads "GATE FAIL — NOT VERIFIED as a reproducible green landing." and `reports/round-88/r88-verifier.md:20` reads "GATE FAIL as a reproducible green landing — PASS on every encoded law."
- Critic opinions are advisory, not adjudications: `SCORECARD.md:906,918`; `corpus/QUALITY.md:19` = Q11; `corpus/lessons/round-101.md:31` = M25. `reports/round-87/r87-critic.md:9` and `reports/round-88/r88-critic.md:9` both say "**Verdict: ADMIT-with-findings.**"
- `SKILL.md` untouched this round (`git diff --stat defbe1286..343cd978e -- SKILL.md` empty); `SHONEN.md` now carries `[ ]` + three `[~]` boxes with pointers to `reports/round-2/r2-verifier.md`, `reports/round-3/r3-adjudicator.md`, `reports/round-24/r24-verifier.md`; all three files exist at head.

## 4. SOURCES and source re-opens

### Contract census — clean; fleet validator — one E-code

Contract commands (run from lane root):

```
rows: 15
malformed: 0
tiers: A=11 B=2 C=2
statuses: mined=14 rejected=1
dup-ids: (nothing)
enum/tier-inflation: (nothing)
missing-usedby: (nothing)
```

`bash .../fleet-census/scripts/sources-census.sh validate <lane>` → **exit 1**:

```
audio-shokunin	W01	S007 tierC mined used-by=corpus/knowledge/2026-10-19-game-loudness-whole-mix-protocol.md, corpus/lessons/round-101.md
audio-shokunin	E09	S011 recheck=—
audio-shokunin	W04	S014 duplicate url raw.githubusercontent.com/FFmpeg/FFmpeg/n9.0.1/libavfilter/af_loudnorm.c across scopes
audio-shokunin	W04	S015 duplicate url www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.1770-5-202311-I!!PDF-E.pdf across scopes
```

`E09` is the only exit-1 cause. Proof: a scratch copy of the registry with S011's `recheck` cell changed to `frozen` validates `exit 0` with only the same W01/W04 warnings (`fixed-lane ok`). `W01`/`W04` are by design here: S007 is cited only as a labelled lead in K5, and S014/S015 are superseding rows required by contract rule 2 (same URL, different scope). See D1.

### Re-opened rows (≥3; new tier-A and rejected included)

| Row | Tier/status | Re-opened verification |
|---|---|---|
| S014 | A / mined (new) | n9.0.1 `af_loudnorm.c` l.740 reads "static const int input_srate[] = {192000, -1};"; l.751-752 gate on `frame_type != LINEAR_MODE`; l.808 sets `FIRST_FRAME`. Gate quote/anchor exact. |
| S010 | A / mined (new) | Godot 4.4 class reference Properties `int compress/mode = 2`; Description "By default, Godot imports WAV files using the lossy Quite OK Audio compression." (1 match). S009 (4.3) → `0`; S008 (stable) → `2` + same sentence. |
| S011 | C / **rejected** | Godot 4.4 tutorial §Compress > Mode: "Three compression modes can be chosen from for WAV files: Disabled (default), RAM (Ima-ADPCM), or QOA (Quite OK Audio)." Same-version contradiction with S010 and host S013 confirmed. |
| S015 | A / mined (new) | BS.1770-5 Annex 2, `pdftotext -layout` l.788-789: "an unfortunately-phased tone at a quarter of the sampling frequency" (the 3 dB fs/4 example is phase-qualified). S001 l.258 "Incomplete gating blocks at the end of the measurement interval are not used.", l.322-323 (−3.01 LKFS), l.339-341 (pure-tone caveat) also exact. |
| S002 | A / mined | EBU R 128 `pdftotext -layout`: l.110-115 (target/tolerances), l.135 "the True Peak Level of a programme shall not exceed −1 dBTP", l.180 (LRA under 1 minute). Exact. |

Lesson Gate quotes and anchors exist at the sources for every sampled row. Every `used-by` path exists (contract census above); a cross-check of each new entry's first-line `S###` citations against the rows' `used-by` found no omission for real registry rows. The only unmatched ids are the ART dossier's `S023`/`S029` labels (see D5).

## 5. Discernment spot-check (`LEARNING.md` discipline)

| Sample | Type | Verdict | Reason |
|---|---|---|---|
| K4 `2026-10-19-godot-wav-import-default-qoa.md` | admitted | **agree** | Version-pinned 4.3=0, 4.4=2, stable=2; host Godot 4.7.2 import reproduces `compress/mode=2`; the same-version tutorial is rowed rejected with a flip. Consequence is scoped to the lane's PCM16 masters. |
| K5 `2026-10-19-game-loudness-whole-mix-protocol.md` | admitted | **agree** | EBU/ASWG/BS.1770 claims reproduce; ASWG mirror honestly tiered B; S007 tier-C used only as a labelled lead; "measured as a whole" (S003 rec. 9) grounds the no-per-fixture-window inference. |
| K2 (two-pass linear gate + `output_tp` under-read) | rejected | **agree** | Deferral is justified under Q5 (authoring seat did not re-run; only the reviewer did) and Q3 (ART line cites fail at n9.0.1), with an explicit flip: an author re-run with pinned lines. |
| S011 tutorial row | rejected | **agree** | Same-version generated class reference and host headless import both contradict its "Disabled (default)" for this scope; the row keeps reason + flip. |

## 6. New knowledge entries — PASS

Header trio (`source:` / `verified-at:` / `recheck:`) present in all four (`sed -n '1,3p'` on each). Rechecks re-run 2026-10-19 on this host:

- K1: exit 0; printed 0.400 s → `-33.05 → -24.05` linear, 3.0 s → dynamic, amp 0.0003 → `-inf → -4.05`; matches the entry table.
- K3: exit 0; 17 artifact lines match the table values, including `impact SP=-1.8 TP=-0.7`, and dual-mono deltas +3.010/+3.011 on the nine gated files.
- K4: exit 0; 4.3=`0`, 4.4=`2`, stable=`2`; host import `compress/mode=2` twice; `.sample` sizes 39,247 B (stem) and 2,743 B (ui) match the entry.
- K5: exit 0; counts match: `-24 (±2) LKFS` 1, `-18 (±2) LKFS` 1, `minimum of 30 minutes` 1, `measured as a whole` 1, `both stereo and surround configurations` 2; EBU strings 1 each; `loudness of pure tones` 1.

## 7. Credentials — PASS

Command: `git diff defbe1286..343cd978e | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'` — printed nothing (`exit 1`).

## 8. Report conformance — PASS

Required sections present in order: Work performed; Landed changes; Before → after measurements; SHONEN; Sources & frontier; Mistakes; Trend verdicts; L0 questions; Integrator notes.

- No `[x]` in the report or `SHONEN.md`; SHONEN evidence pointers resolve; the report names the round commits (`d00a8d2`, `343cd978e`) and the final receipt SHA-256.
- Claims/evidence counts match the re-runs in §3; the 87/88 critic-opinion correction is reflected in SCORECARD, QUALITY Q11 and lesson M25.
- Low precision nits: D3, D4.

## 9. Recommended per-axis verdicts

The lane scores three owned axes; all three self-verdicts are `unmeasured → unmeasured` because no 0–10 rubric exists (`SCORECARD.md:6-10,1057-1061`). I recommend accepting that honest non-score and the evidence-count deltas:

| Axis | Recommended verdict | Basis |
|---|---|---|
| calibration | **claim verified; score unchanged (`unmeasured`)** | c1a–c1e reproduce; 14 verdict sections, 18 unadjudicated rows, verbatim GATE FAILs, advisory critic handling. |
| coverage | **claim verified with D1; score unchanged (`unmeasured`)** | c2a–c2e reproduce (14→18 entries; 15 rows; 22 criteria; 4 gap rows); four source-backed admits, three rejects with flips. |
| depth | **claim verified with D2; score unchanged (`unmeasured`)** | c3a/c3b reproduce at head; 10 tests OK; independent probe re-run exits 0 with 17 finite peaks; controls pass; canonical artifacts byte-unchanged. |

No axis harmed: `corpus/artifacts` diff base→head is empty; no knowledge file was deleted; the selector equivalence check (§11) is clean.

## 10. Trend verdicts

- **Expansion — improved.** 14→18 knowledge entries; four previously uncovered topics (K1/K3/K4/K5); SOURCES 0→15 rows (A=11, B=2, C=2); each new entry tagged to a coverage-map gap row.
- **Quality — improved.** Q1–Q22 with lesson links; truepeak probe has a no-builder dispatch guard, an independent name-keyed analytic oracle (+2.999335 dB vs +3.0103 ±0.08; phase-0 0.000; dual-mono +3.010 vs 3.0103), round-scoped outputs, 10/10 tests, and an independently re-run probe with 17 finite peaks and empty failures. Outstanding: D1/D2 corrections.
- **Discernment — improved.** K1-as-drafted, K2 and K6 rejected with reasons/flips; S011 rejected on same-version contradiction; six rounds stay `unadjudicated`; critic "ADMIT-with-findings" opinions are explicitly not adjudications. Residual: ART/dossier id namespace collision (D5) and the thin M20→Q3 link.

## 11. C3 no-harm and selector verification

- `measure_audio.py` builder call is guarded by `if not args.probe_truepeak_r101:`; the truepeak branch measures existing `corpus/artifacts` and writes controls/logs/receipt under `corpus/live/round-101-truepeak/<run-id>/` (`TRUEPEAK_R101_SCRATCH = ROOT / "live" / "round-101-truepeak"`, line 54373).
- `python3 corpus/fixtures/test_truepeak_r101.py` → `Ran 10 tests ... OK`; the builder-spy test asserts zero builder calls in truepeak mode and one in default mode.
- Selector equivalence: the mode expression is the base expression with `"probe-truepeak-r101" if args.probe_truepeak_r101 else ` prepended; the suffix expression is the same prepend plus one redundant paren pair around the tail. Evaluating old vs new for all 143 base flags singly and all-false gives **0 mismatches**; with `probe_truepeak_r101=True` the new arms return `probe-truepeak-r101` / `-truepeak-r101`.
- Canonical artifacts: `git diff --stat defbe1286..343cd978e -- corpus/artifacts` empty; `git status --porcelain` in the lane is clean.
- Receipt `corpus/live/round-101-truepeak/20261019T233319127994Z/measurements.json` SHA-256 `0d4d5529f3c255ebaed244f52d151fe167a6c6a84cd041716c3baddbb35c5d0e` matches the report; `artifact_count` 17, `failures` `[]`, all 17 true peaks finite.
- Independent capability re-run in a temp copy (`cp measure_audio.py + 17 WAVs`, run `--probe-truepeak-r101`): exit 0, `failures: {}`, `coverage_blocked: {}`, 17 finite peaks, the same control values. The lane worktree was not written.

## 12. Defects by severity

**D1 — Medium — registry conformance: S011 `recheck = —` fails the fleet census validator.** `sources-census.sh validate` exits 1 with `E09 S011 recheck=—`; contract v1 lists `recheck` as ISO date or cadence. Fix: set the cell to `frozen` (as S009/S010) or `on-release`, and append the old→new cell value to the round lesson per contract rule 2. Scratch proof: after that one change the same validator exits 0 with only W01/W04 warnings. No claim is invalidated; this is a capability-row conformance defect.

**D2 — Medium — C3 measured-commit pointer is wrong for c3b.** The report and `SCORECARD.md` say all C1–C3 after-counts were measured at `d00a8d2`, but the c3b receipt path does not exist at that commit (`git ls-tree ... d00a8d2` → 0); the count is 17 at `343cd978e`, which is also the commit the report says carries the final receipt. The number is real; the "measured commit" attribution is not. Fix: record c3b at `343cd978e` and narrow the blanket sentence.

**D3 — Low — receipt/coverage wording.** "The final receipt reports ... no coverage blocks": the receipt JSON stores `failures: []` but has no `coverage_blocked` key; `coverage_blocked: {}` is printed by `main` and recorded in `LOG.md`. Cite the run output/LOG or persist the field.

**D4 — Low — "Four Core-gap rows moved into Core".** `corpus/README.md` keeps them under `### Core gap` with one entry each; no Frontier row advanced (the README did not exist at base). The claim "Frontier rows advanced: none" is correct; "moved into Core" overstates the index state.

**D5 — Low — ART/dossier id collision.** `corpus/SOURCES.md` Search log/lesson use `S014–S018`, `S019–S022`, `S023–S029` for ART dossier rows while registry rows S014/S015 are different sources. Context usually disambiguates ("the ART dossier's ..."), but a reader can conflate them. Label ART ids explicitly (e.g. `ART-S014`). This is also why a used-by sweep surfaces unmatched `S023`/`S029`; neither is a registry row and neither is a Q20 omission.

### Residual risk / verification gaps

- L2 batch shape (≥8 in one call) is attested by `LOG.md` and the seat reports; the repo cannot prove dispatch shape. Accepted as attestation.
- The pre-fix truepeak path did invoke `build_artifacts.py`; canonical bytes are identical base→head and `git status` is clean, but pre-fix mtimes/untracked writes cannot be reconstructed (already disclosed in M23 and the report).
- W01 (S007 tier-C mined) and W04 (superseding duplicate URLs) are warning-only; both are contract-consistent here, but the lane should not call the validator "clean" without distinguishing warnings from E-codes.
- M20→Q3 coverage is thin: Q3's lesson links are M13 only and its text does not state M20's "do not attribute a mismatch to version drift without comparing revisions" rule; the report says M19/M20/M25 are covered by Q5/Q3/Q11. Substantively acceptable, but worth a link/criterion if M20 is meant to be captured.
- `resume_continuity_v1` / resume paths are not present in this lane task (the continuation was a new L1, not a resume of a persisted runtime), so that check is not applicable.

## 13. Recommendation

**Admit with findings.** C1 (calibration), C2 (coverage + `sources-registry`) and C3 (depth + `truepeak-probe`) all verify at `343cd978e`; recommended axis verdicts are claim-verified with scores honestly unchanged (`unmeasured`). Require D1 (S011 `recheck` cell) and D2 (c3b measured-commit pointer) before closure; D3–D5 are precision/wording fixes. No axis is harmed. This is a non-author recommendation only; the round remains `unadjudicated` until the orchestrator records an adjudication (Q11).

---

# Addendum — 2026-10-20 — targeted recheck of lane HEAD `0d26ef01e` (parent-steered corrections)

Scope: targeted recheck only; original review above preserved. Read-only, own scratch only; no full test suite or probe run (parent runs the 10-test smoke).

## A1. Provenance and append-only of the four new commits

`git log --format='%h %an <%ae> | %cn <%ce> | %s' 343cd978e..HEAD` →

```
0d26ef01 audio-shokunin <audio@shokunin.local> | audio-shokunin <audio@shokunin.local> | round-101: delete mock-dispatch truepeak CLI tests
3fdbecdc ... | round-101: record corrected final measurements
02c13307 ... | round-101: record corrected true-peak run
ba46f371 ... | round-101: correct true-peak acceptance oracle
```

Protected paths over `343cd978e..HEAD`: `LOG.md` 16/0 and `corpus/lessons/round-101.md` 20/0 (additions only); `corpus/SOURCES.md` 1/1 = the permitted S011 `recheck` cell only (cell-by-cell compare: `— → on-release`, all other ten cells byte-identical); `corpus/QUALITY.md` 1/1 = R1 below. Lane worktree clean; branch `kaika/round`.

## A2. D1 — resolved

S011 `recheck` = `on-release` (`corpus/SOURCES.md:19`); lesson:155 logs `— → on-release`; the fleet report's 2026-10-20 erratum repeats it. `bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-ledger/scripts/sources-census.sh validate <lane> --today 2026-10-20` → **exit 0**, `ok`, with only `W01 S007` and `W04 S014/S015` warnings. The assignment's `fleet-census/scripts/` path no longer exists in the tree; the script now lives in the fleet-ledger worktree (path drift, not a lane defect).

## A3. D2 — resolved

`SCORECARD.md:1055` separates measured commit `02c1330708962b5c68938c71bce9658d516dc63e` (fresh receipt and all after-counts), C3 code-work commit `ba46f3718a8b18bf3c4695e1e4de6c8d21a86af8`, and the later measurement-record commit; `M26` records the class. Re-ran the counters against the `02c13307` tree: c1a–c1e = 14/18/2/0/0; c2a–c2e = 18/4/15/22/4; c3a = 2; the c3b receipt is committed in that tree (44 files under the run dir) and its blob holds 17 finite artifact true peaks. The reported receipt SHA-256 `2ce0a0f57757ff9d4a21739da1615566fff41b4ac9855d0ac916d28270ce7f40` matches the committed blob.

## A4. D3–D5 — documented, not promoted

`corpus/lessons/round-101.md:159` (`coverage_blocked` is CLI stdout, not a stored receipt field), `:160` (ART dossier IDs S014–S018 are a separate sequence from registry S014/S015), `:161` ("no Frontier row was promoted into Core"); the report erratum repeats all three. The pre-erratum report lines 27/74 (`d00a8d2`; "moved into Core") remain in the superseded sections; the erratum supersedes them, and the integrator should cite the erratum at closure.

## A5. Critic C3 Q22 counterexample — resolved

- Gate usage at HEAD: the name-keyed analytic oracle alone appends a control failure (`measure_audio.py:54809-54823`); quantized expectations/errors are recorded as non-gating telemetry fields (`quantized_pcm16_expectation`, `overshoot_error_db`, `true_peak_error_db`, `sample_peak_error_db`, `quantized_pcm16_expectation_error`). Remaining failure paths are analytic mismatch, non-numeric integrated loudness, dual-mono delta, and artifact checks.
- New real-CLI regressions prove both directions: `test_real_cli_keeps_quantized_disagreement_non_gating` forces the positive control's quantized overshoot to 0.0 and gets exit False, `failures == []`, `analytic_overshoot_matches` True; `test_real_phase0_positive_generator_fails_analytic_gate` mutates the positive control to phase 0 and gets exit True, `analytic_overshoot_matches` False, with "independent analytic reference" in `failures` (the self-validating mutation the critic described now fails).
- Faded controls (5 ms fade, steady window 240) sit inside the ±0.08 analytic band: fresh receipt positive +2.999335 vs +3.0103 (error 0.010965), phase-0 0.000, dual-mono 3.010 vs 3.0103 (±0.002, error 0.0003).
- Fresh receipt `corpus/live/round-101-truepeak/20261020T001910858001Z/measurements.json`: 17/17 finite artifact true peaks, `failures: []`, gated 9 / short-floor 8; all 17 artifact `sha256` fields equal the canonical WAV bytes; controls carry source path, sha256, frames, rate, channels, format. Fresh vs prior receipt artifact true peaks: 0 differences.

## A6. New residual findings (non-blocking)

- **R1 (low, conformance):** `corpus/QUALITY.md:20` (Q12 lesson pointer) was modified in place, `#M6` → `#M6, #M26`, in `ba46f371` — a prior-line modification in a path the round treats as additions-only, and not logged old→new (unlike S011's `recheck`). Recommend a lesson note or an appended criterion.
- **R2 (low, staleness):** `SCORECARD.md:1079,1086` and `corpus/lessons/round-101.md:167` still say 12 tests; HEAD's suite has 10 after `0d26ef01` deleted the two mock-only dispatch tests. The fleet report's post-HEAD bullet documents the 10-test run at `0d26ef01`; the lane capability pointer remains as-measured at `02c13307`. Recommend one appended line if closure cites the suite at HEAD.
- **R3 (low, coverage delta):** with those two tests deleted, normal-mode builder dispatch is covered only by the recorded temp-copy default-mode run (receipt SHA `8e8cdad6…`) and unchanged `measure()`/`SPECS`, not by an automated test; truepeak no-builder stays guarded inside both real-CLI tests (`command_without_builder` raises on `build_artifacts.py`).
- §12 residual items (L2 batch-shape attestation, pre-fix mtime, W-code wording, M20→Q3 link) are unchanged.

## A7. Disposition (unchanged recommendation)

C1/C2/C3 remain verified at the corrected measured commit `02c13307`; D1/D2 resolved; D3–D5 documented; the Q22 counterexample is falsified by the new real-CLI regressions plus the fresh 17-peak receipt with source-blob provenance. Recommendation: **ADMIT-with-findings** with R1–R3 as documentation/coverage nits. Sampled disposition unchanged: agree with the K4 and K5 admits and the K2 and S011 rejects. Verification limit: I did not run the 10-test suite or the full probe (parent runs smoke); assessments rest on code, tests, committed receipts and hashes. Round remains `unadjudicated` per Q11.
