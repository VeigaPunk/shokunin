# tabi — round 70 report (attempt 1)

Lane HEAD (pushed): `b12a93cf0bb294b46739274b859fed6315a9b844` (`git ls-remote origin refs/heads/master` prints it). Base `90b9ff045542651fb59814fe32f73fee0d1d8243`. Round 69 was admitted (MANIFEST `rounds[1423]`), so no fresh-start obligation applied.

## Work performed

Declared claims (2), frozen at `7c42ef25` (`.ufo/waves/round-70/claims.json`). The pre-freeze instruments and executed controls landed first at `b5d77c4c`, and the digests at `2cde310f` (`.ufo/waves/round-70/freeze.txt`). All six axes started at 9, so both claims work a lowest axis.

- **C1 — coverage, capability acquisition `chromium-synth-tap-gesture-linux`.** Sourced: S175 was opened this round; S174 and S173 are also cited. Predicate `C1-SYNTHTAP-LIVE` (a)–(d).
- **C2 — operability.** `scripts/verify-live-r70.mjs --profile synthscroll-r69` is a live re-derivation of the r69 capability `chromium-synth-scroll-gesture-linux`. Before this round, that capability could only be checked by a counter that reads a receipt (r69 closure, routed defect R1). Predicate `C2-LIVE-R69` (a)–(c).

Work items:

- **Inputs read before declaring.** Round-69 spot-check `corpus/lessons/round-69-verifier-spotcheck.md`. Its routed defects R1–R6 are handled one by one in `corpus/lessons/round-70.md` § Round-69 routed defects.
- **New instruments** (`b5d77c4c`):
  - driver `scripts/chrome-cdp-synthtap-round70.mjs`, an 8-leg tap journey on a loopback button
  - counter `scripts/check-synthtap-r70.mjs`, 84 named checks; it re-derives every leg from raw events plus the CDP send log and refuses look-alike producers
  - battery `scripts/negatives-synthtap-r70.mjs`, one negative per declared check id plus 3 laundered degenerates; it fails on `coverage-gap`
  - live verifier `scripts/verify-live-r70.mjs`, with two profiles, verifier-drawn nonces and ports, run binding, the frozen-digest counter, and cross-run and evidence fingerprints
- **Pre-freeze executed controls: 31/31 hold** (`.ufo/waves/round-70/controls/summary.json`; evaluator `controls/evaluate-controls.mjs` checks the exit code AND the expected finding ids).
  - C1 do-nothing: counter exit 2; live verifier exit 1 `evidence-counter`.
  - Degenerate drivers `js-click`, `dispatch-mouse`, `skip-touch`: exit 1.
  - Battery on smoke1: 95/95.
  - C2 do-nothing: at base, exit 1 `MODULE_NOT_FOUND`.
  - Forgers: replay and rewrite exit 1 with run-binding findings; lying full-rewrite exit 1 `driverDigest`; honest full-rewrite exit 1 `counter`; override copy exit 4; tampered driver exit 2; `scratch-too-long` exit 2; positive exit 0.
  - Discriminating control: the r69 counter alone **accepts** the rewritten replay (`controls/c2/r69-counter-accepts-rewrite` exit 0), while the verifier refuses it.
- **C1 scored run (a), after the freeze** (`6444c12c`). Receipt `corpus/evidence/round70/chromium-synth-tap-gesture/receipt.json`, sha256 `0a51f3a6c97280d4bb5d854e0d0ed9d43726f340b46fb840313559b0bf86d631`, nonce `tabi-r70-scored-8a468fd6`. Counter clean on 84 checks (`scored/c1-counter-a.json`); battery 95/95 with coverage gap 0 (`scored/c1-negatives-a.json`).
- **Live verifier, L1 runs** (`0ff5134e`): synthtap-r70 exit 0 and synthscroll-r69 exit 0. Both report predicate true and pins frozen, with cross-run and evidence agreement true (`scored/c{1,2}-verify-live-L1.json`).
- **Knowledge note** `corpus/knowledge/chromium-synth-tap-gesture-runtime-round-70.md` (cites S175, S174, S173). Measured on this host:
  - The default 50 ms hold is real time.
  - `tapCount:2` gives two `detail:1` clicks and no `dblclick` with a plain mouse source. This contradicts Input.pdl:326.
  - An omitted source becomes touch (S175:22-26), even though the PDL says "platform default".
  - A synthetic touch tap delivers no click.
  - `tapCount:0` returns success and produces no input.
  - `-32602` is returned for out-of-bounds coordinates and for `pen`.
  - Chromium's singleton-socket limit can make both drivers hang for 240 s.
  - The R70Exec3 and R70Exec4 findings are integrated as scope limits.
