# kotoba — round 94 report (attempt 1, L1 KotobaR94; Linux host, omp)

Lane repo: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, branch `master`. Pushed lane tip at report time: **`b623b420bdc8c3d9eecc10ff213ca749d5942ad0`** (`git ls-remote origin refs/heads/master` = this hash; `jj-lane.sh state` → `ahead=0 behind=0 tracked=0 untracked=0`). Round base: `4d3e8e4d290d67ecf94a019059f434c71f399919`. Freeze: `edc731a91a956f6df20c27a74fb981b286f6ba58`. Landing (code + corpus): `f65347a664a9286fecfc41c9e429609bc5b2b284`. Record: `8068e32ee9bba07d23b9c733cbfafe0dfffa1d4b`. Wave evidence: `b623b420…` (the tip).

## Work performed

**Declared claims (2, on distinct axes, frozen before any data in `plans/round-94.md` at `edc731a9`):**

- **C1 — depth (the lowest owned non-retired axis; score held at 9).** The mutation battery's `--self-test` now kills the three round-93 kill-pin gaps: k1 reads the working-tree manifest (MutTesterKillPin m3/F1), k2 labels every could-not-evaluate line `arm kill-set-size:` (m6/F4), and k3 accepts a kill-row count above the pin (F2). The claim is sourced on S269 (PIT basic concepts). My measured reading at `f65347a6`: **MET**.
- **C2 — consistency (calibration sub-axis; score held at 10).** The tip battery's `--self-test` now checks every BATTERY pin key. Two mutants are killed: p1 hardcodes coverage to one key (round-93 MutTesterPinCov m5, closure defect 1), and p2 skips the first key. My measured reading at `f65347a6`: **MET**.

Work items:

1. **Freeze (`edc731a9`).** Committed together: the plan, a shared frozen counter `verifiers/fixtures/round-94/selftest-kills.py`, a forgery `verifiers/fixtures/round-94/forgery-sniff.patch`, and the pre-data receipts.
   - The counter runs the self-test three ways: unmodified (honest), once per literal-anchor mutant (the anchor must match, the mutant must compile, a timeout is could-not-evaluate), and once per comment **decoy**, which guards against sniffing.
   - Do-nothing at the base: `receipts/redbefore-c1-base.txt` reads `C1 targets killed 0 of 3; positive killed 1 of 1; honest rc 0; decoys held 3 of 3`, UNMET, rc 1. `redbefore-c2-base.txt` reads `0 of 2`, UNMET, rc 1.
   - Forgery (a self-test that sniffs its own source): `receipts/forgery-c1-run.txt` reads targets 3 of 3 but `decoys held 0 of 3`, UNMET. `forgery-c2-run.txt` reads `decoys held 0 of 2`, UNMET.
   - Census at round start: `receipts/census-before.txt`, rc 0.
2. **Wave `r94-w1`.** One v1 wave of 12 seats, under `.ufo/waves/round-94/`: `gen-w1.py`, `r94-w1-spec.json`, `r94-w1-dispatch.json` (`counts.spawn = 12`), `r94-w1.ready` / `.ready.dispatched`, `r94-w1-results.json`, and seat outputs in `w1/`. Every seat prompt leads with `/skill:godspeed` plus the binding's directive bytes. The context also requires each seat to write its report file before its final answer (round-93 closure defect 4). All 12 seats wrote one.
3. **Builders:**
   - ExecBatterySelfTest (`w1/ExecBatterySelfTest/ExecBatterySelfTest.patch`, C1): 7 behavioural arms, 31 → 38 assertions.
   - ExecTipSelfTest (`w1/ExecTipSelfTest/…patch`, C2): six per-key keydrop worlds, 80 → 102 assertions.
   - ExecReceiptHeaders (`w1/ExecReceiptHeaders/…patch`): the mined-mistake fix (MALFORMED rule plus `good/`, `hex41/`, `indented/` fixtures).
   - ScribeCorpusR94 (`w1/ScribeCorpusR94/…patch`): S269, the lesson scaffold, and the README row.
   - ScoutMutSources (`w1/ScoutMutSources.md`) and ConnectorOverlapR94 (`w1/ConnectorOverlapR94.md`).
