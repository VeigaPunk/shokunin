# revenger — round 71 report (hyaku run 10, attempt 1)

Lane repo: `/home/vgpnk/Projects/shokunin/revenger-shokunin`, branch `main`.
Base: `b7abcd875c84f4e1d6c8df966b6bd20f4154c53f`.
Final lane tip: `bced500398f3c4aa60536a79642ef78af4a68f20`; `git ls-remote origin refs/heads/main` returned the same hash.

## Work performed

Declared claims: **C1 coverage / knowledge-map ground K**, the lowest scored criterion (C05 sixth pass, target 8/14 → 9/14); **C2 calibration**, the registered embedded-output gate's missing-entry and production-timeout exit-2 classifications.

- Initial claims and counter/controls were frozen before any seat scores at `63b560bec2405228797405ec06a818ee343e61f0`; base receipts are `reports/round-71/claims.md` and `reports/round-71/measure-before.log`. After the W2 sentinel's vote-parser finding, A3 hardened malformed-input handling before the final vote/measurement commit without changing C1's threshold, Q assignments or PASS/n/a rule (`reports/round-71/measure-amendment-A3.md`). The candidate evaluated by fresh wave-2 reviewers is `corpus/knowledge/round-71-apk-axml-byte-evidence.md` at `4c1eeaee88fd07e442f1bd546faf77be3957d390` (SHA-256 `671f55fceb64af27f99c00106f58f9bc2c8b5dc9af6028382ff218655008f092`).
- **C1 falsified / honest stop.** Q09 and Q16 were FAIL; the other 14 outcomes were PASS or n/a. Q09 locates the self-map claim that an out-of-corpus builder was named undigested even though the named generator is inside `corpus/` and is hashed. Q16 locates the item-17 overclaim: `--axml-layout` omits `readout.py:189` (`lineNumber`), `:197` (`styleIndex`), and the entry's locator set omits `:203` (`aoff`). Per-seat decisions and reports are in `.ufo/waves/round-71/w2-votes/` and `.ufo/waves/round-71/w2/`; at `dac9590236f0d3e7213c30ccdb343f0891a36644` the only status flip is the v6 `admission-status` to rejected. README C05 remains `uncovered` (its evidence text records the Q09/Q16 rejection); no repair/re-gate followed.
- **C2 verified.** Final archived-tree counter output shows missing entry `rc=2` and timeout `rc=2`, both without traceback; self-test exit 0 names both legs; `HOLDS_C2_V1=yes`. Independent real-CLI replay reached the production 120-second timeout (`.ufo/waves/round-71/w2/R71W2GateReplay.md:58-68`).
- Two v1 waves dispatched through the ready-file handoff: W1 40 seats (reviewer 9, critic 4, mutation-tester 3, sentinel 1, revenger 1, executor 7, scout 7, scribe 5, connector 2, simplifier 1; 18/40 attackers); W2 34 seats (reviewer 10, critic 5, mutation-tester 4, sentinel 1, revenger 1, executor 5, scout 3, scribe 2, connector 2, simplifier 1; 21/34 attackers). Results: `.ufo/waves/round-71/w1-results.json` and `w2-results.json`. Total 74 seats, 39/74 attackers, 0 empty outputs; L1 held the planner seat. `R71W2ConnCarry` returned a non-empty but unhelpful final string, disclosed here and not counted as dead.
- Curated the frontier: added S052 (own-work, tier A, mined) and S053 (docs, tier A, rejected; supersedes S044); no existing source row was changed in place. Source census receipts: `.ufo/waves/round-71/census-before.txt` and `census-after.txt`.
- Mined M58/M59/M60 in `corpus/lessons/round-71.md`: missing per-verifier HOLD rows, wrong quarantine-register path, and Q09/Q16 self-map overclaims. Each fix has a red-before/result pointer.
- No assimilation: the 26-row quarantine slice was re-derived at `.ufo/waves/round-71/assimilation/quarantine-slice`; no merge/package source was added.

## Landed changes

Every item is recorded in the appended `LOG.md` round-71 entry (`LOG.md:998-1008`); scorecard and lesson are in the final docs commit `bced500398f3c4aa60536a79642ef78af4a68f20` (`SCORECARD.md:646-658`, `corpus/lessons/round-71.md`).

- `63b560bec2405228797405ec06a818ee343e61f0` — frozen C1/C2 claims, counter and controls.
- `18200a4b18e8dfce291a74028a9012ce4401ca10` — v6 candidate, exit-2 gate cases and registered SKILL mapping.
- `da4f1eeae2ff5bb407894e13f7bdccf1b8faf5bd` — timeout-fixture path correction.
- `620849e843e9556ab84b20256794c08219fd37e9` and `4c1eeaee88fd07e442f1bd546faf77be3957d390` — W1 integration and frozen candidate; `PROVINCE.md` fallback pin updated 6.4.0 → 6.5.0 to match scoped route documentation (no provider run/readiness claim).
- `c6e284c6583fa3502754361f411b66646880ba02` — wave-2 freeze/dispatch.
- `a16e6cbe24c51e6952e973d6b47560b49311420d` — explicit post-freeze source/lesson pointer corrections only; candidate bytes and C1 predicate unchanged.
- `33fadb25cdb260ee4a6ac2b0a2bb62c4c1bb8057` — A3 vote parser rejects symlink roots/members and unhashable seats; probes are in `vote-parser-control-a3.txt` and `reports/round-71/measure-amendment-A3.md` (counter SHA-256 `82c817e1c2f7181cae759328fc884b8c38defbdba80dde4aad535d9c1f5f91b2`).
- `da70b5bd2da7274f03d37eb4f49372643d5bf2e0` — W2 results and four per-seat Q vote files.
- `dac9590236f0d3e7213c30ccdb343f0891a36644` — C1 honest-stop status.
- `bced500398f3c4aa60536a79642ef78af4a68f20` — final measurement receipt, lesson, append-only LOG and SCORECARD.