- **SKILL.md `## Round 70 gate registry`** plus `scripts/selftest-r70-gates.mjs --selftest`: exit 0 over 7 cases (`scored/selftest-r70-gates.out`). `check-gate-registry --rev bbdbf62f` shows both r70 gates conformant; the 5 pre-existing missing rows remain (R6, untouched).
- **QUALITY 131** (control evaluation must check exit AND finding ids) and **QUALITY 132** (battery coverage rule).
- **Wave w1:** 12 seats, all settled, evidence in `.ufo/waves/round-70/w1/` (`b12a93cf`).

## Landed changes

| Commit | Content | LOG.md entry |
|---|---|---|
| `b5d77c4ca628c08954c6ffea0e82dcaf06e54de9` | pre-freeze instruments (driver, counter, battery, verify-live-r70), executed controls 31/31 + evaluator + forger, S175 staged bytes, census start | `## Round 70` bullet 1 |
| `7c42ef25e63751d54f36ab213d06162997476219` | freeze `claims.json` | bullet 1 |
| `2cde310fa74b428c5c0e8e7324bce339e921a052` | `freeze.txt` (instrument and claims digests) | bullet 1 |
| `6444c12cc19a3504e1095f6007925dd6f5bf48aa` | C1 scored receipt, counter and battery outputs | bullet 2 |
| `0ff5134e42b985b494274383a009a38873e6db63` | L1 live verifier runs for both profiles | bullets 2–3 |
| `63dcf7c2bba1e8ba07d0d175400bc3aaaec5915c` | knowledge note, S175 row with S173/S174 used-by, lesson, QUALITY 131–132, README, SKILL registry, selftest, wave spec/dispatch/ready | bullets 2, 5 |
| `bbdbf62fb84bce7a51a248038ba4047d43076518` | registry row spelling fix (verdict map/scope) | bullet 2 |
| `b12a93cf0bb294b46739274b859fed6315a9b844` | SCORECARD round-70 block + capability row, LOG, lesson attack findings, note scope limits, wave w1 evidence (12 seats), census end | bullets 4–6 |

## Before → after measurements

| Claim | Counting command | Measured against | Before → after |
|---|---|---|---|
| C1 coverage capability | `node scripts/check-synthtap-r70.mjs --receipt corpus/evidence/round70/chromium-synth-tap-gesture/receipt.json --expect-driver-sha256 704efab816e9bd9cc38cb31dd219aa776f7be52815a17cf1ea68924b6dff9577 --json`; live `node scripts/verify-live-r70.mjs --profile synthtap-r70 --scratch <short ABS> --json` | before `90b9ff04`; after receipt at `6444c12c`, SCORECARD row at `b12a93cf` (re-run at `b12a93cf`: `clean findings=0`, rc 0) | counter exit 2 (no receipt), live exit 1 `evidence-counter` → (a) counter exit 0, 84 clean; (b) live exit 0 by L1 and by R70Exec1; (c) battery 95/95, gap 0; (d) capability row + note citing S175 |
| C2 operability | `node scripts/verify-live-r70.mjs --profile synthscroll-r69 --scratch <short ABS> --json` | before `90b9ff04`; after `b5d77c4c` (verifier bytes 99442a2c…76b8 unchanged to `b12a93cf`) | exit 1 `MODULE_NOT_FOUND` → exit 0 predicate true by L1 (`scored/c2-verify-live-L1.json`) and by R70Exec2 (`w1/R70Exec2/verify.json`); controls 31/31 hold |

**Author's verdicts (closure pending): both predicates met as frozen. Attack findings are disclosed below; the instruments stay pinned.**

- **C1 — R70Critic: FALSIFIED as an execution oracle.** The real verifier exits 0 with pins frozen and no live run in two cases:
  - Attack A: an inherited `NODE_OPTIONS` preload rewrites the driver's receipt (`w1/R70Critic/receipts/c1-env-verifier.json`).
  - Attack B: a same-user driver swap between the pin read at `verify-live-r70.mjs:122` and the spawn at `:158` (`c1-toctou-verifier.json`, runs of 24–26 ms).

  As a result, the claim's own limit sentence is wrong ("passes only if … that binary is the frozen driver"). Other attack results:
  - R70Review1: 16 receipt-form false greens (FG1–FG16) plus one battery gap (FB1).
  - R70Mut1: 21 of 31 counter mutants survive the battery.

  The physical capability itself is corroborated by the scored run, R70Exec1's independent verifier/driver/counter runs, R70Critic's clean run and R70Exec3's 48 variant runs.
- **C2 — R70Critic: HOLDS-WITH-LIMIT.** The same preload/swap bypass applies, and the evidence leg binds the bytes at a path, not their provenance (R70Review2 F1). R70Mut2 killed 15 of 17 verifier mutants (1 equivalent, 1 verdict-redundant).

Both repairs are planned for r71 (SCORECARD round-70 `Planned`).

## Sources & frontier

