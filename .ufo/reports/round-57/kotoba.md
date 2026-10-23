# kotoba — round 57 report (hyaku campaign, attempts 1–3)

Lane HEAD (pushed): `118d3ac4c6ca9db51d4b05a7dc2ce82d35cc4711` (`jj-lane.sh state` → `local=remote=118d3ac4… ahead=0 behind=0 tracked=0 untracked=0`). Base `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a`.
Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Work performed

Declared claims (plan `ee50d8fa`, `plans/round-57.md`; erratum 1 `01312a77`, before any claim content):
- **C1 — depth** (lowest owned axis; the learning claim; the sourced claim). Surface: a new `SKILL.md` table `### Plugin manifests by client`, entry `corpus/knowledge/plugin-manifests-round57.md`, SOURCES S079–S085 (S086–S088 added in attempt 3). Frontier row *MCP/plugin instruction surfaces*, its plugin half. Predicate (frozen): `python3 -B verifiers/check_plugin_manifests.py --rev <rev> --fetch` exits 0 iff F ≥ 5 and G ≥ 3. **Result: MISS as declared** (`4 of 4; new ground 4`, exit 1).
- **C2 — operability** (info-less fence command extraction): **withdrawn before data** (erratum 1). Four pre-freeze controls met its frozen counter. It is a gate reject, not a claim.

Lowest-axis duty: this round uses the **owned-axes reading** (depth 9 is the lowest owned axis). Under the all-axes reading, freshness 8 and adjacency 8.0 are lowest, and neither claim works them. That reading is the operator's open L0 question (`kotoba | round-55 |`).

Anti-loop: rounds 53–56 worked skill-listing and agent-definition surfaces. Round 57 works plugin manifests and command extraction (`A3CriticAxisFit`: anti-loop holds; depth is defensible).

Work items:
- **Attempt 1** (`KotobaR57`, died 05:25Z). Lane commits re-checked in attempt 3:
  - `ee50d8fa`: plan, frozen counters, base receipts.
  - `01312a77`: erratum 1 and the control receipts.
  - `27af04a7`: v2 re-control receipts.
  - `ac22ca87`: C1 content.
  - `07c33d73`: C1 measured, lesson M58–M64, Q41–Q45.
  - Re-check evidence: `.ufo/waves/round-57/a3/falsify/A3RerunC1Counter.md` (counter sha256 `bf11a4ef…` unchanged since `01312a77`; outputs byte-identical to `C1-measure.txt`), plus `A3NoHarmGates.md` and `A3NoHarmPriorClaims.md`.
- **Attempt 2** (`KotobaR57A2`, died 06:19Z). Nothing it did was cited:
  - Its uncommitted edits to `SKILL.md`, `corpus/SOURCES.md` and the entry are saved as an untrusted attack target: `.ufo/waves/round-57/a3/a2-candidate.patch`, sha256 `2e681cf5…`. The three files were reset to the branch.
  - Its `attempt2/` scratch was moved to `/fast/scratch/hyaku/kotoba-r57a3/attempt2-untrusted/`.
  - Every hunk that later landed was re-derived by an attempt-3 seat.
- **Attempt 1's falsify dispatch records** (33 seats, dead with the orchestrator). I re-validated the spec with `ufo-swarm-wave.mjs plan`: 33 of 33 tasks and the context are byte-identical to `falsify-taskcall-sent.json`. They are committed in `bc09a830` as records only. The seats' outputs stay untrusted and are not cited.
- **Attempt-3 falsify wave**: 40 seats (`.ufo/waves/round-57/a3/falsify/`). It attacked:
  - C1, re-run with the counter and by hand;
  - the seven S079–S085 re-opens;
  - the three candidate rows S086–S088;
  - the seven ship cells;
  - the miss accounting, the target census and the axis fit;
  - the quote notes, the entry's shape and the budget move;
  - R2/R6 and the correction sweep (mutated);
  - the C1 guards (mutated) and the hollow controls (replayed);
  - no-harm on the gates and on the prior claims;
  - calibration, the lesson's Mistakes, the Q44 contexts and the frontier note;
  - the Gate rejects, the misroot sweep, the containment bounds, sibling adjacency and the host plugin inventory.
