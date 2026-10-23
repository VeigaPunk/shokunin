# kaidoku round 34 — R34-C1 stopped by a structure-blind control before production

## Work performed

**One claim this round: R34-C1, depth.** The surface is a sourced GNU ELF version-needs (Verneed/Vernaux) decision table plus a section-derived static reader on native ELF ground the lane already owns. It is not coverage and not an REA capability.

The frozen predicate (`P34-version-needs`) reads: "twelve public ELF carriers yield exactly their independently frozen GNU version-needs records on opaque paths, including randomized same-length string-table naming wherever requirements are present, and the pinned source-backed decision table is present." Target: 12.

**Verdict: falsified measure, honest stop.** A fresh adversarial control met the unchanged frozen counter without decoding any ELF structure. It selects a template by input size and reads only fixed name slices, and it scored 12/12 on both schedules, `documents_ok=true`, exit 0. The original kill rule therefore stops the claim. The production reader was never run on the claim set. Main approved the stop.

This is kaidoku's **third straight rejection**:
- r32: a text-presence counter;
- r33: a provider safety hold;
- r34: a fixed-offset replay that meets the counter.

The r34 blocker differs from r33's but belongs to r32's family: in both, the counter cannot tell structure from shape. The lesson is routed as QUALITY 67 and lesson M34-4: the next counter must face a structure-blind replay control **before** it is frozen.

Work items:
- **Outside r33 decision first.** It was rejected-honest-stop, acknowledged before measurement (LOG round-34 entry; SCORECARD round-34 section). Routed defects were handled as follows:
  - **(1) Report:8 statement.** Appended correction: SKILL gained 72 lines (`72 0`); PROVINCE was unchanged. The filed report was not rewritten. Lesson M34-1, QUALITY 65.
  - **(2) R33-C1.** It stays unprovable. The held builder, its derivatives and `U064N008Hf47eb933` were not touched or reproduced.
  - **(3) Freeze maps and parser mutants.**
    - The strict-schema freeze successor `tools/round-34/freeze-integrity.py` turns all seven false-CLEAN map shapes into exit 3 (`prep/R34FreezeSchema-files/receipts/receipt.json`; M34-2, QUALITY 66).
    - The count `>`→`>=` mutant still survives.
    - The metadata-span mutant is now killed by a fresh bounded replay.
    - The tag mutant is still caught only through a detector error (`prep/R34ParserBounds.md`).
  - **(4) r32 wrapper mutants and secondary gates.** Four wrapper mutants are killed by text/JSON successors without changing the frozen code. The independent-pe comparator got a red/green replay. C2v3 and `pe_own_compare` remain excluded (`prep/R34LegacyGaps.md`, `w1/RevLegacyLimits.md`).
  - **(5) Old parser pin.** An appended forward pointer in `.ufo/waves/round-33/prep/R33ChpeParser-independent.json` links it to `text-checker-supersession.json` (M34-3).
- **Sources.**
  - S103: LSB 5.0.0 §10.7.4.
  - S104: pinned glibc 2.42 `elf.h`.
  - S105: the 2013 gABI draft, a real reject for GNU-specific authority.
  - Knowledge entry: `corpus/knowledge/2026-10-23-r34-elf-version-needs.md`. SKILL gained a GNU version-requirements section, an instrument registry and a post-control limits section.
- **Independent expected records.** Twelve public host binaries (7,329,800 B), digest-disjoint from the reader's four development binaries. They hold 107 needed records and 339 auxiliaries, authored by a direct ELF parser and cross-checked with readelf. Three reviewer seats re-derived all twelve with zero field mismatches (`w1/RevOracle{A,B,C}.md`).
- **Decisive control.** `w1/CtlLabels.md`. Counter `d7f0a8cf3ca08562437d40711d15e7ad4f6fa44edb4e8934c36f4673e4e7c45e`. Exact argv and full receipt: `w1/CtlLabels-files/size-pristine.receipt.json`; source `size_lookup.pristine.py` (sha256 `c68511f7…0b22`). `.ufo/waves/round-34/claim-stop.json` binds them.
- **Other controls.** None met the target:
  - do-nothing 1/12;
  - junk 0/12;
  - all-false 0/12;
  - denial and vocabulary bag 0/12 each;
  - one-constant 1/12;
  - SHA replay 1/12 (12/12 on schedule 0 only);
  - filename/label 1/12;
  - five ordinary no-reader controls, 0–1/12.
