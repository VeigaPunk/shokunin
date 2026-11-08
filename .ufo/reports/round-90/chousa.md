# chousa — round 90

Lane `chousa`, round 90, attempt 1. Base `f54a45ed197dd475af50d82e43a22df3d2e99782` (round-89 landing + its
non-author spot-check). Freeze `8d9893b42eb22690ea5f920ab87fd7e1810b847a`; receipts carrier
`9bad12011187d114ba2c4588c5df08a21ab28145`; S220 capture commit `aa7d4223`; landing
`a45cbff6e783b9d817c23c99716c5fc7135f8a44`; evidence commit `64db6a83b8fd262076f80c8cb161fd659da0dac2`; lane branch `master` pushed
`64db6a83b8fd262076f80c8cb161fd659da0dac2`. One v1 wave, 13 seats (5 executor, 2 reviewer, 1 critic, 1 mutation-tester, 1 sentinel, 1 scout,
1 connector, 1 scribe; attack share 6/13 = 46%), 0 dead seats, no residual call; round total 13 seats.

## Work performed

Declared claims (three axes, no exploratory claim):

- **C1 `C1-DRIVER-R90` (operability — the lowest scored non-retired axis, historical 3/10).** The round-89 control
  driver's spot-checked defects close: the committed receipt is read before any fresh run and never rewritten, body
  fields bind as whole tokens (`TOKEN_DETACHED`), duplicate body keys are refused (`DUPLICATE_KEY`), the harm row
  requires `records>=1` and a setup negative exists, the receipt carries a `# computed_against=` pin and the driver
  self-pins the scoring bytes at their carrier revisions, and the fresh re-run agrees on exit/tokens/predicates.
- **C2 `C2-CURATION-R90` (calibration).** The verdict leg moves before the summary so the passing path prints
  `VERDICT fields_hold=1`; four detector functions each get a two-directional witness that kills the two
  constant-substituted detectors round 89 left alive.
- **C3 `C3-TALLY-R90` (freshness).** The nine current `SKILL.md` self-test tallies re-derive to the tool's own
  283-case verdict; three historical quotes are counted and untouched.

Work items, each with its evidence pointer:

- Claim freeze (instruments, expectations, before receipts, pins, registry row, egress table): `plans/round-90.md:1`,
  `corpus/evidence/round90/claims.md:1`, `.ufo/waves/round-90/claims.json:1` at `8d9893b4`.
- C1 instrument: `corpus/evidence/round90/control-driver-r90.py:1`, `control-forgeries-r90.py:1`,
  `harm-recheck-r90.py:1`, `controls/expected.tsv:1`, six receipts under `controls/receipts/` at `9bad1201`.
- C2 instrument: `corpus/evidence/round90/curation-r90.py:1` (ten legs, verdict before the summary, witness),
  `curation-r90-controls.py:1`, `curation-r90-mutants.py:1` at `8d9893b4`.
- C3 instrument: `corpus/evidence/round90/skill-tally-r90.py:1`; source opened this round S220 in
  `corpus/SOURCES.md:232` (GNU grep(1) `-x`), capture `corpus/captures/e6ec761219e8044b0e9e067a.txt` at `aa7d4223`,
  refetch row `2026-11-08T09:52:31Z`.
- Wave: `.ufo/waves/round-90/w1/` (13 seat reports), `w1-results.json`, `claim-falsification.tsv`,
  `w1-spec.json`/`w1-dispatch.json` at the landing commit.
- Integration: `corpus/lessons/round-90.md:1` (Gate, claims, six mistakes, spot-check intake, wave settlement,
  trends), SCORECARD round-90 block, LOG round-90 entry, QUALITY 196–202, `corpus/README.md` frontier line,
  `SKILL.md` tallies at `a45cbff6`.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| egress table for S220 (before the first fetch) | round-90 freeze | `af71d0a1` / `6ccf22b9` |
| claim freeze: seven instruments, expectations, before receipts, S220 row, pins, plan | round-90 freeze | `8d9893b4` |
| six control receipts re-emitted and pinned to the freeze revision | round-90 freeze receipts | `9bad1201` |
| S220 source capture (man7 grep page, HTTP 200) | round-90 freeze | `aa7d4223` |
| landing: SKILL tallies, lesson, SCORECARD, LOG, QUALITY 196–202, README frontier, wave evidence | round-90 | `a45cbff6` |
| landing-revision claim receipts (`after/*-landing.txt`, `after/c3-after.txt`, preflight) | round-90 | `64db6a83b8fd262076f80c8cb161fd659da0dac2` |

