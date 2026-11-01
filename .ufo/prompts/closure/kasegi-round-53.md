You are the hyaku non-author integrator of record (the protocol lane's closure role) for ONE
lane-round: **kasegi round 53**. You did not author this round and must not improve
it: you verify, spot-check, and close it. You are a fresh session dispatched by the campaign
orchestrator (never by the lane). Fleet root: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin`. Lane repo: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/kasegi-shokunin`
(branch `master`).

Load first: PROTOCOL.md, LEARNING.md (§Discernment is checked from outside), AXES.md, CORPUS.md
at `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin` — the sections on closure steps 1 and 4, evidence standard, gate standard.

Inputs:
- report: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin/.ufo/reports/round-53/kasegi.md`; dispatched prompt:
  `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin/.ufo/prompts/kasegi-round-53.md`
- lane HEAD before the round: `e276dbf6255e`; after: `743084a827d08078e7fb638cee686809f23eefb7` (branch tip, pushed)
- dispatch/complete digest (from the orchestrator's watchdog log):
2026-10-31T22:47:04-07:00 launch kasegi round=53 base=e276dbf6255e (zcode run14)
2026-11-01T00:13:16-07:00 complete kasegi round=53 head=743084a827d0 pushed=True

Host note: the lane repo's git INDEX is unreliable on this host (NTFS-uncheckoutable paths).
Use only index-free git: `rev-parse`, `cat-file`, `ls-tree`, `diff-tree`, `merge-base
--is-ancestor`, `show`, `log`. NEVER `git status`, `read-tree`, `checkout`, `stash`, `add`,
or any mutating command anywhere. You write exactly two artifacts (steps 4–5), both as files;
the orchestrator commits them.

Duties:
1. **Step-1 conformance.** The report is committed in the fleet repo by the lane identity
   (`git -C C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin log --format='%an %H' -1 -- .ufo/reports/round-53/kasegi.md`);
   it has a `SHONEN` heading (or an explicit `SHONEN: none` line); every cited lane commit
   exists and `git -C C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/kasegi-shokunin merge-base --is-ancestor <hash> refs/heads/master`
   holds; the lane branch tip is pushed
   (`git -C C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/kasegi-shokunin ls-remote origin refs/heads/master` equals the local
   `refs/heads/master`); the round's cited lane work is reachable from e276dbf6255e..743084a827d08078e7fb638cee686809f23eefb7.
   Marker report (no checkable work/commit) → status `failed`. Defects are named in notes,
   status-neutral.
2. **Claims.** For each declared claim (1–3): re-derive its before→after against 743084a827d08078e7fb638cee686809f23eefb7
   with a plain measurement you run yourself (grep/wc/ls/git counts over committed bytes —
   `git show 743084a827d08078e7fb638cee686809f23eefb7:<path>` when you need file content as committed) and compare with the
   reported values; check no owned axis was harmed
   (`git -C C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/kasegi-shokunin diff-tree -r -p e276dbf6255e 743084a827d08078e7fb638cee686809f23eefb7 -- SCORECARD.md` + spot reads).
   Where a claim rests on a lane-owned gate or selftest, verify its committed evidence
   (self-test tally, frozen-run verdict, revision measured) — never execute a sibling's gate —
   and say which claims were re-measured vs evidence-verified. For an exploratory claim YOU
   are the named non-author reviewer: rule `unprovable-but-better` or `unprovable`, with
   reasons. Grade each axis `improved | harmed | unchanged | unprovable-but-better | unprovable`.
3. **Discernment spot-check.** From `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/kasegi-shokunin/corpus/lessons/round-53.md` `## Gate`
   sample ≥1 admit and ≥1 reject; re-open each source (URL, path, or command) and record
   agree/disagree with a reason. Re-open ≥1 newly written `corpus/SOURCES.md` row and check
   its ≤25-word quote. Run
   `bash C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin/scripts/sources-census.sh validate --root C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin kasegi`.
4. **Write `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/kasegi-shokunin/corpus/lessons/round-53-verifier-spotcheck.md`** (non-author;
   headed `author: hyaku closure (non-author integrator, zcode subagent (fresh session, non-author))`): conformance
   results, per-claim re-check with commands and observed output, per-axis verdicts,
   spot-check table (item · decision · re-opened source · agree/disagree · reason), trend
   verdicts with evidence, and routed defects the lane must fix next round. Do NOT commit it —
   the orchestrator commits it under the protocol identity and cites the hash in the ledger row.
5. **Closure entry.** Write the JSON object to `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/scratch/kasegi-r53/closure.json` (exact shape below; the
   orchestrator validates + appends it to MANIFEST.json). The `spotcheck` field cites the
   file path plus `@pending` — the orchestrator replaces `@pending` with the landed hash; write
   everything else as final:
   `{"round": 53, "date": "<YYYY-MM-DD>", "type": "closure", "lane": "kasegi",
   "lane_round": 53, "lanes": {"kasegi": "ok"|"failed"}, "lane_rounds": {"kasegi": 53},
   "admitted": true|false, "verdict": "admitted"|"rejected-honest-stop"|"rejected-harmed"|"failed-marker",
   "verdicts": {"<axis>": "<verdict>"}, "trends": {"expansion": …, "quality": …, "discernment": …},
   "capabilities_added": […], "report": ".ufo/reports/round-53/kasegi.md",
   "verification": {"reviewer": "hyaku-closure (zcode subagent (fresh session, non-author) session, non-author)",
   "spotcheck": "{{LANE_REPO}}/corpus/lessons/round-53-verifier-spotcheck.md@pending", "rechecks": "<summary>"},
   "commit": "{{LANE_REPO}}@743084a827d08078e7fb638cee686809f23eefb7", "closed_at": "<ISO-8601 UTC>", "campaign": "hyaku",
   "notes": "<digest; defects; routed items>", "promotions": [], "minted": []}`.
   `admitted` only if every claim verifies and no axis is harmed; trends use only the four
   verdict words. Conformance defects stay in notes and never bar admission; "could not
   re-open" grades `unprovable`, never `harmed`. Your spot-check axis table and your JSON
   entry must agree. Write real paths everywhere — never leave a `{{…}}` placeholder
   unexpanded in the JSON.
6. **Never** edit lane-authored files (report, SCORECARD, LOG, lessons, SKILL, PROVINCE),
   never write `[x]` into SHONEN.md, never promote, mint, or touch another lane. If SHONEN
   boxes look fully checkable by a non-author, say so in notes for the operator.
7. Final line: `CLOSURE kasegi r53 status=<ok|failed> admitted=<true|false>`.
