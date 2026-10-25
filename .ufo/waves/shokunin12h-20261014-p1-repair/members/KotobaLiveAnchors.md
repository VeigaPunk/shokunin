# KotobaLiveAnchors — advisory re-census

Seat: scout. Not a judge verdict, round report, receipt, or admission. No lane files edited. No gate/build/lint/test run. Kumitate round counts were not used.

## Revisions

| Surface | Command | Measured |
|---|---|---|
| Lane HEAD | `git -C kotoba-shokunin rev-parse HEAD` | `02302c521b933c55fc4be79193e61537e3380751` (matches `baselines.json`; porcelain `?? plans/` only) |
| Designated source | `git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD` | `964f443ee53df0ce06bd689af01f0dea031b01f9` (`2026-10-12 18:32:12 -0300`) |
| omp binary (declared local surface, not the source tree) | sha256 of `~/.local/bin/omp` | `ff59fc1b484c1308a7247ad208305005627b3fac62b440737c2b1835ac32074e` (276199392 bytes) |

The harness implementation named by the live module comment `packages/coding-agent/src/extensibility/skill-descriptions.ts` is **not a file in the designated tree** (`git ls-files` empty; `test -e` false). Symbol claims that name that path are binary-module comments, not source lines. No source line was invented for them.

## Classifications

`line-drift` = the cited organ still exists, at a different line. `symbol-drift` = minified binder/callee moved; group, file, or constant did not. `genuine-defect` = the cited count or phrase is absent, not relocated. `agrees` = measured value matches the live sentence.

### Source-tree claims

1. **LOG.md round 18 HEAD `964f443e` — agrees.** Full hash above. Proposed anchor: keep the short prefix only with the full hash beside it. No delta.

2. **Live negative: `skills/ufo/SKILL.md` no longer carries the 690-char description — agrees.** YAML `>` fold of `description:` in `/home/vgpnk/Projects/ufo-fsd-alpha/skills/ufo/SKILL.md` is **605** chars (606 if the `>` trailing newline is counted; raw indented block 597). File sha256 `4708d14d99fcb5184f72eb386d9e9efeefcafe96a4874d0314eb54f773fe7ef2`, 600 lines, 36375 bytes. Twelve copies under the tree share that hash (root `skills/`, `.omp/skills/`, `.cursor/skills/`, and the substrate packs). None is 690. The historical "10 substrate packs" sits inside the same errata sentence and is not re-asserted as current; measured pack count is 12. Do not re-pin 10. Owner if that numeral needs an errata: HistoryClaims. Not a live defect.

3. **Live negative: `ports/xbgst-codex` absent — agrees.** `ls ports` returns `ufo-core-runtime` only. Deletion is historical (`467dacbb`, not re-measured as a line). No delta.

4. **`SKILL.md:71-72` and `:456` — godspeed is 18 lines, deferral `Read directive.md … apply verbatim` — genuine defect, not line-drift.**
   - Cited path `~/.agents/skills/godspeed/SKILL.md`: `wc -l` is **17**. `grep -c 'apply verbatim'` is 0. The file has no `directive.md` deferral (lines 1-17 are frontmatter plus four numbered axioms and one stop-asking heading).
   - Source authority `skills/godspeed/SKILL.md`: `wc -l` is **28**. Deferral is line 14: `**Read directive.md before you act.**` The quoted tail `apply verbatim` occurs 0 times in that file and 0 times under `skills/` and `~/.agents/skills`. A second copy `.cursor/skills/godspeed/SKILL.md` is 24 lines, also not 18.
   - Proposed anchor: `skills/godspeed/SKILL.md:14` at `964f443e`, and stop citing 18 / `apply verbatim`. Proposed delta is prose in `SKILL.md` only; this seat did not edit it. Owner: parent (live craft sentence). Not a gate file.

5. **`SKILL.md:64` exemplar `wwkd L16-24` — agrees at the start line; span is wider than the one-line organ. Not line-drift of the heading, not a defect.** `skills/wwkd/SKILL.md:16` is still `# What Would Karpathy Do — Planning Posture`. Lines 18-20 are a paragraph; 22-24 start the authoring-wiki note. Tighter anchor if rewritten: `:16` only. Heading symbols with no line pin: `## Refusals` at **182**, `## Source Excerpts` at **222**. Both agree.

6. **`SKILL.md:480` live source bullet `~/.config/opencode/skills/ufo/SKILL.md` (I1-I10) — cited path deleted; content relocated, not line-drift of a source line (no line was cited).** `test -e` on the host path is absent. Invariants are in the source tree: `skills/ufo/SKILL.md:24` `## Load order (on every activation)`; `:171` `I1`; `:186` `I10`. Proposed anchor: `skills/ufo/SKILL.md:171-186` at `964f443e`. Owner for the dead host path: HistoryClaims. Do not treat `:171` as the old host file's line.

### Binary symbol / count / hash claims (no source line exists)

Measured by a bounded byte scan of `~/.local/bin/omp`, not by running `verify_harness_claims.py` or `verify_surfaces.py`.

