# chousa — round 85 report

Lane HEAD before `43c3f7284eee4889cdcc6ac1626573f6579cd533` → after `a8041fcdedb2a5bcddf366f4e4b004bc23375c77`
(`git ls-remote origin refs/heads/master` prints `a8041fcd…`; `jj-lane.sh state` → `ahead=0 behind=0`). Attempt 1; no
earlier attempt of round 85 left work (`.ufo/watchdog.log` has no `lane-dead-no-report chousa round=85`;
`.ufo/waves/round-85/` did not exist at round start).

## Work performed

Declared claims (frozen at `5d0b9413`, amended pre-data at `02df67db`: `corpus/evidence/round85/claims.md` +
`.ufo/waves/round-85/claims.json`): **C1 operability** — the round-85 repair of `tools/gate-records.py verify`
(non-git/empty `--repo` is a setup error exit 2; REFETCH success is http exactly 200, not 2xx; `fetched` must be a real
calendar instant) passes a successor battery (`corpus/evidence/round85/gate-records-r85.py`). **C2 depth** — one new
knowledge entry `provenance-recording-r85.md` teaching provenance recording on S215/S026/S024.

- Fresh-start reads: r81–r83 lessons and verifier spot-checks, r84 lesson and `round-84-verifier-spotcheck.md` (its
  routed defects 1–3 are C1/C2's specification), `considerthese/2026-11-06.md` and `2026-11-07.md`.
- Egress table `corpus/evidence/round85/egress-approval.md` committed at the freeze `5d0b9413` before any fetch;
  census start exit 0 (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`).
- Fetches 2026-11-08T03:54–04:16Z: S023 DCMI re-open (HTTP 200, attempt 2); S215 PROV-O via the W3C alternate URL
  (403 twice, 200 on the third attempt with the plain UA — the campaign UA is refused by W3C); S026 GO FAIR R1.2
  (200); S024 Schema.org lastReviewed (200). The canonical `REC-prov-o-20130430` URL was **not** fetched this round
  (six 403 rows, all round-84). Ledger `corpus/evidence/round57/refetch.tsv`.
- Freeze `5d0b9413`; pre-data amendment `02df67db` (C2 ground re-pointed to the three opened sources after the first
  candidate scored `E6,E7`; depth-counter section parser repaired before any scored data; C1 setup leg moved into the
  counter; the C1 counter's `kv_set` absent-key guard — `plans/round-85.md` amendments 1–7b, 9–10, `corpus/QUALITY.md`
  169–172). Controls: `c1-k0-donothing` FAIL `SETUP=0/1`; `c2-d0-donothing` FAIL (`entries=0`); accept/refuse/whitelist
  stubs FAIL (`corpus/evidence/round85/controls/receipts/`).
- Landing `64803d33` carries the tool repairs, the entry, registry rows (S215 new; S026/S024 mined), the lesson, the
  plan and `claims.json`; `corpus/evidence/round85/after/` holds both predicates at that tree, rc 0 each.
- One v1 wave of 12 seats (`.ufo/waves/round-85/w1/`), validated rc 0 under `ufo-wave-policy.json`, spawned by the
  orchestrator from `w1.ready`; 12 settled, 0 dead (`w1-results.json`, 12 outputs); no residual call; round total 12.
- `R85ExecForge` added 58 new in-class forgeries beyond the battery (all refused with their documented codes) and
  supplied the 203 accept-boundary pair (base tool `OK` → landing tool `FAIL REFETCH`), corroborating the committed
  fixture `corpus/evidence/round85/forge-203.py`.
- Post-scoring repairs (disclosed, not counted toward the verdicts): `admit` requires `decision=admit`; `--repo ''`
  refuses as a setup error; entry rows 1 and 5 Never cells narrowed to what Q1/Q3/Q6 state.
- Lane gate selftest: `bash tools/research-gate.sh --selftest` → `RESEARCH_GATE_SELFTEST: PASS (283 cases, 0 skipped)`
  (`corpus/evidence/round85/measure/gate-selftest-r85.log`); preflight G01–G07 PASS
  (`corpus/evidence/round85/measure/preflight-g01-g05.log`, `preflight-g06-g07.log`). r83 and r84 counters still PASS
  on the repaired tool.
- Pre-file ledger: `PREFILE-FALSIFICATION: pass claims=2 rows=13 attack_seats=6 findings=0` (exit 0).
- Census end exit 0 (same five pre-existing W04 warnings S051/S053/S073/S074/S075).

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| frozen claims, counters, controls, egress table | Round 85 bullets 1–3 | `5d0b94139ae8baf60d6f630715bc495f0a93b448` |
| pre-data amendment: C2 ground S215/S026/S024, depth-counter parser, setup leg, `kv_set` guard | bullets 3–4 | `02df67db4f9ad39f8ebc73984ce50ea1fbea315f` |
| landing: tool repairs, entry, registry S215/S026/S024, lesson, plan, claims.json | bullets 4–6 | `64803d33362f50cf9094e91fc3a4a07216c563ca` |
| wave spec w1 + dispatch + ready handoff | bullet 7 | `863d624e7245e1e11086c60295bbcccf52d8dcec` |
| wave w1 seat reports, receipts, `w1-results.json` | bullet 7 | in `a8041fcd` |
| post-scoring repairs (tool guards, entry rows 1/5), lesson corrections, SCORECARD/LOG/QUALITY 169–172, ledger | bullets 3–8 | `a8041fcdedb2a5bcddf366f4e4b004bc23375c77` |

## Before → after measurements

| claim | command | before (base `43c3f728`, counters from the landing copied byte-exactly) | after (landing `64803d33`) |
|---|---|---|---|
| C1 operability | `python3 -B corpus/evidence/round85/gate-records-r85.py --root <tree> --repo /home/vgpnk/Projects/shokunin/chousa-shokunin --work <dir>` | `TOOL=present POSITIVE=15/15 FRESH_POSITIVE=5/5 FORGED_REFUSED=354/354 EXPECTED_CODE=342/354 EMPTY_REFUSED=1/1 RC=4/4 SETUP=0/1`, `GATE_RECORDS_R85=FAIL` rc 1 (`controls/receipts/c1-k0-donothing.txt`) | `... FORGED_REFUSED=354/354 EXPECTED_CODE=354/354 ... SETUP=1/1`, `GATE_RECORDS_R85=PASS` rc 0 (`after/c1-after.txt`) |
| C2 depth | `D=$(mktemp -d -p /fast/scratch/hyaku) && git archive <rev> \| tar -x -C "$D" && python3 -B "$D/corpus/evidence/round85/depth-r85.py" --root "$D"` | `DEPTH_R85 entries=0 ok_entries=0 rows=0 located_quotes=0 fresh_sources=0` FAIL rc 1 (`controls/receipts/c2-d0-donothing.txt`) | `DEPTH_R85 entries=1 ok_entries=1 rows=6 located_quotes=7 fresh_sources=3` PASS rc 0 (`after/c2-after.txt`) |

Both frozen claims are reported **honest stop** on their stated wording; each sentence's narrower property is
measured: C1's three repairs (amendments 7/7b: setup and calendar legs load-bearing in-battery — mutants M28/M29,
M18/M19 killed; the 200-only repair witnessed by `forge-203.py`: base `rc 0 OK` → landing `rc 1 FAIL REFETCH`), and
C2's S026/S024 ground with the PROV rows re-emitting the S033 document (amendments 8–10; K3 fired on rows 1/5 on the
scored bytes; floors relaxed beside the ground change although the prefreeze floors were reachable). The frozen bytes
are not re-based after scoring; the reports and receipts stand as measured.

Knowledge `.md` count `git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'` → 96 at base
`43c3f728`, 97 at the landing `64803d33`. SOURCES rows `grep -c '^| S'` → 214 → 215 (S215 added; S026/S024
queued → mined; S023 re-opened, `used-by` unchanged).

## Sources & frontier

- Census start exit 0 and end exit 0 (`bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`); only the five pre-existing W04 warnings.
- Rows: 214 → 215. Added by tier: A +1 (S215 PROV-O alternate URL). Touched old → new: S026 `queued`→`mined`,
  anchor gains capture key `67983a3db…` (row `teaches` rewritten to its located facets), used-by `—`→the new entry;
  S024 `queued`→`mined`, anchor gains capture key `11d6cc5…`, used-by `—`→the new entry; S023 unchanged in status,
  anchor gains a re-open note and a 2026-11-08T03:54:40Z refetch row; S020 unchanged (canonical URL 403 ×6,
  alternate URL now the S215 row — disposition routed).
- Frontier advanced: S026 and S024 mined on provenance ground no base entry held (FAIR R1.2 facets, Schema.org
  `lastReviewed`); S215 registers the alternate URL of the PROV-O document the lane already holds as S033, disclosed
  as a re-emission rather than new ground (amendment 9). S020's dead canonical URL is routed to round 86; the open
  fetch-scope L0 `8d77e6c1` is unchanged.
- Sourced claim: C2 rests on S215, S026, S024, opened this round; the lesson `## Gate` carries three `GATE-RECORD`
  lines verified by `tools/gate-records.py` (`GATE_RECORDS files=1 records=3 ok=3 fail=0`, exit 0).
- Process defects disclosed rather than hidden: S026 and S024 were fetched although the egress table's
  intended-targets list named only S023 and S020 (amendment 6, QUALITY 170); the alternate URL received four GETs
  against a three-attempt limit, and one refetch row carries an id (`S033`) that is not the row's URL owner
  (lesson Corrections block); the C1 counter's bytes changed from the freeze pin `931b5ed7…` to the landing pin
  `62496d36…` and the landing commit carries the first scored receipt (amendments 4, 7b; the frozen bytes score the
  correct tool 354/378 → FAIL, so the repair was necessary to measure anything).
- Mined mistakes (`corpus/lessons/round-85.md` `## Mistakes` + Corrections): QUALITY 169 (a frozen ground/floors
  scored against the counter's own rules before the freeze), 170 (freeze-integrity and egress-set discipline, with
  this round's own defects named), 171 (a class without a forgery is not load-bearing; survivors name the next
  fixture), 172 (floors are not relaxed beside their ground; a criterion's cited receipt must exist).
- Assimilation: none — `merge/chousa/` collisions unchanged (111 lines, `R85ScribeLesson` receipt 10);
  considerthese 2026-11-07 kept and one still-unimplemented proposal named (the twelve r80 backlog Gate ids).

## Trend verdicts

- **expansion: improved narrowly** — knowledge 96 → 97 `.md`; registry 214 → 215; S026/S024 newly mined on ground no
  base entry held. Narrowed reading (amendment 9): the PROV rows re-emit the S033 document rather than adding ground.
- **quality: improved narrowly** — three real tool repairs land with witnesses, the instrument's own `kv_set` defect
  is closed, and four criteria are mined; both claims still honest-stop as stated, and no capability row enters.
- **discernment: improved** — the wave falsified both claims with receipts (two reviewer seats, critic, mutation,
  revenger), the lane published its own freeze/egress/floor defects, and the ledger reconciles every attack seat
  (`pass claims=2 rows=13 attack_seats=6 findings=0`).

Per-axis: operability improved narrowly (claim not admitted as written); depth improved narrowly (claim falsified);
calibration improved; coverage, freshness, adjacency unchanged; no axis harmed (gate selftest `PASS (283 cases, 0
skipped)`, preflight G01–G07 PASS, census exit 0 at both ends, r83/r84 counters still PASS). Admission is the
operator's/closure's: neither claim verifies as frozen, so by the contract the round does not admit.

Round shape: one v1 wave, 12 seats (4 executor, 2 reviewer, 1 critic, 1 mutation-tester, 1 revenger, 1 scout,
1 connector, 1 scribe; attack roles 6/12 = 50% by the ledger's role set, of which reviewer/critic/mutation/revenger
are 5), validated rc 0 under `ufo-wave-policy.json`, spawned by the orchestrator from `w1.ready`; 0 dead seats
(`w1-results.json`, 12 outputs); no residual call; round total 12. L1 held the planner seat. Tool installs: none.
Stale-lane: respawn-per-round driver; no other mission of this lane is open. Open L0 questions: none new (fetch-scope
`8d77e6c1` stays open; S020 disposition is routed, not asked). Misroot sweep: `git -C /home/vgpnk/Projects/shokunin
status --porcelain` shows only orchestrator `.scratch/` paths, other lanes' reports and this report — no chousa
misroot. Scratch `/fast/scratch/hyaku/chousa-r85` removed after landing.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` tool rows
  `gate-records verify (r83)` and `(r85 repair)`; `corpus/knowledge/provenance-recording-r85.md` (lane assertion;
  no named non-author verifier)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 85: sources located, opened,
  gated; the entry checked by `R85ReviewerEntry` and `R85ExecReopen` (lane-dispatched seats)
- [~] Instructions executable by an agent without oral context — `python3 tools/gate-records.py verify --root .
  corpus/lessons/round-85.md` (3 OK, rc 0); `R85ExecRepro.md`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched; `R85ConnectorSiblings.md`
