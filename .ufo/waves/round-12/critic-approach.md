# Critique — falsify the round-12 gate-integrity plan before it lands

CriticApproach (gx-critic-round12), 2026-09-28, main HEAD at attack time `6d27283`
(`git rev-parse --short HEAD`). No sibling drafts existed: `ls .ufo/waves/round-12/`
→ empty (dir absent both checks). Plan attacked as stated. Every number below was
re-executed this session; commands + observed outputs inline.

## Must-fix

**MF-1 — The checker has no defined truth precedence or keying; a naive build is
confidently wrong 15 ways.** I prototyped the obvious checker (regex `.ufo/watchdog.log`,
diff against ledger last-wins). Prototype command (throwaway, inline):

```sh
python3 - <<'PY'
import re, json
log=open('.ufo/watchdog.log').read()
comp={(l,int(r)) for l,r in re.findall(r'complete (\S+) round=(\d+)',log)}
launch={(l,int(r)) for l,r in re.findall(r'launch (\S+) round=(\d+)',log)}
state={}
for e in json.load(open('MANIFEST.json'))['rounds']:
    lr=e.get('lane_rounds',{})
    for lane,st in e.get('lanes',{}).items():
        state[(lane,lr.get(lane,e['round']))]=st
naive={k:'ok' for k in comp}
naive|={k:'in-flight' for k in launch if k not in naive}
for k,v in sorted(naive.items()):
    if state.get(k)!=v: print(k, state.get(k), '->', v)
print('no-log ledger rows:', sorted(set(state)-set(naive))[:8])
PY
```

Observed (abridged to the pattern classes, all 15 rows seen):

```text
('aggregator', 5) failed -> ok
('aggregator', 7) not-dispatched -> ok
('kagi', 1)       failed -> in-flight
('kagi', 11)      not-dispatched -> ok
('kengaku', 8)    failed -> ok
('kotoba', 12)    not-dispatched -> ok
('protocol', 11)  not-dispatched -> ok
('kengaku', 11) ('kumitate', 11) ('protocol', 12) ... -> in-flight (live, correct)
no-log ledger rows: ('aggregator',1) ('kake',1) ('kasegi',1) ('kengaku',1) ...
```

Two confidently-wrong classes: (a) `(kagi,1): failed→in-flight` — steer-era
`launch kagi round=1` 15:50:56 has no `complete` line, yet the ledger's `failed`
is *more* correct than the log; (b) `(kengaku,8): failed→ok` — the marker was
re-adjudicated; the log cannot represent that. Worse, keying legacy fleet-keyed
entries by `lane_rounds.get(lane, entry.round)` **manufactures an eternal
in-flight row `(aggregator, 9)`** from `rounds[3]` = `{round: 9, lanes:
{aggregator: in-flight}}` (no `lane_rounds`) — an aggregator round-9 that never
existed. Falsifiable claim: *a checker that trusts the log over the ledger, or
keys legacy entries naively, emits wrong rows at round 12.* Evidence:
prototype output above; `grep -c 'steer '` .ufo/watchdog.log → 15.
**Fix:** checker MUST take `closed_at` as input; treat the log as
dispatch/complete evidence only for post-fleet-2 (`609ecb6`) rows; skip rows it
cannot adjudicate (`unadjudicable`, never a status); key by `lane_rounds` when
present, ignore legacy `work` entries whose `entry.round` ≠ the lane's recorded
counter; and — PROTOCOL.md step 4 — write the timestamp+text digest of every log
line a status rests on into the entry notes (the digest, not the live log, is
the pointer that resolves at closure). Spec the keying in the script header, not
in prose.

**MF-2 — Fixture selftest alone is exactly the theater PROTOCOL.md forbids.**
PROTOCOL.md:293: "A status command printing configured values is not evidence of
capability." A selftest pinned to a synthetic fixture proves the checker's
*logic over toy inputs* — but the ledger-adjudication layer (MF-1) is where it
will actually be wrong, and a fixture cannot prove that. Falsifiable claim:
*the round-12 metric risks becoming "selftest green" while the landed entries
still carry wrong statuses.* **Fix:** ship both, committed under
`.ufo/waves/round-12/`: (a) `--selftest` on a synthetic fixture; (b) a
**freeze-run** — committed snapshots of `MANIFEST.json` + `.ufo/watchdog.log`
(as of `closed_at`) plus the checker's committed expected output for the
round-12 entries — so re-running `closure-check.py --frozen` must reproduce the
exact statuses the round-12 `rounds[]` entries carry; any later hand-edit of the
entries then contradicts the frozen run. Wire the re-run command into the M2/M8
evidence pointers so SCORECARD cites something falsifiable.

