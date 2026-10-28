# kengaku — round 50 (hyaku run 11), attempt 1

Lane repo `kengaku-shokunin`, final lane tip **`d45c5bb23b5ecff7f6a069cdb17db2a5fed7bc78`** (pushed; `ls-remote
origin refs/heads/master` matches). Freeze `3b02d573…`, instrument repair `c3372a9`, C2 corrections `822f3b7`,
fence/sealed set/battery `6db0279` + `d6f2fce`, results `d45c5bb`. Claims frozen before data in
`plans/round-50-claims.md`; lesson `corpus/lessons/round-50.md`; LOG entry under `## Round 50`.

Declared claims (2): **R50-C1 novelty 7→8** — an honest-geometry instrument for the lane's fixture fence (a frozen
126-fixture population of *documented* git states, 32+18 hostile modules, a 15-row witnessed mutant floor) landed in
one command, with the fence repaired so it passes; **R50-C2 calibration 8→9** — every artifact pointer the three
self-assessment files carry resolves at the tip (`unresolved 12 → 0`). At least one claim works the lowest
non-retired axis: coverage 7 is capped by the open L0 `kengaku | round-33` decision, so C1 works novelty (7, tied
lowest, uncapped) and coverage is not claimed this round.

## Work performed

- **R50-C1 instrument.** `plans/round50_c1_verify.py` — four legs, one predicate; fixtures are rebuilt from the
  pinned population and identity-compared (`POPULATION fixtures=126 pin=b5197f94… mismatched=0`). The fence is
  decided in a **separate process** per fixture (exit 10/11/12), and fixture parents are opaque random tokens padded
  with decoys — both holes were measured by a seat this round: `R50C1CritPredicate` forged `caught=23` with an
  in-process, directory-name-keyed fence (`.ufo/waves/round-50/w1/R50C1CritPredicate.md` §Result rows A, D).
  Owner evidence: `plans/round50_c1_verify.py`; `.ufo/waves/round-50/claims/c1-control-*.txt`.
- **Honest population.** 126 fixtures = 104 battery + 22 novel documented classes; two new this round
  (`n21` separate gitdir, `n22` alternates inside d) at `plans/honest50/modules/novel50/`; builder and pins at
  `plans/honest50/` (`builder-receipt.txt`, `population.sha256`).
- **Fence repair.** `plans/fixture_fence.py` (`57adce4a…`) resolves the five over-refused documented shapes by
  containment after resolution: a `.git` gitfile whose `gitdir:` target is inside `d` (incl. worktree stores and
  their `commondir`), `objects/info/alternates` walked as a borrow graph (visited set, depth cap 4),
  `.git/FETCH_HEAD` and `.git/shallow` allowlisted behind the link-count test, `refs/replace/<40hex>`. Every prior
  refusal path stays closed. A blind critic re-measured the shipped bytes independently:
  `.ufo/waves/round-50/w1/C1CritBlind3/receipts/verdicts-against-lane-repair-57adce4a.json` (b1, b2, a two-hop
  chain all BREACH; `n17`, `n22`, plain `FETCH_HEAD` admitted; `_refs` liveness probes all BREACH).
- **Hostile legs.** `plans/sealed50/` — 18 modules: 10 L1-authored witnesses (stray symlink, outside hard link,
  unknown ref namespace, live hook, unknown `objects/info` entry, worktree-store extra entry, argv escape, junk ref
  value, store without `objects`, foreign reflog name) and 8 blind seat modules from `C1CritBlind1/3/4/6`. All 18
  are refused by the base fence too (genuine hostile cases), receipt `corpus/evidence/round50/c1-receipt.txt`.
- **Mutant battery.** `plans/mutants50/c1-mutants.json` — 15 rows, each witnessed on the shipped fence; the
  carried r49 battery (23 rows against the r49 candidate) measured `caught=4 broken=7` here and was re-derived, its
  7 unwitnessed rows dropped and listed (`dropped_unwitnessed`; witness table
  `.ufo/waves/round-50/w1/R50C1ExecMutRebase-witness.tsv`).
- **R50-C2.** `plans/round50_c2_audit.py` — frozen surface (artifact paths and 40-hex hashes in `SCORECARD.md`,
  `SHONEN.md`, `PROVINCE.md`; hash must be an ancestor of the tip), append-only `SUPERSEDED … -> target|never-landed`
  corrections, `--selftest` proves the check can fail. Corrections block: `SCORECARD.md` §Round 50 — C2 corrections.
- **Frontier.** `corpus/SOURCES.md` S173–S177 (git v2.56.0 documentation, five captures in
  `corpus/evidence/round50/`), `corpus/knowledge/fixture-honest-geometry.md`, `corpus/QUALITY.md` Q41,
  `corpus/lessons/round-50.md` (Gate: 5 admits + 1 reject; 3 Mistakes).
- **Wave.** One v2 wave of **72 seats, 34 attack roles** (policy v2 accepted; spec `…/round-50/w1-spec.json`,
  dispatch `…/w1-dispatch.json`, ready `…/w1.ready`). The inline dispatcher mounted **40** seats
  (`w1.ready.partial`, 40 entries) and 50+ seat outputs landed under `.ufo/waves/round-50/w1/`; **no
  `WAVE-DONE` marker and no `w1-results.json` were written before this round closed.** The round therefore did not
  wait for a settled falsify wave: the seat results used are the ones on disk, and the wave is reported as
  partially dispatched, not as a completed falsification wave (conformance defect, recorded here and in the lesson).
  Dead seats: not enumerable without `results.json`; no seat report claims a peer died.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| stage-1 freeze: claims, counter, C2 command, controls, 126-fixture population, carried battery | `## Round 50` | `f7281bc` |
