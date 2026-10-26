# tsukuroi — round 41 report (hyaku run 9, attempt 1)

L1: `TsukuroiR41`. Lane repo `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin`, measured base
`0e5805a1f149bd2ed9fe0db2e0a832afb034a835` (round-40 tip; the lane tip at round start was `8b7c4132`, which adds only the
round-40 spot-check lesson, and the operator's `1f5e74aa` considerthese commit was rebased under the freeze by the helper —
tools, census, SOURCES, knowledge and SKILL are byte-identical at all three; recorded as R41-BASE-MISREAD). Final lane hash
`6cc927dfcfaa66ca460eabe097fcce7ed5e23da0` (branch `master`, pushed; `git ls-remote origin refs/heads/master` prints it).
Round shape: **one v2 wave of 74 seats** (policy `scripts/hyaku/ufo-wave-policy-v2.json`, band 64–128) **plus a residual
call of 6 reviewer seats**; round total 80. Earlier attempts: none (no `lane-dead-no-report tsukuroi round=41` line); lane
clean at start.

## Work performed

Declared claims (`SCORECARD.md` "Round 41 — declaration", commit `d8b4d521`; counters frozen at `e479fdc5`):
- **C1 — operability**: the census `--selftest` gains four mount-table cases (relative mountpoint, non-`/dev` source, no
  `subvol=`, two btrfs lines) so the round-40 held-out survivors H5, H6, H9 and the count-direction mutant H10 fail it,
  under a counter with a decoy against self-reading selftests (routed R40-ANSWER-KEY).
- **C2 — depth (sourced, S227–S236)**: `corpus/knowledge/alpm-package-anatomy-r41.md`, ALPM package anatomy PA1–PA8 (format
  members, libalpm load requirements, makepkg member order, what install keeps in the local database, `.MTREE`, the
  `-Qkk` zero-error branch, PKGBUILD(5) working directories, vercmp order), with per-row reviewer verdict files required by
  the counter (QUALITY 81).

Work items:
- Protocol load: MISSION.md, AXES.md, CORPUS.md (SOURCES contract), LEARNING.md, the run-9 goal file, the round-40 report,
  lesson and spot-check (§6 five routed defects), QUALITY 81–88, `considerthese/2026-10-25.md` and `2026-10-26.md`.
- Sources opened 2026-10-26: pacman 54d9411 `be_package.c`, `add.c`, `be_local.c`, `version.c`, `makepkg.sh.in`,
  `PKGBUILD.5.asciidoc`, `src/pacman/check.c`, `query.c`, and alpm-package(7) (alpm-docs 0.13.0-1), snapshotted with digests
  in `.ufo/waves/round-41/frozen/src/SHA256SUMS`; read-only host capture `.ufo/waves/round-41/frozen/hostcap/` (1409 local
  entries: mtree 1409, install 51, changelog 0, dot files 0; all mtree gzip, none self-listed).
- Freeze `e479fdc5`: `tools/score-selftest-mounts-r41.py` (sha256 `8306d999…`), `tools/check-package-anatomy-r41.py`
  (sha256 `c83e29a4…`), snapshots, capture, two `SKILL.md` registry rows.
- Pre-data controls (`.ufo/waves/round-41/controls/`): C1 `declare -f` prologue on base and on candidate FAIL (`decoy_pass 0`),
  candidate minus the H9 case FAIL (`survivors 1, params 3`); C2 do-nothing, round-40 token writer, swapped and negated
  rules, one `fails` verdict, no verdicts, one `partly`-only row all FAIL, relation-literal writer FAIL only on verdicts,
  candidate with fixture verdicts PASS.
- C1 implementation `568c397d` (+27 lines in `run_selftest`, arm byte-identical). C2 implementation `c7c40c0f`, pre-dispatch
  refinement `9cc9aa77` (PA1, PA3, PA6 wording, before any seat).
- Wave `w1` (74 seats) attacked and verified both claims (reports `.ufo/waves/round-41/w1/*.md`); five second-read seats
  returned `partly` (PA2, PA3, PA5, PA6, PA7) → corrections appended `20c327b3`; residual call (6 reviewers) re-read the
  corrected rows and the C1 implementation (`.ufo/waves/round-41/residual/`).
- Integration `d7bf279f`: SKILL sections (C1 held-out tables, package anatomy decision table and `-Qkk` checklist step,
  counter lineage rows 13–14, counter-attack scoreboard), README round-41 section, QUALITY 89 (R41-GUARD-BYPASS), LOG entry,
  `tools/check-self-assessment.py --scratch` (R40-TMP-MISROOT), S220 anchor note on the round-40 entry (`20c327b3`).
