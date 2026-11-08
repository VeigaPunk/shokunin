# chousa — round 84 report

Lane HEAD before `142913a959bf99423c5546c27bb1815ed1a3a776` → after `4d5c6bdb49460c6c5ee2d55d7e81584c06761d7f`
(`git ls-remote origin refs/heads/master` prints `4d5c6bdb…`). Attempt 1; no earlier attempt of round 84 left
work.

## Work performed

Declared claims (frozen at `3b616420`, `corpus/evidence/round84/claims.md` + `.ufo/waves/round-84/claims.json`):
**C1 operability** — successor battery for repaired `tools/gate-records.py verify` (post-scoring repair
`c7d29e1c`: ASCII digit classes, rev-quote boundary). **C2 depth** — one new knowledge entry
`search-transparency-reporting-r84.md` teaching PRISMA 2020 search-reporting requirements on S214/S018/S023.

- Fresh-start reads: r80–r83 verifier spot-checks and lessons; claims frozen with two claims.
- Egress table `corpus/evidence/round84/egress-approval.md` committed before any fetch; census start exit 0.
- Fetches 2026-11-08T02:13–02:21Z: S017 landing/checklist/PDF chain, S214 PRISMA 2020 checklist PDF, S018 ACL
  2026 survey abstract, S023 DCMI terms — all HTTP 200; S020 PROV-O 403 ×3, S021/S022/S032 PubMed 203 cookie
  walls, S022 Cochrane news 404 left queued. Ledger `corpus/evidence/round57/refetch.tsv`.
- Freeze `3b616420`; landing `03bbb458` (`instrument-pins.txt`, after receipts); controls 9/9 at `d047cd8d`.
- **Post-freeze amendment `3a17f4da`** rewrote `claims.md` and all control receipts in the fetch commit
  (fresh positives 6→5, `RC=3/3`→`4/4`, C2 sources S017→S214/S018/S023, `c2-k0` semantics tool-absent→pre-repair)
  — sentinel Finding 1; counters byte-identical, rulebook not. Recorded as QUALITY 166.
- One v1 wave of 12 seats (`.ufo/waves/round-84/w1/`), integration `5e66c854`, `4d5c6bdb`.
- Census end exit 0 (`bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`;
  only the five pre-existing W04 warnings S051, S053, S073, S074, S075).

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| egress table, census start, freeze claims/counters | Round 84 bullets 1–3 | `3b616420b2dcc1f8a24a1cb9db4198c7adc8929b` |
| fetch S214/S018/S023, land entry, fix controls (incl. post-freeze claims.md rewrite) | bullets 3–4 | `3a17f4da7f2a70597a80b3900d46b9475b7de998` |
| control fixes (salad used-by, c1-d0 base rev, Q8) | bullets 4–5 | `9a2fbc3e`, `d047cd8d` |
| controls 9/9 at landing rev | bullet 5 | `e98e2a6bf79a3c52ea5b15e1e1a6a2ba9f3e7b24` |
| lesson with Gate records, mistakes, considerthese | bullet 6 | `f0cebde0` |
| instrument pins, after receipts | bullets 4–5 | `03bbb4580b39b442be69f998fae2db48d64b8c93` |
| wave spec w1 + dispatch | bullet 6 | `f099c415`, `142913a9` |
| wave w1 seat reports + receipts | bullet 6 | `8870f055`, `ab9e331d`, `8ed03947` |
| official w1-results.json, claims.json, falsification ledger | bullet 6 | `26505dbe` |
| integration: SCORECARD verdict, LOG, QUALITY 166–168 | bullet 6 | `5e66c8549ed6995e86956141886b222e86708a5d` |
| plans/round-84.md amendment record + ledger narrowing pointers | bullet 6 | `4d5c6bdb49460c6c5ee2d55d7e81584c06761d7f` |

## Before → after measurements

