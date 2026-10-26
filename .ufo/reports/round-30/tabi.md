# tabi — round 30 report (hyaku run 8, attempt 1, L1 TabiR30)

Lane repo `tabi-shokunin`, branch `master`. Baseline `f7c0317e4f8445502005e79e3d65767430912dab` → final lane tip
`66171034636cad5be49b479c98355bd944919b51` (pushed; `git ls-remote origin refs/heads/master` prints it). Claims
measured at `d3cd62a1529fcf8b1cfa2eebc1800e6e7f6e3a1b`; the one later commit adds only `.ufo/waves/round-30/` files,
which neither counter reads. Not a fresh-start round: round 29's closure was admitted (MANIFEST tabi lane_round 29).

## Work performed

Declared claims (frozen before data in `061e62024c0523d3c6c7e819506a773ff2cd7d75`, `.ufo/waves/round-30/claims.json`):

- **C1 — operability** (lowest-axis tie at 8): the self-tests of two lane gates (`scripts/check-s106-evidence.mjs`,
  `scripts/check-release-pins.mjs`) must kill every fault mutant of a frozen catalogue (`scripts/gate-mutants.json`:
  27 fault rows reproducing round 29's MutC1Baseline/MutC3 tables, 13 equivalent rewrites) without falsely killing an
  equivalent rewrite. Counter: new gate `scripts/check-gate-mutants.mjs`.
- **C2 — coverage** (sourced claim; §10 assimilation): the frontier item "Rate/ToS surface for site-interaction
  records" (open since kaika round 1, `corpus/README.md:182`) gains two admitted entries re-grounded in-round from
  `merge/tabi/`. Counter: new gate `scripts/check-frontier-admission.mjs` with `--live`.

Work items:

- Counters, catalogue, controls (do-nothing + three junk per claim) frozen before data — `061e6202`;
  `.ufo/waves/round-30/baseline/README-receipts.md`.
- C1: three s106 cases and nine release-pin cases (wave-1 ExecS106Cases, ExecPinsCasesA, ExecPinsCasesB) — `38891ca0`
  (`scripts/check-s106-evidence.mjs`, `scripts/check-release-pins.mjs`; production code byte-identical, w2 RevC1Diff).
- C2: entries `corpus/knowledge/rate-limit-policy-fields.md` (S116, IETF RateLimit header-fields draft `-11`) and
  `corpus/knowledge/host-published-rate-limit-headers.md` (S117, Discord developer docs Rate Limits), receipts and
  independent refetches under `corpus/evidence/round-30/frontier/` — `38891ca0`; errata from wave 2 — `e8720bcf`.
- Routed round-29 defects: (1) 23 `used-by` appends + 4 `queued→mined` flips, logged (`corpus/lessons/round-30.md`
  §used-by changes, §Wave-2 corrections) — `38891ca0`, `e8720bcf`; (2) S110/S114/S115 Gate quotes re-grounded in their
  own bytes (lesson §Re-grounded Gate quotes) — `38891ca0`; (3) round-29 lesson M4/M5 table rows appended — `072af95f`;
  (4) chromium-156 entry errata (+10/+11, 9-line guard, 156:126) — `072af95f`, `e8720bcf`; (5) release-pin population
  rule named with excluded rows (lesson §Release-pin population rule) — `072af95f`; (6) S118 supersedes S044 (404 path),
  bytes `corpus/evidence/round-30/s118/` — `072af95f`; (7) is C1.
- QUALITY criteria 74–79 (`corpus/QUALITY.md`) — `072af95f`. README frontier rows + scope corrections — `072af95f`,
  `e8720bcf`, `0ffc6ea0`.
- SCORECARD round-30 disposition and tally corrections (`SCORECARD.md` tail), LOG entry (`LOG.md` §Round 30) —
  `0ffc6ea0`, `d3cd62a1`.
- Wave evidence: `.ufo/waves/round-30/w1/` (32 reports) — `af0664ed`; `.ufo/waves/round-30/w2/` (34 reports),
  final measurements `.ufo/waves/round-30/measure/` — `66171034`.

Round shape: **two v1 waves** (policy `ufo-wave-policy.json`, both validated, `w1-validate.stderr`/`w2-validate.stderr`
empty), dispatched through the inline handoff (`w1.ready`, `w2.ready`).
- W1 build + first falsifiers: 32 seats — 9 scribe, 7 executor, 5 critic, 3 reviewer, 3 connector, 2 mutation-tester,
  2 scout, 1 sentinel (m_flash roles 22/32 = 69%; attack roles 10/32 = 31%).
- W2 falsify: 34 seats — 12 critic, 10 reviewer, 6 executor, 2 connector, 2 scribe, 1 mutation-tester, 1 sentinel
  (m_flash 21/34 = 62%; attack 23/34 = 68%); every item names what it attacks.
- Round total **66**; no residual call; dead seats **0** (w1-results.json 32/32 and w2-results.json 34/34 with a report
  each). The §3 planner seat is held by the L1 (validator rejects `planner`); the planning data walk rode W1 scouts and
  connectors. Routing per run-8 role map; no `model` passed.

## Landed changes

| Commit | Change | LOG.md |
|---|---|---|
| `061e62024c0523d3c6c7e819506a773ff2cd7d75` | claims freeze, two counters, catalogue, SKILL registry rows, controls, assimilation collision check | §Round 30 ledger |
| `38891ca0bd28fff45b6736edfcad93438b782063` | C1 cases; C2 entries, rows S116–S117, receipts; used-by curation; lesson Gate; tally corrections | §Round 30 ledger |
| `072af95fe2822f0785a6ff88a578e2142dd258e5` | S118; mistakes M1–M6; population rule; QUALITY 74–79; round-29 addenda; README frontier | §Round 30 ledger |
| `af0664ed039af98a5d8c460cf99c71d726dd41af` | wave-1 evidence and results; w2 spec/dispatch | §Round 30 ledger |
| `e8720bcfcdf97a4bd53fa91a0dab1e4616ae01d4` | wave-2 corrections: status/recheck/used-by changes, entry errata, counter-weakness disclosure, identity-blind C1 receipt | §Round 30 ledger |
| `0ffc6ea01fea2943e4f3516eaa9a0fbb7e6062d3` | SCORECARD disposition, LOG entry, lesson M5–M7 | §Round 30 (this entry) |
| `d3cd62a1529fcf8b1cfa2eebc1800e6e7f6e3a1b` | one-script-per-line tally corrections, lesson M8 (measured revision) | named in report |
| `66171034636cad5be49b479c98355bd944919b51` | wave-2 evidence, final measurements, census end | named in report |

## Before → after measurements

All after-readings in a clean `git clone --shared` at `d3cd62a1` with frozen digests verified
(`.ufo/waves/round-30/measure/measured-provenance-d3cd62a.txt`).

- **C1** — `node scripts/check-gate-mutants.mjs --rev <REV> --json` (counter `02945f88…3a55`, catalogue `cd1c27a2…3833`).
  Before at `061e6202`: fault_survivors **14**/27, benign_killed 0/13, exit 1 (`measure/c1-before-at-freeze.json`).
  After at `d3cd62a1`: fault_survivors **0**/27, benign_killed **0**/13, exit 0; pristine self-tests s106 10/10,
  release-pins 29/29 (`measure/c1-after-at-d3cd62a.json`). **Met** under the frozen rule. Controls: length-fingerprint
  junk 0 survivors / 13 false kills; site-grep junk 9 / 3; literal blacklist exit 2. Disclosed after freeze: the
  counter leaks mutant identity through its run directory (w1 CritC1Counter; CritClaimSizing J5 control meets the
  target) — independent evidence: random-directory re-run 0/0 (`measure/c1-identity-blind-at-072af95.json`), kill
  attribution to fixture-building cases (w2 RevC1KillAttribution, CritC1EnvLeak); one kill (`pins-f3-bytes-absent`) is
  a self-test abort, not a named case. The landed diff also touched the self-test runner (beyond claims.json's
  implementer note); w1 CritClaimSizing shows the cases alone reach 0/0.
- **C2** — `node scripts/check-frontier-admission.mjs --rev <REV> --frontier rate-tos-signal --since 2026-10-26 --live --json`
  (counter `cadef57e…9eca`). Before at `061e6202`: population 0, admitted 0 (`measure/c2-before-at-freeze.json`).
  After at `d3cd62a1`: population **2**, admitted **2**, live true, exit 0 (`measure/c2-after-live-at-d3cd62a.json`;
  offline also 2/2). **Met** under the frozen rule. Controls: package-as-is 0 (r4-opened), date-bump 0 (g1),
  self-quote 2 offline / 0 live. Disclosed after freeze: `--live` accepts `file://`, follows off-host redirects and
  inherits `~/.curlrc` (w1 SentinelFetchScope, w2 MeasureC2Clean); g7 does not prove refetch independence (w1
  CritClaimSizing J5). For the committed receipts: https on the rows' hosts (w2 SentinelReceipts), the live run fails
  `l1-live` inside a no-route namespace (w2 MeasureC2Clean), refetches match independently logged fetches (w2
  CritC2Fabrication), third-seat live fetches agree (w2 RefetchLiveS116/S117).
- No-harm at `d3cd62a1` (`measure/noharm-at-d3cd62a.txt`): gate registry nonconformant 0; release-pins 23/23 resolved;
  s106 valid; sources gate clean; w2 ExecNoHarmTip found no gate green at the freeze and red at the tip.
  `check-selfassessment` mismatches **1** (was 0 at baseline): `SCORECARD.md:1527` gate-mutants 12/12 vs observed 2 —
  the counter reads the first `cases=` token in the gate's output, which is a per-case refusal message
  (`… cases=2 passed=1 …`); the true tally is the summary line `cases=12 passed=12`. Two other findings my two-tally
  lines caused were corrected one script per line. Disclosed as lesson M8; the operator rules whether this residual
  counts as calibration harm.

## Sources & frontier

Census (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`):
start exit 0, `tabi ok`, 18 W04 (`.ufo/waves/round-30/baseline/census-start.txt`); end exit 0, `tabi ok`, 19 W04 — the
new W04 is S118 re-reading the devtools file S036 pins under a different scope (`.ufo/waves/round-30/measure/census-end.txt`;
w2 ExecCensusTip).

- Rows 115 → 118 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`); added by tier: A 3 (S116 spec,
  S117 docs scoped to Discord's own headers, S118 code). Status mined 87 → 94, queued 19 → 15.
- Touched old→new (lesson §used-by changes and §Wave-2 corrections): 23 `used-by` appends (S033…S106); S080/S081/S093/S098
  status queued→mined; S116 recheck 180d→2026-11-24; S118 used-by + `source-recheck-round-18.md`.
- Frontier advanced: "Rate/ToS surface for site-interaction records" open → docs-held on its rate half (ToS half and
  runtime open; `corpus/README.md` §Round 30 + correction); "Gate self-test kill coverage" held for two gates.
- Sourced claim: C2 rests on S116/S117, opened 2026-10-26 (lesson §Gate with URL, access time, located quote).
- Assimilation: theme **rate/ToS signal vocabulary** from `merge/tabi/`. Admitted 2 (`host-rate-limit-signal-classes-r14.md`
  → S116, `host-rate-limit-header-set-r16.md` → S117); rejected 2 (`rate-and-tos-signal-vocabulary.md` — staged S106/S110;
  `host-rate-limit-signal-classes-r13.md` — staged S147–S149; register quotes absent, re-checked live by w1
  RevQuarantineCarry). Lane ids: 115 (S001–S115); staged ids: 148; collisions 14 (S102–S115), none an adopted id;
  renumber map S159 → S116, S182 → S117 (by document); guard proof `.ufo/waves/round-30/assimilation/guard-proof.txt`.
  Quarantine slice 38 rows (register sha unchanged since round 27); none adopted. The staged S159 anchor's
  "-10 and later return 404" was false (lesson M2).
- considerthese/: no such directory in this lane.
- Mistake mined: `corpus/lessons/round-30.md` §Mistakes M1–M8 (each with table row and subsection).

## Trend verdicts

- **expansion: improved** — two admitted entries on ground the lane did not hold (no RateLimit / X-RateLimit vocabulary
  at baseline, w2 CritC2Surface), each citing a mined row opened this round; frontier row advanced.
- **quality: improved** — 14 previously invisible gate checks now seen by self-tests; S044's 404 anchor superseded;
  three Gate quotes re-grounded; errata for every wave-2 content defect (no quote fabricated, w2 RefetchLive*,
  CritEntry*). Disclosed residual: both new counters gameable by junk that attacks the counter (M5–M7).
- **discernment: improved** — package claims tested against live sources (stale revision ceiling refused, emoji-route
  caveat re-scoped), admit/reject spot-checked by a w2 reviewer (agree/agree), round-29 spot-check routed defects all
  turned into fixes or QUALITY 74–79, post-freeze counter holes reported rather than hidden; one calibration finding
  (M8 instrument misread) left standing and disclosed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `tabi-shokunin/SKILL.md:697` (approval table), `:1598-1617`, round-30 registry rows `SKILL.md` §Round 30; no non-author verifier this round
- [~] At least one end-to-end domain task executed and logged in LOG.md — `corpus/knowledge/multi-step-journey.md` §1–§2, §7; `LOG.md` round-3 entry
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/executor-test-sufficiency.md` §0, §4 (executor was a lane-dispatched seat; still needs a non-author run)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:3-19` unchanged; w1 ConnSiblings: C2 surface uncontested, kake/kagi splits respected

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none by the L1; seats reported none.
Open L0 questions: none new; the round-27 tabi question on S114/S140 adoption stays open and was routed around.
Defects of this round (for the closure): seat scratch dirs left under `/fast/scratch/hyaku/tabi-r30/` by several
seats were removed by the L1 after landing; `check-gate-mutants.mjs` leaks an empty work dir on exit-2 refusals
(w1 RevClaimsFreeze).
