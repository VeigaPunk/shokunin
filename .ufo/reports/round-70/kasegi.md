# kasegi — round 70

Lane: kasegi (`kasegi-shokunin`, axes **depth + coverage**, bounty/security research).
Round 70, attempt 1. Base `e7c02bddaa32a4a70afb2e6278f108e03dca067c`. Lane tip after this round:
`3874e40eee92b5501a56c1551f78eb87d6df51ea`. Frozen claims: `.ufo/waves/round-70/claims.json` at
`e74ba6b5d522b1e91dca3a2d244585d6b7babdc5`; pins `.ufo/waves/round-70/controls/pins-r70.txt`.

**Declared claims (2).**

1. **C1 — depth:verifiability (lowest non-retired axis, score 4, nominal per R58). NOT VERIFIED as
   declared (honest stop).** The declared claim: the derive gate refuses the python head's measured
   write/exec/ingress long options — `--root`, `--out`, `--output`, `--json`, `--scratch`, `--url`,
   `--work` — by name and by any unique argparse abbreviation, plus a short `-o`, **while every
   read-only derive stays admitted**. Implementation `c1051749571caf6a0383b15187fc02cdd21785b5`
   (gate sha256 `7a8d52eb…`). The frozen predicate passes (`measurements=12 failures=0`); the declared
   universal fails: the wave's critic measured 10 read-only derives the candidate refuses and the base
   re-derives, and the exec class reachable with no option at all. Score held at 4, no gain claimed.
2. **C2 — coverage (score 8).** Frontier F48 admitted on S105 (GitHub Advisory Database curation
   semantics) with a new knowledge entry, plus the round-69 rejected-row debt V69-1 landed as S104
   (ENISA EUVD API documentation). Landing `b4afd8a0206b23a69d8cd65d92070cdfcd4680a7`.

## Work performed

- **C1, gate repair (depth:verifiability).** `python_head_ok` now runs `python_flags_ok` over the
  decoded argv after the script path: a `--`-prefixed token before a `--` separator is refused when
  its name (text before `=`) equals a denied flag or is a non-empty prefix of one (argparse accepts
  unique abbreviations), a short `-o`/`-oVALUE` is refused, and tokens after `--` are operands and
  stay admitted. Evidence: `corpus/instruments/figure-audit.py` at `c1051749` (sha256 `7a8d52eb…`),
  `SKILL.md:1248` (r70 current-execution amendment), `SKILL.md:1224` (selftest pin 86 → 96).
- **C1, refutation and honest stop.** `CriticC1` (`.ufo/waves/round-70/w1/CriticC1.md`) reproduced
  the predicate and refuted the declared clause with 10 paired rows: `ok.py --out x`,
  `claim-package-check.py … --json` (stdout flag at `:791`), `capture-binding-check.py --root .`,
  `kill-rule-check.py --root .`, `r44-frontier-count.py --root .` (plain, `&&` and pipeline forms),
  `citation-ground-check.py --root .`, `gate-quote-audit.py --root .`, `r44-routed-defects.py --root .`.
  The same seat measured the exec class reachable with **no option at all**
  (`python3 corpus/instruments/frontier-recheck-count.py`, admitted by both gates, runs the entry's
  `recheck:` payload through `bash -c`: 1 marker, 51 `bash` invocations) and through `--selftest` in
  15 instruments. Cause: `PY_DENIED_FLAGS` is global while `--root` is a read-only pointer in six-plus
  instruments and `--json` is stdout-only in one. Routed as V70-5 (per-script denial) and V70-6
  (`--selftest` and the no-argument spelling); not applied after measurement because a post-freeze
  gate edit would invalidate the frozen claim rather than strengthen it.
- **C1, selftest pins (R103 closure).** Ten cases added: seven python-head refusal cases (three
  `--root` spellings, three `--out` spellings, `--json`), one `--`-operand positive control, and the
  two round-69-routed `git_show_operands_ok` limbs (`git show` with no operand; `git show HEAD:g.txt
  -- g.txt`). `EXPECTED_CASES` 86 → 96; the pin is re-derived from committed bytes
  (`git show c1051749:corpus/instruments/figure-audit.py | grep -cE '^\s+run_case\('` = 96).
- **C1, controls before data.** Pre-freeze commit `15d4da87`: base no-work control
  `controls/c1-base-donothing-r70.txt` (`measurements=12 failures=9` exit 1), candidate trial
  `controls/c1-candidate-trial-r70.txt` (`12/0` exit 0), blanket-refusal forgery
  `controls/c1-forgery-blanket-r70.txt` (rejected: 8/8 positive controls fail, selftest 47 failures).
