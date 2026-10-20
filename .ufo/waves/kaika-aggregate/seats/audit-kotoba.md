# Seat audit — `kotoba-shokunin` @ `c61a973`

Seat: `KaikaAggregateR12.AuditKotoba` (aggregator round 12, ad-hoc lane audit).
Lane audited: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (canonical original,
not a retired worktree). Read-only throughout; nothing in the lane was touched.
Date of run: 2026-10-19. Gate used: `.ufo/waves/round-9/corpus-gate.mjs`
(`corpus-gate-v1`) from the aggregator worktree.
**Census totals in this note are provisional** — the parent's indented-Markdown
source-row parser fix is still in flight; nothing here is a final fleet census.

## 1. Revision capture (exact)

```
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD
c61a973b2e02e1ded169703ddcb06466f4edd8bd
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin status --porcelain
(no output; exit 0)
```

HEAD commit: `c61a973` 2026-10-19 19:46:49 -0300
"round-46 verifier spot-check (integrator, kaika): non-author admit/reject sample + adjudication".
Ancestry confirmed: `f2f9ee1d88bc42d80fb96075db0fc3b43fb8a321 78ee57e5ed6fa409476dabea6bd8146ba37425dd`
(f2f9ee1's parent is 78ee57e; `git merge-base --is-ancestor f2f9ee1 HEAD` → yes).
Worktree clean at the audited revision (no untracked/deleted corpus files by
`status --porcelain`); the gate's own stamp agrees: `dirty=0 mode=snapshot`.

## 2. Round selector derivation (committed LOG)

The lane's committed `LOG.md` (425,065 bytes) ends at round 46:
`grep -n '^## ' LOG.md | tail -3` →

```
2286:## 2026-10-19 — Round 46 B2 superseding report pin
2300:## 2026-10-19 — Round 46 landing (kaika steered round 46): C1 improved; C2 improved-bounded; C3 improved as registered, class improved-bounded
2312:## 2026-10-19 — Round 46 landing pin and after-battery
```

Newest lane lesson is `corpus/lessons/round-46.md` (plus `round-46-verifier-spotcheck.md`).
**Derived selector: `--round 46`.** The gate's default (`--round 9`) was also run; the
r10 verdict differs between the two selectors and both runs are reported below. The
selector is a gate parameter, not a property of the repo — a reader must not read one
run's r10 result without the selector.

## 3. Gate run — primary (derived selector 46)

```
$ cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
$ node .ufo/waves/round-9/corpus-gate.mjs \
    --snapshot /home/vgpnk/Projects/shokunin/kotoba-shokunin \
    c61a973b2e02e1ded169703ddcb06466f4edd8bd --round 46
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=46
# expect kotoba-shokunin@c61a973 ABSENT (no committed expected verdict for this revision)
# tree kotoba-shokunin revision=c61a973b2e02e1ded169703ddcb06466f4edd8bd dirty=0 mode=snapshot
...
# verdict kotoba-shokunin failed findings=85 rules=r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
EXIT=1
```

Mechanics: `--snapshot` runs `git -C <lane> rev-parse <commit>`, then
`git -C <lane> archive <commit> | tar -x -C <tmp>`, grades the extracted tree, and
removes the temp tree (`# note kotoba-shokunin extracted with: git archive
c61a973b2e02e1ded169703ddcb06466f4edd8bd | tar -x -C <tmp>`). The dump is not graded.

**Verdict at `c61a973` per gate exit: `not conformant`** (exit 1 = failed; failed rule
IDs `r4`, `r8`, `r10`). This is the gate's mechanically implemented subset only — see §8.

## 4. Gate run — secondary (default selector 9)

```
$ node .ufo/waves/round-9/corpus-gate.mjs \
    --snapshot /home/vgpnk/Projects/shokunin/kotoba-shokunin \
    c61a973b2e02e1ded169703ddcb06466f4edd8bd
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=9
...
# verdict kotoba-shokunin failed findings=84 rules=r4,r8 rules-implemented=r2,r4,r7,r8,r10,shonen
EXIT_DEFAULT_ROUND=1
```

Delta = exactly `CR-kotoba-shokunin-r10-1`. With selector 9, r10 passes because
`corpus/lessons/round-9-aggregator-corpus-verdict.md` exists. With selector 46, r10
fails. Both exits are 1, so the verdict class does not move; the failed-rule set does.

## 5. Findings by rule (primary run, 85 total)

### r4 — 82 findings (count claim on a line with no backticked command)

Per-file histogram (mechanically produced from the gate output; `id → file:line` list
below is the complete set):

```
  8 knowledge/harness-independent-round37.md
  5 knowledge/opencode-offer-trace-round8.md
  5 knowledge/cold-run-round11.md
  4 lessons/round-9.md
  4 knowledge/frontmatter-trigger-surface.md
  4 knowledge/checklist-execution-round15.md
  3 lessons/round-8.md | lessons/round-5-aggregator-audit.md
  3 knowledge/sibling-description-rewrites-round8.md | harness-verifier-round10.md
  3 knowledge/harness-router-models-round9.md | fleet-skill-audit-round5.md
  3 knowledge/claim-census-round12.md | agent-def-audit-round6.md
  2 lessons/round-6.md | round-4-aggregator-audit.md | round-12.md
  2 knowledge/trigger-miss-proxy-round6.md | instruction-surface-census-round13.md
  2 knowledge/independent-verification-round12.md | dispatch-prompt-audit-round7.md
  2 knowledge/anatomy-and-compression.md
  1 each: lessons/round-6-aggregator-audit.md, round-46.md, round-19-recensus.md,
          round-10.md, round-1-aggregator-audit.md;
          knowledge/sibling-citation-routing-round21.md, render-mechanism-round7.md,
          opencode-extraction-round14.md, instruction-surface-remeasure-round13.md,
          corpus-integrity-round11.md, claim-scope-audit-round9.md,
          agent-defs-commands-and-round-prompts.md
```

Exact IDs `CR-kotoba-shokunin-r4-1` … `CR-kotoba-shokunin-r4-82` map to:

```
r4-1..3   knowledge/agent-def-audit-round6.md:9,11,82
r4-4      knowledge/agent-defs-commands-and-round-prompts.md:30
r4-5..6   knowledge/anatomy-and-compression.md:26,88
r4-7..10  knowledge/checklist-execution-round15.md:14,120,248,251
r4-11..13 knowledge/claim-census-round12.md:13,158,183
r4-14     knowledge/claim-scope-audit-round9.md:71
r4-15..19 knowledge/cold-run-round11.md:250,307,311,314,384
r4-20     knowledge/corpus-integrity-round11.md:143
r4-21..22 knowledge/dispatch-prompt-audit-round7.md:37,52
r4-23..25 knowledge/fleet-skill-audit-round5.md:26,28,78
r4-26..29 knowledge/frontmatter-trigger-surface.md:67,73,122,137
r4-30..37 knowledge/harness-independent-round37.md:21,122,178,192,193,327,402,605
r4-38..40 knowledge/harness-router-models-round9.md:14,56,137
r4-41..43 knowledge/harness-verifier-round10.md:15,118,139
r4-44..45 knowledge/independent-verification-round12.md:162,215
r4-46..47 knowledge/instruction-surface-census-round13.md:390,399
r4-48     knowledge/instruction-surface-remeasure-round13.md:12
r4-49     knowledge/opencode-extraction-round14.md:117
r4-50..54 knowledge/opencode-offer-trace-round8.md:30,157,207,254,255
r4-55     knowledge/render-mechanism-round7.md:25
r4-56     knowledge/sibling-citation-routing-round21.md:23
r4-57..59 knowledge/sibling-description-rewrites-round8.md:20,104,496
r4-60..61 knowledge/trigger-miss-proxy-round6.md:7,75
r4-62     lessons/round-1-aggregator-audit.md:37
r4-63     lessons/round-10.md:22
r4-64..65 lessons/round-12.md:28,69
r4-66     lessons/round-19-recensus.md:6
r4-67..68 lessons/round-4-aggregator-audit.md:11,57
r4-69     lessons/round-46.md:61
r4-70..72 lessons/round-5-aggregator-audit.md:6,30,81
r4-73     lessons/round-6-aggregator-audit.md:67
r4-74..75 lessons/round-6.md:17,24
r4-76..78 lessons/round-8.md:4,47,69
r4-79..82 lessons/round-9.md:26,72,73,89
```

(Complete finding texts are reproduced exactly by re-running the command in §3; the
gate prints `… count claim with no backticked command: "<60-char excerpt>" (CORPUS.md:28)`.
The `(CORPUS.md:28)` in every r4 line is a stale pointer — see §7.)

**Spot-check of the predicate on 10 cited lines** (lines read verbatim at HEAD):
`agent-def-audit-round6.md:9` = `## Verdict matrix (18 files × AD-1…AD-9)`;
`:11` = `15/18 files clean. 4 fail cells total:`;
`anatomy-and-compression.md:26` = `## Claim — ~600 lines is a split trigger, not a norm`;
`checklist-execution-round15.md:248` = `- **33 of 41 boxes are still read by a human.** …`;
`claim-census-round12.md:13` = prose ending `…counted 86 rows by a raw`;
`cold-run-round11.md:250` = `COLD RUN: 1 / 9 checks — agrees with the author's recorded verdict`;
`sibling-citation-routing-round21.md:23` = table cell row `| kasegi | 5 | 5 | 0 | …`;
`round-8.md:47` = `- **An artifact is not a landed lesson.** Round 8 produced 799 lines of`;
`round-9.md:26` = `  → db has 17 rows (round 7: 5). Stronger: the cache key's description salt is`;
`round-1-aggregator-audit.md:37` = `16 files = the claimed survey size ✓.`;
`round-10.md:22` = `  block renders **17/17 lines from cache**, so no offered skill is currently on`.
All 10 are literal-text true (a count-noun token and no backtick on the line). The
sample spans headings, normative thresholds (`~600 lines`), table cells whose derivation
command lives in the file's `## Method`/companion (e.g. round-21's predicate), and prose
whose command is elsewhere in the entry. **The implemented check is line-local; it is
not the semantic rule** — a line can legitimately be a r4 finding and still have its
command named in the entry. Do not read 82 as "82 unreproducible counts".

