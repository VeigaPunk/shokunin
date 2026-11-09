# chousa — round 96 report (L1 `ChousaR96`, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/chousa-shokunin`, branch `master`. Base `bbf64970` (round-95 landing +
its non-author spot-check). Freeze F `2db151c5`; wave-forced re-freezes F2 `e91f82fe` and F3 `31810b4e`; landing `c8087ac529003e667505bcc624f9a7bde0cffbce`.

## Work performed

Declared claims (2, both measured; no exploratory claim):

- **C1 `C1-SELFTEST-R96` — operability** (the lowest-scoring non-retired axis, historical 3/10): `tools/search-rerun.py`
  gains `--selftest` (32 in-memory cases) and is re-registered in `SKILL.md` `## Gates` as kind `gate` — round-95
  spot-check D1.
- **C2 `C2-ENTRY-R96` — depth**: new entry `corpus/knowledge/search-peer-review-dedup-r96.md` (PRISMA-S items 14 and 16
  + Box 1 via `S224`; the PRESS 2015 authors' abstract via `S223`; both opened this round) with a `## Searches` record
  of the round's own 8 gap searches. This is the round's sourced claim.

Work items:

- Protocol load: MISSION/AXES binding, prompt §1-§8 read; rejection history checked (r90 rejected, r91-r95 admitted;
  no fresh-start rule binds r96). Round-95 spot-check D1-D5 taken (D1 → C1; D2, D3, D4, D5 → corrections,
  `LOG.md` Round 96, `corpus/README.md` Round96 section, `corpus/lessons/round-96.md` `## Gate`).
- C1 tool change: `tools/search-rerun.py` (`parse_text` split out of `parse_record`; per-row judgement in `evaluate`,
  called by `verify` through closures that keep the round-95 mutation sites byte-identical; `selftest()`; argparse
  `--selftest`) — F `2db151c5`, docstring repair at F2 `e91f82fe`.
- C1 battery `corpus/evidence/round96/selftest-controls-r96.py` (POSITIVE, DO_NOTHING from `git show BASE:tool`,
  23 mutants, 3 stand-ins, NO_WRITE, round-95 REGRESSION legs). Pre-freeze run 1 FAILED (`MUTANTS_KILLED=22/24`,
  `corpus/evidence/round96/prefreeze/c1-run1-transcript.txt`), fixed (P1), run 2 PASS (`prefreeze/c1-run2.txt`).
- C2 sources: five GETs under `corpus/evidence/round96/egress-approval.md` (2 × 200, 2 × 403, 1 × 500;
  `corpus/evidence/round57/refetch.tsv` tail); S223 and S224 rows (`corpus/SOURCES.md:235-236`), Search log entry
  (`corpus/SOURCES.md:417`).
- C2 entry, 8 GNU-grep searches at `bbf64970`, battery `corpus/evidence/round96/entry-controls-r96.py` (adapted from
  r95; new SEARCHES group); pre-freeze PASS (`prefreeze/c2-run1.txt`).
- Do-nothing controls committed before the freeze: `before/c1-base.txt` (exit 2), `before/c2-base.txt` (exit 2),
  separability `before/c2-separable-base-tool.txt` (base tool re-runs C2's record CLEAN).
- Wave: 12 seats; amendments A1-A8, B1-B7 forced by named seat artifacts (`plans/round-96.md` § Amendments).
- Frontier step: SOURCES 221 → 223; seven mistakes mined (`corpus/lessons/round-96.md` `## Mistakes`), QUALITY 222-226.
- Gates: `SKILL.md` checklist item (search peer review/dedup) and Gates row (search-rerun r96 re-registration).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze F: tool + `--selftest`, both batteries, entry, S223/S224, captures, refetch rows, SKILL rows, before/prefreeze receipts, egress table, census start, claims, plan | `LOG.md` Round 96 | `2db151c5ea0883de0b9dc8d95c6fac1755e1056a` |
| re-freeze F2: A1-A5, B1-B6 (tool docstring, entry rows 1/3/5 + L31/L32 + fragment groups + Q6 note, `N_RECORDS` 33, claims/plan amendments) | `LOG.md` Round 96, "Wave-forced amendments" | `e91f82fe139d8bd024dce55a15df478588d51e14` |
| re-freeze F3: B7 (entry text-forms paragraph, `R96ScoutSources` §3) | `LOG.md` Round 96, "Re-freeze F3" | `31810b4e02615f8218fe3c131aee4563fccdf612` |
| landing: after/after-f2/after-f3 receipts, LOG, SCORECARD verdict + planned r97, QUALITY 222-226, README Round96, SOURCES Search log, lesson, census end, wave dir (12 seat reports, results, ledger) | `LOG.md` Round 96 | `c8087ac529003e667505bcc624f9a7bde0cffbce` |

## Before → after measurements

C1 (measured at F2 `e91f82fe`, `corpus/evidence/round96/after-f2/c1-*.txt`):

```
$ python3 -B tools/search-rerun.py --selftest          # base bbf64970 (before/c1-base.txt)
search-rerun.py: error: the following arguments are required: cmd
exit=2
$ python3 -B tools/search-rerun.py --selftest          # F2
SEARCH_RERUN_SELFTEST: PASS cases=32/32
exit=0
$ python3 -B corpus/evidence/round96/selftest-controls-r96.py --root . --work <scratch>     # F2
POSITIVE=1/1 DO_NOTHING_REFUSED=1/1 MUTANTS_KILLED=23/23 ORACLES_REJECTED=3/3 NO_WRITE=1/1 REGRESSION_R95=2/2 CASES=32
SELFTEST_CONTROLS=PASS
exit=0
$ grep -c '^| `search-rerun` (r96 re-registration' SKILL.md                                  # base 0, F2 1
1
```

C2 (measured at F3 `31810b4e`, `corpus/evidence/round96/after-f3/c2-all.txt`; F2 identical in `after-f2/c2-all.txt`; F numbers in `after/c2-all.txt`). C1's paths are byte-identical at F2 and F3 (`after-f3/c1-f2-equals-f3.txt`):

```
$ python3 -B tools/gate-records.py verify --root . corpus/knowledge/search-peer-review-dedup-r96.md   # base: exit 2 (absent)
GATE_RECORDS files=1 records=33 ok=33 fail=0
$ bash tools/research-gate.sh verify-metadata corpus/knowledge/search-peer-review-dedup-r96.md --root .
METADATA_COMPLETE=1/1  RESEARCH_GATE: CLEAN
$ python3 -B tools/search-rerun.py verify corpus/knowledge/search-peer-review-dedup-r96.md --root .
SEARCH_RERUN_SUMMARY searches=8 rev_match=8/8 tree_same=5/8 findings=0  SEARCH_RERUN: CLEAN
$ python3 -B corpus/evidence/round96/entry-controls-r96.py --root . --work <scratch>
POSITIVE=1/1 FORGERY_REFUSED=8/8 BINDING_REFUSED=3/3 SEARCHES=3/3 DO_NOTHING_REFUSED=1/1 ORACLE_REJECTED=1/1 GATE_RECORDS=33/33 LQ_BOUND=32/32 WARRANTS_OK=8/8 WARRANT_TERMS=8/8 LANE_FILLED=8/8 METADATA=clean
ENTRY_CONTROLS=PASS
```

At F (before amendments B1-B2) the same gate printed `records=31 ok=31` (`after/c2-all.txt`); the count rose because
the wave forced two quotes into the entry, not by narrowing.

## Sources & frontier

```
$ grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md      # base 221, landing 223
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa
```

- Start (`corpus/evidence/round96/census-start.txt`): exit 0, `chousa ok`, five pre-existing `W04`.
- End (`corpus/evidence/round96/census-end.txt`): exit 0, `chousa ok`, the five pre-existing `W04` plus one new (S224/S222 across scopes); 223 rows.
- Rows added by tier: A 1 (`S224`, PRISMA-S re-opened for items 14/16 — same bytes as S222, second scope), B 1 (`S223`,
  PRESS 2015 authors' JCHLA abstract). Rows touched old→new: none (no status/recheck/used-by change). New `W04`: S224
  shares S222's URL across scopes, by design (CORPUS rule 2).
- Frontier advanced: `corpus/README.md:1445` (items 14/16 not held) closed for what PRISMA-S says a report must state.
- Assimilation: none (this round took no `merge/chousa/` theme and no `considerthese/` proposal).
- Mistakes mined: seven rows in `corpus/lessons/round-96.md` `## Mistakes`, each with a fix shown able to fail.

## Trend verdicts

- **expansion: improved** — one admitted knowledge entry on ground the coverage map named as a gap (`corpus/README.md:1445`),
  `source: S224, S223` (both `mined`, both opened this round).
- **quality: unchanged** — no existing entry was re-verified, deepened or superseded; the new entry's repairs are
  in-round, credited to depth.
- **discernment: improved** — the gate rejected the CADTH and J Clin Epidemiol routes (403) and Europe PMC (500) as
  route rejections, admitted the abstract at tier B rather than A, and opened a second scope (S224) instead of
  stretching S222's scope; QUALITY 222-226 each cite a `## Mistakes` row.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:83-84` checklist
  item (search peer review/dedup, S223/S224) and the Gates row `search-rerun` (r96 re-registration) (lane assertion;
  no non-author verifier)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 96: the round's own 8 gap
  searches recorded with GNU grep and re-run by the lane's tool; PRESS and PRISMA-S opened, captured and quoted
  (`corpus/evidence/round96/after-f2/`) (lane assertion)
- [~] Instructions executable by an agent without oral context — `python3 -B tools/search-rerun.py --selftest`;
  `.ufo/waves/round-96/claims.md` F2 predicates (lane assertion)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched; tameshi's self-tests routed, not
  absorbed (`.ufo/waves/round-96/w1/R96ConnectorSiblings.md`)

## Round shape, seats, settlement

One v1 wave (policy `ufo-wave-policy.json`, band 8–16), 12 seats, dispatched through the inline handoff
(`.ufo/waves/round-96/w1.ready` → `w1.ready.dispatched`), settled with `WAVE-DONE` and
`.ufo/waves/round-96/w1-results.json` (12 results, 0 dead). No residual call; round total 12. Role mix: executor 3
(one is the wrap probe the validator would not accept as `labrat`), reviewer 2, mutation-tester 1, critic 1,
sentinel 1, revenger 1, connector 1, scout 1, scribe 1. Attack seats (reviewer, critic, mutation-tester) 4/12 = 33 %;
with sentinel, revenger and connector, 7/12. L1 held the planner seat. Seat routes were those the operator's
`task.agentModelOverrides` assigned at spawn (not passed by the L1). One seat (`R96MutantsC1`) went idle without a
report and filed after one L1 nudge.

## Pre-file falsification

```
$ awk -F'\t' '{c[$3]++} END{for(k in c) print k, c[k]}' .ufo/waves/round-96/claim-falsification.tsv
neutral 8
falsifies-wording 8
$ python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane chousa --round 96
PREFILE-FALSIFICATION: pass claims=2 rows=16 attack_seats=7 findings=0
$ echo $?
0
```

Every `falsifies-wording` row points at `plans/round-96.md` § Amendments: C1 narrowed by A1-A4 and A6-A7 (critic,
reviewer, sentinel), C2 repaired and narrowed by B1-B7 (reviewer, critic, connector, wrap probe, scout). Each claim is
filed on the narrowed sentence (`.ufo/waves/round-96/claims.md` § Amendments), not the F text. Instrument gaps
the wave found but that do not falsify a narrowed sentence (sentinel F1 replace-ref guard unasserted, F3 two-code
rows, mutation-tester Class B/C survivors, critic §Ab text-matching cheat) are routed to SCORECARD `## Planned — round 97`.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Tooling

No tool installed or upgraded.

## Open L0 questions

None added this round. Fetch-scope L0 `8d77e6c1` remains open; this round fetched under its own approval table.
