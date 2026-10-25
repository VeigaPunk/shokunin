# Round-13 closure-input trust and spoofing review

## Axes

- **Trust boundary:** lane/operator filesystem writes -> `closure-check.py` loaders -> ledger/debt verdict -> frozen baseline comparison.
- **Gate integrity:** whether a value is independently pinned, and whether a concurrent writer can make a failing run appear legitimate.
- **Confidentiality:** credential sweep of this wave and round-13 commit inputs.

## Ranked input threats (impact x ease)

### 1. `expected.json` in each frozen snapshot — CRIT / highest

**Writer:** any actor able to modify the checkout (all lanes share the repo working tree); the file is also integrator-committed when snapshots are refreshed. Exact checks: `stat -c '%A %U:%G %n' .ufo/waves/round-12/frozen/pre/expected.json` (writable by the checkout owner) and `git ls-files .ufo/waves/round-12/frozen` (tracked files, not an access-control boundary). The checker directly reads it at `closure-check.py:1338` and compares only debt triples plus exit at `:1354-1366`.

**Fabrication and report:** rewrite the expected debt/exit to match a bad snapshot; a failing or altered frozen run then prints `baseline: match` and returns the pinned exit. No independent hash/signature of the snapshot files was found: `grep -RInE 'sha256|expected.json|baseline' .ufo/waves/round-12/mutation-gate.md .ufo/waves/round-12/mutants/mutant-score.json` finds prose/hash records for other material, not per-snapshot expected/manifest/log hashes. This is a concrete spoof path because `do_frozen()` reads both inputs and expected from the same directory.

**Smallest durable fix/cost:** commit one `sha256sum` inventory (3 snapshot directories x 8 files plus the shared README/patch = 26 lines, approximately 2 KiB) and make the gate verify it before loading; alternatively a signed/tagged commit pin (zero protocol lines if operationally enforced, seconds of `sha256sum`). Protocol addition: about 3-5 lines requiring immutable hash inventory and rejecting mismatch.

### 2. Frozen snapshot `MANIFEST.json` and `watchdog.log` — CRIT / high ease

**Writer:** same checkout/integrator; exact loader paths are `closure-check.py:260-271`, and exact write/access observation is `stat -c '%A %U:%G %n' .ufo/waves/round-12/frozen/pre/MANIFEST.json .ufo/waves/round-12/frozen/pre/watchdog.log` plus `git ls-files .ufo/waves/round-12/frozen`. A lane can fabricate rounds, statuses, dispatch/completion events, and timestamps in these files. The gate reports whatever fabricated ledger those bytes produce; if expected is rewritten too, it reports `baseline: match` (otherwise `MISMATCH`, which is the only internal signal).

**Fix/cost:** the same 25-line inventory or a commit/signature pin; runtime is one hash pass (well under a second for these small files). Do not pin only `expected.json`: snapshot inputs must be authenticated as a set.

### 3. Live `MANIFEST.json` `rounds[]` — WARN/CRIT / high ease

**Writer:** integrator appends it; shared checkout means any careless lane can edit it. Exact command: `git ls-files MANIFEST.json; grep -n 'inp.entries = manifest.get("rounds")' .ufo/waves/round-12/closure-check.py`. A fabricated append or in-place historical edit changes the authoritative ledger. The gate then reports altered debt, contradictions, or unadjudicable rows; a matching watchdog event can make false closure appear valid. Existing Git history is the stronger independent record (see history section), but the live working tree is trusted until commit.

**Fix/cost:** require/verify append-only history with `git log --follow` (roughly 5-15 gate seconds depending on repository); about 6-10 protocol lines. This catches non-append edits but not a malicious actor who can rewrite Git history or regenerate both commit and pin.

### 4. `.ufo/watchdog.log` — WARN / high ease

**Writer:** driver-appended/operator process; tracked but mutable. Exact command: `stat -c '%A %U:%G %n' .ufo/watchdog.log; grep -n 'log_path\|_parse_log' .ufo/waves/round-12/closure-check.py`. A careless or malicious writer can add dispatch, complete, or tick lines. The gate parses them at `:222-226` and reports fabricated completion/dispatch evidence, commonly reducing debt or changing pending-round/contradiction outcomes.

**Fix/cost:** append-only check versus Git history plus closed-at cutoff, 6-10 protocol lines and ~5-15 seconds; a hash inventory for frozen snapshots is cheaper and stronger for frozen mode. Git cannot see uncommitted append edits.

### 5. `.ufo/state/*.round` — WARN / high ease

