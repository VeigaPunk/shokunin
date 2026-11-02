# revenger — round 84 report (hyaku run 23)

Lane repo: `fleet/shokunin-binary-forensics`, branch `main`. Base
`54a36bca7bc52d528026ca28beb51f4cab98fa69` (r83 tip + non-author
spot-check). Lane tip:
`5cdebb13713aa20778f3c6b5231c74dd3ba9a590` (pushed to origin/main).
Carry-in landing `67e1470e5b2492df7b86632c5b3bafabfdd3e023` (see Work
performed item 1).

## Work performed

Declared claims: **C1 coverage** (criterion A1v2 registration — the
artifact-graph family's archive-side pair `inspect_artifact` +
`extract_artifact` through real producer records, on the provider's
full available-operation set) and **C2 calibration** (orphan_sweep v5
supersession — the unmatched-bare-citation and LOG-corpus classes the
r83 closure routed as instrument gaps). Distinct axes, causally
separable, neither exploratory. No claim was declared on any other
axis; no exploratory claim.

- **Carry-in first (r83 non-author closure's three routed defects, all
  status-neutral).** Landed as
  `67e1470e5b2492df7b86632c5b3bafabfdd3e023` before any claim work:
  (1) `reports/round-83/v4-postlanding-recon.log` — cited by five
  surfaces (the r83 report ×2, `corpus/lessons/round-83.md`,
  SCORECARD, LOG) but never committed and lost with the r83 scratch —
  regenerated from committed bytes only (fresh scratch repo, HEAD =
  `60693f2` via fetch+update-ref, no checkout; disk = exactly the
  seven r82 receipts, byte-verified 7/7 against the landed blobs —
  `.ufo/waves/round-84/carryin-byteverify.log`, short shas match the
  r83 lesson pins) and run by the COMMITTED v4 blob (full sha
  `f520f8d69875d1ca83eb8daeddbffecb5f471bf5f5e6aba43bd97029fc2ea701`):
  `LANDABLE_ORPHANS=0` exit 0 — the load-bearing values the five
  surfaces cite reproduce; the receipt header discloses the
  regeneration provenance and the basis movement (fleet-reports 23→24;
  lessons=0, same minimal-reconstruction shape as the committed r83
  pre-landing receipt). (2) `reports/round-84/corrections.md`
  correction 1 — the five `f520f8d6…9701` abbreviated-sha drift sites
  named (fleet report ×1, lesson ×2, SCORECARD, LOG); the claims.md
  full sha governs; append-only, no in-place rewrite. (3) Correction
  2 — the `census-round-start-sanctioned2.log` pointer resolved three
  ways: the committed killed-run output body (`.ufo/waves/round-83/
  census-round-start-sanctioned.log`), the r83 verifier's independent
  re-run, and this round's exit-0 re-run receipt
  (`.ufo/waves/round-84/census-round-start-sanctioned.log`, 21 W01 +
  10 W04, zero E). Round-start census receipts (sanctioned + literal)
  landed in the same commit.
- **C1 work (coverage, A1v2 3/5 → 5/5).** Pre-probed both operations
  on the final fixture shape before any committed call
  (`reports/round-84/preprobe-arc-shape.log`: inspect exit 0, stderr 0
  bytes; extract exit 0, stderr 0 bytes; the output vocabulary the
  oracle pins). Authored the inert zip fixture `corpus/fixtures/
  arc-r84/` (`build_zip.py` 17/17 SELFCHECK re-opens the built bytes
  with the stdlib reader and re-derives every checked fact — entry
  order, names, sizes, CRC32s, content sha256s, fixture sha; NO
  byte-size constants anywhere; regen byte-identical across scratch
  and worktree builds; `truth.json` written by the generator's
  derive() from the built bytes with the Q07 hypotheses frozen BEFORE
  the committed runs; `R84Sample.zip` 508 bytes, sha
  `f1f983ef…bc59`: MANIFEST.txt 90 + data/blob.bin 48 +
  data/nested/note.md 32, ZIP_STORED, fixed DOS timestamp). TWO real
  producer runs from the lane root: `rea inspect-artifact
  corpus/fixtures/arc-r84/R84Sample.zip --format json` (exit 0,
  stderr 0 bytes, 9481 bytes stdout, Evidence
  `ev_753cfca9daf92857826b62400bd2f4b09ba6cbb4670fd449e3250c246ca138ba`)
  and `rea extract-artifact …` (exit 0, stderr 0 bytes, 3930 bytes
  stdout, Evidence
  `ev_07e34a9493848c91095a3355069907df24449999088c87a558b45f8d33c77467`;
  the extract output root is the producer's own host-temp directory —
  nothing written inside the lane repo, nothing executed). Oracles
  `ORACLE OK (36/36 checks)` and `ORACLE OK (31/31 checks)` — every
  BYTE check re-derives its expected value from the fixture bytes;
  producer-internal ids checked for FORM only; the HYP checks are the
  pre-registered Q07 predictions, recorded as predicted. **Instrument
  erratum (pre-after-run, mined):** the freeze-time ag_probe2 v2.0
  (sha `6e1c07b5…d1e1`) scanned `runs/round-*/` one level deep and
  could never see the landed `runs/round-84/<operation>/inspection.json`
  layout — the c1-only separability dry-run printed 3/5 against
  LANDED records before any after-run receipt existed; v2.1 (rglob
  `inspection.json` by name, sha `f9772ab1…1990`) re-pinned with the
  erratum appended to claims.md; correction commit `f3d3902`; the red
  re-run printed unchanged values.
