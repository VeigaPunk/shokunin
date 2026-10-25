You are the hyaku non-author integrator of record (the protocol lane's closure role) for ONE
lane-round: **tabi round 12**. You did not author this round and must not improve it:
you verify, spot-check, and close it. You are a fresh subagent dispatched by the hyaku orchestrator
(never by the lane): finish, then return the one line in step 7 plus at most 8 lines of findings.
Never call the `ask` tool. Your tools start at the fleet root; use absolute paths for the lane repo. Fleet root: /home/vgpnk/Projects/shokunin. Lane repo: /home/vgpnk/Projects/shokunin/tabi-shokunin.

Load first: `skill://shokunin`; /home/vgpnk/Projects/kimi-shokunin/skills/shokunin/protocol/PROTOCOL.md (§Round-robin
closure steps 1 and 4, §Evidence standard, §Gate standard), LEARNING.md (§Discernment is checked
from outside), AXES.md, CORPUS.md.

Inputs:
- report: `.ufo/reports/round-12/tabi.md`; dispatched prompt: `.ufo/prompts/tabi-round-12.md`
  (canonical `templates/round-prompt.md` rendering + hyaku addendum §6)
- lane HEAD before the round: `f032f2dccc8a99632eea52edafa8220284b5c919`; after: `37ffbef29486ec93e004a4d3e39fdfa78006024d`
- driver dispatch/completion lines (`.ufo/watchdog.log`, mutable — copy this digest into notes):
2026-10-20T01:00:45-03:00 launch tabi round=12 pgid=651903 driver=hyaku-inline attempt=1
2026-10-20T01:16:16-03:00 complete tabi round=12; hyaku-inline attempt=1

Duties (you may dispatch up to 8 read-only reviewer/critic `task` seats to parallelize re-checks;
never pass a model parameter; you write only the two artifacts in steps 4–5):
1. **Step-1 conformance.** The report is committed in the fleet repo by the lane identity
   (`git log --format='%an %H' -- <report>`); it has the `SHONEN` heading with one line per box;
   every cited lane commit exists and `git -C /home/vgpnk/Projects/shokunin/tabi-shokunin merge-base --is-ancestor <hash> HEAD`
   holds; the lane repo has no uncommitted round work and is pushed (`git status --porcelain`,
   `git rev-list --count @{u}..HEAD`); the prompt carries the template contract. Marker report
   (no checkable work/commit) → status `failed`. Defects are named in notes, status-neutral.
2. **Claims.** For each declared claim (1–3): re-run its counting command against `37ffbef29486ec93e004a4d3e39fdfa78006024d` and
   compare with the reported before→after; check no owned axis was harmed
   (`git -C /home/vgpnk/Projects/shokunin/tabi-shokunin diff f032f2dccc8a99632eea52edafa8220284b5c919 37ffbef29486ec93e004a4d3e39fdfa78006024d -- SCORECARD.md`, plus spot reads). A capability
   claim needs its demonstration to run now. For an exploratory claim YOU are the named non-author
   reviewer: rule `unprovable-but-better` or `unprovable`, with reasons. Grade each axis
   `improved | harmed | unchanged | unprovable-but-better | unprovable`.
3. **Discernment spot-check (LEARNING.md).** From `corpus/lessons/round-12.md` `## Gate`
   sample ≥1 admit and ≥1 reject; re-open each source (URL, path, or command) and record
   agree/disagree with a reason. Re-open ≥1 newly written `corpus/SOURCES.md` row and check its
   ≤25-word quote. Run `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`.
4. **Write `/home/vgpnk/Projects/shokunin/tabi-shokunin/corpus/lessons/round-12-verifier-spotcheck.md`** (non-author;
   headed `author: hyaku closure (non-author integrator, @m_strong)`): conformance results,
   per-claim re-check with commands and observed output, per-axis verdicts, spot-check table
   (item · decision · re-opened source · agree/disagree · reason), trend verdicts with evidence,
   and routed defects the lane must fix next round. Commit only that path:
   `git -C /home/vgpnk/Projects/shokunin/tabi-shokunin -c user.name=protocol-shokunin -c user.email=protocol@shokunin.local commit -m "round-12 verifier spot-check (integrator, hyaku): non-author admit/reject" -- corpus/lessons/round-12-verifier-spotcheck.md`
   (after `git add` of that path), then `git -C /home/vgpnk/Projects/shokunin/tabi-shokunin push`.
5. **Closure entry.** Write the JSON object to a temp file and run
   `/home/vgpnk/Projects/shokunin/scripts/hyaku/append-closure.py --entry <file>` (validates, appends under the
   fleet lock byte-exactly, commits MANIFEST.json as protocol-shokunin, pushes). Shape:
   `{"round": 12, "date": "<YYYY-MM-DD>", "type": "closure", "lane": "tabi",
   "lane_round": 12, "lanes": {"tabi": "ok"|"failed"}, "lane_rounds": {"tabi": 12},
   "admitted": true|false, "verdict": "admitted"|"rejected-honest-stop"|"rejected-harmed"|"failed-marker",
   "verdicts": {"<axis>": "<verdict>"}, "trends": {"expansion": …, "quality": …, "discernment": …},
   "capabilities_added": […], "report": ".ufo/reports/round-12/tabi.md",
   "verification": {"reviewer": "hyaku-closure (@m_strong session, non-author)",
   "spotcheck": "tabi-shokunin/corpus/lessons/round-12-verifier-spotcheck.md@<hash>", "rechecks": "<summary>"},
   "commit": "tabi-shokunin@<lane HEAD>", "closed_at": "<ISO-8601 UTC>", "campaign": "hyaku",
   "notes": "<dispatch/complete digest; defects; routed items>", "promotions": [], "minted": []}`.
   `admitted` only if every claim verifies and no axis is harmed; trends use only
   `improved | harmed | unchanged | unprovable-but-better`. A refusal from the helper is fixed, not bypassed.
6. **Never** edit lane-authored files (report, SCORECARD, LOG, lessons, SKILL, PROVINCE), never
   write `[x]` into SHONEN.md, never promote, mint, or touch another lane. If SHONEN boxes look
   fully checkable by a non-author, say so in notes for the operator (promotion is operator-owned).
7. Final line: `CLOSURE tabi r12 status=<ok|failed> admitted=<true|false>`.
