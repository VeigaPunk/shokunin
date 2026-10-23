# mori — round 31 report (attempt 1, L1 MoriR31)

Lane repo `/home/vgpnk/Projects/shokunin/mori-shokunin`, entering tip `a12c68ae81257fb6f918bb165bcb39c73f82d212`, landed
tip `52435f2f425c2b4a5e7ba63d7abc1292b8736367` (pushed; `jj-lane.sh state`: `local=remote=52435f2f… ahead=0 behind=0`).
Contract `.ufo/waves/round-31/contract.md`; lesson `corpus/lessons/round-31.md`.

## Work performed

Declared claims (2): **C1 — depth (5, tied lowest)**: a sourced decision table on FR5 ground, how a pid probe can and
cannot establish that the fleet watchdog is alive (`corpus/knowledge/watchdog-identity-r31.md`). **C2 — operability
(7)**: a new lane tool `tools/mori-blind-check.sh`, the round-30 blindness gate with routed D1 fixed. C1 is the sourced
claim. Both predicates were frozen before data (`2124cbcd`) and tightened by amendment A1 (`7973034b`) before any entry
or tool was scored; the claims are judged on P-C1-A1 and P-C2-A1, and both original predicates are reported too.

- Freeze before any seat: contract, `count-c1.py`, `count-c2.py`, 16 C2 fixtures (sha256 `1442c14e…`), rule text, three
  C2 control scripts, SCORECARD declaration — `2124cbcd`. Before and control receipts — `8baccf4a`
  (`.ufo/waves/round-31/evidence/c1-before.txt`, `c1-controls.txt`, `c2-before-base.txt`, `c2-controls.txt`).
- Wave 1 (41 seats) built sources, entry drafts, the tool (two independent builds), live probes on throwaway processes,
  repairs, and first falsifiers. Its critics met both frozen counters with cheap shortcuts (CriticSizing junk table,
  CriticC1Counter commented falsifier, CriticC2Counter answer-key/content-hash/order lookups) — lesson M3.
- Amendment A1 `7973034b` (conditions added: C1 no comments, distinct rows, ≥8-word readings, new URLs absent at the
  entering tip, ≥3-word located quotes, quote/row word overlap, a committed non-author row judge; C2 11 more fixtures,
  bwrap isolation, random order/mtimes/nonces, answer-key byte check). A1 control receipts `3b92ccbb`: 11 C2 and 5 C1
  controls, all unmet (`evidence/c2-a1-controls.txt`, `c1-a1-controls.txt`).
- C1 landed `5b728304`: 14-row table, 12 admitted sources S161–S165, S167, S169–S174 (S174 opened by the L1), two
  rejects (S166, S168), SKILL `## Round31` rows, README FR5 rows, upstream copies `corpus/evidence/sources-r31/`.
  Row 14 corrected at `efcb7324` after residual CriticC1Tip reproduced that the `/proc/locks` PID is the `flock` helper.
- C2 landed `458ff1c3`: `tools/mori-blind-check.sh` = wave-1 BuildBlindTool scratch output (`cmp`-identical, residual
  CriticC2Tip), `--selftest` PASS, round-30 writer wave → the three missing-list hits wave-1 RealBriefsR30 derived by
  hand, `CaseR30a.md:105` no longer a hit (`evidence/c2-tool-selftest-and-r30.txt`).
- Routed repairs D1–D9 (`1d94055d` and later): D3 QUALITY 94 supersedes 93; D4 entry corrected in place + appended,
  S120 linked; D5 map row `corpus/README.md:44`; D6 `tools/fixtures/mori-oom-killers/cases-r31-dryrun-flips.json`
  (tip `PASS 2/2`, round-30 base `FAIL 0/2`, `evidence/d6-dryrun-flips.txt`); D7 LOG; D8 SCORECARD; D2 lesson M2; D9
  noted. Residual ReviewRepairs: 9/9 closed (`.ufo/waves/round-31/r1/ReviewRepairs.md`).
- Residual non-author call (8 seats) — judge receipt `.ufo/waves/round-31/r1/JudgeC1Rows.md` (judged `efcb7324`: 13/14
  rows supported, row 9 unsupported); CriticAmendmentA1 found A1's C2 nonce hides an end-of-file failure (lesson M5).
- Planner seat: held by the L1 (validator rejects `planner`); no planning data-walk rode a seat.

## Landed changes

| Change | Commit | LOG entry |
|---|---|---|
| Freeze: contract, counters, fixtures, controls, SCORECARD declaration | `2124cbcd` | `LOG.md` "Round 31 … declaration and freeze" |
| Before and control receipts | `8baccf4a` | same |
| Repairs D3–D8, wave-1 spec/run/dispatch | `1d94055d` | same + "appended correction to the round-30 log (routed D7)" |
| Amendment A1, A1 fixtures, falsifier controls, SCORECARD before-cell correction | `7973034b` | "build, amendment and measurement" |
| A1 control receipts | `3b92ccbb` | same |
| C1 entry, SKILL rows, SOURCES S161–S174, Gate/lesson, copies, README FR5 rows | `5b728304` | same |
| C2 tool, self-test receipt, SKILL tool pointer | `458ff1c3` | same |
| Wave-1 reports, pre-judge receipts | `a29f3e3f` | same |
| C1 row 14 correction, Alt-implementation receipt, census-start | `efcb7324` | same (residual bullet) |
| Residual reports, judge receipt, lesson M5, S120 link, S174 label | `d0cac478` | same |
| Outcome, `c1-after.txt`, `c2-tip.txt`, `census-end.txt`, row 9 [INFERENCE] | `fde0b0b0` | same |
| Tip retention receipt | `52435f2f` | same (tip receipts named) |

