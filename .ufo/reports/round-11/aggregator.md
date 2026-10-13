# aggregator round 11 — mint/dormancy axis-move: first mint counted, probation + 8-lane dormancy

**Stamp.** Aggregator lane round 11 (`.ufo/state/aggregator.round` = 11; runId
`shokunin-r11-aggregator-r1790651969`). Measurements ran against main HEAD
`8afbc8f` during **2026-09-29T03:26:00Z–03:38:20Z**. While this report was
staged, the concurrent kengaku lane moved main HEAD to `896660a` and committed
the already-generated round-11 dispatch prompt; it did not sweep this lane's
report, ledger, scorecard, log, or wave. This report ships in the `round-11`
commit and therefore cannot cite its own hash.

## Result

Axis: **mint/dormancy calls, 8 → 9**.

The first fleet mint is now counted by the lifecycle discriminator rather than
an empty compatibility field:

```sh
python3 -c "import json;r=json.load(open('MANIFEST.json'))['rounds'];\
print(len(r),sum(e.get('type')=='mint' for e in r),\
sum('minted' in e for e in r),sum(bool(e.get('minted')) for e in r))"
# 48 1 35 0
```

`MANIFEST.json` `rounds[36]` is the kama probation mint, landed by `2d19a64`.
The six-id roster is intentionally unchanged: `PROTOCOL.md` requires at least
three verified self-iteration rounds before the roster/ROADMAP graduation.
Kama has r1 completed and r2 live.

Dormancy coverage moved **7 → 8 rows**. All rows were re-run with each repo's
actual LOG grammar; failed marker reports were excluded:

| Lane | Evaluated rounds | Verdict |
|---|---|---|
| kasegi | r17 + r15 (r16 marker excluded) | ACTIVE |
| kengaku | r13 + r11 | ACTIVE — watch; r13 has no LOG entry |
| kake | r16 + r15 | ACTIVE |
| kumitate | r16 + r15 | ACTIVE |
| kotoba | r16 + r14 (r15 marker excluded) | ACTIVE — watch; r14 has no LOG entry |
| kagi | r16 + r15 | ACTIVE |
| kama | no pair; only r1 completed/reported | ACTIVE — insufficient history |
| aggregator | r9 + r8 (r10 marker excluded) | ACTIVE |

**0 / 8 dormant.** Kengaku is the first near-positive; it is one missing LOG
entry short of the literal two-reported-round trigger. Kama cannot satisfy the
trigger with one completed reported round.

## Before → after

| Metric | Before | After |
|---|---:|---:|
| lifecycle-aware mint count | 0 pre-mint; predicate incapable of turning positive | **1** (`type:"mint"`, kama) |
| kama state | candidate / blocked-external | **minted-in-probation** |
| current dormancy rows | 7 / 7 | **8 / 8** |
| rows using the repo's actual LOG grammar | unmeasured | **8 / 8** |
| current candidate calls | four after kama graduation | **five**: four below bar + filesystem-custody WATCH |
| durable L2 seats | 0 / 12 | **12 / 12** |

The older zero-mint values remain valid at their cutoffs: kama was minted
after them. The repaired defect is the predicate, exposed by the first mint.

## Candidate calls

- **kama:** graduated to probation; two more verified rounds required before
  roster promotion.
- **kessho:** below bar; verification builders increased, but 0 unplaceable
  demand instances.
- **umihotaru:** below bar; watchdog/pane work is integrator-owned.
- **kagemusha:** below bar; D-86 is ruled and the work remains distributed
  across served provinces.
- **axis-framework stewardship:** below bar; protocol/operator work, not a
  domain.
- **filesystem custody / vanished-root forensics:** WATCH, not mint-eligible.
  Six observations are one correlated prune regime, not two independent
  unplaceable demands; operator ownership remains unresolved.

## Corpus standing duty

This was not the axis move. The existing committed gate was still executed:

```text
selftest 12/12 PASS
kasegi   b021dc9 dirty=31 exit=1 findings=55
kengaku  e171cdf dirty=13 exit=1 findings=30
kake     ab87a48 dirty=10 exit=1 findings=45
kumitate f9f8e4d dirty=6  exit=1 findings=55
kotoba   d85982d dirty=0  exit=1 findings=82
kagi     8a6ec16 dirty=0  exit=1 findings=60
```

All six remain **not conformant** at the revisions shown. Kama's first corpus
verdict is also **not conformant** at `c6199a2`: the required layout exists,
but 3/5 lessons have neither a commit hash nor a report pointer.

## L2 wave — 12 seats, one batched call

| Role | Seat | Durable artifact |
|---|---|---|
| scout | DormancyScout | `seats/dormancy-table.md` |
| scout | MintScout | `seats/mint-table.md` |
| scout | CorpusSweepScout | `seats/corpus-sweep.md` |
| scout | L0Scout | `seats/l0-forensics.md` |
| scout | CorpusCurrency | `seats/corpus-currency.md` |
| executor | LedgerExec | `seats/exec-ledger-draft.md` |
| critic | MoveCritic | `seats/critic.md` |
| connector | OverlapConnector | `seats/connector.md` |
| reviewer | VerifyReviewer | `seats/reviewer-verify.md` |
| sentinel | FleetSentinel | `seats/sentinel.md` |
| distiller | QueueDistiller | `seats/distiller-queue.md` |
| revenger | EventRevenger | `seats/revenger.md` |

