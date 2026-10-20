# Audit — kumitate-shokunin (aggregator round 12, seat AuditKumitate)

Status of this artifact: revision-bound observation, **no new numeric score**. The gate
finding counts below are the tool's mechanical output, not a score.

## 1. Revision under audit

- Path: `/home/vgpnk/Projects/shokunin/kumitate-shokunin` (original main checkout, branch `master`).
- `git -C /home/vgpnk/Projects/shokunin/kumitate-shokunin rev-parse HEAD`
  → `16a5441a3347a10ac5ed169abcd5a17ba6f3f185` (short `16a5441`), exit 0.
- `git -C /home/vgpnk/Projects/shokunin/kumitate-shokunin status --porcelain`
  → no output, 0 lines, exit 0 (re-checked after all reads; still clean).
- Read-only: no file in the child repo was written, staged, or committed by this seat.

## 2. Gate verdict at HEAD — `not conformant`

Command (cwd `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate`):

```
node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/Projects/shokunin/kumitate-shokunin 16a5441a3347a10ac5ed169abcd5a17ba6f3f185
```

Observed output, exit **1** (run three times, identical):

```
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=9
# expect kumitate-shokunin@16a5441 ABSENT (no committed expected verdict for this revision)
# tree kumitate-shokunin revision=16a5441a3347a10ac5ed169abcd5a17ba6f3f185 dirty=0 mode=snapshot
...107 CR- lines...
# verdict kumitate-shokunin failed findings=107 rules=r2,r4,r8 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
```

Per-rule finding counts (`grep -c '^CR-kumitate-shokunin-<rule>-'` over the same output):

| rule | findings | failed? |
|---|---|---|
| r2 (lesson round/evidence pointer) | 12 | **yes** |
| r4 (count claim without backticked command) | 94 | **yes** |
| r8 (credential-class literal text) | 1 | **yes** (literal; classification `could-not-evaluate`) |
| r10 (round's aggregator lesson present) | 0 at default selector | no |
| shonen (canonical form) | 0 | no |

Exact failed rule IDs: **r2, r4, r8** (CORPUS.md:19 / :28 / :43 per the gate's own
registry lines 170–173). Verdict: `not conformant` at `16a5441` under the gate's
mechanically implemented checks. This is **not** a claim of whole-corpus semantic
conformance (r1/r3/r5/r6/r9, verifier independence, and SHONEN truth are declared
not-evaluated — see §7).

## 3. Round selector (explicit)

The gate's selector is `--round <N>`, **default 9** (gate header line 45; REGISTRY
`round_flag` line 167); it changes only the r10 presence check (gate line 444–447).

