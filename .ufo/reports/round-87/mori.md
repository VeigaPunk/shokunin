# mori — round 87 report

lane: mori · round: 87 · attempt: 1 · date: 2026-11-04 · L1: MoriR87
lane repo: `/home/vgpnk/Projects/shokunin/mori-shokunin` · branch `master`
entering revision: `6fc09d69edbb11e5070ff33258de49f062c0fb9b`
final lane HEAD: `1c9de5f56c62f3fa7f88ce00319d3389e3a49053` · remote `refs/heads/master` verified by `git ls-remote`

**Declared claims (2).** C1 — **operability** (score 7): the six clauses the round-87 mutation probe
found surviving in the three r86 counters get the failing arm each, so their selftests move
15/11/22 → 18/13/23 arms. C2 — **calibration** (score 5, tied lowest with depth 5 and freshness 5):
a legacy receipt retires only when a present, problem-free successor reproduces its command in a
clone at its own revision; two r85 receipts become `superseded`, so `legacy=3 → legacy=1`.
Both are frozen in `.ufo/waves/round-87/contract.md` at `142542e0` (amendment A1 at `b9e6f68d`,
pre-data, disclosed). No claim is exploratory; both verify by counting command.

## Work performed

- **C1 operability — the six surviving r86-counter clauses get their arms.** New population-control
  counter `.ufo/waves/round-87/count-c1.py` (18 detector arms, `--selftest` → `C1_COUNTER_SELFTEST
  pass=18 fail=0`) re-derives the six mutants from any revision's bytes and runs each mutated copy's
  own `--selftest`. The population was measured, not guessed: the probe
  `.ufo/waves/round-87/evidence/probe-r87.txt` scores 23 candidate mutants over the three r86
  counters at `6fc09d69` and reports 16 survivors; the six declared are the ones whose clauses the
  r86 arms leave unreached. Armed in the same round: `count-c1.py` +3 (`unanchored_plus_killed_unmet`,
  `zero_mutants_unmet`, `arms_tally_from_subject`), `count-c2.py` +2 (`summary_required`,
  `binding_required`), `count-c3.py` +1 (`derive_keyshape`). Evidence: `C1=met mutants=6 killed=6
  survivors=0 total=6 arms=54` at `03b66a43` (receipt `.ufo/waves/round-87/evidence/after-r87.txt`);
  control `C1=unmet mutants=6 killed=0 survivors=6 total=6 arms=48` at `6fc09d69`
  (`evidence/controls-r87.txt` §C1); wave seat `w1/Mo87E01C1Arms.md` shows each killer is the *new*
  arm and the arm is the sole killer (`FAIL <label>` per mutant, arm absent at `6fc09d69`).
- **C2 calibration — two legacy receipts superseded by replaying successors.** New counter
  `.ufo/waves/round-87/count-c2.py` (17 detector arms) grades a seven-receipt population, replays
  `# replay: required` receipts in a sparse export and `# replay: clone` receipts in a `--shared`
  clone checked out at the receipt's own `# rev:`, and counts a legacy receipt `superseded` only
  when a present, problem-free successor names it in `# supersedes:`. Two successors recorded:
  `evidence/record-sweep-r87.txt` and `evidence/claim-sweep-r87.txt` (both `# rev: 25a74d4c…`).
  Evidence: `C2=met receipts=7 absent=0 bindings=9 bound=9 revs=7 limits=7 cmd=7 summary=7 replay=4
  matched=6 defeated=1 superseded=2 legacy=1 unexpected=0` at `98f48dba`; control `C2=unmet
  receipts=5 absent=2 … superseded=0 legacy=3` at `6fc09d69`; header-only control (correct headers
  and digests, fabricated bodies) reads `matched=4 … superseded=0 legacy=3 unexpected=2`
  (`evidence/controls-r87.txt` §C2). Wave seats: `w1/Mo87E03Baseline.md` (three-revision before/after
  table, all runs byte-identical on re-run) and `w1/Mo87R02ReviewC2.md` (attack).
- **The supersede rule's first defect, caught before data.** The first call site answered
  "superseded" from the successor's *presence*, not its verdict; the header-only control read
  `superseded=2 legacy=1` with both successors failed. Fixed by `supersede_counts` over the
  clean-successor set and armed twice. Fix shown able to fail on one fixture: pre-fix
  `superseded=2 legacy=1` vs fixed `superseded=0 legacy=3`, one call-site line different
  (`evidence/supersede-controls-r87.txt`). Mined as the round's mistake in
  `corpus/lessons/round-87.md` `## Mistakes` (class `supersede-by-presence`) and as QUALITY 181.
