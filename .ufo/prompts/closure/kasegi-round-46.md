You are the hyaku non-author integrator of record (the protocol lane's closure role) for ONE
lane-round: **kasegi round 46**. You did not author this round and must not improve it:
you verify, spot-check, and close it. You are a fresh subagent dispatched by the hyaku orchestrator
(never by the lane): finish, then return the one line in step 7 plus at most 8 lines of findings.
Never call the `ask` tool. Your tools start at the fleet root; use absolute paths for the lane repo. Fleet root: /home/vgpnk/Projects/shokunin. Lane repo: /home/vgpnk/Projects/shokunin/kasegi-shokunin.

Load first: `skill://shokunin`; /home/vgpnk/Projects/kimi-shokunin/skills/shokunin/protocol/PROTOCOL.md (§Round-robin
closure steps 1 and 4, §Evidence standard, §Gate standard), LEARNING.md (§Discernment is checked
from outside), AXES.md, CORPUS.md.

Inputs:
- report: `.ufo/reports/round-46/kasegi.md`; dispatched prompt: `.ufo/prompts/kasegi-round-46.md`
  (canonical `templates/round-prompt.md` rendering + hyaku addendum §6)
- lane HEAD before the round: `7eb7786d771f4ae2622b0ebc2cb2c5aabe79e76b`; after: `4cdcf7bdea8bea06705de752a2796d4e3aab0242`
- driver dispatch/completion lines (`.ufo/watchdog.log`, mutable — copy this digest into notes):
2026-10-28T19:52:51-03:00 launch kasegi round=46 pgid=3684502 driver=hyaku-inline attempt=1
2026-10-28T23:40:19-03:00 complete kasegi round=46; hyaku-inline attempt=1
2026-10-29T17:09:58-03:00 launch kasegi round=46 pgid=3369392 driver=hyaku-inline attempt=1
2026-10-30T01:20:39-03:00 complete kasegi round=46; hyaku-inline attempt=1

Duties (you may dispatch up to 8 read-only reviewer/critic `task` seats to parallelize re-checks;
never pass a model parameter; you write only the two artifacts in steps 4–5):
1. **Step-1 conformance.** The report is committed in the fleet repo by the lane identity
   (`git log --format='%an %H' -- <report>`); it has the `SHONEN` heading with one line per box;
   every cited lane commit exists and `git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin merge-base --is-ancestor <hash> <branch>`
   holds (the lane repo is jj-colocated, so git HEAD may be detached — test ancestry against the
   branch ref, never `@{u}`); the lane repo has no uncommitted round work and is pushed
   (`/home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh state /home/vgpnk/Projects/shokunin/kasegi-shokunin` — pure git, read-only — must show
   `ahead=0`; `git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin status --porcelain` for leftovers); the prompt carries the
   template contract. Marker report (no checkable work/commit) → status `failed`. Defects are named
   in notes, status-neutral. Never run a jj command in the lane except through the helper (even
   `jj log` snapshots state unless it carries `--ignore-working-copy`).
2. **Claims.** For each declared claim (1–3): re-derive its before→after against `4cdcf7bdea8bea06705de752a2796d4e3aab0242` with a
   plain measurement you run yourself (grep/wc/jq/git/census counts over committed bytes) and
   compare with the reported values; check no owned axis was harmed
   (`git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin diff 7eb7786d771f4ae2622b0ebc2cb2c5aabe79e76b 4cdcf7bdea8bea06705de752a2796d4e3aab0242 -- SCORECARD.md`, plus spot reads). Where the claim
   rests on a lane-owned **gate** or selftest, PROTOCOL §Gate standard (Closure consequence) binds:
   verify its committed evidence (self-test tally, frozen-run verdict, revision measured) — never
   execute a sibling's gate — and say which claims were re-measured vs evidence-verified. For an
   exploratory claim YOU are the named non-author reviewer: rule `unprovable-but-better` or
   `unprovable`, with reasons. Grade each axis
   `improved | harmed | unchanged | unprovable-but-better | unprovable`.
3. **Discernment spot-check (LEARNING.md).** From `corpus/lessons/round-46.md` `## Gate`
   sample ≥1 admit and ≥1 reject; re-open each source (URL, path, or command) and record
   agree/disagree with a reason. Re-open ≥1 newly written `corpus/SOURCES.md` row and check its
   ≤25-word quote. Run `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`.
4. **Write `/home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/lessons/round-46-verifier-spotcheck.md`** (non-author;
   headed `author: hyaku closure (non-author integrator, @m_zfl)`): conformance results,
   per-claim re-check with commands and observed output, per-axis verdicts, spot-check table
   (item · decision · re-opened source · agree/disagree · reason), trend verdicts with evidence,
   and routed defects the lane must fix next round. Commit and push only that path through the
   jj lane helper (it commits under the protocol identity, moves the branch bookmark, pushes, and
   recovers from an operator push by fetch + rebase of the unpushed commit only):
   `/home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh commit /home/vgpnk/Projects/shokunin/kasegi-shokunin --as protocol -m "round-46 verifier spot-check (integrator, hyaku): non-author admit/reject" -- corpus/lessons/round-46-verifier-spotcheck.md`
   — cite ONLY the final `landed <hash>` line after successful remote verification; a
   `rewritten <old> -> <new>` line is diagnostic, not evidence that either hash landed.
   Confirm with `git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin ls-remote origin refs/heads/<branch>`.
   If the helper left one explicitly identified commit stranded after its scope
   guard, do not retry `commit` or adopt a descendant automatically. Recover
   only that reviewed full hash with the original requested paths:

       /home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh recover /home/vgpnk/Projects/shokunin/kasegi-shokunin --as protocol \
         --revision <full-commit-hash> -- corpus/lessons/round-46-verifier-spotcheck.md

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
   `{"round": 46, "date": "<YYYY-MM-DD>", "type": "closure", "lane": "kasegi",
   "lane_round": 46, "lanes": {"kasegi": "ok"|"failed"}, "lane_rounds": {"kasegi": 46},
   "admitted": true|false, "verdict": "admitted"|"rejected-honest-stop"|"rejected-harmed"|"failed-marker",
   "verdicts": {"<axis>": "<verdict>"}, "trends": {"expansion": …, "quality": …, "discernment": …},
   "capabilities_added": […], "report": ".ufo/reports/round-46/kasegi.md",
   "verification": {"reviewer": "hyaku-closure (@m_zfl session, non-author)",
   "spotcheck": "kasegi-shokunin/corpus/lessons/round-46-verifier-spotcheck.md@<hash>", "rechecks": "<summary>"},
   "commit": "kasegi-shokunin@<lane HEAD>", "closed_at": "<ISO-8601 UTC>", "campaign": "hyaku",
   "notes": "<dispatch/complete digest; defects; routed items>", "promotions": [], "minted": []}`.
   `admitted` only if every claim verifies and no axis is harmed; trends use only
   `improved | harmed | unchanged | unprovable-but-better`. A refusal from the helper is fixed, not bypassed.
   Conformance defects (wrong path, late filing, undispatched wave, attribution) stay in notes and
   never bar admission; "could not re-open" grades `unprovable`, never `harmed`. Gitiles endpoints
   (`…googlesource.com/…?format=TEXT`) return base64 — decode before ruling a quote absent (run 6:
   tabi r25 needed two closure-corrections after both mistakes). Your spot-check axis table and your
   MANIFEST entry must agree.
6. **Never** edit lane-authored files (report, SCORECARD, LOG, lessons, SKILL, PROVINCE), never
   write `[x]` into SHONEN.md, never promote, mint, or touch another lane. If SHONEN boxes look
   fully checkable by a non-author, say so in notes for the operator (promotion is operator-owned).
7. Final line: `CLOSURE kasegi r46 status=<ok|failed> admitted=<true|false>`.
