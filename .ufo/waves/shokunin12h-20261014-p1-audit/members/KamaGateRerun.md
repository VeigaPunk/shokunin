# KamaGateRerun

Seat: safe-gate rerun only. Read-only against `/home/vgpnk/Projects/shokunin/kama-shokunin`. No lane file edited. No commit. No push. `snapshot` not run (it writes `registry/history`; outside the safe set).

Compared to the lane lesson's gate lines, not to the repair-wave JSON. Lesson: `corpus/lessons/round-4-recensus.md` lines 8–14. SCORECARD move-log row 4 defers to that lesson and states no scalar.

This file is advisory data. It is not a judge verdict, receipt, or admission.

## Run context

- Post-run clock: `2026-10-14T21:19:45-03:00` (`date -Iseconds` after the gates had already returned). Per-command start times were not captured.
- cwd for every gate: `/home/vgpnk/Projects/shokunin/kama-shokunin`
- `git rev-parse HEAD`: `84a81304d7b0c77c84fe495f3bb728e8729faaff`
- `git log -1 --format=%s`: `round-4: OMP-era freshness re-census (measured gates; records + scoped repair)`
- Commit time: `2026-10-14 21:15:36 -0300`
- That HEAD is the wave's named lane-identity commit. `git merge-base --is-ancestor 84a81304d7b0c77c84fe495f3bb728e8729faaff HEAD` exited 0 (it is HEAD).
- Gate inputs clean: `git status --porcelain -- tools/ registry/` printed nothing.
- Worktree noise not read by these argv: `?? plans/` (full `git status --porcelain` at the post-run stamp).
- Gate shell: `HOME=/home/vgpnk`, `UFO_SRC` unset. No `--ufo-src` flag passed.
- `command -v shellcheck`: absent. Round-4 lesson does not claim this. LOG round-3 and the SCORECARD operability cell do ("shellcheck absent on this box"). That parenthetical still matches. Not a lesson-number mismatch.
- Hermetic residue after `test-snapshot.sh`: `find` under `${TMPDIR:-/tmp}` for `kama-snapshot-test.*` or `kama-probe.*` printed nothing (`wc -l` = 0). The harness uses `mktemp` and removes it on EXIT; this seat did not inspect `/tmp` beyond that name check.

Repair-wave files `kama-after-tools_*.json` record `measured_revision` `ea72c3eae4ecc68dab2b0a08153c9c1d2e16df21`. They were not used as this seat's numbers.

## Claim-by-claim

