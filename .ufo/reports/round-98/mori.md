# mori — round 98 report (L1 MoriR98, attempt 1)

Lane HEAD `db9f1b78b93d1e27d194b4d035d69524b24fd001` (`git ls-remote origin refs/heads/master` prints the same hash).
Entering `b2a67ce562bbf2f0cc73f47d8e79f792badf5e63`, freeze `b75e26ccd771b872099ef7233a61e3e91d9f6f7a`, landing
`600deb7ed2695f54b289cf5b6c3931e0fa9c8bb3`.

## Work performed

Declared claims (2):
- **C1, coverage (score 6), capability acquisition:** `tools/mori-userns-runway.py`. It reads user-namespace runway
  (the `user.max_user_namespaces` limit against the distinct non-initial user namespaces on readable process links;
  states ok, low or exhausted, and a limit of 0 is exhausted). It also scans sudo-logged journal commands for
  kernel-tunable writes. This is new resource-runway ground.
- **C2, calibration (score 5, the lowest non-retired tier):** the SCORECARD `## Axes` Last-change cells for
  operability and freshness now match the admitted r97 closure.

Work items:
- Protocol load: the round prompt, AXES.md, CORPUS.md SOURCES contract, SCORECARD Planned r98, the r97 spotcheck
  (`mori-shokunin/corpus/lessons/round-97-verifier-spotcheck.md`), considerthese/2026-11-05.md, and the MANIFEST mori
  closures r92–r97.
- Pre-freeze controls, executed and committed with the freeze `b75e26cc`:
  - `.ufo/waves/round-98/evidence/controls-r98.txt`: `CONTROLS_DONE unexpected=0`.
  - C1: do-nothing K0, eleven forgeries through the tool's public CLI (K1–K11), and positive P1.
  - C2: do-nothing K0c, four forgeries (K1c–K4c), and positive P1c.
  - The first draft run failed its positive control (`evidence/controls-draft-prefreeze-r98.txt`, `unexpected=1`).
    The counter was fixed before the freeze.
- Incident capture: 276 sudo command lines from 05:14 to 05:43, pinned by sha256 inside `count-c1.py`
  (`.ufo/waves/round-98/evidence/journal-incident-r98.txt`).
- Sources opened and pinned this round: S629–S632 (`corpus/evidence/sources-r98/`). S629 is kernel sysctl/user.rst
  v7.2, S630 is unshare(2), S631 is proc_ns.h v7.2 and S632 is uapi nsfs.h v7.2.
- Knowledge entry: `corpus/knowledge/userns-runway-r98.md`, with 7 sourced claims and a reading-rules table.
- Landing `600deb7e` carries:
  - the tool;
  - a registry row appended to SKILL.md;
  - the PROVINCE core note;
  - the knowledge entry;
  - SOURCES rows S629–S632;
  - the two SCORECARD cells.
- Late-seat addendum for r97 closure D1, committed in `beab7bbb`.
- Wave `w1`: 13 seats, all reports in `mori-shokunin/.ufo/waves/round-98/w1/`.
- Post-hoc randomized check, which is not the claim counter: `.ufo/waves/round-98/xcheck-random-r98.py`. It scores
  the landing tool 40/40 + 40/40 on seeds 1, 2 and 98, and the constant stub 0/40
  (`evidence/xcheck-random-r98.txt`).
- New QUALITY criterion 209 (lookup forgeries against frozen fixture batteries).
- Lesson `corpus/lessons/round-98.md`, with 4 mistakes mined.
- Round shape: ONE v1 wave `w1`, 13 seats.
  - Roles: scout ×2, connector ×1, executor ×3, scribe ×1, reviewer ×2, critic ×3, mutation-tester ×1.
  - Attack seats 6/13 (46 %).
  - No residual call. Round total 13. Dead seats 0 (`w1-results.json`: 13 results, every report file present).
  - Planner seat: held by the L1. The validator rejects `labrat`, so the planned lab probe ran as critic seat
    `Mo98CritLB`.

## Landed changes

All commits landed with `jj-lane.sh`, each tied to the LOG.md `## Round 98` entry.

| commit | content |
|---|---|
| `b75e26ccd771b872099ef7233a61e3e91d9f6f7a` | freeze: contract, counters, controls script and receipt, before receipts, census-before, incident capture, candidate |
| `beab7bbbf7b168108241e98d4c493cf5e4301cb5` | r97 late-seat addendum (closure D1) |
| `600deb7ed2695f54b289cf5b6c3931e0fa9c8bb3` | landing for C1 and C2 |
| `379a2f616c146f29341987e73b2828a0ce728ce2` | landing receipts |
| `e4fb203f8249868b58692e2bb1660f7d0f93b212` | wave evidence, lesson, QUALITY 209, SCORECARD verdict, capability row and Planned r99, LOG, census-after, xcheck |
| `db9f1b78b93d1e27d194b4d035d69524b24fd001` | final receipts |

## Before → after measurements

