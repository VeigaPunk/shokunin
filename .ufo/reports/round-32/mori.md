# mori — round 32 report (attempt 2, L1 MoriR32A2)

Lane `mori-shokunin`, base `641a6e86ecc60634d215c0a47ab86c47661abf86`, landed tip
`5126891f6b6c8d79763cb9271811468b81acd908` (pushed; `jj-lane.sh state` → `local=remote=5126891f… ahead=0 behind=0`).
Attempt 1 (`MoriR32`) died with the orchestrator session and landed nothing. Its `.scratch/` leftovers were not reused.

## Work performed

Declared claim (one): **C1 — freshness**. The 34 `mined` SOURCES rows whose URL is not pinned to a tag or commit were
re-opened live. Each row got a committed copy, located quotes, a verdict and a bound non-author judgment, and the method
rests on new sources S175+. Freshness was tied lowest (5) with depth and calibration. Rounds 30–31 worked depth and
operability, so this round picks a different axis and surface. No exploratory claim, capability, retirement or waiver.

- Freeze before any seat: contract, frozen population (34 ids, sha `4426b650…`) and counter `count-c1.py`, with the
  before receipt `rows_ok=0/34 C1=unmet exit=1` — `29f7d043` (01:10:09Z), `.ufo/waves/round-32/contract.md`.
- Adversarial control wave C0 before data, 7 seats (payload `f44e428e`, receipts `8ab61aff`). The control set covers
  do-nothing at base and freeze, a junk table, all-unreachable with fake transcripts, teaches-echo quotes, a one-fetch
  reuse, a forged judge, a stale judge sha, off-topic quotes, on-topic but non-supporting quotes, 10 counter mutants,
  normaliser attacks and a positive control. **No negative control printed `C1=met`.** All 10 mutants were killed.
  Per-row false accepts that only the judge can catch were found and named before data, with no amendment —
  `.ufo/waves/round-32/evidence/c1-controls.txt`.
- Wave 1, 40 seats. 29 recheck seats opened the 29 distinct URLs live (01:31:22–01:31:35Z). The result is 33 `current`
  and 1 `unreachable` (S056, pnas.org bot challenge, three `curl --fail` exit-22 failures) — data commit `837b2802`,
  `corpus/lessons/round-32.md:17-54`, copies `corpus/evidence/recheck-r32/`.
- New method sources S175 (curl manual), S176 (Python `unicodedata`) and S177 (Python `html`) were admitted, and S178
  and S179 were rejected as duplicate URLs — `corpus/lessons/round-32.md:56-73`, `corpus/evidence/recheck-r32/README.md`.
- Non-author judge JudgeRecheck (reviewer) agreed 34/34 on section sha `251bf664…8407` at `837b2802` —
  `.ufo/waves/round-32/judge/JudgeRecheck.md`, landed `7766732a`.
- Attacks by 3 residual seats plus wave-1 critics. The disagreements are kept open with the judge's readings: S128/S149
  quotes cut before an "although" exception, S058/S117/S128/S149/S137 resting on more than the population URL, and the
  P-C1 text being identical only after whitespace normalisation — `corpus/lessons/round-32.md:97-124`.
- Routed round-31 defects 1–6 (hygiene, not claims):
  - M5 correction appended to `corpus/lessons/round-31.md` (9 masked fixtures, confirmed by script and mutant).
  - Blind-writer gate registry row with all eight §Gate fields at `SKILL.md:784-794`.
  - Digest-pinned frozen run `.ufo/waves/round-32/frozen/blind-check/`: `verify.sh` gives `frozen_run: match` exit 0,
    a tampered input gives `snapshot_tampered` exit 2, and a mutated tool gives exit 1.
  - Docstring note kept in the contract.
  - The R4 sha binding becomes QUALITY 95 (`corpus/QUALITY.md:683`).
  - The counter was frozen before data.
  - 12 edge fixtures at `.ufo/waves/round-32/fixtures/edge/`.
  - Disposition table: `corpus/lessons/round-32.md:137-147`.