### r8 — 2 findings (credential-class, literal text; classification declared CNE)

Exact gate text:

```
CR-kotoba-shokunin-r8-1: credential-class op-ref occurrences=3 lines=3 files=2 owner=aggregator at c61a973 maxseg=0 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[lessons/round-5-aggregator-audit.md,lessons/round-9-aggregator-corpus-verdict.md] first=lessons/round-5-aggregator-audit.md:83 first4="op:/" len=5 (CORPUS.md:43)
CR-kotoba-shokunin-r8-2: credential-class op-ref occurrences=3 lines=3 files=2 owner=lane at c61a973 maxseg=0 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[README.md,knowledge/sibling-description-rewrites-round8.md] first=README.md:42 first4="op:/" len=5 (CORPUS.md:43)
```

Shape reading: for `op-ref`, `maxseg=0` and `len=5` mean every match is the bare
five-character scheme token `op://`; no match had a `vault/item/field` tail (that
would report `maxseg=3`). The six occurrences at HEAD were mapped directly:

```
$ git -C …/kotoba-shokunin grep -c 'op://' HEAD -- corpus/
corpus/README.md:1
corpus/knowledge/sibling-description-rewrites-round8.md:2
corpus/lessons/round-5-aggregator-audit.md:1
corpus/lessons/round-9-aggregator-corpus-verdict.md:2
$ git -C …/kotoba-shokunin grep -c 'op://' 63ceba7 -- corpus/
corpus/knowledge/sibling-description-rewrites-round8.md:2
corpus/lessons/round-5-aggregator-audit.md:1
```

