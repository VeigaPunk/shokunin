# kotodama-shokunin — round 88

author: kotodama lane (L1 `KotodamaR88`, including its dispatched seats),
2026-11-04. Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
branch `main`. Base `4956282281dac1306cfbe59523e46dde99749d75`; executed
pre-dispatch controls `0c8c733088df8c4f06770c9e714360eed7f29272`; claim freeze
`4b76524c51e1c2f76c99eeb3b629cfac08a44a76`; work lands
`a64baad9096954fcbdcf09c4b037f5f955667fc4`; measurement lands
`299991c2ec17b9f4caad968c8407d689849b0be0`; resumed-attempt receipts
`25fc3e7a3ecc7c58be45fcd417117467d56321b2` = lane remote tip
(`git -C <lane> ls-remote origin refs/heads/main` prints it).

This is a resumed attempt of round 88. `.ufo/watchdog.log` records
`lane-dead-no-report kotodama round=88` at 18:02:53 (attempt 1, launched
16:58:39) and two further attempts that died in under a minute (18:03:33,
18:04:12). The earlier attempt had already frozen the claims, run the wave and
landed the work commits; this attempt re-verified the frozen counter from
committed bytes, landed the measured records, and filed this report.
**Reused:** the frozen predicate/counter/cases bytes, the settled 12-seat wave
and its evidence, the work lands, the round lesson. **Discarded:** nothing of
the earlier attempt; its receipts were re-derived rather than trusted — the
counters, census and misroot sweep were re-run here and committed as
`reports/round-88/final/rerun-{o,d,census,misroot-sweep}.json`.

## Work performed

Declared claims (frozen in `reports/round-88/claims.json`; unchanged after
data):

- **O / operability — capability acquisition: exact-set attestation
  discrimination comparator.** Target: `tools/check-finding-sets.py` scores a
  committed 13-case battery honest 13/13 and four committed counterfeits
  exactly 3/4/4/0, with comparator agreement and a passing selftest.
- **D / depth — numeral-notation two-axis typology** in the already-held
  `corpus/knowledge/linguistics/numerals-and-measures.md`.

Work items:

- Comparator built and landed, not the round counter renamed: runs a named
  trusted-local candidate on salted opaque filenames and compares rc plus
  exact finding-id and id/record-pair sets; registered in the SKILL gates
  table at `SKILL.md:768` and described at `SKILL.md:41`; corpus index row at
  `corpus/README.md:909`. Its own subprocess selftest is 16/16 (honest
  positive, four forgeries refused, six malformed outputs failing as cases,
  one hang timeout, three usage refusals) —
  `python3 -B tools/check-finding-sets.py --selftest --work <existing-dir>`.
- Frozen 13-case battery and four counterfeits committed under
  `reports/round-88/cases.json` and `reports/round-88/controls/`; the
  inherited r87 counter's survivors are measured at
  `reports/round-88/pre-dispatch.json` (shotgun-all-labels, extra-id and
  filename-only each 12/12).
- Notation section landed: exactly one
  `## 4b. Numeral notation: two axes, five types, and their trade-offs`
  heading, 5 data rows over 4 columns, entry growth 7997 bytes, plus a worked
  NON-CANON 276/206 design with independently taught readers
  (`reports/round-88/notation-trial.json`, `"passed": true`).
