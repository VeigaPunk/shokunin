# kotodama — round 49 report (kaika wave 2)

Lane: `kotodama-shokunin` (linguistic-cultural worldbuilding). Lane worktree
`.tower/worktrees/kaika/kotodama-shokunin`, branch `kaika/round`, base `c42d675`.
Lane commits: **`c6a174d`** (landed work), **`8c78e6b`** (entry shelf note; the
**measured commit**), **`3596e2b`** (receipt + ledgers). Runner verdict: **admitted**
(`reports/round-49/validation.json`, exit 0). All verdicts are self-verdicts until the
orchestrator's non-author verification.

## Work performed

Declared claims (1–3): **C — coverage** (one right-sized hunting/foraging subsistence
entry; declared in `reports/round-49/claims.json`), **Ca — calibration** (README
`revision: 2.0` stub plus a class control; same declaration), **S — depth, capability
acquisition `sources registry`** (`corpus/SOURCES.md` per SOURCES-CONTRACT-v1; filled the
campaign slot, declared before any merge in `reports/round-49/claims-addendum-kaika.json`).
Coverage was the lowest in-play non-retired axis (freshness is paused pending L0).

- Round identity checked fail-closed: no `.ufo/reports/round-49/kotodama.md` in the fleet
  root, no round-49 close in `LOG.md`; declared baseline `78f77a6` vs worktree base
  `c42d675` differ only in round-49 framing files
  (`git diff --name-only 78f77a6 c42d675 -- corpus tools SKILL.md` → empty;
  `claims-addendum-kaika.json:9`).
- L2 swarm: one batched `task` call of 11 seats — R49Planner (planner), R49Connector
  (connector), R49Scout (scout), R49Entry / R49SourcesA / R49SourcesB / R49Revisions /
  R49Runner (executors), R49Scribe (scribe), R49Reviewer (reviewer), R49Critic (critic);
  each prompt led with `/skill:godspeed` + the verbatim `directive.md` bytes; no model
  passed. Provider exhaustion: R49Entry and R49Runner died on `resource_exhausted`
  (executor route free-model limit); replacement seats R49EntryB / R49RunnerB were spawned
  in one batched call; R49EntryB first hit `turn_rate_limit_exceeded`, so the integrator
  opened and wrote rows S031–S043 itself (R49EntryB later revived and edited the entry).
- C: `corpus/knowledge/culture-material/hunting-foraging-subsistence.md` (205 lines; head
  `:1-23`, chain `:70`, mobility + EA001 dependence calibration `:94-108`, gendered labour
  `:119`, calibration bank `:176`); README rev 2.6 `corpus/README.md:3`, row `:283`.
- Ca: stub deleted (R49Revisions; `reports/round-49/integration/Ca-evidence.md`);
  `tools/check-readme-revisions.py` (388 lines; dup/stub/order legs, orphan/gap warnings,
  selftest 11/11).
- S: `corpus/SOURCES.md` (Registry `:26`, Paths `:74`, Search log `:108`, Leads `:116`);
  Gate `corpus/lessons/round-49.md:18`; pointers `corpus/QUALITY.md:25`, `SKILL.md:557`.
- Learning record: `corpus/lessons/round-49.md:108` `## Mistakes`, `:206` `## Frontier`;
  lessons index revision 4 `corpus/lessons/README.md:451` keeps
  `reports/round-25/audit/c31-lessons-index-audit.py` at `findings: 0`.
- Acceptance runner `reports/round-49/run-validation.py` (C/Ca/S gates; C gated on
  "no existing entry modified"; Gate parsed from the heading line, each id as a bullet;
  separability legs recorded). Run only in a fresh clone of `8c78e6b`.
- Reviewer: entry PASS (after the Binford §13 row), README/Ca PASS, SOURCES PASS.
  Critic: C, Ca, S each "survives with conditions" — conditions met before landing (see
  Mistakes and Integrator notes).

## Landed changes

| change | commit | LOG.md entry |
|---|---|---|
| entry `hunting-foraging-subsistence.md`; README rev 2.6 row/counts/footer + stub deletion | `c6a174d`, `8c78e6b` | `LOG.md:3947` (C, Ca bullets) |
| `tools/check-readme-revisions.py` | `c6a174d` | `LOG.md:3947` (Ca) |
| `corpus/SOURCES.md`, `corpus/lessons/round-49.md`, lessons README rev 4, QUALITY/SKILL pointers | `c6a174d` | `LOG.md:3947` (S, Learning) |
| `reports/round-49/{claims-addendum-kaika.json,run-validation.py,integration/}` | `c6a174d` | `LOG.md:3947` (Trigger, Evidence) |
| `reports/round-49/validation.json`, `SCORECARD.md:54` capability row + `:955` round table, `LOG.md`, `SHONEN.md` | `3596e2b` | `LOG.md:3947` |

## Before → after measurements

All "after" numbers were measured in a fresh clone checked out at **`8c78e6b`**; "before"
at `c42d675`.

