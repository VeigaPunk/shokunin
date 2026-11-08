# tabi — round 92 report

L1 `TabiR92` (attempt 1). Lane `tabi-shokunin`, base `bdf403ff` (the round-91 verifier spot-check
commit), final lane hash **`ba079d19644f2348f7a695e7cd05f50665e78e4e`** (`git ls-remote origin
refs/heads/master` → `ba079d19…`). Rounds 90 and 91 closed `rejected-honest-stop` on the
amendment-59 class (claim sentence wider than its counter), so this round declares one claim, worded
as its counter's checks, frozen with executed controls before any scoring or dispatch.

## Work performed

Declared claims (1): **C1 — coverage, capability acquisition `chromium-crosssite-iframe-chooser-linux`**
(predicate `C1-IFRAME-CHOOSER-R92`, sourced by S227/S228, with S229/S230 added by the wave scout). It
measures on which CDP session an iframe's file chooser arrives and is answered. A cross-site child
(`localhost` under a `127.0.0.1` parent) is its own `iframe` target under flatten auto-attach, and its
chooser arrives on that iframe session. A same-site child (`127.0.0.1`, other port) has no target,
and its chooser arrives on the page session.

- Probe, then instruments: driver `scripts/chrome-cdp-iframe-chooser-round92.mjs`, counter
  `scripts/check-iframe-chooser-round92.mjs` (`--live` runs the sha-pinned driver), and battery
  `scripts/negatives-iframe-chooser-round92.mjs` (31 cases).
- **Freeze before data:** commit `2bac1048` contains `plans/round-92.md` (claim, declared limits 1-6,
  controls, counting command), `.ufo/waves/round-92/claims.json`, the instrument sha256 values
  (`controls/instrument-sha256.txt`) and the executed controls (`controls/rc.txt`):
  - the base has no counter: rc 128;
  - the r91 receipt under the frozen counter: rc 1, 21 finding ids;
  - a real wrong-site run (`--cross-host 127.0.0.1`): rc 1 with `iframe-target-count`,
    `browser-iframe-targets`, `chooser-session` and `answer-session`;
  - the positive run: rc 0 at 93 checks;
  - the battery: 31/31.
- Scored run: commit `a87c7176` (`.ufo/waves/round-92/scored/c1-live.json`): rc 0, `clean`, 93
  checks, nonce `tabi-r92-live-63a66abf7529`. The receipt was copied to
  `corpus/evidence/round92/chromium-crosssite-iframe-chooser/receipt.json`.
- Wave w1: 11 seats, dispatched by the orchestrator through `w1.ready`. All 11 filed under
  `.ufo/waves/round-92/w1/`, and every seat's C1 verdict is `neutral`
  (`.ufo/waves/round-92/claim-falsification.tsv`, 13 rows):
  - **Reproductions, all clean:** R92Exec1 ran 2 cold `--live` runs (93 checks each), and the battery
    scored 31/31 on its receipt. R92Critic2 ran a 10-rep driver run (289 checks), two more `--live`
    runs, and a 5000 ms window that saw no late or second chooser. R92Sentinel ran the frozen command
    once more.
  - **R92Critic1:** a 16-clause wording-vs-counter table and 7 receipt-mode forgeries. All fall under
    declared limit 6, and the procedure clauses are fixed by the pinned driver under `--live`.
  - **R92Mut:** the battery kills 56/63 counter mutants. The 7 survivors are battery gaps.
  - **R92Reviewer:** confirmed that the freeze precedes the scored run, re-ran every control, and
    filed F1-F8 at low severity.
  - **R92ExecProbe** (limit-5 probe, outside the claim): answering on the page session in the
    cross-site arm returns `Node is not a file input element` 3/3; answering on the iframe session
    delivers the file 3/3.
  - **R92Scout:** both pinned sources are byte-identical on re-fetch. It found that S228's
    eTLD+1 sentence does not decide `localhost`/`127.0.0.1`: neither host has a registrable
    domain. It added Playwright `crPage.ts` as corroboration.
  - **R92Scribe:** drafted the knowledge note.
  - **R92Connector:** 0 sibling overlaps.
  - **R92Exec2:** wrote the append-only gate (mined-mistake fix).
