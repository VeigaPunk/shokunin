# kagi — round 57 report (attempt 1)

Lane: `kagi-shokunin` (secrets & vault ops). Claim BASE `1cda9e7ae4767b4133e283bfbc08266d4c86362d`
(the round-56 verifier spot-check tip). Lane tip at report time: `ee1a7457b9a52c585cb1a1114a87aa12599e876d`; the claim readings were taken at `94d72de9e8ca17b7d4756dbde2a4a095b3fefbfb`, and the tip adds only the receipt/capture files cited below (the measured surfaces are byte-identical).
Round shape: one v1 wave, 12 seats (run-15 band 8–16), plus no residual call; residual work stayed
inside the wave.

## Work performed

The round declares two claims: **C1 calibration** — the previous round's numeric self-descriptions
agree with their machine authorities (`C1_CURRENT` 3 → 0) — and **C2 operability (capability
acquisition)** — an OpenBao audit-device custody trial (`C2_AUDIT_TRIAL` 0 → 5, sourced to S115/S116/S117
opened this round).

- **C1 instrument and repair.** Frozen checker `plans/round-57-c1-check.py` and counter
  `plans/round-57-c1.sh` (predeclaration `7aa1f472`); landed gate `corpus/current-claims.py`
  (`--selftest` 13 cases, sha256 `e36472b3…` in `.ufo/waves/round-57/final/landing-receipt.txt`).
  Three stale statements repaired (self-test cases 18 → 20 in `SCORECARD.md`; LOG heading
  "four freeze epochs" → six; round-56 lesson "Three freeze epochs" → Six) plus two epoch-reference
  repairs (capability row → epoch F / 23 MATCH; round-56 note → epoch F). Evidence:
  `.ufo/waves/round-57/final/c1-at-tip.txt` (`value=0 population=16 gate=1 challenge=1`).
- **C1 guards after attack.** Reviewer `R57ReviewC1` demonstrated two false-greens against the first
  guard (delete-the-evidence at population 13, and a printer gate). Freeze epoch C (`8d8e0588`) pins
  the exact census (`population=16 cases=3 match=7 epochs=2 clocks=2 pop=2`), the gate's bytes
  (`GATE_SHA256_PIN`), and a forged-tree challenge (SCORECARD `20 cases` → 19 must read value+1), and
  makes the counter exit 1 unless `value=0`. New controls K1-F8 (deleted statements → FAIL) and K1-F9
  (printer gate → FAIL) pass: `.ufo/waves/round-57/controls/controls-prefreeze-epochC.txt`
  (`CONTROLS: match=13 mismatch=0`).
- **C2 trial.** `corpus/openbao-audit-trial.sh` (measured bytes sha256 `7e645194…`, 10922 B) executes
  T1 enable path (documented `bao audit enable` refused on a default server; accepted with
  `unsafe_allow_api_audit_creation = true`), T2 salted-HMAC value form with request/response echo and
  no plaintext, T3 `log_raw` value and client-token cleartext in the raw device only, T4 disable +
  re-enable salt rotation, T5 non-audited `sys/seal-status`. Counter `plans/round-57-c2.sh` runs the
  trial twice, five in-trial shims, a no-`bao` SETUP leg, a PATH-wrapper leg and a secret-shape sweep.
  Evidence: `.ufo/waves/round-57/final/c2-at-tip.txt`
  (`value=5 tests=5 shims=5 vectors=5/5 real=1 none=1 wrap=1 secret=1`, rc 0).
- **Independent, non-author domain evidence.** `R57Labrat` re-measured the mechanics with a curl-level
  probe (default-refusal, flag route, salt rotation, token leak counts) and its report is cited in the
  entry; `R57ExecTrial` re-ran the landed trial's nine counter legs independently (real/real2 HHHHH,
  none rc2, SH1–SH5 designated vectors, wrap BHHHH); `R57ScoutSources` opened the three pages and
  caught the `hmac-sha256:` attribution gap that produced S117; `R57ScribeEntry`/`R57ScribeLesson`
  drafted the entry/lesson; `R57MutChecker` mutation-tested the checker (5/10 killed, survivors named);
  `R57CriticC2` found the ceiling misdescription and the A1-grammar mock gap; `R57Sentinel` found the
  trial's argv leak (fixed) and the epoch drift; `R57Connector` swept the sibling lanes.
- **Frontier step (§2b).** `SOURCES.md` curated (3 rows added, 0 touched), one mistake class mined, one
  sourced claim (C2 rests on S115/S116/S117 opened this round).
