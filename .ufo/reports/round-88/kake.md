# kake round 88 — three routed defects closed and a conservative Vary-match reader

Lane `kake`, round 88 (attempt 1). Lane root `/home/vgpnk/Projects/shokunin/kake-shokunin`.
Base `f4479c14813037ad993a49a3dee4028763470f7a`; measured carrier
`55d67f15f7a58fb49ca32a31b5c63ae716e1c38a`; lane HEAD at filing
`741fb728b2e22c7a35288d9c645e0dd71d9a0e6b` (pushed; `git ls-remote origin
refs/heads/master` prints it). Report commit: the fleet commit carrying this file.

## Work performed

Declared claims (2, each on a distinct owned axis, each with its own before→after):

- **C1 — calibration (lowest owned non-retired axis, held at 2):** close the three
  defects the round-87 outside closure routed — R1 (`corpus/knowledge/gate-agreement-ledger.json`
  under `knowledge/` with no provenance trio), R2 (the `invalid_input` message that
  names `boolean` for a float), R3 (an ephemeral `/fast/scratch` path in the
  `recheck:` line).
- **C2 — freshness (held at 10), bounded capability:** an offline conservative
  `Vary`-match reader for RFC 9111 §4.1's match rule, scored on 20 hand-labelled
  cases and a seeded 200-input differential population, plus one source-backed
  knowledge entry and one SOURCES row.

Work items, each with its evidence pointer:

- Froze the contract, both counters, the 20-case set and three base blobs **before
  any data**: `.ufo/waves/round-88/{contract.md,c88_defect_queue.py,c88_vary.py,vary-cases.json,frozen/}`
  at `4f8945ea`, amended `80637397` (added the seeded population) and `52e41d2d`
  (validation before the wildcard rule — see the errata in the contract and in
  `corpus/lessons/round-88.md`).
- Built the **do-nothing / cheapest controls** before freezing the targets:
  C1 base `open=3 met=false` (`.ufo/waves/round-88/controls/base-c1.txt`), C2 base
  `frozen=0/20 random=0/200 met=false` (`controls/base-c2.txt`), and three
  constant-answer stubs scoring `7/20 + 67/200`, `9/20 + 109/200`, `4/20 + 24/200`
  (`controls/ctl-c2-constant-{match,mismatch,invalid}.txt`). Counter selftests
  `11/11` and `17/17` (`controls/c1-selftest.txt`, `controls/c2-selftest.txt`).
- Ran **one validated v1 wave of 14 seats** through the inline spawn handoff
  (`w1-spec.json`, `w1-dispatch.json` at `add7e49b`, `w1.ready`, `w1.ready.dispatched`,
  `w1-results.json`, `wave-done-receipt.txt`): scout 2 (`ScoutVary`, `ScoutSpec`),
  executor 4 (`ExecReader`, `ExecCases`, `ExecDefects`, `ExecTrial`), scribe 3
  (`ScribeVary`, `ScribeLedger`, `ScribeLesson`), reviewer 2 (`ReviewCounter`,
  `ReviewReader`), critic 1 (`CriticClaims`), mutation-tester 1 (`MutReader`),
  connector 1 (`ConnectorScope`). Requested attack share 4/14 = 28.6 % over
  {reviewer, critic, mutation-tester, labrat}. All 14 settled with non-empty output
  and a report on disk; **0 dead seats, no replacement, no residual call**. The
  results schema carries no per-seat `status` field for any seat — disclosed, as in
  round 87.
- Integrated the independent candidates into production (L1 is the only writer):
  `scripts/vary_match.py` (seat `ExecReader`, sha256 `fdceef47…`),
  `scripts/cache_current_age.py` (seat `ExecDefects`, one line),
  `corpus/knowledge/vary-matching.md` (seat `ScribeVary`, plus the L1's adapter-limits
  section), `corpus/knowledge/gate-agreement-metadata.md` and
  `corpus/knowledge/cache-current-age.md` (seat `ScribeLedger`), `corpus/SOURCES.md`
  row S463, `SKILL.md` registry section. Carrier `55d67f15`.
- Confirmed the carrier with independent probes rather than the counter's own
  banner: three payloads including the Age-omitted branch are byte-identical to the
  frozen base (`controls/diagnostic-d2-arithmetic.txt`), the integrated tools' own
  selftests pass 22/22 and 61/61 (`controls/integrated-selftests.txt`), and the
  trailing-LF token class is refused by the shipped reader
  (`controls/diagnostic-lf-probe.txt`).
