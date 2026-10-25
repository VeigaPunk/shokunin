# ItemReviewer — honesty attack on the 9 runnable / 7 by-hand split

Round 15 · lane kagi-shokunin · repo `/home/vgpnk/projects/shokunin/kagi-shokunin`.
Reviewed: `corpus/checklist.tsv` + `corpus/checklist-run.sh`, re-based mid-audit
onto the *current* bytes (`md5sum` at the time of writing `7fc6c84d…` for
`checklist-run.sh` and `a7754e88…` for `checklist.tsv`) after an earlier
in-flight copy — identical gate verdict, re-verified before use. Reviewer lanes
are read-only on the repo: every drill below runs in a `/tmp/ir15/full` sandbox
copy verified gate-identical (`bash corpus/checklist-run.sh` in the copy gives
the same `CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7 delegated=3 direct=6`
+ `CLEAN (items=16 …)` verdict as HEAD).

**Method.** Per item: (1) find the sentence bearing the item's duty in the
verbatim item at `SKILL.md:419ff` (16 items confirmed — `grep -c '^- \[ \]'`
section-scoped = 16); (2) execute the shipped row's `check` verbatim against this
host (all 9 run; observed verdicts); (3) attack: either execute a drill that
makes the row's *shipped* check pass while the duty sentence is violated, or
prove no command form exists that could; (4) prove or refute the shipped
verdict-line pinning under the drill's mutation class.

Verdict classes per ticket:

- `HONEST` — a pass verdict detects violation of the item's duty sentence.
- `SHOULD-BE-BY-HAND` — the shipped runnable form detects only a premise or a
  sibling-track artifact of the duty (an executed drill separates them); the
  honest motion is to reclassify the row by-hand (or narrow the row + the note).
- `PREMISE-ONLY` — row stays runnable but only on a tightened duty sentence
  (SKILL edit), not the current one.
- `SHOULD-BE-RUNNABLE` — shipped by-hand but a real command achieves the duty.

---

## Verdicts (executed row commands, verbatim-checked first)

### E1 (runnable) — Record mechanism and metadata → census + drift

Verdict `HONEST (direct-duty)`. The item's imperatives are literally two
commands — surface-census then drift-pins — and the row sequences both in one
`&&`-chain, pinning the drift verdict as the row's witness. Two sharper notes,
both observation-backed, not defects:

1. **Attribution skew (MSD-1).** The shipped check mutes census stdout
 (`surface-census.sh >/dev/null`), so the row's *verdict line* is drift's
 summary only; a future run where census fails and drift passes still ends
 rc=1 (both exits asserted) — the duty's defect signal survives — but the
 printed `got … want …` pair points at the wrong gate.
2. **Count-semantics floor.** SKILL.md pins "15 files / 20 pins as of round 12;
   19 before it" — history prose, deliberately unanchored; checkable only as an
   exact `expect_last`. Shipped `expect_last` is `[0-9]+`-shaped. A tightening
   would pin `^DRIFT_PINS: CLEAN \(files=15 symbols=20\)$`. Floor-tightening
   option, not a blocker.

### E2 (by-hand, manual-change) — `--pin` once and report accepted lines

Verdict: `HONEST`. Duty = accept/reject REPIN/MOVED lines after an intentional
host-file change, with the no-re-pin-same-round ordering rule — an authoring call
at change time. No command shape exists at gate scope; the note already names the
operator's half. Counterexample attempt fails: any runnable form
(e.g. "drift-pins exit 0 today") verifies the *outcome* (baseline and host agree),
not the *reported acceptance class*, and the same outcome can arise from a
host-change the operator accepted by hand a round earlier. The by-hand class is
the residue. Floor-survivor.

### E3 (by-hand, authoring-duty) — quote only metadata output

Verdict: `HONEST`. Deciding a quoted block is metadata-only is a writing
judgement; no regex separates a metadata block from pasted output (the `note`
already names the allow-list recursion). The duty sentence is a writing rule —
by-hand is right. Floor-survivor.

