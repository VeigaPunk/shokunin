# tabi — round 99 report (L1 `TabiR99`, attempt 1)

Lane `/home/vgpnk/Projects/shokunin/tabi-shokunin`, branch `master`. Base `9eaa5cbe`. Final lane hash
`63b9c9a7527cd2c3c0ba9a60a6eff19e3abe4ad3`; `git ls-remote origin refs/heads/master` prints it.

## Work performed

Declared claims (1): **C1, coverage, capability acquisition `client-oopif-uploadsets-linux`**. It is sourced
from four new rows (S244, S245, S246, S247) and three rows re-opened this round (S237, S238, S240).

Predicate `C1-CLIENT-OOPIF-UPLOADSETS-R99` is in `plans/round-99.md` §Claim. The setup:
- Chromium 155.0.8059.84, puppeteer-core 25.16.0, playwright-core 1.65.0.
- A cross-site (`localhost`) child frame holds two file inputs: `#s` without `multiple` and `#m` with it.
- 8 arms × 3 reps = 24 legs. Each leg reads both inputs and every landed file twice, through `arrayBuffer()`
  and through `FileReader`, each with a sha256.

What the legs show:
- **PUAM** (Puppeteer `launch`, absent path): the call resolves. It leaves a trusted 0-byte phantom file, and
  both read APIs reject it with `NotFoundError`.
- **PLAM** (Playwright `chromium.launch`, absent path): `Error: ENOENT … stat`. Nothing is set.
- **PLBX** (one untyped 256-byte payload named `.png`): the file lands as `image/png`. Its events are
  untrusted. The bytes are intact.
- **PLBM** (one typed payload and one untyped `.tabi99` payload on `#m`): the files land in order as
  `text/plain` and `application/octet-stream`. Events are untrusted. Bytes are intact.
- **PLBN** (the same two payloads on `#s`): `Error` "…Non-multiple file input can only accept single file".
  Nothing is set and no event fires.
- **PLLP** (Playwright `isLocal`) and **PUCM** (Puppeteer `connect`), two paths on `#m`: the files land in
  order. Events are trusted. Bytes are intact.
- **PUCN** (two paths on `#s`): `Error` "Multiple file uploads only work with <input type=file multiple>".
  Nothing is set.

Work items:
- **Fresh-start read: not owed.** r93-r98 were admitted (MANIFEST tabi rows).
- **r98 spot-check §6, D1-D4** (`corpus/lessons/round-98-verifier-spotcheck.md`), all answered:
  - D1: an appended README correction, `## Correction — round 97 coverage summary, isLocal scope (round 99;
    append-only)`.
  - D2: the driver now sets `TMPDIR` before it loads the clients. The strace control shows the fix working:
    the r98 driver made 4 `/tmp/playwright-artifacts-*` dirs, the r99 driver made 0 under `/tmp` and 5
    under its scratch (`.ufo/waves/round-99/controls/rc.txt`).
  - D3: on driver exit 3 the counter still checks the receipt (limit 8). Live killer K-partial gives the
    frozen counter rc 1 and the r98 mapping rc 2; K-launchonly gives rc 2.
  - D4: the R98Mut survivor classes are now battery cases.
- **Sources** were opened by the L1 and staged in `.ufo/waves/round-99/sources/` (`fetch-log.txt`). See
  §Sources & frontier.
- **Instruments frozen at `27685238`**:

  | instrument | file | sha256 prefix |
  |---|---|---|
  | driver | `scripts/client-oopif-uploadsets-round99.mjs` | `98efdc1293cc` |
  | counter | `scripts/check-client-oopif-uploadsets-round99.mjs` | `1a0f25293771` |
  | battery | `scripts/negatives-client-oopif-uploadsets-round99.mjs` | `854f4fef8418` |
  | live-killer harness | `scripts/livekillers-client-oopif-uploadsets-round99.mjs` | `03aae02849b2` |

  `claims.json` was stamped `frozenAt` 02:11:46.
- **Pre-freeze controls** were executed and committed in the freeze commit (`.ufo/waves/round-99/controls/rc.txt`):

  | control | result |
  |---|---|
  | no-work: counter absent at base | rc 128 |
  | no-work: r98 receipt under the r99 counter | rc 1 |
  | positive run | rc 0, 278 checks |
  | battery | 109/109 |
  | live killers | 6/6 |
  | wrong library, `--live` | rc 1 `libs` |
  | tampered tree, `--live` | rc 1 `libs` |
  | driver pin mismatch | rc 1 |
  | eight setup refusals | rc 2 each |
  | chromium left after the controls | 0 |
  | strace (D2) | r98 driver 4 under `/tmp`, r99 driver 0 |

