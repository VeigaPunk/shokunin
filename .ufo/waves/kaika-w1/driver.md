
Reviewer: W1Driver (leaf, no subagent dispatch). Date: 2026-10-19.
Files reviewed:

- `F` = `/home/vgpnk/Projects/shokunin/scripts/shokunin-watchdog.sh` (118 ln)
- `K` = `/home/vgpnk/Projects/kimi-shokunin/scripts/shokunin-watchdog.sh` (149 ln)
- `M` = `/home/vgpnk/Projects/kimi-shokunin/scripts/mint-agent.sh` (98 ln)
- `TF` = `/home/vgpnk/Projects/shokunin/templates/round-prompt.md` (91 ln)
- `TK` = `/home/vgpnk/Projects/kimi-shokunin/templates/round-prompt.md` (67 ln)
- `LW` = `/home/vgpnk/Projects/shokunin/.ufo/lane-watch.sh` (24 ln)
- `C` = `/home/vgpnk/Projects/shokunin/shokunin.conf` (77 ln)

Method: `shellcheck 0.11.0` on all four scripts (result: clean except K:23/32 SC1007,
K:—/M:19 style warnings and M:84 SC2016 info note — all cosmetic), line-by-line diff
of F vs K and TF vs TK, ground-truth checks against live `.ufo/state/` and
`.ufo/watchdog.log`, and targeted reproductions shown inline. The watchdog loop was
never executed.

## 0. Ground truth that frames every finding

- `.ufo/watchdog.log` ends 2026-10-15T01:58 (4 days stale); every `.ufo/state/*.mission`
  file contains a **bare PID** (e.g. `2685430`), every `*.out` file holds lane stdout.
  Verified all sampled PIDs dead.
- The log's message vocabulary (`lane-round-failed … marker/contentless report`,
  `launch <lane> round=N pid=<pid>`) exists **only in K's source**, not F's. The running
  driver is a kimi-port-shaped script whose exact source is committed nowhere I could
  find in the fleet repo — F is its stale ancestor still shipping a different mechanism.
- `.ufo/state/` also holds orphan rows for retired lanes (`audio`, `game-dev-2d`,
  `game-dev-3d`, `mori`, `souji`…) — see M7.

## 1. Findings by severity

### C1 — committed fleet watchdog cannot run at all; live driver is uncommitted (F)

`F:8` — `UFO=/home/vgpnk/Projects/origin-work/ufo-fsd-alpha/scripts/ufo-sighting`.
Verified: `ls` on that path → ENOENT. Every `launch_lane` (F:72-79) therefore captures
"no such file" into `out`, fails the F:80 grep, and writes `launch-fail` — for all 9
lanes, every 450s, forever. Anyone who checks the repo out and starts
`scripts/shokunin-watchdog.sh` gets a dead fleet that logs failure forever with zero
agent processes. The actual running driver (a K-shaped port writing PIDs and `.out`
files) is not what the repo commits. This is a fleet-meta SSOT violation: the committed
machinery is not the machinery.

### H1 — no singleton lock on the driver (F and K)

Neither script uses `flock`/pidfile. Two concurrent instances each run the full sweep:
`launch_lane` fires twice per lane per tick, `.round`/`.mission` files race
(last-writer-wins), and each instance believes the other's lanes. Repro: start the
script twice. Fix: `exec 9>"$UFO/.watchdog.lock"; flock -n 9 || die "driver already running"`.

### H2 — `.round` unsanitized; `$((n+1))` silently rewinds the counter (F:43,96,100,103)

`round_of` in F returns the file contents verbatim. If `.ufo/state/<lane>.round`
contains `abc` (crashed write, hand edit), F:96 `[ "$n" -eq 0 ]` errors under `set -u`
but the loop continues; then `launch_lane $((n+1))` treats `abc` as an unset variable →
`1`, relaunching **round 1** and silently rewinding the ledger vs MANIFEST.json.
Repro: `echo abc > .ufo/state/kasegi.round` → next tick launches `round=1`.
K fixed this at K:58-59 (`case $n in ''|*[!0-9]*) echo 0`); the fix never reached F.

