# kama — round 80 (attempt 1)

Lane: kama (`/home/vgpnk/Projects/shokunin/kama-shokunin`). Base `c45fc7d1a8427e9c98a9dd7befa542c7b5caed38`.
Frozen plan `plans/round-80-claims.md` (freeze `fe7b978013bd1aa6d67a7e0fbf6369b8d7a9b023`). Assigned axes
(`shokunin.conf` kama row): operability + calibration. Sealed revision for C1:
`a9b4543f14625d0f37daa42ef664ee6f6ea975ea` (the round-79 record tip the round-79 verifier spot-check graded).

## Work performed

Three declared claims on three distinct axes, each with its own falsifiable before→after and its own
counting command. C1 works calibration (7), the lowest assigned axis, below the saturation line (8/10), so
the stagnation nudge is inactive. No claim is exploratory. Wave shape: **one v1 wave, 13 seats**, roles
4 executor / 2 scribe / 2 scout / 1 connector / 1 reviewer / 2 critic / 1 mutation-tester (attack 4/13 =
31 %); no residual call; round total 13. The §3 planner seat is held by the L1 (the validator rejects a
`planner` item; the plan data-walk rode scout items SR01/SR02).

- **C1 calibration — the round-79 self-record's six declared facts re-derive, or are answered by dated
  value-bound corrections.** New instrument `tools/round80-selfrecord-round79.py` reads each fact at the
  sealed revision with `git show`, re-derives it at the tip, and grades one committed
  `corrected F<n> old=… new=… at=… date=…` block per stale fact whose `new` equals the tip value
  (`corpus/lessons/round-80.md` §Corrections). Evidence: `SELFRECORD_R79 claims=6 mismatches=0 corrected=3
  unbacked=0`, exit 0 (`.ufo/waves/round-80/measured/after/c1-green.out`, rev `08eb6949`);
  `SELFRECORD_R79_SELFTEST pass=11 fail=0`.
- **C2 freshness — every pinned serving-engine ref the lane holds carries a dated, re-derivable relation
  row.** New `registry/engine-pin-relations.tsv` (five rows: llama.cpp `b11755`, the S553 commit anchor
  `39febd2a` = tag `b11963`'s peeled commit, kengaku's S178 tag `b7200`, sglang `v0.5.22`, vllm
  `v0.32.0`) and `tools/round80-engine-pin-relations.py`, which re-derives every `newest`/`newer`/`relation`
  cell from the committed `git ls-remote --tags` lists under `measured/after/c2-tags/`. Evidence:
  `PIN_RELATIONS engines=3 refs=5 unexplained=0`, exit 0 (`measured/after/c2-relations.out`);
  `PIN_RELATIONS_SELFTEST pass=12 fail=0`.
- **C3 operability — the `registered` census class is proven on a second engine fixture and its engine
  coverage is a register.** New `tools/round80-ollama-census.py` starts the pinned Ollama v0.40.11 child on
  a free unregistered loopback port under a scratch HOME/model store, creates one model from the lane
  fixture GGUF, drives both registry legs through `bash tools/kama-probe.sh listeners`, tears the child down
  and checks port closure; `registry/unregistered-class-engines.tsv` registers each engine with its receipt.
  Evidence: `OLLAMA_CENSUS port=54939 engine=ollama unregistered=1 governed=1 class_missing=0`, exit 0
  (`measured/after/c3-ollama-census.out`; receipt `c3-ollama-census.json`, teardown
  `returncode=0 port_closed=true`); `CLASS_ENGINES engines=2 verified=2 stale=0`, exit 0
  (`measured/after/c3-audit.out`); `OLLAMA_CENSUS_SELFTEST pass=12 fail=0`.
