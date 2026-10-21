# kama — round 19 (attempt 1)

## Work performed

Declared claims:

- **C1 — calibration, 7 → 7 (delta 0; lowest assigned axis; sourced):** four
  material citations become machine-checkable. `tools/citation-provenance.py` +
  `registry/required-citations.json` require a `cite(<rev>, <path>, sha256=…)`
  token in the registry-bound document, verify the blob at that revision and
  require the revision to be an ancestor of origin/master. The declared 7 → 8
  was **refuted** by a fresh critic (the instrument binds digests, not the
  sentence beside a token; routed defects 1 and 4 are record corrections) and
  the score is held at 7; erratum in `corpus/lessons/round-19.md` and
  `SCORECARD.md`.
- **C2 — operability, 8 → 8 (delta 0):** a sixth receipt pin,
  `--expect-install-tree-sha256`, passed by the official runner from the
  producer's own `install_tree()` digest, with `tests/llamacpp-live/install-tree-grid.py`
  measuring consistent swaps of three install-tree members.

Work items:

- **Routed round-18 defects corrected first.** Verdict counts now read 4
  confirm / 3 partial with a committed dispatch record
  (`.ufo/waves/round-18/residual/assignments.json`); S055/`Gate` pointers are
  revision-qualified (S055 qualification in `corpus/SOURCES.md`, lesson-18
  erratum); the SCORECARD C2 command erratum names `--json` only; the residual
  role split is recorded. Evidence: `corpus/lessons/round-18.md` §Erratum,
  `SCORECARD.md` erratum block, `registry/required-citations.json`.
- **C1 instrument:** `tools/citation-provenance.py` (registry rows may bind a
  required `doc`; unreadable docs and non-repo lanes exit 2; stale tokens are
  `mismatch`; 15 selftest cases) plus the three tokens in the lesson-18
  erratum. Evidence: `evidence/c1-counting.txt`.
- **C2 instrument:** the gate accepts `--expect-install-tree-sha256` and
  cross-checks `server_impl_sha256` against `install_tree` (`tests/llamacpp-live/check-receipt.py`);
  the runner imports the producer's `install_tree()` and passes the observed
  digest; the grid has a `--selftest` and fails closed on absent default
  members. Evidence: `evidence/c2-grid.txt`.
- **Frontier:** S057 (`man7.org ld.so(8)`, opened 2026-10-21) grounds the
  identity boundary with two located quotes (10 and 11 words); census 56 → 57,
  both exits 0; `validate` exit 0 with the three expected W04s.
- **Waves:** build wave 1 = 64 seats validated under policy v2
  (`.ufo/waves/round-19/build/{spec.json,dispatch.json,advice/swarm-registry.json}`,
  spawn 64, resume 0; roles: scout 18, reviewer 12, executor 10, critic 6,
  scribe 5, connector 4, mutation-tester 3, revenger 3, sentinel 2,
  simplifier 1; planner = L1). Falsify wave 2 validated at 66 seats but its
  dispatch was refused by the host job cap: 66/66 seats failed to start
  ("Background job limit reached (100)"), none spawned, recorded at
  `.ufo/waves/round-19/falsify/refused-attempt-1.json`; the payload was not
  split or shrunk and wave-1 seats were not respawned. Wave-1 findings were
  integrated (doc binding, stale-token branch, uppercase/short-rev cases,
  unreadable-doc fail-closed, grid absent-member fail-closed, grid selftest
  fixes) and the rest are named below.
- **Measurement:** the official harness started on the clean tree `7229fa9`.
  It met its expected exit for 34 of 35 commands (all ten selftests, C1 counter
  and self-mutants, three live runs and five-pin gates, the tree-grid pair and
  the tree-pin negative, five legacy pairs, the wrong-probe-pin control, the
  snapshot and round-16 clone measures). Its final `c2-survivors` stage was cut
  off after ~50 min under wave contention and the job was stopped; the aborted
  run's lane artifacts were restored from HEAD and **not committed**, so the
  last full harness record remains round 18's 32-command `runs/commands.json`.
  C2's 15-mutant ledger inputs were not edited this round. The two round-19
  counting commands were then re-run at the final tree and recorded under
  `.ufo/waves/round-19/evidence/`.

## Landed changes

- `7229fa95eb122310e9e5334ad799ee3006293ebd` — C1 checker/registry/tokens,
  C2 gate pin/grid/runner wiring, S057 row and lesson-19 Gate, SCORECARD
  round-19 declaration, the r18 erratum and residual manifest.
