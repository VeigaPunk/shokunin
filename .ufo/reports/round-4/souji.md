# souji — round 4 (vault-verify; obsidian claim withdrawn by operator)

Lane HEAD at report time: `48a64d8` (souji-shokunin identity). Single
batched dispatch: 64 seats on **devin/deepseek-v4-1-flash-max** (operator
devin test); 63/64 completed in ~72 min.

## Amendment (recorded, not hidden)

The round opened with claim O1 "Obsidian-CLI integration". Mid-round the
operator directed: "forget the obsidian integration for now; i'll look
into it later on how to use properly." O1 was **withdrawn by the
operator** and replaced by O1' — the Obsidian-free receipt machinery
(ledger-backed moved-to-obsidian verification). The goal's completion
criterion (obsidian capability row) is correspondingly waived by the
operator; this report and LOG carry the waiver.

## Work performed

- **CLI recon (8 seats)**: decisive finding — the official CLI has **no
  invocable entry point on this host**. It is the app as a second-instance
  socket client (`$XDG_RUNTIME_DIR/.obsidian-cli.sock`, JSON-line protocol,
  73 handlers decoded from the asar); registration is structurally refused
  under the pacman packaging (argv0 gate requires basename containing
  "obsidian"; the wrapper's argv0 is `electron`); bounded live socket
  probes returned 0 bytes. `obsidian-cli-inspector` is third-party
  (stats; size:mtime, not content hashes). Banked for the operator:
  `.ufo/scopes/souji-mint-20261018/obsidian-cli-probe.md` (round-4 section).
- **Tournament**: 7 impls (impl-19's seat failed), 8 fixture authors, 16
  runners, 8 reviewers, 8 adversarial testers, 8 judges. Majority judges
  (57/58/59/61/63) converged on **impl-20** with sha-pinned rationales:
  selftest 35/35, refuses self-referential ledger rows (a false-SAFE class
  rivals accepted). Dissent (60/62/64: NO-CLEAN-CANDIDATE over fixture
  rot) recorded, not suppressed.
- **Parent verification**: 4/4 decisive battery (match → SAFE/
  moved-to-obsidian; vault tamper, source tamper, vault absent → NOT-SAFE)
  + real-vault live probe against
  `/home/vgpnk/Documents/shokoknowledge/Home.md` with a temp ledger →
  VERIFIED (`cli=unavailable` flag honest). Live ledger untouched
  (header-only). Winner installed byte-identical: `tools/souji-vault-verify.sh`
  (sha256 d312263a…).

## Landed changes

- `tools/souji-vault-verify.sh` + 7 impl variants + `tests/vault/`
  fixtures + `tests/results/v*.json` + `census/round-4/` — commit `48a64d8`.
- `corpus/lessons/round-4.md`; LOG.md r4 entry; SCORECARD operability 8 +
  ledger-verify capability row.
- Fleet: `.ufo/scopes/souji-mint-20261018/obsidian-cli-probe.md` round-4
  findings addendum (same commit as this report).

## Before → after measurements

- O1' operability: before — no vault-verification capability → after —
  `bash tools/souji-vault-verify.sh --selftest; echo $?` → 0 (35 checks);
  parent battery 4/4; live vault probe VERIFIED. Measured against `48a64d8`.
- C1 calibration: before — no judge-dissent adjudication practice →
  after — 4/8 judge dissent resolved by parent re-derivation (battery +
  live probe), majority verdict adopted only after independent
  confirmation; dissent preserved in the record.

## SHONEN

- [~] SKILL.md decision tables — receipt taxonomy extended by the r4 battery findings (self-referential rows, cli-unavailable flag).
- [~] End-to-end domain task — real-vault verification executed and logged.
- [~] Executable without oral context — 63 zero-context seats built the tournament from the template.
- [~] No cross-domain bleed — vault read-only throughout; obsidian deferred to the operator; PROVINCE.md unchanged.