4. **Attack seats:**
   - ReviewerBatterySelfTest (`w1/ReviewerBatterySelfTest.md`): no blocking finding. It applied each mutant by hand and named the behavioural assertion that fails.
   - ReviewerTipSelfTest (`w1/ReviewerTipSelfTest.md`): no blocking finding; F1–F4 are non-blocking.
   - MutTesterBattery94 (`w1/MutTesterBattery94.md`): 12 new mutants, 8 killed. Survivors: N1, N4, N5, N11. It also built a tokenize-based sniffer that meets C1 under the counter.
   - MutTesterTip94 (`w1/MutTesterTip94.md`): C2 n1 is newly killed. In the receipt-check fix, r1 (39-hex) and r4 survived.
   - CriticClaimsR94 (`w1/CriticClaimsR94.md`): C1 and C2 MET on its candidate. It raised defects D1–D8, including D4: a comment-skipping sniffer meets C1.
   - SentinelScopeR94 (`w1/SentinelScopeR94.md`): scope, no-harm and safety all PASS.
5. **Integration (`plans/round-94-addendum-1.md`, record `8068e32e`).** No frozen predicate, counter, kill rule or target changed.
   - **A1** repairs the mined-mistake fix for Critic D1 (a scratch-tagged malformed header) and D2 (a second declaration on a header line). It also adds the `hex39/`, `scratch-hex41/` and `double-decl/` fixtures (MutTesterTip94 r1). Each reads rc 1 (`receipts/landing/receipt-hdr-*-a1.txt`).
   - **A2** discloses that the decoy guard misses comment-skipping sniffers (D4).
   - **A3** discloses that S269 shares S262's URL and does not ground the timeout rule (D7).
   - **A4** covers the C2 label (D6).
6. **Landing measurements** at the committed revision `f65347a6` (`receipts/landing/landing-rev.txt`), listed in the measurements section below.
7. **Frontier step:** S269 opened and appended; two same-round rejects; mined mistake `receipt-header-fail-open`, with a fix shown able to fail (`corpus/lessons/round-94.md` § Gate, § Mistakes, § Settlement).

## Landed changes

| change | commit | LOG.md / record |
|---|---|---|
| freeze: `plans/round-94.md`, `selftest-kills.py`, `forgery-sniff.patch`, pre-data receipts | `edc731a9` | LOG § Round 94 (claims as frozen; pre-data controls) |
| C1: `verifiers/check_mutation_battery.py` (self_test arms only; production code unchanged) | `f65347a6` | LOG § Round 94 (landing) |
| C2: `verifiers/check_tip_battery.py` (self_test only) | `f65347a6` | LOG § Round 94 (landing) |
| mistake fix: `verifiers/fixtures/round-93/check-receipt-revs.sh` MALFORMED rule + `verifiers/fixtures/round-94/receipt-headers/{good,hex41,indented}` | `f65347a6`; A1 repair + `{hex39,scratch-hex41,double-decl}` in `8068e32e` | LOG § Round 94 (integration A1) |
| corpus: `corpus/SOURCES.md` S269 (194 → 195), `corpus/lessons/round-94.md`, `corpus/README.md` row | `f65347a6`; lesson settlement in `8068e32e` | LOG § Round 94 (frontier step) |
| `plans/round-94-addendum-1.md`, LOG § Round 94, SCORECARD round-94 annotations + round-95 intentions | `8068e32e` | LOG § Round 94 |
| wave evidence `.ufo/waves/round-94/` (spec, dispatch, ready, results, 12 seat outputs, landing + A1 receipts) | `b623b420` | LOG § Round 94 (wave) |

Unchanged: SKILL.md (600 lines; `git diff --stat 4d3e8e4d b623b420 -- SKILL.md PROVINCE.md` is empty), the battery manifest, the round-91 and round-92 fixtures, and every `round-*-verifier-spotcheck.md`.

## Before → after measurements

**C1 — depth.** Counting command: `python3 -B verifiers/fixtures/round-94/selftest-kills.py c1 <rev>`, frozen at `edc731a9`.
- **Before** (base `4d3e8e4d`, `receipts/redbefore-c1-base.txt`): `C1 targets killed 0 of 3; positive killed 1 of 1; honest rc 0; decoys held 3 of 3` → `C1-PREDICATE-UNMET`, rc 1.
- **After** (`f65347a6`, `receipts/landing/c1-counter.txt`): `C1 targets killed 3 of 3; positive killed 1 of 1; honest rc 0; decoys held 3 of 3` → `C1-PREDICATE-MET`, rc 0. Self-test reads `0 failure(s) over 38 assertions` (`landing/bat-selftest.txt`).
- **Bound (A2):** the frozen predicate can also be met by a comment-skipping source sniffer (MutTesterBattery94 tokenize forgery; CriticClaimsR94 D4 line filter). The counter's MET therefore does not prove behavioural arms. That proof comes from the three non-counter readings, which applied each mutant by hand and named the failing behavioural assertion.
- **Routed survivors:** N1, N5, N11 (round 95).

