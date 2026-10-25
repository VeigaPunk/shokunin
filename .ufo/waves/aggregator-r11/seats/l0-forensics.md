# L0-questions line forensics — aggregator r11 / fleet-ledger-refresh 8, seat `L0Scout`

**Measured at** `2026-09-29T03:26:26Z` – `2026-09-29T03:35:45Z` (`date -u` run beside every state probe below; newest stamp `Tue 29 Sep 2026 03:35:45 AM UTC`).
**Scope:** `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` read-only; all commands run from the main-repo root.
**Method:** content-keyed pickaxe (`git log -S'<literal>'`) instead of line numbers, per the brief. Line labels `L1..L20` are *current* positions and are quoted only for readability; the digest (`len` + `sha1[:10]` of the whole line) is the stable identity.

File shape at measurement: **20 lines = 19 content lines + 1 blank separator (L18)** — HEAD carries 19 (18 content); the working tree gained **one uncommitted line (L20, `kake | round-17`, 725 B)** at ~03:2x–03:35Z while this seat was running, because `.ufo/l0-questions.md` is a **live append target** for the lanes (kama r2 and kake r17 are in flight). Both revisions are covered; the digest is the identity, so a line-number shift is harmless.
```
$ python3 -c "import hashlib;ls=open('.ufo/l0-questions.md',encoding='utf-8').read().split('\n');print(len(ls)-1)"
20
$ git diff --stat -- .ufo/l0-questions.md
 .ufo/l0-questions.md | 1 +
```

Reusable digest command (regenerates every `sha1`/`len` cell below):
```
$ python3 -c "import hashlib;[print(f'L{i} len={len(l)} sha1={hashlib.sha1(l.encode()).hexdigest()[:10]}') for i,l in enumerate(open('.ufo/l0-questions.md',encoding='utf-8').read().split('\n')[:-1],1)]"
```

---

## 1. One row per line

`intro` = commit that *first inserted* the line (pickaxe `-S`); `last-touch` = commit that last rewrote it in place (`git blame`). Content-kiosk digest = `len`/`sha1`. `status` ∈ OPEN | ANSWERED-BY-EVENT | SUPERSEDED (as defined in the brief).

