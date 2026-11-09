# tabi — round 97 report (L1 `TabiR97`, attempt 1)

Lane `/home/vgpnk/Projects/shokunin/tabi-shokunin`, branch `master`. Base `607c8b02`; final lane hash
`7b9f5ecbc3cc7e1041c43b40d5cac4ea62a0930d` (`git ls-remote origin refs/heads/master` prints it).

## Work performed

Declared claims (1): **C1 — coverage, capability acquisition `client-oopif-uploadfile-linux`** (sourced:
S237, S238). Predicate `C1-CLIENT-OOPIF-UPLOADFILE-R97`: on Chromium 155.0.8059.84 `--headless=new`,
puppeteer-core 25.16.0 / playwright-core 1.65.0 are attached over CDP, and the target is a file input `#s`
inside a cross-site iframe, with a same-site control. Puppeteer `uploadFile` fills it and `#s` sees exactly
`[input trusted, change trusted]` (PUX, PUS). Playwright `setInputFiles` over the default `connectOverCDP`
fills it and `#s` sees `[input untrusted, change untrusted]` (PLX, PLS). With `connectOverCDP(url,
{isLocal: true})` the events are trusted (PLL). Puppeteer set followed by clear leaves `[]` with `[T, T, U,
U]` (PUC). An absent path resolves in Puppeteer as `[["tabi-r97-missing.txt", 0]]` with trusted events
(PUM). In Playwright the same path gives `Error: ENOENT: no such file or directory, stat '<path>'`, and the
input stays untouched with no events (PLM). On every leg the parent `#pp` stays `[]`. That is 24 legs. After
the wave, `plans/round-97.md` §Post-wave amendment A1 items 1-6 narrowed the wording. The counter, driver
and numbers are unchanged.

- Fresh-start read was not owed: r92-r96 were admitted (MANIFEST tabi rows r92-r96 `admitted`). Round 96
  spot-check §6 was answered as follows:
  - D1: appended corrections in `corpus/knowledge/client-oopif-filechooser-round-96.md` and
    `corpus/lessons/round-96.md` (commit `decbcdfb`).
  - D3: a whole-tree sha256 per client is now in the counter. Freeze control 7, a comment-only
    `CdpSession.js` edit, now gives rc 1 `libs` (`.ufo/waves/round-97/controls/counter-tampered-tree-live.json`).
  - D2/D4: carried in SCORECARD Planned.
- Sources opened by the L1, all staged under `.ufo/waves/round-97/sources/`:
  - Puppeteer `ElementHandle.ts` @ puppeteer-v25.16.0 → S237
  - Playwright `fileUploadUtils.ts` @ v1.65.0 → S238
  - Playwright `injectedScript.ts` @ v1.65.0 → S239 (opened after the wave; it grounds the note only)
  - `chromium.ts` and `crPage.ts` were opened and rejected as rows (reasons in the lesson Gate).
- Instruments, frozen at `4a4e15e3`:
  - driver `scripts/client-oopif-uploadfile-round97.mjs` (`09f0c2fe2895`)
  - counter `scripts/check-client-oopif-uploadfile-round97.mjs` (`8571f6b9971b`)
  - battery `scripts/negatives-client-oopif-uploadfile-round97.mjs` (`22b63727b75c`)
  - claims file `.ufo/waves/round-97/claims.json`
- Pre-freeze controls were executed and committed in the freeze (`.ufo/waves/round-97/controls/rc.txt`):

  | control | result |
  |---|---|
  | no-work, base | rc 128 |
  | no-work, r96 receipt | rc 1 |
  | positive | rc 0, 229 checks |
  | battery | 70/70 |
  | wrong-site | rc 1 (`iframe-targets`) |
  | wrong-library `--live` | rc 1 (`libs`) |
  | tampered-tree `--live` | rc 1 (`libs`) |
  | driver-pin | rc 1 |
  | seven setup refusals | rc 2 each; 0 chromium left |

- Scored `--live` run (`be9487f6`): rc 0, clean, 232 checks, nonce `tabi-r97-live-152ce8256675`. The
  receipt is committed at `corpus/evidence/round97/client-oopif-uploadfile/receipt.json` (sha256
  `6c948131…`).
- Wave w1 (12 seats, `.ufo/waves/round-97/w1/`): 10 seats `neutral`, 2 `falsifies-wording`, both handled
  by amendment A1:
  - R97Scribe F1: the process clauses are driver-pin facts.
  - R97Sentinel: the identity wording ("whole installed package tree", "lockfile integrity").

  Every independent `--live` reproduction was clean: R97Exec1 ×2, R97Exec2 default and `--reps 10` (736
  checks, 80 legs), R97Reviewer, R97Sentinel baseline ×2.
- Records:
  - knowledge note `corpus/knowledge/client-oopif-uploadfile-round-97.md` (including a producer-signature
    synthesis table)
  - README `## Round 97 coverage`
  - SKILL `## Round 97 gate registry`
  - lesson `corpus/lessons/round-97.md`
  - mined checks in `.ufo/waves/round-97/mined/`

## Landed changes

| commit | contents | LOG.md entry |
|---|---|---|
| `4a4e15e3` | freeze: plan, claims.json, 3 instruments, executed controls, probes, staged S237/S238 sources, census-start | LOG `## Round 97` (freeze paragraph) |
| `be9487f6` | scored `--live` run + committed receipt | LOG `## Round 97` (scored) |
| `decbcdfb` | S237/S238 + search log, r97 note, README, SKILL registry, lesson, mined checks, r96 D1 corrections | LOG `## Round 97` (records) |
| `7b9f5ecb` | wave evidence + results, amendment A1, falsification ledger, S239 + post-wave log, note/README narrowing, lesson wave/leads, LOG, SCORECARD r97, census-end | LOG `## Round 97` (round shape, verdicts) |

