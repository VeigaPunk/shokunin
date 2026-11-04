# tameshi — round 73 report (hyaku run 15, child-lane round)

Lane: `tameshi-shokunin`. Round: 73 (attempt 1). Base: `a3dd35742eee608d1205843dacebc461b4242b9e`
(= `origin/master` at round start, the round-72 non-author verifier spot-check commit).
Lane tip at report time: `5c9a5559039e6ba90e006e768fa6a034fb03ba17` (= `origin/master`; the tip receipts were measured at `e309f59f`, the commit before the receipts commit, and that receipts commit carries no monitored edit). Report commit: this file.

## Work performed

Declared claims (frozen pre-data in `plans/round-73.plan.md`, declaration commit
`17cd19396b36d4c15f1bce1bbdb7c42346f1df76`):

- **R73-C1 — calibration** (the lowest scored numeric axis at 8; capability acquisition; sourced on
  the re-opened S066): `tools/wave-reconcile.py` + `tools/wave-reconcile.json` re-derive a round
  record's own execution claims (seat count, committed seat-report count, role multiset, attack
  share) from the committed wave artifacts, with the round-72 closure's two routed defects standing
  as measured red arms.
- **R73-C2 — operability** (verdict-only): `tools/rekey-cost.py --arms` turns the recorded arm table
  into a re-runnable 7-arm battery and gains the ignored-path arm the round-72 wave's coverage
  finding named.

Work items, each with its evidence pointer:

- **Frozen plan + controls, before any claim data.** `plans/round-73.plan.md` (predicates, counters,
  kill rules, arms, three controls); controls measured pre-freeze in
  `.ufo/evidence/round-73/reh/reh-c1-controls.txt` (always-meet and echo-printed reconcile stubs
  read `rows=6 met=4 unexpected=2` exit 1; a green-rows-only stub reads `rows=4 met=4 unexpected=0`
  and fails the frozen row count) and `reh/reh-c2-m3-six-arms.txt` (`KILLING_ARMS=0/6` before).
- **C1 instrument** — `tools/wave-reconcile.py` (four row kinds, span/token binding, git-object
  artifacts, BOM refusal per S066 §8.1) + `tools/wave-reconcile.json` (six standing rows over the
  committed round-72 wave), commit `fddbb667`; hardening from seat findings `8f7ff279`.
- **C1 record edits** — `corpus/SOURCES.md` S066 re-open + round-73 tail note,
  `corpus/QUALITY.md` criteria 121–123, `tools/pointer-recheck.json` note count, commit `be1199d3`;
  S066 row repair after seat T73W1S05 caught a collapsed row (`1d118c14`); criterion-122 falsifier
  re-pinned revision-stable (`21a7332f`).
- **Cold-read rekey, three batches** — 13 sections at `be1199d3` (`2e89e539`, ledger 820 → 833),
  13 at the S066 repair (`caa5c4c5`, 833 → 846), 6 at the criterion pin (`06ce20f7`, 846 → 852);
  CRLF preserved in every merge (`REBIND merge eol=CRLF …`), additivity raw `raw_old_only=0` on the
  ledger and QUALITY, 1 on SOURCES (the documented S066 cell edit, decoded in
  `additivity-sources-decode-r73.txt`).
- **C2 battery** — `tools/rekey-cost.py --arms` (7 arms incl. `ignored-skill`), commit `7982619f`;
  M3 kill receipts `reh/reh-c2-m3-battery.txt`.
