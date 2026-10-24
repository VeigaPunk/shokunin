# kama — round 32 report (hyaku inline campaign, attempt 1)

Lane tip (measured, pushed): `907cdcc0a76f8656fde4574c0a50725fcea42fa9` on `master`
(`jj-lane.sh state`: local=remote, ahead=0, untracked=0). Round-32 commits, in order:
`9afaf0e9` freeze · `c4c46ad5` C2 gate · `dc4258bd` docs · `967d8852` receipts · `3f1a7330` final
receipts · `907cdcc0` wave prepared. Data tip cited by the SCORECARD claims table:
`c4c46ad5b87d8b63f03e200a7b13eb8eeff46279` (ancestor of the tip; receipt lineage disclosed per claim).

## Work performed

Declared claims (1–3 rule; preregistered `.ufo/waves/round-32/preregistration.json`, frozen at
`9afaf0e9f03ea513e8ee54b43793d2f01cfa309e` before any data):

- **C1 — calibration** (lowest axis, 7): repair the frozen round-31 claim-row-evidence counter's
  non-injective `(row, class)` correction key with a round-qualified `(round, row, class)` key and
  a declared uniqueness precondition (`.ufo/waves/round-32/count-c2r.py`).
- **C2 — operability** (8, at the saturation line): repair the instrument-registry gate from an
  occurrence check into a meaning check — table-row presence, cell presence, non-empty exit map,
  cited-path existence (`tools/gate-registry-check.py` v2). Routed defect 3 of the round-31
  closure; C2's lesson Gate and evidence cite new row **S193**.

Work items:

- Freeze commit `9afaf0e9`: counter, preregistration, census start (exit 0), C1 before-receipts and
  kill-rule controls — evidence `.ufo/waves/round-32/{count-c2r.py,count-c2r.sha256,
  preregistration.json,census-start.out,c1/}`.
- C1 data: three round-qualified corrections appended (`CR31:11/12/13:C1:p1`); before/after
  receipts `.ufo/waves/round-32/c1/before-base.json` and `c2r/c2r-tip.json`; kill-rule controls
  `c1/controls/KeyCollapse/` (the frozen counter flips to `met True` on one collapsed `CR31:`-prefixed
  correction at `aca07f21`; the repaired counter refuses it: false 1, unresolved 3) and
  `c1/controls/DupKey/` (two corrections, one qualified key → both false).
- C2 build: gate v2 with `--selftest` (hermetic fixture arms + lane-tip arm); control matrix and
  mutation arms `.ufo/waves/round-32/c2/{controls,mutations}/`; summary `c2/SUMMARY.md`.
- Docs commit `dc4258bd`: SCORECARD round-32 sections (claims table, round-qualified corrections,
  round-31 record corrections for routed defects 5–6), SKILL round-32 registry block (registers the
  two prose-exposed counters round-17/round-26, the gate v2 row, the count-c2r row), LOG entry,
  PROVINCE/README dispositions, `corpus/lessons/round-32.md`, SOURCES row S193.
- Receipts commits `967d8852` + `3f1a7330`: C1 after (`met True`, valid 13), gate at the data tip
  (`registered 10 unregistered 0 defective 0`, exit 0), `GATE_SELFTEST pass=6 fail=0`, KQ36 re-runs
  (below), census end (exit 0).
- Wave prepared, not dispatched (host mapping): `.ufo/waves/round-32/w1/` — 32 seats, policy v1,
  validator exit 0, `taskCall.json` rendered; itemized below.
- Reconciliations (routed defects 5–6, appended records, not claims): RefRepair pointer drift
  (SCORECARD.md:1723 and the filed r31 fleet report cite `w2/out/RefRepair/`; the receipt is at
  `.ufo/waves/round-31/controls/RefRepair/receipt.txt`); w2 seat census
  (`find .ufo/waves/round-31/w2/out -maxdepth 1 -type d | wc -l` → 44 including `out` itself → 43
  seat dirs; 44 planned seats; `ConnInstrumentDup` has no dir and no referencing file — corrected
  count recorded in SCORECARD §Round 32).
