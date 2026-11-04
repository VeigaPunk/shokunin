# kumitate — round 88 report

Lane `kumitate-shokunin`, hyaku run 15, round 88 attempt 1 (no earlier attempt: watchdog shows only
`launch kumitate round=88 … attempt=1`). Base `7ac24afa477a44304a3b125e320ef86929218189`; final lane hash
`4f7d8ea9f5e314f7a76d8687a16b14ef752bdbe6` (`git ls-remote origin refs/heads/master` prints it).
Paths `open/`, `controls/`, `probe/`, `build/`, `w1/`, `close/` are under the lane's `.ufo/waves/round-88/`.

## Work performed

Declared claims (1): **C1 — operability (lowest non-retired axis), capability acquisition `receipt-bind`
v2** (contract `kumitate-receipt-bind-v2`). No second claim (every coverage sub-axis is saturated at 10;
a second operability claim would be the same claim). No exploratory claim. **Verdict: UNMET
(rejected-honest-stop) — the frozen kill rule fired.**

- Protocol load: MISSION/AXES, the round prompt §1–§7 and run-15 addenda, lane SCORECARD tail
  (round-88 pre-registration), `corpus/lessons/round-87.md`, `round-87-verifier-spotcheck.md`, skill://swarm.
- Round-87 spot-check routed defects: K87-V1 receipt `open/k87v1-bind-r87.txt` (`RECEIPT_BIND: CLEAN
  matched=12 … external=1` over the round-87 close dir at its M); K87-V2 the spot-check adopted inside the
  freeze commit (`open/spotcheck-adopt.txt`), `close/plan.txt` PASS for round 88; K87-V3/R86-D3 three source
  gates re-measured with receipts (`build/K88ExecCarry/`, all CLEAN); K87-V4 deterministic `sweep` arm
  (three runs diff-identical, `build/K88Review2/determinism-diff.txt`). R86-D2 stays open (not producible).
- Freeze `114877a308ffc0bcd63e354bcef03e6b9fe538d4`: `plan.md`, frozen 20-arm scorer `probe/probe88-c1.mjs`
  (three-body fixture repo: commit A, commit B, dirty worktree; four boundary arms with positive twins),
  `controls/make-worktree-variant.mjs`, `controls/refuse-all.mjs`, `controls/run-controls.sh`.
- Pre-data controls `8735f70f545c9a0355816d5ce86b30791ae7e6be` (17): do-nothing `base-v1` 16/20, its worktree
  twin 11/20, refuse-all 2/20, absent 0/20, round-87 controls/seat constructions 0–16/20 (`controls/*.txt`).
- L1 v2 instrument `0ff3562f15c18d0ca01dc6a76c9f827d30c26950`: `ESCAPES_LANE`, `SYMLINK_DIR`,
  `RECEIPT_TOO_LARGE`, `AMBIGUOUS_FIELD` (`scripts/receipt-bind.mjs`).
- Wave w1 (12 seats) → integration `7817d20093015866a419f865fd2e0085195873a9`: selftest 39 → 59
  (`build/K88ExecSelftest/`), SOURCES S252/S253/S254 + S218 used-by, knowledge section *v2* and
  *Round 88 verdict* (`corpus/knowledge/receipt-subject-binding.md`), QUALITY Q81, close runner v3
  (`run-close.mjs`, bind last with ALL/SHORT count), SKILL row/checklist text, lesson `corpus/lessons/round-88.md`.
- Close battery at M `close/*.txt` → final `4f7d8ea9…` with disposition and round-89 pre-registration.
- Kill-rule evidence: nine seat constructions at `C88_C1: HELD held=20/20`: `build/K88Critic/SCORES.md`
  (7: HEAD/index default-rev reads, fixture-gated boundaries, size-after-read, textual escape, loose limit,
  equal-duplicate acceptance, each with off-fixture discrimination `disc-*.txt`),
  `build/K88Connector/probe-ctl-abs-disk.txt` (absolute in-lane token read from worktree),
  `build/K88Review2/ctl-nogit-overfit.txt` (no git; A/B inferred from `.git/logs/HEAD` + probe constants).

## Landed changes

