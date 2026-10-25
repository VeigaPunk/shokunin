# STATE dossier — lane `souji` (kaika W1, 2026-10-19)

Scribe: W1StateSouji. Read-only wave; this file is the only artifact written.
Lane repo: `/home/vgpnk/Projects/shokunin/souji-shokunin` (untouched). All
commands are pasteable from the lane repo root unless prefixed `git -C` or
`$SHOKUNIN_ROOT`. Tool note: this is a STATE probe (lane-internal); no web
research was needed or used.

## 1. Identity

- **Domain:** fleet repository & workspace hygiene (掃除) — receipt-gated
  removal of stale, duplicate, and already-preserved artifacts; dry-run by
  default; quarantine before delete; receipts `pushed` /
  `moved-to-obsidian` / `stale` (+ `SAFE(metadata-prune)`, fail-closed
  refusals). (PROVINCE.md, SKILL.md)
- **Rank:** unrostered. MANIFEST `roster[]` lists 13 lanes; souji is absent —
  `<0> — grep -c '"id": "souji"' $SHOKUNIN_ROOT/MANIFEST.json` (roster body) → 0;
  souji appears only in `minted: ["souji"]`. Probation gate CLEARED r3
  (r1–r3 verified; LOG r3: "the roster row remains the operator's
  decision"). SHONEN.md promotion checklist: 0/4 boxes marked
  (`grep -c '^\- \[x\]\|^\- \[~\]' SHONEN.md` → 0).
- **Git:** branch `master`, HEAD `dcc8b9e8382b74825363c75d641798c81dceb387`
  == `origin/master`; tree clean (`git status --porcelain | wc -l` → 0);
  0 unpushed commits (`git log --branches --not --remotes --oneline | wc -l`
  → 0). origin = `https://github.com/VeigaPunk/shokunin-repo-hygiene.git`
  — exists now; r7 recorded it as 404/not created, so it was created between
  r7 and r11 ("lane repo pushed to origin", LOG r11).
- **Last round: 11** — closed 2026-10-18T23:59:00-03:00, fleet MANIFEST
  status `failed` (REJECTED as a round): census `--compare` contract fix
  landed and verified (cand-census-02, selftest 36/36), but certification
  NOT granted (certifier evidence-integrity defects: shared relay
  overwrites; verdicts on non-installed bytes). Report:
  `$SHOKUNIN_ROOT/.ufo/reports/round-11/souji.md` (exists).
- **Fleet ledger cross-check:** the assignment hint "no lane round found in
  fleet MANIFEST by lane key" is **disproven**. All 11 souji rounds are
  recorded — `<11> — jq '[.rounds[] | select(.lanes.souji)] | length'
  $SHOKUNIN_ROOT/MANIFEST.json` → 11 — with statuses exactly matching the
  lane LOG: ok = r1,2,3,4,5,8; failed = r6,7,9,10,11. Fleet max round:
  `<104> — jq '(.rounds | map(.round) | max)' $SHOKUNIN_ROOT/MANIFEST.json`.
- **Admitted/failed ledger:** 5 admitted (1, 2, 3, 5, 8), 1 admitted-amended
  (4), 5 rejected (6, 7, 9, 10, 11) — all filed honestly; dissent preserved
  each time. Operator **cancelled the 12-round goal after r11** (LOG r11).
- **Next round number: 12** — but the declared carry (LOG r11,
  lessons/round-11.md) is: "Re-run the certifier suites under a no-relay
  protocol … then flip certification and rate the axes" — the next
  session's first task, not a scheduled goal round.
- **Minted 2026-10-18** (MINT.md; MANIFEST `minted` array) — hint
  confirmed. 18 LOG entries (`grep -c '^## ' LOG.md` → 18).

## 2. Axes

Lane owns **calibration, operability, coverage** (SCORECARD header; subset
of fleet AXES.md six). None retired.

| axis | score | verdict (evidence) | last change |
|---|---|---|---|
| coverage | 8 | improved (C1, r3): 21/21 metadata prunes with receipts; lore worktrees 20→1, gd2d 6→4; `git -C lore-shokunin worktree list \| wc -l` → 1 | r3 |
| calibration | 7 | improved (V1, r5): audit of r1–r4 found 3 material defects, all corrected in-round with re-run evidence; 0 unresolved | r5 |
| operability | 8 | improved (O1', r4): souji-vault-verify.sh live; `bash tools/souji-vault-verify.sh --selftest; echo $?` → 0; parent battery 4/4 + real-vault probe | r4 |

- **Lowest non-retired axis: calibration (7).** Saturation line 8,
  stagnation window 3 (SCORECARD). Stagnation nudge NOT triggered
  (calibration 7 < 8) → the lowest-axis obligation stands for the next
  round.
- **Score-provenance caveat (r9):** lessons/round-9.md — "current axis
  scores are LEGACY-UNMAPPED; new scores UNRATED" — the 8/7/8 are the
  legacy mapping; the rubric re-rate is blocked behind certification.
- **Capabilities: 4 rows** (fleet census r1; souji-verify r2; worktree
  metadata prune r3; ledger-verify r4) — `<4> — awk '/## Capabilities/,/## Planned/' SCORECARD.md | grep -cE '^\| (fleet|souji|worktree|ledger)'`.
- **Planned section: stale** — last planned round listed is r5 (plus the r4
  operator amendment); rounds 6–11 ran without Planned updates (defect, §5).
- **Certification state:** tools PATCHED-NOT-CERTIFIED; deletion
  authorization OFF (SCORECARD r9 section; r11). SCORECARD's note "advisory
  until the r10 hardening closes the classes" is stale by one round — r10
  AND r11 ran; classes closed in tools; certification still withheld on
  evidence-integrity grounds.

## 3. Corpus

- **knowledge/: 1 file** — `<1> — ls corpus/knowledge | wc -l`. It is
  `obsidian-ledger.tsv`, **header-only**: `<0> — tail -n +2
  corpus/knowledge/obsidian-ledger.tsv | grep -c .` → 0 rows. So: 0
  conventional knowledge entries; 0 overdue `recheck:` (before 2026-10-19)
  vacuously; 0 entries missing `source:`/`verified-at:`/`recheck:` vacuously.
  By design the ledger is operator-fed ("Rows enter only when the operator
  records an export; nothing automated writes here" — corpus/README.md);
  the live ledger has stayed header-only since mint (LOG r4: "live ledger
  still header-only").
- **lessons/: 11 files** (round-1 … round-11) — `<11> — ls corpus/lessons | wc -l`.
- **QUALITY.md criteria: none — `corpus/QUALITY.md` does not exist** (defect,
  §5). No lane repo fleet-wide has one (`glob *-shokunin/corpus/QUALITY.md`
  → no files), so souji is not an outlier, but the admission bar is
  unwritten here.
- **Coverage map (corpus/README.md):** 1 knowledge row + 1 parenthetical
  ("census tables land here from r1 onward"), 1 lessons row, 3
  `## Known gaps` rows. **No `## Frontier` section** (shape drift vs the
  lane contract). Two of the three gap rows are **stale**: "No census data
  yet (r1)" — census data exists since r1 (census/round-1/census.tsv, 246
  rows); "No gate tool yet (r2)" — three verdict tools + census exist since
  r2/r4/r6/r8. The third (numeric rubric standing gap) is still true.
- **PROVINCE.md:** Owns 5 / Work surfaces 3 / Refuses 6 / Adjacency 3 —
  current, matches SKILL.md surfaces and AGENTS.md rules; no Frontier
  section either.
- **Round-2 evidence location:** `census/round-2/` does not exist; r2's
  evidence lives in `tests/results/` (INSTALL.json, parent-harness-live.json
  — both verified present). Coverage-map shape inconsistency, no evidence
  lost.

## 4. Mistakes (rejected / harmed / honest-stop / errata / gate disagreements)

No axis was ever harmed (every round's verdict block says so; the failures
are claim-level, not axis-trade-level). Inventory by class:

1. **False-SAFE defect classes** — the lane's defining failure mode.
   r5: 3 material defects in the lane's own r1–r4 work (symlink false-SAFE;
   local-master pushed fallback; r1 logs_tier.txt) — lessons/round-5.md,
   LOG r5. r9: 23 deduplicated classes (Turkish-locale `id_*` bypass, NUL
   authorization forgery, ledger revocation-after-capture, nested-repo
   deletion via ancestor receipts, hidden live references, index-write
   contract violation, git-2.55 linked-worktree HEAD skew, …) —
   lessons/round-9.md. r10: 1 residual class (census `--compare` accepts
   empty priors) — LOG r10. r11: closed in the tools (selftest 36/36; all
   three cert-16 shapes refuse) — lessons/round-11.md.
   *Captured?* Partially: SKILL.md "Error patterns (false-SAFE signatures)"
   holds 4 patterns (unpushed-lane trap, superseded-snapshot drift,
   checkpoint-blob bloat, worktree-with-unique-commits) — the r1–r5 era
   only; the r9 classes are NOT in SKILL.md. *Proposed criterion* (wave-2
   QUALITY.md): "every reproducible red-team defect class lands as a named
   SKILL.md error pattern or a tests/ fixture in the round that closes it."
2. **Evidence-integrity compromise in certification (r11)** — shared relay
   file (cert-16.json) overwritten repeatedly; CERTIFIED verdicts attached
   to bytes other than those measured; a candidate-selection rule picked a
   candidate that fails the class. lessons/round-11.md, LOG r11.
   *Captured?* No — nothing in SKILL.md/AGENTS.md governs certifier
   evidence hygiene. *Proposed criterion:* "certification verdicts attach
   only to hash-verified installed bytes; each certifier writes its own
   fragment; no shared writable relay files."
3. **Append-only violation (r1 LOG mid-file insertion**, discovered r5) —
   LOG r5 process findings. *Captured?* Rule exists (AGENTS.md "append-only
   LOG.md entry"; LOG header) but no check. *Proposed:* "LOG entry order
   matches date order in `git log --follow -p LOG.md`."
4. **SCORECARD numeric drift** — prose said 6/7 where rows said 8/7;
   corrected r9 after judges caught it (SCORECARD saturation prose; LOG
   r9). *Captured?* No. *Proposed:* "SCORECARD prose and table agree — one
   grep over both."
5. **Seat write-scope overstep (r2)** — a seat installed a synthesized
   tools/souji-verify.sh; deleted. LOG r2, lessons/round-2.md.
   *Captured?* Yes — AGENTS.md worker write-scope clause.
6. **GUI-launch incident (r4)** — a harness spawned Obsidian, rewriting
   `.obsidian` metadata; disclosed, verdicts unaffected. LOG r5 process
   findings. *Captured?* Yes — AGENTS.md seat-harness headless clause
   explicitly cites the r4 incident.
7. **`git add -A` scope-adds (operator sweep 2026-10-19)** — pre-removal
   `git add -A` over live lanes swept 10 live `.scratch/*.out` + the
   in-flight r11 report + a `.gitignore.tmp` into hygiene commits; two
   corrective commits (9c220bf, 99819ec) untracked them again. LOG operator
   sweep. *Captured?* No. *Proposed criterion:* "hygiene commits stage
   named paths only; never `git add -A` over live lanes."
8. **Quarantine tool staging-loop hang (2026-10-19)** —
   souji-quarantine.sh staged 3 files then hung to its 20-min driver
   timeout; the manual protocol (engine stage-gate → git mv →
   hash-vs-origin second check) completed the sweep and is logged as
   equivalent-or-stronger. LOG operator sweep. *Captured?* No. *Proposed:*
   bounded per-target staging (timeout + fail-closed abort with
   diagnostics).
9. **Honest stops (kept — evidence of taste, not defects):** r6 K1 — a
   live-written tree is not classifiable to 0; honest claim form is a
   timestamped snapshot RANGE; a handoff draft carrying unsupported claims
   was stripped (lessons/round-6.md). r7 O1 — no authorized target existed
   in scope; nothing forced (LOG r7). r4 — 4/8 judge dissent
   (NO-CLEAN-CANDIDATE over fixture rot) adjudicated by parent
   re-derivation, dissent preserved (LOG r4). r9 — dissent-24 preserved
   (rubric zeroing semantics, dirty-file SAFE interpretation,
   exploration-vs-coverage; lessons/round-9.md).
10. **Caught-and-corrected (calibration wins):** r7 parent column misread
    (lore worktrees=3 was unpushed=3) caught by blind seat S02 (LOG r7);
    r1's blind-seat disagreement traced to defect D1, not missed evidence
    (LOG r1); fixture rot + host /tmp disk-quota failures escalated r8
    (LOG r8).

## 5. Contract defects

1. **`corpus/QUALITY.md` missing** — required lane file (fleet ground:
   admission bar); absent fleet-wide, souji included.
2. **All 11 lessons lack the contracted `## Gate` section** — `<0> — grep -rc '^## Gate' corpus/lessons/ | grep -cv ':0$'`. Gate-record content
   exists as prose ("gate record", Declared/Outcome blocks) but not the
   contracted candidates/admitted/rejected/spot-check shape.
3. **corpus/README.md has no `## Frontier` section** (uses `## Known
   gaps`), and 2 of its 3 gap rows are stale (see §3).
4. **SCORECARD `## Planned` stale** — last planned round listed is r5;
   rounds 6–11 ran without updates.
5. **SCORECARD certification note stale** — says "until the r10 hardening";
   r10+r11 happened; current state is "re-cert under no-relay protocol
   pending" (LOG r11).
6. **Strays at lane root** (reported, never touched): `err4.nl2`, `err4.z2`
   (67 B each; content is a census stderr fragment — "souji-census: compare
   file header mismatch (want 7 census columns)"; mtime 2026-10-18 23:18;
   the operator sweep classified souji `err4.*` live/too-young — they age
   past the 24 h stale threshold ≈2026-10-19 23:18); `.ufo-reports-placeholder`
   (0 B, mtime 2026-10-18 23:58); `.scratch/s29-freeze-dir.txt` (38 B);
   `results/.s54-write-probe.txt` (6 B).
7. **Bloat:** `<120> — ls tools | wc -l` files / 4.3 M in `tools/` —
   tournament candidate accumulation (61 `cand-*`, 47 `*impl*`, 39
   `souji-*`; patterns overlap). Repo total 80 M (`du -sh .`): census 56 M,
   tests 9.3 M, results 29 files/528 K. These are now receipt-eligible
   (unpushed = 0) but most are cited round evidence; the stale receipt
   requires zero live references and the tool's own sweeps exclude
   `census/**` and `tests/**` — a lane self-census question for the
   operator, not an auto-clean.
8. **`census/round-2` absent** (r2 evidence in `tests/results/`); README's
   "census tables land here from r1 onward" overstates continuity.
9. **SCORECARD pointer shorthand** — `census/round-5/final-57..64.json` is
   not a literal path; the eight files final-57.json … final-64.json all
   exist. Not dead, but fails as a pasteable path.
10. **No root `.gitignore`** in the lane repo (only `results/.gitignore`,
    covering tmp dirs).
11. **Identity:** souji in MANIFEST `minted` but not in `roster` —
    probation cleared r3; roster row is the operator's decision (recorded;
    operator-owned, listed for completeness).
- **Uncommitted changes: none** (`git status --porcelain | wc -l` → 0).
- **Dead pointers: none** among the checked set (5 pointers verified OK:
  obsidian-cli-probe.md, kotodama-scratch-handoff.md, gate-runbook.md,
  operator-approval-list.tsv, operator-sweep approval-list.tsv; the
  final-57..64 shorthand is item 9).

## 6. Proposed round (next = r12; goal cancelled — frame as the declared carry)

Lowest non-retired axis is **calibration (7)** → ≥1 claim must work it.
Stagnation nudge not applicable. All three claims below are causally
separable.

1. **Calibration — re-certification under a no-relay protocol** (r11's
   declared carry). Before: 0 certified tools; deletion authorization OFF.
   After: the 15 corpora/reproducer suites pass with per-certifier
   fragments, verdicts hash-tied to installed bytes; certification flips
   ON. Counting: cert suites → unsafe outcomes 0; `bash
   tools/souji-verify.sh --selftest; bash tools/souji-vault-verify.sh
   --selftest; bash tools/souji-quarantine.sh --selftest` → 0/0/0
   (40/51/91 checks) + census selftest 36/36. *Serves:* SOURCES.md rows on
   git receipt idioms and sha256 verification; knowledge entries: "pushed
   receipt = ancestor-of-default AND zero unpushed-touching commits"
   (git-scm docs, tier A) and "fail-closed certification: verdicts only on
   hash-verified bytes" (own-work, tier A).
2. **Coverage — kotodama `.scratch` re-sweep at age > 24 h** (≈2026-10-20;
   the r6 K1 honest stop's scheduled closure). Before: 256/256 children
   receipt-denied (newest-mtime < 24 h; the big three additionally
   `secrets-refusal` → route to kagi, never read). After: full
   classification of the 42 G tree with receipts. Counting: `bash
   tools/souji-census.sh --root $SHOKUNIN_ROOT` + the command set in
   `census/round-6/kotodama-scratch-handoff.md`. *Serves:* knowledge entry
   on mtime-based staleness semantics (GNU findutils `-newermt`, tier A) +
   the secrets-refusal boundary (kagi adjacency, reported not absorbed).
3. **Operability — fix the quarantine staging-loop hang.** Before: live
   staging hung to the 20-min driver timeout (operator sweep 2026-10-19).
   After: bounded completion or fail-closed abort with diagnostics.
   Counting: `timeout 300 bash tools/souji-quarantine.sh --dry-run --list
   census/round-3/operator-approval-list.tsv; echo $?` → completes ≤300 s
   with the r8 baseline 96/96 PASS dry-run. *Serves:* knowledge entry on
   bounded process supervision (GNU coreutils `timeout`, tier A).

SOURCES.md seeding for this lane (wave 2): git-scm.com log/worktree docs
(A), GNU findutils manual (A), GNU coreutils timeout/sha256sum (A), the
banked `.ufo/scopes/souji-mint-20261018/obsidian-cli-probe.md` as own-work
(A) — the Obsidian-CLI integration remains banked for the operator (r4
finding: no usable CLI entry point on this host).
