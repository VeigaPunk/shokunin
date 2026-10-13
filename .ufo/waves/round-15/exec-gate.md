# exec-gate.md — round-15 closure gate (`closure-check.py`, protocol lane round 15)

Artifact: `.ufo/waves/round-15/closure-check.py` (2060 lines, stdlib only, read-only, exit map 0/1/2/3).
Durable evidence: `proofs.txt`, the two digest-pinned snapshots under `frozen/`, this execution record, `mutation-gate.md`, and reproducible selftest commands. Ephemeral stdout captures were deliberately not retained.

## 1. Provenance of the base

| revision | lines | state |
|---|---|---|
| `.ufo/waves/round-12/closure-check.py` | 1536 | r12 canonical gate |
| `.ufo/waves/round-13/closure-check.r13.py` | 1566 | **dead duplicate** — pin path `.ufo/waves/round-13/history-pin.json` (that file never existed), no counter source, selftest 15/19 (its own `"closure-sample" in inp.root` short-circuit disabled the pin check for every fixture) |
| `.ufo/waves/round-13/closure-check.py` | 1759 | evolved r13 successor — **the base of this revision** (selftest 19/19, live run sees kama) |
| `.ufo/waves/round-15/closure-check.py` | 2060 | this revision; final sha256 `0ac440f7a3b3a7500568fa469b7efba451ee0eabb9683b827630dcc0869a778c` |

Diff sizes (`diff -u BASE r15 | grep -c '^[+-]'`): vs r12 `+664/-140`, vs r13.py `+659/-164`, vs r13-final `+430/-128`.
Every sound r13-final addition is carried; the two r13.py-only deltas above are deliberately **not** carried.

## 2. Semantic deltas

### 2.1 carried from r13-final (r12 → r13-final, unchanged here)

1. **Lane universe** = MANIFEST `roster` ids ∪ base `LANES` ∪ `.ufo/state/<lane>.round` counters, assembled *before* the log is parsed (r12 filtered `lane in LANES` in the parser and could not see a mid-round mint at all).
2. **History pin** at the canonical `.ufo/history-pin.json` with canonical-JSON digest, anchor verification (`history_pin_unverifiable` / `history_pin_unanchored` / `history_pin_orphan`), `--pin` override.
3. **Frozen roots** resolved across every `.ufo/waves/*/frozen` root (newest first, bare name ambiguous ⇒ exit 3), `--frozen-root`, `--frozen <wave>/NAME`; `expected.json` `inputs` digest verification ⇒ `snapshot_tampered` exit 2; a baseline without digests reads `unpinned (legacy)`.
4. **`prompt_untracked`** debt class (`git ls-files -o` under `.ufo/prompts`, integrator step-4 duty) instead of a silent hand-sweep.
5. `MAIN_LANES`/child-lane derivation, deeper `.ufo/waves/**` activity globs, `.ufo/history-pin.json` + `PROTOCOL-APPENDIX.md` in protocol write scope.

### 2.2 new in round 15