| commit (landed) | LOG.md entry | content |
|---|---|---|
| `114877a308ffc0bcd63e354bcef03e6b9fe538d4` | Round 88 (freeze) | plan, probe, control generators, spot-check adoption, K87-V1 receipt, start census |
| `8735f70f545c9a0355816d5ce86b30791ae7e6be` | Round 88 (controls) | 17 control receipts |
| `0ff3562f15c18d0ca01dc6a76c9f827d30c26950` | Round 88 | receipt-bind v2 |
| `8e4ea5f6503e4dccced9ffcfbf95c6882b7cc29b` | Round 88 | w1 spec + validated dispatch |
| `7817d20093015866a419f865fd2e0085195873a9` | Round 88 | integration (M) + wave artifacts |
| `4f7d8ea9f5e314f7a76d8687a16b14ef752bdbe6` | Round 88 — measured disposition | close battery, disposition, pre-registration, end census |

## Before → after measurements

**C1** — counting command: `node .ufo/waves/round-88/probe/probe88-c1.mjs --lane <LANE> --work <SCRATCH> --rev <REV> [--tool X]`.
Before (do-nothing control = instrument at freeze `114877a3`): `C88_C1: UNMET held=16/20` (`controls/base-v1.txt`).
After at M `7817d200`: `C88_C1: HELD held=20/20` exit 0 (`close/c1-probe.txt`); worktree twin at M 11/20
(`close/twin.txt`). Kill rule: nine seat-constructed controls also 20/20 → **UNMET**. Capability row not added.
Ancillary: selftest 39/39 → 59/59 (`close/bind-selftest.txt`); C2 222 → 224, `PROXY: MATCH --strict` (`close/proxy.txt`).

## Sources & frontier

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate`:
start exit 0 (`open/census-start.txt`), end exit 0 (`open/census-end.txt`), 7 pinned `W04` both times.
Rows 189 → 192 (`node scripts/sources-check.mjs` → `rows=192`): added tier A ×2 (S252 CWE-22, S253
gitrevisions — `mined`), tier B ×1 (S254 OWASP community path traversal — `rejected`, flip recorded).
Touched old→new: S218 used-by `…replay-output-isolation-link-following.md` → `+ corpus/knowledge/receipt-subject-binding.md`.
Captures pinned (`SOURCE_CAPTURE: CLEAN captures=81`). Sourced claim: C1's knowledge section cites S252,
S253, S218. Mined mistake: `corpus/lessons/round-88.md` `## Mistakes` (survivor recurrence, K87-V1
attribution, K87-V2 ordering). Assimilation: none (package not adopted; `considerthese/2026-10-26.md`
re-checked, no unimplemented proposal mined).

## Trend verdicts

- **expansion — unchanged.** Two admitted rows in a held band, no frontier area entered, no capability row.
- **quality — improved.** The instrument closes four sentinel fail-open boundaries with a 59-case selftest
  (each boundary's removal fails it: `build/K88ExecSelftest/selftest-mutant-*.txt`), v1/v2 agree on all 41
  historical close dirs (`build/K88Scout/walk/table.tsv`), K87-V1/V2/V3/V4 closed. Tempered: claim UNMET.
- **discernment — improved.** The round honoured its frozen kill rule against its own 20/20 predicate,
  recorded nine forgeries with off-fixture discrimination, and pre-registered the scorer fix rather than
  narrowing the rule (non-author confirmation pending closure).

## Round shape

ONE v1 wave `w1`, 12 seats (policy band 8–16, validated `counts.spawn=12`): executor 3, scribe 2, scout 1,
connector 1, reviewer 2, critic 1, mutation-tester 1, sentinel 1. Attack seats 4/12 = 33 % (+ sentinel).
No residual call; round total 12 + L1 (holds the §3 planner seat; planning data-walk on K88Scout). Dead
seats 0 (all 12 reports in `w1/`; `w1-results.json` notes the orchestrator kernel restarted mid-wave, outputs
null there, reports present). Disclosed defect: `ready-handoff` DRIFT `RELATIVE_WAVE_PATH` on K88ExecCarry's
item text (`close/ready.txt`). Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` → no
file written by this round's seats (only `.scratch/*`, another lane's report and a Nov-3 `after` file).
Scratch `/fast/scratch/hyaku/kumitate-r88` removed. Tool installs: none. Open L0 questions: none.
Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:646` receipt-bind row (v2), checklist item `SKILL.md:763`
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md "Round 88" + `close/*.txt` at `7817d200`
- [~] Instructions executable by an agent without oral context — `close/bind-selftest.txt`, `close/c1-probe.txt`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md untouched this round (`git diff 7ac24afa 4f7d8ea9 -- PROVINCE.md` empty)
