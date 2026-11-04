# tameshi — round 72 report

- **Lane:** `tameshi-shokunin` (verification-fixture craft) · **Round:** 72 (attempt 1)
- **Base:** `f20ba482c7441d4c75818e7cd8a3165fee7821a1` (= `origin/master`, clean tree)
- **Final lane tip:** `9b4ffe4722befcf6d271d6e168d6a3d20575e913` (= `origin/master` at the
  pre-report `ls-remote` check) · **Report commit:** this commit on the fleet repo
- **Round shape:** ONE v1 wave, **12 seats** (policy `scripts/hyaku/ufo-wave-policy.json`,
  band 8–16). Roles: 3 executor · 2 scribe · 1 scout · 1 reviewer · 1 critic ·
  1 mutation-tester · 1 sentinel · 1 revenger · 1 connector. Attack seats by the
  policy's named set (reviewer, critic, mutation-tester) = 3/12 = 25 % (the floor),
  plus a revenger probe (a fourth adversarial seat in substance). No residual call.
- **Planner seat:** held by the L1 (the validator rejects `planner`); the bounded
  planning data-walk rode the scout item `T72W1S06`.

## Work performed

Two claims, both frozen **before any claim data** in
`tameshi-shokunin/plans/round-72.plan.md` (declaration commit `dfb534ca`), each on
a distinct axis and causally separable:

- **R72-C1 — capability acquisition, axis `operability` (verdict-only):**
  a **planning-time rekey-cost forecast**. `tools/rekey-cost.py` prices a planned
  edit set against the cold-read ledger's own input pins, so the re-read debt a
  round would owe is known before the bytes change (the class that cost round 52
  its admission; `considerthese/2026-10-28.md` proposal 3, adopted this round).
- **R72-C2 — axis `calibration` (the lowest scored numeric axis, 8):** the two
  routed defects from the round-71 non-author closure are **paid** — S302's
  `§4.3` label superseded by S303 (`§4.2 Selecting lines by numbers`; the §4.4
  quote sits at page lines 2446–2449, not 2445–2448) and the PROVINCE round-16
  append's `:85-91` corrected by append — with the cold-read rekey the edits owed.

Work items, each with its evidence pointer:

- **Model first, tool second.** The forecast's rule ("newest ledger entry per
  section pins the path") was **measured, not asserted**: four single-edit
  counterfactuals were re-driven on the frozen guard in scratch clones at base
  before the plan was frozen — `corpus/SOURCES.md` `lost=13`, `PROVINCE.md`
  `lost=6`, `corpus/QUALITY.md` `lost=6`, `SCORECARD.md` `lost=0`, and both edits
  `lost=17` (`tameshi-shokunin/.ufo/evidence/round-72/reh/`, five receipts +
  `reh/README.txt`). That rehearsal also corrected the plan's first draft, which
  had assumed 13 for the round's edit set.
- **The instrument** (`tools/rekey-cost.py`, commit `b3392010`): selftest 8/8,
  four discriminating arms (`at_risk=13/6/6/0/0/17`, no-path exit 2), each arm
  equal to its guard counterfactual; the round's own forecast 17 equals the
  guard's measured `lost=17 RED` at the edit commit `d618518a`
  (`cost-live-*.txt`, `cost-prediction-at-edit.json`, `live-red-r72.out`).
- **The corrections** (commit `d618518a`): `corpus/SOURCES.md:178` gains S303
  (`supersedes S302 —`), `PROVINCE.md` gains the correction block naming
  `:88-94` and `:88-97`, and `.ufo/evidence/round-72/corrections.md` is the
  pointer record.
- **The payment** (commits `bc7dc2fb`, `b611e763`, `d7eb02c2`): the RED the edits
  cost was measured (`lost=17 RED`) and paid by the rekey — `REBIND OK
  sections=17 entries_added=17 ledger_before=797`, ledger 797 → 814 — and, after
  a third correction the wave found, a second batch (`REBIND OK sections=6
  entries_added=6 ledger_before=814`, ledger 814 → 820).
