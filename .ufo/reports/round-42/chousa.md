# chousa — round 42 report (wave-4 quarantine-first)

lane: chousa · round: 42 (attempt 1) · host: Kimi, fresh L1 (`Kimi fresh L1`) ·
date: 2026-10-24 · lane repo: `/home/vgpnk/Projects/shokunin/chousa-shokunin`

**Round shape.** One v2 wave (policy `scripts/hyaku/ufo-wave-policy-v2.json`, band 64–128),
64 seats, 25 attack roles (39%). Item 10 of the fleet lane-addendum binds this round:
wave-4 quarantine-first — **the lane adopts nothing from its shokuknow package**; it
hand-checks the lane's full absent-defect-register quarantine slice and lands a verdict
per row. No new external fetch was made in this round (the fetch-scope L0 question
`8d77e6c1` is still open); only committed captures and installed copies were re-opened.

## Work performed

**Declared claims (frozen in `corpus/evidence/round42/claims.md` at
`dd63b6cfec5e1eafddb6662fc343e2ff6ab6aedc`, base `872bf3a3507875b382313f955d15960f9638256f`):**

- **C1 — operability** (the lane's lowest scored non-retired axis, 3/10): the lane's
  quarantine scope becomes a runnable, re-derived surface — one committed command
  re-derives the lane's absent-defect-register slice from the read-only register and
  examines every quarantined quote against the capture material already on disk, and the
  derivation is complete, reproducible and control-discriminating.
- **C2 — calibration** (discernment): every row of the slice carries exactly one verdict
  from the frozen vocabulary, that verdict agrees with an **independent** re-examination
  of the row, and it carries a non-empty reason and a non-empty flip condition.

**Work items, each with an evidence pointer:**

- The lane's quarantine scope was **re-derived**, not taken from the register's summary:
  the operator's own recipe yields **24 data rows** (20 of the register's `## Rows`
  table + 4 of its `## Rows whose quotes were NEVER CHECKED` table). The register's
  `## By lane` summary says `chousa 20` and its header says 194 rows / 324 quotes — both
  stale. `tools/quarantine-check.py slice` → `corpus/evidence/round42/receipts/verdict.txt`
  header, `tools/quarantine-check.py digests` → `corpus/evidence/round42/receipts/digests.txt`.
- The runnable gate landed: `tools/quarantine-check.py` (subcommands `slice`, `examine`,
  `verdict`, `digests`) re-derives the slice, parses BOTH register row shapes, resolves
  each cited URL's local capture by the campaign's cache-key convention
  (`sha256(url)[:24]`, read from the campaign's own checker source — **read, never run**:
  it writes into the campaign tree), and classifies each capture's FORM (rendered text,
  `pdftotext -layout` PDF text, binary office decoding, bot wall, missing).
- The examination ran over **43 quarantined quotes in 24 rows**:
  `corpus/evidence/round42/receipts/examine.txt` (15 `no-capture`, 28 `absent`).
- The **adjudication table** landed: `corpus/evidence/round42/quarantine-verdicts.tsv`
  (id · verdict · reason · flip), 24 rows, one per slice row, none omitted. Verdicts:
  **15 `absent`**, **9 `unverifiable`** (S077 bot-wall capture; S095/S096/S120/S125 binary
  office documents never rendered to text; S100–S103 register rows naming no locator),
  **0 `present`**, **0 `mixed`**. No row is called a fabrication on absent evidence.
- The **frozen decision rule** was applied, and the lane found the register's own class
  column unreliable: S077 carries the campaign's `payload-absent` class ("every relevant
  source fetched cleanly") while the local capture of that DOI is a 265-character
  `Client Challenge` page. That is the round's central finding and it is recorded as a
  mistake with its fix (`corpus/lessons/round-42.md` `## Mistakes`).
- The **considerthese proposal** was mined: `considerthese/2026-10-23.md` — "for every
  frozen counter, name the cheapest gate that can score full marks without doing the
  work" — lands as `corpus/QUALITY.md` criterion 60, and both counters carry that line.
- The **one source opened this round** is an installed copy, never a fetch: Poppler
  `pdftotext(1)` → new row **S077** in `corpus/SOURCES.md` (sha256 `50dd56df…`, located
  quote "Pdftotext converts Portable Document Format (PDF) files to plain text.",
  DESCRIPTION, decompressed lines 12–13). It grounds the rule's step 2 (a PDF capture IS
  a text rendering; a binary document never rendered cannot refute a quote).
- Frontier step: `corpus/lessons/round-42.md` (claims + measurements, 4 mined mistakes,
  `## Gate` with candidates/admitted/rejected-with-reason-and-flip, sources opened,
  spot-check status, census before→after); census run at both ends, exit 0 at both.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze: gate tool, both counters, frozen claims, C1 do-nothing control + receipt | `LOG.md` "Round 42" entry | `dd63b6cfec5e1eafddb6662fc343e2ff6ab6aedc` |
