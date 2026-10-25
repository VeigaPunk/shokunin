# Kaika README ownership probe — exact attribution

Read-only probe. No file was edited, restored, moved, or committed. Scope: original
`/home/vgpnk/Projects/shokunin/README.md`, WT `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/README.md`,
`history://KaikaAggregateR12`, root `.ufo/waves/kaika-aggregate`.

## Verdict

**Exact mutation attribution (not inference):** the entire root README dirty delta
(65 added / 44 removed) is produced by agent **KaikaAggregateR12**'s two successful
`edit` tool calls, both issued with a *basename-only* patch header `[README.md#…]`.
The tool resolved them against the session cwd `/home/vgpnk/Projects/shokunin`
(the original fleet-root checkout), **not** the assigned worktree. The third call
in the sequence errored without writing. Nothing else touched the root README.

| # | toolCallId | started (UTC) | patch header | outcome | wrote to |
|---|---|---|---|---|---|
| 1 | `call_403cfb02…b6868788` | 2026-10-19T23:44:47.019Z | `[README.md#A810]` | ok | `/home/vgpnk/Projects/shokunin/README.md` |
| 2 | `call_9e245c9b…9871508191` | 23:45:28.660Z | `[README.md#FE5A]` | **error, no write** (anchor mismatch) | — |
| 3 | `call_1c162293…aba1ef9c8191` | 23:45:38.163Z | `[README.md#FE5A]` (retry) | ok | `/home/vgpnk/Projects/shokunin/README.md` |

Rendered-history lines 132 and 171 map to call 1 and the call-2/3 pair respectively.
The owned WT README was never edited by this agent (see identity checks below).

## Evidence chain (each item independently re-checkable)