- **Disclosed instrument limits** (lesson "Pre-production wave findings" and SKILL post-control section):
  - the freeze-successor selftest is flaky: 24/25 when a commit hash starts with 0, while the real 21-pin verdict is CLEAN;
  - duplicate JSON members and path aliases are accepted;
  - six fixture type-coercion survivors;
  - reader metadata table locator, classification and precedence defects (`w1/RevDecisionTable.md`).
- **Scope exclusion.** `CtlNoReader` added an unrequested process-memory side-channel probe. Its code, raw records and procedural details were excluded. Only a high-level hash record remains (`w1/CtlNoReader-files/EXCLUSIONS.txt`). It contributes no claim evidence, was not rerun and was not reassigned. It is not a provider hold.

Paths are relative to `kaidoku-shokunin/.ufo/waves/round-34/` unless they start with `corpus/`, `tools/` or `.ufo/waves/round-33/`. Base: `ec3125ad3d130d92f888a4128dfaa2982f36fff7`.

## Landed changes

All five commits carry `kaidoku-shokunin <kaidoku@shokunin.local>`, were made through `jj-lane.sh` and are pushed (`state … local=remote=f432c8e3… ahead=0 behind=0`).

| commit (`landed`) | content | LOG.md |
|---|---|---|
| `8897a67f6074580d6eac1a3fc0e37fdcd7aa0df0` | Reader, counter, strict freeze successor, expected-author manifest, 12 public carriers, knowledge entry, SKILL table, S103–S105, QUALITY 65/66, lesson, r33 pin pointer, prep evidence | LOG:3081-3089 |
| `54a87a51a865ab931fd355e767303337b05cccf4` | `claims.json` first-add (freeze) and freeze-ledger rows | LOG:3085 |
| `d52e2404ea0160de990d28df673011bb671829f8` | Base receipt, sandboxes, validated spec/dispatch/submitted payload | LOG:3087 |
| `abbd76042fd23b1ba049350fc37a360f793892b7` | Decisive counterexample, `claim-stop.json`, critic reports, QUALITY 67, M34-4, SCORECARD stop | LOG:3090-3091 |
| `f432c8e3bc58934887c83f1db2b26f9910a9d87f` | Settled wave evidence, provenance, limits, misroot relocation, end census | LOG:3092 |

Inherited state: none. At the base, `tracked=0 untracked=0` (`start-state.json`). `corpus/lessons/round-33-verifier-spotcheck.md` is non-author and was read, not edited.

## Before → after measurements

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| R34-C1 / depth | matched 0/12, `reader_absent`, exit 1 (`before/c1-at-base.json`) | **production not run (claim stopped).** Decisive adversarial control: 12/12 on both schedules, documents true, exit 0 (`w1/CtlLabels-files/size-pristine.receipt.json`) | `python3 -I -B tools/round-34/version-needs-counter.py --root <lane> --freeze 54a87a51a865ab931fd355e767303337b05cccf4 --rev <REV>` (control run adds `--control-reader <file>`) | before `ec3125ad`; control `54a87a51` |

Owned scores stay 10→10, delta 0. No capability row was added and no exploratory relabel was made.

## Sources & frontier

