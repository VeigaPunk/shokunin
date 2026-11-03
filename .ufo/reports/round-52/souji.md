# souji — round 52 (attempt 1) — report

Lane repo: /home/vgpnk/Projects/shokunin/souji-shokunin (branch master). Base f778b9d131574d3ff09c0cc8a077643c0fc84bb4 (r51 non-author spot-check, ok/admitted). Lane tip reported here: fbf1ea3c58774b4fe28b8c3441347dde96db48f3 (`ls-remote origin refs/heads/master` equals it). Final lane commit set: df7d1300 (freeze), ab8c1fcf (round-start receipt), 5b34efe7 (tool + fixture), 8ec412c6 (capture set), 9c0f1281 (C1 corrections, LOG), 049fdc06 (end census + L1 tip checks), fbf1ea3c (standing checks).

## Work performed

Claims declared (frozen in census/round-52/preregistration.txt, freeze df7d1300):
- **C1 — calibration 7 (the lowest-scoring axis).** Enumerated declared-count annotations agree with the recomputed value; each mismatch is filed by an append-only R52-CORRECTION line.
- **C2 — coverage 8 (capability acquisition).** tools/souji-fleet-root-census.py, a read-only census of the fleet root's top-level entries, with a committed capture verified by census/round-52/c2-counter.py.
- No exploratory claim. Shape: 2 claims on 2 distinct axes, causally separable (C1 reads lane records; C2 reads the fleet-root capture).

