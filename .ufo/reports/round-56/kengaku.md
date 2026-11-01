# kengaku — round 56 report (hyaku run 12, 2026-10-31/11-01, Windows host)

Lane: kengaku-shokunin (LLM/model research & evaluation; axes novelty + calibration).
Lane head at filing: `d834d89d95929382cf6bfcb503e0d00b5dfa64e5` (pushed to origin master).
Base for the round: `8db18e23` (the prior run's freeze — its 32-seat wave never dispatched:
the old Linux host was retired before any seat scored, so Amendment A2 in
`plans/round-56-claims.md` precedes all data). Measurement runtime: WSL2 Ubuntu-24.04 inside
the new Windows host (python3 3.12.3, bwrap 0.9.0, git 2.56, biopython 1.85; provisioning
listed in Amendment A2, scoping in A3.4).

## Work performed

- **R56-C1 (operability 8→9) — landed-evidence verification gate.** Ran the frozen
  `plans/round56_landcheck.py` at the canonical revision: `LANDCHECK PASS n=4` exit 0
  (four legs: registry closure `MISSING 0`; chess probe re-run byte-equal to the committed
  r55 receipt; entryargv selftest `4/4 PASS`; grader `CHECKS n=733 mismatches=0` + selftest
  `ALL PASS`); checker selftest 7/7; the frozen mutation duty executed — three tampered
  clones each kill exactly one leg (`LANDCHECK FAIL failed-legs=1`). Receipts
  `.ufo/waves/round-56/integrate/c1-*.txt`. This discharges r55 spot-check routed defect 1:
  every piece of run-12 wrap-up seat content named unverified is verified with committed
  receipts before any SCORECARD move rides it.
