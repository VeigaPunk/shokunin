# chousa — round 95 report (attempt 2, L1 `ChousaR95a2`)

Lane repo `/home/vgpnk/Projects/shokunin/chousa-shokunin`, branch `master`. Base `7b2373586fb70f0ead6446c671fcc8b546d3e687`
(round-94 landing + its non-author spot-check). Final lane hash `07e0e3323db692da4f726437bbc388acea4ae5e0` (pushed).

## Work performed

Declared claims (two, distinct axes, both resting on `S222`, PRISMA-S, opened this round):

- **C1 `C1-RERUN-R95` — operability (the lowest scored axis), capability acquisition:** `tools/search-rerun.py`
  re-runs each recorded local search expression at the revision the record names and over the current tree, and
  refuses a record whose filed count or hit set differs (`COUNT_DRIFT`/`SET_DRIFT`), reporting a moved corpus
  separately (`TREE_CHANGED`).
- **C2 `C2-ENTRY-R95` — depth:** `corpus/knowledge/search-rerun-record-r95.md`, 7 decision rows warranted by 13
  located PRISMA-S quotes, with the lane's reading confined to a marked `Lane` column.

Work items:

- Attempt-1 leftovers (untracked `corpus/evidence/round95/*`, 19 files, no freeze) listed with digests and
  discarded unverified — `.ufo/waves/round-95/inherited-attempt1.txt` (commit `d6429e02`); its
  `control-driver-r95.py` had an arity bug (`input_report` returns 6 values on one path, 7 on the other).
- Read the last spot-check (`corpus/lessons/round-94-verifier-spotcheck.md`): D1–D8 are answered as append-only
  corrections in `LOG.md` Round 95 (commit `07e0e332`) and QUALITY 221; D3 is met by the S222 Gate record carrying
  URL, access date and quote (`corpus/lessons/round-95.md:25`).