- **The wave** (see "Wave" below): 12 seats, 11 reports; three seats found real
  defects the L1 had not seen (S03: the merge's CRLF→LF rewrite; S05: a third
  stale span and the unattainable frozen control line; S09: an arm-coverage gap).

### Wave (seats, roles, findings, dead seats)

Dispatch `.ufo/waves/round-72/w1-dispatch.json` (validator exit 0; policy
`maxLanes` 16, band 8–16), handed over as `.ufo/waves/round-72/w1.ready` and
taken at 21:21:33. Seat reports under `.ufo/waves/round-72/w1/`.

| seat | role | verdict | what it changed in the round |
|---|---|---|---|
| T72W1S01 | executor | support | independent oracle agrees with the tool on all six arms |
| T72W1S02 | executor | support | ledger census `CENSUS base_entries=797 live_entries=820 sections=64`, exit 0 (`w1/T72W1S02/ledger-census.json`) |
| T72W1S03 | executor | **falsify → fixed** | found the rekey merge rewrote the ledger CRLF→LF (293,268 insertions / 281,925 deletions); repaired at `b611e763` |
| T72W1S04 | scribe | support | live sed fetch (sha256 `511edd60…`, byte-identical to the r71 snapshot) + S303 row draft |
| T72W1S05 | scribe | **falsify → fixed** | third stale span `PROVINCE.md:56` `:84-89`; and the frozen C2 control line is unattainable as written |
| T72W1S06 | scout | support | 96 records / 2,310 pointer tokens: 995 resolvable, **30 out-of-range**, 302 target-missing (270 bare sibling basenames), 53 ambiguous (`w1/T72W1S06/pointer-census.md`) |
| T72W1S07 | reviewer | support | cheat forecasts (constant-13/0, sum-not-union) each fail a frozen arm |
| T72W1S08 | critic | support | §4.2 is the correct label (§4.3 is "selecting lines by text matching"); census E04 exemption real |
| T72W1S09 | mutation-tester | support + gap | four mutants killed; `IGNORED`-filter mutant survives the arms (selftest-only kill) |
| T72W1S10 | sentinel | support | no credentials, no misroot, TMPDIR honoured, no escaping symlinks |
| T72W1S11 | revenger | support | credit keys on recorded input pins (mutated pin → only that section uncredited, `input-drift:…`) |
| T72W1S12 | connector | support | no sibling owns cold-read cost accounting; shokuknow `merge/tameshi/` not readable |

All 12 seats settled and returned a report (`w1/*.md`); the dispatcher's
`w1-results.json` (12 seat records, no `note`, no failure) is committed as wave
evidence at `56866fa3`. **Dead seats: none.** No residual call was needed; the
round total is 12 seats.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| plan + wave spec/dispatch + census/base/rehearsal receipts (the freeze) | `LOG.md` "Round 72 — declared" | `dfb534ca` |
| S303 supersession, PROVINCE append, corrections note, lesson opening | `LOG.md` "Round 72 — declared" (the work it froze) | `d618518a` |
| rekey batch 1 (17 sections, ledger 797 → 814) | "Round 72 — measured" | `bc7dc2fb` |
| CRLF repair of the merged ledger (byte-additive) | "Round 72 — appended after the wave" | `b611e763` |
| `tools/rekey-cost.py` + capability row (`## Capabilities`) | "Round 72 — measured" | `b3392010` |
| pointer rows 8 → 11, control manifest, measured verdicts, lesson | "Round 72 — measured" | `de43f7dc` |
| quote-citation fixes (receipts dirs cited, composite quote split) | — | `93cae77b` |
| third correction (six-leg anchor) | "Round 72 — appended after the wave" | `b7b98375` |
| rekey batch 2 (6 sections, ledger 814 → 820, CRLF preserved) | "Round 72 — appended after the wave" | `d7eb02c2` |
| fourth pointer row + errata (third correction, plan defect, coverage gap) | "Round 72 — appended after the wave" | `a533d7d3` |
| backing receipts (batch-2 line, pre-repair/repair additivity, aimed control) | — | `ebad004b` |
| base-record ERROR probe receipt | — | `d8e7f337` |

