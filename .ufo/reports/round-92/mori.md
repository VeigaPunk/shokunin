# mori — round 92 (attempt 1) — report

Lane: `mori-shokunin` (fleet and host observability). Entering `f63d1ab030d4179576e494342f48ef8718e497a5`.
Frozen contract `699f6276`. Landing `9dce2ca6`. Bookkeeping and after-receipts `587c7dfe` (lane `master`, remote-equal).
Round verdict: **honest stop**. C1 is met as frozen (presence); C2 is unmet as frozen. No claim is admitted by this lane.

## Work performed

Declared claims (2; both on tied-lowest axes, depth 5 and freshness 5):

- **C1 (depth)** every `corpus/knowledge/` entry carries `source:`, `verified-at:`, `recheck:` within its first 12 lines. Contract: `.ufo/waves/round-92/contract.md` §C1; counter `.ufo/waves/round-92/count-c1.py`.
- **C2 (freshness)** the digest gate reports zero unresolved mismatches once supersession rows correct S615 and S235. Contract §C2; counter `.ufo/waves/round-92/count-c2.py`.
- The round-91 planned re-declarations (gate-clause arming; dated census snapshot) are not re-declared; the reason is in the contract (`## Claims`).

Work items with evidence:

- Do-nothing controls at `f63d1ab0` (committed before the wave): `C1=unmet knowledge=98 missing=19 floor=98`, exit 1; `C2=unmet mismatch=2 ... negatives=0 selftest=absent`, exit 1; the landed tool at `f63d1ab0` reads `DIGEST_CHECK rows=121 ok=87 mismatch=2 prefix_only=31 unpinned=1`, reproducing the round-91 receipt. `.ufo/waves/round-92/evidence/controls-r92.txt:3,6,9`.
- Frozen-population evidence: `evidence/c1-missing-entering.txt` (the 19 files); full census receipt `evidence/census-before-full.txt` (exit 0, 391 rows).
- Wave `w1` (one v1 wave, 11 seats; spec `.ufo/waves/round-92/w1-spec.json`, dispatch `w1-dispatch.json`, handoff `w1.ready`, results `w1-results.json`). Seats and outcomes (all 11 returned output; **no dead seat**):
  - `Mo92E01Digest` (executor): supersession and selftest for the digest tool. `w1/Mo92E01Digest.md`; patch `w1/patches/Mo92E01Digest.patch`. It raised the conflict in §5 (S349) and changed the exit rule, which the L1 refused (lesson Mistakes 1–2).
  - `Mo92S01Successors` (scribe): S619 and S620 rows, verified digests; `w1/Mo92S01Successors.md`.
  - `Mo92Sc01Src` (scout): gate facts. S619 quote 11 words, one occurrence, pinned sha256 re-measured; S235 PDF quote located; FIPS 180-4 §6.2 quote located. `w1/Mo92Sc01Src.md`.
  - `Mo92K01Trio`, `Mo92K02Trio` (scribes): trio lines on 19 knowledge entries; patches `w1/patches/Mo92K0{1,2}Trio.patch`; move-only check in `evidence/trio-moveonly.txt`.
  - `Mo92R01Atk` (reviewer, C1): `ATTACK C1 forger-accepted=3 rejected=3` (fenced keys, empty values, unrelated body accepted). `w1/Mo92R01Atk.md`.
  - `Mo92R02Atk` (reviewer, C2): `ATTACK C2 forger-accepted=1 rejected=6`; the accepted forgery is a forged tool that prints the expected lines. `w1/Mo92R02Atk.md`.
  - `Mo92R03Sweep` (reviewer): found the truncated `census-before.txt` (lesson Mistake 3). `w1/Mo92R03Sweep.md`.
  - `Mo92K03Crit` (critic): C1 does not hold as a depth move; C2 does not hold as frozen; the exit-rule relaxation would turn 31 failing rows green. `w1/Mo92K03Crit.md`.
  - `Mo92M01Mut` (mutation-tester): kill matrix over 8 tool mutants and 6 counter mutants (`w1/Mo92M01Mut.md`). Survivors are equivalent at the entering corpus, named there. Its own patch files are `w1/Mo92M01Mut-m1..m8.patch`.
  - `Mo92Conn01` (connector): overlap scan. C1 method overlaps but ownership does not; C2 detection overlaps kama `digest-ledger.py` (A4), with no ownership overlap. `w1/Mo92Conn01.md`.
