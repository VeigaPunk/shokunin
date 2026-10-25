# Kagi historical marking — describe-don't-pin

Lane: `kagi-shokunin`. Audited tree: HEAD `5b0d4b784624a15506d3c85c77c3ae619e07467f` (worktree matches HEAD for `LOG.md`, `SCORECARD.md`, `corpus/stamps.tsv`; `git status --porcelain` on those three was empty). Read-only. No lane file edited. No live gate run (those belong to the gate rerun). No private file content read; `af8873ca` was not expanded.

Rule applied: a superseded count, hash, pid, or line number may stay if the sentence is marked historical / describe-don't-pin. A content hash of a missing file must not be stated as that file's current identity. A drift-baseline row is a preserved comparison pin, not a presence claim, only when prose does not also say the absent file currently is that hash.

## Verdict on the lane's own record

| Claim | Verdict | Why |
|---|---|---|
| `SCORECARD.md:323` "describe-don't-pin satisfied: no content hash of a missing file is asserted anywhere, the handler's last *measured* sha lives only in `drift-baseline.tsv`" | **disagree** | Prefixes of absent-file hashes are still in live knowledge entries. The same sentence also says "10 claims are parked" while quoting `deferred=11`. |
| `corpus/lessons/round-19-recensus.md:34-35` `SKILL.md:46` "54 stamps + 32 claims" and `:241` "94 scratch cases" are superseded; live data is 56 / 35 and `R11-09` = 97 | **agree** | Measured: 56 stamp rows, 35 claim ids, 97 `tcase`/`tcase_last` calls in the selftest block. Those two SKILL lines are still current-voice, not marked historical. |
| `round-19-recensus.md:36-37` host source-basis lines still assert hash prefixes of absent files; `af8873ca…` must not be expanded | **agree** | Listed below. Prefix is not expanded in-repo or here. |
| `round-18.md:58-62` round 9–17 quotes stay verbatim; handler last stamped sha is `2eb86e1f…` of the pin list, described not re-derivable | **disagree on the hash** | Form is historical. The prefix is not the handler and not the pin list. It is `corpus/surface-census.sh` at `301b9ec` (`2eb86e1f0ee4`, 877 newlines). Handler pin is `drift-baseline.tsv:1` `2408b0c9…`. Current `surface-census.sh` stamp prefix is `275d8294a94e` (886 newlines). |
| `round-19-recensus.md:40-41` `round-13.md:9` `<FILL ON STAMP>` was never filled; not re-pinned as HEAD | **agree** | Placeholder still at `corpus/lessons/round-13.md:9`. It is not a content hash asserted as current identity. |
| `PROVINCE.md:10-17` surfaces below are HISTORICAL | **agree** for that caption | The list under it (including line pins at `:21`) is marked. `PROVINCE.md:52` current gate paragraph says 56 stamps + 35 claims + 97 cases, which matches the data files. |
| Carried debt "11 deferred rows" (`SCORECARD.md:331-333`, `substrate-deferral.md:21`, round-19) | **agree** | 11 `[substrate]` tags: `R11-01/02/03/04/06`, `R12-01`, `R15-01`, `R13-03`, `R16-01/03`, `R17-01`. |
| `round-18.md:72` "10 deferred ledger rows" | historical lesson, count wrong vs landed tags | Not a live pin. Round-19 and the scorecard debt list say 11. Left as a lesson-internal error. |

## Commands (this slice)

Host path existence (`test` via `os.path.lexists`, no content read). Exit 0.

| Path | Result |
|---|---|
| `$HOME/.local/bin/the-janitor` | missing |
| `$HOME/.config/the-janitor/` (client.py, opencode.json, config.json, op.env) | missing |
| `$HOME/.config/opencode/agents/janitor.md`, `tools/janitor_auth.ts`, `plugin/fnm-nudge.js` | missing |
| `$HOME/.local/bin/tac-check`, `$HOME/.local/state/the-janitor/`, `$HOME/.local/state/tac/` | missing |
| `$HOME/.agents/AGENTS.md` | missing |
| musketeer `com.1password.1password.json` | missing |
| `$HOME/.config/opencode/opencode.json` | file, mode `600`, 5 newlines, 95 bytes |
| `$HOME/.config/opencode/` | dir |
| `$HOME/.opencode/bin/opencode`, `/usr/bin/op` | file (not baseline-hashed) |
| `~/projects/shokunin` | missing |
| `~/Projects/shokunin` | dir |

`python3` stamp compare of `corpus/stamps.tsv` against worktree bytes (sha256 + `wc -l` newline count + byte length). Exit 0. Result: 56 rows, 0 missing paths, 54 match, 2 mismatch. Same two mismatch against `git show HEAD:` blobs, so this is the landed commit, not a dirty tree.

