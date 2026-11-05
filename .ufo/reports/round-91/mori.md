# mori — round 91 report (L1 MoriR91, attempt 1)

Lane: mori-shokunin, branch `master`. Entering revision `79eaa8cfe5e0b9b1c5ff45f524199d4a123f0520`.
Contract commit `e02b8a39` (frozen before any wave output). Lane HEAD after the round's landing:
`bee9f21e18db79ca27493b1453a9543f1994d59f` (`git ls-remote origin refs/heads/master` prints the same).
Outcome: honest stop. Both declared claims were **not admitted**; the round landed a digest-class gate,
two source rows and the round's mistake lesson.

## Work performed

Declared claims (frozen in `.ufo/waves/round-91/contract.md`; SCORECARD `## Round 91`):

- **C1 — calibration (score 5, lowest non-retired):** the round-87 receipt gate's four unarmed clause
  families (`c2-replay-compare-off`, `c2-supersede`, `c2-absent`, `c2-defeated-accounting`) get selftest
  arms, killed by an independent and a lane-declared mutant population with family-prefixed attribution.
  Verdict: **not admitted** — P1 (`Mo91E01Arms`) and P2 (`Mo91M01Mut`) returned no output.
- **C2 — freshness (score 5, lowest non-retired):** a dated census snapshot of the round-86 value channel
  re-derived from committed raw inputs. Verdict: **not admitted** — the snapshot and counter seat
  (`Mo91E02Snap`) returned no output; `snapshot=absent` at the entering revision and at `bee9f21e`.

Work items, each with its evidence pointer:

- Load order read: `skill://shokunin`, kimi-shokunin `SKILL.md`, `MISSION.md`, `AXES.md`, the lane
  `SCORECARD.md` (`## Axes`, `## Planned (round 91)`), `SHONEN.md`, `corpus/lessons/round-90*.md`,
  `corpus/README.md ## Frontier`, and the round prompt `.ufo/prompts/mori-round-91.md` (sections 1–6).
- Claim choice: scores coverage 6, operability 7, depth 5, freshness 5, calibration 5, adjacency 6
  (`SCORECARD.md` `## Axes`). Two claims on the two lowest axes that the round-90 plan carried (calibration,
  freshness); operability (nonce guard) and depth (pin supersession) carried, not claimed. Contract
  `.ufo/waves/round-91/contract.md` (commit `e02b8a39`).
- Wave validation: `ufo-swarm-wave.mjs plan` rc 0 and `run` rc 0 under `scripts/hyaku/ufo-wave-policy.json`
  (v1 band 8–16); dispatch `.ufo/waves/round-91/w1-dispatch.json` (schema `ufo-swarm-wave-dispatch-v1`,
  12 spawn seats, no residual call). Ready handoff `.ufo/waves/round-91/w1.ready` taken at 02:17:33
  (`w1.ready.dispatched`). WAVE-DONE received; results `.ufo/waves/round-91/w1-results.json`.
- Seat outcomes (`w1-results.json`, `w1/*.md`):
  - `Mo91E03C1Ctr` (executor): C1 counter `w1/candidates/count-c1.py`, sha256
    `cc599626bb09851bf07eed82886aa725a3fe5815483e3d5ba255b5e12ebce1f9`; selftest 14/14 (report §Selftest).
    Fixture run found that the subject's supersede labels are `supersede_*`, so `c2-supersede` reads
    `isolated` (report §Fixture run).
  - `Mo91E04Digest` (executor): digest checker `w1/candidates/digest-check.py`, sha256
    `a692b159646e8979f9fc95d5eee82a9a30cee4d8f67432ee824fff7e9d30cee7`; at the entering registry
    `DIGEST_CHECK rows=121 ok=87 mismatch=2 prefix_only=31 unpinned=1`, exit 1; able-to-fail by a flipped
    S490 digest (`mismatch=3`, exit 1) (report §Able-to-fail).
  - `Mo91S01Pins` (scout): `w1/candidates/pins.txt`, the receipts that pin the round-87 arm count.
  - `Mo91R01Atk` (reviewer): `ATTACK C1 forger-accepted=3 rejected=1` (`w1/Mo91R01Atk.md`).
  - `Mo91R02Atk` (reviewer): `ATTACK C2 forger-accepted=6 rejected=4` (`w1/Mo91R02Atk.md`).
  - `Mo91Sc01Src` (scribe): opened S617 (Jia & Harman, TSE 2011, course-hosted PDF) and S618 (SRE book
    ch. 6); rows in `w1/candidates/SOURCES.rows.md` (`w1/Mo91Sc01Src.md`).
  - `Mo91Sc02Lesson` (scribe): mistake row, the captured-by sweep and the S235 finding
    (`w1/Mo91Sc02Lesson.md` §1–§2).
  - Dead, empty output and null status/note, not replaced: `Mo91E01Arms` (executor), `Mo91E02Snap`
    (executor), `Mo91M01Mut` (mutation-tester), `Mo91K01Conn` (connector), `Mo91C01Ctl` (critic).
    Recorded as an L0 question (`.ufo/l0-questions.md`, line appended with this commit).
