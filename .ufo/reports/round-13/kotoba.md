# kotoba — round 13 report

**Lane:** kotoba-shokunin (prompt & skill craft) · **Round:** 13 · **Axis move:**
`coverage` 7 → **8.0** (`SCORECARD.md`, owned/advisory labels unchanged; the move
was selected by the mission's lowest-axis rule — see § Move selection).

**Lane repo:** `VeigaPunk/kotoba-shokunin`, pushed `d49dfa5..3ea0e08`
(`3ea0e08` baseline re-record · `ae3bbb4` LOG/SCORECARD · `5cc1340` the landing ·
plus the aggregator lane's `683d147..2839f60` which landed inside this repo
during the round).

---

## 1. Move selection, and why the planned move was deferred

`SCORECARD.md`'s lowest row was `coverage` (7, advisory). `AXES.md` defines
coverage as "the fraction of the domain's real surfaces the skill governs", which
for a prompt/skill-craft lane *is* the instruction-surface inventory, so the
lowest axis was also the best fit. The round-12 plan's rank-1 candidate — make one
`SKILL.md` checklist box executable — was **deferred with reason**: it improves
`operability`, an axis this lane does not own, and the plan itself recorded that it
cannot move an owned score without a protocol ruling. It stays first in `planned`
for round 14, with its axis-accounting question still open.

**Claim taken, and its scope.** *The instruction-surface inventory is derived from
loader code; every loader-derived class is either governed by a craft row or
excluded with a named reason; the derivation is machine-checked and independently
re-measured.* The machine-checked half is explicitly narrower than that sentence:
`surfaces.no_uncovered_class` proves set parity over a **documented extraction set**
(`(Id|Cl|jD[ef])(<v>, "<group>", "<file>.md")` over the omp dump) and is vacuous by
construction for opencode. The census says so in its § Honest ceiling rather than
leaving it implied — which is why the score is 8.0 and not the pre-registered 8.5.

## 2. What landed

| Artifact | Content |
|---|---|
| `corpus/knowledge/instruction-surface-census-round13.md` | 41 class ids (33 governed, 8 excluded with reasons): omp's registry read from its own description strings + call shapes (8 machine-extracted `.md` registrations, 17 hand-declared rule-text classes), opencode's instruction service quoted from its shipped JS, plus § A2 (provider-priority derivation), § A3 (partial wire probe), § D (non-loader mentions), § Honest ceiling |
| `corpus/knowledge/instruction-surface-remeasure-round13.md` | the blind second witness: method, agreement table, five adopted additions, two description-vs-code gaps, the one shared open question |
| `verifiers/verify_surfaces.py` | 4 checks (`literal_present`, `no_uncovered_class`, `table_parity`, `excluded_reason`), exit 0/1/2/3, `--inventory`/`--self-test`/`--json`, 629 lines, sha256 `4fb06cdd…` |
| `verifiers/surfaces-baseline.json` | 41 entries, **derived from the census tables**; the reviewer lane regenerated it independently and found no difference |
| `verifiers/fixtures/surfaces/` | 12 synthetic fixtures (no dump excerpts — the sentinel lane found PEM fixtures inside the bundled JS) |
| `SKILL.md` | § Instruction surfaces 7 → 9 rows; CLAUDE.md row's "9/17 string refs" proof replaced by code shapes + the harness divergence; dispatch rows labelled **host-observed**; agent-def roster counts corrected; B1/B2/B3 repairs (catalogue-file selection rule, mutating-harness label, cache-count semantics) |
| `corpus/README.md`, `SHONEN.md`, `LOG.md`, `SCORECARD.md` | index rows, box marks, round entry, axis rows |
| `verifiers/baseline.json` | `omp.db.rows` + `rows_wellformed` 17 → 18 with the mechanism in `measured_against.round13_move` |

## 3. Falsifiers, run (all green at `3ea0e08`)

- `python3 verifiers/verify_surfaces.py` → **4/4 PASS, exit 0** (≈19 s);
  `--self-test` → `0 failure(s) over 28 assertions`.
- **Anti-vacuous, proven by its author lane:** with the original empty baseline the
  live census produces `table_parity` FAIL naming all 41 rows and
  `no_uncovered_class` FAIL naming the 8 extracted classes — parity never passes on
  0==0; missing inventory → exit 2, missing baseline → 3.
- **Mutation lane:** 13 planted faults, **11 caught**; the 2 escapes (a census row's
  *literal* or *evidence* column rewritten) are recorded as a named id-level
  boundary, not smoothed over.
- `verify_corpus_integrity.py` → **9/9**, `verify_corpus_independent.py` → exit 0
  (both instruments agree), `verify_harness_claims.py` → **27/27**,
  `fault_injection_corpus.sh --self-test` → **OK**.
- **The round's own instrument caught the round's own change:** the first pass at
  repairing four dead pointers used the *relative* shape, and
  `fault_injection_corpus.sh --self-test` failed T2/T3 (a relative `.ufo/reports`
  pointer dies in a `$TMPDIR` clone). Reverted to host-absolute and recorded; the
  same probe also caught the mid-landing state twice (an unindexed corpus file),
  which is its job. After the landing commit it reads OK.

## 4. The round's central finding: a lane-vs-lane disagreement decided by bytes

The host-census lane concluded *"opencode's `CLAUDE.md` is prompt text; the loader
is omp-only → that table row overstates its evidence."* The anchor-review lane
concluded the opposite. Adjudicated from the raw bytes: opencode's instruction
service carries

```js
n=[X.join(r.config,"AGENTS.md"), ...!t.disableClaudeCodePrompt?[X.join(r.home,".claude","CLAUDE.md")]:[]]
y=["AGENTS.md", ...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[], "CONTEXT.md"]
```

with `Instruction.find` breaking on the first name that exists per directory. So
**the reviewer was right** and the host census under-read the binary — and the row's
*claim* was substantively true while its *evidence* ("9/17 string refs") was exactly
the proof class this round forbids. Two further lane-vs-lane items were resolved the
same way: the `.cursorrules` "false friend" is the bun template list only for
`.cursor/rules` (omp really does register a cursor class), and the
`["AGENTS.md","CLAUDE.md"]` loop is memory consolidation, not loading (killed
independently by the wire probe).

## 5. Second witness

Blind lane `scout-independent` re-derived the class list with its own printable-run
extractor (`strings` never invoked) and **agrees check-for-check on every
load-bearing class**. It added the omp provider-enablement gates
(`RTo`/`eu()`/`enabledProviders`/`disabledProviders` — a repo carrying `GEMINI.md`
or `.cursor/rules` may be read by nobody), `RULES.md`, opencode's Read-tool
`<system-reminder>` channel, and the two description-vs-code gaps. One item is
unresolved **by both** lanes (`LDe`/`instructions` consumer) — recorded as a shared
open question, not as agreement.

## 6. Forced corrections from a non-author witness

The aggregator lane landed a round-8 box-3 cold run **inside this repo** during the
round. Its findings were adopted rather than argued with:

- **B1** — SKILL.md's "newest `<skills>` block" recipe named no file-selection rule;
  now *catalogue-bearing* + `omp.catalogue_path`.
- **B2** — `verifiers/fault_injection_corpus.sh` was listed among runnable
  verifiers with no mutating warning; now labelled (clones + `rm -rf`s).
- **B3** — the cache-row count moved same-day (17 → 18); now stated as a change
  detector with the mechanism.
- **SHONEN.md** — boxes 1–3 reverted `[x]` → `[~]`: PROTOCOL.md:34-39 says "a
  subagent the lane dispatched is still the lane", so the round-11 `ColdRunRecord`
  and round-12 `ReviewSHONEN` attributions were author attestation.
- Four dead pointer sites in that lane's two in-repo files repaired (two ABSENT
  dispatch pointers → the recorded prose idiom; two bare → host-absolute).

