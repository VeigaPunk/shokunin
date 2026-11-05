# mori — round 97 report (L1 MoriR97, attempt 1; fresh start)

Lane repo `mori-shokunin`, branch `master`. Entering `973b2af11f41bd362163d7e29ac08286832f546b`; freeze
`dd1ae1150f53df54e7530311b2323368e3c0e5e9`; landing `e85ed91249953094b067554bfa79fcdc65791f8e`; evidence/records
`5497e6f70aaf21a38fc0140d9f7291a5571f4987`; final pushed tip `b6d034082582340a69371393d5bca25d04e05f4f`
(`git -C mori-shokunin ls-remote origin refs/heads/master` → `b6d034082582340a69371393d5bca25d04e05f4f`).

## Work performed

Declared claims (2), frozen at `dd1ae115` with every control executed and committed first:
**C1 — operability** (the gate registry at `SKILL.md`, audited by the existing `tools/mori-gate-registry.py`) and
**C2 — freshness** (lowest-scoring non-retired tier, score 5: SOURCES rows S615/S616/S623 flagged stale at r96).
Contract: `mori-shokunin/.ufo/waves/round-97/contract.md`.

- Fresh-start reads: `corpus/lessons/round-94-verifier-spotcheck.md`, `round-95-…`, `round-96-…` (MANIFEST rounds
  1334, 1339, 1348, all rejected-honest-stop). Root causes bound into the contract: r94/r95 C2 predicates a
  do-nothing control already met; r96 C2's `live == recorded` rule that a per-build page stamp can never meet.
- Pre-freeze control battery `.ufo/waves/round-97/controls-r97.sh` → `evidence/controls-r97.txt`
  (`CONTROLS_DONE unexpected=0`, committed in `dd1ae115`): do-nothing controls fail at entering (C1 `unregistered=4`,
  C2 `unpinned=3`); forgeries — eight-cell junk rows make the auditor alone green but score `targets_ok=0/4`; wrong
  selftest outcome `0/4`; missing verdict token `3/4`; a random 362,493-byte S615 copy that the digest tool
  supersedes (the r96 hole) scores `hole_guard=fail`; today's live S616 bytes score `mismatch=1`; correct pins with S623
  pointed at another live page fail on the live leg alone (`content-drift`); positive controls score `met`.
- C1 work: four registry rows appended to `SKILL.md` (section "Round97 gate registry backfill") for
  `tools/mori-cgroup-pressure.py`, `mori-drift-recheck.py`, `mori-scorecard-calibration.py`, `mori-source-digest.py`
  (landing `e85ed912`); three cells corrected in `5497e6f7` after the domain trial and review
  (`w1/Mo97ExecTrial.md`: drift re-check writes `tools/__pycache__` bytecode; cgroup `--group` path takes no leading
  slash; `w1/Mo97RevC1.md`: the `<id> unresolved` row shape).
- C2 work: `corpus/evidence/sources-r97/S615.html` (r90 ast bytes = S619's correction digest), `S616.html` (r90 tokenize
  bytes = recorded digest), `S623.html` (today's live page with only its stamp line restored to `(08:02 UTC)`; sha256
  `90ac3b25…31ad0` = recorded digest); live re-verification by the existing r66 re-check (`time-churn` ×3).
- Sourced: new row S628 (python/docsbuild-scripts README, opened 2026-11-05, pinned `corpus/evidence/sources-r97/S628.md`)
  grounds the build-churn reading; `corpus/lessons/round-97.md` `## Gate`.
- Domain trial run on real host state: the four registered tools run live on this host (`w1/Mo97ExecTrial.md`:
  cgroup PSI survey on live `/sys/fs/cgroup` → `PRESSURE_OK` rc 0; drift re-check S615/S616/S623/S577; calibration
  counter at the landing → `C1=met`; digest gate `DIGEST_CHECK rows=125 ok=92 mismatch=0 superseded=2 prefix_only=31 unpinned=0`).
