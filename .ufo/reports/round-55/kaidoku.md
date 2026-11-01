# kaidoku round 55 — the carry-in repair round: four routed round-54 closure defects close, and the corrections ledger gains its mechanical pin

## Work performed

Fresh-start round, L1-inline on the Windows host (no wave surface; the kaidoku
round-53 L0 question stays open and unanswered — routed around, never treated as
answered). Round base `79421b75…` (the r54 spot-check commit). Commit chain
(rebased, see below): declaration `c191d8df…` → freeze `1f9be6eb…` (first commit
adding `.ufo/waves/round-55/claims.json`) → landing `fa4cd11…` → landing follow-up
`627a9c20…` → record `d79e630d…` → close `6742d3f7…` (removes the stray `C:`
subtree the pushed base carried) → sha-citation correction `5c9fc48b…` →
post-correction gate receipt `e601d8ca…`. Local main == origin/main == `e601d8ca…`
at filing (measured: `git rev-parse HEAD origin/main`).

- **Fresh-start compliance:** r50/r51/r52 (all `rejected-honest-stop`, digests in
  the rendered prompt §7; lessons re-read), the r53 and r54 spot-checks, and the
  r54 plans' fresh-start section were read before declaring. **Ruled out, with
  reasons:** (1) the AVM LE-SquashFS Frontier→Core C1 — REA 6.5.0,
  sasquatch/sasquatch-v4be, unblob and vendor fetches are absent on this host
  (PROVINCE `## Host migration — 2026-10-31`); three rounds died re-attempting it;
  routed findings stay routed. (2) A second declared claim beyond the carry-in
  pair — r51/r52 failed on a second claim that could not land; this round declares
  exactly the two claims the carry-in work grounds. (3) The r53-sized-out
  registry-drift census (`census3` outside-13) — stays planned. (4) Any wave
  dispatch — no surface on this host.
- **R55-C1 (calibration — a lowest-axis claim; all three owned axes tied at 10.0)**
  — the four routed r54-closure defects (spot-check §5 items 1-4) close with
  committed, content-checked artifacts: (a) the tip gate receipt
  `.ufo/waves/round-54/l1/scores/freeze-gate-tip-90f3a9b9.json` (the freeze gate
  executed this round AT rev `90f3a9b9…`: exit 0, disclosures exact 29/29, no
  stray, round-54 row CLEAN); (b) the executed-instruments correction — appended
  `## Corrections (round 55)` block in `corpus/lessons/round-54.md` naming BOTH
  frozen instruments (`r53-record.py`, three record receipts; `sqfs-triage-v6.py`,
  the landing re-score, `c1-v6-at-landing.json`); (c) the v6-table digest repair —
  new probe `tools/round-55/v6-block-digest.py` defines the extraction of record,
  receipt `.ufo/waves/round-55/l1/records/v6-digest-repro.txt` transcribes the
  command, the full digest `946e5359…d204bcc` identical at four revisions, and the
  ~100-boundary sweep that failed to reproduce the r54 16-hex value
  `b340ed2b48facca7` (the value superseded, never deleted from the filed receipt);
  (d) `corpus/QUALITY.md` row 101 (correction-block provenance fields are list
  items; their checkers grep unanchored and say so). Evidence:
  `.ufo/waves/round-55/l1/scores/c1-before.txt` (0/4 at the base, committed at the
  freeze), `.../scores/c1-after.txt` (4/4 content-checked at the landing).
- **R55-C2 (depth — capability acquisition)** — the mechanical pin the r54 closure
  observed missing (§3 observation a): `tools/round-55/corrections-pin.py`, a gate
  over append-only TSV ledgers read at two revisions from git objects (exit map
  0/1/2; finding ids `row_edited`/`row_deleted`/`row_inserted`/`header_changed`).
  Selftest 11 cases 0 failures; green demo: the corrections ledger
  `c753b24f…→627a9c20…` clean (rows 2, appended 0); red demo: the lane's own
  historical r53 in-place verdict edit `fe8fab8d→f78fc766` — exit 1,
  `row_edited` line 29 `round-53`, exactly the event QUALITY row 100 governs.
  SKILL instrument-registry row landed; SCORECARD capability row entered this
  round. Evidence: `.ufo/waves/round-55/l1/scores/c2-before.txt`,
  `.../c2-after.txt`, `.../records/{selftests,pin-green-demo,pin-red-demo}.txt`.
- **Sourced claim:** C2 rests on **S255** (git-show documentation, git-scm.com,
  opened this round; snapshot `.ufo/waves/round-55/l1/s255/`, sha256 `0a95cbcd…`):
  "For plain blobs, it shows the plain contents" grounds the revision-pinned blob
  read both round-55 instruments perform.
