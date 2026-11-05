# kagi — round 43 (attempt 1)

Lane repo: `/home/vgpnk/Projects/shokunin/kagi-shokunin`, branch `master`. Lane tip at report time: `65f66e17a313efd839db2a77e7156a313a1e363d` (`ls-remote origin refs/heads/master` matches; `jj-lane.sh state`: `ahead=0 behind=0 tracked=0 untracked=0`). Claim BASE `5f3566c4cfe65a74da4d201d74d28b403929807b` (round-42 tip). Frozen plan `plans/round-43.md`, predeclaration `a9180250955ad44530b565fa5b131b540c849199`.

## Work performed

Declared claims (three, one per distinct axis; none exploratory; no capability entered):

- **C1 — calibration.** The journal-gate counter gains a sixth forgery (F6: base row `R11-03` deleted, no journal entry) and must reject the three broken-instrument shapes the round-42 counter accepted (guard-drop mutant, token-drop mutant, answer-key gate). Target N = 6. BASE/before: round-42 counter 5 with all three broken shapes at 5. Measured after: `bash plans/round-43-c1.sh` = **6** at the candidate.
- **C2 — freshness.** A committed gate, `corpus/controls-replay.sh`, re-derives the eight manifest receipts of the round-41 and round-42 controls runners from the clone's own revision and refuses stale and silent fixtures. Target N = 1. Before: no gate, `bash plans/round-43-c2.sh` = 0. After: **1**.
- **C3 — operability.** Five lane gates' selftest scratch defaults move off `TMPDIR`/`/tmp` onto `${HYAKU_SCRATCH:-/fast/scratch/hyaku}`. Target N = 5. Before: `bash plans/round-43-c3.sh` = 0. After: **5**.

Work items, each with its evidence pointer:

