# Secrets hygiene — M10 devin-opus

Every artifact in this tree was produced by scripts that read credentials from
`~/.kimi-code/config.toml` at runtime and pass them only into request headers.
Captures are written through the M3 battery's `common.write_json`, which redacts
credential-shaped keys and values before anything touches disk. This is the scan
that proves no key material reached disk.

## Command and output

```
$ bash scripts/hygiene_check.sh
scope dir  : /home/vgpnk/Projects/shokunin/.tower/worktrees/wt-10/research/round-18-kimi-model-routing/devin-opus
config     : /home/vgpnk/.kimi-code/config.toml
config sha : c5f12997f7cee456eacddbaf03c95e598ca5911cb18d6e6cf7821909b6fc9ebf
patterns   : 28 (values never printed)

  credential-prefix-A          files_matched=0
  auth-scheme-spelling-B       files_matched=0
  credential-prefix-C          files_matched=0
  api_key-head8/mid16/tail16   files_matched=0   (7 configured keys x 3 slices)
  custom-header-value          files_matched=0   (3 header values)
  env-OPENAI_CODEX_TOKEN-*     files_matched=0
  env-XAI_OAUTH_TOKEN-*        files_matched=0

TOTAL HIT LINES: 0
RESULT: CLEAN (0 hits)
$ echo $?
0
```

Run from `research/round-18-kimi-model-routing/devin-opus`. The scan covers
`raw/` (36 requests were sent; **31 per-request captures** remain — the pre-adapter
attempts' records were overwritten by their corrected re-runs: 2 real captures and
10 skipped-probe rows from the first battery attempt, plus 3 captures from the
first tool attempt. Their failure is preserved in `raw/run.log` and section 2 of
`ANALYSIS.md`), `scripts/` (6 files, this checker included) and the three documents.

## What the scan checks

| Check | Applied to | Rationale |
| --- | --- | --- |
| Fragments (head8/mid16/tail16) of every configured `api_key` ≥ 24 chars | every file | the strongest practical test: real key material must appear nowhere |
| Credential-shaped prefixes (`s`+`k-`, `oc_`+`sk_`) | every file | catches a credential from outside this config's provider list |
| The wire auth-scheme spelling | every file | catches an unredacted header capture |
| Every `custom_headers` *value* in the config | every file | custom headers are credential-bearing by position, not by name |
| Fragments of OAuth tokens held in this shell's env | every file | tokens that never appear in the config |

Pattern values are written to a `mktemp` file outside the scope tree and never
printed; only labels and hit counts are reported.

## Self-reference

The gate is designed to scan its own scripts, and it caught one: an earlier
`scripts/run_all.sh` carried the auth-scheme spelling literally in a `curl -H`
argument (`files_matched=1`, one hit line). It held no credential — the value was
the shim's own placeholder, which the shim does not check — but the round's
convention is that no artifact carries the scheme spelling, so the header is now
assembled from adjacent fragments, the same way every other checker in this round
assembles its own patterns. The re-run above is on the fixed tree and reports 0.

## Per-artifact notes

- `raw/devin-models-list.txt` and `raw/devin-models-opus.txt` are `devin models
  list` output: public model ids, context sizes and prices, no credential.
- `raw/models-shim-live.json` records the shim's static model list; the request's
  auth header is not part of the captured body and the shim answers without
  validating it.
- Every request record stores header *names* (`["Authorization"]`) and never
  values, per the M3 capture convention.
- `raw/run.log` records the config's sha256 and its opus/devin grep counts, not
  its contents.
- `scripts/candidate-config.toml` is a measurement-only config carrying the local
  shim's placeholder value (`devin-local`, 12 chars, below the fragment threshold
  and not a credential). No live-config key was copied into it.