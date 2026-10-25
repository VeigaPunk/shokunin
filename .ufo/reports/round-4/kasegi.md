# kasegi-shokunin — round 4 report

Repo: `/home/vgpnk/projects/shokunin/kasegi-shokunin`. Commits: `d6b71c0`
(round-4) + `0bde2e0` (round-4 cited-paths addendum).

## Gap closed

Two carried gaps, one closed trivially:

1. **`ledger/` undocumented → `corpus/knowledge/mission-ledger.md`.**
   Censused `missions.jsonl` (718 lines, 260 missions, 218 programs):
   dominant path `SCOPED→PLANNED→LEARNED` ×207; deep path
   `EVIDENCED→VERIFIED→SUBMISSION_PREPARED` exists once; `SUBMITTED` ×3 and
   `DISCLOSED_FREE` are operator-attributed facts. `ops/shared.mjs::
   appendLedger` is the sole writer — 3500-byte line cap for O_APPEND
   atomicity, `gitMutationBlocker` fail-closes git mutations. Telemetry
   census (7218 lines, ~30 event kinds). `candidates.jsonl` =
   the-bounty-hunter intake keyed by `b1k-NNN` run_ids. `imports.jsonl` =
   evidence_id-bound board imports. Full 14-tool `ops/` inventory included.
2. **`evidence/` vs `claims/*/evidence/` → `corpus/knowledge/evidence-dir.md`.**
   592-dir census: `scope-snapshot.json` 583, `authorization-envelope` 580,
   `provenance` 532, `custodian-receipts` 514, `honest-zero-record`
   (`honest-zero/v1`) 346, `status.json` 275; subdirs `raw/` 244,
   `history/` 154, `custodian/` 27, `b1k-NNN/` per-run dirs. Verified it's a
   heterogeneous per-program audit store — strict manifest contract applies
   only inside claim packages. `honest-zero/v1` schema + park-status shape
   read out of `evidence/bugcrowd-seek/`.
3. **`vgn-bounty-lab/` — resolved**: empty `git init`, zero commits, zero
   files. Nothing to learn; removed from gaps.
4. **`george/` — parked**: 49G comma.ai research workspace, zero `claims/`
   references; not claim-corpus material unless a package cites it.

## Changes

- `corpus/knowledge/mission-ledger.md` — new.
- `corpus/knowledge/evidence-dir.md` — new.
- `corpus/lessons/round-4.md` — new.
- `corpus/README.md` — coverage rows + gap closures (incl. vgn-bounty-lab,
  george parked).
- `SKILL.md` — new "Mission ledger & audit store" section + 3 cited paths.
- `LOG.md` — round-4 entry.
- Note: `corpus/lessons/round-1-aggregator-audit.md` (aggregator lane's
  round-1 audit, written mid-round by another lane) was swept into commit
  `d6b71c0` — legitimate in-scope content, retained.

## Carried gaps

- `fleets/registry.json` lane→model routing — likely cross-domain (fleet
  mechanics); left for aggregator adjudication.
- `george/` deep-walk — parked pending a claim-package reference.

## Friction noted (in lessons)

- `find -maxdepth 2` flat listings conflate nested run-dirs (`b1k-NNN`) with
  program dirs — census claims now cite depth.
- `telemetry.jsonl` has 3 unparseable lines / 7218 — census tolerantly.