- **Round-72 closure response** — defects 1–2 become C1's red arms; defect 3 restated in
  `corpus/lessons/round-73.md` `## Gate`; defect 4 fixed in `tools/pointer-recheck.json`; defect 5
  paid in the LOG measured entry; carry 6 is C2; carry 7 re-measured
  (`.ufo/evidence/round-73/inherited-misses-r73.txt`: SCORECARD paths missing 20, LOG quotes
  missing 5 (and 6 at the mid-round reading, before the round's own quote-backing pointers landed), all inherited — brace-notation citations from rounds 17–66 and five round-35/41 quote
  lines, none from this round).
- **Wave** — one v1 wave, 13 seats (3 executor · 2 scribe · scout · 2 reviewer · critic · mutation-tester · sentinel · revenger ·
  connector; attack seats by the policy's named set = 2 reviewer + 1 critic + 1 mutation-tester =
  4 = 30.8 %), dispatched from `.ufo/waves/round-73/w1-dispatch.json` (validator exit 0, policy band
  8–16, `counts.spawn=13`), taken at 22:00:32 -03; **13/13 records** in `w1-results.json`, 13 seat
  reports under `.ufo/waves/round-73/w1/`, **0 dead seats**, no residual call — round total 13 seats.

  | seat | role | judgment | what it changed |
  |---|---|---|---|
  | T73W1S01 | executor | support | independent oracle of the C1 rule (own git reader, own span locator, own JSON/BOM refusal): `ORACLE_CMP rows=6 equal=6`, its offsets agreeing (3618 / 179 / 7042) |
  | T73W1S02 | executor | support + gaps | six setup cases driven from outside (all exit 2 with named lines), three mutants; found m2 (`delimited := True`) survives all twelve arms and the sweep, and that the docstring overclaimed arm coverage |
  | T73W1S03 | executor | support → **fixed** | binding audit of all six rows; found the `record` block inert on `roles`/`attack_share` (forged span = silent pass), a meaningless `printed` on `r72-spec-roles`, and an uncaught `KeyError` without `--extra-root`; all three fixed at `8f7ff279` |
  | T73W1S04 | scribe | support → **fixed** | drafted criteria 121–123 and measured that the landed 122 falsifier stopped failing after the round's own correction; re-pinned at `21a7332f` |
  | T73W1S05 | scribe | support → **fixed** | verified the SOURCES delta and caught the collapsed S066 row (8 fields, census E01); repair `1d118c14` + rekey batch-2 |
  | T73W1S06 | scout | support | swept rounds 60–73: 14 records, **1 disagreement** (r72's `11 reports`), 11 rounds with no `results.json`, r60's `agent='task'` vocabulary caveat |
  | T73W1S07 | reviewer | support (3 landed, 2 refuted) | counter spoofable by `measured := expect`; the plan's kill-rule wording contradicted by the green-only control; the `seat_reports` red arm red by span choice (the report self-corrects at line 81); `plan-roles` red arm robust; wrong-reason meets constructible at kind level |
  | T73W1S08 | reviewer | support | committed-byte census, no instrument run: `AGREE rows=6/6` |
  | T73W1S09 | critic | support | both frozen counters green at five tips; C1 upheld, C2 upheld; measured the over-filtering direction (M3c survives battery + selftest while turning a 20-pin forecast into a false 0) and that C2 values are ledger-derived |
  | T73W1S10 | mutation-tester | support + gap | M3 killed by 1/7 battery arms + 1/8 selftest arms with the value re-derived; W1 killed by arms 2/6 but invisible to the sweep; W2 (any-depth `seat_reports`) survives everything with a non-equivalence probe (`files=12` vs `13`) |
  | T73W1S11 | sentinel | falsify → **fixed** | `SECRETS=1` (the RFC fetch's `set-cookie` line — redacted in-round, value never reproduced); `TMPDIR_VIOLATIONS=0`; `MISROOT=3`, all orchestrator-owned runtime state (`.scratch/run13-state.json`, dispatcher and watchdog logs), none written by this round |
  | T73W1S12 | revenger | support | reverse-engineered the artifact contract: `seats` = dispatched spawn lanes; a spawned dead seat IS a record; `note` set only on kernel-loss; proposed a row-level `population` field with a falsifier (carry) |
  | T73W1S13 | connector | support | sibling scan: nearest cousin `kaidoku-shokunin/tools/round-47/record.py` (record reading, not record-vs-artifact reconciliation); this lane's ground is new; `ASSIMILATION=readable` |


  Dispatcher artifacts: `w1-spec.json`, `w1-dispatch.json`, `w1.ready`, `w1.ready.dispatched`.
- **Standing instruments at the tip** — `.ufo/evidence/round-73/instruments-tip-r73.txt`
  (figure-attribution 7/7, count-recheck 7/7 met, anchor-drift 16/16, arm-liveness 9/9 live,
  pointer 12/12, bind selftest 7/7), census end exit 0 (`additivity-b2-r73.txt` §census).

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| `plans/round-73.plan.md` (frozen plan), lesson gate, LOG declared entry, census/base receipts, wave spec + dispatch | `LOG.md` "Round 73 — declared" | `17cd1939` |
| `tools/wave-reconcile.py`, `tools/wave-reconcile.json` | "Round 73 — declared" | `fddbb667` |
| `corpus/SOURCES.md` (S066 re-open + tail note), `corpus/QUALITY.md` (criteria 121–123), `tools/pointer-recheck.json` (note count) | "Round 73 — measured" | `be1199d3` |
| cold-read rekey r73-batch-1 (13 sections) | "Round 73 — measured" | `2e89e539` |
| `tools/rekey-cost.py` `--arms` | "Round 73 — measured" | `7982619f` |
| receipts (RED at edit commit, guards, additivity) | "Round 73 — measured" | `4ebf7a1e` |
| `plans/round-72.plan.md` erratum | "Round 73 — measured" | `3e0ef1c8` |
| `corpus/SOURCES.md` S066 row repair | "Round 73 — appended after the wave" | `1d118c14` |
| cold-read rekey r73-batch-2 (13 sections) | "Round 73 — appended after the wave" | `caa5c4c5` |
| `tools/pointer-recheck.json` note style repair | "Round 73 — appended after the wave" | `7c5ffe04` |
| `tools/wave-reconcile.py`/`.json` hardening | "Round 73 — appended after the wave" | `8f7ff279` |
| `corpus/QUALITY.md` criterion-122 falsifier pin | "Round 73 — appended after the wave" | `21a7332f` |
| cold-read rekey r73-batch-3 (6 sections) | "Round 73 — appended after the wave" | `06ce20f7` |
| wave settlement (spec/dispatch/ready, 13 seat reports + seat artifacts, `w1-results.json`) | "Round 73 — appended after the wave" | `9ffaf039` |
| `SCORECARD.md` measured section + capability row + counter-cheat disclosure; lesson measured/mistakes/wave-attack sections; RFC header `set-cookie` redaction | "Round 73 — measured" / "…after the wave" | `8b6e1bbe` |
| `LOG.md` measured entry + quote-backing pointers | "Round 73 — measured" | `862e8844` |
| quote-backing pointers, S066 field-count and cost-forecast receipts | "Round 73 — appended after the wave" | `bbb7b189` |
| live-instrument, additivity and inherited-miss receipts | "Round 73 — appended after the wave" | `de036cc9` |
| lesson pointer/quote corrections | "Round 73 — appended after the wave" | `9afadc1a`, `314a68de` |
| tip receipts (measured at `9afadc1a`, then at `e309f59f`) | "Round 73 — appended after the wave" | `1decfb23`, `5c9a5559` |

## Before → after measurements

| Claim | Before | After (measured) | Counting command | Measured commit |
|---|---|---|---|---|
| R73-C1 | `git ls-tree -r a3dd3574 -- tools/ \| grep -c wave-reconcile` → `0`; `git grep -c WAVE_RECONCILE a3dd3574 -- tools/` → `0`; the r72 closure's two defects are prose | `WAVE_RECONCILE_SELFTEST: 12/12 pass` exit 0; `WAVE_RECONCILE: rows=6 met=6 unexpected=0` exit 0 with `printed=11 files=12` and plan `labrat` vs executed `revenger` measured as drift on every sweep; independent oracle `ORACLE_CMP rows=6 equal=6` | `python3 -I -X utf8 tools/wave-reconcile.py --selftest`; `python3 -I -X utf8 tools/wave-reconcile.py --repo . --extra-root fleet=/home/vgpnk/Projects/shokunin --manifest tools/wave-reconcile.json` | `fddbb667` → `8f7ff279` |
| R73-C2 | `git show a3dd3574:tools/rekey-cost.py \| grep -c REKEY_ARMS` → `0`; M3 survives 6/6 recorded arms (`KILLING_ARMS=0/6`) | `REKEY_ARMS: arms=7 meet=7 unexpected=0` exit 0 at the C2 commit, after all three rekeys and at the tip; `REKEY_COST_SELFTEST: 8/8 pass`; M3 killed (`measured=9`, `meet=6 unexpected=1` exit 1) | `python3 -I tools/rekey-cost.py --arms`; `python3 -I tools/rekey-cost.py --selftest` | `7982619f`; re-read at `06ce20f7` and the tip |

## Sources & frontier

Counting command and both runs (round start / round end):

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi
round start: 163 rows, warnings only (19 × W04, 1 × W01 S101) -> "tameshi ok …", exit 0
round end:   163 rows, same warning set                         -> "tameshi ok …", exit 0
```
(`.ufo/evidence/round-73/census-start-r73.txt`, `additivity-b2-r73.txt` §census.)

- Rows: **163 → 163**. No new row: the round's sourced claim rests on **S066**, re-opened this round
  for §8.1's encoding ground (UTF-8, the byte-order-mark rule) while S066's §6 number-grammar scope
  stands; a new row on the held URL would be a within-scope duplicate (CORPUS rule 2; the S289/S293
  precedent). Flip condition: the §6 scope is retired or RFC 8259 is superseded.
- Rows touched old → new: S066 `used-by`: `corpus/knowledge/guard-kill-closure.md` →
  `corpus/knowledge/guard-kill-closure.md, corpus/lessons/round-73.md`; three located quotes added to
  the Gate (18, 17, 21 words at page lines 485–486, 494–495, 496–498; fetch 2026-11-04, 28,360 B,
  sha256 `61a5378f…`).
- Rows added by tier: none. Registry tiers unchanged (A 145, B 14, C 4).
- Frontier rows advanced: none — F1–F11 unchanged; this round's ground is a lane instrument, and the
  README `## Frontier` table is byte-identical base → tip.
- Assimilation: **none this round** — `shokuknow/merge/tameshi/` is readable again (seat T73W1S13:
  `ASSIMILATION=readable`, census 103 / 0 / 86 / existing 107 staging snapshot); the round's claim
  set (one capability + the r72 routed-defect closure + three rekeys) carried no theme slot, and an
  adoption needs its own per-entry gates. `considerthese/2026-10-28.md` proposal 4 (assimilation
  backlog burn-down) is the only still-unimplemented proposal and does not fit this round's claims.

## Trend verdicts

- **expansion — improved.** A capability entered `SCORECARD.md` `## Capabilities` (`wave-record
  reconciliation`, first working round 73) through a demonstrated run, and the corpus gained a
  re-opened source row with three fresh located quotes and three new QUALITY criteria (121–123) that
  turn three closure-routed defect classes into standing obligations.
- **quality — improved.** Two of the round-72 closure's routed defects now stand as measured red
  arms; three falsifiers were corrected to revision-stable forms; the cold-read monitor reads
  `lost=0 ok` at both floors and `credited=64/64` in rev mode after three rekeys with byte additivity
  preserved (CRLF included, the r72 defect class not repeated); the tool was hardened on two seat
  findings with the frozen counters unchanged.
- **discernment — improved.** Five seats' attacks were adopted as work (S03's three binding defects,
  S05's collapsed-row catch, S02's docstring overclaim, S04's unstable falsifier, S10's W2 gap
  recorded); one honest self-catch is recorded as a mistake (the S066 cell edit that dropped four
  cells, caught by a seat and repaired in-round); S09's M3c over-filtering mutant is recorded as a
  named gap rather than argued away.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — [lane assertion, no independent promotion verifier](reports/round-1-calibration.md#box-1)
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — [lane assertion, no independent promotion verifier](reports/round-1-calibration.md#box-2)
- `[~]` Instructions executable by an agent without oral context — [lane assertion, input-keyed monitor only; no independent promotion verifier](.ufo/evidence/round-21/coldread/ledger.json)
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — [lane assertion, no independent promotion verifier](reports/round-1-calibration.md#box-4)

## Round extras

- **Stale-lane:** none — this round ran under the respawn-per-round driver; no other mission of this
  lane is open.
- **Tool installs:** none this round (no `uv`, `npx`, `pacman`, `~/.local/bin` write; pacman stayed
  paused per the addendum guard).
- **L0 questions:** none opened this round.
- **Dead seats:** none — 13/13 records in `w1-results.json` and 13 seat reports; no seat died, no seat was replaced. Residual call: none.