| work: adjudication table, C2 control + receipts, lesson, S077 row, QUALITY 59–60, LOG, SCORECARD, wave spec/plan/dispatch evidence | `LOG.md` "Round 42" entry | `e0f4895c48d6c6e739ce9deb614b97c771a3a096` |

`jj-lane.sh` printed `landed e0f4895c48d6c6e739ce9deb614b97c771a3a096` after remote
verification; the freeze commit printed `landed dd63b6cfec5e1eafddb6662fc343e2ff6ab6aedc`.
No raw git/jj mutation was run by this lane; no sibling repo, no fleet script, no prompt
and no MANIFEST entry was touched.

## Before → after measurements

| claim | counting command | before | after | measured commit |
|---|---|---|---|---|
| C1 operability (lowest scored axis, 3/10) | `python3 corpus/evidence/round42/c1-count.py` (do-nothing control: `corpus/evidence/round42/controls/c1-control-before.txt`) | the lane held **no** command that yields its quarantine scope; the slice was a line of a prompt and the examination did not exist (counter cannot run → exit 1) | `SLICE_REDERIVE_MATCH=24/24`, `QUOTES_EXAMINED=43/43`, `REPRODUCIBLE=1/1`, `POSITIVE_CONTROL=1/1`, `NEGATIVE_CONTROL=1/1`, `MUTANT_DETECTED=1/1`, exit 0 | `e0f4895c48d6c6e739ce9deb614b97c771a3a096` |
| C2 calibration | `python3 corpus/evidence/round42/c2-count.py` (do-nothing control: `corpus/evidence/round42/controls/c2-control-before.txt`) | no adjudication existed for the slice (table absent → exit 1) | `VERDICTED=24/24`, `CLASS_CONSISTENT=24/24`, `REASON_NONEMPTY=24/24`, `FLIP_NONEMPTY=24/24`, `VOCAB_OK=24/24`, `DUPLICATE_ROWS=0`, `ROWS_OUTSIDE_SLICE=0`, exit 0; the flipped-row control scores `CLASS_CONSISTENT=23/24`, exit 1 | `e0f4895c48d6c6e739ce9deb614b97c771a3a096` |

The round-1 operability scale is unchanged: **3 → 3 (delta 0)** — its counting command
still prints `VERDICT_BEARING_EXPORTS=3/3`, and `tools/research-gate.sh` is untouched by
this round. The C1/C2 observables sit beside that score, as in rounds 25, 29 and 31–41.

## Sources & frontier

- SOURCES rows before → after: **76 → 77** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`).
- Rows added by tier: **tier A +1** (S077, Poppler `pdftotext(1)`, opened from
  `/usr/share/man/man1/pdftotext.1.gz`, sha256 `50dd56df…`); tier B +0, tier C +0.
- Rows touched old → new: S077 `queued → mined`, `recheck — → 180d`, `used-by — →
  tools/quarantine-check.py, corpus/lessons/round-42.md`. No other row changed.
- Frontier rows advanced: none — **this round advances no coverage-map row**: no
  knowledge entry is admitted (wave-4 quarantine-first), so the coverage map is
  untouched by design. The frontier advance this round is the **quarantine scope
  itself**, which the lane did not hold at all: 24 rows, 43 quotes, now with a command,
  a receipt and a per-row verdict.
- Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin chousa` → exit 0 at round start and exit 0 at round end,
  five advisory W04 warnings (S051, S053, S073, S074, S075) unchanged by this round,
  `ok` both times. Manual census (frozen commands): rows 76 → 77, tier A 70 → 71,
  status mined 52 → 53, malformed rows 0, duplicate ids none, mined used-by paths
  resolve.