- Chose a named domain gap over the planned meta-instrument layers: `corpus/README.md:398-399` ("the sweep re-run is
  a glob/existence check … never the recorded command"); reasons in `plans/round-95.md` § Why these claims.
- Source opening under an approval table (`corpus/evidence/round95/egress-approval.md`): Europe PMC full text
  answered http 500 (refetch row `2026-11-08T22:51:19Z`), the JMLA publisher PDF http 200 (capture
  `1a8c36c4c24444967bd9c3ce`, `2026-11-08T22:51:39Z`); `S222` registered (`corpus/SOURCES.md:234`).
- Built `tools/search-rerun.py` and a real 8-search record over the base capture store, recorded with GNU grep 3.12
  (`corpus/fixtures/search-rerun-r95.md`); Python and GNU grep agree on all 8 (`after-f2/c1-verify.txt`).
- Built the C1 battery `corpus/evidence/round95/rerun-controls-r95.py` and the C2 battery
  `corpus/evidence/round95/entry-controls-r95.py`; before receipts at base committed before any seat scored
  (`corpus/evidence/round95/before/c1-base.txt`, `c2-base.txt`, both exit 2) — freeze F `d6429e02`, carrier C
  `d27e9891` (`corpus/evidence/round95/after/*.txt`).
- One v1 wave of 12 seats attacked C; every seat filed (`.ufo/waves/round-95/w1-results.json`, 12 results, 0 dead).
  Nine `falsifies-wording` findings forced Amendments 1–7 (`plans/round-95.md` § Amendments), re-frozen at F2
  `86909f02`; receipts at F2 in carrier C2 `dbfc602f` (`corpus/evidence/round95/after-f2/*.txt`).
- Mutation follow-up: `corpus/evidence/round95/mutants-r95.py` rebuilds the seat's surviving mutants against the
  amended tool; first run `MUTANTS_KILLED=9/10` (`corpus/evidence/round95/controls/mutants-first-run.txt`), the
  `f10` forgery reshaped, then `MUTANTS_KILLED=10/10` (`after-f2/c1-mutants.txt`).
- Lesson with Gate and six mined mistakes (`corpus/lessons/round-95.md`), QUALITY 220–221, SKILL.md checklist item
  and Gates row, README Round95 coverage section, SCORECARD capability row and verdicts (commits `86909f02`,
  `07e0e332`).
- Planner seat: held by the L1 (the validator refuses `planner`); the planning data-walk is in
  `plans/round-95.md`.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `d6429e02` | freeze F: tool, record, both batteries, entry, S222 row + capture + refetch rows, approval table, before receipts, census start, claims, plan, attempt-1 discard list | Round 95 (Before) |
| `d27e9891` | carrier C: five receipts at F + measurement wrapper | Round 95 (After … F receipts kept) |
| `bc94923b` | wave w1 spec, builder, dispatch, ready marker, registry | Round 95 header |
| `86909f02` | freeze F2: Amendments 1–7, claims F2 sentences, SKILL/README rows, lesson, search log | Round 95 (Wave-forced amendments) |
| `dbfc602f` | carrier C2: seven receipts at F2 | Round 95 (After at F2) |
| `07e0e332` | landing: LOG, SCORECARD, QUALITY 220–221, census end, ledger, 12 seat reports and results | Round 95 + Corrections D1–D8 |

## Before → after measurements

C1 (measured against F2 `86909f02`, tree equal for the measured paths per each receipt header):

```
python3 -B tools/search-rerun.py verify corpus/fixtures/search-rerun-r95.md --root .
  before (base 7b237358): python3: can't open file '<basetree>/tools/search-rerun.py' … exit=2
  after:  SEARCH_RERUN_SUMMARY searches=8 rev_match=8/8 tree_same=3/8 findings=0 / SEARCH_RERUN: CLEAN, exit 0
python3 -B corpus/evidence/round95/rerun-controls-r95.py --root . --work <scratch>
  after:  POSITIVE=1/1 STRICT_TREE=1/1 FORGERY_REFUSED=10/10 PRIOR_ACCEPTED=10/10 SETUP_REFUSED=12/12 CLONE_TREE=2/2
          GREP_AGREE=4/4 CONTAINMENT=2/2 DO_NOTHING_REFUSED=1/1 ORACLES_REJECTED=4/4 / RERUN_CONTROLS=PASS, exit 0
python3 -B corpus/evidence/round95/mutants-r95.py --root . --work <scratch>
  after:  MUTANTS_KILLED=10/10, exit 0
```

`PRIOR_ACCEPTED=10/10` is the do-nothing instrument: `research-gate verify-sweeps` returns CLEAN on every forgery
because it reads no `## Searches` section (vacuous, `R95RevenPrior` F2). Receipts:
`corpus/evidence/round95/before/c1-base.txt`, `corpus/evidence/round95/after-f2/c1-{verify,controls,mutants}.txt`.
At F (`d6429e02`) the battery read `FORGERY_REFUSED=8/8 … ORACLES_REJECTED=3/3` (`after/c1-controls.txt`).

C2 (measured against F2 `86909f02`):

```
python3 -B tools/gate-records.py verify --root . corpus/knowledge/search-rerun-record-r95.md
  before (base): GATE_RECORDS_ERROR missing corpus/knowledge/search-rerun-record-r95.md, exit=2
  after:  GATE_RECORDS files=1 records=13 ok=13 fail=0, exit 0
bash tools/research-gate.sh verify-metadata corpus/knowledge/search-rerun-record-r95.md --root .
  after:  METADATA_COMPLETE=1/1 / RESEARCH_GATE: CLEAN, exit 0
python3 -B corpus/evidence/round95/entry-controls-r95.py --root . --work <scratch>
  after:  POSITIVE=1/1 FORGERY_REFUSED=8/8 BINDING_REFUSED=3/3 DO_NOTHING_REFUSED=1/1 ORACLE_REJECTED=1/1
          LQ_BOUND=13/13 WARRANTS_OK=7/7 WARRANT_TERMS=7/7 LANE_FILLED=7/7 / ENTRY_CONTROLS=PASS, exit 0
```

Receipts: `corpus/evidence/round95/before/c2-base.txt`, `corpus/evidence/round95/after-f2/c2-{gate,metadata,controls}.txt`.
At F the entry carried 9 records (`after/c2-gate.txt`); Amendment 1 added four located fragments.

No axis harmed: `git diff --quiet 7b237358 07e0e332 -- tools/research-gate.sh tools/gate-records.py PROVINCE.md` exit 0;
on the landing tree `SKILL_TALLY_R94=PASS` and `CURATION_R94=PASS`.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`
  — start exit 0 (`corpus/evidence/round95/census-start.txt`), end exit 0 (`corpus/evidence/round95/census-end.txt`),
  the same five pre-existing `W04` warnings both times.
- Rows: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` → 220 at base, 221 at landing.
- Added by tier: A 1 (`S222`, PRISMA-S, JMLA publisher PDF, status `mined`, used-by the C2 entry). B 0, C 0.
- Touched old→new: none (no existing row's status/recheck/used-by changed). One correction to the new row's source
  cell is recorded in the lesson Gate, not in the row (`10:39` came from a web-search summary, not the capture).
- Rejected: the Europe PMC route (url/unreach Gate record, curl rc 22, http 500).
- Frontier advanced: README gap 398-399 closed for local searches over committed lane files (README Round95
  section); left open: non-local re-runs, recall, PRISMA-S items 14 and 16.
- Sourced claims: C1 and C2 both cite `S222`, opened this round.
- Mined mistakes: six rows in `corpus/lessons/round-95.md` `## Mistakes`, each with captured-by and a shown-able-to-fail fix.
- Assimilation: none (no `merge/chousa/` theme or `considerthese/` proposal taken this round).

## Trend verdicts

- **expansion: improved** — a capability row enters SCORECARD (`## Capabilities (round-95 addition)`) and a
  standard the lane never held as text (PRISMA-S checklist and explanations) becomes a knowledge entry; the README
  frontier gap 398-399 moves for local searches. Registry +1 row.
- **quality: improved** — the new tool and entry each pass a battery whose controls were committed before any seat
  scored, and every wave falsification was answered by a repair covered by a new leg the F state fails
  (`oracle-carrier-c-tool`, `BINDING_REFUSED`); no admitted older entry was found false.
- **discernment: improved** — nine wording falsifications were taken before filing and both sentences narrowed to
  what the instruments enforce (Amendments 6, 7); round-94 routed defects D1–D8 recorded as corrections. Author
  verdict; the non-author closure decides.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:81-82` new
  executable checklist item (search re-run, S222) and Gates row `SKILL.md:177` (lane assertion; no non-author verifier)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 95: 8 real searches of the
  capture store recorded with GNU grep and re-run by the new tool; PRISMA-S opened, captured and quoted
  (`corpus/evidence/round95/after-f2/`) (lane assertion)
- [~] Instructions executable by an agent without oral context — `corpus/evidence/round95/measure-r95.sh` re-emits
  every receipt; `.ufo/waves/round-95/claims.md` F2 predicates (lane assertion)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched; sibling count re-checks routed,
  not absorbed (`.ufo/waves/round-95/w1/R95ConnectorSiblings.md`)

## Round shape, seats, settlement

One v1 wave (policy `ufo-wave-policy.json`, band 8–16), 12 seats, dispatched through the inline handoff
(`.ufo/waves/round-95/w1.ready` → `w1.ready.dispatched`), settled with `WAVE-DONE` and
`.ufo/waves/round-95/w1-results.json` (12 results, 0 dead). No residual call; round total 12. Role mix: executor 3
(one is the engine-agreement probe the validator would not accept as `labrat`), reviewer 2, sentinel 1,
mutation-tester 1, critic 1, revenger 1, connector 1, scout 1, scribe 1. Attack seats (reviewer, critic,
mutation-tester) 4/12 = 33 %; with sentinel, revenger and connector, 7/12.

## Pre-file falsification

```
$ awk -F'\t' '{c[$3]++} END{for(k in c) print k, c[k]}' .ufo/waves/round-95/claim-falsification.tsv
neutral 7
falsifies-wording 9
$ python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane chousa --round 95
PREFILE-FALSIFICATION: pass claims=2 rows=16 attack_seats=7 findings=0
$ echo $?
0
```

Every `falsifies-wording` row points at `plans/round-95.md` § Amendments, where the narrowing or repair is named
with its seat.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Tooling

No tool installed or upgraded.

## Open L0 questions

None added this round. Fetch-scope L0 `8d77e6c1` remains open; this round fetched under its own approval table.
