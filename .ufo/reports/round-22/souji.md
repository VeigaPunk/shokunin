# souji — round 22 report (attempt 2, hyaku session)

**Attempt 1 is superseded, not erased.** It was judged `rejected-honest-stop`
by the non-author spot-check (`corpus/lessons/round-22-verifier-spotcheck.md`;
MANIFEST records souji round 22 as rejected). Its report and receipts remain in
fleet git history and its measurements remain historical evidence. This attempt
**does not re-claim, re-pin or reword** attempt 1's strict-adequacy claim. It
declares two claims, frozen before data in
`.ufo/waves/round-22/attempt2/preregistration.txt` at base
`4edb25dfe262515d0da63224bbba71e02e36cba5`.

**Lane tip and measured revision: `c1664fcde8b12c7e6082a98cbbab1f1e7509177d`**
(`jj-lane.sh state` → `ahead=0 behind=0 tracked=0`).

## Work performed

**Declared claims (2).** **C1 — calibration** (lowest non-retired axis, 7): a
declared-evidence audit that re-derives the lane's own `SCORECARD.md`
assertions from committed bytes and drives the mismatch count to 0 over the
enumerated set. **C2 — coverage**: assimilation of one theme
(restorable-quarantine staging) with two re-grounded knowledge entries, the six
registry rows they cite, and a verdict for every row of the lane's
absent-defect register slice.

- **C1 instrument** — `tools/souji-declared-evidence.py`, stdlib only, git
  plumbing only, `/var/tmp` scratch, no writes; digest pinned in
  `census/round-22/attempt2/instrument-digests.txt`. Three frozen classes
  (backticked path pointers incl. `:line`/glob/`<rev>:<path>`; bare 7–40-hex
  tokens in a revision-context cell; 64-hex digests paired with exactly one
  path). Selftest 8/8, including the cheapest do-nothing control
  (`control always-zero -> FALSE-GREEN-REJECTED`).
- **C1 repairs, three real defects** — the fleet `AXES.md` had been written as
  lane-relative; `reason-after.txt` was a bare basename (real path
  `census/round-21/reason-after.txt`); and
  `.ufo/scopes/souji-mint-20261018/obsidian-cli-probe.md` **does not exist**
  (`ls` → No such file or directory), so the cell now records the absence
  instead of asserting a banked artifact. One repair (AXES.md) names an
  absolute host path and therefore *leaves* class A rather than resolving
  inside it — disclosed, not hidden.
- **C1 out-of-enum repairs from the audit seats** (not counted by the frozen
  counter, each receipt-backed): capability row 6 bound to its revision
  (`measured at d7266c5`), row 8's `5/5` bound to `measured at 6f8ee0f`,
  row 10's glob narrowed to the real receipt file, the stale "current installed
  digest" phrase for the two tools replaced by "r13-era digest (superseded)",
  one short id expanded to its full commit, and `literal32/32` corrected to
  `read32/32 (base18/32)`.
- **C2 theme and entries** — one theme from
  `/home/vgpnk/Projects/shokuknow/merge/souji/`. Adopted
  `corpus/knowledge/quarantine-staging-no-copy-r23.md` (no-clobber rename;
  S109–S111) and
  `corpus/knowledge/quarantine-origin-record-fields-r24.md` (restore side of a
  per-item origin record; S112–S114 + existing S022). Both carry a lane-authored
  `## Gate` with `opened: 2026-10-25`, per-ADMIT `reason:` clauses, a real
  REJECT with a flip condition, and quotes that appear verbatim in committed
  snapshots under `census/round-22/attempt2/sources/` (13 snapshots: `.raw` +
  `.txt`, sha256 in `instrument-digests.txt` / seat manifests).
- **C2 re-grounding, executed this round** — six public sources fetched and
  converted (man7 `mv.1`/`rename.2`/`statx.2`, `docs.gtk.org` `File.trash`,
  `man.archlinux.org` `gio.1`, FreeDesktop trash spec), plus the five-device
  `RENAME_NOREPLACE` measurement **vendored byte-exact**
  (`vendor-noreplace-probe.out`, sha256
  `1634d206ef534f683b5d469a9f0333c80a4aaba58215bb63683111c024be8bb5`, labelled
  in both entries and the lesson as *not re-run in this lane*).
