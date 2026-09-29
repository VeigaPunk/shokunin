# ItemsScout — ground-truth census of `SKILL.md` §Credential-hygiene checklist

Round 15 · lane kagi-shokunin · scope: the 16-item checklist surface only.
Repo `/home/vgpnk/projects/shokunin/kagi-shokunin`. HEAD advanced mid-census
`baec94f` → **`2486643`** (round-14 committed by L1); `SKILL.md` is clean at HEAD,
so the "working tree" numbers below are the committed `2486643` content — the
censused surface did not move under me. Round-13 close = `git show 4b8c018:SKILL.md`.
L1's new gate landed untracked at 22:29 (`corpus/checklist-run.sh`, 19460 B);
`corpus/checklist.tsv` did not exist yet when this census closed (§6).

Every claim below is a command I ran. `[INFERENCE]` marks judgement, not observation.

---

## 1. Count: confirmed 16, unchanged since round 13

```
cd /home/vgpnk/projects/shokunin/kagi-shokunin
awk '/^## Credential-hygiene checklist/,/^## Evidence-receipt patterns/' SKILL.md | grep -c '^- \[ \]'
# -> 16
git show 4b8c018:SKILL.md | awk '/^## Credential-hygiene checklist/,/^## Evidence-receipt patterns/' | grep -c '^- \[ \]'
# -> 16
```

| surface | WT | `4b8c018` (r13) | `2486643` (r14) |
|---|---|---|---|
| section header | `SKILL.md:419` | `:406` | — |
| item starts | `SKILL.md:422–429`, `432–439` | `:409–416`, `419–426` | — |
| item count | **16** | **16** | **16** |

- 8 items under `Evidence production:` (`SKILL.md:421` WT / `:408` r13),
  8 under `Handler operation:` (`SKILL.md:431` WT / `:418` r13).
- Section body is **byte-identical** between `4b8c018` and the working tree:
  `diff <(git show 4b8c018:SKILL.md | awk '/^## Credential-hygiene checklist/,/^## Evidence-receipt patterns/') <(awk '/^## Credential-hygiene checklist/,/^## Evidence-receipt patterns/' SKILL.md)` → no output.
  All 16 item line numbers shift by exactly **+13** (round-14 added 13 lines above the section).

### Growth trajectory (why every older count is wrong)

```
for c in $(git log --format=%h --reverse -- SKILL.md); do
  printf '%s ' "$c"
  git show $c:SKILL.md | awk '/^## Credential-hygiene checklist/,/^## Evidence-receipt patterns/' | grep -c '^- \[ \]'
done
```

| commit | round | items |
|---|---|---|
| `9b3e49f` | 2 | 10 |
| `06ef644`…`5f55ba8` | 3–6 | 10 |
| `51c9d30` | 7 | 12 |
| `148ae5c` | 8 | 13 |
| `ea77bf0` (r8-close HEAD) | 8 | **13** |
| `e64e81b` | 9 | 14 |
| `03477c0` / `301b9ec` | 10 / 11 | 14 |
| `4b8c018` | 13 | **16** |
| `2486643` | 14 | 16 |

Items entered the checklist in rounds 7, 8, 9 and 13. **No revision ever held 15
items** — the "15-item" number was never true, and it is now stale by one round
of growth as well.

---

## 2. Wrong-count assertions — `path:line` pointers

| # | pointer | asserted | truth at that revision | truth today | status |
|---|---|---|---|---|---|
| D1 | `SCORECARD.md:16` | "a **15-item** hygiene checklist" (pre-move table measured at `ea77bf0`) | 13 at `ea77bf0` | 16 | **wrong twice** — wrong by 2 when written, stale by 3 now |
| D2 | `corpus/lessons/round-6-aggregator-audit.md:51` | row 18: `SCORECARD.md:16` depth counts … "**15-item** checklist" → `❌ (defect 2)` | measured 13 (`ea77bf0`) / 14 | 16 | **quarantined defect record, numbers correct for what it measured**; carries the bad string, never re-measured after growth |
| D3 | `corpus/lessons/round-6-aggregator-audit.md:68` | quotes the falsified claim verbatim ("a **15-item** hygiene checklist") | — | — | same record, part of the defect entry that starts at `:67` |
| D4 | `corpus/lessons/round-6-aggregator-audit.md:72-73` | "checklist `13`/`14`" | correct at its two revisions | now 16 | **stale by growth**, not a miscount when written |
| D5 | `corpus/lessons/round-6-aggregator-audit.md:193` | open-issue index restating "15-item checklist … all falsified (…, 13\|14, …)" | — | 16 | index row, same string + same staleness |
| D6 | `SCORECARD.md:209` | "Falsifiable target for the next round: … add ledger rows that measure … **the checklist item count**" | — | — | **not a wrong count — the r13 self-named gap.** Round 15's `checklist-run.sh` + a ledger row closes exactly this |
| — | `PROVINCE.md` | **no item count is asserted anywhere** | — | — | refuted as a defect site |

