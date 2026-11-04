# kaidoku round 73 — report

Lane `kaidoku-shokunin`, round 73, attempt 1. Base `05bf065684e52d72ea25aad95f7acb71fcd7874c`;
lane tip `0c8eb69730dbd788874ca2cb64973488850af162` (pushed; `ls-remote origin refs/heads/main`
prints it). Claims: **R73-C1 coverage** (the kernel-side witness), **R73-C2 calibration** (the
record audit), **R73-C3 operability** (the reader-seam battery). All three are capability
acquisitions and all three verify on the frozen counters. **lowest-axis: coverage** — no nudge
waiver is claimed (the round-72 spot-check's routed defect 6 correction).

## Work performed

- **Declared three claims on three distinct axes** in `plans/round-73-claims.md`, froze them in
  `.ufo/waves/round-73/claims.json` (freeze `8b928422b51e2f03039ab365f7bafa838389c6d2`; the
  round-29 gate audits that freeze FLAGGED on `INSTRUMENT_PIN_MISMATCH`, see the gate bullet),
  and disclosed five errata/supersessions in that container before landing data: the base-arm
  comparator (erratum 1), a grep-count typo (erratum 2), two producer pins (erratum 3), the
  instrument fix `d36c6ee0` and the hardening `55cac1d2` plus the D2 target `ada4f902`.
- **R73-C1 — the kernel's record.** `tools/round-73/seam-probe.py` gains A12: `kernel_witness`
  polls `/proc` for a process whose argv names the run's shim dir **and whose parent chain
  reaches a pid the arm started**, then reads `/proc/<pid>/environ` (key census only,
  HOME/TMPDIR as containment booleans). A12 carries its own falsifier: a forged sub-run whose
  child dumps read clean while its kernel samples read dirty. Landing 12 of 12,
  `A12_kernel_witness` true, `failed []` (`.ufo/waves/round-73/l1/scores/c1-at-landing.json`).
- **R73-C2 — the record audit.** `tools/round-73/record-audit.py` re-derives seven atoms (D1–D7)
  from the receipts the record cites, over a population derived from the round-72 non-author
  spot-check's routed-defect list. 6 mismatches at base `05bf0656`
  (`.ufo/waves/round-73/pre/c2-at-base.json`) → 0 at the record revision
  (`l1/scores/c2-at-landing.json`, exit 0). Five record repairs landed as **appended**
  corrections in `SCORECARD.md` and one appended provenance block in the round-72 knowledge
  entry; the freeze ledger row, the recorded checker rc and the six registry rows complete the
  set.
- **R73-C3 — the reader seams.** `readelf_header()` and `implicit_capsule()` are extracted from
  `check_receipt` so a selftest can exercise them; three cases bind the three round-72
  MutReaders survivors. Landing `--patch-set r73`: `survivor_count 0`, each mutant killed by its
  declared case, pristine 38 cases green, target pin matched
  (`l1/scores/c3-at-landing.json`).
- **Wave.** One v1 wave `r73-w1`, 16 seats (5 executor, 3 scribe, 2 reviewer, 2
  mutation-tester, 1 critic, 1 sentinel, 1 scout, 1 connector; attack 5/16 = 31%), all 16
  settled, none dead (`.ufo/waves/round-73/r73-w1-results.json`). The L1 held the planner seat;
  no residual call. Findings fixed in-round: SentinelScope's three blocking items (argv-only
  selection, interpolated shim source, HOME/TMPDIR values) and CriticClaims' D1 false-green;
  routed to round 74: MutProbe's six A12 selftest survivors and ExecC2's D7 false-green.
- **Frontier step.** S277 opened (man-pages 6.19 `proc_pid_cmdline(5)`, HTTP 200, 7 918 B,
  sha256 `1fc68168…`, 15-word located quote) and cited by the new knowledge entry; the lesson
  `corpus/lessons/round-73.md` mines four mistakes with their captured-by; assimilation
  `none` (the package does not serve these claims); `considerthese/` absent in this lane.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| six round-73 instruments + the frozen plan + census start | round-73 entry, "Claims" | `da6c17c1` |
