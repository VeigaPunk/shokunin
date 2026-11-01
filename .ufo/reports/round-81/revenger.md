# revenger — round 81 report (hyaku run 20)

Lane repo: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/shokunin-binary-forensics`, branch `main`.
Base `081f032fda9502ebfbceb295d7e097dd8803bce1`; freeze
`8261a24cb806d60a47a640f948de339912dcc96b`; landing
`88b7e7cee2f07c77b7d9597e8d9e3159aed37f19`; adjudication
`b330049b2aab33deff147737d22e515c229b1b75`; correction
`b2fc6bbb195c6029ac2ce6a51e6e376ec0001c4a` (final measured revision) —
pushed, `git ls-remote origin refs/heads/main` returns the same hash.

## Work performed

Declared claims (2, distinct axes, causally separable, neither exploratory;
frozen before any after-run in `reports/round-81/claims.md` at `8261a24c`):

- **C1 — coverage: an eleventh F family (`artifact-graph`) moves through a
  real keyed-archive producer record.** Registered the F4 mapping revision
  (`reports/round-81/f_probe4.py`, frozen sha `4d871971…6a3c7`; the ten F3
  families byte-equal to the frozen `f_probe3.py` `9441640d…4b418`, plus
  `artifact-graph: {decode_interface_builder, inspect_keyed_archive,
  trace_dylib_resolution}`; the denominator risk disclosed in the instrument
  header and claims BEFORE the run). Authored an inert Foundation
  keyed-archive fixture (`corpus/fixtures/keyed-r81/`: generator whose
  self-check derives EVERY oracle-checked fact from the built bytes — roots,
  6 objects, 4 references, format, totals; 14/14 SELFCHECK; regen
  byte-identical; fixture.db-equivalent `fixture.plist` 210 bytes sha256
  `f0e02e64…37785c`; `truth.json`; `oracle_check.py`). Ran one bounded
  `rea inspect-keyed-archive corpus/fixtures/keyed-r81/fixture.plist
  --format json` (6.8.0, built-in `rea-artifact-graph` provider) on the
  committed bytes → `corpus/live/runs/round-81/inspection.json` (exact
  stdout, 3174 bytes, sha256 `83fe4046…348fcf`, exit 0, stderr 0 bytes,
  Evidence `ev_6eb77fb0…02af4b73`, receipt + LEDGER). Oracle
  `ORACLE OK (27/27 checks)` over the archive bytes. Evidence:
  `reports/round-81/f4-before.log` (base archive: 9/11 = 8.18 red),
  `f4-after.log` (landing archive: 10/11 = 9.09 green + oracle + regen
  re-run), `preprobe-keyed-shape.log` (committed at the freeze, with the
  Q06 stale-constants catch and the oracle sort-defect catch disclosed).
- **C2 — calibration: orphan_sweep v2 — the r80 carry-in classes close
  inside the standing instrument.** `reports/round-81/orphan_sweep2.py`
  (sha `30aa3527…93eb6`; v1 `reports/round-80/orphan_sweep.py` blob
  unchanged `f21f5e3d…1890b`; declared exits 0/1/64 unchanged): (1)
  repeated trailing line-ref stripping (`file.md:57,:148,` → `file.md` — the
  r80 false absent); (2) dir-style cite normalization with a masked-absent
  negative vector (`corpus/lessons/round-64` → committed via
  `round-64.md`, with the proof the normalization cannot mask a real
  absent); (3) the `SWEEP_CORPUS fleet-reports=<n> lessons=<n>` count-basis
  header (the r80 CITED=344-vs-357 routed rule); (4) `--format full`
  (default) / `--format summary` (states its filter) — the r80
  2-of-357-lines truncated receipt class closes. Hermetic `--selftest`
  extended to 7 legs with the attributed mutant kill preserved.

Round-80 carry-in (non-author closure), addressed first:

1. **Sweep-count drift** (`CITED=344 COMMITTED=330` quoted vs the committed
   receipt's `CITED=357 COMMITTED=343`) — root-caused FIRST-HAND, not taken
   on trust (`preprobe-keyed-shape.log` §r80-corpus reconstruction): the v1
   tokenizer over lessons@`ef7d3ee3` + fleet reports minus round-80 yields
   **exactly CITED=344** → 330 committed + 6 absent-fleet + 8 absent
   (LANDABLE_ORPHANS=0) — the quoted figure is the LANDING-ERA citation
   corpus; over lessons@`b1e0c60e` + current fleet yields **exactly 357** —
   the receipt's corpus; the current tree prints 358 (the r80 spot-check
   lesson). Verdict values identical in all corpora. Correction filed as an
   APPENDED erratum section in SCORECARD.md + a correction entry in LOG.md
   naming per-revision citation corpora (never an in-place rewrite); the
   rule lands as v2 change 3.
2. **Truncated sweep receipt** — the r81 real-tree receipt
   (`sweep2-real-after.log`) carries FULL output (all 357 SWEEP lines +
   basis line); `--format summary` states its filter. The r80 receipt stays
   as committed evidence.
3. **SHONEN `[~]` reviewer debt** — operator-side (the r80 closure noted it
   for the operator); routed around: `[~]` lines with resolvable pointers
   again below, no `[x]` claimed, no SHONEN claim declared.

Fresh-start §7 (binding via the prompt's r71/r72/r73 rejected-closure
list): all three re-read at fleet `.ufo/reports/round-7{1,2,3}/revenger.md`
and spot-checked — every one is a K-admission claim whose 16-vote wave
Q-review surface never existed or never settled (r71 falsified by Q09/Q16;
r72 falsified by its own frozen predicate with the wave unsettled; r73
unresolved, wave released un-settled) — a class a do-nothing control reaches
identically on this host (no `.ufo/state/` dispatcher; the r74 L0 at fleet
`.ufo/l0-questions.md:233` re-read this round: unanswered). Ruled out this
round, with fresh probes (2026-11-01): **F android** (`REA_JADX_MCP_JAR`
UNSET, no jadx on PATH, `~/tools` = downloads/ + ghidra only; S448 receipt
stands — F4's honest exception is 10/11, not 11/11); **macho/signature
families** (`rea capabilities`: `unsupported_host`, S453; Hopper
`unsupported_host` on win32; IDA/kuna `not_configured`); **K admissions**
(L0 unanswered); **criterion C repair** (§9 sizing, unchanged r78–r80);
**criterion R extension / criterion N attribution pair** (stay routed, not
declared this round). The declared claims are ones a do-nothing control
cannot reach: a new producer record + mapping revision (C1) and an
instrument supersession with new attributed vectors (C2). Note on the r80
planned line ("a further F move needs a new host surface"): the surface was
already on the host — the rea CLI's `rea-artifact-graph` provider reports
three decode operations `available: true` that no earlier capability scan
had mined as family ground (S457); C1 routes onto that record.

L2 floor: no dispatch surface on this host (r74 L0 stands) — no wave was
dispatched or needed: both claims verify from committed bytes and live local
producer runs whose receipts the closure judge can re-run.

## Landed changes

(LOG entry "Round 81 — artifact-graph family through a real keyed-archive
producer run; the orphan sweep learns the r80 carry-in classes", including
the appended correction naming per-revision citation corpora.)

- Freeze `8261a24c`: `reports/round-81/{claims.md, f_probe4.py,
  orphan_sweep2.py, f4-before.log, sweep-v1-red.log,
  preprobe-keyed-shape.log}` (6 files, 988 insertions, 0 deletions).
- Landing `88b7e7ce`: `corpus/fixtures/keyed-r81/{generator.py,
  fixture.plist, truth.json, oracle_check.py}`,
  `corpus/live/runs/round-81/{inspection.json, receipt.json, LEDGER.md,
  stderr.txt}`, `corpus/SOURCES.md` (S457–S458 inside the Registry
  section) (9 files, 412 insertions).
- Adjudication `b330049b`: `reports/round-81/{f4-after.log,
  sweep2-selftest-after.log, sweep2-real-after.log, c1-only.log,
  c2-only.log, noharm-diff.txt, census-after.log}`,
  `corpus/lessons/round-81.md`, SCORECARD.md (round-81 section + the
  appended r80 erratum + the capabilities supersession note), LOG.md
  (10 paths).
- Correction `b2fc6bb` (disclosed, post-adjudication): the mandated
  post-commit diff check caught the LOG.md append riding CRLF worktree
  bytes — the adjudication commit had rewritten every line's ending (1167
  insertions / 1158 deletions for a 9-line semantic append). The correction
  restores the LF landing blob and re-appends the entry: diff vs the
  landing `88b7e7ce` = 0 deleted / 9 added (byte-verified); SCORECARD
  mistakes list + `corpus/lessons/round-81.md` Mistakes row 6 (the CRLF
  class) (3 paths).
- No-harm: protected paths (knowledge, README, verifiers, SHONEN, PROVINCE,
  pre-r81 fixtures, frozen instruments v1/F2/F3/orphan_sweep v1/P2/P3/
  gate+receipt probes/r71 counter) empty on `081f032..88b7e7ce`; frozen
  instrument content sha256s match their pins
  (`reports/round-81/noharm-diff.txt`).
- Fleet-root (not the lane repo): this report file.

## Before → after measurements

- **C1** (measured commits `081f032` → `88b7e7ce`; re-verified over the
  landing archive at adjudication):
  - before: `PYTHONUTF8=1 python -B reports/round-76/f_probe.py
    <base-archive>/corpus` → `F_COVERAGE=7/8 score=8.75`;
    `…/reports/round-79/f_probe2.py` → `F2_COVERAGE=8/9 score=8.89`;
    `…/reports/round-80/f_probe3.py` → `F3_COVERAGE=9/10 score=9.00`;
    `…/reports/round-81/f_probe4.py` → `F4_COVERAGE=9/11 score=8.18`
    (artifact-graph absent) — `f4-before.log`.
  - after (landing archive): v1 7/8, F2 8/9, F3 9/10 unchanged (frozen
    holds); `F4_COVERAGE=10/11 score=9.09`, `artifact-graph` in
    `F4_FAMILIES` + `ORACLE OK (27/27 checks)` over the archive bytes —
    `f4-after.log`.
- **C2** (measured commits `081f032` (red) → adjudication; receipts at
  `b330049b`):
  - before: `PYTHONUTF8=1 python -B reports/round-80/orphan_sweep.py --lane
    <lane> --fleet <fleet>` (v1, committed bytes) → `CITED=358
    COMMITTED=344 LANDABLE_ORPHANS=0 ABSENT=14`, NO count-basis line, and
    `grep -cE '^SWEEP absent (corpus/knowledge/round-68-apk-axml-byte-evidence\.md:57|corpus/lessons/round-64) '`
    = **2** (`sweep-v1-red.log`, full output); plus the committed r80
    truncated receipt (`reports/round-80/sweep-real-after.log`, 2 of the
    SWEEP lines, no stated filter) as the second red.
  - after: `PYTHONUTF8=1 python -B reports/round-81/orphan_sweep2.py
    --selftest` → 7 legs ok, `SWEEP_SELFTEST=pass`, exit 0, with
    `SWEEP_SELFTEST_MUTANT_FLAGGED=ok` (`sweep2-selftest-after.log`; run
    from the extracted landing archive outside any repo);
    `… orphan_sweep2.py --lane <lane> --fleet <fleet> --format full` →
    FULL output (357 SWEEP lines), `SWEEP_CORPUS fleet-reports=21
    lessons=42`, `CITED=357 COMMITTED=345 LANDABLE_ORPHANS=0 ABSENT=12`,
    parser-artifact grep = **0**, exit 0 (`sweep2-real-after.log`);
    unrecognized forms exit 64.
- Holds: FRESH_ROWS 18/18 (seed 12 + readiness 6, exit 0); K 8/15 not
  re-run (no README/knowledge byte changed — no-harm diff); P3 not re-run
  (probe and PROVINCE bytes unchanged — no-harm diff).

## Sources & frontier

SOURCES: 456 → 458 rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md`; +S457 the rea 6.8.0 artifact-graph capability surface
[own-work, tier A, opened this round — located quote "Inspect a Foundation
keyed archive as an object-reference graph", `rea --llms`; 9 words], +S458
the producer record [own-work, tier A]; both appended inside the Registry
section directly after S456; C1 is the sourced claim (S457); C2 rests on
the r80 closure's routed rule, S456 lineage). Census: round start —
sanctioned explicit-lane-dir form exit 0, 31 W (21 W01 + 10 W04, the same
disclosed classes; literal form exit 2, disclosed r74–r81 lineage); round
end — sanctioned worktree form exit 0, 31 W; landing-archive-bytes census
over `88b7e7ce` fires E11 ×2 (S457/S458 used-by preceding the lesson — the
expected intermediate state, resolved by the adjudication commit) with 31 W
and zero other E-findings; the FINAL-TIP archive census (over `b2fc6bb`)
exit 0 with zero E-findings, 31 W — re-runnable by the closure judge per
the receipt's note (`reports/round-81/census-after.log`; the receipt
discloses a self-caught first-draft defect: it grepped the wrong row prefix
over the extraction and printed 0 W-lines — rewritten from the raw output).
Mistake mining: six rows in `corpus/lessons/round-81.md` `## Mistakes` —
the generator's stale self-check constants (Q06 caught), the oracle's
None-vs-int reference sort (caught by the first real run), the r80
corpus-drift class (carry-in, root-caused first-hand), a recon
corpus-isolation error (self-caught by a tokenizer-vs-sweep cross-check), a
census receipt prefix defect (self-caught before commit), and the post-commit
LOG.md CRLF whole-file rewrite (caught by the mandated diff check; corrected
by `b2fc6bb`, append-only byte-restored).