- **Census command** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`:
  - start: exit 0, 174 rows (`.ufo/waves/round-70/census/start.txt`)
  - end: exit 0, 175 rows (`.ufo/waves/round-70/census/end.txt`; W04 cross-scope warnings only)
  - Row count: `grep -c '^| S[0-9]' corpus/SOURCES.md` 174 → 175.
- **Rows added:** 1, tier A — **S175**, Chromium 155.0.8059.84 `content/common/input/synthetic_tap_gesture.cc`, kind `code`, status `mined`. Staged sha256 `ac27658f…d331`. R70Scout re-opened it independently and got identical bytes (`w1/R70Scout/receipt-s175-fetch.json`).
- **Rows touched (old → new):** S173 and S174 used-by gain `corpus/knowledge/chromium-synth-tap-gesture-runtime-round-70.md`. Logged in the lesson `## Gate`.
- **Frontier advanced:**
  - `Input.synthesizeTapGesture` runtime delivery moved from unheld to core (capability row).
  - Touch-tap behaviour is now measured across emulation variants; its cause stays frontier.
- **Sourced claim:** C1 rests on S175 (opened 2026-11-06).
- **Mistakes mined** (`corpus/lessons/round-70.md` `## Mistakes`):
  1. Refusals for the wrong reason were counted as passing controls (a Chromium launch failure from the socket path). Shown able to fail: `lesson-proof/evaluator-wrong-reason-summary.json`. Became QUALITY 131.
  2. Evidence was judged with the override pin.
  3. A battery coverage rule was missing. Became QUALITY 132.
  4. The claim's limit sentence overclaimed. Not fixed; routed.
- **Assimilation:** none. `merge/tabi/` adoption stays closed (L0 `tabi | round-57`). `considerthese/`: this lane has no such directory.

## Trend verdicts

- **expansion: improved.** Knowledge 82 → 83, on ground the lane did not hold (tap delivery). Registry 174 → 175. New capability row `chromium-synth-tap-gesture-linux`. A live re-derivation command now exists for the r69 capability.
- **quality: improved.**
  - The r69 capability is re-verified live on today's host, with fingerprints equal to the committed receipt (C2, L1 + R70Exec2).
  - The knowledge note is corrected in-round against R70Exec3/R70Exec4: scope limits on item 2, plus new item 5.
  - QUALITY 131–132 added.
- **discernment: improved.** Three PDL statements were rejected against runtime and source (lesson Gate). The round records its own attack seats' refutation of the C1 limit sentence and of the counter's strength instead of claiming more. Outside agreement is still owed.

## Round shape and seats

- **Shape:** ONE v1 wave `w1` (policy band 8–16): 12 seats.
- **Roles:** scout 1, connector 1, executor 4, scribe 1, reviewer 2, critic 1, mutation-tester 2. Attack seats: 5/12 (42 %).
- **Planner:** the L1 holds the planner seat, because the validator refuses `planner`.
- **Dispatch:** inline spawn handoff (`w1.ready` → `w1.ready.dispatched`); WAVE-DONE received from the orchestrator. All 12 seats settled, 0 dead (`.ufo/waves/round-70/w1-results.json`).
- No residual call. **Round total 12.**
- The scribe's draft was cross-checked; its battery-row patch was not adopted.

## Other

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/run15-state.json` and `.scratch/run15-wrapup/misroot-cff0b4cb/`. Both are orchestrator-owned and not tabi's; no tabi seat misroots.
- **Scratch:** `/fast/scratch/hyaku/tabi-r70` removed.
- **Host incident (lane-local, no host change):** a long scratch path made Chromium exit FATAL "Socket path too long", and the drivers then hung for 240 s. Recorded in the note and the lesson; the verifier now refuses such paths before launch.
- **Tool installs:** none (no seat reported one).
- **L0:** appended `tabi | round-70 | …`, asking whether same-user environment/TOCTOU tampering is in scope for live-verifier admission. Earlier tabi L0s (including r69 kotoba, the adjacency rulings and the r57 register) remain open and are routed around.
- **Open routed items:** R70Connector reports kama `none → adjacent` and 9 of 20 sibling heads moved since the r69 snapshot (not absorbed). R4: `w1-results.json` per-seat status is orchestrator-written, and its rows carry no `status` field.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` `## Round 70 gate registry`; knowledge note items 1–7 tied to S175/S174/S173 lines. Lane-authored, not verified by a non-author.
- [~] At least one end-to-end domain task executed and logged in LOG.md — live `Input.synthesizeTapGesture` journey on Chromium 155 (`corpus/evidence/round70/chromium-synth-tap-gesture/receipt.json`; independent run `.ufo/waves/round-70/w1/R70Exec1/`); `LOG.md` `## Round 70`.
- [~] Instructions executable by an agent without oral context — R70Exec1 and R70Exec2 ran the note's `recheck:` command (`verify-live-r70.mjs`) cold and got exit 0. These are lane-dispatched seats, not non-authors.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — R70Connector found no sibling holding the tap surface; the kama/kotoba matrix changes are reported in the lesson, not absorbed. `PROVINCE.md` is unchanged this round.
