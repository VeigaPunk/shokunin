# round-85 report — revenger (hyaku run 23)

Lane tip at report time: `d14e4c847a8895d9571b8fc2facaf840bf5d2687`
(branch `main`, pushed; base `8cf92f0c7c3d983181ac458ae90c2bb687226f62`).
Claims: two, distinct axes (coverage, calibration), causally separable,
neither exploratory. Carry-in (r84 non-author closure D1–D3,
status-neutral) addressed first.

## Work performed

- **Carry-in D1 (wording precision), status-neutral** —
  `reports/round-85/corrections.md` correction 1: the r84 report prose
  absolute ("ZERO instrument rows") corrected to the precise class
  statement — zero holds of the **bare-token class** only; the
  PATH-form twin row exists at `reports/round-84/v4-invisible-red.log:637`
  (`SWEEP absent reports/round-83/v4-postlanding-recon.log`); the r84
  `claims.md` §C2 wording governs. The fleet report is orchestrator-owned
  and is not rewritten; the correction is the lane-side file plus a
  standing wording rule honored by every r85 text (this report's C2
  bullet names the bare-token class explicitly). Commit
  `9cadaedeba8ed7968e4acd2907d2a4fb30090a83`.
- **Carry-in D2 (post-adjudication absolute as a committed file)** —
  `.ufo/waves/round-85/postadjudication-sweep.log`: the v5 committed
  blob (sha `d9a7ba17…46cb`, re-verified over the worktree immediately
  before the run) over tip `8cf92f0` + fleet root →
  `CITED=1024 COMMITTED=964 LANDABLE_ORPHANS=0 ABSENT=60` exit 0, basis
  `SWEEP_CORPUS fleet-reports=25 lessons=50 log=1` cited first — the
  closure-time prose absolute is now reproducible from a committed
  receipt (per-revision-corpus basis movement disclosed in its header).
  Commit `9cadaed`.
- **Carry-in D3 (census literal form, standing)** — dual round-start
  receipts `.ufo/waves/round-85/census-round-start-{sanctioned,literal}.log`:
  sanctioned explicit-lane-dir form exit 0 (21 W01 + 10 W04, zero E —
  the same disclosed classes as r74–r84); contract-literal form exit 2
  (`<root>/revenger-shokunin/corpus/SOURCES.md` missing — the disclosed
  r74–r84 lineage). Routed around; nothing assumed answered. Commits
  `9cadaed` + `acfb3b4ad24caf8e550edd4c96c4ecb9f9657d96`.
- **C1 (coverage, criterion M)** — registered the managed-provider
  criterion (`reports/round-85/mg_probe.py`, sha
  `1840c30cf4f1cad0815c89ca80492053d4a43c5d752609a2edf33fa21a3ac03f`,
  scan shape born v2.1 — rglob `inspection.json` by name; denominator
  disclosure pre-run, S469: exactly three available operations) and
  landed three real oracle-checked producer records on the authored
  inert 1048-byte IL-only PE/CLI fixture (`corpus/fixtures/managed-r85/`,
  generator `self_check()` re-derives every premise from the built
  bytes, regen byte-identical across scratch and landed builds,
  `truth.json` Q07 hypotheses frozen pre-run, `oracle_check.py`
  re-derives every BYTE value from fixture bytes with its own
  independent parser, negative control demonstrated pre-run — one
  mutated field flips the members oracle to `ORACLE FAILED (46/47)`):
  `rea inspect-managed-artifact` Evidence `ev_0eea92d7…f796e2` ORACLE OK
  20/20; `rea inspect-managed-members` Evidence `ev_e5d7a0b9…ae359f4`
  ORACLE OK 47/47; `rea inspect-managed-native-boundaries` Evidence
  `ev_2115d335…063890ba` ORACLE OK 39/39 — all exit 0, stderr 0 bytes.
  Freeze `d27cf95db88b86de611fb5931dd0e89d2a1da8a7`, landing
  `8b49e2d9507340c8faa2cbf6a7d4ae4c8d36c7ab` (20 files, 1226 insertions,
  0 deletions), adjudication `f09cadad9a51aa0671477fd2f754ef8a2ce4ba31`.
  Honest note, disclosed pre-freeze: the red is 0/3, not 1/3 — the r76
  artifact record is real but predates the oracle-receipt gate (its
  receipt carries no `oracle` field), so the registered definition
  counts it unrecorded; the r76 record is not re-graded.
