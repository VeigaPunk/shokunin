# Round-13 preservation gate — `verify-protocol.sh`

**Owner:** `protocol` lane. **Write scope:** `.ufo/waves/round-13/` only; read-only elsewhere.
**Type:** **gate** (worst case a verifier that can fail — proven in §4 and §6), not a probe.
**Pinned values:** `anchor-phrases.txt`, `modal-census.tsv`, `shonen-seed.txt` (this directory).
**Entry command:** `sh .ufo/waves/round-13/verify-protocol.sh PROTOCOL.md` — works from any cwd.
**Self-test spelling:** `--selftest` (exit 0 iff 8/8 cases pass).
**Verdict map:** `0 clean | 1 findings | 2 could-not-evaluate | 3 no-baseline`; every code declared here.
**Revision measured:** `PROTOCOL.md` 526 lines / 49269 bytes, `md5 63de15a37a42ce57decb951a7e8aa2f0`.
A verdict names the revision it grades; the expected values in this directory are derived from that revision.

Why this exists: the round-11 census (`../round-11/verify-census.sh`, `grep -qE` over TSV predicates)
is a *predicate-presence* test. A probe this round proved it passes `93/93` after a global
`MUST`→`SHOULD` rewrite and after rewording obligations that leave another occurrence of the predicate
phrase behind. This gate adds the four things presence cannot see: **verbatim normative anchors**,
**per-section modal-token floors**, **the canonical seed's byte identity**, and **the appendix digest's
rows and pointer resolution**.

---

## 1. Checks (ids are stable strings)

| id | what it proves |
|---|---|
| `census` | delegates to `../round-11/verify-census.sh <target> <census-tsv>`; every `MISS` row is a finding. Default census = `obligation-census-r13.tsv` when present, else `../round-11/obligation-census.tsv`; the path used and its row count are reported. |
| `anchors` | every line of `anchor-phrases.txt` (61 phrases: 51 body/gate + 10 appendix-only) occurs as a fixed string in the wrap-normalized target. |
| `modals` | per-`## `-section count of `MUST\|REQUIRED\|NEVER\|never\|must\|required\|only\|may not\|must not` ≥ the floor in `modal-census.tsv`. |
| `caps` | total lines ≤ `--max-lines` (default 470) and body inline `round-N` refs ≤ `--max-body-refs` (default 4); body = everything before the `## Appendix` heading. |
| `structure` | the nine `## ` headings exist in the contract order (ASCII prefix keys, `## Appendix` tolerated as a prefix so the em-dash tail may be reworded). |
| `seed` | the canonical `SHONEN.md` seed block is byte-identical to `shonen-seed.txt`. |
| `appendix` | ≤ 0 vs floor: the digest keeps ≥ 32 data rows, and every body pointer `(§Appendix, "X")` resolves to a row whose first column contains `X`. |
| `xref` | every `§<Name>` names a heading of the target (first-word match against the `## ` heading set, plus a committed allowlist of round-report section names). |

Output grammar: one `INFO <check-id> <detail>` line per check, one `FAIL <check-id> <detail>` line per
finding, then `verify-protocol: <clean|findings> checks=8 failed=<n>`. `failed` counts **distinct check
ids** that emitted at least one finding (a census with three `MISS` rows reports `failed=1`).
`--json` prints one JSON object instead of the text report (validated in §6).

The table above describes **single-file mode** (the whole protocol in `<target>`, the mode the eight
seeded cases prove). With `--appendix FILE` the same eight ids grade a body plus the moved digest — the
per-check split is §8.1.

---

## 2. Clean run against the pinned revision

```console
$ wc -l -c PROTOCOL.md; md5sum PROTOCOL.md
  526 49269 PROTOCOL.md
63de15a37a42ce57decb951a7e8aa2f0  PROTOCOL.md

$ sh .ufo/waves/round-13/verify-protocol.sh PROTOCOL.md --max-lines 526
INFO census /home/vgpnk/projects/shokunin/.ufo/waves/round-13/obligation-census-r13.tsv rows=156 miss=0 156/156 obligations found; 0 MISSING
INFO anchors /home/vgpnk/projects/shokunin/.ufo/waves/round-13/anchor-phrases.txt phrases=51 missing=0 line-exact-missing=0
INFO modals /home/vgpnk/projects/shokunin/.ufo/waves/round-13/modal-census.tsv sections=9 floor-sum=120 measured-sum=120 regex=MUST|REQUIRED|NEVER|never|must|required|only|may not|must not
INFO caps PROTOCOL.md lines=526/526 body-refs=4/4 (appendix heading at line 487)
INFO structure keys=## Lifecycle|## Promotion gates|## Round-robin rounds|## Evidence standard|## Gate standard|## File contract per shokunin repo|## Invariants|## Fleet-2 conventions (adopted)|## Appendix order=contract
INFO seed /home/vgpnk/projects/shokunin/.ufo/waves/round-13/shonen-seed.txt header-line=400 extracted-lines=8 byte-identical=yes
INFO appendix PROTOCOL.md rows=32/32 body-pointers=19
INFO xref PROTOCOL.md refs=12 headings=9 unresolved=0 allowlist=Closure Conformance Audit Integrator Stale-lane Dispatch L2 Push
verify-protocol: clean checks=8 failed=0
exit=0
```

`--max-lines 526` names the measured length of *this* revision; the flag is the record of which
revision the verdict was taken against. *The block above is the verdict as taken before the
appendix-mode addition (§8); that addition extended the INFO grammar (`line-exact-missing=`, `scope=`,
`rows-source=`, `modals-appendix`) without touching any expected value — §8.7 re-runs the same
command on the live revision with the current script, and §1's check table still describes every id
the same way.* With the default flags the same target reports exactly one
finding — the debt the compaction round exists to repay (declared deviation D1 in §9):

```console
$ sh .ufo/waves/round-13/verify-protocol.sh PROTOCOL.md
INFO caps PROTOCOL.md lines=526/470 body-refs=4/4 (appendix heading at line 487)
FAIL caps total lines 526 > --max-lines 470
verify-protocol: findings checks=8 failed=1
exit=1
```
(the other seven `INFO` lines are identical to the block above; only the `caps` line and the tally differ.)

Exit-code map, each demonstrated:

