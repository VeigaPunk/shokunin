# audit-tabi — tabi-shokunin lane audit (aggregator round 12)

Seat: `KaikaAggregateR12.AuditTabi`. Audit time: 2026-10-19.
Lane under audit: `/home/vgpnk/Projects/shokunin/tabi-shokunin` (physical lane repo, read-only).
Gate under audit: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/.ufo/waves/round-9/corpus-gate.mjs`
(sha256 `e7d49942017a8c522e2b16f3de78e60d16a23ffad6838396a8c44897c12299c3`, gate id `corpus-gate-v1`).
No lane file was written, staged, or committed.

## 1. Revision and cleanliness

```
$ git -C /home/vgpnk/Projects/shokunin/tabi-shokunin rev-parse HEAD
9bc89bfe78b1c455501b2c7a0d9bd061ea539c21
exit 0

$ git -C /home/vgpnk/Projects/shokunin/tabi-shokunin status --porcelain
(no output)
exit 0
$ git -C /home/vgpnk/Projects/shokunin/tabi-shokunin status --porcelain | wc -l
0
```

All observations below are bound to **HEAD `9bc89bfe78b1c455501b2c7a0d9bd061ea539c21`**, clean tree.
The gate run itself reports `dirty=0 mode=snapshot` and extracts committed bytes only
(`git archive 9bc89bfe78b1c455501b2c7a0d9bd061ea539c21 | tar -x -C <tmp>`, per the gate's own note line).

## 2. Round selector, stated explicitly

The gate's registry default is `--round 9` ("the round whose aggregator lesson r10 requires").
The lane's committed LOG's newest round is **“kaika fleet round-1”** (`LOG.md:462` heading;
claims at `:477`; post-review fixes at `:508`), after training rounds 0–11. There is no
unambiguous numeric mapping from that fleet-round name to the gate's `--round N` for this lane,
so I ran both selectors and report both, explicitly:

- **primary:** `--round 9` (the gate default),
- **sensitivity:** `--round 1` (the lane's newest committed round name).

The two runs differ **only** in the r10 finding text; every other finding id and line is
byte-identical (`diff` of the non-r10 findings: no output). Both exits are 1.

## 3. Gate result at HEAD — NOT CONFORMANT

### Command and exit

```
$ cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
$ node .ufo/waves/round-9/corpus-gate.mjs \
    --snapshot /home/vgpnk/Projects/shokunin/tabi-shokunin \
    9bc89bfe78b1c455501b2c7a0d9bd061ea539c21 --round 9
exit 1
```

Full stdout captured at `/tmp/audit-tabi-gate-r9.txt`
(sha256 `7ce081bd5ce930e733696f2c94119e10348323c982063c9e4d6724cd8a79431a`); stderr empty.

Selected gate output lines (verbatim):

```
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=9
# expect tabi-shokunin@9bc89bf ABSENT (no committed expected verdict for this revision)
# tree tabi-shokunin revision=9bc89bfe78b1c455501b2c7a0d9bd061ea539c21 dirty=0 mode=snapshot
...
# verdict tabi-shokunin failed findings=158 rules=r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
```

**Verdict: not conformant at `9bc89bf` by gate exit 1.** Failed rules and exact finding ids:

| rule | count | ids | first/last |
|---|---|---|---|
| r4 (count claim without backticked command, CORPUS.md:28) | 155 | `CR-tabi-shokunin-r4-1` … `CR-tabi-shokunin-r4-155` | `README.md:5` … `lessons/training-round-11.md:20` |
| r8 (credential material, literal text, CORPUS.md:43) | 2 | `CR-tabi-shokunin-r8-1`, `CR-tabi-shokunin-r8-2` | see below |
| r10 (round’s aggregator lesson absent, CORPUS.md:21) | 1 | `CR-tabi-shokunin-r10-1` | see below |

Clean rules in this same run: **r2, r7, shonen — 0 findings each**
(`grep -c '^CR-tabi-shokunin-\(r2\|r7\|shonen\)-'` → 0).

### Exact r8 finding text (both)

```
CR-tabi-shokunin-r8-1: credential-class cookie occurrences=3 lines=3 files=2 owner=lane at 9bc89bf literal_shaped=0/3 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[evidence/w9-tabi-b91/compare.mjs,knowledge/stateful-fixture-evidence.md] first=evidence/w9-tabi-b91/compare.mjs:25 first4="Set-" len=21 (CORPUS.md:43)
CR-tabi-shokunin-r8-2: credential-class kv-secret occurrences=19 lines=19 files=8 owner=lane at 9bc89bf literal_shaped=0/19 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[evidence/w10-aud-b10-work/fence-nonl.txt,evidence/w10-aud-b10-work/fence.txt,evidence/w9-tabi-b91/curl-control.sh,evidence/w9-tabi-b91/curl-replay.sh,evidence/w9-tabi-b91/journey.mjs,evidence/w9-tabi-b91/server.py,+2 more] first=evidence/w10-aud-b10-work/fence-nonl.txt:178 first4="toke" len=28 (CORPUS.md:43)
```

The gate’s complete r8 file lists (from its `# note` lines):