- Mistakes M1–M3 mined (`corpus/lessons/round-32.md:75-95`). QUALITY 96 comes from M1 (`corpus/QUALITY.md:691`).
- SKILL decision rows for the live recheck at `SKILL.md:796-810`.

## Landed changes

| Commit | What | LOG |
|---|---|---|
| `29f7d04355f17b5d45d6e00c40e2a5c3e5a2c9c4` | C1 freeze: contract, population, counter, before receipt, census start | `LOG.md:2041` (round-32 entry, freeze bullet) |
| `f44e428ec01b6914984b1365310abdf607959edc` | C0 dispatch payload | `LOG.md:2041` (C0 bullet) |
| `8ab61affbd2fc59030040bf80cddc08f7c60ad82` | C0 receipts, seat helper `seat-check.py`, wave-1 spec, validator run and dispatch | `LOG.md:2041` (C0, wave-1 bullets) |
| `837b2802c60a6e37a9d462f2354107307fba6ef1` | recheck data: 34 rows, 33 copies + 1 transcript, S175–S177, README | `LOG.md:2041` (wave-1 bullet) |
| `a45850f05e4faf039b70431dee0a93e6fe2b200f` | residual R1 payload | `LOG.md:2041` (R1 bullet) |
| `7766732a98795467d0541630e9707a7acba518e1` | judge receipt, wave-1/R1 reports, blind-gate frozen run and registry row, edge fixtures, M5 correction | `LOG.md:2041` (R1, routed bullets) |
| `8abb90a3f751f6984bb359ae64b4f6a216f6a595` | lesson (mistakes, attacks, dispositions), QUALITY 95–96, SCORECARD declaration and outcome, LOG | `LOG.md:2041` |
| `b0d1d4cbd1ebab576fc843488cf004b62996a185` | round-end receipts (C1 after, census end, retention) | `LOG.md:2041` (C1 bullet) |
| `55c3ed5e3386e1adf524a63589f51cc0540607fa` | Gate rejects S178/S179, their copies as uncounted evidence | lesson Gate |
| `5126891f6b6c8d79763cb9271811468b81acd908` | S179 reason corrected; tip receipt at `55c3ed5e` | lesson Gate |

## Before → after measurements

| Claim | Command | Before | After |
|---|---|---|---|
| C1 freshness | `python3 .ufo/waves/round-32/count-c1.py <rev>` | `641a6e86` → `rows_ok=0/34 new_ok=0 C1=unmet exit=1` (`evidence/c1-before.txt`) | `7766732a` → `recheck_rows=34 header_ok=True judge_ok=True judge_agree=34 rows_ok=34/34 verdicts={'current': 33, 'unreachable': 1} new_ok=3 C1=met exit=0` (`evidence/c1-after.txt`); re-measured at `55c3ed5e`: same, plus the expected `new_failures` for the two rejected rows (`evidence/tip-c1.txt`) |

Predicate P-C1 (contract `:31-34` = counter docstring, same words, different line wraps — lesson M3). It was frozen
before data and never amended. Proposed verdict: **improved, pending closure**. Freshness held at 5. Open point for the
closure: on five multi-source rows the judge read `current` as "the part the population URL carries holds and
nothing contradicts the rest". Under a strict reading those rows fail R4 and C1 is a miss (lesson `:113-116`).

No-harm: retention scan metric 4 at `8abb90a3` = 4 at base (`evidence/tip-retention.txt`). Census `mori ok` exit 0 at
start and end with the same twelve W04 lines. No axis score changed. `PROVINCE.md` and `tools/` are unchanged.

## Gate

Five candidates opened: three admitted, two rejected (`corpus/lessons/round-32.md:56-73`).
- S175 `https://curl.se/docs/manpage.html`, S176 `https://docs.python.org/3/library/unicodedata.html`,
  S177 `https://docs.python.org/3/library/html.html` — admit, A, mined. Copies are at
  `corpus/evidence/sources-r32/`, and the counter's new-source check passes all three.
