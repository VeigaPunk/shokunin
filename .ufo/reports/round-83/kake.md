# kake — round 83 (attempt 1)

Lane `kake-shokunin` (web properties & publishing) · hyaku run 15 · Linux/omp · 2026-11-04
Base `826b0061f233ce1dffb9bd6874abc1342a864247` · frozen contract
`64b7199281e5457df0e08652977f698c4f34f46e` · carrier `304c0f8787e292e4bc0f7b795987c9ba81f233ec` ·
final lane tip `64847b5fc946c61c972b2ab33fa3f798053725cd` (pushed; `git ls-remote origin
refs/heads/master` prints `64847b5fc946c61c972b2ab33fa3f798053725cd`).

Two claims, each on a distinct axis: **C1 — calibration** (score 2, the lowest non-retired axis):
the round-82 routed-defect queue closes. **C2 — freshness** (score 10, held): the drift gate
classifies every header that moved between the two dated captures and decides same-object vs
representation-changed, grounded in `S456` (RFC 9111). Scores are held; a claim moves evidence, not
a scalar. Everything below is author-side — admission belongs to the non-author closure.

## Work performed

**C1 (calibration 2): the six routed defects of the round-82 non-author closure close.** Population
is exactly `D1` … `D6` filed at `corpus/lessons/round-82-verifier-spotcheck.md` §6, frozen before
any seat ran; none added or dropped. Predicate `met <=> open == 0`, decided by
`python3 -B .ufo/waves/round-83/c83_defect_queue.py --root <tree> [--revision <rev>] [--fleet <dir>]`
from lane bytes and the fleet repo read-only — every item carries a state conjunct re-derived from a
non-lesson file plus a row conjunct only prose can carry (the item table is
`.ufo/waves/round-83/contract.md` §C1). The six corrections landed: the wave's own settled attack
share is re-derived from `w1-spec.json` + `w1-results.json` (5 of 14, `0.3571`, five attack seats
settled); the accounting record carries `bytes_basis: "utf-8"` and one `output_bytes` per seat
re-derived as `len(output.encode("utf-8"))`; the standing instrument gate has its own committed
`--check` receipt (`controls/after-c83-instrument-check.txt`, `bound=30`, `mismatches=0`, `met=true`);
the round-81 report erratum quotes, verbatim, five physical lines the amendment removed
(`[r83-erratum]`, verified as substrings of the pre-amendment blob and absent from the amended one);
the five round-82 mutation survivors are guarded by `killers/run_killers.py` (`distinguished=5/5`:
four killed on their named fixtures, `C2-m5` proven equivalent by the guarding `receipts_ok`
conjunct); and `corpus/QUALITY.md` gains a standing Gate-provenance criterion
(`corpus/lessons/round-82.md`, `Gate`, `round-83`). Evidence: `corpus/lessons/round-83.md`
§Corrections, `controls/after-c1.txt`, `controls/after-c1-tip.txt`, `controls/ctl-c83-junk-queue.txt`,
`controls/c83-selftest-c1.txt`, `killers/`.

**C2 (freshness 10): the drift gate's header changes are classified, and the verdict re-derives
(capability).** The new offline classifier `scripts/header_change_class.py` reads the two committed
capture trees (A `.ufo/waves/round-81/capture/`, B `.ufo/waves/round-82/capture/`), verifies every
receipt against its retained body (GET, integer status, byte count, sha256, not truncated),
canonicalises header lists, and sorts each changed header into the frozen class table
(`per-request` / `validator` / `representation` / `policy` / `unknown`); a surface is
`representation-changed` when status or body digest differs or any changed header is
validator/representation/unknown, else `same-object`. The committed record
`controls/after-c2-classes.txt` reads `summary surfaces=3 diffs=14 per_request=14 validator=0
representation=0 policy=0 unknown=0 verdict=same-object` — every moved field is request/edge
metadata, so both instants observed the same stored representation. The control pair
(`capture-control/`, a changed `ETag` plus one flipped body byte with matching digest) reads
`verdict=representation-changed validator=1`; an identical-pair tree reads `control_ok=0 met=false`.
The counter `.ufo/waves/round-83/c83_drift_class.py` re-derives the record, the determinism pair, the
control and the offline property from committed bytes. Evidence:
`controls/after-c2.txt`, `controls/after-c2-tip.txt`, `controls/ctl-c83-control-class.txt`,
`controls/c83-selftest-c2.txt`, `w1/ExecControlPair.md`, `w1/ReviewC2.md`.