## Before → after measurements

### R72-C1 — verifies (measured)

Counting command (both sides, one command each):

```sh
git -C tameshi-shokunin ls-tree -r f20ba48 tools/ | grep -c rekey-cost          # before
python3 -I tools/rekey-cost.py --selftest                                       # after
python3 -I tools/rekey-cost.py --edit corpus/SOURCES.md --edit PROVINCE.md      # after
```

- **before:** `0` (no such tool; no `REKEY_COST` line in the tree at base).
- **after:** `REKEY_COST_SELFTEST: 8/8 pass` exit 0; `REKEY_COST sections=64
  planned=2 at_risk=17 predicted_lost=17` exit 0; arms `at_risk=13` (SOURCES),
  `6` (PROVINCE), `6` (QUALITY), `0` (SCORECARD), `0` (pointer manifest), `17`
  (both), exit 2 (no path).
- **the model is measured, not asserted:** each non-structural arm equals the
  guard re-driven on that same single edit at base (`reh/reh-*.out`).
- **live check:** the forecast 17 = the guard's `COLDREAD_PRECHECK … lost=17 RED`
  at the edit commit `d618518a`.
- **measured commit:** `b3392010` (tool bytes), prediction at `d618518a`.
- **control:** constant-13 fails the 2/0 arms; constant-0 fails 13/17; sum-not-union
  reports 19 and fails; the base tree cannot produce the forecast at all.

### R72-C2 — verifies (measured), with one disclosed plan defect

```sh
python3 -I tools/pointer-recheck.py --repo . --manifest tools/pointer-recheck.json
python3 -I tools/pointer-recheck.py --repo . --manifest .ufo/evidence/round-72/control-manifest.json
python3 -I tools/rekey-cost.py --edit corpus/SOURCES.md --edit PROVINCE.md   # forecast 17
python3 -I tools/coldread-precheck-portable.py --repo . --floor f20ba482c744 --cand d618518a6783
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi
```

- **before:** S302 (`corpus/SOURCES.md:177`) cites `§4.3` for a sentence in
  `§4.2` and page lines 2445–2448 for a quote at 2446–2449; `PROVINCE.md:57`
  carries `:85-91` and `:56` carries `:84-89`, both stale; the lane's red arm
  `province-r16-sevenleg-85-91` measures the drift on every sweep.
- **after:** `POINTER_RECHECK: rows=12 met=12 unexpected=0` exit 0 with four new
  rows `hit ok` (`sources-s303-sed-4-2`, `province-r72-tenleg-88-97`,
  `province-r72-sevenleg-cut-88-94`, `province-r72-sixleg-cut-88-93`); the
  two-row stale-span control `rows=2 met=2` both `miss ok`; the **aimed** control
  (record at the edit commit, target at base) `rows=3 met=2 unexpected=1` — the
  S303 row reads `MISMATCH`, i.e. the base cannot satisfy the label check; the
  base-record probe reads `ERROR reason=pointer-absent-in-record` exit 1
  (the frozen control line cannot be scored at base at all — see below).
- **census:** exit 0 at round start (`census-start-r72.txt`, 19 lines, known W04/W01
  warnings) and at round end (`census-end-r72.txt`, `tameshi ok`).