**C2 — consistency.** Counting command: `python3 -B verifiers/fixtures/round-94/selftest-kills.py c2 <rev>`.
- **Before** (`redbefore-c2-base.txt`): `C2 targets killed 0 of 2; positive killed 1 of 1; honest rc 0; decoys held 2 of 2` → UNMET, rc 1.
- **After** (`landing/c2-counter.txt`): `C2 targets killed 2 of 2; positive killed 1 of 1; honest rc 0; decoys held 2 of 2` → `C2-PREDICATE-MET`, rc 0. Tip self-test reads `self-test: 0 failure(s) over 102 assertions` (`landing/tip-selftest.txt`).

**No-harm at landing (`f65347a6`):**

| check | reading |
|---|---|
| round-93 `c1-killpin-rev.sh` | `C1-PREDICATE-MET` |
| round-93 `c2-pinkey.sh` | `C2-PREDICATE-MET` |
| round-92 `controls-run.sh` | `shortcuts refused 2 of 2; honest held 2 of 2`, rc 0 |
| gate registry | `74 of 74 … phantom 0`, rc 0 |
| floors self-test | `0 failure(s) over 176 assertions` |
| census validate | rc 0 |
| SKILL.md | byte-identical |
| tip battery | `guards 5 of 5; tip battery exit 0: 2 of 6` (round-93 landing: 3 of 6) |

**Tip-battery note.** The added red is `check_assertion_floors.py` hitting its 280 s gate timeout under a fleet load average of about 100. At the round-93 landing that gate took 188.7 s.
- No byte the floors gate measures changed between base and landing (`landing/floors-inputs-unchanged.txt`, empty diff).
- Run standalone at the same load, the floors gate exits 0 in 309 s (`landing/floors-gate-standalone.txt`).
- I read this as environmental. It is disclosed, not hidden, and the non-author closure may rule otherwise.

**Mined-mistake fix, shown able to fail:**
- Before, using the freeze-commit script: `hex41/` and `indented/` → rc 2, no finding (`landing/receipt-hdr-*-before.txt`).
- After:
  - `hex41`, `indented`, `hex39`, `scratch-hex41` and `double-decl` → rc 1, each naming `MALFORMED`.
  - `good` → rc 0.
  - Round-93 receipts: `9 resolved, 0 unresolved over 19 files`, rc 0.
  - Round-92 landing receipts are still `1 resolved, 5 unresolved`, rc 1 (`landing/receipt-*-a1.txt`, measured at `8068e32e`).
- The round-94 receipts themselves read `15 resolved, 0 unresolved over 35 files`, rc 0.

## Sources & frontier

- **SOURCES.md rows before → after:** 194 → 195. Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` at `4d3e8e4d` and at `b623b420`.
- **Census:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`.
  - Round start: `receipts/census-before.txt`, exit 0, 33 pre-existing `W04`.
  - Round end: `receipts/landing/census-validate-end.txt`, exit 0, final line `kotoba ok …/corpus/SOURCES.md`, 34 `W04`. The added warning is S269 sharing S262's URL across scopes; there is no `E`-code.
- **Rows added by tier:** tier A ×1. S269 is the PIT "Basic concepts" page (`https://pitest.org/quickstart/basic_concepts/`), opened by me on 2026-11-05: HTTP 200, 12155 B, sha256 `c51d8423f5a75e00c7039463f8a5992ef8f1f92b994d69f67d212ff7bfd92b3a`. The located quote is "Killed means a test caught the mutation successfully." Status `mined`. Tier B and tier C: 0.
- **Rows touched old→new:** none (append-only; lesson § Status changes).
- **Disclosure (A3):** S262 already held this URL without the trailing slash. S269's `teaches` cell is scoped to what each outcome class means for a kill rule. CriticClaimsR94 D7 holds: the page does not support the counter's timeout rule, and the lesson is corrected to say so.
- **Same-round rejects:** the mutmut docs index (names no outcome class) and the Cosmic Ray docs (a different class set). Reason and flip condition for each are in the lesson Gate.
- **Sourced claim:** C1 cites S269 (plan § C1, lesson § Gate, SCORECARD round-94 annotation).
- **Mined mistake:** `receipt-header-fail-open` · evidence `.ufo/waves/round-93/w1/CriticClaimsR93/CriticClaimsR93.md` D2/D3 · captured-by `none` · fix: the MALFORMED rule, shown failing as above. Attack seats also caught the first fix as incomplete (D1, D2, r1); A1 closed those cases.
- **Frontier rows advanced:** self-test mutation kills are now measured with an anti-sniffing decoy. Receipt headers now fail closed.
- **Assimilation:** none. L0 `kotoba | round-88` (55-id collision) is still open, and no claim depends on it.
- **Considerthese:** I re-read `considerthese/2026-10-26.md` and implemented nothing. Proposal 3 is carried because SKILL.md is at its 600-line ceiling (lesson § Considerthese).

