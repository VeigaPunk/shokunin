# tabi — round 84

Claims declared (2): **C1** coverage — capability `chromium-showpicker-linux` generation r84
(cross-origin `type=tel`/`search`/`text` SecurityError legs, every r83 leg carried); **C2**
calibration — record drift (the eight routed defects of the r83 non-author spot-check).

Lane base `a5d6ffbf`; freeze commit `84ebfa95`, identity commit `d90b7f55` (D1
`a5bdb15ec9a7`); final **D `31fc14c29f84`**, nonce **`tabi-r84-l1-31fc14c29f84`**; round commit
**`0837866a7525a38bc669fcc2a0e0625b0b610741`** (pushed; `ls-remote` shows it).

## Work performed

- **C1 — generation r84 (coverage).** The driver `scripts/chrome-cdp-showpicker-round84.mjs`
  (18 legs, one fresh browser per leg) adds cross-origin `#te` (`type=tel`), `#se` (`search`),
  `#tx` (`text`) with child buttons `#go12`–`#go14`; each child script calls `showPicker()` and
  the receipt records `childResult`, `childActivation{Before,After}`, `childEvents`,
  `parentCrossAccess`, `childLate`, and zero `Page.fileChooserOpened` per leg
  (`corpus/evidence/round84/chromium-showpicker/receipt.json`, nonce
  `tabi-r84-l1-31fc14c29f84`). Evidence: receipt legs 12–14 quoted in
  `corpus/knowledge/chromium-showpicker-runtime-round-84.md` §The measured laws.
- **C2 — record drift (calibration).** `corpus/lessons/round-84.md` §Corrections carries the eight
  routed defects with directional pairs (accept extension token, 8-byte-signature PNG, Scout row
  polarity, Review2 cross-origin narrowing, 69/41 counts, reverse control withdrawn, SKILL 84→153,
  census/erratum/Gate reconciliation); the r83 note gained an append-only `## Erratum` (commit
  `0837866a`). Counter `scripts/check-record-drift-r84.mjs` reads both the lesson and the note.
- **Wave w1 (one v1 wave, 10 seats, 4 attack roles).** spec/dispatch/ready committed under
  `.ufo/waves/round-84/`; `w1-results.json` records all ten seats settled, no dead seats. Findings
  reconciled below and in `plans/round-84.md` §Narrowings.
- **Re-freeze history.** D1 `a5bdb15ec9a7` (commit `84ebfa95`) was superseded by the battery repair
  that R84Review2/R84Mut1 measured: the D1 battery failed the honest receipt (156 cases, 3 failed,
  coverage 74/80 — no refusal case for the three new leg ids). D2 `31fc14c29f84` adds the three leg
  mutators, three `*-law` cases, two field witnesses and the `LEG_ALSO` entry (battery pin
  `42fcfedc…`), and the drift counter was strengthened (note/erratum reads, `laws8` gate, knowledge
  count, r83 family retention) before any post-amendment scoring. The D1 receipt was re-executed at
  the D2 nonce and the old one is superseded, never edited. Driver and picker counter are byte-identical
  to D1 (`f436b229…`, `e88e9fc7…`), so the leg evidence is the same generation.
- **Wave findings.** R84Review1 confirmed 80 checks clean and measured that the three new legs are
  not distinguishable from the other SecurityError legs (one distinct `childResult`/
  `parentCrossAccess`/`childLate` across ten); R84Review2 measured 32/159 battery cases firing an
  allowlisted collateral and the D1 pin drift; R84Critic measured the no-work control (r83 receipt →
  exit 1, 48 findings), the 31-event escape minimum, and the D1 drift counter's reach; R84Mut1 ran
  123 independent mutants with 51 case-level survivors; R84Connector pinned 20 siblings, 0 contested;
  R84Scout re-opened S219/S220/S223 byte-identical and found the spec agrees with all three legs;
  R84Exec1 two cold runs clean at 80/80; R84Exec2 the C2 before/after/control; R84Exec3 the D1
  battery/killpower/selftest run (recorded, superseded); R84Scribe drafted the note, the erratum and
  the lesson, whose content the L1 integrated and re-measured.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Driver `scripts/chrome-cdp-showpicker-round84.mjs` (18 legs) | `LOG.md` §Round 84 | `0837866a` |
| Counter / battery / kill power / selftest / drift counter (`scripts/*r84*`) | `LOG.md` §Round 84 | `0837866a` |
| Knowledge note `corpus/knowledge/chromium-showpicker-runtime-round-84.md` + r83 note erratum | `LOG.md` §Round 84 | `0837866a` |
| Lesson `corpus/lessons/round-84.md` (Gate, Mistakes, Corrections) | `LOG.md` §Round 84 | `0837866a` |
| `SCORECARD.md` §Round 84 (two claims, capability row, narrowings, planned r85) | same | `0837866a` |
| `SKILL.md` §Round 84 gate registry + r83 battery 84→153 correction | same | `0837866a` |
| Wave evidence `.ufo/waves/round-84/**` (spec, dispatch, ready, w1 reports, scored outputs, census, ledger) | same | `0837866a` |
| Receipt `corpus/evidence/round84/chromium-showpicker/receipt.json` | same | `0837866a` |

## Before → after measurements

**C1** — counting command (frozen predicate `C1-SHOWPICKER-R84`):

