# tameshi — round 33 (attempt 2)

## Work performed

Declared claims (frozen at `f6d8a891`, contract `.ufo/evidence/round-33/contract.json`):

- **C1** — operability, capability acquisition: `tools/tally-audit-v2.py` audits the runner's
  `--regression` tally without editing it (routed from the round-32 closure). **Not measured this
  round** (honest stop): the sealed held-out set the predicate requires was never authored — see
  Before → after. The tool and counter were hardened through five disclosed pre-data amendments
  driven by a 33-seat wave-1 falsification wave.
- **C2** — freshness: repair the S055 digest drift with a `supersedes` row pinned by committed
  bytes. **Measured true** at the lane head.

Work items, each with its evidence:

- Froze both claims before any data seat: contract, tool, both counters, before-receipts, dev
  selftest 21/21 (`f6d8a891`; conformance audited clean by seat ReviewFreeze, report
  `.ufo/waves/round-33/w1/ReviewFreeze.md`).
- Wave 1 — 33 seats in one validated v1 wave (spec `.ufo/waves/round-33/spec-w1.json`, dispatch
  `dispatch-w1.json`), dispatched by the orchestrator per its mid-flight directive: 4 pre-data
  controls (all caught: do-nothing `kill=0/18`, always-pass `0/18`, always-fail `accept=0/8`,
  sha-only `accept=1/8` — reports `w1/Ctl*.md`), 9 dev sweeps (DevGuard/DevHead/DevArm/DevLoopOps/
  DevNlegs/DevMulti/DevHarness/DevStderr/DevAccept), 8 reviews/critics, 2 panel calibrations
  (v1 and v2 tools both `18/18 8/8` under four seeds), frontier source seats (S100 opened, S099
  rechecked), connector/sentinel/revenger/ledger/census seats. Zero dead seats.
- Amendments (all pre-data, no default-mode counter run occurred; artifacts
  `.ufo/evidence/round-33/contract-amendments.json`): 1 `27902a16` counter `--receipt` fix;
  2 `e6a5f4b` c2 hardening; 3+4 `49876298` tool hardening (runtime sweep under both runner
  configs; co-occurrence vectors over every position pair — 15,158 vectors x 2 configs; nesting-aware
  `run_regression` extraction with tally-block depth + postamble checks; loop identification by
  case-subject dataflow accepting renamed variables and `while`/`until`; five harness-region
  weakening faults; extraction regex quote tolerance; sandbox boundary repaired — real bwrap
  read-only runtime mounts, `timeout` outside; controls gate requires non-empty controls all
  `predicate_pass=false`; witness vectors must name 9 legs; contract kill-rule sentences);
  5 `ee398492` DevHead twice-only head rule (19/35 survivors killed, validated on all 35).
- C2 landing: S100 row (`corpus/SOURCES.md`), committed snapshot
  `.ufo/evidence/round-33/c2/doctest-snapshot.html` (216,574 B, sha256 `217edd57…4899`), fetch
  receipt, lesson Gate (`corpus/lessons/round-33.md`).
- mte-interop SETUP repair (carried queue): jsonschema 4.25.1 via uv
  (`sudo /home/vgpnk/.local/bin/uv pip install --system --break-system-packages`), selftest
  `MTE_SELFTEST: 17/17 pass` (`.ufo/evidence/round-33/repair/mte-selftest.{stdout,exit}`).

## Landed changes

- `tools/tally-audit-v2.py` — new capability tool (amendment-hardened; sha256 `7b11ba25…8d10`)
  — `f6d8a891`, amendments `49876298`, `ee398492` — LOG Round 33.
- `.ufo/evidence/round-33/` — contract, amendments, counters, before receipts, wave evidence,
  measurement receipts, snapshot, repair receipts — freeze through `61401c28` — LOG Round 33.
- `corpus/SOURCES.md` — S100 row (97 rows; census end exit 0) — `5bfa3b59` — LOG Round 33.
- `corpus/lessons/round-33.md` — Gate (S100 opened with located quote + committed digest; S099
  recheck unchanged at `b0c7e050…`; live-digest pins rejected), 4 mined mistakes, routed holds —
  `ee398492` — LOG Round 33.
- `corpus/knowledge/runner-tally-audit-v2.md` — the four round-32 classes, the v2 counters, the
  co-occurrence/driver-pin coverage lesson — `732b6860` — LOG Round 33.
- `SCORECARD.md` — round-33 block (C2 measured; C1 honest stop; mte row supersession) — `732b6860`.
- `LOG.md` — Round 33 entry — `732b6860`.
- `.ufo/waves/round-33/` — wave-1 spec, dispatch, 33 seat reports — `61401c28`.

## Before → after measurements

- **C2 (measured, improved)** — counter `python3 .ufo/evidence/round-33/c2/c2-measure.py --lane LANE --rev REV`.
  Before at base `66e1fb44`: `C2_R33: row=none versioned_url=0 snapshot_sha_ok=0 gate_sha_ok=0 quote_ok=0 C2_R33_PASS=false`, exit 1 (`.ufo/evidence/round-33/before/c2-at-base-v2.*`).
  After at `732b6860`: `C2_R33: row=S100 versioned_url=1 snapshot_sha_ok=1 gate_sha_ok=1 quote_ok=1 C2_R33_PASS=true`, exit 0 (`.ufo/evidence/round-33/after/c2-at-head.{stdout,exit}`; re-verified at `5bfa3b59` after the row move — census end exit 0).