1. **Lane universe closed over log + prompt lanes** (A:42 residual, mutant m10). `_lane_universe` = roster ∪ base ∪ counters ∪ lanes named by a dispatch/complete/wrap line ∪ lanes named by a prompt file; `_parse_log` collects every lane unfiltered and `_open_lane_universe` opens the buckets afterwards. A lane whose counter file was deleted stays adjudicable from its log lines instead of going invisible — proof 1 below.
2. **`unknown_lane` class** (could-not-evaluate) with two reachable homes: (a) a dispatch/complete/wrap line whose lane token the lane-id grammar cannot read — caught by new loose regexes so the line can never be silently dropped; (b) a `lane_rounds` key naming a lane *no* source knows (r13-final validated `lane_rounds` **values** but never keys, so such an annotation was silent).
3. **Non-closure entries reported, never skipped** (P:208-211, A:43). `build_ledger` now returns a dict and reports every non-adjudicated entry with `type`, `recognized` (`mint`/`scaffold`/`work`/`ops`) and whether it carries lanes/notes; a type outside that vocabulary is `unknown_entry_type` (could-not-evaluate). Live `rounds[36]` (`type:"mint"`) is now printed where r13-final skipped it without a word.
4. **Third driver verb `wrap <lane> round=N complete; NOT respawning (fleet-wrap)` counts as termination evidence** (the line says `complete`). 22 such lines exist in the live log; r13-final matched none of them, so a wrap-only mission read as still in-flight. Proof 3 shows the class of change and that today's live debt is unchanged by it.
5. **could-not-evaluate bucket.** Findings the gate cannot adjudicate are excluded from `debt` (so a frozen baseline's pinned debt unit stays comparable) and drive exit 2 only when there is no debt; `cne=` joined the verdict line, `_counts` gained `could_not_evaluate`/`unknown_lane`/`unknown_entry_type`/`nonclosure`/`nonclosure_unrecognized`, and text + frozen output gained `== Could not evaluate ==` and `== Non-closure entries ==` sections plus a `lane universe:` header line naming counter-only (probation) lanes.
6. **Docstring re-anchored** to the landed 470-line `PROTOCOL.md` (section heading + line span, `A:<row>` for `PROTOCOL-APPENDIX.md` rows) and one explicit exclusion recorded: `.ufo/watchdog-driver.log` is **not** an evidence source (the driver holds fd1/fd2 on it as a launcher redirect and writes every dispatch/complete line to `.ufo/watchdog.log`; it is empty when healthy).
7. **Selftest** fixture root is this revision's own `fixtures/closure-sample`; the comparison may now pin `could_not_evaluate`/`unknown_lane`/`unknown_entry_type`/`nonclosure`/`nonclosure_unrecognized` when present in `expected.json` (the five r12 keys are still the required minimum), and a failing case prints the full observed counts.

Lane-id grammar widened `[a-z]+` → `[a-z][a-z0-9_-]*`; `EXIT_*` map, `--selftest`, `--frozen`, `--json`, `--show-keying`, `--no-ledger`, `--no-citations`, citation sweep and the read-only guarantee are unchanged.

## 3. First amended gate selftest — historical 24/24 before final parser/`closed_at` guards

```
closure-check: ok selftest passed=24/24 failed=0
  ambiguous-supersedes                   pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  bad-status                             pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  contradiction                          pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  counter-deleted-dispatch-only          pass  exit=1 debt=1 contradictions=0 unrowed_terminated=1 pending_round=0 could_not_evaluate=0 unknown_lane=0 nonclosure=0
  failed                                 pass  exit=0 debt=0 contradictions=0 unrowed_terminated=0 pending_round=0
  history-pin-absent                     pass  exit=1 debt=1 contradictions=0 unrowed_terminated=0 pending_round=0
  history-pin-invalid                    pass  exit=1 debt=1 contradictions=0 unrowed_terminated=0 pending_round=0
  history-pin-mismatch                   pass  exit=1 debt=1 contradictions=0 unrowed_terminated=0 pending_round=0
  history-pin-unverifiable               pass  exit=1 debt=1 contradictions=0 unrowed_terminated=0 pending_round=0
  in-flight-live                         pass  exit=0 debt=0 contradictions=0 unrowed_terminated=0 pending_round=0
  in-flight-terminated                   pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  kama-counter-admitted                  pass  exit=0 debt=0 contradictions=0 unrowed_terminated=0 pending_round=0 could_not_evaluate=0 unknown_lane=0 nonclosure=0
  keying-violation                       pass  exit=1 debt=1 contradictions=0 unrowed_terminated=0 pending_round=0
  lanes-list-duplicate                   pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  legacy-unadjudicable                   pass  exit=0 debt=0 contradictions=0 unrowed_terminated=0 pending_round=0
  marker                                 pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  mint-nonclosure-entry                  pass  exit=0 debt=0 contradictions=0 unrowed_terminated=0 pending_round=0 could_not_evaluate=0 unknown_lane=0 nonclosure=1 nonclosure_unrecognized=0
  not-dispatched-without-lane_rounds     pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  ok                                     pass  exit=0 debt=0 contradictions=0 unrowed_terminated=0 pending_round=0
  prompt-orphan                          pass  exit=1 debt=1 contradictions=0 unrowed_terminated=0 pending_round=0
  unknown-lane                           pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  unknown-lane-annotation                pass  exit=2 debt=0 contradictions=0 unrowed_terminated=0 pending_round=0 could_not_evaluate=2 unknown_lane=2 nonclosure=0
  unrowed                                pass  exit=0 debt=0 contradictions=0 unrowed_terminated=0 pending_round=1
  wrap-terminated-unreported             pass  exit=1 debt=1 contradictions=0 unrowed_terminated=1 pending_round=0 could_not_evaluate=0 nonclosure=1
selftest: 24/24 passed
```

All 19 r12/r13 fixtures are carried verbatim (tree + `expected.json` + fixture-relative `.ufo/history-pin.json`); five are new:

| fixture | what it pins |
|---|---|
| `kama-counter-admitted` | a lane whose **only** trace is `.ufo/state/kama.round` (no roster row, no log line, no prompt) is adjudicable: the `{kama: ok}` row with its report passes, universe 9 lanes, `kama` listed as counter-only. |
| `counter-deleted-dispatch-only` | **m10 residual**: dispatch + complete lines, counter file *deleted*, no roster row, no report ⇒ `unrowed_terminated` debt (not blind, not a crash). |
| `mint-nonclosure-entry` | a `type:"mint"` entry (no `lanes`) is reported as a recognized non-closure entry (`nonclosure=1`) and the closure row beside it still grades clean. |
| `unknown-lane-annotation` | both `unknown_lane` homes: an unreadable lane token (`launch Kama.1 round=1`) and `lane_rounds: {"ghost": 3}` ⇒ `cne=2 / unknown_lane=2`, exit 2 with `debt=0`. |
| `wrap-terminated-unreported` | the fleet-wrap verb alone terminates a lane-round that never reported ⇒ `unrowed_terminated` debt. |

## 4. Mutation proofs (`.ufo/waves/round-15/proofs.txt`)

```
### proof 1: m10 residual (dispatch-only lane, counter file deleted) — r13-final vs r15
$ python3 .ufo/waves/round-13/closure-check.py --repo …/counter-deleted-dispatch-only --no-citations
closure-check: ok debt=0 contradictions=0 unrowed_terminated=0 pending_round=0
$ python3 .ufo/waves/round-15/closure-check.py --repo …/counter-deleted-dispatch-only --no-citations
closure-check: debt debt=1 contradictions=0 unrowed_terminated=1 pending_round=0 cne=0 nonclosure=0
unrowed_terminated     kama       r1    entry=-    dispatch `… launch kama round=1 …` with termination
      evidence and no row: complete at 2026-09-27T10:31:00-03:00, counter unknown   [suggested failed]

### proof 2: driver counter as a universe source (fixture kama-counter-admitted)
$ python3 … r15 --repo …/kama-counter-admitted  # .ufo/state/kama.round present
closure-check: ok debt=0 … cne=0 nonclosure=0
lane universe: 9 lanes (protocol, aggregator, kasegi, kengaku, kake, kumitate, kotoba, kagi, kama)  counter-only (probation, no roster row): kama
$ mv .ufo/state/kama.round away; python3 … r15 --repo …/kama-counter-admitted
closure-check: debt debt=1 contradictions=1 … cne=1 nonclosure=0
unknown_lane           kama       r1    entry #0 lane_rounds[kama]=1 annotates a lane no evidence source knows: not in the roster, the base lanes, the driver counters, the log, or the prompt set (A:42)

### proof 3: fleet-wrap verb as termination evidence (fixture wrap-terminated-unreported)
$ python3 .ufo/waves/round-13/closure-check.py --repo …/wrap-terminated-unreported  # blind to wrap
closure-check: ok debt=0 … pending_round=1
$ python3 .ufo/waves/round-15/closure-check.py --repo …/wrap-terminated-unreported
closure-check: debt debt=1 contradictions=0 unrowed_terminated=1 pending_round=0 cne=0 nonclosure=1
$ same, wrap line deleted (mutant): expect pending_round, debt 0
closure-check: ok debt=0 … pending_round=1 cne=0 nonclosure=1

### proof 4: non-closure entry reporting (fixture mint-nonclosure-entry)
$ python3 .ufo/waves/round-13/closure-check.py --repo …/mint-nonclosure-entry --no-citations
closure-check: ok debt=0 contradictions=0 unrowed_terminated=0 pending_round=0        # mint entry invisible
$ python3 .ufo/waves/round-15/closure-check.py --repo …/mint-nonclosure-entry --no-citations
closure-check: ok debt=0 … nonclosure=1
entry #0    round=11.5   type=mint      recognized=yes lanes=0 notes=yes
```

### proof 5: the drafted round-15 ledger (18 appended entries) under this gate
```
$ python3 .ufo/waves/round-15/closure-check.py --repo /tmp/r15-smoke2 --no-citations
closure-check: debt debt=1 contradictions=0 unrowed_terminated=0 pending_round=0 cne=0 nonclosure=5
kama           1  ok                61  closure             CLOSED_AT                 -
kama           2  in-flight         62  closure             CLOSED_AT                 -
kama       r2    entry=62   2026-09-29T00:19:34-03:00 launch kama round=2 runId=shokunin-r2-kama-r1790651973
kama       r1    dispatched 2026-09-28T22:44:08-03:00 after round 1 closed 2026-09-28T18:21:16-03:00 -> rides the next closure-correction for 1
kama       r2    dispatched 2026-09-29T00:19:34-03:00 after round 2 closed 2026-09-28T18:21:16-03:00 -> rides the next closure-correction for 2
kama           2  2026-09-29T00:19:34-03:00     1470  silent       no lane-authored commit and no file newer than the launch
```

## 4b. Cross-check against the drafted round-15 ledger (proof 5)

LedgerExecutor's draft (`.ufo/waves/round-15/round15-entries.json`, 18 entries; their `/tmp` smoke root was gone, so this rebuilt one: live `MANIFEST.json` + the 18 entries, `.ufo/*` symlinked to the live tree) grades without a single `unknown_lane` finding:

```
$ python3 .ufo/waves/round-15/closure-check.py --repo /tmp/r15-smoke2 --no-citations
closure-check: debt debt=1 contradictions=0 unrowed_terminated=0 pending_round=0 cne=0 nonclosure=5
kama 1 ok / kama 2 in-flight      (ledger rows 61/62; no unknown-lane, no contradiction)
```

The one remaining debt item is a **smoke-root artifact**, not a ledger defect: `history_pin_unverifiable — cannot read ae19fca:MANIFEST.json (git exit 128)`, because `/tmp/r15-smoke2` is not a git work tree, so the pin's anchor commit cannot be read. Likewise, the stale-mission probe reports `kama r2 … silent` there because the smoke root carries no `kama-shokunin/` child repo (the probe is not a verdict and not debt). Run the gate against the real repo for both checks.

Also note: the r12 gate over the same appended ledger reads `debt=2 contradictions=2` (both `unknown_lane (P:207)` on kama r1/r2) purely because its hardcoded `LANES` omits kama — the divergence LedgerExecutor measured.

## 5. Historical live run — `python3 .ufo/waves/round-15/closure-check.py` → exit 1

```
closure-check: debt debt=26 contradictions=0 unrowed_terminated=10 pending_round=9 cne=0 nonclosure=5
repo: /home/vgpnk/Projects/shokunin  mode: live  manifest entries: 48  log lines: 316  dispatches: 121  completes: 126
lane universe: 9 lanes (protocol, aggregator, kasegi, kengaku, kake, kumitate, kotoba, kagi, kama)  counter-only (probation, no roster row): kama
history pin: anchored at ae19fca k=48 prefix=ce97497ed699
```

(`completes: 126` = 104 `complete` lines + the 22 fleet-wrap lines counted as termination evidence; the live log grows while the fleet runs, so this was the named execution instant, not a stable constant.)

Gate-to-gate comparison on the same live tree:

| gate | verdict |
|---|---|
| round-12 | `debt=16 contradictions=0 unrowed_terminated=9 pending_round=8` (kama invisible: `LANES` hardcoded) |
| round-13.r13.py | `debt=17 … unrowed_terminated=9 pending_round=8` (pin unavailable, kama still invisible) |
| round-13 final | `debt=26 … unrowed_terminated=10 pending_round=9` |
| **round-15** | `debt=26 … unrowed_terminated=10 pending_round=9 cne=0 nonclosure=5` |

The kama lane-rounds appeared in that round-15 output:

```
unrowed_terminated     kama  r1  entry=-  dispatch `2026-09-28T22:44:08-03:00 launch kama round=1 …` with
      termination evidence and no row: complete at 2026-09-28T23:39:57-03:00, counter 2   [suggested ok]
prompt_untracked       kama  r2  entry=-  .ufo/prompts/kama-round-2.md (1561 B) is untracked: generated
      dispatch evidence is non-durable until the integrator commits it (step-4 write scope)
```

and in the informational rows: `pending_round kama r2` (dispatched `00:19:34`, no termination yet, "rides the next closure-correction for 2"), `dispatched after their round's closure: kama r1 (after 18:21:16) / kama r2`, stale-mission probe `kama r2 … progressing lane file: tools/kama-probe.sh`. The five non-closure entries reported are `#0 scaffold r0`, `#1 work r1`, `#2 ops r1.5`, `#3 work r9`, `#36 mint r11.5`.

Why the r12 gate reads 16 and this gate 26 on the same bytes — debt-class histograms from `--json`:

| gate | debt | classes |
|---|---|---|
| round-12 | 16 | `stale_in_flight=7`, `unrowed_terminated=9` |
| round-13 final | 26 | `prompt_untracked=9`, `stale_in_flight=7`, `unrowed_terminated=10` |
| **round-15** | 26 | `prompt_untracked=9`, `stale_in_flight=7`, `unrowed_terminated=10` |

The whole delta is recovered evidence: `+9 prompt_untracked` (the untracked round-15..18 prompts — a class r12 does not have) and `+1 unrowed_terminated` (kama r1, whose dispatch line the hardcoded r12 `LANES` drops). `stale_in_flight` is 7 in both, so the round-15 gate re-grades *nothing* the r12 gate had already graded, and no r12 exit-1 class was redefined. The three round-12 frozen baselines still reproduce their committed verdicts exactly (§6).

## 6. Frozen-baseline evidence

Round 15 now carries two distinct, input-digest-pinned snapshots generated by
`.ufo/waves/round-15/freeze-snapshot.py`:

| Snapshot | `closed_at` | Manifest source | Entries | Expected |
|---|---|---|---:|---|
| `round-15/r15-pre-003400` | `2026-09-29T00:34:00-03:00` | `git-ref ae19fca` | 48 | exit 1, debt 17 |
| `round-15/r15-post-012710` | `2026-09-29T01:27:10-03:00` | live `MANIFEST.json` | 74 | exit 0, debt 0 |

Each `expected.json` pins SHA-256 digests for `MANIFEST.json`, `watchdog.log`,
`reports-index.txt`, `prompts-index.txt`, `state-counters.txt`, and
`CLOSED_AT.txt`. Replaying either snapshot through
`closure-check.py --frozen round-15/<name> --no-ledger --no-citations` returns
`baseline: match` with its expected exit. The older round-12
`pre`/`post-actual`/`post` baselines remain deliberately `unpinned (legacy)`
and still reproduce 1/1/0.

Distinct names avoid the fail-closed duplicate-name rule. A missing baseline
still exits 3; an edited pinned input exits 2 (`snapshot_tampered`) before any
verdict comparison.

## 7. Residuals (honest, not silent)

- **The universe is closed over the sources the gate reads** (roster, base lanes, counters, log, prompts). A lane with no counter, no log line, no prompt and no roster row is not observable by construction — the union narrows but cannot close that, since nothing in the tree names the lane.
- `.ufo/prompts/<id>-round-N.md` for an id outside the universe is reported through `inp.foreign`; today the ladder (prompt lane ⇒ universe member) makes that branch unreachable, kept as a tripwire rather than dead code.
- Frozen `prompts-index.txt` pins parseable prompt names, not git trackedness. Frozen replay therefore re-derives closure status, lane-universe, and input bytes, but not live-only `prompt_untracked` debt: the pre snapshot carries 17 closure findings while the same historical live run also carried nine untracked prompts. A later generator must encode trackedness before claiming that durability dimension is replayed.
- `nonclosure` entries are reported and excluded from tallies but not schema-checked beyond type recognition; a `mint` entry whose notes omit the probation pointer is not a gate finding (it is protocol prose, reviewed by the integrator).
- The stale-mission activity probe still reads "files modified under its repo" as activity; the `progressing-weak` grade (sibling-authored only) is carried unchanged from r13-final (A:40).
- `.gitignore` still omits `kama-shokunin/` (gitlink hazard, `?? kama-shokunin/` in `git status`). The nine prompts untracked at the historical live instant became durable in `896660a`; three prompts generated before the follow-up snapshot landed in `bfc5db9`. Later prompts are moving fleet state, not backdated into the `01:27:10` measurement. The empty `.ufo/watchdog-driver.log` remains an excluded launcher redirect, not evidence.

## 8. Final integration amendments

- Final gate sha256: `0ac440f7a3b3a7500568fa469b7efba451ee0eabb9683b827630dcc0869a778c`.
- Checker control: 27/27 (25 fixture repos + two parser unit checks). The added
  cases reject an invalid `closed_at`, preserve hyphenated prompt lane ids, and
  ignore non-round prompt names without crashing.
- Snapshot-generator control: 37/37. It uses the same lane-id grammar, includes
  off-roster counter/prompt lanes, excludes wrap-only counters, round-trips
  lane-less debt, and permits only the round-15 frozen output root.
- Final mutation campaign: 7/7 killed with an identical live-gate hash before
  and after. The two final arms remove `closed_at` validation and restore the
  v1 prompt parser; `invalid-closed-at` and `prompt-key-hyphen` kill them.
  Full commands and outcomes are in `mutation-gate.md` §FINAL.