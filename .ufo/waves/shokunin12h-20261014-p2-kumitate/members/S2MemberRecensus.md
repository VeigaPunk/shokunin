# S2MemberRecensus — round-32 script-layer re-census (S2)

**Seat:** `S2MemberRecensus` · **Family:** S2 native trial path  
**Origin tree:** `/home/vgpnk/Projects/ufo-fsd-alpha` HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9`  
**Lane:** `/home/vgpnk/Projects/shokunin/kumitate-shokunin` (read + note edit; registry/stanza untouched)  
**Status:** measured re-census + note sectionization complete — **not a verdict**

---

## 1. Files inspected

| Path | Role |
|---|---|
| `SCORECARD.md` (registry row S2 + `## Planned` round-32) | declared cell + deletion set |
| `corpus/README.md` | coverage-map cites for native-trial-launch / failure-telemetry |
| `corpus/knowledge/native-trial-launch.md` | S2 primary note (edited) |
| `corpus/knowledge/failure-telemetry.md` | co-cited note (S5 peer already sectionized; **not** rewritten by this seat) |
| `scripts/claims-check.mjs` | section/anchor/member-count arms |
| origin `scripts/run-omp-native-trial.mjs` | live member |
| origin `scripts/collect-omp-native-handoff.mjs` | live member |
| origin `scripts/collect-omp-native-handoff-lib/*` | live lib members (5) |

---

## 2. Live membership — commands + observed output

Origin HEAD confirmed:

```
$ git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD
964f443ee53df0ce06bd689af01f0dea031b01f9
```

### Command A — top-level pair

```
$ ls -1 /home/vgpnk/Projects/ufo-fsd-alpha/scripts/run-omp-native-trial.mjs \
        /home/vgpnk/Projects/ufo-fsd-alpha/scripts/collect-omp-native-handoff.mjs
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/collect-omp-native-handoff.mjs
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/run-omp-native-trial.mjs
```

### Command B — lib directory (sorted; locale-safe)

```
$ find /home/vgpnk/Projects/ufo-fsd-alpha/scripts/collect-omp-native-handoff-lib -type f | LC_ALL=C sort
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/collect-omp-native-handoff-lib/base.mjs
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/collect-omp-native-handoff-lib/events.mjs
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/collect-omp-native-handoff-lib/evidence.mjs
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/collect-omp-native-handoff-lib/policy.mjs
/home/vgpnk/Projects/ufo-fsd-alpha/scripts/collect-omp-native-handoff-lib/screening.mjs
```

`find … | wc -l` → **5** (not 6).

### Command C — relative member list (authoritative for this family)

```
$ {
    printf '%s\n' scripts/run-omp-native-trial.mjs scripts/collect-omp-native-handoff.mjs
    find /home/vgpnk/Projects/ufo-fsd-alpha/scripts/collect-omp-native-handoff-lib -type f \
      | sed 's|.*/scripts/|scripts/|'
  } | LC_ALL=C sort
scripts/collect-omp-native-handoff-lib/base.mjs
scripts/collect-omp-native-handoff-lib/events.mjs
scripts/collect-omp-native-handoff-lib/evidence.mjs
scripts/collect-omp-native-handoff-lib/policy.mjs
scripts/collect-omp-native-handoff-lib/screening.mjs
scripts/collect-omp-native-handoff.mjs
scripts/run-omp-native-trial.mjs
```

### Command D — sizes

```
$ wc -l /home/vgpnk/Projects/ufo-fsd-alpha/scripts/run-omp-native-trial.mjs \
        /home/vgpnk/Projects/ufo-fsd-alpha/scripts/collect-omp-native-handoff.mjs \
        /home/vgpnk/Projects/ufo-fsd-alpha/scripts/collect-omp-native-handoff-lib/*.mjs
  4304 scripts/run-omp-native-trial.mjs
  1804 scripts/collect-omp-native-handoff.mjs
   955 scripts/collect-omp-native-handoff-lib/base.mjs
   383 scripts/collect-omp-native-handoff-lib/events.mjs
  1163 scripts/collect-omp-native-handoff-lib/evidence.mjs
   924 scripts/collect-omp-native-handoff-lib/policy.mjs
   745 scripts/collect-omp-native-handoff-lib/screening.mjs
 10278 total
```

