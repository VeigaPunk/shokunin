# kake — round 16 report (freshness axis-move: detection widened to all standing claims, and made reproducible)

**Verdict:** freshness **9 → 10** — critic-adjudicated (two independent
branches, both MOVE-ELIGIBLE; predicate recorded in `/tmp/kake-r16/critic.md`).
operability stays 10 (saturated; free-read audit retired at r12).

## Axis state (SCORECARD.md)

- freshness 9 → **10**: drift detection widened from *path citations only*
  (r10's retired "60/60", r15's 58-target sweep) to *every quantified standing
  claim*, with a committed read-only instrument that re-derives the pinned
  checks in one command and exit-codes the verdict.
- operability 10 (unchanged).

## The move, part 1 — instrument (the standing half)

`scripts/freshness-sweep.mjs` (read-only, node ≥18, zero deps, ~1,050 lines) +
`corpus/knowledge/freshness-pins.json` (48 pins) + runbook
`corpus/knowledge/freshness-sweep.md`.

| mode | exit | result at round close (02:4xZ) |
|---|---|---|
| bare | **1** | `§armed: plazir-live-source-gap` (the intended open drift, below); §paths 0 drift, §history MATCH |
| `--json` | 1 | one JSON object: sections, pins, reasons, `gateWarnings` |
| `--section=paths` | 0 | 62 targets · resolve 47 · declaredAbsent 9 (+3 indirect) · drift 0 · unresolved 6 (globs) · files 38 · `newMissing []` |
| `--offline` | 0 | armed = `skipped(offline)`, `complete=false` — never counted as a pass |
| `--selftest` | 0 | **9/9** (declaredAbsent exit-neutral; unannotated miss → 1; interior-tampered history → 1; malformed JSONL → 2; unknown flag/section → 64; write-API confinement) |
| `--section=bogus` | **64** | usage error on stderr |

Checks gated: §paths — every `~/…` citation resolves + frozen `pathsMissSet`
(a NEW miss is drift; a recovered path is informational) + `pathsFiles`;
§history — row floor 78, last-`at` ceiling 6h20m, fleet-shape **set**
equality, `probe-delta` exact event count + last-event pin + phantom max 0;
§armed — PQ-12 (5-state), PQ-5 (E1), PQ-2 gate, ds4cc sitemap, **PQ-14**.
`pins._unused` reports every pin the run did not evaluate, so a pin cannot
look armed while inert (critic finding, fixed in-round).

Write-free proof: `sha256sum ~/Projects/webzites/state/*` aggregate
`15a5c47f…4669cb2` identical at round open and after every instrument run;
sentinel 33/33 byte-identical.

## The move, part 2 — first complete claim sweep (the evidence)

160 quantified standing claims enumerated with one live recipe each
(`/tmp/kake-r16/scout-claims.md`, machine-readable `claims.tsv`,
`raw/claim-checks.md`): **117 HOLD / 15 STALE / 7 UNVERIFIABLE /
21 HISTORICAL-OK**. All 15 fixed or re-pinned this round:

| # | site | claim → live | class |
|---|---|---|---|
| S01–S03 | `ops-automation.md:4,22,29-31,112` | 77 rows→**78**; 66 full→**67**; 65 gaps→**66**; 20/65→**21/66** band; detector "on 77 rows"→78 | row-count literals (rot by design → now floors/dated) |
| S04–S05 | `probe-delta-alerting.md:40,102` | 76→**78** rows, 66→**67** full, 10→**11** spot; era families `{1:10→11, 18:7→8}` | counts + histogram |
| S06–S07 | `keeper-timer-inert.md:65`, `free-read-verbs.md:373` | `log=8d(round …)` on **19/21** (not 20 — `veigapunk-page` ends `log=8d(e2e fix)`; 20 only under the widened `log=8d(`) | miscount |
| S08 | `free-read-verbs.md:212-216` | bare `sync-check` sample `{ok:3, attention[6]}` → `{ok:4, attention[5]}`, 3+3 → 3 sentinel + **2** real drift | **verb-outcome literal (never swept before)** |
| S09 | `free-read-verbs.md:166-171` | fleet `reconcile`: 7 attention ids / "6 DIFF + 1 ERR" → **6** / 5 DIFF + 1 ERR (`plazir27runs-on` now in-sync) | **verb-outcome literal** |
| S10 | `publish-queue.md:30` (PQ-10) | `Nightcall` case-mismatch → body carries **both** cases (2/2); clause retired | marker-config claim |
| S11 | `publish-queue.md` ETag | sampler read `6ab49126-1365d`; **refuted** — L1 7/7 fetches give `6ab49127-1365d`; rule landed instead (ETag = edge-unstable, never a freeze metric) | identifier stability |
| S12 | `fire-journal-codes.md:55` | `recreate plazir15 ×2 fired` → **×3** (`fire:true` in c7/c4/c6) | **meter accounting** |
| S13 | `fire-journal-codes.md:7-13` | journal top-level key union over all 28 journals is exactly `site,mode,startedAt,steps[],fire[,error]` — `newVersion`/`preview`/`operatorNext`/`liveAfter` are NOT top-level | **structural claim, wrong when written** |
| S14–S15 | `SKILL.md:42,187` | `src/cli.mjs:1086`→**1087**; `:386`→**389** | code-line pins |
| — | `publish-queue.md` §r15 | "kake cites `bounties` 0 times" → **1** (that paragraph; pre-r15 `git grep` = 0) + line pin `:213`→`:214` | self-contradiction (reviewer-caught), also mirrored in the r15 SCORECARD plan text (corrected) |