- Post-wave clarifications W1-W6 were appended to `plans/round-92.md` §Wave clarifications. They
  attribute each clause to the counter or to the pinned driver, and record the default `--reps 3`,
  the launcher's user flags, a killed driver reporting `receipt-unreadable`, and the S228/S229
  mechanism. No predicate, counter, driver, battery, pin or control was changed after data.
- Routed r91 spot-check §8 items:
  - 2, 4 and 6 were repaired by **appended** records: QUALITY 165, the SCORECARD
    `## Correction — round 91 capability row`, and `corpus/lessons/round-89.md` §Corrections
    carried by round 92.
  - 1 and 8 are process items: this report was written once, after the last lane commit, and the
    claim was frozen before dispatch.
  - 7 is fixed: the counter records `revision`.
  - 3 and 5 are carried; the r91 instruments are frozen. Table: `corpus/lessons/round-92.md`
    §Routed defects.
- Tip re-run (`.ufo/waves/round-92/scored/c1-live-final.json`): rc 0, `clean`, 93 checks, revision
  `63f5d1dc`; instrument sha256 values 3/3 OK.
- `PREFILE-FALSIFICATION: pass claims=1 rows=13 attack_seats=6 findings=0` — exit 0.

Round shape: ONE v1 wave `w1` of 11 seats.
- Roles: 3 executor, 2 critic, 1 mutation-tester, 1 reviewer, 1 scout, 1 scribe, 1 connector,
  1 sentinel.
- Protocol attack seats: 4 of 11 (36 %).
- The validator refused `labrat` as a swarm role, so the limit-5 probe ran on an executor seat.
- The L1 holds the §3 planner seat.
- No residual call. Round total 11. Dead seats: 0.

## Landed changes

All landed with `jj-lane.sh`; the `LOG.md` `## Round 92` entry and its `## Correction` entry cover them.

| commit | content |
|---|---|
| `2bac1048` | freeze: plan, claims.json, driver/counter/battery, pre-freeze controls, sources staged |
| `a87c7176` | C1 scored `--live` run + evidence receipt |
| `4fe08d26` | w1 spec + dispatch |
| `63f5d1dc` | wave evidence and integration: `w1/`, `w1-results.json`, falsification ledger, census end; knowledge note `corpus/knowledge/chromium-crosssite-iframe-chooser-round-92.md`; SOURCES S227-S230; lesson `round-92.md`; QUALITY 165; r89 appended correction; SCORECARD r92 section + capability row + r91 row correction; LOG correction + r92 entry; README/SKILL round-92 sections; `scripts/check-append-only-round92.mjs` |
| `ba079d19` | tip gate runs (append-only both ranges + selftest, C1 live re-run) and the lesson's gate record |

## Before → after measurements

**C1** — counting command (frozen in `2bac1048`):

```
node scripts/check-iframe-chooser-round92.mjs --lane /home/vgpnk/Projects/shokunin/tabi-shokunin \
  --expect-driver-sha256 0feca90ba0272d92d3444d1b23bf0e85a089946408fe52e383e8ddf740321688 \
  --live --scratch <ABS> --ports <http,child,cdp> --json
```

| | value | commit |
|---|---|---|
| before | the command does not exist at base (`git cat-file -e bdf403ff:scripts/check-iframe-chooser-round92.mjs` → rc 128); the newest lane iframe receipt (r91) under the frozen counter → rc 1, 21 ids | `bdf403ff` |
| after (scored) | rc 0, `clean`, 93 checks, 0 findings, 6 legs | `a87c7176` |
| after (tip re-run) | rc 0, `clean`, 93 checks | `63f5d1dc` (`revision` field) |

Verdict: **VERIFIED** on the frozen predicate. No wave artifact falsifies its wording (ledger 13 rows,
all `neutral`). SCORECARD: coverage 9 → 9 on the scalar (the lane does not re-pin scalar scores),
plus capability row `chromium-crosssite-iframe-chooser-linux` (first-working round 92).

## Sources & frontier

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`

| | census | rows |
|---|---|---|
| start | exit 0, `tabi ok` (`.ufo/waves/round-92/census-start.txt`) | 226 |
| end | exit 0, `tabi ok` (`.ufo/waves/round-92/census-end.txt`); W04 cross-scope duplicate-URL warnings only | 230 |

Row count: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`.

