# kake — round 99 report (hyaku run 15, attempt 1)

L1: KakeR99. Lane `kake-shokunin`, branch `master`. Round base `cde408e5817bf1376c701d8decc5469fa82b2985`;
final lane hash `dc89a9064c10ded88f958128acb9702bdf033586` (`git ls-remote origin refs/heads/master` prints it).
Freeze: `.ufo/waves/round-99/freeze.md` at `ab35eacebf922f4f598237590f0220d63111dc94`. The outside closure owns admission.

## Work performed

Declared claims (2): **C1 — calibration** (score 3, the lowest owned non-retired axis): the SKILL.md
gate/probe registry tables against the committed tools directly under `scripts/`. **C2 — freshness**
(HOLD 10), capability acquisition, sourced on S484: which stored responses a 304 (Not Modified) freshens
and their updated header fields (RFC 9111 §4.3.4 + §3.2 with the §3.1 exceptions).

- Fresh-start reads (amendment 35): rejected closures r94, r96, r98 and their spot-checks; r98's
  routed defects R98-C1/C2/C3 read from `corpus/lessons/round-98-verifier-spotcheck.md:134-141`.
- Instruments committed before any control or seat: `c99_registry.py` (selftest 20/20),
  `c99_fresh304.py` (50 hand cases, seeded generator, reference drift check), contract
  `fresh304-contract.md` (LC1-LC6), control subjects `frozen/` (positive oracle + 7 forgeries),
  retained RFC 9111 and EID 9185 bodies, SKILL.md instrument rows — commit `2345e309`.
- Pre-freeze controls (`controls.sh`, scratch-clone fixture commits), receipts in
  `.ufo/waves/round-99/controls/`, freeze commit `ab35eace`:
  - C1: base `unlisted=26` exit 1; names-only / fenced / false-selftest / wrong-owner forgeries all `met=false`;
    positive `met=true`; junk-prose `met=true` (declared counter limit, covered by the review conjunct).
  - C2: base `candidate=absent` exit 1; positive oracle `hand=50/50 generated=240/240 met=true`;
    constant, lookup, must-not→no-update, first-match, copy-all, weak-in-strong and lenient forgeries all `met=false`.
- C1 repair: `## Round 99 — tool registry completion` (26 rows) appended to SKILL.md — `9d341d1b`;
  receipt `controls/after-c1.txt` `unlisted=0 … met=true` exit 0.
- One v1 wave, 13 seats (`w1-spec.json`, validated; `w1-results.json`). Outputs integrated:
  - ExecFresh built `scripts/freshen_304.py` from the contract alone. It scored met on 4 seeds
    (`w1/ExecFresh/score-*.txt`) and its selftest is 76/76.
  - ExecTwinFresh: an independent twin over 2400 inputs. It found 30 disagreements, all one class
    (LC6 case sensitivity, a contract ambiguity); 0 oracle defects (`w1/ExecTwinFresh/disagreements.md`).
  - ExecRegProbe: 18/18 self-test cells exit 0 and 78 probes. It found 0 contradictions, but its item
    excused argparse exit 2 (mistake 5).
  - ReviewRegA (2 disagree) and ReviewRegB (3 disagree) judged the 26 rows (`w1/ReviewReg{A,B}/verdicts.tsv`).
  - ReviewFresh: hand expectations 48/50 agree. It filed 12 contract findings, 3 of them RFC
    contradictions (F1/F2/F10) (`w1/ReviewFresh/contract-findings.md`).
  - CriticClaims: 8 C1 escapes, 7 C2 escapes and 11 predicate holes. The landed candidate agreed
    with the reference on 9/9 escape-class probes (`w1/CriticClaims/attacks.md`).
  - MutCounters: registry counter 12/29 killed (10 survived, 7 not run); fresh304 counter 13/23
    killed (6 survived, 4 not run). Host `/fast` ENOSPC mid-run voided one batch (`w1/MutCounters/mutants.tsv`).
  - SentinelScope: 11 vectors, 4 verdict-affecting. One is blocking: W1, a candidate can read the
    oracle via procfs (`w1/SentinelScope/vectors.md`).
  - ScoutRfc9111 re-fetched both sources byte-identically and found 6/6 quotes. It drafted S484/S485 (`w1/ScoutRfc9111/`).
  - ScribeEntry drafted `freshening-304.md`: 35 quotes found, metatext lint 0 (`w1/ScribeEntry/`).
  - ScribeLesson drafted the Gate, mistakes 1-4 and criterion R99-A. ConnectorScope found sibling
    prior art in kotoba `verifiers/check_gate_registry.py` (`w1/ConnectorScope/overlap.md`).
