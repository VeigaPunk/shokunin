# revenger — round 79 report (hyaku run 18)

Lane repo: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/shokunin-binary-forensics`, branch `main`.
Base `c205ef83ca3fa8e0c0e20488625d232cc3efc4c7`; freeze
`34c2c5a1dc77424ab93044842e4161c87b23c818`; landing
`95e50032a6484f42297a6072d39843cc0222887d`; final measured revision (adjudication)
`abc522d2f7c06cbf641afcf99475299586aae207` — pushed, `git ls-remote origin refs/heads/main`
returns the same hash.

## Work performed

Declared claims (2, distinct axes, causally separable, neither exploratory; frozen
before any after-run in `reports/round-79/claims.md` at `34c2c5a1`):

- **C1 — coverage: a ninth F family (`native-authenticode`) moves through a real
  producer record.** Registered the F2 mapping revision (`reports/round-79/f_probe2.py`,
  frozen; the eight round-1 families byte-equal to the frozen `f_probe`, plus
  `native-authenticode: {inspect_pe_certificates}`; the denominator risk disclosed in
  the instrument header and claims BEFORE the run). Authored an inert native PE32
  certificate-table fixture (`corpus/fixtures/native-auth-r79/`: generator with a
  byte-derived self-check, fixture.dll sha256 `813778b9…cf80`, `truth.json`,
  `oracle_check.py`; regen byte-identical). Ran one bounded
  `rea inspect-pe-certificates` (6.8.0, built-in `rea-pe-certificates`) on the
  committed bytes → `corpus/live/runs/round-79/inspection.json` (exact stdout,
  sha256 `317b0b74…47b79`, exit 0, stderr empty, Evidence `ev_3701e3a1…52fcc`,
  receipt + LEDGER). Oracle `ORACLE OK (27/27 checks)` over the archive bytes.
  Evidence: `reports/round-79/f2-before.log` (base), `f2-after.log` (landing archive),
  `receipt.json`, `LEDGER.md`.
- **C2 — calibration: §Gate-standard self-test modes for both r78-registered gates
  (the routed debt closed by supersession, not re-pinned).** Superseding revisions
  `reports/round-79/gate_probe2.sh` (sha `e2b71649…aead`) and
  `reports/round-79/receipt_probe2.sh` (sha `076cdb67…d9d9`): hermetic `--selftest`
  modes (temp fixtures, no network, no live-tree write, no producer call — verified by
  a PATH-stripped leg), asserting the exit code and stable committed finding-ids
  (S452 clause), plus a declared usage exit 64; frozen sed mutants die with attributed
  last lines. Counting instrument `reports/round-79/selftest_probe.sh`
  (sha `4126af12…2e1e`). Plain-mode value lines byte-equal to v1
  (`plain-equal.log`) — criterion G/R verdict bytes did not move. Evidence:
  `reports/round-79/selftest-before.log` (v1 pair, red), `selftest-after.log` (v2 pair
  over the landing archive, green), `plain-equal.log`. Registry rows for both v2
  instruments landed in SKILL.md `## Gate registry`; the v1 rows stand for the v1
  bytes.

