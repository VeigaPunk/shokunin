# revenger — round 68 report (hyaku, attempt 2)

lane: revenger · lane repo: `/home/vgpnk/Projects/shokunin/revenger-shokunin` · fleet root:
`/home/vgpnk/Projects/shokunin` · round: 68 (campaign target 100) · date: 2026-10-25
base at pre-registration: `f165908aaffcf14798de53405fe788986bd33ff9` · final measured lane tip:
`d00f77942d78cb9a3b41547370d7a8a4ebea6c72` (`ahead=0`, `untracked=0`).

Stale-lane: none — this is the respawn-per-round driver's round 68 for this lane; no other mission of
this lane is open. Attempt 2 inherits attempt 1's two committed round-68 revisions and its two
untracked wave-spec files; both are re-verified and named below.

## Work performed

**Declared claims (frozen before any after-measurement, `reports/round-68/claims.md` at `f505526`,
counter `reports/round-68/measure.py` sha256 `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766`):**

- **C1 — calibration, new criterion C8 on the embedded-output surface: the registered gate must
  attribute its own kill.** Frozen predicate: gate present, self-test pass, control 1/1, the frozen
  mutant killed 1/1 **and attributed 1/1**, a new negative control (same mutant with the marker text
  spoofed) killed 1/1 **but not attributed** (0/1), the r65 red snapshot still detected,
  `HOLDS_OK_V5=yes`, `HOLDS_OK_V6=yes`, counter exit 0.
- **C2 — coverage, knowledge-map ground K (lowest non-retired criterion, 5.7): the C05 re-gate,
  third pass, with every spec line number derived by a committed script from the pinned snapshot.**
  Frozen predicate: `K_HELD_BACKED=9/14`, `K_HELD_BACKED_STRICT=9/14`, C05 row `held` naming exactly
  the round-68 entry, legend mismatch 0, `HOLDS_C2_V3=yes`, `C7_V3_CLEAN=yes`, every applicable
  Q01–Q13 wave decision PASS, spot-check not REJECT, counter exit 0.

