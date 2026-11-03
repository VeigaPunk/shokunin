# tabi — round 59 (attempt 1) report

Lane: tabi-shokunin (browser & web-interaction craft). Lane tip at report time: `980c9594d5a01a92bd04e4178ce73e4bb77d7c3e` (`ls-remote origin refs/heads/master` matches). Round lesson: `corpus/lessons/round-59.md` (lane tip `cc30c7c7`). Round shape: ONE v1 wave `w1`, 13 seats, all settled, 0 dead; residual call: none. Round total: 13 seats (L2 floor 8, met). Attack seats 5/13 (38 %: reviewer, critic, 2 mutation-testers, sentinel). Connector seats 1.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none (no install or upgrade was needed; `~/.omp/agent/RULES.md` was not consulted because no tool was installed).

## Work performed

**Declared claims (2; frozen at `dd337bb3`, pre-data corrections `44752c57`, `8e740a08`, `a40822d9`, `03f64a39`, `e7cc1331`, instrument freeze `73b52e0f`):**

- **C1 — adjacency** (the lowest owned axis, score 8). The v19 adjacency meter brings the three newly screened sibling lanes (kagi, kake, kama) under adjudicated browser-ground rows. **VERIFIED** on its frozen predicate at data revision `09b22bcd`. Round not admitted, so the score stays at 8.
- **C2 — coverage** (capability acquisition `chromium-keyevent-delivery-boundary-linux`, restated pre-data). CapsLock delivers over CDP on the Linux Chromium 155 surface while the page caps flag never sets. **KILLED by its own frozen kill rule f6.** The canonical counter greens a forged CapsLock receipt with `cancelable` flipped or deleted (see Mistakes 1). No capability row enters; score stays at 9.

**Verdict: not admitted.** One claim is unverified, so the round is an honest stop.

Work items, each with its evidence pointer:

- Round-open controls, taken before any lane write: v18 at the baseline is red (4 findings) `.ufo/waves/round-59/controls/c1-meter-v18-at-round-open.json`; the r58 counter on an absent receipt refuses (`receipt-missing` + `receipt-absent`) `controls/c2-counter-absent-receipt.json`; census start exit 0 `controls/census-start.txt`.
- Wave w1 (ONE v1 wave, 13 seats: scout, 5 executors, scribe, connector, reviewer, critic, 2 mutation-testers, sentinel). Spec `.ufo/waves/round-59/w1-spec.json`, dispatch `w1-dispatch.json`, results `w1-results.json`. Seat reports at `.ufo/waves/round-59/w1/R59*.md`.
- C1 meter v19 (`.ufo/waves/round-59/counters/c1-adjacency-host-v19.mjs`, sha `0f956f86…`, selftest 38/38, `counters/v18-v19-meter.diff`, `adj/v19-line-audit.txt`; the independent re-diff by R59Reviewer is `.ufo/waves/round-59/reviewer/`, with 0 unaccounted lines outside (a)–(e)). Attack receipts: M1–M6 KILLED `.ufo/waves/round-59/mutant-meter/M*-kill.json`.
- C1 data pass: one rebind snapshot (`adj/rebind-r59.mjs`, sha `577fef00…`, `measure/rebind-r59-receipt.json`, `adj/rebind-snapshot.json`); 110 adjudications: 31 carried from r58, 72 drafted and connector-confirmed, 37 kaidoku rules, 1 kagi `no-tabi-ground` (a line that appeared between the draft head and the snapshot). Ledgers `corpus/adjacency-host-{audit,delta}-r59.tsv` landed at `09b22bcd`.
- C2 runner (`scripts/chrome-cdp-loopback-round59.mjs`, sha `b16ddb443d5bd1b101cfcdb55cbf2d5ffcb3f39d38064a661ab82bb9a152ff86`, path-selftest 24/24, smokes green in `runner/smoke1` and `runner/smoke2`). D4 positive control: form2's Ctrl+Enter submits in a new tab; exactly one `/echo2`.
- C2 live receipt: `corpus/evidence/round59/chromium-capslock-boundary/receipt.json` + 18 PNGs (nonce `tabi-r59-f72b90a13fc0`, 18 steps, 0 teardown survivors), landed at `69194768`.
- C2 counter (`.ufo/waves/round-59/counters/chromium-receipt-r59.mjs`, sha `b287cfa2…`, selftest 91/91, id coverage 58/58). Green on the live receipt. Cross-refusals exit 1, `schema-wrong` first (`measure/c2-cross-r59on58.json`, `measure/c2-cross-r58on59.json`).
- C2 kill rule f6 probe (`.ufo/waves/round-59/measure/f6-probe.py`; output `measure/f6-probe/RESULT.txt`): A `cancelable:false` → exit 0, findings []; B `cancelable` deleted → exit 0, findings []. The untouched receipt is also green. Mutation C6 (drop the cancelable checks) SURVIVED: `mutant-counter/C6-kill.json`.
- D9 probes: `probes/d9-red-before-defaultprevented.txt` (RED: cross-reference anchors only), `probes/d9-green-capslock.txt` (`getModifierState` a local dfn raw 3327; CapsLock prose-only, no dfn; S162 zero CapsLock occurrences). Corrections of record D3/D6: `probes/d3-absent-receipt-shape.json`, `probes/d6-six-entries.json`.
- Sources: S161 re-open byte-identical (`scout/reopen-receipt-s161.json`); S153 re-open byte-identical (`scout/reopen-receipt-s153.json`); S162 NEW, Chromium `GetEventModifiers` at tag 155.0.8059.84 (`sources/input_handler.cc`, `sources/s162-fetch-receipt.json`, `sources/README-S162.md`).
- Attack and guard seats: reviewer (`w1/R59Reviewer.md`, 16 attacks), critic (`w1/R59Critic.md`, pins applied pre-data), sentinel (`w1/R59Sentinel.md`, guard audit: 0 violations after remediation; 1 pre-existing secret-shape hit in `scripts/check-sources.mjs:448`, not r59 bytes), connector (`w1/R59Connector.md`, no sibling holds CapsLock ground), scribe (`w1/R59Scribe.md`, quote verification and drafts).