- **monitor:** `lost=17 RED` at the edit commit → `lost=0 ok` at the round base
  floor and the historical floor, measured at cand `56866fa37ec4`
  (`live-green-r72.out`: floor `f20ba482c744` 64 → 64; `live-green-hist-r72.out`:
  `8b0042bd` 46 → 64), the r71 round floor measured separately
  (`live-green-floor4ed9-r72.txt`: `4ed9ce1c` 64 → 64), and `credited=64/64` in
  rev mode; raw additivity over the rekey tip `raw_old_only=0 raw_new_only=53`,
  exit 0. The commits after the measured cand add only evidence files, none of
  which is in a section's input union — the receipt names the exact measured cand,
  and the pre-report `ls-remote` prints the final tip.

  *Citation erratum (seat T72W1S05 read the receipt bytes):* the lesson's first
  sentence named `4ed9ce1c` for `live-green-r72.out`, whose floor is
  `f20ba482c744`. Corrected by an appended erratum and a receipt
  (`live-green-floor4ed9-r72.txt`) rather than by rewriting the committed line.
- **measured commits:** `d618518a` (edits) → `bc7dc2fb` (merge) → `b611e763`
  (repair) → `b7b98375` (third correction) → `d7eb02c2` (batch 2).
- **disclosed plan defect:** the frozen control sentence — "the same three rows
  at base revs read three `miss ok` under `rows=3 met=3`" — is **unattainable**
  as written: the instrument refuses a record revision whose pointer token is
  absent (`pointer-absent-in-record`), and a record absent at base is a setup
  error (`error=setup … not in 'f20ba48'`, exit 2; seat T72W1S05). The control
  was re-shaped **after the freeze** to the two-row stale-span manifest plus the
  aimed control. C2's claim is unaffected (the four tip rows hit, census 0,
  monitor green), but the frozen control line was wrong and is reported as wrong
  rather than silently replaced. The fourth pointer row and the batch-2 rekey are
  likewise disclosed as post-freeze additions, not retro-fitted into the plan.

## Sources & frontier

- **Rows before → after:** **162 → 163** —
  `git -C tameshi-shokunin grep -c -E '^\| *S[0-9]{3,} *\|' <rev> -- corpus/SOURCES.md`
  → `162` at `f20ba48`, `163` at the tip.
- **Rows added by tier:** A 144 → 145; B 14 → 14; C 4 → 4. Status: mined 130 → 131,
  queued 22, rejected 10. Kind: docs 89 → 90.
- **Row added:** **S303** — GNU sed manual (GNU sed 4.9), `docs`, tier A, scope =
  the line-address semantics behind the pointer-recheck engine, re-stated with the
  manual's section numbers **measured this round** (§4.4 quote at page lines
  2446–2449; §4.2 at heading line 2246, numeric-address sentence at 2255).
  Opened 2026-11-03 (HTTP date `Wed, 04 Nov 2026 00:21:37 GMT`, Content-Length
  415310, sha256 `511edd60…`, byte-identical to the r71 snapshot). `teaches`
  opens `supersedes S302 —`; `used-by corpus/lessons/round-72.md`; census E04
  exemption exercised (the counter-run without the prefix prints E04 — critic
  seat T72W1S08).
- **Rows touched old → new:** none — the registry is append-only and S302's
  status/recheck/used-by cells are unchanged; the correction is the superseding
  row plus the lesson's erratum.
- **Frontier rows advanced:** none. The capability enters the **SCORECARD
  repertoire**, not a `corpus/README.md` frontier row; adding one would re-owe the
  rekey payment for no measured gain this round (the README is a monitored file).
  Named as next-round work if the frontier table is to carry the cost instrument.
- **Gate (≤25-word located quotes, access dates):** in
  `corpus/lessons/round-72.md` `## Gate` — the §4.2 sentence (12 words, page line
  2255) and the §4.4 range sentence (20 words, page lines 2446–2449), both fetched
  2026-11-03. **Reject re-sampled:** S293's standing rejection (same-URL
  git-cat-file batch framing) — verdict unchanged.
