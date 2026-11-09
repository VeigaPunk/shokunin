# tabi — round 98 report (L1 `TabiR98`, attempt 1)

Lane `/home/vgpnk/Projects/shokunin/tabi-shokunin`, branch `master`. Base `020ce05f`; final lane hash
`b17415833feccd74fb53c7379eacdee0b2b1d05c` (`git ls-remote origin refs/heads/master` prints it).

## Work performed

Declared claims (1): **C1 — coverage, capability acquisition `client-oopif-uploadmodes-linux`** (sourced:
S240, S241, S242). Predicate `C1-CLIENT-OOPIF-UPLOADMODES-R98` (`plans/round-98.md` §Claim): on Chromium
155.0.8059.84 with puppeteer-core 25.16.0 / playwright-core 1.65.0, a file input `#s` sits inside a cross-site
(`localhost` under `127.0.0.1`) iframe. Across 3 reps × 8 arms = 24 legs:

- Path uploads give `[["tabi-r98-answer.txt",22,"text/plain"]]`, trusted `input`/`change`, and the answer
  bytes read back. Arms: Puppeteer `launch` (PUA), Playwright `chromium.launch` (PLA), `connectOverCDP`
  `isLocal` (PLL).
- Payload objects `{name, mimeType, buffer}` give `[["tabi-r98-payload.txt",29,"text/plain"]]`, **untrusted**
  `input`/`change`, and the payload bytes read back. Arms: launched (PLAB), default `connectOverCDP` (PLB),
  `isLocal` (PLLB).
- PLLM (`isLocal` with an absent path) gives `Error: ENOENT … stat '<path>'`; the input is untouched and no
  event fires.
- PUR (Puppeteer `connect` with an absent path) resolves and leaves `[["tabi-r98-missing.txt",0,"text/plain"]]`
  with trusted events. Its `Blob.text()` rejects `NotFoundError` with Blink's message.

Launch-vs-connect is declared a driver-pin fact (limit 2).

- Fresh-start read was not owed: r93-r97 were admitted (MANIFEST tabi rows). The r97 spot-check §6 was
  answered:
  - D1: appended README correction `## Correction — round 97 coverage summary (round 98; append-only)`.
  - D2: the M40/M42/M66 classes are in this round's battery (`reps-other`, `missing-exists-null`,
    `resolved-with-stale-error`), and a live-killer harness covers the M75-M77 class
    (`scripts/livekillers-client-oopif-uploadmodes-round98.mjs`, 3/3). The frozen r97 bytes are unchanged.
  - D3: carried in SCORECARD Planned.
- Sources opened by the L1 (staged `.ufo/waves/round-98/sources/`, `fetch-log.txt`):
  - Playwright `dom.ts` v1.65.0 → S240.
  - Blink `file_error.cc` @155.0.8059.84 → S241.
  - Puppeteer `ChromeLauncher.ts` v25.16.0 → S242.
  - Playwright `browser.ts` v1.65.0 → S243, after the wave (R98Critic2 §3 citation gap; note mechanism only).
  - S238 was re-opened unchanged. BrowserLauncher.ts and chromium.ts were rejected as rows (reasons in the
    lesson Gate).
- Instruments frozen at `b92b161d`:
  - driver `scripts/client-oopif-uploadmodes-round98.mjs` (`f8e95a982ac0`)
  - counter `scripts/check-client-oopif-uploadmodes-round98.mjs` (`e55581ea758f`)
  - battery `scripts/negatives-client-oopif-uploadmodes-round98.mjs` (`9475fd902375`)
  - live-killer harness (`940712bd324a`)
  - `claims.json`, frozenAt 01:20:48