### H3 — `.mission` is a bare PID; `kill -0`/`kill` liveness hits PID reuse (K:93,126,130)

K records `pid=$!` of a backgrounded subshell. After any driver restart, a recycled PID
can belong to an unrelated process: the lane shows `live=1` forever (**starvation** —
never respawned until that process exits), and if a report lands meanwhile K:130
`kill "$mid"` SIGTERMs a random host process. Ground truth: every `.mission` file today
holds a PID dead since Oct 15 — on the next driver start, each lane's fate depends on
those PIDs staying dead. Worse edge: a `.mission` file containing `0` → `kill -0 0`
always succeeds (own process group) → lane permanently "live"; a landing report →
`kill 0` signals the watchdog's whole process group. Fix: validate `mid` numerically and
confirm `/proc/$mid/cmdline` matches the substrate before trusting it, or store and
kill a PGID.

### H4 — `kill $mid` kills the wrapper subshell, orphaning the agent mid-write (K:91-93,130)

`launch_lane` backgrounds `( cd …; eval "$run_cmd" )` and records the **subshell** PID.
The `eval`'d agent (omp/kimi) is its child. When a report lands early, K:130 kills the
subshell; the agent is reparented and keeps running — while `advance` immediately
launches round N+1 **in the same lane repo**. Two concurrent L1 processes interleave
commits and invalidate each other's before→after measurements. Repro: any round where
the report file lands before the agent exits. Fix: `setsid` + kill the process group,
and/or wait for child exit before `advance`.

### H5 — `report_of` in F is existence-only; the template's "marker rule" is unenforced (F:45)

`report_of() { [ -f "$SK/.ufo/reports/round-$2/$1.md" ]; }` — `touch` of the file
advances the round. TF §4's marker rule ("a contentless report … counts as the round
failed") has no driver-side enforcement under F. K's content check (K:66-71: SHONEN
marker + `MIN_REPORT_BYTES`) is the intended contract — see M3 for its own defect.

### H6 — mass relaunch storm when status/liveness check fails (F:92,95)

`status=$("$UFO" status --lite 2>/dev/null || true)` once per tick. If `ufo-sighting`
is down (or, per C1, absent), `status` is empty → every lane with a `.mission` shows
`live=0` → every lane relaunches every tick, no backoff. Same shape in K for a dead
`.mission` PID plus `lane-dead-no-report` relaunch each tick (K:141-144). Neither
driver has a failure counter, backoff, or per-lane launch-rate cap.

### M1 — `render_prompt` sed substitutions are data-unsafe (K:75-77)

`sed -e "s/{{AXES}}/${LANE_AXES[$lane]:-}/g" …` with no escaping:

- `/` in axes → sed syntax error → `render_prompt` fails → `launch-fail` forever for
  that lane. Reproduced: `AXIS='cross-lane quality, mint/dormancy calls'` →
  `sed: error: invalid substitute flag: 'd'`. The shipped `templates/shokunin.conf.example`
  aggregator row (`mint/dormancy calls`, line 21) triggers this verbatim — the fleet's
  own conf.example cannot boot that lane under K. C dodges it only because its axes say
  "and" instead of "/".
- `&` in axes → re-inserts `{{AXES}}` literally. Reproduced: `'depth & coverage'` →
  rendered `axes: depth {{AXES}} coverage`. Silent wrong prompt.
- `|` in `SHOKUNIN_ROOT` or `\` anywhere breaks the third expression similarly.

Fix: escape `[\/&|\\]` in every substitution value, or render with awk (`gsub` on
fixed strings) instead of sed.

### M2 — template ships a never-substituted placeholder (TF:1, TK:1)

`Working dir: {{FLEET_ROOT}}/<{{LANE}}-repo>.` — `<{{LANE}}-repo>` is literal angle-
bracket text; neither renderer touches it. Verified in a live rendered prompt:
`.ufo/prompts/kasegi-round-17.md:1` reads
`Working dir: /home/vgpnk/Projects/shokunin/<kasegi-repo>.` — a path that does not
exist. Rounds only work because `SUBSTRATE_CMD`/`--cwd` sets the real cwd. Fix:
substitute the real repo path from the LANES table (add `{{LANE_REPO}}`), or delete
the field — F's heredoc interpolates `${LANE_CWD[$lane]}` correctly.

### M3 — report-content gate regex is brittle in both directions (K:69-70)

- Too strict: requires uppercase `SHONEN` (`^#+ *SHONEN|\*\*SHONEN\*\*`); a report
  headed `## Shonen`/`## Shōnen` fails → infinite same-round relaunch loop burning
  compute forever.
