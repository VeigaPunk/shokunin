# kagi-shokunin — round 12 report

**Axis moved:** depth **7 → 8** (`SCORECARD.md` §Round 12). **Repo commit:**
`round-12` (follows `4391b3b`, which is where three foreign commits landed
mid-round — §Adjacency). **Wave:** 12 L2 lanes, one batched call (planner,
connector, 2 executors, 2 scouts, reviewer, critic, sentinel, labrat,
mutation-tester, distiller).

**Landed revision hashes** (the final ones; recompute with
`bash corpus/claim-ledger.sh verify`):

| Artifact | sha256 (prefix) |
|---|---|
| `corpus/op-ref-probe.sh` | see `corpus/stamps.tsv` (v4: one chokepoint, per-path guard, 29 selftest cases) |
| `corpus/knowledge/op-ref-consumption.md` | see `corpus/stamps.tsv` (13 bounds, §2b hard-failure class) |
| `corpus/claim-ledger.sh` | see `corpus/stamps.tsv` (per-path `stamp` guard, 43 selftest cases) |
| `corpus/claim-ledger.tsv` | 14 rows (`R11-01..11`, `R12-01..03`) |
| `corpus/stamps.tsv` | 32 rows |

Hashes are not transcribed here by design: this repo stamps them, and a number in
prose is a claim that goes stale the moment the file moves (round-11 rule). The
stamp file is the authority; `verify` recomputes all four columns.

## 1. Why depth, and what the ceiling claim cost

The prompt's rule is "pick the lowest-scoring axis". Depth was 7 — the lowest —
and this file had carried the same explanation for three rounds: *"vault-side
structure stays unmapped — a deliberate scope refusal"*. That refusal is real,
and it was not what was binding. What held depth at 7 was an unmeasured,
**vault-free** surface: the other half of `op.env` consumption. `refs` had been
mapped since round 2; the parser that actually loads the file (`op run
--env-file`, which `cmd_run` L248 execs) had never been measured, and neither had
the true scope of `op run`'s masking. Both are reachable with zero vault contact.
Correcting that self-assessment is the calibration half of this round; landing
the measurement is the depth half.

## 2. What landed

- `corpus/op-ref-probe.sh` — the contract gate: `verify` / `--evaluate F` /
  `--fixture DIR` / `--selftest`. Fixtures are generated from the contract arrays
  (so a fixture cannot drift from the expectation), plain-valued by construction,
  and every `op` invocation goes through `op_exec`, which guards each
  `--env-file=` argument.
- `corpus/knowledge/op-ref-consumption.md` — the contract: two-parser
  divergence table, §2b hard-failure class, masking table with evidence grading,
  dotenv edge semantics, precedence/union, six error signatures, decision table,
  13 named bounds, reproduction, falsifiers.
- `SKILL.md` — 3 decision rows, 3 failure rows, 4 anti-patterns, 2 checklist
  items, a `## op.env consumption` section, a round-12 falsification bullet.
- `corpus/claim-ledger.tsv` — `R12-01` (live probe verdict), `R12-02` (selftest
  case count), `R12-03` (stamp row count, non-blank-line count).
- `corpus/drift-symbols.tsv` — one new pin: `the-janitor` L248
  `exec op run --env-file="$ENV_FILE" -- "$@"` (the masking premise; 19 → 20).
- `corpus/claim-ledger.sh` — the `stamp` guard became per-path (§5).
- Sweeps: 16 stale live-doc rows corrected in place (scout lane), plus every
  number this round itself moved.

## 3. Measurements

Before → after (all exits are the shipped exit codes):

| Gate | Before (round-11 close) | After |
|---|---|---|
| `op-ref-probe.sh` | did not exist | `OP_REF_PROBE: CLEAN (checks=44 oprun=12 refs=7 divergent=5 edge=10 sig=6)`, exit 0 |
| `op-ref-probe.sh --selftest` | did not exist | `OP_REF_SELFTEST: PASS (29 cases)`, exit 0 |
| `claim-ledger.sh verify` | `CLEAN (claims=11 stamped=28)` | `CLEAN (claims=14 stamped=32)`, exit 0 |
| `claim-ledger.sh --selftest` | `PASS (39 cases)` | `PASS (43 cases)`, exit 0 |
| `drift-pins.sh` | `CLEAN (files=15 symbols=19)` | `CLEAN (files=15 symbols=20)`, exit 0 |
| `surface-census.sh` | `CLEAN (assets=20 runtime=15 scanned=4 ok=34 absent=2 skipped=0)` | unchanged, exit 0 |
| `transcript-scan.sh` | `HITS=2`, exit 1 by design | unchanged, exit 1 |

## 4. The finding (condensed)

`refs` and `run` are **different parsers over the same file**, and they disagree
in three increasing severities:

1. **Keys the resolver injects and the inventory cannot see** — `export K=v`,
   `K = v`, lowercase, digit-leading and indented keys: `op run` injects 12 keys
   on the probe fixture, `refs` lists 7 (`divergent=5`).
2. **Values the resolver rewrites and the inventory only redacts** — `#` starts a
   comment anywhere in an unquoted value (`K=ab#cd` → `ab`, silently), quotes are
   stripped, `$K`/`${K}`/`${K:-default}` expand (single quotes suppress
   expansion), CRLF/whitespace are trimmed, duplicate keys last-win, and `op run`
   trims values inherited from the parent process.
3. **Files the resolver refuses and the inventory clears** — a `-` in a key, a
   bare key, a lone `=`, or a UTF-8 BOM aborts the whole parse (`[ERROR] … parsing
   Dotenv file …`, exit 1, zero keys injected) while `refs` exits 0 with a healthy
   inventory. "The env file is fine" is not a question `refs` can answer.

And the masking contract is narrower than its help text reads: only
**reference-resolved** values are concealed on stdout/stderr. Plain values pass
through verbatim (four shapes + stderr + a full-`env` multiset, two independent
lanes), and `--no-masking` cannot change that. `cmd_run` passes no masking flag,
so this is the default path — "the handler masks its output" is false for every
plain-valued key. Since the observed `op.env` holds 8 refs and 2 raw identifier
values, nothing material is leaking *today*; what is fixed is the false belief,
plus the operational rule (never paste `run` output; never put a plain secret in
an env file expecting masking).

## 5. Defects found in flight (all reproduced before and after)

1. **The `stamp` guard was a length rule.** An equal-count **path swap**, a
   missing-final-newline off-by-one, and a **blank-line** substitution (which
   passed a `grep -c` count while `verify` lost a row) all slipped past it
   (mutation lane). Now: any pinned path not named again is refused
   (`refusing to shrink … 'X' is pinned and would be dropped`, exit 2), a blank
   row is a setup error, `R12-03` counts non-blank lines, and four selftest cases
   cover the guard.
2. **Two CRIT guard bypasses in my own probe** (sentinel F1/F2, plus F3): a
   `--fixture` tree could hand the binary a ref-bearing `absent.env`, a *file*
   named `adir`, a symlink or a FIFO. Now the guard is per-path inside a single
   `op_exec` chokepoint; symlinks/non-regular files are refused outright;
   premises are asserted (`absent.env` absent, `adir` a real directory). I
   re-ran the sentinel's four poison trees by hand: all `POLICY` exit 2, stub log
   **empty** (the binary never ran).
3. **A false header claim** (reviewer F1, WRONG): "every invocation goes through
   `op_run()`" while four sites called the binary directly. Fixed by the
   chokepoint — `grep -n '"$OP_BIN"' corpus/op-ref-probe.sh` now returns the
   chokepoint and the `command -v` check only.
4. **`trap` + `local` under `set -u`** re-ran the probe's cleanup trap with an
   out-of-scope variable (`d: unbound variable` on exit). Fixed with global
   scratch + one `cleanup` trap.
5. **Two stale numbers in my own first draft**: the `refs`-omission set started
   at 3 keys (now 5) and the masking rows were described as fully mechanised
   (they are two mechanised + three one-off). Both are now graded in the entry.

## 6. L2 wave — what 12 lanes changed

The wave's biggest finding is procedural and mine: **the freeze was stale on
arrival.** I kept editing (probe v1 → v4, entry twice) while the lanes ran, and
four of them recorded the movement independently. The lanes still produced
reproducible findings because each one re-ran the gates itself; the cost is that
canned comparisons in the early window describe a revision that no longer exists.
Recorded in `corpus/lessons/round-12.md` §L2 wave with the per-finding table.

