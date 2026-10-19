# tabi — round 1 (kaika fleet round-1 continuation, 2026-10-19)

Lane: tabi-shokunin (browser & web-interaction craft). Worktree
`/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/tabi-shokunin`, branch `kaika/round`,
base `40a6de87f72b78d90ea627ad89717e55f219001e`. Lane commits (identity
`tabi-shokunin <tabi@shokunin.local>`):

- `a4115fafce511b7f140ea176bcd0807ebf141fc6` — round work (13 files, +1366/−1)
- `9e3b607de722b95da2d7fa83a85d3d38fe11286a` — LOG + SCORECARD records measured against `a4115fa`

Round identity: steered `1` (`.ufo/waves/kaika/steer.md:32`). Fail-closed check passed:
neither `.ufo/reports/round-1/tabi.md` (fleet root or ledger) existed, and the lane LOG has
no closed round 1 in this namespace. The 2026-10-15 fleet round-1 attempt was blocked and
never admitted (`SCORECARD.md:131-216`); training round 1 (2026-10-14) is a different
series. Because `corpus/lessons/round-1.md` is byte-pinned by the lane's own gate (see
Mistakes, M13), this round's lesson is a new file, `corpus/lessons/kaika-fleet-round-1.md`.

## Work performed

Declared claims (3, distinct axes, causally separable):
**C1 operability 7→8** (lowest non-retired axis) — a structural SOURCES census gate;
**C2 coverage 8→9 + capability `sources-registry`** — `corpus/SOURCES.md` plus three
current-art knowledge entries on uncovered ground;
**C3 calibration 8→9** — self-description drift 17→0 and the lane's mistakes mined into
QUALITY criteria. No exploratory claim.

- **Pre-action — `user-20261015-r07` recorded, not retired silently.** It ran and was
  committed (`2676cc8`, 37 evidence files) with no LOG, SCORECARD, report or lesson. Its
  only receipt is byte-identical to r01's already-credited receipt (sha256 `77374a71…`
  both), and its 29 hash seats still MATCH at base. Recorded as executed, unadmitted, no
  credit: `LOG.md:464-476`.
- **L2 swarm, one batched call of 11** (planner, connector, executor ×4, scribe ×2, scout,
  reviewer, critic), each prompt led by `/skill:godspeed` + the verbatim
  `directive.md` bytes, models left to the route table. The provider stalled three
  executor seats (Flake/BiDi errored 21:56–21:57Z; Gate made no progress after 21:32Z).
  They were killed and re-dispatched as fresh seats in one batch of 3. A post-landing
  review wave of 2 (reviewer, critic) ran before the commit. Every L2 was a leaf; none
  committed.
- **C1** — `scripts/check-sources.mjs` (`a4115fa`). Exit 0 clean / 1 failed / 2
  could-not-evaluate. It reads with `O_NOFOLLOW`; refuses symlinked, non-regular and
  escaping used-by paths; maps fleet E/W codes; and offers `--since`. 25 hermetic
  self-test cases, one of them checking row and tier parity against the contract's own
  awk programs. Receipt: `corpus/evidence/kaika-fleet-round-1/operability/selftest-receipt.txt`.
  Registry row: `SKILL.md:1610-1617`.
- **C1 fixes from the review wave.** The `supersedes` correction regex was dead; row-id
  matching was substring; used-by split only on `,`; `www.` was not normalized. All are
  fixed, each with a self-test case. A non-regular-registry case with refusal-detail
  asserts was added because the critic found criterion 6 unmet.
- **C2 registry** — `corpus/SOURCES.md:11-61`: 27 rows, each opened this round, with 4
  study paths, a 5-entry search log and leads. The lesson Gate holds the fetch record
  for every row: quote ≤25 words, location and raw sha256
  (`corpus/lessons/kaika-fleet-round-1.md:32-84`).