- **Frontier step — curated `corpus/SOURCES.md`.** One new row **S603** (git-clone(1), tier A,
  `docs`, `mined`) opened this round: two fetches byte-identical, HTTP 200, no redirect, 107882
  bytes, 3391 lines, sha256 `d31b6c9f…`; two located quotes (18 words at raw 2627-2628, 16 words at
  raw 2696-2699), each occurring exactly once. S600 re-opened (bytes match its registered sha) and
  its `used-by` gained `corpus/knowledge/receipt-supersede-r87.md`. One rejection recorded with a
  flip condition (a second row for S600's URL is a within-scope duplicate). Knowledge entry
  `corpus/knowledge/receipt-supersede-r87.md` + coverage-map row; the claim rests on S603.
- **Inherited state.** No lane-authored leftovers at round start (`jj-lane.sh state`: `tracked=0
  untracked=0`). The round-86 spot-check's eight routed defects are inherited and recorded, not
  re-litigated; its only class that bears on this round's instruments (a cited output the receipt
  does not carry) is answered by every after-value naming its receipt revision and digests.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows the fleet's own
  driver/`.scratch/` state (operator-owned) and no file one of this round's seats wrote into the
  fleet root; the only untracked root entry, `after/`, predates the round and is not mine.

## Landed changes

| Commit | Change | LOG entry |
|---|---|---|
| `142542e0` | freeze: `contract.md`, `count-c1.py`, `count-c2.py`, `evidence/controls-r87.txt`, `evidence/probe-r87.txt` | `LOG.md` Round 87 — claims (frozen `142542e0`) |
| `03b66a43` | C1 subject: the three r86 counters gain the six arms (selftest 15/11/22 → 18/13/23) | `LOG.md` Round 87 — Claims |
| `98f48dba` | C2 subject: the two replay-capable successor receipts | `LOG.md` Round 87 — Claims |
| `b9e6f68d` | contract A1 + the w1 spec/dispatch/ready | `LOG.md` Round 87 — Claims, Frontier step |
| `728bc5f4` | after receipt, `corpus/SOURCES.md` (S603 + S600 used-by), `corpus/README.md`, knowledge entry, lesson, QUALITY 181–182, SCORECARD, `LOG.md` | `LOG.md` Round 87 — Frontier step / No-harm |
| `a42b1d79` | lesson integration: the wave scribe's four findings merged, absent-target arm defect routed to round 88 | `LOG.md` Round 87 — Routed-defect disposition |
| `1523b6cf` | lesson: the material C2 falsifier (target reachable with zero replays) + provenance wording | `LOG.md` Round 87 — Routed-defect disposition |
| `a90126ef` | lesson: deferred TUF source candidate with a flip condition | `LOG.md` Round 87 — Frontier step |
| `859b7e9a` | contract erratum E1 (canonical C2 grading revision; A1 timing corrected) | `LOG.md` Round 87 — Claims |
| `22fa2919` | `SCORECARD.md` planned-88: the three C2 counterfeit paths and the measured counter survivors | `LOG.md` Round 87 — Wave |
| `c05b1cad` | wave evidence: `.ufo/waves/round-87/w1/` (11 seat reports + registry) | `LOG.md` Round 87 — Wave |
| `6056d001` | lesson adjacency block (tameshi/mado/kotodama complements) | `LOG.md` Round 87 — Frontier step |
| `31982062` | wave evidence: 12/12 seat reports, dispatch marker, validator stderr | `LOG.md` Round 87 — Wave |
| `442b108f` | scout report self-corrections (two prose counts) | `LOG.md` Round 87 — Wave |
| `1c9de5f5` | wave results: `w1-results.json` (12/12 settled, zero dead) | `LOG.md` Round 87 — Wave |

All commits went through `/home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh commit … --as mori`
and cite the helper's `landed <hash>` line; the lane identity and remote are verified by
`ls-remote` (below).

## Before → after measurements

**C1 — operability.** Counting command, run at the named revisions:

```sh
python3 -I /home/vgpnk/Projects/shokunin/mori-shokunin/.ufo/waves/round-87/count-c1.py <rev>
```

| | revision | output | rc |
|---|---|---|---|
| before | `6fc09d69edbb11e5070ff33258de49f062c0fb9b` | `C1=unmet mutants=6 killed=0 survivors=6 total=6 arms=48` | 1 |
| after | `03b66a437e68d493ce0aacd1d80c321cc2e6bf7c` | `C1=met mutants=6 killed=6 survivors=0 total=6 arms=54` | 0 |

