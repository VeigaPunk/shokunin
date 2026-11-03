# souji round 56 — rejected-harmed

## Work performed

Declared claims: **C1 calibration** (lowest non-retired axis, 7), correction-filing counter v5; **C2 coverage** (8), receipt-key counter v5. Operability stays 8; numeric deltas 0, no reproducible score mapping. No exploratory claim or new capability.

- C1 instruments hidden pair filings, the r55 four-space comment-opener regression, NUL correction files and binary numstat finding names; exact form-feed fixture pinned; visible prose-token over-hide repaired. Evidence: `census/round-56/preregistration.txt`, official `c1-matrix-v4.tsv` / `c1-matrix-v5.tsv` under `census/round-56/records/`.
- C2 restores digit/underscore-initial receipt-key detection, refuses unknown empty-value keys, and checks that every expected selftest row ran. Evidence: corresponding C2 matrices and `row-omission-v4.txt` / `row-omission-v5.txt` in that records directory.
- **Admission fails:** reviewer01 B4 (NBSP prefix) and C4 (closed multiline inline comment) hide real correction tokens in independent CommonMark renders; v4 refuses, v5 passes. Finite C1 matrix holds, but calibration is harmed. Frozen bytes remain unchanged. Evidence: `census/round-56/wave/w1/S56reviewer01/S56reviewer01-report.md:17-50` and its reproduction files.
- C2's 75-shape differential found zero narrowing harms, eight repair-direction cases and three relabels. Evidence: `census/round-56/wave/w1/S56reviewer02/S56reviewer02-report.md`.
- One v1 wave, **12 seats**, after validated ready handoff. Main delivered WAVE-DONE before this report. Roles: scout 1, connector 1, executor 2, scribe 1, reviewer 2, critic 1, mutation-tester 2, sentinel 1, revenger 1. Attack share 5/12 (42%); one connector; L1 planner. Round total 12; residual 0; dead seats 0 (all twelve returned outputs). Dispatch/results: `census/round-56/wave/w1-dispatch.json`, `w1-results.json`. The prereg prose role enumeration totals eleven; dispatch/results establish twelve. No model argument passed; host role routing used.
- Mistakes and prevention: QUALITY Q111–Q114, lesson Mistakes and Further mistake tables. The main lesson is that HTML-block start conditions are not a complete inline visibility model. R55 missing LOG tie-ins for f9da665e, 51551399 and 6d8bfb8e appended in LOG Round 56.
- Sentinel found quadratic correction-line processing and terminal-control diagnostic injection (MEDIUM), scratch-symlink and memory limits (LOW). No frozen edits; routed r57 with exact receipts. Mutation: C1 8/10 killed (secondary finding assertion and de-claimed LF parser survive); C2 row-set assertion removal survives ordinary selftest, while actual arm omission is refused. Evidence: the two mutation reports and sentinel report under `census/round-56/wave/w1/`.
- Connector found seven overlapping numstat/append-only surfaces (kaidoku/kama), no C2 grammar overlap. Lane-local evidence, not fleet-first; sibling trees untouched. Revenger classified 41 carried items, with explicit open/r57 list. Their seat reports are in the same committed wave tree.

## Landed changes

All rows tie to `LOG.md ## Round 56` in the lane. Final pushed lane revision: **8c27791a1606cd654b059df6a00f0e031ad6abb8**.

| landed commit | work / LOG tie-in |
|---|---|
| cce21b555a617cadda782613ec1e9d3a0c12ac83 | Freeze: prereg, v5 counters, fixture builder/expected TSVs, pre-freeze controls and dry-run matrices, source capture/Gate/entry; LOG Freeze bullet |
| 148f39a6c902b27e997ac36d395735406d3ad9de | Official matrices/selftests, real-lane receipts, wave spec/dispatch copies, SKILL registry, Q111–Q113, README; LOG Post-freeze evidence bullet |
| 31ef3388a9ab855018c6a5c5ddf8729ffb182300 | Settled wave results and reports, C1 harms, Q114, SCORECARD, source-entry correction, attribution corrections; LOG Integration / Wave settled bullets |
| ff2a3c76a63f14e922817900fb2534a2d392d0bc | Six new abbreviated SCORECARD pointers repaired; red standing measurement preserved, verified final census; LOG Pointer repair bullet |
| 8c27791a1606cd654b059df6a00f0e031ad6abb8 | Terminal standing receipts, r53/r54 receipts, search log and lesson errata; LOG terminal measurement bullet |

No inherited uncommitted lane work at round start. The r55 integrator spot-check was read and left unchanged. No removal/quarantine or new deletion authority; certification OFF, K5 HELD, NAMESPACE/reap holds unchanged.

## Before → after measurements

Both v4 and v5 arms use the same frozen fixture population. Commands run from the lane root:

```sh
awk -F'\t' 'NR>1 && $5==0{n++} END{print n+0}' census/round-56/records/c1-matrix-v4.tsv
awk -F'\t' 'NR>1 && $5==0{n++} END{print n+0}' census/round-56/records/c1-matrix-v5.tsv
# 9 → 7, 33 repository fixtures
awk -F'\t' 'NR>1 && $5==0{n++} END{print n+0}' census/round-56/records/c2-matrix-v4.tsv
awk -F'\t' 'NR>1 && $5==0{n++} END{print n+0}' census/round-56/records/c2-matrix-v5.tsv
# 5 → 2, 16 repository fixtures (+2 selftest-only arms)
```