- **C2 knowledge** — three new entries, each opening with `source:` / `verified-at:` /
  `recheck:`:
  - `corpus/knowledge/chrome-remote-debugging-profile-boundary.md` — read first-hand
    from `remote_debugging_server.cc` @main:169-177. The ≥136 default-profile refusal is
    compiled only into Google-branded desktop builds and fails closed. This host's
    unbranded Chromium 152 does not enforce it, so the runbook's `--user-data-dir`
    stays the guard.
  - `corpus/knowledge/webdriver-bidi-capability-matrix.md` — maps each CDP evidence
    surface tabi uses to its counterpart in the BiDi Working Draft of 2026-10-08. Every
    row says locally measured: no.
  - `corpus/knowledge/web-flake-retry-evidence.md` — the Playwright 1.64 `--shuffle`
    claim is confirmed from the release notes; the note defines what a receipt must keep
    for a flaky result.
  - Map rows: `corpus/README.md:161-169`.
- **C3 reconciliation** — the 15 unmapped notes are now mapped and the frontier restated
  (`corpus/README.md:123-194`). The owed training round-11 lesson is written
  (`corpus/lessons/training-round-11.md`, closes O5), and r07 is recorded.
- **C3 learning** — 15 mistake classes, M1–M15, are mined at
  `corpus/lessons/kaika-fleet-round-1.md:12-30`. QUALITY criteria 6–11 and 13 cite them
  (`corpus/QUALITY.md:10-30`); criterion 12 is the contract's source-tier rule.
- **SKILL.md stays lean.** One append of 20 lines (`SKILL.md:1598-1617`): a pointer to
  `corpus/SOURCES.md`, three durable decision rows and the gate registry row. The
  freshness-pinned prefix is intact.
- **L1 re-opened 9 rows itself** (S001, S002, S004, S013, S017, S020, S023, S026, S027).
  The quotes are present. Seat sha256 matched except S001, a dynamic page. S026 was
  re-read through the Stack Exchange API after a challenge page.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| r07 recorded, no credit | `LOG.md:464-476` | `a4115fa` |
| `scripts/check-sources.mjs` + receipt + SKILL registry row | `LOG.md:477-507` (C1) | `a4115fa` |
| `corpus/SOURCES.md`, 3 knowledge notes, README admits/frontier, census receipt | `LOG.md:477-507` (C2) | `a4115fa` |
| README reconciliation, `training-round-11.md`, `kaika-fleet-round-1.md`, QUALITY 6–13 | `LOG.md:477-507` (C3) | `a4115fa` |
| SCORECARD: claim table, capability row, saturation, planned/retired | `LOG.md:477-507` | `9e3b607` |

## Before → after measurements

All three claims were measured on `40a6de87f` (before) and `a4115fa` (after). The full
commands are in `SCORECARD.md:393-421`.

- **C1 operability 7→8:**
  - Receipt in tree: 0 → 1. Command:
    `git ls-tree -r --name-only <rev> | grep -c '^corpus/evidence/kaika-fleet-round-1/operability/selftest-receipt.txt$'`.
  - Self-test: file absent → `SOURCES_SELFTEST verdict=clean cases=25`. Command:
    `node scripts/check-sources.mjs --self-test | tail -1`.
- **C2 coverage 8→9:**
  - Knowledge notes opening with `source: S###`: 0 → 3. Command:
    `git grep -l '^source: S[0-9]\{3,\}' <rev> -- corpus/knowledge | wc -l`.
  - SOURCES rows: 0 → 27, from the contract census in
    `corpus/evidence/kaika-fleet-round-1/sources/census-receipt.txt`. Malformed 0, no
    duplicate, enum, tier-inflation or missing-used-by output. Histograms: A=21 B=4 C=2;
    mined=19 queued=6 rejected=2.
  - Cross-checks: the gate reads `verdict=clean`, and the in-flight fleet census
    `validate` reads `ok`.
- **C3 calibration 8→9:** drift 17 → 0, and QUALITY criteria citing the lesson 0 → 7.
  - Drift parts: notes missing from the README map 15 → 0; executed waves missing from
    LOG 1 → 0; training rounds without a lesson 1 → 0.
  - Commands: `LC_ALL=C comm -23` of the knowledge listing vs README mentions;
    evidence-dir IDs grep'd in `LOG.md`; lesson-file presence for rounds 1–11; and
    `grep -c 'kaika-fleet-round-1.md#mistakes' corpus/QUALITY.md`.