```
cookie/lane:    evidence/w9-tabi-b91/compare.mjs knowledge/stateful-fixture-evidence.md
kv-secret/lane: evidence/w10-aud-b10-work/fence-nonl.txt evidence/w10-aud-b10-work/fence.txt
                evidence/w9-tabi-b91/curl-control.sh evidence/w9-tabi-b91/curl-replay.sh
                evidence/w9-tabi-b91/journey.mjs evidence/w9-tabi-b91/server.py
                knowledge/state-changing-matrix-r9.md knowledge/stateful-fixture-evidence.md
```

Reviewer observation on the hit shapes (exact bytes read; **classification stays not-evaluated** —
I am not claiming these are or are not real credentials):
- `evidence/w9-tabi-b91/compare.mjs:25` — `/^Set-Cookie: /.test(l)` (a regex literal in the compare script).
- `knowledge/stateful-fixture-evidence.md:59` — `Set-Cookie: tabi_sid=<16 lower-hex>;` (placeholder shape in the fixture description); `:446` `Set-Cookie: … (mint)`.
- `evidence/w10-aud-b10-work/fence-nonl.txt:178` — `token = secrets.token_hex(8)` (a Python assignment inside an archived fixture fence); `evidence/w9-tabi-b91/server.py:178` same line.
- The remaining kv-secret hits are `token=<T>` URL-encoded form bodies and `document.getElementById('token')` expressions
  (`curl-control.sh:23,27,29`, `curl-replay.sh:27,30,32`, `journey.mjs:344,353,364,365,380,392,415,436,443,457,460`,
  `knowledge/state-changing-matrix-r9.md:203`).
- The gate’s own shape measure agrees with this reading: `literal_shaped=0/3` and `0/19` — the value part of every
  match is non-literal-shaped (grammar/expression text, not an opaque token). That is a syntax fact only; CORPUS.md:43
  still counts the literal text, so the findings stand as failed. Who owns the byte-level decision is the parent’s call.

### Exact r10 finding text (primary run)

```
CR-tabi-shokunin-r10-1: no corpus/lessons/round-9-aggregator-*.md — the round-9 review duty has no emitted lesson (CORPUS.md:21)
```

Sensitivity run `--round 1` (exit 1, same 158 findings, same rules r4,r8,r10):

```
CR-tabi-shokunin-r10-1: no corpus/lessons/round-1-aggregator-*.md — the round-1 review duty has no emitted lesson (CORPUS.md:21)
# verdict tabi-shokunin failed findings=158 rules=r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
```

(Output sha256 `b1ac00fa526154614553bb835c094603b95e396814256eb6a56372206b396663`.)

