# kasegi — round 99 report

Lane: kasegi (`/home/vgpnk/Projects/shokunin/kasegi-shokunin`). Round 99, attempt 1.
Base `b9411a6b530e486180cf14c72fccc46668dcf5ee`; freeze
`6195db307c1cb101eba1d268f8cbfc1578d2caf7`; C2 landing
`a3db47e71fe292c03b00ba11f38cccbec45d3966`; C1 landing
`3746f64e0f36e1ff91173f7124d39f91dc89851c`; landing receipt
`29cd3058c8651b05881764893558deab6780ef1a`; integration `bedb6c47f80143b6fb73f3e4bc7a5376816a65b1`; final lane tip
`6f4858a89764ef29263c3abe4387873ed583f806` (remote equal).

## Work performed

Declared claims (frozen in `.ufo/waves/round-99/claims.json`):

- **C1 — `depth:verifiability`** (the lane's lowest non-retired axis, score 4): the
  citation census of record becomes tamper-evident and layout-stable. Before: the
  round-98 check verified only the pinned line (5 of 12 tamper classes rejected), the
  pinned rate flipped 2589/7961 vs 2591/7961 across work dirs, and the exact command
  died under earlyoom at 3.5 GiB. After: 12/12 tamper classes rejected, the same pinned
  triple in a clean and a contaminated work dir, 2.23 s at 512 MB peak RSS.
- **C2 — `coverage`** (score 8 held; capability extension of `capture-secret-scan`):
  `gitlab-session-cookie` adopts S140's assignment-context separator window
  `[^\n]{0,8}[:=][^\n]{0,8}`. Before: 0 of the twelve real session values the round-98
  sentinel measured were detected. After: 12/12, ten boundary negatives clean, selftest
  170 → 192.

Work items:

- **C1 instrument rewrite.** `corpus/instruments/census-at-rev.py` now confines every
  relative citation to the measured tree (a `..` walk-out that resolves outside the
  extract is `HOST-OWNED`, out of the pinned numerator and in the denominator), extracts
  under a private parent (`<work>/extract-<rev12>/tree`), runs `resolve.py` under a
  confined `HOME` (empty `Projects/`), binds the five header lines with `header-sha256`
  and the body with `body-sha256`, never reads the measurement cache in `--check`, and
  requires `measured-at` to be exactly 40 hex and an ancestor of a local branch tip;
  `--write` refuses a non-ancestor revision. Evidence:
  `.ufo/waves/round-99/controls/c1-landing-r99.txt` (P1–P4), instrument sha256
  `c06d95cd71a39dcde7b24ab743a36d5ae07500e25fb40681d4fb3356d395a0a3`.
- **C1 census of record regenerated** at the C2 landing: `corpus/instruments/citation-survival.md:5-12`
  (`measured-at: a3db47e7…`, `home: confined`, pinned SKILL 162/732 = 22.13 %, corpus
  2569/7624 = 33.70 %, lane 2607/8026 = 32.48 %, host-owned 76, confined 1,
  `header-sha256`, `body-sha256`).
- **C1 host-owned body fix (R161).** The round's own final check exposed that the digest-bound body
  embedded a host-owned row's occurrence count (`.ufo/watchdog.log` grew 3237 → 3239 during the
  round), so `--check` failed `body-mismatch` on the unchanged census of a revision that had
  passed at the landing. A `RESOLVES`/`MIRROR-EQUIVALENT` row's occurrence cell is normalised to
  `-`; the census is regenerated at the same revision with the same pinned triple and the
  instrument pin becomes `c06d95cd…`. Evidence: `3746f64e`, lesson M99-10.
- **C1 tamper harness.** `.ufo/waves/round-99/c1/tamper.py` (12 named classes over the
  census and its measurement environment); base receipt
  `.ufo/waves/round-99/controls/c1-tamper-base-r99.txt` (`killed=5 total=12`), candidate
  receipt `c1-tamper-candidate-r99.txt` (`killed=12 total=12`).