So 3 occurrences at `63ceba7` → 6 at `c61a973`; the three added ones are
`corpus/README.md:42` (an index row *describing* the round-9 r8 finding:
"the `op://`-literal rule with no placeholder exception") and
`corpus/lessons/round-9-aggregator-corpus-verdict.md:9,17` (the verdict text and the
`git grep -n 'op://'` sweep command). I read all six sites: each is a schematic,
inline-code, or quoted-sweep mention; none is a resolvable reference and no secret
value is reproduced. The lane's own `round-9-aggregator-corpus-verdict.md:9` already
records the class as **"FAIL-literal / PASS-intent"** and notes the rule "has no
placeholder exception". The gate's finding is therefore literal-text true and
intent-false, exactly as the lane documented; the gate itself abstains
(`classification=could-not-evaluate`). The occurrence count grows mechanically whenever
the lane *writes about* the rule — that property belongs in any fleet reading of r8
totals.

### r10 — 1 finding (round's aggregator lesson absent)

```
CR-kotoba-shokunin-r10-1: no corpus/lessons/round-46-aggregator-*.md — the round-46 review duty has no emitted lesson (CORPUS.md:21)
```

Verified: `ls corpus/lessons/ | grep -i aggregator` →
`round-1-aggregator-audit.md, round-4-aggregator-audit.md, round-5-aggregator-audit.md,
round-6-aggregator-audit.md, round-8-aggregator-box3-coldrun.md,
round-9-aggregator-corpus-verdict.md` — the newest aggregator lesson is round 9.
Consequently **any selector R ≥ 10 fails r10 on this lane**; the round-46 finding is not
a one-round slip. Whether the round-46 aggregator duty *should* have emitted a lesson in
this lane is a fleet-ledger question outside this seat (the file is absent at HEAD; that
fact is what the gate decides).

