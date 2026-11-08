# tabi — round 91 report

**Lane:** tabi (browser & web-interaction craft — 旅)
**Round:** 91, **attempt 3**. **Lane repo:** `/home/vgpnk/Projects/shokunin/tabi-shokunin`
**Base:** `b1d8f07b` (the round-90 verifier spot-check commit; lane clean).
**Scored receipt:** `corpus/evidence/round91/chromium-showpicker-proxy/receipt.json` (nonce
`tabi-r91-l1-1d073adc0b8d`, driver `343eb0f202d9b37a21d948adf0f5eff84fbebf8c195ab99c272fd66580e33015`,
fixtures `a6ecf367…` parent / `01380a98…` same / `01380a98…` child, **15 legs, `failures: []`**,
Chromium 155.0.8059.84 / node v24.21.0).
**Instrument freeze:** D3 `12cbe8a0267f` (`.ufo/waves/round-91/freeze.txt`, per-digest artifact
`freeze-12cbe8a0267f.txt`; D1 `1d073adc0b8d`, D2 `2d825d85aab7` — `plans/round-91.md`
§Re-freeze history). **Lane tip:** `878bc9125b858653615516c804769ef292bb4b4f` (pushed;
`git ls-remote origin refs/heads/master` prints it) — the round was filed at `7c59b264` and this
addendum commit carries the orchestrator's `w1-results.json` handoff (written at 13:36, after the
filing) plus its LOG note. **Axes at start:** all six at 9.

**Attempts and inherited state.** Attempt 1 (12:28:52–13:22:38) authored the six instruments, the
scored receipt, the records and the wave spec, dispatched w1 at 13:15:55, then ended without a
report. Attempt 2 (13:22:42) died at wake (13:23:19). Attempt 3 (this one) re-verified every
inherited byte (five-gate suite on the tip bytes, 202.71 s, all green; the drift gate twice; the
fleet census; every seat artifact read) and then **closed the wave's late seats by direct message**,
because no `w1-results.json` handoff existed at filing (the orchestrator wrote it at 13:36, after
this report; it is committed at `878bc912` and noted in `LOG.md`): six seats that the dead attempt left
unfiled (Exec2, Review1, Critic, Mut1, Scribe, Connector) filed reports on request. **Reused:** the six
instruments, the scored receipt, the record drafts, `w1` evidence. **Repaired:** `freeze.txt`/
`freeze.sh` (a false nonce line), `LOG.md`'s `six gates` and its nonexistent `w1-results.json`
pointer, `SCORECARD.md`'s `10 causal cases`, the claims numeral entries, and both claim verdicts
after the attack seats landed. **Discarded:** nothing.

## Work performed

Declared claims (2, distinct axes): **C1 `coverage` — new capability
`chromium-showpicker-proxy-linux`; C2 `calibration` — the six lane-measurable routed defects of the
round-90 non-author spot-check §8.** Both instrument legs hold on their frozen predicates; **both
claims land NOT VERIFIED as written** on executed non-author counterexamples. The round is an honest
stop: no predicate, counter, battery, kill rule, prior or receipt was changed after data, and the
repairs are routed to r92.

