# Round 34 — mado

Lane: `mado-shokunin`. Lane tip at report time: `dff394109f3cc3d851309ad7c67dd3b35b46adf2`
(`master`, pushed). Round shape: **one v2 wave, 64 seats**, 25 of them attack roles (39%).
Resumed round — the prior attempt froze both predicates and landed the data before its
provider route died; this attempt inherited both, re-verified them, and re-declared
nothing.

## Work performed

**Declared claims (1–3, distinct axes, frozen before data):**

- **C1 — coverage** (tied-lowest axis; the axis round 33 missed). The Waybar
  event-socket client route: one admitted knowledge entry
  `corpus/knowledge/waybar-module-text-route-r25.md` plus two normalized registry rows
  (S201, S202), both sources re-opened by the lane on 2026-10-24.
- **C2 — calibration** (tied-lowest axis). The published S189 queue-cap line number must
  match a re-read of the pinned fetch `.ufo/waves/round-32/fetch/S189.bin`.

Both predicates are frozen in `.ufo/waves/round-34/registration.md` and are byte-identical
in `c1/count.py` + `c1/frozen.json` and `c2/count.py` + `c2/frozen.json`. The **round-33
counters were not amended**: their blob ids are identical at the round-33 freeze
`9a46ccf3282117f960b8d53cd71599a91f388ee3`, the round-33 tip
`69f72100bee31a60b811f8fbbe7796db883e17b3` and this round's tip
(`.ufo/waves/round-34/w1/reports/RevFrozenBlobs.md`).

**Work items, with evidence pointers:**

- The prior attempt froze `PRED-C1-r34-v1` and `PRED-C2-r34-v1` at
  `3420e827bd7b21b1374b23245526554ffd20d096`, with pre-data receipts in
  `.ufo/waves/round-34/controls/`. I re-ran every one of them at write time: the symlink
  crib, the symlinked-entry, symlinked-parent and symlinked-sources trees, the hardlink
  and do-nothing receipts, the entries-only, rows-only and used-by-prefix trees **all**
  print `TARGET_MISSED` exit 1; only the regular-file golden tree prints
  `TARGET_MET` exit 0 (`.ufo/waves/round-34/w1/reports/RevC1Matrix.md`,
  `.../RevReceiptsBytes.md`). The r33 counter still prints `TARGET_MET` on its own crib
  and was **not** substituted for the frozen one
  (`.ufo/waves/round-34/controls/r33-counter-on-its-crib.txt`).
- The data landed **after** the freeze at `fa7ba11346116672352b5d41494141c5c4d738d0`:
  `corpus/knowledge/waybar-module-text-route-r25.md`, `corpus/SOURCES.md:203-204`,
  `corpus/README.md:58`, and the calibration publication in `SCORECARD.md`.
- One v2 wave, 64 seats, validated before dispatch by
  `ufo-swarm-wave.mjs run --spec .ufo/waves/round-34/w1-spec.json` under
  `scripts/hyaku/ufo-wave-policy-v2.json` (band 64–128, `spawn=64`, `resume=0`,
  `calls=1`, no refusal). Spec: `.ufo/waves/round-34/w1-spec.json`; payload:
  `.ufo/waves/round-34/w1-taskcall.json`; dispatcher: `.ufo/waves/round-34/dispatch-w1.sh`.
  Seat plan, exits and manifest: `.ufo/waves/round-34/w1/{seat-plan.tsv,exit-codes.tsv,manifest.json}`.
  **64 dispatched, 64 finished, 64 reports written, 0 dead seats, 0 missing.** Roles:
  executor 14, scout 12, reviewer 10, critic 8, scribe 7, connector 4, mutation-tester 3,
  sentinel 2, revenger 2, simplifier 2 → 25 attack roles (reviewer + critic +
  mutation-tester + revenger + sentinel) = 39%. Answering models as routed by the
  operator's table (`task.agentModelOverrides` in `~/.omp/agent/config.yml`, read only,
  never modified): `@m_zfl` 21, `@m_sol` 20, `@m_flash` 19, `@m_grok` 4.
  The Kimi subagent surface has no `task` tool, so the validator's single batched
  `taskCall` was issued as one concurrent `omp` launcher that consumes the payload
  verbatim; the parent blocked on `wait` until settlement and then wrote the manifest
  (`dispatch.out`: `64/64 finished; reports=64; dead=[] missing=[] no_report=[]`).