- **C2 (calibration, orphan_sweep v6)** —
  `reports/round-85/orphan_sweep6.py` (sha
  `b2db45b07bc86ffd501971582730497e2d5ddc83e685665c200fc24b3c7f12b7`;
  v5 blob unchanged `d9a7ba17…46cb`) closes the r84 lesson's routed v6
  candidate vector 2 — change 9: an unmatched bare token whose basename
  exists under the fleet root resolves `absent-fleet` (bare-token
  normalized, up to 3 matches shown, `(+N more)` beyond) instead of
  being recorded as an unmatched absent row; absent-fleet never gates,
  exit codes 0/1/64 unchanged. Selftest 21 legs + pass from the
  committed blob (`sweep6-selftest-after.log`); ONE frozen one-substitution
  sed mutant dies exit 1 attributed (`sweep6-mutant-kill-after.log`,
  `FLEET_BARE_RESOLUTION` → `selftest: fleet-bare resolution drifted
  (fleet-bare class)`, exactly line 115). Separability `c1-only.log` /
  `c2-only.log`; no-harm `noharm-diff.txt` (protected paths empty
  `d27cf95..8b49e2d`, additions only, FRESH_ROWS 18/18).
- **Fresh-start §7** (the prompt carries the FRESH-START gate; the
  r74–r84 closures were admitted, and the gate was run anyway,
  conservatively) — r71/r72/r73 rejected closures re-read and
  spot-checked (all three are K-admission claims whose wave Q-review
  surface never settled on this host; a do-nothing control reaches each
  identically here; neither r85 claim routes through K). Fresh probes
  (receipt `reports/round-85/freshstart-probes.log`, 2026-11-02): F
  android (`REA_JADX_MCP_JAR` UNSET, no jadx — S448 stands); macho/
  signature (`unsupported_host`, 7 groups printed this round vs 8 at
  r84 — the lane records the count it prints, not a cause); K admissions
  (r74 L0 unanswered, re-read); criterion C repair (§9); R-extension/
  N-attribution (stay routed); ghidra-headless repeat (the r75
  capability row holds — a repeat reaches no new measurement). C1's
  route is the one every standing ruling-out map left open (the managed
  pair — both recorded-state greps print empty through r84).
- **Defects found and fixed this round (all mined,
  `corpus/lessons/round-85.md`)** — (1) treecommit absolute-path args
  built an EMPTY carry-in commit (`ac91c05`); caught by the mandated
  post-commit diff check; completed by `9cadaed` with repo-relative
  paths. (2) Two treecommit args named files still scratch-side —
  silently skipped (`9cadaed` carried 2 of 4); caught by the same
  check; completed by `acfb3b4`. Rule landed in the lesson: repo-relative
  args only, every arg must exist on disk before the call, the landing
  diff must count one numstat row per arg (third variant of the
  r78/r84 class). (3) ImplMap.MemberForwarded coded row 1 (SayHello,
  carrying an IL body) instead of the P/Invoke row 2 — the preprobe
  boundaries record exposed it; fixed pre-freeze. (4) ECMA metadata
  authoring triple (blob compressed-length prefixes; #US terminal flag
  0x00 per II.24.2.4; table numbers 0x1A/0x1C) — all caught by the
  producer's own preprobe outputs before any committed run. (5) Oracle
  parser bugs (rows at t+48; GUID (n-1)*16; table names) — caught by
  the oracle-vs-preprobe cross-check; the negative control re-run after
  the fixes still FAILs. (6) f_probe4's score line pinned by `tail -1`
  is its families list — grep the named token, never tail -1.
- **Assimilation** — `considerthese/` re-read (2026-10-20 through
  2026-10-28; proposals 1–3 grounded out r83/r84, proposal 4 sits in
  the §9-ruled criterion-C space, proposal 5 is the daily bot's own
  procedure, not lane scope); adopted nothing — shokuknow unreachable.
- **L2 floor** — no dispatch surface on this host (r74 L0 stands); all
  verdicts re-derive from committed bytes.

## Landed changes

