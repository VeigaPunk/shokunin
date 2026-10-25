# tabi — round 23 report (hyaku run 6, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/tabi-shokunin`. Baseline
`a89f1935f523a64b00991d792fca6a8c0d321948`; production checkpoint
`03c1b4d9a9ea7719ff4a13a63989fa9be36229c3`; wave-2 correction commit
`7ac9fffa5303e27aac3e092eb1a4aad2802c24bd`; disposition commit
`dfae5cdb09ee3384c7f3edd4474d8a1ad22a6843`; post-report corrections
`add37e7671365c381ba8df139704633997152e3f`; final wave-2 reports
`af00b59a4728be30757b62b6222756d710a1261e`; late wave-2 fail-open closures
`2433ed25c44eabcdd24d1a5a10ab692668bb023e`; all 44 wave-2 reports
`e059a8f1878424261c6d1e3d025a9139cadfb143`; final predicate/test
`b905efb5abd148dc73c7dece477c834eeab9a26f`; post-landing LOG binding
`c90dffd3807a68de7ab9c6503273eeddbcd03e2b` (**lane tip, pushed, ahead=0**); round shape:
**two v1 waves, 44 + 44 = 88 seats**.

## Work performed

Round 23 declared **two claims**, frozen in `.ufo/waves/round-23/claims.json` before either
instrument existed, with six disclosed post-freeze revisions (no predicate, metric, target or
population changed):

- **C1 — operability (lowest non-retired tie at 8), capability acquisition.** A fail-closed
  round-evidence auditor deriving six defect classes from a round's committed bytes, each
  reproducing one defect the round-22 non-author spot-check routed. Target 0 → 6.
- **C2 — coverage.** One shokuknow staged entry (the CSRF defence-shape boundary, a named
  corpus-frontier item) admitted only after this lane re-opened every source itself, with the
  two rows it cites appended. Target 0 → 1.

Work items, each with its pointer:

- **`scripts/round-evidence-audit.mjs`** — six classes (`c1-refusal-arithmetic`,
  `c2-wave-caps`, `c3-gate-spotcheck`, `c4-stale-attempts`, `c5-registry-identities`,
  `c6-landed-log-binding`), revision-scoped reads (`rev-parse` + `cat-file -t blob` +
  `cat-file blob` with the object id re-verified), a scrubbed git environment, mandatory
  `--round-cap`, band read from the fleet policy with a tighten-only authority check, and
  refusals (exit 2) instead of guesses. `03c1b4d:scripts/round-evidence-audit.mjs`.
- **Two self-test arms.** `--selftest` → 12 cases, 6 red + 6 green with an inventory
  assertion (`.ufo/waves/round-23/w1/W2InMemory.md` found the inventory gap this closes);
  `--selftest --rev <rev>` → the evidence-keyed matrix: baseline 7 findings / 6 classes and
  **6/6 repairs**, each repair removing exactly its own class
  (`corpus/evidence/round-23/c1-measurements.json`).
- **Skip-work control** `.ufo/waves/round-23/fixtures/skipwork-control.mjs` — reaches 6 on
  round-22 evidence *and* 6 on a clean fixture; receipt `fixtures/skipwork-receipt.json`
  (`verdict: control-refused`).
- **Source re-opening (C2).** Draft §8.8.1 and OWASP sheet fetched 2026-10-25 with digests
  (`06223931…`, `6f32bfbf…`), spans located by line/heading; three staged citation defects
  corrected (errata E1–E3 in the entry).
- **Assimilation.** One entry adopted, three candidates refused with reasons
  (`.ufo/waves/round-23/w1/SrcRefusals.md`), collision guard proven on an indented fixture
  (`.ufo/waves/round-23/scratch/ExecCollisionGuard/`), row-normalization + scratch-mirror
  census before the append (`.ufo/waves/round-23/w1/ExecAppendNormalize.md`,
  `ExecMirrorCensus.md`).