- Round-start protocol load: `MISSION.md`, `AXES.md`, `SKILL.md` (lane), `PROVINCE.md`, `SCORECARD.md`, `corpus/QUALITY.md`, `corpus/README.md` (`## Frontier`), `corpus/lessons/round-42.md`, `corpus/lessons/round-42-verifier-spotcheck.md`, the round-42 plan and its verifier's routed items (§6).
- Predeclaration `a918025` (lane commit `a9180250955ad44530b565fa5b131b540c849199`): frozen plan `plans/round-43.md`; counters `plans/round-43-c1.sh`, `plans/round-43-c2.sh`, `plans/round-43-c3.sh`; controls runner `plans/round-43-controls.sh`; BASE receipts `.ufo/waves/round-43/controls/` (measured at `5f3566c`; `measured-at.txt`).
- Amendment A1 `dd6ccb92bf04a061e9f1e66913d15f097397b1b3`: the landing check's command form in kill rule C1(e) corrected to materialized files (`<(git show …)` refused at setup; corrected form `CLEAN (changed=6 journaled=6)`, rc 0).
- Amendment A2 `f2b4ec761b2fa40ecc621cd6fcbfa3e54788cff9`: six pre-measurement defects found by the critic and reviewer seats, closed as text or added clauses (kill clauses C1(f), C3(g) byte-pin the four round-43 instruments; restore-on-refusal clause C2(e); `final/` anchored; C3 fixture controls are the predeclaration receipts, A2-7). No predicate, target, counter or BASE reading changed.
- BASE eight-receipt re-derivation, committed as `.ufo/waves/round-43/controls/c2-manifest-rederive-base.txt`: 8/8 MATCH in a plain re-run and a delete-then-re-run at `5f3566c`.
- Wave `build` (10 seats; see roster below). Results: `.ufo/waves/round-43/build-results.json`; per-seat outputs: `.ufo/waves/round-43/build/<seat>.md` and `build/<seat>/`.
- Candidate commit `542885ed1514fd01d4e949caa5fab58eb000fffc`: `corpus/controls-replay.sh` (new; seat `K43ExecReplayGate`, sha256 `fab42e1d0a6b06b3608bb6a0543fad0da37a3c4e40ad85fd9c208cfb0d9e740f`, verified against the seat's recorded digest) and the five gate patches (seat `K43ExecScratchFix`; sha256s verified against `sha256sums.txt`; `patch -p1 --dry-run` clean first).
- Candidate measurements, in a fresh `git clone --shared` of `542885ed` (see `.ufo/waves/round-43/final/measured-at.txt`): counters 6 / 1 / 5; gate usage rc 2; clean clone CLEAN rc 0; stale fixture (D=2) REFUSED rc 1 with the controls directories equal to their pre-run state; silent fixture REFUSED rc 1 with the controls directories clean; landing check CLEAN rc 0; C1(d) gate bytes unchanged rc 0; C1(f)/C3(g) instrument pin rc 0; C3(c) selftests `SELFTEST: PASS (16 cases)`, `PREFREEZE_SELFTEST: PASS (25 cases)`, `SELFTEST: PASS (10 cases)`; C3(e) numstat 7 changed lines in 5 files.
- Registry: S094 `used-by` extended (round-42 routed item 2): `corpus/lessons/round-39.md` → `corpus/lessons/round-39.md, corpus/lessons/round-42.md, corpus/lessons/round-43.md`. S094 re-opened 2026-11-05 by the scout seat and re-checked by the L1: HTTP 200, 11296 bytes, sha256 `88556402940e7a0f1dbbed3abef9e00c87a90db6f80eaed03269e371f50050b8`, `cmp` exit 0 against `.ufo/waves/round-39/capture/S094.body`.
- Lesson `corpus/lessons/round-43.md` (claims, gate, mistakes M43-1…M43-7, frontier, routed, considerthese, assimilation, adjacency from the connector seat). QUALITY rows QM46–QM49 (`corpus/QUALITY.md`). SCORECARD pre/post blocks and LOG entry (`SCORECARD.md`, `LOG.md`).
- Lane commits (all via `jj-lane.sh`): predeclaration `a9180250`; amendment A1 `dd6ccb92`; amendment A2 + BASE receipt `f2b4ec76`; candidate `542885ed`; integration `65f66e17`.

### Wave shape and seat roster

ONE v1 build wave, 10 seats, validated under `scripts/hyaku/ufo-wave-policy.json` (band 8–16), dispatched through the inline spawn handoff (`.ufo/waves/round-43/build.ready` → `build.ready.dispatched`; spec `build-spec.json`, dispatch `build-dispatch.json`). Roles: executor 3 (`K43ExecC1Inst`, `K43ExecReplayGate`, `K43ExecScratchFix`), scout 1 (`K43ScoutS094`), scribe 1 (`K43ScribeDocs`), connector 1 (`K43ConnOverlap`), reviewer 2 (`K43ReviewC1`, `K43ReviewC2`), critic 1 (`K43CriticClaims`), mutation-tester 1 (`K43MutCounters`). Attack seats (reviewer + critic + mutation-tester) = 4/10 = 40 % (floor 25 %). Connector 1 (≤ 2). Planner duty held by the L1 (the validator rejects the role). Residual call: none. Round total: 10 seats.

Seat outcomes. `build-results.json` carries no per-seat `status` field (M42-5 recurring; see QM47). Status below is taken from each seat's own final output or deliverable:

| seat | role | per-seat status line | deliverable |
|---|---|---|---|
| K43ExecC1Inst | executor | none (settled; receipts recorded) | `build/K43ExecC1Inst/receipts.txt` |
| K43ExecReplayGate | executor | `SEAT-STATUS: complete` | `build/K43ExecReplayGate/` |
| K43ExecScratchFix | executor | none (settled; diff + receipts recorded) | `build/K43ExecScratchFix/` |
| K43ScoutS094 | scout | `SEAT-STATUS: complete` | `build/K43ScoutS094/notes.md` |
| K43ScribeDocs | scribe | `SEAT-STATUS: complete` | `build/K43ScribeDocs/` |
| K43ConnOverlap | connector | `SEAT-STATUS: complete` | `build/K43ConnOverlap/ConnOverlap.md` |
| K43ReviewC1 | reviewer | `SEAT-STATUS: complete` | `build/K43ReviewC1/attacks.md` |
| K43ReviewC2 | reviewer | `SEAT-STATUS: complete` | `build/K43ReviewC2/attacks.md` |
| K43CriticClaims | critic | none (settled; `findings.md`) | `build/K43CriticClaims.md` |
| K43MutCounters | mutation-tester | none (settled; `mutants.md`) | `build/K43MutCounters/mutants.md` |

Dead seats: none. Four seats settled without a status line; they are counted as settled with deliverables, not as `complete`, under QM47. No seat ran a lane write; the L1 applied every change.

## Landed changes

| change | commit | LOG entry |
|---|---|---|
| predeclaration: frozen plan, counters, controls runner, BASE receipts | `a9180250955ad44530b565fa5b131b540c849199` | Round 43 (2026-11-05) |
| amendment A1 (landing-check command form) | `dd6ccb92bf04a061e9f1e66913d15f097397b1b3` | Round 43 |
| amendment A2 (seat defects D1–D5, restore duty, C3 BASE receipts) + BASE manifest re-derivation receipt | `f2b4ec761b2fa40ecc621cd6fcbfa3e54788cff9` | Round 43 |
| candidate: `corpus/controls-replay.sh` + five selftest-scratch patches | `542885ed1514fd01d4e949caa5fab58eb000fffc` | Round 43 |
| integration: lesson, S094 `used-by`, QUALITY QM46–QM49, SCORECARD, LOG, `final/` receipts, wave evidence | `65f66e17a313efd839db2a77e7156a313a1e363d` | Round 43 |

Diff stats (re-derived this round with `git diff --numstat` over the named ranges, as QM46 requires): `git diff --numstat 5f3566c 542885ed` gives `corpus/controls-replay.sh` 144 insertions; `plans/round-43-c1.sh` 153, `-c2.sh` 82, `-c3.sh` 53, `-controls.sh` 206 and `plans/round-43.md` 247 (all added at predeclaration); `corpus/anchor-pins.sh` 1/1, `corpus/claims-declared.sh` 1/1, `corpus/prefreeze-control.sh` 2/2, `corpus/self-description-sweep.sh` 2/2, `corpus/surface-census.sh` 1/1 (7 changed lines, 5 files). `corpus/expect-journal.sh` unchanged (`git diff --quiet 5f3566c HEAD -- corpus/expect-journal.sh` rc 0). This is the diff-stat check the round-42 report's sentences lacked (round-42 report: +23/−3 and +7/−1 against 21/2 and 6/1 measured then; see M42-4 in the lesson).

## Before → after measurements

Counting commands, pasted outputs and the commit each was measured against. All run in fresh clones unless noted.

- **C1 calibration** — `bash plans/round-43-c1.sh`
  - Before (BASE `5f3566c`, round-42 instrument `plans/round-42-c1.sh`): `bash plans/round-42-c1.sh` → 5 (`controls/c1-old-real`; committed predeclaration receipt). Broken shapes under the old counter: `c1-old-m3-K1` 5, `c1-old-m5-K3` 5, `c1-old-fakeC` 5; blankets 0/0.
  - After (candidate `542885ed`): `bash plans/round-43-c1.sh` → **6** (`final/c1-new-real`, rc 0). Broken shapes under the new counter: `c1-new-m3-K1` 6, `c1-new-m5-K3` 6, `c1-new-fakeC` 5 (against target 6); blankets 0/0; K1 0, K3 0.
  - Broken-shape rejection: 0/3 → 3/3. Gate bytes unchanged (`corpus/expect-journal.sh`). Landing check `CLEAN (changed=6 journaled=6)` rc 0 (materialized base `git show 5142b52:corpus/claim-ledger.tsv`, journal `.ufo/waves/round-41/expectation-migrations.json`).
- **C2 freshness** — `bash plans/round-43-c2.sh`
  - Before (BASE): `controls/c2-base` → 0 (no gate at BASE; `git cat-file -e 5f3566c:corpus/controls-replay.sh` rc 128). Blankets `c2-blanket-0` 0, `c2-blanket-1` 0.
  - After (candidate `542885ed`): `bash plans/round-43-c2.sh` → **1** (`final/c2-base`, rc 0). Blankets `final/c2-blanket-0` 0, `final/c2-blanket-1` 0. Direct gate runs: clean `controls-replay: CLEAN` rc 0; stale fixture `REFUSED` rc 1, `controls` dirs equal to their pre-run state; silent fixture `REFUSED` rc 1, `controls` dirs clean.
  - BASE eight-receipt manifest: `controls/c2-manifest-rederive-base.txt` (8/8 MATCH, both modes).
- **C3 operability** — `bash plans/round-43-c3.sh`
  - Before (BASE): `controls/c3-base` → 0 (all five gates carry `TMPDIR:-/tmp` defaults; leg 1 fails for each).
  - After (candidate `542885ed`): `C3_ROOT` default (lane) → **5** (`bash plans/round-43-c3.sh`, rc 0). Fixture controls: `controls/c3-pos` 1 (one gate fixed), `controls/c3-blanket` 4 (every grep leg fixed, surface-census PASS token sabotaged) — both predeclaration receipts (A2-7), committed at `a918025`.

## Sources & frontier

- **SOURCES.md rows before → after:** census `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi` → `kagi ok`, **98 rows** at round start and round end; exit 0 at round start and round end. Rows added by tier: none. Rows touched old → new: **S094** `used-by` `corpus/lessons/round-39.md` → `corpus/lessons/round-39.md, corpus/lessons/round-42.md, corpus/lessons/round-43.md` (permitted in place; `status` `mined`, `recheck` `90d` unchanged). W04 duplicate-URL warnings: 19 at round start and 19 at round end, counted by `grep -c W04` (warnings allowed; exit 0).
- **Sourced claim:** C2 rests on S094 (the registry's in-place rule), re-opened 2026-11-05 (scout seat `K43ScoutS094`; L1 re-check: `cmp` exit 0, sha256 `88556402…`, 11296 bytes). Located quote (8 tokens): *"Only `status`, `recheck` and `used-by` change in place"*, raw offset 6172, line 116. C1 relies on S094 only by analogy and says so in the lesson. The `teaches` cell is unchanged.
- **Frontier rows advanced:** the calibration ground (journal-gate counter discrimination of counter-mutant and answer-key shapes, `corpus/lessons/round-43.md` §Frontier); the freshness ground (committed controls-replay gate); the operability ground (five selftests honour the lane scratch root). No frontier-to-core move; no `corpus/knowledge/` entry.
- **Mistakes mined** (`corpus/lessons/round-43.md` §Mistakes): M43-1 (frozen kill-clause command refused at setup), M43-2 (runner's C3 fixture section fails by construction at the candidate), M43-3 (C3 narrative misdescribed two gates), M43-4 (receipt-name notation), M43-5 (restore duty not pinned on refusing runs), M43-6 (instrument bytes not pinned to landing), M43-7 (named, routed: the C2 counter's N1 and N2 legs have no negative fixture in the frozen battery; mutants y1/y2 survive). Captured-by is recorded per row; the seat-caught ones were caught before any candidate measurement.
- **Assimilation:** none this round (no `merge/kagi/` theme matches the three instrument claims).
- **considerthese:** latest file `considerthese/2026-10-26.md`; proposals 1 and 3 remain unimplemented, reason recorded in the lesson.
- **Adjacency (connector seat):** `.ufo/waves/round-43/build/K43ConnOverlap/ConnOverlap.md` — 20 sibling lanes; overlap 5, adjacent 39, none 6 (by category in the lesson §Adjacency). Explicit answers: kake r91 already re-derives controls in a clone at a revision (fleet prior art for C2, not absorbed); mado, kotoba and kake already verify counter discrimination against answer-key or negative fixtures (fleet prior art for C1's principle; C1's matrix is kagi-local in arrangement).

## Trend verdicts

- **expansion: unchanged.** No registry row added and no knowledge entry; the only registry change is the `used-by` extension of S094. Evidence: census 98 → 98, exit 0 both ends; `git diff --numstat` over `corpus/SOURCES.md` shows 1 changed line (the S094 row).
- **quality: improved.** Freshness (C2) and operability (C3) moved to their frozen targets with committed evidence: a committed gate refuses stale and silent fixtures (`final/c2-base` 1, `c2-blanket-*` 0/0, `controls/c2-manifest-rederive-base.txt` 8/8), and the five selftests no longer depend on `/tmp` (`controls/c3-base` 0 → `final`-measured 5, counter `plans/round-43-c3.sh`). Named ceilings: the C2 counter's N1/N2 legs survive mutation (M43-7); the gate is not yet scheduled; the gate's default verification is reviewed as code.
- **discernment: improved.** Calibration (C1) moved to its frozen target: the instrument refuses the three broken shapes it accepted at round start (broken-shape rejection 0/3 → 3/3; `final/c1-new-m3-K1` 6, `final/c1-new-m5-K3` 6, `final/c1-new-fakeC` 5 < 6). Named ceilings: a six-key answer-key gate still reaches N = 6.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Gate registry and §Vault-ops decision table (unchanged this round; not re-verified by a non-author).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round-3 entry (stdin→lock→tmux→serve to the 1Password auth gate); this round's work is instrument-level, not vault contact.
- [~] Instructions executable by an agent without oral context — `plans/round-43.md`, `plans/round-43-c1.sh`, `plans/round-43-c2.sh`, `plans/round-43-c3.sh`, `plans/round-43-controls.sh` and `corpus/controls-replay.sh` run as written (`bash …`), with receipts under `.ufo/waves/round-43/`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` §Surfaces and `corpus/scope-gate.sh`; the connector's sibling sweep (`.ufo/waves/round-43/build/K43ConnOverlap/ConnOverlap.md`) found kake r91, kasegi and mado overlaps, recorded as fleet prior art and not absorbed.

No box is `[x]`: no non-author verifier has checked these boxes.

## Stale-lane

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Tool installs

None. The round used only existing tools (bash, git, jj-lane, python3 stdlib, sha256sum, patch, curl, sleep). No pacman transaction; no sysctl or host-service change.

## Errata

- Round-42 report (`.ufo/reports/round-42/kagi.md`) diff-stat sentences (+23/−3, +7/−1) disagree with `git diff --numstat` (21/2, 6/1), per the round-42 spot-check §6 item 1. Not rewritten; this round's QM46 and the lesson's M43 entries carry the correction. The owed in-place erratum of the round-40 report (round-41 routed item 3) remains unclaimed.

## Routed (named, not claimed this round)

1. C2 counter negative fixtures for N1 and N2 (M43-7; `build/K43MutCounters/mutants.md` y1, y2) — a counter amendment before data, next round.
2. Schedule for `corpus/controls-replay.sh` (no runner runs it yet).
3. `expect-journal.sh` `*.json` discovery failing closed on a wave directory (frozen interface; no slot).
4. C3 counter defects M40-9 / M40-10 / M40-17 (round-40 instruments).
5. Considerthese `2026-10-26.md` proposals 1 and 3.
6. Six-key answer-key ceiling of C1.

## Open items

- L0 question open (operator-owned): `.ufo/l0-questions.md` line 368 — the retirement form for the unconditional `DELETED` rule (`kagi | round-42 | …`). Routed around; no answer assumed. No new L0 question this round.
- Results-file gap: `build-results.json` has no per-seat `status` field (M42-5 recurring); four seats lack an explicit status line. QM47 records the rule; the wave-prompt template needs the status requirement, a fleet-root change outside this lane.
- Trend verdicts and claim verdicts are the L1 reading, for the non-author closure and the operator's ruling; no claim is self-admitted.

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` (no pathspec) → one entry, ` M .scratch/run15-state.json` (orchestrator-owned; not touched). No untracked fleet-root file names kagi round 43; no seat misroot to copy back. Recorded: none.

## Commit gates

- `git ls-remote origin refs/heads/master` on the lane → `65f66e17a313efd839db2a77e7156a313a1e363d`, the lane's final hash.
- `grep -c '^## SHONEN'` on this report → 1 (checked before commit).