- **C1 layout and memory controls.**
  `.ufo/waves/round-99/controls/c1-layout-memory-controls-r99.txt`: `CENSUS-CHECK pass`
  in a clean work dir and in one whose parent carries `MISSION.md` and
  `.ufo/waves/shokunin12h-20261014-p1-repair/members/KasegiGateRepair.md`, identical
  `skill=162/732 corpus=2569/7624 lane=2607/8026`; `/usr/bin/time -v` prints 2.23 s wall
  and 512,980 kB maximum resident set size; `--write` refuses `0123456789ab`
  (`bad-revision rc=2`) and a detached fixture commit (`rev-not-ancestor rc=2`).
- **C2 separator window.** `corpus/instruments/capture-secret-scan.py:318-320` — the
  `gitlab-session-cookie` shape now uses `[^\n]{0,8}[:=][^\n]{0,8}`; the docstring entry
  states the window and the twelve payloads it closes. Evidence:
  `.ufo/waves/round-99/controls/c2-probe-candidate-r99.txt`
  (`mustfix_hit=12/12 negatives_extra=0`), base `c2-probe-base-r99.txt`
  (`mustfix_hit=0/12 negatives_extra=2`).
- **C2 selftest.** `python3 -B corpus/instruments/capture-secret-scan.py --selftest`
  prints `SELFTEST-RESULT pass cases=192` (170 at the base); the twelve separator
  positives and ten boundary negatives are the round-98 sentinel's own payloads
  (`.ufo/waves/round-98/w1/SentinelShapes-receipts/final-checks.txt:15-26`) plus their
  negatives.
- **C2 knowledge and source.** `corpus/knowledge/gitlab-iam-ci-build-and-session-token-shapes.md`
  now states the assignment-context window, cites S150, and carries the wave's correction
  that the pinned commit supersedes the MR form with `assignmentOperand` (S151);
  `corpus/SOURCES.md:162` is the new S150 row (the rules repo's MR !151, live HTTP 200,
  128,120 bytes) and `corpus/SOURCES.md:163` the new S151 row (the generator source at the
  pinned commit, three fetches, 9,776 bytes, sha256
  `91519731800ab8d96a00a03fff44e72c1c16a3bad12c9e017d7d679a8fad756d`).
- **C2 evidence sweep.** The new window matched 57 synthetic 64-hex values in four
  round-98 sentinel receipts; all are redacted structurally
  (`.ufo/waves/round-99/controls/redaction-r99.txt`, one
  `[session-cookie-fixture-redacted-r99]` marker per value, line numbering preserved,
  before/after digests); the landing scan prints `hits=0 unused_allow=0`
  (`controls/c2-landing-r99.txt`), and the pre-redaction `hits=4 files=4` failure is kept
  in the same receipt.
- **Round-98 routed defects 1–9.** Closed or answered one by one in
  `corpus/lessons/round-99.md` § Routed defects; the two that touch history (S148/S149
  Gate records, the `147 → 149` and superset corrections) are appended to
  `corpus/lessons/round-98.md` § Appended corrections.
- **Wave w1.** One v1 wave of 13 seats (3 critic, 2 reviewer, 2 mutation-tester, 1
  sentinel, 2 executor, 1 scout, 1 connector, 1 scribe; attack 8/13 = 62 %), dispatched
  from `.ufo/waves/round-99/w1.ready`; spec `w1-spec.json`, dispatch `w1-dispatch.json`
  (`counts.spawn=13`), results `w1-results.json`. Findings in § Wave findings.

## Landed changes

