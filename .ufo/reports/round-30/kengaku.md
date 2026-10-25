# kengaku — round 30 report (hyaku run 6, 2026-10-25)

Declared claims (frozen before any seat ran, `plans/round-30-claims.md`): **C1** coverage (lowest
non-retired, tie-break over novelty) — shokuknow assimilation round 2, the contamination-transparency
card admitted as an amendment; **C2** calibration — the five routed defects D1–D5 closed; **C3**
operability — the adoption gate validates quotes. Round shape: two v1 waves, **36 build + 33 falsify =
69 seats** (`scripts/hyaku/ufo-wave-policy.json`, band 32–64; both waves validated and dispatched as one
`task` call each).

## Work performed

- **C1** — admitted `corpus/knowledge/contamination-transparency-card.md` as the amendment round 29's
  refusal demanded: six sources re-opened on 2026-10-25 with located quotes and own captures
  (`.ufo/waves/round-30/build/R30SrcS081.md` … `R30SrcS086.md`), every staged anchor replaced (S081's was
  30 words and in neither HTML fetch; S082's `# Benchmark Governance` section does not exist in v2; S085's
  fullwidth quotes had been flattened), the field list mapped into the round-6 union table's columns with
  the delta stated as **one new field (S2)**, the entry's answerability questions relabelled **CG1–CG8**
  to stop colliding with `QUALITY.md`, and an `Extends` section naming both objects it extends.
- **C2** — D1 receipt committed at the path the round-29 report cites, carrying the report's seven-field
  line *and* the wave file's eight-field variant (`corpus/evidence/round29-attempt2/control-nothing.txt`);
  D2 kappa sentence narrowed to the scope its command measured, with the line-unit count re-derived
  (`corpus/lessons/round-29.md:231-236`); D3 lesson count 9→8 (`:194`); D4 addendum committed
  (`.ufo/waves/round-29/attempt2/build/R29a2CritEntry.md`, +22/0); D5 asymmetry recorded in the round-29
  expect file with its seven printed fields unmoved (`.ufo/waves/round-29/attempt2/adoption-expect.json`).
- **C3** — `plans/sources_adopt.py` gained a quote mode (`--quote-file`/`--artifact`): every quoted span in
  a row's anchor cell must be ≤25 words and a byte substring of a named capture, exit 6 over-long / 7
  absent / 4 structural / 2 unreadable beside the existing 3/4/5; the ten original cases keep their names
  and verdicts and five pre-existing invocations are stdout/exit identical
  (`.ufo/waves/round-30/falsify/R30FxGateRegression.md`).
- Frontier step: census before/after (`.ufo/waves/round-30/assimilation/`,
  `corpus/evidence/round30/census-{before,after}.txt`); id-collision check before any append (82 vs 175 →
  6 collisions, resolved by adopting only unheld ids); quarantine slice re-derived with per-row verdicts
  (`.ufo/waves/round-30/falsify/R30FxQuarantine.md`); two mistakes mined into `corpus/lessons/round-30.md`
  §Mistakes; one considerthese proposal landed as `QUALITY.md` Q20.
- Falsification: 33 seats produced 28 reports; twelve landed claims were falsified in the round's own bytes
  and repaired before the second commit (frontier instruction edited in place, "two new fields" overclaim,
  missing flip conditions, S084/S086/S083 count and normalisation errors, S082 title, registry blank lines
  splitting the table, a D1 receipt that answered a different defect, a D2 check made unsatisfiable by its
  own repair, a C1 counter purchasable for 159 bytes, a silently-ignored combined CLI invocation). Four
  limitations are disclosed rather than closed: the C3 25-word cap is inert for CJK (a 1200-character
  Chinese span counts 1 word and passes), a zero-row quote file exits 0, two C2 counter paraphrases
  survive, and 115 added gate lines are unexercised (simplifier delete list recorded) —
  `.ufo/waves/round-30/falsify/R30FxQuotes.md`, `R30FxCounterSelfGuard.md`, `R30SimplGate.md`.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| entry + six registry rows + README index/coverage/frontier rows, D1–D5 repairs, quote gate, defect counter, freeze controls | `LOG.md` §Round 30 items 1–5 | `623c1fc9b083a9b3def3b9f66f5518628e01b6a5` |