- **No harm, read on `a4115fa`:**
  - `FRESHNESS_GATE verdict=clean matched=34 unique=34`, unchanged.
  - `ROUND_CONTRACT verdict=clean rounds=10`, unchanged.
  - `USER_ROUND_CONTRACT verdict=failed finding=round_count` (6/10). It was red at base
    with the same finding.
  - Existing self-tests: 12, 4 and 4 cases, all clean.
  - Append-only byte prefixes hold for LOG, SCORECARD, SKILL, QUALITY and README.
    Protected files are unchanged: `round-1.md`, `PROVINCE.md`, `SHONEN.md` and
    `check-freshness.mjs`.
  - Depth, freshness and adjacency: no claim, still 8.

Per-claim self-verdicts, all pending non-author verification:

- **C1 verifies.** Pre-landing critic: "verifies-with-fix"; the fixes are applied.
- **C2 verifies.** Pre-landing critic: "verifies-with-fix". S012 is re-kinded as `docs`
  with narrower `teaches`, and the capability row is added.
- **C3 verifies, by self-verdict — the critic dissents.**
  - Critic's dissent, recorded verbatim in spirit: a mention-count can be gamed; it
    reads as reconciliation, not calibration.
  - Answer, a content spot-check by the reviewer:
    - 5 of the 15 new README rows, picked by seeded random draw, are faithful to their
      notes.
    - The `training-round-11.md` Gate commands re-run to the same values; two stale
      counts were fixed.
    - Every fact in the r07 LOG paragraph checks out.
    - 7 of 7 lesson-derived criteria trace to Mistakes rows marked `none`.
  - The rationale: `AXES.md` defines calibration as "SHONEN/SCORECARD entries match
    observed repo state", which is what this measures.
  - **The operator rules on C3.**

## Sources & frontier

