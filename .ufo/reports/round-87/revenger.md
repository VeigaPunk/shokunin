# revenger — round 87 report

Lane: `fleet/shokunin-binary-forensics`, branch `main`. Base `1306ec9`
(r86 tip + non-author spot-check). Lane head at report time:
`1481f4907b370a32bc6543dfe831a3da30741d97` (pushed; remote parity
verified via `git ls-remote origin refs/heads/main`). Round shape:
fresh-start (FRESH-START per the round contract §7 — the r71/r72/r73
rejected closures re-read and spot-checked; §gate below). One declared
claim, not exploratory, with counting commands. Non-author verification:
pending the closure judge (every verdict below is self-measured from
committed bytes; receipts cite their own stdout).

## Work performed

Claim: **C1 — calibration**: criterion N's mutation-killed attribution
pair lands on the negctl harness itself (instrument v2 supersedes the
never-registered r75 v1 harness), and the criterion-N instrument gets
its Gate-registry row. Target axis: calibration. This is the routed
r75-planned-(b) item, carried verbatim through every Routed-forward list
r75–r86 ("criterion N attribution pair").

- Carry-in first (r86 non-author closure — clean, three status-neutral
  items, none a defect): (1) census contract-literal form exit 2 — dual
  round-start receipts landed again
  (`.ufo/waves/round-87/census-round-start-{sanctioned,literal}.log`;
  sanctioned exit 0, 21 W01 + 10 W04, zero E; literal exit 2, disclosed
  r74–r87 lineage, L0 r79 stands, routed around, nothing assumed
  answered); (2) SHONEN box 1 non-author re-confirmation stays
  operator-side — SKILL.md changed this round, so the standing need
  names the r87 bytes; no box marked by the author; (3) the coverage
  unreachability routing re-probed fresh 2026-11-02 (probe receipt:
  `reports/round-87/freshstart-probes.log`).
