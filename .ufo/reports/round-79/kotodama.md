# kotodama — round 79 (attempt 2) — honest stop (operator wrap-up, run 12)

Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin · final lane tip `cb9b1c5c88e5daff346dce74485f1cfd1c7a729b` (verified: `git ls-remote origin refs/heads/main` prints it).
Report committed via `fleet-commit.sh --as kotodama`.

## Verdict

Two claims were scoped, frozen, landed and counter-verified **before** the
wrap-up arrived; the wave was still settling and wave 2 was never launched.
This is an honest stop, not a fleet closure: no axis score is asserted, the
in-flight wave is released unsettled, and the next round stays unchanged.

| claim | axis | landed | counter | verdict |
|---|---|---|---|---|
| Ca — bind r78 census S884 used-by drift with an append-only correction | calibration (unclaimed record/instrument repair, per the r79 CLAIMS-DRAFT pre-freeze scope disposition) | `reports/round-79/corrections/ca79-r78-s884.md` @ `0439764` (in graded history) | `reports/round-79/accept-ca.py` @ `82b822a` | `ACCEPT-CA-79: PASS legs=7/7` |
| O — acquire `tools/ledger-token-guard.py` | operability | `tools/ledger-token-guard.py` + `corpus/SOURCES.md` (S897) + `SKILL.md` (gate row) @ `80c6352` | `reports/round-79/accept-o.py` @ `7fdf355` | `ACCEPT-O-79: PASS legs=10/10` |

Lowest non-retired axis: freshness remains paused by the unresolved round-11
L0 question (same disposition as rounds 77/78), so the round worked
operability + calibration instead.

## What landed (commit chain, all pushed)

- `98b0e53` freeze #1: claims.json, both counters, r77 fixture ledgers
  (red/green), 16-file refusal battery, echo-stub control.
- `404b0aa`, `0439764`, `241627d`, `19d6901`, `ad2427c` Ca lands + two
  receipt-path corrections (see process findings).
- `80c6352` O lands: guard tool, S897 own-work row, SKILL.md gate row.
- `82b822a` re-freeze: counter fixes (`-z` diff-tree parsing, guard `--work`
  scratch dirs) + claims `sibling_paths` extension; supersedes `98b0e53` as
  the frozen base for grading.
- `7fdf355` accept-ca fix: corrections derive from `base..lands` adds;
  freeze..lands stays the separable window.
- `cb9b1c5` LOG entry + start-census telemetry.

Graded-run receipts live in this fleet dir:
`kotodama-accept-ca-lands.txt` (PASS 7/7), `kotodama-accept-o-lands.txt`
(PASS 10/10), `kotodama-pre-freeze-dry.txt` (both counters refuse at base,
exit 2), `kotodama-pre-dispatch-receipt.txt` (first dry-run receipt,
superseded). Claims/frozen constants: `reports/round-79/claims.json` in the
lane tree.

## The guard (claim O artifact)

`tools/ledger-token-guard.py` (sha256 `504c51c6…f040dd7964`, 17822 bytes)
re-runs a claim ledger's recorded observations against immutable committed
bytes: ops `count`/`line` on `cat-file` blobs only, `observe.rev` must be
40-hex, unsafe paths / command-channel keys / unknown ops / missing blobs /
mutable revs all refuse with the stable `LEDGER-TOKEN-GUARD` label; detects
`MISMATCH` (recorded≠observed, the r77 R78-M1 class) and `VACUOUS`
(stated==observed echo). Red fixture → 11/11 failures (10 mismatch + 1
vacuous); green → PASS 11 pairs; selftest 9/9; 16/16 refusal fixtures;
fresh-nonce oracle: real tool observed `1`, echo stub echoed the stated
nonce and never the observed token.

## Waves and seats

- W1: 32 seats dispatched through the inline handoff (`w1.ready` →
  orchestrator spawn, tranches 25→31→32 under the cap). ~27 seats delivered
  stage artifacts and `w1/*.md` reports; 5 seats returned empty stages
  (ScribeClaims, ScoutR77Truth, ConnHistory, RevSeparable, ScribeCorrection).
  WAVE-DONE had not arrived at wrap-up; the wave is released unsettled.
- W2 (falsify wave on the landed tool/counter): not launched.

## Integrated from W1 before the stop

- `ExecCaCounter` draft promoted to `reports/round-79/accept-ca.py` and
  adopted wholesale (its cfg/CORR_KEYS contract drove claims.json and the
  correction file).
- `ExecCaCounter` Ca claims fragment values verified and frozen verbatim
  (receipt blob `62eb55b7`, sha256 `05b5011a`, measured `4b255745`, S884
  r13-vs-10-23 used-by tokens — all re-derived by the L1).
- `RevQuality` binding map used to structure declared inputs, dry runs and
  review-only clauses.
- Adopted-but-UNLANDED seat findings (recorded for round 80, worktree edits
  reverted at honest stop to keep the tree identical to the graded lands):
  `MutPath` F5/F6 → `GIT_NO_REPLACE_OBJECTS=1` + `cat-file -t` blob check
  (blob check landed; env var reverted); `SentinelLimits` → 1 MiB ledger
  input cap + expanded `GIT_*` env drop (reverted); `MutRevision` →
  pristine-ledger-as-green is a defect class (red fixture correctly kept
  red).
- Mutation/critic batteries (`MutVacuous`, `MutRevision`, `MutPath`,
  `RevMalformed`, `SentinelLimits`, `CritNoopO/Ca`, `RevOContract`,
  `RevCaContract`) delivered fixture/driver evidence under
  `.ufo/waves/round-79/w1/stage/` — not yet folded into the tool.

## Process findings (for the record)

- Freeze/receipt geometry had two collisions: a committed receipt path first
  landed inside the Ca SEPARABLE window (fixed by relocating receipts to
  this fleet dir; lane A+D nets out of the diff), then inside
  `correction_dir` where the correction parser graded it (fixed by the
  base..lands corrections window in accept-ca). Both documented in
  `LOG.md` and the receipts.
- One counter re-freeze (82b822a) was needed after two counter defects
  (`-z` parsing; missing scratch dirs). Frozen claims were re-issued, not
  silently edited in place.

## Remains (explicitly not done)

- w1 integration of ~20 delivered stage findings into the tool/counter
  (replace-ref + input-cap hardening, distinct-observation floor).
- W2 falsify wave never launched; no mutation run against the landed tool.
- SHONEN/SCORECARD/PROVINCE updates beyond LOG.md; no corpus lesson
  (ScribeLesson draft exists under `w1/stage/ScribeLesson/`).
- 5 empty seat stages; orchestrator settles the wave record.

Tool installs: none. pacman not run (addendum guard respected).
Stale-lane: none at report time (`git status --porcelain` shows only
`.ufo/waves/` artifacts, never committable).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:20`,`:505`,`:564`; registry row added at `:767` this round (ledger-token-guard).
- [~] At least one end-to-end domain task executed and logged in LOG.md — round-79 O lands + `ACCEPT-O-79: PASS legs=10/7fdf355` + `ACCEPT-CA-79: PASS legs=7/7` receipts (fleet `.ufo/reports/round-79/kotodama-accept-*.txt`).
- [~] Instructions executable by an agent without oral context — counters run from committed bytes only (`--root/--lands/--freeze/--work`), receipts reproduce them verbatim.
- [~] No cross-domain bleed — lane paths only (tools/, corpus/SOURCES.md, SKILL.md, reports/round-79/); PROVINCE unchanged.
