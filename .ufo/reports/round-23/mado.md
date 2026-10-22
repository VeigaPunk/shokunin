# mado — round 23 report (attempt 1, repair-first recovery)

Lane: mado-shokunin. Pushed lane hash: `fa819d561d613cf3cfd8f58ed763e1ca57ab5eb4` (helper `landed`). Registration `.ufo/waves/round-23/registration.md` landed at `6b383c46` before any production edit.

## Work performed

Declared claims: **C1 operability** (repair of routed harms: frozen 12-case tripwire repair set 6/12 → 12/12 with no-harm guards), **C2 coverage** (learning, sourced: foot, kitty, ghostty config trees 0/3 → 3/3 sourced routes), **C3 calibration** (lowest scored axis: SHONEN box 4 "PROVINCE.md still accurate" versus tracked lane tools without a PROVINCE row, 5 → 0, counter v2).

- Routed harms named with before values and commands (registration H-table): H1 r21 F1–F5 (57/57 at base, `round-22/oracle/measure.py`); H2 precision 172→166/175 (`round-20/tw-precision.py REV`, not repaired, reason in registration clarification 2); H3 r22 supplemental 2/4 (`round-22/residual-truth/measure.py`); H4 caller-frame leak and H5 callback-store recall (repair-set cases). Repair set truth is mechanical: `repair/truth.py` 12/12 (`evidence/repair-truth.json`).
- Routed round-22 defects: expectations committed before production (`6b383c46` precedes every `tools/` change); census pasted byte-exact below; executors in separate clones; guards sequential.
- C1: wave-1 candidate ExecFullB landed at `2e592aff` (12/12, all guards green, `evidence/guards-candidateB-scratch.json`). Wave-2 critics found regressions against base outside every guard (AttackEscapeGate 1, AttackRecallRegress 13 of 45, AttackFrameScopes 11 of 41 + 4). L1 repaired them at `03227ddf` (classifier `e1dc8029`): 12/12, guards green (`evidence/guards-fix5-scratch.json`), zero regressions on those fixtures (`evidence/attacks-fix5.txt`; seat addenda). Later reports still showed regressions (AttackLateCell relay case at `3732c7a7`; ReClosureNeighbour 7 stored-callable rebind shapes at `2f1134f3`). One more fix broke the repair set (11/12) and was discarded. **Production classifier restored to base bytes `cd9da20c` at `3df10626`; candidate kept at `evidence/candidate-classifier-e1dc8029.py`. C1 is an honest stop.**
- C2: note `corpus/knowledge/terminal-trees-r23.md` (`c8cb3930`, errata `3732c7a7`, `3df10626`), SOURCES S123–S152 (29 mined, S132 queued), SKILL.md decision table, README frontier entry. All 30 rows re-opened in wave 2 (ReopenFoot 11/11, ReopenKitty 11/11, ReopenGhostty 8/8; wording defects recorded as errata). CritC2Gaming: honest 3/3.
- C3: PROVINCE five-row tool table (`2f1134f3`) plus append-only correction (`3732c7a7`) for mado-verify.sh live reads, redaction scope, mori/tsukuroi overlaps and the tools/-only inventory scope.
- Counters tightened before after-measurement after CritRegistration (`4de44647`).

## Landed changes

| Commit | Change | LOG entry |
|---|---|---|
| `6b383c46`, `a28e4815`, `4de44647` | registration, repair set, counters, before receipts | LOG "round 23: repair-first recovery" |
| `2e592aff`, `03227ddf` | C1 candidate and repair (later withdrawn) | same, and "C1 withdrawn" |
| `c8cb3930` | C2 note + SOURCES S123–S152 | same |
| `2f1134f3`, `3732c7a7` | C3 PROVINCE table and correction; note errata | same |
| `3df10626` | classifier back to base bytes, lesson, LOG, SCORECARD, SKILL, README, wave evidence | "C1 withdrawn" |
| `fa819d56` | large raw wave receipts | — |

## Before → after measurements