## 7. L2 seats — 14 lanes, two batched calls (floor 8)

Call 1 (11): `PlanCov13`, `ScoutOmp`, `ScoutOpencode`, `ScoutIndependent`,
`LabratInject`, `ExecChecker`, `ExecHostCensus`, `CriticClass`, `ConnectorCross`,
`SentinelScope`, `ReviewerAnchors`.
Call 2 (3): `MutationSurfaces`, `ReviewRound13`, `CriticFinal`.
Every landed claim is attributed where it lives; the lanes that disagreed are named
rather than averaged. `LabratInject` died on a provider rate limit mid-run — its
reproduced results are recorded as partial (§ A3) and nothing it did not finish is
claimed.

## 8. Cross-domain — routed, never absorbed

- **`~/Projects/bounties` vanished mid-survey** (connector §4b: listed, then
  `test -e` → GONE; survivors under `~/Projects/the-bounty-hunter/`). Kasegi's
  domain root; the census records the host-absence as *never a governed pass*.
- **Bootstrapper roster incompleteness (D1 → kumitate):** `rosters[]` misses the
  singular `~/.config/opencode/agent/` dir, inline `opencode.json` prompts, and
  `raw`/`devin`/`kimi`; the `ufo` row points at a non-effective file.
- **Contested scope:** kumitate/kasegi `.omp` trees + the relocated bounty registry;
  `~/.codex/AGENTS.md` live but unlisted in other lanes; kagi's fenced
  `~/.config/opencode` enumeration.
- **Fleet-level:** D-78 (`AXES.md` ↔ `MISSION.md` axis names) still open — this
  round worked an advisory axis on the mission's own lowest-axis instruction and
  says so in the SCORECARD row rather than relabelling it.
- **Aggregator-owned:** its two files in this repo now carry repaired pointers and a
  reconciliation note; the ledger items it routes remain its lane's.

## 9. SHONEN

Boxes 1–3 `[~]` (reverted per PROTOCOL.md:34-39), box 4 `[~]`; the only non-author
evidence on record is the aggregator lane's round-8 cold run, which graded box 3
`[~]` on B1/B2 — both fixed this round, so a fresh non-author run is what would
restore `[x]`. Verifier note updated accordingly.

## 10. Carried into round 14

opencode-side machine check (the withheld 0.5); the checklist-execution move with
its axis question; the omp provider-priority derivation (single-lane, now
wire-corroborated for the dedupe only); `LDe` consumer; id-level parity vs the
census's prose columns; implicit-intent fidelity; pointer hermeticity as a
*measured* failing probe; `LOG.md`/`SCORECARD.md`/`SKILL.md` outside both corpus
instruments' scan.