```console
$ sh .ufo/waves/round-13/verify-protocol.sh /nonexistent.md; echo exit=$?
verify-protocol: could-not-evaluate checks=8 failed=0 target not found: /nonexistent.md
exit=2
$ sh .ufo/waves/round-13/verify-protocol.sh PROTOCOL.md --max-lines abc; echo exit=$?
verify-protocol: bad --max-lines: abc
exit=2
$ sh .ufo/waves/round-13/verify-protocol.sh PROTOCOL.md --census /nope.tsv; echo exit=$?
verify-protocol: could-not-evaluate checks=8 failed=0 missing expected values: /nope.tsv
exit=2
$ cp .ufo/waves/round-13/verify-protocol.sh /tmp/lonely/ && (cd /tmp/lonely && sh verify-protocol.sh PROTOCOL.md --selftest); echo exit=$?
verify-protocol: no-baseline checks=0 failed=0 missing expected values: /tmp/lonely/anchor-phrases.txt /tmp/lonely/modal-census.tsv /tmp/lonely/shonen-seed.txt /tmp/lonely/../round-11/verify-census.sh /tmp/lonely/obligation-census-r13.tsv
exit=3
$ (cd /tmp && sh /home/vgpnk/projects/shokunin/.ufo/waves/round-13/verify-protocol.sh /home/vgpnk/projects/shokunin/PROTOCOL.md --max-lines 526 --json); echo exit=$?
{"target":"/home/vgpnk/projects/shokunin/PROTOCOL.md","status":"clean","checks":8,"failed":0,"census":{"path":"/home/vgpnk/projects/shokunin/.ufo/waves/round-13/obligation-census-r13.tsv","rows":156},"findings":[]}
exit=0
```

---

## 3. Self-test — the eight seeded cases

`--selftest` copies the target into a temp dir, applies one mutation per case, and asserts that the
named check id fires (expected ids must be a **subset** of the observed findings, and the mutant must
exit `1`); the unmutated target must be clean. Case 1 is the baseline the brief requires. The line cap
for the whole selftest run is the target's current line count unless `--max-lines` is given explicitly
(deviation D1), so the baseline is a true clean-state assertion at any revision, before and after the
compaction lands.

```console
$ sh .ufo/waves/round-13/verify-protocol.sh PROTOCOL.md --selftest
selftest target=PROTOCOL.md lines=526 caps=--max-lines 526 --max-body-refs 4 census=/home/vgpnk/projects/shokunin/.ufo/waves/round-13/obligation-census-r13.tsv
selftest 1/8 baseline-unmutated expect=[clean] got=[clean] rc=0 ok
selftest 2/8 drop-anchor-phrase expect=[anchors] got=[anchors] rc=1 ok
selftest 3/8 weaken-modals-invariants expect=[modals] got=[modals] rc=1 ok
selftest 4/8 append-60-filler-lines expect=[caps] got=[caps] rc=1 ok
selftest 5/8 drop-named-appendix-row expect=[appendix] got=[appendix] rc=1 ok
selftest 6/8 rename-heading expect=[structure xref] got=[modals structure xref] rc=1 ok
selftest 7/8 alter-seed-line expect=[seed] got=[seed] rc=1 ok
selftest 8/8 truncate-last-section expect=[structure] got=[appendix modals structure xref] rc=1 ok
selftest: 8/8 passed
exit=0
```

| # | mutation (applied to a temp copy) | expected | observed |
|---|---|---|---|
| 1 | none (baseline) | clean, exit 0 | clean, exit 0 |
| 2 | first anchor phrase removed (all occurrences, byte-level) | `anchors` | `anchors` |
| 3 | every `never` in `## Invariants` rewritten to `may` (floor 11 → 8) | `modals` | `modals` |
| 4 | 60 blank-line-free filler lines appended, cap = baseline lines | `caps` | `caps` |
| 5 | first body-named appendix data row deleted | `appendix` | `appendix` |
| 6 | `## Invariants` renamed to `## Core invariants` | `structure`, `xref` | `structure`, `xref` (+`modals`: the section key no longer matches, so its count is 0) |
| 7 | second seed `- [ ]` line altered | `seed` | `seed` |
| 8 | last section (from `## Appendix`) truncated away | `structure` | `structure` (+`appendix`, `modals`, `xref`, all consequences of the missing section) |

Case 4 needed one design decision: the cap is derived from the *unmutated* target, otherwise the
baseline case itself could never be clean while the pre-compaction text is 526 lines (D1).

---

## 4. Committed expected values — derivation commands and observed output

### 4.1 `anchor-phrases.txt` — verbatim normative substrings (51 body/gate + 10 appendix-only)

Coverage: the seven round-12 pins (row identity / `lane_rounds` never re-keys / `unadjudicable`;
orphaned-report order + the re-grade-to-`failed` condition + the aggregator-`corpus/` exclusion;
erratum appended after the filed bytes and never a rewrite; `progressing-weak`; L0 append-only +
integrator durability owner + cite-by-lane-and-round; `in-flight` ended only by a landed report;
`supersedes` MAY carry `entry`) and every operative requirement of `## Gate standard` (verdict map,
self-test, two evidences, registry, scope, closure consequence, delivery). Anchors are ASCII-only on
purpose (§6.4 shows the reason) and each pin anchor carries its modal word.

```console
$ awk 'substr($0,1,1)=="#"||$0==""{next}{n++}END{print n}' .ufo/waves/round-13/anchor-phrases.txt
51
$ grep -c '^#\|^$' .ufo/waves/round-13/anchor-phrases.txt
30
$ n=0; miss=0; while IFS= read -r l; do case $l in ""|"#"*) continue;; esac; n=$((n+1)); \
    grep -F -q -- "$l" PROTOCOL.md || { miss=$((miss+1)); printf 'MISS %s\n' "$l"; }; \
  done < .ufo/waves/round-13/anchor-phrases.txt; printf 'checked=%s missing=%s\n' "$n" "$miss"
checked=51 missing=0
```

The gate itself reports the same result through its own reader, and additionally reports the
line-exact count as information (`INFO anchors … phrases=51 missing=0 line-exact-missing=0`).
Matching semantics are §6.5 / deviation D3. *The counts above are the state before the appendix-mode
addition; §8.2 records the ten appendix-only anchors and the resulting 61-phrase file.*

### 4.2 `modal-census.tsv` — per-section floors (9 rows)