## Trend verdicts

- **expansion — improved.** An eleventh in-province F family with a real,
  oracle-checked current-producer record (F3 9/10 → F4 10/11 on the
  registered instrument); the frozen v1 (7/8), F2 (8/9) and F3 (9/10) holds
  are unchanged; the honest exception stands (android hard-gated — 10/11,
  not 11/11); no knowledge admission (K 8/15 untouched, operator-blocked
  route not attempted).
- **quality — improved.** A new covered producer surface with a byte-derived
  identity oracle (every oracle-checked fact derived from the built bytes by
  the generator's 14-check self-check, never copied from the record; 27/27
  over archive bytes), and the standing hygiene instrument now closes its
  own named false-disposition and receipt classes with attributed kills and
  a machine-checkable count basis; no admitted entry failed any re-check
  (FRESH 18/18); the r80 quoted-vs-receipted number drift is corrected by an
  appended erratum with the per-revision corpora first-hand reproduced.
- **discernment — improved.** Six real defects mined with captures (lesson
  Mistakes rows 1–6): two caught by the round's own disciplines before any
  committed byte (Q06 stale constants; the oracle sort), one routed carry-in
  root-caused first-hand to exact numbers (344/357), one self-caught by a
  cross-check before it could poison the erratum (recon corpus isolation),
  one self-caught at receipt review (census prefix), and one caught by the
  mandated post-commit diff check after landing (the CRLF rewrite — the
  r78/r80 class check extended to line endings) and repaired in-round by
  `b2fc6bb` with the append-only property byte-restored; the mapping
  revision's denominator risk disclosed at freeze pre-run; v2's
  normalization carries its masked-absent negative rather than trusting the
  mapping.