- **Mutation testing of the new counter** (`.ufo/waves/round-34/w1/reports/MutC1Drop.md`,
  `.../MutC2Drop.md`, `.../MutC1ClauseMap.md`): the per-component path walk and the
  whole-token `used-by` equality are load-bearing — their mutants wrongly meet
  `controls/extra/symlink-parent` and `controls/extra/used-by-prefix`. The sha256 pin and
  the nlink check are load-bearing against scratch cribs. Two clauses are honestly
  **redundant** under this frozen spec and are recorded as such: the 1–25 word bound
  cannot fail once `found == quote` holds, and the `S_ISLNK`/`O_NOFOLLOW` pair is
  TOCTOU-only protection that no static tree can kill.
- **Repair — the line-169 quote correction.** Re-verified against the pinned bytes
  (6479 B, sha256 `eea605dfe5ce09e1f92a67ec478bf61a19894c6e0ee3302c0393521a2ee9540d`):
  line 128 is the `formatEvent` `eventString` assignment, line 169 is
  `const size_t MAX_QUEUED_EVENTS = 64;`. **Both line numbers are correct for their own
  quote.** The r33 closure read the round-33 lesson's "line 128" as a false statement
  about the queue-cap quote; the lesson was speaking about the register's quoted span.
  The repair is an appended disambiguation in `corpus/lessons/round-33.md` naming both
  lines and both quotes — not a retraction, and not a rewrite
  (`.ufo/waves/round-34/w1/reports/{ScoutS189,RevC2Truth,MutC2Drop}.md`).
- **Repair — the literature reject, restated against the opened file's ids.**
  `two-literature-drift-r26.md` cites **S206, S209, S210, S211**; `S199` appears nowhere
  in it, and the S195/S198/S199 named in the round-32 lesson were staged-register ids.
  Its tier-C community rows are **S210 and S211** (CSDN posts), so the reject still
  holds on two independent grounds — documentation localization is outside PROVINCE.md,
  and tier C may not be the sole support. Recorded with reason and flip in
  `corpus/lessons/round-34.md` §Gate
  (`.ufo/waves/round-34/w1/reports/CritLiterature.md`).
- **Repair — the 12 undisclosed seat scratch trees and the 7 disclosed leftovers, by
  re-verification, not a sweep.** The wave hashed every scratch file against all HEAD
  blobs and classified each tree (`.../ScoutScratch12.md`, `.../ScoutK2.md`,
  `.../ScoutControls7.md`). Disposition: the 6 control fixture trees and the 12 seat
  scratch trees are **committed** this round, so every round-33 receipt is now
  re-derivable from committed bytes alone;
  `.ufo/waves/round-33/scratch/ExecK2Receipts` (495,961,904 bytes / 30,892 files — three
  throwaway git clones whose measured outputs are pasted verbatim into the committed
  `.ufo/waves/round-33/w1/reports/ExecK2Receipts.md`) was **moved out of the lane tree**
  to `/fast/scratch/mado-r33-k2-receipts/` with an `ORIGIN.md`, byte count identical
  before and after. Not swept, not silently dropped.
- **Repair — `ScoutRound30.md` citation.** The five rewritten round-30 seat reports are
  cited as the rewritten, final-pass reports verified by `ScoutRound30` (round-33 w1) and
  committed at `d40b35f90ad8bf630ad9404d25aeee1d9737f300`; their earlier committed drafts
  (`15ddd7d`/`a0dd664`/`274f735`) are superseded and must not be quoted
  (`.ufo/waves/round-34/w1/reports/ConnRound30Cite.md`). No round-34 finding relies on
  those bytes.