C1, measured with `git -C mori-shokunin archive <rev> | tar -x -C DIR; python3 .ufo/waves/round-98/count-c1.py --root DIR`:

| point | revision | output | exit |
|---|---|---|---|
| before | entering `b2a67ce5` | `C1=unmet cases_ok=0/15 selftest=absent live=absent registry=met sourced=unmet province=unmet` | 1 |
| after | landing `600deb7e` | `C1=met cases_ok=15/15 selftest=ok live=ok(limit=122865,used_lb=8,state=ok) registry=met sourced=met(S629,S630,S631,S632) province=met checks_failed=-` | 0 |
| after | tip `e4fb203f` | same verdict (`evidence/final-c1.txt`) | 0 |

C2, measured with `python3 .ufo/waves/round-98/count-c2.py <rev>`:

| point | revision | output | exit |
|---|---|---|---|
| before | `b2a67ce5` | `C2=unmet mismatches=2 columns_unchanged=yes tool=ok tool_rc=1 mismatched_axes=operability,freshness` | 1 |
| after | landing `600deb7e` | `C2=met mismatches=0 columns_unchanged=yes tool=ok tool_rc=0 mismatched_axes=-` | 0 |
| after | tip `e4fb203f` | same verdict | 0 |

Attack results:

- **C1:**
  - Holds per `w1/Mo98RevC1.md`, `w1/Mo98ScoutHost.md` (lsns 6 = used_lb 6), `w1/Mo98ExecTrial.md` (live +3
    delta) and `w1/Mo98MutC1.md` (13/14 killed; survivor m03 is used > limit).
  - **Needs-amend per `w1/Mo98CritC1.md`:** a fixture-shape lookup stub passes the frozen counter at 15/15, and the
    live leg checks only the limit echo.
  - The claim stays as frozen. The defect is reported, routed into QUALITY 209, and shown with the post-hoc
    randomized check. The closure decides admission.
- **C2:** holds per `w1/Mo98CritC2.md`, `w1/Mo98RevC2.md` and `w1/Mo98ExecCalib.md`.
  - RevC2 framing note: the gate checks against the fleet MANIFEST.
  - The Evidence cells still cite older closures, and the r96 gate pins those cells to base `66c5518e`. This is
    routed to Planned r99.

## Sources & frontier

- SOURCES rows: 400 → 404, counted with `grep -cE '^ {0,3}\| *S[0-9]{3,}' corpus/SOURCES.md`.
  - Added by tier: A +4 (S629, S630, S631 and S632, all `mined`, used-by `corpus/knowledge/userns-runway-r98.md`).
  - Rows touched old→new: none.
  - Rejected and logged in the Gate: re-scoping S627.
- Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`.
  - Round start: exit 0, 43 W04 (`evidence/census-before.txt`).
  - Round end: exit 0, last line `mori ok`, 43 W04 (`evidence/census-after.txt`).
- Digest gate (`tools/mori-source-digest.py`): S629–S632 `ok`; `DIGEST_CHECK rows=129 ok=96 mismatch=0
  prefix_only=31 unpinned=0`.
- Sourced claim: C1. The knowledge entry cites S629–S632, all opened this round.
- Mistakes mined: 4 (landing, number-drift, vacuous, survivor) in `corpus/lessons/round-98.md` `## Mistakes`.
- r97 closure D2: correction of record (42 → 43 W04) in the lesson.
- Assimilation: none. `merge/mori/` has no theme that fits.
- considerthese: `2026-11-05.md` was read; no proposal was taken.

## Trend verdicts

- **expansion: improved** — one new admitted-candidate knowledge entry (`corpus/knowledge/userns-runway-r98.md`)
  cites mined rows on ground that was uncovered at entering. At entering, `git show b2a67ce5:PROVINCE.md | grep -ci
  namespace` → 0.
- **quality: improved** — four new tier-A rows were re-verified live by a non-author seat as byte-identical to the
  pins (`w1/Mo98ScoutSrc.md`). QUALITY 209 is grounded and shown able to fail.
- **discernment: unprovable-but-better** — the lane's own critic falsified the counter's discrimination, and the
  round reports it rather than prettifying. No outside judge has confirmed this yet.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `mori-shokunin/SKILL.md`
  Round98 registry row; `corpus/knowledge/userns-runway-r98.md` reading-rules table (S629–S632).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 98`; live trial
  `.ufo/waves/round-98/w1/Mo98ExecTrial.md`.
- [~] Instructions executable by an agent without oral context — `python3 tools/mori-userns-runway.py --selftest`
  → `MORI_USERNS_RUNWAY_SELFTEST: PASS (11 cases)`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` Round-98 notes (detection only; repair goes
  to tsukuroi, sysctl policy to the operator); `w1/Mo98ConnSibling.md` (no sibling owns this detection).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none.
Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows one untracked file, `w4lines.txt`.
It is not mori's (numeric content, 0 lane/seat mentions), so it was left untouched.
Open L0: none new. The earlier mori | round-94/95/96 questions stay open.