- **Wave shape.** `.ufo/waves/round-57/w1-spec.json` / `w1-dispatch.json`: 12 seats — 2 scout, 2 executor,
  2 scribe, 1 reviewer, 1 critic, 1 mutation-tester, 1 sentinel, 1 reviewer-probe, 1 connector; attack
  share 5/12. All 12 seats settled (`.ufo/waves/round-57/w1-results.json`: 12 results) and all 12 seat reports are under `.ufo/waves/round-57/w1/`; no seat died in the wave; the L1
  held the planner seat (bounded data-walks rode the two scouts).
- **Inherited state.** None: no `lane-dead-no-report kagi round=57` line exists before this attempt; no
  uncommitted round-57 leftovers were inherited.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows orchestrator-owned
  `.scratch/*`, a sibling lane's report, and two contentless strays (`f.txt`, `trail-ids.txt`) that name
  no lane/round; no kagi seat file landed at the fleet root. Nothing copied, nothing deleted.

## Landed changes

| Commit | Content |
|---|---|
| `7aa1f472` | predeclaration: plan, checker, C1/C2 counters, controls, wave spec/dispatch, claims-declared rows |
| `03cbf656` | freeze epoch B: C2 counter adopts the lane trial convention (A1) and the measured default-refusal/flag enable path (A2); plan predicate and 11-control battery re-run |
| `8d8e0588` | freeze epoch C: C1 guard pins the census, gate bytes and forged-tree challenge (A3); counter exit encodes the reading; round-56 lesson repair committed (missed by the landing path list) |
| `d857f344` | landing: `corpus/current-claims.py`, three statement repairs + two epoch-reference repairs, `corpus/openbao-audit-trial.sh`, audit entry, S115/S116, capability and coverage rows, ledger `R57-01`, SCORECARD/LOG/lesson/stamps |
| `94d72de9` | final receipts: epoch-C candidate readings, gate battery vs BASE, shape-keyed ceiling demonstration, S117, ceiling/T2 text corrections |

Every change is tied to the round's `LOG.md` entry (2026-11-07, "Round 57 …") and to the commits above;
`SCORECARD.md` carries the pre/post sections and the capability row, `corpus/lessons/round-57.md` the
Gate/Mistakes/Sources/Adjacency record.

## Before → after measurements

**C1 — calibration.** Counting command: `bash plans/round-57-c1.sh <rev>` (extracts the revision, runs
the frozen checker over the audited round-56 surface).
- BASE `1cda9e7` → `C1_CURRENT: value=3 population=16 gate=0 guard=1` (the three stale self-descriptions).
- Tip `94d72de9` (same bytes at `ee1a7457`) → `C1_CURRENT: value=0 population=16 gate=1 challenge=1 guard=1` (rc 0), receipt
  `.ufo/waves/round-57/final/c1-at-tip.txt`.
- Controls (epoch C): `CONTROLS: match=13 mismatch=0`, `.ufo/waves/round-57/controls/controls-prefreeze-epochC.txt`.

**C2 — operability.** Counting command: `bash plans/round-57-c2.sh <rev>`.
- BASE `1cda9e7` → `C2_AUDIT_TRIAL: value=0 tests=0 pass=0 shims=0 guard=0 (absent)` (the trial does not exist).
- Tip `94d72de9` (same bytes at `ee1a7457`) → `C2_AUDIT_TRIAL: value=5 tests=5 pass=5 shims=5 vectors=5/5 guard=1
  (real=1 none=1 wrap=1 secret=1)` (rc 0), receipt `.ufo/waves/round-57/final/c2-at-tip.txt`.
- Named ceiling, demonstrated: a zero-mechanics mock that shape-keys the shim vectors and introspects the
  PATH wrapper also reads `value=5` (`.ufo/waves/round-57/final/ceiling-mock-receipt.txt`), so the counter
  is necessary, not sufficient; the live mechanics and the non-author probe are the check.

No-work controls: C1 BASE reads 3 against target 0; C2 BASE reads 0 against target 5. Neither target is
reachable by doing nothing.

## Sources & frontier

Census command, run at round start and round end:

    scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi

- start: `kagi ok` rc 0, 114 registry rows (`.ufo/waves/round-57/controls/census-start.txt`)
- end: `kagi ok` rc 0, 117 registry rows (`final/gates.txt`, `rows=117`)

