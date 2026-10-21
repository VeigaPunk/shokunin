# mado — round 20 report (attempt 2, recovery coordinator MadoR20Recovery)

Lane `/home/vgpnk/Projects/shokunin/mado-shokunin`; claim base `1f7f995`; lane landed `94b692591a99ebac34fd2ba03094ad13fcf0fbe7`.
Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Work performed

Declared claims (registered `e629f73`, unchanged): **C1 operability** — tripwire precision
(`python3 -I .ufo/waves/round-20/tw-precision.py REV`, suite pin `f3da504`); **C2 calibration**
(lowest measured axis; `python3 .ufo/waves/round-17/measure.py REV`, key c1). L1 holds the planner seat.

- Recovery inventory: attempt 1 left `f8576f7` (helper-recovered, PHASE2 incident 6), `ed4bf22`,
  `38d1b36`, w1 85/85 and w2 76/78 reports; wave 2 falsified C1's no-harm reading at `28c6837`
  (52 recall losses, 13 crash flips, ~N⁴ hang, 24 pure-data leads, missed `jj -R` writes).
- Attempt-2 registration + frozen guard counter `a2/a2-guards.py` and nine fixtures: `6a7d9ca`;
  before-receipts: `107955e` (`.ufo/waves/round-20/a2/evidence/guards-before-*.txt`).
- Tripwire v3 `3610e3e` (reached-body `lead` sweeps, recursion guard + 2000-follow budget,
  iterative eager walk + deep-stack thread, jj subcommand by index, git short clusters, stdlib
  purity by process denylist, namespace reads, installer `--help`, same-command lead dedup).
- v3.1 `a8960de`: no exemption in unparsed segments (found by the removal-side corpus diff, lesson M15).
- Receipts at `a8960de`, sources S113–S115, lesson M9–M15, QUALITY/SKILL/README/note, w2
  dispositions (`.ufo/waves/round-20/a2/w2-dispositions.md`), SCORECARD/LOG: `94b6925`.

## Landed changes

| Commit | Content | LOG |
|---|---|---|
| `6a7d9ca` | attempt-2 registration, `a2-guards.py`, fixtures | LOG "Round 20, attempt 2" |
| `107955e` | before-receipts | same |
| `3610e3e` | tripwire v3 | same |
| `a8960de` | tripwire v3.1 | same |
| `94b6925` | receipts, docs, sources, lesson, SCORECARD, LOG | same |

Reused after re-run at `a8960de`: precision suite/counter, recall counters, 11 suites + frozen
replays, measure.py, tally-check, isolation check + harnesses/mutants, census, w2 fixture
populations. Discarded: attempt-1's `28c6837` after-readings as C1's final state (kept append-only).

## Before → after measurements

- C1 `tw-precision.py`: `1f7f995` 29/175 = 1.6571 → `a8960de` 172/175 = 9.8286
  (`a2/evidence/precision-a8960de….txt`); target 175/175 **missed by 3**. Guards: recall 6/6 =
  5 observed + 1 lead, 20 controls 0; corpus diff `9c54c56`→`a8960de` 0 lost
  (`corpus-diff-9c54c56-vs-a8960de.json`); `a2-guards.py REV --fixtures-rev 6a7d9ca`
  `28c6837`→`a8960de`: recall_lost 52→0, crash_flip 13→0, pure_rows 24→0, vcs_fn 0→0,
  vcs_fp 31→20; held-out 0/12→2/12.
- C2 `measure.py` c1: 20/28 = 7.1429 → `a8960de` 22/30 = 7.3333 (21/29 if 30′ ruled a swap);
  criterion 29 re-verified (`a2/evidence/iso/`).

## Sources & frontier

`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`: start exit 0
(`.ufo/waves/round-20/evidence/census-start.txt`), end exit 0 (`a2/evidence/census-end.txt`; rerun at lane tip: `ok`, exit 0).
Rows 112 → 115 (tier A +3: S113 os Process Management, S114 json, S115 subprocess.list2cmdline;
opened 2026-10-21); no row touched old→new. Sourced claim: C1's v3 stdlib purity split.
Mistakes mined: M9–M15 (`corpus/lessons/round-20.md`).

## Trend verdicts

- expansion: improved — +3 tier-A rows, two capability rows (`SCORECARD.md` attempt-2 capabilities).
- quality: improved — C1 172/175 with out-of-suite guards clean; target miss stated.
- discernment: improved — wave-2 falsification turned into the removal-side guard and M15; a 30′ scope limit is recorded (M9).

## SHONEN

- [~] claims measured with receipts — `.ufo/waves/round-20/a2/evidence/`
- [~] no axis harmed — harm-watch PASS `a2/evidence/harm/harm-watch-summary.txt`
- [~] sources curated — S113–S115, census exit 0
- [~] mistake mined — lesson M9–M15

## Waves and seats