- **Round-79 routed defects R79V1–R79V7 disposed** (SCORECARD §Round 80, "Routed-defect dispositions for
  the prior record"): V1 banner/operability row re-derived plus an appended correction subsection; V2 the
  appended `LOG-CORRECTION round=79 claim=C2 verdict=not-verified`; V3 the `round79-selfrecord-round78.py`
  fact docstring; V4 S556 files the `docs/preset.md` rejection with its flip; V5 the C3 control re-run from
  `git show 7a3cd982:tools/kama-probe.sh` (sha256 `4393ab81…`); V6 S555 supersedes S553's anchor; V7 the
  gate docstring's arm list aligned with `ARM_ORDER` (ten arms) and the validate-warning inventory stated.
- **Round-79's report-gate defect repaired**: `tools/round78-live-reconcile.py`'s selftest now writes under
  `TMPDIR` instead of `.ufo/waves/round-78/measured/after/`; red-before receipt
  `measured/defects/r79-live-reconcile-before.out` shows the base module dirtying
  `c3-selftest.{json,out}` in a scratch clone, the after receipt shows `wave-78 dirties: 0`.
- **Frontier step (§2b).** `corpus/SOURCES.md` 293 → 297 rows; `corpus/knowledge/unregistered-class-second-engine.md`
  admitted (`source: S554`) and indexed in `corpus/README.md`; `corpus/QUALITY.md` gains KQ132 from the mined
  `self-record-states-intent` mistake; `corpus/lessons/round-80.md` carries `## Gate` (3 admits, 1 reject,
  each with URL/access date/located quote), `## Corrections` (the three blocks) and `## Mistakes`
  (2 rows incl. this round's own leaked manual fixture).
- **Assimilation (§10):** none. `merge/kama/` was not adopted this round; `considerthese/2026-10-26.md`
  proposal 4 (daily pin-gap line) remains pending — the C2 relation register now gives it a surface.

## Landed changes

Every change is committed in the lane under the lane identity; `LOG.md` §Round 80 carries the narrative
plus the appended round-79 correction entry.

| Commit | What it carries | LOG entry |
|---|---|---|
| `fe7b9780` | frozen plan `plans/round-80-claims.md`, wave-1 spec (13 seats), dispatch payload, ready handoff | §Round 80 |
| `dea7c269` | the three claim instruments, `registry/engine-pin-relations.tsv`, `registry/unregistered-class-engines.tsv`, `corpus/SOURCES.md` +3 rows, `corpus/knowledge/unregistered-class-second-engine.md`, `corpus/README.md`, `corpus/QUALITY.md` KQ132, `corpus/lessons/round-80.md` | §Round 80 |
| `28debbcf` | SCORECARD §Round 80 + corrected banner/axes/planned/retired/saturation, `LOG.md` correction and round entries, the three routed-defect repairs (`tools/pre-report-gate.py`, `tools/round78-live-reconcile.py`, `tools/round79-selfrecord-round78.py`), `tools/round80-selfrecord-round79.py` (sealed-bound F2) | §Round 80 |
| `4ced97ae` | measured receipts at `28debbcf`: C1 green + selftest, C2 relations + selftest, C3 audit/selftest/census JSON, all controls, three committed tag lists, routed-defect red-before/after | §Round 80 |
| `b7d62643` | canonical capability list as of round 80 (43 rows) and the port-free operability run fact | §Round 80 |
| `07ef2adf` | `PROVINCE.md` round-80 note: the two registers, the third grader, the fixture boundary | §Round 80 |
| `b93c73af` | coverage row re-anchored at the new `PROVINCE.md` hash/line count | §Round 80 |
| `5fcef757`, `223c881a` | record-path fixes so the receipt-pointer audit resolves the round's citations under §Round 80 | §Round 80 |
| `84fd2b21` | S557 (Ollama's OpenAI-compatible `/v1/models` at v0.40.11), the entry's `## Round-80 addendum`, the census erratum and the SCORECARD correction | §Round 80 + erratum |
| `97cfec8a` | S557 bounded against the already-held docs-site row S010 (no discovery claim) | §Round 80 |
| `08eb6949` | the two attack findings fixed (C1 correction container, C3 receipt engine token) with new selftest arms; gate prose aligned; SCORECARD tallies updated | §Round 80 + erratum 2 |
| `1bd94657` | the 13-seat wave evidence (`w1/*`, `w1-results.json`, seat reports) and the re-measured receipts at `08eb6949` | §Round 80 |
| `a2af1af5` | the pre-report gate receipt (`arms=10 failed=1 uncommitted=0`) | §Round 80 |
| (wave evidence) | `.ufo/waves/round-80/**` including `w1-spec.json`, `w1-dispatch.json`, `w1.ready.dispatched`, seat outputs, `w1-results.json` | §Round 80 |

Pushed lane hash at report time: `a2af1af59faf6cf66fe854559293c4e4b441aff3` (the pre-report gate receipt names
`1bd94657`; `git ls-remote origin refs/heads/master` printed `a2af1af5…` after the receipt landed).

## Before → after measurements

| Claim | Axis | Before | After | Counting command | Measured at |
|---|---|---|---|---|---|
| C1 | calibration 7 | exit 1 `SELFRECORD_R79_ENUM claims=6 stale=3 corrected=0` (`measured/before/c1-enum.out`; F4 the record's C2 "verified" against its own `failed=1` receipt, F5 `pass=26` vs `pass=22`, F6 the LOG "all verified") | exit 0 `SELFRECORD_R79 claims=6 mismatches=0 corrected=3 unbacked=0` (`measured/after/c1-green.out`) | `python3 tools/round80-selfrecord-round79.py --repo .` | `08eb6949` |
| C2 | freshness 8 | no register at the base (`measured/before/c2-relations-absent.out`: `BASE_REGISTER=absent`); live `pin-watch` `pins=3 current=0 behind=3 missing=0 error=0` | exit 0 `PIN_RELATIONS engines=3 refs=5 unexplained=0` (`measured/after/c2-relations.out`) | `python3 tools/round80-engine-pin-relations.py --repo . --tags-dir .ufo/waves/round-80/measured/after/c2-tags` | `08eb6949` |
| C3 | operability 8 | one engine, no register (`measured/before/c3-engines-before.out`: `CLASS_ENGINES engines=0`, exit 2) | exit 0 `OLLAMA_CENSUS port=54939 engine=ollama unregistered=1 governed=1 class_missing=0` (`measured/after/c3-ollama-census.out`) and `CLASS_ENGINES engines=2 verified=2 stale=0` (`measured/after/c3-audit.out`) | `python3 tools/round80-ollama-census.py --repo .`; `--audit` | `08eb6949` |

Controls that skip each claim's work, each committed red: C1 `--no-corrections` →
`mismatches=3 corrected=0`, exit 1 (`measured/control/c1-score-nocorrections.out`); C2 header-only register
→ `refs=0` exit 1 and a `current` claim for the `behind` llama.cpp pin → `unexplained=1` exit 1
(`measured/control/c2-empty-register.out`, `c2-stale-relation.out`); C3 the pre-class probe →
`class_missing=1` exit 1 and a one-engine register → `engines=1` exit 1 (`measured/control/c3-base-probe.out`,
`c3-one-engine.out`).

Re-run at the final tip (receipt `measured/after/final-tip-recheck.out`, rev named in its header): the
three counters print `SELFRECORD_R79 claims=6 mismatches=0 corrected=3 unbacked=0`,
`PIN_RELATIONS engines=3 refs=5 unexplained=0` and `CLASS_ENGINES engines=2 verified=2 stale=0`, each
exit 0.

**Pre-report gate.** `python3 tools/pre-report-gate.py --repo . --round 80 --tip master` →
`PRE_REPORT round=80 arms=10 failed=1 uncommitted=0`, exit 1 (receipt `measured/gate.out`, rev `1bd94657`). Arms 1–7 and 9–10 are green; arm 8
(`round75-instruments`) is red on `round75-append-accepted.py`, and that red is **inherited plus declared,
never hidden**: round-79's commit `4af44f7` deleted lines in `SCORECARD.md` and `corpus/lessons/round-79.md`,
this round's banner replacement and its pre-commit lesson section add two more events, and no
`registry/append-only-accepted.tsv` row may answer a deletion at or after that register's introduction
(the counter's `precedes` rule). The round names each event under KQ131 instead of booking it as accepted
history; `round75-append-accepted.py`'s own selftest stays green (`APPEND_ACCEPTED_SELFTEST pass=12
fail=0`) and every other arm executes.

## Sources & frontier

Census, same command at both revisions (`scripts/sources-census.sh census --file <blob>`, exit 0 both
times): base `c45fc7d1` **rows 293** (A 278 / B 11 / C 4; mined 264, queued 8, rejected 21) → tip
**rows 297** (A 282 / B 11 / C 4; mined 267, queued 8, rejected 22). Validation:
`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama` → exit 0 (pre-existing `W04`
duplicate-URL warnings and the pre-existing `W01 S481` tier-C-mined warning; no malformed row, duplicate
id or tier inflation).

- Rows added by tier: **A +4** — S554 Ollama `docs/api.md` at v0.40.11 (`GET /api/tags`), S555 supersession
  of S553's anchor, S556 the `docs/preset.md` rejection, S557 Ollama's OpenAI-compatible `/v1/models` at
  v0.40.11 (the route the probe reads). B and C unchanged.
- Rows touched old→new: **none**. No existing row was edited in place; S553 keeps its bytes and S555
  supersedes only its anchor locator. The additions are pure appends (no existing row edited).
- Frontier rows advanced: S553's anchor now resolves to `### GET /models: List available models`, note 1,
  line 2227 (S555); S554 grounds the class's second engine.
- Admitted knowledge: one entry (`unregistered-class-second-engine`, `source: S554`), one coverage-map row,
  one QUALITY criterion (KQ132).
- `SOURCES: unchanged — main-repo lanes hold no corpus/` does **not** apply: this is a child lane and the
  registry moved 293 → 297.

## Trend verdicts

- **expansion — improved.** Net new admitted entry on ground the coverage map did not hold (the class's
  engine-agnostic reading), its `source:` citing mined S554; three admits and one reject filed as rows; three
  capability rows entered (selfrecord-round79, engine-pin-relations, class-engine-register), each
  demonstrated running this round. Bound: one entry, three rows, no package assimilation.
- **quality — improved, bound.** The round-79 self-description's false C2 verdict is mechanically captured
  and repaired value-bound in three places (banner, claim table correction, LOG correction), the three
  routed defects are fixed with red-before/after receipts, and KQ132 cites the lesson. Bound/regression:
  the pre-report gate's arm 8 stays red (inherited `4af44f7` plus this round's own two events); the round
  reports it as debt, not as a green gate.
- **discernment — improved, bound.** The Gate's two admits and one reject were drafted by a seat,
  re-opened by the L1 with its own `curl` receipts, and handed to the non-author closure for the required
  agree/disagree sample; the C1 counter grades the record against its own receipts rather than against
  intent, which is the same discipline applied to this round's own self-description. Bound: the closure's
  spot-check of this round's gate decisions is not yet on record.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists with cited sources →
  `SKILL.md` (48 `## ` sections, sha re-anchored round 78); no named non-author verifier this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md → the Ollama v0.40.11 fixture
  lifecycle (start → model create → two graded registry legs → teardown, port closed) logged in `LOG.md`
  §Round 80 and receipted at `measured/after/c3-ollama-census.json`; author assertion.
- [~] Instructions executable by an agent without oral context → `plans/round-80-claims.md` predicates,
  the three modules' docstrings/`--help` and `measured/` receipts; author assertion.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → `PROVINCE.md` round-80 note plus the connector
  scan `w1/CN01Connector/scan.out` (kengaku/kaidoku share llama.cpp refs; no sibling holds a pin relation
  register or the `registered` class); author assertion.

## Round mechanics, stale-lane and tooling

- **Stale-lane:** this round was dispatched by the hyaku-inline driver at 07:33 (watchdog line
  `launch kama round=80 pgid=1824947 attempt=1`) and is **progressing**: lane commits `fe7b9780` →
  `223c881a` plus measured receipts and wave evidence landed after launch. No other mission of this lane is
  open (respawn-per-round).
- **Wave:** `w1-results.json` carries **13 seats, 13 returned non-empty, 0 empty**; seat roles 4 executor / 2 scribe / 2 scout / 1 connector / 1 reviewer / 2 critic / 1 mutation-tester; every seat wrote its report into `.ufo/waves/round-80/w1/`, and the L1 re-derived each finding it used. No seat was replaced; dead seats stay
  dead in the evidence.
- **Tool installs/upgrades:** none this round (no pacman transaction; the host-wide pacman pause is intact).
- **Scratch:** every clone/fixture used `/fast/scratch/hyaku/kama-r80/<seat>/`; the L1 removed its own
  scratch trees, and the one leaked manual fixture (`48175`) was killed and is mined as a mistake.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no kama-round-80 seat
  file at the fleet root: the untracked entries are orchestrator-owned `.scratch/*`, other lanes'
  `.ufo/reports/*`, this report, and a pre-existing 24-byte `after` stray dated 2026-11-03 (not this round);
  `.ufo/l0-questions.md` is modified by another lane. Nothing was copied or deleted.
- **L0 questions opened:** none.