- **Corrections to the filed round-54 report (the correcting round carries them):**
  (1) routed defect 2 — the report's "the only executed instrument is the frozen
  `tools/round-53/r53-record.py`" is corrected: BOTH executed instruments were
  frozen (`r53-record.py` AND `sqfs-triage-v6.py`); the durable row is the r54
  lesson's appended correction 1. (2) Routed defect 1 — the report's "freeze gate
  at the tip: exit 0, disclosures 29/29" is now receipted (see (a) above). (3)
  Routed defect 3 — the report's atom-T6 digest `b340ed2b48facca7…` is superseded
  by the pinned command with the disclosure sweep. The filed r54 report is
  fleet-owned and stays as filed.

## Chain re-base and correction disclosures (M55-2..M55-6, all in `corpus/lessons/round-55.md` and LOG)

The first declaration commit `29a7477b…` was created by a helper call that both
passed absolute Windows paths (M55-2: four files landed under a `C:` tree
directory) and carried `--push` (M55-5: the garbage commit reached origin/main
before the defect was caught). History is never rewritten: the five round-55
commits are a faithful replay onto the pushed base — byte-identical content trees,
every internal sha re-cited, after-arms and gate receipts re-measured at the
replayed revs (never substituted), and the close commit `6742d3f7…` removes the
`C:` subtree as a content correction. The replay builder then skipped its
substitution pass for five files (M55-6: 22 orphan-sha citations); commit
`5c9fc48b…` corrects the container/FREEZE citations in place (disclosed; pins
untouched), appends `round-55/correction-1` to the corrections ledger for the
ledger row's cause cell, and appends correction blocks to the lesson and the
SCORECARD record section. A post-push citation sweep shows 0 orphan shas in the
corrected container/FREEZE; the remaining occurrences are the appended blocks'
"was" values. M55-1 (the r54 digest-without-command receipt class) and M55-4 (the
freeze pathspec slip that silently dropped the tip receipt — caught by the
after-arm `git cat-file -e`) are mined with fixes.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| Declaration (plans/round-55-claims.md + ruled-out set) + the two frozen instruments | "declared: the carry-in repair round" | `c191d8dfe00f86a2826708dd8f297105f5db435a` |
| Freeze: claims container (pins `tools/round-55/corrections-pin.py` `f71e6b21…`, `tools/round-55/v6-block-digest.py` `22785c1e…`, and — first claims file to do so — the R29 gate `25b54339…`), before-arms, census-start, selftest/demo/digest receipts, S255 snapshot | "freeze recorded; before-arms measured" | `1f9be6ebba1dbe6f64aba91ff0f779b4433eb921` |
| Landing: r54-lesson corrections block, QUALITY row 101, SKILL registry rows ×2, SOURCES S255, ledger row round-55, round-55 lesson | "landing: the four routed r54 defects close…" | `fa4cd1127f7f943b71a717c8f369c49b8636d4eb` |
| Landing follow-up: the r54 tip-gate receipt (M55-4) | same section, appended bullet | `627a9c20a27ceae90986e290cd8dfff8867f839f` |
| Record: SCORECARD round-55 section (atoms T1-T12, capability row, record corrections), after-arms re-measured, landing gate receipt 30/30 CLEAN | "record landing: after-arms green, gate 30/30 CLEAN" | `d79e630da82f2fc36ec07fcff0984e9f9c6a18d3` |
| Close: census-end exit 0 (19 standing W04), tip gate receipt at the record rev, `C:` subtree removed | "close" | `6742d3f737ce9ab8314aafc6a8ee4659f790cfe4` |
| Sha-citation correction: container/FREEZE fixed in place (disclosed), `round-55/correction-1`, appended correction blocks | "sha-citation correction (post-push, appended)" | `5c9fc48b54fd7e486605b84865bed831f85eb493` |
| Post-correction gate receipt (exit 0, 30/30, CLEAN) | ordering note appended | `e601d8caffd7fbf607fa6b1d7672e521cd680214` |

Gate runs, all receipted: pre-flight at the freeze `1f9be6eb…` (round-55 CLEAN,
disclosures 29/29 + missing [round-55] — the row landing later); landing
`fa4cd11…` (exit 0, 30/30 exact, CLEAN, receipt
`.ufo/waves/round-55/l1/scores/freeze-gate-landing.json`); record tip `d79e630d…`
(exit 0, 30/30, CLEAN, receipt `.../freeze-gate-tip-rebased.json` — the tip run
receipted in its own round); post-correction `5c9fc48b…` (exit 0, 30/30, CLEAN,
receipt `.../freeze-gate-post-correction.json`).

## Before → after measurements

- **R55-C1:** before — at the base `79421b75…`, 0 of 4 repairs present
  (`scores/c1-before.txt`; per-check commands and outputs transcribed).
  After — at the landing `627a9c20…`, 4/4 content-checked
  (`scores/c1-after.txt`). Representative counting command (a):
  `git cat-file -e 627a9c20…:.ufo/waves/round-54/l1/scores/freeze-gate-tip-90f3a9b9.json`
  → exit 0 (base: same command at `79421b75…` → exit 1, absent), and
  `git show 627a9c20…:.ufo/waves/round-54/l1/scores/freeze-gate-tip-90f3a9b9.json | grep -c '"verdict": "CLEAN"'`
  → 1. Representative (c): `python -X utf8 -I -B tools/round-55/v6-block-digest.py
  --root . --rev <REV>` → sha256 `946e535947ba6d17da9f4b1ca7993af285e66103547a5c2107b253e5dd204bcc`
  (23 lines, 8961 bytes) identical at `45c68786`/`c753b24f`/`90f3a9b9`/`627a9c20`.
  Measured at `627a9c20…`.
