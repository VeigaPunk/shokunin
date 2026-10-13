# DedupeSimplifier — YAGNI/dedupe pass over the 16-row checklist (round-15)

Lane: kagi-shokunin (`/home/vgpnk/projects/shokunin/kagi-shokunin`).
Reviewed: the SHIPPED `corpus/checklist.tsv` + `corpus/checklist-run.sh` as of
now (`git status`: gate + tsv untracked, `corpus/knowledge/checklist-execution.md`
untracked, PROVINCE/SKILL/census-tsv modified on top of `round-14` HEAD
`2486643`). Ash-heap note: head-state snapshots lab-tested mid-review, and
`bash corpus/checklist-run.sh --selftest` ⇒ `CHECKLIST_SELFTEST: PASS (28
cases)` exit 0 (my run), while the default verify run currently fails.
I did not edit repo files.

# The decision rule I used

For each proposed row: (a) **DELETE** — the item is already *fully governed by
an existing gate* (the existing gate exits 1/2 on exactly the same defect
class); (b) **DELEGATE** — the row is right, but only if its check *calls the
existing gate* and does not re-implement the assertion inline; (c) **DIRECT** —
the assertion is new and must be written. A row that re-derives an existing
gate's summary from host facts is a *second copy* only when the re-derivation
would carry the same exit-code information; a row that carries a *different
verdict family* (value-level contract vs byte-level drift) is not a duplicate.

# Existing gates and what each one already covers

| gate | what it asserts (proof, inline) |
|---|---|
| `corpus/surface-census.sh` (`--verbs`/`--verbs --deep`/`--selftest`) | kind/exact-mode per declared path, `UNLISTED` children of the 4 enumerable dirs (round-6 leak class), runtime shape pins, and the **10 write-side verb probes** (`--verbs` ⇒ `CLEAN (pass=7 skip=3)` exit 0, ≤25 s, no `op` exec; `--verbs --deep` ⇒ `CLEAN (pass=10 skip=0)`) — per surface-census knowledge entry §"what the gate covers" (`corpus/knowledge/surface-census.md`) and `PROVINCE.md:34-37` |
| `corpus/drift-pins.sh` + baselines | mode+lines+sha256 per pinned host file (15 rows), per-symbol claims (~20 rows) against `corpus/drift-baseline.tsv` / `drift-symbols.tsv`; verdicts `OK/DRIFT/MISSING/LINK/UNPINNED/EXTRA/DUP/POLICY(MODE)/POLICY(SHA)/SHAPE`; `--selftest 13 cases`; per L1's round-13 scratch `HostScout.md` and PROVINCE:38 |
| `corpus/transcript-scan.sh` (`--classify`, `--selftest`) | snapshot-scans opencode-db keys 888 × 32+5 leak patterns + 5 credential-table tripwires; HITS=2 baseline pinned in `corpus/op-ref-probe.tsv` as a claim row; ⇒ `CLEAN (HITS=2)` exit 0 today — per PROVINCE:39 and L1's round-15 host-scout scratch |
| `corpus/op-ref-probe.sh` (`--evaluate`/`--fixture`/`--selftest`) | 5 env-file fixtures ⇒ `OP_REF_PROBE: CLEAN (checks=N oprun=12 refs=7 divergent=5 edge=10 sig=6)`; POLICY REFUSE on op://-shaped fixture paths, `--evaluate` mode does NOT exec `op` — per PROVINCE:40 and the fixture list at `corpus/knowledge/op-env-refs.md` |
| `corpus/claim-ledger.sh` (modes `verify`/`cells`/`docs`/`citations`/`stamp`) | 44 revision stamps + 18 claim rows + per-doc `Reverify:` declarations; ⇒ `CLAIM_LEDGER: CLEAN (claims=18 stamped=44 ids=18 cited=18 labeled_ids=17 orphans=0)` exit 0 (my run) |
| new: `corpus/checklist-run.sh` (`verify`/`--list`/`--only`/`--selftest`) | checks the 16-item SKILL.md checklist from `corpus/checklist.tsv`, lead-phrase bijection, DUPLICATE-QA + accept-cookie enforcement; ≥ 8-runnable floor ⇒ `CHECKLIST_RATIO` + `CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7 failed=0)` — currently NOT green from my live run (see E4 below) |

# Head-state line ranges (measured)

- SKILL.md checklist items: 431-438 (Evidence production), 441-453 (Handler
  operation), 16 items total.
