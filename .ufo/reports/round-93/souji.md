# souji — round 93 report (hyaku run 15, attempt 1, L1 SoujiR93)

Lane repo `souji-shokunin`, branch `master`. Lane base `91c9bcb1041b18be154ca466ac3c047ac7862fe1` (r92 closed).
Final lane tip `2794527218c938ebe9d1d1c07073ebe598565616` (pushed; see `ls-remote` below).

## Work performed

Declared claims (frozen in `census/round-93/preregistration.txt`, commit F `9a4ab88f`):

- **C1 — calibration 7** (the lane's lowest owned non-retired axis): two counter edits that survive every r92 row,
  `h-ok-admits-one` (line 552 `resolved >= len(pop) - 1`, R92MutC1 E1) and `a491c22-<-to-<=` (`_ledger` width guard
  `len(r) <= 3`), are bound by two rows of two new harness row types, LD5 (`ledger-drop`) and LD6 (`ledger-trim`).
  **Verifies as narrowed** (`plans/round-93.md` A1, A2, A3; limit A4).
- **C2 — coverage 8** (sourced claim, S356): the K4 excerpt's cut-POSITION edge class. KFF19 (exact equality with a
  reference cut written from the WHATWG UTF-8 decoder) and KFF20 (overlong across the head cut) reject the three
  forgeries the r92 fixture passed 20/20. **Verifies as narrowed** (`plans/round-93.md` A5; no score change, A6).

Work items:

- Protocol load and claim choice from the r92 spot-check's routed items 1-5 and R92MutC1/R92MutC2 —
  `plans/round-93.md` A0.0.
- C1 instruments: r93 harness with the `ledger-drop`/`ledger-trim` row types and the r93 population pin
  (`census/round-93/c1-false-row-harness.py`); population `census/round-93/c1-false-rows.tsv` (r92 64 rows
  byte-for-byte + comment + LD5 + LD6, sha256 `d6439f65…`); survivor search v3 (`census/round-93/c1-survivor-search.py`:
  hand edit `h-ok-admits-one`, row-mismatch kill rule, SIGINT/SIGTERM cleanup, `--emit` /tmp guard); targets and the
  written prediction `census/round-93/c1-prediction.txt` — all in P1 `2c82d362`.
- C2 instruments: `tests/fixtures/r93-k4-flagfail.py` (KFF19 reference cut `_ref_len`/`_ref_straddle`/`ref_cuts`,
  14,586-payload sweep; KFF20); `census/round-93/c2-forgery-probe.py` (F1-F4, N0 + F5 surrogatepass, F6 multichar,
  F7 head-forward) — P1 `2c82d362`.
- S356 opened (WHATWG Encoding Standard §8.1.1, capture `census/round-93/srcs/encoding.html`), row appended,
  knowledge entry `corpus/knowledge/utf8-cut-position-reference.md` — P1 `2c82d362`.
- Do-nothing controls committed before F: C1 `census/round-93/controls/c1-control-r92-population.txt`
  (`killed=0 survived=2`); C2 `controls/c2-control-r92-fixture-probe.txt` (`rejected=5`, EXIT 1),
  `controls/c2-control-r91-tool-both-arms.txt` (16/22, EXIT 1); pre-freeze feasibility disclosed in
  `controls/prefreeze-feasibility-note.txt` — P2 `0d6442cc`.
- After receipts post-F: `census/round-93/records/c1-after.txt`, `c1-pristine-after.txt`, `c2-forgery-after.txt`,
  `c2-after.txt`, `c2-k4-regression.txt` — A `7bdb96b7`.
- One v1 wave of 13 seats; spec/dispatch `.ufo/waves/round-93/w1-spec.json`, `w1-dispatch.json` — `f268ce22`;
  every seat integrated (`.ufo/waves/round-93/w1/`, driver `w1-results.json`), amendments A1-A6 recorded before
  filing, pre-file ledger `.ufo/waves/round-93/claim-falsification.tsv` — `27945272`.
- Lesson `corpus/lessons/round-93.md` (Gate, five mistakes, wave findings, routed), QUALITY Q169/Q170, LOG `## Round
  93`, SCORECARD Round 93 rows + capability rows + `### Planned (r94)` — `27945272`.

## Landed changes

