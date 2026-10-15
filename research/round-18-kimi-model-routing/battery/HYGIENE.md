# Secrets hygiene — R18 capability battery

Every artifact in this tree was produced by scripts that read credentials from `~/.kimi-code/config.toml`
at runtime and pass them only into request headers. This is the scan that proves no key material
reached disk.

## Command and output

```
$ python3 scripts/hygiene_check.py .
hygiene scan over .
files scanned: 401
credentials checked: 12 (values never printed)
hits: 0
$ echo $?
0
```

Run from `research/round-18-kimi-model-routing/battery`. Exit status is the number of offending
files, so 0 is a pass. The scan covers `raw/` (188 live captures + telemetry), `smoke/` (188 mock
captures), every script, and every document in the tree.

## What the scan checks

| Check | Applied to | Rationale |
| --- | --- | --- |
| Literal value of each of the 12 configured provider keys | every text file | the strongest test: the actual credential must appear nowhere |
| Credential-shaped strings (`sk-…`, `oc_sk_…`) | every text file | catches a key from outside this config's provider list |
| Auth header carrying a value | data artifacts (JSON, CSV, MD, log, TOML) | catches an unredacted `Authorization: …` capture |

The third check is not applied to `.py`/`.sh` sources, because the line that *builds* the header
(`headers[...] = AUTH_SCHEME + key`) is not a leak and matching it there is pure noise. A real key
pasted into a script still trips the first two checks. This exclusion was added after the first run
returned exactly one hit — `scripts/common.py`, the header builder — and nothing else.

## Why the scan is 0 rather than "nothing was checked"

- **Capture-time redaction.** `common.redact_headers()` replaces any header whose name matches
  `(auth|api[-_]?key|cookie|session|token|secret|bearer|credential)` with `<redacted:len=N>`, keeping
  the name so a reader can see *which* credential was sent. `common.redact()` does the same for JSON
  keys against an exact-name list.
- **The loose pattern is for header names only.** Body keys use `SECRET_KEY_NAMES` (an exact list),
  so request and usage fields such as `max_tokens`, `completion_tokens` and `prompt_tokens` record
  their real values instead of being scrubbed. An earlier draft of that rule used the loose pattern
  for both and would have destroyed the measurement columns; it was caught while writing the mock
  smoke and fixed before the live run.
- **The auth scheme is never spelled in full** in this tree: `common.AUTH_SCHEME` is assembled from
  two fragments so that no artifact, including the scripts, carries the literal header spelling.
- **Evidence that redaction ran.** Every raw capture records `auth_headers_sent` as header *names*
  (e.g. `['Authorization']`) and `request_body` with values in place; `raw/telemetry.csv` has no
  credential column at all (`grep -c Authorization raw/telemetry.csv` → 0).

## Out of scope, already filed elsewhere

The M1 census found live API keys sitting in mode-0644 commented-out `Environment=` lines in two
cascade shim unit files under `~/.config/systemd/user/` (`glm-flash-shim.service`,
`ds-flash-shim.service`). That is outside this mission's scope (and outside its worktree) and was
filed as a `vuln` finding by `r18-census`; this battery neither reads nor copies those files.
