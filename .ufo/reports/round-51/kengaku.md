# kengaku — round 51 report (hyaku run 11, attempt 1)

Lane: `kengaku-shokunin` · L1 `KengakuR51` · 2026-10-28 · campaign target round 100

**Declared claims (1–3, frozen before data at `e07f131c`, `plans/round-51-claims.md`):**

1. **R51-C1 — freshness 8→9.** Every surface `PROVINCE.md` declares is machine-checked at the tip: a
   committed manifest (one entry per surface row) plus a counter that probes each target, requires a dated
   `ABSENT <ISO date>` verdict for every absent surface, compares every declared count to the count on disk,
   and refuses to let the resolved set fall below a recorded floor.
2. **R51-C2 — adjacency 8→9.** Every routed finding in `corpus/routed-findings.jsonl` names its owner lane
   and a disposition, carries a resolving source pointer and a non-empty check, re-runs every
   `fixed-verified` check, resolves every `fixed-historical` close reference, and gives every routed row a
   non-`kengaku` owner plus a `next`.

Both are causally separable: different files, different counters, neither reads the other's inputs
(`RevSeparability`, `MutCrossCounter`). The lowest non-retired axis is **coverage 7**, which is not claimed
because its own cap is open (`kengaku | round-25`, `kengaku | round-33` in `.ufo/l0-questions.md`); the round
works the next-lowest band (the 8s). No model probe was possible — `:34113` is absent and the only live
servers on this host belong to the serving plane this lane refuses (see R51-R1/R51-R4).

## Work performed

- **C1 instrument, frozen at `e07f131c`** — `plans/round51_surfaces.py` (manifest counter, 9-case selftest,
  stdlib only, honours `TMPDIR`) and `plans/round51-surfaces.json` (19 entries, one per PROVINCE table row,
  each with an anchor, the truthful probed `state`, the recorded reading of the row, a probe spec and an
  optional `count_claim`). Evidence: `plans/round51_surfaces.py`; `python3 plans/round51_surfaces.py --selftest`
  → `cases=9 failures=0`.
- **C2 instrument, frozen at `e07f131c`** — `plans/round51_routing.py` (owner/disposition/check-re-run/
  close-reference/routed-next legs, 11-case selftest). Evidence: `python3 plans/round51_routing.py --selftest`
  → `cases=11 failures=0`.
- **Before measurements at the base tip `297e1792`** — C1 `DRIFT 3`, `UNVERDICTED 1`, `NUMBER-DRIFT 1`,
  `present=13`, `PREDICATE fail`, exit 1 (`corpus/evidence/round51/c1-before.txt`); C2 `rows=71`,
  `FIELDS complete=0`, `OWNERS attributed=0`, `CHECKS present=61`, `PREDICATE fail`, exit 1
  (`corpus/evidence/round51/c2-before.txt`).
- **One v2 wave, 64 seats** (spec `4090c3db`): 20 executor, 11 critic, 10 scribe, 6 reviewer, 5
  mutation-tester, 4 scout, 4 connector, 2 revenger, 2 simplifier — 22 attack seats (34 %). Seat reports and
  fragments under `.ufo/waves/round-51/w1/`; dispatch `w1-dispatch.json`; `.ready` written before the wave and
  taken by the orchestrator (`w1.ready.dispatched`).
- **Surface probes landed as receipts** — `corpus/evidence/round51/surfaces/paths.txt` (three surfaces absent,
  no relocation found), `endpoints.txt` (`:34113` → 000; `:8791`, `:45669`, `:1234` → 200, with model identity,
  `/props` build `b1-39ebd2`, n_ctx 32768, slots 4, and both argv lines), `pins.txt` (all three PROVINCE digest
  pins match their files; 171 SOURCES rows; 12 evidence dirs; 28 root receipts; three selftests exit 0).
- **C1 repairs landed** — dated `ABSENT 2026-10-28` markers on the research-notes, benchmark-battery and
  served-model rows; a dated verdict on the route-telemetry row; the registry count corrected 25 → 171; a new
  surface row declaring the live LFM3 server pair as a capture-time identity pin (`PROVINCE.md` §Surfaces,
  `corpus/knowledge/served-endpoint-identity-pin.md`). Evidence: `PROVINCE.md`; `plans/round51-surfaces.json`.
