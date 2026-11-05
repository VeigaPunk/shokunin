# revenger — round 92 report (hyaku run 15, attempt 1)

**Lane:** `/home/vgpnk/Projects/shokunin/revenger-shokunin` · **Lane tip (pushed):** `b4ee0b16c82e08d075e7177bc0b977f92ef2d8e6` (`git ls-remote origin refs/heads/main` returns the same hash) · **Freeze:** `9402183a9492428fa0064d250746c62a0a2d9ca5` · **Landing:** `2760f32ba2a855a3919d7d93f962754bccd81b7b` · **Adjudication:** `1a520c9e30ad1afb679e2ca386c6bc0ab8f8db9a` · **Round shape:** one v1 wave, 10 seats (`ufo-wave-policy.json`, band 8–16), attack seats 4/10 = 40 %.

## Work performed

**Declared claims (2, frozen before any seat ran; `reports/round-92/claims.md`):**

1. **C1 — coverage, the lowest non-retired axis** (K 8/15 = 5.3): coverage-map row C03 (managed (.NET/CLI) assemblies) moves `frontier` → `held` on one admitted knowledge entry; `K_HELD_BACKED` 8/15 → 9/15. Counter: `reports/round-92/c1_k_admit_counter.py`.
2. **C2 — calibration** (self-assessment vs repo state, class M36): the legend probe's mismatch set `['C03','C08']` → `['C03']` by moving C08 `frontier` → `uncovered`. Counter: `reports/round-92/c2_legend_counter.py` (runs the unmodified frozen probe `reports/round-66/measure.py`).

No exploratory claim. Both claims are axis moves on distinct axes.

**Work items (evidence pointer on each):**

- Round-start census: exit 0, 31 W01/W04, 0 E — `reports/round-92/census-round-start.log` (commit `9402183a`).
- Pre-freeze control runner and six control receipts (do-nothing ×2 fail, junk ×3 fail, positive pass) — `reports/round-92/controls/run_controls.py`, `controls/*.log`; run before any seat was dispatched; `CONTROLS_UNEXPECTED=0/6`.
- Wave `revenger-r92-w1`: spec `.ufo/waves/round-92/w1-spec.json`, validated `w1-plan.out` (exit 0) and dispatched `w1-dispatch.json` under `scripts/hyaku/ufo-wave-policy.json`; handoff `w1.ready` taken (`w1.ready.dispatched`); `WAVE-DONE` received; results `w1-results.json` — **10 of 10 seats settled, 0 dead seats.**
- Quarantine-first verdicts (wave-4 duty, which r91 skipped; `grep -c -i quarantin corpus/lessons/round-91.md` → 0): `ScoutR92Quarantine/verdicts.tsv` — 26 register rows: 24 `candidate-present`, 2 `unverifiable`, 0 `refuse-absent`. Adoption stays closed (`merge/revenger/` remains in 155/155 id collision; L0 `revenger | round-91` unanswered).
- Managed-format sources S491–S494 (ECMA-335 6th and 5th edition PDFs; PE Format CLR-header row; `MetadataRootBuilder` remarks), each opened 2026-11-05, quotes re-located byte-exactly in `ScoutR92Managed/snapshots/` (`sources.md`, 221 lines).
- Entry `corpus/knowledge/round-92-managed-assembly-metadata-evidence.md` drafted by `ScribeR92Entry`; READY digest `2c96e633fc730d218560b9693b881ffdeb1244cad5ac77f5fb6626f494306fb6` (`w1/ScribeR92Entry/READY`); lint `corpus/lint_entry.py` exit 0 (`LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0`); embedded `corpus/check_embedded_outputs.py` exit 0 (11 blocks, 0 problems).
- Producer trial (`ExecR92Producer`): `npx rea-agents@6.8.0` (host `rea` is 6.7.0; channel and reason recorded in the seat report) — two runs byte-identical to each other; both differ from the committed record only in `evidence_id` and the local-path fields (`w1/ExecR92Producer/comparison.txt`).
- Legend cross-check (`ExecR92Legend`): probe reproduced independently (`rows=['C03','C08']`); the round-77 CDP record audited: no rejection or quarantine marker, receipt exit 0 — work evidence, so `uncovered` is the legend-correct token (`legend-crosscheck.md`).
- Blind derivation (`ReviewerR92Blind`): an independent parser over fixture bytes only; zero mismatches against every fact the entry states (`w1/ReviewerR92Blind.md`).
- Gate review (`ReviewerR92Gate`): re-fetched S491–S494, re-ran the 11 embedded blocks with zero drift, located 12 source quotes verbatim; verdict ADMIT (`w1/ReviewerR92Gate.md`).
- Critic (`CriticR92Claims`): adjudication addendum to the entry, plus 11 ranked findings against the claims and counters (`w1/CriticR92Claims/findings.md`) — see Trend verdicts and Routed defects.
- Mutation test (`MutationR92Counters`): C1 21 mutants (1 killed pre-READY, survivors with kill recipes); C2 7 mutants (4 killed) — `w1/MutationR92Counters/mutants.md`.
- Connector (`ConnectorR92Overlap`): sibling overlap for C03 and C08 (kaidoku and tabi overlap by artifact class, separated), considerthese proposal 1 measured (own-work 55 of 490 rows at round start) — `w1/ConnectorR92Overlap/overlap.md`.
- Landing (`2760f32b`): entry admitted (`admission-status: admitted`; normalised digest unchanged); SOURCES S491–S494 appended inside the Registry after S490, byte-identical to the seat's block; `corpus/README.md` C03 → `held`, C08 → `uncovered`; SKILL registry rows for both counters; D9 pointer re-point; D8 `__pycache__` removal and `.gitignore`.
- Adjudication (`1a520c9e`): round lesson `corpus/lessons/round-92.md`, LOG entry, SCORECARD section, after-logs `reports/round-92/c1-after.log` and `c2-after.log`, separability receipts `.ufo/waves/round-92/separability.log`, round-end census `reports/round-92/census-round-end.log` (exit 0).
- Wave evidence landing (`b4ee0b16`): the 1.7 MB ECMA-335 6th-edition snapshot the S491 quotes were located in.