- **Repair — the axis-gate selftest transcript, committed.**
  `.ufo/waves/round-34/controls/axis-selftest.txt`: `MADO_AXIS_SELFTEST: 18/18 assertions
  passed` exit 0, and the live gate `MADO_AXIS: checked=3 mismatched=0
  rev=fa7ba11346116672352b5d41494141c5c4d738d0` exit 0. The publication "operability
  selftest 12/12" appended with the data commit conflated the operability **axis
  fraction** (12/12) with the gate **selftest** (18/18); the correction is appended in
  `SCORECARD.md`, the axis table itself is unchanged.
- **Assimilation (item 10), applied only after the counter was frozen.** Package
  `/home/vgpnk/Projects/shokuknow/merge/mado/` read-only; 1–3 entries on ONE theme
  (the Waybar event-socket route). Id-collision check in scratch before any append —
  190 registry ids vs 140 staged ids, `collisions` empty, and the 0–3-leading-space
  extractor proven able to fail on an indented `  | S002 |` fixture while a
  column-zero-only extractor does not
  (`.ufo/waves/round-34/controls/indented-guard.txt`: `spaced=S197 column_zero='' collisions='S197'`).
  Append block built and normalized in scratch
  (`.ufo/waves/round-34/assimilation/append-block.md`): no literal or escaped pipe, recheck
  `90d`, status `mined`, opened `2026-10-24`, `used-by` exactly the admitted entry.
  Validate-before-append on a scratch mirror of the lane exited 0
  (`.ufo/waves/round-34/assimilation/census-scratch.txt`).
  **Quarantine:** the register slice's 13 rows were hand-checked
  (`.../ScoutQuarantineA.md`, `.../ScoutQuarantineB.md`); only the register's `S189` row
  is IN-REGISTRY-SAME-ID, and its `payload-absent` mark is a false negative because the
  register's quoted span is the line-128 `formatEvent` assignment. Every other slice row
  is NOT-IN-REGISTRY by URL; the prose-class rows name no locator at all, so they are
  unverifiable, not fabricated.
  **Id-space:** the register speaks the campaign's pre-remap staging ids, not this lane's
  registry ids — its "S201" is the arXiv paper now packaged as S212/S274/S319, so the
  lane's S201 is unambiguous and **no renumber is warranted**
  (`.ufo/waves/round-34/w1/reports/CritDupIdSpace.md`). The real finding is on the merge
  side: the package repeats the lane's S186–S189 URLs as S199/S200/S260 and its frozen
  remap base ("registry ends at S196") is now stale.
- **considerthese** — mined, never edited. One unimplemented proposal from
  `considerthese/2026-10-24.md` (item 4, propose the next Hyprland config table) was
  grounded through the lane's own bar, not through the proposal text:
  `hyprctl windowrules -j`, `layerrules -j` and `rules -j` all print `unknown request` on
  this host's v0.56.2, so the r25–r27 predict-table method does not transfer to the
  window-rule table, while `hyprctl monitors -j` does answer. It lands as a lesson
  (planning knowledge about oracle availability), not a QUALITY.md criterion and not a
  SOURCES row (`.ufo/waves/round-34/w1/reports/ScribeConsider.md`).
- **Sibling-overlap scan** found no sibling lane holding the Waybar Hyprland IPC /
  event-socket theme, and no sibling file was touched
  (`.ufo/waves/round-34/w1/reports/ConnSibling.md`).

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Freeze of `PRED-C1-r34-v1` / `PRED-C2-r34-v1` with the pre-data control receipts (prior attempt, inherited and re-verified) | Round 34 entry, "Work" | `3420e827bd7b21b1374b23245526554ffd20d096` |
| The admitted entry, the two registry rows, the coverage-map row and the calibration publication (prior attempt, inherited) | Round 34 entry, "Work" | `fa7ba11346116672352b5d41494141c5c4d738d0` |
| Wave-1 spec, validated taskCall, dispatcher, 64 seat plans/logs/reports, the manifest, every seat's scratch tree, the assimilation append block and census receipt, the axis-gate selftest transcript | Round 34 entry, "Work" | `57622b8453f5ca6eb720dfbd1bc6b3285ec2a818` |
| The six round-33 control fixture trees and the twelve round-33 seat scratch trees, committed so every round-33 receipt is re-derivable from committed bytes | Round 34 entry, "Honest notes" | `57622b8453f5ca6eb720dfbd1bc6b3285ec2a818` |
| `corpus/lessons/round-34.md` (Gate + Mistakes), the appended disambiguation in `corpus/lessons/round-33.md`, the round-34 LOG entry, the round-34 SCORECARD claim rows and the 12/12-vs-18/18 correction | Round 34 entry | `dff394109f3cc3d851309ad7c67dd3b35b46adf2` |

