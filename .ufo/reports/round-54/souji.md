# souji round 54 — report

Round 54, attempt 1. Lane `souji` (`/home/vgpnk/Projects/shokunin/souji-shokunin`). Base `fe12daad2549f534650d406ebdbac9113d59313f` (r53 non-author spot-check commit). Freeze `3c394cab0cd406bbab72b8d365e0f3deed4ef98a`. Capture commit `bfdbb336329e6afba3ab1ca83cbd6d9759271062`. Content tip `0fada8b33988e9de377566798b4f5a8fd4d10060`. Final lane commit (wave close) `8fb6fbc651f1f1d31f77f944a2e3389bb4a9e894` — the report cites this hash.

## Work performed

Declared claims (2, one per distinct axis; no exploratory claim; no assimilation):
- **C1 — calibration 7** (lowest non-retired axis): the annotation-agreement counter amended to v3 (`census/round-54/c1-counter.py`) to instrument the r53 routed filing surfaces. Target: v3 kills 11 of 13 matrix rows (v2 kills 5), each with its named finding; F1 and F12b green; real lane exit 0. **Verdict: verifies on its frozen predicate; carries a HIGH named limit (S1, below) that the operator must rule on (L0).**
- **C2 — coverage 8**: the capture counter amended to v3 (`census/round-54/c2-counter.py`) to instrument the widened `#`-row shape, unknown receipt keys, CAPTURE-CRLF, the `--tool-sha256` pin, and branch fixtures FA7/FA8/FH2. Target: v3 kills 8 of 10 rows (v2 kills 6); real lane exit 0 over the fresh capture. **Verdict: verifies; no HIGH limit.**

