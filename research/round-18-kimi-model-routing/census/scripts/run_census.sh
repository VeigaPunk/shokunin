#!/usr/bin/env bash
# Reproduce the whole R18 census, in order.
#
#   bash scripts/run_census.sh [config.toml]
#
# Every step reads ~/.kimi-code/config.toml at runtime (override with $1 or
# $KIMI_CONFIG) and writes into this census directory. The config digest is
# printed before and after so a mid-run config edit is visible rather than
# silent -- the first pass of this census was invalidated exactly that way.
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$HERE"
CONFIG="${1:-${KIMI_CONFIG:-$HOME/.kimi-code/config.toml}}"

# Two digests, printed side by side on purpose. They are different values for the
# same file and conflating them is a real trap:
#   file_sha256_16    sha256 of the file's bytes, the value `sha256sum` gives.
#   parsed_sha256_16  sha256 of the parsed TOML re-serialised with sorted keys.
#                     This is the identity manifest.json records (see
#                     scripts/common.py:config_digest) and the one ANALYSIS.md
#                     quotes, so it is the one to compare against.
file_digest() { sha256sum "$CONFIG" | cut -c1-16; }
parsed_digest() {
  KIMI_CONFIG="$CONFIG" python3 -c "
import hashlib, json, os, tomllib
with open(os.environ['KIMI_CONFIG'], 'rb') as fh:
    cfg = tomllib.load(fh)
print(hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()[:16])
"
}
show_digests() {
  echo "  file_sha256_16   = $(file_digest)"
  echo "  parsed_sha256_16 = $(parsed_digest)  <- manifest.json / ANALYSIS.md identity"
}

echo "== census start $(date -Is) =="
echo "config=$CONFIG"
show_digests

python3 scripts/build_manifest.py "$CONFIG" || exit 1
python3 scripts/probe_shims.py "$CONFIG" || exit 1
python3 scripts/probe_models.py "$CONFIG" || exit 1
python3 scripts/probe_chat.py "$CONFIG" || exit 1
python3 scripts/probe_codex_input_shape.py "$CONFIG" || exit 1
python3 scripts/probe_rechecks.py "$CONFIG" || exit 1
python3 scripts/probe_stream.py "$CONFIG" || exit 1
python3 scripts/probe_usage.py "$CONFIG" || exit 1
python3 scripts/build_analysis.py || exit 1
python3 scripts/verify_numbers.py || exit 1
bash scripts/hygiene_check.sh

echo "== census done $(date -Is) =="
show_digests
