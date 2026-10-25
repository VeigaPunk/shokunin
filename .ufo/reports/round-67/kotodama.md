# kotodama - round-67 report

Lane tip (lands+records): `ecbb28517030ebf7b7afe3d7bee1de3efd44be63`
Per-claim lands chain (R67-M7 resolution): A_r `c5f099211e1d6c095e7c59edbd05c0043b4b95fc` (repairs + r66 dispositions) → A_c `c58eb84b6359b30e6930d6e240c574f678c686f9` (claim C lands) → A_ca `e7e17af06ea35c5846e1c72280af0b2f107feb16` (claim Ca lands + records-1) → records-2 `ecbb2851` (direct child of A_ca).

## Work performed

Three declared claims (claims.json, frozen pre-data at `b78f8b8e`, counter fixes at `c5f0992`):

1. **C — coverage (sourced register)**: medicine / healing / physician / remedy register was unowned at base (0 word-bounded filename owners, `.ufo/waves/round-67/rows/ScoutGapMed/gap.md` re-derived) → landed `corpus/knowledge/culture-material/medicine-healing-codes.md` supported by exactly 24 registry rows S805–S828, each cited once. Verdict: **ACCEPT-C-67 PASS** at lands `c58eb84b` — 14/14 legs PASS (`reports/round-67/telemetry/final-measures-c.txt`, stamped==evaluated inside a materialized clone per QUALITY 19).
2. **O — operability (capability acquisition)**: `tools/check-receipt-seq.py` — the R66-D3 fix as a tool: `--lands` evaluates receipts over committed bytes (`git show`, never a moved worktree, `moved_past` flag), header equality stamped/evaluated/measured + tree + counter sha256, `--topo` carrier-parentage post-records, `--selftest` 14/14; five pinned mutants under `.ufo/waves/round-67/stage/mut-o/`. Verdict: **ACCEPT-O-67 PASS** at lands `c58eb84b` — 9/9 legs PASS incl. R66 re-derivation (`reports/round-67/telemetry/final-measures-o.txt`).
3. **Ca — calibration (R66-D1..D5 dispositions + sequencing protocol)**: D1 wave-66 evidence made durable via committed manifest + curated bundle (194 files, all 63 seat reports); D2 census E12×23 moved into Registry + E11 S753 used-by `—` + status `rejected` (exit 0); D3 receipt lands-sequencing protocol landed across all three counters + QUALITY criterion 19; D4 LOG.md/SCORECARD.md round-66 entries restored; D5 first-class rejected rows S801–S804 + S829–S832 (9 today-opened rejects at census). Verdict: **ACCEPT-CA-67 PASS** at lands `e7e17af0` — 9/9 legs PASS incl. QUOTES gate_ids=24 clean (`reports/round-67/telemetry/final-measures-ca.txt`).

## Landed changes

- `c5f0992` — repairs: SOURCES.md E12/E11 fixes, S801–S804 rejected rows, LOG/SCORECARD r66 backfill, QUALITY c19, accept-ca rev1 (QUOTES capture-group fix), r66 wave manifest + bundle (LOG.md round-67 entry; dispositions in `reports/round-67/dispositions/r66-wave-evidence-manifest.txt`).
- `c58eb84b` — claim C lands: entry + 24 rows + README index (34 culture-material / 241 entries) + S753 cell repair.
- `e7e17af0` — claim Ca lands + records-1: claims.json lands-commit note, C/O receipts, `corpus/lessons/round-67.md` (Gate 32 rows, mistakes R67-M1..M9), S829–S832, LOG/SCORECARD r67 entries, `.ufo/waves/round-67/` evidence.
- `ecbb2851` — records-2: `final-measures-ca.txt` + `post-records.txt` (C/O carrier topo PASS; ca carrier verified at tip post-landing: `carrier=ecbb2851 parent=e7e17af0 stamped=e7e17af0`).

## Before → after measurements

- **C** — `python3 -B reports/round-67/accept-c.py --root <clone> --lands c58eb84b…`. Before at base `ad5b52b0` (`telemetry/dry-run-c.txt`): FAIL on base bytes (FILE/SET/ROWS…). After at `c58eb84b` (`final-measures-c.txt`): all 14 legs PASS — FILE lines=42, SET missing=[], HOSTS=13, LINK/CAPTURE/TOPIC clean. Registry rows 724 → 752 at A_c (`git show <rev>:corpus/SOURCES.md | grep -c '^| S[0-9]'`).
- **O** — `python3 -B reports/round-67/accept-o.py --lands c58eb84b…`. Before (tool absent at base, `dry-run-o.txt`): FAIL. After (`final-measures-o.txt`): SELFTEST 14/14, LANDS exit=1 moved_flag=True, TOPO healthy=0 wrong=1, MUT 5/5, R66 bad=[] carrier=4589ebdd parent_of=65fe8572.
- **Ca** — `python3 -B reports/round-67/accept-ca.py --lands e7e17af0…`. Before (`dry-run-ca.txt` at base): FAIL (D1 manifest_absent, D2 E12×23, SEQ counter legs, QUOTES). After (`final-measures-ca.txt`): D1 includes=194 seats=63, D2 census_exit=0 E_lines=0, D3/D4/SEQ/CRITERION/QUOTES PASS.
- Do-nothing controls at base all FAIL (`telemetry/controls-{c,o,ca}.txt`); frozen predicates cannot be passed by inaction.

