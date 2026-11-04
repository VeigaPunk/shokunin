# kama round 78 — lane report

Lane: kama. Round: 78 (attempt 1). Base `c62ffd3aea930b98375f805cc3dfb821a703148b`; freeze
`11f46d644ed08d11758874a92d79214b3577a8a0` (amended pre-dispatch from `d015a178`); lane tip
`7a3cd98243b69fcbee0cc9e31878782bd8459320` (branch `master`, remote-verified below). Assigned axes:
operability + calibration (`shokunin.conf`). Round shape: ONE v1 wave of **12 seats** under
`ufo-wave-policy.json` (band 8–16), attack 4/12 = 33 % (1 reviewer, 2 critic, 1 mutation-tester),
one connector seat. Seats: 3 executor, 3 scribe, 1 scout, 1 connector, 1 reviewer, 2 critic,
1 mutation-tester. **3/12 seats returned output; 9 returned empty and are recorded dead**
(`.ufo/waves/round-78/w1-results.json`). No residual call; round total 12.

## Work performed

Declared claims (frozen in `plans/round-78-claims.md`, committed at the freeze; amended once
pre-dispatch, before any seat scored):

- **C1 — calibration** (lowest assigned axis, 7): six declared facts of the round-77 self-record
  re-derive from the tree, or are answered by dated value-bound corrections.
- **C2 — freshness**: every base audit event is accounted once at the audited revision, and register
  rows outside that population change no bucket.
- **C3 — operability**: the probe's `MODEL_OK` / `MODEL_MISMATCH` / `DEAD` verdicts are exercised
  end-to-end against a live pinned llama.cpp child.

Work items:

- **C1 counter.** `tools/round78-selfrecord-round77.py` (40 KB): `PREDICATE` is the plan's blockquote
  verbatim; F1–F6 derive from the tree (Axes vector, the sealed canonical capability table, the SKILL
  gate row bound by AST to the gate module's `ARM_ORDER` plus the round-77 receipt tally, the record's
  last §-pointer sentence, knowledge introductions in `(record base..sealed]` with `S###` provenance,
  README coverage rows); §Corrections blocks are graded value-bound (`at` must be the sealed revision,
  `old` re-derives there). Eight selftest arms. Real-tree run before the repairs: `mismatches=2
  corrected=2`; after: the frozen line. Evidence: `tools/round78-selfrecord-round77.py`,
  `.ufo/waves/round-78/measured/after/c1-facts.out` (line 4362 of `SCORECARD.md` §Round 78).