- L1 verification of the seat outputs (own commands, recorded in `.ufo/waves/round-91/evidence/controls-r91.txt`):
  - S617 re-opened: `curl -sSL` (final URL unchanged, PDF bytes), sha256 `056ac9b99410321c7cb80a29284c4ca106456e1a0cf64b6f4d633ba83edff342`,
    pdftotext raw text, `grep -c -F` of the located opening = 1.
  - Digest tool copy: `tools/mori-source-digest.py` sha256 matches the seat's `a692b159…`; run from the
    lane root on the committed registry it prints the same `DIGEST_CHECK` line as the seat.
  - Corrections of record measured by `sha256sum` on the pinned bytes (see Landed changes, C-1 and C-2).
- Frontier census (protocol §2b): registry rows 389 before, 391 after; S617 admitted (`mined`), S618
  rejected with reason and flip (`rejected`); knowledge entry `corpus/knowledge/calibration-arming-r91.md`
  cites S617 only.
- Mistake mined: `recorded-digest-unverified` (R8 and S235), with four further classes in
  `corpus/lessons/round-91.md` `## Mistakes` (frozen-family-label-mismatch, attack-found forgers in the
  frozen predicates, wave-seat-silent-death, correction-held-append-only).
- Stale leftover removed: `w1/candidates/calibration-arming-r91.md` (an untracked seat draft with
  `QUOTE-PENDING` markers, superseded by `corpus/knowledge/calibration-arming-r91.md`, which carries the
  located quote). Not committed.

## Landed changes

| Change | Commit | Tied log entry |
|---|---|---|
| Frozen contract, claims C1 and C2, kill rule, do-nothing predicates | `e02b8a39` | `LOG.md` `## Round 91` (declaration, SCORECARD `## Round 91`) |
| Wave `w1` evidence (spec, dispatch, results, ready marker, seat reports, candidates `count-c1.py`, `digest-check.py`, `pins.txt`, `SOURCES.rows.md`), controls receipt `evidence/controls-r91.txt` | `bee9f21e` | `LOG.md` `## Round 91` |
| `tools/mori-source-digest.py` (R8 detection gate; QUALITY 193) | `bee9f21e` | `LOG.md` `## Round 91`; `corpus/QUALITY.md` `## Criteria added round 91` |
| `corpus/SOURCES.md` rows S617 (mined) and S618 (rejected) appended after S616 | `bee9f21e` | `LOG.md` `## Round 91` |
| `corpus/knowledge/calibration-arming-r91.md` (source S617) | `bee9f21e` | `LOG.md` `## Round 91`; `corpus/README.md` `## Round-91 knowledge addition` |
| `corpus/lessons/round-91.md` (mistakes, gate, corrections of record C-1, C-2, C-3) | `bee9f21e` | `LOG.md` `## Round 91` |
| `corpus/README.md` round-91 frontier note | `bee9f21e` | `LOG.md` `## Round 91` |
| `SCORECARD.md` `## Round 91` (claims, verdicts, instruments, planned round 92) | `bee9f21e` | `LOG.md` `## Round 91` |
| `LOG.md` `## Round 91` | `bee9f21e` | this entry |
| `.ufo/l0-questions.md` line for mori round 91 (dead seats) | fleet commit, this report | — |

