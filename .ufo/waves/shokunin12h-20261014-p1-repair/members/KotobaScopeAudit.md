# KotobaScopeAudit

Advisory baseline scope audit of the kotoba gate/citation inventory and province boundary at starting revision `02302c521b933c55fc4be79193e61537e3380751` (working tree clean except untracked `plans/`). Not a native judge verdict, lane round report, receipt, or admission. No gate was executed. `lsp` is not a mounted device (`xd://lsp` absent); caller/definition checks below are source reads, not semantic proof.

Axes: freshness, operability, calibration, adjacency.

## Inventory actually in force

| Instrument | Kind in prose | Checks in source | Registry row in `SKILL.md` | Source default |
|---|---|---|---|---|
| `verifiers/verify_harness_claims.py` | gate, live recipe | 28 keys in `CHECKS` (lines 523–552), matching `baseline.json` `checks` | none | `Path.home()` binaries/db/log/sessions; no `--src`, no `$UFO_SRC` |
| `verifiers/verify_surfaces.py` | gate | 7 `CHECK_IDS` (lines 160–168) | none | hardcoded `/home/vgpnk/.local/bin/omp` and `/home/vgpnk/.opencode/bin/opencode` (lines 126–129) |
| `verifiers/verify_skill_checklist.py` | gate | 10 `CHECK_IDS` (lines 282–293) | none | script grandparent; citation roots closed |
| `verifiers/verify_corpus_integrity.py` | gate | 9 ids in the module docstring | none | script grandparent; corpus `*.md` only |
| `verifiers/verify_corpus_independent.py` | second witness | same 9 ids | none | same class, own tokenizer |
| `verifiers/fault_injection_corpus.sh` | mutating probe/harness | 10 planted classes | none | clones under `${TMPDIR}` |

Wave before receipt `.ufo/waves/shokunin12h-20261014-p1-repair/evidence/kotoba-before.json` records only `python3 verifiers/verify_corpus_integrity.py`, exit 0, `9/9 checks pass`, `report_dead=0/32`. It is not a six-instrument baseline.

Round 18's "gates never took `--src`" (`LOG.md` lines 905–907) is true of the argparse surfaces. It is not the wave repair pattern. None of these gates resolve `$UFO_SRC` → `~/Projects/ufo-fsd-alpha` → `~/Projects/origin-work/ufo-fsd-alpha` → fail-closed. They grade installed binaries and this repo. Shape check, not content: `~/Projects/ufo-fsd-alpha` exists, HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9` (matches the round-18 citation); `~/Projects/origin-work/ufo-fsd-alpha` is absent; `skills/ufo/SKILL.md` exists only on the relocated tree (36375 bytes). No gate hashes or length-checks that file.

## Findings

### 1. High — live fleet-root citations use a path this lane already measured absent, and no gate can see them

`/home/vgpnk/projects` does not exist (`exists=False`, not a symlink). `/home/vgpnk/Projects/shokunin` does. `corpus/knowledge/checklist-execution-round17.md` lines 263–265 already recorded that split and case-corrected corpus report pointers. `SKILL.md` still presents the dead case as the current base, unmarked historical, at lines 88, 97, 106, 144, 153, 386, 482, 484, and 486 (examples: `/home/vgpnk/projects/shokunin/.ufo/prompts/`, `…/*/AGENTS.md`).

`verify_skill_checklist.py` lines 164–169 and 209–212, and `CITATION_ROOTS` at line 342, admit only `corpus/`, `verifiers/`, `opencode/`, `.ufo/`, and `../`. A named base (`~`, `/`, `$VAR`) is out of scope. Absolute paths are not subjects of `trigger.citation_resolves` or `governance.citation_resolves`. Corpus integrity only tokenizes `.ufo/reports/round-N/*.md` and ``commit `<token>` `` inside tracked `corpus/*.md` (`verify_corpus_integrity.py` lines 16–37, 134–139). Deleting or keeping these nine sites does not change any current gate verdict.

Counterexample: a reader following `SKILL.md:386` ("Checkable by reading the file") opens a path that is not on this host. The mandated repair in the checklist's own limit text is to name the real base, not to widen the root set until the dead path disappears from the subject list.

Proposed delta: case-correct those live citations to `/home/vgpnk/Projects/shokunin/…`, or mark each same-line as a historical round-7/9 observation. Do not teach the citation gate to swallow absolute paths. Owner: kotoba lane via parent. Not a GateRepair verifier edit.