**r10 is a genuine structural absence at this HEAD, not a selector accident.** `git ls-tree` of
`corpus/lessons/` at `9bc89bf` lists 29 files and **none** matches `round-<N>-aggregator-*.md` for any N.
The nearest files are `round-9.md` (the lane's own round-9 lesson) and `kaika-fleet-round-1.md`
(lane-authored). For comparison, six legacy lanes carry `round-9-aggregator-corpus-verdict.md`
(kagi, kake, kasegi, kengaku, kotoba, kumitate); tabi is not among them.

### r4 shape (spot-checked, not re-read line by line)

155 findings on the canonical surfaces (`README.md`, `knowledge/**.md`, `lessons/**.md`). Per-file
counts at the top of the distribution (from the finding ids, full list in the captured output):
`lessons/round-8.md` 10, `lessons/round-9.md` 9, `knowledge/hygiene-sweep-r4.md` 9,
`knowledge/archive-receipt-r10.md` 9, `knowledge/archive-receipt-r5.md` 8, `lessons/round-4.md` 7,
`knowledge/multi-step-journey.md` 7; `README.md` 3 (`:5`, `:66`, `:158`).
I opened three flagged lines and confirmed they are real `<n> <count-noun>` claims on lines with no
backticked command (e.g. `README.md:5` "Held at round 3 (2026-10-14): 8 knowledge notes, 1944 lines";
`knowledge/async-step-evidence.md:200-203` table rows with `10 lines`). I did **not** audit all 155;
the rule is a form rule and a finding is not a truth verdict.

## 4. SOURCES structural observations (PROVISIONAL — census parser fix in progress elsewhere)

The parent’s direction stands: a parser fix for indented Markdown source rows is in progress, so
**no final census total is frozen here**. What follows are read-only observations at `9bc89bf`, from
`corpus/SOURCES.md` (blob `89a69384adeff8ccda3b41e4938abc40425492b9`, 17,820 B).

Commands and outputs:

```
$ grep -c '^| S[0-9]\{3\} |' corpus/SOURCES.md
28
$ grep -o '^| S[0-9]\{3\} ' corpus/SOURCES.md | sort | uniq -d
(no output — no duplicate ids)
$ awk -F'|' '/^\| S[0-9]{3} \|/ {gsub(/ /,"",$5); print $5}' corpus/SOURCES.md | sort | uniq -c
     22 A
      4 B
      2 C
$ grep -o '^| S[0-9]\{3\} |[^|]*|[^|]*|[^|]*|[^|]*|[^|]*|[^|]*| [a-z]* |' corpus/SOURCES.md \
    | awk -F'|' '{print $9}' | sort | uniq -c
     20 mined
      6 queued
      2 rejected
$ grep -n '^## ' corpus/SOURCES.md
11:## Registry
44:## Paths
51:## Search log
59:## Leads (unopened)
$ grep -c '^[[:space:]]\+| ' corpus/SOURCES.md
0
```

- Row set: `S001`–`S028`, contiguous, unique. 28 rows = 20 mined + 6 queued + 2 rejected; tiers A22/B4/C2.
- **Zero leading-indented table rows in this file** (`^[[:space:]]+| ` = 0), so the in-flight indented-row
  parser fix does not change *this file’s* row set — the totals above are still labelled provisional per
  parent direction, and I did **not** run `node scripts/check-sources.mjs` (committed tree, but a test-run;
  no builds/tests in this seat, and its output would be the thing under repair).
- `used-by` column resolution at HEAD: 20 rows carry a `used-by` path; all 20 resolve with
  `git cat-file -e 9bc89bf:<path>` (S001–S019, S028). The 8 queued/rejected rows (S020–S027) carry `—`.
- Consistency note (not a defect claim): the round lesson’s Gate says "all 27 rows are new"
  (`corpus/lessons/kaika-fleet-round-1.md:76`) and `LOG.md:489-491` states "27 opened rows (A21 B4 C2;
  19 mined, 6 queued, 2 rejected)". Both are the pre-post-review figure; the post-review added **S028**
  (`supersedes S004 —`, `corpus/lessons/kaika-fleet-round-1.md:99`), giving the HEAD values above
  (28 / A22 B4 C2 / 20 mined). Any parent ledger quoting "27" from those records would be quoting the
  pre-fix state.
- Structure present: Registry, Paths, Search log, Leads (unopened) — the four sections the lane’s own
  `check-sources.mjs` requires (`requiredSections`, `scripts/check-sources.mjs:31`). Three leads are
  listed as unopened and were **not** used as evidence in this note.

## 5. One directly evidenced study path (from `corpus/SOURCES.md` §Paths)

Verbatim (`SOURCES.md` §Paths, heading at `:44`):

