# mori round 84 — report

lane: mori-shokunin · round 84 (attempt 1) · date 2026-11-04 · L1 `MoriR84`
entering revision: `5adf4337b6510dd246b247092c11cbaa97c930d3` (branch `master`, pushed, clean)
freeze commit: `daa77bd5684c8db75eec1e80c87ee4fa5c3a6bb4` · pre-data amendments A1 `dbdb1aaa`,
A2 `39190f8a`, A3–A4 carried in A5/A6 `5a231ef8`, A7 `4a83e6aa`, A8 `0a843033`, A9 `792a824d`
code commit: `da7631f4a44aaa6d7c1c822308df4d265fb8d7da` · record commit
`d95746921d3b330d58db5ff3992b5457f9f32950` · final lane tip
`72fc09247aae134057336e99f7db34a7123d5759` (pushed; `ls-remote origin refs/heads/master` prints it)

## Work performed

Declared claims (frozen in `.ufo/waves/round-84/contract.md` before any seat ran; nine pre-data
amendments, each disclosed there and in `corpus/lessons/round-84.md`):

- **C1 — operability (7):** the r83 counter family's four extra mutants (M24a–M24d, measured by
  the r83 C1 reviewer at `c4845c83`) get the failing arm each needs, with M24c/M24d adjudicated
  equivalent behind byte coupling proofs. Target `C1=met mutants=4 killed=2 equivalent=2
  survivors=0 total=4 pristine=green detector=green`.
- **C2 — calibration (5, tied lowest):** the record sweep's revision arm grades **every** row the
  anchor selects on both sides (`ALL_ANCHOR_ROWS`), with two defeated ambiguous fixtures. Target
  `C2=met arm=all-rows defeated=2 fixtures=3/3 bindings=3 revisions=0 arms=44`.
- **C3 — depth (5, tied lowest):** the r83 drift counter's live reading becomes a per-token delta
  classification (absent-live / added-live / class-changed / agreed). Target `C3=met
  delta=classified tokens=64 classified=union residual=0 live=derived`.

Work items and evidence:

- **Contract, three counters, entering controls (L1).** `.ufo/waves/round-84/contract.md`,
  `count-c1.py`, `count-c2.py`, `count-c3.py`, `evidence/controls-r84.txt` — `daa77bd5`. At
  `5adf4337` the three controls read `C1=unmet harness=absent`, `C2=unmet arm=absent`,
  `C3=unmet delta=absent`, each rc 1.
- **Amendments A1–A9 (L1, pre-data; contract §A1–§A9).** A1 corrected a fixture finding's line
  number; A2 re-pinned three anchors that the freeze had quoted from r83 prose rather than bytes
  (M24b occurred 2×, M24c/M24d 0× — three seats found this independently); A3 clarified that
  `tokens=64` is the snapshot count; A4 corrected the `blind_case_tally` assertion to
  `killed=1 survivors=1 total=2`; A5 bound the C1 subject's two arm labels and the 2/2/4 split
  after the critic's tripwire control reached the target; A6 made C3 import and grade the
  classifier and recount the snapshot after the critic's null classifier reached the target; A7
  corrected the separability wording and hardened C3's import against `SystemExit`; A8 added
  supersede pointers and the per-fixture mismatch kind; A9 superseded P-C3's stale preservation
  list. No predicate, kill rule, target or class was changed after data.
- **C1 arms, count-c1.py (seat `Mo84E01C1Arms`).** Two arms — `blind_case_tally` and
  `green_requires_fail_zero` — taking the r83 counter's selftest 6 → 8 arms;
  `w1/Mo84E01C1Arms.md`. The two equivalence exemptions ride `agreed == len(snapshot_tokens)`,
  `residual += duplicates` and `duplicates == 0`, each exactly once at the graded revision.
- **C3 classifier, count-c2.py (seat `Mo84E03C3Delta`).** Pure `live_delta(snapshot_tokens,
  live_tokens, names, stated)`, one `LIVE_DELTA <token> <class>` line per non-agreed token, tail
  fields `classified=/union=/absent_live=/added_live=/class_changed=/deltas=`, four delta arms
  (selftest 12 → 16); `w1/Mo84E03C3Delta.md`. The seat's honest stop: a scratch clone resolves a
  different census fleet root, so its probe read `deltas=26`; the lane checkout reads `deltas=0`.