- Outcome `64f9062e`: SCORECARD measured outcome, axes table (self-assessment 27 checked, 0 mismatches,
  `after/self-assessment-final.jsonl`), planned row, lesson `corpus/lessons/round-41.md`, sources census end.
- Residual addendum `6cc927df`: residual verdicts, results files, C1 final receipt, PA6 third-path note.

## Landed changes

LOG.md entry: "Round 41 — hyaku run 9 (stamp: the commit that lands this entry)" (commit `d7bf279f`).

| Commit | What |
|---|---|
| `e479fdc54d0977ccd8112a42d8d139baaebcb02e` | freeze: two counters, pinned sources, host capture, registry rows, start census |
| `d8b4d5217b2a74c7b7cddd33351c2a0cce5e8b84` | declaration, C2 controls, C2 before receipt, assimilation checks |
| `568c397da11339aed65181be598414f268835555` | C1: four held-out mount tables in the census selftest |
| `c7c40c0f370bcbaf4246de70a08c017119607c0f` | C2: entry PA1–PA8, S227–S236 |
| `9cc9aa77e30e0e23de2d4d2697b3b218ada02969` | C2 pre-dispatch refinement |
| `71851d636ab1bffaf8fee5016617c88878a666f1` | C1 controls, before/after receipts (dispatch tip) |
| `20c327b3f1cf96ad1828792c2ae5db71b5fd9ef7` | wave corrections PA2/PA3/PA5/PA6/PA7; S220 anchor note |
| `d7bf279f6551d92f379dbd3bb531803555fce7bd` | integration of w1 (reports, SKILL/README/QUALITY/LOG, tool fix, dispatch evidence) |
| `64f9062e6554e0f18fe162876293e0179fbbc78c` | measured outcome, axes table, lesson, receipts |
| `6cc927dfcfaa66ca460eabe097fcce7ed5e23da0` | residual verdicts and results, final receipts, addendum |

## Before → after measurements

| Claim | Counting command | Before (base `0e5805a1`) | After | Measured against | Verdict |
|---|---|---|---|---|---|
| C1 operability | `python3 tools/score-selftest-mounts-r41.py --revision <REV> --scratch <DIR>`; predicate `baseline_pass == 1 and neutral_pass == 3 and decoy_pass == 1 and mutants_applied == 13 and survivors == 0 and params == 4` | survivors 4 (H5, H6, H9, H10), params 0, FAIL (`.ufo/waves/round-41/before/c1-before.jsonl`) | survivors 0, params 4, baseline 128/128, PASS exit 0 | `568c397d` (`after/c1-after-568c397.jsonl`), `d7bf279f` (`after/c1-final-d7bf279.jsonl`) | **verified under the frozen predicate; counter sufficiency falsified** — a here-document-stripping text gate plus one shared fixture line passes with no new case (`w1/C1CritDecoy.md`); forged labels credited (`w1/C1CritLabels.md`). The landed bytes are four fixture cases, no self-reading construct (`residual/C1RevDiffRead.md` supports) |
| C2 depth | `python3 tools/check-package-anatomy-r41.py --revision <REV>`; predicate `rules_verified == 8 and verdicts_ok == 8 and host_ok == 6 and source_ok == 1 and duplicate_rows == 0 and duplicate_headings == 0 and novelty_base_hits == 0` | entry absent, 0/0/0/0, FAIL (`before/c2-before.jsonl`) | rules 8, verdicts 8, host 6, source 1, PASS exit 0 | `d7bf279f` (`after/c2-after-d7bf279.jsonl`); `9cc9aa77` all but verdicts (`after/c2-impl-9cc9aa7.jsonl`) | **not verified: the declared kill rule fires** — PA6 stays `partly` after its appended correction (`residual/C2RevPA6c.md`: the allocation-failure NULL path `be_local.c:263-265` unnamed); PA2, PA3, PA5, PA7 re-read `holds`; the verdict gate is also shown not to be an authorship check (`w1/C2CritControl.md`) |

No-harm: lane gates exit 0 at the dispatch tip (`w1/GateAllRegistry.md`); round-39 and round-40 C1 counters PASS
(`w1/C1ExecPriorCounters.md`); additions only (`w1/RevNoHarmAxes.md`); self-assessment 27/0 at `64f9062e` and at
`6cc927df`. Causal separability: `w1/CritSeparability.md`.

## Sources & frontier

- Rows: 226 → 236 — `grep -cE '^ {0,3}\| *S[0-9]{3,} *\|' corpus/SOURCES.md`; malformed 0.
- Census: start `tsukuroi ok`, exit 0, 39 W04 (`.ufo/waves/round-41/before/sources-census-start.txt`); end `tsukuroi ok`,
  exit 0, **40 W04** (`after/sources-census-final.txt`): the one new W04 is S230 (same add.c URL as S213, declared distinct
  scope; `w1/RoutedW04.md`).