- Wave `w1` falsification: replay `w1/Mo97ExecReplay.md` (both claims reproduced, controls re-run unexpected=0);
  reviewers `w1/Mo97RevC1.md` (32 cells, VERDICT C1 holds), `w1/Mo97RevC2.md` (VERDICT C2 holds); critics
  `w1/Mo97CritC1.md` (holds; residuals R1–R3 outside P1, carried), `w1/Mo97CritC2.md` (holds; one green forgery needs an
  edit of the recorded digest, excluded by the diff); mutation `w1/Mo97MutC1.md` (10/12 killed; m07, m12 defence-in-depth
  survivors), `w1/Mo97MutC2.md` (M5/M6/M9 killed by seat fixtures beyond the committed controls; M7 redundant),
  `w1/Mo97MutCalib.md` (carried r96 debt: 10/11 killed, survivor M10); stamp hypothesis `w1/Mo97RevStamp.md` (14/14 pairs
  differ only in the stamp line); live re-open `w1/Mo97ScoutLive.md`; sibling scan `w1/Mo97ConnSibling.md`.
- Mistake mining: `corpus/lessons/round-97.md` `## Mistakes` rows 1–5 (instrument amnesia, evidence loss, supersession
  hole, junk-row false green, quote word-count label 14→12 caught by seat Mo97ScoutLive).
- r96 routed defects 1–7: disposition in `corpus/lessons/round-97.md` ("r96 closure routed defects — disposition").

Round shape: ONE v1 wave `w1`, 14 seats, validator rc 0 (`.ufo/waves/round-97/w1-validator.out`, spec `w1-spec.json`,
dispatch `w1-dispatch.json`, results `w1-results.json`): scout ×2, connector ×1, executor ×2, reviewer ×2, critic ×2,
mutation-tester ×3, revenger ×1, scribe ×1. Attack seats (reviewer/critic/mutation-tester) 7/14 = 50 %. No residual call;
round total 14. Dead seats: 0 (14/14 settled with reports; results.json carries no per-seat `status` field, settlement
read from non-empty outputs). Planner seat: held by the L1 (validator refuses `planner`); the planning data-walk is the
contract and control battery. Routing: role map in `~/.omp/agent/config.yml` (`task.agentModelOverrides`), never passed.

## Landed changes

| commit | what | LOG.md entry |
|---|---|---|
| `dd1ae1150f53df54e7530311b2323368e3c0e5e9` | freeze: contract, `count-c1.py`, `count-c2.py`, `controls-r97.sh`, `evidence/controls-r97.txt`, candidate inputs | Round 97 |
| `e85ed91249953094b067554bfa79fcdc65791f8e` | C1 registry rows (`SKILL.md`), C2 pins `corpus/evidence/sources-r97/`, S628 row (`corpus/SOURCES.md`, +1 line), `corpus/lessons/round-97.md` | Round 97 |
| `5497e6f70aaf21a38fc0140d9f7291a5571f4987` | wave `w1` evidence, before/landing receipts, three registry cell corrections, lesson update, `LOG.md`, `SCORECARD.md` round-97 section + Planned r98 | Round 97 |
| `b6d034082582340a69371393d5bca25d04e05f4f` | final-revision receipts `evidence/final-c1.txt`, `final-c2.txt`; census before/after receipts | Round 97 |

## Before → after measurements

Method: `git -C /home/vgpnk/Projects/shokunin/mori-shokunin archive <rev> | tar -x -C DIR`, then the frozen counter
(`count-c1.py` sha256 `78a09016…d2a95`, `count-c2.py` sha256 `957a7be6…1e91`, unchanged since `dd1ae115`).

- **C1** `python3 .ufo/waves/round-97/count-c1.py --root DIR`
  - before @`973b2af1`: `C1=unmet unregistered=4 registry=unmet targets_ok=0/4` exit 1 (`evidence/before-c1.txt`)
  - after @`e85ed912` (landing): `C1=met unregistered=0 registry=met targets_ok=4/4 checks_failed=-` exit 0 (`evidence/landing-c1.txt`)
  - after @`5497e6f7` (final, post cell corrections): same line, exit 0 (`evidence/final-c1.txt`)