### 2. High — recorded checklist green does not describe this tree; the budget rule would fail it

`SKILL.md` is 601 lines (`splitlines()`). The executed box at lines 329–331 says `File ≤ 600 lines` and binds `trigger.line_budget`. `check_line_budget` (`verify_skill_checklist.py` lines 1084–1092) FAILs when `len(lines)` exceeds the first integer in that box. `LINE_BOUND_BOX_RE` (lines 362–363) matches `File ≤ 600 lines`.

`LOG.md` lines 952–953, in this same commit, says the checklist was unchanged, exit 0, at 552 lines. Both numbers are false of HEAD. Checklist box count is still 41, so the overrun is prose/errata around the boxes, not a new box. This audit did not run the verifier; the contradiction is the committed file against the function it claims is green.

Proposed delta: do not carry the round-18 checklist exit 0 forward. Trim `SKILL.md` back under 600 or record the fail. Do not raise the box or `--max-lines` to fit 601. Owner: kotoba lane via parent. GateRepair must not re-pin the budget.

### 3. High — two harness "absence" pins cannot fail

`CHECKS` (`verify_harness_claims.py` lines 548–550) sets `oc.permission.skill_lines` and `oc.permission.skill_allow` to mode `at_least`. `baseline.json` lines 108–115 set both `expect` to 0. `evaluate()` lines 573–574 accepts any int `value >= want`. A return of the pre-rebuild count 471, or any other non-negative count, is PASS.

Round 18 (`LOG.md` lines 929–932; `baseline.json` `measured_against.round18_move`) says `evaluated permission=skill` no longer appears and is expected 0. That sentence is not what the mode implements. Contrast: `oc.log.init_count_max` is mode `equal` expect 0 (lines 80–82), so a returned old grammar does DRIFT. The permission pair does not.

Proposed delta: change those two modes to `zero` or `equal`, and add a fixture whose positive count is DRIFT. Do not leave `at_least` + `0` as an absence claim. Owner: KotobaGateRepair (implementation file only). Notified this wave.

Post-audit read, not a re-run: `verify_harness_claims.py:549-550` now says `equal` for both ids. Expect 0 is untouched. The `at_least` branch in `evaluate()` remains. `baseline.json:110` and `:114` still say `"mode": "at_least"` — documentary drift, parent errata. Absence is now what `equal` implements; this seat still has not executed the gate.

### 4. Medium — the live harness recipe still says 27 checks

`SKILL.md` lines 194 and 546, and `corpus/README.md` line 34, state 27 checks as the current instrument. The script and `baseline.json` both have 28 keys; the added key is `oc.log.skills_rescan_max` (`verify_harness_claims.py` line 538, `baseline.json` lines 120–123). `LOG.md` line 947 says `28/28`. Round-10 `LOG.md` line 188 saying 27 is a dated landing record and should stay. The recipe section is not dated that way, and line 547 calls this file the authority for every harness number in it.

`SKILL.md` line 80's "7 checks" for surfaces matches `CHECK_IDS`. The 10-check checklist count matches. The drift is specifically the harness count and the index basis cell that still describes "17/17 reproduction" and `init count == root union + builtin` as the live detector.

Proposed delta: errata the recipe and the index basis to 28 and name `oc.log.skills_rescan_max`. Do not rewrite the round-10 log line. Owner: kotoba lane via parent.

### 5. Medium — "historical" is a prose banner, not a gate class

Round 18 (`LOG.md` lines 908–914) says four dead-path sites were marked historical and no claim was deleted. The markers are sentences:

- `SKILL.md` lines 35–38, tilde path, parenthetical "historical path"
- `LOG.md` lines 469–471, same
- `corpus/knowledge/harness-verifier-round10.md` lines 112–114
- `corpus/knowledge/opencode-extraction-round14.md` lines 3–12, blockquote

No verifier has a `historical` disposition. Governance exclusion is same-line double quotes plus ellipsis / literal `round-N` (`verify_skill_checklist.py` lines 181–184, 1199–1206), and only for the closed roots, and only in `LOG.md`/`SCORECARD.md`. A tilde path is excluded by construction (line 169), so the errata is not what keeps the origin-work path green. Corpus integrity never scans `SKILL.md`.

