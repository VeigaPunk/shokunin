# S6MemberRecensus — round-32 script-layer re-census (family S6)

**Seat:** `S6MemberRecensus` (leaf). **Family:** S6 ops watchers.  
**Lane:** `kumitate-shokunin` HEAD `175de6ba2e9e904010411b19cab27e0af9aad3d4`.  
**Origin:** `/home/vgpnk/Projects/ufo-fsd-alpha` HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9` (`964f443e`).  
**Scope:** live membership + note section honesty only. Registry row / proxy stanza not edited (parent-owned).

## Axes (named, not judged)

- **coverage:** S6 member set vs note `##` sections vs claims gate.
- **operability:** commands are re-runnable; every count carries its command.
- **calibration:** registry line-count cells vs live `wc -l` (drift recorded, not fitted here).

## Files inspected

| Path | Role |
|---|---|
| `kumitate-shokunin/SCORECARD.md` | registry row S6; round-32 `## Planned` |
| `kumitate-shokunin/corpus/README.md` | map row → `knowledge/ops-watchers.md` |
| `kumitate-shokunin/corpus/knowledge/ops-watchers.md` | S6 family note (section form) |
| `kumitate-shokunin/scripts/claims-check.mjs` | member-section gate |
| origin `scripts/ufo-stale-watchdog.mjs` | S6 member |
| origin `scripts/ufo-l0-monitor.mjs` | S6 member |
| origin `scripts/ufo-l0-watch.mjs` | S6 member |
| origin `scripts/the-tick-ping.mjs` | S6 member |
| origin `scripts/ufo-ground-handler.mjs` | S6 member |

## Live membership (origin tree)

**Command (exact list + sort):**

```bash
cd /home/vgpnk/Projects/ufo-fsd-alpha
ls -1 scripts/ufo-stale-watchdog.mjs \
      scripts/ufo-l0-monitor.mjs \
      scripts/ufo-l0-watch.mjs \
      scripts/the-tick-ping.mjs \
      scripts/ufo-ground-handler.mjs | LC_ALL=C sort
```

**Observed output:**

```
scripts/the-tick-ping.mjs
scripts/ufo-ground-handler.mjs
scripts/ufo-l0-monitor.mjs
scripts/ufo-l0-watch.mjs
scripts/ufo-stale-watchdog.mjs
```

**Presence (each `test -f` → PRESENT):** all five paths exist under origin `scripts/`.

**Count command:**

```bash
ls -1 scripts/ufo-stale-watchdog.mjs scripts/ufo-l0-monitor.mjs \
  scripts/ufo-l0-watch.mjs scripts/the-tick-ping.mjs \
  scripts/ufo-ground-handler.mjs | wc -l
```

**Observed:** `5`

**Sizes (`wc -l` at origin HEAD `964f443e`):**

```bash
wc -l scripts/ufo-stale-watchdog.mjs scripts/ufo-l0-monitor.mjs \
  scripts/ufo-l0-watch.mjs scripts/the-tick-ping.mjs \
  scripts/ufo-ground-handler.mjs
```

| Member (repo-relative) | Live `wc -l` |
|---|---:|
| `scripts/ufo-stale-watchdog.mjs` | 1010 |
| `scripts/ufo-l0-monitor.mjs` | 1638 |
| `scripts/ufo-l0-watch.mjs` | **1762** |
| `scripts/the-tick-ping.mjs` | **724** |
| `scripts/ufo-ground-handler.mjs` | **792** |
| **total** | 5926 |

### Exact member list (authoritative for this seat)

1. `scripts/ufo-stale-watchdog.mjs`
2. `scripts/ufo-l0-monitor.mjs`
3. `scripts/ufo-l0-watch.mjs`
4. `scripts/the-tick-ping.mjs`
5. `scripts/ufo-ground-handler.mjs`

**Declared count the registry row must carry:** **5**  
(set identity unchanged; no members added or deleted relative to the frozen S6 five-name list.)

## Registry row S6 (read-only compare)

**Source:** `SCORECARD.md` in-scope surface registry, row `| S6 | ops watchers | … |`

**Declared members (names):** same five basenames as live list.  
**Declared sizes in cell (stale vs live):**

| Basename | Registry cell | Live `wc -l` | Delta |
|---|---:|---:|---:|
| `ufo-stale-watchdog.mjs` | 1010 | 1010 | 0 |
| `ufo-l0-monitor.mjs` | 1638 | 1638 | 0 |
| `ufo-l0-watch.mjs` | 1679 | 1762 | +83 |
| `the-tick-ping.mjs` | 831 | 724 | −107 |
| `ufo-ground-handler.mjs` | 859 | 792 | −67 |

