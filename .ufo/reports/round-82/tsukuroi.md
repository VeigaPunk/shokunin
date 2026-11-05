# tsukuroi-shokunin — round 82 (hyaku run 15)

Lane repo: `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin` (branch `master`).
Delivered lane tip: **`11d6112b1c96e8ac44097bbba72b54c3f2a3c654`** — `git ls-remote origin refs/heads/master`
prints it, `jj-lane.sh state` = `local=11d6112b remote=11d6112b ahead=0 behind=0 tracked=0 untracked=0`.
Round date 2026-11-04. This is the fourth driver launch of the round and the second L1 to write
into it (see *Inherited state*); every commit below was re-measured by me at the delivered tip.

## Work performed

The round declares **three causally separable claims**, frozen before any candidate work
(`2786562e`, declaration block `SCORECARD.md` "Round 82 — declaration"):

- **C1 — depth (the lowest non-retired axis: depth 8, tied with adjacency 8).** For every `MT`
  row of `corpus/knowledge/mount-unit-fstab-plane-r81.json`, the quote locates in the
  line-preserving strip of the pinned snapshot **and** the row's cited `lines` is exactly the
  located raw span `[first,last]`. Target `count 8 / target 8 / met`.
- **C2 — operability (9).** Of the 26 committed single-clause mutants of
  `tools/count-mount-rows-r81.py` and `tools/measure-round81.py`, those whose own `--selftest`
  exits non-zero. Target `killed >= 24 / 26` **and** `genuine_killed == 17 / 17`.
- **C3 — calibration (9).** Every (round, axis) asserted by the standing `SCORECARD.md` blocks
  carries exactly one *after* ordinal; a block retires an earlier assertion only through a
  machine-readable `supersedes-ordinal: round-N axis` line. Target `count 0` findings.

Adjacency 8 is the other lowest axis and is **not** worked: its open item (ADJ-06/OUT-009
kaidoku/revenger arbitration) is operator-owned and unruled, so an adjacency move would have
been invented padding (`SCORECARD.md` "Lowest non-retired axis").

Work items, each with its evidence pointer:

- **Freeze with controls, before any candidate.** Three instruments, their sha256, the 26
  frozen mutation recipes and the no-work/red control receipts land in `2786562e`
  (`SCORECARD.md` "Round 82 — declaration"; `.ufo/waves/round-82/before/controls.txt`). C2's
  no-work score is appended at `683ae456`, still before a candidate exists.
- **No-work control (the do-nothing round).** At the lane tip `d5b3e134` the frozen counters
  read C1 `count 0 / target 8 / unmet` rc 1 (all eight rows `cited-range-not-the-quote-span`),
  C2 `killed 6 / 26, genuine 0 / 17` rc 1, C3 `count 1` finding (round 81 depth `[8, 9]` at
  `SCORECARD.md:6861` and `:6903`) rc 1 — `.ufo/waves/round-82/before/controls.txt:22-38`.
- **Red controls inside each instrument's own suite.** C1 `shifted-two-lines`,
  `fabricated-quote`, `range-too-wide` unmet and `correct-span` met; C3 `contradiction` and
  `silent-correction` each 1 finding, `named-correction` clean; C2 `kill-and-survive`,
  `recipe-missing-is-not-a-kill`, `red-baseline-refuses`, `no-recipes-absent` ok
  (same receipt). Blanket refusal is therefore not a gain.
- **C1 repair.** The eight `lines` values of the entry JSON are replaced by the located raw
  spans and the `.md` decision-table `source` column follows, plus a `## Coordinate convention`
  section and a Limits rewrite; quotes, statements, settings and `snapshot_sha256` untouched
  (`f376054a`; `.ufo/waves/round-82/w1/ExecAnchor.md`).
