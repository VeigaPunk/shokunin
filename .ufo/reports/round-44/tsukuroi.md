# tsukuroi — round 44 report (hyaku run 9, attempt 1)

L1: `TsukuroiR44`. Lane repo `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin`, branch `master`. Base
`98020ece0674e0b569ee23aed10ffbee355b248e` (the `jj-lane.sh state` local at round start, which carries the round-43
spot-check). Final lane hash `e9ca7ef629810df61f7090eff2f3aa57de7925ae`; `jj-lane.sh commit` pushes on every landing, and
`git ls-remote origin refs/heads/master` is checked at the end. Wave evidence is in `.ufo/waves/round-44/` in the lane
(called `W/` below). No earlier attempt of this round existed, so nothing was inherited.

## Outcome

| Claim | Axis | Before (base) | After (`fbfef071`) | Verdict |
|---|---|---|---|---|
| C1: census scrub-record arm | coverage | FAIL (no SCRUB line) | PASS — cases 16/16, identity, wired, live, selftest 148/148, `selftest_r44` 16 | **PASS** |
| C2: SR7-SR9 entry | depth | FAIL (rows 0) | FAIL — every lexical and global gate passes (rows, quotes, props, host 3/3; sources 1; novelty 0; pointer 1), but `verdicts_ok 0` | **FAIL** |

Receipts are `W/after/c1-final-fbfef071.jsonl` and `W/after/c2-final-fbfef071.jsonl`, both made with
`tools/run-receipt.py`. The before receipts are in `W/before/`. The counters stayed frozen at commit `1d2afffe`:

- C1 counter: `tools/score-scrub-arm-r44.py`, sha256 `1409a5fd…6388`.
- C2 counter: `tools/check-scrub-record-r44.py`, sha256 `c96aeda9…8059`.

The C2 verdicts recorded for the six counted wave-2 seats (from `W/w2-results.json`):

| Row | Reviewer seat | Critic seat |
|---|---|---|
| SR7 | holds | holds |
| SR8 | partly | holds |
| SR9 | partly | holds |

C2 fails for two reasons:

- **No residual seat for the `partly` rows.** A residual wave needs at least 32 seats under the wave band, and I judged that out of budget, so SR8 and SR9 fail the predicate's `partly` rule.
- **Two outputs are unbound by design.** C2RevSR7 returned a JSON string rather than an object. C2CritSR9's JSON carried `verdict: supports` next to its holds line, which contradicts it. Controls K14-K16 were built to refuse exactly these shapes.

I applied the SR8 and SR9 narrowings after the counted reads:

- SR8's host reading now names the fsid instead of "the root filesystem".
- SR8's `memparse` suffix claim is marked [inference].
- SR9 now claims package ownership for the timer only.

No counted seat has judged the narrowed text, so C2 stays FAIL. The depth ordinal is unchanged at 8, and coverage
stays at 9.

## Work performed

- **Protocol load.** I loaded the shokunin and swarm skills, MISSION, AXES, PROTOCOL, the round-43 report and
  spot-check, considerthese 2026-10-26, and QUALITY 79-92. Claims were taken from items (1) and (2) of the round-43
  planned row. Item (3), the census readers, stays routed because it would share C1's surface.
- **Freeze `1d2afffe`.** It holds the declaration, both counters, and the pre-data controls; both batteries read
  `should_fail_accepted 0, control_accepted 1`.
  - C1 controls: K0-K6, K10-K13, with K7 recorded.
  - C2 controls: K0-K19. K17 caught a source-line defect in my own first counter draft before any seat ran.
  - The freeze also pins the sources S242, S243 and S244 with SHA256SUMS and FETCH.txt, and the own-work host capture S245.
- **Implementation (`ab8aae16` and `7e081698`).**
  - `probe_scrub_record` and nine `R44-C1` selftest cases.
  - The SR7-SR9 entry and SOURCES rows S242-S245.
  - The S237 and S240 used-by changes.
  - The r43 header pointer.
  - The repair of R43-SR1-LIMITS-CONTRADICTION (a correction appended to the r43 entry).
- **Wave 1 (46 seats).** Integration commits `071ab0d1`, `9608ebc3` and `8eee79db`:
  - Arm hardening: a sysfs root that is not a directory now reads `sysfs:not-directory`, and timer directories are excluded.
  - Seven more selftest cases, written from the C1MutSelftest survivors.
  - The SR7 replace path and its attach/clear window.
  - SR8 now states the limit is held in memory only.
