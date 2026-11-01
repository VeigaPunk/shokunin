# revenger — round 74 report (hyaku run 13, fresh start, new Windows host)

Lane repo: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/shokunin-binary-forensics`, branch `main`.
Base: `85db6abefae7b706cf5583ab24eefbcbd28a4f01` (the inherited r74 freeze; both frozen instruments sha-verified byte-unchanged: `corpus/audit_source_quotes.py` `72c6938a…8743f`, `reports/round-74/measure.py` `ff2e52bd…4ea6`).
Final lane tip: `bbbce158035f8295344a3af5eea4b15e850cb12e`; `git ls-remote origin refs/heads/main` returns the same hash.

## Work performed

Fresh-start disposition first (§7 ruling): the last three rejected closures (r71, r72, r73) all died on claims whose verification needed the wave/Q-review surface that never settled. I read all three reports plus the outside `corpus/lessons/round-73-verifier-spotcheck.md` and spot-checked the inherited freeze at `85db6ab`. **Ruled out: the inherited freeze's C1 (carry the r73 C10 admission and land 4 wave-vote files).** On this host the required review cannot exist — there is no `.ufo/state/` dispatcher and no seat-spawn handoff (`ls /home/vgpnk` → ENOENT), so a do-nothing control reaches the identical outcome; instead the freeze's own frozen kill rule was executed as disposition work (below). **Declared claims: C1 coverage, C2 calibration** — distinct axes, causally separable, each with its own counting command.

- **C1 (coverage — lowest active axis, K 8/15 = 5.3) — new bounded criterion P, province surface accuracy.** New probe `reports/round-74/province_probe.sh` checks all 11 surfaces PROVINCE.md names: present-by-probe or dated-absent-record. Red-before `province-before.log`: exit 1, `RESOLVED=4/11 UNRECORDED_ABSENT=7 P_SCORE=3.6`. PROVINCE.md corrected to this host (§6 absent-surface rule): REA skill dir absent (packaged `rea` CLI present at 6.8.0, `rea --version` exit 0), ghidra/ida/jadx/binwalk-unblob/pwntools absent (PATH/import probes), `~/Projects/gamez/research/` absent, write scope renamed to `fleet/shokunin-binary-forensics`. After `province-after.log`: exit 0, `11/11 / 0 / 10.0`. Boundary stated in SCORECARD: K and F unchanged; instrument-level coverage only, no admission claimed.
- **C2 (calibration — the inherited frozen QA criterion, the r73 spot-check carry-forward #3): source-registry quote fidelity, executed at full scale.** 51 fetch receipts + 51 raw bodies committed at `.ufo/waves/round-74/quote-audit/` (105 files with the 3 pre-derivation origs). 10 of the 42 range quotes were not verbatim in fetchable bytes: 2 real misquotes (S062 — "hexadecimal editor" belongs to the preceding radare2 sentence; S068 — reordered dnSpyEx wording), 1 inserted word (S094 "The"), 2 early sentence-ends (S063, S080), 5 representation-only drifts (S057, S058, S066, S084, S088, S095 class), plus markup-interrupted S115/S131 and the S380 revision drift (portal replaced APM rev 4.10 with rev 4.11 on 2026-10-29). All corrections landed ONLY as superseding rows S429–S442 opened this round; S062/S068/S094 flipped `mined`→`rejected` with located-quote reasons naming successors (Q12); S343 re-opened at the reposiTUm record its own anchor names; S379/S381/S400 verified via derived/snapshot representations with named derivations. Disclosure: no seat surface exists on this host, so the receipts are L1-authored (`seat: revenger-r74-L1 (no seat surface on this host…)`); every verdict is mechanically re-derivable from committed bytes via the unchanged frozen counter, whose negative control (S071's drift quote absent from the S427 body) passes.
- **C10 disposition (frozen kill rule, not a claim):** counter `reports/round-73/measure.py` (byte-unchanged) over an archive of base `85db6ab`: `C10_CANDIDATE_PIN=1/1`, `C10_SOURCES=1/1`, `C10_Q_VOTES=0/16`, `C10_HELD_BACKED=0/1`, exit 0 (`reports/round-74/c10-disposition.log`). Required review unavailable → per `reports/round-73/claims.md` the candidate's `admission-status:` flipped `candidate` → `rejected` (single line); README C10 stays `partial`; no repair-and-revote.
- **Frontier step (§2b):** census validate run at round start and round end (below); mistake mining landed 5 classes in `corpus/lessons/round-74.md`; C2 rests on S429–S442, rows opened this round.
- **L0 filed:** no L2/AgentSwarm dispatch surface on this host — MISSION's ≥8-L2 floor is not executable here; routed around, never treated as answered (`.ufo/l0-questions.md`, appended; tabi r44 and kake r65 already carry the same class of question).

## Landed changes

Every item is in the round-74 `LOG.md` entry; all commits are helper-built and pushed.

- `c9f490c` — work commit: PROVINCE.md corrections, SOURCES.md S429–S442 + 3 Q12 rejections, C10 candidate status flip, round-74 lesson, SCORECARD, LOG. **Defect, self-caught and repaired:** I passed directories to treecommit, whose paths are files — the commit deleted the three frozen instruments from the tree and landed none of the receipts; found by the mandated `git diff 85db6ab..c9f490c --stat`, mined as a lesson Mistake, repaired append-only.
- `704be4d` — repair: all 111 files re-listed explicitly (frozen instruments restored; 51 receipts + bodies + 3 origs landed).
- `e302492` — receipts: `reports/round-74/measure-after.log` (counter at `704be4d`), `c10-disposition.log`, `no-harm-diff.txt` (protected corpus paths 0 diff bytes; knowledge/ limited to the single admission-status line); lesson updated.
- `bbbce15` — census receipt `reports/round-74/census-after.log`.

## Before → after measurements

- **C1 (P):** `bash reports/round-74/province_probe.sh` — before `PROVINCE_SURFACES_RESOLVED=4/11 UNRECORDED_ABSENT=7 P_SCORE=3.6`, exit 1 (`province-before.log`) → after `11/11 / 0 / 10.0`, exit 0 (`province-after.log`); measured at `704be4d` bytes (probe unchanged since).
- **C2 (QA):** `PYTHONUTF8=1 python -B reports/round-74/measure.py TREE` over `git archive <commit> corpus .ufo/waves/round-74`. Before (frozen `measure-before.log`, base `c7008577`): `QA_VERIFIED_TOTAL=0/51 QA_UNRESOLVED=51/51 QA_NEGCTRL=n/a QA_TARGET=no`. After: at `704be4d` (`measure-after.log`) and re-confirmed at the final tip `bbbce15`: `QA_VERIFIED=42/42 QA_MANUAL_VERIFIED=9/9 QA_VERIFIED_TOTAL=51/51 QA_UNRESOLVED=0/51 QA_NEGCTRL=pass QA_TARGET=yes`, counter exit 0; instrument self-test `ok (7/7 legs)`, exit 0.
- **Holds:** protected corpus paths (README map, live, fixtures, prior admitted knowledge, r70–r73 lessons) diff empty between `85db6ab` and `704be4d` (`no-harm-diff.txt`, `protected-diff-bytes=0`); knowledge/ changes limited to the one C10 status line; `K_HELD_BACKED=8/15`, `C10_STATUS=partial` re-derived at the final tip (r73 counter over its archive).

## Sources & frontier

Rows before → after: **428 → 442**. Commands: `git show 85db6ab:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` → 428; `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 442. Added S429–S442 (13 tier A, 1 tier A spec correction; all mined, opened this round); S062/S068/S094 → rejected; no other in-place change; supersedes chains `TERMINALS=42/42`.