| Commit | LOG entry | What it carries |
|---|---|---|
| `6195db30` | Round 99 bullet 2 (Freeze) | `claims.json` (C1 P1–P4, C2 K1–K6, kill rules, do-nothing controls, pins), `c1/tamper.py`, `c2/session-cookie-probe.py`, the base/candidate receipts, the layout/memory controls |
| `7f890046` | Round 99 bullet 3 (C2 landing) | `capture-secret-scan.py` separator window + selftest 192, the knowledge entry's window and S150 citation, the S150 row, the capability row |
| `a3db47e7` | Round 99 bullet 4 (C2 addendum) | the round-98 receipts redacted structurally (57 markers; the commit message says 53 — the receipt and the lesson carry the corrected 57), the redaction receipt, the pre-redaction K4 failure |
| `35e3ab60` | Round 99 bullet 5 (C1 landing) | `census-at-rev.py` (confinement, digests, cache bypass, ancestor pins), the census of record regenerated at `a3db47e7`, the updated control receipts |
| `29cd3058` | Round 99 bullet 5 (C1 receipt) | `controls/c1-landing-r99.txt` (P1–P4 at the landing) |
| `bedb6c47` | Round 99 bullets 6–7 (Sources, Integration) | lesson `round-99.md`, QUALITY R159/R160, the SCORECARD round-99 section, the round-98 appended corrections, LOG round-99, the wave spec/dispatch/ready |
| `2c2124f2` | Round 99 bullet 7 (Integration, correction) | the `controls` erratum on both claims (R148, lesson M99-7) and the post-integration re-run of the whole control set (R149) |
| `e7d70757` | Round 99 bullet 7 (Integration, re-anchor) | the R143/R144 re-anchor: 43 citations across seven knowledge entries, 122 explicit citations in range, the committed line map |
| `01f4f59f` | Round 99 bullet 6 (Sources, correction) | S151 (the generator source at the pinned commit), the knowledge entry's two-form statement, the C1/C2 `erratum_wave` fields, the per-line redaction digests |
| `44897114` | Round 99 bullet 7 (Integration, wave) | the lesson's wave findings and the SCORECARD's wave paragraph |
| `c264526a` | Round 99 bullet 7 (Integration, correction) | the round-98 appended corrections replaced with the audited draft |
| `3746f64e` | Round 99 bullet 5 (C1 landing, re-made) | R161: the census body normalises a host-owned row's occurrence count, the census of record regenerated at `a3db47e7` with the same pinned triple, the instrument pin `c06d95cd…`, the claim's `erratum_landing` |
| `5015113f` | Round 99 bullet 8 (Wave evidence) | the wave spec/dispatch/ready/results, the 13 seat reports and receipts, the wave-evidence redaction, the misrooted `cli-checks.txt`, the report-evidence and re-anchor receipts, QUALITY R161 and lesson M99-10 |
| `6f4858a8` | Round 99 bullet 5 (C1 receipt, re-made) | `controls/c1-landing-r99.txt` re-run at the re-made landing: tamper 12/12 vs 5/12, both layouts pass, the pin matches |

## Before → after measurements

**C1 — `depth:verifiability` (score 4 held).**

Counting command (paste):

```sh
python3 -B .ufo/waves/round-99/c1/tamper.py --lane . \
  --rev a3db47e71fe292c03b00ba11f38cccbec45d3966 \
  --alt-rev b9411a6b530e486180cf14c72fccc46668dcf5ee \
  --instrument corpus/instruments/census-at-rev.py --work <scratch>
```

- Before: the same harness with `--instrument <git show e2d3de7b847f8e9bac72a5bc4dea455ea051cf1a:corpus/instruments/census-at-rev.py>`
  prints `TAMPER-RESULT killed=5 total=12 evaluated=12 instrument_sha256=66383371…`
  (survivors: T05 body-edited, T06 host-line-removed, T07 host-line-edited, T08
  body-from-other-rev, T09 poisoned-cache, T11 host-owned-edited, T12 body-truncated).
- After (measured at `35e3ab60`): `TAMPER-RESULT killed=12 total=12 evaluated=12
  instrument_sha256=6d68d955…`.
