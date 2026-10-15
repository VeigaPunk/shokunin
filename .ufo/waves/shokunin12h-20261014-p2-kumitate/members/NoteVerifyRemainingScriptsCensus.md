# NoteVerifyRemainingScriptsCensus — S8 note honesty (round 32)

**Seat:** `NoteVerifyRemainingScriptsCensus` (leaf, read-only). **Family:** S8 remaining scripts.
**Note verified:** `kumitate-shokunin/corpus/knowledge/remaining-scripts-census.md`
**Note pin:** sha256 `298ce94097d2632e0ed2baae5ff44b9bfdf0d391fd59002c1bdc4a9f296df82c`, 846 lines.
**Lane HEAD at write:** `cdeaa0a608f279c137ae9965a6ca91e09f19ab30` (moved during this seat; dispatch pin was `175de6ba2e9e904010411b19cab27e0af9aad3d4`). The note hash above is what was checked.
**Origin:** `/home/vgpnk/Projects/ufo-fsd-alpha` HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9`.
**This seat edited nothing** except this report. Not a verdict.

## Axes (named, not judged)

- **coverage:** each `##` member section exists in the live origin tree and carries a live own-file anchor; live S8 members with no section are the gap.
- **operability:** every count below has its command; both sides of every `comm -3` are `LC_ALL=C sort`ed.
- **calibration:** gate-live vs pathish-dead cites are split; stale Limits / probe transcript / registry prose are recorded, not fitted.

## Files inspected

| Path | Role |
|---|---|
| `kumitate-shokunin/corpus/knowledge/remaining-scripts-census.md` | S8 note (section form) |
| `kumitate-shokunin/SCORECARD.md` | S8 registry cell (read only; working tree) |
| `kumitate-shokunin/scripts/claims-check.mjs` | frozen anchor rule (`RE_PATHISH`, `RE_BARE`, liveness) |
| `kumitate-shokunin/corpus/README.md` | map row for this note |
| origin `scripts/*.mjs` + `scripts/*/` | live script-layer universe |
| origin S8 members listed below | existence + anchor endpoints |

## Anchor rule used

Frozen `scripts/claims-check.mjs` header: a candidate is any `<pathish>:<N>[-<M>]` that uniquely resolves under `--src`, plus any bare `:<N>[-<M>]` bound to the section's own file. Live means `1 ≤ a ≤ b ≤` line count (split on `\n`) and both endpoint lines non-blank. A section is honest when ≥1 own-file candidate is live. Symbol hit (backticked token, no `/\:.` or space, length ≥ 3, verbatim in the file) was recorded beside that, not substituted for it.

## Live S8 derivation

Universe = `scripts/*.mjs` plus every file at `scripts/*/` depth ≥ 2. Subtract live S1–S7 only (registry names + live `probe-*.mjs` / `fake-omp.mjs` + live files under `collect-omp-native-handoff-lib/` and `ufo-sighting-lib/`). Not widened to other families. Top-level non-`.mjs` shells are outside the universe and were not absorbed.

```bash
cd /home/vgpnk/Projects/ufo-fsd-alpha
{ ls -1 scripts/*.mjs; find scripts -mindepth 2 -type f; } | LC_ALL=C sort -u > /tmp/s8-all-scripts.txt
# S1–S6 named tops + live libs + live probe-*.mjs + fake-omp.mjs
# written to /tmp/s8-s1s7-indep.txt, then LC_ALL=C sort -u
comm -23 /tmp/s8-all-scripts.txt /tmp/s8-s1s7-indep.txt > /tmp/s8-live.txt
wc -l /tmp/s8-all-scripts.txt /tmp/s8-s1s7-indep.txt /tmp/s8-live.txt
```

**Observed:**

```
S_members 91
S1-S7 indep 28
S8 63
```

Note's embedded exclusion heredoc vs this independent list:

```bash
comm -3 /tmp/s8-s1s7-indep.txt /tmp/s8-note-excl.txt
```

**Observed:** empty. `comm` exit 0. No exclusion-list path was absent from the tree.

Arithmetic: 91 − 28 = 63. Of the 63: 54 top-level `*.mjs` + `charter-scribe/` 5 + `lean-cargo/` 4. Class labels on the note table: 23 suite + 32 tool + 3 shim + 4 asset + 1 doc = 63.

`wc -l` of the 63, origin worktree: `36827 total`. Table `L` column vs `wc -l`: **0 mismatches** (63 rows).

### Exact live member list (authoritative for this seat)

