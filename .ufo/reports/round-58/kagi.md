# kagi — round 58

Lane `kagi` (secrets & vault ops), round 58, attempt 1. Claim BASE `1b13f5dad921f8901f56d30c428f89614dd74d8a`
(the round-57 verifier spot-check tip). Lane tip after landing: `0a9b52ba12cb204d10d72bb49c478ec2f4b8f4ca`
(pushed, `ls-remote origin refs/heads/master` = the same tip).

## Work performed

Declared claims (frozen in `plans/round-58.md`, predeclaration `0085a5f7`, §Amendments A1–A5 all landed
before the recorded candidate reading):

- **C1 — calibration:** the round-57 routed record defects are resolved and re-derived from committed
  bytes by one frozen checker (eight items, `C1_ROUTED` FAIL/8-unresolved → 0, population 8, guard 1).
- **C2 — operability (capability acquisition):** an executed OpenBao ACL-policy semantics trial
  (`C2_POLICY_TRIAL` 0 → 5), five documented authorization rules on throwaway OpenBao 2.7.2 dev servers.

Work items, each with its pointer:

- **Predeclaration and freeze.** `plans/round-58.md` (`0085a5f7`), instruments `plans/round-58-c1-check.py`,
  `plans/round-58-c1.sh`, `plans/round-58-c2.sh`, `plans/round-58-controls.sh`; amendments A1–A5 in the plan.
- **The routed defects, measured at BASE then repaired.** Spot-check `corpus/lessons/round-57-verifier-spotcheck.md`
  §7 (D1–D12). Fixes: epoch-C record in `LOG.md` (appended round-57 correction entry) and
  `SCORECARD.md` (round-57 post-move header); epoch-C controls receipt regenerated over the shipped bytes
  (`.ufo/waves/round-57/controls/controls-prefreeze-epochC-final.txt`, `CONTROLS: match=15 mismatch=0`, five
  `INSTRUMENT` pins equal to the tip); S117 Gate row with URL/date/located quote plus the lesson's `source:`
  line and the row's `used-by`; the landing-117 / tip-120 registry split; the `SKILL.md` gate-registry row
  for `corpus/current-claims.py`; `corpus/current-claims.py --round` with a behavioural probe (a planted
  round-57-only disagreement must move `--round 57` and not `--round 56`); the live heading at
  §Enabling/Disabling audit devices; and `stale_basis=1 → 0` in `corpus/adjacency.tsv`.
- **The trial.** `corpus/openbao-policy-trial.sh` (sha256 `1f1eed9d…`): T1 deny-by-default and exact-path
  reach; T2 `*` only as the last character (the sibling `bars` refused); T3 `deny` outranking a broader
  allow; T4 `+` bounded to one segment; T5 same-pattern union vs highest-priority match through
  client-side introspection, which a PATH wrapper lies about (flips T5 only). Receipts
  `.ufo/waves/round-58/build/R58ExecTrial/receipt-ref-real.txt`, `…-real2.txt`, `receipt-sh1..5.txt`,
  `receipt-ref-none.txt`, `receipt-ref-wrap.txt`.
- **Sources opened this round.** S118 `https://openbao.org/docs/concepts/policies/` (200, 122498 B,
  sha256 `a55ff1a4…`), S119 `https://openbao.org/docs/commands/policy/` (200, 32520 B, sha256
  `0472f293…`), S120 `https://openbao.org/docs/api/system/policies/` (200, 47012 B, sha256 `9b13c6d9…`);
  captures `.ufo/waves/round-58/capture/`, provenance rows in `corpus/source-fetches.tsv`.
- **Entry.** `corpus/knowledge/openbao-acl-policy-semantics.md` with a `## Measured (round 58 …)` section
  carrying the receipt lines, bounds and falsifiers; `Reverify: R21-02`, `cites: S120`.
- **Gate battery (candidate tree, `.ufo/waves/round-58/final/gates.txt`):** docs CLEAN (entries=39
  row_linked=36 by_hand=3), `CLAIMS_DECLARED: CLEAN (claims=41)`, `SOURCES_CENSUS: CLEAN (rows=120 …)`,
  `RELEASE_CLOCK: CLEAN (on_release=32 bound=32 unbound=0 …)`, `SELF_COUNTS … stale=0 unlocated=0
  ambiguous=0` (two operator-routed POLICY rows unchanged), `ADJACENCY_SCOPE … stale_basis=0` with
  `breadth_drift=5` carried (host movement, named in the lesson), `CHECKLIST_RUN: BROKEN failed=7`
  (the-janitor substrate absent, `PROVINCE.md` round-18 erratum — unchanged), `CITATION_GATE: BROKEN
  (cites=4245 docs=145 unresolved=15 ephemeral=0 labeled=23)` — the one finding this round created (a
  named release-clock receipt) is fixed by creating the receipt; the remainder name files this round did
  not author (`round-30/32/33/34/35-verifier-spotcheck.md`) and one round-56 SCORECARD phrase; BASE was
  not re-measured (the scan costs ~15 min) — carried honestly, not claimed repaired.
