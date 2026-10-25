# KengakuLiveAnchors — advisory remeasure

Seat: scout, report-only. Not a native judge verdict, not a lane round report, not a gate receipt, not an admission. No lane file was edited. `grader.py` was not run (pre-wave receipt already holds the gate output; this wave forbids member gate runs).

Lane revision measured: `d84e48d525d6af6b1d137d608aea8c726f8bead4` (`round-15: OMP/ufo-fsd re-census — substrate drift does not reach this lane`). Lane porcelain: `?? plans/` only (parent plan; not this seat).

Source revision measured: `964f443ee53df0ce06bd689af01f0dea031b01f9` on `main`, subject `routing: regenerate omp-seat-routing mirror from the live global config (operator: ompskills host apply)`, committer date `2026-10-12 18:32:12 -0300`. Checkout is shallow (`git rev-parse --is-shallow-repository` → `true`; reachable `rev-list --count HEAD` → `3`; `.git/shallow` has 30 boundary hashes). Worktree is dirty, 5 modified paths, 0 deletions vs HEAD: `README.md`, `config/ufo.json`, `crates/ufo-core-runtime/bundled/config.json`, `crates/ufo-core-runtime/bundled/omp-seat-routing.json`, `scripts/fleet-dispatcher.test.mjs`. No live kengaku claim cites those paths, so the dirt is source state, not a lane anchor. Contents were not read.

Resolved source path: `/home/vgpnk/Projects/shokunin/../ufo-fsd-alpha` → `/home/vgpnk/Projects/ufo-fsd-alpha`. `/home/vgpnk/Projects/origin-work` and `/home/vgpnk/Projects/origin-work/ufo-fsd-alpha` are absent. No second `ufo-fsd-alpha` checkout under `/home/vgpnk/Projects` (depth 3).

## Inventory

Live OMP-derived claims are the round-15 pins in `SCORECARD.md:186-200` and `LOG.md:22`, plus the host-path sentences at `SCORECARD.md:205-207` and `:217`. A sweep for other live line/symbol/count/hash pins into the source tree found none.

Commands and results:

- Search for `ufo-fsd`, `origin-work`, `--src`, `UFO_SRC` in the lane: hits are the round-15 census text, `PROVINCE.md:55` (read-only policy sentence, no line/symbol/count/hash), `corpus/evidence/round10-fleet/INTEGRATOR-NOTES.md:72` (same policy class), and `corpus/evidence/round14-fleet/r14-scout-surfaces.md:137,148` (historical neighbour notes, not ufo-fsd paths).
- Search for `crates/`, `.rs:`, `ufo-core`, `omp-seat`, `maxConcurrentL1`, `fleet-dispatcher` in the lane: no source-file citations. The only `--src` strings are the round-15 denial that the gate has one.
- `grader.py:5665-5681` argparse flags are `--selftest`, `--selftest-r12`, and the four in-repo evidence path groups. No `--src`, no `UFO_SRC`, no origin-tree default.
- Deleted-path cross-check: 970 paths from the tree diff below were sought as full paths in 186 decoded lane files. Path hits = 0. Basename hits for names of length ≥ 16 = 0. Targeted search for `atomic-write`, `charter-scribe`, `refusal-line`, `collect-omp-native`: 0.

So there is no live file:line or symbol pin into OMP source to drift. The live claims are path, hash, and count pins about the source tree itself.

## Claims

