# kaidoku — round 47 report

Lane `kaidoku`, round 47, attempt 1. Lane repo `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`,
base `13a9e9e1f7ca3b95f2cc11f24f69d0d92a21a8a5`.

Lane tip at filing: `242e8b973b28c10953e59688626e9092db89031a`
(`git ls-remote origin refs/heads/main`).

**Declared claims (2, both landed and measured).**

| claim | axis | surface | verdict |
|---|---|---|---|
| R47-C1 | depth | `SKILL.md` `## Queue-drain craft` rule block 24 (marker `<!-- exactness-table v3 -->`) and its counter `tools/round-47/exact.py` | **met** (exit 0 at `a0753786`) |
| R47-C2 | calibration | `tools/round-47/record.py` re-deriving 50 self-assessment atoms, plus the append-only `## Record corrections — round 47` | **met** (exit 0 at `a0753786`) |

## Work performed

- **Froze both instruments before any verdict**, then amended them five times under disclosure: the
  freeze series is `5017e1f7` (plan + counters) → A1 `9018c53b` (an unreachable `window` clause) →
  A2 `62e33f7d` (a window forgery that was empty by construction; block 24's arm cells reduced to
  the token clause 5 binds) → A3 `2e4ae43` (a correction for a round older than the window stays
  valid evidence) → A4 `1e2c310295` (a selftest fixture typo) → A5 `07d2894e` (the ghost-atom
  forgery landed outside the corrections section) → A6 `f54b3b6d` (the battery fixture lacked a
  citation the landed block names). **Declared freeze: A6.** Every amendment carries a red-before
  receipt; the series itself is the round's M47-1/2/5/7 finding, not a footnote.
- **Landed block 24** (`SKILL.md`, four rows, one per R46-CL2/CL3/CL4/CL6): exact arm tokens, routed
  ids exactly once, `mutations_sha256` over the counter's own mutation list, the gate's flag order,
  nine resolving citations including `corpus/lessons/round-46.md` and a `corpus/knowledge/` entry,
  and both sha256 pins. Evidence: `SKILL.md:612-641`, `l1/scores/c1-at-A7.json`.
- **Landed the record repair**: `## Record corrections — round 47` in `SCORECARD.md` names the
  round-45 seat atom (claimed `wave 2: 32`, dispatched `36`) and the round-46 window that named a
  `<tip>` placeholder, and states the window the counter itself reproduces as empty
  (`332f4884..58eb04b6 -- tools/round-46 plans/round-46-claims.md`, 0 bytes). The `## Owned axes`
  coverage, depth and calibration heads now read `138/138`, `24/24` and `4 → 0 mismatches`.
  Evidence: `SCORECARD.md` corrections section, `l1/scores/c2-at-A7.json`.
- **Fixed the record's own proxy harm before claiming**: block 24 first cited lessons and plans only,
  so command A read `23/24` (`depth_score 9.58`) — round-46's M46-4 exactly, one round after
  `QUALITY.md` row 77. The block now cites `corpus/knowledge/2026-10-25-r34b-pre-freeze-shortcut-replay-gate-stop.md:40-66`
  and command A reads 24/24; recorded as M47-6 and QUALITY row 78.
- **Opened two sources**: S143 (`re.fullmatch`, admitted, tier A, `mined`) grounds the equality the
  arm clause needs; S144 (the Regular Expression HOWTO) was opened and **rejected** — `fullmatch`
  occurs 0 times in its rendered text. Both are in `corpus/lessons/round-47.md` `## Gate` with the
  access date and a ≤25-word located quote.
- **Wave**: one v2 wave, `r47-w1`, 75 seats — role mix and settlement in *Round shape* below. The
  seats did the round's falsification: `C1Battery` rebuilt the four forgeries with its own mutation
  code (v2 0 / v3 1 on all four) and found clause 5 membership-only plus a vacuous-citation hole;
  `CritGold` built the cheapest artefact that scores both claims `met_target true` without the work;
  `ConnSeparability` falsified the claims file's separability assertion in one direction and caught
  the record quoting its own receipt wrongly; `RevC2Scope` showed `record.py` has no freeze arm;
  `C1Order`/`RevC1Digest` found the flag-order clause forgeable by a comment and the battery's no-op
  branch counting a non-forgery as a pass. Every one of them is routed in
  `corpus/lessons/round-47.md` (R47-CL6…CL14) rather than smoothed over.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| `plans/round-47-claims.md`, `tools/round-47/{exact,record}.py` (freeze) | round-47 freeze bullet | `5017e1f7` |
