# kake — round 79 report (attempt 1, hyaku run 15)

Lane `kake-shokunin` (operability + freshness, plus calibration as a round-54 evidence-backed
sub-axis). Base `0898085450ee1b65d910f1dcb7a0efc20b413b88`; freeze `e1a9a897`; terms-only
amendment 1 `43e0a9b7`; first carrier `436f4429`; final carrier `9cfa404d`; final lane tip
`93809011eaa5d35d2767f54516aebc2b26f53a8d` (`git ls-remote origin refs/heads/master` prints the
same hash).

## Work performed

The round declared **two claims** (1–3 cap), each an axis-move with its own falsifiable
before→after and its own counter:

- **C1 — calibration (score 2, the lowest non-retired axis):** the receipt-rewrite disclosure
  ledger is made current and the round-58-scoped check becomes a standing gate. Base
  `undisclosed=5 met=false`; final carrier `undisclosed=0 met=true`.
- **C2 — operability (capability):** a new offline X-Robots-Tag declaration audit
  (`scripts/x_robots_tag_audit.py`) decides all 31 frozen cases with four degenerate constants
  rejected. Base: tool absent; final carrier: `correct=31 wrong=0 constants_failed=4/4 met=true`.

Round shape: **one v1 wave `w1`, 14 seats** (band 8–16): scout 2, executor 4, scribe 2, reviewer 2,
critic 1, mutation-tester 1, connector 1, sentinel 1; attack share 4/14 = 28.6 % (reviewer 2,
critic 1, mutation-tester 1); connectors 1; the L1 held the planner seat; no residual call.
Spec `w1-spec.json`, dispatch `w1-dispatch.json`, ready `w1.ready`, results `w1-results.json`.

- **Freeze.** `contract.md`, the two counters, the 31-case set with an oracle outside the case
  directories, four degenerate constants, five red controls and the source receipts, committed
  before any seat ran (`e1a9a897`). The frozen case set was implementable exactly: an L1 scratch
  reference passed 31/31 before the tool existed, which exposed three readings that amendment 1
  pinned (A1 `noarchive`; A2 `none` replaced, `all` dropped, `index`/`follow` kept).
- **C1 — disclosure ledger current.** Five undisclosed receipt rewrites found at the base
  (`controls/base-c1-receipt-ledger.txt:2`, `controls/base-c1-events.txt:3-7`): two in round 75
  (`after-harm-battery.txt` at `3ae076ab` and `0df52aed`) and three in round 78
  (`base-c2-sweep.txt` at `c758904c`; `after-c1-population.txt` and `after-c3-matrix.txt` at
  `406021c7`). Five ledger entries with true blob pairs and byte-level kinds
  (`content, append, content, content, content`), append-only `[r79-correction 2026-11-04]` rows in
  `corpus/lessons/round-75.md:154-163` and `corpus/lessons/round-78.md:95-105`, and one
  `corpus/QUALITY.md:1604` criterion. The standing counter imports the frozen round-58 event,
  ledger, `classify()` and note-pointer semantics and generalizes only the predicate (drops the
  round-58 file-count conjunct; replaces its round-scoped rewrite conjunct with `--round`).
  Selftest 15/15; fixture control one green and four red (`controls/ctl-c1-fixtures.txt`), and the
  fabricated/drop-one/cheap-note/round-rewrite variants each fail as designed.
- **C2 — X-Robots-Tag audit.** The tool reads a `x-robots-tag-manifest/v1` document (URL plus
  recorded header fields), network-free, and decides per check the declared normalized global
  directives, the global effective restriction set and the per-bot scopes with seven finding ids
  and exits 0/1/2/64 (`scripts/x_robots_tag_audit.py`, tool `dd83c2c8…`, 19,680 B, selftest
  26/26). The frozen matrix compares exit, finding ids and every check's three sets
  (`c79_xrt_matrix.py`, selftest PASS; `cases_sha256=fd0a3bcc…`); the oracle sits outside the case
  directories and each manifest is copied to scratch before the run, so the oracle-reader cheat
  scores 0/31 (`controls/ctl-c2-oracle-cheat.txt`). Real input: the 12 recorded round-61 header
  sets, exit 0, `checks=12 findings=0` (`controls/after-c2-realrun-final.txt`).
