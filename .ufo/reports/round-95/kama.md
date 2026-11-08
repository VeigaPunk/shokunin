# kama — round 95 report

L1 `KamaR95` (attempt 1), lane repo `kama-shokunin`, base `2011161d5e5612fa953708cf54084b7f10ce99b1`,
**lane tip `65eca4ec210f088226713770a213387e38b84d49`** (`git ls-remote origin refs/heads/master` prints it;
`jj-lane.sh state` — ahead=0 behind=0 tracked=0 untracked=0).
Claims: **C1** operability, **C2** depth (lowest non-retired axis, 7), **C3** calibration — declared in
`plans/round-95-claims.md` (freeze `c798e831d6703428563a70789d1252dc39503d60`) and narrowed by
`plans/round-95-amendment-1.md` (C3), `-amendment-2.md` (C2/C3 after the wave) and `-amendment-3.md` (C1 after the
wave falsified its first revision).
Round shape: **one v1 wave, 12 seats** (2 reviewer, 2 critic, 1 mutation-tester, 1 sentinel, 2 scout, 2 executor,
1 connector, 1 scribe) — 7 attack seats (58 %), 1 connector; no residual call.

## Work performed

- **C1 (operability): the router file-state verdict is a function of the file's bytes.** The wall clock is gone from
  the per-file decision: `ROUTER_PY`'s shared 4 s call deadline (round 93) and its replacement 15 s per-file slice
  (round 94) are removed, and work is bounded by `MAX_STEPS` (4 000 000 read/seek steps, now one per string element)
  and `MAX_META` (512 MiB). The pass-level allowance is derived from the work a listing implies: `20 + 25 * npaths`
  seconds, where `npaths` comes from the `ROUTER_PY` `count` verb — not a constant, and not per entry.
  Evidence: `tools/kama-probe.sh` at `c810f51e` (`:561-576` constants, `:636-648` `need`, `:682-706`
  `skip_strings`, `:785-800` `path_count`, `:850-870` `router_file_states`).
  - Frozen counter `tools/round95-router-budget.py` (10 cells, natural + synthetic-CPU passes, byte-level fixture
    oracle that never consults a probe — round-94 SC02 F1 closed). Receipt `measured/c1-m1b.out`:
    `ROUTER_BUDGET95 cells=10 mismatches=0 positive_mismatches=0 load_cells=10 load_stable=1 budget=work probe=rev …
    w03_seconds=99.7 load1_nat=137.85`, exit 0.
  - Discriminators: `controls/c1-base.out` (round-94 probe, same counter: `mismatches=1`, W03 `MODEL_OK` at 60.20 s —
    the constant wrapper truncating forty distinct slow files) and `controls/c1-discriminator-guard.out` (the counter
    refuses to claim a discriminator it did not exercise: exit 2 at 8 files).
  - The wave's first-revision falsification and the repair are `plans/round-95-amendment-3.md`.
- **C2 (depth): the setter table decides per entry point and admits the carriers.** `SKILL.md` §Listen port and
  slot-count setters (round 95 revision) plus §Round 95 correction c1–c4: population 92 → 106 rows, the 14 new rows
  covering config.ini section scoping, the `common_params` whole-struct carrier at `tools/cli/cli-server.h:43`, and
  the `params_base.n_parallel` realisation reads; P15–P17 relabelled `other` → `cli`; `R18`/`R19` replaced by nine
  `R20`/`R21` rows, one per (parameter, entry) that owns a setter row. Evidence: M2 `beef8922`, correction
  `37820b5b`, registry citations re-pointed in `5fcca5b4`; receipt `measured/c2.out`
  (`population=106 rows=106 bound=106 unbound=0 missing=0 duplicates=0 fabricated=0 derived_disagree=0 entries=7
  decisions=9 decisions_bound=9 met=True`, exit 0).
- **C3 (calibration): the round audits its own claims statement.** `tools/round95-freeze-audit.py` grades named
  receipt paths, predicate token names against the counters' bytes, and cited `S###` ids at a revision. Evidence:
  `measured/c3-amended.out` (`receipts=9 present=9 missing=0 tokens=24 matching=24 cited=14 unresolved=0 met=True`,
  exit 0) and the red control `controls/c3-base.out` on the round-94 plan at its own freeze `285f1783`
  (`receipts=12 present=0 missing=12`, named counter absent, S604 unresolved, exit 1).