- **Wave.** `kagi-r58-w1`, 13 seats, one v1 wave under `scripts/hyaku/ufo-wave-policy.json` (band 8–16),
  0 dead; 4 executives, 2 scouts, 2 scribes, reviewer, critic, mutation-tester, sentinel, connector
  (attack share 4/13 = 31 %, connector seats 1). The L1 held the canonical planner seat. Dispatch
  `.ufo/waves/round-58/w1-dispatch.json`, results `.ufo/waves/round-58/w1-results.json`, reports
  `.ufo/waves/round-58/w1/`. The wave changed the instrument before admission: the sentinel found T1's
  denial text (preflight 403, not the literal `permission denied`), the reviewer found the decoy coverage
  row / symlink tree / dead `--round` / one-word quote false-greens, the mutation seat found three
  survivors (S1–S3, all closed), and the critic forced the control-expectation corrections A5.
- **Inherited state.** None: the lane was clean at the BASE (`jj-lane.sh state` ahead=0 behind=0
  tracked=0 untracked=0). The fleet-root strays `f.txt` and `trail-ids.txt` predate this round and carry
  no lane/round marker; they are not this lane's misroot and were left untouched. The lane committed no
  `.ufo/prompts/` file (D10 class stays integrator-owned).

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| `corpus/current-claims.py` gains `--round` + behavioural probe; `SKILL.md` gate-registry row; the eight routed-defect repairs; `corpus/adjacency.tsv` basis re-point; `QUALITY.md` QM73–QM75 | `## Round 58` | `be8705f8b08054cfb96db8d2b70e4234c1a2992f` |
| `corpus/openbao-policy-trial.sh`, `corpus/knowledge/openbao-acl-policy-semantics.md`, S118–S120 rows + fetch rows + captures, S115–S117 `on-release` → `180d` | `## Round 58` | `be8705f8` |
| instruments `plans/round-58*`, pre-freeze controls receipt (20/20), wave evidence, `corpus/claims-declared.tsv` rows `58 C1`/`58 C2`, ledger row `R58-01`, lesson `corpus/lessons/round-58.md`, `SCORECARD.md` sections + capability row, `LOG.md`, `corpus/stamps.tsv` (146 rows) | `## Round 58` | `be8705f8` |
| round-57 correction entry (epoch C + report-order correction) | `## Round 57 correction` | `be8705f8` |
| revision-bound readings at the landed revision + the clock/census/controls records | `## Round 58` | `0a9b52ba12cb204d10d72bb49c478ec2f4b8f4ca` |

## Before → after measurements

| claim | counting command | before | after | measured at |
|---|---|---|---|---|
| C1 calibration | `bash plans/round-58-c1.sh <rev>` | `C1_ROUTED: value=FAIL population=8 i1=0 … i8=0 guard=0` (diagnostic leg `value=8 population=8`) | `C1_ROUTED: value=0 population=8 i1=1 … i8=1 guard=1` (rc 0) | base `1b13f5da` (`.ufo/waves/round-58/final/c1-base.txt`), landed `be8705f8` (`.ufo/waves/round-58/final/c1-landed.txt`) |
| C2 operability | `bash plans/round-58-c2.sh <rev>` | `C2_POLICY_TRIAL: value=0 tests=5 pass=0 shims=0 vectors=0/5 guard=0 (absent)` | `C2_POLICY_TRIAL: value=5 tests=5 pass=5 shims=5 vectors=ok/5 guard=1 (real=1 none=1 wrap=1 secret=1)` | base `1b13f5da` (`.ufo/waves/round-58/final/c2-base.txt`), landed `be8705f8` (`.ufo/waves/round-58/final/c2-landed.txt`) |

Do-nothing control: the same counters on the claim BASE (`K1-BASE` `FAIL`, `K2-BASE` `0`) — a round that
lands nothing scores the before column. Full battery `plans/round-58-controls.sh` →
`.ufo/waves/round-58/controls/controls-prefreeze.txt` `CONTROLS: match=20 mismatch=0` (two no-work, two
positive reference, ten C1 item/fail-closed controls, seven C2 trial/counter/binary/environment controls).
Kill rules: C1 K1 (any item's substance break must read >0 on the forged tree — C1-F1…F8) and K2 (an item
that reads 0 on a byte-identical BASE input is vacuous); C2 K1 (no-bao PATH must read SETUP rc2 with no
HOLDS), K2 (PATH resolution is the wrapper leg), K3 (no secret-shaped string in any receipt).

