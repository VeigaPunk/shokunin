# AGENTS.md

Fleet root for the **shokunin** (職人) protocol — a swarm of domain-specialist agent lanes that
learn their craft through continual, evidence-driven rounds. This repo is **not an application**:
it holds the protocol contract, operator-side tooling, and the fleet ledger. The nested
`*-shokunin/` directories are independent git repos, gitignored from the fleet root; 17 of them
carry their own `AGENTS.md`. Read `PROTOCOL.md` before changing anything here.

## Setup commands

No install and no build. Requirements: bash, coreutils, `gawk`, `flock`, Python 3 (stdlib only), `jj`.

- Fleet driver (round-robin, respawn-per-round): `scripts/shokunin-watchdog.sh`
- In-session orchestrator (current mode): `scripts/hyaku/inline.sh {queue,dispatch,verify,fail,closure,closed,advance}`
- Source-registry census: `scripts/sources-census.sh {census,validate,overdue,shared,selftest}`
- Root-ledger gate: `python3 .ufo/gates/root-ledgers.py --selftest`
- Fleet status: `scripts/hyaku/status.sh [n]` · Seat gate: `scripts/hyaku/wave-slot.sh {acquire,release,status}`

Never run the watchdog and `inline.sh` together — one driver per fleet root.

## Project layout

- `PROTOCOL.md` — the round contract; `PROTOCOL-APPENDIX.md` is its required pair (incident digest).
- `MISSION.md`, `AXES.md`, `LEARNING.md`, `CORPUS.md` — mission SSOT, six expertise axes, three learning trends, corpus contract.
- `MANIFEST.json` — canonical roster + append-only `rounds[]` history. `ROADMAP.md` is its human mirror.
- `SCORECARD.md`, `LOG.md` — fleet root ledgers (identity-pinned; see `.ufo/gates/root-ledgers.py`).
- `shokunin.conf` — lane roster + substrate launch command. Operator-side.
- `scripts/` — operator-side tooling: watchdog driver, source census, `hyaku/` session orchestrator.
- `templates/round-prompt.md` — prompt template; it must embed the round contract verbatim.
- `.ufo/` — fleet runtime: `reports/round-N/`, `prompts/`, `waves/`, `state/`, `gates/`, `l0-questions.md`.
- `*-shokunin/` — nested lane repos (gitignored). Each owns `SKILL.md`, `PROVINCE.md`, `corpus/`, `LOG.md`, `SCORECARD.md`, `SHONEN.md`.

A lane repo that exists on disk is **not** rostered. Membership comes only from `MANIFEST.json`.

## Evidence rules

This is where agents break the protocol — read it twice.

- Evidence = a resolvable pointer: a repo path, a command plus its output, a commit hash, or an
  external document. A naked assertion is not evidence.
- "Claimed" ≠ "re-executed". Re-run the command at write time and quote what it actually printed.
  Never report a result copied from an earlier session, from a plan, or from a file that exists
  only in a working tree.
- Cite commits by full hash, never by subject or tag. A cited hash must exist and be an ancestor
  of the repo's `HEAD`.
- Append-only files (`LOG.md`, `MANIFEST.json.rounds[]`, `corpus/`) are corrected by **appending**.
  Rewriting a closed entry breaks `.ufo/history-pin.json`.
- Non-author review is mandatory for promotion and for any `unprovable-but-better` verdict. A
  subagent the lane dispatched is still the lane — it does not count as a reviewer.

## Code style

- Bash: `set -u` (add `set -euo pipefail` where safe); quote every expansion; `$(...)` over backticks.
- Exit codes are contract, not convention: `0` clean · `1` failure · `2` usage/env · `3` committed-but-push-failed · `64` usage (`jj-lane.sh`).
- Python: stdlib only; `argparse` with exit `64` for usage errors.
- Markdown protocol files: append-only. Never rewrite a published paragraph — add a dated entry.
- Every new script starts with a header comment stating what it is, its contract, and its exit codes.

## Testing instructions

- Driver gate: `python3 .ufo/gates/root-ledgers.py --selftest`
- Census: `bash scripts/sources-census.sh selftest`
- Lane VCS: `bash scripts/hyaku/jj-lane-selftest.sh` · Seat gate: `bash scripts/hyaku/wave-slot-selftest.sh`
- A gate must exit `0` on clean fixtures and non-zero on its seeded defect fixtures.
- Gates read surfaces they do not own and never mutate them.

## PR & commit conventions

- Default branch is `main`. Branch before committing; never push to `main` directly.
- **Pathspec-limited commits only** — `git commit -- <path>`, never `commit -a` / `add -A`. This fleet
  has concurrent writers and a sweep commits sibling in-flight work.
- Lane commits carry lane identity: `git -c user.name=<id>-shokunin -c user.email=<id>@shokunin.local commit …`.
  Commits made under the operator identity by a lane round are a conformance defect.
- Lane repos are Jujutsu-colocated (`HYAKU_VCS=jj`). Commit through `scripts/hyaku/jj-lane.sh`; its
  `landed <hash>` line is the only citable output.
- `.ufo/state/` and `.ufo/watchdog.log` are driver runtime — never include them in a commit.
- When acting as a **lane**, main-repo writes are limited to `PROTOCOL.md`, `PROTOCOL-APPENDIX.md`,
  `ROADMAP.md`, `SCORECARD.md`, `LOG.md`, `MANIFEST.json` `rounds[]` appends, `.ufo/prompts/*.md`,
  `.ufo/l0-questions.md`, `.ufo/waves/round-N/`, and `.ufo/history-pin.json`. `MISSION.md`, `AXES.md`,
  `CORPUS.md`, `scripts/` and `shokunin.conf` are operator-side — name the correction in the round
  report instead of editing them. This file is operator-facing, not lane scope.

## Security

- Local-first: domain-facing actions are operator-owned. Publishing, vault approval and claim
  submission never happen from a lane.
- Push scope is a hard rule: lanes push only to the fleet remote or their own `<lane>-shokunin`
  remote. Domain source trees outside the fleet root are read-only — never commit, never push.
- Never commit secrets or credentials. The `kagi` lane owns secrets/vault ops; its material stays
  in that lane.
- Operator-gated artifacts (staged payloads, publish candidates, embargoed evidence) are committed
  locally but not pushed until the operator releases the gate.
