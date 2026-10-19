# kaika W3 — non-author verification: kotodama round 49

Reviewer: W3ReviewKotodama (fresh orchestrator-dispatched non-author). Verdict is a recommendation.
Round head `3596e2bb3` (`kaika/round`), base `c42d675be`, measured commit `8c78e6b`.
Scratch `/tmp/kaika-verify/kotodama/` (base archive, head archive, head clone), deleted at end.
Lane worktree: clean (`git status --porcelain | wc -l` → 0); no lane write performed.

## 0. Recommendation

**ADMIT C, Ca, S** — each measured claim re-verifies from head bytes. Three conditions on the record (none blocks admission):

1. Trend label: report says quality "improved locally, flat corpus-wide" (not a LEARNING.md vocabulary value). Recommend `unchanged`.
2. Mistakes row count: report says 22 (LOG says 21); measured 23 (command in §11, D2). Correct the figure.
3. Tier A granted to three publisher descriptions (S034, S038, S039). Recommend B, or a recorded disagreement lesson (§5).

Trend verdicts recommended: expansion `improved`; quality `unchanged`; discernment `improved` only if the S034/S038/S039 tier disagreement is recorded as a lesson, otherwise `unchanged`.

## 1. Provenance (check 1) — PASS

Command: `git -C .../kotodama-shokunin log --format='%h %an <%ae> | %cn <%ce> | %s' c42d675be..3596e2bb3`

```
3596e2b kotodama-shokunin <kotodama@shokunin.local> | kotodama-shokunin <kotodama@shokunin.local> | round-49: ledgers …
8c78e6b kotodama-shokunin <kotodama@shokunin.local> | kotodama-shokunin <kotodama@shokunin.local> | round-49: entry shelf note …
c6a174d kotodama-shokunin <kotodama@shokunin.local> | kotodama-shokunin <kotodama@shokunin.local> | round-49: C hunting-foraging entry …
```
All three author and committer as the lane identity. `c42d675be` is an ancestor of `3596e2bb3` (`git merge-base --is-ancestor` → OK).

## 2. Append-only (check 2) — PASS with one self-disclosed in-place count edit

Command: `git diff c42d675be..3596e2bb3 -- LOG.md corpus/lessons corpus/QUALITY.md` → 396 lines; 1 removed line total (`^-[^-]`):

- `corpus/lessons/README.md:21` (base) `-**Rows: 33. Files: 33.** The count is the runner's own partition glob` → `+**Rows: 34. Files: 34.**` (hunk `@@ -101,8 +101,9 @@`).

Disposition: a count line in an index, not a per-round provenance claim; the same edit is logged in the new `## Revision 4` block (`corpus/lessons/README.md`, appended at `@@ -446,3 +447,21 @@`). LOG.md: additions only (`@@ -3943,3 +3943,43 @@`). QUALITY.md: 4 lines added (pointer only). `corpus/SOURCES.md` is a new file (165 insertions).

## 3. Claims (check 3) — all re-run at base and head

Base = `git archive c42d675be`; head = `git archive 3596e2bb3`. Commands run from each tree root.

