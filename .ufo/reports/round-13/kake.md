# kake — round 13 report (freshness axis-move)

**Verdict:** freshness re-verification round; score **stays 8** — the
r13 plan's own trigger (probe-latest >6h stale at open) never
materialized (snapshot was 3.9h fresh, 18:51:26Z vintage), and the
round's critic falsification found no defensible move trigger in any
branch. What landed instead: every standing freshness claim re-verified
against live state at 22:47–22:50Z, 4 stale citations fixed, 2 new
drift-detection rules landed, 1 imprecise claim rescoped, and the
missing round-12 commits repaired in both repos.

## Axis state (SCORECARD.md)

- operability 10 (unchanged; free-read surface saturated — see Retired note).
- freshness 8 (unchanged, evidence refreshed): pattern HELD — today's 3
  timer sweeps (history `at` 06:00:46.703Z, 12:00:53.973Z, 18:01:09.822Z —
  r14 erratum: this report first wrote 06:00:36Z, which is the journal
  `Starting` line, not the history row) + the off-cadence
  manual re-probe (18:51:26Z, r3 vintage, **not** the timer) all carry
  the identical 12-ok/5-violated/1-error set; an independent 18-curl
  live replication at 22:50Z reproduced it with **0 verdict diffs**.

## Findings (all read-only; L2 evidence in /tmp/kake-r13/)

1. **charter-ghp pin-lag persists over a deploy-CURRENT live page.**
   The `2026-09-26` pin has failed in every full-universe row since the
   09-27T06:22Z ENTER, but the live page is no longer stale: the human
   pushed 5 commits directly to `origin/main` of the charter repo
   18:32:06–20:43:21Z (`b74190e` bake → `d69dd22` og/twitter/hreflang →
   `0c767c2` window sync → `b9db4b1` CORRECTION → `a8f1e2b` fixup) and
   Pages served each within ~30s — live sha `0decd827…` ==
   `raw.githubusercontent.com/…/a8f1e2b` (53,353B). r12's "churn paused"
   is rescoped: the scribe automation's push leg is still failing
   (ledger beats `pushed:false`), but the repo keeps moving by hand.
   PQ-12 remains a one-line operator edit (`fleet.config.json:256`);
   the local clone lags origin by 5 (`61d0ce6`) — `git pull --ff-only`
   first for any charter work.
2. **`observed:"absent"` semantics (draft error caught by critic,
   withdrawn before landing):** the marker check is an exact-literal
   `includes()` (`src/probe.mjs:55`) — "absent" means the *pin* wasn't
   found, never that the beat line vanished. Live carried
   `2026-09-28 scribe beat (` on every measured byte-shape while pinned
   to `2026-09-26`. Rule landed in SKILL.md.
3. **at-vs-mtime freshness rule (new, from r13 forensics):**
   `probe-latest.json` freshness must be read from the `at` field —
   after the r11 clobber + manual restore, mtime 21:31:45Z vs `at`
   18:51:26Z diverge 2h40m; birth-time = the clobber instant; sha proved
   the restored file IS the r11 backup (`8c5bb8ca…b6591e`). Also: no
   verb can append history without rewriting latest — the single writer
   is `saveProbe` (`src/fleet.mjs:39-52`), so the 21:31Z `total:1` row
   and the restored latest are two halves of the same r11 event.
4. **PQ-5 unchanged-pending:** live slot still serves the
   byte-identical 13,409B 404 sentinel (sha `93ddca9a…` == 09-26
   journals); zero fires fleet-wide since 09-26T15:34Z; `kimi-map`
   content is 09-26-vintage (CDP :9222 down — `publishedUrl:null` is
   NOT same-day evidence). Still the shortest path to a green row:
   Publish card `efc1830` + set slug `charter-ufo-fsd`.
5. **PQ-2 unchanged:** mirror serves 19/93 canonical locs, 74 missing
   by live-GET (75 by f3d2ecd accounting — 5 of the additions
   pre-serve), 0 per-URL transitions, root byte-frozen 74,641B (max
   embedded date 08-21). Decomposition: `/speedrun/`+`/burnerchrome/`
   404s are the kimi dir-index pitfall (`index.html` twins serve 200);
   `/iqrunway/` is dead on BOTH surfaces (0 sitemap locs, absent from
   source). Advance gated on the 20 unpushed ds4cc commits (live
   canonical sitemap still 404).
6. **Automation layer unchanged:** probe timer healthy (3 sweeps
   today, next 00:00:59Z); keeper timer still never fired (disabled +
   inactive, 26 boots, zero journal); L0 kake round-12 question
   (keeper/lucario) still **unanswered**. Detector upheld: 6 events /
   0 phantom on 77 rows (the +1 spot row is suppressed by the universe
   rule; naive diffing would fabricate 6 phantom EXITs).
7. **Reviewer citation sweep: 60 citations, 0 broken, 4 stale — all
   fixed:** PQ-3 "behind 2" → behind 5; PQ-6 `kimi-surface-ops.md:189`
   → `:175`; PQ-5 "zip 1 day stale" → 2 days; ops-automation header
   "76 rows" → 77.

## Protocol repair (this round's git actions)

Round-12's commits were missing in BOTH repos (kake head was round-11,
main head round-6; kasegi independently reported the same gap).
Repaired before the r13 commit: `a642f93` (kake round-12) and
`9af7245` (main round-12 report), then round-13 commits on top. Zero
webzites-state writes this round (sentinel 33-file sha guard; the
fleet.config.json pin line + mtime re-checked unchanged).

## L2 manifest (10 probes, one batch; roles routed per mission map)

scout (sweep table + live replication) · executor×4 (charter flip
decomposition, PQ-5, PQ-2, PQ-5 follow-up) · labrat (timers + L0) ·
revenger (history writer forensics + detector) · critic (3 claims
falsified — 1 withdrawn, 2 wording-fixed) · reviewer (60-citation
sweep) · connector (sibling overlap: only kagi's CDP-lease doc cite =
collaboration; kasegi's registry contest is with kumitate) · sentinel
(mutation guard baseline). Artifacts: `/tmp/kake-r13/`.

## Next (r14 plan, in SCORECARD.md)

Verify the 00:00:59Z sweep (pattern + charter-ghp pin FAIL persists
unless the operator lands the PQ-12 one-liner → first EXIT since
09-27T06:22Z); re-check PQ-5 (operator may Publish `efc1830`) and the
charter human-push series; L0 answers → operator-gated execution
support.
