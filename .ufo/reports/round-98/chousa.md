# chousa — round 98 report (L1 `ChousaR98`, attempt 1)

Lane repo `chousa-shokunin`, branch `master`. Base `98b8177c1e8b39cdf1167928e4f5d609f6fa81b6` (round-97 landing plus
its non-author spot-check). Final lane hash `80b754e425361f7fdc4675aa85ac36366dacf2b1` (ls-remote below). No earlier attempt of round 98 existed
(`.ufo/watchdog.log`: one `launch chousa round=98 … attempt=1` line); nothing inherited.

## Work performed

Declared claims (frozen at F `aac82684`, re-frozen at F2 `1689f4ad` on wave-forced amendments, F3 `1c6e01c5` wording
only; `.ufo/waves/round-98/claims.md`, `claims.json`):

- **C1 `C1-SELFTEST-R97MUTANTS-R98` — operability** (the lowest axis, historical 3/10): `tools/search-rerun.py
  --selftest` gains a guard canary `g00` (runs `_collect`/`_summary` on four fixed case sets; a failed canary
  prints the FAIL line itself) and cases `r17`-`r34`; battery `corpus/evidence/round98/selftest-controls-r98.py`
  scores it against the 37 mutants round-97 seat `R97MutantsC1` wrote (read from committed bytes), the 34 + 23
  prior mutants, three equivalent mutants that must survive, five stand-ins (incl. hash-of-self, guard-blind), its
  own kill rule and the direct FAIL path.
- **C2 `C2-ENTRY-R98` — depth, sourced on S231 (opened this round)**: new entry
  `corpus/knowledge/press-2015-statement-questions-r98.md` — the PRESS 2015 Guideline Statement's own abstract via
  Europe PMC's record of PMID 27005575 (14 abstract quotes + title), element names compared with the reprint, and
  the 20 S225 checklist question lines the round-97 entry did not quote (36/36 across the two entries).

Work items:

- Fresh-start read: not bound (r95-r97 admitted, MANIFEST closures); round-97 spot-check
  `corpus/lessons/round-97-verifier-spotcheck.md` routed defects 1-2 → C1, 3 → C2 wording + K3, 4 → round-98
  battery docstring/scratch cwd, 5 (D1) → routed with a seat-proposed rule (`R98RevenPrior`).
- Approval table before the first GET: `corpus/evidence/round98/egress-approval.md` (rows appended between GETs,
  disclosed in the file); four GETs, `corpus/evidence/round57/refetch.tsv` rows S228-S231.
- Do-nothing controls committed before the freeze: `corpus/evidence/round98/before/c1-base.txt` (base tool
  `KILL_REQUIRED=12/35`, FAIL), `before/c2-base.txt` (entry absent, gate exit 2; `BASE_HELD=16/36`); F2:
  `before-f2/c1-base.txt`. Harm leg: `before/c1-verify-harm.txt`, `after-f2/c1-verify-harm.txt` (8×SAME).
- Pre-freeze fix P0 (`plans/round-98.md`): two new cases' text contained mutant site `return exc.code`.
- One v1 wave, 12 seats (`.ufo/waves/round-98/w1-dispatch.json`, validated under `scripts/hyaku/ufo-wave-policy.json`);
  seat reports `.ufo/waves/round-98/w1/R98*.md`.
- Wave-forced amendments (all with seat artifacts, `claims.md` § Amendments): C1 A1-A7 (canary one/four-failure sets
  after `R98MutantsC1` S02/S03/X4; DIRECT_PATH after D01-D04; KILL_RULE and pinned sizes after B1/B3/B5; named
  limit (e) per `R98SentinelC1`); C2 B1-B8 (M1 is the title — FIELD leg; row-2 Never; limit (c); IDENTITY leg; S231
  tier A → B; forgeries f8-f12, ACCEPT; controls docstring).
- L1 re-score of `R98MutantsC1`'s probe on the F2 tool: `corpus/evidence/round98/after-f2/c1-rescore-r98mutants.txt`.
- Found and routed: `tools/gate-records.py` admits a quote from an http-200 challenge page
  (`corpus/evidence/round98/gate-records-challenge-200.txt`); QUALITY 229.
- Falsification ledger `.ufo/waves/round-98/claim-falsification.tsv` (16 rows, every attack seat):
  `PREFILE-FALSIFICATION: pass claims=2 rows=16 attack_seats=8 findings=0`, exit 0.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `aac826848dda5029ba459568b29d9a92176dc2b6` | freeze F: tool, batteries, entry, S228-S231, captures, refetch rows, before receipts, census start, egress table, plan, claims | Round 98 |
| `bc3ebc7cecec74d2b6528a5035c7e8bc26f190b7` | carrier: after receipts at F, wave spec, dispatch, ready | Round 98 |
| `1689f4ad85e11d7f9a7a10a1b5127ec9d7019e49` | re-freeze F2: A1-A5, B1-B7 | Round 98 (corrections) |
| `1c6e01c52149c7b4d6dfc4a8cfc419243dc8c101` | re-freeze F3: A6-A7, B8 (wording); F2 receipts | Round 98 (corrections) |
| `f0050074b8d977523466f7d213c592b69fc030f9` | landing: after-f3 receipts, challenge-200 probe, census end, lesson, LOG, SCORECARD, QUALITY 229, README, SKILL correction, search log, ledger, seat reports | Round 98 |
| `80b754e425361f7fdc4675aa85ac36366dacf2b1` | wave results file (12/12 seats) | Round 98 |

## Before → after measurements

**C1** (measured at F2 `1689f4ad`, bytes identical at F3: `corpus/evidence/round98/after-f3/c1-f2-equals-f3.txt`)

    python3 -B tools/search-rerun.py --selftest
    python3 -B corpus/evidence/round98/selftest-controls-r98.py --root . --work <scratch>

