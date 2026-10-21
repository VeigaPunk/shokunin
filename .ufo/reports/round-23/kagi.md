# kagi — round 23 (hyaku phase 2)

Lane: `kagi-shokunin`. Base `d218603b74099ddca0bd8f869516fc41db0979bf`; measured
lane commit `e1884c6ecb7ccd717965b0d748bc193137118dbf`, final lane commit
`5dd14116f76968f28c6446a9487936a23b1630b3` (helper `landed` lines, pushed).
Build wave: parent-held 66 seats (43 claim-ledger command-row audits + 23 source-row
audits, `parent-build-dispatch.json`). This lane dispatched no second build wave and
remained the sole production writer. Falsify wave: 64 seats, `.ufo/waves/round-23/falsify-spec.json`.

## Work performed

Declared claims (`plans/round-23.md`):

- **C1 calibration, capability acquisition** — outside-closure dispositions.
  `corpus/closure-dispositions.py` parses the round-22 non-author spot-check
  (nine routed defects, five discernment decisions, one adjudication), requires exactly
  one typed disposition per obligation, resolves every `fixed` pointer in-tree, and
  fails on missing/duplicate/unknown obligations or source drift. Verdict: **verifies**.
  `CLOSURE_DISPOSITIONS: CLEAN (obligations=15 fixed=6 reported=3 operator_owned=1
  no_action=5 rejected=0 pointers=15)` exit 0; selftest `PASS (14 cases)` (13 + symlink-escape regression).
- **C2 freshness (D7)** — declared source provenance.
  `corpus/source-fetches.tsv` carries 10 declared captures (S017–S026) over nine distinct
  URLs with request profile, final URL, HTTP status, representation, raw digest, decoded
  byte count, row-identity digest, located quote, normalization and normalized digest.
  `corpus/sources-census.sh` gains fail-closed `SC_FETCH` (coverage, identity, URL, status,
  shape, moving-ref revision, duplicate id) with 12 new selftest cases. SOURCES.md gains
  S024 (Vault KV v2 API), S025 (supersedes S014's locator) and S026 (supersedes S016's
  locator). Verdict: **verifies**, bounded as below.
  `SOURCES_CENSUS: CLEAN (rows=26 A=24 B=0 C=2 queued=1 mined=24 rejected=1
  entries_sourced=4 legacy=21)` exit 0; selftest `PASS (59 cases)`.
- **C3 operability (D9)** — hermetic `cells`.
  `corpus/fixtures/cells-hermetic/` (five files, two local claim rows, two stamp rows)
  plus ledger row `R23-01`. Verdict: **verifies**.
  `CELL_AUDIT: CLEAN (cells=6 row_pointed=6 stamp_pointed=1 uncited=0 missing_ids=0
  rows_run=2 row_deferred=0 row_failures=0 stale_pointers=0 self_skipped=0 orphans=0)`.

Falsification wave (64 seats: 20 reviewer, 10 critic, 20 scout, 4 mutation-tester,
4 revenger, 4 connector, 2 sentinel; no planner swarm role — L1 held the frozen
planner seat). Zero seats were replaced. Integrated findings:

- **Fixed:** census `SUPERSEDED` write after its declaration was deleted crashed every
  `verify` (`S007: unbound variable`, exit 1, no verdict); the dead supersession block
  was removed and the live verdict/selftest re-run. Provenance header still called the
  normalized digest a "stable identity" and still described a removed same-URL rule;
  corrected to a chrome-sensitive point attestation. `S022` location corrected from
  "JWT verification" to the Introduction Note where its quote occurs. Distinct-URL and
  fixture-file counts corrected (9 URLs, 5 files, 2 claims rows, 2 stamps). Closure
  pointer resolution now rejects symlink escapes and catches `UnicodeDecodeError`/
  `OSError` as SETUP. Fixture adjacency lines converted to TAB separators and the count
  row timeout aligned to 30 s. D3's guard wording narrowed (mode token covered; id-shaped
  positional remains routed debt). D9 pointer moved to the executable fixture scorecard.
  Census false-clean attack re-run: deleting all 10 captures yields 10
  `SC_FETCH ... missing-provenance` findings and exit 1.