- **Actual domain work**: one public `GET https://ds4cc.com/` (HTTP 200, 78,897 B,
  sha256 retained, `vary: Accept-Encoding`, no cookie or credential), captured by
  seat `ExecTrial`; four retained payloads replayed through the integrated reader at
  the carrier — `match`, `mismatch`, `match`, `invalid_input`, exits 0/0/0/1
  (`controls/integrated-trial.txt`). One identical-side observation is not a
  discriminating proof and is not claimed as one.
- Attacked the round's own instruments and recorded every surviving false green:
  a table keyed on the committed seed or an oracle-import stub passes C2
  (`w1/CriticClaims.md` §2.1/§2.2); the counter's `is_token` accepts a trailing LF
  while the shipped reader refuses it (`w1/ReviewReader.md` §4b); frozen case 14 and
  13 seeded labels are adapter conventions a §5.6.1.2-faithful reader would fail
  (`w1/ReviewReader.md` S2, `w1/ExecCases.md`); 6 of 21 C2 mutants survive
  (`w1/MutReader.md` §3); C1's D1/D2/D3 predicates are weaker than their wording
  (`w1/ReviewCounter.md` F1–F10). Routed, not repaired after scoring.
- **Frontier step**: opened RFC 9111 §4.1 and RFC 9110 §12.5.5/§5.2/§5.6.1.2 this
  round, wrote the Gate with one admit and three rejects, mined four mistakes, and
  recorded the assimilation collision census (`.ufo/waves/round-88/w1/ConnectorScope/{reg-ids,staged-ids,collisions}`).

## Landed changes

Each change is tied to the LOG entry `LOG.md` §Round 88 (appended at `edcb2980`) and
to the commit that carries it.

| Change | Commit |
|---|---|
| Freeze v1: contract, both counters, 20-case set, three base blobs, base and control receipts | `4f8945ea` |
| Freeze v2: seeded 200-input differential population added to the C2 counter, target restated | `80637397` |
| Freeze v3: reference validation ordered before the wildcard rule; controls re-run; L1 fallback draft | `52e41d2d` |
| Validated 14-seat wave handoff: spec, dispatch, registry | `add7e49b` |
| Round-start source census (exit 0, W04 = 24) | `f60a852a` |
| Production: `scripts/vary_match.py`, the one-line `scripts/cache_current_age.py` diagnostic, `corpus/knowledge/vary-matching.md`, `corpus/knowledge/gate-agreement-metadata.md`, the corrected `corpus/knowledge/cache-current-age.md` (one replaced metadata line + one appended checklist item), `corpus/SOURCES.md` S463, `SKILL.md` registry | `55d67f15` |
| Records: `LOG.md`, `SCORECARD.md`, `corpus/README.md` frontier, `corpus/lessons/round-88.md`, contract errata, all wave evidence and carrier receipts | `edcb2980` |
| Final source census receipt (exit 0, W04 = 25) | `741fb728` |

Errata, disclosed not rewritten: commit `add7e49b`'s subject says "twelve-seat" while
the wave has fourteen seats (subject copied from round 87); `52e41d2d`'s sentence
"No item, case, threshold, control or target moved" is inaccurate for three seeded
labels and the population digest — corrected in the contract's appended errata and in
`corpus/lessons/round-88.md`.

## Before → after measurements

Both measured at carrier `55d67f15f7a58fb49ca32a31b5c63ae716e1c38a`, re-run at
`edcb2980` with identical results; base is `f4479c14`.

**C1 (calibration, 2 HOLD)** — counting command:

```sh
python3 -B .ufo/waves/round-88/c88_defect_queue.py --root . \
  --revision 55d67f15f7a58fb49ca32a31b5c63ae716e1c38a \
  --work /fast/scratch/hyaku/kake-r88/L1/after-c1
```

Before: `C1v1 revision=f4479c14… items=3 open=3 closed=0 met=false`, exit 1
(`controls/base-c1.txt`; details: companion missing; float diagnostic still says
`boolean`; recheck names `/fast/scratch` and `TMPDIR=` and no `mktemp` command).
After: `C1v1 revision=55d67f15… items=3 open=0 closed=3 met=true`, exit 0
(`controls/after-c1-carrier.txt`). Verdict: **met (bounded)** — D2 is behavioural,
D1 binds the ledger's sha256 into the companion, D3 permits exactly one replaced
metadata line and otherwise only insertions; the shipped repair is proven separately
by the diff and the three-payload arithmetic receipt. Counter selftest 11/11.