### r2, r7, shonen — 0 findings

- r2 (lessons cite round + evidence): clean over all 21 `lessons/*.md`.
- r7 (phantom index rows): clean; gate notes: `r7: 15 backticked path template(s)/glob(s)
  skipped (contain *, <, {, ~, $ or …)` and `r7 under-coverage (not a finding): 4/58
  corpus files carry no index row`.
- shonen: clean on `SHONEN.md` (form check only). `git show HEAD:SHONEN.md | wc -l` → 12;
  4 `[~]` boxes, one indented evidence line each; no `[x]` mark, so the
  `<verifier-id>` rule is not exercised.

## 6. Gate metadata defect — every embedded `CORPUS.md:<n>` pointer is stale

The finding texts cite `CORPUS.md:28` (r4), `:43` (r8), `:21` (r10), and the script's
header cites `:19`/`:40`. At the graded revision, in **both** the main repo tree and the
gate's own worktree (identical files; `diff -q` → IDENTICAL), those lines are not the
rules:

```
$ grep -n 'A count carries its command\|No credential material, ever\|An index row is a claim\|entries cite the round and the evidence\|aggregator reviews every corpus' <worktree>/CORPUS.md
24:- `knowledge/` entries cite a source: …
25:- `lessons/` entries cite the round and the evidence …
27:- The aggregator reviews every corpus each round and files gaps as lessons.
34:- **A count carries its command.** …
42:- **A quote names its location.** …
46:- **An index row is a claim.** …
49:- **No credential material, ever.** …
53:- **Corrections are new entries, never rewrites.** …
```

Line 28 is blank; 21 is blank; 43 is inside the quote rule's round-1 defect list; 40 is
inside the negative-claim rule. Correct mapping: r2→25, r10→27, r4→34, r5→39, r6→42,
r7→46, r8→49, r9→53. I checked the immediately preceding revision
(`git show fa78388^:CORPUS.md`): rules were at 24/26/33/45/48 — still not 19/21/28/40/43,
so the gate's pointers are stale by at least two `CORPUS.md` edits, not by the last one.
Rule identity is unambiguous from the text, so the rule IDs stay usable; **the line
pointers must not be followed**.

## 7. `SOURCES.md` — structural observations

Header: cites fleet `SOURCES-CONTRACT-v1.md` (2026-10-19); that file exists at
`/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` (and worktree
copies). Access evidence named: `.ufo/round-46/evidence/w2/sources/fetch-log.json`
(tracked: `git ls-files --error-unmatch` → exit 0; 8,456 bytes on disk).

Contract § Census commands run verbatim from the lane root (read-only):