Named ceilings: C1 — eight items is a closed set read structurally, a forged authority that satisfies an
item passes, and the I6 literal scan excludes the module docstring, `--selftest` fixture bodies and
`.replace/.write/.remove` plumbing (QM75); C2 — a zero-mechanics trial that shape-keys the shim vectors
and introspects the wrapper reads 5 (the round-51/57 class, checked by receipts and the non-author
probe), one binary (2.7.2), dev-server in-memory storage, the `secret/data/…` half only, `sudo` and
`scan` unmeasured.

## Sources & frontier

- Registry **117 → 120** (S118, S119, S120; all tier A, `mined`, `180d`). Counting command:
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi`
  — start `.ufo/waves/round-58/controls/census-start.txt` `kagi ok` rc 0 (117 rows); end rc 0,
  `SOURCES_CENSUS: CLEAN (rows=120 A=116 B=2 C=2 queued=1 mined=115 rejected=4 …)` (19 standing W04
  duplicate-URL warnings, unchanged in kind).
- Rows added by tier: A +3 (`docs`), B/C/queued/rejected unchanged.
- Rows touched old→new: S115/S116/S117 `on-release` → `180d` (M58-1); S118/S119 locator cells re-pointed
  to `.ufo/waves/round-58/capture/` (byte-identical), S118 `teaches` quotes replaced by locating forms;
  S120 added; `corpus/source-fetches.tsv` +4 rows and two quote cells.
- Frontier advanced: ACL policy authorization moved from the province's refused/unmapped ground to an
  executed capability (`SCORECARD.md` §Capabilities row 58, `corpus/README.md` coverage map).
- Assimilation: none this round (the lane's claims did not need the staged `merge/kagi/` package; the
  round's expansion comes from its own opened sources). `considerthese/` was not mined this round; the
  operator-authored file list is unchanged.

## Trend verdicts

- **expansion: improved** — one admitted entry on ground the coverage map did not hold (OpenBao ACL policy
  authorization), sourced by three tier-A rows opened this round, plus a capability row whose first
  working round is 58 (`SCORECARD.md` §Capabilities; entry §Measured).
- **quality: improved** — eight routed record defects repaired and now read by a gate, an executed trial
  with five documented rules and measured bounds, and the gate battery shows no new harm (docs/claims/
  census/release-clock CLEAN, `SELF_COUNTS` stale=0). Carried, not repaired: `breadth_drift=5`,
  `CHECKLIST_RUN: BROKEN` (substrate), `CITATION_GATE` unresolved legacy findings.
- **discernment: improved** — the round's own attacks changed the instrument before admission (sentinel:
  the 403 preflight text; reviewer: decoy row, symlink tree, dead flag, one-word quote; mutation seat:
  three survivors closed; critic: control expectations corrected in A5), and three new criteria
  (QM73–QM75) each cite the mistake that produced them. The outside judgment is the non-author closure
  of this round; this report does not assert it.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence:
  `SKILL.md` §Vault-ops decision table, §Failure table, §Credential-hygiene checklist, and the new
  §Gate registry — round-58 additions; `bash corpus/claim-ledger.sh citations` runs over this tree.
- [~] At least one end-to-end domain task executed and logged — evidence: `LOG.md` §Round 58:
  `corpus/openbao-policy-trial.sh` on throwaway OpenBao 2.7.2 dev servers, receipts
  `.ufo/waves/round-58/build/R58ExecTrial/`, landed reading `C2_POLICY_TRIAL: value=5`.
- [~] Instructions executable by an agent without oral context — evidence: `plans/round-58.md` with the
  frozen predicates and A1–A5; `plans/round-58-controls.sh` (20 MATCH); `--selftest` 18 cases;
  `bash plans/round-58-c2.sh <rev>` re-runnable from a clean checkout.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` §Deliberate refusals
  unchanged (vault-side structure still unmapped); the connector sweep found no sibling claiming ACL
  policy ground; the `~/.config/opencode` ownership question stays reported, not ruled.

## Lane status

- Stale-lane: respawn-per-round driver; no other mission of this lane is open. This round ran
  `launch kagi round=58` 11:54:48 −03:00 and completed after the report lands.
- Tool installs: none this round (no pacman transaction attempted; `bao` 2.7.2 and `sops`/`age-keygen`
  were already in `~/.local/bin`).
- L0 questions: none added; no operator decision was needed.
- Points for the operator: (a) `ADJACENCY_SCOPE` breadth pins drifted with host state (5 counts,
  `breadth_ok=0`) — carried, needs a reviewed breadth re-pin round; (b) `CITATION_GATE` carries 15
  unresolved references, most in integrator-authored spot-check files this lane may not edit;
  (c) the round-57 `plans/round-57-c1-check.py` docstring defect (D8) stays an erratum because its bytes
  are frozen.