**Frontier step.** `corpus/SOURCES.md` 193 → 194 rows: **S456** (RFC 9111 *HTTP Caching*
§3.1/§3.2/§4/§4.2/§4.2.3/§4.3.1/§4.3.4, tier A) admitted after a fresh GET of
`https://www.rfc-editor.org/rfc/rfc9111.txt` (HTTP 200, 84,477 bytes, sha256 `aeb52adb…cf3e`) and
line-located raw-substring spans; the retrieved copy is committed at
`.ufo/waves/round-83/w1/ScoutSources/rfc9111.txt`. New entry
`corpus/knowledge/header-change-classes.md` on ground the coverage map did not hold (header-change
classification over two dated captures), with the record quoted in it. Census exit 0 at round start
and end; `W04` 22 → 22. `corpus/QUALITY.md`, `PROVINCE.md`, `corpus/README.md`, `SCORECARD.md` and
`LOG.md` carry the round's appends; the capability row enters the scorecard.

**Wave `w1` (shape and settlement).** One v1 wave, 14 requested seats inside the run-15 band 8–16 —
scout 2, executor 4, scribe 3, reviewer 2, mutation-tester 2, critic 1; requested attack share
5/14 = 35.7 % over the run-15 roles {reviewer, critic, mutation-tester, labrat}. **All 14 seats
settled with non-empty output; no dead seat, no replacement.** Settled output is 81,754 UTF-8 bytes
(`w1-accounting.json`, `bytes_basis: "utf-8"`); the smallest seat output is 3,581 bytes. The L1 held
the planner seat, as the validator forbids `planner` as a swarm role; the bounded planning data-walk
rode `ScoutRecon` (pre-freeze recon and item-order walk). **Conformance deviation, named:** the L2
floor's minimum role split asks for one connector seat; this wave carried none. The two claims are a
self-contained defect queue and a classifier over already-committed capture bytes, so no
sibling-overlap question was opened, and the run-15 band caps connector seats at two without a floor
— the omission is reported, not back-filled by padding. Spec `w1-spec.json`, dispatch
`w1-dispatch.json`, ready `w1.ready`, results `w1-results.json`, accounting `w1-accounting.json`,
seat registry `w1/swarm-registry.json`.

**Inherited state and misc.** No earlier attempt of round 83 existed (`.ufo/watchdog.log` shows a
single `launch kake round=83` at 10:18:12 and no `lane-dead-no-report`), and `.ufo/waves/round-83/`
did not exist at round open, so nothing was inherited, reused or discarded. Misroot sweep
(`git -C /home/vgpnk/Projects/shokunin status --porcelain`): no fleet-root file written by this
round's seats. The untracked root file `after` (24 bytes, mtime 2026-11-03 20:05, content
`== SCORECARD diff base-`) predates this round and is not kake's; left untouched, as are `.scratch/`
(orchestrator-owned) and `.ufo/reports/round-82/{mado,tameshi}.md` (sibling lanes). The lane is clean
and level with its remote (`state … ahead=0 behind=0 tracked=0 untracked=0`).