- **C2, source and entry (coverage).** S105 captured 2026-11-05T00:14:43Z (HTTP 200, 616388 fetched
  bytes → 656 lines, sha256 `9dd51a8e…e3350`), 19 pinned quotes all located by
  `source-recheck.py` (`S105:Q01…Q19 OK`); entry
  `corpus/knowledge/github-advisory-database-curation-semantics.md` (advisory classes, imported feeds,
  supported-registry review gate, GHSA id shape, CVSS provenance, EPSS sync rule, community path);
  README row F48; snapshot manifest `corpus/source-snapshots/round-70/manifest.json`.
- **C2, post-wave correction (erratum 1).** The wave's `CriticC2` listed 21 source-outruns in the F48
  entry (three wrong-branch statements, one misquote, an inverted author cell, unsupported
  generalizations). All 21 were applied to the entry and its three summaries; the frozen pins file is
  untouched and the delta is recorded in `.ufo/waves/round-70/controls/pins-r70-erratum-1.txt` with the
  old→new entry hash (`d479c495…` → `0775d2a4…`) and re-measured C2 values (unchanged). QUALITY R108.
- **C2, rejected-row debt V69-1.** S104 (ENISA EUVD apidoc) re-fetched 2026-11-05: HTTP 200, 3062
  bytes, sha256 `6fb32b61…a38d5` — byte-identical to the round-69 receipt — with zero `endpoint` and
  zero `/api/` occurrences in the static body, so the row lands `rejected` with its flip condition.
- **Frontier step / assimilation.** `Assimilation: none`: the staged package carries 94 ids of which
  73 collide with the lane's 103-row registry (mass drift), so nothing is adopted and an L0 question
  is filed. Slices committed: `assimilation/reg-ids`, `staged-ids`, `collisions`,
  `quarantine-slice` (7 rows).
- **Lesson and criteria.** `corpus/lessons/round-70.md` (C1/C2 results, Gate block for S104/S105,
  Mistakes M70-1..M70-4, dispositions of V69-1..V69-3, residuals); `corpus/QUALITY.md` R104–R106.
- **Wave.** One v1 wave, 12 seats, dispatched via `.ufo/waves/round-70/w1.ready` (payload
  `w1-dispatch.json`, registry `w1/swarm-registry.json`); attack share 6/12 (two reviewers, two
  critics, one mutation-tester, one sentinel), one connector, one scout, one scribe, three executors;
  the L1 holds the planner seat.

### Wave outcome (10 of 12 seat reports landed; wave not yet settled)

| seat | role | verdict | effect on the round |
|---|---|---|---|
| ReviewerC1 | reviewer | **C1 VERIFIED** from committed bytes (12/0 candidate, 12/9 base, pins and byte-identity reproduced) | none |
| ReviewC2 | reviewer | **C2 VERIFIED** — all 10 frozen limbs reproduce; 19 quotes relocate | none |
| CriticC2 | critic | 21 source-outruns (O1–O21) in the F48 entry | erratum 1 applied; R108 |
| SentinelGate | sentinel | **widening-free** — `ADMITTED_NOW=0` over 482 derives; ledger 35/35 unchanged; one recorded capability loss (`--root <fixture>` through the gate) | V70-3 |
| MutationC1 | mutation-tester | 13/22 mutants killed, 9 survived; 7 real pin holes, ranked repair list | V70-1 |
| ExecR103 | executor | isolation audit: 2/3/7/8/9 exclusive killers, 4/5 group-only, 6 and 10 conjunction-pinned | V70-1 |
| ExecCountersC2 | executor | C2 counters, census, 73-collision and quarantine re-derivation all reproduce | none (found the frozen-receipt overwrite → erratum 2) |
| ScoutS105 | scout | zero content drift; 19/19 quotes; S104 digest reproduces; 301 redirect found; audit blind spot measured | erratum 3; V70-4 |
| ScopeF48 | connector | **SCOPE CLEAR** — no held row or sibling lane carries the ground | none |
| ScribeRound | scribe | found the mid-write pinned receipt | erratum 2; M70-8; R109 |
| CriticC1 | critic | predicate reproduces; **declared universal refuted** (10 over-refusal rows; no-option and `--selftest` exec) | C1 → NOT VERIFIED; V70-5/V70-6 |
| ExecProbe | executor | **dead** — provider 401 on `commandcode/z-ai/glm-5.3-flash`; no report | recorded, not replaced |

