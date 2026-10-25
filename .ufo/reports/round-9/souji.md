# souji — round 9 (adversarial hardening + differential + rubric)

Lane HEAD at report time: `455b1de2` (souji-shokunin identity). Single
batched dispatch: 24 seats on **openai-codex/gpt-6.1-sol-max**; 23/24.

## Round verdict: REJECTED — O1 NOT-MET (all four final judges)

The strongest model in the schedule red-teamed the lane's toolchain and
found **23 deduplicated defect classes**. K1 (differential) and C1
(rubric) verify within bounds; O1 (hardening) does not — patches landed
mid-round but fresh replays still reproduce unsafe deletions. Reported
as such; nothing forced; deletion authorization is OFF.

## What the round found (named classes, all fixture-confirmed)

Environment/hostility: git disappearing mid-run → false
`metadata-prune` zero-counts; `LANG=tr_TR` folding `ID_*` into
`ıd_*` bypassing secrets refusal. Authorization forgery: NUL bytes in
--list rows; tab-spliced pins; **ledger revocation after row capture**
(captured rows keep authorizing after the ledger goes header-only);
nested dirty/unpushed repositories deleted via ancestor receipts.
Stale-sweep blind spots: hidden live references missed; directory
staleness checking only parent metadata. Quarantine second-check missing
current default-ref/ancestry revalidation. git 2.55: linked-worktree
HEADs included in `--all` → `unique=0` wrong; owner names lacking
`-shokunin` hide registrations from scanning. Contract violation: both
"read-only" verifiers rewrite `.git/index`. Plus the parent's own drift:
SCORECARD rows (7/8) contradicted its saturation prose (6/7) —
corrected in this round's commit.

## State at closure (honest)

- **S17 patches applied** to all three verdict tools + shared selftest
  runner: selftests 40/51/91 (+census 32); the adjudicated S08 universe
  went 10→0 false-SAFE and 7→0 false-DELETE. **But** fresh S09/S10/S11
  replays against the patched tools still execute unauthorized deletions
  — **≥16 classes open** (S24's dedup). Tools are PATCHED-NOT-CERTIFIED:
  receipts are advisory; nothing quarantines for real until r10 closes
  the classes.
- **S18's candidate line** (`.r9-s18` variants + guard) passes its own
  37/37 battery but loses S17's NUL/ledger protections — banked for
  composition, not promotion (S24's merge guidance adopted).
- **Rubric banked**: `census/round-9/rubric-final.md` (S13-based merged
  scorer, 12/12 independent checks). Current axis scores are
  LEGACY-UNMAPPED; new scores UNRATED until tools freeze.
- **Dissent preserved**: `census/round-9/dissent-24.md` (rubric zeroing
  semantics; dirty-file SAFE interpretation).

## Landed changes

- S17 tool patches + `tools/souji-round9-selftest.sh`; S18 candidate
  variants; `census/round-9/` (24 fragments, fixes-17/18, rubric drafts
  + final, verifier-20, final-21..24, dissent-24); SCORECARD corrections
  + Tool-certification note; lessons; LOG — commit `455b1de2`.

## Before → after measurements

- O1: before — tools carried 23 latent defect classes → after: the
  adjudicated universe is clean and selftests grew 24→40, 35→51, 63→91,
  but the open-class set is ≥16 → NOT-MET, honest stop.
- K1: three independent 40-case corpora; contradiction taxonomy
  delivered (5 unsafe directional + benign refusals separated).
- C1: rubric prospective-spec delivered; 2 scorecard contradictions
  found and corrected.

## SHONEN

- [~] SKILL.md decision tables — the r9 defect taxonomy now defines what the tools must refuse.
- [~] End-to-end domain task — the fleet's first full adversarial audit of its own gates.
- [~] Executable without oral context — 23 zero-context seats, 214+ pinned regression assertions.
- [~] No cross-domain bleed — every attack was fixture-bound; live fleet untouched.
