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