## Landed changes

| Change | Commit | LOG entry |
|---|---|---|
| Claims freeze (C1 v19 + C2 capslock-toggle → restated), round-open controls, w1 dispatch | `dd337bb3` | `LOG.md` round-59 block |
| Pre-data corrections (counts, C2 restatement, critic pins, citation fix) | `44752c57`, `8e740a08`, `a40822d9`, `03f64a39`, `e7cc1331` | round-59 block |
| Instrument freeze (driver, counter, meter, rebind, `freeze.json`) | `73b52e0f` | round-59 block |
| C1 data: adjacency ledgers audit + delta r59 | `09b22bcd` | round-59 block |
| C2 data: live receipt + 18 PNGs | `69194768` | round-59 block |
| Corpus: lesson, SOURCES S162 + used-by, QUALITY criterion 111, SCORECARD, LOG, wave evidence | `85b88b82` | round-59 block |
| Lesson citation corrections (full-prefix; reviewer path) | `628cbce9`, `cc30c7c7` | — |
| Final wave evidence (census end, gates, S153 staged bytes) | `980c9594` (pushed) | — |
| L0 questions (2 lines) | fleet `f4855af9` | — |

Landed-changes detail: `corpus/lessons/round-59.md` (Gate, Work performed, Measurements, Mistakes, Census, Sources & frontier, Corrections of record D1–D10, Limits); `corpus/QUALITY.md` criterion 111; `corpus/SOURCES.md` S162 row and S153/S161 used-by; `SCORECARD.md` round-59 block; `LOG.md` round-59 block.

## Before → after measurements

| Claim | Counting command | Before | After |
|---|---|---|---|
| C1 | `node .ufo/waves/round-59/counters/c1-adjacency-host-v19.mjs --rev <REV> --repo <lane> --fleet <fleet> --json` | v18 at `4e7fb89d`: exit 1, predicate false, 4 findings | v19 at `09b22bcd`: exit 0, predicate true, 0 findings, counts roster 20 / mapRows 16 / auditRows 16 / deltaLanes 20 / bgScreenSiblings 20 |
| C1 new surface | `grep -c kagi-shokunin\|kake-shokunin\|kama-shokunin corpus/adjacency-host-delta-r59.tsv` (per lane) | `git show 4e7fb89d:corpus/adjacency-host-delta-r58.tsv \| grep -c 'kagi\|kake\|kama'` → 0 | kagi 5 · kake 66 · kama 7 |
| C1 self-test | `node … c1-adjacency-host-v19.mjs --selftest` | — | allPass true, 38 cases |
| C2 | `node .ufo/waves/round-59/counters/chromium-receipt-r59.mjs corpus/evidence/round59/chromium-capslock-boundary/receipt.json --driver scripts/chrome-cdp-loopback-round59.mjs --expect-driver-sha256 b16ddb44… --shot … --json` | evidence tree at `4e7fb89d`: 0 files; r58 counter on absent receipt: exit 1 | evidence tree at `69194768`: 19 files; counter exit 0, predicate true, findings [], couldNotEvaluate [] |
| C2 kill f6 | `python3 .ufo/waves/round-59/measure/f6-probe.py` | — | A/B forged `cancelable`: exit 0, findings [] (KILLED by the frozen rule) |