| ID | Where | Claimed | Command and measured output | Class | Proposed anchor |
|---|---|---|---|---|---|
| H1 | `SCORECARD.md:187`, `LOG.md:22` | HEAD `964f443e` | `git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD` → `964f443ee53df0ce06bd689af01f0dea031b01f9`. `git rev-parse 964f443e` resolves that same object (abbreviation unambiguous). `git merge-base --is-ancestor 964f443e HEAD` exit 0. | Holds at the commit. Not line drift. | Full hash above. Pin the commit, not the dirty worktree. |
| P1 | `SCORECARD.md:186-187`, `:217` | New tree `~/Projects/ufo-fsd-alpha` resolves | `test -d` true; `readlink -f` → `/home/vgpnk/Projects/ufo-fsd-alpha`. | Holds. | That absolute path plus H1. |
| P2 | `SCORECARD.md:186-187`, `:205` | Old tree `~/Projects/origin-work/ufo-fsd-alpha` and `~/Projects/origin-work/` absent | `test -d` false for both. | Absence holds. | Record absence only. |
| P3 | `SCORECARD.md:186-187`, `LOG.md:22` | Substrate relocated from `origin-work/ufo-fsd-alpha` | Current disk shows new present, old absent. It does not show that the old path ever held this repo. `r14-scout-surfaces.md:137` names `origin-work/` as a directory neighbour of `the-bounty-hunter`. `:148` names `origin-work/open-bug-bounties/` at `1307b8b6f8361cfa338de9bee903f4810020f320`. Neither line names `ufo-fsd-alpha`. | Not line drift. From-clause is unprovable on current surfaces, not a falsified current path. | Keep P1/P2. Mark the from-clause historical and unmeasured. Do not pin it as a current relocation fact. |
| C1 | `SCORECARD.md:187`, `LOG.md:22` | `~50` upstream files deleted | No counting command is stored with the number. Reachable history: name-status `D` count → 0; `rev-list --count HEAD` → 3. Local object `5725fa7d3ebdc6fe6e9cc07ed81999f8863dca70` exists (`cat-file -t` → commit, 2026-09-28) but `merge-base --is-ancestor 5725fa7d3 HEAD` is false, so it is not a parent on the reachable line. `git diff --name-status 5725fa7d3 HEAD` → 176 A, 970 D, 829 M. D by top directory: reports 735, tests 115, scripts 41, packages 32, drills 20, crates 9, substrates 7, conformance 3, other 8. D excluding `reports/` = 235. D under scripts/tests/crates/packages/conformance/drills = 220. None of those slices is 50. Three paths present at the pin and absent at HEAD: `scripts/atomic-write.mjs`, `scripts/charter-scribe/sync.test.mjs`, `scripts/collect-omp-native-handoff-lib/refusal-line.mjs`. | Genuine defect in the live count, not line drift. The number is uncommanded, and both available measurements contradict it (reachable D = 0; non-ancestor tree diff D = 970). Do not replace `~50` with 970: ancestry is unproven, so 970 is a tree delta, not a commit-range deletion count. | Withdraw the count. Anchor the two commands above and the non-ancestry caveat. Specific absences may be cited only per path, with the pin and HEAD. |
| G1 | `SCORECARD.md:188-189`, `LOG.md:22` | Gate has no `--src` and no origin-tree I/O | `grader.py:5665-5681` has no such flag. Search of `grader.py` for `--src`, `UFO_SRC`, `ufo-fsd`, `origin-work`: no matches. Defaults are in-repo evidence paths. | Holds. Stale-`--src` class for this lane is 0. Not a gate defect. | No code change. GateRepair should leave `grader.py` untouched. |
| N1 | `SCORECARD.md:196` | `grep -rln 'origin-work' . --exclude-dir=.git` → 1 hit, `r14-scout-surfaces.md` | `git grep -l -I -e origin-work` at lane HEAD returns 3 files: `LOG.md`, `SCORECARD.md`, `corpus/evidence/round14-fleet/r14-scout-surfaces.md`. The extra two exist because the census text contains the search term. | Genuine defect in the live command-result pin, not line drift. The r14 lines still say what the scorecard says they say. | Re-scope the command, or record 3 files and state that the only pre-census observation is `r14-scout-surfaces.md:137,148`. |
| T1 | `SCORECARD.md:198-200` | Taxonomy (a) stale `--src` 0, (b) citation-to-deleted 0, (c) line drift 0, (d) genuine lane defect 0 | (a) holds: G1. (b) holds: 0 of 970 deleted paths cited in 186 lane files. (c) holds: no live OMP file:line pin exists, so none drifted. (d) does not hold: C1 and N1 are genuine defects in the census text. | (a)(b)(c) hold. (d) is a genuine defect of the census's own count pins, not of a source-line citation and not a gate defect. | Erratum: (d) is 2 (C1, N1), both calibration/count pins. Do not reopen (a)(b)(c). |

`5725fa7d3` was taken from a sibling note only as a candidate object id, then resolved and diffed locally. The sibling's deletion count was not used as a result.

## Proposed delta

Not applied. This seat does not own `SCORECARD.md`, `LOG.md`, or `grader.py`. No gate implementation change: G1 is not a remaining defect.

Parent / HistoryClaims, append-only, do not rewrite round-15 bytes:

- H1 holds at `964f443ee53df0ce06bd689af01f0dea031b01f9`. Worktree was dirty on the five paths named above; the pin is the commit.
- P1 and P2 hold. P3's from-clause is unmeasured; `r14-scout-surfaces.md` does not observe `origin-work/ufo-fsd-alpha`.
- Withdraw `~50`. Record reachable D = 0 and the non-ancestor tree diff D = 970. Do not install 970 as a branch deletion count.
- N1's command now lists 3 files. Pre-census observation remains the r14 file only.
- T1 (d) is no longer 0. (a)(b)(c) stay 0.

No source repair. No `--src` patch. No re-pin of grader expected values.

## Unresolved debt

- Deletion magnitude on the reachable line cannot be recovered here. The clone is shallow, `5725fa7d3` is not an ancestor, and fetching is out of scope. Unblock: do not fetch; do not pin a count; if a non-shallow local history appears later, kumitate remeasures its own registry, kengaku does not.
- Source worktree dirt (5 modified paths) is unowned by this lane. No current kengaku anchor depends on it. A later line citation against those files must say commit versus worktree.
- `:34113` absence is already named operator-side debt in `SCORECARD.md:208-216`. It is not an OMP line/symbol/hash claim and was not re-probed.

## Cross-domain owner

- Upstream file census, registry members, and any `--src` default: kumitate. Kengaku cites none of the absent paths.
- Relocation narrative for `origin-work/ufo-fsd-alpha`: unowned on current kengaku evidence; do not absorb it as a measured kengaku fact.
- Append-only erratum for C1, N1, P3, T1(d): parent integrator / HistoryClaims. This seat did not write it.
- Gate files: GateRepair. No change recommended.
