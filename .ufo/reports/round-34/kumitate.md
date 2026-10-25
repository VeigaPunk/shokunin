# kumitate — round-34 report (kaika campaign, 2026-10-19)

Lane worktree `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kumitate-shokunin`, branch `kaika/round`, base `16a5441`. Round commit: `1a8eed5` (`1a8eed5aaa32043cf109dd28ceb5cd37ccd5555e`, author `kumitate-shokunin <kumitate@shokunin.local>`). Steered round 34 per the round-33 continuation record; no collision (no `round-34/kumitate.md` existed in the fleet root or ledger; the lane LOG did not close round 34). Precedence named: the standing operator rule "No push" overrides MISSION.md's commit-then-push — the round is committed, not pushed. Every verdict below is the lane's self-verdict, pending non-author verification.

## Work performed

Declared claims (2; causally separable, distinct axes):

1. **Claim 1 — operability (the lowest live axis, 8) + capability `sources-registry`.** New gate `scripts/sources-check.mjs` (contract `kumitate-sources-v1`) over a new `corpus/SOURCES.md` (fleet SOURCES contract v1), two checklist items, and a `## Gate registry` in `SKILL.md`. Measured as an f_O walk: integer held at 8.
2. **Claim 2 — coverage:kimi-layer, live-derived 9 → 10.** The Kimi substrate grew a sixth counted-live `skills/` child (`cursor-lane`); a member section plus the census tripwire re-pin restores 50/50.

Work items:

- `corpus/SOURCES.md` — 20 rows, every one opened 2026-10-19 by the sources scribe seat; `## Paths` (3), `## Search log` (4 notes), `## Leads (unopened)`; 2 rejected rows with reason + flip (S019 security province → kasegi/kagi; S020 locator drift). Evidence: `corpus/SOURCES.md:10-34`; gate record `corpus/lessons/round-34.md` `## Gate` and `.ufo/rounds/round-34/sources-gate.md`.
- `scripts/sources-check.mjs` — 698 lines; finding kinds mapped to the fleet census codes E01–E11; `--selftest` 34/34 incl. awk-census parity; two cases added by the L1 after the mutation seat's two survivors (over-wide row; ISO recheck exactly today). Evidence: `node scripts/sources-check.mjs` → `SOURCES_CHECK: CLEAN (rows=20 tiers=A:19,B:1,C:0 status=queued:9,mined:9,rejected:2 entries_with_source=2 legacy=38)` exit 0.
- `SKILL.md` `## Gate registry` (7 rows, PROTOCOL §Gate standard registry home) + checklist items 12–13 (`SKILL.md:587-630`).
- Census tripwire re-pin `scripts/kimi-census.mjs` (skills 5 → 6, FROZEN K2 26, selftest 43 → 45, --json echo of all five FROZEN values asserted) and `pin.sources-check` in `scripts/proxy-check.mjs` (selftest 102 → 103).
- `corpus/knowledge/kimi-skills-plugins.md` — `## ~/.kimi-code/skills/cursor-lane` section + append-only erratum (lines 173-216, 438-442); the runbook's credential lines deliberately not reproduced (sentinel seat listed them by line/category only).
- `corpus/QUALITY.md` — admission bar Q1–Q14, every criterion citing its lesson.
- `corpus/lessons/round-34.md` — `## Mistakes` (14 classes) + `## Gate` (admits, holds/rejects, all 20 source quotes).
- Expansion entries: `corpus/knowledge/omp-task-contract.md` (214 L, S001–S004; frontier) and `corpus/knowledge/kimi-mcp-plane.md` (S005–S008; shape-only, 0 content reads).
- `PROVINCE.md` Core/Frontier/Adjacent appended (`PROVINCE.md:8-28`); `SCORECARD.md` `## Saturation` declared (line 9, window N = 3); `## Planned` round-35 pre-registration (mcp.json K1 change, S/R distinct derivation, R5+R7).
- L2 swarm: one batched dispatch of 12 seats — planner, connector, 3 executors, 2 scribes, scout, reviewer, critic, sentinel, mutation-tester — routed by the session route table (no model passed). The executor/mutation-tester route hit provider exhaustion (`resource_exhausted`, "Reached free model rate limit"): 3 seats died and 1 stalled (cancelled); those four seats were re-dispatched fresh in two batched calls per the orchestrator route note. The first L2 batch also failed once on the 100-job cap and was retried unchanged after a wait.

## Landed changes

All in commit `1a8eed5`, logged in `LOG.md` round 34 (`LOG.md:1411-1511`):

