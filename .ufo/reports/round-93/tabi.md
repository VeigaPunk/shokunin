# tabi — round 93 report

L1 `TabiR93a2` (attempt 2; attempt 1 `TabiR93` ended when the orchestrator session was SIGTERM-killed,
`.ufo/watchdog.log` `lane-dead-no-report tabi round=93` 21:09:28). Lane `tabi-shokunin`, base
`192535d7` (the round-92 verifier spot-check commit), final lane hash **`5246985e9b21474ce3350de5bc82579bece5019b`**
(`git ls-remote origin refs/heads/master` → `5246985e9b21474ce3350de5bc82579bece5019b`).

## Work performed

Declared claims (1): **C1 — coverage, capability acquisition `chromium-oopif-backendnode-scope-linux`**
(predicate `C1-CROSS-SESSION-ANSWER-R93`, sourced by S231/S232, both opened this round). It moves r92's
declared limit 5: what a cross-site iframe chooser's `backendNodeId` B names on the PAGE session. On
Chromium 155.0.8059.84 `--headless=new`, B on the page session names a `#document`, the page's pierced
document holds 0 `INPUT#s`, and page-session `DOM.setFileInputFiles(B)` fails with exactly `Node is not
a file input element` and delivers nothing; the iframe session names the `INPUT` and answers. The
same-site arm answers on the page session.

- Instruments: driver `scripts/chrome-cdp-cross-session-answer-round93.mjs` (pin `a0deddda855a`),
  counter `scripts/check-cross-session-answer-round93.mjs` (`--live` runs the sha-pinned driver),
  battery `scripts/negatives-cross-session-answer-round93.mjs` (65 cases, carrying the r92 spot-check
  §8 item-7 classes).
- **Freeze before data** (attempt 1): commit `7a7f39f3` — `plans/round-93.md` (claim, declared limits
  1-6, controls, counting command), `.ufo/waves/round-93/claims.json` (`frozenAt` 20:47:56, committed
  20:48:00), instrument sha256 (`controls/instrument-sha256.txt`), staged sources, and the executed
  controls (`controls/rc.txt`): base has no counter rc 128; r92 receipt under the frozen counter rc 1
  (10 unique ids); real wrong-site run (`--cross-host 127.0.0.1`) rc 1 with behaviour ids; positive rc 0
  at 101 checks; busy-port setup rc 2 (`setup`; attempt with no live holder disclosed and superseded);
  battery 65/65.
- Scored run: commit `bf0bd622` (`.ufo/waves/round-93/scored/c1-live.json`): rc 0, `clean`, 101 checks,
  0 findings, nonce `tabi-r93-live-b39038e077b0`; receipt copied to
  `corpus/evidence/round93/chromium-oopif-backendnode-scope/receipt.json`.
- Records commit `9fac89c3` (attempt 1): knowledge note `corpus/knowledge/chromium-oopif-backendnode-scope-round-93.md`,
  S231/S232, `SKILL.md` `## Round 93 gate registry` (complete rows; supersedes the two r92 rows — §8 item 2),
  README late `## Round 90/91/92 coverage` + r83–89 index, SCORECARD W6 correction (§8 item 3), the
  freeze-stamp gate and the log-section-claims gate (mined mistakes).
- Wave w1: 12 seats via `w1.ready`; the orchestrator was killed mid-wave and finalized
  `w1-results.json` with `output: null` for every seat. Attempt 2 read every seat's report from
  `.ufo/waves/round-93/w1/` and did not re-dispatch. Every C1 verdict is `neutral`
  (`.ufo/waves/round-93/claim-falsification.tsv`, 15 rows):
  - **Reproductions, all clean:** R93Exec1 ×2 `--live` (101) + battery 65/65; R93Exec2 ×3 `--live`
    (101) + one `--reps 10` (311 checks, 38 legs identical); R93Sentinel ×1.
  - **R93Critic1:** 26-clause wording-vs-counter table; 10 receipt-mode forgeries (rc 0), all inside
    declared limits 3-6 — procedure clauses are fixed by the pinned driver under `--live`.
  - **R93Critic2:** 4 procedure variants; `#document` and the exact error hold 15/15 X legs.
  - **R93Critic3** (outside the claim, limit 3): page-session B = 2 is the parent's own `#document` root
    (documentURL = parent URL) 3/3 — the S232 per-renderer id map measured.
  - **R93Mut:** 39/53 distinct counter mutants killed; 14 survivors are battery gaps.
  - **R93Reviewer:** freeze precedes scoring; F1-F6 notes only.
  - **R93Sentinel:** S4 (signalled driver scored `findings` not `setup`) and S5 (counter kill orphans
    the driver) — hygiene defects routed to r94 (SCORECARD r93 Planned).
  - **R93Connector:** 0 sibling hits. **R93Scribe:** knowledge-note draft, source sha256 re-check.
    **R93Exec3:** freeze-stamp gate, selftest 3/3.
  - **R93Scout:** left only re-fetched source bytes (`w1/R93Scout-sources/sha256.txt`, S231/S232
    byte-identical to staged); narrative report lost with the orchestrator kill — recorded as missing.
