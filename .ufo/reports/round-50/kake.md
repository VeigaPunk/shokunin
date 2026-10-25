# Round 50 — kake

Lane: `kake-shokunin`. Round shape: one v1 wave of 36 seats. Lane tip at report
time: 1c7f0769a838852971426a672936413fa50ef84f. Measured commit: ff3f6ecff5caf579fdc76216aa9cb82fa146a30e. Base: `9619af67c52939daac502ca7a24c9d714f3f51db`.
Author: Kimi fresh L1 (this session), continuing the round after the first attempt died on a
provider-route failure; the dead attempt's uncommitted work was inspected, re-verified and
re-used, never re-declared from scratch.

## Work performed

Two claims were declared and frozen before any score, in `.ufo/waves/round-50/contract.json`,
with one-command counters that read committed bytes only and a do-nothing control at the base:

- **C1 — freshness (capability acquisition): the quote-class instrument.** Predicate
  `met: classed == 3 of 3 declared ids` over S273, S274 and S286. Counting command
  `python3 -B .ufo/waves/round-50/c50_quote_class.py --root . --revision <commit>`. Before:
  `classed 0/3 met=False`, exit 1 at the base. Target: a new instrument that derives, per id,
  whether a quoted span is a raw substring of the retained HTML (`raw-substring`) or survives only
  whitespace collapse (`collapsed-only`), pins both retained blobs by sha256, and never opens a
  worktree path.
- **C2 — operability: pre-append order and wave-grant durability.** Predicate
  `met: durable == 1 of 1`. Counting command
  `python3 -B .ufo/waves/round-50/c50_durable.py --root . --revision <commit>`. Before:
  `durable 0/1 met=False`, exit 1 at the base. Target: the mirror committed before the registry
  append, the census run on the mirror with `--file` only, the wave-slot grant stdout and the
  exact dispatch command committed at a strict ancestor, and the LOG entry citing the wave only
  after that ancestor exists.

Both owned axes sit on the legacy 10/10 line, so the lowest-axis obligation is met by
construction. The stagnation nudge would have waived it (round 49 entered no capability inside
N=1); C2 works the operability surface anyway because the routed repair is operability.

Work items:

- **Declared and froze the two claims.** `.ufo/waves/round-50/contract.json` (base
  `9619af67c52939daac502ca7a24c9d714f3f51db`, `declaredBeforeScoring: true`, author
  `Kimi fresh L1`), `.ufo/waves/round-50/c50_quote_class.py`, `.ufo/waves/round-50/c50_durable.py`.
  The counters read only `git show <revision>:<path>` and `git merge-base --is-ancestor`.
- **Verified the dead attempt's partial work instead of re-declaring it.** The inherited
  untracked `.ufo/waves/round-50/` held the two counters, the class ledger, the S286 retained
  source, the assimilation scratch and the draft lesson and entry. Independently re-derived the
  three quote classes from the committed blobs (both sha256 pins matched, derived class matched
  the recorded class for all three ids), re-ran the frozen census on the mirror (exit 0, no
  E03/E04), re-ran the do-nothing counters at the base (exit 1, 0/3 and 0/1), and re-opened the
  S286 source live myself (HTTP 200, 193275 bytes, the 15-word span a raw substring of the fresh
  body). The dead attempt's `collisions` file, the one-line guard proof and the quarantine slice
  were re-derived rather than trusted.
- **Pre-append mirror committed before any registry append.**
  `.ufo/waves/round-50/assimilation/pre-append/corpus/` is the lane's `corpus/` plus the S286
  row (143 rows against the live 142). The census was run on the mirror with `--file` only:
  argv, stdout and exit 0 are committed at
  `.ufo/waves/round-50/assimilation/pre-append/census-{argv,stdout,exit}.txt`. Lane commit
  `33eec7f2cecfdbb9c7a1f85c3d8efae8dacd7dd1`.
