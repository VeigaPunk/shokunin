# kotoba — round 9 report

Lane: `kotoba` (child repo `kotoba-shokunin/`, axes depth + consistency).
Landed before this report: commit **`8e22a41`** (`kotoba-shokunin` HEAD; the
integration commit is `e997d45`, an ancestor of it). Both pushed.

## Axis move — consistency (lowest axis)

Defect class: harness-specific routing claims written as universal rules.
Measured first (L2 sentinel, `SKILL.md` @ `143fe473…`, 487 lines): 31 claim
units, **15 SCOPED / 9 UNSCOPED / 7 UNSUPPORTED**, and
`grep -c '<available_skills>' SKILL.md` → **0** — the file described a
one-harness router world two rounds after the two-harness evidence existed.

Landed: `SKILL.md` `## Router model — which harness, which gate` (per-harness
tag / render / offer gate / failure mode + a check-before-predict recipe),
harness-qualified intro, frontmatter-craft opener, rules 8 and 9, and three
anti-pattern rows. After (independent sentinel re-measurement): **UNSCOPED
9 → 0**, UNSUPPORTED 7 → 6, SCOPED 15 → 23, `<available_skills>` 0 → 3; the six
residuals were re-worded in-round to cite the router model or be labelled
guidance/heuristic (`grep -c 'router never\|router can.t either\|every byte
loads every time'` → 0). A second L2 reviewer applied the file's own 13-item
trigger-fidelity checklist to `SKILL.md`: **13/13 pass, 0 ambiguous**, with two
citation fixes applied same-round (split the `skill/index.ts` dedupe range into
`:105-139`/`:235-246`; widen the `session_init` counter range).

## Drift re-measure (freshness inside the move)

- `sqlite3 -readonly ~/.omp/agent/skill-descriptions.db "select count(*) from
  skill_descriptions;"` → **17** (round 7: 5).
- The cache key's description salt is **style-aware** (`>-`/plain →
  ws-collapsed 11/17; `>` → +`"\n"` 5/17; `|` → as-written + `"\n"` 1/17):
  round-7's ws-normalised recipe reproduces only 11/17, the corrected one
  **17/17**. Every live description is >100 ws chars and the newest captured
  catalogue (2026-09-28T21:06:34Z) renders 17/17 from cache, 0 truncations —
  "the truncator is the default" is a truncation-era statement.
- Catalogue freeze upgraded from [INFERENCE] to measured: 230 `<skills>` blocks,
  four signatures monotone 3 ⊂ 5 ⊂ 11 ⊂ 17, one per session; kill-proof =
  L1's frozen catalogue holds a sekhmet-l3 render the live db has replaced, and
  the db's last write (20:57:58.180Z) landed 3.9 s after L1's session render
  (20:57:54.260Z).
- Counters: compression warns 10681 → 10925; `session_init` 3911 → ~4032–4120
  (live counter, drifts inside a round); opencode.db 415 calls/216 sessions and
  opencode.log 471 permission lines unchanged since round 5.

## Changes landed (all under `LOG.md` round-9)

| Artifact | Change |
|---|---|
| `SKILL.md` | Router-model section + harness scoping; Sources drift fixes (stable anchors instead of an ELF offset, style-aware key rule, re-counted censuses, split misattributed citations); 557 lines (≤600 bound) |
| `corpus/knowledge/harness-router-models-round9.md` | New: two-harness model, key-reproduction and freeze evidence, cross-harness craft rules, unknowns |
| `corpus/knowledge/claim-scope-audit-round9.md` | New: the before→after measurement table |
| `corpus/lessons/round-8.md` | New (a round late): round-8's discovery-vs-landing split + round-9 corrections of three round-8 mechanism sentences |
| `corpus/lessons/round-9.md` | New: the round's lessons, cures, and recipe appendix |
| `corpus/README.md` | Index debt paid: rows for both round-8 artifacts, both round-9 knowledge artifacts, both lesson files; two superseded rows re-based; Known-gaps updated |
| `SCORECARD.md` | New per AXES.md contract: 7 axes, evidence pointer + last-change round on each; consistency 5 → 7; planned = round-10 depth move (committed drift-detector script) |
| `SHONEN.md` | Regenerated to the canonical 4-box seed, one evidence line per box, all `[~]` (no `[x]`) |
| `LOG.md` | Round-9 entry (append) |

Lane identity fixed in-repo: `user.name=kotoba-shokunin`,
`user.email=kotoba@shokunin.local` (round-7's `3b029b8` was a conformance defect
under the operator identity) — recorded in the LOG entry.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md` (557 lines) anatomy + decision-table + four fidelity checklists + 22-row anti-pattern table + Sources; round-9 reviewer ran the 13-item checklist → 13/13 pass.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: round-5 fleet audit, round-7 dispatch audit of 43 files, round-9 two-harness model + claim-scope audit (`LOG.md` round 9, commit `e997d45`).
- [~] Instructions executable by an agent without oral context — pointer: round-7 blank-context reviewer (13 verdicts, zero questions); round-9 second reviewer applied the checklist to `SKILL.md` itself, 13/13, zero clarifications.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: round-9 defects in sibling repos and `~/.config/opencode/` audited and routed in `knowledge/sibling-description-rewrites-round8.md` and the connector lane's sweep, never fixed; `PROVINCE.md` unchanged.

Verifier note: every check this round, including the four verification lanes,
was lane-dispatched or lane-run — therefore `[~]`, and SHONEN `[x]` still
requires a non-author verifier.

## Cross-domain evidence (routed, not absorbed)

- **Sibling lane repos** (`kagi/kake/kasegi/kengaku/kumitate-shokunin/`): round-9
  connector swept all five `SKILL.md` files for the same harness-unscoped claim
  class (`grep 'cliff\|<skills>\|<available_skills>\|slice(0,99)\|router\|opencode\|omp'`
  per file) → **none found**; no handover owed this round. Open from round 8 and
  still unlanded: the five drop-in `description:` rewrites
  (`knowledge/sibling-description-rewrites-round8.md`) whose targets sit outside
  every omp discovery root.
- **Agent-definition surface** (`~/.config/opencode/agents/`, operator-owned):
  round-6/7 defects persist — `ufo.md` missing `name:` + stale `cascade_note`,
  `mutation-tester.md` doubled godspeed preamble, `scout.md` `aaron` bin absent
  from PATH.
- **Dispatch prompts** (`/home/vgpnk/projects/shokunin/.ufo/prompts/`,
  integrator/operator-owned): round-7 defects persist; the population grew to 50
  `*-round-*.md` files, and rounds still restate the L2 route map (this round's
  own prompt carries the current `m_flash`/`m_zfl`/`m_lunamax` bucket, so the
  generator fix appears to have propagated).
- **opencode upstream** (`sst/opencode`, dev): used as the authority for the
  offer-gate corrections; belongs to no lane province, reported to the fleet as
  a citation source only.

## Conformance / process notes

- Mission `shokunin-r9-kotoba-r1790629073` opened 2026-09-28T17:57:54-03:00 —
  open ~33 min at report time, i.e. **longer than two 450 s driver ticks**, but
  actively working through the whole window (14 L2 lanes, two batched `task`
  calls, commits landed); no stale-lane action requested.
- L2 minimum met with margin: 14 lanes / two batched calls (floor 8).
- Known residual: `/tmp` scratch pointers remain inside the append-only
  round-7/round-8 corpus artifacts (historical text, not rewritten); no new
  `/tmp`, `local://`, or session-scoped pointer was added by round 9.