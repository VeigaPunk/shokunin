# kaika W3 — non-author verification: revenger, round 1

Subject: lane `revenger`, steered round 1, round head `19b3174ed` (base `8bbcb4e32`), branch `kaika/round`.
Reviewer: `W3ReviewRevenger` (fresh orchestrator dispatch; not a lane L2).
Scratch: `/tmp/kaika-verify/revenger/{base,head,a7acc20,35b2e8b,src}` from `git -C <worktree> archive <commit> | tar -x`; deleted at end.
Working-tree rule: all commands used absolute paths and the `cwd` parameter (the shell `cd` was unreliable).

## Incident (self-reported)
A `curl` run without an absolute output path wrote five downloaded source files into the fleet root `/home/vgpnk/Projects/shokunin/` (`cftt.html`, `msft-pe.html`, `pycodecs.html`, `swgde-17f002.pdf`, `unicode-ch3.html`; all untracked, created 19:18). I deleted exactly those five with `rm -f`. Afterwards `git -C /home/vgpnk/Projects/shokunin status --short` printed nothing. Re-downloads went to scratch.

## Recommendation (one line)
**Do not admit as declared.** C1 and both C2 counts verify. C3 (freshness) does not verify as a currency gain. The fleet validator exits 1. Admission should wait for the fixes in §Required before admit.

## 1. Provenance — PASS
`git -C <W> log --format='%h %an <%ae> | %cn <%ce> | %s' 8bbcb4e32..19b3174ed` →
- `a7acc20 revenger-shokunin <revenger@shokunin.local> | revenger-shokunin <revenger@shokunin.local> | round-1: quality bar, pre-admission coverage map, mined mistakes`
- `35b2e8b … round-1: ROOT/HIST replay for two PE ledgers, SOURCES registry + 4 gated knowledge entries, readiness re-verification`
- `19b3174 … round-1: record kaika claims, measurements, freshness axis, sources-curation capability`

All three: author and committer `revenger-shokunin <revenger@shokunin.local>`.

## 2. Append-only — PASS
`git -C <W> diff 8bbcb4e32..19b3174ed -- LOG.md corpus/lessons corpus/QUALITY.md | grep -cE '^-[^-]'` → `0`.
Hunks: `LOG.md @@ -762,3 +762,16` (additions only); `corpus/lessons/round-1.md @@ -23,3 +23,111` (base lines 23–25 kept as context, 108 lines added); `corpus/QUALITY.md` is new (base absent).
`corpus/knowledge/seed.md` and `2026-10-12-rea-readiness-checklist.md`: `diff <base> <head> | grep -c '^<'` → `0` each (base bytes contiguous).
`corpus/SOURCES.md` and `corpus/README.md` are new files at this round (no in-place edits). Out of scope but noted: `SCORECARD.md` removes one placeholder table row (`| — none yet — |`) and three sentences when the lane writes its declared values.
`fixtures/` and `live/` are byte-identical base→head: `diff -rq base/corpus/fixtures head/corpus/fixtures && diff -rq base/corpus/live head/corpus/live` → no output.

## 3. Claims — counting commands re-run at each commit

