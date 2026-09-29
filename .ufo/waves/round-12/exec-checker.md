# Round 12 — the executable closure gate (protocol lane / integrator-of-record)

`.ufo/waves/round-12/closure-check.py` — python3 stdlib, read-only, deterministic; five outputs (last-wins
ledger; unresolved `in-flight` rows + launch pointer; rows contradicting evidence; dispatched lane-rounds with
no valid row, and those dispatched after their round's closure; tallies + stale-mission grades). Exit map
(also in `--help`): 0 clean · 1 debt/contradiction · 2 could-not-evaluate · 3 no pinned baseline.

## Files

| Path | What |
|---|---|
| `.ufo/waves/round-12/closure-check.py` | the gate; `--repo`, `--json`, `--show-keying`, `--selftest`, `--frozen NAME`, `--no-ledger`, `--no-citations` |
| `.ufo/waves/round-12/fixtures/closure-sample/<15 cases>/` | synthetic MANIFEST+log+reports trees with a pinned `expected.json` (exit + 5 counters) |
| `.ufo/waves/round-12/frozen/{pre,post-actual,post}/` | snapshots + `expected.json`, `CLOSED_AT.txt`, `patch-entries.json`, `README.md` (the freezing rule) |
| `.ufo/waves/round-12/mutants/{m0..m7}/`, `mutant-score.json` | detection harness: MANIFEST copies + symlinked `.ufo`; no repo writes |

## Semantics implemented

| Rule as implemented | PROTOCOL.md |
|---|---|
| a row names lane-round `(lane, entry.round)`; `lane_rounds[id]` is the counter annotation, never a re-key; last row per `(lane, lane_round)` wins; append-only, corrections carry `supersedes` (index-validated, `supersedes.entry` supported) | 264–269, 280–287 |
| legacy `scaffold`/`work`/`ops` entries are fleet-keyed → `unadjudicable`, never a status | 228–231 |
| dispatch evidence = `launch`/`steer` line; a prompt with no dispatch line = attempted dispatch → `failed`; completion evidence = report at the contract path, contentless marker → `failed` (bytes, hash token, `SHONEN`) | 163, 233–241 |
| termination = `complete` line **or** counter past N **or** a *landed* report (`landed_at <= instant`) | 241–242 |
| `in-flight` decided from the absence of a `complete` line and a landed report — never a liveness probe; it is debt, answered by the next pass (terminal status or re-confirmation + launch pointer) | 245–246, 253–260 |
| no `not-dispatched` while dispatch evidence exists; no `in-flight` unless live at `closed_at`; `closed_at` required on those rows | 230, 261–263 |
| shape contradictions: `not-dispatched` without `lane_rounds`; unknown lane (roster = `MANIFEST.json` `roster` ∪ protocol/aggregator); non-string/outside-vocabulary status; `lanes` not a map (list duplicates named); `supersedes` naming no earlier entry / ambiguous / index mismatch; and `keying_violation` — a `lane_rounds` value naming an absent identity, sitting behind the lane's counter at `closed_at`, or (on a `not-dispatched` row) not behind the entry round | 206–207, 261–269, 280–287 |
| stale-lane actuator: age from the launch timestamp vs 2 ticks (900 s); progressing = lane-authored commit/file, sibling-only = `progressing-weak` (sibling named), else silent; step-1 citation sweep classifies every ledger report's hex tokens (commit/blob/dead/orphan/pin/runId-date/placeholder) across main + 6 child repos + external read-only trees | 135–141, 196 |

## Frozen baselines (the round's measurement)

    python3 .ufo/waves/round-12/closure-check.py --frozen pre         # exit 1, baseline: match
    python3 .ufo/waves/round-12/closure-check.py --frozen post-actual # exit 1, baseline: match
    python3 .ufo/waves/round-12/closure-check.py --frozen post        # exit 0, baseline: match

`pre` (22 entries, 20:55:00) → `debt=5` (protocol r11, kumitate r11, kotoba r12, aggregator r7, kasegi r14),
each row's `source` pinned from `scout-closure.md` / `reviewer.md` or marked checker-only. `post-actual` (the
pass's 30 entries, 21:20:00) → `debt=4` (the four stale `in-flight` rows, all resting on evidence *inside*
21:20:00: `complete` 21:14:05 / 21:14:11, report add-commits 21:11:33 / 21:13:01 / 21:15:59 / 21:18:11 — not
post-window leakage). `post` (= `pre` + `patch-entries.json` `appended` + `owed_appended`, 34 entries) →
`ok debt=0`. One timestamp rule in all three dirs (log lines ≤ `closed_at`; reports/prompts by add-commit ≤
`closed_at` else mtime, per-report `landed_at` carried; counters from the kept log): `frozen/README.md`,
each `CLOSED_AT.txt`.

