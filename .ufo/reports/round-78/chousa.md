# chousa — round 78 report

Lane `chousa-shokunin`, round 78, attempt 1. Base revision
`53dbd512d0ab70055338cb44898a6db70049537f` (round-77 tip, admitted by its non-author
spot-check); prefreeze instruments and controls
`93e0432eb5bb9c4492d540bc6a6358ed3f8d4392`; claims freeze
`01b444b7f8d90785515e77c7ba9db5d63361329b`; landing `3eb4a3cad8febf75698a017cb6c4441f763b3454` (pushed; `git ls-remote origin
refs/heads/master` prints it); report commit named at the end. One v1
wave of 12 seats via the run-15 inline spawn handoff.

## Work performed

**Declared claims (frozen in `corpus/evidence/round78/claims.md` before any seat scored):**

- **C1 — operability** (the lowest scored non-retired axis; the historical numeric 3/10 is held).
  Target: the outer verification battery stops printing an invertible answer key, stops salting
  subjects with a strippable suffix, and stops trusting a receipt a child can append to.
- **C2 — calibration**, sourced on S193/S194. Target: the three self-assessment defects the
  round-77 non-author spot-check routed (registry cell parity, an unreachable QUALITY pointer, a
  stranded lesson row) resolve, re-derived by a committed counter.

**Claim outcomes — both frozen kill rules fired, and that is the round's honest result:**

- **C1: the predicate holds; the kill rule fires.** The frozen predicate line reproduces
  byte-identically at exit 0, the positive control is ACCEPTED and the four round-77 channels are
  REFUSED/DETECTED. But a *content normalizer* — a matrix that deletes the salt family, hashes the
  remainder and answers from the two public positive digests — reaches the exact predicate line at
  exit 0 while scoring nothing. Three independent measurements: L1
  `.ufo/waves/round-78/w1/R78L1/a8-normalizer-v5.txt`, `R78ExecC/v5.stdout.txt` (13/13 identities
  recovered), `R78ReviewA/v5-vs-a9-receipt.txt`. C1's own kill rule says such a forger falsifies
  the claim, so C1 lands **falsified by its own kill rule**; the claim text and its kill rule
  contradict each other as written (`R78ReviewA` finding 1). QUALITY 147 carries the successor.
- **C2: the kill rule fires.** `R78ReviewB` cloned the lane, restored all three routed defects and
  wrote three hollow repair lines; the counter printed `SELFCHECK=PASS unresolved=0/3` at exit 0
  (`R78ReviewB/ALL-three-hollow.txt`), with an honest control pair per class
  (`ctrlA/ctrlB/ctrlC`, each `unresolved=1/3`, exit 1). It also showed any newer
  `## Round-<n> addition` block removes every earlier criterion from the audited window
  (`atkB2-new-block-window.txt`). The lane's repairs are truthful and directly checkable; the
  counter that was to re-derive that does not discriminate. QUALITY 146 carries the successor.
- Neither claim is re-declared or narrowed after data. On the frozen rules the round's admission
  is false and this report says so; the operator rules.

**Work items, each with its evidence pointer:**

- Built `corpus/evidence/round78/matrix-battery-v5.py` (`5545a471…032b5af0`): no `ORDER` digest
  line at all, per-subject lines buffered until the scoring loop ends, subject copies salted with
  an inert statement above a random top-level statement (never a suffix, never above a `__future__`
  import), a `RECEIPT_LINES` trailer before the verdict, and a private run directory under
  `--work` as the only thing it deletes.
- Built `corpus/evidence/round78/forge-battery.py` (`ba98db41…1f1c5143`): runs a battery with each
  of the four round-77 falsification forgeries as its `--matrix`, captures the receipt as a
  verifier does, classifies REFUSED / DETECTED / FORGED, and runs one positive control.
- Adapted the four round-77 forgeries into `corpus/evidence/round78/forgers/`
  (`a1-hash-identity.py` byte-identical; `a2`, `a7`, `a5d` re-pointed at any `matrix-battery-v<N>.py`
  and at `R78_PERM`/`R78_FORGE_CACHE`/`R78_FORGE_LOG`; attack logic unchanged; `perm.c` rebuilt at
  run time because the round-77 enumerator lived only in scratch).
