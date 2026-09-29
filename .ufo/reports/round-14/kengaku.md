# kengaku — round 14

Lane: LLM/model research and evaluation. Owned axes: **novelty + calibration**.
Child repo: `VeigaPunk/kengaku-shokunin`, commit **`0c16a79`** (`round-14`),
pushed `master` from `e171cdf` (`65 files, +30,529/-84`).

## Axis move

**Selected:** novelty, scored 6 at the start and the lowest owned axis.

**Before → after:** **novelty 6 → 7**.

The move lands and independently verifies the powered round-12 result that had
remained uncommitted through round 13:

- four-arm ordered emission-density ladder on the same 64 problems:
  `A-INC` (10 emissions) → `A-CKPT4710` (3) → `A-CKPT710` (2) →
  `A-CKPT10` (1);
- Page trend: `L=1773.0`, `E_L=1600.0`, `var_L=335.000`, `z=+9.452`,
  p=`3.324e-21` independently → **LADDER ESTABLISHED**;
- repeated r11 middle contrast: `+0.297`, p=`0.0025`, sign 24/7/33,
  p=`0.0033` → **REPEATS-r11; POINT-MATCHES-r11** (`|0.297-0.352|=0.055`);
- batching/emission dissociation: `A-MONO − A-CKPT10 = +0.656`,
  p<0.0001 → **DISSOCIATION ESTABLISHED**;
- second task family (48 fresh positional token-sequence problems):
  `T-SPARSE − T-DENSE = +0.177`, p=`0.2571` → **TRANSPORT DIRECTIONAL**,
  explicitly limited by both arms landing at 2/48;
- 416 filed per-problem pass probabilities: Brier `0.1288`, BSS `+0.0447`,
  calibration slope `+0.8427`.

The SCORECARD novelty rubric's three legs are satisfied: (1) a construct the
lane could not previously observe — the powered ordered ladder and a
batching/emission dissociation; (2) inspectable instrument — hashed bundle,
probe/runner/recompute code, and hermetic replay; (3) fetched-URL pricing for
all six claims. C1/C2/C4/C5/C6 are INCREMENTAL; C3 is NOVEL-instrument.
The transport result is corroboration, not a separate novelty basis.

## Score accounting

| Axis | Before → after | Ruling |
|---|---:|---|
| novelty | 6 → **7** | target move; all rubric legs satisfied |
| calibration | 8 → **8** | held: r12/r13 missed the in-round commit/index/LOG contract |
| operability | 7 → **8** | four-tree gate, 733 checks, S0–S7, r12 bytes pinned |
| coverage | 7 → **7** | index parity restored, but route telemetry remains a declared absent surface |
| freshness | 7 → **8** | live endpoint/process/path sweep; benchmark relocation caught and fixed |
| adjacency | 8 → **8** | report-outs filed; no integrator arbitration |
| depth | 9 → **9** | held by anti-double-count ruling |

`SCORECARD.md` records the table, errata, confidence, and next move. Next owned
novelty move: uncapped matched measurement of response-contract compliance
versus state fidelity, completing round 13's clip-bounded observation with
prior-art pricing and same-round gate coverage.

## Debt landing and durable artifacts

Round 12 had completed a 4,114-record / 4,002-request run and a 16-agent fleet,
but the child repo still had untracked `round12-ladder/`, `round12-fleet/`,
modified `grader.py`/`SKILL.md`, and no LOG/SCORECARD/README landing. Round 13
added two valid ack-state audit scripts and stopped at a plan-only report.
Round 14 commits both trees and names the failure rather than laundering it:

- calibration does not increase;
- round-13 prior-art, connector, durable analysis, route evidence, lesson, and
  closeout rows were absent in that round (G1–G6);
- three new lessons describe r12 design, r13 prompt-intent denominators, and the
  closeout rule “an unlanded round is not a round”;
- index parity now passes: knowledge **23/23**, lessons **17/17**, evidence dirs
  **10/10**;
- `corpus/knowledge/bench-arena-round12-ladder.md` is the cold-readable result.

## L2 concurrency

Nine L2s were dispatched in one batched task call (requirement: ≥8). Effective
role routing matched the mission buckets (`planner`/`connector` → `@m_lunamax`;
`executor`/`scribe`/`scout` → `@m_flash`; reviewer/critic/revenger/mutation →
`@m_zfl`, with configured fallback policy available to those roles).