## Observed runs

### (a) `python3 .ufo/waves/round-12/closure-check.py --selftest` → exit 0

```
closure-check: ok selftest passed=15/15 failed=0
  ambiguous-supersedes                   pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  bad-status                             pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  contradiction                          pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  failed                                 pass  exit=0 debt=0 contradictions=0 unrowed_terminated=0 pending_round=0
  in-flight-live                         pass  exit=0 debt=0 contradictions=0 unrowed_terminated=0 pending_round=0
  in-flight-terminated                   pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  keying-violation                       pass  exit=1 debt=1 contradictions=0 unrowed_terminated=0 pending_round=0
  lanes-list-duplicate                   pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  legacy-unadjudicable                   pass  exit=0 debt=0 contradictions=0 unrowed_terminated=0 pending_round=0
  marker                                 pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  not-dispatched-without-lane_rounds     pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  ok                                     pass  exit=0 debt=0 contradictions=0 unrowed_terminated=0 pending_round=0
  prompt-orphan                          pass  exit=1 debt=1 contradictions=0 unrowed_terminated=0 pending_round=0
  unknown-lane                           pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  unrowed                                pass  exit=0 debt=0 contradictions=0 unrowed_terminated=0 pending_round=1
selftest: 15/15 passed
```

### (b) live — `… --no-ledger --no-citations | sed -n '1,5p;/== Debt/,/== Live in-flight/p;/== Tallies/,/^$/p' | grep -vE '^    '` → exit 0 (21:4x, 36 entries)

```
closure-check: ok debt=0 contradictions=0 unrowed_terminated=0 pending_round=1
repo: /home/vgpnk/projects/shokunin  mode: live  manifest entries: 36  log lines: 221  dispatches: 95  completes: 79
keying: entry-keyed (a row names (lane, entry.round); lane_rounds annotates, never re-keys)

== Ledger (last-wins, entry-keyed): 104 status rows (table suppressed by --no-ledger; use --json for rows) ==
== Debt (exit-1 drivers): 0 ==
none

== Live in-flight (compliant: re-confirm next pass with the launch pointer) ==
== Tallies ==
entry-keyed, adjudicated (closure*) entries only: ok=75 failed=4 in-flight=7 not-dispatched=18 rows=104
entry-keyed, all entries incl. legacy fleet-keyed rows: ok=83 failed=4 in-flight=7 not-dispatched=18 rows=112
unadjudicable rows: 16 (entries #1, #3)
live missions: 8 (stale > 900 s: 6)
```