| Claim (lane record) | Observed | Label |
|---|---|---|
| Lesson L8–9: `bash tools/kama-probe.sh consumers` → exit 0 | exit 0; last line `consumer_rows_evaluated=3 exit=0`; stderr lines absent from the combined transcript | agree |
| Lesson L8–9: `$UFO_SRC` rows resolve `file_match=yes` | both `$UFO_SRC` rows printed `file_match=yes` (`ufo-fsd-thetick`, `ufo-fsd-local-helper`). The `omp-llama-cpp-default` row is `inherited`, not a `$UFO_SRC` row | agree |
| Lesson L9: against `~/Projects/ufo-fsd-alpha` (HEAD `964f443e`) | not a printed field. Derived: `UFO_SRC` unset, `--ufo-src` absent, `~/Projects/origin-work/ufo-fsd-alpha` absent, `~/Projects/ufo-fsd-alpha` exists, both cited files exist there, resolver order in `tools/kama-probe.sh` is flag → env dir → that candidate first. `git -C ~/Projects/ufo-fsd-alpha rev-parse --short HEAD` printed `964f443e`. `git rev-parse --verify 964f443e^{commit}` printed `964f443ee53df0ce06bd689af01f0dea031b01f9` | agree (path binding derived, not printed) |
| Lesson L10–11: `bash tools/kama-probe.sh check` → exit 2, `DEAD` / connection-refused, correct while nothing model-serves | exit 2; all 3 rows `DEAD` / `connection-refused` on 8080 and 34113; last line `registry_rows_evaluated=3 model_ok=0 drift=3 exit=2`. Listeners census had `model_endpoints=0` and did not list 8080 or 34113 | agree |
| Lesson L12–13: `bash tools/kama-probe.sh listeners` → exit 0; `FOREIGN_SERVICE` on a non-model port, classified, not a fault | exit 0; last line `probed=5 model_endpoints=0 foreign_service=3 unauthorized_service=0 dead=2 not_http=0`. Three `FOREIGN_SERVICE` rows (631 CUPS `html-non-model`; 38101 and 39929 `non-2xx-non-model-http`). Lesson does not pin the count | agree |
| Lesson L14: `bash tools/test-snapshot.sh` → `RESULT pass=24 fail=0` | exit 0; last line exactly `RESULT pass=24 fail=0`; 24 `PASS` lines above it; no `FAIL` line | agree |
| Safe set, not in the lesson verdict list: `bash -n tools/kama-probe.sh` and `bash -n tools/test-snapshot.sh` | both exit 0; stdout empty. LOG round-3 line 242 and SCORECARD operability cell say `bash -n` clean | agree with LOG/SCORECARD; lesson silent, so not a lesson mismatch |
| SCORECARD move-log row 4: freshness, "measured at HEAD (see lesson)" / "verdicts recorded per gate, no scalar" | row asserts no scalar. The lesson it defers to still matches this rerun | agree (deferred); no scalar in the row to disagree with |
| SCORECARD operability cell (last change round 3) and LOG round-3 live-proof block: `registry_rows_evaluated=3 model_ok=0 drift=3 exit=2`; `consumer_rows_evaluated=3 exit=0`; `RESULT pass=24 fail=0` | same last lines as this rerun | agree (older record, still true of these gates) |

No mismatch between the lesson's gate numbers and this rerun.

"Nothing serves" in the lesson's check bullet is scoped by the next bullet: non-model listeners exist and are classified. This rerun does not read "nothing serves" as "zero TCP listeners."

## Commands

### 1. `bash tools/kama-probe.sh consumers`

- argv: `bash` `tools/kama-probe.sh` `consumers`
- cwd: `/home/vgpnk/Projects/shokunin/kama-shokunin`
- exit: `0`
- stderr: no stderr lines in the combined transcript
- last line: `consumer_rows_evaluated=3 exit=0`
- stdout:

```
id                    | consumer                              | declared                                   | resolved_from_file                         | file_match | resolver_kind | endpoint                                   | port  | verdict | served_model
omp-llama-cpp-default | ~/.local/bin/omp                      | http://127.0.0.1:8080                      | LLAMA_CPP_BASE_URL                         | inherited  | raw           | http://127.0.0.1:8080                      | 8080  | DEAD    | -
ufo-fsd-thetick       | $UFO_SRC/config/the-tick.machine.json | http://127.0.0.1:34113/v1/chat/completions | http://127.0.0.1:34113/v1/chat/completions | yes        | url           | http://127.0.0.1:34113/v1/chat/completions | 34113 | DEAD    | -
ufo-fsd-local-helper  | $UFO_SRC/scripts/local-helper.mjs     | http://127.0.0.1:34113                     | http://127.0.0.1:34113                     | yes        | url           | http://127.0.0.1:34113                     | 34113 | DEAD    | -
consumer_rows_evaluated=3 exit=0
```