Lane tip: `dff394109f3cc3d851309ad7c67dd3b35b46adf2` (`master`, pushed;
`jj-lane.sh state` → `ahead=0 behind=0`, working tree clean, `untracked=0`).

## Before → after measurements

**C1 — coverage** (surface: the Waybar event-socket client route; the command that would
show it unmoved is the same counter over a tree lacking the entry and rows):

- before (pre-data freeze `3420e827bd7b21b1374b23245526554ffd20d096`):
  `PRED-C1-r34-v1 closed_entries=0 closed_rows=0 open_cites=2 verdict=TARGET_MISSED` exit 1
- after (tip `dff394109f3cc3d851309ad7c67dd3b35b46adf2`):
  `PRED-C1-r34-v1 closed_entries=1 closed_rows=2 open_cites=0 verdict=TARGET_MET` exit 0
- counting command:
  `python3 -I .ufo/waves/round-34/c1/count.py --root . --frozen .ufo/waves/round-34/c1/frozen.json`
- controls, all `TARGET_MISSED` exit 1: `controls/symlink-crib`,
  `controls/symlink-entry`, `controls/extra/symlink-parent`,
  `controls/extra/symlink-sources`, `controls/extra/used-by-prefix`,
  `controls/entries-only`, `controls/rows-only`; plus the do-nothing and hardlink
  controls, which are committed as receipts (`controls/c1-donothing.txt`,
  `controls/c1-hardlink.txt` — `nlink=2`) and were rebuilt in scratch and re-run this
  round (`.../ExecDonothing.md`, `.../MutC1Drop.md`).
  `controls/golden` (regular files only) → `TARGET_MET` exit 0.
- registry rows 190 → 192; coverage-map navigation 46/46 → 47/47.

**C2 — calibration** (surface: the published S189 line number against the pinned fetch):

- before (publication absent):
  `PRED-C2-r34-v1 published=absent measured=169 mismatch=1 verdict=TARGET_MISSED` exit 1
- after (tip `dff394109f3cc3d851309ad7c67dd3b35b46adf2`):
  `PRED-C2-r34-v1 published=169 measured=169 mismatch=0 verdict=TARGET_MET` exit 0
- counting command:
  `python3 -I .ufo/waves/round-34/c2/count.py --repo . --scorecard SCORECARD.md --frozen .ufo/waves/round-34/c2/frozen.json`
- controls: a card whose last marker tail is `line=128` → `published=128 mismatch=1` exit 1;
  a card with no marker → `published=absent mismatch=1` exit 1; the reachable card →
  `mismatch=0` exit 0.

Both claims are measured on committed bytes and are re-runnable by a non-author from the
frozen spec alone.

## Sources & frontier

Census before and after this attempt:

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado
mado	W04	S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado	W04	S042 duplicate url wayland.freedesktop.org/extras.html across scopes
mado	W04	S045 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado	W04	S097 duplicate url raw.githubusercontent.com/basecamp/omarchy/v3.8.4/themes/matte-black/colors.toml across scopes
mado	W04	S119 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Lib/imaplib.py across scopes
mado	W04	S120 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado	W04	S121 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado	ok	/home/vgpnk/Projects/shokunin/mado-shokunin/corpus/SOURCES.md
```

Exit code **0** before (22:10, at the start of this attempt) and **0** after (23:40,
round end). The seven `W04` warnings are pre-existing and unchanged. Counting command for
the row count: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` →
**192** before and after this attempt; the round's own change was 190 → 192, landed at
`fa7ba113` by the prior attempt.