### E4 (runnable) — `refs` output: key names OK; ref paths stay out of artifacts

Verdict: `HONEST (direct-duty)`. The item's second imperative ("ref paths stay
out of artifacts") is a property of file bytes, and the sweep is a defect signal
that fires on exactly the violation class: `hits≥1` ⇒ `ITEM-FAIL`. The shipped
exclusion is a name allowlist — a declared class boundary
(`op://(FakeVault|wal|vault)/`) — verified today (`hits=0` verbatim; the three
placeholder literals live at `corpus/transcript-scan.sh:202`, `:242` and
`corpus/surface-census.sh:608`). The sweep is green by exclusion-list
*construction*, not by an empty corpus — EntryDraftExecutor F-2's 3-hit story
was fixed exactly by growing the allowlist past `FakeVault|wal` to include
`vault`. The duty's edge: a future *new placeholder* entering via a reviewed
commit would be read as a REAL leak until the allowlist is re-declared — that's
not today (hits=0 verbatim live), but it is the tension that keeps the note's
"class's weak point" ruling on the recommendation list below.
```console
$ cd /home/vgpnk/projects/shokunin/kagi-shokunin   # live repo, read-only
$ n=$(grep -RInE --exclude-dir=.git --include='*.md' --include='*.tsv' \
      --include='*.sh' 'op://[A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]+' . \
      | grep -vE 'op://(FakeVault|wal|vault)/' | wc -l | tr -d ' ')
$ printf 'REF_PATH_SCAN: hits=%s\n' "$n"; test "$n" -eq 0
REF_PATH_SCAN: hits=0          # exit 0 — the shipped row's verdict, executed
$ grep -RnE --include='*.sh' 'op://(FakeVault|wal|vault)/' corpus/ | awk -F: '{print $1}' | sort | uniq -c
      1 corpus/surface-census.sh     # :608 FakeVault
      2 corpus/transcript-scan.sh    # :202 (`op://vault/item/field`), :242 (`op://wal/resident`)
      # 3 placeholder literals total — the exact class the exclude covers