- **Scored `--live` run** (`ff978cb4`): rc 0, verdict clean, 282 checks, nonce `tabi-r99-live-6d2a1508cbc1`.
  - Committed receipt: `corpus/evidence/round99/client-oopif-uploadsets/receipt.json` (sha256 `ed4b2129…`).
  - Outcome classes: trustedMulti 6, untrustedPayload 6, refusedMultiple 6, enoent 3, phantomUnreadable 3.
- **Wave w1** (12 seats, `.ufo/waves/round-99/w1/`): 11 seats returned `neutral` and 1 returned
  `falsifies-wording`.
  - R99Critic1 found two wording faults:
    - W1: the plan's "Surface moved" sentence says no lane instrument ever put two files into one input or
      read an upload with `arrayBuffer()`. That is false: the r77/r78 raw-chooser instruments did both.
    - W2: limit 8's first clause is wider than the code for the case where every leg fails to launch.
  - Both faults were narrowed by **plan §Amendment A1**, which is also recorded in `claims.json`
    `frozenAmendments`. The predicate, counter, kill rule and target are unchanged.
  - R99Connector H1 reported the same item as W1.
- **Independent reproductions**:
  - R99Exec1: two cold runs, clean at 282 checks each.
  - R99Exec2: `--reps 10` clean at 898 checks, and the live killers 6/6.
  - R99Sentinel: a strace run that was clean and wrote nothing under `/tmp` or `/var/tmp`.
- **Mechanism checks**:
  - R99Critic2 re-fetched every cited source and confirmed each cited line.
  - R99Revenger's protocol logs show the refused arms send no `DOM.setFileInputFiles` and run no injected
    `setInputFiles`.
- **R99Mut**: 98 mutants, 68 killed, 30 survived. No survivor appears in the scored receipt; the gaps are
  routed to r100.
- **Records**:
  - knowledge note `corpus/knowledge/client-oopif-uploadsets-round-99.md`, plus its appended relation/scope
    correction;
  - README `## Round 99 coverage`;
  - SKILL `## Round 99 gate registry`;
  - lesson `corpus/lessons/round-99.md`;
  - an appended r77 note correction (R99Connector H2: the "first path" practice bullet holds over raw CDP
    only).

## Landed changes

| commit | contents | LOG.md entry |
|---|---|---|
| `27685238` | freeze: plan, claims.json, 4 instruments, executed controls (incl. D2 strace, D3 killers), probe, staged sources, census-start | LOG `## Round 99` (freeze paragraph) |
| `ff978cb4` | scored `--live` run + committed receipt | LOG `## Round 99` (scored) |
| `75a8a6f7` | S244-S247 + search log, r99 note, README r99 coverage + r98 D1 correction, SKILL registry, lesson gate/mistakes | LOG `## Round 99` (records) |
| `2259688a` | wave evidence + results, falsification ledger, Amendment A1, r77/r99 note corrections, lesson wave/mistakes/leads, LOG, SCORECARD r99, census-end | LOG `## Round 99` (round shape, verdicts) |
| `63b9c9a7` | falsification ledger: narrowing pointer set to `plans/round-99.md` so the prefile gate resolves it | LOG `## Round 99` (round shape, verdicts) |

## Before → after measurements

- **C1.** Counting command:
  `node scripts/check-client-oopif-uploadsets-round99.mjs --lane <ABS lane> --expect-driver-sha256 98efdc1293cc729b04a3774dfc45caf75bf20acf0d657f962a93b3eaba6b89f8 --live --deps <ABS npm install of puppeteer-core@25.16.0 playwright-core@1.65.0> --scratch <ABS> --ports <http,child,cdp> --json`
  - Before (base `9eaa5cbe`): `git cat-file -e 9eaa5cbe:scripts/check-client-oopif-uploadsets-round99.mjs`
    returns rc 128. The r98 receipt under the frozen counter returns rc 1 (schema, files, payloads, leg-set, …).
  - After: rc 0, `verdict: clean`, 282 checks, 0 findings. Measured at revision `27685238` (the master tip when
    the counter ran) and shipped in `ff978cb4`.
  - Neither the do-nothing controls nor the wrong-input controls reach the target: r98 receipt rc 1,
    wrong-library rc 1, tampered-tree rc 1, driver-pin rc 1.

## Sources & frontier

- Census start (`.ufo/waves/round-99/census-start.txt`):
  `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi` returned `tabi ok`, exit 0.