- **C1 repairs (four).** `SKILL.md` pre-report-gate row rewritten in place to nine arms / `arms=9` /
  `pass=22` / `round77-instruments` (SC03Duties' landed edit); a pointer correction appended to
  `SCORECARD.md` §Round 77 (`corpus/lessons/round-77.md` §Freeze divergences item 3); a
  `source-correction:` line citing S073 in `corpus/knowledge/register-cutoff-split.md`; two coverage-map
  rows in `corpus/README.md`. Evidence: `SCORECARD.md:4388-4390`, `corpus/knowledge/register-cutoff-split.md:76`.
- **C2 counter.** `tools/round78-append-registers.py` imports the byte-frozen round-77 module, adds the
  population filter (an event must be ancestral to `--to`), the committed-row boundary (`--commit-at`),
  the `APPEND_REGISTERS_OUT_OF_POPULATION` and `APPEND_REGISTERS_REGISTERS` lines, and seven selftest
  arms. Three `exempt-head` rows appended for the round-77 SCORECARD events (counts 3/2/1, sections
  derived from the audit, never fitted). Evidence: `tools/round78-append-registers.py`,
  `registry/append-only-exempt.tsv:58-61`.
- **C3 instrument.** `tools/round78-live-reconcile.py` starts `~/.local/opt/llama-b11755/llama-server`
  (binary and model sha256 recorded) on an unregistered free loopback port, writes a three-row scratch
  registry, runs the probe, grades the three verdicts, requires `runtime=llama.cpp` and the pinned
  served id, refuses registered consumer ports before probing, tears the child down and records its
  exit; four arms (`fake-responder`, `registered-port`, `wrong-expect`, `no-teardown`). Evidence:
  `tools/round78-live-reconcile.py`, `.ufo/waves/round-78/measured/after/c3-live.json`.
- **Frontier.** S551 (git-rev-parse `--verify`, tier A docs, located 18-word quote) and S552 (own-work
  tier A, the round-78 instrument class) admitted; the `git-cat-file` candidate rejected as a duplicate
  of S071/S083 with its flip; two knowledge entries admitted; KQ129 appended to `corpus/QUALITY.md`
  from `considerthese/2026-10-26.md` proposal 3. Evidence: `corpus/SOURCES.md:303-304`,
  `corpus/lessons/round-78.md` §Gate, `corpus/QUALITY.md` §Criteria added — round 78.
- **Gate and tip state.** `PRE_REPORT round=78 arms=9 failed=0 uncommitted=0` at `rev=2842ad29`, exit 0;
  selftest `PRE_REPORT_SELFTEST pass=22 fail=0`. The round-77 register counter is green at the tip
  `22cce544`: `events=250 … exempt=60 … unaccounted=0 … rotation_safe=1`. Evidence:
  `.ufo/waves/round-78/measured/after/gate-run.out`, `gate-selftest.out`, `SCORECARD.md` §Round 78
  §Gate and tip state.
- **Post-data correction (disclosed).** C1's F2 derivation read the worktree SCORECARD; this round's own
  record commit adds three capability rows, so F2 printed `capabilities=37/max-round=78` at the tip and
  the counter reported `mismatches=1`. F2's subject is the sealed round-77 table, so the derivation was
  corrected to `git show <sealed>:SCORECARD.md`; `PREDICATE`, target and arms unchanged and green.
  Evidence: `tools/round78-selfrecord-round77.py:390-396`, `corpus/lessons/round-78.md`
  §Post-data correction.
- **Domain observation (not a claim).** An unregistered host listener was live during the round:
  `127.0.0.1:1234`, a `llama.cpp` router serving four LFM3 ids (`MODEL_OK` under a wildcard expectation).
  It is recorded as an observation and not adopted into the registry (admitting a consumer pin is
  operator-owned). Evidence: `.ufo/waves/round-78/measured/observation/unregistered-1234.out`.
- **Wave and dead seats.** Nine seats returned empty: EX02 (module landed, no rows/receipts), EX03
  (module and receipt landed), SC01 (evidence only, no SOURCES append), SC03 (SKILL/README edits landed),
  CN01/CR01/CR02/MT01 (nothing landed), RV01 (13 independent receipts, no report). Their landed files are
  used only where they re-derive; the L1 appended the three register rows, applied the four repairs, ran
  the three frozen commands, the controls and the gate. **No attack certification is claimed.**
  Evidence: `.ufo/waves/round-78/w1-results.json`.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only
  orchestrator-owned `.scratch/*`, sibling lanes' reports and a pre-existing 24-byte `after` file whose
  content names no lane or round. Nothing was copied or deleted.

## Landed changes

Every change ties to the LOG §Round 78 entry (`LOG.md:3169`); the record's canonical capability list is
`SCORECARD.md` §Round 78, and the wave evidence is committed under `.ufo/waves/round-78/`.

| Change | Commit |
|---|---|
| Freeze: claims plan, pre-freeze receipts (`stale=4`, `unaccounted=3`, `model_ok=0`), control | `d015a178` |
| Freeze amendment: append-only-safe F4/F5 derivations, fixed value strings (pre-dispatch) | `11f46d64` |
| Wave 1 spec and dispatch (12 seats, attack 4/12) | `0f56ad5a` |
| Wave 1 ready handoff | `2bd07a8a` |
| Three counters, four repairs, two knowledge entries, S551/S552, three exempt rows | `773c8abe` |
| Claim receipts at `773c8abe` (three frozen lines, three green selftests) and wave evidence | `098c306f` |
| SCORECARD record, head re-derivation (37 capabilities, round-77 closure pointer), PROVINCE instruments | `4048b44a` |
| LOG entry and freshness run-fact repair (exact selftest line for the round-41 reconciler) | `590e4f38` |
| Hold the superseded head bytes; account the freshness repair event | `22cce544` |
| Gate selftest receipt (`pass=22`) | `2842ad29` |
| Green pre-report gate receipt (9 arms, 0 failed, 0 uncommitted) | `354d858f` |
| Record the green gate and the tip accounting state | `fa65ce2c` |
| F2 derivation moved to the sealed record (transcription bug disclosed) | `381b53dc` |
| Disclose the F2 correction in record and lesson; C1 tip receipt | `979aa9db` |
| Refresh the C3 receipt from the tip run | `7a3cd982` |

Remote check: `git ls-remote origin refs/heads/master` →
`7a3cd98243b69fcbee0cc9e31878782bd8459320`, equal to local `master`.

## Before → after measurements

| Claim | Counting command | Before | After | Measured revision |
|---|---|---|---|---|
| C1 calibration | `python3 tools/round78-selfrecord-round77.py --repo .` | exit 1 `SELFRECORD_R77_ENUM claims=6 stale=4 corrected=0` (`measured/before/c1-facts.out`) | exit 0 `SELFRECORD_R77 claims=6 mismatches=0 corrected=4 unbacked=0` (`measured/after/c1-facts.out` at `773c8abe`; re-derived at the tip in `measured/after/c1-facts-tip.out`, `rev=381b53dc`) — **VERIFIED**, with the F2 correction disclosed | `773c8abe` → `7a3cd982` |
| C2 freshness | `python3 tools/round78-append-registers.py --repo . --to c62ffd3a…` | exit 1 `APPEND_REGISTERS … events=248 accepted=53 exempt=56 … unaccounted=3` (`measured/before/c2-append.out`) | exit 0 `APPEND_REGISTERS to=c62ffd3a… events=248 accepted=53 exempt=59 permitted=28 out_of_region=4 restored=99 disclosed=5 unaccounted=0 introductions=1/1 rotation_safe=1` (`measured/after/c2-registers.out`; re-derived at the tip with `OUT_OF_POPULATION rows=1` and the same frozen line) — **VERIFIED** | `773c8abe` → `7a3cd982` |
| C3 operability | `python3 tools/round78-live-reconcile.py --repo .` | `registry_rows_evaluated=3 model_ok=0 drift=3 exit=2` (`measured/before/c3-noserver.out`) | exit 0 `LIVE_RECONCILE rows=3 model_ok=1 mismatch=1 dead=1 probe_exit=2 runtime=llama.cpp served=stories260K` (`measured/after/c3-live.out`) — **VERIFIED** | `773c8abe` → `979aa9db` |

Selftests: `SELFRECORD_R77_SELFTEST pass=8 fail=0`, `APPEND_REGISTERS_SELFTEST pass=7 fail=0`,
`LIVE_RECONCILE_SELFTEST pass=4 fail=0`. Controls that skip the claimed work: C1 with the four repairs
reverted `mismatches=4 corrected=0` exit 1 (`w1/EX01C1Selfrecord/clone-norepair.out`, run by the seat);
C2 with the three rows removed `unaccounted=3` exit 1 (base receipt); C3 with no server `model_ok=0
drift=3` (base receipt). Freeze divergences are recorded in `SCORECARD.md` §Round 78 and are not
rewritten: the C2 predicate sentence vs scope ruling (b); the plan's first freeze carrying a
41-character revision token that no object answers (L1 transcription; caught pre-dispatch by the
enumerator and fixed in `11f46d64`); the F3 tally source; and the F2 post-data correction.

## Sources & frontier

- Census before → after, same command with exit codes:
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`
  → **before exit 0** over **290 rows** (A 275 / B 11 / C 4; mined 261, queued 8, rejected 21);
  **after exit 0** over **292 rows** (A 277 / B 11 / C 4; mined 263, queued 8, rejected 21).
  Counting: `scripts/sources-census.sh census --file corpus/SOURCES.md`.
- Rows added by tier: **S551** tier A (docs, git-rev-parse `--verify`, admitted with an 18-word located
  quote at `Documentation/git-rev-parse.txt---verify`, opened 2026-11-04, retained copy sha256
  `00e3b1aa…`) and **S552** tier A (own-work, the round-78 instrument class). One reject: the
  `git-cat-file` candidate is a duplicate of S071/S083 (flip recorded in the lesson's Gate).
- Rows touched old→new: none. `S549` keeps its round-77 `rejected` status; no `status`/`recheck`/`used-by`
  cell changed.
- Frontier advanced: two knowledge entries admitted on ground the coverage map did not hold —
  `corpus/knowledge/append-registers-at-the-tip.md` and `corpus/knowledge/live-reconcile-trial.md` (both
  cite S552; the first also names S073/S175 in prose) — and three capabilities entered the repertoire
  with passing demonstrations (`selfrecord-round77`, `append-registers-tip`, `live-reconcile`).
  `corpus/README.md` gained the round-78 coverage rows and the frontier paragraph.
- The sourced claim is C2's: its knowledge entry cites **S552** and its receipt; the Gate records S551's
  admit and the `git-cat-file` reject with URL, access date and located quote.
- **Assimilation: none adopted.** `merge/kama/` was not re-derived this round: the connector seat
  (CN01) returned nothing, so the id-collision guard, the package rows and the quarantine slice were
  **not** re-run, and nothing was appended from the package. This is reported as a gap, not a pass;
  round 79 owes the guard.
- **considerthese:** `considerthese/2026-10-26.md` proposal 3 (a running count of counters a shortcut can
  satisfy) landed as KQ129 in `corpus/QUALITY.md`, citing the file and date.

## Trend verdicts

- **expansion — improved.** Registry 290 → 292 rows (A 275 → 277, mined 261 → 263), two admitted
  knowledge entries on new ground, three capabilities entering the repertoire with green demonstrations
  (51 filtered entries, up from 49). Bound: the two new entries cite one own-work row and no package
  entry was adopted this round.
- **quality — improved.** Four stale self-descriptions repaired and re-derived at their named
  revisions (gate row, §Round 77 pointer, knowledge provenance, two coverage rows); the gate is green at
  the final tip with a committed receipt; the tip register accounting is green at `22cce544`; the
  do-nothing controls are red on all three claims; the F2 post-data defect is disclosed and corrected
  rather than hidden. Bound: the nine dead seats delivered no attack, and C1's tip re-derivation depends
  on the disclosed F2 correction.
- **discernment — unchanged.** The round kept a rejected row rejected (S549), rejected a duplicate
  (`git-cat-file`) and disclosed its own F2 defect, and it added KQ129; but no non-author spot-check of
  this round exists yet (`corpus/lessons/round-77-verifier-spotcheck.md` is the newest closure), so the
  outside-agreement leg is unproven. Reported honestly as unchanged.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `SKILL.md` sha256 `a50f6f74…` (1736 lines, 48 `## ` headings); this round rewrote the gate registry
  row; no named non-author verifier, so no `[x]`.
- [~] At least one end-to-end domain task executed and logged — the C3 trial executed the lane's core
  verdict against a live pinned child (`measured/after/c3-live.json`), and three instruments ran on
  committed bytes; the registered consumers stay DEAD.
- [~] Instructions executable by an agent without oral context — `plans/round-78-claims.md` is
  self-contained and three seats executed parts of it; nine seats produced nothing, so an independent
  execution review remains open.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` now names the three round-78
  instruments; no serving, routing or credential surface was touched; the unregistered `:1234` listener
  is reported, not absorbed.

## Stale-lane

Respawn-per-round driver; kama has no other open mission. Round 78 is the only round this lane worked;
no round 79 work was started.

## Inherited state

No uncommitted lane-authored leftovers at start (tree clean, `jj-lane.sh state` ahead=0 behind=0).
Files not authored by this round (`.ufo/waves/round-77/*`, fleet `.scratch/*`, sibling reports) were
read, never edited.

## Tool installs

None. No pacman, `uv`, `npx` or binary install ran this round (pacman remains paused per the addendum
guard).

## L0 questions

None filed this round: no operator-owned decision blocks the claims. The open `MISSION.md` axes conflict
(`.ufo/l0-questions.md:145`) and the round-16/60/65 fixture L0s remain as filed. The unregistered
`:1234` listener is reported as an observation; admitting a consumer pin is operator-owned.