| four control receipts + C2 before/selftest receipts | `## Round 50` | `3b02d57` |
| wave spec + dispatch evidence (72 seats) | `## Round 50` | `5c56819` |
| C2 corrections (12 pointers), S173–S177, knowledge entry, open-window record | `## Round 50` | `822f3b7` |
| counter open-window repair (module attribution; later: subprocess harness + name hiding — see note) | `## Round 50` | `c3372a9` |
| fence repair, `plans/sealed50/`, re-derived battery, Q41, lesson | `## Round 50` | `6db0279` |
| battery frozen at 15 witnessed rows | `## Round 50` | `d6f2fce` |
| scored receipt, measured outcomes, LOG, corpus index | `## Round 50` | `d45c5bb` |

Note (honesty): the subprocess-harness/name-hiding repair of the counter was made **after** `c3372a9` and landed
inside `6db0279`'s tree; its digest is `d8787b34…`-lineage (final in `d45c5bb`). The claims doc records the first
open-window repair only; the second is recorded here and in the lesson, and it left the predicate sentence, the
four leg names and the literals unchanged.

## Before → after measurements

| claim | before (command, revision) | after (command, revision) | verdict |
|---|---|---|---|
| R50-C1 | `python3 plans/round50_c1_verify.py --lane .` at `71f5f5f` with the base fence: `HONEST fixtures=126 admitted=113 refused=13`, `PREDICATE R50-C1 fail` (`.ufo/waves/round-50/claims/c1-control-do-nothing.txt`) | same command on a clean clone of `d6f2fce`: `HONEST fixtures=126 admitted=126 refused=0 error=0`; `REFUSALS total=20 clean=20 leaked=0`; `SEALED total=12 clean=12` + `SEALED total=18 clean=18`; `MUTANTS total=15 caught=15 broken=0 floor=12 verdict=met`; `PREDICATE R50-C1 pass`, exit 0 (`corpus/evidence/round50/c1-receipt.txt`) | **admitted**, novelty 7→8 |
| R50-C2 | `python3 plans/round50_c2_audit.py --lane .` at `71f5f5f`: `POINTERS total=275 paths=216 hashes=59 resolved=263 … unresolved=12`, exit 1 (`.ufo/waves/round-50/claims/c2-before.txt`) | same command at `d45c5bb` (tree of `d6f2fce` + results): `POINTERS total=279 … resolved=279 … unresolved=0`, exit 0 | **admitted**, calibration 8→9 |

Controls, all failing the predicate (receipts in `.ufo/waves/round-50/claims/`): do-nothing base fence;
`admit_all`; `refuse_all`; `keyed_names` (shape keys). No axis harmed: coverage held at 7 (cap), depth 9,
operability 8, freshness 8, adjacency 8 unchanged.

## Sources & frontier

Census command (both runs): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin kengaku` — **exit 0 at round start** (165 rows) and **exit 0 at round end**
(`kengaku ok`); rows `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` = **170**. Rows added:
5, all tier **A** (S173 gitrepository-layout, S174 git-init `--separate-git-dir`, S175 git-worktree, S176
git-replace, S177 git-fetch; captured 2026-10-28 at tag `v2.56.0`). Rows touched old→new: **none**. Rejections
added: 1 in the lesson Gate (the mutable `tbench.ai` hub, HTTP 404 on the cited path). Frontier rows advanced:
"git store geometry / fixture honesty" moved from frontier into `corpus/knowledge/fixture-honest-geometry.md`.
Assimilation: **one** `considerthese/2026-10-26.md` proposal (proposal 1, routed-findings burn-down) landed as
QUALITY Q41 + the corrections block; `merge/kengaku/` not adopted (its staged entries are benchmark facts outside
this round's internal-instrument claims — stated, not silently skipped).

## Trend verdicts

- **expansion: improved** — five opened tier-A rows and one admitted knowledge entry on ground the coverage map did
  not hold (documented git indirection shapes), plus a capability row (**honest-geometry fence counter**, first
  working round 50) in `SCORECARD.md`.
- **quality: improved** — the fence's measured over-refusal fell from 13/126 to 0/126 while all 32+18 hostile
  modules stay refused; Q41 adds a re-runnable criterion; three Mistakes rows landed with evidence.
- **discernment: improved** — the round's gate admitted 5 sources and rejected 1 with a flip condition; a blind
  seat's independent verdict matrix agreed with the shipped repair on all 10 cases it measured
  (`C1CritBlind3/receipts/verdicts-against-lane-repair-57adce4a.json`), and a second seat's forged-pass finding
  (`R50C1CritPredicate`) was turned into an instrument repair rather than a verdict. The outside (non-author,
  non-dispatched) spot-check for this round is the closure's, not this report's.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer `SKILL.md`;
  this round's knowledge lands in `corpus/knowledge/fixture-honest-geometry.md` (entry not yet folded into SKILL.md).
- `[~]` At least one end-to-end domain task executed and logged — `LOG.md` `## Round 50`; predicate receipt
  `corpus/evidence/round50/c1-receipt.txt`.
- `[~]` Instructions executable by an agent without oral context — `plans/round50_c1_verify.py` docstring +
  `plans/round-50-claims.md` re-run the scored predicate end to end.
- `[~]` No cross-domain bleed; `PROVINCE.md` still accurate — the instrument is lane-local tooling; sibling overlap
  scanned by `R50C1ConnOverlap` (report on disk), nothing absorbed.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Tool installs: none (no pacman
transaction attempted; nothing needed). Open L0 questions: none new — the coverage cap stays with the open
`kengaku | round-33` line. Inherited state: none uncommitted at close; the r49 seat's candidate fence
(`9baedf13…`, `C1ExecRepair/fence_candidate.py`) was **not** landed (it reaches `admitted=117`); the shipped repair
is the L1's, measured end to end.
