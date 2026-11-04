# kaidoku — round 87 (attempt 1)

Lane HEAD after the round: `4136ac0cc6640829655c637ad016db530450b822` (`git -C kaidoku-shokunin ls-remote origin refs/heads/main` prints it). Base `99f8b6a8979978fe02dc3c8f674ce4fdee3ab44b`.

## Work performed

Declared claims (one): **R87-C1 — coverage, capability acquisition**: the PROVINCE Frontier class "anti-UPX stub whose magic … is altered" moves to Core. A UPX-packed ELF whose `UPX!` words are overwritten still runs, but `upx -t/-l/-d` answer `NotPackedException`. A new tool restores the magic from the packer's own structures, and the pinned packer and REA then recover the original. One claim only: rounds 85–86 were rejected on claims about the lane's own records, and the round-86 spot-check routed SHONEN box 2 (no end-to-end domain task) and V86-1 (unowned axis).

- Declaration with counter, do-nothing and cheap-rule controls, and census before: `f0ebf61161d08279dca98841461330ad442d3023` (`plans/round-87-claims.md`, `.ufo/waves/round-87/claims.json`, counter `tools/round-87/upx-tamper-battery.py` sha256 `0f2d2bd8…4b0`, `.ufo/waves/round-87/pre/`).
- Repair candidate before dispatch (L1-authored, attacked by the wave): `b5c7a49e20647bb73117ed1ffb4f68dd69916cd8`.
- Wave spec and validated 11-seat dispatch: `1c8a76f41f340d575b707d597678efdfed0550c4`.
- Integration: `73c3a29740884b0c134bbe50e3c9b13f141daccf`. Repair with the ExecRepairCases 33-case selftest and mixed-method chains; SentinelR87 F1/F2/F3 hardening (best-candidate sentinel, memoised walk, rc 2 on non-regular or >256 MiB input); `tools/round-87/freeze-precheck.py` (M87-1); `tools/round-87/registry-opened-check.py` (M87-2); S306–S308; knowledge entry.
- Measurement at `73c3a297`: `.ufo/waves/round-87/l1/scores/c1-at-73c3a297.json`, `recovered 8 of 8`, exit 0.
- Record: `4136ac0cc6640829655c637ad016db530450b822`. PROVINCE `## Round-87 additions to Core`, README coverage row, knowledge row and frontier note, SKILL round-87 rule block and four registry rows, QUALITY rows 152–153, `corpus/lessons/round-87.md`, SCORECARD capability row and round-87 section, LOG, wave evidence and `r87-w1-results.json`.
- Before-state domain run (end-to-end RE task): `.ufo/waves/round-87/w1/ExecReaBefore/before.json`. The tampered jq/xxd/docker-init binaries run unchanged. REA 6.5.0 sees only the stub (3 procedures), or 98/184 on the `.so`, and gives identical counts on intact and tampered files. After repair: declared counts 167/99/184/1268.
- Decoy re-probe after hardening: `.ufo/waves/round-87/l1/decoy-probe-after-hardening.txt`. All four decoy cases now restore the real sentinel.

## Landed changes

| commit | carries | LOG.md entry |
|---|---|---|
| `f0ebf611` | declaration, counter, controls, census before | `## 2026-11-04 — round 87` (declared claim) |
| `b5c7a49e` | repair candidate | same entry (wave) |
| `1c8a76f4` | wave spec and dispatch | same entry (wave `r87-w1`) |
| `73c3a297` | integrated tools, S306–S308, knowledge entry | same entry (measured, sources, mistakes) |
| `4136ac0c` | record, Core move, lesson, QUALITY, SCORECARD, wave evidence | same entry |

## Before → after measurements

**R87-C1 (coverage).** Recovered 0 of 8 → 8 of 8.
- Counting command: `python3 -I -B tools/round-87/upx-tamper-battery.py --root . --repair-cmd tools/round-87/upx-magic-repair.py --upx /usr/bin/upx --pkg <rea-agents 6.5.0 dir> --work <scratch> --json-out <receipt>`.
- Measured against `73c3a29740884b0c134bbe50e3c9b13f141daccf`.
- Before (at the declaration `f0ebf611`): the do-nothing control `identity` scored `recovered 0 of 8`, exit 1. The cheap rule `naive-global` scored `recovered 4 of 8` with N1 false, exit 1.
- After: `recovered 8 of 8`. Controls: N1 4/4, N2 0/4 recovered, N3 4/4. Exit 0.
- REA counts after repair: jq 167/30/190, xxd 99/29/103, libz 184/29/199, docker-init 1268/29/1111.