## Before → after measurements

- **C1.** Counting command:
  `node scripts/check-client-oopif-uploadfile-round97.mjs --lane <ABS lane> --expect-driver-sha256 09f0c2fe2895ee0e035e8107995873328ce74f4e4d6d1ab3c8efd455b8c9e4eb --live --deps <ABS npm install of puppeteer-core@25.16.0 playwright-core@1.65.0> --scratch <ABS> --ports <http,child,cdp> --json`
  - Before (base `607c8b02`): `git cat-file -e 607c8b02:scripts/check-client-oopif-uploadfile-round97.mjs`
    gives rc 128. The r96 receipt under the frozen counter gives rc 1.
  - After: rc 0, `verdict: clean`, 232 checks, 0 findings. Measured at revision `4a4e15e3` (the master tip
    when the counter ran); shipped in `be9487f6`.
  - Do-nothing and wrong controls do not reach the target: r96 receipt rc 1, wrong-site rc 1,
    wrong-library rc 1, tampered-tree rc 1.

## Sources & frontier

- Census start (`.ufo/waves/round-97/census-start.txt`): `scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin tabi` gives `tabi ok`, exit 0.
- Census end (`.ufo/waves/round-97/census-end.txt`): the same command gives `tabi ok`, exit 0, with W04
  warnings on older rows only and none on S237-S239.
- Rows: 236 → 239 (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`).
- Added by tier: A +3 (S237, S238, S239; all `mined`, 90d, used by the r97 note).
- Rows touched old→new: none (append-only).
- Rejected as rows: `chromium.ts` (companion to S238) and `crPage.ts` (same URL as S230).
- Frontier advanced: client direct-set uploads and event trust (r96 had only the chooser path).
- Mined mistakes (lesson `## Mistakes`):
  1. A line-anchored edit at a guessed line was a recurrence of the r96 class. `node --check` was shown
     NOT to catch it (`mined/syntax-mutant.txt` rc 0). The fix is `mined/check-driver-positive.sh`, shown
     able to fail: committed driver rc 0, misanchored mutant rc 1 with 4 failures.
  2. The launch window failed under host load. This was captured by the existing `setup` mapping, so it
     is not counted as a shown fix.
- Sourced claim: C1 rests on S237 and S238, both opened this round.
- Assimilation: none. considerthese: there is no `considerthese/` directory in this lane.

## Trend verdicts

- **expansion: improved.**
  - Knowledge 109 → 110 (`ls corpus/knowledge | wc -l`).
  - SOURCES 236 → 239.
  - New capability row `client-oopif-uploadfile-linux`.
- **quality: improved.**
  - The r96 D1 over-attribution was corrected append-only.
  - The installed-tree identity binding was added and shown to fail on a tampered tree (D3).
  - The note and README phantom wording were narrowed to what was measured, after R97Exec3 (d).
  - The recurring misanchored-edit class now has a mechanical, shown-to-fail check.
- **discernment: improved.**
  - Both `falsifies-wording` findings were narrowed before filing (A1 items 1-6).
  - Two candidate rows were rejected with reasons.
  - Seat-opened leads (R97Scout) were held as leads, not rows.
  - A candidate fix (`node --check`) was shown not to work and was not adopted.

## Round shape

- ONE v1 wave `w1` of 12 seats: executor ×3, critic ×3, mutation-tester ×1, reviewer ×1, sentinel ×1,
  scout ×1, scribe ×1, connector ×1.
- Attack share (reviewer+critic+mutation-tester) is 5/12 = 42 %.
- Dead seats: 0. R97Sentinel's background chains died; the L1 messaged it and it re-ran the variants in
  the foreground and filed.
- Residual call: none. Round total: 12.
- The planner seat was held by the L1 (the validator rejects `planner`).
- Dispatch: `.ufo/waves/round-97/w1-dispatch.json` via the inline handoff (`w1.ready` at 00:25:46).
  Results are in `.ufo/waves/round-97/w1-results.json` (WAVE-DONE received).

Pre-file falsification ledger: `.ufo/waves/round-97/claim-falsification.tsv` (13 rows; 2
`falsifies-wording`, both with narrowing `plans/round-97.md`).
`python3 scripts/hyaku/prefile-falsification.py --lane tabi --round 97` → `PREFILE-FALSIFICATION: pass claims=1 rows=13 attack_seats=7 findings=0`, exit 0.

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only orchestrator-owned
`.scratch/` entries and no file written by this round's seats.

Tool installs:
- npm `puppeteer-core@25.16.0` + `playwright-core@1.65.0`, and `puppeteer-core@25.15.0` for the
  wrong-library control.
- Installed into `/fast/scratch/hyaku/tabi-r97/` from the npm registry, as client deps of the counter.
- Seats installed the same pair into their own scratch.
- No pacman. Scratch was removed after landing.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Open L0 questions: none.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` `## Round 97 gate registry`; no non-author verifier named this round
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 97` (scored `--live` run, `.ufo/waves/round-97/scored/c1-live.json`)
- [~] Instructions executable by an agent without oral context — the counting command was reproduced cold from the plan text by lane-dispatched seats R97Exec1/R97Exec2 (`.ufo/waves/round-97/w1/R97Exec1.md`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; R97Connector found no sibling overlap (`.ufo/waves/round-97/w1/R97Connector.md` §3)