| A1–A6 amendments + the pin update | freeze-series bullet | `9018c53b`, `62e33f7d`, `2e4ae43`, `1e2c310295`, `07d2894e`, `f54b3b6d`, `a0753786` |
| wave spec, dispatch, controls | wave bullet | `3186f69b` |
| block 24, the corrections section, the axis heads, S143 | landing bullet | `e856beb5` |
| SCORECARD round section, LOG entry, lesson + Gate, QUALITY 78, S144, receipts | record bullet | `caafeffa`, `a631bba0`, `31b092d1` |
| the knowledge citation that repairs the proxy harm | M47-6 bullet | `04469ee8` |
| wave-1 seat reports (74 of 75 seats) and R47-CL15 | wave bullet | `242e8b97` |
| final receipts at the tip | measurements bullet | `b1a058f3` |

## Before → after measurements

- **R47-C1** — `python3 -I -B tools/round-47/exact.py --root . --freeze f54b3b6d --rev <REV>`.
  Before (at the freeze): exit 1, `block_present 0`, `rule_blocks 23`, `marker_occurrences 0`
  (`.ufo/waves/round-47/controls/ctl-c1-0-do-nothing.json`); the battery cannot be built before a
  block exists (`ctl-c1-2-freeze-battery-absent.json`); the ported round-46 profile accepts all four
  forgeries — `--profile v2 --no-battery` exit 0 (`controls/ctl-c1-1-v2-profile.json`), and the
  battery's own `v2_green` reads 4. After (at `a0753786`): exit 0, `rule_blocks 24`, `rows 4`,
  `refs 9`, `unresolved_citations []`, both pins equal the bytes at rev, battery
  `forgeries_total 4 / v2_green 4 / v3_green 0 / genuine_green 1 / crash 0`
  (`.ufo/waves/round-47/l1/scores/c1-at-A7.json`).
- **R47-C2** — `python3 -I -B tools/round-47/record.py --root . --rev <REV>`.
  Before (at the base): exit 1, 4 mismatches — the round-45 seat atom (claimed `32`, dispatched
  `36`), the round-46 window atom naming a `<tip>` placeholder, coverage `133/133` against
  `138/138`, depth `20/20` against `23/23`
  (`.ufo/waves/round-47/controls/ctl-c2-0-do-nothing.json`). After (at `a0753786`): exit 0,
  `atoms 42`, `mismatches []`, `corrections 2` (both re-derived), `exempted 1 <= 3`, battery
  `correction_forgeries 3 / forgeries_green 0`
  (`.ufo/waves/round-47/l1/scores/c2-at-A7.json`). The atom count falls from 50 to 42 because the
  last-two-sections window advanced to rounds 46–47 when this round appended its own section.
- **Separability, measured not asserted.** The claims file said R47-C2 "never reads the craft
  section"; `ConnSeparability` showed `record.py`'s `axes` class derives the `depth` head from
  `SKILL.md`, so C2 moves with C1's artefact (block 24 removed → `depth 24/24 → 23/23`, C2 exit 1).
  C1 is independent (`SCORECARD.md` deleted → C1 exit 0). Reported as falsified in one direction
  (M47-8); the frozen predicate is unchanged.
- **The record quotes its own receipts.** `ConnSeparability` caught the round section saying
  `atoms 50` / `exempted 2` while the cited receipt reads `atoms 42` / `exempted 1`; both cells are
  corrected (M47-9), and the absence of a counter that binds a quoted number to its receipt is
  routed (R47-CL13). The two `- corrects axes` lines were inert (the correction grammar excludes the
  class) and are now prose; routed as R47-CL14.
- **No axis harmed**: the round's diff over the lane touches `SKILL.md`, `SCORECARD.md`, `LOG.md`,
  `corpus/{QUALITY,SOURCES}.md`, `corpus/lessons/round-47.md`, `plans/`, `tools/round-47/` and
  `.ufo/waves/round-47/`; `corpus/knowledge/` and `PROVINCE.md` are byte-unchanged
  (`git log --name-status --format= e856beb5..f54b3b6d -- corpus/knowledge PROVINCE.md` → 0 lines).

## Sources & frontier

- `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku` — round start
  exit 0 (`kaidoku ok`, warnings only); round end exit 0 (`kaidoku ok`, 16 `W04` warnings).