## Before → after measurements

**C1 — operability.** Counting command (the corrected literal command, Amendment 7):

```sh
L=/home/vgpnk/Projects/shokunin/chousa-shokunin; W=/fast/scratch/hyaku/chousa-r90/work
python3 -B "$L/corpus/evidence/round90/control-driver-r90.py" verify --root "$L" --repo "$L" \
  --rev 8d9893b42eb22690ea5f920ab87fd7e1810b847a \
  --receipts-rev 9bad12011187d114ba2c4588c5df08a21ab28145 --work "$W"
python3 -B "$L/corpus/evidence/round90/control-forgeries-r90.py" --root "$L" --work "$W" \
  --rev 8d9893b42eb22690ea5f920ab87fd7e1810b847a
```

Before: the round-89 driver prints `CONTROL_RECEIPTS=PASS` over its own rows and accepts all six forgery fixtures
(`FORGERY_REFUSED=0/6`; `controls/receipts/c1-prior-driver.txt`). After (measured at `a45cbff6`):
`COMMITTED_OK=6/6 EXACT_OK=6/6 PIN_OK=6/6 FRESH_OK=6/6 CONTROL_DRIVER_R90=PASS` with `SELF_PIN OK`, exit 0, and
`FORGERY_REFUSED=6/6 PRIOR_ACCEPTED=6/6 POSITIVE=pass`, exit 0 (`after/c1-verify-landing.txt`,
`after/c1-forgeries-landing.txt`). **Verified on the wording narrowed by Amendments 2, 3, 4, 7 and 9**: the wave
showed duplicate header keys are last-wins, the executed instrument bytes are unpinned, `EXACT_OK` is not a term of
`passed`, and the frozen command omitted `--work`; those states are named limits 4–6 and Amendment 7 carries the
runnable command.

**C2 — calibration (honest stop).** Counting commands:

```sh
python3 -B corpus/evidence/round90/curation-r90.py --root .
python3 -B corpus/evidence/round90/curation-r90-mutants.py --root . --work <scratch>
python3 -B corpus/evidence/round90/curation-r90-controls.py --root . --work <scratch>
```

Before: the round-89 counter prints `LEGS_MEASURED=8/8` with no `VERDICT fields_hold=1` token on the passing path
(`grep -c` → 0; `controls/receipts/c2-prior-landing.txt`, `after/c2-token-counts.txt`) and both substituted detectors
survive (`PRIOR_R89_SURVIVORS=2/2`; `controls/receipts/c2-subst-before.txt`). After (measured at `a45cbff6`):
`CURATION_R90=PASS`, `LEGS_MEASURED=10/10`, `VERDICT fields_hold=1` (`grep -c` → 2), `DETECTOR_WITNESS=8/8`;
mutants `MUTANTS_KILLED=10/10 COUNTER_DETECTED=9 BATTERY_DETECTED=1 PRIOR_R89_SURVIVORS=2/2`; controls
`CONTROLS=PASS FORGERY_REFUSED=7/7 PRIOR_REGRESSION=7/7` (`after/c2-*-landing.txt`). **The claim does not verify as
frozen**: its kill rule K2 fires — `R90ExecC2Forge` F1/F2 build two tree forgeries (a `## Located quotes` row outside
the parser's `Q`/3-cell shape; a cited source's `mined` → `rejected` status flip) that the full three-command kit
accepts at exit 0 (`w1/R90ExecC2Forge/t-nonq-row-*.txt`, `t-status-rejected-*.txt`). A kill rule is not a wording
clause and cannot be rewritten after a seat has scored (§9); the enforceable property and the round-91 repairs are
Amendment 8.

**C3 — freshness.** Counting command: `python3 -B corpus/evidence/round90/skill-tally-r90.py --root .` (it runs the
subject selftest itself). Before: `TALLY_ROWS=9 STALE_TALLIES=9/9 EXPECTED_CASES=283 EXPECTED_SKIPPED=0
OTHER_OCCURRENCES=3 SKILL_TALLY_R90=FAIL`, exit 1 (`controls/receipts/c3-before.txt`). After (measured at
`a45cbff6`): `TALLY_ROWS=9 STALE_TALLIES=0/9 EXPECTED_CASES=283 EXPECTED_SKIPPED=0 OTHER_OCCURRENCES=3
SKILL_TALLY_R90=PASS`, exit 0 (`after/c3-after.txt`). **Verified on the wording narrowed by Amendments 1 and 10**
(the three historical labels corrected; the expected-number clause is bound by the before+landing pair).