- **C2 attribution landed** — all 71 base rows plus four new cross-domain rows carry `owner`, `disposition`
  and (where routed) `next`; 41 `fixed-verified`, 28 `accepted-risk`, 4 `routed`, 2 `refused-out-of-scope`
  (`corpus/routed-findings.jsonl`; merge script `.ufo/waves/round-51/integrate_ledger.py`; per-row seat
  fragments `w1/C2Exec{A..H}.jsonl`). New rows: R51-R1/R51-R4 → `kama`, R51-R2 → `protocol`, R51-R3 →
  `unowned:integrator`.
- **Frontier step** — S178 admitted (llama.cpp server API reference @ `b7200`, `ab49f094`; quote at `:1163`);
  the Hugging Face revision-pinning page rejected (HTTP 404, no locatable anchor); census 170 → 171 rows,
  `malformed=0`, exit 0 (`corpus/SOURCES.md`, `corpus/lessons/round-51.md` §Gate).
- **Wave findings that changed the instrument before the after-run** — `C2ExecG`, `C2ExecH`, `C2MutLedger` and
  `CritSurvivor` measured that the frozen C2 counter ran checks from a scratch cwd while 61/61 ledger checks
  are lane-relative (6 pass vs 43 pass), that its owner regex matched 0 lines of `shokunin.conf` and rejected
  seven real lane directories, and that `--ledger` crashed on a relative path; amendment A1 records the four
  fixes. `C1CritDeclareAllAbsent` proved control 1 fails on `STALE 13`, not on the resolve floor;
  `CritProseRead` ruled 18/19 readings right and SF01 wrong (below); `C2MutLedger` named five frozen-predicate
  survivors and killed all seven of its named mutations.
- **Inherited state resolved** — round 50's closure defects D1/D3 (uncommitted wave outputs) are committed
  here as `2cec536a`: `.ufo/waves/round-50/w1.ready`, `w1.ready.partial` and `w1/` (193 files). No other
  lane-authored leftover existed at round start; `plans/round50_c1_verify.py` was already committed at the
  round-50 tip.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| stage-1 freeze: claims, both counters, manifest, before receipts | `## Round 51` | `e07f131cf7037e58a21db6e1f3986cf401ad257c` |
| v2 wave spec + validated dispatch payload (64 seats) | `## Round 51` | `4090c3db79d11279ab5e5121ba25e74aa316e6e7` |
| inherited round-50 wave evidence (closure D1/D3) | `## Round 51` | `2cec536a692b3586d107f6cd255fbb7ab1d38cc8` |
| C1 + C2 landing: PROVINCE dated verdicts, successor surface row, manifest states, ledger attribution, knowledge entry, lesson, S178, SCORECARD, LOG, README index, wave evidence | `## Round 51` | `11e79380d33d6e811f0010f2a2a0c22a3cdc359e` |
| after receipts + measured-revision lines in SCORECARD/LOG | `## Round 51` | `7864296ee02a95ee1c23e9697966fcda4054f802` |
| final seat reports (5 seats that wrote after the landing commit) | `## Round 51` | `dbf0be6c01215f4940fe2655685f4a0528ab5a56` |

Lane branch tip at filing: `dbf0be6c01215f4940fe2655685f4a0528ab5a56` (`git -C kengaku-shokunin ls-remote origin refs/heads/master` prints it; `jj-lane.sh state` → `ahead=0 behind=0`).

## Before → after measurements

**R51-C1** — counting command `python3 plans/round51_surfaces.py --lane .`

- before, measured at base tip `297e1792` (`corpus/evidence/round51/c1-before.txt`):
  `ANCHORS 19/19`, `ROWS 9+10 uncovered=0`, `PROBES present=13 absent=6`, `DRIFT 3`, `STALE 0`,
  `UNVERDICTED 1`, `NUMBER-DRIFT 1`, `RESOLVE present=13 floor=13 verdict=met`, `PREDICATE R51-C1 fail`, exit 1.