**Corpus map:** `corpus/README.md` → `knowledge/ops-watchers.md` (“registry family S6, 5 of 5 named”).

**Parent action (not done here):** refresh the three drifted line counts in the S6 cell when the registry is rewritten; keep declared member **count = 5**.

## Family note — section honesty

**Note:** `corpus/knowledge/ops-watchers.md`

**Member `##` headings present:**

```
## `scripts/ufo-stale-watchdog.mjs`
## `scripts/ufo-l0-monitor.mjs`
## `scripts/ufo-l0-watch.mjs`
## `scripts/the-tick-ping.mjs`
## `scripts/ufo-ground-handler.mjs`
```

**Boundary probe (`LC_ALL=C sort` both sides):**

```bash
printf '%s\n' scripts/ufo-stale-watchdog.mjs scripts/ufo-l0-monitor.mjs \
  scripts/ufo-l0-watch.mjs scripts/the-tick-ping.mjs \
  scripts/ufo-ground-handler.mjs | LC_ALL=C sort > /tmp/s6-live.txt
grep -E '^## `scripts/' corpus/knowledge/ops-watchers.md \
  | sed 's/^## `//;s/`$//' | LC_ALL=C sort > /tmp/s6-sec.txt
comm -3 /tmp/s6-live.txt /tmp/s6-sec.txt
```

**Observed:** empty (no only-live, no only-section). `comm` exit 0.

### Sections added

**None.** Every live member already has exactly one `## \`scripts/<file>\`` section.

### Sections removed

**None.** No note section names a path absent from the origin tree (no phantoms).

### Anchor / claims gate

```bash
cd /home/vgpnk/Projects/shokunin/kumitate-shokunin
node scripts/claims-check.mjs --row S6 --src /home/vgpnk/Projects/ufo-fsd-alpha
```

**Observed:**

```
ROWS: 1  YES: 1  NOTES: 1  SECTIONS: 5
ROW S6   form=section   notes=1 sections=5 adv=0
SUMMARY: errors=0 warnings=0
CLAIMS: MATCH (rows=1 yes=1 notes=1 sections=5 adv=0)
```

exit 0. Gate confirms ≥1 live own-file anchor + ≥1 verbatim symbol per member section under current `--src`.

### Note header calibration debt (not a section edit)

Note header still pins measurement HEAD `daa371583` and sizes `1010 1638 1679 831 859`. Live HEAD is `964f443e` with sizes `1010 1638 1762 724 792`.  
**This seat did not rewrite the note** — section membership already matches the tree and `CLAIMS: MATCH`; size/HEAD prose refresh is optional honesty work for parent/doc pass, not required to keep the S6 `yes` claim.

## Symbol spot-check (operability of citations, not a gate substitute)

| Member | Symbol still present in file |
|---|---|
| `ufo-stale-watchdog.mjs` | `POLL_MS` |
| `ufo-l0-monitor.mjs` | `DRIFT_CODES` |
| `ufo-l0-watch.mjs` | `INTERVAL_MS` |
| `the-tick-ping.mjs` | `fanOutPathPing` |
| `ufo-ground-handler.mjs` | `PATH_PING_ERROR_CODES` |

## Cross-domain findings (owner: parent / other families)

- **S-layer universe drift (already in round-32 Planned):** origin `S_members` live **91** vs frozen stanza **114**. S6 itself is stable at 5/5; the layer ratio move is outside this family’s set identity.
- **Line-count cell drift on three S6 members** (`ufo-l0-watch`, `the-tick-ping`, `ufo-ground-handler`) — owner: parent registry rewrite.
- No member migrated into/out of S7/S8 from this five-name set in this measurement.

## Unresolved blockers

**None for S6.** Live set = note sections = claims sections = **5**. No phantom section to remove; no missing section to add.

## Summary for parent integration

| Field | Value |
|---|---|
| Family | S6 ops watchers |
| Live members | 5 paths listed above |
| Declared count row must carry | **5** |
| Sections added | 0 |
| Sections removed | 0 |
| Note edits by this seat | none (already honest on membership) |
| Registry/stanza edits by this seat | none (forbidden) |
| `claims-check --row S6` | `CLAIMS: MATCH … sections=5 adv=0` |
| Size drift to fold into cell | l0-watch 1679→1762; tick-ping 831→724; ground-handler 859→792 |

End of advisory. Not a verdict.