- **Assimilated one theme from the shokuknow package, read-only.** Theme: the crawl-error status
  layer. One entry, `corpus/knowledge/crawl-error-status-table.md`, grounded on S286 alone.
  Scratch collision check with the census parser's own 0-to-3-leading-space pattern: the staged
  ids overlapping the lane registry are S273 and S274 only, so the adopted id S286 is free; the
  guard was proven able to fail on an indented `S286` row
  (`.ufo/waves/round-50/assimilation/guard/guard-collisions` is non-empty while the
  column-zero-only fixture `guard-col0` is empty). Row normalization: recheck `180d`, the staged
  prose `curl ... | grep -c 'scale back its crawling'` stripped and recorded in the lesson's Gate
  block, no literal or escaped pipe in any cell, status `mined`, opened re-grounded to this
  round's access date 2026-10-24, `used-by` exactly the one admitted entry.
  Validate-before-append: the mirrored registry passed `sources-census.sh validate --file` with
  exit 0 and no E03/E04 before any live append.
- **Recorded reason+flip rejects.** `corpus/knowledge/jekyll-url-baseurl-options.md` (staged S259)
  refused: its URL is already mined as S080, so a second row would be a within-scope duplicate
  URL; flip: supersede S080 in place, no second row for that URL.
  `corpus/knowledge/ollama-openapi-contract.md` (staged S321) refused as out of province —
  local model-serving endpoints are kama's domain and kake's PROVINCE.md Adjacent says the same;
  flip: the operator amends kake's province, or kama releases the surface.
- **Did not adopt the 12 quarantine ids.** The slice was re-derived read-only from
  `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` with
  the prompt's own awk filter (12 rows: S142, S143, S148, S154, S156, S161, S178, S184, S193,
  S194, S195, S206; nine are `payload-absent` and three carry the register's
  "could not be fetched" class cell). None was hand-checked this round and none was appended, so
  the round-48 hand-check is not used as an adoption basis.
- **Mined one unimplemented considerthese proposal, without editing it.**
  `considerthese/2026-10-24.md`, second unimplemented proposal — watch unmerged operator-save and
  WIP branches by tree diff, not ancestry. The pointer was opened: `remotes/origin/wip/operator-save-20261023`
  is `e80f84ddb84f4120cf62128c32498edc30db38bc`, `git merge-base --is-ancestor` against `master`
  exits 1, and the tree diff against `master` is not empty (4 lines are in that commit and not in
  `master`). The branch is not merged and not deleted; it stays operator-owned. The reflection is a
  pointer, not evidence: the lane's own bar measured it.
- **Turned the routed defects into lesson-backed QUALITY criteria.** `corpus/QUALITY.md` §Round-50
  criteria: a wave citation carries its own grant; a quote's match class is derived from its own
  two blobs, never asserted; operator-owned and inherited artifacts are not swept to zero a count.
- **Fixed a dispatch defect before the wave launched.** The first launch of
  `.ufo/waves/round-50/dispatch_w1.sh` exited in 0.08 s with `KeyError: 'role'` and launched no
  seat: the validator's payload carries the taxonomy role under `agent`, not `role`. The fix is
  committed at `dfb4a3f9705f26d50c38695ad73a9c8461baf122`; the dispatch command line is unchanged.

## Landed changes

- Lane commit `33eec7f2cecfdbb9c7a1f85c3d8efae8dacd7dd1` — declares the two claims, freezes both
  counters, the class ledger, the S286 retained source, the class-swap control and the
  pre-append census mirror and its `--file` receipts. LOG entry: the round-50 block.
- Lane commit `89096c387622785af59312bd2ee3b169202f1d4e` — the wave-slot grant stdout
  (`.ufo/waves/round-50/wave-grant.txt`) and the exact dispatch command
  (`.ufo/waves/round-50/dispatch-command.txt`), plus the validated spec
  (`.ufo/waves/round-50/w50-spec.json`), the dispatch payload
  (`.ufo/waves/round-50/w50-taskcall.json`), the route map and its generator, and the dispatcher.
  The grant is durable before any later entry cites the wave. LOG entry: the wave-evidence block.