| claim (report row) | command (run at base / a7acc20 / 35b2e8b / head) | before → after (reproduced) | report says | verdict |
|---|---|---|---|---|
| C1 calibration, CALIBRATION | SCORECARD.md:32-43 command C via `python3 -B -c`, cwd = tree root | base `CALIBRATION 2 / 4 score= 5.0`, `REPLAY 8 / 10`; 35b2e8b and head `CALIBRATION 4 / 4 score= 10.0`, `REPLAY 10 / 10` | 2/4→4/4; 8/10→10/10 | **verified** (count). Axis-fit caveat, §6-L5 |
| C2 coverage-K, held rows | `grep -cE '^\| C[0-9]+ .*\| held \|$' corpus/README.md` | a7acc20 `0` (exit 1); 35b2e8b `4`; head `4`; rows = `14` | 0/14→4/14 | **verified** |
| C2 expansion | reconstructed from prose (LOG.md:773): new knowledge files absent at base, whose coverage-map row was uncovered/partial at a7acc20, and whose `source:` S-rows are `mined` with the entry in `used-by` | new: C13 partial, C01 uncovered, C12 partial, C11 uncovered → `EXPANSION uncovered=2 partial=2 total=4` | 0→4 (2+2) | **verified by reconstruction**; the report does not paste the command (§6-M4) |
| C2 capability, 7 census commands | the 7 commands of SOURCES-CONTRACT-v1 §Census on `head/corpus/SOURCES.md` | rows `15`; malformed `0`; tier `A=14 C=1`; status `mined=12 queued=1 rejected=2`; dup / enum / missing-path: no output | "seven commands all run clean" | **verified** for the 7 commands; **not clean** under the fleet validator (§4, H1) |
| C3 freshness, count | `grep -cE '^\| [FK][0-9]+ .*\| (holds\|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md` | base exit 1, `0` / `0`; head `12` / `6` = `18`; `^verified-at: 2026-10-19` head `1` / `1` | "18/18 hold or flagged (10.0)" | count **verified**; the score does not measure currency. **not-verified** as a freshness gain (§6-H2) |
| C3 freshness, "before" 8/18 (4.4) | the same command at base | base returns `0` lines (no tables exist at base) | "base text vs live host 8/18 facts hold (4.4)" | **not-verified** by its stated command (§6-M5). The 8/18 appears only when read off the head table: holds in head = 5 seed (F01, F03, F04, F08, F12) + 3 checklist (K01, K04, K06) = 8 |
| guard F, coverage record families | SCORECARD.md:45-57 command F via `python3 -c`, cwd = tree root | base `COVERAGE 4 / 8 score= 5.0`; head `COVERAGE 4 / 8 score= 5.0` (both families `['native-static','javascript','archives','evm']`) | unchanged | **verified** unchanged |

Other report numbers I checked: `Mistakes` awk over lesson → `20 18 2` (matches); `Gate` awk → `4 4` (matches); `Require/raise counts did not drop`: `verify_icon_languages.py` 32→32, `verify_multi_icon_states.py` 29→29 (`grep -cE 'require\(|raise ' <file>`), matches.

## 4. SOURCES — validator and re-opened rows

`bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/revenger-shokunin`:
```
revenger-shokunin	E09	S008 recheck=—
revenger-shokunin	E09	S012 recheck=—
validate exit=1
```
**Exit 1, not 0.** Contract §Shape (`recheck` bullet): "`recheck` — ISO date or cadence (`90d`, `180d`, `on-release`)." The two rejected rows carry `—`. Required: exit 0.

Re-opened rows (URL fetched by me, or local file):
- **S010** (new tier-A) Unicode 18.0.0 Ch.3, D91: "isolated UTF-16 code units in the range D800..DFFF are ill-formed." **Verbatim.** C10 "shall treat ill-formed code unit sequences as an error condition" **verbatim.** Page meta-revision `b734c94a…` matches the entry.
- **S011** (new tier-A) Python codecs, Error Handlers, surrogatepass row: "Allow encoding and decoding surrogate code point (U+D800 - U+DFFF) as normal code point." **Verbatim** (PDF-style line wrap in HTML text only).
- **S006** (new tier-A) FIPS 180-4 §3 Explanation: "Any change to a message will, with a very high probability, result in a different message digest." **Verbatim.** §6 Applicability: "may be adopted and used by non-Federal Government organizations." **Verbatim.**
- **S005** (new tier-A) SWGDE 17-F-002 §8: "The process of verification might not verify all data as read from the subject media." **Verbatim.** §9 lists "Acquisition details (e.g., type of acquisition, imaging tool and version number)." **Verbatim.**
- **S003** (new tier-A) SWGDE 18-Q-001 §4 General Discussion: "bases its testing baseline recommendations on the function of the tool, not on the tool origin." **Verbatim.** §4: "Testing is not necessarily pass/fail." **Verbatim.** APPENDIX A: "Lab created datasets can be targeted at the parameters most important to the functionality being tested." **Verbatim.**
- **S004** (new tier-A) NIST CFTT overview: "The testing methodology developed by NIST is functionality driven." **Verbatim.**
- **S009** (new tier-A) PE format: "Resources are indexed by a multiple-level binary-sorted tree structure." **Verbatim.** "By convention, however, Windows uses three levels." **Verbatim.**
- **S008** (rejected) RFC 3227 Abstract: "The purpose of this document is to provide System Administrators with guidelines on the collection and archiving of evidence" — **verbatim prefix.** The RFC **does** contain §2.1 "Order of Volatility" — the primitive the row's own flip names (§6-L2).
- **S012** (rejected, tier C) Wikipedia lede: "The PE format supports storing the data required to load and start an operating system process" — **verbatim.** Only the lede mentions "resource management data"; the fetched article text shows no resource-directory section. Consistent with the reject.
- **S013** (own-work) `corpus/live/runs/round-59/inspection.stdout.json`: `'A=\ude00B!'`, `41003d0000de42002100`, `coverage complete, 8 examined, 3 resources`, Evidence `ev_8ab30e1…` — reproduced (see §6 entries). **Verbatim.**