| falsify-wave repairs (byte-identical frontier instruction, corrected field delta, per-Q record, counter self-guard, registry placement and clause fixes) | `LOG.md` §Round 30 items 1–5 (re-verified paragraph) | `706ed3f2f3a19b2a4953de61d2dd4c40b28151cd` |
| landing receipts, measured landing block, SCORECARD/LOG final wording | `LOG.md` §Round 30 | `501d07074bd9cc5d09fc9908100fe72895df4415` |
| final wave evidence (late seat reports) + the six-row quote-mode receipt | `.ufo/waves/round-30/falsify/R30FxQuotes.md` §What a green receipt does not cover | `6f6d6c98b5be5e99deee81de1a90a759651583bc` |

Lane HEAD at report time: `6f6d6c98b5be5e99deee81de1a90a759651583bc` (pushed; `jj-lane.sh state` →
`local=remote`, `ahead=0`).

## Before → after measurements

| claim | counting command | before | after | measured at |
|---|---|---|---|---|
| C1 | `python3 plans/adoption_check.py --expect .ufo/waves/round-30/adoption-expect.json --census` | `entries=0 indexed=0 cited_rows=0 rows_present=0 rows_mined=0 usedby_ok=0 census=ok`, exit 1 (`.ufo/waves/round-30/claims/control-nothing.txt`) | `entries=1 indexed=1 cited_rows=6 rows_present=6 rows_mined=6 usedby_ok=1 census=ok`, exit 0 (`corpus/evidence/round30/adoption-after.txt`) | `706ed3f2` |
| C2 | `python3 plans/round30_defects.py --lane .` | `defects=5`, exit 1 (`.ufo/waves/round-30/claims/defects-before.txt`) | `checks=5 defects=0`, exit 0 (`corpus/evidence/round30/defects-after.txt`) | `706ed3f2` |
| C3 | `python3 plans/sources_adopt.py --selftest` | `cases=10 failed=0`; `--quote-file/--artifact` → argparse exit 2 (`.ufo/waves/round-30/claims/gate-before.txt`) | `SELFTEST cases=14 failed=0`, exit 0 (`corpus/evidence/round30/gate-selftest-after.txt`) | `706ed3f2` |

Registry 82 → 88 rows (tier A 76→79, B 4→7), knowledge files 38 → 39, index rows 38 → 39. Counter
hardening control: a 7-line stub entry bought the old C1 pass line for 159 bytes; it now exits 1
(`corpus/evidence/round30/counter-hardening-control.txt`). Q13: `gate_timing_check.py --lesson
corpus/lessons/round-30.md --commit 706ed3f2…` → `admissions=1 passed=1 failed=0 second-seat-reports=31`,
exit 0.

## Sources & frontier

`corpus/SOURCES.md` rows before → after: **82 → 88**, counting command
`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` (baseline → tip). Rows added by tier: **A
76 → 79** (S083, S084, S086), **B 4 → 7** (S081, S082, S085), C unchanged at 2. Rows touched old→new:
S081–S086 (new, `mined | 2026-10-25 | 180d | used-by corpus/knowledge/contamination-transparency-card.md,
corpus/lessons/round-30.md`); no existing row's status, recheck or used-by changed
(`git diff --numstat <baseline> -- corpus/SOURCES.md` → 6 insertions, 0 deletions before the placement
fix). Census: fleet census exit 0 both ends, same 14 `W04` warnings
(`corpus/evidence/round30/census-before.txt`, `census-after.txt`). Frontier rows advanced: bullet 2
("Contamination transparency cards") — **partly discharged** (card format + CG1–CG8 gate landed; releases
on hidden-test governance, a runtime judge, and card adoption by any benchmark stay open).
Assimilation: one theme, one entry, six rows; the remaining 63 staged entries and 169 staged rows were
refused this round with reasons and flips (`corpus/lessons/round-30.md` §Gate).

## Trend verdicts

- **expansion: improved** — registry 82→88, knowledge 38→39 with index parity 39/39, and a frontier
  bullet moved from unopened lead to a landed amendment; bounded by the fact that the coverage/surfaces
  leg did not move (no `PROVINCE.md` round-30 section).
- **quality: improved** — a ten-repair falsification pass over the round's own bytes, a quote valve on
  the adoption gate with mutants killed, a defect counter whose own neutering is now visible
  (`checks=5 failed=0`), and Q13 passing at the landing commit with 31 second-seat reports in tree;
  bounded by three disclosed limitations (CJK cap, two counter paraphrases, 115 unexercised lines).
- **discernment: improved** — the round refused the staged card's own anchors (30-word quote, a
  section that does not exist, flattened fullwidth quotes) and kept its own overclaim out of the entry
  ("two new fields" → one field, one placement retired); the quarantine slice was re-derived with two
  per-row verdicts; the cost is that four of the round's self-assessments needed a falsify seat to
  correct them.

## SHONEN

