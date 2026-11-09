# tabi — round 96 report (L1 `TabiR96`, attempt 1)

Lane `/home/vgpnk/Projects/shokunin/tabi-shokunin`, branch `master`. Base `b16b3aa1`; final lane hash
`e62077ce2315d9b6cd1a4dd4a9d3c4d443c7b840` (`git ls-remote origin refs/heads/master` prints it).

## Work performed

Declared claims (1): **C1 — coverage, capability acquisition `client-oopif-filechooser-linux`** (sourced:
S236). Predicate `C1-CLIENT-OOPIF-CHOOSER-R96`: on Chromium 155.0.8059.84 `--headless=new`, with
puppeteer-core 25.16.0 / playwright-core 1.65.0 attached over CDP, Puppeteer's
`page.waitForFileChooser({timeout: 3000})` ends `TimeoutError` with the child empty on every cross-site
iframe leg (PPX, PPW; on PPW a raw witness on the iframe session receives exactly one
`Page.fileChooserOpened`), while Puppeteer same-site (PPS) and Playwright cross- and same-site (PWX, PWS)
resolve and fill the child. Wording narrowed after the wave by `plans/round-96.md` §Post-wave amendment
A1 items 1-4; counter, driver and numbers unchanged.

- Fresh-start read: not owed (r92-r95 admitted, MANIFEST rounds 1589/1594/1596/1598). r95 spot-check §8:
  items 1 partial (unwritable scratch → `setup`, `ports-bound`, `driver-exit` built into the r96 counter;
  `plans/round-96.md` §Record work), D1-D3 and R95Mut survivors carried in SCORECARD Planned (one claim per
  round; none moves this surface).
- Source opened: Puppeteer `Page.ts` @ puppeteer-v25.16.0 (HTTP 200, sha256 `e7f2f6b8ea8b`), staged
  `.ufo/waves/round-96/sources/Page.ts` → S236 (`corpus/SOURCES.md:251`).
- Instruments (freeze `ba611b22`): driver `scripts/client-oopif-chooser-round96.mjs` (`4020e57ef865`),
  counter `scripts/check-client-oopif-chooser-round96.mjs` (`778d429fe090`), battery
  `scripts/negatives-client-oopif-chooser-round96.mjs` (`950c3ca2e557`); `.ufo/waves/round-96/claims.json`.
- Pre-freeze controls executed and committed in the freeze (`.ufo/waves/round-96/controls/rc.txt`):
  no-work base rc 128; r95 receipt rc 1; positive rc 0 (163 checks); battery 63/63; wrong-site rc 1;
  wrong-library `--live` (puppeteer-core 25.15.0) rc 1 `libs` only; busy-port, SIGTERM (0 chromium left),
  no-deps, receipt-dir, unwritable `/proc` and chmod-500 scratch, launch-fail each rc 2 `setup`.
- Scored `--live` run (`75fe36dc`): rc 0, clean, 165 checks, nonce `tabi-r96-live-c1225d318ea6`, receipt
  sha256 `aad4611df158…` committed at `corpus/evidence/round96/client-oopif-filechooser/receipt.json`.
  Tip re-run at `3f0e422a`: clean 165 (`.ufo/waves/round-96/scored/c1-live-tip.json`).
- Wave w1 (12 seats, `.ufo/waves/round-96/w1/`): 10 neutral, 2 `falsifies-wording` (R96Scribe prose
  "never"/"chooser opened"/S230 citation; R96Sentinel library identity via three fields only) → amendment
  A1. Independent `--live` reproductions all clean: R96Exec1 ×2 (165), R96Exec2 `--reps 10` (515, 50
  legs) + default (165), R96Sentinel baseline (165).
- Records: knowledge note `corpus/knowledge/client-oopif-filechooser-round-96.md`; corpus/README
  `## Round 96 coverage`; SKILL `## Round 96 gate registry`; appended corrections in the r92 and r94 notes
  (R96Connector); lesson `corpus/lessons/round-96.md` (Gate, 2 mined mistakes, wave, leads); mined check
  `.ufo/waves/round-96/mined/check-control-labels.sh`.

## Landed changes

| commit | contents | LOG.md entry |
|---|---|---|
| `ba611b22` | freeze: plan, claims.json, 3 instruments, controls, probes, staged S236 source, census-start | LOG `## Round 96` (freeze paragraph) |
| `75fe36dc` | scored `--live` run + committed receipt | LOG `## Round 96` (scored) |
| `3f0e422a` | knowledge note, S236 + search log, README, SKILL registry, lesson, mined check | LOG `## Round 96` (records) |
| `e62077ce` | wave evidence, amendment A1, narrowing of note/README, r92/r94 corrections, LOG, SCORECARD r96, tip run, falsification ledger, census-end | LOG `## Round 96` (round shape, verdicts) |