- after, measured in a clean clone of `11e79380` (`git status --porcelain` → 0 lines;
  `corpus/evidence/round51/c1-after.txt`): `ANCHORS 20/20`, `ROWS 10+10 uncovered=0`, `PROBES present=14
  absent=6`, `DRIFT 0`, `STALE 0`, `UNVERDICTED 0`, `NUMBER-DRIFT 0`, `RESOLVE present=14 floor=13
  verdict=met`, `PREDICATE R51-C1 pass`, exit 0.

**R51-C2** — counting command `python3 plans/round51_routing.py --lane . --run-checks`

- before, measured at base tip `297e1792` (`corpus/evidence/round51/c2-before.txt`): `rows=71`,
  `FIELDS complete=0 incomplete=71`, `OWNERS attributed=0 unattributed=71`, `DISPOSITIONS set=0 bad=71`,
  `CHECKS present=61 absent=10`, `VERIFIED ran=0`, `PREDICATE R51-C2 fail`, exit 1.
- after, measured in a clean clone of `11e79380` (`corpus/evidence/round51/c2-after.txt`): `rows=75`,
  `FIELDS complete=75`, `OWNERS attributed=75 unattributed=0`, `DISPOSITIONS set=75 bad=0`,
  `SOURCES resolved=75 missing=0`, `CHECKS present=75 absent=0`, `VERIFIED ran=41 passed=41 failed=0`,
  `CLOSE_REFS resolved=0 missing=0`, `NEXT violations=0`, `PREDICATE R51-C2 pass`, exit 0.

Controls (all fail the predicate, receipts in `corpus/evidence/round51/`): C1 `declare-all-absent`
(`STALE 13` — **not** the resolve floor; the floor counts probes, a correction recorded in
`corpus/lessons/round-51.md`), `drop-one-entry` (`UNCOVERED 1`), `stale-pin` (`STALE 1`), `undated-absence`
(`UNVERDICTED 1`), do-nothing (base tip, exit 1). C2: seven named mutations all killed by `C2MutLedger`
(m1 FIELDS+OWNER, m2 OWNER, m3 CHECK_FAILED, m4 CHECK, m5 NEXT on the real routed row, m6 SOURCE,
m7 CLOSE_REF), plus `CritClaimSizing`'s cheapest skip-the-work control.

Corrections and disclosed limits (append-only; nothing was narrowed after data):

