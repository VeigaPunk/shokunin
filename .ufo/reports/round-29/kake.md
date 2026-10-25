# Kake round 29 — project-site base paths: sourced knowledge and an offline audit

Lane: `/home/vgpnk/Projects/shokunin/kake-shokunin`, branch `master`, pushed tip
`234524cdc06167ad14477e0956a8786cc3fc752d` (helper line `landed 234524c…`;
`jj-lane.sh state`: local = remote, ahead 0, behind 0, untracked 0). Base
`fe1805cf32a7aadf4574637a3a8912354cee2c7b`. Attempt 1; in-session L1 KakeR29.

## Work performed

Declared claims (SCORECARD "Round 29 — declared claims", commit `d18bbf3`,
notes `9e541a1`, both before any after-measurement):

- **C1 — freshness, frontier.** Project-site base-path knowledge enters as
  `corpus/knowledge/pages-base-path.md`, grounded in four primary sources
  opened this round (S040 GitHub Docs "What is GitHub Pages?", S041 Jekyll
  Docs "GitHub Pages", S042 Jekyll Docs "Liquid Filters", S043 Vite Docs
  "Deploying a Static Site"). Declared after: 4/4 ids pass.
- **C2 — operability, capability.** Offline base-path audit
  `scripts/base_path_audit.py`. Declared after: 30/30 frozen matrix cases with
  all three constant gates rejected.