- **Post-attack hardening (disclosed, not hidden).** SentinelC's F1–F6 and ReviewC2's F1 found
  defects outside the frozen cases; the tool was repaired (crashes on huge integer caps and deep
  JSON, non-regular/oversize read, duplicate scan for all four value-bearing directives, text-mode
  id escaping, usage exit 64), selftest 24 → 26, and C2 re-measured at the final carrier. The
  predicate, cases and oracle did not change; the first carrier's receipts stay as history. The
  comma-split date unreachability (ReviewC2 F1) is **not** fixed and is a stated limit.
- **Mutation and security.** MutC killed 10/10 tool mutants by named cases (`w1/MutC/`); it also
  showed the C1 fixture battery does not exercise `wrong_kind`, `malformed` or `symlinks`
  end-to-end (survivors k3/k4/k5), which the QUALITY criterion states. SentinelC reproduced the
  base red, the fixture verdicts and the carrier matrix, and found no claim-breaking vulnerability
  after the fixes.
- **Coverage corrections (ConnectorC).** `corpus/README.md:558-559` and `PROVINCE.md:580-581`
  attributed the X-Robots-Tag channel to `header_audit.py`, which parses no robots directive;
  `corpus/knowledge/meta-robots-directives.md:123` repeated the exclusion. Append-only corrections
  landed (README, PROVINCE, and a `[r79-correction 2026-11-04]` tagged line in the meta entry).
- **Round-78 closure routed defects.** R1 closed by the five entries + lesson rows; R2 by the
  landed-blob selftest `9/9` and counter digest (`w1/ExecR2R3/c78-selftest-landed.txt`, sha256
  `c09651e4…`, 12,238 B); R3 closed by dropping the hard-coded scratch root in
  `c78_shonen_population.py`, two `SKILL.md` registry rows, `exit=` on round-79 receipts and the
  SCORECARD HOLD-token correction row; R4 remains the operator's.
