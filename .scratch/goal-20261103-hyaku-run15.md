# hyaku run 15 — 2026-11-03 (Linux/omp host; continues zcode run 14)

Operator directive (verbatim): "ok i need you to continue the hyaku run, we will be using 32-40
concurrent workers, you are the orchestrator of each run; i want you to do 10 rounds of training per
shokunin, until each reeach 100 completed rounds. our subagents for the swarms rounds (each round, a
wave composed of m_flash, m_mim, m_zfl on roles you assign) on the hyaku style but using these models
and conc i've assigned; remember, the essence of the shokunin runs is to learn by doing, to activelky
get better and more capable, to have curated source of knowledge (corpus and their own trials)".
Interjection: "you will be running until each shokunin reaches round 100".

## Campaign shape

- **Goal: every pool lane reaches round 100** (17 lanes, 706 lane-rounds remaining at start).
  10-round blocks per lane; a lane holds its slot for its whole block, then the slot goes to the
  lowest-`next/` lane (`inline.sh queue` order) — the long-pole lanes (kagi r29, tabi r44, souji r46)
  stay live continuously.
- **Concurrency 32–40 workers total**: ~6 L1 lanes live at once; dispatcher `SEAT_CEILING=36`
  (seat spawns stop at 36 running jobs); L1/closure spawns only while running jobs < 40; closures
  may use ≤3 helper seats.
- **Round size: ONE v1 wave of 8–16 seats** (`ufo-wave-policy.json` band 8–16; residual ≤4;
  ≥25 % attack seats; ≤2 connector seats).
- Hyaku in-session inline mode unchanged (inline.sh + inline-dispatcher.py, jj lanes, fleet-commit.sh,
  fresh non-author closures, append-closure.py the only MANIFEST writer).

## Routing (never pass `model`; backup `~/.omp/agent/config.yml.pre-run14-20261103`)

| roles | model |
|---|---|
| task (L1 + closure judges), main, planner, reviewer, security-reviewer, critic | @m_zfl |
| executor, revenger, scout, labrat, mutation-tester, simplifier | @m_flash |
| connector, sentinel, scribe, sonic, distiller, seance | @m_mim |

## Start-state reconciliation

The zcode run-14 campaign (`.scratch/goal-20261031-hyaku-zcode-run14.md`, Windows host, 2026-10-31 to
2026-11-02) advanced every pool lane while this host sat on run-13 state. Reconciled 2026-11-03:
- Fleet repo: local run-15 setup commit rebased onto origin tip b73780ab; stale local commit
  "round-60: hyaku closure dispatch for tameshi" (tameshi r60 was already closed remotely) abandoned.
- Lane repos: all 17 fast-forwarded to their remote tips (all were ahead=0, behind 6-98). Dead run-13
  working-copy residue (tracked diffs + untracked strays) preserved under /tmp/run13-orphans/<lane>/.
- Local hyaku state rebuilt from MANIFEST closure rows: next = closed_max+1, outcome files per closed
  round; run-13 claims moved aside. kake r68 landed unclosed on zcode (report 9d56e80b) → claim
  reconstructed (base = r67 closure lane tip a6cb7efa), closed first.
- chousa r70-72 rejected on the Windows host (no flock, sibling load): streak lifted at run start,
  fresh-start rule applies to chousa r73.
- 574 lane-rounds remain at start: revenger 89, tsukuroi 64, kama 70, tameshi 72, tabi 56, mado 65,
  mori 79, souji 52, kaidoku 64, kake 68, kagi 30, kasegi 57, chousa 73, kengaku 63, kumitate 74,
  kotoba 85, kotodama 82 (next round per lane). Critical path: kagi (71 sequential rounds).

## Progress

State file: `.scratch/run15-state.json` (rounds trained this run, per-lane block progress).

## Orchestrator resume (after compaction or kernel loss)