- **Wave 2 (32 seats).** Integration `fbfef071`:
  - The narrowings listed under Outcome.
  - A selftest fixture that kills glob mutant g1, which survived both the counter and the selftest (C1MutFinal).
- **Documentation.** PROVINCE "Round-44 promotion — R44-SCRUB-VIEW", the corpus/README round-44 note, two SKILL
  sections, and the round44 registry table (70/70 rows at `3a1c6b5c` and later).
- **Scorecard, log and lesson.** SCORECARD "Round 44 — measured outcome" plus the round-44 axes and capabilities
  tables, LOG, and `corpus/lessons/round-44.md`.

## No-harm and checks

- **Kill rules did not fire.**
  - PLANE lines, the rollup and the exit code match between base and tip; the only differences were live PSI and memory readings that also vary between runs of one revision (w2/C1ExecFinalPlaneDiff).
  - The predecessor storage counters are unchanged (w2/C1ExecFinalPrior).
  - The live arm window made 29 syscalls, all read-only (w2/C1ExecFinalLiveRead).
- **Repository state.** Base to tip: 0 deleted files and SCORECARD append-only. The sources census exits 0
  (`W/after/sources-census-final.txt`).
- **Self-assessment.** `check-self-assessment` on the round-44 tables gave 27 checks and 1 mismatch (K17) before the
  capabilities table was appended. At the final tip `e9ca7ef6` it reads 27 checks, 0 mismatches, PASS.
- **Recorded defects, routed to round 45.**
  - Registry coverage was red at 68/70 from the declaration until `3a1c6b5c` (the round-27 class); it is repaired.
  - Adjacency anchor IN-109 was moved by the census insertions (w2/CritNoHarmFinal).
  - Live-leg evasion through script path and process ancestry: both channels pass the frozen C1 counter (w2/C1CritFinalEvasion).
  - C2 json last-wins duplicate keys, CR stripping and substring quote matching (w1/C2MutBinding, w1/C2RevCounter).
  - An orphaned w1 `grep` was left blocked on a fixture FIFO (w2/SentFinalScope F-1). It was not killed, because only the seat that started it may signal it.

## Incidents

- **Fleet-root misroot.** Seat C1ExecEdgeNames wrote `fx/A2-uppercase-fsid-sysfs/` into the fleet root at 21:08.
  The orchestrator quarantined it, I messaged the seat, and the seat disclosed it in its report.
- **Missing reports.** C1MutArm and SentMisroot settled without a report file. I reconstructed both reports from
  their transcripts' final texts, with the paths corrected.
- **Integration bugs I introduced.** My own integration twice broke the timers branch. The census selftest caught it
  both times (the timers case went red), and it was fixed before measurement.

## Tooling

No installs or updates by the L1. pacman was paused throughout.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources.
  - Round 44 adds the SCRUB-line observation → reading → action table and the SR7-SR9 rows table (`SKILL.md`
    "Scrub-record census arm — round 44", "Scrub record — round 44 rows"), plus the round44 registry table (70 rows).
  - Wave-2 `W/w2/SkillReview.md` reviewed them and supports; that seat is the lane, not a non-author.
- [~] At least one end-to-end domain task executed and logged in LOG.md.
  - `LOG.md` "Round 44": a read-only census arm was built, measured red-before at base and PASS at `fbfef071`, and
    reproduced independently in a private namespace (`W/w2/C1ExecHandReproFinal.md`).
  - Non-author replay is pending.
- [~] Instructions executable by an agent without oral context.
  - The round-44 sections carry paste-ready read-only commands and the counter invocations. Seat
    `W/w2/C1ExecHandReproFinal.md` derived the expected lines from the header contract text alone.
  - A whole-SKILL retest was not executed.
- [~] No cross-domain bleed (PROVINCE.md still accurate).
  - `W/w1/ConnSiblings.md` found no contested scope. The PROVINCE promotion covers only the unprivileged view;
    record content and running state stay Frontier.
  - Moved anchors: the census insertions move the lane's own anchor IN-109, which is unmarked
    (`W/w2/CritNoHarmFinal.md`) and routed to round 45. Sibling pins are inventoried in `W/w1/AdjPins.md`.
- No promotion is claimed. No box changed state this round.

## Next

The planned row for round 45 is drafted in w2/ConnFrontierFinal. It covers:

- the census readers (the `:777` foreign-baseline lookup and the single-line readers);
- the C2 counter parse gaps;
- a residual-capable verdict design.

Non-author closure of round 44 is pending.