- Layout: before, the round-98 instrument's pinned rate flipped 2589/7961 (clean) vs
  2591/7961 (contaminated parent); after, both layouts print
  `skill=162/732 corpus=2569/7624 lane=2607/8026 host_owned=76` and `CENSUS-CHECK pass`.
- Runnable: before, the exact command died `CENSUS-CHECK fail reason=resolve-rc-15 rc=2`
  under earlyoom at 2–3.5 GiB; after, 2.23 s wall / 512,980 kB peak RSS.

**C2 — `coverage` (score 8 held; capability extension).**

Counting command (paste):

```sh
python3 -B .ufo/waves/round-99/c2/session-cookie-probe.py --lane . \
  --instrument corpus/instruments/capture-secret-scan.py --work <scratch>
```

- Before (round-98 instrument at `e2caf4a1`): `PROBE-RESULT mustfix_hit=0/12
  negatives_extra=2 negatives=10 instrument_sha256=45f8d226…`.
- After (measured at `a3db47e7`): `PROBE-RESULT mustfix_hit=12/12 negatives_extra=0
  negatives=10 instrument_sha256=8b338726…`.
- Selftest: `SELFTEST-RESULT pass cases=170` → `cases=192`.
- The lane's own scan at the C2 landing revision: `hits=0 files=0 allowed=27
  unused_allow=0` (before the redaction sweep: `hits=4 files=4`, kept as evidence).

**Non-target guard — `depth:density`:** `python3 corpus/instruments/density.py SKILL.md
--label r99` reads 273.2 before and after; `git diff --stat b9411a6b 35e3ab60 -- SKILL.md`
is empty.

## Sources & frontier

- Registry rows: **149 → 151** (`grep -cE '^ {0,3}\| S[0-9]{3} \|' corpus/SOURCES.md`
  prints 149 at the base and 151 at the final lane commit).
- Rows added by tier: **S150, tier B** (kind `code` — the rules repo's merge request
  !151, the assignment-context generator's `<keyword>.{0,8}[:=].{0,8}<value>` form;
  opened this round, live HTTP 200, 128,120 bytes; status `mined`) and **S151, tier A**
  (kind `code` — the same generator's source at the pinned commit, byte-stable across
  three fetches, 9,776 bytes, sha256 `91519731800ab8d9…`, which carries
  `assignmentOperand` and supersedes the MR form; status `mined`, used-by the knowledge
  entry). The wave's ScoutSources found S150's HTML digest nonce-bound (F2) and the
  pinned form different (F1); S151 is the byte-stable authority and the knowledge entry
  states both forms.
- Rows touched old → new: **S140** re-opened from its committed capture for lines
  547-551 (live `/-/raw/` answered HTTP 403 again, a Cloudflare challenge page) — status
  `mined`, recheck `180d`, used-by unchanged; **S148** re-opened from its committed
  capture for the value's length and alphabet — no cell change.
- Frontier rows advanced: the coverage map's credential-shape ground (no frontier row
  id; the `capture-secret-scan` capability row is the surface) — the session-cookie
  separator class moves from "not detected" to "detected with ten boundary negatives
  clean".
- Census before → after:
  `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`
  exits **0** at round start and **0** at round end (`kasegi ok`), with the seven
  inherited W04 duplicate-URL warnings (S028, S029, S072, S076, S080, S085, S143)
  unchanged.
- Assimilation: **none** — the staged ids collide with the lane registry by
  construction; package adoption waits for a later round.

## Trend verdicts

- **expansion: improved** — S150 and S151 are new ground (the generator's window and its
  pinned-commit source, which no row held), and the capability row gains a separator class
  covering twelve real session values. Evidence: the registry count above, the two rows,
  the probe's 12/12.
- **quality: improved, with a measured qualifier** — the census check's discrimination
  rises 5/12 → 12/12, the census is layout-stable and runnable (2.23 s / 512 MB), the
  scanner's window closes the twelve round-98 MUST-FIX payloads (0/12 → 12/12) and its
  selftest grows 170 → 192. Qualifier: the window implements the MR !151 form, which the
  pinned commit supersedes with `assignmentOperand` (S151), and the wave measured 23
  payload classes the round-98 scanner hit that the landing does not (the Netscape cookie
  jar among them) plus 4 rune-width misses; a remediation (candidate B) is measured and
  routed to round 100. Evidence: `.ufo/waves/round-99/controls/`, `w1/SentinelCookie.md`,
  `w1/ScoutSources.md`.
- **discernment: improved** — nine mistakes mined (M99-1…M99-9), the round-98
  spot-check's nine routed defects closed or answered, the round's own controls caught two
  defects before the landing, and the wave falsified the C2 statement's "S140's class"
  clause, which the round reports rather than smooths over (the C2 erratum). Evidence:
  `corpus/lessons/round-99.md` § Mistakes, § Routed defects; `.ufo/waves/round-99/claims.json`
  `erratum_wave`.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `corpus/lessons/round-47-verifier-spotcheck.md` (line 94; non-author: boxes 1, 3 and 4 checkable from outside; SKILL.md is the object under test, not its evidence).
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `corpus/practice/curl-h1-1913733/report.md` (round 85) and `corpus/practice/curl-ibb-h1-1997312/report.md` (round 86), both logged in LOG.md.
- [~] Instructions executable by an agent without oral context — evidence: `corpus/lessons/round-47-verifier-spotcheck.md` (declared-root recheck observations; not promotion).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` (scope unchanged; live-target testing remains refused).