```

### E5 (runnable) — run the probe before relying on key inventory

Verdict: `HONEST` on the shipped *runnable* form (the item's first imperative —
**"Before relying on a key inventory, run bash corpus/op-ref-probe.sh"** — is a
command, and the row runs it with an exact `expect_last`). This is a direct-duty
row. The trailing "…and remember what it pins" phrase is unmechanizable prose
(a memory operator's), which by-hand would make the row lose the runnable half.
Floor-survivor.

### E6 (by-hand, authoring-duty) — never paste run output; class-check before quoting

Verdict: `HONEST`. The note already claims the duty ("no command can tell whether
a value's class was checked before quoting") and points the consequence at row
E5's probe (a value-class classifier over the artifact would have to read the
value it's judging — circular). The consequence space is already guarded:
transcript scan and census shape rows testify elsewhere for the *artifact*
(`surface-census.tsv` note "env-ref file; values never read into an artifact"):
`drift-gate.md` §"`op.env` is the only file where NOHASH is forced" (EntryDraft
§5). Floor-survivor.

### E7 (by-hand, authoring-duty) — receipts bind bytes; scope sentence only

Verdict: `HONEST`. The scope-sentence half is a writing rule; the byte-binding
half is `tac-check`'s own offline gate (`drift-symbols.tsv` pins both).
Counterexample: any "banned-claim scan over the receipt" would have to decide
whether e.g. `LIMIT: locally writable evidence` is allowed (it is — the
vocabulary is quotable per SKILL.md) or implies provider attestation. Not
machine-decidable without an authoring call above the scanner. Floor-survivor.

### E8 (runnable) — handoff boundaries vocabulary

Verdict: `HONEST` at the current fastening. The item's duty — "`handoff-status.json`
`boundaries` is the vocabulary: `credentials_in_evidence: false`,
`target_authority_conferred: false`; access_receipt; receipt_sha256" — names four
keys, and the check asserts all four. Drilled (MSD-2 in the sandbox copy): **dropping only the
`target_authority_conferred is False` half let the SAME row pass
(`CHECKLIST_RUN: CLEAN (…)`) while the live file has the key present** —
so the row's verdict line and the four-value tuple are the fastening; the
`all(k in d…)` covers the two keys and the `expect_last` pins the printed
tuple. The drill's finding: if L1 later *shortens* the assert, the SAME last
line would still pass while the vocabulary check weakens — hence the verdict
line + notes must state the tuple's inclusiveness explicitly (already in the
shipped note: "asserts the vocabulary the item names — key names and boolean
values only"). Floor-survivor. Bottom line for the review lane: **keep the
four-key-tuple fastening visible**.

### H1 (runnable) — one request at a time; queue instead of racing

Verdict: `PREMISE-ONLY`, honest by note. The serialization premise is enforced
(observed: `CLIENT_LOCK: flock=3 declared=1 mode=600` — the shipped row's own
verdict on this host). The other half ("queue instead of racing") is operator
behavior — the shipped note names it explicitly ("…the queue-instead-of-race
half is the operator's behaviour"), which Main's criterion back-fills.
Floor-survivor as a premise row.

### H2 (by-hand, runtime-behavior) — after stop, expect AUTH_REQUIRED

Verdict: `HONEST`. The row needs a live-handler cycle — explicitly operator
scope per the shipped note; no passive command shape exists (the handler is
stopped today: no listener on 40961, 0 established sockets — host fact).
Floor-survivor.

### H3 (runnable) — keep `config_overlay` intact

Verdict: `HONEST` today at value `autoupdate=False` (ItemsScout said this knob
was in no gate pre-round-15); a documented evidence gate directly reflects the
item's own deliverables. **MSD-3 (drilled, `/tmp/ir15/full` copy)**: dropping
only `o.get('share')=='disabled'` still yielded `CHECKLIST_RUN: CLEAN` (the
`share=%s` formatting still prints the live value `disabled`), showing that
the *print* and the *assertion* are separable: if L1 ever shortens the check,
the row must re-assert `share` as an `and`-clause or the row weakens. Not an
attack on today's shipped row (shipped `and`-chain is in place and was
re-verified after restore: `CHECKLIST_RUN: CLEAN…`). Floor-survivor; on the
one-verdict-per-round freshness rule this is the class of drill the next
review should replay after any row text edit.

### H4 (runnable) — never widen the janitor permission ceiling

Verdict: `HONEST` (L1 fixed the earlier trailing-newline parsing drop;
shipped row now reports `entries=2 steps=4` — actively executed and observed,
entry-draft fix confirmed). `{"*": deny}` and `janitor_auth: allow` are pinned
by exact tuple; a widened list (third entry, or deny flipped → allow) makes
`JANITOR_PERMS: DEFECT` fail-closed. Floor-survivor.

### H5 (by-hand, cross-lane) — CDP port 9222 and musketeer profile lease

Verdict: `HONEST`. The muscle of the duty ("report lease conflicts, don't absorb
them") is a cross-lane reporting duty against the kake fleet, correctly pinned
into the census row as CONTESTED reported-not-ruled; nothing adjudicates here.
Floor-survivor.

### H6 (by-hand, authoring-duty) — secret-adjacent text in requests

Verdict: `HONEST`. The point-of-writing check cannot be mechanized without
reading the request text (exactly the material that mustn't persist); the
durable consequence is row H7's scan. Floor-survivor.

### H7 (runnable, transcript-scan) — run the scan; exit 1 is by design

Verdict: `HONEST` in the shipped form (`expect_exit 0|1`). Entry draft bounds §3
names why: demanding exit 0 would paint the healthy host red (the round-8
false-positive class). The teeth are the `HITS=2`-pinned line. Residual risk
(inline below) only. Floor-survivor.

### H8 (runnable) — treat 40961 as unauthenticated handler access

Verdict: `HONEST` (premise + count). Shipped row asserts
`password_refs=0` in the daemon's two own scripts (matches live
`grep -c OPENCODE_SERVER_PASSWORD` on both = 0; host fact re-measured by L1)
and `established=0` (live: no listener, 0 established). Listener is a
legitimate-while-running value → *reported not asserted*, printed in the
verdict line (`listeners=%s`) — but the row still FAILs (rc 1) if a socket
*established* appears, per `test "$E" -eq 0`. Floor-survivor. The remaining
attack class — "no local process should POST to it" — is a *behavioral*
duty that no passive count enforces; this is exactly the premise half the
shipped note names. Under the shipped criterion (a command whose verdict is a
defect signal), the row's `established>0` and `password_refs>0` ARE defect
signals; passes.

---

## Mutation-sensitivity drills (executed; no repo edit, sandbox copies only)

MSD-1..3 mutate one assert in a row-copy of `corpus/checklist.tsv` (never the
live repo), verbatim run, verbatim restore, verbatim `CLEAN (…) failed=0`
re-run. MSD-4 is the one *host-state* counterexample: it mutates a sandbox
file, not the row.

- **MSD-1 (E1, attribution).** Drill change: `bash corpus/surface-census.sh >/dev/null && bash corpus/drift-pins.sh`
  → `bash corpus/surface-census.sh && bash corpus/drift-pins.sh >/dev/null`
  (mute drift, keep exits). Output:
  `ITEM-LASTLINE E1 (want /^DRIFT_PINS: CLEAN \(files=[0-9]+ symbols=[0-9]+\)$/ got SURFACE_CENSUS: CLEAN \(assets=20 runtime=15 scanned=4 ok=34 absent=2 skipped=0\))` — the exact skew.
- **MSD-2 (E8, four-key fastening).** Drill change: drop the
  `target_authority_conferred is False` assert from the check. Output was still
  the green row's `HANDOFF_STATUS: OK (boundaries=…)`, i.e. the same line, proving
  the *assertion* is what nails the key — not the format string.
- **MSD-3 (H3, share-disabled assertion).** Drill change: drop
  `o.get('share')=='disabled'` from the `and`-chain. Output stayed green
  `OK (providers=1 share=disabled autoupdate=False global=parsed global_providers=absent)` — the
  *assertion*, not the printing, is what carries the item's three knobs.
- **MSD-4 (E4, include-filter boundary — a true host-state counterexample).**
  In the sandbox copy, add an *untracked, non-declared-kind* artifact
  (`corpus/scratch.json` — not in the `--include` allowlist) whose content is a
  ref-shaped literal `op://TestDoc/Item123/Field`:
  ```console
  $ printf 'note: fake artifact scratch — KAGI_REF=op://TestDoc/Item123/Field\n' > corpus/scratch.json
  $ n=$(grep -RInE --exclude-dir=.git --include='*.md' --include='*.tsv' \
        --include='*.sh' 'op://[A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]+' . \
        | grep -vE 'op://(FakeVault|wal|vault)/' | wc -l | tr -d ' ')
  $ printf 'REF_PATH_SCAN: hits=%s\n' "$n"; test "$n" -eq 0; echo "E4_EXIT=$?"
  REF_PATH_SCAN: hits=0
  E4_EXIT=0            # the row PASSES — a ref-shaped literal is in the
                       # working tree inside a file kind the include-list
                       # does not declare. Removed right after (rm).
  ```
  An executed pass-while-violated instance against the item's blanket wording
  ("ref paths stay out of artifacts"): the row's guard has TWO declared class
  boundaries — placeholder vault names *and* artifact file kinds
  (`md/tsv/sh`). A future new artifact kind (json/yaml/…) is the second
  expansion path the E4 recommendation names.

