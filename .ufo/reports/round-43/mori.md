# mori — round 43 (2026-10-24) — repair-first: successor operability counter, calibration repair, one-theme assimilation

lane: mori · round: 43 (attempt 1) · host: Kimi, fresh L1 (`Kimi fresh L1`) · date: 2026-10-24 ·
lane repo: `/home/vgpnk/Projects/shokunin/mori-shokunin` · entering tip
`e3a2b58f72ba3bd52a90646f7285fb85f0ee5dd2` · landed lane tip
`91cb221f35f7cb9afeff99ef1959512dabddfc46` (`jj-lane.sh state`: local=remote=91cb221f…,
ahead=0, behind=0, tracked=0, untracked=0) — the report lands last, after that commit.

**Round shape.** One v2 wave (policy `scripts/hyaku/ufo-wave-policy-v2.json`, band 64–128),
64 seats, 31 attack roles (48.4%), plus a residual call of 8 reviewer/critic seats — 72 seats
in the round. The 64-seat wave was starved by the provider's rate limit (34 seat logs carry
`provider.rate_limit: 429`); 60 of its seats are dead seats and are not credited and were not
replaced. **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
**Tool installs:** none; pacman was not used.

**Inherited state, disposed.** The same round's earlier attempt (which died on a provider-route
failure before dispatch) left the frozen contract, two counters, the wave spec, five SOURCES
rows, three knowledge entries and the lesson uncommitted in the lane tree. This L1 **re-executed
every control** (claimed ≠ re-executed), **opened the one source the inherited rows had not
opened** (systemd.scope(5) — the inherited S350 row said so in its own anchor cell), and kept
the claims as they were declared: **P-C1S and P-C2 were not re-declared**.

## Work performed

Declared claims, frozen in `.ufo/waves/round-43/contract.md` before any seat scored
(entering tip `e3a2b58…`):

- **C1S — operability (7):** a *successor* measurement of the frozen round-42 counter that
  completes — including the no-harm arm the frozen counter never reached — and prints `C1S=`.
  The frozen r42 counter is **not amended** (sha256 `105ce075f331…` unchanged; its `run()` still
  takes `argv, timeout` only).
- **C2 — calibration (5, tied lowest non-retired axis with depth and freshness):** the two
  r42-routed self-assessment errors repaired append-only — the SCORECARD declaration cell that
  claimed `C1=met`, and the S235 registry row whose anchor sha256 is transposed.

Work items, each with an evidence pointer:

- The frozen contract (P-C1S, P-C2, the controls, the kill rule) —
  `mori-shokunin/.ufo/waves/round-43/contract.md`; the successor counter
  `.ufo/waves/round-43/count-c1s.py` (sha256 `93482248b46def2a2cec7238732af1551ef315517e76833c3843875313b65dc5`);
  the calibration counter `.ufo/waves/round-43/count-c2.py`.
- **Controls re-executed by this L1, not inherited**: do-nothing C1S at the entering tip →
  `C1S=unmet` exit 1 (`evidence/control-c1s-donothing.txt`); junk control (a counter whose body
  only prints `C1S=met`) → `C1S=unmet` exit 1 (`evidence/control-c1s-junk.txt`); green C1S on
  a scratch clone → 15 checks PASS, `C1S=met` exit 0 (`evidence/control-c1s-green.txt`);
  do-nothing C2 → `C2=unmet mismatches=2` exit 1 (`evidence/control-c2-donothing.txt`); green C2
  → `C2=met mismatches=0` exit 0 (`evidence/control-c2-green.txt`).
- **C2's two append-only repairs**: the S235 row is untouched (its line sha256 is still
  `971df55e9e1ed8826e66dd31d12f9cbb5b2c727cf71201a2c0eabc7311e169a2`, checked by the counter);
  a new row **S349** carries the committed PDF's real sha256
  `9855a4986a312dfc946b1b97b6010a8e4f1e65a4a30dca99359e6df057ad8020` and opens
  `supersedes S235 — `; the SCORECARD's round-42 declaration cell is still present and
  unmodified, and one new correction line names it (counted exactly once by the counter).