- **Frontier step.** `corpus/SOURCES.md` 355 → 357 rows: S616 (`tools/server/server-context.cpp` @ b12177, sha256
  `e0e43f22fd2357a1e76ad6b8996b099d62615dd973de33feaa02fa0ee1a2a973`) and S617 (`tools/server/server-schema.cpp`,
  sha256 `7f4d7c35a10d0deb6eef8a02a222a0ecf3295b7ec6c65b512e3f241b47df6b54`), both opened this round; one new
  rejection (`tools/cli/README.md:56` states `--parallel` default 1, falsified for the embedded server). Lesson
  `corpus/lessons/round-95.md` carries `## Gate` and `## Mistakes` (M1–M5).
- **Wave.** 12 seats, one v1 wave, dispatched through the `.ready` handoff at 02:33:45; all twelve settled and wrote
  reports under `.ufo/waves/round-95/w1/`, `WAVE-DONE` received at 03:27. Findings reconciled in amendments 2–4, the
  SKILL correction block c1–c4, the registry fix (`5fcca5b4`) and the claim-falsification ledger
  (`PREFILE-FALSIFICATION: pass claims=3 rows=10 attack_seats=7 findings=0`, exit 0).

## Landed changes

| Commit | Change | LOG entry |
|---|---|---|
| `c798e831` | freeze: plan, the three counters, `claims.json`, the seven freeze receipts, wave spec/dispatch | §Round 95 |
| `f6325660` | C1 first revision: clock removed from the router file-state decision; count-derived pass limit | §Round 95 |
| `beef8922` | C2+C3: round-95 setter section (106 rows, 9 decisions), S616/S617, `corpus/lessons/round-95.md` | §Round 95 |
| `719214fa` | amendment 1 (C3 narrowed) and the first measurement receipts | §Round 95 |
| `bba10f75` | amendment 1 carries the measured audit line | §Round 95 |
| `ca531563` | complete C1 receipt, C3 amended receipt, SCORECARD §Round 95, LOG entry | §Round 95 |
| `37820b5b` | SKILL §Round 95 correction c1–c4 (wave-1 RV02 findings) | §Round 95 |
| `7db1c54a` | amendment 2 (C2/C3 narrowed), harm pair receipt | §Round 95 |
| `c810f51e` | C1 repair: per-element step charging; pass allowance priced by model paths (RV01 BLOCKER-1/DEFECT-2/3) | §Round 95 |
| `ed3bd05f` | amendment 3 (C1 filed on the repaired revision), post-repair harm receipt | §Round 95 |
| `5fcca5b4` | registry citations R18 → R20 (server) (CN01 F4) | §Round 95 |
| `a9b5014c` | C1 measured at the repaired revision | §Round 95 |

## Before → after measurements

- **C1** — `python3 tools/round95-router-budget.py --repo . --rev <rev> --work <scratch>`
  - before (`a27656a4`, round-94 probe, `--allow-clock --skip-load`): `cells=10 mismatches=1
    positive_mismatches=1 load_cells=10 load_stable=1 budget=work`, exit 1 — `W03-slow-x40 ok=0
    want=MODEL_UNLOADED/router-model-invalid run1=MODEL_OK/router-unloaded-autoload/60.20s`
    (`controls/c1-base.out`).
  - after (`c810f51e`, M1b): `cells=10 mismatches=0 positive_mismatches=0 load_cells=10 load_stable=1 budget=work
    probe=rev … w03_seconds=99.7`, exit 0; W03 `MODEL_UNLOADED/router-model-invalid` at 99.66 s natural and
    179.25 s under the burners (`measured/c1-m1b.out`).
- **C2** — `python3 tools/round95-setter-sweep.py --repo . --rev <rev> --work <scratch>`
  - before (`2011161d`): `population=106 rows=0 bound=0 unbound=0 missing=106 duplicates=0 fabricated=0
    derived_checked=0 derived_disagree=0 entries=0 decisions=0 decisions_bound=0 met=False`, exit 1
    (`controls/c2-base.out`).
  - after (`beef8922`): `population=106 rows=106 bound=106 unbound=0 missing=0 duplicates=0 fabricated=0
    derived_checked=47 derived_disagree=0 entries=7 decisions=9 decisions_bound=9 met=True`, exit 0
    (`measured/c2.out`).
- **C3** — `python3 tools/round95-freeze-audit.py --repo . --rev <rev> --plan <plan>`
  - before (round-94 plan at its freeze `285f1783`): `receipts=12 present=0 missing=12 tokens=0 matching=0 cited=11
    unresolved=4 met=False`, exit 1 (`controls/c3-base.out`).
  - after (`plans/round-95-amendment-1.md` at `bba10f75`): `receipts=9 present=9 missing=0 tokens=24 matching=24
    cited=14 unresolved=0 met=True`, exit 0 (`measured/c3-amended.out`).