The after-value is re-derived at `98f48dba` too (`C1=met … rev=98f48dba3267`, rc 0), so C1 does not
depend on C2 landing, and both targets still hold at the lane tip `6056d001` (`C1=met … rev=6056d0010250`,
`C2=met … rev=6056d0010250`, rc 0 each).

The C1 reviewer (`w1/Mo87R01ReviewC1.md`) re-derived the target from the worktree and from a
`--shared` clone, showed every kill is an assertion kill attributable to exactly one new arm, that
each new arm is load-bearing (reverting it makes its mutant survive), that the pre-existing arms
were not edited or weakened (additions only), and that a label-only extra arm is rejected. Its
routed caveats: (i) the per-file arm gate is tally-based, so a same-count substitution that drops a
non-clause arm and adds an inert one still reads `arms=54` (it cannot hide a regression in any of
the six graded clauses); (ii) three kills (M1–M3) are function-contract kills whose CLI tail barely
moves; (iii) M6's branch is exercised by no committed classification token. None falsifies P-C1. Receipt: `.ufo/waves/round-87/evidence/after-r87.txt` (`# replay: clone`,
digests `e2ff9687…` count-c1, `264a43f0…` count-c2).

**C2 — calibration.** Counting command:

```sh
python3 -I /home/vgpnk/Projects/shokunin/mori-shokunin/.ufo/waves/round-87/count-c2.py <rev>
```

| | revision | counter bytes | output | rc |
|---|---|---|---|---|
| before | `6fc09d69` | freeze `073276ee…` | `C2=unmet receipts=5 absent=2 bindings=7 bound=7 revs=5 limits=5 cmd=5 summary=5 replay=2 matched=4 defeated=1 superseded=0 legacy=3 unexpected=0` | 1 |
| bridge | `03b66a43` | A1 `269842f7…` | same counts as the before row, `detector=green` | 1 |
| after | `98f48dba` | A1 `269842f7…` | `C2=met receipts=7 absent=0 bindings=9 bound=9 revs=7 limits=7 cmd=7 summary=7 replay=4 matched=6 defeated=1 superseded=2 legacy=1 unexpected=0` | 0 |

The two ends are labelled with their counter blob because amendment A1 (the C2 counter's subject arm
count, 11 → 13) was needed after C1 changed the same subject file; the bridge row reproduces the
before *counts* with the A1 bytes, so the delta `+receipts2 +bindings2 +bound2 +revs2 +limits2 +cmd2
+summary2 +replay2 +matched2 +superseded2 −legacy2` is caused by the two successor receipts landing,
not by the amendment (`w1/Mo87E03Baseline.md` §4c). Recorded plainly: the counter that certifies the
C2 after-value is committed at `b9e6f68d`, one commit after the measured `98f48dba` — the
certificate is revision-order post-hoc and is named as such.