- Rows: **142 → 144** (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`). Added by
  tier: one tier-A `docs` (S143, admitted, `mined`) and one tier-C `docs` (S144, `rejected`).
- Rows touched old→new: none (`status`, `recheck` and `used-by` edits: 0). Frontier rows advanced:
  none — this round's sources are instrument documentation, not domain ground.
- **Sourced claim**: R47-C1's arm clause rests on S143, opened this round
  (`https://docs.python.org/3/library/re.html`, `re.fullmatch`).
- **Assimilation: none.** No `merge/kaidoku/` theme applies to an instrument-exactness round;
  `considerthese/` is absent in this lane.

## Trend verdicts

- **expansion — `unchanged`.** `corpus/knowledge/*.md` 138 → 138 at the base and at the final tip; no
  coverage-map row changed; `PROVINCE.md` byte-unchanged. S143/S144 are instrument documentation and
  a rejection, not domain ground.
- **quality — `improved`.** The exactness counter scores its own four forgeries red (v2 accepts all
  four, v3 rejects all four) and the record counter scores its own three forged corrections red;
  block 24 states four routed defects as checkable clauses; `QUALITY.md` row 78 grounds two of them.
  Bound, stated in the lane: this is instrument quality, and the two counters' own limits are routed
  (R47-CL1…CL8).
- **discernment — `improved`.** Four of the round's own defects were found by measuring its own
  instrument before the operator (A1 unreachable clause, A2/A5 no-op forgeries, A6 an incomplete
  fixture), and the record defect (M47-6, proxy harm) was caught and repaired before the claim was
  called met. Caveat recorded: the freeze became a seven-commit series, and the round's record was
  wrong twice on the way in.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — rule block
  24 (four routed defects, one clause each) and the two new instrument-registry rows at
  `SKILL.md:612-641` and the registry section; verifier: none (author-asserted).
- [~] At least one end-to-end domain task executed and logged in LOG.md — this round is
  instrument-first by design; the last domain execution remains round 42/43 (`LOG.md` round-42/43
  entries). No new domain task this round; recorded, not claimed.
- [~] Instructions executable by an agent without oral context — `tools/round-47/exact.py` and
  `record.py` each carry a `--selftest` (16 and 10 cases, both exit 0 at the tip) and a documented
  CLI; evidence `.ufo/waves/round-47/l1/scores/{c1,c2}-at-A7.json`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` byte-unchanged in the round
  (`git log --name-status --format= e856beb5..f54b3b6d -- PROVINCE.md` → 0 lines); no domain claim
  was added or promoted.

## Round shape

- One v2 wave, `r47-w1`, validated under `scripts/hyaku/ufo-wave-policy-v2.json` (band 64–128), one
  `task` call; spec `.ufo/waves/round-47/w1-spec.json`, dispatch `w1-dispatch.json`, registry
  `w1/swarm-registry.json`, results `r47-w1-results.json`.
- Seats: **75** (`counts.spawn 75`) — executor 17, scribe 8, scout 8, reviewer 14, critic 10,
  mutation-tester 8, connector 4, sentinel 2, revenger 2, simplifier 2. Attack share
  (reviewer + critic + mutation-tester + sentinel + revenger) 36/75 = 48 %. Connector seats 4.
- **Settlement (honest record).** No `WAVE-DONE` was received and no `r47-w1-results.json` exists:
  the dispatcher settles a wave only when every seat returns, and one seat never did. Measured at
  filing (2026-10-28T18:16Z): **74 of 75 seats wrote output** (report file or seat directory with
  receipts); **1 seat wrote nothing**: `SentFixtures`. The orchestrator was asked twice to settle
  (`agent://Main`), and the round files with the observed settlement rather than a claimed one. No
  seat was replaced and no wave was re-sent.
- No residual call was made: the wave's attack items (36 seats) exceeded the 32-item floor, so no
  separate reviewer/critic batch was needed.
- Planner seat: the L1 holds the canonical §3 planner seat; the validator rejects `planner` as a
  swarm role, so the bounded planning data-walks rode scout seats (eight of them). Recorded per the
  orchestrator ruling 2026-10-19.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none (no `pacman`, no `uv tool`, no binary added); the pacman pause was
  respected.
- **Inherited state:** the lane carried round-45/46 wave leftovers (`git status` showed 5 modified and
  169 untracked paths under `.ufo/waves/` before this round); none was authored by this round and
  none was swept into a commit.
- **L0 questions:** none opened; none pending for this lane.