## Sources & frontier

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`:

- **before** (`controls/census-start.out`): 120 finding lines — all pre-existing W04 duplicate-URL warnings plus W01
  S481 — and the final line `kama	ok	…/corpus/SOURCES.md`; **exit 0**; rows **355**
  (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`).
- **after** (`measured/census-end.out`): same pre-existing warning set, final line `kama	ok`; **exit 0**; rows
  **357**.

| | before | after |
|---|---|---|
| rows | 355 | 357 |
| added by tier | — | A: 2 (S616, S617) |
| rows touched (status/recheck/used-by) | — | none |
| rejections recorded | — | `tools/cli/README.md` default-1 claim; archive-as-row (carried) |
| frontier advanced | — | a value set through a struct copy / a realisation read is now inside the governed surface |

Assimilation: none — no `merge/kama/` theme was taken this round (`considerthese/2026-11-07.md` unopened).

## Trend verdicts

- **expansion: unchanged** — no new `knowledge/` entry and no new surface; the two rows deepen an existing one
  (population 92 → 106 with a new entry-point dimension).
- **quality: improved** — a load-dependent verdict became byte-decided after the wave caught the first revision
  relocating the clock into the wrapper and reproduced a base-green/new-red regression, which was repaired and
  re-measured in-round (`c810f51e`, `measured/c1-m1b.out`); the harm pair is green at base and both tip revisions.
- **discernment: improved** — the wave falsified C1's first revision, C2's section prose (four statements, corrected
  in `SKILL.md` §Round 95 correction) and C3's own instrument (a dead status arm), and every finding was taken into
  an amendment, a correction or a routed defect rather than filed as a pass.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Decision
  table, §Router error signatures, §Checklist, §Listen port and slot-count setters (round 95 revision); author
  assertion, no named non-author verifier.
- [~] At least one end-to-end domain task executed and logged — `LOG.md` §Round 95; the wave ran a lane-owned
  b12177 router (SC02) and the ten-cell counter at both loads; author assertion.
- [~] Instructions executable by an agent without oral context — `plans/round-95-claims.md` predicates and the three
  counters' `--help`; all three counting commands ran from the plan text alone this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` §Write boundary; the connector seat's
  sibling scan was read-only and reported contested scope rather than absorbing it.

## Round facts

- Wave `w1`: 12 seats dispatched in one v1 wave; **12 reports, 0 dead seats**, `WAVE-DONE` received with
  `w1-results.json` (66825 B, 12 seats); roles: 2 reviewer, 2 critic, 1 mutation-tester, 1 sentinel, 2 scout,
  2 executor, 1 connector, 1 scribe.
- Verdicts by seat: RV01 falsified, RV02 falsified, CR01 falsified (five BLOCKERs), CR02 falsified (one BLOCKER),
  MT01 partial (7/12 mutants survive), SC01 falsified, SN01 **holds** against the filed revision `c810f51e`,
  EX01 falsified, EX02 holds (harm), CN01 holds, SB01 delivered the lesson draft, SC02 **falsified** (a live
  false green at 700 000 tensor headers — the `MAX_STEPS` ceiling bites at ~666 666 tensors, 333 334 below the
  `MAX_TENSORS` the plan's limit named — plus live confirmation that the 40-file false green is fixed on the tip).
- Wave cleanliness: the `SC02LiveRouter` seat's router children were gone at filing, but it left 64 CPU burners
  running from its scratch (`cwd /fast/scratch/hyaku/kama-r95/SC02LiveRouter`, PPID 1487, age 5 min); the L1 reaped
  all 64 (`pgrep -f 'while True: pass'` → 0) and records it as a seat-reaper defect.
- Round total: 12 seats, no residual call.
- `PREFILE-FALSIFICATION: pass claims=3 rows=10 attack_seats=7 findings=0` (exit 0,
  `python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane kama --round 95`; receipt
  `.ufo/waves/round-95/controls/prefile-gate.out`).
```
- Stale-lane: respawn-per-round driver; no other mission of this lane is open; mission started 02:06:53 -03:00 and
  completed 02:33:45 -03:00 (wave dispatched) with all seats settled by 03:27 -03:00; the lane is progressing, not
  silent.
- Tool installs: none (no `uv tool`, no `npx`, no pacman; the pacman pause is untouched).