- SCORECARD.md: head-cell block (4th table) boundary rows at 176-187.

# Per-row verdicts

## Evidence-production rows (E1…E8)

| id | item (SKILL.md:LN) | verdict | reason + existing-gate evidence |
|---|---|---|---|
| E1 | 431 "Record mechanism and metadata … **`bash corpus/surface-census.sh` first** … then `drift-pins.sh`" | **DELETE** | the item is already fully governed by its own named gates; the row re-runs an EXISTING gate ($2 copy) and adds only a second copy of the same exit codes — surface-census and drift-pins already are gates; the round-15 add must not blanket-remount the pair |
| E2 | 432 "After any intentional host-file change run `--pin` once" | **DELEGATE** | the duty belongs to drift-pins' own `REPIN` verification, not to a new check; the roadmap already names the repin-acceptance loop (`corpus/knowledge/claim-ledger.md` §"stamps/rows" while `REPIN`/`MOVED` are drift-pins' own output symbols seen in `drift-pins.sh` L240-260); a deep verifier would add nothing the gate does not already do |
| E3 | 433 "Quote command output only when it is metadata-only" | **DIRECT** (shallow) | no existing gate checks any checkout of the "counting this statement" class — `grep -c 'command output' corpus/*.md` ⇒ 0 (I ran; exit 1) — but a *deleted* check over the same subtree would only chase the same info `CLAIM_LEDGER docs` re-verifies from its own stamp set; keep, but scope-limit it to the item's named `cdp-bridge`/`tac-check`/`status` transaction names still existing (name-membership). As shipped the row does none of that: it carries `mode=600, predicate ok` on an unstated hand-classified baseline — that's an over-claim, and I recommend re-deriving it or dropping it to by-hand with the 24-char reason |
| E4 | 434 "ref paths stay out of artifacts" | **DIRECT** but row currently RED | `grep -cE 'op://' corpus/**/*.md` itself counts 6 files (SKILL.md + 5 knowledge + 0 non-doc), so an `op://`-absence assertion is DIRECT — no gate currently asserts it (the PDFs/notes listed above are the *first* artifacts whose ref-class burden the checklist row covers, and PROVINCE.md's §Refusals records the *behaviour* gate refusal but not the corpus's own doc contents). **However the shipped check currently fails my live run:** `bash corpus/checklist-run.sh` ⇒ `ITEM-FAIL E4 (exit 1 want 0)` + `REF_PATH_SCAN: hits=3`, the 3 hits being `op://vault/item/field` lines inside `corpus/knowledge/op-env-refs.md:14`, `corpus/lessons/round-5-aggregator-audit.md:19`, and `corpus/transcript-scan.sh:202` (test fixture #202 — the same `wal/resident` fixture class the FakeVault exemption covers at 2 line-sites). The 3 hits use the bare-`vault/item/field` placeholder form *outside* the exempted line sites. Either exempt the quoted/backticked form (naming the exclusion) or pin `hits=3` as a declared baseline like H7 does. |
| E5 | 435 "Before relying on a key inventory, run `bash corpus/op-ref-probe.sh`" | **DELEGATE** | the item literally names the gate; the row `bash corpus/op-ref-probe.sh` is exactly the correct delegate |
| E6 | 436 "Never paste `the-janitor run` output" | **DELEGATE to op-ref-probe's masking pins — not a new check** | the alternate is a new check that would re-derive op-ref-probe's 6 (drift) masking assertions; the existing gate pins the *deny* class. This round's add adds a pointer, not a count; cheaper as a knowledge note under E4's ERE |
| E7 | 437 "Receipts/checksums bind bytes" | **DELETE** | already an executed byte-check: `corpus/knowledge/tac-evidence-integrity.md` + `tac-check` (offline receipt check run each round, PROVINCE.md lists it under "command surface"), and round-10's claim-ledger shipped per-row byte-verification for every stamp — a checklist row would be a third copy of `tac-check`'s own verdict |
| E8 | 438 "Handoffs carry context + receipt *path*" | **DELEGATE (part) + DIRECT (part)** | the *only* part not already machine-checked is the `boundaries`/`access_receipt`/`receipt_sha256` key set in `handoff-status.json`; the receipt *file bytes* and `tac-check` verdict are already agenda items of the existing lifecycle rows. The shipped H-status check is the correct minimal direct check |

## Handler-operation rows (H1…H8)

| id | item (SKILL.md:LN) | verdict | reason + existing-gate evidence |
|---|---|---|---|
| H1 | 441 "One request at a time — `client.lock` flock" | **DELETE the grep, keep a mode-only assert (or roll back to I)** | the item is about serialization *premises*: `surface-census.tsv` row $(SEE F1 CORRECTION BELOW) `client.lock` (mode 600, runtime) and the CLI exec are already pinned by the census. The `flock 9`/`LOCK_FILE=` grep itself I could NOT find in any TSV (`grep -n 'flock 9\|LOCK_FILE=' corpus/drift-symbols.tsv` ⇒ exit 1, no rows); what DOES cover the premise is the corpus's own stamped doc: `corpus/knowledge/handler-trust-boundary.md:263` carries the literal command `grep -n 'flock 9' ~/.local/bin/the-janitor # 3 sites: L131, L140, L176`, it is byte-stamped in `corpus/stamps.tsv:13` (sha256 `263c7b0e…`, 285 lines) which `CLAIM_LEDGER verify` enforces. My live count today: `grep -c 'flock 9' ~/.local/bin/the-janitor` ⇒ **3** ⇒ the *factual* handoff already holds in a stamped, re-run-by-`claim-ledger` claim. Adding a checklist row that re-derives that count is then a second copy with the *weaker* pin (a checklist-row grep re-runs unreferenced, the ledger row enforces the full stamp cycle). So the honest choice for H1: keep it by-hand, and add, when L1 lands the round-15 `checklist-execution.md` doc, one line citing handler-trust-boundary's own Reverify declaration (which is already the ledger's declared source for this assertion). |
| H2 | 442 "After `stop`, expect `AUTH_REQUIRED`" | **by-hand always** — no verdict | requires a handler stop→request cycle; the round-15 lane cannot legally start/stop the opencode handler (PROVINCE.md §Refusals). Nothing in the TSV can express this row's premise; keep by-hand |
| H3 | 443 "Keep `config_overlay` intact (providers/share/autoupdate/global)" | **DELEGATE (part) + DIRECT (part)** | drift-symbols.tsv pins `"share": "disabled"` and `"enabled_providers"` *and* `MODEL_ENDPOINT` line-shape, so `drift-pins` already covers the config overlay's 3 symbol pins as a byte-level class; but the *value-tuple semantics* (providers==["qwen-local"], autoupdate False, janitor default_agent) are a *value assertion*, NOT a byte/mode assertion — this is a new class, keep it direct but **fail-closed on the `global opencode.json` files' mode only (census already covers exact mode)**; the round must NOT double-count this as a *new* coverage claim for drift |
| H4 | 444 "Never widen `janitor` agent permissions" | **DELEGATE (part) + DIRECT (part)** | drift-symbols pins `janitor.md` (`^pn-...$` and `^steps: 4`) as symbol-level, and drift-baseline pins the file's sha256; the *value-class* of the two front-matter entries is a new assertion (drift-pins cannot express "exactly two permission entries of exact form") — keep this direct |
| H5 | 445 "CDP 9222 + musketeer profile shared with kake" | **by-hand always** — cross-lane, cannot be a local command verdict | `surface-census.tsv` rows for the chrome-profile NMH manifest enforce only *presence + mode*; the item asks for a *lease/adjudication* verdict, which is by-construction outside kagi's corpus. Keep by-hand |
| H6 | 446-448 "Never put secret-adjacent text into a request" | **by-hand** (no honest baseline) | the only mechanical check would have to read the secret-adjacent text itself; surface-census/trn-scan are already the fix — no honest new row; keep by-hand |
| H7 | 449-452 "Run `corpus/transcript-scan.sh` after credential-shaped requests" | **DELEGATE** | the row literally calls the existing gate; correct |
| H8 | 453-455 "Treat `127.0.0.1:40961` as unauthenticated handler access" | **DELEGATE (port) + DIRECT (refusal-of-password-ref)** | census pins `$HOME/.local/state/the-janitor/...` (nothing on port 40961). The `password_refs` class is a new assertion (no gate counts that literal); the shipped port-`ss` assertion is, per this grep, a new check — but it MUST NOT be sold as a "new host-stray check" since ports 40961's *listener absence* is exactly what the round-12/13 `handler-on-disk-state.md` §"Absence assertions" already claims in prose (the *prose* is not a verdict). Keep as DIRECT with a note that the delta versus prose is the verdict, not the fact |

# The minimal honest row set

Given the verdicts above, the honest minimal set is the 16-row TSV
**minus the horns it currently grows**:

1. Row **E1 is the double-count winner** — delete the row; the
   surface-census + drift-pins gates already exit non-zero on the same
   defect class, and the item is already named inside SKILL.md's own
   instruction text. Cost: 0 line-checks; Benefit: an entire honest
   "runnable=10" that the next read cannot claim twice (see the
   double-counting sweep below).
2. Row **E7 delete** (a third copy of `tac-check`'s own bytes-check).
3. Row **H1: fold to by-hand** (keep a mode-only assert inside the E1 census
   row only if census still owns it) — a checklist grep would be a weaker
   second copy of the stamped handler-trust-boundary claim (full reasoning
   in the table above).
4. Row **E4 stays, but must count the three `op://vault/item/field`
   placeholder hits as their own named class** (the current allowlist's
   honest gap) — else the TSV row says CLEAN while the working tree holds
   3 documented placeholder hits (`op://vault/item/field` in two notes +
   the transcript `--selftest` fixture string), and the gate contradicts
   its own round-10 lesson line. Two honest shapes: (a) exempt the
   backtick/single-quoted literal, so `hits=0` stays green with a *named*
   exclusion, or (b) pin the declared baseline `hits=3` in the TSV row's
   `expect_last` line (like H7 pins `HITS=2`), turning the three hits from
   a broken compile into a pinned, named baseline. Both have teeth; (b) is
   simpler. The verdict line must then distinguish
   *hits == declared-baseline but changed item* (`ITEM-DRIFT`) from
   *unknown new item* (`ITEM-FAIL`) — the gate already has that pair.
5. Rows E8, H3, H4, H8 are the only rows that carry non-redundant verdict
   classes (value-tuple + string-count): those are the row set that can
   honestly move operability's axis NOT covered by any existing gate
   (`surface-census`, `drift-pins`, `transcript-scan`, `op-ref-probe`,
   `claim-ledger`).

So **runnable = 9 − 3 double-counts = 6**: E4, E8, H3, H4, H7 (delegate
row, correct as-is), H8, plus E5 (the literal-delegate). Recounting:
E4(fix), E5, E7(del), E8, H1(to-by-hand), H3, H4, H7, H8. With E1, E7
deleted and H1 folded, runnable = **6** and by_hand = **10** (16 total, the
shipped floor=8 must then be **re-derived** — the 8-runnable floor came
from the original 16-row assumption, not a constant; if L1 wants a floor
after the cleanup it must come with a *named reason*, e.g. "E4's
declared-baseline pins + the two delegate rows + the four DIRECT
value-tuple rows re-assert the corpus's own factual handoff, floor 6"? —
the ratio line is the gate's teeth; it must never print a number the
*table* doesn't carry).

# Double-counting sweep vs SCORECARD.md

I searched `grep -n 'operability\|checklist' SCORECARD.md`:

- The ONLY operability cells that name a checklist status are:
  - round 9 (L18/L28): "checklist item 1 is now a runnable command rather
    than a print-out. Remaining manual: **12 of the checklist items are
    still operator judgement, not commands**." — this is a claim about a
    *one-item* effect.
  - round 10 (L62, L84): "…12 checklist items still operator judgement."
  - round 11 (L74): "the checklist's 12 judgement items … the increment
    is claimed under calibration, not double-counted here."
  - round 13 head-cell (L177): "Five modes with verdicts + selftests …
    the checklist's judgement items remain judgement."
  - round 14 (L187): "checklist still holds judgement items" (freshness
    ceiling table, column header context).
- There is **no cell that claims a checklist-widening increment beyond
  range (0-1)** — the operability axis's 8 has been held because it counts
  *gate verdicts*, never *checklist rows*. So round-15's add of
  "one check per item" is a new claim; if it IS claimed under operability,
  **the round must not ALSO claim the same check-increment under
  coverage/freshness/calibration** — the shipped design's
  `CHECKLIST_RATIO` line is operability's own verdict; scorecell-wise keep
  the other axes untouched.

**Crucial boundary already forsworn by the scorecard itself:** SCORECARD.md
L162-164 (and re-stated in the "Planned" block at L220-222) says the
remaining operability move "needs a **scheduling** decision that touches
host state (systemd/cron), i.e. **operator scope**, so it is **not a
lane-only move**". Round-15's axis move (8→9) therefore cannot ride on
*scheduling*, and the shipped design rightly doesn't claim scheduling. It
must, however, name (in its own new cell) **why the increment is
scheduling-free**: the gate is a *lane-local* verdict-runner, and the
checklist items' *executor* is still the round's L1 (no cron). The honest
wording is "the checklist items now **execute and return verdicts when the
lane decides to run them**", not "the checklist is scheduled".

**Second double-count risk: the "12 remaining" figure.** The operability
round-9 cell states "Remaining manual: 12 of the checklist items are still
operator judgement, not commands." If round-15 ships `runnable=9
by_hand=7`, the round-9 number must not silently become "6 remaining" in
the new cell without visibly re-deriving the delta — the shipped ratio
line already puts this in-machinery (`CHECKLIST_RATIO: runnable=9/16
floor=8 by_hand=7`), which is the right shape: cite the ratio line, not a
naked digit derived by subtraction. The honest textual claim is "7 by-hand
+ 9 runnable, measured, ratio line at reproducible id".

# What my two live runs proved (repro block)

```
$ bash corpus/checklist-run.sh --selftest
CHECKLIST_SELFTEST: PASS (28 cases)                       # exit 0
$ bash corpus/checklist-run.sh                            # default verify, live tree
ITEM-FAIL E4 (exit 1 want 0)
    | REF_PATH_SCAN: hits=3
CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7
CHECKLIST_RUN: BROKEN (items=16 runnable=9 by_hand=7 failed=1)   # exit 1
```

Hit list (repro):
```
$ grep -RInE 'op://[A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]+' . \
    --include='*.md' --include='*.tsv' --include='*.sh' --exclude-dir=.git \
  | grep -vE 'op://(FakeVault|wal)/'
./corpus/knowledge/op-env-refs.md:14:         op://vault/item/field …
./corpus/lessons/round-5-aggregator-audit.md:19:  op://vault/item/field …
./corpus/transcript-scan.sh:202:      fake op://vault/item/field marker
```

# Recommended hand-off to L1 (order matters)

1. **Fix E4's allowlist first** (the lane cannot ship a
   `CHECKLIST_RUN: CLEAN` that fails its own run). The correct class is
   the round-10 lesson's own wording: the *three* `op://vault/item/field`
   literals are *quoted placeholder* lines the ledger already treats as
   non-refusage; L1 should either (a) exempt the quoted form
   `` `op://vault/item/field` `` (backtick-delimited) and
   `"fake op://vault/item/field marker"` (a single-quoted fixture string),
   or (b) exempt the bare-vault class everywhere except inside
   backticks/single-quotes. Do NOT widen the exemption to all bare-vault
   forms — that would let a real `op://vault/...` real path slip.
2. **Apply the deletions** in the order (E1 → E7 → H1-to-by-hand): each
   deletion step reduces the runnable count by 1, so shipping E4's fix +
   the three deletions in one commit re-derives
   `runnable=6 by_hand=10` and the ratio floor *must* be re-derived then.
   One commit, one rerun, print *both* before and after `CHECKLIST_RATIO`.
3. **Keep E5 and H7 as row-level delegates** — they are already DM-shaped
   (`bash <gate>` as their whole check) and cost nothing.
4. **Keep E2/E3/E6/E8/H3/H4/H5/H6/H8 as-shipped semantics** (some
   by-hand, some direct) — those carry non-redundant verdict families.
5. **Scorecard**: when L1 writes the round-15 operability cell, it must
   claim the *ratio-line* increment only, note the deleted double-count
   rows (E1/E7/H1) by name (so the next audit cannot accuse the round of
   shrink-to-fit), and leave the scheduling ceiling (SCORECARD L162-164)
   textually untouched.

# Anti-overfitting check

**Would this row set still be worthwhile if the exact task (round-15
checklist-executability) disappeared?** Yes for E4/E8/H3/H4/H8: they
express value-level contracts (`op.env` allowlist semantics,
`handoff-status.json` lifecycle fields, `opencode.json`'s provider map,
`janitor.md`'s permission ceiling, the 40961 port-hygiene count) that no
existing gate encodes and that the next lane of this round would need as
machine-checkable facts regardless. No for E1/E7/H1-in-shipped-form:
they exist only as second copies of exits the round-10 and round-11 gates
already own.
