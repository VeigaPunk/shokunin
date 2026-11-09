# souji round 100 — session-owned escapee reap is structurally unreachable (C1 harmed); S075/S332 attribution repair (C2)

Lane base `a662bb0d7e033cc5ceccd70b52eb234404300845`. Attempt 2 (`SoujiR100a2`), inherited from attempt 1
(`SoujiR100`) which died mid-wave: reused `census/round-100/c2-*.py`, the uncommitted `corpus/knowledge/deadline-owned-reaping.md`
+ `corpus/SOURCES.md` edits, and 11 of 14 seat dirs in `.ufo/waves/round-100/w1/`; discarded the never-WAVE-DONE
results.json-less state; re-ran the live measurements L1-side with fresh `--work` dirs. No `merge/souji/` theme,
no `considerthese/` dir (Assimilation: none).

## Work performed

- **C1 (operability 8, Q177)** — successor counter `census/round-100/c2-setup-arms.py` with branch (b) (field-6
  session key); falsified live: the escapee's session is its own pid, the spawn's session is the spawn pid, so
  `escapee_sid == spawn_sid` is False by construction. Evidence pointers: `census/round-100/records/c2-escapee-r100.txt`
  (L1, pid 3418284, alive=1), `census/round-100/wave-evidence/ReviewerC1Predicate.md` (attacks a/b/c),
  `SentinelEscapee/sid_chain_probe.py` (dry probe `owned_count=0`), `ConnectorOverlap/session-key.txt`.
- **C2 (calibration 7, correction-class)** — append-only correction block in `corpus/knowledge/deadline-owned-reaping.md`
  citing S332 for field-4 ppid; S075 row `used-by` gains the entry. Evidence: `grep -c 'S332'` = 1 at
  `corpus/knowledge/deadline-owned-reaping.md:80`; `corpus/SOURCES.md:110` used-by tail names the entry
  (ExecC2Attribution.md; ReviewerC2Attribution F1/F2 carried as graded gaps).
- **Controls** — r99 counter on the same decoy test (fresh work): alive=1, spared 84/84 (L1, receipts
  `census/round-100/records/c2-decoy-r100.txt`, `c2-counter-r100.txt`); r97 argv-only mutant kills 60
  (`census/round-99/records/c2-decoy-r97.txt` read-only); CM8 mutant kills 82 (`c2-decoy-cm8.txt`).
- **Frontier sources** — S075/S332/S368 re-opened by ScoutSources, 23/23 checks pass
  (`.ufo/waves/round-100/w1/ScoutSources/verify-run.txt`); lesson `corpus/lessons/round-100.md` with M14/M15.
- **Wave shape** — one v1 wave, 14 seats: 2 executor, 2 reviewer, 1 critic, 1 mutation-tester, 1 sentinel,
  1 connector, 1 scout, 1 scribe, 1 revenger, 1 labrat; attack 7/14 (50 %); connector 1. Dead seats (2):
  `MutC1SessionKey` produced no dir; `ExecC1SessionApplier`/`ExecC1SessionNoReap` dirs empty at attempt-1 end
  (build verified from the worktree diff instead). No residual call.

## Landed changes

- `census/round-100/c2-setup-arms.py`, `census/round-100/c2-decoy-test.py`, `census/round-100/records/` (3 receipts),
  `census/round-100/wave-evidence/` — LANDED `cbe068d03eb5a49fc0736bef89f182679a86ca51` (LOG round-100 entry).
- `corpus/knowledge/deadline-owned-reaping.md` (+5 lines append-only), `corpus/SOURCES.md` (S075 used-by tail),
  `corpus/lessons/round-100.md` (M14/M15), `SCORECARD.md` (round-100 rows), `LOG.md` (round-100 entry) — same
  commit `cbe068d03eb5a49fc0736bef89f182679a86ca51`.
- `plans/round-100.md` was already committed by attempt 1 (`bf990609bfc621e7175bc10e42472d07112cac39`).

## Before → after measurements

