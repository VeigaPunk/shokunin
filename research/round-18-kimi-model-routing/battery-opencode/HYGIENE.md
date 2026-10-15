# Secrets hygiene — R18 opencode-go probe

Every artifact in this tree was produced by scripts that read credentials from `~/.kimi-code/config.toml`
at runtime and pass them only into request headers. This is the scan that proves no key material
reached disk.

## Command and output

```
$ python3 scripts/hygiene_check.py .
hygiene scan over .
files scanned: 44
credentials checked: 12 (values never printed)
hits: 0
$ echo $?
0
```

The first output line echoes the root argument. The run reproduces byte-for-byte on the same tree.

Run from `research/round-18-kimi-model-routing/battery-opencode`. Exit status is the number of
offending files, so 0 is a pass. The scan covers the 11 live captures in `raw/responses/`, the 11
mock captures in `smoke/raw/responses/`, `raw/telemetry.csv`, the prediction files, `raw-run.log`,
every script and this document.

## What the scan checks

| Check | Applied to | Rationale |
| --- | --- | --- |
| Literal value of each of the 12 configured provider keys | every text file | the strongest test: the actual credential must appear nowhere |
| Credential-shaped strings (`s`+`k-` and `oc_`+`sk_` prefixes) | every text file | catches a key from outside this config's provider list |
| The auth header name carrying a value | data artifacts (JSON, CSV, MD, log) | catches an unredacted header capture |

The third check is not applied to `.py`/`.sh` sources, because the line that *builds* the header is
not a leak; a real key pasted into a script still trips the first two checks.

## Why the scan is 0 rather than "nothing was checked"

- **Capture-time redaction.** `common.redact_headers()` replaces any header whose name matches
  `(auth|api[-_]?key|cookie|session|token|secret|bearer|credential)` with `<redacted:len=N>`, keeping
  the name so a reader can see *which* credential was sent. The opencode-go session header is in
  `common.SECRET_HEADER_NAMES`, so it is redacted on the same path.
- **Body keys use an exact-name list** (`SECRET_KEY_NAMES`), so request and usage fields such as
  `max_tokens`, `completion_tokens` and `prompt_tokens` record their real values instead of being
  scrubbed.
- **The auth scheme is never spelled in full** in this tree: `common.AUTH_SCHEME` is assembled from
  two fragments, so no artifact, including the scripts, carries the literal header spelling.
- **Evidence that redaction ran.** Every capture records `auth_headers_sent` as header *names* and
  `request_body` with values in place; `raw/telemetry.csv` has no credential column at all. The
  response headers kept in each capture are transport headers (`Server`, `CF-RAY`,
  `x-opencode-endpoint-id`, `x-opencode-upstream-model-id`, `x-zen-model`, `x-opencode-log-id`) — no
  credential is among them.
- **The user agent is not a secret.** The lane needs a browser-class user agent (M2 definitions
  ANALYSIS section 1). The value is a generic modern browser string, recorded per capture as
  `user_agent_sent` and in the manifest as the class `browser-chrome-141-linux`; it carries no
  fingerprint data and no credential.

## Note for future edits to this tree

Any text that spells the credential header name immediately in front of a token of twelve or more
characters will be reported by the third check — including text inside a document, which is how the
M3 battery's first `HYGIENE.md` tripped its own scanner in review round 1. That is the scanner
working; rewrite the sentence rather than relaxing the pattern.