- **C2 all-anchor-rows, tools/mori-record-sweep.py (L1 stand-in for the dead `Mo84E02C2Rows`).**
  `anchor_rows()` + `ALL_ANCHOR_ROWS` on both sides, four new selftest arms (40 → 44). The L1
  applied it from a scratch prototype validated against the frozen counter before application
  (prototype: `RECORD_SWEEP_SELFTEST pass=44 fail=0`, `C2=met … arms=44`); no seat report exists
  for this item because the seat produced no output.
- **Controls verification (seat `Mo84E04Controls`).** Independent re-run of the nine control
  commands — `evidence/controls-verify-r84.txt` — every expected line matched, including the
  freeze population control and the r83 no-harm battery.
- **Defeated-control receipts (L1).** `evidence/controls-r84-defeated.txt`: the freeze population
  control; the critic's tripwire control (pristine green, all count-c1 mutants killed, the target
  split printed, no arms) defeated as `C1=unmet subject=absent-arms`; the critic's stub control
  defeated as `C3=unmet … import-failed:SystemExit`; a null classifier defeated as
  `C3=unmet … selftest=red`.
- **Source (seat `Mo84Sc01Source`).** S599 pinned at
  `corpus/evidence/sources-r84/arXiv-2408.01760-abs.html` (sha256 `68822410…`, 42566 bytes, 597
  newlines, three fetches byte-identical, `last-modified` 2026-08-24, 304 on revalidation), quote
  at body line 121 (24 words); arXiv:2404.09241 screened and refused with a flip condition;
  `w1/Mo84Sc01Source.md`.
- **Clause sweep (seat `Mo84Sc02Clauses`).** Unarmed-clause tables for both r83 counters, the
  measured `pass=7 fail=1` for the wrong `blind_case_tally` assertion, and the D1/D2/D3 findings;
  `w1/Mo84Sc02Clauses.md`.
- **Connector (seat `Mo84K01Conn`).** Six-lane × three-ground overlap matrix; tameshi owns the
  mutation method (mori owns its counter), kumitate the closest live-delta owner; the tameshi
  boundary is contested and reported, not absorbed; `w1/Mo84K01Conn.md`.
- **Reviewers and critic (seats `Mo84R01C1`, `Mo84R03Record`, `Mo84C01Crit`).** R01 re-derived all
  four anchors (1× each) and the population control at both revisions, judged A2 sound, and found
  two new surviving counter mutants (X1 `if not k and coupling is not None:`, X2
  `coupled = base.count(coupling) == 1` → `>= 1`); R03 found five prose-vs-code divergences
  (F1–F5) and the executing-counter-bytes gap; C01 built the tripwire and null-classifier
  controls that forced A5/A6; `w1/Mo84R01C1.md`, `w1/Mo84R03Record.md`, `w1/Mo84C01Crit.md`.
- **Mutation probe (seat `Mo84M01Mut`).** `MUTANTS total=49 killed=23 survivors=26` over the three
  r84 counters (c1 23/14, c2 12/5, c3 14/4), each survivor named with the arm it needs;
  `w1/Mo84M01Mut.md`.
- **Lesson, QUALITY and coverage rows (seats `Mo84S01Lesson`, `Mo84S02Quality`).**
  `corpus/lessons/round-84.md` (mistake: the r83 round read its counters met while its own
  mutation-probe seat died without a tally; census before/after; the L1 Gate and A2 resolution),
  `corpus/QUALITY.md` 170–172, `corpus/README.md` Round-84 row; `w1/Mo84S01Lesson.md`,
  `w1/Mo84S02Quality.md`.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Freeze: contract, three counters, entering controls | Round 84 §freeze | `daa77bd5` |
