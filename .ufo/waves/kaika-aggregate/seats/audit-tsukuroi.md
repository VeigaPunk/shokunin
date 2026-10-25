# audit-tsukuroi — aggregator round 12 / fleet round 1 lane audit

Seat: `KaikaAggregateR12.AuditTsukuroi`. Date: 2026-10-19. Lane: `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin`
(original path; no retired worktree used). Write scope: this note only. Nothing in the lane repo was
edited, staged, or committed; every lane read used the worktree file or `git show <HEAD>:<path>` /
`git archive <HEAD>` bytes.

**Status of numbers in this note:** the lane counts below are revision-bound measurements of this
audit. They are **provisional**: the parent has stated a census parser fix for indented Markdown
source rows is in progress, and final census waits for `FINAL LANES READY`. Nothing here freezes a
fleet total or a score.

## 1. Revision and tree state (recorded verbatim)

```
$ git -C /home/vgpnk/Projects/shokunin/tsukuroi-shokunin rev-parse HEAD
d8ec15d5e6c1d93370f5a85b929745e26577f4d8
$ git -C /home/vgpnk/Projects/shokunin/tsukuroi-shokunin status --porcelain
          # empty output, 0 lines; exit 0
```

HEAD commit: `d8ec15d5e6c1d93370f5a85b929745e26577f4d8 2026-10-19 20:07:14 -0300
"protocol-shokunin round-1 verifier spot-check (integrator, kaika): non-author admit/reject sample + adjudication"`.
Post-audit re-check (after all gate runs and reads): `git status --porcelain` → 0 lines.
`git archive` extraction is the gate's own read path; it wrote only into `os.tmpdir()` and removed it.

Gate exit is the verdict basis; **the gate is not a whole-corpus semantic certificate**.

## 2. Gate invocation, selector derivation, and observed result

Round selector derivation from the committed LOG (this lane):
- `LOG.md:173-176` — round 11 (training r10) is "the closeout: the arc's final round … nothing in
  this entry presumes a round 12".
- `LOG.md:251` — `2026-10-15 — **fleet round 1, interactive continuation; blocked before dispatch**`.
- `LOG.md:364`, `409`, `411`, `419` — `2026-10-19 — fleet round 1` continuation, measured commit
  `549ec0c…`, post-review correction, measurement pin. HEAD `d8ec15d` is the later verifier
  spot-check commit on that round.

→ the lane's current committed round is **fleet round 1**, so the primary run used `--round 1`.
The gate's default is `--round 9`; it was run explicitly as a second observation. Both runs differ
only in the r10 message text; counts and exit are identical.

```
$ cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate && \
  node .ufo/waves/round-9/corpus-gate.mjs \
    --snapshot /home/vgpnk/Projects/shokunin/tsukuroi-shokunin \
    d8ec15d5e6c1d93370f5a85b929745e26577f4d8 --round 1; echo "GATE_EXIT=$?"
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=1
# expect tsukuroi-shokunin@d8ec15d ABSENT (no committed expected verdict for this revision)
# tree tsukuroi-shokunin revision=d8ec15d5e6c1d93370f5a85b929745e26577f4d8 dirty=0 mode=snapshot
CR-tsukuroi-shokunin-r4-1: knowledge/adjacency-handoffs-fleet-r1.md:34 count claim with no backticked command: "reported through the fleet report. It does **not** mean 8/10" (CORPUS.md:28)
… 96 further r4 lines …   [elided here; the full 97-line r4 list is emitted by the recorded
                              command and is deterministic by (rule,key) sort — re-run it to
                              reproduce CR-tsukuroi-shokunin-r4-1 … -97 verbatim; per-file
                              distribution and samples in §3]
CR-tsukuroi-shokunin-r10-1: no corpus/lessons/round-1-aggregator-*.md — the round-1 review duty has no emitted lesson (CORPUS.md:21)
# note tsukuroi-shokunin r7 under-coverage (not a finding): 19/35 corpus files carry no index row
# note tsukuroi-shokunin extracted with: git archive d8ec15d5e6c1d93370f5a85b929745e26577f4d8 | tar -x -C <tmp>
# verdict tsukuroi-shokunin failed findings=98 rules=r4,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
GATE_EXIT=1
```