## Sources & frontier

- Rows: `git show <rev>:corpus/SOURCES.md | grep -c '^| S[0-9]'` → **724 at base `ad5b52b0`, 756 at tip `ecbb2851`** (+32). Added: 24 mined rows S805–S828 (tier A 18, B 6; kinds: paper 12, docs 11, book 1; all opened 2026-10-24, used-by the medicine entry) + 8 first-class rejected rows S801–S804 / S829–S832 (tier A 2, B 4, C 2; each carries `REJECTED: …; flip:` teaches).
- Rows touched old→new: S753 status→`rejected`, used-by `-`→`—` (generic mutable cells; E04 exemption for the rejected-pair); E12 ×23 rows moved Leads→Registry unchanged.
- Census: `sources-census.sh validate --file corpus/SOURCES.md` → start `EXIT=1` (E12×23 + E11, `telemetry/census-start.txt`) → end `exit=0` (accept-ca D2 leg at lands).
- Frontier advanced: medicine/healing register 0 filename owners → owned entry (knowledge files 240 → 241); rejected rows promoted from untracked fragments (r66) and new gate rejects (r67) to durable registry rows.
- Mined mistakes: R67-M1..M9 (`corpus/lessons/round-67.md` `## Mistakes`).

## Wave prepared status

One v2 wave of 64 seats in a single task call; 63/64 returned reports under `.ufo/waves/round-67/w1/` (ScoutGapMed delivered its finding as `rows/ScoutGapMed/gap.md`). All 24 row fragments + 4 reject fragments + 8 row-seat rejects.txt delivered — no dead row seat, no claim shrink; late-landing fragments (S807/S808/S827/S828) arrived inside the round window. Wave-67 evidence committed at `e7e17af0`; wave-66 evidence made durable via manifest + curated bundle at `c5f0992` (manifest excludes named: scratch clones, mut-c fixture, zero-byte streams).

## Noted

- **Receipt-sequencing root cause fixed (the round's reason to exist)**: r65 = wrong anchor (hard-derived `main^`), r66 = wrong time (carrier leg at lands sees an unborn records commit). Protocol now: REQUIRED `--lands` + stamped==evaluated STAMP + evaluations inside materialized clones + carrier-parentage as post-records `--topo` evidence. All three r67 receipts' carriers verified: c/o `e7e17af0^==c58eb84b`, ca `ecbb2851^==e7e17af0`.
- **R67-M2 (instrument regression, fixed pre-data)**: rev0 accept-ca QUOTES put `S` inside the capture group → `gate_ids=0` forever; fixed to `\b(S8[0-2]\d)\b`, counter re-frozen sha `5382ffed`, base control re-run.
- **R67-M7 (resolved as per-claim lands separation)**: C's APPEND bound (S805–S828 + S801–S804 only) conflicts with Ca needing ≥6 today-opened rejects — resolved by lands order A_r < A_c < A_ca, no counter widening; claims.json records the amendment (C's lesson entry completes at A_ca per CriticFrontier F7(iii)).
- **Fragment repairs at integration**: S813's fragment asserted the opposite of its source (recast to the real quote); S814 teaches over-reach trimmed; S824 teaches→quote restatement rewritten; S829/S830 teaches cells >240 chars rewritten; S753 disposition reshaped to the frozen APPEND mutation rules (R67-M8/M9).

## Trend verdicts

- **expansion: improved** — knowledge files 240 → 241, registry 724 → 756 (+32 rows incl. 8 first-class rejects), one new sourced register landed and PASSed its frozen predicate at its own lands.
- **quality: improved** — the r65/r66 rejection class is now enforced by a runnable tool + QUALITY criterion 19; all three receipts carry stamped==evaluated headers and post-records carrier proof; census clean 0.
- **discernment: improved (author-side)** — eight rejected rows carry real `REJECTED:/flip:` reasoning; integration caught one source-inverted fragment and two over-reach teaches cells that mechanical legs missed; pre-data critic/revenger seats found real defects (M2 capture-group, M7 lands-bound collision, dirty-worktree stamp gap recorded for a future round).

## SHONEN

- [~] Box 1 — `SKILL.md` decision tables / error patterns / checklist; sources in `corpus/SOURCES.md` (lane assertion, no non-author verifier on record).
- [~] Box 2 — end-to-end work and measurements logged in `LOG.md` Round 67 and `SCORECARD.md` Round 67; receipts under `reports/round-67/telemetry/`.
- [~] Box 3 — counters + checker executable from repo paths: `reports/round-67/accept-{c,o,ca}.py`, `tools/check-receipt-seq.py` (`--selftest` 14/14), `tools/check-gate-quotes.py` (0 findings on the lesson).
- [~] Box 4 — PROVINCE scope holds (depth+coverage, culture-material register); adjacent partial owners named one-way in the entry and README (bathing-and-body-hygiene, scent-perfume-aromatics, myth-symbol apotropaic purity).