- **C1 — coverage (9), capability `chromium-showpicker-proxy-linux` (new, first-working round 91).**
  The same file/date/colour input shapes in a same-origin and a cross-origin iframe are reached
  through a `window.postMessage` proxy in each child that accepts only the served parent origin; the
  15-leg law table is frozen in `plans/round-91.md` §Claims and measured at
  `corpus/evidence/round91/chromium-showpicker-proxy/receipt.json` (15 legs, 0 failures).
  **Instrument legs:** (a) counter `clean`, `checkCount 30`, 0 findings at the D3 pins and the scored
  nonce on the final bytes (`scored/selftest.json`); (b) battery **44 cases / 0 failed** (positive
  control included) and kill power **32 mutants / 32 killed / 0 survived / 0 crashed / 0 unapplied**;
  (c) capability row `SCORECARD.md:4349-4366`, knowledge note
  `corpus/knowledge/chromium-showpicker-proxy-runtime-round-91.md`, `SKILL.md:3365` `## Round 91 gate
  registry`, gate runner `scripts/selftest-r91-gates.mjs` (five gates). **Independent reproduction:**
  R91Exec1 ran the frozen driver twice (fresh nonces, disjoint ports 19951–19956); both clean at 30
  checks with a law table identical to the scored receipt and to probe4/probe5, disjoint run
  identities; R91Exec2 re-measured leg (b) on the same committed bytes with the same numbers plus
  harness falsification (an inert counter makes the battery 43/44 failed; one inert mutant leaves
  `survived 1`). **Verdict: NOT VERIFIED as written** — R91Critic's executed counterexamples
  (`w1/R91Critic.md` C1-F1–F8): the first sentence's "all three shapes in both frames" is wider than
  the 15-leg plan (same-origin colour is never proxied; counter still 30/30 with every same-origin
  colour behaviour deleted); the frozen law (2) "direct **and proxy** calls" proxy arm has no leg;
  `hasBeenActive=false` on both parent-click arms scores clean 30; leg (c)'s row/note/SKILL items are
  read by no gate; the claims file was narrowed at 13:19:45 **after** the scored receipt (13:07:04)
  and after R91Exec3 filed (13:18:31), and its pin map was replaced D1 → D3 post-data.
  R91Mut1 adds 27/40 surviving counter clauses (20 true battery gaps), R91Scribe the note's N1–N7
  divergences, and R91Connector shows the cross-origin arms are same-site (127.0.0.1, different
  port), not out-of-process frames — a further scope narrowing for the capability row.
- **C2 — calibration (9), the six lane-measurable r90 routed defects**
  (`corpus/lessons/round-90-verifier-spotcheck.md` §8 items 1, 2, 3, 5, 7, 8), counted by
  `scripts/check-record-drift-round91.mjs` over eight statements. Before: **8 findings** at base
  `b1d8f07b` (`scored/drift-before.json`). After: **0 of 8** at tip `21e14593`
  (`scored/drift-a.json`); `--selftest` ok with **8 causal cases**. **Verdict: NOT VERIFIED as
  written** — R91Critic's scratch copy of the nine files the gate reads, with four independent
  violations, scores clean: the false `plan-calls` attribution retained beside `send-log-allowlist`,
  the 225-preflight delta deleted, the counted S224 quote lengthened under its `17-word` marker, and
  SCORECARD rows claiming 31 checks / 99 causal cases (C2-F1–F9). Statement 4 passes on a revision
  the instrument does not implement (`--revision` is an unchecked echo); statement 7 reads the
  artifact the runner itself wrote; §8 item 6's lane-writable half (the r89 "(the committer time)"
  wording) is uncorrected and excluded. R91Mut1: the gate's own `--selftest` kills only **4 of 13**
  clause mutants. The gate is frozen for this round; strengthening is r92 work with the critic's
  tautology fixture as the red case.
- **Wave w1 — ONE v1 wave, 13 seats** (`ufo-swarm-wave.mjs run`, `counts.spawn 13`, policy v1 band
  8–16, `w1-dispatch.json`; `.ready` written by the L1 and taken by the dispatcher,
  `w1.ready.dispatched`). Roles: 4 executor, 2 reviewer, 1 critic, 1 mutation-tester, 1 scout,
  1 scribe, 1 connector, 1 sentinel, 1 simplifier — **5 attack seats of 13 (38 %)**, 1 connector
  (policy cap 2). The L1 holds the planner seat; no planner dispatched (the validator rejects
  `planner`). **Round total 13, no residual call, no dead seats.** **All thirteen seats filed:** Exec1,
  Exec2, Exec3, Exec4, Review1, Review2, Critic, Mut1, Scout, Scribe, Sentinel, Simplifier,
  Connector — six of them (Exec2, Review1, Critic, Mut1, Scribe, Connector) only after attempt 3
  messaged them, because no `w1-results.json` handoff existed after the attempt-2 L1 died and their
  work had no landing path; no seat was replaced. Evidence:
  `.ufo/waves/round-91/w1/swarm-registry.json` + `w1/`.