The extraction doc's body under the banner is still present tense ("are now derived", line 16). `corpus/README.md` line 38 indexes that file as the current rule source ("opencode's 9 instruction classes are now reproduced…"). Index coverage checks the FILE column exists (`verify_corpus_integrity.py` lines 33–34), not the basis sentence. Deleting the banner does not move `corpus.index.*` or `surfaces.*`.

The census table itself was rewritten: `instruction-surface-census-round13.md` lines 162–209 are the v2.0.26 rows; the old ids at lines 172–175 are prose, and `inventory_class_ids` reads only `|`-led rows (`verify_surfaces.py` lines 457–459). `surfaces-baseline.json` live opencode row seen: `opencode:project/AGENTS.md`. That part of the historical/live split is real. The index and the extraction doc do not follow it.

Proposed delta: append an index errata that the round-14 extraction file is historical evidence and the live rule source is the census § B plus `verify_surfaces.py`. Do not delete the round-14 body. Owner: kotoba lane via parent.

### 6. Medium — province boundary is a sentence, and the sibling set is the pre-kama roster

`PROVINCE.md` is six lines: domain "prompt & skill craft", owns "the domain knowledge… above" (nothing above), refuses "anything outside". It does not list work surfaces. `PROTOCOL.md` file contract says declared surfaces must resolve. `LEARNING.md` requires Core / Frontier / Adjacent. None of those headings exist. `corpus/QUALITY.md` is absent (`ls` No such file), so the corpus contract's quality bar is also undeclared; the index gate cannot miss a file that was never added.

`SKILL.md` lines 10–12 arbitrate only kagi, kake, kasegi, kengaku, kumitate. `shokunin.conf` lines 45–61 also roster kaidoku, kama, audio, game-dev-2d, game-dev-3d, lore, revenger, tameshi, mado, tsukuroi, tabi. The gates read host surfaces the province does not name: `~/.local/bin/omp`, `~/.opencode/bin/opencode`, `~/.omp/agent/skill-descriptions.db`, `~/.omp/agent/sessions/**/*.jsonl`, `~/.local/share/opencode/log/opencode.log`. This audit did not content-read session or log bytes. Those reads are the harness gate's live path (`verify_harness_claims.py` lines 51–56, 390–398, and `oc_observations`).

Proposed delta: declare Core (skill/AGENTS/dispatch craft files), Frontier (loader-derived instruction classes), and Adjacent (sibling `SKILL.md` content, session logs, vault material) with the paths that must resolve. Do not absorb sibling skill content or session secrecy. Owner: kotoba for the province text; kagi / KagiSecrecySentinel for whether the log and session-jsonl reads are in secrecy scope; protocol for the Core/Frontier/Adjacent requirement.

### 7. Medium — no gate is registrable as conformant

`PROTOCOL.md` lines 382–402: registry rows live in the lane `SKILL.md` (name, `gate|probe`, entry command, verdict map, self-test spelling, pinned-value path, write scope, owner), and closure grades no gate conformant until that row exists. Current `SKILL.md` has commands and exit-code prose (lines 192–212, 545–553) and zero `gate|probe` rows. This was already fleet-wide at round 13; it is still true here. Self-test green is not a substitute. Frozen-run digest pins of snapshot inputs are also absent: `baseline.json` `measured_against` records binary sha256 as notes, and the census (`instruction-surface-census-round13.md` lines 53–56) already says those hashes are recorded, not check-enforced. `verify_surfaces.py` does not compare the running binary to that pin before grading strings.

Proposed delta: add six rows when the parent writes the round record. Do not copy expected values into a fleet index. Owner: kotoba for the rows; protocol for the schema. Not a verifier logic change.

### 8. Low — recheck commands and the two binary defaults disagree with the live allowlist

`verify_surfaces.py` `CALL_RE` (lines 144–147) includes `Tl|dr|GW` and says the callee list is the first thing to re-pin. The module docstring (lines 16–19) and the census method row (`instruction-surface-census-round13.md` line 47) still give only `Id|Cl|jDe|jDf|…`. A human re-running method row 1 on a binary that kept only the new names would see zero registrations while the gate still extracts. Not executed here.

`verify_harness_claims.py` follows `Path.home()`. `verify_surfaces.py` does not. Counterexample: `HOME` pointing at another user makes the harness gate look elsewhere and the surfaces gate stay on `/home/vgpnk`. On this host both paths exist and are the same files, so this is a latent split, not a current miss.