Kernel helpers live in `.scratch/run15-kernel.py` (step / run_for / launch / close / fill_slots).
Kernel lost → `%load scripts/hyaku/inline-dispatcher.py` then `%load .scratch/run15-kernel.py`
(separate cells), `await bootstrap()`, then loop `await run_for(1500)` (cell timeout 1700).
Each L1 end → verify → closure; each closure end → advance → relaunch same lane until its
10-round block ends or it reaches 101, then the slot goes to the queue head. MAX_LIVE_LANES=6.
Seat results auto-deliver into the orchestrator transcript; they need no action.

## Resume checkpoint — 2026-11-04

This checkpoint supersedes the initial concurrency/routing/resume values above, not the
round contract. Kernel state was retained; setup was not reloaded.

- `step()` observed 136 trained closures: 109 admitted, 27 rejected. This is a
  run-15 counter, not the fleet-wide historical total printed by `status.sh`.
- Active limits: `SEAT_CEILING=60`, `MAX_LIVE_LANES=9`, total target 32–64 workers;
  one 8–16-seat v1 wave per round, 10-round blocks, every pool lane through round 100.
- zai seats exhausted their five-hour quota (429/type=1308; reset text
  `2026-11-04 21:14:48`) and Kimi fallback denied subscription access (403).
  All 18 role overrides now use `@m_flash` (`devin/swe-2:max`); five changed
  roles (reviewer, critic, executor, mutation-tester, sentinel) each completed an
  actual `printf 'RUN15_ROUTE_OK <role>\n'` smoke with exit 0. Backup:
  `~/.omp/agent/config.yml.pre-run15-zai-quota-20261104`.
- Interrupted ticks could consume an in-memory L1/closure event before persistent
  `live` state advanced. `step()` now restores watch entries from persistent
  state before ticking. Isolated smoke: before, three terminated claims emitted
  no events; after, two L1 ends and one closure end were handled exactly once,
  while a still-running L1 stayed live.
- Actual recovery: `verify` accepted the already-landed kagi r32 and kasegi r59
  reports, then spawned fresh `CloseKagiR32` and `CloseKasegiR59` judges. No round
  was re-run, no verdict was assumed, and no lane work was deleted.
- Four lanes remain quality-paused after three rejected closures: souji next 58,
  tabi next 62, chousa next 74, tsukuroi next 77. Their block evidence is preserved;
  resuming them requires operator authorization for the fresh-start procedure
  (read the last three rejected closures/spot-checks; new claims must defeat the
  do-nothing control). Other pool lanes continue normally.

## Operator ruling — 2026-11-04 (quality-pause lift)

Operator, verbatim: "Resume all four". This lifts only the current three-rejection pause on the
four quality-paused lanes — souji (next r58), tabi (next r62), chousa (next r74), tsukuroi
(next r77) — and nothing else.

- **History is preserved.** Every failed/rejected closure and its spot-check stays on the record;
  nothing is retroactively admitted. The 3-rejection pause gate applies unchanged to their new rounds.
- **Fresh start is required.** Before a resumed round files claims, the orchestrator reads the
  lane's last three rejected closures and their spot-checks; new claims are re-measured on this
  host and must beat a do-nothing control — a claim that would pass unchanged with no work is not
  a claim.
- **No campaign/run change.** Round counters continue; concurrency, 10-round blocks, the 8–16-seat
  wave band and the all-`@m_flash` routing stay as committed (failover `180fc2b`, interrupted-watch
  recovery `0d82ccc`). The parent archives the four runtime pause markers and shows the `inline.sh`
  queue before dispatching; this ruling lands no runtime, claims, MANIFEST or lane writes.

## Availability recovery checkpoint — 2026-11-04

- User reports `m_zfl` usage reset; accepted as ground truth. Devin subsequently returned
  `permission_denied: This model is no longer available for your account`.