Derivation attempt from committed LOG: the lane's last numbered round in `LOG.md` is
**33** (“round 33 (single-axis wave-artifact erratum; still blocked)”), and the in-flight
steered round is **34** (`.ufo/prompts/kumitate-round-34.md`, which also names round 34 as
the next attempt after round 33's continuation record). Committed `corpus/lessons/` at
16a5441 contains aggregator lessons only for rounds 1, 4, 5, 6, 8, 9 — none for 33 or 34.
The selector is therefore ambiguous for r10 and is stated rather than guessed:

```
node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/Projects/shokunin/kumitate-shokunin 16a5441a3347a10ac5ed169abcd5a17ba6f3f185 --round 33
```

→ exit **1**, `findings=108 rules=r2,r4,r8,r10`, extra exact line:

```
CR-kumitate-shokunin-r10-1: no corpus/lessons/round-33-aggregator-*.md — the round-33 review duty has no emitted lesson (CORPUS.md:21)
```

The r2/r4/r8 findings are selector-invariant; all verdicts below use the default-9 run
unless labeled otherwise (as this one is).

## 4. Rule-level spot verification (specific findings re-read at HEAD)

### r2 — 12 exact findings

`lessons/round-9.md`, `round-19.md`, `round-20.md`, `round-21.md`, `round-22.md`,
`round-23.md`, `round-24.md`, `round-25.md`, `round-26.md`, `round-27.md`,
`round-28.md`, `round-31.md` — each “carries no evidence pointer (commit hash,
.ufo/reports/ path, or LOG.md)”.

- `grep -nE '[0-9a-f]{7,40}|LOG\.md|\.ufo/reports/' corpus/lessons/round-19.md`
  → no output; same for `round-31.md`. The lesson body cites “round-19”/“Round 31” in
  prose but no hash, report path, or LOG.md.
- `round-9.md` carries one hex-shaped token, a `sha256:de50bca59b…` content pin at
  line 28 (64 hex chars); it has no `.ufo/reports/` or `LOG.md` string. The gate's
  evidence regex is `\b[0-9a-f]{7,40}\b|\.ufo/reports/|LOG\.md` (gate line 439), so a
  64-hex digest cannot match it. Finding is a literal true positive with an
  implementation nuance, not a hidden pointer.
- Counter-evidence at corpus level: the index rows in `corpus/README.md` for these
  lessons **do** carry `LOG.md round-N` plus a `commit round-N` label (e.g. README.md:55
  for round-9, :76 round-19, :78 round-31, :89 round-20). The `commit round-N` form is
  not a resolvable ref: `git rev-parse --verify --quiet refs/tags/round-9^{commit}`
  (also round-19, round-31) → empty (NO_TAG); matching commits exist only by message
  (`git log --all --oneline --grep='round-19'` → `154fc45 round-19: …`, `f1b341f`,
  `4fc889c`). So r2 is file-local and the corpus index carries the pointer in a form
  the rule does not read.

### r4 — 94 findings, sampled

Rule as implemented: a `<n> <count-noun>` line with no backticked command
(CORPUS.md:28, gate line 171). Samples re-read:

- `corpus/knowledge/kimi-session-state.md:147` — “Across all 161 files (56 472 records)
  the type census is dominated by context plumbing: …” — no backticked command on the
  line. True positive under the line-local rule.
- `corpus/lessons/round-10.md:99` — “Coverage unchanged at 7 (C1 14/18 families,
  C2 36/36 rows/files after this round's two rows)” — no backticked command on the
  line. True positive under the line-local rule.

The remaining 92 sites were not individually re-read (see §8).

### r8 — 1 finding, exact line

```
CR-kumitate-shokunin-r8-1: credential-class op-ref occurrences=2 lines=2 files=2 owner=aggregator at 16a5441 maxseg=0 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[lessons/round-5-aggregator-audit.md,lessons/round-9-aggregator-corpus-verdict.md] first=lessons/round-5-aggregator-audit.md:79 first4="op:/" len=5
```

Re-read both sites (exact text):

```
corpus/lessons/round-5-aggregator-audit.md:79
Credential sweep 0 hits (`grep -rn 'op://' corpus/` across 16 files; token/
```

```
corpus/lessons/round-9-aggregator-corpus-verdict.md:20 (clause)
… the landed corpus has one literal `op://` occurrence, at `corpus/lessons/round-5-aggregator-audit.md:79`, inside a quoted sweep command …
```

- `grep -o 'op://' <both files> | wc -l` → `2`. Both are schematic (a sweep-command
  quote and prose naming it); no credential value is reproduced. The gate's
  `could-not-evaluate` is its own abstention class; the literal r8 findings still count
  as failed, exactly as the gate prints.

## 5. Structural observations at HEAD (separate from the gate verdict)

- **`corpus/SOURCES.md` is ABSENT at 16a5441**:
  `git cat-file -e HEAD:corpus/SOURCES.md` → `fatal: path 'corpus/SOURCES.md' does not
  exist in 'HEAD'`. Same fatal for `HEAD:README.md` (root), `HEAD:QUALITY.md`, and
  `HEAD:corpus/QUALITY.md`. `git ls-tree -r HEAD` over those four paths prints no rows.
  What exists is `corpus/README.md` (the corpus index, 178 lines).
  → The assignment's SOURCES/QUALITY inputs have **no committed instance at this
  revision**; there is nothing to structurally grade there beyond absence.
- **Index arithmetic** (context for the r7-clean note): `grep -cE '^\| \`(knowledge|lessons)/'
  corpus/README.md` → **74**; `git ls-tree -r --name-only HEAD corpus | awk '/\.md$/{n++}
  END{print n}'` → **75**; the extra file is `corpus/README.md` itself, so r7's 74-row
  universe is consistent. Gate note verbatim:
  `# note kumitate-shokunin r7 under-coverage (not a finding): 0/74 corpus files carry no index row`.
- **SHONEN.md** (365 B): canonical 4-box checklist, all marks `[ ]`
  (SKILL decision tables / end-to-end logged task / executable-without-oral-context /
  no cross-domain bleed). The gate emitted no shonen finding; that is form-only and says
  nothing about the truth of the boxes.
- **Provenance frontmatter scan (parent direction, bounded):** all 38
  `corpus/knowledge/*.md` files at HEAD were asked for `^source:`, `^verified-at:`,
  `^recheck:` (first match per file). Result: **0/38 contain any of the three keys**
  (each printed `source=NONE | verified-at=NONE | recheck=NONE`). Consequence: the
  specific fidelity criterion — a `recheck:` value pointing into an ephemeral
  `.tower/worktrees` or `/tmp` path — has **no instance at HEAD because the field does
  not exist at HEAD**. `/tmp/...` strings do occur in knowledge *bodies*
  (`executable-scorecard.md:374`, `layer-axes.md:349`, `member-claims-gate.md:75,94`,
  `remaining-scripts-census.md:33,35,68,70,71,181,201,203,205,211,213,221,222,302,303`,
  `native-trial-launch.md:219`), but they are command/probe paths in prose, not
  provenance fields; `grep -rnE '\.tower/worktrees' corpus/` at HEAD → no hits.

## 6. In-flight round-34 state — PROVISIONAL, not the audited revision

Parent direction: a census parser fix is in progress for indented Markdown source rows;
do not freeze or publish final census totals. Originals-only rule honored: the in-flight
branch was read from the original repo via `git show`, not from the retired worktree.

- `git -C /home/vgpnk/Projects/shokunin/kumitate-shokunin rev-parse kaika/round`
  → `0acb7752d19058b953ebbeba253b1e35f6548de5`. Log: `0acb775 round-34: fix SOURCES
  Markdown row parsing`, `6336d71`, `06757b0`, `1a8eed5 round-34: sources-registry gate +
  SOURCES/QUALITY …`, base `16a5441`.
- `corpus/SOURCES.md` exists on `kaika/round`, blob
  `6e92b79bdfe022648574c271c4a9a9768238912b` (last touched by `1a8eed5`). Sections:
  `## Registry` (:10), `## Paths` (:35), `## Search log` (:56), `## Leads (unopened)` (:95).
- **PROVISIONAL census** (contract-v1 commands, run as
  `git show kaika/round:corpus/SOURCES.md | …`; these totals must not be treated as
  final): rows **20**, malformed **0**, tier `A=19 B=1`, status
  `mined=9 queued=9 rejected=2`, duplicate ids **none**, enum/tier-inflation violations
  **none**, `^[[:space:]]+\|` indented registry rows **0**. The set includes ≥1 rejected
  row (S019, S020) and recheck values are cadence tokens only
  (`on-release`, `90d`, `30d`, `180d`, `365d`); `grep -nE '\.tower/worktrees|/tmp'`
  over SOURCES.md → no output.
- **Parser-fix scope (verified in originals):**
  `git show kaika/round:scripts/sources-check.mjs | grep -nE 'indent|S\[0-9\]'` →
  `135: /** Strip Markdown's 1–3 ASCII-space indentation without consuming 4-space code
  blocks. */`, row regex at :233, selftest cases `indented-valid-rows`,
  `indented-invalid-rows`, `indented-outside-registry` (:681,:694,:715). This lane's own
  SOURCES.md has no indented registry rows, so the provisional totals above should be
  insensitive to that fix — still provisional pending the parent's `FINAL LANES READY`.
- **Study path extracted (directly evidenced, in-flight only — the file is absent at the
  audited HEAD).** From `## Paths`:
  **“OMP delegation contract — S001 → S002 → S003 → S004.”** The file's stated order:
  “the task boundary (batch shape, caps, isolation) first, because it bounds every spawn;
  then the hub lifecycle that decides what a parked or killed child can still do; then
  discovery precedence, which explains which definition actually ran; end at the
  installed version, because `main` docs and the host binary can skew.”
  Evidence that this is a reading sequence, not a lead: S001–S004 all exist as registry
  rows (4/4), and `used-by` = `corpus/knowledge/omp-task-contract.md`
  (blob `9ad41eaf46385b4cfe0c963387459f54cb4fc911`), which exists at `kaika/round`.
  Two further `## Paths` sequences pass the same membership check: “Kimi MCP plane —
  S005 → S006 → S007 → S008” (used-by `corpus/knowledge/kimi-mcp-plane.md`, blob
  `83eb9ed106f7b7ad4db0661b6ae025f920182803`) and “Multi-agent design judgment — S015 →
  S016 → S018 → S010 → S011 → S012 → S013 → S014” (8/8 ids present).
- **New-entry provenance frontmatter at `kaika/round`:** 2/40 knowledge files carry the
  fields (`kimi-mcp-plane.md`, `omp-task-contract.md`). Their `recheck:` values are
  inline commands with dates, e.g. `curl -fsSL https://moonshotai.github.io/kimi-code/
  en/customization/mcp.md | grep -c 'User level'` → 1, `stat -c '%F %s %a %y'
  ~/.kimi-code/mcp.json`, `node scripts/kimi-census.mjs`. Scan for the parent's criterion,
  `grep -nE '^(source|verified-at|recheck):.*(\.tower/worktrees|/tmp)'` over those files
  → no output. **No ephemeral-path `recheck:` value found; no provenance/fidelity finding
  on this criterion** (reported as a checked absence, with the command).
- At the audited HEAD the same four paths are absent
  (`git ls-tree -r HEAD corpus/SOURCES.md corpus/QUALITY.md
  corpus/knowledge/omp-task-contract.md corpus/lessons/round-34.md` → no rows).

## 7. Gate limitations (named, from the tool's own registry)

- Implemented only: r2, r4, r7, r8 (literal text), r10 (presence), shonen (canonical
  form). Declared **not evaluated**: r1, r3, r5, r6, r9, box-3 verifier independence,
  and shonen semantics (gate lines 177–185). A gate pass here is not conformance.
- r8's real-vs-schematic classification is `could-not-evaluate` by design (needs a
  vault read, operator-gated); its literal findings stand as failed.
- `--snapshot` grades `git archive <rev> | tar -x -C <tmp>`: no history, no author
  identity, so append-only/ownership checks are unavailable. `dirty=0` is the snapshot
  mode's own stamp, not a worktree cleanliness claim.
- `# expect kumitate-shokunin@16a5441 ABSENT` — there is **no committed expected verdict**
  for this revision, so this run is not a frozen-match/independence check.
- r2's evidence regex cannot see a ≥41-hex digest (sha256 pin) and does not read
  `corpus/README.md` index rows; r4 is line-local and does not judge semantic truth.
- Gate notes at this run: `8 backticked path template(s)/glob(s) skipped (contain *,
  <, {, ~, $ or …)`; `0/74 corpus files carry no index row`; extraction line
  `git archive 16a5441a3347a10ac5ed169abcd5a17ba6f3f185 | tar -x -C <tmp>`.
- Round selector changes only the r10 presence check (§3).

## 8. What this audit did not check

- r1/r3/r5/r6/r9; verifier independence; SHONEN truth; corpus semantic truth.
- 3 of 12 r2 files were re-read (round-9, round-19, round-31) — all 12 IDs are listed;
  the other 9 were not individually opened.
- 2 of 94 r4 sites re-read; the rest were not individually inspected.
- r8 beyond the two named lines.
- No builds, tests, lint, formatting, or new score. No writes outside this note.

## 9. Commands run (cwd, exit)

| # | command (abridged) | cwd | exit | key output |
|---|---|---|---|---|
| 1 | `git rev-parse HEAD; git status --porcelain` | lane root | 0 | `16a5441…`; empty |
| 2 | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot <lane> 16a5441…` | fleet-aggregate | 1 | 107 findings; r2,r4,r8 |
| 3 | same `--round 33` | fleet-aggregate | 1 | 108 findings; +r10 |
| 4 | `grep -c '^CR-…-r<N>-'` over run #2 | fleet-aggregate | 0 | 12 / 94 / 1 / 0 / 0 |
| 5 | `git cat-file -e HEAD:{corpus/SOURCES.md,README.md,QUALITY.md,corpus/QUALITY.md}` | lane root | non-zero | all absent (fatal each) |
| 6 | per-file `source:/verified-at:/recheck:` scan (38 files) | lane root | 0 | 0/38 have any key |
| 7 | `git rev-parse kaika/round`; `git show kaika/round:<paths>` | lane root | 0 | `0acb775…`; SOURCES blob `6e92b79…` |
| 8 | contract-v1 census commands over `git show kaika/round:corpus/SOURCES.md` | lane root | 0 | **provisional** rows=20 malformed=0 A=19/B=1 mined=9/queued=9/rejected=2 |
| 9 | `git show kaika/round:scripts/sources-check.mjs \| grep -nE 'indent\|S\[0-9\]'` | lane root | 0 | 1–3-space indent stripper + 3 indented-row selftests |
| 10 | `grep -nE '^(source\|verified-at\|recheck):.*(\.tower/worktrees\|/tmp)'` on the 2 new entries | lane root (via `git show`) | 1 (no match) | none — no ephemeral provenance pointer |