| Wave spec, dispatch, handoff (14 seats) | Round 84 §Wave | `fce96d1f` |
| A1: fixture finding line number | contract §A1 | `dbdb1aaa` |
| A2: M24b/M24c/M24d anchors corrected | contract §A2; lesson §A2 | `39190f8a` |
| A5/A6 (+A3/A4): C1 subject markers + split, C3 classifier import + recount | contract §A5/§A6 | `5a231ef8` |
| A7: separability wording, C3 import hardening, defeated-control receipts | contract §A7 | `4a83e6aa` |
| A8: supersede pointers, per-fixture mismatch kind | contract §A8 | `0a843033` |
| A9: P-C3 preservation list superseded | contract §A9 | `792a824d` |
| C1 arms (r83 count-c1.py 6 → 8), C3 classifier (r83 count-c2.py 12 → 16), C2 all-rows (record sweep 40 → 44, L1 stand-in), wave reports and results | Round 84 §C1/§C2/§C3/§Wave | `da7631f4` |
| Record: SCORECARD round-84 section + three capability rows + Planned (r85), LOG, SKILL registry row 18, SHONEN, PROVINCE Round-84 note, QUALITY 170–172, SOURCES S599 + search log, knowledge entry, lesson, after and battery receipts | Round 84 §Frontier/§No-harm | `d9574692` |
| Final-tip re-run receipt | Round 84 §No-harm | `72fc0924` |

## Before → after measurements

Measured by the round's frozen counters; receipt `.ufo/waves/round-84/evidence/after-r84.txt`
(primary at `da7631f4`, re-run at the record commit `d9574692`; the counters are the worktree
bytes at those revisions).

| Claim | Counting command | Before (entering `5adf4337`; freeze control) | After (measured) |
|---|---|---|---|
| C1 operability | `python3 -I .ufo/waves/round-84/count-c1.py <rev>` | `C1=unmet harness=absent`, rc 1; at the freeze `C1=unmet mutants=4 killed=0 equivalent=2 survivors=2 total=4 pristine=green detector=green`, rc 1 | `C1=met mutants=4 killed=2 equivalent=2 survivors=0 total=4 pristine=green detector=green`, rc 0 at `da7631f4` and `d9574692` |
| C2 calibration | `python3 -I .ufo/waves/round-84/count-c2.py <rev>` | `C2=unmet arm=absent`, rc 1 | `C2=met arm=all-rows defeated=2 fixtures=3/3 bindings=3 revisions=0 arms=44`, rc 0 at `da7631f4` and `d9574692` |
| C3 depth | `python3 -I .ufo/waves/round-84/count-c3.py <rev>` | `C3=unmet delta=absent`, rc 1 | `C3=met delta=classified tokens=64 classified=64 union=64 residual=0 live=derived live_tokens=64 live_agree=64 deltas=0 arms=16 classifier=5/5`, rc 0 at `da7631f4` and `d9574692` |

Supporting measurements: the r83 no-harm battery at the freeze still reads
`C1=met mutants=23 killed=22 equivalent=1 …`, `C2=met snapshot=bound … live_tokens=64`,
`C3=met arm=anchored … arms=40`; the standing battery at `da7631f4` reads `BATTERY pass=57
setup=4 fail=0` (`BATTERY 57/61`, rc 2 for the four expected host-setup cases; receipt
`evidence/battery-r84.txt`), unchanged from r83; the record sweep over the real lane reads
`RECORD_SWEEP pending=0 pinned=0 carriers=1 bindings=3 revisions=0` rc 0; the claim sweep reads
`CLAIM_SWEEP mismatches=0 unresolved=0 tallies=0 stale=0 carriers=4 pointers=266` rc 0.

## Sources & frontier