- All 18 role overrides now use `@m_zfl`; aliases and fallback chains unchanged, `m_mim`
  remains off every role. Backup:
  `~/.omp/agent/config.yml.pre-run15-devin-unavailable-20261104.Qfa62SXH.bak`.
  Operational addendum committed/pushed as `0ad04e305ddcad137802299fe6c17bf3d7669045`.
- Actual recovery proof: previously provider-failed `CloseKakeR84` completed, appended its
  rejection, and advanced to KakeR85; KamaR83, MoriR88 and MadoR83 also closed rejected.
- `run_for(1200)` observed 154 trained closures: 121 admitted, 33 rejected. SoujiR58
  started under the authorized fresh-start rule; tabi, chousa and tsukuroi await slots.
- Empty seat outputs are not successes. Exact retained JSONL error evidence supplied to
  TameshiR83, KasegiR61 and KaidokuR81; expired proc records mean final status unavailable.
  T83W1R1's recorded `cyber_policy` refusal is not retried, rephrased or rerouted.

## Renewed current-pause ruling — 2026-11-04

Operator choice, verbatim: **"Resume all four once"**. This new authorization covers
only the current four pauses: **kagi next35, souji next59, tabi next63, chousa next75**.
The existing first authorization ("Resume all four": souji58/tabi62/chousa74/tsukuroi77)
does not cover future pauses; this new one covers the current four only. Rejection
history and the future three-rejection gate stay binding, including immediate
re-pause after one rejection if the historical last-three window still warrants it.
This appendix records authority/prerequisites, not an executed runtime resume.

### Exact reads and retained rejection evidence

Full reviewed-work hashes, committed spotcheck hashes, concrete root failures and
per-lane prerequisites are in `scripts/hyaku/lane-addendum.md`,
**Run15 renewed current-pause authorization — 2026-11-04**. Read before declaration:

| Resumed round | Zero-based MANIFEST.json rounds indices | Required local spotcheck paths (each pinned full hash in addendum table) | Binding root-failure lesson |
|---|---|---|---|
| kagi35 | 1208, 1217, 1225 | `kagi-shokunin/corpus/lessons/round-32-verifier-spotcheck.md`, `round-33-verifier-spotcheck.md`, `round-34-verifier-spotcheck.md` in same directory | Residual non-owned SD6; invented captures BASE101/target111; C1/C3 population coupling 88/14/88 versus frozen87/13/87. Independently measure/separate populations; reject empty/SETUP false-zero. |
| souji59 | 1099, 1105, 1230 | `souji-shokunin/corpus/lessons/round-56-verifier-spotcheck.md`, `round-57-verifier-spotcheck.md`, `round-58-verifier-spotcheck.md` in same directory | B4/C4 hidden filings; second-opener/over-hide harms; receipt confinement/tag/rc-test debt; C2 control committed after freeze. Late C1 replay cannot bind original headerless evidence. |
| tabi63 | 1094, 1100, 1236 | `tabi-shokunin/corpus/lessons/round-60-verifier-spotcheck.md`, `round-61-verifier-spotcheck.md`, `round-62-verifier-spotcheck.md` in same directory | K7 v19 red; K4 malformed frozen header; post-scoring interface change; exact M5 AND→OR survives16/16 plus duplicate/fabricated-label falsegreens. Freeze readable inputs/final bytes and source-specific polarity negatives. |
| chousa75 | 1036, 1133, 1234 | `chousa-shokunin/corpus/lessons/round-72-verifier-spotcheck.md`, `round-73-verifier-spotcheck.md`, `round-74-verifier-spotcheck.md` in same directory | Incomplete battery; numstat additions/deletions inversion bypassed by helper test; missing QUALITY126 prefreeze forgers and surviving order oracle9/9. Actual load() append/deletion controls and source-discriminating forgery kills required; repeated r73 Linux completion is no gain. |