- **C2 gate counter** — `tools/souji-gate-check.py` (digest
  `5b8025a8…`): six frozen per-entry checks + slice-verdict completeness,
  selftest 9/9 (byte-exact staged copy, symlink escape, indented `source:`,
  missing `reason:`, 26-word quote, locator-from-filename and always-green
  control all rejected). Before: `entries=2 ok=0 slice_verdicts=0
  slice_total=8 fail=10`, exit 1. After: `entries=2 ok=2 slice_verdicts=8
  slice_total=8 fail=0`, exit 0.
- **C2 register slice, all 8 rows hand-checked, three passes** —
  `census/round-22/attempt2/slice-verdicts.tsv`: 5 `accepted` with a stated
  correction (S114 `git-repack[1]` markup; S123 and S131 man-page spans the
  rows cite against local payloads; S124 intervening `NOREPLACE_new` field;
  S133 rename(2) span against a probe), 2 `present` (S126, S138), 1
  `unverifiable` (S118 — DOI answers 202 with an empty body; unreachable is not
  fabrication), 0 `refused`. The boundary that produced this is written into the
  lesson after two passes disagreed on three rows.
- **Assimilation preconditions** — frozen collision step before any write:
  registry 108 ids, staged 134 ids, `collisions` **0**; the indented-row guard
  was proven on a scratch fixture (0–3-space pattern catches `  | S002 |`,
  column-zero pattern misses it). Append block validated in a `/var/tmp` corpus
  mirror (`sources-census.sh validate --file` exit 0) **before** the first
  registry write. Adopted ids continue at **S109** with citations re-pointed
  **by document**: campaign S124→S109, S116→S110, S115→S111, S137→S112,
  S126→S113, S117→S114; S022 was already present and is cited, never
  duplicated.
- **Lesson** — `corpus/lessons/round-22.md`: M13–M16 (attempt-2 mistakes),
  M17–M21 (seat-driven: locator naming an absent section, counts line not
  self-verifying, class C unexercised on the file, census gate narrowness,
  campaign-vs-lane numeric overlap after adoption), M22–M23 (novelty
  overclaim; verdict boundary drift), and two Gate blocks naming
  admitted/rejected candidates and the spot-check seat.
- **Bookkeeping** — SCORECARD capability row *declared-evidence calibration
  audit* + rewritten calibration row; `corpus/README.md` F4 map row, Frontier
  note and § *Round22 attempt 2*; LOG entry; SKILL.md scratch-class glob
  repaired (`launch-*.json` matched 0 tracked files → `launch-<id>.json`).
- **Received but not integrated** — inherited attempt-1 leftovers: none
  uncommitted. Four `tests/vault/**` files carried content-empty
  mode-only dirt (`100644→100755`, mtimes 2026-10-18); they were reverted with
  `chmod 644` (provably lossless — worktree blobs equal HEAD) and are no longer
  modified. Operator-owned `census/operator-sweep-20261019/` and inherited
  `census/round-21/__pycache__/` stay untracked and untouched.

### Swarm accounting

Round shape: **one v1 wave** under
`scripts/hyaku/ufo-wave-policy.json` (band 32–64, validated by
`ufo-swarm-wave.mjs plan`), **53 seats**, dispatched as exactly one batched
`task` call from `.ufo/waves/round-22/attempt2/w1-spec.json` →
`w1-dispatch.json` → `taskCall`; plus **one residual call of 6 seats** after
landing (≤8, ordinary). L1 holds the canonical planner seat; no `planner`
role was dispatched (the validator rejects it). Round total **59 seats** (≤128).

| call | seats | role mix | reports |
|---|---:|---|---|
| w1 (v1 wave) | 53 | 12 executor, 15 reviewer, 8 scout, 7 scribe, 4 critic, 3 mutation-tester, 2 revenger, 1 sentinel, 1 connector | 53/53 |
| residual | 6 | 4 reviewer, 1 sentinel, 1 critic | 6/6 |

