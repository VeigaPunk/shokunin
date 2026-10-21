# kagi — round 24 report

Lane `kagi-shokunin`, BASE `4f94b52a3cdfaa289d779bd8a2afcd0b1fcd9105`; lane tip `2b8a7d52e686a829777c77743c561daaaef69d4a`; code/data measured commit `6c23a56dea0f68dfb93d793a7de440a3ac5bb7b5`. Driver: hyaku-inline, attempt 1. No earlier attempt (`lane-dead-no-report kagi round=24` absent); nothing inherited.

## Work performed

Declared claims (frozen in `kagi-shokunin/plans/round-24.md`): **C1 operability** — safe-by-default `claim-ledger.sh verify`/`cells` (routed D4, plus the audit's R11-08 red, single-backslash guard and SKIP-SELF/rows_run debts); **C2 freshness** — the 16 historical in-row pins (S001–S016) are recaptured and classified under one declared normalizer (D5, D6; sourced, S027–S031); **C3 calibration** — membership identity for the 15 count-only ledger rows (audit: R12-03, R21-04, R22-03/04, R11-10/11). All axes are tied at 9, so each claim is on a lowest non-retired axis. The L1 held the frozen planner seat; the planning data walk rode the wave-1 connector and revenger items.

- C1: `kagi-shokunin/corpus/claim-ledger.sh` adds `[host]`/`[substrate]` HOST-SKIP by default, with `--allow-host-rows` as the only consent. It refuses POLICY `untagged-host`, `host-path` (`~`, absolute, `..`), `bash-option` and `script-symlink`. The single-backslash guard is fixed. SKIP-SELF now fires only on an actual invocation, and `rows_run` counts executed rows only. Citations split quote/comma lists and resolve `.ufo/` lane-first. 19 new selftest cases bring the total to 140. R18-01 is tagged `[host]`; R18-02 is rewritten without a backslash. Landed in `a3eb6c75` and `735123d5`.
- C2: `kagi-shokunin/corpus/rendered-text-v1.py` is the single declaration (20 cases; uses the round-23 opener). It reproduces 10/10 of the round-23 normalized digests (`kagi-shokunin/.ufo/waves/round-24/normalizer-replay.json`). Added: 16 capture rows in `corpus/source-fetches.tsv`; `corpus/inrow-pins.tsv`; census `SC_INROW`, which recomputes each verdict, restricts the exemption to S001–S016 and adds the `captures/inrow/inrow_only/inrow_nonreproducing` fields (11 cases, 70 total); and S027–S031.
- C3: `kagi-shokunin/corpus/row-identity.sh` plus ledger rows R24-03..R24-16 (count and sha256 per membership). The old rows are kept. Migrations: `.ufo/waves/round-24/expectation-migrations.json`.
- Routed D1–D8: D1 SCORECARD main capabilities row; D2 SKILL.md §Gate registry — round-23/24; D3 R24-02 plus `final-verification.json` with a per-run `measured` revision; D7 all evidence committed (`2b8a7d52`) before this report; D8 explicit Gate rejects, plus R24-C1..C4 plan corrections in `corpus/lessons/round-24.md`. QM15–QM18 are appended to `corpus/QUALITY.md`, each backed by a lesson.
- Spot-check (`corpus/lessons/round-23-verifier-spotcheck.md`): every routed defect is fixed or turned into a criterion. The spot-check's "S008 non-reproducing" reading was wrong: S008 reproduces raw (R24-C4, M24-1).

## Landed changes

| commit (helper `landed`) | LOG.md entry | content |
|---|---|---|
| `a3eb6c756dcc14470442e719d86fb1beadf561ec` | LOG §Round 24 | C1/C2/C3 candidate, docs, wave-1 evidence |
| `735123d532387caccdbf04cb0303217d2483de73` | LOG §Round 24 (M24-6) | python allowlist regex for rendered-text-v1 (the comment had changed, the code had not) |
| `ce9c544d167d392cd34aeb102cb2d134fb439ed4` | LOG §Round 24 | restamp after a seat mutated `surface-census.tsv` in place |
| `6c23a56dea0f68dfb93d793a7de440a3ac5bb7b5` | LOG §Round 24 (M24-7) | R24-13 note no longer spells the tag; lesson outcome |
| `2b8a7d52e686a829777c77743c561daaaef69d4a` | — (evidence only) | final verification and remaining wave-1 reports |

## Before → after measurements

| claim | counting command | before (BASE `4f94b52a`) | after (revision) |
|---|---|---|---|
| C1 | `bash .ufo/waves/round-24/tools/host-tripwire.sh <label> <rev>` (scratch clone, host scripts stubbed, HOME scratch) | `total=35` (verify absent 1, present 22; cells 1/11) | `total=0 complete=4/4`, verify `population_skipped=12/12` (`735123d5`; gate code unchanged since) |
| C1 | `bash corpus/claim-ledger.sh citations` | `unresolved=2` | `unresolved=0` (`6c23a56d`) |
| C1 | real-tree `env -i PATH HOME=<scratch> bash corpus/claim-ledger.sh verify` | not runnable (QM12 forbade it) | exit 0 `CLAIM_LEDGER: CLEAN (claims=61 … host_skipped=12)` (`6c23a56d`) |
| C2 | rows whose only provenance is an in-row pin (SOURCES.md × source-fetches.tsv) | 16 | 0; census `captures=31 inrow=16 inrow_only=0 inrow_nonreproducing=12` (`6c23a56d`) |
| C2 | named non-reproducing in-row pins | 5 of 12 | 12 of 12, verdict recomputed by SC_INROW |
| C3 | `python3 .ufo/waves/round-24/tools/identity-swap.py <label> <rev>` | `survived=15 killed=0 invalid=0` | `survived=0 killed=15 invalid=0` (`6c23a56d`) |

Evidence: `kagi-shokunin/.ufo/waves/round-24/final-verification.json`, `tripwire-*.txt`, `identity-*.txt`, `verify-final.txt`.

## Sources & frontier

`SOURCES.md` rows 26 → 31: S027, S028, S029 and S031 are tier A/mined, and S030 is tier A/rejected (an ASCII-whitespace collapse reproduces only 7 of 10 recorded digests). By tier: A +5, B 0, C 0. Counting command: `bash corpus/sources-census.sh` (R21-02). No existing row's status, recheck or used-by changed, so there are no old→new entries. S001–S016 were reopened and recaptured, and new frontier path "rendered-text-v1 declaration" was added. Fleet census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi`:
- start: reproduced after the fact on a BASE clone (M24-4) → exit 0, `kagi ok` plus 7 W04 duplicate-url warnings (S019–S023, S025, S026).
- end: exit 0, `kagi ok` plus the same 7 W04 (`.ufo/waves/round-24/census-end.txt`).

The sourced claim is C2 (S027–S029, S031); the mined mistakes are M24-1..M24-7 in `corpus/lessons/round-24.md` §Mistakes.

## Trend verdicts

- expansion — **unchanged**: no new knowledge entry and no governed surface. The new rows ground tooling.
- quality — **improved**: the normalizer is declared once with sources and reproduces 10/10. 16 legacy pins are recaptured and 12 named non-reproducing. The ledger's real-tree `verify` runs CLEAN without host reads.
- discernment — **improved**: the Gate records 6 explicit rejects, one demotion and S030. The 15/15 count-preserving swaps that the ledger used to admit are now all refused, with pristine controls still admitted. No outside agreement is self-certified; non-author verification remains pending.

## SHONEN

- [~] Box 1 — `kagi-shokunin/SHONEN.md`; evidence `final-verification.json` (no non-author verifier this round)
- [~] Box 2 — `corpus/QUALITY.md` QM15–QM18 with lessons
- [~] Box 3 — real-tree `verify` CLEAN at `6c23a56d` (`verify-final.txt`)
- [~] Box 4 — `corpus/lessons/round-24.md` §Mistakes

## Waves, seats, safety

- Wave 1 (build): 67 seats validated under policy v2. Mix: 29 scout, 15 reviewer, 5 executor, 4 revenger, 4 critic, 4 scribe, 3 connector, 2 sentinel, 1 mutation-tester. The first dispatch was refused in full ("Background job limit reached (100)", 0 started); the same payload was retried about 3 minutes later and all 67 started.
- Dead seat: ProbeAbsPath (`Retry budget exhausted … Codex is at capacity (turn_rate_limit_exceeded)`), not replaced. 61 reports were committed. 5 Ident seats were still running at report time (IdentR1605/1702/1802/2104/2204); their reports, if they land, are uncommitted.
- **Wave 2 (falsify) was not dispatched**: the L1 run budget ran out. Its residual checks were the L1's own re-measurements on committed revisions. Those runs caught M24-6 and M24-7 before landing. Round total: 67 seats.
- Seat deviations: IdentR1111 edited the live `corpus/surface-census.tsv` once, restored it, and admitted it. IdentR1604 ran a default `verify` in a BASE scratch clone without an isolated HOME. Both are disclosed in the lesson, and no value was copied. No vault, account or handler action was taken, and no credential was read.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed no kagi seat files (none moved).
- Tool installs: none. No pacman use. Stale-lane: respawn-per-round driver; no other mission of this lane is open. L0 questions: none.
