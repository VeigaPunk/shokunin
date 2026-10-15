# KagiScopeAudit — baseline scope audit

Advisory only. Not a native judge verdict, lane-round report, receipt, or admission. No gate file was edited. No build, lint, test, formatter, or registered gate command was run.

- Audited tree: `/home/vgpnk/Projects/shokunin/kagi-shokunin` at `fecee8743e52eb8fb5fbb40782934cb619a1a96e` (matches `baselines.json` and `evidence/kagi-before.json`). Tracked tree clean. Untracked: `plans/wwkd-round-19-recensus.md` only.
- Starting citation receipt (parent, not re-run): `CITATION_GATE: CLEAN (cites=912 docs=53 unresolved=0 ephemeral=0 labeled=13)` exit 0.
- Shape census only: `test`/`stat`/`scandir` counts. No credential, oauth, token, or session file was content-read. `~/.config/opencode/opencode.json` was mode-stat'd only.
- `lsp` device: not mounted. Caller/definition checks are text evidence, not semantic proof.
- `resume_continuity_v1`: no match in this lane. Not a kagi surface.

## Axis reading (audit, not a score move)

| Axis | Reading | Why |
|---|---|---|
| freshness | harmed vs the round-18 narrative | Live shared-dir cardinality is not the preserved "three dirs absent / one survivor" sentence, and the ledger cannot see that drift. |
| operability | unchanged, with a skipped proof | Seven gate scripts still exist and still have verdict paths. `R11-03` is deferred, so `verify` does not re-prove the absent-handler selftest. |
| calibration | harmed | `CELL_AUDIT`/`CLAIM_LEDGER` CLEAN treats deferred rows as non-failures. Several deferred rows measure objects that are present and drifted. The round-18 freshness cell describes a command the row does not run. |
| adjacency | unchanged mechanism, stale boundary text | Partition bases still text-match. Province/README still state the 2026-09-29 ratios as what the gate prints. |

No axis is saturated. Do not re-pin breadth or drift baselines to this host.

## Findings

### 1. High — substrate deferral hides measurable province-boundary drift

`substrate_present()` is only `[[ -x "$HOME/.local/bin/the-janitor" ]]` (`corpus/claim-ledger.sh:138-143`). A note containing `[substrate]` is skipped before `policy_check` and before execution (`claim-ledger.sh:396-399`). `cells` then prints CLEAN whenever `C_FAILED=0`, even if `C_DEFER>0` (`claim-ledger.sh:978-984`). Deferral is defined as "the thing the claim measures is not installed" (`corpus/knowledge/substrate-deferral.md:17-37`). That predicate is not what the tag implements.

`R16-01`, `R16-03`, and `R17-01` are tagged. Their commands are `scope-gate.sh`, `--falsify`, and `--breadth`. Breadth does not need the handler: a missing leaf is `SCOPE BREADTH-HOST-MISSING`; a live count mismatch is `SCOPE BREADTH-CHILDREN-DRIFT` / `BREADTH-DECLARED-DRIFT` (`corpus/scope-gate.sh:546-601`). Asset absence is exit-neutral for the partition (`scope-gate.sh:405-410`, `639`); cardinality drift is not.

Shape-only counts, 2026-10-14, names withheld:

| Leaf | Pin (`adjacency.tsv:75-78`) | Live |
|---|---|---|
| `$HOME/.config/opencode` | children=20 declared=4 | dir, children=3; only `opencode.json` exists among the four census children (`agents/`, `tools/`, `plugin/` absent) |
| `$HOME/.local/bin` | children=105 declared=2 | dir, children=34; `the-janitor` and `tac-check` absent |
| `$HOME/.agents` | children=4 declared=1 | dir, children=1; `AGENTS.md` absent |
| chrome-profile | children=53 declared=1 | absent |

[INFERENCE] From those counts plus `scope-gate.sh:550-601`, an untagged `R17-01` would not print `BREADTH_AUDIT: CLEAN (... children=182 ...)`. It would emit children-drift on the three existing dirs, declared-drift where the census child is gone, and `BREADTH-HOST-MISSING` on the profile. That verdict was not executed here. Parent should run `bash corpus/scope-gate.sh --breadth` after integration and keep the full line.

