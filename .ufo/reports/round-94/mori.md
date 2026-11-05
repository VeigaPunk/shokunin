# mori — round 94 (L1 MoriR94, attempt 1)

Lane `mori-shokunin` landed and pushed at `fa1af84211d17958ba2b931b362418bc8ecbe253` (`ls-remote origin refs/heads/master` prints the same hash; `jj-lane.sh state`: `ahead=0 behind=0 untracked=0`). Freeze `6b65e7c11f318481d5efa0429cdabb50743a2cc2`; spec and dispatch `4ae1678df9c190209971ceb4604b71d3e54d779d`. Entering `84b152308fa6c2f224ad75dff68e525dab9057ac`. Axes: calibration (C1, score 5, tied lowest non-retired) and operability (C2, score 7).

## Work performed

**Declared claims (2, distinct axes; C1 is on the lowest-tied axis):**
- **C1 — calibration.** The round-92 admission self-check must not pass an admission hash embedded in a longer token (round-93 routed defect R02, `count-c1.py:141`, `ac[:7] in va`). Predicate: the frozen v1 reads 3/3 embedded fixtures as met (false pass); the round-94 v2 reads 0/3, and v2 reads the live trio 19/19. Contract `.ufo/waves/round-94/contract.md` §C1.
- **C2 — operability.** The round-94 counters carry no host home literal and run with HOME unset and the fleet root passed by environment. Predicate `C2=met literal_r94=0 files_r94=3 frozen_r93=unchanged env_i=met env_unset=rc2`. Contract §C2.

