# kake — round 76 (hyaku run 15, attempt 1)

Lane `kake` (operability + freshness — web properties and publishing; calibration is the lane's round-54
evidence-backed sub-axis). Base `a0491fcd041cbc3fff2c964ecf6268557e45a5c1`. Lane tip
`284a00fb8442e3d17e358e3f43d3c4f176986908` (pushed; `git ls-remote origin refs/heads/master` prints it).
One v1 wave, 15 seats, no residual call, no dead seat, round total 15. The L1 held the planner seat. The orchestrator's wave
finalizer did not write `w1-results.json` for this wave (the dispatcher's tick never observed the settled
wave); every seat settled and its report is committed under `.ufo/waves/round-76/w1/`, which is the
substantive completion evidence.

**Stale-lane:** this mission was dispatched at 2026-11-03T21:37:27-03:00 and is reported in the same
sitting; it is progressing (14 lane commits authored by `kake-shokunin <kake@shokunin.local>` since launch),
not silent. No earlier attempt of round 76 exists (`grep 'kake.*round=76' .ufo/watchdog.log` → one `launch`
line, attempt 1), so there is no inherited working tree to resolve.

## Work performed

The round declared **two claims on distinct axes**, both frozen in
`kake-shokunin/.ufo/waves/round-76/contract.md` (`b758cb04`) before any seat ran, with eight terms-only
amendments recorded before their after-states (`783c7c13`, `e674bc60`, `6b52407b`, `f4f076ba`, `152bffd5`,
`d2555766`, `d00ea7fb`; amendment 5 at `152bffd5`).

