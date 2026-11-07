# kagi — round 59 (secrets & vault ops)

Lane: kagi. Round 59, attempt 1. Claim BASE `5fa6e658f36bd9e440cb567fbbd2bfac88f868b6`
(round-58 spot-check tip). Predeclaration `af7b6651` (frozen plan `plans/round-59.md`,
§Amendments A1–A4, each landed before the recorded candidate reading). Census start:
`kagi ok` rc 0, 120 rows. Axes at BASE: all six at 9.

Round shape: ONE v1 wave, 14 seats (`.ufo/waves/round-59/w1-dispatch.json`, band 8–16;
`ufo-swarm-wave.mjs` rc 0, counts `spawn=14`), attack share 4/14 = 29 %.

## Work performed

Declared claims (1–3, distinct axes, each with its own before→after):

- **C1 (calibration)** — the five round-58 routed record defects (spot-check D1–D5) become an
  audited item set; `C1_ROUTED` FAIL (diagnostic 5/5) → 0, population 5.
- **C2 (operability, capability acquisition)** — an executed OpenBao **transit-engine** trial with
  a clean-room leg; `C2_TRANSIT_TRIAL` 0 → 5.

Work items:

- **Predeclaration and shape.** `plans/round-59.md` (frozen predicate, item conditions, kill
  rules, ceilings) committed alone at `af7b6651`; A1 corrected the seat count 13 → 14 and the
  frozen-topology role (`planner`/`labrat` are refused by the wave validator — refusal reproduced
  at `.ufo/waves/round-59/build/KagiR59/validator-refusal.txt`), A2 fixed the trial's printed
  contract, A3 the reading of the forgery controls, A4 the control composition, the wrapper
  entry command, T5's enforced `derived: true` prerequisite and the C2 absent-leg exit code.
- **C2 instrument.** `corpus/openbao-transit-trial.sh` (355 lines) starts one throwaway
  `bao server -dev` on 127.0.0.1 under `setpriv --pdeathsig KILL`, resolves `bao` through PATH
  only, and measures T1–T5 plus the clean-room leg. Real run (receipt
  `.ufo/waves/round-59/build/R59ExecTrial/receipt-ref-real.txt`):
  `OPENBAO_TRANSIT_TRIAL: HOLDS holds=5 broken=0 error=0 bao=v2.7.2` and
  `TRIAL CLEANROOM HOLDS own-storage-refused=1`.
- **C1 instruments.** `plans/round-59-c1-check.py` (33-case `--selftest`), `plans/round-59-c1.sh`
  (driver, materialises the measured tree, refuses a challenge copy inside it — QM74),
  `plans/round-59-c2.sh` (counter: two real runs, five shim vectors, no-bao leg, clean-room
  requirement, secret scan, `env -i` legs).
- **Record repairs.** An append-only `## Correction (round 59)` block in `corpus/lessons/round-58.md`
  carrying D1 (registry `117 → 120`), D2 (`source-fetches.tsv` +6 rows), D3 (control census
  20 = 9 C1 + 7 C2, and the two never-shipped controls), D4 (the committed post-fix citation
  reading), D5 (101-minute mission, `progressing`) — every number derived by the checker from
  `git show 1b13f5da…` / `git show be8705f8…` and the named receipts.
- **The two controls round 58 documented and never shipped.** `plans/round-58-controls-supplement.sh`
  ships `C1-F10` (printer-stub challenge) and `C2-F4` (single-run trial); its receipt
  `.ufo/waves/round-59/final/supplement-receipt.txt` ends `SUPPLEMENT: match=2 mismatch=0`.