```
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
11
$ awk -F'|' '…NF!=13…' corpus/SOURCES.md            → 0
$ awk … tier histogram                                → A=10 C=1
$ awk … status histogram                              → mined=4 queued=6 rejected=1
$ awk … duplicate ids                                 → (no output)
$ awk … enum violations + tier inflation              → (no output)
$ awk … mined used-by paths must exist                → (no output)
$ grep -c 'op://' corpus/SOURCES.md                    → 0
```

Also verified: 11 rows × 11 columns, no empty cell in any row; ids `S001`–`S011` unique
and sequential; `used-by` for the 4 mined rows = `SKILL.md` (exists at lane root);
`opened` = 2026-10-19 on all rows; `recheck` values are in the contract's enum shape
(`on-release`, `90d`, `180d`, `365d`, `on-commit`); kind enum holds
(`spec`/`docs`/`own-work`/`community`); no `community` row is tier A.
The round lesson's `### Sources` table has exactly 11 rows, all `location` cells
non-empty, longest `quote` = 18 words (contract limit 25), and the row-level
`status` changes are logged old→new (`S001, S002, S003, S008 queued→mined,
used-by —→SKILL.md`). **SOURCES.md is structurally clean against the contract's own
checks** — that is a structural statement, not a claim that any row's URL, sha256, or
`teaches` content is true; I fetched nothing and re-ran no verifier.

Sections present and shaped per contract: `## Registry`, `## Paths` (2 sequences),
`## Search log` (3 dated entries, each with question/where/identified/screened/included/
excluded/stop rationale), `## Leads (unopened)` (~20 bullets marked as leads). The
search-log arithmetic is internally consistent (30 identified = 8 included + 1 rejected
+ ~21 excluded; 2 own-work identified = 2 included).

### 7a. Provenance observation — access evidence runs from a worktree path

`fetch-log.json` records, verbatim:
`"cwd": "/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kotoba-shokunin"` and
`"census": {"run_from": "/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kotoba-shokunin", …}`.
This is the parent-flagged class (provenance value naming an ephemeral
`.tower/worktrees` path), but it lives in the **sources evidence file**, not in a
knowledge-entry `recheck:` field. It is not a gate rule and not a semantic verdict; it
is a fidelity risk: the recorded run directory is not the canonical lane root, so a
future re-runner following the log is pointed at a worktree that may be retired. The
census *commands* recorded alongside are lane-relative and re-ran clean from the
canonical root (§7), so the risk is to the recorded location, not to the numbers.

### 7b. Provenance observation — fetch-log contradicts the corrected S010 row

- `corpus/SOURCES.md:23` (S010): `--self-test exit 0 and --json exit 1
  (9 PASS / 1 FAIL governance.citation_resolves at LOG.md:2111) runs 2026-10-19`.
- `fetch-log.json` row S010: `"url": "verifiers/verify_skill_checklist.py --self-test
  and --json (local runs, both exit 0)"`.