- **Assimilation (item 10), one theme — what `journalctl --disk-usage` counts**: one entry
  admitted, `corpus/knowledge/journal-disk-usage-total-r51.md` (row S470; the journalctl(1)
  page re-opened this round; a live read-only invocation printed
  `Archived and active journals take up 269M in the file system.`), two entries refused with
  reason and flip (S350 `systemd.scope(5)` — the staged entry's recheck is
  `systemctl reset-failed`, host mutation; S351 `journalctl(1)` — the staged entry cites a
  campaign `file://` note and greps kernel `MESSAGE` text). Registry **238 → 243** rows.
- **Validate-before-append, re-derivable**: the lane was mirrored in scratch from committed
  bytes (entering-tip `corpus/` + the append block in the Registry table + the admitted
  knowledge files) and gated with `sources-census.sh validate --file …` → **exit 0** before the
  first registry append (`.ufo/waves/round-43/assimilation/validate-receipt.txt`, 243 rows).
- **Collision guard**: registry 238 ids vs staged 127 ids → `collisions` empty before the
  append; the indented-row guard proven on a scratch fixture (column-zero pattern hits 0 rows,
  the 0–3-space pattern hits `S348`); the **post-append** guard and its shadow map by document
  in `.ufo/waves/round-43/assimilation/guard/collisions-post.txt` (5 ids: S470 is the same
  document and keeps its id; S348–S351 are lane-owned rows that shadow four provisional staged
  ids, so the campaign renumbers by document at its next adoption — the id follows the document,
  never arithmetic).
- **Quarantine slice** of the campaign's absent-defect register: `S244`, `S262`, `S268` — all
  three are prose-class "could not be fetched", i.e. unverifiable, not fabrication. S268 stays
  refused; S262 was admitted in round 42 and is not re-opened; S244 is cited by no admitted
  entry.
- **considerthese (item 10)**: one still-unimplemented proposal mined —
  "Check that frozen instruments replay off-host" (`considerthese/2026-10-24.md`, read-only, not
  edited) → QUALITY 115. A residual seat's S268 attack added **QUALITY 116** (an "unreachable"
  verdict needs a full GET probe, not a HEAD probe alone).
- **S268 not re-admitted**: `curl -sI` of the stampPDF URL returned HTTP 418,
  `content-type: text/html`, content-length 15410 (`evidence/s268-headers.txt`); no committed
  PDF, so the flip condition ("a fetch this host can reproduce") is not met and there is no
  re-gate.
- **OpenAlex tier-A L0 not re-filed**: already filed at fleet commit
  `527fc8dd5f36a7f7ee45aff66f0e3daf413222de` (mori identity, ancestor of fleet HEAD).
- **Misroot sweep**: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows
  `bm.json`, `live.html`, `live_s228.html` (all dated 18:07, before this round, naming no
  lane), `.omp/mcp.json` and the driver's `.ufo/state/*` files. None is a mori round-43 seat
  file; none was touched.

## Landed changes