## Landed changes

| change | LOG.md / SCORECARD / lesson | commit |
|---|---|---|
| freeze: claims, both counters, controls, round-start census | LOG r92 entry; SCORECARD r92 section; `lessons/round-92.md` | `9402183a` |
| landing: C03 entry (admitted), SOURCES S491–S494, README C03/C08 flips, SKILL probe rows, D9, D8, votes, wave evidence | LOG r92 "Landing" bullet; lesson `## Gate` | `2760f32b` |
| adjudication: lesson, LOG, SCORECARD, after-logs, separability, round-end census | LOG r92; SCORECARD r92; lesson | `1a520c9e` |
| wave evidence: ECMA-335 6th-ed snapshot | wave dir `.ufo/waves/round-92/w1/ScoutR92Managed/snapshots/` | `b4ee0b16` |

## Before → after measurements

| claim | counting command (committed tree) | measured commit | before | after | verdict |
|---|---|---|---|---|---|
| C1 — K | `python3 -B reports/round-92/c1_k_admit_counter.py --rev 2760f32b` | `9402183a` → `2760f32b` | `C1_K_HELD_BACKED=8/15`, `C1_VERDICT=fail` (`controls/c1-do-nothing.log`) | `C1_K_HELD_BACKED=9/15`, `C1_VERDICT=pass` (`reports/round-92/c1-after.log`) | **MET on its frozen counter; contested — see Trend verdicts** |
| C2 — legend | `python3 -B reports/round-92/c2_legend_counter.py --rev 2760f32b` | `9402183a` → `2760f32b` | `README_TOKEN_LEGEND_MISMATCH=2 rows=['C03','C08']`, `C2_VERDICT=fail` (`controls/c2-do-nothing.log`) | `rows=[]`, `K_HELD==K_HELD_BACKED=9/15`, `C2_VERDICT=pass` (`reports/round-92/c2-after.log`) | **MET on its frozen counter; contested — see Trend verdicts** |

Separability (`.ufo/waves/round-92/separability.log`): C1 passes with C2's C08 move reverted (C2 then fails on C08 — `rows=['C08']`); C2 passes with C1's entry absent (C1 then fails at `K_HELD_BACKED=8/15`). Each claim verifies without the other.

Both after-states are stronger than declared: C2's declared after was `rows=['C03']`; the landing clears C03 as well because C1's admission flips it.

## Sources & frontier

