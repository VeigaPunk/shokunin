# kaidoku — round 30 (attempt 1, hyaku in-session L1 `KaidokuR30`)

Lane `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, base `d210fb8fa62d2af04d009cfa0c65a4e8137dc742`, pushed tip `328ca4f4b1ed4b73dc47fceaf8d127ad31d0ddab` (`jj-lane.sh state`: local = remote, ahead 0, tracked 0, untracked 0). Dispatched 02:14Z.

## Work performed

Declared claims (frozen at `4ee65c67`, `.ufo/waves/round-30/claims.json`):
- **R30-C1 — coverage.** Surface: PROVINCE Core gains REA `inspect-rust-binary` on its positive input class, images that carry a cargo-auditable `.dep-v0` section, in ELF, PE and thin Mach-O. At the base, PROVINCE named the verb 0 times and every lane run of it had returned `auditable_metadata: null`.
- **R30-C2 — depth.** Surface: a SKILL.md decision table of the 6.5.0 reader's refusal signatures (exact messages, error codes, thresholds), predicted from the code and tested live on 19 mutants.

This round does repair first. It leaves the rejected streak (EVM naming in rounds 28–29, evidence-ID identity in round 27) and works a new surface.

- Repair of the round-29 spot-check defects (`SCORECARD.md` round-30 section, "Round-29 routed defects"):
  - **1–2 (axis misfit, target a control could meet):** mistake M30-1, QUALITY rows 48 and 50, `tools/round-30/axis-fit-gate.py`. It exits 1 on round 29 and 0 on round 30 after the controls. The pre-data control wave ran before any data.
  - **3 (M29-3):** an `instrument_supersessions` entry was appended to the round-29 claims.json (append-only, `w2/ReviewM293.md` holds). `tools/round-30/prefreeze-gate.py` makes the pre-freeze rule an exit code.
  - **4 (M29-1):** `tools/round-30/settle-gate.py`. `.ufo/waves/round-30/settle.tsv` returns `settle: PASS`.
  - **5 ("published" carriers):** corrections appended at PROVINCE, the round-29 entry, README, SCORECARD, LOG and `lessons/round-29.md`.
  - **6 (SCORECARD:3166):** a correction bullet was appended.
  - **7 (docstring):** not revised, because no round-29 counter was revised.
- Instruments were committed before the claims file. Commit `0dbabf78` holds the counters, the independent oracle `tools/round-30/rust_dep_oracle.py`, 16 frozen carriers from 7 official uv 0.13.0 PyPI wheels, and 19 frozen predictions. The freeze followed at `4ee65c67` (02:35:13Z). Before-receipts at `d210fb8f`: both counters exit 2 (`.ufo/waves/round-30/before/`).
- **Pre-data control wave w1 (39 seats).** Ten controls, each scored with the frozen counter. None met a target (`.ufo/waves/round-30/controls/receipts.tsv`, committed at `f39f4530` before the data):
  - C1, passes out of 16: do-nothing 0, junk-row 0, all-false 0, no-reader 0, id-keyed shortcut 1.
  - C2, matches out of 19: do-nothing, junk-row, generic-message, all-accept and rotated-messages controls 0; empty predictions refused (exit 2); predictions copied as observations 16.
  - Before data, seats traced all 19 predictions to the code and found agreement on each (`w1/RevPredRefuseA.md`, `RevPredRefuseB.md`).
- **Data** at `24da3459`: 16 C1 envelopes and 19 C2 envelopes from live `rea-agents@6.5.0`, run 02:59:33Z–03:01:50Z.
- **Falsify wave w2 (34 seats):**
  - Independent readers in every format group agree 16/16 (`w2/ReDerive*.md`).
  - Counter re-runs and separability checks hold (`ReRunC1`, `ReRunC2`, `SepC1`).
  - S089, S090 and S091 re-opened, all admitted.
  - The defects they found were fixed before filing:
    - C1 holds 7 dependency documents, not 5.
    - "Five architectures" corrected to 3 ISAs in 7 format×architecture pairs.
    - The SKILL table had a pipe that split a row, and its "exactly one" gate wording was wrong.
    - S090 cited the wrong `cli.js` path.
    - The refusal-count wording was wrong.
    - QUALITY rows 48 and 49 were too broad, so rows 50 and 51 supersede them.
- Frontier step: three SOURCES rows (S089–S091), mined mistakes M30-1 to M30-5 (`corpus/lessons/round-30.md`), and two sourced claims (C1 cites S089/S091, C2 cites S090).

## Landed changes

Every change below is tied to the LOG.md round-30 entry. All were landed through `jj-lane.sh`.

- `0dbabf78`: instruments and frozen inputs.
- `4ee65c67`: freeze (`claims.json`).
- `a6e7d9ce`: before-receipts and the wave-1 spec.
- `004053d6`: wave-1 reports, the three gates, the SHONEN pointer-drift fix (`PROVINCE.md:95-116` → `97-118`), and the round-29 M29-3 disclosure.
- `f39f4530`: control receipts in the gate's format.
- `24da3459`: data, both entries, the SKILL section and registry, the PROVINCE Core addition, README rows, SOURCES S089–S091, the round-29 corrections, and the l7-02 pointer.
- `92b1dd2d`: SKILL lead-line fix (M30-4), lesson, QUALITY rows 48–49.
- `3502b94c`: SCORECARD round-30 section, LOG entry, wave-2 spec.
- `39fbad9d`: wave-2 reports and fixes, QUALITY rows 50–51, settle ledger, round-30 freeze-ledger rows, and the Core-admission ids in LOG.
- `328ca4f4`: tip receipts.

## Before → after measurements

| claim | counting command | before (`d210fb8f`) | after |
|---|---|---|---|
| R30-C1 | `python3 -I -B tools/round-30/c1-rust-positive.py --root <LANE> --rev <REV>` | exit 2 `PIN pinned input absent` | `carriers=16 pass=16 target=16 entry_ok=1 province_ok=1`, exit 0, at `24da3459`, `92b1dd2d` and `39fbad9d` (`after/c1-rust-positive-at-tip.txt`) |
| R30-C2 | `python3 -I -B tools/round-30/c2-rust-refusals.py --root <LANE> --rev <REV>` | exit 2 (predictions absent) | `mutants=19 matches=19 target=19 entry_ok=1 skill_ok=1`, exit 0, at `92b1dd2d` and `39fbad9d`. At `24da3459` it printed `skill_ok=0`, exit 1 (M30-4: the SKILL line lacked the verb/entry pair; the receipt is kept) |

Unmoved command (C1): `git show <REV>:PROVINCE.md | grep -c inspect-rust-binary` gives 0 at the base and 3 at `92b1dd2d`. Recipe A gives 114/114 → 116/116 mapped, with depth 17/17 (`w2/ReviewRecipeA.md`).

Gates at the tip:
- `axis-fit-gate` exit 0.
- `prefreeze-gate` CLEAN.
- `settle-gate` PASS.
- `tools/round-29/prefile-check.sh`: `prefile: tree clean`, both freeze ledgers exit 0, `prefile: PASS`, exit 0 (rerun after committing the tip receipts). The first run was red only on those untracked receipts; that output is committed at `328ca4f4`.

## Sources & frontier

SOURCES rows go from 88 to 91 (`grep -cE '^\| S[0-9]{3,} \|' corpus/SOURCES.md`). The three new rows are all tier A:

| row | kind | source |
|---|---|---|
| S089 | docs | cargo-auditable README, PARSING.md and schema at commit `e2316a67` |
| S090 | code | rea-agents 6.5.0 tarball `531717a0…` |
| S091 | dataset | PyPI uv 0.13.0 JSON `2eaed6c8…` |

No existing row was touched. The S090 anchor was corrected after wave 2: `dist/cli-runtime/cli.js:5176-5218`; the change is logged in the lesson Gate.

Census, run with `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`:
- Round start: `kaidoku ok`, six W04 warnings, exit 0.
- Round end: `kaidoku ok`, exit 0, with the W04 warnings unchanged plus a new one: S090 and S083 share the same tarball URL with different scopes.

Frontier advanced: positive-class Rust dependency metadata (`.dep-v0`) moved into Core. The PROVINCE Frontier list itself is unchanged.

## Trend verdicts

- **expansion: improved.** A surface was newly governed: the positive class of `inspect-rust-binary` on 3 containers and 3 ISAs. Knowledge files 114 → 116 and SOURCES rows 88 → 91; wave 2 re-opened all three new rows.
- **quality: improved.** Eleven seats re-derived the data or re-ran the counters, and none produced a counterexample. Wave-2 defects were fixed in the entries and the SKILL table before filing. QUALITY rows 50–51 narrow rows 48–49 instead of overclaiming. Known open weaknesses are disclosed in the entries:
  - M30-3: C2's committed-refusal clause compares only `ok`.
  - The doc gates are token checks.
- **discernment: unprovable-but-better.** Before data, the control wave caught counter weaknesses and wrong-wording risks, and the lane corrected its own miscounts ("5 documents", "five architectures"). This is still an author-side assessment until the outside spot-check.

## SHONEN

- [~] Decision tables / error patterns / cited sources: `SKILL.md` round-30 section. It is a 19-row refusal table checked live, backed by S090 (`corpus/knowledge/2026-10-23-r30-rust-auditable-refusals.md`).
- [~] End-to-end domain task logged: the LOG.md round-30 entry, with Core-admission evidence ids and subject sha256.
- [~] Executable instructions: the recheck commands in both entries; independent seats in w2 re-ran them (`ReRunC1.md`, `ReRunC2.md`).
- [~] No cross-domain bleed: `SHONEN.md:12` pointer refreshed to `PROVINCE.md:97-118`. Sibling scans found overlap only as cite-not-absorb (`w1/ConnSiblingsRust.md`, `w2/ConnFleetOverlap2.md`).

## Gate

Real rejects, with reasons:
- The SOURCES draft kind `registry` for S091 was rejected (E05, not in the enum) and changed to `dataset`.
- The S090 citation `cli.js` was rejected as the wrong file, because a different `dist/cli.js` exists (`w2/ReopenS090.md`).
- A second cargo-auditable row for the master copy was not made, because that copy was not opened separately.

## Round shape, seats, holds

- **Shape:** default, two v1 waves.
  - w1: 39 seats (scribe 9, mutation-tester 8, critic 7, reviewer 7, executor 4, scout 2, connector 1, sentinel 1). All 39 returned.
  - w2: 34 seats (reviewer 21, critic 6, mutation-tester 4, sentinel 1, scout 1, connector 1). 29 returned.
  - Round total: 73. No residual call.
  - Planner seat: held by the L1. The planning data-walk rode the w1 scouts and connector.
- **Dead seats (not replaced):** w2 `CriticAxisC1After`, `CriticHonesty` and `CriticAxisC2After`. Each failed with `Cloud Code Assist API error (429) … Individual quota reached … RESOURCE_EXHAUSTED` (gemini-4-argon).
- **Cancelled at wrap-up:** w2 `CriticControlsAfter` and `ScoutMisroot`. Their findings were not integrated. The L1 ran the misroot sweep itself: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed no untracked file naming kaidoku round 30.
- **Mistake M30-2:** a w1 seat's `llvm-objcopy --dump-section` without an output file rewrote 4 carriers in place. The C1 pin check caught it with exit 2. The carriers were restored and set `chattr +i` before any counted data.
- **Hold:** item `U064N008Hf47eb933` remains held and untouched.
- **L0 questions:** none.
- **Tool installs** (official channel `uv tool`; to obtain more cargo-auditable carriers, which did not pan out): `ty` 0.0.91 installed and `ruff` already present; neither binary carries `.dep-v0`. One w2 seat installed `cmarkgfm` 2025.10.22 into a scratch uv venv. No pacman transaction.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