| change | commit |
|---|---|
| carry-in (EMPTY — the treecommit absolute-args class, mined) | `ac91c05` |
| carry-in landing (D1 corrections.md, D2 postadjudication-sweep.log) | `9cadaed` |
| carry-in landing completion (round-start census receipts) | `acfb3b4` |
| freeze (claims, mg_probe, orphan_sweep6, reds, preprobe, §7 gate, mutant receipt) | `d27cf95` |
| landing (fixture + three records + LEDGERs + S469–S471) | `8b49e2d` |
| adjudication (lesson, SCORECARD, LOG, mg-after, real-tree pair, separability, noharm, census-after) | `f09cada` |
| receipt completion (selftest + mutant-kill logs) | `d14e4c8` |

All cited commits are ancestors of `main` (linear chain
`8cf92f0 → ac91c05 → 9cadaed → acfb3b4 → d27cf95 → 8b49e2d → f09cada →
d14e4c8`); every commit pushed to `origin/main` and verified by the
mandated post-commit diff check (`git diff --numstat` per commit).

## Before → after measurements

- **C1 (coverage, criterion M)** — counting command:
  `PYTHONUTF8=1 python -I -B reports/round-85/mg_probe.py <archive>/corpus`.
  BEFORE (red, over the base archive `8cf92f0`, committed
  `reports/round-85/mg-red.log`): `M_RECORDED=0/3 score=0.00` (all three
  operations unrecorded; the r76 record predates the oracle-receipt
  gate — disclosed pre-freeze). AFTER (green, over the landing archive
  `8b49e2d`, committed `reports/round-85/mg-after.log`):
  `M_RECORDED=3/3 score=10.00`. Frozen holds over the same archive:
  `A1V2_RECORDED=5/5 score=10.00` (r84), `A1_RECORDED=3/3 score=10.00`
  (r82), `F4_COVERAGE=10/11 score=9.09` (r81). Oracles re-run over the
  archive bytes: `ORACLE OK (20/20 checks)`, `ORACLE OK (47/47 checks)`,
  `ORACLE OK (39/39 checks)`; regen byte-identical from the archive
  generator; record stdout shas match the receipt pins. Measured commits:
  red `8cf92f0` → green `8b49e2d`.
- **C2 (calibration, v6 supersession; no criterion score moves — the
  moved quantity is bare-token attribution fidelity)** — counting
  commands: `PYTHONUTF8=1 python -I -B reports/round-85/orphan_sweep6.py
  --selftest` (21 legs + `SWEEP_SELFTEST=pass`, exit 0, from the
  committed blob) and `… --lane <lane-dir> --fleet <fleet-root>
  --format full`. BEFORE (red pair over ONE pre-landing tree, frozen at
  `d27cf95`): `v5-full-prelanding.log` — 48 unmatched recorded absent
  rows including `SWEEP absent MISSION.md | bare-token unmatched: no
  file named MISSION.md under HEAD or the working tree`;
  `v6-full-prelanding.log` — SAME tree,
  `unmatched_recorded_absent=26 fleet_resolved=22`, rows
  `SWEEP absent-fleet MISSION.md | bare-token normalized:
  fleet/MISSION.md`; gating values identical
  (`CITED=1024 COMMITTED=964 LANDABLE_ORPHANS=0 ABSENT=60`). AFTER
  (real-tree pair over the committed adjudication tip from the
  committed blobs, `sweep6-real-after.log`): v5 48 absent rows vs v6
  26+22, gating identical `CITED=1025 COMMITTED=965
  LANDABLE_ORPHANS=0 ABSENT=60`, both exit 0. Mutant: the frozen sed
  copy (mutated sha `8a1706ee…05a78`, exactly line 115) dies exit 1
  attributed (`selftest: fleet-bare resolution drifted (fleet-bare
  class)`). Measured commits: red `d27cf95` → green `f09cada`.

## Sources & frontier

