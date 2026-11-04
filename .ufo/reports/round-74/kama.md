# kama — round 74 report

Lane: kama. Round 74, attempt 2 (attempt 1 died `lane-dead-no-report` ~30 s after launch;
watchdog `.ufo/watchdog.log` lines 2206–2208 — KQ47 receipt; this attempt launched
2026-11-04T00:15:07-03:00). Lane tip after the round: `8020b2f26c1bc1807680024f71267c46c98bbf7c`
(remote-verified, `git ls-remote origin refs/heads/master`).

## Work performed

Declared claims (frozen in `plans/round-74-claims.md`, freeze commit `df18ad1e`, base
`868dd701`):

- **C1 — calibration** (lowest assigned axis, 7): the self-description reconciler sees the
  newest capability repertoire whatever heading form it wears (R73-D1 repair).
- **C2 — operability**: the tip-claim rule is realizable — an explicit-revision binding
  replacing the impossible committed-header-equals-tip clean rule, killing wrapped/offset
  claims, hex case-insensitive (R73 routed defect 2).
- **C3 — freshness**: a host block cannot be edited into matching the live host —
  base-revision preservation (R73 routed defect 5; not an assigned-axis change).

Work items, each with an evidence pointer:

- Frozen the three claims with pre-freeze do-nothing controls: fixtures
  `c1_invisible/c1_clean`, `c2_wrapped/c2_offset/c2_mixed_honest/c2_clean_realizable`,
  `c3_edited/c3_clean` built by `.ufo/waves/round-74/controls/build-survivors.py`; before
  receipt `.ufo/waves/round-74/measured/before/score-survivors-base.out` (base counters
  green on every hole: `canon` round 71, `claims=0` on both escapes, edited block green);
  `controls/freeze.txt` pins base/plan/script/receipt sha256s (commit `df18ad1e`).
- ONE v1 wave, 13 seats (spec/dispatch `b0b903a0`, band 8–16, attack share 4/13 ≈ 30.8% —
  reviewer, critic, mutation-tester, revenger; 1 connector; planner seat held by the L1 per
  the frozen-topology ruling): 4 executors, 2 scribes, 1 scout, 1 connector, 1 revenger,
  1 reviewer, 1 critic, 1 mutation-tester, 1 sentinel. `w1-results.json`: 13/13 settled,
  0 dead seats. All seat reports under `.ufo/waves/round-74/w1/`.
- Built and certified three instruments: `tools/round74-selfdesc-canon.py` (selftest 11/11),
  `tools/round74-receipt-claim-binding.py` (selftest 9/9 including the `blob-reader-seam`
  arm), `tools/round74-province-host-drift.py` (selftest 10/10); gate arm 7 composes them
  (`PRE_REPORT_SELFTEST pass=15 fail=0`, post-apply gate sha256
  `6d2e379796de027cc246aaa1673a175d058ea35f1f3ad5c9b9128a095045c1c0`).
- **Concurrent-write incident, fully disclosed** (lesson Mistakes 3): the L1's emergency
  pre-WAVE-DONE build of the C2 module overwrote seat EX02ClaimV2's completed deliverable
  twice. EX02's committed report (15-arm selftest record, critic-fixture matrix, preserved
  `receipts/overwritten-peer-version.py`) is the evidence of the seat's work; the committed
  module is the L1's re-certified replacement, re-run against CRT01's four critic fixtures
  (`measured/after/critic-fixtures-committed-module.out`; one documented F2c divergence).
- Frontier step: opened S546 os-release(5) live (accessed 2026-11-04, retained bytes
  sha256 `c7ba68ea…`, 16-word located quote §OPTIONS `ID=` lines 187–194), mirror census
  exit 0 BEFORE the append (`measured/after/mirror-census-gate.out`); registry 285 → 286
  rows; knowledge entry `corpus/knowledge/host-block-base-revision.md` (44 filtered
  knowledge files); assimilation none (9 staged-id collisions, 7 quarantined rows —
  `assimilation/summary.out`); considerthese 2026-10-26 nothing new (proposals 1–3 landed
  r46/r53/r48; proposal 4 = KQ122 + this round's live pin-watch run:
  engine=sglang pin=v0.5.22 newest=v0.5.23 newer=1; engine=vllm pin=v0.32.0 newest=v0.33.0
  newer=1; engine=llama.cpp pin=b11755 newest=b12098 newer=273; `pins=3 current=0 behind=3
  missing=0 error=0`, exit 1).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only
  orchestrator-owned `.scratch` state and the pre-wave `after` file — no seat misroots;
  nothing copied or deleted.