Counterexample: handler absent, `~/.local/bin` present with 34 children. `verify` DEFERS `R17-01` and can still be CLEAN. The coverage number the row claims to pin is never re-measured. Round-18's own contract says a deferred summary is not a pass (`substrate-deferral.md:59-61`). `cells` does not enforce that sentence.

Proposed delta (GateRepair, gate files only): do not tag rows whose command is decidable without the handler. `R16-01` / `R17-01` should fail closed on this host. Do not retarget their expect lines at the new counts. `R16-03` is a harder case: its note already says two breadth mutations read live host counts, so a partial run is real; splitting those mutations from the scratch mutations is the narrow fix, not a new pin.

Cross-domain owner: kagi parent integrator for the scorecard erratum. Not kotoba/kake — this is the lane's own tag.

### 2. High — preserved "all-GONE" / sha256sum absence pin does not match the row or the host

`R18-01` command is `bash corpus/drift-pins.sh`, expect `DRIFT_PINS: DRIFT (files_ok=0 files_bad=15 symbols_ok=0 symbols_bad=20)`, exit 1 (`claim-ledger.tsv:47`). The note says "the all-GONE summary" and "when the substrate returns this row fails".

`drift-pins.sh:139-160` increments `files_bad` for `MISSING` and for `DRIFT`. The summary line does not say GONE. A mode-drifted survivor still yields `files_ok=0 files_bad=15`.

Measured: 14 of 15 pinned paths are absent. `$HOME/.config/opencode/opencode.json` exists, mode `600`. The pin is mode `644`, 455 lines, hash `b270d762…` (`drift-baseline.tsv:6`). Mode mismatch alone cannot be `files_ok`. [INFERENCE] The summary regex can still match. A non-matching return of this file does not flip `R18-01`. A byte-identical return would. The note overclaims the return signal.

`SCORECARD.md:322` says `R18-01` is "`sha256sum` on the handler path, exit 1 `No such file`". The row does not run `sha256sum`. `substrate-deferral.md:49-54` already records why a direct handler-path probe is refused (`the-janitor` is a policy deny-word). The cell and the row disagree. `cells` will not catch that: pointer relevance is an accepted ceiling, and this is a live instance of it.

Proposed delta: correct the `R18-01` note and the scorecard cell to "drift-pins all-bad summary, not all-missing". Do not change the expect regex unless a parent-run verdict shows `files_ok` is not 0. Do not hash `opencode.json` into a report.

Owner: kagi parent for the scorecard sentence; GateRepair only if the note in `claim-ledger.tsv` is in the allowed gate-data edit.

### 3. Medium — province boundary still speaks the 2026-09-29 ratios as current

`PROVINCE.md:10-17` correctly marks the surface list HISTORICAL. The gates paragraph is below that erratum and is present tense:

- `PROVINCE.md:8` still heads the section with `resolved on this host 2026-09-29` and `absent=2`.
- `PROVINCE.md:51` says `--breadth` prints `20/4, 105/2, 4/1, 53/1` (182/8/174).
- `corpus/README.md:44` says "live leaf ratios 20/4, 105/2, 4/1, 53/1".
- `corpus/knowledge/adjacency-breadth.md:5-24` and `adjacency-scope.md:147` still show those numbers as the reproduction result. `Reverify: R17-01` does not re-run while the row is deferred, so `docs` can stay CLEAN.

The citation gate cannot see this. Host paths are excluded by rule (`claim-ledger.md:116-120`). The `historical` marker is line-local (`claim-ledger.sh:432-440`, `524`, `542`), so the erratum line does not reclassify the gates paragraph.

`SCORECARD.md:312` says three of the four pinned dirs are absent and opencode shrank 20→3. `SCORECARD.md:341-343` says opencode is "the one surviving shared dir". Current shape falsifies both: opencode, `~/.local/bin`, and `~/.agents` exist; only the chrome-profile leaf is absent. `corpus/lessons/round-18.md:15-21` does not make the three-absent claim. Same-commit narrative split.

Proposed delta: append a named erratum to the gates paragraph, README ratio cell, and the two scorecard sentences. Keep the pins. Do not rewrite round 9–17 evidence quotes.

Owner: kagi parent / RecordPrep. Not a sibling lane.

### 4. Medium — documented source root is the absent lowercase path; code uses another root

