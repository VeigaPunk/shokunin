# S1MemberRecensus — round-32 script-layer re-census (family S1)

**Seat:** `S1MemberRecensus` (leaf). **Family:** S1 dispatcher core.  
**Lane:** `kumitate-shokunin` HEAD `175de6ba2e9e904010411b19cab27e0af9aad3d4`.  
**Origin:** `/home/vgpnk/Projects/ufo-fsd-alpha` HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9` (`964f443e`).  
**Scope:** live membership + note section honesty only. Registry row / proxy stanza not edited (parent-owned).

## Axes (named, not judged)

- **coverage:** S1 member set vs note `##` sections vs claims gate.
- **operability:** commands are re-runnable; every count carries its command.
- **calibration:** registry line-count cell vs live `wc -l` (drift recorded, not fitted here).

## Files inspected

| Path | Role |
|---|---|
| `kumitate-shokunin/SCORECARD.md` | registry row S1; round-32 `## Planned` |
| `kumitate-shokunin/corpus/README.md` | coverage-map entries citing the five S1 notes |
| `kumitate-shokunin/corpus/knowledge/queue-and-claim.md` | primary S1 family note (sectionized this seat) |
| `kumitate-shokunin/corpus/knowledge/successor-chain.md` | cited S1 note (topic body; no path `##` section) |
| `kumitate-shokunin/corpus/knowledge/enqueue-admission.md` | cited S1 note (marked superseded/historical) |
| `kumitate-shokunin/corpus/knowledge/reconcile-and-cycle.md` | cited S1 note (marked superseded/historical) |
| `kumitate-shokunin/corpus/knowledge/queue-summary.md` | cited S1 note (historical line cites; erratum present) |
| `kumitate-shokunin/scripts/claims-check.mjs` | member-section gate |
| origin `scripts/fleet-dispatcher.mjs` | sole S1 member |
| origin `scripts/fleet-dispatcher.test.mjs` | present on tree but **S8**, not S1 |

## Live membership (origin tree)

**Command (exact list + sort):**

```bash
cd /home/vgpnk/Projects/ufo-fsd-alpha
ls -1 scripts/fleet-dispatcher.mjs | LC_ALL=C sort
```

**Observed output:**

```
scripts/fleet-dispatcher.mjs
```

**Presence:** `test -f scripts/fleet-dispatcher.mjs` → PRESENT.

**Count command:**

```bash
ls -1 scripts/fleet-dispatcher.mjs | wc -l
```

**Observed:** `1`

**Related path explicitly out of family (S8 remainder, not S1):**

```bash
ls -1 scripts/fleet-dispatcher.test.mjs
# scripts/fleet-dispatcher.test.mjs  — owned by remaining-scripts-census / S8
```

No `scripts/*dispatch*/` directory; no additional dispatcher-core split files under `scripts/` at this HEAD.

**Size (`wc -l` at origin HEAD `964f443e`):**

```bash
wc -l scripts/fleet-dispatcher.mjs
```

| Member (repo-relative) | Live `wc -l` | sha256 prefix |
|---|---:|---|
| `scripts/fleet-dispatcher.mjs` | **9829** | `ba5e02beac55` |

### Exact member list (authoritative for this seat)

1. `scripts/fleet-dispatcher.mjs`

**Declared count the registry row must carry:** **1**  
(set identity unchanged: still the single basename `fleet-dispatcher.mjs`; no members added or deleted. Line-count cell 14769 → 9829 is calibration drift for the parent cell rewrite.)

## Registry row S1 (read-only compare)

**Source:** `SCORECARD.md` in-scope surface registry:

```
| S1 | dispatcher core | `fleet-dispatcher.mjs` (14769 L) | yes — successor-chain · queue-and-claim · enqueue-admission · reconcile-and-cycle · queue-summary |
```

| Field | Registry | Live | Notes |
|---|---|---|---|
| member basename | `fleet-dispatcher.mjs` | `scripts/fleet-dispatcher.mjs` | match |
| member count | implicit 1 (no `N members` grammar) | **1** | match |
| line count | 14769 L | **9829** | **stale cell** (pre-2026-10-12 file); parent refreshes |
| note stems | 5 ·-joined stems | all 5 files exist under `corpus/knowledge/` | match |
| form (pre-edit) | topic (0 path `##` sections) | — | was `ROW_NO_SECTIONS` advisory |

**Corpus map:** `corpus/README.md` lists the five notes as separate coverage-map rows (queue-and-claim, successor-chain, enqueue-admission, reconcile-and-cycle, queue-summary), each primary-sourcing `fleet-dispatcher.mjs`.

**Parent action (not done here):** refresh the S1 members-cell line count 14769 → 9829 when the registry is rewritten; keep declared member **count = 1**. Do not widen S1 to absorb `fleet-dispatcher.test.mjs` (S8).

## Family notes — section honesty

**Cited notes (from the S1 cell):**

1. `corpus/knowledge/successor-chain.md`
2. `corpus/knowledge/queue-and-claim.md` ← **sectionized this seat**
3. `corpus/knowledge/enqueue-admission.md`
4. `corpus/knowledge/reconcile-and-cycle.md`
5. `corpus/knowledge/queue-summary.md`

**Pre-edit path-like `##` member headings across all five notes:** none (topic-form; `claims-check --row S1` → `form=topic sections=0 adv=1` / `ROW_NO_SECTIONS`).