- Misroot sweep before this report: `git -C /home/vgpnk/Projects/shokunin status --porcelain` —
  17 fleet-root untracked files, **none kama-related** (spot-checked each for kama/round-32
  content: `live.html live_s228.html nama.html s395.txt tf_bavelas.html unblob.log wb2.html write
  xc.xml` and `.bak` files under `scripts/hyaku/` are other lanes'/integrator debris; left
  untouched per the sweep rules). No kama seat note landed at the fleet root.

## Landed changes

| Commit | Change | LOG.md tie |
|---|---|---|
| `9afaf0e9f03ea513e8ee54b43793d2f01cfa309e` | C2r counter + preregistration freeze + census start + C1 before/controls | §Round 32, freeze bullet |
| `c4c46ad5b87d8b63f03e200a7b13eb8eeff46279` | `tools/gate-registry-check.py` v2 + `c2/` controls/mutations/selftest | §Round 32, C2 bullet |
| `dc4258bdb08d658f1c5b15abc8378461659bd155` | SCORECARD/LOG/SKILL/PROVINCE/README/lesson/S193 docs | §Round 32, docs bullet |
| `967d88528c1d83535563f971863f7855f76b4849` | `c2r/`, `c2/` data-tip receipts, `kq36/` re-runs, census end | §Round 32, receipts bullet |
| `3f1a73308bec9c2f4497c557d01bc58ec8e72eca` | final receipts (gate/selftest at data tip) | §Round 32, receipts bullet |
| `907cdcc0a76f8656fde4574c0a50725fcea42fa9` | wave-1 spec + validator + taskCall (prepared, undispatched) | §Round 32, wave bullet |

No capability row enters; the repairs are instruments, not repertoire (`AXES.md` §Capabilities).

## Before → after measurements

- **C1 (calibration 7 → 7).** Command:
  `/usr/bin/python3 .ufo/waves/round-32/count-c2r.py --repo <fresh clone> --tip <full commit> --out <receipt>`
  (counter sha256 `ef298b6311cc30907590317f1e477704d28bf880c292d25e1c711cd8f379c92e`, frozen at
  `9afaf0e9`). Before, base `18464d0866afd5c4b471c8478d72b079d82d1fa8`:
  `rows 30 base_mismatched 13 exempt 1 valid_corrections 10 false_corrections 0 unresolved 3 append_only True met False`
  (`c1/before-base.json`; the frozen round-31 counter prints identical counts). After, data tip
  `967d88528c1d` (re-run of the `dc4258bd` measurement, receipt `c2r/c2r-tip.json`):
  `rows 30 base_mismatched 13 exempt 1 valid_corrections 13 false_corrections 0 unresolved 0 append_only True met True`;
  `--list` shows the three `CR31:1x:C1:p1` corrections `ok=True` with distinct keys
  `(11|C1|p1)`, `(12|C1|p1)`, `(13|C1|p1)`. Kill rule, both directions:
  `c1/controls/KeyCollapse/tips.txt` — frozen counter `met True` / repaired counter
  `false 1 unresolved 3 met False` on the same tree; `c1/controls/DupKey/tips.txt` —
  `false_corrections 2 unresolved 3 met False`.
- **C2 (operability 8 → 8).** Commands: `python3 tools/gate-registry-check.py --rev <full commit>`
  and `python3 tools/gate-registry-check.py --selftest`. Before: v1 gate bytes (from base) exit 0
  `registered 9 unregistered 0` on a thin empty row, on an empty-exit-map row, on a row citing
  `.ufo/waves/round-999/count-c999.py`, and on the base tree whose round-17/round-26 counters are
  prose-only (`c2/controls/*-v1.out`, `c2/controls/prose-only-v1.out`); v2 semantics on the base
  tree exit 1 with both prose-only counters unregistered (`c2/before-base.out`). After, data tip
  `967d88528c1d`: `registered 10 unregistered 0 defective 0`, exit 0 (`c2/gate-tip.out`);
  `GATE_SELFTEST pass=6 fail=0` (`c2/selftest-final.out`); each fixture exits 1 with its named
  defect under v2 (`c2/controls/*-v2.out`); mutation arms flip exactly their fixture
  (`c2/mutations/`, thin-row entanglement disclosed).
