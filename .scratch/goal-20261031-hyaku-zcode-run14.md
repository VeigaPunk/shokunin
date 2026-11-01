# hyaku run 14 — 2026-10-31 (zcode host)

Operator directive (verbatim): "Ok i need you to read my shokunin repo, understand its raison
deitre, check my shokunin skill on my github; then, i want you to train the shokunins that
haven't gotten to 100 rounds of training, by doing 10 rounds in sequence, for each shokunin in
the roster until they all have 100 trained rounds. The goal is to get them there, to 100 rounds
of training. Use maximum concurrency posssible here in zcode, so we can train faster and more
broadly."

## Campaign shape

- **Target: every roster lane at ≥100 trained rounds.** 17 lanes below 100 at run start
  (pool.txt set); audio 101, game-dev-2d 105, game-dev-3d 108, lore 103 already clear;
  protocol/aggregator are fleet meta-lanes, out of scope. ~706 lane-rounds needed.
- **Blocks: 10 rounds in sequence per lane** (directive), repeated until the lane reaches 100.
  One round = dispatch → lane work (1–3 falsifiable claims) → non-author verify + closure →
  ledger advance. Non-author closure before the next dispatch (standing rule).
- **Concurrency: maximum on this host — all 17 lanes live simultaneously**, each lane's rounds
  sequential. The orchestrator (zcode main session) is the single fleet-repo writer; lane
  workers and closure judges are fresh subagent sessions.
- **Host: Windows zcode (win32, Git Bash).** No omp, no jj, no tmux, no /home/vgpnk. Lanes are
  GitHub clones under the session workspace; lane commits go through the index-free plumbing
  helper (`treecommit.py`) because 10 of 17 lane trees carry NTFS-uncheckoutable paths that
  poison full-tree git operations on Windows. MANIFEST writes via `append-closure-win.py`
  (faithful port: same validate, same canonical bytes, plain git replaces jj). Routing note:
  the run-13 role→model map is omp-specific and does not exist here; seats are fresh zcode
  subagent sessions (the operator's "maximum concurrency here in zcode" supersedes the
  16–32-seat wave band and the 2026-10-31 20-worker omp directive recorded earlier today —
  this campaign runs the same craft rules with zcode subagents as the substrate).

## Lane order (queue = lowest round first at run start)

| # | lane | start | start state |
|---|------|-------|-------------|
| 1 | kagi | r29 | HOLD LIFTED by this directive (operator, 2026-10-31): training resumes; the 2026-10-21 content-safety refusal itself is NEVER retried, rephrased or routed around; C1 fix only per the frozen round-28 recipe rules |
| 2 | tabi | r44 | FRESH-START (trailing 6 rejected closures) |
| 3 | souji | r46 | FRESH-START (3) |
| 4 | kasegi | r50 | clean (r49 admitted) |
| 5 | kaidoku | r53 | FRESH-START (3) |
| 6 | tsukuroi | r53 | FRESH-START (8) |
| 7 | kengaku | r56 | normal (2) |
| 8 | mado | r57 | r57 dispatch evidence exists from the other host (2026-10-30 16:04 −03) with zero landed work: treated as never-worked; r57 runs fresh here. SECURITY HOLD on the r56-era credential material stands: never print, copy, or surface it; operator-owned rotation is outside lane scope |
| 9 | tameshi | r60 | FRESH-START (3) |
| 10 | mori | r62 | FRESH-START (5) + standing rule: no copied settings-values, no session identifiers |
| 11 | kake | r65 | FRESH-START (4) |
| 12 | kama | r65 | FRESH-START (3) |
| 13 | chousa | r66 | normal (2) |
| 14 | kumitate | r70 | clean (r69 admitted) |
| 15 | revenger | r74 | FRESH-START (7) |
| 16 | kotodama | r79 | FRESH-START (3) |
| 17 | kotoba | r82 | FRESH-START (6) |

Fresh-start rule (runs 8–13, operator-sanctioned, carried): the lane's first campaign round
reads its last three rejected closures and spot-checks first, and declares only claims a
do-nothing control cannot reach (§9). `advance` re-blocks a lane on a fresh 3-rejection
streak; the operator directive "train them all to 100" lifts streak blocks at run start only.

## Standing rules (carried from runs 7–13, still binding)

10-round blocks; one steered round per dispatch; non-author closure before the next dispatch;
clean commits (lane workers commit only their own changed paths through the helper; the
orchestrator is the only fleet-repo writer); report lands after the work commits it cites;
§9 claim sizing (do-nothing control); §10 assimilation (`considerthese/` mined where present;
shokuknow unreachable on this host → `Assimilation: none — shokuknow unreachable` unless a
register mirror is provided); append-only history everywhere (`append-closure-win.py` is the
only MANIFEST writer); lane identities on lane commits, protocol identity on closure
artifacts; no secret values in any artifact; mori's settings/session redaction rule; mado's
credential-material rule; kagi's refusal boundary.