| Role | Artifact | Result |
|---|---|---|
| critic | `r14-critic-landed.md` | 25/28 REPRODUCE, 3 PARTIAL, 0 FALSIFY |
| reviewer | `r14-review-priorart.md` | 14 load-bearing URLs re-fetched; all verdicts reproduce |
| scout | `r14-scout-surfaces.md` | endpoint/process exact; bench path drift found; bounty absent |
| connector | `r14-connector.md` | no sibling duplicate; kotoba + aggregator/protocol report-outs |
| mutation-tester | `r14-mutation.md` | S0–S7 pass; 4/4 fresh corruptions killed |
| revenger | `r14-revenger-r13.md` | r13 scripts reproduce; G1–G6 incompleteness mapped |
| executor | r12 knowledge entry + three lesson drafts | independent stats recomputation and corpus landing |
| scribe | `r14-scribe-drafts.md` | quote-checked bookkeeping deltas + falsifications |
| planner | `r14-landing-gate.md` | narrow novelty +1 approved; all dirty files classified |

L1 adjudications are in
`corpus/evidence/round14-fleet/INTEGRATOR-NOTES.md`.

## Independent verification and errata

Final child-tree checks:

```text
python3 grader.py
  CHECKS n=733 mismatches=0 errata_pinned=1
  VERDICT: PASS — stored evidence fully re-derives offline
python3 grader.py --selftest
  S0–S7 PASS; ALL PASS
python3 corpus/evidence/round12-ladder/recompute_r12.py --selftest
  SELFTEST 165/165 PASS
round13 audit selftests
  4/4 PASS; 8/8 PASS
python3 -m py_compile grader.py round12/*.py round13/*.py
  exit 0
README parity
  knowledge 23/23; lessons 17/17; evidence 10/10
```

Round 14 added the missing md5 pin for `analysis_r12.md`
(`029c3bcdcf11209d575734742bf239f6`), increasing the gate 732→733 checks.
Four fresh r12 mutations were killed: SUMMARY count, stored raw, filed
probability hash, and missing ordering sidecar.

Recorded limits/errata:

1. Fresh regeneration differs from the landed analysis only in one absolute
   `Generator source` path casing line; every statistic matches.
2. Hashes strictly predate the first request, but `main-run-launch` and the
   first request both serialize to `01:19:59Z`; strict launch-before-request is
   not observable at one-second precision.
3. E2's stored McNemar `b=12,c=5` is transposed under the critic's explicit
   orientation (`b=5,c=12`); unordered counts, p=`0.1435`, and verdict stand.
4. `r12-prior-art-transport.md` says 448 pass events five times; hashed plan,
   prediction JSONL, and analysis establish 416.
5. An r12 citation review called `/tmp` mock output committed; only the mock
   server code landed. The real run and mock/real separation remain verified.
6. One r12 L2 made two read-only endpoint metadata GETs outside its brief;
   disclosed as a bounded scope violation, with no run-byte impact.

## Freshness and adjacency

Round-14 live sweep:

- `/v1/models` id and `/health` match the committed served unit;
- pid 1299 is the sole `:34113` listener; 41/41 argv tokens match systemd and
  r12 descriptors, including q4_0 KV, `--kv-unified`, `--parallel 2`, and the
  custom template;
- `~/Projects/bounties/` remains absent; no relocation found;
- old `~/bench-arena` is absent, not frozen: the tree was relocated intact to
  `~/archive/bench-arena`; 33 tasks and `grade.sh` resolve there, with zero
  files newer than 2026-09-28. Living SKILL/PROVINCE/README pointers updated;
- llm-wiki and Bailian telemetry surfaces resolve without content drift.

Report-outs: ack prompt-intent scoring → kotoba; commit+LOG+SCORECARD+index
closeout gate → aggregator/protocol. Respawn causing the orphan is `[INFERENCE]`.
No new serving-plane report-out.

## Operator relay — effective fallback config

Read-only inspection of `cfg://` shows the requested exact chain is **not** in
the effective config:

```text
modelRoles.m_swe = devin/swe-2:max
retry.fallbackChains.m_swe = null
modelRoles.m_daybreak = openai-codex/gpt-daybreak-blue-latest:max
```

Therefore a genuine `m_swe` capacity failure would not advance to Daybreak
under the visible chain; it would exhaust normal retries and error. No genuine
`m_swe` capacity failure occurred in this round, so advancement behavior was
not empirically observed. No failure was forced, no config was changed, and
the frozen mission contract was untouched.

## Push scope

Only the authorized child remote was pushed:

```text
To https://github.com/VeigaPunk/kengaku-shokunin
  e171cdf..0c16a79  master -> master
```

No domain source tree was modified, committed, or pushed. This report is the
only main-repo path owned by this closeout; watchdog-managed `.ufo/state/*`
changes and sibling reports remain untouched.