- Tools installed/upgraded this round: none (no seat installed anything; SEN01 two-pass
  audit clean, pacman guard respected).

## Landed changes

All commits via `jj-lane.sh`, pushed (remote == local at `8020b2f2`):

- `df18ad1e` — frozen claims + controls + before receipts (LOG §Round 74 names it).
- `b0b903a0` — wave spec + dispatch evidence.
- `07994dfc` — three v2 instruments, gate arm 7 patch, settled wave evidence (incl. EX02's
  report and receipts).
- `9e2b547f` — the round record: SCORECARD §Round 74, 25-row bold canonical list, LOG
  entry, lesson, S546 + knowledge entry, PROVINCE `recorded at` token.
- `0701c7f6`…`f54b4709` — record corrections: EX02 concurrent-write truth, receipt rev
  headers + re-pins, closure pointer, head mirror, reconciler statements.
- `ee68adf4` — canon selftest cli-misuse arm made cwd-independent.
- `77496128`, `b9f8a807`, `baa0675a` — PROVINCE/SKILL instrument registrations, registry
  and province counter receipts, dependent row re-anchors.
- `a5bc42a1`, `8020b2f2` — final receipt pin + the green gate receipt.

## Before → after measurements

Counting command for all three claims:
`python3 .ufo/waves/round-74/controls/score-survivors.py` (pinned receipts:
`measured/after/score-survivors.out`, measured at `baa0675a`).

- **C1** — before: `SURVIVORS c1 base_round=71 base_rows=3 v2_killed=0 v2=absent clean=n/a`
  (before receipt, freeze commit). After: `SURVIVORS c1 base_round=71 base_rows=3
  v2_killed=1 v2=present clean=True`; kill fixture exit 1 `invisible=4` each named; clean
  fixture exit 0 `total=7 invisible=0`; live lane before `total=22 invisible=5` exit 1,
  after the record `total=25 invisible=0` exit 0 (`w1/EX01CanonV2/live-at-tip.out`).
  Measured at `baa0675a`, carried by `98d2f577`/`a5bc42a1`.
- **C2** — before: `SURVIVORS c2 base_green=2 v2_killed=0 v2=absent clean=n/a` (r73
  counter green, `claims=0`, on both escape fixtures). After: `SURVIVORS c2 base_green=2
  v2_killed=2 v2=present clean=True`; `c2_wrapped` exit 1 `wrapped-claim`; `c2_offset`
  exit 1 `offset-claim`; `c2_mixed_honest` exit 0 `bound_revisions=1`;
  `c2_clean_realizable` exit 0 (the realizable clean rule).
- **C3** — before: `SURVIVORS c3 base_green=1 v2_killed=0 v2=absent clean=n/a` (r73
  counter green on the date-edited block). After: `SURVIVORS c3 base_green=1 v2_killed=1
  v2=present clean=True`; `c3_edited` exit 1 `edited-block`; `c3_clean` exit 0 `edited=0`;
  live lane `stale=0 edited=0` exit 0 (`w1/EX03DriftV2/live-lane.out`).