Classes S08/S09 (verb outcomes), S13 (journal structure), S12 (fire count) and
S10 had **no detection method** in any earlier round — r11/r12 executed those
verbs once and pinned the exits, never re-swept the outcome literals.

## The move, part 3 — in-round domain drift caught (PQ-14)

`~/Projects/plazir-15-site` is **5 commits ahead of `origin/main`** (HEAD
`c814526`, remote `bd02d10`, all five dated 2026-09-26), so live serves the
pre-push tree:

| evidence | live | source | `origin/main` |
|---|---|---|---|
| `sitemap.xml` `<loc>` | **8** incl. `/tetris/` (1,293B, sha `3eb1722c…`) | **7** (`8e162356…`) | 8 |
| `snake/` `og:url` | 0 hits | 1 hit (`3059bf0`) | 0 |
| `speedrun/` canonical | self | `https://ds4cc.com/speedrun/` (`0de5eb9`) | self |

All 8 live locs are 200 → **stale-vs-source, not rot**; invisible to `probe`
and to `reconcile` (root `index.html` is not in the lag set → `in-sync`).
Falsifies `drift-detection.md`'s "plazir15-ghp tree byte-identical to live"
(corrected + §r16 proof block; r6's lesson had recorded "5 ahead / 5 diffs" but
the claim it contradicted was never updated). Ledgered as **PQ-14**
(`publish-queue.md`, gate = operator `git push`). r7's "103 locs" baseline is
now written as **103 live-side / 102 source-side — the delta IS the gate**
(`sitemap-orphan-audit.md`, `SKILL.md:194`, `corpus/README.md`). The instrument
now catches it mechanically: `PQ-14 … sitemap LIVE-SOURCE-GAP !! DRIFT`,
exit 1.

## Re-verification reads (all non-PERSIST branches evidence-excluded)

1. **PQ-12 → `PERSIST`** — pin `2026-09-26 scribe beat` (`fleet.config.json:256`,
   mtime unchanged 09-27T15:30:57Z) vs live `2026-09-29 scribe beat (`
   (200 / 53,386B / sha `fb365e38…` == r15 == remote+clone `9c28d29`).
   EDIT-LANDED (pin≠literal), CHURN-AGAIN (live date == 09-29, not newer),
   SILENT (fresh 200, literal present), ANOMALY (live == deploy) all excluded.
   Scribe ledger 28 beats, newest 00:06:19.897Z `pushed:true`; none newer than
   `9c28d29`.
2. **PQ-5 → `PENDING`** — 404 / 13,409B / `93ddca9a…`, byte-identical to the
   armed baseline; E1 never fired. P3 holds: vault `ufo-fsd.kimi.page`
   200 / 9,966B / `d93d6a0c…`, 13 PROPERTIES (10 url-bearing), 3/10 dead.
   (Twin `veigapunk.kimi.page` = 10,059B — do not swap the two.)
3. **PQ-2 → `GATE-CLOSED`** — remote `e6bd071`, local `f3d2ecd`, 20 unpushed,
   `sitemap.xml`/`robots.txt` 404/9,379B.
4. **Path base STABLE** — full re-sweep 02:36:54Z: 59 targets / 49 resolve /
   10 declared-absent / **0 new dangling**; all five r15 danglers still absent;
   four new in-round targets all resolve (incl. `~/Projects/origin-work/open-bug-bounties`);
   kake's four domain roots untouched by both drift windows (A `23:51:31.175Z`,
   B `01:45:06.815Z`); lowercase `~/projects` is a distinct inode (27238 vs
   101125103).
5. **History/detector** — 78 rows, full 67 / spot 11, last
   `2026-09-29T00:01:09.976Z` (2.6h), shape MATCH; `probe-delta` 6 events /
   0 phantom / last ENTER lucario 09-27T16:38:27Z; naive symdiff now 52 events
   (~46 phantom) at 78 rows vs r10's 42/40 at 76.