- **Rows added by tier:** 2 × tier A (`code`) — S201 (Waybar 0.15.0 Hyprland IPC backend,
  6550 B, sha256 `799bf02f…`) and S202 (Waybar 0.15.0 Hyprland window module, 8324 B,
  sha256 `5df496eb…`). Tier B: 0. Tier C: 0.
- **Rows touched old → new:** none. No `status`, `recheck` or `used-by` value of an
  existing row was changed.
- **Frontier rows advanced:** 0. The Waybar module-text frontier item U7 stays **open** —
  this round documents the event-socket route to it, not the rendered module text. The
  critic called the registration headline "frontier → core" an overshoot and this report
  scores the claim accordingly: a bounded documentary-route increment.
- **Refusals recorded with reason and flip:** 12 of the 13 register slice rows
  (`corpus/lessons/round-34.md` §Gate), including the literature entry restated against
  S210/S211.
- **Assimilation:** 2 entries admitted on one theme, 0–3 ids from the package, 12 rows
  refused.

## Trend verdicts

- **expansion: improved.** One net-new admitted knowledge entry on ground the coverage
  map did not hold, each of its two citations a `mined` tier-A registry row (S201, S202),
  plus one new capability admitted to the SCORECARD capabilities table (the
  crib-rejecting coverage counter, demonstrated running in this round). Frontier item U7
  itself did not advance, which bounds the size of the move but does not undo it.
- **quality: unchanged.** No weaker entry was superseded by a stronger one this round,
  and no **stale** entry was re-verified against a live source — the S189 evidence was
  re-read from committed bytes and the corpus's ambiguous line reference was corrected by
  append, which is calibration work, not a quality move. The r33 closure's `quality:
  improved` was itself overclaimed; this round does not repeat that. No admitted entry
  failed its re-check.
- **discernment: improved.** Every routed defect from the r33 closure was either repaired
  (the literature reject restated against the file's real ids; the scratch trees disposed
  by re-verification with named dispositions; the `ScoutRound30.md` citation rule; the
  axis-gate selftest transcript committed) or, in the S189 case, re-verified against the
  pinned bytes and turned into an appended lesson. No disagreement was left unlearned.

Axis verdicts: coverage **improved** (C1 met on the frozen counter); calibration
**improved** (C2 met on the frozen counter); depth, operability, freshness and adjacency
**unchanged**; no axis harmed.

## SHONEN

All four boxes remain `[~]` with resolvable pointers. No box was self-promoted, and no
non-author verifier judged a box this round, so no box is promotion-checkable.

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `.ufo/waves/round-34/w1/reports/RevKnowledge.md`; historical assertion
  `corpus/knowledge/executor-test-sufficiency.md` (MADO-R3-4); outside-lane verifier
  independence is not established by the inherited record.
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  `corpus/knowledge/config-health-report-r3.md` and LOG.md round 3 (VER-M3); this round
  executed no new end-to-end desktop task, and a seat this lane dispatched is still the
  lane.
- [~] Instructions executable by an agent without oral context —
  `corpus/knowledge/executor-test-sufficiency.md` (MADO-R3-4); dispatched subagents do
  not satisfy the outside-lane promotion rule.
- [~] No cross-domain bleed (PROVINCE.md still accurate) —
  `.ufo/waves/round-34/w1/reports/CritProvince.md` (verdict IN PROVINCE) and
  `.../ConnSibling.md` (no sibling overlap); PROVINCE.md was not edited.

---

Stale-lane: none — respawn-per-round driver; no other mission of this lane is open.
Tool installs: none. Wave shape: one v2 wave, 64 seats, 64 finished, 64 reports,
0 dead seats, 0 missing, 0 refused waves, 0 residual calls, round total 64.
Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no
untracked file written by this round's seats at the fleet root; the untracked files present
belong to other lanes or the driver and were left alone.
