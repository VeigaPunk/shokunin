# chousa — round 79 report

Lane `chousa` (deep-research method), round 79, attempt 1. Base
`ee70e6df19fe43b1b384166cf5d360c3b99dafe2` (round-78 lane tip); prefreeze instruments, controls
and repairs `e2bf2bbb5ca66f06b6571cbcaa15554d1a74a67c`; claims freeze
`b58a02dbc8876dd1ad7647d88ca2c9cb2ae51ff9`; landing commit `LANDING`.

**Round result in one line: both frozen predicates hold on the bytes they count, and both frozen
kill rules fired on inputs the predicates do not enumerate — the round's admission is false on the
rules declared before data.**

## Work performed

The round declares **two claims on two distinct axes**, frozen before any seat scored in
`corpus/evidence/round79/claims.md`:

- **C1 — operability** (lowest scored non-retired axis; the historical numeric 3/10 is held).
  Round 78's outer battery salts the *source text*, so one four-line normalizer recovers every
  subject byte-for-byte; the successor's subject copy must stop being a textual derivative of a
  committed file, while the legitimate matrix is still accepted and one text-level normalizer per
  salt family is refused. Sourced on **S196** (QUALITY 147).
- **C2 — calibration.** Round 78's self-assessment counter accepts presence-only repair lines and
  audits only the newest `## Round-<n> addition` block; the successor must validate every repair
  line against the bytes it names and audit every block. Sourced on **S197** (QUALITY 146).

Work items, each with its evidence pointer:

- **The v6 outer battery.** `corpus/evidence/round79/matrix-battery-v6.py` (`bb91406e…a61e1d`)
  keeps the round-78 order, quiet, content and receipt legs and replaces the salt with
  re-emission: parse the subject, drop every docstring, rename every bound identifier through a
  fresh per-copy table (imports, keyword-argument names, builtins and dunders excluded), insert one
  random-named integer assignment after the last `__future__` import, compile under a random file
  name and write a wrapper that `exec`s the marshalled code object. No 40-byte window of a copy
  occurs in its source (`controls/derivative-after-v6.txt`: `DERIVATIVE_COPIES=0/13
  MAX_WINDOW=23`, exit 0) against `13/13 MAX_WINDOW=4096` exit 1 for v5
  (`controls/derivative-before-v5.txt`); the 23 shared bytes are the shebang line
  (`.ufo/waves/round-79/w1/R79ReviewA/receipts/maxwin.out`).
- **The six-forger battery, one normalizer per salt family.**
  `corpus/evidence/round79/forge-battery.py` (`5761edc5…fc936`) carries the four round-77/78
  channels plus `a8-v5-salt-normalizer.py` (the round-78 `_r78<hex>` family, recovered from
  `.ufo/waves/round-78/w1/R78L1/a8-normalizer.py`) and
  `a9-v6-wrapper-normalizer.py` (the round-79 wrapper family), with the positive control
  (`corpus/evidence/round76/loader-matrix-v3.py`) still required to be ACCEPTED.
  `controls/forge-battery-before-v5.txt` → `FORGE_BATTERY=FAIL forgers_handled=5/6 positive=1/1`,
  exit 1, `a8 … verdict=FORGED`; `controls/forge-battery-after-v6.txt` →
  `FORGE_BATTERY=PASS forgers_handled=6/6 positive=1/1`, exit 0.
- **The v2 self-assessment counter.** `corpus/evidence/round79/selfcheck-v2.py`
  (`b99ccee5…ffeed2`) validates three repair shapes against the bytes they name
  (`correction: SKILL.md:<line> cells=<n> digest=<16hex>`, `supersedes: <id> digest=<16hex>`,
  `erratum: <file>:<line> digest=<16hex>`) and audits every criterion in `corpus/QUALITY.md`, not
  the newest block. `controls/selfcheck2-before.txt` → `SELFCHECK2=FAIL unresolved=3/3` exit 1;
  `controls/selfcheck2-after.txt` → `SELFCHECK2=PASS unresolved=0/3` exit 0.