- Census end (`census-end.txt`): `tabi ok`, exit 0. The only warnings are W04 on older rows (S222, S223).
- Rows: 243 → 247 (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`).
- Added, all tier A, all `mined`, 90d, used by the r99 note:

  | row | source |
  |---|---|
  | S244 | Puppeteer `util/assert.ts` |
  | S245 | W3C File API |
  | S246 | mime 4.1.0 `types/standard.ts` |
  | S247 | mime 4.1.0 `src/Mime.ts` |

- Rows touched old→new: none. S237, S238 and S240 were re-opened byte-identical and are unchanged.
- Rejected as rows:
  - Playwright root `package.json`: it only pins the mime version, and S246's anchor cites it.
  - `bundles/utils/package.json`: HTTP 404.
  - Reasons and flip conditions are in the lesson Gate.
- Frontier advanced:
  - multi-file sets
  - the `multiple` refusal in both clients
  - untyped payload name → type
  - binary bytes under two read APIs
  - absent path on client-launched browsers
- Mined mistakes (lesson `## Mistakes`):
  1. TMPDIR was set after the module that reads it (r98 mistake 3). Fixed; the strace control shows the fix
     working (4 → 0).
  2. The exit-3 refusal masked findings (r98 D3). Fixed; K-partial shows the fix working.
  3. Source ids were assigned before the registry was read. Caught pre-freeze; recorded as a practice.
  4. A universal negative rested on a narrower grep (R99Critic1 W1). Narrowed by A1. The whole-`scripts/`
     grep finds 2 hits, so the check can fail.
  5. Limit 8's first clause was wider than its branch (W2). Narrowed by A1.
- Sourced claim: C1 rests on S244-S247, all opened this round, plus the re-opened S237, S238 and S240.
- Assimilation: none. considerthese: this lane has no `considerthese/` directory.

## Trend verdicts

- **expansion: improved.**
  - Knowledge notes went from 111 to 112.
  - SOURCES went from 243 to 247 rows.
  - New capability row `client-oopif-uploadsets-linux`.
- **quality: improved.**
  - r98 D1 was corrected append-only.
  - D2 and D3 were fixed, and controls show each fix working.
  - D4's survivor classes are now killed by this round's battery.
  - The r77 note's "first path" practice bullet was scoped append-only.
  - No admitted entry failed its re-check (R99Critic2 confirmed every row).
- **discernment: unprovable-but-better.**
  - The wave's adversarial seats found two over-wide sentences in the frozen text (R99Critic1 W1/W2), and the
    L1 narrowed them under §8 choice (i) before filing rather than filing the wider wording.
  - Two candidate rows were rejected with reasons.
  - Seat-opened sources (R99Scout) were held as leads, not rows.
  - The R99Sentinel hardening diffs were not folded into the frozen bytes; they are routed to r100.
  - The over-wide sentence was the L1's own, so this is not counted as `improved`. A non-author closure
    must judge it.

## Round shape

- ONE v1 wave `w1` of 12 seats: executor ×3, critic ×2, mutation-tester ×1, revenger ×1, reviewer ×1,
  sentinel ×1, scout ×1, scribe ×1, connector ×1.
- Attack share: 4/12 = 33 %.
- Dead seats: 0.
- Residual call: none. Round total: 12.
- The L1 held the planner seat.
- Dispatch went through the inline handoff (`w1.ready` at 02:12:45, spawned 02:12:59). WAVE-DONE was received
  and the results are in `w1-results.json`.

Pre-file falsification ledger: `.ufo/waves/round-99/claim-falsification.tsv` (12 rows: 11 `neutral`, 1
`falsifies-wording` narrowed by Amendment A1). `python3 scripts/hyaku/prefile-falsification.py --lane tabi
--round 99` → `PREFILE-FALSIFICATION: pass claims=1 rows=12 attack_seats=7 findings=0`, exit 0. The first
gate run failed with `narrowing-unresolved` because the pointer carried a `#anchor`; it was fixed in
`63b9c9a7`.

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed no entries outside the
orchestrator-owned `.scratch/`.

Tool installs:
- npm `puppeteer-core@25.16.0` + `playwright-core@1.65.0`, plus `puppeteer-core@25.15.0` for the
  wrong-library control.
- Channel: the npm registry, into `/fast/scratch/hyaku/tabi-r99/`. Seats installed the same pair into their
  own scratch.
- `strace` was already present. No pacman.
- Scratch was removed after landing.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Open L0 questions: none.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` `## Round 99 gate registry`; no non-author verifier named this round
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 99` (scored `--live` run, `.ufo/waves/round-99/scored/c1-live.json`)
- [~] Instructions executable by an agent without oral context — the counting command was reproduced cold from the plan text by lane-dispatched seats R99Exec1/R99Exec2 (`.ufo/waves/round-99/w1/R99Exec1.md`, `R99Exec2.md`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; R99Connector found no sibling overlap (`.ufo/waves/round-99/w1/R99Connector.md`)