`corpus/lessons/round-46.md` M18 records that the first read said "both exit 0", that a
re-run found `--json` exit 1, and that the row was "corrected before commit" — but the
committed evidence log still carries the pre-correction string, and its `notes` (3
entries) carry no correction. The log's `quote`/`quote_location` fields are consistent
with the row; only the `url` string contradicts it. I did not re-run the verifier
(prohibited by this seat's contract), so this is a **textual contradiction between two
committed files**, not an adjudicated exit-code verdict.

### 7c. Provenance observation — S009's scope says "landing commit", anchor pins a pre-landing hash

`corpus/SOURCES.md:22` (S009) scope: "The comparator's own self-model at the round-46
landing commit"; anchor: `Final line "self-test: 0 failure(s) over 328 assertions";
commit 78ee57e`. The lane's own commit `04192c2` names the landing pin as `f2f9ee1`, and
`f2f9ee1`'s parent is `78ee57e` (checked with `git rev-list --parents`). The round-46
lesson's M17 fix cell records the landing self-test moving `328 → 330`. So the row's
scope wording and its pinned commit disagree, and the quoted figure is the pre-landing
figure by the lane's own record. I did not execute the self-test (prohibited), so I
cannot state the figure at HEAD; I only state the textual mismatch and the ancestry.

## 8. Knowledge provenance frontmatter scan (parent-requested, bounded)

Scope: `corpus/knowledge/**/*.md` (34 files), fields `source:`, `verified-at:`,
`recheck:` at line start (leading whitespace allowed).

```
knowledge_md_total=34 with_source=2 with_verified_at=2 with_recheck=2
```

The two files carrying the full trio (and their exact `recheck:` values):

- `corpus/knowledge/harness-independent-round41-census.md:3` — `recheck: From repo root,
  run `PYTHONDONTWRITEBYTECODE=1 python3 .ufo/round-45/drafts/v10/post-r44-hunt.py` for
  the exact-input R45 replay; run the fresh live join, comparator self-test, assertion
  floors, and both corpus gates using the commands in `.ufo/round-45/scouts/V10.md`.`
- `corpus/knowledge/sibling-citation-routing-round16.md:3` — `recheck: run the counting
  command below with the measured lane revision and `frozen`; use `live` only for a new
  source observation, never as a historical replay.`

**Instances of `recheck:` values pointing into `.tower/worktrees` or `/tmp`: 0 of 2.**
Neither value names either path class. (Broader corpus scan for
`.tower/worktrees|/tmp/|worktrees/kaika` shows many **body** hits in older
knowledge/lesson files — historical evidence, left unchanged per the parent's
instruction — and one lesson-header pointer: `lessons/round-46.md:8` names
`/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-ledger/.ufo/waves/kaika-w1/kotoba-state.md`
as the kaika W1 STATE dossier. That is a fleet-ledger pointer in prose, not a
`recheck:` value; reporting it, not editing it.)

Newly added knowledge file check (`git log --diff-filter=A`):
`harness-independent-round41-census.md` added `d374d3b 2026-10-19`;
`sibling-citation-routing-round16.md` added `292bbf8 2026-10-15` (not new).

**Resolvability of the new file's provenance at HEAD (adjacent fidelity finding):**
- all three `source:` paths `.ufo/round-41/drafts/v10/{probe-results,subprocess-replay,
  channel-census}.json` → `git cat-file -e HEAD:<path>` fails: **ABSENT** at HEAD;
- the `recheck:` runner `.ufo/round-45/drafts/v10/post-r44-hunt.py` → **ABSENT**, and
  `git log --all --oneline -- <path> | wc -l` → `0` (never committed).
- The file *body* discloses both: line 45 "The census `source` paths point into the
  pruned `.ufo/round-41/drafts/v10/` tree, so this recheck is bounded by retained
  sidecars and payload copies"; line 115 "Recheck correction: the `recheck:` runner …
  was never committed … so this entry's recheck line is dead".
The frontmatter fields themselves were not updated. Report as provenance/fidelity
observation (pruned-source and dead-runner pointers), not as a gate rule. Note the
tension this creates with the lane's own `QUALITY.md` Q04 ("Every `recheck:`/source
command resolves and runs today") and Q12 (frontmatter trio) — the body disclosure is
honest, the machine-readable field is dead.

## 9. `QUALITY.md` — structural observations

18 criteria `Q01`–`Q18`, append-only shape, every row has a `supersedes` cell (all `—`,
i.e. nothing superseded yet). All `grounded in` targets resolve: the cited class ids
`M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, M13, M14, M15, M16, M17` are exactly
present as `| M<n> …` rows in `corpus/lessons/round-46.md` § Mistakes (which also
carries `M18`, `M19` — present but uncited by any criterion; not a defect against the
stated "no criterion without a lesson" direction). `Tier definitions` delegation to
`SOURCES.md` matches the contract's rule 3 ("no second method").

**Pointer drift in the fleet-CORPUS citations** (exact, checked both revisions):

| QUALITY row | pointer | line at HEAD | what is at HEAD | line before `fa78388` | resolves? |
|---|---|---|---|---|---|
| Q12 | `CORPUS.md:17` | 17 | "Each `knowledge/` entry opens with `source:`, `verified-at:` and `recheck:`;" | 17 | **exact, both** |
| Q13 | `CORPUS.md:33` | 33 | blank line | 33 = count rule head | **drifted +1** |
| Q14 | `CORPUS.md:38` | 38 | count rule's example list ("~40 clones"…) | 38 = sweep rule head | **drifted +1** |

Cause is checkable: `fa78388` ("corpus contract: SOURCES.md (contract v1), kaika
rules…") is dated `2026-10-19 19:53:01 -0300`, i.e. **after** lane HEAD
`c61a973` `2026-10-19 19:46:49 -0300`; `git show --numstat fa78388 -- CORPUS.md` →
`116 0 CORPUS.md`, and the one-line shift is visible between 17 and 24. So the pointers
were true when written and the target moved seven minutes later. Classified as
cross-repo pointer instability (the same record-vs-tree drift class the lane's own
Q03/M3 names), not as a semantic defect in the criteria. Q14's stale pointer is the
worse of the two: `:38` now lands inside the *count* rule's examples, so a reader could
mis-attribute the sweep requirement.

## 10. `corpus/README.md` (index) and `SHONEN.md`

- `corpus/README.md`: 64 table rows (`grep -c '^|'`); sections Coverage map / Frontier /
  Known gaps; round-46 rows exist at `:60` (`QUALITY.md`), `:61` (`SOURCES.md`),
  `:62` (`lessons/round-46.md`).
- Under-coverage instance (gate-declared not-a-finding): `grep -c 'verifier-spotcheck'
  corpus/README.md` → `0`, so the round-46 lesson `lessons/round-46-verifier-spotcheck.md`
  has no index row. The gate's note counts 4 such files of 58; I confirmed this one and
  did not reconstruct the other three.
- Tracking consistency: gate snapshot `stats.files` = 59 total corpus files =
  `git ls-tree -r --name-only HEAD -- corpus/ | wc -l` = 59. No untracked/deleted
  corpus file at the audited revision.
- `SHONEN.md`: 12 lines at HEAD; gate shonen check = 0 findings (form only; all four
  marks `[~]`, evidence lines present; box-3 independence and box truth are outside the
  check).

## 11. Study path extracted from `corpus/SOURCES.md` (directly evidenced)

From `## Paths`, first sequence, verbatim:
**"Authoring a SKILL.md that loads everywhere — S001 → S008 → S003 → S002 → S011."**

Row-level evidence for each hop (all cells from the same committed `SOURCES.md`; ids
resolve, rows opened 2026-10-19, and the round lesson's `### Sources` table carries the
URL/access/quote/location for each):

1. `S001` spec, tier A, `status: mined`, `used-by: SKILL.md` — agentskills.io
   specification; anchor "§ Skill metadata table, § Progressive disclosure"; teaches name
   length/charset, description 1–1024 chars, SKILL.md < 500 lines.
2. `S008` spec, tier A, `mined` — YAML 1.2.2 §7.3.3 Plain Style; teaches the colon-space
   and space-hash ambiguity that breaks a plain-scalar description.
3. `S003` docs, tier A, `mined` — Claude Docs best practices; teaches the vendor-only
   rules the open spec lacks (no XML tags in description, third person, 500-line body).
4. `S002` docs, tier A, `mined` — client implementation guide; teaches lenient client
   validation (warn-and-load) as the contract that explains why invalid files still load.
5. `S011` community, tier C, `status: rejected` — teaches `REJECTED: … flip: …`; the
   path's stated reason is that knowing the rule it gets wrong is evidence of taste.

Second sequence, same section: **"Why the comparator distrusts its input JSON —
S006 → S007 → S009 → S010"** (RFC 8259 §4 → Python json docs → comparator self-test at
commit `78ee57e` → checklist gate), with `S009`/`S010` `queued`. Note §7c above: the
S009 anchor/scope mismatch applies to this path's own evidence.

