# souji round 51 report — the r50-closure routed record corrections land append-only; the session-workspace live census refresh

Lane: `fleet/shokunin-repo-hygiene` (branch `master`), Windows host. Round base
`d1b8734d835171c7329225fdaab249c5c6799de8` (the r50 non-author spot-check,
verdict `ok, admitted`). Final tip `e004ee1a765df8e1f9d5e14bf13f76539ed133df`,
pushed to origin (verified by `ls-remote`: both `e004ee1a…`). Three commits,
all through the plumbing helper, all `souji-shokunin <souji@shokunin.local>`:
freeze `851093b670e3fd1416df326d0479168222959ed1` → content `d9aa24f4b09efa8c8b69a6035ba1f3a09b6d35dc` →
end receipts `e004ee1a765df8e1f9d5e14bf13f76539ed133df`. PROVINCE.md untouched
(absent from the range diff-tree).

## Work performed

- **Carry-in item 1 (r50 closure routed item 1, addressed first as directed):**
  the duplicated `## Gate` "Reject sample" bullet in `corpus/lessons/round-50.md`
  — fixed by the appended `R51-CORRECTION` line naming the duplication; the
  duplicated bytes preserved verbatim (the frozen counter's dup leg reads
  exactly two occurrences at BOTH the base and the tip revs — append-only
  proven, never an in-place edit). Evidence: `census/round-51/records/c1-tip-content-51.txt`.
- **Carry-in item 2 (r50 closure routed item 3):** the r50 NTFS tip receipt's
  missing `quoted_d_rows` field — fixed by the appended field with a
  provenance note; the six-path listing and `count=6` proven byte-identical to
  base by the counter's listing leg. Evidence: same receipt; the corrected
  receipt `git show e004ee1a…:census/round-50/records/ntfs-exclusion-check-tip.txt`.
- **Carry-in item 3 (r50 closure routed item 2, operator-owned):** the census
  conf-form rc-2 host state stays disclosed inside every receipt
  (`CONF-RC=2` verbatim in both v1 receipts); the consolidated r50 L0 proposal
  line remains open; routed around, nothing assumed answered. No new L0 line
  owed (the question is already consolidated; nothing needed a new operator
  decision).
- **Claim C1 (calibration 7 — the lowest non-retired axis):** the two routed
  corrections above PLUS the standing landing-suite receipt restored to green
  at the tip, per the r50 closure's directed ordering: the r50 tip-state
  suite receipt honestly read `COULD-NOT-EVALUATE dirty worktree … 31
  unexpected rows` exit 2 (committed r50 evidence
  `census/round-50/records/c1-suite-tip-50.txt`); this round the r46 frozen
  counter reads green (exit 0, `unfiled=0`) at the content tip (clean window,
  receipt committed `census/round-51/records/c1-suite-content-tip-51.txt`)
  and at the FINAL tip after the terminal idx-repair (quoted below).
- **Claim C2 (coverage 8, sourced on S274):** the round contract's census
  surface — this session workspace — re-censused live: 126-row dry-run
  capture `census/round-51/workspace-census.tsv` (metadata only; r46 method,
  r46-comparable non-hidden scope disclosed in the method note
  `census/round-51/workspace-census.txt`), drift receipt
  `census/round-51/records/ws-drift-vs-r46.tsv` (every COUNT line and
  ADDED/REMOVED key row re-derived by the frozen counter from the two
  committed captures), per-artifact receipts
  `census/round-51/records/per-artifact-receipts.tsv` (helpers-r74 NOT-SAFE,
  disposition unchanged pending operator approval; scratch-r80v NOT-SAFE
  secrets-refusal — the new-since-r46 foreign scratch root — foreign, active,
  untouched). Nothing moved, nothing deleted, no removal proposed;
  certification OFF, receipts advisory.
