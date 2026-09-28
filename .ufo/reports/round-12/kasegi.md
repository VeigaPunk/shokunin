# kasegi-shokunin — round 12 report

**Axis move:** coverage 7→9 (proxy: top-level surfaces of `~/Projects/bounties`
with a corpus entry or recorded disposition — 13/18 → **18/18**).
`SCORECARD.md` created this round per AXES.md (was missing). Gap closed: the
`.ufo/` runtime-workspace layer (round-11's last named residual) + `.omp/` +
root `README.md`/`.gitignore` + `pendle-core-v2-public/` (discovered mid-round,
never previously named) + the repo's own git runtime state.

**L2 fan:** 10 subagents in ONE batched call — scouts ×4 (bh* workspaces,
bounty-fleet, sessions, grok-assessment), executors ×2 (.omp/claim-recovery
drafter, skeleton+insertion planner), critics ×2 (falsifying rounds 9–11),
connector (sibling-overlap matrix), reviewer (74-citation audit). Peers
cross-checked each other by IRC and caught two L2 errors in flight
("claim-ship disjoint" → merged ancestor; sessions "248 entries" → 8).

**Deliverables:** `corpus/knowledge/{ufo-workspaces,repo-git-state,target-checkouts}.md`
(new), SKILL.md + "UFO runtime workspaces" section + 8 cited paths, 10 citation
repairs across SKILL.md + 5 corpus entries, `corpus/README.md` coverage map +
3 gaps CLOSED, `SCORECARD.md`, `corpus/lessons/round-12.md`, LOG.md entry,
L0 question filed. Commit `round-12`.

## Headline findings (all live-verified 2026-09-28)

- **ACTIVE live-infra hazard, escalated to L0:** `~/Projects/bounties` is
  stalled mid-interactive-rebase (detached HEAD `58acb6d8`, "editing a
  commit", 0 commands left, autostash present) since **before 2026-09-11**
  (`grok-bounty-assessment` manifest records
  `BLOCKED_ACTIVE_PREEXISTING_REBASE`). `gitMutationBlocker` fail-closes →
  the dispatcher cannot commit/tag/push at all; 903 dirty entries; **every
  Sep 7–15 fleet artifact exists only in the working tree**. `george/` (49 G)
  and `.ufo/` (1.5 G) are untracked AND un-ignored — one `git add -A` from
  ingesting gigabytes. `claims/`: 198 tracked files vs 3,361 on disk (20/274
  program dirs).
- **`.ufo/` is a cited evidence store with rotting references:** 656
  `claims/` files cite `.ufo/…` provenance paths; 51 of 543 JSON refs already
  dangling (incl. `.ufo/missions/` — never existed); `claim-check.mjs`
  resolves none of them. New rule in SKILL.md: copy bytes into the package;
  a `.ufo/` citation is not durable evidence.
- **bh* audit layer:** producer = L0 bounty-warden; 25 workspaces (19
  top-level + 6 under `bounty-fleet/sessions/`, disjoint roots) vs 22 reports
  = 19 shared / 3 report-only / 6 workspace-only / 1 phantom. Verdicts:
  **20 BLOCKED, 2 READY** (intigriti-yahoo + hackerone-superhuman, both
  claim-check OK) — falsifies round 5's "21, all BLOCKED". `reroutes.jsonl`
  (121 records): every cause a grok/xai 403/429 → `devin/swe-2:max` — model
  provenance = resolved route, never the registry pin. Yahoo READY package
  cites the superseded runId (provenance split; that workspace must not be
  pruned).
- **bounty-fleet (805 M keeper tree):** four irreconcilable run counts —
  265 launched / 249 reports / 233+9 plans / 184 ledgered → **81 runs never
  reached the ledger**; b1k-248 + 251–265 silently truncated; two halts
  (launch_cap@64, night_budget); a **second `missions.jsonl`** (525 rows) =
  different state machine from root `ledger/`; `session/` vs `sessions/`,
  `report.md` vs `reports/`, two `plan-round0.md` — three do-not-confuse
  pairs recorded.
- **sessions/bpolish1..8 (117 M):** omp recorder v3 transcripts, 2026-09-15,
  board-polish over origin-work hunt packages. **Refile verdict: NONE** —
  zero non-null `submitted_url`; do-not-refile registry unchanged. Grep trap:
  `no_submission_performed: true` → 471 false positives / 0 real.
- **grok-bounty-assessment-20260911:** frozen, zero live consumers, gate
  BLOCKED with `clean_repository_closure` fail×266 — **unpassable by
  construction** on the dirty tree; 88.30/100 descriptive is an NA-exclusion
  artifact (never quote without the gate string); **self-invalidating** —
  re-running the frozen scorer today hard-fails because its validator
  re-derives cited line ranges against live files (gamma readiness-audit
  rewritten 09-14). `claim-recovery/final-audit.json` likewise superseded in
  place by the package's own 09-14 audit.
- **`.omp/` = second routing truth:** uncommitted `config.yml` rewrites all
  six `fleet_*` roles (→ `devin/swe-2:max` / deepseek-v4.1-flash); root
  README describes git HEAD, not the live router ("9 lanes" stale = 10);
  `registry-check` RED (7 violations, partly checker-resolver artifacts);
  4 non-registry agent cards invisible to every check; `skills/ufo` a drifted
  untracked fork (304 vs canonical 626 lines). Mechanics cross-domain →
  kumitate/protocol (connector matrix); bounty consequence absorbed: the
  resolved-route rule.
- **Provenance pins:** 187/255 `provenance.json` carry a `pin` (remote/clone/
  command families; 11 sparse-clone pins with `tree` sha) — but
  `claim-check.mjs:96-97` **never validates pins**. Vendored target:
  `pendle-core-v2-public/` = shallow clone `f242659` (v6.10.0), pin-bound to
  the cantina-pendle package.
- **Git authority:** all 12 `claim-*` tags are pushed ancestors of
  `origin/main` (third-source corroboration of rounds 9–10); `claim-ship` is
  a merged ancestor line whose `claim-ready:` commit messages are superseded
  by `56d62572` ("claim-ready = exactly the 3 submitted reports") — a
  historical commit message is never current authority.

## Depth repair (measured)

First-ever citation audit (independent L2): **74 checked — 64 OK / 9
spot-mismatch / 1 broken (86.5% clean)**; core receipts, decree texts, gate
line-numbers, and the entire do-not-refile set reproduce exactly. All 10
defects repaired in place, each marked "round-12 correction" (bh verdict
split; claims denominator 275→274 program dirs / 295 packages / 280 gated;
archive missions 19→20; histogram BLOCKED 16→15 + OPERATOR_GATED
nested-not-top-level; `duplicate_of` records only 3892215; "only ops
writers" false — `rank.mjs:203` + 4 others; wordpress redaction-receipt path;
tracker 24/24 + log-end 17:24:52Z; telemetry count as-of dated). Critics also
falsified round-9's LOG wording ("all three + receipt.md" — only mozilla has
one; the registry table itself was correct) and confirmed round-11's census
9/10 (denominator off-by-one). Notably, rounds 1/4/5 **aggregator audits had
already flagged** the 274/295 and 2-READY facts — this round propagates those
late fixes into SKILL.md/corpus.

## Cross-domain (reported, not absorbed)

Per connector matrix: OMP router/fallback mechanics + UFO-FSD session runtime
→ kumitate; route-role contract / gate-integrity defect (registry-check RED)
→ protocol (+ kumitate for implementation); plazir-shared `origin/main`
history → named in repo-git-state. Stalled rebase → L0 question filed
(operator decision: resolve vs intentional freeze). No kake overlap.

**Residual gaps:** `george/` stays parked; `bounty-fleet/sessions|scopes`
(790 M) structure+sample censused, not exhaustively read (deliberate, recorded
in SCORECARD); rebase cause/autostash contents unexamined (git mutation
banned); whether the 3 report-only bh ids ever had workspaces is unobservable
from disk.