- **Corrections landed in `bc09a830`**:
  - All seven `What a plugin can ship` cells, corrected per client from live re-fetches. Examples: Claude Code's root single-skill rule and that a plugin-root `CLAUDE.md` is not loaded (`A3ShipClaudeCode`); Codex's `.app.json` and `defaultPrompt` (`A3ShipCodex`); VS Code and Copilot CLI's "in Agent Plugins 1.0" qualifier (`A3ShipVSCode`, `A3ShipCopilotCLI`); Gemini CLI's fallback to a root `GEMINI.md` and its safety checkers (`A3ShipGeminiCLI`); Cursor's `skills` condition, which needs both absences (`A3ShipCursor`); opencode's agent transforms and session prompts (`A3Shipopencode`).
  - The quote-location notes (`A3ReopenS079`–`A3ReopenS085`).
  - The opencode manifest wording (M67).
  - The Limits wording (`A3ReviewEntryShape`).
  - `agent-definition-files-round56.md:91` (`A3ReviewR2R6` F1).
  - Corpus index rows (`verify_corpus_integrity` goes from 4/9 to 5/9; `unindexed` is cleared).
  - SHONEN recount (`A3CriticScorecardCalib`).
  - The lesson's Gate and Mistakes.
- **C1 re-measured** at `bc09a830`: unchanged miss (`.ufo/waves/round-57/a3/C1-remeasure-a3.txt`). It was pre-measured on sandbox `61debdc9` (`/fast/scratch/hyaku/kotoba-r57a3/L1-premeasure`) before landing, with the same output (`a3/L1-premeasure-noharm.txt`).

Round shape: counter-writing call, pre-freeze control call, a v1 build wave, a v1 falsify wave (attempt 1, dead), a residual call (attempt 2, untrusted), and the v1 falsify wave of attempt 3. I held the planner seat. The planning data walk rode the scout and critic items.

| Wave | Seats | Roles | Outcome |
|---|---|---|---|
| w0 (counter-writing) | 2 | executor 2 | returned |
| controls | 11 | critic 9, mutation-tester 2 | returned |
| build | 32 | scribe 14, scout 6, executor 4, critic 3, reviewer 3, mutation-tester 1, connector 1 | returned |
| falsify, attempt 1 | 33 | reviewer 12, critic 9, scout 8, mutation-tester 2, sentinel 1, connector 1 | all dead (orchestrator died 05:25Z); outputs untrusted |
| residual, attempt 2 | 8 | reviewer 6, critic 2 | dead (orchestrator died 06:19Z); 6 reports, untrusted and not cited |
| falsify, attempt 3 | 40 | reviewer 14, critic 13, scout 9, mutation-tester 2, sentinel 1, connector 1 | all 40 returned; none dead |

- **Round total: 126 seats.** The attempt-3 falsify wave was validated under policy v1 and dispatched as one `task` call carrying the validator's `taskCall` unchanged. Gate grant: `granted lane=kotoba wave=kotoba-r57-falsify-a3 seats=40 live=43 cap=128`.
- **Refusals and cancellations:** no refusals and no cancelled seats in attempt 3.
- **Q44:** the bound is verbatim in the attempt-3 falsify context. `jq -r .context … | grep -c 'Kill only by the PIDs you started'` → 1 (`a3/q44-context-grep.txt`). Corrected M63: the build context prints 0.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists the same 15 non-driver untracked files before dispatch (06:45Z) and after (07:11Z). `A3ScoutMisroot` scanned their bytes and found no kotoba, round-57 or KotobaR57* content, so nothing was moved.
- **Cross-lane noise:** seat `ChousaR32A2.CtlC2WeakReaderB` sent a chousa C2 note that reached several kotoba seats. None of them replied. Routed to Main as an observation only.
- **Bounds note:** `A3NoHarmPriorClaims` ran read-only `--rev` counters with the lane as its cwd rather than a sandbox clone. Lane state was unchanged (`git status --porcelain` clean before each commit).

## Landed changes

| commit | what | LOG entry |
|---|---|---|
| `ee50d8fa` | plan, frozen C1/C2 counters, base receipts, bounds | LOG § Round 57 (attempt 1) |
| `01312a77` | erratum 1: C1 counter v2, C2 withdrawn; control receipts | LOG § Round 57 (attempt 1) |
| `27af04a7` | v2 re-control receipts, MutC1Counter, build spec | LOG § Round 57 (attempt 1) |
| `ac22ca87` | C1 content: SKILL.md table, entry, S079–S085, Gate, budget move, R2/R6, Q41–Q44 | LOG § Round 57 (attempt 1) |
| `07c33d73` | C1 measured (miss), M58–M64, Q45, SCORECARD, Frontier note | LOG § Round 57 (attempt 1) |
| `bc09a830` | attempt-3 falsify wave evidence and corrections (cells, notes, S086–S088, index rows, SHONEN, lesson M65–M69); attempt-1 falsify dispatch records | LOG § Round 57 attempt 3 |
| `118d3ac4` | C1 re-measure receipt, census end, LOG, SCORECARD | LOG § Round 57 attempt 3 |

