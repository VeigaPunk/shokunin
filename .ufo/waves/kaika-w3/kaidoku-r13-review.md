# Review — kaidoku r13 source-curation capability (non-author verification)

Reviewer: KaidokuR13Review · 2026-10-19 · read-only (no edits, no commits; scratch `/tmp/kaika-verify/kaidoku-r13-review`)
Target: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kaidoku-shokunin` @ r13 head `5ac7860730e7be7156b1a71f590d50261fb14e63`, previous integrated r12 head `1170f71`
Report under review: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-ledger/.ufo/reports/round-13/kaidoku.md`
Contract: `fleet-ledger/CORPUS.md` §“SOURCES.md — where a shokunin learns” (Contract v1, frozen)

**Recommendation: accept as a capability-only round; conformant with two minor citation-fidelity defects (S017, S018) and one minor out-of-scope hygiene residue that need follow-up; no blocking defect. No ARM64X claim, no numeric score change, no knowledge expansion was found.**

---

## 1. Lane identity and diff shape — verified

```text
$ git -C <lane> log --format='%H %ae %an %s' -3
5ac7860730e7be7156b1a71f590d50261fb14e63 kaidoku@shokunin.local kaidoku-shokunin ... kaidoku-shokunin: arc3-loop1-round13 source registry
1170f717c4ffeb3d0a9fd24522d8fb42f78fa837 protocol@shokunin.local protocol-shokunin ... round-12 verifier spot-check (integrator, kaika) ...
2a0d6c19840dbc30728c2ca2a061e25c12ade8cb kaidoku@shokunin.local kaidoku-shokunin ... round-12: records ...

$ git -C <lane> diff 1170f71..5ac7860 --numstat
33 0 LOG.md
38 0 SCORECARD.md
2  0 SKILL.md
2  0 corpus/QUALITY.md
50 0 corpus/SOURCES.md
59 0 corpus/lessons/round-13.md
```

- Author/committer is the lane identity `kaidoku-shokunin <kaidoku@shokunin.local>`; parent is the stated integrated r12 head `1170f71`; worktree clean (`git status --porcelain` empty).
- Diff is **184 insertions, 0 deletions** across exactly the six files the report names. Old corpus/LOG are append-only (numstat zeros); `corpus/README.md` and `PROVINCE.md` intentionally untouched (not in diff).
- `git show 1170f71:corpus/SOURCES.md` → **absent** at r12 (new file, so “rows touched old→new: 0” is trivially consistent).
- No push: `git branch -r --contains 5ac7860` prints nothing; `kaika/round` has no upstream.
- Report disposition: `git -C fleet-ledger status --porcelain` → `?? .ufo/reports/round-13/kaidoku.md` (intentionally uncommitted, as stated). No routing/config/UFO files in the diff; `resume_continuity_v1`/rerouting checks are N/A — this round adds a corpus registry only.

## 2. Claim measured before → after — reproduced exactly

After (report’s exact command, rerun byte-for-byte; lane root = root arg):

```text
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --root <lane> <lane>
kaidoku-shokunin	rows	22
kaidoku-shokunin	tier.A	20
kaidoku-shokunin	tier.B	1
kaidoku-shokunin	tier.C	1
kaidoku-shokunin	status.mined	21
kaidoku-shokunin	status.rejected	1
FLEET	rows	22
FLEET	tier.A	20
FLEET	tier.B	1
FLEET	tier.C	1
FLEET	tier.invalid	0
FLEET	status.queued	0
FLEET	status.mined	21
FLEET	status.rejected	1
FLEET	status.invalid	0
FLEET	missing	0
exit=0
```

Before (non-author reproduction: a lane-shaped root with `corpus/README.md` but no `SOURCES.md`; same script):

```text
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --root /tmp/kaika-verify/kaidoku-r13-review/before /tmp/kaika-verify/kaidoku-r13-review/before/kaidoku-shokunin
kaidoku-shokunin	missing	.../before/kaidoku-shokunin/corpus/SOURCES.md
FLEET	rows	0
FLEET	...	0 (all)
FLEET	missing	1
exit=1
```

