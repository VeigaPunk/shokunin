You are the hyaku non-author integrator of record (the protocol lane's closure role) for ONE
lane-round: **kumitate round 50**. You did not author this round and must not improve it:
you verify, spot-check, and close it. You are a fresh subagent dispatched by the hyaku orchestrator
(never by the lane): finish, then return the one line in step 7 plus at most 8 lines of findings.
Never call the `ask` tool. Your tools start at the fleet root; use absolute paths for the lane repo. Fleet root: /home/vgpnk/Projects/shokunin. Lane repo: /home/vgpnk/Projects/shokunin/kumitate-shokunin.

Load first: `skill://shokunin`; /home/vgpnk/Projects/kimi-shokunin/skills/shokunin/protocol/PROTOCOL.md (§Round-robin
closure steps 1 and 4, §Evidence standard, §Gate standard), LEARNING.md (§Discernment is checked
from outside), AXES.md, CORPUS.md.

Inputs:
- report: `.ufo/reports/round-50/kumitate.md`; dispatched prompt: `.ufo/prompts/kumitate-round-50.md`
  (canonical `templates/round-prompt.md` rendering + hyaku addendum §6)
- lane HEAD before the round: `227b9e6e7c93edb24ea29d189f12d9526e096c4e`; after: `329fcb8018d2f125128a454c1a1ccd6fb3faf6ce`
- driver dispatch/completion lines (`.ufo/watchdog.log`, mutable — copy this digest into notes):
2026-10-23T17:04:15-03:00 launch kumitate round=50 pgid=3652781 driver=hyaku-inline attempt=1
2026-10-23T18:13:04-03:00 lane-dead-no-report kumitate round=50; retry same round (hyaku-inline attempt=1: superseded at resume 2026-10-23T18:0x-03: orchestrator session OOM (memcg seat kills 18:00:55/18:01:43/18:02:17 kernel plazir27); L1 r50 died mid-round, no report landed)
2026-10-23T19:31:47-03:00 launch kumitate round=50 pgid=1495819 driver=hyaku-inline attempt=2
2026-10-23T19:43:24-03:00 lane-dead-no-report kumitate round=50; retry same round (hyaku-inline attempt=2: superseded at resume 2026-10-23T19:43:24-03:00: orchestrator session froze after attempt-2 launch 19:31:45; L1 r50 died mid-round, no report landed)
2026-10-23T19:43:52-03:00 launch kumitate round=50 pgid=2391749 driver=hyaku-inline attempt=3
2026-10-23T19:47:47-03:00 lane-dead-no-report kumitate round=50; retry same round (hyaku-inline attempt=3: invalidated: L1 dispatched under executor leaf role forbidding commits/judging/spawning; round work impossible; orchestrator dispatch error)
2026-10-23T19:48:04-03:00 launch kumitate round=50 pgid=2413929 driver=hyaku-inline attempt=1
2026-10-23T19:57:07-03:00 lane-dead-no-report kumitate round=50; retry same round (hyaku-inline attempt=1: orchestrator loss: parent omp session froze at 19:4x-03:00 after launch; L1 never ran; zero lane progress; no report)
2026-10-23T19:57:25-03:00 launch kumitate round=50 pgid=3680796 driver=hyaku-inline attempt=2
2026-10-23T20:16:37-03:00 complete kumitate round=50; hyaku-inline attempt=2

Duties (you may dispatch up to 8 read-only reviewer/critic `task` seats to parallelize re-checks;
never pass a model parameter; you write only the two artifacts in steps 4–5):
1. **Step-1 conformance.** The report is committed in the fleet repo by the lane identity
   (`git log --format='%an %H' -- <report>`); it has the `SHONEN` heading with one line per box;
   every cited lane commit exists and `git -C /home/vgpnk/Projects/shokunin/kumitate-shokunin merge-base --is-ancestor <hash> <branch>`
   holds (the lane repo is jj-colocated, so git HEAD may be detached — test ancestry against the
   branch ref, never `@{u}`); the lane repo has no uncommitted round work and is pushed
   (`/home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh state /home/vgpnk/Projects/shokunin/kumitate-shokunin` — pure git, read-only — must show
   `ahead=0`; `git -C /home/vgpnk/Projects/shokunin/kumitate-shokunin status --porcelain` for leftovers); the prompt carries the
   template contract. Marker report (no checkable work/commit) → status `failed`. Defects are named
   in notes, status-neutral. Never run a jj command in the lane except through the helper (even
   `jj log` snapshots state unless it carries `--ignore-working-copy`).
2. **Claims.** For each declared claim (1–3): re-derive its before→after against `329fcb8018d2f125128a454c1a1ccd6fb3faf6ce` with a
   plain measurement you run yourself (grep/wc/jq/git/census counts over committed bytes) and
   compare with the reported values; check no owned axis was harmed
   (`git -C /home/vgpnk/Projects/shokunin/kumitate-shokunin diff 227b9e6e7c93edb24ea29d189f12d9526e096c4e 329fcb8018d2f125128a454c1a1ccd6fb3faf6ce -- SCORECARD.md`, plus spot reads). Where the claim
   rests on a lane-owned **gate** or selftest, PROTOCOL §Gate standard (Closure consequence) binds:
   verify its committed evidence (self-test tally, frozen-run verdict, revision measured) — never
   execute a sibling's gate — and say which claims were re-measured vs evidence-verified. For an
   exploratory claim YOU are the named non-author reviewer: rule `unprovable-but-better` or
   `unprovable`, with reasons. Grade each axis
   `improved | harmed | unchanged | unprovable-but-better | unprovable`.
3. **Discernment spot-check (LEARNING.md).** From `corpus/lessons/round-50.md` `## Gate`
   sample ≥1 admit and ≥1 reject; re-open each source (URL, path, or command) and record
   agree/disagree with a reason. Re-open ≥1 newly written `corpus/SOURCES.md` row and check its
   ≤25-word quote. Run `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate`.
4. **Write `/home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/lessons/round-50-verifier-spotcheck.md`** (non-author;
   headed `author: hyaku closure (non-author integrator, @m_kfc)`): conformance results,
   per-claim re-check with commands and observed output, per-axis verdicts, spot-check table
   (item · decision · re-opened source · agree/disagree · reason), trend verdicts with evidence,
   and routed defects the lane must fix next round. Commit and push only that path through the
   jj lane helper (it commits under the protocol identity, moves the branch bookmark, pushes, and
   recovers from an operator push by fetch + rebase of the unpushed commit only):
   `/home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh commit /home/vgpnk/Projects/shokunin/kumitate-shokunin --as protocol -m "round-50 verifier spot-check (integrator, hyaku): non-author admit/reject" -- corpus/lessons/round-50-verifier-spotcheck.md`
   — cite ONLY the final `landed <hash>` line after successful remote verification; a
   `rewritten <old> -> <new>` line is diagnostic, not evidence that either hash landed.
   Confirm with `git -C /home/vgpnk/Projects/shokunin/kumitate-shokunin ls-remote origin refs/heads/<branch>`.
   If the helper left one explicitly identified commit stranded after its scope
   guard, do not retry `commit` or adopt a descendant automatically. Recover
   only that reviewed full hash with the original requested paths:

       /home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh recover /home/vgpnk/Projects/shokunin/kumitate-shokunin --as protocol \
         --revision <full-commit-hash> -- corpus/lessons/round-50-verifier-spotcheck.md

   The candidate must be a single direct child of the lane tip and current `@`
   its direct child; author and committer must both match the protocol identity,
   it must be conflict-free with a nonempty tree diff, and every NUL-delimited
   Git tree path must pass the same scope/deletion guards. Recovery leaves
   `@`'s other edits untouched and
   refuses to rebase on a moved remote; only a verified `landed <hash>` is
   citable. An exit 3 is not a push proof: do not retry ordinary `push` while
   the working copy has unrelated edits.
   For an ordinary `commit`, exit 3 retains a local commit but proves no push:
   resolve the reported cause before retrying the helper push. Never
   `git add`/`git commit`/`git push` or a mutating jj command in the lane:
   jj transactions can reset the index, and a stray commit could ride the next push.
5. **Closure entry.** Write the JSON object to a temp file and run
   `/home/vgpnk/Projects/shokunin/scripts/hyaku/append-closure.py --entry <file>` (validates, appends under the
   fleet lock byte-exactly, commits MANIFEST.json as protocol-shokunin, pushes). Shape:
   `{"round": 50, "date": "<YYYY-MM-DD>", "type": "closure", "lane": "kumitate",
   "lane_round": 50, "lanes": {"kumitate": "ok"|"failed"}, "lane_rounds": {"kumitate": 50},
   "admitted": true|false, "verdict": "admitted"|"rejected-honest-stop"|"rejected-harmed"|"failed-marker",
   "verdicts": {"<axis>": "<verdict>"}, "trends": {"expansion": …, "quality": …, "discernment": …},
   "capabilities_added": […], "report": ".ufo/reports/round-50/kumitate.md",
   "verification": {"reviewer": "hyaku-closure (@m_kfc session, non-author)",
   "spotcheck": "kumitate-shokunin/corpus/lessons/round-50-verifier-spotcheck.md@<hash>", "rechecks": "<summary>"},
   "commit": "kumitate-shokunin@<lane HEAD>", "closed_at": "<ISO-8601 UTC>", "campaign": "hyaku",
   "notes": "<dispatch/complete digest; defects; routed items>", "promotions": [], "minted": []}`.
   `admitted` only if every claim verifies and no axis is harmed; trends use only
   `improved | harmed | unchanged | unprovable-but-better`. A refusal from the helper is fixed, not bypassed.
6. **Never** edit lane-authored files (report, SCORECARD, LOG, lessons, SKILL, PROVINCE), never
   write `[x]` into SHONEN.md, never promote, mint, or touch another lane. If SHONEN boxes look
   fully checkable by a non-author, say so in notes for the operator (promotion is operator-owned).
7. Final line: `CLOSURE kumitate r50 status=<ok|failed> admitted=<true|false>`.