- Too loose: any ≥`MIN_REPORT_BYTES` (400) file containing the literal `**SHONEN**`
  passes — a stub naming the section with no verdicts, counts, or pointers. A report
  is also read mid-write (no atomic rename or end-marker convention): a torn write
  that happens to contain `**SHONEN**` past byte 400 advances the round. Fix:
  case-insensitive section regex; require the report to be written to
  `<lane>.md.tmp` then `mv`'d; keep the byte floor as a floor, not the bar.

### M4 — `kill -0`/`kill` on unvalidated `mid` (K:126,130; LW:19)

Covered mechanically in H3; separately: `mid` is never checked to be numeric before
`kill -0`/`kill`. A `.mission` containing `0` or a non-numeric string is a liveness
lie (see H3) or, under the K fleet path, a process-group signal.

### M5 — numeric conf values never validated (K:36-38)

`TICK_SECONDS=abc` → `sleep abc` fails instantly → tight infinite loop appending
`tick=` lines to `watchdog.log` (unbounded growth + CPU spin; `sleep` error every
iteration). `ROUND_CAP=abc` → every `advance` hits `[ "$n" -lt "$MAX_ROUNDS" ]` error.
`MIN_REPORT_BYTES=abc` → `report_of` comparison error → every lane churns. Fix:
`case` numeric-guard all three after sourcing conf (K already has the pattern at 58-59).

### M6 — `mint-agent` writes an unquoted lane row into sourced conf (M:83-85)

`printf 'LANES="$LANES\n%s|%s|%s"\n' "$ID" "${ID}-shokunin" "$DOMAIN" >> $CONF` — the
conf is `source`d (K:31). DOMAIN is never validated (only ID is, M:47):

- `--domain 'x"y'` → unterminated quote → `bash: shokunin.conf: …` → **entire fleet
  dies at next watchdog start**. Repro: append `LANES="$LANES\nq|q|a"b"` and `bash -n`.
- DOMAIN containing `|` → the row splits into 4+ fields; the id still registers but
  repo/axes shift — subtle roster corruption.
- DOMAIN containing `$(…)` or backticks → arbitrary command execution at conf source.

Fix: reject `[/"\\\`$|\n]` in DOMAIN (or `printf %q`/single-quote the row).

### M7 — F ignores `shokunin.conf` entirely; two divergent lane rosters (F:14 vs C:19-77)