- **C1:** exactly F24/F26/F28 tighten 0→1; F29 repairs an honest false positive 1→0; F27 names binary numstat refusal; form-feed F7-FF2 retained. Selftest 33/33. Real-lane measurement **cce21b55**: EXIT=0, unfiled=0, pairhidden=0, recomputed=79 (`census/round-56/records/c1-tip.txt`). Full argv in prereg C1. Executor01 independently reproduced and derived T1–T5. This is finite measurement, **not admission**: out-of-fixture B4/C4 harm remains.
- **C2:** exactly FC1/FC2/FC3 tighten 0→1 RECEIPT-UNKNOWN-KEY; thirteen carry-over rows unchanged. Selftest 18/18. Real-lane measurement **cce21b55**: EXIT=0, receipt=ok sorted=ok tool_pin=ok (`census/round-56/records/c2-tip.txt`). Full argv in prereg C2. Row-omission control: v4 cases=14 EXIT=0 → v5 cases=17 SELFTEST-ROW-MISMATCH EXIT=1. Executor02 reproduced.
- Four official TSVs equal pre-freeze dry-run TSVs byte-for-byte; critic's always-zero stub fails the detection conjunction. Controls retain observed-rc:128 rather than EXIT trailers: receipt-format conformance debt, not an invented pass. Quoted matrix exit columns are data, not shell receipt trailers.
- Standing: at final hash **8c27791a**, `python3 -B census/round-46/c1-counter.py --root . --rev 8c27791a1606cd654b059df6a00f0e031ad6abb8 --work <scratch>` printed `assertions=609 mismatches=76 registered=76 corrected=0 exempted=0 unfiled=0`, EXIT=0. Same result measured at **ff2a3c76** in committed `landing-suite-final.txt`. r53/r54 C1/C2 at ff2a3c76 all EXIT=0 (four named records). Earlier usage-error, dirty-tree, and six-unfiled-pointer receipts remain separately preserved; none is called green.

## Sources & frontier

Before/after literal command:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji
# before: souji ok …/souji-shokunin/corpus/SOURCES.md; EXIT=0 (61 W04 warnings)
# after:  souji ok …/souji-shokunin/corpus/SOURCES.md; EXIT=0 (same 61 W04)
grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
# 202 → 202
```

Evidence: `census/round-56/records/census-before-receipt.txt`, `sources-census-before.txt`, `sources-census-after.txt`, `census-after-receipt.txt`; both digest-bound receipts verify. Final literal command re-run at 8c27791a also EXIT=0.

Rows added: A=0, B=0, C=0. **S277 reopened this round**: HTTP 200, no redirect, 514698 bytes, digest c85f56cc…60f0d; quotes located (19/8 words). Scribe independently re-fetched twice and verified byte equality. C1 cites this sourced basis. S277 used-by old `corpus/knowledge/correction-filing-fence-grammar.md` → adds `corpus/knowledge/correction-filing-html-comment-opener.md`; other cells unchanged. Gate and search log record the change. Entry wording correction appended after the scribe's finding, not silently rewritten.

One admitted entry on existing Core ground, no frontier row advanced, no capability added. No reject candidate opened; no reject sample manufactured. **Assimilation: none** — no considerthese/ directory; shokuknow package held by unanswered r46 mass-id-drift question. Open L0: credential-name refusal/redaction, ignored-column derivation, mass-id drift; prior r55 admission request not assumed answered. No new operator decision needed to report this honest stop.

## Trend verdicts

- **expansion: unchanged** — entry deepens existing correction-filing surface; no frontier promotion or capability.
- **quality: harmed** — B4/C4 are real hidden-filing over-acceptance introduced by C1 opener narrowing. Finite gains do not cancel harm.
- **discernment: unchanged** — lane-dispatched scribe/reviewers are not outside discernment. New admit source verified, no reject sample; outside closure pending. Mistakes are recorded with Q114, not counted as independent approval.

## SHONEN

- [~] Real decision tables, error patterns, checklists, cited sources — SKILL.md Decision tables / Error patterns / Gate registry and Round 56 contracts; SOURCES S277.
- [~] End-to-end domain task executed and logged — LOG.md Round 56, committed matrices, actual counter runs, paired harm receipts; no cleanup action claimed.
- [~] Instructions executable without oral context — prereg real-lane argv, builder and matrix runner, independently reproduced by executor01/02; fixture-only Git authority needed one clarification.
- [~] No cross-domain bleed — PROVINCE.md boundaries unchanged; connector overlap report routes sibling mechanisms without editing them.

Stale-lane: respawn-per-round, no other souji mission open; this round progressed through five pushed commits and settled wave evidence.

Fleet misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`) found only operator .scratch run-state files and shared L0 changes; no souji seat misroot. No sibling/operator files touched. All scratch is removed after evidence landing.

Tools: reviewer01 installed markdown-it-py 4.2.0 and mdurl 0.1.2 via official PyPI/uv into scratch only for independent CommonMark rendering; venv deleted. No permanent installs, pacman transactions or service changes. Final verdict: **rejected-harmed; no admission claimed**.
