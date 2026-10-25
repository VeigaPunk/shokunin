# KengakuGateRerun

Seat: gate rerun only. Read-only against `/home/vgpnk/Projects/shokunin/kengaku-shokunin`. No lane file edited. No commit. No live/session mode. Safe set from the wave contract: `python3 grader.py` and `python3 grader.py --selftest`.

Compared to the lane lesson, not to the lesson's own arithmetic. Lesson file: `corpus/lessons/round-16-recensus.md` (lines 8–10). SCORECARD move-log row 16 does not restate a scalar; it defers to that lesson.

## Run context

- When: `2026-10-14T21:17:41-03:00` (host `date -Iseconds` immediately after both gates returned).
- cwd: `/home/vgpnk/Projects/shokunin/kengaku-shokunin`
- `git rev-parse HEAD`: `7153e671b1581a4b705583656883b6af158257df`
- `git log -1 --format=%s`: `round-16: OMP-era freshness re-census (measured gates; records + scoped repair)`
- Commit time: `2026-10-14 21:15:36 -0300`
- That HEAD is the wave's named lane-identity commit. `git merge-base --is-ancestor` of that hash against HEAD exited 0 (it is HEAD).
- Tracked gate inputs were clean: `git status --porcelain -- grader.py corpus/evidence LOG.md SCORECARD.md corpus/lessons/round-16-recensus.md SKILL.md PROVINCE.md` printed nothing.
- Worktree noise not read by these argv: `?? plans/`.
- Interpreter: `/usr/bin/python3`, `Python 3.14.7`. Lesson does not pin an interpreter. Not a claimed-number mismatch.
- `grader.py` sha256 `90c87c8865022681b1249a42ea580726932d2e97ec0de43e0c89efe0e5ae941f`, 5737 lines. Lesson does not pin this hash. Not a claimed-number mismatch.
- Selftest temp prefix `kengaku-grader-selftest-` under `/tmp`: no residue after the run (`ls -d` found none).

## Claim-by-claim

| Claim (lane record) | Observed | Label |
|---|---|---|
| Lesson L8–9: `python3 grader.py` → exit 0, ``CHECKS n=733 mismatches=0 errata_pinned=1``, ``VERDICT: PASS — stored evidence fully re-derives offline`` | exit 0; stdout is exactly those two lines; stderr empty | agree |
| Lesson L10: `python3 grader.py --selftest` → exit 0, ``[selftest] ALL PASS`` (S0–S7) | exit 0; last stdout line is exactly `[selftest] ALL PASS`; stderr empty; S0–S7 each printed `PASS` on the eight lines above | agree |
| SCORECARD move-log row 16: freshness, "measured at HEAD (see lesson)" / "verdicts recorded per gate, no scalar" / evidence `corpus/lessons/round-16-recensus.md` | Row asserts no scalar of its own. The lesson it defers to still matches this rerun. | agree (deferred verdicts); no scalar in the row to disagree with |

No mismatch between the lesson's gate numbers and this rerun.

The "(S0–S7)" in the lesson sits outside the backticked last-line quote. It is a gloss, not a claim that the program prints that parenthetical. The gloss is true of the scenario lines, not of the last line. Not recorded as a mismatch.

## Commands

### 1. `python3 grader.py`

- argv: `python3` `grader.py`
- cwd: `/home/vgpnk/Projects/shokunin/kengaku-shokunin`
- exit: `0`
- stderr: empty (0 bytes)
- stdout (complete; last line is the verdict line):

```
CHECKS n=733 mismatches=0 errata_pinned=1
VERDICT: PASS — stored evidence fully re-derives offline
```

- last line: `VERDICT: PASS — stored evidence fully re-derives offline`
- stdout sha256: `279121d07b1f3a62408a162277341dd3a38e3c5c678ed97b8ad61aaf0a0be044`
- em dash in the verdict line is UTF-8 `e2 80 94` (U+2014), matching the lesson's em dash, not a hyphen.

### 2. `python3 grader.py --selftest`

- argv: `python3` `grader.py` `--selftest`
- cwd: `/home/vgpnk/Projects/shokunin/kengaku-shokunin`
- exit: `0`
- stderr: empty (0 bytes)
- stdout (complete; last line is the verdict line):

```
[selftest] PASS S0 control (clean copies): exit 0, expected 0
[selftest] PASS S1 stored-ok flip (record layer): exit 1, expected 1 + check-id r8.replay.A-INC.ok (flip applied: True, id fired: True)
[selftest] PASS S2 run.log SUMMARY edit (summary layer): exit 1, expected 1 + check-id r8.summary.A-INC (id fired: True)
[selftest] PASS S3 raw-digit bump (re-parse layer): exit 1, expected 1 + check-id r9.replay.A-MONO.got (mutation applied: True, id fired: True)
[selftest] PASS S4 r11 stored-ok flip (record layer): exit 1, expected 1 + check-id r11.replay.A-CKPT4710.ok (flip applied: True, id fired: True)
[selftest] PASS S5 r11 run.log SUMMARY edit (summary layer): exit 1, expected 1 + check-id r11.summary.A-CKPT4710 (id fired: True)
[selftest] PASS S6 stats anchors (betai/t_crit known values): all known-value assertions hold
[selftest] PASS S7 r12 stats anchors (Page L / grade_seq / Brier-BSS / Newton): all known-value assertions hold
[selftest] ALL PASS
```

- last line: `[selftest] ALL PASS`
- stdout sha256: `ad3ee3fa0097429e8b5dc30a3edca12abc4c1427adb39d3e1ee79c848d9e9fc3`

## Counterexamples

None. Both gates exited 0. `n=733`, `mismatches=0`, `errata_pinned=1`, and the PASS verdict line match the lesson byte-for-byte on the quoted strings. Selftest did not print `FAILURES PRESENT`. No scenario in S0–S7 failed.

Not run, and not a counterexample: `python3 grader.py --selftest-r12` exists in `grader.py` and is outside the safe set named for this seat.

## Named debt

Gate debt from this rerun: none. No red gate. No owner/unblock owed by a failed safe command.

Lesson-named host-surface debt (lesson lines 21–29) was not re-measured here. It is outside the safe gate set. This seat neither confirms nor clears it. Owners named in that lesson, not re-derived: serving-plane identity routed to kama; the absent paths (`~/Projects/webzites/repos/llm-wiki`, `~/archive/bench-arena`, `~/bench-arena`, `~/.bailian`, `:34113` / pid 1299 / `qwen-coder.service`) are operator-side absences the lesson says not to re-pin. Unblock, as the lesson states it: operator restores or retires those surfaces. Not a gate finding.