Attempt 1: w1 85 seats (0 dead), w2 78 seats (2 dead: SentinelPostWaveScan, ConnConsumers) = 163.
Attempt 2: no new wave (≤37 left); one ordinary task call of 8 seats (5 reviewer, 3 critic),
refused three times by the 100-job cap, started on the 4th try; reports pending at
`mado-shokunin/.ufo/waves/round-20/a2/review/` when this report landed. Round total 171.
Installs: none. L0: none. Open: removal-side criterion queued for round 21; 20 VCS false positives remain.

## Residual review update (after report)

CriticRecallV3 (`mado-shokunin/.ufo/waves/round-20/a2/review/CriticRecallV3.md`): **partly falsifies
C1's no-recall-loss reading** — an invoked `functools.partialmethod` spawn is reported by `9c54c56`
and `1f7f995` but silent at `28c6837` and `a8960de` (pre-existing since `28c6837`, not fixed in
attempt 2); all four tools miss a same-line bash `function name { …; }; call`. Open defect for
round 21; C1 admission should weigh it. Other seven review reports were still running.

ReviewV3Diff (`mado-shokunin/.ufo/waves/round-20/a2/review/ReviewV3Diff.md`): **v3/v3.1 introduce
recall losses vs `28c6837`** — a recursive helper call carrying a literal shell string
(`pacman -S pkg`, observed at `28c6837`, clean at `a8960de`: the recursion branch only reads argv
lists) and a swept callback that loses the module literal env (clean + unparsed instead of a lead);
plus new false leads (function passed only to `print`; class target sweeps an uncalled method) and
a read-only `globals()` comparison that still clears bindings. Author verdict for C1 is therefore
revised to **harmed (recall regression vs `28c6837` on two shapes)** pending the closure; fixes are
round-21 work. Remaining six review reports were still running.

CriticPrecisionV3 (`mado-shokunin/.ufo/waves/round-20/a2/review/CriticPrecisionV3.md`): falsified —
18 false `lead` rows at `a8960de` that are clean at `28c6837` (reference sweeps of bodies that never
run), and a purity hole: `imaplib.IMAP4_stream` (stdlib, outside PROCESS_STDLIB) launches a process,
reported at `28c6837`, silent at v3.1. Confirms C1 **harmed** (recall and precision regressions vs
`28c6837` off-suite). Round-21 work: narrow reference sweeps, add process-launching stdlib entries.

CriticAdmission (`mado-shokunin/.ufo/waves/round-20/a2/review/CriticAdmission.md`): C1 172/175 is
below its registered 175/175 target; C2's 30′ green reuses the C1 counter (L 17/18, b14 emits no
lead), so C2 is not independent of C1; held-out 2/12 still includes the `jj log --version` false
positive; it also notes a revision-bound `measure.py` rejection discrepancy (the note's `surface:`
head at `a8960de`, renamed `scope:` only at `94b6925`). Author verdicts after review: C1 harmed,
C2 unprovable-independently (22/30 literal; 21/29 conservative) — admission is the closure's.

ReviewRuntimeV3 (`mado-shokunin/.ufo/waves/round-20/a2/review/ReviewRuntimeV3.md`): **v3.1 memory
blow-up** — 50,000 assignment-only statements and a 20,000-statement cell exceed an 1,800 MiB RSS cap
at `a8960de` (earlier revisions 80–167 MiB) [INFERENCE: `prepare_eval_calls` copies env and bindings
per statement, O(n²)]; no new exit-2; 300-file aged corpus sample max 0.112 s; `huge_bash_cmd`
~82 s at all revisions (parity). Another resource harm for C1; round-21 fix: share snapshots
copy-on-write or snapshot only statements holding a call/reference.

ReviewDocsV3: three documentation defects fixed at lane landing
`c2a306db8a0425925111c46ba2c2083f48e63611`: wave-2 wording now distinguishes 49 certain
recall-loss shapes from one signal-contingent and one old false positive; `rejected=[]`
is pinned to the review's measured `451c7e41` (not tool measurement `a8960de`); the
watchdog citation resolves through `../.ufo/watchdog.log`. Six of eight residual review
reports are committed; ReviewVcsV3 and RerunAllV3 remain outstanding. Final author
verdicts remain C1 harmed, C2 not independently established.

RerunAllV3 independently reproduced precision 172/175, held-out 2/12, recall 6/6
(5 observed + 1 lead), zero control findings, all frozen guard counts, harm-watch PASS,
tally 9/9 and all isolation results at `a8960de`. Its corpus rerun retained zero lost
findings versus `9c54c56` and the same 5 lost / 10 added versus `28c6837`, but whole-corpus
populations and additions changed as live transcripts grew. Historical corpus totals are
observations, not repeatable pinned-population measurements; a frozen manifest/snapshot is
missing. Review landed at `4386045f73ef892bbc01f361c81ac4e8436795be`.
Seven of eight residual reviews are committed; only ReviewVcsV3 remains outstanding.