Corrections of record (append-only; registry rows not rewritten):

- **C-1** — S615 recorded digest `7891c58897fe9f78cf16d15fd3464b746a187214c82587ac94b8f1a60ad1a6f0`; full
  sha256 of its pinned copy is `7891c58897fe9f78cf16d15fd3464b746a187214c82587ac94b0f83b9a8a42f5`.
- **C-2** — S235 recorded digest `9855a4986a312dfc946b1b97b6010a8e4f1e65a4a30cda99359e6df057ad8020`; full
  sha256 of `corpus/evidence/sources-r42/S235.pdf` is `9855a4986a312dfc946b1b97b6010a8e4f1e65a4a30dca99359e6df057ad8020`.
- **C-3** — S156, S158, S159 mismatch against id-named copies; not classified this round.

Not landed (declared, not admitted): the C1 arms and the P1/P2 populations; the C2 snapshot and counter.

## Before → after measurements

Counting commands were run at the entering revision (before) and at the landing commit (after). Both
claims stay unmeasured after the round because their populations and counter did not return.

- **C1 (calibration).** Command: `python3 -I .ufo/waves/round-91/w1/candidates/count-c1.py 79eaa8cfe5e0b9b1c5ff45f524199d4a123f0520 --repo <lane> --scratch <scratch>`.
  Before (`79eaa8cf`): `C1_SETUP p2 population absent: …/mutants-c1-independent.json`, exit 2.
  After (`bee9f21e`): not re-run; the populations are absent at `bee9f21e` (`git ls-tree -r --name-only bee9f21e .ufo/waves/round-91/` lists neither file). Verdict: not admitted.
- **C2 (freshness).** Command: `git cat-file -e <rev>:corpus/evidence/value-census-2026-11-05.txt`.
  Before (`79eaa8cf`): absent. After (`bee9f21e`): absent. Verdict: not admitted.
- **Digest class (instrument, detection).** Command: `python3 tools/mori-source-digest.py <registry> <pinned-dir>` on the entering registry (scratch tree mirroring `79eaa8cf`): before `DIGEST_CHECK rows=121 ok=87 mismatch=2 prefix_only=31 unpinned=1` exit 1; after (`bee9f21e`, same registry rows, the gate does not repair): identical line, exit 1. The gate's detection on a flipped digest: `DIGEST_CHECK rows=121 ok=86 mismatch=3 prefix_only=31 unpinned=1` exit 1 (scratch copy only).
- **Registry (census).** Command: `grep -cE '^ {0,3}\| *S[0-9]{3,}' corpus/SOURCES.md` → 389 at `79eaa8cf`, 391 at `bee9f21e`. `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori` → exit 0 before (`mori ok`; 40 `W04` warning lines) and exit 0 after (`mori ok`; 41 `W04` lines; the one added is `mori W04 S618 duplicate url sre.google/sre-book/monitoring-distributed-systems across scopes`, a warning, not an error).

## Sources & frontier

- `SOURCES.md` rows before → after: **389 → 391** (counting command above; census exit 0 before and after).
- Rows added by tier: **A: 2** (S617 `paper`, status `mined`, used-by `corpus/knowledge/calibration-arming-r91.md`; S618 `docs`, status `rejected`, reason and flip recorded in the row).
- Rows touched old → new: none. No status, recheck or used-by changed on an existing row.
- Frontier: the digest class moved from "unverified" to "gated by a tool" (`tools/mori-source-digest.py`), with 121 in-scope rows measured. Not advanced: the calibration arms, the freshness snapshot.
- Sourced claim: the knowledge entry cites S617 with a located quote (re-checked by the L1 on 2026-11-05).
- Gate detail: `corpus/lessons/round-91.md` `## Gate (sources, protocol §2b)`.

## Trend verdicts

