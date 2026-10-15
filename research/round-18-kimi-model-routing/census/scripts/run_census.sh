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

digest() { sha256sum "$CONFIG" | cut -c1-16; }

echo "== census start $(date -Is) =="
echo "config=$CONFIG digest_before=$(digest)"

python3 scripts/build_manifest.py "$CONFIG" || exit 1
python3 scripts/probe_shims.py "$CONFIG" || exit 1
python3 scripts/probe_models.py "$CONFIG" || exit 1
python3 scripts/probe_chat.py "$CONFIG" || exit 1
python3 scripts/probe_codex_input_shape.py "$CONFIG" || exit 1
python3 scripts/probe_rechecks.py "$CONFIG" || exit 1
python3 scripts/probe_stream.py "$CONFIG" || exit 1
python3 scripts/probe_usage.py "$CONFIG" || exit 1
python3 scripts/build_analysis.py || exit 1
bash scripts/hygiene_check.sh

echo "== census done $(date -Is) =="
echo "config digest_after=$(digest)"