- **Reported as remaining bounds, not fixed:** C1 pointer proof is presence-only
  (file + anchor substring + id token); its source digest is pinned in the same
  lane-writable JSON; only `fixed` requires the id token. C2 `SC_FETCH` is shape/identity (17 selftest mutants survive; the in-row branch covers 16/26 rows only in the real-tree run),
  not content verification: 16 legacy in-row digests pass on presence and are never
  compared (stated historical bound); quote text and location are not verified against
  the page (a changed-word quote, a blank quote/location, or thin-space-joined words
  pass the ASCII word/shape test); the 59-case selftest does not exercise the in-row
  branch; captures are point attestations. C3 proves the `cells` mechanics, not all 43 row obligations;
  `rows_run` counts selected rows, so only `row_deferred=0`/`self_skipped=0` exclude an
  unexecuted fixture; one fixture stamp (`fx-ok.sh`) is inert because no cell cites it.
- **Inherited, reported unverified:** `R11-08` citations is red at base because the
  round-22 spot-check adds three class-shaped tokens (`CITATION_GATE: BROKEN
  (cites=1257 docs=65 unresolved=3 ephemeral=0 labeled=13)`, exit 1); this round did not
  edit that non-author file and does not credit the row. `cells` `SKIP-SELF` can print
  CLEAN while a cited row is skipped. The single-backslash policy guard accepts one
  backslash. `surface-census.sh` `DEEP` was uninitialised (fixed: `DEEP=""`, so an
  ambient value cannot select `--deep`/op exec). `R18-02` note/selftest gap, `R13-01`
  identity-free count, `R22-03`/`R22-04` case-identity count, and `R11-01 scanned=0`
  tolerance remain debt. Plan wording "for every mined row" was corrected before landing
  to the measured ten active rows; 16 legacy pins stay historical.

Other evidence bullets:

- Census at round start: lane exit 0 `rows=23`; the fleet wrapper then printed five W04
  lines. At round end: lane exit 0 `rows=26`; the fleet wrapper prints seven W04 lines:
  `W04 S019 duplicate url www.1password.dev/brokered-access across scopes`,
  `W04 S020 duplicate url 1password.com/blog/1password-credential-broker-public-preview across scopes`,
  `W04 S021 duplicate url openbao.org/docs/concepts/tokens across scopes`,
  `W04 S022 duplicate url developer.hashicorp.com/vault/docs/auth/jwt across scopes`,
  `W04 S023 duplicate url developer.hashicorp.com/vault/docs/concepts/lease across scopes`,
  `W04 S025 duplicate url openbao.org/docs/auth/jwt across scopes`,
  `W04 S026 duplicate url openbao.org/docs/concepts/tokens across scopes`.
- QM12 safe-row substitute (`.ufo/waves/round-23/final-verification.json`): 45 rows
  considered, 32 pass, 12 skipped by id (R11-01/02/03/04/06, R12-01, R13-03, R15-01,
  R16-01/03, R17-01, R18-01 — host-bound/substrate), one inherited fail (R11-08).
  Recorded measured commit is the verdict file's own `measured_commit: e1884c6e…`.
  No full legacy `verify`/`cells` was run; no host-private gate was executed.
- Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): four
  seat reports had landed at the fleet root (`falsify/RevS019.md`,
  `falsify/ScoutMigration.md`, `falsify/RevW04.md`, `parent-build/ClaimR11X11.md`); each was byte-copied
  into the same lane-relative path under `.ufo/waves/round-23/`, verified with `cmp`,
  then the fleet copy was deleted. Recorded as M23-4. Inherited lane leftovers: none
  for round 23 (attempt 1 was clean); other parent-built reports remain parent-owned
  and uncommitted by this lane.
- Tool installs: none. No pacman transaction. No account/vault/handler action; the only
  network use was `curl` against public documentation.
- Round-22 routing record is unchanged: `CriticNoTrade` produced 130 spawn IDs under 129
  names (fresh `-2` identity), no replacements; this round added no such reuse.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| closure disposition gate + records, source-fetch table, census SC_FETCH, hermetic cells fixture, lesson, SOURCES S024–S026, SCORECARD/LOG/SKILL/prose corrections, stamps, wave specs | `LOG.md` §Round 23 | `e1884c6e` |
| measured verdict with `measured_commit`, corrected provenance header/location, final pins | `LOG.md` §Round 23 | `ea5b7348` |
| migration record (R12-03/R13-01/R21-02/R21-03/R21-04/R22-03 old→new), symlink regression case, stale 47→59 counts, S015 debt | `LOG.md` §Round 23 | `7af07b4d` |
| quote/location bound corrections (declared, shape-checked only; location unverified; blank/thin-space bypass named) and in-row selftest-adequacy bound | `LOG.md` §Round 23 | `284d40e0` |
| removed the contradictory cross-capture equality rule, aligned case counts, S024 frontier-row wording and the KV v2 lead disposition | `LOG.md` §Round 23 | `def9bc2e` |
| D3 relabelled reported, seven-W04 correction, selftest-adequacy bounds, dead-array removal, closure docstring bounds | `LOG.md` §Round 23 | `58bd8d70` |
| W04 base/round-end wording, R13-03 SKIP-SELF semantics, D4 named tuples | `LOG.md` §Round 23 | `57776b28` |
| measured verdict refreshed to the final tree (`measured_commit=57776b28`, R23-02 `fixed=6 reported=3`) | `LOG.md` §Round 23 | `5dd14116` |