7. **Template hash and 273-byte count — agrees on the binary; absent from the source tree.** Unique anchor `Compress into one routing hint`, NUL-terminated, contains `{{name}}` and `{{description}}`. Length **273**. sha256 `c1f03c8e248eb40ec7735baab67f686fc2f254e00d2a0241ff220628461bdb51` (matches `verifiers/baseline.json` `omp.elf.template_sha256` / `omp.elf.template_bytes`). No `compress-description-*.md` file in the source tree. Proposed anchor stays the binary blob, not a checkout path.

8. **`_8n=100`, `idl=160`, `adl=12`, `A8n`, `H7s`, `ldl` — symbol-drift, not a constant defect, not a source line.** Those identifiers are absent as assignments (`_8n=100` count 0, `idl=160` count 0, `function A8n` count 0). Current module comment still reads `// packages/coding-agent/src/extensibility/skill-descriptions.ts`, then `var A = 100; var _ = 160; var b = 12;`. Truncator is `function eit` (`previewSkillDescription` export alias): ws-collapse, `length <= A`, `slice(0, A - 1)`, sentence keep if `>= 40`, else last space plus ellipsis. Acceptance `function L` uses `_` and `b`; the error string is still `max 12 words, 160 chars`. Key function is `R`, still `sha256(k | 0x00 | name | 0x00 | description)`. Proposed anchor: that `var A = 100; var _ = 160; var b = 12;` statement beside the module comment. Do not re-pin `_8n` / `A8n`.

9. **Census section A call shapes `jDe(e,Pqr,"AGENTS.md")`, `jDe(e,BWr,"CLAUDE.md")`, `Id(...)`, `Cl(...)` — symbol-drift. Class pairs agree. `jDe(` count 0; `Pqr = "agents-md"` count 0; `BWr = "claude-md"` count 0.** Measured replacements in the same binary:

| Live claim | Measured call | Group/file |
|---|---|---|
| `jDe(e,Pqr,"AGENTS.md")`, `Pqr="agents-md"` | `GW(u, s1, "AGENTS.md")` with `var s1 = "agents-md"` | unchanged |
| `jDe(e,BWr,"CLAUDE.md")`, `BWr="claude-md"` | `GW(u, a1, "CLAUDE.md")` with `var a1 = "claude-md"` | unchanged |
| `Id(e,"opencode","AGENTS.md")` | `Tl(u, "opencode", "AGENTS.md")` | unchanged |
| `Id`/`Cl` gemini `GEMINI.md` / `system.md` / `SYSTEM_TEMPLATE.md` | `Tl` / `dr` with the same three literals | unchanged |
| `Cl(e,"github","copilot-instructions.md")` | `dr(u, "github", "copilot-instructions.md")` | unchanged |
| `Id(e,"windsurf","memories/global_rules.md")` | `Tl(u, "windsurf", "memories/global_rules.md")` | unchanged |

Proposed anchor: cite the group/file literals, and treat the callee (`GW`/`Tl`/`dr`) as build-local. `verifiers/verify_surfaces.py` `CALL_RE` (lines 144-147) already lists `Id|Cl|jD[ef]|Tl|dr|GW`, so this is not a missing-callee gate defect on the text read. Parent still runs the gate; this seat did not. Owner of a census evidence-column rewrite: parent / HistoryClaims. Not GateRepair unless a post-integration run fails.

## Proposed delta

Only one live sentence is false rather than renamed:

- `kotoba-shokunin/SKILL.md:71-72` and `:456`: drop `18 lines` and `apply verbatim`. Point the minimal-file exemplar at `skills/godspeed/SKILL.md:14` (`Read directive.md before you act.`) under source `964f443e`, or at the host file's actual 17 lines without the deferral quote. Do not keep both.

Optional, not required to make a false sentence true:

- Census section A evidence cells: replace `jDe`/`Id`/`Cl`/`Pqr`/`BWr` with the measured callees, or say the callee is build-volatile.
- `SKILL.md:480`: the host `opencode/skills/ufo` path does not resolve; the I1-I10 list is `skills/ufo/SKILL.md:171-186`.

No verifier, baseline, or fixture change is justified by these measurements. Constants 100/160/12/40 and the template sha256 still match the pins the gate enforces.

## Unresolved debt

- **No source-tree line for the harness.** `packages/coding-agent/...` is a binary module comment. Unblock: declare a coding-agent checkout before anyone pins a source line; until then the anchor is the binary constant statement above. Owner: parent, if a later round wants source-line pins. Not this seat.
- **Minified census callees will move again on the next omp rebuild.** Unblock: evidence cells should pin group/file literals. Owner: parent prose, after the gate run. Not a current gate-regex hole on the text read.
- **Historical "10 packs" / 690-char byte** already carry a 2026-10-14 errata. Current identical-copy count is 12 at sha256 `4708d14d…`. Do not re-pin either number. Owner: HistoryClaims if the numeral inside the historical clause must be marked describe-don't-pin more loudly.

## Cross-domain

- HistoryClaims: dead host path `~/.config/opencode/skills/ufo/SKILL.md`; already-errata'd origin-work path and `ports/xbgst-codex`.
- GateRepair: no remaining implementation defect found in the call-shape regex. Do not re-pin baselines to hide symbol renames.
- Parent: the godspeed 18-line sentence is the only live false claim that asks for a prose delta. This report is not that edit.