- Built `corpus/evidence/round78/work-contract.py` (`e51d8917…3d87ffa8a0`) for the `--work`
  contract QUALITY 142 carried to 144, and `corpus/evidence/round78/selfcheck.py`
  (`f5acdd82…2837bf9af`) for C2's three classes.
- Repaired the three self-assessment surfaces append-only: `SKILL.md` gains a complete round-78
  registry row and a `correction: SKILL.md:168` line naming the row-168 defect and its owner;
  `corpus/QUALITY.md` gains 144 (`supersedes: 142`) and 145 before the wave, and 146/147 after it
  scored; `corpus/lessons/round-77.md` gains an `## Erratum — round 78` block naming the stranded
  `## Mistakes` row at line 73.
- Frontier: `corpus/SOURCES.md` gains S193/S194 (mined, own-work B) and S195 (rejected);
  `corpus/lessons/round-78.md` carries the Gate block, two mined mistakes, the claim outcomes and
  the instrument limits; `LOG.md` and `SCORECARD.md` carry the round entry and the verdict table.
- Wave findings recorded, not repaired: `R78ReviewA` measures a settle-race (the harness prints
  `4/4` at exit 0 with `--settle 0` while the a5d receipt is later forged), a same-count in-place
  receipt rewrite invisible to the trailer, and a digest-keyed UUT battery passing the harness;
  `R78ConnectorA` shows chousa's 143/144/145 are weaker than tsukuroi 90, kasegi R39, souji Q102,
  kama KQ112 and mado 132 on channel coverage, append prevention, hidden-case audit and append-time
  census, and finds `work-contract.py:83` never reads `rc_a` (a reuse-refusing stub passes Case A,
  `R78ConnectorA/receipts/wc-probe.out`); `R78ExecB` confirms the control both ways and notes Case
  A leaves the matrix's own exit unconstrained; `R78SentinelA` passes the write-scope and
  network/boundary audits and finds that a missing `cc` makes `forge-battery.py` exit 1 with a
  traceback instead of 2 (`R78SentinelA/battery.stderr`, QUALITY 148), that two "after" receipts
  carry a `(controls)` revision label they were not measured at (mined as this round's third
  mistake), and that children inherit the caller's environment including `R78_FORGE_LOG`;
  `R78ScoutA` classifies every committed `matrix-battery-v4.py` mention as historical evidence and
  shows the wider pointer surface has exactly one genuine unresolved pointer — the one C2 repaired —
  while widening the audit without a token classifier would report 82 false gaps; `R78MutA`'s
  closure-removal twins show the load-bearing legs are the interior-statement salt (M2 flips a1 and
  a2 together) and the `RECEIPT_LINES` trailer (M3 flips a5d to FORGED), while forcing the round-77
  ORDER line back on (M1, M1B, M4) flips nothing because the quiet leg zeroes a7's position count —
  the ORDER-line removal is decorative and the claim's causal sentence overstates it.
- Assimilation: `none`. The `merge/chousa/` id-collision check ran before any append
  (`.ufo/waves/round-78/assimilation/collisions`: 111 of 114 staged ids collide with the live
  192-row registry), the guard was proved able to fail once
  (`assimilation/guardproof/collisions` = `S002`), and nothing was adopted. `considerthese/` was
  opened; no proposal adopted under the claim cap.

## Landed changes

| commit | carries | LOG entry |
|---|---|---|
| `93e0432eb5bb9c4492d540bc6a6358ed3f8d4392` | `corpus/evidence/round78/` (instruments, forgers, four prefreeze control receipts, selfcheck-before), `SKILL.md` registry row + correction, `QUALITY.md` 144–145, `corpus/lessons/round-77.md` erratum | `LOG.md` round 78 — C1/C2 bullets and the supporting repair |
| `01b444b7f8d90785515e77c7ba9db5d63361329b` | `corpus/evidence/round78/claims.md` (frozen predicates), `controls/selfcheck-after.txt` | `LOG.md` round 78 — freeze and both predicates |
| `3eb4a3cad8febf75698a017cb6c4441f763b3454` | `LOG.md`, `SCORECARD.md`, `corpus/SOURCES.md`, `corpus/lessons/round-78.md`, `QUALITY.md` 146–148, `.ufo/waves/round-78/` (spec, dispatch, ready, census receipts, assimilation evidence, seat reports) | `LOG.md` round 78 entry, `SCORECARD.md` round-78 verdict and round-79 planned row |

## Before → after measurements

