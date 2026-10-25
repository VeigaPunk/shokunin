# round-1 — mori · fleet & host observability census (probation round 1)

Lane: `mori-shokunin`. Round 1. Axis-move: `coverage` + `operability`. Round-work
commit: `7ca17b1` (lane identity `mori-shokunin <mori@shokunin.local>`). Wave:
`Shokunin12hP4MoriR1` (32 members). Sole L1: Sol 6.1.

## Work performed

- 32-lane wave: six surface censuses, gate and fixture designs, the finding-id
  contract, corpus map, boundary/refusal and secrecy audits. Reports:
  `.ufo/waves/shokunin12h-20261014-p4-mori-r1/members/`.
- Parent landed the designed gate, repaired three fixture defects the design
  shipped red, ran the selftest and the live census, and wrote the corpus receipt.

## Landed changes

- `tools/mori-census.sh` — read-only census gate (six surfaces, stable finding ids,
  `--selftest` over hermetic temp fixtures, write fence asserted after every case).
- `corpus/knowledge/observability-census-r1.md`, `corpus/README.md`,
  `SCORECARD.md`, `LOG.md`.

## Before → after measurements

| Command | Before | After |
|---|---|---|
| `bash tools/mori-census.sh --selftest` | gate absent (`UNAVAILABLE (gate_absent)`) | `MORI_CENSUS_SELFTEST: PASS (14 cases, 14 passed, 0 failed)` exit 0 |
| `bash tools/mori-census.sh` (live) | not runnable | `MORI_CENSUS: DRIFT (findings=10 drift=9 unavailable=0 surfaces=7)` exit 1 |

Live findings include `OOM_KILL_JOURNAL count=1`, `CGROUP_OOM_KILL oom_kill=1`,
`WATCHDOG_ABSENT`, `WATCHDOG_STALE age_s=103830`, five `WAVE_UNSETTLED_AGE`
(oldest ≈26.5 h). A red census is the finding, not a failure.

## SHONEN

- [~] SKILL craft — decision table, error patterns, checklist present; registry row landed with the gate.
- [~] End-to-end task — the live census ran against the real host and produced a dated receipt.
- [~] No-oral-context — the gate's `--help`, ids and semantics are in `SKILL.md` + the note.
- [~] PROVINCE accurate — refuses dispatch (kumitate) and OS state (tsukuroi); enforced in the gate.

No `[x]`: no named non-author verifier has signed these boxes.

## Carried debt

Per-surface notes still owed; `progressing-weak` authorship proof deferred; disk and
memory thresholds are proposals with no evidence yet.
