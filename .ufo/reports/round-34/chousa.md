# chousa — round 34 (attempt 2) report

Lane: chousa-shokunin (deep-research method: question framing, source hierarchy, citation
chaining, claim-vs-source verification). Driver: hyaku-inline attempt=2 (watchdog launch
2026-10-23 15:04:49 -03). Attempt 1 of this round died `lane-dead-no-report` (~09:30 -03)
after landing its work (`f20aeaa7`…`bf7c931a`); this attempt inherits it, re-verifies it,
and completes the round. Lane HEAD at report: `08be4c9e3a4ebe55d915ce4761c81854286c23ae` (final: post-cutoff wave reports ExecC1RerunA2.md and ExecC2Oracle artifacts; HEAD was `8bc930a9` when this report line was last meaningfully accurate) (late-arriving wave evidence committed
after the integration cutoff: ExecC1RerunA2's four c1v3 receipts on the C2-landed gate — LONGSPAN_MATCH=42/42
on seeds 4601-4603 (LC_ALL=C) and 4604 (UTF-8) — closing the gap that every committed c1v3 receipt had bound
the pre-C2 gate; plus its mutation battery and a SKILL.md stale gate pointer it flagged, fixed in `8bc930a9`).

## Work performed

Declared claims (frozen before data, `corpus/evidence/round34/claims-a2.md`, design v4
`7c7eb3a6`):
- **C2 — operability** (the lane's only scored, hence lowest-scoring non-retired axis):
  `verify-claims` verifies spans of 32765..32767 bytes — the dead zone where the
  4-bytes-per-byte PCRE pattern still fits one grep argv string but PCRE2 refuses to
  compile it ("regular expression is too large", row S065).
- **C3 — calibration**: the lane's round-34 self-assessment vs observed repo state,
  counted — `self-audit.py` + committed `audit-set.json` + `audit-dispositions.md`.
- Inherited, NOT re-opened: attempt-1 **C1** (spans ≥32768 bytes) stands at `unverified
  (required controls held)` per its frozen exclusion; attempt-1 repairs E1–E5 stand.

Work items (evidence pointers lane-relative):
- Dead-zone probe on the landed gate, 20 lengths × 5 content classes: the failure window
  is exactly 32765–32767 bytes and length-only (`/fast/scratch/hyaku/chousa-r34-a2/probe/`);
  the planned-r35 hypothesis "about 28000–32767" was wrong (mined as a lesson).
- C2 counter `corpus/evidence/round34/c2-count.py` (37 records, 17 classes, per-seed
  generated): do-nothing control on the unfixed gate `772a1d8e` = 21/37 on seeds
  5011/5023 (`measure-a2/c2-before-s*.json`, `2592f9da`).
- C2 fix `fe0f22e0`: `TOK_DIRECT_SPAN_MAX` 32767→32764 (sole functional line — RevGateDiff),
  selftest cases 254–256, gate `a6307edf…`; after: 37/37 on seeds 5011/5023/5033/5047
  (`measure-a2/c2-after-s*.json`) + L1 fresh re-runs 7001/7013.
- No-harm battery 11 rows PASS (`measure-a2/battery/`); selftest 256 cases.
- C3 first counted run 0/0 over 43 checks (`0af0844c`); negative control 2 lies → 2.
- Frontier: S065 re-opened (pins unchanged; 32765 boundary re-confirmed); knowledge entry
  `corpus/knowledge/dead-zone-pcre-r34.md`; lesson attempt-2 sections; SCORECARD/LOG/SKILL/
  README/SOURCES updates; capability row added.
- Inherited-state resolution: attempt-1's untracked leftover
  `corpus/evidence/round34/__pycache__/` (debris from running its counter) deleted and
  named here; `.ufo/waves/round-34/` attempt-1 debris reused after re-verification (its
  counters re-run inside the no-harm battery and the C3 receipt bindings); a second
  `__pycache__` written mid-wave by a seat was removed by that seat (MutC2Trunc).
- Misroot sweep: fleet root shows a `0` file (`NF=13 cells=11 double_quotes=0`, 09:09 -03)
  and `.ufo/waves/round-58/` — neither names chousa; both left untouched and named here.
  No chousa seat wrote to the fleet root.
- Wave 2 = 33-seat falsify/verify wave against committed bytes at tip `707da818`, dispatched
  by the orchestrator as one batched call per the mid-flight dispatch directive; 23 of 33
  seat reports returned and are committed under `.ufo/waves/round-34/w2a2/`; 10 were still
  queued behind the host 100-jobs-per-session clamp at the integration cutoff (named below;
  none dead, no error text).

## Landed changes

(All tied to LOG.md "Round 34 — attempt 2" and the wave addendum; commits via
`scripts/hyaku/jj-lane.sh`, each `landed` with push.)
- `7c7eb3a6` design v4 + C2 counter · `2592f9da` C2 do-nothing receipts · `fe0f22e0` C2 gate
  fix + selftest + after-receipts + battery + SKILL tallies · `0af0844c` C3 tool/set +
  first-run + negative control · `fce3119c` SCORECARD/LOG/README/SOURCES/lesson/knowledge ·
  `707da818` lesson able-to-fail evidence (`measure-a2/deadzone-fixture-vs-gates.txt`) ·
  `bd8c8bd8`/`fe3db76c` wave spec/plan/taskCall · `b8e782a1` C3 reshape integration ·
  `0b0af3ef` SCORECARD literal + pattern anchor + claims-a2 re-pin · `50a8c693` wave
  evidence + erratum wording + final receipt · `60b41dad` final audit receipt ·
  `53e4aa05` census end receipt.

## Before → after measurements

- C2: `LC_ALL=C python3 corpus/evidence/round34/c2-count.py --seed N --receipt F` —
  before 21/37 (seeds 5011/5023, gate `772a1d8e`) → after 37/37 (seeds 5011/5023/5033/5047,
  gate `a6307edf`, `fe0f22e0`; L1 re-runs 7001/7013). P2 met: four committed 37/37 receipts,
  no committed below-37 run (RevC2Receipts scanned), re-derived by ExecC2Rerun on fresh
  seeds 7311/7417/7589.
- C2 supporting: selftest PASS 256 at `fe0f22e0`; no-harm battery 11 rows; C1's counter v3
  re-run by wave seats on the new gate (42/42 class holds — ExecC2Rerun history scan; the
  dedicated ExecC1RerunA2 seat was queued-out, named below).
- C3: `python3 corpus/evidence/round34/self-audit.py` — first counted run
  `SELF_AUDIT_MISMATCHES=0` / `SELF_AUDIT_UNDISPOSITIONED=0` over 43 checks (`0af0844c`,
  re-run byte-identical by RevC3Set/MutC3Inject). Wave verdict: the written form was
  falsified by CritC3Claim (a shallow-set do-nothing reproduces identical 0/0 under planted
  drift); reshaped in-round to a bounded structural-audit acquisition: 62 checks (content
  pins of the self-assessment documents, 9/9 measurement-receipt bindings + a
  `receipt_gate_file` kind for control receipts, HEAD-byte reads so a dirty worktree cannot
  move the count, `SET_SHA256` per run); identical before/after measurement — 3 counted at
  the pre-integration tree (2 real: the SKILL banner vs the gate's exact output form,
  ScoutSkillTally; 1 superseded-pin artifact) with 1 undispositioned
  (`measure-a2/audit-v3-prelim.txt`), and at the landed tip 1 counted (the superseded tool
  pin, dispositioned), 0 undispositioned over 62 checks (`measure-a2/audit-v3-final.txt`).
  Assessment-derived controls: 5/5 injected lies killed exactly (MutC3Inject); junk auditor
  killed by re-derivation; do-nothing unreachable (MutC3Bypass).

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin chousa` — round start (attempt 2): exit 0 (W04 S051/S053
duplicate-URL warnings + ok row); round end: exit 0 (same two warnings; receipt
`measure-a2/census-end-a2.txt`).
Rows before → after: 66 → 66 (attempt 1 opened S064–S066; attempt 2 opens none; S065
re-opened this attempt with pins verified — sha256 `a3ea2c67…74bd6`, pcre2 10.49-1, both
gate quotes verbatim — and its used-by now also lists `corpus/knowledge/dead-zone-pcre-r34.md`).
Located quotes (opened this round, installed copies, no network):
- S064 execve(2), man-pages 6.19-1, sha256 `4489dfef…0dc`, accessed 2026-10-23: "Additionally,
  the limit per string is 32 pages (the kernel constant MAX_ARG_STRLEN), and the maximum
  number of strings is 0x7FFFFFFF." (attempt 1; anchor corrected in-round after
  R34ReopenSources; re-verified by ScoutSourcesA2)
- S065 pcre2limits(3), pcre2 10.49-1, sha256 `a3ea2c67…4bd6`, accessed 2026-10-23 (re-opened
  this attempt): "The maximum size of a compiled pattern is approximately 64 thousand code
  units for the 8-bit and 16-bit libraries" — the ceiling C2 rests on; the row's host note
  (32764 compiles / 32765 rejects) re-confirmed by this attempt's probe.
- S066 grep(1), grep 3.12-2, sha256 `9b027d02…85ba`, accessed 2026-10-23: "Obtain patterns
  from FILE, one per line." (attempt 1; re-verified by ScoutSourcesA2). Note: the row pins
  the GNU man page, not the binary — this host's `/usr/bin/grep` self-reports "pi-uu-grep
  0.2.0" while pacman owns grep 3.12-2 (RevGateDiff ENV HAZARD, confirmed in this attempt's
  shells; the 32764/32765 boundary measured identically in every in-round run; the gate
  resolves bare `grep` via PATH at research-gate.sh:1618/1641/1687; r35: pin the binary and
  verify provenance).
Touched old→new: S065 used-by adds the dead-zone knowledge entry (logged in the lesson).
Frontier rows advanced: S065 (re-open, pins unchanged). Rejects this attempt: none new.
Mined mistakes: `corpus/lessons/round-34.md` attempt-2 rows — (1) planned-hypothesis-as-
measured (28000–32767 vs the measured 32765–32767); (2) C1's chunk matcher shipped with no
selftest case (cases 252–253 use the 29999-byte direct path), fix cases 254–256, shown able
to fail (`measure-a2/deadzone-fixture-vs-gates.txt`); (3) a C3 negative control first wired
to read the pristine lane set; plus the wave-2a2 table: shallow-set calibration claims,
keyed-engine output-equivalence, window-coverage arithmetic, the `\u2192` locale root cause,
the grep-binary hazard, the `slen` dynamic-scope coupling, and the worktree-vs-HEAD audit
read (fixed in the deepened auditor).
Sourced claim: C2 rests on S065 (opened this round, re-opened this attempt).

## Trend verdicts

- expansion — **improved**: a new measured surface (spans 32765–32767 bytes) with a
  capability row; the dead-zone knowledge entry covers previously undocumented ground (the
  two-ceiling interaction and the exact 3-length window); the audit tool acquires a
  receipt_gate_file kind and HEAD-byte reads (capability acquisition within the claim).
- quality — **improved**: the chunk matcher gains selftest cases; S065 re-open pins hold;
  the LC_ALL=C selftest failures are root-caused to one byte (`\u2192` decodes only in a
  UTF-8 locale; all 10 failing blocks carry `CLAIM_SPAN_NOT_FOUND obs=id=P4`; none of the
  new dead-zone cases is locale-dependent — ExecSelftestEnv); the counter is sound (10 stub
  attacks fail-closed; 1110 generated spans across 30 seeds, zero window violations —
  RevC2CounterCode).
- discernment — **improved**: C3 became a demonstrated (not asserted) calibration
  instrument — the count moves on real drift (before 3, after 1-dispositioned) and the wave
  falsified-and-reshaped it within the round; C1's unverified verdict held under wave
  attack with the exclusion intact (CritC1Wording was queued-out; the C1-row wording was
  checked by the L1 against the exclusion record).

## SHONEN

- [~] SKILL.md decision tables/cited sources — `SKILL.md` gates table + `corpus/knowledge/
  dead-zone-pcre-r34.md`; wave seat ScoutSkillTally re-derived every range (all match after
  the exact-banner fix it found). No non-author verifier on record (RevShonenA2's caution:
  a lane-dispatched seat does not qualify per PROTOCOL) — closure's call.
- [~] End-to-end domain task logged — round-34 C2/C3 entries; RevShonenA2 re-executed the
  r9 verify-all task (CLEAN, tallies reproduced). Same verifier caveat.
- [~] Instructions executable without oral context — `bash tools/research-gate.sh
  --selftest` PASS 256 re-run by RevShonenA2 (receipt `w2a2/RevShonenA2/selftest-tip.log`).
- [~] No cross-domain bleed — PROVINCE.md diff empty (RevShonenA2); RevProvinceA2 was
  queued-out, named below.

## Round shape and wave accounting

- Shape: **default — two v1 waves**. Wave 1 = attempt-1 build wave, 32 seats (registry
  `w1/swarm-registry.json`) + 7-seat residual falsify call (`w2/residual-call.json`).
  Wave 2 = this attempt's 33-seat falsify/verify wave (roles: 10 mutation-tester, 9
  reviewer, 4 critic, 5 executor, 2 scout, 2 scribe, 1 connector; 23 attack = 70%),
  validated under policy v1 (band 32–64, `scripts/hyaku/ufo-wave-policy.json`,
  dispatch.calls=1), dispatched by the orchestrator as one batched task call per the
  mid-flight directive (no seat dispatched from this session; spec/plan/taskCall committed
  `bd8c8bd8`/`fe3db76c`). Round total: 32 + 7 + 33 = 72 seats ≤ 128. No planner seat
  anywhere (L1 holds the §3 planner seat; the planning data-walk rode scout/reviewer items).
- Dead seats: attempt 1 — five provider `cyber_policy` holds (CtlC1Shortcut, CtlC1Windows,
  CtlC1Halves, MutC1Counter, CritC1AxisFit; refrozen as the exclusion, never rerouted).
  This attempt — none dead; no error text received.
- Returned: 23 of 33 wave-2 reports committed (`w2a2/*.md`). Queued-out at the integration cutoff (named, not dead, no error text): ExecC2Oracle,
  ExecNoHarmA2, CritC1Wording, CritRoundShape, RevClaimsA2, RevQualityA2, RevProvinceA2,
  ScribeReportFacts, ScribeCloseout. ExecC1RerunA2 returned post-cutoff (see HEAD note above). Their items are covered by redundancy (ExecC2Oracle's
  feasibility by the four 37/37 receipts + MutC2Counter's ablation; ExecNoHarmA2 by the L1
  battery committed at `fe0f22e0`; CritRoundShape's registry counts by the committed
  w1/w2 registries) or remain open honesty gaps named for the closure.
- Residual call: none (the falsify wave itself is the attack surface; no second wave was
  dispatched under the orchestrator's all-dispatch-via-Main rule).

## Stale-lane / extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs this attempt: none (L1 and wave seats installed nothing; the host's
  `/usr/bin/grep` provenance anomaly is named above as an r35 check, not an install).
- L0 questions: none new this attempt. Standing: the fetch-scope question (man7.org
  unregistered host — S064's URL recorded but not fetched) and the rea MCP pin rewrite
  reported by kaidoku r19 (operator-owned file, untouched).