- **Row counts.** 102 → 105. Tiers: A 96→99, B 5, C 1. Status: mined 99→101, rejected 3→4. Malformed 0. Counting command and immutable revisions: `source-counts.json`.
- **Rows added.** S103 (A, mined), S104 (A, mined), S105 (A, rejected; flip condition recorded). No existing row cell was touched. Path and search-log entries were added.
- **Census.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku` exited 0 at both start and end, with nine pre-existing W04 duplicate-URL warnings (`start-state.json`, `end-census.json`).
- **Gate quotes.** 21, 3 and 11 words (`quote-counts.json`).
- **Frontier.** No frontier row advanced. This was depth on held ground.
- **Sourced claim.** R34-C1 rests on S103/S104, which are cited in its knowledge entry.
- **Mistakes mined.** M34-1 through M34-5. M34-5 is a misrooted `glibc-tag-object.json`: copied byte-exact into the lane, `cmp` 0, fleet copy deleted.
- **Gate reject.** S105 is rejected as authority for GNU Verneed/Vernaux. The four opened files have zero hits for the GNU version-needs terms; it was reopened by `w1/ScoutRejectGABI.md`. The outside non-author spot-check is pending.

## Trend verdicts

- **expansion: unchanged.** The knowledge entry sits on the existing Native ELF row. PROVINCE is unchanged, and no frontier row or capability was entered.
- **quality: improved** (author assessment). There is a new sourced decision table, reopened by `w1/RevLSBLayout.md` and `w1/RevGlibcTypes.md`. The seven routed false-CLEAN freeze shapes now fail. Four wrapper mutants are killed in successors, the span mutant is killed, and the r33 report and pin corrections are appended. No admitted entry failed re-check. New instrument limits are disclosed, not hidden.
- **discernment: improved** (author assessment; outside spot-check pending). The real S105 reject is recorded with its flip. A structure-blind shortcut was caught before production and the frozen rule was applied rather than amended. QUALITY 65–67 each cite a lesson mistake with a red case.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the new GNU version-requirements table, error patterns and checklist cite S103/S104 (`SKILL.md`, round-34 section; `w1/RevLSBLayout.md`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — still rests on the historical round-1 libjq task (`corpus/lessons/2026-10-15-round-1.md`); R34-C1 production was not run.
- [~] Instructions executable by an agent without oral context — the SKILL checklist and counter command are written out (`SKILL.md` round-34 section); no non-author has executed them.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE is unchanged and the claim has no runtime/REA/sibling scope (`w1/ConnectorSiblingBoundary.md`).

## Round shape, seats and filing receipts

**Round shape.**
- One ordinary preparation `task` call of 8 seats: executor 4, mutation-tester 1, scout 1, scribe 1, connector 1. This was not a validated swarm wave. Preparation writers used disjoint archival directories in the lane instead of separate worktrees; that is a disclosed containment limit.
- One validated v1 control wave of 32 seats in one `task` call (`w1-spec.json`, `w1-dispatch.json`, `w1-submitted.json`): reviewer 11, mutation-tester 11, executor 3, critic 2, scout 2, scribe 2, connector 1. Each seat had its own sandbox clone.
- Round total **40**. The L1 held the planner seat. No wave 2 was dispatched: the claim stopped, so there were fewer than 32 attack items. No residual call.
- The §3 L2 floor is met inside w1.

**Seat outcomes.** All 40 seats completed. Dead 0, cancelled 0, provider safety holds 0, replacements 0 (`prep-settle.json`, `w1-settle.json`, `final-provider-provenance.json`). Ordinary quota fallbacks were recorded; they are not holds.

**Transport and gate.** The `task` tool requires `solutionSpace` and intent metadata, so they were added; nothing else was edited. `wave-slot.sh` granted 32 seats (live 68 of 100). The requested 3700 s bash timeout was clamped to 3600 s; reported via `xd://report_issue`.

**Prefile.** Run 11:21:07Z, after all seats settled: `prefile: tree clean`, both freeze gates `--disclosures` exit 0 at `f432c8e3`, `prefile: PASS`, exit 0. No KaidokuR34 job was running at filing (`proc://`).

**Stale-lane.** Respawn-per-round driver; no other kaidoku mission is open.

**Tool installs:** none. **L0 questions:** none.

**Gate.** S105 was rejected for GNU version-needs authority, with its flip recorded.

**Round verdict: rejected-honest-stop recommended.** Outside closure decides.