| stamps.tsv | Asserted | HEAD / worktree |
|---|---|---|
| `:52` `LOG.md` | `e6db90d2a37c4b34…`, 762 newlines, 56847 bytes | `a7c5f8e895d1a883…`, 769 newlines, 57126 bytes |
| `:54` `SCORECARD.md` | `f3e61bfe2e7878cb…`, 446 newlines, 66069 bytes | `a30eb36c9236ca9a…`, 452 newlines, 66281 bytes |

`opencode.json` sha compared to `drift-baseline.tsv:6` (`b270d762…`, 455 lines). Match: no. Current hash not printed (mode 600).

`git show 301b9ec:corpus/surface-census.sh | sha256sum` prefix `2eb86e1f0ee4`, 877 newlines. Confirms the mis-attribution above.

Selftest case count: 97 `tcase` / `tcase_last` invocations in `claim-ledger.sh` lines 1002–1316. Matches `claim-ledger.tsv` `R11-09` expect `^SELFTEST: PASS \(97 cases\)`. Not executed here.

## Counterexamples (presented as current)

### Counts

- `SKILL.md:46` decision table, current voice: "54 stamps + 32 claims". Data files: 56 stamp rows, 35 claim ids. Not under the falsification historical header (`SKILL.md:555-558` starts at line 553). Round-19 names this and leaves it.
- `SKILL.md:241` current instruction: "94 scratch cases". Implementation and `R11-09` are 97.
- `corpus/knowledge/claim-ledger.md:301-304` section title is `## Reproduction` (undated). It tells a reader the commands print `claims=17 stamped=33`, `cites=700 docs=43`, `cells=60`, `SELFTEST: PASS (72 cases)`. Those are round-13 figures. Round-19 did not name this block.
- `SCORECARD.md:323` same cell: `deferred=11` and "10 claims are parked". Tag count is 11. The "10" is a current scorecard claim, not a lesson.

Not counterexamples (dated or schema): `SKILL.md:249` "18 rows as of round 14"; `SKILL.md:183` "15 files as of round 9"; `claim-ledger.md:4-6` "436 lines … at the frozen wave revision" with current identity deferred to `stamps.tsv` (current stamp prefix `93c5827202b9`, not `d63c60b0`).

### Hashes of missing files asserted as identity

Full 64-char hashes of absent host files appear only in `corpus/drift-baseline.tsv` (rows 1–3, 6–10, 15). That file is the comparison pin. Agree it is not, by itself, a presence claim. Disagree that nothing else asserts those identities.

Present-tense or live-entry identity lines, files confirmed absent:

- `corpus/knowledge/config-layering.md:58` — `config.json` (0600, sha256 `af8873ca…`) "looks like a second overlay". No date on that sentence. Baseline row 4 withholds the hash (`-`). This is the sharp case: a prefix the hash policy refuses to pin, of a missing private file, stated as a current property. Do not expand.
- `corpus/knowledge/handler-on-disk-state.md:3-5` — handler `sha256 2408b0c9…57edd`, 333 lines, plus line pins. Line 9 dates line numbers and says re-grep; it does not say the file is absent or that the hash is not current identity. File is absent, so re-grep cannot succeed.
- `corpus/knowledge/handler-trust-boundary.md:3-6` — same handler prefix, plus `client.py` `8179b241…ce51`. Lines 10–11 date the read only.
- `corpus/knowledge/janitor-env-contract.md:3-4` — "read 2026-09-28 (sha256 `2408b0c9…57edd`, 333 lines)" then present-tense "The script's env reads are concentrated at L7–27". Date is on the source line; the hash is still the identity of a missing file in the live entry.

Dated reproductions that embed the missing handler's hash as what the gate prints, but are section-marked historical (not counted as unmarked current claims): `SKILL.md:608` (`deadbeef0b7e->2408b0c90b7e`, under the falsification historical header); `corpus/knowledge/drift-gate.md:175` (`Reproduction (2026-09-28)`). On this host that arrow cannot be the live output: the file is missing, so the gate's file verdict is absence, not a sha arrow to `2408b0c9`.

In-repo hashes that are still true, so not superseded: `drift-pins.sh` `c138d34c…0feb` / 451 newlines (`drift-gate.md:3`, `stamps.tsv:7`); `transcript-scan.sh` `2d60981b…` / 282 (`stamps.tsv:51`).

### Hashes asserted as current identity of files that moved

Not missing-file hashes. Still superseded hashes pinned as current:

- `corpus/stamps.tsv:52` `LOG.md`
- `corpus/stamps.tsv:54` `SCORECARD.md`