**C2 (freshness, 10 HOLD, capability)** — counting command:

```sh
python3 -B .ufo/waves/round-88/c88_vary.py --root . \
  --revision 55d67f15f7a58fb49ca32a31b5c63ae716e1c38a \
  --work /fast/scratch/hyaku/kake-r88/L1/after-c2
```

Before: tool absent, `frozen=0/20 random=0/200 met=false`, exit 1
(`controls/base-c2.txt`). After: `frozen=20/20 random=200/200 met=true`, exit 0,
`cases_sha256 c461cbd8…`, `random_sha256 52714a5f…`
(`controls/after-c2-carrier.txt`). Verdict: **met (bounded)** — the frozen 20, the
seed and the thresholds are unchanged from freeze v3 to the carrier
(`controls/frozen-identity-carrier.txt`); the capability is independently corroborated
by a second implementation (`w1/ReviewReader/indep.py`), an independent expectation
table (`w1/ExecCases/expectations.json`), a 21-mutant battery (15 killed) and one real
capture replay. Instrument limits R88-1…R88-7 stay on the routed queue.

No owned axis is harmed on the exercised paths: the only modified script is
`scripts/cache_current_age.py` (one diagnostic line; arithmetic byte-identical on
three payloads), the round-87 instrument and fixtures are untouched, and both
counters still run. This is not a whole-corpus no-harm proof.

## Sources & frontier