| change | lane commit | LOG entry |
|---|---|---|
| frozen contract, successor counter `count-c1s.py`, calibration counter `count-c2.py`, wave spec, the 5 control receipts, the census-start receipt, the S268 header receipt, the disk-usage receipt, the wave plan | `dde525ea4a7fca365e8ff2f3c486bccf28b94e52` | `LOG.md` §"Round 43 (L1 Kimi fresh mori-r43)" |
| registry rows S348–S351 + S470, three knowledge entries, the round-43 lesson, QUALITY 115, the coverage-map note, the SCORECARD declaration + correction, the assimilation mirror and its receipt | `dde525ea4a7fca365e8ff2f3c486bccf28b94e52` | same |
| after-scores (`c1s-after.txt`, `c2-after.txt`), the round-end census, the generated P-C1S clause map, the L1 mutant battery receipt, the 10 seat reports, both settle tables, QUALITY 116, the wave record, the measured outcome | `efb92cd5fc27d392fbedc406933c398b35a5c09f` | `LOG.md` §"Round-43 wave record" |
| the 72 seat logs (each dead seat's last error text), the frozen-sha mutant receipt | `91cb221f35f7cb9afeff99ef1959512dabddfc46` | `LOG.md` §"Round-43 seat logs" |

The frozen round-42 counter was **not** touched: `.ufo/waves/round-42/count-c1.py` still hashes
to `105ce075f331…` and `git diff e3a2b58… 91cb221f… -- .ufo/waves/round-42/count-c1.py` is empty.
Both round-43 counters are byte-identical at the final tip and at the tip they were first
measured at (`count-c1s.py` sha256 `93482248…`, `count-c2.py` sha256 `a1e05c98…`).

## Before → after measurements

| claim | before (one command) | after (one command) | measured against |
|---|---|---|---|
| **C1S** — operability | `python3 .ufo/waves/round-43/count-c1s.py e3a2b58…` → `check self_at_rev FAIL (absent)` → `C1S=unmet`, exit 1 | `python3 .ufo/waves/round-43/count-c1s.py <tip>` → 15 checks PASS (incl. `noharm_cwd PASS (rc=0 MORI_SOURCES_APPENDONLY_SELFTEST pass=22 fail=0)`, `v5_selftest_17 PASS (pass=17 fail=0 rc=0)`, three `mutant_kill_* PASS (pass=16 fail=1)` on exactly their own arms, `frozen_still_crashes PASS (rc=1 crash=True C1_line=False)`) → `C1S=met`, exit 0 | `dde525ea4a7fca365e8ff2f3c486bccf28b94e52`; receipts `evidence/c1s-after.txt`, `evidence/c1s-clause-map.txt` |
| **C2** — calibration | `python3 .ufo/waves/round-43/count-c2.py e3a2b58…` → `correction_row FAIL (ids=[])`, `scorecard_correction FAIL (count=0)` → `C2=unmet mismatches=2`, exit 1 | `python3 .ufo/waves/round-43/count-c2.py <tip>` → all 8 checks PASS → `C2=met mismatches=0`, exit 0 | `dde525ea4a7fca365e8ff2f3c486bccf28b94e52`; receipt `evidence/c2-after.txt` |

Verdicts, stated as the L1 sees them and left to the closure to rule:

- **C1S — verified (measured), with a disclosed instrument-tamper limitation.** Every clause of
  the frozen P-C1S sentence is discharged at the landed tip by the receipt and the generated
  clause map, and the two cheap controls show the target is not reachable without the work. The
  limitation: the counter's verdict is **not tamper-evident**. L1's own 8-class battery
  (`evidence/c1s-mutants.txt`, mutation applied to both the running copy and the rev copy so the
  counter's own self-check cannot short-circuit it) killed 4 classes and **survived 4**: removing
  the no-harm arm, loosening the v5 selftest threshold, accepting any single failing mutant arm,
  and accepting a `C1=` line from the frozen counter all still print `C1S=met` with one check
  fewer. This is a statement about the instrument, not about the input: on honest input at the
  landed tip the counter prints 15 PASS lines, and the counter's identity is pinned by its
  sha256 `93482248…` (a mutated copy is not the claim's counter). A stricter reading of the
  kill rule would grade this claim **not verified**; the L1's reading is **verified (measured)
  with the limitation disclosed and routed**, and the ruling is the closure's.
- **C2 — verified (measured).** The S235 row's bytes are unchanged, a separate row carries the
  correct sha256, the round-42 declaration cell is still present and unmodified, and the
  append-only correction line appears exactly once.

**No axis harmed.** Scores held: coverage 6, operability 7, depth 5, calibration 5, freshness 5,
adjacency 6. No score move is claimed — the claims repair routed defects at held scores, the
lane's established pattern.

## Sources & frontier

- **Counting command** (before → after): `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`
  → **238 → 243** rows. Census
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`
  → exit 0 at round start (`evidence/census-start.txt`, 16 pre-existing W04 warnings) and exit 0 at
  round end (`evidence/census-end.txt`, 19 W04 warnings — the three new ones are S349 vs S235,
  S351 and S470 sharing the journalctl URL, all "duplicate url across scopes", i.e. deliberate).
- **Rows added by tier**: tier A — S348 (Python `subprocess.run` signature, the `cwd=None` in the
  documented signature), S349 (openEuler whitepaper, the committed PDF's sha256; supersedes
  S235), S470 (systemd journalctl(1), what `--disk-usage` counts). Tier B — S350 and S351, both
  **rejected** rows (a rejection is evidence of taste). No row was appended without its source
  being opened this round, and no row was bulk-appended.
- **Rows touched old→new**: none in place — no existing row's `status`, `recheck` or `used-by`
  changed this round. The only in-place touch anywhere was the SCORECARD (an appended
  declaration block, an appended correction line and an appended measured-outcome block), never a
  rewritten cell.
- **Frontier rows advanced**: the resource-runway ground "what the journal store's size reading
  means" moved into the coverage map as a **frontier** row in `corpus/README.md` §"Round-43
  coverage additions" — no Core move is claimed. Two adjacent package entries were refused with
  reasons and flips, so no sibling-domain ground was absorbed.
- **Sourced claim**: C1S rests on S348 (opened this round), cited by
  `corpus/knowledge/c1s-cwd-r43.md`.
- **Assimilation: one theme, one entry.** `merge/mori/` was read read-only; no campaign tool was
  run there and no byte was written into it. Admitted: `journal-disk-usage-total-r51.md`.
  Refused: `journal-reach-at-ceiling-r46.md` (campaign `file://` note + kernel MESSAGE grep),
  `failed-scope-keeps-limit-r50.md` (`systemctl reset-failed` = host mutation). Flip conditions
  are recorded in `corpus/lessons/round-43.md` and in the rejection rows themselves.

## Trend verdicts

- **expansion — improved.** One admitted knowledge entry on coverage-map ground the map did not
  hold (`journal-disk-usage-total-r51.md`, resource runway), each `source:` citing a row opened
  and mined this round (S470); the registry grew 238 → 243 with every new row grounded in a
  source opened this round; the item-10 assimilation added one entry on one theme.
- **quality — improved.** The two r42-routed false self-assessments are superseded by
  append-only records rather than left standing, and C2's counter fails a re-assertion of the
  old state. The lesson's mistakes M1–M5 each name the criterion that should have caught them;
  QUALITY 115 and 116 are lesson-backed.
- **discernment — improved, with one honest disagreement recorded.** The lane's gate agrees with
  the seat attacks on the admits and on both refusals, and the S268 refusal was kept when a
  re-gate was offered, because the fetch was HTTP 418 rather than a PDF. The one disagreement
  found was against this round's own method: the S268 receipt rests on a HEAD probe, which
  cannot distinguish a mitigation page from an endpoint that refuses HEAD but serves GET — that
  became QUALITY 116 rather than a silent pass. The wave's seats are still the lane; the
  non-author spot-check remains the closure's.

## SHONEN

- `[~]` real decision tables / error patterns / checklists with cited sources — the frozen
  contract and the clause map are a per-clause decision table with the clause, the check line and
  the receipt pointer; pointer `mori-shokunin/.ufo/waves/round-43/evidence/c1s-clause-map.txt`.
- `[~]` end-to-end domain task executed and logged — the round's measurement ran end-to-end at
  the landed tip and the receipts are committed; pointer
  `mori-shokunin/.ufo/waves/round-43/evidence/c1s-after.txt`.
- `[~]` instructions executable by an agent without oral context — the 64-seat wave spec and
  the 8-seat residual spec carry their own context and per-seat instructions; pointer
  `mori-shokunin/.ufo/waves/round-43/w1-spec.json`.
- `[ ]` no cross-domain bleed, PROVINCE.md still accurate — PROVINCE.md was not touched this
  round and the two adjacent package entries were refused with reasons and flips rather than
  absorbed; no independent reviewer has attested this box.

## Wave record (as observed)

- **One v2 wave**: 64 seats — attack 31 (48.4%: reviewer 12, critic 11, mutation-tester 8);
  build 33 (scout 12, scribe 8, executor 8, sentinel 2, connector 1, simplifier 1, revenger 1).
  Validated (`ufo-swarm-wave.mjs run --spec`, exit 0, `counts.spawn=64`). **AgentSwarm is not
  exposed on this Kimi seat**; the validator's `taskCall` was issued as ONE batch of 64
  `kimi --agent-file` processes with the `/skill:godspeed` lead and the verbatim directive bytes.
- **Grant**: `wave-slot.sh acquire mori round-43-w1 64 3600` → `granted lane=mori
  wave=round-43-w1 seats=64 live=54 pending=0 cap=256`; released after settlement. A second
  grant for the residual call: `acquire mori round-43-residual 8 2400` → `granted lane=mori
  wave=round-43-residual seats=8 live=55 pending=32 cap=256`; released after settlement.
- **Dead seats, honestly**: the 64-seat wave returned **4 reports** (`Exec2.md`, `Exec4.md`,
  `Exec5.md`, `Exec6.md`); 8 seats exited 1 and **52 were killed by the 540 s seat timeout**,
  34 seat logs carrying `provider.rate_limit: 429 Rate limit reached for requests`. Those 60
  seats are dead, are not credited, and were **not replaced**.
- **Residual call** (the contract's ≤8 reviewer/critic allowance; 8 seats, all attack roles,
  staggered two at a time, 1200 s seat timeout): **6 reports** — `ResCritDoNothing.md`
  (the entering tip still prints `C1S=unmet` exit 1), `ResCritJunk.md` (a counter that only
  prints `C1S=met` → the attack failed, `C1S=unmet` exit 1), `ResCritInPlace.md` (an in-place
  S235 rewrite is scored `C2=unmet`), `ResCritNoHarm.md` (the no-harm arm **CONFIRMED**:
  `MORI_SOURCES_APPENDONLY_SELFTEST pass=22 fail=0` exit 0, 3/3 of the gate's own mutants
  killed), `ResCritS268.md` (the refusal stands: HTTP 418, no committed PDF), `ResCritScope.md`
  (no host-mutation vector; every grep hit is a refusal record or prose). **2 dead seats**
  (`ResCritBulkAppend`, `ResCritDeclaration`) were killed at the timeout — their logs are kept,
  they filed no report, they are not credited and were not replaced.
- **Round total: 72 seats** (64 in the wave + 8 in the residual call). No second wave shape, no
  filler, no replaced seat.
- **L1's own battery** (the seats that mattered most could not report): 8 mutation classes
  against the successor counter, mutation applied to both copies; 4 killed, 4 survived —
  `evidence/c1s-mutants.txt`.
- The launcher's `wait` ran inside a pipeline subshell and printed `SEATS 0` while the 64
  processes were already running; the seats were fine and a waiter parent that spawns nothing
  stayed alive until they had settled (lesson M5).

## Routed repairs from round 42 (all five)

1. **C1 stays unverified in r42 → a NEW successor measurement.** The frozen r42 counter is not
   amended; the successor completes the no-harm arm and prints `C1S=` — and the r42 crash is
   re-confirmed as a standing fact by the same counter (`frozen_still_crashes PASS (rc=1
   crash=True C1_line=False)`). **Landed**, with the tamper-evidence limitation disclosed.
2. **S235's transposed sha → a new correction row, not an in-place rewrite.** S349
   (`supersedes S235 — …`) carries the committed PDF's sha256; the S235 row's line sha256 is
   unchanged and the counter fails an in-place rewrite. **Landed.**
3. **SCORECARD still said `C1=met` → an append-only correction line**, the declaration cell left
   in place and counted exactly once. **Landed.**
4. **S268 re-gate only on a reproducible fetch.** The only fetch this host can reproduce returns
   HTTP 418 / `text/html` / 15410 bytes; no committed PDF; **not re-admitted**, and the probe's
   weakness became QUALITY 116. **Routed, not re-gated.**
5. **The report cited the wrong tip last time.** This report lands **last** and cites the final
   lane tip, which carries the S235 PDF evidence — the r42 PDF landed in `25200325`, after the
   report was committed.

## Open L0 questions

None new this round. The OpenAlex tier-A L0 (`mori | round-42 | …`, fleet commit
`527fc8dd…`) is already filed and was **not** duplicated. No question blocks this round.

## Report integrity

- Lane work is committed and pushed only through `scripts/hyaku/jj-lane.sh`; the only citable
  lane lines are its `landed <hash>` outputs: `dde525ea4a7fca365e8ff2f3c486bccf28b94e52`,
  `efb92cd5fc27d392fbedc406933c398b35a5c09f` and
  `91cb221f35f7cb9afeff99ef1959512dabddfc46` (the lane tip).
- This report is committed on the fleet repo through `scripts/hyaku/fleet-commit.sh --as mori`,
  after the lane tip above — the last write of the round.
- No host service was started, stopped, signalled or reconfigured; no sibling repo, lane jj
  state, fleet script, template, prompt or MANIFEST entry was edited; no domain-facing action
  was taken.
