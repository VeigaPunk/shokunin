# tameshi — round 89 report (attempt 1, L1 TameshiR89)

Lane HEAD (pushed): `20e78a5566ffe70a7dde1ff1b2672b334f958f68` (`git ls-remote origin refs/heads/master`).
Fresh start under Amendment 46. Round shape: one v1 wave `r89-w1`, 12 seats, no residual call. Round total: 12.

## Work performed

Declared claim (one): **R89-C1 — operability, capability acquisition**: `tools/ledger-witness.py`, a
kernel-witnessed audit of `tools/mutate-and-run.sh --regression` that runs the ledger under
`strace -f -y -v` and binds every declared leg to observed execs, bytes and kernel exits instead of the
runner's printed figure. **Outcome: predicate met; claim killed by its own kill rule (b); not admitted.**

- Fresh-start reads: rounds 86/87/88 rejected closures and spot-checks (common root: counters that read a figure the subject prints) — `plans/round-89.plan.md` § Fresh-start reads.
- Witness built (15 checks W_PARSE…W_ENV, 21-arm public-CLI selftest) — `tools/ledger-witness.py`, pre-freeze commit `a65e11c01a469336b74662d2e3c51ba6f174ac6f`.
- Forgery battery: 9 new forgeries (`.ufo/evidence/round-89/controls/make-forgeries.py`) + the round-88 trio (parked, stub, dupbase; closure routed item 1) + 2 honest variants; expectations `controls/expected.tsv`.
- Full counter at the pre-freeze commit: real + 2 honest PASS, 12/12 forgeries refused, `capability_row=0` — `.ufo/evidence/round-89/pre-freeze/measure-a65e11c0.out` (commit `483832950064a2cd1a7283c42e4264c7254c2b68`).
- No-work control at base: `witness=absent … C1_R89_PASS=false`, exit 1 — `pre-freeze/nowork-base.out`.
- Freeze (predicate, kill rule, declared limits L1–L4): `8876cca5dbb877b168aa09a86128d672f6b4ed5a`.
- Landing (capability row, knowledge entry, S313/S314): `ff7a4b06c054bc3ef9cf52612e876629e83a6a14`; counter `C1_R89_PASS=true`, exit 0 — `landing/measure-ff7a4b06.out`.
- Wave attacks (all in `tameshi-shokunin/.ufo/waves/round-89/w1/`): **T89E2 kill** — `hardlink`, `dirswap`, `symlink` runners exec stubs at the audited paths and install exact bytes through an alias afterwards; accepted with `findings=0` (`T89E2.md`), reproduced by the L1 (`.ufo/evidence/round-89/landing/t89e2-reproduced-by-l1.txt`). T89C1: a counterfeit witness (no subprocess) passes the frozen counter; selftest conjunct accepts any `n/n` (`T89C1.md`, `T89C1-measure.out`). T89E4: `umask`/`/dev/full` per-defect coercion accepted — inside declared L3 (`T89E4.md`). T89M1: witness selftest kills 15/23 single-edit mutants (`T89M1.md`). T89R1: 1 kill (same aliasing) + 3 defects. T89R2: nonconformant on round-88 routed items 4 and 6 (now mined as M8/M9). T89C2: 4 parser misparse cases (`T89C2.md`). T89E3: 2 honest variants accepted (kill rule (c) not fired). T89E1: independent counter run, `conjuncts-met`. T89S1: 4/4 quotes located; S315 candidate. T89CN1: 18 adjacent sibling counters. T89SC1: entry draft.
- Records: lesson `corpus/lessons/round-89.md` (Gate, Mistakes M1–M10, Verdict, Routed), QUALITY 136–138, LOG, SCORECARD Round 89 section, capability row annotated not admitted — commit `20e78a5566ffe70a7dde1ff1b2672b334f958f68`.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| `tools/ledger-witness.py`, forgery generator, counter, controls, sources | `LOG.md` § Round 89 | `a65e11c01a469336b74662d2e3c51ba6f174ac6f` |
| pre-freeze counter receipt | § Round 89 | `483832950064a2cd1a7283c42e4264c7254c2b68` |
| plan freeze | § Round 89 | `8876cca5dbb877b168aa09a86128d672f6b4ed5a` |
| capability row, knowledge entry, S313/S314, docstring scan | § Round 89 | `ff7a4b06c054bc3ef9cf52612e876629e83a6a14` |
| wave evidence, lesson, QUALITY 136–138, S315, records, row annotation | § Round 89 | `20e78a5566ffe70a7dde1ff1b2672b334f958f68` |