- **C1 (not run — honest stop)** — counter `python3 .ufo/evidence/round-33/c1/c1-measure.py --lane LANE --rev REV --work EMPTY_DIR`.
  Before at base: `tool_present=0 … C1_R33_PASS=false`, exit 1 (`before/c1-at-base.stdout`).
  At head `732b6860`: `tool_present=1 tool_sha_ok=1 runner_sha_ok=1 controls_ok=0(receipt-missing) v1_kill=0/0 v1_accept=0/0 ho_kill=0/0 ho_accept=0/0 ho_invalid=0 heldout_after_freeze=0 … C1_R33_PASS=false`, exit 1 (`after/c1-at-head-notrun.{stdout,exit}`) — the structural false of a predicate whose sealed held-out set does not exist. No deciding run was consumed; the measurement (sealed set authored post-freeze + committed controls receipt + counter run) is routed to round 34 with the tool pin `7b11ba25…8d10`.
- Panel calibration (supporting, not the claim): v1 and v2 tools both `kill=18/18 accept=8/8` on the
  public panel under four seeds (`w1/PanelCheckA.md`, `w1/PanelCheckB.md`).

## Sources & frontier

Census command: `TZ=UTC bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`.
Start (seat CensusStart, `w1/CensusStart.md`): exit 0, 96 rows (A87/B7/C2; mined 68/queued 22/rejected 6), 8 known W04 duplicate-url warnings.
End (`.ufo/evidence/round-33/after/census-end.{stdout,exit}`): exit 0, 97 rows — `tameshi ok`.
Rows added: 1 — S100 (tier A, `supersedes S055 — the /3/ alias drifts; this pins the 3.15 build by committed bytes`; opened by seats SrcDoctestReopen/ReviewSrcDoctest, quote at module-intro lines 245-246, digest committed). Rows touched: none (S099 rechecked, unchanged at its pinned digest). Frontier rows advanced: S055's drift repaired by supersession; S099 recheck completed. Lesson `corpus/lessons/round-33.md` `## Gate` carries URL/access-date/quote per row.
Mined mistake: `corpus/lessons/round-33.md` `## Mistakes` x4 (counter flag shipped broken — fix amendment 1 shown able to fail by the seats' frozen-byte exit-2 receipts; docstring-only sandbox — fix shown able to fail by the frozen-boundary witness runs; the nine-seat coverage convergence; the wave-2 budget miss). The r32-origin fix (sealed set before data) remains demonstrated able to fail by round-32's own `ho_kill=1/10` receipt.

## Trend verdicts

- **expansion: improved** — knowledge entry `corpus/knowledge/runner-tally-audit-v2.md` on ground the
  coverage map did not hold (the four held-out classes + the co-occurrence/driver-pin coverage
  lesson), S100 admitted on uncovered registry ground; no frontier row retcon.
- **quality: improved** — the round's own gate rejected its counter interface, its sandbox docstring,
  and nine coverage holes before any data run (five disclosed amendments with able-to-fail
  demonstrations); S099 re-verified at its pinned digest; S055's stale pin superseded by committed
  bytes. Not scored up: no entry was superseded by a stronger one.
- **discernment: improved** — the gate rejected C1's own measurement (structural false on a missing
  fixture, kill rule preserved), rejected live-digest pins with two independent footer-drift
  observations, and kept every rejection as a lesson row; wave-1 seats (independent authors) caught
  what the L1's smoke tests missed. Non-author closure remains the verification layer.

## SHONEN

- [~] SKILL.md decision tables — lane assertion (cold-read ledger `.ufo/evidence/round-21/coldread/ledger.json`); this round's records drift sections — re-crediting routed to round 34.
- [~] End-to-end domain task — mutation sweep craft exercised pre-data (9 sweeps); the round's measured claim is freshness (C2).
- [~] Executable without oral context — lane assertion (round-21 input-keyed monitor).
- [~] No cross-domain bleed — lane assertion; connector scan reported adjacency, absorbed nothing.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Installs

jsonschema 4.25.1 (+ referencing 0.37.0, rpds-py 2026.9.1, attrs, jsonschema-specifications) via
`sudo /home/vgpnk/.local/bin/uv pip install --system --break-system-packages` — channel: uv (pacman
paused host-wide); reason: mte-interop selftest SETUP repair (carried queue).

## Round shape and seats

Default two-v1-wave shape, truncated to one wave by the 2 h freeze: wave 1 build+attack, 33 seats
(policy v1 band 32-64, validated exit 0; roles: mutation-tester 16, reviewer 8, critic 2, scout 2,
scribe 2, connector 1, sentinel 1, revenger 1; attack seats 28/33 ≈ 85%). Wave 2 (falsify + sealed
held-out authoring + cold reads, ~33 planned) not dispatched — the sealed set cannot be authored
against a tool still being hardened, and the budget was spent on nine amendment-driving findings.
Round total: 33 seats, 0 dead, 0 residual calls. The §3 L2 floor was met inside wave 1 (connector,
scribes, scouts, reviewers, critics, sentinel, revenger, executors-by-role); the L1 holds the
planner seat (validator-frozen topology); bounded planning data-walks rode LedgerAudit and
ReviewFreeze.

## Dead seats / refusals

None. All 33 seats returned.

## Open L0 questions

None new this round. (Standing: the mcp.json rea pin rewrite remains the operator's; pacman pause
stands.)

## Tooling note

The controls receipt mint (`--write-controls` over the four seat controls) hit a counter defect
(`score_tool` definition dropped during the boundary repair — restored in `5bfa3b59`) and the
attempt budget; the four seat-authored controls and their scratch receipts (each showing
`predicate_pass=false` against the frozen/amended counter) are committed as wave evidence, and the
receipt mint is first in round 34's queue. C1's kill panel and the cold-read re-crediting
(~19 SOURCES-citing sections + 3 all-four, sized by seat LedgerAudit) are routed there too,
with the v3 residue classes listed in the lesson's Holds.
