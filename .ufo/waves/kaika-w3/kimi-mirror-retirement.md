# Kimi shokunin mirror retirement findings

## Observed evidence

- `/home/vgpnk/Projects/myskills` is at HEAD `fd9ed8c`. Names-only status: unrelated dirty paths are `M godspeed/SKILL.md`, `D godspeed/filter.md`, and `D godspeed/velocity.md`. No `shokunin` path is dirty.
- The tracked `shokunin` file set is exactly:
  - `shokunin/SKILL.md`
  - `shokunin/protocol/AXES.md`
  - `shokunin/protocol/CORPUS.md`
  - `shokunin/protocol/MISSION.md`
  - `shokunin/protocol/PROTOCOL-APPENDIX.md`
  - `shokunin/protocol/PROTOCOL.md`
- Literal `shokunin` search hits occur in those six files only. No tracked installer, discovery implementation, or outside caller referencing this mirror was found in `myskills`.
- `shokunin/SKILL.md:32-41` names the five protocol files under `skills/shokunin/protocol/`; `:43-47` also names `templates/mint/`, other `templates/` files, and `scripts/`. The mirror inventory contains none of those template or script paths.
- `readlink` and `readlink -f` both show `~/.kimi-code/skills/shokunin` targets `/home/vgpnk/Projects/myskills/shokunin`.
- Existing archive examples are under `_attic/`: `_attic/local-writegoal-godspeed/SKILL.md` and `_attic/myskills-stubs/godspeed-stub/SKILL.md`. `ufo/SKILL.md:29-34` describes host/packaged copies as generated mirrors, not additional authorities. No `vendor` tree or explicit installer/discovery exclusion rule for `_attic` was found.
- The scout environment has no `lsp` device (`xd://lsp` returned “No such tool”); the findings above are literal repository searches/inventory, not semantic LSP caller proof.
- The current `/home/vgpnk/Projects/shokunin` checkout is at HEAD `88b130f`; names-only status shows `M README.md`. No file was changed.

## Recommendation

Delete the six tracked mirror files listed above and let the now-empty `shokunin/` directories disappear; do not move the old `SKILL.md` into `_attic` and do not leave a thin binding. The repository has attic examples, but no evidence establishes that the regular installer or Kimi discovery excludes nested archived `SKILL.md` files. Deleting this obsolete copy avoids that unresolved duplicate-discovery risk and avoids retaining an active shim after canonical authority is chosen.

No tracked myskills caller update is indicated. The sole observed host binding is the symlink above; the parent-owned cutover should repoint that link directly to the canonical skill. The old `SKILL.md`'s internal load references disappear with the mirror.

## Limits / unresolved

There is no tracked installer/discovery source in `myskills`, so source evidence cannot say whether a regular installer would recreate the symlink or whether the Kimi loader recursively discovers archived `SKILL.md` files. Those behaviors remain unverified; do not claim they are false. Repo archive examples and the mirror-authority wording are convention evidence only, not loader guarantees. Confidence is high for the six-file tracked inventory and current symlink target, moderate for the repository convention, and low/undetermined for installer and recursive-discovery behavior.