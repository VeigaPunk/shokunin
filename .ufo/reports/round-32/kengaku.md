# kengaku — round 32 (hyaku run 6, 2026-10-25)

Lane: `kengaku-shokunin` (novelty + calibration; LLM and model research and evaluation).
Baseline `f20a1097`; landed lane tip `bcd2a6c0d49e6c7d3c30307cf0cd43be6d9660d0` (confirmed by `jj-lane.sh push` landed output and remote tip).
Frozen prereg: `plans/round-32-claims.md`, freeze commit `0d32691d`.
Round shape: build wave 34 seats, falsify wave 34 seats. Duplicate `-3` build dispatch attempt was killed; the surviving registry carries 34 seats. Reports: `.ufo/waves/round-32/build/` and `.ufo/waves/round-32/falsify/`.

## Work performed

C1 coverage — shokuknow grader-semantics candidate; C2 calibration — seven routed defects; C3 freshness — public model catalogs. The falsify wave invalidated C1 admission and showed C3's frozen pass condition cannot honestly pass with the observed nonzero HF schema delta.

- **C1 assimilation refused.** The staged package contains candidate ids colliding with live registry identifiers: S094/S097 are already present; S101/S102 identify unrelated SWE-bench sources. No candidate was admitted. Four shaped rejected correction rows record those collisions. The draft entry remains unadmitted. Evidence: `corpus/evidence/round32/adoption-after.txt` and `FxEntryTruth.md`.
- **S094 source correction.** The executed tolerance is 0.05 at the call site, not the staged 0.1 default. The logging helper has caught-exception True paths, but credential failures can fall through to implicit None and fail closed. Entry and rejection text were corrected. Evidence: `.ufo/waves/round-32/falsify/FxFailOpen.md`, `FxTolerance.md`, `FxEntryTruth.md`.
- **C2 routed defects.** The round-31 CLI receipt uses `../../../../plans/`; SKILL.md has a sources-adopt registry row. R1/R2/R5/R6/R7 remain red: report phantom-hash erratum, final report ordering, R31FxEntryBar ledger, and lesson errata are incomplete. The lane report does not claim C2 closure.
- **C3 live probe.** Hugging Face returned 50 records with four fields absent from its default projection (`author`, `sha`, `lastModified`, `gated`); `?full=true` restores them. OpenRouter returned 467 records with all twelve recorded fields. Summary receipt: `corpus/evidence/round32/catalogs/after.txt`; independent probe: `.ufo/waves/round-32/falsify/FxC3DiffTruth.md`. This is an observed delta, not a successful freshness claim. C3 is **failed as declared**; its frozen predicate was not changed after scoring.

## Landed changes

Lane commit `bcd2a6c0d49e6c7d3c30307cf0cd43be6d9660d` contains the entry and catalog refresh drafts, registry rejection records, README/SKILL edits, CLI receipt, C3 counter/selftest repair, lesson and evidence receipts. The lane helper's `landed` output verified the remote tip.

The fleet report is being committed after the lane tip; its commit hash follows in the next post-commit measurement section.

## Before → after measurements

| Claim / probe | Before | Observed after | Verdict |
|---|---|---|---|
| C1 adoption | Freeze control: `entries=0 indexed=0 cited_rows=0 rows_present=0 rows_mined=0 usedby_ok=0 census=ok`, exit 1 | Draft collision detected; final census exit 0 after recording rejected rows. C1 not admitted. | **Refused as declared** |
| C1 content receipt | Draft second receipt `checks=6 defects=0` | This does not establish source admission; receipt `corpus/evidence/round32/c1-verify-after.txt` | Not an admission verdict |
| C2 defects | Freeze control `checks=7 defects=7`, exit 1 | Partial tree `checks=7 defects=5`, exit 1; R1/R2/R5/R6/R7 remain red | **Incomplete** |
| C3 catalog | Freeze control entry stale, exit 1 | Live probe `hf=ok openrouter=ok hf_models=50 or_models=467 hf_schema_delta=4 or_schema_delta=0`; counter selftest `SELFTEST checks=9 failed=0` | **Failed as declared** |
| Registry census | Baseline exit 0, 15 W04 | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku` → exit 0, 15 W04, no E findings | Clean |

## Sources & frontier

No assimilation sources were admitted. S094/S097/S101/S102 rejected rows are correction records for staged collisions; existing registry identities remain authoritative. The unadmitted C1 entry is not counted as expansion. The catalog entry records the probe but does not convert C3's failed frozen predicate into a frontier closure.

## Trend verdicts

- **expansion: held** — no admitted entry on uncovered ground.
- **quality: held** — drafts corrected and census clean after rejections; admission quality is not claimed.
- **discernment: improved** — seats found duplicate ids, an incorrect executed-tolerance statement, an overbroad fail-open claim, and an unsatisfiable C3 predicate before a false pass was reported (`FxEntryTruth.md`, `FxFailOpen.md`, `FxClassics.md`).

## SHONEN

- [~] SKILL.md decision aids — sources-adopt registry row added and corrected against reviewer evidence; no independent verifier of the landed commit yet.
- [~] End-to-end domain task executed and logged — pinned source reads and live catalog probe are recorded in wave reports and `corpus/evidence/round32/`; raw catalog JSON is not committed.
- [~] Instructions executable without oral context — claims, wave specs, counters, and receipts are committed, but C3 failed as declared and closure remains incomplete.
- [~] No cross-domain bleed — sibling connector found no contest (`FxConnector.md`); `PROVINCE.md` unchanged.

No box is `[x]`: no non-author has judged the committed landing.

## Stale-lane

Respawn-per-round lane. Lane tip `bcd2a6c0d49e6c7d3c30307cf0cd43be6d9660d` is pushed; remote tip matched at the gate.

## Disclosures, dead seats, open questions

- **Seats:** 34 build and 34 falsify seats in the surviving registries. Duplicate `-3` build jobs were killed; no duplicate report set is counted.
- **R31FxEntryBar:** missing report in the round-31 falsify registry; recorded as dead/unreported in `corpus/lessons/round-32.md`.
- **Open routed defects:** R1 phantom-hash erratum, R2 report ordering, R5 seat ledger, and R6/R7 lesson errata remain incomplete or need verification.
- **Open claims:** C1 candidate refused for collisions; C3 failed as declared; no post-score predicate change.
- **Tool installs:** none.