## Round shape

One v1 wave of 13 seats under `ufo-wave-policy.json` (band 8–16): 3 critic, 2 reviewer,
2 mutation-tester, 1 sentinel, 2 executor, 1 scout, 1 connector, 1 scribe; attack
8/13 = 62 %; no planner seat (the L1 holds the canonical §3 planner seat per the
fleet-wide 2026-10-19 ruling). No residual call. Round total: **13 seats**.

## Wave findings

One v1 wave of 13 seats (`.ufo/waves/round-99/w1-spec.json`, `w1-dispatch.json`,
`counts.spawn=13`). Twelve seat reports had landed when this section was written; the
thirteenth (ConnectorOverlap) is recorded in the same wave's results file.

**C1 — P1–P4 stand; the wave names the counter's coverage limit.**

- `CriticClaimsC1`: P1 STANDS (12/12 at the landing, 5/12 on the round-98 bytes,
  both reproduced), P2 STANDS (identical triple in both layouts), P3 STANDS, P4
  STANDS (8.99 s / 514,764 KB). Three attack classes it built are accepted and
  routed: (d) a symlinked extract *tree*, (e) a pre-seeded extract reused across
  revisions, (f) a recomputed `header-sha256` over a false `home:` line.
- `ExecC1Indep`: independent extractor AGREES exactly (SKILL 162/732, corpus
  2569/7624, lane 2607/8026, distinct 8026, one `../` HOST-OWNED exclusion); the
  tamper harness reproduces 12/12 and 5/12; the 76 host-owned citations decompose
  into 73 resolving absolute/`~` citations plus 3 `~/Projects*` roots.
- `ReviewC1Instrument`: numbers MATCH, P1–P4 PASS, the cache key carries the
  instrument digest, `--check` never reads the cache; qualifiers F3 (`--check`
  writes the cache), F4 (the `home:` line is digest-bound but not verified), F5
  (the title/prose are unbound).
- `MutC1Tamper`: 12 instrument mutants against the frozen harness — 8 survive
  (dropped confinement, 12-hex `measured-at`, dropped ancestor check, dropped
  header digest, cache bypass, SKILL-only pinned compare, missing pinned line).
  The harness is artifact-level by design; an instrument-level mutant harness is
  routed to round 100.