- Rows added by tier: tier A 10 (S227 alpm-package(7); S228 be_package.c; S229 makepkg.sh.in; S230 add.c database members;
  S231 check.c; S232 PKGBUILD.5; S233 version.c; S234 be_local.c; S235 query.c; S236 own-work capture); B 0; C 0. All
  `mined`, opened 2026-10-26; Gate quotes in `corpus/lessons/round-41.md` `## Gate`.
- Rows touched old→new: none (S220's anchor drift corrected by an appended note in `pacman-exec-environment-r40.md`).
- Sourced claim: C2 rests on S227–S235 opened this round.
- Frontier: no Frontier area moves; C2 deepens held pacman-state Core (`corpus/README.md` round-41 section).
- Mistake mined: eight rows in `corpus/lessons/round-41.md` `## Mistakes` (R41-LABEL-SUFFIX, R41-CAPTURE-FIFO,
  R41-PIPEFAIL-SIGPIPE, R41-LEXICAL-OVERREACH, R41-CENSUS-PIPEFAIL-692 (live census wrong verdict, routed),
  R41-GUARD-BYPASS → QUALITY 89, R41-BASE-MISREAD, R41-TMP-MISROOT-REPEAT).
- Assimilation: theme "alpm package anatomy" (`merge/tsukuroi/…/alpm-package-anatomy-r26.md`, sha256 `3fa1b809…`):
  PA1, PA7, PA8 propositions admitted by re-grounding; the `package()`-in-`$pkgdir` sentence and the ground pointer
  rejected; no staged row, id or text adopted. Collision check: registry ids 226 at base, staged 147, collisions 27
  (S200–S226); guard proof indented `  | S227 |` 1 vs column-zero 0; renumber map by document: staged S215 → lane S227,
  staged S217 → lane S232 (asciidoc source). Quarantine slice 12 rows, none intersects this round's documents.
- considerthese: `considerthese/2026-10-26.md` proposal "Counter-attack scoreboard" → `SKILL.md` "Counter-attack
  scoreboard — rounds 40-41".

## Trend verdicts

- **expansion: unchanged.** The admitted entry deepens held pacman-state Core, no coverage-map ground newly held, no
  Frontier move (`w1/C2CritAxis.md`, `w1/CritTrend.md`).
- **quality: unchanged.** The C1 selftest now refuses four mutants that passed at the base and the round-40 entry's anchor
  drift is corrected, but C2 did not verify under its own kill rule (PA6), so no stronger entry is admitted this round.
- **discernment: unchanged.** The Gate records admits and rejects, five second-read disagreements became appended
  corrections and QUALITY 89 has its lesson, but both counters' guards were beaten by reading the guard and the outside
  spot-check is pending.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — round 41 adds the package-anatomy
  symptom → PA row → command table and the `-Qkk` mtree checklist step (`SKILL.md` "Package anatomy and the local database —
  round 41"); non-author verification pending.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` "Round 41 — hyaku run 9"; non-author
  replay pending.
- [~] Instructions executable by an agent without oral context — the round-41 tables carry paste-ready read-only commands
  (`w1/C2LabratQkk.md` replayed the `-Qkk` reproduction); whole-SKILL retest unexecuted.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `w1/ConnSiblings.md` sibling sweep; self-asserted.

## Round shape, seats, routing

- `w1`: 74 seats — executor 19, critic 18, reviewer 15, mutation-tester 5, scribe 5, connector 4, scout 3, sentinel 2,
  simplifier 2, revenger 1 (m_flash roles 47, 64 %; attack roles 38, 51 %). `labrat` is rejected by the validator, so the
  four empirical probes rode executor seats. Spec `.ufo/waves/round-41/w1-spec.json` (generator `make-w1-spec.py`),
  dispatch `w1-dispatch.json`, results `w1-results.json`. Residual: 6 reviewer seats, `residual-dispatch.json`,
  `residual-results.json`. Planner seat held by the L1. Round total 80.
- Dead seats: 0 — all 74 + 6 settled (orchestrator WAVE-DONE for both) and every seat wrote its report.
- Routing: run-8/9 role map from `~/.omp/agent/config.yml`; `model` never passed; no claim depends on a seat's model.
- Tool installs: none by the L1; no seat reports an install.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Open L0 questions: none filed this round.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `?? .ufo/reports/round-48/tameshi.md`
  (another lane's file, untouched) besides driver state; one seat built a 300 MB archive under `/tmp` (self-cleaned;
  R41-TMP-MISROOT-REPEAT); an orphaned `cp` from an L1 pre-freeze run was killed.
