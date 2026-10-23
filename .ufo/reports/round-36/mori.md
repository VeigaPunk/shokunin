# mori round 36 — fleet & host observability (森), attempt 2 (L1 MoriR36)

Lane HEAD at report time: `7c6fbac50a05051de8ff701c216124b925adfe59` (pushed; `ahead=0`; post-close wave-2
reports sweep). Round base
(entering): `6bd57097` (round 35 closed `rejected-honest-stop`, MANIFEST `rounds[531]`).
Attempt 1 of this round died with the phase-4 orchestrator (~09:30 -03); its committed outputs were inherited per
addendum §5 and are named in `corpus/lessons/round-36.md` M3.

## Work performed

Declared claims (2, per the r35-rejection sizing rule):

1. **C2 (measured, operability; capability acquisition)** — the SOURCES append-only gate
   `tools/mori-sources-appendonly.py` (promoted from the round-35 wave script) with new deleted-row detection, a
   fixture self-test, and a `SKILL.md` registry row. Target axis: operability. Sourced claim: both claims rest on
   S205 (fleet `CORPUS.md` §SOURCES.md contract at pinned commit `6a1dd8ce`), opened and verified this round
   (w2/RevSupS205.md PASS: copy sha256 `88556402…` == fetched body; quotes contiguous ≤25 words).
2. **C1 (exploratory, freshness technique; declared before data at `5842dc0` after the w1 critic showed the frozen
   byte predicate cannot carry a freshness verdict)** — the source-drift byte probe `tools/mori-source-drift.py`:
   the first reusable whole-registry re-fetch over the committed `sources-r<N>` copies with per-state
   classification. Verifies only as `unprovable-but-better` with a named non-author reviewer; **none exists inside
   the round, so C1 lands `unprovable`** with the hyaku closure session named as the reviewer of record.

Work items, each with an evidence pointer:

- Inherited attempt-1 state re-verified and landed: contract + frozen v2 counters, c0 receipts (25/25 controls
  unmet under v2), 28 wave-1 reports, exploratory declaration (`da12b37`, `c1a026c`, `5842dc0`); the C1 tool that
  attempt 1 never delivered was rebuilt by L1 to the frozen interface (selftest PASS 4 cases).
- Data commit `bf0df77`: the three tools, SOURCES S205–S220 + copies, QUALITY 103–105, SKILL Round36 rows,
  knowledge note, wave evidence.
- Both claims scored at the clean tip `bf0df77`; receipts committed in the integration commit `9ca8f2e`.
- Wave 2 (66 seats, orchestrator-inline per the mid-flight directive): 45+ reports at report time; every FAIL is a
  documentary defect repaired in `9ca8f2e`/`6827d6e` or a frozen-byte residual disclosed below — the measurement
  core (ExecReC2A, ExecReC1A, RevC1Receipt, RevC2Receipt, RevC2Oracle, RevPredIdentity, RevAppendDebt,
  RevR13R16Gates, RevCensusRows, RevQuality103/104/105, RevSupS205–S220) is PASS-clean.
- Routed round-35 repairs: 18 in-place SOURCES ids superseded (S205–S220; violations stay listed — a superseder is
  a disposition, not a discharge, QUALITY 102); gate registered with self-test; M4 index-clean check landed and
  run after every helper commit (QUALITY 103); operator items (LOG.md:1801 setting value, `refs/jj/keep 3b19cac`,
  `.scratch/` 2026-10-21, SHONEN promotion) untouched and operator-owned.

## Landed changes

(all lane commits via `scripts/hyaku/jj-lane.sh`, push verified; author `mori-shokunin <mori@shokunin.local>`)

- `da12b37` freeze C1/C2 contract + counters + before receipts (attempt 1)
- `c1a026c` C0 receipts; v2 counter re-design after met controls (K9/J11/K13); 25/25 controls unmet under v2
- `5842dc0` C1 declared exploratory before data (axis-fit defect, w1/CritAxisFit)
- `bf0df77` data commit: tools + SOURCES S205–S220 + copies + QUALITY 103–105 + SKILL rows + knowledge note + w1 evidence
- `9ca8f2e` integration: counter receipts (c1-after, c2-after, drift-live), freeze-v3 pin record, w2 spec/dispatch/
  payload/validator log + 34 w2 reports, lesson round-36 (M1–M4), SCORECARD round-36 section + capabilities row,
  LOG entry, README Round-36 coverage rows, documentary repairs (contract :13 reconciliation + oracle-prose
  amendment, nine-row enumeration with commands + open-time shas in note/SKILL/QUALITY 105-addendum/README,
  S205 used-by correction old→new logged in the lesson Gate)
- `6827d6e` close-out: contract :4-5 history correction, novelty bound (w2/CritC1Axis), disposition wording,
  post-landing check records in the dispatch log
- `8ff9bba` final wave evidence: 11 late w2 reports (45 total on disk), the RevSupS214S217 repairs (12 mined
  rows' `used-by` repointed to the now-citing lesson, old→new logged; per-row Gate lines with URL/access-date/
  quote; SupS183 label hazard recorded), dispatch-log TZ annotation