- **KQ36 re-runs at the new tip** (sources changed → registered commands re-run,
  `.ufo/waves/round-32/kq36/`): frozen r31 count-c2 `... unresolved 3 append_only True met False`
  (unchanged); r30 hold `statements 141 ... valid_corrections 13 unresolved 0 met True`
  (unchanged); r29 `statements 69 ... unresolved 0 met True` (unchanged); r31 count-c1 live
  `registered 18 counted 17 target 12 met True not-counted ['K31-10']` (byte-consistent with the
  round-31 receipts).
- Receipt lineage honesty: `c2r/c2r-tip.json` and the gate/selftest finals measure the data tip
  `967d88528c1d` and are committed in `3f1a7330`; SCORECARD cites the data tip `c4c46ad5b87d` for
  the row revisions (ancestor of the tip).

## L2 floor and round shape

**Round shape: single prepared v1 wave (build + attack together), 32 seats, NOT dispatched.**
This seat has no `task`/AgentSwarm/workpool dispatch tool (accepted host mapping, reported as
expected — not a conformance defect): the L1 executed the build, controls, measurements and
integrations directly, and prepared the falsification wave for the orchestrator to dispatch between
rounds (same mapping round 31 attempt 3 used for its prepared wave-3). Wave:
`.ufo/waves/round-32/w1/spec.json` + `validate.json` (validator `ufo-swarm-wave.mjs plan`, policy
`scripts/hyaku/ufo-wave-policy.json`, **exit 0**, band 32–64) + `taskCall.json` (32 tasks,
rendered, not dispatched). Seat-role mix (32): executor 7, reviewer 6, scout 5, critic 4, scribe 3,
connector 2, mutation-tester 2, sentinel 1, revenger 1, simplifier 1. The §3 floor roles are
covered: connector ×2 (sibling-overlap, instrument-reuse), executor ×7, scribe ×3, scout ×5,
reviewer ×6, critic ×4, plus sentinel, revenger, mutation-tester ×2, simplifier; `planner` is the
frozen-topology seat held by the L1 (orchestrator ruling 2026-10-19) — the bounded planning
data-walk rode the L1 directly; `labrat`/`distiller` are not swarm roles (validator), so the one
bounded live probe rides a scout seat (`LiveGrammarProbe`) and the dedupe seat rides a simplifier
(`SimplifyEvidenceSet`). Routing: no `model` passed anywhere; the orchestrator's dispatch binds
`task.agentModelOverrides` from `~/.omp/agent/config.yml` (operator-owned, read-only here).
**Dead seats: none spawned** (nothing dispatched); the r31 wave-2 reconciliation above records one
historical unverifiable seat (`ConnInstrumentDup`). **Round total: 32 prepared seats, 0 dispatched,
0 dead**; residual-call rule not needed (no dispatched wave). Wave items attack the round-32 claims
(`RevCountC2rKeys`, `RevGateV2Rows`, `RevControlIsolation`, `RevReceiptReRun`, `CriticC1Shortcut`,
`CriticC2Shortcut`, `CriticSizing`, `CriticPreregDrift`, `MutC2rMatrix`, `MutGateV2Matrix`,
`SentinelScope`, `RevengerR32Defects`, `RevLessonGate`) and build the round-33 candidates
(eligibility counter, KQ42 probe gate, pin bytes, pointer sweep, wave census, grammar-transform
live measurement and recon; itemized in the spec, each item names its target).

## Sources & frontier

