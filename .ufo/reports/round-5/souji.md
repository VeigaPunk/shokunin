# souji — round 5 (verification round over rounds 1–4)

Lane HEAD at report time: `ce58c2b4` (souji-shokunin identity). Single
batched dispatch: 64 seats on **openai-codex/gpt-6-luna-max**; 64/64 in
~29 min.

## Work performed

Claims: **V1 calibration** — independent verdict audit of rounds 1–4;
**V2 coverage** — missed-items sweep; **V3 operability** — tool regression
battery. The round's job was to find what the lane got wrong. It did.

**Material findings (all corrected in-round; 0 unresolved at closure):**

1. **Symlink false-SAFE class** (final judges S63/S64, independently
   reproduced): both tools' `dir_digest` used `find -type f`, silently
   dropping symlinks — a source tree with `alias.md -> payload.md` and no
   alias in the vault verified SAFE(moved-to-obsidian). Fixed fail-closed:
   any symlink in a digest scope → `symlink-present` refusal, both tools,
   both call paths. Post-fix: judges' reproduction probe refuses
   (`NOT-VERIFIED(symlink-present)`); selftests 24/24 and 35/35 green.
2. **Local-master pushed fallback** (final judges S59/S62/S63/S64): with
   zero remote-tracking refs, both tools emitted SAFE(pushed) from
   `refs/heads/master`, which cannot establish a pushed receipt. Fixed:
   no `refs/remotes/origin/*` → `NOT-SAFE(pushed-unverifiable)`;
   `tools/souji-verify.spec.md` D1 text amended accordingly. Post-fix
   probe: NOT-SAFE(pushed-unverifiable).
3. **r1 false-SAFE row** (final judges S57/S58; audit seat S12): the r1
   final table recorded logs_tier.txt SAFE(pushed) although the file was
   already deleted (delete commit a1b44b1 predates the census commit —
   the r1 parent correction verified introducing-commit ancestry but not
   existence). No operational impact (r3 re-cut to 96 actionable rows;
   the file is absent everywhere). Correction entry: pushed-receipt
   corrections must re-verify existence at correction time.

**Dispositions:** the 3 pinned gd2d registrations had been left
bare-prune-eligible after r3's unlock — re-locked durably (locks persist
until the branches are pushed or the operator dispositions). Process
findings (r1 LOG mid-file insertion; r4 read-only claim vs a sibling
seat's GUI-launch incident during adversarial tests — vault content
untouched; SKILL.md doc drift routed to r6) are recorded in
`corpus/lessons/round-5.md` with named finders.

## Landed changes

- Patched `tools/souji-verify.sh` + `tools/souji-vault-verify.sh`
  (symlink fail-closed + pushed-ref discipline), amended
  `tools/souji-verify.spec.md`; `census/round-5/` (64 fragments +
  final-judge verdicts); `corpus/lessons/round-5.md`; LOG.md; SCORECARD —
  commit `ce58c2b4`.
- Re-locked gd2d wt-r98/99/100 registrations (game-dev-2d-shokunin).

## Before → after measurements

- V1 calibration: before — no independent audit of r1–r4 existed →
  after — 8 final judges audited every round; 3 material findings caught
  by non-authors, fixed same-round, each with a re-run probe; unresolved
  contradiction count at closure: 0.
- V2 coverage: missed-items/gap table consolidated in
  `census/round-5/seat-51.json` (worktree drift re-zero, scratch watch —
  kotodama `.scratch` now **16G** and live, approval-list staleness 0,
  ledger discipline intact, /tmp residue queue for tsukuroi).
- V3 operability: both tools' selftests green post-patch (24/24, 35/35);
  live regression: kotodama NOT-SAFE (47 unpushed, 28 dirty), launch file
  SAFE(pushed), pruned /tmp/r87-B1 correctly NOT-SAFE(unreachable).

## SHONEN

- [~] SKILL.md decision tables — receipt taxonomy amended this round (symlink, pushed-ref disciplines); doc-drift fix routed to r6.
- [~] End-to-end domain task — the verification loop itself: find → fix → re-prove.
- [~] Executable without oral context — 64 zero-context seats audited and reproduced defects.
- [~] No cross-domain bleed — findings dispositioned in-lane; gd2d pins and /tmp residue routed to their owners.