- Fresh-start §7 gate — what was ruled out and why (all three rejected
  closures re-read at the fleet reports, verdict lines match the
  dispatch digests): r71 (C1 coverage/K C05 sixth pass, falsified
  Q09/Q16), r72 (C1 coverage/C15, `C15_TOOL_ROWS=18/18` but
  `C15_HELD_BACKED=0/1` — row labels are not admission), r73 (C1
  coverage/C10, wave released un-settled, honest stop). Common thread:
  all three are K-admission claims whose deciding wave Q-review surface
  has never settled on this host (L0 r74 re-read this round, probe 6b,
  unanswered) — a do-nothing control reaches each identically, so none
  is declarable. Ruled out with fresh probes: coverage/K (operator
  blocked); coverage/F android (`REA_JADX_MCP_JAR` UNSET, no jadx on
  PATH — S448 stands; F4's honest exception stays 10/11); coverage/M,
  A1, A1v2 (saturated 3/3, 3/3, 5/5 — frozen holds re-run green over
  the landing archive); coverage/asset-catalog (macOS-gated; sentinel
  unchanged: 7 `availability_code: unsupported_host` groups 2026-11-02,
  same as r85/r86); the r86 planned depth row (its trigger — "if the
  drift class recurs" — is unmet: v7 `mismatch=0` stands, no
  recurrence); the considerthese 2026-10-28 Q16 self-map checker
  proposal (considered, NOT adopted — its consumers are the
  operator-blocked C05 surface; routed). Lowest-axis routing: coverage
  is the lowest non-retired axis (K 5.3 < 7.0, so the stagnation nudge
  does NOT apply) — the obligation routes on documented unreachability
  with fresh receipts, per the r86 closure's standing condition.
- C1 instrument: `reports/round-87/probe_negctl2.sh` (sha256
  `d70271464a437a6c0de598237a603cc50498458a14c94e37f8df2edf7e03070d`,
  frozen at the freeze commit). Plain mode is v1-identical (same frozen
  P1/P2 fixtures, same legs, byte-identical value lines —
  `plain-equal.log`, diff empty, both exit 0); `--selftest` is hermetic
  (synthetic verdict vectors only — no fixture build, no probe run, no
  producer call; expected finding-ids `NEGCTL_SELFTEST_FALSEPASS_LOGIC=ok`,
  `NEGCTL_SELFTEST_ATTRIBUTION_GUARD=ok`, `NEGCTL_SELFTEST_STALE_LOGIC=ok`,
  `NEGCTL_SELFTEST_UNRECORDED_LOGIC=ok`, last line
  `NEGCTL_V2_SELFTEST=pass`); usage exit 64 declared per PROTOCOL
  §Gate standard. The pair: mutant A (`stale_flag_ok` blinded to
  `return 0`, exactly line 35, mutated sha `f70c0e9a…9a99`) dies exit 1
  attributed `selftest: stale-record verdict accepted a false-pass`;
  mutant B (attribution pattern relaxed to `.*`, exactly line 35,
  mutated sha `ec29099c…39cb`) dies exit 1 attributed `selftest:
  attribution guard accepted an unattributed kill`. Deterministic
  ST1→ST2 ordering gives each mutant its own message. Evidence:
  `reports/round-87/{negctl-red.log,negctl-v1-baseline.log,green-prelanding.log,mutants-prelanding.log,plain-equal-prelanding.log}`
  (freeze) and `{negctl-green.log,negctl-mutant-kill-after.log,plain-equal.log,c1-only.log}`
  (from committed blobs).
- C1 counting instrument: `reports/round-87/selftest_probe.sh` (sha256
  `ed0b328279133579a100d99f331ba752267782cd9b6764899c2082bfad4d87ed`;
  the r79 shape: producer dir stripped from PATH, sed-must-change-bytes
  guard, mktemp copies removed on exit). The SAME command measures both
  ends.
- C1 registration: SKILL.md §Gate registry gains the `probe_negctl2`
  row (7 → 8 rows) — the criterion-N instrument was never registered
  (v1, round 75), the same gap the round-78 registration closed for
  R/G. Verdict map declares 0/1/2/64; the self-test clause is satisfied
  with the two-evidences pair over committed input snapshots naming the
  measured revisions. The criterion-N score stays 10.0 held (scored
  r75); the moved quantity is the instrument's self-conformance plus
  registry visibility — the r79 registration precedent shape.
- SOURCES curation: S473 (own-work, tier A, opened 2026-11-02) — the
  criterion-N instrument-blindness evidence (frozen v1 bytes +
  baseline green + counting red over the SAME bytes + the routed-debt
  lineage). Located quote grounding `teaches` (13 words, verbatim,
  re-read 2026-11-02): "attribution pair on the negctl harness itself,
  or retire/split P2 at saturation" — SCORECARD.md round-75 planned
  paragraph. NF=13 checked at landing; 0 malformed, 0 duplicates.
- Mistake mining: five rows in `corpus/lessons/round-87.md` `## Mistakes`
  (loose-pattern counting 31 vs 7; mutant-recipe over-escaping;
  command-substitution newline stripping; grep-piped exit attribution +
  the missed A1 leg; `paste -sd:")"` transcription drift). Four of the
  five were caught before any committed byte could mislead; two of the
  five are disclosed recurrences of mined classes on new signatures.
- L2 floor: not executable on this host (no dispatch surface; r74 L0
  re-read, unanswered) — disclosed every round; every verdict here
  re-derives from committed bytes.

## Landed changes

All tied to the LOG.md round-87 block (append-only):

| change | commit |
|---|---|
| Freeze: claims.md + probe_negctl2.sh + selftest_probe.sh + negctl-red.log + negctl-v1-baseline.log + freshstart-probes.log + plain-equal-prelanding.log + green-prelanding.log + mutants-prelanding.log + dual round-start census receipts (11 files, 554 insertions, 0 deletions) | `ea143a3a0f93db8e054395bdaa29645f17db6bd2` |
| Landing: SKILL.md `probe_negctl2` registry row (additions only) + corpus/SOURCES.md S473 append (2 files, 12 insertions, 0 deletions) | `1fa086d3ad6d91dd30bd5bc0adf2e225585c5f54` |
| Adjudication: corpus/lessons/round-87.md (Gate + Mistakes + Routed forward), LOG.md round-87 block, SCORECARD.md round-87 section, official receipts (negctl-green.log, negctl-mutant-kill-after.log, plain-equal.log, c1-only.log, holds-over-landing-archive.log, noharm-diff.txt), dual round-end census receipts (11 files, 400 insertions, 0 deletions) | `1481f4907b370a32bc6543dfe831a3da30741d97` |

No protected byte changed anywhere in the round (`noharm-diff.txt`:
protected paths empty over the full range; corpus/live, corpus/fixtures,
corpus/knowledge, corpus/README.md, PROVINCE.md, QUALITY.md, SHONEN.md,
and all standing verifiers byte-unchanged; PROVINCE.md byte-unchanged —
adjacency unaffected).

## Before → after measurements

C1 (calibration — criterion-N instrument self-conformance + registry
visibility), measured commits: red state = the frozen v1 bytes at base
`1306ec9` (v1 unchanged since r75); green = landing tip `1fa086d3`;
standing re-run at the final tip `1481f490` (identical values):

```
bash reports/round-87/selftest_probe.sh reports/round-75/probe_negctl.sh; echo $?
# red   (negctl-red.log):        0/1 · 0/2 · 0/1   exit 1
bash reports/round-87/selftest_probe.sh reports/round-87/probe_negctl2.sh; echo $?
# green (negctl-green.log):      1/1 · 2/2 · 1/1   exit 0
#        (labels: NEG_SELFTEST_MODE_PRESENT, NEG_SELFTEST_MUTANTS_KILLED_ATTRIBUTED, NEG_USAGE_EXIT64)

sed -n '/^## Gate registry/,/^## 7\./p' SKILL.md | grep -cE '^\| name \|'
# 7 (base 1306ec9) -> 8 (landing 1fa086d3)
```

Mutation receipts (from the committed blob over `1fa086d3`, sha-verified
against the claims pins): mutant A dies `selftest: stale-record verdict
accepted a false-pass`, mutant B dies `selftest: attribution guard
accepted an unattributed kill` — both exit 1, each diff exactly 35c35
(`negctl-mutant-kill-after.log`). Plain-mode identity: v1 vs v2 diff
empty (`plain-equal.log`). Separability: base archive + the two
instruments only (no SKILL row, no S473) runs green identically with
base-state markers 7 rows / no S473 (`c1-only.log`). Holds over the
landing archive `1fa086d3`, all probe exits 0
(`holds-over-landing-archive.log`): `M_RECORDED=3/3 score=10.00`,
`F4_COVERAGE=10/11 score=9.09`, `A1V2_RECORDED=5/5 score=10.00`,
`A1_RECORDED=3/3 score=10.00`, freshness 12+6=18, `K_HELD_BACKED=8/15`.

## Sources & frontier

SOURCES.md rows 472 → 473 (counting command:
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
→ 473; malformed 0: `awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md`
→ 0; duplicates: none). One row appended this round (S473, opened
2026-11-02, own-work tier A, status mined, used-by
`corpus/lessons/round-87.md` + `reports/round-87/claims.md`); C1 is the
sourced claim (Q01). Census: round start sanctioned exit 0 (21 W01 +
10 W04, zero E) / literal exit 2 (disclosed r74–r87 lineage, operator
side, L0 r79 stands); round end sanctioned exit 0 (31 W = 21 W01 +
10 W04, zero E — `.ufo/waves/round-87/census-round-end-sanctioned.log`)
/ literal exit 2 (`.ufo/waves/round-87/census-round-end-literal.log`).
The lane contract's round-end requirement (exit 0) is met by the
sanctioned explicit-lane-dir form; the literal form's exit 2 is the
standing operator-side host defect, routed around with receipts, nothing
assumed answered.

## Trend verdicts

- **expansion: unchanged** — no knowledge admission (K untouched,
  operator-blocked), no new capability row (v2 supersedes the existing
  criterion-N instrument; first-working-round unchanged wherever
  registered), denominators held (M 3/3, A1 3/3, A1v2 5/5, F4 10/11,
  K 8/15). Evidence: holds + no-harm receipts.
- **quality: improved** — the routed twelve-round criterion-N debt
  became machine-caught: a verdict harness that could not show it can
  fail now carries a hermetic selftest, a declared usage contract, two
  mutation-checked switches with per-mutant attribution, and its first
  registry row; no axis harmed (holds green, no-harm clean, additions
  only). Evidence: `negctl-green.log`, `negctl-mutant-kill-after.log`,
  `plain-equal.log`, SKILL.md registry diff.
- **discernment: improved** — five real defects mined with evidence
  pointers and fixes, four caught before any committed byte could
  mislead (preprobe + bash -n + pin-vs-receipt + prior-receipt
  cross-checks); the honest red state — legs-green and conformance-red
  over the SAME committed bytes — is the round's central evidence, and
  the first receipts draft that attributed grep exits to the probes was
  overwritten before landing and mined rather than shipped. Evidence:
  `corpus/lessons/round-87.md` `## Mistakes`.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md gained the `probe_negctl2` registry row this round (r87 bytes); the standing non-author re-confirmation is operator-side routing (`corpus/lessons/round-69-verifier-spotcheck.md` lineage; the r86 closure note 2 names the mechanism); no box marked by the author.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round's evidence-ledger task (red→green instrument conformance with mutation receipts) is logged in the LOG.md round-87 block and re-derivable from committed bytes (`reports/round-87/negctl-green.log`); no producer rerun this round (no fixture claim declared).
- [~] Instructions executable by an agent without oral context — the frozen counting commands and both sed mutant recipes were executed verbatim this round with observed exits matching the claims.md pins (`negctl-red.log`, `negctl-green.log`, `negctl-mutant-kill-after.log`); no independent outside instruction verifier this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md byte-unchanged in the round range (`noharm-diff.txt`); ADJ-06 remains reported, not absorbed; no contested scope this round; no outside verifier this round.

Assimilation: considerthese re-read (2026-10-20 through 2026-10-28, the
same eight files; no new proposals since r70's window). One
still-unimplemented proposal considered (the 2026-10-28 lesson-1 Q16
claimed-coverage-set vs actual-compared-set checker) and not adopted
this round — its natural consumers are the operator-blocked C05 re-gate
surface, and it is a larger instrument than one bounded round; routed.
Adopted nothing — shokuknow unreachable.

L0 side channel: nothing new filed this round; the standing operator-side
questions (r74 dispatch surface, r79 census literal form) were re-read,
remain unanswered, and were routed around with receipts.