Work items with evidence:
- Protocol load and round start: `skill://shokunin`, kimi-shokunin protocol files, `MISSION.md`, `AXES.md`, the lane SKILL/PROVINCE/SCORECARD, `corpus/QUALITY.md`, `corpus/lessons/round-53.md` and `round-53-verifier-spotcheck.md`. Round-start census: `census/round-54/records/census-before-receipt.txt` (CONF-RC=0 DIR-RC=0 DIR-RESULT=ok, RECEIPT-SHA256 `6fdebcae…`); base note `census/round-54/records/base-note.txt`; porcelain at base `census/round-54/records/porcelain-at-base.txt` (1 line: this round's own directory).
- Pre-freeze instrument work: v3 counters, extended fixture builder (pinned GIT dates, hardened git env), expected TSVs, controls. Selftests with pins: `census/round-54/records/c1-selftest.txt` (`SELFTEST pass cases=13`, EXIT=0), `c2-selftest.txt` (`SELFTEST pass cases=10`, EXIT=0). Negative pins exit 2 (`CANNOT-EVALUATE PIN-MISMATCH`) in both controls.
- Freeze: `census/round-54/preregistration.txt`; `census/round-54/records/freeze-check-at-freeze.txt` → `SUMMARY claims=2 findings=0`. Pinned instruments: c1-counter `f45d3d8f…`, c2-counter `84b05295…`, builder `ae5881f8…`, run-matrix `f9d27763…`, expected TSVs `4e73c495…` and `e32f7934…`.
- Frontier step: live fetch of CommonMark 0.31.2 by scribe seat S54scribe01 (curl HTTP 200, no redirect, 514698 bytes, sha256 `c85f56cc…f0d`); five located quotes re-verified by the L1 as verbatim substrings of the pinned capture (`census/round-54/sources/s277-located-quote.txt`); knowledge entry `corpus/knowledge/correction-filing-fence-grammar.md` (sources S277 and S276).
- Matrices (`census/round-54/fixtures/run-matrix.sh`): `census/round-54/records/c1-matrix-v2.tsv`, `c1-matrix-v3.tsv`, `c2-matrix-v2.tsv`, `c2-matrix-v3.tsv`. Fixture revs reproduce across builds (executor01, critic01).
- Real-lane receipts: `c1-tip.txt` and `c2-tip.txt` at `bfdbb336`; `c1-content-tip.txt` and `c2-content-tip.txt` at `0fada8b3`; re-run at the final lane commit `8fb6fbc6` (both exit 0, see the measurement table note).
- Capture: `census/round-54/records/fleet-root-census.tsv` and `fleet-root-census-run.txt` (RECEIPT_VERSION=1, 49 entries, fleet HEAD `3b0d5329`), staged outside the fleet root and copied cmp-exact. Connector01 confirms no new top-level fleet entry since that HEAD, so ENTRIES=49 stands.
- Wave w1: one v1 wave, 12 seats, all settled with output and reports (`census/round-54/wave/w1-results.json`; spec `w1-spec.json`; dispatch `w1-dispatch.json`; registry `swarm-registry.json`; seat reports `census/round-54/wave/S54*.md`).
- Standing receipts: r53 c1/c2 green at `bfdbb336` (executor03); r52 c1/c2 and r51 c1/c2 green; landing suite (`census/round-46/c1-counter.py`) on a clean clone at `0fada8b3`: `census/round-54/records/landing-suite-content-tip.txt` → `SUMMARY assertions=579 mismatches=76 registered=76 corrected=0 exempted=0 unfiled=0`, rc 0. At `bfdbb336` it read `assertions=570 mismatches=74 registered=74`, rc 0. The two new mismatches are new round text; all are registered and unfiled is 0.
- Round-end census: `census/round-54/records/census-after-receipt.txt` (CONF-RC=0 DIR-RC=0 DIR-RESULT=ok W04=61; `VERIFY ok`).
- Routed-item disposition (r53 verifier §6): §6.1 (report count) — the r53 report's "six rows" is wrong (the table has seven); recorded as a mistake, with the counting command; §6.3 (prereg wording) — closed; §6.4 (oracle/builder pins) — closed; §6.2 (wave-results pointer) — integrator-owned, not closed here.
- Attacks (wave seats, advisory; full detail in `corpus/lessons/round-54.md` `## Wave findings`):
  - sentinel01 (write-scope review): verdict CONDITIONAL PASS — 1 HIGH, 2 MEDIUM, 2 LOW, 2 named-limit observations. Host trust boundary intact. **S1 HIGH: the C1 fence refusal is defeated by exotic line separators** (see Named limits). The L1 reproduced S1 independently (`census/round-54/records/s1-formfeed-reproduction.txt`): the committed F7 shape with two form-feed lines above the `~~~` fence goes from exit 1 (`fenced=2`) to exit 0 (`filed=2 unfiled=0 fenced=0`).
  - critic01: both claims SURVIVE the frozen predicates and kill rules; vacuity probes show the v2 arm kills none of the new fixtures. Seven named limits (N1–N7); N2–N4 are false statements in the frozen prereg and control, filed as errata.
  - reviewer01 (C1 attack, 60 counter runs over 31 states): six routed defect classes R1–R6 on states outside the frozen fixtures (hidden-correction swallow, dual-anchor aliasing, pair-filing stale drop, rows-word dodge, fence over-hide against CommonMark, pair-scan fence false positive). No attack makes v3 exit 0 on F1 or F12b.
  - reviewer02 (C2 attack): zero routed defects against the frozen claim; five named limits NL-1–NL-5.
  - mutation01: 9 of 12 mutants killed; survivors M2, M7, M11 (coverage gaps, none equivalent).
  - connector01: NO-OVERLAP on all three declared surfaces (20 sibling lanes counted); PTR — the pointer exemption `PTR_RE` is path-unscoped (a timestamp hides an overstating pair line; measured).
  - executor01: AGREE 13/13 (C1). executor02: AGREE 10/10 (C2). executor03: standing receipts 11/11 green. scout01: tip, zone, append-only, freeze and ancestry checks, all pass. scribe01: S277 live fetch and quotes. revenger01: routed-item reproduction (§6.1 red; §6.3, §6.4 green; §6.2 unresolved, integrator-owned).
- Errata (append-only): `corpus/lessons/round-54.md` `## Wave findings` ERRATUM-R54-1 (the wrong-pin refusal is shown on the real lane, not in the selftest), ERRATUM-R54-2 (the F11 mechanism clause), ERRATUM-R54-3 (the control's "filed=no is not printed" line); filed also as R54-CORRECTION lines in SCORECARD.md.

Round shape and seats:
- One v1 wave, 12 seats: scout ×1, executor ×3, scribe ×1, reviewer ×2, critic ×1, mutation-tester ×1, sentinel ×1, connector ×1, revenger ×1. The L1 holds the canonical planner seat (not a swarm seat). Attack roles by the protocol definition (reviewer, critic, mutation-tester, labrat): 4 of 12 = 33% (≥25%); connectors 1 (≤2). Residual calls: none. Round total: 12 swarm seats.
- Dead seats: none (all 12 returned output and reports; `w1-results.json`).
- Routing: no model argument passed; roles routed through the global run-15 table.

## Landed changes

- `3c394cab` — round-54 freeze: preregistration, both v3 counters, builder, run-matrix, expected TSVs, controls, pre-flight receipts. LOG: `## Round 54` entry (landed in `0fada8b3`).
- `bfdbb336` — round-54 C2 capture (fleet-root census at fleet HEAD `3b0d5329`, RECEIPT_VERSION=1 run receipt). LOG: `## Round 54` entry, Capture bullet.
- `0fada8b3` — round-54 content: S277 registry row; S276 used-by old→new; S277 search-log note; knowledge entry `corpus/knowledge/correction-filing-fence-grammar.md`; lesson `corpus/lessons/round-54.md`; LOG round 54 entry; SCORECARD measurements and r55 plan; SKILL r54 gate rows; corpus README frontier note; matrices and tip receipts; wave evidence. LOG: `## Round 54`.
- `8fb6fbc6` — wave close: lesson wave findings for sentinel01 and connector01, mistakes (8 rows), named limits, knowledge-entry qualifications (S1, S2, PTR), SCORECARD r55 plan leading with v4, SKILL limit line, end-of-round receipts (census-after, landing-suite content tip, S1 reproduction, content-tip C1/C2), wave evidence. LOG: `## Round 54` addendum (appended after the wave closed).
- Fleet repo (this commit, via `fleet-commit.sh --as souji`): this report; the L0 question line in `.ufo/l0-questions.md` (`souji | round-54 | Operator ruling wanted on C1's admission …`).

## Before → after measurements

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| C1 (calibration 7) | v2 arm kills 5 of 13 matrix rows (F2–F6); F7–F12 exit 0 | v3 kills 11 of 13, each with its named finding; F1 and F12b green; real lane exit 0 `unfiled=0 record_sha=ok appended=ok multi=0 inert=0 fenced=0 straddle=0 bogus=0 logunfiled=0 logrecomp=0` | `awk -F'\t' 'NR>1 && $5==1{n++} END{print n+0}' census/round-54/records/c1-matrix-v2.tsv` → 5; same on `c1-matrix-v3.tsv` → 11; `python3 -B census/round-54/c1-counter.py --root . --rev 8fb6fbc651f1f1d31f77f944a2e3389bb4a9e894 --base fe12daad2549f534650d406ebdbac9113d59313f --record-sha256 2b90a262c29772d4a9a7bd5ab29ce06b9d8f350832f0d0cd5114d52b0f6dad30 --sources-rev-before f778b9d131574d3ff09c0cc8a077643c0fc84bb4 --sources-rev-after 9bf9234ae4d11c7b31706354302a9e95ad0d1f81 --scratch DIR` → exit 0 | fixtures: builder-deterministic revs; real lane `8fb6fbc6` (also `0fada8b3`, `bfdbb336`) |
| C2 (coverage 8) | v2 arm kills 6 of 10 rows; FA4 and FA5 exit 0; FA6 first finding spurious | v3 kills 8 of 10 (FA4 COMMENT-AMBIGUOUS-NAME, FA5 RECEIPT-UNKNOWN-KEY, FA6 CAPTURE-CRLF first); FH and FH2 green; real lane exit 0 `receipt=ok sorted=ok tool_pin=ok` | `awk -F'\t' 'NR>1 && $5==1{n++} END{print n+0}' census/round-54/records/c2-matrix-v2.tsv` → 6; same on `c2-matrix-v3.tsv` → 8; `python3 -B census/round-54/c2-counter.py --root . --rev 8fb6fbc651f1f1d31f77f944a2e3389bb4a9e894 --capture census/round-54/records/fleet-root-census.tsv --receipt census/round-54/records/fleet-root-census-run.txt --tool-sha256 e7e79952f7830d75c5b0eee35c2369716053f40121c7d3be370f7abdda067a5b --scratch DIR` → exit 0 | real lane `8fb6fbc6`; base `fe12daad` has no capture (control rc 128) |

Note on the measured commit: the matrices are fixture-revision runs from the deterministic builder (revs reproduced across builds). The real-lane recomputes were run at `8fb6fbc6` (final), with earlier identical-exit runs at `bfdbb336` and `0fada8b3`.

Owned scores: calibration 7, coverage 8, operability 8 — unchanged. Both claims are instrument amendments, and the kill-power over committed attack fixtures is the measured move. No capability row (no new repertoire demonstrated).

Admission verdict per claim (reported, not ruled; the operator rules):
- C1: verifies on its frozen predicate (every frozen kill and green check holds on the committed bytes). Carries **HIGH named limit S1**: the fence refusal is defeated by two form-feed lines above a `~~~` fence (exit 0). The kill rule names committed fixtures only, so this is recorded as a named limit, not a kill-rule breach. **Operator ruling requested** (L0): admit C1 with S1 recorded and fixed in r55, or hold C1 unadmitted until counter v4 lands.
- C2: verifies on its frozen predicate; no HIGH limit (the `--tool-sha256` pin is shown on the real lane; the selftest does not reach that branch, ERRATUM-R54-1).

## Sources & frontier

- `corpus/SOURCES.md` rows: **200 at base `fe12daad` → 201 at content tip `0fada8b3`** (final lane tip `8fb6fbc6` unchanged in the registry). Count: `git show <rev>:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`. Census: `./scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` → exit 0 at `8fb6fbc6` (201 rows, malformed 0, no duplicate id). Round start: `census-before-receipt.txt` CONF-RC=0 DIR-RC=0; round end: `census-after-receipt.txt` CONF-RC=0 DIR-RC=0 VERIFY ok.
- Rows added by tier: S277 (tier A, kind docs; CommonMark 0.31.2 §4.5 and §4.6; opened live 2026-11-03; status `mined`, cited by `correction-filing-fence-grammar.md`).
- Rows touched old→new: S276 `used-by`: `corpus/knowledge/fleet-root-capture-receipt-grammar.md` → `corpus/knowledge/fleet-root-capture-receipt-grammar.md, corpus/knowledge/correction-filing-fence-grammar.md`. S277 `queued` → `mined` (same commit as its citing entry). No other status, recheck or used-by cell changed.
- Search log: one bounded search (CommonMark spec, sections 4.5 and 4.6) recorded in `corpus/SOURCES.md` `## Search log`; C2 reuses S276 without a new search.
- Frontier rows advanced: none. PROVINCE Core/Frontier unchanged; the knowledge entry sits on Core ground the lane already holds.
- Assimilation: none (shokuknow `merge/souji/` held by the open r46 L0 question; `considerthese/` absent — `ls | grep -ci consider` → 0, rc 1).

## Trend verdicts

- **expansion: unchanged.** One admitted knowledge entry on Core ground (the correction-filing grammar, PROVINCE Owns), so no net new uncovered ground; `improved` is not claimed. The one new registry row (S277) is mined by that entry.
- **quality: improved, with a HIGH caveat.** Kill-power over committed attack fixtures rose on both counters (C1 5 → 11 of 13; C2 6 → 8 of 10); the r53 routed surfaces are instrumented; the standing r51/r52/r53 receipts are green at the tip; the r53 registry annotations still re-derive at the tip; no admitted entry failed a re-check. The S1 limit means the C1 instrument is not robust against exotic separators. v2 had the same F7 hole (it accepted F7 outright), so this is not a regression against the prior state, but it is not a quality gain on that surface, and the knowledge entry now says so.
- **discernment: unchanged.** Non-author attacks disagreed with the lane's own statements four times (the r53 "six rows" miscount; prereg F11 mechanism clause; the control's `filed=no` line; the prereg's selftest-pin citation). Each is recorded as an erratum or mistake with its evidence. Two further defects (S1, PTR) were found by non-author seats and are recorded as mistakes with routed fixes. No QUALITY criterion was added: none is yet shown able to fail, so discernment is not claimed improved.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md `## Round 54 contracts` (two v3 gate rows with entry commands, verdict maps, self-tests, pinned digests, write scope, owner; limit line for S1/S2/PTR); asserted by the lane (SoujiR54); evidence: SKILL.md r54 section; verifier: pending non-author closure.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md `## Round 54` and its addendum (capture, instrument amendments, wave, measurements, the S1 reproduction); evidence: LOG.md round 54; verifier: pending non-author closure.
- [~] Instructions executable by an agent without oral context — the round-54 gate commands in SKILL.md run from committed bytes; the independent reproductions (executor01 13/13, executor02 10/10) and the control rows are the evidence; verifier: pending non-author closure.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md unchanged; connector01 found NO-OVERLAP on all three declared surfaces across 20 sibling lanes; evidence `census/round-54/wave/S54connector01.md`; verifier: pending non-author closure.

## Stale-lane, holds, L0, incidents

- Stale-lane: none — respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (host python3 and git only; no pacman, uv, npx or binary install was needed). Recorded for the report contract.
- Open L0 questions routed around, not answered or assumed: credential-shaped names refuse-vs-redact (r52); `ignored`-column derivation (r52); r46 mass id drift (assimilation held); r48 census conf-form (this host: conf form rc 0, recorded).
- **New L0 this round** (`.ufo/l0-questions.md`, `souji | round-54 | Operator ruling wanted on C1's admission …`): admit C1 with the HIGH named limit S1 recorded and counter v4 first in r55, or hold C1 unadmitted until v4 lands.
- Protocol-integrator item (not this lane): the r53 verifier §6.2 — round-53 fleet-side wave artifacts are not durable; this round's wave evidence is committed under `census/round-54/wave/`.
- Misroot sweep (run before this report): `git -C /home/vgpnk/Projects/shokunin status --porcelain` → only the orchestrator-owned `.scratch/` entries (never a misroot); nothing moved.
- Mistakes (lesson `## Mistakes`): **8 rows**. Count command: `awk '/^## Mistakes/{f=1;next} /^## /{f=0} f && /^\| /' corpus/lessons/round-54.md | tail -n +2 | wc -l`.
- Scratch: every seat's scratch tree was removed before yield (per seat reports); the L1 removed `/fast/scratch/hyaku/souji-r54/` run trees after the receipts were copied.

## Named limits (routed to r55; none edits the frozen bytes)

- **HIGH — S1 (sentinel01; reproduced by the L1):** the C1 fence refusal is defeated by exotic line separators. `hidden_lines()` numbers lines with `str.splitlines()` (also breaks on `\x0b \x0c \x1c \x1d \x1e \x85 \u2028 \u2029`); the correction's own line number counts only `\n`. Committed F7 shape with two form-feed lines above the fence: exit 0, `filed=2 unfiled=0 fenced=0`. Fix: counter v4 with one line model, red-before fixture F7-FF committed first.
- **MEDIUM — S2 (sentinel01):** the pair scan is ASCII `->` only; LOG.md:1845 and LOG.md:1858 use `→` in the same idiom and are not scanned (both pairs below the registry count — a coverage gap, not a live misread).
- **MEDIUM — S3 (sentinel01; = reviewer02 NL-3):** the unknown-receipt-key regex is uppercase-only.
- **MEDIUM — PTR (connector01):** `PTR_RE = [A-Za-z0-9_.\-]+:\d` is path-unscoped; a timestamp hides an overstating pair line from UNFILED.
- **MEDIUM — reviewer01 R1–R6:** hidden-correction swallow behind a wrapper or with leading spaces (R1); dual-anchor aliasing (R2); pair-filing stale drop (R3); rows-word dodge (R4); fence over-hide against CommonMark 0.31.2 (R5); pair scan not hide-fenced (R6).
- **MEDIUM — mutation01 M2, M7, M11 (coverage):** the bare-short-run fence case (`F8b-BT4-SHORT-RUN`), the pointer exemption (`F12c-LOG-POINTER-EXEMPT`), the `--tool-sha256` selftest arm (`FA9-WRONG-TOOL-PIN`).
- **MEDIUM — reviewer02 NL-1, NL-2, NL-4, NL-5 and critic N5:** `#`-rows with four tabs silently dropped; prose comments with five tabs refused; whitespace-variant unknown keys evade the check; pin shape errors exit 2; SOURCES-RECOMPUTE-MISMATCH has no committed fixture.
- **LOW / named limit — sentinel S4–S6, critic N1, N6:** builder relative `--work` nests fixtures; the C1 docstring names a `PRISTINE FAIL` class it never emits (and `SOURCES-ANNOTATION-DRIFT`, which no code emits); `--scratch` accepted and ignored by both counters; R12 exit-code ambiguity undisclosed in the prereg.
- Erratum (not a limit): ERRATUM-R54-1..3 in `corpus/lessons/round-54.md`.

## Pre-report gate

- `git -C /home/vgpnk/Projects/shokunin/souji-shokunin ls-remote origin refs/heads/master` → `8fb6fbc651f1f1d31f77f944a2e3389bb4a9e894	refs/heads/master` (final lane hash, equal to the local tip; `jj-lane.sh state` → `local=8fb6fbc6 remote=8fb6fbc6 ahead=0 behind=0`).
- `grep -c '^## SHONEN' .ufo/reports/round-54/souji.md` → 1.
- `souji-shokunin` `census` gate at the final tip: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` → exit 0.
