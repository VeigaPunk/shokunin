# kumitate — round 100 report (hyaku run 15, attempt 1)

Base `dc8b7e4aff45e7ac10193643f23b1866791d0345` (r99 closure spot-check tip) → final lane
`034e52b4f5dbea4686d6dc8d9e957b705f2e60da`, branch master. L1 KumitateR100 holds the planner seat (the validator refuses
`planner`). `git ls-remote origin refs/heads/master` prints that final hash; helper state local=remote, ahead/behind=0,
tracked/untracked=0. No inherited uncommitted lane work. No earlier attempt of this round (fleet `.ufo/watchdog.log`: one
`launch kumitate round=100 … attempt=1`, no `lane-dead-no-report`). Not a fresh-start round (r92–r99 admitted).
Paths below are lane-relative under `.ufo/waves/round-100/` unless stated.

## Work performed

Declared one claim: **C1 operability**, the lowest non-retired axis (9, terminal under f_O). R100:
`scripts/cite-sources.mjs:36` and `scripts/source-capture.mjs:157` recognise a SOURCES row id exactly as the census
`row_pass` does: one LF record per line, 0–3 ASCII SP indent, id cell padded with SP/TAB only, `S` + 3+ ASCII digits
closed by `|`. Before the change, both tools used JS `\s` pads. source-capture also accepted any `\s` indent and used
`matchAll(/gm)`, so a row after CR, U+2028 or U+2029 on one LF record counted as a row. Sourced on S280/S281 (MDN, opened
this round) with S276/S277/S274. Every coverage axis unchanged at 10. Not a capability acquisition.

- Pre-freeze adoption `5e2f9856`: the r99 spot-check went into the README map, DRIFT → CLEAN
  (`open/readme-map-before-adopt.txt`, `close-l1/adopt-r99-spotcheck.txt`; considerthese 2026-11-06 proposal 3).
- Freeze `445196e4`:
  - plan;
  - frozen counter `probe/probe100-c1.mjs` (135-row battery, census oracle live; arms (a) cite per row, (b) capture whole
    file, (c) BASE = candidate on 21 fleet lanes, (d) selftests);
  - generator and 16 pre-data controls, all matching expected (`controls/OBSERVED.txt`): positive HELD; 15 negatives
    UNMET, including `ctl-k99`, the r99 draft fix, which keeps the `m`-flag hole (six record-axis misses).
  - Do-nothing BASE reads `UNMET a=0 b=0 c=1 d=1 a_miss=42 b_miss=64` (`controls/ctl-nothing.txt`).
  - Seed replays of the positive and do-nothing controls reproduce identically (`close-l1/replay-controls.txt`).
  - Five extra seeds: positive HELD and k99 UNMET each time (`close-l1/seed-stability.txt`).
- The first control run let `ctl-indent4` read HELD because the generator added a random extra indent space. I repaired the
  generator before the freeze and re-ran all 16 controls (`controls/pre-repair/`; M100-2).
- Spec and validated dispatch `2abafa0e`: ONE w1 v1 wave of 12 seats. Main sent WAVE-DONE; `w1-results.json` holds 12
  results and no dead seats.
- M `7c3bca09` = K100ExecTool READY (cite `e887b982…`, capture `ad3227d6…`). Selftests: cite 8→25, capture 13→33. The
  frozen counter reads HELD twice (`close/probe-m-{1,2}.txt`). L1 re-mutation gives `REMUT: killed=15/15 reference=PASS`
  (`close-l1/integration-remut-M.txt`; BASE reads 0/15, `close-l1/remut-base.txt`).
- M2 `4897e20c` (cite `da16e32b…`, capture `c9f22275…`) adds selftest arms for what the wave found:
  - **K100CriticA's 14 wrong readers that the counter rates HELD:** undrawn Zs/NUL/ZWNJ pads, 8/9-digit caps, U+2000
    indent, a 1000-record cap, the README gate, and fixture-keyed fallbacks. Result: `M2_TEETH: killed=18/18`
    (`close-l1/m2-teeth.txt`).
  - **K100Mutation's two non-equivalent survivors:** M30 (2-digit ids in capture) and M32 (cite split-any). Result:
    `M2_SURVIVORS: killed=2/2` (`close-l1/m2-survivors.txt`).
  - Selftests now read 45/45 and 54/54 (`close-l1/selftest-M2.txt`), REMUT is 15/15 (`close-l1/integration-remut.txt`), and
    the frozen counter reads HELD twice (`close/probe-m2-{1,2}.txt`).