**MF-3 — The mandated `--selftest` flag name is already contradicted by a
sibling.** kotoba's gate flag is `--self-test` (hyphen) —
`kotoba-shokunin/verifiers/verify_harness_claims.py:608`: `ap.add_argument("--self-test",
action="store_true", help="check the script's model only")`. kagi prints
`DRIFT_SELFTEST` (`corpus/drift-pins.sh:398-402`: `drift-selftest: FAIL %s:
exit %s want %s`); kengaku has `run_selftest()` (grader.py:1601). A standard
mandating the literal flag `--selftest` brands kotoba nonconformant on day one
for a hyphen. **Fix:** mandate *capability* — a self-invocation mode asserting
exit code AND expected check-id with expected values pinned in-repo — not the
flag spelling; the registry records each gate's actual flag.

## Falsified claims

**F-1 — The round-12 brief's live facts were stale on arrival; the closure list
must be re-derived at execution, not copied.** HEAD moved `55e23de`→`6d27283`:
`git log --diff-filter=A --format='%h %ci %an' -- .ufo/reports/round-7/aggregator.md`
→ `6d27283 2026-09-28 20:32:43 -0300 aggregator-shokunin` — aggregator r8 landed
its predecessor's report itself at 20:32:43 (subject: "…landed by round 8: the
driver completed round 7 on report-file existence before the lane commit step
ran"), removing it from the untracked set. `wc -l .ufo/watchdog.log` → 200 (brief
said 199). `git status --porcelain` → exactly 4 untracked:
`.ufo/prompts/kotoba-round-13.md`, `.ufo/prompts/protocol-round-12.md`,
`.ufo/reports/round-11/kengaku-DRAFT.md`, `.ufo/reports/round-12/kotoba.md`.
Commit chain observed: `029c474` (kagi report, operator) → `3ea42cb` (closure) →
`6bd4f38` (compaction) → `55e23de` (scorecard/log) → `392b3c7` (protocol r11
report) → `6d27283` (aggregator r8). Falsified claim: *a durability-commit list
written from the 20:31 snapshot is correct at execution time.* It double-commits
`round-7/aggregator.md` or mislabels it. **Fix:** re-derive the
untracked/terminated sets inside the checker run at execution time; commit only
files whose mission has a `complete` line in the committed digest.

**F-2 — "The 4 in-flight rows" is keying-dependent.** Same prototype, two
tallies. Entry-keyed last-wins over `rounds[].lanes`:
`Counter({'ok': 73, 'not-dispatched': 23, 'failed': 4, 'in-flight': 4})`,
in-flight = `[(kengaku,11),(kotoba,12),(kumitate,11),(protocol,11)]` — matches
the brief and the carried rows in `rounds[19]`/`rounds[20]`
(`closed_at` 2026-09-28T20:10:00-03:00). Lane-round-keyed
(`lane_rounds.get(lane, entry.round)`): only `(aggregator, 9)` — the
manufactured row (MF-1). Falsified claim: *"the 4 in-flight rows" is a
well-defined set.* It is only well-defined under entry-keying. **Fix:** state
the keying in the checker header and in the metric definitions.

**F-3 — The plan's exit-code convention ("0/1/2 + ≥3 reserved") breaks
kumitate's working gate.** `kumitate-shokunin/scripts/round-gate.mjs:161`:
`'exit map: 0 clean · 1 findings (errors; warnings too under --strict) · 2
fail-closed · 64 usage'`. A convention that reserves 2 for "usage/setup" and
mandates no other codes brands kumitate's 64 a violation — while the lane is
mid-edit on that file (`git -C kumitate-shokunin status --porcelain -- scripts/`
→ ` M scripts/round-gate.mjs` + `?? scripts/proxy-check.mjs`). **Fix:** see W-1
counter-proposal.

## Wrong-move risk