Second run (`--round 9`, same `--snapshot` and revision): identical structure; only the r10 line read
`no corpus/lessons/round-9-aggregator-*.md — the round-9 review duty has no emitted lesson`;
`# verdict … findings=98 rules=r4,r10`, `# process-exit 1 (failed)`, `GATE_EXIT=1`.

Structured confirmation (`--round 1 --json`, same exit 1), observed stats:

```
repo tsukuroi-shokunin revision d8ec15d5e6c1d93370f5a85b929745e26577f4d8 dirty 0 mode snapshot exit 1
stats {"files":36,"rules":{"r2":0,"r4":97,"r7":0,"r8":0,"r10":1,"shonen":0}}
findings by rule: {"r4":97,"r10":1}
```

**Verdict: not conformant** at `d8ec15d5e6c1d93370f5a85b929745e26577f4d8` per `corpus-gate-v1`
exit 1 (failed). Failed rule IDs: **r4** (97 findings, `CR-tsukuroi-shokunin-r4-1 … -97`) and
**r10** (1 finding, `CR-tsukuroi-shokunin-r10-1`). Clean-returning implemented rules: r2, r7, r8,
shonen (0 findings each) — which is not evidence for the rules the gate declares not-evaluated (§7).
The frozen-expectation line says `ABSENT` (no committed expected verdict for this lane@revision), so
exit stayed 1 and no exit-3 drift was recorded.

## 3. r4 — what the 97 findings actually are

Unit: 97 finding lines across 27 corpus files (r4 is line-local: a count literal on a line with no
backticked command). Representative exact lines read from `git show HEAD:corpus/...`:

- genuine count claims, command on an adjacent physical line (hard-wrapped prose):
  - `knowledge/package-state-plane.md:170` → `wall ≈17 s**, 1332 raw lines, all 1188 packages covered. Non-tty output`; the command is on `:169` (`timeout 240 pacman -Qkk > /tmp/tsukuroi-qkk-full.txt 2>&1` → **rc=1,).
  - `knowledge/systemd-user-plane.md:106` → `**[obs]** Raw output = **60,941 lines**; JSON entry count = **238**`; the command `journalctl -b -p err -o json --no-pager | wc -l` is on `:107` (and the heading on `:104`).
  - `knowledge/aur-risk-plane.md:55` → `## 1. The register — 16 rows, per package [observed]` (section header; probe set in §1 body).
  - `knowledge/update-safety-note.md:315` → `  (3139 entries) — cache is never pruned, so superseded copies accumulate`.
- matches that are not count assertions at all (gate literal-text artifacts):
  - section cross-references: `knowledge/timer-drift-plane.md:169` `see §5 row 7.`; `:233` `§5 rows 4/5`;
    `knowledge/update-safety-v2.md:125` `r2 §7 row 3)`; `:205` `r2 §6 rows in parentheses`;
    `knowledge/aur-risk-plane-ver-s7.md:131` `register §1 rows`.
  - digit-suffixed identifiers/dates followed by a count noun: `knowledge/adjacency-recheck-2026-10-19.md:2`
    `SHA-256 pins`; `knowledge/memory-arm-mutants-s8.md:98` `owning S7-2 case`; `:122` `No S7-2 case`;
    `knowledge/memory-arm-ver-s8.md:198` `41 non-S7-2 cases`; `knowledge/executor-test-sufficiency.md:219`
    `R3-1 note`; `knowledge/journal-boot-plane.md:347` `[2026-10-14 probe]`.
  - format spec: `lessons/round-1.md:86` `| id | source URL or own-work path | access date | quote location | quote (≤25 words) |`.