| commit | what | LOG.md entry |
|---|---|---|
| `2c82d36254a40f717f120a08112836386d01771b` | P1: r93 harness + population (LD5/LD6), search v3, targets + prediction, r93 fixture KFF19/KFF20, 8-forgery probe, S356 capture + row + knowledge entry, census before | `## Round 93` Claims, Sources |
| `0d6442ccd0d763964529bdc73caffe21f6434adf` | P2: C1 and C2 do-nothing controls, pre-freeze feasibility note | `## Round 93` Claims |
| `9a4ab88f2495bb2e6df24021f6d6e10738afea95` | F: preregistration alone | `## Round 93` Claims |
| `7bdb96b74401d75b459d026c079a3e6e7bb209ff` | A: after receipts (C1 2/0, pristine 66/0; C2 8/8, 22/22, K4 12/0) | `## Round 93` Claims |
| `f268ce22298fbefb26914615bfc2f23912dde026` | wave spec + validated dispatch (spawn 13), plan A0 | `## Round 93` Wave |
| `2794527218c938ebe9d1d1c07073ebe598565616` | wave evidence (13 seats), pre-file ledger, plan A0-A6, lesson, Q169/Q170, LOG/SCORECARD, census after, labrat-role repro | `## Round 93` Narrowed, Mistakes, Wave |

## Before → after measurements

- **C1** (measured at `7bdb96b7`; instruments P1 `2c82d362`, freeze F `9a4ab88f`). Command:
  `python3 -B census/round-93/c1-survivor-search.py --counter census/round-87/c1-pointer-counter.py --harness
  census/round-93/c1-false-row-harness.py --population <POP> --lane . --fleet-root /home/vgpnk/Projects/shokunin
  --work WORK --jobs 2 --ids census/round-93/c1-targets.json`.
  Before (POP = r92 population): `SEARCH-SUMMARY generated=2 ambiguous=0 uncompiled=0 hung=0 scored=2 errored=0
  killed=0 survived=2`, EXIT 0. After (POP = r93 population): `… scored=2 errored=0 killed=2 survived=0`, EXIT 0;
  pristine harness `SUMMARY rows=66 mismatches=0 accepted=0 refused_true=0 errors=0`, LD5 `rc=1 match=yes`, LD6
  `rc=0 match=yes`, EXIT 0. Killing rows (R93ExecC1 §5, R93ExecResidual (a)): LD5 `got=UNRESOLVED rc=0 match=no` for
  h-ok-admits-one, LD6 `got=UNRESOLVED rc=1 match=no` for a491c22. Narrowed: A1 (the "because no r92 run reaches their
  clause" sentence is false — h-ok flips three r92 exits on rows that assert no rc), A2 (edits, not clauses), A3 (an
  uncaught counter exception still scores killed), A4 (two gitignored lane-disk inputs). Reported, not claimed: the
  78-id residual set `killed=0 survived=78` (r92) → `killed=2 survived=76` (r93).