- Lane commit `dfb4a3f9705f26d50c38695ad73a9c8461baf122` — the dispatch role-key fix, committed
  before the wave launched. LOG entry: the dispatch-defect block.
- Lane commit ff3f6ecff5caf579fdc76216aa9cb82fa146a30e — appends the S286 row to `corpus/SOURCES.md` after the pre-append
  mirror, and lands `corpus/knowledge/crawl-error-status-table.md`,
  `corpus/lessons/round-50.md`, the Round-50 QUALITY criteria, the wave settlement and the two
  order/citation proofs, plus the wave seat reports. LOG entry: the wave-settlement block.
- Lane commit 1c7f0769a838852971426a672936413fa50ef84f — records the measured results in `SCORECARD.md` (measured table and the
  capabilities row for the quote-class instrument).
- Fleet commit — this report.

## Before → after measurements

- **C1 — freshness (capability):** `python3 -B .ufo/waves/round-50/c50_quote_class.py --root . --revision <commit>`
  - Before, base `9619af67c52939daac502ca7a24c9d714f3f51db`: `C1 classed 0/3 met=False`, exit 1
    (class ledger absent, lesson absent; S286 also "retained blob absent, no live registry row,
    entry absent"). The do-nothing control cannot reach the target.
  - Before, pre-append `33eec7f2cecfdbb9c7a1f85c3d8efae8dacd7dd1`: `C1 classed 0/3 met=False`,
    exit 1 (the lesson and the entry land with the append, and the live row is not yet there).
  - After, measured commit ff3f6ecff5caf579fdc76216aa9cb82fa146a30e: `C1 classed 3/3 met=True`, exit 0 — `C1 classed 3/3 met=True`, exit 0, all three ids `all rules hold`
  - After, lane tip 1c7f0769a838852971426a672936413fa50ef84f: `C1 classed 3/3 met=True`, exit 0, all three ids `all rules hold`
- **C2 — operability:** `python3 -B .ufo/waves/round-50/c50_durable.py --root . --revision <commit>`
  - Before, base `9619af67c52939daac502ca7a24c9d714f3f51db`: `C2 durable 0/1 met=False`, exit 1
    (order proof absent, wave-cite proof absent, settlement absent). The do-nothing control
    cannot reach the target.
  - After, measured commit ff3f6ecff5caf579fdc76216aa9cb82fa146a30e: `C2 durable 1/1 met=True`, exit 0
  - After, lane tip 1c7f0769a838852971426a672936413fa50ef84f: `C2 durable 1/1 met=True`, exit 0
- **Registry census:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin kake` — before this round, exit 0; after the append, exit 0
  (exit 0, the same twelve W04 cross-scope duplicate-URL warnings as before and `kake ok`, over 143 rows).
- **Pre-append mirror census:** `sources-census.sh validate --file
  /home/vgpnk/Projects/shokunin/kake-shokunin/.ufo/waves/round-50/assimilation/pre-append/corpus/SOURCES.md`
  — exit 0, warnings only, no E03 or E04; argv, stdout and exit are committed at
  `.ufo/waves/round-50/assimilation/pre-append/`.

## Sources & frontier

- Registry rows 142 → 143. The counting command is
  `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`; the census command is
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin kake` (exit 0 before and after, exit 0, the same twelve W04 cross-scope duplicate-URL warnings as before and `kake ok`, over 143 rows).
- Rows added by tier: one tier-A docs row, S286, mined, opened 2026-10-24, recheck `180d`,
  `used-by` exactly `corpus/knowledge/crawl-error-status-table.md`.
- Rows touched old→new: none. S286 is new; no existing row's cell changed. The staged row's
  `opened` `2026-10-23` became `2026-10-24` and its prose `recheck` became `180d` in the
  admitted row; the stripped prose is recorded in the lesson's Gate block. The staged S259 row
  and the staged Ollama entry keep their staged values because they were refused.
- Frontier rows advanced: one. The crawl-error status layer — what an error status does to
  crawling — enters the lane as held ground through
  `corpus/knowledge/crawl-error-status-table.md`, on coverage-map ground the lane did not hold
  (the lane held robots-directive semantics and crawl-budget consequences, never the error-status
  layer).
- Assimilation: one theme, one admitted entry, two refuses with reason and flip, a 12-row
  quarantine slice re-derived and left unadopted. The shokuknow tree was read only; no campaign
  tool was run there.
- `corpus/README.md` coverage map: the new entry is on ground the map did not hold, so no map row
  was rewritten.

## Trend verdicts

- **expansion: improved.** One knowledge entry on ground the lane did not hold
  (`corpus/knowledge/crawl-error-status-table.md`), grounded on one row opened this round, with
  the registry growing 142 → 143.
- **quality: improved.** Both do-nothing controls fail (C1 0/3 exit 1, C2 0/1 exit 1) and both
  predicates pass only after the claimed work landed. The class ledger pins both blobs by sha256
  and the derived class is computed from the blobs, so a swapped label fails; the swapped-label
  control is committed at `.ufo/waves/round-50/verification/blur-control.txt`. The order proof
  ties the append to a strict ancestor that carries the mirror and its `--file` census exit 0.
- **discernment: improved.** Two staged entries refused with a reason and a flip condition; the
  12 quarantine ids were re-derived and none was adopted without a fresh hand-check; the
  considerthese reflection was treated as a pointer and its target was measured instead of
  believed. No row was adopted on another round's hand-check.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — the
  lane's held ground is cited to `corpus/SOURCES.md` rows; the round's own entry is
  `corpus/knowledge/crawl-error-status-table.md` (S286). Author assessment; no non-author
  verifier is bound to this round.
- `[ ]` At least one end-to-end domain task executed and logged in LOG.md — not self-promoted
  this round. The round executed its frozen counters end to end, but the box stays `[ ]` because
  no non-author reviewer checked it and promotion is operator-owned.
- `[~]` Instructions executable by an agent without oral context — the wave context and every
  seat item name absolute paths and the frozen commands
  (`.ufo/waves/round-50/w50-spec.json`). Author assessment.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — the Ollama OpenAPI entry was refused
  as kama's province (`corpus/lessons/round-50.md` §Gate). Author assessment.

## Waves

Shape: one v1 wave of 36 seats under `scripts/hyaku/ufo-wave-policy.json` (band 32-64).
`ufo-swarm-wave.mjs plan` and `run` exited 0 (`spawn` 36, `resume` 0, waveMinLanes 32,
waveMaxLanes 64, hard ceiling 256). AgentSwarm is not bound on this L1 subagent, so the
validator's rendered `taskCall` was dispatched as one `kimi --prompt` batch, and the seats are
counted from the settlement receipt, not from the spec alone.

Grant: `granted lane=kake wave=r50-w1 seats=36 live=54 pending=0 cap=256`, committed at
`89096c387622785af59312bd2ee3b169202f1d4e` together with the exact dispatch command. The slot was
released only after settlement.

Role mix: scout 5, executor 6, scribe 4, reviewer 5, critic 5, mutation-tester 4, sentinel 3,
revenger 2, connector 1, simplifier 1. Strict attack roles (reviewer, critic, mutation-tester)
14 of 36 (38.9 percent). The L1 holds the canonical planner seat; `planner` is frozen topology and the
validator rejects it as a swarm role, so the planner binding rides the L1 and is recorded here.

Routing: each role's model was resolved by reading the operator's own route table
(`~/.omp/agent/config.yml`: `task.agentModelOverrides` and `modelRoles`) and projecting each
role's bucket onto the aliases this substrate's config exposes, then probing each with a
one-line prompt. `scout` and `critic` (@m_sol) ran on `devin/swe-2-max`; `reviewer`, `revenger`,
`simplifier` and `scribe` (@m_zfl) ran on `zai-coding-plan/glm-5.3-flash`; `connector`,
`executor`, `mutation-tester` and `sentinel` (@m_grok, @m_flash) fell back to `devin/swe-2-max`
because their own buckets were unreachable here (`xai-oauth/grok-4.7-fast` answered 403 out of
credits, `commandcode/deepseek/...` is not configured on this substrate). The map is committed at
`.ufo/waves/round-50/route-map.json` and the deviation is recorded rather than hidden.

Settlement: 24 processes exited 0; 12 were killed at 300s and were not replaced (`ScribeGateQuotes`, `ScribeRowShape`, `ScribeLessonShape`, `ScribeConsider`, `ReviewClassLedger`, `ReviewOrderProof`, `ReviewEntryCite`, `ReviewReportContract`, `ReviewShonen`, `RevengerR49`, `RevengerR48`, `SimplifierCounters`). All five critic seats and all four mutation-tester seats returned; the five reviewer seats, the four scribe seats, both revenger seats and the simplifier seat were the dead ones. Dead seats stayed dead and were not replaced; no wave was split and no
seat was re-dispatched. Report files: 25 at settlement, 26 present when this report was written (one seat's file landed after the settlement snapshot). The seat reports are committed under
`.ufo/waves/round-50/w1/`.

No second wave and no residual replacement call: the wave's own output did not yield 32 distinct
new attack items against the frozen claims, so the contract's residual path applies and the
falsification stayed inside the wave's own attack seats.

## Stale-lane

No other mission of this lane is open; this was the only dispatched round in the lane's current
cycle. The lane is not stale.

## Tool installs

None. No package was installed or upgraded this round, so no entry is owed under
`/home/vgpnk/.omp/agent/RULES.md`; the pacman guard was respected (no pacman transaction was
attempted).

## Mistakes

- **class:** wave citation without a durable grant. **evidence:**
  `corpus/lessons/round-49-verifier-spotcheck.md` routed defect 1 (the grant line and the
  `kimi --prompt` transport lived only in the report and the LOG; `live=39` was never
  re-derived). **captured-by:** none at round 49. **fix:** `c50_durable.py` requires
  `wave-grant.txt` and `dispatch-command.txt` at a strict ancestor and requires the LOG at that
  ancestor not to cite the wave. **shown able to fail:** the same counter at the base is durable
  0, exit 1.
- **class:** quote class blurred. **evidence:**
  `corpus/lessons/round-49-verifier-spotcheck.md` (S273 collapsed-only, S274 a raw substring).
  **captured-by:** none (the round-49 counter checked a substring of the collapsed blob only).
  **fix:** `c50_quote_class.py` derives the class from both blobs and fails a swapped label.
  **shown able to fail:** `.ufo/waves/round-50/verification/blur-control.txt` records the swapped
  S286 class `collapsed-only` against derived `raw-substring`, `swapped_equals_derived=False`.
- **class:** a dispatched wave with a broken dispatcher. **evidence:** the first launch of
  `.ufo/waves/round-50/dispatch_w1.sh` exited 0.08 s with `KeyError: 'role'` and launched no seat
  (the payload's role key is `agent`). **captured-by:** none. **fix:** the dispatcher reads either
  key, and the fix is committed before the wave launches
  (`dfb4a3f9705f26d50c38695ad73a9c8461baf122`). **shown able to fail:** the failure is the
  observed run.

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` was run before this report. No file
written by a round-50 seat landed at the fleet root, so there was nothing to copy, `cmp` and
delete. Five untracked files at the fleet root — `bm.json`, `live.html`, `live_s228.html`,
`nama.html` and `s395.txt` — are dated 2026-10-24 18:07, hours before this round's launch
(22:35), and their content names neither this lane nor this round; they are inherited from an
earlier lane's seats and were left untouched. `.omp/mcp.json` and the `.ufo/state/*` driver files
are operator-owned.

## Open L0 questions

None appended this round. No operator decision blocks the round; the quarantined rows, the
operator-owned branches and the uncommitted inherited artifacts were routed around, not asked
about.