| claim | counting command | before | after |
|---|---|---|---|
| C | `find corpus/knowledge -name '*.md' \| wc -l` | 224 | 225 |
| C | `ls corpus/knowledge/culture-material/*.md \| wc -l` | 26 | 27 |
| C | `python3 -B reports/round-28/readme/sweep.py` | rows 224 files 224 | rows 225 files 225, topic_mismatch 0, totals_ok, footer_ok |
| C | `find corpus/knowledge -iname '*hunt*' -o -iname '*forag*' -o -iname '*subsist*' \| wc -l` | 0 | 1 (the new entry) |
| Ca | `grep -c '^revision: 2\.0' corpus/README.md` | 2 | 1 |
| Ca | `python3 -B tools/check-readme-revisions.py` (on base bytes / live) | exit 1 (REVISION-DUP 55,57; STUB 55) | exit 0, findings 0; `--selftest` 11 PASS |
| S | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | file absent (0) | 43 |
| S | contract census (malformed / dup / enum+inflation / missing used-by) | n/a | 0 / none / none / none |
| S | tier and status histograms | n/a | A=34 B=3 C=6; mined=20 queued=19 rejected=4 |
| all | `python3 reports/round-49/run-validation.py` | n/a | admitted, C/Ca/S improved; separability legs both pass |

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:20`, `:468`, `:522`; `corpus/SOURCES.md` (43 rows)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:3947`; `reports/round-49/validation.json`
- [~] Instructions executable by an agent without oral context — round-49 counting commands re-run in a fresh clone of `8c78e6b` (`SCORECARD.md:955`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — entry §15 lore handoff (`hunting-foraging-subsistence.md:203`); connector: 0 sibling owners

No box is `[x]`: no non-author verifier is on record (§6.6).

## Sources & frontier

- Rows before → after: 0 → **43**
  (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; file absent at `c42d675`).
- Rows added by tier: A 34, B 3, C 6. By status: mined 20, queued 19, rejected 4
  (S028 Folklore Database, S029 ARAS, S030 Vulgarlang, S043 ScienceDaily press release —
  each with reason and flip).
- Rows touched old → new: none existed before. Pre-landing normalizations, logged in
  `corpus/lessons/round-49.md:77`: rejected-row `recheck` `—` → `365d`; `used-by` trimmed
  on S001/S002/S007/S013 and S004 `mined` → `queued` (bibliographic-record citations are
  not citations of the scoped catalogue or dataset); S003 quote trimmed to 21 words;
  anchors dated on S007/S008/S010/S017/S022/S025/S026/S029; S013 tier A → B.
- S001–S030 keep the wave-1 ART dossier's draft ids; every one was re-opened this round.
  S031–S043 are new hunting/foraging rows (12 mined by the entry, 1 rejected).
- Paths: 15 study sequences; Search log: 3 bounded notes; Leads: 38 unopened items.
- Frontier: no README `## Known gaps (frontier)` bullet advanced. Ground moved from
  uncovered to covered: the hunting/foraging production register. New frontier items:
  `corpus/lessons/round-49.md:206` (6 bullets), plus the routed rev-1.9 headless body.

## Mistakes

- Classes mined: 22 rows in `corpus/lessons/round-49.md:108` (class · evidence pointer ·
  captured-by · fix), each pointer re-verified. Five STATE-dossier pointers were corrected
  on re-verification (e.g. r17/r22 at `LOG.md:3223/:3298`, not `1081/1156`; the
  r35 placeholder came from commit `57c8409`).
- Still uncaptured: r11 freshness threshold (L0), r35 placeholder tokens, r42 pre-commit
  overwrite gate, r44 carried-candidate, r47 size criterion, r9 write boundary, the
  r33–r48 lessons convention.
- New this round, caught before landing: (1) a declared premise was false ("0 true topic
  owners" — two partial owners exist) → narrowed in the entry and README rev 2.6;
  (2) the framing instruction `targets.json:137` was inverted (it said to delete the real
  record) → not followed; (3) claims were attributed from title-only bibliographic records
  → re-scoped `(to-verify)`; (4) a site-name substring was treated as a citation → class
  lesson at `corpus/lessons/round-49.md:92`; (5) the runner matched an inline "## Gate"
  mention and would have rejected a valid S → anchored to the heading.
- Criteria added: **none** to `QUALITY.md` this round (only the tier pointer at
  `:25-27`). The uncaptured classes are routed to Frontier, not claimed.

## Trend verdicts

- **Expansion: improved.** +1 admitted knowledge entry on uncovered ground, citing 12
  mined rows (S031–S042); a 43-row registry with 15 study paths now records where the lane
  learns (`corpus/SOURCES.md`).
- **Quality: improved locally, flat corpus-wide.** The new entry carries the full
  `source:`/`verified-at:`/`recheck:` head and passed the reviewer after the citation fixes listed under Mistakes.
  The corpus-wide header gap from the STATE dossier (152/133/148 of 224 missing) is
  untouched.
- **Discernment: improved.** The critic falsified a declared premise and an inverted
  framing instruction; 4 rejections are kept with flips; 3 identity-only rows are scoped
  honestly; the S-capability "depth" label is defensible only through "cited sources"
  (critic) — reported here rather than over-claimed.

## L0 questions

- `kotodama | round-49 | Lessons convention: rounds 33–48 left their scribe records in reports/round-N/scribe/ and no corpus/lessons file, while corpus/lessons/README.md:3 says "one file per round that ran". Index those records as parent-owned rows, or amend the README claim?`
- `kotodama | round-49 | The freshness pause (l0-questions.md:47, r11) is still unruled. SOURCES.md now has per-row recheck cadences, which give a countable freshness surface. Rule the threshold or retire it so freshness can be claimed again?`

## Integrator notes

- **No push:** the operator's standing "No push" rule takes precedence over MISSION.md's
  commit-then-push. Lane commits are local on `kaika/round`; this report is not committed
  (the integrator commits it as `kotodama-shokunin <kotodama@shokunin.local>`).
- Filed bytes not edited, but defective: `reports/round-49/targets.json:137` (inverted
  delete instruction), `reports/round-49/claims.json:19,30` ("0 true topic owners").
  Corrections live in this report, README rev 2.6 and `LOG.md:3947`.
- Provider exhaustion this round: executor route `resource_exhausted` (2 seats) and
  `turn_rate_limit_exceeded` (1 replacement seat). The claims were not shrunk; the
  integrator absorbed the S031–S043 rows.
- Harness `cd` hazard: verified that this lane wrote nothing in the fleet root (no
  `.scratch/r49*` or `tools/check-readme-revisions.py` there).
- `reports/round-49/integration/` seat fragments lag the landed registry; re-running
  `merge.py` would undo the logged corrections (see that directory's README).
- README residual: the round-28 revision-1.9 body has no `revision:` label (header lost
  at `ce103bf`). `check-readme-revisions.py` only warns on it (`REVISION-ORPHAN`).
- `LOG.md:3947` says "21 classes"; the lesson table holds 22 rows (`awk` count over `## Mistakes`) — the LOG figure undercounts by one, left as filed.
- Reviewer's open low-severity note: the entry's §2 boundary table omits three neighbours
  it cites elsewhere.
- Fleet-root `SCORECARD.md`/`LOG.md` clobber: W2RoundProtocol relayed that the clobbered
  blobs equal kotoba `b7470d7`, not `c8e233d`. This is outside kotodama's scope.

## Post-review fixes

Lane commit: **`8cee75561cab92c8da7edc501d6221b9f9b5cde8`** (same round; no new claims). This append-only section supersedes the affected wording and counts above.

- **Tier inflation:** appended S044–S046 as tier-B superseding rows for S034/S038/S039; publisher abstracts/descriptions remain useful secondary descriptions, not primary authority for substantive book claims. The prior `tier` cells were not edited. Their source URLs were reopened, with ≤25-word quoted passages and locators in `corpus/lessons/round-49.md` `## Gate`. `corpus/QUALITY.md` criterion 6 records the reviewer disagreement and the resulting source-authority rule.
- **S029 rejection basis:** reopened https://aras.org/ and appended S047, beginning `supersedes S029 —`, with the `Archive Search` membership statement and `Supporting ARAS` universal-connections framing, each with its exact section and quote in the lesson Gate. S029 remains unchanged.
- **Mistakes count:** the original `## Mistakes` table contains 23 data rows. This corrects the report's 22 and `LOG.md`'s 21; recount: `awk '/^## Mistakes/{m=1;next} /^## Frontier/{m=0} m && /^\| / && !/^\| class/ {n++} END{print n+0}' corpus/lessons/round-49.md` → 23. Both corrections are appended in the lesson and LOG.
- **Trend verdicts:** expansion `improved`; quality **`unchanged`** (LEARNING.md vocabulary; no qualifying corpus-wide quality observable moved); discernment `improved` because the non-author tier disagreement became a lesson and a grounded QUALITY criterion. This supersedes “improved locally, flat corpus-wide.”
- **Separability:** C and S are coupled. The `c_without_s.passed` receipt only tested inline URLs; it did not test the required `S###` rows, so it is an incomplete counterfactual and does not establish C without S.
- **Post-commit gates:** `python3 -B tools/harness/claims-freshness.py --claims .scratch/r49-claims-candidates.json --checks reports/round-49/calib/r49-checks.json --json` → `fresh`, exit 0 (C and Ca; 4/4 clauses hold); `python3 -B tools/check-readme-heading.py` → one leading H1, findings 0, exit 0; `bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kotodama-shokunin` → lane `ok`, exit 0.

- **Final lane commit:** `d91c632fe71515acc8e133a804ed2fcfbbe31264` appends an erratum for the doubled-backslash typo in the first LOG/lesson recount snippets; the corrected snippet is in `corpus/lessons/round-49.md#dated-correction-recount-command-escaping` and the count remains 23. It follows commit `8cee75561cab92c8da7edc501d6221b9f9b5cde8`; no prior record was rewritten.
- The freshness, heading, and SOURCES census checks above were re-run after this final commit and remained fresh / clean / `ok` (all exit 0).