- Gate (the round's composed verdict): before no arm 7; after
  `PRE_REPORT round=74 arms=7 failed=0 uncommitted=0` (`measured/after/pre-report-gate.out`
  at `8020b2f2`): selfdesc `mismatches=0 met=True closure_ptr=1`; newest-closure green;
  receipt-audit `cited=200 resolved=182 unresolved=0`; worktree-landing `clean=5 dirty=0`;
  round-scope `cases=6 findings=0`; round-clean `files=0`; round74-v2
  `canon total=25 invisible=0 | cited=14 bound=14 unbound=0 shifted=0 stale=0 | stale=0
  edited=0`.

## Sources & frontier

Census command (both ends):
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`.
Round start: exit 0, 285 rows (receipt: `w1/SCR01Sources` report + round-start run).
Round end: exit 0, **286 rows**. Rows added by tier: A=1 (S546 os-release(5), man7.org,
docs, mined, opened 2026-11-04, accessed-by-URL fetch with retained bytes sha256
`c7ba68ea45180c33bad72a3b47cf09e3d6d34d0a5313a5acf73a14fc64f8a74e`). Rows touched
old→new: S546 `queued`→`mined` at append (pre-append state recorded in the seat draft and
the lesson Gate). Frontier rows advanced: none (S546 is new). Assimilation: none — 9
staged-id collisions (S330 S333 S334 S335 S346 S347 S352 S353 S363; mass drift, adopt
nothing per §10) and 7 quarantined payload-absent register rows; receipt
`.ufo/waves/round-74/assimilation/summary.out`. considerthese: see Work performed.

## Trend verdicts

- **expansion: improved** — knowledge files 43 → 44 on uncovered ground (host-block
  base-revision grammar; the r73 closure's hole class), cited to the new S546 row; the
  repertoire grew 22 → 25 demonstrated operations.
- **quality: improved** — the three routed holes are killed with committed red-before
  receipts (base counters green on every survivor); the record's receipt citations now
  bind by explicit revision (14/14 bound, 0 shifted); the r73 closure's own record
  corrections (closure pointer, head mirror, reconciler statements) are re-derived green
  at the tip (`mismatches=0 met=True`). Bounded: the append-only history audit stays
  disclosed red (carried, not re-stamped); the full C2 kill vocabulary carries one
  disclosed interpretation (F2b) and one routed ambiguity (F2c).
- **discernment: improved, with a self-caught defect** — every attack seat is on record:
  LAB01 reproduced the before receipt byte-for-byte and named one junk-row cheat per claim
  (each forbidden by the frozen wording); RVW01 found no reachable shortcut in nine
  attempts; CRT01 refuted no claim and its pre-registered gaming acceptance holds;
  MT01 killed 24/25 mutants with the survivor covered by the new seam arm; SEN01's
  two-pass audit is clean. The L1 itself committed the round's one real defect — the
  concurrent-write overwrite of EX02's deliverable — and mined it as lesson Mistakes 3
  with the fix stated in the round-75 plan; the disclosure is in the record, not hidden.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
      → §§Decision table, Error signatures, Checklist; round 74 adds four registry rows
      (`SKILL.md:317-320`); no named non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md
      → §§round 1–3, 16–17, 61; round 74 adds three live instrument receipts at the tip
      (canon/drift/claim-v2 live runs + the seven-arm gate); no non-author mark.
- [~] Instructions executable by an agent without oral context
      → §Checklist + the frozen plan's predicates; every measured receipt carries its
      command and revision.
- [~] No cross-domain bleed (PROVINCE.md still accurate)
      → §Write boundary + `corpus/knowledge/cross-lane-scope.md`; round 74 registers the
      new instruments in PROVINCE.md and records the host triple + recorded-at token.

## Round shape and extras

Round shape: ONE v1 wave, 13 seats (band 8–16), no residual call; 13/13 settled, 0 dead;
attack share 4/13 ≈ 30.8% (≥25%); connector seats 1 (≤2); roles span m_flash (12 seats)
and m_zfl (reviewer) per the live route table (`task.agentModelOverrides`; the run-15
"scout m_antigravity" note is superseded by the 2026-11-03 net map — config is authority).
L2 floor: planner = L1 (frozen topology), 3+ executors, 2 scribes, 1 scout, 1 connector,
1 reviewer, 1 critic. Tooling installs: none. Stale-lane: respawn-per-round driver; no
other mission of this lane is open. L0: the round-65 NTFS-path question stays unanswered —
routed around; nothing assumed answered. KQ47 attempt record: attempt 1
`lane-dead-no-report` (watchdog 2206–2208); attempt 2 is this round.