## Before → after measurements

**C1** — `python3 -B verifiers/check_plugin_manifests.py --rev <rev> --fetch`, counter v2. sha256 `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e`, frozen at `01312a77` and untouched since. `--self-test`: 0 failures over 235 assertions.

| revision | output | exit | receipt |
|---|---|---|---|
| `47c05558` (base) | `plugin manifests found on the live page 0 of 0; new ground 0` | 1 | `.ufo/waves/round-57/controls/C1-base-v2.txt` |
| `ac22ca87` (content) | `plugin manifests found on the live page 4 of 4; new ground 4` | 1 | `.ufo/waves/round-57/C1-measure.txt` |
| `07c33d73` | `4 of 4; new ground 4` | 1 | `a3/falsify/A3RerunC1Counter.md` |
| `bc09a830` (after corrections) | `4 of 4; new ground 4` | 1 | `.ufo/waves/round-57/a3/C1-remeasure-a3.txt` |

- **Verdict:** the target is F ≥ 5, so the claim is a **miss**. Counted: Claude Code, Codex, Gemini CLI, Cursor. Rejected: VS Code and Copilot CLI (shared bare `plugin.json`) and opencode (folder token).
- **Mutation check:** no counter mutant turns the miss into a pass without its self-test failing. `A3MutC1Guards` tried five guard mutants, all killed; the trailing-slash mutant alone gives `5 of 5`, and the self-test fails it.
- **Hand count:** a reader accepts 6 of 7 rows as source-backed (`A3RerunC1ByHand`). Under a different client-neutral row rule, VS Code's Legacy OpenPlugin `.plugin/plugin.json` could make F = 5 [INFERENCE, not run] (`A3CriticMissHonesty`). That rule was not frozen, and no row was changed after measurement.

**C2** — withdrawn before data, so there is no after-value. The base is `info-less fence cases correct 48 of 120`, exit 1 (`controls/C2-base.txt`). The controls met the v1 predicate at 120 of 120 (Gate).

## Sources & frontier

