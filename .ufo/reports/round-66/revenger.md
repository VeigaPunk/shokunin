# revenger round 66 report — attempt 1 (frozen-order adjudication)

Lane: revenger · repo: `/home/vgpnk/Projects/shokunin/revenger-shokunin` · round tip: `8362a23538b1683dd0b6fac8a61389b412744188` (pushed, ahead=0, working tree clean) · base: `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0` · measured revision: `a4c712a082ff18a6f8ac0713fd35ad43a766a9f5` (measure-after receipt committed as `8362a235`).

**Stale-lane:** no — respawn-per-round driver; no other mission of this lane is open.
**Tool installs:** none (no package installed or updated; python3/git/node used read-only).

## Work performed

Declared claims (frozen at `reports/round-66/claims.md`, pre-registered `16b9387b`):

- **C1 — coverage, the frozen round-65 admission order executed (lowest non-retired criterion):** adjudicate the orchestrator-dispatched 64-seat round-65 wave's decisions on the C05 APK candidate and flip the README row either way per `reports/round-65/claims.md:110-123`, then re-measure on the committed tip. **Verdict this round: r65 C1 FALSIFIED → C05 flipped `frontier → uncovered`; candidate marked `admission-status: rejected` and retained.**
- **C2 — calibration, new criterion C6 (exit_code / fixture_sha256 receipt guards):** `C6_RECEIPT_KILLED_ATTRIBUTED` 0/4 → 4/4 via two in-script forged controls per receipt script. **Verified this round.**

Work items:

- Re-verified every named fresh-seat decision against committed bytes at the claim base: three FAILs reproduced by command — `python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]'` prints `payload_first16_hex 4d616e69666573742d56657273696f6e` vs the entry's recorded `4d616e696673742d56657273696f6e` at `corpus/knowledge/round-65-apk-axml-byte-evidence.md:41` (15-byte `Manifst-Version` vs 16-byte `Manifest-Version`); `RES_XML_RESOURCE_MAP_TYPE` sits at ResourceTypes.h:253 outside the cited :239-250; the S039 quoted anchor is snapshot lines 7-8, not line 5 (`older server.`). Every PASS decision confirmed consistent; `R65SpotcheckDiscern` = REJECT at current bytes.
- Executed the falsification branch: `corpus/README.md` C05 coverage row `frontier → uncovered` naming `fixtures/apk-r65` and the retained rejected candidate; `## Frontier` C05 prose refreshed in the same revision; the candidate kept every byte except its `admission-status:` line.
- C6 patch: two controls per script appended after the forged-evidence control in `corpus/verify_icon_languages.py:158-163` and `corpus/verify_multi_icon_states.py:157-162` (deep-copy receipt → forge `exit_code`=1 / `fixture_sha256`=H(b'') → `require(not receipt_ok(...))` ending `forged receipt exit|fixture accepted`); 6 insertions / 0 deletions each, `receipt_ok` untouched, unmutated self-tests green.
- Committed the round-65 wave evidence corpus (64 seat reports + spec + briefs + snapshots + validated plan) and the round-66 verification spec (64 seats, `ufo-swarm-wave.mjs plan` exit 0 under `scripts/hyaku/ufo-wave-policy-v2.json`) — prepared-but-undispatched per the accepted host mapping.
- Registered dispositions in the same revision: S042 (wave corpus, own-work) + S043/S044 (supersede S039/S040 — correction by new row, contract rule 2); stale `candidate` headers on the round-63/64 admitted entries repaired to `admitted`; SOURCES `## Search log` retro r65 note + r66 note; SKILL.md round-66 refresh (header verified-at + M37–M41 rows, §6.1 counter repoint, §6.4 apk-r65 regen warning, §6.5 gate update, §7 pointer rows).

## Landed changes

| commit | content | LOG.md entry |
|---|---|---|
| `16b9387b` | pre-registration `reports/round-66/claims.md` + frozen counter `measure.py` (sha256 `a59914e9…1da`) + `measure-before.log` | "Round 66 declaration — frozen-order adjudication round" |
| `a4c712a082ff18a6f8ac0713fd35ad43a766a9f5` | C05 disposition (README flip + rejected marker), C6 controls both verifiers, S042–S044, header repairs, `.ufo/waves/round-65/` evidence corpus + `.ufo/waves/round-66/` spec, `corpus/lessons/round-66.md`, SKILL.md refresh | "Round 66 adjudication and disposition" |
| `8362a23538b1683dd0b6fac8a61389b412744188` | `reports/round-66/measure-after.log` + `LOG.md` + `SCORECARD.md` round-66 sections | "Round 66 measurement and trends" |

Harms sweep over the full round diff (`git diff --name-status 8214e4dd..8362a235`): only round-66 paths; `corpus/fixtures` and `corpus/live` byte-identical (empty numstat — round-66 registers no new fixture/live paths); README delta limited to the named C05 row + its `## Frontier` paragraph; verifier patches 6 insertions / 0 deletions each; `QUALITY.md`, `SHONEN.md`, `PROVINCE.md` untouched; knowledge diffs limited to each entry's `admission-status:` header line.

