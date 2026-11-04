# kumitate — round 87 report (hyaku run 15, attempt 1)

Lane `kumitate-shokunin`, axes **operability + coverage**. Base `db97929212bb61ae970b10abac3cc4cd976713ae`;
freeze `25a3a75df123a59c5cf0de944a6d2f067e278f82`; measured revision M = `d3f64dc43027a9754700e70129b6ba91deaada19`;
lane tip at report time `71efd992093161b872a8989c957253bc9427e076` (`ls-remote origin refs/heads/master` prints it).

## Work performed

**Declared claim (1): C1 operability — capability acquisition `receipt-bind`.** The lane must be able to
bind a close receipt to the instrument its own `cmd=` names, at a judged revision. It is the lowest
non-retired axis (9; every coverage sub-axis is saturated at 10), and a second operability claim would
be one claim under `AXES.md`, so the round declares one claim and spends the remaining seats on the
routed defects R86-D1–D4, the spot-check adoption and the frontier step.

- **C1 predicate, frozen before data.** `node .ufo/waves/round-87/probe/probe87-c1.mjs --lane <LANE>
  --work <SCRATCH> --rev <REV>` → `C87_C1: HELD held=12/12` exit 0. Twelve arms: usage, selftest,
  detection on the committed round-86 receipts, the round-87 receipts, four same-directory fixtures
  (filename unchanged, `cmd=` or digest changed), four fail-closed arms, and a receipt generated at run
  time from lane bytes. Pointer: `.ufo/waves/round-87/plan.md`, `probe/probe87-c1.mjs` at freeze
  `25a3a75d`.
- **Pre-data controls** (scored with the frozen probe, committed at freeze): base `0/12`,
  constant-CLEAN `0/12`, constant-DRIFT `1/12`, path-keyed `3/12` — `.ufo/waves/round-87/controls/*.txt`.
- **Motivating census** (scratch probe, committed): `.ufo/waves/round-87/open/census-toolbind.txt` →
  `receipts=239 bound=1 mismatch=9 unresolved=0 no_cmd=229` over rounds 74–86; 225 of the 229 carry
  neither field, 4 (all round 85) carry `cmd=` only. Reproduced independently by the connector seat
  (`.ufo/waves/round-87/build/K87Connector/census-details.txt:1`).
- **Instrument.** `scripts/receipt-bind.mjs`, contract `kumitate-receipt-bind-v1`, 544 L, 39-case
  hermetic selftest (`close/bind-selftest.txt` → `RECEIPT_BIND_SELFTEST: PASS held=39/39`); the
  instrument is the second token of `cmd=`, hashed from `git cat-file blob <rev>:<path>`, with a
  lane-external tool hashed from disk and counted `external=`; `unchecked` receipts are never clean.
- **Claim verdict: UNMET.** Three seat-constructed controls reach 12/12 and the frozen kill rule says
  such a control scores like a committed one: `build/K87Critic/cand-a-worktree.mjs` (hashes the
  worktree instead of the judged revision — the load-bearing counterexample, its transcript
  `build/K87Critic/transcript-cand-a-worktree.txt`), its hardcoded round-86-path variant, and
  `build/K87Review/dirkey-control.mjs`. Reported as a rejected-honest-stop; no capability row.
- **R86-D1 repair measured on real bytes.** `close/bind.txt` → `RECEIPT_BIND: DRIFT matched=1
  mismatched=9 unchecked=0 external=1` on the round-86 receipts, and the round-87 receipts read
  `RECEIPT_BIND: CLEAN matched=12 mismatched=0 unchecked=0 external=1`.
- **Round-87 close battery** emitted by a v2 runner that derives the subject per case
  (`.ufo/waves/round-87/build/K87ExecClose/run-close.mjs`, tested in a hermetic clone before use):
  `.ufo/waves/round-87/close/` — 11 of 12 cases green; `plan` is red (below).