- **C2 work (calibration, orphan_sweep v5).** Both routed gaps close
  inside the standing instrument (`reports/round-84/orphan_sweep5.py`,
  sha `d9a7ba174ce3c30a4414fcebe8e074ea00d58bfce4cfbf2c2cdb76f888ca46cb`;
  v4 blob byte-untouched — full sha per corrections.md). Change 7: an
  unmatched extension-bearing bare token is RECORDED as an absent row
  (filename test: no `..`, not all digits+dots, tail extension; the v4
  BARE_UNMATCHED_SKIPPED leg re-pinned to the prose class; disclosed
  noise: dotted JSON field paths; absent never gates — exit codes
  0/1/64 unchanged). Change 8: LOG.md joins the citation corpus
  (`SWEEP_CORPUS` gains `log=`). Red pair over ONE tree (pre-carry-in
  worktree): `v4-invisible-red.log` (v4: ZERO instrument rows name the
  bare-cited `v4-postlanding-recon.log`; matched=302
  unmatched_skipped=1408) vs `v5-red-unmatched-absent.log` (v5: the
  recorded absent row `bare-token unmatched`, unmatched_recorded_absent=47,
  CITED=987 vs 705). Resolved by the carry-in landing. Selftest 18
  legs + pass; THREE frozen one-substitution sed mutants each die
  exit 1 attributed (bare-token / unmatched-absent / log-corpus
  classes), demonstrated at the freeze
  (`sweep5-mutant-kill.log`) and re-run from the committed blob at
  adjudication (`sweep5-mutant-kill-after.log`). The real-tree receipt
  ran over the pre-adjudication-text worktree (the r83 receipt
  ordering — the LOG/SCORECARD/lesson texts are appended after the
  run, disclosed in the receipt header): it prints the target token
  bare-token-normalized COMMITTED and named in no absent row; its
  three LANDABLE_ORPHANS rows are the instrument's documented
  conservative-ambiguity rule firing on this round's own then-
  uncommitted same-basename receipts (`c1-only.log`, `c2-only.log`,
  `noharm-diff.txt` against their committed r81/r82/r83 twins) —
  corrected by a post-run note in the receipt, resolved by the
  adjudication commit (post-adjudication verification re-run:
  `LANDABLE_ORPHANS=0` exit 0, basis `fleet-reports=24 lessons=49
  log=1`).
