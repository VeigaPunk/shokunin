# kengaku — round 94 report (hyaku run 15, attempt 1; L1 KengakuR94)

Lane `kengaku-shokunin`, branch `master`. BASE `0cbb927914e07818e1aaee7e72d8b3c90a2d21c2` (round 93
admitted, MANIFEST 1388). Final lane hash **`a618227e4c4d09a04c1f613fc5e5cf9f298a12ef`**
(`git ls-remote origin refs/heads/master` → `a618227e4c4d09a04c1f613fc5e5cf9f298a12ef`).
Inherited state: clean tree, no `lane-dead-no-report kengaku round=94` line; nothing inherited.

## Work performed

Declared claims (2), frozen at F `844c504e` in `plans/round-94-claims.md`:
**R94-C1 — coverage** (the lowest non-retired axis, held at its L0 cap 7): a twelfth located
offline replay of a pinned Terminal-Bench 2.0 grader, `write-compressor`. **R94-C2 —
calibration** (held at ceiling 10): known false gates that pass the lane's freeze-integrity
counter, 5 → 0, through gate v2 and a counter that mutates the gate under test.

- Protocol load and claim choice: round-93 spot-check read
  (`corpus/lessons/round-93-verifier-spotcheck.md`), all seven routed defects dispositioned in
  `corpus/lessons/round-94.md` (table "Round-93 spot-check routed defects").
- P0 mechanism predictions filed before any probe run and the capture landed:
  `bdcb1ec06434adfdea25823a2fb90f33bcf1dc5c` (`.ufo/waves/round-94/L1/predictions-mechanism.txt`;
  `corpus/evidence/round94/graders/write-compressor/`, 11 files fetched HTTP 200 at `2fd12b88`).
