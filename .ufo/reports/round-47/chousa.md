# chousa — round 47 report (hyaku run 6, in-session L1)

Lane: `/home/vgpnk/Projects/shokunin/chousa-shokunin` · lane branch `master`
Base: `9a9f94dbcb010eca6636886e53950f38ca806329` · freeze:
`22a44b8b5c923d25123a96a852c11938559bb9b2` · landings: C1 `a15610a59aaeaf43b79ccc650acee4bd4da00341`
+ `980fe43fc885f1c2b6c8394fb50745b856c63f15`, C2 `7fb9a2321da78cf1a1b94dbe08c533461dbfd778`,
C3 `3d2a0637fd583260be6a51e0024f337f5592e3f3`, record `1fc5ed193ad48a482402c862f4e4cc47e46d5b2d`
· final lane tip: `900c72eca0f4f4d5bdfbd2c9c25cc8c149f88561` (`git ls-remote origin refs/heads/master` prints it)

Declared claims (frozen in `corpus/evidence/round47/claims.md` before any seat scored,
with their do-nothing controls): **C1 operability** (the lowest non-retired axis, 3/10) —
the inference check refuses a windowed stem-sharing polarity flip, a capability
acquisition (round-46 named limit "entailment", the D7 class); **C2 calibration** — the
gate registry agrees with the tree its own checks depend on, as a mismatch count
(round-46 named limit "mention, not dependence"; closure routed defects 2 and 4);
**C3 depth** — the claim-support-test theme adopted from the shokuknow package by
document, with anchor cells bound to located quotes (round-46 named limit "anchor
cells"; routed defect 5). C3 is the round's sourced claim (S090–S094 opened this round).

## Work performed

- **C1 — polarity probe.** `tools/inference-ground.py` rule 5 (`INF_POLARITY_FLIP`):
  a phrase its span negates, reused in the bullet's own words without a negator nearby;
  an affirmed phrase the bullet negates or `un`-prefixes; a counts figure whose next words
  disagree with its key. Three positive and three junk fixtures in
  `corpus/fixtures/inference-ground-r47/`, byte-pinned, plus CANARY, round-46-counter and
  round-46-entry no-regression legs (`corpus/evidence/round47/c1-count.py`). Wave 1 found
  the first version refused 9/10 correctly-reasoned bullets
  (`.ufo/waves/round-47/w1/LabC1FalsePos.md`) and was order-dependent
  (`ReviewerC1Polarity.md` M4); refinements landed at `980fe43f` (lesson mistakes 4–5).
  Evidence: `corpus/evidence/round47/measure-after.txt` (`C1=PASS` exit 0).
- **C2 — dependence-and-check registry count.** `corpus/evidence/round47/c2-count.py`
  imports the pinned round-46 set and adds a dependence closure, the QUALITY/SKILL
  check-named leg, entry-cell and exit-code roles, DANGLING rows and FLOOR=92 in code.
  Thirteen `SKILL.md` Gates rows added or repaired (four QUALITY checks, three wave
  instruments, `mechanism-witness` pipe repair, the controls row's exit codes plus three
  base gates, the round-29 counter, the round-26 oracle, the round-47 counters and span
  builder). Wave 1 found the freeze counter's escaped-pipe split, `exit`-substring test,
  `./` padding, missed `$SCRIPT_DIR` call and a `.pyc` pin bypass
  (`ReviewerC2Set.md`, `MutC2Forge.md`, `CritC2Framing.md`, `SentScopeAudit.md`);
  repaired toward the literal sentence and disclosed (lesson mistake 3). Evidence:
  `measure-after.txt` (`MISMATCHES=0 C2=PASS` under both the final and the freeze-time
  counter).
- **C3 — two entries, five new rows, one re-bound row, 35 spans.**
  `corpus/knowledge/claim-support-test-r37.md` (S085, S090, S091) and
  `…-r37-amendment-2026-10-23.md` (S092, S093, S094), drafted by
  `ScribeEntryBase`/`ScribeEntryAmend` from the captures and edited by the L1 (the
  PEOPLEPROFILES model-agreement figure left to kengaku). `corpus/evidence/round47/build-spans.py`
  builds `spans.tsv` from `quotes.tsv`; Registry anchor cells are generated from it.
  Six sources re-opened (`ReviewOpenS085…S094.md`), four quarantine rows hand-checked
  `present` (`QuarReg093/094/108/110.md`). Evidence: `measure-after.txt` (`C3=PASS` both modes).
- **Frontier step.** `corpus/SOURCES.md` 89 → 94 rows; `corpus/lessons/round-47.md`
  `## Mistakes` (nine mined, each with captured-by and fix); QUALITY 67 (polarity) and 68
  (per-round receipt re-verify, mined from `considerthese/2026-10-24.md`); coverage map +2.
- **Round-46 closure routed defects** (`corpus/lessons/round-46-verifier-spotcheck.md` §6):
  1 freeze-time sentence/code gap — this round froze the counters with the claims and
  disclosed every later instrument edit (lesson mistake 3); 2 kill floor — enforced in
  code (C2 FLOOR=92); 3 stale control receipt labels — refreshed receipt
  `corpus/evidence/round47/r46-c2-controls-refresh.txt` (ScribeR46Defects); 4 cheap-gate
  residue — entry-cell roles and exit-code pattern (C2), the one-junk-row forge stays a
  named limit; 5 anchor drift — S085 `char 2349` → `2360`/`1271`, `ANCHOR_BOUND=6/6` (C3);
  6 report wording — corrected here: the round-46 seat `CritC2Scope`'s report IS
  committed (lane `5c6e2ca`); it did not die. No disagreement was routed (all four
  spot-check rows AGREE), so no QUALITY criterion was required by it.

## Landed changes

Every change is under the LOG.md entry `## Round 47` and was landed by
`scripts/hyaku/jj-lane.sh` (`landed <hash>` after remote verification):

| commit | what |
|---|---|
| `22a44b8b` | freeze: claims, three counters, C1 fixtures, controls and before receipts, assimilation collision check and guard proof |
| `a15610a5` | C1 polarity probe |
| `980fe43f` | C1 refinements after wave 1 |
| `7fb9a232` | C2 Gates rows and counter repairs; re-measured C2 receipts |
| `3d2a0637` | C3 entries, rows, spans, lesson, QUALITY 67–68, coverage map |
| `1fc5ed19` | SCORECARD/LOG/SKILL rows; `.pyc`-safe C2 pin; refreshed round-46 receipt; wave-1 evidence |
| `02d95d32` | C1 wave-2 fixes (span-side explicit negators, leaf-key polarity, `un` flip after a negator, latent false negators excluded) |
| `b8bc06c6` | wave-2 corrections: entry narrowings, `q33-check` self-test cell, QUALITY 67 limit, SCORECARD numbers and the disputed C1 axis; wave-2 evidence (34 reports) |
| `11ead577`, `900c72ec` | after-measurement receipt over a `git archive` of `b8bc06c6` (the second run fixes the freeze-time counter's placement in the receipt) |

## Before → after measurements

| claim | counting command | before (commit) | after (commit) |
|---|---|---|---|
| C1 | `python3 corpus/evidence/round47/c1-count.py` | `POSITIVE_PASS=3/3 JUNK_KILLED=0/3 CANARY=fail R46_COUNTER=pass R46_ENTRIES=2/2 C1=FAIL` exit 1 (freeze `22a44b8b`, `controls/c1-before.txt`) | `3/3 3/3 CANARY=pass R46_COUNTER=pass R46_ENTRIES=2/2 C1=PASS` exit 0 (`b8bc06c6`, `measure-after.txt`) |
| C2 | `python3 corpus/evidence/round47/c2-count.py --list` | freeze tree `MISMATCHES=25` (freeze counter) / `21` (final counter); bare base `22` / `18` (`controls/c2-before.txt`) | `ENTRY_POINTS=94 REGISTERED=94/94 UNREGISTERED=0 DANGLING=0 MISMATCHES=0 C2=PASS` exit 0 (FLOOR=92 met); freeze-time counter `REGISTERED=93/93 MISMATCHES=0 C2=PASS` exit 0 (`b8bc06c6`) |
| C3 | `python3 corpus/evidence/round47/c3-count.py` (and `--lane-only`) | `ENTRIES=0/2 CITES_BOUND=0/6 ANCHOR_BOUND=0/6 INFERENCE_GROUNDED=0/2 QUARANTINE_VERDICTS=0/4 C3=FAIL` exit 1 (freeze, `controls/c3-before.txt`) | every leg full (`QUOTE_ROWS=35 CAPTURE_BOUND=35/35 ANCHOR_BOUND=6/6`), `C3=PASS` exit 0 both modes (`b8bc06c6`) |

Do-nothing controls, committed before data: C1 — the round-46 tool `JUNK_KILLED=0/3`,
always-exit-1 `POSITIVE_PASS=0/3`, negator-word refuser `1/3`; C2 — the round-46 counter
passes the base tree that this counter fails; C3 — the staged entries copied unchanged
fail `REF_ID_UNBOUND=17 CITES_BOUND=0/6`, invented digests fail `CAPTURE_BOUND=0/12`.

## Report extras — round shape, waves, seats

- **Shape:** default, two v1 waves (policy `scripts/hyaku/ufo-wave-policy.json`, band 32–64),
  each validated by `ufo-swarm-wave.mjs run` and dispatched as ONE batched `task` call
  through the eval bridge with the validator's `taskCall` unchanged. No residual call.
- **Wave 1 — build + first falsifiers, 37 seats:** reviewer 12, scribe 10, executor 4,
  critic 4, scout 3, mutation-tester 2, connector 1, sentinel 1
  (`.ufo/waves/round-47/w1-spec.json`, `w1/` 37 reports). The validator refused `labrat`
  as a swarm role, so the false-refusal probe rode a critic seat (`LabC1FalsePos`).
- **Wave 2 — falsify, 34 seats:** reviewer 22, critic 7, mutation-tester 2, executor 1,
  sentinel 1, connector 1 (`w2-spec.json`, `w2/` 34 reports); every item names what it
  attacks (each report opens `ATTACKS:`/`VERDICT:`).
- **Round total: 71 seats. Dead seats: 0** (71 reports). No job-limit refusal occurred.
- **Planner seat:** the L1 held the §3 planner seat (the validator rejects `planner`); the
  bounded planning data-walk rode `ConnectSiblings` (wave 1) and `ConnectR48` (wave 2).
- **Routing:** every seat took the host role table (`task.agentModelOverrides`, global
  `@m_flash`); no `model` was passed. No claim depends on a seat's answering model.
- **Seat scope breaches, recorded:** a wave-2 seat wrote `assimilation/reg-ids.rerun` and
  `staged-ids.rerun` into the lane outside its report (re-derivable, cited by no report;
  discarded, not committed); wave-1 `ExecMirrorCensus` left `/tmp/chousa-r47-ExecMirrorCensus/`
  (deleted by the L1). Misroot sweep of the fleet root (`git status --porcelain`): no
  untracked file names chousa round 47.
- **Earlier attempts:** the watchdog shows no `lane-dead-no-report chousa round=47`; this is
  attempt 1 and inherited nothing from round 47.
- **Inherited tree:** the three modified r40/r41 JSON paths stay left-named and uncommitted
  (bytes unchanged since round 45, `ScoutInheritedTree`); L0 `8d77e6c1` and the chousa
  round-43/44 questions remain unanswered. No `operator-*.md` lesson exists.
- **considerthese:** `considerthese/2026-10-24.md` "Spot re-verify one receipt a week" mined
  as QUALITY 68 (the one unimplemented proposal of the latest file); its first run found
  four round-39/40 receipts failing `gate-sha256-mismatch` since round 41, routed to round 48.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none (no seat reported one).
- **Open L0 questions:** none added this round.
- **Tooling note:** the session's file Read tool refused 4–40 KB files with "exceeds maximum
  allowed characters (100000)"; the L1 and several seats read them through the shell.

## Sources & frontier

- `SOURCES.md` rows **89 → 94** (`grep -cE '^ {0,3}\| S[0-9]{3,} ' corpus/SOURCES.md`).
  Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`:
  round start **exit 0** (89 rows, five pre-existing W04;
  `.ufo/waves/round-47/assimilation/census-start.txt`), round end **exit 0** (94 rows, the
  same five W04; `measure-after.txt`).
- Rows added by tier: **A 5** (S090 PEOPLEPROFILES, S091 CFEVER AAAI-24, S092 FEVER arXiv
  v3, S093 climate-fever, S094 CorFEVER), all `mined`, opened 2026-10-25 from on-disk
  captures, recheck `365d`; URL, access date and ≤25-word located quotes in
  `corpus/lessons/round-47.md` `## Gate`.
- Rows touched old→new: **S085** anchor `char 2349` → `char 2360`/`char 1271`; `used-by`
  `evidence-pool-versioning-r39.md` → `+ claim-support-test-r37.md`.
- Frontier advanced: claim-vs-source verification gains the support test's definition,
  its annotator procedure and per-step reliability; coverage map +2 rows.
- **Assimilation (§10):** one theme (what a support test is, how it is applied, how
  reliable it is), two entries admitted from `merge/chousa/` (`claim-support-test-r37.md`
  and its amendment — the round-46 reject, its flip met), two refused with reason and flip
  (`citation-count-semantics-r37.md`, `search-log-fields-r36.md`). Id lists:
  `assimilation/reg-ids` (89, S001–S089) and `assimilation/staged-ids` (114); **8
  collisions** (S082–S089, each a different document on each side). Renumber map **by
  document** (URL equality): S097 → S085 (held), S098 → S090, S099 → S091, S113 → S092,
  S114 → S093, S115 → S094. Guard proven (`assimilation/guard-proof/`: indented `S097`
  caught, column-0 extraction misses it). Pre-append mirror census exit 0
  (`assimilation/mirror-census.txt`). Quarantine slice re-derived (24 data rows); the four
  rows on this theme's URLs (register S093, S094, S108, S110) hand-checked **present**
  (interleave/markup false negatives), no row refused.
- Sourced claim: C3 cites S090–S094, opened this round.

## Trend verdicts

- **expansion — improved.** Two admitted entries on ground the coverage map did not hold
  (the support definition, the annotator decision rule, per-step reliability), five tier-A
  `mined` rows opened this round; a non-author spot-check is still the closure's.
- **quality — improved.** Three counters pass over committed bytes against committed
  do-nothing controls; thirteen lesson mistakes, each with a fix shown able to fail; wave 2
  corrected four entry sentences and two SCORECARD numbers before landing. The C1 axis
  verdict carries an open dispute (per-axis paragraph below).
- **discernment — unchanged.** Seats this lane dispatched are still the lane; wave 2
  agreed with every admit and both rejects it attacked, and two seats ruled C1 a trade.
  The outside spot-check is the closure's.

Per-axis (from `SCORECARD.md` `## Round 47 verdict`): operability **improved, disputed as a
trade** (held-out: 4/12 flips killed vs 0; 2/12 correct bullets refused vs 0; 0 exit changes
on 63 real entries — wave-2 `CritC1Claim` and `CritScorecard` rule it a trade; operator to
rule); calibration **improved narrowly** (8 real registry mismatches closed; 10 of the 25
were the freeze counter's own parser artifact); depth **improved**; coverage **improved
narrowly**; freshness **unchanged** (captures predate launch); adjacency **unchanged**.
If the operator rules C1 a trade, the round does not meet "no axis harmed" and is not
admitted on C1; C2 and C3 are separable and verify on their own counters.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` `## Gates` (every one of 94 entry points registered, `c2-count.py`); lane assertion, no non-author verifier
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 47` (claim-support adoption re-grounded on six captures); lane assertion
- [~] Instructions executable by an agent without oral context — `corpus/evidence/round47/measure-after.txt` (every counting command re-run over a `git archive`); lane assertion
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `.ufo/waves/round-47/w1/ScoutProvinceFit.md` (PEOPLEPROFILES model agreement left to kengaku); lane assertion