**Before declaration/predicate freeze and candidate scoring, actually execute and
commit failing-before no-work and forgery controls**, with independent expectations,
observed rc/finding IDs, commands, input revisions and instrument hashes. Exercise
the public/production path with genuine positive controls, not just helpers. Late
control binding, a to-be-built oracle, digest identity or later replay cannot satisfy
the earlier prerequisite. Prior falsegreens/procedural misses must not be backdated,
re-scored or retroactively admitted; frozen evidence and rejected history stay intact.

No pausemarker, state, MANIFEST, lane file, historical row, route, alias, concurrency,
wave size or quality threshold is changed here. Existing safety/refusal boundaries,
credential shape-only treatment and unanswered operator questions remain binding.
Source pointers above were checked by file/ledger reads only; no validation, test,
gate, build, lint, formatter, provider probe or commit was run for this appendix.

## Routing split — 2026-11-04 (operator; no role on @m_zfl; supersedes the all-@m_zfl and m_mim-off notes for future launches)

Operator, verbatim (first ruling): "use m_mim and m_flash on most m_zfl"

Operator, verbatim (second ruling): "assign more m_flash and m_mim to roles"

Operator, verbatim (third ruling): "also m_antigravity as connector"

Final map (`task.agentModelOverrides`, 18 roles; backup `config.yml.pre-run15-most-off-zfl-20261104T153242`):

- `@m_flash` (devin/swe-2:max), 10: task, main, planner, reviewer, security-reviewer, executor, revenger, labrat, mutation-tester, sentinel.
- `@m_mim` (minimax-code/MiniMax-M3.1-Flash:high), 7: critic, scout, simplifier, scribe, sonic, distiller, seance.
- `@m_antigravity` (google-antigravity/gemini-3.8-flash:high), 1: connector.
- `@m_zfl`: no role.

Future launches only; no live restarts; live seats keep their captured route. No safety-refusal retries or rerouting. Aliases, fallback chains, concurrency and wave sizing unchanged. Known risk: devin/swe-2:max (m_flash) returned permission_denied on 2026-11-04; disclosed, not probed. Historical entries are not rewritten.

## Restart checkpoint - 2026-11-04 (operator session restart)
- Campaign 191 closed this run (136 admitted / 55 rejected); fleet 764 rounds done. Drain flag `.scratch/run15-drain` is SET: no new rounds launch until it is removed.
- In flight (state `live`): chousa r76, kengaku r85, tsukuroi r80 at closure (L1 reports landed; closure judges may die with the session -> `step()` relaunches a closure when `closed` returns 0 rows); kotoba r85, mado r85, kotodama r88, kumitate r86, kasegi r66, kaidoku r85 at L1. L1s killed by the restart: `step()` runs verify -> fail; RETRYABLE relaunches the same round (claims and freeze commits survive).
- Paused by the three-rejection gate (need operator fresh-start authorization): kama r86, tameshi r86, tabi r64, souji r60, kagi r36.
- Resume: `%load scripts/hyaku/inline-dispatcher.py` and `%load .scratch/run15-kernel.py` (separate cells), `await bootstrap()`, `rm .scratch/run15-drain`, then loop `await run_for(900)`.
- Routing (config.yml): m_flash opencode-go -> commandcode -> amr -> devin deepseek-v4.1-flash (devin re-auth confirmed by RouteSmokeCritic4); m_zfl zai glm-5.3-flashx primary with glm-5.3-flash elsewhere; model-keyed fallbackChains apply whatever the agent role.

## Wrap-up 2026-11-04 ~22:50 -03:00 (operator: "wrap up this run, i'll restart omp so it picks up my new credentials")

