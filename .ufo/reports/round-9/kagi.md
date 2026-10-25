# kagi-shokunin — round 9 report

**Axis-move (freshness, lowest pre-move score 2/10):** the corpus's drift
detection could not detect drift. `corpus/drift-pins.sh` v1 printed live
fingerprints and stored nothing — `git show HEAD:corpus/drift-pins.sh | grep -c
baseline` → 0 — and `PROTOCOL.md` §Evidence standard named this repo as the
example ("a fingerprint printer with no stored baseline cannot detect drift:
round-8 audit found kagi's pins verifiable for only 2 of 13 files"). Landed the
missing half: **committed baselines + per-symbol claim pins + a real exit code +
a self-proving selftest.** Commit `e64e81b round-9` in `kagi-shokunin/`,
pushed (`ea77bf0..e64e81b`).

**Same round, second finding (freshness again, on the other gate):** the
round-8 transcript gate was wrong on first contact — SQL `LIKE` treats `_` as
"any single character", so `gsk_` matched `gsk`+any-4-alnum and produced 7 false
HITs; the shipped revision is 888 cells × 32+5 patterns, not the recorded
270 × 25+5. Escaped, corrected, re-baselined, and given a content-free triage
mode. **No secret material is in the transcript DB** (both remaining HITs are
`xai-` provider prose, `key_shaped=0`).

## Evidence (all self-verified by L1; every gate run on the delivered revision)

- **Gate v2** `corpus/drift-pins.sh` (451 lines, sha256 `c138d34c…0feb`):
  `DRIFT_PINS: CLEAN (files=15 symbols=19)` exit 0 · `--selftest`
  `DRIFT_SELFTEST: PASS (13 cases)` exit 0 · `--baseline` with no argument →
  exit 2 · falsified-baseline copy → `DRIFT … sha deadbeef0b7e->2408b0c90b7e`
  exit 1 · malformed `op.env` baseline row → `POLICY …` exit 1 (checked *before*
  any read, so no secret-derived digest can ever print) · patched endpoint copies
  → `GONE` ×2 exit 1 · forced count pin → `count pin changed … refusing to pin`
  exit 2 · hardlinked twin → `LINK … nlink 2` exit 1 · `--pin` on a falsified
  baseline printed three `REPIN` lines (audit path proven live) · cwd-independent
  from `/tmp`.
- **Baselines.** `corpus/drift-baseline.tsv` 15 rows (`$HOME`-relative
  path/mode/lines/sha256); `corpus/drift-symbols.tsv` 19 claim pins
  (`path<TAB>line<TAB>ERE[<TAB>shape]`) — value pins on **both** endpoint
  declarations (`^MODEL_ENDPOINT="http://127\.0\.0\.1:8080/v1"$`,
  `"baseURL": "http://127\.0\.0\.1:8080/v1"`), key-presence pins elsewhere,
  `#10`+`shape` on `op.env`, two `#1` count pins on the published handoff field
  names. 15 files = v1's 13 + 2 cited-but-unpinned files found this round;
  the two `xdg-data` artifacts and package-managed binaries are named
  deliberate exclusions.
- **Hash policy (L2 sentinel, CRIT-driven).** Six private 0600 files are pinned
  by mode+lines only (`op.env`, `config.json`, `~/.agents/AGENTS.md`,
  `handoff-status.json`, both TAC receipt/custody records): a committed sha256 of
  a low-entropy private file is an offline confirmation oracle — sentinel
  demonstrated identifier recovery from a hash with zero host contact. The cost
  is stated in the corpus (content drift blind for those 6), sentinel's own
  refinement ("only `op.env` strictly requires it") is recorded *next to* the
  decision, and the two items I declined (hashes for the 9 non-private files;
  keeping `op.env`'s `#10`) were accepted by sentinel as non-CRIT with the
  documented controls. Policy is enforced by path before any read, never selected
  by the data file.
- **Transcript gate re-verification** (`transcript-scan.sh`, sha256
  `2d60981b…3a23`, 282 lines): `TRANSCRIPT_SCAN: HITS=2 (cells=888 patterns=32+5
  warns=2 schema-absent=0)` exit 1, 5/5 credential tripwires empty;
  `--classify` → `CLASSIFY part.data pattern=xai- rows=1 key_shaped=0 prose=1`
  (same for the one `event.data` row); `--selftest` OK (seeded hit + wal-resident
  hit). Literal `gsk\_` with `ESCAPE '\'` = 0 rows vs the unescaped wildcard's 7;
  run-length after literal `gsk` = 4 chars in all 7 (a Groq key is `gsk_` + ~52).
  Row census unchanged (7 sessions / 39 messages / 55 parts / 238 events), so
  nothing new was written — the false HITs were the gate's own semantics.
- **Independent corroboration.** Scout re-derived all 15 fingerprints and 19
  symbol pins on the host *before* the baseline existed (byte-identical, plus
  35 cited host paths: 0 absent, 0 symlinks). Reviewer adjudicated **168
  citations**: 149 VERIFIED, 6 WRONG, 3 PARTIAL, 5 STALE, 5 UNRESOLVABLE —
  all 6 WRONG + 3 PARTIAL + the stale set fixed this round (see Corrections).
  Scribe confirmed both TSVs carry 0 `op://` refs and 0 `op.env` key names.

## Axis measurement (before → after, recorded in `SCORECARD.md`)

| Axis | Before | After | Basis |
|---|---|---|---|
| freshness | **2** | 7 | printer→gate; 15/19 committed pins; exit 0/1/2; 13-case selftest; detection proven on four falsifications; *not* 9-10: no scheduler, coverage = enumeration, 6 files content-unhashed, count pins value-swap blind |
| operability | 5 | 7 | both repo gates answer with verdicts and prove themselves on scratch state |
| coverage | 5 | 6 | `PROVINCE.md` now lists surfaces + refusals; pin list 13→15; exclusions named |
| calibration | 4 | 6 | first-ever `SCORECARD.md`; `SHONEN.md` regenerated to the protocol mark form with a named non-author verifier per box; "every cited host file" overclaim corrected in 3 places; README index completed (4 lesson files were unindexed) |
| depth | 7 | 7 | `knowledge/drift-gate.md` adds the sourced contract; scope ceiling unchanged |
| adjacency | 8 | 8 | two overlaps documented with owners, still reported not ruled |

Planned next move (lowest post-move axis, coverage 6): enumerate the surfaces
the corpus *describes but does not exercise* — the write-side verbs
(`tac-register` re-run, `cdp-bridge ensure` under a live profile) and the two
`xdg-data` artifacts, each with a command whose output is a verdict.

## Corrections landed this round (not just recorded)

- Overclaim sweep: `SKILL.md:205`/`:304` + `corpus/README.md:33` claimed "every
  cited host file" was pinned while 4 cited files were unpinned; all three
  rewritten to the exact 15-row scope + named exclusions.
- Reviewer WRONGs: `janitor-lifecycle.md` `cmd_request` L128–135 → **L121–135**;
  `op-cli-surface.md` stop's `rm -f` L184 → **L183**;
  `handler-trust-boundary.md` `client.py request()` L20–33 → **L22–38** (×2);
  `cdp-bridge-1password.md` knob lines L23–26 → **L22–26**;
  `config-layering.md` "unsets 18 cloud-key vars" → **20**; PARTIALs
  "~19 unset vars" → **20** (`credential-isolation.md`,
  `janitor-env-contract.md`); scan-surface list → **11 tables**
  (`SKILL.md`, `transcript-hygiene.md`); `config-layering.md` "appended last"
  → "appended at the end (one path-scoped rule follows)"; the 26-agent claim
  annotated with both measurement surfaces.
- Round-8 baseline claim corrected: the 0-HIT/270-cell/25-pattern figure
  describes a narrower revision than the one committed that round; the
  read-design claim (`?immutable=1`) also described a superseded mechanism (the
  shipped gate copies db+wal to `mktemp`, which is what closes the wal blind
  window). New rule recorded: a baseline names the shipped revision's hash +
  pattern/cell counts.

## L2 dispatch (one batch, 10 lanes; route buckets as specified)

`planner` (m_lunamax design attack), `connector` (m_lunamax cross-lane),
`scout`, `executor`, `scribe` (m_flash), `reviewer`, `critic`, `sentinel`,
`labrat`, `distiller` (m_zfl). **Their defects, fixed and attributed:**
`REPIN` audit lines could never fire (old-row map keyed literally, lookups
expanded); `--baseline` with no argument exited 1 instead of the documented 2;
an empty/missing symbol file could be wiped by `--pin`; symbol scans followed
symlinks; the hardlink variant of the symlink case was undetected; the `op.env`
count pin had no dotenv *shape* assertion (added as an opt-in 4th column);
membership was one-directional (now closed both ways + `DUP`); temp files could
linger in the corpus dir (now TMPDIR + `RETURN INT TERM`); `--pin` could absorb
a credential-inventory change (count pins now refuse). Sentinel supplied the
hash policy; distiller supplied the superseded-claim sweep (one row per file);
critic supplied the failure-mode matrix and the resolution-message wording.

## Process defect (self-reported, L2-caught)

The reviewer observed an **in-flight revision of `drift-pins.sh` (18:02–18:10)
that was broken** — bash parse error, exit 2 on every invocation including
`--selftest`. The delivered 451-line revision is green (re-verified after the
last edit; hashes cited above are of the committed bytes). Lesson recorded in
`corpus/lessons/round-9.md` §14: a gate is cited only after it is committed,
exactly as PROTOCOL's evidence-before-commit ordering requires.

## Open items for the operator (unchanged + 2 new; also appended to `.ufo/l0-questions.md`)

1. **Endpoint drift** — `opencode.json` `baseURL` → `127.0.0.1:34113` (8080 is
   a Jitsi videobridge). New friction by design: the gate now value-pins both
   declarations, so the fix red-lines two rows (`GONE`, exit 1) until the citing
   text is re-read. Confirm the friction is wanted.
2. **Control-plane auth** — `OPENCODE_SERVER_PASSWORD` + a `client.py`
   Authorization header (recipe: `control-plane-hardening.md`).
3. **Successful `request`** still needs an operator `op signin`.
4. **Transcript at rest (new)** — 9.2 MB of durable request text at 0600 with no
   purge verb; no material found, so this is a policy decision (audit trail vs
   purge), not an incident.
5. **No purge verb** for the transcript DB; hygiene is monitorable, deletion is
   manual (`stop` + `rm -rf xdg-data`).

## Cross-lane (reported, not absorbed)

- `~/.agents/AGENTS.md` is pinned here and audited by **kotoba** — both
  read-only, no adjudication needed.
- The musketeer `NativeMessagingHosts` 1Password manifest is pinned here while
  **kake** leases that chrome profile machine-wide; kake's round-9 still reports
  ownership unresolved, so this stays contested.
- The round-5 aggregator lesson's `corpus/drift-pins.sh:19` citation is now dead
  (v2 stores `$HOME`-relative paths) — left for the integrator per the
  append-only rule for aggregator-owned lessons.

## Files landed (commit `e64e81b`)

`corpus/drift-pins.sh` (rewritten), `corpus/drift-baseline.tsv`,
`corpus/drift-symbols.tsv`, `corpus/knowledge/drift-gate.md`,
`corpus/transcript-scan.sh` (escape fix + `--classify` + header/baseline),
`corpus/knowledge/transcript-hygiene.md`, `corpus/lessons/round-9.md`,
`SCORECARD.md`, `SHONEN.md`, `PROVINCE.md`, `SKILL.md`, `corpus/README.md`,
`LOG.md`, plus the six citation corrections above.

No vault access; no secret values, `op://` ref paths, account-identifying
values, private-file hashes, or private-file line layouts in any artifact.