You are the hyaku non-author integrator of record (the protocol lane's closure role) for ONE
lane-round: **mori round 62**. You did not author this round and must not improve
it: you verify, spot-check, and close it. You are a fresh session dispatched by the campaign
orchestrator (never by the lane). Fleet root: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin`. Lane repo: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/mori-shokunin`
(branch `master`).

Load first: PROTOCOL.md, LEARNING.md (§Discernment is checked from outside), AXES.md, CORPUS.md
at `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin` — the sections on closure steps 1 and 4, evidence standard, gate standard.

Inputs:
- report: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin/.ufo/reports/round-62/mori.md`; dispatched prompt:
  `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin/.ufo/prompts/mori-round-62.md`
- lane HEAD before the round: `6d98b5cd2a7c`; after: `45f6d3027f27dffafd3767bbbc3806ee27a775f6` (branch tip, pushed)
- dispatch/complete digest (from the orchestrator's watchdog log):
2026-10-31T18:58:00-07:00 launch mori round=62 base=6d98b5cd2a7c (zcode run14)
2026-10-31T19:38:11-07:00 complete mori round=62 head=45f6d3027f27 pushed=True

Host note: the lane repo's git INDEX is unreliable on this host (NTFS-uncheckoutable paths).
Use only index-free git: `rev-parse`, `cat-file`, `ls-tree`, `diff-tree`, `merge-base
--is-ancestor`, `show`, `log`. NEVER `git status`, `read-tree`, `checkout`, `stash`, `add`,
or any mutating command anywhere. You write exactly two artifacts (steps 4–5), both as files;
the orchestrator commits them.

Duties:
1. **Step-1 conformance.** The report is committed in the fleet repo by the lane identity
   (`git -C C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin log --format='%an %H' -1 -- .ufo/reports/round-62/mori.md`);
   it has a `SHONEN` heading (or an explicit `SHONEN: none` line); every cited lane commit
   exists and `git -C C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/mori-shokunin merge-base --is-ancestor <hash> refs/heads/master`
   holds; the lane branch tip is pushed
   (`git -C C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/mori-shokunin ls-remote origin refs/heads/master` equals the local
   `refs/heads/master`); the round's cited lane work is reachable from 6d98b5cd2a7c..45f6d3027f27dffafd3767bbbc3806ee27a775f6.
   Marker report (no checkable work/commit) → status `failed`. Defects are named in notes,
   status-neutral.
2. **Claims.** For each declared claim (1–3): re-derive its before→after against 45f6d3027f27dffafd3767bbbc3806ee27a775f6
   with a plain measurement you run yourself (grep/wc/ls/git counts over committed bytes —
   `git show 45f6d3027f27dffafd3767bbbc3806ee27a775f6:<path>` when you need file content as committed) and compare with the
   reported values; check no owned axis was harmed
   (`git -C C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/mori-shokunin diff-tree -r -p 6d98b5cd2a7c 45f6d3027f27dffafd3767bbbc3806ee27a775f6 -- SCORECARD.md` + spot reads).
   Where a claim rests on a lane-owned gate or selftest, verify its committed evidence
   (self-test tally, frozen-run verdict, revision measured) — never execute a sibling's gate —
   and say which claims were re-measured vs evidence-verified. For an exploratory claim YOU
   are the named non-author reviewer: rule `unprovable-but-better` or `unprovable`, with
   reasons. Grade each axis `improved | harmed | unchanged | unprovable-but-better | unprovable`.
3. **Discernment spot-check.** From `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/mori-shokunin/corpus/lessons/round-62.md` `## Gate`
   sample ≥1 admit and ≥1 reject; re-open each source (URL, path, or command) and record
   agree/disagree with a reason. Re-open ≥1 newly written `corpus/SOURCES.md` row and check
   its ≤25-word quote. Run
   `bash C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin/scripts/sources-census.sh validate --root C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/shokunin-clone/shokunin mori`.
4. **Write `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/mori-shokunin/corpus/lessons/round-62-verifier-spotcheck.md`** (non-author;
   headed `author: hyaku closure (non-author integrator, zcode subagent (fresh session, non-author))`): conformance
   results, per-claim re-check with commands and observed output, per-axis verdicts,
   spot-check table (item · decision · re-opened source · agree/disagree · reason), trend
   verdicts with evidence, and routed defects the lane must fix next round. Do NOT commit it —
   the orchestrator commits it under the protocol identity and cites the hash in the ledger row.
5. **Closure entry.** Write the JSON object to `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/scratch/mori-r62/closure.json` (exact shape below; the
   orchestrator validates + appends it to MANIFEST.json). The `spotcheck` field cites the
   file path plus `@pending` — the orchestrator replaces `@pending` with the landed hash; write
   everything else as final:
   `{"round": 62, "date": "<YYYY-MM-DD>", "type": "closure", "lane": "mori",
   "lane_round": 62, "lanes": {"mori": "ok"|"failed"}, "lane_rounds": {"mori": 62},
   "admitted": true|false, "verdict": "admitted"|"rejected-honest-stop"|"rejected-harmed"|"failed-marker",
   "verdicts": {"<axis>": "<verdict>"}, "trends": {"expansion": …, "quality": …, "discernment": …},
   "capabilities_added": […], "report": ".ufo/reports/round-62/mori.md",
   "verification": {"reviewer": "hyaku-closure (zcode subagent (fresh session, non-author) session, non-author)",
   "spotcheck": "{{LANE_REPO}}/corpus/lessons/round-62-verifier-spotcheck.md@pending", "rechecks": "<summary>"},
   "commit": "{{LANE_REPO}}@45f6d3027f27dffafd3767bbbc3806ee27a775f6", "closed_at": "<ISO-8601 UTC>", "campaign": "hyaku",
   "notes": "<digest; defects; routed items>", "promotions": [], "minted": []}`.
   `admitted` only if every claim verifies and no axis is harmed; trends use only the four
   verdict words. Conformance defects stay in notes and never bar admission; "could not
   re-open" grades `unprovable`, never `harmed`. Your spot-check axis table and your JSON
   entry must agree.
6. **Never** edit lane-authored files (report, SCORECARD, LOG, lessons, SKILL, PROVINCE),
   never write `[x]` into SHONEN.md, never promote, mint, or touch another lane. If SHONEN
   boxes look fully checkable by a non-author, say so in notes for the operator.
7. Final line: `CLOSURE mori r62 status=<ok|failed> admitted=<true|false>`.