- **C1 — calibration (the lane's lowest non-retired axis, score 2, HOLD).** The lane's claim rows stop
  quoting command output that no committed receipt contains. Instrument `scripts/doc_quote_truth.py`
  (hardened from the frozen v1 `c76_quote_truth.py`, sha256 `e7f86d3a…`, selftest 63/63). Evidence:
  base `a0491fcd` seven absent-span findings (`controls/base-c1-quote-truth-v2.txt`), carrier
  `7ac91803` no findings (`controls/after-c1-quote-truth-final.txt`), closed by seven whole-line
  correction rows in `SCORECARD.md` §"Round 75 — quote corrections (appended round 76)", one
  `corpus/QUALITY.md` criterion and one `corpus/lessons/round-75.md` §Corrections bullet.
- **C2 — operability (capability acquisition, score 10, HOLD).** The lane can audit hreflang declarations
  offline: `scripts/hreflang_audit.py` (sha256 `0762452f…`, selftest 59/59) with a frozen 71-case matrix
  (`cases=71 decided=69 correct=69 wrong=0 undecided=2 constants_failed=4/4 met=true`,
  `controls/after-c2-matrix.txt`) and an end-to-end run over the eight retained served pages
  (`pages=8 findings=[] exit=0`, `controls/after-c2-realrun.txt`). Capability row: `SCORECARD.md`
  §"Capabilities acquired in round 76"; registry rows: `SKILL.md` §"Round 76 gate registry additions".
- **Frozen v1 counter and five red controls** committed with the freeze: do-nothing (7 findings), junk
  correction (T4), laundering (a validated quote that names no defective span: `corrections=1 exempted=0
  findings=8`), deletion (`A1`, `append_only=false`), cheap content — all exit 1
  (`controls/ctl-*.txt`).
- **Contract defects found and decided by amendment, not argued away.** The wave found 16 undecided C2
  classes (Amendment 2), a counter/receipt tautology (Amendments 4 and 5: a diagnostic receipt laundered
  the defects it reported and the round's do-nothing control silently turned green), a receipt-universe
  over-exclusion (Amendment 7), the canonical/x-default granularity (Amendment 6) and a real
  source-vs-contract divergence (Amendment 8: the same-tag reciprocity rule is stricter than S444's
  stated rule).
- **Assimilation: none.** The connector re-checked `merge/kake/` read-only: staged ids S287–S415 all sit
  below the registry tip (S443), eight of them are occupied with different content, so adoption as written
  would rewrite held rows and insert ids mid-file (`w1/ConnectorOverlap.md` §2).
- **Sibling overlap:** no sibling lane holds an hreflang audit, a documentation-quote-truth counter or a
  BCP-47 validator; the three nearest analogues are complementary, not duplicate
  (`w1/ConnectorOverlap.md` §1).
- **considerthese:** `considerthese/2026-10-26.md` Part 2 proposal 5 (historical-gate list) is already
  adopted (r66 ledger + r75 criterion); no new proposal was mined, and the report says so rather than
  double-counting it.

## Landed changes

Every change below is tied to the `LOG.md` round-76 entry and carried by the named lane commit (all
authored `kake-shokunin <kake@shokunin.local>`).

| Commit | What it lands | LOG tie |
|---|---|---|
| `b758cb04` | frozen contract, v1 counter, five red controls, wave spec and dispatch | LOG r76 "Frozen contract" |
| `783c7c13` | Amendment 1 (real-input population = 8 retained served pages) | LOG r76 "Frozen contract" |
| `e674bc60` | Amendment 2 (16 undecided hreflang classes decided), L1 disposition ledger, sweep receipt, census-before | LOG r76 "Frozen contract" |
| `6b52407b` | Amendment 3 (revision/digest split, section identity, whole-line correction closure, exact append-only, ready artifacts, re-measured before-state) | LOG r76 "Frozen contract" |
| `f4f076ba` | Amendment 4 (the counter's own diagnostics are never receipts) | LOG r76 "Frozen contract" |
| `442d36c6` | C1 repair: five quote-correction rows in `SCORECARD.md`, one `corpus/QUALITY.md` criterion, one `corpus/lessons/round-75.md` correction | LOG r76 "C1 landed and measured" |
| `152bffd5` | Amendment 5 (receipt directories only; diagnostic-line stripping; the delivered selftest must run) | LOG r76 "Frozen contract" |
| `d2555766` | Amendments 6–7; `corpus/knowledge/hreflang-declaration.md`; `corpus/SOURCES.md` S444–S446 | LOG r76 "Frontier and sources" |
| `d00ea7fb` | Amendment 8 (same-tag reciprocity is a stricter lane policy; frozen ASCII grammar is not BCP-47); entry corrections; `corpus/README.md` coverage rows | LOG r76 "Frontier and sources" |
| `2cccd59a` | `scripts/doc_quote_truth.py`, `scripts/hreflang_audit.py`, `SKILL.md` registry rows, `SCORECARD.md` claims + capability row, `LOG.md` entry, `corpus/lessons/round-76.md`, wave evidence | LOG r76 (whole entry) |
| `9dea7b2f` | lesson corrections (whole-line digests, selftest tally 63/63) and admissible summary receipts | LOG r76 "Corrections (round-75 closure R1/R2)" |
| `b8673e87` | C1 after-state receipt, mutation-breadth paragraph, wave seat evidence | LOG r76 "C1 landed and measured" |
| `7ac91803` | after receipt + `w1/` seat reports | LOG r76 "C1 landed and measured" |
| `b5597f55` | final C1 receipt at `7ac91803` | LOG r76 "C1 landed and measured" |
| `ffbb2e69` | `PROVINCE.md` §"Round-76 hreflang frontier step" (hreflang moves to Core with its boundary) | LOG r76 "Frontier and sources" |
| `284a00fb` | last seat report (`w1/ScribeRegistry.md`) | LOG r76 "Wave w1" |

## Before → after measurements

**C1 (calibration).** Counting command, run over committed bytes:

```sh
python3 -B scripts/doc_quote_truth.py --root . --revision <rev> \
  --base a0491fcd041cbc3fff2c964ecf6268557e45a5c1 --rounds 75,76
```

- Before, measured at `a0491fcd` (base): `C1v2 revision=a0491fcd rows=16 receipt_files=7923 spans=25
  exempted=0 corrections=0 findings=7 met=false`, exit 1 — `controls/base-c1-quote-truth-v2.txt`.
- After, measured at `7ac91803`: `C1v2 revision=7ac91803 rows=42 receipt_files=7934 spans=67 exempted=7
  corrections=8 findings=0 met=true`, exit 0 — `controls/after-c1-quote-truth-final.txt`; re-run at the
  final tip `284a00fb` gives the same verdict (`findings=0 met=true`).
- Do-nothing evidence: a tree at base plus this round's controls, with no repair rows, still prints
  `findings=7 met=false`, exit 1 (`w1/ExecQuoteRepair.md` Appendix A, receipt 13).

**C2 (operability, capability).** Counting command:

```sh
python3 -B .ufo/waves/round-76/w1/ExecAuditMatrix/c76_hreflang_matrix.py --root . \
  --tool scripts/hreflang_audit.py --revision <rev> \
  --cases .ufo/waves/round-76/w1/ExecAuditMatrix/cases \
  --consts .ufo/waves/round-76/w1/ExecAuditMatrix/consts --work <scratch>
```

- Before: no hreflang audit exists in the lane (`git ls-files 'scripts/*hreflang*'` at `a0491fcd` → 0
  paths); a do-nothing tree decides no case.
- After, measured at `284a00fb`: `cases=71 decided=69 correct=69 wrong=0 undecided=2
  constants_failed=4/4 met=true`, exit 0 — `controls/after-c2-matrix.txt`. Each of the four constants
  (no-op, always-clean, report-all, empty-list) fails 69 of 69 cases; a bare findings-empty printer fails
  all of them under the matrix's shape check (`w1/MutationTesterGates.md`).
- Tool selftest `selftest 59/59 passed`, exit 0; real-input run over the eight retained served pages:
  `{"version": 1, "pages": 8, "findings": [], "counts": {...all zero...}, "exit": 0}` —
  `controls/after-c2-realrun.txt`.

**Attack breadth.** 18 mutants across both instruments, 17 killed, one survivor that is an unreachable
redundancy (dropping the append-only conjunct changes no observable because every base-only row already
emits `A1`); one named selftest gap (a case-insensitive span comparison survives the counter's own
selftest and is caught only by an external probe) — recorded in `SCORECARD.md` and not claimed closed.

## Sources & frontier

Counting command, run at round start and round end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake
```

- **Before:** exit 0, `kake ok`, 181 rows (`controls/census-before.txt`).
- **After:** exit 0, `kake ok`, 184 rows (same 16 pre-existing `W04` duplicate-URL warnings, unchanged).
- **Rows added by tier:** 3 rows, all tier **A** — S444 (Google localized versions, `docs`), S445 (WHATWG
  HTML `hreflang`/`alternate`, `spec`), S446 (RFC 5646 / BCP 47, `spec`). No B or C rows added.
- **Rows touched old→new:** none. No existing row's `status`, `recheck` or `used-by` cell changed this
  round (`git diff a0491fcd..284a00fb -- corpus/SOURCES.md` is three added lines, no modified row).
- **Frontier rows advanced:** hreflang declarations entered from frontier to core — the knowledge entry
  `corpus/knowledge/hreflang-declaration.md` cites S444–S446, `corpus/README.md` §"Coverage — round 76"
  records the area, and `PROVINCE.md` §"Round-76 hreflang frontier step" moves it to Core with its
  boundary.
- **Gate record:** three admits (S444, S445, S446) with URL, access date and a ≤25-word located quote, and
  two rejects (the canonical-interaction rule is not stated by any opened source — it stays a lane policy;
  `x-default`'s reserved status is Google-grounded only) — `corpus/lessons/round-76.md` §Gate. The scout's
  own quote receipt is `w1/ScoutHreflangSources/verify-output.txt` (`quotes=17`, `failures=0`).
- **Assimilation: none** — `merge/kake/` was re-checked read-only and every staged id sits below the
  registry tip with eight occupied and different (`w1/ConnectorOverlap.md` §2).

## Trend verdicts

- **expansion — improved.** One admitted knowledge entry on coverage-map ground the lane did not hold
  (hreflang declarations), citing three `mined` rows opened this round, plus two new coverage rows and a
  `PROVINCE.md` core move; the new capability row enters `SCORECARD.md` with a running demonstration.
  Qualified: the entry is scoped to declaration auditing, and one of its contract rules is explicitly
  unsourced.
- **quality — improved.** Seven claim rows that quoted receipt fragments now quote whole lines and are
  re-derivable; a standing instrument (the C1 counter) is able to fail on the base and green only after
  the repair; the new hreflang audit decides 69/69 decided cases with all four constants failing and nine
  tool mutants killed. No admitted entry was found false or left unmarked.
- **discernment — improved.** The Gate records three admits and two rejects with flip conditions, the
  round's own contract was amended eight times rather than argued around (including a tautology that made
  the do-nothing control pass), and the source-vs-contract divergence was disclosed in the entry and the
  capability row instead of smoothed. Outside spot-check of this round's gate decisions is owed to the
  hyaku closure.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence:
  `SKILL.md` §"Round 76 gate registry additions" (two instruments with verdict maps and pinned proofs),
  the C2 finding table in `corpus/knowledge/hreflang-declaration.md`, and `corpus/QUALITY.md` §"Round-76
  criterion"; author-side only, no non-author verifier yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: the real-input hreflang
  audit over the eight retained served pages (`controls/after-c2-realrun.txt`) plus the C1 repair
  measurement chain, logged in `LOG.md` §"Round 76"; executed and logged, non-author verification owed.
- [~] Instructions executable by an agent without oral context — evidence: `SKILL.md` "How to verify" gives
  the three commands and their expected lines; `scripts/*.py --selftest --work <dir>` are runnable as
  written; asserted by the lane, not yet re-run by a non-author.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` §"Round-76 hreflang
  frontier step" states the boundary (no engine selection, translation quality, language detection or
  header-delivered hreflang); the connector found no sibling scope contention
  (`w1/ConnectorOverlap.md` §1). Author-side; the closure's independent check is owed.

## Round shape, seats and limits

- One v1 wave `w1`, 15 seats: scout 2 (`ScoutHreflangSources`, `ScoutHreflangEdge`), executor 5
  (`ExecAuditTool`, `ExecAuditMatrix`, `ExecAuditRealRun`, `ExecQuoteCounter`, `ExecQuoteRepair`), scribe 2,
  reviewer 2, critic 1, mutation-tester 1, connector 1, sentinel 1. Attack share 4/15 = 26.7 % (reviewer,
  critic, mutation-tester); one connector seat. No residual call. **Dead seats: 0** — all 15 delivered
  reports under `.ufo/waves/round-76/w1/`; round total 15. The validator accepted the wave under
  `ufo-wave-policy.json` (band 8–16, declared 15).
- **Tool installs:** none. No tool was installed or upgraded; pacman untouched.
- **Open L0 questions:** unchanged and routed around — `kake | round-69` (the freshness sweep's single
  `~/projects` drift; the sweep still exits 1 and was not re-pinned), `kake | round-59` (calibration
  sub-axis ownership), `kake | round-71` (attack-share set), `kake | round-72` (staged ids S303/S304/S352).
  No new L0 line was needed this round.
- **Stated limits, not claimed closed:** the same-tag reciprocity rule is a lane policy stricter than S444
  (Amendment 8 §G1); the frozen grammar is an ASCII validator that rejects grandfathered and extension tags
  (§G2); three matrix classes stay `undecided` (§G3); the real-input population is eight retained served
  pages of twelve named surfaces (Amendment 1), and only one of them declares hreflang at all, so the real
  run is clean because the population is nearly declaration-free; the two sidecar tools remain outside the
  instrument receipt (disposition 4); `c58_receipt_rewrites.py` still does not watch
  `corpus/knowledge/` (disposition 11).
- **Fleet-root strays:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only
  orchestrator-owned `.scratch/` files, `.ufo/l0-questions.md`, two sibling reports
  (`.ufo/reports/round-68/mado.md`, `.ufo/reports/round-71/kama.md`) and a 24-byte `after` file dated
  20:05 (before this round launched, no kake/round-76 content). No seat of this round wrote into the fleet
  root; nothing was copied or deleted.

## Erratum (appended after filing; supersedes the text it names)

The paragraph above "Round shape, seats and limits" says the orchestrator's wave finalizer did not write
`w1-results.json`. That was true at filing time and is now superseded: the dispatcher finalized the wave
after this report was committed and wrote `kake-shokunin/.ufo/waves/round-76/w1-results.json`, which is
committed as lane commit `a1b3f33b`. The file records `lane=kake round=76 wave=w1 seats=15`, 15 results,
0 empty outputs, role mix executor 5 / scout 2 / scribe 2 / reviewer 2 / critic 1 / mutation-tester 1 /
connector 1 / sentinel 1 — identical to the shape this report states. Dead seats: 0. The lane tip is now
`a1b3f33b9d00137b1c45c5b4c274ce8f0cc95446` (pushed; `git ls-remote origin refs/heads/master` prints it);
the earlier cited tip `284a00fb` remains an ancestor of it, and the C1 counter re-run at `a1b3f33b` prints
`findings=0 met=true`, exit 0. No other statement in this report changes.