- **R86-D2/R86-D3** (post-integration transcript, three source-gate receipts) were assigned to seat
  `K87ExecSources`, which returned **no artifact and no report**; they remain open and are disclosed,
  not claimed. `close/census.txt`, `close/spotcheck.txt` and `close/proxy.txt` re-measure three of the
  surfaces the seat was to cover, at M.
- **R86-D4** answered by construction: the round-87 spec names absolute paths only, and
  `ready-handoff` read `READY wave=w1 seats=14 resumes=0 total=14 attack=4/14 connector=1` with no
  `RELATIVE_WAVE_PATH` finding (`close/ready.txt`).
- **Spot-check adoption** (fourth recurrence): `node scripts/spotcheck-adopt.mjs --lane . --adopt
  corpus/lessons/round-86-verifier-spotcheck.md` → `SPOTCHECK_ADOPT: ADOPTED … wrote=both`,
  `README_MAP: CLEAN files=220 rows=220 covered=220`.
- **R87 map fix** (K86ExecMap's latent bug): a covered symlink whose target exists now reads
  `covered-not-file`, never `stale-covered` (`scripts/readme-map.mjs`, selftest 19/19 including the new
  arm; reproduction `build/K87ExecMap/repro/`).
- **Seat evidence used in this report**: critic (`.ufo/waves/round-87/w1/K87Critic.md`), reviewer
  (`w1/K87Review.md` + `build/K87Review/receipts/`), second reviewer (`w1/K87Review2.md`), sentinel
  (`build/K87Sentinel/findings.json`), mutation-tester (`build/K87Mutation/summary.json`), connector
  (`build/K87Connector/`), scribe pair (`build/K87ScribeLesson/`, `build/K87ScribeEntry/`), revenger
  (`w1/K87Revenger.md`), scout (`w1/K87Scout.md`), map executor (`w1/K87ExecMap.md`), instrument
  executor (`w1/K87ExecBind.md`).
- **Round shape**: ONE v1 wave, 14 seats (band 8–16) under `ufo-wave-policy.json`; roles
  executor 4, scribe 2, scout 1, connector 1, reviewer 2, critic 1, mutation-tester 1, sentinel 1,
  revenger 1; attack 4/14 = 28.6 % (≥ 25 %), connector 1 (≤ 2); no residual call; round total 14 seats
  plus the L1 planner seat (the validator rejects `planner`, so the L1 holds the canonical §3 seat and
  the bounded planning data-walk rode the scout item).
- **Dead / partial seats** (disclosed, never credited): `K87ExecSources` — no artifact, no report;
  `K87ExecClose` — runner artifact, no report; `K87Mutation` — battery artifact, no report. Eleven of
  fourteen seats filed `w1/<seat>.md`.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| `scripts/receipt-bind.mjs` (new gate, contract `kumitate-receipt-bind-v1`) | round 87 | `d3f64dc4` |
| `scripts/readme-map.mjs` R87 covered-symlink fix (+ selftest arm 19) | round 87 | `d3f64dc4` |
| `scripts/proxy-check.mjs` `pin.receipt-bind` key in `GATE_PINS` | round 87 | `d3f64dc4` |
| `SKILL.md` gate-registry row + checklist item 46 | round 87 | `d3f64dc4` |
| `SCORECARD.md` stanza (A 36, C 46, C2 222, pins), declaration, disposition, round-88 pre-registration | round 87 | `d3f64dc4`, `71efd992` |
| `corpus/knowledge/receipt-subject-binding.md` (new entry) | round 87 | `d3f64dc4` |
| `corpus/SOURCES.md` S250 (admit, A) + S251 (reject, B) | round 87 | `d3f64dc4` |
| `corpus/QUALITY.md` Q80 | round 87 | `d3f64dc4` |
| `corpus/lessons/round-87.md` | round 87 | `d3f64dc4` |
| `corpus/README.md` rows + `.ufo/pins/readme-map.json`, `.ufo/pins/source-captures.json` | round 87 | `d3f64dc4` |
| `.ufo/waves/round-87/**` (plan, probe, controls, census, 14-seat spec/dispatch/ready, build, w1, close) | round 87 | `d3f64dc4`, `71efd992` |

## Before → after measurements

**C1 (operability, capability acquisition `receipt-bind`)** — counting command, one line:
`node .ufo/waves/round-87/probe/probe87-c1.mjs --lane . --work <SCRATCH> --rev d3f64dc43027a9754700e70129b6ba91deaada19`

| state | value | commit |
|---|---|---|
| before — instrument absent (control) | `C87_C1: UNMET held=0/12` exit 1 | `25a3a75d` (`controls/base.txt`) |
| before — constant-CLEAN / constant-DRIFT / path-keyed | `0/12`, `1/12`, `3/12` | `25a3a75d` (`controls/*.txt`) |
| after — integrated instrument | `C87_C1: HELD held=12/12` exit 0 (twice) | `d3f64dc4` (`close/c1-probe.txt`) |
| **claim verdict** | **UNMET** — kill rule fired (three seat-constructed controls at 12/12) | `d3f64dc4` |

Supporting counts at M: round-86 detection `DRIFT matched=1 mismatched=9 unchecked=0 external=1`
(`close/bind.txt`); round-87 receipts `CLEAN matched=12 mismatched=0 unchecked=0 external=1`;
`RECEIPT_BIND_SELFTEST: PASS held=39/39`; mutation battery 14 mutants, 9 killed, 5 survivors
(`build/K87Mutation/summary.json`).

**Accounting (not a claim):** `node scripts/proxy-check.mjs --strict` → `PROXY: MATCH (A=36 C=46
operability=9; C2=222/222 …)`; operability's integer stays 9 (`f_O` = 82/85 ≈ 0.965, terminal under the
frozen formula). **Gate red at M:** `plan-before-ready` → `FAIL reason=MAP_DRIFT plan=25a3a75d
map_first=uncovered:lessons/round-86-verifier-spotcheck.md` (`close/plan.txt`) — the plan was frozen
before the adoption commit; round-88 candidate (2). `cite-check` carried debt unchanged.