**Stale-lane.** Respawn-per-round driver; no other mission of this lane is open. The mission launched
10:18:12 and this report lands ~10:52, i.e. past two driver ticks (450 s): **progressing** — four
lane-authored commits since launch (`64b71992`, `304c0f87`, `2586243e`, `64847b5f`), not silent.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Frozen contract, both counters, the header-change classifier, junk/control builders, base and control receipts, wave spec and dispatch | §Round 83 ¶Frozen contract | `64b7199281e5457df0e08652977f698c4f34f46e` |
| C1 items D1–D6 landed (accounting v2, instrument receipt, erratum quotes, killer suite, QUALITY criterion); C2 record + control pair; wave w1 evidence (spec, results, 14 seat reports, registry, killer suite); lesson; `S456` and `corpus/knowledge/header-change-classes.md` | §Round 83 ¶C1, ¶C2, ¶Frontier, ¶Mined mistakes | `304c0f8787e292e4bc0f7b795987c9ba81f233ec` |
| SCORECARD round-83 block and capability row, LOG round-83 entry, `PROVINCE.md` §Round 83, `corpus/README.md` coverage row, after receipts at `304c0f87`, carrier instrument receipt, census-after | §Round 83 (all bullets) | `2586243ed9ccbb770709012fc609d748c5f43e93` |
| Tip receipts for both claims at `2586243e` | §Round 83 ¶C1, ¶C2 | `64847b5fc946c61c972b2ab33fa3f798053725cd` |

## Before → after measurements

| Claim | Counting command | Before | After | Measured commit |
|---|---|---|---|---|
| C1 calibration: the round-82 routed-defect queue closes | `python3 -B .ufo/waves/round-83/c83_defect_queue.py --root . --revision <rev>` | `C1v1 revision=826b0061f233ce1dffb9bd6874abc1342a864247 items=6 open=6 closed=0 met=false`, exit 1 (`.ufo/waves/round-83/controls/base-c83-defect-queue.txt`) | `C1v1 revision=304c0f8787e292e4bc0f7b795987c9ba81f233ec items=6 open=0 closed=6 met=true`, exit 0 (`controls/after-c1.txt`); tip `2586243e` also `met=true` (`controls/after-c1-tip.txt`) | `304c0f87…` (carrier); `64847b5f…` (tip) |
| C2 freshness: header changes are classified and the verdict re-derives | `python3 -B .ufo/waves/round-83/c83_drift_class.py --root . --revision <rev>` | `C2v1 revision=826b0061… declared=3 surfaces_a=3 surfaces_b=3 receipts_ok=1 diffs=14 validator=0 representation=0 unknown=0 verdict=same-object record_equal=0 determinism=0 control_ok=0 tool_offline=0 selftest_ok=0 tool_absent=1 met=false`, exit 1 (`controls/base-c83-drift-class.txt`) | `C2v1 revision=304c0f87… declared=3 surfaces_a=3 surfaces_b=3 receipts_ok=1 diffs=14 validator=0 representation=0 unknown=0 verdict=same-object record_equal=1 determinism=1 control_ok=1 tool_offline=1 selftest_ok=1 tool_absent=0 met=true`, exit 0 (`controls/after-c2.txt`); tip `2586243e` also `met=true` (`controls/after-c2-tip.txt`) | `304c0f87…` (carrier); `64847b5f…` (tip) |

Controls actually exercised: C1 selftest `selftest: 9/9 passed`, exit 0, and the junk-prose tree
`open=6 closed=0 met=false`, exit 1; C2 counter selftest `9/9`, exit 0, tool selftest `6/6` nested in
it, and the identical-pair tree `control_ok=0 met=false`, exit 1. Every receipt was committed before
the after-state it governs; nothing was re-cut after measurement.

## Sources & frontier

- **Census.** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake` —
  round start exit **0** (22 `W04`, one `ok` line; log `kake ok …/corpus/SOURCES.md`), round end exit
  **0** with 22 `W04` (`.ufo/waves/round-83/controls/census-after.txt`); the registry is not missing,
  so the exit-2-at-round-start case does not apply.
- **Rows.** `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: base `826b0061`
  → **193**, tip `64847b5f` → **194**. Added: `S456` (tier **A**, kind `spec`, status `mined`,
  `opened 2026-11-04`, `recheck 365d`, `used-by corpus/knowledge/header-change-classes.md`). Rows
  touched old→new: none in place — `S456` is new and no other row changed cell. Rows opened this
  round: `S456` only (RFC 9111), fetched once GET-only and retained at
  `w1/ScoutSources/rfc9111.txt`; the Gate records the admission quote and three rejects (the
  65-word freshness paragraph over the ≤25-word cap; the `ETag`-as-validator span already owned by
  `S455`; two sections the code does not implement).