- Integrator work (L1): applied the four settled patches; restored the entering exit rule in `tools/mori-source-digest.py` (docstring paragraph, `exit_code`, two arm expectations); removed the S620 row (redundant with S349); selftest `DIGEST_SELFTEST pass=11 fail=0` (`w1/Mo92E01Digest.after-run.txt`).
- Able-to-fail for the supersession logic on the landed tool: `evidence/mutants-r92.txt` (control 11/11 passes; m1 supersession disabled 9/11 fail, rc 1; m2 successor check removed 10/11 fail, rc 1; m3 superseded counted ok 9/11 fail, rc 1).
- Landed-registry run: `DIGEST S235 superseded-by S349`, `DIGEST S615 superseded-by S619`, `DIGEST_CHECK rows=122 ok=88 mismatch=0 superseded=2 prefix_only=31 unpinned=1`, exit 1 (`evidence/after-r92.txt:9`, `lesson` §Claims).
- Frozen counter at the landing revision (`evidence/after-r92.txt:3-10`): C1 met; C2 unmet, `checks_failed=run_rc,superseded_ids,negatives`.
- Fleet-root hygiene: the mutation-tester disclosed a transient stray `tools/mori-source-digest.py` in the fleet root; the L1 verified absence (`evidence/fleet-root-after-removal.txt`; `ls tools` shows no digest copy). The L1 removed its own earlier `.ufo/mo92-*` scratch files from the fleet root (lesson Mistake 4).

## Landed changes

- `699f6276` — frozen contract, counters `count-c1.py` and `count-c2.py`, do-nothing controls, census-before receipt (LOG: Round 92 entry, `587c7dfe`).
- `9dce2ca6` — landing (LOG Round 92):
  - `corpus/knowledge/` trio lines on 19 files (C1 presence);
  - `tools/mori-source-digest.py` supersession and `--selftest`;
  - `corpus/SOURCES.md` S619 (mined, correction row for S615) and S621 (queued, FIPS 180-4);
  - `corpus/lessons/round-92.md`; wave evidence `.ufo/waves/round-92/w1/` and `evidence/`.
- `587c7dfe` — bookkeeping: SCORECARD `## Round 92` with the capability row; LOG Round 92 entry; QUALITY 194–197; `corpus/README.md` round-92 frontier note; after-receipts `evidence/after-r92.txt` and `evidence/census-after.txt`.
- Not landed: S620 (redundant with pre-existing S349); the gate exit-rule change (refused under QUALITY 193).

## Before → after measurements

| Claim | Counting command | Before (`f63d1ab0`) | After (`9dce2ca6`) | Evidence |
|---|---|---|---|---|
| C1 trio in first 12 lines | `python3 -I .ufo/waves/round-92/count-c1.py <rev> --repo <clone>` | `C1=unmet knowledge=98 missing=19 floor=98`, exit 1 | `C1=met knowledge=98 missing=0 floor=98`, exit 0 | `evidence/controls-r92.txt:3`, `evidence/after-r92.txt:3-4` |
| C2 digest gate, zero unresolved mismatch | `python3 -I .ufo/waves/round-92/count-c2.py <rev> --repo <clone>` | `C2=unmet mismatch=2 superseded=- prefix_only=31 unpinned=1 negatives=0 selftest=absent`, exit 1 | `C2=unmet mismatch=0 superseded=2 superseded_ids=S235,S615 prefix_only=31 unpinned=1 negatives=0 selftest=pass checks_failed=run_rc,superseded_ids,negatives`, exit 1 | `evidence/controls-r92.txt:6`, `evidence/after-r92.txt:6` |
| Digest tool selftest (supporting) | `python3 -I tools/mori-source-digest.py --selftest` | absent (rc 2) | `DIGEST_SELFTEST pass=11 fail=0`, rc 0 | `w1/Mo92E01Digest.md` §3; `evidence/mutants-r92.txt` |
| Census (supporting) | `scripts/sources-census.sh validate --file corpus/SOURCES.md` in a clone | exit 0, rows 391 | exit 0, rows 393 | `evidence/census-before-full.txt`, `evidence/census-after.txt` |