## Adjudication trail (why this is a move, not a script landing)

Critic ruling 1 (pre-evidence): NOT-ELIGIBLE — no trigger fired, and a script
land follows r10's operability precedent; plus two *executable* instrument
counterexamples (interior-history tamper absorbed at exit 0; ±2-line OR
`declaredAbsent` mislabels a genuine dangler). Both were closed
(`deltaEventsExact`/`deltaLastEvent` pins reproduce exit 1 on the tamper
fixture; set-delta gate armed by the shipped pins; opt-in
`pathsAbsenceStrictSameLine`; 9/9 selftest). Critic ruling 2, after the
evidence: **MOVE-ELIGIBLE on both independent branches** — (A) the complete
claim sweep is a *freshness outcome*, not capability (160 claims, 15 stale, 10
in unswept classes, raw recipes); (B) PQ-14 is previously unledgered
live/source drift, independently reproduced by the reviewer. Predicate:
"complete live standing-claim sweep flags a previously unmeasured
stale/unverifiable claim with raw evidence OR catches previously unledgered
live/source drift and repairs/ledgers; instrument alone remains
operability-only." Reviewer verdict `concerns`, 1 FAIL (the self-cite line
number) — fixed in-round; 3 low pre-r15 residue items recorded, not fixed.

## Sibling / adjacency (reported, not absorbed)

Kasegi's two source-loss reports (bounties r15; groknight −681f/41d/14MB at
01:45:06.815Z r16) have **0 kake citation descendants**; kake's own two new
citations into that tree resolve. Revenger bounded a **live, escalating prune
regime** on `~/Projects` roots inside r16 — five instants: W1 ≤23:51:31Z,
W2 00:42:39Z, W3 01:45:06Z, W4 `.ufo-missions` 262→2 dirs ≤02:05:07Z,
W5 groknight re-touched 02:19:20Z — actor undetermined, all `.git` mtimes
contaminated; the kasegi "fleet GC" hypothesis is **not** confirmed
(dispatcher-daemon.out / fleet-ledger.jsonl contain no groknight/prune
unlinks). L0 corroboration line appended (kake | round-16); decision carrier
stays kasegi's r15/r16 entries. kotoba r14's `probe-delta` exit-0 complaint
remains dispositioned by design.

## L2 batch (12 agents, one batched call — all read-only)

planner (move frame), scout-paths (59-target sweep, BASE-STABLE), scout-claims
(160-claim inventory), executor×2 (instrument + armed reads), labrat (timers,
detector, naive-diff repro), revenger (timeline, 5 drift instants, continuity),
critic (2 rulings + instrument fixture attacks), reviewer (~40 citation/numeric
checks; 1 FAIL, fixed), connector (sibling overlap, 0 descendant citations),
sentinel (state guard byte-identical), scribe (report skeleton). Zero fires,
zero pushes, zero systemctl mutations, zero `~/Projects/**` writes.

## Evidence

`/tmp/kake-r16/` — planner.md, scout-paths.md (+4 target/miss/resolve lists),
scout-claims.md + claims.tsv + raw/{claim-checks.md,http.sh,parity.mjs,
canonical.mjs,body/}, freshness-sweep.mjs, freshness-pins.json,
executor-instrument.md, executor-arms.md, labrat-timers.md, revenger-history.md,
critic.md, reviewer-cites.md, connector.md, scribe-draft.md,
sentinel-{before,after}.sha, raw/{final-bare2,offline,selftest,plazir-live-sitemap,
charter-live,pq5,vault,l1-pathsweep.json}. Repo: SKILL.md ×6 edits,
corpus/README.md ×4, corpus/lessons/round-16.md, corpus/knowledge/ ×10
(freshness-sweep.md + freshness-pins.json new; ops-automation,
probe-delta-alerting, drift-detection, publish-queue, sitemap-orphan-audit,
keeper-timer-inert, free-read-verbs, fire-journal-codes corrected),
SCORECARD.md 9→10, LOG.md r16.

## Carried / L0

- **PQ-14** — operator `git push origin main` in `~/Projects/plazir-15-site`
  (5 commits); the instrument then reports `GATE-OPENED` + `MATCH`.
- PQ-12 waits on the operator one-line edit (`fleet.config.json:256`; live
  literal at edit moment `2026-09-29 scribe beat`; next beat ~06:06Z).
- PQ-5 waits on the human Publish+slug click; PQ-2 on the ds4cc push.
- Keeper-timer / lucario-registry L0 questions unanswered since r12.
- `~/Projects` prune regime: L0 (kasegi r15/r16 + kake r16 lines); no kake
  pull/fetch in `origin-work/*` without explicit sanction.