1. `scripts/charter-scribe/config.json`
2. `scripts/charter-scribe/prompts/kimi-update.prompt.txt`
3. `scripts/charter-scribe/sync.mjs`
4. `scripts/charter-scribe/systemd/charter-scribe.service`
5. `scripts/charter-scribe/systemd/charter-scribe.timer`
6. `scripts/check-hand-authored-sets.mjs`
7. `scripts/check-hand-authored-sets.test.mjs`
8. `scripts/check-routing-free-config.mjs`
9. `scripts/check-routing-free-config.test.mjs`
10. `scripts/fleet-dispatcher.test.mjs`
11. `scripts/fleet-ledger-read.mjs`
12. `scripts/fleet-ledger-read.test.mjs`
13. `scripts/fleet-ledger-rotate.mjs`
14. `scripts/fleet-ledger-rotate.test.mjs`
15. `scripts/fleet-selfheal-verify.mjs`
16. `scripts/gates-plan.mjs`
17. `scripts/land-fleet-run.mjs`
18. `scripts/lean-cargo/README.md`
19. `scripts/lean-cargo/bin/cargo-shim.sh`
20. `scripts/lean-cargo/install-shim.sh`
21. `scripts/lean-cargo/measure.sh`
22. `scripts/local-helper.mjs`
23. `scripts/omp-native-shutdown.mjs`
24. `scripts/omp-role-work.mjs`
25. `scripts/omp-wave-context.mjs`
26. `scripts/prepare-ephemeral-fleet.mjs`
27. `scripts/prepare-ephemeral-fleet.test.mjs`
28. `scripts/prepare-ephemeral-l1.mjs`
29. `scripts/primeagent-recovery-assess.mjs`
30. `scripts/primeagent-refinement-ledger.mjs`
31. `scripts/project-devin-subagents.mjs`
32. `scripts/render-seat-tables.mjs`
33. `scripts/render-seat-tables.test.mjs`
34. `scripts/sync-global-routing.mjs`
35. `scripts/sync-ufo-contracts.mjs`
36. `scripts/the-tick-config.mjs`
37. `scripts/ufo-credential-screen.mjs`
38. `scripts/ufo-drills.mjs`
39. `scripts/ufo-godspeed-inject.test.mjs`
40. `scripts/ufo-l0-monitor-hook.test.mjs`
41. `scripts/ufo-l0-monitor.test.mjs`
42. `scripts/ufo-l0-watch.test.mjs`
43. `scripts/ufo-mission-activity.mjs`
44. `scripts/ufo-mission-activity.test.mjs`
45. `scripts/ufo-mission-lifecycle.mjs`
46. `scripts/ufo-mission-observation.mjs`
47. `scripts/ufo-mission-observation.test.mjs`
48. `scripts/ufo-native-names.mjs`
49. `scripts/ufo-night-watchdog.test.mjs`
50. `scripts/ufo-refinement-context.mjs`
51. `scripts/ufo-refinement-context.test.mjs`
52. `scripts/ufo-route-preflight.mjs`
53. `scripts/ufo-route-preflight.test.mjs`
54. `scripts/ufo-stale-watchdog.test.mjs`
55. `scripts/ufo-state-census.mjs`
56. `scripts/ufo-state-census.test.mjs`
57. `scripts/ufo-state-retention.mjs`
58. `scripts/ufo-state-retention.test.mjs`
59. `scripts/ufo-statusline-hook.test.mjs`
60. `scripts/ufo-swarm-collect.test.mjs`
61. `scripts/ufo-swarm-wave.test.mjs`
62. `scripts/ufo-watchdog-repend.mjs`
63. `scripts/ufo-watchdog-repend.test.mjs`

## Section boundary

Non-member `##` headings (not counted): `Membership and measurement`, `Composition and conventions`, `Member-completeness probe`, `Limits of this note`, `Citation ledger`.

Member headings: 63, all `` ## `scripts/…` ``. No duplicates.