- **Six routed round-22 defects closed by appended correction** —
  `corpus/lessons/round-23.md` §Corrections items 1–6, criteria 61–63 in
  `corpus/QUALITY.md:1160-1180`.
- **Wave evidence** — `w1-spec/w2-spec`, dispatch payloads, registries with `record`
  receipts (`w1-record.json`, `w2-record.json`; 88/88 agentIds, 0 nulls; routed defect 5
  closed for this round too), spawn receipts, 44 + 23 seat reports, scratch fixtures.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Auditor + fixtures + measurement receipt (`scripts/round-evidence-audit.mjs`, `.ufo/waves/round-23/fixtures/`, `.ufo/waves/round-23/measure.mjs`, `corpus/evidence/round-23/c1-measurements.json`) | `LOG.md` §Round23 | `03c1b4d9a9ea7719ff4a13a63989fa9be36229c3` |
| Entry `corpus/knowledge/csrf-defense-shape-boundary.md` + rows S102/S103 (`corpus/SOURCES.md` 101 → 103) | `LOG.md` §Round23 | `03c1b4d` (same commit; the entry and its `used-by` land together) |
| `corpus/README.md` coverage row + frontier restatement; `corpus/QUALITY.md` criteria 61–63; `corpus/lessons/round-23.md` | `LOG.md` §Round23 | `03c1b4d` |
| Wave evidence under `.ufo/waves/round-23/` (specs, dispatches, registries, records, spawn receipts, W1 reports, scratch) | `LOG.md` §Round23 | `03c1b4d` |
| Wave-2 corrections: c1 receipt shape, c2 spawn bound + unaccounted receipt, c4 attempt joining (top-level receipts only), c5 absent-registry + identity/cardinality arms, c2 wave specs restricted to the round directory's top level, the child environment switched from a denylist to an allowlist (a `GIT_CONFIG_COUNT`/`GIT_CONFIG_PARAMETERS` injection executed a command through `core.fsmonitor` — `.ufo/waves/round-23/w2/W2Secrets.md` §SEC-1), `--report` contained to the fleet reports tree; corrected lesson/entry/README text; W2 reports; W2 evidence | `LOG.md` §Round23 (entry lands in `03c1b4d`) | `7ac9fffa5303e27aac3e092eb1a4aad2802c24bd` |
| M4 control restatement, counting commands for the spot-check counts, self-audit receipt | `LOG.md` §Round23 (entry lands in `03c1b4d`) | `dfae5cdb09ee3384c7f3edd4474d8a1ad22a6843` |
| `measure.mjs` (the receipt generator) — carried by `7ac9fff`, not by the checkpoint | `LOG.md` §Round23 and §Round23 — post-landing corrections (entry lands in this commit) | `7ac9fffa5303e27aac3e092eb1a4aad2802c24bd` |
| Late fail-open closures (c6 unresolvable commit, c2 non-blob spec), SCORECARD corrections, last late reports | `LOG.md` §Round23 — post-landing corrections; LOG entry lands in `c90dffd` | `2433ed25c44eabcdd24d1a5a10ab692668bb023e` |
| c2 round-total red arm (13 selftest cases), c6 escape resolution, entry/claim wording | `LOG.md` §Round23 — post-landing corrections; LOG entry lands in `c90dffd` | `43e9bb575a015ac8753348f2a9ad920ed0757796` |
| All 44 wave-2 seat reports landed | `LOG.md` §Round23 — post-landing corrections; LOG entry lands in `c90dffd` | `e059a8f1878424261c6d1e3d025a9139cadfb143` |
| c1 markdown-emphasis citation, Gate self-audit command, corrected scratch count | `LOG.md` §Round23 — post-landing corrections (entry lands in `c90dffd`) | `b905efb5abd148dc73c7dece477c834eeab9a26f` |
| Disposition (SCORECARD round-23 executed block + capability row) and this report | `LOG.md` §Round23; LOG entry lands in `03c1b4d` | `dfae5cd` carries the disposition; this report lands after it on the fleet repo |

## Before → after measurements