| claim | command | base (c42d675) | head (3596e2b) | report before→after | verdict |
|---|---|---|---|---|---|
| C | `find corpus/knowledge -name '*.md' \| wc -l` | 224 | 225 | 224→225 | verified |
| C | `ls corpus/knowledge/culture-material/*.md \| wc -l` | 26 | 27 | 26→27 | verified |
| C | `python3 -B reports/round-28/readme/sweep.py` | totals 224, footer_ok True | `rows 225 files 225`, topic_mismatch 0, totals_ok True, footer_ok True, exit 0 | 224→225 green | verified |
| C | `find corpus/knowledge -iname '*hunt*' -o -iname '*forag*' -o -iname '*subsist*' \| wc -l` | 0 | 1 | 0→1 | verified |
| C | `grep -c '^# ' entry` / `grep -c '^- topic:' entry` / `wc -l entry` | — | 1 / 1 / 205 | ≤~250, one H1, one topic | verified |
| C | topic byte-equal to README row (python `==`) | — | `TOPIC_BYTE_EQUAL: yes` (1147 chars) | byte-equal | verified |
| Ca | `grep -c '^revision: 2\.0' corpus/README.md` | 2 | 1 | 2→1 | verified |
| Ca | `python3 -B tools/check-readme-revisions.py` on base bytes | exit 1: `REVISION-DUP lines=[55, 57]`, `REVISION-STUB lines=[55]` | — | exit 1 on base | verified |
| Ca | same on head bytes | — | exit 0, findings 0, warnings 1 (REVISION-ORPHAN, disclosed) | exit 0 | verified |
| Ca | `--selftest` in head clone | — | `PASS=11 SKIP=0 FAIL=0`, exit 0 | 11/11 | verified |
| Ca | `python3 -B tools/check-readme-heading.py` | — | `h1_lines [1]`, findings 0, exit 0 | green | verified |
| S | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | absent | 43 | 0→43 | verified |
| S | contract census: malformed (NF!=13) / dup ids / enum+tier-inflation / missing used-by | — | 0 / none / none / none | clean | verified |
| S | `sources-census.sh validate <lane-root>` (check 4) | — | `kotodama-shokunin	ok	…/corpus/SOURCES.md`, **exit 0** | exit 0 | verified |
| S | `sources-census.sh census` | — | tier A34 B3 C6; status mined20 queued19 rejected4; invalid 0; missing 0 | as reported | verified |
| S | all 43 `opened` cells = 2026-10-19 | — | 43 | 43 | verified |
| S | Gate: every id with URL + accessed date + quote | — | 43 Gate lines, 43 `accessed 2026-10-19` | 43 | verified |
| all | `python3 reports/round-49/run-validation.py` in head clone | — | `acceptance_checks_passed: True`, `verdict: admitted`, exit 0 | admitted | verified |
| all | entry trio (`- source:`/`- verified-at:`/`- recheck:`) | — | 3 lines present | — | verified |
| all | `c31-lessons-index-audit.py --json` | — | `findings []`, exit 0 | findings 0 | verified |
| all | `git diff --name-only 78f77a6 c42d675be -- corpus tools SKILL.md` | — | 0 lines | framing-only | verified |

Notes: the clone run dirties one tracked file, `reports/round-49/validation.json` (16 lines, `.scratch/r49-*` temp names differ). See D4.

## 4. SOURCES (check 4) — PASS

Census (`bash …/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kotodama-shokunin`): `kotodama-shokunin	ok	…/corpus/SOURCES.md`, exit 0.

Re-opened rows (≥3 required; 20 done):

| row | opened source | result |
|---|---|---|
| S031 (tier A, mined) | PLOS ONE 10.1371/journal.pone.0287101 | Results para 1: "Of the 63 different foraging societies, 50 (79%) of the groups had documentation on women hunting." — match |
| S042 (tier A) | d-place.org/parameters/EA001 | description matches; values 722/265/118/62/48/35/31/6/3/0 sum 1290 — match |
| S043 (rejected, C) | sciencedaily 231020145921 | a press release restating Lacy & Ocobock, DOI 10.1111/aman.13914 on page — rejection substantiated |
| S028 (rejected, C) | folkloredatabase.com | "expressly reserves all rights in relation to text and data mining" — match |
| S029 (rejected, C) | aras.org | "about 18,000 photographic images" — match |
| S030 (rejected, C) | vulgarlang.com | demo 200 words, signup 4000 — match |
| S013 (tier B, after A→B) | ruthenia.ru thompson indexleft | "Please write me about errors etc" — match; digitization is secondary, B correct |
| S010 (tier A, queued) | github.com/def-gthill/lexurgy | "It allows the user to simulate historical changes in spoken languages by applying regular rules to a list of words." — match. Commit `fa50277` / 2026-06-18 NOT verified (GitHub API 403) |
| S033 (tier A) | PLOS ONE 10.1371/journal.pone.0309543 | "concerns were raised about the reliability and replicability of the results" — match |
| S032 (tier A, title-only) | Crossref 10.1016/j.evolhumbehav.2024.04.014 | title and vol 45 issue 4 page 106586 — match; body unread, scope limited to title (acceptable) |
| S035 | Crossref 10.2307/2801707 | "Egalitarian Societies", Man, 17(3), 431, 1982-09 — match |
| S036 | Crossref 10.1086/203816 | title and Current Anthropology record — opened as identity only |
| S040 | Crossref 10.2307/279653 | abstract "mapping-on" and "logistics" — match |
| S041 | Crossref 10.1126/sciadv.abd0310 | "in statistical parity with early male hunter burials" — match |
| S038 (tier A) | routledge 9781138702615 | "Sahlins concludes, controversially, that the experiences…" — match |
| S039 (tier A) | press.princeton.edu foraging-theory | "present the basic “average-rate maximizing” models and their extensions." — match |
| S037 | culturalsurvival ecologically-noble-savage | "The recently accumulated evidence, however, refutes this concept of ecological nobility." — match |
| S002 | github cldf-datasets/wals | "the derived dataset using the DOI of the particular released version you were using" — match (reader render; a curl grep missed it across a Markdown link) |
| S001 | glottolog.org/about.html | Contributing: "Glottolog data is curated in a public repository…" — match |
| S034 | Crossref 10.1017/CBO9781139176132 | "challenges the preconceptions that hunter-gatherers were Paleolithic relics living in a raw state of nature" — match (Cambridge fetch returned HTTP 429; checked via Crossref abstract) |