## Sources & frontier

Census before → after: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin chousa` → exit 0 both times; rows 218 → 219 (`corpus/evidence/round90/census-start.txt`,
`census-end.txt`); same five pre-existing `W04` warnings. Rows added by tier: tier A +1 (`S220`, docs, mined).
Rows touched old → new: `S220` is new; no existing row's `status`/`recheck`/`used-by` cell changed. Frontier rows
advanced: none — `S220` grounds an instrument rule, not a knowledge entry; `corpus/knowledge/*.md` is unchanged.
Gate: `GATE-RECORD S220 url=https://man7.org/linux/man-pages/man1/grep.1.html fetched=2026-11-08T09:52:31Z tier=A
decision=admit capture=corpus/captures/e6ec761219e8044b0e9e067a.txt
capture_sha256=5a5e69c56413ba682b1609cba2baacafb393ff6821d5b752938efc390fd12823 words=10 quote="Select only those
matches that exactly match the whole line."` (`corpus/lessons/round-90.md:11`;
`GATE_RECORDS files=1 records=1 ok=1 fail=0`, exit 0). The capture is committed at `aa7d4223`, after the wave tree,
so a verifier must read the Gate record at or after the landing commit. `S219` stays reserved to the round-89
fixture's mirror row and is not a registry row; the failed gnu.org attempt (curl rc 28) is a refetch row only.
Assimilation: none — no `merge/chousa/` entry was adopted this round. `considerthese/2026-11-07.md` proposal 1
("duplicate wins") is applied as C1's `DUPLICATE_KEY` leg and its `C-duplicate-key` forgery is the witness.

## Trend verdicts

- **expansion: unchanged** — `corpus/knowledge/*.md` unchanged; one mined registry row (S220) cited by the claims
  file, not by a knowledge entry.
- **quality: improved** — C1 and C3 verified with red-before witnesses (six forgery classes accepted by r89 and
  refused by r90; nine stale tallies re-derived to the tool's own verdict), and the round's own wave findings became
  QUALITY 196–202. C2's instrument gains are reported but not admitted (honest stop).
- **discernment: improved** — the wave fired C1's overstatement, C2's kill rule and two defects the clean tree hid
  (`UNENTAILED_TERM` double-count, the dispatch command form); the lane narrowed C1/C3, honest-stopped C2, and
  recorded every deviation in six `## Mistakes` rows and Amendments 1–10.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` Gates table
  (nine tallies re-derived this round), `corpus/evidence/round90/claims.md` (lane assertion).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round 90; C1/C2/C3 receipts under
  `corpus/evidence/round90/` (lane assertion).
- [~] Instructions executable by an agent without oral context — `bash tools/research-gate.sh --selftest`
  `PASS (283 cases, 0 skipped)`; `python3 -B tools/lane-preflight.py` `PREFLIGHT=8/8 FAILED=none ENV=none
  SKIPPED=none` (`after/preflight-landing.txt`) (lane assertion).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched; `R90ConnectorSiblings` reports
  zero sibling ownership overlap (lane assertion).

## Process notes

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Round shape: one v1 wave of 13 seats under `ufo-wave-policy.json` (band 8–16), attack share 6/13 = 46%; 0 dead; no
  residual call. The L1 held the canonical planner seat; no planner was dispatched (validator-frozen topology).
- Disclosures: (a) the freeze commit's receipts carry the provisional `f8fa55ec` pin and are re-emitted at the
  carrier `9bad1201` before any scored run (`R90SentinelScope` F2) — the scored set is the carrier's; (b) the wave
  context named a `--root <lane> --repo <clone>` form that the driver's self-pin rejects (`R90SentinelScope` F1);
  the claim's command is `--root . --repo .`, and the path-base repair is QUALITY 202/round 91; (c) the S220 capture
  lands at `aa7d4223`, after the wave tree.
- Prefile falsification: `PREFILE-FALSIFICATION: pass claims=3 rows=18 attack_seats=6 findings=0` exit `0`.
- Tool installs: none this round (no install, no upgrade).
- Open L0 questions: none opened this round; the carried fetch-scope, `merge/chousa/` id-drift and hold-out items are
  unchanged.