**Writer:** lane/operator processes; exact scan command: `stat -c '%A %U:%G %n' .ufo/state/*.round; grep -n 'state_dir\|counters' .ufo/waves/round-12/closure-check.py`. A writer can raise counters and make progress/pending checks appear satisfied. The gate reads digit-only contents at `:242-248`, reporting altered counter/pending/debt findings; state counters are included in frozen `state-counters.txt`, not independently authenticated.

**Fix/cost:** record counters in the same snapshot hash inventory (no extra protocol beyond 3-5 lines; one hash pass). For live mode, reject counter decreases/non-append edits via Git where tracked; cannot detect uncommitted writes.

### 6. `.ufo/reports/**` — WARN / very high ease

**Writer:** any lane can write any path under the shared reports tree; exact loader sweep is `grep -n 'reports_dir\|_grade_file' .ufo/waves/round-12/closure-check.py`. A lane can fabricate a report, marker-sized file, hash presence, SHONEN heading, or mtime-sensitive landing. The gate reports report-missing/marker/contract/closed-at evidence according to filesystem state. In frozen mode report metadata comes from `reports-index.txt` and mtimes are deliberately absent (`:194-197`), so the index itself is the trust point.

**Fix/cost:** enforce ownership mechanically in the driver (about 15-30 lines, seconds); protocol text alone is not enforcement. For frozen mode include reports-index in the snapshot hash inventory.

### 7. `.ufo/prompts/**` — INFO/WARN / very high ease

**Writer:** prompt-generating operator/lane; exact parser is `grep -n 'prompts_dir\|prompts.add' .ufo/waves/round-12/closure-check.py`. A fabricated correctly named prompt makes the gate report prompt presence; an untracked prompt can disappear before commit. It cannot by itself forge a completion, but can affect prompt/deployment debt classification.

**Fix/cost:** driver records prompt path plus Git tracked blob/commit and rejects untracked prompt at closure (10-20 lines); frozen index must be hashed.

### 8. Child repositories' Git object stores — INFO/WARN / medium ease

**Writer:** child-lane commits and any actor with access to child repo objects. Exact citation path: `grep -n 'git_activity\|cat-file\|_classify' .ufo/waves/round-12/closure-check.py`. A report can cite an object/hash from a child store; ancestry classification can accept it if reachable from that child HEAD. This can fabricate provenance only if the child repository itself is compromised; the gate reports accepted citation/ancestry rather than a closure ledger spoof.

**Fix/cost:** record child HEAD OIDs and require signed/protected refs (about 8-15 protocol lines; seconds for `git rev-parse`). It cannot detect a compromised child repository whose HEAD is itself malicious.

## Frozen-baseline spoofing proof and hashes

`do_frozen()` hard-codes `.ufo/waves/round-12/frozen/<NAME>` (`closure-check.py:1329-1334`), loads snapshot `MANIFEST.json` and `watchdog.log`, then independently loads `expected.json` (`:1338`) and declares `baseline: match` when debt triples and exit agree (`:1345-1350`). Thus a lane that rewrites all three bytes can make a failing pass read `baseline: match`; nothing in the checker pins their bytes. The only observed independent records are narrative/hash values in `mutation-gate.md` and `mutant-score.json`, and the search command was:

`grep -RInE 'sha256|expected.json|baseline' .ufo/waves/round-12/mutation-gate.md .ufo/waves/round-12/mutants/mutant-score.json`

The exact current hash sweep (all files under all three frozen dirs) was:

```
3f1a2d0cc2a7b316732324aef174a06c9b248bb30acd634465b9f0ab60f967e1  .ufo/waves/round-12/frozen/README.md
6f653b041def59ddfe072d049623c4e15215031ae9cad4f7eaf20e7b051d5027  .ufo/waves/round-12/frozen/patch-entries.json
be8d79d20ed8f44786c7772561a6616ab15b239df3b4dcb169aec405fbc59245  .ufo/waves/round-12/frozen/post-actual/CLOSED_AT.txt
b95f9f7f04ee578f381a1999400573119e84c3d784ab24a6e2418d73a6597dae  .ufo/waves/round-12/frozen/post-actual/MANIFEST.json
fbf88062ddfadb66de8af3187b5397557074ce89403c4872052945645d6a0d33  .ufo/waves/round-12/frozen/post-actual/expected.json
bdad8a0ff82e3ded8c6ffc17401cf740e3ccc70e3b0c2216ec2e8d50c3e8ce57  .ufo/waves/round-12/frozen/post-actual/prompts-index.txt
03dabe50f37dea07e07eff11656bd6afc7579df9113161cd655a43b791091a64  .ufo/waves/round-12/frozen/post-actual/reports-index.txt
cb21fcf4488ac100b8cc8a845612e71ba0c5a7e6e27d905efccb211f2447db49  .ufo/waves/round-12/frozen/post-actual/state-counters.txt
d19283864cdcf28ba6e34c91729dcff27a54ea849131b17501671d2b2d84d637  .ufo/waves/round-12/frozen/post-actual/watchdog.log
```