Rows added by tier: **3 × tier A** — S115 `openbao.org/docs/audit/` (41787 B, sha256 `76339ff7…`),
S116 `openbao.org/docs/commands/audit/` (33338 B, sha256 `3dc88732…`), S117
`openbao.org/docs/api/system/audit-hash/` (35071 B, sha256 `bca1461e…`), all opened 2026-11-07, status
`mined`, `recheck on-release` bound to the S090 OpenBao releases feed, used by the entry and the lesson.
Rows touched old→new: **none** (no in-place `status`/`recheck`/`used-by` change). Rejections: the
`api-docs/system/audit/` stub (no mechanism text) and the SIGHUP route as a T4 test (recorded with flip
conditions in the lesson Gate). Frontier rows advanced: none in the declared "Observable release clocks"
frontier; the audit-device ground moved from unheld coverage to core (`PROVINCE.md` §Core, round 57).
Assimilation: **none** this round (no `merge/kagi/` theme taken; `considerthese/2026-10-26.md` screened,
its fitting proposal is already C1).

Mistakes mined into `corpus/lessons/round-57.md` `## Mistakes`: M57-1 stale-self-description (captured-by
`none` until the non-author spot-check; fix = the C1 gate), M57-2 freeze-epoch drift (captured by a wave
seat), M57-3 plan/instrument contract drift, M57-4 stale premise (default-refusal), M57-5 shim-label
drift, M57-6 token-on-argv in a scout probe, M57-7 a seat claim contradicted by the tree, M57-8 an
overclaimed amendment sentence, M57-9 draft-vs-landed instrument hashes, M57-10 ceiling misdescription.

## Trend verdicts

- **expansion: improved** — a new capability row (OpenBao audit-device custody trial, first-working round
  57), audit-device ground entered core, registry 114 → 117 (3 tier-A rows), coverage map +1 entry. No
  existing scope absorbed from a sibling.
- **quality: improved** — three stale self-descriptions repaired and the class gated; the trial and entry
  add executable, sourced domain ground; the gate battery against BASE shows no regression
  (`checklist-run` BROKEN failed=7 at BASE and at the tip — a substrate-absence condition; `scope-gate`
  DEFECT at BASE with `stale_basis=3`, at the tip with `stale_basis=1`; `docs` CLEAN 38/35/3;
  `claims-declared` CLEAN 39).
- **discernment: improved** — the round's own attacks changed the instrument before admission: the C1
  reviewer's delete-the-evidence/printer false-greens are closed by A3 (K1-F8/K1-F9 FAIL), the C2 critic's
  ceiling sentence was false and is corrected with a live demonstration, the sentinel's argv-leak finding
  was fixed and re-measured. Ten mistake rows, two rejections with flip conditions.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `SKILL.md` §Decision table, §Failure table, §Credential-hygiene checklist; `bash corpus/claim-ledger.sh citations` run of record at `LOG.md` (round-56 entry); no non-author `[x]` verifier named this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `LOG.md` round-57 entry; the audit trial starts two dev servers, writes/reads a KV value, reads the raw/default audit logs and rotates a salt (`final/trial-real.txt`, `final/trial-shims.txt`), and the labrat re-probed it independently.
- [~] Instructions executable by an agent without oral context — evidence: `plans/round-57.md` + four frozen instruments + `corpus/current-claims.py --selftest` (13 cases) and the 13-control battery; all commands are in the lesson and SCORECARD.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` §Core round-57 bullet and §Adjacent unchanged ownership; `R57Connector` reports no sibling holding audit-device ground; the S115–S117 URLs appear in no sibling registry.

## Stale-lane

Stale-lane: n/a — respawn-per-round driver; no other mission of this lane is open.

## Tool installs

None. No tool was installed or upgraded this round; all binaries (`bao` 2.7.2, `sops`, `age`, python 3.14.8,
git 2.56.0, jj 0.45.1) were present and unchanged; pacman stayed untouched.

## Open questions and dissent

- **Freeze-epoch record for the operator's ruling.** The predeclaration `7aa1f472` (11:10) was followed by
  epoch B `03cbf656` (11:16–11:19, A1/A2) and epoch C `8d8e0588` (after the reviewer's false-green), both
  before the binding candidate reading; the trial file and the labrat probe predate epoch B, and the plan's
  A1 sentence "before the trial existed and before any candidate measurement" is false as written. The
  `R57Sentinel` dissent is recorded verbatim in its report: the predeclaration and two frozen instruments
  were amended in place after the freeze and after measurements; severity recalibrated Critical → High
  once it verified that no candidate C2 score preceded epoch B. No target or kill rule moved; the
  `7aa1f472` state stays recoverable in history.
- Ceilings not closed: the C1 checker's frozen `unbound=0` diagnostic (value/population unaffected; the
  landed gate prints the real number); `plans/round-57-c1.sh` still defaults its scratch to `/tmp` when
  `TMPDIR` is unset (routed); mutation survivors M2/M5/M7/M9 on the frozen checker (coverage findings).