- **SOURCES rows: 78 → 88** (`grep -c '^| S[0-9]' corpus/SOURCES.md` at `47c05558` vs `118d3ac4`). All ten were added as tier A, `docs`, `mined`, opened 2026-10-23:
  - S079–S085 by the attempt-1 build seats; all seven were re-opened byte-identical by `A3ReopenS079`–`A3ReopenS085` at 06:45Z.
  - S086 (Codex scaffold contents; correction row for S080) by `A3CandS086` at 06:47:23Z, 38,036 B, sha256 `c37e330d…`.
  - S087 (opencode discovery page; correction row for S085's anchor) by `A3CandS087` at 06:46:53Z, 4,371 B, sha256 `39afa299…`.
  - S088 (Cursor plugins reference) by `A3CandS088` at 06:46:23Z, 30,324 B, sha256 `3bbf36f3…`.
  - URL, access time and a quote of at most 25 words for each new row are in `corpus/lessons/round-57.md` § Gate.
- **Rows touched (old → new):** none in place. S080 and S085 stay `mined` → `mined`, with recheck and used-by unchanged. S028 is now cited by the entry for Copilot CLI component fields only.
- **Census:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`.
  - Start: `.ufo/waves/round-57/census-start.txt`, `kotoba ok`, exit 0, 7 W04.
  - End: `.ufo/waves/round-57/census-end.txt`, 07:10:35Z, `kotoba ok`, exit 0, 8 W04. The new W04 is S086, which shares S080's URL as its correction row.
- **Sourced claim:** C1 rests on S079–S085 (plus S086–S088 for the corrected cells).
- **Frontier:** *MCP/plugin instruction surfaces*, plugin half, is recorded and not held (`corpus/README.md` round-57 note; `A3ReviewFrontierNote` HOLDS).
- **Mined mistakes:**
  - M58–M64 (attempt 1).
  - Corrections to M62 (the population is 4 only under the chosen row rule), M63 (the build context lacks the bound) and M64 (clarified).
  - New: M65 (the quote notes repeated the defect routed by Q42), M66 (a dead attempt's scratch carried provenance), M67 (a negative overstated against its own source), M68 (correction-sweep arms are weak: 7 of 11 mutants survive), M69 (an item premise was false).
  - Q45 is now shown able to fail: a record check over `plans/round-57.md` prints `Q45 FAIL …`, exit 1 (`A3CriticTargetCensus` § 2).

## Gate

Real rejects with reasons (`corpus/lessons/round-57.md` § Gate, Rejected):
1. **C2 claim:** four hollow controls met the frozen predicate (120 of 120) before data, so it was withdrawn.
2. **C1 counter v1 as the rule:** bare words, nav text, a changelog line and case variants met it, so it was replaced by v2 before content.
3. **VS Code `.plugin/plugin.json` as the row token:** it would pass the counter while naming a legacy third-party format instead of the default.
4. **opencode `package.json` as the token:** it is the npm package manifest, not a plugin-specific one, and it fails the grammar.
5. **GFM spec row** for C2.
6. **Copilot CLI legacy paths:** citing them would re-cite base row S028.
7. **Q42 quote swaps for S080/S083** (attempt 3): the quotes are counted, so swapping them after measurement re-scores the claim; and the proposed lines do not state the manifest location.
8. **The attempt-2 candidate as landed text:** wrong "two sentences" note, uncitable provenance, `or` for a conjunction, overbroad "only manifest", and a shaped quote in quote marks.
9. **Band-10 relabel:** a score ruling that belongs to the closure.
10. **A new correction-sweep registry row** while the sweep's arms are weak (M68).

`A3ReviewGateRejects` re-opened rejects 1–6 and agrees with all six.

## Trend verdicts

- **expansion: improved.**
  - New frontier ground: plugin manifests and what a plugin can ship, for seven clients.
  - SOURCES 78 → 88, and one new knowledge entry indexed.
  - The claim that carried it missed its frozen target, so the depth score holds at 9.
- **quality: improved.**
  - The 40-seat falsify wave corrected all seven ship cells and the quote notes against live bytes, with every sha256 identical.
  - It withdrew an overstated negative (M67).
  - Corpus integrity went from 4/9 to 5/9 (unindexed cleared).
  - Four calibration mismatches were corrected and one was routed.
  - No-harm held:
    - checklist FAIL set identical and line budget 598/600;
    - gate registry 30/30;
    - correction sweep 0 stale;
    - sources append-only 0 protected-cell changes;
    - the prior-round counters byte-identical at base and tip (`A3NoHarmGates`, `A3NoHarmPriorClaims`, `a3/L1-premeasure-noharm.txt`).
- **discernment: improved.**
  - Ten real gate rejects; the outside re-check agreed 6 of 6.
  - The untrusted candidate was attacked hunk by hunk rather than adopted.
  - M62's over-claim ("honest count is 4") was corrected instead of defended.

Admission note (status-neutral; the operator rules): C1 is a measured **miss**, so under "every claim verifies" this round's claim does not verify. No axis was harmed: every SCORECARD score is unchanged.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `SKILL.md` § Plugin manifests by client (S079–S088), re-opened by `A3ReopenS079`–`S085` and `A3CandS086`–`S088`; inventory recount in `SHONEN.md:6`
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `corpus/knowledge/cold-run-round11.md` (unchanged this round)
- [~] Instructions executable by an agent without oral context — evidence: `corpus/lessons/round-8-aggregator-box3-coldrun.md` (unchanged)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `.ufo/waves/round-57/a3/falsify/A3ConnSiblingPlugins.md` (no contradiction with sibling lanes); `A3ReviewFrontierNote` (PROVINCE.md needs no round-57 line)

## Open L0 questions, routed items, installs

- **L0:** none new. Still open: `kotoba | round-55 |`, the owned-axes vs all-axes lowest-axis reading. This round uses the owned-axes reading.
- **Routed to round 58:**
  - The correction-sweep arms (M68).
  - The C1 v2 self-test never exercises a successful `main()` path (`A3CriticScorecardCalib` M05).
  - Band-10 attribution at `SCORECARD.md:29` (closure).
  - Dead lowercase `/home/vgpnk/projects/` paths at `SKILL.md:514-515` (`A3ReviewR2R6` F3).
  - The Q45 census record in the round-58 plan (`A3CriticTargetCensus` § 2).
  - R8 (carried).
- **Installs:** none, by the L1 or any attempt-3 seat. Pacman was not used.