- `5b108c1a…`, `84cf2f76…`, `f1790e25…`, `028235e6…`, `05f0f6c7…`,
  `30ed3783…`, `24adc8ed372e85d4739ae290e5fde5a6a7ebc2e9` — fail-closed grid,
  empty-tree rejection, INVALID-only kill classification, the four-row C1
  registry (incl. the checkpoint gate pin), C1 scope erratum, evidence
  receipts and the wave advice. **Lane tip at report time: `24adc8ed…`**;
  measured work commit for both claim commands: `028235e6…` (receipts in
  `evidence/c1-counting.txt`, `evidence/c2-grid.txt`).
- LOG entries: `LOG.md` §round-19.

## Before → after measurements

| Claim | Before → after | Counting command | Evidence |
|---|---|---|---|
| C1 | `required=4 found=0 verified=0 missing=4` exit 1 → `required=4 found=4 verified=4 missing=0 mismatch=0 off_ref=0` exit 0; selftest 15 cases | `python3 tools/citation-provenance.py` (before: `--docs` on the round-start `corpus/lessons/round-18.md` blob) | `evidence/c1-counting.txt` |
| C2 | baseline VALID, consistent member swaps `rejected=0/3` exit 1 → `rejected=3/3` exit 0, tree pin on (51/51 with the full-member census); invalid baseline exits 2 without counting mutants; grid selftest green | `python3 tests/llamacpp-live/install-tree-grid.py --gate tests/llamacpp-live/check-receipt.py --receipt .ufo/waves/round-18/live-recovery/receipt-1.json --model-sha … --server-sha … --impl-sha … --probe-sha … --tool-sha … [--tree-sha 6c216313…]` | `evidence/c2-grid.txt` |

The measured commit for both claims is `7229fa95…` plus the post-commit grid
fail-closed change (committed in the evidence commit); the harness's own
records label their run with the branch tip at run start. No axis is harmed:
legacy receipts replay with their four own pins, the new pin is optional, and
the gate's 76-mutation selftest and the checker's 15 cases pass.

## Sources & frontier

Census command
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin kama`
→ **56 → 57 rows**, exit 0 both times (`sources/census-before.txt`,
`sources/census-after.txt`). Tiers A 53 → 54, C 3 → 3. Status mined 45 → 46,
queued 5 → 5, rejected 6 → 6. `validate` exit 0 with three expected W04
duplicates (S031, S043, S056). Rows added: S057 (tier A, docs). Rows touched
old→new: none (S055's revision qualification is an appended clarification, no
cell rewritten). Frontier advanced: S057 grounds the install-tree identity
boundary in loader resolution; the lane's ownership entry from round 18 is
unchanged.

## Trend verdicts

- **expansion — improved (narrow).** One new curated source row and its Gate
  were opened and verified this round; census 56 → 57 with exit 0.
- **quality — improved (bounded).** The routed r18 pointer defects are now
  machine-checked, both instruments grew fail-capable cases (15 checker cases,
  grid selftest, 77 gate mutations), and wave-1 falsifiers' surviving mutants
  were closed or named. Not claimed: full gate coverage or universal detector
  adequacy.
- **discernment — unchanged.** The round-18 non-author spot-check is on record
  (`corpus/lessons/round-18-verifier-spotcheck.md`, head `8bf99cae`), but round
  19's outside admit/reject sample is still owed; the wave-1 seats are
  lane-dispatched advice, not that judgment.

## SHONEN

- [~] SKILL decision tables / error patterns / checklist — `SKILL.md` §§Decision
  table, Error signatures, Checklist; no named non-author verifier this round.
- [~] End-to-end domain task executed and logged — `LOG.md` §round-19; the
  five-pin live receipts and the sixth-pin grid run.
- [~] Instructions executable without oral context — `SKILL.md` §Checklist,
  `corpus/knowledge/*`; independent execution review still open.
- [~] No cross-domain bleed — `PROVINCE.md` §Write boundary remains accurate;
  host/package/routing decisions stay operator-owned.

## Extras

- **Wave seats:** build 64 spawned; 59 advice reports present at report time
  (the rest were still running or left none; all advisory, under
  `.ufo/waves/round-19/build/advice/`); falsify 66 validated and refused at the
  job cap (0 spawned); no seat respawned. Round total spawned 64 of ≤200.
- **Named residuals:** symlinked sonames escape the install-tree digest
  (`TreeCap`); the producer silently drops unreadable members and raises on a
  non-UTF-8 member name (`TreeDeterminism`); the grid counts any non-zero gate
  exit as rejected and `DEFAULT_MEMBERS` pins versioned names (`GridDefaults`);
  the harness hard-codes the canonical lane path (`SentinalSecrets`); stale
  round-18 leaves listed in `SCORECARD.md` §Planned remain open.
- **Stale-lane:** respawn-per-round driver; no other kama mission open.
- **Tool installs:** none. No host, package, service or compositor action.
- **Open L0:** the round-17 llama archive question remains unanswered;
  non-blocking, no new question filed.