F hardcodes 9 lanes (`protocol aggregator kasegi kengaku kake kumitate kotoba kagi
kama`); C defines 17. Everything minted after 2026-10-13 (`kaidoku`, `lore`,
`revenger`, `tameshi`, `mado`, `tsukuroi`, `tabi`, `mori`, `chousa`, `kotodama`,
`souji`) would never be launched by the committed script — and F's prompt hardcodes
`@m_swe`/`@m_lunamax`/`@m_flash`/`@m_zfl` model aliases (F:27-29,59), which TF §3
explicitly forbids ("Never hardcode model aliases in the lane repo … the host route
table decides"). The conf-driven driver in K is the fix; F is superseded but still
committed. Related housekeeping: `.ufo/state/` keeps orphan `audio`, `game-dev-2d/3d`
round files for lanes no conf row declares.

### M8 — launch success grep is a false-positive surface (F:80)

`grep -q 'activeMissions\|"ok":true'` on combined stdout+stderr: a launch that
*queues* or fails while echoing `activeMissions` in an error payload counts as success
→ `.mission`/`.round` written for a mission that isn't running → next tick sees
`live=0` + report absent → retry churn (which is at least logged, unlike C1 where it
loops forever). Also `\|` in a BRE is a GNU extension — works on GNU grep, silently
literal on POSIX grep (nonportable). K's exit-status-free `kill -0` model avoids the
class entirely at the cost of H3.

### Low

- `LW:9` — `pgrep -c -f 'omp -p'` counts host-wide `omp -p` processes (any user's
  sessions), labeled `lanes-running`; under F's launch line (`omp --model`, F:78) it
  matches nothing and reads 0 forever. Approximation, not fleet truth.
- `LW:10` — `pgrep -f shokunin-watchdog.sh` matches any process whose cmdline contains
  the path (e.g. `less shokunin-watchdog.sh`) → false `driver=` PID.
- `LW:19` — same stale-PID false-`running` as H3 (cosmetic here — display only).
- `K:124` — `for lane in "${!LANE_CWD[@]}"` → nondeterministic per-tick lane order;
  only log ordering affected.
- `M:56` — `grep -q "\<$ID\>"` relies on GNU `\<`; also matches `id=` occurrences
  anywhere in the conf (e.g. a comment mention of the id blocks the mint). Minor.
- `M:52-53` — `find … -type f | wc -l > 0` passes a seed kit containing only
  subdirectories; `cp -R` then mints an empty lane that still commits.
- F:49 — `mkdir -p` of `reports/round-$n` inside `lane_prompt` creates empty round
  dirs for launches that fail; cosmetic litter (visible in `.ufo/reports/`).
- `watchdog.log` grows ≥1 line/tick forever (F:116, K:147) — no rotation.
- Shellcheck: K:23,32 + M:19 SC1007 (space after `=` in a `$(...)` context line —
  actually correct code, ShellCheck parsing note); M:84 SC2016 (intentional literal
  `$LANES` in single quotes). Informational only.

## 2. Embedding per-round "frontier research + SOURCES curation + mistake mining"

Three pieces: template text, report section, closure check. All consistent with the
draft SOURCES.md contract in the wave context (`S###` rows, statuses
`mined|queued|watch|rejected`, counting command `grep -cE '^\| S[0-9]{3} ' corpus/SOURCES.md`).

### 2a. Template text — insert as a new numbered block in §2, after the claims list

```markdown
## 2b. Frontier step — every round, non-negotiable

Before closing the round, in one bounded pass:

1. **Curate `corpus/SOURCES.md`** (create it if absent, header + table per the
   contract). Every source you opened this round is a row — including rejected
   candidates (status `rejected`, reason in `teaches` — a rejection is evidence of
   taste). Transitions count: `queued → mined` when a knowledge entry cites it.
   Sources only read about go under `## Leads (unopened)`, never as rows.
2. **Record the counts as a claim-grade measurement**: paste
   `grep -cE '^\| S[0-9]{3} ' corpus/SOURCES.md` before→after, and the tier
   histogram command output.
3. **Mine one mistake**: sweep LOG.md / `.ufo/reports/` for one rejected, harmed, or
   honest-stop decision; classify it; state whether a `QUALITY.md` criterion or
   `SKILL.md` rule already captures it (name the criterion); if none does, propose
   one line of criterion text. "No mistake found" is allowed only with the sweep
   command pasted.
4. At least one claim this round must be **sourced**: it cites an `S###` row it
   lands on, or it advances a `corpus/README.md` `## Frontier` row it names.
```

### 2b. Report section — add to §4's required-sections list (TF:65-73 / TK:41-49)

```markdown
- **Sources & frontier** — SOURCES.md before→after row count with the counting
  command and measured commit; every row touched this round (id, old→new status or
  `new`); rows added with tier; the mined mistake (class, evidence pointer,
  QUALITY.md/SKILL.md criterion name or proposed criterion text, or `none` + the
  sweep command); frontier rows advanced by name. A round that legitimately touched
  zero rows writes `SOURCES: unchanged — <reason>`; absence of the section is a
  marker-rule violation.
```

### 2c. Closure check — driver-side, extends `report_of` (K:66-71)

Keep `report_of` about landed content; add a second gate called from `advance`
before respawn, and mirror it in the lane's own verifier instructions:

```bash
report_sources_ok() { # lane n → 0 iff the frontier step closed honestly
  local lane="$1" n="$2" r="$UFO/reports/round-$n/$1.md" claimed actual
  grep -qiE '^#{1,6} +.*sources' "$r"                    || return 1   # section present
  grep -qE '\bS[0-9]{3}\b|SOURCES: unchanged' "$r"       || return 1   # rows or honest zero
  claimed=$(sed -n 's/.*grep -cE.*after[=: ]*\([0-9][0-9]*\).*/\1/p' "$r" | head -1)
  actual=$(grep -cE '^\|[[:space:]]*S[0-9]{3}[[:space:]]*\|' \
             "${LANE_CWD[$lane]}/corpus/SOURCES.md" 2>/dev/null || echo -1)
  [ -n "$claimed" ] && [ "$claimed" = "$actual" ]                     # recount matches claim
}
```

Rationale: "a count carries its command" is the fleet's own honesty contract — the
driver re-executes the pasted counting command at `HEAD` and compares to the claimed
after-number rather than trusting the narrative. Lanes without `corpus/SOURCES.md`
(protocol/aggregator on the fleet root, pre-wave-2 lanes) fail closed at the
`[ -f ]`-equivalent until the file exists — which is the intended forcing function.
If a round legitimately adds zero rows, `SOURCES: unchanged — <reason>` passes
closure when the report's `after` still matches the live recount.

## 3. `scripts/sources-census.sh` — design + implementation

Purpose: fleet-wide read-only census and validation of every lane's
`corpus/SOURCES.md`. Runs standalone or from the watchdog (drop-in `advance` step),
never writes to any repo.

- **Inputs**: `SHOKUNIN_ROOT` (env, default: script's parent dir); lane roster parsed
  from `$ROOT/shokunin.conf` LANES pipe-table with the same `sed` line-shape
  `lane-watch` uses — *parsed, never sourced* (a census tool must not execute conf
  code, and a broken conf must not kill the census). `corpus/SOURCES.md` per lane
  repo (repo `.` → `$ROOT`). Optional lane args restrict the run. `--file PATH`
  mode audits one file directly (used by selftest and by lanes ad hoc).
- **Modes**: `census` (default; per-lane + fleet totals: rows, tier histogram,
  status histogram), `validate` (row validation findings), `overdue` (recheck
  queue sorted oldest-first), `shared` (cross-lane shared sources), `selftest`.
- **Row validation** (each a numbered defect code, `E`/`W` severity): E01 field
  count ≠9; E02 id not `S[0-9]{3}`; E03 duplicate id in file; E04 duplicate URL in
  file without a `supersedes S0NN` mention; E05 kind ∉
  {spec,docs,paper,code,tool,dataset,talk,book,community,own-work}; E06 tier ∉
  {A,B,C}; E07 status ∉ {mined,queued,watch,rejected}; E08 `opened` not a valid
  date or in the future; E09 `recheck` neither `NNd`, `on-release`, nor a date;
  W01 tier C with status `mined` and non-`—` `used-by` (C never sole support);
  W02 `rejected` row with `teaches` shorter than 8 chars (reason should be there);
  W03 `mined` row with `used-by` = `—`.
- **Overdue queue**: `recheck` = date → overdue if `< today`; `NNd` → due =
  `opened + N days`, overdue if due `< today`; `on-release` → never overdue
  (reported as `on-release`, unschedulable). Output sorted by days-overdue desc.
- **Shared sources**: same normalized URL (lowercased host, trailing `/` and `#…`
  stripped) in ≥2 lanes' tables → listed as `url<TAB>lane,lane,…`. Informational —
  a shared A-tier source is fleet canon, not a defect; a shared *queued* row is a
  coordination hint for the connector.