### Command E — deleted lib member

```
$ test ! -e /home/vgpnk/Projects/ufo-fsd-alpha/scripts/collect-omp-native-handoff-lib/refusal-line.mjs \
    && echo 'refusal-line.mjs ABSENT'
refusal-line.mjs ABSENT
```

Matches Planned deletion set: `scripts/collect-omp-native-handoff-lib/refusal-line.mjs` (S2).

---

## 3. Exact member list (live)

**S2_members = 7** (disjoint, exhaustive for the family path set named in the assignment):

1. `scripts/run-omp-native-trial.mjs` (4304 L)
2. `scripts/collect-omp-native-handoff.mjs` (1804 L)
3. `scripts/collect-omp-native-handoff-lib/base.mjs` (955 L)
4. `scripts/collect-omp-native-handoff-lib/events.mjs` (383 L)
5. `scripts/collect-omp-native-handoff-lib/evidence.mjs` (1163 L)
6. `scripts/collect-omp-native-handoff-lib/policy.mjs` (924 L)
7. `scripts/collect-omp-native-handoff-lib/screening.mjs` (745 L)

**Not a member (removed from tree):**  
`scripts/collect-omp-native-handoff-lib/refusal-line.mjs`

---

## 4. Registry row S2 vs live

| | Registry cell (untouched) | Live measure |
|---|---|---|
| Launcher | `run-omp-native-trial.mjs` **(4693 L)** | **4304 L** |
| Collector | `collect-omp-native-handoff.mjs` **(1943 L)** | **1804 L** |
| Lib | `collect-omp-native-handoff-lib/` **(6)** | **(5)** files |
| Implied total | 2 + 6 = **8** | **7** |
| Notes cell | `yes — native-trial-launch · failure-telemetry` | both notes still resolve |

**Declared count the row must carry after parent rewrite:** **`7 members`**  
(Recommended cell shape for parent — this seat did **not** edit SCORECARD:)

```
| S2 | native trial path | 7 members: `run-omp-native-trial.mjs` (4304 L) + `collect-omp-native-handoff.mjs` (1804 L) + `collect-omp-native-handoff-lib/` (5: base, events, evidence, policy, screening) | yes — native-trial-launch · failure-telemetry |
```

Optional parent follow-up: drop `failure-telemetry` from the S2 note cell (see §7) so S2 stops absorbing S5's `ufo-mission-result.mjs` section as `SECTION_FILE_NOT_MEMBER`.

`corpus/README.md` map rows for the two notes are descriptive only; no edit required for membership arithmetic.

---

## 5. Note edits (this seat)

### `corpus/knowledge/native-trial-launch.md`

**Sections added** (path-form `## \`scripts/…\`` with live own-file anchors + verbatim symbols):

| Section heading | inFamily |
|---|---|
| `scripts/run-omp-native-trial.mjs` | yes |
| `scripts/collect-omp-native-handoff.mjs` | yes |
| `scripts/collect-omp-native-handoff-lib/base.mjs` | yes |
| `scripts/collect-omp-native-handoff-lib/events.mjs` | yes |
| `scripts/collect-omp-native-handoff-lib/evidence.mjs` | yes |
| `scripts/collect-omp-native-handoff-lib/policy.mjs` | yes |
| `scripts/collect-omp-native-handoff-lib/screening.mjs` | yes |

**Sections removed:** none pre-existed as path-form member headings (note was topic-form: `Ordered pipeline`, `Spawn`, …). No phantom `## \`…refusal-line…\`` heading was present to delete.

**Prose removal / correction recorded in-note:**