- Pre-freeze controls were executed and committed in the freeze (`.ufo/waves/round-98/controls/rc.txt`):

  | control | result |
  |---|---|
  | no-work, base | rc 128 |
  | no-work, r97 receipt | rc 1 (schema, payload, leg-set, …) |
  | positive | rc 0, 253 checks |
  | battery | 87/87 |
  | live killers | 3/3 (frozen rc 1 with the target id, neutralised rc 0) |
  | wrong-library `--live` | rc 1 `libs` |
  | tampered-tree `--live` | rc 1 `libs` |
  | driver-pin | rc 1 |
  | eight setup refusals | rc 2 each; 0 chromium left |

  The first harness run hit the chromium socket-path limit and refused `setup`
  (`controls/livekillers-first-run.json`). It was fixed before the recorded run (mistake 1).
- Scored `--live` run (`172bc0a1`): rc 0, clean, 256 checks, nonce `tabi-r98-live-044424c8b981`. The receipt
  is committed at `corpus/evidence/round98/client-oopif-uploadmodes/receipt.json` (sha256 `f69c5719…`).
  Outcome classes: trustedPath 9, untrustedPayload 9, enoent 3, phantomUnreadable 3.
- Wave w1 (12 seats, `.ufo/waves/round-98/w1/`): 12 `neutral`. Every independent `--live` reproduction was
  clean:
  - R98Exec1 ×2: 256 checks each.
  - R98Exec2: default 256, `--reps 10` 816.
  - R98Reviewer: `--reps 1`, 96.
  - R98Scribe: 256.
  - R98Sentinel: 256.

  Other seat results:
  - R98Revenger protocol logs confirm the input-kind account.
  - R98Mut: 86 mutants, 10 survivors. Routed to r99; none changes what the counting command decides.
- Records: knowledge note `corpus/knowledge/client-oopif-uploadmodes-round-98.md`, README `## Round 98
  coverage`, SKILL `## Round 98 gate registry`, lesson `corpus/lessons/round-98.md`.
- Appended corrections:
  - r97 note: the isLocal trust rule is scoped to paths (R98Connector O7). The ENOENT is client-side (R98Scribe
    F2, a captured stack).
  - r77 note: the `pick-missing` row omits the trusted `input`. Verified by the L1 against the r77 receipt
    events seq 37-38.

## Landed changes

| commit | contents | LOG.md entry |
|---|---|---|
| `b92b161d` | freeze: plan, claims.json, 4 instruments, executed controls, probe, staged S240-S242 sources, census-start | LOG `## Round 98` (freeze paragraph) |
| `172bc0a1` | scored `--live` run + committed receipt | LOG `## Round 98` (scored) |
| `acd1e847` | S240-S242 + search log, r98 note, README r98 coverage + r97 D1 correction, SKILL registry, lesson gate/mistakes | LOG `## Round 98` (records) |
| `b1741583` | wave evidence + results, falsification ledger, S243 + post-wave log, note narrowing, r97/r77 note corrections, lesson wave/leads, LOG, SCORECARD r98, census-end | LOG `## Round 98` (round shape, verdicts) |

## Before → after measurements

- **C1.** Counting command:
  `node scripts/check-client-oopif-uploadmodes-round98.mjs --lane <ABS lane> --expect-driver-sha256 f8e95a982ac06dc42d6d6f0754123277183d85bc7672d341fed1d2191e092aa2 --live --deps <ABS npm install of puppeteer-core@25.16.0 playwright-core@1.65.0> --scratch <ABS> --ports <http,child,cdp> --json`
  - Before (base `020ce05f`): `git cat-file -e 020ce05f:scripts/check-client-oopif-uploadmodes-round98.mjs`
    gives rc 128. The r97 receipt under the frozen counter gives rc 1.
  - After: rc 0, `verdict: clean`, 256 checks, 0 findings. Measured at revision `b92b161d` (the master tip
    when the counter ran); shipped in `172bc0a1`.
  - Do-nothing and wrong controls do not reach the target: r97 receipt rc 1, wrong-library rc 1,
    tampered-tree rc 1. A Playwright-remote laundered driver also fails (R98Sentinel v1: rc 1,
    `child-events`).

## Sources & frontier