| claims container, wave spec, nonce commitment, route receipt | "Claims" | `8b928422` |
| instrument fix (per-seam records, readelf seam body, `r73base` site) | "R73-C3" | `d36c6ee0` |
| hardened probe/audit/controls, container errata, ledger rows | "R73-C1", "Controls", "Gate" | `55cac1d2` |
| corrected container (pins, D2 supersession) | "R73-C2" | `73b29fdb`, `ada4f902` |
| ledger row telling the gate's truth | "Gate" | `0b363371` |
| knowledge entry, lesson, QUALITY 129–132, PROVINCE, README, SKILL, SCORECARD, LOG, S277, landing receipts | the whole round-73 entry | `e0094011` |
| landing/base receipts and the D2 change | "R73-C2" | `55c1b703` |
| the six registry rows under grammar v2 | "Record" | `362e193b` |
| closing receipts (census end, audit, gate, registry census) | "Gate", "Sources" | `0c8eb697` |

## Before → after measurements

| claim | counting command | before | after | measured at |
|---|---|---|---|---|
| R73-C1 | `python3 -I -B tools/round-73/seam-probe.py --root . --rev <rev> --tool <route> --battery <battery> --pkg <REA> --work <scratch> --receipt <route receipt> --expect-upx <pinned copy> --nonce-commitment <hex> --json-out <receipt>` | the round-72 probe: **11 arms, 11 passed, no A12** (`pre/c1-at-base-r72probe.json`); the round-73 probe against the round-72 route: **8 of 12** (A2/A10/A11/A12 false — erratum 1); `grep -c '/proc/%d/environ'`: **0** vs **1** | **12 of 12**, A12 true, genuine 4-key samples with both containment flags, forged 275-key samples + canary, `forged_detected true` (`l1/scores/c1-at-landing.json`) | `d36c6ee0` |
| R73-C2 | `python3 -I -B tools/round-73/record-audit.py --root . --rev <rev> --json-out <receipt>` | **6 mismatches** (D1, D2, D3, D4, D5, D6; D7 true) at `05bf0656` (`pre/c2-at-base.json`) | **0 mismatches**, 7 atoms ok, exit 0 (`l1/scores/c2-at-landing.json`) | `362e193b` |
| R73-C3 | `python3 -I -B tools/round-73/mutation-check.py --root . --rev <rev> --tool <route> --patch-set <set> --work <scratch> --min-pristine-cases 38 --expect-target-sha256 <hex> --json-out <receipt>` | `--patch-set r73base` on the round-72 route: **3 survivors** (`pre/c3-at-base.json`) | `--patch-set r73`: **0 survivors**, `killed` names `git-reader-allowlisted-exec`, `checker-readelf-allowlisted-exec`, `implicit-capsule-polluted-raw-log`; pristine 38; `target_pin.matched true` (`l1/scores/c3-at-landing.json`) | `d36c6ee0` |

Controls: six arms, all met (`l1/scores/controls-at-landing.json`) — no-kernel-channel probe,
blind-witness verdict, base audit 6, lying audit receipt rejected, base reader mutants 3,
stripped registry red on `case-inventory`.

**Freeze-gate finding (disclosed, not repaired).** The freeze `8b928422` pins two round-72
producer digests that are not the blobs at the freeze (`973d504b…`/`7f46e3ef…` against
`330ecf89…`/`602b305d…`). `tools/round-29/freeze-gate.py` reads pins from the freeze commit, so
round 73 is **FLAGGED** `INSTRUMENT_PIN_MISMATCH` at every measured revision
(`l1/scores/gate-at-freeze.json`, `gate-at-record.json`, `required_failed ["round-73"]`). The
container is corrected at the record revision (erratum 3) and the ledger row
`corpus/claim-freezes-v2.tsv` says `round-73 FLAGGED INSTRUMENT_PIN_MISMATCH`; disclosures are
48 of 48 exact, missing `[]`, stray `[]`. Planned item (d) pins producers from the blobs at the
freeze next round.