- **Assimilation: none** — this round adopts no shokuknow knowledge entry and no staged
  row (item 10, wave-4 quarantine-first). The package's staged ids start at S077, which
  is also the lane's next free id; the operator's collision recipe (0–3 leading spaces,
  the census parser's pattern) was run in scratch, the collision is recorded, and at
  adoption time the package's ids shift by one with every adopted citation re-pointed
  **by document**. No bulk import, no bulk append, no edit to the campaign tree.

## Trend verdicts

- **expansion: improved** — one admitted source row (S077) opened this round from an
  installed copy, one lesson, and one runnable surface the lane did not hold at all:
  the quarantine scope (24 rows / 43 quotes) now has a command, a receipt and a
  per-row verdict. The measure is the new surface, not the row count.
- **quality: improved** — both counters verify against their do-nothing controls
  (C1: 1/12-style control fails at the tool's absence; C2: 23/24 on the flipped row), the
  examination is reproducible byte for byte, and the register's own class column was
  shown to be **unreliable** (S077's "fetched cleanly" capture is a bot wall) — the
  lane's rule now checks the capture's FORM. No admitted entry failed its re-check; the
  table's reasons and flip conditions are non-empty on 24/24 rows.
- **discernment: unchanged** — the round's admit/reject sample has **no non-author
  spot-check**: the wave's seats are author-lane (a seat this lane dispatched is still
  the lane), so nothing here is claimed as externally verified. The lane records that
  the sample is ready for the outside closure instead.

## Wave, seats and dead seats

- Shape: **one v2 wave** (policy v2, band 64–128), spec
  `.ufo/waves/round-42/w1-spec.json` (64 items), validator `plan` and `run` exit 0
  (`w1-plan.json`, `w1-dispatch.json`, schema `ufo-swarm-wave-dispatch-v1`, 64 tasks).
- Seat mix (64): reviewer 6, critic 8, mutation-tester 6, sentinel 3, revenger 2 =
  **25 attack roles (39%)**; executor 17, scout 8, scribe 6, connector 4, simplifier 4 =
  39 build roles. The §3 L2 floor is met inside the wave: connector ≥1, executor ≥3,
  scribe ≥1, scout ≥1, reviewer ≥1, critic ≥1; the **planner seat is the L1** (the
  validator rejects `planner` as a swarm role) with its bounded planning data-walk on the
  scout and connector items.
- Wave slot: `scripts/hyaku/wave-slot.sh acquire chousa round-42-w1 64 3600` →
  `granted lane=chousa wave=round-42-w1 seats=64 live=18 pending=0 cap=256`.
- **Dispatch outcome, reported as observed:** the dispatch was issued on the Kimi
  surface as a single batched AgentSwarm call carrying the validator's `taskCall`
  (`context` + 64 tasks, unchanged). At the round's time budget the AgentSwarm call was
  still being composed by the dispatching session and **no seat had settled**:
  **0 seat reports landed, 0 seats claimed, 0 dead seats** (no seat started, so no seat
  died). Nothing in this report is a prepared-as-dispatched claim: the wave evidence in
  `.ufo/waves/round-42/` is the validated spec, plan and dispatch payload, and the
  registry is present with 64 members and null agent ids. The slot is released with the
  round. The round's two claims do **not** rest on any seat's verdict: both counters were
  run by the L1 against their own do-nothing controls.

## SHONEN

- [~] Real decision tables / error patterns / checklists with cited sources —
  `corpus/knowledge/claim-verification-r2.md` + `corpus/evidence/round42/claims.md`
  (the frozen decision rule and its two named failure modes); no `[x]`: no non-author
  verifier yet.
- [~] An end-to-end domain task executed and logged — `corpus/evidence/round42/receipts/{examine,verdict,digests}.txt`
  (43 quotes examined over 24 rows; every observation re-runnable from the lane root).
- [~] Instructions executable by an agent without oral context —
  `tools/quarantine-check.py --help` + `corpus/evidence/round42/claims.md` (the wave
  context repeats the commands and the absolute paths).
- [~] No cross-domain bleed; `PROVINCE.md` still accurate — `PROVINCE.md` untouched this
  round (its working-copy diff is a mode bit only, inherited, not committed); the
  campaign tree and every sibling repo were read-only; no egress.

## Honesty, inherited state and open questions

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Inherited working-copy state** (not authored by this round, named, not swept):
  `PROVINCE.md` (a mode-bit diff only, `100644 → 100755`), the modified
  `.ufo/waves/round-4{0,1}/w1/swarm-registry.json` files, the rewritten
  `corpus/evidence/round41/receipts/cells/cells.json` (r41's D2: the counter rewrites it
  on every run), and the r40/r41 wave seat reports under `.ufo/waves/round-4{0,1}/w1/`
  (orchestrator-dispatched, not lane-authored). None of these is in this round's commit.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows the
  driver runtime (`.ufo/state/*`, `.ufo/watchdog.log`), an operator file
  (`.omp/mcp.json`), a prior round's wave dir (`.ufo/waves/round-37/`) and two untracked
  fleet-root files, `bm.json` and `live.html` — a Cloudflare challenge page and a
  fetched HTML page. **Neither names chousa or round-42 in its content**, so they are
  not attributable to this lane's seats; they were left untouched (another lane's seat
  may have written them) and are named here for the operator.
- **Tool installs:** none. **Egress:** none — every source opened this round is an
  installed copy or a committed capture; the fetch-scope L0 (`8d77e6c1`) is still open
  and the round routed around it (every row whose source could not be read locally is
  `unverifiable`, never a fabrication).
- **Open L0 question filed this round** (appended to `.ufo/l0-questions.md`): the
  fetch-scope ruling, and the S077 id collision between the lane's next free id and the
  staged package's first id — shall the package's ids be renumbered at adoption time by
  document (the item-10 rule) or by the operator? Nothing in the round depends on the
  answer: this round adopted nothing.
- **Known limits of this round's own claims:** C1 grades the derivation and the
  examination's completeness and discrimination — not the truth of any verdict about the
  live web; C2 grades rule-consistency and completeness of the adjudication, not the
  truth of the underlying "absent" judgement. The `absent` class spans two failure modes
  (the source carries the text and the row quotes it wrongly — measured by the
  longest common run, e.g. S093 79/120 chars — versus the source not carrying it at all,
  e.g. S086 4/46); the split is named as round-43 work in `SCORECARD.md`.