Anchors in the entry (check via sha256 and line reads, head tree):
- `algonquian.md` sha256 `8260bad1…261e0c` = pinned value (match). Line 3 "seasonal subsistence, material culture, and naming, with explicit regional limits" — match.
- `inuit.md` sha256 `52c5a11b…8ef0ca` = pinned (match). Line 159 "analytical production model, not an asserted indigenous taxonomy" — match.
- `algonquian.md:147-148` present ("Do not extend a Mille Lacs wild-rice/maple round…") — match.

## 5. Discernment spot-check (check 5, LEARNING.md)

| sample | gate decision | reviewer verdict | reason |
|---|---|---|---|
| ADMIT: `culture-material/hunting-foraging-subsistence.md` | admitted (C, +1 entry) | **agree** | Header trio present; 205 lines; §9 decision table, §13 calibration bank with R/C/B/H/T codes; 12 registry rows cite it; anchors and sha pins match; quotes S031, S033, S037, S038, S041, S042 re-opened and match. |
| REJECT: S043 ScienceDaily press release | rejected, C | **agree** | Page is a university press release that restates Lacy & Ocobock; no data, no page locators. Flip (open DOI 10.1111/aman.13914) is concrete and on-page. |
| REJECT: S028 Folklore Database | rejected, C | **agree, reason noted** | Rejection rests on licence (TDM reservation), not epistemic quality. The teaches-cell states this. Acceptable taste call; flip is concrete. |
| TIER (not a reject): S034 Kelly, S038 Sahlins, S039 Foraging Theory (tier A) | admitted A on publisher abstracts/descriptions | **disagree** | Contract §Shape "tier" lists A as primary/authoritative (spec, docs, source, original paper, maintainer statement). A publisher blurb is none of these. Recommend B, or record as a lesson. |

## 6. Credentials (check 7) — PASS

Command: `git diff c42d675be..3596e2bb3 | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'` → no output, grep exit 1.

## 7. New knowledge entries (check 6)

- Header trio present (`- source:` / `- verified-at:` / `- recheck:`; `grep -cE`→3).
- Recheck runs: sweep (§3); `algonquian.md:147-148`, `inuit.md:159`, and EA001 re-opened.
- Claim matches source: S031 36/41 → 87%, 87.8% exact (§7 of entry); S042 counts match; S038 quote corrected per its page.
- Corpus-wide: 68 of 224 base and 68 of 225 head knowledge files lack at least one bullet-form trio line. Command: `for f in corpus/knowledge/**/*.md; grep -qE '^- source:' && grep -qE '^- verified-at:' && grep -qE '^- recheck:'`. Unchanged by the round.

## 8. Report conformance (check 8)

`.ufo/reports/round-49/kotodama.md` (fleet-ledger worktree, 165 lines) contains: Work performed, Landed changes, Before → after measurements, SHONEN, Sources & frontier, Mistakes, Trend verdicts, L0 questions, Integrator notes. No `[x]`: the only match for `[x]` in `SHONEN.md` is the legend line (`` `[x]` only with a named non-author verifier``). It cites round commits `c6a174d`, `8c78e6b`, `3596e2b`. Fail-closed collision check: `/home/vgpnk/Projects/shokunin/.ufo/reports/round-49/kotodama.md` does not exist (verified).

## 9. Per-axis verdicts (recommended; all six scored axes)