## Sources & frontier

- `corpus/SOURCES.md` **183 → 184 rows**. Counting command:
  `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku` — start exit 0
  (`l1/census-start.txt`), end exit 0 with 24 W04 duplicate-URL warnings
  (`l1/census-end.txt`).
- Rows added by tier: **1 tier A** (S277, `proc_pid_cmdline(5)`, docs, opened 2026-11-04, mined).
- Rows touched old→new: **none** (S275 was opened in round 72 and is cited, not re-registered; no
  status/recheck/used-by change on an existing row).
- Frontier rows advanced: **"a producer-independent (hostile-wrapper) child census"** — the
  round-72 note's line becomes Core for the sampled-descendant case
  (`PROVINCE.md ## Round-73 additions to Core`; `corpus/README.md` round-73 frontier note); the
  remainder (a wrapper that never runs a sampled process, `PR_SET_MM_ENV_START` relocation,
  non-Linux substrates) stays Frontier.
- Sourced claim: R73-C1 cites S277 through
  `corpus/knowledge/2026-11-04-r73-kernel-witness-record.md` (trio at the file's open, atom D5).
- Assimilation: **none** — `merge/kaidoku/` does not serve these claims; nothing adopted.
- `considerthese/`: absent in this lane (no directory).

## Trend verdicts

- **expansion: improved.** One admitted tier-A row on ground the round-72 note held only as a
  Frontier bullet (the hostile-wrapper census), a new knowledge entry with a channel table and a
  limits section, and the frontier note moves the sampled-descendant case to Core. Registry
  183 → 184.
- **quality: improved.** Three instruments now bind what they claim: A12's ancestry guard closes
  a decoy selector, the audit's D1 requires the measured digest in a correction, and the three
  reader seams have named cases. The wave's three blocking security findings and one
  false-green are fixed in-round under disclosed supersessions; six A12 selftest survivors and
  D7's false-green are named debt.
- **discernment: improved.** The wave falsified the first cut on four independent fronts
  (decoy selection, interpolated shim source, value serialization, D1 wrong-token acceptance),
  each with a receipt, and the round's own freeze was wrong in two places the gate caught — both
  disclosed rather than repaired by rewriting. The freeze-gate FLAG is reported as the gate
  found it.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  six round-73 registry rows in grammar v2 (census 105 rows, 0 nonconformant,
  `l1/scores/registry-census-at-record.json`), the knowledge entry and QUALITY 129–132 carry the
  decisions and their evidence; no non-author verifier has signed this box.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the three claim
  commands ran end to end at `d36c6ee0`/`362e193b` and their receipts are committed; the
  round-73 LOG entry records them.
- [~] Instructions executable by an agent without oral context — every instrument's invocation
  is a frozen command in the plan, the registry row and the report; a non-author seat
  (ExecSweep) re-ran them from the plan text alone.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — ConnectorCross found sibling owners
  for the surfaces (kama, chousa, mado) and reports them as adjacency, not absorption; the
  PROVINCE section names only this lane's instruments.

**Stale-lane:** respawn-per-round driver (this round was dispatched inline by the hyaku
orchestrator); no other mission of this lane is open.

**Tool installs:** none this round (no pacman transaction, no uv/npx install); the host's pacman
pause was not exercised.

**Open L0 questions:** none new; `kaidoku | round-72` (raw child-env dumps) stays open and is
honoured by A12's key-census record.

**Previous-attempt state:** the watchdog shows no `lane-dead-no-report kaidoku round=73` line —
this is the first attempt; no inherited uncommitted lane work was found (the lane tree was clean
at base and the wave dir was created this round).