## Sources & frontier

Counting command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin kumitate` → exit **0** at round end (7 `W04` duplicate-URL warnings, all
pinned in `.ufo/pins/source-dupes.json` `known=7`). At round start the same command read exit 0 with
**187** rows; at round end **189**.

- Rows before → after: **187 → 189** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`).
- Rows added by tier: **A +1 (S250)**, **B +1 (S251)**; status histogram `mined 149 → 150`,
  `rejected 25 → 26`, `queued 13` unchanged.
- Rows touched old→new: **none** — no existing row's `status`, `recheck` or `used-by` changed this round.
- Frontier rows advanced: the receipt-subject-binding surface entered the operability repertoire as a
  **landed instrument without a capability row** (claim UNMET); the OMP/MCP/isolation/durable-execution
  frontier rows are untouched.
- Captures: `.ufo/pins/source-captures.json` `76 → 78` (`node scripts/source-capture.mjs` →
  `SOURCE_CAPTURE: CLEAN captures=78 exemptions=111`); both new rows bind committed bytes under
  `.ufo/waves/round-87/open/`.
- **Assimilation: none.** The package `/home/vgpnk/Projects/shokuknow/merge/kumitate` was not adopted;
  no package row was re-grounded this round and no staged row is represented as admitted.
  `considerthese/2026-10-26.md` was re-checked: ideas 1/2/3/4/6 already have Q75/Q76/Q68/Q69/Q72
  implementations, idea 5 is outside this lane's authority.
- Gate decisions (admit S250, reject S251, quotes, captures) and the mined mistakes are in
  `corpus/lessons/round-87.md` `## Gate` and `## Mistakes`.

## Trend verdicts