1. **Session cwd.** `KaikaAggregateR12` session record (jsonl, first line):
   `id 01a15687-27cb-749b-abb8-dc6a08a12265`, `cwd /home/vgpnk/Projects/shokunin`,
   `parentSession …/2026-10-19T20-36-43-523Z_01a155e1-….jsonl`.
   Jsonl path: `/home/vgpnk/.omp/agent/sessions/-Projects-shokunin/2026-10-19T20-36-43-523Z_01a155e1-7d83-74e9-8383-9ee7c15d7c99/KaikaAggregateR12.jsonl`
   (5.1 MB, child of Main's session file of the same base name).
2. **Tool path-resolution mechanism, disclosed by the tool itself in the same
   session.** Every `dispatch.md` edit used the relative path
   `.ufo/waves/kaika-aggregate/dispatch.md`; each result carried the warning:
   *"Path \".ufo/waves/kaika-aggregate/dispatch.md\" does not exist; matched its
   filename and snapshot tag #… to /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/.ufo/waves/kaika-aggregate/dispatch.md
   (read earlier this session)."* → relative paths are tried against the cwd first;
   filename+tag fallback applies **only when the cwd path is absent**. For `README.md`
   the cwd path exists (`/home/vgpnk/Projects/shokunin/README.md`), so no fallback
   fired and no warning was emitted; the edit landed on the root file.
3. **Timestamps (sub-millisecond).** root README `mtime=ctime=2026-10-19 20:45:38.163695312 -0300`
   = `23:45:38.163695312Z`, i.e. exactly call 3's start instant. WT README
   `mtime=ctime=20:36:47.205230509 -0300` = worktree materialization time, unchanged
   since (the agent's first read of that file followed at 23:37:55Z); it is not any
   edit time.
4. **Distinct file identity.** root README `inode=11381365`, WT README `inode=42829853`,
   both `links=1` (no hardlink); sizes 8554 vs 6407 B; md5 `01b90164…` vs `6b15b3cb…`.
5. **Byte-exact content reconstruction.** Base = WT README = root `HEAD:README.md`
   (all md5 `6b15b3cb6e834c04fe6b6e581663933a`, 6407 B — root HEAD `10405f43…` and WT
   HEAD `ee8ba85…` share identical README bytes). Applying exactly the 9 ops of call 1
   and then the 3 ops of call 3 to that base reproduces the current root README
   **line-for-line (147 lines, comparison `state2 == root` → True)**; unified diff of
   base→root = **65 added / 44 removed**, matching the parent's observation exactly.
   Corollary: call 2 wrote nothing, and **no other change of any kind exists in the
   root README** — the pre-edit root file was at HEAD (the patches' removed lines match
   HEAD text verbatim in every op region, and no residual difference remains).
6. **Scoped git status.** root: ` M README.md` only (paths README.md and
   `.ufo/waves/kaika-aggregate`). WT: `?? .ufo/waves/kaika-aggregate/` only; WT README
   clean. Root campaign `.ufo` paths (`round-12`, `reports/round-12`, `kaika`,
   `kaika-w1/w2j/w3`, `reports/AGGREGATE.md`) are clean.

**Residual gap (only one, minor):** the `edit` results for calls 1 and 3 echo the
*relative* header (`[README.md#A810]` / `[README.md#9AE6]`) and do not print an
absolute resolved path; the tool logs a resolved path only when it emits the fallback
warning. Resolution to the root file is therefore established by items 2–5
(mechanism + mtime + inode + byte-exact reproduction) rather than by a literal
"resolved path" field. No other session/agent is implicated: the root README mtime is
the edit instant and the content is exactly the two patches.

## Patch inventory (for reconstruction; full text in the jsonl above)

Call 1 (`[README.md#A810]`, ops against pre-edit numbering, applied simultaneously):
`PUT 12.=15` (7 lines), `PUT >33` (10 lines), `PUT 69.=72` (5), `PUT 75.=77` (3),
`PUT 81.=84` (4), `PUT 88.=91` (6), `PUT 93.=110` (18, roster table),
`PUT 112.=114` (4), `PUT 119.=125` (10). Call 3 (`[README.md#FE5A]`, ops against the
post-call-1 content): `PUT 12.=18` (7 lines, reworded intro), `PUT >36` (blank line),
`PUT 100.=100` (`## Roster` → `## Roster records and existing repository links`).

## Root vs WT delta (the misplaced deliverable)

Base→root diff = the round-12 README update: fleet-root authority paragraph,
SOURCES-registry / census-CLI / frontier-mistake-non-author paragraph, corpus listing
(`SOURCES.md` row), "Corrections are append-only" wording, round/sibling-mint wording,
`## Roster records and existing repository links` heading, `Manifest status` column
with 13 rostered rows + mori/chousa/kotodama labeled "repository link only — not in
MANIFEST", 13-vs-21 inventory note, rewritten Files section, and removal of the
hardcoded "79 rounds" claim. Full diff reproducible via
`git -C /home/vgpnk/Projects/shokunin diff -- README.md`; saved copy at
`/home/vgpnk/.omp/agent/sessions/-Projects-shokunin/2026-10-19T20-36-43-523Z_01a155e1-7d83-74e9-8383-9ee7c15d7c99/14409.bash-original.log`
(10,486 B).

**Divergence the parent must not carry over blindly:** the misplaced draft's authority
sentence says *"Fleet-root copies govern this repository; an upstream or vendored
mirror is reference-only"* — the opposite of the chosen authority (kimi-shokunin
canonical at `e737d2ea97f6b0198503e077676c3f2ea07974a9`; fleet root = vendored
deployment; local metadata cannot override canonical rules). The agent itself recorded
this divergence and withheld the correction in the WT dispatch notes at
00:17:21Z and 00:22:57Z. So the root README content is a **draft needing the authority
fix**, not final deliverable text. Also note the same draft was superseded in intent
by the later `#FE5A` refinement, which is included in the 65/44.

## Root `.ufo/waves/kaika-aggregate`

Does **not** exist: `ls -d /home/vgpnk/Projects/shokunin/.ufo/waves/kaika-aggregate`
→ "No such file or directory"; root `.ufo/waves/` contains `kaika`, `kaika-w1`,
`kaika-w2j`, `kaika-w3` (campaign files PLAN.md, steer.md, JJ-ADOPTION.md,
tooling-global.md, …) and no `dispatch.md`/`seats/` copies. No root-side duplicates or
mismatches of the WT files; nothing to reconcile. WT dir (untracked, expected):
35 files — `dispatch.md`, `r12-gate-checkpoint.md`, `sources-census-checkpoint.md`,
and `seats/` with 32 seat notes (21 lane audits + connector, critic, index-usability,
own-history-mistakes, planner, registry-readme-truth, schema-provenance,
source-adversarial, source-count-reconciliation, source-curation, source-freshness).

## Must preserve (do not touch)

1. Root README worktree bytes (`01b90164f06a6d5a35d50cf71faa5b17`, 8554 B) — the only
   copy of the draft; recoverable also from the two patch texts in the jsonl.
2. WT `.ufo/waves/kaika-aggregate/` untracked evidence (35 files) — the agent's L2
   corpus; not committed on `kaika/aggregate` (WT log head still `ee8ba85`).
3. WT README (pristine base `6b15b3cb…`) until the corrected wording is written by
   its owner; do not "sync" it from the root copy without fixing the authority
   sentence.
4. Root `.ufo/waves/kaika*` campaign artifacts and the unrelated `README.md`-external
   root state (out of scope here; left untouched).

## Minimal non-destructive recovery plan (parent-owned; not executed)

1. **Capture** the root README worktree content (bytes or diff) as the draft artifact —
   required before any restore.
2. **Transfer** into the WT: write `README.md` at the **absolute** path
   `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/README.md`
   using the captured draft as base, with the authority sentence corrected to
   kimi-shokunin-canonical / fleet-vendored (`e737d2e`). Because root HEAD README ==
   WT base byte-for-byte, this is a plain content write — no 3-way merge needed.
3. **Restore** the original checkout only after step 2 is durable:
   `git -C /home/vgpnk/Projects/shokunin checkout -- README.md` (uncommitted, so no
   history is lost); verify `git -C /home/vgpnk/Projects/shokunin status --porcelain -- README.md`
   is empty afterwards.
4. **Re-verify**: WT `git status --porcelain` shows ` M README.md` plus the untracked
   wave dir; WT README diff equals the corrected intended update.
5. **Prevent recurrence**: require absolute WT paths for every edit/write from this
   agent (parent already instructed; the agent acknowledged at 00:16:59Z and used
   absolute/`cwd-relative-to-WT` paths for all later dispatch edits).

## Confidence

High. Content attribution is byte-exact (reconstruction == worktree, 65/44 diffstat
match); file identity (inode/mtime/ctime) and the tool's own path-resolution warning
independently corroborate the mechanism. The only non-logged detail is an explicit
resolved-path string for the two README edits (item 2–5 chain stands in for it).