## Before → after measurements

Counting command (frozen): `git archive <commit> corpus | tar -x -C <tree>` then from `/`: `TMPDIR=<lane-owned> python3 -B reports/round-66/measure.py <tree>`.

- **C1 (frozen order):** `K_ROW C05 status=frontier` → **`uncovered`**; `C05_REJECTED_MARKED` `no` → **`yes`**; `README_TOKEN_LEGEND_MISMATCH` `0` → `0`; `K_HELD`/`K_HELD_BACKED`/`STRICT` 8/14 → 8/14 — honest: falsified-candidate ground moves to uncovered, not held. Measured: before `8214e4dd…` (`measure-before.log`), after `a4c712a0…` (`measure-after.log`), probe exit 0.
- **C2 (claim):** `C6_CONTROL_PRESENT` 0/4 → **4/4**; `C6_CONTROLS_PASS` → **4/4**; `C6_RECEIPT_KILLED` → **4/4**; `C6_RECEIPT_KILLED_ATTRIBUTED` 0/4 → **4/4** (attributed markers `forged receipt exit accepted` / `forged receipt fixture accepted`). Every `receipt_ok` conjunct on both ledgers is now mutation-covered (C3–C6 complete).
- Holds: C2/C3/C4/C5 attributed 2/2 each, `HOLD_CALIBRATION` 4/4, `HOLD_REPLAY` 10/10, `FRESH_ROWS` 18/18, `F_COVERAGE` 5/8, `STRICT_REJECT_WINDOW_SELFTEST=pass`, `HOLDS_OK_V4=yes` (`no` at base), probe exit 0.

## Sources & frontier

Census command: `scripts/sources-census.sh validate --today 2026-10-24 <lane>` — **round start: exit 0** (41 rows); **round end: exit 0** (44 rows; same four disclosed W04s S024/S028/S029/S034). Rows added: S042 own-work **mined** (the r65 wave finding corpus, 64 reports re-read as adjudication authority); S043 **queued** supersedes S039 (corrected REA route-scope anchor, snapshot lines 7-8); S044 **queued** supersedes S040 (corrected zipfile-docs title 3.15.1). No prior row's status/tier/used-by changed. Frontier rows advanced: C05 moved `frontier → uncovered` — the adjudicated honest state: authored evidence exists and is retained, but the candidate was falsified and no held ground is claimed.

Frontier-step items: census before→after recorded; mistakes mined M39 (number-drift — the transcribed hex pair the wave's Q-gate caught), M40 (located-quote pointers stated from intent in the r65 lesson), M41 (attribution — the r65 report's "scribe 3" vs committed spec's scribe 4); each with capture path and fix shape in `corpus/lessons/round-66.md`.

**Round shape (accepted host mapping):** this seat prepares waves; the orchestrator dispatches between rounds. This round the *incoming* artifact was the orchestrator-dispatched 64-seat r65 wave (committed as evidence); the *outgoing* artifact is one v2-band verification spec, 64 seats, `plan` exit 0, committed at `.ufo/waves/round-66/` — zero seats dispatched in-seat, reported as the mapping, not a conformance defect. §3 planner seat held by the L1; no lane-side seat count claimed.

## Trend verdicts

- **expansion: honestly recorded, unchanged-held** — C05 adjudicated to `uncovered`; `K_HELD` 8/14 at both ends (no inflation from the falsified candidate; the fixture/oracle/readout evidence is retained for the re-gate).
- **quality: improved** — the last unguarded receipt conjuncts (`exit_code`, `fixture_sha256`) now carry in-script forged controls with attributed kills on both scripts; calibration ledger complete C3–C6; rejected-candidate retention and stale-header repairs keep the ledger honest.
- **discernment: improved** — the r65 Q-gate did its job (byte-reproducing checks caught a one-byte-pair transcription error that authoring missed); the fleet's correction-by-new-row rule repaired S039/S040 without rewriting history; the round-65 seat-mix erratum is recorded.

## Routed forward (carried, non-blocking)

C05 re-gate path (all text-level repairs, named in lesson §Routed item 6): entry:41 hex pair, dex-header spec row + S043 route-scope source, item-8 provenance sentence, item-9 dex semantics row, Q-map pointers. AST-bound mutation counter + README label-spoof surface; generator conditional-symlink note; evidence-ID prongs (a)/(b)/(d) + injectivity registry; endswith-attribution asymmetry; recheck-pin H1–H3; SHONEN box 1 `[x]` non-lane re-confirmation (r64/r65 D3, unchanged); r58/59 PASS-count quotes. The committed `.ufo/waves/round-66/` 64-seat verification spec awaits orchestrator dispatch.