- **Sources and entry.** S121 (`https://openbao.org/docs/secrets/transit/`) and S122
  (`https://openbao.org/docs/api/secret/transit/`) opened live 2026-11-07 with a desktop browser
  agent, captured at `.ufo/waves/round-59/capture/` (48604 B / 267984 B, sha256 in the rows),
  quotes located by `corpus/rendered-text-v1.py`; entry `corpus/knowledge/openbao-transit-engine.md`
  (measured table, docs-vs-binary rows, the scout's G1–G10 page gaps, bounds, falsifiers),
  `Reverify: R21-02`, stamp row, `DOC_AUDIT: CLEAN (entries=40 row_linked=37 by_hand=3 …)`.
- **Pre-freeze battery.** `plans/round-59-controls.sh`, 20 controls, final receipt
  `.ufo/waves/round-59/controls/controls-prefreeze.txt` reads
  `CONTROLS: match=20 mismatch=0` (rc 0) over the shipped instrument bytes.
- **Seat evidence.** The wave's attack seats drove real repairs: the critic found the C2 counter's
  absent-leg exit code and the two text-only items; the mutation-tester found the I5 existential
  predicate; the reviewer measured the wrapped-bullet class that made three items read false-red.

### Wave seats

14 seats, 14 reports in `.ufo/waves/round-59/w1/`, no dead seat (`w1-results.json`, `seats: 14`);
the results file carries no per-seat `status` field (QM47 defect, routed — the seats' own
`SEAT-STATUS:` lines are in their reports: 27 report files carry `SEAT-STATUS: complete`, none
carries `partial` at the tip).

### Attack findings and what happened to them

- **critic** (`build/R59CriticClaims/critique.md`): the C2 counter's absent-trial leg exited 0
  against the frozen `exit 0 iff value=5` — fixed in the instrument (A4); `C1_ROUTED value=0` is
  reachable by five right-looking lines and `I4` accepts any `unresolved=` — stated as ceilings in
  the SCORECARD row and the lesson, never as "repaired"; D2's defective line lives in the fleet
  report the lane may not edit — restated with the derived delta (6).
- **mutation-tester** (`build/R59MutCounters/mutants.md`): 8 mutants killed, **10 survived** on the
  frozen battery — the counter's `pass` counting, its secret scan, its `real2` conjunct, its
  no-bao leg and its clean-room independence are not guarded by any control (N02–N05, N08), and
  three checker mutants (missing-line default, in-place challenge copy, I3 total-only) walk past
  every control. This is a routed defect of the *battery*, not of the claims: no survivor changes a
  claim reading, and each is named in `corpus/lessons/round-59.md` §Routed dispositions.
- **reviewer** (`build/R59ReviewerCounters/attacks.md`): measured the wrapped-bullet class (M59-1)
  that made three items read false-red, and an independent 12-item attack grid.
- **sentinel** (`build/R59SentinelTrial/audit.md`): seven security checks CLEAN (secret shapes, cookie
  hygiene, `strace` argv hygiene over 3103 execve lines, server confinement with a SIGKILL orphan
  probe, ambient `BAO_*`/`VAULT_*`, scratch confinement, no key material on disk).
- **connector** (`build/R59ConnectorSiblings/sweep.md`): no sibling holds transit-engine ground or the
  supplement-controls pattern; the shokuknow `merge/kagi/` package stages no transit material.
- **revenger** (`build/R59LabratContext/probe.md`): a convergent key refuses a context-free rewrap and
  a wrong context fails the MAC — absorbed as R1/R2 in the lesson.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| frozen plan `plans/round-59.md` (predicate, items, kill rules, ceilings) | §Round 59 | `af7b6651` |
| instruments, record repairs, supplement, entry, rows S121/S122, gates, SCORECARD/LOG, lessons | §Round 59 | `a0c77ecdb7deeedaa01232e040089982b569489c` |
| the 20-control receipt, the wave evidence tree, the scoped citation receipt, candidate readings | §Round 59 | `160caf750dcf15892b78ec066e66bc605ba57a5c` |
| revision-bound readings at the landed tip + the wave results file | §Round 59 | `75165a07b1b55a96ddf03fc71449211455d968ee` |

## Before → after measurements

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| C1 calibration | `C1_ROUTED: value=FAIL` (diagnostic `value=5 population=5`, guard=0) | `C1_ROUTED: value=0 population=5 i1=1 i2=1 i3=1 i4=1 i5=1 guard=1` (rc 0) | `bash plans/round-59-c1.sh <rev>` / `python3 -I -B plans/round-59-c1-check.py --root . --repo . --no-challenge` | `75165a07` (re-read at the landed tip: `.ufo/waves/round-59/final/c1-landed.txt`) |
| C2 operability | `C2_TRANSIT_TRIAL: value=0 … (absent)` | `C2_TRANSIT_TRIAL: value=5 tests=5 pass=5 shims=5 vectors=ok/5 guard=1` | `bash plans/round-59-c2.sh <rev>` | `75165a07` (`.ufo/waves/round-59/final/c2-landed.txt`) |

## Sources & frontier

SOURCES: 120 → 122 rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
⇒ 120 at BASE, 122 at the tip); census before `kagi ok` rc 0 at 120 rows
(`.ufo/waves/round-59/controls/census-start.txt`), after `kagi ok` rc 0 at 122 rows.
Rows added: **S121, S122** (both tier A, `mined`, `180d`, `used-by`
`corpus/knowledge/openbao-transit-engine.md`), each with a fetch-provenance row
(`corpus/source-fetches.tsv`) bound to its capture body digest and byte count.
Rows touched old→new: none (no existing cell changed; `recheck` of the new rows is `180d`, so the
release-clock gate reads `CLEAN (on_release=32 bound=32 unbound=0 …)`).
Frontier rows advanced: the transit engine moved from an empty surface
(`grep -rl transit corpus/knowledge/` matched no executed mechanic) to an executed capability with
one entry, five measured mechanics and a documented-vs-measured split (the scout's G1–G10).
Assimilation: none — the shokuknow `merge/kagi/` package's staged themes (Alibaba RAM custody)
were assimilated in an earlier round and hold no transit material (connector sweep,
`.ufo/waves/round-59/build/R59ConnectorSiblings/sweep.md`). considerthese: the latest file
(2026-10-26) has one still-unimplemented proposal (a `BACKLOG.md` status table); it is recorded as
not mined this round because it would add an unread surface, and the round's claims are the
routed-defect set.

## Trend verdicts

- **expansion: improved** — a registry delta of two admitted rows and one executed entry on ground
  the coverage map did not hold (transit engine), plus a coverage-map row.
- **quality: improved** — the five routed defects now read true against derived numbers; the stale
  C2 exit encoding is fixed; two never-shipped controls ship and run; the entry states its measured
  limits and the page gaps behind every measured leg.
- **discernment: improved** — the wave's attack seats changed the instruments before admission
  (critic: absent-leg exit code, text-only items; mutation-tester: the I5 existential predicate;
  reviewer: the wrapped-bullet class; sentinel: seven CLEAN security checks including argv/strace
  and orphan-process probes), and each finding is routed in the lesson.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  Evidence: SKILL.md §Vault-ops decision table, §Failure table, §Credential-hygiene checklist, and the
  new `## Gate registry — round-59 additions` rows for the routed-record item set and the transit trial.
- [~] At least one end-to-end domain task executed and logged in LOG.md
  Evidence: LOG.md §Round 59 — the transit trial runs five mechanics plus the clean-room leg on
  throwaway OpenBao 2.7.2 dev servers (`OPENBAO_TRANSIT_TRIAL: HOLDS holds=5 broken=0 error=0`);
  LOG.md §Round 3 remains the credential-delivery end-to-end record.
- [~] Instructions executable by an agent without oral context
  Evidence: `corpus/lessons/round-19-recensus.md` §Independent audit erratum (runnable gates green);
  round 59 adds `plans/round-59-c1.sh --tree DIR`, `plans/round-59-c2.sh --tree DIR`,
  `plans/round-59-controls.sh` (20 controls) and `plans/round-58-controls-supplement.sh` — each a
  one-command verdict with its receipt.
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  Evidence: `PROVINCE.md` §Surfaces + `corpus/scope-gate.sh` (`stale_basis=0`; the carried
  `breadth_drift=5 breadth_unverified=1` named, not absorbed); the round's connector sweep found no
  sibling holding transit-engine ground and absorbed nothing.
- No box is marked `[x]`: every pointer above is lane-authored and no named non-author verifier has
  checked them this round (promotion is operator-owned).

## Lane status

Stale-lane: `progressing`. Lane commits inside the mission window; launch
2026-11-07T13:49:28-03:00 (`.ufo/watchdog.log`), landing `2026-11-07 lane tip `75165a07``.

## L0

No new operator decision is required. Carried: the three operator-routed reds R25-02, R29-01,
R29-02 and R38-03 stay red (untouched this round).