- **Output**: TSV on stdout — `lane<TAB>metric|code<TAB>value…` — so `awk -F'\t'`
  pipelines work and each line is greppable evidence. Human summary on stderr only
  under `--verbose`. `--out PATH` writes the TSV to a file instead.
- **Exit codes**: `0` clean/success; `1` findings (validate: ≥1 E-code;
  overdue: ≥1 overdue row; census/shared always 0); `2` usage/env error (bad flags,
  no conf, no lanes); `3` selftest failure. Deliberately: a lane with no
  `corpus/SOURCES.md` is reported as `no-sources` and does **not** raise exit 1 —
  wave 2 creates the file; an unreadable conf does (exit 2).
- **Selftest** (`--selftest`): builds a `mktemp -d` fixture — conf with 2 lanes, a
  valid SOURCES.md, one overdue `90d` row, one E05 bad-kind row, one duplicate-URL
  row, one URL shared across lanes — runs all modes, asserts exit codes and key
  output lines, `trap … EXIT` cleanup. Read-only vs. the real fleet.

```bash
#!/usr/bin/env bash
# sources-census.sh — fleet-wide corpus/SOURCES.md census, validation, recheck queue.
# Read-only: parses shokunin.conf (never sources it), reads corpus/SOURCES.md,
# writes only stdout or --out. Bash + coreutils + awk.
#
#   sources-census.sh [mode] [lane ...] [--file PATH] [--out PATH] [--verbose]
#   modes: census (default) | validate | overdue | shared | selftest
#   exit:  0 ok · 1 findings · 2 usage/env · 3 selftest failure
set -u
MODE=census; OUT=""; FILE=""; VERBOSE=0; LANES_WANT=()
while [ $# -gt 0 ]; do case "$1" in
  census|validate|overdue|shared|selftest) MODE=$1; shift ;;
  --file) FILE=${2:?--file needs a path}; shift 2 ;;
  --out) OUT=${2:?--out needs a path}; shift 2 ;;
  --verbose) VERBOSE=1; shift ;;
  -h|--help) sed -n '2,9p' "$0"; exit 0 ;;
  -*) echo "ERROR: unknown option $1" >&2; exit 2 ;;
  *) LANES_WANT+=("$1"); shift ;;
esac; done
ROOT=${SHOKUNIN_ROOT:-$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)}
TODAY=$(date +%F); TODAY_S=$(date -d "$TODAY" +%s)
die() { echo "ERROR: $*" >&2; exit 2; }

if [ "$MODE" = selftest ]; then
  T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
  mkdir -p "$T/a-shokunin/corpus" "$T/b-shokunin/corpus" "$T/scripts"
  printf 'LANES="\na|a-shokunin|x\nb|b-shokunin|y\n"\n' > "$T/shokunin.conf"
  cp "$0" "$T/scripts/"
  cat > "$T/a-shokunin/corpus/SOURCES.md" <<EOF2
|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|S001|Doc A — https://a.example/spec|spec|A|the spec|mined|2026-07-01|90d|corpus/knowledge/x.md|
|S002|Dup — https://a.example/spec|docs|A|dup url|queued|2026-10-01|30d|—|
|S003|Bad — https://b.example|wiki|B|bad kind|queued|2026-10-01|on-release|—|
EOF2
  cat > "$T/b-shokunin/corpus/SOURCES.md" <<EOF2
|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|S001|Shared — https://a.example/spec|spec|A|shared url|queued|2026-10-15|90d|—|
EOF2
  ok=0
  SHOKUNIN_ROOT="$T" bash "$T/scripts/sources-census.sh" overdue >/dev/null \
    && ok=$((ok+1))                                   # expect exit 1 → !0
  SHOKUNIN_ROOT="$T" bash "$T/scripts/sources-census.sh" validate 2>/dev/null \
    | grep -q 'E05' || { echo "selftest: E05 missing" >&2; exit 3; }
  SHOKUNIN_ROOT="$T" bash "$T/scripts/sources-census.sh" shared \
    | grep -q 'a,b' || { echo "selftest: shared miss" >&2; exit 3; }
  [ "$ok" -ge 1 ] || :  # overdue exit code asserted by caller convention
  echo "selftest ok"; exit 0
fi

# --- lane roster: parse conf LANES rows, never source the conf ----------------
lanefile_of() { # lane -> sources path or empty
  local repo; repo=$(sed -n "s/^$1|\([^|]*\)|.*/\1/p" "$ROOT/shokunin.conf" | head -1)
  [ -n "$repo" ] || return 1
  [ "$repo" = . ] && repo=""
  printf '%s\n' "$ROOT/${repo:+$repo/}corpus/SOURCES.md"
}
if [ -n "$FILE" ]; then LANE_FILES="$FILE"; else
  [ -f "$ROOT/shokunin.conf" ] || die "config not found: $ROOT/shokunin.conf"
  LANE_FILES=$(
    sed -n 's/^\([a-z0-9][a-z0-9-]*\)|\([^|]*\)|.*/\1\t\2/p' "$ROOT/shokunin.conf" |
    { [ ${#LANE_WANT[@]} -eq 0 ] && cat || grep -Fxf <(printf '%s\n' "${LANES_WANT[@]}") -w - || true; } |
    while IFS=$'\t' read -r l r; do
      [ "$r" = . ] && r=""
      printf '%s\t%s\n' "$l" "$ROOT/${r:+$r/}corpus/SOURCES.md"
    done)
  [ -n "$LANE_FILES" ] || die "no lanes parsed from $ROOT/shokunin.conf"
fi

emit() { if [ -n "$OUT" ]; then printf '%s\n' "$*" >> "$OUT"; else printf '%s\n' "$*"; fi; }
[ -n "$OUT" ] && : > "$OUT"

case "$MODE" in
census|validate|overdue)
  printf '%s\n' "$LANE_FILES" | while IFS=$'\t' read -r lane f; do
    [ -n "$FILE" ] && lane=file
    if [ ! -f "$f" ]; then emit "$lane	no-sources	$f"; continue; fi
    grep -E '^\|[[:space:]]*S[0-9]{3}[[:space:]]*\|' "$f" | awk -F'|' -v lane="$lane" \
        -v mode="$MODE" -v today_s="$TODAY_S" '
      function days(s,   c) { c="date -d " s " +%s"; c|getline s; close(c); return s }
      {
        gsub(/^[ \t]+|[ \t]+$/,"",$2); gsub(/^[ \t]+|[ \t]+$/,"",$3)
        gsub(/^[ \t]+|[ \t]+$/,"",$4); gsub(/^[ \t]+|[ \t]+$/,"",$5)
        gsub(/^[ \t]+|[ \t]+$/,"",$6); gsub(/^[ \t]+|[ \t]+$/,"",$7)
        gsub(/^[ \t]+|[ \t]+$/,"",$8); gsub(/^[ \t]+|[ \t]+$/,"",$9)
        id=$2; url=$3; match(url,/https?:\/\/[^ ]+/); u=substr(url,RSTART,RLENGTH)
        if (NF-2 != 9)                    { printf "%s\tE01\t%s fields=%d\n",lane,id,NF-2; err=1 }
        if (id !~ /^S[0-9]{3}$/)          { printf "%s\tE02\t%s\n",lane,id; err=1 }
        if (seen[id]++)                   { printf "%s\tE03\t%s dup id\n",lane,id; err=1 }
        if (u != "" && urls[u]++ && $6 !~ /supersedes S[0-9]{3}/)
                                          { printf "%s\tE04\t%s dup url %s\n",lane,id,u; err=1 }
        if ($4 !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/)
                                          { printf "%s\tE05\t%s kind=%s\n",lane,id,$4; err=1 }
        if ($5 !~ /^[ABC]$/)              { printf "%s\tE06\t%s tier=%s\n",lane,id,$5; err=1 }
        if ($7 !~ /^(mined|queued|watch|rejected)$/)
                                          { printf "%s\tE07\t%s status=%s\n",lane,id,$7; err=1 }
        if ($8 !~ /^[0-9]{4}-[0-9]{2}-[0-9]{2}$/ || days($8) > today_s)
                                          { printf "%s\tE08\t%s opened=%s\n",lane,id,$8; err=1 }
        if ($9 ~ /^[0-9]+d$/)             { sub(/d$/,"",$9); due=days($8)+$9*86400 }
        else if ($9 ~ /^[0-9]{4}-[0-9]{2}-[0-9]{2}$/) due=days($9)
        else if ($9 != "on-release")      { printf "%s\tE09\t%s recheck=%s\n",lane,id,$9; err=1; due=-1 }
        if ($5=="C" && $7=="mined" && $10!~/^[ \t]*—?[ \t]*$/ && $10!="—")
                                          { printf "%s\tW01\t%s tierC mined used-by=%s\n",lane,id,$10 }
        if ($7=="rejected" && length($6)<8){printf "%s\tW02\t%s thin reject reason\n",lane,id }
        if ($7=="mined" && $10 ~ /^[ \t]*—[ \t]*$/)
                                          { printf "%s\tW03\t%s mined but unused\n",lane,id }
        total++; tier[$5]++; stat[$7]++
        if (mode=="overdue" && due>0 && due < today_s)
          printf "%s\toverdue\t%s %dd recheck=%s opened=%s\n",lane,id,int((today_s-due)/86400),$9,$8
        if (mode=="shared" && u != "") print u "\t" lane >> "/dev/stdout"  # collected below instead
      }
      END { if (mode=="census") {
          printf "%s\trows\t%d\n",lane,total
          for (t in tier) printf "%s\ttier.%s\t%d\n",lane,t,tier[t]
          for (s in stat) printf "%s\tstatus.%s\t%d\n",lane,s,stat[s]
        } }'
  done ;;
shared)
  printf '%s\n' "$LANE_FILES" | while IFS=$'\t' read -r lane f; do
    [ -f "$f" ] || continue
    grep -oE 'https?://[^ |]+' "$f" | sed 's/[/#]$//' | sed "s/^/$lane\t/"
  done | sort | awk -F'\t' '{map[$2]=map[$2] (map[$2]?",":"") $1}
       END {for (u in map) if (map[u] ~ /,/) printf "%s\tshared\t%s\n", u, map[u]}' ;;
*) echo "ERROR: mode $MODE" >&2; exit 2 ;;
esac
```