This matches the lesson’s recorded before-state (“registry missing, FLEET.rows=0, exit 1”) and the after-state verbatim; the report’s “0 → 22” count is from the existing fleet script, not a second validator.

## 3. Registry conformance (independent of the fleet script)

```text
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md   → 22
$ awk …'NF!=13'… corpus/SOURCES.md                                        → malformed=0
tier histogram  → tier.A=20 tier.B=1 tier.C=1
status histogram → status.mined=21 status.rejected=1
duplicate ids   → (empty)
mined used-by disk check (contract snippet) → (empty; all 22 used-by = corpus/lessons/round-13.md, which exists)
$ bash …/sources-census.sh validate --root <lane> <lane> → kaidoku-shokunin	ok	…/corpus/SOURCES.md ; exit=0
```

- 11-column Contract v1 header (`| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`), one Registry table; 22 S-rows only inside it; distinct ids; status/kind/tier enums clean; `community` never tier A (`B`=S016 blog, `C`=S022).
- All rows carry `opened = 2026-10-19`; recheck cadences are ISO-date/`NNd`/`on-release`; no credential-ish strings (`grep -nE 'op://|secret|token|cookie|bearer '` → empty).
- `## Paths` (5 ordered study sequences with why-this-order prose), `## Search log` (internally consistent: 5 screened = 1 included + 4 excluded; query/reasons/stop rationale present), `## Leads (unopened)` separated from rows (SoK, LLM4Decompile, GoReSym releases, Electron 42/14.8 `.jsc` route, later Ghidra notes / operator-gated providers).
- QUALITY.md pointer is a single appended line (Contract v1 “QUALITY.md points here”); SKILL.md pointer is a single appended block; both inside the 6-file diff.

## 4. Quote/anchor audit — all 22 rows reopened (2026-10-19)

Method: fresh fetch/read of every row’s source (local files re-read; `Base-src.zip` entries re-extracted; web sources reopened live), then word-for-word comparison with the lesson `## Gate` table; quote word counts checked programmatically (`over_25: []`).

**20/22 verbatim-exact** (allowing only stripped markdown backticks/bold and mid-sentence substring starts): S001, S002 (sentence wraps lines 47–48 in `native-and-artifacts.md`, section `Recorded Linux crashes` L41), S003 (`SUPPORTED_VERSIONS = GoVerRange.parse("1.15-1.25");` at `GoRttiMapper.java:79`; zip SHA-256 `f00d29c2…` re-verified; second anchor `GoApiSnapshot.java:get` exists — `public static GoApiSnapshot get(GoVer,…)` L102), S004 (title “GP-6528 add support for golang 1.26”; compare API `385e8cd…master` → `status=ahead`, merge-base = the commit ⇒ reachable from master), S005, S006 (quote at line 19, within cited window), S007 (line 1), S008, S009 (pp. 23250–23267), S010 (pp. 11498–11516), S011, S012 (docs `meta-docs-sha 60169b45…` matched), S013 (`"load_browser_process_specific_v8_snapshot": "0",` in v44.9.0 `fuses.json5`, `_version: 1`), S014 (`meta-docs-sha` matched; `Version support`), S015 (quote in `details`; prose “36.8.1” vs `extracted_events` fixed `36.8.0` discrepancy reproduced as recorded), S016 (section `From frozen pizza to unsigned code execution`, 2025-09-03), S019 (`Parsing Improvements`, 2025-02-16), S020 (`dyld extract`), S021 (`Function Selector`), S022 (quote + both rejection facts; see §5).

**DEFECT-1 — S017 quote is a splice, not a verbatim sentence (minor–moderate; citation fidelity).**
Lesson Gate prints: “Use --normalize to replace address-derived function names with deterministic names based on parse order.”
The repo has exactly one README at the pinned commit `ef39099b…` (GitHub tree API: `README.md`, sha `2a0c5a60…`). The two nearest sentences are:
- CLI table: “Replace address-derived function identifiers with deterministic names based on parse order.”
- Section `Deterministic Function Names and Mapping CSV`: “Use `--normalize` to replace address-derived function names with deterministic identifiers.”
The printed “quote” is the section prefix combined with the CLI bullet’s tail, swapping names/identifiers; it exists verbatim nowhere. `teaches` is substantively supported, but a Gate whose function is verbatim quotability (Contract v1 rule 1; CORPUS.md “a quote names its location”) should not publish a spliced quote. **Fix: quote either verbatim sentence and cite that exact location** (recommend the CLI bullet, since it carries the “based on parse order” claim).

