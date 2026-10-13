# ReviewerCompact — round-11 protocol compaction, mechanical re-verification

Candidate: `/tmp/shokunin-r11/protocol-100.md` · Original: `git show HEAD:PROTOCOL.md` (saved as `/tmp/shokunin-r11/HEAD-PROTOCOL.md`)
**Final candidate identity: 444 lines / 39,264 bytes, sha1 `7ba46f6e12441dbb9155c1d7ea4882dfe93e2535`, mtime 2026-09-28 19:49:31 -03:00.**
⚠ Mid-audit rewrite: my first read captured a 445-line / 39,330-byte draft (rLE row then at :428); the lane finalized during the audit (−1 line, −66 bytes). Every result below was re-executed against the current sha1. Line numbers cited are current-file lines.

---

## 1. SHONEN seed block byte-identity — PASS

Content-based extraction (intro line through the indented block, stopping at first non-indented non-blank line) re-run against both files:

```
$ diff seed-h2.txt seed-c2.txt && echo SEED-DIFF-EMPTY
SEED-DIFF-EMPTY
0afa05a797a17cdd4946eed479d90353ff58a8e5  seed-h2.txt
0afa05a797a17cdd4946eed479d90353ff58a8e5  seed-c2.txt
```

(Independent earlier block-only extraction also diffed empty, sha1 `d4952a1e…` both.)

- `The canonical `SHONEN.md` seed (verbatim` — count 1 (candidate line 329).
- `no other prose, added boxes, or removed boxes` — count 1, single line 324.
- Four boxes intact; `<name>` only substitution; mark sentence present.

## 2. Four executable commands verbatim, single line — 2 PASS / 2 FAIL

| Command | cand single-line | head single-line | Verdict |
|---|---|---|---|
| `git merge-base --is-ancestor <hash> HEAD` | 1 (line 93) | 1 (line 123) | **PASS** |
| `find <repo> -newermt <launch-ts> -type f -not -path '*/.git/*'` | 0 | 0 | **FAIL** — both wrap, at *different* points |
| `git -c user.name=<lane>-shokunin -c user.email=<lane>@shokunin.local commit` | 0 | 1 (line 553) | **FAIL** — candidate splits it |
| `grep -rLE '^#{1,6} *SHONEN' .ufo/reports/round-*/*.md` (appendix row) | 1 (line 427) | 1 (line 100) | **PASS** (pipes correctly escaped `\|` for table context) |