Attack share of w1: 23/53 (43%). **Dead seats: none**; every seat returned a
report. No seat was replaced or resumed. Two seats' assigned candidate paths did
not exist when they ran (`evidence/impl-a`, `impl-b`); they fell back to the
committed `tools/` bytes and said so — recorded, not papered over.

Runner note (evidence): the wave runner's `run` subcommand validated and
rendered the wave but did not itself spawn seats in this session; the rendered
`taskCall` was dispatched as the single `task` call the policy note requires.
That is recorded here because the first `run` invocation produced no agents.

## Landed changes

Only helper-confirmed `landed <hash>` lines are cited; each maps to the LOG
entry *Round22 attempt2*.

- `a211e4d1bf6ea592670d16269f34e9f67f33e8b3` — both tools, both knowledge
  entries, six registry rows (S109–S114), snapshots + vendored payload, derived
  slice + verdict table, before receipt, preregistration, wave spec/registry.
- `70af563c3086d5799a7fdaf988ba3b687f3b128c` — SCORECARD capability + axis
  rows, README attempt-2 section, lesson M13–M16 + Gate, LOG.
- `2a130b47db43eb4b3d80b2e7a5112d6b4b021899` — last declared-evidence repair.
- `3216c1998fe04d7e23793ffd4e135bd37c3a11f4` — measured counts recorded.
- `5ff5041b64964d4e6e8374b0eefb8b12010b9997` — seat-driven corrections
  (locators, slice verdicts, stale digest, lesson M17–M21).
- `d6a75bad8129960bdb96874421298e3bf42aa8c4` — connector/row-draft corrections
  to registry, entry and README.
- `af73b8ba92fa2783d9f4653bd504233939daa2d6` — review-driven hardening of
  gate-check, entry `reason:` clauses, row wording.
- `5fdd5d54fdf5ca9e203e5ed65bcffb8712572447` — declared-evidence instrument
  hardening and the honest calibration row.
- `ee1aef2b87e35923859b3e1b84ae09ca56d1d289` — wave evidence, SKILL glob
  repair, final numbers.
- `4a6ee90a8f8804ba268e44c204e95a931f74a051` — escaped-pipe cell split.
- `c9f1fe3caf642dfe3a9e00de94caf1d4bf86503f` — wave report evidence (52/53).
- `f8f0b4a2c4ab3d16369413b6aa9f2d2c08590581` — digest-pinned calibration row.
- `8990ae4c6284005d42e6edeb9bf0060a2450f566` — instrument digest receipt, row
  cleanup, frontier note.
- `c1664fcde8b12c7e6082a98cbbab1f1e7509177d` — final calibration numbers at
  the measured tip. **Final lane hash cited above.**

## Before → after measurements

| claim | counting command (lane root) | before | after |
|---|---|---|---|
| C1 calibration | `python3 -B tools/souji-declared-evidence.py --root . --file SCORECARD.md --rev <rev> --format counts` | base `4edb25d`: `assertions=55 resolved=52 skipped=33 mismatches=3`, exit 1 | tip `c1664fc`: `assertions=62 resolved=62 skipped=39 mismatches=0`, exit 0 |
| C2 coverage | `python3 -B tools/souji-gate-check.py --root . --round-date 2026-10-25 --entries corpus/knowledge/quarantine-staging-no-copy-r23.md corpus/knowledge/quarantine-origin-record-fields-r24.md --snapshot-dir census/round-22/attempt2/sources --slice census/round-22/attempt2/quarantine-slice --slice-verdicts census/round-22/attempt2/slice-verdicts.tsv` | entries absent: `entries=2 ok=0 slice_verdicts=0 slice_total=8 fail=10`, exit 1 | `entries=2 ok=2 slice_verdicts=8 slice_total=8 fail=0`, exit 0 |