**DEFECT-2 — S018 quote is verbatim but mislocated (minor).**
Quote “The goal is not perfect source recovery — V8 compilation is lossy, and the output of decompilation remains pseudocode.” appears once, at page line 87 under `# Introduction` (heading L77). The lesson cites `Decompiled output`, whose heading is at L151 and opens differently. **Fix: relabel the location as `Introduction`** (the row’s `Analysis methodology`/`Decompiled output` anchor topics are otherwise fine).

Cosmetic: S006 line window is “15–20” in the lesson vs “15–22” in SOURCES.md; the quoted line (19) lies inside both — no action needed beyond consistency.

## 5. Admit/reject non-author taste spot-check (reasons)

Admits reviewed with reasons (representative, beyond the ≥3-source requirement):
- **S012/S013/S014 (tier A)** — official Electron docs and a tag-pinned schema; appropriate A (official docs / upstream source), and each row explicitly bounds scope (“this describes ASAR, not every code-bearing file”; “pin a concrete release instead of generalizing”). Both docs pages’ `meta-docs-sha` matched the recorded hash today.
- **S019 (tier A, docs)** — LIEF maintainer’s own post; maintainer statement = A per contract; the row’s caveat (“it says nothing about Ghidra or REA holding a carrier”) correctly refuses to upgrade documentation to held capability.
- **S016 (tier B, community)** — expert disclosure with reproducible detail; contract forbids A for `community`, and B is the right call.
- **S021 (tier A, spec)** — normative Solidity ABI spec; scope (“not selector-name resolution”) correctly excludes the signature-database step.
Reject reviewed:
- **S022 (tier C, community, status `rejected`)** — page verified: “You upload a `.jsc` file through the browser, and it returns decompiled JavaScript.” (`JSC Decompiler`); coverage claim “Electron 17 through Electron 38” verified in body and the feature table; published 2026-03-11 verified. Rejection reason (browser upload conflicts with local-artifact custody; coverage misses the lane’s Electron 42/V8 14.8 frontier) **holds on the evidence**, and the recorded flip (“verifiable local/no-upload workflow + reproducible Electron 42/V8 14.8 coverage”) is a concrete, checkable condition. I concur with the rejection and with the C tier.

Overall taste verdict: tiers are scope-bound (not global), no row inflates a source into host capability, and the rejection is retained with evidence — conformant with Contract v1 rules 1/2/4/5.

## 6. Gate / smoke results (report commands rerun; no REA target, no binary execution)

```text
$ python3 <lane>/.ufo/gates/c1-census-v10.py --root <lane>
PROVINCE.md lines=162 loci=6 · SCORECARD.md lines=2160 loci=12 · SKILL.md lines=451 loci=2
STALE 0 · AMBIGUOUS 0 · UNDECLARED 0 · UNRESOLVED 0
SCOPE-ERRORS [] · FRONTIER register (G21): 14 rows asserted, errors: []
UNREADABLE [] · G2 ok (20/19/3; floor 1/file) · G7 [] · G11 [] · DECLARED FAIL CLASSES []
VERDICT: PASS  (exit=0)

$ python3 <lane>/.ufo/gates/citation-drift/citation-drift-probe.py --root <lane> --rev HEAD --strict
CITATION_DRIFT_VERDICT: clean findings=0 exit=0

$ python3 …/citation-drift-probe.py --selftest              → CITATION_DRIFT_SELFTEST: CLEAN cases=13 passed=13 failed=0 exit=0
$ python3 <lane>/.ufo/gates/custody-pair/custody-pair.py selftest
  scratch: /dev/shm/custody-pair-selftest-o8imvj3m
CUSTODY_PAIR_SELFTEST: CLEAN cases=28 passed=28 failed=0 exit=0
```