## Trend verdicts

- **expansion: unchanged.** No `knowledge/` entry was admitted. S269 is a SOURCES row cited by the plan and the lesson.
- **quality: improved.** Two self-tests now kill five mutants they missed at base: C1 3/3 and C2 2/2 (`c1-counter.txt` and `c2-counter.txt` against the `redbefore-*` receipts). The receipt check now fails closed on five malformed-header shapes that read rc 0 or 2 before.
- **discernment: improved, conditional.** Round-93 closure defects became fixes: 1 → C2, 2 → C1, 3 → the mined mistake, 4 → the report-file-first rule. Attack seats caught the counter's sniffing bound and the incomplete first fix, and both were disclosed or repaired before the record commit. The non-author spot-check of S269 and the two rejects is still owed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: `SHONEN.md` box 1 pointers, unchanged; SKILL.md byte-identical at 600 lines between `4d3e8e4d` and `b623b420`.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: `LOG.md` § Round 94 (C1/C2 arms built, attacked and landed; readings at `f65347a6` in `.ufo/waves/round-94/receipts/landing/`).
- [~] Instructions executable by an agent without oral context. Evidence: seats ExecBatterySelfTest, ExecTipSelfTest, CriticClaimsR94, the reviewers and SentinelScopeR94 each ran the frozen counter `verifiers/fixtures/round-94/selftest-kills.py` on their own candidates (`w1/*`). The `SHONEN.md` box 3 pointer is unchanged.
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: `PROVINCE.md` unchanged; ConnectorOverlapR94 sibling grep (`w1/ConnectorOverlapR94.md`); no sibling file touched. The sibling census is still red (`province rows 20 matched 4`, carried).

## Round shape, seats, and lane status

- **Shape:** ONE v1 wave `r94-w1` (band 8–16) of 12 seats, all settled:

  | role | seats |
  |---|---|
  | executor | 3 |
  | scout | 1 |
  | scribe | 1 |
  | connector | 1 |
  | reviewer | 2 |
  | mutation-tester | 2 |
  | critic | 1 |
  | sentinel | 1 |

  Attack seats are 5 of 12 = 42 % (≥ 25 %); there is 1 connector (≤ 2). No residual call; the round total is 12 seats. Routing came from `task.agentModelOverrides` at spawn, and no `model` was passed.
- **Planner seat:** the validator rejects `planner`, so the L1 held the §3 planner seat. ConnectorOverlapR94 carried the planning data-walk.
- **Dead seats:** none. All 12 seats have final outputs in `r94-w1-results.json` and report files in `w1/`. WAVE-DONE was received before this report.
- **Stale-lane:** none. This respawn-per-round driver has no other open mission for this lane.
- **Tooling:** nothing was installed or upgraded by the L1 or any seat (seat final outputs). No pacman and no sysctl.
- **Scratch:** everything was under `/fast/scratch/hyaku/kotoba-r94/` and has been removed (`ls /fast/scratch/hyaku | grep -c kotoba-r94` → 0).
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only orchestrator-owned `.scratch/*`, which I did not touch, and the pre-existing `?? w4lines.txt`, which has no kotoba content and was not written by this lane. No kotoba seat file is at the fleet root.
- **Earlier attempts:** none (one `launch kotoba round=94 … attempt=1`; no `lane-dead-no-report`).
- **Commits:** all through `jj-lane.sh commit … --as kotoba`. Landed: `edc731a9…`, `f65347a6…`, `8068e32e…`, `b623b420…`.

## Open items and L0

- **Routed to round 95:**
  - A code decoy, so comment-skipping sniffers trip the guard (A2).
  - The counter scores a run error as a kill (Critic D8; S269 lists `Run error` as its own class).
  - Battery survivors N1 (manifest read at HEAD, not `--rev`), N5 (target-set refusal labelled `kill-set-size`) and N11 (`want + 2` accepted).
  - Receipt declarations that do not start the line (Critic D3).
  - Round-93 R2 (cause attribution in the `other` world).
- **Carried, unchanged:** L0 `kotoba | round-88`, `kotoba | round-73` and `kotoba | round-92`; the sibling census red; the checklist and corpus-integrity reds.
- **No new L0 question this round.**
- **Verdicts are measured, not admitted.** The claim readings above are my measurements at `f65347a6`. The non-author closure rules the round.