`w1-results.json` records 12 settled seats: 11 with reports and one dead seat (ExecProbe). No seat was
replaced and no residual task call was made. C1's verdict depends on CriticC1's rows, all pasted in its
report; ExecProbe's silence changes nothing in the claims.

## Landed changes

| commit | content | LOG entry |
|---|---|---|
| `b4afd8a0` | C2 landing: entry + S105 capture + manifest + rows S104/S105 + README F48 + knowledge-expected 88/86 | round 70 bullet 4 |
| `15d4da87` | pre-freeze controls (base no-work, candidate trial, forgery, counter), C2 base/after counters, assimilation slices | round 70 bullet 2 |
| `e74ba6b5` | frozen claims + pins | round 70 bullet 3 |
| `c1051749` | C1 implementation (gate + selftest 96) and SKILL.md amendment | round 70 bullet 3 |
| `7f6e39a9` | final verification receipts, C2 after counters, lesson, QUALITY R104–R106, LOG, SCORECARD, wave spec/dispatch/ready | round 70 bullets 5–8 |
| `ede38bf5` | restore the frozen C2 receipt and land the clone re-measurement separately (R107); V70-1/M70-6 | round 70 bullet 9 |
| `97eda97e` | F48 entry correction (21 source-outruns), erratum 1, R108, M70-7 | round 70 bullet 10 |
| `afcced40` | routed defects V70-1/V70-2/V70-3 | round 70 bullet 9 |
| `5cbd4945` | erratum 2 — pinned forgery receipt captured mid-write; re-run `failures=4`; M70-8, R109 | round 70 bullet 11 |
| `db2e33ab` | erratum 3 — S105 301 redirect, typed word count 18→17, V70-4 | round 70 bullet 12 |
| `f8fef204` | settled wave evidence, CriticC1 refutation, lesson/SCORECARD/LOG verdicts | round 70 bullets 13–14 |

Every change is tied to the `## Round 70` block in `LOG.md`: bullet 3 (freeze/implementation), bullet 4
(C2 landing), bullets 5–8 (verification, counters, assimilation, wave outcome), bullet 9
(corrections), bullet 10 (QUALITY gains), bullet 11 (round-69 dispositions). The commit→bullet map in
the table above names the bullet each commit implements.

## Before → after measurements

**C1 (depth:verifiability).** Counting command (frozen, `claims.json`):

```
python3 -B .ufo/waves/round-70/controls/c1-probe-run-r70.py \
  --gate <gate exported from the measured revision> \
  --work /fast/scratch/hyaku/kasegi-r70/L1/FINAL --mode candidate
```

- Before, base gate `c09b0fb1…` at `e7c02bd` (`controls/c1-base-donothing-r70.txt`, and the paired
  shared-clone run `controls/c1-base-donothing-r70-clone.txt`): `VERIFY measurements=12 failures=9`
  exit 1 — P1/P2/P3 run the fixture entry's `recheck:` payload through `bash -c` (marker_runs=1),
  P4/P5/P6 write their named outside file (wrote=1), P7 does both; selftest 86.
- After, gate `7a8d52eb…` at `c1051749` (`controls/final-verification-r70.txt`): `VERIFY
  measurements=12 failures=0` exit 0 — P1–P7 `rc=2 reason=derive-not-read-only marker_runs=0
  wrote=0`, 8/8 read-only controls exact, selftest 96/0, mutbat 5/5, ledger 35/35, no write side
  effect.
- Verdict: **predicate verified, claim NOT VERIFIED as declared** — the frozen counter passes, the
  declared universal ("while every read-only derive stays admitted") is measurably false on 10 rows.
  Score 4 → 4, delta 0; no gain claimed; honest stop per §9.
- Closure note: the first final run used a `git archive` export and failed only its `real-ledger`
  limb (35/11/24, exit 1) because the ledger's derives are `git show <rev>:<path>`; the receipt is
  committed as `controls/final-verification-r70-archive-export-failed.txt` and the claim is graded on
  a `git clone --shared` checkout of the same revision (R106).