- **expansion — unchanged.** One admitted source row deepens ground the coverage map already holds
  (receipt/attestation band); no new frontier area was entered, no capability row credited, and
  assimilation was none.
- **quality — improved.** A class that no gate could see becomes visible and gated: the round-86 bytes
  read `DRIFT matched=1 mismatched=9` where the lane previously read silence, the round-87 receipts bind
  clean, the map gate gains a real fix with a 19-case suite, and Q80 turns R86-D1 into a criterion. The
  claim itself is UNMET, so no scalar or repertoire credit is taken.
- **discernment — improved.** The round's own predicate was falsified from outside by three independent
  constructions and the round took the honest stop instead of narrowing the rule; five mined mistakes
  include two the L1 had introduced (a wrong census reading of `no_cmd=229`, and a wrong line citation
  `run-close.mjs:20` for the digest at `:24`), both corrected in-round.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence:
  `SKILL.md` gate registry (29 rows; `receipt-bind` added at round 87) and `## Verifiable checklist`
  (46 items); no non-author verifier wrote this line.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: LOG.md round 87
  (instrument built, close battery run at M, receipts committed `71efd992`).
- [~] Instructions executable by an agent without oral context — evidence: `plan.md`, the frozen probe
  and `w1/*.md` were executed by 11 seats that had no conversation with the L1.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` untouched this round
  (`git diff --stat d3f64dc4~1 d3f64dc4 -- PROVINCE.md` empty); no sibling-domain material admitted.

## Round mechanics and disclosures

- **Stale-lane:** none — this round was dispatched by the respawn-per-round driver and completed in one
  attempt; no other mission of this lane is open.
- **Tool installs:** none (no `uv`/`npx`/binary install this round); pacman stayed paused per the guard.
- **Inherited state:** the lane opened clean (`state … ahead=0 behind=0 tracked=0 untracked=0`). The
  fleet root holds one untracked file `after` (2026-11-03 20:05, content `=== SCORECARD diff base-`) that
  predates this round and is not this lane's; it is named, not touched. `.ufo/reports/round-89/kake.md`
  and the `.scratch/closure-*` files belong to other lanes/orchestrator and are untouched.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` found no file written by
  this round's seats outside the lane (every seat wrote beneath
  `kumitate-shokunin/.ufo/waves/round-87/`), so no copy-and-delete was needed.
- **Honesty:** every number above is a committed receipt path at M; the claim is UNMET and is reported
  as such.

## Erratum — round-start census (appended after the filed bytes, 2026-11-04)

The **Sources & frontier** section above says: *“At round start the same command read exit 0 with
**187** rows”*. That sentence is superseded: the census command was **not** run at round start; only
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` was, and it read **187**. The
round-start census was reconstructed after the fact, and the reconstruction is what the record now
rests on:

```
$ git clone --shared kumitate-shokunin /fast/scratch/hyaku/kumitate-r87/errata/base/kumitate-shokunin
$ git -C …/base/kumitate-shokunin reset -q --hard db97929212bb61ae970b10abac3cc4cd976713ae
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin \
    /fast/scratch/hyaku/kumitate-r87/errata/base/kumitate-shokunin
kumitate-shokunin  W04 S126 duplicate url docs.temporal.io/encyclopedia/detecting-activity-failures across scopes
kumitate-shokunin  W04 S247 duplicate url arxiv.org/abs/2212.06118 across scopes
kumitate-shokunin  ok  …/base/kumitate-shokunin/corpus/SOURCES.md
exit=0
```

The clone is a scratch fixture at the base revision (its directory basename makes the census print the
lane label `kumitate-shokunin`); it is not the lane and it was removed with the round scratch. Round-end
census, run in the lane: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate` →
`kumitate ok …/kumitate-shokunin/corpus/SOURCES.md`, exit **0** (7 `W04`, all pinned). Rows 187 → 189
stands, measured by `grep -cE` at both ends.