> `profile-isolation` — S002 → S001 → S004 → S003: the support posture first (CDP is unsupported and
> unversioned), then the published ≥136 rule, then the code that shows it is branding-gated, then the
> testing build that sidesteps it. Ends at `knowledge/chrome-remote-debugging-profile-boundary.md`.

Evidence that the sequence is real at HEAD (not a lead):
- All four rows are present in `## Registry` with `status=mined` and
  `used-by corpus/knowledge/chrome-remote-debugging-profile-boundary.md` (verified in the 20-row
  resolved set above).
- The terminal note exists at HEAD: `corpus/knowledge/chrome-remote-debugging-profile-boundary.md`,
  blob `9ecc5d6d524c3e9d6bd8ba7b001d1a6f5eb29565`, 8,817 B.
- The note’s own frontmatter cites the same four rows: `source:` line names S001–S004
  (`corpus/knowledge/chrome-remote-debugging-profile-boundary.md:5`), and `grep -o 'S0[0-9][0-9]'`
  over the file yields exactly `S001 S002 S003 S004`.
- Reading caveat carried by the corpus itself: **S028** re-fetched the same Chromium source as S004 and
  supersedes its `teaches` — the "host Chromium does not enforce it" wording is a source-level
  **inference**, never observed (`SOURCES.md` S028 row; README correction at `:199`). A reader following
  `profile-isolation` should read S028 after S004.

The other two mined paths (`protocol-choice` S002→S005→S006→S012→S011→S008→S009;
`flake-receipts` S013→S014→S017→S015→S016→S018→S019) are structurally identical (all rows mined,
terminal notes present at HEAD). The fourth path, `accessible-selectors` (S025→S023→S024), is marked
**queued, not mined** and is therefore a lead, not evidence.

## 6. Provenance frontmatter scan (parent follow-up) — `recheck:` values

Bounded scan of `corpus/knowledge/*.md`:

```
$ grep -l -E '^\s*(source|verified-at|recheck)\s*:' corpus/knowledge/*.md | wc -l
5
```

Only 5 of the 29 knowledge notes carry that frontmatter: the three kaika-round-1 admits
(`chrome-remote-debugging-profile-boundary.md`, `webdriver-bidi-capability-matrix.md`,
`web-flake-retry-evidence.md`) and two older synthesis notes (`arc-synthesis.md`, `closeout-r11.md`).
The other 24 notes carry none (absence observation; not a gate rule and not a conformance verdict).

Exact `recheck:` values, all five:

- `arc-synthesis.md:7` — `recheck: re-derive §0's counts with the commands shown, re-run §6's manifest spot (sha256sum -c MANIFEST.txt), and re-read the §1/§2/§4 anchors against the cited notes; this note is written to be re-readable by a cold reader without its author.`
- `closeout-r11.md:7` — `recheck: re-run §5's commands (manifest spot sha256sum -c MANIFEST.txt × 3 groups; the L0 read; the daemon read; the census commands); re-read §1–§3's anchors against the cited notes; the note is written for a cold reader without its author.`
- `chrome-remote-debugging-profile-boundary.md:7` — `recheck: on each chromium major bump — chromium --version, then re-fetch remote_debugging_server.cc@main and diff the IsRemoteDebuggingAllowed block; 90d for the protocol-viewer page (living document, no version anchor)`
- `web-flake-retry-evidence.md:6` — `recheck: on each Playwright release, compare the stable docs for retries, traces, actionability, assertions, and the shuffle flag; 180d for the 2025 paper records, preserving the DOI/PDF identity`
- `webdriver-bidi-capability-matrix.md:7` — `recheck: 90d or on W3C republication — re-fetch https://www.w3.org/TR/webdriver-bidi/, record the dated WD URL and source revision; re-audit the cited command/type/event anchors in §§7.1–7.10; refresh MDN, Selenium, and chromium-bidi README revisions; do not promote a WPT app shell to support evidence without reading its result data`

**Finding: none of the five `recheck:` values points into `/tmp` or `.tower/worktrees`** (or any
filesystem path at all — they are re-derivation instructions and time-based cadences). Verified by
scanning lines 1–15 of every `corpus/knowledge/*.md` for `/tmp/|\.tower/worktrees|worktree`:
the only hits are listed below.