Both ends of C1 use the **same instrument** (digest pinned in
`census/round-22/attempt2/instrument-digests.txt`). Supporting counts:
knowledge files 9 → 11; registry rows 108 → 114 (mined 85 → 91) with
`sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` exit 0;
landing gate at the tip `SUMMARY findings=0 checked_reg=50 checked_changed=11
checked_pins=13 checked_measured=3 checked_markers=18 status_lines=134
checked_reports=239`.

**Kill rules, exercised.** C1: fixtures 2–5 each fail on their own fault and a
zero-printing control is rejected (`FALSE-GREEN-REJECTED`); the base-scored
do-nothing state is M=3, so the target is unreachable without the repair.
C2: a byte-exact staged copy without a Gate fails check 1; a 26-word quote, a
quote absent from the named snapshot, a dangling source id, a missing REJECT, a
missing verdict row and an always-green control all fail.

**Claims are causally separable** — C1 verifies from `SCORECARD.md` and one tool;
C2 from the entries, registry rows, snapshots, verdict table and the other tool.
Neither needs the other's bytes.

### Verdicts (with the attacks on record)

- **C1 — counter `verifies`; axis move `not supported`.** Two critics attacked
  it and both stand: `CritC1Predicate` (enum gaps — command-embedded paths and
  word-glued revision tokens are invisible; class C is structurally empty on
  this file; skips are not itemised; class B proves existence, not measurement)
  and `CritC1Axis` (**`bookkeeping-only`**, settling observable V=0 — no
  verdict-bearing cell changed as a consequence of a repair). Calibration score
  stays **7**; the round claims a **capability acquisition plus record
  accuracy**, not a scored axis move. Attempt-1's adequacy claim remains
  unproven and is untouched.
- **C2 — counter `verifies`; coverage credit `unproven`.** `CritC2Coverage`
  graded Q1/Q2 `fails`: the lane's admitted
  `trash-spec-restorable-quarantine.md` already held the spec's read side
  (`Path`, no-overwrite, `O_EXCL`) and the HELD
  `quarantine-same-filesystem-rename.md` already held the primitive. Both
  entries were rewritten to state an explicit delta (restore command, write
  contract, identity fields, vendored device observation) and the r23 title was
  narrowed to the five measured devices. Coverage score stays **8**; the honest
  class is **import with re-grounding**, and the operator/closure rules.
  `CritC2Counter` additionally showed the counter's green is reachable by a
  fabricated fixture root (no positive-evidence floor); that is stated as a
  limit of the frozen predicate, not hidden.

## Sources & frontier