Evidence boundary: this is a direct transcription of the committed registry/path text
plus the contract census results. I did not fetch any URL, did not verify any `teaches`
claim, and did not run S009/S010. The `## Leads (unopened)` bullets were not used as
evidence.

## 12. Gate limitations — explicit

Declared by `corpus-gate.mjs` (registry block), confirmed by reading the source:

- **Not evaluated by construction:** r1 (source is semantic; the `~/Projects/bounties`
  province tree is gone), r3 (falsifiability), r5 (negative-claim sweep needs negation +
  proximity matching), r6 (quote location needs the quoted surface outside the repo),
  r9 (correction discipline; `--snapshot` has no history, and author identity is a
  commit-time string), box-3 non-author independence, and shonen-semantics (box truth).
- **r8 classification is declared could-not-evaluate** (needs a vault read,
  operator-gated). The literal-text occurrence findings stand; the schematic-vs-real
  judgment is not made.
- **r4 is a line-local predicate** over the canonical surfaces (`README.md`,
  `knowledge/**.md`, `lessons/**.md`); it charges headings, table cells, and
  threshold/word-limit expressions (e.g. `≤25 words` in `lessons/round-46.md:61`), and
  cannot see a command named on another line or in a companion artifact. A pass/fail on
  r4 is not a semantic rule-4 verdict.