| Claim | Counting command | Before | After | Measured against |
|---|---|---|---|---|
| C1 | `node scripts/round-evidence-audit.mjs --rev <REV> --round 22 --round-cap 128 --json` → distinct `findings[].class` | 0 (`git cat-file -e a89f1935:scripts/round-evidence-audit.mjs` → exit 128: no instrument) | **6** (exit 1; 7 findings; per-class 1/1/1/1/1/2) | `03c1b4d` |
| C2 | `git grep -lE '^source: S10[23] ' <REV> -- corpus/knowledge \| wc -l` | 0 | **1** (`corpus/knowledge/csrf-defense-shape-boundary.md`; `git diff --diff-filter=A` names that file only; rows 101 → 103) | `03c1b4d` |

Round-23 self-audit at the final tip: `node scripts/round-evidence-audit.mjs --rev 2433ed25c44eabcdd24d1a5a10ab692668bb023e --round 23 --round-cap 128 --json`
→ **exit 0, clean, 0 findings** (re-run clean at `2433ed2`, `43e9bb5` and `e059a8f`; the lesson's
`## Gate` now carries this command so the receipt is re-derivable from committed bytes) — the auditor run against this round's own committed bytes, with
this report present (at the production checkpoint it had found two real evidence gaps of this
round's own: the wave-2 registry and receipts were not yet committed, and a scratch fixture tree
was being read as a wave; both fixed before this landing).

Supporting arms re-run at the final tip `2433ed2`: `--rev 2433ed2 --round 22 --round-cap 128 --json`
→ 6 classes / exit 1; `--selftest --rev 2433ed2 --round 22 --round-cap 128` → baseline 7 findings,
6/6 repairs, exit 0; `--selftest` → 12/12 with the inventory assertion;
`--selftest --rev 03c1b4d --round 22 --round-cap 128` → 6/6 repairs, exit 0; round-21
evidence → exit 1 with `c3-gate-spotcheck` only (a true positive under the frozen predicate,
recorded as `revisions[2]`, not smoothed); round-23 self-audit → see *Trend verdicts*.

## Sources & frontier