| # | content digest (len / sha1:10 / label) | introducing commit | status | evidence command (verbatim, main-repo root) |
|---|---|---|---|---|
| L1 | 754 / `9dc74c52ac` — kasegi r12: `~/Projects/bounties` stalled mid-interactive-rebase, gitMutationBlocker fail-closed | `e8cd25e` (2026-09-28 18:21:45) | **SUPERSEDED** by L10 — moot-by-event: the subject root no longer exists (no operator ruling on *freeze vs resolve* was ever given; the either/or cannot now be executed) | `git log --format='%h %ad' --date=iso -S'kasegi | round-12' -- .ufo/l0-questions.md` + `ls -d ~/Projects/bounties` |
| L2 | 508 / `88bd12bca2` — protocol r10: mint kama, or record a rejection? | `43342dd` (18:41:48) | **ANSWERED-BY-EVENT** — minted by operator directive; ledger record **does exist** as probation (see §3, this corrects the round premise) | `git log --format='%h %ad' --date=iso -S'kama mint decision' -- .ufo/l0-questions.md` + `python3 -c "import json;d=json.load(open('MANIFEST.json'));print([e for e in d['rounds'] if e.get('type')=='mint'])"` |
| L3 | 750 / `316eb22399` — protocol r10: operator-side driver/template debt (lane_prompt 1-of-5; report_of file-existence; .ufo/state + watchdog.log tracked) | `43342dd` (18:41:48) | **OPEN** — all three sub-items still live at HEAD (see §5.1) | `git log --format='%h' -S'Operator-side driver/template debt' -- .ufo/l0-questions.md` + `sed -n '45,70p' scripts/shokunin-watchdog.sh` |
| L4 | 451 / `e459e50c23` — kagi r10: cmd_refs redaction is a prefix match; export/leading-space/lowercase keys silently dropped | `ade32e4` (19:10:10) | **OPEN** — handler unchanged (see §5.2) | `git log --format='%h' -S'cmd_refs (the-janitor' -- .ufo/l0-questions.md` + `sed -n '228,236p' ~/.local/bin/the-janitor` |
| L5 | 1461 / `6b094e17be` — kake r12: `webzites-keeper.timer` loaded but DISABLED+inactive, never fired | `e333e7c` (19:28:15), **rewritten in place** by `46e9ec3` (20:45:10) | **OPEN** — still `disabled` / `inactive`, `LastTriggerUSec=` empty (see §5.3) | `git log --format='%h %ad' --date=iso -S'webzites-keeper.timer' -- .ufo/l0-questions.md` + `systemctl --user show webzites-keeper.timer -p LastTriggerUSec` |
| L6 | 1147 / `b161624669` — aggregator r6: axis vocabulary split (D-78), MISSION vs AXES `novelty`/`consistency` | `e333e7c` (19:28:15) | **OPEN** — `AXES.md` still has neither name (`grep` exit 1) | `git log --format='%h' -S'Axis vocabulary split' -- .ufo/l0-questions.md` + `grep -n 'novelty\|consistency' AXES.md; echo exit=$?` |
| L7 | 536 / `b1ec7f276b` — kengaku r10: promote the gate convention to a fleet-wide PROTOCOL.md standard? | `46e9ec3` (20:45:10) | **OPEN** — PROTOCOL.md carries no gate-convention standard (only a `--selftest` spelling note at L337) | `git log --format='%h' -S'Promote the gate convention' -- .ufo/l0-questions.md` + `grep -n 'selftest\|gate convention\|exit 0/1/2' PROTOCOL.md` |
| L8 | 832 / `bc5ae54a69` — kumitate r10: adopt `round-gate.mjs` at the driver level? | `46e9ec3` (20:45:10) | **OPEN** — no `round-gate` mention in PROTOCOL.md; the cited defect (`report_of()` file-existence closure) is unchanged (see §5.1) | `git log --format='%h' -S'adopt round-gate.mjs' -- .ufo/l0-questions.md` + `grep -n 'round-gate' PROTOCOL.md; echo exit=$?` |
| L9 | 1086 / `c68221f770` — kumitate r11: fleet adoption of the machine-readable scorecard claim block (`kumitate-proxy-v1`)? | `46e9ec3` (20:45:10) | **OPEN** — contract string confined to kumitate + aggregator wave docs; no second lane adopted it | `git log --format='%h' -S'machine-readable scorecard claim block' -- .ufo/l0-questions.md` + `grep -rl 'kumitate-proxy-v1' --include=*.md --include=*.mjs .` |
| L10 | 1747 / `944494563b` — kasegi r15: `~/Projects/bounties` (PROVINCE root) GONE from the filesystem | `df1b2c6` (21:16:51) | **OPEN** — root still absent; actor UNDETERMINED; no operator response anywhere in-repo | `git log --format='%h' -S'PROVINCE root' -- .ufo/l0-questions.md` + `ls -d ~/Projects/bounties; echo exit=$?` |
| L11 | 914 / `68ca202f35` — kotoba r13: ratify advisory-axis lowest-axis move + D-78 disposal | `df1b2c6` (21:16:51) | **OPEN** — both sub-items unanswered; sub-item 2 is a duplicate of D-78 (L6) | `git log --format='%h' -S'Axis-accounting ratification' -- .ufo/l0-questions.md` + `grep -n 'advisory' AXES.md; echo exit=$?` |
| L12 | 2210 / `ed90fa62b4` — aggregator r9: CORPUS.md amendment set (rule 8 `op://` ban vs 6/6 child corpora, …) | `6415a9b` (22:29:46) | **OPEN** — CORPUS.md rule 8 verbatim intact at L44; no amendment commit | `git log --format='%h' -S'CORPUS.md amendment set' -- .ufo/l0-questions.md` + `git log --oneline -1 -- CORPUS.md; sed -n '43,46p' CORPUS.md` |
| L13 | 1199 / `7b8de4f08e` — kama r1: endpoint-drift repoint decision (3 options a/b/c) | `3069841` (22:52:19) — **NOT 17c1fad** | **OPEN** — every named pin still `:8080` at 03:26:45Z; the live server is still on `:34113` (see §4) | `git log --format='%h' -S'Local model endpoint drift' -- .ufo/l0-questions.md` + `grep -n '8080\|34113' ~/.config/opencode/opencode.json ~/.config/the-janitor/opencode.json` |
| L14 | 580 / `33443496be` — kake r15: corroboration on kasegi r15 (5 danglers, window ≤23:32–23:51:31Z) | `3069841` (22:52:19) | **SUPERSEDED** by L19 (same item, later re-sweep, explicit update; L14's r15 window bound appears only here) | `git log --format='%h' -S'corroboration on kasegi\|r15' -- .ufo/l0-questions.md` — **run with the pipe unescaped in a quoting-preserving shell:** `git log --format='%h' -S"corroboration on kasegi|r15" -- .ufo/l0-questions.md` → `3069841` |
| L15 | 1143 / `9617266d4c` — kama r1: addendum (janitor zero failover; declared 32768 vs served 16384 ctx; omp builtin `llama-cpp-local` default `:8080`) | `3069841` (22:52:19) | **OPEN** — all three sub-items re-verified live at 03:26Z (see §4) | `git log --format='%h' -S'Addendum to the repoint question' -- .ufo/l0-questions.md` + `systemctl --user cat qwen-coder.service \| grep ctx-size` |
| L16 | 1809 / `996fb6a71a` — kasegi r16: SECOND in-round source loss (`open-bug-bounties/.ufo-missions/groknight`, −681f/41d/14MB) | `b5fff81` (22:59:26) | **OPEN** — escalation; no operator response | `git log --format='%h' -S'SECOND in-round source loss' -- .ufo/l0-questions.md` + `ls ~/Projects/origin-work/open-bug-bounties/.ufo-missions \| wc -l` |
| L17 | 939 / `8c0afce4b9` — kama r1: fleet hygiene (`.gitignore` omits `kama-shokunin/`; `.ufo/state/kama.*` untracked) | `cd2d343` (23:20:47) | **OPEN (primary)** — omission still live, and the predicted accident *already happened once* (§4c) / **ANSWERED-BY-EVENT (secondary)** — both state files are now tracked | `git log --format='%h' -S'Fleet hygiene gap' -- .ufo/l0-questions.md` + `git check-ignore -v kama-shokunin; echo exit=$?` |
| L18 | 0 / `da39a3ee5e` — blank separator | `17c1fad` (00:19:02) | **N/A** (structural, not a question) | `git log --format='%h' -S'' -- .ufo/l0-questions.md` (pickaxe on empty string is unstable — use `git show 17c1fad -- .ufo/l0-questions.md`) |
| L19 | 983 / `3255aa642d` — kake r16: corroboration update (5 deletion windows W1–W5; "no new decision requested") | `17c1fad` (00:19:02) | **SUPERSEDED** by L20 (same regime, one window later; both are decision-free corroboration stamps, so "superseded" means *content subsumed*, not *closed*) | `git log --format='%h' -S'corroboration update on the kasegi' -- .ufo/l0-questions.md` → `17c1fad` |
| L20 | 725 / `9bec9c9052` — kake r17: FS-prune regime **W6** — `~/projects` (lowercase twin) vanished between kake r16 sweep ~02:4xZ and r17 baseline 03:20:19Z; "No new decision requested — corroboration for kasegi r15/r16 loss reports; actor still undetermined" | **none — uncommitted working-tree insertion** (no `git log -S` hit; observed `2026-09-29T03:35:33Z`) | **OPEN** (monitor-only — the line explicitly requests no decision; it is a corroboration stamp on L10/L16) | `git diff -- .ufo/l0-questions.md \| grep '^+kake \| round-17'` + `git log --format='%h' -S'FS-prune regime W6' -- .ufo/l0-questions.md` (empty) + `ls -d ~/projects` in the same shell → `No such file or directory` |

### Totals

```
content lines            19   (20 file lines − 1 blank; HEAD has 18 — L20 is the uncommitted kake r17 append)
OPEN                     15   (14 fully open: L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L15,L16,L20 + L17 primary)
  of which monitor-only    2   (L20 and, before its supersession, L19 — corroboration stamps that request no decision)
SUPERSEDED                3   (L1 by L10; L14 by L19; L19 by L20)
ANSWERED-BY-EVENT         1   (L2, by operator directive) + 1 secondary component (L17b)
N/A (structural)          1   (L18 blank separator)
operator-answer text      0   (unchanged from round 9 — see §2)
```

---

## 2. Does any operator answer text exist anywhere in the file's history? — **No. Still 0.**

The file's entire history is **11 commits, 9 of them insertions-only, and exactly one in-place modification**:
```
$ git log --numstat --format='C %h %ad %an' --date=iso -- .ufo/l0-questions.md
C 17c1fad ... Joao Pedro Veiga        2  0  .ufo/l0-questions.md
C cd2d343 ... Joao Pedro Veiga        1  0  .ufo/l0-questions.md
C b5fff81 ... protocol-shokunin       1  0  .ufo/l0-questions.md
C 3069841 ... Joao Pedro Veiga        3  0  .ufo/l0-questions.md
C 6415a9b ... aggregator-shokunin     1  0  .ufo/l0-questions.md
C df1b2c6 ... protocol-shokunin       2  0  .ufo/l0-questions.md
C 46e9ec3 ... Joao Pedro Veiga        4  1  .ufo/l0-questions.md   <-- the only deletion set
C e333e7c ... aggregator-shokunin     2  0  .ufo/l0-questions.md
C ade32e4 ... kagi                     1  0  .ufo/l0-questions.md
C 43342dd ... protocol-shokunin       2  0  .ufo/l0-questions.md
C e8cd25e ... Joao Pedro Veiga        1  0  .ufo/l0-questions.md
C 609ecb6 ... shokunin                0  0  .ufo/l0-questions.md   (file created empty)
```
The single deletion (`46e9ec3`, 2026-09-28 20:45:10) is the **lane-content rewrite of the kake r12 line** (L5): the old text was replaced by the same question with the critic note (`empty LastTriggerUSec`) and the second half (lucario row, cmdProbe handoff) appended — a report-artifact sweep whose message is `reports: kumitate round-11 (+ L0 question on the proxy claim block)`, **not** answer text.

Strict answer-verb scan over the full history (loose scan in the brief returns only question-body prose and `+`-diff duplicates, as in round 9):
```
$ git log -p -- .ufo/l0-questions.md | grep -cE '^\+.*(Answer:|ANSWER:|RULING|Decided by operator)'
0
```
Loose scan, eyeballed (`grep -in 'answer\|decided\|yes\|no \|ruling'`) matched only: (a) the word "Decision:" / "(a)/(b)/(c)" **inside question bodies** (L13, L15), (b) `no ` inside ordinary prose, (c) `+`-prefixed copies of already-present question lines. No line in the file ends with an answer, and no commit *message* in the file's history claims an answer.

**Authorship note (worth reusing):** the human/operator identity `Joao Pedro Veiga <jpveigao10@gmail.com>` authored 5 of the 11 file-touching commits (`e8cd25e`, `46e9ec3`, `3069841`, `cd2d343`, `17c1fad`) — but every one of those is an artefact-sweep commit (message = a lane round report) that only *appends* lane questions. Lane bots commit as `<lane>@shokunin.local` and the integrator as `integrator@shokunin.local`. There is no operator answer commit anywhere in the history, and **no answer channel exists in `.ufo/`** (only `history-pin.json`, `l0-questions.md`, `prompts/`, `reports/`, `state/`, the two watchdog logs, `waves/`):
```
$ ls .ufo/
history-pin.json  l0-questions.md  prompts/  reports/  state/  watchdog-driver.log  watchdog.log  waves/
$ grep -rln 'l0-answer\|ANSWERS.md\|operator answer' --include=*.md .
./.ufo/waves/round-10/scratch/ledger-15-skeleton.md
./.ufo/waves/aggregator-r11/seats/exec-ledger-draft.md
./.ufo/waves/aggregator-r11/seats/l0-forensics.md      # this file (self-match)
./.ufo/reports/round-9/aggregator.md
./SCORECARD.md
./LOG.md
```
Those six hits are ledger/protocol *discussions of the L0 channel* (routing rows, this round's own seat files), not answer text — none of them states a decision on any line above.

---

## 3. kama provenance: were the three kama r1 lines added in `17c1fad`? — **No.**

`17c1fad` appended exactly **2 lines** to the file: the blank separator (L18) and the kake r16 corroboration update (L19). Kama's three r1 lines arrived elsewhere:

| kama r1 line | introducing commit | instant | author |
|---|---|---|---|
| L13 repoint decision | `3069841` (`round-15: kake report …`) | 2026-09-28 22:52:19 −03 | Joao Pedro Veiga (sweep) |
| L15 config-drift addendum | `3069841` | 2026-09-28 22:52:19 −03 | Joao Pedro Veiga (sweep) |
| L17 fleet hygiene | `cd2d343` (`kama round-1: file fleet-hygiene gap …`) | 2026-09-28 23:20:47 −03 | Joao Pedro Veiga |

```
$ git show --stat --format='' 17c1fad -- .ufo/l0-questions.md
 .ufo/l0-questions.md | 2 ++
$ git log --format='%h %ad' --date=iso -S'Local model endpoint drift' -- .ufo/l0-questions.md
3069841 2026-09-28 22:52:19 -0300
$ git log --format='%h %ad' --date=iso -S'Fleet hygiene gap' -- .ufo/l0-questions.md
cd2d343 2026-09-28 23:20:47 -0300
```
(Note: passing two `-S` terms in one invocation ANDs them and returns neither commit here — run the two pickaxes separately.)
**Defect found while tracing this (new, report it):** `b5fff81`'s message claims it carried "five new lane questions (kama r1 x2, kake r15, kasegi r16, aggregator r9)", but its diff carries **1 line** (`+kasegi | round-16`). All five questions did land, but via three different commits (`3069841`, `6415a9b`, `b5fff81`) — the commit message over-claims again, exactly the class `b5fff81` itself was written to correct.

**Ledger correction to the round premise (important for the aggregator row):** the kama mint *is* recorded, as a **probation** mint:
```
$ python3 -c "import json;d=json.load(open('MANIFEST.json'));print([e for e in d['rounds'] if e.get('type')=='mint'])"
[{'round': 11.5, 'date': '2026-09-28', 'type': 'mint', 'minted': [],
  'notes': 'sibling-mint allowance landed in PROTOCOL.md Lifecycle; kama-shokunin minted in
            probation (local model serving & endpoint health — aggregator mint-eligible r4/r6/r7,
            demand instances: kagi r3 + kengaku r4 endpoint-drift 8080->34113). Roster row withheld
            until >=3 verified self-iteration rounds per the new clause; lane wired into watchdog
            (m_flash, axes operability+freshness).'}]
```
`rounds[36]` (round 11.5, type `mint`) was committed by `integrator@shokunin.local` in **`2d19a64` (2026-09-28 22:44:21)**, which simultaneously landed the enabling clause:
```
$ git show 2d19a64 -- PROTOCOL.md | grep -E '^\+' | head -4
+- **Sibling mint (lane-initiated)** — any lane may mint a sibling when it finds a domain demand no
+  existing province owns. Steps, in order: (a) the minting lane scans `MANIFEST.json` + every
...
+  `rounds[].notes` meanwhile, not as a roster row.
```
So `"minted": []` is **the designed shape of a probation mint**, not a missing record. `roster` holding 6 lanes is likewise by declaration ("Roster row withheld until >=3 verified self-iteration rounds"). The kama lane repo confirms the mint: `9cee9fc` seed commit 22:42:49 + `MINT.md` ("**Minted by:** L0 integrator session (operator directive, `2026-09-28`), on aggregator evidence"), `c6199a2` round-1. `17c1fad` added the MISSION.md directive side only (`## Fleet shape (9 L1 lanes)` + kama row L19); it did **not** touch root `MANIFEST.json`:
```
$ git show --stat=200 --format='' 17c1fad | grep MANIFEST.json | grep -v waves   # (empty → root untouched)
$ git log --oneline -4 -- MANIFEST.json    # newest = ae19fca (22:55) then 2d19a64 (22:44)
$ grep -n 'L1 lanes' MISSION.md
7:## Fleet shape (9 L1 lanes)
```

---

## 4. kama r1 mootness test (read-only probes, `date -u` = `Tue 29 Sep 2026 03:26:45 AM UTC`)

**(a) Repoint pins — all still stale, question is LIVE, not moot:**
```
$ grep -n '8080\|34113' ~/.config/opencode/opencode.json ~/.config/the-janitor/opencode.json
~/.config/opencode/opencode.json:158:        "baseURL": "http://localhost:8080/v1"
~/.config/the-janitor/opencode.json:16:        "baseURL": "http://127.0.0.1:8080/v1"
$ grep -n '8080' ~/.config/opencode/agents/janitor.md ~/.local/bin/the-janitor
~/.config/opencode/agents/janitor.md:21:  `http://127.0.0.1:8080/v1`; there is no fallback.
~/.local/bin/the-janitor:19:MODEL_ENDPOINT="http://127.0.0.1:8080/v1"
```
The 8080 holder is still the Jitsi container, and it still passes status-code liveness falsely — both claims of L13 re-verified:
```
$ curl -s -o /dev/null -w 'metrics:%{http_code} ' http://127.0.0.1:8080/metrics; curl -s -o /dev/null -w 'root:%{http_code}\n' http://127.0.0.1:8080/
metrics:200 root:404
$ docker ps --format '{{.Names}} {{.Ports}}' | grep 8080
docker-jitsi-meet-jvb-1 127.0.0.1:8080->8080/tcp, 0.0.0.0:10000->10000/udp, [::]:10000->10000/udp
$ ss -ltnp | grep -E ':8080|:34113'
LISTEN 127.0.0.1:8080  0.0.0.0:*
LISTEN 127.0.0.1:34113  …  users:(("llama-server",pid=1299,fd=16))
```
**(b) Config-drift sub-item — still live:** declared `context: 32768` (`~/.config/the-janitor/opencode.json:22`) vs served `--ctx-size 16384`:
```
$ systemctl --user cat qwen-coder.service | grep -n 'ctx-size'
21:  --no-agent --ctx-size 16384 --cont-batching
$ systemctl --user is-enabled qwen-coder.ctx32k-q4.service
disabled
```
**(c) Hygiene sub-item (L17) — primary OPEN, and the predicted accident already fired once:**
```
$ git check-ignore -v kama-shokunin; echo "exit=$?"
exit=1                         # no .gitignore match; .gitignore lines 1-6 list only the six siblings
$ git log --oneline -2 -- .gitignore       # 78a0ddc "gitignore child shokunin repos" predates the kama mint
$ git show 8afbc8f | grep -E '^(\+|-)[^-+]'
-Subproject commit c6199a2542440db77d69918599e5a378ee116337
```
`17c1fad`'s broad add staged `kama-shokunin` as an embedded gitlink (`Subproject commit c6199a25`), and the operator untracked it 13 s later at `8afbc8f` (00:19:15, "untrack embedded kama-shokunin repo"). The *proposed* fix (append `kama-shokunin/` to `.gitignore`) was **not** applied, so the accident remains reproducible (`git status --short` still shows `?? kama-shokunin/`).
Secondary sub-claim (`.ufo/state/kama.*` untracked) is now **answered-by-event**:
```
$ git ls-files .ufo/state | grep kama
.ufo/state/kama.mission
.ufo/state/kama.round
$ git status --short | grep kama
 M .ufo/state/kama.mission
 M .ufo/state/kama.round
?? .ufo/prompts/kama-round-2.md
?? kama-shokunin/
```
**(d) omp builtin provider sub-item (L15.3) — still live:** the installed binary (mtime Sep 28 15:14) still defaults the builtin local provider to 8080:
```
$ strings ~/.local/bin/omp | grep -A1 -i 'llama-cpp-local' | grep 'baseUrl'
        baseUrl: Bun.env.LLAMA_CPP_BASE_URL || "http://127.0.0.1:8080",
```

---

## 5. Status checks for the remaining OPEN rows (all read-only, same window)

**5.1 Driver debt (L3) / round-gate adoption (L8) — both still live, one item worse:**
```
$ sed -n '45p;97p;103p' scripts/shokunin-watchdog.sh
report_of() { [ -f "$SK/.ufo/reports/round-$2/$1.md" ]; }
      if report_of "$lane" "$n"; then
    elif report_of "$lane" "$n"; then
$ git ls-files .ufo/state | wc -l
18            # was 16 when the question was filed → grew by the kama pair
$ git ls-files .ufo/watchdog.log
.ufo/watchdog.log      # still tracked, as the question states
```
`lane_prompt()` at HEAD still lacks the SHONEN heading rule and the commit-hash citation requirement, and still writes the report path before the commit line it must cite; nothing from `.ufo/reports/round-10/protocol.md`'s corrected template was landed (only path-case and route-fallback edits distinguish it from the r10-era template):
```
$ git log --format='%h' -2 -- scripts/shokunin-watchdog.sh     # 17c1fad, f5d8507 — neither a template fix
$ diff <(git show f5d8507:scripts/shokunin-watchdog.sh | sed -n '/^lane_prompt()/,/^}/p') <(sed -n '/^lane_prompt()/,/^}/p' scripts/shokunin-watchdog.sh)
```
(3 hunks, all `/home/vgpnk/projects` → `/home/vgpnk/Projects` case + one route-map fallback; no contract-item change.)

**5.2 cmd_refs (L4) — unchanged, both halves still defective:**
```
$ sed -n '228,236p' ~/.local/bin/the-janitor
cmd_refs() {
  ...
  awk -F= '/^[A-Z][A-Z0-9_]*=/{v=substr($0,index($0,"=")+1); print $1 "=" (v ~ /^op:\/\// ? v : "<redacted-non-op-value>")}' "$ENV_FILE"
}
```
`/^op:\/\//` is still a **prefix** test on the whole value (a value whose first 5 bytes are the ref scheme is echoed whole), and the key filter `^[A-Z][A-Z0-9_]*=` still silently drops `export FOO=…`, leading-space and lowercase keys.

**5.3 keeper timer (L5) — still inert:**
```
$ systemctl --user is-enabled webzites-keeper.timer; systemctl --user is-active webzites-keeper.timer
disabled
inactive
$ systemctl --user show webzites-keeper.timer -p LastTriggerUSec -p NextElapseUSecRealtime
LastTriggerUSec=
NextElapseUSecRealtime=
```

**5.4 axis vocabulary (L6) / kotoba ratification (L11) / CORPUS rule 8 (L12) / gate standard (L7) / proxy block adoption (L9) / vanished root (L10) / groknight loss (L16):**
```
$ grep -n 'novelty\|consistency' AXES.md; echo exit=$?
exit=1
$ git log --oneline -1 -- CORPUS.md ; sed -n '44p' CORPUS.md
6565e89 aggregator round 3: fleet quality review, corpus audit rules, round record versioned
  vault ref paths (`op://…`) stay out of every corpus, including this one's
$ grep -n 'gate convention\|exit 0/1/2\|round-gate' PROTOCOL.md
337:  spelling is the lane's (`--selftest`, `--self-test`, `run_selftest()`)
$ grep -rl 'kumitate-proxy-v1' --include=*.md --include=*.mjs . | grep -v '^./kumitate-shokunin'
./.ufo/reports/round-8/aggregator.md
./.ufo/reports/round-11/kumitate.md
./.ufo/reports/round-12/kumitate.md
./.ufo/reports/round-12/protocol.md
./.ufo/reports/round-13/kumitate.md
./.ufo/l0-questions.md      # the L9 question line itself (self-reference), not an adoption
```
No *child-lane* SCORECARD/SKILL outside `kumitate-shokunin/` carries the block; the non-kumitate hits are aggregator ledger reports plus L9's own text.
```
$ ls -d ~/Projects/bounties
ls: cannot access '/home/vgpnk/Projects/bounties': No such file or directory
$ ls ~/Projects/origin-work/open-bug-bounties/.ufo-missions | wc -l
2
```

---

## 6. Flags

1. **Operator answers: 0 — unchanged since round 9's classification.** No line carries answer text; no commit in the file's history is an answer; no answer channel file exists. The only in-place edit ever (`46e9ec3`, 2026-09-28 20:45:10) is a lane/content rewrite of the kake r12 line and **predates** round 9's own refresh commit (`6415a9b`, 22:29:46), so it does not change round 9's verdict.
2. **Status changed since round 9: L2 (kama mint) — pending → ANSWERED-BY-EVENT (operator directive).** Executed after round 9's 22:29:46 refresh: `2d19a64` (22:44:21, integrator: PROTOCOL sibling-mint clause + `rounds[36]` probation mint entry), `9cee9fc`/`c6199a2` (kama seed + round-1), `17c1fad` (00:19:02, MISSION.md 9-lane row). **The round-11 brief's premise ("no `rounds[]` entry carries a `minted` record") is stale on both clauses:** a `type:"mint"` entry exists at `rounds[36]` (round 11.5) with `minted: []` *by design* ("probation state is recorded in `rounds[].notes` meanwhile, not as a roster row"), and the roster's 6 lanes are withheld pending ≥3 verified kama rounds. The dormancy/mint tables should key kama as **probation-minted, roster row pending**, not as "unrecorded".
3. **Secondary status change: L17's `.ufo/state/kama.*` half is answered-by-event** (both files are tracked at HEAD); the `.gitignore` omission half is still open — and the accident it predicted already occurred once (`17c1fad` staged `kama-shokunin` as subproject `c6199a25`; reverted 13 s later at `8afbc8f`).
4. **New lines since round 9's refresh:** L16 (`b5fff81`, 22:59:26), L19 (`17c1fad`, 00:19:02), and L20 (kake r17, **uncommitted**, appended during this seat's run); L12 was added by round 9's own refresh (`6415a9b`).
5. **Commit-message over-claim, again:** `b5fff81` claims 5 new questions, carries 1 (`+kasegi | round-16`); all 5 did land via 3 commits. Same class the commit was written to correct — route as a ledger/self-defect row.
6. **D-key queue premise stale:** the max existing key is **D-150** (`.ufo/reports/AGGREGATE.md`, added at `cc6d9d4`, round-9 §14.18 addendum: bounties blast radius beyond kasegi), not D-149. New rows should be proposed relative to D-150.
7. **Ticket-openable defects observed but not in my remit** (read-only seat): `report_of()` (`scripts/shokunin-watchdog.sh:45`) still completes a round on file existence; `.ufo/state` grew 16→18 tracked files, contradicting PROTOCOL.md's untracked claim; `webzites-keeper.timer` still dead while the L5 question sits unanswered.
8. **The L0 file is a live append target, so its HEAD revision lags the working tree.** At `2026-09-29T03:35:33Z` the working tree carried one line HEAD does not (L20, `kake | round-17`, 725 B / `9bec9c9052`) with no introducing commit, and `git status --short` shows `.ufo/l0-questions.md` as ` M` — a lane appended mid-seat, exactly as `lane_prompt()` instructs ("L0 side channel: if you need an operator decision, append …"). Any census of this file must state whether it read HEAD or the working tree; this seat read the working tree and reported both revisions.
9. **L20 re-verified independently (same window):** its claim holds — `ls -d ~/projects` → `No such file or directory` (lowercase twin still absent), and the r15 citation base stays gone (`ls -d ~/Projects/ufofsdbeta` → absent). It is the sixth deletion/mutation instant in the escalating FS-prune regime (W1–W5 ledgered in L19), carries no decision request, and cites kasegi's L10/L16 items as its parents — so the kasegi r15/r16 questions remain the only ones in that cluster needing an operator, and they have had no response (0 answers, §2).

---

## 7. Addendum — the `minted` field is vestigial, and a truthiness filter silently erases the kama mint

Cross-check requested by `MintScout` (whose draft applied the brief's census filter `if x.get('minted')`); re-derived independently at `2026-09-29T03:33:16Z` from the main-repo root:

```
$ python3 -c "import json;r=json.load(open('MANIFEST.json'))['rounds'];print(len(r), sum(1 for e in r if e.get('type')=='mint'), sum(1 for e in r if 'minted' in e), sum(1 for e in r if e.get('minted')), sum(1 for e in r if 'kama' in json.dumps(e)))"
48 1 35 0 1
$ git log --format=%h -- MANIFEST.json | while read c; do git show $c:MANIFEST.json | python3 -c "import sys,json;print(sum(1 for e in json.load(sys.stdin)['rounds'] if e.get('minted')))"; done | sort | uniq -c
     12 0
```
- **48 `rounds[]` entries; exactly 1 is `type:"mint"` (the kama probation row, `rounds[36]`/round 11.5); 35 entries carry a `minted` key; 0 entries have a non-empty `minted` list — and that holds for all 12 historical revisions of `MANIFEST.json`.** So `minted` has never carried a value in this ledger's lifetime: it is a **vestigial field**, and `if x.get('minted')` is a falsy test that returns 0 for a *correct, populated* probation mint. Standardize on `type == "mint"` (+ `notes`), or populate `rounds[36].minted = ["kama"]`; either way the truthiness filter must be retired.
- **The falsy filter propagated into standing cells** (verified read-only, not edited by this seat):
```
$ grep -n 'mints executed' SCORECARD.md .ufo/reports/AGGREGATE.md
SCORECARD.md:178:| M2 | mints executed | 0 | 0 — correct: the bar is met only by kama and the ruling is operator-side | `python3 -c "…[r.get('minted') for r in …['rounds']]"` → 15 × `[]` |
SCORECARD.md:208:… mints executed 0 over 22 `rounds` entries …
.ufo/reports/AGGREGATE.md:940:**M2 unchanged and correct: 0 mints executed** — the bar is met only by kama and the ruling is operator-side.
```
  All three cells are downstream of the same falsy read; SCORECARD.md:178's own repro command prints a list-of-lists (`15 × []`), which reads as "nothing minted" while the ledger's `type:"mint"` row says otherwise. Re-key them to **mints executed = 1 (kama, probation, roster row withheld)** under the new PROTOCOL.md clause.
- **Probation progress, independently derived from the driver log** (cross-check with `DormancyScout`, re-run at `2026-09-29T03:33:50Z`):
```
$ grep -n 'kama' .ufo/watchdog.log
249:2026-09-28T22:44:08-03:00 launch kama round=1 runId=shokunin-r1-kama-r1790646247
274:2026-09-28T23:39:57-03:00 wrap kama round=1 complete; NOT respawning (fleet-wrap)
283:2026-09-28T23:47:29-03:00 wrap kama round=1 complete; NOT respawning (fleet-wrap)
293:2026-09-28T23:55:00-03:00 wrap kama round=1 complete; NOT respawning (fleet-wrap)
311:2026-09-29T00:19:33-03:00 complete kama round=1; respawning
312:2026-09-29T00:19:34-03:00 launch kama round=2 runId=shokunin-r2-kama-r1790651973
$ grep -oE 'wrap kama round=[0-9]+ (complete|in-flight)[^;]*' .ufo/watchdog.log | sort | uniq -c
      3 wrap kama round=1 complete
$ ls .ufo/reports/round-2/kama.md ; cat .ufo/state/kama.round
ls: cannot access '.ufo/reports/round-2/kama.md': No such file or directory
2
```
  The three `wrap … NOT respawning (fleet-wrap)` lines are **re-emissions of one completed round**, not three completions: kama has **1 distinct completed round (r1)** plus r2 in-flight (`kama.round`=2, no report yet at 03:33:50Z). Probation needs ≥3 verified self-iteration rounds ⇒ **2 to go** before the roster row is due. Independent D-key confirmation: `grep -oE '^\| D-[0-9]+' .ufo/reports/AGGREGATE.md | sort -t- -k2 -n | tail -1` → `| D-150`.
- **LOG token-scan hazard for the inherited counting rule** (measured `2026-09-29T03:34:23Z`, same window): the inherited rule is a **case-sensitive** heading match `^#{2,3} Round [0-9]+`, and it returns **0 for 6 of the 7 lane repos**:
```
$ for l in kasegi kengaku kake kumitate kotoba kagi; do printf '%s %s\n' "$l" "$(grep -cE '^#{2,3} Round [0-9]+' $l-shokunin/LOG.md)"; done
kasegi 0
kengaku 0
kake 0
kumitate 0
kotoba 9
kagi 0
$ grep -cE '^#{2,3} Round [0-9]+' kama-shokunin/LOG.md
0
$ grep -nE '^#{1,3} ' kama-shokunin/LOG.md
1:# kama-shokunin — Iteration Log
7:## round 1 — operability axis (measured via freshness)
```
  kama's only round heading is lowercase `## round 1`, so the token scan reads a lane that *did* log its round as zero-activity. Because dormancy is defined as "no LOG.md activity across two consecutive rounds", a lane whose headings are lowercase (or otherwise non-canonical) is a **false-dormant** under the literal scan — the dormancy seat must confirm heading *form* per repo, not just the token count. kama r1's report itself is present and substantive (`.ufo/reports/round-1/kama.md`, 145 lines / 10144 B, committed 23:15), so the mark is ok+defect by report evidence, not by the LOG scan.
  **Root cause, measured per lane (`2026-09-29T03:34:50Z`–`03:35:05Z`):** five lanes have **no round headings at all** — they log rounds as date bullets under the file title (`# <lane>-shokunin — Iteration Log` then `- 2026-09-28 — round N: …`). The heading-only scan therefore cannot see their activity:
```
$ for l in kasegi kengaku kake kumitate kagi kama kotoba; do printf '%-9s bullet=%s heading_ci=%s heading_cs=%s\n' "$l" "$(grep -cE '^- [0-9]{4}-[0-9]{2}-[0-9]{2} — round [0-9]+' $l-shokunin/LOG.md)" "$(grep -ciE '^#{2,3} [Rr]ound [0-9]+' $l-shokunin/LOG.md)" "$(grep -cE '^#{2,3} Round [0-9]+' $l-shokunin/LOG.md)"; done
kasegi    bullet=16 heading_ci=0 heading_cs=0
kengaku   bullet=16 heading_ci=0 heading_cs=0
kake      bullet=16 heading_ci=0 heading_cs=0
kumitate  bullet=17 heading_ci=0 heading_cs=0
kagi      bullet=18 heading_ci=0 heading_cs=0
kama      bullet=1  heading_ci=1 heading_cs=0
kotoba    bullet=8  heading_ci=9 heading_cs=9
$ grep -nE '^#{1,4} ' kasegi-shokunin/LOG.md
1:# kasegi-shokunin — Iteration Log      # only heading in the file
```
  **Correct per-repo matcher for this round's tables:** heading form for `kotoba` (`^#{2,3} Round [0-9]+` → 9) and `kama` (`^#{2,3} [Rr]ound [0-9]+` → 1); date-bullet form `^- [0-9]{4}-[0-9]{2}-[0-9]{2} — round [0-9]+` for `kasegi` 16 / `kengaku` 16 / `kake` 16 / `kumitate` 17 / `kagi` 18. The inherited case-sensitive heading-only rule returns **0 for six of seven lanes** and would manufacture dormancy pairs for lanes that logged 16–18 rounds each.
  **Double-sourced:** `DormancyScout` reproduced this census cell-for-cell at `03:35:36Z` and re-ran its pair-presence test under the per-repo matcher (`03:35:55Z`), obtaining identical absence/`presence` cells, so its verdicts (0/8 dormant literal, 1/8 kengaku reading-B) were unchanged — the hazard affected the *instrument wording*, not the round's dormancy result; its table now carries the per-repo matcher. The falsy-`minted` finding is likewise double-sourced (`MintScout` + this seat).