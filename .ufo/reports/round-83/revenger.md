# revenger — round 83 report (hyaku run 22)

Lane repo: `fleet/shokunin-binary-forensics`, branch `main`. Base
`60693f2ce6b086ea3f0ee84fe27a8f8a13d46f46` (r82 tip + non-author
spot-check). Lane tip:
`b56d81bd83811b3e122f24cb81352472d2afd554` (pushed to origin/main).
Carry-in landing = the base itself: `60693f2` (see Work performed
item 1).

## Work performed

Declared claims: **C1 coverage** (criterion A1 completion — the
artifact-graph family's third operation `decode_interface_builder`
through a real producer record) and **C2 calibration** (orphan_sweep v4
supersession — the bare-filename citation class). Distinct axes,
causally separable, neither exploratory. No claim was declared on any
other axis; no exploratory claim.

- **Carry-in first (r82 non-author closure's first obligation).** The
  seven cited green receipts (`ag-after.log`, `sweep3-selftest-after.log`,
  `sweep3-mutant-kill.log`, `sweep3-real-after.log`, `c1-only.log`,
  `c2-only.log`, `noharm-diff.txt`) landed via treecommit explicit paths
  (the b1e0c60e receipt-completion class): `60693f2ce6b086ea3f0ee84fe27a8f8a13d46f46`,
  7 files, 433 insertions; all seven byte-verified worktree == landed
  blob; all `git show`-readable. Standing orphan_sweep v3 re-run over
  the post-landing tree went LANDABLE_ORPHANS=2 → 0, receipted both
  states: `.ufo/waves/round-83/sweep-pre-landing.log` (exit 1,
  `CITED=386 COMMITTED=372 LANDABLE_ORPHANS=2 ABSENT=12`) and
  `.ufo/waves/round-83/sweep-post-landing.log` (exit 0, `CITED=386
  COMMITTED=374 LANDABLE_ORPHANS=0 ABSENT=12`).
- **C1 work (coverage, A1 2/3 → 3/3).** Pre-probed the operation's real
  surface before any committed call (`reports/round-83/preprobe-app-shape.log`:
  the parser rejects a bundle without a supported Info.plist layout —
  exit 1; standard-LEB128 nib varints die "NIBArchive variable integer
  is too long" — the parser's terminator-bit encoding is the inverse of
  LEB128; the final-shape vocabulary probe). Authored the inert
  two-document `.app` bundle `corpus/fixtures/app-r83/` (generator 18/18
  SELFCHECK re-parses the built bytes and re-derives every oracle-checked
  fact; regen byte-identical across three scratch builds; fixture shas
  `1bb04ef8…319e` / `f0746e35…315e` / `7953ce25…566`). One real
  `rea decode-interface-builder corpus/fixtures/app-r83/R83Sample.app
  --format json` run from the lane root: exit 0, stderr 0 bytes,
  Evidence `ev_260481425d1a43fbbc0327c2033aafda8d7a51599c520a74b9985c3c550610f8`
  (`corpus/live/runs/round-83/`). Oracle `ORACLE OK (44/44 checks)` =
  26 BYTE + 18 pre-registered Q07 HYP checks (the HYP set frozen in
  `truth.json` at the freeze commit, before the committed run), re-run
  over the landing-archive bytes. Evidence pointers: freeze
  `28e8c290235f2e6d588a9b81538b61ae50e533b7`, landing
  `75298d427d97c5668753969fecf54d98630735b7`.
- **C2 work (calibration, orphan_sweep v4).** The carry-in demonstrated
  the class live: five of the seven uncommitted receipts were cited by
  BARE filename, invisible to v3's lane-domain filter (v3 saw 2 of 7).
  `reports/round-83/orphan_sweep4.py` (sha `f520f8d6…9701`; v3 blob
  unchanged `af64b4c5…b8748` re-verified over the landing archive)
  adds change 6 — bare-filename receipt normalization against the
  basename index of HEAD ∪ working tree, conservative ambiguity
  resolution, four new selftest legs (13 total) with an embedded
  disabled-twin mutant leg. Falsifiable red/green over a MINIMAL
  pre-landing reconstruction in scratch (fresh repo, HEAD=`c153e448`
  via fetch + update-ref — no checkout — plus exactly the seven
  receipts on disk): committed v3 exits 1 with `LANDABLE_ORPHANS=2`
  while seven landable receipts exist (`v3-prelanding-recon.log`); v4
  over the same tree flags 9 orphan rows covering all seven files
  (`v4-prelanding-recon.log`); v4 over the reconstruction with HEAD =
  the carry-in landing prints 0, exit 0 (`v4-postlanding-recon.log`).
  Frozen sed mutant (one substitution, line 87) dies exit 1 attributed
  (`sweep4-mutant-kill-after.log`).
- **§7 fresh-start gate.** r71/r72/r73 rejected closures re-read and
  spot-checked (all three are K-admission claims whose wave Q-review
  surface never existed or never settled on this host — a do-nothing
  control reaches each identically here). Ruled out with fresh probes
  (2026-11-01): F android (`REA_JADX_MCP_JAR` UNSET, no jadx on PATH,
  `~/tools` = downloads/ + ghidra only — S448 stands; F4's honest
  exception stays 10/11); macho/signature providers (`unsupported_host`,
  S453; the artifact-graph group stays `available: true`); K admissions
  (r74 L0 re-read, unanswered — routed around, never treated as
  answered); criterion C repair (§9 sizing, r78–r82 standing
  disposition); criterion R full extension / criterion N attribution
  pair (stay routed — not declared). C1's route is the one the r82
  ruling-out map explicitly left open (`decode_interface_builder`, "a
  separate bounded round") — this is that round.
- **Frontier.** SOURCES rows S462–S465 appended inside the Registry
  (below). Census receipts: round start sanctioned exit 0 (31 W = 21
  W01 + 10 W04, the same disclosed classes as r74–r82; first
  backgrounded attempt killed at a 120 s shell timeout printed a false
  exit 1 with the same clean "ok" output — re-run foreground, exit 0,
  mined); literal form exit 2 (disclosed r74–r82 lineage, the
  consolidation L0 line stands). Round end: `reports/round-83/census-after.log`
  — sanctioned worktree exit 0 (zero E), landing-archive census fires
  the expected E11 ×4 (S462–S465 used-by the lesson that lands with the
  adjudication; verified resolved by touching the lesson in the
  extraction). SOURCES grammar checked mid-flight (S465's regex pipes
  broke NF=13 — fixed before the landing; malformed rows now 0).
- **Assimilation.** `considerthese/` exists (8 digests); checked the
  standing proposal lists (2026-10-22 §Ways, 2026-10-24 #1, 2026-10-26
  #1/#4, 2026-10-28 #1–#3): the live proposals target the blocked
  K-route (quote-substring sampling), a cross-round ledger scope
  (disagreement ledger, adoption ledger, per-role yield) or a reporting
  convention (numerator/denominator split — K untouched this round, and
  this report already states held rows and totals separately). None
  adoptable this round; adopted nothing — Assimilation: none —
  shokuknow unreachable.
- **L2 floor.** No dispatch surface on this host (the r74 L0 stands,
  re-read unanswered); every verdict re-derives from committed bytes.

## Landed changes

All in the appended `LOG.md` round-83 entry; full gate/receipts/mistakes
in `corpus/lessons/round-83.md`; SCORECARD section appended.

- `60693f2ce6b086ea3f0ee84fe27a8f8a13d46f46` — carry-in receipt
  completion (the seven r82 receipts; treecommit explicit paths,
  pushed).
- `28e8c290235f2e6d588a9b81538b61ae50e533b7` — round-83 freeze: claims +
  sha pins + `orphan_sweep4.py` + reds (`ag-red.log`,
  `v3-prelanding-recon.log`) + `preprobe-app-shape.log` + freeze-time
  selftest/mutant receipts + carry-in sweep receipts (pushed).
- `75298d427d97c5668753969fecf54d98630735b7` — landing: the app-r83
  fixture (bundle + generator + truth + oracle), the round-83 producer
  record (inspection/receipt/LEDGER/stderr), S462–S465 inside Registry
  (pushed).
- `b56d81bd83811b3e122f24cb81352472d2afd554` — adjudication: SCORECARD
  round-83 section, LOG entry, `corpus/lessons/round-83.md`, after/
  separability/noharm/census receipts (pushed).

## Before → after measurements

- **C1 (coverage, A1).** Counting command:
  `PYTHONUTF8=1 python -B reports/round-82/ag_probe.py <archive-extract>/corpus`
  (the r82-registered instrument, blob unchanged, sha re-verified
  `22be124b…a08a5` over the landing archive). Before (base archive
  `60693f2`): `A1_RECORDED=2/3 score=6.67` with
  `decode_interface_builder=unrecorded` (`reports/round-83/ag-red.log`).
  After (landing archive `75298d4`): `A1_RECORDED=3/3 score=10.00`
  with `decode_interface_builder=round-83` (`reports/round-83/ag-after.log`,
  which also carries the oracle `ORACLE OK (44/44 checks)` re-run, the
  byte-identical regen, and the F4 hold `F4_COVERAGE=10/11`). Measured
  commits: `60693f2` → `75298d4`. F4 (family presence) and K (8/15)
  unchanged, as frozen.
- **C2 (calibration, v4).** Counting command:
  `PYTHONUTF8=1 python -B reports/round-83/orphan_sweep4.py --lane
  <lane-dir> --fleet <fleet-root> [--format full]` (red side: committed
  `reports/round-82/orphan_sweep3.py`). Before: v3 over the minimal
  pre-landing reconstruction `LANDABLE_ORPHANS=2` exit 1 while seven
  landable cited receipts exist (`reports/round-83/v3-prelanding-recon.log`,
  reconstruction state documented in its header); v4 over the same
  tree: 9 orphan rows covering all seven files (`v4-prelanding-recon.log`).
  After: selftest 13/13 + `SWEEP_SELFTEST=pass` exit 0
  (`sweep4-selftest-after.log`); mutant dies attributed
  (`sweep4-mutant-kill-after.log`); reconstruction resolved 0/exit 0
  (`v4-postlanding-recon.log`); real tree `CITED=677 COMMITTED=665
  LANDABLE_ORPHANS=0 ABSENT=12` exit 0 with `SWEEP_CORPUS fleet-reports=23
  lessons=46` and `SWEEP_BARE_TOKENS matched=291 unmatched_skipped=1366`
  (`sweep4-real-after.log`); final standing sweep over the
  post-adjudication tree: `LANDABLE_ORPHANS=0` exit 0 (basis
  `fleet-reports=23 lessons=47` — the round-83 lesson itself now in the
  corpus and committed). Measured commits: `c153e448`/`60693f2` (red) →
  adjudication `b56d81b`.
- **No-harm.** `reports/round-83/noharm-diff.txt`: protected paths empty
  on `28e8c29..75298d4` (11 files, 757 insertions, 0 deletions —
  additions only); v1/v2/v3 sweep instruments + f_probe4 + ag_probe
  absent from the range; FRESH_ROWS 18/18. Separability:
  `c1-only.log` (A1 3/3 + oracle OK with v4 ABSENT) / `c2-only.log`
  (selftest pass with fixture ABSENT + A1 holds 2/3), both from the
  pre-freeze base `60693f2`.

## Sources & frontier

`SOURCES.md` rows **461 → 465** (counting command:
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
= 465; malformed rows 0; tier histogram A=417 B=21 C=27; status mined=430
queued=16 rejected=19; duplicate-id, enum and used-by checks print
nothing on the worktree). All four opened this round; C1 is sourced by
S462+S463+S464 and C2 by S465:

- S462 — the declared `decode_interface_builder` surface (`--help` /
  `--schema` / `rea capabilities`, own-work tier A; quote: "Decode
  compiled storyboard and nib archives from an app bundle").
- S463 — the installed rea-agents 6.8.0 parser source (own-work tier A;
  quote: "throw new TypeError(`Unsupported NIBArchive format version
  ${formatVersion}`)", NibArchive.js:28) — the fixture layout is
  derived from the lane's own tool source, never from intent.
- S464 — the producer record + fixture (own-work tier A).
- S465 — the carry-in class evidence (the reconstruction receipts,
  own-work tier A).

Census: round start sanctioned exit 0 / literal exit 2 (disclosed
lineage); round end sanctioned exit 0 / literal exit 2 / landing-archive
E11 ×4 resolved by the adjudication (`reports/round-83/census-after.log`,
raw logs in `.ufo/waves/round-83/`).

## Trend verdicts

- **expansion: improved** — the artifact-graph family's third and last
  declared operation now carries a real oracle-checked record (A1 2/3 →
  3/3); F unchanged (android hard-gated), no knowledge admission (K 8/15
  untouched — operator-blocked route re-checked, not attempted).
- **quality: improved** — A1 completed on its registered instrument
  unchanged (blob-verified), and the standing hygiene instrument's
  demonstrated citation-form blind spot became machine-caught inside v4
  with four mutation-checked vectors; the record's identity oracle
  separates 26 byte-derived from 18 pre-registered hypothesis checks.
- **discernment: improved** — six real defects mined this round
  (`corpus/lessons/round-83.md` ## Mistakes): LEB128 varint drafting
  (pre-probe-caught), check-from-intent (self-check wrong, bytes right —
  caught before the freeze), count-from-intent twice (282→313, 7507→
  9012 — caught by measure-before-write), CRLF-mutant (the mutant must
  derive from the committed LF bytes), separability-tree base error
  (self-caught), killed-run census receipt artifact (exit-vs-output
  cross-check). The carry-in's class was reproduced first-hand over
  reconstructed historical bytes, not taken on trust; the fixture
  byte-count and stdout byte-count in this report's sources were each
  measured, not recalled.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns,
  checklists, cited sources — unchanged this round; the routed need
  stands: a non-lane reviewer re-confirming the CURRENT bytes
  (`corpus/lessons/round-69-verifier-spotcheck.md`); this round added no
  SKILL byte and claims no promotion signal.
- [~] At least one end-to-end domain task executed and logged in
  LOG.md — this round's `decode_interface_builder` producer run,
  oracle-checked over archive bytes: `corpus/live/runs/round-83/`
  (receipt.json `exit_code 0`, Evidence `ev_260481425d1a43fbbc0327c2033aafda8d7a51599c520a74b9985c3c550610f8`),
  LOG.md round-83 entry, commit `75298d4`; no independent outside
  verifier this round.
- [~] Instructions executable by an agent without oral context — the
  round's instruments run from their committed bytes with declared
  exits (`orphan_sweep4.py --selftest` 13/13 exit 0; `ag_probe.py` 3/3;
  `oracle_check.py` usage in its docstring; `build_app.py` regen
  byte-identical); no independent outside instruction verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE
  byte-unchanged in `60693f2..b56d81b` (`git diff 60693f2..b56d81b --
  PROVINCE.md` empty); the record is scoped to the observed family,
  operation and authored inputs (LEDGER Q10 scope note); ADJ-06
  unchanged, reported-not-absorbed.

CLOSURE-PREP: re-runnable by the closure judge at the final tip
`b56d81bd83811b3e122f24cb81352472d2afd554` — every expected value below
was measured first-hand at report time, not predicted: (1) `git archive
b56d81bd83811b3e122f24cb81352472d2afd554 | tar -x` then
`sources-census.sh validate <extraction>` → measured exit 0, zero
E-findings, 31 W (the round-83 lesson travels inside the archive, so
the landing-time E11 ×4 are resolved); (2) the standing sweep needs a
GIT REPO — the plain extraction dies `SWEEP_ERROR git ls-tree failed`
(disclosed; do not score it a sweep failure) — either run it over the
lane repo worktree at the tip (receipted: `CITED=677 COMMITTED=665
LANDABLE_ORPHANS=0 ABSENT=12` exit 0 before the adjudication; re-run
after: `LANDABLE_ORPHANS=0` exit 0, basis `fleet-reports=23
lessons=47`) or over the minimal tip reconstruction (git init + `git
fetch <lane-repo> main` + `git update-ref refs/heads/main b56d81bd…`,
no disk files): measured `CITED=432 COMMITTED=427 LANDABLE_ORPHANS=0
ABSENT=5` exit 0, basis `SWEEP_CORPUS fleet-reports=24 lessons=0`
(fleet-reports now 24 = the fleet root carries this report itself;
lessons=0 = the bare reconstruction has no lessons dir on disk; cite
basis lines first, never bare CITED across corpora); (3) `python -B
reports/round-82/ag_probe.py <extraction>/corpus` → measured
`A1_RECORDED=3/3 score=10.00`; (4) `python -B
reports/round-83/orphan_sweep4.py --selftest` → measured
`SWEEP_SELFTEST=pass`, exit 0; (5) the seven carry-in receipts resolve
at `60693f2` (measured: `git show 60693f2:reports/round-82/<name>`
succeeds for each of ag-after.log, sweep3-selftest-after.log,
sweep3-mutant-kill.log, sweep3-real-after.log, c1-only.log, c2-only.log,
noharm-diff.txt).
