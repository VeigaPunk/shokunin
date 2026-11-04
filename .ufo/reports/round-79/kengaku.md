# kengaku — round 79 (hyaku run 15, attempt 1, 2026-11-04)

Lane: `kengaku-shokunin` (LLM/model research & evaluation; axes **novelty + calibration**).
Base `660ec0b9`; lane tip `f10a2678` (`git -C kengaku-shokunin ls-remote origin refs/heads/master`
prints it). Two claims, both admitted; one v1 wave of 14 seats; no residual call.

**Declared claims.** **R79-C1 / coverage** (lowest non-retired axis, L0-capped at 7) — the whole
16-class Terminal-Bench 2.0 grader population (88 members, 230 member-class pairs) becomes a
machine-checked member ledger. **R79-C2 / calibration** (held at ceiling 10, exercised) — the
round-78 closure's seven routed defects are discharged with checks that fail at the base revision.

## Work performed

- **R79-C1 — the 88-member population ledger.** `plans/grader-population-ledger.json` prices every
  member of `corpus/evidence/round62/class-survey.txt` exactly once: 18 `executed` (a tracked receipt
  that locates the member in one of five frozen subject shapes and carries execution observations),
  6 `executed-unlocated` (the round's probe instrument names the member, a receipt under that round
  carries observations, the receipt does not locate its subject — the `no-subject-stamp` debt is
  named), 64 `unexecuted` (7 with a blocker whose frozen detector fires over that task's own
  `tests/test_outputs.py`: 2 `browser-required`, 1 `vm-required`, 1 `external-db-required`,
  3 `candidate-library-required`; 57 the honest `unattempted` default). Counter
  `plans/round79_c1_population_ledger.py` (freeze `5d684313`); after receipt
  `corpus/evidence/round79/c1-after.txt` → `DEFECTS n=0`, rc 0.
- **R79-C1 — the 16 SKILL.md class rows become derived.** Every row of §Decision table now carries
  `executed k of n` (previously 13 rows said a bare `executed`, one said `recipe-unexecuted`) plus the
  ledger pointer paragraph; `SKILL.md:70-86`. The counter re-derives each cell from the ledger
  (`CLASS-K-MISMATCH` otherwise).
- **R79-C1 — three losing controls** (`corpus/evidence/round79/c1-control-namegrep.txt`,
  `-default-reason.txt`, `-all-blocked.txt`): the name-grep skip reaches `executed=88` and dies on
  `RECEIPT-POPULATION` ×88 (the census receipt mentions every member); the default-reason skip dies on
  `REASON-UNDERSTATED` ×7; the all-blocked skip dies on `REASON-UNBACKED` ×62.
- **R79-C1 — attack-driven Amendment A1.** The wave's critic, mutation-tester and sentinel proved the
  first counter accepted evidence it had not established; six defect classes were added before the
  after receipt was re-measured (`plans/round-79-claims.md` §Amendment A1, commit `e560695c`):
  `RECEIPT-POPULATION` in the unlocated branch, `UNLOCATED-FOREIGN-MEMBER`, `GRADER-ABSENT`,
  `EVIDENCE-SHA-MISMATCH`, `EVIDENCE-NOT-VERBATIM`, `LEDGER-DUPLICATE-KEY`. Verified against each
  attack: the critic's 88-docstring-instrument ledger now prints `RECEIPT-POPULATION` ×64 instead of
  `replayed=88`; the zero-hash ledger `EVIDENCE-SHA-MISMATCH` ×57; the removed-bodies ledger
  `GRADER-ABSENT` ×64; `M02` `EVIDENCE-NOT-VERBATIM` ×2; `M06` `LEDGER-DUPLICATE-KEY`.