**Verdict: met under the frozen predicate.** Disclosed weakenings:
- A chain-walk-free heuristic also reaches 8/8 (CriticClaim `receipts/cheap-v4-checksum-lite-rea.json`), so the plan's sentence "only a structural repair reaches" the zeroed class overstates what the counter forces (M87-3).
- `rea_recover` is entailed by `identity` (ReviewerRepair F1).
- The freeze precheck flagged the declaration container (M87-1 false findings, plus one genuine M87-4 finding).

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`.
  - Before: `kaidoku ok`, exit 0 (`.ufo/waves/round-87/pre/sources-census-before.txt`).
  - After: `kaidoku ok`, exit 0, 27 W04 warnings, all pre-existing (`.ufo/waves/round-87/l1/sources-census-after.txt`).
- Rows: 210 → 213 (`grep -c '^| S[0-9]' corpus/SOURCES.md`). Added by tier: A +3 (S306 linux.h, S307 p_lx_elf.cpp, S308 packhead.cpp). All three were opened 2026-11-04 and went absent → mined, with used-by set to the round-87 knowledge entry.
- `src/p_unix.cpp` was opened and rejected; no row was written (reason and flip condition are in the lesson Gate).
- Rows touched old→new: none other.
- Frontier rows advanced: one. The magic-altered anti-UPX class went Frontier → Core for 4 carriers, UPX 5.2.0 `--best`, LE x86-64.
- Sourced claim: the R87-C1 entry cites S306–S308.
- Mined mistakes M87-1..4 are in `corpus/lessons/round-87.md` `## Mistakes`, each fix shown able to fail. The new rows pass `registry-opened-check` (base `99f8b6a8` → `73c3a297`: clean).
- Assimilation: none (`merge/kaidoku/` was not consumed; no package entry was opened). `considerthese/`: this lane has no such directory.

## Trend verdicts

- **expansion: improved.** One Frontier class moved to Core with a working capability row (`UPX magic-tamper repair`). It is a new artifact-class edge (packer-tampered ELF), not apparatus. Three new tier-A sources were added.
- **quality: improved.** Both instrument defects were fixed with failing-before evidence:
  - the precheck `.json`→`.js` false finding;
  - registry rows without an opened document (red on round 86's S305).
  
  The repair was hardened against the wave's decoy and DoS findings before measurement. Limits are stated in the entry.
- **discernment: unchanged, pending non-author closure.**
  - Admit sample: S306 to S308.
  - Reject sample: p_unix.cpp.
  - The critic's falsified rationale is reported, not hidden.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: the round-87 UPX rule block in SKILL.md (symptom → action → status, citing the entry and S306–S308). There is no non-author verifier yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: tamper → REA before (stub) → repair → `upx -d` → pinned bytes → REA after (declared counts), at `.ufo/waves/round-87/w1/ExecReaBefore/before.json` and `.ufo/waves/round-87/l1/scores/c1-at-73c3a297.json`, logged in the LOG.md round-87 entry. A non-author verifier is still pending.
- [~] Instructions executable by an agent without oral context — evidence: the knowledge entry's command table and the SKILL registry rows with self-test commands.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: ConnectorR87's sibling-lane sweep found no sibling holding UPX/ELF repair ground (`.ufo/waves/round-87/w1/ConnectorR87/links.md` §2).

## Wave shape, seats and dead seats

- **Shape:** one v1 wave, `r87-w1`, 11 seats, validated under `ufo-wave-policy.json` (band 8–16). No residual call. Round total 11.
- **Roles:** scout 1, executor 3, scribe 2, reviewer 1, critic 1, mutation-tester 1, sentinel 1, connector 1. Attack share is 3/11 = 27 %.
- **Planner seat:** held by the L1 (the validator rejects `planner`).
- **Seat outcomes:** all 11 seats returned output and wrote DONE markers (`r87-w1-results.json`). Dead seats: 0.
- **Routing:** via `task.agentModelOverrides`, the amendment-9 map with every role on @m_mim. Per-seat models are not recorded in results.json.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Tool installs

None. No seat reported an install.

## Misroot sweep and inherited state

- `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows ` M .ufo/reports/round-84/kama.md` (another lane), `?? after` (dated 2026-11-03, not this round), and `.scratch/*` (orchestrator-owned). None were written by this round's seats, and none were touched.
- Lane: the untracked `.ready`/`.ready.dispatched` handoff markers for rounds 85–87 are orchestrator files and were left untracked, as in previous rounds.
- No `lane-dead-no-report kaidoku round=87` line was found, so there was no earlier attempt to inherit.
- Scratch `/fast/scratch/hyaku/kaidoku-r87` was removed.

## Open L0 question

None new. The round-86 L0 on operability ownership stays open and was routed around (this claim is on an owned axis).

## Routed to the next steered round

- Freeze the chain-walk-free heuristic as a second cheap-rule control (M87-3).
- Keep claimed artifacts outside counter-scanned claim strings (M87-4).
- Counter exit-contract fixes: an uncaught exception should not exit 1, and N1 should not count rc `None` as a refusal.
- Add cases for the repair's surviving guard mutants.
- Carried items: V86-6, V86-7, R85-4.
