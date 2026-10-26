#!/usr/bin/env bash
# Thin gate wrapper for scripts/hyaku/disk-guard.sh — keeps the disk guard beside the other
# *-selftest.sh gates (`bash scripts/hyaku/disk-guard-selftest.sh`).
# Contract: exit 0 = every fixture case passes, including the seeded-defect arm that proves the
# gate can fail; 1 = a case failed; 2 = the guard itself is unusable (bad env/usage).
# Runs entirely under a mktemp fixture: touches no real root, no lane repo, no fleet state.
set -u
SELF_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
exec bash "$SELF_DIR/disk-guard.sh" selftest "$@"