| Claim | Before (e33ea304) | After (fa819d56 tip; same bytes as 3df10626) | Command |
|---|---|---|---|
| C1 | 6/12 | **6/12 — target 12/12 not met** (12/12 was reached at `2e592aff` and `03227ddf`, withdrawn for regressions) | `python3 -I .ufo/waves/round-23/repair/measure.py --tool <git show REV:tools/mado-tripwire.py>` |
| C2 | 0/3 | **3/3** | `python3 -I .ufo/waves/round-23/c2/count.py REV` |
| C3 | 5 (v2) | **0** | `python3 -I .ufo/waves/round-23/c3/count.py REV` |

## Sources & frontier

SOURCES rows 122 → 152 (+30, all tier A; 29 mined, 1 queued; 0 rejected added). Rows touched old→new: none. Frontier: foot, kitty, ghostty trees moved onto documentary sourced ground (README round-23 entry). Count: `grep -c '^| S[0-9]' corpus/SOURCES.md`.

Start census (exact, `evidence/sources-start.txt`):
```
mado	W04	S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado	W04	S042 duplicate url wayland.freedesktop.org/extras.html across scopes
mado	W04	S045 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado	W04	S097 duplicate url raw.githubusercontent.com/basecamp/omarchy/v3.8.4/themes/matte-black/colors.toml across scopes
mado	W04	S119 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Lib/imaplib.py across scopes
mado	W04	S120 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado	W04	S121 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado	ok	/home/vgpnk/Projects/shokunin/mado-shokunin/corpus/SOURCES.md
census rc=0
```
End census (exact, `evidence/sources-end.txt`):
```
mado	W04	S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado	W04	S042 duplicate url wayland.freedesktop.org/extras.html across scopes
mado	W04	S045 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado	W04	S097 duplicate url raw.githubusercontent.com/basecamp/omarchy/v3.8.4/themes/matte-black/colors.toml across scopes
mado	W04	S119 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Lib/imaplib.py across scopes
mado	W04	S120 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado	W04	S121 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado	ok	/home/vgpnk/Projects/shokunin/mado-shokunin/corpus/SOURCES.md
census rc=0
```

Mistakes mined: `corpus/lessons/round-23.md` M23-1…M23-7 (census paste omission, expectation order, residual defects, guard-blind regressions, stale result files, gameable counters, withdrawn C1).

## Trend verdicts

- expansion: **improved** — 30 opened sources, new knowledge on three unsourced trees (C2).
- quality: **unchanged** — production classifier equals base; C1 not delivered; PROVINCE accuracy improved (C3).
- discernment: **improved** — wave-2 base-versus-tip attacks caught guard-blind regressions and the lane withdrew the trade instead of landing it.

## SHONEN

- [~] SKILL.md decision tables/error patterns/cited sources — new terminal table, `SKILL.md:121-127`.
- [~] End-to-end domain task logged — unchanged.
- [~] Instructions executable without oral context — unchanged.
- [~] No cross-domain bleed (PROVINCE accurate) — PROVINCE table + correction, `evidence/c3-after-3732c7a7.json`.

## Swarm, seats, extras

Shape: default two v1 waves. Wave 1: 36 seats (executor 5, reviewer 13, critic 5, mutation-tester 2, scribe 6, scout 4, connector 1). Wave 2: 33 seats (reviewer 21, critic 8, mutation-tester 2, scribe 1, scout 1). Round total 69; no residual call; five idle wave-2 attackers were resumed to re-run on the repaired tool. L1 held the planner seat. Dead seats: 0. Cancelled by L1 at wrap-up (budget): 14 (ExecFrameEnv, ScribeRejectSweep, ReResidual, ReCorpus, ReResource, ReEscapeNeighbour, MutHunks, ReviewDiff, ReviewPresent, AttackPerf, ReviewNoteClaims, ReviewProvinceTruth, ReviewHarmTable, ScribeLessonCheck). Seat dispatch added the tool-required `solutionSpace` field to each validated task. Misroot sweep (ScoutMisroot): none from this round. Stale-lane: respawn-per-round driver; no other mado mission open. Tool installs/updates: none. Open L0: "mado | round-23 | …" (H2 precision versus repair-first ruling).