**Work items (each with its evidence pointer):**
- Premise greps, entering receipts and the controls run: `.ufo/waves/round-94/evidence/premises-r94.txt`, `entering-c1-r94.txt`, `entering-c2-r94.txt`, `controls-r94.txt`, `gitignore-red-before.txt`.
- Admission token rule (`count-c1v2.py`, `admission_token_ok`): the first whitespace token of `verified-at:` must be ≥7 characters and a prefix of the admission `%h`. Live: 19/19 tokens are 8-character prefixes (premise P3).
- Frozen battery `controls-r94.py`: v1 `EMBED_FALSE_PASS v1=3/3`, v2 `v2=0/3`, `live_v2=met` (`evidence/controls-r94.txt`, rc 0).
- Replay `w1/Mo94E01Replay.md`: battery reproduced (rc 0); four extra fixture classes (token deleted; `0`+hash; uppercase; hash doubled): v1 false-passes 2/4, v2 0/4.
- Attack `w1/Mo94R01Atk.md`: eight out-of-battery admission forgeries (comma, fullwidth digit, 7-char prefix with the 8th replaced, closing paren, decoy first line, another file's prefix, uppercase, zero-width space): v2 0 false passes. Legitimate forms (one space, no space, tab) read met.
- Mutation `w1/Mo94M01Mut.md` (C1 counter): killed m1, m1b, m7 (the R02 substring form); survived m2 (length clause), m3 (census gate), m4 (trio floor), m6 (patched12); m5 equivalent. The four survivors are routed (Mistakes row 6).
- Relocation and HOME isolation `w1/Mo94E02Relo.md`: `C1=met` and `C2=met` under `env -i HOME=/nonexistent` with a copied census script; `C1_SETUP` rc 2 with no root (fail-closed).
- C2 attack `w1/Mo94R02Atk.md`: the literal scan misses `.json`, `.md`, `.env`, uppercase `.PY`, and split literals (host paths); it does catch a symlink; HOME is not a dependency (a planted `.gitconfig` changes nothing).
- C2 mutation `w1/Mo94M02Mut.md`: killed m4 (regex broadened) and m7 (root dropped); survived m1, m2, m3, m5, m6.
- Critic K01 `w1/Mo94K01Crit.md`: C1 **admit-candidate**, scoped to instrument calibration (the round-93 bookkeeping objection rebutted, §1e). C2 **not admitted as framed** (§2f): the round-94 counters are successor artifacts; the before was absence (`files=0`); `env_unset=rc2` also holds for a missing counter (§2c); the contract says "HOME unset" while the counter sets `HOME=/nonexistent`.
- Critic K02 `w1/Mo94K02Crit.md`: S624 teaches corrected (prefix test, no provenance claim); the proposed `.gitignore` rule **rejected** (would hide 33 tracked legacy markers); planner D1 **open** (the shape line discloses, does not close); fixture coverage gap named.
- Scout `w1/Mo94S01Src.md`: independent re-open of `stdtypes.html`: same bytes and sha256 as the L1's fetch; the `library/` URL redirects to `builtins/stdtypes.html`; the contract's quote spacing is a tag-stripping artifact.
- Connector `w1/Mo94Conn01.md` (read-only, 21 siblings): no sibling carries the R02 admission defect; seven siblings carry the host literal `/home/vgpnk` in live tooling (chousa, kaidoku, kama, and four more; full list in the file). Routed to the operator via L0; no sibling edited.
- Considerthese (2026-10-26 suggestion 3, QUALITY 136): the round-93 counters re-run at the scored revision `8edbb86d`: `count-c1.py` → `C1=met … adm_ok=19` rc 0; `count-c2.py` → `C2=met … home_literals=0` rc 0 (`.ufo/waves/round-94/evidence/rerun-r93-counters-at-8edbb86d.txt`). Round 93's reading of this item was wrong; corrected in the lesson.
- Lesson `corpus/lessons/round-94.md`: Gate (S624 admit, S625 reject), six Mistakes rows, routed defects, assimilation none, considerthese correction, trend verdicts.

**Wave shape:** one v1 wave `w1`, 12 seats (band 8–16): executor 3, scout 1, reviewer 2, critic 2, mutation-tester 2, connector 1, scribe 1. Attack seats 6/12 = 50 % (reviewer, critic, mutation-tester). The §3 planner seat is the L1 (the validator rejects `planner`; the contract's shape line discloses this; critic K02 §3 holds that this is disclosure, not closure: D1 stays open). Routing by role only; no `model` passed. Dead seats: none (12/12 returned output; `.ufo/waves/round-94/w1-results.json`). Residual call: none. Round total: 12 seats. The ready file was taken once (`w1.ready.dispatched`). Earlier attempts of round 94: none (watchdog shows a single launch at 07:01:47).

## Landed changes

| Change | Commit | Tied to |
|---|---|---|
| Frozen contract, `count-c1v2.py`, `count-c2v2.py`, `controls-r94.py`, receipts | `6b65e7c1` | LOG.md Round 94; `.ufo/waves/round-94/contract.md` |
| Wave spec, dispatch payload, registry | `4ae1678d` | LOG.md Round 94 |
| S624 (mined, used-by the lesson) and S625 (rejected) rows | `fa1af842` | LOG.md Round 94; `corpus/SOURCES.md` lines 405–406 |
| `corpus/lessons/round-94.md` | `fa1af842` | LOG.md Round 94 |
| `corpus/QUALITY.md` criteria 202 (token boundary), 203 (fail-closed root), 204 (durable dispatch markers) | `fa1af842` | LOG.md Round 94; QUALITY lines 2279–2303 |
| `SCORECARD.md` Round 94 section, capability row, Planned (round 95) | `fa1af842` | LOG.md Round 94 |
| `LOG.md` Round 94 entry | `fa1af842` | itself |
| Wave evidence `w1/` (12 seat reports, `swarm-registry.json`, `patches/gitignore-d3.patch` kept as rejected evidence), `w1-results.json`, `w1.ready`, `w1.ready.dispatched`, and the untracked dispatch markers of rounds 92–93 (D3 fix) | `fa1af842` | lesson Mistakes rows 1–2 |
| `.ufo/l0-questions.md`: three lines (D1; sibling host-literal class; C2 ruling) | fleet repo, via `fleet-commit.sh` with this report | L0 side channel |

No counter, controls file or contract changed after the freeze (`git diff --stat 6b65e7c1 fa1af842 -- .ufo/waves/round-94/{count-c1v2.py,count-c2v2.py,controls-r94.py,contract.md}` is empty). The round-93 counters are untouched (`git diff --stat 84b15230 fa1af842 -- .ufo/waves/round-93/{count-c1.py,count-c2.py,controls-r93.sh}` is empty). The `.gitignore` patch from `Mo94E03Gitig` was **not** applied (rejected by critic K02).

## Before → after measurements

**C1 (calibration).** Counting command: `python3 -I .ufo/waves/round-94/controls-r94.py /home/vgpnk/Projects/shokunin/mori-shokunin /home/vgpnk/Projects/shokunin` (prints `EMBED_FALSE_PASS`; exit 0 iff the expectations hold). Live: `SHOKUNIN_ROOT=/home/vgpnk/Projects/shokunin python3 -I .ufo/waves/round-94/count-c1v2.py <rev> --repo <lane>`.
- Before, entering `84b15230`: frozen v1 `EMBED_FALSE_PASS v1=3/3` (`evidence/controls-r94.txt`).
- After, freeze `6b65e7c1`: v2 `v2=0/3 live_v2=met adm_ok=19` (`evidence/controls-r94.txt`).
- After, landing `fa1af842`: `C1=met trio=98 files=19 adm_ok=19 adm_fail=0 patched12=12 seven_same=7 census=ok rev=fa1af842` rc 0; battery `EMBED_FALSE_PASS v1=3/3 v2=0/3 live_v2=met` rc 0.
- Score: not moved (no score claim; axis verdict below).

**C2 (operability).** Counting command: `SHOKUNIN_ROOT=/home/vgpnk/Projects/shokunin python3 -I .ufo/waves/round-94/count-c2v2.py <rev> --repo <lane> --root /home/vgpnk/Projects/shokunin`; diagnostic: `… --report --scan .ufo/waves/round-93`.
- Before, entering `84b15230`: round-93 counters `C2_REPORT … literal=6 files=5`; full check `C2=unmet literal_r94=0 files_r94=0 … checks_failed=files,env_i` (`evidence/entering-c2-r94.txt`).
- After, freeze `6b65e7c1`: `C2=met literal_r94=0 files_r94=3 frozen_r93=unchanged env_i=met env_unset=rc2`.
- After, landing `fa1af842`: `C2=met literal_r94=0 files_r94=3 frozen_r93=unchanged env_i=met env_unset=rc2 rev=fa1af842` rc 0.
- Score: not moved. The critic's objection to this as an operability move is carried in the verdicts.

## Sources & frontier

- Census before (entering `84b15230`): `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori` → `mori ok`, exit 0 (W04 duplicate-URL warnings only).
- Census after (landing `fa1af842`): same command, exit 0 (`/fast/scratch/hyaku/mori-r94/l1/census-after.txt`; W04 warnings only).
- Registry rows: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 395 before, 397 after. Malformed rows (`awk -F'|' … NF!=13`): 0 before, 0 after.
- Rows added by tier: A 2 (S624 `mined`, used-by `corpus/lessons/round-94.md`; S625 `rejected`, used-by `—`). B 0, C 0.
- Rows touched old→new: none (append-only; no status, recheck or used-by of an existing row changed).
- Sourced claim: C1 rests on S624, opened this round by the L1 (sha256 `2397d832…`, 815447 bytes, access 2026-11-05) and re-opened by a non-author scout (same bytes; `w1/Mo94S01Src.md`).
- Frontier rows advanced: none; `corpus/README.md` `## Frontier` unchanged.
- Assimilation: none (the lane checkout carries no `merge/mori/` package; shokuknow not opened). Considerthese: 2026-10-26 suggestion 3 executed as a re-run (evidence above).

## Trend verdicts

- **expansion: unchanged.** No knowledge entry admitted; two registry rows (S624 mined, S625 rejected) are rows, not expansion (CORPUS.md rule 4).
- **quality: unchanged.** No admitted entry superseded or found false; the 19 round-92 `verified-at` lines were re-checked by the frozen counter (`adm_ok=19`) and by the replay.
- **discernment: improved.** Two spot-check disagreements became lesson-backed criteria: the R02 substring defect (QUALITY 202, shown able to fail by the battery) and the untracked dispatch markers (QUALITY 204, shown able to fail by the porcelain before/after). The round-93 calibration reading was rebutted with evidence by a non-author critic (K01 §1e). The reject S625 is not yet non-author spot-checked (named).

## Axis and round verdicts

- **calibration:** C1 met as frozen; critic K01 **admit-candidate** (scoped to the instrument). No score moved.
- **operability:** C2 met as frozen; critic K01 **not admitted as framed**: successor artifacts, not a move on an existing artifact. Not re-declared after data (the freeze rule). No score moved.
- **Other axes:** unchanged. No axis harmed.
- **Round:** **honest stop on C2** (not admitted). C1 is an admit-candidate awaiting the operator's admission. Progression is held pending the operator's ruling on C2 (L0 line 3 of `.ufo/l0-questions.md`).

## Mistakes (lesson `## Mistakes`, six rows)

1. `untracked-orchestrator-marker` (round-93 D3) — fixed by committing the markers (`fa1af842`); porcelain `.ufo/waves`: 3 before, 0 after.
2. `fix-hides-evidence` — a `.gitignore` rule proposed by the wave was rejected by critic K02 (it would hide 33 tracked markers).
3. `located-quote-tag-artifact` — the contract's P5 quote spacing; corrected in the S624 row (tag-stripped count 1 for the visible text, 0 for the contract form).
4. `successor-as-before` — the C2 before was absence; caught post-data by critic K01; routed to round 95.
5. `env-fail-open-missing-counter` — `env_unset=rc2` holds for a missing counter; routed to round 95.
6. `control-battery-gap` — mutation survivors m2, m3, m4, m6 (C1) and m1, m2, m3, m5, m6 (C2); routed to round 95 as a frozen-battery amendment.

## Round notes

- Stale-lane: progressing — one mission (launch 07:01:47, WAVE-DONE received); lane commits `6b65e7c1`, `4ae1678d`, `fa1af842` authored by `mori-shokunin`.
- Tool installs: none. `~/.omp/agent/RULES.md` was read; no install, update or pacman transaction was run by the L1 or any seat. Tools used: `curl`, `git`, `python3`, `bash` (all existing).
- Host: no sysctl, service or user was changed. Seats were instructed not to mutate host settings; none reported doing so.
- Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`, no pathspec): `.scratch/run15-state.json` (modified; orchestrator-owned, not touched) and `.ufo/l0-questions.md` (this round's L0 append, committed with this report). No seat wrote into the fleet root.
- `/tmp`: the first `plan` probe wrote `/tmp/plan-r94.json` and `/tmp/plan-r94.err` (under 1 KB each); both were removed. All later scratch lives under `/fast/scratch/hyaku/mori-r94/`, removed at round end.
- L0 questions appended: D1 planner binding (operator); sibling host-literal class (route to owners); C2 ruling (capability row or round-95 restatement).
- Open, not claimed: the digest-gate debt (31 prefix-only rows, S125 unpinned; round-93 contract P4) and the round-90 nonce guard (QUALITY 191).
- Counter-owned host path: closed for the round-94 counters only; round-93 counters keep the literal as frozen history (named).
- Pre-report gate: `git -C /home/vgpnk/Projects/shokunin/mori-shokunin ls-remote origin refs/heads/master` → `fa1af84211d17958ba2b931b362418bc8ecbe253`.

## SHONEN

Bounds: the four boxes of `SHONEN.md` (seed unchanged; no `[x]` claimed; no non-author verifier named).

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `corpus/QUALITY.md:2279-2303` (criteria 202–204 this round, with the battery and porcelain receipts); earlier pointers as in `SHONEN.md`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 94 (the C1 battery on the fixture commits; the round-93 counters re-run at `8edbb86d`, `.ufo/waves/round-94/evidence/rerun-r93-counters-at-8edbb86d.txt`).
- [~] Instructions executable by an agent without oral context — `python3 -I .ufo/waves/round-94/controls-r94.py <lane> <fleet>` (prints `EMBED_FALSE_PASS`, exit 0 at `fa1af842`; `evidence/controls-r94.txt`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `corpus/lessons/round-94.md` §Routed defects (sibling host-literal class routed via L0; no sibling edited); connector `w1/Mo94Conn01.md`.