## Assimilation

`considerthese/` exists (8 files, bot daily reflections through 2026-10-28,
last changed at `3a41d1a`; re-checked this round — no still-unimplemented
implementable proposal remains; the two earlier implementable items landed
as Q14 (r68) and a zero line (r69)).
Assimilation: none — shokuknow unreachable.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited
  sources — SKILL.md byte-untouched this round (no-harm diff; the census §4a
  sanctioned form stays current and was re-run both ends); the routed need for a
  non-lane reviewer re-confirmation of the CURRENT bytes stands (r69 V7, r79
  spotcheck §8, r80 closure §7 — operator-side, routed around per the r80
  carry-in); no author `[x]`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — this
  round's own producer run is end-to-end domain work (authored fixture with a
  byte-deriving self-check → real producer run → oracle 27/27 over archive
  bytes → counter move; `corpus/live/runs/round-81/LEDGER.md`); the box's
  r64-record basis unchanged; no outside verifier this round.
- [~] Instructions executable by an agent without oral context — the round's
  instruments and receipts re-derive every verdict from committed bytes
  (freeze/landing/adjudication/correction shas above; archive-run receipts in
  `reports/round-81/`; the claims.md kill rules are execute-as-frozen); no
  independent outside instruction verifier this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md
  byte-untouched (no-harm diff); the keyed-archive surface is in-province
  (shipped artifacts; PROVINCE.md "Owns" archives; Q10 scope note in the
  LEDGER — classes never instantiated, one authored 210-byte snapshot);
  ADJ-06 unchanged; no outside verifier this round.