- **SOURCES.md rows before → after:** 490 → 494. Command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` (`reports/round-92/census-round-start.log`, `census-round-end.log`).
- **Rows added by tier:** tier A ×4 (S491 spec, S492 spec, S493 docs, S494 docs); tier B 0; tier C 0. All opened 2026-11-05, status `mined`, `used-by` the entry.
- **Rows touched old → new:** none (`status`, `recheck`, `used-by` of existing rows unchanged; the append is inside the Registry after S490).
- **Census:** round-start exit 0 (31 W01/W04, 0 E); round-end exit 0 (`ok` line, `reports/round-92/census-round-end.log`). Malformed rows 0.
- **Quarantine (wave-4 duty):** 26 register rows hand-checked — 24 `candidate-present`, 2 `unverifiable`, 0 `refuse-absent`; `ScoutR92Quarantine/verdicts.tsv`. Adoption closed (no package row appended).
- **Assimilation:** none — the `merge/revenger/` package remains in 155/155 id collision; L0 unanswered.
- **considerthese:** `considerthese/2026-11-04.md` proposal 1 (own-work vs external share) measured by the connector, not adopted as a criterion; carried in the round lesson.
- **Frontier rows advanced:** C03 frontier → held (one admitted entry, fixture-scoped); C08 frontier → uncovered (work evidence recorded, no knowledge claimed).

## Trend verdicts

- **expansion: improved.** One admitted knowledge entry on ground the coverage map did not hold (C03, previously `frontier` with no knowledge and no sourced ground; four saved producer records existed and were not coverage). Evidence: `corpus/knowledge/round-92-managed-assembly-metadata-evidence.md`, `corpus/README.md` C03 row, `reports/round-92/c1-after.log`. Expansion is scoped to the observed fixtures and producer surface; no general .NET claim (Q10).
- **quality: improved.** The admitted entry is gated by three non-author votes bound to one digest (`reports/round-92/votes/`), a blind derivation with zero mismatches, a lint pass and an embedded-output pass. The C08 token moved from a contradicted state to the legend-correct one. Caveat: the frozen counters are shown reachable by forgeries (below); the quality claim rests on the votes and the blind derivation, not on the counter alone.
- **discernment: improved, bounded by a named contest.** The two counters were scored against pre-freeze do-nothing and junk controls, and the critic and mutation-tester then found forgeries those controls did not model. The round did not promote the counters' passes into proof: each is recorded as **MET on its frozen counter, contested**, with the forgeries named and kill-recipes demo-verified in scratch. Mistakes mined (M36 recurrence; the r91 quarantine skip; the counter-forgery class) are in `corpus/lessons/round-92.md` `## Mistakes`. Under the operator's rule ("report all verdicts and let the operator rule") the round is **not admitted as a clean verification of either claim**; the operator rules on whether a frozen-counter pass with named forgery reachability counts.

Admission under AXES.md, stated plainly: both claims verify on their frozen predicates, neither axis is harmed, and every verdict is reported. Whether a contested frozen-counter pass is admissible is the operator's ruling.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — author attestation; the non-author re-confirmation of the current SKILL.md bytes is still operator-side and was not performed this round. Pointer: `SKILL.md` (round-92 registry rows; `git show 1a520c9e:SKILL.md`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — the managed producer re-run (`ExecR92Producer`, `w1/ExecR92Producer/comparison.txt`) and the four oracle commands re-run by the gate and critic seats; LOG r92. Pointer: `LOG.md` round-92 entry.
- [~] Instructions executable by an agent without oral context — the entry's `recheck:` and `## Reproduce` commands re-run by three seats (exit 0, 11/21/48/40 stdout lines). Pointer: `corpus/knowledge/round-92-managed-assembly-metadata-evidence.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` byte-unchanged; connector overlap found C03 and C08 each claimed by a sibling province, separated by artifact class and reported, not absorbed. Pointer: `w1/ConnectorR92Overlap/overlap.md`.

Each box is `[~]` (author-asserted, with a pointer). No box is `[x]`: the non-author verifiers (three review seats) reviewed the **entry**, not the promotion checklist, so none is a named verifier of a SHONEN box.

## Routed defects (status-neutral unless the round's rules prescribe otherwise)

- **Counter forgery reachability (critic findings 1–5; mutation report §2–4).** Successor counters C1 v2 and C2 v2 with the critic's closes as frozen predicates are routed to round 93 (`corpus/lessons/round-92.md`, `SCORECARD.md` planned).
- **Entry erratum.** `recheck:` header cites "§8" for the sibling commands, which live in the unnumbered `## Reproduce`; substance verified; fix in the entry's next revision (frozen bytes not edited in-round).
- **Entry note-level statements** (critic finding 9, lines :224-226/:354, :399-400, :378): beyond-quote statements recorded; not FAIL-grade under Q01–Q17.
- **S136 scope cell** says the Augments addendum is "unopened"; the cell is frozen by SOURCES rule 2; correction of record is the lesson bullet.

## Dead seats

None. All 10 seats of `revenger-r92-w1` settled with outputs (`w1-results.json`).

## Stale-lane

Round-92 mission progressed continuously; the lane was not idle beyond the seat waits. No other mission of this lane is open.

## Tooling

No install. `npx -y rea-agents@6.8.0` was run for the producer trial (official npm channel; recorded in `w1/ExecR92Producer/`). No `pacman`, no `sudo`, no host-sysctl change.

## Open L0 questions

- `revenger | round-91` (assimilation id-collision, mass drift) — still unanswered; nothing adopted.
- Operator ruling needed: whether a frozen-counter pass with named forgery reachability counts toward admission (see Trend verdicts).

## Pre-report gates

- `git ls-remote origin refs/heads/main` → `b4ee0b16c82e08d075e7177bc0b977f92ef2d8e6` (final lane hash, pushed).
- `grep -c '^## SHONEN' <report>` → 1 (see below).