Highest-value items: the sentinel's two CRIT bypasses (must-fix, closed with
proof), the reviewer's WRONG header claim (closed), the mutation lane's three
`stamp`-guard holes (closed) and its quantified bound (5/12 tested mutants
caught on the older revision; 3/17 check classes lack a seeded negative — now
recorded in the entry's §Bounds.11-12), executor B's three new classes
(whole-file parse abort, union semantics, inherited-value trimming), labrat's
FIFO/directory/BOM/dev-stdin probes, executor A's independent confirmation of
the masking scope, the planner's correct objection that C3's resolver half is an
author one-off (now stated as such), the scout's 16 stale live rows (fixed), and
the connector's verdict that no sibling verifier duplicates this probe.

## 7. Verification

Run from the repo root on the shipped revision:

```
bash corpus/op-ref-probe.sh            # OP_REF_PROBE: CLEAN (checks=44 oprun=12 refs=7 divergent=5 edge=10 sig=6)  exit 0
bash corpus/op-ref-probe.sh --selftest # OP_REF_SELFTEST: PASS (29 cases)                                          exit 0
bash corpus/claim-ledger.sh verify     # CLAIM_LEDGER: CLEAN (claims=14 stamped=32)                                exit 0
bash corpus/claim-ledger.sh citations  # CITATION_GATE: CLEAN (cites=… docs=… unresolved=0 ephemeral=0 labeled=16) exit 0
bash corpus/claim-ledger.sh --selftest # SELFTEST: PASS (43 cases)                                                 exit 0
bash corpus/drift-pins.sh              # DRIFT_PINS: CLEAN (files=15 symbols=20)                                   exit 0
bash corpus/surface-census.sh          # SURFACE_CENSUS: CLEAN (assets=20 runtime=15 scanned=4 ok=34 absent=2 skipped=0) exit 0
bash corpus/transcript-scan.sh         # TRANSCRIPT_SCAN: HITS=2 (cells=888 patterns=32+5 warns=2)                 exit 1 by design
```

Falsification performed this round (not just asserted): a poisoned fixture tree
(`KAGI12_POISON=op://…` appended) ⇒ `POLICY` exit 2 **with an empty logger-stub
log**; the sentinel's four bypass trees ⇒ `POLICY` exit 2, empty stub log; a
falsified observation file ⇒ `FAIL` + exit 1 (nine seeded mutation classes);
a mutated `stamp` argv ⇒ refusal exit 2; appended line to a stamped artifact ⇒
`STALE` + exit 1; `KAGI12-BAD=v` in an op-side fixture ⇒ the hard-failure
signature fires and the `malformedrefs` blindness check still sees the valid key.

Vault contact: **none.** No `op read|inject|whoami|signin|account|service-account`
execution, no ref-bearing file passed to `op run`, no handler start, no secret
value or ref path recorded anywhere. The one-off probes that did reach the vault
API (a nonexistent-vault ref, exit 1 in ~2 s, bounded) are labelled in the entry
as one-offs.

## 8. Bounds and honest ceilings (summary; the entry carries 13)

- Masking of *ref-resolved* values, the mask token's shape, `--no-masking`
  against a ref, masking beyond the two streams — **unmeasurable here** (each
  needs a resolved reference).
- `op inject` / `op read` execution semantics, `op read` query parameters, global
  `--cache`, `op plugin`, `--encoding` — help-text-only (14 such items
  enumerated by the scout lane).
- Loadability of the **real** `op.env` is not testable without the vault; the
  hard-failure class is proven on plain fixtures.
- The gate cannot prove its own honesty: three check classes lack a seeded
  negative, the masking pair is a self-comparison, and `--evaluate` is a
  comparator that accepts a forged file. The compensating control is the revision
  stamp plus diff review.
- Scores in `SCORECARD.md` remain author-assigned; the pointers under them are
  machine-checked, the numbers are not.

## 9. Adjacency (reported, not absorbed)

- **Foreign commits.** Three commits landed in this repo during the round
  (`e0a04d8 corpus: round-8 aggregator box-3 non-author cold run`, `7c3377c`,
  `4391b3b` — the aggregator lane's box-3 audit lesson). Its citations to
  `.ufo/reports/round-8/aggregator.md` resolve nowhere in the main repo's history
  (`git log --all -- <path>` is empty; the round-8 report directory holds no
  `aggregator.md`). I labelled the three tokens where they are cited (the repo's
  own rule) and stamped the file because this report cites it — but the pointer
  is the aggregator's to fix, and **the integrator should rule** whether a lane
  may cite a main-repo report that was never committed.
- **Sibling verifiers.** No sibling duplicates the `op.env` behaviour probe
  (connector lane, with file:line evidence). Nearest overlap is kagi's own
  `surface-census.sh --verbs --deep`. The question of a shared verifier contract
  (kumitate `scripts/cite-check.mjs`, kotoba `verifiers/*.py`, kengaku
  `grader.py`, kasegi `ops/claim-check.mjs`) stays with the integrator.
- **`cmd_refs` redaction fix** (L0 question from round 10) is still open and
  unre-asked; this round's findings strengthen it: the fix should treat
  "the line is not `^[A-Z][A-Z0-9_]*=`" as its own class rather than silence.

## 10. Next move

All six cells sit at 8, so the next move is chosen by reachability, not by
lowest score. Named in `SCORECARD.md` §Planned: make every score **cell** cite
the claim ids it rests on, and make `claim-ledger.sh verify` fail when a cited id
is missing from the ledger (the round-11 plan, still only partially landed —
this round's depth row cites `R12-*`). Operability's ceiling (nothing schedules
the four gates) is reachable but needs an operator-level scheduling decision;
depth's remaining increments are the ones §Bounds refuses.