Path binding for the HEAD claim (not part of this argv's stdout):

- `printf` of `UFO_SRC`: `<unset>`
- `DIR_ABSENT /home/vgpnk/Projects/origin-work/ufo-fsd-alpha`
- `DIR_EXISTS /home/vgpnk/Projects/ufo-fsd-alpha`
- `FILE_EXISTS config/the-tick.machine.json` (1756 bytes)
- `FILE_EXISTS scripts/local-helper.mjs` (13983 bytes)
- `git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD` → `964f443ee53df0ce06bd689af01f0dea031b01f9`
- `git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse --short HEAD` → `964f443e`

### 2. `bash tools/kama-probe.sh check`

- argv: `bash` `tools/kama-probe.sh` `check`
- cwd: `/home/vgpnk/Projects/shokunin/kama-shokunin`
- exit: `2`
- stderr: no stderr lines in the combined transcript
- last line: `registry_rows_evaluated=3 model_ok=0 drift=3 exit=2`
- stdout:

```
id                    | consumer                              | declared                                   | verdict | reason             | served_model | evidence
omp-llama-cpp-default | ~/.local/bin/omp                      | http://127.0.0.1:8080                      | DEAD    | connection-refused | -            | file=inherited via raw @8080; rc=7 Failed to connect to 127.0.0.1:8080 after 0 ms: Could not connect to server; GET /v1/models -> 000
ufo-fsd-thetick       | $UFO_SRC/config/the-tick.machine.json | http://127.0.0.1:34113/v1/chat/completions | DEAD    | connection-refused | -            | file=yes via url @34113; rc=7 Failed to connect to 127.0.0.1:34113 after 0 ms: Could not connect to server; GET /v1/models -> 000
ufo-fsd-local-helper  | $UFO_SRC/scripts/local-helper.mjs     | http://127.0.0.1:34113                     | DEAD    | connection-refused | -            | file=yes via url @34113; rc=7 Failed to connect to 127.0.0.1:34113 after 0 ms: Could not connect to server; GET /v1/models -> 000
registry_rows_evaluated=3 model_ok=0 drift=3 exit=2
```

Exit 2 is the identity gate, not a probe error (probe error is exit 1). Matches the lesson.

### 3. `bash tools/kama-probe.sh listeners`

- argv: `bash` `tools/kama-probe.sh` `listeners`
- cwd: `/home/vgpnk/Projects/shokunin/kama-shokunin`
- exit: `0`
- wall time: 5.10 s
- stderr: no stderr lines in the combined transcript
- last line: `probed=5 model_endpoints=0 foreign_service=3 unauthorized_service=0 dead=2 not_http=0`
- stdout:

```
port  | bind     | owner           | verdict         | reason                 | served_model | evidence
53    | loopback | -               | DEAD            | connection-refused     | -            | rc=7 Failed to connect to 127.0.0.1:53 after 0 ms: Could not connect to server; GET /v1/models -> 000
631   | loopback | -               | FOREIGN_SERVICE | html-non-model         | -            | GET /v1/models -> 404 text/html; charset=utf-8 (Server: CUPS/2.4 IPP/2.1); 200|text/html; charset=utf-8 @ /
5355  | wildcard | -               | DEAD            | timeout                | -            | rc=28 timeout (connect=2s max=5s); GET /v1/models -> 000
38101 | loopback | omp(pid=935236) | FOREIGN_SERVICE | non-2xx-non-model-http | -            | GET /v1/models -> 404 text/plain;charset=utf-8 (non-2xx HTTP from a non-model service); 404|text/plain;charset=utf-8 @ /
39929 | loopback | -               | FOREIGN_SERVICE | non-2xx-non-model-http | -            | GET /v1/models -> 404 text/plain; charset=utf-8 (non-2xx HTTP from a non-model service); 404|text/plain; charset=utf-8 @ /
probed=5 model_endpoints=0 foreign_service=3 unauthorized_service=0 dead=2 not_http=0
```

Lesson does not quote this tally. No numeric disagreement to record. Counts are a sample, not a pin.

### 4. `bash tools/test-snapshot.sh`

- argv: `bash` `tools/test-snapshot.sh`
- cwd: `/home/vgpnk/Projects/shokunin/kama-shokunin`
- exit: `0`
- stderr: no `FAIL` lines in the combined transcript (`bad()` writes to stderr; exit 0 also requires `FAIL=0`)
- last line: `RESULT pass=24 fail=0`
- stdout:

```
PASS check fixture is MODEL_OK/exit 0
PASS snapshot exit mirrors clean check
PASS baseline TSV written
PASS transition ledger written
PASS one dated JSON written
PASS snapshot JSON contract + redaction
PASS baseline fields are normalized and complete
PASS first run records baseline, not transitions
PASS unchanged snapshot stays exit 0
PASS unchanged snapshot reports zero transitions
PASS unchanged snapshot leaves DELTA.md byte-stable
PASS unchanged snapshot leaves latest.tsv byte-stable
PASS dead fixture makes snapshot exit 2
PASS MODEL_OK to DEAD transition recorded
PASS served-id transition recorded
PASS row-set change preserves drift exit 2
PASS row-added transition recorded
PASS row-absent transition recorded
PASS malformed baseline rebaselines without breaking gate
PASS malformed baseline warns
PASS malformed baseline audited
PASS malformed line never becomes phantom transition
PASS snapshot --port refused with probe-error exit
PASS symlinked history dir refused
RESULT pass=24 fail=0
```

PASS-line count is 24. The `RESULT` line matches the body. Writes stayed in the harness temp dir (`--history` under `mktemp`); `tools/` and `registry/` porcelain stayed empty after the run.

### 5. `bash -n tools/kama-probe.sh`

- argv: `bash` `-n` `tools/kama-probe.sh`
- cwd: `/home/vgpnk/Projects/shokunin/kama-shokunin`
- exit: `0`
- stdout: empty
- last line: empty

### 6. `bash -n tools/test-snapshot.sh`

- argv: `bash` `-n` `tools/test-snapshot.sh`
- cwd: `/home/vgpnk/Projects/shokunin/kama-shokunin`
- exit: `0`
- stdout: empty
- last line: empty

## Counterexamples

None on the safe-gate numbers. No red gate. `consumers` exit 0, `check` exit 2, `listeners` exit 0, `test-snapshot.sh` exit 0 with `RESULT pass=24 fail=0`, both `bash -n` exit 0.

Not run, and not a counterexample: `bash tools/kama-probe.sh snapshot` (and `--json`). Outside the safe set; it writes tracked history. LOG round-3 snapshot lines (`20261014T124232Z`, `transitions=16`) were not re-executed. The round-4 lesson does not restate them.

Wording calibration, not a gate-number miss: lesson lines 29–30 say `SKILL.md` "still teaches a live 11-row `MODEL_OK` world." Checklist item 1 (`SKILL.md:177`) already says `registry_rows_evaluated=3 model_ok=0 drift=3 exit=2`, which matches this rerun. Items that still teach the old live world, and that this rerun's last lines contradict if read as current:

- `SKILL.md:195-197` pins `34113` `MODEL_OK` and `8080` `FOREIGN_SERVICE`. This listeners run did not list either port; `check` classified both `DEAD` / `connection-refused`.
- `SKILL.md:203` says tally `consumer_rows_evaluated=11 exit=0`. This rerun's last line is `consumer_rows_evaluated=3 exit=0`.
- `SKILL.md:213` says summary `{"registry_rows_evaluated":11,"model_ok":3,"drift":8,"exit":2}`. This rerun's check last line is `registry_rows_evaluated=3 model_ok=0 drift=3 exit=2`.

The lesson already marks that prose "recorded, not rewritten." The gloss overstates how uniform the staleness is. Not a failed safe command.

## Named debt

Gate debt from this rerun: none. No owner/unblock owed by a failed safe command.

Lesson-named host debt, re-observed because the check bullet depends on it:

- Positive controls `ufo-fsd-thetick` and `ufo-fsd-local-helper`: `file_match=yes`, verdict `DEAD`, reason `connection-refused`, port 34113. `omp-llama-cpp-default` likewise `DEAD` / `connection-refused` on 8080.
- `systemctl --user is-active qwen-coder.service` → `inactive`. `systemctl --user is-enabled qwen-coder.service` → `not-found`. Unit path `~/.config/systemd/user/qwen-coder.service` absent (and no `.service.d` directory).
- Owner: operator. Unblock, as the lesson states it: restore a serving unit. Until then `model_ok=0` / exit 2 is the identity result, not a probe defect.
- Province contraction remains an L0 decision (lesson lines 27). Not re-opened here.

SKILL checklist items 3–5 above: owner is the kama record on a later prose pass; unblock is to mark those items historical or rewrite them to the 3-row dead tally. The lesson already refused that rewrite this round. Not fixed here.
