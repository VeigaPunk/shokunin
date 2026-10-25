# S7MemberRecensus — advisory (unjudged fleet wave)

Lane: `kumitate-shokunin` @ dispatch HEAD `175de6ba2e9e904010411b19cab27e0af9aad3d4`  
Origin (READ-ONLY): `/home/vgpnk/Projects/ufo-fsd-alpha` HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9`  
Family: **S7** — route-probe cluster + shared helpers  
Note: `corpus/knowledge/route-probe-cluster.md`  
Registry row (not edited): `SCORECARD.md` line 125  

This report is data, not a verdict. Parent owns the registry row, stanza, and gate re-pin.

---

## Axes (this seat)

- **coverage** — honest live membership + one `##` section per live member  
- **operability** — commands + `claims-check --row S7` evidence a parent can re-run  
- **calibration** — declared count the row must carry equals measured live set (6)

---

## Files inspected

| Path | Role |
|---|---|
| `/home/vgpnk/Projects/ufo-fsd-alpha/scripts/probe-*.mjs` | live origin membership |
| `/home/vgpnk/Projects/ufo-fsd-alpha/scripts/fake-omp.mjs` | live helper |
| `/home/vgpnk/Projects/ufo-fsd-alpha/scripts/atomic-write.mjs` | absence probe (GONE) |
| `kumitate-shokunin/SCORECARD.md` | S7 registry row (read-only) |
| `kumitate-shokunin/corpus/README.md` | family → note citation |
| `kumitate-shokunin/corpus/knowledge/route-probe-cluster.md` | family note (edited) |
| `kumitate-shokunin/scripts/claims-check.mjs` | section/anchor gate (read) |

---

## Exact commands + observed output

### Origin HEAD

```text
$ git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD
964f443ee53df0ce06bd689af01f0dea031b01f9
```

### Live S7 membership enumeration

Historical family rule (round 13): `scripts/probe-*.mjs` + `scripts/atomic-write.mjs` + `scripts/fake-omp.mjs`.  
Live tree drops the two colocated `probe-*.test.mjs` suites and `atomic-write.mjs`.

```text
$ ORIGIN=/home/vgpnk/Projects/ufo-fsd-alpha
$ ( ls -1 "$ORIGIN"/scripts/probe-*.mjs; ls -1 "$ORIGIN"/scripts/fake-omp.mjs ) | LC_ALL=C sort
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/fake-omp.mjs
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/probe-redact.mjs
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/probe-token-plan-kimi.mjs
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/probe-token-plan-models.mjs
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/probe-token-plan-shared.mjs
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/probe-ufo-route-health.mjs

$ ( ls -1 "$ORIGIN"/scripts/probe-*.mjs; ls -1 "$ORIGIN"/scripts/fake-omp.mjs ) | wc -l
6

$ wc -l "$ORIGIN"/scripts/probe-*.mjs "$ORIGIN"/scripts/fake-omp.mjs | tail -1
 2253 total

$ test -f "$ORIGIN"/scripts/atomic-write.mjs; echo $?
1

$ ls "$ORIGIN"/scripts/probe-*.test.mjs 2>&1 | head -1
ls: cannot access '.../scripts/probe-*.test.mjs': No such file or directory

$ # historical 9-set command against live tree (ls errors on missing → non-zero)
$ ls -1 "$ORIGIN"/scripts/probe-*.mjs "$ORIGIN"/scripts/atomic-write.mjs "$ORIGIN"/scripts/fake-omp.mjs 2>&1 | wc -l
7
```

Per-file live sizes (`wc -l`):

| Member | L |
|---|---|
| `scripts/probe-ufo-route-health.mjs` | 1195 |
| `scripts/probe-redact.mjs` | 116 |
| `scripts/probe-token-plan-kimi.mjs` | 147 |
| `scripts/probe-token-plan-models.mjs` | 244 |
| `scripts/probe-token-plan-shared.mjs` | 159 |
| `scripts/fake-omp.mjs` | 392 |
| **total** | **2253** |

`node --check` on each of the six → exit 0 (6/6).

### Gone vs historical 9