- Independent attack evidence:
  - K100CriticC built a differential from its own generator: 1344/1344 cite probes and 990/990 capture fixtures agree with
    the census on two seeds; BASE disagrees on 115 and 203 (`w1/K100CriticC.md`).
  - K100Reviewer: production diff = one reader line per tool; 20/20 hand cases match the census (`w1/K100Reviewer.md`).
  - K100ExecHarm: the battery is unchanged apart from the designed pin drift; 209/209 history comparisons are the same
    (`w1/K100ExecHarm.md`).
  - K100Scout and K100CriticB: 0 divergent rows live (21 lanes) and in 363 historical revisions (`w1/K100Scout.md`,
    `w1/K100CriticB.md`).
- Honest limits:
  - HELD is a refutation budget, not a proof: 14 wrong constructions read HELD; the M2 arms kill them.
  - The change is prospective: no live row is affected, and arm (c) is vacuous on today's data, as the plan disclosed.
  - Section scope (rows outside `## Registry`) is excluded. K100ExecSection measured it and routed it to r101
    (`w1/K100ExecSection.md`).
  - The census oracle hash is not pinned in the receipts. K100CriticB flagged this and it is routed.
- Hygiene (disclosed, not claimed): two SOURCES gates had been red since r93/r94 because the close battery omitted them.
  - `source-capture` went from DRIFT bad=11 to CLEAN: S269–S279 are bound to committed captures, S270/S276 are exempted with
    reasons, and S280/S281 are bound.
  - `source-dupes`: the S253/S271 group is pinned.
  - This is mined as M100-4 and Q95. At freeze, `surface-probe --checklists` read 37/47
    (`close-l1/checklists-at-freeze.txt`). Items 743/744 are now repaired; the other reds (host-bound OMP shape, kimi score,
    omp census, gate-mutants, round-close audit) are routed.
- Close: S280/S281, knowledge `corpus/knowledge/row-id-reader-class.md`, lesson M100-1..4, Q94/Q95, SKILL rows, README map,
  LOG and SCORECARD landed. Final battery is all CLEAN/MATCH, exit 0, `--strict` included (`close/battery-final.txt`).

## Landed changes

Every row is tied to LOG.md `## Round 100` and its dated bullet.

| lane commit | change |
|---|---|
| `5e2f9856271525760ade3b08892f6df7601fa689` | r99 spot-check map adoption before freeze |
| `445196e4609b76f23d706403b7bebf1135066952` | plan, frozen counter/generator, 16 control receipts (+pre-repair), read-order log, open receipts, battery |
| `2abafa0eb95ac67e98cc898d2c1ebe503d650618` | w1 spec + validated dispatch + read-order check at freeze |
| `7c3bca09124f32887045c1b843d587dc692f9bb1` | M: R100 readers, selftests 25/33, remut + replay receipts |
| `4897e20c37a684a8c366cc5aa1bfe84ffae130a4` | M2: undrawn-class + survivor arms, selftests 45/54, teeth receipts |
| `173a5314a8ef82ff362a70d02b5493308a06627b` | wave evidence, S280/S281, knowledge, lesson, Q94/Q95, capture/dupes pins, proxy/counter pins, SKILL/LOG/SCORECARD/map, final battery |
| `034e52b4f5dbea4686d6dc8d9e957b705f2e60da` | K100CriticC differential outputs as gzip (raw >1 MiB; raw sha256 kept) |

## Before → after measurements

Command (candidate bytes from `git show REV:scripts/{cite-sources,source-capture}.mjs`):

```sh
node .ufo/waves/round-100/probe/probe100-c1.mjs --cite <cite bytes> --capture <capture bytes> --work <scratch>
```

| C1 | before: base 5e2f9856 (= ctl-nothing bytes) | after: M2 4897e20c |
|---|---|---|
| frozen verdict | UNMET a=0 b=0 c=1 d=1 | HELD a=1 b=1 c=1 d=1, twice |
| cite rows disagreeing with census | 42 / 135 | 0 / 135 |
| capture ids disagreeing with census | 64 | 0 |
| selftests | cite 8/8, capture 13/13 (pin no row class; REMUT 0/15) | 45/45, 54/54 (REMUT 15/15, teeth 18/18, survivors 2/2) |

The axis score delta is **9→9 terminal**; every coverage row is **10→10**. Proxy bookkeeping only: `A_wave` 1755→1839,
`C2`/`C2_total` 257→260, `pin.cite-sources` 7211be84…→da16e32b…, `pin.source-capture` 39bdeb39…→c9f22275… (also re-pinned
in counter-pins). `PROXY: MATCH --strict` holds at close.

## Sources & frontier