Exact counting command used for every floor (also recorded in the file's comment header):

```console
$ for s in '## Lifecycle' '## Promotion gates' '## Round-robin rounds' '## Evidence standard' \
           '## Gate standard' '## File contract per shokunin repo' '## Invariants' \
           '## Fleet-2 conventions (adopted)' '## Appendix — incident digest (why these rules exist)'; do
    awk -v w="$s" 'index($0,w)==1 && length($0)==length(w){ins=1;next} /^## /{ins=0} ins{print}' PROTOCOL.md \
      | grep -oE 'MUST|REQUIRED|NEVER|never|must|required|only|may not|must not' | wc -l | tr -d ' ' | \
      awk -v s="$s" '{ printf "%s\t%s\n", s, $0 }'; done
## Lifecycle	2
## Promotion gates	3
## Round-robin rounds	57
## Evidence standard	10
## Gate standard	10
## File contract per shokunin repo	8
## Invariants	11
## Fleet-2 conventions (adopted)	4
## Appendix — incident digest (why these rules exist)	15
$ grep -oE 'MUST|REQUIRED|NEVER|never|must|required|only|may not|must not' PROTOCOL.md | wc -l
120
$ grep -oE 'MUST|REQUIRED|NEVER|never|must|required|only|may not|must not' PROTOCOL.md | sort | uniq -c
     16 must
      2 must not
     47 never
     49 only
      6 required
```

Per-section counts as measured today (floors = these numbers; floor sum 120 = total 120):

| section | tokens |
|---|---|
| `## Lifecycle` | 2 |
| `## Promotion gates` | 3 |
| `## Round-robin rounds` | 57 |
| `## Evidence standard` | 10 |
| `## Gate standard` | 10 |
| `## File contract per shokunin repo` | 8 |
| `## Invariants` | 11 |
| `## Fleet-2 conventions (adopted)` | 4 |
| `## Appendix — incident digest (why these rules exist)` | 15 |

The census file keys the appendix as the ASCII prefix `## Appendix` (the heading's em-dash tail is not
carried through a shell `read`, see §6.4); the check opens a section at the first line starting with the
key and closes it at the next `## ` line, which is exactly the slice the derivation above used.
`must not` counts as a single token (GNU `grep -oE` is leftmost-longest); `may not` occurs 0 times.

### 4.3 `shonen-seed.txt` — the canonical seed block, 8 lines

Extracted range: **`PROTOCOL.md:400-407`** — the four indented checklist lines plus their surrounding
indented block (header line, `Promotion to shokunin requires all of:`, and the internal blank lines).
Locating rule used by the gate (so a moved or re-prosed paragraph still resolves): find the first line
matching `^    # <name>`, then take the run of blank-or-4-space-indented lines that carries it, stripping
leading and trailing blanks.

```console
$ grep -n '^    # <name>' PROTOCOL.md
400:    # <name> — Promotion checklist
$ awk 'NR>=400 && NR<=407' PROTOCOL.md > .ufo/waves/round-13/shonen-seed.txt
$ awk 'NR>=400 && NR<=407' PROTOCOL.md > /tmp/seed-extract.txt
$ cmp /tmp/seed-extract.txt .ufo/waves/round-13/shonen-seed.txt; echo exit=$?
exit=0
$ wc -l .ufo/waves/round-13/shonen-seed.txt; md5sum .ufo/waves/round-13/shonen-seed.txt
8 .ufo/waves/round-13/shonen-seed.txt
07d0d4b5738400c4c42ac2eb5c7c3870  .ufo/waves/round-13/shonen-seed.txt
```

The gate's own reading of the same target: `INFO seed … header-line=400 extracted-lines=8 byte-identical=yes`.

### 4.4 Figures behind `caps`, `appendix`, `xref`

```console
$ awk '/^## Appendix/{print NR;exit}' PROTOCOL.md
487
$ awk 'NR<487' PROTOCOL.md | grep -o 'round-[0-9][0-9.]*' | wc -l
4
$ A=$(awk '/^## Appendix/{print NR;exit}' PROTOCOL.md); awk -v a="$A" 'NR>=a' PROTOCOL.md | grep '^|' | tail -n +3 | wc -l
32
$ grep -o '(§Appendix, "[^"]*")' PROTOCOL.md | wc -l; grep -o '(§Appendix, "[^"]*")' PROTOCOL.md | sort -u | wc -l
19
17
$ grep -o '§[^ ,;:)]*' PROTOCOL.md | sort | uniq -c
     20 §Appendix
      1 §Audit
      4 §Closure
      1 §Closure/§Conformance
      9 §Conformance
      1 §Dispatch
      2 §Evidence
      1 §Gate
      1 §Integrator
      3 §Invariants
      1 §L2
      1 §Push
      1 §Stale-lane
```

The 12 tokens the gate swept (`refs=12`) are the distinct ones after splitting on `§`; 9 headings
resolve them, and the 8 report-local names (`Closure Conformance Audit Integrator Stale-lane Dispatch
L2 Push`) are the committed allowlist — they appear only inside appendix pointer cells or as
`MISSION.md` section citations, never as PROTOCOL.md headings.

---

## 5. Verdict on the current compaction draft (stronger than the census, demonstrated)

The sibling seat's draft at `md5 d07056983b364e97d3b27c43170bd534` (434 lines) — *this reading is a
point-in-time observation: the draft is being iterated by another seat while this gate was built, and
the hash names exactly which revision was graded.* The r13 census is green on it
(`156/156, 0 MISSING`) — and the gate is not:

```console
$ wc -l .ufo/waves/round-13/PROTOCOL.compact.md; md5sum .ufo/waves/round-13/PROTOCOL.compact.md
434 .ufo/waves/round-13/PROTOCOL.compact.md
d07056983b364e97d3b27c43170bd534  .ufo/waves/round-13/PROTOCOL.compact.md

$ sh .ufo/waves/round-13/verify-protocol.sh .ufo/waves/round-13/PROTOCOL.compact.md --max-lines 470
INFO census /home/vgpnk/projects/shokunin/.ufo/waves/round-13/obligation-census-r13.tsv rows=156 miss=0 156/156 obligations found; 0 MISSING
INFO anchors /home/vgpnk/projects/shokunin/.ufo/waves/round-13/anchor-phrases.txt phrases=51 missing=0 line-exact-missing=7
INFO modals /home/vgpnk/projects/shokunin/.ufo/waves/round-13/modal-census.tsv sections=9 floor-sum=120 measured-sum=106 regex=MUST|REQUIRED|NEVER|never|must|required|only|may not|must not
INFO caps .ufo/waves/round-13/PROTOCOL.compact.md lines=434/470 body-refs=1/4 (appendix heading at line 430)
INFO structure keys=## Lifecycle|## Promotion gates|## Round-robin rounds|## Evidence standard|## Gate standard|## File contract per shokunin repo|## Invariants|## Fleet-2 conventions (adopted)|## Appendix order=contract
INFO seed /home/vgpnk/projects/shokunin/.ufo/waves/round-13/shonen-seed.txt header-line=347 extracted-lines=8 byte-identical=yes
INFO appendix .ufo/waves/round-13/PROTOCOL.compact.md rows=0/32 body-pointers=17
INFO xref .ufo/waves/round-13/PROTOCOL.compact.md refs=6 headings=9 unresolved=0 allowlist=Closure Conformance Audit Integrator Stale-lane Dispatch L2 Push
FAIL modals section '## Appendix' normative tokens 0 < floor 15
FAIL appendix appendix data rows 0 < floor 32
FAIL appendix body pointer (§Appendix, "Prompt embeds contract") resolves to no row
FAIL appendix body pointer (§Appendix, "Lands last") resolves to no row
FAIL appendix body pointer (§Appendix, "Orphaned report") resolves to no row
FAIL appendix body pointer (§Appendix, "Stale-lane actuator") resolves to no row
FAIL appendix body pointer (§Appendix, "Marker vs report") resolves to no row
FAIL appendix body pointer (§Appendix, "No closure channel") resolves to no row
FAIL appendix body pointer (§Appendix, "Closure entries") resolves to no row
FAIL appendix body pointer (§Appendix, "Liveness probes") resolves to no row
FAIL appendix body pointer (§Appendix, "Unlanded report") resolves to no row
FAIL appendix body pointer (§Appendix, "Row identity") resolves to no row
FAIL appendix body pointer (§Appendix, "Append-only `rounds`") resolves to no row
FAIL appendix body pointer (§Appendix, "Ledger") resolves to no row
FAIL appendix body pointer (§Appendix, "Evidence standard") resolves to no row
FAIL appendix body pointer (§Appendix, "Canonical form") resolves to no row
FAIL appendix body pointer (§Appendix, "Lane identity") resolves to no row
FAIL appendix body pointer (§Appendix, "L0 durability") resolves to no row
verify-protocol: findings checks=8 failed=2
exit=1
```

Read: anchors, seed, structure, xref, caps and the census are **clean** on the draft (the sibling's
revision restored wording that an earlier revision of it had changed — the same 51 anchors were
`missing=0` at every reading taken after that fix; an earlier reading at `md5 c4de7324…` had 6 genuine
anchor misses and is analysed below). The remaining gap is homogeneous: **the digest left the target**.
The draft points at `PROTOCOL-APPENDIX.md`, so the `## Appendix` section holds no table rows and every
`§Appendix` body pointer resolves to nothing *inside the file the protocol contract is read from*. That
is either a deliberate relocation — in which case this gate must be extended to grade the sibling
artifact and carry its expected values (§10 item 5) — or the digest must stay in `PROTOCOL.md`.

### Earlier draft, and why the criterion is wrap-normalized (D3)

An earlier revision of the same draft (`md5 c4de73245be0e7fb2a686844c9104b35`, 442 lines) exposed both
false positives and real losses. Line-exact matching reported 12 anchor misses; normalizing whitespace
inside a paragraph showed **6 genuine wording changes** and 6 pure re-wraps. The genuine six (verbatim
before → after) were:

1. `for durability only if that successor mission also terminates without landing it`
   → "sweeps it for durability only **after** a successor mission also terminates without landing it";
2. `the order never reaches aggregator-owned` → "**that** order never reaches aggregator-owned";
3. `report is a record: a correction to it lands in the correcting round's own report, or as an erratum`
   → "record: a correction lands in the correcting round's own report, or as an erratum";
4. `never by line number: the queue grows, so every line number moves` → "never by line number." (rationale dropped);
5. `and never from a status` → "— never from a status probe";
6. `the expected values committed in the owning repo and independent of the recomputation`
   → "expected values committed in the owning repo …" (article dropped).

The six re-wraps were phrases such as
`annotates it and never re-keys it, so last-wins is computed over `(id, entry.round)`` — intact in the
draft, split across two lines. A line-exact criterion would have demanded the lane fight the verifier
over line breaks; the normalized criterion demands only that the words survive.

---

## 6. Probe evidence beyond the eight seeded cases

### 6.1 Modal blindness — the check the census cannot make

```console
$ awk '{ gsub(/must/,"should"); gsub(/MUST/,"SHOULD"); print }' PROTOCOL.md > /tmp/modal.md
$ sh .ufo/waves/round-13/verify-protocol.sh /tmp/modal.md --max-lines 526 | grep -E '^FAIL|^verify-protocol'
FAIL modals section '## Round-robin rounds' normative tokens 46 < floor 57
FAIL modals section '## Evidence standard' normative tokens 8 < floor 10
FAIL modals section '## File contract per shokunin repo' normative tokens 6 < floor 8
FAIL modals section '## Invariants' normative tokens 10 < floor 11
FAIL modals section '## Appendix' normative tokens 13 < floor 15
FAIL census MISS F2 [FileContract] PROVINCE.md declared surfaces must resolve; correct to real path
verify-protocol: findings checks=8 failed=2
exit=1
```

### 6.2 Census delegation really fires

```console
$ awk '{ gsub(/unadjudicable/,"unjudicable"); print }' PROTOCOL.md > /tmp/censusmiss.md
$ sh .ufo/waves/round-13/verify-protocol.sh /tmp/censusmiss.md --max-lines 526 | grep -E '^FAIL census|^verify-protocol'
FAIL census MISS P14 [Step4] Pre-fleet-2 fleet-keyed entries carry no lane_rounds and are unadjudicable as lane-rounds
verify-protocol: findings checks=8 failed=2
exit=1
```

### 6.3 The `structure` order branch

```console
$ awk 'NR==346{next} {print}' PROTOCOL.md \
  | awk 'index($0,"## Evidence standard")==1 && !done { print "## Gate standard"; done=1 } { print }' > /tmp/order.md
$ sh .ufo/waves/round-13/verify-protocol.sh /tmp/order.md --max-lines 526 | grep -E '^FAIL|^verify-protocol'
FAIL modals section '## Gate standard' normative tokens 0 < floor 10
FAIL structure heading out of order: ## Gate standard at line 306 after line 307
verify-protocol: findings checks=8 failed=2
exit=1
```

### 6.4 Non-ASCII must not travel through a shell `read`

Observed in this environment (bash 5.x as `/bin/sh`): a line carrying UTF-8 bytes read with
`read -r` is transcoded (`e2 80 94` → `c3 a2 c2 80 c2 94` for an em dash), while `awk getline`,
command substitution and literal arguments are byte-exact. Consequence, and the reason every anchor and
every modal-census key is ASCII: patterns that survive a `read` are the only ones a POSIX `sh` loop can
compare byte-for-byte. The gate therefore reads both committed files with `awk getline`, and the
appendix key is the ASCII prefix `## Appendix`.

### 6.5 Anchor matching is fixed-string over the wrap-normalized text

No regex, no case folding: the phrase must occur literally after collapsing intra-line whitespace runs
to one space and rejoining wrapped lines of one paragraph with a single space. A blank line stays a hard
boundary, so a phrase cannot be satisfied by stitching two paragraphs together. `line-exact-missing` is
reported alongside, purely as information.

### 6.6 `--json` validity

```console
$ sh .ufo/waves/round-13/verify-protocol.sh /tmp/modal.md --max-lines 526 --json > /tmp/p5.json; echo exit=$?
exit=1
$ python3 -c "import json; d=json.load(open('/tmp/p5.json')); print('valid status=%s checks=%s failed=%s findings=%d first=%s' % (d['status'], d['checks'], d['failed'], len(d['findings']), d['findings'][0]['check']))"
valid status=findings checks=8 failed=2 findings=6 first=census
```

### 6.7 The self-test is not a tautology

Run with a cap the target cannot meet: the baseline case must fail and the tally must say so.

```console
$ sh .ufo/waves/round-13/verify-protocol.sh PROTOCOL.md --selftest --max-lines 100
selftest target=PROTOCOL.md lines=526 caps=--max-lines 100 --max-body-refs 4 census=/home/vgpnk/projects/shokunin/.ufo/waves/round-13/obligation-census-r13.tsv
selftest 1/8 baseline-unmutated expect=[clean] got=[caps] rc=1 FAIL
  | INFO census /home/vgpnk/projects/shokunin/.ufo/waves/round-13/obligation-census-r13.tsv rows=156 miss=0 156/156 obligations found; 0 MISSING
  | INFO anchors /home/vgpnk/projects/shokunin/.ufo/waves/round-13/anchor-phrases.txt phrases=51 missing=0 line-exact-missing=0
  | INFO modals /home/vgpnk/projects/shokunin/.ufo/waves/round-13/modal-census.tsv sections=9 floor-sum=120 measured-sum=120 regex=MUST|REQUIRED|NEVER|never|must|required|only|may not|must not
  | INFO caps PROTOCOL.md lines=526/100 body-refs=4/4 (appendix heading at line 487)
  | INFO structure keys=## Lifecycle|## Promotion gates|## Round-robin rounds|## Evidence standard|## Gate standard|## File contract per shokunin repo|## Invariants|## Fleet-2 conventions (adopted)|## Appendix order=contract
  | INFO seed /home/vgpnk/projects/shokunin/.ufo/waves/round-13/shonen-seed.txt header-line=400 extracted-lines=8 byte-identical=yes
exit=1
```

---

## 7. Files

```console
$ wc -l .ufo/waves/round-13/verify-protocol.sh .ufo/waves/round-13/anchor-phrases.txt \
        .ufo/waves/round-13/modal-census.tsv .ufo/waves/round-13/modal-census-appendix.tsv \
        .ufo/waves/round-13/shonen-seed.txt
  971 .ufo/waves/round-13/verify-protocol.sh
   98 .ufo/waves/round-13/anchor-phrases.txt
   26 .ufo/waves/round-13/modal-census.tsv
   16 .ufo/waves/round-13/modal-census-appendix.tsv
    8 .ufo/waves/round-13/shonen-seed.txt
 1119 total
$ grep -n '/home/' .ufo/waves/round-13/verify-protocol.sh .ufo/waves/round-13/anchor-phrases.txt \
        .ufo/waves/round-13/modal-census.tsv .ufo/waves/round-13/shonen-seed.txt; echo exit=$?
exit=1
$ grep -n '/tmp' .ufo/waves/round-13/verify-protocol.sh .ufo/waves/round-13/anchor-phrases.txt \
        .ufo/waves/round-13/modal-census.tsv .ufo/waves/round-13/shonen-seed.txt; echo exit=$?
exit=1
```

No absolute paths and no `/tmp` references in any committed expected-value or script file (the two
`grep`s return nothing); all are POSIX text files ending in a newline, and the two TSVs carry their
derivation in `#` comment headers. Digest of the delivered bytes (as of the appendix-mode addition):

```console
$ md5sum .ufo/waves/round-13/verify-protocol.sh .ufo/waves/round-13/anchor-phrases.txt \
         .ufo/waves/round-13/modal-census.tsv .ufo/waves/round-13/modal-census-appendix.tsv \
         .ufo/waves/round-13/shonen-seed.txt
fa99ec26a69036c8f72ada1702e7115f  .ufo/waves/round-13/verify-protocol.sh
50133b4202d6b5f7e3f61ec9e0779a15  .ufo/waves/round-13/anchor-phrases.txt
3a763db7728e6b05757ca5c628d5c87c  .ufo/waves/round-13/modal-census.tsv
7068abfc52125d975fd2c3eb3c02acb8  .ufo/waves/round-13/modal-census-appendix.tsv
07d0d4b5738400c4c42ac2eb5c7c3870  .ufo/waves/round-13/shonen-seed.txt
```

`verify-protocol.sh` resolves its expected values
relative to its own directory and takes the target as a path, so it runs from any cwd. It uses POSIX
`sh` plus `awk/grep/cmp/mktemp/rm` only — no python, no node, no network, no environment variables —
and is `set -u`-safe; `sh -n` is clean.

---

## 8. Two-file mode (`--appendix FILE`) — added after the design change

Motivation: the obligation-preserving single-file floor was measured at 486 lines on the surveyed
revision, so reaching the ≤470 target requires the 40-row `## Appendix — incident digest` to move into
a committed sibling artifact with a short pointer block left behind. The gate was extended (Main's
adaptation, round 13) so the digest's obligations stay graded where they now live. **Single-file mode is
unchanged** and still proven by its own 8-case suite; the appendix-mode addition leaves every
single-file expected value untouched.

### 8.1 Contract

```console
$ sh verify-protocol.sh <body.md> --appendix FILE \
      [--appendix-census TSV] [--max-appendix-lines N]
```

| check | body (`<target>`) | appendix artifact (`FILE`) |
|---|---|---|
| `census` | delegated census against the body; every MISS is a finding | `--appendix-census TSV` (optional) is run against `FILE` and its MISSes fold into the same `census` check id, labelled `[TSV]`; without `--appendix` a MISS whose predicate matches `FILE` is annotated `[appendix-scoped …]` |
| `anchors` | matched against body **+** artifact (union) | same |
| `modals` | the `modal-census.tsv` floors minus the `## Appendix` row (8 sections) | the `modal-census-appendix.tsv` floor, applied to `FILE`'s `## Appendix` section, or to `FILE` whole when it carries no `## ` heading |
| `caps` | `--max-lines` (default 470) + `--max-body-refs` | lines ≤ `--max-appendix-lines` (default 60), reported separately |
| `structure` | the eight body headings in order | must carry an H2 `## Appendix … incident digest …` heading |
| `seed` | body, unchanged | — |
| `appendix` | the body's `(§Appendix, "X")` pointers | the table they resolve against: rows ≥ 32 (header + separator excluded) |
| `xref` | all `§<Name>` of body + artifact resolve against the heading set of both | `Appendix` is a declared resolvable name in this mode |

Exit map, error paths and INFO/FAIL grammar are unchanged; `--json` gains
`"appendix":{"path":…,"lines":…,"rows":…}`. Demonstrated:

```console
$ sh .ufo/waves/round-13/verify-protocol.sh <body> --appendix /nope.md; echo exit=$?
verify-protocol: could-not-evaluate checks=8 failed=0 appendix artifact not found: /nope.md
exit=2
$ sh .ufo/waves/round-13/verify-protocol.sh <body> --appendix <FILE> --max-appendix-lines x; echo exit=$?
verify-protocol: bad --max-appendix-lines: x
exit=2
$ sh .ufo/waves/round-13/verify-protocol.sh <body> --appendix <FILE> --max-lines 460 --json | python3 -c "import json,sys; d=json.load(sys.stdin); print('valid', d['status'], d['failed'], d['appendix'], len(d['findings']))"
valid findings 1 {'path': '.ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md', 'lines': 40, 'rows': 32} 1
```

### 8.2 Committed expected values added

`modal-census-appendix.tsv` — one row, `## Appendix<TAB>15`, same token command as
`modal-census.tsv`; the floor is the appendix section's token count at the pinned revision, and it
still holds at the live one:

```console
$ awk '/^## Appendix/{print NR;exit}' PROTOCOL.md
502
$ awk -v a=502 'NR>=a' PROTOCOL.md | grep -oE 'MUST|REQUIRED|NEVER|never|must|required|only|may not|must not' | wc -l
15
$ grep -oE 'MUST|REQUIRED|NEVER|never|must|required|only|may not|must not' .ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md | wc -l
15
```

`anchor-phrases.txt` — 61 phrases: the 51 single-file anchors plus a marked block of 10
appendix-only anchors, each verified at the baseline to live in the digest and nowhere in the body:

```console
$ sed -n '/^# --- appendix-only/,$p' .ufo/waves/round-13/anchor-phrases.txt | while IFS= read -r l; do \
    case $l in ""|"#"*) continue;; esac; \
    b=$(grep -F -q -- "$l" /tmp/body.txt && echo yes || echo no); \
    x=$(grep -F -q -- "$l" /tmp/appx.txt && echo yes || echo no); printf 'body=%s appendix=%s | %s\n' "$b" "$x" "$l"; done
body=no appendix=yes | the progressing test's "files modified under its repo" half attributes a sibling's work to the lane
body=no appendix=yes | kotoba r13 graded progressing on three `aggregator-shokunin` commits
body=no appendix=yes | tick counter resets on driver restart
body=no appendix=yes | 46 of 60 reports swept into
body=no appendix=yes | the kengaku-r10 and kumitate-r10 questions sat uncommitted across two rounds
body=no appendix=yes | its own r12 work uncommitted, no `complete` line, counter still 12
body=no appendix=yes | self-declares "a report, not a gate"
body=no appendix=yes | 0 of 62 reports committed under a lane identity
body=no appendix=yes | entry-keyed last-wins reproduces the round-11 record exactly
body=no appendix=yes | falsified on round-11 re-execution already at write time
```

(`/tmp/body.txt` = `awk -v a=502 'NR<a' PROTOCOL.md`, `/tmp/appx.txt` = `awk -v a=502 'NR>=a' PROTOCOL.md`.)

### 8.3 Selftest in appendix mode — both tallies

Two files in the temp dir, ten appendix cases (the eight single-file mutations adapted to the pair plus
two appendix-specific ones), and the eight single-file cases nested over the reversible
body+artifact reconstruction. Verbatim, against the current drafts — the only elision is the random
`mktemp -d` path, written `/…/selftest/…` below (each nested line is prefixed with `  | ` because the
nested suite's output is passed through indented):

```console
$ sh .ufo/waves/round-13/verify-protocol.sh .ufo/waves/round-13/PROTOCOL.compact.md \
      --appendix .ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md --selftest --max-lines 460
selftest single-file suite (nested over body+artifact reconstruction /…/selftest/single.md):
  | selftest target=/…/selftest/single.md lines=500 caps=--max-lines 500 --max-body-refs 4 census=…/obligation-census-r13.tsv
  | selftest 1/8 baseline-unmutated expect=[clean] got=[clean] rc=0 ok
  | selftest 2/8 drop-anchor-phrase expect=[anchors] got=[anchors] rc=1 ok
  | selftest 3/8 weaken-modals-invariants expect=[modals] got=[modals] rc=1 ok
  | selftest 4/8 append-60-filler-lines expect=[caps] got=[caps] rc=1 ok
  | selftest 5/8 drop-named-appendix-row expect=[appendix] got=[appendix] rc=1 ok
  | selftest 6/8 rename-heading expect=[structure xref] got=[modals structure xref] rc=1 ok
  | selftest 7/8 alter-seed-line expect=[seed] got=[seed] rc=1 ok
  | selftest 8/8 truncate-last-section expect=[structure] got=[anchors appendix modals structure xref] rc=1 ok
  | selftest: 8/8 passed
selftest-appendix target=.ufo/waves/round-13/PROTOCOL.compact.md lines=459 appendix=.ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md lines=40 caps=--max-lines 460 --max-appendix-lines 40 --max-body-refs 4 census=…/obligation-census-r13.tsv
selftest-appendix 1/10 baseline-two-files expect=[target-verdict] got=[structure] rc=1 ok (unmutated target; mutation cases assert attribution)
selftest-appendix 2/10 drop-anchor-phrase-body expect=[anchors] got=[anchors structure] rc=1 ok
selftest-appendix 3/10 weaken-modals-invariants expect=[modals] got=[modals structure] rc=1 ok
selftest-appendix 4/10 append-60-filler-lines expect=[caps] got=[caps structure] rc=1 ok
selftest-appendix 5/10 drop-first-named-appendix-row expect=[appendix] got=[appendix structure] rc=1 ok
selftest-appendix 6/10 rename-heading expect=[structure xref] got=[modals structure xref] rc=1 ok
selftest-appendix 7/10 alter-seed-line expect=[seed] got=[seed structure] rc=1 ok
selftest-appendix 8/10 truncate-body-last-section expect=[structure] got=[anchors census modals structure] rc=1 ok
selftest-appendix 9/10 drop-last-named-appendix-row expect=[appendix] got=[anchors appendix structure] rc=1 ok
selftest-appendix 10/10 drop-appendix-only-anchor expect=[anchors] got=[anchors structure] rc=1 ok
selftest(appendix): 10/10 passed
selftest(combined): 18/18 passed (single-file nested + appendix)
exit=0
```

Case 9 deletes the row named by the **last** distinct body pointer and case 5 the row named by the
first (the brief's new case (a) and the adapted single-file case (d) coincide in class, so they target
different rows); case 10 drops the first appendix-only anchor and must fire `anchors`.

### 8.4 Run against the two current drafts (`--max-lines 460`)

```console
$ wc -l .ufo/waves/round-13/PROTOCOL.compact.md .ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md
  459 .ufo/waves/round-13/PROTOCOL.compact.md
   40 .ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md
$ sh .ufo/waves/round-13/verify-protocol.sh .ufo/waves/round-13/PROTOCOL.compact.md \
      --appendix .ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md --max-lines 460
INFO census /home/vgpnk/projects/shokunin/.ufo/waves/round-13/obligation-census-r13.tsv rows=169 miss=0 169/169 obligations found; 0 MISSING
INFO anchors /home/vgpnk/projects/shokunin/.ufo/waves/round-13/anchor-phrases.txt phrases=61 missing=0 line-exact-missing=7
INFO modals /home/vgpnk/projects/shokunin/.ufo/waves/round-13/modal-census.tsv sections=8 floor-sum=105 measured-sum=113 regex=MUST|REQUIRED|NEVER|never|must|required|only|may not|must not
INFO modals-appendix /home/vgpnk/projects/shokunin/.ufo/waves/round-13/modal-census-appendix.tsv sections=1 floor-sum=15 measured-sum=15 scope=.ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md
INFO caps body=.ufo/waves/round-13/PROTOCOL.compact.md lines=459/460 body-refs=1/4 (appendix heading at line 455); appendix=.ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md lines=40/60
INFO structure keys=## Lifecycle|## Promotion gates|## Round-robin rounds|## Evidence standard|## Gate standard|## File contract per shokunin repo|## Invariants|## Fleet-2 conventions (adopted) order=contract; appendix-artifact=.ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md digest-heading-line=none
INFO seed /home/vgpnk/projects/shokunin/.ufo/waves/round-13/shonen-seed.txt header-line=372 extracted-lines=8 byte-identical=yes
INFO appendix .ufo/waves/round-13/PROTOCOL.compact.md rows=32/32 body-pointers=16 rows-source=.ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md
INFO xref scope=.ufo/waves/round-13/PROTOCOL.compact.md+.ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md refs=12 headings=9 unresolved=0 allowlist=Closure Conformance Audit Integrator Stale-lane Dispatch L2 Push Appendix
FAIL structure appendix artifact carries no H2 '## Appendix ... incident digest ...' heading: .ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md
verify-protocol: findings checks=8 failed=1
exit=1
```

One finding, and it is the only thing standing between the drafts and a clean two-file verdict: the
artifact titles itself with an H1 (`# PROTOCOL-APPENDIX.md — incident digest (why these rules exist)`),
so the digest heading the contract requires (`## Appendix — incident digest (why these rules exist)`)
is absent. The 32 rows, the 16 pointers, the 61 anchors, the seed block, the appendix modal floor
(15/15), the body's eight-section floors and both line caps are all already green.

### 8.5 Clean-path proof (heading-corrected artifact copy)

```console
$ awk 'NR == 1 { print "## Appendix — incident digest (why these rules exist)"; next } { print }' \
      .ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md > /tmp/appx-clean/art.md
$ sh .ufo/waves/round-13/verify-protocol.sh .ufo/waves/round-13/PROTOCOL.compact.md \
      --appendix /tmp/appx-clean/art.md --max-lines 460; echo exit=$?
verify-protocol: clean checks=8 failed=0
exit=0
$ sh .ufo/waves/round-13/verify-protocol.sh .ufo/waves/round-13/PROTOCOL.compact.md \
      --appendix /tmp/appx-clean/art.md --selftest --max-lines 460 | tail -14
selftest-appendix target=.ufo/waves/round-13/PROTOCOL.compact.md lines=459 appendix=/tmp/appx-clean/art.md lines=40 caps=--max-lines 460 --max-appendix-lines 40 --max-body-refs 4 census=…/obligation-census-r13.tsv
selftest-appendix 1/10 baseline-two-files expect=[clean] got=[clean] rc=0 ok
selftest-appendix 2/10 drop-anchor-phrase-body expect=[anchors] got=[anchors] rc=1 ok
selftest-appendix 3/10 weaken-modals-invariants expect=[modals] got=[modals structure] rc=1 ok
selftest-appendix 4/10 append-60-filler-lines expect=[caps] got=[caps structure] rc=1 ok
selftest-appendix 5/10 drop-first-named-appendix-row expect=[appendix] got=[appendix] rc=1 ok
selftest-appendix 6/10 rename-heading expect=[structure xref] got=[modals structure xref] rc=1 ok
selftest-appendix 7/10 alter-seed-line expect=[seed] got=[seed structure] rc=1 ok
selftest-appendix 8/10 truncate-body-last-section expect=[structure] got=[anchors census modals structure] rc=1 ok
selftest-appendix 9/10 drop-last-named-appendix-row expect=[appendix] got=[anchors appendix] rc=1 ok
selftest-appendix 10/10 drop-appendix-only-anchor expect=[anchors] got=[anchors] rc=1 ok
selftest(appendix): 10/10 passed
selftest(combined): 18/18 passed (single-file nested + appendix)
```

(The `tail` also shows the nested single-file tally above those lines: `| selftest: 8/8 passed`.)
So the two-file verdict is reachable: with the artifact's H2 in place both suites read `clean` at the
baseline and every mutation still fires.

### 8.6 Declared semantics of the addition

**D4 — baseline assertion.** A self-test whose baseline case demands *target* cleanliness fails on a
draft that carries its own findings, which is a verdict on the target, not on the verifier. In both
suites the unmutated case therefore reads `expect=[clean] got=[clean]` **when the target is clean**
(the acceptance case: today's `PROTOCOL.md`, §3/§8.5) and `expect=[target-verdict] got=[…]` otherwise,
printing the target's own `FAIL` lines. Attribution is preserved: every mutation must (a) exit 1,
(b) carry all expected ids, and (c) *differ from the unmutated verdict* — a mutation that changes
nothing is a FAIL (this is what caught two real defects while adding the mode: a row-deletion helper
that silently did nothing on an artifact without a heading, and a case whose mutation call was lost).

**D5 — `[appendix-scoped]` MISS annotation.** The brief asks the gate to report a MISS "whose
predicate matched only appendix text today". At run time "today's" appendix text is the artifact, so
the annotation tests each MISS's predicate against `--appendix FILE` (awk dynamic regex; same ERE
dialect as `grep -E`). Measured at the baseline, the set is empty, so the annotation is a no-op today
and exists to make retargeting immediate when a predicate does move:

```console
$ awk -F'\t' 'NR>1 && $1!=""{print $1"\t"$4}' .ufo/waves/round-13/obligation-census-r13.tsv > /tmp/rows.tsv
$ n=0; tot=0; while IFS="$(printf '\t')" read -r id pred; do [ -n "$id" ] || continue; tot=$((tot+1)); \
    if grep -qE -- "$pred" /tmp/appx.txt 2>/dev/null && ! grep -qE -- "$pred" /tmp/body.txt 2>/dev/null; then \
      n=$((n+1)); printf 'appendix-scoped: %s :: %s\n' "$id" "$pred"; fi; done < /tmp/rows.tsv; \
  printf 'census rows=%s appendix-scoped=%s\n' "$tot" "$n"
census rows=169 appendix-scoped=0
```

### 8.7 Revision move (rebase) and the live revision

`PROTOCOL.md` moved while this gate was being extended: the surveyed revision
`e275d4a` = 526 lines / `md5 63de15a3…` (everything in §1–§9 above) gained a 15-line sibling-mint
bullet in `## Lifecycle`, so live `2d19a64` = **541 lines** / `md5 444667c4…`. No check needed a
rebase — nothing is pinned to a line number; the gate resolves the appendix heading, the seed header
and every section slice dynamically, and `caps` counts whatever revision it is given:

```console
$ wc -l -c PROTOCOL.md; md5sum PROTOCOL.md
  541 50603 PROTOCOL.md
444667c4a69f5998f9abb957a68a4343  PROTOCOL.md
$ sh .ufo/waves/round-13/verify-protocol.sh PROTOCOL.md --max-lines 541
INFO census …/obligation-census-r13.tsv rows=169 miss=0 169/169 obligations found; 0 MISSING
INFO anchors …/anchor-phrases.txt phrases=61 missing=0 line-exact-missing=0
INFO modals …/modal-census.tsv sections=9 floor-sum=120 measured-sum=123 regex=MUST|REQUIRED|NEVER|never|must|required|only|may not|must not
INFO caps PROTOCOL.md lines=541/541 body-refs=4/4 (appendix heading at line 502)
INFO structure keys=## Lifecycle|…|## Appendix order=contract
INFO seed …/shonen-seed.txt header-line=415 extracted-lines=8 byte-identical=yes
INFO appendix PROTOCOL.md rows=32/32 body-pointers=17 rows-source=PROTOCOL.md
INFO xref scope=PROTOCOL.md refs=12 headings=9 unresolved=0 allowlist=Closure Conformance Audit Integrator Stale-lane Dispatch L2 Push
verify-protocol: clean checks=8 failed=0
exit=0
$ sh .ufo/waves/round-13/verify-protocol.sh PROTOCOL.md --selftest
selftest target=PROTOCOL.md lines=541 caps=--max-lines 541 --max-body-refs 4 census=…/obligation-census-r13.tsv
selftest 1/8 baseline-unmutated expect=[clean] got=[clean] rc=0 ok
selftest 2/8 drop-anchor-phrase expect=[anchors] got=[anchors] rc=1 ok
selftest 3/8 weaken-modals-invariants expect=[modals] got=[modals] rc=1 ok
selftest 4/8 append-60-filler-lines expect=[caps] got=[caps] rc=1 ok
selftest 5/8 drop-named-appendix-row expect=[appendix] got=[appendix] rc=1 ok
selftest 6/8 rename-heading expect=[structure xref] got=[modals structure xref] rc=1 ok
selftest 7/8 alter-seed-line expect=[seed] got=[seed] rc=1 ok
selftest 8/8 truncate-last-section expect=[structure] got=[anchors appendix modals structure xref] rc=1 ok
selftest: 8/8 passed
exit=0
```

On the live revision the committed floors still hold (per-section 5, 3, 57, 10, 10, 8, 11, 4, 15 vs
floors 2, 3, 57, 10, 10, 8, 11, 4, 15; the +15-line bullet only *adds* three `## Lifecycle` tokens),
the seed header moved 400 → 415, the appendix heading 487 → 502, and the appendix section is still
exactly 40 lines (`awk 'NR>=502' PROTOCOL.md | wc -l` → 40). Floors were deliberately left at the
values derived on the surveyed revision (they are the "today's text" values, per the round's
instruction) — a floor only ever fires on a loss, so added text can never trip one.

---

## 9. Declared deviations from the brief

**D4/D5 — declared with the appendix-mode addition** (both in §8.6): the self-test's baseline case
asserts *clean* when the target is clean and reports the target's own verdict otherwise, with mutation
attribution doing the proving; and the `[appendix-scoped]` MISS annotation tests the predicate against
the appendix artifact, which is the run-time form of "matched only appendix text today".

**D1 — the clean-run flag.** The brief pins `--max-lines` default 470 *and* asks that a clean run
against today's `PROTOCOL.md` exit 0. That revision is 526 lines at the pinned revision and 541 on live
`HEAD` (both above 470), so the bare default reports exactly one `FAIL caps` line. The acceptance is met
the honest way: the clean run is `--max-lines <the measured length>` (§2, §8.7) and the `--selftest`
baseline (§3), while a bare run states the round's target as a finding. Nothing was weakened to hide the
excess — and the target once compacted is 470 or fewer, at which point the bare default is clean too.

**D2 — appendix floor 32, not ≥ 40.** The committed baseline carries **32** data rows
(command + output in §4.4; 34 `|` lines including the header and separator). The appendix *section*
spans exactly 40 lines (`awk 'NR>=487' PROTOCOL.md | wc -l` → 40), which is very likely where the
brief's figure came from; a 40-row floor is unreachable on today's text and would make the gate fail
its own baseline — which the brief itself declares a wrong expected value ("fix them, do not weaken the
check"). The floor is therefore pinned to the measured 32, and the check still fires when a body-named
row is deleted (§3 case 5) or when the digest leaves the file (§5).

**D3 — anchors are matched wrap-normalized.** The brief specifies `grep -F -q`. A re-wrap (which the
compaction necessarily performs) breaks a line-exact `grep -F`, so line-exactness would test the
compaction's line breaks rather than its obligations; §5 shows 6 of 12 line-exact misses in one draft
were pure re-wraps while 6 were real wording changes. The gate keeps fixed-string semantics (no regex,
no case folding) over the wrap-normalized text and reports both counts.

---

## 10. Residual blind spots

What this gate still cannot catch — the residual is the human read of the diff:

1. **An obligation relocated between sections.** Floors are per-section, so a rule moved out of a
   section that was above its floor, into a section that is also above its floor, trips nothing.
2. **A narrowed scope inside a surviving anchor.** Anchors are substrings: "…never re-keys it, so
   last-wins is computed over `(id, entry.round)`" can sit in a sentence whose leading qualifier was
   trimmed, and the anchor still matches.
3. **New obligations.** There is no addition detector: the current draft adds a `Gate standard`
   requirement about `expected.json` digests and no check objects (a section already above its floor
   only ever gets compared for *losses*).
4. **Synonym replacement.** "must never X" rewritten to "is prohibited from X" keeps a section's token
   count if anything else in the section compensates, and an obligation rephrased as prose can hold the
   floor while its modality weakens.
5. **Digest relocation.** The `appendix` check grades the target only. A move of the digest to a sibling
   artifact (`PROTOCOL-APPENDIX.md`, as the current draft does) is reported as an appendix failure by
   construction; grading the sibling would require its own committed expected values and a
   pointer-following rule, and the `§Appendix` pointers in the body would still resolve only inside that
   sibling.
6. **Rewrapped-paragraph boundaries.** Wrap normalization joins wrapped lines of one paragraph with a
   space but treats a blank line as a hard boundary: a phrase whose words are identical but which is
   split by a *new* blank line fails, and (conversely) a phrase cannot be satisfied across two
   paragraphs. Both are deliberate, but neither is a semantic judgement.
7. **Legitimate tightening.** A deliberate, argued reduction of normative tokens (or of an appendix
   row) is indistinguishable from a lost obligation; the gate makes the act visible and the round report
   has to justify re-pinning the expected value.
8. **`xref` name space.** Resolution is first-word matching against `## ` headings plus a committed
   allowlist; a new reference to a non-PROTOCOL section (`§Foo` in a round report) needs an allowlist
   entry, and a heading that shares its first word with the intended target would resolve silently.
9. **Two-file mode: union matching can mask a single-file deletion.** `anchors` accepts a phrase found
   in *either* file. If the same wording survives in the other file, deleting it from one is invisible
   to this check (this is why the appendix suite's case B-2 picks an anchor that is present in the body
   rather than "the first anchor" — the first anchor is already answered by the artifact). The appendix
   check is the compensating half: a body pointer whose row left the artifact still fails.
10. **Two-file mode: the artifact's own prose is scanned too.** Its documentation sentence names the
    template form `(§Appendix, "X")`; the literal placeholder `X` is skipped by name, so a rule whose
    pointer name were exactly `X` would be ignored (implausible, but it is a name-shaped hole).
11. **Two-file mode: the digest heading requirement is a shape check.** `structure` requires an H2 whose
    text contains `Appendix` and `incident digest`; it does not require the exact em-dash form, so a
    reworded tail passes. The pointer resolution and the row floor are what actually bind the artifact.
12. **Two-file mode: nothing forces the body to keep its pointer block.** A body whose `## Appendix`
    section is deleted entirely loses its `body-refs` accounting (the cap then counts the whole file)
    and its pointers, but a body that keeps pointers while dropping the block is not separately graded.