| axis | report | recommended | evidence |
|---|---|---|---|
| coverage | improved (C) | **improved** | §3 C rows verified: 224→225, culture-material 26→27, filename owner 0→1, sweep green |
| calibration | improved (Ca) | **improved** | §3 Ca rows verified: 2→1, base control exit 1, head exit 0, selftest 11/11 |
| depth | improved (S, capability) | **improved, conditional** on tier fix (§5) | census clean (exit 0), 43 rows, 13 re-opens match; tier A on publisher blurbs is a depth-of-evidence defect |
| operability | unchanged, not harmed | **unchanged** | `c31` audit findings 0; lessons index revision 4 |
| freshness | unchanged (paused) | **unchanged** | freshness pause in force (`claims.json`); no freshness claim made |
| adjacency | unchanged | **unchanged** | topic sweep at head: 2 partial owners pre-existing (`algonquian.md:3`, `semantic-fields-lexicon-building.md:3`) + new entry; 0 sibling owners of the register |

## 10. Trend verdicts

- **Expansion — `improved`.** +1 admitted entry on uncovered ground (filename 0→1), citing 12 S rows (`used-by` check: all 12 list the entry path, §4).
- **Quality — recommend `unchanged`.** The report's "improved locally, flat corpus-wide" is not a LEARNING.md value, and the LEARNING.md `improved` condition ("a weaker entry is superseded… or stale entries re-verify") did not occur. Entry quality is good; the trend observable did not move.
- **Discernment — recommend `improved` only if the tier disagreement (§5) is logged as a lesson; otherwise `unchanged`.** Gate decisions on the sampled admit and two rejects agree (§5). The critic's falsifications are recorded (report `## Mistakes`), but no non-author verdict was on record before this check. No QUALITY criterion added (`corpus/QUALITY.md` diff: pointer only).

## 11. Defects by severity

- **D1 (medium) — tier inflation.** S034 (`Kelly 2013` publisher abstract), S038 (Routledge description), S039 (Princeton description) are tier A. Contract A list excludes publisher descriptions. Evidence: `corpus/SOURCES.md` rows S034/S038/S039 (`| A |`); scope cells "publisher abstract", "as described by its publisher". Fix: tier B (new `supersedes` row per contract rule 2, or pre-landing change, which the report may record).
- **D2 (low) — Mistakes count wrong in report and LOG.** Measured 23 data rows: `awk '/^## Mistakes/{m=1;next} /^## Frontier/{m=0} m && /^\| / && !/^\| class/' corpus/lessons/round-49.md | wc -l` → 23. Report `## Integrator notes` says 22 and "LOG undercounts by one"; LOG.md:3978 says 21. Both figures wrong.
- **D3 (low) — trend label outside vocabulary.** Report `## Trend verdicts`: "improved locally, flat corpus-wide" (LEARNING.md allows one value per trend).
- **D4 (low) — receipt not byte-reproducible.** `run-validation.py` writes `.scratch/r49-*-<random>.md` names into `reports/round-49/validation.json` (16 changed lines after re-run in clone). Verdict fields identical (`acceptance_checks_passed: True`, `verdict: admitted`). Fix: deterministic temp names.
- **D5 (low) — in-place count edit.** `corpus/lessons/README.md` `Rows: 33` → `34` in place (§2). Self-disclosed in revision 4. Precedent exists (revision 3).
- **D6 (low) — unverified pointer.** S010 `fa50277 (2026-06-18; v1.7.6)`: GitHub API returned HTTP 403; commit hash unverified (quote verified).
- **D7 (info) — report-known defects, confirmed.** `targets.json:137` inverted instruction and `claims.json:19,30` "0 true topic owners" are filed bytes, corrected in report and LOG (confirmed by grep). Entry §2 boundary omits three neighbours (report-disclosed, not re-checked).
- **D8 (info) — revisions control warns on base-era headless paragraph** (`REVISION-ORPHAN lines=[90, 101]`, head). Disclosed; warning-only.

## 12. Verification gaps

- Not re-run: `symbolism-synthesis-method.md:69`, `kinship-terminology.md:63` (entry recheck list).
- Not opened: JSTOR full text of S035 (open-access paywall; entry marks `(to-verify)`); S010 master commit `fa50277`.
- Cambridge S034 page returned HTTP 429; S034 quote checked via Crossref abstract (same text).
- Freshness-gate inputs (`.scratch/r49-claims-candidates.json`) were not in the committed tree; `tools/harness/claims-freshness.py` is committed. The declared freshness result (`claims.json` `declared_after_freshness_gate`) was not re-run.
- Discernment sample is 4 gate decisions; not a statistical sample.

Scratch `/tmp/kaika-verify/kotodama/` deleted after this report was written.