**C2 (coverage).** Counting commands (frozen): `python3 corpus/instruments/frontier-recheck-count.py`;
`python3 corpus/instruments/capture-binding-check.py`; `wc -l` and `grep -vc '^#'` on
`corpus/instruments/knowledge-expected.txt`; `LC_ALL=C sort -c`; `ls corpus/knowledge/*.md | wc -l`;
`grep -cE '^\| F[0-9]+ \|' corpus/README.md`; `sources-census.sh validate --root … kasegi`.

- Before at `e7c02bd` (`controls/c2-base-counters-r70.txt`): rows=47 admitted=47 closed=47
  problem-rows=0 registry=103; entries=50 pass=50; records=83 bound=83 unbound=0; expected 87 lines /
  85 entries; 85 knowledge files; 47 frontier rows; census exit 0 with six inherited W04 warnings.
- After at `b4afd8a0` (`controls/c2-after-counters-r70.txt`, `controls/census-after-r70.txt`):
  rows=48 admitted=48 closed=48 problem-rows=0 registry=105; entries=51 pass=51 exit=0; records=84
  bound=84 unbound=0; expected 88/86 sort-clean; 86 knowledge files; 48 frontier rows; 0 malformed
  registry rows; census exit 0 with the same six inherited W04 warnings (none names S104/S105).
- Verdict: **verified**; score 8 → 8, delta 0 (the coverage denominator is operator-owned).

## Sources & frontier

- **Census before → after** (command
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`):
  before exit **0** (rows 103, six inherited W04 duplicate-url warnings on S028/S029/S072/S076/S080/S085);
  after exit **0** (rows 105, the same six warnings; `controls/census-after-r70.txt`). The registry
  file did not exist as a census failure at round start, so no exit-2 case applies.
- **Rows:** 103 → **105**; added by tier: **A 1** (S105, docs, mined), **C 1** (S104, docs,
  rejected); touched old→new: none (append-only this round).
- **Frontier rows advanced:** 47 → **48** (F48 admitted on S105; F47's `next` cell now points at
  F48/S105 for the curation semantics it had named unopened). Knowledge entries 85 → **86**; capture
  records 83 → **84**.
- **Assimilation:** none — 73 of the staged package's 94 ids collide with the lane registry
  (`assimilation/collisions`), mass drift under the contract's drift rule; L0 question filed. The
  7-row quarantine slice is re-derived and classified (`assimilation/quarantine-slice`): two
  `payload-absent`, five the register's unchecked "could not be fetched" family.

## Trend verdicts

- **Expansion — improved.** F48 admitted on ground the held corpus named as unopened, with a new
  mined A-tier row (S105, 19 located quotes) and a rejected row (S104) that closes a contract debt:
  registry 103 → 105, knowledge 85 → 86, frontier 47 → 48, capture 83 → 84, census exit 0.
- **Quality — unchanged.** The measured gate refuses seven shapes the base gate executed or wrote on
  (`12/9` → `12/0`), the forgery is rejected by positive controls and the selftest pin rises 86 → 96 —
  but the round's own critic refuted the claim's universal (10 read-only derives now refused) and the
  exec class is still reachable without an option, so no quality gain is claimed. Six process misses
  became R104–R109.
- **Discernment — improved.** The attack share did its job: a critic refuted the round's own declared
  sentence, a mutation-tester and an executor measured the selftest pin holes, a scout found a 301
  redirect and the quote-audit blind spot, and a scribe found a pinned receipt captured mid-write. All
  of it became criteria (R104–R109) and routed defects (V70-1..V70-6) instead of being smoothed over.
  The round found six of its own misses from committed receipts. Non-author closure still owns
  admission.

## Stale-lane

Respawn-per-round driver; this round is the lane's only open mission. No sibling lane work touched;
no domain source tree was written (the two opened sources are read-only fetches).

## Tooling

No tool installed or upgraded this round. Host binaries measured: `/usr/bin/sort` GNU coreutils 9.12,
git 2.56.0, python3 3.14.8 (the omp bash tool's bare `sort` is a shell builtin, not the gate's binary
— R101).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:1248` r70 amendment plus the gates registry row at `SKILL.md:1224`; author-asserted, outside promotion verification remains required.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — not claimed; no authorized end-to-end bounty task, former roots absent, live-target testing refused.
- [~] Instructions executable by an agent without oral context — this round's receipts are re-runnable commands (`controls/c1-probe-run-r70.py`, `controls/final-verification-r70.txt`); `corpus/lessons/round-47-verifier-spotcheck.md` records the standing caveat.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — no PROVINCE change this round; both new rows are GitHub-advisory curation ground inside the lane's province, sibling scan `ScopeF48`.