- **Frontier step:** SOURCES curated (197 → 198, S274 opened live this round,
  from the standing Leads list); one mistake mined beyond the round's own
  three counter-defect catches (four Mistakes rows total,
  `corpus/lessons/round-51.md`); census before→after both ways with the
  conf-form rc-2 disclosed (before = round start, after = end, both exit 0
  via the adapter; the contract's literal conf form reads rc 2 `souji
  missing` on this host — the documented L0-open state, disclosed inside both
  receipts).
- **Fresh-start round (§7):** the last three REJECTED closures were re-read
  and spot-checked before anything was declared. Ruling-out table:
  - r43 (preregistration-after-ready-handoff; counters that could not bind
    their captured tokens) → ruled out by the ONE-commit freeze
    (`851093b…` carries prereg + counters + populations + controls + pre-flight
    receipts, before any claim receipt exists) and by counters whose every
    value is parsed from committed bytes at named 40-hex revs.
  - r44 (frozen predicate honest work could not meet: register identities
    disagreed with the frozen counter) → ruled out by deriving every target
    from states the base honestly exhibits (blob absence for C2's red arm;
    the routed defect text itself names C1's defects) and by pre-freeze
    feasibility runs of every legged command over a synthetic tip containing
    exactly the claimed byte shapes — which caught three real counter defects
    BEFORE they could become frozen.
  - r45 (the different-instrument limit: the new instrument accepted what the
    base already accepted) → ruled out structurally: the SAME counter bytes
    measure both arms (red at the base rev, green at the tip rev; only the
    world moves), and both claims' repair direction is the r50 closure's own
    routed items plus the round contract's own census surface — no new
    instruments invented to flip verdicts.
- **L2 floor:** no dispatch surface on this host; dispatched=0, completed=0,
  dead=0; no wave dispatched, no WAVE-DONE claimed; standing L0 questions
  routed around (round-44 symlink contract, round-46 L2 floor, round-46
  staged package, round-48/50 census-form routing); nothing assumed answered.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze: preregistration, c1/c2 counters + arms populations, red do-nothing controls (both EXIT=1 at base), pre-flight receipts (census-before raw + v1 receipt, porcelain-at-base 8 rows, idx-repair base 8→6, NTFS base 6 paths, feasibility synth red/green x2, defects note), S274 captures | LOG.md `## Round 51` | `851093b670e3fd1416df326d0479168222959ed1` |
| content: the two carry-in corrections (`R51-CORRECTION` line; `quoted_d_rows` field), SOURCES S274 + provenance paragraph, lesson round-51 (Gate + 3 Mistakes), SCORECARD r51 section + planned r52, LOG r51 entry, SKILL r51 contracts, workspace census TSV + method note, drift receipt, per-artifact receipts | LOG.md `## Round 51` | `d9aa24f4b09efa8c8b69a6035ba1f3a09b6d35dc` |
| end receipts: census-after raw + v1 receipt + verify + the disclosed E12 first take, c1/c2 content-tip receipts, freeze-check content tip, suite content tip, NTFS tip re-check, SOURCES S274 position fix, lesson Mistake row 4, LOG end-receipts addendum | LOG.md `### Round 51 end-receipts addendum` | `e004ee1a765df8e1f9d5e14bf13f76539ed133df` |

Landing verification: `git diff <base>..<new> --stat` per landing and
`git show <new>:<path>` spot reads (the helper's printed shas only);
idx-repair ran after every landing (base: BEFORE 8 → AFTER 6 unexpected=0,
`census/round-51/records/idx-repair-base-51.txt`; content: 19→6, receipt
staged in scratch; terminal end: 18→6, receipt `idx-repair-end-51` in
scratch, `AFTER rows=6 unexpected=0` EXIT=0; the six-path Amendment-1
tolerance not widened — NTFS re-checks at base and tip both read exactly the
six pinned paths with `quoted_d_rows=6`/`count=6`).

## Before → after measurements

| claim | axis | before | after | counting command | measured commit |
|---|---|---|---|---|---|
| C1 routed record corrections + standing suite receipt | calibration 7 | at base `d1b8734…` the frozen counter is red, exit 1: `SUMMARY corr=FAIL dup=ok ntfs=FAIL listing=ok corr_lines=0 dup_base=2 dup_tip=2` (control `census/round-51/controls/c1-control-donothing.txt`); the r50 tip-state suite receipt: `COULD-NOT-EVALUATE … 31 unexpected rows`, exit 2 | at content tip `d9aa24f…`: `SUMMARY corr=ok dup=ok ntfs=ok listing=ok corr_lines=1 dup_base=2 dup_tip=2`, exit 0 (receipt `census/round-51/records/c1-tip-content-51.txt`); identical SUMMARY re-derived at the final tip `e004ee1…`, exit 0; suite at content tip AND final tip: `SUMMARY assertions=552 mismatches=70 registered=70 corrected=0 exempted=0 unfiled=0`, exit 0 | `python -B census/round-51/c1-counter.py --root LANE --rev FULL40 --base-rev d1b8734d835171c7329225fdaab249c5c6799de8 --scratch DIR`; suite: `python -B census/round-46/c1-counter.py --root LANE --rev FULL40 --work SCRATCH` | content tip `d9aa24f4b09efa8c8b69a6035ba1f3a09b6d35dc` (receipts committed); final tip `e004ee1a765df8e1f9d5e14bf13f76539ed133df` (re-measured; receipts in session scratch, quoted here) |
| C2 live workspace census refresh + drift receipt + per-artifact receipts (sourced on S274) | coverage 8 | at base `d1b8734…`: `PRISTINE FAIL WORKSPACE-CENSUS-ABSENT …:census/round-51/workspace-census.tsv (rc=128)`, exit 1 (control `census/round-51/controls/c2-control-donothing.txt`) | at content tip `d9aa24f…` and final tip `e004ee1…`: `SUMMARY shape=ok drift=ok receipts=ok limit=ok rows=126 added=79 removed=2`, exit 0 (receipt `census/round-51/records/c2-tip-content-51.txt`; final-tip re-measure quoted here); pasteable greps at the tip: `grep -c -P "\tin-use/pushed\t" census/round-51/workspace-census.tsv` → 14; `grep -c "^ADDED" census/round-51/records/ws-drift-vs-r46.tsv` → 78; `grep -c "^| S274 |" corpus/SOURCES.md` → 1 | `python -B census/round-51/c2-counter.py --root LANE --rev FULL40 --base-rev d1b8734d835171c7329225fdaab249c5c6799de8 --scratch DIR` | content tip `d9aa24f4b09efa8c8b69a6035ba1f3a09b6d35dc` (receipt committed); final tip `e004ee1a765df8e1f9d5e14bf13f76539ed133df` (re-measured) |

Final-tip re-measurements (session scratch `final-tip-measure-51.txt`, quoted):
`C1-FINAL-TIP-EXIT=0`, `C2-FINAL-TIP-EXIT=0`,
`FREEZE-CHECK-FINAL-TIP-EXIT=0` (`SUMMARY claims=2 findings=0` over the
preregistration at `e004ee1…`; also green at the freeze and the content tip,
receipt `census/round-51/records/freeze-check-at-content-tip-51.txt`),
`SUITE-FINAL-TIP-EXIT=0` (`SUMMARY assertions=552 … unfiled=0`; porcelain at
that moment = exactly the 6 tolerated rows; terminal idx-repair receipt
`AFTER rows=6 unexpected=0`).

Numeric axis scores unchanged (calibration 7, operability 8, coverage 8): no
reproducible 0–10 mapping exists (standing SCORECARD disclosure). C1 repairs
the routed record defects append-only and restores the standing receipt
ordering; C2 runs installed tools over live targets (the r47 precedent — no
capability row proposed), dry-run, no authority taken.

## Sources & frontier

SOURCES: 197 → 198 rows.

- Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
  (197 at base `d1b8734…`; 198 at the final tip `e004ee1…`).
- **S274 admitted (opened live this round, the sourced claim C2's ground):**
  https://git-scm.com/docs/git-cherry opened live 2026-11-01 by this session
  (curl -sSL, HTTP 200, no redirect, 27219 bytes, sha256
  `abe223069d94dda86990eaa958c684c18742e23bcfde026b2b0a576ad9ab73e3`; full-page
  capture `census/round-51/sources/s274-git-cherry-page.html`). Located quote
  (15 words, counted by the pasted command in
  `census/round-51/sources/s274-git-cherry-located-quote.txt`; tags stripped
  display-faithfully with empty replacement): "git-cherry therefore detects
  when commits have been "copied" by means of git-cherry-pick[1], git-am[1]
  or git-rebase[1]." Grounds the pushed-receipt copied-history limit named in
  the census method note (a rebased/cherry-picked/am'd-then-pushed lane reads
  unpushed to the sha comparison; no r51 lane row is in that state —
  disclosed, not exercised). Opened from the standing Leads list; used-by
  `corpus/lessons/round-51.md`; no existing row's status/recheck/used-by cell
  changed.
- **Reject sample (stated explicitly):** ONE candidate fetched, admitted,
  ZERO new reject rows; the fetch bound = the single capture above (the
  census runs are local metadata reads, not fetches); the Leads item is
  discharged by S274's admission.
- **Census before→after (2b), both outputs and exit codes:** before (round
  start): adapter exit 0 — `CENSUS-RUN lane=souji conf_rc=2 dir_rc=0`,
  DIR-RESULT=ok, DIR-WARN-W04=59 (raw `census/round-51/records/census-before.txt`;
  v1 receipt `census-before-receipt.txt`, `verify` ok over every check
  including both script hashes). After (round end): adapter exit 0 —
  `CENSUS-RUN lane=souji conf_rc=2 dir_rc=0`, DIR-RESULT=ok, DIR-WARN-W04=59
  (raw `census/round-51/records/census-after.txt`; v1 receipt
  `census-after-receipt.txt`, `census-after-verify.txt` reads `VERIFY ok …
  checks=grammar,digest,raw-section,rc,w04,result,adapter-sha,fleet-script-sha
  adapter=ok`). Re-verified at the final tip: exit 0, dir_rc=0, 59 W04. The
  contract's literal conf form reads rc 2 `souji missing` on this host —
  disclosed verbatim inside every receipt (the carried r48/r50 L0 question;
  routed around, nothing assumed answered). The first end-census take read
  `E12 S274 row outside Registry section` (dir_rc=1) because the S274 row was
  appended at end-of-file — disclosed, row moved inside the Registry in the
  end commit (lesson Mistake row 4; the first take committed as
  `census/round-51/records/census-after-first-take-disclosed.txt`).
- **Mistake mining (2b):** `corpus/lessons/round-51.md` `## Mistakes` — four
  rows, each with evidence pointer, captured-by and fix: (1) the two-sided
  header-row filtering that read a TSV table header as a REMOVED workspace
  row (pre-freeze feasibility leg); (2) the unpinned definition of
  `new-top-level-candidates` reading 2 where the receipt line says 1 (same
  leg); (3) the CRLF receipt vs LF-assuming regex that vacated the listing
  leg to two empty sets passing green (pre-freeze receipt review); (4) the
  end-of-file SOURCES append landing outside the Registry section, caught by
  the round-end census gate itself (E12). Disclosed, not mined as rows: the
  discarded first census take that included the host tooling dir `.zcode`
  (124 vs 126 rows; r46-comparable scope disclosed in the method note), the
  live-workspace growth 86 → 89 foreign scratch dirs between two r51 takes
  (a census row is a point-in-time fact), and the two discarded suite-receipt
  takes (staged-inside-repo porcelain pollution — the r48 lesson recurring —
  and a missing `--work` dir; both named in the committed suite receipt's
  header).

## Trend verdicts

- **expansion: unchanged** — no `corpus/knowledge/` entry, no Core promotion,
  no PROVINCE change (absent from the range diff); SOURCES +1 on the standing
  Leads list; the workspace census refresh covers already-owned census ground
  with current data (coverage stays 8, no new surface claimed).
- **quality: improved** — the round's record-accuracy repairs make two prior
  artifacts self-consistent again (the round-50 lesson Gate duplication named
  append-only; the NTFS receipt shape now matches its base sibling), and the
  standing suite receipt is green at the tip again under the ordering the
  closure directed; the drift receipt's every number re-derives from
  committed captures by a frozen counter (re-run by this session at two revs;
  evidence above).
- **discernment: improved** — four mistakes mined with same-round executed
  fixes, three of them caught by pre-freeze feasibility/review before they
  could become frozen instruments, one by the round-end census gate doing
  exactly its job; the S274 admission names its scope precisely (the
  equivalence semantics, not the census labels); fresh-start rulings
  re-derived against r43/r44/r45; both claims' controls red at the base with
  greens re-derived from committed bytes; the honest E12 failure is disclosed
  with the first take committed, not deleted.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — evidence: SKILL.md Decision tables/Error patterns/Checklists/
  Gate registry + the r51 contracts section; corpus/SOURCES.md S274 (and
  S100–S103 standing); corpus/lessons/round-51.md Gate. (Author-asserted
  boxes; no non-author verifier wrote `[x]` this round — the r50 closure's
  SHONEN note for the operator stands.)
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  evidence: LOG.md `## Round 51` (the live workspace census end-to-end:
  capture, drift receipt, per-artifact receipts, sourced limit) and LOG.md:362
  (the r21-era operator sweep, standing).
- [~] Instructions executable by an agent without oral context — evidence:
  `census/round-51/c1-counter.py` / `c2-counter.py` run red-at-base and
  green-at-tip from committed bytes alone (controls + feasibility receipts);
  the preregistration's CLI lines are the executable contracts.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: PROVINCE.md
  absent from the round range diff-tree; the workspace census classified
  foreign/other-lane surfaces report-only and routed nothing; souji took no
  removal authority (certification OFF, K5 HELD).

Assimilation: none — the lane repo holds no `considerthese/` directory
(named-path check at round start); shokuknow unreachable from this host.
Assimilation: none — shokuknow unreachable.

Scratch: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/scratch/souji-r51`
deleted at round end (the receipts quoted above were read from it before
deletion; every committed artifact is in the lane repo).