Re-open coverage: web or file sources opened by me: S003, S004, S005, S006, S008, S009, S010, S011, S012 (9 rows, including the rejected S008 and S012); S013 checked from its file. Not opened by me: S001, S002, S007, S014, S015 (repo, own-work, docs or queued rows).

## 5. Discernment spot-check (LEARNING.md)

| sample | gate decision | my decision | agree / disagree | reason |
|---|---|---|---|---|
| `corpus/knowledge/utf16-unpaired-surrogates-in-resource-names.md` | admit | admit | **agree** | Every load-bearing value reproduces from bytes/spec: `bytes.fromhex('41003d0000de42002100').decode('utf-16-le')` → `UnicodeDecodeError … position 4-5: illegal encoding`; `…'surrogatepass')` → `'A=\ude00B!'` (Python 3.14.7); byte diff pe-r55 vs pe-r59 → `[(741, '0xd8', '0x0')]`; unit list `['0041','003D','DE00','0042','0021']`; D91 verbatim (§4 S010). Limits and unknowns are stated. |
| `long-term-fixity-evidence-records` (ART candidate, `corpus/lessons/round-1.md` Gate table) | reject (Q01: RFC 4998 not opened) | reject | **agree** | Q01 is decisive: nothing tier-A was opened. I would not endorse the second reason ("no lane need shown") unqualified: C13 (`corpus/README.md`) is the fixity/provenance row and is `held` in the head, so the need question is judgment, not a fact. |
| S008 RFC 3227 (source row, rejected) | reject: "predates current device-specific acquisition guidance" | reject, with a record defect | **agree on outcome, disagree on record** | The stated flip — "an entry needs its volatility-ordering primitive specifically" — is met by RFC 3227 §2.1 "Order of Volatility," which the row does not disclose. The reject is still correct while no entry needs ordering; the row should say so. |
| S012 Wikipedia (source row, rejected) | reject, tier C | reject | **agree** | Community tier, never A (contract §Shape). Lede-only mention of resource data. |

Spot-check size is thin: 1 admit, 1 knowledge reject, 2 source rejects. Discernment is supported on this sample, not beyond it.

## 6. Knowledge entries (new in this round)

- Header trio present in all four new entries (`source:` / `verified-at: 2026-10-19` / `recheck:`), plus `coverage-map:`. Entries: `pe-resource-directory-layout.md`, `utf16-unpaired-surrogates-in-resource-names.md`, `digest-scope-versus-provenance.md`, `tool-validation-by-function-and-version.md`.
- Recheck commands run:
  - PE layout `## Reproduce` block (extracted, `python3 -B`): `resource dir rva=8192 size=240 file_base=512`; six tables `dir@file512 named=0 ids=2` … `dir@file648 named=0 ids=1`; data at 672/688/704; `STR@file736 len=5 raw=41003dd800de42002100` → `A😀B!`; payload sha `d7aaca7b…` matches entry.
  - UTF-16 recheck: prints `0 41003d0000de42002100`, then the `UnicodeDecodeError` the entry states.
  - Digest recheck: `sha256sum corpus/live/runs/round-35/inspection.json` → `74a45d0c…`; receipt `output_sha256` → `8c8d96db…`. Both as stated.
  - Tool-validation: `python3 -c … corpus/live/runs/round-7/comparison.json` → `15 0`; `python3 -B corpus/verify_js_graph_delta.py --self-test` → `POSITIVE … removed checksum 1/1`, `NEGATIVE REJECTED`, exit 0. **Not done by me:** the SWGDE current-revision check the entry's recheck also names.