- **The false-green controls.** `corpus/evidence/round79/selfcheck-control.py`
  (`00cf811a…f4499d`) rebuilds round 78's two false greens on scratch mirrors: a hollow repair set
  and a newer-block shadow. `controls/selfcheck-control-before.txt` →
  `CONTROL=PASS cases=4 v1_false_greens=2/2 v2_refusals=2/2`, exit 0.
- **The digest-bearing repairs (append-only).** `SKILL.md` gains
  `correction: SKILL.md:168 cells=7 digest=e6e751ec67878243 …` beside the round-78 correction;
  `corpus/QUALITY.md` gains criterion **149** carrying `supersedes: 116 digest=ae134338138ad3e0`
  and the all-block audit rule; `corpus/lessons/round-77.md` gains
  `erratum: round-77.md:73 digest=7f2d54a7eb33df54 …`. Every earlier entry's filed bytes are
  untouched (`git diff --numstat` over the three files is additions only: 4/0, 4/0, 2/0).
- **Registry rows.** S196 and S197 admitted (own-work B, mined, used-by
  `corpus/lessons/round-79.md`), S198 rejected (a defect receipt offered as a source about
  verification method, kept with its flip condition).
- **Wave.** One v1 wave of 12 seats under `ufo-wave-policy.json` (band 8–16) through the run-15
  inline spawn handoff: `R79ExecA/B/C`, `R79ScoutA`, `R79ScribeA`, `R79ConnectorA`, `R79ReviewA/B`,
  `R79CriticA/B`, `R79MutA`, `R79SentinelA` — 5 attack seats (2 reviewer, 2 critic, 1
  mutation-tester) = 42 %, one connector seat. The L1 holds the canonical planner seat; no residual
  call. Wave evidence: `.ufo/waves/round-79/w1-spec.json`, `w1-dispatch.json`, `w1/`.

### What the wave falsified

- **C1.** `R79CriticA`'s `a10-payload-decode.py` regexes the wrapper's base85 literal, decodes it,
  unmarshals the code object and identifies each subject by its surviving string constants — no
  canonicalisation, no execution. It reaches the battery's own exact target line
  (`BATTERY=PASS forgers_rejected=11/11 positive=2/2 oracle=REJECTED`, exit 0;
  `.ufo/waves/round-79/w1/R79CriticA/a10-receipt.txt`), re-run by the L1 with the same result. The
  kill rule's clause is "if **any** forger is FORGED" while the predicate counts six, so C1 does
  not verify as written. Independently, `R79ExecC` shows the structure channel is a full forgery of
  *both* batteries (`receipt-v6-structure-matrix.txt`, `receipt-v5-structure-matrix.txt`).
- **C2.** A newer `## Round-<n> addition` block re-using criterion number `116.` overwrites the
  earlier body in `criteria()` and hides criterion 116's live dead pointer, printing
  `SELFCHECK2=PASS unresolved=0/3` exit 0
  (`.ufo/waves/round-79/w1/R79CriticA/selfcheck2-duplicate116-head.txt`; independently
  `R79ReviewB/05-dupid-v2.txt`). The kill rule names exactly that event. Two further inputs of the
  same class: a blank line before the malformed Gates row (`R79ReviewB/07-blankwindow-no-repair-v2.txt`)
  and a stranded `## Mistakes` row whose first cell is the literal word `class`
  (`R79ReviewB/08-stranded-probes-v2.txt`).
- **Claim-text defects found and reported, not repaired:** `claims.md`'s class provenance named the
  wrong routed defect and overstated the wider audit (`R79CriticA` F2), and the after receipt was
  measured on the worktree and labelled `REV=worktree` (`R79CriticA` F8). Both are mined in the
  round lesson; QUALITY 150–151 carry the successor rules.
- **Legs measured, not assumed.** `R79MutA`'s table: reverting the identity leg to round-78's
  salt flips `a8` to FORGED (M1, killed), dropping the `RECEIPT_LINES` trailer flips `a5d` to
  FORGED (M5, killed), `--no-permute` makes the positive control MISS (M3, killed), and the
  ORDER line plus the quiet leg are jointly load-bearing (M2b killed, M2/M2c survive). Two
  legs are decorative for this predicate and are reported as such: `--no-content` (M4) and
  identifier renaming (M6) — with renaming off, `a8` and `a9` still refuse, because the
  channel they would need is payload decoding, which is exactly `a10`.