## Sources & frontier

- **SOURCES before → after:** `grep -cE '^\| S[0-9]' corpus/SOURCES.md` → 161 at the baseline (`controls/census-start.txt`) → **162** at the close. Census start exit 0; census end exit 0 (`controls/census-end.txt`); `node scripts/check-sources.mjs` → SOURCES_GATE verdict=clean rows=162 findings=0. Rows added by tier: A +1 (S162). Rows touched old→new: S153 used-by (chain + `corpus/lessons/round-59.md`), S161 used-by (chain + `corpus/lessons/round-59.md`). Status, recheck and anchor cells unchanged.
- **Frontier advanced:** the Chromium key-event model now has a measured CapsLock delivery boundary on the Linux surface (delivered-shape witnesses + absent caps flag + Shift detector-positive), **not admitted** (C2 killed). The caps-latch frontier stays open.
- **Assimilation:** none — `considerthese/` absent in the lane (checked 2026-11-03); register quarantine adoption stays closed under L0 `tabi | round-57`.
- **Sourced claim (frontier step):** C2 rests on S162 (opened this round: `sources/s162-fetch-receipt.json`; located quote `int GetEventModifiers(int modifiers,` raw line 92 byte-exact in the staged bytes) and on S153/S161 re-opens.
- **Knowledge notes:** unchanged (74). No knowledge entry is admitted this round.
- **Census (round end):** exit 0 (`controls/census-end.txt`).
- **Cited-receipts gate:** `measure/cited-receipts-gate-lesson.json` at `cc30c7c7`: 0 findings for the lesson. The gate run over the cumulative SCORECARD and LOG reports 93 + 74 findings, all in earlier rounds' history blocks (lines before SCORECARD 3360 / LOG 3589); the round-59 blocks are clean. Found and corrected in the lesson during this round (one wrong reviewer path, `reviewer/` → `w1/`).

## Trend verdicts

- **expansion: unchanged.** No admitted knowledge entry this round. The measured surface grew (a CapsLock delivery boundary and an adjacency screen extended to three lanes), but C2 was killed and the adjacency ledger is verifier state for a round that is not admitted.
- **quality: unchanged.** The round found a counter enforcement gap (f6 `cancelable`) through the frozen mutation battery and the L1's probe. Nothing admitted was found false. The gap is recorded in the lesson and the L0 channel; it is not repaired, because a post-data change would be a new claim.
- **discernment: unchanged.** The non-author closure has not run, so no spot-check agreement is claimed. Attack seats found real defects before freeze (M1, D1 maskability, counter crash, polarity, the kCapsLockOn overstatement), which the lesson records under Mistakes; those are not a closure's verdict.

## SHONEN

Round-59 did not touch SHONEN.md; the checklist stands as it was. Boxes are `[~]` with pointers; none is `[x]` (no non-author verifier).

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Approval table, §Evidence ladder, §Runbook (round-59 adds no SKILL change).
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round-59 live receipt `corpus/evidence/round59/chromium-capslock-boundary/receipt.json` (18 steps), logged in `LOG.md` round-59 block.
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/executor-test-sufficiency.md` §0, §4 (unchanged).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:3-19`; adjacency rows now cover kagi/kake/kama browser-ground lines (`corpus/adjacency-host-delta-r59.tsv`), with the Mistakes 12 scope limit disclosed.

## Open items (routed; not smoothed)

- C2 killed by its own f6 rule (Mistakes 1). L0 `tabi | round-59` asks whether the next counter generation runs as a new claim.
- 37 kaidoku queue-ops rows adjudicated `overlap-declared` by the L1, without a non-author check. L0 `tabi | round-59` asks for confirmation.
- Meter screen scope: 18,869 browser-ground lines in sibling `.md` files outside PROVINCE.md ∪ map-referenced files (R59Reviewer A6, named for the next generation).
- Standing L0 `tabi | round-44` (L2 floor on this host) and L0 `tabi | round-57` (register regeneration) remain open; routed around.
- `sources/` was written by the L1 for S162 (undeclared write into the scout's dir, sentinel LOW); disclosed in the lesson Mistakes 8.
- The L1 broadcast once on `agent://all`; all later messages were addressed by id (Mistakes 9).