- Claims versus sources: every quote in §4 matches; the S013-based claims match the saved record.
- **Q11 not applied (M1).** Q11 (`corpus/QUALITY.md`, "Supersedes Q08") was added because the critic found entries without in-entry derivations. None of the four entries mentions Q11 (`grep -c Q11` → 0 each). Each carries a 10-row Q01–Q10 table, and the pe-resource table still rests on Q08.
- **Freshness entries (`seed.md`, checklist):** the probes I re-ran agree with the table on every fact except the two noted below. Verified: `command -v rea` → exit 1; `jadx --version` → `1.5.6`; `binwalk --version` → `binwalk 3.1.0`; `unblob --version` → `26.6.4`; `python3 -c 'import pwn'` → `ModuleNotFoundError`; `command -v ghidra`/`ida` → exit 1; skill frontmatter `version: "42"`, `tool_count: 207`; `npx …rea-agents@6.7.0` in SKILL.md; `~/.omp/agent/mcp.json` key `rea` → `rea-agents@6.5.0`; `npm view rea-agents version` → `6.7.0`.
  - Node: bash `node --version` → `v24.21.0` (matches entry); a Python subprocess on this host returned `v26.12.0`, because the resolved `node` is shell-dependent (fnm/mise multishells). The entry records no resolved path (§6-L1).

## 7. Credentials — PASS
`git -C <W> diff 8bbcb4e32..19b3174ed | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'` → no output (exit 1).

## 8. Report — `…/fleet-ledger/.ufo/reports/round-1/revenger.md`
- Required sections present in order: Work performed, Landed changes, Before → after measurements, SHONEN, Sources & frontier, Mistakes, Trend verdicts, L0 questions, Integrator notes. Cites round commit `19b3174`.
- No `[x]` anywhere; SHONEN boxes are `[ ]`/`[~]` and match `SHONEN.md` (unchanged since base).
- Work-performed second bullet says "The RevScribe L2 pointer audit … found 4 defective pointers, all fixed before commit." **Not true** for M14 (§6-M3).

## 9. Per-axis recommended verdicts (every axis the lane scores)

| axis / criterion | recommended | evidence |
|---|---|---|
| calibration — saved-ledger runnability (C1) | **improved** (narrow) | §3 C1 rows: 2/4→4/4 and 8/10→10/10 reproduced. Its counts measure replay pass rate of the lane's own verifiers after a relocation edit, not self-assessment quality (§6-L5). |
| coverage — knowledge-map ground K (C2) | **improved** | §3 K: 0→4 of 14 reproduced. |
| coverage — record presence F | **unchanged** | §3 guard F: 4/8 both. |
| freshness — re-verification currency (adopted) | **not-verified** | §3 C3: the score counts `STALE` as passing (10.0 = holds + flagged). On a currency reading (holds/facts) the figure is 8/18 before and after. Flagging is real labeling work, but it is not a currency gain (§6-H2). |
| depth (retired guardrail) | unchanged (retired) | SCORECARD retirement line. |
| adjacency | unchanged | Not measured. |

## 10. Trend verdicts (LEARNING.md)
- **Expansion: improved.** Evidence: §3 expansion (2 uncovered + 2 partial = 4, reproduced); each cites `mined` rows whose `used-by` lists it (checked). Caveat: Q11 not applied (§6-M1).
- **Quality: improved, with a caveat.** Evidence: every recheck runs; no admitted entry fails a recheck; the 10 STALE facts carry current values. Caveats: F03 (§6-M2) and the node probe (§6-L1).
- **Discernment: improved, thin sample.** Evidence: §5 — agree on the admit, the knowledge reject and both source rejects.

## Defects by severity (cited elsewhere as §6-<ID>)

**High**
- **H1 — Validator exits 1; capability row says "clean".** §4 `validate` exit 1 with E09 on S008 and S012 (`recheck=—`), contrary to contract §Shape (`recheck` bullet). The SCORECARD capabilities row says the census commands "all run clean"; the seven contract commands do, but the fleet validator does not. Fix: give the two rejected rows a contract-conformant recheck (`on-release` or a cadence), re-run `validate` to exit 0.
- **H2 — Freshness is scored by label, not currency.** §3 C3: `grep` counts `holds|STALE` alike, so 10.0 = 18/18 "hold or flagged"; the "before" is 8/18 holds. The improvement measured is flagging, while the body still holds 10 stale facts. Fix: score currency as holds/facts (8/18 → 4.4, unchanged) and report flagging separately, or withdraw freshness as a scored axis.