No kagi script implements `$UFO_SRC` or `--src`. `origin-work` / `ufo-fsd` strings exist only as round-18 prose (`LOG.md:722-727`, `lessons/round-18.md:1-8`, `SCORECARD.md:314`). There is no path citation to `~/Projects/ufo-fsd-alpha` (present) or `~/Projects/origin-work/ufo-fsd-alpha` (absent). The stale-`--src` class is vacuous for execution. The sentence "grep is EMPTY" is false after the writeup that contains those strings. Class (a) is "no gate opens that tree", not "the substring is absent".

The source root the lane does use is implicit and documented wrongly:

- Code: `LANE_ROOT` is `corpus/../../` (`scope-gate.sh:91`), i.e. this checkout's grandparent `/home/vgpnk/Projects/shokunin`. `cite_target` uses `$ROOT/../` (`claim-ledger.sh:464-465`). Both work here.
- Docs still say `~/projects/shokunin/<lane>-shokunin/`: `adjacency.tsv:19`, `knowledge/adjacency-scope.md:92`, `claim-ledger.tsv` `R11-08` note, `knowledge/surface-census.md:248`. That path is absent. `LOG.md:710-711` already records the round-17 code fix and leaves the comments.

Counterexample: a reader who follows `adjacency-scope.md:92` looks up `~/projects/shokunin/kake-shokunin/SKILL.md` and gets ENOENT. The gate resolves `lane:kake/SKILL.md:161` through the capital-P grandparent, where line 161 still contains `the-musketeer`. Same-identity is the script grandparent, not the documented path. A lone clone still fails sibling cites (`R11-08` note is right about that failure, wrong about the path spelling).

Latent second identity: census verbs use `command -v the-janitor` (`surface-census.sh:82`, `817`). The ledger uses the fixed path. A PATH stub with no pinned binary would skip-case one way and defer the other. Both are absent today (`command -v the-janitor` empty; `/usr/bin/op` and `/usr/bin/sqlite3` present). Not a live fail.

Proposed delta: replace the lowercase layout sentence with "script grandparent, which on this host is `~/Projects/shokunin`". Do not add a `ufo-fsd` pin. There is nothing to point at.

Owner: kagi. Integrator only if fleet docs still teach `~/projects/shokunin` as canonical.

### 5. Medium — citation inventory does not cover the province's actual evidence

`citations` CLEAN is about the scanned doc set and five token shapes (`claim-ledger.sh:442-466`, `495-508`). Before-receipt labeled set is 13 session/unresolved tokens, all on lines that already say so. That result does not mean host citations resolve.

Missing coverage, each with a counterexample:

1. Host paths and absolute paths are not a class (`claim-ledger.md:116-120`). `knowledge/handler-trust-boundary.md:245` cites `/home/vgpnk/.config/the-janitor/opencode.json`, which is absent. `lessons/round-8-aggregator-box3-coldrun.md:81` cites the musketeer NMH path, which is absent. Neither can fail `citations`.
2. `lane:` bases are not a citation-gate class. They are checked only by `scope-gate.sh:338-370`, and that row is deferred. Spot-check (not a gate run): `kake-shokunin/SKILL.md:161` still matches `musketeer`; `kotoba-shokunin/corpus/knowledge/alwayson-checklist-round7.md:30` still matches `AGENTS.md` and still says the host file is 75 lines / 3781 B. The host file is absent. Token match does not mean the shared surface exists. The note column cites `lane:kama/corpus/knowledge/cross-lane-scope.md` and is parsed by nobody (`adjacency-scope.md:94`). That kama file exists; a deletion would not fail either gate.
3. Default doc set omits `plans/`. The only unscanned markdown is `plans/wwkd-round-19-recensus.md` (54 markdown files, 53 scanned). It cites the before-receipt, which exists. Unscanned anyway.
4. Class 3 prose is stale relative to the scanner. `claim-ledger.md:104-106` still says a token is the first word inside a backtick span. The script scans every whitespace token on every line (`claim-ledger.sh:537-576`). The entry understates the gate. It also still says the shipped script is 436 lines and the ledger had 9 rows, with later counts only in parentheses.
5. Marker laundering is line-substring, case-insensitive. `relocat` matches `relocated` (`lessons/round-18.md:4`). `historical` on `PROVINCE.md:10` labels only that line. A broken `.ufo/…` token on a line that merely says "relocated" is `LABELED`, not `UNRESOLVED`. Not currently exploited beyond the 13 labeled hits. It is the counterexample the rule admits.