| Change | Files | LOG pointer |
|---|---|---|
| Sources registry + gate + checklist + gate registry (Claim 1) | `corpus/SOURCES.md`, `scripts/sources-check.mjs`, `SKILL.md`, `scripts/proxy-check.mjs` (pin) | `LOG.md:1411-1433` |
| Kimi skills re-pin + cursor-lane section (Claim 2) | `scripts/kimi-census.mjs`, `corpus/knowledge/kimi-skills-plugins.md` | `LOG.md:1434-1449` |
| QUALITY bar, lessons, expansion entries, PROVINCE bands, saturation, README rows 74 → 77 | `corpus/QUALITY.md`, `corpus/lessons/round-34.md`, `corpus/knowledge/omp-task-contract.md`, `corpus/knowledge/kimi-mcp-plane.md`, `PROVINCE.md`, `SCORECARD.md`, `corpus/README.md` | `LOG.md:1450-1456` |
| Measurement revision, origin drift, review corrections, critic isolation | `LOG.md`, `SCORECARD.md` | `LOG.md:1457-1511` |

## Before → after measurements

All after-values measured on `1a8eed5` (clean tree). Origin-dependent terms use a read-only snapshot of the round-open origin revision 964f443ee53df0ce06bd689af01f0dea031b01f9 (`git -C /home/vgpnk/Projects/ufo-fsd-alpha archive 964f443 | tar -x -C /tmp/kumitate-r34/origin-964f443`), because the origin advanced to 2cad7085 during the round.

**Claim 1 (operability; capability `sources-registry`).**
- `ls scripts/*.mjs | wc -l`: 6 → 7 (A). `grep -c '^\s*- \[' SKILL.md`: 11 → 13 (C). `f_O = (A+C)/(A+C+3)`: 17/20 = 0.85 → 20/23 ≈ 0.870; `floor(10 × f_O)` 8 → **8 (held)**.
- `grep -c '^| [a-z-]* | gate |' SKILL.md`: 0 → 7 gate-registry rows.
- Contract census (`SOURCES-CONTRACT-v1.md` lines 68-80): before — file absent, cannot run; after — rows 20, malformed 0, tiers `A=19 B=1`, status `mined=9 queued=9 rejected=2`, duplicates / enum-violations / missing used-by each print nothing.
- `node scripts/sources-check.mjs` → `SOURCES_CHECK: CLEAN (rows=20 …)` exit 0; `--selftest` → `SOURCES_SELFTEST: 34/34 pass`. Fleet cross-check: `bash …/fleet-census/scripts/sources-census.sh validate --file corpus/SOURCES.md --root .` → `file ok`.
- `node scripts/proxy-check.mjs --src /tmp/kumitate-r34/origin-964f443` → `PROXY: MATCH (A=7 C=13 operability=8; C1=19/19 C2=77/77 coverage=10; S=91/91 coverage:script-layer=10; R=83/92 coverage:runtime-layer=9; K=50/50 coverage:kimi-layer=10; pins=7 match)` (also `--strict`).

**Claim 2 (coverage:kimi-layer).**
- Before (round open, live): `PROXY: DRIFT (K_MEMBERS_DRIFT term=K_members declared=49 computed=50 delta=+1; COVERAGE_KIMI_DRIFT term=coverage_kimi declared=10 computed=9 delta=-1; AXES_DRIFT …)`; `KIMI_CENSUS: DRIFT (UNLISTED skills/; UNLISTED mcp.json)`.
- After: proxy K terms `K=50/50 coverage:kimi-layer=10` (MATCH, command above) → live-derived **9 → 10**; `node scripts/kimi-census.mjs` → `KIMI_CENSUS: DRIFT (UNLISTED mcp.json)` (members=50, errors 2 → 1); `--selftest` 43/43 → 45/45. strace `-e trace=open,openat,openat2`: 0 opens of `~/.kimi-code/mcp.json`.
- Scope: verified for the declared 50-member universe; the root census stays red on mcp.json by design (held, see Mistakes).

**Separability** (critic seat, phase 2, /tmp copies): Claim 1 alone → `PROXY: MATCH` with `A=7 C=13`, `K=49/50 … 9`; Claim 2 alone → `PROXY: MATCH (A=6 C=11 operability=8; … K=50/50 coverage:kimi-layer=10; pins=6 match)`.