Fresh-start §7 (binding via the prompt's r71/r72/r73 rejected-closure list): all three
re-read and spot-checked — every one is a wave-blocked K-admission claim (C05 sixth
pass, C15 tool landscape, C10 entry), a class a do-nothing control reaches identically
on this host (no wave Q-review surface; the r74 L0 stands unanswered, re-checked in
the fleet `.ufo/l0-questions.md`). Ruled out this round, with fresh probes: **F
android** (`REA_JADX_MCP_JAR` UNSET, no jadx on PATH, no `~/tools/jadx*`; S448
receipt stands); **macho/signature F families** (`rea capabilities`:
`unsupported_host` — "Native macOS utilities require macOS", S453); **K admissions**
(L0 unanswered); **criterion C repair** (§9 sizing, unchanged from r78's ruling,
stays routed). Claims declared are ones a do-nothing control cannot reach: a new
producer record + mapping revision (C1) and two superseding gate instruments with
attributed kills (C2).

Carry-in dispositions (r78 non-author closure, addressed first, all status-neutral):

1. Census literal-form host defect: both forms re-run at round start (literal exit 2,
   sanctioned exit 0 — 450 rows) and round end (`census-after.log`); the sanctioned
   form stays documented (SKILL.md §4a, current); the requested **L0 consolidation
   line naming the whole r74–r79 lineage** landed in the fleet `.ufo/l0-questions.md`.
2. Gate self-test routed debt: **closed by supersession** (C2's substance — the "add"
   branch; the "pin" branch would have re-recorded the debt).
3. Criterion-instrument class question and criterion C repair: both stay routed,
   re-pinned in `corpus/lessons/round-79.md` §Routed forward (F2 was frozen as a
   claims revision, deliberately NOT a registry row, so the question stays open).

L2 floor: no dispatch surface on this host (no `.ufo/state/`, no seat spawn; r74 L0
stands) — no wave was dispatched or needed: both claims verify from committed bytes
and live local producer runs whose receipts the closure judge can re-run.

## Landed changes

(LOG entry "Round 79 — native-authenticode family through a real producer run; gate
self-test debt closed by supersession".)

- Freeze `34c2c5a1`: `reports/round-79/{claims.md, f_probe2.py, gate_probe2.sh,
  receipt_probe2.sh, selftest_probe.sh, preprobe-cert-shape.log, f2-before.log,
  selftest-before.log}` (8 files, +706/−0).
- Landing `95e50032`: `corpus/fixtures/native-auth-r79/{generator.py, fixture.dll,
  truth.json, oracle_check.py}`, `corpus/live/runs/round-79/{inspection.json,
  receipt.json, LEDGER.md, stderr.txt}`, SKILL.md (two v2 registry rows),
  `corpus/SOURCES.md` (S451–S453) (10 files, +397/−0).
- Adjudication `abc522d2`: `reports/round-79/{f2-after.log, selftest-after.log,
  plain-equal.log, c1-only.log, c2-only.log, noharm-diff.txt, census-after.log}`,
  `corpus/lessons/round-79.md`, SCORECARD.md (round-79 section), LOG.md (10 files,
  +312/−0).
- Fleet-root (not the lane repo): the L0 consolidation line appended to
  `.ufo/l0-questions.md` (append-only side channel; not a lane commit).
- No-harm: protected paths (knowledge, README, verifiers, SHONEN, PROVINCE, LOG,
  SCORECARD, P2/P3, f_probe, receipt/gate v1, r71 counter) empty on
  `c205ef83..95e50032`; v1 instrument shas at the landing match their pins
  (`reports/round-79/noharm-diff.txt`).

## Before → after measurements

- **C1** (measured commits `c205ef83` → `95e50032`):
  - before: `PYTHONUTF8=1 python -B reports/round-76/f_probe.py <base-archive>/corpus`
    → `F_COVERAGE=7/8 score=8.75`;
    `PYTHONUTF8=1 python -B reports/round-79/f_probe2.py <base-archive>/corpus` →
    `F2_COVERAGE=7/9 score=7.78` (native-authenticode absent) — `f2-before.log`.
  - after (landing archive): v1 `F_COVERAGE=7/8 score=8.75` (frozen eight unchanged);
    `F2_COVERAGE=8/9 score=8.89`, `F2_FAMILIES=[… 'native-authenticode']` +
    `ORACLE OK (27/27 checks)` — `f2-after.log`.
- **C2** (red at `c205ef83` worktree bytes blob-identical to base; green over the
  landing archive): `bash reports/round-79/selftest_probe.sh <gate> <receipt>` →
  before (v1 pair): `SELFTEST_MODE_PRESENT=0/2`,
  `SELFTEST_MUTANT_KILLED_ATTRIBUTED=0/2`, `USAGE_EXIT64=0/2`, exit 1
  (`selftest-before.log`); after (v2 pair): `2/2`, `2/2`, `2/2`, exit 0, with the
  attributed kill lines in the same receipt (`selftest-after.log`); plain-mode drift:
  none twice (`plain-equal.log`).
- Holds: FRESH_ROWS 18/18 (seed 12 + readiness 6, exit 0); K 8/15 not re-run (no
  README/knowledge byte changed — no-harm diff); P3 not re-run (probe and PROVINCE
  bytes unchanged — no-harm diff).

## Sources & frontier

SOURCES: 450 → 453 rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md`; +S451 the producer record [own-work, tier A], +S452 the §Gate
standard §Self-test/§Verdict clauses at the S449 checkout [narrower-scope re-open,
disclosed], +S453 the `rea capabilities`/`--llms` availability surface [own-work]).
C1 and C2 are both sourced claims. Census: round start — literal form exit 2 (the
disclosed r74–r79 old-host layout lineage; L0 consolidation line landed), sanctioned
explicit-lane-dir form exit 0 (31 W); round end — sanctioned form **exit 0** (31 W:
21 W01 + 10 W04, the same disclosed classes; the S452 re-open cites a path+hash, no
new W04), literal form exit 2 (`reports/round-79/census-after.log`). The first
round-end census run fired E12 ×3 (rows appended outside the Registry section) —
fixed in-round, mined in `corpus/lessons/round-79.md` Mistakes row 1. Mistake mining:
three classes mined (E12 row position; non-8-aligned WIN_CERTIFICATE dwLength,
self-caught at the scratch self-check; truth drafted from the observed record instead
of the authored bytes, self-caught on Q06 — the generator now derives every
oracle-checked fact).

## Trend verdicts

- **expansion — improved.** A ninth in-province F family with a real, oracle-checked
  current-producer record (7/8→8/9 on the registered instrument); the frozen eight
  and their 7/8 hold are unchanged; no knowledge admission (K 8/15 untouched,
  operator-blocked route not attempted).
- **quality — improved.** A new covered producer surface with a byte-derived identity
  oracle (27/27 over archive bytes), and both criterion gates now self-verifying per
  the §Gate standard with attributed kills and a declared usage map — with the v1
  instruments frozen and byte-identical (no verdict drift, `plain-equal.log`); no
  admitted entry failed any re-check (FRESH 18/18).
- **discernment — improved.** Three real defects mined, two self-caught before any
  committed byte (the dwLength assert; the observation-as-premise truth draft) and
  one by the round-end census receipt (E12); the mapping revision's denominator risk
  was disclosed in the instrument header and claims before the run; boundaries stated
  as boundaries (v1 holds 7/8 unchanged; android/macho/signature ruled out with
  receipts, not silence).

## Assimilation

`considerthese/` exists (8 files, bot daily reflections through 2026-10-28 covering
rounds already consumed — the two earlier implementable items landed as Q14 (r68) and
a zero line (r69)); no still-unimplemented implementable proposal remains in them.
Assimilation: none — shokuknow unreachable.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited
  sources — two v2 gate-registry rows appended this round (evidence: SKILL.md
  `## Gate registry`, `reports/round-79/selftest-after.log`); the r69 routed need for
  a non-lane reviewer re-confirmation of the CURRENT bytes stands; no author `[x]`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — this
  round's own producer run is end-to-end domain work (authored fixture → real
  producer run → oracle 27/27 → counter move; `corpus/live/runs/round-79/LEDGER.md`);
  the box's r64-record basis unchanged; no outside verifier this round.
- [~] Instructions executable by an agent without oral context — the round's
  instruments and receipts re-derive every verdict from committed bytes (archive-run
  receipts in `reports/round-79/`); no independent outside instruction verifier this
  round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md byte-untouched
  (no-harm diff); the certificate-table surface is in-province (native binaries;
  PROVINCE.md "Owns"); ADJ-06 unchanged; no outside verifier this round.