Supporting greps:

```
grep -rn "15-item\|16-item\|13-item\|14-item\|item hygiene\|hygiene checklist" --include=*.md --include=*.tsv --include=*.sh .
grep -n "checklist\|hygiene\|15-item\|16-item" PROVINCE.md
# PROVINCE.md -> only :3 "credential hygiene evidence" (prose, no count)
grep -n "operator judgement\|checklist item\|checklist items\|runnable command" SCORECARD.md
# :40, :62, :84 -> "12 checklist items [still] operator judgement" (rounds 9-11)
```

`SCORECARD.md:40/62/84` add a second, count-adjacent defect: "**12** checklist items
[are] still operator judgement". At round 9 the checklist held 14 items, at round 10
it held 14, at round 11 it held 14 — a "12 manual" reading implies 2 runnable when
item 1, item 5 and item 15 each already named a live gate (3 liable). **Wrong at
every revision it appears in, and unmeasured by any row.** [INFERENCE] — the exact
split is a judgement call, but ≥3 items named an existing gate at every one of those
revisions.
`SCORECARD.md:18` (round-9 pre-move) states the same shape for items 1/5/15.

Other mentions carry no number and are fine: `LOG.md:19`,
`corpus/lessons/round-8-aggregator-box3-coldrun.md:62`, `SCORECARD.md:38/60/82`,
`SKILL.md:419` (the header itself).

---

## 3. The 16-row table

Legend for **current repo verification** — does any *committed gate*
(`corpus/*.sh` + the `.tsv` data it reads) mechanically assert the path/symbol the
item names, today?
- **FULL** — a green gate's verdict *is* the item's claim.
- **PARTIAL** — some named symbol/path is pinned, the item's own duty is not.
- **NONE** — no gate names it; the item is prose-only.
- **banned-cmd** — the item's own named command is excluded from the new gate
  (contract: no `claim-ledger.sh`, no `op` exec, no vault read, no mutate).