- **Rows added, all tier A:**
  - S227 — CDP Target.pdl `setAutoAttach` at tag 155.0.8059.84 (code);
  - S228 — Chromium process_model_and_site_isolation.md at that tag (docs);
  - S229 — WHATWG HTML §7.1.1 obtain-a-site (spec);
  - S230 — Playwright crPage.ts v1.65.0 OOPIF handling (code).
- **Rows touched old→new:** none of the pre-existing rows. Before its first commit, S228's
  `teaches`/anchor was narrowed and the L1's draft exclusion of the WHATWG Sites text was reversed
  (admitted as S229). Both changes come from R92Scout's finding and are logged old→new in
  `corpus/lessons/round-92.md` §Gate.
- **Rejected:** MDN Same-origin policy (secondary; flip condition recorded).
- **Frontier advanced:** the CDP target/session surface, where an iframe chooser arrives and is
  answered (knowledge 104 → 105).
- **Sourced claim:** C1 rests on S227/S228, opened this round.
- **Mined mistake:** `corpus/lessons/round-92.md` `## Mistakes` 1 records r91's in-place rewrites
  of append-only records.
  - Captured by: PROTOCOL §Round-robin and QUALITY 164, both prose rules with no gate.
  - Fix: `scripts/check-append-only-round92.mjs`. It fails as it should on `b1d8f07b..878bc912`:
    exit 1, `rewritten` at LOG.md:4079 and QUALITY.md:1060.
  - Selftest 4/4; the r92 range exits 0 (`.ufo/waves/round-92/scored/append-only-*.json`).
- **Assimilation:** none.
- **considerthese:** the lane has no `considerthese/` directory.

## Trend verdicts

- **expansion: improved.** Knowledge 104 → 105; SOURCES 226 → 230. The new capability covers ground
  the lane did not hold: the r91 "cross-origin" arm was same-site, and no earlier instrument
  enumerated `Target.*`.
- **quality: improved.**
  - The record defects routed by r91 were repaired by appended blocks instead of rewrites
    (QUALITY 165, SCORECARD correction, r89 lesson correction, LOG correction).
  - The append-only rule now has a gate that is shown able to fail.
  - The claim's instruments were reproduced clean by three seats' own live runs: R92Exec1 ×2;
    R92Critic2 ×3 plus a 10-rep, 20-leg driver run; R92Sentinel ×1.
- **discernment: improved.**
  - Controls ran before the freeze: the no-work control, a real wrong-site run, a positive run and
    the 31-case battery.
  - The six attack-role seats' artifacts are read into the ledger.
  - The scout's correction of the L1's own S228 derivation was taken, recorded old→new, and turned
    the L1's draft exclusion into an admit.
  - Receipt-mode forgeries are disclosed under limit 6, not hidden.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` `## Round 92 gate registry`; decision table in `corpus/knowledge/chromium-crosssite-iframe-chooser-round-92.md` §The measured decision table
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 92` (cross-site/same-site iframe chooser, click → intercept → answer → readback, 6 legs; `.ufo/waves/round-92/scored/c1-live.json`)
- [~] Instructions executable by an agent without oral context — five wave seats re-ran the frozen command or driver from `plans/round-92.md` alone (`.ufo/waves/round-92/w1/R92Exec1.md`, `R92Critic2.md`, `R92Sentinel.md`, `R92Reviewer.md`, `R92Scribe.md`); lane-dispatched seats, not non-author
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `.ufo/waves/round-92/w1/R92Connector.md` (0 sibling hits on 7 terms); C1 stays inside browser/web-interaction craft

## Extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (Node v24 and system Chromium 155.0.8059.84 as found; no seat reported an
  install).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no file from this
  round's seats; only orchestrator `.scratch/` entries, which were left untouched.
- Scratch: `/fast/scratch/hyaku/tabi-r92` removed after landing; no chromium left on this round's
  ports.
- Open L0 questions: none filed this round.
- Inherited state: the lane was clean at start (`jj-lane.sh state` ahead=0 behind=0, tracked=0
  untracked=0); no earlier attempt of r92.
