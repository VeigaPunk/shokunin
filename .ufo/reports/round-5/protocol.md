# Round 5 — protocol lane findings

Inspected every child repo's commits/LOG.md/corpus/ since the round-4 pass
(`adb049c` interval → present). Landed edits in `PROTOCOL.md` + `ROADMAP.md`
only; committed `c5abaac` on the main repo.

## Child-repo state observed

| Repo | Since round-4 inspection | Working tree | Round-4/5 conformance |
|---|---|---|---|
| kasegi | `d6b71c0` + `0bde2e0` round-4 (ledger + evidence-dir census, cited-paths addendum) | clean | Report cites real commits; swept aggregator audit file into its commit explicitly |
| kengaku | `a1af83c` round-4 (authored eval vs live local model; PROVINCE drift finally fixed; audit defects closed) | clean | Full checklist assessment; first authored end-to-end task logged |
| kake | `6b1cd07` round-4 (fire-journal exit-code table) | clean | Round-3 uncommitted-work defect self-healed; report before commit this time |
| kumitate | `efe19da` round-3 landed after round-4 inspection | `corpus/lessons/round-1-aggregator-audit.md` untracked | Steered to round 4 at 16:02; prompt file exists, mission in-flight, no round-4 commit/LOG/report yet |
| kotoba | `397b29c` round-4 (taxonomy 3→5 surfaces) | `corpus/lessons/round-1-aggregator-audit.md` **modified in place** | See finding 2 |
| kagi | `06ef644` round-3 (end-to-end janitor attempt, negative result at auth gate; endpoint drift) | clean | Mission on round 3 since 16:02; report + commit conform |

Driver state (`.ufo/state/*.round`, `watchdog.log`): kake/kasegi/kengaku/
kotoba/protocol on round 5; kumitate round 4; kagi + aggregator still on
round-3-era missions (in-flight since 16:02).

## Gaps found → fixes landed (commit `c5abaac`)

1. **Stale-prompt missions outlive protocol changes.** The aggregator lane
   (mission live since round 1, `aggregator.round` = 3) is editing
   `CORPUS.md` in the main repo right now — authorized by its round-1 prompt
   (`commit ... AGGREGATE.md CORPUS.md`) but now conflicting with the
   round-3 aggregator write-scope exception and the "only integrator writes
   protocol files" invariant. Its added rules cite
   `.ufo/reports/round-2/AGGREGATE.md`, which does not exist — an
   unresolvable pointer. Fix landed: **prompts are snapshots; repo files
   win** — lanes re-read the protocol each steered round; aggregator scope
   line now says "no main-repo files outside its own report"; main-repo
   write scope extended to `CORPUS.md`, `scripts/`, `.ufo/` (the last
   previously unowned — the uncommitted `scripts/shokunin-watchdog.sh`
   v3-edit has no owning lane). The `CORPUS.md` diff itself is left
   uncommitted for the integrator/operator to rule on — the content is real
   (rules match observed round-1/2 audit findings) but the citation defect
   and write-scope conflict need adjudication, not a silent lane commit.
2. **Aggregator audits get edited in place by lane owners.** `kotoba`'s
   `corpus/lessons/round-1-aggregator-audit.md` carries an uncommitted
   in-place rewrite of an aggregator-filed gap (4-line → 5-line AGENTS.md
   correction). The corpus append-only rule (in the uncommitted `CORPUS.md`
   addendum) protected lane files from the aggregator but not the reverse.
   Fix landed: corrections are new entries **in both directions**;
   `round-<N>-aggregator-*.md` files are aggregator-owned.
3. **A silent lane can hold a round open forever.** The aggregator has
   never filed a report (contract added round 4: `aggregator.md`, but
   `reports/round-{3,4}/aggregator*` absent) and no `MANIFEST.json` `rounds`
   entry exists since round 1 because no round ever completed.
   Fix landed: a terminated/respawned mission without a report is recorded
   `failed`; a mission open two+ rounds past its steer is a stale-lane
   review trigger (context predates landed protocol changes).
4. **Round numbers conflated fleet-wide.** `.ufo/state/*.round` diverge
   (kagi 3, kumitate 4, others 5); report dirs and LOG.md assume a shared
   counter. Fix landed: rounds are **per-lane counters**;
   `reports/round-<N>/` collects each lane's Nth round; integrator closes
   round N per lane.
5. **SHONEN checklist assessment still skipped/variable** in round-4
   reports (contract-required since round 1). Fix landed: report minimum
   now names a `SHONEN` heading with one line per box (`[x]`/`[ ]`/`[~]` +
   pointer) — mechanically greppable for the independent reviewer.

## ROADMAP.md

- Watchlist += `kama` — local model serving & endpoint health. Evidence:
  two lanes independently discovered the same endpoint drift
  (`qwen-local`/janitor overlay pins `localhost:8080` = Jitsi videobridge;
  real llama-server Qwen3-Coder-30B on `127.0.0.1:34113`) — kagi round-3
  report + kengaku round-4 report. Not minted: configuration-fault
  discovery is not yet demonstrated recurring demand; watchlisted pending
  a third instance or operator directive.

## Cross-domain / integrator items (open, carried)

- **CDP-9222 / shared burner-chrome lease** — claimed by both kagi and
  kake provinces; flagged in reports since round 2. No ruling recorded.
  Suggested: kake owns the lease (publishing surface); kagi's need is
  read-only status checks.
- **`fleets/registry.json` lane→model routing** (kasegi round-3/4 flag):
  file lives in the bounties tree but describes fleet mechanics —
  kumitate-shaped content reachable via kasegi's surface. Needs a
  PROVINCE ruling; protocol lane cannot write child repos.
- **`qwen-local` endpoint repoint** (8080→34113): operator decision
  pending; blocked auth (`op signin`) also operator-owned.

## SHONEN checklist assessments (spot per repo, not promotion review)

- kagi: box 2 checked by lane (executed-with-negative-result — arguable;
  protocol's "end-to-end task" requires trigger→action→outcome; a
  documented boundary failure does log all three. Reviewer call.)
- kengaku: all four boxes assertable post round-4 (authored eval landed);
  awaits non-author reviewer per gate.
- kotoba: reviewer-passed round-1 revision only; rounds 3–4 deltas
  unreviewed.
- kasegi, kake, kumitate: checklists present; no non-author review yet.
- No repo is promotion-ready on evidence alone — every gate requires the
  independent review, which has not been scheduled. Integrator action.

## Watch items for round 6

- Whether the watchdog respawn fix (uncommitted `scripts/` diff: runId
  tracking) gets committed — currently main-repo scripts have no owning
  lane; new invariant assigns them to the integrator.
- Round-5 prompt files now exist only where a dispatch happened;
  `kumitate-round-4`, `kagi-round-3` still open — per new rule these
  become `failed` candidates if missions die silent.
- `.ufo/` reports uncommitted (only `.gitignore`'d child repos excluded);
  evidence pointers resolve on this host only — acceptable while
  local-first holds, flag if reports ever need to survive a clean.

## Scope compliance

Edited `PROTOCOL.md`/`ROADMAP.md` only; commit `c5abaac`. Not touched:
`MANIFEST.json`, child repos, `CORPUS.md` (aggregator's in-flight edit left
uncommitted), `scripts/`, `.ufo/` state.
