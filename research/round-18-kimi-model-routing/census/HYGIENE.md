# R18 provider & model census — secrets hygiene

Scope: every file under `research/round-18-kimi-model-routing/census/` —
`manifest.json`, `ANALYSIS.md`, `HYGIENE.md`, all of `raw/`, and all of
`scripts/`.

## The check

```console
$ bash scripts/hygiene_check.sh
```

The checker builds a fixed-string pattern file at runtime and greps the whole
census tree for it. Patterns:

| Label | What it matches |
| --- | --- |
| `credential-prefix-A` | the two-character credential prefix used by the config's keys, plus a hyphen |
| `auth-scheme-spelling-B` | the auth-scheme word used on the wire, plus a space |
| `credential-prefix-C` | the third credential prefix spelling used by the config's keys |
| `api_key-head8` / `api_key-mid16` / `api_key-tail16` | head, middle and tail slices of every `api_key` in `~/.kimi-code/config.toml` long enough to have a distinctive slice |
| `custom-header-value` | every `custom_headers` value declared in the config |
| `env-OPENAI_CODEX_TOKEN-*` / `env-XAI_OAUTH_TOKEN-*` | middle and tail slices of the two OAuth tokens present in this shell's environment |

Three deliberate design choices:

- **The pattern literals for the prefix rows are assembled from adjacent shell
  fragments** (`"s""k-"`). That keeps the checker's own source free of the
  strings it hunts for, so the scan can cover the entire tree — checker and
  probe scripts included — without matching itself. A hand-written pattern file
  would have made the checker its own single false positive. The same trick is
  used in `scripts/common.py` for the auth-scheme constant.
- **Credential *values* are read from the config at runtime** into a `mktemp`
  file outside the census directory and are never echoed; the script prints only
  labels and match counts. No probe script contains a key: `scripts/common.py`
  reads `~/.kimi-code/config.toml` and passes credentials straight into request
  headers.
- **Redaction happens at capture time, not just at write time.**
  `common.redact_text()` scrubs credential-shaped values out of anything captured
  from the environment — notably `systemctl --user cat` output, where a unit file
  can carry a real key in a commented-out line. A commented credential is still a
  credential, so comment lines are redacted like any other.

Header *names* (such as the session header and `OpenAI-Beta`) are intentionally
**not** patterns. The raw captures legitimately record which credential headers
were sent — that is evidence, and a header name is not credential material. The
*values* of those headers are covered by the `custom-header-value` patterns.

## The gate caught a real leak

The first full run of this check exited **1** with three offending lines, all in
`raw/shims.json`. They were not false positives:

- `~/.config/systemd/user/glm-flash-shim.service` carries the **zai-coding-plan
  `api_key` verbatim** in a commented-out `Environment=` line, which
  `systemctl --user cat` returns and the shim probe had captured.
- `~/.config/systemd/user/ds-flash-shim.service` carries the **opencode-go key**
  the same way.

Two fixes followed:

1. `probe_shims.py` now runs every captured command's output through
   `common.redact_text()`, so no future capture can import those values.
2. The shim probe no longer dumps the entire `systemctl --user list-units` output.
   Besides being irrelevant to the census, that dump produced a false positive:
   an unrelated systemd service description happened to contain the
   `credential-prefix-A` sequence. Only the shim units' own lines are kept.

The underlying leak lives in `~/.config/systemd/user/`, outside this mission's
scope, so it was **filed as a TowerFinding** (`vuln`, medium) rather than fixed
here. It is also the reason this census's own artifacts are clean rather than
merely unaudited: the gate was proven to have teeth on a real finding before it
was used to certify the deliverable.

## Result

```console
$ bash scripts/hygiene_check.sh
census dir : /home/vgpnk/Projects/shokunin/.tower/worktrees/wt-1/research/round-18-kimi-model-routing/census
config     : /home/vgpnk/.kimi-code/config.toml
patterns   : 28 (values never printed)

  credential-prefix-A          files_matched=0
  auth-scheme-spelling-B       files_matched=0
  credential-prefix-C          files_matched=0
  api_key-head8                files_matched=0
  api_key-mid16                files_matched=0
  api_key-tail16               files_matched=0
  api_key-head8                files_matched=0
  api_key-mid16                files_matched=0
  api_key-tail16               files_matched=0
  api_key-head8                files_matched=0
  api_key-mid16                files_matched=0
  api_key-tail16               files_matched=0
  api_key-head8                files_matched=0
  api_key-mid16                files_matched=0
  api_key-tail16               files_matched=0
  api_key-head8                files_matched=0
  api_key-mid16                files_matched=0
  api_key-tail16               files_matched=0
  api_key-head8                files_matched=0
  api_key-mid16                files_matched=0
  api_key-tail16               files_matched=0
  custom-header-value          files_matched=0
  custom-header-value          files_matched=0
  custom-header-value          files_matched=0
  env-OPENAI_CODEX_TOKEN-mid16 files_matched=0
  env-OPENAI_CODEX_TOKEN-tail16 files_matched=0
  env-XAI_OAUTH_TOKEN-mid16    files_matched=0
  env-XAI_OAUTH_TOKEN-tail16   files_matched=0

TOTAL HIT LINES: 0
RESULT: CLEAN (0 hits)
```

Exit status 0. The 28 patterns are the 3 prefix spellings, 3 fragments × 6
configured keys that are long enough to slice, 3 custom-header values, and 4
fragments from the two environment OAuth tokens. Re-run the command above to
reproduce.

## What is in the artifacts instead of secrets

| Artifact | Credential representation |
| --- | --- |
| `manifest.json` | `api_key_present` (bool), `api_key_len` (int), `key_digest` (first 16 hex of a sha256 — non-reversible, used only to show the token-plan keys are distinct), `custom_header_names` (names only) |
| `raw/*.json` | `auth_headers_sent` lists credential header *names*; `Authorization`, `Set-Cookie` and the session-header value are replaced with `<redacted:len=N>`; other non-allow-listed headers keep only a length marker |
| `ANALYSIS.md` | no credential material; lanes are described by auth *kind* |

One class of value is kept verbatim on purpose: rate-limit and quota response
headers (`x-ratelimit-*`, `retry-after`, `x-codex-*-used-percent`,
`x-codex-credits-balance`, `x-request-id`). These are usage telemetry, not
credentials, and they are the evidence the operator's usage addendum asked for.
The allow-list is consulted *before* the "name contains a sensitive word" rule,
because otherwise `x-ratelimit-limit-tokens` would be hidden merely for
containing the word "token". `x-codex-turn-state` is an opaque per-turn blob and
is excluded from the allow-list, so it is stored as a length marker only.