- Header size **4693 → 4304**; `main()` anchor **:3539 → :3229**.
- Failure surface no longer attributes schema lines to  
  `collect-omp-native-handoff-lib/refusal-line.mjs` (file absent).  
  Live writer: local `die` at `scripts/run-omp-native-trial.mjs:831`  
  (and collector-side `die` at `…/base.mjs:303`).
- Explicit **Round-32 S2 membership** block documents the 7-member set and the refusal-line removal.

### `corpus/knowledge/failure-telemetry.md`

**Not edited by this seat.** Concurrent S5 recensus already:

- owns `## \`scripts/ufo-mission-result.mjs\`` (S5 member);
- routes `CAPACITY_FAILURES` / `ROUTING_HEALTH_OUTCOMES` / classifier prose to S2 `base.mjs` without inventing S5 sections;
- removed the old `refusal-line.mjs` exit-path cite.

S2 still *claims* this note via the registry cell → gate sees the S5 section as out-of-family (advisory only).

---

## 6. Claims gate re-check (evidence, not a round verdict)

```
$ node scripts/claims-check.mjs --row S2 --src /home/vgpnk/Projects/ufo-fsd-alpha
ROWS: 1  YES: 1  NOTES: 2  SECTIONS: 8
ROW S2   form=section   notes=2 sections=8 adv=1
CLAIMS  warn  SECTION_FILE_NOT_MEMBER  row=S2  scripts/ufo-mission-result.mjs is outside S2's declared members
SUMMARY: errors=0 warnings=1
CLAIMS: MATCH (rows=1 yes=1 notes=2 sections=8 adv=1)
```

Breakdown:

| Kind | Count |
|---|---|
| In-family member sections (`inFamily: true`) | **7** (= live S2 membership) |
| Out-of-family section (S5 `ufo-mission-result.mjs` via shared note) | 1 |
| Raw `SECTIONS` total | 8 |
| Errors | 0 |
| `MEMBER_COUNT_DRIFT` | none (cell has no `N members` integer yet — parent rewrite) |

All seven in-family sections: `live: true`, `symbolHit: true`.

---

## 7. Cross-domain findings (owner: parent / other seats)

| Finding | Owner |
|---|---|
| Registry S2 cell still prints lib **(6)** and stale 4693/1943 sizes; must become **7 members** with live sizes | **parent** (registry + stanza) |
| S2 note cell still lists `failure-telemetry` after S5 made that note S5-primary section-form → `SECTION_FILE_NOT_MEMBER` advisory on every S2 claims run | **parent** (consider dropping the stem from S2's cell, or accept the advisory like R9's out-of-family sections) |
| `coverage:script-layer` numerator: this family contributes **+7** in-family sections (was 0 topic-form) once parent re-derives `S_sections` | **parent** (proxy re-pin / stanza) |
| `membrane-seal write` argv defect remains filed in native-trial topic prose; not absorbed | origin / prior ledger (unchanged) |
| S5 peer already moved capacity/routing-health authority attribution to S2 `base.mjs` in failure-telemetry | S5MemberRecensus (observed; no conflict with S2 sections placed in native-trial-launch) |

---

## 8. Unresolved blockers

**None for S2 note honesty.** Every live member has a gated section with live anchors.

Parent still must:

1. Rewrite the S2 registry members cell to **7** (and sizes).
2. Re-derive layer stanza terms (`S_members` / `S_sections`) — not this seat.
3. Optionally de-couple S2 from `failure-telemetry` to clear the advisory.

No member was invented. No section was left for a file absent from the tree.

---

## 9. Axes touch (informational)

| Axis | Effect of this seat's work |
|---|---|
| `coverage:script-layer` | +7 honest in-family sections for S2 (gate-visible once integrated); does not by itself move the frozen stanza |
| operability | unchanged (no new runnable artifact) |
| calibration | live HEAD + `LC_ALL=C sort` membership; claims MATCH with documented advisory |

---

*End of advisory. Data only — parent integrates.*