- **Wave settlement.** All 12 seats settled (`w1-results.json`). Ten filed a retained report;
  `R79CriticB` and `R79SentinelA` settled with partial output only. The sentinel's single
  claim — a missing `cc` with a pre-seeded `perm` raises a traceback instead of the
  could-not-evaluate exit — was re-measured by the L1 and holds (`FileNotFoundError` from
  `cc --version`, QUALITY 148's O2 clause); the critic's last line names an unverified
  "annotation-future drift" with no receipt, recorded as unverified and not used.
- **Agreements:** `R79ReviewA` agrees with every C1 predicate line, the independent 40-byte
  measurement (`0/13` v6, `13/13` v5), byte-exact v5 recovery (`13/13`), and behaviour preservation
  (`divergences=0/13`); `R79ReviewB` agrees on the base, hollow, window, partial-digest and honest
  directions of C2; `R79ConnectorA` finds no sibling lane holding a stronger form of either move
  (all weaker or equal, at pinned sibling revisions) and absorbs none.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| prefreeze instruments, controls and the digest-bearing repairs (`corpus/evidence/round79/`, `SKILL.md`, `corpus/QUALITY.md`, `corpus/lessons/round-77.md`) | `LOG.md` §Round 79 | `e2bf2bbb5ca66f06b6571cbcaa15554d1a74a67c` |
| claims freeze, S196–S198, wave spec and dispatch | `LOG.md` §Round 79 (Frontier bullet) | `b58a02dbc8876dd1ad7647d88ca2c9cb2ae51ff9` |
| round lesson, LOG entry, SCORECARD verdict, QUALITY 150–151, wave outputs | `LOG.md` §Round 79 (full entry) | `LANDING` |

## Before → after measurements

| claim | counting command | before | after | measured commit |
|---|---|---|---|---|
| C1 operability | `python3 -B corpus/evidence/round79/forge-battery.py --battery corpus/evidence/round78/matrix-battery-v5.py --work DIR` (before) / `--battery corpus/evidence/round79/matrix-battery-v6.py --work DIR` (after) | `FORGE_BATTERY=FAIL forgers_handled=5/6 positive=1/1`, exit 1 (`controls/forge-battery-before-v5.txt`) | `FORGE_BATTERY=PASS forgers_handled=6/6 positive=1/1`, exit 0 (`controls/forge-battery-after-v6.txt`) | base `ee70e6df` → controls `e2bf2bbb` |
| C1 supporting | `python3 -B corpus/evidence/round79/derivative-check.py --battery BATTERY` | `DERIVATIVE_COPIES=13/13 MAX_WINDOW=4096`, exit 1 | `DERIVATIVE_COPIES=0/13 MAX_WINDOW=23`, exit 0 | base → controls |
| C2 calibration | `python3 -B corpus/evidence/round79/selfcheck-v2.py --lane . [--rev REV]` | `SELFCHECK2=FAIL unresolved=3/3`, exit 1 at `--rev ee70e6df` (`controls/selfcheck2-before.txt`) | `SELFCHECK2=PASS unresolved=0/3`, exit 0 (`controls/selfcheck2-after.txt`, re-measured at the landing in `controls/selfcheck2-after-landing.txt`) | base → controls → landing |
| C2 controls | `python3 -B corpus/evidence/round79/selfcheck-control.py --lane . --work DIR --base REV` | `SELFCHECK=PASS unresolved=0/3` on both round-78 false greens | `CONTROL=PASS cases=4 v1_false_greens=2/2 v2_refusals=2/2` | base → controls |

The battery's own predicate, re-derived by the L1 and by three seats:
`BATTERY=PASS forgers_rejected=11/11 positive=2/2 oracle=REJECTED`, exit 0.

**Verdicts:** C1 — predicate holds, **kill rule fired** (`a10` forger). C2 — predicate holds,
**kill rule fired** (duplicate criterion number in a newer block). No axis is harmed; the
instruments are measurably better on the channels they close and the surviving channels are
measured rather than asserted. The admission is false and the operator rules.

## Sources & frontier

Census, both ends, command and exit code recorded:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa
```

- **before** (base `ee70e6df`, scratch clone with the fleet `shokunin.conf`): exit 0 —
  `rows 195 · tier.A 123 · tier.B 54 · tier.C 18 · mined 156 · queued 19 · rejected 20`
  (`.ufo/waves/round-79/census/census-start.txt`, `census-start-census.txt`).
- **after** (landing tree): exit 0 — `rows 198 · tier.A 123 · tier.B 56 · tier.C 19 · mined 158 ·
  queued 19 · rejected 21` (`.ufo/waves/round-79/census/census-end.txt`).

Rows added: **S196** (own-work B, QUALITY 147 at the base, mined — grounds C1), **S197** (own-work
B, QUALITY 146 at the base, mined — grounds C2), **S198** (own-work C, rejected — a defect receipt
offered as a source about verification method, with its flip condition). Rows touched old→new:
none. Frontier rows advanced: none — the round works the instrument frontier, not the
domain-document frontier, and says so rather than claiming a coverage move. Assimilation: **none**
— the `merge/chousa/` package stays closed (111 of 114 staged ids collide with the live registry;
the id drift is not renumbered in scratch), and the claim cap was spent on C1/C2.

## Trend verdicts

- **expansion — unchanged.** No admitted `knowledge/` entry, no capability row, no
  `corpus/README.md` frontier row, no `PROVINCE.md` ground. The three registry rows are curation
  (two admits, one rejection); a rejection is taste, not expansion.
- **quality — improved.** Both round-78 false greens are closed with before receipts and controls
  (`5/6` → `6/6` with the positive accepted; `13/13` → `0/13`; `FAIL 3/3` → `PASS 0/3` while round
  78's counter still prints PASS on the hollow mirror), and the two surviving channels — payload
  decoding and the duplicate-id audit window — are measured with receipts instead of asserted.
  Nothing frozen was rewritten; every lane edit is append-only.
- **discernment — improved.** Both frozen claims were falsified inside the round by its own attack
  seats, each with an independent reproduction (`R79CriticA` `a10` and duplicate-116; `R79ReviewB`
  cases 05/07/08; `R79ExecC` structure matrix), and the disagreements became QUALITY 150–151 and
  five mined mistakes. A non-author spot-check of the two admits and the reject remains requested,
  not self-granted.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `SKILL.md` `## Gates` registry (rows for the v6 battery, the six-forger battery and the v2
  counter, each with exit map and self-test cell); `corpus/QUALITY.md` criteria 1–151. Lane
  assertion; no non-author verifier.
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` §Round 79; the
  instruments run end to end on committed bytes (`corpus/evidence/round79/controls/`). Lane
  assertion.
- `[~]` Instructions executable by an agent without oral context —
  `python3 -B corpus/evidence/round79/matrix-battery-v6.py --matrix MATRIX --work DIR`,
  `python3 -B corpus/evidence/round79/forge-battery.py --battery BATTERY --work DIR`,
  `python3 -B corpus/evidence/round79/selfcheck-v2.py --lane .`, each with its exit map in
  `SKILL.md`. Lane assertion.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched; `R79ConnectorA`
  reports the sibling rows it compared (tsukuroi 683ae456, kasegi c1051749, souji d05a0001, kama
  3ff23da3, mado a722c604) and absorbs none. Lane assertion.

## Stale-lane

Respawn-per-round driver: no other chousa mission is open. This round is the only one dispatched;
the lane's round-78 closure is admitted and pushed.

## Inherited state and sweep

- Inherited uncommitted lane work: none — `git -C chousa-shokunin status --porcelain` held only
  this round's own files at the start.
- Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): only `.scratch/*`
  (orchestrator-owned run state, never a misroot) and another lane's report modification; no seat
  of this round wrote a file into the fleet root.
- Files not authored by this lane: `.ufo/reports/round-84/kama.md` shows as modified in the fleet
  repo — another lane's report, never touched here.
- Tool installs: none this round (no seat reported one; `python3` 3.14.8 and `cc` 16.2.1 sufficed).