- machine-assisted shape count over all 97 lines (heuristic, not per-line adjudication): **79 lines carry
  at least one plain `<number> <count-noun>` literal; 18 lines have only artifact-shaped matches**
  (section-ref / identifier-or-date suffix / `≤N words`). Therefore 97 is a line-local literal count,
  not 97 semantically unbacked claims.

Per-file distribution (r4 lines): aur-risk-plane-ver-s7 9, calibration-synthesis 9, degraded-triage-r4 7,
journal-boot-plane 7, package-state-plane 7, host-health-report-r3 5, memory-arm-mutants-s8 5,
timer-drift-plane 5, memory-arm-ver-s8 4, oom-event-plane 4, systemd-user-plane 4, update-safety-note 4,
aur-risk-plane 3, executor-test-sufficiency 3, foreign-provenance-r6 3, kill-event-deep-r8 3,
update-safety-v2 2, update-safety-v3 2, closeout-r11 2, aur-risk-plane-ver-s6 2, and 1 each for
adjacency-handoffs-fleet-r1, adjacency-recheck-2026-10-19, aur-drift-receipt-r9, boot-plane,
driver-firmware-plane, pacnew-plane, lessons/round-1.

Reading: CORPUS.md:28 (rule "A count carries its command … written as `<number> — <command> <date>`")
is **not met line-locally** on these lines; the corpus instead carries commands in adjacent wrapped
lines, section probe ledgers, or `## Contract keys` blocks. Both readings (rule-literal failure vs
gate line-locality) are recorded; no rewrite of lane text was made.

## 4. r10 — missing aggregator lesson (attribution matters)

- Finding: `CR-tsukuroi-shokunin-r10-1` — no `corpus/lessons/round-<R>-aggregator-*.md`.
  `corpus/lessons/` at HEAD contains exactly `round-1.md` and `round-1-verifier-spotcheck.md`.
- Both selectors fail: `--round 1` (derived) and `--round 9` (default). A glob check over all 21 lane
  repos finds `corpus/lessons/round-1-aggregator-*` only in kagi, kake, kasegi, kengaku, kotoba and
  kumitate (7 files across 6 lanes; kagi carries both `round-1-aggregator-audit.md` and
  `round-1-aggregator-seed.md`). CORPUS.md:23-25 names those `round-1-aggregator-audit.md` entries,
  with `.ufo/reports/round-2/AGGREGATE.md`, as the evidence for its round-1/2 corpus-audit rules —
  i.e. they are historical audit artifacts, not fleet-round-1 lessons. tsukuroi has never carried one,
  and no lane carries a fleet-round-1 file of that shape.
- Attribution: CORPUS.md:21 says "The aggregator reviews every corpus each round and files gaps as
  lessons"; CORPUS.md:47 says "the aggregator writes only `lessons/round-<N>-aggregator-*.md`". So r10
  is the **aggregator's emission duty**, measured absent for this lane. It counts in the gate exit but
  is not a lane-authored content defect. This round's review can close it by filing the lesson.

## 5. SOURCES structural observations (`corpus/SOURCES.md`, 73 lines at HEAD) — structural only, provisional

Measured from `git show d8ec15d5…:corpus/SOURCES.md`:
- Registry table: 11 columns (`id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by`);
  34 rows `S001…S034`; no empty cells in `status/tier/kind/anchor/scope/teaches/opened/recheck`;
  every value in `status` ∈ {mined, queued, rejected}.
- Status: mined 26, queued 5, rejected 3. Tier: A 31, B 1, C 2. Kind: docs 24, code 5, dataset 1,
  tool 2, own-work 2.
- Every `used-by` path of the form `corpus/knowledge/*.md` resolves at HEAD (0 missing, checked with
  `git cat-file -e`). `corpus/` at HEAD holds 36 files: 31 knowledge entries (30 `.md` + 1 `.json`),
  2 lessons, README.md, QUALITY.md, SOURCES.md.
