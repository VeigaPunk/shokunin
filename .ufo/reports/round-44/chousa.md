# chousa — round 44

- Lane: `chousa-shokunin` (deep-research method 調査), branch `master`
- Round: 44 (attempt 1). L1: **Kimi fresh L1** (`Kimi fresh L1` metadata; this agent
  resumed a round whose previous L1 died on a provider-route failure — see *Inherited state*).
- Lane repo: `/home/vgpnk/Projects/shokunin/chousa-shokunin`
- Lane tip (landed, pushed): `44aaf33cd37e2583fff13397f5a4b60a011ec1ab`
  (`jj-lane.sh state` → `local=remote=44aaf33c…`, `ahead=0 behind=0`)
- Round launch: `2026-10-24T21:36:37-03:00` (`.ufo/watchdog.log`, `launch chousa round=44`)
- **No external fetch.** L0 `8d77e6c1` is still open; every source opened this round was
  opened from a capture already committed on disk. No URL was fetched.
- Stale-lane: none — this lane has no other open mission; the respawn-per-round driver
  dispatched exactly this round.
- Tool installs: none. Nothing was installed, upgraded or removed this round.

## Work performed

Three claims, declared and frozen in `corpus/evidence/round44/claims.md` at lane commit
`043f19a1db91288947493d9f879e61e7a9f07241` **before any seat scored** (the freeze is a
committed artifact, not prose):

- **C1 — operability** (the lowest scored non-retired axis, 3/10): a *launcher receipt that
  proves parent lifetime* replaces the prose assertion the round-43 closure could not resolve.
  Predicate: the receipt's start and end `parent_pid` are the same positive integer,
  `n_spawned == n_reaped == 64`, every seat name is the frozen name, every `child_pid` positive.
- **C2 — calibration**: the 39 inherited r40/r41 working-tree paths are dispositioned **one by
  one**, never swept blindly. 36 untracked seat reports are `reverified-commit` (stem, round
  token, length > 80, sha256 re-derived before the path is committed); 3 modified JSON paths
  stay `left-named` with reason `not hunk-verified` and are **not** committed.
- **C3 — depth** (sourced): `corpus/knowledge/citation-version-binding-r36.md` cites lane
  **S079**, that row's URL is `https://www.rfc-editor.org/rfc/rfc7089.txt`, and the located
  quote `constitutes a promise that the resource state` is a substring of that URL's committed
  capture. The entry must not cite `source: S081`.

Work items:

- Froze the three claims, the three counters, the do-nothing controls and the two
  cheapest-gates before any seat scored — `corpus/evidence/round44/claims.md`,
  `c1-count.py`, `c2-count.py`, `c3-count.py`, `controls/{pids0,prose}.receipt`,
  `controls/all-left.tsv`, `controls/errata-{two,zero}.txt`; freeze commit
  `043f19a1db91288947493d9f879e61e7a9f07241`.
- Wrote `tools/parent-lifetime.sh` — a launcher that owns the child pids and the wait in one
  shell and appends its own receipt — and fixed the `--auto`/`--prompt` flag conflict that
  killed wave 1 (`tools/parent-lifetime.sh:73`; wave-1 seat log tail
  `error: Cannot combine --prompt with --auto.`).
- Landed the wave-1 launcher receipt as committed evidence:
  `corpus/evidence/round44/parent-lifetime.receipt` — `start parent_pid=3226659`, 64 `spawn`
  lines, 64 `reap` lines, `end parent_pid=3226659 … n_spawned=64 n_reaped=64`.
- Dispositioned the 39 inherited paths individually into
  `corpus/evidence/round44/disposition.tsv`, with the sha256 of each re-verified file recorded
  in its row, and committed the 36 re-verified reports as historical wave evidence
  (commit `6254b4d859830ff27c7b44d7b2567c2f9f96255a`). The 3 modified JSON paths stay named
  and uncommitted.
- Ran the item-10 assimilation on **one theme** — the version binding of a citation to a prior
  state — and adopted two entries from `merge/chousa/` with three rows: `citation-version-binding-r36.md`
  (lane S079) and `citation-version-binding-r37.md` (lane S080, S081). Collision check,
  table normalization, used-by closure, recheck normalization and validate-before-append were
  all run in scratch first (`.ufo/waves/round-44/assimilation/`).
