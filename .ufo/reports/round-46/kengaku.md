# kengaku — round 46 (hyaku run 9, 2026-10-27; attempt 1, L1 `KengakuR46`)

Lane tip `a68afb2fffd66c8bb2c4687fd40b7779f2761743` (pushed; `git ls-remote origin refs/heads/master` prints it).
Base `64ba8385ea10af1b78d367dcb242b92d97062af7` (round-45 closure tip). Claims `kengaku-shokunin/plans/round-46-claims.md`.

## Work performed

Declared claims (3): **C1 calibration** — the fixture fence's advertisement vs its observed behaviour under a
re-frozen counter that hides its own names (QUALITY Q39; routed: "re-freeze C1 with a path-hidden control");
**C2 depth** — round 45's false line-level detail superseded and marked (routed: S152–S154, anchor-line gate check,
predictor lone-CR gap); **C3 coverage** (lowest axis, tied with novelty at 7) — the pinned TB2 `polyglot-c-py` grader
admitted with an executed probe. Verdicts: **C1 predicate met, not admitted** (frozen wave-2 kill rule fires);
**C2 predicate met** (one named counter limit); **C3 not admitted** (frozen counter V7/V8 defects).

- Stage-1 freeze: C2 whole (counter `plans/round46_c2_verify.py`, gate `plans/anchor_line_check.py`, 5 controls), C1/C3
  predicate sentences + controls + kill rules — commit `fd4129eb`.
- Wave 1 (35 seats) built: C1 counter (`R46ExecC1Counter`, closes round-45 bypasses B1–B6 except io_uring), 10 converted
  held-out modules (`plans/refusals46/` f11–f20), 12 sealed modules (4 critic seats), three fence variants, C2 rows +
  entry repair, C3 captures/probe/spec/counter/filler package/entry/rows/index, `plans/log_appendonly.py`, attacks —
  reports `kengaku-shokunin/.ufo/waves/round-46/w1/*.md` (35/35 present).
- Stage-2 instruments `cf7de6af` (C1 `P=65 R=20 S=12`, C3 `V=13`, DECISIVE re-keyed, spec pin with receipt digest
  masked), amendment `4fdeebaa` (`plans/round-46-claims.md` §Freeze amendments), C1 control receipts `7768716c`
  (21 controls, all `PREDICATE C1 fail`; base fence `contradicted=22`), C2 control replays + C3 controls
  (`.ufo/waves/round-46/claims/stage2_controls.py`, all fail).
- C1 landing `420eec9f` (fence variant A, allowlist, no git child): `integrate/c1-landing.txt` `PREDICATE C1 pass`.
- C2 landing `c1ec334c` (rows S157–S165, entry repair): `integrate/c2-landing.txt` `PREDICATE C2 pass`.
- C3 first recorded probe run `8d7f74ce` (after the amendment): `cases=18 observed_pass=7 observed_fail=11 mismatches=0`,
  `regrade cases=18 differ=7`; package `e9d20145`; `integrate/c3-landing.txt` `checks=13 defects=2`, `PREDICATE C3 fail`.
- Bookkeeping `85a40be5`: lesson `corpus/lessons/round-46.md`, QUALITY Q40, LOG D1 correction + round-46 entry, SCORECARD
  round-46, 11 routed-ledger rows (`corpus/routed-findings.jsonl` R45-S5-*), `plans/log_appendonly.py`.
- Wave 2 (32 seats) falsified at `42d5043a`; verdicts + appended corrections `264b7757`; final-tip receipt `a68afb2f`
  (`integrate/final-tip.txt`: C1 pass, C2 pass, C3 fail at `264b7757`).
- No-harm (`integrate/noharm.txt`, `e9d20145`): round-45 C2 counter `checks=11 defects=0`; round-45 C1 counter
  `PREDICATE C1 pass`; `anchor_digest_check rows=165 tokens=71 defects=0`; `routed_open=24`; census ok. Wave-2
  `R46W2NoHarm`: 8 legs, 0 red at tip or base.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| claims + anchor-line gate + C2 counter + controls | LOG round 46 (claims line) | `fd4129eb` |