The complete reproducible command is `find .ufo/waves/round-12/frozen -type f -print0 | sort -z | xargs -0 sha256sum`; it also covers the corresponding `pre` and `post` files (the command output is the authoritative full record; no secret material is involved). No committed artifact independently records hashes for every snapshot file. Smallest durable pin: commit `frozen/SHA256SUMS` generated by that command and verify it before `load_frozen`; 26 lines/~2 KiB and one hash pass.

## Proposed canonical-history pin

A pin over canonical JSON of `rounds[0..k-1]` detects any in-place edit or deletion of that prefix if the pin is held outside the edited data. It does **not** authenticate watchdog events, reports, prompts, state counters, frozen snapshots, or a newly appended `rounds[k]`; it also does not help if the same integrator can regenerate the pin after editing the prefix. Abuse path: integrator edits old `rounds[]`, recomputes canonical JSON, commits a replacement pin, and the gate blesses both.

Git is already the stronger historical pin for committed `MANIFEST.json`: `git log --oneline --follow -- MANIFEST.json` records each committed edit (and `git ls-files MANIFEST.json` confirms it is tracked). Cheaper alternative: gate verifies `git log --follow`/diffs are append-only for `rounds[]` (about 6-10 protocol lines, ~5-15 seconds). It cannot see uncommitted working-tree edits, force-pushed/deleted remote history, or a compromised signer/integrator with authority to rewrite history.

## Concurrency races and least-cost mitigations

- **Integrator appends `rounds[]` while eight lanes commit:** lost update or ordering mismatch can drop an entry, duplicate a row, or produce a transient malformed manifest. Least cost: serialize manifest updates with a lock and atomic temp-file rename (one driver change, negligible runtime); gate rejects non-append diffs.
- **Report lands between `closed_at` and commit:** filesystem mtime can be after the closure instant while the eventual commit makes it look landed. Live loader compares report mtime to `closed_at` (`closure-check.py:189-197`); race yields missing/late report debt. Least cost: capture/commit report before emitting closure, then immutable snapshot; do not infer timing from commit time.
- **Prompt durability treadmill (five untracked prompts):** prompts exist in the worktree and affect live detection but vanish from a commit or can be replaced by another lane. Least cost: require prompt files tracked before closure and include their paths in the atomic snapshot; 10-20 driver lines, no meaningful runtime cost.

## Credential screen

Sweep command (names only, never values):

`find .ufo/waves/round-13 .ufo/reports/round-13 -type f -print0 2>/dev/null | xargs -0 grep -IlE 'token|secret|password|api[_-]?key|credential|1password|op://|BEGIN .* PRIVATE KEY|/home/[A-Za-z0-9_.-]+' 2>/dev/null | sort`

Hits were only absolute-home-path class in `.ufo/reports/round-13/kumitate.md` (the report contains the lane working-directory/home-path class), plus ordinary instruction-surface words matched by the broad token/secret regex in `.ufo/reports/round-13/kotoba.md`; no credential value is reproduced. The narrower key-format sweep was:

`grep -RInE 'AKIA[0-9A-Z]{16}|(sk|pk|ghp|xox[baprs]-)[A-Za-z0-9_-]{8,}|1password|op://|BEGIN (RSA|OPENSSH|EC|PGP) PRIVATE KEY|/home/[A-Za-z0-9_.-]+/' .ufo/waves/round-13 .ufo/reports/round-13 2>/dev/null || true`

It hit absolute-home-path class in `.ufo/reports/round-13/kumitate.md`; no token/key/1Password/private-key class was observed. The wave directory itself was absent before this artifact, so its sweep had no pre-existing files. Re-run the same command after sibling wave artifacts are staged; this report does not claim to screen files that did not yet exist.

## Findings

- **CRIT:** frozen baseline set is mutable and co-loaded with its expected verdict; no complete independent pin.
- **WARN:** live manifest/log/state/report/prompt inputs are filesystem-trusted; protocol write-scope text is not mechanical enforcement (the loader has no ownership/ACL check).
- **INFO/WARN:** child Git object ancestry is stronger than free-form report claims but inherits child-repository trust.

Recommended order: (1) commit and verify `frozen/SHA256SUMS`; (2) atomic manifest/report/prompt snapshot plus append-only Git diff check; (3) optional signed child HEADs. 