- Sections present: Registry, `## Paths` (3 sequences), Search log, `## Leads (unopened)`. The Leads
  section is explicitly declared not evidence and not registry rows; I did not use any Lead as evidence.
- Provenance observation: row `S030`'s `source` cell is a worktree path,
  `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-ledger/.ufo/waves/kaika-w1/tsukuroi-art.md`.
  It exists at audit time (`ls` rc=0), but it is a `.tower` worktree artifact, not a durable repo file;
  S030 is `rejected` (tier C), so it supports no admitted claim. `S033` is also rejected (own-work /
  `web_search` transcript recorded in this file's Search log).

These are structural facts, not a semantic verdict on whether any source supports its `teaches` claim.

## 6. Directly evidenced study path from `corpus/SOURCES.md`

Present as `## Paths` (line 42). Extracted sequence — **Update gate without `-Sy` (U2)**, `SOURCES.md:45`:

> `S010 → S009 → S012 → S001 → S013 → S006 → S005`

Each id resolves to a registry row at HEAD (0 missing), and each row's `scope` matches the path's step
description:

| step | row (tier / status) | scope (abridged) |
|---|---|---|
| S010 | A / mined | ArchWiki System maintenance — pre-upgrade news, full upgrades, pacnew, rollback doctrine |
| S009 | A / mined | pacman-contrib `checkupdates.sh.in` — temporary DB boundary / `pacman -Qu` |
| S012 | A / queued | Official repositories web interface — JSON package search/detail |
| S001 | A / mined | Arch Linux News archive — dated official notices |
| S013 | A / queued | Arch Linux Archive — date-pinned snapshots as rollback reference |
| S006 | A / queued | pacman NEWS 7.0/7.1 — downloader isolation, signature defaults |
| S005 | A / mined | pacman 7.0 DownloadUser / local-repository transition notice |

Note the path includes 3 `queued` (not yet mined) rows (S012, S013, S006); the path is a reading
plan, not a claim that all steps were opened. The other two sequences are `SOURCES.md:44`
(S023→S018→S019→S020→S028→S027) and `:46` (S026→S014→S025→S017→S015→S016→S021→S022→S002); both
resolve with 0 missing ids (same check). All three are *directly evidenced* by registry rows; the
Leads list is not.

## 7. README / QUALITY / lessons (scoped surfaces)

- `corpus/README.md` (51 lines): index rows all resolve — gate r7 = 0 findings. Gate note:
  **19/35 corpus files carry no index row** (under-coverage is not a finding by CORPUS.md:40).
  Independent check with a stricter unit: 17 of 31 knowledge entries are not named by a backticked
  `knowledge/<name>` span in README (adjacency-handoffs-fleet-r1.json, aur-drift-receipt-r9, aur-risk-plane,
  aur-risk-plane-ver-s6, aur-risk-plane-ver-s7, calibration-synthesis, census-closeout-receipt-r10,
  closeout-r11, degraded-triage-r4, foreign-provenance-r6, kill-event-deep-r8, memory-arm-mutants-s8,
  memory-arm-ver-s8, oom-event-plane, timer-drift-plane, update-safety-v2, update-safety-v3).
  The two units differ (gate resolver vs backtick-span presence); do not add or compare them.
  README carries an appended erratum (2026-10-19) superseding the journal-boot row's "0 unit failures
  in 13 retained boots" claim, with a measured retention of 9 boots and a command anchor.
- `corpus/QUALITY.md` (17 lines): 13 criteria; 6–13 were added this round and cite `lessons/round-1.md`
  `## Mistakes` rows. Criterion 8 requires `source:`, `verified-at:`, `recheck:` with an ISO date or a
  cadence (`<N>d` / `on-release`); see §8 for the measured key state.
- Lessons implicated by gate findings:
  - `lessons/round-1.md` (148 lines): `## Gate` records candidates admitted/rejected and states
    "**no independent non-author admit/reject spot-check obtained in-round**". Its `## Mistakes` table's
    header is the r4-97 line (`:86`, `≤25 words` field spec). The `## Gate` also states the
    "Legacy-addendum exception": 25 base notes receive keys as an appended `## Contract keys` block,
    not as opening lines.
  - `lessons/round-1-verifier-spotcheck.md` (17 lines, integrator-written): records the later non-author
    spot-check (`W3ReviewTsukuroi`, admit + reject, 6 of 7 sampled decisions agree; the seventh became an
    appended `## QUALITY check`), verifiers cited at `daa918749` and fleet reports under
    `.ufo/waves/kaika-w3/`. r2 checks pass for both lesson files (each cites round-1 and an evidence
    pointer). The gate cannot evaluate whether that verifier is independent (§8); this note reads the
    file's own attribution only.
- SHONEN.md: gate shonen check = 0 findings; read directly: canonical header, exactly 4 boxes, all four
  `[~]` with one indented author-side evidence line each, no `[x]`. Gate limitation `box-3` /
  `shonen-semantics` applies (§8).

## 8. Provenance-frontmatter scan (parent addendum)

Bounded scan of `corpus/knowledge/**/*.md` at HEAD (30 `.md` + 1 `.json`), keys as line starts and as
multi-line values:
- Key placement: 5 notes carry `source:`/`verified-at:`/`recheck:` as opening lines
  (adjacency-recheck-2026-10-19, arch-news-gate-2026, initramfs-v42-sysroot-recovery, pacnew-plane,
  snapper-eacces-mechanism). 25 notes carry an appended block headed
  `## Contract keys (appended 2026-10-19, fleet round 1)`.
- Duplication/parse ambiguity: **19 notes contain a `source:` line both in the header preamble and in
  the appended block** (adjacency-handoffs-fleet-r1, aur-drift-receipt-r9, aur-risk-plane,
  aur-risk-plane-ver-s6, aur-risk-plane-ver-s7, boot-plane, calibration-synthesis,
  census-closeout-receipt-r10, closeout-r11, degraded-triage-r4, foreign-provenance-r6,
  host-health-report-r3, journal-boot-plane, kill-event-deep-r8, memory-arm-ver-s8, oom-event-plane,
  timer-drift-plane, update-safety-v2, update-safety-v3). Of these, 14 also duplicate `verified-at:`
  and `recheck:` (2 occurrences of each); the remaining 5 (aur-risk-plane-ver-s6, aur-risk-plane-ver-s7,
  memory-arm-ver-s8, update-safety-v2, update-safety-v3) duplicate `source:` only. Example:
  `aur-risk-plane.md` has `source:` at 3 and 345, `verified-at:` at 13 and 346, `recheck:` at 15 and 347. A parser must define first-vs-last occurrence; today the two values differ
  in wording (header prose vs appended contract form).
- Cadence: 44 `recheck:` key lines exist; 30 begin with a cadence token (`180d` 6, `90d` 7, `30d` 9,
  `7d` 1, `on-release` 7). The other 14 are legacy header lines (`§N` / "Appendix … command set" /
  command list) — each of those 14 notes also carries an appended cadence value, so every one of the
  30 `.md` notes has at least one cadence-or-date `recheck:`.
- **Ephemeral-path findings (exact):**
  - `recheck:` values containing `/tmp`: **2**, both as a continuation line inside the value, both
    self-declared ephemeral scratch:
    - `knowledge/kill-event-deep-r8.md:11` → `recheck: §11 probe ledger; every negative claim carries its sweep.` …
      continuation: ``Scratch `/tmp/w8-s82-tsukuroi/` (ephemeral).``
    - `knowledge/oom-event-plane.md:10` → `recheck: §11 probe ledger; negative claims carry their sweep.` …
      continuation: ``Scratch `/tmp/w6-tsukuroi-s63/` (ephemeral; `oom-table-raw.txt` = the event-A task table as extracted).``
    The actionable recheck instruction in both is the in-repo §11 probe ledger; the `/tmp` path is a
    scratch record a later reader cannot recover.
  - `recheck:` or `verified-at:` values containing `.tower/worktrees`: **0**.
  - `source:` values containing `/tmp`: **12** notes, all in prose as scratch-dir records
    (`aur-drift-receipt-r9` `/tmp/w9-tsukuroi-s93/`; `aur-risk-plane-ver-s6`; `aur-risk-plane-ver-s7`
    `/tmp/w7-tsukuroi-vers7/`; `aur-risk-plane`; `census-closeout-receipt-r10`; `closeout-r11`;
    `foreign-provenance-r6`; `host-health-report-r3`; `memory-arm-ver-s8` `/tmp/w8-ver/`;
    `timer-drift-plane`; `update-safety-v2` `/tmp/w7-s73-tsukuroi/`; `update-safety-v3`
    `/tmp/w8-s83-tsukuroi/`). Each `source` value also names host probes / repo paths / S-ids, so the
    scratch mention is not the only anchor; this is a durability observation, not a support failure.
  - `source:` values containing `.tower/worktrees`: **0** in knowledge frontmatter; the only `.tower`
    reference in the scoped surfaces is `SOURCES.md` row S030 (§5), which is rejected.

## 9. Explicitly named gate limitations (as printed/declared by the gate and observed here)

- **Not evaluated by design:** r1 (is a token a source), r3 (falsifiable-or-opinion), r5 (negative
  claim carries its sweep), r6 (a quote names its location), r9 (append-only / no cross-lane edits),
  box-3 (is an `[x]` verifier non-author), shonen-semantics (is a box claim true). A clean return on
  r2/r7/r8/shonen therefore says nothing about those rules.
- **r8 classification** is `could-not-evaluate` by design (needs a vault read); the gate reports shape
  only. Independent literal grep at HEAD (`op://`, `sk-…`, `ghp_…`, `github_pat_`, `xox[baprs]-`,
  `AKIA…`, `BEGIN … PRIVATE KEY`, `Bearer <token>`, `password|token|secret = …`) returned **0 lines
  each** under `corpus/`; that corroborates "no literal credential forms found", not r8's
  classification.
- **Snapshot mode** grades a `git archive` tree with no history, which is why r9 is unavailable here.
- **No frozen expectation** for `tsukuroi-shokunin@d8ec15d` (`ABSENT`), so no exit-3 drift check was
  performed; exit 1 is the measured failure class.
- **r4 is line-local**: hard-wrapped Markdown puts the command on an adjacent line (verified at
  package-state-plane.md:169-170 and systemd-user-plane.md:104-107), and `§N row` / `S7-2 case` /
  `SHA-256 pins` / `≤25 words` shapes match the count regex without being count claims.
- **r10 is a round-selector check** for `lessons/round-<R>-aggregator-*.md`; its verdict depends on
  `--round`, and the duty it measures is the aggregator's (§4). Selector used: 1 (derived from LOG);
  default 9 also run and reported.
- Single-lane `--snapshot` mode was used (not `--all` discovery), so no fleet-level coverage claim is
  made here.

## 10. Residual risk / gaps

- The 97 r4 findings were counted exactly and sampled (8 lines read verbatim; 18 classified by regex
  shape), but not each adjudicated one-by-one; treat the artifact/plain split as indicative.
- The r10 lesson, if filed this round, changes the lane's gate exit; the verdict here is bound to
  `d8ec15d` and must not be quoted against a later revision.
- SOURCES `teaches` accuracy, tier appropriateness, and whether a path's steps are sufficient were not
  semantically verified (out of the gate's scope and of this seat's remit); only structural/resolution
  facts are recorded.
- Census totals are intentionally not frozen (parent census-parser fix pending; `FINAL LANES READY`
  not yet received). No numeric axis score is proposed.
