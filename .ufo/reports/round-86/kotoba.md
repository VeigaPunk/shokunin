# kotoba — round 86

- **Lane:** kotoba (`kotoba-shokunin`), axes depth + consistency (calibration sub-axis). Host: Linux, `omp/18.15.0`.
- **Round:** 86, attempt 1. A `launch kotoba round=86 … attempt=1` line is in the watchdog log, and there is no `lane-dead-no-report` line for round 86. Nothing was inherited.
- **Round base:** `e5d966b51494f4177868ad5f46806a204783ef6c`. **Lane tip at report:** `4212b6930fa2a424b2c794ab9724384c4f93b7b4` (`master`).
  - `git ls-remote origin refs/heads/master` prints the same hash.
  - `jj-lane.sh state` reads `ahead=0 behind=0 tracked=0 untracked=0`.
- **Round shape:** ONE v1 wave, `r86-w1`, with 13 seats. There was no residual call. Round total: 13 wave seats plus 1 out-of-wave seat (see Extras).
  - WAVE-DONE was received from `Main`. The marker and its provenance are in `.ufo/waves/round-86/r86-w1-wavedone.txt`.
  - Seat-role mix: scout 2, executor 1, scribe 3, connector 1, reviewer 2, critic 1, mutation-tester 1, sentinel 1, revenger 1.
  - Strict attack share (reviewer, critic, mutation-tester) is 4/13 = 30.8 %. There is 1 connector seat.
  - Dead seats: 0. All 13 seat reports exist under `.ufo/waves/round-86/w1/`.
  - `r86-w1-results.json` carries `output: null` for every seat (orchestrator telemetry). This is disclosed in the marker file.
- **Planner seat:** held by the L1, because the validator rejects `planner`. The planning data-walk rode ScoutRootsSource, ScoutRootsHost and Connector.

## Work performed

**Declared claim (one):** **C1 — freshness** (lowest non-retired axis, tied with adjacency at 8). The lane's executable model of how omp builds the `<skills>` catalogue was re-derived against omp 18.15.0 and scored by reproducing a real catalogue line for line. The claim is sourced on **S255**, opened this round.

- **Drift measured before any work.** The newest real omp catalogue on this host has 215 lines (session `KakeR90.jsonl` line 7, rendered 2026-11-04T21:55:22.890Z). The lane model reproduced **83 of 215**.
  - Every modelled line was right.
  - The 132 misses are `not-discovered`: the model's four 2026-09-28 roots never included omp's plugin root.
  - Evidence: `.ufo/waves/round-86/receipts/c1-K0-base.txt`.
- **Freeze committed before any candidate data.** Commit `ecfad51` holds the plan `plans/round-86.md`, a new counter `verifiers/check_omp_catalogue_repro.py`, the fixture `verifiers/fixtures/omp-catalogue-r86/catalogue.json` (sha256 `0b3443e1…`), and controls K0–K2 with a self-test.
  - The model runs under bwrap, and guards G1–G4 run in the parent process.