- Attempt-2 integration commit `c46317ab`: wave evidence, ledger, lesson, SCORECARD r93 section +
  capability row, LOG `## Round 93`, README `## Round 93 coverage`.
- Tip gates (`corpus/lessons/round-93.md` §Gate runs): C1 `--live` re-run rc 0, clean, 101, revision
  `c46317ab` (`scored/c1-live-final.json`); pins 3/3 OK; freeze-stamp rc 0; log-section-claims rc 0;
  append-only rc 1 on corpus/SOURCES.md only (two table rows inserted above `## Paths`, numstat `2 0`;
  disclosed), the other four files `ok`.
- `PREFILE-FALSIFICATION: pass claims=1 rows=15 attack_seats=7 findings=0` — exit 0 (`.ufo/waves/round-93/scored/prefile.txt`)`

Round shape: ONE v1 wave `w1` of 12 seats.
- Roles: 3 executor, 3 critic, 1 mutation-tester, 1 reviewer, 1 sentinel, 1 scout, 1 scribe, 1 connector.
- Attack seats (reviewer, critic, mutation-tester): 5/12 (42 %). Connector seats: 1.
- The L1 holds the §3 planner seat.
- No residual call. Round total 12. Dead seats: 0 hard deaths recorded; all 12 seat outputs were lost
  with the orchestrator kill (`w1-results.json` note); 11 filed reports, R93Scout filed artifacts only.

## Landed changes

All landed with `jj-lane.sh`; the `LOG.md` `## Round 93` entry covers them.

| commit | content |
|---|---|
| `7a7f39f3` | freeze: plan, claims.json, driver/counter/battery, pre-freeze controls, staged sources |
| `bf0bd622` | C1 scored `--live` run |
| `9fac89c3` | records: knowledge note, evidence receipt, S231/S232, SKILL r93 gate registry, README late coverage r90-92, SCORECARD W6 correction, freeze-stamp and log-section-claims gates, w1 spec/dispatch/ready |
| `c46317ab` | w1 evidence (12 seats), w1-results.json, falsification ledger, lesson, SCORECARD r93 section + capability row, LOG r93 entry, README r93 coverage |
| `5246985e9b21474ce3350de5bc82579bece5019b` | tip gate runs (C1 live re-run, freeze-stamp, log-claims, append-only), census end, lesson gate record |

## Before → after measurements

**C1** — counting command (frozen in `7a7f39f3`):

```
node scripts/check-cross-session-answer-round93.mjs --lane /home/vgpnk/Projects/shokunin/tabi-shokunin \
  --expect-driver-sha256 a0deddda855a3eb48f9dd02f6d01eee0f607e9ab319dd74c6182c1d9ecc9a4a0 \
  --live --scratch <ABS> --ports <http,child,cdp> --json
```

| | value | commit |
|---|---|---|
| before | command absent at base (`git cat-file -e 192535d7:scripts/check-cross-session-answer-round93.mjs` → rc 128); the r92 receipt under the frozen counter → rc 1 (10 unique ids) | `192535d7` |
| after (scored) | rc 0, `clean`, 101 checks, 0 findings, 6 legs | `bf0bd622` (receipt `revision` `7a7f39f3`) |
| after (tip re-run) | rc 0, `clean`, 101 checks, 0 findings | `c46317ab` (`revision` field) |