- **R79-C1 — provenance is reported honestly, not inflated.** `COVERAGE` prints `covered=15
  covered_located=13`: `signal-delivery` (1 of 1) and `numeric-band` (2 of 10) rest on unlocated
  attribution alone (the critic's independent derivation, `CriticC1R79` §2). The claim is the
  population map, not 15 execution-backed classes.
- **R79-C2 — seven closure defects discharged.** `corpus/routed-findings.jsonl` gains `R78-D1` …
  `R78-D7`, each with `verified_at`, a `close_commit` ancestor, `evidence_path` + `evidence_literal`
  that resolve at that commit, and a `check` that fails at `660ec0b9`. Gate
  `plans/round79_c2_closure_debt.py` (freeze `5d684313`); after receipt
  `corpus/evidence/round79/c2-after.txt` → `TARGET ids=7 closed=7 checks_passed=7 indexed=yes`,
  `DEFECTS n=0`.
- **R79-C2 — repair-sensitivity leg (Amendment A1).** `ReviewerC2R79` showed a recap file plus
  `test -f` reached the target; the gate now re-runs every `check` in a copy of the tree with the row's
  evidence file reverted to its `660ec0b9` bytes and requires the check to fail there
  (`CHECK-NOT-REPAIR-SENSITIVE`), plus `EVIDENCE-LITERAL-ABSENT`. Residual limit stated: a presence
  gate cannot prove a semantic repair; the non-author closure is the authority for that.
- **Repairs D1–D6 landed** (D7 is the index + registration above): the per-class split correction
  re-derived from `corpus/evidence/round78/c2-before.txt` (`11 TOOL-UNNAMED, 11 COMMAND-ABSENT,
  5 PASS-UNLOCATED, 2 WORKTREE-ABSENT`, `TOOL-UNPINNED` never fires); the two round-77 rows now read
  `stamped cd2e25bb, clean` (`SCORECARD.md:3564-3565`); the at-tip rerun block quotes
  `corpus/evidence/round79/routed-open.txt` (`ROWS total=105 open=31 blocked=1 closed=71 refused=2`);
  the S254/S255 citation metadata is corrected in the lesson; the base-redness paragraph is restated
  with R75-C1/R76-C2 as the red gates; the gate block was re-run in a clean clone
  (`corpus/evidence/round79/gates-clean.txt`, `WORKTREE clean`, 12/12 `EXIT 0`).
- **Gate integration.** The two counters are registered in `SKILL.md` §Gate/probe registry (128 rows,
  `MISSING 0`, `SELFTEST-UNBACKED 0`); `round78-c1-class-member-ledger` is **retired** there
  (superseded by the population ledger — its universe rule now selects the 88-member population; its
  round-78 verdict stands at `148801a6`, re-verified in `gates-clean.txt`); `SF14` re-pinned 247 → 249
  and the `PROVINCE.md` count row re-pinned with it; `corpus/README.md` gains the round-79 lesson row,
  the round-78 spot-check row and the `evidence/round79/` index row.
- **Misroot sweep** (`git -C /home/vgpnk/Projects/shokunin status --porcelain`, no pathspec): 7 entries,
  all `.scratch/*` (orchestrator-owned) plus an untracked `after` file dated 2026-11-03 20:05 that names
  no lane or round — **0 files from this round's seats**; nothing copied, nothing deleted.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| freeze: claims, two counters, 88-member ledger, 16 class rows, before receipts, three controls | round 79, bullets 1–2 | `5d684313` |
| integration: lesson, SOURCES S256/S257, SCORECARD round-79 section, routed rows, index rows, wave spec | round 79, bullets 1–6 | `42d9d60a` |
| gate integration: registry rows, R78-C1 retired, SF14/PROVINCE re-pins, evidence index, at-tip routed-open + census receipts | round 79, bullets 3–6 | `e2d418ca` |
| routed rows closed: `verified_at`/`close_commit`/evidence fields for D3/D6 | round 79, bullet 3 | `dd302f48` |
| Amendment A1: six C1 defect classes, the C2 sensitivity leg, `covered_located`, receipts re-measured | round 79, bullets 1–2 | `e560695c` |
| clean-tree gate block at `e560695c` (12/12 `EXIT 0`) | round 79, bullet 3 | `5302b92a` |
| wave evidence: spec, dispatch, results, 14 seat reports | round 79, header | `f10a2678` |

## Before → after measurements

**R79-C1** — counting command `python3 plans/round79_c1_population_ledger.py --lane .` (before:
`--rev 660ec0b9`). Before (`corpus/evidence/round79/c1-before.txt`, rc 1): `UNIVERSE classes=16
members=88 pairs=230`, `LEDGER rows=0`, 88 `MEMBER-UNACCOUNTED`, 13 `CLASS-ROW-UNQUANTIFIED`,
`LINK-ABSENT`, `DEFECTS n=105`, `TARGET … unaccounted=88 covered=0`. After
(`corpus/evidence/round79/c1-after.txt`, measured at `5302b92a`, rc 0): `LEDGER rows=88 executed=18
unlocated=6 unexecuted=64`, `COVERAGE replayed=24 covered=15 covered_located=13
uncovered=container-image census_covered=12`, `DEFECTS n=0`, `TARGET classes=16 members=88 pairs=230
replayed=24 located=18 unlocated=6 unexecuted=64 unaccounted=0 unbacked=0 understated=0 covered=15`.
Batteries: `SELFTEST cases=16 red=15 failures=0`, `MUTANTS real=6 killed=6 survived=0`, three controls
`target_reached=False`.

**R79-C2** — counting command `python3 plans/round79_c2_closure_debt.py --lane .` (before:
`--rev 660ec0b9`). Before (`c2-before.txt`, rc 1): 7 `DEBT-UNREGISTERED` + `INDEX-MISSING`,
`DEFECTS n=8`, `TARGET ids=7 closed=0 checks_passed=0 indexed=no`. After (`c2-after.txt`, measured at
`5302b92a`, rc 0): `DEBT-TOTAL ids=7 registered=7 closed=7 checks_passed=7`, `INDEX … indexed=yes`,
`DEFECTS n=0`, `TARGET ids=7 closed=7 checks_passed=7 indexed=yes`. Batteries: `SELFTEST cases=9 red=8
failures=0`, `MUTANTS real=4 killed=4 survived=0`, `CONTROL presence target_reached=False`. Every
`check` also fails at `660ec0b9` (sensitivity leg, `CHECK-NOT-REPAIR-SENSITIVE` would fire otherwise).

## Sources & frontier

- Registry **247 → 249** rows: `grep -cE '^\|\s*S[0-9]{3,}\s*\|' corpus/SOURCES.md` → `249`
  (before: 247 at `660ec0b9`). Census
  `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku` → rc 0 at round
  start (`corpus/evidence/round79/census-before.txt`) and rc 0 at round end
  (`census-after.txt`), 25 `W04` duplicate-URL warnings unchanged in both.
- **Rows added, by tier:** 2 × tier A — **S256** (Terminal-Bench 2.0 harness README at the pinned tree,
  opened live 2026-11-04: HTTP 200, 4 574 bytes, sha256 `7dfa9992…d972364`, capture
  `corpus/evidence/round79/sources/tb2-readme.md`, located quote at capture line 24, 22 words: "…to
  perform valuable work in containerized environments"; the row grounds only the containerized-run
  premise, not the package/service inference — the `SourcesScribeR79` narrowing is folded in) and
  **S257** (`own-work`: the population ledger + the round-62 census receipt it expands, sha256
  `ee30c698…`).
- **Rows touched old→new:** S256 absent → `mined` / `2026-11-04` / `on-release`; S257 absent → `mined`
  / `2026-11-04` / `90d`. No existing row's status, recheck or used-by changed.
- **Frontier rows advanced:** the class-replay frontier moved from 12 priced members over 3 classes to
  88 members over 16 classes (24 replayed, 15 classes with a replay claim, 13 with a located one);
  the `unattempted` set (57 members) is the named next-round frontier, and the six
  `executed-unlocated` receipts are re-mintable (all six probes re-run today; five writers stamp only
  `REV`, `protein-assembly`'s writer has no `--receipt` — `RosterScoutR79`).
- **Sourced claim:** R79-C1's blocker taxonomy rests on S256 (opened this round).
- **Assimilation: none.** `/home/vgpnk/Projects/shokuknow/merge/kengaku/` not adopted; the mass id
  drift stays open at L0 `kengaku | round-54`. `considerthese/2026-10-26.md`: proposal 1
  (routed-findings burn-down) is implemented and used for the seven ids; proposals 2 and 3 stay open.

## Trend verdicts

- **expansion: improved.** Two capability rows enter `SCORECARD.md` with a demonstrated command and a
  committed receipt (`grader-population-member-ledger`, `closure-debt-discharge`), the population the
  lane can price grows 12 → 88 members, and the registry gains two opened, tiered, cited rows
  (S256 live-verified, S257 hash-verified). No new `corpus/knowledge/` entry — declared, not hidden.
- **quality: improved.** Twelve gates that were green at `42d9d60a`'s predecessor are green again in a
  clean clone at `e560695c` (12/12 `EXIT 0`, `grader.py` `CHECKS n=733 mismatches=0`), one superseded
  gate retired with its own-tip verdict re-verified, two evidence defects (missing bodies, unverified
  hashes) closed by defect classes, and the round's own receipts re-measured after the amendment. The
  residual limit is named: a presence-based closure gate cannot prove a semantic repair.
- **discernment: improved.** The wave's attack seats changed committed bytes: six defect classes and a
  sensitivity leg exist because the critic, mutation-tester and sentinel found the seams, and the
  critic's independent `covered_located=13` is now a printed number rather than a footnote. Two
  disagreements stand on record and are *not* repaired (they are honest limits, not defects): a
  zero-replay filler ledger passes the frozen target (the claim is a map, not new execution), and the
  `unattempted` default is an absence, not a proven blocker.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:70-86`
  (16 derived class rows + ledger pointer), `SKILL.md:720-723` (two new gate rows, one retirement).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round-79 block,
  bullets 1–3, with `corpus/evidence/round79/c1-after.txt` / `c2-after.txt` / `gates-clean.txt`.
- [~] Instructions executable by an agent without oral context — `plans/round-79-claims.md` (frozen
  predicates, controls, kill rules) + `corpus/lessons/round-79.md` §Gate.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `ConnectorR79` matrix: 0 duplicate artifacts
  across the live sibling lanes; the closest analogues (audio, chousa, game-dev-3d) are adjacent, not
  identical; `PROVINCE.md:1041` count row re-pinned this round.

**Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
**Tool installs:** none this round (no `pacman`, no `uv tool`, no `npx` install; the seat that needed
`selenium` reported the channel without installing).

## Round shape and seats

One v1 wave (`kengaku-r79-w1`, policy band 8–16), **14 seats, 0 dead**, no residual call — round total
14. Roles: executor 5 (`C1ReplayR79`, `LedgerAuditA/B/C`, `C1BatteriesR79`), scribe 3
(`SourcesScribeR79`, `DebtScribeR79`, `LessonScribeR79`), critic 1, reviewer 1, mutation-tester 1,
sentinel 1, connector 1, scout 1 — attack roles 4/14 = 29 % (≥ 25 %), connector 1 (≤ 2). The §3 L2
floor (≥ 8, one batched wave) is met inside wave 1; the canonical planner seat is held by the L1
(no planner seat in the wave, per the orchestrator ruling). Dispatch evidence
`.ufo/waves/round-79/w1/{w1-spec.json,w1-dispatch.json,w1-results.json}` + 14 seat reports, committed
at `f10a2678`.

**Seat results that changed the round.** `C1ReplayR79`: independent re-derivation, `DISAGREE: []`,
18/6/64 reproduced over 1 353 tracked evidence files. `LedgerAuditA/B/C`: 88/88 rows OK, no WRONG row;
`openssl-selfsigned-cert`'s receipt prints `PREDICATE R59-C1 fail` and is correctly priced as
replayed-but-unlocated (observations, not a green probe). `CriticC1R79`: the `executed-unlocated`
seam (88 docstring instruments + census receipt → `replayed=88`), `covered_located=13`, and the
cheapest-skip control. `MutantC1R79`: 12 new mutations, 10 killed, 2 survived → both now killed
(M02/M06). `SentinelC1R79`: detector-aware bookkeeping passes without new knowledge — reported as a
frozen-target limit, not repaired. `ReviewerC2R79`: the recap-file + `test -f` attack → sensitivity
leg added. `SourcesScribeR79`: S256 scope narrowed. `RosterScoutR79`: host surfaces (browser+driver
present, qemu/nginx absent, DB artifacts absent) and six re-mintable receipts. `ConnectorR79`: 0
duplicate artifacts across the sibling lanes. `C1BatteriesR79`: all batteries reproduced
(`cases=13 red=12` at the freeze counter; `16/15` after A1). `DebtScribeR79`: base-failing checks per
id. `LessonScribeR79`: the M79-1 row and the Gate block.

**Inherited state.** No prior attempt of round 79 (`watchdog.log` shows the launch line only); no
uncommitted lane leftovers were inherited, and the `.ufo/waves/round-79/` tree was created this round
and is committed.

## L0 questions

None opened this round. Still open from earlier rounds: `kengaku | round-54` (shokuknow mass id
drift), `kengaku | round-63` (the round-63 pypi receipt of record stays MISS), and the coverage axis's
open-L0 cap question (unchanged, and not blocking).