## Before → after measurements

| Claim | Counting command | Before (`61990f3d8cd99932bfb0575e1c292e03d310b436`) | After (`ff7a4b06c054bc3ef9cf52612e876629e83a6a14`) | Verdict |
|---|---|---|---|---|
| R89-C1 | `bash .ufo/evidence/round-89/measure.sh <lane> REV /home/vgpnk/Projects/shokunin <empty dir>` | `witness=absent selftest=0/0 real=SETUP forgeries_refused=0/0 capability_row=0 C1_R89_PASS=false`, exit 1 | `witness=present selftest=21/21 real=PASS(legs=11) honest_accepted=2/2 forgeries_refused=12/12 capability_row=1 C1_R89_PASS=true`, exit 0 | **killed** by kill rule (b) (T89E2 alias runners accepted); counter also cheat-passable (T89C1). Not admitted. Operability: unprovable. |

No-harm: `tools/mutate-and-run.sh` unchanged; selfstate `rows=26 match=24 stale=2 unexpected=0`, pins 26/26, registry 9/9, pointers 12/12 (`.ufo/evidence/round-89/landing/`); cold-read precheck `credited=24/72` at base, landing and final tip. Scores: depth 10, calibration 8, freshness 9 (unchanged).

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi` — start exit 0, end exit 0 (`tameshi ok`); receipts `.ufo/evidence/round-89/census-before.txt`, `census-after.txt`.
- Rows `grep -c '^| S[0-9]' corpus/SOURCES.md`: 172 → 175. Added by tier: A ×3 — S313 execve(2) (mined), S314 strace(1) `-y`/`-v` (mined), S315 Licker & Rice ICSE 2019 mkcheck (queued). Rows touched old→new: none.
- Frontier advanced: kernel-observed verification of a subject's work (`corpus/knowledge/kernel-witnessed-ledger.md`, citing S313/S314); S315 queued as the successor grounding.
- Sourced claim: R89-C1 rests on S313/S314 (opened this round).
- Mistake mined: M1 (round-88 print-binding check accepts `stub-lines`, shown in `landing/m1-r88-check-vs-stub-lines.txt`) through M10 — `corpus/lessons/round-89.md` `## Mistakes`.
- Assimilation: none (one claim; no `merge/tameshi/` theme serves it). considerthese `2026-11-06.md` idea 5 applied: `landing/docstring-vs-code.txt`. Correction for S312 word counts (routed item 5) appended in the lesson.
- Misroot sweep (`git status --porcelain` on the fleet root): no files from this round's seats.

## Trend verdicts

- **expansion: improved** — new knowledge entry on ground the lane did not hold, citing two mined rows opened this round (S313, S314); S315 queued.
- **quality: unchanged** — no held entry re-verified or superseded.
- **discernment: improved** — the wave killed the claim; the kill and nine other mistakes are mined into QUALITY 136–138, each tied to a committed control that shows the failure (T89E2 runners, T89C1 counterfeit witness, stub-lines receipt).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `tameshi-shokunin/SKILL.md` (unchanged this round)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `tameshi-shokunin/LOG.md` § Round 89
- [~] Instructions executable by an agent without oral context — `tameshi-shokunin/.ufo/evidence/round-21/coldread/ledger.json`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `tameshi-shokunin/PROVINCE.md` (unchanged)

## Round extras

- Wave: `r89-w1`, 12 seats — executor 4, mutation-tester 1, reviewer 2, critic 2, scout 1, scribe 1, connector 1; attack share 5/12. Dead seats: 0 (`.ufo/waves/round-89/r89-w1-results.json`, 12 entries). Planner seat: held by the L1. Labrat-class probe rode executor T89E4.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none. pacman untouched.
- Open L0 questions: none.
