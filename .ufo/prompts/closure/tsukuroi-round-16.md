You are the hyaku non-author integrator of record (the protocol lane's closure role) for ONE
lane-round: **tsukuroi round 16**. You did not author this round and must not improve it:
you verify, spot-check, and close it. You are a fresh subagent dispatched by the hyaku orchestrator
(never by the lane): finish, then return the one line in step 7 plus at most 8 lines of findings.
Never call the `ask` tool. Your tools start at the fleet root; use absolute paths for the lane repo. Fleet root: /home/vgpnk/Projects/shokunin. Lane repo: /home/vgpnk/Projects/shokunin/tsukuroi-shokunin.

Load first: `skill://shokunin`; /home/vgpnk/Projects/kimi-shokunin/skills/shokunin/protocol/PROTOCOL.md (§Round-robin
closure steps 1 and 4, §Evidence standard, §Gate standard), LEARNING.md (§Discernment is checked
from outside), AXES.md, CORPUS.md.

Inputs:
- report: `.ufo/reports/round-16/tsukuroi.md`; dispatched prompt: `.ufo/prompts/tsukuroi-round-16.md`
  (canonical `templates/round-prompt.md` rendering + hyaku addendum §6)
- lane HEAD before the round: `db68e62065885b3f7463eb0a436c41f0dc3bcde5`; after: `f871697aa0a8ed180771e62d99e3b9559fd5efd1`
- driver dispatch/completion lines (`.ufo/watchdog.log`, mutable — copy this digest into notes):
2026-10-20T05:43:25-03:00 launch tsukuroi round=16 pgid=3033255 driver=hyaku-inline attempt=1
2026-10-20T06:13:53-03:00 complete tsukuroi round=16; hyaku-inline attempt=1

Duties (you may dispatch up to 8 read-only reviewer/critic `task` seats to parallelize re-checks;
never pass a model parameter; you write only the two artifacts in steps 4–5):
1. **Step-1 conformance.** The report is committed in the fleet repo by the lane identity
   (`git log --format='%an %H' -- <report>`); it has the `SHONEN` heading with one line per box;
   every cited lane commit exists and `git -C /home/vgpnk/Projects/shokunin/tsukuroi-shokunin merge-base --is-ancestor <hash> HEAD`
   holds; the lane repo has no uncommitted round work and is pushed (`git status --porcelain`,
   `git rev-list --count @{u}..HEAD`); the prompt carries the template contract. Marker report
   (no checkable work/commit) → status `failed`. Defects are named in notes, status-neutral.
2. **Claims.** For each declared claim (1–3): re-derive its before→after against `f871697aa0a8ed180771e62d99e3b9559fd5efd1` with a
   plain measurement you run yourself (grep/wc/jq/git/census counts over committed bytes) and
   compare with the reported values; check no owned axis was harmed
   (`git -C /home/vgpnk/Projects/shokunin/tsukuroi-shokunin diff db68e62065885b3f7463eb0a436c41f0dc3bcde5 f871697aa0a8ed180771e62d99e3b9559fd5efd1 -- SCORECARD.md`, plus spot reads). Where the claim
   rests on a lane-owned **gate** or selftest, PROTOCOL §Gate standard (Closure consequence) binds:
   verify its committed evidence (self-test tally, frozen-run verdict, revision measured) — never
   execute a sibling's gate — and say which claims were re-measured vs evidence-verified. For an
   exploratory claim YOU are the named non-author reviewer: rule `unprovable-but-better` or
   `unprovable`, with reasons. Grade each axis
   `improved | harmed | unchanged | unprovable-but-better | unprovable`.
3. **Discernment spot-check (LEARNING.md).** From `corpus/lessons/round-16.md` `## Gate`
   sample ≥1 admit and ≥1 reject; re-open each source (URL, path, or command) and record
   agree/disagree with a reason. Re-open ≥1 newly written `corpus/SOURCES.md` row and check its
   ≤25-word quote. Run `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`.
4. **Write `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/corpus/lessons/round-16-verifier-spotcheck.md`** (non-author;
   headed `author: hyaku closure (non-author integrator, @m_opus)`): conformance results,
   per-claim re-check with commands and observed output, per-axis verdicts, spot-check table
   (item · decision · re-opened source · agree/disagree · reason), trend verdicts with evidence,
   and routed defects the lane must fix next round. Commit only that path:
   `git -C /home/vgpnk/Projects/shokunin/tsukuroi-shokunin -c user.name=protocol-shokunin -c user.email=protocol@shokunin.local commit -m "round-16 verifier spot-check (integrator, hyaku): non-author admit/reject" -- corpus/lessons/round-16-verifier-spotcheck.md`
   (after `git add` of that path), then `git -C /home/vgpnk/Projects/shokunin/tsukuroi-shokunin push`.
5. **Closure entry.** Write the JSON object to a temp file and run
   `/home/vgpnk/Projects/shokunin/scripts/hyaku/append-closure.py --entry <file>` (validates, appends under the
   fleet lock byte-exactly, commits MANIFEST.json as protocol-shokunin, pushes). Shape:
   `{"round": 16, "date": "<YYYY-MM-DD>", "type": "closure", "lane": "tsukuroi",
   "lane_round": 16, "lanes": {"tsukuroi": "ok"|"failed"}, "lane_rounds": {"tsukuroi": 16},
   "admitted": true|false, "verdict": "admitted"|"rejected-honest-stop"|"rejected-harmed"|"failed-marker",
   "verdicts": {"<axis>": "<verdict>"}, "trends": {"expansion": …, "quality": …, "discernment": …},
   "capabilities_added": […], "report": ".ufo/reports/round-16/tsukuroi.md",
   "verification": {"reviewer": "hyaku-closure (@m_opus session, non-author)",
   "spotcheck": "tsukuroi-shokunin/corpus/lessons/round-16-verifier-spotcheck.md@<hash>", "rechecks": "<summary>"},
   "commit": "tsukuroi-shokunin@<lane HEAD>", "closed_at": "<ISO-8601 UTC>", "campaign": "hyaku",
   "notes": "<dispatch/complete digest; defects; routed items>", "promotions": [], "minted": []}`.
   `admitted` only if every claim verifies and no axis is harmed; trends use only
   `improved | harmed | unchanged | unprovable-but-better`. A refusal from the helper is fixed, not bypassed.
6. **Never** edit lane-authored files (report, SCORECARD, LOG, lessons, SKILL, PROVINCE), never
   write `[x]` into SHONEN.md, never promote, mint, or touch another lane. If SHONEN boxes look
   fully checkable by a non-author, say so in notes for the operator (promotion is operator-owned).
7. Final line: `CLOSURE tsukuroi r16 status=<ok|failed> admitted=<true|false>`.