`drift-baseline.tsv:6` pins `$HOME/.config/opencode/opencode.json` at 644 / 455 / `b270d762…`. The path exists and does not match (mode 600, 5 newlines, 95 bytes). That is drift against a preserved pin, not a missing-file identity claim. `PROVINCE.md:27` "644, 455 lines" sits under the historical caption. Current hash not recorded here.

### Line numbers presented as current (handler absent)

`PROVINCE.md:21` line pins are under the historical caption. Agree.

Unmarked current-voice pins of `~/.local/bin/the-janitor`, file missing, so not re-derivable:

- `SKILL.md:24` L194
- `SKILL.md:25` L196
- `SKILL.md:32` L248 (the masking sentence is dated 2026-09-28; the line number is still in the decision table as the default path)
- `SKILL.md:335` L194–210
- `SKILL.md:357-358` L234 and L248
- `SKILL.md:400` L214–219
- `SKILL.md:412` L194

Knowledge entries that say "line numbers date to this read — re-grep before citing" (`handler-on-disk-state.md:9`, `handler-trust-boundary.md:10-11`) are partially marked. The re-grep instruction is not satisfiable while the binary is absent. Treat as the same debt class as the hash prefixes, weaker than the unmarked decision-table lines.

### Pids

No numeric pid is asserted as current. `corpus/lessons/round-8-aggregator-box3-coldrun.md:31` `llama-server` pid 1299 is a 2026-09-28 lesson observation. `janitor-command-surface.md:76` `server_pid` is a field name, not a live pid. Clean on this axis.

### Deleted-path spelling (adjacent, not a hash)

`scope-gate.sh:91` derives `LANE_ROOT` from the script directory (`SCRIPT_DIR/../..`), not from a hardcoded `~/projects/shokunin`. Agree with round-19 on the resolver. The lowercase spelling is still written as the resolution root in `corpus/adjacency.tsv:19`, `corpus/knowledge/adjacency-scope.md:92`, and as a reproduction `cd` in `corpus/knowledge/surface-census.md:248`. `~/projects/shokunin` is absent; `~/Projects/shokunin` exists. Dead-path sweep owns the citation class; noted here only because round-19 bundled it with this debt.

## Named debt

| Debt | Where | Owner | Unblock |
|---|---|---|---|
| Decision-table counts still current-voice | `SKILL.md:46`, `SKILL.md:241` | kagi | Mark those lines historical, or replace with 56 / 35 / 97. Do not treat a lesson note as the mark on the line itself. |
| Undated reproduction block | `corpus/knowledge/claim-ledger.md:301-304` | kagi | Date it, or point at the verdict line the way `SKILL.md:555-558` already does. |
| Scorecard 10 vs 11 | `SCORECARD.md:323` | kagi | The tag list is 11. The "10" in that cell is the wrong current count. |
| Absent-file hash prefixes in live entries | `config-layering.md:58`, `handler-on-disk-state.md:3`, `handler-trust-boundary.md:3-6`, `janitor-env-contract.md:3-4` | kagi | Erratum on those lines: historical, file absent, identity is the baseline pin or withheld. Do not expand `af8873ca`. Do not re-pin the baseline to an empty host. |
| Erratum names the wrong hash | `corpus/lessons/round-18.md:59-60` | kagi | `2eb86e1f…` is not the handler pin. Handler prefix in the pin list is `2408b0c9…` (`drift-baseline.tsv:1`). Describe that, or say the described prefix does not resolve to the handler. |
| Stamps behind the landed docs | `corpus/stamps.tsv:52`, `:54` | kagi | Reviewed stamp of `LOG.md` and `SCORECARD.md`. Leaving them is a current-identity pin of a superseded blob. Not fixed here. |
| Handler line numbers in the executable layer | `SKILL.md:24`, `:25`, `:335`, `:357-358`, `:400`, `:412` | kagi | Same historical caption `PROVINCE.md` already has, or drop the line numbers until the binary is back. |
| Substrate absence (context, not a marking fix) | 14 of 15 baseline paths missing; one survivor (`opencode.json`) does not match its pin | host / whoever reinstalls the-janitor | Reinstall, then the baseline re-derives. Re-pinning to the empty host would destroy the preserved record. |

## What holds

- No in-repo stamp row points at a missing path.
- No full 64-char hash of a missing host file is copied into prose. The full hashes stay in `drift-baseline.tsv`.
- `af8873ca` is a prefix only. Not expanded.
- `round-13.md:9` is an unfilled placeholder, not a fake current hash.
- Falsification round bullets in `SKILL.md` are explicitly historical (`:555-558`).
- `PROVINCE.md` surface list is captioned historical, and its current gate-count sentence matches 56 / 35 / 97.
- No current numeric pid pin.