- find-cmd split points: HEAD breaks after `-not -path` (H181 `…-type f -not -path` → H182 `'*/.git/*'`); candidate breaks after `-newermt` (C131 `…(`find <repo> -newermt` → C132 `<launch-ts> -type f -not -path '*/.git/*'`). Per the stated rule (split acceptable ONLY if HEAD splits the same way) → FAIL. Command text itself is complete and verbatim modulo the wrap; rewrap to HEAD's split point or one line.
- lane-commit: candidate line 390 ends `…a main-repo lane commits with `git -c`, continuation on 391 `user.name=<lane>-shokunin -c user.email=<lane>@shokunin.local commit …`. HEAD keeps it on one line (553). Rewrap needed.

## 3. Headings, integrator label, steps 1–4 — PASS

```
$ diff <(grep -vF 'Appendix' hc.txt) hh.txt && echo SEVEN-SHARED-HEADINGS-BYTE-IDENTICAL
SEVEN-SHARED-HEADINGS-BYTE-IDENTICAL        # Lifecycle / Promotion gates / Round-robin rounds /
                                            # Evidence standard / File contract per shokunin repo /
                                            # Invariants / Fleet-2 conventions (adopted)
$ grep -c '^## Appendix' protocol-100.md → 1   # "## Appendix — incident digest (why these rules exist)"
```
- `**Integrator of record.**` at candidate:156.
- Steps 1–4 numbered list intact: candidate 177 / 186 / 198 / 201 (1. Reads every lane report… 2. Lands warranted protocol improvements… 3. Mints a new shonen… 4. Appends one entry to `MANIFEST.json`'s `rounds`…).

## 4. Must-survive anchors — PASS with 2 formatting flags

| Anchor (grep -F) | Result |
|---|---|
| "A status command printing configured values is not evidence of capability." | Present, single line 291 — but candidate continues the sentence with `:` where HEAD ends with `.` |
| "a pin only counts if its expected values are persisted inside the repo" | **FLAG** — line 312 adds bold: `…expected values are **persisted inside the repo**` → byte-exact grep -F fails; words/semantics intact. Downstream cite-checks (kagi `drift-gate.md:14` quotes it) lose their search key |
| "a fingerprint printer with no stored baseline cannot detect drift" | PASS — candidate 314 `fingerprint *printer* with no stored baseline cannot detect drift` is byte-identical to HEAD's own form (HEAD:459 also italicizes `*printer*`; the sweep anchor is a de-formatted paraphrase that never byte-existed in HEAD) |
| "pins verifiable for only 2 of 13 files" | SINGLE, line 439 |
| "a subagent the lane dispatched is still the lane" | SINGLE, line 36 |
| "Commits are cited by hash, never by subject or tag" | SINGLE, line 309 |
| "the counting command that produced it and the commit it was measured against" | SINGLE, line 327 |
| "silence is not a ruling … whichever lane wrote first" | Candidate 351 `silence is not a ruling and must never default scope to whichever lane wrote first` = HEAD's exact wording (HEAD:498–499; sweep anchor omits "scope" — anchor inexact, not a candidate defect) |
| "never amend a cited commit" (paraphrase) | Candidate 94 `Corrections land as new commits, never by amending a cited one — amending or rewriting orphans the record` = HEAD:123–124 wording. PASS |
| Lane identity `<lane>-shokunin` / `<lane>@shokunin.local` / `git config user.name` | ×3 / ×2 / ×1 |
| Report contract ("lands last", hash-citation, ancestor check, landed-by-lane) | `lands last` ×1; C90–96 carries the full contract incl. merge-base check |
| Durability (`/tmp`, `/dev/shm`) | `/dev/shm` ×1; `/tmp` ×2 |
| Step-4 semantics (`Partial entries`, `closed_at`, minimum-content marker distinction) | ×1 / ×4 / ×2 |
| Write-scope ("stay untracked") | ×1 (appendix row) |

**Only split-across-lines occurrence:** the mint bar (item 7) — lines 14–15, markdown continuation wrap, same style HEAD itself uses (H15–18).

## 5. Status vocabulary + entry keys — PASS

```
ok | failed | not-dispatched | in-flight => 1   (line 205)
closed_at => 4      lane_rounds => 1      closure-correction => 4
supersedes => 1     retroactive-closure => 1    protocol_updates => 1
{round, date, type, lanes: {<id>: <status>}, promotions: [{id, from, to}], minted: [id...], notes} => 1  (line 204, exact)
```

## 6. Appendix fact spot-check (10 rows, 36 figures) — PASS with 4 provenance flags

Verified in `.ufo/reports/round-N/*.md` unless noted:

- **Lands last r9**: `85b22e3` ×2 (r10 kengaku+protocol), `f147a27` ×5, `c80c2a1` → **r9/kasegi.md:4** (not in r10 prose; found in the round record).
- **Lands last r10**: `6565e89` ×3, `609ecb6` ×6, `0a30b44` ×3, `17:38:25`, `17:32:47`, `8e32ae0` ×5, `shokunin@local` ×3 (kotoba+protocol), `9a2e9fb` ×2 — all in r10. Sweep split r10:133 "`6565e89` and `609ecb6` swept 21 reports each, `0a30b44` 4" (= the 21/21/4). `025b2e3` / `8ec7a56`: **not in report prose — verified as real commits via `git log`**: `025b2e3 18:47:47 protocol-shokunin`, `8ec7a56 18:57:35 kengaku-shokunin`, `9a2e9fb 18:37:14 kumitate` → the "landed 18:37–18:57" window is exact.
- **Stale-lane actuator**: `tick=13`/`17:32:48`/`17:50:21` ✓ r10:102. **FLAG**: "kumitate 39 min, kake 34 min, protocol 47 min" appears **nowhere in any round report**. Derivable for kumitate (17:57:53→18:37:14) and protocol (17:50:20→18:37:02 ≈ 47) from r10's stale-lane table + git times; kake's 34 min not reconstructable from r10 (kake r10 launch time not listed). The assertion's only home is HEAD's own Evidence standard.
- **D-49 correction**: `43342dd` ×5 (+git 18:41:48).
- **Marker vs report**: `8c300ad` ×5, `7a4c9a0` ×5, `101 B` ×2, kengaku 8→9 at `f147a27`.
- **r5 aggregator marker**: `1395393`/`a50bbda`/`294cbf1` ×1 each.
- **Closure entries**: `16:47` ×2, `17:57` ×19, 66 dispatched/58 terminated ✓ (r10:26 "58 = 66 dispatched − 8 live"). **FLAG**: `[0, 1, 1.5, 9]` not in r10 prose; verified against the cited artifact itself — `git show 0a30b44:MANIFEST.json` = 4 round entries incl. `"round": 1.5`.
- **Round-1**: `15:50:56` ×8, `15:52:38` ×4.
- **Liveness probes**: `18:31` ×2 (r10:139), `18:27:55` ×6 (r10:101), `lane-dead-no-report` 0 ✓ (r10:103,143). **FLAG**: "135 log lines" unverifiable from the round record (watchdog.log has rotated).
- **Drift pins r8**: **FLAG — pointer inaccurate.** "2 of 13" is absent from `.ufo/reports/round-8/` entirely; r8/kagi.md:35 says `drift-pins.sh`: 13/13 pinned host files unchanged. The figure lives in round-6/aggregator.md, round-9/kagi.md, AGGREGATE.md. Suggest Round column 6/9 or pointer fix.

## 7. Mint bar exact — PASS

```
$ tr -s '[:space:]' ' ' < protocol-100.md | grep -oF 'two documented *unplaceable* demand instances (work no existing province could absorb) or an explicit operator directive' | wc -l
1
```
- Present once, in **Lifecycle** (lines 14–15, continuation wrap — HEAD wraps the same bar at H15–18).
- Step 3 (line 198) is **pointer-only**: "minimum evidence per **Lifecycle**"; candidate adds "the mint bar, stated once here; closure step 3 applies it" (15–16), mirroring HEAD H17–18. `unplaceable` occurs exactly once in the whole candidate (HEAD restated the bar in step 3 at H294–295; candidate correctly does not).

## 8. Line/byte budget — PASS

```
444 protocol-100.md        (≤ 450)
38649 HEAD-PROTOCOL.md     39264 protocol-100.md
```
Byte delta: candidate is **+615 bytes** vs HEAD (line count −139; rewrap + appendix table add bytes). vs the superseded 445-line draft: −1 line, −66 bytes.

---

## Verdict

**FAIL (fixable in minutes):** item 2b and 2c — the `find` and lane-`commit` commands must sit on one line (or split exactly as HEAD does); currently neither holds, and both split at points HEAD does not use.

**Fix recommended before landing:** unbold "persisted inside the repo" (line 312) to restore the quoted search key; align the drift-pins row's round/pointer with the actual measurement record (round 6/9, not r8); optionally re-derive or drop "39/34/47 min" and "135 log lines" appendix figures, or pin them to their true source (HEAD Evidence standard / watchdog rotation).

Everything else — seed byte-identity, headings, anchors, vocabulary, JSON shape, mint bar placement, and 32/36 spot-checked figures — verified clean against the current sha1 `7ba46f6e12441dbb9155c1d7ea4882dfe93e2535`.