| Path | Status |
|---|---|
| `scripts/probe-ufo-route-health.mjs` | LIVE |
| `scripts/probe-token-plan-shared.mjs` | LIVE |
| `scripts/probe-token-plan-kimi.mjs` | LIVE |
| `scripts/probe-token-plan-models.mjs` | LIVE |
| `scripts/probe-redact.mjs` | LIVE |
| `scripts/fake-omp.mjs` | LIVE |
| `scripts/probe-ufo-route-health.test.mjs` | **GONE** |
| `scripts/probe-redact.test.mjs` | **GONE** |
| `scripts/atomic-write.mjs` | **GONE** |

### Registry row (read-only; parent owns edit)

```text
$ grep -n '^| S7 ' kumitate-shokunin/SCORECARD.md
125:| S7 | route-probe cluster + shared helpers | 9 members: 7 `probe-*.mjs` + `atomic-write.mjs` + `fake-omp.mjs` (3,132 L) … | yes — `knowledge/route-probe-cluster.md`: 9 of 9 …
```

`corpus/README.md` still cites the note as “9 of 9 members” (parent / README owner).

### Heading ↔ member parity (after note edit)

```text
$ {
    ls -1 "$ORIGIN"/scripts/probe-*.mjs
    ls -1 "$ORIGIN"/scripts/fake-omp.mjs
  } | sed 's|.*/scripts/|scripts/|' | LC_ALL=C sort > /tmp/s7-members.txt
$ grep -oE '^## `scripts/[^`]+`' corpus/knowledge/route-probe-cluster.md \
    | sed -E 's/^## `//; s/`$//' | LC_ALL=C sort > /tmp/s7-headings.txt
$ wc -l < /tmp/s7-members.txt    # 6
$ wc -l < /tmp/s7-headings.txt   # 6
$ LC_ALL=C comm -3 /tmp/s7-members.txt /tmp/s7-headings.txt
# (empty)
```

### claims-check (section quality)

```text
$ node scripts/claims-check.mjs \
    --self /home/vgpnk/Projects/shokunin/kumitate-shokunin \
    --row S7 --src /home/vgpnk/Projects/ufo-fsd-alpha
ROWS: 1  YES: 1  NOTES: 1  SECTIONS: 6
ROW S7   form=section   notes=1 sections=6 adv=0
CLAIMS  error MEMBER_COUNT_DRIFT       row=S7  declared 9 members, found 6 distinct sections
SUMMARY: errors=1 warnings=0
CLAIMS: DRIFT (MEMBER_COUNT_DRIFT row=S7 declared 9 members, found 6 distinct sections)
```

Interpretation: **all six live member sections resolve with live own-file anchors and symbol hits** (`adv=0`). The sole error is the expected **declared-count drift** while the registry cell still says `9 members`. Parent flips that cell to **6** and re-runs.

---

## Exact member list (live)

Relative to origin `scripts/`:

1. `scripts/fake-omp.mjs`  
2. `scripts/probe-redact.mjs`  
3. `scripts/probe-token-plan-kimi.mjs`  
4. `scripts/probe-token-plan-models.mjs`  
5. `scripts/probe-token-plan-shared.mjs`  
6. `scripts/probe-ufo-route-health.mjs`  

**Declared count the S7 registry row must carry: `6`.**

(Not 9. Not 7 `probe-*` alone. Helper retained: `fake-omp.mjs` only.)

---

## Note edits (`corpus/knowledge/route-probe-cluster.md`)

### Sections removed (3)

| Heading removed | Reason |
|---|---|
| `## \`scripts/atomic-write.mjs\`` | file absent on origin |
| `## \`scripts/probe-ufo-route-health.test.mjs\`` | file absent on origin |
| `## \`scripts/probe-redact.test.mjs\`` | file absent on origin |

Removal recorded in-note under `## Round-32 membership removals` with absence evidence and where durable-write responsibility moved (inlined `persistState` / `writeVerdict`).

### Sections retained / rewritten (6) — anchors re-derived on live files

| Heading | Status |
|---|---|
| `## \`scripts/probe-ufo-route-health.mjs\`` | rewritten (1195 L; was 1364); live anchors e.g. `:2-3`, `main` `:1164`, `persistState` `:1080`, exit `:1185` |
| `## \`scripts/probe-token-plan-shared.mjs\`` | rewritten (159 L; was 235); live anchors `:19-20`, `runOmpCatalog` `:51`, `probeListedModel` `:84` |
| `## \`scripts/probe-token-plan-kimi.mjs\`` | rewritten (147 L); live anchors `:2`, `fail` `:24`, exit `:140` |
| `## \`scripts/probe-token-plan-models.mjs\`` | rewritten (244 L); live anchors `VERDICT_PATH` `:35`, `writeVerdict` `:40` (path is now sibling `.verdict.json`, not `.ufo/probes/…`) |
| `## \`scripts/probe-redact.mjs\`` | rewritten (116 L; was 160); live anchors `CREDENTIAL_SHAPE` `:8`, `redact` `:67`; notes loss of `containsCredential` / `RedactError` |
| `## \`scripts/fake-omp.mjs\`` | rewritten (392 L); live anchors `:10`, `FAKE_OMP_MODE` `:30`, `flushSession` `:174` |

### Sections added (structural, not new members)

- `## Round-32 membership removals` — records the three deletions  
- Scope / membership / probe / Limits prose updated 9 → **6**, with the live enumeration command  
- Import graph updated: no `atomic-write.mjs`; route-health redaction is a standalone parity copy (`:63-65`)  
- Citation ledger fence kept as **historical** artifact (pre-restructure paths/lines)

### Sections not added

No invented members. No widening into S5 (`omp-global-config.mjs`) or S8. No absorption of `tests/route-probes.test.js`.

---

## Compare: registry / README vs live

| Source | Claim | Live |
|---|---|---|
| SCORECARD S7 members cell | 9 members: 7 `probe-*.mjs` + `atomic-write` + `fake-omp` (3132 L) | **6** members, 2253 L; atomic-write + 2 tests gone |
| SCORECARD S7 covered cell | yes — 9 of 9 named | note now has **6 of 6** sections; row still says 9 → `MEMBER_COUNT_DRIFT` |
| `corpus/README.md` route-probe row | “9 of 9 members” + lists test suites + atomic-write | stale prose (parent/README) |
| Family note (pre-edit) | 9 `## \`scripts/…\`` sections | 3 were phantoms |

---

## Unresolved blockers

None for this seat’s deliverable.

Parent still must:

1. Set S7 declared member cell to **6** with the live command above (not the historical 9-set).  
2. Refresh covered-cell prose (`6 of 6`, line totals 2253).  
3. Optionally refresh `corpus/README.md` S7 blurb (out of this seat).  
4. Re-pin stanza / `S_sections` after all family seats land.  
5. Expect `MEMBER_COUNT_DRIFT` to clear only after (1).

---

## Cross-domain findings (owner)

| Finding | Owner |
|---|---|
| `atomic-write.mjs` deleted; durable write inlined into route-health + token-plan-models | origin / OMP tree (already landed); kumitate parent for registry arithmetic |
| Colocated `probe-*.test.mjs` deleted; consumer remains `tests/route-probes.test.js` (outside script-layer universe) | origin; S7 note treats it as consumer only |
| S8 remainder arithmetic (was 60 = 69−9) must re-derive against live S_members 91 and live S7=6 — do not reuse 60 by subtraction from 69 | **S8MemberRecensus** / parent |
| Topic sections + frozen citation ledger in the S7 note still hold pre-restructure line numbers; member sections are the claims surface | optional follow-up (cite-check debt), not required for section-form yes |
| Registry/README still advertise 9 | **parent** (this seat did not edit them per contract) |

---

## Files changed by this seat

1. `kumitate-shokunin/corpus/knowledge/route-probe-cluster.md` — membership honesty + 6 live sections + 3 removals recorded  
2. `.ufo/waves/shokunin12h-20261014-p2-kumitate/members/S7MemberRecensus.md` — this advisory  

**Not changed:** `SCORECARD.md` registry row, proxy stanza, `corpus/README.md`, origin tree.

---

## Summary for parent

- **Live S7 members = 6** (command above).  
- **Row must declare 6.**  
- Note: 3 phantom sections removed; 6 sections with live anchors (`claims-check` sections=6 adv=0).  
- Remaining drift is solely `MEMBER_COUNT_DRIFT declared=9 found=6` until parent updates the cell.