SOURCES.md rows 468 → 471. Counting command:
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
→ 471. Opened this round (all inside the Registry directly after S468,
NF=13 checked mid-flight): +S469 the M provider surface (`rea
capabilities` + both `--help` summaries + the freshstart probes; quote:
"Inspect PE/CLI metadata members, signatures, CIL anchors, and ldstr
string literals without loading target code", 15 words); +S470 the
three records + fixture (quotes: `ORACLE OK (20/20 checks)` / 47/47 /
39/39); +S471 the fleet-root bare-token class evidence (the v5/v6 red
pair + the r84 lesson's routed v6-vector note; quotes: "SWEEP absent
MISSION.md" bare-token unmatched vs "SWEEP absent-fleet MISSION.md"
bare-token normalized). C1 is sourced by S469+S470; C2 by S471. No
rejects this round (all three openings were admits; the §7
ruling-outs above are the round's reject-shaped decisions). Census:
round start sanctioned exit 0 (21 W01 + 10 W04, zero E), literal exit 2
(disclosed lineage); round end worktree exit 0 (21 W01 + 10 W04, zero
E), landing-archive exit 1 with the expected E11 ×3 (S469–S471
missing used-by the round-85 lesson that postdates the landing —
resolved by the adjudication commit `f09cada`); receipts
`reports/round-85/census-after.log`. Mistakes mined: six rows in
`corpus/lessons/round-85.md` (the treecommit absolute-args empty
commit; the treecommit absent-file-args silent skip; the ImplMap
coded-index authoring error; the ECMA metadata authoring triple; the
oracle parser bugs; the tail-line receipt assumption).

## Trend verdicts

- **expansion: improved** — the managed provider's full available set
  (all three declared available operations, S469) now carries real
  oracle-checked records (M 0/3 → 3/3 re-measured); no knowledge
  admission, K untouched (operator-blocked route re-checked, not
  attempted); F4's honest exception stays 10/11 (android hard-gate
  re-probed).
- **quality: improved** — a new registered coverage criterion with a
  byte-derived + pre-registered-hypothesis oracle split and a
  demonstrated negative control (the mutated-field FAIL printed in the
  preprobe receipt); the standing hygiene instrument's routed
  fleet-resolution class became machine-caught with a mutation-checked
  switch and a same-tree red pair; all verdicts re-derive from
  committed bytes (oracles re-run over the landing archive, selftest +
  mutant from the committed blob).
- **discernment: improved** — six real defects mined, four caught
  before any committed byte could mislead (three by the producer's own
  preprobe outputs, one by the oracle cross-check with the negative
  control re-run after the fixes), two treecommit landing no-ops caught
  by the mandated post-commit diff check within the round; the two
  honest disclosures (the 0/3 red shape; the 7-vs-8 unsupported_host
  group count) recorded rather than papered over.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md byte-unchanged this round (`noharm-diff.txt` protected paths); the routed need for a non-author re-confirmation of the CURRENT bytes stands (round-69 spot-check V7; r84 closure D4 surfaced it for the operator).
- [~] At least one end-to-end domain task executed and logged in LOG.md — this round: three real producer runs on an authored fixture, oracle-checked and committed (`corpus/live/runs/round-85/`, `mg-after.log`); LOG round-85 entry landed.
- [~] Instructions executable by an agent without oral context — the claims/receipt chain is runnable from committed bytes (`mg_probe.py`, `orphan_sweep6.py`, `oracle_check.py`, `generator.py` all re-run from the landing archive this round; exits in `mg-after.log`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md byte-unchanged (`noharm-diff.txt`); records scoped to the observed provider/operations/one authored image (Q10 notes in all three LEDGERs); ADJ-06 unchanged.

CLOSURE-PREP: re-runnable by the closure judge at the final tip
`d14e4c8` — extract the committed blob
`git show d14e4c8:reports/round-85/orphan_sweep6.py` (sha
`b2db45b0…f12b7`), run `PYTHONUTF8=1 python -I -B <blob>
--lane <lane-dir> --fleet <fleet-root> --format full` → expected
`LANDABLE_ORPHANS=0` exit 0 (basis `SWEEP_CORPUS fleet-reports=25
lessons=51 log=1` at report time; the tip confirmation run printed
`CITED=1043 COMMITTED=982 ABSENT=61 fleet_resolved=22` — counts are
per-revision-corpus, cite the basis line first); and
`git show d14e4c8:reports/round-85/mg_probe.py` over an extraction of
`git archive d14e4c8 corpus` → expected `M_RECORDED=3/3 score=10.00`.