## Before → after measurements

- **C1** — counting command `node scripts/check-client-oopif-chooser-round96.mjs --lane <ABS lane>
  --expect-driver-sha256 4020e57ef865e5eed506796238bb981bb4dbcb226e8fe80eb52728585ce63b91 --live --deps
  <ABS npm install of puppeteer-core@25.16.0 playwright-core@1.65.0> --scratch <ABS> --ports
  <http,child,cdp> --json`. Before (base `b16b3aa1`): `git cat-file -e
  b16b3aa1:scripts/check-client-oopif-chooser-round96.mjs` → rc 128; r95 receipt under the frozen counter
  → rc 1. After: rc 0, `verdict: clean`, 165 checks, 0 findings, measured at revision `ba611b22` (master
  tip when the counter ran; shipped in `75fe36dc`); tip re-run at `3f0e422a` clean 165.
  Do-nothing control does not reach the target (r95 receipt rc 1; wrong-site rc 1; wrong-library rc 1).

## Sources & frontier

- Census start (`.ufo/waves/round-96/census-start.txt`): `scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin tabi` → `tabi ok`, exit 0 (W04 warnings only, S220-S223).
- Census end (`.ufo/waves/round-96/census-end.txt`): same command → `tabi ok`, exit 0.
- Rows: 235 → 236 (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`). Added by tier: A +1
  (S236, `mined`, 90d, used-by the r96 note). Rows touched old→new: none (append-only). Rejected: a second
  row for Playwright `crPage.ts` (duplicates S230). Frontier advanced: client-library chooser routing (new
  path from raw CDP r92-r95 to production clients).
- Mined mistakes (lesson `## Mistakes`): (1) a setup-refusal path that never returns (Node recursive mkdir
  spins on `/proc`; shown: first control run hung, `controls/rc-firstrun-hung.txt`; fixed run rc 2);
  (2) a line-anchored edit at a guessed line number dropped control 10 (shown: `mined/labels-mutant.txt`
  rc 1 vs `labels-committed.txt` rc 0).
- Sourced claim: C1 rests on S236, opened this round.
- Assimilation: none. considerthese: no `considerthese/` directory in this lane.

## Trend verdicts

- **expansion: improved** — knowledge 108 → 109 (`ls corpus/knowledge | wc -l`), SOURCES 235 → 236, new
  capability row `client-oopif-filechooser-linux`.
- **quality: improved** — two own-lane over-general statements corrected append-only (r94:52, r92:66-67);
  the unwritable-scratch hang found and fixed with a shown-to-fail control; r95 R95Sentinel `--live` port and
  driver-status bindings now enforced (`ports-bound`, `driver-exit`).
- **discernment: improved** — both `falsifies-wording` findings narrowed explicitly before filing
  (amendment A1); duplicate S230 row rejected; scout's 17 opened sources held as leads, not rows.

## Round shape

ONE v1 wave `w1`, 12 seats: executor ×3, critic ×3, mutation-tester ×1, reviewer ×1, sentinel ×1, scout
×1, scribe ×1, connector ×1. Attack share (reviewer+critic+mutation-tester) 5/12 = 42 %. Dead seats: 0.
Residual call: none. Round total: 12. Planner seat held by the L1 (validator rejects `planner`).
Dispatch: `.ufo/waves/round-96/w1-dispatch.json` via the inline handoff (`w1.ready` 23:49:53, spawned
23:50:17); results `.ufo/waves/round-96/w1-results.json`.

Pre-file falsification ledger: `.ufo/waves/round-96/claim-falsification.tsv` (13 rows; 2
`falsifies-wording` with narrowing `plans/round-96.md`). `python3 scripts/hyaku/prefile-falsification.py --lane tabi --round 96` → `PREFILE-FALSIFICATION: pass claims=1 rows=13 attack_seats=7 findings=0`, exit 0.

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` — no file written by this round's
seats at the fleet root (`.ufo/waves/round-92/w1/R92ScoutSources.md` belongs to souji r92; untouched).

Tool installs: npm `puppeteer-core@25.16.0`, `playwright-core@1.65.0` (and `puppeteer-core@25.15.0` for the
wrong-library control) into `/fast/scratch/hyaku/tabi-r96/` (npm registry; reason: client deps of the
counter); seats installed the same pair into their own scratch. No pacman.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Open L0 questions: none.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` `## Round 96 gate registry`; no non-author verifier named this round
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 96` (scored `--live` run, `.ufo/waves/round-96/scored/c1-live.json`)
- [~] Instructions executable by an agent without oral context — the counting command reproduced cold by lane-dispatched seats R96Exec1/R96Exec2 from the plan text alone (`.ufo/waves/round-96/w1/R96Exec1.md`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; R96Connector found no sibling overlap (`.ufo/waves/round-96/w1/R96Connector.md` §3)