Work items (evidence pointers):
- Protocol load: MISSION.md, AXES.md, PROTOCOL.md, CORPUS.md, LEARNING.md, shokunin and swarm skills; the r51 non-author spot-check (corpus/lessons/round-51-verifier-spotcheck.md §8, four routed items).
- Round-start census: census/round-52/records/census-before.txt (adapter: CONF-RC=0 DIR-RC=0 W04=59); census-before-receipt.txt (v1, verify ok, commit ab8c1fcf); conf form resolves on this Linux host (rc 0); porcelain-at-base.txt 0 rows; standing suite at base refused on a dirty worktree (1 row: this round's receipt, committed to clear it), then green at ab8c1fc (`SUMMARY assertions=552 mismatches=70 registered=70 corrected=0 exempted=0 unfiled=0`).
- Do-nothing controls (red at base, committed in the freeze): census/round-52/controls/c1-control-donothing.txt (`SUMMARY sites=2 mismatches=2 filed=0 unfiled=2`, EXIT=1); census/round-52/controls/c2-control-donothing.txt (`PRISTINE FAIL FLEET-CENSUS-ABSENT`, EXIT=1).
- Wave w1 (one v1 wave, 13 seats; see Round shape): spec census/round-52/… is not committed (wave dirs are gitignored); validator plan `13 spawn, 0 resume`; dispatch payload `.ufo/waves/round-52/w1-dispatch.json` (policy band 8–16); ready file `.ufo/waves/round-52/w1.ready` (taken 15:13; spawned by the orchestrator at 15:35:48 after a ~22 min queue at the 36-seat ceiling, dispatcher log `spawned souji 52 w1 13`); WAVE-DONE for all 13 seats; results `.ufo/waves/round-52/w1-results.json`.
- Wave findings (full text in corpus/lessons/round-52.md `## Wave findings`):
  - reviewer01 (C1 counter attack, 18 runs): the frozen counter reads the first annotation in the 16 characters after the anchor; a planted annotation before a stale one yields unfiled=0 without a correction; the recompute source is not pinned; a fenced correction is accepted; an in-place rewrite is accepted at one revision. Named limits (counter not edited after freeze). The tip is checked by hand (work item below).
  - critic01: C1 survives; its kill rule is not implemented for an inert correction (the counter exits 0; the prereg text says it kills); C2 "verifiable capture" weakened (a hand-written capture with the right tool bytes verifies; "sorted by name" is not instrumented). S275 "supports, with a wording condition" (applied: the knowledge entry states the lane's reading).
  - reviewer02: `#`-leading data rows are read as comments; CRLF and tab-in-name captures cannot satisfy the grammar (no escaping defined); FLEET_HEAD is format-checked only.
  - sentinel01 (security review of the wave candidate, S1–S8): S1 HIGH repo-local core.fsmonitor was executed by git ls-files during the census (marker written, execve trace in .ufo/waves/round-52/w1/S52sentinel01/receipts.txt); S2 HIGH repo-local include.path made git open files outside the root; S3 HIGH no protected-namespace refusal; S4 MEDIUM the ignored set walked the operator-protected .ufo/state/; S5 MEDIUM credential-shaped names printed verbatim; S6 MEDIUM a timeout killed only the direct child; S7/S8 LOW --out inside the root; a repo subdirectory accepted as the root. All fixed in the lane tool (below) except S5, refused rather than redacted (operator ruling, L0).
  - connector01: no sibling claims the fleet-root census surface; the two honest derivations of the ignored column (listing vs check-ignore) disagree on three rows (.jj, .ruff_cache, kumitate-shokinin) and both verify under the frozen counter. Named limit; the lane tool keeps check-ignore (the listing walks .ufo/state/).
  - scout02 (discovery of six lane annotations): SCORECARD.md:1196 (the S1 site) is the transcription defect; LOG.md:18 (dated 2026-10-18 worktree count, recomputes 1) and corpus/README.md:40 (self-dated, superseded in place) are expired dated observations, routed, not counted.
  - mutation01 (six mutants of the frozen C1 counter, two prescribed arms): kills 2 of 6 on the prescribed arms; four survivors are killed only by supplementary arms; the 200-character window mutant turns a fail-closed exit 2 into a measured value. Named kill-power limit.
  - executor03 (C1 feasibility on a synthetic repo): the frozen counter reproduces the preregistered numbers (unfiled=2 exit 1; filed=2 unfiled=0 exit 0; a wrong recomputed value unfiled=1 exit 1).
  - scribe01 (S275) and scribe02 (knowledge entry draft); scout01 (fleet-root recon: 49 entries, facts only).
- Tool hardening (lane copy tools/souji-fleet-root-census.py; the wave candidate is not committed): every git call carries `-c core.fsmonitor=false -c core.hooksPath=/dev/null -c core.excludesFile=/dev/null` and the frozen GIT_* environment; git runs in its own session and the group is killed on timeout; repository config read with --no-includes, refused on include/includeIf or core.worktree; the fleet root must be its own repository top-level; roots inside ~/.omp, ~/.ssh, ~/.gnupg, ~/.aws, ~/.kube, ~/.docker, ~/.config/gh refused; credential-shaped top-level names refuse the run; --out inside the root refused; ignored status by `git check-ignore --no-index` on top-level names (no subtree listing). Selftest 39/39 (tool-selftest.txt); the wave candidate's selftest was 34/34 and did not catch S1.
- Discrimination control for S1 (census/round-52/records/discrimination-s1.txt): the wave candidate executed a planted repo-local fsmonitor (MARKER: fsmonitor EXECUTED); the lane tool did not (lane tool: no marker).
- Fixture: tests/fixtures/r52-fleet-root-census-fixture.py on the lane tool: `SUMMARY cases=8 honest_passed=6/6 controls_failed=2/2 exit=0` (census/round-52/records/fixture-run-lane-tool.txt).
- First real capture refused on a top-level `.omp` (fail-closed). `.omp` is a tracked project OMP directory of the fleet repo (agents/executor.md, mcp.json), not the credential namespace; the name rule was narrowed (the root-namespace check still refuses ~/.omp roots). Named in the lesson's Mistakes.
- Capture: census/round-52/records/fleet-root-census.tsv — ENTRIES=49, tracked 22, ignored 22, untracked-stray 5 (.jj, .local, .ruff_cache, kumitate-shokinin, tools; all report-only), symlink 0; run receipt census/round-52/records/fleet-root-census-run.txt (staged outside the root, byte-exact copy; staged sha256 215bf849…).
- C2 counter at the capture commit 8ec412c6: `SUMMARY entries=49 rows=49 unclassified=0 class_mismatch=0 counts=ok tool_sha=ok removal_proposed=0 receipt=ok`, exit 0; re-run at the final tip fbf1ea3c, same SUMMARY, exit 0.
- C2 negative control (scratch repo, one row's class flipped to tracked): census/round-52/records/l1-tip-checks.txt §(h): `class_mismatch=1 counts=FAIL receipt=FAIL`, rc=1.
- C1 corrections: SCORECARD.md (appended block "Round 52 corrections") holds two R52-CORRECTION lines naming SCORECARD.md:1196 and census/round-51/preregistration.txt:125 (stated 78, recomputed 79). Counter at 9c0f1281: `SUMMARY sites=2 mismatches=2 filed=2 unfiled=0`, exit 0; re-run at fbf1ea3c, same SUMMARY, exit 0.
- L1 tip checks (census/round-52/records/l1-tip-checks.txt; each pasteable): (a′) annotations inside the counter's 16-character window after each anchor: 1 and 1; (b) deleted lines base→tip per touched lane file: `git diff --numstat f778b9d1 049fdc06 -- SCORECARD.md LOG.md SKILL.md corpus/README.md corpus/SOURCES.md` → 0 deletions in each; (c) corrections outside any fenced block (awk fence parity at lines 1243, 1245); (d) stale text still `(78)` at both sites; (e) the anchor appears exactly once in each site file; (f) the two corrections name the sites, stale 78 and recomputed 79; (g) the recomputed command at the tip: 79.
- Frontier step: S275 opened live (curl -sSL, HTTP 200, 244355 bytes, sha256 0c126da2…; capture and located quote under census/round-52/sources/; the quote is 25 words).
- Standing checks (census/round-52/records/standing-tip.txt, measured at 049fdc06 on a clean worktree; fbf1ea3c adds only that record): r46 landing suite `SUMMARY assertions=556 mismatches=70 registered=70 corrected=0 exempted=0 unfiled=0`, exit 0 (assertions 552→556: the round's new SCORECARD text adds four declared-evidence tokens, all registered); r51 routed-corrections counter `SUMMARY corr=ok dup=ok ntfs=ok listing=ok corr_lines=1 dup_base=2 dup_tip=2` (NTFS tolerance six paths, unchanged), exit 0; r51 workspace counter `SUMMARY shape=ok drift=ok receipts=ok limit=ok rows=126 added=79 removed=2`, exit 0.
- Round-end census: census-after.txt (adapter CONF-RC=0 DIR-RC=0 W04=60), census-after-receipt.txt, census-after-verify.txt (VERIFY ok); conf-form `sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` exit 0 (W04 duplicate-URL warnings; 199 registry rows).
- Misroot sweep (fleet root, `git status --porcelain`): ` M .scratch/run15-state.json` and `?? .scratch/run13-state.json` are orchestrator-owned and untouched; ` M .ufo/l0-questions.md` is this round's append (see the rider note below). No seat-authored fleet-root file remains (the sentinel seat's `repo/` probe was removed by the seat and is disclosed in its report).

## Landed changes

- Freeze, prereg and both counters with their do-nothing controls and pre-flight receipts — df7d1300 (census/round-52/preregistration.txt; census/round-52/c1-counter.py sha256 f5cd614c…; census/round-52/c2-counter.py sha256 863a551d…). LOG.md `## Round 52` (commit 9c0f1281).
- Round-start census receipt — ab8c1fcf (census/round-52/records/census-before-receipt.txt). LOG.md `## Round 52`.
- C2 tool and fixture and discrimination control and selftest/fixture receipts — 5b34efe7 (tools/souji-fleet-root-census.py; tests/fixtures/r52-fleet-root-census-fixture.py). LOG.md `## Round 52` (commit 9c0f1281).
- C2 capture set — 8ec412c6 (tool name-rule narrowing; census/round-52/records/fleet-root-census.tsv and run receipt; census/round-52/sources/ S275 capture and quote; corpus/SOURCES.md S275 row; corpus/knowledge/fleet-root-stray-census.md; corpus/lessons/round-52.md). LOG.md `## Round 52` (commit 9c0f1281).
- C1 corrections and round-52 record bookkeeping — 9c0f1281 (SCORECARD.md appended block: measurements, R52-CORRECTION lines, capability row, planned r53; LOG.md `## Round 52` with its corrections paragraph; SKILL.md `## Round 52 contracts` with the tool and both counter gates; corpus/README.md `## Round 52 frontier update`).
- End-of-round census and L1 tip checks — 049fdc06 (census/round-52/records/census-after*.txt, l1-tip-checks.txt). Standing checks — fbf1ea3c (census/round-52/records/standing-tip.txt).
- L0 questions (fleet repo, .ufo/l0-questions.md): four souji lines for round 52 (credential-name rule, ignored derivation, report-only strays, conf-form host note).

## Before → after measurements

| claim | before (base f778b9d1) | after | counting command | measured commit |
|---|---|---|---|---|
| C1 declared-count annotations agree | `SUMMARY sites=2 mismatches=2 filed=0 unfiled=2`, exit 1 (controls/c1-control-donothing.txt) | `SUMMARY sites=2 mismatches=2 filed=2 unfiled=0`, exit 0 (also at fbf1ea3c) | `python3 -B census/round-52/c1-counter.py --root LANE --rev FULL40 --scratch DIR` | after: 9c0f1281 (the "round-52: C1 corrections" commit); re-run fbf1ea3c |
| C2 fleet-root census capture verifies | `PRISTINE FAIL FLEET-CENSUS-ABSENT`, exit 1 (controls/c2-control-donothing.txt) | `SUMMARY entries=49 rows=49 unclassified=0 class_mismatch=0 counts=ok tool_sha=ok removal_proposed=0 receipt=ok`, exit 0 (also at fbf1ea3c) | `python3 -B census/round-52/c2-counter.py --root LANE --rev FULL40 --scratch DIR` | after: 8ec412c6 (capture commit); re-run fbf1ea3c |

Coverage, calibration and operability axis scores are unchanged (calibration 7, coverage 8, operability 8); no reproducible 0–10 mapping was asserted (SCORECARD round-52 measurements). No axis is harmed (standing checks above; the r51 counters unchanged).

## Sources & frontier

- corpus/SOURCES.md rows before→after: 198 → 199. Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` at f778b9d1 (198) and at fbf1ea3c (199); conf-form census exit 0 at round end (census-after.txt).
- Rows added by tier: A +1 (S275), B 0, C 0. Tier histogram at base A=189 B=6 C=3; at tip A=190 B=6 C=3 (`awk` over the registry rows at each revision).
- Rows touched old→new: none (no existing status, recheck or used-by changed; S275 is new, status mined).
- Frontier rows advanced: none (the surface is PROVINCE Owns, already Core; no F-row moved; no Core promotion).
- Knowledge: corpus/knowledge/fleet-root-stray-census.md admitted (source S275; verified-at 2026-11-03; recheck commands above). Gate: lesson round-52 `## Gate` (URL, access date, sha256, located quote, admitted/rejected, the reject sweep: none beyond S275).
- Assimilation: none. shokuknow's merge/souji package stays held by the open L0 question on mass id drift (r46); nothing adopted; no shokuknow write or campaign tool run.
- considerthese/: no such directory in this lane — stated.
- Duplicate-URL disclosure: S275 shares its URL with S006 (scope differs; both rows stand); the census's W04 count moved 59 → 60 (warning class).

## Trend verdicts

- expansion: **improved** — one admitted knowledge entry on ground the lane's coverage map did not hold (the fleet-root hygiene surface had no knowledge entry), sourced on an S### row opened this round (S275). Evidence: corpus/knowledge/fleet-root-stray-census.md; SOURCES row S275.
- quality: **improved** — two stale annotations re-verified and filed (C1), with the append-only proof at the tip (L1 tip checks (a′)–(g)); no admitted entry failed a re-check (the r46 suite and the r51 counters are green at the tip). The counter-level limits found by the attacks are named, not hidden (lesson `## Wave findings`).
- discernment: **unchanged** — the non-author spot-check of this round's gate decisions has not run (LEARNING.md: the closure does it). The round added no QUALITY criterion without a lesson behind it. The attacks found counter defects (C1 first-annotation reading, unpinned recompute source; C2 no run binding); these route to the next round's counter amendment, not to a claim of improvement here.

## SHONEN
- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: SKILL.md `## Round 52 contracts` (tool and both counter gates, pinned digests); corpus/SOURCES.md S275 (census/round-52/sources/).
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: LOG.md `## Round 52` (fleet-root capture of 49 entries; C1 filing; standing suite); census/round-52/records/fleet-root-census.tsv.
- [~] Instructions executable by an agent without oral context — pointer: census/round-52/c2-counter.py and c1-counter.py (SUMMARY at the tip, exit 0); tools/souji-fleet-root-census.py --selftest (checks=39 failures=0).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: corpus/lessons/round-52.md `## Wave findings` (connector01 sibling-overlap result: no sibling claims the fleet-root census surface); L0 kumitate-shokinin line in .ufo/l0-questions.md.

## Round shape and seats

- Shape: one v1 wave (`souji-r52-w1`), 13 seats, band 8–16 (`scripts/hyaku/ufo-wave-policy.json`). Planner held by the L1 (not a swarm seat); no residual call; no wave 2 (run-15 shape).
- Seat-role mix: scout 2, connector 1, executor 3, scribe 2, reviewer 2, critic 1, mutation-tester 1, sentinel 1. Attack seats 4 of 13 (reviewer ×2, critic, mutation-tester; 31%, ≥25%). Connectors 1 (≤2).
- Route map (routes are never passed as a model argument): m_flash — scout ×2, executor ×3, mutation-tester ×1; m_mim — connector, scribe ×2, sentinel; m_zfl — reviewer ×2, critic. The seats' results do not record their answering models; none of the claims depends on one.
- Dead seats: none. 13 spawned, 13 settled (WAVE-DONE, results file), 0 dead.
- Residual calls: none.

## Stale-lane, tools, inherited state, erratum

- Stale-lane: none; the mission progressed throughout (commits 5b34efe7, 8ec412c6, 9c0f1281, 049fdc06, fbf1ea3c). The wave waited about 22 minutes for fleet capacity (cap-defer, 36 seats occupied) before spawning.
- Tool installs: none. The round used the installed python3 (3.14.8), git 2.56.0 and curl. pacman was not used (paused host-wide).
- Inherited state: none from r51; the r51 spot-check's routed items were handled (defect 1 by C1; defect 2 named in the lesson; defect 3 a prereg-plan note with no action; defect 4 operator-owned SHONEN).
- Rider note (fleet L0 file): `.ufo/l0-questions.md` carried an uncommitted line from another lane (`kake | round-69`, the offline freshness-sweep question) when this report's L0 append was committed. The fleet-commit helper commits the whole file, so that line rides in this commit; it is not this lane's content and is not reattributed here.
- Erratum (appended; the filed bytes of .ufo/reports/round-51/souji.md are unchanged): the r51 report line 108 states `grep -c "^ADDED" census/round-51/records/ws-drift-vs-r46.tsv` → 78. The recomputed value is 79 (r51 tip e004ee1a and round-52 tip fbf1ea3c); the r51 SUMMARY `added=79` was always correct. Filed by the R52-CORRECTION lines in SCORECARD.md (C1).

## Open items (routed, not closed)

- Counter amendment (next round): C1 counter v2 (one annotation per site; pinned recompute source; inert-correction kill; append-only check across revisions; fence refusal). C2 counter v2 (sort order; `#`-leading names; a run-receipt check). Named limits are in the lesson and SCORECARD.
- Operator rulings (L0): credential-shaped names (refuse vs redact); the derivation of the ignored column (check-ignore vs listing).
- Dated observations (LOG.md:18; corpus/README.md:40) are expired annotations; a census of dated annotations is a candidate next claim.
- The `.omp` name rule has no dedicated control yet (lesson Mistakes row 4).
- Assimilation remains closed (shokuknow L0, r46).

Checklist note: no box is [x] (no non-author verifier has written one).

Verifier note for the closure: the round's discernment spot-check, the independent re-run of both counters at fbf1ea3c, and the attack seats' transcripts are the evidence to re-derive. The lane asserts only what is pointed at above.
