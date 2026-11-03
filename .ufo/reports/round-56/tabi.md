# tabi — round 56 report (2026-11-03, Linux host)

Lane head at round end: `43d9e0f6` (pushed; `git ls-remote origin refs/heads/master` →
`43d9e0f6f4523059d5ae87139baeba03281c6ffa`). Baseline `faee4cb2`. Freeze `ad3e2afd`. C1 data
`3b3c5d77` → correction 1 `909b3892` (the frozen correction flow, cycle 1 of 2; the red receipt
kept). C2 data `c2aa8447`. Work `da151b26`; gate receipt `43d9e0f6`. Axes at round start:
adjacency 8, coverage 9, depth 9, operability 9, freshness 9, calibration 9; saturation 8 /
window 3; the r55 capability row keeps the window RESTARTED (round 56 = position 1) — the nudge
is inactive, the lowest-axis obligation applies. Claims: 2 (C1 adjacency, C2 coverage). Both
verified; no axis harmed (self-derived; the non-author closure re-derives everything).

**Fresh-start ruling:** rounds 53–55 were all ADMITTED (no three-rejected streak), so no
fresh-start round is owed. The refused claim classes remain ruled out by construction: r42
(counter greens synthetic receipts) — the r56 counter pins committed-byte digests
(`--expect-driver-sha256`), requires the invocation-bound nonce on the data page, typed values
and server log, and ships 39 hand-declared fixtures with exact-match expected sets; r43
(in-model do-nothing seats) — no wave/seat claim is declared; r47 (reasoned-not-measured
after-states) — both after-states are instrument outputs at named revisions.

**Host delta:** round 55 ran the webview2 surface on the Windows host; this Linux host cannot
run it. The host offers `/usr/bin/chromium` = Chromium 155.0.8059.84 (Arch) — a WRAPPER that
prepends the user's `~/.config/chromium-flags.conf` (sentinel RISK 1: the user's own extension
loads into a fixture browser; RISK 3: the crashpad handler writes into the user's default
profile). The C2 runner therefore redirects `HOME`/`XDG_CONFIG_HOME` to a throwaway dir under
the scratch and adds `--disable-extensions` — amended PRE-freeze, smoke re-run green.

## Work performed

Claims declared (frozen in `.ufo/waves/round-56/claims.json` before any seat ran):

- **C1 — adjacency (lowest owned axis, 8):** the v16 adjacency meter (v15 relabelled
  r55→r56; 277 logic lines byte-equal on both sides; diff committed
  `.ufo/waves/round-56/counters/v15-v16-meter.diff`) admits the lane state at the data
  revision after the audit and delta ledgers re-bind at ONE fresh sibling-head snapshot.
- **C2 — coverage (capability acquisition `chromium-keyevent-control-keys-linux`):** the
  Linux host's Chromium 155 headless surface carries the form fixture's control-domain key
  leg with page-side DOM witnesses (End negative-edit witness, Backspace residue + exact
  restore, Tab activeElement witness, ONE Enter keyDown with `text: "\r"` driving the
  implicit submission witnessed server-side and client-side), scored green by the frozen
  counter over committed bytes.

Work items, each with evidence:

