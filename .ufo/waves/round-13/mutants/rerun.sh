#!/bin/sh
set -eu
ROOT=$(mktemp -d /tmp/r13-rerun.XXXXXX); trap 'rm -rf "$ROOT"' EXIT
mkdir -p "$ROOT/.ufo/waves/round-12" "$ROOT/.ufo/waves/round-13"
cp MANIFEST.json "$ROOT/"; cp .ufo/watchdog.log "$ROOT/.ufo/"; cp -a .ufo/state .ufo/reports .ufo/prompts "$ROOT/.ufo/"
cp -a .ufo/waves/round-12/frozen .ufo/waves/round-12/fixtures "$ROOT/.ufo/waves/round-12/"
cp .ufo/waves/round-13/closure-check.py "$ROOT/.ufo/waves/round-12/closure-check.py"
cp .ufo/history-pin.json "$ROOT/.ufo/"
python3 .ufo/waves/round-13/closure-check.py --selftest | head -1
for n in pre post-actual post; do python3 .ufo/waves/round-13/closure-check.py --repo "$ROOT" --frozen "$n" | grep 'baseline:'; done
printf 'synthetic-pristine '; python3 .ufo/waves/round-13/closure-check.py --repo "$ROOT" --no-citations | head -1