- **Attack results (all recorded, none greened).** Exec4: 55 single-field mutants, 41 refused /
  14 clean — thirteen reach gaps (chooser `mode`, `hasBeenActive`, the four string mirrors, chooser
  `backendNodeId`, event `at`, `actionAt`, `closedAt`, `interceptSendId`, `soFrameId` in an xo leg,
  forged `replies`/`proxyLog` on a direct leg, `argv[4]` profile dir, `proxyLog[0].at`), M55 is the
  declared receipt-regeneration limit, M38 is refused by `prior-set` alone. Review2: 29
  origin-attribution forgeries, every field the binding reads is refused. Review1: pins 9/9,
  probe/fixture recomputation, six mutate arms — and four reach findings (`prior-set` is
  count-level: the same probe listed twice scores clean 30/30; fabricated driver+fixture pins pass
  30/30; a no-op proxy expression and a wrong `targetOrigin` fail only
  `send-log-allowlist`/`plan-calls`; `hasBeenActive` unread). Critic: both claims falsified with
  executed fixtures (`w1/R91Critic-c1-hasbeen.json`, `w1/R91Critic-c2-tautology.json`). Mut1:
  40 counter mutants (13 killed / 27 survived / 20 true battery gaps) and 13 drift-gate mutants
  (`--selftest` kills 4/13). Sentinel: F1 claims moved mid-wave, F2 the pre-amendment C1 text,
  F3 the false nonce line in `freeze.txt`, F4 presence-only drift statements and a committed
  `working-tree` revision, F5 unpinned control churn. Simplifier: K-3/N-3/C-3/R-3 dead weight and
  "at least" assertions. Scribe: note/record divergences N1–N7, G1–G5. Connector: 20/20 sibling lanes on four surfaces,
  nothing contested (tabi is the only holder of iframe/`postMessage` showPicker ground and of
  `check-record-drift*`), and two limits — the driver binds the first `type=page` target without a
  `Target.*` enumeration, and the cross-origin leg is `127.0.0.1` on another port, i.e. **same-site,
  not OOPIF**. **Ledger:** `.ufo/waves/round-91/claim-falsification.tsv` (18 data rows, 13 seats). Repair status: F3 and F5 fixed in-round
  (per-digest freeze artifact, scored nonce read from `claims.json`, `controls/c1/digests.txt`,
  annotated census artifacts); F4's artifact re-measured at the tip and committed; everything else
  recorded as r92 work in `plans/round-91.md` §Limits discovered by the wave.