- **SF01 reading disagreement.** `CritProseRead` rules 18/19 `prose` readings right and SF01 (the
  research-notes row) wrong: that row already carried an `ABSENT 2026-10-20` marker, so a stricter reading is
  `absent`, which would make the base-tip `DRIFT` 2 rather than 3. The frozen reading stands (a reading
  changed after data is not the claim's rule); the after-state is unaffected because both readings agree once
  the row is dated.
- **`DRIFT` is self-consistency** (two manifest fields), not truth; the external check is the reading audit.
- **Frozen-predicate survivors** (`C2MutLedger`): duplicate `id`, row deletion, `check: "true"` as proof of a
  fix, `fixed-verified` on an open row, a `source` naming a directory. Recorded in amendment A2; the landed
  ledger contains none of them (asserted: 75 unique ids, base id set ⊆ merged id set, no tautology check, no
  `fixed-verified` on a non-closed row, no directory source, no empty check).
- **Instrument amendment A1** (cwd, timeout, owner universe, `--ledger`) changed no predicate leg.
- **Ledger amendment A2**: the after-target's literal `rows=71` is reconciled to 75 (71 base + R51-R1..R4);
  no row was deleted.

## Sources & frontier

`SOURCES: 170 → 171 rows` — counting command
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`
→ exit 0 both times; `malformed=0` (`awk -F'|' '/^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|/ && NF!=13' corpus/SOURCES.md`).
Round-start census (run at stage-2 start, disclosed): 170 rows, tier A=146/B=22/C=2, status
mined=154/queued=8/rejected=8. Round end: 171 rows, tier A=147/B=22/C=2, status mined=155/queued=8/rejected=8.

- Rows added by tier: **A +1** (S178), B +0, C +0.
- Rows touched old→new: none (no `status`/`recheck`/`used-by` change to an existing row this round).
- Frontier rows advanced: none from `corpus/README.md` §Frontier (the round's sourced ground is instrument
  ground, not a frontier item); the admitted row is cited by
  `corpus/knowledge/served-endpoint-identity-pin.md`, which is the round's sourced claim basis (C1's successor
  surface row rests on S178).
- **Assimilation: none** — the staged `merge/kengaku/` package was not adopted this round; the round's one
  theme (surface truth) is not in that package, and no one-theme 1–3-entry subset was selected.
  `considerthese/` was not mined this round (no still-unimplemented proposal matched the claims).
- Gate: one admit (S178, quote at `:1163`, 20 words), one reject (Hugging Face revision page, 404, flip
  condition recorded) in `corpus/lessons/round-51.md` §Gate; spot-check of the admitted row by the L1
  (re-opened at the pinned tag, sha256 `fb4ab6f2…` identical); the non-author spot-check is the verifier's.

## Trend verdicts

- **expansion — improved.** One new tier-A source row opened with a located quote and a knowledge entry
  admitted on ground the coverage map did not hold (served-endpoint identity pinning), plus a new declared
  surface that resolves. Evidence: `corpus/SOURCES.md` S178, `corpus/knowledge/served-endpoint-identity-pin.md`,
  census 170→171 exit 0.
- **quality — improved.** Two counters landed and both pass at the tip with before-states that fail;
  four control receipts fail the predicate; the wave found four instrument defects and one control-expectation
  error before the scored run, all recorded as amendments rather than patched silently.
  Evidence: `corpus/evidence/round51/c1-after.txt`, `c2-after.txt`, `plans/round-51-claims.md` A1/A2.
- **discernment — improved.** The round's own gate re-opened its sources, rejected one candidate on a measured
  404, and recorded a disagreement between its recorded reading and an independent critic (SF01) instead of
  smoothing it; five predicate survivors are named rather than hidden. Evidence: `corpus/lessons/round-51.md`
  §Gate/§Mistakes; `CritProseRead`, `C2MutLedger` seat reports.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md unchanged
  this round; the round's actionable table landed in `corpus/knowledge/served-endpoint-identity-pin.md`
  (pin table + decision rules) instead.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 51`; the executed
  task is the surface re-verification + ledger attribution, with receipts.
- [~] Instructions executable by an agent without oral context — `plans/round-51-claims.md` §C1/§C2 carry the
  counting command, predicate, controls and kill rules; `python3 plans/round51_surfaces.py --selftest` and
  `--selftest` on the routing counter run without context.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` corrected this round; the serving
  plane stays kama's and the fleet-ledger schema is routed to protocol (R51-R1/R51-R2/R51-R4).

**Stale-lane:** none — respawn-per-round driver; no other mission of this lane is open.

**Tool installs:** none this round (no `uv`/`npx`/binary install; no pacman transaction attempted).

**Wave accounting:** one v2 wave, 64 seats specified, 64 mounted, 64 settled (`WAVE-DONE w1`, results
`.ufo/waves/round-51/w1-results.json`: 64 entries, all with output, **0 dead seats**), 22 attack seats (34 %:
11 critic, 5 mutation-tester, 6 reviewer). Role mix: 20 executor, 11 critic, 10 scribe, 6 reviewer, 5
mutation-tester, 4 scout, 4 connector, 2 revenger, 2 simplifier. 65 report files landed under
`.ufo/waves/round-51/w1/` (every seat name covered) plus 8 ledger fragments `C2Exec{A..H}.jsonl`; the spec,
the validated dispatch payload and the `.ready` handoff are committed in the same wave dir. Round total:
64 seats — one wave, no residual call. The planner seat is the L1's own (the validator refuses a `planner`
swarm lane); the bounded planning data-walk rode the scout/connector items `C1ScoutSurfaces`,
`C1ScoutSiblings`, `C2ConnLedgerSchema`.

**Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` at filing shows `.scratch/*`
(orchestrator-owned), this report, and four strays that predate the round and name no kengaku/round-51
content (`o.bin`, `oldrep1.out`, `oldrep2.out`, `lane3/`) — another lane's, not touched. No kengaku seat wrote
into the fleet root; no misroot this round.
