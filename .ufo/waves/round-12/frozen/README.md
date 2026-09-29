# frozen/ — pinned closure baselines for the round-12 pass

`closure-check.py --frozen <NAME>` re-runs the gate against the static inputs in `frozen/<NAME>/`
and diffs the analyzed debt set against that directory's `expected.json`. The pinned unit is the
debt set as `(lane, lane_round, class)` triples (order-stable); the checker's evidence prose and
each row's `source` are printed beside the baseline and are *not* part of the match. Exit 3 when
the snapshot or its `expected.json` is absent.

    python3 .ufo/waves/round-12/closure-check.py --frozen pre          # exit 1, baseline: match
    python3 .ufo/waves/round-12/closure-check.py --frozen post-actual  # exit 1, baseline: match
    python3 .ufo/waves/round-12/closure-check.py --frozen post         # exit 0, baseline: match

| dir | `closed_at` | MANIFEST.json | expected |
|---|---|---|---|
| `pre/` | 20:55:00 | the pre-pass 22-entry blob, `git show 3ea42cb:MANIFEST.json` | exit 1 — the 5 debt rows the pass owed (protocol r11, kumitate r11, kotoba r12, aggregator r7, kasegi r14), each row's `source` naming `scout-closure.md`/`reviewer.md` |
| `post-actual/` | 21:20:00 | the pass's actual bytes (30 entries) | exit 1 — the 4 `stale_in_flight` rows still open at that instant |
| `post/` | 21:20:00 | `pre` + `patch-entries.json` (`appended` + `owed_appended`), 34 entries | exit 0 — the pass's target end state; `--frozen post` green means the ledger closes once the 4 corrections land |

## One freezing rule (all three dirs; `CLOSED_AT.txt` records the numbers)

For instant `C = closed_at`:

- `watchdog.log` — only lines whose leading ISO timestamp is `<= C`.
- `reports-index.txt` — `.ufo/reports/round-*/*.md` present at `C`: a tracked file whose *add-commit*
  committer time is `<= C`, or an untracked file whose mtime is `<= C`. Line format
  `rel<TAB>bytes<TAB>tracked<TAB>has_hash<TAB>has_shonen<TAB>landed_at`, where `landed_at` is that
  add-commit time (`-` when untracked). **`landed_at` is the termination-evidence timestamp**: a
  report whose commitment postdates `C` never counts as termination evidence for that snapshot, so
  post-window landings cannot leak in.
- `prompts-index.txt` — `.ufo/prompts/<lane>-round-N.md` present at `C` (same add-commit/mtime rule).
- `state-counters.txt` — the highest `launch`/`steer` round per lane among the kept log lines (the
  counter files are driver-written and can be mid-write; the kept log is the durable source).
- `patch-entries.json` — `appended` = `post-actual`.rounds[22:] (what the pass actually wrote);
  `owed_appended` = the 4 checker-derived corrections that `post` adds. `post` = `pre` + both.

## Invariance

`post`'s expected exit 0 is a claim: any silent narrowing of the pass (a dropped correction,
a `lane_rounds` re-key, a missing `supersedes`) breaks it, and any later hand-edit of the live
`rounds[]` shows up as live debt. The live 21:30 correction pass appended the same four corrections
(`rounds[30]` aggregator r8, `[32]` kengaku r11, `[33]` kumitate r12, `[34]` kotoba r13), which is why
the live verdict is green as well. `post-actual`'s expected exit 1 is the opposite claim — the
pass's own bytes did **not** close those four rows, and each rests on evidence inside its instant
(`complete` lines 21:14:05 / 21:14:11 and add-commits 21:11:33 / 21:13:01 / 21:15:59 / 21:18:11,
all `<= 21:20:00`); `unlanded` files (e.g. `round-12/kagi.md`, untracked) are excluded by the
`landed_at` rule above.

## Re-deriving a snapshot (read-only; ran in this round)

The generator is the round-12 protocol report's §Frozen baselines block; the decisive parts are

    git show 3ea42cb:MANIFEST.json > frozen/pre/MANIFEST.json          # pre
    cp MANIFEST.json frozen/post-actual/MANIFEST.json                 # post-actual (pass bytes)
    python3 -c "import json;a=json.load(open('frozen/post-actual/MANIFEST.json'));p=json.load(open('frozen/patch-entries.json'));a['rounds']+=p['owed_appended'];json.dump(a,open('frozen/post/MANIFEST.json','w'),indent=1)"
    git log -1 --diff-filter=A --format=%cI -- <report>               # the landed_at column

then re-apply the timestamp rule above to `watchdog.log`, the two indexes and the counters.