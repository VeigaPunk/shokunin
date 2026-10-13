# kake-shokunin — round 10 report

**Axis-move: operability (lowest, 6→8).** Closed the "alerting on `violated[]`
deltas is undecided" README known gap (open since r5) with a runnable,
verified detector, and ran the first full checklist-executability audit.
Freshness deliberately not re-scored (probe-latest 2.07h fresh at audit; no
double-count). Commit `round-10` in `kake-shokunin/`. 11 read-only L2 probes
in ONE batch (planner/scout/executor×2/labrat/revenger/reviewer/critic/
connector/sentinel/scribe → `/tmp/kake-r10/`); zero fires, zero pushes, zero
browser ops; sentinel sha-verified webzites state unchanged.

## Landed (kake-shokunin)

- `scripts/probe-delta.mjs` — history-delta + coverage-hole detector over
  `state/probe-history.jsonl`. Verified: naive consecutive-row diff = **42
  events, 40 phantom** (labrat-replicated; spot `total:1` rows vs fleet
  sweeps fabricate clear/re-enter pairs) → universe-rule diff = **6 events,
  0 phantom**, all four r5 ground-truth records reproduced (sentinel: "the
  detector reproduces all four ops-automation.md r5 truths"). Critic
  falsifiers closed: exit-64 input validation (`--hole-hours banana`,
  `--since notadate` → explicit errors), `total>1` universe guard,
  partial-sweep flag. Exit codes proven: 0 / 2 (unreadable) / 64 (bad flag).
- `corpus/knowledge/probe-delta-alerting.md` — rules, baseline, naive-phantom
  mechanism, writer-semantics caveats (revenger), corrected ground truth.
- SKILL.md — probe-delta wired into audit step 1 (read-only semantics per
  sentinel WARN: audit never re-runs mutating verbs — `probe --all` writes
  `probe-latest.json` + appends history, `src/fleet.mjs:40-45`), drift-table
  row, cited-paths entry, absolute `kimi-surface.mjs` invocations.
- README known gap closed; `lessons/round-10.md`; SCORECARD.md created with
  before→after + move log; LOG.md round-10 entry.

## The round's falsification: our own r5 record was wrong

Raw rows prove `veigapunk-page`'s real violated→ok transition is
**09-21T03:32:06.747Z → 04:14:50.502Z**; the 04:14:50 and 09-22T22:58:23
sweeps carry *identical* `violated[]` sets (zero delta) — r5 had used the
42.73h coverage hole's **endpoints** as the transition window. Corrected in
`ops-automation.md` (planner + labrat + reviewer + L1 raw-row reads agree).
Also corrected there: xsnapshot-app "every run since 09-21" → constant on
**every full sweep since 09-21T01:34:20Z** (absent on 11 earlier full
sweeps; spot rows trivially omit other sites).

## Checklist-executability audit results

- Scout: **33/33** SKILL.md commands + **60/60** cited paths resolve (r9 PATH
  fix held); 11 mutating commands correctly flagged.
- ExecutorA (live): 5 verbs executed — 2 undocumented CLI behaviors found
  and landed in SKILL.md: `webzites status` **exits 1 on any last-probe
  violation** (`src/cli.mjs:99` — stdout-read, never a gate);
  `kimi-surface.mjs` has **no `--help`** (usage via unknown verb, exit 64,
  `:1197-1198`).
- ExecutorB (citations, RED/GREEN reproducer): 6/7 line-citations FIT; 1
  DRIFTED (`vault-properties.md` `:891-894`→`:903`) + 1 precision flag
  (`:339`→`:342`, range `:339-346`) — both fixed.
- Revenger (writer code): sole history writer `saveProbe`
  (`src/fleet.mjs:39-53`); `grokbot tick`/`bots task` write **merged
  fleet-sized rows** (stale-carried, `src/fleet.mjs:30-37`) — detector
  caveat documented; deficit rows carry skipped sites; `errors[]` =
  catch-block failures (`src/probe.mjs:79-81`), a different class from
  `violated[]`.

## Honest limits (critic verdict: rethink claim wording — addressed)

- The detector has **no consumer yet**: detection + checklist wiring only;
  alert *delivery* (notify/systemd fan-out) stays operator/webzites-owner
  gated — recorded as the standing handoff.
- "Suite audit" executed 5 of ~20 free-read verbs live; the rest cite LOG
  rounds (per sentinel: mutating verbs are audited by citation, never
  re-run). Planned r11: execute the live free-read subset.
- Connector: no sibling collision on probe-history alerting (kumitate/
  kagi/kasegi tooling adjacent only); CDP-9222 lease ownership between kake
  and kagi still unresolved — reported, not absorbed.

## Round-end actions

kake-shokunin: commit `round-10` + push (origin/master, branch clean before).
Main repo: this report committed + pushed.