## Before → after measurements

- **C1 (P-C1-A1)** — `python3 .ufo/waves/round-31/count-c1-a1.py <rev>`. Before `a12c68ae`: `entry=absent`,
  `C1=unmet`, exit 1 (`evidence/c1-before.txt`). After at `d0cac478` (entry bytes identical to the judged `efcb7324`):
  `rows=14 distinct_rows=14 short_readings=0`, `new_ids=12`, `gates_ok=12/12 copies_ok=12/12 fetch_ok=12/12
  distinct_sources=yes`, `rows_without_quote_overlap=0`, `judge … supported=13 supported_new=13 unsupported=[9]`,
  `skill_rows=6`, `C1=met`, exit 0 (`evidence/c1-after.txt`). Original `count-c1.py d0cac478` → `C1=met`, exit 0.
  Re-checked at `fde0b0b0` → `C1=met` (`evidence/tip-retention.txt`).
- **C2 (P-C2-A1)** — `python3 .ufo/waves/round-31/count-c2-a1.py <rev>`. Before at the freeze `2124cbcd` (tool absent):
  `exact=0/16`, `C2=unmet`, exit 1 (`evidence/c2-controls.txt`); at `a12c68ae` the counter exits 2 (fixtures absent;
  the declaration's before cell was wrong — lesson M1, SCORECARD correction). After at `d0cac478`: both bwrap runs
  `exact=27/27`, `answer_key_strings=none`, `C2=met`, exit 0; original `count-c2.py d0cac478` → `exact=16/16`,
  `C2=met`, exit 0 (`evidence/c2-tip.txt`). Uncounted: the independent BuildBlindToolAlt also `27/27`.
- No-harm: retention metric 4 at `fde0b0b0` (base 4, wave-1 RetentionBase); `git diff --diff-filter=D a12c68ae
  52435f2f` empty; round-30 evidence, `tools/mori-oom-killers.py`, `tools/mori-census.sh` unchanged; older
  oom-killers fixtures pass (residual CriticNoHarm, ReviewRepairs).

## Gate

Fourteen candidates opened; 12 admitted, **2 rejected**: S166 (`fs/proc/base.c` v7.2 — same URL and bytes as S127/S148)
and S168 (`proc.rst` v7.2 — same URL as S082). Rows and reasons in `corpus/lessons/round-31.md` `## Gate`; both stay as
`rejected` SOURCES rows. Residual ReviewGateSpot re-fetched 7 ids and agreed 7/7. Two locator corrections reported by
the row judge were rejected after checking the bytes (lesson Gate note).

## Sources & frontier

- Census start (`8baccf4a`): `sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori` → ten W04, `mori ok`,
  exit 0. Census end: twelve W04 (+S166, S168, rejected duplicates), `mori ok`, exit 0 (`evidence/census-end.txt`).
- Rows 160 → 174 (`grep -c '^| S[0-9]' corpus/SOURCES.md`): +14 (tier A: 12 mined — 7 code/docs from Linux v7.2 and
  procps-ng v4.0.7, 5 man-pages 6.20 pages; 2 rejected). Rows touched old → new: S120 `used-by` + the round-30 entry
  (D4). No status or recheck change on existing rows.
- Frontier: FR5 narrowed, not closed (`corpus/README.md` "Round-31 Frontier note"); the census probe is unchanged.
- Mined mistakes: M1–M5 in the lesson (M5 is a repeat of the round-30 D2 class: A1 said nothing loosened, but its C2
  nonce hides an end-of-file failure; C2 is met under both predicates, so the verdict does not depend on it).

## Trend verdicts

- **expansion: improved** — one new entry on unmapped FR5 ground with 12 new tier-A sources, and coverage-map rows for
  it and for the round-30 entry that lacked one (D5); no entry removed.
- **quality: improved** — new runnable gate with self-test (C2), routed D3/D4/D6 repairs closed (ReviewRepairs 9/9);
  caveat: entry row 9 was judged unsupported (now marked [INFERENCE], counted unsupported) and row 14 needed a
  correction before judging.
- **discernment: unchanged** — the round's own critics caught the counter shortcuts before data and the Gate spot-check
  agreed 7/7, but the L1 repeated the D2 class in A1's C2 nonce (M5) and mis-declared a before cell (M1).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` `## Round31` (6
  rows, S161+), judged by JudgeC1Rows (non-author seat, not a promotion verifier).
- [~] At least one end-to-end domain task executed and logged in LOG.md — live pid-probe measurements (LiveCommProbe,
  LiveArgvProbe) and the gate run on the round-30 wave, `LOG.md` round-31 entries.
- [~] Instructions executable by an agent without oral context — `SKILL.md` "Round31 — blind-writer gate" (command,
  outputs, limits).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; residual CriticNoHarm adjacency.

## Round shape and seats

Default shape with a residual instead of wave 2 (fewer than 32 genuine attack items after wave 1): **wave 1 v1, 41 seats**
(18 scout, 7 executor, 7 scribe, 4 critic, 3 reviewer, 1 mutation-tester, 1 connector), validated under policy v1, one
task call; **residual call 8 seats** (4 reviewer, 4 critic). Round total **49**. Dead seats: 0. Refusals: 0.
Wave registry and payload: `.ufo/waves/round-31/wave1-spec.json`, `wave1-run.json`, `wave1-dispatch.json`.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Inherited state: `.scratch/` only
(pre-round, untouched, not round work). Tool installs: none (bwrap 0.13.1 already present). Misroot sweep: none found.
Open L0 questions: none.