- **R55-C2:** before — at the base, no pin (`git cat-file -e
  79421b75…:tools/round-55/corrections-pin.py` → exit 1), 0 SKILL registry rows,
  0 capability rows (`scores/c2-before.txt`). After — `--selftest` 11 cases 0
  failures; green demo exit 0 (clean, rows 2, appended 0); red demo
  `fe8fab8d→f78fc766` exit 1 with `row_edited` line 29 `round-53`; registry row 1
  (`scores/c2-after.txt`, transcribed commands and outputs). Capability row
  entered at `d79e630d…`. Measured at `627a9c20…`.
- **No axis harmed:** `git diff 29a7477b..HEAD --numstat -- PROVINCE.md` empty;
  SCORECARD `117/0` insertions-only (the owned-axes coverage/depth/calibration
  rows byte-equal); LOG `44/0` (append-only); SKILL `2/0` (exactly the two
  registry rows; the v6 marker block digest unchanged at the close tip —
  `946e5359…d204bcc`); SOURCES `162` rows (161 → 162, S255 only).

## Sources & frontier

`corpus/SOURCES.md` rows 161 → 162 (S255 only). Counting command:
`git show 6742d3f7…:corpus/SOURCES.md | grep -c '^| S'` → 162 (base `79421b75…`
→ 161). S255 (git-show documentation, tier A docs) was opened this round by curl
(2026-11-01; snapshot bytes + sha256 `.ufo/waves/round-55/l1/s255/`,
`0a95cbcd…`) and grounds C2's revision-pinned blob reads; a first fetch of the
git-cat-file doc was rejected as the anchor (the instruments call `git show`) and
is recorded as the round's Gate reject 1. Census: start exit 0 / end exit 0 / a
final run exit 0, 19 standing W04 warnings at both ends (receipts
`.ufo/waves/round-55/l1/census-{start,end}.txt`); W04 stays named debt. Mistakes
mined: M55-1 (digest-without-command receipt class — the r54 value superseded
with the sweep transcribed), M55-2 (absolute-path helper arguments → `C:` tree),
M55-3 (an instrument named in a frozen atom must be pinned — caught by the gate
pre-flight), M55-4 (the freeze pathspec slip — caught by the after-arm cat-file),
M55-5 (an aborted local commit reached the remote — commit, verify, then push as
a separate act), M55-6 (the rebase builder's skipped substitution pass — run the
catching grep before committing).

## Trend verdicts

- **expansion: unchanged** — no Frontier→Core move; PROVINCE.md untouched (no
  diff across the round); S255 grounds a read discipline, not a surface; SOURCES
  161→162 is the only registry growth.
- **quality: improved** — all four routed r54-closure defects closed with
  committed, content-checked artifacts; a filed-but-unreproducible digest value
  superseded by a pinned command with an honest disclosure sweep; the corrections
  ledger gained the mechanical pin the r54 closure asked for, demonstrated red on
  the lane's own historical in-place edit; the freeze gate ran four times, all
  receipted.
- **discernment: unchanged** (pending the outside spot-check, not self-certified)
  — the round executed the last closure's routed list verbatim and self-routed
  six mistakes (M55-1..M55-6) into the lesson with evidence pointers; every
  verdict rests on re-runnable commands over committed bytes; the two
  process defects that reached the remote were disclosed and corrected by
  appended content, never by a rewrite.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited
  sources — pointer: SKILL craft section (27 rule blocks; command A proxies
  unchanged: map 142/142, `citation_resolved_rules 27` at the landing; the v6
  marker block byte-identical under the new pinned probe); this round added the
  two instrument-registry rows the new gates required.
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  pointer: the round's end-to-end task is the receipted repair of the four routed
  r54-closure defects plus the rebase recovery (LOG entries "declared" →
  "post-correction gate receipt"; the two new instruments executed with committed
  demonstrations; the freeze gate executed at four revisions).
- [~] Instructions executable by an agent without oral context — pointer: every
  after-check is a pasteable command over committed bytes, transcribed with
  outputs in `.ufo/waves/round-55/l1/scores/c1-after.txt` / `c2-after.txt`; a
  non-author can re-run them at `627a9c20…`/`e601d8ca…`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: PROVINCE.md
  has no diff across the round (`git diff 29a7477b..HEAD --numstat -- PROVINCE.md`
  empty); S255 is recorded as grounding a read discipline, not an REA surface.

No SHONEN box is self-issued `[x]`; all four remain `[~]` with resolvable
pointers pending non-author verification.

Assimilation: none — shokuknow unreachable; `considerthese/` does not exist in
this lane (measured at round start).