- **Frontier step (§2b).** `corpus/SOURCES.md` curated per the contract: S225 and S226 added (tier
  A, fetched this round, located quotes in `corpus/lessons/round-91.md` §Gate), S219 re-opened in
  place. Census command and both runs below. **Mistake mined** (4th row of the lesson's `## Mistakes`):
  `freeze-artifact-reissued-over-a-scored-nonce` — `freeze.sh` truncated `freeze.txt` and re-derived
  a nonce at every re-freeze, so the artifact named `tabi-r91-l1-12cbe8a0267f`, a nonce no receipt
  carries, and the D1/D2 bytes survived nowhere (Sentinel F3, Review1 F2); the fix (per-digest
  artifact, refuse-to-overwrite, scored nonce read from `claims.json`) is committed and re-ran.
  **Sourced claim:** C1 cites S225 (`postMessage` target-origin discipline) and S226 (transient
  activation as a resource with a consuming API), both opened this round by the L1 and re-opened by
  the scout (`w1/R91Scout.md`). **Assimilation: none** — `merge/tabi/` adoption stays closed pending
  the open L0 `tabi | round-57`; this lane has no `considerthese/` directory.
- **Bounds and hygiene.** No seat wrote outside the lane: Sentinel's time-stamped sweep found no
  r91/tabi path elsewhere; the fleet-root sweep
  (`git -C /home/vgpnk/Projects/shokunin status --porcelain`) shows only orchestrator-owned
  `.scratch/` state and another session's `.ufo/l0-questions.md` edit — **no misroot to rehome**. No
  cookie/token/session material. Scratch lived under `/fast/scratch/hyaku/tabi-r91/` and is removed;
  `R91Mut1/work/` resisted removal while that seat was mid-run and was removed by the seat itself
  before it yielded.

## Landed changes

| Commit | Paths | LOG.md entry |
|---|---|---|
| `249b7d0c` (attempt 1) | six instruments, `corpus/evidence/round91/…/receipt.json`, knowledge note, `SKILL.md`, `SCORECARD.md`, `LOG.md`, `README.md`, `corpus/SOURCES.md` 224→226, `QUALITY.md` 164, plans, wave spec/dispatch/registry | `LOG.md` ## Round 91 |
| `21e14593` | `.ufo/waves/round-91` (wave evidence, claims `frozenAmendments`, `freeze-12cbe8a0267f.txt`, `freeze.sh`/`freeze.txt` repair, `controls/c1/digests.txt`, four `scored/control-*.json`, `census-end-final.txt`, `claim-falsification.tsv`, `w1.ready`), `LOG.md`, `README.md`, `SCORECARD.md`, `SKILL.md`, `plans/round-91.md`, `corpus/lessons/round-91.md`, knowledge note | `LOG.md` ## Round 91 (attempts 1–3) + wave outcome |
| `df4ef1fc` | `.ufo/waves/round-91/scored/drift-a.json` re-measured at `21e14593` with the revision recorded | `LOG.md` ## Round 91 (C2 after-run) |
| `a60d2f75` | `claim-falsification.tsv` (Exec2 + Review1 rows), `w1/R91Review1.md`, `LOG.md` seat accounting, `plans/round-91.md` §Limits (prior-set count-level guard, declaration-level pins, proxy execution unproven, `hasBeenActive` unread) | `LOG.md` ## Round 91 wave outcome |
| `7c59b264` | `claim-falsification.tsv` (Connector row, 13/13 filed), `w1/R91Connector.md`, `LOG.md` seat accounting, `plans/round-91.md` §Limits (same-site vs OOPIF, first-target binding) | `LOG.md` ## Round 91 wave outcome |
| `878bc912` | `.ufo/waves/round-91/w1-results.json` (the orchestrator's 13-seat handoff, written after the filing) + `LOG.md` wave-handoff note | `LOG.md` ## Round 91 wave handoff |
| `f3f11579` | `claim-falsification.tsv` (Critic, Mut1, Scribe rows), `w1/R91Critic.md` + its two fixture JSONs, `w1/R91Mut1.md` + results, `w1/R91Scribe.md`, `SCORECARD.md` verdicts, `LOG.md` verdicts, `plans/round-91.md` §Limits (battery coverage, selftest kill power, post-data narrowing, statement narrowness, §8 item 6, colour/date arms) | `LOG.md` ## Round 91 verdicts |

## Before → after measurements

- **C1 (coverage, capability `chromium-showpicker-proxy-linux`).** Counting command:
  `node scripts/check-showpicker-proxy-round91.mjs --lane /home/vgpnk/Projects/shokunin/tabi-shokunin --receipt corpus/evidence/round91/chromium-showpicker-proxy/receipt.json --expect-driver-sha256 343eb0f2… --expect-nonce tabi-r91-l1-1d073adc0b8d --expect-parent-sha256 a6ecf367… --expect-same-sha256 01380a98… --expect-child-sha256 01380a98… --prior-set .ufo/waves/round-91/controls/c1/prior-set.txt --json`
  → **before:** no r91 receipt and no r91 instrument at base `b1d8f07b` (exit 2
  `receipt-unreadable`); the r90 receipt under the r91 counter → exit 1, `schema` first
  (`scored/control-r90-under-r91.json`); **after:** exit 0, **`checkCount 30`, 0 findings**, 15 legs
  — measured at `f3f11579` (gate run on the tip bytes). Do-nothing controls: `controls/c1/noreceipt.txt`
  → exit 2 `receipt-unreadable`; `nowork-proxy-flip.json` → exit 1 `law`/`proxy-law`/`prior-set`;
  `nowork-post-removed.json` → exit 1 `send-log-allowlist`/`plan-calls` (pinned with outputs in
  `controls/c1/digests.txt`). **Verdict NOT VERIFIED as written** (see Work performed).
- **C1 leg (b) — battery and kill power.** `node scripts/negatives-showpicker-proxy-round91.mjs …
  --work <scratch> --json` and `node scripts/kill-power-proxy-round91.mjs … --json`: **before** no
  r91 battery/kill power at base; **after** battery **44/44, 0 failed** and kill power **32 mutants,
  32 killed, 0 survived, 0 crashed, 0 unapplied**, reproduced by R91Exec2 with harness falsification
  (inert counter → 43/44 failed; inert mutant → `survived 1`) — and the seat's disclosed limit: both
  instruments derive from the same counter, so green proves the checks are load-bearing, not that
  they are the right ones (`w1/R91Exec2.md`). R91Mut1's clause sweep shows the limit concretely:
  **13/40** clause mutants killed, 20 true battery gaps.
- **C2 (calibration, `C2-RECORDDRIFT-R91`).** Counting command:
  `node scripts/check-record-drift-round91.mjs --lane /home/vgpnk/Projects/shokunin/tabi-shokunin --json`
  → **before** (same gate, tip bytes, on a base `b1d8f07b` worktree): exit 1, **8 findings**
  (`scored/drift-before.json`); **after** at tip `21e14593`: exit 0, **`checkCount 8`, 0 findings**
  (`scored/drift-a.json`, `revision: "21e14593fd4ad7e21664b8e388c7cba96d6cc401"`; regenerated after
  the evidence commit, so it names its own parent — `df4ef1fc` carries it). Selftest: `--selftest
  --json` → `ok: true`, 8 causal cases. **Verdict NOT VERIFIED as written**: four statements accept
  injected violations, statement 7 is self-attested, statement 4 rides an unimplemented revision,
  and the selftest kills 4/13 clause mutants (`w1/R91Critic.md`, `w1/R91Mut1.md`).

## Sources & frontier

- **Census before → after** (frozen command from `CORPUS.md` §*SOURCES.md — where a shokunin learns*):
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`
  — **before** (round start, `.ufo/waves/round-91/census-start.txt`): exit **0**, rows **224**;
  **after** (round end, `.ufo/waves/round-91/census-end-final.txt`, annotated with the command, the
  exit code and the registry sha256 `5c7b27ad55ea94cad96127ee8679ec7a65f980bce16e42a2f2617a162fb38c39`):
  exit **0**, `tabi ok`, rows **226** (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'` on
  `corpus/SOURCES.md`). W04 cross-scope duplicate-URL warnings persist (pre-existing, not errors).
- **Rows added by tier:** S225 (tier A — WHATWG HTML §9.3 cross-document messaging, `postMessage()`
  target origin; fetched 2026-11-08, 132,045 B, sha256 `26fe488d4437`), S226 (tier A — WHATWG HTML
  §6.4 tracking user activation; fetched 2026-11-08, 454,117 B, sha256 `7499db18f2b3`). Quotes and
  access dates in `corpus/lessons/round-91.md` §Gate; the scout re-located every fragment in live
  bytes identical to the staged copies and the scribe re-derived the counts (`w1/R91Scout.md`,
  `w1/R91Scribe.md`).
- **Rows touched old→new:** S219 re-opened in place at its existing URL — `status` stays `mined`,
  `recheck` stays `2026-11-07` (cadence `90d`), and `used-by` goes
  `corpus/knowledge/chromium-showpicker-runtime-round-80.md, …round-81.md` →
  `…round-80.md, …round-81.md, corpus/knowledge/chromium-showpicker-proxy-runtime-round-91.md`.
  No row was superseded, deleted or renumbered.
- **Frontier rows advanced:** none held. The proxy/`postMessage` capability was named and measured
  but its claim fails as written, so the row stays **entered, not held**; carried: the colour popup
  itself, a second browser build (Edge/WebView2), real-site cross-origin frames (operator approval
  absent; loopback only), the critic's unbound clauses (same-origin colour, parent-activated date,
  `hasBeenActive`), and the connector's same-site-not-OOPIF and first-target-binding limits.