Census command (both ends pasted, exits 0):
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`
- before: `.ufo/waves/round-32/census-start.out` — `ok`, 192 `| S` rows (plus intentional W04
  duplicates, as every round since round 11).
- after: `.ufo/waves/round-32/census-end.out` — `ok`, **193 rows** (192 → 193).
- Rows added: 1, tier A: **S193** (own-work — `tools/gate-registry-check.py` v2 contract; opened
  2026-10-24 at `c4c46ad5b87d`; located quote 16 words, recorded in the round-32 lesson Gate).
- Rows touched old→new: none (S180–S192 byte-unchanged). Frontier rows advanced: none (S192 stays
  the grammar-transform frontier anchor).
- Sourced claim: **C2** — its evidence lands cite S193 via the lesson Gate
  (`corpus/lessons/round-32.md`) and the SKILL round-32 registry block; the SCORECARD C2 row's
  Evidence column names the lesson.
- Mistake mined: `corpus/lessons/round-32.md` §Mistakes — (1) reference-drift (RefRepair pointer,
  routed defect 5), (2) number-drift (w2 seat count, routed defect 6), (3) prose-only registration
  of two counters for four rounds. Each fix shown able to fail (receipts cited in the lesson).

## Trend verdicts

- **expansion — unchanged.** No new `knowledge/` entry and no coverage-map ground moves (README
  round-32 disposition); S193 is an own-work instrument row, and the repairs deepen method, not
  domain surface. The serving frontier (`response_format` grammar transform, `/v1/completions`,
  other engines, K05) is carried forward unchanged and armed with wave items.
- **quality — improved.** Two frozen-counter defects routed by the round-31 closure are repaired
  with fail-capable controls and mutation arms; the meaning gate exposed and fixed two
  prose-only registrations; the round-31 counters re-run byte-stable at the new tip (KQ36); the
  two routed record reconciliations (pointer drift, seat census) are corrected by append with
  committed sweep commands. No admitted entry failed its re-check.
- **discernment — improved (author reading; outside closure decides).** Every shortcut the waves
  would have hunted was hunted by the preregistered kill rules before admission: the frozen
  counter's collapse shortcut is receipted red-handed, the do-nothing gate is receipted on every
  fixture, and both claims are reported as instrument repairs with held scores rather than
  promoted. The unresolved-3→0 census delta is exactly the three named dispositions, no more.

## Routed-defect dispositions (round-31 closure)

1. C1 eligibility — NOT repaired this round; wave items `ExecEligibilityCounter`,
   `ConnInstrumentReuse`, `MutC2rMatrix` (arm 1) attack/build it for round 33. 2. C2
   round-qualified key — **repaired and claimed (C1)**. 3. C3 occurrence-only gate — **repaired
   and claimed (C2)**. 4. KQ42 probe gating — NOT repaired; wave items `ExecKQ42ProbeGate`,
   `ExecMeaningProbes`. 5. RefRepair pointer drift — reconciled (appended correction). 6. w2 seat
   count 43-vs-44 — reconciled (43 seat dirs; 44 planned; `ConnInstrumentDup` unverifiable).
   Pin-bytes (MutC1Pin) — NOT repaired; wave item `ExecPinBytes`.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources →
  unchanged this round; registry blocks extended (round-32 rows); asserted by author, evidence
  `SKILL.md` §§Local gate/probe registry, Round-31/32 instrument registry rows.
- [~] At least one end-to-end domain task executed and logged in LOG.md → round-16/17 live
  llama.cpp lifecycle receipts (`.ufo/waves/round-16/live/receipt.json`,
  `.ufo/waves/round-17/live/receipt-{1,2,3}.json`) plus this round's live re-runs of the r31
  chat-adapter counter (`.ufo/waves/round-32/kq36/r31-c1-at-tip.json`); no named non-author
  verifier.
- [~] Instructions executable by an agent without oral context → unchanged; this round's
  receipts were produced by pasting the preregistered commands; asserted by author.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → `PROVINCE.md` round-32 note keeps the
  boundary (no endpoint/consumer sampling; sibling surfaces reported, not absorbed;
  `ConnGrammarOverlap` wave item re-checks the grammar-transform scope).

## Extras

- **Stale-lane:** none — respawn-per-round driver; this report is the only open artifact of the
  round and lands last.
- **L0 questions:** none appended this round (no operator decision blocked the round; the
  prepared-wave host mapping and the paused pacman guard are operator-owned and respected).
- **Tool installs:** none this round (no installs or upgrades by the L1 or any seat — nothing was
  dispatched).
- **Watchdog digest** (mutable log, verbatim): `2026-10-24T02:48:12-03:00 launch kama round=32
  pgid=589693 driver=hyaku-inline attempt=1`; no `lane-dead-no-report kama round=32` line exists —
  this attempt 1 is the round's first and only launch.
- **Honesty notes:** the claims are instrument repairs with held axis scores (calibration 7,
  operability 8); depth re-earn under a repaired eligibility counter is deliberately deferred to
  round 33 with the falsification wave prepared first; the thin-row mutation arm is entangled with
  the cell-presence checks and is disclosed as such rather than presented as isolated.