```
node scripts/check-showpicker-r84.mjs --lane /home/vgpnk/Projects/shokunin/tabi-shokunin \
  --receipt corpus/evidence/round84/chromium-showpicker/receipt.json \
  --expect-driver-sha256 f436b229df3a9194f074d9489dbeed54a24081afaae3d3027ff46aad4198807e \
  --expect-nonce tabi-r84-l1-31fc14c29f84 \
  --expect-fixture-sha256 da8178f1f46731ade566ce023f4e71b1cc64b4ed0b9dd92e76d73fc11cb5df18 \
  --prior-set .ufo/waves/round-84/controls/c1/prior-set.txt --json
```

- before (`a5d6ffbf`): no r84 receipt → exit 2 `receipt-unreadable`; the r83 receipt under the r84
  counter → exit 1, 48 findings (schema, plan, 15 unknown legs, laws) — `w1/R84Critic.md` §2.
- after (`0837866a`): **exit 0, `verdict clean`, checkCount 80, findings []**
  (`.ufo/waves/round-84/scored/counter-a.json`); battery **162 cases / 0 failed / coverage 80/80**
  (`scored/battery-a.json`); kill power **50 mutants / 50 killed / 0 survived / 0 crashed**
  (`scored/killpower-a.json`); selftest **9/9** (`scored/selftest.out`); two independent cold runs
  80/80 (`w1/R84Exec1.md`).

**C2** — counting command: `node scripts/check-record-drift-r84.mjs --lane <ABS lane> --json`.

- before: exit 1, **8 mismatches** on a clean mirror
  (`.ufo/waves/round-84/w1/c2-before.json`: `r83-accept-correction`, `r83-png-correction`,
  `falsification-scout`, `record-counts`, `r83-numbers`, `census-artifacts`, `r84-identity`,
  `r84-numbers`).
- after: exit 0, **0 mismatches** (`w1/R84Exec2.md` AFTER leg and the L1 run at `0837866a`);
  control: the corrected mirror with one stale rewrite exits 1 on `r83-accept-correction`
  (`w1/c2-control.json`).

**Narrowings (all recorded in `plans/round-84.md`).** (1) The three new legs bind the fixture
descriptor's `type` and the law tables, not a distinct Chromium branch (R84Review1). (2) Kill power
50/50 covers the frozen mutant list only; R84Mut1's 51 case-level survivors (message pin, `childLate`,
child event seq, `parentCrossAccess`, loop deletion) are routed to r85. (3) C2's predicate does not
reconcile the r83 spot-check's Gate `0/0/0/0` vs `5/5` prose and `claim-count-stable` is vacuous
(R84Critic, R84Exec2). (4) Battery cases witness "refused", not "this conjunct fired" (32/159 cases
fire an allowlisted collateral — R84Review2).

## Sources & frontier

SOURCES: unchanged — 0 new rows. Census start and end both exit 0, 223 rows
(`.ufo/waves/round-84/census/{start,end}.txt`; command
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`).
Rows touched old→new: none; carried rows S219, S220, S223 re-opened by R84Scout with byte-identical
sha256 (`w1/R84Scout.md`; 687,515 B spec page, decoded Chromium file sha256 `405b52c7…`) and
`used-by` unchanged (no row appended). Rows added by tier: none. Frontier advanced: the r83 note's
named frontier `type=tel`/`search`/`text` moved to core as measured legs; the accept MIME-token and
`image/*` grammar (S223) and a same-origin tel/search/text contrast stay frontier.
Assimilation: none (`merge/tabi/` adoption stays closed pending the open L0 `tabi | round-57`);
`considerthese/`: no such directory in this lane.

## Trend verdicts

- **expansion: improved** — a new knowledge entry (`chromium-showpicker-runtime-round-84.md`, 97
  entries from 96) and three new measured legs on ground the r83 note named as frontier; the
  capability row carries generation r84 (`SCORECARD.md` §Round 84).
- **quality: improved** — 80 checks clean (from no r84 receipt), battery 162/162 (from the D1
  battery's 3 failures / 74-80 coverage, measured by two seats), kill power 50/50, selftest 9/9, and
  the r83 note's overstated clauses corrected in an append-only erratum that the drift counter reads.
- **discernment: improved** — the round's own wave falsified three wordings it had declared (leg
  distinctness, kill-power reach, case coupling) and each was narrowed in the plan before filing; the
  D1 freeze gap was caught by two independent seats and fixed by a recorded re-freeze rather than
  hidden; the C2 counter was strengthened where the critic showed it could pass with the note absent.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md`
  §Approval table, §Evidence ladder, §Runbook, `## Round 84 gate registry` (`SKILL.md:3300`).
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  `corpus/knowledge/chromium-showpicker-runtime-round-84.md` (18-leg generation) and `LOG.md` §Round 84.
- [~] Instructions executable by an agent without oral context —
  `corpus/knowledge/chromium-showpicker-runtime-round-84.md` `recheck:` command (exit 0, 80 checks)
  plus `w1/R84Exec1.md`'s independent cold runs.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:3-19`; `w1/R84Connector.md`
  (20 siblings, 0 contested on this surface, nothing absorbed).

## Round extras

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none (node 24 and the system Chromium served every run; no pacman transaction).
- **Pre-file falsification:** `PREFILE-FALSIFICATION:` line pasted below.
- **Wave shape:** one v1 wave, 10 seats, 0 dead. Roles: 3 executors, 2 reviewers, 1 critic, 1
  mutation-tester, 1 scout, 1 scribe, 1 connector = 4 attack seats (40 %). Planner seat held by the
  L1 (validator forbids a planner item). Round total 10 seats; no residual call.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed no
  lane-written stray at the fleet root.