**Round record.** `node scripts/round-gate.mjs --round 34 --reports-dir <fleet-ledger>/.ufo/reports --main-repo <fleet-ledger>` (run from the lane worktree after this report was written) → `ROUND_GATE: CLEAN (round=34 lane=kumitate checks=10 errors=0 warnings=0)` — QUALITY Q10 satisfied for this round (round 32's record still reads DRIFT; not repaired this round).

**No-harm checks.** C2 74/74 → 77/77 (`grep -c '^| \`\(knowledge\|lessons\)/' corpus/README.md` vs `find corpus/knowledge corpus/lessons -name '*.md' | wc -l`). Per-file cite-check errors: `SKILL.md` 9 → 9, `kimi-skills-plugins.md` 10 → 10, every new file 0; `corpus/README.md` 30 → 30 on the snapshot (31 live — origin drift on an unchanged line). Checklist `node scripts/surface-probe.mjs --checklists`: 6/11 → 7/13 live, 9/13 with `UFO_SRC` pinned. Selftests: cite 62/62, claims 39/39, round-gate 60/60, surface-probe 42/42 unchanged. External (not caused by the round): live origin 2cad7085 drops coverage:script-layer 10 → 9 (`S_members 91→88`, `S_sections 91→86`) — recorded in `LOG.md:1467-1477`, stanza left at the measured 91/91, re-census is open debt.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:587-630` (gate registry + 13-item checklist), `corpus/SOURCES.md` (20 opened, tiered sources).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:1434-1449` (substrate drift: trigger census DRIFT → census re-pin + member section → K 50/50, census residue dispositioned).
- [~] Instructions executable by an agent without oral context — `SKILL.md:613-630` checklist (9/13 pass with the origin pinned), `corpus/QUALITY.md` `## How to apply`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:24-28` Adjacent band; S019 rejected to kasegi/kagi; the `rea` MCP registration routed to kaidoku (`corpus/knowledge/kimi-mcp-plane.md`).

## Sources & frontier

- Rows: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` 0 (file absent) → 20.
- Added by tier: A 19 (spec 2, docs 13, paper 1, tool 1, own-work 2), B 1 (community: Cognition). Status: mined 9, queued 9, rejected 2.
- Rows touched old→new: none (all rows new this round).
- Frontier advanced: OMP harness contract moved from unnamed to entered Frontier ground with its first sourced entry (`corpus/knowledge/omp-task-contract.md`, S001–S004); MCP revisions, isolation substrates and failure research named as Frontier with queued rows (`PROVINCE.md:17-22`).

## Mistakes

- Mined 14 classes into `corpus/lessons/round-34.md` `## Mistakes`: 11 from the lane's history (recalled counts, gate blind spots, attribution/identity, substrate mutation, own round-gate failing own record, admission-status ambiguity, dead pointers, stale prose, unadopted contract surfaces, revision skew, correction reintroducing the fixed class) and 3 from this round (a registry change slipped into the measuring round — proposed by the L1, refused by the critic seat and held to round 35; a relay message displacing two seats' finals; executor seats skipping assigned verification).
- Criteria added: Q1–Q9 (entry), Q10–Q14 (round: own round-gate, dated admission entry, lane identity, round-open drift disposition, no /tmp pointers) in `corpus/QUALITY.md`, each citing its lesson.
- Admitted: `kimi-mcp-plane.md`, `omp-task-contract.md`, the cursor-lane section, SOURCES rows. Held/rejected: mcp.json as a K1 member (flip: the round-35 pre-registration lands with tool + stanza + axes), S019, S020, the original 51/51 target.

## Trend verdicts

- **Expansion: improved.** Two admitted knowledge entries whose `source:` cites mined rows on uncovered ground (the MCP plane had 0 corpus mentions; the OMP contract had 0 upstream citations), plus one new K2 member section. Evidence: `node scripts/sources-check.mjs` `entries_with_source=2` (0 before).
- **Quality: improved, with an external drift named.** A 7th self-tested gate, a gate registry, QUALITY bar, two mutation survivors killed (L1 re-run: each mutant now 33/34 FAIL). The live origin move lowers script-layer to 9 at 2cad7085 — not caused by the round, recorded as open debt.
- **Discernment: improved.** The critic's falsification of the registry-timing design was accepted before landing (Claim 2 rescoped 51/51 → 50/50); reviewer findings folded into `LOG.md:1486-1499`; no `[x]`, no unearned integer.

## L0 questions

- kumitate | round-34 | The `kumitate-proxy-v1` stanza gained a 24th key (`pin.sources-check`), additive by the lane's L1 as in rounds 16 and 20; the critic asks whether a "parent-frozen" contract may be extended this way or needs a v2 — which rule applies?
- kumitate | round-34 | Commit 16a5441 (2026-10-17; runtime 83/92, score 9) still has no dated admission entry (Q11). Should round 35 record it as admitted on its live gate lines, or re-measure it as a fresh claim?
- kumitate | round-34 | The origin tree /home/vgpnk/Projects/ufo-fsd-alpha advanced mid-round (964f443 → 2cad7085, 5 scripts deleted). Should lane rounds pin `--src` to the round-open revision by default?

