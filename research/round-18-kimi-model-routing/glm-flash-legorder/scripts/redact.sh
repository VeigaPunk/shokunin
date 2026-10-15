#!/usr/bin/env bash
# redact.sh -- filter stdin -> stdout, replacing credential-shaped tokens with
# placeholders. Used at capture time so no artifact in this directory can carry
# live key material. Patterns are generic (shape-based), not the two known keys,
# so an unexpected new secret in the same capture is caught too.
set -euo pipefail
sed -E \
  -e 's/[0-9a-f]{32}\.[A-Za-z0-9]{16}/<REDACTED-ZAI-KEY>/g' \
  -e 's/sk-hyper[A-Za-z0-9._-]*/<REDACTED-HYPER-KEY>/g' \
  -e 's/\bsk-[A-Za-z0-9._-]{16,}/<REDACTED-SK-KEY>/g' \
  -e 's/(Bearer )[A-Za-z0-9._-]{16,}/\1<REDACTED-BEARER>/g' \
  -e 's/("?(api_)?key"?[[:space:]]*[:=][[:space:]]*"?)[A-Za-z0-9._-]{24,}/\1<REDACTED-VALUE>/g'
