# ChainHopFixture

Advisory measurement. Not a judge verdict. Not a landed gate.

Seat: mutation-tester. Fixture root: `/tmp/chousa-chainhop-fixture` (temp, disposable). Lane files were not modified. No external fetch.

## Headline

A three-hop chain with hop 3 an unmarked dead link fires the chain-clause probe. The same three hops, all present, do not.

| arm | what hop 3 is | probe | exit | fires? |
|---|---|---|---|---|
| `intact/` | file exists | `CHAIN_HOP: CLEAN (walked=3 resolved=3 marked=0 unresolved=0)` | 0 | no |
| `broken-dead/` | `corpus/hop3-primary.md` absent, unmarked | `CHAIN_HOP: DRIFT … finding=CHAIN_HOP_UNRESOLVED` reason `dead-link` | 1 | yes |
| scratch pristine (copy of intact) | file exists | CLEAN, same line | 0 | no |
| scratch mutated (one byte in the hop-3 pointer) | pointer names a missing file | DRIFT, `dead-link` | 1 | yes — **killed** |
| scratch restored | bytes match pristine | CLEAN | 0 | no |

`tools/research-gate.sh` was absent at sweep time, so the named gate did not fire. The probe below is the chain clause only (`resolved or marked unresolved` / dead link). It is not that script and does not print `RESEARCH_GATE:`.

## Rule used

Admitted from the lane skill, not from the exports:

- `chousa-shokunin/SKILL.md:19` — follow each hop to the cited artifact; do not stop at a summary of the citation; each hop resolved or marked unresolved.
- `chousa-shokunin/SKILL.md:29` — a chain that ends at a dead link is broken; record the hop and stop.
- `chousa-shokunin/SKILL.md:50-53` — the named checker is `tools/research-gate.sh`; chain hops must be resolved-or-marked; `verify` prints `RESEARCH_GATE: CLEAN|DRIFT` and exits 0/1.

The exports do not contain the word "chain". Their citation chrome is the shape this fixture encodes, not the rule text. `research/README.md:3-8` says the three files are browse-enabled GPT-6-Astra chat exports, not a Deep Research pipeline. Their own citations are unverified. This probe did not fetch them and does not treat a site name as a resolved hop.

## Named gate: absent

Sweep, this run, exit 0, no paths printed:

```text
find /home/vgpnk/Projects/shokunin -name 'research-gate.sh' -not -path '*/.git/*'
```

`chousa-shokunin/tools` was absent (`tools_dir=absent`). Unknown whether a sibling lands the script after this sweep. This report does not wait on that and does not claim the absence is permanent.

Finding id `CHAIN_HOP_UNRESOLVED` is the example string in this wave's FindingIds prompt. It is a fixture label, not a landed vocabulary.

## Probe bounds

`/tmp/chousa-chainhop-fixture/chain-walk.sh` sha256 `d4427ffd040ad9215471994febfc326bfda70bc61c750ac5d8d99acea80d1b8e` (2964 bytes). Same sha before and after the mutation probe.

Walks exactly three hops. Each artifact has one `cites:` line. The next hop is the first field of that line.

| class | condition | result |
|---|---|---|
| RESOLVED | token is `corpus/…`, no `..`, not absolute, `-f` under the arm root | hop counts resolved |
| MARKED | the cites line contains `unresolved` (any case) | stop, do not fire |
| dead-link | `corpus/…` and the file is absent | fire, stop |
| summary-not-artifact | token is neither `corpus/…` nor `http(s)://` | fire, stop |
| external-fetch-refused | token starts with `http://` or `https://` | fire, stop, do not open the URL |
| outside-root | token contains `..` or is absolute | fire, stop, before `-f` |

