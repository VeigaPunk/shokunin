# kake — round 100 report (attempt 2, L1 KakeR100a2; fresh start under run-15 amendment 35)

## Work performed

Declared claims (frozen at `69cdc1eb`, `.ufo/waves/round-100/freeze.md`, before any seat ran):
**C1 — calibration** (score 3, lowest owned non-retired axis): one SKILL.md registry row per committed
`scripts/` tool, with verdict maps checked by executing each tool. **C2 — freshness (HOLD 10),
capability acquisition, sourced (S486, S487)**: 304 freshening contract v2 in `scripts/freshen_304.py`.

- Attempt 1 (L1 KakeR100) loaded the protocol, froze the claims with do-nothing, forgery and positive
  controls, landed the instruments `d7b73d16`, the freeze `69cdc1eb`, the C1 repair `e84a1871` and the
  C2 content `06c81f08`, and dispatched w1 (`w1.ready.dispatched` 22:46:35). Then it died
  (`.ufo/watchdog.log` `lane-dead-no-report kake round=100` 23:31:17).
- Inherited and reused after a re-check (attempt 2): all 13 seat reports on disk; `controls/after-c1.txt`
  and `controls/after-c2.txt` (reproduced by CriticClaims baselines and by ReviewDeterminism `3/3`
  identical); `controls/tip-c1-at-c2.txt` and the two post-freeze disclosures; the `assimilation/`
  scratch; the modified `make_spec_w1.py`, whose LabratDeterminism→ReviewDeterminism rename matches the
  dispatched `w1-dispatch.json`. Discarded: nothing. ScribeLesson was lost with the crashed
  orchestrator session and wrote no report, so the L1 wrote the lesson.
- C1 counter `c100_registry.py` before → after (`controls/base-c1.txt` → `controls/after-c1.txt`).
  Review conjunct: `w1/ReviewRegA/verdicts.tsv` 8 agree, `w1/ReviewRegB/verdicts.tsv` 8 agree, of 8
  units each. ExecRegProbe ran an independent probe and found `not_one_row=0 probe_contradictions=0
  history_verbatim=7/7` (`w1/ExecRegProbe/report.md`).
- C2 counter `c100_fresh304.py` before → after (`controls/base-c2.txt` → `controls/after-c2.txt`).
  ExecTwinFresh ran 3600 independent inputs with 0 disagreements (`w1/ExecTwinFresh.md`). ReviewFresh
  found 43/43 agree and 0 RFC contradictions, with findings G1-G3 (`w1/ReviewFresh.md`).
- Attacks (routed, not repaired, nothing re-scored): CriticClaims `c1_escapes=6 c2_escapes=5
  framing_defects=3` (`w1/CriticClaims.md`); MutCounters registry 8/15 and fresh304 13/17 mutants
  killed, 11 survivors (`w1/MutCounters.md`); SentinelScope `vectors=28 escapes=0 cross_case_leaks=2`,
  where R1/R3/R4/R12 show the C1 counter can be driven to met by a hostile tree (`w1/SentinelScope.md`).
- Held-out checks added by attempt 2 after the freeze (reported, not scored):
  - `controls/post-freeze-heldout-c1-gaming-scan.txt`: no committed tool names the probe token or
    calls `getpid`, and the repair changed no tool.
  - `controls/post-freeze-heldout-critic-probes-landed.txt`: the landed candidate matches the frozen
    oracle on 4/4 of the CriticClaims X1-X5 probe inputs.
- Integration: knowledge entry `corpus/knowledge/freshening-304.md` replaced with the ScribeEntry draft
  (44 quotes, lint 0; `knowledge_metatext_lint.py --dir corpus/knowledge` `gate_findings=0`); README
  section `## Round-100 frontier step`; QUALITY.md §Round 100 R100-A; SCORECARD round-100 section and
  calibration row 3 → 4; LOG entry; lesson `corpus/lessons/round-100.md`.
- Round-99 spot-check routes R99-C1 (C1 re-entry with verdict cells derived from code), R99-C2
  (isolated candidate runner) and R99-C3 (contract v2) are carried by C1, by the C2 sandbox and by
  C2 (freeze.md lines 10-26 and 60-69).
- Inherited files I did not author: `corpus/lessons/round-99-verifier-spotcheck.md`, read and not
  edited.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Instruments (both counters, contract v2, frozen oracle and forgeries, RFC 9110 body, census before) | Round 100 bullet 1 | `d7b73d16` |
| Freeze with pre-freeze controls | Round 100 bullet 1 | `69cdc1eb` |
| C1 repair: SKILL.md one row per tool, seven old rows kept in a fenced history block | Round 100 bullet 2 | `e84a1871` |
| C2 content: `scripts/freshen_304.py` contract v2, registry row, SOURCES S486/S487 | Round 100 bullets 3-4 | `06c81f08` |
| Integration: w1 evidence, lesson, SCORECARD/LOG, knowledge entry, README, QUALITY R100-A, census after, held-out receipts, considerthese p5 triage | Round 100 bullets 3-6 | `2bdec5f8` |
| w1-results.json and the seat-yield line | Round 100 bullet 6 | `72a6cd60` (lane tip; `git ls-remote origin refs/heads/master` = `72a6cd6018b68a7f633e216bdcb164c2eec8d22e`) |

## Before → after measurements