Census command (frozen by CORPUS.md), run at round start and at round end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji
```

- **Before:** exit **0**, `108` rows (`FLEET rows 108 / tier.A 104 / B 3 / C 1 /
  mined 85 / queued 15 / rejected 8`), duplicate-URL warnings only.
- **After:** exit **0**, `114` rows (`tier.A 110 / B 3 / C 1 / mined 91 /
  queued 15 / rejected 8`).

Rows added: **6, all tier A** — S109 (vendored `RENAME_NOREPLACE` probe,
own-work), S110 `rename(2)`, S111 `mv(1)`, S112 `gio(1)`, S113 GIO
`File.trash`, S114 `statx(2)`. Rows touched old→new: **none** — no existing
row's status/recheck/used-by/teaches cell was rewritten, and S022 was reused as
is. Rows by tier: 6 A / 0 B / 0 C. Frontier rows advanced: **F4** (map row,
Frontier note and README § Round22 attempt 2); no promotion to core.

**Assimilation (§10).** One theme, 2 entries, package `merge/souji/`;
re-grounded in-round (every cited source opened 2026-10-25, this lane's own Gate
blocks, committed snapshots). Admit/reject pair for the spot-check: ADMIT both
entries; REJECT `quarantine-staging-no-copy-r24` (adds EXCHANGE/WHITEOUT and
more mounts but no consequence a staging tool here would use; flip named in the
Gate) and `quarantine-origin-record-fields-r23` (dominated by the r24 entry;
flip: a fact the r23 holds and r24 does not). Id lists and collisions: registry
108, staged 134, **collisions 0** before adoption; renumber map by document as
above. Post-adoption the lane's S109–S114 and the campaign's S109–S114 are
different documents — recorded as M21, disambiguated by the map, never by
arithmetic.

**Considerthese:** no `considerthese/` directory exists in this lane repo
(`ls considerthese` → absent), so no consideration was mined.

## Trend verdicts

- **expansion: improved.** Two entries enter on F4 with re-grounded provenance
  and 6 new tier-A rows (108→114, mined 85→91); a byte-exact copy of the staged
  entry fails the gate, so the entries are not imports of unopened bytes. Not
  claimed: new ground — `CritC2Coverage` showed the read side was largely held.
- **quality: improved, bounded.** Both instruments are fixture-backed and
  reject their own always-green controls; C1 repaired three real self-assessment
  defects; both tools are read-only with no execution surface. Not claimed: the
  counter sees only its three token classes, and its green is reachable by a
  fabricated fixture root (limit stated).
- **discernment: improved, pending outside check.** Three independent passes
  over the slice, a fallback to `unverifiable` for an unreadable DOI instead of
  "fabricated", two staged entries refused with flips, and an overclaimed
  novelty corrected in the corpus. A lane-dispatched seat is still the lane, so
  no independent admission is asserted.

## SHONEN

- [~] SKILL.md / SCORECARD carry real commands and decision tables — new
  capability row + two tool rows whose selftests are committed; no promotion
  verifier.
- [~] End-to-end domain task executed and logged — LOG *Round22 attempt2*; both
  counters run before and after at named revisions.
- [~] Instructions executable by an agent without oral context — every cited
  command runs at `c1664fc`; the vendored probe is labelled not-re-run.
- [~] No cross-domain bleed; PROVINCE accurate — both entries are F4 restorable
  quarantine; credential/exposure decisions stay with Kagi/operator, host
  liveness with Mori.
  No `[x]` is claimed without a named non-author verifier.

**Holds / no-harm scope:** certification OFF, K5 HELD; no deletion or move
authority created; quarantine stays dry-run by default; `/home/vgpnk/Projects/shokuknow`
was read-only (no writes, no commits, no campaign tools); no live `/proc`,
credentials, private TSVs, `.tower` or operator-sweep contents were read. A
mode-only `chmod 644` on four `tests/vault/**` fixtures restores their committed
modes; nothing was deleted.

**Scope cleanliness:** process-scope-clean for this attempt — no seat wrote
outside its report/evidence path (validated by report and by `git show --stat`
on each landing commit), one seat's `git status` probe refreshed `.git/index`
mtime only (no ref, commit or tree change; disclosed in its report), and this
L1 removed only its own generated `tools/__pycache__/`.

**Misroot sweep:** unfiltered `git -C /home/vgpnk/Projects/shokunin status
--porcelain` shows the driver's `.ufo/state/*` and `watchdog.log`, an operator
file cluster (`bm.json`, `live*.html`, `nama.html`, `s395.txt`,
`tf_bavelas.html`, `unblob.log`, `wb2.html`, `write`, `xc.xml`, mtime
2026-10-24 18:07, none mentioning souji or round-22), `scripts/hyaku/hyaku.env`
+ `lane-addendum.md` (operator-owned), and this report. **No souji seat
misrooted a file into the fleet root**; nothing was copied or deleted.

**Stale-lane:** respawn-per-round; no other mission of this lane is open; round
23 was not started.

**Tool installs:** none by this L1 or its seats (one seat reinstalled `ruff`
0.17.2 / `pyflakes` 4.0.3 into a `/var/tmp` venv after a host-wide
`~/.local/share/uv/tools` deletion, outside the lane and not persisted). No
pacman transaction was run anywhere (host-wide pause respected).

**Open L0 questions:** none new. Inherited souji questions (r17 jj-keep-refs /
operator-sweep disposition, r18 reap/NAMESPACE, r20 F5 historical exposure)
remain operator-owned. Reported, not asked: the lane has **no `.gitignore`**
while 152 operator-owned census files sit untracked (one `git add -A` from lane
history); and `scripts/hyaku/ufo-swarm-wave.mjs run` did not spawn seats in this
session, so the rendered `taskCall` had to be dispatched by hand.