Proposed delta: either scan `plans/` and absolute host paths that match the census, or state in Class 3 that those are out of scope and that CLEAN does not re-verify them. Correct the backtick-span sentence to the whole-line scan. Do not treat the 13 labeled hits as new defects.

Owner: kagi citation gate. Kotoba owns the meaning of `~/.agents/AGENTS.md`; kake owns the musketeer lease. Both host objects are absent; report, do not absorb.

### 6. Low — `R11-03` deferral skips a proof that was written to pass without the handler

`R11-03` expects `SELFTEST: PASS (16 cases)` and is tagged. `surface-census.sh:817-846` prints `skip-case` for `verbs-sandboxed` and `verbs-break-injection` when `command -v the-janitor` fails, does not increment `failures`, and still exits 0 on `PASS (16 cases)`. On this host `verify` never runs that path. A regression that deletes the skip branch stays invisible to the calibration command exactly where it matters.

`R11-05`, `R11-07`, `R12-02`, `R15-02`, and `R16-02` are not tagged. The asymmetry is the defect, not the existence of selftests.

Proposed delta: remove `[substrate]` from `R11-03` only. Parent runs `--selftest` after integration. If it does not print `PASS (16 cases)`, the tag was load-bearing and this finding is wrong.

### 7. Low — deferred-count prose does not match the tag surface

Literal `[substrate]` notes: 11 rows (`R11-01/02/03/04/06`, `R12-01`, `R13-03`, `R15-01`, `R16-01/03`, `R17-01`). `R18-02` expects `^11$` and its note says "10 tagged rows plus this row's own pattern". The command text is `\[substrate\]`, which is not the substring `[substrate]`, so the 11th hit is an 11th tag, not the pattern. `SCORECARD.md:322` says 10 rows carried and 11 deferred in the same round. `lessons/round-18.md:72` says 10 deferred ledger rows.

The pin can be green while the explanation is false. Not a reason to re-pin.

## What is not a defect

- Handler, `~/.config/the-janitor`, tac state, `tac-check`, and the musketeer profile are absent. That matches the round-18 absence list. Do not re-pin `drift-baseline.tsv`.
- Four adjacency bases still resolve and still match their tokens (`SCORECARD.md:54` contains `opencode`; kake `:161`; kotoba `:30`; round-8 lesson `:64` contains `NativeMessagingHosts`). Text-match is not host presence.
- `op` at `/usr/bin/op` does not make `R12-01` measurable. The probe also requires the handler (`op-ref-probe.sh:462-465`) and is correctly a substrate row.
- No `ufo-fsd` execution root to repair. Do not import the sibling `--src` fallback.

## Unresolved debt

- Handler reinstall remains the unblock for `R11-01/02/04/06`, `R12-01`, `R15-01`, and the drift/census/checklist/transcript pins. Un-deferral on a poisoned stub is the conservative fail (`substrate-deferral.md:62-64`). Keep that.
- Breadth pins stay 20/4, 105/2, 4/1, 53/1 until a reviewed re-pin. Current counts are debt, not a new baseline. Same-cardinality swap remains invisible even after a re-pin (`adjacency-breadth.md` bounds).
- `opencode.json` mode 644→600 is live drift on a file the "all missing" story omits. Unblock: parent `drift-pins` verdict, then either restore the file or record a named mode drift. Do not print or hash it here.
- Nothing schedules the gates. Operator scope. Unchanged.
- Vault refusal (ref-resolved masking, `op read` / `op inject`) is still a refusal, not a measurement. Unchanged.
- `$HOME/.config/opencode` ownership is still `unresolved` / integrator (`adjacency.tsv:81`). Contested musketeer lease stays kake's. Both rulings are moot only while the objects are absent; the opencode directory is not absent, so the ownership ruling is not moot.

## Verification gaps

- Registered gates were not run. Predicted `BREADTH_*` and `files_ok=0` lines are code-plus-shape inferences, not verdicts.
- `opencode.json` line count and hash were not measured (content-read refusal). Mode mismatch is sufficient to reject `files_ok` for that row.
- `plans/wwkd-round-19-recensus.md` was not in the before-receipt doc set.
- GateRepair was told the `R16-01` / `R17-01` / `R11-03` / `R18-01` classification and may edit gate files after this baseline. This report does not describe those edits.
- No saturation claim. No promotion claim.