- [~] SKILL.md decision tables/error patterns/checklists/cited sources — `SKILL.md` untouched this round;
  the round's decision surface is `corpus/knowledge/contamination-transparency-card.md` §How kengaku
  applies it, not SKILL.md.
- [~] one end-to-end domain task executed and logged — `LOG.md` §Round 30 items 1–3.
- [~] instructions executable without oral context — `corpus/lessons/round-30.md` §Landing (four commands,
  their exits) plus `corpus/evidence/round30/`.
- [~] no cross-domain bleed, PROVINCE.md accurate — `.ufo/waves/round-30/build/R30ConnSibling.md` and
  `.ufo/waves/round-30/falsify/R30FxSibling.md`: no sibling surface claimed; `PROVINCE.md` unchanged
  (no round-30 section landed, stated in the coverage verdict).

## Extras

- **Stale-lane:** none — respawn-per-round driver; no other kengaku mission is open. The mission ran long
  (two waves, 69 seats) but was progressing throughout (commits `623c1fc9`, `706ed3f2`, `501d0707`).
- **Seats:** wave 1 36 (10 scout, 7 reviewer, 6 executor, 4 scribe, 3 critic, 2 connector, 2
  mutation-tester, 1 revenger, 1 simplifier); wave 2 33 (12 scout, 8 reviewer, 5 critic, 5 executor, 1
  mutation-tester, 1 connector, 1 revenger) — 16/33 attack roles. **Dead seats: none.** `R30DraftEntry`
  (scribe) never landed a report — unlanded, not dead, and its draft was not used. The wave-2 dispatch was
  refused twice at the host job limit ("Background job limit reached (100)") and resent unchanged once a
  slot settled; the harness appended `-3` to agent ids, so the wave-2 agent ids are not recorded in the
  falsify registry (`agentId: null`), while report paths match the registry names.
- **L0 questions:** none opened. **Tool installs:** none (pacman paused and untouched; `npx marked` and
  `uv run --with pypdf/PyMuPDF` by seats ran from caches/venvs, recorded in their reports).
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only driver-owned
  files (`.ufo/state/*`, `watchdog.log`, `scripts/hyaku/*`, `.scratch/`); no seat wrote into the fleet
  root, so nothing was relocated.

## Erratum (appended 2026-10-25, after the report's first commit — the filed bytes above are unchanged)

Lane corrections landed after this report's first commit, all as new commits (never as amendments):
`d0253c52` (claims change record: the C1 counter was hardened in-round, with which body produced which
receipt; S084 locator), `5cd92295` (**Q20 is now an executable check** with the roster closure over the
touched gate, and its two wrong limits corrected — the detector is the `grader.py` PASS-line count, not
the pinned integer, and R6 defines non-author by roster id, not by workflow run; the C2 counter now
judges **committed** bytes for D2/D3/D5, requires exactly one control line, and requires the addendum
**body**, not only its header), `baa53e70` (final seat reports, six-row quote-mode receipt) and
`bdcd7bed` (the complete-set Q10 review report, which also carries a `VERDICT:` line).
**Lane tip at this erratum: `bdcd7bed667ce5cf2b6053566d2eeb22e5bf5dbe`** (pushed, `local=remote`);
the hash this report cited earlier (`6f6d6c98…`) remains an ancestor. Re-measured at the tip: C1
`entries=1 indexed=1 cited_rows=6 rows_present=6 rows_mined=6 usedby_ok=1 census=ok` exit 0; C2
`checks=5 defects=0` exit 0 and `--selftest checks=5 failed=0`; C3 `cases=14 failed=0`; Q13 at
`5cd92295` → `admissions=1 passed=1 failed=0 second-seat-reports=31`, exit 0. The four disclosed
limitations stand; the Q20 and counter defects the wave found are now closed rather than only recorded.

Second erratum item (2026-10-25, after the committed bytes above and the first erratum): a falsify seat
found that **S086 is not peer-reviewed** — the society's own submission page states the proceedings are
"published without peer review". The entry's attribution, the registry row's tier (A → **B**, the same
call this lane makes for preprints) and the tier tallies were corrected at lane commit
`a6a9b57a…`/the S086 correction that follows it: **tier A 76 → 78, tier B 4 → 8** (not the 79/7 the
measurement table above reports), with the C1 counter re-issued unchanged
(`entries=1 indexed=1 cited_rows=6 … census=ok`) because tier is not one of its fields. The Q4 falsifier
now names its unit, population and observation. The Q5 label and the tier count in this report are
superseded by that commit; the claim, its predicate and the axis verdict are not.