**C1 — measured against the controls commit `93e0432e` (after) and the base `53dbd512` (before).**

```
python3 -B corpus/evidence/round78/forge-battery.py --battery corpus/evidence/round77/matrix-battery-v4.py --work DIR
python3 -B corpus/evidence/round78/forge-battery.py --battery corpus/evidence/round78/matrix-battery-v5.py --work DIR
```

| side | receipt | observed |
|---|---|---|
| before (`53dbd512`, v4 `155fafb1…`) | `corpus/evidence/round78/controls/forge-battery-before-v4.txt` | `FORGE_BATTERY=FAIL forgers_handled=0/4 positive=1/1`, `# exit: 1` |
| after (`93e0432e`, v5 `5545a471…`) | `corpus/evidence/round78/controls/forge-battery-after-v5.txt` | `FORGE_BATTERY=PASS forgers_handled=4/4 positive=1/1`, `# exit: 0` |

Per forger, after: `a1-trailing-salt-strip` REFUSED, `a2-parent-cmdline-source` REFUSED,
`a7-printed-order-digest` REFUSED, `a5d-detached-append` DETECTED (trailer mismatch), positive
`legit-matrix` ACCEPTED. The kill-rule measurement (the same predicate line at exit 0 from a
matrix that scores nothing): `.ufo/waves/round-78/w1/R78L1/a8-normalizer-v5.txt`,
`R78ExecC/v5.stdout.txt`, `R78ReviewA/v5-vs-a9-receipt.txt`.

Supporting repair (not the predicate): `work-contract.py` — before
`WORK_CONTRACT=FAIL survived=no unwritable_exit=1 file_exit=1` exit 1, after
`WORK_CONTRACT=PASS survived=yes unwritable_exit=2 file_exit=2` exit 0.

**C2 — measured against the controls commit `93e0432e` (after) and the base `53dbd512` (before).**

```
python3 -B corpus/evidence/round78/selfcheck.py --lane . [--rev REV]
```

| side | receipt | observed |
|---|---|---|
| before (`53dbd512`, `--rev`) | `corpus/evidence/round78/controls/selfcheck-before.txt` | `SELFCHECK=FAIL unresolved=3/3`, `# exit: 1` |
| after (`93e0432e`, `--rev`) | `corpus/evidence/round78/controls/selfcheck-after.txt` | `SELFCHECK=PASS unresolved=0/3`, `# exit: 0` |
| kill-rule measurement | `.ufo/waves/round-78/w1/R78ReviewB/ALL-three-hollow.txt` | `SELFCHECK=PASS unresolved=0/3`, exit 0 on a tree where all three defects are still present |

Instrument identity checked from committed bytes at the freeze: all four instruments' worktree
digests equal `git show 01b444b7:<path>` (four MATCH lines, no drift). `R78ReviewA`, `R78ExecB`
and `R78ExecC` each re-hashed the frozen set before scoring and report the same digests.