- **Frontier rows advanced.** The round-82 drift ground (`corpus/README.md` coverage row and
  `PROVINCE.md` §Round 82) narrows to a classified instrument: `corpus/README.md` §Coverage — round
  83 and `PROVINCE.md` §Round 83 record the move; an occurrence oracle and value-level
  classification stay frontier and are the C2 counter's honest limits.
- **Assimilation.** None — the `merge/kake` package still collides on 8 ids (S312, S329, S367, S372,
  S373, S374, S390, S409), unchanged since round 80; nothing adopted, nothing appended from it.
- **SOURCES: 193 → 194 rows**, `W04` 22 → 22, census exit 0 at both ends.

## Trend verdicts

- **expansion — improved.** One net-new admitted `knowledge/` entry on ground the coverage map did
  not hold (`corpus/knowledge/header-change-classes.md`, header-change classification over two dated
  captures), its `source:` citing `S456` — a `mined` row opened this round — and the coverage map
  gained the matching row (`corpus/README.md` §Coverage — round 83). Registry 193 → 194.
- **quality — improved.** Both claims are decided by counters with committed base/junk/control pairs
  and green selftests; six routed defects close, one of them a standing `corpus/QUALITY.md` criterion
  against Gate-summary drift; the classifier turns the round-82 record's undifferentiated
  `changed=<n>` into a decision-grade `same-object` verdict with a control that proves the verdict
  can flip; the round-82 mutation survivors are closed (four kills, one proven equivalence).
- **discernment — unchanged (owed).** This round's own gate decisions (S456 admit, three rejects)
  have not yet been spot-checked by a non-author; the closure owes that check, as round 82's closure
  carried it for S455. The round's own mistakes were mined into `corpus/lessons/round-83.md`
  §Mistakes with fixes shown able to fail, which is the author-side half of discernment only.

## SHONEN

Box count matches `SHONEN.md` (`grep -c '^- \[' SHONEN.md` → 4); no box is `[x]`, so this round
supplies no promotion evidence.

- [~] **SKILL.md contains real decision tables, error patterns, checklists, cited sources** — author-side only; ledger row `box 1` `status=evidenced` (scopes amendment 1 A11 (i)–(iv)), evidence `SKILL.md` unchanged from the round-77 base to the round-78 carrier; not re-measured this round.
- [ ] **At least one end-to-end domain task executed and logged in LOG.md** — declared gap in ledger row `box 2`; this round's LOG entry adds the classifier trial but the row's flip condition (one named receipt path resolving at the revision) still fails on `.ufo/waves/round-47/verification/offline-sweep-r46-verdict-time.txt`.
- [~] **Instructions executable by an agent without oral context** — author-side only; ledger row `box 3` `status=evidenced` over `scripts/*.py|sh`, counter paths and `python3 -B` targets; the three `node ~/Projects/webzites/...` spans and `scripts/kimi-surface.mjs` remain the row's open defect.
- [~] **No cross-domain bleed (PROVINCE.md still accurate)** — author-side only; ledger row `box 4` measured 0 sibling-repo citations across the `corpus/knowledge/*.md` population; this round added one entry citing no sibling path, and `PROVINCE.md` §Round 83 records the move.

## Open L0 questions

None filed this round; the lane rides the existing unresolved operator items (calibration sub-axis
ruling, CJK quote-length rule, SHONEN promotion, `wip/operator-save-20261023`) unchanged.

## Tool installs

None. No install or upgrade; pacman untouched (host-wide pause respected).
