# KagiSecrecySentinel — secrets shape membrane

Advisory only. Not a gate verdict, lane-round report, receipt, or admission. No live gate was run. Protected targets were not opened.

Start revisions from `baselines.json`: kagi `fecee8743e52eb8fb5fbb40782934cb619a1a96e`, kake `b0feb30886585d8df6d4671845a2d18989ca722b`, kama `ea72c3eae4ecc68dab2b0a08153c9c1d2e16df21`, kasegi `d1e6e8f3931a2bfbeb4319b9b41980c1e801e9f1`, kengaku `d84e48d525d6af6b1d137d608aea8c726f8bead4`, kotoba `02302c521b933c55fc4be79193e61537e3380751`. Lane plan read: `kagi-shokunin/plans/wwkd-round-19-recensus.md`. The other five WWKD plans use the same gate sentence.

## Severity

**High.** Two registered commands content-read real session payloads. One of them also copies the payload store. Parent `claim-ledger.sh verify` and `cells` invoke the kagi reader. The captured before argv does not.

Named paths `credentials/`, `oauth/`, and `server.token` do not appear as open targets in the six before commands or in kagi gate code. That absence is not a license to add a walk.

## Exploit path

1. Parent treats "registered safe local commands" as the post-integration set (`wwkd-round-19-recensus.md` Gates, all six plans).
2. `bash corpus/claim-ledger.sh verify` runs `R11-06` `bash corpus/transcript-scan.sh` (`claim-ledger.tsv:20`). `cells` re-runs every cited non-self row through `verify_claims` (`claim-ledger.sh:766-797`).
3. `transcript-scan.sh:263-274` copies `$HOME/.local/state/the-janitor/xdg-data/opencode/opencode.db` plus `-wal`/`-shm` into `mktemp`, then `sql()` (`:100`) runs `LIKE` over text columns including `part.data`, `message.data`, `session.title`, and `session_input.prompt` (`:52-60`, `:143-160`). Output is counts (`:278-280`). The copy and the `LIKE` are still a content-read of session payloads.
4. Separately, registered `python3 verifiers/verify_harness_claims.py` walks `~/.omp/agent/sessions` (`verify_harness_claims.py:56`, `:390-405`) and `json.loads` each `.jsonl` line (`:405`). That is a live session-payload read. It is not the before argv.

`surface-census.sh:276-278` copies the same database before counting tables and rows (`:283-300`). Queries are metadata. The `cp` is still a copy of the payload store.

## Evidence

### Named paths

Grep of kagi `corpus/*.sh`, the six before scripts, and `ufo-fsd-alpha` found no open of `credentials/`, `oauth/`, or `server.token`. UFO `local_ship.rs:1898` only denylists the filename `credentials`. These directories were not listed or read.

### Before argv — do not exclude

| Lane | argv | Content-read of the four targets? |
|---|---|---|
| kagi | `bash corpus/claim-ledger.sh citations` | No. Reads lane Markdown. `cite_target` is `[[ -e ]]` on repo-relative classes only (`claim-ledger.sh:442-466`, `:512-577`). |
| kake | `node scripts/freshness-sweep.mjs --offline` | No. Citation check is `existsSync` (`freshness-sweep.mjs:420-421`). `readdirSync` of `~/Projects` keeps names (`:464-467`). History reads `probe-history.jsonl`, not a session store (`:945-946`). `--offline` skips fetches (`:736-743`). |
| kama | `bash tools/kama-probe.sh consumers` | No. Registry rows are `~/.local/bin/omp`, `$UFO_SRC/config/the-tick.machine.json`, `$UFO_SRC/scripts/local-helper.mjs` (`endpoint-consumers.tsv:35-37`). URL userinfo is stripped before print (`kama-probe.sh:609-612`). |
| kasegi | `python3 corpus/instruments/anchorcheck.py SKILL.md` | No on this argv. `CITE` (`anchorcheck.py:104`) requires a line anchor and an allowlisted prefix. `SKILL.md` has no backtick cite of `credentials/`, `oauth/`, `server.token`, or `sessions/` plus `:digits`. |
| kengaku | `python3 grader.py` | No. Defaults are committed files under `corpus/evidence/` (`grader.py:66-69`). |
| kotoba | `python3 verifiers/verify_corpus_integrity.py` | No. Reads tracked `corpus/*.md`. External pointers are `is_file()` only (`verify_corpus_integrity.py:484-491`). |

### Exclude from the post-integration set

| Command | Why | Evidence |
|---|---|---|
| `bash corpus/transcript-scan.sh` | Copies and scans session text | `:263-274`, `:52-60`, `:143-160` |
| `bash corpus/claim-ledger.sh verify` | Runs `R11-06` | `claim-ledger.tsv:20` |
| `bash corpus/claim-ledger.sh cells` | Re-runs cited rows, including `R11-06` | `claim-ledger.sh:766-797` |
| `bash corpus/checklist-run.sh` | `H7` is `bash corpus/transcript-scan.sh` | `checklist.tsv:40`; `claim-ledger.tsv:32` |
| `bash corpus/surface-census.sh` | `cp` of the session database | `surface-census.sh:276-278` |
| `bash corpus/drift-pins.sh` | `wc -l` and `grep -cE` on `op.env` | `drift-pins.sh:70-71`, `:96`, `:209`, `:222` |
| `python3 verifiers/verify_harness_claims.py` | Reads every omp session jsonl | `verify_harness_claims.py:56`, `:390-405` |
| `bash corpus/surface-census.sh --verbs --deep` | Operator-present; reads real custody; can raise a vault prompt | `SKILL.md:36` |