Both owned axes sit at 10/10 and round 28 added no capability, so the
stagnation nudge applies; the round makes one frontier move and one
capability move. The frontier area is new (PROVINCE Frontier "Jekyll/base-path
build tooling"); the citing-set gate worked in rounds 27 and 28 was left alone
because a third round on that surface trips the session drift sentinel.

Work items:

- Declared claims, frozen matrix (`.ufo/waves/round-29/c2-matrix.json`, 30
  cases, digest-pinned) and both counters before implementation: `d18bbf3`;
  before-values in `.ufo/waves/round-29/verification/c1-before-fe1805c.json`
  (0/4) and `c2-before-fe1805c.json` (0/30; constant gates 7/30, 0/30, 7/30).
- Opened S040–S043 with one public GET each (HTTP 200, 2026-10-22T10:29:37Z);
  retained bodies, visible text and sha256 receipts: `e58b66c`,
  `.ufo/waves/round-29/sources/`. Wave-1 `ReviewSourcesReopen` and wave-2
  `ReopenS040`–`ReopenS043` re-fetched all four: byte-identical.
- Screened six secondary candidates (wave-1 `ScreenRejectCandidates`):
  3 rejected (S044–S046), 2 queued (S047, S048), 1 not opened (Stack Overflow
  returned 403 with a bot-challenge page; no other means used). Retained bytes:
  `.ufo/waves/round-29/sources/screened/`.
- Knowledge entry, S040–S048 rows, lesson Gate: `f8675e5`;
  `corpus/knowledge/pages-base-path.md`, `corpus/SOURCES.md:48-56`,
  `corpus/lessons/round-29.md` "Gate".
- Tool, committed selftest and fixtures, real-input run: `98dbab2`;
  `scripts/base_path_audit.py`, `scripts/base_path_selftest.py`,
  `scripts/fixtures/base-path/`, `.ufo/waves/round-29/real-input/`.
- SKILL decision table "Project-site base-path triage — round 29" and gate
  registry row, README and PROVINCE frontier updates, QUALITY criteria,
  lesson Mistakes: `7697990`, repaired in `d8cd2e4`.
- Wave-2 repairs (entry wording and sourcing, reject reasons, S040/S042
  anchors, SKILL rows, tool same-scheme resolution and docs, 15 regression
  fixtures, selftest key and floor checks, reject-path witness, QUALITY
  pointers): `d8cd2e4`; listed in `corpus/lessons/round-29.md` "Wave-2
  falsification and the repairs it caused".
- SCORECARD measured results and capability row, LOG entry, census after:
  `234524c`.
- Round-28 routed defects: (1) and (2) citing-set fixtures and round-27
  families — explained, not fixed (drift sentinel), carried as named debt in
  `corpus/lessons/round-29.md` "Not repaired this round"; turned into QUALITY
  criteria "A committed fixture asserts the reason code, not only the finding
  id" and "A counter compares the reason code, not only the id", whose
  current failure on the citing-set fixtures is stated. (3) both round-29
  counters address it: C1 matches quotes against retained source text with a
  sha256 check; C2 compares reason tuples. (4) the source gate screened 9 and
  rejected 3. (5) `.gitignore` now ignores `__pycache__/` and `*.pyc`, and the
  untracked round-26 bytecode directory was removed (`d18bbf3`).
- Planner seat: held by the L1 (canonical §3 planner); no planner swarm role.

## Landed changes

Every lane commit carries the LOG entry "Round 29 — attempt 1" (`LOG.md`, last
section, committed in `234524c`).

| Commit | Change |
|---|---|
| `d18bbf3055f33a992fc9adc4b757172554ec9981` | declaration, counters, frozen matrix, before receipts, `.gitignore` |
| `e58b66c203bed4e38f89afeaa9573d980344ab64` | S040–S043 openings and receipts |
| `9e541a1d138158cd957c0e7b1a32050478c02dd0` | declaration notes (capability row promise, counter blobs) |
| `f8675e5a2aac9007ade31bf98813fcb1deee8093` | entry, S040–S048 rows, lesson Gate, screened candidates |
| `98dbab22ae93d325c9dcd791728c38ecf79ba0b6` | tool, selftest, 30 fixtures, real-input run |
| `7697990cbca20291f3b0367b8ff4220e93b38b03` | SKILL, README, PROVINCE, QUALITY, lesson Mistakes, wave-1 evidence |
| `d8cd2e45a903fb05e4f34179aae8a21095a83dbb` | wave-2 repairs and wave-2 evidence |
| `234524cdc06167ad14477e0956a8786cc3fc752d` | SCORECARD results and capability row, LOG, census after |

## Before → after measurements

| Claim | Command (lane root) | Before | After | Measured at |
|---|---|---|---|---|
| C1 | `python3 -B .ufo/waves/round-29/c1_quote_truth.py --root . --revision <commit>` | 0/4 at `fe1805cf`, exit 1 | 4/4, exit 0 | `f8675e5`; re-measured at `98dbab2`, `7697990`, `d8cd2e4`, `234524c` |
| C2 | `python3 -B .ufo/waves/round-29/c2_matrix_count.py --root . --revision <commit>` | 0/30 at `fe1805cf`, exit 1 | 30/30 (control 7/7, defect 14/14, input 8/8, usage 1/1), constant gates 7/30, 0/30, 7/30 all rejected, exit 0 | `98dbab2`; re-measured at `7697990`, `d8cd2e4`, `234524c` |

Counter and matrix blobs are identical from `d18bbf3` to the tip (wave-2
`RerunC1Counter`, `RerunC2Counter`). Receipts:
`.ufo/waves/round-29/verification/c1-after-*.json`, `c2-after-*.json`.
Capability evidence beyond the count: committed selftest 45/45
(`verification/selftest-lane-final.json`; 30 matrix + 15 regression
fixtures); real-input run on the round-23 snapshots of three owned project
sites: 3 pages, 114 references, 4 findings, all `<a href>` links to other
paths on the owner host (`real-input/out/summary.json`, reproduced byte for
byte by wave-2 `RealInputReproduce`).

Limits (wave-2 findings, recorded in the lesson): C1 proves sourcing, not
that each entry sentence follows from its quote — wave 2 found six such
wording defects, repaired by hand in `d8cd2e4`; C2 does not compare `id`,
`page`, `resolved` or the counts; the tool treats http and https on one host
as one site, wider than the matrix wording; remaining resolution and
tokenizer gaps are listed in the tool docstring.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`.
  Before (base, 10:32Z): `kake W04 S033 duplicate url …rfc9110.txt across scopes` / `kake ok …/corpus/SOURCES.md`, exit 0
  (`verification/census-before.txt`). After (`d8cd2e4`): same two lines, exit 0 (`verification/census-after.txt`).
- Rows 39 → 48 (`grep -cE '^\| *S[0-9]{3}' corpus/SOURCES.md`). Added: tier A
  ×5 (S040–S043 mined; S048 queued), tier C ×4 (S044–S046 rejected, S047
  queued). S001–S039 byte-identical to base (wave-2 `CensusAndRows`).
- Rows touched old → new: none of S001–S039. Rows added this round and
  corrected after wave 2 (S044, S045, S046 teaches; S040, S042, S046 anchors;
  S040 teaches inference mark) are logged in the lesson "Registry changes";
  old cells in `verification/reject-rows-old-teaches.json`.
- Frontier: PROVINCE "Jekyll/base-path build tooling" moves from open to held
  Frontier ground (first entry plus offline gate; not Core). Render deploy
  semantics and accessibility conformance stay open.
- Sourced claim: C1 rests on S040–S043, opened this round.
- Mined mistakes (`corpus/lessons/round-29.md` "Mistakes"): round-28 counter
  checked quote shape, not truth; round-28 source gate rejected nothing; a
  wave-2 misroot. Fixes shown able to fail: C1 drops to 3/4 on a one-letter
  quote change (reproduced by wave-2 `ReopenS042`, `MistakesRowsCheck`);
  the reject-path witness fails on each named mutation and, after wave 2, on
  zero rejections.

## Trend verdicts

- **expansion: improved** — project-site base paths were open Frontier with
  no `baseurl`/`relative_url` statement in the corpus (wave-1
  `ScoutPriorSubpathKnowledge`); one new entry on four new mined tier-A rows,
  plus a new capability row.
- **quality: improved** — the round-28 counter weaknesses (ids only, quote
  shape only) are replaced in this round's counters by reason-tuple and
  retained-text checks, and a new gate ships committed fixtures that assert
  reason codes from birth; no existing knowledge entry was re-verified, so the
  corpus-quality observable itself moved only through the new entry.
- **discernment: improved** — the source gate screened 9 and rejected 3 with
  reasons and flips; wave 2 corrected two weak reject reasons (S044, S046)
  and six overstated entry sentences before landing; three QUALITY criteria
  added from the round-28 spot-check. Outside spot-check still owed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` "Project-site base-path triage — round 29" (S040–S043, S024) and "Base-path audit gate registry — round 29"; no non-author `[x]` sign-off.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` "Round 29 — attempt 1": real-input audit of three owned project-site snapshots (`.ufo/waves/round-29/real-input/out/`); no live property probed.
- [~] Instructions executable by an agent without oral context — tool `--help`, docstring and SKILL rows; wave-2 seats ran the tool, selftest and counters from the committed text alone (`w2/AttackEntryLimits.md`, `w2/RealInputReproduce.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — browser execution stays tabi's, source method chousa's (`w1/ConnectorSiblingOverlap.md`); PROVINCE Frontier updated in `7697990`.

## Round shape

- Shape: default, two v1 waves (policy `scripts/hyaku/ufo-wave-policy.json`).
- Wave 1 `kake-r29-w1` (build plus first falsifiers): 32 seats — scribe 11,
  critic 5, reviewer 5, scout 4, executor 3, connector 2, mutation-tester 2;
  attack seats 12/32. 0 dead. Registry `.ufo/waves/round-29/w1/swarm-registry.json`.
- Wave 2 `kake-r29-w2` (falsify, 39 attack items, each naming its target):
  39 seats — reviewer 18, critic 15, mutation-tester 4, sentinel 1, scout 1.
  0 dead. Registry `.ufo/waves/round-29/w2/swarm-registry.json`.
- No residual call. Round total 71 seats; attack seats 51/71.
- Each wave dispatched as one `task` call with the validator's `taskCall`
  unchanged, after a `granted` seat-gate line; both reservations released
  after every seat returned. No refusals.

## Process notes and installs

- Seat bound breaches, recorded: `NoHarmExistingGates` ran the freshness
  sweep without a section flag once at base and once at tip, which sends GET
  requests to pinned owned sites and `git ls-remote` to pinned repositories;
  its live results are treated as unverified. `HtmlParsingEdges` used the
  installed Chromium headless on local files only (proxy blackholed) as a
  parsing oracle; no challenge or access control was involved.
  `FieldsAndCounts` misrooted one report copy at the fleet root and removed it.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain`
  before this report shows no untracked kake round-29 file; the empty fleet
  directory `.ufo/waves/round-29/` predates the round and was left alone.
- Installs by seats: parse5 8.0.1 via npm into a sandbox (`HtmlParsingEdges`,
  DOM oracle); GNU time 1.9 built from https://ftp.gnu.org/gnu/time/time-1.9.tar.gz
  into `~/.local/bin/time` (`PerfPathological`, `/usr/bin/time` absent). No
  pacman. The L1 installed nothing.

## Open items

- C2 counter does not compare `id`, `page`, `resolved` or counts; tool misses
  `http:host/path` on https pages, percent-encoded or non-ASCII hosts and an
  unparseable base; srcset density grammar narrower than the HTML parser;
  html.parser tokenizer differences (tool docstring).
- Round-28 routed defects 1 and 2 (citing-set fixtures, round-27 families)
  carried as debt; the next citing-set round inherits them.
- L0 questions: none new. The round-24 policy-stop line stays open.

Stale-lane: respawn-per-round driver; attempt 1 pushed through `234524c`; no
other kake mission is open and no round 30 was started.