- **Addendum 1, committed before any candidate was scored** (`b9ee548`, `plans/round-86-addendum-1.md`). ExecModel was put on hold and had scored nothing.
  - **What falsified the frozen counter:**
    - Critic-2 F1: a `*` ledger row plus a `.zcode` root omp never reads gave `215 of 215`, exit 0.
    - Sentinel-3 F2: the request dumps in `~/.omp/logs` carry the renders and were readable inside the sandbox.
    - ReviewerCounter-2 F3: an encoded answer key, one path offered for every name, and a network fetch of the fixture.
  - **What the addendum changed:**
    - G4 now requires a dot-directory segment in each pattern, and the quote must contain it.
    - The sandbox now hides all of `~/.omp` and binds back only plugin `node_modules` and `agent/skills`. It also unshares net, pid and ipc, and clears the environment.
    - The parent now re-derives each render. It checks that the directory name equals the skill name, that the description occurs in the file, and that the module's key and preview equal reference ports of omp's `A`/`dnt`.
  - **Re-run controls:** self-test `0 failure(s) over 46 assertions`. K0 = 83 / exit 1. K1 and K2 = exit 1. K3/K3b (F1's world) = G4 FAIL / exit 1. K4 sandbox probe: logs, sessions and cache are absent, the network is blocked, and home is not writable.
  - Evidence: `.ufo/waves/round-86/receipts/*-a1.txt`.
- **Candidate (ExecModel)** is in `verifiers/verify_harness_claims.py`:
  - Roots are re-derived per provider: native, agents, omp-plugins and managed. The claude/codex/opencode user roots are opt-in and off on this host.
  - `omp_plugin_skill_roots()` reads `~/.omp/plugins` from `package.json`, the lock file and the manifest.
  - `preview` is fixed to omp's `o >= E` last-space rule. This was a real lane bug, found while porting the reference; no fixture line exercises it.
  - The new ledger `verifiers/omp-skill-roots.tsv` has 12 rows. Every quote is located in the ELF.
  - Self-test: 34 assertions, exit 0. Report: `.ufo/waves/round-86/w1/ExecModel.md`.
- **Independent root review (non-author seat ReviewerRoots):** 9 of 12 rows are `sound`. Rows 1, 8 and 9 have the right roots but quotes that are located and irrelevant. Row 9, the plugin root, carries 132 names and cannot pass the amended G4 with a code quote. Final line: `C1 roots: sound` (`w1/ReviewerRoots/review.md`).
- **Post-data attacks on the amended counter.** These are reported and not patched, because the counter cannot change after data.
  - Critic-2 F5: 39 brute host roots cited with junk dot-spelling ELF strings score 212–215, exit 0 (`w1/Critic/worlds.md`).
  - MutTester-2 and Sentinel-3 F6: G4 matches the unnormalised path. A `..` path laundered through `~/.omp/*` or through the candidate's own `node_modules/*` row scores 215, exit 0 (`w1/MutTester/MutTester-2/g4-dotdot-bypass.txt`, `w1/Sentinel/receipts/g4-launder-world.txt`).
  - Sentinel S4: `/run/docker.sock` is still reachable from inside the sandbox (`w1/Sentinel/audit.md`).
  - MutTester: 15 of 26 counter mutants survive the self-test, on sandbox flags, the G3 total and the rebind list (`w1/MutTester/r85-seat-batteryA.md`).
  - The candidate uses none of these doors. Its 215 lines resolve to `~/.agents/skills` (83) and `~/.omp/plugins/node_modules/ecc-pi-core/skills` (132).
- **Precedence probe (RevengerPrecedence):** omp ranks by provider priority. A later copy with a different body is kept, renamed as `<ns>/<name>`, not dropped. The fixture has 0 cross-root name collisions, so the rule is not exercised (`w1/RevengerPrecedence/probe.md`).
- **Knowledge, registry, quality and lesson:**
  - New entry `corpus/knowledge/omp-catalogue-model-round86.md` (S255).
  - S255 row added to `corpus/SOURCES.md`.
  - Q77 added to `corpus/QUALITY.md:96`.
  - Lesson `corpus/lessons/round-86.md`, which includes mistake M86-1.
  - SKILL.md registry row (line 522) and a round-86 note on the render (line 578).
  - Corpus baseline re-recorded.

## Landed changes

| commit (`jj-lane.sh` `landed`) | what | LOG.md |
|---|---|---|
| `ecfad51fe3f24540a6d67d2b54920929c7b83041` | freeze: plan, counter, fixture, controls K0–K2, SKILL.md registry row | `LOG.md` § Round 86 C1 claim (`:3239`) |
| `b9ee5484a139c4428a2d53e572868abe86844821` | addendum 1, before any candidate data: G4 dot rule, sandbox allowlist and namespaces, parent-side reference; controls re-run | same entry (`:3255-3262`) |
| `04647b0f715ff3c4f314b0d8f03dea28bc453688` | C1 landing: model, roots ledger, S255 entry and row, README index rows, Q77, lesson, LOG, r85 corrections | `:3239-3296` (claim, S255 intake, M86-1, routed defects) |
| `99c217423bc0feff33ca46a99ddc98bd6bda09c1` | wave integration (13 seat reports, WAVE-DONE marker), after-values, SCORECARD § Round 86, corpus baseline re-record + D3 note | `:3262`, `:3275` |
| `4212b6930fa2a424b2c794ab9724384c4f93b7b4` | gate-registry pinned-values cell fixed; tip re-measure receipt | — (registry fix; receipt `.ufo/waves/round-86/receipts/tip-remeasure.txt`) |

## Before → after measurements

**C1 (freshness).** Counting command: `python3 -B verifiers/check_omp_catalogue_repro.py --rev <rev>`. This is the amended counter: sha256 `39a014f2f3142096b43031faedb0ea9819995fb2926138c3ebf2b194002e4520`, committed at `b9ee548` before any candidate scored.

| rev | reading | receipt |
|---|---|---|
| base `e5d966b5…` | `omp catalogue lines reproduced 83 of 215`; G4 FAIL (no ledger); exit 1 | `.ufo/waves/round-86/receipts/c1-K0-base-a1.txt` |
| landing `04647b0f…` | `215 of 215`; G1–G4 PASS; exit 0 | `.ufo/waves/round-86/receipts/c1-after.txt` |
| tip `99c21742…` | `215 of 215`; exit 0 | `.ufo/waves/round-86/receipts/tip-remeasure.txt` |
| tip `4212b693…` | `215 of 215`; registry `67 of 67` | re-run at report time; the command above with `--rev 4212b69…` |

- **Target was N ≥ 205 with G1–G4 PASS. It is met by the number.**
- **Honest bound (Q71/Q74, measured after data):** worlds that read no omp source also reach the target on this counter (F5 and F6). By the lane's own Q74, the number alone is not this claim's evidence.
  - The semantic half, that these are the roots omp reads, rests on the non-author review `C1 roots: sound` and on the closure.
  - The closure should also rule on the kill-rule clause "counter … changed after this freeze". Addendum 1 changed the counter after the freeze but before any candidate data, following the round-74 addendum precedent.
- **No-harm** (`.ufo/waves/round-86/receipts/noharm-after.txt`, `tip-remeasure.txt`):

| check | result |
|---|---|
| gate registry | 66/66 at base → 67/67 at `4212b69` (it read 66/67 at `99c2174` until the pinned-values cell fix) |
| `verify_harness_claims.py --self-test` | exit 0 |
| `verify_surfaces.py` | exit 0 |
| `check_substrate_pins.py` | `OK 3/3` |
| sources census | exit 0 |
| `check_sibling_census.py` | 20/20, 10/10 |
| corpus integrity | 8/9; the one red is the carried `commit_unresolvable 1` at `corpus/lessons/round-81.md:8` |
| `verify_skill_checklist.py` | `governance.citation_resolves` red, carried from base |

## Sources & frontier

- **Census, round start:** `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0, 33 `W04` (`.ufo/waves/round-86/receipts/census-round-start.txt`).
- **Census, round end:** the same command → exit 0, 33 `W04`, 0 `E` rows, last line `kotoba ok …/corpus/SOURCES.md` (`.ufo/waves/round-86/receipts/census-round-end.txt`).
- **Rows:** `grep -cE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md` → 180 before, **181** after.
  - **Added by tier:** A 1 — **S255**: omp 18.15.0 TypeScript embedded in the installed ELF, plus upstream `github.com/can1357/oh-my-pi` tag `v18.15.0` (HTTP 200). Kind `code`, `mined`, opened 2026-11-04, recheck `on-release`.
  - The located quote (≤ 25 words) is at ELF offset 178770368: `const c = o >= E ? r.slice(0, o).trimEnd() : r;` (`w1/ScribeSources/fetch-record.txt`).
  - B 0, C 0. Rows touched: 0.
- **Frontier advanced: 1.** The *Loader-rule freshness* row now has a round-86 append-only note (`corpus/README.md:263` at `4212b69`) moving the catalogue leg.
- **Sourced claim:** C1's entry `corpus/knowledge/omp-catalogue-model-round86.md` cites S255.
- **Mined mistake M86-1:** `corpus/lessons/round-86.md` § Mistakes.
  - The catalogue check matched lines only against the cache, so 132 unmodelled lines read as a DRIFT count for about 30 rounds.
  - Captured-by: none. Fix: Q77, which is shown able to fail (the base fails it at 83 of 215).
- **Assimilation:** none this round. Connector names the next candidate: staged `skill-paths-and-precedence.md` plus an omp precedence row for `skill-name-precedence-round69.md` (`w1/Connector/overlap.md`).
- **considerthese:** proposals 1–2 of `2026-10-26.md` remain untouched. The registry move is still blocked on L0 `round-73`.

## Trend verdicts

- **expansion — `improved`.**
  - One tier-A row was added (S255), and one frontier row was advanced (README `:263`).
  - The model now governs a root class it never held: omp plugins, 132 of the 215 catalogue lines.
  - Counts are from the commands above.
- **quality — `improved`.**
  - The freshness re-derivation moved reproduction from 83 to 215 of 215.
  - A real `preview` deviation from omp's `o >= E` rule was fixed.
  - This rests on the non-author root review for meaning, since the counter's G4 is form-only (F5, F6).
- **discernment — `improved`.**
  - Attack seats falsified the lane's own frozen counter three times before data. The lane amended it before any candidate scored, with an addendum, re-run controls and a hold.
  - Two further doors found after data (F5, F6) are reported as bounds on the claim, not patched. Under Q74 the number alone is not offered as admission evidence.
  - r85 D1–D7 have dispositions (below).

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists and cited sources — `SHONEN.md:5-6`. The gate registry is `67 of 67` at `4212b69` (`python3 -B verifiers/check_gate_registry.py --rev 4212b6930fa2a424b2c794ab9724384c4f93b7b4`).
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — this round's C1 reproduces a real omp catalogue from the installed client's inputs (`LOG.md:3239-3262`, `.ufo/waves/round-86/receipts/c1-after.txt`).
- `[~]` Instructions executable by an agent without oral context — the recorded gap remains (`corpus/lessons/round-8-aggregator-box3-coldrun.md:36-37`). There has been no fresh non-author cold run.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` is untouched; `check_sibling_census.py … --province PROVINCE.md` reads 20/20. Connector's no-absorb line (the `~/.omp/agent` inventory and the `.agents/skills` symlink provenance belong to kumitate) is honoured.

## Extras

- **r85 routed defects:**
  - D1, D4, D5: append-only `## Correction, round 86` block in `corpus/lessons/round-85.md`.
  - D2: tip receipts committed (`receipts/tip-remeasure.txt`).
  - D3: additive `round86_rerecord` note in `verifiers/corpus-baseline.json`.
  - D6: K4 re-captured in full (`receipts/r85-D6-K4-recapture.txt`).
  - D7: WAVE-DONE marker committed (`r86-w1-wavedone.txt`).
- **Routed to round 87:**
  - G4 should normalise and resolve roots before matching, forbid `..`, and require per-root code quotes.
  - Hide `/run/docker.sock` and the system D-Bus socket.
  - Add self-test arms for the sandbox flags, the G3 total and the rebind list.
  - Bind `~/.omp/plugins/{package.json,omp-plugins.lock.json}` so the model's registry branch, not its fallback, is what gets scored.
- **Out-of-wave seat:** an L1 message addressed to `MutTester` revived the parked round-85 seat of that name. It wrote only `w1/MutTester/r85-seat-batteryA.md`, which is used as evidence above and is not counted in the 13. The wave's own seat ran as `MutTester-2`.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open. Round 87 has not been started.
- **Tool installs:** none, by the L1 or any seat on record. pacman stayed paused.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no kotoba-r86 file at the fleet root. The untracked `after` (2026-11-03) and the modified `.ufo/l0-questions.md` belong to other actors.
- **L0:** no new line. Open kotoba items are unchanged (`round-73`, `round-82`).
- **Scratch:** `/fast/scratch/hyaku/kotoba-r86` was removed, along with the K1 forge directory.