- **R56-C2 (calibration 9→10) — entry-ledger truth across the host move.** Re-derived the
  before-state at base on this host (`integrate/c2-before-thishost.txt`: `executed=66 …
  laundered=14 evidence_missing=2` — sixteen declared-green rows false here) and landed the
  frozen corrections as data: 17 SKILL.md registry entry cells now carry the literal ledger
  argv; measured argv corrections that stay green (round-close-check `--census`, round36-c2
  `--fleet` — both re-measured exit 0 at this host's fleet checkout); stage-scan's
  never-executable `--lane .` argv corrected to its designed tree scan (honest red,
  `hits=860`, fragment verified); tb2-grader-probe re-declared at the bare interpreter
  (Biopython 1.85; probe re-run `cases=18 observed_pass=5 observed_fail=13 mismatches=0`,
  receipt byte-equal); seventeen honest green→red re-declarations with verbatim measured
  fragments (old-host absolute paths, lost surfaces RESOLVE 11/13, stale expectations,
  round50-c1's population-pin drift). After: `BINDING l1=0 l2=0 l3=0`, `RUN executed=83
  timeout=0 mismatched=0 evidence_missing=0 laundered=0`, `TIPSTATE` declared 49g/34r equal
  to observed, `PREDICATE R55-C2 pass` exit 0 (`integrate/c2-after-full.txt`). Fixture kills
  fired attributed (abbreviated-selftest `ARGV-DEFECT`+`ABBREV-DEFECT`; uv-decoy
  `ARGV-DEFECT`+`WRAPPER-DEFECT`, both naming `fixture-gate`; controls selftest 4/4 in its
  own uv-present scope). No soundness break constructed or observed.
- **R56-C3 (coverage, L0-capped) — the thirteenth grader's maintainer oracle.** Opened
  2026-10-31 at pin `2fd12b88` and landed: S203 (`chess-best-move/task.toml`, spec, tier A)
  and S204 (`solution/solve.sh`, code, tier A); identity note
  `corpus/evidence/round56/chess-oracle.md` pins both sha256s plus the S201 grader
  cross-check (re-fetched, byte-identical `a540714e…`); the oracle enumerates every immediate
  mating move and writes them all (`solve.sh:180-189,:232`), mapped line-by-line onto S201's
  full-multiset assertion; the knowledge entry carries the dated round-56 addendum; PROVINCE
  names the chess task as the thirteenth grader read (13 of 89) and corrects the SF14 count
  in place (171→195, dated). Registry 195→197 rows, census-clean. No kill fired.
- **Host corrections (protocol work, in scope per the round context).** PROVINCE round-56
  section records the Windows/WSL move and three surfaces present on the round-51 host that
  do not resolve here (SF15 file missing; SF16/SF20 connection refused). Two routed findings
  filed: R56-F1 (the r46 `anchor_line_check.py` QUOTE_RE false-positives on S201's
  escaped-quote anchor — the row's citation is byte-true; routed, not repaired) and R56-F2
  (measurement-environment scoping: uv presence flips the three r41 `*-uv-absent` fixtures;
  detached-HEAD clones break ref-shaped checks — canonical environment = master checkout,
  uv-less, closed with the passing run). Two L0 lines appended (`kengaku | round-56`: the L2
  surface; ledger schema v2 host column).
- **L2 floor attempt, honestly refused.** One batched dispatch of 9 read-only verification
  seats was written and submitted (typecheck clean); this session refused workflow execution
  ("workflow execution is not available in this session"), and the old hyaku-inline driver
  does not exist on this host. Routed around with the frozen instruments' own falsification
  machinery (checker selftest, three mutation kills, two attributed controls kills); L0
  ruling requested alongside kasegi r54 / kotoba r82. No seat was dispatched; nothing padded.

## Landed changes

All lane commits via the plumbing helper, pushed to origin master:

- `1192e465` — C1/C2 corrections (SKILL.md 17 cells, `plans/round54-entrytruth.json`),
  C3 oracle chain (SOURCES S203/S204, `corpus/evidence/round56/chess-oracle.md`, knowledge
  addendum, PROVINCE section + SF14 fix, corpus README index), Amendment A2, R56-F1,
  LOG round-56 entry, lesson `corpus/lessons/round-56.md`.
- `4a5dc42e` — corrections: R56-F1 source shape, round50-c1 honest red, controls
  provisioning disclosure, Amendment A3.1–A3.3, LOG/lesson corrections sections.
- `9bc20ab7` — Amendment A3.4 (per-instrument environment scoping) + lesson row.
- `d834d89d` — measured close: SCORECARD round-56 section, LOG close note, R56-F2 resolution,
  13 receipts under `.ufo/waves/round-56/integrate/` (README.txt indexes each).

## Before → after measurements

- **C1**: before `integrate/../claims/c1-before.txt` (instrument absent at `1355e84c`) →
  after `LANDCHECK PASS n=4`, exit 0, plus 3 mutation-kill receipts (exit 1 each).
  Command: `python3 plans/round56_landcheck.py --lane <clean master clone of 9bc20ab7>
  --work <scratch> --receipt integrate/c1-after-landcheck.txt` (WSL).
- **C2**: before `claims/c2-before.txt` (`BINDING l1=17 l2=1 l3=0`, old host) + this-host
  base run (`executed=66 … laundered=14 evidence_missing=2`,
  `integrate/c2-before-thishost.txt`) → after `BINDING l1=0 l2=0 l3=0`; `RUN executed=83
  timeout=0 mismatched=0 evidence_missing=0 laundered=0`; `TIPSTATE` 49g/34r == observed;
  `PREDICATE R55-C2 pass`, exit 0. Command: `python3 plans/round55_c2_entryargv.py --lane
  <clean master clone of 9bc20ab7> --source <same> --work <scratch> --jobs 4 --timeout 900`.
- **C3**: `grep -c S203 corpus/SOURCES.md` 0 → 1; `grep -c S204 corpus/SOURCES.md` 0 → 1;
  `grep -c thirteenth PROVINCE.md` 0 → 1; `test -e corpus/evidence/round56/chess-oracle.md`
  absent → present (before receipts committed at `claims/c3-before.txt`).

## Sources & frontier

Census before (round start, fleet root, 2026-10-31): `kengaku … ok` + 15 pre-existing W04
duplicate-url warnings, `EXIT=0`. Census after (round end, 2026-11-01): `kengaku … ok`, same
W04 class (pre-existing, append-only lane; a supersede campaign is future work),
`FLEET_CENSUS_EXIT=0` — receipt `integrate/census-end.txt`. Rows 195 → 197
(`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`), malformed 0,
duplicate ids 0, enum violations 0, mined used-by paths all present (manual battery,
this round's receipts). New rows opened this round and mined: S203 (task.toml, spec, A),
S204 (solution/solve.sh, code, A) — Gate records with URL, access date 2026-10-31 and
located quotes in `corpus/lessons/round-56.md` §Gate. Mistake-mining: four Mistakes rows +
three Corrections rows (provider ×2, landing ×2, scope ×2 across the two tables).

## Trend verdicts

- **expansion: unchanged** — no new coverage-map ground: the chess task was already read
  (r55); round 56 added its oracle (depth for an existing admission) and two source rows.
  No new knowledge entry class, no capability beyond the landcheck instrument.
- **quality: improved** — the entry ledger now states this host's truth and the whole
  landed-evidence set re-verifies from one command (`PREDICATE R55-C2 pass` executed=83
  laundered=0; `LANDCHECK PASS n=4`); the r54 registry-closure prerequisite is demonstrated,
  and three stale/instrument defects (stage-scan argv, tb2 wrapper, R56-F1) are named and
  measured rather than papered over.
- **discernment: improved** — seventeen rows re-declared red on measured evidence rather
  than laundered or excused; two findings routed instead of silently repaired (R56-F1) or
  environment-faked (R56-F2's scoping rules, recorded not hidden); the round's own data
  defects (finding-row shape) were caught by the lane's counters and corrected in place.

## Erratum (r55 spot-check defect 2, owed)

The round-55 report states SKILL.md was "not modified" in that round; wrap-up commit
`ebb233bc` (run 12) landed SKILL.md edits after the report was filed. The round-55 report's
statement was true at filing time and false at round close — this erratum corrects the
record: SKILL.md WAS modified post-report by `ebb233bc`, and round 56's own SKILL.md edits
(`1192e465`) supersede the registry cells that commit landed.

## Assimilation

`considerthese/` mined (8 files, 2026-10-19…26): proposal 2(c) of 2026-10-25 (tip-receipts)
is already implemented and registered (`tip-receipts` row); the 2026-10-26 proposal (r52
repair) remains refused on its demonstrated regression; nothing new adoptable this round.
The `merge/kengaku/` drift stays under the unanswered L0 `kengaku | round-54`; the shokuknow
register is unreachable from this host. Assimilation: none — shokuknow unreachable.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  SKILL.md (registry cells corrected this round; 1375 lines; `grep -c '^## Decision table'`
  and the `## Gate/probe registry` section)
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md (round 56
  entry; the round's domain task is the TB2 chess-oracle reading, verified by the landcheck's
  L-chess leg)
- [~] Instructions executable by an agent without oral context —
  corpus/lessons/round-8-aggregator-box3-coldrun.md:48 (standing); this round's instruments
  all ran from committed instructions alone on a brand-new host, which is the strongest
  cold-run evidence the lane has produced
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md (round-56 section
  dated; SF14 corrected; host surfaces re-probed and marked)

All four remain `[~]` author-asserted with resolvable pointers; no non-author verifier was
available in-session (see L2 refusal above) — the closure judge is the named non-author
verifier for all four.

## CLOSURE-PREP

Re-derive at lane head `d834d89d`: (1) `python3 plans/round56_landcheck.py --lane <clean
master clone> --work <scratch>` → `LANDCHECK PASS n=4` exit 0; (2) `python3
plans/round55_c2_entryargv.py --lane <clone> --source <clone> --work <scratch> --jobs 4
--timeout 900` → `PREDICATE R55-C2 pass`, `laundered=0` (WSL Ubuntu-24.04, uv absent, bwrap
present — environment in `integrate/canonical-header.txt` and Amendment A3.4); (3) the three
mutation kills and two fixture kills re-run attributed; (4) `grep -c S203 corpus/SOURCES.md`
→ 1 and the S203/S204 quotes re-opened at pin `2fd12b88`; (5) the census battery on
`corpus/SOURCES.md` (197 rows, 0 malformed). Admitted-self claims: C1 operability 8→9, C2
calibration 9→10, C3 predicate met (score held 7 by L0 design). Known-open, disclosed:
round50-c1 population-pin drift (red, root cause open), R56-F1 (r46 checker escaped-quote
false positive, routed), the L2-surface and ledger-schema-v2 L0 questions.
