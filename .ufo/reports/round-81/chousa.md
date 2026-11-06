# chousa — round 81 report (fresh start, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/chousa-shokunin`, branch `master`. Base `378fda82dc2cbcc555a0565052cc408121813cef`
(round-80 tip, closed `rejected-honest-stop`). Final lane tip **`6ef7929234f5116af79014e371fff6131c588abe`**, confirmed by
`git ls-remote origin refs/heads/master`. L1: `ChousaR81`. Earlier attempts: none. `.ufo/watchdog.log` holds no
`lane-dead-no-report chousa round=81` line, and the lane was clean at start (`jj-lane.sh state`: tracked=0 untracked=0).

## Work performed

Declared claims (frozen at `bb54e7f8`, `corpus/evidence/round81/claims.md`):
**C1 depth (sourced on S203–S207)**: two new `corpus/knowledge/` entries on research-method ground.
**C2 operability (the lowest-scored non-retired axis, historical 3/10)**: checklist items 2, 4 and 5 of SKILL.md
`## Checklist (executable)` get `Run:` lines, and those lines discriminate on frozen fixtures.

- **Fresh-start reads.** Read MANIFEST closure rows 1288, 1294 and 1314 (r78, r79, r80) and their spot-checks
  `corpus/lessons/round-7{8,9}-verifier-spotcheck.md` and `round-80-verifier-spotcheck.md`. Shared root cause: ten
  rounds went into hardening the lane's own forger batteries. Every frozen predicate in that run was falsified by the
  next forger, and depth, coverage and freshness stayed `unchanged` throughout. This round leaves that surface
  (`claims.md` §Fresh-start reads).
- **Sources opened** (`tools/capture-fetch.py`, refetch rows 2026-11-06T18:44:29–31Z, `corpus/evidence/round57/refetch.tsv`):
  - S203: the TARCiS accepted manuscript (PDF).
  - S204: the Campbell searching guide.
  - S205: the NLM errata/retraction policy.
  - S206: ICMJE corrections and version control.
  - S207: Crossref's Retraction Watch documentation.
  - S208: the BMJ correction q2458, which returned HTTP 403 and was registered as a rejected row.

  Bytes are in `corpus/captures/` and were committed at `f7929f87`.
- **Egress table.** `corpus/evidence/round81/egress-approval.md`. It was written *after* the fetches. The disclosure is
  in the file itself and in a lesson `## Mistakes` row.
- **Prefreeze controls** at `f7929f87`, committed before the freeze. Counters are `depth-r81.py` and
  `checklist-run.py`; fixtures are in `checklist-fixtures/`; the driver is `run-controls.sh`. Receipts in
  `corpus/evidence/round81/controls/` show the expected rc on all 16:
  - Do-nothing controls: C1 `entries=0 FAIL` rc 1; C2 `3/6 0/3 FAIL` rc 1.
  - Seven C1 grounding forgers, each rc 1.
  - Five C2 forgers, each rc 1 or 2.
  - Positive controls: both rc 0.
- **Candidate landing** `7e2da96a`:
  - `corpus/knowledge/citation-searching-tarcis-r81.md` and `corpus/knowledge/correction-retraction-status-r81.md`.
  - Registry rows S203–S208.
  - SKILL.md Run lines for items 2, 4 and 5.
  - `negA-probe.md`. Before landing, the L1 found that `verify-sweeps` alone exits 0 on a negative claim that has no
    sweep, so the item-2 line was made composite.
- **Wave w1** (12 seats, validated rc 0, `.ufo/waves/round-81/w1-validate.rc`). Each seat attacked or measured the
  landing; reports are in `.ufo/waves/round-81/w1/`, results in `w1-results.json`. Key findings:
  - `R81ExecReopen`: C1 K2 held. All 14 counted quotes were re-opened live. 7 are VERBATIM via `quote-reopen.py`, and
    7 are present in the live S203 PDF, which is byte-identical to its capture.
  - `R81ExecRepro`: both predicates reproduce. Instrument sha256 match 8/8, and controls 16/16 are byte-identical.
    C2 K2 fired.
  - `R81ReviewerC2`: C2 K2 fired. Six item-2 records and five item-4 records exit 0.
  - `R81ExecTrial`: an end-to-end trial research record was run through the checklist. C2 K2 fired again.
  - `R81CriticClaims`: two 10-line filler entries reach `DEPTH_R81=PASS` (`receipts/r09-c1-filler-entries.txt`).
  - `R81ReviewerEntries`: K3 fires in spirit on one E2 row (S206 line 222). It also listed 8 non-firing defects.
  - `R81MutationCounters`: survivors are 12/18 for C1 and 9/17 for C2. The P4 shared-quote branch is unexercised, and
    `PASS` can print beside `5/6`.
  - `R81ScoutNovelty`: the landing left the G02 knowledge-index gate failing. Base S120 already cited TARCiS.
  - `R81ConnectorSiblings`: no sibling holds either topic.
  - `R81SentinelScope`: egress S1–S5 (ordering, a self-contradictory seat row, seat GET count, a lesson pointer, and
    a snippet warrant).
  - `R81ScribeR80Defects` and `R81ScribeLesson`: drafts, integrated by the L1.
- **Integration** `6ef79292`:
  - Verdicts recorded.
  - Lesson `corpus/lessons/round-81.md`.
  - Both entries repaired after scoring (quality fixes only; no verdict changes).
  - SKILL.md pass-through notes added.
  - README round-81 coverage section added; G02 PASS restored (`tools/lane-preflight.py --only G02` → `PREFLIGHT=1/1`).
  - QUALITY 161–162 added.
  - r80 routed defects 1–6 closed append-only (`corpus/lessons/round-80.md` tail, `SCORECARD.md` Correction 2).
  - SCORECARD round-81 verdict plus the r82 plan; LOG entry.