Census command, run at round start and at round end, both exit 0:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake
```

Before (`.ufo/waves/round-88/controls/census-before.txt`): exit 0, 24 `W04` warnings,
registry ends at S462. After (`controls/census-final.txt`): exit 0, 25 `W04`, ending
`kake ok …/corpus/SOURCES.md`. The increment is S463, a third scoped row for the
already-carried `httpwg.org/specs/rfc9111.html` URL (S461 lifetime, S462 age, S463
matching) — the expected cross-scope duplicate warning, not an error.

Rows: `corpus/SOURCES.md` 200 → 201 (`controls/committed-corpus-counts.txt`; count
command `git show <rev>:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`).
Rows added by tier: **A = 1** (S463, RFC 9111 §4.1, `kind: spec`, status `mined`,
`opened 2026-11-04`, `recheck 180d`, `used-by` exactly `corpus/knowledge/vary-matching.md`).
Rows touched old→new: none — no existing row's `status`, `recheck` or `used-by` changed.
Knowledge entries `.md`: 74 → 76 (two new entries: `vary-matching.md`,
`gate-agreement-metadata.md`; the latter is provenance metadata for the r84–86
ledger, deliberately not counted as domain expansion).

Frontier rows advanced: RFC 9111 §4.1's *match* rule moves from frontier to core
(`corpus/README.md` §Round-88 frontier step, `corpus/knowledge/vary-matching.md`).
Still open there: field-specific normalisation (the third permitted transformation
the reader declines), the CR/LF/NUL rule, a population the candidate cannot read,
cache-key construction, storage, revalidation and serving.

Gate (`corpus/lessons/round-88.md` §Gate): one admit — S463 with the quote "A stored
response with a Vary header field value containing a member `"*"` always fails to
match." (RFC 9111 §4.1, opened 2026-11-04) — and three rejects: "Vary match proves
cache reuse is safe" (the MUST NOT is one condition among §4's several), "the C2
counter's pass shows the reader implements §4.1" (the counter scores a published
oracle), and "an empty `Vary` must be refused" as an RFC requirement (RFC 9110
§5.6.1.2 requires parsing and ignoring empty list elements; case 14 is an adapter
convention and the entry now says so).

**Assimilation: none** — `merge/kake` still collides on the same eight registry ids
(S312, S329, S367, S372, S373, S374, S390, S409), re-derived this round with the
0–3-leading-space extractor (`w1/ConnectorScope/{reg-ids,staged-ids,collisions}`).

**considerthese**: `considerthese/2026-10-26.md` proposal 2 (receipt-rewrite watch)
was mined into the lesson with a measurement: 1,577 tracked files under
`.ufo/waves/round-*/controls/`, 36 with more than one commit, four of them this
round's own disclosed control re-runs. No new QUALITY criterion was added because no
failing witness was demonstrated for the wider class.

Adjacency: `mori-shokunin` S594 already holds a one-line RFC 9111 §4.1 rule
(`w1/ConnectorScope.md` §1.3). Reported, not absorbed; the lane's entry is the
publisher-side reader and decision table.

## Trend verdicts

- **expansion: improved** — one admitted knowledge entry on ground the coverage map
  did not hold (RFC 9111 §4.1 match semantics), citing the mined A-row S463, plus one
  capability row in `SCORECARD.md` ("Conservative Vary-match reader", first-working
  round 88). Knowledge `.md` 74 → 76; sources 200 → 201. The provenance companion
  earns no expansion credit.
- **quality: improved (bounded)** — the new reader is verified rather than asserted:
  20/20 hand cases, 200/200 seeded, 22/22 integrated selftest, a second independent
  implementation, a 15/21 mutation kill and one real capture replay; the r87 routed
  defects are closed with a behavioural check and a minimal-diff proof. Limits are
  routed, not hidden (R88-1…R88-7). Nothing admitted this round fails its re-check.
- **discernment: improved (instruments only; outside spot-check pending)** — the
  lane's own attack seats falsified its instruments in-round (a table over the
  committed seed and an oracle-import stub both reach `met=true`; the counter's token
  test accepts a trailing LF the shipped reader refuses; a §5.6.1.2-faithful reader
  fails the frozen case set). The gate decisions were made against those findings, and
  the reject rows in §Gate rest on the same §5.6.1.2 sentence the reviewer used.
  The non-author closure's admit/reject sample is still owed; this report does not
  claim it.

## SHONEN

One line per box of `SHONEN.md` (4 boxes, unchanged this round):

- [~] box 1 "SKILL.md contains real decision tables, error patterns, checklists,
  cited sources" — `SKILL.md` gained the Round-88 registry section (three tool rows
  with verdict maps, selftests, pinned values and owners) at `55d67f15`; evidence
  pointer `.ufo/waves/round-88/w1/L1/skill-section.md` and `grep -c 'vary_match'
  SKILL.md` → 1. Not re-promoted to `[x]`: no non-author verifier ruled on this box.
- [ ] box 2 "At least one end-to-end domain task executed and logged in LOG.md" —
  the historical round-47 named-receipt gap stands (`SHONEN.md` row `box 2`,
  `status=gap`); this round's ds4cc.com capture and replay are logged and cited, but
  the box stays open until a non-author verifier accepts the population check.
- [~] box 3 "Instructions executable by an agent without oral context" — the entry's
  three checklist commands run at the carrier (`controls/integrated-trial.txt`,
  `controls/integrated-selftests.txt`), and the SKILL registry rows name the exact
  argv for both counters.
- [~] box 4 "No cross-domain bleed (PROVINCE.md still accurate)" — `grep -rlE
  '<lane>-shokunin' corpus/knowledge/*.md | wc -l` → 0 of 76 entries cites a sibling
  lane repository path; the mori S594 overlap is recorded in `PROVINCE.md`'s
  adjacency note and this report, not absorbed into the entry.

## Stale-lane

Respawn-per-round driver: this lane's mission closed with this round's report; no
other kake mission is open and no round 89 is started here.

## Round shape, seats, tooling

One v1 wave, 14 requested seats inside the run-15 band 8–16, 14 settled, attack
4/14 = 28.6 %, no dead seat, no replacement, no residual call; round total 14.
The L1 held the canonical planner seat (the validator forbids `planner` as a swarm
role) with a bounded planning data-walk on `ScoutVary`; the literal L2-planner
conflict D84-4 remains open in `.ufo/l0-questions.md` (kake | round-86). Routing was
read from `~/.omp/agent/config.yml` at spawn and never passed: task/main/planner/
reviewer/security-reviewer/executor/revenger/labrat/mutation-tester/sentinel
`@m_flash`, critic/scout/simplifier/scribe/sonic/distiller/seance `@m_mim`,
connector `@m_antigravity`; no claim depends on a particular answering model.
No tool was installed or upgraded this round (Python 3.14.8 already present; pacman
untouched). Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain`
shows only orchestrator `.scratch/` state, another lane's `round-84/kama.md` edit, an
unidentified pre-existing `after` file and `tsukuroi`'s `.ufo/tmp-census-r79.txt`;
no file attributable to this lane's seats, nothing deleted, nothing edited outside
the write scope.