- **§7 fresh-start gate.** r71/r72/r73 rejected closures re-read and
  spot-checked (all three are K-admission claims whose wave Q-review
  surface never existed or never settled on this host — a do-nothing
  control reaches each identically here). Ruled out with fresh probes
  (2026-11-02, receipt `reports/round-84/freshstart-probes.log`): F
  android (`REA_JADX_MCP_JAR` UNSET, no jadx on PATH — S448 stands;
  F4's honest exception stays 10/11); macho/signature providers
  (`unsupported_host`, 8 groups — S453); K admissions (r74 L0 re-read,
  unanswered — routed around, never treated as answered); criterion C
  repair (§9 sizing, r78–r83 standing disposition); criterion R full
  extension / criterion N attribution pair (stay routed — this round's
  calibration claim is the v5 classes instead). C1's route is the one
  every standing ruling-out map left open (the archive-side pair,
  "available-but-unrecorded", r81/r82 scorecards) — this is that
  round.
- **Frontier.** SOURCES rows S466–S468 opened and appended inside the
  Registry after S465 (below). Census receipts: round start sanctioned
  exit 0 (21 W01 + 10 W04, the same disclosed classes as r74–r83; the
  first attempt hit the shell tool's own 120 s default timeout — the
  r83 mined class recurring — stopped and re-run foreground with an
  explicit generous timeout, exit 0; mined); literal form exit 2
  (disclosed r74–r83 lineage). Round end:
  `reports/round-84/census-after.log` — sanctioned worktree exit 0
  (zero E) after the census itself caught the E12 ×3 row-placement
  defect (the three new rows first appended past `## Leads`, outside
  the Registry — the r80 mined class recurring; rows moved inside the
  Registry, re-run exit 0; mined); landing-archive census fires E12 ×3
  (the landing carries the pre-fix layout; resolved-by = the
  adjudication commit). SOURCES grammar checked mid-flight (S468's
  quoted receipt row initially carried a literal pipe, NF=14 — fixed
  before the landing, the r83 S465 class).
- **Assimilation.** `considerthese/` exists (8 digests, 2026-10-20
  through 2026-10-28); re-read this round: the live proposals target
  the blocked K-route, cross-round ledger scopes, or operator-owned
  host surfaces — none adoptable this round; adopted nothing —
  Assimilation: none — shokuknow unreachable.
- **L2 floor.** No dispatch surface on this host (the r74 L0 stands,
  re-read unanswered); every verdict re-derives from committed bytes.

## Landed changes

All in the appended `LOG.md` round-84 entry; full gate/receipts/
mistakes in `corpus/lessons/round-84.md`; SCORECARD section appended.

- `67e1470e5b2492df7b86632c5b3bafabfdd3e023` — carry-in: the
  regenerated r83 receipt + corrections.md + 7/7 byte-verify + round-
  start census receipts (pushed).
- `45c8b42fe4f79d6133a0546b58abeefe7a6b5efe` — round-84 freeze:
  claims + sha pins + `orphan_sweep5.py` + `ag_probe2.py` (v2.0) +
  reds (`v4-invisible-red.log`, `v5-red-unmatched-absent.log`,
  `ag2-red.log`) + `preprobe-arc-shape.log` + `sweep5-mutant-kill.log`
  + `freshstart-probes.log` (pushed).
- `d77f997428b715375e72bfb55b00b8e43d3118f5` — landing (SOURCES rows
  only — the treecommit directory-args no-op, mined) and
  `8e21e8f238dccc9d95c5a5a1e84500daf275979f` — landing completion: the
  arc-r84 fixture (zip + generator + truth + oracle), both producer
  records (inspection/receipt/LEDGER/oracle.log/stderr), all 14 files
  explicit (pushed).
- `f3d3902e830ceb55f5524cac9724c157b13a0d98` — instrument correction
  (pre-after-run): ag_probe2 v2.1 + claims erratum + `ag2-red-v21.log`
  (pushed).
- `5cdebb13713aa20778f3c6b5231c74dd3ba9a590` — adjudication: SCORECARD
  round-84 section, LOG entry, `corpus/lessons/round-84.md`, the
  SOURCES row-move fix, after/separability/noharm/census receipts
  (pushed). All twelve files verified worktree == landed blob
  post-commit.

## Before → after measurements

- **C1 (coverage, A1v2).** Counting command:
  `PYTHONUTF8=1 python -B reports/round-84/ag_probe2.py
  <archive-extract>/corpus` (the registered instrument, v2.1, sha
  `f9772ab1…1990`; the v2.0 freeze sha and the erratum are pinned in
  `reports/round-84/claims.md`). Before (base archive `54a36bca`):
  `A1V2_RECORDED=3/5 score=6.00` with `extract_artifact` and
  `inspect_artifact` unrecorded (`reports/round-84/ag2-red.log` +
  `ag2-red-v21.log`, the latter with the corrected instrument — same
  values). After (landing archive `8e21e8f2`): `A1V2_RECORDED=5/5
  score=10.00` with both recorded (`reports/round-84/ag2-after.log`,
  which also carries the oracle re-runs over archive bytes
  `ORACLE OK (36/36)` + `ORACLE OK (31/31)`, the record-stdout
  byte-identity checks against the receipt pins, the byte-identical
  regen, and the frozen holds `A1_RECORDED=3/3` + `F4_COVERAGE=10/11`).
  Measured commits: `54a36bca` → `8e21e8f2`. F4 (family presence),
  the r82 A1 triple, and K (8/15) unchanged, as frozen.
- **C2 (calibration, v5).** Counting command:
  `PYTHONUTF8=1 python -B reports/round-84/orphan_sweep5.py --lane
  <lane-dir> --fleet <fleet-root> [--format full]` (red side:
  committed `reports/round-83/orphan_sweep4.py`, full sha
  `f520f8d6…c2ea701`). Before: v4 over the pre-carry-in tree records
  NOTHING for the bare-cited `v4-postlanding-recon.log`
  (`v4-invisible-red.log`: zero instrument rows, matched=302
  unmatched_skipped=1408); v5 over the same tree records the absent
  row (`v5-red-unmatched-absent.log`: `SWEEP absent
  v4-postlanding-recon.log | bare-token unmatched`,
  unmatched_recorded_absent=47, `SWEEP_CORPUS fleet-reports=24
  lessons=48 log=1`, CITED=987). After: selftest 18 legs +
  `SWEEP_SELFTEST=pass` exit 0 from the committed blob
  (`sweep5-selftest-after.log`); all three sed mutants die exit 1
  attributed (`sweep5-mutant-kill-after.log`); real tree
  `sweep5-real-after.log` — the target token bare-token-normalized
  COMMITTED, named in no absent row, `SWEEP_CORPUS fleet-reports=24
  lessons=48 log=1` (the three LANDABLE_ORPHANS rows + the exit-1
  corrected by the post-run note: the conservative-ambiguity rule on
  this round's own then-uncommitted same-basename receipts);
  post-adjudication verification over the fully committed tree:
  `CITED=1015 COMMITTED=955 LANDABLE_ORPHANS=0 ABSENT=60` exit 0,
  basis `fleet-reports=24 lessons=49 log=1`. Measured commits:
  `67e1470`/`45c8b42` (red) → adjudication `5cdebb1`.
- **No-harm.** `reports/round-84/noharm-diff.txt`: protected paths
  empty on `45c8b42..8e21e8f2` (15 files, 704 insertions, 0 deletions
  — additions only); v1–v4 sweep instruments + ag_probe + f_probe4
  absent from the range; FRESH_ROWS 18/18. Separability: `c1-only.log`
  (A1v2 5/5 + oracles OK with v5 ABSENT) / `c2-only.log` (selftest
  pass with fixture/records/ag_probe2 ABSENT), both from the
  pre-freeze base `67e1470`.

## Sources & frontier

`SOURCES.md` rows **465 → 468** (counting command:
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
= 468; malformed rows 0; NF=13 on all three new rows; the three rows
sit inside the Registry directly after S465 — the first placement was
outside the section, E12 ×3 self-caught by the round-end census, fixed
and mined). All three opened this round; C1 is sourced by S466+S467
and C2 by S468:

- S466 — the A1v2 provider surface (`rea capabilities` +
  `--help` × 2 + the preprobe receipt, own-work tier A; quote:
  "Extract regular contents of supported artifacts; DMG extraction is
  unavailable").
- S467 — the two producer records + fixture (own-work tier A; oracle
  OK 36/36 + 31/31, both exit 0, stderr 0 bytes).
- S468 — the unmatched-bare-citation class evidence (the red pair +
  the r83 closure's routed-defect note, own-work tier A).

Census: round start sanctioned exit 0 / literal exit 2 (disclosed
lineage); round end sanctioned exit 0 (after the census-caught E12 ×3
placement fix) / literal exit 2 / landing-archive E12 ×3 resolved by
the adjudication (`reports/round-84/census-after.log`, raw logs in
`.ufo/waves/round-84/`).

## Trend verdicts

- **expansion: improved** — the artifact-graph family's archive-side
  pair now carries real oracle-checked records on the provider's full
  available set (A1v2 3/5 → 5/5); F unchanged (android hard-gated), no
  knowledge admission (K 8/15 untouched — operator-blocked route
  re-checked, not attempted).
- **quality: improved** — A1v2 extends the registered criterion to the
  provider's own declared available set with the denominator disclosed
  pre-run and the identity oracle separating byte-derived from
  pre-registered hypothesis checks; the standing hygiene instrument's
  two routed blind spots became machine-caught inside v5 with three
  mutation-checked switches; the instrument's own scan-shape defect
  was caught by the round's separability machinery before it could
  produce a false receipt.
- **discernment: improved** — seven real defects mined this round
  (`corpus/lessons/round-84.md` ## Mistakes): the record-layout vs
  scan-shape instrument defect (separability-dry-run-caught before any
  after-run receipt), the treecommit directory-args silent no-op
  (post-commit diff check), the shell-heredoc truncation class
  (post-write tail check; the LOG attempt died at parse before any
  write), the census default-timeout recurrence (r83 class, new
  place), the SOURCES row-placement E12 ×3 (census-caught), the S468
  literal-pipe NF defect (mid-flight grammar check), and the
  count-from-intent placeholder (measure-before-write, before the
  freeze). The carry-in receipts were regenerated from committed bytes
  first-hand, not taken on trust; the one expected-GREEN line the run
  disagreed with (the real-tree exit) is corrected by a post-run note
  in the receipt itself.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns,
  checklists, cited sources — unchanged this round; the routed need
  stands: a non-lane reviewer re-confirming the CURRENT bytes
  (`corpus/lessons/round-69-verifier-spotcheck.md`); this round added
  no SKILL byte and claims no promotion signal.
- [~] At least one end-to-end domain task executed and logged in
  LOG.md — this round's two producer runs (inspect + extract) on the
  authored inert archive, oracle-checked over archive bytes:
  `corpus/live/runs/round-84/` (receipts `exit_code 0`, Evidence
  `ev_753cfca9…138ba` / `ev_07e34a94…77467`), LOG.md round-84 entry,
  commits `d77f997`+`8e21e8f2`; no independent outside verifier this
  round.
- [~] Instructions executable by an agent without oral context — the
  round's instruments run from their committed bytes with declared
  exits (`orphan_sweep5.py --selftest` 18/18 exit 0; `ag_probe2.py`
  5/5; `oracle_check.py` usage in its docstring; `build_zip.py` regen
  byte-identical); no independent outside instruction verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE
  byte-unchanged in `45c8b42..5cdebb1` (`git diff 45c8b42..5cdebb1 --
  PROVINCE.md` empty); the records are scoped to the observed family,
  operations and authored inputs (LEDGER Q10 scope notes; DMG/PKG/
  nested-container surfaces unclaimed per the provider's own
  limitations); ADJ-06 unchanged, reported-not-absorbed.

CLOSURE-PREP: re-runnable by the closure judge at the final tip
`5cdebb13713aa20778f3c6b5231c74dd3ba9a590` — every expected value
below was measured first-hand at report time, not predicted: (1)
`git show 5cdebb13713aa20778f3c6b5231c74dd3ba9a590:reports/round-84/orphan_sweep5.py`
sha256 must print `d9a7ba174ce3c30a4414fcebe8e074ea00d58bfce4cfbf2c2cdb76f888ca46cb`,
then `python -B <blob> --selftest` → measured 18 `=ok` legs +
`SWEEP_SELFTEST=pass` exit 0; the three frozen sed mutants (recipes in
`reports/round-84/claims.md`) each die exit 1 attributed
(`sweep5-mutant-kill-after.log`); (2) the standing sweep over the lane
repo worktree at the tip → measured `CITED=1015 COMMITTED=955
LANDABLE_ORPHANS=0 ABSENT=60` exit 0, basis `SWEEP_CORPUS
fleet-reports=24 lessons=49 log=1` (cite basis lines first, never bare
CITED across corpora); `grep -c "v4-postlanding-recon"
<full-receipt>` on instrument rows finds the token ONLY as
bare-token-normalized committed; (3) `python -B
reports/round-84/ag_probe2.py <extraction>/corpus` over a
`git archive 5cdebb1…` extraction → measured `A1V2_RECORDED=5/5
score=10.00`, plus `python -B reports/round-82/ag_probe.py` →
`A1_RECORDED=3/3` and `python -B reports/round-81/f_probe4.py` →
`F4_COVERAGE=10/11`; (4) the oracle re-runs over the archive bytes:
`python -I -B corpus/fixtures/arc-r84/oracle_check.py
corpus/fixtures/arc-r84/truth.json
corpus/live/runs/round-84/inspect-artifact/inspection.json
corpus/fixtures/arc-r84/R84Sample.zip` → `ORACLE OK (36/36 checks)`
and the extract sibling → `ORACLE OK (31/31 checks)`; (5) `git archive
5cdebb13713aa20778f3c6b5231c74dd3ba9a590 | tar -x` then
`sources-census.sh validate <extraction>` → measured exit 0, zero
E-findings, 31 W (the round-84 lesson and the corrected SOURCES layout
travel inside the archive, so the landing-time E12 ×3 are resolved);
(6) the red/green pair is re-runnable from the committed receipts:
`v4-invisible-red.log` + `v5-red-unmatched-absent.log` over one tree
(pre-carry-in), `ag2-red-v21.log` over the base archive — the
instrument shas and reconstruction recipes are pinned in
`reports/round-84/claims.md`.