- **C2** (measured at `7bdb96b7`). Command: `python3 -B census/round-93/c2-forgery-probe.py --fixture <FIXTURE> --tool
  tools/souji-record-agreement.py --before census/round-92/controls/c2-before-tool.py --work WORK`. Before (FIXTURE =
  `tests/fixtures/r92-k4-flagfail.py`): `FORGERY-SUMMARY forgeries=8 rejected=5 positive=pass`, EXIT 1 (F5/F6/F7
  20/20). After (FIXTURE = `tests/fixtures/r93-k4-flagfail.py`): `FORGERY-SUMMARY forgeries=8 rejected=8
  positive=pass`, EXIT 0; fixture `SUMMARY cases=22 tool_pass=22 before_pass=16` EXIT 0; K4 `SUMMARY rows=12
  mismatches=0 errors=0` EXIT 0. Narrowed A5 (KFF18 is the r92 cut-position case; the reference is independent of
  tool code and Python's codec, not of the excerpt constants).

## Sources & frontier

- Rows before → after: 277 → 278 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Added by
  tier: A +1 (S356, `spec`, `mined`, WHATWG Encoding Standard §8.1.1 UTF-8 decoder, opened 2026-11-09; re-opened live
  byte-identical by R93ScoutSources). Rows touched old→new: none (one `+` line, zero `-` lines; R93Connector §4).
  Frontier: the excerpt cut's verification moves from a faithfulness property (r92 KFF18) to an exact-position check
  against a reference written from the decoder algorithm (S356); reject sample BOM precedence (§8.1.1 first sentence)
  with a flip condition; the `surrogatepass` codecs page stays S351 (no duplicate row).
- Census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`:
  round start `souji ok`, EXIT 0 (`census/round-93/records/sources-census-before.txt`); round end `souji ok`, EXIT 0
  (`census/round-93/records/sources-census-after.txt`); W04 warnings only.
- Mined mistakes: `corpus/lessons/round-93.md` `## Mistakes` M1-M5 (M3 and M4 shown able to fail: Q169 prints
  `rejected=5` on the r92 fixture; Q170's crash probe reads `yes` today, `R93Sentinel/repro/h-crash3.out`).
- Sourced claim: C2 rests on S356 (cited by the fixture's KFF19 comment and the knowledge entry).
- Assimilation: none — no theme taken from `merge/souji/`. considerthese: the lane has no `considerthese/` directory.
- r92 spot-check routed defects: 1 answered (C2), 2 answered for E1 (C1; the 76 residuals carried), 3 answered for
  SIGINT/SIGTERM and the /tmp guard (SIGKILL residual stated), 4 compliant (no in-place cell edit), 5 checked (misroot
  sweep found none).

## Trend verdicts

- **expansion: improved.** S356 admitted (278 rows) with a new knowledge entry on ground the lane did not hold
  (position-pinning by a decoder-algorithm reference vs r92's well-formedness rule); three capability rows (ledger-edit
  false rows, exact-position excerpt check, interruptible survivor search) with passing demonstrations.
- **quality: improved.** Two counter edits that survived every r92 row are bound (2/0 vs 0/2); three forgeries the r92
  fixture accepted are refused (8/8 vs 5/8); 300,000 random wave payloads show 0 filed-tool disagreements with the
  reference; Q169/Q170 land with able-to-fail checks. Residuals (crash-as-kill, m5/m6/g2, filler/length, fixture
  exception handling) are named and routed.
- **discernment: improved.** The wave falsified three claim sentences and one instrument sentence; each was narrowed in
  `plans/round-93.md` before filing (A1, A3, A5) rather than defended, the C1 construction is stated with a committed
  prediction and control, and the C2 score is held at 8 because 8/8 is not a fraction (A6).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `corpus/SOURCES.md` S356;
  `corpus/QUALITY.md` Q169/Q170; `corpus/lessons/round-93.md` Gate.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md `## Round 93` (controls, after
  receipts on committed bytes: `census/round-93/records/`).
- [~] Instructions executable by an agent without oral context — `census/round-93/preregistration.txt` commands
  reproduced by non-author seats (`.ufo/waves/round-93/w1/R93ExecC1.md`, `R93ExecC2.md`, `R93ReviewerC1.md`,
  `R93ReviewerC2.md`, `R93Critic.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `.ufo/waves/round-93/w1/R93Connector.md` §1: no sibling owns
  the surfaces; no credentials, history or sibling lane touched.

## Extras

- **Round shape:** one v1 wave (`w1`, policy `ufo-wave-policy.json`, `w1-dispatch.json` validated `spawn 13`), 13
  seats: 3 executor, 2 reviewer, critic, 3 mutation-tester (R93Labrat ran as a mutation-tester: the validator refuses
  `labrat`, `census/round-93/controls/labrat-role-refusal-repro.txt`, A0.1), sentinel, connector (1), scout, scribe;
  planner held by the L1 (validator-frozen); the planning data-walk rode R93Connector. Residual call: none. Round
  total 13. Dead seats: none (13/13 settled with a report, `w1-results.json`). Ready file `l1` `SoujiR93`;
  WAVE-DONE received.
- **Attack share:** 6/13 = 46 % (reviewer ×2, critic, mutation-tester ×3); the prefile gate's broader set 8/13.
- **Pre-file falsification ledger:** `.ufo/waves/round-93/claim-falsification.tsv` (23 rows; 9 `falsifies-wording`,
  each pointing at `plans/round-93.md` A1-A6). `python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py
  --lane souji --round 93` → `PREFILE-FALSIFICATION: pass claims=2 rows=23 attack_seats=8 findings=0`, EXIT=0.
- **Pre-report gate:** `git -C souji-shokunin ls-remote origin refs/heads/master` →
  `2794527218c938ebe9d1d1c07073ebe598565616	refs/heads/master`.
- **Inherited state:** none (attempt 1; lane clean at base, no `lane-dead-no-report souji round=93` line). Not
  authored by this lane and not edited: `corpus/lessons/round-92-verifier-spotcheck.md`, `.ufo/state/*`.
- **Misroot sweep:** fleet-root `git status --porcelain` (with and without `--ignored`) shows no souji r93 file; only
  orchestrator `.scratch/` entries, which are never touched.
- **Stale-lane:** respawn-per-round driver, round 93 of the hyaku campaign; no other mission of this lane is open.
- **Tool installs:** none (no pacman, uv, npx or binary fetch; no sysctl or sudo).
- **L0 questions:** none opened this round.