- **C2 selftest hardening.** 19 cases in `tools/count-mount-rows-r81.py --selftest` (was 6) and
  6 in `tools/measure-round81.py --selftest` (was 2), each driving the tool's own public
  `--fixture` path and asserting exit code plus token (`f376054a`;
  `.ufo/waves/round-82/w1/ExecMutCount.md`, `ExecMutMeasure.md`).
- **C3 correction.** One appended block names the round-81 depth ordinal the lane stands behind
  (8) with `supersedes-ordinal: round-81 depth`; nothing above it was edited (`f376054a`;
  `.ufo/waves/round-82/w1/ScribeOrdinal.md`).
- **Sourced claim and registry.** S331 re-opened at v262 (HTTP 200, 37 234 bytes, sha256
  `afbf3be6…2394`, byte-identical to the pinned snapshot) and a new row **S333** carries the
  raw spans with `supersedes S331 —` in `teaches`; validated on a mirror (`validate --file`
  rc 0) before the append (`8111113c`; `corpus/lessons/round-82.md` ## Gate).
- **Lesson, criteria, gates.** `corpus/lessons/round-82.md` with the Gate block and six mined
  mistakes; QUALITY 113 and 114; three gate-registry rows for the new instruments in
  `SKILL.md:5909-5911` (`8111113c`). Registry coverage `registered 125 / tools_total 125 /
  findings 0` rc 0 (`8111113c`, re-measured `43aa5768`).
- **Measured outcome and LOG entry** (`804dc4cb`), then the **wave evidence**, the two
  wave-driven refinements and the scout's coverage map (`43aa5768`), the tip receipts
  (`41fbe5da`, `aaba83cc`), the second L1's confirmation block and the concurrent-L1 mistake row
  (`c744021c`), and the `considerthese` adoption (`11d6112b`).
- **Wave.** One v1 wave `w1` under `ufo-wave-policy.json` (band 8–16), 12 seats, 12 settled,
  **12 durable reports**, 0 dead seats, 0 residual call (`.ufo/waves/round-82/w1-results.json`,
  `w1/*.md`). Round total 12. The wave produced six routed defects (R82-V1…V6) and the cheat
  table in `w1/CriticClaims.md`.
- **Frontier census.** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin
  tsukuroi` exit **0** at round start (`before/census-before.txt`, 332 rows) and exit **0** at
  round end (`after/census-after.txt`, 333 rows, 52 W04 duplicate-url warnings, no E-code).

## Landed changes

Every change is tied to its LOG entry (`LOG.md` "## Round 82 — raw-line anchors, mutation kills
and one ordinal") and to the commit that carries it.

| Change | Carried by | LOG/evidence |
|---|---|---|
| Three frozen predicates, instruments, 26 recipes, no-work/red controls | `2786562e` | LOG ¶ "Freeze before data"; `SCORECARD.md` "Round 82 — declaration" |
| C2 no-work score appended at the freeze commit | `683ae456` | `before/controls.txt` ¶ C2 |
| C1 raw-line anchors, C2 selftest hardening, C3 named ordinal correction | `f376054a` | LOG ¶ C1/C2/C3 |
| SOURCES row S333, lesson `round-82.md`, QUALITY 113/114, three gate-registry rows | `8111113c` | LOG ¶ "Sources and frontier" |
| Measured outcome table + LOG round-82 entry | `804dc4cb` | `SCORECARD.md` "Round 82 — measured outcome" |
| Wave `w1` evidence (spec, dispatch, ready, results, 12 seat reports), the `mutation-kill-r82` recipe clause, the criterion-113 precision, scout coverage map + its correction block | `43aa5768` | LOG ¶ "Wave — corrected at landing" |
| Final-tip re-derivation, registry-coverage/knowledge-refs gates, census receipt | `41fbe5da` | `after/commands-tip.txt`, `after/gates-tip.txt`, `after/census-tip.txt` |
| L1 confirmation block, `concurrent-L1-collision` mistake row, after-census receipt | `c744021c` | `SCORECARD.md` "Round 82 — L1 confirmation"; `corpus/lessons/round-82.md` ## Mistakes |
| Final-tip receipt for the three counters and four supporting gates | `aaba83cc` | `after/commands-tip.txt` |
| `considerthese/2026-10-26.md` "Counter-attack scoreboard" adopted as a lesson table + QUALITY 115 | `11d6112b` | `corpus/lessons/round-82.md` § Counter-attack scoreboard; `corpus/QUALITY.md:226` |

## Before → after measurements

Each claim's counting command is the frozen one, run at the no-work revision and at the after
revision. Instrument bytes are unchanged from the freeze (`fedd45ce…c3b3`,
`6e6d9715…7c24`, `888a3da9…1e84`, recipes `5e176afc…cb43`), re-verified by `sha256sum` at
`43aa5768` (`after/commands-tip.txt`).

| Claim / axis | Before (no-work control, committed before any candidate) | After at the measured commit | Verdict |
|---|---|---|---|
| **C1** depth | `python3 tools/check-anchor-coordinates.py --revision d5b3e134` → `count 0 / target 8 / unmet`, rc 1; eight rows `cited-range-not-the-quote-span` (`before/controls.txt:22-29`) | `… --revision f376054a` → `count 8 / target 8 / met`, rc 0; `MT1 [135,138] … MT8 [259,260]`, all `exact true`; re-derived by me at `11d6112b` | **verified**; depth 8 → 8 (one plane's coordinates repaired against a finite equality counter; no uplift claimed) |
| **C2** operability | `python3 tools/mutation-kill-r82.py --revision 2786562e` → `killed 6 / 26, genuine_killed 0 / 17`, `unmet`, rc 1 (`683ae456`) | `… --revision f376054a` → `killed 22 / 26, genuine_killed 16 / 17`, `unmet`, rc 1; re-derived by me at `11d6112b`; survivors `C06`, `C07` (equivalent) and `C16`, `M06` (recipe encoding) | **unmet — honest stop**; operability 9 → 9 |
| **C3** calibration | `python3 tools/check-scorecard-ordinals.py --revision d5b3e134` → `count 1`, round 81 depth ordinals `[8, 9]`, rc 1 | `… --revision f376054a` → `count 0 / examined 77 / clean`, rc 0; re-derived at `11d6112b` → `count 0 / examined 80 / clean` (the two extra blocks are the round's own outcome and confirmation blocks) | **verified**; calibration 9 → 9 |

**C2 is reported as a miss, not repaired in-round.** The frozen recipe file cannot be edited
after the freeze, and the miss is the recipe encoding, not the selftests:
`.ufo/waves/round-82/after/c2-recipe-applicability.txt` re-applies `C16-empty-manifest` and
`M06-mutation-unlink-noop` with a real newline and each mutant is then killed (`--selftest`
rc 3). Under the frozen file the arithmetic maxima are 22 killed and 16 genuine, so the target
`killed >= 24` and `genuine == 17` is unreachable by construction. The driver's ruling to the
wave's sentinel seat is on record: the frozen `mutants-r82.json` is not amended, C2 stays
unmet with this arithmetic, and the recipes are routed to round 83.

**No axis is harmed** (admission criterion): C2's miss leaves operability where it stood, and
neither verified claim moves an ordinal. The round is **not admitted** because a claim missed.

## Sources & frontier

Counting command (0–3 leading spaces, the census parser's own tolerance):

```
grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md
```

- **Rows before → after:** **332** at `d5b3e134` → **333** at `11d6112b`.
- **Census:** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`
  — round start **exit 0** (332 rows, `.ufo/waves/round-82/before/census-before.txt`), round
  end **exit 0** (333 rows, 52 `W04` duplicate-url warnings, no `E` finding,
  `.ufo/waves/round-82/after/census-after.txt`). My own run at `43aa5768` also exited 0 with
  333 rows (`after/census-tip.txt`).
- **Rows added by tier:** 1 row — **S333**, tier `docs`, grade `A`, `status mined`,
  `recheck 2026-11-04`, `used-by on-release`, cited by `corpus/knowledge/mount-unit-fstab-plane-r81.md`
  and `.json`. Every other tier gained nothing.
- **Rows touched old→new:** **none.** S331 is cell-for-cell identical at `d5b3e134` and at the
  delivered tip (checked column by column with a script over both blobs), so no `status`,
  `recheck` or `used-by` value changed and no old→new log line is owed; the supersession is
  recorded in S333's `teaches` cell ("supersedes S331 — …"), and the lesson's Gate block records
  the decision (S331 kept as filed, S333 admits the raw spans).
- **Frontier rows advanced:** S331's tag-stripped anchor window is superseded by S333's raw
  spans (MT1 135-138, MT2 502-503, MT3 486-487, MT4 491-492, MT5 234-236, MT6 339-341,
  MT7 198-201, MT8 259-260), so the mount-unit plane is now citable by raw file line. The
  scout's append to `corpus/README.md` (28 lines, `43aa5768`) records the round's ground and
  names seven open frontier surfaces (automount unit, `x-systemd.mount-timeout=`, swap unit,
  `/dev/shm` tmpfs, the `/tmp` device job bound, MT7/MT8 unexercised on this host, generation
  provenance) plus four open debts.
- **Refused reading (kept as a row-level rejection in the lesson's Gate):** "nofail guarantees
  the boot never waits, even with `x-systemd.before=`", contradicted by the same page at raw
  lines 239-242.
- **Assimilation:** `Assimilation: none` — no `merge/tsukuroi/` theme was adopted this round;
  the round's 1–3 claim cap was spent on the frozen claims, and the package's entries were not
  re-opened, so no row was appended from it (CORPUS rule 4: a row no admitted entry cites is
  not appended).
- **considerthese:** one still-unimplemented proposal mined —
  `considerthese/2026-10-26.md` (2026-10-26) "Counter-attack scoreboard", grounded through the
  lane's own bar: it lands as the per-counter table in `corpus/lessons/round-82.md`
  § Counter-attack scoreboard (arms fielded, killed/total, survivors, class that beat it) and as
  **QUALITY 115** (`11d6112b`). The other four proposals in that file stay unmined this round;
  the patch-offset one is already covered by QUALITY 103.

## Trend verdicts

- **expansion — unchanged.** No new ground surface: the one registry row is a re-registration of
  a held URL, and no knowledge entry was added (`git diff --stat d5b3e134 11d6112b --
  corpus/knowledge` touches only the two existing round-81 entry files, 32 insertions / 20
  deletions, all coordinates and prose about them). The README coverage map grew 40 lines, but
  they describe held ground and open debt.
- **quality — improved.** Three new QUALITY criteria (113 raw-line anchors and exact-span proof,
  114 frozen instruments with controls plus machine-readable supersession, 115 counter-attack
  scoreboard), three gate-registry rows for instruments whose own suites carry red cases
  (`SELFTEST 12/12`, `4/4`, `8/8`), the standing ordinal contradiction closed (`count 0` at
  `11d6112b`), and the mutation kills 6 → 22 of 26 with the surviving classes named instead of
  hidden.
- **discernment — improved.** The frozen target was recorded unmet rather than re-scoped or
  repaired after data; the round's own routed defects R82-V1…V6 are filed with evidence and
  routed to round 83 instead of being patched mid-round; the wave's critic produced a cheat
  table that names what each counter cannot see; and the driver/L1 collision is mined as a
  mistake row rather than written out of the record.

## SHONEN

- `[~]` **SKILL.md contains real decision tables, error patterns, checklists, cited sources** —
  resolvable: `SHONEN.md:5` carries the author-side pointer list; this round adds three gate
  rows at `SKILL.md:5909-5911` verified by `python3 tools/check-registry-coverage.py --revision
  43aa5768` → `registered 125 / tools_total 125 / findings 0` rc 0. Non-author verification
  still owed.
- `[~]` **At least one end-to-end domain task executed and logged in LOG.md** — resolvable:
  `LOG.md` round-82 entry (three claims, controls, measured outcome) plus the round-81
  end-to-end plane task it repairs; the domain task this round is the anchor repair of
  `corpus/knowledge/mount-unit-fstab-plane-r81.json` against the pinned v262 snapshot.
- `[~]` **Instructions executable by an agent without oral context** — resolvable: the wave's 12
  seat prompts were executed from absolute paths with no oral context
  (`.ufo/waves/round-82/w1-dispatch.json`), and the counters' usage lines plus the Gate block in
  `corpus/lessons/round-82.md` carry the replay steps. The whole-SKILL retest remains unexecuted.
- `[~]` **No cross-domain bleed (PROVINCE.md still accurate)** — resolvable:
  `.ufo/waves/round-82/w1/ConnectorScope.md` scans sibling lanes for the round's three surfaces
  (mutation harness owned by tameshi/kaidoku, self-assessment gate by tabi/kama/souji, anchor
  checking by kumitate/mori/tameshi) and finds the mount/fstab plane uncontested
  (`0` matches under sibling `corpus/knowledge/`); the round adds no claim over a sibling's
  surface. Contested kaidoku/revenger reverse-engineering ownership is still unruled.

## Round shape, seats and handoffs

- **Shape:** one v1 wave `w1` under `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy.json`
  (band 8–16), `reportDir: .ufo/waves/round-82/w1`. Spec `w1-spec.json`, dispatch
  `w1-dispatch.json`, handoff `w1.ready` (`l1: TsukuroiR82a2`), results `w1-results.json`.
  Dispatcher log: `spawned tsukuroi 82 w1 12` at 21:20:11.
- **Seats (12):** 3 executor (`ExecAnchor`, `ExecMutCount`, `ExecMutMeasure`), 3 scribe
  (`ScribeOrdinal`, `ScribeLesson`, `ScribeRegistry`), 1 scout (`ScoutFrontier`), 1 connector
  (`ConnectorScope`), 1 reviewer (`ReviewAnchor`), 1 critic (`CriticClaims`), 1 mutation-tester
  (`MutCheck`), 1 sentinel (`SentinelGate`).
- **Attack share:** reviewer + critic + mutation-tester = **3/12 = 25 %**, exactly the floor;
  with the sentinel counted as a fourth adversarial seat, 4/12 = 33 %. Connector seats: 1 (≤2).
- **Dead seats:** **0.** All 12 seats settled and wrote a durable report; the three that landed
  after the mid-wave count (`ScribeRegistry` 21:37, `SentinelGate` 21:38, `ScoutFrontier` 21:42)
  are why `LOG.md`'s mid-wave "10 durable reports / two seats died" paragraph is corrected in an
  appended paragraph rather than rewritten.
- **Residual call:** 0. **Round total:** 12.
- **Planner seat:** held by the L1 (the validator rejects `planner` as a swarm role); the
  round's bounded planning data-walk rode the `ScribeOrdinal` scribe item and the
  `ConnectorScope` connector item. Recorded here per the orchestrator ruling of 2026-10-19.
- **Routing:** no seat received a `model` argument; role routes come from
  `task.agentModelOverrides` in `~/.omp/agent/config.yml` (operator-owned, read-only for the
  lane). No claim's verdict depends on which model answered.
- **Seat bounds honoured:** every seat wrote only its report under
  `.ufo/waves/round-82/w1/` plus the lane files named in its item; no seat committed, pushed or
  ran a mutating VCS command; scratch lived under `/fast/scratch/hyaku/tsukuroi-r82/<seat>/`
  and was removed on exit (the two seats that left a tree named it as their own defect).

## Limits and routed defects

- **R82-V1 (high)** — C2's frozen target is unreachable, both legs (two recipes carry a
  two-character `\`+`n`, two are equivalent). Routed to round 83 with the recipes, not repaired
  in-round. `.ufo/waves/round-82/w1/SentinelGate.md:134`.
- **R82-V2 (medium)** — C3 retires an axis globally: a `supersedes-ordinal:` line silences every
  block, not only earlier ones, and quoted prose is parsed as an assertion (`SentinelGate.md:149`).
- **R82-V3 (medium)** — C3's `--revision` cannot-evaluate leaks as a traceback with rc 1
  (`SentinelGate.md:158`).
- **R82-V4 (medium)** — C2 counts a hung or unlaunchable selftest as a kill (`SentinelGate.md:161`).
- **R82-V5 (low)** — C1 never reads the entry's declared `snapshot_sha256`, so a doctored entry
  with self-consistent coordinates would pass (`SentinelGate.md:169`).
- **R82-V6 (low)** — importing a lane instrument writes `tools/__pycache__/` into the lane
  (`SentinelGate.md:174`).
- **C1 semantic limit** — the predicate proves locate-and-span equality, not that a quote entails
  its statement; a shortened quote still passes (`w1/ReviewAnchor.md` §4).
- **C3 scope limit** — the counter cannot distinguish quoted prose from an assertion; the block
  appended this round cites prose at `SCORECARD.md:7009-7010`, which only R82-V2's retirement bug
  keeps from being a finding (`w1/CriticClaims.md` §6, `SentinelGate.md` check 2).
- **Anchor authority** — the anchors are upstream v262 positions, not verified against the
  installed Arch build (QUALITY 103); the round does not claim installed-build line numbers.

## Inherited state, attempts and hygiene

- **Four driver launches for one round:** `.ufo/watchdog.log` records `launch tsukuroi round=82`
  at 21:04:36 (attempt 1), 21:08:34 (2), 21:22:19 (3) and 21:40:54 (this one), each preceded by
  `lane-dead-no-report`. The declared deaths were false for at least attempt 2: that L1 was
  blocked in `wait` on its own wave and kept working, so two L1s held the round at once
  (mined as `concurrent-L1-collision` in `corpus/lessons/round-82.md` ## Mistakes, `c744021c`).
  The two writers were separated by message: attempt 2 owned the lane and stood down after
  `11d6112b`; this attempt owns the report. No lane commit was rewritten, rebased or reverted.
- **Reused from the inherited state (all re-measured before citation):** the freeze and control
  receipts (`2786562e`, `683ae456`), the three candidates and their measured outcome
  (`f376054a`, `804dc4cb`), the source row, lesson, criteria and gate rows (`8111113c`), the
  wave payload and the 12 seat reports (`43aa5768`), and the two late doc refinements
  (`SKILL.md` recipe clause, `corpus/QUALITY.md` 113 precision) which were uncommitted in the
  working tree and are committed at `43aa5768`.
- **Discarded:** nothing was deleted. The wave's `w1.ready` was already taken
  (`w1.ready.dispatched`) and was never rewritten.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no file this
  round's seats wrote into the fleet root (no untracked fleet-root file names tsukuroi or round
  82). The single stray at the fleet root, `after` (24 B, `== SCORECARD diff base-`), is dated
  2026-11-03 20:05 — before this round — and belongs to no seat of mine; it was left untouched.
- **Scratch:** every seat's tree lived under `/fast/scratch/hyaku/tsukuroi-r82/`; the L1 removed
  the round's scratch root after landing; no counter writes a hardcoded `/tmp` path.
- **Tool installs:** none this round (no pacman transaction; the host-wide pacman pause holds).
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **L0 questions:** none appended this round; no operator decision blocks the round's landing.