- **Mistake + sourced claim:** the mined mistake and the S225/S226-sourced C1 are in the lesson's
  `## Mistakes` and `## Gate` as above.

## Trend verdicts

- **expansion — improved.** Registry 224 → 226 (S225, S226 tier A); knowledge 103 → 104; six new
  instruments and a 15-leg receipt landed. Evidence: `corpus/SOURCES.md:240-241`,
  `corpus/knowledge/chromium-showpicker-proxy-runtime-round-91.md`, `census-end-final.txt` (exit 0).
- **quality — unchanged.** The measured surfaces are green and independently reproduced (30 checks,
  battery 44/44, kill power 32/32, drift 8 → 0), but the claim that those meters bind the stated laws
  failed, and the battery's clause coverage is 13/40. No regression: nothing previously green went
  red (`scored/selftest.json`, `w1/R91Exec1-score-cold*.json`).
- **discernment — improved.** Five attack seats executed counterexamples that falsified both claims
  rather than greening them: the critic's two fixtures, the mutation sweep's 27 survivors, the
  reviewer's prior-set and pin findings, the sentinel's F1–F5, and an 18-row ledger. Evidence:
  `claim-falsification.tsv`, `w1/R91Critic-c2-tautology.json`, `w1/R91Mut1-results.json`.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:3365` `## Round 91 gate registry` (six instruments, five gates, exact commands), knowledge note (laws, limits, cited S216/S219/S221/S222/S225/S226); non-author verifiers for the r91 block: R91Sentinel (provenance), R91Simplifier (coverage), R91Critic (clause binding).