- before (base tool `98b8177c`, F2 battery; `before-f2/c1-base.txt`): `POSITIVE=0/1 KILL_RULE=4/4 DIRECT_PATH=0/2
  KILL_REQUIRED=12/35 … EQUIVALENT_SURVIVED=0/3 … EXTERNAL_R97_KILLED=12/37`, `SELFTEST_CONTROLS_R98=FAIL`, exit 1.
- after (`after-f2/c1-all.txt`): `SEARCH_RERUN_SELFTEST: PASS cases=67/67` exit 0; `POSITIVE=1/1 KILL_RULE=4/4
  DIRECT_PATH=2/2 KILL_REQUIRED=35/35 DO_NOTHING_REFUSED=1/1 PRIOR_R97_KILLED=34/34 R96_MUTANTS_KILLED=23/23
  EQUIVALENT_SURVIVED=3/3 ORACLES_REJECTED=5/5 NO_WRITE=1/1 REGRESSION_R95=2/2 EXTERNAL_R97_KILLED=35/37
  BASE_KILLED=12/37 CASES=67`, `SELFTEST_CONTROLS_R98=PASS`, exit 0.

**C2** (measured at F3 `1c6e01c5`; `after-f3/c2-all.txt`)

    python3 -B tools/gate-records.py verify --root . corpus/knowledge/press-2015-statement-questions-r98.md
    bash tools/research-gate.sh verify-metadata corpus/knowledge/press-2015-statement-questions-r98.md --root .
    python3 -B tools/search-rerun.py verify corpus/knowledge/press-2015-statement-questions-r98.md --root .
    python3 -B corpus/evidence/round98/entry-controls-r98.py --root .

- before (`before/c2-base.txt`): entry absent at base, `GATE_RECORDS_ERROR missing …` exit 2; `BASE_HELD=16/36`.
- after: `GATE_RECORDS files=1 records=38 ok=38 fail=0`; `METADATA_COMPLETE=1/1`, `RESEARCH_GATE: CLEAN`;
  `SEARCH_RERUN_SUMMARY searches=5 rev_match=5/5 …`, `SEARCH_RERUN: CLEAN`; `POSITIVE=1/1 DO_NOTHING_REFUSED=1/1
  NEW_ONLY=1/1 FORGERY_REFUSED=12/12 IDENTITY=1/1 FIELD_SCOPED=15/15 ACCEPTED=2/2 QUESTION_LINES_HELD=36/36
  BASE_HELD=16/36 …`, `ENTRY_CONTROLS_R98=PASS`; all exit 0.

## Sources & frontier

- Census before → after: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa` → exit 0
  both (`corpus/evidence/round98/census-start.txt`, `census-end.txt`; warnings identical: W04 ×6 pre-existing, W01
  S226). Registry rows (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`): 226 → 230.
- Rows added by tier: S231 B (`mined`, admitted); S228 A, S229 A, S230 A (`rejected` for route: 403, 203 cookie
  challenge, http-200 reCAPTCHA). Gate lines with URL, access date and ≤25-word located quote:
  `corpus/lessons/round-98.md` `## Gate`.
- Rows touched old→new: S225 `used-by` `…/press-checklist-questions-r97.md` →
  `…/press-checklist-questions-r97.md, …/press-2015-statement-questions-r98.md` (status, recheck unchanged).
- Frontier advanced: README Round97's "17 of S225's 33 question lines are not quoted" closed (36/36 question-mark
  lines); the guideline statement held at abstract level (`corpus/README.md` `## Round98 coverage and frontier`).
- Sourced claim: C2 cites S231 (opened this round). Mistakes mined: 4 (`corpus/lessons/round-98.md` `## Mistakes`),
  each fix shown able to fail.
- Assimilation: none. considerthese: not mined this round.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` → only orchestrator-owned `.scratch/`
  entries; no seat file at the fleet root.

## Trend verdicts

- expansion: **improved** — one new knowledge entry on README's named gap; registry 226 → 230 (`after-f3/c2-all.txt`).
- quality: **improved** — the search re-run self-test kills 35/37 non-author mutants vs 12/37 for the base tool and
  refuses hash-of-self (`after-f2/c1-all.txt`).
- discernment: **improved** — three routes refused with reasons (incl. an http-200 challenge page the gate tool
  would have admitted), S231 graded B under the carrier rule, M1's field recorded and checked (lesson Gate,
  QUALITY 229). Author-measured; non-author closure pending.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` Gates table and round-98 correction line (lane assertion; no non-author verifier named)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 98` (search, source opening, entry, gates)
- [~] Instructions executable by an agent without oral context — `python3 -B tools/search-rerun.py --selftest`; `corpus/evidence/round98/after-f2/c1-all.txt`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched; `R98ConnectorSiblings` routed sibling patterns

## Round shape and extras

- Shape: one v1 wave, 12 seats, policy v1 (band 8-16): executor 2, mutation-tester 2, reviewer 2, critic 1,
  sentinel 1, scout 1, revenger 1, connector 1, scribe 1; attack share (reviewer, critic, mutation-tester) 5/12.
  L1 holds the canonical planner seat (the validator refuses `planner`). Residual call: none. Round total: 12.
  Dead seats: 0 (12/12 settled with reports; `.ufo/waves/round-98/w1-results.json`). Seat routes per `task.agentModelOverrides` (not passed).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (L1 and, per their reports, every seat).
- L0 questions: none opened this round.
- Final lane hash: `git -C chousa-shokunin ls-remote origin refs/heads/master` → `80b754e425361f7fdc4675aa85ac36366dacf2b1`.