**Medium**
- **M1 — Q11 not applied in the four entries.** §6: no `Q11` in any entry; entries carry a Q01–Q10 table, and the pe-resource table still cites Q08 (superseded by Q11). `corpus/README.md:9` says "Q01–Q10". Fix: add a Q11 row to each entry's QUALITY table and update the README index.
- **M2 — Freshness verdict contradicts the scout on F03.** Scout (`.ufo/waves/kaika-r1/scout-freshness.md`, row 3, "References list") gives `STALE`: "the six recorded canonical docs remain; five `.rea.backup` files are also present." Lane `seed.md` row F03 says `holds (names); content revised`. "0 left unmarked" is contestable. Fix: reconcile the verdict or record why it is holds.
- **M3 — "4 defective pointers, all fixed" is false.** Scribe audit (`.ufo/waves/kaika-r1/scribe-pointer-audit.md`, tally line 100: 2 line-off, 2 wrong). Head `corpus/lessons/round-1.md` M14 still cites `SCORECARD.md:9,20-21`; the scribe's corrected pointer is `SCORECARD.md:9,19-20`. M07 is fixed; M19 partly (the pointer now carries `seed.md:5`). Fix: apply the M14 correction and correct the report's claim.
- **M4 — Expansion counting command not in the report.** LOG.md:773 and the report describe the expansion script in prose only. I reproduced it from the prose (§3). Fix: paste the script into the report and the lane's LOG.
- **M5 — C3 "before" not reproducible by its stated command.** The stated `grep` returns 0 lines at base (no tables there). The 8/18 is a read-off of the head table. Fix: state how the base value was derived, or measure it from base text against a recorded probe table.

**Low**
- **L1 — Node probe depends on the shell.** `node --version` → `v24.21.0` in bash, `v26.12.0` in a Python subprocess on the same host (fnm/mise multishells). The entry does not record the resolved binary. Fix: record `command -v node` in the recheck or drop the version claim.
- **L2 — S008 row omits the primitive its own flip names.** RFC 3227 §2.1 "Order of Volatility" exists (fetched). Fix: state it in `teaches`.
- **L3 — Own-work tier A on logs.** S014 (`LOG.md`) and S015 (the round lesson) are tier A. Contract §Shape defines A's own-work case as "the lane's own re-runnable gate output"; a log is a record, not re-runnable output. Fix: downgrade to B or document why they count as gate output.
- **L4 — Absolute path embedded in a verifier.** `corpus/verify_icon_languages.py` and `verify_multi_icon_states.py` now define `HIST=/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus` (never read; identity only). It is pinned, so the replay is host-layout-dependent for identity. Disclose in the report.
- **L5 — Calibration axis-fit.** The C1 proxy is the replay pass count of the lane's own verifiers after the path edit. The edit is a stricter receipt check plus an exact-equality artifact check against a pinned literal (diff at `corpus/verify_*_states.py`, lines ~8–10, 121–145). It is an honest runnability gain, not a self-assessment measure; the operator should decide whether it moves the calibration axis.
- **L6 — README index stale.** `corpus/README.md:9` says Q01–Q10 (see M1).
- **L7 — Verification gap (mine).** The tool-validation recheck's SWGDE revision check was not performed.

## Required before admit
1. H1: fix the two `recheck` cells; `validate` exit 0 (paste output).
2. H2: restate freshness as currency (holds/facts) or withdraw it as a scored axis; keep flag counts as a separate note.
3. M1, L6: Q11 rows in the four entries; README index to Q01–Q11.
4. M3: apply the M14 pointer correction; correct the "all fixed" sentence.
5. M2, M4, M5: reconcile F03; paste the expansion command; state how the freshness "before" was derived.
6. Then re-admit: C1, C2-K, C2-expansion, and capability (after item 1). Freshness stays not-verified until item 2.

## Appendix — commands used (condensed)
- Snapshots: `git -C <W> archive <commit> | tar -x -C /tmp/kaika-verify/revenger/<dir>`.
- C1: SCORECARD.md:32-43 command C, `python3 -B -c …`, cwd per tree.
- K: `grep -cE '^\| C[0-9]+ .*\| held \|$' corpus/README.md`.
- Census: seven commands from SOURCES-CONTRACT-v1 §Census.
- Validate: `bash …/sources-census.sh validate <W>`.
- Freshness: `grep -cE '^\| [FK][0-9]+ .*\| (holds|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md`.
- Expansion: reconstruction from LOG.md:773 prose, with `a7acc20` statuses.
- Credentials: grep from the brief, no output.
- Append-only: `git diff 8bbcb4e32..19b3174ed -- LOG.md corpus/lessons corpus/QUALITY.md | grep -cE '^-[^-]'` → 0.