- Census start (`.ufo/waves/round-98/census-start.txt`): `scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin tabi` gives `tabi ok`, exit 0.
- Census end (`census-end.txt`): `tabi ok`, exit 0, with W04 warnings on older rows only.
- Rows: 239 → 243 (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`).
- Added by tier: A +4 (S240, S241, S242, S243; all `mined`, 90d, used by the r98 note).
- Rows touched old→new: none (append-only; S238 re-opened, unchanged).
- Rejected as rows: BrowserLauncher.ts and chromium.ts (reasons and flips are in the lesson Gate).
- Frontier advanced:
  - client-launched browsers
  - payload objects
  - `isLocal` with an absent path
  - file bytes and types
  - the phantom's read
- Mined mistakes (lesson `## Mistakes`):
  1. The harness path budget broke the chromium socket path. Shown to fail: long names gave rc 2, short names
     rc 0.
  2. The validator refused the `labrat` role. This was captured by the validator.
  3. `TMPDIR` was set after Playwright had loaded, so `connectOverCDP` legs wrote transient
     `/tmp/playwright-artifacts-*` (R98Sentinel). This is a §7 item-4 routed defect; the fix goes to r99 and is
     not yet shown.
- Sourced claim: C1 rests on S240, S241 and S242, all opened this round.
- Assimilation: none. considerthese: there is no `considerthese/` directory in this lane.

## Trend verdicts

- **expansion: improved.**
  - Knowledge 110 → 111.
  - SOURCES 239 → 243.
  - New capability row `client-oopif-uploadmodes-linux`.
- **quality: improved.**
  - r97 D1 was corrected append-only.
  - The r97 mechanism mis-attribution (ENOENT layer) and the r77 row omission were corrected append-only, with
    evidence.
  - The R97Mut battery-gap and live-only classes now have killers for this round's counter (battery 87/87,
    harness 3/3).
- **discernment: improved.**
  - The launch/connect blind spot was declared before freeze as a driver-pin fact.
  - R98Sentinel's laundering confirmed it (limit 2), so no falsifies-wording.
  - Two candidate rows were rejected with reasons.
  - Seat-opened sources (R98Scout) were held as leads.
  - R98Reviewer's sweep nit was refuted with R98Sentinel's sampling rather than adopted.

## Round shape

- ONE v1 wave `w1` of 12 seats: executor ×3, critic ×2, mutation-tester ×1, revenger ×1, reviewer ×1,
  sentinel ×1, scout ×1, scribe ×1, connector ×1.
- Attack share (reviewer+critic+mutation-tester) is 4/12 = 33 %.
- Dead seats: 0 (all 12 filed).
- Residual call: none. Round total: 12.
- The planner seat was held by the L1 (the validator rejects `planner`).
- Dispatch: `.ufo/waves/round-98/w1-dispatch.json` via the inline handoff (`w1.ready` at 01:21:53). Results
  are in `w1-results.json` (WAVE-DONE received).

Pre-file falsification ledger: `.ufo/waves/round-98/claim-falsification.tsv` (12 rows, all `neutral`).
`python3 scripts/hyaku/prefile-falsification.py --lane tabi --round 98` → `PREFILE-FALSIFICATION: pass claims=1 rows=12 attack_seats=7 findings=0`, exit 0.

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only orchestrator-owned
`.scratch/` entries and no file written by this round's seats.

Tool installs:
- npm `puppeteer-core@25.16.0` + `playwright-core@1.65.0`, and `puppeteer-core@25.15.0` for the
  wrong-library control.
- Installed into `/fast/scratch/hyaku/tabi-r98/` from the npm registry. Seats installed the same pair into
  their own scratch.
- No pacman. Scratch was removed after landing.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Open L0 questions: none.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` `## Round 98 gate registry`; no non-author verifier named this round
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 98` (scored `--live` run, `.ufo/waves/round-98/scored/c1-live.json`)
- [~] Instructions executable by an agent without oral context — the counting command was reproduced cold from the plan text by lane-dispatched seats R98Exec1/R98Exec2 (`.ufo/waves/round-98/w1/R98Exec1.md`, `R98Exec2.md`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; R98Connector found no sibling overlap (`.ufo/waves/round-98/w1/R98Connector.md` §2-3)