Fixture choices, not extra skill sentences: the marker spelling `unresolved` (the skill says "marked unresolved" and does not name a token); rejecting `..` before `-f` (hermetic bound; kasegi's separate class is `OUTSIDE-BASE` at `kasegi-shokunin/corpus/instruments/anchorcheck.py:15`); fixed length 3 (the assignment, not a general length rule).

Not checked, and not claimed: line-in-range / PAST-EOF (`anchorcheck.py:14`, `:53-56` keeps that separate from semantic support); whether the terminal file's text supports the claim; symlinks (`-f` would follow one; no symlink arm was run); a marker sitting on the previous line (not run).

`grep -nE 'curl|wget|ssh|nc |ncat|fetch|python|node|http.client'` on the probe matched only the comment "Does not fetch" and the reason string `external-fetch-refused`. No network command.

`strace -f -e trace=network` on the URL arm (`/usr/bin/strace`, output `/tmp/chousa-chainhop-fixture/strace-url.txt`, 348 bytes, 5 lines) recorded no `socket` / `connect` / `sendto`. Lines were two `SIGCHLD` records and three `exited` records; the traced process exited 1. Origin of the two exit-0 child pids was not identified. Observation stops at "no network syscall in that trace."

## What the three hops are

Modeled on the export stop, not copied from instruction-shaped export text. The only export token placed in a fixture file is `コトバンク`.

Observed stops (citation chrome, not a machine-readable chain — the exports have no `cites:` field; that field is the fixture encoding):

- `research/deep-research-2026-09-28/A-shokunin-tradition.md:67-69` — dictionary claim, then the line `コトバンク`, then `+3`. sha256 `9033857d4625555c7b778dfad6df80e3e1b24ed8bffa3fee2fd445b9c5540b85`, 109 lines.
- `research/deep-research-2026-09-28/B-multiagent-knowledge.md:71-72` — `Sources:` titles, then the line `arxiv.org`. sha256 `6d8dbddd3e2d2f47dcb153c5a3347cc6321db4afc72cf07da40f0f7fe5022006`, 100 lines.
- `research/deep-research-2026-09-28/C-rank-taxonomy.md:81-83` — dictionary claim, then `コトバンク`, then `+5`. sha256 `e48fe70ff92055c217ac6ca6ce68e403aa5689fee8717f3bd0ccf5badc92321b`, 154 lines.

`arxiv.org` is the same class as `コトバンク` (a bare name, not a path). The summary arm uses `コトバンク` only.

Hermetic chain, each arm its own root so `--root` cannot see a sibling arm:

1. `corpus/record.md` cites `corpus/hop1-secondary.md` (secondary restatement).
2. that file cites `corpus/hop2-aggregator.md` (aggregator page).
3. that file cites the primary — present, absent, a summary token, a URL, or marked unresolved.

`broken-dead/corpus/hop3-primary.md` was absent (`hop3_absent=yes`).

## Measured probe runs

Command form: `bash /tmp/chousa-chainhop-fixture/chain-walk.sh <arm>/corpus/record.md`

Intact:

```text
hop 1 RESOLVED corpus/hop1-secondary.md
hop 2 RESOLVED corpus/hop2-aggregator.md
hop 3 RESOLVED corpus/hop3-primary.md
CHAIN_HOP: CLEAN (walked=3 resolved=3 marked=0 unresolved=0)
exit=0
```

Broken, hop 3 dead, unmarked (`SKILL.md:29`):

```text
hop 1 RESOLVED corpus/hop1-secondary.md
hop 2 RESOLVED corpus/hop2-aggregator.md
hop 3 CHAIN_HOP_UNRESOLVED corpus/hop3-primary.md dead-link
CHAIN_HOP: DRIFT (walked=3 resolved=2 marked=0 unresolved=1 finding=CHAIN_HOP_UNRESOLVED)
exit=1
```

Hops 1 and 2 still resolve. The fire is the broken hop, not a missing start file.

Summary stop (`SKILL.md:19` never-column; export shape):

```text
hop 3 CHAIN_HOP_UNRESOLVED コトバンク summary-not-artifact
CHAIN_HOP: DRIFT (walked=3 resolved=2 marked=0 unresolved=1 finding=CHAIN_HOP_UNRESOLVED)
exit=1
```

Marked unresolved (same missing primary, word `unresolved` on the cites line). The clause is resolved-**or-marked**. This arm must not fire:

```text
hop 3 MARKED corpus/hop3-primary.md
CHAIN_HOP: CLEAN (walked=3 resolved=2 marked=1 unresolved=0)
exit=0
```

`walked=3 resolved=2` is not an intact chain. The hop is marked, not resolved.

External URL, not fetched (`https://example.invalid/daijisen`):

```text
hop 3 CHAIN_HOP_UNRESOLVED https://example.invalid/daijisen external-fetch-refused
CHAIN_HOP: DRIFT (walked=3 resolved=2 marked=0 unresolved=1 finding=CHAIN_HOP_UNRESOLVED)
exit=1
```

`..` hop (`corpus/../not-in-root.md`), classified before `-f`:

```text
hop 3 CHAIN_HOP_UNRESOLVED corpus/../not-in-root.md outside-root
CHAIN_HOP: DRIFT (walked=3 resolved=2 marked=0 unresolved=1 finding=CHAIN_HOP_UNRESOLVED)
exit=1
```

Usage, so exit 2 is not confused with a fire: no args → `chain-walk: usage: chain-walk.sh <corpus/record.md>` exit 2. Two `cites:` lines → `ambiguous cites lines (2)` exit 2.

## Mutation probe

Claimed invariant under test: an unmarked dead hop in a three-hop chain is detected; the intact chain is not.

Scratch: `cp -a intact scratch`. Isolated. No sibling source touched.

Pristine hop-2 sha256 `1db9b7f67c39950bb41d7ccfc52bfc5855810a40bbaa6d276cf3abc68aa96077`. Tree:

```text
70d8a476d255c011dc09da8628c1aaf87d35465c87202b4598241380d60ce21a  ./corpus/hop1-secondary.md
1db9b7f67c39950bb41d7ccfc52bfc5855810a40bbaa6d276cf3abc68aa96077  ./corpus/hop2-aggregator.md
53ef773ef4491a6b231a42f71e0edb2c1d45b3f9e7240e81576ba6506105b61c  ./corpus/hop3-primary.md
80e1698fba01510895c57298cb1ab68d1cd9e3ee1a8e2d17f8b39e2fcf8b0925  ./corpus/record.md
```

Pristine detector: CLEAN, exit 0. Baseline did not fail, so the later fire is not inconclusive.

Mutant: one byte in `scratch/corpus/hop2-aggregator.md`, the hop-3 pointer only. `cmp -l` against the saved pristine bytes: `75 171 170` (1-based offset 75, octal 171 `y` → octal 170 `x`). `corpus/hop3-primary.md` → `corpus/hop3-primarx.md`. File length unchanged (79 bytes). The target file was left in place; the pointer moved. Mutated sha256 `8e48b02b045a2bd6e952c0dc3940291dbcf2b7a34fb1f8299e2c25c79b707fae`.

Expected detector: exit 1, hop 3 `CHAIN_HOP_UNRESOLVED`, reason `dead-link`.

Actual:

```text
hop 1 RESOLVED corpus/hop1-secondary.md
hop 2 RESOLVED corpus/hop2-aggregator.md
hop 3 CHAIN_HOP_UNRESOLVED corpus/hop3-primarx.md dead-link
CHAIN_HOP: DRIFT (walked=3 resolved=2 marked=0 unresolved=1 finding=CHAIN_HOP_UNRESOLVED)
exit=1
```

Verdict: **killed**.

Restoration: pristine bytes copied back. `hop2_hash_match=yes`. `cmp` identical. Tree hashes equal the pristine tree above. Restored detector: CLEAN, exit 0. Probe sha unchanged (`d4427ffd…`).

The standing `broken-dead/` arm is the same break class, present as files, not only as this transient edit. It fired the same way (target name `corpus/hop3-primary.md` instead of `corpus/hop3-primarx.md`).

## Precedent gate, not averaged in

`kagi-shokunin/corpus/claim-ledger.sh` sha256 `93c5827202b9cdecd6874e75c5dac5281eeae07eddeeff3883bd0da14bfbcd29`. Read-only. Citations mode (`:986-994`) prints `CITATION_GATE: CLEAN|BROKEN` and exits 0/1. A dead checked-class path must be labelled on its own line or it fails (`:45-46`, `:431-433`). Marker set (`:440`) is `scratch|ephemeral|relocat|formerly|no longer|removed|renamed|historical`. The word `unresolved` is not in that set.

Checked classes (`:434-438`) are `corpus/…`, `knowledge/…`, `lessons/…`, `<lane>-shokunin/…`, `ufo/…`, `.ufo/…`, and six root doc names. A bare name is not a path (`:430`).

### Last-token blind spot (observation)

On the original fixture, every `cites:` path is the last token of its line. Citations mode then reports `cites=0` and CLEAN, including on `broken-dead` (docs=3, exit 0) and on intact (docs=4, exit 0).

`bash -x` on intact `hop2-aggregator.md` showed `content='cites: corpus/hop3-primary.md'` and a `norm_tok` of `cites:` only. The path token was not classified.

Controlled files under `/tmp/chousa-ledger-tok.SgCCiW`, same citations mode:

| file | line | result |
|---|---|---|
| `last.md` | `see corpus/nope.md` | CLEAN cites=0 exit 0 |
| `space.md` | `see corpus/nope.md ` (trailing space) | UNRESOLVED exit 1 |
| `word.md` | `see corpus/nope.md end` | UNRESOLVED exit 1 |
| `last-ok.md` | `see corpus/ok.txt` (file exists) | CLEAN cites=0 exit 0 |
| `ok-word.md` | `see corpus/ok.txt end` | CLEAN cites=1 exit 0 |
| `selftest-shape.md` | `` see `corpus/nope.md` here `` | UNRESOLVED exit 1 |

Inference, from that trace plus `claim-ledger.sh:574`: the splitter is `printf '%s'` (no added newline) piped to `tr ' ' '\n'`, then `while IFS= read`. A final token with no trailing newline is not consumed by the loop body. The shipped selftest does not hit this: `claim-ledger.sh:1103-1104` puts the word `here` after the path.

This is a coverage finding about that gate. It is not permission to change it, and it is not a surviving mutant of `chain-walk.sh`. The one-byte mutant above is the last token of its line, and `chain-walk.sh` killed it.

### Fair comparison

`ledger-visible/<arm>/` is a copy with one trailing space on each `cites:` line, so the path is not the last token. `chain-walk.sh` on those copies repeated the same verdicts as the original arms (CLEAN / DRIFT / DRIFT / DRIFT / CLEAN for intact, dead, summary, url, marked).

Citations mode on the visible copies:

| arm | docs scanned | citation gate | exit | vs chain probe |
|---|---|---|---|---|
| intact, all four files | cites=3 docs=4 | CLEAN | 0 | agrees (no fire) |
| broken-dead, all three files | `UNRESOLVED corpus/hop2-aggregator.md:2 corpus/hop3-primary.md (local)` cites=3 | BROKEN | 1 | agrees (fires) |
| broken-dead, record only | cites=1 docs=1 | CLEAN | 0 | disagrees — does not walk into hop 2 |
| broken-summary, all three | cites=2 docs=3 | CLEAN | 0 | disagrees — `コトバンク` is not a checked class |
| broken-url, all three | cites=2 docs=3 | CLEAN | 0 | disagrees — URL is not a checked class |
| marked, all three | UNRESOLVED the same dead path | BROKEN | 1 | disagrees — `unresolved` is not in `MARK_RE` |

Record-only command (clean re-run, no trailing space on the path argument):

```text
bash kagi-shokunin/corpus/claim-ledger.sh citations \
  --root /tmp/chousa-chainhop-fixture/ledger-visible/broken-dead \
  --docs /tmp/chousa-chainhop-fixture/ledger-visible/broken-dead/corpus/record.md
CITATION_GATE: CLEAN (cites=1 docs=1 unresolved=0 ephemeral=0 labeled=0)
exit=0
```

Same tree, chain probe: DRIFT exit 1. A flat scan of the record does not follow the hop. That is the gap `SKILL.md:19` names (do not stop at a summary / follow each hop) and that a single-document citation scan does not close unless every hop file is already in the doc set and the broken token is a checked-class path.

`kumitate-shokunin/scripts/cite-check.mjs` was not run. No claim about it.

`anchorcheck.py:17-19` is the other precedent for "marked dead is reported and not counted as validated" (`LOST-RECORDED`). It was not executed on this fixture. The marked arm's no-fire result is from `chain-walk.sh` only.

## Observation / inference / unknown

Observation:

- Intact three-hop does not fire. Unmarked dead hop 3 fires. One-byte pointer mutant is killed. Restored bytes match and do not fire.
- Summary token, URL, and `..` each fire on hop 3. Marked dead hop does not fire.
- Named gate file was absent at the sweep above.
- Precedent citations mode, once the path is not the last token, fires on the dead `corpus/` hop when that file is in `--docs`, and does not fire on the summary token, the URL, or a record-only scan.
- Precedent citations mode does fire on the marked arm.
- Network trace of the URL arm listed no network syscalls.

Inference:

- The export lines `コトバンク` / `arxiv.org` are the summary-stop class in `SKILL.md:19`, encoded here as a hop cite. The exports themselves are not a three-hop record.
- The last-token miss is the `printf '%s'` / `read` interaction at `claim-ledger.sh:574`. The behavioral difference (trailing space vs not) was measured; the mechanism sentence is that inference.
- A chain checker that only scans the starting record will miss a break at hop 3. Measured on the visible broken-dead tree.

Unknown:

- Whether a later `tools/research-gate.sh` will use this label, this marker spelling, or this length rule.
- Whether a marker on the previous line, a symlink hop, or a past-EOF line anchor would fire. Those arms were not run.
- What the two exit-0 pids in the strace output were.
- Whether the export chrome, if fetched, would resolve. Not fetched. Not claimed.

## Rejections kept

- Rejected reading "claim-ledger CLEAN on original `broken-dead`" as "the chain is intact." cites=0 there means the path was not seen.
- Rejected reading the marked arm as a fire. The skill clause accepts a marked unresolved hop. The precedent gate's fire on that arm is a marker-vocabulary mismatch, not a second verdict on the clause.
- Rejected treating `コトバンク` or `https://example.invalid/daijisen` as resolved because a string was present.
- Rejected shipping this probe as `tools/research-gate.sh`, printing `RESEARCH_GATE:`, or editing the lane.
- A claim-ledger miss (summary, URL, record-only, last-token) is a coverage finding about that gate. It does not change the chain clause.

## Proposal (not admitted)

- Parent gate should walk embedded hops, not only tokens in the starting record. Ground: the record-only row above, plus `SKILL.md:19`. The walk itself is not yet a landed script.
- Marker token should be one declared spelling. This probe used the substring `unresolved`. kagi's set does not include it. Leaving both unlabeled will make the two gates disagree on a marked hop, as measured.
- `CHAIN_HOP_UNRESOLVED` waits on the finding-id note. It is the prompt's example, used here so the fire is greppable.

## Pins (sha256, size, path under the fixture root)

Standing arms and probe:

```text
d4427ffd040ad9215471994febfc326bfda70bc61c750ac5d8d99acea80d1b8e  2964  chain-walk.sh
80e1698fba01510895c57298cb1ab68d1cd9e3ee1a8e2d17f8b39e2fcf8b0925   103  intact/corpus/record.md
70d8a476d255c011dc09da8628c1aaf87d35465c87202b4598241380d60ce21a    83  intact/corpus/hop1-secondary.md
1db9b7f67c39950bb41d7ccfc52bfc5855810a40bbaa6d276cf3abc68aa96077    79  intact/corpus/hop2-aggregator.md
53ef773ef4491a6b231a42f71e0edb2c1d45b3f9e7240e81576ba6506105b61c    88  intact/corpus/hop3-primary.md
184e9eebafbd865c6082bbc62d0010ba4e85dfaa2240d9f345622dab5ec11b51    85  broken-dead/corpus/hop2-aggregator.md
e82ff44fda6914483e30bcdd71c8097af70aceb6e686513f17e80b2dcf05862a    72  broken-summary/corpus/hop2-aggregator.md
7cb35f8349f54a753520602e74334826b6dd8bdfd1aed2842765037de7539510    99  broken-url/corpus/hop2-aggregator.md
1d67d948dbb17f241ec3cdf6d11966866879de5b66544abbcac2b8cd3710824d   102  marked/corpus/hop2-aggregator.md
```

`record.md` and `hop1-secondary.md` hashes match across intact, broken-dead, broken-summary, broken-url, marked, and the restored scratch (`80e1698f…`, `70d8a476…`). Scratch hop-2 and hop-3 match intact after restore.

Replay helper `run-probe.sh` is in the temp dir and is not part of the measured arms.