- **Dead seats.** 14 seats settled; `ExecC2Tool` and `CriticC` returned empty output, and
  `ExecC1Ledger`, `ExecR2R3`, `ReviewC1` stopped after their first read
  (`w1-results.json` carries each seat's final text; the three partial seats' last lines name only
  their first read). The L1 completed the tool, the five ledger entries and lesson rows, the
  R2/R3 repairs and the C1 attacks; the independent C1 evidence is SentinelC's reproduction, not a
  separate reviewer seat.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no file a kake
  r79 seat wrote at the fleet root; the stray `after` (2026-11-03) and `agent:/` directory
  (other lanes' seat names) are not kake's.
- **Inherited state.** None: the lane was clean at the base with no prior attempt for round 79.

## Landed changes

Every change is tied to the `LOG.md` `## Round 79` entry and the commit that carries it.

| Commit | Carries | LOG entry |
|---|---|---|
| `e1a9a897` | frozen contract, C1/C2 counters, 31 cases + oracle, four constants, red controls, source receipts | **Frozen contract** bullet |
| `24476085` | w1 spec, validated dispatch, ready handoff | Wave `w1` bullet |
| `6dcc1156` | dispatch evidence, census-before, base C1 event dump | C1 bullet (base receipt) |
| `43e0a9b7` | amendment 1 (vocabulary and normalization terms), oracle-cheat control | Frozen contract bullet |
| `436f4429` | first carrier: five ledger entries, round-75/78 corrections, `x_robots_tag_audit.py`, knowledge entry, S452 + S449 rows, coverage corrections, QUALITY criterion, SKILL rows, R2/R3 fixes | C1/C2 bullets |
| `81e662f9` | first-carrier receipts (C1, C1 cross-check, C2 matrix, real run, census, no-harm freshness) | C1/C2 bullets |
| `87280595` | instrument receipt (23 instruments) and SHONEN population update | C1/C2 bullets |
| `db4ee7e0` | instrument-receipt and SHONEN-population no-harm receipts | C2 bullet |
| `b65b4b78` | registry-row correction for the date-branch claim (ReviewC2 F1) | Routed bullet |
| `9cfa404d` | hardened tool after attacks, all seat reports, `w1-results.json`, lesson and SCORECARD | Post-attack hardening bullet |
| `eabffcb0` | final-carrier receipts and re-pinned instrument receipt | Post-attack hardening / C1/C2 bullets |
| `93809011` | LOG entry, settlement corrections, final instrument-receipt check | All bullets / **Not done** |

## Before → after measurements

**C1 (calibration).** Counting command:
`python3 -B .ufo/waves/round-79/c79_receipt_ledger.py --root . --revision <rev>`.

- Base `0898085450ee1b65d910f1dcb7a0efc20b413b88` (`controls/base-c1-receipt-ledger.txt:2`, exit 1):
  `C1v2 revision=0898085450ee1b65d910f1dcb7a0efc20b413b88 events=32 undisclosed=5 phantom=0 malformed=0 wrong_kind=0 unpointed=0 symlinks=0 round_rewritten=0 met=false`
- Final carrier `9cfa404dbed4dc7f0dca3784b01d33792fe684f0` (`controls/after-c1-receipt-ledger-final.txt:2`, exit 0):
  `C1v2 revision=9cfa404dbed4dc7f0dca3784b01d33792fe684f0 events=32 undisclosed=0 phantom=0 malformed=0 wrong_kind=0 unpointed=0 symlinks=0 round_rewritten=0 met=true`
- Cross-check with the frozen round-58 counter at the same revision
  (`controls/after-c1-r58-crosscheck-final.txt:2`):
  `C1 receipt-rewrites events=32 undisclosed=0 phantom=0 malformed=0 wrong_kind=0 unpointed=0 symlinks=0 new_rewritten=0 new_receipts=2 met=True`

**C2 (operability, capability).** Counting command:
`python3 -B .ufo/waves/round-79/c79_xrt_matrix.py --root . --tool-revision <rev> --cases .ufo/waves/round-79/cases --expect .ufo/waves/round-79/expect/expect.json --consts .ufo/waves/round-79/consts --work <scratch>`.

- Base `0898085` (`controls/base-c2-matrix.txt:1`, exit 2):
  `TOOL_ABSENT rc=128 error=fatal: path 'scripts/x_robots_tag_audit.py' does not exist in '0898085450ee1b65d910f1dcb7a0efc20b413b88'`
  (`controls/base-c2-tool-absent.txt:2` prints the same `rc=128` for `git cat-file -e`).
- Final carrier `9cfa404d` (`controls/after-c2-matrix-final.txt:2`, exit 0):
  `C2v1 revision=9cfa404dbed4dc7f0dca3784b01d33792fe684f0 tool_sha256=dd83c2c8e9046faa0a62afda4cea00fee85468e83d2f1720c92159fb11f2609b tool_bytes=19680 cases=31 decided=31 correct=31 wrong=0 undecided=0 constants_failed=4/4 selftest_ok=true cases_sha256=fd0a3bccbe7c1b6d3522259ab5c57d4eb1f272abe6acaba44013aae3af7978af met=true`
- Real input (`controls/after-c2-realrun-final.txt`, exit 0): `XRTv1 checks=12 findings=0 exit=0`.

**No-harm checks at the final tip.** `python3 -B scripts/instrument_receipts.py --check` prints
`C2v1 revision=eabffcb0489e856c781a4d1ffe8c5265d8cac69c population=23 bound=23 mismatches=0 met=true`
(exit 0); `python3 -B .ufo/waves/round-78/c78_shonen_population.py --root . --revision
9cfa404dbed4dc7f0dca3784b01d33792fe684f0` prints
`C1v1 revision=9cfa404dbed4dc7f0dca3784b01d33792fe684f0 rows=4 rows_with_population=4 undeclared=0 stale_populations=0 exact_mismatches=0 floor_violations=0 growth_tolerated=4 met=true`;
and `node scripts/freshness-sweep.mjs --offline` still prints
`VERDICT: OK (exit 0, partial: offline)` (`controls/after-freshness-offline.txt:4`).

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin kake`.

- **Before:** exit 0, `189` rows, `19` `W04` lines (`controls/census-before.txt`).
- **After:** exit 0, `190` rows, `19` `W04` lines (`controls/census-after.txt`). The counting
  companion `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` prints `190`; `S452`
  adds no `W04`.
- **Rows added by tier:** 1 → tier B (`S452`, MDN X-Robots-Tag). One rejected row is kept
  (`S453`, RFC 9309, tier A, `status=rejected`, 0 `x-robots-tag` occurrences in its text).
- **Rows touched old→new:** `S449` `used-by` gained `corpus/knowledge/x-robots-tag-header.md`
  (logged old→new in the lesson `## Gate`); no `status` or `recheck` change.
- **Frontier rows advanced:** X-Robots-Tag response-header declarations move from "ground it does
  not hold" (README:558-559, PROVINCE:580-581) into held ground with a source-backed entry
  (`corpus/knowledge/x-robots-tag-header.md`) and an offline gate; the corrections are append-only.
  Knowledge `.md` population 65 → 66 (`git ls-tree -r --name-only <rev> -- corpus/knowledge |
  grep -c '\.md$'`).
- **Gate.** Admit `S452` with its located ≤25-word quote and access date (lesson `## Gate`);
  reject RFC 9309 for the header carrier with the sweep and flip; reject a second row on S449's
  URL (within-scope duplicate). Assimilation: none — the `merge/kake` staged ids still collide on
  8 rows (`assimilation/collisions`: `S312 S329 S367 S372 S373 …`). `considerthese/2026-10-26.md`
  Part 2 item 2 (receipt-rewrite watch) is implemented by C1; no other proposal was acted on.

## Trend verdicts

- **expansion — improved.** One admitted knowledge entry on coverage-map ground the lane did not
  hold (`corpus/knowledge/x-robots-tag-header.md`, S452 + S449) and one capability entering the
  SCORECARD table through a demonstrated run, with a new registry row; the entry cites its mined
  row and the capability's receipts are revision-bound.
- **quality — improved.** Five receipt rewrites disclosed with true blobs and byte-level kinds and
  a standing gate with an able-to-fail fixture battery; the X-Robots-Tag tool and its frozen
  differential matrix; three coverage-map mis-attributions corrected append-only; the round-78
  R1/R2/R3 defects closed; the post-attack hardening disclosed rather than folded into an earlier
  scoring.
- **discernment — improved (author-side; the non-author spot-check is owed to the closure).** The
  gate admitted S452 and rejected RFC 9309 and the duplicate-URL row with located evidence; two
  attack seats' disagreements (ReviewC2 F1, SentinelC F1–F6) became a lesson limit, a QUALITY
  criterion clause and a repaired tool, not a silent pass. The lane's attributed seats are not
  outside discernment, so the closure's independent re-open remains the admission check.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `corpus/knowledge/shonen-ledger.json` box 1 `status=evidenced`; re-measured by
  `c78_shonen_population.py` at the final carrier (`met=true`, `stale_populations=0`); the two new
  gate rows are at `SKILL.md:1494-1496`.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — box 2 stays a `gap`:
  one historical LOG-named receipt (`.ufo/waves/round-47/verification/offline-sweep-r46-verdict-time.txt`)
  was never committed; the flip is unchanged and no later rerun can retroactively prove it.
- [~] Instructions executable by an agent without oral context — box 3 `status=evidenced` within
  its frozen scope (`scripts/*.py|sh`, counter paths and `python3 -B` targets); the three
  `node ~/Projects/webzites/...` spans and `scripts/kimi-surface.mjs` remain a stated defect.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — box 4 `status=evidenced`; population
  66 `.md` at the final carrier, 0 sibling-lane repository citations; PROVINCE gains the round-79
  coverage correction, append-only.

No box is `[x]`: no named non-author verifier signed one this round.

## Stale-lane, tooling, open questions

- **Stale-lane:** respawn-per-round driver; this is the lane's only open mission. The launch line is
  `2026-11-04T06:30:42-03:00 launch kake round=79 pgid=630878 driver=hyaku-inline attempt=1`; the
  lane was progressing (commits and worktree changes throughout), and the report is filed in the
  same session.
- **Tool installs:** none; nothing installed or upgraded, pacman untouched.
- **Open L0:** no new line appended this round. Pre-existing kake questions stay open
  (`kake | round-24/25/35/45/58/59/65/67/69/71/72`); the calibration sub-axis ownership question
  (round 59) is still unanswered and the round worked calibration because it is the lowest
  non-retired axis.
- **Stated limits (not claims):** the real-input population is negative (0 of 12 recorded surfaces
  declare the header; four are 404 records), so it proves acceptance and empty-set rendering only;
  RFC 822/850 `unavailable_after` values are unreachable under the comma split (ReviewC2 F1);
  `xrt_input_unreadable` is unexercised by the frozen cases; per-bot effective resolution,
  meta+header conflicts and redirect-hop inheritance are out of scope; S452 is tier B and says the
  header is "not part of any specification", so the bot-name charset, precedence rule and several
  value rules are lane readings; C1's population is the measured revision's first-parent line, the
  byte-level kind cannot prove a run happened, and the ledger has no chronological introduction
  cutoff; the fixture battery does not exercise `wrong_kind`/`malformed`/`symlinks` end-to-end
  (MutC k3/k4/k5); the freeze receipts print `exit=` twice; the freshness axis is held, with
  remote/armed/history checks skipped and never counted as pass.