## Before → after measurements

| claim | before (base) | after (measured) | counting command | measured against |
|---|---|---|---|---|
| C1 | `test -e corpus/closure-dispositions.py` exit 1; 9 `^- D[0-9]` obligations with no machine record | 15 obligations, 15 dispositions, all pointers resolve | `python3 corpus/closure-dispositions.py`; `--selftest` | `e1884c6e` |
| C2 | `grep -c 'Fetch sha256:'` = 16 of 23; 0 `source-fetches` references in the census | 26 rows; 10 declared captures / 16 historical pins; `SC_FETCH` enforced; 59 cases | `bash corpus/sources-census.sh`; `--selftest` | `e1884c6e` |
| C3 | 0 ledger rows executing `cells` host-free; R13-03 skipped | `R23-01` exact CLEAN line; mutation killed (BROKEN, row_failures=1) | `bash corpus/claim-ledger.sh cells --root corpus/fixtures/cells-hermetic --claims … --stamps … --scorecard … --docs …` | `e1884c6e` |

Supporting counts at `e1884c6e`: `grep -c '^## Round ' SCORECARD.md` = 27;
`grep -c '[^[:space:]]' corpus/stamps.tsv` = 79; `grep -cE '^R[0-9]+-[0-9]+'
corpus/claim-ledger.tsv` = 45; ledger selftest 121 cases; revision audit
`CLEAN (stale=0 missing=0 dropped=0 added=16 invalid=0)`.

## Sources & frontier

Census before (round start): exit 0, `rows=23 A=21 B=0 C=2 queued=1 mined=21
rejected=1 entries_sourced=4 legacy=21` plus the five W04 lines above.
Census after: exit 0, `rows=26 A=24 B=0 C=2 queued=1 mined=24 rejected=1
entries_sourced=4 legacy=21`, same five W04 lines. Command:
`bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi`.

Rows added by tier: S024, S025, S026 — three A/mined correction rows (only the KV v2
API URL is new; 18 → 19 distinct registry URLs). Rows touched old→new: none of
status/recheck/used-by changed on any existing row. Frontier advanced: the round-22
"Vault KV v2 API (version deletion settings)" lead is opened as S024; S014/S016 locator
defects get active superseding rows. New rows are sourced from public pages opened
2026-10-21; quotes and fetch digests are in `corpus/lessons/round-23.md` §Gate and
`corpus/source-fetches.tsv`.

## Trend verdicts

- expansion — **improved**: one demonstrated capability row enters the repertoire
  (closure disposition review); coverage ground is unchanged (three correction rows).
- quality — **improved**: census crash caught and fixed before landing, provenance is
  machine-declared for ten rows, hermetic cells row exists, 32 safe rows pass, inherited
  red rows are recorded rather than absorbed.
- discernment — **improved**: outside D1–D9 became typed obligations instead of prose;
  five falsify seats' defects were integrated and their residual bounds are stated; no
  self-certified outside agreement is claimed. Late falsify reports added a
  QM14 migration record (`expectation-migrations.json`), a symlink-escape
  regression case, and the bounds: `cells` row paths are not contained,
  in-root hardlinks can reach outside inodes, and captures live only in
  declared metadata (no bytes in-lane).

## SHONEN

- [~] SKILL.md decision tables/error patterns/citations — evidence: `SKILL.md` + ledger
  `R11-05`/`R12-02`/`R15-02` (36-case probe count corrected this round); no named
  non-author verifier signature in this report.
- [~] One end-to-end domain task executed and logged — `LOG.md` §Round 23 (gates executed;
  no vault/account task).
- [~] Instructions executable without oral context — `corpus/claim-ledger.tsv` R23-01,
  R23-02; `corpus/closure-dispositions.py --selftest`; `sources-census.sh --selftest`.
- [~] No cross-domain bleed — `PROVINCE.md` unchanged; parent-held findings from sibling
  gates are reported, not absorbed.

Stale-lane: fresh respawn-per-round driver; no other kagi mission is open.
L0: none opened; no operator decision blocks this round.