- **Planner seat.** The L1 held the canonical §3 planner seat. No planner role is in the wave because the validator
  rejects it.

## Landed changes

| commit (`landed`) | contents | LOG.md entry |
|---|---|---|
| `f7929f877e6fd54f4dc5ce7f993da46bc7df43f9` | counters, fixtures, control driver + 16 receipts, egress table, 5 captures, refetch rows, census-start | Round 81 |
| `bb54e7f89da9ba4213aec9d976c13f3f4ba548fb` | frozen `claims.md` | Round 81 |
| `7e2da96a0541946e796384d42fea18e09ede9e9f` | two entries, SOURCES S203–S208, SKILL Run lines, negA probe (scored bytes) | Round 81 |
| `b1ed9b6ad61f0af9e44a190c666a8f6d10264c8e` | w1 spec, dispatch, validate | Round 81 |
| `6ef7929234f5116af79014e371fff6131c588abe` | integration (see above) + wave evidence, census-end | Round 81 |

## Before → after measurements

| claim | counting command | before (base `378fda82`) | after (measured at `7e2da96a`) | verdict |
|---|---|---|---|---|
| C1 depth | `D=$(mktemp -d -p /fast/scratch/hyaku) && git archive <rev> \| tar -x -C "$D" && python3 -B corpus/evidence/round81/depth-r81.py --root "$D"` | `DEPTH_R81 entries=0 fresh_rows=0 located_quotes=0` / `FAIL` rc 1 | `entries=2 fresh_rows=5 located_quotes=14` / `PASS` rc 0 (at `6ef79292`: 15 quotes, PASS) | **honest stop**: K1 and K2 held. The counter accepts filler entries (a §9 cheapest-control defect, now QUALITY 162), and one table row contradicted its cited source (K3 in spirit, repaired) |
| C2 operability | `python3 -B corpus/evidence/round81/checklist-run.py --root <tree>` | `CHECKLIST_RUN=3/6 DISCRIMINATE=0/3` / `FAIL` rc 1 | `CHECKLIST_RUN=6/6 DISCRIMINATE=3/3` / `PASS` rc 0 | **falsified by its own kill rule K2 (honest stop)**: item 4 passes flip `-`, `n/a` or `none`; item 2 passes undeclared sweep ids and `n/a` locations |

## Sources & frontier

- Census start: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa` → exit 0, with five
  pre-existing W04 warnings (`.ufo/waves/round-81/census-start.txt`).
- Census end: exit 0, warnings unchanged (`census-end.txt`).
- Registry rows: 202 → 208.
  - Counting command: `grep -cE '^\| S[0-9]{3,} \|' corpus/SOURCES.md`.
  - Added by tier: A +6 (S203–S207 mined; S208 rejected, unreachable).
  - Rows touched old→new: none outside the six new rows. Each new row is logged `— → value` in the lesson `## Gate`.
- Frontier advanced:
  - Citation searching and correction/retraction status were held only as a citation inside S120's capture. They now
    sit in two knowledge entries plus a README coverage section.
  - S028 (Crossmark) is still undispositioned.
- Sourced claim: C1 rests on S203–S207, all opened this round.
- Mined mistake (`corpus/lessons/round-81.md` `## Mistakes`): the r80 draw-label vs receipt-name mismatch, with a
  checker shown to fail on the bad labels. Three L1 mistakes for round 81 follow it: the missing cheapest-content
  control, the under-tested Run lines, and the egress ordering.
- Assimilation: none. In the `merge/chousa` package, 111 of 114 staged ids still collide (round 78).
- considerthese: `2026-11-05.md` and `2026-11-06.md` were read. The "one open Gate-record S-id per daily review"
  proposal was not implemented (reason in the lesson).

## Trend verdicts

- **expansion: improved.** Knowledge went from 92 to 94 entries on ground that previously existed only as a citation
  inside S120's capture. Six registry rows were added, and no sibling holds either topic. The claim is not admitted,
  but the ground moved.
- **quality: unchanged.** The new entries were reviewed and repaired, the r80 defects were closed, and the G02
  regression was caught and fixed. Both instruments, however, proved insufficient.
- **discernment: improved.** Both claims are reported as honest stops on the wave's own findings. The L1 did not argue
  the K3 letter. QUALITY 161–162 name the missed controls.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: the checklist now has
  6/6 Run lines, with pass-through limits stated (`SKILL.md:72,76,78`).
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: the trial record
  `.ufo/waves/round-81/w1/R81ExecTrial/`, LOG Round 81.
- [~] Instructions executable by an agent without oral context. Evidence: the `checklist-run.py` receipts; K2 forms are
  documented.
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: `R81SentinelScope.md` §2 and
  `R81ConnectorSiblings.md`.

## Extras

- **Round shape:** one v1 wave of 12 seats (band 8–16), no residual call; round total 12.
  - Roles: executor ×3, reviewer ×2, scribe ×2, critic, mutation-tester, scout, connector and sentinel ×1 each.
  - Attack share is 4/12 (33%); there is 1 connector seat.
  - Dead seats: 0.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no untracked fleet-root file from
  this round. The `/tmp/r81c2_*` files belong to kengaku (2026-11-04) and were left untouched. Scratch
  `/fast/scratch/hyaku/chousa-r81` was removed.
- **Open L0:** none new. The general fetch-scope question `8d77e6c1` is still open; this round routed around it via the
  egress table.