- Sources opened and gated: S931 A/mined (Chrisomalis, Terrain 70),
  S932–S933 B/mined (MacTutor Babylonian/Egyptian numerals), S934 A/mined
  (S929's complete boundary quote, prospective correction only), S935
  C/rejected (filename oracle). Gate rows, locators and ≤25-word quotations:
  `corpus/lessons/round-88.md` `## Gate`; L1's own located quotations in
  `reports/round-88/evidence/l1-quote-locations.json`.
- Discernment work: QUALITY criterion 35 grounded in an executed false-green
  probe (`reports/round-88/counter-selftest-false-green.json`,
  `probe-counter-selftest.py` exit 1), and six mistakes R88-M1–M6 mined in
  `corpus/lessons/round-88.md` `## Mistakes`.
- Re-verification on this attempt: both frozen counters, the census and the
  misroot sweep re-run against a `git clone --shared` checked out at the lands
  revision with `KOTODAMA_ROOT` set (`reports/round-88/final/rerun-*.json`).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain`
  shows no untracked fleet-root file naming kotodama round-88. The stray
  `after` file (24 bytes, mtime 2026-11-03 20:05, before this round launched)
  is another lane's; `.scratch/` entries are orchestrator-owned. Nothing
  copied, nothing deleted (`reports/round-88/final/rerun-misroot-sweep.json`).

Round shape: **one v1 wave, 12 seats**, no residual and no replacement —
3 executor (`ExecBattery`, `ExecControls`, `ExecReceipts`), 2 scribe
(`ScribeNotation`, `ScribeRowsLesson`), 2 scout (`ScoutSources`,
`ScoutProtocol`), 1 connector (`ConnectorScope`), 1 reviewer (`ReviewerO`),
1 critic (`CriticD`), 1 mutation-tester (`MutationBattery`), 1 sentinel
(`SentinelFrozen`). Canonical attack share 3/12 = 25 % plus one additional
sentinel. Validated under `scripts/hyaku/ufo-wave-policy.json` (band 8–16);
`w1-dispatch.json` carries 12 tasks, `.ufo/waves/round-88/w1.ready` names L1
`KotodamaR88`. **Dead seats: 4** — `ReviewerO`, `CriticD`, `MutationBattery`,
`SentinelFrozen`, all on the provider with
`402 Upstream request failed: Insufficient account funds (type=server_error)`,
no deliverable; they stay dead in the evidence and were not replaced
(`reports/round-88/provider-deaths.json`). Eight seats delivered reports.
WAVE-DONE was received before integration (`reports/round-88/wave-done.json`).
L1 holds the planner seat; `ScoutProtocol` carried the bounded planning
data-walk. The formal L2-planner conflict stays open (L0 `kotodama | round-86`).

## Landed changes

Every change below is inside the lane repo and is named in the round-88 LOG
entries (`LOG.md`, the `Round88` block appended after the wave).

| change | LOG entry | commit |
|---|---|---|
| Pre-dispatch controls: comparator absent at base; inherited counter accepts three counterfeits 12/12 | LOG round88 controls paragraph | `0c8c7330` |
| Frozen claims O/D, `measure88.py`, cases, separability checker | LOG round88 freeze paragraph | `4b76524c` |
| `tools/check-finding-sets.py`, `reports/round-88/controls/*`, `cases.json`, numerals §4b, S931–S935 rows, SKILL/index/lesson updates, wave evidence | LOG round88 integration paragraph | `a64baad9` |
| SCORECARD measured section + comparator capability row, LOG final-measurement entry, `final/` receipts, census-end, provider deaths, notation trial, settled wave summary | LOG final-measurement entry | `299991c2` |
| Resumed-attempt re-run receipts (`final/rerun-*.json`) | same LOG entry (re-verification) | `25fc3e7a` |

Frozen bytes were not rewritten: `reports/round-88/measure88.py`
(SHA256 `5a80a439…bd995e7`), `claims.json` (SHA256 `50a7f107…`), `cases.json`
(SHA256 `188c4b27…`) and `tools/check-attestation-packet.py`
(SHA256 `4abcbbd0…`) are equal at freeze and at lands
(`reports/round-88/final/noharm.json` `pins`).

## Before → after measurements

Counter: `python3 -B reports/round-88/measure88.py --root <clone at lands>
--base 4956282281dac1306cfbe59523e46dde99749d75 --lands
a64baad9096954fcbdcf09c4b037f5f955667fc4 --claim <O|D> --work <existing-dir>`
with `KOTODAMA_ROOT=<clone>`; measured against `a64baad9`
(receipts re-derived on this attempt at `25fc3e7a`).

| claim | before (base) | after (lands) | verdict |
|---|---|---|---|
| O / operability | `tools/check-finding-sets.py` absent (`git show base:…` fails); inherited counter accepts shotgun-all-labels, extra-id, filename-only at 12/12 each (`reports/round-88/pre-dispatch.json`) | committed comparator: honest 13/13, constant-pass 3, shotgun-all-labels 4, extra-id 4, filename-only 0; comparator agreement `[13,4]`; battery selftest exit 0; **PASS 9/9** | verifies |
| D / depth | heading count 0; S931–S933 absent from entry and registry; growth 0 bytes | heading 1; rows 5; columns 4; cited new ids 3 (S931 A, S932 B, S933 B, all mined); growth 7997 bytes; **PASS 7/7** | verifies |

Separability (each claim measured with only its own paths overlaid on the
freeze tree): O rc 0 at sandbox `bb442acf` with only
`tools/check-finding-sets.py`; D rc 0 at sandbox `c2ba8080` with only
`corpus/knowledge/linguistics/numerals-and-measures.md` and
`corpus/SOURCES.md` (`reports/round-88/final/separability.json`).

Disclosed instrument limits (not repaired inside the frozen counter): the
frozen `measure88.py --selftest` exits 0 while a FileNotFoundError child is
blessed (`counter-selftest-false-green.json`), so the frozen D command omits
its required `--work` and is an input-contract defect (`final/declared-d-missing-work.json`,
rc 2); the supplied-work measurement above is disclosed, not backdated.
Duplicate multiplicity is deliberately ungraded, and a content-memorising
candidate would survive this finite case set.

## Sources & frontier

Census command (run at round start and at round end):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
```

- **Before:** exit 0 (`reports/round-88/census-start.json`), worktree run.
- **After:** exit 0 (`reports/round-88/census-end.json`; re-run this attempt
  → exit 0, `final/rerun-census.json`), final line
  `kotodama ok /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`.

Rows before → after: **854 → 859** (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'
corpus/SOURCES.md` at base and at lands). Added by tier: **A +2**
(S931, S934), **B +2** (S932, S933), **C +1** (S935, rejected). Status:
mined 753 → 757, queued 58, rejected 43 → 44
(`reports/round-88/final/registry-counts.json`). Rows touched old→new:
**none** — every pre-existing row keeps its status, recheck and used-by
cells; S934 is a new row that supersedes S929's *quotation only* and leaves
S929 and its historical lesson unchanged.

Frontier rows advanced: the notation entry's one-line bullet became the §4b
two-axis/five-type cost sheet (5 rows, 4 columns, 7997 bytes of growth) on
ground the lane did not hold; the registry's frontier gained no new topic
partition, so coverage is not claimed as moved. Mistakes mined: R88-M1
(survivor), R88-M2 (vacuous selftest), R88-M3/M5 (reference drift),
R88-M4 (survivor), R88-M6 (attribution) in `corpus/lessons/round-88.md`
`## Mistakes`, each with a captured-by criterion and a fix that can fail.
Sourced claim: **D** rests on S931–S933, all opened this round with the Gate's
access date and located quotations.

Assimilation: none — no shokuknow package append and no `considerthese/`
directory in this lane (bounded sweep recorded by `ScoutProtocol`).

## Trend verdicts

- **expansion: unchanged** — no new topic partition or province surface; the
  comparator enters the repertoire table under operability, and the notation
  work deepens an entry the lane already held rather than adding coverage.
- **quality: improved** — depth and operability both move on re-derivable
  committed bytes: comparator 9/9 with honest 13/13 versus counterfeits
  3/4/4/0, notation 7/7 with 7997 bytes of new method, QUALITY35 grounded in
  an executed false-green probe.
- **discernment: improved (author-side observation)** — four counterfeit
  classes are separated where the inherited counter accepted three at 12/12,
  six mistakes are mined with fail-able fixes, and the frozen instrument's
  own false green is disclosed rather than papered over. No non-author
  sampling is supplied by this round's seats: all four attack seats died on
  the provider, so outside admit/reject judgment remains the closure's.

Stale-lane: respawn-per-round driver; this is the sole kotodama mission open;
no other open mission of this lane is asserted. Tools installed/upgraded:
none.

## SHONEN

- [~] Decision tables / error patterns / checklists / cited sources — SKILL
  gates row `SKILL.md:768` and `corpus/lessons/round-88.md` Gate; author
  assertion, not promotion approval.
- [~] End-to-end domain task executed and logged — LOG round-88 entries plus
  `reports/round-88/notation-trial.json` (276/206 NON-CANON design, passed);
  no historical certification or lore acceptance claimed.
- [~] Instructions executable without oral context — public comparator CLI,
  16/16 selftest and frozen `final/lands-o.json` 9/9; content-memorisation and
  duplicate-multiplicity limits disclosed.
- [~] Province accurate / no cross-domain bleed — `reports/round-88/final/noharm.json`
  (only the declared knowledge path changed, old registry rows unchanged) and
  `ConnectorScope`'s scope receipt; lore/chousa authority retained. No named
  non-author promotion verifier; no box is `[x]`.

Open L0 questions (unchanged, not answered this round): `kotodama | round-51`
(bot-challenge source opening), `kotodama | round-69` (kill-rule versus
predicate conflict), `kotodama | round-86` (L2-planner role conflict). No new
L0 question was needed.