Symbol-shaped `` ## `reconcileQueue(...)` `` / `` ## `runCycle(...)` `` heads in `reconcile-and-cycle.md` and similar topic heads in `queue-summary.md` are **not** member sections (`claims-check` requires `/` or a file extension in the first backticked token).

### Sections added

| Note | Heading | Anchors (live under `--src`) |
|---|---|---|
| `corpus/knowledge/queue-and-claim.md` | `## \`scripts/fleet-dispatcher.mjs\`` | `QUEUE_SCHEMA:95`, `writeQueue:4853`, `acquireQueueLock:4942`, `maybeEnqueueIterationSuccessor:5513`, `admitQueueCandidates:5956`, `reconcileQueue:7078`, `queueSummary:7624`, `runCycle:8966`, `main:9536` |

One section for the one declared member (occurrence = distinct = 1). Other cited notes left without a duplicate path `##` so S1 does not inflate `S_sections` five-fold for a single file.

### Sections removed

**None.** No note section named a path absent from the origin tree (no phantoms to drop).

### Boundary probe (`LC_ALL=C sort` both sides)

```bash
printf '%s\n' scripts/fleet-dispatcher.mjs | LC_ALL=C sort > /tmp/s1-live.txt
grep -E '^## `scripts/' \
  corpus/knowledge/queue-and-claim.md \
  corpus/knowledge/successor-chain.md \
  corpus/knowledge/enqueue-admission.md \
  corpus/knowledge/reconcile-and-cycle.md \
  corpus/knowledge/queue-summary.md \
  | sed 's/.*## `//;s/`.*//' | LC_ALL=C sort -u > /tmp/s1-sec.txt
comm -3 /tmp/s1-live.txt /tmp/s1-sec.txt
```

**Observed:** empty (no only-live, no only-section). `comm` exit 0.

### Anchor / claims gate

```bash
cd /home/vgpnk/Projects/shokunin/kumitate-shokunin
node scripts/claims-check.mjs --row S1 --src /home/vgpnk/Projects/ufo-fsd-alpha
```

**Observed (after section add):**

```
ROWS: 1  YES: 1  NOTES: 5  SECTIONS: 1
ROW S1   form=section   notes=5 sections=1 adv=0
SUMMARY: errors=0 warnings=0
CLAIMS: MATCH (rows=1 yes=1 notes=5 sections=1 adv=0)
```

exit 0. Gate confirms ≥1 live own-file anchor + ≥1 verbatim symbol in the member section under current `--src`.

**Pre-edit baseline (for the record):**

```
ROWS: 1  YES: 1  NOTES: 5  SECTIONS: 0
ROW S1   form=topic     notes=5 sections=0 adv=1
CLAIMS  warn  ROW_NO_SECTIONS          row=S1  S1 has no member section — member completeness unchecked
CLAIMS: MATCH (rows=1 yes=1 notes=5 sections=0 adv=1)
```

## Symbol spot-check (operability of citations, not a gate substitute)

| Symbol | Live line in `scripts/fleet-dispatcher.mjs` |
|---|---:|
| `QUEUE_SCHEMA` | 95 |
| `writeQueue` | 4853 |
| `acquireQueueLock` | 4942 |
| `maybeEnqueueIterationSuccessor` | 5513 |
| `admitQueueCandidates` | 5956 |
| `reconcileQueue` | 7078 |
| `queueSummary` | 7624 |
| `runCycle` | 8966 |
| `main` | 9536 |

Topic-body `L<n>` / bare `:<n>` cites in the five notes largely still address the **superseded** 14,769-line revision (explicitly marked on enqueue-admission / reconcile-and-cycle; queue-summary erratum already records `queueSummary` moved 10896 → 7624). That prose rot is **not** a member-section defect; cite-repair is out of this seat’s membership scope.

## Cross-domain findings (owner: parent / other families)

- **S-layer universe drift (round-32 Planned):** origin `S_members` live **91** (`ls scripts/*.mjs` → 73 + `find scripts -mindepth 2 -type f` → 18) vs frozen stanza **114**. S1 itself is stable at 1/1; the layer ratio move is outside this family’s set identity.
- **S1 cell line-count drift:** 14769 → 9829 — owner: parent registry rewrite.
- **`fleet-dispatcher.test.mjs`:** live on origin; remains **S8** (`remaining-scripts-census.md` already has `## \`scripts/fleet-dispatcher.test.mjs\``). Do not pull into S1.
- **Four supporting S1 notes** still topic-form / historical-line-heavy; optional follow-up is cite re-anchor or a single consolidated dispatcher note — not required for the S1 `yes` claim once one live member section exists.
- No member migrated into/out of S2–S8 from this one-name set in this measurement.

## Unresolved blockers

**None for S1.** Live set = note path-section set = claims sections = **1**. No phantom section to remove; missing member section added.

## Summary for parent integration

| Field | Value |
|---|---|
| Family | S1 dispatcher core |
| Live members | `scripts/fleet-dispatcher.mjs` |
| Declared count row must carry | **1** |
| Sections added | 1 (`queue-and-claim.md` → `## \`scripts/fleet-dispatcher.mjs\``) |
| Sections removed | 0 |
| Note edits by this seat | `corpus/knowledge/queue-and-claim.md` only |
| Registry/stanza edits by this seat | none (forbidden) |
| `claims-check --row S1` | `CLAIMS: MATCH … sections=1 adv=0` |
| Size drift to fold into cell | `fleet-dispatcher.mjs` 14769 → **9829** |

End of advisory. Not a verdict.
