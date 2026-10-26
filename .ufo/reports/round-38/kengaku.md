# kengaku — round 38 report (hyaku run 8, 2026-10-26)

Lane `/home/vgpnk/Projects/shokunin/kengaku-shokunin`, branch `master`. Baseline as read at start `fc1174f52b150999bef91f2e81da78732ca0eb9f`
(the round-37 L1 then landed `21e6251b` 3 s before the freeze, so the freeze is that commit's child — lesson header);
frozen claims `plans/round-38-claims.md` (freeze `e0a378539a45cc9388c66cfba22f44275131de23`); first recorded probe run
`e95cf5500b6c13305cc41b8532ae07fb2c9dcd7b`; final lane hash `1fa7af4528a5a5fe4e15a630caf33bacee7a05b9` (`git ls-remote origin refs/heads/master` → that hash).
L1 agent id `KengakuR38`; the L1 holds the canonical planner seat (the wave validator rejects `planner`; the round-39
planning data-walk rode scout `R38PlanNext`).

## Work performed

Declared claims (2), frozen with red controls before any battery38 fixture and before the first recorded probe run:

- **C1 — calibration (owned, 8):** the gate behaviours `plans/pkg_gate.py` advertises that the round-37 battery does not
  demonstrate — 22 frozen mutants N01–N22 (16 round-37 wave-2 extra-mutant survivors, one diagnostic, six freeze-excluded
  shapes, one overlap; the claims text says "13", erratum in the lesson),
  silence and mirror directions, an **attributed** kill rule, counter `plans/round38_c1_verify.py`.
- **C2 — coverage (lowest non-retired axis, 7, tied with novelty; frozen tie-break):** the pinned Terminal-Bench 2.0
  `build-pmars` grader admitted as `corpus/knowledge/tb2-build-pmars-grader.md` with a 22-case bubblewrap probe
  (`plans/build_pmars_probe.py`), rows S115/S116; counter `plans/round38_c2_verify.py` (inputs pinned; V7 derives map
  labels from all violating cases).

Work items:

- Protocol load: the round prompt, `skill://godspeed`, `skill://swarm`, AXES, SCORECARD `### Planned (round 38)`
  (`SCORECARD.md:1307-1312` at baseline), the round-37 report and non-author spot-check (`corpus/lessons/round-37-verifier-spotcheck.md`
  §5, routed D1–D7), round-37 wave-2 reports (`.ufo/waves/round-37/falsify/F37XMut*.md`), `R37PlanNext.md`.
- Freeze `e0a37853`: claims, both counters, the probe and its frozen case table
  (`corpus/evidence/round38/build-pmars-dry-cases-freeze.txt`, `cases=22 predicted_pass=7 predicted_fail=15`, `violates=` tags),
  five captures + `SHA256SUMS`, controls in `.ufo/waves/round-38/claims/`: C1 nothing `killed=0 survived=22`; C1 gate-edited
  `invalid=22`; C2 nothing `checks=7 defects=4`; C2 skip `checks=7 defects=2`; census-before exit 0, 15 W04;
  `frozen-digests.txt`. Disclosed in the claims (`:8-15`): the C2 skip-control's P10 executed the frozen probe once at control
  time, output discarded unread (a recurrence of round 37's mistake, mined below).
- First recorded probe run `e95cf550` on a clean clone of the freeze: `cases=22 observed_pass=7 observed_fail=15 mismatches=0`;
  a second run byte-equal.
- Wave 1 (spec/dispatch `2c5f4e0b`, 40 seats): 40 reports, 0 dead (`.ufo/waves/round-38/build-results.json`; committed `8c7422d7`).
- C1 battery (`dc0cdb54`): twelve executor seats wrote `plans/battery38/` (12 modules, 22 fixtures). Landing on a clean clone of
  `d93b7d68` (`.ufo/waves/round-38/integrate/measure-final.txt`): `PINS total=14 mismatched=0`, `BATTERY fixtures=86 wrong=0
  renamed_disagree=0 sidechannel=0`, `MUTANTS total=22 killed=21 survived=1 invalid=0 null_detected=0`, `PREDICATE C1 fail`.
- **C1 freeze defect (found by `build/R38BatD5.md` within the first wave-1 hour):** N21 (`sums.splitlines()` →
  `sums.splitlines()[:1]` in the D5 manifest lookup) is frozen as `silence`, but it makes D5 stricter on every input, so no
  battery can satisfy the silence rule. The L1 did not relabel it after scoring; C1 is an honest stop. New
  `plans/mutant_direction_check.py` (QUALITY Q29) flags it: `DIR N21 D5 declared=silence observed=mirror MISLABELLED`,
  `DIRECTIONS total=22 mislabelled=1`, exit 1 (`integrate/direction-check.txt`). Post-hoc diagnostic, not the frozen rule:
  with N21 relabelled `mirror` in a scratch copy the landed battery kills 22/22 (`integrate/n21-mirror-diagnostic.txt`).
- C1 limits found in wave 1: a two-fixture junk module that monkeypatches the counter's in-process `run_gate` reaches
  `killed=20` with `wrong=0 sidechannel=0` (`build/R38CritClaims.md` §2; `build/R38CritC1Counter.md` H1); 3 of the 22 `adv`
  cells name no advertising sentence, and the claims' source arithmetic (13+1+6) does not reach 22 (`R38CritClaims` §1);
  `build/R38RevCounters.md` six minor/medium defects (V6 runs an unpinned fleet script; mirror attribution does not
  require an accept fixture; round-35 package bytes unpinned).
- C2 package (`dc0cdb54`, `d93b7d68`): `R38PkgEntry` drafted entry, rows and README lines (its clone `checks=7 defects=0`);
  the L1 integrated them with the prior-art section rewritten from `R38ScoutPriorArt` (14 hits; TB2 #59 is the oracle's apt pin;
  an LLM audit names the provenance gap but calls `ldd` reliable) and `R38ScoutUpstream` (pin = `main`; TB2.1 moved the task,
  grader byte-equal), "14-line" corrected to 21-line, and a contestable-tags subsection from `R38CritProbe` §3 (frozen tags
  unedited; `canned-x11-dlopen`'s `no-x11` tag is load-bearing for one label). The L1 opened `environment/Dockerfile:9`
  (warriors copied into `/app`) and cites it: the probe's seven passes are fabricated artefacts by construction.
  Landing: `checks=7 defects=0`, `PREDICATE C2 pass`. Independent: real pytest 8.4.1 22/22 (`R38CritPytest`), re-derivation
  22/22 + 3/3 extra (`R38CritIndep`), probe mutants 5/5 change the receipt (`R38MutProbe`), counter mutants 11/11 caught
  (`R38MutC2Counter`). Limit: an informed filler package also reaches `checks=7 defects=0` (`R38CritC2Counter` §1).
- Frontier / routed (`d93b7d68`): Q28 + appended `## Errata (round 38)` on `tb2-git-webserver-grader.md` (D2; `R38MapErratum`
  controls B/C show V7 red on a witness-picked label; `R38MapRetro` finds 2 disagreeing rows in the round-37 map);
  `plans/anchor_digest_check.py` binds each digest to its own row's capture (D3; `R38AnchorBind`: M4b/M5/M6/M7 →
  `digest-wrong-capture`, tip `rows=109 tokens=17 defects=0`); `plans/ledger_tip.py` binds an absent branch ref and refuses
  with exit 2 (D4; `R38LedgerTip`); PROVINCE sibling report-out, 16 surfaces with file:line (D6; `R38SiblingCite`); D1 was
  closed by the round-37 L1 (`21e6251b`); SKILL build-provenance decision table (13 rows) + five registry rows.
- Assimilation: `considerthese/2026-10-25.md` proposal 2(c) landed as `plans/tip_receipts.py` (`R38TipReceipts`): at the tip
  `receipts=24 byte_equal=4 differ=0 skipped=20`, tamper control `differ`.
- Docs (`a022ae60`): lesson `corpus/lessons/round-38.md`, SCORECARD round-38 section (+3 capability rows, `### Planned (round 39)`),
  LOG entry.
- No-harm at the landing tip (`measure-final.txt`): round-37 C1 `killed=55/55` pass, round-37 C2 pass, round-36 C2 pass, anchor
  check `defects=0`, ledger-tip `mismatches=0`, census exit 0, `sha256sum -c frozen-digests.txt` 8/8 OK, tip receipts 4/4 equal.
- Wave 2 (falsify, 34 seats, `falsify-dispatch.json` validated against `8c7422d7`, committed `4d00e6d8`): handed to the dispatcher after WAVE-DONE build. **I filed this report before WAVE-DONE falsify** because the run's request budget forced the round to close; no wave-2 finding is integrated, and the closure should read `.ufo/waves/round-38/falsify/*.md` (seats still writing at filing; 16 seat dirs present, 0 reports). Lane tip re-measured at `10d2e977` (`integrate/measure-tip2.txt`, same numbers) and the round-37 attribution audit at the tip prints `ATTRIBUTED 55/55 UNATTRIBUTED=0` (`integrate/r37-attribution-at-tip.txt`).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all` lists no file written by a
  kengaku round-38 seat (the fleet-root entries are orchestrator-owned: `.ufo/prompts/closure/kengaku-round-37.md`,
  `.ufo/state/kengaku.report-baseline`, `.scratch/`, `.tower/`). Scratch: seat `R38CritC1Counter` left
  `/fast/scratch/hyaku/kengaku-r38/R38CritC1Counter2` (734 MB) — a defect of that seat; the L1 removes
  `/fast/scratch/hyaku/kengaku-r38` after landing.

Round shape: two v1 waves. Wave 1 has 40 seats: 16 executor, 7 scribe, 6 critic, 4 scout, 2 reviewer, 2 mutation-tester, 2 connector, 1 sentinel; m_flash roles 30/40, attack 10/40, 0 dead (40/40 reports). Wave 2 has 34 seats: 11 critic, 7 reviewer, 7 executor, 5 mutation-tester, 2 connector, 1 scout, 1 sentinel; m_flash roles 19/34, attack 23/34; outcome not integrated at filing. Round total 74 seats, no residual call.

Stale-lane: respawn-per-round driver, no other mission of this lane open.

Tool installs: none on the host. biopython 1.85 via `uv run --with` (gate P10, ephemeral uv cache, PyPI); pytest 8.4.1 +
pytest-json-ctrf 0.3.5 into scratch `uv venv -p 3.13` by seats `R38CritPytest` and `R38PlanNext` (PyPI via uv, removed with
the scratch); gcc 16.2.1, bubblewrap 0.13.1 and libX11 were already installed. pacman not touched.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `e0a37853` | freeze: claims, C1/C2 counters, probe, dry table, captures, controls | round 38 entry ¶1 |
| `e95cf550` | first recorded probe receipt | ¶1, C2 bullet |
| `2c5f4e0b` | wave-1 spec and dispatch | ¶1 |
| `dc0cdb54` | `plans/battery38/` (12 modules), `plans/mutant_direction_check.py`; C2 entry, S115/S116, README | C1, C2 bullets |
| `d93b7d68` | Q28 + round-37 entry errata, Q29, anchor binding, ledger-tip refs, `tip_receipts.py`, PROVINCE, SKILL, entry tags note | Frontier/routed, Assimilation bullets |
| `a022ae60` | lesson, SCORECARD and LOG round-38 sections, landing measurement, direction-check receipt | entry |
| `8c7422d7` | wave-1 reports and results, census after | — |
| `4d00e6d8` | wave-2 spec and dispatch | — |
| `10d2e977` | post-hoc N21 mirror diagnostic | — |
| `1fa7af45` | tip re-measure, round-37 attribution audit at tip, falsify ready marker | — |

## Before → after measurements

- **C1 (calibration)** — `python3 plans/round38_c1_verify.py --lane .` on a clean clone.
  - Before, at freeze (`claims/control-c1-nothing.txt`): `PINS total=14 mismatched=0`, `BATTERY fixtures=64 wrong=0
    renamed_disagree=0 sidechannel=0`, `MUTANTS total=22 killed=0 survived=22 invalid=0 null_detected=0`, `PREDICATE C1 fail`, exit 1.
  - After, at `d93b7d68` (`integrate/measure-final.txt`): `BATTERY fixtures=86 wrong=0 renamed_disagree=0 sidechannel=0`,
    `MUTANTS total=22 killed=21 survived=1 invalid=0 null_detected=0`, `PREDICATE C1 fail`, exit 1.
  - Verdict: **frozen predicate NOT met — honest stop.** Mismatch count 22 → 1 observed (19 → 1 over advertised classes per
    `R38CritClaims`), but the claim is judged on its frozen predicate. Score **8 → 8 held**.
- **C2 (coverage)** — `python3 plans/round38_c2_verify.py --lane .` on a clean clone.
  - Before (`claims/control-c2-nothing.txt`): `checks=7 defects=4` (V2, V3, V4, V7), exit 1.
  - After, at `d93b7d68`: `checks=7 defects=0`, `PREDICATE C2 pass`, exit 0; probe `cases=22 observed_pass=7 observed_fail=15
    mismatches=0`.
  - Verdict: **frozen predicate met**. Score **7 → 7 held** (L0 cap). Admission also rests on the wave-1 non-author-model re-reads (pytest parity, independent re-derivation) and is pending the wave-2 re-reads.
- **Frontier fix shown able to fail:** `python3 plans/mutant_direction_check.py --lane .` → `mislabelled=1`, exit 1 on N21;
  V7 Control B (`build/R38MapErratum/controls.txt`) → `labelled enforced, receipt derives partly`.

## Sources & frontier

- Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` gives 107 → 109. Tier A +2
  (S115 `build-pmars/tests/test_outputs.py`, S116 `build-pmars/instruction.md`, terminal-bench-2 @ `2fd12b88`), both `mined`,
  both used by the new entry; opened 2026-10-26.
- Rows touched old→new: none.
- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`: before exit 0,
  15 W04 (`claims/census-before.txt`); after exit 0, the same 15 W04, `kengaku ok` (`integrate/census-after.txt`).
- Frontier advanced: README §Frontier TB2 clause narrowed for a fourth task (4 of 89 read); one new executed edge class (graded
  state = a built artefact plus a source tree).
- Sourced claim: C2 (S115, S116 opened this round).
- Mined mistakes (`corpus/lessons/round-38.md` §Mistakes): the N21 direction freeze defect (fix `mutant_direction_check.py`,
  shown red); the order-of-operations recurrence (lint shown red on the freeze); the witness-picked map label (D2; V7/Q28,
  shown red); the claims' source arithmetic.
- Assimilation: `considerthese/2026-10-25.md` proposal 2(c) → `plans/tip_receipts.py`. `merge/kengaku/`: adopted nothing; re-screen
  2 admit-candidates (card family, deferred: no frozen claim names them), 5 hold, 5 refuse (`build/R38MergeRescreen.md`); id
  collisions 31 (`.ufo/waves/round-38/assimilation/collisions`), moot — nothing appended; quarantine slice 2 rows, not
  hand-checked because nothing is adopted.

## Trend verdicts

- **expansion — improved.** One admitted entry on Frontier ground (a fourth TB2 grader, the first whose graded state is a built
  artefact plus a source tree), S115/S116 `mined`, three capability rows entered with demonstrations
  (`build-provenance-grader-probe`, `mutant-direction-check`, `tip-receipt-validator`). One instance and one edge class, not breadth.
- **quality — improved.** Routed defects closed with receipts: D2 (errata + Q28, V7 shown red on a witness-picked label), D3 (anchor
  binding, cross-capture fixtures now caught), D4 (ledger-tip detached refs), D6 (sibling report-out); the new entry carries its
  contestable tags and fabricated-by-construction limit instead of hiding them. Caveat: wave-2 re-reads not integrated.
- **discernment — unprovable-but-better at most; not `improved`.** The round-37 closure's disagreements became Q28 and errata,
  and this round's own freeze defect (N21) was named, not relabelled, with a check shown able to fail (Q29). Against that, the
  L1's own freeze mislabelled a mutant direction and repeated the order-of-operations mistake, so C1 is not admitted; the
  non-author closure decides.

## Open L0 questions

No new line filed. Still open: `kengaku | round-25` (coverage cap, novelty conversion) and `kengaku | round-33` (decision packet
for the coverage cap). Routed around: coverage held at 7.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Build-provenance TB2 grader — round 38 (13-row decision table, each row citing a receipt case) and registry rows build-pmars-probe / round38-c1-mutants / round38-c2 / mutant-direction-check / tip-receipts
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round 38 entry; `corpus/evidence/round38/build-pmars-probe.txt` (22 cases, byte-equal re-run; real pytest parity 22/22 in `build/R38CritPytest.md`)
- [~] Instructions executable by an agent without oral context — `.ufo/waves/round-38/integrate/measure.sh` re-runs every claim counter and the no-harm set from a clean clone
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` §Round38 partial frontier admission and its sibling report-out (16 surfaces with file:line); linkage interpretation routed to kaidoku