## Integrator notes

- Provider exhaustion: the executor and mutation-tester route returned `resource_exhausted` mid-round (3 seats died, 1 stalled); seats re-dispatched fresh. One batch also hit the 100-job cap and was retried.
- `scripts/round-gate.mjs` default audit fails closed in tower worktrees (`REPORTS_DIR_MISSING`: its main-repo default derives to `.tower/worktrees/kaika`); run it with explicit `--reports-dir` / `--main-repo`. Lane-owned defect, queued.
- `node scripts/surface-probe.mjs` fails on origin drift (`SCRIPT_DIGEST_MISMATCH`, `VERB_UNDECLARED surface`, `SURFACE_UNREACHABLE status exited 1`; origin `config/ufo.json` was locally modified) — upstream surface, reported, not patched.
- The W1 STATE dossier `fleet-ledger/.ufo/waves/kaika-w1/kumitate-state.md:52` prints the operator's personal email address in the commit-author histogram; the lane lesson redacts it. Consider redacting the dossier.
- Fleet-root strays (`RelNotes-2.54.0.txt`, `dedupe.rs`, `err.*.txt`) are not from this lane; no write outside the lane worktree, `/tmp/kumitate-r34*`, and this report.
- `SHONEN.md` itself was not edited (boxes stay `[ ]` there); the `[~]` marks above are the lane's assertion with pointers.

## Post-review fixes

Lane commits (both author and committer `kumitate-shokunin <kumitate@shokunin.local>`,
with `maintenance.auto=false`):

- `06757b0da6c790f823bf765aff366274dc5e1a5a` — `round-34: post-review fixes`
- `6336d712d7634c541ca5d60dd707f17ea2563ed7` — `round-34: correct saturation pointers`

`scripts/sources-check.mjs` now counts only rows under `## Registry`, rejects
empty required cells, and independently rejects missing rejection reasons and
missing `flip:` conditions. The no-header exemption is the immutable 38-path
knowledge identity set from base `16a5441`. Those legacy files remain
exempt-but-counted; new headerless files and removal of a new entry's `source:`
header fail. The cursor-lane subsection appended to the base legacy
`kimi-skills-plugins.md` is not a new sourced entry or expansion admission.
The two separate new header-trio files remain the sourced-entry basis.

`kumitate-proxy-v1` retains its parent 23-key set (17 terms and six pins):
`pin.sources-check` is absent from the stanza and parser contract. The
independent source gate remains in `SKILL.md`'s gate registry. The Kimi claim is
still limited to 50 frozen K1–K5 members; root `mcp.json` remains undeclared
round-35 debt, so this is not a clean whole-root census.

**Verification.** Commands below ran from the lane root unless a full path is
shown:

```text
node scripts/sources-check.mjs --selftest
SOURCES_SELFTEST: 42/42 pass
VERDICT: PASS
```

The seeded-invalid fixtures rejected with exit 1 and the named finding:

```text
ROW_OUTSIDE_REGISTRY: exit=1 kinds=[ROW_OUTSIDE_REGISTRY]
ROW_FIELD_EMPTY: exit=1 kinds=[ROW_FIELD_EMPTY]
REJECTED_NO_REASON: exit=1 kinds=[REJECTED_NO_REASON]
REJECTED_NO_FLIP: exit=1 kinds=[REJECTED_NO_FLIP]
HEADER_INCOMPLETE (empty header trio): exit=1 kinds=[HEADER_INCOMPLETE]
ENTRY_HEADER_REQUIRED (new headerless file): exit=1 kinds=[ENTRY_HEADER_REQUIRED]
ENTRY_HEADER_REQUIRED (source header removed from new entry): exit=1 kinds=[ENTRY_HEADER_REQUIRED]
```

The same selftest confirms the legacy set is `base=38 unique=38` and a listed
headerless legacy fixture stays clean with `legacy=1`. The actual lane gate
returned:

```text
node scripts/sources-check.mjs
SOURCES_CHECK: CLEAN (rows=20 tiers=A:19,B:1,C:0 status=queued:9,mined:9,rejected:2 entries_with_source=2 legacy=38)
```

Parser and validator checks:

```text
node scripts/proxy-check.mjs --selftest
PROXY_SELFTEST: 104/104 pass
VERDICT: PASS
PASS parent-frozen v1 parser accepts its unchanged 23-key base stanza — keys=23 baseKeysMatch=true accepted=true
PASS STANZA_KEY_UNKNOWN: parent-frozen v1 rejects pin.sources-check — exit=2 token=STANZA_KEY_UNKNOWN

bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kumitate-shokunin
kumitate-shokunin	ok	/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kumitate-shokunin/corpus/SOURCES.md
exit=0
```