Rows **217→219**, counted with `git show <rev>:corpus/SOURCES.md | grep -cE '^ {0,3}\| S[0-9]{3}'` at `5e2f9856` and
`034e52b4`.

- **Tier B +2:** S280 (MDN Input boundary assertion: the `m`-flag `^` after a line terminator) and S281 (MDN Lexical
  grammar: the four ECMAScript line terminators). Both are `docs`, `mined`, opened 2026-11-07, used-by
  `corpus/knowledge/row-id-reader-class.md`. L1 and scribe captures are byte-identical, and the quotes are located in the
  lesson `## Gate`.
- **Existing rows:** no `status`, `recheck` or `used-by` changes. Capture bindings for S269–S281 and the dupes pin changed
  outside the rows.
- **Unreachable, not rejected:** the GNU gawk manual (www.gnu.org:443 failed to connect, five times total).
- **Frontier:** the entry above covers new coverage-map ground: the lane's four row readers vs the census, and the
  `m`-flag record hole.
- **Mistakes mined:**
  - M100-1: three canonical/binding inputs were read after the claim line. The frozen log fails the r99 checker
    (`MISSING_CANONICAL` on its line shape, `CANONICAL_AFTER_CLAIM` when split; `close-l1/read-order-at-freeze.txt`,
    `close-l1/read-order-split.txt`).
  - M100-2: a control was frozen without its witness being drawn (→ Q94).
  - M100-3: plan prose counts the battery differently from the artifacts.
  - M100-4: two SOURCES gates red for seven rounds (→ Q95).
- **Assimilation:** none from shokuknow.
- **considerthese:** `2026-11-06.md` proposal 3 applied.

Census command before and after:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate`.
The before and after outputs (`open/census-before.txt` / `close/census-after.txt`) are byte-identical (`diff` empty):

```text
kumitate W04 S034 duplicate url stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics across scopes
kumitate W04 S068 duplicate url github.com/can1357/oh-my-pi/tree/45c35e40c46166dc726ccc52f5d27f40f2449f99 across scopes
kumitate W04 S084 duplicate url infection.github.io/guide across scopes
kumitate W04 S095 duplicate url raw.githubusercontent.com/containers/bubblewrap/v0.13.1/bwrap.xml across scopes
kumitate W04 S123 duplicate url docs.langchain.com/oss/python/langgraph/checkpointers across scopes
kumitate W04 S126 duplicate url docs.temporal.io/encyclopedia/detecting-activity-failures across scopes
kumitate W04 S247 duplicate url arxiv.org/abs/2212.06118 across scopes
kumitate W04 S271 duplicate url git-scm.com/docs/gitrevisions across scopes
kumitate ok /home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/SOURCES.md
exit=0
```

## Trend verdicts

- **expansion: improved.** A new S280/S281-grounded knowledge entry covers the four row readers vs the census and the
  record-axis hole, with a map row. SOURCES went 217→219.
- **quality: improved.** The two remaining JS-`\s` readers now agree with the census on every drawn class: counter HELD ×4,
  CriticC 2334/2334. Selftests went 21→99 cases with teeth (REMUT 15/15, 18/18, 2/2). Two long-red SOURCES gates now pass.
  No admitted entry failed re-check.
- **discernment: improved.** Q94 (control witness) and Q95 (gate battery) each have a lesson and a failing-before receipt.
  The r99 outside finding (used-by split) stays routed rather than folded in. The 14 HELD constructions, the K99 draft fix
  and section-scope parity are explicitly rejected. The current outside spot-check is pending closure; dispatched seats are
  not credited as independent judgment.

## Round shape

- **Wave:** ONE v1 wave w1 of 12 seats: executor 3, scribe 2, scout 1, connector 1, reviewer 1, critic 3, mutation-tester 1.
  Attack seats are 5/12 = 42 %.
- **Totals:** 0 dead seats, no residual call, round total 12.
- **Planner:** the L1 held the planner seat.

## Notes

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none.
- **L0:** no new questions. Open and routed around: `kumitate | round-99` (used-by path parts) and `kumitate | round-96`
  (census CR).
- **Misroot sweep** (`close-l1/misroot-sweep.txt`): 0 moved. Fleet-root `f.txt` (content `x`, written inside this wave's
  window) names no lane, so it is not attributable and was left in place.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — cite-sources/source-capture registry rows updated at `173a5314` (`SKILL.md:628`, `SKILL.md:634`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 100` (frozen counter HELD at M2, `close/probe-m2-1.txt`).
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/row-id-reader-class.md` recheck command; `close/battery-final.txt`.
- [ ] No cross-domain bleed (PROVINCE.md still accurate)