- `5a2fe05d` close-out receipts: `evidence/census-end.txt` (exit 0, `mori ok`; W04 lines only), C1 re-score at
  `8ff9bba` (receipt `evidence/c1-after-final.txt`), C2 re-score at `8ff9bba` (`C2=met`, seed
  13468019365462637710), final index-clean/gate records, wave-slot release, freeze-v3 contract pin annotation
  (tip blob `f505594b…` after the `:4-5` history correction — predicate sentences byte-identical)
- `b7874b19` late wave-2 report ExecReC2B (46 reports on disk)

Each change ties to a LOG.md round-36 entry line and the commit above.

## Before → after measurements

- **C2**: before — `python3 .ufo/waves/round-36/count-c2.py 6bd57097` → `tool_absent C2=unmet` exit 1
  (`evidence/c2-before.txt`). After — same command at `bf0df77` → blind arm 24/24 sandbox histories match the
  run-time-hidden truth; real arm == independent oracle at rev 6bd57097 (base `f10a320d`), 18 ids,
  `appendonly_violations=18 deleted=[] superseded=[S069,S182,S193] round_changed=[S182,S193]`; `C2=met` exit 0,
  seed 15440749816798970567 (`evidence/c2-after.txt`, counter sha `c7edaacf…` == `evidence/freeze-v3.txt`).
  Re-verification: 7 fresh draws + fixed seeds 42/7 all `C2=met` (w2/ExecReC2A.md; determinism across
  fixed seeds, w2/ExecReC2B.md, which also names a scratch-path-collision robustness candidate for r37);
  re-scored `C2=met` at the
  integration tip (seed 14475316978074684109); oracle re-derived byte-identical by a seat that never read the
  counter (w2/RevC2Oracle.md). **Frozen-counter note (w2/RevC2Oracle M5): the real arm binds the predicate-pinned
  entering rev 6bd57097 exactly as P-C2 specifies — it is not tip-history evidence.**
- **C1**: before — `python3 .ufo/waves/round-36/count-c1.py 6bd57097` → `tool_absent C1=unmet` exit 1
  (`evidence/c1-before.txt`). After — same command at `bf0df77` → blind arm 40/40 mismatches=0; real arm
  `rows=220 oracle_fetched=58 oracle_fresh=49 oracle_drifted=9 oracle_excluded=0 mismatches=0`; `C1=met` as
  **byte-behavior evidence only**, exit 0, seed 7388485190103051243 (`evidence/c1-after.txt`, counter sha
  `86dd3b7a…` == freeze-v3). Full-tool live run: `MORI_SOURCE_DRIFT rows=220 fresh=49 excerpt=0 drifted=9
  unavailable=0 no-copy=162` (`evidence/drift-live-r36.txt`). Re-verification at the final tip `8ff9bba`:
  `C1=met` again (blind 40/40 mismatches=0, real arm clean), seed 15951461284190234552
  (`evidence/c1-after-final.txt`). The claim itself: **`unprovable`** — no named
  non-author reviewer inside the round (hyaku closure named of record).
- Round landing gate: `python3 tools/mori-sources-appendonly.py <tip> --round-base 6bd57097` →
  `round_changed=[]` exit 0 at `bf0df77`, `9ca8f2e`, `6827d6e`. Index: `MORI_INDEX_CLEAN staged=0
  intent_to_add=0` exit 0 after every helper commit.
- Disclosed frozen-byte residuals (cannot repair post-data without voiding receipts; registered as r37 debt):
  `count-c2.py:70-82` SIGKILLs only its own timed-out sandbox child on a tool timeout (no fleet/host kill);
  `count-c1.py`'s module docstring still says v1 (cosmetic; predicate bytes frozen); the frozen counters do not
  detect a SOURCES.md delete+restore inside a round (w2/CritC2Axis counterexample — needs a successor counter
  under a new freeze); the c1 receipt exercised no 429/4xx oracle path (`oracle_excluded=0`).

## Sources & frontier

- Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori` — round start (attempt-1
  receipt `evidence/census-start.txt`): 204 rows, exit 0; round end (w2/ExecCensusEnd.md at the data tip, re-run
  at the final tip): **220 rows, exit 0** (`mori ok`; +2 benign W04 duplicate-URL lines for S218/S220, scope-cell
  reworded by design; r35 S201 precedent). Command exit codes: 0 and 0.
- Rows added by tier: 16 rows S205–S220 — 15 mined (A-tier: S205 fleet CORPUS contract, S206 RFC 6585, S207 jj
  docs, S208 NIST SP 800-122, S209 RFC 8785, S210 git-rev-parse, S212/S213 v7.2 block docs, S214 part_stat.h,
  S215 blk-core.c, S216 blk-mq.c, S217 blk_types.h, S218/S219 kernel iostat commits, S220 sysstat iostat.c) +
  1 rejected (S211 PMC mirror — duplicate of S056's URL, kept as rejection evidence).
- Rows touched old→new: S205 `used-by` `tools/mori-source-drift.py` → `corpus/knowledge/source-drift-r36.md`
  (mined used-by must cite the citing entry; logged in the lesson Gate). No other existing row changed
  (round gate `round_changed=[]` at every tip).
- Frontier rows advanced: none closed; the drift probe and the append-only gate enter the README coverage map as
  new ground (Round-36 rows); FR rows unchanged. Re-opened rows w2-verified: S205–S209, S211–S213, S218–S220 PASS;
  S210 PASS as a row with a drifted copy (post-copy asset rebuild; taught prose byte-identical).
- Frontier step: mistake mined (lesson M1–M4: axis-fit, number-drift, landing, scope); C2 is the round's sourced
  claim (S205 opened and re-verified this round).

## Trend verdicts

- **expansion: improved** — capability row added (SOURCES append-only gate, first-working round 36,
  `SCORECARD.md`); one knowledge entry on previously uncovered freshness-technique ground
  (`corpus/knowledge/source-drift-r36.md`, citing mined S205); 16 SOURCES rows admitted with located quotes; two
  README coverage-map rows.
- **quality: improved** — the nine-row drift enumeration now carries commands, dates and open-time shas at four
  sites (the stale seven-row count was caught by five independent wave-2 seats before landing and repaired,
  lesson M2); freeze integrity re-pinned and verified (freeze-v3; counters byte-identical to v2); S205's used-by
  corrected; no admitted entry failed its re-check (w2/RevQuality105 re-derived all seven original witnesses and
  the two new ones).
- **discernment: improved** — every wave-2 documentary FAIL (18 reports) was either repaired in the integration/
  close-out commits or disclosed as a frozen-byte residual with an r37 repair path; nothing was waived silently;
  the exploratory claim is reported `unprovable` with the reviewer condition named rather than self-attested
  (w2/CritAdmission/CritC1Axis concur with the disposition).

## SHONEN

- [~] Decision tables — the drift-probe state table (`corpus/knowledge/source-drift-r36.md`) and the Round36 SKILL
  rows are landed with re-runnable entries; no named non-author verifier (w2/RevSkillRows PASS on registry fields).
- [~] End-to-end task logged — the full round is in `.ufo/waves/round-36/dispatch-log.txt` + LOG.md round-36 entry
  (both committed at `9ca8f2e`).
- [~] Executable without oral context — every command in this report runs from the committed bytes at the named
  tips (receipts committed at `9ca8f2e`).
- [~] No cross-domain bleed — `git diff 6bd57097..6827d6e` is lane-local; PROVINCE untouched; the one scope
  wording slip (restore instruction) was repaired in the integration commit (lesson M4); the frozen-counter
  sandbox SIGKILL is disclosed, not hidden.

## Round shape, waves, seats

- Shape: **one v2 wave (w2, 66 seats) + inherited attempt-1 waves** (c0 25 controls, w1 33 build/falsify).
  Policy: `scripts/hyaku/ufo-wave-policy-v2.json` (band 64–128; validator exit 0; wave-slot grant
  `granted lane=mori wave=mori-r36-w2 seats=66 live=135 cap=256`). The w2 `taskCall` was handed to the
  orchestrator and dispatched inline per the mid-flight directive (no seat spawned from the L1 session; the w2
  registry records null agent ids as a side effect — lesson note).
- w2 role mix: 35 reviewer, 10 executor, 7 mutation-tester, 4 critic, 3 sentinel, 3 scribe, 2 revenger,
  1 connector, 1 scout — attack seats (reviewer+critic+mutation-tester+sentinel+revenger) = 51/66 (77%).
- Round total: 25 + 33 + 66 = **124 seats** (≤128).
- Dead seats: w1 MutC1Novel, MutC2Novel (provider rate limit, "Reached free model rate limit… reset in 4 hours
  56 minutes"); w1 CritC1Counter, CritC2Counter refused-hold (provider `cyber_policy` flag, not retried); w1
  BuildDriftTool never returned (scratch build only). w2 RevSkillRows returned late (empty relay, full report on
  disk, PASS). At the final sweep **50 of 66 w2 reports** are on disk and committed; the 16 never-returned seats
  (remaining mutation-testers/sentinels/revengers/scribes/connector/scout/four executors/one reviewer) were still
  running at the freeze deadline with no known dead — their items are partially covered by landed seats (all four
  critics, the C2 re-scores, both interface reviews, and 2 of 7 mutation-testers landed), and every landed FAIL is
  repaired or disclosed above. This partial-settlement is reported honestly as a conformance limitation; no
  refusing or shrinking of the wave occurred.
- Wave-2 attack results: 19 FAIL reports — all documentary, all repaired (13 in `9ca8f2e`, 3 in `6827d6e`,
  2 in `8ff9bba` — the RevSupS214S217 used-by/Gate-letter repairs, plus the TZ annotation) or disclosed as
  frozen-byte residuals above; the measurement core is PASS-clean.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Tool installs

None this round (no seat reported an install; the counters and tools run on stock python3/git/curl).

## Open L0 questions

- `<lane> | round-36 | mori`: none new filed by the round. Carried operator items (r35 §6 item 5) remain named in
  the report, not acted on.