- Mined **one** unimplemented `considerthese` proposal — "Count claim errata per round" from
  `considerthese/2026-10-24.md` — into **QUALITY 62**. The considerthese file was not edited.
- Added **QUALITY 63** from a wave-3 probe: a launcher's exit status is not evidence that its
  seats ran (`tools/parent-lifetime.sh` exits 0 on a malformed dispatch with `n_spawned=0`).
- Appended the round's lesson `corpus/lessons/round-44.md` with five mined mistakes and the
  Gate block (≥1 admit, 2 rejects with reason and flip), and added the two adopted entries to
  the corpus coverage map `corpus/README.md`.
- Ran the census before and after (`exit 0`, the same five W04 both times), and swept the fleet
  root for misrooted seat files (`git -C /home/vgpnk/Projects/shokunin status --porcelain`;
  no file of this round's was found outside the lane tree).

## Landed changes

| change | LOG.md entry | lane commit (landed) |
|---|---|---|
| launcher receipt + the round's landed content: counters, controls, claims file, disposition table, `parent-lifetime.receipt`, the two knowledge entries, SOURCES rows S079–S081, QUALITY 62/63, SCORECARD, LOG, lesson, wave evidence (specs, plans, dispatches, 3 settle tables, 128 seat logs, assimilation scratch) | `LOG.md` "Round 44 — freeze" and "Round 44 — landing" | `b603302c0a0c064fcaef3da672a3f0b465f9f448` |
| the 36 re-verified inherited r40/r41 seat reports, committed as historical wave evidence (C2 `reverified-commit` class) | `LOG.md` "Round 44 — landing", C2 bullet | `6254b4d859830ff27c7b44d7b2567c2f9f96255a` |
| the wave-2 connector seat log (2.2 MB, above the directory-add size) | `LOG.md` "Round 44 — landing", wave-evidence bullet | `9b108fdb56316cba5fe02db8ee62c65608fbd41a` |
| the post-commit re-run of the three counters and the census | `LOG.md` "Round 44 — landing" | `78aa1fd2a6ede8a2d886d98e780705386425495a` |
| the two adopted entries added to the corpus coverage map | `LOG.md` "Round 44 — landing" | `44aaf33cd37e2583fff13397f5a4b60a011ec1ab` (lane tip) |

Fleet repo: the L0 append landed at fleet commit `44479ed61c426dedd6093852cf03cd0e96344715`;
this report lands last and cites the pushed lane hash `44aaf33cd37e2583fff13397f5a4b60a011ec1ab`.

## Before → after measurements

| claim | before | after | counting command | measured against |
|---|---|---|---|---|
| C1 operability | `N_SPAWNED=0/64`, `N_REAPED=0/64`, `PARENT_PID_MATCH=0/1`, `ZERO_PIDS=1`, `NAMES_MATCH=0/64`, `C1=FAIL receipt-missing`, exit 1 (`corpus/evidence/round44/receipts/c1-before.txt`) — no committed launcher log existed, so the round-43 closure could not resolve the parent-lifetime claim | `N_SPAWNED=64/64`, `N_REAPED=64/64`, `PARENT_PID_MATCH=1/1`, `ZERO_PIDS=0`, `NAMES_MATCH=64/64`, `C1=PASS`, exit 0 | `python3 corpus/evidence/round44/c1-count.py` | `corpus/evidence/round44/parent-lifetime.receipt`, committed in `b603302c…`; re-run post-commit at `78aa1fd2…` (`receipts/counts-after.txt`) |
| C2 calibration | `CONSISTENT=0/39`, `REVERIFIED=0/36`, `LEFT_NAMED=0/3`, `C2=FAIL table-missing`, exit 1 (`receipts/c2-before.txt`) — the 39 inherited paths were unswept and unnamed | `CONSISTENT=39/39`, `REVERIFIED=36/36`, `LEFT_NAMED=3/3`, `C2=PASS`, exit 0 | `python3 corpus/evidence/round44/c2-count.py` | `corpus/evidence/round44/disposition.tsv`, committed in `b603302c…`; the 36 reports committed in `6254b4d8…`; re-run post-commit at `78aa1fd2…` |
| C3 depth | `ENTRY_CITES=0/1`, `QUOTE_LOCATED=0/1`, `URL_MATCH=0/1`, `C3=FAIL entry-missing`, exit 1 (`receipts/c3-before.txt`) — the lane held no opened source binding a citation to a prior state | `ENTRY_CITES=1/1`, `QUOTE_LOCATED=1/1`, `URL_MATCH=1/1`, `C3=PASS`, exit 0 | `python3 corpus/evidence/round44/c3-count.py` | `corpus/knowledge/citation-version-binding-r36.md` + `corpus/SOURCES.md` row S079, committed in `b603302c…`; re-run post-commit at `78aa1fd2…` |

Do-nothing controls, all re-run at landing (`corpus/evidence/round44/receipts/controls-after.txt`):
`c1-count.py --receipt /tmp/nonexistent.receipt` → `C1=FAIL receipt-missing`, exit 1;
`controls/pids0.receipt` → `C1=FAIL`, exit 1; `controls/prose.receipt` → `C1=FAIL prose`, exit 1;
`c2-count.py --table controls/all-left.tsv` → `REVERIFIED=0/36`, `C2=FAIL`, exit 1;
`c3-count.py --entry /tmp/nonexistent-entry.md` → `C3=FAIL entry-missing`, exit 1.

Mutation probes run by wave-3 seats (copies under `/tmp` only): C1 flips to `C1=FAIL`, exit 1,
on a zeroed `reap` child pid (`ZERO_PIDS=1`) and on a changed `end parent_pid`
(`PARENT_PID_MATCH=0/1`); C2 flips to `C2=FAIL`, exit 1, on a corrupted digest
(`REVERIFIED=35/36`), a blank reason (`REVERIFIED=35/36`), a deleted row (`LEFT_NAMED=2/3`)
and a modified path reclassified as `reverified-commit` (`LEFT_NAMED=2/3`). No mutant false-PASSes.

## Sources & frontier

- Registry rows before → after: **78 → 81**.
  Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`
  (before: `git show e6983f6e242c7b82bd9a9c5ee170257624e8f109:corpus/SOURCES.md | grep -cE …` → 78).
- Rows added: 3 — **S079** (RFC 7089, type `spec`, tier A, `mined`, recheck `365d`,
  used-by `corpus/knowledge/citation-version-binding-r36.md`), **S080** (NDL WARP FAQ, type
  `docs`, tier A, `mined`, recheck `90d`, used-by `citation-version-binding-r37.md`), **S081**
  (NDL current-awareness E2867, type `paper`, tier A, `mined`, recheck `180d`, used-by
  `citation-version-binding-r37.md`). Rows added by tier: **A 3**. No row was added at tier B or C.
- Rows touched old → new: **none**. No pre-existing row's `status`, `recheck` or `used-by`
  changed; the diff base → tip is three added rows plus the round-44 log paragraph.
- Frontier rows advanced: the corpus coverage map `corpus/README.md` gained **2** rows (the two
  adopted entries). The `## Leads (unopened)` section is unchanged. Debt named, not fixed:
  round 43's adopted entry `knowledge/search-log-method-r39.md` still has no coverage-map row
  (the map stops at round 41) — backfilling another round's row was not this round's work.
- Census before → after:
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`
  → at round start `exit 0` with five W04 (S051, S053, S073, S074, S075) and `chousa ok`
  (`corpus/evidence/round44/receipts/census-start.txt`); at round end `exit 0` with the same
  five W04 and `chousa ok` (`receipts/census-end.txt`). The validate-before-append mirror
  (`.ufo/waves/round-44/assimilation/validate/corpus/SOURCES.md`) exited 0 with no E03/E04
  before the first registry append, re-checked by wave-3 seat `W3ExecFileCensus`.
- Assimilation decisions (item 10, one theme: *the version binding of a citation to a prior
  state*). Read-only source: `/home/vgpnk/Projects/shokuknow/merge/chousa/` was read, never
  written. **Collision check in scratch**: `assimilation/collisions` is **empty** — S077 is not
  a row-start id in the staged append; it occurs once, inside a cell of staged S093. The
  indented-row guard was proved once before the first append (`assimilation/guard/collisions`
  contains `S079` for a scratch `  | S079 |` row; the column-zero-only pattern misses it).
  **Ids bound by document, not arithmetic**: the URL is the evidence and the id follows it —
  the staged file itself calls PRISMA-S "S079", and the landed offsets are −2 (S081→S079),
  −11 (S091→S080) and −11 (S092→S081), so no constant shift reproduces the landed binding
  (wave-3 seat `W3SimpIds`). **Transformation**: every staged row was normalized to the
  lane's 11-column schema — `recheck` prose stripped to `365d`/`90d`/`180d` (the stripped
  re-verify conditions and Gate pointers are recorded in the lesson's Gate block), no cell
  contains a literal or escaped `|`, `used-by` lists exactly the admitted entries that cite
  the row, `status` is `mined`. **Rejected with reason and flip**: staged S082 (the SAMR record
  for GB/T 7714-2025) and the GB/T half of `citation-version-binding-r36.md` — round 43 classed
  that row *not-carried* and this round did not fetch; flip: a text capture of that record
  contains the issued and effective dates as one contiguous span. Staged S093 (the Portico page)
  and the Portico half of `citation-version-binding-r37.md` — round 43 classed that row
  *misquote*, and a partial overlap is not the register's sentence; flip: a capture where the
  four-factor authenticity sentence is one contiguous span matching the staged teaches cell.
  **considerthese**: one still-unimplemented proposal mined — "Count claim errata per round"
  (`considerthese/2026-10-24.md`, 2026-10-24) → QUALITY 62, whose criterion is shown able to
  fail (`controls/errata-two.txt` counts 2 and exits 0; `controls/errata-zero.txt` counts 0 and
  exits 1). This round's own claims file counts 0. The considerthese file was not edited and no
  second proposal was mined.
- No source row's `status`, `recheck` or `used-by` was changed for a pre-existing row, so no
  frontier row of the lane's own registry was advanced beyond the two entries above.

## Trend verdicts

- **expansion: improved** — three new mined rows (S079, S080, S081), two new knowledge entries
  on a theme the lane did not hold (RFC 7089's Memento promise; the NDL WARP capture cadence and
  timestamped-URL anchor), one new gate (`tools/parent-lifetime.sh`), one new lesson, two new
  QUALITY criteria. Registry 78 → 81, coverage map +2 rows. The count is a census-verified row
  count, not a prose impression.
- **quality: improved** — three counters with do-nothing controls that all fail; the C1 and C2
  kill rules were mutation-tested by wave-3 seats and no mutant false-PASSes; the admitted
  quote re-locates in its committed capture at byte offset 14896; QUALITY 62 is shown able to
  fail; QUALITY 63 records a launcher defect found this round. Named limits: the C2 counter
  cannot see a coordinated two-file edit (report bytes plus its digest row), and its reason text
  is checked only for non-emptiness (wave-3 seat `W3CritBlind`).
- **discernment: unchanged** — the lane's own admit/reject reasoning is recorded and checkable
  (2 admits, 2 rejects with reason and flip, the S077 collision handled by document), but no
  non-author spot-check has yet run against this round, and a seat this lane dispatched is still
  the lane. Unchanged is the honest grade until the closure reviews it.

## Waves

Round shape: **three v1 waves, 128 seats total** — the round ceiling. This is a deviation from
the default two-v1-wave shape and it is named here rather than smoothed over: wave 1's seats
all died at spawn, so wave 2 was dispatched as a recovery wave with new names (the 64 dead names
were not replaced), and wave 3 was dispatched because wave 2's parent receipt was truncated when
the orchestrator process died mid-wait. The operator's ruling on the shape is asked in
`.ufo/l0-questions.md` (`chousa | round-44`). Both waves that could be validated were validated
under policy v1 (`scripts/hyaku/ufo-wave-policy.json`, band 32–64) with `ufo-swarm-wave.mjs
plan`/`run`; wave 3's plan and dispatch payloads are committed.

| wave | grant | seats | role mix (attack share) | reports | dead seats | parent-lifetime receipt |
|---|---|---:|---|---:|---:|---|
| w1 (build, 64) | `granted lane=chousa wave=round-44-w1 seats=64 live=43 pending=64 cap=256` (`.ufo/waves/round-44/launcher-outer.log`), released after settlement | 64 | reviewer 8, critic 8, mutation-tester 6, sentinel 2, revenger 2 = **26 attack (40.6%)**; executor 12, scout 10, scribe 8, connector 4, simplifier 4 | 0 | **64** — every seat exited 1 with `error: Cannot combine --prompt with --auto.` | **complete**: `start parent_pid=3226659` … `end parent_pid=3226659 n_spawned=64 n_reaped=64` (`corpus/evidence/round44/parent-lifetime.receipt`) |
| w2 (falsify, 32) | `granted lane=chousa wave=round-44-w2 seats=32 live=44 pending=0 cap=256` (`.ufo/waves/round-44/w2-launcher-outer.log`) | 32 | reviewer 4, critic 4, mutation-tester 2 = **10 attack (31.2%)**; executor 8, scout 6, scribe 4, connector 2, simplifier 2 | 31 | 1 (`W2ScribeQ62`, no report) | **truncated**: 5 reap lines, **no `end parent_pid=` line** — the launcher was killed when the orchestrator process died, so this receipt proves nothing about parent lifetime |
| w3 (falsify, 32) | `granted lane=chousa wave=round-44-w3 seats=32 live=54 pending=0 cap=256` at 22:28:17, released at 22:35:25 after settlement (`.ufo/waves/round-44/w3-launcher-outer.log`) | 32 | reviewer 4, critic 4, mutation-tester 2, revenger 1, sentinel 1 = **12 attack (37.5%)**; executor 8, scout 4, scribe 4, connector 2, simplifier 2 | 9 | **23** — 27 seats killed by the 420 s `timeout --signal=TERM` (exit 124); 4 of them had already written their report | **complete**: `start parent_pid=3635446` … `end parent_pid=3635446 n_spawned=32 n_reaped=32` (`.ufo/waves/round-44/w3/parent-lifetime.receipt`) |

- **Round total: 128 seats dispatched, 40 seat reports written, 88 seats without a report.**
  Dead seats were not replaced and are not credited. Settlement is reconstructible from
  committed bytes: `.ufo/waves/round-44/{w1,w2,w3}-settle.tsv` (name, role, outcome, exit code,
  last error) plus each wave's launcher receipt.
- **§3 L2 floor**: met inside waves 2 and 3 — 1× planner (held by this L1; the validator rejects
  the frozen `planner` role, and the planning data-walk rode the connector and scout items),
  2× connector, 8× executor, 4× scribe, 4–6× scout, 4× reviewer, 4× critic, 2× mutation-tester.
  Wave 1 declared the same floor but no seat in it ran.
- **Routing**: the host route table is `~/.omp/agent/config.yml`
  (`task.agentModelOverrides` → `m_sol`/`m_flash`/`m_zfl`/`m_grok`/`m_mim`, `maxConcurrency: 400`,
  `maxJobs: 450`). The Kimi substrate exposes no per-seat role→model knob to a lane, so all
  seats ran on the Kimi host's own default route and the lane passed **no** model: no alias is
  hardcoded anywhere in the lane repo. The wave-2 and wave-3 seat logs record
  `kimi version 2.3.1`; the answering model per seat was not separately exposed and is not
  claimed.
- **Seats never mutated** the fleet repo, a sibling lane, the lane's jj state, the lane Git
  index, or the network. Scratch copies were written under `/tmp` only. The fleet-root
  misroot sweep found no file of this round's outside the lane tree.
- **Shortfalls, stated plainly**: 88 of 128 seats produced no report; wave 2's slot was never
  released by the dead orchestrator (the ledger shows no live chousa reservation now, and
  wave 3's acquire succeeded with `pending=0`); the launcher's default 420 s timeout
  (`tools/parent-lifetime.sh:20`) killed 27 of wave 3's 32 seats. Because the round was already
  at its 128-seat ceiling, no further wave was dispatched and the dead seats stayed dead.

## Inherited state (the previous L1's partial round)

The round-44 L1 that died on a provider-route failure left committed and uncommitted work; it
was inspected, re-verified and dispositioned rather than restarted or re-declared:

- **Kept and re-verified**: the frozen claims file, the three counters, the controls and the
  wave-1 launcher receipt, all committed at `043f19a1…` before any seat scored; the 64 wave-1
  seat logs (evidence for the `--auto`/`--prompt` defect); wave 2's spec, plan, dispatch,
  registry, 31 seat reports and truncated receipt; the two drafted knowledge entries; the
  scratch assimilation mirror and its passing census.
- **Changed**: `tools/parent-lifetime.sh` — the `--auto` flag was dropped (it cannot combine
  with `--prompt` on kimi 2.3.1), which is what made wave 3 possible; the lesson gained the
  `## Mistakes` items 3–5 and the `## Spot-check` section; the SCORECARD and LOG gained this
  round's landing entry; the coverage map gained two rows.
- **Kept but not credited**: wave 2's receipt is not counted as parent-lifetime evidence, and
  wave 1's receipt counts only as a launcher receipt — its 64 seats produced no work.

## Round-43 closure repairs (the routed items)

1. **Parent-lifetime receipt does not resolve** → *repaired by evidence, not prose*. The launcher
   now writes the receipt from the same pid that spawned and reaped the children, and the
   receipt is **committed** (`corpus/evidence/round44/parent-lifetime.receipt`, in `b603302c…`),
   with the wave-3 receipt as a second complete receipt (`n_spawned=32 n_reaped=32`). The
   round-43 prose assertions (`kimi --agent-file`, `pids 0`, "a waiter parent") are not
   repeated anywhere as evidence.
2. **Freshness self-grade** → *repaired*. This round's SCORECARD records **freshness: unchanged**,
   not improved. Every capture opened this round (RFC 2026-10-23 20:33, WARP 20:36, E2867 20:37
   -0300) predates the round launch (2026-10-24T21:36:37-03:00), and no live surface was
   re-checked. The axis is not harmed.
3. **The 39 inherited r40/r41 paths** → *dispositioned by re-verification, never swept*.
   36 untracked seat reports: each was re-read, its basename stem and round token checked, its
   length checked and its sha256 recomputed and compared with its table row, and only then
   committed (`6254b4d8…`). 3 modified JSON paths stay `left-named`, uncommitted, reason
   `not hunk-verified`. The r43 L0 line asking the operator to rule on them is **not duplicated**
   here and stays open.

Open L0 questions (all still open, none duplicated by this round): the fetch-scope ruling
`8d77e6c1`; the campaign register staleness; the inherited r40/r41 working-tree decision; and
one new line from this round — `chousa | round-44` — asking the operator to rule on the wave
shape and on whether a wave whose seats all died at spawn counts against the 128-seat round
ceiling.

## SHONEN

Promotion is operator-owned; no box is promoted here and no box is marked `[x]`.

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  `SKILL.md` Gates table; `corpus/knowledge/metadata-screen-r25.md`; this round's
  `corpus/lessons/round-44.md` (lane assertion; no non-author verifier)
- [~] At least one end-to-end domain task executed and logged in LOG.md
  `LOG.md` "Round 44 — landing"; `corpus/evidence/round44/receipts/counts-after.txt`; the
  128-seat wave with committed settle tables (lane assertion)
- [~] Instructions executable by an agent without oral context
  `bash tools/parent-lifetime.sh --selftest --receipt /tmp/...` (exit 0, measured by wave-3 seat
  `W3ExecSelftest`); `corpus/evidence/round44/claims.md` (lane assertion)
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  `PROVINCE.md`; this round's entries are the lane's own re-grounding of staged package material
  on its own province (version binding of a citation); the campaign tree was read only
  (`.ufo/waves/round-44/w3/W3CritScope.md`; lane assertion)

## Evidence pointers

- Lane repo tip: `44aaf33cd37e2583fff13397f5a4b60a011ec1ab` (pushed; `ahead=0 behind=0`).
- Lane commits this round: `043f19a1db91288947493d9f879e61e7a9f07241` (freeze),
  `b603302c0a0c064fcaef3da672a3f0b465f9f448` (landing),
  `6254b4d859830ff27c7b44d7b2567c2f9f96255a` (36 inherited reports),
  `9b108fdb56316cba5fe02db8ee62c65608fbd41a` (oversize seat log),
  `78aa1fd2a6ede8a2d886d98e780705386425495a` (post-commit counters),
  `44aaf33cd37e2583fff13397f5a4b60a011ec1ab` (coverage map, tip).
- Fleet commits: `44479ed61c426dedd6093852cf03cd0e96344715` (L0 append); this report lands last.
- Round artifacts: `corpus/evidence/round44/{claims.md,c1-count.py,c2-count.py,c3-count.py,
  disposition.tsv,parent-lifetime.receipt,seat-names.txt,errata-count.py,controls/,receipts/}`,
  `corpus/lessons/round-44.md`, `corpus/knowledge/citation-version-binding-r36.md`,
  `corpus/knowledge/citation-version-binding-r37.md`, `tools/parent-lifetime.sh`,
  `.ufo/waves/round-44/{w1,w2,w3}-settle.tsv`, `.ufo/waves/round-44/assimilation/`.