- [~] At least one end-to-end domain task executed and logged in LOG.md — 15-leg cross-origin proxy run `corpus/evidence/round91/chromium-showpicker-proxy/receipt.json` (0 failures), logged in `LOG.md` ## Round 91; independently re-run twice by R91Exec1.
- [~] Instructions executable by an agent without oral context — `SKILL.md:3365-3372` names every counting command with its pins; R91Exec3 reproduced the C2 before/after and all four C1 controls from those lines alone, and R91Mut1 re-ran the batteries against 40 mutant counters without lane writes.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched this round; every landed path is lane-owned (`249b7d0c` … `878bc912`); Sentinel's out-of-lane sweep found no r91/tabi write outside the lane.

## Addendum — the wave-results handoff

The orchestrator wrote `.ufo/waves/round-91/w1-results.json` (all 13 seats, their outputs and the
wave metadata) at 13:36 -03, after this report's first filing. It is committed at `878bc912` with
the LOG note; the report, the ledger and the verdicts above were built from the seats' filed
reports and the direct messages, not from that file. Nothing else in this report changes.

## Stale-lane

Respawn-per-round driver (hyaku inline); no other mission of this lane is open. Open L0 items routed
around, not answered: `tabi | round-57` (shokuknow register quote-column shift — assimilation stays
closed), `tabi | round-70` (same-user live-verifier threat model). One new L0 line filed for the
verdict question below.

## Tooling

No tool installed or upgraded this round (no pacman transaction; the host-wide pause was respected).