- **Assimilation:** `considerthese/2026-10-28.md` proposal 3 (cold-read cost
  forecast at planning time) adopted as C1; proposals 1-2/5 landed in earlier
  rounds, proposals 4 unadopted. `shokuknow/merge/tameshi/` was not readable this
  round (connector seat T72W1S12, read-only check) — no package adoption, no
  fabrication of one.

## Trend verdicts

- **expansion — improved.** A capability entered the repertoire through a
  demonstrated round (`tools/rekey-cost.py`, SCORECARD `## Capabilities`, row
  greppable as `| rekey-cost forecast |`), and the registry gained one mined row
  (S303) with a located quote. No admitted entry was displaced.
- **quality — improved.** Two routed record defects are now corrected **and
  measured** on every sweep (four green pointer rows beside the standing red arm),
  the cold-read monitor is restored at both floors and in rev mode, and the merge's
  CRLF→LF defect — invisible to the guard because it parses JSON — was caught and
  repaired to byte-additivity (`raw_old_only=0`). Standing instruments re-read
  clean: figure-attribution 3/3, count-recheck 7/7, anchor-drift 16/16,
  arm-liveness 9/9 live.
- **discernment — improved (lane-side; the independent spot-check is the closure's).**
  The gate's standing rejection was re-sampled and agreed; three seats' attacks
  were adopted as work rather than argued away (the EOL defect, the third stale
  span, the arm-coverage gap), and one frozen counter line was found unattainable
  and reported as wrong instead of being silently rewritten. Mistakes mined: four
  (see `corpus/lessons/round-72.md` `## Mistakes` and the appended rows).

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — [lane assertion, no independent promotion verifier](reports/round-1-calibration.md#box-1)
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — [lane assertion, no independent promotion verifier](reports/round-1-calibration.md#box-2)
- `[~]` Instructions executable by an agent without oral context — [lane assertion, input-keyed monitor only; no independent promotion verifier](.ufo/evidence/round-21/coldread/ledger.json)
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — [lane assertion, no independent promotion verifier](reports/round-1-calibration.md#box-4)

## Extras

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Inherited state:** the lane was clean at base (no uncommitted leftovers, no
  earlier attempt of round 72 in `.ufo/watchdog.log`); nothing inherited to resolve.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` →
  only orchestrator-owned `.scratch/*` files and the pre-existing untracked `after`
  entry; no seat wrote a tameshi round-72 file at the fleet root, so no misroot to
  copy back or delete.
- **Tool installs:** none. No package was installed or upgraded this round; pacman
  stays paused. (All runs used the host's `python3`, `git`, `curl`, `node`.)
- **L0 questions:** none appended this round. The r60/r70/r71 operator items stand
  (promotion review, runbook wording). Note: the **L2-minimum prompt item is now
  present** in the dispatched prompt (§3) — the r71 spot-check's routed
  prompt-fidelity defect no longer reproduces on this round's prompt, so the r60
  L0 line is superseded by observation, not by an answer.
- **Assimilation line:** see Sources & frontier (adopted: `considerthese/2026-10-28.md`
  proposal 3; shokuknow unreachable).
- **Record instruments at the final tip (`9b4ffe47`):** quoted-line — lesson
  15/15 backed (0 missing), SCORECARD 377/377 quotes backed with exit 1 from **6
  inherited absent cited paths** (rounds 38-63, e.g. `.ufo/reports/round-63/tameshi.md`),
  LOG 128/133 with the **5 inherited misses from rounds 35-41**; receipt-exists on
  the round's three documents `paths=16 missing=0 extra=0` exit 0;
  receipt-commit-bind over the 16-commit range `findings=0` exit 0; census end
  exit 0 (`tameshi ok`). None of the residual findings is authored by this round.
- **Open carries (not claims):** the ignored-path arm for the forecast battery
  (S09); a PDF heading parser for the anchor-drift snapshots; the frontier row for
  the cost instrument; SCORECARD's inherited receipt-exists misses (22, rounds
  17-66, disclosed by the 365-path sweep).