**Attack finding on C2 (material; reported, not prettified).** The wave's supersede attacker
(`w1/Mo87E02C2Supersede.md`) reached the exact frozen target line with **zero replays**: a
`--shared` clone whose two successor receipts had their `# replay: clone` headers stripped and
their bodies fabricated prints `C2=met … replay=4 matched=6 defeated=1 superseded=2 legacy=1
unexpected=0 rev=85e8bd763281`, rc 0 (fixture `85e8bd76`). Mechanism: the replay is gated on the
receipt's header while the replay *count* and the supersede rule read the population row's declared
mode, and the r87 rewrite of `header_fields` dropped r86's `missing-replay` problem. At the real
revision `98f48dba` both successors do carry `# replay: clone` and both were replayed with bodies
equal to stdout, so the after-value stands; the detector's *refusal* does not. Read strictly
against P-C2's clause ("both `# replay: clone` receipts reproduce their bodies"), the counter
accepts a population where that clause is false, and the claim's instrument is under-implemented.
No post-data edit was made (§9: a rule changed after data is not the claim's rule); the defect is
routed to round 88 with two required arms, and the verdict below is written for the closure to rule
on.

The C2 reviewer (`w1/Mo87R02ReviewC2.md`) verified the supersede *mechanics* independently — all
nine digit bindings verify at each receipt's own `# rev:`, both successors reproduce byte-for-byte
in a fresh clone, a one-field-stale successor stops superseding, and the `after-r85.txt` legacy
reason is honest — and routed three further defects:

- **F1 (high, calibration reproducibility).** The frozen P-C2 sentence is false read literally at
  R = `98f48dba`: the counter committed there still has `SUBJECT_ARMS = 11` and prints `C2=unmet …
  subject=selftest`; `met` exists only with the A1 counter at `b9e6f68d`, a child of `98f48dba`.
  Appended as contract **erratum E1**: the canonical grading form is counter bytes at `b9e6f68d`
  over subject `98f48dba` — exactly what `after-r87.txt` records — and A1's "before any C2
  after-value existed" is corrected to "before any C2 after-value was measured". No target,
  population or rule moved.
- **F2 (medium, rule strength).** The replay binds *body text = stdout of the named command*, not
  *named command = bound tool*: a successor whose `# cmd:` is a literal `printf` while it keeps the
  genuine `tools/mori-record-sweep.py` digest binding prints the full target line (fixture
  `47217847`, rc 0) and retires its legacy receipt. The two committed successors are **not** vacuous
  (their `# cmd:` names the exact tool their digest binds, reproduced independently), so C2's data
  is honest; the rule would accept a counterfeit. Routed to round 88 (require every bound path to
  appear as a `# cmd:` token, plus an arm).
- **F3 (medium-low, hermeticity).** The two r86 `required` receipts replay against the host lane
  path (`--repo /home/vgpnk/…` is skipped by the sparse exporter), so `replay=4` holds on this host
  and would fail in a relocated checkout. The two r87 successors are hermetic (clone mode, relative
  paths). Portability defect, no byte-substitution risk (git objects are content-addressed).

Together with the zero-replay fixture these mean the **C2 instrument is not tamper-proof even though
its measured after-value is honest**; the verdict recorded below is a data verdict, and the closure
should read it with E1 and these three routed defects.

## Sources & frontier

`SOURCES.md` rows before → after, counting command
`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` at the round's own
worktree: **375 → 376**. Census
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`:
**rc 0 before (375 rows, 35 `W04`)** and **rc 0 after (376 rows, 35 `W04`)**, zero `E` codes both
times.

- Rows added by tier: **A +1** (S603, `docs`, `mined`), B +0, C +0.
- Rows touched old→new: **S600** `used-by` `corpus/knowledge/receipt-provenance-r85.md` →
  `corpus/knowledge/receipt-provenance-r85.md, corpus/knowledge/receipt-supersede-r87.md`
  (`status`/`opened`/`recheck` unchanged; bytes re-fetched and byte-identical to the registered
  sha). Rejection: a new row for S600's URL, duplicate scope, with a flip condition.
- Frontier rows advanced: **FR9** (durable fixture evidence) — the clone-replay mode is a
  reproducible-by-construction replay, and the tree-versus-clone measurement is committed; **FR3**
  (settlement evidence) unchanged. `PROVINCE.md` scope unchanged: this is evidence integrity inside
  the lane's own instruments, detection and report only.
- Knowledge: `corpus/knowledge/receipt-supersede-r87.md` (decision table + limits), coverage-map row
  in `corpus/README.md`. Mined mistake: `corpus/lessons/round-87.md` `## Mistakes`. Census of
  mistakes: one, with a rebuildable fixture (`evidence/supersede-controls-r87.txt`).
- `Assimilation: none` — no `merge/mori/` package adopted this round; `/home/vgpnk/Projects/shokuknow`
  was not written, fetched or pushed.
- `considerthese/2026-10-26.md` suggestion 3 ("re-execute what closures only evidence-verified") is
  the C2 rule's standing motivation and is cited by QUALITY 181.
- **Adjacency (connector, `w1/Mo87K01Conn.md`):** two complements named, neither absorbed —
  tameshi's `receipt-revision-gate.py` carries eleven refusal codes of which mori implements one
  (`RECEIPT_CONTROL_NOT_ANCESTOR`), and mado's `mado-tripwire.py --frozen` replays a pinned verdict
  while explicitly disclaiming snapshot provenance, the gap mori's `body == out` reopens for its own
  receipts. kotodama's receipt grammar is disjoint (no `# cmd:`), so no single receipt serves both.
  Recorded in `corpus/lessons/round-87.md` `## Adjacency`; no sibling claim is contested.

## Trend verdicts

- **expansion: improved.** One admitted knowledge entry on ground the coverage map did not hold
  (`corpus/knowledge/receipt-supersede-r87.md`, map row appended), grounded on a new tier-A row
  (S603); registry 375 → 376, append-only, census rc 0. The entry carries ground the lane did not
  hold: the replay *environment* rule and the supersede rule with their measured split.
- **quality: improved, with one material falsifier reported.** Both frozen targets are met in the
  digest-bound after receipt; two counters
  gained 18 and 17 detector arms; the six r86 subject arms are each shown to be the sole killer of
  their mutant (`w1/Mo87E01C1Arms.md` §5); the receipt body of every after-value is bound to its
  command by `# replay: clone`. **Falsifier:** the C2 target line is reachable with zero replays by
  stripping the `# replay:` headers (`w1/Mo87E02C2Supersede.md`, fixture `85e8bd76`), because the
  r87 grammar lost r86's `missing-replay` refusal — so the claim's after-value is measured but its
  detector is not tamper-proof. Other named gaps: the absent-target arm defect (routed), the
  call-site limit of the supersede rule, and the C2 certificate's revision-order gap.
- **discernment: improved.** The round's own header-only control caught a defect in the rule it was
  validating *before* data and the fix is shown able to fail; a rejection is recorded with a flip
  condition; the before/after table labels each end with its counter blob instead of presenting one
  number for two byte-sets. The wave's critique and review seats are the lane (dispatched seats do
  not count as outside verification); the non-author closure remains the outside check.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `SKILL.md` registry rows 1–20 plus `corpus/QUALITY.md` criteria 181–182 and
  `corpus/knowledge/receipt-supersede-r87.md`'s decision table; no named non-author verifier for
  this round's addition.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 87 (both
  claims, the frontier step, the no-harm read).