- **C1.** Before: r99 counter `ESCAPEE-ALIVE alive=1` (`census/round-99/records/c2-escapee-r99.txt`).
  After: r100 counter `ESCAPEE-ALIVE alive=1` + `DECOY-SUMMARY verdict=spared` 83/83
  (`census/round-100/records/c2-escapee-r100.txt`, `c2-decoy-r100.txt`). Counting command:
  `python3 -B census/round-100/c2-decoy-test.py --counter census/round-100/c2-setup-arms.py --probe census/round-98/c2-forgery-probe.py --tool tools/souji-record-agreement.py --before census/round-92/controls/c2-before-tool.py --work <fresh> --arm-timeout 200 --plant-delay 2` + live `/proc` argv scan of `<work>/arms/fixture-pipe-holder.py`. Measured at `cbe068d03eb5a49fc0736bef89f182679a86ca51`. Verdict: **harmed (trade); not admitted**. The `m_noppid` mutant is vacuous under this rule (branch (b) never fires on the escapee); the r98 branch-(c) net remains the only in-lineage escapee mechanism (RevengerR98Rule).
- **C2.** Before: leg1 `grep -c 'S332' corpus/knowledge/deadline-owned-reaping.md` = 0; leg2 S075 used-by = 0 (both at base `a662bb0d`).
  After: leg1 = 1, leg2 = 1. Counting command: the pair of greps above; sources-census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` EXIT 0, 294 rows before/after. Measured at `cbe068d03eb5a49fc0736bef89f182679a86ca51`. Verdict: **improved (verifies under the frozen predicate)**; Q62 graded gaps carried (body-only cite, no S332 located quote — ReviewerC2Attribution F1/F2).

## Sources & frontier

SOURCES.md rows before→after: 294 → 294 (`grep -cE '^\s*\| S[0-9]' corpus/SOURCES.md`). Counting command at round start
(294 rows, EXIT 0) and round end (294 rows, EXIT 0):
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`
(output: `ok …corpus/SOURCES.md`; pre-existing W04 duplicate-URL warnings only). Rows added by tier: none.
Rows touched old→new: S075 used-by only (append `, corpus/knowledge/deadline-owned-reaping.md`; no status/recheck/
row change; S332/S368 rows unchanged). Frontier rows advanced: none. Sourced claims: C1 rests on S075+S368,
C2 rests on S332 — each opened this round by ScoutSources (HTTP 200, byte-identical captures).
Assimilation: none. Mistakes mined: `corpus/lessons/round-100.md ## Mistakes` M14 (session-key never fires; shown able to fail
by the sentinel dry probe + both live alive=1 runs) and M15 (arity snapshot; shown able to fail by the unpack proof).

## Trend verdicts

- expansion: **unchanged**. No registry row added; S075/S332/S368 re-verified only (census 294→294, EXIT 0).
- quality: **improved** for C2 attribution (bidirectional grep 0/0 → 1/1) and **harmed** for C1 (a new rule that cannot
  fire replaces no rule); net quality: **improved** on the calibration axis, harmed on the operability axis — axis verdicts
  do not cancel; the round reports both.
- discernment: **harmed**. The pre-freeze gate froze a structurally unreachable predicate (M14); four non-author seats
  (Reviewer, Critic, Sentinel, Connector) caught it. The gate did not.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  Evidence: SKILL.md Decision tables/Error patterns/Checklists/Gate registry; corpus/SOURCES.md S100-S103 (pre-existing rows, unchanged this round).
- [~] At least one end-to-end domain task executed and logged in LOG.md
  Evidence: LOG.md round-100 entry (C1 live decoy+escapee runs with fresh work dirs, C2 grep legs).
- [~] Instructions executable by an agent without oral context
  Evidence: census/round-100/c2-decoy-test.py + c2-setup-arms.py counting command above re-runnable by the closure.
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  Evidence: PROVINCE.md untouched; only souji-lane corpus/census bytes landed; one mount-point check: `git status --porcelain` at the fleet root verified below.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Tool installs: none.
L0 side channel: reap-authority question `souji | round-100` appended to `.ufo/l0-questions.md`.