## Before → after measurements

The counter command was `python3 -B reports/round-71/measure.py "$TREE"` with this archived input:

```sh
cd /home/vgpnk/Projects/shokunin/revenger-shokunin
rev=dac9590236f0d3e7213c30ccdb343f0891a36644
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
git archive --format=tar "$rev" corpus SKILL.md SCORECARD.md SHONEN.md .ufo/waves/round-71/w2-votes | tar -xf - -C "$tmp"
python3 -B reports/round-71/measure.py "$tmp"
```

`reports/round-71/measure-before.log` is the base run on `b7abcd875c84f4e1d6c8df966b6bd20f4154c53f`; `reports/round-71/measure-after.log` is the final vote/adjudication run on `dac9590236f0d3e7213c30ccdb343f0891a36644`. Counter SHA-256: A3 `82c817e1c2f7181cae759328fc884b8c38defbdba80dde4aad535d9c1f5f91b2`.

| Claim | Before → after | Result |
|---|---|---|
| C1 — coverage/K | `K_HELD_BACKED=8/14` (5.7) → `8/14` (5.7); C05 `uncovered` → `uncovered`; `C1_W2_Q_VOTES=0/16`; `HOLDS_C1_V6=no` both ends | **Falsified.** Final `C1_GATE` still reports 24 checked blocks / 0 problems and lint `0/0/0/0`, but Q09/Q16 FAIL; no admission credit. |
| C2 — calibration | Missing-entry `0/1 rc=1 traceback=yes` → `1/1 rc=2 traceback=no`; timeout `0/1 rc=1 traceback=yes` → `1/1 rc=2 traceback=no`; self-test `named_legs=0` → `1`; `HOLDS_C2_V1=no` → `yes` | **Verified.** Both real CLI legs meet the registered exit-2 contract; independent replay observed elapsed 120 s. |

No-harm holds at the final measurement: `HOLD_REPLAY=10/10`, `HOLDS_OK_V8=yes`, `F_COVERAGE=5/8`, `FRESH_ROWS=18/18`; retained `EMB_R65` red label and historical pins/drift labels are unchanged. The complete output, including all ten `HOLD <name> exit=0` rows, is `reports/round-71/measure-after.log`.

Counter limitation: its round-70 self-check diagnostic imports `reports/round-70/measure.py` through the live absolute lane path (`LANE`), not the archived `TREE`; this is disclosed in `.ufo/waves/round-71/w2/R71W2Sentinel.md` F4 and `.ufo/waves/round-71/w2/R71W2CounterReplay.md`, not claimed as hermetic.

## Sources & frontier

- **Rows before → after:** 51 → 53. Commands: `git show b7abcd8:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` → 51; `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 53. Frozen manual totals and validation are in `census-after.txt`.
- **Census:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` exited 0 at both ends (`census-before.txt`, `census-after.txt`); disclosed W04/W01 warnings only. Final histogram: tier A=50, C=3; mined=44, queued=4, rejected=5; no malformed/duplicate/enum/missing-used-by violation.
- **Added by tier:** A=2 — S052 own-work mined/90d; S053 docs rejected/on-release and superseding S044. Their final `used-by` values are logged from `—` to the lesson/entry in `corpus/lessons/round-71.md`; no pre-existing row's status/recheck/used-by changed in place. One C05 Paths line (S049 → S052) and one 2026-10-27 Search log line were added (`corpus/SOURCES.md:66-84`).
- **Frontier advanced:** none. C05 remains uncovered, no entry admitted, and no assimilation occurred. The 26-row quarantine slice has no new verdict/adoption; the round-70 verdict counts are historical only.

## Trend verdicts

- **Expansion — unchanged:** no knowledge entry was admitted and C05 remains uncovered (`measure-after.log`, `corpus/README.md:45`).
- **Quality — unchanged:** no admitted entry failed re-check or was strengthened; the sixth-pass candidate's Q09/Q16 defects were caught before admission and it was rejected (`corpus/lessons/round-71.md`, C1 table).
- **Discernment — unchanged:** S052/S053 were offered for outside spot-check, but `R71W2SpotcheckDraft` is a lane-dispatched scribe, not an external reviewer. Independent agreement/disagreement remains pending; no lane result is counted as outside discernment.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists and cited sources — `SKILL.md:288,296`; gate replay verified the registered exit-2 row, but current bytes have no outside confirmation (`R71W2GateReplay.md:103-108`).
- [~] At least one end-to-end domain task executed and logged — `LOG.md:998-1008` and `reports/round-71/measure-after.log` record the round's action and observed outcome.
- [~] Instructions executable by an agent without oral context — `python3 -B corpus/check_embedded_outputs.py --self-test` exits 0 and names both exit-2 legs (`R71W2GateReplay.md:81-87`); no independent cold-run verifier this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:16` pins the documented REA package fallback to 6.5.0; no provider execution/readiness claim or cross-domain source was added.

## Closure metadata

- **Stale-lane:** none observed. At finalization start, `jj-lane.sh state` showed local and remote both at `da70b5bd2da7274f03d37eb4f49372643d5bf2e0`; only this round's adjudication/docs changes followed, and the pushed remote now equals `bced500398f3c4aa60536a79642ef78af4a68f20`.
- **Round shape:** W1 40 + W2 34 = 74 seats; 0 empty results; 39/74 attackers; planner held by L1; no residual call. One W2 output was unhelpful but non-empty and is disclosed above.
- **Tools:** none installed or updated; pacman remained paused.
- **L0:** none filed. No operator decision blocks closure; external discernment remains pending as stated above.