- **C2** `python3 .ufo/waves/round-97/count-c2.py --root DIR`
  - before @`973b2af1`: `C2=unmet mismatch=0 unpinned=3 targets_ok=0/3 hole_guard=n/a live=S615:no-copy,S616:no-copy,S623:no-copy` exit 1 (`evidence/before-c2.txt`)
  - after @`e85ed912`: `C2=met mismatch=0 unpinned=0 targets_ok=3/3 hole_guard=pass live=S615:time-churn,S616:time-churn,S623:time-churn checks_failed=-` exit 0 (`evidence/landing-c2.txt`)
  - after @`5497e6f7`: same line, exit 0 (`evidence/final-c2.txt`; live fetch at that time)

Both frozen targets met as declared; no predicate, counter or target changed after the freeze. Score moves: none claimed.

## Sources & frontier

- Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`
  - round start: exit 0, `mori ok` (`evidence/census-before.txt`)
  - round end (tip `b6d03408` bytes): exit 0, `mori ok` (`evidence/census-after.txt`); W04 duplicate-URL lines identical
    before/after (diff empty; 43 lines by `grep -c W04` — the lesson's "42" is copied from the r96 closure, not re-counted).
- Rows: 399 → 400 (`grep -cE '^ {0,3}\| *S[0-9]{3,}' corpus/SOURCES.md`). Added by tier: B +1 (S628, kind code, mined).
  Rows touched old→new: none (no `status`/`recheck`/`used-by` edit; S615/S616/S623 re-opened, bytes unchanged).
- Frontier rows advanced: none.
- Sourced claim: C2 cites S628 (opened this round).
- Mistake mined: `corpus/lessons/round-97.md` `## Mistakes` (5 rows).
- Assimilation: none (`/home/vgpnk/Projects/shokuknow/merge/mori/` exists; no theme fits these claims).
- considerthese: mined by seat `w1/Mo97ScoutConsider.md` — of the five proposals in `considerthese/2026-11-05.md`, three
  unimplemented (admitted-share ledger, fleet snapshot path, gate runtimes), one partial (sibling host-path sweep); none
  adopted this round; gate runtimes is the candidate for the r98 registry work.
- Routed (not absorbed): 11 sibling lanes hold 58 docs.python.org rows with recorded page digests that the same stamp churn
  will stale (`w1/Mo97ConnSibling.md` §1); 0/4 registered tools belong to another province.

## Trend verdicts

- **expansion: unchanged** — no admitted `knowledge/` entry (`git diff 973b2af1 b6d03408 -- corpus/knowledge/` empty); S628
  is a registry row, not expansion (CORPUS rule 4).
- **quality: improved** — three stale-flagged rows re-verified against the live surface and pinned with the bytes their
  digests record (C2, `evidence/landing-c2.txt`); four running gates now carry accurate, executable registry rows (C1),
  with three cells corrected from a live domain trial.
- **discernment: unchanged** (pending the closure's outside spot-check) — the S628 admit and the "pin today's live bytes"
  reject are on the lesson's Gate; seat disagreements (word-count label, registry cells, counter survivors) became lesson
  rows or Planned r98 items.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` section "Round97 gate registry backfill" (four 8-cell registry rows; known-limit clause on the digest gate's supersession hole)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` "Round 97" (live drift re-check of three docs rows; live cgroup PSI survey, `w1/Mo97ExecTrial.md`)
- [~] Instructions executable by an agent without oral context — `python3 .ufo/waves/round-97/count-c1.py --root DIR` re-runs each new row's selftest and requires its stated line (`evidence/final-c1.txt`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `w1/Mo97ConnSibling.md` §3 (0/4 tools in another province); sibling stale-row finding routed, not absorbed

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none. Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` → one untracked
`w4lines.txt` (mtime 16:57 -03, before this round's 17:42 launch, no mori content) — not this lane's; left untouched.
Open L0 questions (not treated as answered): mori | round-94 (D1 planner binding; sibling host-literal class; C2 restate),
mori | round-95 (C1 axis classification; C2 do-nothing; dead-seat policy), mori | round-96 (stale digests — this round
appended no supersession row and edited no digest). No new L0 question this round.
Scratch: `/fast/scratch/hyaku/mori-r97` removed after landing (seat Mo97ExecTrial had reported its tree retained).