- **Reject S178** `https://git-scm.com/docs/git-diff-tree`: duplicate URL, already the second URL of S058's source
  cell (`corpus/SOURCES.md:64`).
- **Reject S179** `https://pmc.ncbi.nlm.nih.gov/articles/PMC5856500/`: duplicate URL, already named in S056's source
  cell as its full-text route (`corpus/SOURCES.md:62`).

## Sources & frontier

- Rows: `grep -c '^| S[0-9]' corpus/SOURCES.md` → 174 at `641a6e86` → 179 at tip.
- Added by tier: A +5 (3 mined, 2 rejected).
- Rows touched old→new: none (the 34 rechecked rows keep every cell; results live in the lesson `## Recheck` table).
- The census command was run at start (`evidence/census-start.txt`, exit 0) and at end (`evidence/census-end.txt`,
  exit 0, `mori ok`, the same twelve W04).
- Frontier rows advanced: none. ScoutFrontier found that no FR row covers source-registry freshness, and QUALITY 59
  forbids calling re-verification new ground (`.ufo/waves/round-32/w1/ScoutFrontier.md`).
- Sourced claim: C1's method README cites S175–S177.
- Mined mistakes: M1 (frozen contract asserted "last opened when added", contradicted by the base sweep
  `evidence/m1-reopen-sweep.txt`), M2 (round-31 defect 5), M3 (byte vs normalised parity).

## Trend verdicts

- **expansion: unchanged.** No new knowledge entry or coverage ground. Three method sources were added; the frontier is
  unchanged.
- **quality: improved.** 34 mutable-URL rows were re-verified live with committed copies under a pre-frozen counter.
  The blind-writer gate gained a digest-pinned frozen run and a full registry row. The M5 wording was corrected.
  QUALITY 95–96 were added.
- **discernment: unchanged.** The judge is a lane seat, not an outside spot-check. Lane attackers disagree with it on
  several rows, and those disagreements are recorded, not resolved. Outside verification is pending.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:796-810` (Round32
  recheck rows citing S175–S177), `:784-794` registry row. Seat-reviewed only.
- [~] At least one end-to-end domain task executed and logged in LOG.md — live recheck of 29 URLs and the frozen gate
  run, `LOG.md:2041`.
- [~] Instructions executable by an agent without oral context — `corpus/evidence/recheck-r32/README.md` (method,
  limits), `count-c1.py` and `seat-check.py` usage.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; sources opened read-only, no
  bot challenge passed.

## Round shape and seats

The orchestrator's 01:05Z ruling required an adversarial control wave before any data seat. So the shape is a control
call, then one v1 wave, then a residual call instead of wave 2 (fewer than 32 genuine attack items after wave 1).
- **C0**: ordinary task call, 7 seats (4 critic, 3 mutation-tester).
- **Wave 1**: v1, validated under `ufo-wave-policy.json`, one task call, 40 seats (33 scout, 3 executor, 1 connector,
  1 scribe, 1 reviewer, 1 critic). The §3 floor is met inside it. The planner seat is the L1, and the frontier
  planning data walk rode ScoutFrontier.
- **Residual R1**: 4 seats (2 reviewer, 1 critic, 1 mutation-tester).
- **Round total 51.** Dead seats: 0. Spawn refusals: 0.
- Payloads: `.ufo/waves/round-32/c0-dispatch.json`, `wave1-spec.json`, `wave1-run.json`, `wave1-dispatch.json`,
  `r1-dispatch.json`.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Inherited state: `.scratch/` only (not
round work). Tool installs: none. Misroot sweep: there are eight untracked fleet-root files plus a pycache file; none
names mori round 32 and all predate the 01:01Z dispatch, so none was moved. Open L0 questions: none.