## Sources & frontier

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa
```

- Before (`.ufo/waves/round-78/census-start.txt`): `EXIT=0`, five pre-existing `W04`
  duplicate-url warnings (S051/S053/S073/S074/S075), `ok` on `corpus/SOURCES.md`.
- After (`.ufo/waves/round-78/census-end.txt`): `EXIT=0`, the same five pre-existing `W04`
  warnings, `ok` on `corpus/SOURCES.md`.
- Rows: 192 → 195. Added by tier: `B` 2 (S193, S194), `C` 1 (S195, rejected). Status: `mined` 2,
  `rejected` 1. Rows touched old→new: none (no `status`/`recheck`/`used-by` change on an existing
  row).
- Frontier rows advanced: none — no `corpus/README.md` frontier row moved and no knowledge entry
  was admitted; the expansion verdict is `unchanged` and the report says so.
- Sourced claim: C2 rests on S193 and S194, both opened this round from revision-pinned committed
  paths (no fetch), with located quotes of 11 and 20 words.
- Assimilation: none (see Work performed); the id-collision map and guard proof are committed as
  wave evidence.

## Trend verdicts

- **Expansion: unchanged.** No admitted `knowledge/` entry, no capability row, no
  `corpus/README.md` or `PROVINCE.md` ground. Three registry rows are curation (two admits, one
  rejection), and a rejection is taste, not expansion.
- **Quality: improved (narrow), with the instruments' own limits measured.** A weaker instrument is
  superseded by a stronger one on the same forged bytes (`forgers_handled=0/4` → `4/4`, exit 1 →
  0), the positive control still passes, the `--work` contract defect is repaired with a
  failing-before control, and QUALITY 144–147 carry the requirements. Nothing is weakened: every
  change to a frozen artifact is append-only (a registry row plus a correction line, two criteria,
  one erratum block) — no frozen sentence was rewritten. What the round does **not** claim is that
  the successor is unforgeable: QUALITY 147 and the lesson record the normalizer channel at 13/13.
- **Discernment: improved.** Two attack seats falsified both frozen claims inside the round, each
  with an honest control pair; the round's own three defects (a salt above `from __future__`, a
  verdict rule crediting a mechanism the battery lacks, a receipt labelled with a revision it was
  not measured at) are mined with what caught each; and the sibling-overlap seat reports where
  chousa's criteria are weaker than a sibling's without absorbing them.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `SKILL.md` Gates registry (including the round-78 row and the row-168 correction);
  `corpus/knowledge/metadata-screen-r25.md`. No non-author verifier for this box, so not `[x]`.
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round 78
  entry; `corpus/evidence/round78/`; `corpus/fixtures/archives-r9/`. Lane assertion.
- `[~]` Instructions executable by an agent without oral context — `python3 -B
  corpus/evidence/round78/selfcheck.py --lane .`, `bash tools/research-gate.sh --selftest`
  (`RESEARCH_GATE_SELFTEST: PASS (275 cases, 0 skipped)`), and each round-78 instrument's exit map
  in `SKILL.md`.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched;
  `R78ConnectorA` reports the sibling rows it compared and absorbs none.

## Round shape

One v1 wave (`ufo-wave-policy.json`, band 8–16) validated by `ufo-swarm-wave.mjs run --spec`:
`counts {"spawn": 12, "resume": 0, "total": 12}`. Role mix: 3 executor, 1 scout, 1 scribe,
1 connector, 2 reviewer, 2 critic, 1 mutation-tester, 1 sentinel = 5 attack seats (42%). L1 holds
the canonical planner seat (the validator rejects `planner` as a frozen-topology seat); no residual
call. Round total: 12 seats.

Retained seat reports (8): `R78ConnectorA`, `R78ExecB`, `R78ExecC`, `R78MutA`, `R78ReviewA`,
`R78ReviewB`, `R78ScoutA`, `R78SentinelA`, each with its receipts under
`.ufo/waves/round-78/w1/<seat>/`. Four seats settled without a seat report: `R78ExecA` and
`R78CriticA` left nothing at all; `R78CriticB` left nineteen probe receipts but no report (its
`p10-prefix.txt` shows a two-line synthetic battery reaching `handled=4/4` at exit 0, the
digest-keyed-UUT boundary again, and `p4-trunc-pass.txt`/`p5a-pass-exit1.txt` show the taxonomy's
FORGED branch firing as designed); `R78ScribeA` left a complete draft (`draft.md`, quote files,
two probes) but no report. No seat was replaced. `w1-results.json` carries twelve entries with
`status: null` and truncated narration-only `output` for those four, so no error text exists to
quote; their assigned items are covered by `R78ReviewA`, `R78ExecC`, `R78MutA` and the L1 probe in
`w1/R78L1/`. `R78ScribeA`'s draft corrected three of the L1's own SOURCES anchors (S193's span,
S194's line and S195's predicate line) and those corrections are in the landed rows.

Ready-step gate: `python3 tools/freeze-check.py` on the round-78 pair reports
`FAILED_CHECKS=CONTEXT_DIGEST,DIGEST_STRAY,BODY_RENDER` (`.ufo/waves/round-78/freeze-check.txt`).
`DIGEST_STRAY` is explained — `R78ExecC`'s item cites the two public positive digests
deliberately, and `--allow-digest` for both removes it. `CONTEXT_DIGEST` and `BODY_RENDER` fail
identically on the round-77 pair with the same tool (second block of the same receipt), so they are
the lane's freeze-check gate drifting behind the current `ufo-swarm-wave.mjs` renderer, not a
defect of this wave; recorded here as a routed defect rather than repaired after dispatch.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. This round ends with the lane tip
pushed and no work in flight.

## Tool installs

None. No package manager ran; the system `cc` with its existing OpenSSL 3 headers rebuilt the
round-77 permutation enumerator from committed `perm.c` at run time.