**W-1 — Mandating a uniform map imposes work on six lanes that never agreed, and
closure cannot enforce verdicts.** Writing the ruling is in scope: PROTOCOL.md
§Fleet-2 conventions, precedence bullet — "`PROTOCOL.md` owns process, evidence,
and gates." But *enforcing* it at closure means re-running sibling code, which
step 1 never required — and a re-run can disagree with a gate's own verdict for
environment reasons (kotoba exit 2 is literally "Environment cannot answer the
question", verify_harness_claims.py:506). The strongest rejected alternative
(fleet-wide 0/1/2 map) buys uniformity at the cost of retro-breaking two working
gates. **Concrete counter-proposal:** the standard = *verdict classes*, not
codes — `0 clean / 1 findings / ≥2 gate-defined but every non-zero class
documented in-repo and pinned in the registry` — plus a per-repo registry row
(gate path, exit map, selftest flag, pinned-expected path). Convergence toward a
uniform map becomes a direction lanes migrate on their own rounds; the
integrator's closure check is structural (registry row exists, expected file
committed), never a verdict re-run. This keeps kotoba's exit 3 (documented at
`kotoba-shokunin/corpus/knowledge/harness-verifier-round10.md:15,181`: "exit 0
agree / 1 drift / 2 environment unreadable / 3 no [baseline]"; "baseline deleted
| exit 3, observations printed") and kumitate's 64 conformant, and turns the
reservation clause from a loophole ("any new code grabs ≥3 forever") into a
falsifiable standard (a class is real iff the pinned file proving it is
committed).

**W-2 — Durability commits racing live lanes.** kotoba r13 (launched 20:28:23,
log line observed) re-filed its predecessor's report last round under lane
identity (`f9dcfd2` precedent, round-11 report §Conformance 8). If protocol
commits `.ufo/reports/round-12/kotoba.md` while kotoba r13 is live and about to
commit the same path, kotoba's own commit becomes empty or divergent. The plan's
terminated-only rule is right; execution must check termination *at commit time*
from the digest, not from a plan-time list (F-1). Committing another lane's
report stays an attribution defect to record — it does not violate "landed by
the lane" (PROTOCOL.md:96): the appendix already rules "A swept report is still
landed — history is never rewritten to fix attribution." What it must not do is
pre-empt a live lane's self-commit.

**W-3 — Pareto risk is real: this is three moves wearing one coat.** Closure
pass + checker = gate-integrity (M2/M8 re-runs — direct). Gate-standard ruling =
protocol-soundness territory *and* touches six lanes' debt queues. P4 tracks
PROTOCOL.md length (446 lines, SCORECARD.md M/P table; `wc -l PROTOCOL.md` → 446)
and P6 is a 93-predicate preservation census (`sh
.ufo/waves/round-11/verify-census.sh PROTOCOL.md`). A new section must re-pass
both or the move regresses protocol-soundness while claiming gate-integrity.
**Fix:** (a) two commits — closure+checker first, gate ruling second — so a
revert is surgical; (b) keep the ruling ≤ ~20 net lines (compact section, or
fold into §Evidence standard's Drift-pins neighborhood + one file-contract
registry line), disclose the byte delta like round-11 did; (c) re-run
`verify-census.sh` after landing and cite the count.

## Cheaper alternative

The closure pass needs **no** PROTOCOL.md change: steps 1–4 already mandate
everything; the checker is an accelerator, not a rule. Cheapest sufficient
version: commit `closure-check.py` + frozen snapshot + expected output under
`.ufo/waves/round-12/` (round-11 committed `verify-census.sh` there — precedent),
run it, cite it in M2/M8 — zero protocol lines spent. For the gate question, the
~20-line registry-class ruling (W-1) replaces the planned fleet-wide mandate and
answers kengaku r10 without a retrofit. Only genuine loss vs. the plan: no
`## Gate standard` heading to cite — the file-contract registry row plus the
evidence-standard paragraph carry the same normative content for less surface.
Take the cheap form unless the operator wants the heading for discoverability.

## Gaps

- kengaku `grader.py` exit-2 semantics (lines 281/1635) not fully read; if 2
  means findings there, the class-map still holds, but kengaku's registry-row
  values are unverified this session.
- kagi `corpus/transcript-scan.sh` exit map not opened (only `drift-pins.sh`);
  its registry values are inferred from
  `kengaku-shokunin/corpus/evidence/round10-fleet/r10-connector.md`, not
  re-executed.
- Whether kotoba r13 will re-commit `round-12/kotoba.md` is unknowable before
  termination; W-2 is a contingency, not an observed race.
- The 93-predicate census was not re-run here (no PROTOCOL.md edit exists yet);
  the ≤20-line budget in W-3 is a design constraint, not a measured post-state.
- Sibling drafts: `ls .ufo/waves/round-12/` checked twice, empty both times; any
  draft landing after this read is unattacked.

DESPAWN: gx-critic-round12 — signal delivered. Send me shutdown_request.