- **r7 grades phantom rows only**; under-coverage (file without row) is printed as a
  note, not a finding.
- **r10 is selector-parameterized** (`--round`, default 9) — the same repo fails or
  passes r10 depending on the number passed. Both runs are reported in §3–§4.
- **Exit 3 (expectation drift) is not applicable here**: the gate printed
  `# expect kotoba-shokunin@c61a973 ABSENT (no committed expected verdict for this
  revision)`, so no frozen expectation exists for this revision to reproduce.
- **`--snapshot` grades a `git archive` export**: no `.git`, so history-dependent checks
  (r9; authorship) are unavailable by construction, and `.gitignore`d/untracked files
  are never seen.
- **Stale `CORPUS.md` line pointers** in every finding text (§6) — rule IDs remain
  valid; the line numbers do not.
- This gate is the **round-9 aggregator artifact** (`corpus-gate-v1`); it is not the
  lane's own verifier suite, and a pass here would not establish the lane's other gates.

## 13. Verdict and residual risk

- **Gate verdict at `c61a973` (selector 46): `not conformant`** — exit 1; failed rule IDs
  `r4` (82), `r8` (2), `r10` (1).
- Same revision, selector 9: `not conformant` as well (exit 1; `r4` 82, `r8` 2), with
  r10 passing only because the round-9 aggregator lesson exists.
- **r8 is FAIL-literal / PASS-intent** at this HEAD, and every occurrence is the bare
  `op://` scheme token (`maxseg=0`, `len=5`), with the lane's own round-9 lesson already
  documenting the same classification. **r4's 82 are line-local literal hits**, not 82
  proven unreproducible counts. These two sentences are the honest reading; the gate
  output alone overstates both.
- **`SOURCES.md` is structurally clean** against contract v1's own census commands
  (11 rows, 0 malformed, A=10/C=1, mined=4/queued=6/rejected=1, unique ids, resolving
  `used-by`, no `op://`, complete search log, leads quarantined).
- **`QUALITY.md` is structurally clean** (18 criteria, all `grounded in` ids resolve)
  with two drifted fleet-CORPUS line pointers (Q13/Q14, +1 via `fa78388`).
- Provenance/fidelity observations that are **not** gate rules: access-evidence `cwd` in
  an ephemeral worktree (§7a); fetch-log S010 vs SOURCES S010 exit-code contradiction
  (§7b); S009 anchor/scope mismatch (§7c); new knowledge entry's `source:` paths absent
  and `recheck:` runner never committed (§8).
- **Provisional:** this note's counts describe only `kotoba-shokunin@c61a973`. Any fleet
  total derived from it waits for the parent's parser fix and the exact
  `FINAL LANES READY` signal. No numeric score is assigned here.

## 14. What this seat did not do

- Did not run any verifier, self-test, build, lint, or formatter (prohibited), so no
  exit code printed in the lane's corpus was re-confirmed.
- Did not fetch any URL, vault item, or external page.
- Read 10 of the 82 r4 finding lines verbatim (§5); the other 72 are represented by the
  gate's exact output and the mechanically generated id list, not individually opened.
- Did not reconstruct the other three r7 unindexed files.
- Did not bisect `CORPUS.md` further than `fa78388^` for the gate's stale pointers.
- Did not edit, stage, or otherwise mutate the lane or any fleet file except this note.