C2 failing clauses at the landing revision, all reproduced: `run_rc` (the gate exits 1 on the known 31 prefix-only and 1 unpinned rows, QUALITY 193); `superseded_ids` (the frozen successor map names S620 for S235; the actual successor is the pre-existing S349); `negatives` (fixture B needs an S620 row, which is not written).

## Sources & frontier

- `SOURCES.md` before → after: rows 391 → 393 (census before exit 0; after exit 0). Rows added by tier: A 2 (S619 docs, mined; S621 spec, queued). Rows touched old → new: none (append-only; S620 was not written).
- Rows added by tier, detail: S619 is mined (correction row for S615, used-by `corpus/lessons/round-92.md`); S621 is queued (FIPS 180-4 §6.2, located quote, no knowledge entry cites it this round).
- Frontier rows advanced: none of FR1–FR14. The digest-supersession premise and the host-path item are recorded as QUALITY 196 and 197 (`corpus/QUALITY.md` lines 2247–2255); the round-92 frontier note is in `corpus/README.md`.
- Assimilation: none (`merge/mori/` does not match this round's claims; reason in the lesson).
- considerthese: one item, `considerthese/2026-10-25.md` proposal 2 (host-path portability), measured: `tools/` 3 files, tracked wave `*.py|*.sh` 436, tracked `*.py|*.sh` 458 at `f63d1ab0` (`evidence/premise-and-hostpath.txt`). The reflection's count of 13 is not reproduced.
- Search log: the scout's two fetches (S619 pinned copy re-hashed; FIPS 180-4 landing page HTTP 200, PDF 833315 bytes, not retained). The rejected candidate S620 is recorded in the lesson gate with its flip condition.

## Trend verdicts

- **expansion: unchanged.** One correction row (S619) and one queued source (S621); no knowledge entry admitted.
- **quality: unchanged.** No admitted entry failed a re-check. The C1 predicate is presence-only (three forgeries accepted, `Mo92R01Atk`). The C2 predicate is unmet as frozen. The exit-rule relaxation was refused (QUALITY 193).
- **discernment: unchanged.** No non-author closure has run. The lane's gate decisions are the sample (admit S619, reject S620, refuse the exit-rule change). C1's depth verdict is left to the non-author closure.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer `SHONEN.md` line 10 (`SKILL.md:1211`, `corpus/QUALITY.md:1479-1514`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer `SHONEN.md` line 11 (`LOG.md` Round74).
- [~] Instructions executable by an agent without oral context — pointer `SHONEN.md` line 12 (selftest commands in SKILL.md; round 92 adds `python3 -I tools/mori-source-digest.py --selftest`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer `SHONEN.md` line 13 (`corpus/knowledge/wave-settlement-artifacts-r59.md`).

No box is `[x]`: no non-author verifier has signed any box.

## Extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none by the L1 or any seat; no install or upgrade was needed (poppler `pdftotext`, `curl`, `git`, `python3` were already present). `pacman` not used.
- Mistakes this round (full table in `corpus/lessons/round-92.md` §Mistakes): unchecked registry premise (S349); exit-rule relaxation proposed by the executor (refused); truncated census receipt (replaced by the full one); fleet-root scratch by the L1 (removed); body-moved trio lines (move-only check; two blank lines disclosed).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only ` M .scratch/run15-state.json` (orchestrator-owned; not touched by mori). No seat misroot found. The lane's untracked `w1.ready.dispatched` is the orchestrator's marker and is not committed.
- Dead seats: none (11 of 11 returned output; `w1-results.json`).
- Wave shape: one v1 wave `w1`, 11 seats (executor 1, scribe 3, scout 1, reviewer 3, critic 1, mutation-tester 1, connector 1); attack share 5/11 = 45 %; connector seats 1. The L1 is the planner seat. No residual call.
- L0 question appended: `mori | round-92 | Digest gate exit rule ...` in `.ufo/l0-questions.md` (the QUALITY 193 decision: keep the red gate, or narrow the exit rule to mismatch only).
- Contract deviation disclosed: the frozen C2 predicate was not satisfiable as written (see the lesson, Claims C2); the defect is named, the claim is not re-declared, and it is not admitted.

## Pre-report gate

- `git -C /home/vgpnk/Projects/shokunin/mori-shokunin ls-remote origin refs/heads/master` → `587c7dfe13a637c8a82515eed8233827f4d58a5f` (local equal).
- `grep -c '^## SHONEN' <report>` → 1 (checked before commit).