- [~] Instructions executable by an agent without oral context — the counters are `python3 -I … <rev>`
  and `--selftest` with usage text, and the lesson records the exact commands; evidence
  `.ufo/waves/round-87/evidence/after-r87.txt`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; the new
  knowledge entry's Limits say the rule is receipt-level for this lane's own evidence and not a fleet
  lifecycle, result-acceptance or authorship verdict; no remediation added.

## Round shape, wave evidence and seats

- **Shape:** one v1 wave (`w1`) under `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy.json`
  (band 8–16), validated by `ufo-swarm-wave.mjs run` → `w1-dispatch.json` with `counts.total = 12`.
  Spec `w1-spec.json`, reports `.ufo/waves/round-87/w1/`, results `w1-results.json`. Residual call:
  none — the 12 seats are the round's L2 floor and ceiling; no `task` call was made by the lane.
- **Role mix (12):** 3 executor, 1 simplifier, 1 scout, 2 scribe, 2 reviewer, 1 critic,
  1 mutation-tester, 1 connector. Attack seats: 4/12 = **33.3 %** (≥25 %); connector seats: 1 (≤2).
  The planner seat is held by the L1 (frozen-topology seat, validator-rejected as a swarm role).
- **Seats landed (12 of 12):** `Mo87E01C1Arms` (C1 kills/sole-killer), `Mo87E02C2Supersede`
  (supersede fixtures; found the zero-replay path), `Mo87E03Baseline` (three-revision table),
  `Mo87K01Conn` (sibling scan: tameshi/mado/kotodama complements), `Mo87M01Mut` (52-mutant matrix;
  survivors listed in SCORECARD planned-88), `Mo87R01ReviewC1` (C1 attack; target stands),
  `Mo87R02ReviewC2` (C2 attack; F1–F3), `Mo87S01Lesson` (lesson), `Mo87S02Sources` (S600/TUF
  screening), `Mo87Si01Simplify` (dead weight; the C2 grading core is unreachable from `--selftest`),
  `Mo87C01Critic` (cheap paths), `Mo87Sc01Scout` (55 unarmed clauses ranked for round 88; not used by
  either claim). `w1-results.json` (committed at `1c9de5f5`) records `seats: 12` and twelve
  completed outputs; **dead seats: 0**; no seat was replaced.
- **Critic (cheap-path) result:** both frozen targets are reachable by fabrication — C1 with three
  submitting subjects whose selftests print tallies they never assert (`arms=54`, P2) and C2 with two
  `echo`-bodied receipts carrying `# replay:`/`# supersedes:` headers (P6) or with two header lines on
  already-clean receipts (P7). That is the expected trust boundary of a counter that grades
  self-reported tallies and committed receipt bytes; the round's defence is that the *committed*
  data is what it is, and the two reviewers replayed it independently (nine bindings verified, both
  successors reproduced byte-for-byte). It is reported, not softened: the counters are discriminators
  against an honest population, not against a forger.
- **Round total:** 12 seats + the L1; **dead seats: 0** (`w1-results.json`).
- **Tool installs:** none. No `pacman` transaction was run (host-wide pause respected); no
  `uv`/`npx`/binary install this round.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. `next/` advanced 87 → 88 by the
driver after closure; this report covers round 87 only.