- **SOURCES rows: 0 → 27.** Counted with
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` at `a4115fa`
  (file absent at base).
  - Added by tier: A 21, B 4, C 2.
  - By status: mined 19, queued 6, rejected 2 — S026 fixed-sleep answer and S027
    port-9222-on-everyday-profile recipe, each with reason and flip.
- **Rows touched old→new:** none; every row is new. In-round amendment before commit:
  S012 changed from `code`/broad `teaches` to `docs`/narrow, on critic review.
- **Frontier rows advanced** (`corpus/README.md:171-194`):
  - WebDriver BiDi: open → docs-held (spec map; runtime unmeasured).
  - New, docs-held: Chrome ≥136 profile boundary; runner flake receipts.
  - Playwright accessible locators / ARIA snapshots: lead → opened rows S023–S025,
    queued.
  - WebMCP spec: lead → S020, queued.
  - Evidence-byte archival: restated as superseded (64 groups / 45 manifests at base).
  - Extension↔daemon handshake, native WebMCP, rate/ToS and real-site journeys: restated
    `open`.

## Mistakes

Classes mined: **15**, M1–M15 (`corpus/lessons/kaika-fleet-round-1.md:12-30`).

- **M1–M12** come from history and are each re-verified this round. Examples: anchor
  slips; the over-claimed extension-target sighting; the tooling-safety defect in
  freshness gate v1; the unrecorded r07 wave; redundant Brave re-rejects; the blocked
  2026-10-15 dispatch; the owed round-11 lesson; the frozen coverage map.
- **M13–M15 happened in this round:**
  - M13 — a scribe appended to gate-protected `corpus/lessons/round-1.md`. Caught before
    commit by reading `baseline-census.tsv` and `check-round-contract.mjs:110-118`, then
    reverted.
  - M14 — provider stall killed seats and left partial work.
  - M15 — the L1 relayed a sibling's anchor without opening it, and the path was wrong.
- **Criteria added: 7 lesson-cited** — QUALITY 6 (gate input pinning and refusal
  self-tests), 7 (an executed wave lands in LOG or is retired), 8 (pin repeated rejects),
  9 (dispatch only on resolved bindings), 10 (no admission while a round's lesson is
  missing), 11 (the index map stays complete or states its gap), 13 (pre-write check
  against gate-protected paths).
- **Plus 1 contract-derived:** criterion 12 (source tier).

## Trend verdicts

- **Expansion: improved.** Three admitted knowledge entries on ground where the base
  corpus had 0 hits for `bidi`, `flak` and the word `ARIA`. Each cites `mined` rows
  (contract rule 4). Evidence: `LOG.md:477-507`, `SOURCES.md:15-33`.
- **Quality: improved.** A new runnable gate whose defects the reviewer found and fixed
  under test (25 cases). Three opened-source rejections are kept. Stale counts were
  corrected, and the L1 re-opened 9 rows. No axis harmed (no-harm readings above).
- **Discernment: unchanged, pending.** No outside non-author admit/reject spot-check has
  happened yet. The in-round critic dissent on C3 and the reviewer's content check are
  recorded but are lane-internal (`LEARNING.md` requires an outside check). This flips
  only on the orchestrator's verification.

## SHONEN

`SHONEN.md` is byte-pinned by the lane gates and was left unchanged; the marks below are
this round's assessment, `[~]` only (non-author verification owed).

- [~] SKILL craft — `SKILL.md:1598-1617`: decision rows citing `corpus/knowledge/*` plus the sources gate registry row. Historical tables and pins: `SKILL.md` §Approval table `:697`.
- [~] End-to-end task — `corpus/knowledge/multi-step-journey.md` §1–§2 (4-page loopback journey, logged `LOG.md` round-3). This round adds documentation-tier entries, not a new browser task.
- [~] No-oral-context — `corpus/knowledge/executor-test-sufficiency.md` §4 (SUFFICIENT). The new SKILL rows point to self-contained notes.
- [~] PROVINCE accuracy — `PROVINCE.md` unchanged and still accurate for this round's surfaces (CDP/profile/BiDi/flake evidence). kaidoku's Playwright install note is cited without being absorbed (`web-flake-retry-evidence.md` §4). The connector's kake/kagi port-9222 shared-profile lease is reported, not touched.

## L0 questions

- tabi | round-1 | Ratify tabi's round namespace. This "kaika fleet round-1" sits beside training round 1 (2026-10-14) and the blocked 2026-10-15 fleet round-1 attempt. Is the next steered tabi round 2?
- tabi | round-1 | `SHONEN.md` and `corpus/lessons/round-N.md` are byte-pinned by the lane's own gates (`corpus/evidence/pstack-20261015/baseline-census.tsv`, `protectedPath` in `scripts/check-*-contract.mjs`). PROTOCOL `:417` wants SHONEN regenerated verbatim from the canonical template. Authorize a gate re-baseline, or exempt tabi?
- tabi | round-1 | `scripts/check-user-round-contract.mjs` has been red since the user swarm stopped at r06/r07 (`finding=round_count`, 6 of 10). Retire the 10-round expectation, or keep it red?
- tabi | round-1 | Promotion. SHONEN has been 4/4 with named non-author verifiers since round 3, yet `MANIFEST.json` has no tabi roster row. Rule on it.

## Integrator notes

- **Push.** No push. The standing operator rule "No push" overrides `MISSION.md:79` commit-then-push; operator-gated artifacts are committed, not pushed. This report is uncommitted for the integrator to commit with `--author="tabi-shokunin <tabi@shokunin.local>"`.
- **Probe paths.** The fleet probes named in the prompt's §6.3 as being in `.ufo/waves/kaika/` live in `.ufo/waves/kaika-w1/` (`critic.md`, `art-*.md`, `mistakes.md`).
- **Watchdog.** `scripts/shokunin-watchdog.sh:14` `LANES` still omits tabi (O14, operator-side).
- **Fleet ledger.** `MANIFEST.json` has no tabi rows for the 2026-10-15 continuation rounds or for this round.
- **Fleet census.** `fleet-census/scripts/sources-census.sh` is uncommitted in the fleet-census worktree. Tabi's gate emits its E01–E11 and W03 codes, and `validate --file` read `ok` on tabi's `SOURCES.md`.
- **Stale frontmatter.** `SKILL.md:4` still says "Rank: shonen (probation)". It sits inside the freshness-pinned prefix, so the lane cannot correct it without a re-baseline.
- **Carried defect.** `corpus/knowledge/carried-debt-closure-r8.md:5` still carries the malformed 37-hex pin (O13). It is reported, and stays unrepaired because a fix would edit an old note in place.
- **Environment.**
  - The shell `cd` hazard was relayed to all live L2s; no tabi seat wrote outside the worktree (checked with `git -C <fleet root> status`).
  - Provider exhaustion on the executor route stalled 3 seats; they were re-dispatched.
- **Measurement scope.** The C3 drift command counts `user-2*` and `pstack-2*-r*` evidence dirs. Future kaika evidence groups need to be added to that pattern, as the reviewer noted.

## Post-review fixes

Orchestrator adjudication (non-author reviewer: admit with conditions, 6/6 agree; critic:
C2 verifies, C1/C3 fixable). Lane commit **`5cdc97654b71c81da9e324f619a335a1594d1e02`**
(`tabi-shokunin`, pathspec-limited, credential sweep empty). No new claims.

1. **C1 — Registry scoping.** `scripts/check-sources.mjs` now validates `S###` rows only
   inside `## Registry`; a row in any other section fails `row_outside_registry`. New case
   `row-outside-registry`. `node scripts/check-sources.mjs --self-test` →
   `SOURCES_SELFTEST verdict=clean cases=26` (was 25). Live registry →
   `SOURCES_GATE verdict=clean rows=28 … findings=0`. Probe: a valid copy of S001 renamed
   S900 and placed after `## Leads (unopened)` → `FINDING id=row_outside_registry row=S900`,
   exit 1. Receipt: `corpus/evidence/kaika-fleet-round-1/operability/selftest-receipt-post-review.txt`.
2. **C3 — locale-safe command** (appended, `SCORECARD.md:446-456`):
   `( export LC_ALL=C; comm -23 <(git ls-tree --name-only <rev> corpus/knowledge/ | xargs -n1 basename | sort) <(git show <rev>:corpus/README.md | grep -o 'knowledge/[a-z0-9-]*\.md' | sed 's|knowledge/||' | sort -u) | wc -l )`
   → `15` at `40a6de87f`, `0` at `a4115fa`, no `comm` warnings. Without C, under
   `en_US.UTF-8`, it prints `comm: file 1 is not in sorted order`. The drift total stays
   17 → 0.
3. **M-1 — inference stated as observation.** Corrections appended at `SKILL.md:1619-1629`,
   `corpus/README.md:196-199` and `LOG.md:508-525`, which corrects `:491`. SOURCES
   contract rule 2: new row **S028**, `supersedes S004 —`, re-fetched by the L1 with
   sha256 identical to S004's. Rows 27 → 28 (A 22, B 4, C 2; mined 20). In-place cells
   touched: none.
4. **M-2 — SHONEN.** Regenerated verbatim from the canonical seed (`PROTOCOL.md:425-432`,
   diff against the seed identical). All four boxes are `[~]`, each with a pointer. L0 Q4's
   promotion premise ("4/4 with named non-author verifiers") is **withdrawn**.

**Fleet census:** `TZ=UTC bash …/fleet-census/scripts/sources-census.sh validate <worktree>`
→ `tabi-shokunin ok`, **exit 0**. The first attempt hit a mid-edit syntax error in the
tool (exit 2); a retry 45 s later was clean.

**Gate consequence — reported, not hidden:** `SHONEN.md` is byte-pinned by the lane's own
`scripts/check-round-contract.mjs` and `check-user-round-contract.mjs` (`protectedPath`).
Both now read `verdict=failed finding=history_rewritten detail=Protected bytes changed:
SHONEN.md`. `ROUND_CONTRACT` was clean before this change. This is the direct effect of the
ordered regeneration, and it makes L0 Q2 (re-baseline the lane gates or exempt tabi)
blocking for a green operability gate. `FRESHNESS_GATE` is still clean at 34/34.

**L0 Q4, revised:** tabi | round-1 | SHONEN is now 0/4 `[x]` (4 `[~]`). Promotion needs an
outside non-author verifier per box. No promotion ask stands.