- C2 content commit `998b6d5f` contains:
  - the candidate;
  - the knowledge entry, with a known-limits section from ReviewFresh;
  - SOURCES rows S484/S485;
  - the README section;
  - the registry row for `freshen_304.py`.

  Scored by the frozen counter (`controls/after-c2.txt`). Landed blob vs reference over the twin's
  2400-input generator: 0 disagreements (`controls/c2-landed-vs-oracle-twin-generator.txt`). Static
  check: imports json/re/sys only (`controls/c2-candidate-static.txt`; the grep hits are docstring
  prose), which mitigates W1 for this blob.
- Routed r98 closure defects closed:
  - R98-C2: the unbacked r98 capability row was moved to the no-admitted-closure table — `7f5b1b7b`.
    `c98_captable.py` now reads `unbacked=0 met=true` (`controls/r98c2-captable-after-move.txt`).
  - R98-C1: `knowledge_metatext_lint.py` registry row landed at `9d341d1b`. Its run at a landed
    revision gives `gate_findings=0` (`controls/metatext-lint-at-master.txt`).
  - R98-C3 is a wording defect only. This report cites each receipt's measured revision.
- Post-review corrections of the three disputed rows (verdict unchanged), lesson, LOG, SCORECARD
  section — `bec2212e`. Wave results and late evidence — `4f2b32da`, `dc89a906`.
- Planner seat: held by the L1 (the validator rejects `planner`).

## Landed changes

| Commit | Change | LOG.md entry |
|---|---|---|
| `2345e309640adac6c36e41eca87409085ba3a276` | instruments, contract, control subjects, RFC 9111 + EID 9185 bodies, assimilation check, census-before, SKILL.md instrument rows | Round 99, C1/C2 bullets |
| `ab35eacebf922f4f598237590f0220d63111dc94` | freeze + pre-freeze controls, spec builder, repair-section copy | Round 99, C1/C2 |
| `9d341d1b46f16dbfbb41af75dd6d4966808dfa5d` | C1 repair: 26 SKILL.md registry rows | Round 99, C1 |
| `82ce1b6232ad6a4423402c5da9eb0ea39e29f147` | w1 spec/dispatch/ready, C1 after-receipt | Round 99, Wave |
| `7f5b1b7b8dbfdae74dfe6d487bbf5406c478b916` | R98-C2 row move, R98-C1 lint run | Round 99, Routed closure defects |
| `998b6d5f6dd453d910b15c0bdf9e5ac124c84497` | C2 candidate, knowledge entry, S484/S485, README section, registry row | Round 99, C2 / Frontier |
| `bec2212ecf093c2b1071019c8939f3413f97e39e` | lesson, LOG, SCORECARD section, three post-review row corrections, C2 receipts, census-after, w1 evidence | Round 99, all bullets |
| `4f2b32da39bce4e3243b7b4cedd517e007c30245` | w1-results.json, MutCounters evidence, routes R99-12 + seat yield | Round 99, Wave |
| `dc89a9064c10ded88f958128acb9702bdf033586` | dispatch marker, ExecTwinFresh full results (1.8 MB) | Round 99, Wave |

## Before → after measurements

- **C1** — `python3 -B .ufo/waves/round-99/c99_registry.py --root . --revision <REV> --work <scratch>`
  - Base `cde408e5`: `tools=54 rows=124 listed=28 unlisted=26 dangling=0 exec_fail=1 mismatches=26 met=false`, exit 1.
  - Repair `9d341d1b`: `tools=54 rows=152 listed=54 unlisted=0 dangling=0 exec_fail=1 mismatches=0 met=true`, exit 0.
  - Review conjunct: `cut -f2 .ufo/waves/round-99/w1/ReviewReg{A,B}/verdicts.tsv | sort | uniq -c`. ReviewRegA
    gives 24 agree / 2 disagree; ReviewRegB gives 23 agree / 3 disagree. The disputed rows are
    `quote_class.py`, `wave_seat_record.py` and `sitemap_audit_selftest.py`: the verdict maps were
    copied from docstrings that contradict the code. I reproduced each fault: rc 2, rc 2 and rc 64.
  - **Verdict: unmet** under the frozen kill rule. Calibration stays 3.
  - At the C2 commit `998b6d5f` and at the final tip: `tools=55 … unlisted=0 met=true`, reported and not re-scored
    (`controls/tip-c1-at-c2.txt`).