The live exit code is a moving target by construction. At 21:3x it was red: `closure-check: debt debt=4
contradictions=0 unrowed_terminated=0 pending_round=5` with `stale_in_flight` ×4 — aggregator r8 (#23),
kengaku r11 (#24), kumitate r12 (#25), kotoba r13 (#26), each printed with its launch pointer and
`suggested status: ok` (exactly the rows in `frozen/patch-entries.json` `owed_appended`). Main's 21:30
correction pass appended entries 30–35 closing precisely those four (`rounds[30]` aggregator r8 ok,
`[32]` kengaku r11 ok, `[33]` kumitate r12 ok, `[34]` kotoba r13 ok) — the gate's owed set was adopted
verbatim and the live verdict went green. `--show-keying` prints the naive `lane_rounds` tally beside the
authoritative entry-keyed one, and `--frozen pre` reproduces the round-11 record exactly (`73/4/4/23` over
104 rows). The citation sweep over the ledger's reports: `commit=338 pin=24 runId/date=21 dead=86 orphan=5
non-commit=0 placeholder=1` over 105 lane-rounds / 77 reports, including `round-14/kasegi.md:54 4028846`
dead, `round-12/kotoba.md:81 391a54f4` dead and `round-12/kotoba.md:224 LANE_HASH` placeholder.

### (c) `--json` on the fixture — `… --repo .ufo/waves/round-12/fixtures/closure-sample/marker --json --no-citations | python3 -c "import json,sys;print(json.dumps(json.load(sys.stdin),sort_keys=True))" | cut -c1-690` → exit 1

```json
{"after_closure": [], "citation_scope": "disabled", "citation_tally": {}, "citations": [], "contradictions": [{"class": "contradiction", "evidence": "ok row (entry #0) but .ufo/reports/round-1/kagi.md is a marker: 55 B, no commit hash, no SHONEN heading (P:150-155)", "key": "row", "kind": "ok-vs-marker", "lane": "kagi", "lane_round": 1, "suggested_status": null}], "counts": {"by_class": {"contradiction": 1}, "contradictions": 1, "debt": 1, "live_in_flight": 0, "pending_round": 0, "prompt_orphan": 0, "stale_in_flight": 0, "unrowed": 0, "unrowed_terminated": 0}, "debt": [{"class": "contradiction", "evidence": "ok row (entry #0) but .ufo/reports/round-1/kagi.md is a marker: 55 B, no c
```

## Mutation proof (MutationGate's mutants; harness under `mutants/`, base sha256 `9b89166c…`, 36 entries)

`m0` control `debt=0` → **7/7 determinate**: m2 `not-dispatched-without-lane_rounds`,
m3 `status-outside-vocabulary` (no traceback), m4 `lane_rounds-behind-counter` (`keying_violation` on the
superseded round-11 row — the row-identity trap; the keying check scans *every* adjudicated row, not just
last-wins, because a superseded row's annotation can still invent an identity), m5/m7 `ok-without-report`,
m6 `closure-correction-missing-supersedes` killed; m1 (failed→ok inside a legacy `work` entry)
not-applicable, with the `unadjudicable` rows named instead of a silent pass. `mutants/mutant-score.json`
holds the per-mutant new-kind evidence.

## Live debt found (exact rows, 2026-09-28 21:3x -03:00, 30 entries)

`stale_in_flight` ×4: aggregator r8 (#23), kengaku r11 (#24), kumitate r12 (#25), kotoba r13 (#26), each with
its launch pointer and `suggested status: ok`; `contradictions=0`, `unrowed_terminated=0`, `pending_round=5`
(aggregator r9, kasegi r15, kengaku r12, kumitate r13, kotoba r14 — informational); `unlanded_report_at_path`
empty (kagi r12's untracked draft is covered by the 21:06:05 `complete` line). The four owed corrections, with
evidence, are in `frozen/patch-entries.json` `owed_appended`; appending them makes `--frozen post` green.

## Gaps

- Live mode determines landedness with `git ls-files` now (no commit time): a live `ok` row accepts an uncommitted report as content, while `landed_at` governs termination only in frozen snapshots.
- Marker screen = 400-byte cutoff plus hash/`SHONEN` signals (record: markers 101–254 B, smallest real report
  4370 B); citations classify unresolved 7–11-hex tokens as `dead` and ≥12-hex as pins (a genuine 7-char
  sha-pin would be misreported, and `bounties/` is absent on this host so its hashes read as `dead`).
- `--frozen` matches the pinned triple set, not the evidence prose (a same-set baseline with different evidence would still match).