| C1/C3 stage-2 instruments, refusals46/sealed46, polyglot captures/probe/dry/spec/filler | LOG round 46 | `cf7de6af` |
| stage-2 freeze amendment + C2/C3 control receipts | LOG round 46 | `4fdeebaa` |
| C1 control receipts | LOG round 46 (C1 bullet) | `7768716c` |
| C1 repaired `plans/fixture_fence.py` | LOG round 46 (C1 bullet) | `420eec9f` |
| C3 probe receipt + spec receipt digest | LOG round 46 (C3 bullet) | `8d7f74ce` |
| C2 rows S157–S165 + password-recovery entry repair | LOG round 46 (C2 bullet) | `c1ec334c` |
| C3 package (entry, S166–S172, README, PROVINCE) | LOG round 46 (C3 bullet) | `e9d20145` |
| wave-1 evidence + landing receipts | LOG round 46 | `f1871acc`, `42d5043a` |
| lesson, Q40, LOG D1 correction, SCORECARD, routed rows, log_appendonly | LOG "Round 45 LOG correction" + round 46 | `85a40be5` |
| wave-2 evidence, verdicts, appended corrections, census after | LOG "Round 46 wave-2 results" | `264b7757` |
| final-tip receipt | LOG round 46 wave-2 | `a68afb2f` |

## Before → after measurements

- **C1** `python3 plans/round46_c1_verify.py --lane .` — before (base fence, `claims/control-c1-base-fence.txt`, measured
  `cf7de6af`): `REFUSALS total=20 clean=10 leaked=10`, `SEALED total=12 clean=0 leaked=12`, `CALIBRATION advertised=32
  contradicted=22`, fail → after (`integrate/c1-landing.txt`, `420eec9f`; again `integrate/final-tip.txt`, `264b7757`):
  `PINS total=65 mismatched=0`, `REFUSALS total=20 clean=20`, `SEALED total=12 clean=12`, `HONEST fixtures=104
  admitted=104`, `contradicted=0`, `PREDICATE C1 pass`. Kill rule (frozen): wave-2 held-out modules admitted = 3
  (`w2/R46W2C1HoArgv.md` 2, `w2/R46W2C1HoPaths.md` 1) ≥ 2 → **not admitted**. The authoring seats say none of the three
  reaches outside `d`; the kill rule did not carve that out, so the literal count stands (operator may rule).
  Also: 9/9 novel honest fixtures refused (`R46W2C1HoHonest`), fence mutants 2/13 caught, counter mutants 1/6.
- **C2** `python3 plans/round46_c2_verify.py --lane .` — before (`claims/control-c2-nothing.txt`, base `64ba8385`):
  `A live=8`, `B disagree=6`, `C source_ranges_bad=4 errata_marks=0/5`, fail → after (`integrate/c2-landing.txt`,
  `e9d20145`; `final-tip.txt`, `264b7757`): `A live=0 repaired=8 base_changed=0`, `B disagree=0`, `C source_ranges_bad=0
  errata_marks=5/5`, `D selftest exit=0`, `PREDICATE C2 pass`. Named limit (`w2/R46W2C2Bypass.md`): leg C passes on the
  five bare errata tokens; legs A/B still require the real repairs; `R46W2C2Entry` found the errata true (0 defects,
  predictor 0/200 disagreements).
