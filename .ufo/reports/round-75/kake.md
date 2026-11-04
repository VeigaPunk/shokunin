# kake — round 75 report (hyaku run 15, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/kake-shokunin` (branch `master`), Linux host. Base
`c9c5e484c533aa65f4374b841a3edcf572ed19a9` (round-74 verifier spot-check tip). Freeze
`88f2e05f36f008faf01fcf77afedd33ae3c53e40`; Amendment 1 (terms only) `9a9c4a6f`, Amendment 2 (terms
only) `d599c8be`, Amendment 3 (terms only) `7348d37e`; wave evidence `ab939c46`. Round shape: one v1
wave `w1`, 14 seats, all settled with non-empty output, 0 dead (`.ufo/waves/round-75/w1-results.json`),
no residual call — round total 14. Lane tip at filing (pushed, verified with
`git -C kake-shokunin ls-remote origin refs/heads/master`): `3ae076ab3e01914abc636da680de1bbafc3314df`.

## Work performed

The round declared two claims, one per owned axis, frozen before any seat ran:

- **C1 — calibration** (owned score 2, the lane's lowest non-retired axis): every live gate-registry
  row's claim re-derives by execution over a frozen 16-instrument population that grows to 18 with
  the round's own instruments, `mismatches` 2 → 0. Contract §C1 with amendments 1–2.
- **C2 — operability** (owned score 10, HOLD; capability acquisition): every live registry
  instrument is bound to a committed digest receipt that re-derives from committed bytes,
  `bound` 0 → 18. Contract §C2 with amendments 1 and 3.

Work items, each with its evidence:

- **Freeze with controls** — `.ufo/waves/round-75/contract.md` plus base receipts
  (`controls/base-c1-row-truth.txt`, `controls/base-c2-receipts.txt`) and the two writes-are-not-enough
  controls (`controls/ctl-cheapcontent.txt`, `controls/ctl-deletion.txt`) committed at `88f2e05f`.
  Pre-freeze diagnosis is disclosed in the contract (harness traps found and excluded: `git archive`
  materialisation, scratch inside the clone).
- **One v1 wave, 14 seats** (`w1-spec.json`, `w1-dispatch.json`, `w1/swarm-registry.json`): scout 2,
  executor 4, scribe 2, reviewer 2, critic 1, mutation-tester 1, connector 1, sentinel 1. Attack
  seats 4/14 = 28.6 %. The L1 held the planner seat (the validator rejects a planner role).
- **C1 counter** — `.ufo/waves/round-75/c75_row_truth.py` (final sha256 `63e321b2…`, selftest 29/29):
  executes each effective row's own self-test at the measured revision, word-bounded `differential`,
  command-to-instrument binding, claim-segment tallies, whole-population E4, append-only + population
  floor. `w1/ExecC1Counter.md`, `w1/ReviewerC1.md` (10 held-out attacks), `w1/MutationTesterC2.md`,
  `w1/CriticPredicates.md`.
- **C2 tool and receipt** — `scripts/instrument_receipts.py` (`162dd68…`, selftest 17/17) and
  `corpus/knowledge/instrument-receipts.json` (18 entries, `15768f81…`, 3,793 B). `w1/ExecC2Tool.md`,
  `w1/ExecC2Receipts.md`, `w1/ReviewerC2.md` (forgery suite), `w1/SentinelScope.md` (scope audit).
- **Registry section** — `SKILL.md` `### Round 75 gate registry additions` (appended at EOF, below the
  sidecar's highest pinned line 935): the `c69_tmp_honour.py` demotion row (closes round-74 R2), the
  `c74_registry_gap.py` eight-fixture row (closes R1), and rows for both new instruments.
  `w1/ScribeRows.md`.
- **Corpus** — `corpus/knowledge/instrument-receipts.md` (provenance trio, S443), one appended
  `corpus/QUALITY.md` criterion ("a registry row's claim is executable as written"), two
  `corpus/README.md` coverage rows, a `PROVINCE.md` round-75 instruments section, `LOG.md` round-75
  entry, `SCORECARD.md` claims/capability/move-log rows, `corpus/lessons/round-75.md`.
  `w1/ScribeKnowledge.md`, `w1/ConnectorOverlap.md`, `w1/ScoutSources.md`, `w1/ScoutRegistry.md`.
- **Harm battery at the tip** — `controls/after-harm-battery.txt` (`306fff49`, after the append-only
  repair below): sweep selftest 36/36
  exit 0; sweep `--offline` exit 1 with the single `~/projects` drift (unchanged class); c66
  `members=28 ... agreement=25 met=True` exit 0; c70 exit 0; c72 `findings=[] met=True`; c73_tmp_v3
  `selftest=41/41 findings=[] met=True`; c73_wave_pointers exit 0; c74_registry_gap
  `unregistered=0 own_row=true met=true`; c74_sidecar_reobserve `contradictions=0 met=true`; c75
  `mismatches=0 met=true`; c2 `bound=18 mismatches=0 met=true`. One red was found and repaired
  in-round: `c73_wave_pointers` reported `append_only false file=LOG.md`/`file=SCORECARD.md` at
  `6c10b433` because a bulk text substitution had rewritten three historical bytes; the three lines
  were restored byte-for-byte from the base, committed as `ca1a2982`, and the gate re-ran
  `append_only=true met=true`, exit 0. The incident is mined in `corpus/lessons/round-75.md`
  `## Mistakes`.
- **Frontier** — S443 admitted from a live fetch (see Sources & frontier); `Assimilation: none` on the
  connector's mechanical finding; the `considerthese/2026-10-26.md` proposal-5 prior adoption named.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Freeze: contract, v0 counter, base/control receipts | round 75, *Frozen contract* | `88f2e05f` |
| Wave w1 spec, dispatch, ready handoff | *Wave `w1`* | `ab939c46` |
| Amendment 1 (floor, not equality) | *Frozen contract* bullet | `9a9c4a6f` |
| Amendment 2 (own-instrument self-test, E4 scope) + early seat reports | *Frozen contract* bullet | `d599c8be` |
| Amendment 3 (committed receipt, declared-revision validation) | *Frozen contract* bullet | `7348d37e` |
| `scripts/instrument_receipts.py`, `SKILL.md` section, `corpus/knowledge/instrument-receipts.md`, `corpus/QUALITY.md` criterion, README rows, `PROVINCE.md` | *C1/C2 landed* bullets | `f1fc5d0a` |
| First C2 receipt (superseded by the re-cut after the final counter) | *C2 landed* | `4e3fc159` |
| Final C1 counter (29/29) and the row's tally | *C1 landed* | `abfbfaac` |
| C2 receipt re-cut for the final counter bytes | *C2 landed* | `f87d14a9` |
| Measured receipts, LOG/SCORECARD entries, lesson, wave evidence | all bullets | `6c10b433` |
| Append-only repair of the three bulk-rewritten historical lines | *Mistakes* row (bulk substitution) | `ca1a2982` |
| The bulk-substitution mistake row | *Mistakes* | `306fff49` |
| Wave `w1` results (14/14 settled), final seat reports, controls | *Wave `w1`* | `3ae076ab` |

## Before → after measurements

| Claim | Counting command | Before (base `c9c5e484`) | After (tip `6c10b433`) |
|---|---|---|---|
| C1 | `python3 -B .ufo/waves/round-75/c75_row_truth.py --root . --revision <rev> --base c9c5e484c533aa65f4374b841a3edcf572ed19a9 --work <scratch>` | `rows=28 live=16 files=16 mismatches=2 classes=E1 E3 append_only=true met=false missing_frozen=0`, exit 1 — `controls/base-c1-row-truth-landed.txt` | `rows=32 live=20 files=18 mismatches=0 append_only=true met=true missing_frozen=0`, exit 0 — `controls/after-c1-row-truth.txt` (`f87d14a9`) |
| C2 | `python3 -B scripts/instrument_receipts.py --root . --revision <carrier commit> --check` | `population=16 bound=0 mismatches=16 met=false`, exit 1 — `controls/base-c2-receipts.txt` | `population=18 bound=18 mismatches=0 met=true missing_frozen=0`, `receipt: source=committed declared_valid=true`, exit 0 — `controls/after-c2-receipts.txt` (carrier `f87d14a9`) |

Controls, measured with the landed counter: cheap content (junk rows repeating the two wrong claims)
stays `mismatches=2`, exit 1 (`controls/ctl-cheapcontent-landed.txt`); deleting the failing row gives
`mismatches=3 classes=E3 append_only=false missing_frozen=1`, exit 1
(`controls/ctl-deletion-landed.txt` — the third finding is Amendment 1's floor; the frozen v0 control
receipt pinned two findings). Forgeries are red: fabricated digests `mismatches=16`, dropped path
`bound=15`, mode flip, worktree-only receipt, unresolved and unanchored declared revisions
(`w1/ExecC2Tool.md`, `w1/ExecC2Receipts.md`, `w1/ReviewerC2.md`).

Inherited state: the round's wave directory was created fresh; the only pre-existing leftovers were
untracked `.ufo/waves/round-75/w1/__pycache__` (removed) and two untracked `__pycache__` directories
under `.ufo/waves/round-66/` and `round-72/` that the sentinel seat flagged (removed). The fleet-root
sweep shows no kake misroot: only orchestrator-owned `.scratch/` files and one unattributed `after`
file left untouched since round 74 (R6).

## Sources & frontier

- `corpus/SOURCES.md` 180 → **181** rows; added by tier: **A +1** (S443, `spec`); zero rows touched
  old→new in status/recheck/used-by terms — no `status`, `recheck` or `used-by` cell changed on any
  pre-existing row.
- **S443** — in-toto Attestation Framework, Statement v1
  (`raw.githubusercontent.com/in-toto/attestation/main/spec/v1/statement.md`), opened 2026-11-03:
  HTTP 200, 2,492 bytes, sha256 `cbe684a1…a455ebea`, byte-identical across two independent fetches;
  located quote "Each element MUST have `digest` set." (6 words, raw line 37), status `mined`,
  `used-by corpus/knowledge/instrument-receipts.md`. Prior fleet adjacency recorded, not claimed as
  new ground: tameshi's S281 is the same bytes, and four sibling lanes hold digest-binding variants
  (tabi, chousa, souji, tameshi — `w1/ConnectorOverlap.md` §1).
- **Row counting command**:
  `sh scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`; counting of
  rows: `grep -c '^| S[0-9]' corpus/SOURCES.md` → 181.
- **Census**: round start exit 0 (`kake ok`, 180 rows, 16 W04 duplicate-URL warnings unchanged);
  round end exit 0 (`controls/census-end.txt`, 181 rows, same warnings).
- **Frontier rows advanced**: `PROVINCE.md` §Frontier ground unchanged — the new entry is Core
  instrumentation (a gate over the lane's own registry), not new domain frontier; the frontier map
  in `corpus/README.md` therefore gains coverage rows, not ground rows.
- **Assimilation (§10): none.** The connector re-read `merge/kake/MERGE-REPORT.md` and the four
  candidate entries; every locator they cite is unreachable in this lane and five cited ids are below
  the registry tip, so nothing was adoptable as written and nothing was written into the source repo
  (`w1/ConnectorOverlap.md` §3, with each entry's flip condition).
- **considerthese** (`considerthese/2026-10-26.md`): proposal 5 was already adopted in round 66
  (`corpus/knowledge/gate-status-ledger.md:1-10`); this round does not re-mine it as new ground — the
  appended `QUALITY.md` criterion names that prior adoption and makes the live/historical distinction
  an admission-time rule. Proposal 4 (gate-agreement ledger) is the one still open and is routed.
- **DRIFT class met**: one — the lane's own registry stated two capabilities its instruments did not
  have; a committed instrument now measures that class (`c75_row_truth.py`).

## Trend verdicts

- **expansion — improved.** One admitted knowledge entry on ground the lane did not hold (the
  registry-derived instrument inventory, with its own precedence rule) and one new tier-A source row;
  qualified by the connector's finding that the digest primitive itself is held in four sibling lanes,
  so the entry is scoped to the inventory, not to digest binding.
- **quality — improved.** Two registry rows that stated false capabilities now re-derive
  (`mismatches` 2 → 0 over 18 files); 18 instruments are digest-bound with a committed receipt that
  re-derives from committed bytes; the standing gates are unchanged or green in the tip battery, and
  the sweep's single named drift was not silenced. Documentation defects found by the closure of
  round 74 (R1, R2, R5) are closed; R3/R4/R6 are handled by scribe items, with R4's corrected line
  range recorded in the lesson.
- **discernment — improved.** The Gate records three admits and three rejects, each with a flip
  condition; two reviewer seats' findings were adopted as amendments (10 held-out C1 attacks, the
  C2 provenance defects) instead of argued away; the critic's "erasure is as cheap as the honest fix"
  finding is reported as a stated limit, not hidden. Outside non-author spot-check is owed to the
  hyaku closure.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the
  round-75 registry section and the new QUALITY criterion are landed; verifier:
  `SKILL.md` `### Round 75 gate registry additions`, `corpus/QUALITY.md` round-75 section.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the C1/C2 measurements are
  logged end to end at `LOG.md` round 75 with receipts under `.ufo/waves/round-75/controls/`.
- [~] Instructions executable by an agent without oral context — both instruments take documented
  argv and carry selftests (`29/29`, `17/17`); `SKILL.md` rows name the exact entry commands.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` round-75 section scopes the
  new instruments to the lane's own evidence and records the sibling adjacencies; the connector
  seat found no duplicate ownership.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none (pacman untouched; no `uv`/`npx` used).
L0: no new question filed; the round-69 lowercase `~/projects` question stays open and its single
drift is unchanged.