- **C1**, counted with `python3 -B .ufo/waves/round-100/c100_registry.py --root . --revision <REV> --work <scratch>`:
  - At `3989618d`: `tools=55 … duplicated=7 probe_mismatch=2 exec_fail=1 mismatches=9 met=false`, exit 1.
  - At `e84a1871`: `tools=55 rows=146 listed=55 unlisted=0 dangling=0 duplicated=0 probe_mismatch=0
    exec_fail=0 mismatches=0 met=true`, exit 0.
  - Review count, `cut -f2 .ufo/waves/round-100/w1/ReviewReg{A,B}/verdicts.tsv | sort | uniq -c`:
    16 agree, 0 disagree.
  - Pre-freeze do-nothing and forgery controls: `deleteall` and `keepold` both `met=false`.
  - **Verdict: met on the frozen predicate.**
- **C2**, counted with `python3 -B .ufo/waves/round-100/c100_fresh304.py --root . --revision <REV> --work <scratch>`:
  - At `3989618d` (the v1 blob): `hand=72/91 generated=224/300 met=false`, exit 1.
  - At `06c81f08`: `candidate=present sha256=00edf6c4… hand=91/91 generated=300/300 refusals=122/122
    met=true`, exit 0. The scored sha256 equals `git show 06c81f08:scripts/freshen_304.py | sha256sum`.
  - Pre-freeze controls: all 13 single-mutation forgeries and the oracle-theft forgery give
    `met=false`.
  - **Verdict: met on the frozen predicate.**

## Sources & frontier

- **Census.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`:
  - Before: exit 0, 41 W04 (`controls/census-before.txt`).
  - After: exit 0, 43 W04 (`controls/census-after.txt`).
- **Rows.** 222 → 224 (`grep -c '^| S' corpus/SOURCES.md`). Two tier-A spec rows were added:
  - S486: RFC 9111 §5.2, §5.2.2.4, §5.2.2.7 and §5.2.3.
  - S487: RFC 9110 §5.5, §5.6.1.2, §5.6.2 and §5.6.4.
  - Both were opened 2026-11-06. ScoutSources re-opened both with HTTP 200, byte-identical to the
    retained bodies. The Gate in `corpus/lessons/round-100.md` holds the URLs, access dates and
    located quotes.
- **Rows touched:** none (no `status`, `recheck` or `used-by` change on older rows). The two new W04
  warnings are duplicate URLs with S484 and S466 whose scopes do not overlap.
- **Frontier rows advanced:** Cache-Control argument grammar and field-value trimming moved into
  core, behind the contract-v2 capability.
- **Sourced claim:** C2 rests on S486 and S487.
- **Mined mistakes** (lesson `## Mistakes`):
  - M1: masking by an any-row-conforms rule.
  - M2: a stale "unimplemented" considerthese pick. The fix grep was shown to fail twice.
  - M3: the attempt-1 L1 died after dispatch.
- **Assimilation: none.** Collision check: `reg-ids` 222, `staged-ids` 129, `collisions` 8 (S312 S329
  S367 S372 S373 S374 S390 S409). The guard was proven on an indented `  | S002 |` fixture, which gave
  `guard-collisions` = S002. There is no renumber map. The quarantine slice has 12 rows, not
  hand-checked, so adoption stays closed.
- **considerthese.** `2026-11-05.md` proposal 5 (branch triage) was mined, receipt
  `.ufo/waves/round-100/considerthese-p5-branch-triage.txt`. Nothing was adopted; follow-up is routed
  as R100-5. Proposals 2, 3 and 4 were already landed (R98-B, R95-D, R99-A).

## Trend verdicts

- **expansion: improved.** Two new tier-A rows, and contract-v2 ground (Cache-Control grammar, value
  trimming) that the lane did not hold before (`corpus/README.md` §Round-100).
- **quality: improved.** Both frozen predicates are met and beat their do-nothing controls. A
  held-out check sits beside each `met` line (R95-D). Instrument defects are recorded as R100-A and
  routes R100-1…4, not hidden.
- **discernment: unchanged.** Merge/kake adoption was refused again with re-derived collisions. No new
  outside spot-check ran inside this round; the closure judges it.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md`
  registry at `e84a1871` (`controls/after-c1.txt`); ledger row `box 1`.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — ledger row `box 2`
  `status=gap`. Untouched this round.
- [~] Instructions executable by an agent without oral context — `controls/after-c1.txt`
  (`exec_fail=0`); ledger row `box 3`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — ledger row `box 4`; the new entry cites
  only lane paths and RFCs.

## Round shape and extras

- **Shape.** One v1 wave `w1` of 14 seats (`ufo-wave-policy.json`):
  - Roles: scout 1, connector 1, executor 3, scribe 2, reviewer 4, critic 1, mutation-tester 1,
    sentinel 1.
  - Attack share 6/14 (43 %).
  - No residual call. Round total: 14.
  - The L1 held the planner seat.
- **Seat yield: 13/14, attack 6/14.** ScribeLesson was lost with the crashed orchestrator session and
  produced no report. Every `w1-results.json` output is null, so results were read from the reports on
  disk. No other seat died; I have no error text for ScribeLesson.
- **Stale-lane:** respawn-per-round driver. No other mission of this lane is open. Round 100 is the
  lane's last training round (amendment 38).
- **Tool installs:** none (pacman paused; none needed).
- **Misroot sweep:** `git status --porcelain` on the fleet repo shows only `w4lines.txt` (16:57, no
  kake content). It belongs to another lane and was not touched.
- **Scratch:** `/fast/scratch/hyaku/kake-r100` removed. It held leftovers from the ExecFresh,
  ScribeLesson and attempt-1 L1 dirs, which those seats should have removed themselves.
- **Open L0 questions:** none new; R95-2 is carried.