| claim | command | before (tree `3b616420`) | after (landing `03bbb458`, re-verified at `4d5c6bdb`) | verdict |
|---|---|---|---|---|
| C1 operability | `python3 -B corpus/evidence/round84/gate-records-r84.py --root . --repo /home/vgpnk/Projects/shokunin/chousa-shokunin --work /fast/scratch/hyaku/chousa-r84/postwave` | `TOOL=present POSITIVE=15/15 FRESH_POSITIVE=5/5 FORGED_REFUSED=288/288 EXPECTED_CODE=288/288 EMPTY_REFUSED=1/1 RC=4/4` PASS rc 0 | identical PASS rc 0 at `03bbb458` and at HEAD `4d5c6bdb` | **falsified by its own kill rules (K2) — honest stop**: setup leg non-git `--repo` prints `FAIL LINE,REV` rc 1 where frozen K2 requires `GATE_RECORDS_ERROR` rc 2 (`R84ExecRepro`, `R84ExecForge`, `R84CriticClaims`, `R84ReviewerTool`, `R84SentinelScope`, `R84ScribeLesson`); mutation seat: counter PASSes 11/34 single-point mutants, 6 accept real forgeries incl. claims' own stale-refetch/short-rev class-1 items, 7/8 enumerated r83 classes absent from the 288 (`R84MutationTool`). K3 held (21/21 lesson records OK, zero side effects, `R84ExecHarm`); K4 held (whitelist stub FAILs) |
| C2 depth | `python3 -B corpus/evidence/round84/depth-r84.py --root .` | `DEPTH_R84 entries=0 ok_entries=0 rows=0 located_quotes=0 fresh_sources=0` FAIL rc 1 | `entries=1 ok_entries=1 rows=11 located_quotes=12 fresh_sources=3` PASS rc 0 at `03bbb458` and at HEAD `4d5c6bdb` | **falsified by its own kill rules (K3) — honest stop**: decision-table row 9's Do/Never do not follow from Q10 alone; required `modified` Definition unique at S023 capture ~L8786 never quoted (`R84ReviewerEntry`; corroborated `R84ConnectorSiblings`). K2 held (12/12 quotes in captures and on 3 HTTP-200 re-opens byte-identical, `R84ExecReopen`); K4 held (`R84ScoutNovelty`) |

Knowledge `.md` count: `git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'` → 95 at base
`408ae68f`, 96 at HEAD `4d5c6bdb`. SOURCES rows `grep -cE '^\| S[0-9]{3,} \|'` → 213 → 214 (S214 added;
S018/S023 re-opened rows updated; S017 reverted to queued).

## Sources & frontier

- Census: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`
  — start exit 0, end exit 0; only the five pre-existing W04 warnings (S051, S053, S073, S074, S075).
- Rows: 213 → 214. Added by tier: A +1 (S214 PRISMA 2020 checklist PDF). Touched old → new: S018/S023 re-opened
  (status/anchor/teaches updated), S017 reverted to queued (landing page carries no quotable checklist text).
- Frontier advanced: S214 mined; S018/S023 mined; S017 stays queued; S020/S021/S022/S032 stay queued (403/203/404).
- Sourced claim: C2 rests on S214, S018, S023, all opened this round (Gate records checked).
- Mined mistakes (`corpus/lessons/round-84.md` `## Mistakes`): QUALITY 166 (post-freeze predicate amendment),
  167 (mutation-coverage vs enumeration), 168 (egress intended-targets scope).
- Assimilation: none — `merge/chousa/` collisions unchanged; considerthese 2026-11-07 entry added
  (`c555a34a`).

## Trend verdicts

- **expansion: improved** — knowledge 95 → 96 `.md`; registry 213 → 214; one new mined source (S214).
- **quality: unprovable-but-better** — the successor battery exists and passes its predicate, but the K2 setup
  leg misreports and the counter's mutation coverage is thinner than its enumeration (QUALITY 166–167); no
  capability row enters.
- **discernment: improved** — C2 reported as falsified on the wave's K3 finding without narrowing; the entry's
  other 10 rows held under full-paragraph read; sentinel process findings filed as QUALITY criteria.

Per-axis: depth improved narrowly, claim falsified; operability improved narrowly, claim falsified; calibration,
coverage, freshness, adjacency unchanged; no axis harmed. Admission is the operator's/closure's: two claims
falsified, so by the contract the round does not admit.

Round shape: one v1 wave, 12 seats (4 executor, 2 reviewer, 1 critic, 1 mutation-tester, 1 scout, 1 connector,
1 scribe, 1 sentinel; attack share 6/12 = 50%), validated rc 0 under `ufo-wave-policy.json`, spawned by the
orchestrator from `w1.ready`; 0 dead seats (`w1-results.json`, 12 outputs); no residual call; round total 12.
L1 held the planner seat. Tool installs: none. Stale-lane: respawn-per-round driver; no other mission of this
lane is open. Open L0 questions: none new (fetch-scope `8d77e6c1` stays open; this round fetched under its own
table). Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only orchestrator
`.scratch/` paths — no chousa misroot. Scratch `/fast/scratch/hyaku/chousa-r84` removed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` tool row
  `gate-records verify (r83)`; `corpus/knowledge/search-transparency-reporting-r84.md` (lane assertion; no
  non-author verifier named)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 84: sources located,
  opened, gated (`tools/gate-records.py` on the lesson, records verified); entry reviewed by
  `R84ReviewerEntry` (lane-dispatched seat)
- [~] Instructions executable by an agent without oral context — `python3 tools/gate-records.py verify --root .
  corpus/lessons/round-84.md` (rc 0); `R84ExecRepro.md`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched; `R84ConnectorSiblings.md`,
  `R84SentinelScope/sentinel.md` §2