- P1 instruments: `997a6fe5fbb4a4af9f38e436bccd8f604da1d746` — `plans/round94_compressor_probe.py`
  (reference `data.comp` rebuilt offline from the captured `solve.sh` with host rustc inside bwrap;
  8 cases × 4 legs of the grader's own three functions), `plans/round94-cases.json`,
  `plans/round94_c1_replay.py` (L7 now checks the executed member *set* against BASE, round-93 W-5),
  `plans/round94_freeze_integrity.py` (gate v2: `--full-history`, one table block, duplicate rows
  refused, 15-case in-process battery), `plans/round94_c2_counter.py` (W1–W5; W5 = seven CLI-path
  mutants K1–K7 + null copy). Dry runs `dryrun-1.txt`, `dryrun-2.txt` (7/8 mechanism predictions
  held; C08 refuted).
- P2 controls executed against P1: `74b3d2a1e88112763a06a2bdbdfb7ee14a531f55`
  (`.ufo/waves/round-94/L1/controls/README.md` tabulates all 19 receipts: do-nothing, forgeries,
  member swap, sandbox outage, positive control, the five known false gates, the round-93 gate,
  and the BEFORE receipts of the frozen round-93 counter).
- F frozen claims with an 11-row `frozen-instruments` table: `844c504e5147ce767a146af98e4d9b2cacb4258d`.
- C official receipt (`corpus/evidence/round94/compressor-probe.txt`, 8/8 `ok=True`, mismatches 0),
  ledger flip, SOURCES S297–S302, host observation `corpus/evidence/round94/decomp-opt-divergence.txt`:
  `90c7677f0ba95d0930d93bda6a14aa50605ebe2e` = measured tip T for both counters.
- Counter receipts at T: `242b3669176876f076914011d057fd559a37177c`
  (`.ufo/waves/round-94/L1/c1-tip.txt` rc 0; `c2-tip.txt` rc 0).
- Wave w1 spec + validator dispatch: `d04e6664c4fc5d7bf5ce39cab3d22b77001c9e97`; integration after
  WAVE-DONE: `a618227e4c4d09a04c1f613fc5e5cf9f298a12ef` (lesson, QUALITY Q75/Q76
  `corpus/QUALITY.md:1390-1391`, SCORECARD `SCORECARD.md:4345` section + capability row
  `SCORECARD.md:575`, SKILL registry row `SKILL.md:698`, LOG `LOG.md:3565`, S299 correction, wave
  evidence, end receipts).
- Conformance items from the round-93 closure (no claim slot): registry row (`SKILL.md:698`),
  `## Capabilities` row (`SCORECARD.md:575`), SELFTEST echo (C2 W3 `W3 echo SELFTEST cases=15 ok=15`).
- Planner seat: held by the L1 (validator rejects `planner`); no planning data-walk was delegated.

## Landed changes

| commit (landed, remote-verified) | change | LOG entry |
|---|---|---|
| `bdcb1ec06434adfdea25823a2fb90f33bcf1dc5c` | P0 predictions, write-compressor capture, census-start receipt | `LOG.md:3565` (order line) |
| `997a6fe5fbb4a4af9f38e436bccd8f604da1d746` | P1 instruments + dry-run receipts + draft-counter bytes | `LOG.md:3565` |
| `74b3d2a1e88112763a06a2bdbdfb7ee14a531f55` | P2 controls | `LOG.md:3565` |
| `844c504e5147ce767a146af98e4d9b2cacb4258d` | F `plans/round-94-claims.md` | `LOG.md:3565` |
| `90c7677f0ba95d0930d93bda6a14aa50605ebe2e` | C receipt, ledger flip, SOURCES S297–S302, divergence observation | `LOG.md:3565` R94-C1 / Sources bullets |
| `242b3669176876f076914011d057fd559a37177c` | counter receipts at T | `LOG.md:3565` R94-C1 / R94-C2 bullets |
| `d04e6664c4fc5d7bf5ce39cab3d22b77001c9e97` | w1 spec, dispatch, registry | `LOG.md:3565` Wave bullet |
| `a618227e4c4d09a04c1f613fc5e5cf9f298a12ef` | integration: lesson, Q75/Q76, SCORECARD, SKILL, LOG, S299 9→10 words, w1 evidence (9 seat dirs), results, end receipts | `LOG.md:3565` Conformance / Mistakes / Wave bullets |

## Before → after measurements

**R94-C1 (coverage)** — counting command:
`python3 plans/round94_c1_replay.py --lane . --rev 90c7677f0ba95d0930d93bda6a14aa50605ebe2e --work DIR`
- Before (BASE `0cbb9279`, `controls/c1-base.txt`): `LEGS L1..L9=fail`, `TARGET executed_rows=37 member=write-compressor located=0 executed=0 cases=0 legs=0 …`, `PREDICATE R94-C1 fail`, rc 1.
- After (T `90c7677f`, `c1-tip.txt`): `LEGS L1=pass … L9=pass`, `TARGET executed_rows=38 member=write-compressor located=1 executed=1 cases=8 legs=32 mismatches=0 defects=0`, `PREDICATE R94-C1 pass`, rc 0.
- Ledger: executed 37 → 38 of 88; `file-artifact` 28 → 29 of 76; `stdout-inspection` 12 → 13 of 29; `subprocess-exec` 14 → 15 of 45; set = BASE ∪ {write-compressor}.
- Controls: ledger-only flip rc 1 (only L7 passes); class-matched swap rc 1 (L7 fails on the set); `--bwrap /nonexistent/bwrap` rc 2.
- Self-verdict: **met on its frozen predicate**, scoped "at the grader's pinned compile on this host" (wave W-7: gcc `-O3` flips 3 of 8 vectors). Critic: "verifies, narrowed".

**R94-C2 (calibration)** — counting command:
`python3 plans/round94_c2_counter.py --lane . --rev 90c7677f0ba95d0930d93bda6a14aa50605ebe2e --work DIR`
- Before (BASE, frozen round-93 counter, `controls/before-r93-counter-*.txt`): the 5 known false gates x-head-not-rev, x-diff-rev-minus-1, x-table-at-rev, m06, m13 each → `PREDICATE R93-C2 pass`, rc 0 → **5 pass**. Round-94 counter at BASE (`controls/c2-base.txt`): 0 of 5, rc 1.
- After (T, `c2-tip.txt`): `W1 pass` (r92 `(4, 1, 3)`, r93 `(9, 9, 0)`), `W2 pass fixtures=12 ok=12`, `W3 pass` (SELFTEST 15/15 echoed ×2), `W4 pass freeze=844c504e5147 rc=0 summary=(11, 11, 0)`, `W5 pass mutants=7 killed=7` (null 12/12), `TARGET legs_passed=5 of 5`, `PREDICATE R94-C2 pass`, rc 0. The 5 false gates through it: rc 1 each, designated fixture RED (`controls/c2-false-*.txt`) → **0 pass**.
- Self-verdict: **met on its frozen predicate.** Critic dissent on record: "does not verify as calibration" — the 5 → 0 is confounded (each false gate also fails v2-only fixtures and W3) and in-sample. The wave built ≥ 9 new false gates that pass the frozen counter 5/5 (lesson W-2, W-3): the counter discriminates against the recorded set, not in general. Reported, not prettified; the operator/closure rules.

Harm check (not claims): hermetic `grader.py` `VERDICT: PASS`; `plans/state_check.py` PASS;
`plans/round68_capability_table.py` `PREDICATE R68-A3 pass`; `plans/round91_f1_counter.py` pass;
`plans/anchor_line_check.py` `live=0 cells=0` rc 0 (`.ufo/waves/round-94/L1/lane-gates-end.txt`,
`anchorline-end.txt`). At T the anchor gate was red (S299, lesson M1) and was restored by the
after-T SOURCES correction in `a618227e`. Legacy `plans/round79_c1_population_ledger.py --rev`
already fails at BASE (13 defects); T adds one `RECEIPT-UNTRACKED write-compressor`, the same kind
round 93 added (receipt kept in `evidence`, gate reads a `receipt` key) — disclosed, routed to
round 95 (`SCORECARD.md` round-94 "Legacy gate note"). Other axes held: novelty 8, depth 10,
operability 10, freshness 10, adjacency 9.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`.
  Round start: `kengaku ok`, exit 0, 288 rows (`.ufo/waves/round-94/L1/census-start.txt`).
  Round end: `kengaku ok`, exit 0, 294 rows (`census-end.txt`; pre-existing W04 duplicate-url warnings only).
  Row count: `grep -c '^| \?S[0-9]\+ ' corpus/SOURCES.md` 288 → 294.
- Rows added by tier: tier A ×6 — S297 (grader), S298 (decomp.c), S299 (data.txt), S300 (solve.sh) **admitted / mined**; S301 (test.sh, byte-identical to S294) and S302 (Dockerfile) **rejected** with flips (`corpus/SOURCES.md:313-318`).
- Rows touched old → new: S299 anchor word count `(9 words)` → `(10 words)` (same-round row; lesson M1). No status/recheck/used-by change to earlier rows.
- Frontier rows advanced: ledger member `write-compressor` unexecuted → executed (round 94).
- Sourced claim: R94-C1 rests on S297–S300 (opened 2026-11-05; Gate block with ≤25-word located quotes in `corpus/lessons/round-94.md` `## Gate`).
- Mistake mined: `corpus/lessons/round-94.md` `## Mistakes` M1–M4 (M1 captured-by `plans/anchor_line_check.py`, shown able to fail at T; now QUALITY Q76).
- Assimilation: none (`merge/kengaku/` held by open L0 `kengaku | round-54`). considerthese: none taken (2026-11-05 proposal 2 named as the gate's residual; not implemented).

## Trend verdicts

- **expansion: improved** — population frontier 37 → 38 of 88 with three class-cell moves, and 4 admitted tier-A rows on a member the corpus did not hold (S297–S300); the grader findings C04/C06/C08 and the `-O3` divergence are new knowledge about this member.
- **quality: unchanged** — no admitted `knowledge/` entry was superseded or re-verified; the S299 correction fixed a row written this same round.
- **discernment: improved** — two rejects with flip conditions (S301, S302); Q75 (scoped by the wave) and Q76 are new criteria grounded in mistakes M2 and M1; the non-author wave's dissent on C2 is recorded beside the self-verdict, not overwritten.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:698` (new `freeze-integrity` registry row in the gate table at `SKILL.md:592`)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:3565` (write-compressor replay, receipt `corpus/evidence/round94/compressor-probe.txt`)
- [~] Instructions executable by an agent without oral context — `plans/round-94-claims.md` (each predicate is one command; controls README `.ufo/waves/round-94/L1/controls/README.md`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `.ufo/waves/round-94/w1/ConnectorOverlap.md` (no sibling replays TB2 graders; kaidoku/mado freeze-gate overlaps are complements, cross-cited, not absorbed)

## Round shape, seats, extras

- Shape: ONE v1 wave `w1` (policy `scripts/hyaku/ufo-wave-policy.json`, band 8–16), 12 seats, no residual call; round total 12.
- Role mix: 3 executor, 1 scout, 1 connector, 1 scribe, 2 reviewer, 1 critic, 2 mutation-tester, 1 sentinel; attack share (reviewer, critic, mutation-tester) 5/12 = 42 %; connectors 1.
- Dead seats (3, not replaced): ScoutSources (scout), ReviewerC1 (reviewer), ReviewerC2 (reviewer) — empty final output, no file, results `note` null (`.ufo/waves/round-94/w1-results.json`). The live source re-open was still covered by CriticClaims (`receipts/source-fetch-S297-S302.txt`) and ScribeQuality (`receipts/receipt-sources-s297-s302.txt`).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` → `.scratch/*` (orchestrator-owned) and `w4lines.txt` (created 16:57 -03, before this round's launch at 18:47, no kengaku content) — not this round's; untouched. No misroot.
- Open L0 questions: none new this round. Existing kengaku L0s (rounds 54, 90–92) routed around.
- Tool installs: none (L1 and every seat that reported).
- Scratch: `/fast/scratch/hyaku/kengaku-r94` removed after landing.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