- **Wave w1 (the round's single v1 wave, 12 seats) dispatched via the inline spawn handoff**
  (`w1.ready` → `w1.ready.dispatched` 2026-11-03T15:03:39; results
  `.ufo/waves/round-56/w1-results.json`; all 12 settled, 0 dead). Seat-role mix: scout,
  executor×4 (one is the labrat-class probe — the validator rejects `labrat` as a swarm role,
  so the probe rode an executor seat; the L1 holds the planner seat, which the validator
  rejects as a swarm role), scribe, connector, reviewer, critic, mutation-tester, sentinel.
  Attack share 3/12 = 25% (reviewer, critic, mutation-tester). Residual call: none. Round
  total: 12 seats.
- **C2 runner built and amended pre-freeze** — `scripts/chrome-cdp-loopback-round56.mjs`
  (sha `26da87bb…`): loopback-only fixture, per-keystroke prefix witness, the four control
  legs, keyed sweep by token + profile path + crash-db path, throwaway HOME/XDG,
  `--disable-extensions`, shape-only argv; smoke green, `--path-selftest` 6/6
  (`w1/R56Runner.md`; artifacts `w1/R56Runner-artifacts/`).
- **C2 counter built with 39 exact-findings fixtures** —
  `.ufo/waves/round-56/counters/chromium-receipt-r56.mjs`: 26 frozen ids + 3 pre-freeze
  additions (host-browser-mismatch, host-argv-home-leak, server-log-echo-count — closing
  sentinel RISK 1/4 and making the runner's own echo witness counter-checked); selftest 39/39
  (`w1/R56Counter.md`; do-nothing controls refuse).
- **C1 meter v16 + rebind** — `.ufo/waves/round-56/counters/c1-adjacency-host-v16.mjs`
  (selftest 16/16), ledgers re-derived at a fresh snapshot
  (`corpus/adjacency-host-audit-r56.tsv` 16 rows; `corpus/adjacency-host-delta-r56.tsv` 16
  lane rows + 30 line rows; `w1/R56Adj.md`, `adj/l1-rebind-*`).
- **N1 class fix instrument** — `scripts/check-cited-receipts.mjs` (sha `0457f354…`), proven
  RED at the r55 close revision (`gate/red-at-545b251d.txt`: exit 1, 6 findings / 5 distinct
  missing paths) and GREEN at the r56 work rev (`measure/gate-at-work-rev.txt`: 14 tokens, 0
  missing) (`w1/R56Gate.md`).
- **Frontier sources re-opened** — S083, S153, S161 fetched live, quotes verified verbatim in
  the staged bytes (`w1/R56Scribe.md`; staged copies `.ufo/waves/round-56/sources/`).
- **Sibling-overlap scan** — 78 verbatim-quoted BG hits across all 20 roster lanes with
  dispositions from the frozen vocabulary; 58 of 78 sit in lanes the BG screen never reaches
  (map-covered only), 10 were adjudicated under three stale lane names whose bytes are
  sha-proven identical to revenger/souji/kaidoku (`w1/R56Connector.md`,
  `connector/overlap.tsv`).
- **Attacks** — reviewer: 5 blocking findings (folded: the clean-tree scoring rule, the
  browser-version pin, the audit diff receipt, the N1 count correction, the S153 drift
  disclosure); critic: 9 C2 design attacks + 8/9 C1 attacks (the meter-core items are
  post-freeze disclosures — the v16 core is frozen byte-identical to v15 by the claim text);
  mutation-tester: 8 caught / 1 survivor (m4: the meter selftest never asserts `predicate` —
  next-round instrument work); sentinel: 6 risks, each closed by a rule (three closed
  pre-freeze in the runner; the curl `-q --proto` rule and the fixture-server bind/escape
  rules recorded for the next runner generation) (`w1/R56Reviewer.md`, `w1/R56Critic.md`,
  `w1/R56Mutant.md`, `w1/R56Sentinel.md`).
- **Labrat-class probe** — H1 (Enter implicit submission) and H2 (End non-edit + Backspace
  exact-one-char) both supported 3/3 with negative controls; the `text: "\r"` requirement
  measured (a textless Enter submits nothing) (`w1/R56LabProbe.md`, `labrat/probe.json`).

## Landed changes

Every change below is tied to a LOG.md entry (round-56) and to the commit that carries it:

| Change | Commit |
|---|---|
| Frozen claims + round-open controls (v15 red 19 findings; v16 before-rebind red 30) + wave w1 evidence (spec, dispatch, results, 12 seat reports, staged sources, scout/labrat/gate/connector/reviewer/critic/mutant/sentinel/scribe/adj artifacts) | `ad3e2afd` |
| C1 ledgers re-bound at one fresh snapshot (audit 16 rows: 5 stale + 10 unchanged + 1 moved; delta 16 lane rows + 30 line rows, all carried by exact whole-line quote match) | `3b3c5d77` |
| C1 correction 1 (the rebind tool's trimEnd sha bug — caught by the meter's own sha check; raw-byte re-derivation; rebind receipts) | `909b3892` |
| C2 evidence tree (receipt + six per-step PNGs; nonce `tabi-r56-189d4fd6ffafb77a`) | `c2aa8447` |
| SOURCES (S083/S153/S161 re-opens, used-by + anchor appends), knowledge note 72, round-56 lesson, QUALITY criterion 110, SCORECARD block, PROVINCE round-56 line, LOG entry, measure receipts (meter green, counter green, cross-refusals, selftests, census end, check-sources) | `da151b26` |
| The cited-receipts gate GREEN receipt at the work rev | `43d9e0f6` |

## Before → after measurements

- **C1 (adjacency):**
  - Before (round open, before any lane write):
    `node .ufo/waves/round-55/counters/c1-adjacency-host-v15.mjs --rev faee4cb27982388b18e9a45f292cdfb9dfd1ebc8 --repo /home/vgpnk/Projects/shokunin/tabi-shokunin --fleet /home/vgpnk/Projects/shokunin --json`
    → exit 1, predicate false, **findingCount 19** (6 audit-status-mismatch, 5
    roster-lane-uncovered, 3 delta-lane-not-on-roster, 1 lane-screen-sha-mismatch, 1
    lane-screen-lines-mismatch, 3 lane-screen-head-mismatch) — receipt
    `.ufo/waves/round-56/controls/c1-meter-v15-red-at-round-open.json`, measured at
    `faee4cb2`. (Note: a LATER re-run shows 20–21 findings as sibling heads move; the
    committed receipt is the frozen before-state.)
  - After:
    `node .ufo/waves/round-56/counters/c1-adjacency-host-v16.mjs --rev 909b3892f7f66a55ca9ddc3ad5c93ec069ac1c91 --repo /home/vgpnk/Projects/shokunin/tabi-shokunin --fleet /home/vgpnk/Projects/shokunin --json`
    → exit 0, predicate true, **findingCount 0**, counts {roster 20, mapRows 16, auditRows
    16, deltaLanes 16} — receipt `.ufo/waves/round-56/measure/c1-meter-green-at-correction1.json`,
    measured at `909b3892`. Correction cycle consumed: 1 of 2 (the rebind tool's trimEnd sha
    bug; red receipt `measure/c1-meter-red-at-correction0.json`).
- **C2 (coverage):**
  - Before: `git ls-tree -r --name-only faee4cb27982388b18e9a45f292cdfb9dfd1ebc8 -- corpus/evidence/round56 | wc -l`
    → **0**; the counter on an absent receipt → exit 1, `receipt-missing` (the do-nothing
    control; `w1/R56Counter.md`).
  - After: `git ls-tree -r --name-only c2aa84479a953ca715945f50fffcaddd5ff30141 -- corpus/evidence/round56 | wc -l`
    → **7**; `node .ufo/waves/round-56/counters/chromium-receipt-r56.mjs corpus/evidence/round56/chromium-control-keys/receipt.json --driver scripts/chrome-cdp-loopback-round56.mjs --expect-driver-sha256 26da87bbfcc2eb7034f6815fd48430ce6bd8a12bf5ba21ae766950a840893b7d --json`
    → exit 0, predicate true, findings [], couldNotEvaluate [] — receipt
    `.ufo/waves/round-56/measure/c2-counter-green-at-data.json`, measured at `c2aa8447`.
    Cross-refusals: r55 webview2 counter on the r56 receipt → exit 1, 18 findings
    (`measure/c2-r55counter-refuses-r56.json`); r56 counter on the committed r55 receipt →
    exit 1, 13 findings (`measure/c2-r56counter-refuses-r55.json`). Selftests at the frozen
    bytes: counter 39/39 (`measure/c2-counter-selftest-at-freeze.json`), runner
    `--path-selftest` 6/6 (`measure/c2-path-selftest-at-freeze.json`), meter v16 16/16
    (`adj/v16-selftest.json`).

## Sources & frontier

Registry 161 → **161** rows (counting command:
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 161; census
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`
exit 0 at start AND end — receipts `controls/census-start.txt`, `measure/census-end.txt`; 22
pre-existing W04 duplicate-URL warnings unchanged). Rows added by tier: none (no new row — no
duplicate-URL draft was proposed this round). Rows touched old→new (in-place, logged in the
lesson's Gate): S083 used-by extended (+2 paths), anchor cell carries the r56 raw digest
`2e70de25…` (the r55 raw digest `dc7c3088…` at the SAME byte count no longer matches — drift
disclosed, the located ground re-verified verbatim: the Implicit-submission quote greps 1 hit
at line 2589); S153 used-by extended (+2 paths), anchor cell carries the r56 digest
`d6737c31…` (1,423,170 B — `@master` moved from the anchored `f60f0c02…` at 1,421,620 B; the
modifiers description re-verified verbatim, 1 hit scoped to the command block); S161 used-by
extended (+2 paths), byte-identical re-open (`8ded5eaf…` == the registered anchor). Frontier
rows advanced: the key-event model now holds on a second host class (Linux Chromium 155) —
the knowledge note `corpus/knowledge/chromium-control-keys-round-56.md` (notes 71 → 72) cites
S083 + S153 + S161, all opened this round (the round's sourced claim). `node
scripts/check-sources.mjs` → SOURCES_GATE verdict=clean rows=161 findings=0
(`measure/check-sources-at-work.txt`).

**Assimilation: none — the wave-4 quarantine-first duty is OWED.** The shokuknow checkout is
reachable on this host for the first time (`merge/tabi/`: 148 proposed rows, 86 knowledge
entries; `absent-defect-register.md`: 39 tabi data rows), but rounds 44–55 never ran the
register-slice hand-check (grep over `corpus/lessons/round-4*`/`round-5*` finds no slice
verdicts), so adoption stays CLOSED until the 39-row slice is hand-checked verdict-per-row;
named as the next round's opening item. `considerthese/` does not exist in the lane repo
(checked 2026-11-03).

## Trend verdicts

- **expansion: improved** — the measured surface grew to a second host class: the key-event
  control domain now holds on the Linux Chromium 155 surface (evidence tree 0 → 7; capability
  row `chromium-keyevent-control-keys-linux` enters the table, first-working 56, demonstrated
  by the live run the counter scores green), the knowledge note is admitted on ground the
  coverage map did not hold, and its `source:` cites three `mined` rows re-opened this round.
- **quality: improved** — the regression gate absorbed a full host change AND 16 sibling-head
  movements at ONE correction cycle (the rebind tool's trimEnd sha bug was caught by the
  meter's own sha check — the frozen instrument working as designed; the red receipt kept and
  the fix shown able to fail in the red direction first); the v16 generation bump is
  logic-line byte-identical (277/277, diff committed and reviewed before any run); the
  pre-freeze amendments (sentinel RISK 1/3/4) landed before the freeze with the smoke re-run
  green; the new counter ships 39 exact-findings fixtures; the N1 class fix is an instrument
  proven RED at the r55 close revision; the r55 D54-1 landing claim is corrected of record
  (seven lost files, two of the three "landed" receipts absent). No admitted entry failed a
  re-check (S161 byte-identical; S083/S153 moved and re-verified verbatim, drift disclosed).
- **discernment: improved** — every after-state is an instrument output at a named revision
  (the greens name `909b3892` and `c2aa8447`; the receipts name their nonces); the r55-closure
  carry-ins were corrected of record with measured oracles (N1's absence sweep at two
  revisions; N2's empty-tree check; N3's two-mover disclosure; N5 vacuous); the frozen
  cross-refusal expectation was corrected pre-data by walking the counter's check flow; the
  meter's OR-mutant survivor and the gate's relative-form gap are disclosed as next-round
  instrument work, not smoothed; the lane did not self-check its SHONEN boxes (the
  operator-owned gate routed around per the standing routing).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `SKILL.md` §Approval table, §Evidence ladder, §Runbook; this round added the PROVINCE
  round-56 host line and the chromium control-keys note; prior `[x]` named lane-dispatched
  seats — not non-author (orchestrator ruling, kaika round 1)
- [~] At least one end-to-end domain task executed and logged in LOG.md — the C2 live
  Chromium 155 control-keys run end-to-end (launch → fixture → six legs → teardown 0) at
  `corpus/evidence/round56/chromium-control-keys/receipt.json`; logged in `LOG.md` round-56
- [~] Instructions executable by an agent without oral context — the runner's
  `--path-selftest` 6/6 and the counter's 39/39 selftest are agent-runnable from the committed
  bytes alone; `corpus/knowledge/executor-test-sufficiency.md` §0/§4 stands
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:3-19` + the round-56
  host line; the connector's overlap scan keeps every contested surface adjudicated in the
  frozen vocabulary (78/78 quotes verified); refusal routes revenger/kaidoku/kake/kagi held

## Stale-lane, L0, tools, shape

- **Stale-lane:** none — respawn-per-round driver; this round is tabi round 56, attempt 1; no
  earlier attempt of round 56 died mid-work (`watchdog.log` line 2063: launch 2026-11-03, no
  `lane-dead-no-report` line for round 56).
- **L0 standing:** `tabi | round-44` (the L2-floor/AgentSwarm question) stays OPEN — routed
  around via the inline spawn handoff (the wave ran; the floor's ≥8-L2-subagents intent is met
  by 12 seats in one batched wave). Never treated as answered. No new L0 question filed this
  round.
- **Tool installs:** none (no seat and not the L1 installed or upgraded anything; pacman
  stayed paused per the addendum guard).
- **Round shape:** ONE v1 wave w1 of 12 seats (band 8–16 under
  `scripts/hyaku/ufo-wave-policy.json`; ≥25% attack share: 3/12; ≤2 connectors: 1). Residual
  call: none. Round total: 12 seats. Dead seats: 0 (`w1-results.json`: all 12 settled).
- **Inherited state:** the round-55 uncommitted leftovers named by the r55 closure (N1) were
  checked at round open: none exist on disk or in any commit — disclosed LOST in the lesson
  (Corrections item 1), never silently replaced; no r56 claim cites them.
- **Scratch:** `$HYAKU_SCRATCH/tabi-r56` deleted after landing (the seats' own scratch dirs
  were removed by their seats per the contract; R56Scout's 167 MB and R56Adj's lane-clone were
  removed with the round dir). `/tmp` holds no round artifact.