Adjacent fidelity observations (not `recheck:` values; recorded because they bear on the same concern):
- `corpus/knowledge/webdriver-bidi-capability-matrix.md:1` (provenance comment): "Local anchors were
  spot-checked in **this worktree**." — no worktree path or revision is named, so that spot-check is
  not re-derivable from the committed tree alone. Exact text unbound; parent should treat it as an
  unverified provenance claim, not as a resolvable pointer.
- `corpus/knowledge/browser-surface-census.md:164` — `~/.tower/comms/missions/M5-burnerchrome-cdp-host-launcher.md`
  (a `~/.tower` pointer in body text, not `.tower/worktrees`; also mirrored in two archived evidence copies).
- Body-level `/tmp` scratch references are pervasive and mostly self-labelled as volatile, e.g.
  `webbridge-daemon-disposition.md:10` "Scratch namespace: `/tmp/tabi-r2-2-*` (6 files, 173 lines;
  sha256s in §8)"; `webbridge-revival-assessment.md:6` "Scratch: `/tmp/w6-tabi-b62/` (volatile; pins §8)";
  and `corpus/README.md`’s `stateful-fixture-evidence.md` row says `/tmp/w8-tabi-b81` "remains
  unarchived (`closeout-r11.md` O2), so these pins stay provisional." These are body/provenance text,
  not frontmatter `recheck:` values — reported as observation only, no verdict.

## 7. Gate limitations (named, not waived)

1. **Not evaluated by the gate (declared):** r1 (is a token a source), r3 (falsifiable-or-opinion),
   r5 (negative claim carries its sweep), r6 (quote names its location), r9 (append-only/history),
   box-3 verifier independence, and SHONEN box **truth**. The clean r2/r7/shonen result is a form result.
2. **r8 classification is `could-not-evaluate`** (needs an operator-gated vault read). The two r8 findings
   stand as literal-text findings; the schematic-vs-real question is not decided by anyone here.
3. **No frozen expectation for this revision** — the gate printed
   `# expect tabi-shokunin@9bc89bf ABSENT (no committed expected verdict for this revision)`, so exit 3
   (drift) was impossible for tabi; the exit is a fresh evaluation, not a pinned one.
4. **Snapshot mode carries no history** (`git archive`), so the r9 mechanical sub-check could not run even
   if implemented; `dirty=0` means the graded bytes equal the committed bytes, but no mode/symlink
   metadata beyond tar defaults is graded.
5. **r4 is a lexical heuristic** (count-noun line without a backtick). 155 findings describe line form, not
   155 false claims; conversely, a line with any backtick is skipped even if it carries no command.
6. **r10 is presence-only** and selector-dependent; here both selectors (9 and 1) fire, so the r10 failure
   is selector-independent at this HEAD.
7. **r7 under-coverage is a note, not a finding:** `2615/2648 corpus files carry no index row`; 5 backticked
   path templates were skipped. The index rule is phantom-row-only by design.
8. **SOURCES.md is outside the gate’s canonical surfaces.** corpus-gate-v1 does not grade the SOURCES
   registry, tier/status semantics, or study paths; my §4 observations are read-only structure checks,
   not gate output.
9. Adjacent, **not verified by me**: the lane’s `LOG.md:508-525` records that `SHONEN.md` was regenerated
   with all four `[~]` boxes and that its own `ROUND_CONTRACT` reads `history_rewritten` from that commit
   as an operator-ordered change. I did not run the lane’s contract gates; this is a quoted lane record.

## 8. What I did not do

- Did not open every r4-flagged line (3 opened); did not adjudicate any r4/r8 item’s truth.
- Did not run `scripts/check-sources.mjs`, `check-freshness.mjs`, `check-round-contract.mjs`, or
  `check-user-round-contract.mjs` (no builds/tests in this seat; census parser in flight).
- Did not treat any `## Leads (unopened)` item or the queued `accessible-selectors` path as evidence.
- Did not freeze any census total; §4 values are provisional pending the parent’s parser fix and the
  `FINAL LANES READY` signal.