- **C3** `python3 plans/round46_c3_verify.py --lane .` — before (`claims/control-c3-base.txt`, `cf7de6af`): `checks=13
  defects=8`, fail → after (`integrate/c3-landing.txt`, `e9d20145`): `checks=13 defects=2` (V7: frozen tags
  `both-print`/`toolchain` violated by no frozen case; V8: `control-c3-echo` ran the gate's P10 before the receipt),
  `PREDICATE C3 fail`. Counted coverage move: knowledge files 52 → 53 (`ls corpus/knowledge | wc -l`), §Frontier
  `11 of 89` → `12 of 89`, rows 149 → 165.

## Sources & frontier

`SOURCES.md` rows 149 → 165: `git show <rev>:corpus/SOURCES.md | grep -cE '^ {0,3}\| *S[0-9]{3}'` at `64ba8385` → 149,
at `a68afb2f` → 165. Added by tier: A 16 (S157–S165 superseding rows under Q34 for S108, S149–S156; S166–S172
`polyglot-c-py` at `2fd12b88`, opened 2026-10-27). Rows touched old→new: none (no `status`/`recheck`/`used-by` change;
superseded rows keep `mined` and `used-by`, precedent S025/S036). Frontier advanced: TB2 task graders 11 → 12 of 89.
Census: start `.ufo/waves/round-46/claims/census-before.txt` (15 W04, `kengaku ok`, exit 0); end
`.ufo/waves/round-46/integrate/census-after.txt` (`kengaku ok`, exit=0). Sourced claim: C3 rests on S166–S172 opened
this round; lesson `## Gate` carries URL, access date and located quote per new row plus two rejects (Docker Hub tag
page; unpinned `main` ref). Mined mistakes: `corpus/lessons/round-46.md` §Mistakes (10 rows; new criterion Q40, shown
able to fail on the round-46 dry table vs round 45's). Assimilation: none. considerthese: `2026-10-26.md` proposal 2
mined as C3's V13 filler control.

## Trend verdicts

- `expansion`: **improved** — one new entry on uncovered ground (`corpus/knowledge/tb2-polyglot-c-py-grader.md`, 52 → 53)
  citing 7 mined tier-A rows opened this round; frontier 11 → 12 of 89. Its own counter does not admit it (C3 V7/V8).
- `quality`: **improved** — round-45 false detail superseded by stronger rows (S157–S165) and the entry's predictor
  corrected and marked (`## Errata (round 46)`), re-verified by `PREDICATE C2 pass` and `R46W2C2Entry`; one new
  overclaim in the C3 entry found by wave 2 and marked in-round (`## Errata (round 46, wave 2)`).
- `discernment`: **unchanged** — the C1 calibration claim is not admitted (kill rule, over-refusal 9/9, mutants 2/13);
  Q40 adds a grounded criterion from this round's own mistake; the outside spot-check is the closure's.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `kengaku-shokunin/SKILL.md` (unchanged this round)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `kengaku-shokunin/LOG.md:7`; this round's executed probe `corpus/evidence/round46/polyglot-c-py-probe.txt`
- [~] Instructions executable by an agent without oral context — `corpus/lessons/round-8-aggregator-box3-coldrun.md:48`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:129`; round-46 paragraph appended (C3)

## Round shape, seats, conformance

- Shape: two v1 waves (policy `ufo-wave-policy.json`). Wave 1: 35 seats (executor 11, critic 8, scribe 6, reviewer 4,
  scout 2, connector 2, mutation-tester 1, sentinel 1). Wave 2: 32 seats (reviewer 14, critic 10, mutation-tester 5,
  sentinel 1, executor 1, connector 1). Round total 67; no residual call. Planner seat: the L1.
- Dead seats: none died; 4 wave-2 seats left no report file (`R46W2C1Advert`, `R46W2Scorecard`, `R46W2C2Mut` — no mutant
  run, `R46W2C2Rows` — unfinished output); their outputs are recovered verbatim as `w2/<seat>.recovered-output.md`.
  The C2 wave-2 row re-open and C2 mutation items are therefore unattacked in wave 2.
- Misroot: `R46CritC1Freeze` wrote to a misspelled fleet-root path; the orchestrator copied it byte-identical into the
  lane and quarantined the stray (`.tower/quarantine/fleet-root-strays-20261027T0600/`). Final sweep:
  `git -C /home/vgpnk/Projects/shokunin status --porcelain` empty before this report.
- Disclosed order issues: the C3 counter seat's V11 runs executed the captured grader on generated states before the
  freeze (disclosed in the amendment); the stage-2 `control-c3-echo` executed the probe via gate P10 before the receipt
  (caught by V8; lesson + Q40).
- Inherited state: none (`jj-lane.sh state` clean at start; no earlier attempt of round 46).
- Tool installs: none by the L1; none reported by seats.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Open L0 questions: none new; `kengaku | round-33` (coverage cap) still open.