`SOURCES: changed — rows 101 → 103 (A88/B4/C9 → A89/B5/C9; mined 73 → 75, queued 19,
rejected 9).` Census command
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`
→ round start exit **0** (101 rows, 16 `W04` duplicate-URL warnings), round end exit **0**
(103 rows, the same 16 warnings; no E-line). Rows added by tier: 1×A (S102), 1×B (S103).
Rows touched in place: none — two new rows; no status/recheck/used-by change to an existing
row, and no `supersedes` edge (neither document was registered before). Frontier rows
advanced: **the corpus frontier item "CSRF-checked submits untested by rule"** now reads
*documented taxonomy held; measured submit still untested* — and that restatement is narrowed
further after a wave-2 attack: one loopback fixture submit carrying a token-shaped pair was
already captured at round 8 (`corpus/evidence/w9-tabi-b91/runs/replay-consumed-post/rep1/facts.json`)
and had never been classified; no site's defence shape has been classified.

Assimilation (`corpus-expansion-1`, read-only): one entry adopted (`csrf-defense-boundary.md`
→ `corpus/knowledge/csrf-defense-shape-boundary.md`), three candidates refused with reasons
(`webmcp-429-counters-and-residency-friction-r26.md`, `agent-approval-handshake.md`,
`webbridge-daemon-handshake-amendment-r14.md` — `.ufo/waves/round-23/w1/SrcRefusals.md`), id
map by document (staged S145 → S102, S146 → S103; staged ids S102/S103 are other documents),
collision count 0 with the false-green proven on a fixture. The round-22 quarantine verdicts
(38 register rows: 37 refused for absent quotes, 1 unverifiable) stand; nothing further was
adopted from that register. `considerthese/`: this lane has no such directory, so no operator
proposal was mined.

## Trend verdicts

- **expansion — improved.** One admitted entry on ground the baseline sweep did not hold
  (`git grep -rniE 'synchroni[sz]er token|double-submit|custom request header' a89f1935 -- corpus SKILL.md`
  → exit 1, no hits), citing two rows first opened this round (S102, S103, both `mined`), with
  a coverage row and a frontier restatement in `corpus/README.md` (append-only: `git diff
  --numstat a89f1935 03c1b4d -- corpus/README.md` → 28/0).
- **quality — improved (bounded).** No admitted entry is left false or stale: the round-22
  entries were not found stale; the new entry was corrected twice inside the round (quote
  verbatim, closed enumeration opened, locator fixed) on wave-2 attack; six prior-round
  figures were corrected append-only; the auditor's six checks each carry a red and a green
  fixture and an evidence-keyed repair. Bound: no browser run, no real site, nothing measured;
  the auditor's c1 fires on whole-document citations, so a historical mention inside a round's
  own lesson would fire falsely (named, not fixed).
- **discernment — improved.** The round-22 outside spot-check routed six defects; all six
  became lessons (`corpus/lessons/round-23.md` §Mistakes) and three became grounded
  `QUALITY.md` criteria (61–63). Round 23's own gate agreement is **owed to closure**: every
  seat is this lane's, so no non-author judgment is asserted anywhere in this round.

## SHONEN

- `[~]` **Decision tables/checklists resolvable** — `SKILL.md` decision tables plus the
  round-23 errata; the auditor's six class predicates are written out in
  `.ufo/waves/round-23/claims.json` `revisions[5]`.
- `[~]` **An executed-and-logged task** — `LOG.md` §Round23, landed in two commits
  (`03c1b4d` + this one), each naming what it carries.
- `[~]` **Executable counters that run from committed bytes** —
  `node scripts/round-evidence-audit.mjs --rev <rev> --round 22 --round-cap 128 --json` and
  `git grep -lE '^source: S10[23] ' <rev> -- corpus/knowledge`; both re-run at `03c1b4d`
  (6 classes, 1 entry) and recorded in `corpus/evidence/round-23/c1-measurements.json`.
- `[~]` **Province/refusal routes named** — `PROVINCE.md:15-19` (refuse/report, never absorb);
  no `[x]` is claimed, since promotion is operator-owned and no non-author verifier exists for
  this round.

**Stale-lane:** not stale — **attempt 1 only** for round 23 (dispatch 2026-10-25T04:04:05-03,
this landing). One commit pair, no silent window, no second dispatch, so the per-attempt
grading the round-22 correction requires has one row and says so. (Round 22's own three
attempts are graded in `corpus/lessons/round-23.md` §Corrections item 4.)

## Round shape, seats, dead seats

- **W1 (build) 44 seats** — scout 10 · reviewer 10 · executor 8 · scribe 8 · critic 4 ·
  connector 2 · mutation-tester 1 · sentinel 1; **44/44 reports, 0 dead**; registry ids
  recorded (`w1-record.json`), 44/44 non-null.
- **W2 (falsify) 44 seats** — reviewer 28 · critic 6 · mutation-tester 3 · sentinel 2 ·
  revenger 2 · scout 2 · simplifier 1 (37/44 attack roles, 84%). **44/44 reports, 0 dead** by the final
  tip (34 reports existed when the correction commit landed; the remaining ten
  — `W2Determinism`, `W2SelfAudit`, `W2NoHarm`, `W2LandedCites`, `W2QuoteB`, `W2Mistakes`,
  `W2Simplifier`, `W2Log`, `W2Scorecard`, `W2Cheat` — landed in `e059a8f`, and every one of
  their findings is accounted for above or in the disclosed-defect list). Registry ids recorded
  (`w2-record.json`), 44/44 non-null.
- Round total **88 seats** (≤128). The canonical planner seat is held by the L1 (the validator
  rejects a `planner` seat); the bounded planning data-walk rode `ConnPlannerWalk`.
- Wave-2 harvest: 16 line-level defects accepted and fixed in `7ac9fff` / `dfae5cd` (c1 receipt shape,
  c2 spawn bound + unaccounted receipt, c4 attempt joining + top-level receipts, c5
  absent-registry + identity/cardinality arms, self-test inventory, lesson 85-hour window
  corrected to 30.7 h *and* 85.3 h distinguished, "9 wave files" → 7, the "23" mechanism
  identified as the W2 envelope file family, the already-captured token-shaped submit, entry
  locator/partition/label defects, PROVINCE pointer). 3 defects were already fixed by wave-1
  falsifiers before this commit (c3 widening reverted, `--root` removed, `--policy` contained).

## Defects this round leaves open (disclosed)

- **M5 — seat scratch over-committed.** The production checkpoint carries 868 files / 23.6 MB of
  seat scratch (1,034 scratch paths by the final tip) under `.ufo/waves/round-23/scratch/` (`git ls-tree -r <A> .ufo/waves/round-23/scratch | wc -l`
  → 868). `7ac9fff` and `dfae5cd` carry none; a follow-up cleanup commit removes the committed
  scratch (the helper is the only writer, so it is one commit). Recorded as M5 in
  `corpus/lessons/round-23.md`, with the check that would have caught it.
- **c4 grades presence, not truth.** The class requires per-attempt grades that join to
  committed attempt receipts; it cannot tell whether a grade is true
  (`.ufo/waves/round-23/w2/W2CorrAttempts.md` §F4).
- **c1 reads the round's lesson and report as whole documents**, so a historical "0 whole-payload
  refusals" sentence inside a round's own lesson would fire falsely
  (`.ufo/waves/round-23/w2/W2Cls1.md`).
- **c3 is word-presence only**: a wrong spot-check count inside a Gate clears it
  (`.ufo/waves/round-23/w2/W2CorrGate.md`).
- **The S102/S103 digests pin the fetched bytes**; the two tag-interleaved OWASP spans are
  matched on stripped text whose own digest is not recorded (`corpus/evidence/round-23/c2-measurements.json`).
- **Two read-path fail-opens closed at `2433ed2`, two left open.** Closed: a cited commit that
  does not resolve is now a c6 finding rather than a skip, and a directory named `*-spec.json` is
  now a c2 finding rather than an invisible wave. Open: `lessonSha256` hashes a re-encoded string
  rather than the blob's bytes, and a missing/unreadable object still reads as "absent at this
  revision" instead of refusing (`.ufo/waves/round-23/w2/W2Determinism.md` §F3/§F4).
- **The round cap is supplied, not verified** against any committed declaration
  (`W2Determinism` §F5): the auditor records the value it was given, so a caller could pass a
  looser cap. The claim's counter always passes 128.
- **c2 and c5 read only top-level `<stem>-spec.json` waves**, so nine of the twelve report-bearing
  rounds (whose specs sit at `w1/spec.json`) are outside their reach — a coverage limit of the
  instrument, named rather than hidden (`.ufo/waves/round-23/w2/W2Simplifier.md`).
- **c1 drops a citation line that contains a correction word** (e.g. "… were filed this round"),
  and c4 is vacuous for round 23 because this round committed no attempt receipts.
- **`SCORECARD.md`'s append-only wording was corrected in `2433ed2`:** five of the six mutable docs
  are byte-prefix extensions; `corpus/SOURCES.md` is a pure mid-file insertion (2 added, 0 removed).

## Honest bounds

Every seat here is this lane's, so all findings are author-side and no non-author agreement
exists for round 23. C1 is a capability over the lane's own evidence, not a fleet gate: it
reads the fleet round report and the fleet policy by path with their digests in every output,
writes nothing outside stdout/stderr, and refuses when an input is absent (its round-23
self-audit refused while this report did not exist). C2 is documented-upstream — no browser
ran, no site was touched, no submit was classified, and no axis scalar moved (depth 8,
coverage 9, operability 8, freshness 8, calibration 9, adjacency 8 — unchanged). Tooling:
nothing installed or upgraded this round (no pacman, uv, cargo or npm transaction; host pacman
transactions remain paused by the orchestrator ruling).