The report’s quoted decisive lines match these reruns line-for-line (report omits the HISTORICAL/INFO sections, which do not affect the verdict). My custody selftest run created one `/dev/shm` fixture; I removed exactly it (`rm -rf /dev/shm/custody-pair-selftest-o8imvj3m`; count returned to 151; `/tmp` count 0).

## 7. ARM64X / numeric / knowledge checks — verified negative

- `git grep -i arm64x 5ac7860` over the diff paths: only disclaimers (“no ARM64X carrier… not pursued under this steer”, S019 scoped to LIEF, the path note “does not claim Ghidra/REA ARM64X support”) plus pre-existing `corpus/README.md`/`knowledge` text. **No new ARM64X claim.**
- SCORECARD/LOG/SKILL/QUALITY/SOURCES/lesson changes are pure appends; the appended SCORECARD section states “no owned score was changed” and its axis table is “unchanged” throughout. **No numeric score inflation.**
- No `corpus/knowledge/` entry added; registry is framed and counted as capability, not knowledge. **No expansion-as-rows inflation.** The report’s “no outside admit/reject spot-check claimed by the lane” honesty statement is correct — L2 reviewers are lane-dispatched, and this review is independent of the lane.

## 8. Findings

1. **[Minor–moderate] S017 Gate quote is a splice** of two README sentences; not verbatim (evidence in §4). Fix before integrating the registry as citation-grade.
2. **[Minor] S018 Gate quote location mislabeled** (`Decompiled output` vs actual `Introduction`, page L87). Fix the label.
3. **[Minor, hygiene] Main-repo checkout is dirty**: `git -C /home/vgpnk/Projects/shokunin status --porcelain` → ` M LOG.md`; the diff is exactly **+1 blank line at EOF** (index `06fdeca`); mtime `2026-10-19 20:27:39`, inside this lane’s r13 window, and the lesson’s Mistake #2 describes an accidental append to exactly this path. The kaidoku block content is absent (no `arc3-loop1-round13` anywhere in that file — grep clean), so the removal took out the block but left a trailing-newline residue; “removed exactly the appended block” is therefore not byte-exact, and the steer’s read-only main checkout is still dirty. I made no edits; ask the operator to `git restore LOG.md` (or the lane to drop the stray line) before closure.
4. **[Cosmetic] S006 line-window mismatch** between lesson (15–20) and SOURCES.md (15–22); quote at L19 is inside both.

## 9. Residual risk and verification gaps

- **Search-log counts are not reproducible today.** Rerunning the recorded query through the current `web_search` returned a synthesized brief, not a 10-URL list; only the S008 paper resurfaced (and “GP-6528” was not surfaced at all). The bounded-search note preserves query, counts, exclusions and stop rationale as the contract requires, but its “identified 10 / screened 5” numbers cannot be independently re-counted from here — treat as recorded-not-reproduced.
- **L2 narrative unverifiable from the repo**: “eight leaf seats in one batched `functions.task` call, no per-lane model key” is process narrative; the diff shows only that no L2 file edits landed (consistent with it).
- **No push** is evidenced by absence of any remote-tracking ref containing HEAD and no upstream on `kaika/round`, but a push to an unobserved ref cannot be excluded cryptographically.
- **/dev/shm population**: 151 `custody-pair-selftest-*` fixtures from other lanes remain fleet-wide (latest mtime 19:02, before this lane’s 19:07–20:33 window); no in-window fixture remains, so the lane’s own-cleanup claim is consistent but its single removed directory is not individually provable.
- GP-6528 is confirmed reachable from master; the installed 12.1.4 source (zip entry dated 2026-09-21) still gates `1.15-1.25`, which is exactly the installed-vs-upstream framing the row uses — no overclaim found there.
- Every source fetch in this review was live on 2026-10-19; the Electron docs pages still carry `meta-docs-sha 60169b45…` matching the registry.

## 10. Limits of this review

Read-only: no lane file, fleet file, or main checkout file was modified; nothing committed; no REA target, binary, sample, ARM64X carrier, or live REA session was opened (only the two existing gate scripts and their selftests were run, plus read-only git/awk/python and source reopens). Scratch: `/tmp/kaika-verify/kaidoku-r13-review` (the before-state simulation root lives there). This review does not adjudicate outside of the r13 capability claim; the r12 claims remain frozen per steer.