```bash
NOTE=kumitate-shokunin/corpus/knowledge/remaining-scripts-census.md
grep -oE '^## `scripts/[^`]+`' "$NOTE" | sed -E 's/^## `//; s/`$//' | LC_ALL=C sort > /tmp/s8-headings.txt
awk -F'`' '/^\| `scripts\//{print $2}' "$NOTE" | LC_ALL=C sort > /tmp/s8-table.txt
echo "headings $(wc -l < /tmp/s8-headings.txt) table $(wc -l < /tmp/s8-table.txt)"
comm -3 /tmp/s8-live.txt /tmp/s8-headings.txt
comm -3 /tmp/s8-live.txt /tmp/s8-table.txt
comm -3 /tmp/s8-headings.txt /tmp/s8-table.txt
```

**Observed:** headings 63, table 63, all three `comm -3` empty.

### Sections whose member is absent

**None.** Every current member heading names a file present in the origin worktree.

### Declared members with no section

**None.** Live S8 (63) = note table (63) = member headings (63).

### Sections added / removed by this seat

**Added 0. Removed 0.** Read-only.

Delta already in the note versus dispatch pin `175de6ba` (heading `comm`, `LC_ALL=C sort` both sides): dispatch headings 60, current 63.

Removed headings, each `test -f` → **ABSENT** (not left as phantoms in the current note):

- `scripts/charter-scribe/sync.test.mjs`
- `scripts/local-helper.test.mjs`
- `scripts/omp-global-config.test.mjs`
- `scripts/omp-role-work.test.mjs`
- `scripts/prepare-ephemeral-l1.test.mjs`
- `scripts/primeagent-refinement-ledger.test.mjs`
- `scripts/project-devin-subagents.test.mjs`
- `scripts/run-omp-native-trial.test.mjs`
- `scripts/sync-global-routing.test.mjs`
- `scripts/ufo-drills.test.mjs`
- `scripts/ufo-ground-handler.test.mjs`
- `scripts/ufo-mission-lifecycle.test.mjs`
- `scripts/ufo-mission-result.test.mjs`
- `scripts/ufo-statusline-gate.test.mjs`
- `scripts/ufo-statusline-hook-machinery.test.mjs`

Added headings (all in the live list above, each with a live own-file anchor): the 18 paths the note's `## Limits` removal record names (`check-hand-authored-sets` through `ufo-state-census.test.mjs`). Confirmed present; not re-invented here.

## Anchor results

Independent walk of the pinned note (same regexes as `claims-check.mjs`) against origin worktree bytes:

| Result | Count |
|---|---:|
| Member sections | 63 |
| Live own-file anchor (honest) | **63** |
| Of which ≥1 live **pathish** own-file anchor | 61 |
| Of which live **only** via bare `:<N>` | 2 |
| No own-file anchor / all own anchors dead | 0 |
| Verbatim symbol miss | 0 |

Gate cross-check (read-only, not the proof):

```bash
cd /home/vgpnk/Projects/shokunin/kumitate-shokunin
node scripts/claims-check.mjs --row S8 --src /home/vgpnk/Projects/ufo-fsd-alpha
```

**Observed:** `ROWS: 1  YES: 1  NOTES: 1  SECTIONS: 63` / `ROW S8 form=section notes=1 sections=63 adv=0` / `SUMMARY: errors=0 warnings=0` / `CLAIMS: MATCH (rows=1 yes=1 notes=1 sections=63 adv=0)` exit 0. JSON: 63 sections, 0 with `live` false or `symbolHit` false, findings none.

### Bare-only (still honest under the frozen rule; pathish cite is dead)

These two count in the 63 because a bare continuation resolves to a non-blank line of the section's own file. The explicit pathish cite does not.

`scripts/charter-scribe/sync.mjs` — `wc -l` = 844.

- Dead pathish: `:665` blank (the `runBeat` cite). `:1054` and `:1084` are past EOF (bare, also dead).
- Live bare: `:57`, `:85`, `:104`.
- Observed `:57`: `// allocation, and the size+1 slack buffer fails closed if the file grows`
- Observed `:85`: `throw new Error(\`beat input exceeds ${MAX_BEAT_INPUT_BYTES} bytes: ${path}\`);`
- Observed `:104`: `}`

`scripts/ufo-drills.mjs` — `wc -l` = 1726.

- Dead pathish: `:4450` out of range (the `main` cite). Bare `:232` blank. Bare `:4597` out of range.
- Live bare: `:264` only.
- Observed `:264`: `` `outcome ${JSON.stringify(got)}, expected ${JSON.stringify(expect.outcome)}`); ``

The preceding pathish token in both sections is the section's own path, so the note's "last full path" reading and the gate's "bare binds to own file" reading agree. A parent who wants every named pathish cite live still has a repair on these two. This seat did not edit them.

### Pathish-live sections that also carry dead pathish cites

Not failures. Each has ≥1 live pathish own-file anchor. Dead cites (blank or past EOF) left in the prose:

| Member | Dead pathish |
|---|---|
| `scripts/fleet-ledger-read.mjs` | 78 blank; 1036, 1067 oor |
| `scripts/fleet-ledger-rotate.mjs` | 1450, 1522 oor |
| `scripts/fleet-ledger-rotate.test.mjs` | 46, 51 blank; 2360, 2634 oor |
| `scripts/local-helper.mjs` | 363 oor |
| `scripts/prepare-ephemeral-l1.mjs` | 28 blank; 1111, 1226, 1377, 1433 oor |
| `scripts/primeagent-recovery-assess.mjs` | 92 blank; 723, 724, 727, 728, 729, 1076, 1686, 1785, 1787, 1829, 1845 oor |
| `scripts/project-devin-subagents.mjs` | 450 oor |
| `scripts/sync-ufo-contracts.mjs` | 481 blank |
| `scripts/ufo-l0-monitor-hook.test.mjs` | 43 blank |
| `scripts/ufo-mission-lifecycle.mjs` | 278, 280 oor |
| `scripts/ufo-mission-observation.test.mjs` | 31, 34 blank; 112, 131, 174, 208 oor |
| `scripts/ufo-state-retention.test.mjs` | 1019, 1355 oor |
| `scripts/ufo-swarm-collect.test.mjs` | 1767, 2028, 2088, 2205 oor |
| `scripts/ufo-swarm-wave.test.mjs` | 573 blank |

## Honest count

**63.**

- Sections whose member is absent: **0**
- Declared live members with no section: **0**
- Sections with a live own-file anchor: **63 / 63**
- Pathish-live subset: **61**; bare-only subset: **2** (listed above; still resolving)

## Calibration debt (not a membership miss)

- `## Limits` still says `scripts/ufo-l0-monitor.test.mjs` is 1345 under `wc -l` and the set is 54874. Live `wc -l` is **1415**; S8 total is **36827**. The table in the same note already says 1415. Stale paragraph, not a phantom member. Owner: parent / note maintainer.
- `## Member-completeness probe` Arm 1 "verbatim" block still prints `60` from `/tmp/kumitate-r13/s8-members.txt`, while the command comment says expect 63. That recipe's `sort` is not `LC_ALL=C sort`. This seat's `LC_ALL=C` `comm -3` was empty. Owner: parent, if that recipe is re-run.
- Working-tree S8 registry cell starts `63 members` (that is why `--row S8` does not fire `MEMBER_COUNT_DRIFT`) but the same cell still says `60 of 60` and `ls scripts/*.mjs → 72 − 13 − 9 = 50`. Owner: parent registry prose. This seat did not edit `SCORECARD.md`.
- Origin dirty path inside S8: `scripts/fleet-dispatcher.test.mjs` is `+10` vs HEAD (`git diff --stat`; worktree `wc -l` 3278, `git show HEAD:… | wc -l` 3268). The note table uses 3278, matching the worktree the gates read. Its live pathish anchor is line 3, present in both. No honest anchor sits only in the dirty tail (3269–3278).

## Cross-domain findings (owner named; not absorbed into S8)

- **S2:** `scripts/collect-omp-native-handoff-lib/` is 5 files, not 6. `refusal-line.mjs` is absent (pre-registered). Owner: S2.
- **S4:** `scripts/ufo-sighting-lib/` is 4 files, not 26. `scripts/ufo-sighting` (bash, no extension) exists and is **outside** the `S_members` walk (top-level non-`.mjs`). Owner: S4. Not an S8 member.
- **S7:** live subtraction used 6 files (`probe-ufo-route-health.mjs`, `probe-redact.mjs`, three `probe-token-plan-*.mjs`, `fake-omp.mjs`). Absent, not moved into S8: `scripts/atomic-write.mjs`, `scripts/probe-ufo-route-health.test.mjs`, `scripts/probe-redact.test.mjs`. Owner: S7.
- **Universe shells, not S8:** `scripts/dev-verify.sh`, `gates.sh`, `self-iter.sh`, `smoke.sh`, `ufo-night-watchdog.sh` (the note's five) plus live extras `scripts/nc5-origin-sync.sh`, `scripts/nc5-seat-watch.sh`, `scripts/ufo-night-watchdog-lib.sh`. None appear in the `S_members` walk. Owner: parent / registry definition. Do not widen S8 to hold them.

## Unresolved blockers

**None for the assigned question.** Current note: no phantom member section, no live S8 member without a section, honest own-file-anchor count **63**. Cite repairs on the two bare-only sections and the dead-pathish list are optional prose work, not missing members.

End of advisory. Not a verdict.