**Round shape — ONE v2 wave of exactly 64 seats** under
`scripts/hyaku/ufo-wave-policy-v2.json` (band 64–128), validated `plan` exit 0 with
`counts.spawn=64` and `dispatch.calls=1`, dispatched as exactly one batched `task` call after
`wave-slot.sh acquire revenger round-68-w1 64` printed
`granted lane=revenger wave=round-68-w1 seats=64 live=66 pending=0 cap=256`. Role mix: reviewer 25,
critic 15, executor 12, mutation-tester 3, scribe 3, sentinel 2, scout 1, simplifier 1, connector 1,
revenger 1 — **attack roles 46/64 = 71.9 %**. §3 planner seat held by the L1 (the validator rejects
`planner`; `R68WaveContractAudit` obtained the validator's own `unknown_role` message); the bounded
planning data-walk rode `R68AnchorBlind` (scout) and `R68ConnectorOverlap` (connector).

Work items, each with its evidence pointer:

- **C1 build (inherited, re-verified).** `corpus/check_embedded_outputs.py:135-146` — the drifted
  case is an `if not caught:` branch that prints `MARKER` as its last line and exits 1; the dead
  `ok()` helper is gone. Independent verification: `R68MutC7Kill` (frozen mutant, one hunk, exit 1,
  last line `drifted entry output accepted`, control green), `R68MutC7Spoof` (2×2 isolation:
  mutant-only attributed, mutant+spoof not attributed, pristine green, spoof-only green),
  `R68ReviewC7Gate` (full exit inventory, no shadowing require on the mutant path),
  `R68MutC7Entry` (drift injected into the v3 candidate at entry:25/200 caught with the exact line,
  appended text rejected), `R68C7Hermetic` (three identical runs, `strace`: 12 mutating ops all
  inside TMPDIR, zero network), `R68SimplifierGate` (8-line minimal form; `ok()` removal correct).
- **C1 measurement.** `reports/round-68/measure-after.log` on the final measured tree:
  `C7_MUTANT_KILLED_ATTRIBUTED=1/1`, `C7_NEG_SPOOF_KILLED=1/1`,
  `C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1`, `C7_RED_ON_R65_CANDIDATE=yes`, `HOLDS_OK_V5=yes`,
  `HOLDS_OK_V6=yes`, exit 0 — replayed independently by `R68HoldSweep` and `R68CounterIntegrity`.
- **C2 build (inherited, re-verified).** `corpus/derive_axml_anchors.py` (`bce497d6…1f249`, exit 2
  on a missing/ambiguous symbol), `corpus/snapshots/ResourceTypes.h` (byte-exact copy,
  `56b88bc4…c56f`, 86255 B, tracked and unignored), `corpus/knowledge/round-68-apk-axml-byte-evidence.md`,
  `corpus/SOURCES.md` row S046. Anchors: `R68AnchorDerive` (16/16 symbol lines re-derived, failure
  contract exercised), `R68AnchorBlind` (blind derivation CONCUR; `:244`→`:245` repair real),
  `R68SpotcheckDiscern` (AGREE/AGREE on S046 and on the tier-A claim).
- **C2 adjudication — the wave's Q decisions on the landed v3 bytes are FAIL at Q04, Q05, Q07, Q08
  (that seat routed the row to Q11 and returned FAIL under it), Q11 and Q13; PASS at Q01, Q02, Q03,
  Q06, Q09, Q10 and Q12 (n/a).** Root cause, found independently by five seats: item 11 claims
  *every* stated S038 line number is printed by the derivation script, while `:237` and `:244` are
  stated and never printed (`R68ReviewEntryQ04` §F1, `R68ReviewEntryQ11`, `R68ReviewEntryQ13`,
  `R68CriticEntryDeps`, `R68AnchorCritic`); item 5's struct widths are a Python literal
  (`readout.py:51-58`) presented as computed from S038 (Q04 §F2); item 9's namespace-resolution
  sentence is ungrounded and contradicted by the entry's own output (Q07). Kill rule executed in one
  revision: C05 stays `uncovered`, the v3 entry carries `admission-status: rejected` with every
  other byte kept, the r65/r67 candidates untouched. **C2 is FALSIFIED — honest stop.**
- **Registered repairs (not claims).** **D1** — this report restates attempt 1's end at committed
  strength only (§Attempt 2 inheritance); no per-seat transcript or stop reason is claimed.
  **D2** — `SKILL.md` gate-registry row rewritten from the after-run: `self-test` cell now
  describes the reachable marker as the last line and both controls and *names* the single-line-
  fixture limitation; `verdict map` now declares `64` and both exit-1 finding kinds; `pinned-value
  path` declares `unpinned (legacy)`; `measured-against` re-pointed to the round-68 counter; the
  §"No gate registry" bullet corrected; §6.1 now lists `C7_*`, `HOLDS_OK_V5`/`V6` and the V6↔C05
  coupling. **D3** — S045's quoted sentence is 19 words (lesson) / 14 (row anchor), both ≤ 25;
  recorded as a superseding row, `round-67.md` byte-preserved. **D4** — case (b): the r68 candidate
  was rejected, so S045's `used-by` is unchanged and D4 stays open and named.
- **Registry repair.** `corpus/SOURCES.md` S046 `used-by` `—` → the round-68 entry (removes the
  census `W03`; `R68CensusReplay`, `R68ReviewSourcesS046` HIGH) and the blank line that split the
  registry into two pipe tables removed.
- **considerthese (operator input, mined read-only).** `considerthese/2026-10-24.md`
  §Self-improvement proposal 1 (hex/ASCII sanity pass on candidates) grounded through the lane's own
  bar and landed as `corpus/QUALITY.md` **Q14**, whose first exemplar is the rejected v3 entry's
  line 46 (`4d616e69666573742d` = 9 bytes, prose calls it "the 16-byte prefix").
- **Frontier step (§2b).** Census before/after with both outputs and exit codes; one mistake
  family mined (M46, with M47); C2's rows rest on `S038`/`S046` opened this round.
- **Housekeeping.** A seat's non-`-B` import left an untracked
  `corpus/__pycache__/check_embedded_outputs.cpython-314.pyc`; deleted before the commit. Misroot
  sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`) found only driver-owned
  `.ufo/state/*`, `.ufo/watchdog.log`, harness files and `.scratch/` — **no lane-authored file in
  the fleet root**, so nothing to repatriate.

## Landed changes

| change | commit (pushed) | LOG.md entry |
|---|---|---|
| pre-registration: claims, frozen counter, red-before receipt (attempt 1) | `f505526f7ecf4ac1ad51d99aa2d1dd5c57c0bae0` | §Round 68 declaration and build |
| build: C7 attribution repair, anchor derivation + snapshot copy, v3 candidate, S046 row, `build-r68.py` (attempt 1) | `4232235723cf8d4731a1e7e78ca098b8af953a57` | same |
| adjudication: v3 `rejected`, SKILL registry + §6.1, S046 `used-by` + table split, QUALITY Q14, lesson, SCORECARD, LOG, 64-seat wave evidence + dispatch receipt | `14774a2c3cd3918364f211e08009f9f327b4c7b3` | §Round 68 wave and adjudication |
| first measurement receipt | `dddf1479ad7ba4e4124b02c0a0e32edf399e4c95` | same |
| correction: Q08 recorded as FAIL-under-Q11 (its own verdict) | `1c3460336d14e9bbe64778f826a07bdd996ce39b` | same |
| measurement receipt re-pinned to `1c34603` (counter stdout byte-identical) | `d00f77942d78cb9a3b41547370d7a8a4ebea6c72` | same |

All six are ancestors of the lane branch tip `d00f7794`; the lane is pushed (`local=remote`, `ahead=0`).

## Before → after measurements

Frozen counting command (`reports/round-68/claims.md` §Frozen counter), run by this L1 on trees
exported from committed bytes — never on a working tree:

```sh
T=$(mktemp -d /tmp/rev-r68-after2-XXXX)
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 1c3460336d14e9bbe64778f826a07bdd996ce39b corpus | tar -x -C "$T"
cd / && TMPDIR=/tmp python3 -B \
  /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/measure.py "$T"
```

**C1 — calibration (C8 attribution), base `f165908` → final measured tip `d00f7794`:**

| label | before | after | verdict |
|---|---|---|---|
| `C7_MUTANT_KILLED_ATTRIBUTED` | `0/1` | **`1/1`** | improved |
| `C7_NEG_SPOOF_KILLED` / `…_ATTRIBUTED` | `1/1` / `0/1` | `1/1` / `0/1` | hold |
| `C7_MUTANT_KILLED` | `1/1` | `1/1` | hold |
| `C7_SELFTEST` | `pass` | `pass` | hold |
| `C7_RED_ON_R65_CANDIDATE` | `yes` | `yes` | hold |
| `HOLDS_OK_V5` / `HOLDS_OK_V6` | `no` / `no` | **`yes` / `yes`** | improved |
| counter exit | `0` | `0` | hold |

Receipts: `reports/round-68/measure-before.log`, `reports/round-68/measure-after.log` (stdout
byte-identical between the `14774a2c` and `1c34603` trees — `diff` exit 0).

**C1 verdict: improved — the frozen predicate is met on the final measured tree.** Reported, not
hidden: two critics show the predicate is satisfiable by a gate that does not detect drift.
`R68CriticC7Claim` built a gate with no `evaluate()` at all (self-hash check + marker print) and one
where `drift()` accepts a real line plus appended text; both read every C1 conjunct at target.
`R68CriticClaimsC1` reached the same labels by printing the marker from the base gate's shadowed
`require`. `R68CriticC7Surface` showed a `drift(lines[:1], …)` weakening survives. So the counter's
C7 labels establish *marker-presence on a textual mutation*, not behavioural attribution; the landed
gate's behaviour was established by the behavioural seats listed above, and the instrument gap is
routed rather than repaired after the wave (the reviewed artifact stays the measured artifact).

**C2 — coverage (K), base `f165908` → final measured tip `d00f7794`:**

| label | before | after | verdict |
|---|---|---|---|
| `K_HELD_BACKED` / `K_HELD_BACKED_STRICT` | `8/14` / `8/14` | `8/14` / `8/14` | unchanged (honest) |
| `K_ROW C05 status` | `uncovered` | `uncovered` | kill rule executed |
| `C05_SINGLE_V3` | `no` | `no` | unchanged |
| `C7_V3_CLEAN` | `n/a (no v3 file)` | `yes (17 blocks, 0 problems)` | diagnostic only |
| `HOLDS_C2_V3` | `no` | `no` | unchanged |
| counter exit | `0` | `0` | hold |

**C2 verdict: FALSIFIED** — six wave Q decisions FAIL on the landed bytes. The target was not
narrowed and no acceptance condition was repaired: the frozen order ran to its fail branch.

## Sources & frontier

Census, round start (before any round-68 registry edit), exact command and exit code:

```sh
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
revenger	W03	S046 mined but unused
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
CENSUS_EXIT=0
```

Census, round end, same command:

```sh
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
CENSUS_EXIT=0
```

- Rows before → after: **45 → 46** (`| S046 |`, own-work, tier A, opened 2026-10-24 — the only row
  added). Rows by tier: unchanged, A 42 / C 4. The round-start `W03 S046 mined but unused` is gone
  at round end; only the four long-disclosed `W04` duplicate-scope warnings remain.
- Rows touched old→new (append-only fields, logged in `corpus/lessons/round-68.md` §Gate):
  `S046 used-by` `—` → `corpus/knowledge/round-68-apk-axml-byte-evidence.md`. `S045 used-by`
  deliberately unchanged (D4 case b — both its consumers are retained-rejected entries).
- Frontier rows advanced: **none.** C05 stays `uncovered`; K is unchanged at 8/14; `corpus/README.md`
  is byte-unchanged.
- Sourced claims: C2 rests on `S038` (re-opened this round from the committed snapshot) and `S046`
  (own-work, opened this round); C1 rests on the gate's own committed bytes and the frozen counter,
  no source row.
- **Assimilation: none.** This is a resumed round with frozen claims; §10's frozen-round clause
  forbids adopting package material into an already-frozen claim. The lane's §10 quarantine-first
  obligation was discharged in round 67 (26/26 verdicts, adoption closed); the slice re-derived at
  round time is still **26** data rows
  (`awk … > .ufo/waves/round-68/assimilation/quarantine-slice; wc -l` = 26) and remains fully
  quarantined. Nothing from `/home/vgpnk/Projects/shokuknow` was written, fetched or run.
- considerthese: `considerthese/2026-10-24.md` §Self-improvement proposal 1 → `corpus/QUALITY.md`
  Q14 (one proposal, implemented; falsifier transcript in `corpus/lessons/round-68.md` §Mistakes).

## Trend verdicts

- **expansion — unchanged.** No frontier row moved to core, no coverage row became `held`, no new
  family or surface. The C05 candidate was rejected and `corpus/README.md` is byte-unchanged.
  Evidence: `K_HELD_BACKED=8/14` at both ends; `R68ReadmeFlipCheck` measured the row `uncovered`.
- **quality — improved.** The registered gate attributes its own kill
  (`C7_MUTANT_KILLED_ATTRIBUTED 0/1 → 1/1`, `HOLDS_OK_V5/V6 no → yes`); the gate-registry row, the
  §6.1 label set, the S046 `used-by` cell and the registry table split are corrected; the bar gained
  Q14. Every prior hold is green: `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `FRESH_ROWS=18/18`,
  `README_TOKEN_LEGEND_MISMATCH=0`, STRICT window selftest pass, C2–C6 attributed 2/2·2/2·2/2·2/2·4/4,
  `F_COVERAGE=5/8`. Evidence: `reports/round-68/measure-after.log`, `R68HoldSweep.md`,
  `R68CounterIntegrity.md`, `R68ReviewSkillRegistry.md`.
- **discernment — improved (with a named defect).** Five fresh seats falsified C2 on the landed bytes
  before any flip, and the frozen kill rule was executed rather than the target being repaired; the
  outside-discernment spot-check returned AGREE/AGREE. Defect against this lane's own instrument:
  `SKILL.md:268` carried the r67 limitation as current truth until this round's adjudication (M46).
  Evidence: `R68ReviewEntryQ04.md`, `Q05`, `Q07`, `Q08`, `Q11`, `Q13`, `R68SpotcheckDiscern.md`,
  `corpus/lessons/round-68.md` §Mistakes.

## Attempt 2 inheritance (stated at committed strength — D1)

Attempt 1 committed `f505526` (pre-registration) and `4232235` (build) and ended before any wave was
dispatched and before any report existed. What the committed bytes support: `.ufo/watchdog.log`
records `lane-dead-no-report revenger round=68` at `2026-10-25T03:23:08-03:00` and a relaunch 32 s
later. **No per-seat attempt-1 transcript, stop reason or dead-seat record is committed for round
68**, and this report makes no claim about why attempt 1 ended — the r67 lesson's D1 restatement
standard is applied here deliberately (the earlier round's "aborted / 0 seat work" wording was
overstated and is routed, not repeated).

Attempt 1's uncommitted leftovers were exactly two files, `.ufo/waves/round-68/build-wave-spec.py`
and `wave-spec.json`; both are **reused after re-verification** and committed as wave evidence, no
attempt-1 byte discarded unexamined. They also had to be **repaired**: the inherited spec failed its
own validation —

```
$ node ~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs plan --spec .ufo/waves/round-68/wave-spec.json
{"schema":"ufo-swarm-wave-error-v1","code":"invalid_spec","message":"spec.milestone exceeds 256 bytes"}
PLAN_EXIT=1
```

— and it carried **66** seats against the frozen registration of exactly **64**. Repair in the
generator plus regeneration: milestone shortened to 235 bytes; the two duplicate seats dropped
(`R68AnchorBlind2`, fully covered by `R68AnchorBlind`'s independent derivation; `R68CounterReplay2`,
fully covered by `R68HoldSweep`'s counter run over the committed tree); `seats=64 ... attack=46
(71.9%)` printed. Re-validated: `plan` exit **0**, `counts.spawn=64`, `dispatch.calls=1`.

## Round shape, seats, dead seats

- 1 validated v2 wave, **64 seats**, 1 batched call, 46 attack seats (71.9 %); **64/64 seat reports,
  0 dead seats**. Reports: `.ufo/waves/round-68/R68*.md`. Evidence committed with the round:
  `wave-spec.json`, `build-wave-spec.py`, `dispatch/plan-validated.json`, `dispatch/dispatch-run.log`,
  `assimilation/quarantine-slice`.
- Residual `task` call: **none** — the wave produced 64 distinct build/attack items, so no
  follow-up reviewer batch was needed.
- Seat decisions that carried the verdicts: `R68ReviewEntryQ04`/`Q05`/`Q07`/`Q08`/`Q11`/`Q13`
  (C2 FAILs), `R68MutC7Kill`/`R68MutC7Spoof`/`R68ReviewC7Gate`/`R68MutC7Entry` (C1),
  `R68SpotcheckDiscern` (discernment), `R68CounterReplay`/`R68HoldSweep`/`R68CounterIntegrity`
  (instrument), `R68WaveContractAudit` (shape).
- Wave-contract audit verdict: CONTRACT-OK, with three named defects reported and not hidden —
  13 seat prompts carry *abridged* Q-criterion lines (verbatim matches 0/13); `R68ReviewEntryQ08` is
  a redirect to Q11 rather than an independent Q08 read; `R68ReviewSkillRefresh` is the single seat
  serving no claim (1/64, kept because SHONEN box 1 asks for it). A fifth finding (the slot key
  `round-68-w1` vs the spec wave name `revenger-r68-v2`) is recorded; the slot is released under the
  key actually acquired.

## SHONEN

- [x] SKILL.md contains real decision tables, error patterns, checklists, cited sources — named
  non-author verifier `revenger-r64.R64ReviewSkill` (lane-external) on the earlier bytes; this
  round refreshed the gate-registry row and §6.1, and the lane-dispatched seat
  `R68ReviewSkillRefresh` re-read the current bytes (`.ufo/waves/round-68/R68ReviewSkillRefresh.md`)
  and correctly declined to flip the box itself.
- [~] At least one end-to-end domain task executed and logged — `reports/round-68/measure-after.log`
  replay plus the v3 candidate's 15-line readout and 17-line anchor table re-derived by ten seats;
  no producer rerun.
- [~] Instructions executable by an agent without oral context — every §Reproduce command re-run by
  `R68Item1`…`R68Item10`, `R68AnchorDerive`, `R68AnchorBlind`; no outside instruction verifier.
- [~] No cross-domain bleed — `PROVINCE.md` unchanged; `R68ConnectorOverlap` (CONTEST-NAMED,
  ADJ-06 open at `.ufo/l0-questions.md:42`) and `R68SentinelScope` (CONTAINED) report contested scope
  and absorb nothing.

## Open L0 question

Appended to `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`:

`revenger | round-68 | C1's frozen C7 predicate is satisfiable by a non-detecting gate (two critic seats built one). May the next round replace marker-presence with behavioural legs and drop c7_v3_clean from HOLDS_OK_V6, or should the frozen instrument stay as-is and the gap remain a named limitation?`

The round does not block on it.

## Tool installs

None. No package was installed, upgraded or removed this round; the host-wide pacman pause was
respected (python3, node, jq-equivalents and coreutils only; the wave slot and the census script are
already-present repo tooling).