Census: the contract's literal command `sources-census.sh validate --root <fleet-root> revenger` exits 2 on this host (it expects the old layout `<root>/revenger-shokunin/`); the host-adapted explicit-lane-dir invocation (sanctioned by the script's own explicit-dir target resolution and selftest) is `… sources-census.sh validate --root <fleet-root> <lane-dir>`. Round start: exit 0, 28 W warnings (8 W04, 20 W01), `ok`. Round end: exit 0, 31 W warnings, 0 E (`census-after.log` committed): +W04 S429/S430 (duplicate URL across scopes — inherent to superseding-row corrections, the class the r73 spot-check called inherent), +W01 S437 (tier C mined with used-by).

## Trend verdicts

- **Expansion — unchanged:** no knowledge entry admitted; K `K_HELD_BACKED=8/15` (5.3) unchanged; C05 uncovered, C10 partial (candidate now rejected), C15 uncovered; registry growth is not admission (r73 precedent).
- **Quality — unchanged:** no admitted entry was re-checked or strengthened; the 14 registry corrections are frontier/registry fixes per the r73 closure's own classification; criterion QA is an admission-bar instrument, not a depth move.
- **Discernment — unchanged:** no new outside verdict this round; the receipts await the closure judge's re-derivation, and no lane-internal result is counted as outside. The round's self-caught defects (probe arithmetic, helper misuse) are logged, not credited.

## Assimilation

considerthese/ exists (8 files, 2026-10-20 → 2026-10-28). Adopted exactly one: `considerthese/2026-10-28.md` proposal 1 ("Read-only quote-substring sampling of new SOURCES rows") — mined as a bounded procedure in r73 and **implemented this round** as the frozen C2 audit at 51-row scale (receipts + counter + negative control). Proposals 2–5 remain unimplemented (2 and 3 are report-format changes better made with an outside verdict in hand; 4 targets open candidates — C10 was disposed, none open; 5 is the bot's own daily-file hygiene). Assimilation: considerthese 2026-10-28 #1 implemented as C2; shokuknow register unreachable from this host.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — no SKILL byte touched this round; current bytes still have no non-lane re-confirmation (r69 V7 routing stands; `git diff 85db6ab..bbbce15 -- SKILL.md` is empty).
- [~] At least one end-to-end domain task executed and logged in LOG.md — the 51-source quote-fidelity audit executed end-to-end with committed evidence (`LOG.md` round-74 entry; `.ufo/waves/round-74/quote-audit/`; `reports/round-74/measure-after.log`).
- [~] Instructions executable by an agent without oral context — every counting command in this report was executed verbatim on this host with pasted outputs; the frozen instruments run under the documented `PYTHONUTF8=1` host invocation (locale defect mined, zero instrument bytes changed).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md corrected to this host's real surfaces with dated absence records; AMD legal-boilerplate scoping note (S380/S442) restates that product terms are not statements on studying third-party binaries; no other lane's scope absorbed.

**Fresh-start addendum:** claims declared this round are executable to a verdict on this host without the absent wave surface; the carried C10 claim was closed under its frozen kill rule rather than re-declared; no exploratory claim was declared.