`op-ref-probe.sh` default `verify` writes plain fixtures under `mktemp` and refuses `op://` before exec (`op-ref-probe.sh:452-457`, `:214-222`). It does not open real `op.env`. Keep `--selftest`. Do not point `--fixture` at the live env file.

`scope-gate.sh` counts children with `find -print0` and deletes the name list (`scope-gate.sh:564-583`). It does not read file bytes except lane `basis` lines. Not a content-read of the four targets.

`session-id` is mode-only (`state-shape.tsv:40`). Do not `cat` it.

## Impact

A parent that runs the registered kagi verify set, or kotoba's harness verifier, loads operator session text into a temp copy or a Python process and can persist counts, paths, or excerpts in the wave receipt. Counts-only stdout does not undo the read or the copy. The before receipts already on disk do not do this.

## Smallest remediation

Do not edit gate code in this wave. Parent excludes the table above and runs only the shape-only set. No hash, no `sqlite3` open, no `cp`, no `LIKE`, no `json.loads` of a session file, no walk of `credentials/`, `oauth/`, or `server.token`.

Shape-only replacements, for parent after integration:

```sh
# kagi session store: header and stat only. Do not cp. Do not sqlite3.
DB="${THE_JANITOR_STATE_DIR:-$HOME/.local/state/the-janitor}/xdg-data/opencode/opencode.db"
if [[ -e $DB && ! -L $DB ]]; then stat -c 'db mode=%a bytes=%s' "$DB"; else echo 'db ABSENT'; fi
# 16-byte magic compare is the existing surface-census magic assertion; stop there.

# session-id and op.env: presence, type, mode, size. Do not read bytes.
for p in \
  "${THE_JANITOR_STATE_DIR:-$HOME/.local/state/the-janitor}/session-id" \
  "${THE_JANITOR_ENV:-$HOME/.config/the-janitor/op.env}"
do
  if [[ -e $p && ! -L $p ]]; then stat -c '%n type=%F mode=%a bytes=%s' "$p"; else echo "$p ABSENT"; fi
done
```

```sh
# credentials/ oauth/ server.token: stat a path only if a non-secret registry already names it.
# Do not find, grep, hash, or open. Absence is the result if no such registry row exists.
# This audit found no such row in the six before commands.
```

```sh
# kotoba session dir: count names, do not open jsonl.
d="$HOME/.omp/agent/sessions"
if [[ -d $d && ! -L $d ]]; then find -P "$d" -name '*.jsonl' -printf 'jsonl\n' | wc -l; else echo 'sessions ABSENT'; fi
```

Keep these already-safe commands, plus fixture selftests that stay on scratch trees:

- `bash corpus/claim-ledger.sh citations`
- `bash corpus/claim-ledger.sh docs`
- `bash corpus/claim-ledger.sh --selftest`
- `bash corpus/transcript-scan.sh --selftest`
- `bash corpus/surface-census.sh --selftest`
- `bash corpus/drift-pins.sh --selftest`
- `bash corpus/op-ref-probe.sh --selftest`
- `bash corpus/scope-gate.sh --selftest`
- `bash corpus/checklist-run.sh --selftest`
- `bash corpus/checklist-run.sh --list`
- `node scripts/freshness-sweep.mjs --offline`
- `bash tools/kama-probe.sh consumers`
- `python3 corpus/instruments/anchorcheck.py SKILL.md` on the current file only
- `python3 grader.py`
- `python3 verifiers/verify_corpus_integrity.py`

Do not add a kama registry row whose `consumer_path` is under those protected trees. `kama-probe.sh:631` prints a non-URL match raw.

## Proposed delta

Parent measurement exclusion, not a source edit. GateRepair must not "fix" this by printing less of a read that still copies the database.

## Unresolved debt

A leak scan cannot be shape-only and still inspect payload text. That measurement stays out of this wave. Owner: kagi, operator-present, not this seat.

`verify_harness_claims.py` cannot prove catalogue freshness without reading session jsonl. Replacement above is a count, not that claim. Owner: kotoba.

`anchorcheck.py:222-227` prints 100 characters of any resolved cite. Current `SKILL.md` does not aim it at the protected paths. A later cite under the `.ufo/` or bounty prefixes would. Owner: kasegi.

`checklist-run.sh:266-271` echoes the last six lines of a failing row. Safe only while excluded rows stay excluded.

Substrate absence may already `DEFER` some kagi rows (`claim-ledger.sh:129-143`). Not re-measured here.

## Cross-domain owner

Parent owns the post-integration command list and must apply the exclusion before any gate run. Kagi owns `transcript-scan.sh` and the database copy in `surface-census.sh`. Kotoba owns `verify_harness_claims.py`. Kasegi owns the excerpt printer. Kama owns registry path admission. This report does not authorize a code change.