Verdict: **VERIFIED** on the frozen predicate; no wave artifact falsifies its wording (ledger 15 rows,
all `neutral`). SCORECARD: coverage 9 → 9 on the scalar (the lane re-pins no scalar), plus capability
row `chromium-oopif-backendnode-scope-linux` (first-working round 93). Pending non-author closure.

## Sources & frontier

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`

| | census | rows |
|---|---|---|
| start | exit 0, `tabi ok` (`.ufo/waves/round-93/census-start.txt`, 20:41:39) | 230 |
| end | exit 0, `tabi ok` (`.ufo/waves/round-93/census-end.txt`); W04 cross-scope duplicate-URL warnings only | 232 |

Row count: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`.

- **Rows added, tier A (code):** S231 — Blink `inspector_dom_agent.cc` at 155.0.8059.84 (`AssertNode` →
  `DOMNodeIds::NodeForId`; `setFileInputFiles` "Node is not a file input element"); S232 — Blink
  `dom_node_ids.cc` at 155.0.8059.84 (process-static `g_last_id` and id→node map). Quotes, word counts
  (`wc -w`) and digests in `corpus/lessons/round-93.md` §Gate.
- **Rows touched old→new:** none.
- **Frontier advanced:** CDP node-id scope across sessions (OOPIF vs parent renderer); knowledge 105 → 106.
- **Sourced claim:** C1 rests on S231/S232.
- **Mined mistakes** (`corpus/lessons/round-93.md` `## Mistakes`): (1) LOG entries claiming README
  sections never committed (r90/r92) — gate `check-log-section-claims-round93.mjs` exit 1 at base,
  exit 0 at tip after the late sections landed; (2) r92 future-dated `frozenAt` — gate
  `check-freeze-stamp-round93.mjs` exit 1 on r92, exit 0 on r93, selftest 3/3.
- **r92 spot-check §8:** items 1-5 and 7 addressed (lesson §Corrections); item 6 (r91 items 3/5) carried.
- **Assimilation:** none.
- **considerthese:** the lane has no `considerthese/` directory.

## Trend verdicts

- **expansion: improved.** Knowledge 105 → 106; SOURCES 230 → 232; new capability on ground no lane
  instrument held (no earlier instrument sends a node id across CDP sessions).
- **quality: improved.** Two record-drift classes now have gates shown able to fail; r92 §8 routed
  defects repaired by appended records; the claim was reproduced clean by three seats' own live runs
  plus a tip re-run.
- **discernment: improved.** Controls ran before the freeze (no-work ×2, real wrong-site run, positive,
  busy-port setup, 65-case battery); every attack-role artifact is read into the ledger; the
  append-only failure on SOURCES.md and the missing scout narrative are disclosed rather than hidden.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` `## Round 93 gate registry`; `corpus/knowledge/chromium-oopif-backendnode-scope-round-93.md` (error texts S231, id scope S232)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 93` (click → intercept → cross-session describe/answer → correct answer → readback, 6 legs; `.ufo/waves/round-93/scored/c1-live.json`)
- [~] Instructions executable by an agent without oral context — R93Exec1, R93Exec2, R93Sentinel re-ran the frozen command from `plans/round-93.md` alone (`.ufo/waves/round-93/w1/`); lane-dispatched seats, not non-author
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `.ufo/waves/round-93/w1/R93Connector.md` (0 sibling hits); C1 stays inside browser/web-interaction craft

## Extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (Node v24.21.0, system Chromium 155.0.8059.84; no seat reported an install).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no file from this
  round's seats; only orchestrator `.scratch/` entries, left untouched.
- Scratch: `/fast/scratch/hyaku/tabi-r93` removed after landing; no chromium left on this round's ports.
- Open L0 questions: none filed this round.
- Inherited state (attempt 1): uncommitted `corpus/lessons/round-93.md`, `.ufo/waves/round-93/w1/`,
  `w1-results.json`, `w1.ready.dispatched` — all re-read and adopted in `c46317ab`; nothing discarded.
- Routed to r94: R93Sentinel S4/S5, R93Mut 14 battery gaps, R93Critic1 receipt hardening (B on every
  step, page `#document` `documentURL`), SOURCES-aware append-only check (table-row insert).