Wave total: **12 files / 2,449 lines / 262,860 bytes** under
`.ufo/waves/aggregator-r11/seats/`.

Critic amendments absorbed before landing:

1. “No mint record” was false: `rounds[36]` is the record; the defect is the
   census predicate.
2. Kama's roster absence is required probation, not drift.
3. A heading-only LOG scan is invalid for six of seven child repos; per-repo
   grammars reproduce the 0/8 verdict.
4. Fleet-wrap lines repeat; only the 00:19:33 `complete kama round=1` line is
   completion evidence.

## Cross-lane quality findings routed

Queue before this round: 160 rows / 146 distinct keys / max D-150. Added:

- **D-151:** latent mint-census predicate defect.
- **D-152:** `.gitignore` omits `kama-shokunin/`; `17c1fad` staged the exact
  predicted embedded gitlink, reverted by `8afbc8f` 13 seconds later.
- **D-153:** fleet closeout overwrote kotoba's real r15 report: 14,715 bytes at
  `4419fb9` became a 273-byte marker at the canonical path.
- **D-154:** effective `m_swe` fallback chain does not contain Daybreak.
- **D-155:** ROADMAP still says the kama mint decision is pending.

D-40 is answered by the mint event. D-143 worsened: the latest MANIFEST
`closed_at` remains 22:23 -03; the L1 counted 17 distinct later `complete`
lane-rounds, including kama r1.

## L0 surfacing

Current worktree: 20 lines = 19 content + 1 blank. Content-keyed history:
**15 open / 3 superseded / 1 answered-by-event / 0 operator-answer markers**.
The uncommitted kake r17 line is reported here but is not swept into this
commit.

## Operator relay — effective model fallback

The requested chain is **not visible**:

- `modelRoles.m_swe = devin/swe-2:max`
- `retry.fallbackChains.m_swe = null`
- Daybreak is configured for `slow`, `plan`, and `advisor`, not as m_swe's
  fallback.

The active model identifier is Daybreak, but no capacity-failure/reroute
telemetry proves advancement from m_swe. No genuine m_swe capacity failure
occurred, no failure was forced, and the frozen contract was not altered.

## Self-defects

- **27:** the mint census used a field, not the recognized lifecycle event.
  Prior values were time-correct; the predicate could never observe the first
  mint.
- **28:** the round seed turned that bug into the stronger false premise “no
  ledger record”; critic/reviewer found `rounds[36]` before publication.
- **29:** the current-wave dormancy seed assumed one LOG grammar; six of seven
  child repos use another. Corrected before grading.

## SHONEN

The main repo has no `SHONEN.md`; these are report-local author assessments:

- `[~]` **Decision tables / error patterns / cited sources:** ledger §15 has
  lifecycle, dormancy, candidate, corpus, L0, and routing decisions with
  runnable evidence; no lane `SKILL.md` exists.
- `[~]` **End-to-end domain task executed and logged:** 12-seat wave,
  lifecycle census, 8-row dormancy run, corpus gate, ledger/scorecard/log/report.
- `[~]` **Instructions executable without oral context:** seat artifacts carry
  exact commands; the L1 independently re-ran load-bearing cells.
- `[~]` **No cross-domain bleed:** only main-repo aggregator paths and wave
  evidence changed; no child repo or domain source tree was edited or pushed.

All marks remain `[~]`: every verifier in this wave was dispatched by this
lane and therefore is not an independent non-author verifier.

## Compliance and verification

Planned commit paths are limited to:

- `.ufo/reports/AGGREGATE.md`
- `.ufo/reports/round-11/aggregator.md`
- `.ufo/waves/aggregator-r11/**`
- `SCORECARD.md`
- `LOG.md`

The dispatch prompt is already durable at `896660a`; it is not re-staged by
this lane.

Not committed: live `.ufo/state/**`, `.ufo/watchdog.log`, `.ufo/l0-questions.md`,
other lanes' prompts/waves, `kama-shokunin/`, or any child/domain repo bytes.

Observed checks:

- `node .ufo/waves/round-9/corpus-gate.mjs --selftest` → **12/12 PASS**.
- `node .ufo/waves/round-9/corpus-gate.mjs --all` → exit 1 with six explicit
  not-conformant summaries (expected verdict, not a test failure).
- mint census → **48 entries / 1 type-mint / 35 minted keys / 0 truthy arrays**.
- dormancy table → **8 rows / 0 dormant**.
- report overwrite → **14,715 B → 273 B**.
- queue before append → **160 rows / 146 distinct / max D-150**.

## Next

Round 12: **cross-lane quality** (8, now the lowest). Re-run the six box-3
verdicts after rounds 14–17 and add canonical report durability to the grade.
Falsified if an overwritten marker remains a current report or any verdict
lacks the revision it measured.