- Campaign totals this run: trained=229 admitted=149 rejected=80. Nothing live; kernel loop stopped.
- **Drain flag `.scratch/run15-drain` is SET.** Remove it to resume launching.
- Why it stopped: devin weekly quota exhausted (`failed_precondition`), on top of commandcode 401, amr 402 (resets 2026-11-06T22:28Z) and opencode-go 402. Every L1/closure died; 11 lanes hit 3 failed attempts.
- Provider-failure blocks were cleared on wrap-up (markers moved to `~/.local/state/shokunin-hyaku/blocked/.<lane>.run15-20261104-provider-failure-4`): chousa r80, kaidoku r90, kake r93, kama r86, kasegi r71, kengaku r86, kotoba r87, kotodama r90, mado r86, mori r90, tabi r64. On resume those rounds relaunch at attempt 1 and adopt each lane's uncommitted in-flight work.
- **Quality pauses still BLOCKED (3 consecutive rejected closures; operator fresh-start authorization needed):** kagi (next 37), kumitate (90), revenger (92), souji (61), tameshi (87), tsukuroi (83).
- Routing at wrap-up (config.yml; amendments 14-19 in scripts/hyaku/lane-addendum.md):
  - m_flash = amr/deepseek-v4.1-flash:high. Chain: amr -> opencode-go -> commandcode -> devin/swe-2-flash.
  - m_zfl (zai glm-5.3-flashx) for reviewer and executor.
  - m_mim (MiniMax-M3.1-Flash -> haiku -> glm-5.3-flash -> swe-2-flash) for scout and scribe.
  - connector = devin/swe-2-flash:high. All other roles @m_flash.
  - alibaba-token-plan removed.
- In-flight lane work left uncommitted for the next L1s: kama, tabi, mado, kaidoku, kake, kasegi, kengaku, kotodama. Examples: kake r93 `scripts/conditional_eval.py` (sha256 d3bac7de, frozen counter met=true on a scratch commit, needs landing plus a re-score); kaidoku round-90 plan/tools.
- All 17 lane repos are pushed: 0 unpushed commits vs origin.
- Fleet notes:
  - `.ufo/reports/round-84/kama.md` was a misroot overwrite (kama r86 SN01 F1), restored to HEAD. The overwrite is preserved at `.scratch/run15-wrapup/round-84-kama.misroot-overwrite.md`.
  - `.ufo/reports/round-89/kaidoku.md` has an uncommitted post-closure fill by a dead L1. It is left as is; the closure already judged that round a marker (rounds[1293]).
- Resume recipe:
  1. Confirm credentials with a route smoke (`agent('Reply with exactly: ROUTE_OK. No tools.', agent='critic', label='RouteSmoke')`, then read the session jsonl provider).
  2. `%load scripts/hyaku/inline-dispatcher.py`, then `%load .scratch/run15-kernel.py`, each in its own cell.
  3. `await bootstrap()`.
  4. `rm .scratch/run15-drain`.
  5. Loop `await run_for(1200)`.
- Late wrap-up (Amendments 20-21): `retry.maxRetries` 5 -> 10.
  - omp rotates sibling keys only on usage-limit-classified errors. Stored keys: amr 5, commandcode 7, opencode-go 13 (3 unblocked), devin 4.
  - A 401 on one commandcode key walks the model chain without trying the other 6.
  - After the restart, the first route smoke should confirm which keys authenticate.
- Post-wrap-up late seats committed as "not a landed round": kasegi 34faab90 and 3cc8cd45, kake d838e744.
  - kake r93 integration owes a 3-entry freshness-sidecar re-pin: spec at `kake-shokunin/.ufo/waves/round-93/w1/ScribeC1Prose/sidecar-repin-for-L1.json`. Without it the paths sweep exits 2.
  - Zero subagents were running at restart time.

## Resume 2026-11-05 (operator restarted omp with new credentials)
- Route smoke: m_flash amr still 402 (quota until 2026-11-06T22:28Z) -> served by commandcode; scribe haiku-5-5 ok; reviewer zai glm-5.3-flashx ok; scout MiniMax ok. connector devin/swe-2-flash -> `permission_denied: model no longer available`, fell to openai-codex/gpt-6.1-sol. devin/swe-2-flash is the dead tail of every chain.
- bootstrap(): nothing to adopt, nothing live. Drain flag removed; campaign loop resumed. Six quality pauses still blocked pending operator fresh-start authorization.