`corpus/SOURCES.md` before → after: **371 → 372** rows by the grammar count
`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; the census
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`
reads `mori ok` and exits **0** both times, with the same **35** tolerated W04 duplicate-URL
warnings; malformed rows 0. Rows added: **1**, by tier **A=1** (S599, paper). Rows touched
old→new: none (no status/recheck/used-by change on an existing row). Frontier rows advanced: none
— S599 grounds a new knowledge entry, not a `PROVINCE.md` frontier item; FR1–FR14 are unchanged
and no census surface moved (PROVINCE's Round-84 note).

S599 — arXiv:2408.01760v1, "Large Language Models for Equivalent Mutant Detection: How Far Are
We?" (Tian, Shu, Wang, Cao, Kamei, Chen; ISSTA'24) — pinned at
`corpus/evidence/sources-r84/arXiv-2408.01760-abs.html`, sha256
`688224106999973f3b5c318af871b77923df2c36d0e3e2d799424e2c697cff49`, 42566 bytes / 597 newlines;
three fetches byte-identical, `last-modified: Mon, 24 Aug 2026 20:41:50 GMT`, no ETag, 304 on
`If-Modified-Since`. Located quote at body line 121, 24 words: "However, the presence of
equivalent mutants is known to introduce redundant cost and bias issues, hindering the
effectiveness of mutation testing in practical use." The row is `mined`, used by
`corpus/knowledge/equivalent-mutant-adjudication-r84.md` (K1–K4). arXiv:2404.09241 ("An Empirical
Evaluation of Manually Created Equivalent Mutants") is refused (defines equivalence, reports a
weaker cost line over manually created mutants in a game study, no bias half, no adjudication
procedure) with its flip condition in the round lesson's Gate. Search log: identified 2, screened
2, included 1, excluded 1. Assimilation: none (`merge/mori` untouched this round).

## Trend verdicts

- **expansion: improved** — one admitted `corpus/knowledge/` entry on ground the coverage map did
  not hold (`equivalent-mutant-adjudication-r84.md`, K1–K4), its `source:` citing the `mined` row
  S599 opened, pinned and quoted this round; coverage-map row appended in `corpus/README.md`;
  registry 371 → 372; census rc 0.
- **quality: improved** — the r83 counters gained working, graded arms (count-c1 6 → 8, count-c2
  12 → 16), the record sweep 40 → 44 arms with the all-rows rule, and the classification gained a
  per-token delta with an imported, independently graded classifier; the standing battery is
  unchanged at `BATTERY pass=57 setup=4 fail=0`. Counterweights routed, not hidden: the mutation
  probe still reports 26 survivors over the r84 counters (`.ufo/waves/round-84/w1/Mo84M01Mut.md`),
  and R01 found two new surviving mutants in the r83 detector logic.
- **discernment: improved** — five independent seats (S01, S02, K01, R01, C01, R03, Sc02) found
  the freeze's prose-anchor defect and the two counter holes before any after-value; the nine
  pre-data amendments are on record with their measurements, and the critic's controls are
  committed as defeated. Named weaknesses: the round needed nine pre-data amendments, which says
  the freeze under-checked its own prose (the A2 class is exactly the lane's own QUALITY 168
  lesson), and the C2/C3 attack seat `Mo84R02C23` died with no output.

## SHONEN

`SHONEN.md` boxes, one line each (`[x]` only with a named non-author verifier; none is written
here):

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `SKILL.md:1370` (r84 gate-registry row 18); `corpus/QUALITY.md` 170–172 (added round 84);
  `corpus/knowledge/equivalent-mutant-adjudication-r84.md` (K1–K4, sourced S599).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 84 (C1/C2/C3
  with their measured values and receipts; the dead-seat and L1 stand-in record).
- [~] Instructions executable by an agent without oral context — `python3 -I
  .ufo/waves/round-84/count-c1.py --selftest` (15/15), `count-c2.py --selftest` (9/9),
  `count-c3.py --selftest` (11/11), `tools/mori-record-sweep.py --selftest` (44/44), re-run
  2026-11-04 at `da7631f4`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` Round-84 note (no census
  surface, no threshold, no baseline rewrite, no remediation); the connector's contested tameshi
  boundary reported, not absorbed (`w1/Mo84K01Conn.md` §2).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none (no `uv`, `npx`, pacman or binary install; pacman paused host-wide and no
transaction was attempted).

## Round shape and settlement

ONE v1 wave of 14 seats under `ufo-wave-policy.json` (band 8–16; dispatch `w1-dispatch.json`,
validated, 14 spawn / 0 resume): 4 executor, 3 reviewer, 2 scout, 2 scribe, 1 critic, 1
mutation-tester, 1 connector — attack share 5/14 (35.7 %), connectors 1, residual none; the
planner seat is the L1 (no planner lane exists in the validator). `w1.ready` was taken at
09:39:36Z. Dead seats, never replaced: `Mo84E02C2Rows` (executor, empty output, no tool edit) and
`Mo84R02C23` (reviewer, empty output); the L1 landed E02's assignment from a scratch prototype
validated against the frozen counter before application, and R02's attack is covered by the
critic, the C1 reviewer, the mutation probe and the record reviewer. Round total: 14 seats, 12
with reports, 2 dead.