- `CriticHarm`: NO HARM on the committed landing (SKILL/PROVINCE/SHONEN/AGENTS
  byte-identical, no shape lost, the redaction byte-clean at 57 markers). One
  provenance harm: the redaction receipt recorded 4 of the 57 lines — closed by
  appending per-line before/after digests for all 57. The census clobber during
  the wave is a live incident, not the landing (M99-9).

**C2 — K1–K6 stand; the wave falsifies the statement's "S140's class" clause.**

- `CriticClaimsC2`: K1–K6 all PASS; the strict `_gitlab_session=` matcher is killed
  by the twelve payloads, the `.*` matcher by three negatives, the newline refusal
  is real; the `cell-<N>-` group and the right boundary are passable (V11/V4).
- `SentinelCookie`: 192-cell matrix, 4,000-case fuzz. 7 MUST-FIX (left boundary,
  right boundary, a 65-hex run behind `cell-N-`), 4 rune MUST-FIX (a gap of 3+
  multi-byte runes is refused because `[^\n]` counts bytes where RE2's `.` counts
  runes), and 23 payload classes the round-98 scanner hit that the landing does
  not — including a TAB-separated Netscape cookie jar (end-to-end: landed
  `hits=0`, round-98 `hits=1`). It measured a remediation (candidate B: 12/12,
  0/10, jar recovered) and routed it.
- `MutC2Counter`: 10 mutants, one survivor (M05, the `cell-<N>-` group) — the same
  unbound limb `CriticClaimsC2` found independently.
- `ExecC2Probe`: 24/24 independent positives hit, 23/24 negatives clean; one extra
  hit on a 65–72-hex run (the window eats one hex byte), a precision note outside
  the frozen negative set.
- `ReviewC2Scanner`: APPROVE on the window, the no-regression check and the C2
  landing.
- `ScoutSources`: **F1** — the pinned commit 59ada1f4 already carries
  `assignmentOperand = [="' :>\],\t.()\\?|]{1,10}`, not the MR !151 form the
  scanner implements (verified independently by the L1: three fetches, 9,776
  bytes, sha256 `91519731800ab8d9…`); **F2** — S150's anchor digest is nonce-bound
  and not reproducible. Both are corrected: S151 (the generator source at the
  pinned commit) is added as the byte-stable authority, the knowledge entry states
  both forms and their two-way difference, and the C2 erratum records the material
  statement correction.
- `ScribeGate`: found three defects in the round's appended corrections (S148/S149
  word counts, the landing/integration conflation in the `147 → 149` sentence, the
  S140 used-by enumeration) plus the redaction count (53 → 57); all corrected from
  its draft.

**The round's own final check.** Before the wave evidence was committed, the L1's last `--check`
printed `body-mismatch` on the unchanged census: the digest-bound body embedded a host-owned row's
occurrence count and `.ufo/watchdog.log` had grown 3237 → 3239 during the round. Fixed as R161
(the occurrence cell of a `RESOLVES`/`MIRROR-EQUIVALENT` row is normalised to `-`), the census
re-landed at the same revision with the same pinned triple, and the instrument pin re-made
(`c06d95cd…`); lesson M99-10. This is the class the r98 spot-check routed as defect 8, closed for
the body as well as the header.

**Cross-cutting.** `ConnectorOverlap`: zero overlap on both axes — no sibling lane maintains a
revision-bound citation census with digests, and `_gitlab_session` / `assignmentContext` /
`gitlab-session-cookie` do not exist outside this lane's corpus; the six sibling hits it did
find (`tsukuroi`'s `census-at-rev.sh`, `kotoba`'s routing index, `mori`'s observational note,
`kagi`'s snapshot digest check, `tabi`'s benchmark body hash) are name collisions, each
recorded with its path and line. No seat died; every seat's report carries its own receipts
under `.ufo/waves/round-99/w1/`.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Tool installs

None this round (no tool was installed or upgraded).

## Open L0 questions

None opened this round.
