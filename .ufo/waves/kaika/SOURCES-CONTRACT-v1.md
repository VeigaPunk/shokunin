# `corpus/SOURCES.md` — contract v1 (kaika, 2026-10-19, frozen)

Where a shokunin learns. `corpus/knowledge/` holds admitted facts; `corpus/SOURCES.md`
holds the places they come from — what each teaches, how far to trust it for which
scope, and when to look again. It is the lane's curated reading list and the standing
record of its taste. Inputs: `kaika-w1/art-curation.md` (curation and grading practice),
`kaika-w1/critic.md` (H4–H6 gates).

## Shape

```
# SOURCES — where <id> learns
## Registry           the one table below
## Paths              ordered study sequences: `<topic> — S003 → S010 → S014: why this order`
## Search log         one prose note per bounded search (rule 5)
## Leads (unopened)   bullets; a lead is not evidence and never a row
```

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|

- `id` — `S` + 3 or more digits, the next unused; never reused. No `|` inside any cell.
- `source` — title — canonical URL or DOI (a repo path or command for `own-work`).
- `kind` — `spec` · `docs` · `paper` · `code` · `tool` · `dataset` · `talk` · `book` ·
  `community` · `own-work`.
- `tier` — scoped to `scope`, never global. **A**: primary or authoritative for that scope
  (spec, official docs, source code, original paper, maintainer statement, the lane's own
  re-runnable gate output). **B**: strong secondary (expert write-up with reproducible
  detail, survey, textbook). **C**: lead only — never sole support for an admitted entry.
  `community` is never A. Tier is curation, not truth: no NATO/GRADE labels on rows.
- `scope` — the claim or topic the tier applies to.
- `anchor` — exact section / heading / page / line plus revision (version, commit, or
  publication date). Never a bare homepage.
- `teaches` — one grounded learner benefit. Rejected rows read
  `REJECTED: <reason>; flip: <what would change the verdict>`.
- `status` — `queued` (opened, worth mining) · `mined` (cited by ≥1 path in `used-by`) ·
  `rejected` (kept — a rejection is evidence of taste).
- `opened` — ISO date the row's author opened the source. `recheck` — ISO date or cadence
  (`90d`, `180d`, `on-release`).
- `used-by` — repo-relative paths of the knowledge entries or lessons citing the row,
  comma-separated, or `—`.

## Rules

1. **A row is a claim.** Write it only after opening the source in the round that writes
   the row. The round lesson's `## Gate` records, for every new row, the URL, the access
   date, and a ≤25-word quote with its location grounding `teaches`. Non-author
   verification re-opens a sample.
2. **Append-only.** Only `status`, `recheck` and `used-by` change in place, and each change
   is logged old→new in the round lesson. A correction is a new row whose `teaches` opens
   `supersedes S0NN —`.
3. **No second method.** Claim admission stays in `corpus/QUALITY.md`; the research method
   stays chousa's (`chousa-shokunin/SKILL.md`: question → source hierarchy → citation
   chain → claim-vs-source check). `SOURCES.md` duplicates neither; `QUALITY.md` points
   here for tier definitions.
4. **Expansion is knowledge, not rows.** The expansion trend counts admitted `knowledge/`
   entries whose `source:` cites a `mined` row on uncovered coverage-map ground. There is
   no row quota; a short registry of opened, honestly tiered rows beats a long one.
5. **Search log.** PRISMA-inspired, not PRISMA-compliant: question/query, where searched,
   date, identified / screened / included / excluded counts, exclusion reasons, stop
   rationale. A negative claim carries its sweep.
6. **No credential material**, session or private URLs, or `op://` references — ever.

## Census — run from the lane root (tested 2026-10-19 on a synthetic table)

```sh
# rows (spacing-tolerant)
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
# malformed rows — 11 columns means NF=13; must print 0
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
# tier histogram
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
# status histogram
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
# duplicate ids — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | sort | uniq -d
# enum violations and tier inflation — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; gsub(/[[:space:]]/,"",i); gsub(/[[:space:]]/,"",k); gsub(/[[:space:]]/,"",t); gsub(/[[:space:]]/,"",s); if (t !~ /^[ABC]$/) print "tier", i, t; if (s !~ /^(queued|mined|rejected)$/) print "status", i, s; if (k !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/) print "kind", i, k; if (t=="A" && k=="community") print "tier-inflation", i}' corpus/SOURCES.md
# mined rows whose used-by paths do not exist — must print nothing
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {s=$9; gsub(/[[:space:]]/,"",s); if (s=="mined") {n=split($12, a, /[,;]/); for (j=1;j<=n;j++) {p=a[j]; gsub(/^[[:space:]]+|[[:space:]]+$/,"",p); if (p!="" && p!="—") print p}}}' corpus/SOURCES.md | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
```