| # | sec | WT L | r13 L | runnable cmd named in the item | current verification | gap to a runnable row |
|---|---|---|---|---|---|---|
| 1 | Evidence | 422 | 409 | `bash corpus/surface-census.sh`; `bash corpus/drift-pins.sh`; `--pin`; **`bash corpus/claim-ledger.sh verify`**; re-`stamp` | **FULL** for census+drift-pins (`surface-census.tsv` pins every named mode; `drift-pins` verdict `files=15 symbols=20` = the item's own "15 files / 20 pins"). `claim-ledger.sh` leg = **banned-cmd** | drop the ledger leg; row = census (+drift-pins) |
| 2 | Evidence | 423 | 410 | `--pin` (drift-pins) | **NONE for the duty** — mechanism exists (`drift-pins.sh:314` `REPIN`, `:242`/`:356` `MOVED`, usage `:29`), nothing verifies a round *reported* them | by-hand (`manual-change`) or a new "no unreported drift" check |
| 3 | Evidence | 424 | 411 | none (`status`, `cdp-bridge status`, `tac-check` are *subjects*, not commands to run) | **NONE** — `cdp-bridge status` verb exists (`knowledge/janitor-command-surface.md:23`), `tac-check` is a pinned asset; the quoting rule is unenforced | by-hand (`operator-scope`) |
| 4 | Evidence | 425 | 412 | none (`refs` is the subject) | **NONE** — no gate sweeps artifacts for ref paths. Round-6's sweep was an ad-hoc `grep`, not a committed row. See §5 finding F4: `surface-census.sh:516-528` proves `refs` prints the ref path **verbatim** and only redacts the plain value, so the duty is real and unmechanised | runnable is *authorable* (runtime-assembled ref-shape sweep) — currently absent |
| 5 | Evidence | 426 | 413 | `bash corpus/op-ref-probe.sh`; `op run --env-file=<f> -- printenv <KEY>` | **FULL** — probe green (`checks=44 oprun=12 refs=7 divergent=5 edge=10 sig=6`), pinned by ledger rows `R12-01`/`R12-02` | row = `op-ref-probe.sh` |
| 6 | Evidence | 427 | 414 | none (`the-janitor run` is the subject) | **PARTIAL** — the *masking claim* is mechanically pinned inside `op-ref-probe.sh` (it measures 4 plain-value shapes); the "never paste run output" duty is not | runnable shares item 5's gate; duty otherwise by-hand (`authoring-duty`) |
| 7 | Evidence | 428 | 415 | none | **PARTIAL** — receipt machinery pinned: `drift-symbols.tsv` `tac-check:63 LOCAL_RECEIPT_INTEGRITY: OK`, `:69 LIVE_ACCESS_NOW`; `state-shape.tsv` pins `tac-daybreak-blue.json` keys incl. `receipt_sha256`, `verification_method`, `evidence_scope` | scope-wording duty by-hand (`authoring-duty`) |
| 8 | Evidence | 429 | 416 | none | **PARTIAL / asymmetric** — `drift-symbols.tsv` pins `handoff-status.json` `#1 "boundaries"` and `#1 credentials_in_evidence`; **`target_authority_conferred` appears in ZERO gate files** | needs a new pin, else by-hand |
| 9 | Handler | 432 | 419 | none | **PARTIAL + mis-attributed** — `surface-census.tsv:36` pins `client.lock` mode 600 and `state-shape.tsv` pins it as `lock` kind; **nothing asserts the flock/one-at-a-time behaviour**, and `surface-census.tsv:22` files "lock" under `client.py` although flock lives in `~/.local/bin/the-janitor` | by-hand (`runtime-behavior`), and the census note is a live inaccuracy |
| 10 | Handler | 433 | 420 | none | **NONE** — `AUTH_REQUIRED` occurs in gate files only as *note text* (`surface-census.tsv:28`, janitor_auth.ts description), never as an assertion; handler is stopped today so the behaviour is unobservable | by-hand (`runtime-behavior`) |
| 11 | Handler | 434 | 421 | none | **PARTIAL, 2 of 3 knobs** — `drift-symbols.tsv` pins `opencode.json:4 "share": "disabled"`, `:5 "enabled_providers"`, `:16 baseURL`, plus the global `~/.config/opencode/opencode.json` by `drift-baseline.tsv` hash. **`autoupdate` appears in ZERO gate files** | 2/3 covered by `drift-pins`; the third needs a row |
| 12 | Handler | 435 | 422 | none | **FULL** — `drift-symbols.tsv` `janitor.md:8 ^  "\*": deny` + `drift-baseline.tsv` pins `janitor.md` by full-file sha256 (so `janitor_auth: allow` front-matter is byte-pinned) and `janitor_auth.ts` by sha256 | row = `drift-pins.sh` |
| 13 | Handler | 436 | 423 | none | **PARTIAL** — `surface-census.tsv` pins `chrome-profile` (asset, mode `-`, note "CONTESTED with kake") + the NMH manifest (600, `drift-baseline.tsv` sha256). **Port 9222 has no gate** (see §5 F3) | report/lease duty by-hand (`cross-lane`) |
| 14 | Handler | 437–439 | 424–426 | none | **FULL** — persistence is exactly what `transcript-scan.sh` detects (`HITS=2`, exit 1 by design) and `state-shape.tsv` pins `opencode.db` magic/mode/tables/rows; `surface-census.tsv` marks the `opencode.db` runtime row "durable transcripts" | row = `transcript-scan.sh` (`expect_exit 1`) |
| 15 | Handler | 440–443 | 427–430 | `corpus/transcript-scan.sh` | **FULL** — the item *is* a live verdict gate; ledger `R11-06`/`R11-07` pin it | row = `transcript-scan.sh` |
| 16 | Handler | 444–447 | 431–434 | none | **NONE** — `40961` and `OPENCODE_SERVER_PASSWORD`: **0 occurrences in every `corpus/*.sh` + `corpus/*.tsv`**; no listener today (0 established sockets), so even a runtime check only proves absence | by-hand (`runtime-behavior`) |

Runnable-by-existing-gate today = items **1, 5, 12, 14, 15** (5 items, 4 distinct
commands: `surface-census.sh`, `drift-pins.sh`, `op-ref-probe.sh`, `transcript-scan.sh`).
Item 1 must drop its `claim-ledger.sh verify` leg (**contract: recursion**) and its
`--pin` leg (mutates). [INFERENCE] Items 4, 8, 11 are mechanised-able from *new*
per-item checks (ref-shape sweep; a `target_authority_conferred` pin; an `autoupdate`
check on `~/.config/the-janitor/opencode.json`) — all read non-secret host files the
census already reads. Items 2, 3, 9, 10, 13, 16 have no available mechanism and are
the honest by-hand set (classes: `manual-change`, `operator-scope`, `runtime-behavior`,
`runtime-behavior`, `cross-lane`, `runtime-behavior`).

### Verbatim duty sentences

Item texts (working tree; `4b8c018` text is identical) —

```
1  SKILL.md:422  - [ ] Record mechanism and metadata: paths, modes (`op.env`/`config.json`/`opencode.json`/`client.py` 0600–0755 in `$CONFIG_DIR`; state dir 0700; `client.lock`/`session-id` 0600 in `$STATE_DIR`), verb names, exit codes, field names. **`bash corpus/surface-census.sh` first** (round 10): exit 0 = every declared path still has its declared kind/mode, no undeclared child sits in the 4 enumerable dirs, and every runtime shape floor holds. Then `bash corpus/drift-pins.sh`: exit 0 = every pinned host file and symbol pin still matches the committed baseline (15 files / 20 pins as of round 12; 19 before it). Non-zero on either = re-read the named path before citing it. New cited file ⇒ census row (reviewed commit; there is no `--pin`) **and** a drift-pins `--pin` once. In-repo artifacts: run `bash corpus/claim-ledger.sh verify` first and cite the stamped revision (`corpus/stamps.tsv`); after landing edits, re-`stamp` (reviewed commit) — a `STALE` row means the artifact moved under the citation.
2  SKILL.md:423  - [ ] After any intentional host-file change (endpoint fix, config edit), run `--pin` **once** and report the `REPIN`/`MOVED` lines you accepted — that is the durability of every line ref in this corpus. Never re-pin inside the same round that discovers the drift.
3  SKILL.md:424  - [ ] Quote command output only when it is metadata-only (`status`, `cdp-bridge status`, `tac-check` block).
4  SKILL.md:425  - [ ] `refs` output: key names OK for internal use; ref paths stay out of artifacts.
5  SKILL.md:426  - [ ] Before relying on a key inventory, run `bash corpus/op-ref-probe.sh` (exit 0 = the `op.env` contract still holds on this host) and remember what it pins: `refs` answers about *lines*, `op run` answers about *loaded variables*. For a specific file, list keys with `op run --env-file=<file> -- printenv <KEY>`; `export`/spaced/lowercase/quoted-ref lines are where the two diverge.
6  SKILL.md:427  - [ ] Never paste `the-janitor run` output: plain-valued keys are **not** masked (only resolved refs are). Check a value's class before quoting it, and never write a plain secret into `op.env` expecting masking.
7  SKILL.md:428  - [ ] Receipts/checksums bind *bytes*: state scope explicitly ("local receipt integrity only"), never imply provider attestation or live access.
8  SKILL.md:429  - [ ] Handoffs carry context + receipt *path*; `handoff-status.json` `boundaries` is the vocabulary: `credentials_in_evidence: false`, `target_authority_conferred: false`.
9  SKILL.md:432  - [ ] One request at a time — `client.lock` flock serializes machine-wide; queue instead of racing.
10 SKILL.md:433  - [ ] After `stop`, expect `AUTH_REQUIRED` on next request until the operator re-approves.
11 SKILL.md:434  - [ ] Keep `config_overlay` (`opencode.json`) intact: `enabled_providers: ["qwen-local"]`, `share: disabled`, `autoupdate: false` — the gate is post-merge, so the *global* `~/.config/opencode/opencode.json` also reaches the handler (providers/agents/plugins load; janitor deny + `enabled_providers` contain them). Global-config edits are an attack/drift surface on janitor.
12 SKILL.md:435  - [ ] Never widen `janitor` agent permissions (`{"*": deny, janitor_auth: allow}`) — `janitor_auth` ignores all `op` output for a reason.
13 SKILL.md:436  - [ ] CDP port 9222 + musketeer profile are shared with the kake fleet: report lease conflicts, don't absorb them.
14 SKILL.md:437-439  - [ ] Never put secret-adjacent text into a request expecting memory-only / handling — transcripts persist in `xdg-data/opencode/opencode.db` past / `stop`; purge = stop + `rm -rf xdg-data` (no verb).
15 SKILL.md:440-443  - [ ] Run `corpus/transcript-scan.sh` after any request that carried / credential-shaped stdin, before/after operator-signin experiments, and / alongside `drift-pins.sh` — exit 0 `CLEAN` (WARN cells allowed), exit 1 = / finding: report `HIT` lines + counts only, never the matched rows.
16 SKILL.md:444-447  - [ ] Treat `127.0.0.1:40961` as unauthenticated handler access: no local / process should POST to it, and enabling `OPENCODE_SERVER_PASSWORD` without / a `client.py` Authorization header breaks `request` (server_healthy 401 → / foreign-server text). Rollout recipe: `corpus/knowledge/control-plane-hardening.md`.
```

---

## 4. Exact grep commands used

```bash
cd /home/vgpnk/projects/shokunin/kagi-shokunin

# item count, both revisions (section-scoped, not a bare `- [ ]` grep)
awk '/^## Credential-hygiene checklist/,/^## Evidence-receipt patterns/' SKILL.md | grep -c '^- \[ \]'
git show 4b8c018:SKILL.md | awk '/^## Credential-hygiene checklist/,/^## Evidence-receipt patterns/' | grep -c '^- \[ \]'

# per-revision trajectory
for c in $(git log --format=%h --reverse -- SKILL.md); do printf '%s ' "$c"; git show $c:SKILL.md \
  | awk '/^## Credential-hygiene checklist/,/^## Evidence-receipt patterns/' | grep -c '^- \[ \]'; done
git show ea77bf0:SKILL.md | awk '/^## Credential-hygiene checklist/,/^## Evidence-receipt patterns/' | grep -c '^- \[ \]'   # 13

# line maps + byte-identical body
grep -n '^- \[ \]' SKILL.md | head -20
git show 4b8c018:SKILL.md | grep -n '^- \[ \]' | sed -n '1,20p'
diff <(git show 4b8c018:SKILL.md | awk '/^## Credential-hygiene checklist/,/^## Evidence-receipt patterns/') \
     <(awk '/^## Credential-hygiene checklist/,/^## Evidence-receipt patterns/' SKILL.md)

# count-defect sites
grep -rn "15-item\|16-item\|13-item\|14-item\|item hygiene\|hygiene checklist" --include=*.md --include=*.tsv --include=*.sh .
grep -n "checklist\|hygiene\|15-item\|16-item" PROVINCE.md
grep -n "operator judgement\|checklist item\|checklist items\|runnable command" SCORECARD.md

# per-item: does any gate name the path/symbol?
for s in autoupdate '"janitor_auth"' target_authority_conferred credentials_in_evidence 9222 40961 \
         AUTH_REQUIRED OPENCODE_SERVER_PASSWORD flock client.lock masking 'op run' handoff-status; do
  printf '%-24s ' "$s"; grep -c "$s" corpus/*.sh corpus/*.tsv 2>/dev/null | grep -v ':0$' | tr '\n' ' '; echo
done
grep -n "janitor_auth\|autoupdate\|allow" corpus/drift-symbols.tsv corpus/drift-baseline.tsv corpus/state-shape.tsv
grep -rn "ref-shaped\|REF_SHAPE\|refshape" corpus/*.sh          # only op-ref-probe.sh + surface-census.sh, neither sweeps artifacts
grep -n "SKILL.md\|corpus/\*.md\|artifacts" corpus/*.sh          # no gate scans repo docs for ref shapes

# pin inventory behind items 1/12/14
grep -c '^\$HOME' corpus/drift-baseline.tsv      # 15
grep -c '^\$HOME' corpus/drift-symbols.tsv       # 20
grep -cv '^#' corpus/surface-census.tsv          # 35 (20 asset / 15 runtime)
grep -cv '^#' corpus/state-shape.tsv             # 22
grep -n "REPIN\|MOVED\|--pin\|PINNED\|usage" corpus/drift-pins.sh
sed -n '516,528p' corpus/surface-census.sh       # the `refs` verbatim/redaction probe
```

(Policy check: the *unexecuted* `git show … | grep -c` in
`corpus/lessons/round-6-aggregator-audit.md:73` is the audit's own recorded command;
I re-ran the section-scoped form above rather than that literal, because the literal
counts every `- [ ]` in the file, not just this section. At `e64e81b` both forms
agree at 14 — coincidence, not a shared method.)

---

## 5. Findings that matter for `checklist-run.sh` / `checklist.tsv`

**F1 — count is 16, no revision ever held 15.** `SCORECARD.md:16` is the only
live wrong-count assertion; the round-6 audit rows are a correct-at-the-time
record now stale by growth. `PROVINCE.md` is clean. `SCORECARD.md:209` already
names "the checklist item count" as the round-15 falsifiable target — a ledger row
`grep -c` / section-scoped awk of the count closes it; making the *gate* itself
report `items=N` means the count is a verdict, not prose. [INFERENCE] The honest
row is `expect_lastline` on `CHECKLIST_RUN: CLEAN (items=16 …)`.

**F2 — item 1's own command list is un-runnable under the contract.** It names
`bash corpus/claim-ledger.sh verify` (recursion — the contract bans a checklist row
invoking the ledger) and `--pin`/re-`stamp` (mutating). Its runnable row must be
census + drift-pins only, i.e. the row is *narrower* than the item text. Worth
stating in the item or the gate's `--list` output, else the gate silently drops
half of item 1.

**F3 — `grep -c 9222 corpus/*.tsv` hits are a false positive.** The only gate-file
match is `corpus/stamps.tsv:12` — `811572dcf6…e9222ed6…` contains the digit run
`9222` inside a sha256. Port 9222 (item 13) has **no** gate. Any future row must
match the port in a structural context (e.g. `:9222`/`ss -ltn`), not a bare digit
string, or the gate will report clean for the wrong reason.

**F4 — item 4 is inverted by what the gate actually proves.** `surface-census.sh:516-528`
asserts `ref-verbatim yes` (the fabricated `op://`-shaped value **is printed**) and
`plain-redacted yes` (a plain identifier becomes `<redacted-non-op-value>`). So
`the-janitor refs` emits ref paths and redacts plain values — the opposite of a
reader's intuition, and precisely the leak item 4 forbids in artifacts. Combined
with "no gate sweeps artifacts for ref shapes" (only `op-ref-probe.sh` and
`surface-census.sh` contain any ref-shape logic, and both only guard fixtures), item
4 is the strongest candidate for *new* mechanisation: a runtime-assembled
ref-shape sweep over `corpus/` + root docs, `expect_exit 0`. Round-6's sweep
(`round-6-aggregator-audit.md:202`) found 1 residual line
(`transcript-scan.sh:242`, synthetic scratch seed) — an existing row would need that
declared exclusion.

**F5 — three named symbols are pinned nowhere.** `target_authority_conferred`
(item 8), `autoupdate` (item 11), `40961`/`OPENCODE_SERVER_PASSWORD` (item 16):
`0` matches across all `corpus/*.sh` and `corpus/*.tsv`. Items 8 and 11 are
therefore *partially* mechanised (their other symbols are pinned), which is the
failure mode the new gate must not paper over: a row that passes on
`credentials_in_evidence` alone would report item 8 CLEAN while
`target_authority_conferred` is unchecked. [INFERENCE] Cheapest fix in-lane:
one `drift-symbols.tsv` row for `target_authority_conferred` (`#1`) and one for
`"autoupdate": false` on the pinned overlay — both are non-secret host files the
baseline already reads.

**F6 — item 9's census note attributes flock to the wrong file.** Host facts
(L12/L130/139/175-176 of `~/.local/bin/the-janitor`) put the flock there;
`client.py` has `0`. `corpus/surface-census.tsv:22` describes `client.py` as
"HTTP client: lock, session-id, request timeout", and PROVINCE.md repeats it. The
row's *mode* pin (600 on `client.lock`) is right; the prose is wrong, and no gate
asserts the locking behaviour at all. [INFERENCE] A truthful runnable row is a
presence check of `flock` in the-janitor (2 hits) — it would *fail* against the
current mis-attribution narrative, so the census note should be corrected in the
same round rather than left to contradict the gate.

**F7 — item 15's gate exits 1 by design.** `transcript-scan.sh` →
`TRANSCRIPT_SCAN: HITS=2`, exit 1 (ledger `R11-06` pins that expectation). So a
runnable row for items 14/15 needs `expect_exit 1` + `expect_lastline` on the HITS
verdict — the contract's integer `expect_exit` already allows this; `0|1`-style
alternatives would be weaker (they cannot distinguish "clean" from "known baseline").

---

## 6. Cross-check against the landed gate (`corpus/checklist-run.sh`, untracked @ 22:29)

**Status when first written:** `corpus/checklist.tsv` did not exist yet (`ls corpus/checklist*`
→ only the `.sh`). **Now landed** — the gate runs green
(`CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7`, `CHECKLIST_RUN: CLEAN`, exit 0, 2.35 s)
and the rows are censused in §7. The script is L1's; I did **not** edit it.
Read-only observations from the first pass:

- **Item counting matches this census, mechanically.** `extract_items()`
  (`checklist-run.sh:85-104`) walks from `## Credential-hygiene checklist` to the
  next `## ` line and counts `- [ ] ` starts, folding indented continuations into
  the item text. That is the section-scoped method of §1 → `items_n=16`. It then
  asserts `ROWS_N == items_n` (`UNDECLARED`/`EXTRA`, `:189-190`), so the gate is
  self-checking against the same surface this census measured.
- **Contract ↔ implementation column drift.** The stated contract for
  `checklist.tsv` is 6 columns (`id class cmd expect_exit expect_lastline note`);
  the landed `load_rows` (`:106-122`) parses **8**:
  `id class lead check expect_exit expect_last reason note` — an extra `lead`
  column (the item's lead sentence) at position 3, and `reason` split out from
  `note`. Anyone writing rows from the 6-column contract will hit
  `POLICY row …: N columns, want 8`.
- **The recursion ban is NOT enforced.** `DENY_CHECK`
  (`checklist-run.sh:61`) = `op\.env|op run|op read|op inject|the-janitor start|the-janitor stop`
  — `corpus/claim-ledger.sh` is absent, and the string `claim-ledger` appears
  nowhere in the script (`grep -n "claim-ledger" corpus/checklist-run.sh` → no
  match). Cross-checked with the census: **item 1's text itself names
  `bash corpus/claim-ledger.sh verify`** (see §3 / F2), so the one row most likely
  to be drafted from the item text is the one the contract says must be refused.
  Mitigating: `claim-ledger.sh` independently refuses a nested `verify`
  (`CLAIM_LEDGER_DEPTH` guard, `corpus/claim-ledger.sh:199-200`, exit 2), so the
  failure is a loud `ITEM-FAIL` rather than unbounded recursion — but it surfaces as
  an item defect, not a load-time `POLICY`.
- **`--tsv` override exists** (`:70`) alongside `--list`/`--only`/`--selftest`
  (`:67-69`), i.e. the gate is testable on a scratch tree; selftest fixture is
  "6 items, 4 runnable, 2 by-hand → floor = ceil(6/2) = 3" (`:318`, `:343`).
- **No ledger wiring yet**: `grep -c checklist corpus/claim-ledger.tsv` → `0`.
  `SCORECARD.md:209` names "the checklist item count" as the round-15 falsifiable
  target, so a row pinning `CHECKLIST_RUN: CLEAN (items=16 …)` is the expected
  close-out — see F1.

## 7. Attack on the shipped 9/7 split (gate verified live)

Run: `bash corpus/checklist-run.sh` → `CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7`
+ `CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7 failed=0)`, exit 0, 2.35 s (executed).
Runnable = E1 E4 E5 E8 H1 H3 H4 H7 H8; by-hand = E2 E3 E6 E7 H2 H5 H6.

Verdict: **the 9/7 split is defensible on the shipped criterion** ("is there a
command whose verdict is a defect signal for this item"), and **no by-hand row is
misclassified** — but six concrete attacks survive, two of them load-bearing.

### A1 — H7 fails on a state the corpus itself declares legitimate  (real defect risk)

```
bash corpus/transcript-scan.sh --db /nonexistent/none.db
# -> transcript-scan: db not found: /nonexistent/none.db
# -> exit 2
```

Row H7 declares `expect_exit 0|1`; `2` is outside the set ⇒ **ITEM-FAIL**. But the
missing-db state is exactly the purge the checklist's own item 14 prescribes
(`stop + rm -rf xdg-data`), and `corpus/surface-census.tsv:45-47` classifies
`opencode.db` / `-shm` / `-wal` as **`runtime`** — "may legitimately be absent
(ABSENT, informational)". E1 (surface-census + drift-pins) stays CLEAN in that
state because runtime-ABSENT is non-failing (`surface-census.sh:340-350`,
N_ABSENT + `continue`; [INFERENCE] for the E1 half, executed for the exit-2 half).
So one legitimate operator action makes E1 pass and H7 fail. H7's own note only
covers "re-pin after reading the HIT lines" — there is no re-pin path for
*no database*. Fix: `expect_exit 0|1|2` with an alternative last-line, or make
`transcript-scan.sh` print the HITS verdict with `schema-absent=1` + exit 1 on a
missing db (the ERE already reserves `schema-absent=[0-9]+`).

### A2 — E4's allowlist does all the work and prints no exclusion count  (silent-pass vector)

```
# as written (allowlist active):
grep -RInE --exclude-dir=.git --include='*.md' --include='*.tsv' --include='*.sh' \
  'op://[A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]+' . | grep -vE 'op://(FakeVault|wal|vault)/' | wc -l
# -> 0
# same without the -v (allowlist removed): -> 5
```

All five exclusions are placeholders, enumerated by path only (vault segment in
brackets): `corpus/knowledge/op-env-refs.md:14` [vault],
`corpus/lessons/round-5-aggregator-audit.md:19` [vault],
`corpus/transcript-scan.sh:202` [vault], `corpus/transcript-scan.sh:242` [wal]
(the round-6 audit's known residual, §5 F4), `corpus/surface-census.sh:608`
[FakeVault]. Also checked: `git ls-files | grep -vcE '\.(md|tsv|sh)$'` → `0`, so
the `--include` set is the whole tracked tree (no extension blind spot today).
The attack: the row prints only `hits=`, so a *real* ref path under a vault
literally named `vault`/`wal` (or a new fixture reusing those names) yields
`hits=0` with **no signal**. Fix: print `excluded=N`, assert `N=5`, re-pin only
after reading — the same teeth H7 applies with `HITS=2`.

### A3 — E8/H3/H8 demand facts no revision-pinned artifact declares  (structural, cheap fix)

E8's exact expression, probed on fixtures (semantics only; the row's path is
hardcoded, so the expression was lifted verbatim):

```
base  (boundaries has both keys False + access_receipt/receipt_sha256) -> HANDOFF_STATUS: OK      exit 0
nokey (boundaries lacks target_authority_conferred)                    -> HANDOFF_STATUS: DEFECT  exit 1
noreceipt (no access_receipt/receipt_sha256)                           -> HANDOFF_STATUS: DEFECT  exit 1
```

So an absent nested key is a defect, not a skip. Yet `target_authority_conferred`
appears in **zero** pinned artifacts, and `autoupdate` (H3) appears in zero gate
*data* files (`grep -c … corpus/*.sh corpus/*.tsv` → empty for both; §5 F5). The
requirement therefore lives only in the row's own Python. Fix: one
`drift-symbols.tsv` row each for `handoff-status.json #1 target_authority_conferred`
and `opencode.json "autoupdate"` — that moves the demand into the same pinned
declaration layer that already carries item 8's `credentials_in_evidence` and
item 11's other two knobs. (H8's two symbols, `40961` +
`OPENCODE_SERVER_PASSWORD`, are genuinely asserted only by H8; same argument but
they are containment premises, so the row is the right home.)

### A4 — the criterion's ambiguity, quantified

Three readings of the same 16 items: CheckPlanner **3** runnable; this census's
independent "FULL" judgement (a gate verdict *is* the item's claim) **4-5**
(E1, E5, H4, H7, ±H3); shipped **9**. The 9 is honest **only because** each
runnable `note` names the duty it leaves to the operator — verified in the shipped
file: E1 leaves the `claim-ledger.sh verify` + `stamp` leg, E4 leaves "which
exclusions are legitimate", H1 leaves "queue instead of race", H3 leaves the
post-merge/global-config claim, H8 leaves the behavioural rule. So the `note`
column is load-bearing, not decoration, and that property is **not
gate-enforceable** — it should be a review checklist item per runnable row
(`--list` exists; nothing asserts notes are non-empty or duty-naming).

### A5 — the by-hand set: all 7 justified, two for a *hard* reason

Classes read from the file: E2 `manual-change`, E3/E6/E7/H6 `authoring-duty`,
H2 `runtime-behavior`, H5 `cross-lane` — all from the closed set
(`checklist-run.sh:65`), all reasons ≥24 chars. H2 and H6/E6 are by-hand because
the contract **forbids** the only mechanisation (H2 needs `the-janitor stop` + a
live next request, and `DENY_CHECK` refuses start/stop/`the-janitor run`; H6/E6
would have to read the request text, which is the material the item forbids
persisting). That is a stronger justification than "difficulty" and should be
stated as such. E2/E3/E7 residuals are genuinely authoring calls. **No
misclassification found**; H5's by-hand reason is correctly scoped to the lease,
since the manifest half is already pinned by `surface-census.tsv` +
`drift-baseline.tsv`.

### A6 — E1 can pin the item's own numbers for free

E1's `expect_last` is `^DRIFT_PINS: CLEAN \(files=[0-9]+ symbols=[0-9]+\)$` while
item 1's text states "(15 files / 20 pins as of round 12)" and the data holds
exactly 15 (`grep -c '^\$HOME' corpus/drift-baseline.tsv`) / 20
(`corpus/drift-symbols.tsv`). Pinning `files=15 symbols=20` makes the item's own
counts a verdict at zero cost. [INFERENCE] strictly stronger; today a same-count
substitution would pass.

### Resolved since my §6 cross-check

- `DENY_CHECK` (`checklist-run.sh:66`) now reads
  `op\.env|op run|op read|op inject|the-janitor start|the-janitor stop|the-janitor run|claim-ledger\.sh`
  — my F2 recursion gap is closed.
- The 8-column shape is documented in `corpus/checklist.tsv`'s own header, so the
  6-column phrasing of the brief (not the implementation) was the stale side;
  my §6 drift note is resolved in the implementation's favour.

## 8. Unknowns

- **item-count semantics**: `grep -c '^- \[ \]'` (all checkbox bullets in the file)
  vs section-scoped awk. At `e64e81b` both yield 14; at the working tree the
  file-wide grep also yields 16 (no other `- [ ]` list exists). A future
  `checklist.tsv` should pin the *section-scoped* count so a stray checkbox added
  elsewhere cannot inflate `items=`. [INFERENCE]
- **round-11/12 checklist text**: I censused `ea77bf0`, `e64e81b`, `4b8c018`,
  `2486643` and the working tree. The per-commit trajectory in §1 covers every
  `SKILL.md`-touching commit, so item *counts* are exact for all revisions; item
  *line numbers* are only reported for r13 and the working tree (= the two the
  assignment names).