# kaidoku — round 37 report (attempt 1: honest stop at the pre-freeze probe stage)

L1 `KaidokuR37` (holds the §3 planner seat). Lane `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, branch `main`, base `85218c5913c2c42094a2cbc7b1444dea976fa74a`.

## Work performed

This attempt ran the protocol load and the pre-freeze **probe phase** of the planned round-37 claim, then stopped honestly when the run budget expired before any freeze or wave dispatch. No claim was frozen, no counter scored, no receipt committed as claim data, and no swarm wave was launched (the inline spawn handoff was never used).

Declared claim (intended, not frozen): **R37-C1 — coverage**: big-endian SquashFS v4 (`squashfs_v4_be`) through `sasquatch-v4be` via REA `extract-firmware` (rea-agents 6.5.0, unblob 26.6.4), Frontier → Core, with a QUALITY 77/78-compliant successor counter (`plans/round-37-claims.md`).

- Load order executed: `skill://shokunin` + canonical files, `skill://swarm`, lane SKILL/PROVINCE/SCORECARD/SHONEN/QUALITY/README/SOURCES, round-36 lesson + verifier spot-check (routed defects R36-CL1..CL6 read), run-8 goal file, watchdog log; probe of `merge/kaidoku` package (assimilation theme exists; `considerthese/` absent — one line).
- Probe evidence (committed in `77091b49`, `.ufo/waves/round-37/probes/`, `tools/round-37/`, `corpus/evidence/round-37/c1/`):
  - `tools/round-37/gen-squashfs.py` — deterministic SquashFS v4 writer (LE/BE/AVM-BE). Validated: LE gzip images extract byte-identical with `/usr/bin/unsquashfs` 4.7.5; BE gzip images extract byte-identical with `~/.local/bin/sasquatch-v4be -be`; AVM-BE (LE metadata-length fields, `mkfs_time == bytes_used`) fails on `sasquatch-v4be` without `-be` and on unblob's no-flag AVM branch (`ExtractCommandFailedReport`, stderr "different endianess / failed to read id table block") — AVM stays Frontier with this evidence.
  - REA `extract-firmware` after-runs on all four frozen carrier candidates succeed and publish every expected file (K1 5/5, K2 3/3 + 1 symlink `unpublished-entry`, K3/K4 4/4 apples; `squashfs_v4_be` chunk, 0 extraction gaps) — receipts in `.ufo/waves/round-37/probes/rea/`.
  - Before-arm shape verified on K3: with every PATH dir holding `sasquatch`/`sasquatch-v4be` removed, REA reports `extraction_gaps[].kind = missing-extractor-dependency`, `dependencies = ["sasquatch-v4be"]`, `handler = squashfs_v4_be`, `coverage partial`, `published_bytes 0`.
  - 7-Zip 26.04 does not open BE v4 images (recorded rejection candidate for SOURCES gate). unblob fixture bytes and apple digests verified (sha256 listed in `K{3,4}/oracle.tsv`).
- No census start/end artifacts (registry untouched; census validated exit 0 at the base — see Sources & frontier).

## Landed changes

| commit | what | LOG |
|---|---|---|
| `77091b492cc53f8743bd0701b1e7d5e66123dd84` | probe stage: `tools/round-37/{gen-squashfs.py,c1-run.sh,c1-counter.py}`, `corpus/evidence/round-37/c1/` (carriers K1-K4, source trees, oracles, carriers.json), `plans/round-37-claims.md` (intended claim + honest-stop record), `.ufo/waves/round-37/probes/` | no LOG entry (nothing landed; not a round landing) |

## Before → after measurements

None. No claim was frozen, scored or landed this attempt. The probe evidence above is pre-freeze development material, explicitly not claim data (`plans/round-37-claims.md`).

## Sources & frontier

SOURCES: unchanged — no rows added, touched or appended this attempt (111 rows at base; `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku` → `kaidoku ok`, 9× W04, exit 0). No frontier rows advanced (BE/AVM stays Frontier pending a frozen claim). Sourced-claim obligation not met (no claim landed). Assimilation: package theme inspected, id-collision/quarantine hand-checks due next attempt; `considerthese/` absent in this lane.

## Trend verdicts

- **expansion: unchanged** — no admitted entry, no frontier area entered, no capability row.
- **quality: unchanged** — no entry re-verified/superseded; probe tooling is not corpus material.
- **discernment: unchanged** — no gate decisions made; no non-author spot-check exists.

## SHONEN

- [ ] SKILL.md decision tables/error patterns/checklists/cited sources — not touched this round; no verifier.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — probes ran (REA extract on 4 BE carriers) but are not logged as a round task; no verifier.
- [ ] Instructions executable by an agent without oral context — not re-verified; no verifier.
- [ ] No cross-domain bleed (PROVINCE.md still accurate) — unchanged; no verifier.

## Round shape, seats, extras

- Shape: **no wave dispatched**. Round total 0 seats, 0 dead. The inline spawn handoff was prepared but never used because the attempt stopped at the pre-freeze stage (run budget). Planner seat held by the L1 (no planner swarm role).
- Tool installs: none this round (no pacman; no new binaries).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` — no file from this round's session at the fleet root (listed items are orchestrator/`.tower`/`.scratch` run state, not mine).
- Inherited state: lane was clean at start; `round-36/w2.ready.dispatched` untracked leftover remains (R36-CL1, status-neutral, untouched).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Open L0 questions: none added.
- Attempt verdict: **not completed (honest stop at probe stage)** — the round must be relaunched; all probe evidence is in the lane and reusable after re-verification.