- **C2** — `python3 -B .ufo/waves/round-99/c99_fresh304.py --root . --revision <REV> --work <scratch>`
  - Base `cde408e5`: `candidate=absent met=false`, exit 1.
  - `998b6d5f`: `candidate=present sha256=db3a0f12b91a5a54409ebafcf800204011385a523ff4da9b897b71dd7c0c1d4f
    hand=50/50 generated=240/240 refusals=47/47 seed=2576051551 met=true`, exit 0. The landed blob's sha256 is the same.
  - 10 extra seeds: 10/10 met.
  - **Verdict: met on the frozen predicate.** The capability is recorded in the round section's
    repertoire only. Per R98-C2 it does not enter `## Capabilities` before an admitted closure.
  - Caveats: the counter population is blind to 7 classes; the runner is not isolated; contract-v1
    departs from the RFC in F1/F2/F10. These are routed R99-8/9/10.

## Sources & frontier

- Census, `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`:
  - Round start: rc 0 (`controls/census-before.txt`).
  - Round end: rc 0 (`controls/census-after.txt`). The only findings are W04 duplicate-url warnings,
    40 → 41. The new one is S484 sharing the rfc9111.txt URL with S456/S467/S469/S470/S480, a
    pre-existing class.
- Rows, counted with `git show <rev>:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`:
  220 (`cde408e5`) → 222 (`dc89a906`).
- Rows added by tier: A +2, both opened 2026-11-05, status `mined`.
  - S484: spec, RFC 9111 §3.1/§3.2/§4.3.4.
  - S485: dataset, erratum EID 9185, Reported, Technical.
- Rows touched (old → new): none. No existing row's status, recheck or used-by changed.
- Frontier advanced: RFC 9111 §4.3.4/§3.2 freshening ground. It was named open since the round-93
  Planned section. It is recorded in README `## Round-99 frontier step — 304 freshening`.
- Sourced claim: C2 rests on S484, which `corpus/knowledge/freshening-304.md` cites.
- Mined mistake: `corpus/lessons/round-99.md` `## Mistakes` has 5 entries. Entry 5 is the round's own
  C1 kill (rows written from docstrings). Its fix is criterion R99-B, shown red on the three rows.
- Assimilation: none. `.ufo/waves/round-99/assimilation/` holds 220 registry ids against 129 staged ids,
  with 8 collisions (S312 S329 S367 S372 S373 S374 S390 S409). No renumber map exists, so nothing was appended.
- considerthese: `considerthese/2026-11-05.md` Part 2 proposal 4 (open-frontier map) became criterion
  R99-A. Its check script is in `w1/ScribeLesson/` and is red at the tip by 4 grounds.

## Trend verdicts

| Trend | Verdict | Evidence |
|---|---|---|
| expansion | improved | New RFC 9111 §4.3.4/§3.2 ground: S484/S485 and `corpus/knowledge/freshening-304.md`. A working freshening decision scored met by the frozen counter. |
| quality | improved | 26 tools gained registry rows; the counter goes 26 → 0. The three false rows were corrected after review. The routed r98 defects R98-C1/C2 were closed (`unbacked` 1 → 0). The C1 claim itself failed its review conjunct. |
| discernment | improved | The lane's own reviewers rejected 3 L1-written rows, and C1 was recorded unmet rather than re-scored. Critic, sentinel and mutation findings were routed as R99-8…12, not hidden. No closure spot-check of this round exists yet. |

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — 29 registry rows added this round (26 tools in `SKILL.md` `## Round 99 — tool registry completion`, `freshen_304.py` in `### Round 99 C2 capability tool`, two counters in `### Round 99 instrument registry`)
- [ ] At least one end-to-end domain task executed and logged in LOG.md — ledger box 2 status `gap` (unchanged this round)
- [~] Instructions executable by an agent without oral context — 18 registry self-test commands executed exit 0 (`w1/ExecRegProbe/findings.md`); three rows needed correction
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the new entry cites no sibling lane path; ConnectorScope found prior art only (`w1/ConnectorScope/overlap.md`)

## Round shape and extras

- Shape: one v1 wave (`ufo-wave-policy.json`), 13 seats.
  - Roles: scout 1, connector 1, executor 3, scribe 2, reviewer 3, critic 1, mutation-tester 1, sentinel 1.
  - Attack share: 5/13 (ReviewRegA, ReviewRegB, ReviewFresh, CriticClaims, MutCounters; sentinel excluded).
  - No residual call. Round total: 13.
- Seat yield: 13/13 seats settled with non-empty output; no dead seat.
  - MutCounters reported a host `/fast` ENOSPC mid-run. `df` at report time shows 50 % used.
    It left 11 mutants not run. The L1 nudged it once by id to deliver.
- WAVE-DONE received before filing.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists only `.scratch/` and
  untracked `w4lines.txt`. Neither names kake or round 99, so there were no misroots and nothing was touched.
- Scratch: `/fast/scratch/hyaku/kake-r99` was removed after landing.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none.
- Open L0: R95-2, unchanged (fleet `.ufo/l0-questions.md` line 371). No new question.
