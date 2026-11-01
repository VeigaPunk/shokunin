# kasegi — round 51 report (2026-11-01)

Lane: `fleet/kasegi-shokunin`, branch `master`. Base `bcd5d89a65ab612ef88e3d49cea0ef3cb3ccca09`; lane tip of record
`acbdd202b7490a0c4892e78d140952b99db45ee5` (pushed to origin master; `git ls-remote origin refs/heads/master` =
`acbdd202…` = local HEAD). Frozen claims: `.ufo/waves/round-51/claims.json` (commit `73555db`), landed before
implementation. Host: Windows workspace, Git Bash, `python` 3.13.15; `python3` = Store stub (exit 49); `/home`,
`/fast` absent.

## Work performed

Round-50's non-author closure routed two first-priority defects; both are fixed first, as claims, then the round's
own coverage move landed.

- **C1 (depth:verifiability 4 — the lane's lowest non-retired axis): closure D1 fixed.** The round-50 C1 do-nothing
  control `controls/do-nothing-c1.txt` is an imported old-host (Linux) receipt, not a run on the committing host,
  and the round-50 erratum's "Windows CPython error string" host-distinguishing claim is factually wrong. Fixed by:
  a real host-produced control `.ufo/waves/round-51/controls/do-nothing-c1-winhost.txt` (the C1' counter run at a
  c5e3636 base export built per-file via `git show` on this host: instrument absent → `C1_EXIT=2`, this host's
  `Python313\python.exe` path and backslash-quoted target in the error line; reproduce commands in the receipt
  header) + `.ufo/waves/round-51/erratum-1-c1-control-provenance.md`, which relabels the imported file (kept
  byte-identical) and corrects the wrong claim on probed facts (`.ufo/waves/round-51/controls/probe-host-r51.txt`:
  `python3 --version` → Store stub, exit 49; `/fast` absent; `python /fast/...` → Git-mount path form). Evidence:
  commits `73555db`, `aca3c29`; erratum names all four mislabeling locations (round-50 report, `claims.v2.json`
  do_nothing_control, claims-erratum-1 §"What survives unchanged", lesson round-50 M3).
- **C2 (calibration; verdict row, not a number): closure D2 fixed.** The prose records said the census of record
  was 204/4807; the certified tip census at `021989b` reads **204/4809** (verified first-hand:
  `git show 021989b:corpus/instruments/citation-survival.md`). Fixed append-only (R9): lesson round-50 **Erratum 2**
  names 4809 at `021989b` and the regenerated-after-record pattern; the LOG round-51 entry and the SCORECARD
  round-51 section carry the correction against their own round-50 rows; every filed 4807 line stayed
  byte-identical. Evidence: commit `aca3c29` (lesson), `c5743f8` (LOG + SCORECARD).
- **C3 (coverage 8): frontier F32 admitted — CISA Vulnrichment.** The surface: CISA's ADP-container enrichment of
  public CVE records (SSVC decision points on every analyzed CVE, conditional CWE/CVSS, KEV blocks for KEV-listed
  CVEs, CNA-precedence drop rule, major.minor.patch SSVC version encoding, CPE discontinued 2024-12-10), grounded on
  **S081** — CISA's own README at the repo's default branch `develop` (capture
  `corpus/source-snapshots/round-51/S081.txt`, sha256 `2da09414…`, 8290 bytes / 120 lines, fetched
  2026-11-01T02:48:34Z, HTTP 200 / 8501 raw bytes; manifest with 12 assertions Q1-Q12 each exactly-once;
  `source-recheck.py --source S081` exit 0, receipt `controls/s081-recheck.txt`). The **pre-freeze neighbor screen**
  (mandatory since the round-50 D1 lesson) ran BEFORE the freeze: `grep -ric vulnrichment` over
  corpus/knowledge, corpus/README.md, PROVINCE.md, corpus/SOURCES.md, SKILL.md = 0 hits in every file;
  "Authorized Data Publisher" = 0 hits in PROVINCE/README; the entry's §Distinctness names F18/F20/F22/F25/F30
  explicitly. Evidence: commits `73555db` (capture + manifest + freeze), `85e1ea5` (entry, rows, receipts).
- **PROVINCE / registry honesty work (frontier step, not a claim):** the context-named public surface
  `VeigaPunk/open-bug-bounties` was probed read-only (`controls/mirror-probe.txt`): same-named public board, but its
  history provably lacks the lost checkout's recorded HEAD `1307b8b` (gh api → 422) and its root inventory matches
  neither the r15 layout nor the receipt-store → recorded as **S082, rejected with reason and flip**; PROVINCE r51
  status annotation records the negative answer; RECEIPT-STORE-LOST stays corpus-attested-only.
- **Mistake mining:** `corpus/lessons/round-51.md` — two own mistakes (the cd-then-relative-DEST export script
  wrote 496 files into the lane worktree, caught by the counter printing 0 while the script said 496; the
  assumed-`main` capture ref 404'd) plus the two inherited defects fixed this round, each with class / evidence /
  captured-by / fix.
- **The gate caught its own round — recorded, not gamed:** the first census regeneration predated this round's gate
  receipts (which the lesson cites) → first tip re-check read `CENSUS-FRESH=stale` (3 citations GONE→RESOLVES); the
  second re-check caught the SCORECARD correction changing the line count the census rows cite. The census of record
  was regenerated over the truly final tree and the SCORECARD census paragraph records the whole sequence (freeze
  rev 3); final gate receipt `controls/c1-gate-final-r51.txt` = `CENSUS-FRESH=ok files=2`, exit 0 at `acbdd20`.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Freeze `claims.json` + S081 capture + manifest + 7 base control receipts (incl. `do-nothing-c1-winhost.txt`, `do-nothing-c2-r51-winhost.txt`, `probe-host-r51.txt`, `mirror-probe.txt`) | round-51 entry (freeze bullet) | `73555dbaaea5c18456216b6c2646e97914d7b62b` |
| Erratum-1 (D1 relabel + correction) + lesson round-50 Erratum 2 (D2: 4809 at `021989b`) | round-51 entry (C1, C2 bullets) | `aca3c29df8e5ebe9819af51fc1c2c18fd3acad5a` |
| F32 landing: entry `corpus/knowledge/cisa-vulnrichment-adp-enrichment.md`, SOURCES S081+S082 + sweep paragraph, README round-51 admission block (frontier 31→32), PROVINCE r51 amendment + mirror annotation, counter after-receipt | round-51 entry (C3, registry bullets) | `85e1ea5697c302bce2aaf6249ef937de394936a6` |
| Lesson round-51 (2 own + 2 inherited mistakes), LOG round-51 entry, SCORECARD round-51 result, census regen, gate+selftest receipts, freeze rev 2 | round-51 entry (whole) | `c5743f851a169a74cb145c0d12b3a930a9dbcf7d` |
| Second gate catch: census of record over the truly final tree, SCORECARD census paragraph records the catch, receipts re-measured, freeze rev 3 | SCORECARD round-51 census paragraph (the LOG entry's C2 bullet already names the rule; the catch is recorded where the figures live) | `acbdd202b7490a0c4892e78d140952b99db45ee5` |

Range stat: `git diff bcd5d89..acbdd20 --stat` = 24 files changed, 1206 insertions(+), 146 deletions(-) (the
deletions are the regenerated census files' replaced rows; every prose correction is append-only).

## Before → after measurements

- **C1** — command: `ls <lane>/.ufo/waves/round-5*/controls/do-nothing-c1*.txt` plus the probes in
  `controls/probe-host-r51.txt` (`python3 --version` exit 49; `ls /fast` exit 2; `python /fast/...` Git-mount error
  form) and `grep -c "python3: can" .ufo/waves/round-51/controls/do-nothing-c1-winhost.txt` → 0. Before: 1 C1
  control in the lane, 0 reproducible on this host (its bytes name a working `python3` and a `/fast` path this host
  lacks). After: 2, of which 1 is the host-produced control of record (`C1_EXIT=2`, Windows error form). Measured at
  `aca3c29` (control first landed `73555db`).
- **C2** — command: `grep -c 4809 corpus/lessons/round-50.md LOG.md SCORECARD.md`. Before (base `bcd5d89`): 0 / 0 /
  0. After (`acbdd20`): 2 / 3 / 5; and `grep -c "204 files / 4807 distinct"` is unchanged on the filed lines
  (append-only). Census of record: 204/4809 at `021989b` (re-derived from committed bytes) → **206/4868** at
  `acbdd20` (RESOLVES 11, INTERNAL 1075, GONE 3782; total 10388; lane total 1086/4868 = 22.31%); gate receipt
  `CENSUS-FRESH=ok files=2` exit 0, selftest `cases=3 failures=0`. Measured at `acbdd20`.
- **C3** — command: `python corpus/instruments/frontier-recheck-count.py` (lane root). Before: `FRONTIER-CENSUS
  rows=31 admitted=31 closed=1 problem-rows=30 registry=80`, `entries=34 pass=1`, zero F32 lines
  (`controls/do-nothing-c2-r51-winhost.txt`, base export bcd5d89). After: `FRONTIER-CENSUS rows=32 admitted=32
  closed=2 problem-rows=30 registry=82`, `entries=35 pass=2`, `PASS F32 ids=S081 exit=0`, all 33 inherited fails
  exactly `recheck-exit-1` (`controls/c2-counter-final-r51.txt`). Registry rows 80 → 82
  (`grep -cE '^\| S[0-9]{3,} \|' corpus/SOURCES.md`). Measured at `85e1ea5` (counter bytes identical at `acbdd20`).

## Sources & frontier

SOURCES.md rows before→after: 80 → 82 (`grep -cE '^\| S[0-9]{3,} \|' corpus/SOURCES.md`: 80 → 82). S081 (docs,
tier A, mined, opened 2026-11-01, recheck 90d, used-by the F32 entry) — Gate record with URL, access date and the
≤25-word located quote in `corpus/lessons/round-51.md` §Gate: "the public repository of CISA's enrichment of public
CVE records through CISA's ADP (Authorized Data Publisher) container" (S081.txt:2; 24 words). S082 (code, tier C,
rejected, on-release) — the VeigaPunk mirror, rejected with reason and flip. Sweep paragraph appended at SOURCES EOF
(identified 2, screened 2, included 1, excluded 1, stop stated). No pre-existing row's status/recheck/used-by cell
changed (R8). Census validate: round start exit 0, round end exit 0 (5 known W04 duplicate-url warnings, unchanged;
no new warning from S081/S082).

## Trend verdicts

- **expansion: improved.** Frontier 31 → 32 admitted on a genuinely new, first-party-captured surface (CISA's own
  README), reached through the planned-for-round-51 scout with the pre-freeze neighbor screen executed before the
  freeze; PROVINCE gained the F32 amendment plus an honest negative answer on the mirror-identity question (S082).
  Coverage score honestly held at 8 (denominator operator-owned).
- **quality: improved.** Evidence integrity repaired where the closure routed it: the lane's C1 do-nothing control
  of record is now a receipt this host actually produced, with the reproduce commands committed in-header; the
  census-figure correction landed append-only and the fresh-regeneration rule was then enforced on the round's own
  bytes — twice, because the round-50 gate caught this round itself (receipts-cited-before-they-existed drift, then
  SCORECARD line-count drift), and the catches are recorded in the SCORECARD census paragraph rather than smoothed
  over.
- **discernment: improved.** The mirror that looked like a recovery of the lost origin-work checkout was refused as
  such on a two-probe negative (history 422; inventory mismatch) and recorded as a rejected row with a concrete
  flip, instead of a wished-for re-grounding; the two inherited defects were re-verified first-hand before fixing;
  scores asserted: none; held: all (4 / 8 / 9); the calibration verdict is a row, not a number.

**Assimilation:** `considerthese/` exists (8 files, 2026-10-19 … 2026-10-26) and was mined; the ledger
(`corpus/knowledge/considerthese-proposals-ledger.md`) is current through the round-46 dispositions. Two proposals
remain open (write the concrete 4→5 / 7→8 score-distance criteria into SCORECARD §Saturation; run one end-to-end
domain-task round per SHONEN box 2) — both noted for future rounds, neither adopted this round: the round already
carried the two routed defects plus a frontier admission, and a SCORECARD criteria edit this late would re-trigger
the census/gate convergence a third time. Assimilation: none — shokuknow unreachable.

## SHONEN

Lane SHONEN.md (4 boxes; none may be `[x]` without a named non-author verifier):

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — unchanged this round
  (SKILL.md untouched; density guard held); Author assertion stands, outside promotion verification still required
  (SHONEN.md as committed).
- `[ ]` At least one end-to-end domain task executed and logged in LOG.md — untouched this round; the
  considerthese proposal for it is noted above, not adopted.
- `[~]` Instructions executable by an agent without oral context — evidence: the round's own instruments ran
  end-to-end from committed bytes on this host (`source-recheck.py`, `frontier-recheck-count.py`,
  `census-freshness-check.py`, `resolve.py`, `capture-source.py`); still not promotion.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — evidence: PROVINCE r51 appends stay inside the domain
  (a CVE-enrichment program surface and a bounty-board mirror probe); live-target testing still refused.

## Honest stops

- No independent non-author verification this round: no seat ran (no AgentSwarm surface on this host — same
  disposition as rounds 49-50; recorded in the lesson's Wave disposition, not simulated). The claims verify on
  frozen predicates by re-derivable commands only.
- The 67 host-bound recheck lines and the 22 gated lines remain operator-owned disclosed debt; L0 kasegi round-50
  is unanswered and was routed around, not treated as answered (`entries=35 pass=2` is this host's honest reading).
- The erratum-1 correction cannot reach the round-50 report (fleet repo, orchestrator-committed); this report is
  the record of that correction.
- Scratch dir `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/scratch/kasegi-r51` is deleted
  after this report; every receipt it carried is committed under `.ufo/waves/round-51/controls/`.

ROUND kasegi r51 done lane_head=acbdd202b7490a0c4892e78d140952b99db45ee5 pushed=yes claims=3 admitted_self=true