- **expansion — improved.** Evidence: one admitted registry row (S617, `mined`, cited by the knowledge entry), one rejected row with a flip condition (S618), one knowledge entry on the calibration ground (`corpus/knowledge/calibration-arming-r91.md`). Census exit 0 before and after; 389 → 391 rows.
- **quality — improved.** Evidence: a registry-digest check that fails on R8 and S235 at the entering registry and fails on a one-character flip (`mismatch=3`, exit 1), QUALITY 193, corrections of record C-1 and C-2 measured on pinned bytes. No harm measured (no admitted gate was weakened; no score changed).
- **discernment — unchanged.** Evidence: two attack seats found forgers that the frozen wording accepts (C1 3/4, C2 6/10), a real improvement of the lane's ability to see its own predicates' reach; but no claim was admitted or measured, so the lane's calibrated discernment verdict is unchanged. The forgers are the round-92 input (`corpus/lessons/round-91.md` `## Mistakes`).


## SHONEN
- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer `SKILL.md` (round-54 and round-53 tables, unchanged this round); not checked by a non-author this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer `LOG.md` `## Round 91` (digest check run end-to-end on the registry; the claims themselves did not complete).
- [~] Instructions executable by an agent without oral context — pointer `tools/mori-source-digest.py` (usage: `python3 tools/mori-source-digest.py <SOURCES.md> <pinned-dir>`; `evidence/controls-r91.txt` shows the commands and outputs).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer `corpus/knowledge/calibration-arming-r91.md` §3–§4 (limits; S618 not cited).

## Round shape, seats and routing

- Shape: one v1 wave, `w1`, 12 spawn seats (band 8–16, `ufo-wave-policy.json`); no residual call; round total 12 seats.
- Role mix (`w1-results.json`): executor 4 (`Mo91E01Arms`, `Mo91E02Snap`, `Mo91E03C1Ctr`, `Mo91E04Digest`), scout 1 (`Mo91S01Pins`), reviewer 2 (`Mo91R01Atk`, `Mo91R02Atk`), critic 1 (`Mo91C01Ctl`), mutation-tester 1 (`Mo91M01Mut`), connector 1 (`Mo91K01Conn`), scribe 2 (`Mo91Sc01Src`, `Mo91Sc02Lesson`).
- Attack share: 4 of 12 = 33 % (reviewer ×2, critic, mutation-tester), ≥25 % met. Connector seats: 1.
- Planner: held by the L1 (the planner role is frozen-topology and not a swarm role). The planning data-walk was done by the L1 from the scout's pin map.
- Dead seats: five (`Mo91E01Arms`, `Mo91E02Snap`, `Mo91M01Mut`, `Mo91K01Conn`, `Mo91C01Ctl`), each with empty output and null status/note in `w1-results.json`; not replaced.
- Routing: the route is the operator's `task.agentModelOverrides`; no model was passed. Seats' actual answering models were not recorded in the results file, so no claim here depends on one.

## Inherited state and misroot sweep

- Earlier attempts: none for round 91 (`.ufo/watchdog.log` shows one `launch mori round=91 … attempt=1` line, no `lane-dead-no-report mori round=91`).
- Uncommitted lane leftovers: none after the landing (`git status --porcelain` in the lane is empty). The one leftover, `w1/candidates/calibration-arming-r91.md`, was removed (see Work performed).
- Fleet root sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `M .scratch/run15-state.json`, `A mo.tip` (empty file, not created by a mori seat) and `M .ufo/l0-questions.md` (this round's line). The first two are orchestrator-owned or foreign and were not touched. No mori seat wrote a file into the fleet root this round (the seats' `Report:` trailers resolved under the lane).

## Stale-lane

Stale-lane: no. The round driver is respawn-per-round; no other mission of this lane is open.

## Tool installs

None. Read `/home/vgpnk/.omp/agent/RULES.md`. Used pre-installed `git`, `curl`, `pdftotext` (poppler), `python3`, `sha256sum`. No pacman, no uv, no npm installs. The `sources-census.sh --selftest` invocation I tried returned rc 2 (argument error on my side); it is not cited as evidence.

## Open questions

- L0 (`.ufo/l0-questions.md`, appended with this commit): spawn/stop reason for the five empty seats; whether the results handoff should carry it per seat.
- Round 92 decisions (not asked, carried in SCORECARD `## Planned (round 92)`): C1 and C2 must be re-declared with the attack rules before their controls commit; S615/S235 corrections need an appended supersession row, not an in-place rewrite.
