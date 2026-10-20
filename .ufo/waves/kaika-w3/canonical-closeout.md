# D5 canonical closeout

Completed in `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kimi-shokunin-canon` only. No commits or pushes; no watchdog loop/model calls; no edits to the fleet root or `scripts/shokunin-watchdog.sh`.

## Changed paths

- `README.md`
- `install.sh`
- `scripts/sources-census.sh`
- `skills/shokunin/protocol/CORPUS.md`
- `skills/shokunin/protocol/PROTOCOL.md`
- `skills/shokunin/protocol/MISSION.md`
- `templates/MANIFEST.schema.json`
- `templates/round-prompt.md`
- `templates/shokunin.conf.example`

## Changes

- Documented that default census/validation enumerate child repositories only and exclude `repo=.` main-repo lanes, while explicit targets and fail-closed empty-child behavior remain intact. The census selftest now compares default census totals and validation output with/without root declarations, checks that the quoted config is not sourced, and checks an empty child fleet still fails closed.
- Added explicit installer gates for the root fixture inputs and injection fixture required by census selftest.
- Clarified historical pre-regime ledger retention without loosening schema enums; retained the canonical-append validation requirement. No `train`, `craft`, or `closed` enum values added.
- Aligned round-end `rc 2` wording with driver warning/continuation: it remains a conformance defect, not a pass or admission. Documented that source checks do not validate trend verdicts/full admission criteria and independent non-author verification remains required; no trend gate added.
- Added the missing `SOURCES.md` corpus layout row. Removed deployment counts/wave paths from the non-frozen corpus rules and pointed their rationale to the existing appendix rows; left frozen v1/manual census text unchanged.
- Documented `templates/round-prompt.md` and `scripts/sources-census.sh` as configured fleet-root contents, plus the watchdog’s Linux `/proc`/`setsid` requirement. Added the maintained parser’s 0–3 leading-space / 4-space-code note and completed help output through `shared` and symbolic cadence modes.

- Updated canonical `MISSION.md` with startup-time config loading, `<id>|<repo>|<axes>`,
  derived lane cwd, and `SUBSTRATE_CMD`/global routing semantics. Kept the nine-lane
  example explicitly historical and the D5 Frontier step intact; copied no current host
  lane table.

## Scoped checks

- `bash install.sh` — **rc 0**; required files, fixture gates, script syntax, and plugin JSON passed.
- Isolated missing-fixture red/green probes — for missing root fixtures and missing injection `SOURCES.md`, the pre-fix control passed (**rc 0**) and the fixed installer failed with the expected fixture diagnostic (**rc 1**) in both cases.
- `bash scripts/sources-census.sh selftest` — **rc 0**, `selftest ok`; all 96 checks were killed (93 existing plus 3 root-target regressions), including indentation widths 0–3, root-dot exclusion, quoted-config non-execution, and empty-child fail-closed behavior.
- `bash scripts/sources-census.sh --help` — **rc 0**; output includes `shared`, the symbolic `cadence` description, and the child-only default.
- `check-jsonschema` — new canonical closure **rc 0**; negative enum cases `type=train`, `type=craft`, and `lanes.probe=closed` each **rc 1**.
- Final census source SHA-256: `3fb7261569f46423dd80ecc23e0a23789a7926f667c7a3fc559d2439d4a64e30`.

## Intentionally unchanged

- Historical fleet rows remain unnormalized and invalid under current canonical enums (106 legacy rows per the reviewed census); schema constraints were not weakened.
- The watchdog remains Linux-specific (`/proc`, `setsid`, `flock`); only documentation was updated. The parent’s planned fleet-default census after final heads remains outstanding.
- Driver continuation is not admission. Trend/admission validation and independent review remain human protocol duties; no automated trend gate was introduced.