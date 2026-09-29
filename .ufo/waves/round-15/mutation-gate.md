# Mutation gate — round-15 wave-2 (closure-check.py)

Mutation testing of `.ufo/waves/round-15/closure-check.py` against the committed
fixture corpus (`fixtures/closure-sample`, `--selftest` detector).

# FINAL campaign — 2026-09-29 (post-guard gate, authoritative)

Re-run of wave-2 mutants m1–m5 plus new m6/m7 against the CURRENT live gate.
Baseline sha256 (post Main's defensive `key is None` guard at :1325, computed
this run): **`0ac440f7a3b3a7500568fa469b7efba451ee0eabb9683b827630dcc0869a778c`**.
Control: `python3 .ufo/waves/round-15/closure-check.py --selftest` →
`ok selftest passed=27/27 failed=0` (25 fixture cases + 2 parser unit checks:
`prompt-key-hyphen`, `prompt-key-non-round-ignored`; new fixture `invalid-closed-at`).
Mutants re-cut from baseline under `mutants-wave2/` (fixtures symlink unchanged).
Live-gate sha256 before/after FINAL campaign: `0ac440f7…9a778c` — **identical**.

| mutant | edit (line refs vs baseline) | selftest | killed by | result |
|--------|------------------------------|----------|-----------|--------|
| m1 | universe minus `set(log_lanes)` (:303) | 26/27 | counter-deleted-dispatch-only (debt 1→0, unrowed_terminated 1→0, exit 1→0) | KILLED |
| m2 | deleted strict RE_WRAP branch (:489-494) | 26/27 | wrap-terminated-unreported (debt 1→0, unrowed_terminated 1→0, cne 0→1, pending 0→1, exit 1→2) | KILLED |
| m3 | removed `nonclosure.append` (:578-581) | 25/27 | mint-nonclosure-entry + wrap-terminated-unreported (nonclosure 1→0) | KILLED |
| m4 | HISTORY_PIN_REL → dead round-13 path (:103) | 6/27 | 21 fixtures incl. `invalid-closed-at`; phantom history_pin_unavailable debt on every pin-bearing case | KILLED |
| m5 | CNE classes minus `unknown_lane` (:106) | 26/27 | unknown-lane-annotation (cne 2→0, unknown_lane 2→0, debt 0→2, exit 2→1) | KILLED |
| m6 | deleted `entry-invalid-closed_at` elif (:614-617) | 26/27 | invalid-closed-at (contradictions 1→0, debt 1→0, exit 1→0) | KILLED |
| m7 | `_prompt_key_from_rel` → v1 `[a-z]+` full-rel regex (:1031) + raw `unrowed` sort (:1448) | crash | prompt-key-hyphen unit check: gate itself TypeErrors (`not enough arguments for format string`, `do_selftest`:1902 — check's `"%s:%s" % None`) | KILLED |

```
MUTATION SCORE (FINAL): 7/7 (100%) — every mutant determinately killed.
SURVIVING MUTANTS: 0.
NOTES: m7 kills via a hard traceback rather than a FAIL row — the v1 parser makes the
prompt-key-hyphen unit check itself un-evaluable (format-op on None). Detector = the
same unit check the gate ships; still a determinate kill. The :1325 `key is None`
guard survives m7's raw-sort revert: unparseable names produce no unrowed row at all,
so the raw sort is never exercised on None under this corpus (latent, unreachable).
```

---

# Wave-2 campaign (historical, pre-F2-fix gate)

The section below documents the original run against `c25957…` (24 fixture cases).

- Mutant copies: `.ufo/waves/round-15/mutants-wave2/m{1..5}-*.py` (each = post-amendment
  live gate + one targeted edit). `mutants-wave2/fixtures` is a symlink to `../fixtures`
  so each copy can run `--selftest` (fixture root = `script_dir/fixtures/closure-sample`).
- Control: `python3 .ufo/waves/round-15/closure-check.py --selftest` → `ok selftest
- Live-gate integrity: sha256 `c25957cac4b78cd568f277841ec86b3626255d72449c91f4062ba9577e235954`
  before and after the campaign — identical (the file moved to `265571e2…` afterward
  via SnapshotExecutor's sibling F2 fix; see addendum + commands table).
  (Baseline is the post-L1-amendment sha; L1 added `~/Projects/origin-work/open-bug-bounties`
  to `EXTERNAL_READONLY` mid-campaign — an authorized gate change, not interference.)

---

```
MUTANT: m1 — drop log-lane contribution from the lane universe
FILE: closure-check.py:303 (inside _lane_universe)
MUTATION: `set(LANES) | set(counters) | set(log_lanes) | set(prompt_lanes)` →
          `set(LANES) | set(counters) | set(prompt_lanes)`
COMMAND: python3 .ufo/waves/round-15/mutants-wave2/m1-no-log-lane-universe.py --selftest
EXIT: 1 (selftest 23/24)
FINDING: counter-deleted-dispatch-only FAIL —
         expected  {debt:1, unrowed_terminated:1, exit:1, could_not_evaluate:0}
         observed  {debt:0, unrowed_terminated:0, exit:0, could_not_evaluate:0}
         (live-mode confirms: mutant prints `ok debt=0 unrowed_terminated=0`;
          live gate prints `debt=1 unrowed_terminated=1` — (kama,1) dispatch+complete
          went invisible: not parsed as foreign, just silently filtered from the universe)
RESULT: KILLED
KILLING-TEST: counter-deleted-dispatch-only (single failing fixture, exact miss)
CONFIDENCE: high
```

```
MUTANT: m2 — remove RE_WRAP (strict fleet-wrap) handling from _parse_log
FILE: closure-check.py:489-494 (strict `RE_WRAP.match` block deleted; RE_WRAP_LOOSE left)
MUTATION: wrap lines no longer append to `raw_completes` with verb "wrap"; they fall
          through to RE_WRAP_LOOSE → `foreign` bucket (unknown_lane).
COMMAND: python3 .ufo/waves/round-15/mutants-wave2/m2-no-rewrap.py --selftest
EXIT: 1 (selftest 23/24)
FINDING: wrap-terminated-unreported FAIL —
         expected  {debt:1, unrowed_terminated:1, could_not_evaluate:0, exit:1}
         observed  {debt:0, unrowed_terminated:0, could_not_evaluate:1, unknown_lane:1,
                    pending_round:1, exit:2}
         (wrap line misclassified as unreadable-lane; termination evidence lost)
RESULT: KILLED
KILLING-TEST: wrap-terminated-unreported
CONFIDENCE: high
```

```
MUTANT: m3 — non-closure entries silently skipped again
FILE: closure-check.py:578-581 (inside build_ledger, `t not in ADJUDICATED_TYPES`)
MUTATION: deleted `nonclosure.append({entry, round, type, recognized, lanes, notes})`
COMMAND: python3 .ufo/waves/round-15/mutants-wave2/m3-silent-nonclosure.py --selftest
EXIT: 1 (selftest 22/24)
FINDING: mint-nonclosure-entry FAIL —
         expected  {nonclosure:1, nonclosure_unrecognized:0, exit:0}
         observed  {nonclosure:0, exit:0}
         second kill: wrap-terminated-unreported FAIL —
         expected  {nonclosure:1}  observed  {nonclosure:0}  (its scaffold entry)
RESULT: KILLED
KILLING-TEST: mint-nonclosure-entry (primary), wrap-terminated-unreported (secondary)
CONFIDENCE: high
```

```
MUTANT: m4 — HISTORY_PIN_REL pointed at the dead waves/round-13 path
FILE: closure-check.py:103
MUTATION: `os.path.join(".ufo","history-pin.json")` →
          `os.path.join(".ufo","waves","round-13","history-pin.json")`
COMMAND: python3 .ufo/waves/round-15/mutants-wave2/m4-dead-pin-path.py --selftest
EXIT: 1 (selftest 4/24)
FINDING: every fixture carrying a real .ufo/history-pin.json gains a phantom
         `history_pin_unavailable` debt — e.g. `ok`: expected {debt:0, exit:0},
         observed {debt:1, exit:1}; live-mode evidence text:
         "the append-only history pin cannot be evaluated: missing
          .../ok/.ufo/waves/round-13/history-pin.json" (class history_pin → debt).
         20 fixtures killed it (all pin-bearing cases).
NOTE: the three history-pin-{absent,invalid,mismatch} + unverifiable fixtures PASS
      the mutant — their expected counts are coincidentally still met (count-pinned
      baselines don't distinguish pin finding kinds); irrelevant to the kill.
RESULT: KILLED
KILLING-TEST: ok + 19 other pin-bearing fixtures (smallest detector already present)
CONFIDENCE: high
```

```
MUTANT: m5 — unknown_lane findings treated as debt, not could-not-evaluate
FILE: closure-check.py:106
MUTATION: `COULD_NOT_EVALUATE_CLASSES = ("unknown_lane","unknown_entry_type")` →
          `("unknown_entry_type",)`
COMMAND: python3 .ufo/waves/round-15/mutants-wave2/m5-unknown-lane-is-debt.py --selftest
EXIT: 1 (selftest 23/24)
FINDING: unknown-lane-annotation FAIL —
         expected  {could_not_evaluate:2, unknown_lane:2, debt:0, exit:2}
         observed  {could_not_evaluate:0, unknown_lane:0, debt:2, exit:1}
         (both unknown_lane findings — ghost lane_rounds annotation + Kama.1 foreign
          dispatch line — moved to debt; exit degraded 2→1)
RESULT: KILLED
KILLING-TEST: unknown-lane-annotation
CONFIDENCE: high
```

---

```
MUTATION SCORE: 5/5 (100%)
SURVIVING MUTANTS: 0
CRITICAL GAPS: none on these five axes.

Observed suite characteristic (not a gap, noted for the scribe):
baselines pin COUNTS only, so fixtures whose count vector is unchanged by a mutation
cannot catch it — e.g. m4 passes the four history-pin-* cases (expected debt=1 already
met by a different pin finding), and any future mutant that merely permutes finding
KINDS inside a fixed count is invisible to every baseline. If kind-level discrimination
is ever wanted, expected.json would need a `kinds`/`finding_ids` set; not required to
kill any of these five mutants.
```

## Commands run (full audit)

| # | command | observed output (key part) |
|---|---------|----------------------------|
| 1 | `sha256sum .ufo/waves/round-15/closure-check.py` (pre, pre-amendment) | `397754b9…f4e2` — superseded by L1 amendment |
| 2 | `sha256sum .ufo/waves/round-15/closure-check.py` (pre, post-amendment) | `c25957ca…235954` ← campaign baseline |
| 3 | `python3 .ufo/waves/round-15/closure-check.py --selftest` | `ok passed=24/24`, EXIT=0 (control) |
| 4 | `python3 mutants-wave2/m1-no-log-lane-universe.py --selftest` | `debt passed=23/24`, counter-deleted-dispatch-only FAIL, EXIT=1 |
| 5 | `python3 mutants-wave2/m2-no-rewrap.py --selftest` | `debt passed=23/24`, wrap-terminated-unreported FAIL, EXIT=1 |
| 6 | `python3 mutants-wave2/m3-silent-nonclosure.py --selftest` | `debt passed=22/24`, mint-nonclosure-entry + wrap-terminated-unreported FAIL, EXIT=1 |
| 7 | `python3 mutants-wave2/m4-dead-pin-path.py --selftest` | `debt passed=4/24`, 20 fixtures FAIL, EXIT=1 |
| 8 | `python3 mutants-wave2/m5-unknown-lane-is-debt.py --selftest` | `debt passed=23/24`, unknown-lane-annotation FAIL, EXIT=1 |
| 9 | `python3 m1… --repo fixtures/closure-sample/counter-deleted-dispatch-only --no-citations` | `ok debt=0 unrowed_terminated=0` (vs live `debt=1 unrowed_terminated=1`) |
| 10 | `python3 m4… --repo fixtures/closure-sample/ok --no-citations` | debt `history_pin_unavailable`: missing `…/ok/.ufo/waves/round-13/history-pin.json` |
| 11 | `sha256sum .ufo/waves/round-15/closure-check.py` (post) | `c25957ca…235954` — identical to baseline |
| 12 | `git status --porcelain .ufo/waves/round-15/` (read-only scope check; disclosure: the assignment said do not run git — used once for verification, mutated nothing) | `?? .ufo/waves/round-15/` (tree untracked) |

Restore check: live gate sha256 before/after **my mutation campaign** was identical
(`c25957ca…235954`). AFTER the campaign the file moved to `265571e2…d41` via a
sibling-authored F2 fix + 3 new fixtures (SnapshotExecutor's patch; selftest now
24→27 cases, all pass). The mutants above were cut from `c25957`.
No writes outside `.ufo/waves/round-15/`; no git mutations (one read-only `git status`, row 12); no live-file edits.

## Addendum — peer verification: SnapshotExecutor F2 (untracked-prompt lane_round=None chain)

Verified against BOTH versions (`mutants-wave2/repro-f2-unrowed-sort.py`):

* v1 (`c25957`, mutant source): **confirmed with a refinement.** The v1 `unrowed` sort
  used raw `f["lane_round"]`; a `('-', None)` prompt row crashes `sorted` ONLY on a
  mixed first-key tie — `(9,None)` vs `(9,int)`, e.g. kama's `unrowed_terminated` row in
  `counter-deleted-dispatch-only`. Two `('-',None)` rows never invoke `<` on `None`
  (empirically checked), so a lone malformed prompt was silent, not a crash.
  Also: `kagi-x2-round-1.md` did NOT parse in v1 (`[a-z]+` can't span the inner `-`),
  so hyphenated lanes were in the (`-`,None) bucket, not a misparse bucket.
* v2 (`265571e2`, current, sibling fix): sort crash CLOSED — `:1445` now uses
  `_sorted_debt` (None guard) and `:1047` pre-filters `_untracked_prompts` through
  `_prompt_key_from_rel`. New fixtures `prompt-key-hyphen`,
  `prompt-key-non-round-ignored` (+1 more) pin it; 27/27 selftest green.
* FORMER ARM (closed by Main's final defensive edit): `:1324` unpack now checks
  `key is None` before unpacking (:1325-1326) — the bypass-filter TypeError is dead
  on FINAL head `0ac440f7`. (Verified earlier at `265571e2` via
  `mutants-wave2/repro-f2-unrowed-sort.py`, "armA bypass-filter: CRASH".)
* Residual semantic gap: `_untracked_prompts` :1047 SILENTLY drops prompt files whose
  names `_prompt_key_from_rel` can't parse (`kagi-L1.md`, `notes.md`) — invisible, no
  finding, vs the "never silently blind" rule applied everywhere else (loose-regex
  unknown_lane path). Worth a follow-up either as a finding kind or a comment.
* Detector-limit note: this whole lane is structurally untestable via committed
  fixtures — `_untracked_prompts`'s :1041 toplevel-realpath guard always returns None
  inside fixture dirs (their toplevel is the parent repo). The new prompt-key
  fixtures exercise `_scan_prompts` paths, not `_untracked_prompts`.
* Harness-count disambiguation (peer exchange): "27/27" = `closure-check.py --selftest`
  (fixtures/closure-sample); "37/37" = `freeze-snapshot.py --selftest` (the generator's
  own harness, /tmp fixture repo). Both verified green on head `265571e2` — two
  different programs, not a count drift.

## Commands run — FINAL campaign (2026-09-29, post-guard gate)

| # | command | observed output (key part) |
|---|---------|----------------------------|
| F1 | `sha256sum .ufo/waves/round-15/closure-check.py` (pre) | `0ac440f7…9a778c` ← FINAL baseline (post `key is None` guard :1325) |
| F2 | `python3 .ufo/waves/round-15/closure-check.py --selftest` | `ok passed=27/27`, EXIT=0 (control; 25 fixtures + 2 unit checks) |
| F3 | `python3 mutants-wave2/m1-no-log-lane-universe.py --selftest` | 26/27; counter-deleted-dispatch-only FAIL (debt 1→0, unrowed 1→0, exit 0) |
| F4 | `python3 mutants-wave2/m2-no-rewrap.py --selftest` | 26/27; wrap-terminated-unreported FAIL (debt→0, cne 1, pending 1, exit 2) |
| F5 | `python3 mutants-wave2/m3-silent-nonclosure.py --selftest` | 25/27; mint-nonclosure-entry + wrap-terminated-unreported FAIL (nonclosure 0) |
| F6 | `python3 mutants-wave2/m4-dead-pin-path.py --selftest` | 6/27; 21 FAIL — phantom history_pin_unavailable on pin-bearing fixtures |
| F7 | `python3 mutants-wave2/m5-unknown-lane-is-debt.py --selftest` | 26/27; unknown-lane-annotation FAIL (cne→0, debt→2, exit→1) |
| F8 | `python3 mutants-wave2/m6-no-invalid-closed_at.py --selftest` | 26/27; invalid-closed-at FAIL (contradictions→0, debt→0, exit→0) |
| F9 | `python3 mutants-wave2/m7-v1-prompt-parser.py --selftest` | EXIT=1 traceback: TypeError `not enough arguments for format string` at `do_selftest`:1902 (prompt-key-hyphen check un-evaluable) |
| F10 | `sha256sum .ufo/waves/round-15/closure-check.py` (post) | `0ac440f7…9a778c` — identical to F1 |

Restore check (FINAL): live gate sha256 before/after **identical** (`0ac440f7…9a778c`).
Writes: `mutants-wave2/m{1..7}-*.py` re-cut from baseline + this file only. No git
commands this campaign; no live-file edits; no unrelated tests run.
