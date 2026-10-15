# Secrets hygiene — R18 capability battery

Every artifact in this tree was produced by scripts that read credentials from `~/.kimi-code/config.toml`
at runtime and pass them only into request headers. This is the scan that proves no key material
reached disk.

## Command and output

```
$ python3 scripts/hygiene_check.py .
hygiene scan over .
files scanned: 402
credentials checked: 12 (values never printed)
hits: 0
$ echo $?
0
```

Run from `research/round-18-kimi-model-routing/battery`. Exit status is the number of offending
files, so 0 is a pass. The scan covers `raw/` (188 live captures + telemetry), `smoke/` (188 mock
captures), every script, and every document in the tree — this one included.

The output above is the run on the committed tree, and it reproduces. An earlier version of this
document reported `hits: 0` over 401 files and did not reproduce: re-running the same command
reported one hit, in this file. That is a documentation defect, not a leak, and it is recorded in
full in *Self-reference* below.

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

## Self-reference: the hit review round 1 found

Review round 1 on this mission came back `fix-then-merge` with exactly one finding, documentation-only:
the output recorded here said `hits: 0`, but re-running the identical command on the committed tree
reported

```
files scanned: 402
credentials checked: 12 (values never printed)
hits: 1
  HYGIENE.md: auth header carrying a value
$ echo $?
1
```

The cause was this document. An evidence line spelled the auth header name directly in front of a
file path, and the third check in the table above — which looks for that header name followed by a
separator and a token of twelve or more characters — matched the pair. The scanner was behaving
exactly as designed; the document was wrong, not the tree. Three things complete the record:

- **The earlier `0 hits` was honest when produced.** That run predates this file: it scanned 401
  files, i.e. the tree as it stood before `HYGIENE.md` was written, which is why the count here is
  one higher.
- **The hit was benign.** It was the scan matching this document's own example text. No credential,
  no capture and no measured value was involved; the reviewer verified independently that the tree
  is secret-free.
- **The fix removed the pattern, not the check.** The example line no longer places the header name
  next to a path or a token, and `AUTH_VALUE_RE` in `scripts/hygiene_check.py` is unchanged. No
  measured data, capture, grader or analysis file was touched.

The rule to carry forward, because this trap will recur: **any text in this tree that spells the
credential header name followed by a separator and a token of twelve or more characters will be
reported — including text inside a document, and including text that a line break separates. That is
the scanner working. Rewrite the example; do not relax the pattern.**

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
  (e.g. `['Authorization']`) and `request_body` with values in place. `raw/telemetry.csv` has no
  credential column at all — counting that header name as a column in the CSV returns 0. The name is
  not spelled here next to a path, because doing so is what tripped this document's own scanner in
  review round 1 (see *Self-reference* above).

## Out of scope, already filed elsewhere

The M1 census found live API keys sitting in mode-0644 commented-out `Environment=` lines in two
cascade shim unit files under `~/.config/systemd/user/` (`glm-flash-shim.service`,
`ds-flash-shim.service`). That is outside this mission's scope (and outside its worktree) and was
filed as a `vuln` finding by `r18-census`; this battery neither reads nor copies those files.