`USER_ROOTS` comment (lines 59–61) is still "Verified 2026-09-28 against the 17-name catalogue". The rebuilt binary's discovery roots were not re-derived. If omp gained a root, skills offered only there are invisible to both the offer set and a catalogue built from the same roots, and the gate can still pass. Assumption, not a measured extra root.

Proposed delta: point the census method command at `CALLEE_SHAPE` (line 149). Leave the root list alone until a binary re-derivation names a difference. Owner: kotoba; surfaces docstring/default only if GateRepair is already in that file.

## What held

- Harness `CHECKS` and `baseline.json` keys are the same 28. No missing or extra pin key.
- Surfaces check count in `SKILL.md:80` matches the tuple. Checklist check count matches. Corpus before receipt matches the 9-id docstring.
- Round-18 census table rows are the new opencode ids; old ids in that section are prose, which `inventory_class_ids` does not harvest. That is the one historical/live split the surfaces gate actually implements.
- Relocated tree HEAD matches the round-18 hash. Origin-work tree is gone. Explicit bad `--src` cannot be passed because the flag does not exist; the fail-closed branch of the wave pattern is therefore also unimplemented, not violated by a stale default.
- Catalogue floor `min(10, len(known))` (`verify_harness_claims.py` lines 376–386) is an intentional round-18 weakening so a 7-skill catalogue is admissible. It is not an accidental pin. Residual: a newest transcript block that lists the current offer set clears the contamination guard that used to require 10 names. Restoring a hard 10 would false-fail the world the move just recorded. Do not revert it in this wave.

## Unresolved debt

- Case-dead `/home/vgpnk/projects/…` citations in live `SKILL.md`. Unblock: rewrite those nine sites to the resolving case, then a parent gate run.
- Checklist recorded exit 0 at 552 lines versus 601-line file over a 600-line box. Unblock: trim or record the fail; parent runs the checklist after integration, not this seat.
- `at_least` + expect 0 on the two permission checks. Unblock: KotobaGateRepair mode change plus a positive-count fixture. Mode change read back as `equal` at lines 549–550 after this audit; baseline mode fields still say `at_least`; no positive-count fixture was added; gate not re-run.
- 27-check recipe and index basis versus 28-key instrument. Unblock: errata, not a history rewrite.
- Historical banners that no gate reads; index row 38 still present tense. Unblock: index errata naming the census § B as the live rule source.
- `PROVINCE.md` has no surfaces and no Core/Frontier/Adjacent. Unblock: declare the paths the gates already open, and route session-log reads.
- No 8-field registry rows; binary sha256 pins are not verified before grading. Unblock: rows in `SKILL.md`; digest check only if a later round adds a snapshot, not by re-pinning expects.
- `corpus/QUALITY.md` absent. Unblock: a later discernment round, not this re-census.
- Wave before receipt covers one instrument. Unblock: parent saves the other five verdict lines after integration. This seat did not run them.

## Cross-domain owners

- KotobaGateRepair: finding 3 only (`verify_harness_claims.py` mode). Not the line budget, not the case paths.
- Kotoba lane / parent: findings 1, 2, 4, 5, registry rows, province text.
- Protocol: registry schema and Core/Frontier/Adjacent requirement. Standing, not introduced at this HEAD.
- Kagi / KagiSecrecySentinel: harness gate content-reads session jsonl and `opencode.log`. This audit did not.
- LiveAnchors: line/symbol/hash claims inside the binaries and the relocated `skills/ufo/SKILL.md`. This seat did not re-measure those bodies.

## Residual risk and verification gaps

Parent integration has not happened. A later edit that trims `SKILL.md` under 600 or case-corrects the nine paths can clear findings 1 and 2 without a verifier change; a later edit that only rewords the round-18 log would leave them. Finding 3's CHECKS mode is no longer `at_least` in the working tree; the baseline mode strings and the missing positive-count fixture remain.

Not run, by wave rule: the six instruments, their `--self-test` flags, and any formatter. The 601>600 conclusion is from the committed file and `check_line_budget`, not a process exit. The `at_least`/0 conclusion was true of HEAD `02302c52`; the working tree now has `equal` at lines 549–550 and was not executed. Session and credential files were not opened. No sibling report was written.