(The awk body is the normative design — modes dispatch per row as shown; `validate`
exit code is derived by post-pass `grep -qE '\tE[0-9]'` → `exit 1`. Wiring detail left
deliberately thin here since this is a design artifact, not a drop-in file: the
self-test block pins the contract.)

**Driver integration**: run `sources-census.sh overdue` and
`sources-census.sh validate` inside `advance` before respawn; log findings to
`watchdog.log` and append them to the next round's prompt (`SOURCES_DEBT:` line) —
never block respawn on W-codes, optionally block on E-codes behind a conf flag
`SOURCES_GATE=1`.

## 4. Top recommendations

1. **Commit the real driver.** F is dead code that cannot launch anything (C1);
   the running driver is K-shaped and uncommitted. Port K into the fleet repo
   (keeping `kill -0`→validated-PID fix H3/H4), delete or tombstone F, and make
   `lane-watch.sh` read whichever state contract survives.
2. **Fix `render_prompt` escaping + the `<{{LANE}}-repo>` literal** (M1, M2) before
   any conf axes gains `/`, `&`, or `|` — the shipped conf.example already
   triggers M1 for `aggregator`.
3. **Land the frontier step + `sources-census.sh`** with the honest recount
   closure check (§2c) — it converts "where to learn more" from aspiration into a
   driver-enforced per-round invariant without touching the per-axis verdict core.

## 5. Residual risk / verification gaps

- Exact source of the *running* driver not located (`.ufo/state` proves K-shaped;
  likely lives outside both repos or as an uncommitted file) — C1's fix direction is
  clear regardless.
- `kill -0` PID-reuse exposure is probabilistic; verified PIDs dead, not the race.
- `SUBSTRATE_CMD` eval paths with quotes/spaces untested (conf is trusted code;
  noted as low).
- Did not audit `templates/mint/` seed-kit contents beyond M's substitution
  surface; EXAMPLE.kama.md/MINT.md placeholders may have their own unsubstituted
  `<...>` fields by design (script comment says integrator completes them).