Saturation is declared under `SCORECARD.md` `## Saturation` (line 1620; round-34
declaration at line 1624). The earlier report pointer to line 9 was unrelated
membrane-seal text. No live targets were contacted.

Credential scan over the changed lane files and this appended report section:
no matches found.

### Remaining debts

- Root `mcp.json` remains undeclared outside the frozen K1–K5 50-member
  universe; it is still pre-registered for round 35, and the whole-root census
  is not clean.
- The parent-frozen v1 pin set still excludes the independently registered
  `sources-check` script. `[INFERENCE]` The existing `PIN_UNPINNED` arm will
  report it; the proxy selftest confirms that an unpinned script warns and
  `--strict` promotes that warning. No live-tree proxy or Kimi census was run
  in this repair.
- The earlier report's external origin script-layer drift remains untouched;
  this correction did not remeasure the origin tree.

## 2026-10-19 — targeted Markdown parser follow-up (append-only)

Lane commit: `0acb7752d19058b953ebbeba253b1e35f6548de5` on `kaika/round`;
author and committer `kumitate-shokunin <kumitate@shokunin.local>`, with
`maintenance.auto=false`. Only `LOG.md`, `scripts/sources-check.mjs`, and
`.ufo/rounds/round-34/sources-gate.md` were committed. This report remains
uncommitted.

Before the correction, strict consumer runs at prior HEAD
`6336d712d7634c541ca5d60dd707f17ea2563ed7` reproduced:

| Fixture | Before correction |
|---|---|
| Valid `S002` row indented by two spaces | exit 0; `SOURCES_CHECK: CLEAN (rows=1 tiers=A:1,B:0,C:0 status=queued:0,mined:1,rejected:0 entries_with_source=1 legacy=0)` — the row was omitted. |
| Invalid `S023` row indented by two spaces (empty source, tier `Z`) inside Registry | exit 0; same CLEAN output with `rows=1` — the malformed row was omitted. |
| Valid `S022` row indented by two spaces outside Registry | exit 0; same CLEAN output with `rows=1` — no `ROW_OUTSIDE_REGISTRY`. |
| Rejected teaches `REJECTED: outside scope; reflip: ...` | exit 0; `SOURCES_CHECK: CLEAN (rows=2 tiers=A:2,B:0,C:0 status=queued:0,mined:1,rejected:1 entries_with_source=1 legacy=0)`. |

The selftest now checks valid rows at each 1–3-space indent and headings at
1–3-space indents, plus an invalid four-space code row that must remain excluded.
It also checks empty-source/invalid-tier rows at all three supported indents,
all three indented off-Registry rows, and `reflip:` as a rejected-row
false-acceptance. The marker test checks only a word-boundary literal `flip:`;
it does not semantically judge the human-written condition.

**Verification after the correction:**

```text
node scripts/sources-check.mjs --selftest
SOURCES_SELFTEST: 46/46 pass
VERDICT: PASS
exit=0

node scripts/sources-check.mjs
SOURCES  info  LEGACY_NO_HEADER  count=38
SOURCES_CHECK: CLEAN (rows=20 tiers=A:19,B:1,C:0 status=queued:9,mined:9,rejected:2 entries_with_source=2 legacy=38)
exit=0

bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kumitate-shokunin
kumitate-shokunin	ok	/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kumitate-shokunin/corpus/SOURCES.md
exit=0
```

`node scripts/proxy-check.mjs --selftest` returned `PROXY_SELFTEST: 104/104
pass`, `VERDICT: PASS`, exit 0; its frozen-v1 fixture reports the unchanged
23-key base stanza accepted and `pin.sources-check` rejected as
`STANZA_KEY_UNKNOWN`. The frozen 38-path legacy identity assertion remains in
the sources selftest (`base=38 unique=38`). No proxy stanza, score, quota or
SOURCES contract changed; no live UFO origin was contacted.

**Remaining limitation:** the knowledge inventory is intentionally still a
direct-child scan of `corpus/knowledge/*.md`. A nested headerless file such as
`corpus/knowledge/sub/x.md` is not scanned, so this gate does not claim
whole-corpus knowledge admission. The canonical fleet census was not changed;
its successful current-file validation does not establish equivalent
1–3-space fixture behavior. The explicit boundary is also recorded in
`.ufo/rounds/round-34/sources-gate.md` and `LOG.md`.