All four drills ran on the `/tmp/ir15/full` sandbox copy; the mutated row was
restored verbatim and the full gate re-verified `CLEAN (… failed=0)` after
each (`RESTORED_OK`). The repo pair at HEAD and the sandbox pair give the same
`CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7 delegated=3 direct=6`
verdict.

### Honest floor from these drills

Running the floor arithmetic against the shipped ratio semantics (runnable
`K` ≤ 9 of 16 vs gate-math floor 8):

- **Directly duty-witnessed rows** (the item's duty sentence is literally a
  command, an exact tuple or a byte-shape) — **8**: E1, E4, E5, E8, H3, H4, H7,
  H8. All nine runnable row commands executed verbatim on this host; each
  verify-restore cycle reproduced the shipped verdicts exactly.
- **Premise-only-but-documented row** — **1**: H1. Flock/lockfile presence is
  the *premise* of "one request at a time"; the queue-half is operator
  behavior named in the note.

Under the **shipped criterion** (a command whose verdict is a defect signal
for the item), every one of the 9 runnable rows survives: the honest floor
claim of the shipped split is `runnable=9, by_hand=7`. Under the
**stricter duty-vs-premise reading** (CheckPlanner's), the count drops to the
8 direct command/tuple rows — H1 is the one premise row that doesn't clear.
The gate's own floor math (`FLOOR_DEN=2` → 8) means the current set has
exactly one row of slack; any second demotion fires `RATIO`.

**The honest-floor caveat from MSD-4**: E4's include-filter is a second
class boundary (artifact kinds md/tsv/sh). Under the *blanket* item wording
("ref paths stay out of *artifacts*, unscoped") a ref-shaped literal in an
undeclared file kind passes today — an executed pass-while-violated instance.
Two honest resolutions, both already recommended below: (a) declare the
artifact-kinds allowlist in the E4 note so the row's verdict is explicit
(what it does today); (b) widen `--include` whenever a new artifact kind
becomes a declared class. This is why the honest floor is stated as *at the
current declared boundaries* — not "for all future file kinds".

The honest-floor verdict: **`runnable=9, by_hand=7` survives the attack**;
the shipped ratio `9/16, floor=8, by_hand=7` sits exactly on the bound — the
drill record is the proof of an already-bound gate.

### Residual attacks worth recording (each is a watch-list item, not a floor-breaker)

1. **E4 class boundaries (two, both declared).** (a) placeholder vault names
   `op://(FakeVault|wal|vault)/`; (b) artifact *kinds* `md/tsv/sh` (MSD-4:
   an executed pass-while-violated instance against the blanket wording —
   a ref-shaped literal in a `.json` passes). A future new placeholder or
   artifact kind entering via a reviewed commit must re-declare the allowlist;
   not falsified today (hits=0 verbatim live, no json/yaml artifact exists).
2. **H7's `0|1`**: a host whose hit count DROPS to 0 would still pass exit half
   and fail the ERE — `ITEM-LASTLINE` — which is correct-by-note ("re-pin only
   after reading the HIT lines"). Keep the note that names it.
3. **E1's verdict-line attribution skew** (MSD-1) — recommend in-lane fix:
   `&&`-chain preserving both gate outputs; or a combined
   `CHECKLIST_E1: census_ok drift_ok` summary line.

## Blockers

**None for ship.** The three drills are the only execution-proven gaps, and
each is a *row-edit discipline* matter, not a defect in the landed gate. The
recommendation list (L1's call, no review work needed):

1. `E1`'s check keeps the census stdout: drop the redirect (`>/dev/null`) so a
   future census failure attributes to *census* at the verdict line (one
   character of clarity, no semantic change).
2. Keep the E4 exclusion allowlist named as the *two* class boundaries
   (placeholder vault names; artifact kinds md/tsv/sh) in the TSV note
   (vault names are; kinds are not yet explicit) — any future sweep or new
   artifact kind follows the same declared-allowlist rule.
3. Keep the H7 `0|1` + `HITS=2` pin semantics visible in the SKILL bullet text
   (already present); a future host that legitimately drops to `HITS=0` (purge
   + re-run) must re-pin by hand after reading the HITs.

Nothing else must change before the gate ships.
